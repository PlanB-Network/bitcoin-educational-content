---
term: ASICBOOST

---
ASICBOOST è un metodo di ottimizzazione algoritmica inventato nel 2016, progettato per aumentare l'efficienza del mining di Bitcoin di circa il 20% riducendo la quantità di calcoli necessari per ogni tentativo di hash dell'intestazione. Questa tecnica sfrutta una caratteristica della funzione di hash SHA256, utilizzata per il mining, che divide i dati in blocchi prima di elaborarli. ASICBOOST mantiene uno di questi blocchi inalterato per più tentativi di hashing, consentendo al miner di eseguire solo una parte del lavoro per questo blocco in più tentativi. Questa condivisione dei dati consente di riutilizzare i risultati dei calcoli precedenti, riducendo così il numero totale di calcoli necessari per trovare un hash valido.

ASICBOOST può essere utilizzato in due forme: Overt ASICBOOST e Covert ASICBOOST. La forma Overt ASICBOOST è visibile a tutti, in quanto prevede l'utilizzo del campo `nVersion` del blocco come nonce, senza alterare il vero `Nonce`. La forma Covert cerca di nascondere queste modifiche utilizzando gli alberi di Merkle. Tuttavia, questo secondo metodo è diventato meno efficace dopo l'introduzione di SegWit a causa del secondo albero di Merkle, che aumenta il numero di calcoli necessari per utilizzarlo.

In sintesi, ASICBOOST consente ai minatori di non dover eseguire un vero e proprio SHA256 completo per tutti i tentativi di hashing, poiché una parte del risultato rimane invariata, velocizzando così il lavoro dei minatori.