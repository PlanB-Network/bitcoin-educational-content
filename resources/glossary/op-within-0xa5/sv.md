---
term: OP_WITHIN (0XA5)
definition: Opcode som kollar om ett värde ligger inom ett intervall som definieras av två andra värden.
---

Kontrollerar om det översta elementet på stacken ligger inom det intervall som definieras av den andra och tredje översta Elements. Med andra ord kontrollerar `OP_WITHIN` om det översta elementet är större än eller lika med det andra och mindre än det tredje. Om detta villkor är sant skjuts `1` (sant) upp på stacken, annars skjuts `0` (falskt) upp.