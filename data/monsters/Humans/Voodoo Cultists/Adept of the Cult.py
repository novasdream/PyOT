adept_of_the_cult = genMonster("Adept of the Cult", (194, 6080), "an adept of the cult")
adept_of_the_cult.setOutfit(114, 94, 94, 57)
adept_of_the_cult.setHealth(430)
adept_of_the_cult.bloodType("blood")
adept_of_the_cult.setDefense(armor=35, fire=1, earth=0.6, energy=1.05, ice=0.8, holy=0.7, death=1.05, physical=1, drown=1)
adept_of_the_cult.setExperience(400)
adept_of_the_cult.setSpeed(210)
adept_of_the_cult.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=0)
adept_of_the_cult.walkAround(energy=1, fire=1, poison=1)
adept_of_the_cult.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
adept_of_the_cult.summon("Ghoul", 10)
adept_of_the_cult.maxSummons(2)
adept_of_the_cult.voices("Feel the power of the cult!", "Praise the voodoo!", "Power to the cult!")
adept_of_the_cult.regMelee(90, condition=CountdownCondition(CONDITION_POISON, 2), conditionChance=100)