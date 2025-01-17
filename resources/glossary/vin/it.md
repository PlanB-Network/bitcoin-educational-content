---
term: VIN

---
Elemento specifico di una transazione Bitcoin che specifica la fonte dei fondi utilizzati per soddisfare gli output. Ogni `vin` si riferisce a un output non speso (UTXO) di una transazione precedente. Una transazione può contenere più ingressi, ciascuno identificato da una combinazione di `txid` (l'identificatore della transazione originale) e `vout` (l'indice dell'uscita in quella transazione).

Ogni `vin` include le seguenti informazioni:


- `txid`: l'identificatore della transazione precedente che contiene l'output utilizzato come input;
- `vout`: l'indice dell'output nella transazione precedente;
- `scriptSig` o `scriptWitness`: uno script di sblocco che fornisce i dati necessari per soddisfare le condizioni poste dalla `scriptPubKey` della transazione precedente i cui fondi vengono spesi, di solito fornendo una firma crittografica;
- `nSequence`: un campo specifico utilizzato per indicare il modo in cui questo ingresso è bloccato nel tempo, oltre ad altre opzioni come RBF.