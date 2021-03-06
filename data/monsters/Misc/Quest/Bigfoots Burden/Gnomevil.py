Gnomevil = genMonster("Gnomevil", (493, 16149), "a gnomevil")
Gnomevil.setOutfit(95, 95, 95, 95)
Gnomevil.setAddons(0)
Gnomevil.setHealth(250000)
Gnomevil.bloodType("blood")
Gnomevil.setDefense(armor=100, fire=0.5, earth=0, energy=0, ice=0.5, holy=0.5, death=0.7, physical=0.85, drown=0.9)
Gnomevil.setExperience(40000)
Gnomevil.setSpeed(700)
Gnomevil.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
Gnomevil.walkAround(energy=0, fire=0, poison=0)
Gnomevil.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
Gnomevil.voices("No more Mr. Nicegnome!", "Taste the power of the dark side!", "I've seen the light! And it was all engulfing fire!")
Gnomevil.regMelee(750)