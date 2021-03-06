lizard_legionnaire = genMonster("Lizard Legionnaire", (338, 11276), "a lizard legionnaire")
lizard_legionnaire.setHealth(1400)
lizard_legionnaire.bloodType("blood")
lizard_legionnaire.setDefense(armor=32, fire=0.55, earth=0, energy=1, ice=1.1, holy=1, death=1, physical=1, drown=1)
lizard_legionnaire.setExperience(1100)
lizard_legionnaire.setSpeed(220)
lizard_legionnaire.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=10)
lizard_legionnaire.walkAround(energy=0, fire=0, poison=0)
lizard_legionnaire.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
lizard_legionnaire.voices("Tssss!")
lizard_legionnaire.regMelee(180)
lizard_legionnaire.loot( ("legionnaire flags", 2.0), ("lizard scale", 1.0, 3), ("zaoan halberd", 1.0), ("strong health potion", 4.0), ("broken halberd", 14.75), (2148, 100, 165), ("lizard leather", 1.0), ("drakinata", 0.75), ("red lantern", 0.5), ("bunch of ripe rice", 2.0), ("small diamond", 1.5, 2), ("zaoan shoes", 0.5), ("zaoan armor", 0.0025), ("lizard trophy", 0.0025) )