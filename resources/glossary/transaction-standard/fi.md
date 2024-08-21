---
termi: TRANSAKTIOSTANDARDI
---

Bitcoin-transaktio, joka noudattaa konsensus-sääntöjen lisäksi myös Bitcoin Core -solmujen oletusarvoisesti asettamia standardointisääntöjä. Nämä standardointisäännöt asetetaan yksilöllisesti kunkin Bitcoin-solmun toimesta, konsensus-sääntöjen lisäksi, määrittelemään rakenteen vahvistamattomille transaktioille, joita se hyväksyy mempooliinsa ja lähettää vertaisilleen.

Nämä säännöt on siis konfiguroitu ja toteutettu paikallisesti kussakin solmussa ja ne voivat vaihdella solmusta toiseen. Ne koskevat yksinomaan vahvistamattomia transaktioita. Siksi solmu hyväksyy transaktion, jonka se katsoo epästandardiksi, vain jos se on jo sisällytetty kelvolliseen lohkoon.

On huomattava, että suurin osa solmuista jättää oletusasetukset sellaisiksi kuin ne on määritelty Bitcoin Core:ssa, luoden näin yhtenäisyyttä standardointisääntöjen yli verkossa. Transaktio, joka vaikka noudattaakin konsensus-sääntöjä, mutta ei kunnioita näitä standardointisääntöjä, kohtaa vaikeuksia levitä verkossa. Se voidaan kuitenkin sisällyttää kelvolliseen lohkoon, jos se saavuttaa mainaajan. Käytännössä nämä transaktiot, jotka luokitellaan epästandardiksi, lähetetään usein suoraan mainaajalle ulkoisin keinoin Bitcoinin vertaisverkkoon. Tämä on usein ainoa tapa vahvistaa tällainen transaktio. Esimerkiksi transaktio, joka ei kohdista mitään maksuja, on sekä kelvollinen konsensus-sääntöjen mukaan että epästandardi, koska Bitcoin Coren oletuspolitiikka `minRelayTxFee`-parametrille on `0.00001` (BTC/kB:ssa).