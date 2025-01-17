---
term: NODO SPV (NODO LUCE)

---
Un nodo SPV (*Simple Payment Verification*), talvolta chiamato "nodo leggero", è un client leggero di un nodo Bitcoin che consente agli utenti di convalidare le transazioni senza dover memorizzare l'intera blockchain. Al contrario, un nodo SPV memorizza solo le intestazioni dei blocchi e ottiene informazioni su transazioni specifiche interrogando i nodi completi quando necessario. Questo principio di verifica è reso possibile dalla struttura delle transazioni nei blocchi Bitcoin, che sono organizzati all'interno di un accumulatore crittografico (Merkle Tree).

Questo approccio è vantaggioso per i dispositivi con risorse limitate, come i telefoni cellulari. Tuttavia, i nodi SPV si affidano ai nodi completi per la disponibilità delle informazioni, il che implica un ulteriore livello di fiducia e, di conseguenza, una minore sicurezza rispetto ai nodi completi. I nodi SPV non possono convalidare autonomamente le transazioni, ma possono verificare se una transazione è inclusa in un blocco consultando le prove Merkle.