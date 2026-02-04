---
term: OP_2DUP (0X6E)
definition: Opcode duplicating the two elements at the top of the stack.
---

Duplicates the two top elements of the stack, then places them on top of the stack. For example, if the stack is:

```text
A
B
C
D
```

`OP_2DUP` will produce:

```text
A
B
A
B
C
D
```