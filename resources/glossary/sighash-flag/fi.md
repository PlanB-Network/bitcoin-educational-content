---
term: SIGHASH FLAG

---
Bitcoin-tapahtuman parametri, joka määrittää, mitkä tapahtuman osat (tulot ja lähdöt) kuuluvat siihen liittyvän allekirjoituksen piiriin, jolloin niistä tulee muuttumattomia. SigHash Flag on tavu, joka lisätään kunkin syötteen digitaaliseen allekirjoitukseen. Näin ollen SigHash Flagin valinta vaikuttaa suoraan siihen, mitkä transaktion osat jäädytetään allekirjoituksella ja mitkä voidaan vielä muuttaa jälkikäteen. Tällä mekanismilla varmistetaan, että allekirjoitukset sitovat transaktiotiedot täsmällisesti ja turvallisesti allekirjoittajan aikomuksen mukaisesti. SigHash-lipukkeita on kolme pääasiallista:


- `SIGHASH_ALL` (`0x01`): Allekirjoitus koskee kaikkia tapahtuman tuloja ja lähtöjä, jolloin ne lukittuvat kokonaan;
- `SIGHASH_NONE` (`0x02`): Signatuuri koskee kaikkia tuloja, mutta ei yhtään lähtöä, jolloin lähtöjä voidaan muuttaa allekirjoituksen jälkeen;
- `SIGHASH_SINGLE` (`0x03`): Allekirjoitus kattaa kaikki syötteet ja vain yhden lähdön, joka vastaa allekirjoitetun syötteen indeksiä.

Näiden kolmen SigHash-lipputyypin lisäksi modifier `SIGHASH_ANYONECANPAY` (`0x80`) voidaan yhdistää kaikkiin edellisiin tyyppeihin. Kun tätä modifiointia käytetään, vain osa syötteistä allekirjoitetaan, ja muut osat jätetään avoimiksi muutoksille. Seuraavassa on olemassa olevia yhdistelmiä, joissa on muunnin:


- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Allekirjoitus koskee yhtä tuloa ja kattaa kaikki tapahtuman lähdöt;
- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Allekirjoitus kattaa yhden syötteen, mutta ei sitoudu mihinkään tulosteeseen;
- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Allekirjoitus koskee yhtä tuloa ja vain tulosta, jolla on sama indeksi kuin tällä tulolla.

> ► *Signature Hash Types on joskus käytetty synonyymi "Signature Hash Types".*