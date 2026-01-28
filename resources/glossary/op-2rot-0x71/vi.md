---
term: OP_2ROT (0X71)

definition: Mã vận hành di chuyển các phần tử thứ 5 và thứ 6 của ngăn xếp lên đầu.
---
Moves the two elements that are in the sixth and fifth positions from the top of the stack to the top. For example, if the stack is:

```text
A
B
C
D
E
F
```

`OP_2ROT` will produce:

```text
E
F
A
B
C
D
```