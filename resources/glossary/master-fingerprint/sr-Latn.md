---
term: MASTER FINGERPRINT
---

Otisak od 4 bajta (32-bita) glavnog privatnog ključa u Hijerarhijski Determinističkom (HD) Wallet. Dobija se izračunavanjem `SHA256` Hash glavnog privatnog ključa, nakon čega sledi `RIPEMD160` Hash, proces poznat kao `HASH160` na Bitcoin. Glavni Otisak se koristi za identifikaciju HD Wallet, nezavisno od putanja derivacije, ali uzimajući u obzir prisustvo ili odsustvo passphrase. To je sažeta informacija koja omogućava referenciranje porekla skupa ključeva, bez otkrivanja osetljivih informacija o Wallet.