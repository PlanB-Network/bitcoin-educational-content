---
term: SHA512

---
Lühend "*Secure Hash Algorithm 512 bits*". See on krüptograafiline hash-funktsioon, mis toodab 512-bitise digesti. Selle töötas välja *National Security Agency* (NSA) 2000. aastate alguses. Bitcoini puhul ei kasutata "SHA512" funktsiooni otseselt protokollis, kuid seda kasutatakse rakenduse tasandil lapsvõtmete tuletamise kontekstis vastavalt BIP32 ja BIP39. Nendes protsessides kasutatakse seda mitu korda `HMAC` algoritmis ja `PBKDF2` võtme tuletamise funktsioonis. Funktsioon `SHA512` on osa SHA 2 perekonnast, nagu ka `SHA256`. Selle toimimine on viimasega väga sarnane.