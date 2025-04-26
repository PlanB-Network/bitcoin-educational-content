---
term: TESTA DI BLOCCO

---
L'intestazione del blocco è una struttura di dati che funge da componente principale nella costruzione di un blocco Bitcoin. Ogni blocco è composto da un'intestazione e da un elenco di transazioni. L'intestazione del blocco contiene informazioni cruciali che garantiscono l'integrità e la validità di un blocco all'interno della blockchain. L'intestazione del blocco contiene 80 byte di metadati ed è composta dai seguenti elementi:


- La versione a blocchi;
- L'hash del blocco precedente;
- La radice dell'albero Merkle delle transazioni;
- Il timestamp del blocco;
- L'obiettivo di difficoltà;
- Il nonce.

Ad esempio, ecco l'intestazione del blocco numero 785.530 in formato esadecimale, estratto da Foundry USA il 15 aprile 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Se scomponiamo questa intestazione, possiamo riconoscere:


- La versione:

```text
00e0ff3f
```


- L'hash precedente:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```


- La radice Merkle:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```


- Il timestamp:

```text
bcb13a64
```


- L'obiettivo:

```text
b2e00517
```


- Il nonce:

```text
43f09a40
```

Per essere valido, un blocco deve avere un'intestazione che, una volta sottoposta a hash con `SHA256d`, produca un hash inferiore o uguale all'obiettivo di difficoltà.

> *In inglese, si parla di "Block Header" (intestazione del blocco)