---
term: PAGAMENTI MULTIPERCORSO (MPP)
---

Termine generico per tutte le tecniche di pagamento su Lightning che consentono di suddividere una transazione in più parti e di instradarla attraverso percorsi diversi. In altre parole, ogni frazione di pagamento segue un percorso diverso del nodo. In questo modo è possibile aggirare le limitazioni di liquidità su un singolo canale del percorso.


I pagamenti multipercorso offrono anche lievi vantaggi in termini di riservatezza, poiché diventa più difficile per un osservatore collegare ogni frammento di pagamento all'intera transazione. Tuttavia, nella sua versione di base, tutti i frammenti condividono lo stesso segreto per gli HTLC, il che può rendere la transazione tracciabile se un osservatore è presente su più percorsi. Inoltre, poiché il segreto è unico per tutte le frazioni del pagamento, non è atomico. Ciò significa che alcune parti del pagamento possono essere eseguite con successo, mentre altre possono fallire. Questi inconvenienti vengono corretti con "Atomic Multi-Path Payment".