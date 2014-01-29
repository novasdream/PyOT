scorpion = genMonster("Scorpion", (43, 5988), "a scorpion")
scorpion.setHealth(45, healthmax=45)
scorpion.bloodType("slime")
scorpion.setDefense(armor=15, fire=1.1, earth=0, energy=0.8, ice=1.1, holy=1, death=1, physical=1, drown=1)
scorpion.setExperience(45)
scorpion.setSpeed(150)
scorpion.setBehavior(summonable=310, hostile=1, illusionable=1, convinceable=0, pushable=1, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=5)
scorpion.walkAround(energy=1, fire=1, poison=0)
scorpion.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
scorpion.loot( ("scorpion tail", 4.75) )

scorpion.regMelee(50) #poison always up to 18~