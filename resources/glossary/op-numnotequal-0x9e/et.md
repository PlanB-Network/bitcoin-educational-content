---
term: OP_NUMNOTEQUAL (0X9E)

definition: Opcode, mis kontrollib, kas pinu ülemised kaks elementi on arvuliselt erinevad.
---
Võrreldakse virna kahte kõige ülemist elementi, et kontrollida, kas need on numbriliselt ebavõrdsed. Kui väärtused ei ole võrdsed, lükkab ta virna `1` (true), vastasel juhul lükkab ta `0` (false). See on vastupidine `OP_NUMEQUAL`-ile.