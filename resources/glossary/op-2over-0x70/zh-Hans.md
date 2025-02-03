---
term: op_2over (0x70)

---
复制堆栈顶部第四位和第三位的两个元素，然后将它们放到堆栈顶部。例如，如果堆栈为

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