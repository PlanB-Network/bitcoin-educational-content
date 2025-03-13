---
name: GrapheneOS

description: GrapheneOS-opas
---

> "[GrapheneOS](https://grapheneos.org/) on yksityisyyteen ja turvallisuuteen keskittyvä mobiilikäyttöjärjestelmä, joka on yhteensopiva Android-sovellusten kanssa ja kehitetty voittoa tavoittelemattomana avoimen lähdekoodin projektina."

GrapheneOS perustettiin alun perin vuonna 2014 nimellä 'CopperheadOS'. Se pohjautuu perinteiseen Android-koodiin (AOSP), mutta sisältää monia muutoksia ja parannuksia, jotka tähtäävät käyttäjän yksityisyyden ja turvallisuuden parantamiseen. GrapheneOS antaa käyttäjälle hallinnan puhelimestaan, ei suurille teknologiayrityksille.

### Sisällysluettelo:

- Johdanto
- Valmistelu
- Asennus
- Sovellusvaihtoehdot
- Haittapuolet
- Hyödyllistä tietoa

Opas osoitteessa https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md

## Miksi käyttää GrapheneOS:ää?

Nykyajan puhelimet ovat 500–1000 dollarin hintaisia seuranta- ja datankeruulaitteita. Kaikki elämämme osa-alueet kulkevat niiden kautta, ja valitettavasti suuri osa tästä tiedosta jaetaan jossain muodossa kolmansille osapuolille.
GrapheneOS on suunniteltu erityisesti vähentämään tätä tiedonjakoa ja parantamaan laitteesi turvallisuutta mahdollisilta hyökkäysvektoreilta. GrapheneOS-tiliä ei ole olemassa. Et tarvitse sellaista sovellusten lataamiseen tai käyttöjärjestelmän kanssa vuorovaikutuksessa. Yksinkertaisesti sanottuna, sinä et ole tuote.

GrapheneOS tarjoaa lisäturvallisuutta Android-kokemukseesi muutamien yksinkertaisten perusperiaatteiden kautta.

1. **Hyökkäyspinnan vähentäminen** - Tarpeettoman koodin (tai bloatwaren) poistaminen.
2. **Haavoittuvuuden altistumisen ehkäisy** - Käyttäjälle annetaan tarpeeksi valinnanvaraa, jotta he voivat päättää, minkä kompromissien kanssa ovat mukavia.
3. **Hiekkalaatikon rajoittaminen** - GrapheneOS vahvistaa olemassa olevia Android-hiekkalaatikoita, lukiten entisestään kunkin sovelluksen kyvyn kommunikoida loppupuhelimen kanssa.

