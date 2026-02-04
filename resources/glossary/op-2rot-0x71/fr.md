---
term: OP_2ROT (0X71)
definition: Opcode déplaçant les 5e et 6e éléments de la pile vers le sommet.
---

Déplace les deux éléments qui se trouvent à la sixième et à la cinquième place du sommet de la pile vers le sommet. Par exemple, si la pile est :
```text
A
B
C
D
E
F
```
`OP_2ROT` produira :
```text
E
F
A
B
C
D
```
