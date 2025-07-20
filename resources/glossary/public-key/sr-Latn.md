---
term: JAVNI KLJUČ
---

Javni ključ je element koji se koristi u asimetričnoj kriptografiji. Generiše se iz privatnog ključa korišćenjem ireverzibilne matematičke funkcije. Na Bitcoin, javni ključevi se izvode iz njihovog povezanog privatnog ključa putem algoritama digitalnog potpisa eliptičke krive ECDSA ili Schnorr. Za razliku od privatnog ključa, javni ključ se može slobodno deliti bez ugrožavanja sigurnosti sredstava. Unutar Bitcoin protokola, javni ključ služi kao osnova za kreiranje Bitcoin Address, koji se zatim koristi za kreiranje uslova trošenja na UTXO korišćenjem `scriptPubKey`. Javni ključevi se često mešaju sa master ključem ili sa proširenim ključevima (xpub...). Međutim, ovi Elements su prilično različiti.


> ► *Na engleskom, javni ključ se zove "public key." Ovaj termin se ponekad skraćuje kao "pubkey," ili "PK."*