---
term: TXID (TRANSAKTION TUNNISTE)

---
Yksilöllinen tunniste, joka liittyy jokaiseen Bitcoin-tapahtumaan. Se luodaan laskemalla transaktiotietojen `SHA256d`-hash. TXID toimii viitteenä tietyn transaktion löytämiseksi lohkoketjusta. Sitä käytetään myös viittaamaan UTXO:hon, joka on pohjimmiltaan edellisen transaktion TXID:n ja nimetyn ulostulon indeksin (kutsutaan myös "voutiksi") ketjutus. SegWitin jälkeisissä transaktioissa TXID ei enää ota huomioon transaktion todistajaa, mikä poistaa muokattavuuden.