---
term: BLOCK HEADER
---

Block header je datová struktura, která slouží jako hlavní komponenta při konstrukci Bitcoinového bloku. Každý blok se skládá z hlavičky a seznamu transakcí. Hlavička bloku obsahuje zásadní informace, které zajišťují integritu a platnost bloku v rámci blockchainu. Hlavička bloku obsahuje 80 bajtů metadat a skládá se z následujících prvků:
* Verze bloku;
* Hash předchozího bloku;
* Kořen Merkleova stromu transakcí;
* Časové razítko bloku;
* Cílová obtížnost;
* Nonce.

Například zde je hlavička bloku číslo 785,530 ve formátu hexadecimální, vytěžená Foundry USA 15. dubna 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Pokud rozložíme tuto hlavičku, můžeme rozpoznat:
* Verzi:

```text
00e0ff3f
```

* Předchozí hash:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```

* Merkleův kořen:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```

* Časové razítko:

```text
bcb13a64
```

* Cíl:

```text
b2e00517
```

* Nonce:

```text
43f09a40
```

Aby byl blok platný, musí mít hlavičku, která, jednou zahašovaná pomocí `SHA256d`, produkuje hash, který je menší nebo roven cílové obtížnosti.

> ► *V angličtině se tomu říká "Block Header".*