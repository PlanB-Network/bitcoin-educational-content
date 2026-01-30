---
term: OP_3DUP (0X6F)

definition: Opcode yang menduplikasi tiga elemen di bagian atas tumpukan.
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
