---
term: OP_2DUP (0x6E)

---
复制堆栈顶部的两个元素，然后将它们放入堆栈顶部。例如，如果堆栈中元素如下：

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
