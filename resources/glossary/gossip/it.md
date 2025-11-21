---
term: GOSSIP
---

Gossip è un algoritmo distribuito peer-to-peer (P2P) per la diffusione epidemica di informazioni a tutti gli agenti della rete. Per Bitcoin, Lightning e altri sistemi distribuiti, questo protocollo consente di scambiare e sincronizzare il Global State dei nodi in pochi cicli. Ogni nodo propaga le informazioni a uno o più vicini casuali o non casuali, che a loro volta propagano le informazioni ad altri vicini e così via, fino a raggiungere uno stato di sincronizzazione globale.


In Lightning, il gossip è un protocollo di comunicazione tra nodi per condividere informazioni sullo stato attuale e sulla topologia della rete. Il protocollo di gossip consente ai nodi di conoscere lo stato dinamico dei canali di pagamento e degli altri nodi, per facilitare l'instradamento delle transazioni attraverso la rete senza richiedere connessioni dirette tra tutti i nodi.


> *In francese, "protocollo di gossip" potrebbe essere tradotto come "protocole de bavardage". Fonte : https://dl.acm.org/doi/pdf/10.1145/41840.41841.*