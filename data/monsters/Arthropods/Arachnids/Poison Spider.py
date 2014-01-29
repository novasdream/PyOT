poison_spider = genMonster("Poison Spider", (36, 5974), "a poison spider")
poison_spider.setHealth(26)
poison_spider.bloodType("slime")
poison_spider.setDefense(armor=2, fire=1.1, earth=0, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
poison_spider.setExperience(22)
poison_spider.setSpeed(160)#incorrect speed
poison_spider.setBehavior(summonable=270, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=6)
poison_spider.walkAround(energy=1, fire=1, poison=0)
poison_spider.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
poison_spider.loot( (2148, 61.25, 4), ("poison spider shell", 1.25) )

poison_spider.regMelee(20, condition=CountdownCondition(CONDITION_POISON, 2), conditionChance=100)