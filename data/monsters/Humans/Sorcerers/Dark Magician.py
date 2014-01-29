
dark_magician = genMonster("Dark Magician", (133, 6080), "a dark magician")
dark_magician.setOutfit(69, 66, 69, 66) #needs addons
dark_magician.setHealth(325, healthmax=325)
dark_magician.bloodType("blood")
dark_magician.setDefense(armor=15, fire=0.9, earth=0.8, energy=0.8, ice=0.9, holy=0.8, death=1.05, physical=1, drown=1)
dark_magician.setExperience(185)
dark_magician.setSpeed(220)
dark_magician.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=80)
dark_magician.walkAround(energy=1, fire=1, poison=1)
dark_magician.setImmunity(paralyze=0, invisible=1, lifedrain=1, drunk=0)
dark_magician.voices("Feel the power of my runes!", "Killing you gets expensive!", "My secrets are mine alone!", "Stand still!")
dark_magician.regMelee(30)
dark_magician.loot( (2148, 100, 55), ("strong mana potion", 3.75), ("blank rune", 9.25), ("mana potion", 12.25), (7762, 0.75), ("health potion", 12.25), ("strong health potion", 2.75), ("necrotic rod", 0.25), ("reins", 0.0025) )