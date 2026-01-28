---
term: OP_2ROT (0X71)

definition: Op-koodi, joka siirtää pinon 5. ja 6. elementin pinon päälle.
---
Siirtää kaksi elementtiä, jotka ovat kuudennella ja viidennellä sijalla, pinon yläosasta päällimmäiseksi. Jos pino on esimerkiksi:

```text
A
B
C
D
E
F
```

`OP_2ROT` tuottaa:

```text
E
F
A
B
C
D
```