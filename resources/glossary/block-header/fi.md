---
term: BLOCK HEADER

---
Lohkon otsikko on tietorakenne, joka on Bitcoin-lohkon rakentamisen pääkomponentti. Jokainen lohko koostuu otsikosta ja transaktioiden luettelosta. Lohko-otsikko sisältää ratkaisevia tietoja, joilla varmistetaan lohkon eheys ja pätevyys lohkoketjussa. Lohkootsikko sisältää 80 tavua metatietoa, ja se koostuu seuraavista elementeistä:


- Lohkoversio;
- Edellisen lohkon hash;
- Tapahtumien Merkle-puun juuri;
- Lohkon aikaleima;
- Vaikeuskohde;
- Nonce.

Esimerkiksi tässä on Foundry USA:n 15. huhtikuuta 2023 louhiman lohkon numero 785,530 otsikko heksadesimaalimuodossa:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Jos hajotamme tämän otsikon, voimme tunnistaa:


- Versio:

```text
00e0ff3f
```


- Edellinen hash:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```


- Merkle-juuri:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```


- Aikaleima:

```text
bcb13a64
```


- Kohde:

```text
b2e00517
```


- Nonce:

```text
43f09a40
```

Ollakseen kelvollinen lohkolla on oltava otsikko, joka `SHA256d`:llä hajautettuna tuottaa hajautuksen, joka on pienempi tai yhtä suuri kuin vaikeustavoite.

> ► *Englanniksi sitä kutsutaan nimellä "Block Header".*