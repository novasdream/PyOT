wasp = genMonster("Wasp", (44, 5989), "a wasp")
wasp.setHealth(35)
wasp.bloodType("slime")
wasp.setDefense(armor=4, fire=1.1, earth=0, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
wasp.setExperience(24)
wasp.setSpeed(460)
wasp.setBehavior(summonable=280, hostile=1, illusionable=1, convinceable=0, pushable=1, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=0)
wasp.walkAround(energy=1, fire=1, poison=0)
wasp.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
wasp.voices("Bssssss")
wasp.regMelee(20)#plus poison
wasp.loot( ("honeycomb", 3.0, 3) )