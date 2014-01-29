armadile = genMonster("Armadile", (487, 18378), "an armadile")
armadile.setHealth(3800, healthmax=3800)
armadile.bloodType("blood")
armadile.setDefense(armor=30, fire=0.80, earth=0, energy=0.85, ice=0.85, holy=0.85, death=1, physical=0.95, drown=1)
armadile.setExperience(2900)
armadile.setSpeed(350)
armadile.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
armadile.walkAround(energy=0, fire=1, poison=0)
armadile.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
armadile.voices("Creak!")
armadile.regMelee(400)