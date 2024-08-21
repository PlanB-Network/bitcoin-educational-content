---
termi: OP_TUCK (0X7D)
---

Kopioi pinon päällimmäisen alkion ja sijoittaa sen toisen ja kolmannen alkion väliin. Esimerkiksi, jos pino on:

```text
A
B
C
D
```

`OP_TUCK` kopioi päällimmäisen alkion `A` ja sijoittaa sen kolmanteen positioon. Tuloksena oleva pino on:

```text
A
B
A
C
D
```