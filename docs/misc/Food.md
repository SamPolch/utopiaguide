# Food

**Food** is a resource, and it is needed to keep population of a [Province](/category/Province.md "Province") alive. It's measured in **bushels**.

## Food Consumed

```
Bushels Eaten = Total Population * 0.25 * Race Mod * Gluttony Mod
```

|  |  |  |
| --- | --- | --- |
| **Modifier Type** | **Active** | **Otherwise** |
| Race: [Undead](/main/Race.md "Race") | 0 | 1 |
| Race: [Dwarf](/main/Race.md "Race") | 1.5 | 1 |
| Spell: [Gluttony](/guide/Mystics.md "Mystics") | 1.25 | 1 |

- If a province has zero food, it will enter into a state of starvation. While a province is starving, its population (peasants, military units and thieves) will die off at a rate proportional to the food deficit (this also includes armies away from home). Wizards are not affected. This rate is capped at 5% and will continue until the province has a value for food greater than 0.

## Food Produced

```
Base Food Production     = ((Farms * 60) * Building Efficiency) + (Barren Land * 2) + (Race Mod * Acres) + (Personality Mod * Acres)
 
Modified Food Production = Base Food Production * Production Science Mod * Fertile Lands Mod * Drought Mod * Honor Mod
```

|  |  |
| --- | --- |
| **Condition** | **Modifier** |
| [Fertile Lands](/guide/Mystics.md "Mystics") | 1.25 |
| [Drought](/guide/Mystics.md "Mystics") | 0.75 |

## Food Decayed

```
Food Remaining = Food Stock * 0.99 + Modified Food Production - Bushels Eaten
```

0.99 or about 1% of the total food stock decays in normal conditions. The exact amount depends on the modifiers in the formula as provided above and it is calculated on the total food stored in the province. So if a province has 300,000 bushels of food in stock under normal conditions, then the expected decay is slightly less or more than 3000 bushels per tick / Utopia day. There may be scenarios where the total food decayed, is higher than what remains after food needed by the population is consumed from the food grown. This may lead to depletion of the stock in the province especially after a war when the people are much lesser compared to the maximum population limit and the stored food may be much higher or when a new player has built a lot of farms / received aid as food. This will normalize once the population reaches back to expected levels and the province only needs to ensure that the food grown is more than the food needed by the population at all times so as to avoid starvation.

| **The Utopia Guide** | |
| --- | --- |
| Introduction | [Getting Started with Utopia](/misc/Getting_Started_with_Utopia.md "Getting Started with Utopia")  • Creating a province  • [Race](/main/Race.md "Race") & [Personality](/ages/Personality.md "Personality") |
| The Menus | Throne  • Kingdom  • News [Explore](/misc/Explore.md "Explore")  • [Growth](/guide/Growth.md "Growth")  • [Science](/misc/Science.md "Science")  • [Military](/guide/Military.md "Military")  [Mystics](/guide/Mystics.md "Mystics")  • [Thievery](/misc/Thievery.md "Thievery")  • [War Room](/guide/War_Room.md "War Room") • Aid  • [Dragon](/category/Dragons.md "Dragons")  • [Ritual](/misc/Ritual.md "Ritual")  • Stances  Mail & Forums  Politics  • [Relations](/guide/Relations.md "Relations")  • Rankings  • Preferences |
| Advanced | [MunkBot](/misc/MunkBot.md "MunkBot")  • Invitations  • [Reservations](/misc/Reservations.md "Reservations")  • [Utopia](/misc/Utopia.md "Utopia")  • [Province](/category/Province.md "Province")  • [World of Legends](/category/World_of_Legends.md "World of Legends")  • Formulas |
| Rules | [Game Rules](/misc/Game_Rules.md "Game Rules") |
