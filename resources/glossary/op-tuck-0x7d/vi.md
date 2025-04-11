---
term: OP_TUCK (0X7D)

---
Copies the item at the top of the stack and inserts it between the second and third items of the stack. For example, if the stack is:

```text
A
B
C
D
```

`OP_TUCK` will duplicate the top item `A` and place it in the third position. The resulting stack will be:

```text
A
B
A
C
D
```