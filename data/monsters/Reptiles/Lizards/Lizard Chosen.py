lizard_chosen = genMonster("Lizard Chosen", (344, 11288), "a lizard chosen")
lizard_chosen.setHealth(3050, healthmax=3050)
lizard_chosen.bloodType("blood")
lizard_chosen.setDefense(armor=30, fire=0.9, earth=0, energy=0.8, ice=0.9, holy=1, death=1, physical=1, drown=1)
lizard_chosen.setExperience(2200)
lizard_chosen.setSpeed(240)
lizard_chosen.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=50)
lizard_chosen.walkAround(energy=0, fire=0, poison=0)
lizard_chosen.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
lizard_chosen.voices("Grzzzzzzz!", "Kzzzzzzz!", "Garrrblarrrrzzzz!")
lizard_chosen.regMelee(360)
lizard_chosen.loot( (2148, 100, 232), ("lizard leather", 2.0), ("spiked iron ball", 9.5), ("scale of corruption", 3.25), ("platinum coin", 9.75, 5), ("cursed shoulder spikes", 5.75), ("great health potion", 14.5, 3), ("zaoan shoes", 0.75), ("small diamond", 8.25, 5), ("corrupted flag", 2.75), ("lizard scale", 1.0, 3), ("zaoan armor", 1.25), ("zaoan helmet", 0.0025), ("zaoan legs", 0.5), ("tower shield", 1.0) )