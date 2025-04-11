---
term: VERIFICA SEMPLIFICATA DEI PAGAMENTI

---
Metodo che consente ai client leggeri di verificare le transazioni Bitcoin senza scaricare l'intera blockchain. Un nodo che utilizza SPV scarica solo le intestazioni dei blocchi, che sono molto più leggere dei blocchi completi. Quando deve verificare una transazione, il nodo SPV richiede una prova Merkle ai nodi completi per confermare che la transazione è inclusa in un blocco specifico. Questo approccio è efficiente per i dispositivi con risorse limitate, come gli smartphone, ma implica una dipendenza dai nodi completi, che può ridurre la sicurezza e aumentare la fiducia richiesta.

> *L'acronimo "SPV" è spesso usato per indicare questo metodo