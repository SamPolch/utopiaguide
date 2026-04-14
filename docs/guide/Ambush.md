# Ambush

## How to Execute an Ambush

Take a SoM of the attacker, then check the intel site's Armies tab — it has an **Ambush** column that shows the required offense directly, so you don't need to run the formula manually unless you want to understand the math. If the target has multiple armies listed, work through them in reverse order (last hit first) and make sure you are only looking at attacks made against your province, not hits they made against other provinces.

In the War Room, make sure **Ambush** is selected as the attack type and use the ambush calculator option so the game calculates the minimum offense correctly. Enter the value from the intel site manually. Unlike other attack types, the ambush offense requirement does not change mid-tick due to modifiers like Minor Protection.

!!! tip "Skipping an ambush"
    If there are multiple attacks against you and you want to skip over one, send 1 soldier to intentionally fail it. Your next ambush will then target the next hit in reverse order.

## Rules and Mechanics

1. You can ambush each successful attack once. If you fail, too bad.
2. You cannot ambush if your opponent used War Spoils.
3. You cannot ambush if your opponent's hit was made with Anonymity on.
4. A successful ambush recaptures 50% of the land taken from you. Ambush ignores all gains modifiers.
5. Ambush inflicts 15% increased Military Casualties on the defender.
6. You **always** ambush from the last hit to the first.
    1. You will ambush the last successful hit. Conquests don't count. You **can** ambush an ambush.

## Why Ambush?

1. To kill Elites (especially if your target is an Orc, who have a low defensive Elite value).
    1. Ambushes are 25% faster than normal attacks.
2. To decrease incoming land (especially if your target is a chain target).
3. Because you're able to Ambush + Trad and want to rub it in his face.

## Manual Calculation

If you prefer to calculate the required offense yourself:

1. Take a SoM and record the troops out.
2. Apply the formula:

```
Raw Offense Required = [(Target's Elites sent * Racial Elite Defense Value) + (Target's Offspecs Sent * Racial Defspec Value) + (Target's Soldiers sent * Racial Soldier Offense Value)] * 0.8
```

This is the **raw** offense required — sending more than one general has no effect.

If you see a 0 in the army out column, the attacker sent none of that unit type.

### Example

- June 4th, YR5 **call (9:11)** invaded **Kzagl (3:17)** and captured 81 acres of land.
- June 4th, YR5 **I just been (9:11)** invaded **Kzagl (3:17)** and captured 139 acres of land.
- June 4th, YR5 **piercing through (9:11)** invaded **Kzagl (3:17)** and captured 131 acres of land.

**Kzagl** took a SoM of **I just been** (the largest hit) to see what troops were sent out and whether an ambush was viable.

**SOM**

*\*\* Armies #2/#3/#4 (Back in 10:46 hours) \*\**
*Ogres: 4,424 (46,308 offense / 9,485 defense)*

*Captured Land: 143 Acres*

The attacker sent 4,424 Ogres with no specialists. Orc elites have a low defensive value (2 in this example — note values change age to age), so:

```
4,424 Elites * 2 Defense Value = 8,856
```

Multiply by 0.8 (defense fights at 80% capacity on an ambush):

```
8,856 * 0.8 = 7,084.8
```

If sending 5/0 offensive specialists:

```
7,084.8 / 5 = 1,417 offspecs (send a few extra to compensate for rounding)
```

### Order of Ambushes Example

You always ambush the last hit first. If the paper looked like this:

- June 4th, YR5 I just been (9:11) invaded Kzagl Elven Grave (3:17) and captured 139 acres of land.
- June 4th, YR5 piercing through (9:11) invaded Kzagl Elven Grave (3:17) and captured 131 acres of land.
- June 4th, YR5 I just been (9:11) invaded KZAGL ELVEN GRAVE (3:17) and captured 25 acres of land.

You would have to ambush the 25-acre hit before you could ambush the 139-acre hit. You don't have to succeed — once you've attempted an ambush on a hit, the game moves on to the next one regardless.
