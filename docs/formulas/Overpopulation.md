# Difference between revisions of "Overpopulation"

| **[Revision as of 02:26, 4 February 2019](#) ([view source](#))**[Avenger](#) ([talk](#) | [contribs](#))m ([→](#Effects_and_Triggers_for_Overpopulation)‎Effects and Triggers for Overpopulation)[← Older edit](#) | | **[Latest revision as of 21:32, 14 August 2019](#) ([view source](#))** [Avenger](#) ([talk](#) | [contribs](#))m | |
| Line 1: | | Line 1: | |
| − | Overpopulation occurs when your Total Population exceeds your Maximum Population and can be viewed in your Affairs of the State page. | + | Overpopulation occurs when your Total Population exceeds your Maximum Population, and can be viewed in your Affairs of the State page. |
|  |  |  |  |
|  | ===Effects and Triggers for Overpopulation=== |  | ===Effects and Triggers for Overpopulation=== |
| − |  |  | |
| − | Note: these effects stack. |  | |
|  |  |  |  |
|  | \* Population exceeds Max Population: Your peasants will leave and no new peasants will be born. Peasants leave at a rate of ~10.5% of total peasants or the amount you are overpopulated by, whichever of the two is lower. The minimum that will leave is 10. |  | \* Population exceeds Max Population: Your peasants will leave and no new peasants will be born. Peasants leave at a rate of ~10.5% of total peasants or the amount you are overpopulated by, whichever of the two is lower. The minimum that will leave is 10. |
| Line 14: | | Line 12: | |
|  |  |  |  |
|  | \* Your army will also refuse to attack if your total army exceeds your maximum population. |  | \* Your army will also refuse to attack if your total army exceeds your maximum population. |
|  | | + |  |
|  | | + | Note: '''These effects stack.''' |
|  |  |  |  |
|  | ===Troops Desertions=== |  | ===Troops Desertions=== |
|  |  |  |  |
| − | All population except Wizards are prone to desertions when overpopulated and leave at the same rate. The Exact current mechanics have not been calculated, though are currently estimated at a max of 4.6% per tick. <br> | + | All troops except are prone to desertions when overpopulated and leave at the same rate. |
|  | | + |  |
|  | | + | The exact current numbers have not been calculated, though desertions are currently estimated to max at ~5.8% per tick. |
|  | | + |  |
|  | Desertions due to overpopulation will remove soldiers first, up to a maximum of 50% of the total desertions. |  | Desertions due to overpopulation will remove soldiers first, up to a maximum of 50% of the total desertions. |
|  |  |  |  |
|  | [[Category:Formulas]] |  | [[Category:Formulas]] |
|  | | + |  |
|  | | + |  |
|  | | + |  |
|  | | + |  |
|  |  |  |  |
|  | ===Past Mechanics=== |  | ===Past Mechanics=== |

---

## Latest revision as of 21:32, 14 August 2019

Overpopulation occurs when your Total Population exceeds your Maximum Population, and can be viewed in your Affairs of the State page.

### Effects and Triggers for Overpopulation

- Population exceeds Max Population: Your peasants will leave and no new peasants will be born. Peasants leave at a rate of ~10.5% of total peasants or the amount you are overpopulated by, whichever of the two is lower. The minimum that will leave is 10.

- Population exceeds Max Population by 15%: Your army will refuse to attack and your troops (including thieves) will begin to desert. Troops desert at a currently unknown rate and effect all military both at home and out on an attack

- Population exceeds Max Population by 20%: Your thieves will refuse to work.

- Population exceeds Max Population by 35%: Your peasants will riot and your income is reduced by 50%.

- Your army will also refuse to attack if your total army exceeds your maximum population.

Note: **These effects stack.**

### Troops Desertions

All troops except are prone to desertions when overpopulated and leave at the same rate.

The exact current numbers have not been calculated, though desertions are currently estimated to max at ~5.8% per tick.

Desertions due to overpopulation will remove soldiers first, up to a maximum of 50% of the total desertions.

### Past Mechanics

Military Deserted at a rate of 20% the amount you are overpopulated, calculated after peasants leave. Troop losses are calculated on all troops but only troops that are home will leave (troops out are immune from desertion, but will influence the total amount of troops that leave). These losses are calculated individually for each troop type. If you have sufficient soldiers then they can desert in place of a particular troop type, see formula for full calculation.

```
Total Unit Desertions = Leet Desertions + Thief Desertions + Defspecs Desertions + OffSpecs Desertions + Solds Desertions
```

```
Metric = MIN [ 1 , 0.046* [(Current population-Peasants*0.07)/Max population - 1] ]
```

```
Leet Desertions = IF [(Leets home * Metric) > Solds home] Then (Leets home * Metric) Else 0
```

```
Thieves Desertions = IF [(Thieves home * Metric) > (Solds home - Leet desertions)] Then (Thieves home* Metric) Else 0
```

```
Def Specs Desertions = IF [(Defspecs home * Metric) > (Solds home - Leet desertions - Thieves desertions)] Then (Defspecs home* Metric) Else 0
```

```
Off Specs Desertions = IF [(OffSpecs home * Metric) > (Solds home - Leet desertions - Thieves Desertions - Def Spec Desertions)] Then (OffSpecs home* Metric) Else 0
```

```
Solds Desertions = Max[(Solds home-{Leet Desertions + Thief Desertions + Defspecs Desertions + OffSpecs Desertions}) * Metric,0]
```
