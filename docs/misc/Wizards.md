# Units

## Units

| Here are the unit types that are available in [Utopia](Utopia.md) (racial/personality bonuses are not included) | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Units | Description | Offense | Defense | Cost | Networth |
| **Peasants** | Peasants are responsible for working and [generating income](../category/Economy.md) for your province. |  |  |  | 0.25 |
| **Soldiers** | The basic unit for every province. They are drafted from Peasants and can be trained into Specialists, Elites or Thieves. You are not required to pay [Wages](../category/Economy.md) for Soldiers. | 3† | 0† | Varies | 0.25 networth per point of power |
| **Wizards** | Wizards are required to cast spells. They do not count towards your military size. Check out the [Mystics Guide](../guide/Mystics.md) as well as the [Mystic Formulas](../guide/Magic_Formulas.md). |  |  |  | 7 |
| **Thieves** | The part of your military which will conduct [Thievery ops](Thievery.md). Be sure to check out Thievery Formulas as well |  |  | 500gc | 5 |
| **Horses** | Sending horses with your attacks adds raw offensive point per horse. You may include up to one horse per military unit sent in combat. | 2† |  |  | 0.3 per point of power |
| **Prisoners** | Prisoners are taken from the total number of enemies that would've been killed after an attack, usually at a 2/3 prisoner to total kills ratio - IF there is room in your dungeons for them. Prisoners have no upkeep, every 2 prisoners fills 1 job, and every prisoner produces 0.75gc per hour. About one third of the prisoners sent are lost in the fight. They are then again immediately available to your general. You can use at most 1 Prisoner for every 5† normal troops you send. | 8† |  |  | 0.2 per point of power |
| **Mercenaries** | You can use at most 1 Mercenary for every 5† normal troops you send. | 8† |  | 300gc |  |
| **[Defensive Specialist](../guide/Military.md)** | These troops defend your land only, and are unable to attack. |  | 10† | 350gc | 0.5 networth per point of power |
| **[Offensive Specialist](../guide/Military.md)** | These troops are used to attack, and are unable to defend. | 10† |  | 350gc | 0.4 networth per point of power |
| **[Elites](../guide/Military.md)** | Elites have offensive as well as defensive strength. Their offensive and defensive values vary from race to race. For Elite values please see the respective [Race](../main/Race.md) page. | Varies | Varies | Varies | Varies |

† [Racial](../main/Race.md) and [Personality](../ages/Personality.md) modifiers can increase or decrease this number.

## Formulas

### Soldiers Drafted Per Tick

```
Soldiers Drafted per Tick = Peasants * Draft Speed * Race Bonus * Personality Bonus * Patriotism * Affluent Ritual * Sloth * Dragon * Heroism Science Effect
```

| **Modifier Type** | **Active** | **Otherwise** |
| --- | --- | --- |
| **[Patriotism](../guide/Mystics.md)** | 1.3 | 1 |
| **[Sloth](../guide/Mystics.md)** | 0.5 | 1 |
| **Ruby [Dragon](../category/Dragons.md)** | 0.75 | 1 |
| **Expedient Ritual** | 1.2 | 1 |

### Draft Cost Formula

```
Cost of Soldier Drafting = Current Draft Level Factor * Draft Rate * Race Bonus * Personality Bonus * Armouries Mod * Heroism Science Effect * Sloth Effect
```

**Note**

- Current Draft Level Factor scales base soldier draft cost upwards once 50% of max population is reached
- Draft Level Factor is MAX(1.0154\*((Solds+Ospecs+Dspecs+Elites)/maxpop)^2+1.1759\*((Solds+Ospecs+Dspecs+Elites)/maxpop)+0.3633,1)\* base rate for level

### Draft Rate Formula

```
Draft Rate = Base Draft Rate * Patriotism Bonus * Heroism Science Effect * Sloth * Ritual
```

- [Drought](../guide/Mystics.md) reduces draft rate by 15%

| **Base Draft Rate** | **Draft Speed** | **Cost per soldier** |
| --- | --- | --- |
| **Reservist** | 0.5% | 30gc |
| **Normal** | 1.0% | 50gc |
| **Aggressive** | 1.5% | 75gc |
| **Emergency** | 2.0% | 110gc |

### Training Formulas

```
Training Cost = Unit Cost * Race Bonus * Armouries Bonus
```

```
Full training time = 24 * Race Bonus * Personality Bonus * MAX (Inspire Army,Hero's Inspiration) * Valor Science Effect * Haste Ritual * Training Grounds Bonus
```

### Maintenance cost

[**Click here for the Formula**](../category/Economy.md)

| **The Utopia Guide** | |
| --- | --- |
| Introduction | [Getting Started with Utopia](Getting_Started_with_Utopia.md)  • Creating a province  • [Race](../main/Race.md) & [Personality](../ages/Personality.md) |
| The Menus | Throne  • Kingdom  • News [Explore](Explore.md)  • [Growth](../guide/Growth.md)  • [Science](../main/Science_Formulas.md)  • [Military](../guide/Military.md)  [Mystics](../guide/Mystics.md)  • [Thievery](Thievery.md)  • [War Room](../guide/War_Room.md) • Aid  • [Dragon](../category/Dragons.md)  • [Ritual](Ritual.md)  • Stances  Mail & Forums  Politics  • [Relations](../guide/Relations.md)  • Rankings  • Preferences |
| Advanced | [MunkBot](MunkBot.md)  • Invitations  • [Reservations](Reservations.md)  • [Utopia](Utopia.md)  • [Province](../category/Province.md)  • [World of Legends](../category/World_of_Legends.md)  • Formulas |
| Rules | [Game Rules](Game_Rules.md) |

| **Races & Personalities** | |
| --- | --- |
| Races | [Avians](../main/Race.md)  • [Dark Elves](../main/Race.md)  • [Dwarves](../main/Race.md)  • [Elves](../main/Race.md)  • [Faeries](../main/Race.md)  • [Halflings](../main/Race.md)  • [Humans](../main/Race.md)  • [Orcs](../main/Race.md)  • [Undead](../main/Race.md) |
| Extinct Races | [Bocans](../main/Race.md)  • [Dryads](../main/Race.md)  • [Gnomes](../main/Race.md) |
| Personalities | [The Artisan](../ages/Personality.md)  • [The Cleric](../ages/Personality.md)  • [The Heretic](../ages/Personality.md)  • [The Merchant](../ages/Personality.md)  • [The Mystic](../ages/Personality.md)  • [The Rogue](../ages/Personality.md)  • [The Shepherd](../ages/Personality.md)  • [The Tactician](../ages/Personality.md)  • [The War Hero](../ages/Personality.md)  • [The Warrior](../ages/Personality.md) |
| Extinct Personalities | [The Freak](../ages/Personality.md)  • [The General](../ages/Personality.md)  • [The Paladin](../ages/Personality.md)  • [The Raider](../ages/Personality.md)  • [The Undead](../ages/Personality.md)  • [The Necromancer](../ages/Personality.md)  • [The Sage](../ages/Personality.md) |
