
necromancer = genMonster("Necromancer", (9, 6080), "a necromancer")
necromancer.setHealth(580, healthmax=580)
necromancer.bloodType("blood")
necromancer.setDefense(armor=54, fire=1.05, earth=0, energy=0.8, ice=0.9, holy=1.05, death=0.5, physical=1.05, drown=1)
necromancer.setExperience(580)
necromancer.setSpeed(200)
necromancer.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=0)
necromancer.walkAround(energy=1, fire=1, poison=0)
necromancer.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
necromancer.summon("ghoul", 10)
necromancer.summon("ghost", 10)
necromancer.summon("Mummy", 10)
necromancer.maxSummons(4)
necromancer.voices("Taste the sweetness of death!", "Your corpse will be mine.")
necromancer.regMelee(80)
necromancer.loot( ("book of necromantic rituals", 9.5), ("mystic turban", 0.5), ("poison arrow", 44.0, 5), ("green mushroom", 1.5), (2148, 100, 90), ("necromantic robe", 1.0), ("boots of haste", 0.25), ("strong mana potion", 0.5), ("skull staff", 0.0025), ("clerical mace", 0.5), ("spellbook of warding", 0.0025), ("noble axe", 0.0025) )