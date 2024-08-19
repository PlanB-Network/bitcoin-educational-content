---
term: SEED NODES
---

Elenco statico di nodi pubblici Bitcoin, integrato direttamente nel codice sorgente di Bitcoin Core (`bitcoin/src/chainparamsseeds.h`). Questo elenco funge da punti di connessione per i nuovi nodi Bitcoin che si uniscono alla rete, ma viene utilizzato solo se i DNS seeds non forniscono una risposta entro 60 secondi dalla loro richiesta. In questo caso, il nuovo nodo Bitcoin si connetterà a questi seed nodes per stabilire una prima connessione alla rete e richiedere gli indirizzi IP di altri nodi. L'obiettivo finale è acquisire le informazioni necessarie per eseguire l'Initial Block Download (IBD) e sincronizzarsi con la catena che ha accumulato più lavoro. L'elenco dei seed nodes include quasi 1000 nodi, identificati in conformità con lo standard stabilito dal BIP155. Pertanto, i seed nodes rappresentano il terzo metodo di connessione alla rete per un nodo Bitcoin, dopo il possibile utilizzo del file `peers.dat`, creato dal nodo stesso, e la sollecitazione dei DNS seeds.

> ► *Nota, i seed nodes non devono essere confusi con i "DNS seeds", che rappresentano il secondo metodo di stabilire connessioni.*