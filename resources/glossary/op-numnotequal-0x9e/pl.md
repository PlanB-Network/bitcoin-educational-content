---
term: OP_NUMNOTEQUAL (0X9E)
definition: Opcode sprawdzający, czy dwa elementy na szczycie stosu są różne liczbowo.
---

Porównuje dwa najwyższe Elements na stosie, aby sprawdzić, czy są one numerycznie nierówne. Jeśli wartości nie są równe, przesuwa `1` (prawda) na stos, w przeciwnym razie przesuwa `0` (fałsz). Jest to przeciwieństwo funkcji `OP_NUMEQUAL`.