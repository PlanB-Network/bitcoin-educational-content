---
term: OP_2ROT (0X71)
definition: Opcode moving the 5th and 6th elements of the stack to the top.
---

Moves the two elements that are in the sixth and fifth positions from the top of the stack to the top. For example, if the stack is:

```text
A
B
C
D
E
F
```

`OP_2ROT` will produce:

```text
E
F
A
B
C
D
```