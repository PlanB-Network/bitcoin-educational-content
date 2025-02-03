---
term: REGOLE DI STANDARDIZZAZIONE

---
Le regole di standardizzazione sono adottate individualmente da ciascun nodo Bitcoin, oltre alle regole di consenso, per definire la struttura delle transazioni non confermate che accetta nella sua mempool e trasmette ai suoi pari. Queste regole sono quindi configurate ed eseguite localmente da ciascun nodo e possono variare da un nodo all'altro. Si applicano esclusivamente alle transazioni non confermate. Pertanto, un nodo accetterà una transazione che ritiene non standard solo se è già inclusa in un blocco valido.

Si noti che la maggior parte dei nodi lascia le configurazioni predefinite stabilite in Bitcoin Core, creando così un'uniformità di regole di standardizzazione in tutta la rete. Una transazione che, pur essendo conforme alle regole di consenso, non aderisce a queste regole di standardizzazione, avrà difficoltà a essere trasmessa in tutta la rete. Tuttavia, può ancora essere inclusa in un blocco valido se raggiunge un miner. In pratica, queste transazioni, definite "non standard", sono spesso trasmesse direttamente a un miner attraverso mezzi esterni alla rete peer-to-peer Bitcoin. Questo è spesso l'unico modo per confermare questo tipo di transazione.

Ad esempio, una transazione che non assegna alcuna commissione è sia valida secondo le regole del consenso che non standard, perché la politica predefinita di Bitcoin Core per il parametro `minRelayTxFee` è `0,00001` (in BTC/kB).

> *Il termine "regole di mempool" è talvolta usato anche per riferirsi alle regole di standardizzazione