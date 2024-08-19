---
termine: REGOLE DI STANDARDIZZAZIONE
---

Le regole di standardizzazione sono adottate individualmente da ciascun nodo Bitcoin, in aggiunta alle regole di consenso, per definire la struttura delle transazioni non confermate che accetta nel suo mempool e trasmette ai suoi peer. Queste regole sono quindi configurate ed eseguite localmente da ciascun nodo e possono variare da un nodo all'altro. Si applicano esclusivamente alle transazioni non confermate. Pertanto, un nodo accetterà una transazione che considera non standard solo se è già inclusa in un blocco valido.

Si nota che la maggior parte dei nodi lascia le configurazioni predefinite come stabilite in Bitcoin Core, creando così una uniformità delle regole di standardizzazione in tutta la rete. Una transazione che, sebbene conforme alle regole di consenso, non aderisce a queste regole di standardizzazione, avrà difficoltà a essere trasmessa attraverso la rete. Tuttavia, può ancora essere inclusa in un blocco valido se raggiunge un miner. Nella pratica, queste transazioni, definite "non standard", sono spesso trasmesse direttamente a un miner tramite mezzi esterni al network peer-to-peer di Bitcoin. Questo è spesso l'unico modo per confermare questo tipo di transazione.

Ad esempio, una transazione che non alloca commissioni è valida secondo le regole di consenso e non standard perché la politica predefinita di Bitcoin Core per il parametro `minRelayTxFee` è `0.00001` (in BTC/kB).

> ► *Il termine "regole del mempool" è talvolta usato anche per riferirsi alle regole di standardizzazione.*