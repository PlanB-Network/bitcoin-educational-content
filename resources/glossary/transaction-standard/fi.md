---
term: TRANSAKTIOSTANDARDI

---
Bitcoin-tapahtuma, joka konsensussääntöjen noudattamisen lisäksi kuuluu myös Bitcoin Core -solmujen oletusarvoisesti asettamiin standardointisääntöihin. Kukin Bitcoin-solmu asettaa nämä standardointisäännöt erikseen konsensussääntöjen lisäksi määrittelemään niiden vahvistamattomien transaktioiden rakenteen, jotka se hyväksyy mempoolissaan ja lähettää vertaisryhmilleen.

Kukin solmu määrittää ja toteuttaa nämä säännöt paikallisesti, ja ne voivat vaihdella solmusta toiseen. Niitä sovelletaan yksinomaan vahvistamattomiin tapahtumiin. Sen vuoksi solmu hyväksyy epätyypilliseksi katsomansa transaktion vain, jos se on jo sisällytetty kelvolliseen lohkoon.

On huomattava, että suurin osa solmuista jättää Bitcoin Core -ohjelmassa määritetyt oletuskonfiguraatiot, mikä luo yhtenäiset standardointisäännöt koko verkkoon. Transaktiolla, joka on konsensussääntöjen mukainen, mutta ei noudata näitä standardointisääntöjä, on vaikeuksia levitä verkossa. Se voidaan kuitenkin edelleen sisällyttää kelvolliseen lohkoon, jos se saavuttaa louhijan. Käytännössä nämä ei-standardeiksi luokitellut transaktiot välitetään usein suoraan louhijalle Bitcoin-vertaisverkon ulkopuolisten keinojen kautta. Tämä on usein ainoa tapa vahvistaa tällainen transaktio. Esimerkiksi transaktio, jossa ei jaeta maksuja, on sekä konsensussääntöjen mukaan pätevä että epätyypillinen, koska Bitcoin Coren oletuskäytäntö `minRelayTxFee`-parametrille on `0.00001` (BTC/kB).