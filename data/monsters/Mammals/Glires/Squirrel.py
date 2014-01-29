Squirrel = genMonster("Squirrel", (274, 7628), "a squirrel")
Squirrel.setTargetChance(0)
Squirrel.bloodType("blood")
Squirrel.setHealth(20)
Squirrel.setExperience(0)
Squirrel.setSpeed(200) #incorrect
Squirrel.walkAround(1,1,1) # energy, fire, poison
Squirrel.setBehavior(summonable=220, hostile=0, illusionable=1, convinceable=220, pushable=1, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=20)
Squirrel.voices("Chchch")
Squirrel.setImmunity(0,0,0) # paralyze, invisible, lifedrain
Squirrel.setDefense(1, fire=1.0, earth=1.0, energy=1.0, ice=1.0, holy=1.0, death=1.0, physical=1.0, drown=1.0)
Squirrel.loot( ("acorn", 51.25), ("walnut", 0.5), ("peanut", 1.5) )