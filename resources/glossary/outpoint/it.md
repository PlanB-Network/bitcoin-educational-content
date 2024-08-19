termine: OUTPOINT

Un riferimento unico a un output di transazione non speso (UTXO). È composto da due elementi:
* `txid`: l'identificatore della transazione che ha creato l'output;
* `vout`: l'indice dell'output nella transazione.

La combinazione di questi due elementi identifica precisamente un UTXO. Ad esempio, se una transazione ha un `txid` di `abc...123` e l'indice dell'output è `0`, l'outpoint sarà indicato come:

```text
abc...123:0
```

L'outpoint è utilizzato negli input (`vin`) di una nuova transazione per indicare quale UTXO sta venendo speso.

> ► *Il termine "outpoint" è spesso usato come sinonimo di "UTXO".*