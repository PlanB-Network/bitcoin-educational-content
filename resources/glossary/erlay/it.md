---
term: ERLAY
---

Protocollo di rete proposto per migliorare l'efficienza della trasmissione di transazioni non confermate tra nodi Bitcoin.


Attualmente, ogni transazione viene propagata attraverso un sistema in cui ogni nodo trasmette la transazione di cui è a conoscenza a tutti i suoi pari. Il problema è che questo porta a una grande ridondanza e all'utilizzo della larghezza di banda per i duplicati. Molte trasmissioni di transazioni non sono necessarie, poiché il destinatario è già a conoscenza di queste transazioni e ogni nodo deve essere a conoscenza di ogni transazione solo una volta. Erlay propone di limitare per default a 8 il numero di peer a cui un nodo invia direttamente le transazioni di cui è a conoscenza, e di utilizzare un processo di riconciliazione basato sulla libreria minisketch per condividere in modo più efficiente le transazioni mancanti.


Erlay ridurrebbe il consumo di banda di circa il 40%, rendendo il funzionamento del Full node più accessibile agli utenti con connessioni Internet limitate e promuovendo così una migliore decentralizzazione della rete. Questo protocollo manterrebbe inoltre quasi costante il consumo di banda all'aumentare del numero di connessioni. Ciò significa che sarebbe molto più semplice per gli operatori dei nodi accettare un numero molto elevato di connessioni dai loro pari, il che aumenterebbe la sicurezza della rete Bitcoin riducendo il rischio di partizione, sia intenzionale che accidentale. Inoltre, Erlay renderebbe più difficile determinare il nodo di origine di una transazione, aumentando così la riservatezza per gli utenti dei nodi che non operano sotto Tor.


Erlay è proposto in BIP330.