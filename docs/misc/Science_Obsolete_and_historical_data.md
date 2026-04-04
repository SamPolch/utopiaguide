# Science: Obsolete and historical data

### Age 77

```
Science Bonus = [ MIN( Science Multiplier * Skill points , Cap ) + MAX( 0, Science Multiplier * Skill points - Cap ) * Diminishing Return Factor ] * Race Mod * Personality Mod * Scientific Insights Mod
```

```
Skill points = Number of Novices + 1.5 * Number of Graduates + 2 * Number of Professors
```

| **Modifier Type** | **Multiplier** | **Science Category** |
| --- | --- | --- |
| Personality: [Heretic](../ages/Personality.md) | 1.3 | Crime |
| Personality: [Heretic](../ages/Personality.md) | 1.3 | Channeling |
| Personality: [Rogue](../ages/Personality.md) | 1.5 | Crime |
| Personality: [Mystic](../ages/Personality.md) | 1.75 | Channeling |
| Personality: [Sage](../ages/Personality.md) | 1.3 | All |
| Spell: [Scientific Insights](../guide/Mystics.md) | 1.1 | All |

**\*NOTE\* Starting Age 73: Science no longer has a hard maximum for all categories. Science will scale in a linear fashion up to stated maximums (Cap) as normal. Once this point is reached, additional scientists will yield diminishing returns.**

| **Science Category** | **Effect** | **Multiplier** | **Cap** | **Scientist Cap** |
| --- | --- | --- | --- | --- |
| **Alchemy** | Income | 0.500% | 30% | 30 |
| **Tools** | Building Effectiveness | 0.333% | 20% | 30 |
| **Housing** | Population Limits | 0.250% | 15% | 30 |
| **Production** | Food & Rune Production | 2.000% | 120% | 30 |
| **Military** | Military Efficiency | 0.250% | 15% | 30 |
| **Crime** | Thievery Effectiveness | 1.667% | 100% | 30 |
| **Channeling** | Magic Effectiveness | 2.084% | 125% | 30 |

- As of Age 77, Universities protect a province from [Amnesia](../guide/Mystics.md).
- Starting Age 77, the number of scientists required for (soft) cap will be the same number for all categories: 30.
- Abduct attack has been removed in Age 77.

**Scientist Spawn Rate**

Each province starts with a set number of scientists assigned to the various science categories. Scientists start out as Recruits that provide no bonus, then as they progress ther provide incrementally greater benefits with each progression.

- Recruit -> Novice = 3 Utopian days (3 hours)
- Novice -> Graduate = 72 Utopian days (3 days)
- Graduate -> Professor = 96 Utopian days (4 days)

Scientists can be re-assigned at any time, but revert to Recruit level when doing so. 
Every tick each province builds progress towards a new random scientist. Laboratories increase the rate of this progress.

```
Scientists Spawn Rate = 9.5 * Race Mod * Laboratories Effect * Revelation Mod
```

| **Modifier Type** | **Multiplier** |
| --- | --- |
| Race: [Human](../main/Race.md) | 1.25 |
| Spell: [Revelation](../guide/Mystics.md) | 1.3 |

**Scientist Networth**

```
Networth Per Scientist = ~1.7gc * tick of experience
```

- Professors experience caps at 72 hours
- A maxed-out professor will provide ~413gc Networth

### Age 69 - Age 76

**Abduct Attacks**

- Through combat, you can abduct scientists from another province. Universities protect a province from abduction. **Note: Abduct attack has been removed in Age 77.**

**Changelog**

- Age 69: The new science system is introduced.
- Age 70: Professors experience capped at 72 hours (a maxed-out professor will provide ~624gc Networth). Tools cap increased from 15% to 20%, housing and military cap from 10% to 15%, food from 100% to 200%, channeling from 100% to 125%. Additional scientist rank added: Recruit.
- Age 71: Approximately +50% scientists will be required to reach maximum effects (see table below). Production Science maximum will be 120% (down from 200%) and it will increase both Food and Rune production.
- Age 72: Scientists are generated on a flat ratio (7.5) similar to wizards instead of via RNG.
- Age 73: Science will no longer have a hard maximum for all categories. Science will scale in a linear fashion up to the previously stated maximums as normal. Once this point is reached additional scientists will yield diminishing returns.
- Age 74: Scientist experience will now show on the Science page and in the Spy on Sciences.
- Age 76: The number of scientists required for soft cap will be the same number for all categories: 35.

**Old scientist multipliers and caps, during Age 76:**

| **Science Category** | **Effect** | **Multiplier** | **Soft Cap** |
| --- | --- | --- | --- |
| **Alchemy** | Income | 0.428 | 30% |
| **Tools** | Building Effectiveness | 0.287 | 20% |
| **Housing** | Population Limits | 0.215 | 15% |
| **Production** | Food & Rune Production | 1.714 | 120% |
| **Military** | Military Efficiency | 0.215 | 15% |
| **Crime** | Thievery Effectiveness | 1.428 | 100% |
| **Channeling** | Magic Effectiveness | 1.785 | 125% |

**Old scientist multipliers and caps, Age 71 - Age 75:**

| **Science Category** | **Effect** | **Multiplier** | **Cap** | **Scientist Cap** |
| --- | --- | --- | --- | --- |
| **Alchemy** | Income | 0.5 | 30% | 30 |
| **Tools** | Building Effectiveness | 0.33 | 20% | 31 |
| **Housing** | Population Limits | 0.2 | 15% | 38 |
| **Production** | Food & Rune Production | 2 | 120% | 30 |
| **Military** | Military Efficiency | 0.2 | 15% | 38 |
| **Crime** | Thievery Effectiveness | 1.65 | 100% | 31 |
| **Channeling** | Magic Effectiveness | 2 | 125% | 32 |

### Age ?? to Age 68

**NOTE: These formulas apply to the old books system of science. In Age 69, books were replaced by scientists.**
**From Ages ?? to 68 Science formulas worked as follows:**

**Science Effects**

```
Books per Acre = Books / MAX(Acres,300)
```

```
Science Bonus = Race Mod * Personality Mod * Science Multiplier * SQRT( Books per Acre ) * Library Effect
```

| **Science Category** | **Multiplier** |
| --- | --- |
| **Alchemy** | 1.4 |
| **Tools** | 1 |
| **Housing** | 0.65 |
| **Food** | 8 |
| **Military** | 0.52 |
| **Thievery** | 6 |
| **Channeling** | 6 |

**Science Costs**

```
Science Cost = Raw Cost (Table Below) * Race Mod * Schools Effect
```

| **Science Rate** | **BPA** | **GC / Book** | **GC / Acre** |
| --- | --- | --- | --- |
| **No Research** | 0 | 0 | 0 |  |
| **Minimal** | 0.3 | 6 | 1.8 |
| **Limited** | 0.4 | 7 | 2.8 |
| **Sustained** | 0.5 | 9 | 4.5 |
| **Active** | 0.7 | 13 | 9.1 |
| **Focused** | 0.9 | 17 | 15.3 |
| **Accelerated** | 1.2 | 22 | 26.4 |
| **Intensive** | 1.5 | 27 | 40.5 |
| **Rushed** | 2.0 | 36 | 72.0 |
| **Extreme** | 3.0 | 50 | 150.0 |

| **Obsolete and historical data** | |
| --- | --- |
|  | **Science**  • [Stances](#) |
