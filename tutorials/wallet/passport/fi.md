---
name: Passi - Säätiö
description: Passport-laitteiston lompakon määrittäminen ja käyttö manuaalisessa tilassa
---
![cover](assets/cover.webp)

Passport on pelkästään Bitcoinia käyttävä laitteistolompakko, jonka on suunnitellut huhtikuussa 2020 Bostonissa perustettu yhdysvaltalainen yritys Foundation Devices.

Passport "*Batch 2*", jota esittelemme tässä oppaassa, on "*Founder's Edition*"-version seuraaja. Se erottuu premium-muotoilullaan, korkearesoluutioisella värinäytöllään ja ergonomisella fyysisellä näppäimistöllään. Se toimii "*Air-Gap*"-tilassa, mikä varmistaa, että lompakkosi yksityiset avaimet pysyvät täysin eristettyinä, ja tiedonsiirto tapahtuu MicroSD-kortin tai QR-koodien kautta. Laitteessa on irrotettava ja ladattava Nokia BL-5C akku, jonka kapasiteetti on 1200 mAh. Tämä vakiomalliakku on helposti vaihdettavissa, koska BL-5C-mallia on laajalti saatavilla kaupoista.

Liitettävyyden osalta Passportissa on MicroSD-portti, USB-C-portti latausta varten ja takakamera QR-koodien skannausta varten.

Turvallisuuden osalta Passport sisältää turvallisen elementin, ja laitteen lähdekoodi on täysin avointa lähdekoodia. Se tarjoaa kaikki ominaisuudet, joita hyvältä Bitcoin-laitelompakolta odotetaan. Huomaa, että Passport ei vielä tue miniscriptiä, mutta tämä ominaisuus on suunnitteilla vuoden 2025 toiselle neljännekselle.

Passport on hinnoiteltu 199 dollariin, ja se kilpailee Coldcard Q:n, Jade Plusin, Tezor Safe 5:n ja Ledgerin huippumallien kanssa.

![Image](assets/fr/01.webp)

Voit hallita turvallista lompakkoasi Passportissa useilla eri vaihtoehdoilla. Tämä laitteistolompakko on yhteensopiva useimpien markkinoilla olevien lompakonhallintaohjelmistojen kanssa, kuten Sparrow Wallet, Specter Desktop, Nunchuk, Keeper ja muut. Tässä opetusohjelmassa opettelemme käyttämään sitä Sparrow-lompakon kanssa.

Jos olet aloittelija, helpoin vaihtoehto on käyttää Passportia Foundationin kehittämän Envoy-sovelluksen kanssa. Jos haluat tietää, miten Envoy-sovellusta käytetään Passportin kanssa, katso tämä toinen opetusohjelma :

https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

## Passin avaaminen

Kun saat passisi, varmista, että laatikko ja pahvipakkauksen sinetti ovat ehjät, jotta voit varmistaa, ettei pakettia ole avattu. Laitteen aitouden ja koskemattomuuden ohjelmistovarmennus suoritetaan myös laitteen käyttöönoton yhteydessä.

![Image](assets/fr/02.webp)

Laatikon sisältö sisältää:


- Passi;
- Pahvinpala, johon voit kirjoittaa muistisääntösi;
- USB-C-kaapeli latausta varten ;
- MicroSD-kortti ;
- Kaksi MicroSD Lightning- tai USB-C-sovitinta ;
- Tarrat.

Laitteessa on :


- Näppäimistö (1) ;
- USB-C-portti (2);
- Poistopainike (3);
- Paluupainike (4) ;
- Vahvistuspainike (5);
- Suuntatyyny (6);
- On/off-painike (7);
- Tilan ilmaisin (8);
- MicroSD-portti (9) ;
- Painike tilan aA1 vaihtamiseksi (10) ;
- Takakamera.

![Image](assets/fr/03.webp)

## Aloituspassi

Käynnistä laite painamalla laitteen sivulla olevaa on/off-painiketta.

