
minotaur_guard = genMonster("Minotaur Guard", (29, 5983), "a minotaur guard")
minotaur_guard.setHealth(185)
minotaur_guard.bloodType("blood")
minotaur_guard.setDefense(armor=15, fire=0.8, earth=1, energy=1, ice=1.1, holy=0.9, death=1.1, physical=1, drown=1)
minotaur_guard.setExperience(160)
minotaur_guard.setSpeed(190)
minotaur_guard.setBehavior(summonable=550, hostile=1, illusionable=1, convinceable=550, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
minotaur_guard.walkAround(energy=1, fire=1, poison=1)
minotaur_guard.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
minotaur_guard.voices("Kirrl Karrrl!", "Kaplar")
minotaur_guard.regMelee(100)
minotaur_guard.loot( (2148, 100, 20), ("minotaur horn", 10.25, 2), ("chain armor", 2.75), ("brass armor", 3.75), ("piece of warrior armor", 5.5), ("battle shield", 2.0), ("minotaur leather", 1.0, 3), ("double axe", 0.5), ("health potion", 0.25), ("fishing rod", 0.75), ("minotaur trophy", 0.25) )