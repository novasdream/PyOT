# bad
Slug = genMonster("Slug", (407, 6079), "a slug") # not right yet
Slug.setTargetChance(10)
Slug.bloodType("blood")
Slug.setHealth(255)
Slug.setExperience(70)
Slug.setSpeed(200) #incorrect
Slug.walkAround(1,1,1) # energy, fire, poison
Slug.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=0)
Slug.setImmunity(0,0,0) # paralyze, invisible, lifedrain
Slug.setDefense(9, fire=1.0, earth=1.0, energy=1.0, ice=1.0, holy=1.0, death=1.0, physical=1.0, drown=1.0)
Slug.loot( ('gold coin', 62.5, 40), ('worm', 5, 3) )
Slug.regMelee(45)