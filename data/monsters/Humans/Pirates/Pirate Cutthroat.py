pirate_cutthroat = genMonster("Pirate Cutthroat", (96, 6080), "a pirate cutthroat")
pirate_cutthroat.setHealth(325)
pirate_cutthroat.bloodType("blood")
pirate_cutthroat.setDefense(armor=15, fire=1.05, earth=0.9, energy=1, ice=0.95, holy=0.8, death=1.05, physical=1, drown=1)
pirate_cutthroat.setExperience(175)
pirate_cutthroat.setSpeed(230)
pirate_cutthroat.setBehavior(summonable=0, hostile=2, illusionable=1, convinceable=495, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=20, targetChange=0)
pirate_cutthroat.walkAround(energy=1, fire=1, poison=1)
pirate_cutthroat.setImmunity(paralyze=1, invisible=0, lifedrain=1, drunk=1)
pirate_cutthroat.voices("Give up!", "Plundeeeeer!", "Hiyaa!")
pirate_cutthroat.regMelee(175)#+poison
pirate_cutthroat.loot( (2148, 100, 50), ("light shovel", 2.0), ("compass", 9.75), ("pirate bag", 1.0), ("steel shield", 3.0), ("treasure map", 1.0), ("scale armor", 2.75), ("eye patch", 0.5), ("pirate knee breeches", 1.0), ("peg leg", 0.5), ("hook", 0.5, 3), ("rum flask", 0.0025), ("dice", 0.0025), ("very old piece of paper", 0.0025) )