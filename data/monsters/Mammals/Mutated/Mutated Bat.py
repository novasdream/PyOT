mutated_bat = genMonster("Mutated Bat", (307, 9829), "a mutated bat")
mutated_bat.setHealth(900)
mutated_bat.bloodType("blood")
mutated_bat.setDefense(armor=20, fire=1, earth=0, energy=1, ice=1, holy=1, death=0, physical=1, drown=0)
mutated_bat.setExperience(615)
mutated_bat.setSpeed(245)
mutated_bat.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=300)
mutated_bat.walkAround(energy=0, fire=0, poison=0)
mutated_bat.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
mutated_bat.voices("Shriiiiiek")
mutated_bat.regMelee(169, condition=CountdownCondition(CONDITION_POISON, 6), conditionChance=100)
mutated_bat.loot( (2148, 100, 130), ("star herb", 5.0), ("rusty armor", 13.0, 2), ("battle shield", 7.75), ("obsidian lance", 7.0), ("bat wing", 7.75, 3), ("mutated bat ear", 5.0), ("energy ring", 1.0), ("small amethyst", 0.75, 2), ("black pearl", 1.75, 3), ("batwing hat", 0.0025), ("mercenary sword", 0.0025), ("black shield", 0.0025) )