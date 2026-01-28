---
term: OP_EVAL

definition: Opcode propuesto en 2011 y abandonado, finalmente reemplazado por P2SH.
---
Opcode propuesto por Gavin Andresen en 2011. Toma el script situado en la parte superior de la pila, lo ejecuta como si fuera parte del `scriptPubKey`, y coloca su resultado en la pila. `OP_EVAL` fue abandonado debido a preocupaciones relacionadas con la complejidad de este opcode, que con el tiempo sería sustituido por P2SH.