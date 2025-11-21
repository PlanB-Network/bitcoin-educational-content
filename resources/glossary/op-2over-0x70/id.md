---
term: OP_2OVER (0X70)

---
Menyalin dua elemen yang berada di posisi keempat dan ketiga dari atas _stack_, lalu menempatkannya di atas _stack_. Misalnya, jika _stack_-nya adalah:

```text
A
B
C
D
```

`OP_2OVER` akan menghasilkan:

```text
C
D
A
B
C
D
```
