---
term: OP_2SWAP (0X72)

definition: Opcode yang menukar dua elemen pertama tumpukan dengan dua elemen berikutnya.
---
Menukar dua elemen di bagian atas _stack_ dengan dua elemen tepat di bawahnya. Misalnya, jika _stack_-nya adalah:

```text
A
B
C
D
```

`OP_2SWAP` akan menghasilkan:

```text
C
D
A
B
```
