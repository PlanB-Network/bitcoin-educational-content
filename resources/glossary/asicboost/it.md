---
term: ASICBOOST
---

ASICBOOST è un metodo di ottimizzazione algoritmica inventato nel 2016, progettato per aumentare l'efficienza del mining di Bitcoin di circa il 20% riducendo la quantità di calcoli necessari per ogni tentativo di hash dell'intestazione. Questa tecnica sfrutta una caratteristica della funzione di hash SHA256, utilizzata per il mining, che divide i dati in blocchi prima di elaborarli. ASICBOOST mantiene uno di questi blocchi invariato attraverso più tentativi di hashing, consentendo al minatore di fare solo parte del lavoro per questo blocco su diversi tentativi. La condivisione dei dati consente il riutilizzo dei risultati di calcoli precedenti, riducendo così il numero totale di calcoli necessari per trovare un hash valido.

ASICBOOST può essere utilizzato in due forme: ASICBOOST palese e ASICBOOST occulta. La forma palese di ASICBOOST è visibile a tutti, poiché coinvolge l'uso del campo `nVersion` del blocco come nonce, senza alterare il vero `Nonce`. La forma occulta cerca di nascondere queste modifiche utilizzando alberi di Merkle. Tuttavia, questo secondo metodo è diventato meno efficace dall'introduzione di SegWit a causa del secondo albero di Merkle, che aumenta il numero di calcoli necessari per utilizzarlo.

In sintesi, ASICBOOST consente ai minatori di non dover eseguire un vero e proprio SHA256 completo per tutti i tentativi di hashing, poiché parte del risultato rimane invariato, il che accelera il lavoro dei minatori.