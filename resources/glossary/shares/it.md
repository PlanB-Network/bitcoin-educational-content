---
termine: SHARES
---

Nel contesto delle mining pool, una "share" (quota) è un indicatore utilizzato per quantificare il contributo di un singolo minatore all'interno della pool. Questa misura serve come base per calcolare la ricompensa che la pool ridistribuisce a ciascun minatore. Ogni share corrisponde a un hash che soddisfa un target di difficoltà inferiore a quello della rete Bitcoin.

Per spiegare con un'analogia, considera un dado a 20 facce. Su Bitcoin, supponiamo che la prova di lavoro richieda di ottenere un numero inferiore a 3 per validare un blocco (cioè, ottenere un risultato di 1 o 2). Ora, immagina che all'interno di una mining pool, il target di difficoltà per una share sia impostato a 10. Così, per un singolo minatore nella pool, ogni lancio di dado che risulta in un numero inferiore a 10 conta come una share valida. Queste share vengono poi trasmesse alla pool dal minatore, per rivendicare la loro ricompensa, anche se non corrispondono a un risultato valido per un blocco su Bitcoin.

Per ogni hash calcolato, un singolo minatore in una pool può incontrare tre diversi scenari:
* Se il valore dell'hash è maggiore o uguale al target di difficoltà impostato dalla pool per una share, allora questo hash non è di alcuna utilità. Il minatore cambia quindi il proprio nonce per tentare un nuovo hash: `hash > share > blocco`.
* Se l'hash è inferiore al target di difficoltà della share, ma maggiore o uguale al target di difficoltà di Bitcoin, allora questo hash costituisce una share valida che, tuttavia, non è sufficiente a validare un blocco. Il minatore può inviare questo hash alla sua pool per rivendicare la ricompensa associata alla share: `share > hash > blocco`.
* Se l'hash è inferiore al target di difficoltà della rete Bitcoin, è considerato sia una share valida che un blocco valido. Il minatore trasmette questo hash alla sua pool, che si affretta a trasmetterlo sulla rete Bitcoin. Questo hash è anche conteggiato come una share valida per il minatore: `share > blocco > hash`.

![](../../dictionnaire/assets/32.png)

Questo sistema di share è utilizzato per stimare il lavoro svolto da ciascun minatore individuale all'interno di una pool, senza dover ricalcolare individualmente tutti gli hash generati da un minatore, il che sarebbe completamente inefficiente per la pool.

Le mining pool aggiustano la difficoltà delle share per bilanciare il carico di verifica e assicurare che ogni minatore, piccolo o grande che sia, invii share approssimativamente ogni pochi secondi. Questo permette un calcolo accurato del hashrate di ciascun minatore e la distribuzione delle ricompense secondo il metodo scelto per il calcolo della compensazione (PPS, PPLNS, TIDES...).

> ► *In francese, "shares" può essere tradotto come "part".*