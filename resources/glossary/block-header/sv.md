---
term: BLOCK HUVUDEN
---

Blockhuvudet är en datastruktur som fungerar som huvudkomponent i konstruktionen av ett Bitcoin-block. Varje block består av en header och en lista med transaktioner. Blockhuvudet innehåller viktig information som säkerställer integriteten och giltigheten för ett block inom Blockchain. Blockhuvudet innehåller 80 byte metadata och består av följande Elements:


- Blockversionen;
- Hash i föregående block;
- Merkle Tree är roten till transaktionerna;
- Blocket Timestamp;
- Svårighetsmålet;
- Nonce.


Här är till exempel rubriken för blocknummer 785 530 i hexadecimalt format, utvunnet av Foundry USA den 15 april 2023:


```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```


Om vi bryter ner den här rubriken kan vi känna igen:


- Versionen:


```text
00e0ff3f
```



- Den tidigare Hash:


```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```



- Merkle Root:


```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```



- Timestamp:


```text
bcb13a64
```



- Målet:


```text
b2e00517
```



- Nonce:


```text
43f09a40
```


För att vara giltigt måste ett block ha ett huvud som, när det har hashats med `SHA256d`, producerar en Hash som är mindre än eller lika med svårighetsmålet.


> ► *På engelska kallas det för "Block Header"*