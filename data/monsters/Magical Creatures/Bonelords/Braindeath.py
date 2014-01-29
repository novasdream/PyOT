Braindeath = genMonster("Braindeath", (226, 6079), "a Braindeath")
Braindeath.setTargetChance(10)
Braindeath.bloodType("blood")
Braindeath.setHealth(1225)
Braindeath.setExperience(985)
Braindeath.setSpeed(200) # not correct
Braindeath.walkAround(0,0,0) # energy, fire, poison
Braindeath.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=0)
Braindeath.voices("You have disturbed my thoughts!", "Let me turn you into smething more useful!", "Let me taste your brain!", "You will be punished!")
Braindeath.setImmunity(1,1,1) # paralyze, invisible, lifedrain
Braindeath.setDefense(13, fire=1.15, earth=0, energy=0.9, ice=0.8, holy=1.2, death=0.85, physical=0.85, drown=1.0)
Braindeath.summon("Vampire", 10)
Braindeath.maxSummons(2)
Braindeath.regMelee(100)
Braindeath.loot( ("clerical mace", 2.25), ("piece of dead brain", 4.5), ("bone sword", 16.0), ("sniper arrow", 16.25, 4), ("bonelord eye", 2.25), ("steel shield", 5.75), (2148, 100, 88), ("haunted blade", 1.0), ("spellbook", 0.75), ("bonelord shield", 0.25), ("bonelord helmet", 0.25) )