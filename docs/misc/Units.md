# Units

Unit types available in Utopia. Racial and personality bonuses are not included unless noted.

| Unit | Offense | Defense | Cost | Networth |
| --- | --- | --- | --- | --- |
| **Peasants** | — | — | — | 0.25 |
| **Soldiers** | 3† | 0† | Varies | 0.25 per point of power |
| **Offensive Specialists** | 10† | 0 | 350gc | 0.4 per point of power |
| **Defensive Specialists** | 0 | 10† | 350gc | 0.5 per point of power |
| **Elites** | Varies | Varies | Varies | Varies |
| **Wizards** | — | — | — | 7 |
| **Thieves** | — | — | 500gc | 5 |
| **Horses** | 2† | — | — | 0.3 per point of power |
| **Prisoners** | 8† | — | — | 0.2 per point of power |
| **Mercenaries** | 8† | — | 300gc | — |

† [Racial](../main/Race.md) and [Personality](../ages/Personality.md) modifiers can increase or decrease this value.

---

## Peasants

Peasants work the land and [generate income](../main/Economy.md) for your province. They are the source of all drafted soldiers, thieves, and wizards.

## Soldiers

The basic unit for every province. Drafted from peasants and can be trained into Specialists, Elites or Thieves. No wages required for soldiers.

## Offensive Specialists

Used to attack only — cannot defend.

## Defensive Specialists

Defend your land only — cannot attack.

## Elites

Have both offensive and defensive strength. Values vary by race — see the [Race](../main/Race.md) page.

## Generals

Provinces have 5 generals. One must always stay home to lead the defense; the others may be sent to combat.

- Each additional general sent adds **+3% Offensive Military Efficiency**
- At least 1 general must be sent on any attack
- Sending more than 1 general has no effect on an Ambush

## Wizards

Required to cast spells. Do not count toward military size. See the [Mystics Guide](../guide/Mystics.md) and [Magic Formulas](../guide/Magic_Formulas.md).

## Thieves

Conduct [thievery operations](Thievery.md). See also [Thievery](Thievery.md) for formulas.

## Horses

Sending horses adds raw offensive power. You may include up to **one horse per military unit** sent in combat.

## Prisoners

Taken from enemies that would have been killed after an attack (roughly 2/3 of kills), provided there is room in your dungeons. 

- No upkeep; every 2 prisoners fills 1 job and produces 0.75gc/hour
- About one third of prisoners sent in combat are lost in the fight
- You can send at most **1 prisoner per 5† normal troops**

## Mercenaries

Hired fighters available for combat.

- You can send at most **1 mercenary per 5† normal troops**

---

## Formulas

### Soldiers Drafted Per Tick

```
Soldiers Drafted per Tick = Peasants * Draft Speed * Race Bonus * Personality Bonus * Patriotism * Affluent Ritual * Sloth * Dragon * Heroism Science Effect
```

| Modifier | Active | Otherwise |
| --- | --- | --- |
| [Patriotism](../guide/Mystics.md) | 1.3× | 1× |
| [Sloth](../guide/Mystics.md) | 0.5× | 1× |
| Ruby [Dragon](../main/Dragons.md) | 0.75× | 1× |
| Expedient Ritual | 1.2× | 1× |

### Draft Cost

```
Cost of Soldier Drafting = Current Draft Level Factor * Draft Rate * Race Bonus * Personality Bonus * Armouries Mod * Heroism Science Effect * Sloth Effect
```

- Draft Level Factor scales base cost upward once 50% of max population is drafted
- [Drought](../guide/Mystics.md) reduces draft rate by 15%

| Draft Rate | Speed | Cost per Soldier |
| --- | --- | --- |
| Reservist | 0.5% / tick | 30gc |
| Normal | 1.0% / tick | 50gc |
| Aggressive | 1.5% / tick | 75gc |
| Emergency | 2.0% / tick | 110gc |

### Training

```
Training Cost = Unit Cost * Race Bonus * Armouries Bonus
```

```
Full Training Time = 24 ticks * Race Bonus * Personality Bonus * MAX(Inspire Army, Hero's Inspiration) * Valor Science * Haste Ritual * Training Grounds Bonus
```

### Maintenance

See [Economy](../main/Economy.md) for the wage formula.
