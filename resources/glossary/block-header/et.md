---
term: BLOCK HEADER

---
Ploki päis on andmestruktuur, mis on Bitcoini ploki ülesehituse põhikomponent. Iga plokk koosneb päisest ja tehingute loetelust. Ploki päis sisaldab olulist teavet, mis tagab ploki terviklikkuse ja kehtivuse plokiahelas. Ploki päis sisaldab 80 baiti metaandmeid ja koosneb järgmistest elementidest:


- Plokkversioon;
- Eelmise ploki hash;
- Tehingute Merkle-puu juur;
- Bloki ajatempel;
- Raskuse sihtmärk;
- Nonce.

Näiteks siin on plokki number 785,530 pealkiri heksadetsimaalses formaadis, mille kaevandas Foundry USA 15. aprillil 2023. aastal:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Kui me selle pealkirja lahti mõtestame, siis võime ära tunda:


- Versioon:

```text
00e0ff3f
```


- Eelmine hash:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```


- Merkle'i juur:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```


- Ajatempel:

```text
bcb13a64
```


- Eesmärk:

```text
b2e00517
```


- Nonce:

```text
43f09a40
```

Et olla kehtiv, peab plokil olema päis, mis pärast "SHA256d"-ga hashimist annab tulemuseks hashi, mis on väiksem või võrdne raskusastmega.

> ► *Inglise keeles nimetatakse seda "Block Header"