---
term: DERIVAZIONE

---
Si riferisce al processo di generazione di coppie di chiavi figlio da una coppia di chiavi genitore (chiave privata e chiave pubblica) e da un codice a catena all'interno di un portafoglio deterministico e gerarchico (HD). Questo processo consente la segmentazione dei rami e l'organizzazione di un portafoglio in diversi livelli con numerose coppie di chiavi figlio, che possono essere tutte recuperate conoscendo solo le informazioni di base per il recupero (la frase mnemonica e qualsiasi potenziale passphrase). Per derivare una chiave figlia, si utilizza la funzione `HMAC-SHA512` con il codice di catena del genitore e la concatenazione della chiave del genitore e di un indice a 32 bit. Esistono due tipi di derivazioni:


- Derivazione normale, che utilizza la chiave pubblica del genitore come base della funzione `HMAC-SHA512`;
- Derivazione rinforzata, che utilizza la chiave privata del genitore come base della funzione `HMAC-SHA512`;

Il risultato di HMAC-SHA512 viene diviso in due: i primi 256 bit diventano la chiave figlia (privata o pubblica dopo l'elaborazione tramite ECDSA) e i restanti 256 bit diventano il codice di catena figlia.