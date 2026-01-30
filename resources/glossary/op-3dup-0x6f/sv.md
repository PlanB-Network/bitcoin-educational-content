---
term: OP_3DUP (0X6F)
definition: Opcode som duplicerar de tre översta elementen på stacken.
---

Duplicerar de tre översta Elements i stacken och placerar dem sedan ovanpå stacken. Till exempel, om stapeln är:


```text
A
B
C
D
```


`OP_3DUP` kommer att producera:


```text
A
B
C
A
B
C
D
```