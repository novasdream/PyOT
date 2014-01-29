lizard_dragon_priest = genMonster("Lizard Dragon Priest", (339, 11280), "a lizard dragon priest")
lizard_dragon_priest.setHealth(1450)
lizard_dragon_priest.bloodType("blood")
lizard_dragon_priest.setDefense(armor=24, fire=0.15, earth=0, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
lizard_dragon_priest.setExperience(1320)
lizard_dragon_priest.setSpeed(320)
lizard_dragon_priest.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=50)
lizard_dragon_priest.walkAround(energy=1, fire=0, poison=0)
lizard_dragon_priest.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
lizard_dragon_priest.summon("Dragon Hatchling", 10)
lizard_dragon_priest.maxSummons(2)
lizard_dragon_priest.voices("I ssssmell warm blood!")
lizard_dragon_priest.regMelee(50)
lizard_dragon_priest.loot( ("bunch of ripe rice", 1.0), ("platinum coin", 6.0, 2), ("yellow gem", 1.0), ("small amethyst", 10.0, 3), (11361, 10.25), ("focus cape", 0.75), ("strong mana potion", 12.0), ("lizard leather", 1.0), ("terra rod", 1.0), ("great mana potion", 8.0), (2148, 100, 190), ("zaoan robe", 0.25), ("wand of inferno", 1.5), ("lizard scale", 1.0, 3), ("zaoan shoes", 0.5), ("life ring", 0.75) )