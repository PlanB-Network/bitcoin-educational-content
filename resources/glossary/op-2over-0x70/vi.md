---
term: OP_2OVER (0X70)

definition: Mã vận hành sao chép các phần tử thứ 3 và thứ 4 của ngăn xếp lên đầu.
---
Copies the two elements that are in the fourth and third positions from the top of the stack, then places them on top of the stack. For example, if the stack is:

```text
A
B
C
D
```

`OP_2OVER` will produce:

```text
C
D
A
B
C
D
```