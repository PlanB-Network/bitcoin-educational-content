---
term: OP_TUCK (0X7D)

---
Kopioi pinon ylimmässä kohdassa olevan kohteen ja lisää sen pinon toisen ja kolmannen kohteen väliin. Jos pino on esimerkiksi:

```text
A
B
C
D
```

`OP_TUCK` kopioi ylimmän elementin `A` ja sijoittaa sen kolmanteen kohtaan. Tuloksena on pino:

```text
A
B
A
C
D
```