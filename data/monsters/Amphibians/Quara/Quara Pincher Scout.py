quara_pincher_scout = genMonster("Quara Pincher Scout", (77, 6063), "a quara pincher scout")
quara_pincher_scout.setHealth(1800)
quara_pincher_scout.bloodType("blood")
quara_pincher_scout.setDefense(armor=80, fire=0, earth=1.1, energy=1.1, ice=0, holy=1, death=1, physical=1, drown=0)
quara_pincher_scout.setExperience(1200)
quara_pincher_scout.setSpeed(250)
quara_pincher_scout.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=0, targetDistance=1, runOnHealth=0)
quara_pincher_scout.walkAround(energy=1, fire=0, poison=1)
quara_pincher_scout.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
quara_pincher_scout.voices("Clank! Clank!", "Clap!", "Crrrk! Crrrk!")
quara_pincher_scout.loot( ("plate armor", 4.75), ("halberd", 2.25), (12446, 9.25), (2148, 100, 149), ("fish fin", 0.75, 3), ("small ruby", 3.25, 2), ("life crystal", 1.0) )

#Close Range Paralyze (lasts for 1-3 seconds).
quara_pincher_scout.regMelee(240)