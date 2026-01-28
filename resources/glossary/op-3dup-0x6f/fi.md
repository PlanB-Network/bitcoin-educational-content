---
term: OP_3DUP (0X6F)

definition: Op-koodi, joka monistaa kolme ylintä elementtiä pinossa.
---
Kopioi pinon kolme ylintä elementtiä ja asettaa ne sitten pinon päälle. Jos pino on esimerkiksi:

```text
A
B
C
D
```

`OP_3DUP` tuottaa:

```text
A
B
C
A
B
C
D
```