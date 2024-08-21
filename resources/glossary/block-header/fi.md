---
termi: LOHKON OTSIKKO
---

Lohkon otsikko on tietorakenne, joka toimii pääkomponenttina Bitcoin-lohkon rakentamisessa. Jokainen lohko koostuu otsikosta ja tapahtumien listasta. Lohkon otsikko sisältää olennaista tietoa, joka varmistaa lohkon eheyden ja pätevyyden lohkoketjussa. Lohkon otsikko sisältää 80 tavua metadataa ja koostuu seuraavista elementeistä:
* Lohkon versio;
* Edellisen lohkon tiiviste (hash);
* Tapahtumien Merkle-puun juuri;
* Lohkon aikaleima;
* Vaikeustavoite;
* Nonce-arvo.

Esimerkiksi, tässä on lohkon numero 785,530 otsikko heksadesimaalimuodossa, jonka louhi Foundry USA 15. huhtikuuta 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Jos puretaan tämä otsikko, voimme tunnistaa:
* Version:

```text
00e0ff3f
```

* Edellisen tiivisteen:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```

* Merkle-juuren:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```

* Aikaleiman:

```text
bcb13a64
```

* Tavoitteen:

```text
b2e00517
```

* Nonce-arvon:

```text
43f09a40
```

Jotta lohko olisi pätevä, sen otsikon on, kun se tiivistetään `SHA256d`-algoritmilla, tuotettava tiiviste, joka on pienempi tai yhtä suuri kuin vaikeustavoite.

> ► *Englanniksi tätä kutsutaan "Block Header" eli lohkon otsikoksi.*