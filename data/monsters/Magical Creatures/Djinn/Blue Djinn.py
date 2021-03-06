blue_djinn = genMonster("Blue Djinn", (51, 6016), "a blue djinn")
blue_djinn.setHealth(330)
blue_djinn.bloodType("blood")
blue_djinn.setDefense(armor=22, fire=0.8, earth=1, energy=0.5, ice=1.1, holy=0.8, death=1.13, physical=0.8, drown=1)
blue_djinn.setExperience(215)
blue_djinn.setSpeed(220)
blue_djinn.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
blue_djinn.walkAround(energy=1, fire=1, poison=1)
blue_djinn.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
blue_djinn.voices("Simsalabim", "Wishes can come true", "Feel the power of my magic, tiny mortal!", "Be careful what you wish for.")
blue_djinn.regMelee(110)
blue_djinn.loot( (2148, 100, 115), ("carrot", 25.75), ("royal spear", 7.75, 2), ("small sapphire", 6.75, 4), ("blue piece of cloth", 2.0, 3), ("mana potion", 1.0), ("book", 2.5), (12412, 2.25), ("small oil lamp", 1.0), ("mystic turban", 0.25), ("blue rose", 0.5) )