---
term: HASH FUNKTSIOON

---
Matemaatiline funktsioon, mis võtab muutuva suurusega sisendi (nn sõnum) ja annab fikseeritud suurusega väljundi (nn hash, hash, digesti või sõrmejälg). Hash-funktsioonid on krüptograafias laialdaselt kasutatavad algmaterjalid. Neil on spetsiifilised omadused, mis muudavad nad sobivaks kasutamiseks turvalistes kontekstides:


- Eelkujutise resistentsus: peab olema väga raske leida sõnumit, mis annab konkreetse hashi, s.t. leida eelkujutist $m$ hashi $h$ jaoks nii, et $h = H(m)$, kus $H$ on hash-funktsioon;
- Teine eelpildi vastupanu: antud sõnumi $m_1$ puhul peab olema väga raske leida teist sõnumit $m_2$ (mis erineb $m_1$-st), nii et $H(m_1) = H(m_2)$;
- Kokkupõrkekindlus: peab olema väga raske leida kahte erinevat sõnumit $m_1$ ja $m_2$ nii, et $H(m_1) = H(m_2)$;
- Manipulatsioonikindlus: väikesed muutused sisendis peavad põhjustama märkimisväärseid ja ettearvamatuid muutusi väljundis.

Bitcoini kontekstis kasutatakse hash-funktsioone mitmel eesmärgil, sealhulgas töö tõestamise mehhanismiks (*Proof-of-Work*), tehingu identifikaatoriteks, aadresside genereerimiseks, kontrollsumma arvutamiseks ja selliste andmestruktuuride nagu Merkle'i puude loomiseks. Protokolli poolel kasutab Bitcoin eranditult funktsiooni `SHA256d`, mida nimetatakse ka `HASH256`, mis koosneb kahekordsest `SHA256` hashist. `HASH256` kasutatakse ka teatavate kontrollsummade arvutamisel, eelkõige laiendatud võtmete (`xpub`, `xprv`...) puhul. Rahakoti poolel kasutatakse ka järgmist:


- Lihtne `SHA256` mnemooniliste lausete kontrollsummade jaoks;
- "SHA512" algoritmide "HMAC" ja "PBKDF2" raames, mida kasutatakse deterministlike ja hierarhiliste rahakottide tuletamisel;
- `HASH160`, mis kirjeldab `SHA256` ja `RIPEMD160` järjestikust kasutamist. `HASH160` kasutatakse vastuvõtuaadresside genereerimisel (v.a P2PK ja P2TR) ja laiendatud võtmete vanemvõtme sõrmejälgede arvutamisel.

> ► *Inglise keeles nimetatakse seda "hash-funktsiooniks"