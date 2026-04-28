---
term: OP_2SWAP (0X72)
definition: Opcode som byter plats på de två första elementen på stacken med de två nästföljande.
---

Byter ut de två Elements högst upp i stapeln mot de två Elements strax under dem. Till exempel, om stapeln är:


```text
A
B
C
D
```


`OP_2SWAP` kommer att producera:


```text
C
D
A
B
```