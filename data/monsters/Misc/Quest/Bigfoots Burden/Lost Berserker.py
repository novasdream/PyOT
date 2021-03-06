Lost_Berserker = genMonster("Lost Berserker", (496, 16062), "a lost berserker")
Lost_Berserker.setHealth(5900)
Lost_Berserker.bloodType("blood")
Lost_Berserker.setDefense(armor=70, fire=0.9, earth=0, energy=0.85, ice=0.6, holy=1, death=0.85, physical=0.8, drown=1)
Lost_Berserker.setExperience(4400)
Lost_Berserker.setSpeed(300)
Lost_Berserker.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
Lost_Berserker.walkAround(energy=0, fire=0, poison=0)
Lost_Berserker.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
Lost_Berserker.voices("Kill! Kiill! Kill!", "Death! Death! Death!")
Lost_Berserker.regMelee(250)