Lue lisää GrapheneOS:n teknisten ominaisuuksien yksityiskohdista [täältä](https://grapheneos.org/features).

### Siirtymisen helpottaminen

Jos olet ollut vuosia syvällä Googlen tai Applen ekosysteemissä, ajatus kaiken mukavuuden menettämisestä yhdessä yössä voi olla pelottava. Mutta huolellisesti harkituilla sovellusasennuspäätöksillä (käsitellään myöhemmin) suurin osa tästä odotetusta vaikeudesta voidaan vähentää tai poistaa.

Vaikka vaihtoehdot paranevat, ajatus tällaisesta muutoksesta voi silti olla epämiellyttävä. Jos löydät itsesi tästä tilanteesta, paras neuvoni on käyttää uutta GrapheneOS-laitettasi rinnakkain olemassa olevan puhelimesi kanssa jonkin aikaa. Siitä lähtien voit vähitellen vieroittaa itsesi 2-3 sovelluksesta viikossa, kunnes huomaat tavoittelevasi vain GrapheneOS-laitettasi.

Jos otat tämän lähestymistavan, ole itsellesi tiukka ja katkaise riippuvuutesi valvotuista vaihtoehdoista mahdollisimman pian. Me ihmiset olemme laiskoja ja valitsemme usein vähiten vastustuksen tien. Muista, miksi teit vaihdon alun perin.

**Sen sijaan, että maksaisit henkilökohtaisilla tiedoillasi, päätit maksaa ajallasi ja joskus kovalla työllä ansaitsemallasi rahalla (riippuen asentamistasi vaihtoehtoisista sovelluksista).**

## Aloittaminen

GrapheneOS on tällä hetkellä tuotannossa vain _(ironista kyllä)_ [Google Pixel](https://grapheneos.org/faq#supported-devices) -puhelimille. Tähän on kuitenkin hyvä syy. Pixel tarjoaa parhaan laitteistopohjaisen turvallisuuden täydentämään käyttöjärjestelmän kovettamistyötä. Tähän sisältyy esimerkiksi tiettyjen komponenttien eristäminen ja varmennettu käynnistys.

### Laitteen valinta

Valitessasi Pixel-laitetta, johon haluat asentaa GrapheneOS:n, varmista, että tarkistat kuinka kauan laite jatkaa oletusarvoisten [turvapäivitysten](https://support.google.com/pixelphone/answer/4457705?hl=fi#zippy=%2Cpixel-xl-a-a-g-a-g) saamista.
Kirjoitushetkellä Pixel 6a on saatavilla olevista malleista edullisin, jolla on hyvä pitkän aikavälin tuki, taattu aina heinäkuuhun 2027 asti. Jos valitset tämän mallin, OEM-lukituksen avaaminen ei toimi tehtaalta tulevan käyttöjärjestelmän version kanssa. Sinun on päivitettävä se kesäkuun 2022 julkaisuun tai myöhempään ilmateitse tehtävän päivityksen kautta. Päivityksen jälkeen sinun on myös tehtävä laitteelle tehdasasetusten palautus korjataksesi OEM-lukituksen avaamisen. Kaikki muut operaattorilukitsemattomat mallit ovat valmiita GrapheneOS:lle suoraan paketista.

Laitetta valitessasi haluat myös varmistaa, että ostat lukitsemattoman version. Tietyt operaattorit, kuten Verizon, toimittavat yksiköitä, jotka ovat bootloader-lukittuja, mikä estää täysin seuraavan prosessin.

### GrapheneOS:n asentaminen

GrapheneOS:n [web-asennusohjelma](https://grapheneos.org/install/web) tekee koko prosessista tuulen, ja sen voi suorittaa kuka tahansa alle 10 minuutissa.
Seuraavat ohjeet ovat lyhennetty versio yllä olevasta linkistä.

Tarvitset vain:

- Pixel-laitteen
- USB-kaapelin puhelimesta tietokoneeseen
- Tietokoneen, jossa on web-selain (mikä tahansa Chromium-pohjainen selain: Chrome, Edge, Brave jne.)

1. Ensimmäinen askel on mennä kohtaan **Asetukset** > **Tietoja puhelimesta** ja toistuvasti napauttaa rakennusnumeroa, kunnes näet, että **'Kehittäjätila'** on aktivoitu.
2. Seuraavaksi siirry kohtaan **Asetukset** > **Järjestelmä** > **Kehittäjäasetukset** ja ota käyttöön **'OEM-lukituksen avaaminen'**.
3. Käynnistä laite uudelleen ja pidä äänenvoimakkuuden vähennyspainiketta alhaalla, kun puhelin käynnistyy uudelleen.
4. Yhdistä puhelin kannettavaan tietokoneeseesi ja jos yhteyden muodostamista pyydetään vahvistamaan, salli yhteys.
5. Web-asennusohjelman sivulla, klikkaa 'Avaa bootloader'.
6. Näet sitten puhelimen vaihtoehdot muuttuvan. Käytä äänenvoimakkuuspainiketta vaihtaaksesi valintaa `unlock` ja käytä virtapainiketta hyväksyäksesi.
7. Seuraavaksi klikkaa lataa julkaisu web-asennusohjelman sivulla.
8. Kun se on täysin ladattu, siirry seuraavaan vaiheeseen ja klikkaa 'Väläytä julkaisu'. Tämä kestää minuutin tai kaksi, eikä sinun tarvitse koskea puhelimeen ollenkaan.
9. Lopuksi, siirry web-asennusohjelman seuraavaan vaiheeseen ja klikkaa **Lukitse Bootloader**. Sinun on muutettava valintaa ja vahvistettava virtapainikkeella samalla tavalla kuin aiemmin prosessissa.
10. Kun näet sanan `Start`, vahvista tämä virtapainikkeella ja laite käynnistyy uuteen Google-vapaaseen käyttöjärjestelmään.

![kuva](assets/2.webp)

GrapheneOS:n aloitusnäyttö

_Aloituskäynnistyksen ja asetusten määrittämisen jälkeen on hyvä käytäntö poistaa OEM-lukituksen avaaminen käytöstä kohdassa Asetukset > Järjestelmä > Kehittäjäasetukset._

_Saatat myös haluta ottaa ylimääräisen, valinnaisen mutta suositellun askeleen asennuksen tarkistamiseksi Auditor-sovelluksen kautta. Tämän vaiheen suorittamiseen tarvitset erillisen Android-puhelimen, jossa sovellus on asennettuna. Ohjeet tähän löytyvät [täältä](https://attestation.app/tutorial)._

![video](https://www.youtube.com/embed/L1KZWjZVnAw)

Video, joka yksityiskohtaisesti kuvaa yllä mainitut yksinkertaiset vaiheet

Jos nämä yksinkertaiset vaiheet vaikuttavat liian monimutkaisilta, voit harkita Pixelin ostamista, jossa GrapheneOS-ohjelmisto on [esiasennettuna](https://ronindojo.io/en/roninmobile). Huomaa vain, että luotat tällöin pienen määrän toimittajaan.

### Esiasennetut Sovellukset

Kun olet asentanut järjestelmän, saatat huomata, kuinka paljas GrapheneOS näyttää ensiasennuksen jälkeen. Oletuksena sinulla on nämä sovellukset asennettuna:

![kuva](assets/3.webp)

Oletussovellukset
Vain kaksi termiä saattavat olla sinulle tuntemattomia: 'Auditor' ja 'Vanadium'.
- '[Auditor-sovellus](https://play.google.com/store/apps/details?id=app.attestation.auditor) käyttää laitteistopohjaisia turvaominaisuuksia laitteen identiteetin sekä käyttöjärjestelmän aitouden ja eheyden varmentamiseen. Se tarkistaa, että laite käyttää alkuperäistä käyttöjärjestelmää, että sen käynnistyslataaja on lukittu ja että käyttöjärjestelmään ei ole tehty muutoksia.'
- [Vanadium](https://github.com/GrapheneOS/Vanadium) on yksityisyyttä ja turvallisuutta parannettu versio Chromium-selaimesta.

## Mukauttaminen

Puhelimen asetukset ovat henkilökohtainen asia, mutta tässä on joitakin ensimmäisiä asioita, joita muutan asentaessani GrapheneOS:n, jotta tunnen oloni kotoisammaksi.

### Taustakuvan asettaminen ja teeman päivittäminen

Siirry kohtaan Asetukset > Taustakuva ja tyyli. Täältä minä:

- Päivitän koti- ja lukitusnäytön taustakuvat webistä ladatuilla kuvilla.
- Valitsen käyttöliittymän läpi käytettävät korostusvärit.
- Otan käyttöön tumman teeman.

### Näytä akun prosenttiosuus

Siirry kohtaan **Asetukset** > **Akku**, ja ota käyttöön **Näytä akun prosenttiosuus** tilapalkissa.

### Yhteystietojen tuonti

**Toisesta Android-puhelimesta** - Siirry Yhteystiedot-sovellukseen ja etsi Vie VCF-muodossa -vaihtoehto.

**iOS:stä** - Käytä sovellusta kuten Export Contact ja käytä 'vCard' vientivaihtoehtoa yhteystietojen viemiseen VCF-tiedostona.
Kun sinulla on VCF-tiedosto, voit siirtää sen GrapheneOS-laitteeseesi ulkoisen tallennusvaihtoehdon, kuten microSD-kortin tai USB-aseman avulla. Jos sinulla ei ole mitään näistä käytettävissä, voit valita jakamisen monien alla mainittujen sovellusten kautta.

![kuva](assets/4.webp)

Henkilökohtainen kotinäyttö

## Vaihtoehtoiset Sovellukset

Jotta puhelimesi olisi hyödyllinen, haluat asentaa joitakin sovelluksia! Seuraavat vaihtoehdot on sisällytetty, koska olen käyttänyt niitä kaikkia henkilökohtaisesti tai koska ne saavat vahvoja suosituksia laajemmalta yksityisyyden suojan yhteisöltä. Monia muita hienoja vaihtoehtoja, joita ei mainita, on saatavilla, ja [Awesome Privacy](https://awesome-privacy.xyz) tarjoaa uskomattoman kattavan luettelon yksityisyyttä suojaavista sovelluksista kaikenlaisille laitteille.

Se, että sovellus on vapaan ja avoimen lähdekoodin ohjelmisto (FOSS), ei tarkoita, että se olisi vapaa mahdollisista yksityisyyden vuodoista. Käytä [Exodus](https://reports.exodus-privacy.eu.org/en/) -palvelua nähdäksesi, miten valitsemasi sovellukset pärjäävät niiden yksityisyyden suojan auditoinneissa.

### F-Droid

[F-Droid](https://f-droid.org/) on asennettava katalogi FOSS-sovelluksista Androidille. Asiakasohjelma tekee sovellusten selaamisesta, asentamisesta ja päivittämisestä laitteellasi helppoa. On mainitsemisen arvoista, että päivitykset F-Droidin kautta voivat joskus olla hitaampia kuin muiden sovelluskauppojen kautta. Tämä riippuu pääasiassa siitä, löytyykö sovellus pää-F-Droid-repositoriosta vai erillisestä.

F-Droidin asentamiseksi mene vain heidän verkkosivuilleen GrapheneOS-puhelimellasi ja napauta lataa. Tämä lataa `.apk`-tiedoston. Sinulta kysytään sitten, haluatko asentaa sovelluksen.

F-Droidin oletusrepositoriossa löytyvien sovellusten lisäksi monet avoimen lähdekoodin projektit isännöivät myös omaa repositoriotaan, joka voidaan lisätä F-Droid-sovelluksen asetuksissa. Jos näin on, kyseinen projekti opastaa sinut läpi tarvittavat erittäin yksinkertaiset vaiheet heidän verkkosivuillaan.

![kuva](assets/5.webp)

F-Droidin kotinäyttö

### Aurora Store
[Aurora Store](https://auroraoss.com/) on FOSS-versio Google Play -kaupasta. Aurora näyttää ja tuntuu hyvin samanlaiselta kuin perinteinen Play Kauppa ja mahdollistaa minkä tahansa sovelluksen lataamisen ja päivittämisen, jonka normaalisti löytäisit Google-vaihtoehdon kautta.
Auroran tappava ominaisuus on nimetön kirjautuminen. Tämä tarkoittaa, että voit ladata mitä tahansa suosikkisovelluksiasi, joita ei ole saatavilla F-Droidin tai suoran APK:n kautta, ilman että sinun tarvitsee olla kirjautuneena Google-tilillesi.

Ennen kuin kiirehdit tekemään tästä oletusasennusvaihtoehtosi, muista, että monet sovelluksista, joista yritämme päästä eroon, on asennettu Play Kaupasta. Pelkkä niiden saatavuus Aurorasta ei muuta sitä tosiasiaa, että jotkut saattavat sisältää seurantaominaisuuksia. Se ei aina ole mahdollista, mutta aina kun voit, etsi F-Droid-vaihtoehto ennen lataamista Auroran kautta.

Auroran asentaminen on yksinkertaista, etsi vain 'Aurora Store' F-Droidista.

Auroralla on myös joitakin mahdollisia hyökkäysvektoreita, sillä "nimettömät tilit" luodaan ja hallitaan todellisuudessa Auroran toimesta. Teoriassa ne voivat tarjota haitallisia päivityksiä tai työntää sovelluksia puhelimeesi, vaikka sinun silti täytyisi hyväksyä asennuskehotus laitteessa. Aurora kohtaa myös joskus ongelmia sovellusten näkymättömyyden kanssa alue- ja laitevirheiden vuoksi. Tämän voi yleensä kiertää alla olevilla vaiheilla.

**Huippuvinkki** - Joskus Aurora Store voi kohdata rajoitusongelmia, jotka rajoittavat kykyäsi etsiä ja asentaa sovelluksia. Tämän kiertämiseksi mene kohtaan **Asetukset** > **Sovellukset** > **Aurora** > **Avaa oletuksena**, lisää sitten domain `play.google.com`. Nyt, kun navigoit tuotteen tai palvelun verkkosivustolle, jolla on 'Lataa Play Kaupasta' -linkki, napauttaminen avaa kyseisen sovelluksen Aurorassa latausta varten.

![kuva](assets/6.webp)

Aurora Storen kotinäyttö

### APK-lataus

Android-sovelluksia voi myös ladata ja asentaa `.apk`-tiedoston kautta. Tämä on loistava vaihtoehto, joka ei vaadi kolmannen osapuolen sovelluskauppoja, lataa tiedosto suoraan projektin tai palvelun verkkosivustolta tai GitHub-repositoriosta.

Tämän lähestymistavan haittapuoli on, että automaattisia päivityksiä ei saada, joten sinun on seurattava kyseisen palvelun viestintäkanavia uusien julkaisujen oppimiseksi. On kuitenkin olemassa loistava projekti nimeltä Obtanium, joka pyrkii korjaamaan tämän. [Obtainium](https://github.com/ImranR98/Obtainium) mahdollistaa avoimen lähdekoodin sovellusten asentamisen ja päivittämisen suoraan niiden julkaisusivuilta ja ilmoitusten vastaanottamisen, kun uusia julkaisuja on saatavilla.

![kuva](assets/7.webp)

Obtainium-esikatselu

### Web-sovellukset

Niinä aikoina, kun haluat käyttää palvelua harvoin etkä halua ladata natiivia sovellusta, voit yksinkertaisesti käyttää web-versiota. Monet verkkosivustot tarjoavat nykyään myös Progressive Web App (PWA) -tukea. Tämä tarkoittaa, että voit lisätä tietyn verkkosivuston (esim. Twitter.com) kirjanmerkiksi puhelimesi kotinäyttöön. Kun napautat kuvaketta, se avautuu täysikokoisena sovelluksena ilman tyypillisen selainkokemuksen häiriötekijöitä. Alla näet esimerkin siitä, miltä tämä näyttää.

Tämän saavuttamiseksi Vanadiumissa, GrapheneOS:n natiivissa selaimessa, navigoi valitsemallesi verkkosivustolle, napauta kolmea pystypistettä näytön oikeassa yläkulmassa ja sitten napauta **'Lisää kotinäyttöön'**.

Tämän lähestymistavan ainoa haittapuoli on, että koska kyseessä on vain kirjanmerkitty verkkosivu, et saa minkäänlaista ilmoitusta. Vaikka jotkut saattavat pitää tätä positiivisena!

![kuva](assets/8.webp)

Twitter PWA

### Verkkoselaimet
Et voi oikeastaan mennä pieleen esipakatun vaihtoehdon, Vanadiumin, kanssa. Sovellus käyttäytyy identtisesti mihin tahansa muuhun mobiiliselaimeen verrattuna, jota olen kokeillut, eikä minulla ole ollut kertaakaan yhteensopivuusongelmia.
Kun tarvitset pääsyä Torin natiiveihin `.onion` sivustoihin, voit ladata Tor-selaimen APK:n suoraan heidän [verkkosivustoltaan](https://www.torproject.org/download/#android) tai F-Droidin kautta.

### VPN:t

Suojataksesi online-toimintasi uteliaalta internet-palveluntarjoajaltasi (ISP), Virtuaalinen Yksityisverkko (VPN) -sovellus on hyvä vaihtoehto. VPN lähettää internet-liikenteesi salatussa tunnelissa jaettuun IP-osoitteeseen, jota VPN-palveluntarjoaja hallitsee varmistaakseen, että laitteesi toimintaa ei voida yhdistää sinuun.

Seuraavat ovat 3 hyvin arvostettua vaihtoehtoa, jotka sallivat palvelun maksamisen Bitcoinilla ilman henkilökohtaisten tietojen antamista. Kaikki 3 vaihtoehtoa ovat saatavilla F-Droidin kautta.

- [Mullvad](https://f-droid.org/packages/net.mullvad.mullvadvpn/)
- [Proton](https://f-droid.org/en/packages/ch.protonvpn.android/)
- [iVPN](https://f-droid.org/en/packages/net.ivpn.client/)

### Viestintä

Viime vuosina salattujen viestintäratkaisujen määrä on kasvanut runsaasti. Ongelmana kuitenkin on, että vaikka sinulla olisi puhelimessasi paras ja yksityisin vaihtoehto, mikä on sen pointti, jos sinulla ei ole yhteyksiä, jotka sitä käyttävät?

Useimmat ihmiset, jotka eivät ole kiinnostuneita yksityisyyden alueesta, todennäköisesti käyttävät WhatsAppia tai iMessagea. Edellinen voidaan ladata Aurora Storen kautta, mutta jälkimmäinen ei toimi GrapheneOS:ssä (ilmeisesti!).

- [Signal](https://signal.org/) on yksi suosituimmista päästä päähän salatuista (E2EE) viestisovelluksista, jolla on vahva track record ja rikas ominaisuussetti. Signal vaatii puhelinnumeron rekisteröitymiseen, joten jos aiot keskustella ihmisten kanssa, jotka mieluummin eivät tietäisi puhelinnumeroasi, ehkä tutustu joihinkin vaihtoehtoihin. Signal on ladattavissa Aurora Storen kautta.
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) on melko uusi E2EE-viestisovellus. Sillä ei ole käyttäjä-ID:tä, se ei vaadi puhelinnumeroa tai henkilökohtaisia tietoja. Ihmiset löytävät sinut skannaamalla henkilökohtaisen QR-koodisi tai vierailemalla ainutlaatuisessa linkissäsi. Simplex sallii myös edistyneiden käyttäjien pyörittää omaa palvelintaan vähentääkseen riippuvuutta mistään keskitetystä entiteetistä. Simplexillä ei ole työpöytäasiakasta, joten se ei ehkä sovi, jos monilaitetuki on prioriteettilistallasi. Simplex Androidille on saatavilla F-Droidin kautta.
- [Threema](https://threema.ch/en/faq/libre_installation) tarjoaa samankaltaisen kokemuksen kuin Simplex, mutta on ollut olemassa pidempään ja sen seurauksena tuntuu hieman viimeistellymmältä. Threema ei ole ilmainen, elinikäinen lisenssi maksaa 4,99 dollaria ja sen voi ostaa Bitcoinilla. Threema tarjoaa web-asiakkaan ja natiivit työpöytäsovellukset. Android-sovellus on saatavilla F-Droidin kautta.
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) on virallisen Telegram-sovelluksen epävirallinen FOSS-haara Androidille. Telegramilla on E2EE 'salaiset keskustelut', mutta oletusvaihtoehto ei ole yksityinen. Telegram FOSS on ladattavissa F-Droidista.

![kuva](assets/9.webp)
Vasemmalla: Threema
Oikealla: Simplex

### Media
- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/) on alustojen välinen Spotify-asiakasohjelma, joka ei vaadi Premium-tiliä. Spotube on saatavilla F-Droidin kautta.
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/) on fantastinen sovellus, jolla voi striimata mitä tahansa musiikkia YouTube Musicista ilmaiseksi. ViMusic on saatavilla F-Droidista.
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/) tarjoaa YouTube-kokemuksen ilman ärsyttäviä mainoksia ja kyseenalaisia käyttöoikeuksia. NewPipen avulla voit tilata kanavia, kuunnella taustalla ja jopa ladata katsottavaksi offline-tilassa. NewPipe on saatavilla F-Droidin kautta.
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/) on podcast-soitin, jonka avulla voit tilata ja hallita kaikkia lempiohjelmiasi. AntennaPod on saatavilla F-Droidista.

![kuva](assets/11.webp)

Vasemmalla: Spotube
Oikealla: ViMusic

### Kartat

Jos haluat ääniavustusta ajaessasi ja käyttäessäsi karttasovellusta GrapheneOS:ssä, sinun tulee asentaa [RHVoice](https://rhvoice.org/installation/) ja [määrittää](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available) se.

- [Magic Earth](https://www.magicearth.com/) on karttasovellusvaihtoehto, joka tukee käännös käännökseltä -navigointia, 3D- ja offline-karttoja. Magic Earthin voi ladata Aurora Storesta.
- [Organic Maps](https://f-droid.org/en/packages/app.organicmaps/) on karttasovellusvaihtoehto matkailijoille, turisteille, vaeltajille ja pyöräilijöille, joka perustuu joukkoistettuun OpenStreetMap-tietoon. Se on yksityisyyteen keskittyvä, avoimen lähdekoodin haara Maps.me-sovelluksesta (aiemmin tunnettu nimellä MapsWithMe). Se tukee 100% ominaisuuksista ilman aktiivista internet-yhteyttä ja sen voi ladata F-Droidista.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) on toinen loistava karttasovellusvaihtoehto, joka tukee kaikkia edellä mainittuja ominaisuuksia.

![kuva](assets/13.webp)

Vasemmalla: Magic Earth
Oikealla: Organic Maps

### Sähköposti

- [Proton Mail](https://proton.me/mail) tarjoaa ilmaisen yksityisen sähköpostipalvelun, joka tukee auditoitua E2EE:tä. Proton tarjoaa myös maksullisen version, joka tukee mukautettuja domaineja ja [aliaksia](https://proton.me/support/creating-aliases). Proton Mailin voi ladata suorana APK-tiedostona tai Aurora Storen kautta.
- [Tutanota](https://tutanota.com/) tarjoaa samat ominaisuudet kuin Proton Mail, mukaan lukien valinnaiset maksulliset palvelut, ja sen voi ladata suorana APK-tiedostona tai F-Droidin kautta.
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/) on avoimen lähdekoodin sähköpostiasiakas, joka toimii käytännössä kaikkien sähköpostipalveluiden kanssa. Se tukee useita tilejä, yhtenäistä postilaatikkoa ja OpenPGP-salausstandardia.

![kuva](assets/15.webp)

Vasemmalla: Proton Mail
Oikealla: Tutanota

### Tuottavuus

- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/) on tiedostojen synkronointiohjelma. Se synkronoi tiedostoja reaaliajassa kahden tai useamman laitteen välillä, suojattuna uteliailta silmiltä. Tietosi ovat vain sinun tietojasi, ja sinulla on oikeus päättää, missä ne säilytetään, jaetaanko ne kolmannen osapuolen kanssa ja miten ne siirretään internetin yli. Syncthing on saatavilla F-Droidin kautta.
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/) mahdollistaa laitteidesi saumattoman kommunikoinnin kotiverkossasi. Voit helposti lähettää tiedostoja, valokuvia ja leikepöydän tietoja kaikkien laitteidesi välillä (myös iOS:ssä!). KDE Connectin voi ladata F-Droidista.
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/) on E2EE-muistiinpanosovellus, joka synkronoi ajatuksesi ja to-do-listasi kaikille laitteillesi. Heidän ilmainen suunnitelmansa kattaa useimmat henkilökohtaiset käyttötapaukset. Notesnook on saatavilla F-Droidista.
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/) on hyvin samankaltainen kuin Notesnook, mutta vaatii maksullisen suunnitelman vastaavan ominaisuusjoukon saavuttamiseksi. Standard Notes on saatavilla F-Droidin kautta.
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) on näppäimistösovellus, joka mahdollistaa lähes minkä tahansa mukauttamisen, kun on kyse puhelimen kirjoituskokemuksesta. Sen voi ladata F-Droidin kautta.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) on Googlen oletusnäppäimistösovellus. Kokemukseni mukaan se tarjoaa ehdottomasti parhaan kirjoitus- ja pyyhkäisykokemuksen. Jos lataat tämän sovelluksen, varmista, että kaikki verkkoon liittyvät luvat on kokonaan poistettu käytöstä. Sen voi ladata Aurora-kaupan kautta.

![kuva](assets/17.webp)

Vasemmalla: Notesnook
Oikealla: KDE Connect

### Elämäntapa

- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/) on kauniisti suunniteltu avoimen lähdekoodin sääsovellus, joka on saatavilla F-Droidin kautta. Se tukee myös monia eri kokoisia widgettejä, joten voit nähdä valitsemasi sijainnin sään suoraan kotinäytöltäsi.
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) on avoimen lähdekoodin ja yksityisyyttä suojaava käännössovellus, joka tukee yli 200 kieltä. Translate You on saatavilla F-Droidin kautta.
- [Proton Calendar](https://proton.me/calendar/download) on helppokäyttöinen E2EE-kalenteri, joka toimii saumattomasti yhdessä Proton-sähköpostitiliesi kanssa. Proton Kalenterin voi ladata APK-tiedostona tai Aurora-kaupan kautta.
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/) on sovellus, jolla voi näyttää ja säilyttää koneeseen nousukortteja, kuponkeja, elokuvalippuja ja jäsenkortteja jne. Lataa vain asiaankuuluva `pkpass` tai `espass` tiedosto ja avaa sovelluksessa. PassAndroid on saatavilla F-Droidin kautta.

![kuva](assets/19.webp)
Vasemmalla: Geometric Weather
Oikealla: Proton Calendar

### Turvallisuus/Yksityisyys

- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) tarjoaa ilmaisen ja E2EE:n läpi suojatun alustojen välisen salasananhallintaratkaisun kaikille laitteillesi. Heidän maksullinen palvelunsa mahdollistaa 2FA-koodien integroinnin sovellukseen. Bitwardenin palvelinpuoli voidaan hostata itse ja Android-sovellus on saatavilla F-Droidin kautta.
- [Proton Pass](https://proton.me/pass/download) tarjoaa samankaltaisen ilmaisen palvelun kuin Bitwarden, mutta [Proton Unlimited](https://proton.me/pricing) asiakkaat pääsevät käsiksi lisäominaisuuksiin. Proton Pass on saatavilla APK:n tai Auroran kautta.
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/) on kaksivaiheisen tunnistautumisen sovellus järjestelmiin, jotka käyttävät kertakäyttöisiä salasanoja. Tokeneita voi lisätä helposti skannaamalla QR-koodin. FreeOTP on saatavilla F-Droidin kautta.
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/) on ilmainen, turvallinen ja avoimen lähdekoodin sovellus Androidille hallitaksesi 2-vaiheisen tunnistautumisen tokeneita online-palveluissasi. Aegis on saatavilla F-Droidin kautta.
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/) on maksullinen, alustojen välinen palvelu, joka salaa tietosi paikallisesti, jotta voit turvallisesti ladata ne suosikki pilvipalveluusi. Cryptomator on ladattavissa F-Droidin kautta.

![kuva](assets/21.webp)
Vasemmalla: Proton Pass
Oikealla: Bitwarden

### Pilviratkaisut

- [Proton Drive](https://proton.me/drive/download) on maksullinen E2EE-pilviratkaisu kaikkien tiedostojesi varmuuskopiointiin ja tallentamiseen. Kirjoitushetkellä he ovat juuri ilmoittaneet Windows-työpöytäasiakkaasta, mutta Mac- ja Linux-käyttäjien on toistaiseksi jatkettava web-version käyttöä tietokoneiltaan synkronointiin (toistaiseksi). Android-asiakasohjelma on saatavilla APK:nä tai Auroran kautta.
- [Skiff](https://skiff.com/download) tarjoaa myös maksullista E2EE-pilvitallennusta ja tiedostoyhteistyötyökaluja. He tarjoavat Mac- ja Windows-työpöytäasiakkaan (sekä web-sovelluksen) ja heidän Android-asiakasohjelmansa on ladattava Aurorasta.
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/) tarjoaa täysin varustellun pilvipohjaisen ratkaisun yhteistyöhön, laitteiden väliseen synkronointiin ja tiedostojen tallennukseen. Kokeneemmat käyttäjät voivat valita isännöidä heidän vapaan ja avoimen lähdekoodin ohjelmistonsa millä tahansa haluamallaan laitteistolla. Android-asiakasohjelmat voi ladata F-Droidin kautta.
- [Cryptpad](https://cryptpad.fr/) tarjoaa ilmaisen, web-pohjaisen, E2EE-vaihtoehdon Google Docsille.

![kuva](assets/23.webp)

Proton Drive

## Haittapuolet

Avoimen lähdekoodin ja yksityisyyttä suojaavat vaihtoehdot teknologiajättien sovelluksille, joihin olet tottunut käyttämään, ovat runsaat, ja jotkut niistä ovat usein parempia kuin suljetun lähdekoodin, vakoiluohjelmilla täytetyt vaihtoehdot.

Siirtyessäsi GrapheneOS-käyttöjärjestelmään, on kuitenkin joitakin mukavuuksia, joista sinun on luovuttava, koska vaihtoehtoja ei ole. Näihin kuuluvat:

- **Apple CarPlay/Android Auto** - Sinun on tyydyttävä vanhaan kunnon Bluetoothiin, USB:hen tai Auxiin.
- **Apple/Google Pay** - Lähes kaikki kantavat lompakkoaan mukanaan joka tapauksessa!
- **Pankkisovellukset** - Ei niin, että nämä eivät toimisi ollenkaan. Jotkut toimivat, täydellisesti itse asiassa. Toiset toimivat vain, jos Google Play Palvelut on otettu käyttöön (lue lisää tästä alla) ja toiset eivät toimi ollenkaan. Lue raportti pankistasi [täältä](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/) nähdäksesi nykytilanteen. Älä huoli, jos omasi on listalla, joka ei toimi, muista, että voit vain tallentaa URL:n web-sovelluksena kotinäytöllesi.
- **Push-ilmoitukset** - Useimmat sovellukset, jotka lähettävät sinulle päivityksiä käyttämättä tiettyä sovellusta, tekevät niin Google Play Palveluiden kautta. Nämä eivät ole oletusarvoisesti asennettuna GrapheneOS:ssä, joten jos huomaat, ettei sinulle ilmoiteta välittömästi, kun ystäväsi lähettää sinulle sähköpostia, tämä on todennäköisesti syy. Hyvä uutinen on, että jotkut yllä mainituista sovelluksista ovat toteuttaneet oman taustayhteytensä tarkistaakseen päivityksiä ajoittain ja antaakseen sinulle tarvittaessa ilmoituksen

### Hiekkalaatikoitu Google Play
GrapheneOS sisältää yhteensopivuuskerroksen, joka tarjoaa mahdollisuuden asentaa ja käyttää Google Playn virallisia julkaisuja standardissa sovellushiekkalaatikossa. Google Play ei saa GrapheneOS:ssä mitään erityisoikeuksia tai etuoikeuksia verrattuna sovellushiekkalaatikon ohittamiseen ja suuren määrän erittäin etuoikeutettua pääsyä saamiseen.

Jos huomaat, ettet yksinkertaisesti voi elää ilman suosikkisovelluksesi työntöilmoituksia tai tietty "pakko saada" -sovellus on hyödytön ilman Play-palveluita, GrapheneOS mahdollistaa näiden palveluiden asentamisen täysin hiekkalaatikoituun ympäristöön. Asennettuna nämä palvelut eivät vaadi Google-tiliä toimiakseen, ja kunkin palvelun oikeuksia voidaan tiukasti hallita.

Ennen kuin kiirehdit asentamaan näitä ensimmäisenä päivänä, kehotan sinua katsomaan, kuinka pitkälle pääset ilman niitä. Saatat yllättyä siitä, kuinka moni sovellus toimii täysin normaalisti ilman.

Jos haluat asentaa ne, napauta vain esiasennettua "Sovellukset"-sovellusta, jonka jälkeen "Google Play -palvelut". Harkitse niiden asentamista niiden vähemmän yksityisten sovellusten rinnalle, joita et voi elää ilman, täysin erillisessä käyttäjäprofiilissa, jotta saat sen ylimääräisen eristystason puhelimesi muusta sisällöstä.

![kuva](assets/24.webp)

Play-palveluiden asennusnäyttö

### Profiilit

GrapheneOS mahdollistaa erillisen puhelinkokemuksen puhelimessasi. Lisäprofiilit voivat asentaa omat sovelluksensa ja palvelunsa eivätkä ne voi käyttää omistajatilin tiedostoja tai tietoja.
Jos sinulla on vain yksi tai kaksi niistä välttämättömistä sovelluksista, jotka vaativat Play-palveluita, mutta käytät niitä vain harvoin, niiden asentaminen Play-palveluiden kanssa erilliseen profiiliin saattaa olla loistava idea vahvistaa yksityisyyden suojaasi jäljellä olevilta pieniltä yksityisyyden uhkilta, jotka johtuvat niiden ajamisesta omistajaprofiilissa.

Voit lukea lisää tästä käyttötarkoituksesta [täältä](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2).

Jos päätät lisätä erillisen profiilin käyttötarkoitustasi varten, sovellus [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) saattaa olla hyödyllinen sinulle. Insular mahdollistaa minkä tahansa olemassa olevan sovelluksesi helpon kloonaamisen uuteen profiiliin ilman, että sinun tarvitsee käyttää aiemmin oppaassa mainittuja perinteisiä asennusreittejä. Insular mahdollistaa myös minkä tahansa näistä sovelluksista nopean "jäädyttämisen" täysin estääkseen kaikkien kyseisen sovelluksen taustapalveluiden toiminnan.

![kuva](assets/24.webp)

Käyttäjäprofiilien hallintanäyttö

### e-SIM-kortit

Jos haluat viedä puhelimen yksityisyytesi seuraavalle tasolle ja sinulla on matkapuhelinpalvelu, joka ei ole sidoksissa todelliseen henkilöllisyyteesi, eSIM-kortti saattaa olla sinulle sopiva. eSIM on virtuaalinen SIM-kortti, jonka voit ostaa verkosta ja lisätä puhelimeesi QR-koodin avulla. Palveluita, jotka tarjoavat tällaisia palveluita ja joita voidaan maksaa nimettömästi Bitcoinilla, ovat muun muassa [Silent.Link](https://silent.link/) ja [Bitrefill](https://www.bitrefill.com/gb/en/esims/).

eSIM-kortteja ei tulisi pitää täydellisenä ratkaisuna puhelimen yksityisyyteen. Ne voivat olla hyödyllinen työkalu oikeissa käsissä, mutta tee tutkimuksesi [kompromisseista](https://grapheneos.org/faq#cellular-tracking) käyttäessäsi mitä tahansa matkapuhelinpalvelua, jos aikomuksesi on mennä täysin "off grid".

Hiekkalaatikoitujen Play-palveluiden on oltava asennettuna eSIM-kortin määrittämistä varten GrapheneOS:ssä.

## Varmuuskopiot
Kun olet saanut uuden Google-vapaan Pixel-puhelimesi asennettua, on hyvä idea luoda itsellesi varmuuskopio. Tämä varmuuskopio mahdollistaa puhelimen palauttamisen identtiseen tilaan, jos menetät puhelimesi tai se varastetaan.

Voit valita varmuuskopiotiedoston tallennuspaikan mille tahansa ulkoiselle tallennusvälineelle tai itse isännöidylle pilviratkaisulle, kuten Nextcloudille, vaikka jotkut käyttäjät raportoivat vaihtelevista menestystasoista jälkimmäisen vaihtoehdon kanssa.

Luodaksesi ensimmäisen varmuuskopiosi:

1. Siirry kohtaan **Asetukset** > **Järjestelmä** > **Varmuuskopioi**, ja kirjoita ylös 12 sanan palautuskoodisi. Tätä koodia tarvitaan varmuuskopiotiedoston purkamiseen myöhemmässä vaiheessa. Jos menetät koodin, menetät pääsyn puhelimesi varmuuskopioon.
2. Valitse seuraavaksi tallennuspaikkasi. Suosittelisin ulkoista USB-asemaa tai teollisuustason microSD-korttia.
3. Valitse varmuuskopioitavat tiedot. Jos määritellyllä tallennusvälineelläsi on tilaa, suosittelen valitsemaan kaiken.
4. Napauta kolmea pistettä oikeassa yläkulmassa ja valitse **Varmuuskopioi nyt**.

![kuva](assets/26.webp)

Varmuuskopionäyttö

Muista, että jos teet offline-varmuuskopioita ulkoisille tallennusvälineille, on järkevää suorittaa tämä vaihe säännöllisesti varmistaaksesi, että puhelimesi mahdolliset tärkeät päivitykset eivät katoa, jos pahin tapahtuisi.

![video](https://www.youtube.com/embed/eyWmcItzisk)

Video, joka käsittelee varmuuskopiointiprosessia

## Yhteenveto

Viime vuosina GrapheneOS-ohjelmisto on kehittynyt merkittävästi. Se on vakaimpi ja yhteensopivampi kuin koskaan. Yhdistettynä kukoistavaan avoimen lähdekoodin ja yksityisyyttä suojaavien sovellusten ekosysteemiin, GrapheneOS on todellinen vaihtoehto vakio Androidille tai iOS:lle, jopa 'tavallisille' ihmisille juuri kuten sinä!

Tietomurrot ja laajamittainen valvonta ovat nykypäivän maailmassa niin yleisiä, että ne tuskin tekevät enää otsikoita. Sinun on suojeltava itseäsi. Matkalla on tehtävä säätöjä ja uhrauksia, mutta altistumisesi tällaisille loukkauksille vähentäminen ei ole läheskään niin vaikeaa kuin luulet.

Toivon, että tämä opas auttaa sinua matkallasi jollakin tavalla. Jos pidit tätä opasta hyödyllisenä ja haluaisit tukea työtäni, harkitse [lahjoituksen](/tips) lähettämistä.

Jos olet jo GrapheneOS-käyttäjä, tai ryhdyt sellaiseksi tämän oppaan seurauksena, harkitse [lahjoituksen](https://grapheneos.org/donate) lähettämistä heidän tärkeän työnsä tukemiseksi.

### Lue lisää

GrapheneOS on kaninkolo, johon kuka tahansa voisi helposti upota viikkoja. On niin paljon, mitä voit oppia ja säätää kokeillaksesi kokemusta omiin tarpeisiisi ja uhkamalleihisi sopivaksi. Alla on joitakin linkkejä, joista voit jatkaa matkaasi:

- [GrapheneOS Virallinen Käyttöopas](https://grapheneos.org/usage) - Virallinen verkkosivusto
- [GrapheneOS Foorumi](https://discuss.grapheneos.org/) - Virallinen verkkosivusto
- [GrapheneOS Asetusten Mestarikurssi](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - Video 'The Privacy Wayfinder' toimesta
- [GrapheneOS Yleinen Podcast](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - Podcast 'Watchman Privacy' toimesta

täysi tunnustus: https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md