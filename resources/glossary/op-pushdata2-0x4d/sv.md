---
term: OP_PUSHDATA2 (0X4D)
definition: Opcode som skjuter in upp till 65 KB data på stacken.
---

Gör det möjligt att lägga en stor mängd data på stacken. Den följs av två byte (little-endian) som anger längden på de data som ska skjutas (upp till ca 65 KB). Det används för att infoga större data i skript.