vampire = genMonster("Vampire", (68, 6006), "a vampire")
vampire.setHealth(475)
vampire.bloodType("blood")
vampire.setDefense(armor=37, fire=1.1, earth=0, energy=1, ice=1, holy=1.25, death=0, physical=0.8, drown=0)
vampire.setExperience(305)
vampire.setSpeed(220)
vampire.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=10)#runs on some low number maybe as low as 1
vampire.walkAround(energy=1, fire=1, poison=0)
vampire.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
vampire.voices("Kneel before your Mistress!", "Dead is the new alive.", "Come, let me kiss you, darling. Oh wait, I meant kill.", "Enjoy the pain - I know you love it.", "Are you suffering nicely enough?")
vampire.regMelee(150)
vampire.loot( ("skull", 0.5), ("vampire teeth", 6.5), (2148, 100, 49), ("grave flower", 1.75), ("katana", 1.25), ("spike sword", 0.5), ("blood preservation", 0.5), ("strange helmet", 0.5), ("ice rapier", 1.25), ("emerald bangle", 0.5), ("bronze amulet", 0.5), ("black pearl", 0.75) )