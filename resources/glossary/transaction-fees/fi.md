---
term: TRANSAKTIOMAKSUT

---
Transaktiomaksut ovat summa, jolla pyritään korvaamaan louhijoiden osallistuminen proof of work -mekanismiin. Nämä maksut kannustavat louhijoita sisällyttämään transaktioita luomiinsa lohkoihin. Ne syntyvät transaktion panosten ja tuotosten kokonaismäärän erotuksesta:

```text
fees = inputs - outputs
```

Ne ilmaistaan muodossa "sats/vBytes", mikä tarkoittaa, että maksut eivät riipu lähetettyjen bitcoinien määrästä vaan transaktion painosta. Transaktion lähettäjä valitsee ne vapaasti, ja ne määräävät sen nopeuden, jolla transaktio sisällytetään lohkoon, huutokauppamekanismin avulla. Oletetaan esimerkiksi, että teen transaktion, jonka panos on 100 000 satsia, lähtö 40 000 satsia ja toinen lähtö 58 500 satsia. Tuotosten yhteismäärä on 98 500 satsia. Tähän tapahtumaan kohdistetut maksut ovat 1 500 satsia. Kaivostoimittaja, joka sisällyttää tapahtumani, voi luoda 1 500 satsia Coinbase-tapahtumaansa vastineeksi 1 500 satsista, jota en saanut takaisin tuotoksissani.

Louhijat käsittelevät ensisijaisesti tapahtumia, joiden maksut ovat suurempia suhteessa niiden kokoon, mikä voi nopeuttaa vahvistusprosessia. Sitä vastoin tapahtumat, joiden maksut ovat alhaisemmat, voivat viivästyä ruuhka-aikoina. On syytä huomata, että Bitcoinin transaktiomaksut eroavat lohkotuesta, joka on lisäkannustin louhijoille. Lohkopalkkio koostuu uusista bitcoineista, jotka luodaan jokaisessa louhitussa lohkossa (lohkotuki), sekä kerätyistä transaktiomaksuista. Vaikka lohkotuki pienenee ajan myötä bitcoinien kokonaistarjonnan rajoittamisen vuoksi, transaktiomaksuilla on edelleen tärkeä rooli louhijoiden kannustamisessa osallistumaan.

Protokollatasolla mikään ei estä käyttäjiä sisällyttämästä lohkoon maksuttomia transaktioita. Todellisuudessa tämäntyyppiset maksuttomat transaktiot ovat poikkeuksellisia. Oletusarvoisesti Bitcoin-solmut eivät välitä transaktioita, joiden maksut ovat pienempiä kuin `1 sat/vBytes`. Jos joitakin maksuttomia transaktioita on läpäissyt, se johtuu siitä, että voittava louhija on integroinut ne suoraan, kulkematta solmujen verkoston kautta. Esimerkiksi seuraava transaktio ei sisällä maksuja:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

Tässä esimerkissä kyseessä oli F2Pool-kaivospoolien johtajan käynnistämä transaktio. Tavallisena käyttäjänä nykyinen alaraja on siis `1 sat/vBytes`.

On myös otettava huomioon puhdistamisen rajat. Suuren ruuhkautumisen aikana solmujen mempoolit poistavat tietyn rajan alittavat vireillä olevat tapahtumat, jotta ne noudattaisivat niille osoitettua RAM-muistirajaa. Käyttäjä voi valita tämän rajan vapaasti, mutta monet jättävät Bitcoin Coren oletusarvoksi 300 Mt. Sitä voidaan muuttaa `bitcoin.conf`-tiedostossa parametrilla `maxmempool`.

> ► *Englanniksi puhutaan "transaktiomaksuista".*