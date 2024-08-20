---
term: OP_2DUP (0X6E)
---

复制栈顶的两个元素，然后将它们放回栈顶。例如，如果栈是：

```text
A
B
C
D
```

`OP_2DUP` 将产生：

```text
A
B
A
B
C
D
```