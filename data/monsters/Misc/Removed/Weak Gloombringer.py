#largely unknown
weak_gloombringer = genMonster("Weak Gloombringer", (12, 5980), "a weak gloombringer")
weak_gloombringer.setHealth(10000)
weak_gloombringer.bloodType("blood")
weak_gloombringer.setDefense(armor=1, fire=1, earth=1, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
weak_gloombringer.setExperience(0)
weak_gloombringer.setSpeed(300)
weak_gloombringer.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
weak_gloombringer.walkAround(energy=0, fire=0, poison=0)
weak_gloombringer.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
weak_gloombringer.regMelee(3000)
weak_gloombringer.loot( ("small diamond", 100, 5), ("gold ingot", 31.5), ("platinum coin", 100, 35), ("small ruby", 100, 5), (2148, 100, 156), ("midnight shard", 100.0), ("small topaz", 10.5), ("small emerald", 15.75, 2), ("small sapphire", 47.25, 4) )