---
term: OP_3DUP (0X6F)

---
Menduplikasi tiga elemen teratas dari _stack_, lalu menempatkannya di atas _stack_. Misalnya, jika keadaan _stack_ awal adalah sebagai berikut:

```text
A
B
C
D
```

`OP_3DUP` akan menghasilkan:

```text
A
B
C
A
B
C
D
```
