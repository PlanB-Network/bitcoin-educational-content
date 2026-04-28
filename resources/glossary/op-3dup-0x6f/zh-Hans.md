---
term: OP_3DUP (0X6F)

definition: 复制堆栈顶部三个操作数的操作码。
---
复制堆栈的最上三个元素，然后将它们放入堆栈的顶部。例如，如果堆栈如下：

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
