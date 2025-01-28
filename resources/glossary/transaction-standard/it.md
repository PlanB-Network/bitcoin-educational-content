---
term: STANDARD DI TRANSAZIONE

---
Una transazione Bitcoin che, oltre a rispettare le regole di consenso, rientra anche nelle regole di standardizzazione impostate di default sui nodi Bitcoin Core. Queste regole di standardizzazione sono imposte individualmente da ciascun nodo Bitcoin, oltre alle regole di consenso, per definire la struttura delle transazioni non confermate che accetta nella sua mempool e trasmette ai suoi pari.

Queste regole sono quindi configurate ed eseguite localmente da ciascun nodo e possono variare da un nodo all'altro. Si applicano esclusivamente alle transazioni non confermate. Pertanto, un nodo accetterà una transazione che ritiene non standard solo se è già inclusa in un blocco valido.

Si noti che la maggior parte dei nodi lascia le configurazioni predefinite stabilite in Bitcoin Core, creando così un'uniformità di regole di standardizzazione in tutta la rete. Una transazione che, pur essendo conforme alle regole di consenso, non rispetta queste regole di standardizzazione, avrà difficoltà a propagarsi attraverso la rete. Tuttavia, può ancora essere inclusa in un blocco valido se raggiunge un miner. In pratica, queste transazioni, qualificate come non standard, sono spesso trasmesse direttamente a un miner attraverso mezzi esterni alla rete peer-to-peer Bitcoin. Questo è spesso l'unico modo per confermare una transazione. Ad esempio, una transazione che non assegna commissioni è sia valida secondo le regole del consenso che non standard, perché la politica predefinita di Bitcoin Core per il parametro `minRelayTxFee` è `0,00001` (in BTC/kB).