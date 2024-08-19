---
term: VERIFICA DEI PAGAMENTI SEMPLIFICATA
---

Metodo che consente ai client leggeri di verificare le transazioni Bitcoin senza scaricare l'intera blockchain. Un nodo che utilizza la SPV scarica solo gli header dei blocchi, che sono molto più leggeri dei blocchi completi. Quando necessita di verificare una transazione, il nodo SPV richiede una prova di Merkle dai nodi completi per confermare che la transazione è inclusa in un blocco specifico. Questo approccio è efficiente per dispositivi con risorse limitate, come gli smartphone, ma implica una dipendenza dai nodi completi, che può ridurre la sicurezza e aumentare la fiducia necessaria.

> ► *L'acronimo "SPV" è spesso utilizzato per riferirsi a questo metodo.*