![Image](assets/fr/04.webp)

Paina vahvistuspainiketta päästäksesi seuraavaan valikkoon.

![Image](assets/fr/05.webp)

Tässä oppaassa käytämme Sparrow Wallet -lompakkoa passilla suojatun lompakon hallintaan. Valitse "*Manuaalinen asennus*".

![Image](assets/fr/06.webp)

Hyväksy sitten käyttöehdot.

![Image](assets/fr/07.webp)

Seuraavaksi tarkistat laitteesi. Tämä vahvistaa passisi aitouden ja varmistaa, ettei sitä ole peukaloitu kuljetuksen aikana. Sinua pyydetään skannaamaan QR-koodi.

![Image](assets/fr/08.webp)

Mene [viralliselle varmennussivustolle] (https://validate.foundationdevices.com/) ja valitse "*Passi*".

![Image](assets/fr/09.webp)

Skannaa sivustolla näkyvä QR-koodi Passportin kameran avulla.

![Image](assets/fr/10.webp)

Laitteesi näyttää tämän jälkeen 4 sanaa.

![Image](assets/fr/11.webp)

Vahvista passisi aitous kirjoittamalla nämä sanat verkkosivustolla ja napsauta "*Validoi*".

![Image](assets/fr/12.webp)

Jos näyttöön tulee viesti "*Passed*", laitteiston lompakko on aito. Voit nyt käyttää sitä Bitcoin-lompakon suojaamiseen.

![Image](assets/fr/13.webp)

Vahvista testitulos passistasi.

![Image](assets/fr/14.webp)

## PIN-koodin asettaminen

Seuraavaksi tulee PIN-koodin vaihe. PIN-koodi avaa passisi lukituksen. Se suojaa siis luvattomalta fyysiseltä käytöltä. PIN-koodi ei osallistu lompakkosi kryptografisten avainten johtamiseen. Vaikka PIN-koodia ei olisikaan saatavilla, 12- tai 24-sanaisen muistilausekkeen avulla voit saada bitcoinisi takaisin haltuusi, vaikka sinulla ei olisikaan pääsyä siihen.

![Image](assets/fr/15.webp)

Suosittelemme valitsemaan mahdollisimman satunnaisen PIN-koodin. Muista myös tallentaa tämä koodi erilliseen paikkaan siitä, missä passisi on tallennettu (esim. salasanahallintaan).

Voit valita PIN-koodin 6-12 numeron väliltä. Suosittelen tekemään siitä mahdollisimman pitkän.

Syötä PIN-numerot näppäimistöllä. Kun olet valmis, napsauta vahvistuspainiketta.

![Image](assets/fr/16.webp)

Vahvista PIN-koodi toisen kerran.

![Image](assets/fr/17.webp)

PIN-koodisi on rekisteröity.

![Image](assets/fr/18.webp)

## Passportin laiteohjelmiston päivittäminen

Laitteistosi lompakko ehdottaa, että päivität sen laiteohjelmiston. Suosittelen, että päivität välittömästi, jotta voit hyödyntää uusimpien versioiden tuomat parannukset ja korjaukset. Jatka klikkaamalla oikealla olevaa vahvistuspainiketta.

![Image](assets/fr/19.webp)

Passport on valmis vastaanottamaan uuden laiteohjelmiston MicroSD-kortin kautta.

![Image](assets/fr/20.webp)

Käytä tähän Passport-pakkauksen mukana toimitettua MicroSD-korttia (tai toista korttia) ja aseta se tietokoneeseen. Lataa uusin laiteohjelmistoversio [säätiön dokumentointisivustolta](https://docs.foundation.xyz/firmware-updates/passport/) tai [säätiön GitHub-arkistosta](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Ennen kuin asennat sen laitteeseesi, suosittelemme, että tarkistat ladatun laiteohjelmiston aitouden ja eheyden. Jos tarvitset apua tässä, katso tätä ohjetta :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Kun olet tarkistanut `.bin`-tiedoston, aseta se MicroSD-muistikortille ja aseta se sitten Passportiin. Passportin tiedostoetsintä avautuu. Valitse tiedosto `vN.N.N.N-passport.bin`.

![Image](assets/fr/22.webp)

Napsauta "*Valitse*".

![Image](assets/fr/23.webp)

Vahvista sitten laiteohjelmiston asennus.

![Image](assets/fr/24.webp)

Odota, että päivitys on valmis.

![Image](assets/fr/25.webp)

Kun päivitys on valmis, avaa laitteen lukitus PIN-koodilla ja jatka määritystä.

![Image](assets/fr/26.webp)

## Luo uusi Bitcoin-lompakko

Nyt on aika luoda uusi Bitcoin-lompakko. Napsauta vahvistuspainiketta.

![Image](assets/fr/27.webp)

Voit luoda uuden salkun napsauttamalla "*Luo uusi siemen*".

![Image](assets/fr/28.webp)

Voit valita 12- tai 24-sanaisen muistilausekkeen. Molempien vaihtoehtojen tarjoama turvallisuus on samanlainen, joten voit valita sen, joka on helpointa tallentaa, eli 12 sanaa.

![Image](assets/fr/29.webp)

Napsauta "*Jatka*".

![Image](assets/fr/30.webp)

Passisi luo nyt "*Turvakoodin*". Tämä on numerosarja, jota voidaan käyttää MicroSD-kortille tallennetun lompakkosi varmuuskopion salauksen purkamiseen. Tämä Foundation-laitteille ominainen varmuuskopiointijärjestelmä muodostaa lisävarmistuksen muistilauseellesi, mutta se ei ole yhteensopiva muiden Bitcoin-ohjelmistojen kanssa.

Jos päätät käyttää tätä "*Varmuuskopiointikoodia*", muista säilyttää se eri paikassa kuin MicroSD-kortti, joka sisältää lompakkosi salatun varmuuskopion. Voit kuitenkin päättää olla käyttämättä tätä järjestelmää, jos koet, että hyvä varmuuskopio muistikielestäsi riittää.

![Image](assets/fr/31.webp)

Kirjoita "*Backup Code*" vahvistaaksesi, että olet tallentanut sen oikein.

![Image](assets/fr/32.webp)

Jos MicroSD-muistikortti on asetettu paikalleen, portfoliosi salattu varmuuskopio on tallennettu sinne.

![Image](assets/fr/33.webp)

Passissasi näkyy 12-sanainen muistisääntö. Tämä muistisana antaa sinulle täyden, rajoittamattoman pääsyn kaikkiin bitcoineihisi. Kuka tahansa, jolla on hallussaan tämä lauseke, voi varastaa varasi, vaikka hänellä ei olisi fyysistä pääsyä passiisi.

12-sanainen lause palauttaa pääsyn bitcoineihisi, jos passisi katoaa, varastetaan tai rikkoutuu. Siksi on erittäin tärkeää tallentaa se huolellisesti ja säilyttää se turvallisessa paikassa.

Voit kirjoittaa sen laatikossa olevaan pahviin, tai jos haluat lisätä turvallisuutta, suosittelen kaiverrusta ruostumattomasta teräksestä valmistettuun alustaan, joka suojaa sitä tulipalolta, tulvalta tai romahdukselta.

Napsauta vahvistuspainiketta nähdäksesi muistisääntösi.

![Image](assets/fr/34.webp)

Jos haluat lisätietoa siitä, miten muistisääntöjä tallennetaan ja hallitaan oikein, suosittelen seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

näitä sanoja ei tietenkään saa koskaan jakaa internetissä, kuten minä teen tässä ohjeessa. Tätä esimerkkisalkkua käytetään vain Testnetissä, ja se poistetaan opetusohjelman päätyttyä.**_

Tee fyysinen varmuuskopio tästä lauseesta.

![Image](assets/fr/35.webp)

Passportin määritys on onnistunut. Jatka klikkaamalla vahvistuspainiketta.

![Image](assets/fr/36.webp)

## Valikon löytäminen

Passportin käyttöliittymässä on kolme päävalikkoa:


- "*Tili*";
- "*Lisää*";
- "*Settings*".

Voit siirtyä näiden valikoiden välillä käyttämällä ohjauspaneelin vasenta ja oikeaa nuolinäppäintä.

### *Tili*"-valikko

"*Tili*"-valikosta löydät Bitcoin-lompakkosi tärkeimmät ominaisuudet. Voit allekirjoittaa tapahtuman joko kameran tai MicroSD-portin kautta.

![Image](assets/fr/37.webp)

"*Tilin työkalut*" -alavalikossa voit esimerkiksi tarkistaa osoitteen, allekirjoittaa viestin tai tarkastella salkussasi olevia osoitteita.

![Image](assets/fr/38.webp)

"*Tilin hallinta*" -alavalikossa voit liittää Bitcoin-lompakkosi lompakonhallintaohjelmistoon (jota käsittelemme tämän ohjeen seuraavissa vaiheissa) tai tarkastella ja nimetä tilisi uudelleen.

![Image](assets/fr/39.webp)

### Lisää"-valikko

Valikossa "*Lisää*" voit luoda salkkuusi uuden tilin, joka on liitetty samaan muistisääntöön.

![Image](assets/fr/40.webp)

Voit myös syöttää BIP39-salasanan (katso seuraava kohta) tai käyttää väliaikaista siementä.

![Image](assets/fr/41.webp)

### Asetukset"-valikko

Valikosta "*asetukset*" löydät kaikki lompakko- ja laiteasetukset.

![Image](assets/fr/42.webp)

"*Laite*"-alavalikossa voit mukauttaa näytön kirkkautta, asettaa automaattisen lukituksen viiveen, muuttaa PIN-koodia tai nimetä laitteen uudelleen.

![Image](assets/fr/43.webp)

"*Backup*"-alavalikosta voit viedä salatun portfolion varmuuskopion, tarkistaa olemassa olevan varmuuskopion voimassaolon tai etsiä "*Backup-koodin*" uudelleen.

![Image](assets/fr/44.webp)

"*Firmware*"-alavalikossa voit päivittää Passportin laiteohjelmiston. Suosittelemme, että teet nämä päivitykset säännöllisesti, jotta voit hyödyntää uusimpia korjauksia ja ominaisuuksia.

![Image](assets/fr/45.webp)

"*Bitcoin*"-alavalikossa voit vaihtaa näytettävää yksikköä (BTC tai satoshis), hallita mahdollista Multisig-lompakkoa tai siirtyä "*Testnet*"-tilaan.

![Image](assets/fr/46.webp)

Kohdassa "*Advanced*" voit tarkastella muistilauseen sanoja, suorittaa toimintoja asetetulle MicroSD-muistikortille, palauttaa Passportin tehdasasetukset tai suorittaa aitoustarkastuksen, kuten aiemmin on tehty.

![Image](assets/fr/47.webp)

Voit aktivoida "*Turvasanat*" -toiminnon, joka lisää turvallisuutta näyttämällä kaksi erityistä sanaa, kun avaat laitteen lukituksen PIN-koodin neljän ensimmäisen numeron syöttämisen jälkeen. Nämä sanat, jotka tallennetaan konfiguroinnin aikana, varmistavat, että Passportia ei ole vaihdettu tai peukaloitu. Jos myöhemmin ilmenee ristiriitaisuuksia, suosittelemme, ettet käytä laitetta. Suosittelen aktivoimaan tämän vaihtoehdon, jotta vältät suurimman osan laitteen fyysisen vaarantumisen riskeistä.

![Image](assets/fr/48.webp)

Lopuksi "*Laajennukset*"-alavalikossa voit aktivoida laitteen tiettyihin käyttötarkoituksiin liittyviä toimintoja, kuten Whirlpoolin coinjoin-protokollan.

![Image](assets/fr/49.webp)

## Lisää BIP39-salasana

Ennen kuin jatkat, voit halutessasi lisätä BIP39-salasanan. BIP39-salalause on valinnainen salasana, jonka voit valita vapaasti ja joka lisätään muistilausekkeeseen lompakon turvallisuuden vahvistamiseksi. Kun tämä ominaisuus on käytössä, Bitcoin-lompakkoon pääsy edellyttää sekä muistisääntöä että salasanaa. Ilman kumpaakaan lompakkoa olisi mahdotonta palauttaa.

Ennen kuin määrität tämän vaihtoehdon Passportissasi, on erittäin suositeltavaa, että luet tämän artikkelin, jotta ymmärrät täysin salasanan teoreettisen toiminnan ja vältät virheet, jotka voivat johtaa bitcoinien menettämiseen:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Voit aktivoida sen menemällä "*Lisää*"-valikkoon ja napsauttamalla "*Enter Passphrase*".

![Image](assets/fr/50.webp)

Kirjoita salasana aA1-näppäimistöllä ja varmista, että tallennat sen yhden tai useamman kerran fyysiselle tietovälineelle (paperille tai metallille). Esimerkissä käytän hyvin heikkoa salasanaa, mutta sinun kannattaa valita vahva, satunnainen salasana, joka sisältää kaikki merkkityypit ja on riittävän pitkä (kuten vahva salasana).

![Image](assets/fr/51.webp)

Huomaa, että BIP39-salasanat ovat isojen ja pienten kirjainten suhteen herkkiä. Jos syötät hieman erilaisen salasanan kuin alun perin määritetty, Passport ei ilmoita virheestä, vaan se muodostaa toisen salausavaimenpaketin, joka ei ole alkuperäisen lompakkosi avainten joukossa.

Siksi on tärkeää, että kirjaat konfiguroinnin yhteydessä jonnekin muistiin pääavaimen sormenjäljen, jonka saat seuraavassa vaiheessa. Esimerkiksi salasanalla `Plan B Network` pääavaimeni sormenjälki on `745D526B`.

![Image](assets/fr/52.webp)

Aina kun avaat Passportin lukituksen, sinun on palattava tähän valikkoon syöttääksesi salasanasi ja soveltaaksesi sitä lompakkoosi. Passport ei tallenna salasanaa.

Tarkista joka kerta, kun avaat lukituksen kirjoitettuasi salasanan, tästä vahvistusnäytöstä, että annettu sormenjälki on sama kuin konfiguroinnin aikana kirjoittamasi sormenjälki. Jos se on, salasanasi on oikea ja käytät oikeaa Bitcoin-lompakkoa. Jos se ei ole, olet väärällä lompakolla ja sinun on yritettävä uudelleen ja varottava syöttövirheitä.

Ennen kuin saat ensimmäiset bitcoinit lompakkoosi, **suositan sinua tekemään tyhjän palautustestin**. Merkitse muistiin joitakin viitetietoja, kuten xpub- tai ensimmäinen vastaanottava osoitteesi, ja poista lompakkosi Passportista, kun se on vielä tyhjä (`Asetukset -> Lisäasetukset -> Poista Passportti`). Yritä sitten palauttaa lompakkosi käyttämällä paperisia varmuuskopioita muistilausekkeesta ja mahdollisesta salasanasta. Tarkista, että palautuksen jälkeen luodut evästetiedot vastaavat alun perin kirjoittamiasi tietoja. Jos ne täsmäävät, voit olla varma, että paperiset varmuuskopiot ovat luotettavia. Jos haluat lisätietoja testipalautuksen suorittamisesta, tutustu tähän toiseen opetusohjelmaan :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)

## Lompakon määrittäminen Sparrow Walletissa

Tässä opetusohjelmassa näytän sinulle Passportin edistyneen käytön Sparrow Walletin kanssa. Tämä laitteistolompakko on kuitenkin yhteensopiva myös Envoyn (Foundation-sovellus), Keeperin, BlueWalletin, Nunchukin, Specterin ja monien muiden...

Aloita lataamalla ja asentamalla Sparrow Wallet [virallisilta verkkosivuilta](https://sparrowwallet.com/) tietokoneellesi, jos et ole jo tehnyt sitä.

![Image](assets/fr/54.webp)

Varmista ohjelmiston aitous ja eheys ennen asennusta. Jos et tiedä, miten tämä tehdään, tutustu tähän ohjeeseen:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Kun Sparrow Wallet on avattu, napsauta välilehteä "*File*" ja sitten "*New Wallet*".

![Image](assets/fr/55.webp)

Anna lompakollesi nimi ja napsauta sitten "*Luo lompakko*".

![Image](assets/fr/56.webp)

Valitse "*Airapped Hardware Wallet*".

![Image](assets/fr/57.webp)

Napsauta "*Scan...*"-kohtaa "*Passi*"-vaihtoehdon vieressä. Tämä avaa web-kamerasi.

![Image](assets/fr/58.webp)

Mene laitteiston lompakossasi "*Tili*"-valikkoon, valitse "*Tilin hallinta*"-alavalikko ja napsauta "*Lompakon yhdistäminen*".

![Image](assets/fr/59.webp)

Valitse avautuvasta avattavasta luettelosta "*Sparrow*".

![Image](assets/fr/60.webp)

Valitse sitten "*Single-sig*", jos haluat normaalin kokoonpanon ilman multisigiä.

![Image](assets/fr/61.webp)

Valitse vaihtoehto "*QR-koodi*".

![Image](assets/fr/62.webp)

Passisi luo sitten dynaamisia QR-koodeja. Skannaa ne tietokoneen web-kameran avulla Sparrow-ohjelmistoon.

![Image](assets/fr/63.webp)

Sinun pitäisi nyt nähdä xpub ja pääavaimesi sormenjälki, jonka pitäisi olla sama kuin Passportissa, kun syötät tunnuslauseen. Napsauta "*Apply*"-painiketta.

![Image](assets/fr/64.webp)

Aseta vahva salasana, jolla varmistat pääsyn Sparrow-lompakkoosi. Tämä salasana suojaa julkisia avaimia, osoitteita, tarroja ja tapahtumahistoriaa luvattomalta käytöltä. Salasana kannattaa tallentaa salasanahallintaan, jotta et unohda sitä.

![Image](assets/fr/65.webp)

Passport pyytää sinua sitten skannaamaan ensimmäisen vastaanottoosoitteen vahvistaaksesi, että tuonti on onnistunut.

![Image](assets/fr/66.webp)

Siirry Sparrow'ssa välilehdelle "*Vastaanottaa*" ja skannaa ensimmäisen osoitteen QR-koodi.

![Image](assets/fr/67.webp)

Jos toiminto onnistuu, passissa näkyy "*Varmennettu*".

![Image](assets/fr/68.webp)

Tämä vahvistaa, että tuonti onnistui.

![Image](assets/fr/69.webp)

## Vastaanottaa bitcoineja

Nyt kun Passport on perustettu, olet valmis vastaanottamaan ensimmäiset satsit uuteen Bitcoin-lompakkoosi. Tee se Sparrow'ssa napsauttamalla "*Vastaanottaa*"-valikkoa.

![Image](assets/fr/70.webp)

Sparrow näyttää ensimmäisen tyhjän kuittiosoitteen salkussasi. Voit lisätä etiketin.

![Image](assets/fr/71.webp)

Ennen käyttöä tarkistamme Passport-näytössä olevan osoitteen varmistaaksemme, että se kuuluu Bitcoin-lompakkoomme. Sparrow'ssa voit tarvittaessa suurentaa osoitteen QR-koodia klikkaamalla sitä. Valitse Passportin "*Tili*"-valikosta "*Tilin työkalut*".

![Image](assets/fr/72.webp)

Napsauta "*Varmista osoite*" ja skannaa sitten Sparrow Walletissa näkyvä QR-koodi.

![Image](assets/fr/73.webp)

Varmista, että passissa näkyvä osoite vastaa täsmälleen Sparrow'ssa näkyvää osoitetta ja että "*Varmennettu*" on näkyvissä.

![Image](assets/fr/74.webp)

Voit nyt käyttää sitä bitcoinien vastaanottamiseen. Kun transaktio lähetetään verkossa, se näkyy Sparrow'ssa. Odota, kunnes olet saanut tarpeeksi vahvistuksia, jotta voit pitää tapahtumaa lopullisena.

![Image](assets/fr/75.webp)

## Lähetä bitcoineja

Nyt kun lompakossasi on muutama sati, voit myös lähettää niitä. Voit tehdä niin klikkaamalla "*UTXOs*"-valikkoa.

![Image](assets/fr/76.webp)

Valitse UTXO:t, joita haluat käyttää tämän tapahtuman syötteinä, ja napsauta sitten "*Send Selected*".

![Image](assets/fr/77.webp)

Kirjoita vastaanottajan osoite, etiketti, joka muistuttaa sinua tapahtuman tarkoituksesta, ja summa, jonka haluat lähettää tähän osoitteeseen.

![Image](assets/fr/78.webp)

Säädä palkkio nykyisten markkinaolosuhteiden mukaan ja napsauta sitten "*Luo transaktio*".

![Image](assets/fr/79.webp)

Tarkista, että kaikki tapahtumaparametrit ovat oikein, ja napsauta sitten "*Viimeistele tapahtuma allekirjoitusta varten*".

![Image](assets/fr/80.webp)

Klikkaa "*Show QR*" näyttääksesi PSBT:n (*Partially Signed Bitcoin Transaction*). Sparrow on rakentanut transaktion, mutta siitä puuttuvat vielä allekirjoitukset, jotta syötössä käytetyt bitcoinit voitaisiin avata. Nämä allekirjoitukset voi suorittaa vain Passport, joka isännöi siemenesi antamalla pääsyn transaktion allekirjoittamiseen tarvittaviin yksityisiin avaimiin.

![Image](assets/fr/81.webp)

Siirry Passportissasi "*Tili*"-valikkoon ja napsauta "*Allekirjoita QR-koodilla*".

![Image](assets/fr/82.webp)

Skannaa Sparrow-lompakossa näkyvä PSBT (*Partially Signed Bitcoin Transaction*).

![Image](assets/fr/83.webp)

Vahvista, että vastaanottava osoite ja lähetetty summa ovat oikein, ja paina sitten vahvistuspainiketta.

![Image](assets/fr/84.webp)

Tarkista vaihto-osoite. Esimerkissäni sitä ei ole, koska tapahtuma sisältää vain yhden tulosteen.

![Image](assets/fr/85.webp)

Varmista, että maksu on valitsemasi.

![Image](assets/fr/86.webp)

Jos kaikki tiedot ovat oikein, allekirjoita maksutapahtuma napsauttamalla vahvistuspainiketta.

![Image](assets/fr/87.webp)

Napsauta Sparrow Walletissa "*Scan QR*" ja skannaa passissasi näkyvä QR-koodi.

![Image](assets/fr/88.webp)

Allekirjoittamasi transaktio on nyt valmis lähetettäväksi Bitcoin-verkkoon ja sisällytettäväksi louhijan lohkoon. Jos kaikki on oikein, napsauta "*Lähetä transaktio*".

![Image](assets/fr/89.webp)

Tapahtumasi on lähetetty ja odottaa vahvistusta.

![Image](assets/fr/90.webp)

Onneksi olkoon, tiedät nyt, miten Passportin asetukset määritetään ja miten sitä käytetään. Jos löysit tämän ohjeen hyödylliseksi, olisin kiitollinen, jos jättäisit vihreän peukalon alle. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos jakamisesta!

Lisätietoja on Liana-ohjelmiston oppaassa:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
