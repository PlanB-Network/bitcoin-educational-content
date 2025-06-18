---
term: P2SH
---

P2SH označava *Pay to Script Hash*. To je standardni model skripte koji se koristi za uspostavljanje uslova trošenja na UTXO. Za razliku od P2PK i P2PKH skripti, gde su uslovi trošenja unapred definisani, P2SH omogućava integraciju proizvoljnih uslova trošenja i dodatnih funkcionalnosti unutar transakcione skripte.


Tehnički, u P2SH transakciji, `scriptPubKey` sadrži kriptografski Hash od `redeemscript`, umesto eksplicitnih uslova trošenja. Ovaj Hash se dobija korišćenjem `SHA256` Hash. Kada se šalju bitkoini na P2SH Address, osnovni `redeemscript` nije otkriven. Samo njegov Hash je uključen u transakciju. P2SH adrese su kodirane u `Base58Check` i počinju brojem `3`. Kada primalac želi da potroši primljene bitkoine, mora da obezbedi `redeemscript` koji odgovara Hash prisutnom u `scriptPubKey`, zajedno sa potrebnim podacima da zadovolji uslove ovog `redeemscript`. Na primer, u P2SH skripti sa više potpisa, skripta može zahtevati potpise od više privatnih ključeva.


Korišćenje P2SH nudi veću fleksibilnost, jer omogućava izradu proizvoljnih skripti bez potrebe da pošiljalac zna detalje. P2SH je uveden 2012. godine sa BIP16.