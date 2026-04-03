# Difference between revisions of "Dragons, Aid & Stances"

| **[Revision as of 04:01, 14 October 2014](#) ([view source](#))**[Spahrep](#) ([talk](#) | [contribs](#))([→](#Stances)‎Stances)[← Older edit](#) | | **[Revision as of 15:39, 6 November 2014](#) ([view source](#))** [Bishop](#) ([talk](#) | [contribs](#))([→](#Stances)‎Stances)[Newer edit →](#) | |
| Line 26: | | Line 26: | |
|  | \* -50% gains hitting in (slides in over a period of 24 hours) |  | \* -50% gains hitting in (slides in over a period of 24 hours) |
|  | \* -50% gains on magic and thievery ops in(slides in over a period of 24 hours) |  | \* -50% gains on magic and thievery ops in(slides in over a period of 24 hours) |
| − | \* -40% Military training time and cost | + | \* -40% Military training time and cost (not thieves) |
|  | \* +40% Draft speed |  | \* +40% Draft speed |
|  | \* -50% Construction time and cost |  | \* -50% Construction time and cost |

---

## Revision as of 15:39, 6 November 2014

# Stances

You may not change your stance if you have changed it within the last 24 hours, 24 full ticks must pass before it can be changed. If you are in Fortified the game will remove you after 4 days have passed since you entered it. If you enter Fortified on the 1st you will be removed on the 1st 4 days later.

- Stance Effects are negated in [war](#).
- Stances may not be changed during [protection](#).

| Stances | | |
| --- | --- | --- |
| Normal | Aggressive | Fortified |
| - No Effects | - +10% Combat Gains - 10% Lower Attack Time      - +30% Military Wages - +10% Military losses | - -50% gains hitting in (slides in over a period of 24 hours) - -50% gains on magic and thievery ops in(slides in over a period of 24 hours) - -40% Military training time and cost (not thieves) - +40% Draft speed - -50% Construction time and cost      - 3 days maximum duration - -50% gains hitting out - -50% gains on magic and thievery ops out - +500% Explore costs - No Paradise spell available - Science limited to "Active" |

# Dragons

At any given time, a kingdom can only be producing one dragon. In addition, a kingdom can only be the target of a single dragon.

| Dragon Type | | | |
| --- | --- | --- | --- |
| Emerald | Sapphire | Gold | Ruby |
| +20% Military losses in combat -15% Attack Gains | -25% Thievery & Magic Effectiveness | -25% from Building Efficiency | -8% from Military Efficiency |
| All dragons result in 10% lower income and the loss of 20% of new draftees. | | | |

### Dragon Cost

```
Dragon Cost = MAX ( Target Kingdom NW , Your Kingdom NW ) * 1.25
```

- Dragon Cost is determined at the time the dragon is started.

### Dragon HP

```
Dragon HP = ( Receiving Kingdom NW / ~44 ) * Relations Mod
```

- Dragon HP is determined at the time the dragon is sent.

|  |  |
| --- | --- |
| **Condition** | **Modifier** |
| **Relations: [Ceasefire](/guide/Relations.md)** | 0.25 |
| **Relations: None** | 0.5 |
| **Relations: [Unfriendly](/guide/Relations.md)** | 0.5 |
| **Relations: [Hostile](/guide/Relations.md)** | 0.75 |
| **Relations: [War](/guide/Relations.md)** | 1 |

# Aid & Tax

### Max Shipment

```
Max Aid Shipment = Province Networth * 4
```

### Tax

```
Base Tax Rate = -4 * (Trade Balance / Networth + 4)

Tax Rate = DEPEND ( Base Tax Rate ) :
                    Base Tax Rate < 0    = 0
               0 <  Base Tax Rate < 98   = Base Tax Rate
                    Base Tax Rate > 98   = 98
```

- Tax Rate is capped at 98% max.
- If receiving province has been hit significantly and is subject to [Gangbang Protection](#):
  - Tax rate will be cut in half
  - Tax will be capped at 15% rather than the 98% max.
- Taxes don't take effect until your negative trade balance reaches 400% of your networth (equivalent to one maximum aid shipment).
- If the province is below the average networth of the Kingdom, then the tax rate is calculated on the average kingdom province networth.

### Tax Rate Reduction

```
Tax Rate Reduction = Trade Balance * ((1 - 0.75) / 100)
```

It takes 11.5 real life days to halve your trade balance.
