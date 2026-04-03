# View source for Food

You do not have permission to edit this page, for the following reason:

The action you have requested is limited to users in the group: Trusted.

---

You can view and copy the source of this page.

'''Food''' is a resource, and it is needed to keep population of a [[Province|Province]] alive. It's measured in '''bushels'''.
== Food Consumed ==
<b>Bushels Eaten</b> = Total Population \* 0.25 \* [[Race|Race Mod]] \* [[Mystics#Gluttony|Gluttony Mod]]
{{Mods}}
|-
| Race: [[Race#Undead|Undead]] || 0 || 1
|-
| Race: [[Race#Dwarves|Dwarf]] || 1.5 || 1
|-
| Spell: [[Mystics#Gluttony|Gluttony]] || 1.25 || 1
|}
<!--\* Undead population isn't alive, so no food required to make it not dead.-->
\* If a province has zero food, it will enter into a state of starvation. While a province is starving, its population (peasants, military units and thieves) will die off at a rate proportional to the food deficit (this also includes armies away from home). Wizards are not affected. This rate is capped at 5% and will continue until the province has a value for food greater than 0.
== Food Produced ==
<b>Base Food Production =</b> (([[Buildings|Farms]] \* 60) \* Building Efficiency) + (Barren Land \* 2) + (Race Mod \* Acres) + (Personality Mod \* Acres)
<b>Modified Food Production =</b> Base Food Production \* [[Science|Production Science Mod]] \* [[Mystics#Fertile\_Lands|Fertile Lands Mod]] \* [[Mystics#Droughts|Drought Mod]] \* [[Honor|Honor Mod]]
{{Modifier}}
|-
| [[Mystics#Fertile\_Lands|Fertile Lands]] || 1.25
|-
| [[Mystics#Droughts|Drought]] || 0.75
|}
== Food Decayed ==
<b>Food Remaining</b> = Food Stock \* 0.99<!--(1 - (0.01 \* [[Mystics#Vermin|Vermin Mod]]))--> + Modified Food Production - Bushels Eaten
0.99 or about 1% of the total food stock decays in normal conditions. The exact amount depends on the modifiers in the formula as provided above and it is calculated on the total food stored in the province. So if a province has 300,000 bushels of food in stock under normal conditions, then the expected decay is slightly less or more than 3000 bushels per tick / Utopia day. There may be scenarios where the total food decayed, is higher than what remains after food needed by the population is consumed from the food grown. This may lead to depletion of the stock in the province especially after a war when the people are much lesser compared to the maximum population limit and the stored food may be much higher or when a new player has built a lot of farms / received aid as food. This will normalize once the population reaches back to expected levels and the province only needs to ensure that the food grown is more than the food needed by the population at all times so as to avoid starvation.
<!-- The section of the formula (1 - (0.01 \* [[Mystics#Vermin|Vermin Mod]])) represents food decay. Without the vermin modifier, the 1 - 0.01 = -->
<!--
{{Mods}}
|-
| '''[[Mystics#Vermin|Vermin]]''' || 4.5 || 1
|}
-->
{{Guide navigation}}
[[Category:Formulas|Food]]
[[Category:Resources]]

Templates used on this page:

- [Template:Guide navigation](/web/20250315082338//index.php?title=Template:Guide_navigation "Template:Guide navigation") ([view source](/web/20250315082338//index.php?title=Template:Guide_navigation&action=edit "Template:Guide navigation"))
- [Template:Modifier](/web/20250315082338//index.php?title=Template:Modifier "Template:Modifier") ([view source](/web/20250315082338//index.php?title=Template:Modifier&action=edit "Template:Modifier"))
- [Template:Mods](/web/20250315082338//index.php?title=Template:Mods "Template:Mods") ([view source](/web/20250315082338//index.php?title=Template:Mods&action=edit "Template:Mods"))
- [Template:•](/web/20250315082338//index.php?title=Template:%E2%80%A2 "Template:•") ([view source](/web/20250315082338//index.php?title=Template:%E2%80%A2&action=edit "Template:•"))

Return to [Food](/web/20250315082338//index.php?title=Food "Food").
