---
term: RÄSI FUNKTSIOON
---

Matemaatiline funktsioon, mis võtab muutuva suurusega sisendi (mida nimetatakse sõnumiks) ja toodab fikseeritud suurusega väljundi (mida nimetatakse räsiks, räsimiseks, kokkuvõtteks või sõrmejäljeks). Räsi funktsioone kasutatakse laialdaselt krüptograafia põhielementidena. Neil on spetsiifilised omadused, mis muudavad need sobivaks kasutamiseks turvalistes kontekstides:
* Eelkuju vastupanu: peab olema väga raske leida sõnumit, mis toodab spetsiifilist räsi, st leida eelkuju $m$ räsi $h$ jaoks nii, et $h = H(m)$, kus $H$ on räsi funktsioon;
* Teise eelkuju vastupanu: antud sõnumi $m_1$ korral peab olema väga raske leida teist sõnumit $m_2$ (mis erineb $m_1$-st) nii, et $H(m_1) = H(m_2)$;
* Kokkupõrke vastupanu: peab olema väga raske leida kahte erinevat sõnumit $m_1$ ja $m_2$ nii, et $H(m_1) = H(m_2)$;
* Muutmiskindlus: sisendi väikesed muudatused peavad põhjustama olulisi ja ettearvamatuid muutusi väljundis.

Bitcoini kontekstis kasutatakse räsi funktsioone mitmel eesmärgil, sealhulgas töötõendusmehhanismis (*Proof-of-Work*), tehingute identifikaatorites, aadresside genereerimises, kontrollsummade arvutamises ja andmestruktuuride, nagu Merkle puud, loomises. Protokolli poolel kasutab Bitcoin eksklusiivselt `SHA256d` funktsiooni, mida nimetatakse ka `HASH256`, mis koosneb kahekordsest `SHA256` räsist. `HASH256` kasutatakse ka teatud kontrollsummade arvutamisel, eriti laiendatud võtmete puhul (`xpub`, `xprv`...). Rahakoti poolel kasutatakse ka järgmist:
* Lihtne `SHA256` mnemooniliste fraaside kontrollsummade jaoks;
* `SHA512` `HMAC` ja `PBKDF2` algoritmides, mida kasutatakse deterministlike ja hierarhiliste rahakottide tuletamise protsessis;
* `HASH160`, mis kirjeldab järjestikust kasutamist `SHA256` ja `RIPEMD160`. `HASH160` kasutatakse saateaadresside genereerimise protsessis (välja arvatud P2PK ja P2TR) ja laiendatud võtmete vanemate võtmete sõrmejälgede arvutamisel.

> ► *Inglise keeles viidatakse sellele kui "hash function".*