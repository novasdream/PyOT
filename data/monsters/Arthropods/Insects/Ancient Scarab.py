ancient_scarab = genMonster("Ancient Scarab", (79, 6021), "an ancient scarab")
ancient_scarab.setHealth(1000)
ancient_scarab.bloodType("blood")
ancient_scarab.setDefense(armor=40, fire=1.2, earth=0, energy=0.8, ice=1.05, holy=1, death=1, physical=0.9, drown=1)
ancient_scarab.setExperience(720)
ancient_scarab.setSpeed(330)
ancient_scarab.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
ancient_scarab.walkAround(energy=1, fire=1, poison=0)
ancient_scarab.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
ancient_scarab.summon("larva", 10)
ancient_scarab.maxSummons(3)
ancient_scarab.regMelee(210)
ancient_scarab.loot( (2148, 100, 186), ("plate armor", 10.75), ("scarab shield", 0.5), ("scarab coin", 7.0, 2), (2162, 10.75), ("small amethyst", 3.0, 4), ("scarab pincers", 4.25), ("ancient amulet", 1.0), ("strong health potion", 0.5), ("terra hood", 0.25), ("small emerald", 1.0, 3), ("scarab amulet", 0.75), ("daramanian waraxe", 0.25) )