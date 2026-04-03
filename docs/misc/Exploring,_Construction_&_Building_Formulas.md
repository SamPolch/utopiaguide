# View source for Exploring, Construction & Building Formulas

You do not have permission to edit this page, for the following reason:

The action you have requested is limited to users in the group: Trusted.

---

You can view and copy the source of this page.

flag:delete
Deprecated. Already added content to the [[Explore]] and [[Growth]] pages.
<!---
===Soldier Cost===
<b>Exploration Soldier Cost =</b> ''ROUND'' (3 + Metric/210 \* War Status \* Mills)
===GC Costs===
<b>Exploration Gold Cost =</b> ''Floor'' ((600 + 2.3 \* Metric) \* War Status \* Mills)
where
<b>Metric =</b> ( Full Metric + Half Metric )<sup>1.12</sup>
<b>Full Metric =</b> Total Land - 300
<b>Half Metric =</b> ''MIN'' (Full Metric / 2 , [Land Explored - Land Lost] / 2)
--->
==Construction==
===Construction Time===
<b>Construction Time =</b> 16 \* Racial Mod \* Personality Mod \* Builders Boon \* Double Speed \* Expedient Ritual Mod \* Artisan Science Mod
{{Mods}}
| '''[[Mystics#Builders\_Boon|Builders Boon]]''' || 0.75 || 1
|-
| '''Double Speed''' || 0.5 || 1
|-
| '''Double Speed in Protection''' || 0.75 || 1
|-
| '''War''' || 0.75 || 1
|-
| '''[[Ritual|Expedient Ritual]]''' || 0.8 (if at 100% efficiency) || 1
|}
===Construction Costs===
<b>Construction Costs =</b> 0.05\*(land+10000) \* Race Mod \* Mills Mod \* Double Speed \* Expedient Ritual Mod \* Artisan Science Mod
{{Mods}}
| '''Double Speed''' || 2 || 1
|-
| '''Race: Dwarf''' || 0.5 || 1
|-
| '''[[Ritual|Expedient Ritual]]''' || 0.75 (if at 100% efficiency) || 1
|}
===Raze Costs===
<b>Raze Costs =</b> (300+(0.05\*land) \* Artisan Science Mod
<!--
{{Mods}}
| '''Race: [[Race#Dwarves|Dwarf]]''' || 0.5 || 1
|}
-->
==Buildings==
===Building Efficiency===
<b>Available Workers = </b> Peasants + ''ROUNDDOWN'' ( Prisoners / 2 )
<b>Optimal Workers = </b> ''ROUNDDOWN'' ( Total Jobs \* 0.67 )
<b>% Jobs Performed = </b> ''MIN'' ( Available Workers / Optimal Workers '','' 1 )
<b>Building Efficiency = </b> (0.5 \* (1 + % Jobs Performed)) \* Race \* Personality \* Tools Science \* Dragon \* Blizzard
\* The "Current Available Workers" value, provided by the Internal Affairs Adviser page, already takes prisoners into account.
\* Building Efficiency affects all [[Buildings#Classes\_of\_Buildings|Flat Rate]] and [[Buildings#Classes\_of\_Buildings|Percentage-Based]] buildings.
\* Building Efficiency has '''NO''' effect on Capacity component of Capacity Buildings as well as [[Buildings#Universities|Universities]].
<!---<b>Building Efficiency Change Rate = </b> Formula--->
\* Changes in Building Efficiency take effect gradually.
{{Mods}}
|-
| '''Race: Dwarf''' || 1.25 || 1
|-
| '''Dragon: [[Dragons#Topaz|Topaz]]''' || 0.75 || 1
|-
| '''Spell: [[Mystics#Blizzard|Blizzard]]''' || 0.9 || 1
|}
=== Building Effects ===
<b>[[Buildings#Classes\_of\_Buildings|Percentage Based Buildings]] =</b> Base Effect \* BE \* MIN(50%, % of building \* (1 + Race)) \* (100% - MIN(50%, % of building \* (1 + Race)))
<b>[[Buildings#Classes\_of\_Buildings|Flat Rate Buildings]] =</b> Base Effect \* (Number of Buildings \* (1 + Race)) \* BE
\* In general, the Max Effect of a %-Based Building is 25 x Base Effect (exceptions apply, refer to table)
\* If your BE is less than 100%, the effect you would have with 50% of that building is the maximum.
\* If you have less than 100% BE, additional buildings past 50% will have no effect.
==Related Links:==
{{Guide navigation}}
{{Buildings}}
[[Category:Formulas]]

Templates used on this page:

- [Template:Buildings](#) ([view source](#))
- [Template:Guide navigation](#) ([view source](#))
- [Template:Mods](#) ([view source](#))
- [Template:•](#) ([view source](#))

Return to [Exploring, Construction & Building Formulas](Exploring,_Construction_&_Building_Formulas.md).
