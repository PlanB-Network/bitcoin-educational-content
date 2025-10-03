---
term: OP_TUCK (0X7D)
---

Kopierar objektet högst upp i stacken och infogar det mellan det andra och tredje objektet i stacken. Till exempel, om stacken är:


```text
A
B
C
D
```


`OP_TUCK` kommer att duplicera det översta objektet `A` och placera det i tredje positionen. Den resulterande stapeln kommer att vara:


```text
A
B
A
C
D
```