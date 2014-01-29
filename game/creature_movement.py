from game.map import placeCreature, removeCreature, getTile
from twisted.python import log
import config

class CreatureMovement(object):
    def stepDuration(self, ground):
        if not ground.speed:
            return (100.0 / self.speed) #- 0.05

        return (ground.speed / self.speed) #- 0.05
    
    def teleport(self, position, force=False):
        """if not self.actionLock(self.teleport, position):
            return False"""

        
        # 4 steps, remove item (creature), send new map and cords, and effects
        oldPosition = self.position.copy()

        newTile = getTile(position)
        oldPosCreatures = set()
        if not newTile:
            raise game.errors.SolidTile("Tile doesn't exist") # Yea, it's fatal, even in force mode!
        
        if not force:
            for i in newTile.getItems():
                if i.solid:
                    raise game.errors.SolidTile()

        invisible = self.isMonster() and self.hasCondition(CONDITION_INVISIBLE)

        oldStackpos = 0
        if not invisible:
            try:
                oldStackpos = getTile(oldPosition).findStackpos(self)
                for spectator in getSpectators(oldPosition, ignore=(self,)):
                    stream = spectator.packet()
                    stream.removeTileItem(oldPosition, oldStackpos)
                    stream.magicEffect(oldPosition, 0x02)
                    stream.send(spectator)
                oldPosCreatures = getCreatures(oldPosition)
            except:
                pass # Just append creature
        
        stackpos = placeCreature(self, position)
        if not stackpos:
            raise game.errors.ImpossibleMove()
        
        removeCreature(self, oldPosition)
        
        if self.creatureType == 0 and self.client:
            print "Good"
            with self.packet() as stream:
                if oldStackpos: 
                   stream.removeTileItem(oldPosition, oldStackpos)
                
                stream.uint8(0x64)
                stream.position(position)
                stream.mapDescription(Position(position.x - 8, position.y - 6, position.z), 18, 14, self)

                # If we're entering protected zone, fix icons
                pzStatus = newTile.getFlags() & TILEFLAGS_PROTECTIONZONE
                pzIcon = self.extraIcons & CONDITION_PROTECTIONZONE
                if pzStatus and not pzIcon:
                    self.setIcon(CONDITION_PROTECTIONZONE)
                    self.refreshConditions(stream)
                    self.cancelTarget(stream)
                    self.target = None
                    if self.isPlayer() and self.mounted:
                        callLater(0, self.changeMountStatus, False)

                elif not pzStatus and pzIcon:
                    self.removeIcon(CONDITION_PROTECTIONZONE)
                    self.refreshConditions(stream)

                #stream.magicEffect(position, 0x02)

        self.position = position        
        newPosCreatures = getCreatures(position)
        disappearFrom = oldPosCreatures - newPosCreatures
        appearTo = newPosCreatures - oldPosCreatures
        for creature2 in disappearFrom:
            game.scriptsystem.get('disappear').runSync(creature2, self)

        for creature2 in appearTo:
            game.scriptsystem.get('appear').runSync(creature2, self)


        if not invisible:
            for spectator in getSpectators(position, ignore=(self,)):
                stream = spectator.packet()
                stream.addTileCreature(position, stackpos, self, spectator.player)
                stream.magicEffect(position, 0x02)
                stream.send(spectator)

        if self.target and not self.canSee(self.target.position):
            self.cancelTarget()
            self.target = None
            self.targetMode = 0
            
        # Stairhop delay
        if self.isPlayer():
            self.lastStairHop = time.time()
            if self.target and not self.canSee(self.target.position):
                self.cancelTarget()
            
    def turn(self, direction):
        assert direction < 4
        if self.direction == direction:
            return

        if not self.alive: #or not self.actionLock(self.turn, direction):
            return

        self.direction = direction
        self.lastAction = time.time() + 0.15

        # Make package
        for spectator in getSpectators(self.position):
            stream = spectator.packet(0x6B)
            stream.position(self.position)
            stream.uint8(getTile(self.position).findStackpos(self))
            stream.uint16(0x63)
            stream.uint32(self.clientId())
            stream.uint8(direction)
            if spectator.version >= 953:
                stream.uint8(self.solid)
            stream.send(spectator)

    def reverseDirection(self):
        """ Used by pushing """

        direction = self.direction
        if direction == NORTH:
            return SOUTH
        elif direction == SOUTH:
            return NORTH
        elif direction == EAST:
            return WEST
        elif direction == WEST:
            return EAST

    def directionToPosition(self, position, diagonal=False):
        direction = None
        if diagonal:
            if position.y > self.position.y and position.x > self.position.x:
                return SOUTHEAST
            elif position.y > self.position.y and position.x < self.position.x:
                return SOUTHWEST
            elif position.y < self.position.y and position.x > self.position.x:
                return NORTHEAST
            elif position.y < self.position.y and position.x < self.position.x:
                return NORTHWEST

        # First north/south
        if position.y > self.position.y:
            direction = SOUTH
            
        elif position.y < self.position.y:
            direction = NORTH
            
        if position.x > self.position.x:
            direction = EAST

        elif position.x < self.position.x:
            direction = WEST

        return direction

    def turnAgainst(self, position):
        return self.turn(self.directionToPosition(position))
    
    def verifyMove(self, tile):
        """ This function verify if the tile is walkable in a regular state (pathfinder etc) """
        return True

    def clearMove(self, direction, failback):
        self.cancelWalk(direction % 4)
        self.walkPattern = []
        if failback: reactor.callLater(0, failback)
        return False
        
    def move(self, direction, spectators=None, level=0, stopIfLock=False, callback=None, failback=None, push=True):
        if not self.alive or not self.actionLock(self.move, direction, spectators, level, stopIfLock, callback, failback, push):
            return

        if not self.data["health"] or not self.canMove or not self.speed:
            return False

        oldPosition = self.position.copy()

        # Drunk?
        if self.hasCondition(CONDITION_DRUNK):
            directions = [0,1,2,3,4,5,6,7,direction] # Double the odds of getting the correct direction.
            directions.remove(self.reverseDirection()) # From a reality perspective, you are rarely that drunk.
            direction = random.choice([0,1,2,3,4,5,6,7,direction])

        # Recalculate position
        position = oldPosition.copy()
        if direction == 0:
            position.y -= 1
        elif direction == 1:
            position.x += 1
        elif direction == 2:
            position.y += 1
        elif direction == 3:
            position.x -= 1
        elif direction == 4:
            position.y += 1
            position.x -= 1
        elif direction == 5:
            position.y += 1
            position.x += 1
        elif direction == 6:
            position.y -= 1
            position.x -= 1
        elif direction == 7:
            position.y -= 1
            position.x += 1

        position.z += level
            
        # We don't walk out of the map!
        if position.x < 1 or position.y < 1 or position.x > game.map.mapInfo.width or position.y > game.map.mapInfo.height:
            self.cancelWalk()
            return

        # New Tile
        newTile = getTile(position)
        
        if not newTile:
            return self.clearMove(direction, failback)
        
        # oldTile
        oldTile = getTile(oldPosition)
        if not oldTile:
            # This always raise
            raise Exception("(old)Tile not found (%s). This shouldn't happend!" % oldPosition)

        val = game.scriptsystem.get("move").runSync(self)
        if val == False:
            return self.clearMove(direction, failback)

        try:
            oldStackpos = oldTile.findStackpos(self)
        except:
            return self.clearMove(direction, failback)

        # Deal with walkOff
        for item in oldTile.getItems():
            game.scriptsystem.get('walkOff').runSync(item, self, None, position=oldPosition)

        # Deal with preWalkOn
        for item in newTile.getItems():
            r = game.scriptsystem.get('preWalkOn').runSync(item, self, None, oldTile=oldTile, newTile=newTile, position=position)
            if r == False:
                return self.clearMove(direction, failback)

        # PZ blocked?
        if (self.hasCondition(CONDITION_PZBLOCK) or self.getSkull() in SKULL_JUSTIFIED) and newTile.getFlags() & TILEFLAGS_PROTECTIONZONE:
            self.lmessage("You are PZ blocked")
            return self.clearMove(direction, failback)
            
        if newTile.ground.solid:
            self.notPossible()
            return self.clearMove(direction, failback)

        if newTile.things:
            for thing in newTile.things:
                if not self.isPlayer() and isinstance(thing, Item) and thing.teleport:
                    return self.clearMove(direction, failback)

                if thing.solid:
                    if level and isinstance(thing, Creature):
                        continue

                    # Monsters might push. This should probably be a preWalkOn event, but well. Consider this a todo for v1.1 or something.
                    if push and isinstance(thing, Monster) and self.isMonster() and self.base.pushCreatures and thing.base.pushable:
                        # Push stuff here.

                        # Clear up the creatures actions.
                        thing.stopAction()
                        thing.clearMove(direction, failback)

                        if thing.move(thing.reverseDirection(), stopIfLock=True, push=False):
                            # We "must" break here. Assume the tile is good since another creature is on it. Iterator might be invalid at this point.
                            break
                        elif self.base.hostile and thing.isAttackable(self):
                            # We can attack the creature.
                            self.target = thing
                            self.targetMode = 1

                            # Deliver final blow.
                            thing.onHit(self, -thing.data['healthmax'], PHYSICAL)

                    #self.turn(direction) # Fix me?
                    self.notPossible()
                    return self.clearMove(direction, failback)

        _time = time.time()
        self.lastStep = _time
        delay = self.stepDuration(newTile.ground) * (config.diagonalWalkCost if direction > 3 else 1)
        self.lastAction = _time + delay

        newStackPos = newTile.placeCreature(self)
        oldTile.removeCreature(self)

        # Weird #112 issue. Hack fix.
        if self in oldTile.things:
            while True:
                if self not in oldTile.things: break
                oldTile.removeCreature(self)

        # Clear target if we change level
        if level:
            self.cancelTarget()
            self.target = None
            self.targetMode = 0


        # Send to Player
        if self.isPlayer():
            # Mark for save
            self.saveData = True

            ignore = (self,)
            stream = self.packet()

            if (oldPosition.z != 7 or position.z < 8): # Only as long as it's not 7->8 or 8->7
                #stream = spectator.packet(0x6D)
                stream.uint8(0x6D)
                stream.position(oldPosition)
                stream.uint8(oldStackpos)
                stream.position(position)
            else:
                stream.removeTileItem(oldPosition, oldStackpos)

            # Levels
            if oldPosition.z > position.z:
                stream.moveUpPlayer(self, oldPosition)

            elif oldPosition.z < position.z:
                stream.moveDownPlayer(self, oldPosition)

            # Y movements
            if oldPosition.y > position.y:
                stream.uint8(0x65)
                stream.mapDescription(Position(oldPosition.x - 8, position.y - 6, position.z), 18, 1, self)
            elif oldPosition.y < position.y:
                stream.uint8(0x67)
                stream.mapDescription(Position(oldPosition.x - 8, position.y + 7, position.z), 18, 1, self)

            # X movements
            if oldPosition.x < position.x:
                stream.uint8(0x66)
                stream.mapDescription(Position(position.x + 9, position.y - 6, position.z), 1, 14, self)
            elif oldPosition.x > position.x:
                stream.uint8(0x68)
                stream.mapDescription(Position(position.x - 8, position.y - 6, position.z), 1, 14, self)

            # If we're entering protected zone, fix icons
            pzStatus = newTile.getFlags() & TILEFLAGS_PROTECTIONZONE
            pzIcon = self.extraIcons & CONDITION_PROTECTIONZONE
            if pzStatus and not pzIcon:
                self.setIcon(CONDITION_PROTECTIONZONE)
                self.refreshConditions(stream)
                if not level:
                    self.cancelTarget(stream)
                    self.target = None
                if self.isPlayer() and self.mounted:
                    callLater(0, self.changeMountStatus, False) # This should be sent after the move is completed, I believe.

            elif not pzStatus and pzIcon:
                self.removeIcon(CONDITION_PROTECTIONZONE)
                self.refreshConditions(stream)


            stream.send(self.client)
            
        else:
            ignore = ()
            
        self.position = position
        self.direction = direction % 4
        
        oldPosCreatures = getPlayers(oldPosition, ignore=ignore)
        newPosCreatures = getPlayers(position, ignore=ignore)
        spectators = oldPosCreatures|newPosCreatures
        invisible = self.isMonster() and self.hasCondition(CONDITION_INVISIBLE)

        for spectator in spectators:
            # Make packet
            if not spectator.client or invisible:
                continue

            canSeeNew = spectator in newPosCreatures
            if canSeeNew:
                assert spectator.canSee(position)
            canSeeOld = spectator in oldPosCreatures
            if canSeeOld:
                assert spectator.canSee(oldPosition)
            stream = spectator.packet()

            if not canSeeOld and canSeeNew:
                stream.addTileCreature(position, newStackPos, self, spectator, resend=True)

            elif canSeeOld and not canSeeNew:
                stream.removeTileItem(oldPosition, oldStackpos)
                """spectator.knownCreatures.remove(self)
                self.knownBy.remove(spectator)"""

            elif canSeeOld and canSeeNew:
                if (oldPosition.z != 7 or position.z < 8) and oldStackpos < 10: # Only as long as it's not 7->8 or 8->7

                    stream.uint8(0x6D)
                    stream.position(oldPosition)
                    stream.uint8(oldStackpos)
                    stream.position(position)

                else:
                    stream.removeTileItem(oldPosition, oldStackpos)
                    spectator.knownCreatures.remove(self)
                    self.knownBy.remove(spectator)
                    stream.addTileCreature(position, newStackPos, self, spectator)
            stream.send(spectator.client)

        if self.scripts["onNextStep"]:
            scripts = self.scripts["onNextStep"][:]
            self.scripts["onNextStep"] = []
            for script in scripts:
                script(self)

        # Deal with walkOn
        for item in newTile.getItems(): # Scripts
            game.scriptsystem.get('walkOn').runDeferNoReturn(item, self, None, position=position, fromPosition=oldPosition)
            if item.teledest:
                try:
                    self.teleport(Position(item.teledest[0], item.teledest[1], item.teledest[2]), self.position.instanceId)
                    self.magicEffect(EFFECT_TELEPORT)
                except:
                    log.msg("%d (%s) got a invalid teledist (%s), remove it!" % (item.itemId, item, item.teledest))
                    del item.teledest

        # Deal with appear and disappear. Ahh the power of sets :)
        disappearFrom = oldPosCreatures - newPosCreatures
        appearTo = newPosCreatures - oldPosCreatures
        for creature2 in disappearFrom:
            game.scriptsystem.get('disappear').runDeferNoReturn(creature2, self)
            game.scriptsystem.get('disappear').runDeferNoReturn(self, creature2)

        for creature2 in appearTo:
            game.scriptsystem.get('appear').runDeferNoReturn(creature2, self)
            game.scriptsystem.get('appear').runDeferNoReturn(self, creature2)

        # Stairhop delay
        if level and self.isPlayer():
            self.lastStairHop = time.time()

        if self.isPlayer() and self.target and not self.canSee(self.target.position):
            self.cancelTarget()
           
        if callback: reactor.callLater(0, callback)
        return True
