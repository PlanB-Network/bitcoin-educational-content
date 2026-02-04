---
term: OP_2DUP (0X6E)
definition: Opcode som duplicerar de två översta elementen på stacken.
---

Duplicerar de två översta Elements i stapeln och placerar dem sedan ovanpå stapeln. Till exempel, om stapeln är:


```text
A
B
C
D
```


`OP_2DUP` kommer att producera:


```text
A
B
A
B
C
D
```