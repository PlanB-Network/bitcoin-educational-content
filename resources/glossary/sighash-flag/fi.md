---
termi: SIGHASH FLAG
---

Parametri Bitcoin-siirrossa, joka määrittää, mitkä siirron osat (syötteet ja tulosteet) kattaa liitetty allekirjoitus, tehden niistä muuttumattomia. SigHash Flag on tavu, joka lisätään kunkin syötteen digitaaliseen allekirjoitukseen. Näin ollen SigHash Flagin valinta vaikuttaa suoraan siihen, mitkä siirron osat jäädytetään allekirjoituksella ja mitkä voidaan vielä muokata jälkikäteen. Tämä mekanismi varmistaa, että allekirjoitukset sitoutuvat tarkasti ja turvallisesti siirtotietoihin allekirjoittajan aikomuksen mukaisesti. SigHash Flag -tyyppejä on kolme pääasiallista:

- `SIGHASH_ALL` (`0x01`): Allekirjoitus kattaa kaikki siirron syötteet ja tulosteet, lukiten ne kokonaan;

- `SIGHASH_NONE` (`0x02`): Allekirjoitus kattaa kaikki syötteet, mutta ei yhtään tulostetta, mahdollistaen tulosteiden muokkaamisen allekirjoituksen jälkeen;

- `SIGHASH_SINGLE` (`0x03`): Allekirjoitus kattaa kaikki syötteet ja vain yhden tulosteen, joka vastaa allekirjoitetun syötteen indeksiä.

Näiden kolmen SigHash Flag -tyypin lisäksi, modifioija `SIGHASH_ANYONECANPAY` (`0x80`) voidaan yhdistää kuhunkin edellä mainittuun tyyppiin. Kun tätä modifioijaa käytetään, vain osa syötteistä allekirjoitetaan, jättäen muut muokattaviksi. Tässä ovat olemassa olevat yhdistelmät modifioijan kanssa:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Allekirjoitus kattaa yhden syötteen samalla kattaen kaikki siirron tulosteet;

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Allekirjoitus kattaa yhden syötteen, sitoutumatta mihinkään tulosteeseen;

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Allekirjoitus kattaa yhden syötteen ja vain tulosteen, jolla on sama indeksi kuin tällä syötteellä.

> ► *Synonyymi, jota joskus käytetään "SigHash" termille, on "Signature Hash Types".*