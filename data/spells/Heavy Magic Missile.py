conjure = spell.Spell("Heavy Magic Missile", "adori vis", icon=23, group=SUPPORT_GROUP)
conjure.require(mana=350, level=25, maglevel=0, soul=2, learned=0, vocations=(1, 5, 2, 6))
conjure.use(2260)
conjure.cooldowns(0, 3)
conjure.targetEffect(callback=spell.conjure(2311, 10))

rune = spell.Rune(2311, icon=8, count=10, target=TARGET_TARGET, group=ATTACK_GROUP)
rune.cooldowns(0, 2)
rune.require(mana=0, level=25, maglevel=0)
rune.targetEffect(callback=spell.damage(0.8, 1.6, 5, 10, ENERGY))
rune.effects(area=EFFECT_ENERGYAREA, shoot=ANIMATION_ENERGY) #may be wrong effect