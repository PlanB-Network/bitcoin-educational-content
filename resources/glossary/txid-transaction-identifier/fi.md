---
termi: TXID (TRANSAKTION TUNNISTE)
---

Ainutlaatuinen tunniste, joka liittyy jokaiseen Bitcoin-siirtoon. Se luodaan laskemalla siirtotietojen `SHA256d`-hash. TXID toimii viitteenä tietyn siirron löytämiseksi lohkoketjusta. Sitä käytetään myös viittaamaan UTXO:oon, joka on käytännössä edellisen siirron TXID:n ja määrätyn lähdön indeksin yhdistelmä (jota kutsutaan myös "vout"). Post-SegWit-siirroissa TXID ei enää ota huomioon siirron todistajaa, mikä poistaa muunneltavuuden.