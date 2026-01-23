---
term: OP_2SWAP (0X72)
definition: Opcode échangeant les deux premiers éléments de la pile avec les deux suivants.
---

Échange les deux éléments situés au sommet de la pile avec les deux éléments situés juste en dessous d'eux. Par exemple, si la pile est :
```text
A
B
C
D
```
`OP_2SWAP` produira :
```text
C
D
A
B
```
