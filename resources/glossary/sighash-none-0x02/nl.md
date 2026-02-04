---
term: SIGHASH_NONE (0X02)
definition: SigHash-vlag waarbij de handtekening alle inputs dekt, maar geen outputs van de transactie.
---

Type SigHash Flag gebruikt in Bitcoin transactiehandtekeningen om aan te geven dat de handtekening geldt voor alle ingangen van de transactie, maar voor geen van de uitgangen. Het gebruik van `SIGHASH_NONE` impliceert dat de ondertekenaar alleen de invoer vastlegt, waardoor de uitvoer na ondertekening onbepaald of wijzigbaar blijft. Dit type handtekening is nuttig in gevallen waarin de ondertekenaar andere partijen wil machtigen om te beslissen hoe de bitcoins in de transactie zullen worden verdeeld.