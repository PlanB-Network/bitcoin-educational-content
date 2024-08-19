---
termine: TRANSAZIONE RAW
---

Una transazione Bitcoin che è stata costruita e firmata, esistente nella sua forma binaria. Una transazione raw (*raw TX*) rappresenta la rappresentazione finale di una transazione, proprio prima che venga trasmessa sulla rete. Questa transazione contiene tutte le informazioni necessarie per la sua inclusione in un blocco:
* La versione;
* Il flag;
* Gli input;
* Gli output;
* Il locktime;
* Il testimone.

Ciò che viene definito come una "*transazione raw*" rappresenta i dati grezzi che sono passati attraverso la funzione hash SHA256 due volte per generare il TXID della transazione. Questi dati vengono poi utilizzati nell'albero di Merkle del blocco per integrare la transazione nella blockchain.

> ► *Questo concetto è talvolta chiamato anche "Transazione Serializzata". In francese, questi termini potrebbero rispettivamente essere tradotti come "transaction brute" e "transaction sérialisée".*