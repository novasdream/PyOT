chakoya_tribewarden = genMonster("Chakoya Tribewarden", (258, 7320), "a chakoya tribewarden")#261? wrong looktype?
chakoya_tribewarden.setHealth(68, healthmax=68)
chakoya_tribewarden.bloodType("blood")
chakoya_tribewarden.setDefense(armor=9, fire=0.75, earth=1, energy=1.15, ice=0, holy=0.9, death=1.05, physical=1, drown=1)
chakoya_tribewarden.setExperience(40)
chakoya_tribewarden.setSpeed(270)
chakoya_tribewarden.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=305, pushable=0, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=0)
chakoya_tribewarden.walkAround(energy=1, fire=1, poison=1)
chakoya_tribewarden.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
chakoya_tribewarden.voices("Quisavu tukavi!", "Si siyoqua jamjam!", "Achuq! jinuma!", "Si ji jusipa!")
chakoya_tribewarden.regMelee(30)
chakoya_tribewarden.loot( (2148, 100, 20), ("fish", 20.0), ("rainbow trout", 0.25), ("short sword", 3.75), ("bone shield", 1.0), ("green perch", 0.25), ("mammoth whopper", 0.25), ("northern pike", 0.0025) )