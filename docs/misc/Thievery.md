# Thievery

No one ever said leadership involves only public activities. With a state-sanctioned paramilitary thieves guild available to you, the possibilities are endless. What may not be possible through [war](../guide/Relations.md) or [magic](../guide/Mystics.md) may still be possible with deceit and deception. Never underestimate the power of the underground unknown.

Thieves are professional soldiers, trained in the arts of the elite underground and are trained on your [Military](../guide/Military.md) Menu. They maintain a Stealth Rating which determines when they can be used. This rating rises automatically each day by 3 points and drops each time your thieves conduct an operation. Your thieves will not carry out missions without at least a 5% Stealth Rating.

The best measure of your guild's strength is the number of thieves you maintain per acre of land, often known as Thieves Per Acre (TPA), modified by your Thieves' Dens, your Crime science and your [racial](../main/Race.md) bonuses or penalties. The success rate of your guild depends on both your and your target's TPA. The raw damage, however, is based on raw strength - the more thieves you use in an operation, the more damage they can do.

The larger your province, the more difficult it will be to keep your guild well-organized and efficient. As your province grows larger, be prepared to keep training additional thieves to keep your network intact and effective. Like most things in Utopia, thievery operations are easier and more effective against provinces similar to you in size.

Thievery operations are divided in two categories:

