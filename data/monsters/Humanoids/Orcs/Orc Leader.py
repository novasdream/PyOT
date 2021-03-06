orc_leader = genMonster("Orc Leader", (59, 6001), "an orc leader")
orc_leader.setHealth(450, healthmax=450)
orc_leader.bloodType("blood")
orc_leader.setDefense(armor=22, fire=0, earth=1.1, energy=0.8, ice=1, holy=0.8, death=1.1, physical=1, drown=1)
orc_leader.setExperience(270)
orc_leader.setSpeed(230)
orc_leader.setBehavior(summonable=640, hostile=1, illusionable=1, convinceable=640, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
orc_leader.walkAround(energy=1, fire=0, poison=1)
orc_leader.setImmunity(paralyze=1, invisible=1, lifedrain=0, drunk=1)
orc_leader.voices("Ulderek futgyr human!")
orc_leader.regMelee(185)
orc_leader.regDistance(70, ANIMATION_THROWINGKNIFE, chance(21))
orc_leader.loot( ("plate shield", 9.75), ("throwing knife", 21.0, 4), (2148, 100, 35), ("fish", 28.75), ("brown mushroom", 8.25), ("orc leather", 18.5), ("royal spear", 2.5), ("skull belt", 2.5), ("longsword", 2.0), ("health potion", 1.0), ("sword ring", 3.0), ("plate armor", 0.75), ("brass legs", 2.5), ("broadsword", 0.75), ("scimitar", 1.25), ("orc tooth", 0.75), ("plate legs", 0.5), ("warrior helmet", 0.0025) )