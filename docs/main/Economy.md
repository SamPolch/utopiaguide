# Economy

# Money

**Gold Coin** (1gc or $1) is Utopian Currency, the base of Utopian Economics.

Banks and population produce money, wizards could cast it from [Tree of Gold](../guide/Mystics.md).

Spend money on Exploration, Building, Training, Wages, Dragons or aid your teammates.

### Raw Income

```
Raw Income = (3 * Employed Peasants) + (1 * Unemployed Peasants) + (0.75 * Prisoners) + Racial Gold Generation + (Banks * 25 * BE) + Miner's Mystique Gold Generation
```

### Modified Total Income

```
Modified Income = Raw Income * Plague * Riots * Bank % Bonus * Income Sci * Honor Income Mod 
                  * Race Mod * Personality Mod * Dragon * Ritual
```

### Military Expenses / Wages

```
Military Expenses = (((Def specs + Off specs ) * 0.5) + Elites * 0.75) * Wage Rate * Armouries Bonus * Race Mod * Personality Mod * max(Inspire Army , Hero's Inspiration) * Greed * Ritual * Dragon * Bookkeeping Science Effect
```

**Note**

- Wages are not paid to basic soldiers
- Greed affects provinces as a wage penalty, not an income penalty

# Population

### Total Population

```
Raw Living Space = ((Built Land + Land in progress) * 25) + (Barren Land * 15) + (Homes * Homes Capacity)  

Mod Living Space = Raw Living Space * Race Bonus * Population Science * Honor Population Bonus
```

**Note**

- Honor Bonuses are calculated as 1 + (Personality Mod \* Honor Bonus)

### Current Population

```
Current Population = Peasants + Soldiers + Off Specs + Off Specs in Training + Def Specs + Def Specs in Training 
                     + Elites + Elites in Training + Thieves + Thieves in Training + Wizards
```

**Note**

- Prisoners do not add to the population

## Peasants

### Hourly Change

```
Peasants Hourly Change = (Current Peasants * ((Birth Rate + Love & Peace) * Race Bonus * Hospitals Bonus * EOWCF * Chastity - Storms)) + (Homes bonus * Chastity) - Drafted Soldiers - Wizards Trained
```

| **Modifier Type** | **Active** | **Otherwise** |
| --- | --- | --- |
| **Love & Peace** | 0.85% | 0 |
| **Storms** | 1.5% | 0 |
| **Chastity** | 0.5 | 1 |

**Note**

- Base birth rate is 2.05% and ranges from 1.9457% up to 2.1525% (± 5% of 2.05%)
- Base birth rate is increased to ~3% during Protection
- There must be enough population space for peasants to increase
- When a province is overpopulated, the number of peasants will decrease by 10% per tick

## Employment

### Available Jobs

```
Available Jobs = (Completed Buildings - Homes) * 25
```

### Unfilled Jobs

```
Unfilled Jobs = MAX ( Available Jobs - Peasants - ROUNDDOWN( Prisoners / 2 ) , 0 )
```

### Employed Peasants

```
Employed Peasants = MIN ( Peasants , Available Jobs - (ROUNDDOWN ( Prisoners* / 2 )) )
```

**Note**

- Prisoners are included in the Employed Peasants calculation for Building Efficiency. Prisoners are not considered actual peasants, as they do not generate the same amount of gold as employed or unemployed peasants (they only generate 0.75 gold regardless of employment)

### Unemployed Peasants

```
Unemployed Peasants = MIN(Peasants - Employed Peasants)
```

### Employment Rate

```
Employment Rate = (Employed Peasants / Peasants) * 100
```
