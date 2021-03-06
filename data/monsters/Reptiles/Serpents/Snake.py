
snake = genMonster("Snake", (28, 2817), "a snake")
snake.setHealth(15)
snake.bloodType("blood")
snake.setDefense(armor=2, fire=1.1, earth=1, energy=0.8, ice=1.1, holy=1, death=1, physical=1, drown=1)
snake.setExperience(10)
snake.setSpeed(120)
snake.setBehavior(summonable=205, hostile=1, illusionable=1, convinceable=0, pushable=1, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=0)
snake.walkAround(energy=1, fire=1, poison=0)
snake.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
snake.voices("Zzzzzzt")
snake.regMelee(8, condition=Condition(CONDITION_POISON, 0, 1, damage=1), conditionChance=100)
