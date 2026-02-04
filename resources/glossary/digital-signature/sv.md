---
term: Digital signatur
definition: Kryptografiskt bevis på innehav av en privat nyckel som gör det möjligt att signera och validera Bitcoin-transaktioner.
---

Kryptografiskt bevis som visar att man innehar en specifik privat nyckel, associerad med en unik publik nyckel, utan att behöva avslöja den. I Bitcoin konstrueras det med hjälp av den privata nyckeln och Hash för en transaktion. Det intygar Ownership för bitcoins i fråga och gör det möjligt att uppfylla ett skript som låser upp en UTXO. Den genereras genom en digital signaturalgoritm med elliptisk kurva, t.ex. ECDSA eller Schnorr-protokollet.