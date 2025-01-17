---
term: OUTPOINT

---
Uma referência única a uma saída de transação não gasta (UTXO). É constituída por dois elementos:


- `txid`: o identificador da transação que criou a saída;
- vout: o índice da saída na transação.

A combinação destes dois elementos identifica com precisão um UTXO. Por exemplo, se uma transação tiver um `txid` de `abc...123` e o índice de saída for `0`, o ponto de saída será registado como:

```text
abc...123:0
```

O ponto de saída é utilizado nas entradas (`vin`) de uma nova transação para indicar qual o UTXO que está a ser gasto.

> ► *O termo "outpoint" é frequentemente utilizado como sinónimo de "UTXO"