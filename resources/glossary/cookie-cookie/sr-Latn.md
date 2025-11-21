---
term: COOKIE (.COOKIE)
---

Datoteka korišćena za RPC (*Remote Procedure Call*) autentifikaciju u Bitcoin Core. Kada bitcoind počne, generiše jedinstveni autentifikacioni kolačić i čuva ga u ovoj datoteci. Klijenti ili skripte koje žele da komuniciraju sa bitcoind preko RPC Interface mogu koristiti ovaj kolačić za sigurnu autentifikaciju. Ovaj mehanizam omogućava bezbednu komunikaciju između bitcoind i eksternih aplikacija (kao što je Wallet softver, na primer), bez potrebe za ručnim upravljanjem korisničkim imenima i lozinkama. `.cookie` datoteka se regeneriše pri svakom ponovnom pokretanju bitcoind i briše se pri gašenju.