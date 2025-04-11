---
term: BLOCK HEADER

---
Blokkhodet er en datastruktur som fungerer som hovedkomponent i oppbyggingen av en Bitcoin-blokk. Hver blokk består av en header og en liste over transaksjoner. Blokkhodet inneholder viktig informasjon som sikrer integriteten og gyldigheten til en blokk i blokkjeden. Blokkhodet inneholder 80 byte med metadata og består av følgende elementer:


- Blokkversjonen;
- Hashverdien til den forrige blokken;
- Roten til Merkle-treet for transaksjonene;
- Tidsstempelet for blokken;
- Vanskelighetsgraden er målet;
- Noncen.

Her er for eksempel overskriften til blokk nummer 785 530 i heksadesimalt format, utvunnet av Foundry USA den 15. april 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Hvis vi bryter ned denne overskriften, kan vi gjenkjenne:


- Versjonen:

```text
00e0ff3f
```


- Den forrige hasjen:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```


- Merkle-roten:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```


- Tidsstempelet:

```text
bcb13a64
```


- Målet:

```text
b2e00517
```


- Noncen:

```text
43f09a40
```

For å være gyldig må en blokk ha en header som, når den er hashet med `SHA256d`, gir en hash som er mindre enn eller lik vanskelighetsmålet.

> på engelsk kalles det en "Block Header"