# Relations

[Attacking](Military.md) another kingdom affects the relations between the
two kingdoms.

By continually attacking, your kingdom's conflict level against the
opposing kingdom will elevate, thereby changing the relation type; first
from **Normal** to **Unfriendly**, and then **Hostile**.

There are five main relation states, each with different restrictions,
benefits, and war implications.

For the detailed hostility-point values, decay, and exact meter movement
from attacks, spells, ops, and dragons, see
[Hostile Meter](../main/Hostile_Meter.md).

## Relation Types

Each kingdom will have differing relations with others in the world of
Utopia. How these relations evolve depends on conflict history and on
the diplomatic actions of Monarchs and Stewards. You can see your
relation with any given kingdom on its kingdom page:

```
 Their Attitude Towards Us : XX
 Our Attitude Towards Them : YY
```

## Normal

- No effects

This is the default relation between all kingdoms from the start of the age. **Normal** relations will resume after a **War** or **Ceasefire** ends.

## Ceasefire

#### Agreed Ceasefire

Also known as a **Non Aggression Pact** (as seen on the opposing kingdom page and when targeting with spells/ops).

- Prohibits any [Attacks](War_Room.md), Spells, or Ops between opposing kingdoms
- Annuls [Hostility Meter](../main/Hostile_Meter.md)
- Minimum duration of 1  [Utopian Month](../main/Utopia_Time.md)
- Can be enforced for a max of 3 [Utopian Years](../main/Utopia_Time.md)

Both Monarchs and Stewards can send, accept, and break Ceasefires. Once accepted, the Ceasefire agreement cannot be broken for the next 24 hours, though the Monarch or Steward can choose to extend this date no further than 3 weeks. While a Ceasefire is in effect, no hostile actions will be allowed between the two Kingdoms.

#### Forced Ceasefire

In the event that a Defending Kingdom is unable to withstand the might of an Aggressor Kingdom, they will be given the option to Surrender.
A Defending Kingdom can enter into a 96 Ticks unbreakable Ceasefire with an Aggressor Kingdom if:

