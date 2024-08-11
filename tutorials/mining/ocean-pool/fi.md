---
name: Ocean Mining

description: Johdanto valtamerten kaivostoimintaan
---

![signup](assets/cover.webp)

**Toukokuu 2024**

Ocean Mining on hieman erilainen kaivosallas. Täällä ei vaadita tilejä, sähköpostiosoitteita eikä salasanoja. Aivan kuten Bitcoinissa, kaikki on läpinäkyvää, pseudonyymiä, ja osallistujat voivat valita neljästä eri lohkomallista.

### Korvausjärjestelmä

Oceanin korvausjärjestelmää kutsutaan nimellä TIDES, "Transparent Index of Distinct Extended Shares". Tämä järjestelmä kirjaa kaivostyöntekijöiden, tunnettu nimellä "osuudet", tekemän työn. Allas laskee kunkin osallistujan "osuuksien" prosenttiosuuden, lisää sitten heidän Bitcoin-osoitteensa allaslohkon malliin tämän prosenttiosuuden lohkopalkkion saajaksi.

Lohkomallia päivitetään noin joka 10. sekunti ottaen huomioon tuottoisimmat uudet siirrot ja tarvittaessa muuttaen lohkopalkkion jakautumista.

![signup](assets/rem.webp)

Ei ole väliä, ovatko koneesi yhdistettyinä vai ei sillä hetkellä, kun allas louhii uuden lohkon. Aiemmin lähetetty työ säilytetään seuraavien kahdeksan löydetyn lohkon ajan.

Työn säilyttäminen kahdeksan lohkon ajan sen sijaan, että laskurit nollattaisiin jokaisen uuden louhitun lohkon yhteydessä, tarkoittaa, että korvauksesi on 100% vasta, kun allas on löytänyt kahdeksan lohkoa sen jälkeen, kun aloitit osallistumisen. Tämä tarkoittaa myös, että jatkat korvauksen saamista kahdeksan lohkon ajan, jos lopetat osallistumisen altaaseen.

Tämä mekanismi tasoittaa korvausta ja estää "altaan hyppelyn", joka tarkoittaa säännöllistä altaiden vaihtamista sen mukaan, mikä allas todennäköisimmin löytää seuraavan lohkon.

### Nostot

Ocean Miningin toiminta mahdollistaa sen, että sen osallistujat voivat saada "puhtaita" bitcoineja, tarkoittaen bitcoineja, jotka on suoraan myönnetty lohkopalkkiosta.

Toisin kuin useimmissa muissa altaissa, Ocean ei vastaanota vastalouhittuja bitcoineja; osallistujien osoitteet integroidaan suoraan lohkomalliin.

Toistaiseksi puhtaiden bitcoinien todellinen hyödyntäminen vaatii vähintään 1,048,576 satsia. Jokaisen altaan louhimalla lohkolla, "osuuksiesi" on oikeutettava sinut saamaan enemmän kuin 1,048,576 satsia, jotta ne maksetaan sinulle suoraan lohkopalkkiosta.
Muussa tapauksessa satsisi säilytetään Oceanissa, kunnes kokonaispalkkiosi ylittää tämän summan.

