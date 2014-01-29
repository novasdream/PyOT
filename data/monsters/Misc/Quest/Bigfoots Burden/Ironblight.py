Ironblight = genMonster("Ironblight", (498, 16079), "an ironblight")
Ironblight.setHealth(6600)
Ironblight.bloodType("blood")
Ironblight.setDefense(armor=20, fire=0.4, earth=0, energy=0.75, ice=0.8, holy=1, death=0.6, physical=0.85, drown=1)
Ironblight.setExperience(4400)
Ironblight.setSpeed(500)
Ironblight.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
Ironblight.walkAround(energy=0, fire=0, poison=0)
Ironblight.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
Ironblight.voices("Yowl!", "Clonk!")
Ironblight.regMelee(150)