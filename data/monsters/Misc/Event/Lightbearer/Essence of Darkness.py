#mostly incorrect?
essence_of_darkness = genMonster("Essence Of Darkness", (315, 9960), "an essence of darkness")
essence_of_darkness.setHealth(1000) #or more
essence_of_darkness.bloodType("undead")
essence_of_darkness.setDefense(armor=10, fire=0.02, earth=0, energy=0, ice=0, holy=0.8, death=0, physical=0, drown=1)
essence_of_darkness.setExperience(30)
essence_of_darkness.setSpeed(230)
essence_of_darkness.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=0, targetDistance=1, runOnHealth=0)
essence_of_darkness.walkAround(energy=1, fire=1, poison=0)
essence_of_darkness.setImmunity(paralyze=0, invisible=0, lifedrain=1, drunk=1)