---
term: OP_NUMNOTEQUAL (0X9E)

definition: Opcode, der prüft, ob die beiden obersten Stack-Elemente numerisch ungleich sind.
---
Vergleicht die beiden obersten Elemente auf dem Stapel, um zu prüfen, ob sie numerisch ungleich sind. Wenn die Werte nicht gleich sind, wird `1` (wahr) auf den Stapel geschoben, andernfalls wird `0` (falsch) geschoben. Dies ist das Gegenteil von `OP_NUMEQUAL`.