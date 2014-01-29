muddy_earth_elemental = genMonster("Muddy Earth Elemental", (301, 8933), "a muddy earth elemental")
muddy_earth_elemental.setHealth(650)
muddy_earth_elemental.bloodType("undead")
muddy_earth_elemental.setDefense(armor=62, fire=1.15, earth=0, energy=0.85, ice=0.8, holy=0.5, death=0.6, physical=0.65, drown=1)
muddy_earth_elemental.setExperience(450)
muddy_earth_elemental.setSpeed(260)
muddy_earth_elemental.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
muddy_earth_elemental.walkAround(energy=0, fire=1, poison=0)
muddy_earth_elemental.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
muddy_earth_elemental.regMelee(160)
muddy_earth_elemental.loot( (2148, 100, 128), ("lump of earth", 20.5), ("small stone", 100, 5), (2244, 19.5), ("coal", 0.5), ("natural soil", 4.25), ("clay lump", 0.75) )