---
term: OP_2SWAP (0X72)

definition: 将堆栈顶部的两个元素与接下来的两个元素交换位置的操作码。
---
将栈顶的两个元素与其栈底的两个元素交换位置。例如，如果堆栈如下：

```text
A
B
C
D
```

`OP_2SWAP` 将产生：

```text
C
D
A
B
```
