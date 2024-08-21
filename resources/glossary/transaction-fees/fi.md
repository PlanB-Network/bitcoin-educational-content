---
termi: SIIRTO MAKSUT
---

Siirtomaksut edustavat summaa, jonka tarkoituksena on korvata louhijoille heidän osallistumisestaan proof of work -mekanismiin. Nämä maksut kannustavat louhijoita sisällyttämään siirtoja luomiinsa lohkoihin. Ne syntyvät erosta siirron kokonaisinputtien ja kokonaisoutputtien määrässä:

```text
maksut = inputit - outputit
```

Ne ilmaistaan `sats/vBytes`, mikä tarkoittaa, että maksut eivät riipu lähetettyjen bitcoinien määrästä, vaan siirron painosta. Maksut valitsee vapaasti siirron lähettäjä ja ne määrittävät siirron sisällyttämisen nopeuden lohkoon huutokauppamekanismin kautta. Esimerkiksi, sanotaan että teen siirron, jossa on inputtina `100,000 sats`, outputtina `40,000 sats` ja toisena outputtina `58,500 sats`. Outputtien kokonaismäärä on `98,500 sats`. Tälle siirrolle osoitetut maksut ovat `1,500 sats`. Louhija, joka sisällyttää siirtoni, voi luoda `1,500 sats` omassa coinbase-siirrossaan vastineeksi `1,500 sats`ille, joita en saanut takaisin outputeissani.

Korkeampien maksujen siirrot, suhteessa niiden kokoon, käsitellään louhijoiden toimesta etusijalla, mikä voi nopeuttaa vahvistusprosessia. Päinvastoin, matalampien maksujen siirrot voivat viivästyä ruuhka-aikoina. On huomionarvoista, että Bitcoin-siirtomaksut ovat erillisiä lohkopalkkioista, jotka ovat lisäkannustin louhijoille. Lohkopalkkio koostuu jokaisen louhitun lohkon yhteydessä luoduista uusista bitcoineista (lohkopalkkio) sekä kerätyistä siirtomaksuista. Vaikka lohkopalkkio vähenee ajan myötä bitcoinien kokonaistarjonnan rajan vuoksi, siirtomaksut jatkavat keskeisen roolin pelaamista louhijoiden kannustamisessa.

Protokollatasolla mikään ei estä käyttäjiä sisällyttämästä maksuttomia siirtoja lohkoon. Todellisuudessa tämän tyyppinen maksuton siirto on poikkeuksellinen. Oletuksena Bitcoin-verkon solmut eivät välitä siirtoja, joiden maksut ovat alle `1 sat/vBytes`. Jos jotkin maksuttomat siirrot ovat päässeet läpi, se johtuu siitä, että ne on suoraan integroinut voittanut louhija ilman, että ne ovat kulkeneet solmujen verkon läpi. Esimerkiksi seuraava siirto ei sisällä maksuja:

```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```

Tässä erityisessä esimerkissä kyseessä oli siirto, jonka aloitti F2Pool-louhintapoolin johtaja. Tavalliselle käyttäjälle nykyinen alaraja on siis `1 sat/vBytes`.
On myös tarpeen ottaa huomioon puhdistusrajoitukset. Ruuhka-aikoina solmujen muistialtaat puhdistavat odottavat siirtonsa tietyn kynnyksen alapuolelle, kunnioittaakseen niille osoitettua RAM-muistin rajaa. Tämä raja on käyttäjän vapaasti valittavissa, mutta monet jättävät Bitcoin Coren oletusarvon 300 MB. Sitä voidaan muokata `bitcoin.conf`-tiedostossa `maxmempool`-parametrin avulla.
> ► *Englanniksi viittaamme siihen termillä "transaction fees".*