---
term: PROBLEMA DEI GENERALI BIZANTINI

---
Il problema è stato formulato per la prima volta da Leslie Lamport, Robert Shostak e Marshall Pease nella rivista specializzata *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) nel luglio 1982. Oggi viene utilizzato per illustrare le sfide in termini di processo decisionale quando un sistema distribuito non può fidarsi di nessun attore.

In questa metafora, un gruppo di generali bizantini e i loro rispettivi eserciti sono accampati intorno a una città che vogliono attaccare o assediare. I generali sono geograficamente separati l'uno dall'altro e devono comunicare via messaggero per coordinare la loro strategia. Non importa se attaccheranno o si ritireranno, purché tutti i generali raggiungano un consenso.

Pertanto, possiamo considerare i seguenti requisiti:


- Ogni generale deve prendere una decisione: attaccare o ritirarsi (sì o no);
- Una volta presa, la decisione non può essere modificata;
- Tutti i generali devono concordare la stessa decisione ed eseguirla in modo sincrono.

Inoltre, un generale può comunicare con un altro solo attraverso messaggi trasmessi da un corriere, che possono essere ritardati, distrutti, alterati o persi. E anche se un messaggio viene consegnato con successo, uno o più generali possono decidere (per qualsiasi motivo) di tradire la fiducia stabilita e inviare un messaggio fraudolento, seminando il caos.

Applicando il dilemma al contesto della blockchain Bitcoin, ogni generale rappresenta un nodo della rete, che deve raggiungere un consenso sullo stato del sistema. In altre parole, la maggioranza dei partecipanti a una rete distribuita deve concordare ed eseguire la stessa azione per evitare un fallimento totale. L'unico modo per raggiungere il consenso in questo tipo di sistema distribuito è avere almeno 2/3 dei nodi della rete affidabili e onesti. Pertanto, se la maggioranza della rete decide di agire in modo malevolo, il sistema è vulnerabile.

> questo dilemma è talvolta chiamato anche "problema della trasmissione affidabile"