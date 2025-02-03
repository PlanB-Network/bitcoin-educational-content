---
term: OP_2SWAP (0X72)

---
Swaps the two elements at the top of the stack with the two elements just below them. For example, if the stack is:

```text
A
B
C
D
```

`OP_2SWAP` will produce:

```text
C
D
A
B
```