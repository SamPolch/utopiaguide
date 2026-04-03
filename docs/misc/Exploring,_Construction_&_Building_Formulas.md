# Exploring, Construction & Building Formulas

flag:delete

Deprecated. Already added content to the [Explore](/misc/Explore.md "Explore") and [Growth](/guide/Growth.md "Growth") pages.

## Construction

### Construction Time

```
Construction Time = 16 * Racial Mod * Personality Mod * Builders Boon * Double Speed * Expedient Ritual Mod * Artisan Science Mod
```

|  |  |  |
| --- | --- | --- |
| **Modifier Type** | **Active** | **Otherwise** |
| **[Builders Boon](/guide/Mystics.md "Mystics")** | 0.75 | 1 |
| **Double Speed** | 0.5 | 1 |
| **Double Speed in Protection** | 0.75 | 1 |
| **War** | 0.75 | 1 |
| **[Expedient Ritual](/misc/Ritual.md "Ritual")** | 0.8 (if at 100% efficiency) | 1 |

### Construction Costs

```
Construction Costs = 0.05*(land+10000) * Race Mod * Mills Mod * Double Speed * Expedient Ritual Mod * Artisan Science Mod
```

|  |  |  |
| --- | --- | --- |
| **Modifier Type** | **Active** | **Otherwise** |
| **Double Speed** | 2 | 1 |
| **Race: Dwarf** | 0.5 | 1 |
| **[Expedient Ritual](/misc/Ritual.md "Ritual")** | 0.75 (if at 100% efficiency) | 1 |

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
- Building Efficiency affects all [Flat Rate](/category/Buildings.md "Buildings") and [Percentage-Based](/category/Buildings.md "Buildings") buildings.
- Building Efficiency has **NO** effect on Capacity component of Capacity Buildings as well as [Universities](/category/Buildings.md "Buildings").

- Changes in Building Efficiency take effect gradually.

|  |  |  |
| --- | --- | --- |
| **Modifier Type** | **Active** | **Otherwise** |
| **Race: Dwarf** | 1.25 | 1 |
| **Dragon: [Topaz](/category/Dragons.md "Dragons")** | 0.75 | 1 |
| **Spell: [Blizzard](/guide/Mystics.md "Mystics")** | 0.9 | 1 |

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
| Introduction | [Getting Started with Utopia](/misc/Getting_Started_with_Utopia.md "Getting Started with Utopia")  • Creating a province  • [Race](/main/Race.md "Race") & [Personality](/ages/Personality.md "Personality") |
| The Menus | Throne  • Kingdom  • News [Explore](/misc/Explore.md "Explore")  • [Growth](/guide/Growth.md "Growth")  • [Science](/misc/Science.md "Science")  • [Military](/guide/Military.md "Military")  [Mystics](/guide/Mystics.md "Mystics")  • [Thievery](/misc/Thievery.md "Thievery")  • [War Room](/guide/War_Room.md "War Room") • Aid  • [Dragon](/category/Dragons.md "Dragons")  • [Ritual](/misc/Ritual.md "Ritual")  • Stances  Mail & Forums  Politics  • [Relations](/guide/Relations.md "Relations")  • Rankings  • Preferences |
| Advanced | [MunkBot](/misc/MunkBot.md "MunkBot")  • Invitations  • [Reservations](/misc/Reservations.md "Reservations")  • [Utopia](/misc/Utopia.md "Utopia")  • [Province](/category/Province.md "Province")  • [World of Legends](/category/World_of_Legends.md "World of Legends")  • Formulas |
| Rules | [Game Rules](/misc/Game_Rules.md "Game Rules") |

| **Buildings** | |
| --- | --- |
| Civil Buildings | [Barren Lands](/category/Buildings.md "Buildings")  • [Homes](/category/Buildings.md "Buildings")  • [Farms](/category/Buildings.md "Buildings")  • [Mills](/category/Buildings.md "Buildings")  • [Banks](/category/Buildings.md "Buildings") |
| Military Buildings | [Training Grounds](/category/Buildings.md "Buildings")  • [Armouries](/category/Buildings.md "Buildings")  • [Barracks](/category/Buildings.md "Buildings")  • [Forts](/category/Buildings.md "Buildings")  • [Castles](/category/Buildings.md "Buildings")  • [Hospitals](/category/Buildings.md "Buildings")  • [Stables](/category/Buildings.md "Buildings")  • [Dungeons](/category/Buildings.md "Buildings") |
| Thievery and Mystic Buildings | [Guilds](/category/Buildings.md "Buildings")  • [Towers](/category/Buildings.md "Buildings")  • [Thieves' Dens](/category/Buildings.md "Buildings")  • [Watchtowers](/category/Buildings.md "Buildings") |
| Science Buildings | [Universities](/category/Buildings.md "Buildings")  • [Libraries](/category/Buildings.md "Buildings") |
