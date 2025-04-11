---
term: TRANSAZIONE GREZZA

---
Una transazione Bitcoin costruita e firmata, esistente nella sua forma binaria. Una transazione grezza (*raw TX*) è la rappresentazione finale di una transazione, appena prima della sua trasmissione in rete. Questa transazione contiene tutte le informazioni necessarie per la sua inclusione in un blocco:


- La versione;
- La bandiera;
- Gli ingressi;
- Le uscite;
- Il tempo di blocco;
- Il testimone.

La cosiddetta "transazione *raw*" rappresenta i dati grezzi che vengono passati due volte attraverso la funzione di hash SHA256 per generare il TXID della transazione. Questi dati vengono poi utilizzati nell'albero di Merkle del blocco per integrare la transazione nella blockchain.

> questo concetto viene talvolta chiamato anche "transazione serializzata". In francese, questi termini potrebbero essere tradotti rispettivamente come "transazione bruta" e "transazione sérialisée "*