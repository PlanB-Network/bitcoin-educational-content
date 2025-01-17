---
term: PUNTO ESTERNO

---
Riferimento univoco a un'uscita di transazione non spesa (UTXO). Si compone di due elementi:


- `txid`: l'identificatore della transazione che ha creato l'output;
- `vout`: l'indice dell'output nella transazione.

La combinazione di questi due elementi identifica con precisione un UTXO. Ad esempio, se una transazione ha un `txid` di `abc...123` e l'indice di uscita è `0`, l'outpoint sarà indicato come:

```text
abc...123:0
```

L'outpoint viene utilizzato negli ingressi (`vin`) di una nuova transazione per indicare quale UTXO viene speso.

> *Il termine "outpoint" è spesso usato come sinonimo di "UTXO"