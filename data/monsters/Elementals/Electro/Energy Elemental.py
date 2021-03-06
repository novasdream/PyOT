energy_elemental = genMonster("Energy Elemental", (293, 8966), "a energy elemental")
energy_elemental.setHealth(500)
energy_elemental.bloodType("undead")
energy_elemental.setDefense(armor=26, fire=0, earth=1.15, energy=0, ice=0, holy=0.95, death=0.95, physical=0.65, drown=1)
energy_elemental.setExperience(550)
energy_elemental.setSpeed(250)
energy_elemental.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
energy_elemental.walkAround(energy=0, fire=0, poison=1)
energy_elemental.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
energy_elemental.regMelee(180)
energy_elemental.loot( (2148, 100, 169), ("crystal sword", 6.25), ("mana potion", 11.75), ("flash arrow", 61.75, 10), ("strong mana potion", 8.75), ("throwing star", 30.25, 5), ("obsidian lance", 4.0), ("small amethyst", 7.75, 2), ("guardian shield", 0.5), ("energy ring", 0.5), ("crystal ring", 1.75), ("silver amulet", 1.0), ("wand of cosmic energy", 0.75) )