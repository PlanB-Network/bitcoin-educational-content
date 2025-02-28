---
term: CODICE CATENA

---
Nel contesto della derivazione gerarchica deterministica (HD) dei portafogli Bitcoin, il codice di catena è un valore di sale crittografico a 256 bit utilizzato per generare chiavi figlio da una chiave genitore, secondo lo standard BIP32. Il codice di catena viene utilizzato in combinazione con la chiave genitore e l'indice del figlio per generare in modo deterministico una nuova coppia di chiavi (chiave privata e chiave pubblica) senza rivelare la chiave genitore o altre chiavi figlio derivate.

Pertanto, esiste un codice di catena unico per ogni coppia di chiavi. Il codice di catena si ottiene facendo l'hashing del seme del portafoglio e prendendo la metà destra dei bit. In questo caso, si parla di codice di catena master, associato alla chiave privata master. In alternativa, si può ottenere facendo l'hashing di una chiave genitore con il suo codice di catena genitore e un indice, conservando i bit giusti. In questo caso si parla di codice di catena figlio.

È impossibile derivare le chiavi senza conoscere il codice di catena associato a ciascuna coppia di genitori. Introduce dati pseudocasuali nel processo di derivazione per garantire che la generazione delle chiavi crittografiche rimanga imprevedibile per gli aggressori, pur essendo deterministica per il titolare del portafoglio.

> *In inglese, un "code de chaîne" è chiamato "chain code", e un "code de chaîne maître" è chiamato "master chain code "*