---
term: MURO DI PIETRA

---
Una forma specifica di transazione Bitcoin volta ad aumentare la privacy dell'utente durante una spesa, imitando una coinjoin tra due persone, senza esserlo realmente. Infatti, questa transazione non è collaborativa. Un utente può costruirla da solo, coinvolgendo solo i propri UTXO come input. Pertanto, è possibile creare una transazione Stonewall per qualsiasi occasione, senza bisogno di sincronizzarsi con un altro utente.

Il funzionamento della transazione Stonewall è il seguente: all'ingresso della transazione, il mittente utilizza 2 UTXO che gli appartengono. La transazione produce quindi 4 uscite, 2 delle quali saranno esattamente lo stesso importo. Gli altri 2 costituiranno il cambiamento. Tra le due uscite dello stesso importo, solo una andrà effettivamente al destinatario del pagamento.

Pertanto, ci sono solo 2 ruoli in una transazione Stonewall:


- Il mittente, che effettua il pagamento effettivo;
- Il destinatario, che potrebbe non essere a conoscenza della natura specifica della transazione e attende semplicemente il pagamento da parte del mittente.

![](../../dictionnaire/assets/33.webp)

Le transazioni Stonewall sono disponibili sia sull'applicazione Samourai Wallet che sul software Sparrow Wallet.

La struttura Stonewall aggiunge molta entropia alla transazione e oscura la traccia per l'analisi della catena. Dall'esterno, una transazione di questo tipo può essere interpretata come una piccola unione di monete tra due persone. Ma in realtà, proprio come la transazione Stonewall x2, si tratta di un pagamento. Questo metodo genera quindi incertezze nell'analisi della catena, o addirittura porta a false piste. Anche se un osservatore esterno riuscisse a identificare lo schema della transazione Stonewall, non disporrebbe di tutte le informazioni. Non sarà in grado di determinare quale dei due UTXO di pari importo corrisponda al pagamento. Inoltre, non saranno in grado di stabilire se i due UTXO in ingresso provengono da due persone diverse o se appartengono a un'unica persona che li ha uniti. Quest'ultimo punto è dovuto al fatto che le transazioni Stonewall x2 seguono esattamente lo stesso schema delle transazioni Stonewall. Dall'esterno e senza ulteriori informazioni di contesto, è impossibile distinguere una transazione Stonewall da una transazione Stonewall x2. Tuttavia, le prime non sono transazioni collaborative, mentre le seconde lo sono. Ciò aggiunge ulteriori dubbi su questa spesa.