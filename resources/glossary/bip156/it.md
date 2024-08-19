---
termine: BIP156
---

Proposta, nota come Dandelion, che mira a migliorare la privacy del routing delle transazioni nella rete Bitcoin per contrastare la deanonimizzazione. Nel funzionamento standard di Bitcoin, le transazioni vengono immediatamente trasmesse a più nodi. Se un osservatore è in grado di vedere ogni transazione inoltrata da ciascun nodo sulla rete, potrebbe presumere che il primo nodo a inviare una transazione sia anche il nodo di origine di quella transazione e, quindi, che provenga dall'operatore del nodo. Questo fenomeno potrebbe potenzialmente permettere agli osservatori di collegare le transazioni, normalmente anonime, con gli indirizzi IP.

L'obiettivo del BIP156 è affrontare questa problematica. Per fare ciò, introduce una fase aggiuntiva nella trasmissione per preservare l'anonimato prima della propagazione pubblica. Così, Dandelion utilizza prima una fase "stem" (stelo) dove la transazione viene inviata attraverso un percorso casuale di nodi, prima di essere trasmessa all'intera rete nella fase "fluff" (soffione). Stem e fluff sono riferimenti al comportamento della propagazione della transazione attraverso la rete, che ricorda la forma di un dente di leone (*a dandelion* in inglese).

Questo metodo di routing oscura il percorso di ritorno al nodo sorgente, rendendo difficile tracciare una transazione attraverso la rete fino alla sua origine. Dandelion migliora quindi la privacy limitando la capacità degli avversari di deanonimizzare la rete. Questo metodo è ancora più efficace quando la transazione attraversa durante la fase "stem" un nodo che cripta le sue comunicazioni di rete, come con Tor o *P2P Transport V2*. BIP156 non è ancora stato aggiunto a Bitcoin Core.

![](../../dictionnaire/assets/36.png)