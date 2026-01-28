---
term: Offentlig nyckel
definition: Kryptografiskt element härlett från en privat nyckel, som används för att skapa Bitcoin-adresser.
---

Den publika nyckeln är ett element som används i asymmetrisk kryptografi. Den genereras från en privat nyckel med hjälp av en irreversibel matematisk funktion. På Bitcoin härleds publika nycklar från deras associerade privata nyckel genom de digitala signaturalgoritmerna för elliptisk kurva ECDSA eller Schnorr. Till skillnad från den privata nyckeln kan den publika nyckeln delas fritt utan att äventyra fondernas säkerhet. Inom Bitcoin-protokollet fungerar den publika nyckeln som grund för att skapa en Bitcoin Address, som sedan används för att skapa utgiftsvillkor på en UTXO med hjälp av en `scriptPubKey`. Publika nycklar förväxlas ofta med huvudnyckeln eller med utökade nycklar (xpub...). Dessa Elements är dock helt olika.


