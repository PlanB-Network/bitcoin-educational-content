---
term: OP_3DUP (0X6F)
---

复制栈顶的三个元素，然后将它们放回栈顶。例如，如果栈是：

```text
A
B
C
D
```

`OP_3DUP` 将产生：

```text
A
B
C
A
B
C
D
```