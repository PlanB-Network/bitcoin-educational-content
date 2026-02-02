---
term: OP_WITHIN (0XA5)
definition: Opcode die controleert of een waarde binnen een bereik ligt dat door twee andere waarden is gedefinieerd.
---

Controleert of het bovenste element op de stack binnen het bereik ligt dat gedefinieerd wordt door de tweede en derde Elements. Met andere woorden, `OP_WITHIN` controleert of het bovenste element groter of gelijk is aan het tweede en kleiner dan het derde. Als deze voorwaarde waar is, duwt het `1` (true) op de stack, anders duwt het `0` (false).