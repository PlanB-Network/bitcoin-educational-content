---
term: BLOCK HEADER

---
Záhlaví bloku je datová struktura, která slouží jako hlavní součást při vytváření bloku Bitcoinu. Každý blok se skládá ze záhlaví a seznamu transakcí. Záhlaví bloku obsahuje klíčové informace, které zajišťují integritu a platnost bloku v rámci blockchainu. Záhlaví bloku obsahuje 80 bajtů metadat a skládá se z následujících prvků:


- Bloková verze;
- Hash předchozího bloku;
- Kořen Merkleova stromu transakcí;
- Časové razítko bloku;
- Cíl obtížnosti;
- Nonce.

Například zde je hlavička bloku číslo 785 530 v hexadecimálním formátu, vytěženého společností Foundry USA 15. dubna 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Pokud tuto hlavičku rozdělíme, můžeme rozpoznat:


- Verze:

```text
00e0ff3f
```


- Předchozí hash:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```


- Kořen Merkle:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```


- Časové razítko:

```text
bcb13a64
```


- Cíl:

```text
b2e00517
```


- Nonce:

```text
43f09a40
```

Aby byl blok platný, musí mít hlavičku, která po zaheslování pomocí `SHA256d` dává hash, který je menší nebo roven cíli obtížnosti.

> ► V angličtině se označuje jako "Block Header".*