- [Espionage Operations](#the-thieves-toolbox-the-espionage-operations)
- [Sabotage Operations](#the-thieves-toolbox-the-sabotage-operations)

## Modified TPA

The success of each operation depends on the two provinces' relative modified TPA, as well as other thief defences like the spell Clear Sight and Watchtowers.

Your TPA can be affected by your race, personality, buildings, science, rituals, and dragons:

```
Modified TPA = Raw TPA × Invisibility × Crime Science × Racial Mod × Thieves Dens Bonus × Honor Bonus × Ritual Bonus
```

| Modifier | Value |
|---|---|
| Invisibility (spell) | 1.1 |
| Ritual: Havoc | 1.2 |
| Crime Science | varies |

## The Thieves' Toolbox: The Espionage Operations

The espionage operations will simply gather information regarding the enemy province.
Nevertheless, sending **5% of your thieves will return completely accurate results** .

### Spy on Throne

```
 Available to:       All
 Relations Required: All
 Effect:             Shows the target province's Throne page information, including race, honor,
                     resources and military strength (excludes wizards and thieves).
 Difficulty:         very low
 Stealth cost:       1%
 Meter Movemement:   0
```

### Spy on Defense

Reports enemy's standing defenses.

```
 Available to:       All
 Relations Required: All
 Effect:             Reveals Net Defensive Points at Home (troop defense only; if troop defense is
                     lower than acres, the acre value is used instead).
 Difficulty:         very low
 Stealth cost:       1%
 Meter Movemement:   0
```

### Spy on Exploration

Gives current pool size, and costs per acre in gold and soldiers.

```
 Available to:       All
 Relations Required: All
 Effect:             Reveals pool size, and costs per acre in gold and soldiers.
 Difficulty:         very low
 Stealth cost:       2%
 Meter Movemement:   0
```

### Snatch News

```
 Available to:       All
 Relations Required: All
 Effect:             Shows the target province's kingdom news for the current and previous Utopian month.
 Difficulty:         low
 Stealth cost:       2%
 Meter Movement:     0
```

### Infiltrate

Reports on the size of your opponent's guild.

```
 Available to:       All
 Relations Required: All
 Effect:             Shows the total number of thieves the target province has.
 Operation Message:  Our thieves have infiltrated the Thieves' Guilds of [province name] (##:##). They appear to have about X thieves employed across their lands.
 Difficulty:         low
 Stealth cost:       2%
 Meter Movement:     0
```

### Survey

Reports on the distribution of buildings in a province.

```
 Available to:       All
 Relations Required: All
 Effect:             Shows the target's completed buildings, building efficiency, building effects,
                     and buildings in progress. Does not show construction in progress.
 Operation Message:
 Difficulty:         low
 Stealth cost:       2%
 Meter Movemement:   0
```

### Spy on Military

Provides detailed information from your opponent's army.

```
 Available to:       All
 Relations Required: All
 Effect:             Shows the target's military efficiency; number of each unit type at home and out on
                     attacks; return times on armies not at home; and troops in training per unit type.
 Operation Message:
 Difficulty:         low
 Stealth cost:       2%
 Meter Movemement:   0
```

### Spy on Sciences

Estimates strengths and effects of opponent's science levels.

```
 Available to:       All
 Relations Required: All
 Effect:             Shows the number of books the target has invested in each science type, and the
                     total number of unassigned books in each category.
 Operation Message:
 Difficulty:         low
 Stealth cost:       2%
 Meter Movement:     0
```

### Calculating WPA

No intel operation directly reveals an enemy's wizard count, but wizards contribute to networth. With a full set of intel ops you can back-calculate WPA. Run all four of the following on the same Utopian day (ideally back-to-back, since ops or attacks between them can skew results):

- Spy on Throne
- Infiltrate
- Spy on Sciences
- Survey

Spy on Military is not needed — it only shows troop positions, not totals. Once you have consistent data, the remaining networth unexplained by land, troops, thieves, science, and buildings belongs to wizards.

## The Thieves' Toolbox: The Sabotage Operations

Listed here is a short reference guide to each of the offensive operations available to you and their effects. As mentioned previously, sending more thieves will increase the strength of these operations. Nevertheless, sending too many thieves also increases the chances that the enemy catches your men! Certain operations are designated Unfriendly, Hostile or [War](../guide/Relations.md) Only operations -- Because of the destructive nature of these operations, they can be run only against provinces which have at least a certain level of relations with your kingdom. In addition, you will find that many operations are more effective during heightened relations conditions.

### Formulas

**Optimal thieves to send** for an instant sabotage op:

```
Thieves to Send = (Target Resources × Max % of Total) / Gains Per Thief / Racial Mod
```

Target resources can be found with Spy on Throne. Max % of Total and Gains Per Thief are in the individual op entries below.

**Thievery yield** (what you actually receive):

```
Yield = Thieves Sent
      × MIN(Target NW / Self NW, Self NW / Target NW)  [+ War Bonus]
      × Gains Per Thief
      × (1 − Resources Lost)
      × Racial Mod × Personality Mod × Guile × Cunning
      × Target Race Mod × Target Personality Mod
      × Target Illuminate Shadows
      × (1 − Target Watchtowers effect)
      × (1 − Target Shielding)
      × Stance
```

The NW ratio term means gains are penalised when hitting a much larger or smaller target. Resources Lost is the fraction that is destroyed rather than transferred (e.g. 50% for Steal War Horses).

**Duration ops** have a random component, but the minimum, average, and maximum durations all scale with the number of thieves sent. Oversending on Riots reduces duration. Effects like Guile and the Heretic personality do affect duration ops (unlike duration spells).

### Sabotage Wizards

Drains the target's Mana levels for several days, limiting the ability to cast spells.

```
 Available to:       All
 Relations Required: Unfriendly
 Effect:             Reduces Mana level by 5% of current level each Tick, before Mana regeneration.
 Operation Message:  Our thieves have sabotaged their wizards' ability to cast spells.
 Difficulty:         medium
 Meter Movement:     0
```

### Destabilize Guilds

Decreases the target’s Spell Duration for several days.

```
 Available to:       Rogues
 Relations Required: All
 Effect:             Decreases the target’s Duration of Self Spell and Offensive Spell casts while the effect is active by 20%.
 Operation Message:  
 Difficulty:         medium
 Meter Movement:     0
```

### Rob the Granaries

Steals food from your opponent's storages.

```
 Available to:       All
 Relations Required: All
 Effect:             Steals up to a max of 31.5% (46% in war) enemy food at the rate of 95 (135 in war) bushels per thief.
 Operation Message:  Our thieves have returned with X bushels.
 Difficulty:         medium
 Meter Movemement:   0.06
```

### Rob the Vaults

Steals gold from enemy coffers.

```
 Available to:       All
 Relations Required: All
 Effect:             Steals up to a max of 5.2% (14% in war) enemy gc at the rate of 40 (106 in war) gc per thief.
 Operation Message:  Our thieves have returned with X gold coins.
 Difficulty:         medium
 Meter Movement:     0.12
```

### Rob the Towers

Steals runes from your target's wizards.

```
 Available to:       All
 Relations Required: All
 Effect:             Steals up to a max of 24.5% (35% in war) enemy runes at the rate of 18.2 (26 in war) runes per thief.
 Operation Message:  Our thieves were able to steal X runes.
 Difficulty:         medium
 Meter Movement:     0.09
```

### Kidnapping

Kidnaps peasants from your enemy and brings them to your province.

```
 Available to:       All
 Relations Required: All
 Effect:             Steals up to a max of 1.85% (4% in war) enemy peasants at the rate of 0.132 (0.285 in war) peasants per thief.
 Operation Message:  Our thieves kidnapped many people, but only were able to return with X of them.
 Difficulty:         medium
 Meter Movement:     0.12
```

!!! note
    Kidnapping gains drop by 50% when the target province reaches a low population level, to make player-killing harder.

### Arson

Burns down enemy buildings to disrupt an enemy's stability.

```
 Available to:       All
 Relations Required: All
 Effect:             Destroys a small amount of enemy buildings.
 Operation Message:  Our thieves burned down X acres of buildings. OR  Unfortunately, our thieves were too few in number to find any buildings to burn.
 Difficulty:         medium
 Meter Movement:     0.24
```

### Greater Arson

A more powerful version of Arson, this operation allows targetting of a specific type of building to burn down. Only Rogues can master this difficult operation.

```
 Available to:       Rogues
 Relations Required: Unfriendly
 Effect:             Destroys up to a max of ~6% of targeted enemy buildings at the rate of 0.0045 buildings per thief.
 Operation Message:  Our thieves burned down X [building type].
 Difficulty:         Medium
 Meter Movement:     0.3
```

### Night Strike

Assassinates a portion of your enemy's military, both at home and away.

```
 Available to:       All
 Relations Required: Unfriendly
 Effect:             Kills up to a maximum of 16.25% enemy soldiers at a rate of 0.67 soldiers per thief.
                     Also kills a much smaller amount of specialists and elites. Will affect all troops, even those that aren't home.
 Operation Message:  Our thieves assassinated X enemy troops.  
 Difficulty:         medium
 Meter Movement:     0.24
```

### Incite Riots

Incites riots which disrupt tax collection efforts for several days.

- Duration capped to 18 at age 95
- The More thieves you send the higher your min, avg, max duration will be
- Unaffected by Sabotage damage bonus

```
 Available to:       All
 Relations Required: All
 Effect:             Decreases targets income by 15%.
 Operation Message:  Our thieves have caused rioting. It is expected to last X days.
 Difficulty:         medium
 Meter Movement:     0.18
```

### Steal War Horses

Steals an enemy's horses for your own use.

```
 Available to:       Rogue
 Relations Required: Unfriendly
 Effect:             Steals up to 13.6% (12.75% OOW) of the target's horses at a rate of 0.1 (0.094 OOW)
                     horses per thief. Only half are kept; the rest are released.
 Operation Message:  Our thieves were able to release X horses but could only bring back Y of them.
 Difficulty:         medium
 Meter Movement:     0.18
```

### Bribe Thieves

Reduces the ability of an enemy thieves' guild to conduct and defend against thievery operations until the double agents are caught by the enemy.

```
 Available to:       All
 Relations Required: All
 Effect:             Reduces thief effectiveness by 10%
 Operation Message:  Our thieves have bribed members of our enemies' guild!
 Difficulty:         medium
 Meter Movement:     0.09
```

### Bribe Generals

Increases the losses sustained by your enemy in all combat until the bribed generals are discovered by the opponent.

```
 Available to:       All
 Relations Required: All
 Effect:             Effectively a 1 in 5 chance per attack to increase troop losses by 20% on all combat.
 Operation Message:  Our thieves have bribed an enemy general!
 Difficulty:         medium
 Meter Movement:     0.09
```

### Free Prisoners

Releases prisoners from an opponent's dungeons. You gain half of them.

```
 Available to:       All
 Relations Required: All
 Effect:             Releases up to a max of 12% (17% in war) of the targets prisoners at a rate of 0.06 (0.07 in war) prisoners per thief.
 Operation Message:  Our thieves freed X prisoners from enemy dungeons.
 Difficulty:         medium
 Meter Movement:     0.03
```

### Assassinate Wizards

Attempts to assassinate enemy wizards to permanently weaken their ability to cast spells. Only Rogues can master this difficult operation.

```
 Available to:       Rogues
 Relations Required: Unfriendly
 Effect:             Kills up to a max of ~1.6% (~1.4% OOW) target wizards at a rate of ~0.008 (~0.007 OOW) wizards per thief.
 Operation Message:  Our thieves assassinated X wizards of the enemy's guilds!
 Difficulty:         high
 Meter Movement:     0.36
```

### Propaganda

Attempts to convince enemy peasants, military, or wizards to revolt and join your province. Only Rogues can master this difficult operation.

```
 Available to:       Rogues
 Relations Required: War
 Effect:             not fully determined
 Operation Message:  We have converted X [wizards, thieves, soldiers] from the enemy to our guild.
                     OR  We have converted X [of the enemy's specialist troops, (elite unit name) from the enemy] to our army.  
 Difficulty:         high
 Meter Movement:     0 (War Only)
```

## Stealth Costs

Each operation costs stealth. Stealth regenerates at 3% per day (Rogues receive more). Operations cannot be performed below 5% stealth.

| Operation type | Stealth cost |
|---|---|
| Spy on Throne, Spy on Defense | 1% |
| All other espionage operations | 2% |
| Sabotage (hostile relations or higher) | 2% |
| Sabotage (no special relations) | 3% |

The spell Expose Thieves reduces a province's stealth by 5% of its current stealth before regeneration is added each tick. For example, at 50% stealth, Expose Thieves reduces it to 47.5% (rounded to 48%) before the tick's regeneration is applied.

## Changelog

- Age 106: Meter movements updated to reflect forum changes of "all values have tripled" on 6 May 2024.
- Age 106: NS updated to reflect 25% more damage on 29 May 2024.
