---
term: OP_2DUP (0X6E)

definition: Opcode yang menduplikasi dua elemen di bagian atas tumpukan.
---
Menduplikasi dua elemen teratas dari _stack_, lalu menempatkannya di atas _stack_. Misalnya, jika _stack_ awalnya adalah:

```text
A
B
C
D
```

Operasi `OP_2DUP` akan menghasilkan:

```text
A
B
A
B
C
D
```
