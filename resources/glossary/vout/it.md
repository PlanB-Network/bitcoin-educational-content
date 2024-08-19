---
termine: VOUT
---

Un elemento specifico di una transazione Bitcoin che determina la destinazione dei fondi inviati. Una transazione può includere più output, ciascuno identificato univocamente dalla combinazione dell'identificatore della transazione (`txid`) e di un indice chiamato `vout`. Questo indice, che inizia da `0`, segna la posizione dell'output nella sequenza degli output della transazione. Pertanto, il primo output sarà designato da `"vout": 0`, il secondo da `"vout": 1`, e così via.

Ogni `vout` incapsula principalmente due pezzi di informazioni:
* il valore, espresso in bitcoin, che rappresenta l'importo inviato;
* uno script di blocco (`scriptPubKey`) che stabilisce le condizioni richieste affinché i fondi possano essere spesi nuovamente in una futura transazione.

La combinazione del `txid` e del `vout` di uno specifico pezzo costituisce quello che viene chiamato un UTXO, per esempio:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```