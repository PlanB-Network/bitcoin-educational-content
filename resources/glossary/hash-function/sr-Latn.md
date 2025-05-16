---
term: Hash FUNKCIJA
---

Matematička funkcija koja uzima ulaz promenljive veličine (nazvan poruka) i proizvodi izlaz fiksne veličine (nazvan Hash, heširanje, sažetak ili otisak prsta). Hash funkcije su široko korišćeni primitivni elementi u kriptografiji. One pokazuju specifična svojstva koja ih čine pogodnim za upotrebu u sigurnim kontekstima:


- Otpornost na preimage: mora biti veoma teško pronaći poruku koja proizvodi određeni Hash, tj. pronaći preimage $m$ za Hash $h$ tako da je $h = H(m)$, gde je $H$ Hash funkcija;
- Otpornost na drugi predslik: za zadatu poruku $m_1$, mora biti veoma teško pronaći drugu poruku $m_2$ (različitu od $m_1$) tako da je $H(m_1) = H(m_2)$;
- Otpornost na koliziju: mora biti veoma teško pronaći dve različite poruke $m_1$ i $m_2$ takve da je $H(m_1) = H(m_2)$;
- Otpornost na manipulaciju: male promene u ulazu moraju izazvati značajne i nepredvidive promene u izlazu.


U kontekstu Bitcoin, funkcije Hash koriste se za nekoliko svrha, uključujući mehanizam Proof-of-Work (*Proof-of-Work*), identifikatore transakcija, generisanje Address, proračune kontrolnih zbirova i kreiranje struktura podataka kao što su Merkle stabla. Na strani protokola, Bitcoin isključivo koristi funkciju `SHA256d`, takođe nazvanu `HASH256`, koja se sastoji od dvostrukog `SHA256` Hash. `HASH256` se takođe koristi u proračunu određenih kontrolnih zbirova, posebno za proširene ključeve (`xpub`, `xprv`...). Na strani Wallet, takođe se koriste sledeće:


- Jednostavan `SHA256` za kontrolne sume fraza Mnemonic;
- `SHA512` unutar algoritama `HMAC` i `PBKDF2` korišćenih u procesu derivacije determinističkih i hijerarhijskih novčanika;
- `HASH160`, koji opisuje uzastopnu upotrebu `SHA256` i `RIPEMD160`. `HASH160` se koristi u procesu generisanja adresa za primanje (osim P2PK i P2TR) i u izračunavanju otisaka prstiju roditeljskih ključeva za proširene ključeve.


> ► *Na engleskom se to naziva "Hash funkcija".*