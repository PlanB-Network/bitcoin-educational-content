---
term: Anchors.dat

definition: Un file Bitcoin Core che memorizza gli indirizzi IP dei nodi a cui il client era collegato prima dell'arresto, per facilitare la riconnessione al riavvio.
---
File utilizzato nel client Bitcoin Core per memorizzare gli indirizzi IP dei nodi in uscita a cui un client era connesso prima di essere spento. Anchors.dat viene quindi creato ogni volta che il nodo viene fermato e cancellato quando viene riavviato. I nodi i cui indirizzi IP sono contenuti in questo file vengono utilizzati per stabilire rapidamente le connessioni quando il nodo viene riavviato.