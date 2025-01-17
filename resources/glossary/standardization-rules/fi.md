---
term: STANDARDISOINTISÄÄNNÖT

---
Kukin Bitcoin-solmu hyväksyy konsensussääntöjen lisäksi erikseen standardisointisäännöt, joilla määritellään niiden vahvistamattomien transaktioiden rakenne, jotka se hyväksyy mempooliinsa ja lähettää vertaisilleen. Kukin solmu siis määrittää ja toteuttaa nämä säännöt paikallisesti, ja ne voivat vaihdella solmusta toiseen. Niitä sovelletaan yksinomaan vahvistamattomiin transaktioihin. Näin ollen solmu hyväksyy epätyypilliseksi katsomansa transaktion vain, jos se sisältyy jo voimassa olevaan lohkoon.

On huomattava, että suurin osa solmuista jättää Bitcoin Core -ohjelmassa määritetyt oletuskonfiguraatiot, mikä luo yhtenäiset standardointisäännöt koko verkkoon. Transaktio, joka on konsensussääntöjen mukainen, mutta ei noudata näitä standardointisääntöjä, on vaikea lähettää verkossa. Se voidaan kuitenkin edelleen sisällyttää kelvolliseen lohkoon, jos se saavuttaa louhijan. Käytännössä nämä transaktiot, joihin viitataan nimellä "ei-standardit", lähetetään usein suoraan louhijalle Bitcoin-vertaisverkon ulkopuolella olevien ulkoisten keinojen kautta. Tämä on usein ainoa tapa vahvistaa tämäntyyppinen transaktio.

Esimerkiksi transaktio, joka ei kohdista maksuja, on sekä konsensussääntöjen mukainen että epätyypillinen, koska Bitcoin Coren oletuskäytäntö parametrille `minRelayTxFee` on `0.00001` (BTC/kB).

> ► *Termiä "mempool-säännöt" käytetään joskus myös viittaamaan standardointisääntöihin.*