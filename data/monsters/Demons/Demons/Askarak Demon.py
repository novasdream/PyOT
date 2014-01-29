askarak_demon = genMonster("Askarak Demon", (420, 5980), "an askarak demon")#corpse
askarak_demon.setHealth(1500)
askarak_demon.bloodType("blood")
askarak_demon.setDefense(armor=26, fire=1.3, earth=1, energy=0.5, ice=0.5, holy=1, death=1, physical=1, drown=1)#
askarak_demon.setExperience(900)
askarak_demon.setSpeed(300)#
askarak_demon.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
askarak_demon.walkAround(energy=0, fire=0, poison=0)
askarak_demon.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
askarak_demon.voices("DEATH TO THE SHABURAK!", "ONLY WE ARE TRUE DEMONS!", "GREEN WILL RULE!", "RED IS MAD")
askarak_demon.regMelee(140)
askarak_demon.loot( ("springsprout rod", 0.5), ("mastermind potion", 0.5), ("energy ring", 1.0), ("piggy bank", 0.75), ("small emerald", 9.75, 4), ("strong health potion", 5.25), ("strong mana potion", 4.25), ("assassin star", 18.0, 5), ("brown mushroom", 4.0), (2148, 100, 213), ("terra legs", 0.0025) )