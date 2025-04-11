---
term: DANDELION

---
Una proposta volta a migliorare la privacy del routing delle transazioni nella rete Bitcoin per contrastare la deanonimizzazione. Nel funzionamento standard di Bitcoin, le transazioni vengono immediatamente trasmesse a più nodi. Questo fenomeno può potenzialmente consentire agli osservatori di collegare le transazioni, normalmente anonime, con gli indirizzi IP. L'obiettivo di BIP156 è quello di risolvere questo problema. A tal fine, introduce una fase aggiuntiva nel processo di trasmissione per preservare l'anonimato prima della propagazione pubblica. Pertanto, Dandelion utilizza prima una fase "stem" in cui la transazione viene inviata attraverso un percorso casuale di nodi, prima di essere trasmessa all'intera rete nella fase "fluff". Il gambo e la lanugine si riferiscono al comportamento della propagazione della transazione attraverso la rete, che assomiglia alla forma di un dente di leone. Questo metodo di instradamento oscura la traccia che riporta al nodo sorgente, rendendo difficile risalire all'origine di una transazione attraverso la rete.

![](../../dictionnaire/assets/36.webp)