---
term: SCOPERTA DEL PEER

---
Il processo con cui i nodi della rete Bitcoin si connettono ad altri nodi per ottenere informazioni. Quando un nodo Bitcoin viene lanciato per la prima volta, non ha informazioni sugli altri nodi della rete. Tuttavia, deve stabilire connessioni per sincronizzarsi con la blockchain che ha il maggior numero di lavori accumulati. Per scoprire questi peer vengono utilizzati diversi meccanismi, in ordine di priorità:


- Il nodo inizia consultando il suo file locale `peers.dat`, che memorizza le informazioni sui nodi con cui ha interagito in precedenza. Se il nodo è nuovo, questo file sarà vuoto e il processo passerà alla fase successiva;
- In assenza di informazioni nel file `peers.dat` (cosa normale per un nodo appena lanciato), il nodo esegue query DNS ai semi DNS. Questi server forniscono un elenco di indirizzi IP di nodi presumibilmente attivi per stabilire connessioni. Gli indirizzi dei DNS seed sono codificati nel codice di Bitcoin Core. Questa fase è solitamente sufficiente per completare la scoperta dei peer;
- Se i semi DNS non rispondono entro 60 secondi, il nodo può rivolgersi ai nodi seme. Si tratta di nodi Bitcoin pubblici elencati in un elenco statico di quasi mille voci integrato direttamente nel codice sorgente di Bitcoin Core. Il nuovo nodo utilizzerà questo elenco per stabilire una prima connessione alla rete e ottenere gli indirizzi IP degli altri nodi;
- Nel caso molto improbabile in cui tutti i metodi precedenti falliscano, l'operatore del nodo ha sempre la possibilità di aggiungere manualmente gli indirizzi IP dei nodi per stabilire una prima connessione.