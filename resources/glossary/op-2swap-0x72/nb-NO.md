---
term: OP_2SWAP (0X72)

definition: Opcode som bytter de to første elementene på stakken med de to neste.
---
Bytter ut de to elementene øverst i stakken med de to elementene rett under dem. For eksempel, hvis stakken er:

```text
A
B
C
D
```

`OP_2SWAP` vil produsere:

```text
C
D
A
B
```