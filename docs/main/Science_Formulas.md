# Science Formulas

Sciences are the study of knowledge and create our pathway into the future. By studying the laws that govern our being and understanding the effects of these laws, we can strengthen ourselves in all that we do. The mystery of magic and thievery, our military prowess, even our methods of production can all be enhanced through the power of study with an investment in time devoted to those fields. The students of our province will lead us into the future with your careful direction.

Mastering the Arts & Sciences makes your people stronger, smarter, and more efficient. You can grow in strength without growing in size.

Details on the benefits of different sciences can be found below.

## Science Categories, Types and Effects

Check out the Guide for descriptions: [https://utopia-game.com/guide/](https://utopia-game.com/guide/), then go to Science in the navigation menu.

|  |  |  |  |
| --- | --- | --- | --- |
| **Science Category** | **Type** | **Effect** | **Multiplier** |
| **Economy** | Alchemy | Income | ~0.0724 |
|  | Tools | Building Effectiveness | ~0.0524 |
|  | Housing | Population Limits | ~0.0262 |
|  | Production | Food & Rune Production | ~0.2172 |
|  | Bookkeeping | Wage Reduction | ~0.068 |
|  | Artisan | Construction Time Reduction, Construction & Raze Cost Reduction | ~0.0478 |
| **Military** | Strategy | Defensive Military Efficiency | ~0.0367 |
|  | Siege | Battle Gains | ~0.0262 |
|  | Tactics | Offensive Military Efficiency | ~0.0367 |
|  | Valor | Reduced Military Train Time & Increased Dragon Slaying Strength | ~0.0582 |
|  | Heroism | Draft Speed & Draft Costs Reduction | ~0.0418 |
|  | Resilience | Reduced Military Casualties | ~0.0489 |
| **Arcane Arts** | Crime | Thievery Effectiveness | ~0.1557 |
|  | Channeling | Magic Effectiveness | ~0.1875 |
|  | Shielding | Reduced Damage from Enemy Thievery and Magic Instant Operations | ~0.0314 |
|  | Sorcery | Increased Magic Instant Damage | ~0.0314 |
|  | Cunning | Increased Thievery Operation Damage | ~0.0314 |
|  | Finesse | Reduced Wizards and Thieves lost on Failed Spells and Operations | ~0.0965 |

## Science Formula

```
Science Bonus = ( # of Books in Type )^(1/2.125) * Science Multiplier * Race Mod * Personality Mod * Amnesia Effect * Scientific Insights Mod * Libraries Mod
```

## Scientists and Books

- Each province starts with a set number of Scientists assigned to the three science Categories (**Economy, Military, Arcane Arts**).
- Scientists start out as Recruits, then as they progress they provide incrementally greater benefits with each progression.
- Scientist experience is based on how many Books they have produced in that category.
- Scientists have no Networth value.
- Scientists can be re-assigned at any time, but revert to Recruit level when doing so.
- Every tick each province builds progress towards a new scientist. Universities increase the rate of this progress.
- Scientists produce a set number of books each tick in the Category they are allocated (**Economy, Military, Arcane Arts**), based on their rank. Schools increase this effect.
- Books can be allocated to any science Type within the Category they have been produced.
- Allocated books go into effect instantly.
- Inactive provinces do not produce Books.

### Scientist Spawn Rate Formula

```
Scientists Spawn Rate = 2 * Race Mod * Universities Effect * Revelation Mod
```

### Scientist Ranks and Production

|  |  |  |
| --- | --- | --- |
| **Rank** | **Experience** | **Book Production** |
| **Recruit** | 0-1439 | 60 |
| **Novice** | 1440-5279 | 80 |
| **Graduate** | 5280-12479 | 100 |
| **Professor** | 12480+ | 120 |

### Re-assigning Scientists

Re-assigning scientists drops them back to a recruit. Refer to this forum post for a discussion on this topic: [http://forums.utopia-game.com/showthread.php?639982-A-Question-About-Ticks-amp-Buildings](http://forums.utopia-game.com/showthread.php?639982-A-Question-About-Ticks-amp-Buildings)

## Science Efficiency

Some Races and Personalities gain or lose Science Efficiency, as follows:

|  |  |  |
| --- | --- | --- |
| **Race/Pers** | **Category** | **Efficiency** |
| Human | All | 1.1 |
| Artisan | Artisan | 1.25 |
| Cleric | Resilience | 1.25 |
| Heretic | Sorcery | 1.25 |
| Merchant | Income | 1.25 |
| Mystic | Channeling | 1.25 |
| Rogue | Crime | 1.25 |
| Shepherd | Shielding | 1.25 |
| Tactician | Siege | 1.25 |
| War Hero | Strategy | 1.25 |
| Warrior | Tactics | 1.25 |

## Science Networth

Books are worth [0.000006 \* Current Land] points.

## Obsolete and historical data - saved for reference

Historical information on science systems and formulas can be found here: **[Science: Obsolete and historical data](/misc/Science_Obsolete_and_historical_data.md)**

|  |  |
| --- | --- |
| « Previous:  **[Growth](/guide/Growth.md)** | Next:  **[Military](/guide/Military.md)** » |

| **The Utopia Guide** | |
| --- | --- |
| Introduction | [Getting Started with Utopia](/misc/Getting_Started_with_Utopia.md)  • [Creating a province](#)  • [Race](/main/Race.md) & [Personality](/ages/Personality.md) |
| The Menus | [Throne](#)  • [Kingdom](#)  • [News](#) [Explore](/misc/Explore.md)  • [Growth](/guide/Growth.md)  • [Science](/misc/Science.md)  • [Military](/guide/Military.md)  [Mystics](/guide/Mystics.md)  • [Thievery](/misc/Thievery.md)  • [War Room](/guide/War_Room.md) • [Aid](#)  • [Dragon](/category/Dragons.md)  • [Ritual](/misc/Ritual.md)  • [Stances](#)  [Mail & Forums](#)  [Politics](#)  • [Relations](/guide/Relations.md)  • Rankings  • [Preferences](#) |
| Advanced | [MunkBot](/misc/MunkBot.md)  • [Invitations](#)  • [Reservations](/misc/Reservations.md)  • [Utopia](/misc/Utopia.md)  • [Province](/category/Province.md)  • [World of Legends](/category/World_of_Legends.md)  • [Formulas](#) |
| Rules | [Game Rules](/misc/Game_Rules.md) |
