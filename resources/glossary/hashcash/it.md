---
term: HASHCASH
---

HashCash è un sistema di proof-of-work progettato da Adam Back nel 1997 per combattere lo spam e gli attacchi DoS. Si basa sul principio secondo cui il mittente deve eseguire un compito computazionale (specificamente, trovare una collisione parziale su una funzione hash crittografica) per dimostrare il proprio lavoro. Questo compito è costoso in termini di tempo ed energia per il mittente, ma la verifica del risultato da parte del destinatario è rapida e semplice. Questo protocollo si è dimostrato particolarmente adatto a combattere lo spam nelle comunicazioni via email, poiché è minimamente oneroso per gli utenti legittimi mentre rappresenta un ostacolo significativo per gli spammer. Infatti, l'invio di una singola email richiede alcuni secondi di calcolo, ma replicare questa operazione milioni di volte diventa estremamente costoso in termini di energia e tempo, il che spesso annulla l'interesse economico delle campagne di spam, sia che si tratti di scopi di marketing o malevoli. Inoltre, permette di preservare l'anonimato del mittente.

HashCash è stato rapidamente adottato dai cypherpunk che cercavano di sviluppare un sistema di valuta elettronica anonimo senza intermediari. Infatti, l'innovazione di Adam Back ha introdotto per la prima volta il concetto di scarsità nel mondo digitale. Il concetto di proof of work si ritrova poi in diversi sistemi di valuta elettronica che precedono Bitcoin, inclusi:
* b-money di Wei Dai pubblicato nel 1998;
* R-POW di Hal Finney pubblicato nel 2004;
* BitGold di Nick Szabo pubblicato nel 2005.

Il principio di HashCash si trova anche all'interno del protocollo Bitcoin, dove è utilizzato come meccanismo di protezione contro gli attacchi Sybil.