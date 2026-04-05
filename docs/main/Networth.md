# Networth

**Networth** is a nominal gold coin value representing the size and strength of a [Province](Province.md) or Kingdom.

## Formula

```
Total Networth = (Peasants * 0.25) + (Soldiers * Soldier NW) + (Off Specs * Offspec NW)
     + (Def Specs * Defspec NW) + (Elites * Elite NW) + (Money / 1000) + (Horses * Off value * 0.3)
     + (Prisoners * Off value * 0.2) + (Thieves * 5) + (Wizards * 7) + (Books * 0.000007 * Acres)
     + (Barren Land * 40) + (Buildings * 60) + (Buildings in Progress * 50)
```

## NW Reference Table

| Item | NW Value |
| --- | --- |
| Peasant | 0.25 |
| Soldier | (Offense + Defense Points) × 0.25 |
| Soldier (in training) | 0 |
| Offensive Specialist | Offense Points × 0.4 |
| Defensive Specialist | Defense Points × 0.5 |
| Elite | Variable — see [Race](../main/Race.md) |
| Horse | Offense Points × 0.3 |
| Prisoner | Offense Points × 0.2 |
| Thief | 5 |
| Wizard | 7 |
| Food | 0 |
| Runes | 0 |
| Science Book | Acres × 0.000007 |
| Barren Acre | 40 |
| Building (complete) | 60 |
| Building (under construction) | 50 |

See [Units](Units.md) for full unit descriptions and draft/training formulas.
