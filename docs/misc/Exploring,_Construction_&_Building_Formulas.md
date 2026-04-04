# Exploring, Construction & Building Formulas

flag:delete

Deprecated. Already added content to the [Explore](Explore.md) and [Growth](../guide/Growth.md) pages.

## Construction

### Construction Time

```
Construction Time = 16 * Racial Mod * Personality Mod * Builders Boon * Double Speed * Expedient Ritual Mod * Artisan Science Mod
```

| **Modifier Type** | **Active** | **Otherwise** |
| --- | --- | --- |
| **[Builders Boon](../guide/Mystics.md)** | 0.75 | 1 |
| **Double Speed** | 0.5 | 1 |
| **Double Speed in Protection** | 0.75 | 1 |
| **War** | 0.75 | 1 |
| **[Expedient Ritual](Ritual.md)** | 0.8 (if at 100% efficiency) | 1 |

### Construction Costs

```
Construction Costs = 0.05*(land+10000) * Race Mod * Mills Mod * Double Speed * Expedient Ritual Mod * Artisan Science Mod
```

| **Modifier Type** | **Active** | **Otherwise** |
| --- | --- | --- |
| **Double Speed** | 2 | 1 |
| **Race: Dwarf** | 0.5 | 1 |
| **[Expedient Ritual](Ritual.md)** | 0.75 (if at 100% efficiency) | 1 |

### Raze Costs

```
Raze Costs = (300+(0.05*land) * Artisan Science Mod
```

## Buildings

### Building Efficiency

```
Available Workers         =  Peasants + ROUNDDOWN ( Prisoners / 2 )

Optimal Workers           =  ROUNDDOWN ( Total Jobs * 0.67 )

% Jobs Performed          =  MIN ( Available Workers / Optimal Workers , 1 )

Building Efficiency       =  (0.5 * (1 + % Jobs Performed)) * Race * Personality * Tools Science * Dragon * Blizzard
```

- The "Current Available Workers" value, provided by the Internal Affairs Adviser page, already takes prisoners into account.
- Building Efficiency affects all [Flat Rate](../category/Buildings.md) and [Percentage-Based](../category/Buildings.md) buildings.
- Building Efficiency has **NO** effect on Capacity component of Capacity Buildings as well as [Universities](../category/Buildings.md).

- Changes in Building Efficiency take effect gradually.

| **Modifier Type** | **Active** | **Otherwise** |
| --- | --- | --- |
| **Race: Dwarf** | 1.25 | 1 |
| **Dragon: [Topaz](../category/Dragons.md)** | 0.75 | 1 |
| **Spell: [Blizzard](../guide/Mystics.md)** | 0.9 | 1 |

### Building Effects

```
Percentage Based Buildings = Base Effect * BE * MIN(50%, % of building * (1 + Race)) * (100% - MIN(50%, % of building * (1 + Race)))
Flat Rate Buildings = Base Effect * (Number of Buildings * (1 + Race)) * BE
```

- In general, the Max Effect of a %-Based Building is 25 x Base Effect (exceptions apply, refer to table)
- If your BE is less than 100%, the effect you would have with 50% of that building is the maximum.
- If you have less than 100% BE, additional buildings past 50% will have no effect.

## Related Links:

| **The Utopia Guide** | |
| --- | --- |
| Introduction | [Getting Started with Utopia](Getting_Started_with_Utopia.md)  • Creating a province  • [Race](../main/Race.md) & [Personality](../ages/Personality.md) |
| The Menus | Throne  • Kingdom  • News [Explore](Explore.md)  • [Growth](../guide/Growth.md)  • [Science](../main/Science_Formulas.md)  • [Military](../guide/Military.md)  [Mystics](../guide/Mystics.md)  • [Thievery](Thievery.md)  • [War Room](../guide/War_Room.md) • Aid  • [Dragon](../category/Dragons.md)  • [Ritual](Ritual.md)  • Stances  Mail & Forums  Politics  • [Relations](../guide/Relations.md)  • Rankings  • Preferences |
| Advanced | [MunkBot](MunkBot.md)  • Invitations  • [Reservations](Reservations.md)  • [Utopia](Utopia.md)  • [Province](../category/Province.md)  • [World of Legends](../category/World_of_Legends.md)  • Formulas |
| Rules | [Game Rules](Game_Rules.md) |

| **Buildings** | |
| --- | --- |
| Civil Buildings | [Barren Lands](../category/Buildings.md)  • [Homes](../category/Buildings.md)  • [Farms](../category/Buildings.md)  • [Mills](../category/Buildings.md)  • [Banks](../category/Buildings.md) |
| Military Buildings | [Training Grounds](../category/Buildings.md)  • [Armouries](../category/Buildings.md)  • [Barracks](../category/Buildings.md)  • [Forts](../category/Buildings.md)  • [Castles](../category/Buildings.md)  • [Hospitals](../category/Buildings.md)  • [Stables](../category/Buildings.md)  • [Dungeons](../category/Buildings.md) |
| Thievery and Mystic Buildings | [Guilds](../category/Buildings.md)  • [Towers](../category/Buildings.md)  • [Thieves' Dens](../category/Buildings.md)  • [Watchtowers](../category/Buildings.md) |
| Science Buildings | [Universities](../category/Buildings.md)  • [Libraries](../category/Buildings.md) |
