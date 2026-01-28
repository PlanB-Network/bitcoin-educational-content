---
term: OP_NUMNOTEQUAL (0X9E)
definition: Opcode checking if the two top elements on the stack are numerically different.
---

Compares the two topmost elements on the stack to check if they are numerically unequal. If the values are not equal, it pushes `1` (true) onto the stack, otherwise, it pushes `0` (false). This is the opposite of `OP_NUMEQUAL`.