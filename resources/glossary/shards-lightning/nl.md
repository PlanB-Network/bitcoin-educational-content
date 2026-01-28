---
term: Shards (lightning)
definition: Deel van een betaling die afzonderlijk via verschillende Lightning-routes (MPP/AMP) wordt verzonden.
---

In de context van *Multi-Path Payments (MPP)* of *Atomic Multi-Path Payments (AMP)*, is een Shard een fractie van een globale betaling. Elke Shard vertegenwoordigt een deel van de totale betaling, die apart wordt gerouteerd via een andere route op Lightning.


In MPP delen alle scherven hetzelfde geheim, terwijl in AMP elke Shard een uniek deelgeheim heeft. De ontvanger groepeert de scherven om de volledige betaling opnieuw samen te stellen en af te ronden. Dit mechanisme omzeilt liquiditeitsbeperkingen op een enkel kanaal.