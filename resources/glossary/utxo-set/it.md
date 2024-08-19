---
term: UTXO SET
---

Si riferisce alla collezione di tutti gli UTXO esistenti in un dato momento. In altre parole, è un lungo elenco di tutte le diverse porzioni di bitcoin in attesa di essere spesi. Se si sommano gli importi di tutti gli UTXO nel set UTXO, si ottiene la massa monetaria totale dei bitcoin in circolazione. Ogni nodo nella rete Bitcoin mantiene il proprio set UTXO in tempo reale. Lo aggiorna man mano che vengono confermati nuovi blocchi validi, con le transazioni che includono, le quali consumano alcuni UTXO dal set UTXO e ne creano di nuovi in cambio.

Questo set UTXO è mantenuto da ogni nodo per verificare rapidamente se gli UTXO spesi nelle transazioni sono effettivamente legittimi. Questo permette loro di rilevare e respingere i tentativi di doppia spesa. Il set UTXO è spesso al centro delle preoccupazioni riguardanti la decentralizzazione di Bitcoin, poiché la sua dimensione aumenta naturalmente molto rapidamente. Poiché una parte di esso deve essere mantenuta in RAM per verificare le transazioni in un tempo ragionevole, il set UTXO potrebbe gradualmente rendere troppo costoso l'operare un nodo completo. Il set UTXO ha anche un impatto significativo sull'IBD (*Initial Block Download*). Più parti del set UTXO possono essere collocate in RAM, più veloce è l'IBD. Su Bitcoin Core, il set UTXO è memorizzato nella cartella denominata `/chainstate`.

> ► *In inglese, "UTXO set" potrebbe essere tradotto come "set UTXO".*