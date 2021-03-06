
orc_warrior = genMonster("Orc Warrior", (7, 5979), "an orc warrior")
orc_warrior.setHealth(125)
orc_warrior.bloodType("blood")
orc_warrior.setDefense(armor=17, fire=1, earth=1.1, energy=0.7, ice=1, holy=0.9, death=1.1, physical=1, drown=1)
orc_warrior.setExperience(50)
orc_warrior.setSpeed(190)
orc_warrior.setBehavior(summonable=360, hostile=1, illusionable=1, convinceable=360, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=11)
orc_warrior.walkAround(energy=1, fire=1, poison=1)
orc_warrior.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
orc_warrior.voices("Alk!", "Trak grrrr brik.", "Grow truk grrrr.")
orc_warrior.regMelee(60)
orc_warrior.loot( (2148, 100, 15), ("meat", 15.75), ("chain armor", 7.25), ("skull belt", 1.25), ("orc tooth", 0.75), ("orc leather", 4.0), ("broken helmet", 10.25), ("copper shield", 0.5), ("poison dagger", 0.0025) )