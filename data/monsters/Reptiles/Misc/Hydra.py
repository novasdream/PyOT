hydra = genMonster("Hydra", (121, 6048), "a hydra")
hydra.setHealth(2350)
hydra.bloodType("blood")
hydra.setDefense(armor=29, fire=1, earth=0, energy=1.1, ice=0.5, holy=0.7, death=1, physical=1.05, drown=1)
hydra.setExperience(2100)
hydra.setSpeed(260)
hydra.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=300 )
hydra.walkAround(energy=0, fire=0, poison=0)
hydra.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=0)
hydra.voices("FCHHHHH", "HISSSS")
hydra.loot( (2148, 100, 244), ("ham", 60.25, 4), ("small sapphire", 5.0), ("hydra head", 10.0), ("cucumber", 5.0), ("knight armor", 1.0), ("ring of healing", 1.25), ("medusa shield", 0.25), ("warrior helmet", 1.0), ("life crystal", 0.75), ("hydra egg", 1.0), ("stone skin amulet", 0.75), ("strong mana potion", 0.5), ("royal helmet", 0.25), ("boots of haste", 0.0025) )

#Paralyze Bomb (on target) --gfb size poison rings effect
hewave = spell.Spell("hydra ewave", target=TARGET_AREA)
hewave.area(AREA_WAVE8)
hewave.element(EARTH)
hewave.effects(area=EFFECT_SMALLPLANTS) 

hwwave = spell.Spell("hydra wwave", target=TARGET_AREA)
hwwave.area(AREA_WAVE5)
hwwave.element(ICE)
hwwave.effects(area=EFFECT_WATERSPLASH) 

hydra.regMelee(270)
hydra.regTargetSpell("hydra ewave", 65, 320, check=chance(20))
hydra.regTargetSpell("hydra wwave", 100, 250, check=chance(20))
hydra.regTargetSpell("Ice Strike", 70, 155, check=chance(20)) #range? havent seen it past 4
hydra.regSelfSpell("Light Healing", 260, 410, check=chance(20)) 