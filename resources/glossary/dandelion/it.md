---
termine: DANDELION
---

Una proposta volta a migliorare la privacy del routing delle transazioni nella rete Bitcoin per contrastare la deanonimizzazione. Nel funzionamento standard di Bitcoin, le transazioni vengono immediatamente trasmesse a più nodi. Questo fenomeno può potenzialmente permettere agli osservatori di collegare le transazioni, normalmente anonime, con gli indirizzi IP. L'obiettivo del BIP156 è affrontare questa problematica. Per fare ciò, introduce una fase aggiuntiva nel processo di trasmissione per preservare l'anonimato prima della propagazione pubblica. Così, Dandelion utilizza prima una fase "stem" (stelo) dove la transazione viene inviata attraverso un percorso casuale di nodi, prima di essere trasmessa all'intera rete nella fase "fluff" (soffione). Lo stelo e il soffione sono riferimenti al comportamento della propagazione della transazione attraverso la rete, che ricorda la forma di un dente di leone. Questo metodo di routing oscura il percorso che porta al nodo sorgente, rendendo difficile tracciare una transazione attraverso la rete fino alla sua origine.

![](../../dictionnaire/assets/36.png)