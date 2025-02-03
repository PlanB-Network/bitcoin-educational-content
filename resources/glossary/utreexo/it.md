---
term: UTREEXO

---
Protocollo progettato da Tadge Dryja per compattare l'insieme UTXO dei nodi Bitcoin utilizzando un accumulatore basato sugli alberi di Merkle. A differenza dell'insieme UTXO classico, che richiede un notevole spazio di archiviazione, Utreexo riduce drasticamente la memoria necessaria memorizzando solo le radici dell'albero di Merkle. Ciò consente al nodo di verificare l'esistenza degli UTXO utilizzati negli input delle transazioni, senza dover conservare l'insieme completo degli UTXO. Utilizzando Utreexo, ogni nodo conserva solo un'impronta crittografica chiamata radice di Merkle. Quando viene effettuata una transazione, l'utente fornisce le prove di proprietà degli UTXO e i corrispondenti percorsi Merkle. In questo modo, il nodo può verificare le transazioni senza memorizzare l'intero set di UTXO. Facciamo un esempio con un diagramma per capire questo meccanismo:

![](../../dictionnaire/assets/15.webp)

In questo esempio, ho intenzionalmente ridotto il set di UTXO a 4 UTXO per facilitare la comprensione. In realtà, è importante immaginare che ci sono quasi 140 milioni di UTXO su Bitcoin al momento di scrivere queste righe. In questo diagramma, il nodo Utreexo avrebbe solo bisogno di mantenere la Merkle Root nella RAM. Se riceve una transazione che spende l'UTXO n. 3 (in nero), la prova consisterebbe nei seguenti elementi:


- UTXO 3;
- HASH 4;
- HASH 1-2.

Con queste informazioni trasmesse dal mittente della transazione, il nodo Utreexo esegue le seguenti verifiche:


- Calcola l'impronta di UTXO 3, che gli conferisce HASH 3;
- Concatena HASH 3 e HASH 4;
- Calcola la loro impronta, che gli conferisce HASH 3-4;
- Concatena HASH 3-4 con HASH 1-2;
- Calcola la loro impronta, che gli fornisce la radice di Merkle.

Se la radice di Merkle ottenuta attraverso il processo è la stessa della radice di Merkle memorizzata nella RAM, allora è convinto che l'UTXO n. 3 faccia effettivamente parte dell'insieme UTXO.

Questo metodo riduce i requisiti di RAM per gli operatori di nodi completi. Tuttavia, Utreexo presenta delle limitazioni, tra cui l'aumento delle dimensioni dei blocchi dovuto alle prove aggiuntive e la potenziale dipendenza dei nodi Utreexo dai Bridge Nodes per ottenere le prove mancanti. I Bridge Nodes sono nodi completi tradizionali che forniscono le prove necessarie ai nodi Utreexo, consentendo così una verifica completa. Questo approccio offre un compromesso tra efficienza e decentralizzazione, rendendo la convalida delle transazioni più accessibile agli utenti con risorse limitate.