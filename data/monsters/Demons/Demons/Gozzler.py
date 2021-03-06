gozzler = genMonster("Gozzler", (8, 5980), "a gozzler")
gozzler.setHealth(240, healthmax=240)
gozzler.bloodType("blood")
gozzler.setDefense(armor=26, fire=1, earth=1, energy=1, ice=1, holy=0.5, death=0.5, physical=1.05, drown=1)
gozzler.setExperience(180)
gozzler.setSpeed(260)
gozzler.setBehavior(summonable=800, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
gozzler.walkAround(energy=1, fire=1, poison=1)
gozzler.setImmunity(paralyze=0, invisible=1, lifedrain=0, drunk=0)
gozzler.voices("Huhuhuhuuu!", "Let the fun begin!", "Yihahaha!", "I'll bite you! Nyehehehe!", "Nyarnyarnyarnyar.")
gozzler.regMelee(110)
gozzler.loot( ("sabre", 8.0), ("brown flask", 9.0), (2148, 100, 70), ("battle axe", 2.75), ("morning star", 5.0), ("plate shield", 10.0), ("clerical mace", 0.75), ("small sapphire", 0.25), ("dwarven ring", 0.25), ("serpent sword", 0.25) )