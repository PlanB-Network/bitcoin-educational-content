---
term: OP_2DUP (0X6E)

definition: Op-koodi, joka monistaa kaksi ylintä elementtiä pinossa.
---
Monistaa pinon kaksi ylintä elementtiä ja asettaa ne sitten pinon päälle. Jos pino on esimerkiksi:

```text
A
B
C
D
```

`OP_2DUP` tuottaa:

```text
A
B
A
B
C
D
```