---
term: OP_2OVER (0X70)

definition: 将堆栈中的第3个和第4个元素复制到堆栈顶部的操作码。
---
复制位于栈顶第四和第三个位置的两个元素，并将它们放入栈顶。例如，如果堆栈为：

```text
A
B
C
D
```

`OP_2OVER` 将产生：

```text
C
D
A
B
C
D
```
