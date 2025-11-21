---
term: P2PKH
---

P2PKH označava *Pay to Public Key Hash*. To je standardni model skripte koji se koristi za uspostavljanje uslova trošenja na UTXO. Omogućava zaključavanje bitkoina na Hash javnog ključa, odnosno na prijemnom Address. Ova skripta je povezana sa Legacy standardom i uvedena je u ranim verzijama Bitcoin od strane Satoshi Nakamoto.


Za razliku od P2PK, gde je javni ključ eksplicitno uključen u skriptu, P2PKH koristi kriptografski otisak javnog ključa. Ova skripta uključuje `RIPEMD160` Hash od `SHA256` javnog ključa i propisuje da, kako bi pristupio sredstvima, primalac mora obezbediti javni ključ koji odgovara ovom Hash, kao i važeći digitalni potpis generisan iz povezanog privatnog ključa. P2PKH adrese su kodirane koristeći `Base58Check` format, koji im daje otpornost protiv tipografskih grešaka kroz upotrebu kontrolne sume. Ove adrese uvek počinju sa brojem `1`.