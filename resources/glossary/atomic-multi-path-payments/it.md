---
term: PAGAMENTI ATOMICI MULTIPERCORSO
---

Versione migliorata di MPP (*Pagamenti multipercorso*) in cui ogni frammento di pagamento ha un segreto parziale distinto, che assicura che la transazione sia regolata atomicamente, cioè per intero o per nulla.


Gli MPP sono tecniche di pagamento su Lightning che consentono di suddividere una transazione in più parti e di instradarla attraverso percorsi diversi. In altre parole, ogni frazione di pagamento prende un percorso di nodo diverso. In questo modo si aggirano le limitazioni di liquidità su un singolo canale del percorso. Negli MPP di base, ogni frazione di pagamento condivide lo stesso segreto e quindi lo stesso Hash negli HTLC. Questo può rendere la transazione tracciabile se un osservatore è presente su più percorsi, in quanto può collegare tutti questi segreti identici tra loro. Inoltre, poiché il segreto è unico per tutte le parti del pagamento, non è atomico. Ciò significa che alcune parti del pagamento possono essere eseguite con successo, mentre altre possono fallire.


In AMP, per ogni frazione vengono utilizzati segreti parziali unici. Una volta ricevuti tutti i frammenti, questi permettono al destinatario di ricostruire il segreto generale originale e di richiedere il pagamento completo. Questo metodo rende impossibile una liquidazione parziale del pagamento, poiché il possesso di tutti i segreti parziali è necessario per sbloccare il pagamento completo. In questo modo si garantisce che il pagamento sia completamente riuscito o completamente fallito (cioè atomico). AMP migliora anche la riservatezza, poiché non ci sono più collegamenti visibili tra i diversi percorsi.


Un vantaggio degli AMP è che funzionano anche se solo il destinatario e il mittente hanno implementato questo metodo. I nodi intermediari elaborano questi pagamenti come transazioni convenzionali utilizzando gli HTLC, senza rendersi conto che stanno elaborando frazioni di un pagamento più grande.