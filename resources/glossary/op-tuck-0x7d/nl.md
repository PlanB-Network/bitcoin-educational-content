---
term: OP_TUCK (0X7D)
definition: Opcode die de bovenkant van de stack kopieert en op de derde positie invoegt.
---

Kopieert het item bovenaan de stack en voegt het in tussen het tweede en derde item van de stack. Bijvoorbeeld, als de stapel is:


```text
A
B
C
D
```


`OP_TUCK` dupliceert het bovenste item `A` en plaatst het op de derde positie. De resulterende stapel zal zijn:


```text
A
B
A
C
D
```