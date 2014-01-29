hive_overseer = genMonster("Hive Overseer", (458, 15354), "a hive overseer")
hive_overseer.setHealth(7500, healthmax=7500)
hive_overseer.bloodType("slime")
hive_overseer.setDefense(armor=75, fire=0.3, earth=0, energy=0.8, ice=1, holy=0.9, death=1, physical=0.4, drown=1)
hive_overseer.setExperience(100) # XXX: Wrong, just to fix loading
hive_overseer.setSpeed(100) # XXX: Wrong, just to fix loading
hive_overseer.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
hive_overseer.walkAround(energy=0, fire=0, poison=0)
hive_overseer.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
hive_overseer.summon("Spidris Elite", 10)
hive_overseer.maxSummons(2)
hive_overseer.voices("Zopp!", "Kropp!")
hive_overseer.regMelee(450)