# Difference between revisions of "Economy"

| **[Revision as of 23:26, 18 April 2021](/web/20211026130423//index.php?title=Economy&oldid=9221 "Economy") ([view source](/web/20211026130423//index.php?title=Economy&action=edit&oldid=9221 "Economy"))**[Umajon911](/web/20211026130423//index.php?title=User:Umajon911 "User:Umajon911") ([talk](/web/20211026130423//index.php?title=User_talk:Umajon911&action=edit&redlink=1 "User talk:Umajon911 (page does not exist)") | [contribs](/web/20211026130423//index.php?title=Special:Contributions/Umajon911 "Special:Contributions/Umajon911"))([→](#Military_Expenses_.2F_Wages)‎Military Expenses / Wages)[← Older edit](/web/20211026130423//index.php?title=Economy&diff=prev&oldid=9221 "Economy") | | **[Revision as of 13:35, 25 April 2021](/web/20211026130423//index.php?title=Economy&oldid=9334 "Economy") ([view source](/web/20211026130423//index.php?title=Economy&action=edit&oldid=9334 "Economy"))** [Avenger](/web/20211026130423//index.php?title=User:Avenger "User:Avenger") ([talk](/web/20211026130423//index.php?title=User_talk:Avenger&action=edit&redlink=1 "User talk:Avenger (page does not exist)") | [contribs](/web/20211026130423//index.php?title=Special:Contributions/Avenger "Special:Contributions/Avenger"))m ([→](#Money)‎Money)[Newer edit →](/web/20211026130423//index.php?title=Economy&diff=next&oldid=9334 "Economy") | |
| Line 5: | | Line 5: | |
|  | Banks and population produce money, wizards could cast it from [[Mystics#Tree\_of\_Gold|Tree of Gold]]. |  | Banks and population produce money, wizards could cast it from [[Mystics#Tree\_of\_Gold|Tree of Gold]]. |
|  |  |  |  |
| − | Spend money on Exploration, Building, Training and Wages. | + | Spend money on Exploration, Building, Training, Wages, Dragons or aid your teammates. |
| − |  |  | |
| − |  |  | |
|  |  |  |  |
|  | === Raw Income === |  | === Raw Income === |
| Line 19: | | Line 17: | |
|  | <b>Military Expenses = </b>(((Def specs + Off specs )\*0.5) + Elites \* 0.75) \* Wage Rate \* Armouries Bonus \* [[Race|Race Mod]] \* [[Personality|Personality Mod]] \* max([[Mystics#Inspire\_Army|Inspire Army]] , [[Mystics#Hero's Inspiration|Hero's Inspiration]]) \* [[Mystics#Greed|Greed]] \* [[Science\_Formulas#Science\_Categories.2C\_Types\_and\_Effects|Bookkeeping Science Effect]] |  | <b>Military Expenses = </b>(((Def specs + Off specs )\*0.5) + Elites \* 0.75) \* Wage Rate \* Armouries Bonus \* [[Race|Race Mod]] \* [[Personality|Personality Mod]] \* max([[Mystics#Inspire\_Army|Inspire Army]] , [[Mystics#Hero's Inspiration|Hero's Inspiration]]) \* [[Mystics#Greed|Greed]] \* [[Science\_Formulas#Science\_Categories.2C\_Types\_and\_Effects|Bookkeeping Science Effect]] |
|  |  |  |  |
| − | '''Note''' | + | '''Note:''' |
| − | :Wages are not paid to basic soldiers. | + | \*Wages are not paid to basic soldiers |
| − | :Greed affects provinces as a wage penalty, not an income penalty | + | \*Greed affects provinces as a wage penalty, not an income penalty |
|  |  |  |  |
|  | =Population= |  | =Population= |

---

## Revision as of 13:35, 25 April 2021

# Money

**Gold Coin** (1gc or $1) is Utopian Currency, the base of Utopian Economics.

Banks and population produce money, wizards could cast it from [Tree of Gold](/web/20211026130423//index.php?title=Mystics#Tree_of_Gold "Mystics").

Spend money on Exploration, Building, Training, Wages, Dragons or aid your teammates.

### Raw Income

```
Raw Income = (3 * Employed Peasants) + (1 * Unemployed Peasants) + (0.75 * Prisoners) + (Banks * 25 * BE)
```

### Modified Total Income

```
Modified Income = Raw Income * Plague * Riots * Bank % Bonus * Income Sci * Honor Income Mod 
                  * Race Mod * Personality Mod * Dragon * Ritual
```

### Military Expenses / Wages

```
Military Expenses = (((Def specs + Off specs )*0.5) + Elites * 0.75) * Wage Rate * Armouries Bonus * Race Mod * Personality Mod * max(Inspire Army , Hero's Inspiration) * Greed * Bookkeeping Science Effect
```

**Note:**

- Wages are not paid to basic soldiers
- Greed affects provinces as a wage penalty, not an income penalty

# Population

### Total Population

```
Raw Living Space = ((Built Land + Land in progress) * 25) + (Barren Land * 15) + (Homes * Homes Capacity)  

Mod Living Space = (((Raw Living Space - Homes Bonus) * Race Bonus) + Homes Bonus) * Population Science * Honor Population Bonus
```

**Note**

Honor Bonuses are calculated as 1+(Personality Mod \* Base Honor Bonus)

### Current Population

```
Current Population = Peasants + Soldiers + Off Specs + Off Specs in Training + Def Specs + Def Specs in Training 
                     + Elites + Elites in Training + Thieves + Thieves in Training + Wizards
```

**Note**

Prisoners do not add to the population

## Peasants

### Hourly Change

```
Peasants Hourly Change = (Current Peasants * ((Birth Rate + Love & Peace) * Homes Bonus * EOWCF * Chastity - Storms)) - Drafted Soldiers - Wizards Trained
```

|  |  |  |
| --- | --- | --- |
| **Modifier Type** | **Active** | **Otherwise** |
| **Love & Peace** | 0.85% | 0 |
| **Storms** | 1.5% | 0 |
| **Chastity** | 0 | 1 |

- Base birth rate is 2.05% and ranges from 1.9457% up to 2.1525% (± 5% of 2.05%)
- Base birth rate is increased to ~3% during Protection
- There must be enough living space for peasants to increase
- When a province is overpopulated, the number of peasants will decrease by 10% per tick.

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
Employed Peasants = MIN ( Peasants - Available Jobs - ROUNDDOWN ( Prisoners* / 2 ) )
```

- Note that Prisoners is included in the Employed Peasants calculation for Building Efficiency. Prisoners cannot be considered actual peasants as they do not generate the same amount of gold as employed or unemployed peasants (they only generate 0.75 gold regardless of employment).

### Unemployed Peasants

```
Unemployed Peasants = Peasants - Employed Peasants
```

### Employment Rate

```
Employment Rate = (Employed Peasants / Peasants) * 100
```
