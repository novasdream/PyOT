Infected_Weeper = genMonster("Infected Weeper", (489, 15906), "an infected weeper") #mostly unknown
Infected_Weeper.setHealth(6800)
Infected_Weeper.bloodType("blood")
Infected_Weeper.setDefense(armor=20, fire=1, earth=1, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
Infected_Weeper.setExperience(4800)
Infected_Weeper.setSpeed(500)
Infected_Weeper.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
Infected_Weeper.walkAround(energy=0, fire=0, poison=0)
Infected_Weeper.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
Infected_Weeper.summon("Parasite", 10)
Infected_Weeper.maxSummons(1)
Infected_Weeper.voices("Moooaaan")
Infected_Weeper.regMelee(200)