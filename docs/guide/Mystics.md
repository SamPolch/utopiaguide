# Difference between revisions of "Mystics"

| **[Revision as of 16:59, 8 September 2021](#) ([view source](#))**[Avenger](#) ([talk](#) | [contribs](#))m ([→](#Restriction_.26_Limits)‎Restriction & Limits)[← Older edit](#) | | **[Revision as of 17:00, 8 September 2021](#) ([view source](#))** [Avenger](#) ([talk](#) | [contribs](#))m ([→](#Restriction_.26_Limits)‎Restriction & Limits)[Newer edit →](#) | |
| Line 44: | | Line 44: | |
|  | \*[[Mystics#The\_Spell\_Book:\_the\_self\_spells|Self Spells]] |  | \*[[Mystics#The\_Spell\_Book:\_the\_self\_spells|Self Spells]] |
|  | \*\* Some Self Spells can be cast by Clerics on kingdom members. These spells are known as Support Spells. Success is based on the caster's WPA and relative networth to the target, and the duration of these spells is based on target's guilds. The list can be found [[Magic\_Formulas#The Spell Book|'''here''']]. |  | \*\* Some Self Spells can be cast by Clerics on kingdom members. These spells are known as Support Spells. Success is based on the caster's WPA and relative networth to the target, and the duration of these spells is based on target's guilds. The list can be found [[Magic\_Formulas#The Spell Book|'''here''']]. |
|  | | + | \*\*The caster gains honor from kd mates whom they cast support spells on. Those getting casted on lose honor when having a support spell casted on them, ~0.1%. |
|  | \*[[Mystics#The\_Spell\_Book:\_the\_offensive\_spells|Offensive spells]] |  | \*[[Mystics#The\_Spell\_Book:\_the\_offensive\_spells|Offensive spells]] |
|  |  |  |  |

---

## Revision as of 17:00, 8 September 2021

Unlike your fabled land of Earth, the citizens of [Utopia](../misc/Utopia.md) truly believe in and have witnessed the powers of magic. From the deadly plagues to the amazingly fertile land, so much has happened on this planet that cannot be explained away by science or nature. As ruler of your lands, you have access to some of the most amazing magical spells ever known. Below, I will try to explain to the best of my ability the powers of these spells and how to make magic your friend.

### Essentials: Runes, Wizards, and Guilds

Spells require [Runes](#), [Wizards](../misc/Units.md), and [Guilds](../category/Buildings.md) to be cast. [Towers](../category/Buildings.md) produce runes every hour, which are consumed with each spell. Wizards are naturally trained by your Guilds. Like all of the other individuals across your lands, they come from your [peasantry](../misc/Units.md) and reduce your number of available [workers](../category/Economy.md). Be careful not to hold too many Wizards or you may be sacrificing your peasantry, [thieves](../misc/Units.md), or [military](Military.md). At any time, you can release Wizards back into the peasantry or simply shut down additional training. Your Wizards maintain a Mana Rating which determines whether or not they can cast spells. This rating rises automatically each day and drops each time you cast a spell. Your Wizards will not cast spells without at least a 5% Mana Rating. Casting spells is not without risks. Failed attempts can result in explosions and kill a small portion of your wizards.

### Determining Success

To cast a spell, you must have [Guilds](Growth.md), wizards and mystic [Runes](#). For spells cast upon yourself, success is based on your Guild percentage and your Building Efficiency - the more guilds you have, the better you will do. For spells cast upon others, the success is based on your relative wizard population, measured as [Wizards Per Acre](#) (WPA), modified by the racial bonuses or penalties and your knowledge of Channeling science. The higher your WPA compared to an enemy, the better your success. However, there is always a great deal of chance in every spell. Furthermore, the duration of all spells is greatly impacted by your Guild percentage.

For support spells, the formula used to calculate success rate is adjusted to make casting self spells on your allies easier. A WPA vs WPA calculation will still be made which will require the caster to have WPA but the formula will make it so that all Kingdom members have an opportunity to receive the self spell bonuses from their support caster. In other words, although you still need WPA it won't be a very significant part of the formula.

### Duration of Spells

The duration of successful spells is affected by:

- The nominal duration of that particular spell, which differs for each spell.
- The percentage of guilds the casting province has, with no additional effect for amounts over 20%.
- The relative networth of the two provinces.
- The current relations between the two provinces' kingdoms.

Additionally, there is an element of randomness.

One quarter of the nominal duration of a spell is always contributed to the final cast time. A scaling factor made up of the % guilds, relative net worth and current relations then governs the contribution of another quarter of the nominal duration. Finally, the remaining half of the nominal duration is contributed to the final cast time, scaled by both the scaling factor and a random number.

For example, given a spell with a nominal duration of 24 days:

- with a scaling factor of 100% (meaning both provinces have the same net worth, are in war, and the caster has 20% or more guilds), the final cast time will be in the range of 12-24 days.
- in a situation with a scaling factor of 0% (e.g., the cast has no guilds), the final cast time will be 6 days (25% of 24 days).
- in a situation with a scaling factor of 50%, the final cast time will be 6 days (25% of 24 days) + 3 days (25% of 24 days multiplied by scaling factor of 50%) + 0-6 days (random number out of 50% of 24 days multiplied by scaling factor of 50%), which equals 9 - 15 days in total.

### Cost of Spells

All spells cost mana, which the province will regenerate each Utopian day up to a maximum of 100%. Once your mana falls below 5% you are unable to cast any more spells until your mana regenerates.

The costs of spells are:

- Self Spells - 3%
- Offensive Spells (without relations) - 3%
- Offensive Spells (Hostile relations) - 2%
- [Ritual](../misc/Ritual.md) Spells - 2%
- Support Spells on others - 2%

### Restriction & Limits

Certain spells are designated Unfriendly, Hostile or [War](Relations.md) Only spells -- Because of the destructive nature of these spells, they can be cast only against provinces which have at least a certain level of relations with your kingdom. In addition, you will find that many of these spells are more effective during heightened relations conditions.

Spells are divided into two categories, as listed below:

- [Self Spells](Mystics.md)
  - Some Self Spells can be cast by Clerics on kingdom members. These spells are known as Support Spells. Success is based on the caster's WPA and relative networth to the target, and the duration of these spells is based on target's guilds. The list can be found [**here**](Magic_Formulas.md).
  - The caster gains honor from kd mates whom they cast support spells on. Those getting casted on lose honor when having a support spell casted on them, ~0.1%.
- [Offensive spells](Mystics.md)

There are 3 possible outcomes of casting a spell. It can be successful, it can fail, or it can fail and some wizards may die.

- Successful message: Your wizards gather their runes and begin casting. The spell consumes X Runes and ... is successful!
- Fail message: Your wizards gather their runes and begin casting. The spell consumes X Runes and ... fizzles. Alas, we were not able to fulfill your expectations. Please forgive us.
- Dying wizards message: "Leader name", something has gone terribly wrong with our spell. X of our wizards were killed in an explosion!

Please note that Duration is in real time, spell messages are in [Utopia Time](../misc/Utopia_Time.md)

## The Spell Book: Self Spells

Listed here is a short reference guide to each of the spells available that can be cast on yourself. Any restrictions on use will be listed under the name. The max cast shown does not include any racial bonuses. Almost all the spells that provide bonuses for certain activities (like speeding up building construction etc.) need to be cast before the activity is initiated / ordered to reap the benefits of the spell.

### Aggression

This spell refocuses your soldiers from versatile fighting units into an offensive machine. Giving them a lust for attacking, Soldiers will gain 1 offensive point in all combat for the duration of the spell. During this period, though, they will lose 1 defensive point as well.

Is Known: Age 14 ... now

```
 Available to: Orc
 Effect: Your soldiers gain 1 offense points at the cost of losing 1 defense points.
 Duration: max 24 days.
 Cast Message: Our soldiers will fight with unique aggression for X days!
 Mystic Advisor Message: Our soldiers will fight with unique aggression for X days!
```

### Animate Dead

The power to raise the dead gives you the power to protect your people. By casting this spell, you can protect your people from the death and destruction of defending your lands. During your next defensive battle, half of your dead army will be restored into basic soldiers to help repopulate your army.

Is Known: Age 1 ... [Age 87](../misc/Age_87.md), [Age 90](../category/Age_90.md)

```
 Available to: Undead
 Effect: Raises 50% of your dead troops into basic soldiers during your next defensive battle.
 Duration: Expires when attacked.
 Cast Message: Our dead will be awakened the next time our lands are attacked! 
 Mystic Advisor Message: Same as Cast Message
```

### Anonymity

[War](Relations.md) is at the heart of the world of Utopia, but the fear of retaliation makes many leaders cringe. This spell casts an aura of mystery around your army. After a successful cast, your forces will remain anonymous during your next attack -- while your kingdom will be revealed, your enemy will not know your province's name.

Is Known: Age 13 ... now

```
 Available to: All
 Effect: Hides your province name during your next attack at the cost of no honor gains,
 causing the attacked province to be unable to ambush that attack.
 Decreases your attack gains by 15% for your next attack.
 Duration: removed after attack
 Cast Message: Our next attack will be cloaked under the shades of anonymity. 
 Mystic Advisor Message: Our armies are surrounded by a cloud of anonymity for our next battle.
```

### Bloodlust

Bloodlust fires the blood of your troops, igniting in them a desire to cause destruction. This fury will increase the carnage among enemy troops at a cost of increased recklessness among your own troops.

Is Known: Age 1 ... Age 22, [Age 49](../misc/Age_49.md) .. [Age 58](#), [Age 59](#) ... now

```
 Available to: Faery
 Effect: A province under Bloodlust will have 10% increased Offensive Military Efficiency, inflict 10% more kills, and suffer 20% higher military losses while the spell is active.
 Duration: Not yet known.
 Cast Message: Our armies crave the scent of blood. They will savage the enemy, or die trying. 
 Mystic Advisor Message: Same as Cast Message
```

### Builders' Boon

The Builders' Boon spell makes your workers build faster and harder than otherwise. All buildings constructed while the spell is active will be completed more quickly than normal. The spell must be cast before the new construction is ordered in the growth panel for lesser construction time.

Is Known: Age 15 ... now

```
 Available to: All
 Effect: Decreases your construction times by 25% for building set to build while active.
 Duration: max 24 hours
 Cast Message: Our builders have been blessed with unnatural speed for X days! 
 Mystic Advisor Message: Same as cast message.
```

### Cast Ritual

Once your Monarch or Steward has declared what ritual to perform, this spell will increase your progress towards its completion with each cast. This spell has a very high difficulty and cost, and is accessible via the [Ritual](../misc/Ritual.md) tab.

Is Known: [Age 73](../category/Age_73.md) ... now

```
 Available to: All
 Effect: Progresses the ritual counter with each successful cast.
 Duration: Instant Cast
 Cast Message: We are now closer to completing our ritual project!
 Mystic Advisor Message: N/A
```

### Clear Sight

By granting your police the ability to see through the obvious and into the depths, you give them the ability to catch thieves who may wander into the lands. The spell, lasting potentially for weeks, gives you a base chance to catch opposing thieves, regardless of the strength of the guilds involved.

Is Known: Age 1 ... now

```
 Available to: Avian
 Effect: Automatically catches 25% of the thieves' operations conducted against your province.
 Duration: max 22 days
 Cast Message: Our police have been blessed with Clear Sight for X days!
 Mystic Advisor Message: Same as Cast Message
```

### Divine Shield

The cleric protects his people from the black magics of his enemies, granting them further protection against harmful spells.

Is Known: [Age 72](../misc/Age_72.md) ... [Age 80](../misc/Age_80.md) ... [Age 87](../misc/Age_87.md) ... now

```
 Available to: Cleric
 Effect: Reduces Instant Spell Damage taken by 20%. 
 Duration: Moderate, max time unknown
 Cast Message: You imbue your province with a holy shield, protecting against foul sorcery for XX days! 
 Mystic Advisor Message: Same as cast message
```

### Fanaticism

Fanaticism focuses your army on combat, increasing their offensive efficiency for several days. Unfortunately, a side effect of this desire for blood is that your armies remaining at home -- bored and frustrated for not being in combat -- will fight less effectively on defense.

Is Known: Age 14 ... now

```
 Available to: Cleric
 Effect: Increases your offensive military efficiency by 5%. Decreases your defensive military 
 efficiency by 5%.
 Duration: max 12 hours
 Cast Message: Our army will fight with fanaticism for X days! 
 Mystic Advisor Message: Our army fights with fanatical fervor
```

### Fertile Lands

By magically fertilizing your lands, you can ensure excellent food production for the duration of the spell. Whether a lack of farms, a deadly drought, or just wanting to stockpile extra food, this spell offers a definite increase to your food sources.

Is Known: Age 1 ... now

```
 Available to: All
 Effect: Increases food production by 25%.
 Duration: max 30 hours.
 Cast Message: We have made our lands extraordinarily fertile for X days!  
 Mystic Advisor Message: Same as Cast Message
```

### Fountain of Knowledge

Science is a fundamental building block for any and all of the other parts of your province. While a Fountain of Knowledge spell is active, your students work harder and will learn more than they would otherwise.

Is Known: Age 39 ... [Age 68](../misc/Age_68.md), [Age 82](../misc/Age_82.md) ... now

```
 Available to: Elf
 Effect: Increases your science book production by 10% while the spell is active.
 Duration: Moderate, max duration unknown
 Cast Message: Our students are blessed with excellent concentration for X Days!
 Mystic Advisor Message: Our students are blessed with excellent concentration for X days!
```

### Ghost Workers

Creating ghostly workers to perform the duties of your peasants, this spell reduces reduces the amount of filled jobs for maximum efficiency. This spell is effective for several days until the ghosts disappear.

Is Known: Age 13 ... Age 16 ... [Age 81](../category/Age_81.md) ... now

```
 Available to: Faery
 Effect: The required number of jobs filled for maximum Building Efficiency is reduced by 20%.
 Duration: Moderate, max time unknown
 Cast Message: Magical auras enchant our buildings and begin working with increased productivity for XX days!
 Mystic Advisor Message: Same as cast message
```

### Greater Protection

A more powerful version of the Minor Protection spell, this spell functions similarly but lasts potentially a great deal longer. It can be stacked with Minor Protection.

Is Known: Age 1 ... now

```
 Available to: Cleric
 Effect: Increases defensive military efficiency by 5%.
 Duration: max time unknown
 Cast Message: Our realm is now under a sphere of protection for X days. 
 Mystic Advisor Message: Our realm is now under a sphere of protection for X days!
```

### Guile

By focusing your mind and employing cunning techniques, you increase the damage of your spells and operations.

Is Known: [Age 90](../category/Age_90.md)

```
 Available to: Heretic
 Effect: Increases Instant Spell and Sabotage Operation Damage by 20%.
 Duration: Moderate, max time unknown
 Cast Message: Our thieves and wizards' assimilated concentration will increase their damage for X days!
 Mystic Advisor Message: Our thieves and wizards' assimilated concentration will increase their damage for X days!
```

### Illuminate Shadows

Shine light across the land, eliminating the cover of darkness and revealing those who would hide within its shadow. Thieves who would enter these lands are discouraged from performing their duties and will thus have a lessened impact.

Is Known: [Age 72](../misc/Age_72.md) ... now

```
 Available to: Cleric
 Effect: Reduces damage from thievery operations by 20%.
 Duration: Moderate, max time unknown
 Cast Message: Your mages fill your province with holy light, reducing shadows for thieves to hide in for XX days! 
 Mystic Advisor Message: Same as cast message
```

### Inspire Army

Inspire Army helps make your military train harder on their own, thus reducing the daily wages you pay your military for several days. This is especially useful in times of limited cash. This spell also increases the intensity of training, allowing your troops to be ready more quickly; provided the spell is cast before the troops are ordered to be trained.

Is Known: Age 7 ... [Age 71](../category/Age_71.md), [Age 74](../misc/Age_74.md) ... now

```
 Available to: All
 Effect: Decreases your military wages by 15%. Decreases your military training time by 20%. 
 Duration: max 24 hours
 Cast Message: Our army has been inspired to train harder. We expect maintenance costs to be 
 reduced for X days! 
 Mystic Advisor Message: Same as Cast Message
```

### Invisibility

Thieves rely on stealth to master their craft, but a little bit of invisibility never hurts. Through the duration of this spell, your thieves have a 20% bonus to any offensive thievery operations and incur 20% lower losses.

Is Known: Age 1 ... now

```
 Available to: Rogue
 Effect: Increases your offensive thievery efficiency by 20%. Reduce thieves lost during thievery operations by 20%.
 Duration: max 22 hours
 Cast Message: Our thieves have been made partially invisible for X Days!
 Mystic Advisor Message: Same as Cast Message
```

### Love & Peace

Love & Peace creates an aura of calm and happiness across your peasantry for several days. This leads to increased natural birth rates which will quickly replenish your population. This is especially useful when your peasantry has suffered greatly.

Is Known: Age 7 ... now

```
 Available to: All
 Effect: Increases base birth rate from 2.05% to 2.85%. Increase War Horses production by 40%.
 Duration: max 22 hours
 Cast Message: Our peasantry is influenced by a magical calm. We expect birth rates to be higher for
 X days! 
 Mystic Advisor Message: Our people feel at peace (Estimated: X more Days).
```

### Mage's Fury

This spell sparks a destructive fervor in your Mages Guild. They increase their efforts to cause damage to their opponents, whilst sacrificing a portion of their own defense temporarily.

Is Known: [Age 49](../misc/Age_49.md) ... now

```
 Available to: Dark Elf
 Effect: This spell increases the province's WPA by 25% for offensive purposes while decreasing 
 it by 25% for defensive
 purposes. No effect on self-spells.
 Duration: max 12 hours
 Cast Message: The fire of Mage's Fury burns in our wizards' eyes for x days! 
 Mystic Advisor Message: The fire of Mage's Fury burns in our wizards' eyes for x days!
```

### Magic Shield

While the natural aura of your Wizards will help protect from enemy spells, a little additional protection can never hurt. Casting this spell offers you a shield of magical protection for your province for about half a month.

Is Known: Age 1 ... now

```
 Available to: All
 Effect: Increases your defensive magic efficiency by 20%.
 Duration: max 24 hours
 Cast Message: For X days, the magical auras within our province will shine brightly! 
 Mystic Advisor Message: A shield protects us from the black magic of our enemies 
 (Estimated: X more Days).
```

### Minor Protection

Casting a sphere of protection over your province, this spell helps protect your province from invasion from others. This spell lasts for a few weeks.

Is Known: Age 1 ... now

```
 Available to: All
 Effect: Increases defensive military efficiency by 5%.
 Duration: max 24 hours
 Cast Message: Our realm is now under a sphere of protection for X days. 
 Mystic Advisor Message: Same as Cast Message
```

### Mist

Casting a sphere of protection over your province, this spell helps protect your province from invasion.

Is Known: [Age 85](../category/Age_85.md) ... now

```
 Available to: Dwarf
 Effect: Lowers enemy gains by 10% on defensive battles for a duration.
 Duration: Short, max time unknown
 Cast Message: Our lands are protected by a sacred mist for X days from attacks against us!
 Mystic Advisor Message: Our lands are protected by a sacred mist for X days from attacks against us!
```

### Mystic Aura

A defense spell, creating a Mystic Aura around your lands will repel the next evil spell cast upon you from abroad. Unfortunately, the effect focuses only on the first spell cast upon you.

Is Known: Age 1 ... [Age 58](#), [Age 60](#) ... now

```
 Available to: Elf
 Effect: Repels the next offensive spell cast upon you (except own spells).
 Duration: N/A
 Cast Message: A Mystic Aura has been placed around our province, protecting us from the next evil
 spell from abroad. 
 Mystic Advisor Message: Same as Cast Message
```

Note that Mystic Aura does not activate on intel spells like Crystal Ball.

### Nature's Blessing

Nature's Blessing will protect your lands from any droughts and storms the world may see fit to place on you. This spell also has a chance of curing [the Plague](#) if your lands are affected by it.

Is Known: Age 1 ... now

```
 Available to: All
 Effect: Protects your land against Storms and Drought. Has a 33% chance of curing Plague (per cast).
 Duration: max 36 hours
 Cast Message: Our lands have been blessed by nature for X days, and will be protected from drought
 and storms.  
 Mystic Advisor Message: Our land is blessed by nature (Estimated: X more Days).
```

### Paradise

Arguably one of the most powerful -- and difficult -- spells known, Paradise simply creates several acres of new land for your people to populate. Similar in concept to exploring, this Spells gives you instant access to new lands to build upon and grow your province.

Is Known: Age 12 ... now

```
 Available to: All
 Effect: Creates a small amount of land per cast, this land comes directly from your explore pool. Between 1-10 acres per cast.
 Duration: Instant cast
 Cast Message: Our mages created X acres more land for us to use.
 Mystic Advisor Message: N/A
 Note: Paradise is not available during War and Protection. This spell utilizes acres from the explore pool. If the explore pool is empty, it will return 0 acres.
```

### Patriotism

Giving your population life and an innate desire to defend your lands, this spell increases the rate that you can draft peasants for several weeks, and offers partial protection against the Propaganda thievery operation. Excellent in emergencies and other strategic situations, this spell is difficult to cast and will more quickly weaken your economy.

Is Known: Age 11 ... now

```
 Available to: All
 Effect: Increases military draft speed by 30%. Lowers Propaganda Damage received by 30%.
 Duration: max 20 hours
 Cast Message: Our people are excited about the military and will signup more quickly for x days!
 Mystic Advisor Message: Same as Cast Message
```

### Quick Feet

By giving your men magical speed, they can go to battle and return more quickly than usual, leaving your land without defense for a shorter period.

Is Known: Age 1 ... [Age 86](../misc/Age_86.md), [Age 88](../misc/Age_88.md) ... now

```
 Available to: Tactician
 Effect: Decreases your attack time by 15%.
 Duration: Short
 Cast Message: Our armies have been blessed with excellent speed.
 Mystic Advisor Message: Our armies are blessed with incredible speed.
```

### Reflect Magic

Reflect magic places a magical barrier around your lands for several days. During this period, successful spells cast upon your province may randomly be reflected upon the caster, doing unto them as they would have done to you.

Is Known: Age 1 ... now

```
 Available to: Human
 Effect: Has a 25% chance of reflecting offensive spells cast upon your province.
 Duration: max 18 hours.
 Cast Message: Some of the spells cast upon our lands will be reflected back upon their creators for X days!
 Mystic Advisor Message: Same as Cast Message
```

### Revelation

Science is a fundamental building block for any and all of the other parts of your province. While the Revelation spell is active, it increases the rate of a new scientist emerging.

Is Known: [Age 69](#) ... now

```
 Available to: Heretic, Mystic, Rogue
 Effect: Increases the rate of a new scientist emerging on by 30% while the spell is active.
 Duration: Short-moderate, max duration unknown
 Cast Message: Our students are blessed with excellent concentration for X Days!
 Mystic Advisor Message: Our students are blessed with excellent concentration for X days!
```

### Scientific Insights

This spell clears the minds of your scientists, allowing them to think more clearly and increasing the effectiveness of their research.

Is Known: [Age 72](../misc/Age_72.md) ... now

```
 Available to: Sage
 Effect: Increase the science effectiveness of target province by 10%.
 Duration: Very short, max time unknown
 Cast Message: Your scientists have been imbued with mental energy, making them work harder for XX days! 
 Mystic Advisor Message: Same as cast message
```

### Shadowlight

Shadowlight places a face upon a shadow, revealing the province associated with the next thievery operation against your lands. It does not, however, prevent them from being successful.

Is Known: Age 1 ... now

```
 Available to: All
 Effect: Reveals the name of the next province performing a successful thievery operation upon your province.
 Duration: Expires on enemy thievery attempt
 Cast Message: Our lands are blessed with Shadowlight. The next time thieves enter our lands their identities will be revealed.
 Mystic Advisor Message: Same as Cast Message
```

### Town Watch

Town Watch will create a peasant watch upon your town for several days. While the Town Watch is active, all of your peasants will help defend your province in combat. Unfortunately, this also means your peasants will be killed during [war](Relations.md) - and since they are not well-armed, they will suffer heavy losses.

Is Known: Age 7 ... now

```
 Available to: Halfling
 Effect: Every 5 of your peasants will defend your land with 1 point of defense.
 Duration: max 18 hours
 Cast Message: Our peasants will help defend our lands for X days!
 Mystic Advisor Message: Our peasants will help defend our lands for X days!
```

### Tree of Gold

If you're ever in need of extra cash, casting a Tree of Gold may be a potential solution. While it won't give you a great deal of gold, every little bit can help.

Is Known: Age 1 ... now

```
 Available to: Faery
 Effect: Magically creates a small amount of gold (from 26.66% to 53.33% of your daily income).
 Duration: Instant cast
 Cast Message: X gold coins have fallen from the trees! 
 Mystic Advisor Message: n/a
```

### War Spoils

Ordinarily, any land captured in attacks require time to take control of and become available for your own use. War Spoils gives you the opportunity to get this land from combat immediately. The spell lasts just a few Utopian Days, but is more than enough to use on a couple of attacks. This allows you to begin the process of expanding much more quickly than otherwise.

Is Known: Age 12 ... [Age 58](#), [Age 60](#) ... now

```
 Available to: Tactician
 Effect: Makes the land gained from Traditional March immediately available.
 Duration: max 6 hours
 Cast Message: Our army has been blessed with immediate War Spoils for X days! 
 Mystic Advisor Message: War Spoils give us quick returns on our attacks
```

### Wrathful Smite

Smite foes who dare to inflict harm upon the target. Enemy attackers suffer increased casualties when attacking lands protected by this spell.

Is Known: [Age 72](../misc/Age_72.md) ... now

```
 Available to: Cleric
 Effect: Increases enemy casualties when attacking the protected province by 20%.
 Duration: Moderate, max time unknown
 Cast Message: Your magic will smite attackers for XX days! 
 Mystic Advisor Message: Same as cast message
```

## The Spell Book: Offensive Spells

Listed here is a short reference guide to each of the spells available that can be cast upon your enemies. Any restrictions on usage will be listed under the name.

### Abolish Ritual

Reduces the strength of an enemy kingdom's province and has a high cost/difficulty

Is Known: [Age 73](../category/Age_73.md) ... now

```
 Available to: All with minimum relationship of Unfriendly.
 Effect: Reduces ritual strength by 2%. Limited to 10 casts on a single enemy province.
 Duration: Instant
 Cast Message: Your mages infest the guilds of X. Their ritual is now x% destroyed! This province can still be targeted X times! 
 Mystic Advisor Message: N/A
```

### Amnesia

Knowledge is vital to the longterm survival of a province. The unique powers of magic allow you to strip a province of some of its long-sought science. Its effects are temporary. By casting Amnesia, you can cause an enemy province to lose effectiveness of their arts & sciences knowledge, opening a window to attack or further damage the enemy.

Is Known: Age 1 ... now

```
 Available to: All - with a minimum relationship of War
 Effect: Reduces the effectiveness of target's science by ~2%. Reduced science effectiveness will be removed upon entering End of War Cease-Fire.
 Duration: Instant with duration effect: Relation length dependent
 Cast Message: N/A
 Mystic Advisor Message: N/A
 Throne Room Notification: N/A
```

### Blizzard

Reduces the building effectiveness of a province for a short duration.

Is Known: [Age 69](#) ... now

```
 Available to: Faery
 Effect: Reduces the building effectiveness of a province by 10%.
 Duration: Short
 Cast Message: Your wizards gather n runes and begin casting, and the spell succeeds. Blizzards will beset the works of [province name] (#:#) for X days!
 Mystic Advisor Message: N/A
 Throne Room Notification: Blizzards are besetting our works, and our building efficiency will be crippled by 10% for for X days!
```

### Chastity

Introducing Chastity amongst the peasants of your opponents is an effective way to grind their population growth to a halt.

Is Known: [Age 47](#) ... now

```
 Available to: Faery - with a minimum relationship of Unfriendly
 Effect: Suspends births, preventing population from growing naturally.
 Duration: 
 Cast Message: Much to the chagrin of their men, the womenfolk of [Province Name] have taken a vow
 of chastity for X days!
 Mystic Advisor Message: Our womenfolk have taken a vow of chastity preventing population growth for
 X days!
```

### Crystal Ball

Knowing more about your friends and opponents is vital to your success as a leader. This spell gives you insight into the workings of any province of your choice.

Is Known: Age 1 ... [Age 47](#), [Age 88](../misc/Age_88.md) ... now

```
 Available to: All
 Effect: Displays the targeted provinces Throne
 Duration: Instant
 Cast Message: 
 Mystic Advisor Message: N/A
```

### Droughts

The opposite of storms, droughts can do significant damage as well. Without the rains necessary for fertile land, food production will be lower than usual, possibly resulting in starvation throughout the lands. In addition, the harsh conditions slow interest in the military and interferes with the soldier draft. Horses across the province may die as well due to lack of water and food. Droughts negate any Storms currently ravaging the target's land.

Is Known: Age 1 ... now

```
 Available to: All
 Effect: Decreases food production by 25%, military draft rate by 15% and horses production by 50%.
 Some horses may also die as a result.
 Duration: 
 Cast Message: A drought will reign over the lands of [Province Name] for X days! 
 Mystic Advisor Message:
```

### Explosions

Provinces work together by assisting each other in times of need. By casting Explosions, you can interrupt the flow of goods between provinces, creating explosions that destroy portions of shipments to and from a province at random.

Is Known: Age 10 ... now

```
 Available to: All
 Effect: 50% chance to reduce an aid shipment to 55%-80% of original size.
 Duration: 
 Cast Message: Explosions will rock aid shipments to and from [Province Name] for X days! 
 Mystic Advisor Message: Explosions will rock aid shipments to and from our province for X days!
```

### Expose Thieves

Thieves rely on stealth and surprise to be effective at their jobs. Casting this spell will expose an enemy's guild, leaving them less effective until they can recover.

Is Known: Age 1 ... now

```
 Available to: All with a minimum relationship of Unfriendly
 Effect: Decreases available stealth of target province to between 80% and 90% of its original amount.
 Duration: Instant
 Cast Message: Our mages have illuminated the lands of our enemies and exposed the thieves that walk
 through their lands.
 Mystic Advisor Message: N/A
```

### Fireball

If you want to directly go after an enemy, launching a fireball at their peasantry is an effective weapon. The fireball, if successful, will splash directly into the heart of your opponent's lands, exploding on impact, and killing instantly.

Is Known: Age 1 ... now

```
 Available to: All with minimum relationship of Unfriendly 
 Effect: Kills a small and random portion of peasants (4.95-8.47%).
 Duration: Instant
 Cast Message: A fireball burns through the skies of [province name] (##:##). X peasants are killed
 in the destruction!
 Mystic Advisor Message: N/A
```

### Fool's Gold

The art of turning lead into gold has always been a confusing mystery. Is it possible? No one knows. However, turning gold into lead can be done! This spell will convert a portion of your opponent's gold into worthless lead.

Is Known: Age 12 ... now

```
 Available to: Heretic with a minimum relationship of Unfriendly
 Effect: Destroys up to 25% of target's gold.
 Duration: Instant
 Cast Message: Our mages have turned X gold coins in [Province Name] to worthless lead.
 Mystic Advisor Message: N/A
 Throne Room Notification: X gold coins have been turned into worthless lead.
```

### Greed

People are, by their very nature, greedy individuals. Soldiers have been trained to sacrifice themselves for the greater good. However, this spell reverts the natural greed back into soldiers for several days, causing your opponent to have to pay more in wages and to draft new troops.

Is Known: Age 12 ... now

```
 Available to: All
 Effect: Increases military wages and draft costs by 25%.
 Duration: 
 Cast Message: Our mages have caused our enemy's soldiers to turn greedy for X days.
 Mystic Advisor Message: 
 Throne Room Notification: Enemies have convinced our soldiers to demand more money for upkeep.
```

### Gluttony

One of the seven deadly sins, your population will consume more food.

Is Known: [Age 68](../misc/Age_68.md) ... now

```
 Available to: All
 Effect: Increases food required by 25%.
 Duration: 
 Cast Message: The gluttony of [target] has increased for X days.
 Mystic Advisor Message: A fit of gluttony has descended upon our people, and they will not be sated until for X days.
```

### Lightning Strike

The power of a direct Lightning Strike is arguably the most deadly force on the planet. Your Lightning Strikes will go directly at opponents rune stores and destroy everything in sight. This strike is the most effective way to cripple any opponent's ability to cast spells.

Is Known: Age 1 ... now

```
 Available to: All with a minimum relationship of Unfriendly
 Effect: Destroys a random portion of runes between 30-65%.
 Duration: Instant
 Cast Message: Lightning strikes the Towers in [province name] (##:##) and incinerates X runes!
 Mystic Advisor Message: N/A
```

### Land Lust

Land is the defining strength of any province, and this spell is the Mage's way of simply stealing an opponent's land. This spell is a difficult alternative to attacking.

Is Known: Age 15 ... now

```
 Available to: All with minimum relationship of Unfriendly.
 Effect: Captures a small and random (up to 1.35%) of the enemy land.
 Duration: Instant
 Cast Message: Our Land Lust over Enemy Province (location) has given us X new acres of land!
 Mystic Advisor Message: N/A
 Throne Room Notification: X acres of land have disappeared from our control!
```

### Magic Ward

Projects a magical ward into the skies above an enemy province, forcing the enemy to pour more resources into their spell casts.

Is Known: [Age 72](../misc/Age_72.md) ... [Age 81](../category/Age_81.md), [Age 86](../misc/Age_86.md)... now

```
 Available to: Dark_Elf, with minimum relationship of Unfriendly.
 Effect: Increases target's rune costs by 50%.
 Duration: 
 Cast Message: Unknown
 Mystic Advisor Message: Unknown
```

### Meteor Showers

This spell will rain Meteors across the lands of an opponent for several days, killing peasants, troops and more. Deadly and enduring, casting this spell is both difficult and costly. The damage done, however, can be just as great.

Is Known: Age 12 ... now

```
 Available to: Mystics with minimum relationship of Unfriendly
 Effect: Kills peasants and troops (soldiers, specialists and elites) at home each Utopian Day the
 spell is active.
 Duration: Short-moderate
 Cast Message: Meteors will rain across the lands of [province name] (##:##) for X days
 Mystic Advisor Message: Meteors rain across our lands, and are not expected to stop for X days. 
 Throne Room Notification: Meteors rain across the lands and kill X peasants and X troops!
```

### Mystic Vortex

The Mystic Vortex is one of the more powerful spells in the Utopian World. A successful cast will cause approximately half of the spells currently active over a province to vanish. However, this spell does not discriminate and will nullify both positive and negative spells affecting their lands.

Is Known: Age 1 ... now

```
 Available to: All with a minimum relationship of Unfriendly
 Effect: Nullifies spells on the enemy province (50% chance per spell).
 Duration: Instant
 Cast Message: A magic vortex overcomes the province of [province name] (##:##), negating X active
 spells. 
 Mystic Advisor Message: N/A
 Throne Room Notification: A magic vortex rendered many of our spells inactive!
```

### Nightmares

The effects fear can have on an individual are amazing. By causing nightmares within the soldiers of an opposing army, you may be able to cause them to quiver in fear. Troops having nightmares have to be rehabilitated and are unavailable for a period of time.

Is Known: Age 1 ... now

```
 Available to: Heretic with a minimum relationship of Unfriendly
 Effect: Returns around 1.5% of the military troops (specialists, elites and thieves) under training for 8 days. 
 Will only affect the troops that are at home.
 Soldiers simply quit the army.
 Duration: Instant with duration effect: Troops in training queue stretching 8 days.
 Cast Message: During the night, X of the men in the armies and thieves' guilds of [Province Name]
 had nightmares. 
 Some were forced into rehabilitation, but the soldiers simply quit the army!
 Mystic Advisor Message: N/A
 Throne Room Notification: 
   This morning, X of our men from our armies and thieves' guild turned up unfit. 
   The Soldiers quit, while the rest are being retrained. They should be available again in 8 days.
```

### Pitfalls

Placing magical pitfalls throughout an enemy's lands will cause them to suffer higher defensive losses in combat for several days. This is an effective way to frustrate attackers and strengthen your own position in the midst of [war](Relations.md).

Is Known: Age 14 ... now

```
 Available to: Mystic
 Effect: Increases defensive military losses by 25%.
 Duration: 
 Cast Message: Pitfalls will haunt the lands of [province name] (##:##) for X days. They will suffer
 increased defensive losses during battle. 
 Mystic Advisor Message:
```

### Sloth

Originally called Barrier of Integrity, this spell enchants the enemy's peasantry, calling upon their deep-rooted morals to family and preventing them from signing up for military service.

Is Known: [Age 72](../misc/Age_72.md) ... [Age 81](../category/Age_81.md), [Age 87](../misc/Age_87.md) ... now

```
 Available to: Dark Elf, with minimum relationship of Unfriendly.
 Effect: Reduces drafting within a target province by 50%.
 Duration: Short
 Cast Message: Unknown
 Mystic Advisor Message: Unknown
```

### Storms

The power of mother nature is amongst the most powerful in existence. Sending storms over another province will cause destruction and death across the lands for days. The Storm Spell will cancel any Droughts affecting the target province.

Is Known: Age 1 ... now

```
 Available to: All
 Effect: Kills 1.5% of peasant population per day.
 Duration: 
 Cast Message: Storms will ravage [province name] (##:##) for X days!
 Mystic Advisor Message:
 Throne Room Notification: Storms are ravaging our lands!
```

### Tornadoes

One of the most dangerous and destructive offensive spells, casting this will rain a terror of tornadoes across an opponent's lands, laying waste to acres of buildings across the province.

Is Known: Age 14 ... now

```
 Available to: All with minimum relationship of Unfriendly.
 Effect: Destroys a small and random portion of buildings.
 Duration: Instant
 Cast Message: Tornadoes scour the lands of [province name] (##:##), laying waste to X acres of
 buildings!
 Mystic Advisor Message: N/A
 Throne Room Notification: Tornadoes scour the lands, causing the destruction of X acres of
 buildings!
```

### Vermin

Sending vermin scurrying into the food supplies of an opponent forces the destruction of a great deal of their reserves.

Is Known: Age 1 ... [Age 67](#), [Age 82](../misc/Age_82.md) ... [Age 86](../misc/Age_86.md), [Age 90](../category/Age_90.md) ... now

```
 Available to: Halfling
 Effect: Destroys (on average) about 50% of target's food supplies.
 Duration: Instant
 Cast Message: Unknown
 Mystic Advisor Message: N/A
```

## Retired Spells

### Crystal Eye

Cast on a kingdom instead of an individual province, this option gives a Bird's Eye view of all that has happened across the kingdom of the current and previous months.

Is Known: Age 1 ... [Age 47](#)

```
 Available to: All
 Effect: Displays the targeted provinces Kingdom Paper
 Duration: instant spell
 Cast Message: 
 Mystic Advisor Message:
```

### Fog

Casting a sphere of protection over your province, this spell helps protect your province from invasion from others. This spell can last for a couple of days.

Is Known: Age 1 ... [Age 50](#)

```
 Available to: Dwarf, Faery
 Effect: Increases enemy attack times by 3 hours.
 Duration: max 22 hours
 Cast Message: Our lands are protected by dense fog (Estimated: X more Days).
 Mystic Advisor Message: Our lands are filled with fog, slowing opposing armies for X days!
```

### Hero's Inspiration

The spell helps make your military train harder on their own, thus reducing the daily wages you pay your military for several days. This is especially useful in times of limited cash. This spell also increases the intensity of training, allowing your troops to be ready more quickly; provided the spell is cast before the troops are ordered to be trained.

Is Known: [Age 72](../misc/Age_72.md) ... [Age 80](../misc/Age_80.md), [Age 82](../misc/Age_82.md), [Age 85](../category/Age_85.md) ... [Age 86](../misc/Age_86.md)

```
 Available to: War Hero
 Effect: Decreases your military wages by 30%. Decreases your military training time by 25%. Does not stack with Inspire Army.
 Duration: max 24 hours
 Cast Message: Our army has been inspired to train even harder. We expect maintenance costs to be reduced for X days! 
 Mystic Advisor Message: Same as Cast Message
```

### Illusionary

By creating illusionary forces throughout your lands, it is possible to make an army of men look larger than life. Any crystal balls cast while this spell is active will show a larger-than-normal army.

Is Known: Age 1 ... Age 11

### Miner's Mystique

Mines generally serve as a stable, supplemental source of income. By casting this unique spell, you can substantially increase the money you collect through mining for a period lasting several weeks.

Is Known: Age 1 ... Age 21

### Haste

Haste makes your workers build faster and harder than otherwise. All buildings constructed while the Haste spell is active will be completed faster than otherwise would be expected.

Is Known: Age 3 ... Age 14

### Mind Focus

Science is a fundamental building block for any and all of the other parts of your province. While a Mind Focus spell is active, your students work harder and will learn more than they would otherwise.

Was upgraded to [Fountain of Knowledge](Mystics.md)

Is Known: Age 1 ... [Age 38](../misc/Age_38.md)

### Barrier of Integrity

Stops all drafting that would normally take place in target province.

Was upgraded to [Sloth](Mystics.md)

Is Known: Age 72 ... [Age 80](../misc/Age_80.md)

|  |  |
| --- | --- |
| « Previous:  **[Military](Military.md)** | Next:  **[Thievery](../misc/Thievery.md)** » |

| **The Spellbook** | | | |
| --- | --- | --- | --- |
| Self Spells | Army Spells | Defensive Spells | [Wrathful Smite](Mystics.md)  • [Minor Protection](Mystics.md)  • [Greater Protection](Mystics.md)  • [Animate Dead](Mystics.md)  • [Town Watch](Mystics.md)  • †[Fog](Mystics.md) |
|  |  | Offensive Spells | [Quick Feet](Mystics.md)  • [Anonymity](Mystics.md)  • [War Spoils](Mystics.md)  • [Fanaticism](Mystics.md)  • [Aggression](Mystics.md)  • [Bloodlust](Mystics.md) |
|  |  | Army Spells | [Paladin's Inspiration](Mystics.md)  • [Patriotism](Mystics.md)  • †[Inspire Army](Mystics.md) |
|  | Civil Spells | Mystic Security Spells | [Divine Shield](Mystics.md)  • [Magic Shield](Mystics.md)  • [Mystic Aura](Mystics.md)  • [Nature's Blessing](Mystics.md)  • [Mage's Fury](Mystics.md)  • [Reflect Magic](Mystics.md) |
|  |  | Thievery Spells | [Illuminate Shadows](Mystics.md)  • [Invisibility](Mystics.md)  • [Clear Sight](Mystics.md)  • [Shadowlight](Mystics.md)  • [Crystal Ball](Mystics.md)  • †[Crystal Eye](Mystics.md) |
|  |  | Economy Spells | [Scientific Insights](Mystics.md)  • [Fertile Lands](Mystics.md)  • [Love & Peace](Mystics.md)  • [Tree of Gold](Mystics.md)  • [Builders' Boon](Mystics.md)  • [Revelation](Mystics.md)  • [Paradise](Mystics.md)  • †[Fountain of Knowledge](Mystics.md) |
|  |
| Combat Spells | Economy Damage Spells | Friendly | [Magic Ward](Mystics.md) • [Droughts](Mystics.md) • [Gluttony](Mystics.md)  • [Greed](Mystics.md)  • [Fool's Gold](Mystics.md)  • [Lightning Strike](Mystics.md)  • [Explosions](Mystics.md)  • [Blizzard](Mystics.md)  • †[Vermin](Mystics.md) |
|  |  | Unfriendly | [Magic Ward](Mystics.md) • [Barrier of Integrity](Mystics.md) • [Amnesia](Mystics.md)  • [Tornadoes](Mystics.md)  • [Land Lust](Mystics.md) |
|  | Population Damage Spells | Friendly | [Chastity](Mystics.md)  • [Storms](Mystics.md) |
|  |  | Unfriendly | [Fireball](Mystics.md)  • [Nightmares](Mystics.md)  • [Meteor Showers](Mystics.md) |
|  | Interaction Spells | Friendly | [Expose Thieves](Mystics.md)  • [Pitfalls](Mystics.md) |
|  |  | Unfriendly | [Mystic Vortex](Mystics.md) |

| **Races & Personalities** | |
| --- | --- |
| Races | [Avians](../main/Race.md)  • [Dark Elves](../main/Race.md)  • [Dwarves](../main/Race.md)  • [Elves](../main/Race.md)  • [Faery](../main/Race.md)  • [Halflings](../main/Race.md)  • [Humans](../main/Race.md)  • [Orcs](../main/Race.md)  • [Undead](../main/Race.md) |
| Extinct Races | [Bocans](../main/Race.md)  • [Dryads](../main/Race.md)  • [Gnomes](../main/Race.md) |
| Personalities | [The Cleric](../ages/Personality.md)  • [The Heretic](../ages/Personality.md)  • [The Mystic](../ages/Personality.md)  • [The Artisan](../ages/Personality.md)  • [The Rogue](../ages/Personality.md)  • [The Tactician](../ages/Personality.md)  • [The War Hero](../ages/Personality.md)  • [The Warrior](../ages/Personality.md)  • [The Sage](../ages/Personality.md) |
| Extinct Personalities | [The Raider](../ages/Personality.md)  • [The Freak](../ages/Personality.md)  • [The General](../ages/Personality.md)  • [The Merchant](../ages/Personality.md)  • [The Paladin](../ages/Personality.md)  • [The Shepherd](../ages/Personality.md)  • [The Undead](../ages/Personality.md) |

| **The Utopia Guide** | |
| --- | --- |
| Introduction | [Getting Started with Utopia](../misc/Getting_Started_with_Utopia.md)  • [Creating a province](#)  • [Race](../main/Race.md) & [Personality](../ages/Personality.md) |
| The Menus | [Throne](#)  • [Kingdom](#)  • [News](#) [Explore](../misc/Explore.md)  • [Growth](Growth.md)  • [Science](../misc/Science.md)  • [Military](Military.md)  **Mystics**  • [Thievery](../misc/Thievery.md)  • [War Room](War_Room.md) • [Aid](#)  • [Dragon](../category/Dragons.md)  • [Ritual](../misc/Ritual.md)  [Mail & Forums](#)  [Politics](#)  • [Relations](Relations.md)  • Rankings  • [Preferences](#) |
| Advanced | [MunkBot](../misc/MunkBot.md)  • [Invitations](#)  • [Reservations](../misc/Reservations.md)  • [Utopia](../misc/Utopia.md)  • [Province](../category/Province.md)  • [World of Legends](../category/World_of_Legends.md) |
| Rules | [Game Rules](../misc/Game_Rules.md) |