Kaikki Oceanin väliaikaisesti säilyttämät bitcoinit ovat tässä osoitteessa: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, kaikki on todennettavissa TimeChainissa.](https://mempool.space/address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)
On myös mahdollista nostaa satsisi Lightningin kautta käyttäen BOLT12. Näemme, miten tämä asetetaan.

### Altaan Maksut

Maksut vaihtelevat 0%:sta 2%:iin valitun lohkomallin mukaan.

## Oceanin Läpinäkyvyys

### Osallistujan Tiedot

![signup](assets/1.webp)

Kaikki tiedot altaasta ovat läpinäkyviä, mukaan lukien kaikki käyttäjätiedot. Ymmärtääksemme tätä kohtaa, otetaan esimerkki:

[Oceanin hallintapaneelissa](https://ocean.xyz/dashboard) on lukuisia tietoja, kuten hashrate viimeisen kuuden kuukauden aikana, altaan osallistujien määrä, louhittujen bitcoinien kokonaismäärä jne.

Keskitymme "Osallistujat"-osioon. Näet listan kaikista osallistujista heidän keskimääräisen hashratensa kanssa viimeisen kolmen tunnin ajalta sekä prosenttiosuuden **"osuuksista"** ja **"hashista"** verrattuna loppuallasta.
**"Osakkeiden %"** on prosenttiosuus työstä, jonka osallistuja on tarjonnut viimeisimpien kahdeksan lohkon aikana verrattuna loppuun pooliin.
**"Hash %"** on keskimääräisen hashraten prosenttiosuus, jonka osallistuja on tarjonnut viimeisen kolmen tunnin aikana verrattuna loppuun pooliin.

![signup](assets/2.webp)

Huomaat, että "Osallistujat" tunnistetaan Bitcoin-osoitteella. Voit klikata mitä tahansa näistä osoitteista saadaksesi lisätietoja.

Jos otamme ensimmäisen, sen jolla on korkein hashrate [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), voit nähdä kaikki tiedot tästä käyttäjästä: hashrate, louhitut bitcoinit, minkä lohkon kanssa, ja jopa yksityiskohdat heidän koneistaan (ASICs). He pysyvät kuitenkin nimettöminä, kuten Bitcoinissa.

### Lohkopohja

Hallintapaneelin vasemmassa yläkulmassa on "Seuraava lohko". Tällä sivulla on neljä erilaista lohkopohjaa. Ocean sallii jokaisen osallistujan valita lohkopohjan, jota he haluavat tukea. Tällä ei ole suoraa vaikutusta korvaukseesi. Kun pooli louhii lohkon, kaikki osallistujat saavat korvauksen riippumatta siitä, minkä pohjan he ovat valinneet. Tämä yksinkertaisesti sallii kaikkien "äänestää" heille sopivaa lohkopohjaa.

![signup](assets/3.webp)

**CORE:** Maksu 2%, tämä on klassinen Bitcoin Core -malli ilman suodatinta, kuten heidän sivullaan sanotaan "Sisältää transaktiot ja suurimman osan roskapostista"

**CORE+ANTISPAM:** Maksu 0%, Bitcoin Core suodattimella tietyille transaktioille kuten Ordinals "Sisältää transaktiot ja rajoittaa roskapostia"

**OCEAN:** Maksu 0%, Bitcoin Knot "Sisältää vain transaktiot ja kohtuullisen pienet tiedot"

**DATA-FREE:** Maksu 0%, Bitcoin Knot "Sisältää vain transaktiot ilman mitään satunnaisia tietoja"

### Erot Bitcoin Coren ja Bitcoin Knotsin välillä
Bitcoin Core on ohjelmisto, joka mahdollistaa noin 99% maailman Bitcoin-noodien toiminnan. Bitcoin on protokolla, mikä tarkoittaa, että aivan kuten Internetissä, jossa on useita selaimia, voi olla useita eri ohjelmistoja samanaikaisesti TimeChainilla. Kuitenkin yhteensopivuuden ja virheiden riskin rajoittamiseksi, jotka jättäisivät poistumattomia jälkiä TimeChainille, lähes kaikki Bitcoin-kehittäjät työskentelevät Bitcoin Coren parissa. Bitcoin Knots on Bitcoin Coren haarukka, mikä tarkoittaa, että se jakaa suurimman osan heidän koodistaan, rajoittaen suuresti virheiden riskiä. Tämä haarukka luotiin Luke Dashjr toimesta, joka halusi soveltaa tiukempia sääntöjä kuin Bitcoin Core ilman kovaa haarukkaa. Nyt, Bitcoin Core ja Bitcoin Knots elävät rinnakkain Nakamoto-konsensuksen ansiosta.

## Työntekijän lisääminen

Työntekijän lisäämiseksi aloita valitsemalla lohkopohjasi. Tämä valinta määrittää poolin URL-osoitteen, jonka syötät louhijaasi (ASICs).

- **CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- **CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- **OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- **DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404`

Seuraavaksi käyttäjäkenttään syötä oma Bitcoin-osoitteesi. Tässä on lista yhteensopivista osoitetyypeistä:
- **P2PKH** (Alkuperäinen osoitetyyppi. Alkaa “1”:llä)
- **P2SH** (Moniallekirjoitus tai P2SH-Segwit. Alkaa numerolla “3”)- **Bech32** (Segwit. Alkaa kirjaimilla “bc”.)
- **Bech32m** (Taproot. Alkaa kirjaimilla “bc”. Pidempi kuin Bech32.)

Jos sinulla on useita louhijoita, voit syöttää kaikille saman osoitteen, jolloin niiden hash-nopeudet yhdistyvät ja näkyvät yhtenä louhijana. Voit myös erottaa ne toisistaan antamalla kullekin oman nimen. Tee tämä yksinkertaisesti lisäämällä “.workername” Bitcoin-osoitteen perään.

Lopuksi, salasana-kenttään, käytä `x`.

**Esimerkki:**
Jos valitset **OCEAN** mallin, Bitcoin-osoitteesi on `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` ja haluat nimetä louhijasi “Brrrr”, sinun tulee syöttää seuraavat tiedot louhijasi käyttöliittymään:

- **URL**: `stratum+tcp://mine.ocean.xyz:3334`
- **KÄYTTÄJÄ**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- **SALASANA**: `x`

Muutaman minuutin kuluttua louhinnan aloittamisesta, voit nähdä tietosi Ocean-sivustolla etsimällä osoitteesi.

### Koontinäytön Yleiskatsaus
- **Osakkeet Palkintoikkunassa**: Tämä tieto osoittaa osakkeiden määrän, työn, jonka olet lähettänyt altaaseen viimeksi louhitun 8 lohkon ikkunassa.
- **Arvioidut Palkinnot Ikkunassa**: Arvio satoshien määrästä, jonka ansaitset jo tehdystä työstä. Tämä ei ota huomioon transaktiomaksuja, vaan ainoastaan coinbasen, verkoston myöntämät uudet bitcoinit.
- **Arvioidut Tulot Seuraavasta Lohkosta**: Arvio satoshien määrästä, jonka ansaitset, jos lohko louhitaan nyt. Muista, jos tämä arvo on alle 1,048,576 satsia, et suoraan vastaanota satseja osoitteeseesi. Ne lähetetään Oceanin osoitteeseen, kunnes ansiosi ylittävät tämän kynnyksen.

Alla on kuvaaja, joka näyttää hashrate-historiasi jopa 6 kuukauden ajalta.

![signup](assets/4.webp)

Tässä näet keskimääräisen hashratesi eri aikaskaaloilla, 60s:stä 24h:iin, sekä historian lohkoista, jotka allas on louhinut ja joista olet saanut palkkion.

![signup](assets/5.webp)

Voit viedä tämän historian CSV-tiedostona käyttämällä **Lataa CSV** -painiketta.

![signup](assets/6.webp)

Seuraavassa osiossa on luettelo kaikista louhijoista, jotka olet yhdistänyt altaaseen tällä osoitteella. Sinulla on tietenkin heidän yksittäinen hashratensa, mutta myös satoshien määrä, jonka he ovat yksilöllisesti saaneet työstään.

![signup](assets/7.webp)

Voit klikata minkä tahansa louhijan **Lempinimeä**. Tämän jälkeen näet kaikki juuri näkemäsi tiedot, mutta erityisesti kyseiselle louhijalle.

Ja sivun alaosassa on lisätietoja, joista näet osoitteesi maksuhistorian, louhitut satoshit, joita ei ole vielä maksettu, ja louhitut satoshit yhteensä.

![signup](assets/8.webp)

Tässä näet, että **Arvioitu Aika Minimimaksun Saamiseen** -laatikossa lukee Lightning, koska olemme asettaneet BOLT12-tarjouksen.

### Lightning-nostojen asettaminen
Kuten olet ymmärtänyt, Ocean pyrkii maksimoimaan läpinäkyvyyden ja minimoimaan hallinnan (satsien säilyttämisen puolestasi).
Siksi Lightning-nostojen yhteydessä on tarpeen käyttää **BOLT12-tarjouksia**. Tämä on uusi tapa suorittaa maksu Lightning-verkossa, joka alkaa yleistyä vuonna 2024 ja mahdollistaa useita asioita:
- Se on uudelleenkäytettävä maksulinkki, joka mahdollistaa automaattiset maksut ja toisin kuin Lightning-osoite, BOLT12 on ei-hallinnollinen.
- Se on myös maksutapa, joka tarjoaa todisteen maksun suorittamisesta, mikä ei päde LNURL-tapauksissa.
- Erittäin tärkeää, sitä voidaan käyttää yhdessä Bitcoin-allekirjoituksen kanssa todistamaan, että olet sekä BTC-osoitteen että BOLT12-tarjouksen haltija.
Tänään (toukokuu 2024), on olemassa vain muutamia ratkaisuja tämän menetelmän käyttämiseen. Tässä esimerkissä käytämme Start9-palvelinta Core Lightningin kanssa. Kun muut työkalut, kuten esimerkiksi Phoenix Wallet, ovat integroineet BOLT12-tarjoukset, tämä opas pysyy sovellettavana. Varmista, että sinulla on avoimia kanavia sisääntulevalla likviditeetillä, muuten maksut eivät toimi.

Aloita menemällä Ocean-sivuston hallintapaneeliin syöttämällä BTC-osoitteesi, sitten klikkaa **Configuration**-välilehteä.

![signup](assets/9.webp)

Kopioi **Description**-teksti täältä:
`OCEAN Maksut bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`

Siirry nyt Core Lightning -käyttöliittymääsi Start9-palvelimellasi (tai mihin tahansa lompakkoon, joka kykenee tarjoamaan BOLT12-tarjouksen).

![signup](assets/10.webp)

Klikkaa **Receive**.

Valitse **Offer**, sitten liitä aiemmin kopioitu teksti **Description**-kenttään ja jätä **Amount**-kenttä tyhjäksi.

![signup](assets/11.webp)

Klikkaa **Generate Offer**.

![signup](assets/12.webp)

Olet luonut uudelleenkäytettävän ja pysyvän maksulinkin, joka ei vaadi keskitettyä palvelinta kuten Lightning-osoitteiden tapauksessa. Kopioi linkki ja palaa sitten Ocean-sivulle.

**Lightning BOLT12 Offer** -kenttään, liitä maksulinkki ja jätä **Block Height** -kenttä oletusarvoonsa. Klikkaa **GENERATE**.

![signup](assets/13.webp)

Jotta Ocean voi varmistaa, että tämä maksulinkki todella kuuluu sinulle käyttämättä tiliä, sinun on allekirjoitettava juuri luotu viesti yksityisellä avaimellasi, joka vastaa käyttämääsi Bitcoin-osoitetta. Monia ratkaisuja on olemassa viestin allekirjoittamiseksi yksityisellä avaimellasi. Tässä oppaassa otamme esimerkiksi BlueWalletin, mutta menetelmä on sama kaikille lompakoille.

![signup](assets/14.webp)

Olettaen, että yksityinen avaimesi on BlueWalletissa (voit tehdä saman laitteistolompakolla), klikkaa kyseistä lompakkoa.

![signup](assets/15.webp)

Sitten **…** yläoikealla.

![signup](assets/15bis.webp)

Ja **Sign/Verify Message**.

![signup](assets/16.webp)

Tässä ikkunassa on kolme kenttää: **Address**, **Signature**, ja **Message**.

**Address**-kenttään, syötä Bitcoin-osoitteesi. Jos palaamme esimerkkiimme, se on osoite: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.

Jätä **Signature**-kenttä tyhjäksi.
Ja liitä luotu viesti **Viesti**-kenttään Oceanin sivulla: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`Klikkaa **Allekirjoita**.

Tämä luo kryptografisen allekirjoituksen, joka todistaa sinun olevan osoitteen `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` omistaja, ja tämä allekirjoitus on ainutlaatuinen kiitos viestin, jonka Ocean tuotti BOLT12 maksulinkistä.

![signup](assets/17.webp)

Kopioi allekirjoitus ja liitä se Oceanin sivulle, sitten klikkaa **VAHVISTA**.

![signup](assets/18.webp)

Sinun pitäisi nähdä vahvistusviesti.

![signup](assets/19.webp)

Nyt siirry **Omat Tilastot** -välilehteen. Lisätietoja näytetään yläosassa aiemmin Core Lightningilla Start9:ssä luomallasi BOLT12 maksulinkillä.

![signup](assets/20.webp)