---
term: OP_TOALTSTACK (0X6B)
definition: Opcode die de bovenkant van de hoofdstack naar de alternatieve stack verplaatst.
---

Neemt de bovenkant van de hoofdstack (*main stack*) en verplaatst deze naar de alternatieve stack (*alt stack*). Deze opcode wordt gebruikt om gegevens tijdelijk opzij te zetten voor later gebruik in het script. Het verplaatste item wordt dus verwijderd uit de hoofdstapel. `OP_FROMALTSTACK` wordt dan gebruikt om het terug te plaatsen bovenop de hoofdstapel.