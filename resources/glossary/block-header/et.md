---
term: BLOKI PÄIS
---

Bloki päis on andmestruktuur, mis toimib peamise komponendina Bitcoin'i bloki ehitamisel. Iga blokk koosneb päisest ja tehingute loendist. Bloki päis sisaldab olulist informatsiooni, mis tagab bloki terviklikkuse ja kehtivuse blockchainis. Bloki päis sisaldab 80 baiti metaandmeid ja koosneb järgmistest elementidest:
* Bloki versioon;
* Eelmise bloki räsi;
* Tehingute Merkle puu juur;
* Bloki ajatempel;
* Raskusaste;
* Nonce.

Näiteks siin on bloki number 785,530 päis heksadetsimaalformaadis, mille kaevandas Foundry USA 15. aprillil 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Kui me selle päise lahti võtame, saame ära tunda:
* Versiooni:

```text
00e0ff3f
```

* Eelmise räsi:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```

* Merkle juure:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```

* Ajatempli:

```text
bcb13a64
```

* Sihtmärgi:

```text
b2e00517
```

* Nonce:

```text
43f09a40
```

Selleks, et blokk oleks kehtiv, peab sellel olema päis, mis pärast `SHA256d` räsiga töötlemist toodab räsi, mis on väiksem või võrdne raskusastmega.

> ► *Inglise keeles viidatakse sellele kui "Block Header".*