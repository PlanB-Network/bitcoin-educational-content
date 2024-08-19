---
term: ATOMIC SWAP
---

Tecnologia che consente lo scambio diretto di criptovalute tra due parti, senza la necessità di fiducia e senza richiedere un intermediario. Questi scambi sono chiamati "atomici" perché possono risultare solo in due esiti:
* O lo scambio ha successo, e entrambi i partecipanti hanno effettivamente scambiato le loro criptovalute;
* Oppure lo scambio fallisce, e entrambi i partecipanti si ritirano con le loro criptovalute originali.

Gli Atomic Swap possono essere eseguiti sia con la stessa criptovaluta, nel qual caso vengono anche definiti come "*coinswap*", sia tra criptovalute diverse. Storicamente, si sono affidati ai "Hash Time-Locked Contracts" (HTLC), un sistema di blocco temporale che garantisce il completamento o l'annullamento totale dello scambio, preservando così l'integrità dei fondi delle parti coinvolte. Questo metodo richiedeva protocolli in grado di gestire sia script che timelocks. Tuttavia, negli ultimi anni, la tendenza si è spostata verso l'uso delle *Adaptor Signatures*. Questo secondo approccio ha il vantaggio di eliminare la necessità di script, riducendo così i costi operativi. Il suo altro grande beneficio è che non richiede l'uso di hashing identico per entrambe le parti della transazione, il che aiuta a evitare di rivelare un collegamento tra di esse.