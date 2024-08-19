---
termine: DERIVATION
---

Si riferisce al processo di generazione di coppie di chiavi figlie da una coppia di chiavi genitore (chiave privata e chiave pubblica) e un codice catena all'interno di un portafoglio deterministico e gerarchico (HD). Questo processo consente la segmentazione di rami e l'organizzazione di un portafoglio in diversi livelli con numerose coppie di chiavi figlie, che possono tutte essere recuperate conoscendo solo le informazioni di base per il recupero (la frase mnemonica e qualsiasi eventuale passphrase). Per derivare una chiave figlia, viene utilizzata la funzione `HMAC-SHA512` con il codice catena genitore e la concatenazione della chiave genitore e di un indice a 32 bit. Esistono due tipi di derivazioni:
* Derivazione normale, che utilizza la chiave pubblica genitore come base della funzione `HMAC-SHA512`;
* Derivazione rinforzata, che utilizza la chiave privata genitore come base della funzione `HMAC-SHA512`;

Il risultato di HMAC-SHA512 è diviso in due: i primi 256 bit diventano la chiave figlia (privata o pubblica dopo l'elaborazione tramite ECDSA), e i restanti 256 bit diventano il codice catena figlio.