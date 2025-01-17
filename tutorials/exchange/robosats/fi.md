---
name: Robosats

description: Kuinka käyttää Robosatsia
---

![cover](assets/cover.webp)

RoboSats (https://learn.robosats.com/) on helppo tapa vaihtaa Bitcoinia yksityisesti kansallisiin valuuttoihin. Se yksinkertaistaa vertaisverkkokokemusta ja hyödyntää salamalaskutusta vähentääkseen hallinnan ja luottamuksen tarvetta.

![video](https://youtu.be/XW_wzRz_BDI)

## Opas

> Tämä opas on peräisin Bitocin Q&A:sta (https://bitcoiner.guide/robosats/). Kaikki kunnia hänelle, tue häntä siellä (https://bitcoiner.guide/contribute); BitcoinQ&A on myös bitcoin-mentor. Ota yhteyttä häneen saadaksesi mentorointia!

![image](assets/0.webp)

RoboSats - Yksinkertainen ja yksityinen Lightning-pohjainen P2P-vaihto

## Ennen kuin aloitat

### Asiat, jotka sinun tulee tietää

| Jargoni       | Määritelmä                                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Automaattisesti luotu yksityinen kaupankäynti-identiteettisi. Älä käytä samaa robottia useammin kuin kerran, sillä se voi heikentää yksityisyyttäsi.                                                             |
| Token        | Satunnaisista merkeistä koostuva merkkijono, jota käytetään yksilöllisen robottisi luomiseen.                                                                                                                              |
| Maker        | Käyttäjä, joka luo tarjouksen Bitcoinin ostamisesta tai myymisestä.                                                                                                                                            |
| Taker        | Käyttäjä, joka hyväksyy toisen käyttäjän tarjouksen Bitcoinin ostamisesta tai myymisestä.                                                                                                                        |
| Bond         | Bitcoin-määrä, jonka molemmat osapuolet lukitsevat lupauksena toimia reilusti ja suorittaa kauppansa loppuun. Bondit ovat tyypillisesti 3% kaupan kokonaismäärästä ja ne toimivat Hodl-laskujen avulla. |
| Trade Escrow | Myyjän käyttämä menetelmä kaupan Bitcoin-määrän pitämiseen, jälleen käyttäen Hodl-laskuja.                                                                                              |
| Fees         | RoboSats veloittaa 0,2% kaupan määrästä, joka jaetaan makerin ja takerin kesken. Taker maksaa 0,175% ja maker maksaa 0,025%.                                                       |

## Asiat, jotka sinulla tulee olla

### Lightning-lompakko

RoboSats on Lightning-natiivi, joten tarvitset Lightning-lompakon bondin rahoittamiseen ja ostettujen satsien vastaanottamiseen ostajana. Lompakon valinnassa kannattaa olla tarkkana, sillä kaikki eivät ole yhteensopivia RoboSatsin käyttämän teknologian kanssa.

Jos olet solmun pyörittäjä, Zeus on ehdottomasti paras vaihtoehto. Jos sinulla ei ole omaa solmua, suosittelen Phoenixia, joka on alustojen välinen mobiililompakko yksinkertaisella asennuksella ja pääsyllä Lightning-verkkoon. Phoenixia käytettiin tämän oppaan tuottamiseen.

### Jonkin verran Bitcoinia

Ostajien ja myyjien on rahoitettava bond ennen kaupankäynnin aloittamista. Tämä on yleensä hyvin pieni määrä (~3% kaupan määrästä), mutta se on silti edellytys.

Käytätkö RoboSatsia ensimmäisten satsiesi ostamiseen? Miksi et pyytäisi ystävää lainaamaan sinulle pienen tarvittavan määrän aloittaaksesi!? Jos olet yksin liikkeellä, tässä on joitakin muita loistavia vaihtoehtoja hankkia joitakin noKYC satsia aloittaaksesi.

### Pääsy RoboSatsiin

Ilmeisesti tarvitset pääsyn RoboSatsiin! On neljä pääasiallista tapaa, joilla voit tehdä tämän:

1. Tor-selaimen kautta (Suositeltu!)
2. Tavallisen verkkoselaimen kautta (Ei suositeltu!)
3. Android APK:n kautta
4. Oma asiakasohjelmasi

Jos olet uusi Tor-selaimen käyttäjä, opi lisää ja lataa se [täältä](https://www.torproject.org/download/).
Pikahuomautus iOS-käyttäjille, jotka haluavat käyttää RoboSatsia Torin kautta puhelimillaan. 'Onion Browser' ei ole Tor Browser. Käytä sen sijaan Orbot + Safari tai Orbot + DuckDuckGo.

## Bitcoinin ostaminen

Seuraavat vaiheet suoritettiin toukokuussa 2023 käyttäen versiota 0.5.0, johon päästiin Tor-selaimen kautta. Vaiheet pitäisi olla samat käyttäjille, jotka käyttävät RoboSatsia Android APK:n kautta.

Kirjoitushetkellä RoboSats on vielä aktiivisessa kehityksessä, joten käyttöliittymä saattaa muuttua hieman tulevaisuudessa, mutta kaupan suorittamiseen tarvittavat perusvaiheet pysyvät suurelta osin muuttumattomina.

> Kun ensimmäisen kerran lataat RoboSatsin, sinut toivotetaan tervetulleeksi tälle aloitussivulle. Klikkaa Aloita.

![kuva](assets/2.webp)

Luo tokenisi ja säilytä se turvallisessa paikassa, kuten salatussa muistiinpanosovelluksessa tai salasanojen hallintajärjestelmässä. Tätä tokenia voidaan käyttää väliaikaisen Robot ID:si palauttamiseen, jos selain tai sovellus sulkeutuu kesken kaupan.

![kuva](assets/3.webp)

Tutustu uuteen Robot-identiteettiisi, sitten klikkaa Jatka.

![kuva](assets/4.webp)

Klikkaa Tarjoukset selataksesi tilauskirjaa. Sivun yläosassa voit sitten suodattaa mieltymystesi mukaan. Muista ottaa huomioon sidontaprosentit ja preemio keskimääräiseen vaihtokurssiin nähden.

- Valitse Osta
- Valitse valuuttasi
- Valitse maksutapasi

![kuva](assets/5.webp)

> Klikkaa tarjousta, jonka haluaisit ottaa. Syötä summa (valitsemassasi fiat-valuutassa), jonka haluaisit ostaa myyjältä, tarkista sitten tiedot viimeisen kerran ja klikkaa Ota tilaus.

Jos myyjä ei ole online (merkitty punaisella pisteellä heidän profiilikuvassaan), näet varoituksen, että kauppa saattaa kestää tavallista kauemmin. Jos jatkat ja myyjä ei etene ajoissa, saat korvauksena 50% heidän sidontamäärästään hukkaan menneestä ajastasi.

![kuva](assets/6.webp)

Seuraavaksi sinun on lukittava kauppatiiviste maksamalla näytöllä oleva lasku. Kyseessä on pidätyslasku, joka jäädyttää varat lompakossasi. Sitä veloitetaan vain, jos et suorita kauppaa loppuun.

![kuva](assets/7.webp)

Lightning-lompakossasi, skannaa QR-koodi ja maksa lasku.

![kuva](assets/8.webp)

Seuraavaksi, Lightning-lompakossasi, luo lasku näytetylle summalle ja liitä se annettuun tilaan.

![kuva](assets/9.webp)

Odota, että myyjä lukitsee kauppasummansa. Kun tämä tapahtuu, RoboSats siirtyy automaattisesti seuraavaan vaiheeseen, jossa chat-ikkuna avautuu. Sano Hei ja pyydä myyjältä heidän fiat-maksutietonsa. Kun olet saanut tiedot, lähetä maksu valitsemallasi tavalla ja vahvista tämä RoboSatsissa. Kaikki RoboSatsin chatit on PGP-salattu, mikä tarkoittaa, että vain sinä ja kauppakumppanisi voitte lukea viestit.

![kuva](assets/10.webp)

Kun myyjä vahvistaa maksun vastaanoton, RoboSats vapauttaa automaattisesti maksun aiemmin annetulla laskulla.

![kuva](assets/11.webp)

Kun lasku on maksettu, kauppa on valmis ja tiivisteesi vapautetaan. Näet sitten kaupan yhteenvedon.

![kuva](assets/12.webp)

Tarkista Lightning-lompakkosi vahvistus, että satoshit ovat saapuneet.

![kuva](assets/13.webp)

## Lisäominaisuudet

Bitcoinin ostamisen ja myymisen lisäksi RoboSatsissa on muutamia muita ominaisuuksia, jotka sinun tulisi tietää.
Robot Garage
Haluatko käydä useita kauppoja samaan aikaan, mutta et halua jakaa samaa identiteettiä niiden kesken? Ei ongelmaa! Klikkaa Robot-välilehteä, luo lisä Robot ja luo tai ota seuraava tilauksesi.
![kuva](assets/14.webp)

### Tilausten luominen

Voit ottaa jonkun toisen tarjouksen lisäksi luoda myös oman tilauksesi ja odottaa toisen Robotin tulevan luoksesi.

- Avaa Luo-sivu.
- Määritä, onko tilauksesi ostaa tai myydä Bitcoinia.
- Syötä määrä ja valuutta, jolla haluat Ostaa/Myydä.
- Syötä maksutapa(t), joita olet valmis käyttämään.
- Syötä 'Premium over Market' %, jonka olet valmis hyväksymään. Huomaa, että tämä voi olla negatiivinen luku tarjotaksesi alennuksella verrattuna nykyiseen markkinahintaan.
- Klikkaa Luo Tilaus.
- Maksa Lightning-lasku lukitaksesi Maker Bondisi.
- Tilauksesi on nyt aktiivinen. Istu takaisin ja odota jonkun hyväksyvän sen.

![kuva](assets/15.webp)

### On-chain Maksut

RoboSats keskittyy Lightningiin, mutta ostajilla on mahdollisuus vastaanottaa satsinsa on-chain Bitcoin-osoitteeseen. Ostajat voivat valita tämän vaihtoehdon lukittuaan bondinsa. On-chain valinnan jälkeen ostaja näkee yhteenvedon maksuista. Tämän palvelun lisämaksut sisältävät:

- Vaihtomaksu, jonka RoboSats kerää - Tämä maksu on dynaaminen ja muuttuu riippuen siitä, kuinka kiireinen Bitcoin-verkko on.
- Louhintamaksu maksutapahtumasta - Ostaja voi määrittää tämän.

![kuva](assets/16.webp)

### P2P Vaihdot

RoboSats mahdollistaa käyttäjille satsien vaihdon Lightning-lompakkoon tai sieltä pois. Klikkaa vain vaihtopainiketta tarjoussivun yläosassa nähdäksesi nykyiset vaihtotarjoukset.

'Swap In' tarjouksen ostajana lähetät on-chain Bitcoinia vertaiselle ja saat satsit takaisin, vähennettynä mainostetuista maksuista ja/tai preemioista, Lightning-lompakkoosi. 'Swap Out' tarjouksen ostajana lähetät satseja Lightningin kautta ja saat Bitcoinia, vähennettynä mahdollisista maksuista ja/tai preemioista, on-chain osoitteeseesi. Samourai tai Sparrow Wallet -käyttäjät voivat myös hyödyntää Stowaway-ominaisuutta suorittaakseen vaihdon.

RoboSatsin vaihtotarjoukset voivat myös sisältää Bitcoinille sidottuja vaihtoehtoja, kuten RBTC, LBTC ja WBTC. Sinun tulisi olla erittäin varovainen vuorovaikuttaessasi näiden tokenien kanssa, sillä ne kaikki sisältävät erilaisia kompromisseja. Sidottu Bitcoin ei ole Bitcoin!

![kuva](assets/17.webp)

### Aja oma RoboSats-asiakasohjelmasi

Umbrel, Citadel ja Start9 -solmun käyttäjät voivat asentaa oman RoboSats-asiakasohjelmansa suoraan solmuunsa. Tämän tekemisen hyödyt listataan seuraavasti:

- Huomattavasti nopeammat latausajat.
- Turvallisempi: hallitset, mitä RoboSats-asiakasohjelmaa ajat.
- Pääsy RoboSatsiin turvallisesti mistä tahansa selaimesta / laitteesta. Ei tarvetta käyttää TORia, jos olet paikallisverkossasi tai käytät VPN:ää: solmun taustajärjestelmä hoitaa tarvittavan torifikaation anonymisointia varten.
- Mahdollistaa hallinnan siitä, mihin P2P-markkinakoordinaattoriin yhdistät (oletuksena robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)

![kuva](assets/18.webp)

## UKK

### Voinko joutua huijatuksi?
Ostajana, jos olet lähettänyt fiat-valuutan, joka vaaditaan kaupan toteuttamiseksi omalta osaltasi, mutta myyjä ei vapauta sinulle satsseja, voit avata riidan. Jos tämän riidan aikana voit todistaa RoboSatsin välimiehille, että olet todella lähettänyt fiat-valuutan, myyjän escrow-varat ja kauppatakaus vapautetaan sinulle. Miten voin peruuttaa kaupan?

Voit peruuttaa kaupan jättämisen jälkeen klikkaamalla Kaupan valikossa olevaa Yhteistyöllinen peruutus -painiketta. Jos kauppakumppanisi suostuu peruutukseen, et joudu maksamaan mitään maksuja. Mutta jos kauppakumppanisi haluaa suorittaa kaupan loppuun ja peruutat silti, menetät kauppatakauksesi.

### Toimiiko RoboSats ‘X’ maksutavan kanssa?

RoboSatsissa ei ole rajoituksia maksutavoissa. Jos et näe tarjouksia haluamallasi menetelmällä, luo oma tarjouksesi käyttäen sitä!

![kuva](assets/19.webp)

### Mitä RoboSats oppii minusta, kun käytän sitä?

Kun käytät RoboSatsia Torin tai Android-sovelluksen kautta, ei mitään! Lue lisää täältä.

- Tor suojaa verkkoyksityisyytesi.
- PGP-salaus pitää kauppakeskustelusi yksityisenä.
- Tilitön käyttö tarkoittaa yhtä robottia kauppaa kohden. Tämä tarkoittaa, että RoboSats ei voi yhdistää useita kauppoja yhteen entiteettiin.

On kuitenkin joitakin varauksia! Lightning on melko yksityinen lähettäjänä, mutta ei vastaanottajana. Jos vastaanotat omaan Lightning-noodiisi, noodisi ID jaetaan laskuissasi. Tämä noodin ID antaa kenelle tahansa, jolla on tieto siitä, lähtökohdan yrittää yhdistää on-chain toimintasi. Tämä pätee myös, jos käyttäjä päättää vastaanottaa kauppansa on-chain maksuna.

Tämän lieventämiseksi käyttäjät voivat valita käyttää ratkaisua, kuten Proxy Wallet Lightningille tai Coinjoin on-chainille.

### Federaatio

Tällä hetkellä on olemassa yksi RoboSats-koordinaattori, jota operoi RoboSats-kehittäjätiimi. Bitcoinissa minkäänlainen keskittäminen tekee palvelusta helpomman kohteen hallituksille tai sääntelijöille, jotka eivät ehkä katso palvelua suopeasti.

Koska RoboSats on avoimen lähdekoodin projekti, kuka tahansa voisi ottaa koodin ja alkaa pyörittää omaa koordinaattoriaan. Vaikka tämä jossain määrin hajauttaa riskiä pois yhdestä kohteesta, se myös pirstaloittaa jo valmiiksi ohutta likviditeettimarkkinaa.

RoboSats-tiimi on tiedostanut tämän ja on aloittanut työn federoitua mallia varten. Loppukäyttäjänä tämän ei pitäisi muuttaa yllä esitettyä kaupankäyntivirtaa paljoakaan, mutta tulee olemaan lisänäkymiä tai -näyttöjä, joiden avulla voit lisätä tai poistaa eri koordinaattoreita, jotka ilmaantuvat.

OPAS päättyy
https://bitcoiner.guide/robosats/