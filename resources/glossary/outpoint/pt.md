---
term: OUTPOINT
---

Uma referência única para uma saída de transação não gasta (UTXO). Consiste em dois elementos:
* `txid`: o identificador da transação que criou a saída;
* `vout`: o índice da saída na transação.

A combinação desses dois elementos identifica precisamente um UTXO. Por exemplo, se uma transação tem um `txid` de `abc...123` e o índice da saída é `0`, o outpoint será notado como:

```text
abc...123:0
```

O outpoint é usado nas entradas (`vin`) de uma nova transação para indicar qual UTXO está sendo gasto.

> ► *O termo "outpoint" é frequentemente usado como sinônimo de "UTXO".*