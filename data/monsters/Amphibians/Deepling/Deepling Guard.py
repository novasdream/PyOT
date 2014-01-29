Deepling_Guard = genMonster("Deepling Guard", (442, 15175), "a deepling guard")
Deepling_Guard.setHealth(1900, healthmax=1900 )
Deepling_Guard.bloodType("blood")
Deepling_Guard.setDefense(armor=1, fire=0, earth=1.1, energy=1.1, ice=0, holy=1, death=0.9, physical=1, drown=1)
Deepling_Guard.setExperience(2100)
Deepling_Guard.setSpeed(300) #unknown
Deepling_Guard.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=20)
Deepling_Guard.walkAround(energy=1, fire=0, poison=1)
Deepling_Guard.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
Deepling_Guard.voices("QJELL NETA NA!!")

Deepling_Guard.regMelee(400)
Deepling_Guard.regDistance(350, ANIMATION_SPEAR, chance(21))
Deepling_Guard.regSelfSpell("Light Healing", 100, 200, check=chance(20)) #strength?