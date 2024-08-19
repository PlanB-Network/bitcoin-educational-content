---
termine: PROBLEMA DEI GENERALI BIZANTINI
---

Il problema fu formulato per la prima volta da Leslie Lamport, Robert Shostak e Marshall Pease nella rivista specializzata *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) nel luglio 1982. Oggi è utilizzato per illustrare le sfide in termini di processo decisionale quando un sistema distribuito non può fidarsi di nessun attore.

In questa metafora, un gruppo di generali bizantini e i loro rispettivi eserciti sono accampati attorno a una città che desiderano attaccare o assediare. I generali sono separati geograficamente l'uno dall'altro e devono comunicare tramite messaggero per coordinare la loro strategia. Non importa se attaccano o si ritirano, purché tutti i generali raggiungano un consenso.

Pertanto, possiamo considerare i seguenti requisiti:
* Ogni generale deve prendere una decisione: attaccare o ritirarsi (sì o no);
* Una volta presa la decisione, questa non può essere cambiata;
* Tutti i generali devono concordare sulla stessa decisione ed eseguirla in modo sincrono.

Inoltre, un generale può comunicare con un altro solo attraverso messaggi trasmessi da un corriere, che possono essere ritardati, distrutti, alterati o persi. E anche se un messaggio viene consegnato con successo, uno o più generali possono scegliere (per qualsiasi motivo) di tradire la fiducia stabilita e inviare un messaggio fraudolento, seminando il caos.

Applicando il dilemma al contesto della blockchain di Bitcoin, ogni generale rappresenta un nodo nella rete, che necessita di raggiungere un consenso sullo stato del sistema. In altre parole, la maggioranza dei partecipanti in una rete distribuita deve concordare ed eseguire la stessa azione per evitare un fallimento totale. L'unico modo per raggiungere un consenso in questo tipo di sistema distribuito è avere almeno 2/3 dei nodi della rete affidabili e onesti. Pertanto, se la maggioranza della rete decide di agire in modo malevolo, il sistema è vulnerabile.

> ► *Questo dilemma è talvolta chiamato anche "Il Problema della Trasmissione Affidabile".*