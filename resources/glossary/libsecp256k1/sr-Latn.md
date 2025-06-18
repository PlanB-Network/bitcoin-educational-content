---
term: LIBSECP256K1
---

Biblioteka C visokih performansi i visoke sigurnosti za digitalne potpise i druge kriptografske primitive na eliptičnoj krivoj `secp256k1`. Pošto ova kriva nikada nije bila široko korišćena van Bitcoin (za razliku od često preferirane krive `secp256r1`), ova biblioteka ima za cilj da bude najobuhvatnija referenca za njeno korišćenje. Razvoj libsecp256k1 je prvenstveno bio usmeren ka potrebama Bitcoin, i funkcije namenjene za druge aplikacije mogu biti manje testirane ili verifikovane. Pravilna upotreba ove biblioteke zahteva pažljivo razmatranje, kako bi se osiguralo da je pogodna za specifične svrhe aplikacija van Bitcoin.


Biblioteka libsecp256k1 nudi razne funkcije, uključujući:




- ECDSA-secp256k1 potpisivanje i verifikacija, i generisanje kriptografskih ključeva ;
- Aditivne i multiplikativne operacije na tajnim i javnim ključevima ;
- Serijalizacija i analiza tajnih ključeva, javnih ključeva i potpisa ;
- Potpisivanje javnog ključa u konstantnom vremenu i generisanje sa konstantnim pristupom memoriji;
- I mnoštvo drugih kriptografskih primitiva.