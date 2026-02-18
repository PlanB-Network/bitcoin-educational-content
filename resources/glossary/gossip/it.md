---
term: Gossip
definition: Protocollo P2P per la diffusione di informazioni tra nodi in modo epidemico.
---

Gossip è un algoritmo distribuito peer-to-peer (P2P) per la diffusione epidemica di informazioni a tutti gli agenti della rete. Per Bitcoin, Lightning e altri sistemi distribuiti, questo protocollo consente di scambiare e sincronizzare il Global State dei nodi in pochi cicli. Ogni nodo propaga le informazioni a uno o più vicini casuali o non casuali, che a loro volta propagano le informazioni ad altri vicini e così via, fino a raggiungere uno stato di sincronizzazione globale.


In Lightning, il gossip è un protocollo di comunicazione tra nodi per condividere informazioni sullo stato attuale e sulla topologia della rete. Il protocollo di gossip consente ai nodi di conoscere lo stato dinamico dei canali di pagamento e degli altri nodi, per facilitare l'instradamento delle transazioni attraverso la rete senza richiedere connessioni dirette tra tutti i nodi.


