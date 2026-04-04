# Multi-Attack Protection (MAP)

Multi-Attack Protection (**MAP**) (formerly known as Gangbang Protection **GBP**) is a game mechanism introduced which aims to increase the protection conferred to provinces which have been recently hit.

## Effects of Attacking MAP

- Tax is capped at 15% (vs a max of 99%) once above 25% MAP.
- The more MAP on your province, the less an attack will gain from you - all other variables being equal.
- Increase in Military Efficiency.
- MAP rounds off to the nearest percentage (eg. it can be 20% or 21% but not 20.5%)
- MAP is almost negligible in War.

| **MAP Status** | **MAP rating** | **Gains Out of War** | **Gains in War** | **Increase in ME** | **MAP Decay** |
| --- | --- | --- | --- | --- | --- |
| **Not Hit** | 0% | 100% | 100% | N/A | 0 |
| **Couple** | 1-20% | 80-99% | 80-99% | +0.13-2.67% | 1 |
| **Moderately Hit** | 21-40% | 60-79% | 70-79% | +2.80-5.33% | 1 |
| **Heavily Hit** | 41-60% | 40-59% | 70% | +5.47-8.00% | 2 |
| **Extremely Heavily Hit** | 61-90% | 10-39% | 70% | +8.13-12.00% | 3 or 4 if above 79% |

## Attacking MAP Change

### Land Attacks

```
 A land attack (Traditional March, Raze or Conquest) increases the MAP rating by 2.75 * Percent of Targets land taken.
```

For example if a target is attacked for 120 of its 1000 acres (12%) its GBP rating will increase by(12% \* 2.75 = 33%) 33 points, taking it from 0% to 33% if previously un hit - enough to put it into the 'moderately hit' section.

### Non-Land Attacks

```
 Non-Land Attacks (Plunder, Learn or Massacre) increase the GBP rating by 0.06 * Current Gains OOW.
```

For example if a target with a MAP rating of 20% (and thus Gains OOW of 80%) which is hit for a plunder, it will boost its GBP by (0.06 \* 80% = 4.8% rounded off) 5% to 25%.

### Thief/Mystic Operations MAP

- THIS IS RESERVED FOR FUTURE THIEF/MYSTIC OPERATIONS MAP\*

## MAP Decay

```
 MAP rating naturally decreases every hour by an amount dependent on the current MAP rating as shown in the above table.
```

For example if the MAP rating is currently 59% (heavily hit), on the next hour change it will decrease by 2% to 57%.

```
 MAP also decays whenever the province with MAP makes an attack by the same amount as if it  had made the attack on itself - except that it decreases the MAP rating rather than increasing it.
```

## Military Effectiveness

```
 MAP gives a bonus to Military Effectiveness equal to the MAP rating / 7.5
```

For example if the MAP rating of a province is 59% (heavily hit) their ME is boosted by (59 / 7.5 = 7.9%) 7.9% - ie. 1.079 times it's current rating.

## Uses of MAP

### Aid Chained Provinces

If a province gets chained in a war and it is at an obviously disparate size to the rest of the kingdom, what might happen is that the kingdom may approach a friendly kingdom and ask them to hit the chained province with a number of plunders.

This confers MAP on the chained province, which can then be aided with as many soldiers and gc in order to explore him up.

### Building a Bank

| **!** | *The information or formula below is not up to date. Please refer to the [Protection (MAP) discussions tab](#) to contribute to ongoing research or start a new topic.* |

The tax cap has been used to build up [banks](#) before - what happens is that **Kingdom A** approaches a friendly **Kingdom B** and asks them to mass plunder
