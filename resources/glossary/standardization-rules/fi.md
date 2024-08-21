---
termi: STANDARDISOINTISÄÄNNÖT
---

Standardisointisäännöt ovat yksilöllisesti kunkin Bitcoin-solmun hyväksymiä, lisäksi konsensus-sääntöihin, määrittelemään rakenteen vahvistamattomille transaktioille, jotka se hyväksyy omaan muistialtaaseensa (mempool) ja lähettää vertaisilleen. Nämä säännöt on siis konfiguroitu ja suoritettu paikallisesti kussakin solmussa ja ne voivat vaihdella solmusta toiseen. Ne koskevat yksinomaan vahvistamattomia transaktioita. Siksi solmu hyväksyy transaktion, jonka se katsoo epästandardiksi, vain jos se on jo sisällytetty kelvolliseen lohkoon.

On huomattava, että suurin osa solmuista jättää oletuskonfiguraatiot sellaisiksi kuin ne on määritelty Bitcoin Core:ssa, luoden näin yhtenäisyyttä standardisointisääntöihin verkossa. Transaktio, joka vaikka noudattaakin konsensus-sääntöjä, mutta ei noudata näitä standardisointisääntöjä, kohtaa vaikeuksia levitettäessä verkossa. Se voi kuitenkin silti sisältyä kelvolliseen lohkoon, jos se saavuttaa mainaajan. Käytännössä nämä transaktiot, joita kutsutaan "epästandardiksi", lähetetään usein suoraan mainaajalle ulkoisin keinoin Bitcoinin vertaisverkon ulkopuolella. Tämä on usein ainoa tapa vahvistaa tämän tyyppinen transaktio.

Esimerkiksi transaktio, joka ei kohdista mitään maksuja, on sekä kelvollinen konsensus-sääntöjen mukaan että epästandardi, koska Bitcoin Core:n oletuskäytäntö `minRelayTxFee`-parametrille on `0.00001` (BTC/kB).

> ► *Termiä "mempool-säännöt" käytetään joskus viittaamaan standardisointisääntöihin.*