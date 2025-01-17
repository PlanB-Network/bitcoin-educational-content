---
term: BIP156

---
Proposta, nota come Dandelion, che mira a migliorare la privacy dell'instradamento delle transazioni nella rete Bitcoin per contrastare la deanonimizzazione. Nel funzionamento standard di Bitcoin, le transazioni vengono immediatamente trasmesse a più nodi. Se un osservatore è in grado di vedere ogni transazione trasmessa da ogni nodo della rete, potrebbe supporre che il primo nodo a inviare una transazione sia anche il nodo di origine di quella transazione, e quindi che provenga dall'operatore del nodo. Questo fenomeno potrebbe potenzialmente consentire agli osservatori di collegare le transazioni, normalmente anonime, con gli indirizzi IP.

L'obiettivo del BIP156 è quello di risolvere questo problema. A tal fine, introduce una fase aggiuntiva nella trasmissione per preservare l'anonimato prima della propagazione pubblica. Pertanto, Dandelion utilizza prima una fase "stem" in cui la transazione viene inviata attraverso un percorso casuale di nodi, prima di essere trasmessa all'intera rete nella fase "fluff". Il gambo e la lanugine si riferiscono al comportamento della propagazione della transazione attraverso la rete, assomigliando alla forma di un dente di leone (*a dandelion* in inglese).

Questo metodo di instradamento oscura la traccia che riporta al nodo sorgente, rendendo difficile risalire all'origine di una transazione attraverso la rete. Dandelion migliora quindi la privacy limitando la capacità degli avversari di deanonimizzare la rete. Questo metodo è ancora più efficace quando la transazione attraversa, durante la fase "stem", un nodo che cripta le proprie comunicazioni di rete, come Tor o *P2P Transport V2*. BIP156 non è ancora stato aggiunto a Bitcoin Core.

![](../../dictionnaire/assets/36.webp)