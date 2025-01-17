---
term: CHIAVE ESTESA

---
Una sequenza di caratteri che combina una chiave (pubblica o privata), il codice di catena associato e una serie di metadati. Una chiave estesa riunisce in un unico identificatore tutti gli elementi necessari per la derivazione delle chiavi figlio. Sono utilizzate nei portafogli deterministici e gerarchici e possono essere di due tipi: una chiave pubblica estesa (utilizzata per derivare le chiavi pubbliche dei figli) o una chiave privata estesa (utilizzata per derivare le chiavi private e pubbliche dei figli). Una chiave estesa comprende quindi diversi dati, descritti nel BIP32, nell'ordine:


- I prefissi `prv` e `pub` sono HRP (Human Readable Part) e indicano se si tratta di una chiave privata estesa (`prv`) o di una chiave pubblica estesa (`pub`). La prima lettera del prefisso indica la versione della chiave estesa: `x` per Legacy o SegWit V1 su Bitcoin, `t` per Legacy o SegWit V1 su Bitcoin Testnet, `y` per Nested SegWit su Bitcoin, `u` per Nested SegWit su Bitcoin Testnet, `z` per SegWit V0 su Bitcoin, `v` per SegWit V0 su Bitcoin Testnet.
- La profondità, che indica il numero di derivazioni dalla chiave master per raggiungere la chiave estesa;
- L'impronta digitale del genitore. Rappresenta i primi 4 byte della `HASH160` della chiave pubblica del genitore;
- L'indice. È il numero della coppia tra i suoi fratelli da cui viene ricavata la chiave estesa;
- Il codice della catena;
- Un byte di riempimento se si tratta di una chiave privata `0x00`;
- La chiave privata o pubblica;
- Un checksum. Rappresenta i primi 4 byte della `HASH256` del resto della chiave estesa.

In pratica, la chiave pubblica estesa viene utilizzata per generare indirizzi di ricezione e osservare le transazioni di un conto senza esporre le chiavi private associate. Ciò può consentire, ad esempio, la creazione di un portafoglio cosiddetto "watch-only". Tuttavia, è importante notare che la chiave pubblica estesa è un'informazione sensibile per la privacy dell'utente, poiché la sua divulgazione può consentire a terzi di tracciare le transazioni e vedere il saldo del conto associato.