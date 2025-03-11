---
name: Lähettiläs
description: Passin määrittäminen ja käyttö Envoy-sovelluksen kanssa
---
![cover](assets/cover.webp)

Envoy on Foundationin kehittämä Bitcoin-lompakon hallintasovellus. Se on erityisesti suunniteltu käytettäväksi Passport-laitelompakon kanssa.

Passport "*Batch 2*", jonka esittelemme tässä oppaassa Envoy-sovelluksen kanssa, on "*Founder's Edition*" -version seuraaja. Siinä on ensiluokkainen muotoilu, teräväpiirtovärinäyttö ja ergonominen fyysinen näppäimistö. Se toimii "*Air-Gap*"-tilassa, joka varmistaa, että lompakkosi yksityiset avaimet pysyvät täysin eristettyinä, ja vaihdot ovat mahdollisia MicroSD-kortin tai QR-koodien kautta. Laitteessa on irrotettava 1200 mAh:n akku.

Liitettävyyden osalta Passportissa on MicroSD-portti, USB-C-portti latausta varten ja takakamera QR-koodien skannausta varten.

Turvallisuuden osalta Passport sisältää turvallisen elementin, ja laitteen lähdekoodi on täysin avointa lähdekoodia. Se tarjoaa kaikki ominaisuudet, joita hyvältä Bitcoin-laitelompakolta odotetaan. Huomaa, että Passport ei vielä tue miniscriptiä, mutta tämä ominaisuus on suunnitteilla vuoden 2025 toiselle neljännekselle.

Passport on hinnoiteltu 199 dollariin, ja se kilpailee Coldcard Q:n, Jade Plusin, Tezor Safe 5:n ja Ledgerin huippumallien kanssa.

![Image](assets/fr/01.webp)

Voit hallita turvallista lompakkoasi Passportissa useilla eri vaihtoehdoilla. Tämä laitteistolompakko on yhteensopiva useimpien markkinoilla olevien lompakonhallintaohjelmistojen kanssa, kuten Sparrow Wallet, Specter Desktop, Nunchuk, Keeper ja muut.

Tässä aloittelijoille ja keskitason käyttäjille suunnatussa oppaassa opimme, miten Envoy-sovellusta käytetään Passportin kanssa. Se on helpoin tapa saada laitteiston lompakosta kaikki irti.

Jos olet edistynyt käyttäjä ja haluat tutustua monimutkaisempiin ominaisuuksiin, suosittelen tutustumaan tähän toiseen opetusohjelmaan, jossa konfiguroimme Passportin ja Sparrow Walletin :

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

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

## Lataa Envoy-sovellus

Mene sovelluskauppaan ja lataa Envoy :


