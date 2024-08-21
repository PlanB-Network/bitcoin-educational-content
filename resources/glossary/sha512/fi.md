---
termi: SHA512
---

Lyhenne sanoista "*Secure Hash Algorithm 512 bits*" eli turvallinen hajautusalgoritmi 512 bittiä. Se on kryptografinen hajautusfunktio, joka tuottaa 512-bittisen tiivisteen. Sen on suunnitellut *National Security Agency* (NSA) 2000-luvun alussa. Bitcoinin kohdalla `SHA512`-funktiota ei käytetä suoraan protokollassa, mutta sitä käytetään sovellustasolla lapsiavaimia johdettaessa, BIP32:n ja BIP39:n mukaisesti. Näissä prosesseissa sitä käytetään useita kertoja `HMAC`-algoritmissa sekä `PBKDF2`-avaimen johdatusfunktiossa. `SHA512`-funktio on osa SHA 2 -perhettä, kuten `SHA256`. Sen toiminta on hyvin samankaltaista kuin jälkimmäisen.