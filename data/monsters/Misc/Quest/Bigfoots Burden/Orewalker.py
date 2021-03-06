Orewalker = genMonster("Orewalker", (490, 15910), "a Orewalker") #mostly unknown
Orewalker.setHealth(7200)
Orewalker.bloodType("blood")
Orewalker.setDefense(armor=1, fire=0.35, earth=0, energy=1.05, ice=0.95, holy=1, death=0.75, physical=0.75, drown=0.95)
Orewalker.setExperience(4800)
Orewalker.setSpeed(600)
Orewalker.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
Orewalker.walkAround(energy=0, fire=0, poison=0)
Orewalker.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
Orewalker.summon("Orewalker", 10)
Orewalker.maxSummons(0)
Orewalker.voices(CLONK!")
Orewalker.regMelee(350)