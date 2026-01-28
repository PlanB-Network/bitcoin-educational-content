---
term: OP_2OVER (0X70)
definition: Opcode som kopierar det 3e och 4e elementet i stacken till toppen.
---

Kopierar de två Elements som står på fjärde och tredje plats från toppen av stacken och lägger dem sedan ovanpå stacken. Till exempel, om stacken är:


```text
A
B
C
D
```


`OP_2OVER` kommer att producera:


```text
C
D
A
B
C
D
```