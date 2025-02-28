---
term: OP_3DUP (0X6F)

---
Duplicates the top three elements of the stack, then places them on top of the stack. For example, if the stack is:

```text
A
B
C
D
```

`OP_3DUP` will produce:

```text
A
B
C
A
B
C
D
```