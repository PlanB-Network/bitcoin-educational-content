---
termine: CHIAVE ESTESA
---

Una sequenza di caratteri che combina una chiave (pubblica o privata), il suo codice catena associato e una serie di metadati. Una chiave estesa compila tutti gli elementi necessari per derivare chiavi figlie in un unico identificatore. Sono utilizzate in portafogli deterministici e gerarchici e possono essere di due tipi: una chiave pubblica estesa (utilizzata per derivare chiavi pubbliche figlie) o una chiave privata estesa (utilizzata per derivare sia chiavi private che pubbliche figlie). Una chiave estesa include quindi diversi pezzi di dati, descritti in BIP32, nell'ordine:
* Il prefisso: `prv` e `pub` sono HRP (Human Readable Part) che indicano se si tratta di una chiave privata estesa (`prv`) o di una chiave pubblica estesa (`pub`). La prima lettera del prefisso designa la versione della chiave estesa: `x` per Legacy o SegWit V1 su Bitcoin, `t` per Legacy o SegWit V1 su Bitcoin Testnet, `y` per Nested SegWit su Bitcoin, `u` per Nested SegWit su Bitcoin Testnet, `z` per SegWit V0 su Bitcoin, `v` per SegWit V0 su Bitcoin Testnet.
* La profondità, che indica il numero di derivazioni dalla chiave maestra per raggiungere la chiave estesa;
* L'impronta del genitore. Questo rappresenta i primi 4 byte dell'`HASH160` della chiave pubblica genitore;
* L'indice. Questo è il numero della coppia tra i suoi fratelli da cui è derivata la chiave estesa;
* Il codice catena;
* Un byte di padding se si tratta di una chiave privata `0x00`;
* La chiave privata o pubblica;
* Un checksum. Rappresenta i primi 4 byte dell'`HASH256` del resto della chiave estesa.

In pratica, la chiave pubblica estesa è utilizzata per generare indirizzi di ricezione e per osservare le transazioni di un account senza esporre le chiavi private associate. Questo può permettere, ad esempio, la creazione di un portafoglio cosiddetto "solo visualizzazione". Tuttavia, è importante notare che la chiave pubblica estesa è informazione sensibile per la privacy dell'utente, poiché la sua divulgazione può permettere a terze parti di tracciare transazioni e vedere il saldo dell'account associato.