- [Google Play Store](https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- [App Storessa](https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- On [F-Cold] (https://foundation.xyz/fdroid/).

![Image](assets/fr/50.webp)

Voit myös ladata APK-tiedoston suoraan [säätiön GitHub-arkistosta](https://github.com/Foundation-Devices/envoy/releases).

![Image](assets/fr/51.webp)

Kun sovellus on avattu, valitse "*Passin hallinta*".

![Image](assets/fr/52.webp)

Valitse, haluatko aktivoida Tor-yhteyden luottamuksellisuuden vahvistamiseksi, ja paina sitten "*Jatka*".

![Image](assets/fr/53.webp)

Valitse "*Kytke olemassa oleva Passport*", jos Passport on jo määritetty, tai "*Lisää uusi Passport*", jos alustat laitteiston lompakon ensimmäistä kertaa.

![Image](assets/fr/54.webp)

Hyväksy käyttöehdot.

![Image](assets/fr/55.webp)

Tämän jälkeen sinua pyydetään varmistamaan passin aitous. Napsauta "*Seuraava*".

![Image](assets/fr/56.webp)

## Aloituspassi

Käynnistä laite painamalla laitteen sivulla olevaa on/off-painiketta.

![Image](assets/fr/04.webp)

Paina vahvistuspainiketta päästäksesi seuraavaan valikkoon.

![Image](assets/fr/05.webp)

Tässä ohjeessa käytämme Envoyta Passport-suojatun lompakon hallintaan. Valitse "*Envoy App*".

![Image](assets/fr/57.webp)

Napsauta "*Jatka Envoy-ohjelmassa*".

![Image](assets/fr/58.webp)

Seuraavaksi tarkistat laitteesi. Tämä vahvistaa passisi aitouden ja varmistaa, ettei sitä ole peukaloitu kuljetuksen aikana. Sinua pyydetään skannaamaan QR-koodi.

![Image](assets/fr/08.webp)

Skannaa sovelluksessa näkyvät dynaamiset QR-koodit passillasi. Kun skannaus on valmis, napsauta "*Seuraava*".

![Image](assets/fr/59.webp)

Skannaa sitten puhelimellasi passissa näkyvä QR-koodi.

![Image](assets/fr/60.webp)

Jos näyttöön tulee viesti "*Passisi on suojattu*", tämä vahvistaa, että laitteistolompakkosi on aito. Voit nyt käyttää sitä Bitcoin-lompakon suojaamiseen.

![Image](assets/fr/61.webp)

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

### Ilman Envoy-sovellusta

Käytä tähän Passport-pakkauksen mukana toimitettua MicroSD-korttia (tai toista korttia) ja aseta se tietokoneeseen. Lataa uusin laiteohjelmistoversio [säätiön dokumentointisivustolta](https://docs.foundation.xyz/firmware-updates/passport/) tai [säätiön GitHub-arkistosta](https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Ennen kuin asennat sen laitteeseesi, suosittelemme, että tarkistat ladatun laiteohjelmiston aitouden ja eheyden. Jos tarvitset apua tässä, katso tätä ohjetta :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Envoy-sovelluksen avulla

Toinen, yksinkertaisempi vaihtoehto on käyttää suoraan Envoy-sovellusta. Napsauta "*Download Firmware*".

![Image](assets/fr/62.webp)

Käytä Passportin mukana toimitettua sovitinta MicroSD-kortin liittämiseen puhelimeen.

![Image](assets/fr/63.webp)

Valitse MicroSD-kortti tiedostoetsimessäsi laiteohjelmiston tallentamista varten.

![Image](assets/fr/64.webp)

Laiteohjelma on nyt tallennettu. Poista MicroSD-muistikortti älypuhelimesta ja aseta se Passportiin.

![Image](assets/fr/65.webp)

Passport-tiedostonetsintäohjelma avautuu. Valitse tiedosto `vN.N.N.N-passport.bin`.

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

## Salkun määrittäminen Envoy-järjestelmässä

Tässä opetusohjelmassa näytän, miten Passportia käytetään Envoy-sovelluksen kanssa. Tämä laitteistolompakko on kuitenkin yhteensopiva myös Sparrow Walletin, Keeperin, BlueWalletin, Nunchukin, Specterin ja monien muiden...

![Image](assets/fr/66.webp)

Skannaa passissasi näkyvä QR-koodi Envoy-sovelluksella.

![Image](assets/fr/67.webp)

Julkiset avaimesi on nyt tuotu sovellukseen. Napsauta "*Varmenna vastaanottoosoite*".

![Image](assets/fr/68.webp)

Skannaa Envoyn osoittama osoite passisi avulla.

![Image](assets/fr/69.webp)

Passisi vahvistaa, onko Envoyn tuoma lompakko voimassa. Vahvista se hakemuksessa.

![Image](assets/fr/70.webp)

Voit nyt käyttää lompakkosi julkisia tietoja Envoyssa, mutta bitcoinien käyttämiseen sinun on käytettävä passiasi.

![Image](assets/fr/71.webp)

## Tutustu Passin valikot

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

Voit myös syöttää BIP39-salasanan tai käyttää väliaikaista siementä.

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

## Vastaanottaa bitcoineja

Nyt kun Passport on perustettu, olet valmis vastaanottamaan ensimmäiset satsit uuteen Bitcoin-lompakkoosi. Napsauta Envoyssa "*Primary 0*"-tiliäsi.

![Image](assets/fr/72.webp)

Napsauta "*Vastaanottaa*"-painiketta.

![Image](assets/fr/73.webp)

Envoy-sovellus näyttää lompakossasi ensimmäisen vapaana olevan tyhjän osoitteen. Ennen kuin käytät sitä, tarkistetaan osoite Passport-näytöltä varmistaaksemme, että se todella kuuluu Bitcoin-lompakkoomme. Valitse Passportin "*Tili*"-valikosta "*Tilin työkalut*".

![Image](assets/fr/74.webp)

Napsauta "*Varmista osoite*" ja skannaa sitten Envoyn näyttämä QR-koodi.

![Image](assets/fr/75.webp)

Varmista, että passissa näkyvä osoite vastaa täsmälleen Sparrow'ssa näkyvää osoitetta ja että "*Varmennettu*" on näkyvissä.

![Image](assets/fr/76.webp)

Voit nyt käyttää sitä bitcoinien vastaanottamiseen. Kun transaktio lähetetään verkossa, se näkyy Envoyssa. Odota, kunnes olet saanut tarpeeksi vahvistuksia, jotta voit pitää transaktiota lopullisena.

![Image](assets/fr/77.webp)

## Lähetä bitcoineja

Nyt kun lompakossasi on muutama sati, voit myös lähettää niitä. Tee se klikkaamalla "*lähettää*" -painiketta.

![Image](assets/fr/78.webp)

Syötä vastaanottajan osoite joko suoraan tai skannaamalla QR-koodi älypuhelimen kameralla.

![Image](assets/fr/79.webp)

Määritä summa, jonka haluat lähettää, ja napsauta sitten "*Vahvista*".

![Image](assets/fr/80.webp)

Valitse transaktiomaksu nykyisen markkinatilanteen mukaan ja tarkista sitten transaktiotiedot. Jos kaikki on oikein, napsauta "*Allekirjoita passilla*".

![Image](assets/fr/81.webp)

Lisää tapahtumalle etiketti, jotta sen tarkoitus voidaan kirjata selkeästi.

![Image](assets/fr/82.webp)

Envoy näyttää sitten PSBT:n (*Partially Signed Bitcoin Transaction*). Sovellus on muodostanut transaktion, mutta siitä puuttuu vielä allekirjoitus(t), jolla syötössä käytetyt bitcoinit voidaan avata. Nämä allekirjoitukset voi suorittaa vain Passport, joka isännöi siemenesi ja antaa pääsyn transaktion allekirjoittamiseen tarvittaviin yksityisiin avaimiin.

![Image](assets/fr/83.webp)

Siirry Passportissasi "*Tili*"-valikkoon ja napsauta "*Allekirjoita QR-koodilla*".

![Image](assets/fr/84.webp)

Skannaa Envoyn näyttämä PSBT (*Partially Signed Bitcoin Transaction*).

![Image](assets/fr/85.webp)

Vahvista, että vastaanottava osoite ja lähetetty summa ovat oikein, ja paina sitten vahvistuspainiketta.

![Image](assets/fr/86.webp)

Tarkista vaihto-osoite. Esimerkissäni sitä ei ole, koska tapahtuma sisältää vain yhden tulosteen.

![Image](assets/fr/87.webp)

Varmista, että maksu on valitsemasi.

![Image](assets/fr/88.webp)

Jos kaikki tiedot ovat oikein, allekirjoita maksutapahtuma napsauttamalla vahvistuspainiketta.

![Image](assets/fr/89.webp)

Passisi näyttää allekirjoitetun maksutapahtuman QR-koodin muodossa.

![Image](assets/fr/90.webp)

Napsauta Envoy-sovelluksessa QR-koodikuvaketta ja skannaa sitten passin näytöllä näkyvä PSBT.

![Image](assets/fr/91.webp)

Tarkista maksutapahtuman tiedot vielä kerran. Jos kaikki on oikein, paina "*Send Transaction*" lähettääksesi sen Bitcoin-verkkoon.

![Image](assets/fr/92.webp)

Tapahtumasi odottaa nyt vahvistusta. Voit seurata sen tilaa suoraan tililtäsi.

![Image](assets/fr/93.webp)

Onneksi olkoon, tiedät nyt, miten Passport asetetaan ja miten sitä käytetään Envoy-sovelluksen kanssa. Jos tämä opetusohjelma oli mielestäsi hyödyllinen, olisin kiitollinen, jos jättäisit vihreän peukalon alle. Voit vapaasti jakaa tätä artikkelia sosiaalisissa verkostoissa. Kiitos jakamisesta!

Lisätietoja on Liana-ohjelmiston oppaassa:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
