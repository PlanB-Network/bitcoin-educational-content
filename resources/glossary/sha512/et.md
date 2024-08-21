---
term: SHA512
---

Lühend sõnadele "*Secure Hash Algorithm 512 bits*" ehk "Turvaline räsialgoritm 512 bitti". Tegemist on krüptograafilise räsi funktsiooniga, mis toodab 512-bitise kokkuvõtte. Selle on disaininud *National Security Agency* (NSA) 2000ndate alguses. Bitcoin'i protokollis `SHA512` funktsiooni otseselt ei kasutata, kuid see leiab rakendust rakendustasandi lapsevõtmete tuletamisel vastavalt BIP32 ja BIP39 standarditele. Nendes protsessides kasutatakse seda mitu korda `HMAC` algoritmis, samuti `PBKDF2` võtme tuletamise funktsioonis. `SHA512` funktsioon kuulub SHA 2 perekonda, nagu ka `SHA256`. Selle toimimine on väga sarnane viimasele.