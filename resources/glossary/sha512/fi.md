---
term: SHA512

---
Lyhenne sanoista "*Secure Hash Algorithm 512 bits*". Se on kryptografinen hash-funktio, joka tuottaa 512-bittisen digestin. Sen suunnitteli *National Security Agency* (NSA) 2000-luvun alussa. Bitcoinissa `SHA512`-funktiota ei käytetä suoraan protokollassa, mutta sitä käytetään sovellustason lapsiavainten johtamisen yhteydessä BIP32:n ja BIP39:n mukaisesti. Näissä prosesseissa sitä käytetään useita kertoja `HMAC`-algoritmissa sekä `PBKDF2`-avainten johdannaisfunktiossa. `SHA512`-funktio kuuluu SHA 2 -perheeseen, kuten `SHA256`. Sen toiminta on hyvin samankaltainen kuin jälkimmäisen.