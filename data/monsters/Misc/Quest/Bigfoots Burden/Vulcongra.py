Vulcongra = genMonster("Vulcongra", (509, 16185), "a vulcongra") #mostly unknown
Vulcongra.setHealth(1600)
Vulcongra.bloodType("blood")
Vulcongra.setDefense(armor=45, fire=0, earth=0, energy=1, ice=1.15, holy=1, death=0.95 physical=1, drown=1.1)
Vulcongra.setExperience(1100)
Vulcongra.setSpeed(400)
Vulcongra.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
Vulcongra.walkAround(energy=0, fire=0, poison=0)
Vulcongra.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
Vulcongra.voices("Fuchah!", "Fuchah! Fuchah!", "Yag! Yag! Yag!")
Vulcongra.regMelee(230)