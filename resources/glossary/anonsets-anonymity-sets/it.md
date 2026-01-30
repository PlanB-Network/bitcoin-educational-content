---
term: Anonsets (anonymity sets)

definition: Indicatori che misurano il grado di privacy di un UTXO contando il numero di UTXO indistinguibili in un insieme, tipicamente dopo un coinjoin.
---
Gli anonset fungono da indicatori per valutare il grado di riservatezza di uno specifico UTXO. Più precisamente, misurano il numero di UTXO indistinguibili all'interno dell'insieme che include la moneta in esame. Poiché è necessario disporre di un gruppo di UTXO identici, gli anonset vengono generalmente calcolati all'interno di un ciclo di coinjoins. Essi consentono, se del caso, di valutare la qualità dei coinjoins. Un anonset di grandi dimensioni implica un livello di anonimato più elevato, poiché diventa difficile distinguere un UTXO specifico all'interno dell'insieme.

Esistono due tipi di anonset: il forward anonset (forward-looking metrics); e il backward anonset (backward-looking metrics). Il termine "*score*" è talvolta utilizzato anche per indicare gli anonset.

Il primo indica la dimensione del gruppo all'interno del quale si nasconde l'UTXO di uscita analizzato, dato l'UTXO di ingresso. Questo indicatore consente di misurare la resistenza della riservatezza della moneta rispetto a un'analisi dal passato al presente (dall'ingresso all'uscita). Il secondo indica il numero di fonti possibili per una determinata moneta, dato l'UTXO di uscita. Questo indicatore consente di misurare la resistenza della riservatezza della moneta rispetto a un'analisi dal presente al passato (dall'uscita all'ingresso).










