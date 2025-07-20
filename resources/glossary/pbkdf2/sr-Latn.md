---
term: PBKDF2
---

`PBKDF2` označava *Password-Based Key Derivation Function 2*. To je metoda za kreiranje kriptografskih ključeva iz lozinke korišćenjem funkcije derivacije. Kao ulaz uzima lozinku, kriptografski salt, i iterativno primenjuje unapred određenu funkciju (često Hash funkciju kao što je `SHA256` ili `HMAC`) na ove podatke. Ovaj proces se ponavlja mnogo puta da bi se dobio kriptografski ključ.


U kontekstu Bitcoin, `PBKDF2` se koristi u kombinaciji sa funkcijom `HMAC-SHA512` za kreiranje seed determinističkog i hijerarhijskog Wallet (seed) iz fraze za oporavak od 12 ili 24 reči. Kriptografska so koja se koristi u ovom slučaju je BIP39 passphrase, a broj iteracija je `2048`.