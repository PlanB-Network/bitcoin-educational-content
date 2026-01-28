---
term: OP_2ROT (0X71)
definition: Opcode som flyttar det 5e och 6e elementet i stacken till toppen.
---

Flyttar de två Elements som befinner sig i sjätte och femte positionen från toppen av stacken till toppen. Till exempel, om stapeln är:


```text
A
B
C
D
E
F
```


`OP_2ROT` kommer att producera:


```text
E
F
A
B
C
D
```