humorless_fungus = genMonster("Humorless Fungus", (517, 18382), "a humorless fungus") #almost everything is unknown health, stance, etc...--corpse(may be right)
humorless_fungus.setHealth(1000, healthmax=1000)
humorless_fungus.bloodType("blood")
humorless_fungus.setDefense(armor=25, fire=0.95, earth=0, energy=0.85, ice=0.85, holy=0.95, death=1, physical=1, drown=1)
humorless_fungus.setExperience(0)
humorless_fungus.setSpeed(400)
humorless_fungus.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
humorless_fungus.walkAround(energy=0, fire=0, poison=0)
humorless_fungus.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
humorless_fungus.voices("Munch munch munch!","Chatter".)
humorless_fungus.regMelee(480)