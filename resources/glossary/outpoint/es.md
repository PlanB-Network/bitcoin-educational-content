---
term: OUTPOINT
---

Una referencia única a una salida de transacción no gastada (UTXO). Consiste en dos elementos:
* `txid`: el identificador de la transacción que creó la salida;
* `vout`: el índice de la salida en la transacción.

La combinación de estos dos elementos identifica precisamente un UTXO. Por ejemplo, si una transacción tiene un `txid` de `abc...123` y el índice de salida es `0`, el outpoint se anotará como:

```text
abc...123:0
```

El outpoint se utiliza en las entradas (`vin`) de una nueva transacción para indicar qué UTXO se está gastando.

> ► *El término "outpoint" se usa a menudo como sinónimo de "UTXO".*