#unknown
lizard_noble = genMonster("Lizard Noble", (115, 6041), "a lizard noble")
lizard_noble.setHealth(5740, healthmax=5740)
lizard_noble.bloodType("blood")
lizard_noble.setDefense(armor=29, fire=0.15, earth=0, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
lizard_noble.setExperience(2000)
lizard_noble.setSpeed(210)
lizard_noble.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=4, runOnHealth=0)
lizard_noble.walkAround(energy=0, fire=0, poison=0)
lizard_noble.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
lizard_noble.voices("Where are zhe guardz when you need zhem!")
lizard_noble.regMelee(80)
#lizard_noble.loot()