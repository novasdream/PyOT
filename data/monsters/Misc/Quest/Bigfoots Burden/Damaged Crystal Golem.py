damaged_crystal_golem = genMonster("Damaged Crystal Golem", (508, 18466), "a damaged crystal golem")  #unknown blood, heal 10
damaged_crystal_golem.setHealth(500, healthmax=500)
damaged_crystal_golem.bloodType("blood")
damaged_crystal_golem.setDefense(armor=30, fire=0, earth=1, energy=1, ice=0, holy=1, death=1, physical=0.8, drown=1)
damaged_crystal_golem.setExperience(0)
damaged_crystal_golem.setSpeed(350)
damaged_crystal_golem.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=500)
damaged_crystal_golem.walkAround(energy=0, fire=0, poison=0)
damaged_crystal_golem.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
damaged_crystal_golem.regMelee(150)