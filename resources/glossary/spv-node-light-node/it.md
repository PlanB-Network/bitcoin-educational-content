---
term: SPV NODE (LIGHT NODE)
---

Un nodo SPV (*Simple Payment Verification*, Verifica Semplice dei Pagamenti), talvolta chiamato "nodo leggero", è un client leggero di un nodo Bitcoin che permette agli utenti di validare le transazioni senza dover memorizzare l'intera blockchain. Invece, un nodo SPV memorizza solo gli header dei blocchi e ottiene informazioni su transazioni specifiche interrogando i nodi completi quando necessario. Questo principio di verifica è reso possibile dalla struttura delle transazioni nei blocchi Bitcoin, che sono organizzate all'interno di un accumulatore crittografico (Albero di Merkle).

Questo approccio è vantaggioso per dispositivi con risorse limitate, come i telefoni cellulari. Tuttavia, i nodi SPV dipendono dai nodi completi per la disponibilità delle informazioni, il che implica un livello aggiuntivo di fiducia e, di conseguenza, meno sicurezza rispetto ai nodi completi. I nodi SPV non possono validare autonomamente le transazioni, ma possono verificare se una transazione è inclusa in un blocco consultando le prove di Merkle.