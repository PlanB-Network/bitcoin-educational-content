---
term: NODI SEME

---
Elenco statico di nodi Bitcoin pubblici, integrato direttamente nel codice sorgente di Bitcoin Core (`bitcoin/src/chainparamsseeds.h`). Questo elenco serve come punto di connessione per i nuovi nodi Bitcoin che si uniscono alla rete, ma viene utilizzato solo se i semi DNS non forniscono una risposta entro 60 secondi dalla richiesta. In questo caso, il nuovo nodo Bitcoin si connetterà a questi nodi seed per stabilire una prima connessione alla rete e richiedere gli indirizzi IP di altri nodi. L'obiettivo finale è acquisire le informazioni necessarie per eseguire l'Initial Block Download (IBD) e sincronizzarsi con la catena che ha accumulato più lavoro. L'elenco dei nodi seme comprende quasi 1000 nodi, identificati secondo lo standard stabilito dal BIP155. I nodi seed rappresentano quindi il terzo metodo di connessione alla rete per un nodo Bitcoin, dopo l'eventuale utilizzo del file `peers.dat`, creato dal nodo stesso, e la sollecitazione dei seed DNS.

> *Nota, i nodi seme non devono essere confusi con i "semi DNS", che sono il secondo metodo per stabilire le connessioni