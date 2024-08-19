term: VIN

Un elemento specifico di una transazione Bitcoin che specifica la fonte dei fondi utilizzati per soddisfare gli output. Ogni `vin` fa riferimento a un output non speso (UTXO) da una transazione precedente. Una transazione può contenere più input, ciascuno identificato da una combinazione del `txid` (l'identificatore della transazione originale) e del `vout` (l'indice dell'output in quella transazione).

Ogni `vin` include le seguenti informazioni:
* `txid`: l'identificatore della transazione precedente contenente l'output utilizzato qui come input;
* `vout`: l'indice dell'output nella transazione precedente;
* `scriptSig` o `scriptWitness`: uno script di sblocco che fornisce i dati necessari per soddisfare le condizioni poste dallo `scriptPubKey` della transazione precedente i cui fondi vengono spesi, solitamente fornendo una firma crittografica;
* `nSequence`: un campo specifico utilizzato per indicare come questo input è vincolato nel tempo, così come altre opzioni come RBF.