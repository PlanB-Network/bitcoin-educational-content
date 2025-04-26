---
term: AZIONI

---
Nel contesto dei pool di mining, la quota è un indicatore utilizzato per quantificare il contributo di un singolo miner all'interno del pool. Questa misura serve come base per calcolare la ricompensa che il pool ridistribuisce a ciascun minatore. Ogni quota corrisponde a un hash che soddisfa un obiettivo di difficoltà inferiore a quello della rete Bitcoin.

Per spiegarlo con un'analogia, si consideri un dado a 20 facce. Su Bitcoin, supponiamo che la prova di lavoro richieda di tirare un numero inferiore a 3 per convalidare un blocco (cioè, ottenere un risultato di 1 o 2). Ora, immaginiamo che all'interno di un pool di mining, l'obiettivo di difficoltà per un'azione sia fissato a 10. Pertanto, per un singolo minatore del pool, ogni lancio di dadi che risulta in un numero inferiore a 10 conta come una quota valida. Queste azioni vengono poi trasmesse al pool dal minatore per richiedere la loro ricompensa, anche se non corrispondono a un risultato valido per un blocco di Bitcoin.

Per ogni hash calcolato, un singolo miner in un pool può incontrare tre diversi scenari:


- Se il valore dell'hash è maggiore o uguale all'obiettivo di difficoltà impostato dal pool per una quota, l'hash non è utile. Il minatore cambia quindi il proprio nonce per tentare un nuovo hash: `hash > share > block`.
- Se l'hash è inferiore all'obiettivo di difficoltà della quota, ma maggiore o uguale all'obiettivo di difficoltà di Bitcoin, allora questo hash costituisce una quota valida che, tuttavia, non è sufficiente a convalidare un blocco. Il minatore può inviare questo hash al proprio pool per richiedere la ricompensa associata alla quota: `condivisione > hash > blocco`.
- Se l'hash è inferiore all'obiettivo di difficoltà della rete Bitcoin, viene considerato sia una quota valida che un blocco valido. Il minatore trasmette questo hash al proprio pool, che si affretta a diffonderlo sulla rete Bitcoin. Anche questo hash viene conteggiato come quota valida per il minatore: `quota > blocco > hash`.

![](../../dictionnaire/assets/32.webp)

Questo sistema di quote viene utilizzato per stimare il lavoro svolto da ogni singolo minatore all'interno di un pool, senza dover ricalcolare individualmente tutti gli hash generati da un minatore, cosa che sarebbe del tutto inefficiente per il pool.

I pool minerari regolano la difficoltà delle quote per bilanciare il carico di verifica e garantire che ogni minatore, piccolo o grande che sia, invii quote ogni pochi secondi circa. Ciò consente di calcolare con precisione l'hashrate di ciascun minatore e di distribuire le ricompense in base al metodo di calcolo della compensazione scelto (PPS, PPLNS, TIDES...).

> *In francese, "azioni" può essere tradotto come "parte "*