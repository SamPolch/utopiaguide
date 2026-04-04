# Networth

**Networth** is a nominal value in gold coins of a [Province](Province.md)/[Kingdom](#).

# Formula

```
Total Networth =  (Peasants * 0.25) + (Soldiers * Soldier NW) + (Off Specs * Offspec NW) 
     + (Def Specs * Defspec NW) + (Elites * Elite NW) + (Money / 1000) + (Horses * Off value * 0.3) + (Prisoners * Off value * 0.2)
     + (Thieves * 5) + (Wizards * 5) + (Books * 0.000007 * Acres) + (Barren Land * 40)  
     + (Buildings * 60) + (Buildings in Progress * 50)
```

# Table indexes

| **Item** | **NW Value** |
| --- | --- |
| Building (complete) | 60 |
| Building (under construction) | 50 |
| Barren Acre | 40 |

| **Item** | **NW Value** |
| --- | --- |
| Peasant | 0.25 |
| [Soldier](../misc/Units.md) | (Off Points + Def Points) \* 0.25 |
| Soldier (in training) | 0 |
| Offense specialist | Offense Points \* 0.4 |
| Defense specialist | Defense Points \* 0.5 |
| Elite | Variable (see [Race](../main/Race.md) entry) |

| **Item** | **NW Value** |
| --- | --- |
| [Horse](../misc/Units.md) | Offense Points \* 0.3 |
| Prisoner | Offense Points \* 0.2 |
| Thief | 5 |
| Wizard | 5 |
| Food | 0 |
| Runes | 0 |
| [Science Book](../main/Science_Formulas.md) | Acres \* 0.000007 |
