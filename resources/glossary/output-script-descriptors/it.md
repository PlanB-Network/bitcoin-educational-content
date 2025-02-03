---
term: DESCRITTORI DI SCRIPT DI OUTPUT

---
I descrittori di script di output, o semplicemente descrittori, sono espressioni strutturate che descrivono completamente uno script di output (`scriptPubKey`) e forniscono tutte le informazioni necessarie per tracciare le transazioni verso o da uno specifico script. Questi descrittori facilitano la gestione delle chiavi nei portafogli HD attraverso una descrizione standard della struttura e dei tipi di indirizzi utilizzati.

L'interesse principale dei descrittori risiede nella loro capacità di racchiudere in un'unica stringa (oltre alla frase di recupero) tutte le informazioni essenziali per il ripristino di un portafoglio. Salvando un descrittore con le frasi mnemoniche corrispondenti, è possibile ripristinare non solo le chiavi private ma anche la struttura precisa del portafoglio e i parametri di script associati. Infatti, il recupero di un portafoglio richiede non solo la conoscenza del seme iniziale, ma anche indici specifici per la derivazione delle coppie di chiavi figlio, nonché l'`xpub` di ogni fattore nel caso di un portafoglio multisig. In precedenza, si presumeva che queste informazioni fossero implicitamente note a tutti. Tuttavia, con la diversificazione degli script e l'emergere di configurazioni più complesse, queste informazioni potrebbero diventare difficili da estrapolare, trasformando così questi dati in informazioni private e difficili da forzare. L'uso dei descrittori semplifica notevolmente il processo: è sufficiente conoscere le frasi di recupero e il descrittore corrispondente per ripristinare tutto in modo affidabile e sicuro.

Un descrittore è composto da diversi elementi:


- Funzioni di script come `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature) e `sortedmulti` (Multisignature con chiavi ordinate);
- Percorsi di derivazione, ad esempio `[d34db33f/44h/0h/0h]` che indicano un percorso derivato e una specifica impronta digitale della chiave master;
- Chiavi in vari formati, come chiavi pubbliche esadecimali o chiavi pubbliche estese (`xpub`);
- Un checksum, preceduto da un hash, per verificare l'integrità del descrittore.

Ad esempio, un descrittore per un portafoglio P2WPKH potrebbe essere simile:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

In questo descrittore, la funzione di derivazione `wpkh` indica un tipo di script Pay-to-Witness-Public-Key-Hash. È seguita dal percorso di derivazione che contiene:


- `cdeab12f`: l'impronta digitale della chiave master;
- `84h`: che indica l'uso di uno scopo BIP84, destinato agli indirizzi SegWit v0;
- `0h`: che indica che si tratta di una valuta BTC sulla mainnet;
- `0h`: si riferisce al numero di conto specifico utilizzato nel portafoglio.

Il descrittore include anche la chiave pubblica estesa utilizzata in questo portafoglio:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Poi, la notazione `/<0;1>/*` specifica che il descrittore può generare indirizzi dalla catena esterna (`0`) e interna (`1`), con un carattere jolly (`*`) che consente la derivazione sequenziale di più indirizzi in modo configurabile, in modo simile alla gestione di un "gap limit" nel software di portafoglio tradizionale.

Infine, `#jy0l7nr4` rappresenta il checksum per verificare l'integrità del descrittore.