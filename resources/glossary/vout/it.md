---
term: VOUT

---
Elemento specifico di una transazione Bitcoin che determina la destinazione dei fondi inviati. Una transazione può includere più uscite, ciascuna identificata in modo univoco dalla combinazione dell'identificatore della transazione (`txid`) e di un indice chiamato `vout`. Questo indice, che inizia con `0`, indica la posizione dell'uscita nella sequenza delle uscite della transazione. Pertanto, la prima uscita sarà designata da `"vout": 0`, la seconda con `"vout": 1`, e così via.

Ogni `vout' incapsula principalmente due informazioni:


- il valore, espresso in bitcoin, che rappresenta l'importo inviato;
- uno script di blocco (`scriptPubKey`) che stabilisce le condizioni necessarie affinché i fondi possano essere spesi nuovamente in una transazione futura.

La combinazione del `txid` e del `vout` di un pezzo specifico forma quello che viene chiamato UTXO, ad esempio:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```