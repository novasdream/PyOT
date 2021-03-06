lost_soul = genMonster("Lost Soul", (232, 6310), "a lost soul")
lost_soul.setHealth(5800)
lost_soul.bloodType("undead")
lost_soul.setDefense(armor=30, fire=0, earth=0, energy=0.9, ice=0.5, holy=1.25, death=0, physical=1, drown=1)
lost_soul.setExperience(4000)
lost_soul.setSpeed(250)
lost_soul.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
lost_soul.walkAround(energy=1, fire=0, poison=0)
lost_soul.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=0)
lost_soul.voices("Mouuuurn meeee!", "Forgive Meee!", "Help meee!")
lost_soul.regMelee(420)
lost_soul.loot( ("scale armor", 9.75), ("death ring", 1.0), ("unholy bone", 28.25), ("stone skin amulet", 2.5), ("titan axe", 0.75), ("great mana potion", 9.75), ("soul orb", 6.25), ("blank rune", 35.0), ("steel helmet", 9.75), ("rusty armor", 11.75, 2), ("plate armor", 10.25), (2148, 100, 313), ("platinum coin", 11.75, 3), ("demonic essence", 6.0, 3), ("ruby necklace", 1.0), ("silver goblet", 5.5), ("skeleton decoration", 1.0), ("skull staff", 0.75) )