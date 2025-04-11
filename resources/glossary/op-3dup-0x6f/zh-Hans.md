---
term: OP_3DUP (0X6F)

---
复制堆栈的前三个元素，然后将它们放到堆栈的顶部。例如，如果堆栈是

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