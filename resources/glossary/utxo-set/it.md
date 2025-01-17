---
term: UTXO SET

---
Si riferisce alla raccolta di tutti gli UTXO esistenti in un dato momento. In altre parole, è un grande elenco di tutti i diversi pezzi di bitcoin in attesa di essere spesi. Se si sommano gli importi di tutti gli UTXO nel set UTXO, si ottiene la massa monetaria totale dei bitcoin in circolazione. Ogni nodo della rete Bitcoin mantiene il proprio set UTXO in tempo reale. Lo aggiorna man mano che vengono confermati nuovi blocchi validi, con le transazioni in essi incluse, che consumano alcuni UTXO dall'insieme UTXO e ne creano di nuovi in cambio.

Questo set di UTXO viene conservato da ogni nodo per verificare rapidamente se gli UTXO spesi nelle transazioni sono effettivamente legittimi. Ciò consente di individuare e respingere i tentativi di doppio pagamento. L'insieme di UTXO è spesso al centro delle preoccupazioni sulla decentralizzazione di Bitcoin, poiché le sue dimensioni aumentano naturalmente molto rapidamente. Poiché una parte di esso deve essere conservata nella RAM per verificare le transazioni in un tempo ragionevole, il set UTXO potrebbe gradualmente rendere troppo costoso il funzionamento di un nodo completo. L'insieme UTXO ha anche un impatto significativo sull'IBD (*Initial Block Download*). Più il set UTXO può essere collocato nella RAM, più l'IBD è veloce. Su Bitcoin Core, il set UTXO è memorizzato nella cartella denominata `/chainstate`.

> *In inglese, "UTXO set" potrebbe essere tradotto come "set UTXO".*