- the Aggressor Kingdom has reached Hostile Relations with the Defending Kingdom
- the Defending Kingdom has not reached Hostile Relations with the Aggressor Kingdom
- the Defending Kingdom is out of War Range (85%-117.64%)
- the Defending Kingdom has not committed any Attacks within the past 3 hours (similar to the 2-hour restriction on [withdrawing](#withdrawal) from War); this timer does not apply if the Defending Kingdom is at War, hostile Sorcery or Thievery Ops will not reset this timer
- the Defending has not sent any Dragons for at least 3 ticks

An Aggressor Kingdom can enter into a 96 Ticks unbreakable Ceasefire with a Defending Kingdom if:

- the Aggressor has not made military Attacks against the Defending Kingdom for at least 24 Ticks
- the Aggressor has not sent any Dragons for at least 24 Ticks
- the Aggressor is not at War (including EoWCF)
- the Defender is not at War (including EoWCF; timer starts when the Defender leaves War)

(the 24 Ticks waiting period will not begin until EoWCF concludes)

[End-of-War Ceasefire](#end-of-war-ceasefire) has slightly different effects and conditions.

## Unfriendly

- A [Dragon](../main/Dragons.md) sent to an Unfriendly kingdom will only have 50% health points

When the [Hostility Meter](../main/Hostile_Meter.md) reaches **15** hostility points, the aggressor kingdom becomes **Unfriendly** towards the opposing Kingdom. If the meter decays below this limit, **Normal** relations are resumed.

From [Age 112](../history/Age_112.md), relation bonuses and access are granted only towards the Kingdom you have relations with, or which has relations towards you.

### When Your Kingdom Is Unfriendly Towards Another

- +4% Gains
- -5% Military Casualties
- +5% WPA/TPA
- -2.5% Attack Time
- +2% OME

### When Another Kingdom Is Unfriendly Towards You

- +1.5% Gains
- -2.5% Military Casualties
- +2.5% WPA/TPA
- -1% Attack Time
- +1% OME
- Access to Unfriendly T/M actions against that kingdom

For exact spell and thievery-operation requirements by relation level,
see [Hostile Meter](../main/Hostile_Meter.md#spells-and-thievery-operations).

## Hostile

- Mana & Stealth costs for offensive spells/ops reduced to 2%
- A [Dragon](../main/Dragons.md) sent to a Hostile kingdom will only have 75% health points
- Some Honor gains from Ops and Spells

When the [Hostile Meter](../main/Hostile_Meter.md) reaches **30**
hostility points, the Aggressor Kingdom becomes **Hostile** towards the
opposing Kingdom. If the Meter decays below this limit, **Unfriendly**
relations are resumed.

See [Hostile Meter](../main/Hostile_Meter.md) for the full point table,
meter decay, and spell/op hostility values.

### When Your Kingdom Is Hostile Towards Another

- +10% Gains
- -12% Military Casualties
- +15% WPA/TPA
- -6% Attack Time
- +5% OME
- Access to the target kingdom's Unfriendly T/M actions only

### When Another Kingdom Is Hostile Towards You

- +3% Gains
- -4% Military Casualties
- +5% WPA/TPA
- -2% Attack Time
- +2% OME
- Access to Hostile T/M actions against that kingdom

Notable Hostile access includes [Meteor Showers](Mystics.md#meteor-showers).

## War

War begins when a kingdom *declares War* on a Hostile kingdom **OR** if the maximum hostility level is reached by both Kingdoms.

In order to declare War, a Kingdom must:

- have received Attacks from at least three unique provinces on either side (except if Monarch/Stewards grant Hostile Operations)
- be in Range (more than 85% and less than 117.64% of its Net Worth or Land)
- be *at least* **Unfriendly** with the opposing Kingdom, **AND** that Kingdom must be **Hostile** with your Kingdom

*If both kingdoms are **Hostile**, the kingdom with fewer meter points
will receive the war button and be able to declare war. When both
kingdoms reach 90 points, either one can declare.*

*If 180 points are reached by both Kingdoms, War automatically starts.*

Wars last a minimum of 2 [Utopian Months](../main/Utopia_Time.md) (48 hours) after declaration.

A Kingdom can only War one other Kingdom at a time.

Honor and Land gains are higher in War than out of War.

War also has a minimum-gains floor on attacks; by [Age 100](../history/Age_100.md) this was documented as roughly 4%. See [Attacking & Defending](Attacking_&_Defending.md#attack-gains) for the fuller historical note.

### Immediate Effects

- War overrides relations with all other kingdoms. Upon leaving War, **Normal** relations will resume. While in War, there is a decay of two hostility points per [Utopian Month](../main/Utopia_Time.md) or 1/5th of the Meter, whichever is greater.

#### Benefits

- Mana & Stealth costs for offensive spells/ops reduced to 2%
- A [Dragon](../main/Dragons.md) sent in War has full health
- Greatly increased Honor gains from Ops and Spells
- Greatly reduced [Multi-Attack Protection](../misc/Multi-Attack_Protection_(MAP).md)

#### War-only Spells

- [Amnesia](Mystics.md#amnesia)
- [War Spoils](Mystics.md#war-spoils)

#### War-only Thievery Operations

- [Propaganda](../misc/Thievery.md#propaganda)

#### Penalties

- [Paradise](Mystics.md#paradise) cannot be cast (except during EoWCF)
- 600% Exploration Costs

### After 12 Hours

#### Benefits

- -15% Attack Time

### After 24 Hours

#### Benefits

- -80% Gains, Military Casualties and Effectiveness for Spells and Operations to and from other Kingdoms (this fades in from War start)

### Fake War

Any informal or formal agreements made between kingdoms in regards to warring must abide by the Code of Conduct. Violations may cause the war to be deemed a Fake War. Fake Wars are subject to actions by the game operators. As the determination for a Fake War is made on a case-by-case basis by the game operators, the exact punishment may vary.

Ways a War can be faked (Please note, this is just an idea and not a comprehensive list):

- Requesting specific people be targeted by opposing Kingdom or accepting to action a request from the opposing Monarch
- Non-aggression pact during War of any duration and at any time
- Attempts to manipulate War-Win rankings using friends to initiate multiple Wars
- Agreement to trading Acres for a War Win
- "Ending" a war before minimum war duration

Punishments may include (Again, not a comprehensive list):

- Removal from the End of Age rankings for both kingdoms
- Deletion and temporary ban of players making the agreement
- Removal of war wins
- Monarchs of both Kingdoms deleted
- Removal of any gains of the Fake War from all Kingdom members (even if they were unaware of the Fake War)

### Province Creation

Provinces created/reset during War will start without Soldiers, Military & Building Credits.

## Starting a War

Once the **Hostile** relation status has been reached by one kingdom, the
Monarch of the least hostile Kingdom will receive the option to Declare
War as long as their own relations with that Kingdom are at a minimum of
**Unfriendly**. This "War Button" appears on the Relations Page under
the War tab.

If both kingdoms have reached **Hostile** relations status, the kingdom
with fewer points will have the button until both kingdoms reach
**90 points**, at which point either one can declare.

Once the button is pressed, certain effects are applied immediately;
others phase in over the next 24 hours.

## Ending a War

Only the Kingdom's Monarch (or Steward) is able to end a war. This is
accomplished in one of two ways: Mutual Peace or Withdrawal. Either
choice results in an end-of-war ceasefire.

### Mutual Peace

This option requires consent by both parties and simply settles the war with no winner. This is an excellent option when both kingdoms simply lose interest in the war or find it more beneficial to simply move on.

Both kingdoms receive:

- 3 times your median Provinces Acres in Specialist Credits
- Free Building Credits to the total of 200% of median province total Land at the end of the War
- A provision of additional land to each province's individual Explore Pool
- Science Books bonus equal to 24 Ticks of production
- 1 additional War Score point

### Withdrawal

Once the Minimum Time limit is reached (48 Ticks), either Kingdom can Withdraw from War. Withdrawals can occur if the Withdrawing Kingdom has not committed any Attacks within the past 2 Ticks.

War will also automatically end (a Kingdom will automatically Withdraw) if their Net Worth drops below 66% of the opponent's Net Worth on the first Tick this condition is satisfied. This will only occur after a minimum of 48 Ticks.

The Withdrawing Kingdom receives the following benefits:

- 3 times your median Provinces Acres in Specialist Credits
- Free Building Credits to the total of 200% of median Province total Land at the end of the War
- A provision of additional Land to each Province's individual Explore Pool
- Science Books bonus equal to 24 Ticks of production

The Withdrawing Kingdom incurs the following penalties:

- 5% of the Kingdom's Land will be lost and transferred to the Winning Kingdom
- 5% of the Kingdom's Honor will be lost and transferred to the Winning Kingdom

### Victory

A Kingdom is victorious when its opponent withdraws from War. This is also called Surrendering. A Kingdom can only Withdraw if it makes no Attacks for 2 consecutive Ticks. It can then Withdraw on the 3rd Tick. Dragons, Aid, Thievery Operations and Magic Spells do not affect a Kingdom's ability to Withdraw.

After War, the winning kingdom receives the following benefits:

- 3 times your median Provinces Acres in Specialist Credits
- Free Building Credits to the total of 200% of Median Province total Land at the end of the War
- A provision of additional Land to each Province's individual Explore Pool
- Science Books bonus equal to 36 ticks of Production
- +50% advancement towards the next Scientist
- Land bonus equal to 5% of the losing Kingdom's total Land at the end of the War, subtracted from each Province then transferred and distributed evenly
- Land bonus equal to 10% of the losing Kingdom's total Land at the end of the War, distributed prioritizing smallest Provinces in the Winning Kingdom
- Honor bonus equal to 5% of the losing Kingdom's total Honor at the end of the War (subtracted from each province then transferred and distributed evenly), plus 200 Honor per Province
- Recognition on Kingdom Page based on the number of Wars achieved
- 2 additional War Score points

!!! note
    - Each additional War Win achieved will increase War Win bonuses (that are not transferred) by 5%, capped at 50% larger than baseline bonus.
    - War Win bonus will incur a 5% stacking penalty for each Province below 25, calculated at War start - max 25% reduction.
    - At the conclusion of the age, Kingdoms will be awarded bonus War Score points for every Kingdom that they defeated in War, based on the defeated Kingdoms' total War Wins (if any). An additional provision of points will be granted for every Kingdom warred but not defeated, based on the total War Wins of those Kingdoms (if any), a Mutual peace counts as a loss in this instance.
    - War Score will incur a 4% stacking penalty for each missing Province below maximum, calculated for each individual War, this penalty carries over to EoA adjustment, full points only awarded full Kingdoms.

### End-of-War Ceasefire

After a War ends, neither Kingdom may have any Relations for an [Utopian Month](../main/Utopia_Time.md) and are automatically placed in a 24 hour End-of-War Ceasefire. During the ceasefire both Kingdoms remain in War relations, thus retaining the protection benefits while rebuilding. After 24 hours, the Kingdoms have the choice either to end the Ceasefire or to wait up to an additional 72 hours (96 hours total). This choice is independent of the other Kingdom.

During this ceasefire, both sides benefit from:

- Building Efficiency automatically restored to 100% if below 100%
- All Land currently out with armies at War end returns home immediately
- All Military Units currently out on Attacks against the War opponent return home immediately
- Negative Spell effects and Riots are removed
- Any Provinces affected by Plague it removed instantly
- Instant Population growth of 20% of maximum if you are under 50% of your maximum Population
- +1000% Birth Rate (minimum 500) for the first 24 Ticks
- Explore penalty reduced to 300% and explore time reduced by 50% for Provinces below Kingdom Median (including incoming explored Acres)
- Access to Paradise spell
- Dragons that have already begun will be automatically canceled upon entering EoWCF

!!! note
    - All Credits (Specialist or Building) will be lost upon exit of End of War Ceasefire
    - Learn and Amnesia will return books over 48hrs, even if war ends.

# Out-Of-Range War Benefits

There are no benefits for a War that was conducted outside of War Range (85%-117.64%). Neither winner or loser will gain Training or Building Credits and their Land and Troops will not instantly return (they will return at normal time).

# War Forum

Shortly after declaring War, a temporary Forum is created. This is known as the War Forum.

In the War Forum Provinces from either Kingdom can interact by starting new threads or posting in existing ones.

Provinces are expected to interact respectfully and obey the Code of Conduct. Any offending material can be removed by either Kingdom's Monarch or Steward.
