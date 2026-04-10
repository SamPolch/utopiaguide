# Attacking & Defending

## Military Efficiency

### Base Military Efficiency

```
Base Military Efficiency = ( 33 + 67 * ( Effective Wage Rate / 100 ) 0.25 ) * Ruby Dragon * Multi-Attack Protection Bonus
```

- Rounded to one decimal point, it should return the most accurate values. Effective Wage Rate lies between 20% (77.8% Efficiency) to 200% (112.7% Efficiency).
- While wages can be changed instantly, the effective wage rate used for base military efficiency changes slowly per tick. It takes approximately 96hrs to go from 20% wages to max at 200% wages.
- **Effective Wage Rate Formula** = (Final Wage Rate - Previous Wage Rate)\* 0.05 - Previous Wage Rate

- **96 Hour Wage Rate Chart**: [ME Chart](https://upload.wikimedia.org/wikipedia/commons/c/cb/ME_Chart.png)

```
Change in Effective Wage Rate =  0.05 * (Wage Rate Paid - Effective Wage Rate)
```

- If wages were not fully paid in the previous tick, Wage Rate Paid will be set at minimum regardless of the amount of wages actually paid.

### Offensive Military Efficiency

```
OME = (Base Military Efficiency + Training Grounds Bonus + Honor Bonus) * Science Bonus * Race Bonus * Personality Bonus * Fanaticism * Bloodlust * Ritual
```

### Defensive Military Efficiency

```
DME = (Base Military Efficiency + Forts Bonus + Honor Bonus) * Science Bonus * Race Bonus * Personality Bonus * Minor Protection * Greater Protection * Fanaticism * Plague * Ritual
```

## Attacking

### Raw Offense

```
Raw Off = (Soldiers * (Soldier Off value + Aggression)) + (Offensive Specs * Off Spec Attack value) + (Elites * Elite Attack value) + (Horses * War Horse Attack value) + [(Mercs * Attack Value + Prisoners * Attack Value)]
```

### Modified Offense

```
Mod Off = Raw Offense * (OME + General Bonus)
```

| **Condition** | **Modifier** |
| --- | --- |
| **OME** | *check your Military Advisor* |
| **General Bonus** | +5% per additional general over 1 |

### Attack Times

```
Attack Time = Base Attack Time * Race Bonus * Personality Bonus * Barracks Bonus * Quick Feet * Attack Type * War * NW Mod * Ritual Bonus
```

- Note: War Attack Speed phases in to -15%, after 12 hours of War have passed.
- There is a net worth value adjustment for attack times. This adjustment compares your net worth to the net worth of the province you are planning to attack. If these are close to each other the base attack times as given below are used. If the net worth differs, then the base attack time is multiplied, so your attack time is longer. This does not affect intra-KD attacks or in War.

#### Base Attack Time

The base attack time is 14 hours. This is the value all calculations are based upon.

| **Location** | ***Intra KD*** | ***Different KD*** |
| --- | --- | --- |
| **Attack Time** | 7 | 14 |

#### Minimum Offense to Win

To guarantee a win, you must send Mod Offense that is at least 1 greater than the defender's Mod Defense.

On Conquest attacks, the minimum Offense to win is 51% of the opponents Defense.

## Attack Gains

For Attacks that target and capture Resources (Traditional March, Conquest, Plunder, Learn), the Gains are calculated as follows:

```
 Gains = Target Resource * Attack Type * RPNW * RKNW * Multi-Attack Protection * Race Modifier * Personality Modifier * Castles Protection * Relations Modifier * Stance Modifier * Siege Science * Emerald Dragon * Attack Time Adjustment Factor * Ritual Bonus * Anonymity * Mist
```

- Resources are defined as: Land, Gold Coins, Food, Runes, Science Books
- Land attacks (except Ambush) also reward Military Credits (target's Defense Points \*.008 \* relative NW \* Military Credits mod) and Building Credits (Acres captured \* 0.4 \* relative NW \* Building Credits mod).
- Raze ignores all modifiers except Relations, [Multi-Attack Protection](../misc/Multi-Attack_Protection_(MAP).md) and the Attack Time Adjustment Factor.
- Massacre ignores most Resource Gains modifiers, except RPNW, RKNW, Relations, [Multi-Attack Protection](../misc/Multi-Attack_Protection_(MAP).md) and the Attack Time Adjustment Factor; Massacre is affected by Massacre Damage mod.
- Ambush ignores all modifiers except increased/decreased Ambush Battle Losses mod.

### Province Networth Factor

```
 Relative Province Networth (rpnw) = Targets Networth / Self Networth
 
 Province Networth Factor = DEPEND ( rpnw ) :
                                     rpnw < 0.567   = 0
                             0.567 < rpnw < 0.9     = 3 * rpnw - 1.7
                             0.9   < rpnw < 1.1     = 1
                             1.1   < rpnw < 1.6     = -2 * rpnw + 3.2
                                     rpnw > 1.6     = 0
```

### Kingdom Networth Factor

```
 Relative Kingdom Networth (rknw) = Target Kingdom Average Prov. Networth / Self Kingdom Average Prov. Networth
 
 Kingdom Networth Factor = DEPEND ( rknw ) :
                                    rknw < 0.5      = 0.8
                              0.5 < rknw < 0.9      = rknw / 2 + 0.55
                                    rknw > 0.9      = 1
```

!!! note
    RKNW is based on the Average Province size of the Kingdom.

!!! note "Editorial Note: Minimum Gains Across Ages"
    The exact gains formula has changed several times across ages, so the
    notes below are an interpretation of the changelog rather than a
    single canonical formula.

    Best supported reading from the age changes:

    - War has had explicit minimum-gains tuning at several points.
        - [Age 57](../history/Age_57.md): minimum gains in War were reduced by 50%.
        - [Age 100](../history/Age_100.md): minimum gains in War were increased from about 3.5% to about 4%.
    - Outside War, the age notes do not document one timeless general minimum-gains floor.
        - What they do show is that older gains formulas could sometimes produce 0-acre edge cases on severe top-feeds.
    - [Age 71](../history/Age_71.md) added a land factor to the gains formula so some attacks that previously yielded 0 acres would now still produce gains.
    - [Age 72](../history/Age_72.md) describes that change more explicitly as replacing pure Networth Based Gains (NWBG) with a hybrid Land Based Gains (LBG) system that still incorporated networth.
    - [Age 73](../history/Age_73.md) then reduced top-feed minimum gains slightly, while also making hostility-based gains throttling more effective.
    - [Age 76](../history/Age_76.md) later removed the land component again and reverted gains to a networth-based formula only.
    - Raze has had its own explicit minimum-gains floors.
        - [Age 90](../history/Age_90.md): Raze floor lowered to 10 acres, or 5 acres when hitting into War stance.
        - [Age 95](../history/Age_95.md): Raze minimum gains changed to 20 acres.
    - Relative Kingdom Networth and relations can also affect realized gains without being minimum-gains rules by themselves.
        - [Age 91](../history/Age_91.md): removed the RKNW factor.
        - [Age 100](../history/Age_100.md): reintroduced the RKNW factor and hostility-meter gains throttling.

    In short: the changelog supports a documented War minimum-gains floor,
    which was about 4% by [Age 100](../history/Age_100.md), plus several
    formula and relation modifiers that can further reduce or increase
    realized gains. It does not support a simple timeless rule like "0 out
    of War, 4% in War" for every age.

### Attack Time Adjustment Factor

Adding or subtracting hours modifies the Gains (based on your Attack Time), as follows:

| **Hours** | **Gains Modifier %** |
| --- | --- |
| **-2** | (-2 / base attack time) \* 160% |
| **-1** | (-1 / base attack time) \* 150% |
| **+1** | (1 / base attack time) \* 80% |
| **+2** | (2 / base attack time) \* 70% |
| **+3** | (3 / base attack time) \* 60% |
| **+4** | (4 / base attack time) \* 50% |

### Attack Type

#### Traditional March

Base gains are 12% and are capped at 20% of your Acres or your opponent's Acres, whichever is smaller.

#### Ambush

Will return 50% of the Acres lost in the attack. Unaffected by Gains modifiers. Inflicts 15% increased Military Casualties.

See the [Ambush guide](Ambush.md) for how to calculate what to send.

#### Plunder

Base gains are 50% gold, 60% food and 60% runes. Max gains is 1.75x base (67.5% gold, 81% runes/food).
Military Casualties on Plunder defense are reduced by 50%.

#### Learn

Steals ~2% of target's allocated Books, plus ~20% of the target's unallocated Books.
Military Casualties on Learn defense are reduced by 50%.
During War, Learn temporarily removes ~30% of total allocated Science Books, these return over 48 Ticks.

#### Raze

Destroys a portion (~5%) of the target's Land. In War, this attack only destroys ~30% Buildings.

#### Conquest

Base gains are 6.8% land for a full hit, Gains are decreased in proportion to the relative Offense sent vs. target's Defense. Available only within 5% Net Worth range outside Hostile/War, unless attacker has access to Enhanced Conquest.

#### Massacre

Base gains are 9.5% peasants, 7.5% Thieves and 5% Wizards. Efficiency increased roughly 3x during War.

## Defending

```
Raw Defense = (Defense Specs * Def Spec Points) + (Elites at Home * Elite's Defense) + (Soldiers *  Sold Def Points * Aggression) + Townwatch
```

```
Mod Defense = MAX ( Raw Defense * Defensive Military Efficiency , Land )
```

| **Modifier Type** | **Active** | **Otherwise** |
| --- | --- | --- |
| **Def Spec Points** | *Variable* | 10 |
| **Elite Defense** | *Variable* |
| **[Town Watch](../guide/Mystics.md#town-watch)** | Peasants / 5 | 0 |

### Minimum Defense

- All land is protected by a minimum of 1 defense per Acre.

That is, if you should send every single Elite and General out, and release your Defense Specialists, an opponent would still need to send 1 Offense point per Acre to conduct a successful attack against you.
This **does not apply** to Intra-Kingdom attacks.

## Military Casualties

Base Military Casualties are 6.5%-8.5% on Offense, 5%-6.5% on Defense.

| **Modifier** | **Type** | **Effect** |
| --- | --- | --- |
| **Building: Hospitals** | All Military Casualties | Varies |
| **Science: Resilience** | All Military Casualties | Varies |
| **Multi-Attack Protection** | Military Casualties | Varies |
| **Attack: Learn** | Defensive Military Casualties | -50% |
| **Attack: Plunder** | Defensive Military Casualties | -50% |
| **Race: Orc** | All Military Casualties | +15% |
| **Ritual: Stalwart** | All Military Casualties | -20% |
| **Ritual: Onslaught** | Offensive Military Casualties inflicted | +15% |
| **Spell: Pitfalls** | Defensive Military Casualties | +15% |
| **Spell: Bloodlust** | Offensive Military Casualties inflicted, Self Military Casualties | +15% |
| **Spell: Salvation** | All Military Casualties | -15% |
| **Spell: Wrath** | Enemy Military Casualties | +20% |
| **Operation: Bribe Generals** | All Military Casualties | 20% chance for +15% |
| **Emerald Dragon** | All Military Casualties | +20% |
