---
term: OP_2OVER (0X70)
definition: Opcode copying the 3rd and 4th elements of the stack to the top.
---

Copies the two elements that are in the fourth and third positions from the top of the stack, then places them on top of the stack. For example, if the stack is:

```text
A
B
C
D
```

`OP_2OVER` will produce:

```text
C
D
A
B
C
D
```