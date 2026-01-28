---
term: OP_2OVER (0X70)

definition: Op-koodi, joka kopioi pinon 3. ja 4. elementin pinon päälle.
---
Kopioi kaksi elementtiä, jotka ovat neljäntenä ja kolmantena pinon yläreunasta, ja asettaa ne sitten pinon päälle. Jos pino on esimerkiksi:

```text
A
B
C
D
```

`OP_2OVER` tuottaa:

```text
C
D
A
B
C
D
```