---
term: STONEWALL
---

Una specifica forma di transazione Bitcoin volta ad aumentare la privacy dell'utente durante una spesa, imitando un coinjoin tra due persone, senza però esserlo realmente. Infatti, questa transazione non è collaborativa. Un utente può costruirla da solo, coinvolgendo solo i propri UTXO come input. Pertanto, è possibile creare una transazione Stonewall per qualsiasi occasione, senza la necessità di sincronizzarsi con un altro utente.

Il funzionamento della transazione Stonewall è il seguente: all'input della transazione, il mittente utilizza 2 UTXO che gli appartengono. La transazione produce quindi 4 output, 2 dei quali saranno esattamente dello stesso importo. Gli altri 2 costituiranno il resto. Tra i 2 output dello stesso importo, solo uno andrà effettivamente al destinatario del pagamento.

Quindi, ci sono solo 2 ruoli in una transazione Stonewall:
* Il mittente, che effettua il pagamento effettivo;
* Il destinatario, che può essere all'oscuro della natura specifica della transazione e semplicemente attende un pagamento dal mittente.

![](../../dictionnaire/assets/33.png)
Le transazioni Stonewall sono disponibili sia sull'applicazione Samourai Wallet che sul software Sparrow Wallet.

La struttura Stonewall aggiunge molta entropia alla transazione e oscura la traccia per l'analisi della catena. Da fuori, una tale transazione può essere interpretata come un piccolo coinjoin tra due persone. Ma in realtà, proprio come la transazione Stonewall x2, è un pagamento. Questo metodo genera quindi incertezze nell'analisi della catena, o addirittura porta a false tracce. Anche se un osservatore esterno riesce a identificare il modello della transazione Stonewall, non avrà tutte le informazioni. Non sarà in grado di determinare quale dei due UTXO dello stesso importo corrisponda al pagamento. Inoltre, non sarà in grado di determinare se i due UTXO all'input provengano da due persone diverse o se appartengano a una singola persona che li ha uniti. Quest'ultimo punto è dovuto al fatto che le transazioni Stonewall x2 seguono esattamente lo stesso schema delle transazioni Stonewall. Da fuori e senza informazioni contestuali aggiuntive, è impossibile differenziare una transazione Stonewall da una transazione Stonewall x2. Tuttavia, le prime non sono transazioni collaborative, mentre le seconde lo sono. Questo aggiunge ancora più dubbio su questa spesa.