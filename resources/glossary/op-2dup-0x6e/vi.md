---
term: OP_2DUP (0X6E)

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