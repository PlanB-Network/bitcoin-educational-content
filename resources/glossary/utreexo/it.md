---
termine: UTREEXO
---

Protocollo progettato da Tadge Dryja per compattare il set UTXO dei nodi Bitcoin utilizzando un accumulatore basato su alberi di Merkle. A differenza del classico set UTXO che richiede significativi spazi di archiviazione, Utreexo riduce drasticamente la memoria necessaria conservando solo le radici degli alberi di Merkle. Questo permette al nodo di verificare l'esistenza degli UTXO utilizzati negli input delle transazioni, senza dover mantenere l'intero set di UTXO. Utilizzando Utreexo, ogni nodo conserva solo un'impronta crittografica chiamata radice di Merkle. Quando viene effettuata una transazione, l'utente fornisce le prove di proprietà degli UTXO e i corrispondenti percorsi di Merkle. Così, il nodo può verificare le transazioni senza memorizzare l'intero set UTXO. Prendiamo un esempio con un diagramma per comprendere questo meccanismo:

![](../../dictionnaire/assets/15.png)

In questo esempio, ho intenzionalmente ridotto il set UTXO a 4 UTXO per facilitare la comprensione. Nella realtà, è importante immaginare che ci siano quasi 140 milioni di UTXO su Bitcoin al momento della scrittura di queste righe. In questo diagramma, il nodo Utreexo avrebbe bisogno di mantenere solo la Radice di Merkle nella RAM. Se riceve una transazione che spende l'UTXO n. 3 (in nero), la prova consisterebbe nei seguenti elementi:
* UTXO 3;
* HASH 4;
* HASH 1-2.

Con queste informazioni trasmesse dal mittente della transazione, il nodo Utreexo esegue le seguenti verifiche:
* Calcola l'impronta dell'UTXO 3, ottenendo HASH 3;
* Concatena HASH 3 con HASH 4;
* Calcola la loro impronta, ottenendo HASH 3-4;
* Concatena HASH 3-4 con HASH 1-2;
* Calcola la loro impronta, ottenendo la radice di Merkle.

Se la radice di Merkle ottenuta attraverso il suo processo è la stessa che ha memorizzato nella sua RAM, allora è convinto che l'UTXO n. 3 faccia effettivamente parte del set UTXO.
Questo metodo riduce i requisiti di RAM per gli operatori di nodi completi. Tuttavia, Utreexo ha delle limitazioni, inclusi un aumento delle dimensioni del blocco a causa delle prove aggiuntive e la potenziale dipendenza dei nodi Utreexo dai Bridge Nodes per ottenere le prove mancanti. I Bridge Nodes sono nodi completi tradizionali che forniscono le prove necessarie ai nodi Utreexo, consentendo così la verifica completa. Questo approccio offre un compromesso tra efficienza e decentralizzazione, rendendo la validazione delle transazioni più accessibile agli utenti con risorse limitate.