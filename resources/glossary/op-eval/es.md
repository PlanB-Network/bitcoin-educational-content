---
term: OP_EVAL

---
Opcode propuesto por Gavin Andresen en 2011. Toma el script situado en la parte superior de la pila, lo ejecuta como si fuera parte del `scriptPubKey`, y coloca su resultado en la pila. `OP_EVAL` fue abandonado debido a preocupaciones relacionadas con la complejidad de este opcode, que con el tiempo sería sustituido por P2SH.