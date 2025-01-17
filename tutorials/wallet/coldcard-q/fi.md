---
name: COLDCARD Q
description: COLDCARD-kortin asettaminen ja käyttö Q
---
![cover](assets/cover.webp)

Laitelompakko on elektroninen laite, joka on tarkoitettu Bitcoin-lompakon yksityisten avainten hallintaan ja suojaamiseen. Toisin kuin ohjelmistolompakot (tai hot walletit), jotka on asennettu yleiskäyttöisiin koneisiin, jotka ovat usein yhteydessä Internetiin, laitteistolompakot mahdollistavat yksityisten avainten fyysisen eristämisen, mikä vähentää piratismin ja varkauksien riskiä.

Laitteistolompakon päätavoitteena on vähentää laitteen toiminnallisuutta mahdollisimman paljon, jotta sen hyökkäyspinta olisi mahdollisimman pieni. Pienempi hyökkäyspinta tarkoittaa myös vähemmän potentiaalisia hyökkäysvektoreita eli vähemmän järjestelmän heikkoja kohtia, joita hyökkääjät voisivat käyttää hyväkseen päästäkseen käsiksi bitcoineihin.

On suositeltavaa käyttää laitteistolompakkoa bitcoinien suojaamiseen, etenkin jos hallussasi on suuria määriä joko absoluuttisena arvona tai osuutena kokonaisvaroistasi.

Laitteistolompakoita käytetään yhdessä tietokoneessa tai älypuhelimessa olevan lompakonhallintaohjelmiston kanssa. Jälkimmäinen hallinnoi transaktioiden luomista, mutta transaktioiden kryptografinen allekirjoitus, jota tarvitaan näiden transaktioiden validoimiseksi, suoritetaan yksinomaan laitteistolompakossa. Tämä tarkoittaa, että yksityiset avaimet eivät koskaan ole alttiina mahdollisesti haavoittuvalle ympäristölle.

Laitteistolompakot tarjoavat käyttäjälle kaksinkertaisen suojan: toisaalta ne suojaavat bitcoinit etähyökkäyksiltä pitämällä yksityiset avaimet offline-tilassa, ja toisaalta ne tarjoavat yleensä paremman fyysisen suojan avainten irrotusyrityksille. Juuri näiden kahden turvallisuuskriteerin perusteella voimme arvioida ja luokitella markkinoilla olevia eri malleja.

Tässä oppaassa esittelen sinulle yhden tällaisen ratkaisun: **COLDCARD Q**.

---
Koska COLDCARD Q tarjoaa monia toimintoja, ehdotan, että sen käyttö jaetaan kahteen opetusohjelmaan. Tässä ensimmäisessä opetusohjelmassa tarkastelemme laitteen alkukonfigurointia ja perustoimintoja. Toisessa opetusohjelmassa tarkastelemme sitten sitä, miten voit hyödyntää kaikkia COLDCARDin lisäasetuksia.

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
---
## COLDCARD Q:n esittely

COLDCARD Q on pelkästään Bitcoinia sisältävä laitteistolompakko, jonka on kehittänyt kanadalainen Coinkite, joka tunnetaan aiemmista MK-malleistaan. Q edustaa heidän tähän mennessä kehittyneintä tuotettaan, ja se on suunniteltu lopulliseksi Bitcoin-laitelompakoksi.

Laitteiston osalta COLDCARD Q on varustettu kaikilla optimaalisen käyttökokemuksen edellyttämillä ominaisuuksilla:


- Suuri LCD-näyttö helpottaa navigointia ja käyttöä;
- Täysi QWERTY-näppäimistö;
- Integroitu kamera QR-koodien skannausta varten;
- Kaksi microSD-korttipaikkaa;
- Täysin eristetty virtalähde kolmella AAA-paristolla (ei sisälly) tai USB-C-kaapelilla ;
- Kaksi Secure Elementtiä kahdelta eri valmistajalta lisää turvallisuutta;
- Kyky kommunikoida NFC:n kautta.

Mielestäni COLDCARD Q:lla on vain kaksi haittaa. Ensinnäkin se on monien ominaisuuksiensa vuoksi melko kookas, sillä se on lähes 13 cm pitkä ja 8 cm leveä, mikä on lähes pienen älypuhelimen kokoinen. Se on myös melko paksu akkulokeron vuoksi. Jos etsit pienempää ja liikkuvampaa laitteistolompakkoa, paljon kompaktimpi MK4 saattaa olla parempi vaihtoehto. Toinen haittapuoli on tietenkin laitteen hinta, joka virallisilla verkkosivuilla on ** 239,99 dollaria** eli 72 dollaria enemmän kuin MK4:n. Tämä asettaa Q:n suoraan kilpailuun Ledger Flexin tai Foundationin Passportin kaltaisten premium-laitelompakoiden kanssa.

![CCQ](assets/fr/001.webp)

Ohjelmistopuolella COLDCARD Q on yhtä hyvin varustettu kuin muutkin Coinkiten laitteet, ja siinä on lukuisia kehittyneitä ominaisuuksia:


- Nopanheitto tuottaa oman palautuslauseen ;
- PIN-koodi ;
- Lähtölaskenta lopulliseen PIN-lukitukseen ;
- BIP39-salasana ;
- Lopullinen lukitus PIN-koodi ;
- Yhteyden lähtölaskenta ;
- SeedXOR;
- BIP85...

Lyhyesti sanottuna COLDCARD Q tarjoaa paremman käyttökokemuksen kuin MK4, ja se voi olla ihanteellinen keskitason tai edistyneemmille käyttäjille, jotka etsivät suurempaa helppokäyttöisyyttä.

COLDCARD Q on myynnissä [Coinkiten virallisilla verkkosivuilla] (https://store.coinkite.com/store/coldcard). Sen voi ostaa myös jälleenmyyjältä.

## Ohjeen valmistelu

Kun olet vastaanottanut COLDCARD-korttisi, sinun on ensin tarkastettava pakkaus ja varmistettava, ettei sitä ole avattu. Jos pakkaus on vahingoittunut, se voi olla merkki siitä, että laitteiston lompakko on vahingoittunut eikä se ehkä ole aito.

![CCQ](assets/fr/002.webp)

Kun avaat laatikon, sieltä löytyvät seuraavat tuotteet:


- COLDCARD Q suljetussa pussissa;
- Kortti, johon voit kirjata muistisääntösi.

![CCQ](assets/fr/003.webp)

Varmista, että pussi ei ole sinetöity tai vahingoittunut. Tarkista myös, että pussissa oleva numero vastaa pussin sisällä olevassa paperissa olevaa numeroa. Säilytä tämä numero myöhempää käyttöä varten.

![CCQ](assets/fr/004.webp)

Jos haluat syöttää COLDCARD-korttiin virtaa kytkemättä sitä tietokoneeseen (ilmaväli), aseta kolme AAA-paristoa laitteen takaosaan. Vaihtoehtoisesti voit liittää sen tietokoneeseen USB-C-kaapelilla.

![CCQ](assets/fr/005.webp)

Tätä opetusohjelmaa varten tarvitset myös Sparrow Walletin, jolla voit hallita Bitcoin-lompakkoasi tietokoneellasi. Lataa [Sparrow Wallet](https://sparrowwallet.com/download/) virallisilta verkkosivuilta. Suosittelen vahvasti tarkistamaan sekä sen aitouden (GnuPG:n avulla) että eheyden (hash-arvon avulla) ennen asennuksen aloittamista. Jos et tiedä, miten tämä tehdään, seuraa tätä ohjetta:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
## PIN-koodin valinta

Voit nyt kytkeä COLDCARDin päälle painamalla vasemmassa yläkulmassa olevaa painiketta.

![CCQ](assets/fr/006.webp)

Hyväksy käyttöehdot painamalla "*ENTER*"-painiketta.

![CCQ](assets/fr/007.webp)

Tämän jälkeen COLDCARD Q näyttää numeron näytön yläosassa. Varmista, että tämä numero vastaa sinetöidyssä pussissa ja pussin sisällä olevassa muovipalassa olevaa numeroa. Näin varmistetaan, että pakettiasi ei ole avattu Coinkiten pakkauksen pakkaamisen ja avaamisen välisenä aikana. Jatka painamalla "*ENTER*".

![CCQ](assets/fr/008.webp)

Siirry valikkoon "*Valitse PIN-koodi*" ja vahvista valinta "*ENTER*"-painikkeella.

![CCQ](assets/fr/009.webp)

Tätä PIN-koodia käytetään COLDCARD-kortin lukituksen avaamiseen. Se suojaa siis luvattomalta fyysiseltä käytöltä. Tämä PIN-koodi ei osallistu lompakkosi kryptografisten avainten johtamiseen. Vaikka PIN-koodia ei olisikaan saatavilla, voit saada bitcoinisi takaisin, jos sinulla on muistisääntösi hallussasi.

COLDCARDin PIN-koodit on jaettu kahteen osaan: etuliitteeseen ja jälkiliitteeseen, joista kumpikin voi sisältää 2-6 numeroa, eli yhteensä 4-12 numeroa. Kun avaat COLDCARD-korttisi lukituksen, sinun on ensin syötettävä etuliite, minkä jälkeen laite näyttää sinulle kaksi sanaa. Syötä sitten jälkiliite. Nämä kaksi sanaa annetaan sinulle tämän konfigurointivaiheen aikana, ja ne on syytä tallentaa huolellisesti, sillä tarvitset niitä joka kerta, kun avaat COLDCARDin lukituksen. Jos lukituksen avaamisen aikana näytetyt kaksi sanaa vastaavat konfiguroinnin aikana tallentamiasi sanoja, tämä vahvistaa, että laitettasi ei ole vaarannettu sen viimeisimmän käytön jälkeen.

Napsauta uudelleen "*Valitse PIN-koodi*"

![CCQ](assets/fr/010.webp)

Vahvista, että olet lukenut varoitukset.

![CCQ](assets/fr/011.webp)

Nyt valitset PIN-koodin. Suosittelemme pitkää, satunnaista PIN-koodia. Varmista, että säilytät tätä koodia eri paikassa kuin missä COLDCARD-korttia säilytetään. Voit käyttää paketin mukana toimitettua korttia tämän koodin tallentamiseen.

Syötä haluamasi etuliite ja vahvista PIN-koodin ensimmäinen osa painamalla "*ENTER*"-painiketta.

![CCQ](assets/fr/012.webp)

Tämän jälkeen näytölläsi näkyy kaksi anti-phishing-sanaa. Tallenna ne huolellisesti myöhempää käyttöä varten. Voit kirjoittaa ne ylös paketin mukana toimitetulla kortilla.

![CCQ](assets/fr/013.webp)

Syötä sitten PIN-koodin toinen osa ja paina "*ENTER*".

![CCQ](assets/fr/014.webp)

Vahvista PIN-koodisi syöttämällä se toisen kerran ja tarkista, että kaksi phishingin vastaista sanaa vastaavat aiemmin tallentamiasi sanoja.

![CCQ](assets/fr/015.webp)

Muista tästä lähtien joka kerta, kun avaat COLDCARD-korttisi lukituksen, tarkistaa, että näytölle ilmestyvät kaksi phishingin vastaista sanaa ovat voimassa sen jälkeen, kun olet syöttänyt PIN-koodin etuliitteen.

## Firmware-päivitys

Kun käytät laitetta ensimmäistä kertaa, on tärkeää tarkistaa ja päivittää laiteohjelmisto. Voit tehdä tämän avaamalla "*Advanced/Tools*"-valikon.

![CCQ](assets/fr/016.webp)

**Tärkeää:** Jos aiot päivittää laiteohjelmiston ja tämä ei ole ensimmäinen kerta, kun käytät COLDCARDia (eli sinulla on jo lompakko luotuna COLDCARDiin), varmista, että sinulla on muistilauseke ja että se toimii (samoin kuin valinnainen salasana, jos mahdollista). Tämä on tärkeää, jotta vältät bitcoinien menettämisen, jos laitteen päivityksen aikana ilmenee ongelmia.

Valitse "*Upgrade Firmware*".

![CCQ](assets/fr/017.webp)

Valitse "*Näytä versio*".

![CCQ](assets/fr/018.webp)

Voit tarkistaa COLDCARDin nykyisen laiteohjelmistoversion. Esimerkiksi minun tapauksessani versio on "*1.2.3Q*".

![CCQ](assets/fr/019.webp)

Tarkista [COLDCARDin viralliselta verkkosivustolta](https://coldcard.com/downloads), onko uudempi versio saatavilla. Lataa uusi laiteohjelma napsauttamalla "*Download*".

![CCQ](assets/fr/020.webp)

Tässä vaiheessa suosittelemme, että tarkistat ladatun laiteohjelmiston eheyden ja aitouden. Lataa [dokumentti, joka sisältää kehittäjien allekirjoittamat kaikkien versioiden hashit](https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt), tarkista allekirjoitus [kehittäjän julkisella avaimella](https://keybase.io/dochex) ja varmista, että allekirjoitetussa dokumentissa ilmoitettu hash vastaa sivustolta ladatun laiteohjelmiston hashia. Jos kaikki on oikein, voit jatkaa päivitystä.

Jos et ole perehtynyt tähän todentamisprosessiin, suosittelen seuraamaan tätä ohjetta:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Ota microSD-kortti ja siirrä laiteohjelmistotiedosto (tiedostomuoto `.dfu`) sille. Aseta microSD-kortti johonkin COLDCARDin porttiin.

![CCQ](assets/fr/021.webp)

Valitse sitten laiteohjelmiston päivitysvalikosta "*From MicroSD*".

![CCQ](assets/fr/022.webp)

Valitse laiteohjelmistoa vastaava tiedosto.

![CCQ](assets/fr/023.webp)

Vahvista valinta painamalla "*ENTER*"-painiketta.

![CCQ](assets/fr/024.webp)

Odota, kun laiteohjelmistoa päivitetään.

![CCQ](assets/fr/025.webp)

Kun päivitys on valmis, avaa laitteen lukitus syöttämällä PIN-koodi.

![CCQ](assets/fr/026.webp)

Laiteohjelmistosi on nyt ajan tasalla.

## COLDCARD Q -parametrit

Voit halutessasi tutkia COLDCARDin asetuksia avaamalla "*asetukset*"-valikon.

![CCQ](assets/fr/027.webp)

Tässä valikossa on erilaisia mukautusvaihtoehtoja, kuten näytön kirkkauden asettaminen tai oletusmittayksikön valitseminen.

![CCQ](assets/fr/028.webp)

Tarkastelemme muita lisäasetuksia seuraavassa opetusohjelmassa:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0
## Bitcoin-lompakon luominen

Nyt on aika luoda uusi Bitcoin-lompakko! Tätä varten sinun on luotava muistilauseke. Coldcardissa sinulla on kolme tapaa tämän lauseen luomiseen:


- Käytä vain sisäistä satunnaislukugeneraattoria (TRNG);
- Käytä TRNG:n ja nopan heiton yhdistelmää entropian lisäämiseksi;
- Käytä vain nopanheittoa.

**Aloittelijoille ja keskitason käyttäjille suosittelemme käyttämään vain COLDCARDin sisäistä satunnaislukugeneraattoria**

En suosittele pelkän nopan käyttöä, sillä huono toteutus voi johtaa lauseeseen, jonka entropia on riittämätön, mikä vaarantaa lompakkosi turvallisuuden.

Paras vaihtoehto on kuitenkin varmasti jälkimmäinen, jossa TRNG:n käyttö yhdistetään ulkoiseen entropialähteeseen. Tämä menetelmä takaa vähimmäiskentropian, joka vastaa pelkän TRNG:n vähimmäiskentropiaa, ja se lisää lisäturvaa sisäisen generaattorin mahdollisen (vapaaehtoisen tai ei vapaaehtoisen) vikaantumisen varalta. Valitsemalla tämän vaihtoehdon, jossa yhdistyvät TRNG ja nopanheitto, voit hallita paremmin lauseen generointia, mutta et kuitenkaan lisää riskejä, jotka liittyvät siihen, että toteutus ei onnistuisi omalta osaltasi.

Napsauta "*Uudet siemen-sanat*".

![CCQ](assets/fr/029.webp)

Voit valita tuomiosi pituuden. Suosittelen, että valitset 12 sanan pituisen lauseen, koska se on helpompi hallita eikä se tarjoa yhtään pienempää portfoliovarmuutta kuin 24 sanan pituinen lause.

![CCQ](assets/fr/030.webp)

Tämän jälkeen COLDCARD näyttää TRNG:n luoman palautuslausekkeen. Jos haluat lisätä ulkoista entropiaa, paina näppäintä "*4*".

![CCQ](assets/fr/031.webp)

Tämä vie sinut sivulle, jossa voit lisätä entropiaa heittämällä noppaa. Tee niin monta heittoa kuin mahdollista (suositellaan vähintään 50:tä, mutta vähempi ei haittaa, koska hyödyt jo TRNG:n entropiasta) ja kirjaa tulokset näppäimillä "*1*" - "*6*". Kun olet valmis, vahvista painamalla "*ENTER*".

![CCQ](assets/fr/032.webp)

Näyttöön tulee uusi muistisääntö, joka perustuu juuri antamasi entropian ja TRNG:n entropian perusteella.

**Varoitus: Tämä muistilista antaa täyden, rajoittamattoman pääsyn kaikkiin bitcoineihisi**. Kuka tahansa, jolla on hallussaan tämä fraasi, voi varastaa varojasi, vaikka hänellä ei olisi fyysistä pääsyä COLDCARDIisi. 12-sanainen lauseke palauttaa pääsyn bitcoineihisi, jos COLDCARD-korttisi katoaa, varastetaan tai rikkoutuu. Siksi on erittäin tärkeää, että tallennat sen huolellisesti ja säilytät sen turvallisessa paikassa.

Voit kirjoittaa sen COLDCARD-kortin mukana toimitetulle kartongille, tai lisäturvallisuuden vuoksi suosittelen, että kaiverrutat sen ruostumattomasta teräksestä valmistettuun tukeen, joka suojaa sitä tulipalon, tulvan tai romahduksen vaaralta. Älä missään tapauksessa koskaan tallenna sitä digitaaliselle tietovälineelle, sillä muuten voit menettää bitcoinisi.

Kirjoita näytöllä olevat sanat haluamallesi fyysiselle välineelle. Turvallisuusstrategiastasi riippuen voit harkita useiden täydellisten fyysisten kopioiden tekemistä lauseesta (mutta ennen kaikkea älä jaa sitä). On tärkeää, että sanat ovat numeroituja ja juoksevassa järjestyksessä.

On selvää, ettet saa koskaan jakaa näitä sanoja** Internetissä, toisin kuin tässä opetusohjelmassa. Tätä esimerkkisalkkua käytetään vain Testnetissä, ja se poistetaan opetusohjelman päätyttyä.

Kun olet kirjoittanut sanat ylös, paina "*ENTER*".

![CCQ](assets/fr/033.webp)

Varmistaaksesi, että olet tallentanut lauseesi oikein, järjestelmä pyytää sinua vahvistamaan tietyt sanat. Valitse näppäimistöltä kutakin sanaa vastaava numero.

![CCQ](assets/fr/034.webp)

Lompakkosi on nyt luotu! Näytön oikeassa yläkulmassa näet yksityisen pääavaimesi sormenjäljen. Paina "*ENTER*".

![CCQ](assets/fr/035.webp)

Pääset nyt COLDCARDin päävalikkoon.

![CCQ](assets/fr/036.webp)

## Uuden salkun perustaminen Sparrow'ssa

Sparrow Wallet -ohjelmiston ja COLDCARD-korttisi välisen viestinnän luomiseen on useita vaihtoehtoja. Suoraviivaisin on käyttää USB-C-kaapelia. COLDCARD-korttisi kaapeli- ja NFC-viestintä on kuitenkin oletusarvoisesti poistettu käytöstä. Voit aktivoida ne uudelleen siirtymällä kohtaan "*Asetukset*", sitten "*Hardware On/Off*" ja aktivoimalla haluamasi viestintävaihtoehdon.

![CCQ](assets/fr/037.webp)

Jos haluat pitää COLDCARD-kortin täysin erillään tietokoneesta, voit valita epäsuoran "air-gap"-viestinnän QR-koodien tai microSD-kortin avulla. Tätä menetelmää käytämme tässä oppaassa.

Siirry kohtaan "*Advanced/Tools*".

![CCQ](assets/fr/038.webp)

Valitse "*Vie lompakko*".

![CCQ](assets/fr/039.webp)

Valitse sitten "*Sparrow Wallet*".

![CCQ](assets/fr/040.webp)

Paina "*ENTER*" luodaksesi konfiguraatiotiedoston.

![CCQ](assets/fr/041.webp)

Valitse sitten, miten tiedosto lähetetään Sparrow'lle. Tässä esimerkissä olen asettanut microSD-kortin korttipaikkaan "*A*", joten valitsen "*1*"-painikkeen. Voit myös näyttää tiedot QR-koodina COLDCARD-näytöllä painamalla "*QR*"-painiketta ja skannaamalla tämän QR-koodin tietokoneen web-kameralla.

![CCQ](assets/fr/042.webp)

Käynnistä Sparrow Wallet ja hyppää esittelysivujen yli päästäksesi päänäytölle. Varmista, että olet yhdistetty oikein solmuun tarkistamalla näytön oikeassa alareunassa oleva kytkin.

![CCQ](assets/fr/043.webp)

On erittäin suositeltavaa, että käytät omaa Bitcoin-solmua. Tässä ohjeessa käytän julkista solmua (keltainen), koska olen testiverkossa, mutta tuotantokäytössä on parasta käyttää Bitcoin Corea paikallisesti (vihreä) tai Electrum-palvelinta etäsolmussa (sininen).

Siirry "*Tiedosto*"-valikkoon ja valitse "*Uusi lompakko*".

![CCQ](assets/fr/044.webp)

Anna lompakollesi nimi ja napsauta "*Luo lompakko*".

![CCQ](assets/fr/045.webp)

Valitse avattavasta "*Script Type*"-valikosta skriptityyppi, joka suojaa bitcoinisi.

![CCQ](assets/fr/046.webp)

Napsauta "*Airapped Hardware Wallet*".

![CCQ](assets/fr/047.webp)

Napsauta välilehdellä "*Coldcard*" kohtaa "*Scan...*", jos aiot skannata COLDCARD-kortissa näkyvän QR-koodin, tai "*Import File...*" tuodaksesi tiedoston microSD-kortilta (tämä on `.json`-tiedosto).

![CCQ](assets/fr/048.webp)

Tarkista tuonnin jälkeen, että Sparrow'ssa näkyvä *Master-sormenjälki* vastaa COLDCARD-kortissa näkyvää sormenjälkeä. Vahvista luominen napsauttamalla "*Apply*".

![CCQ](assets/fr/049.webp)

Määritä vahva salasana, jolla varmistat pääsyn Sparrow-lompakkoosi. Tämä salasana suojaa julkisia avaimia, osoitteita, tunnisteita ja tapahtumahistoriaa luvattomalta käytöltä.

Salasana kannattaa tallentaa, jotta et unohda sitä (esim. salasanahallintaan).

![CCQ](assets/fr/050.webp)

Lompakkosi on nyt perustettu Sparrow Walletiin.

![CCQ](assets/fr/051.webp)

Ennen kuin saat ensimmäiset bitcoinit lompakkoosi, **neuvon sinua tekemään tyhjän palautustestin**. Kirjoita muistiin joitakin viitetietoja, kuten xpub, ja nollaa sitten COLDCARD Q, kun lompakko on vielä tyhjä. Yritä sitten palauttaa lompakkosi COLDCARDille paperisten varmuuskopioiden avulla. Tarkista, että palautuksen jälkeen luotu xpub vastaa alun perin kirjoittamaasi xpubia. Jos se täsmää, voit olla varma, että paperiset varmuuskopiot ovat luotettavia.

Jos haluat lisätietoja palautustestin suorittamisesta, suosittelen, että tutustut tähän toiseen opetusohjelmaan:

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
## Vastaanottaa bitcoineja

Saat ensimmäiset bitcoinisi aluksi kytkemällä COLDCARDin päälle ja avaamalla sen lukituksen.

![CCQ](assets/fr/052.webp)

Napsauta Sparrow-lompakossa välilehteä "*Vastaanottaa*".

![CCQ](assets/fr/053.webp)

Ennen kuin käytät Sparrow Walletin ehdottamaa osoitetta, tarkista se COLDCARD-näytöltä. Näin voit varmistaa, että Sparrow'n näyttämä osoite ei ole vilpillinen ja että laitteistolompakossa on todellakin yksityinen avain, jota tarvitaan tällä osoitteella suojattujen bitcoinien käyttämiseen. Tämä auttaa sinua välttämään useita hyökkäystyyppejä.

Voit tehdä tämän tarkistuksen napsauttamalla COLDCARDin *Address Explorer* -valikkoa.

![CCQ](assets/fr/054.webp)

Valitse Sparrow'ssa käyttämäsi skriptityyppi. Minun tapauksessani se on Segwit P2WPKH. Napsautan sitä.

![CCQ](assets/fr/055.webp)

Sen jälkeen näet eri johdetut osoitteet järjestyksessä.

![CCQ](assets/fr/056.webp)

Tarkista Sparrow'lta, että osoite täsmää. Minun tapauksessani osoite, jonka johdannaispolku on `m/84'/1'/0'/0/0`, on todellakin `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` sekä Sparrow'ssa että COLDCARDissa.

![CCQ](assets/fr/057.webp)

Toinen tapa tarkistaa osoitteen omistusoikeus on skannata sen QR-koodi suoraan Sparrowiin COLDCARD-kortiltasi. Valitse COLDCARDin aloitusnäytöltä "*Scan Any QR Code*". Voit myös käyttää näppäimistön "*QR*"-näppäintä.

![CCQ](assets/fr/058.webp)

Skannaa Sparrow Walletissa näkyvän osoitteen QR-koodi.

![CCQ](assets/fr/059.webp)

Varmista, että COLDCARD-kortissasi näkyvä osoite vastaa Sparrow'ssa näkyvää osoitetta. Paina sitten "*1*"-painiketta.

![CCQ](assets/fr/060.webp)

Osoite on siis vahvistettu onnistuneesti.

![CCQ](assets/fr/061.webp)

Voit nyt lisätä "*Label*" kuvaamaan bitcoinien lähdettä, joka suojataan tällä osoitteella. Tämä on hyvä käytäntö, jonka avulla voit paremmin hallita UTXO:tasi.

![CCQ](assets/fr/062.webp)

Jos haluat lisätietoja merkinnöistä, suosittelen myös tätä toista ohjetta:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52
Voit sitten käyttää tätä osoitetta bitcoinien vastaanottamiseen.

![CCQ](assets/fr/063.webp)

## Lähetä bitcoineja

Nyt kun olet saanut ensimmäiset satsisi COLDCARDilla suojattuun lompakkoosi, voit myös käyttää niitä!

Kuten aina, aloita kytkemällä COLDCARD Q päälle ja avaamalla sen lukitus, avaa sitten Sparrow-lompakko ja siirry "*lähettää*"-välilehdelle valmistellaksesi uutta tapahtumaa.

![CCQ](assets/fr/064.webp)

Jos haluat "kolikkohallintaa", eli valita tarkkaan, mitä UTXO:ita haluat käyttää transaktiossa, siirry "*UTXO:t*"-välilehdelle. Valitse UTXO:t, jotka haluat käyttää, ja napsauta sitten "*Send Selected*". Sinut ohjataan samalle "*Lähettää*"-välilehdelle, mutta UTXOt on jo valittu tapahtumaa varten.

![CCQ](assets/fr/065.webp)

Kirjoita kohdeosoite. Voit myös syöttää useita osoitteita napsauttamalla "*+ Lisää*"-painiketta.

![CCQ](assets/fr/066.webp)

Kirjoita "*Label*", jotta muistat tämän menon tarkoituksen.

![CCQ](assets/fr/067.webp)

Valitse tähän osoitteeseen lähetettävä summa.

![CCQ](assets/fr/068.webp)

Säädä maksutapahtuman maksuprosentti kulloisenkin markkinatilanteen mukaan.

![CCQ](assets/fr/069.webp)

Varmista, että kaikki tapahtumaparametrit ovat oikein, ja napsauta sitten "*Luo tapahtuma*".

![CCQ](assets/fr/070.webp)

Jos olet tyytyväinen kaikkeen, napsauta "*Viimeistele tapahtuma allekirjoittamista varten*".

![CCQ](assets/fr/071.webp)

Kun olet rakentanut tapahtuman Sparrow'ssa, on aika allekirjoittaa se COLDCARDilla. PSBT:n (allekirjoittamattoman tapahtuman) lähettämiseen laitteeseen on useita vaihtoehtoja. Jos langallinen tiedonsiirto on käytössä, voit lähettää transaktion suoraan USB-C-yhteyden kautta, aivan kuten minkä tahansa muun laitteistolompakon kanssa. Tässä tapauksessa Sparrow'ssa sinun on napsautettava oikeassa alakulmassa olevaa "*Sign*"-painiketta. Esimerkissäni tämä painike on estetty, koska COLDCARDia ei ole liitetty kaapelilla.

![CCQ](assets/fr/072.webp)

Jos haluat säilyttää "ilmarako"-yhteyden ilman suoraa kosketusta laitteiston lompakon ja tietokoneen välillä, sinulla on kaksi vaihtoehtoa. Ensimmäinen ja monimutkaisempi vaihtoehto on käyttää microSD-korttia. Aseta microSD-kortti tietokoneeseen, tallenna tapahtuma Sparrow'n "*Save Transaction*"-painikkeella ja siirrä kortti sitten COLDCARDin porttiin.

![CCQ](assets/fr/073.webp)

Siirry sitten "*Valmis allekirjoittamaan*"-valikkoon.

![CCQ](assets/fr/074.webp)

Tarkista COLDCARD-korttisi maksutapahtuman tiedot, mukaan lukien vastaanottava osoite, lähetetty summa ja maksutapahtumamaksu.

![CCQ](assets/fr/075.webp)

Jos kaikki on oikein, paina "*ENTER*"-painiketta allekirjoittaaksesi tapahtuman.

![CCQ](assets/fr/076.webp)

Aseta sitten microSD-kortti takaisin tietokoneeseen ja lataa allekirjoitettu tapahtuma microSD-kortilta Sparrow'ssa napsauttamalla "*Load Transaction*". Tämän jälkeen voit suorittaa viimeisen tarkistuksen ennen sen lataamista Bitcoin-verkkoon.

![CCQ](assets/fr/077.webp)

Toinen tapa allekirjoittaa COLDCARD-kortilla Air-Gapissa, joka on paljon yksinkertaisempi kuin microSD-menetelmä, on skannata PSBT-kortti suoraan laitteen kameran avulla. Valitse Sparrowissa "*Show QR*".

![CCQ](assets/fr/078.webp)

Valitse COLDCARDissa "*Scan Any QR Code*". Voit myös käyttää näppäimistön "*QR*"-näppäintä.

![CCQ](assets/fr/079.webp)

Skannaa COLDCARDin kameran avulla Sparrow'ssa näkyvä QR-koodi.

![CCQ](assets/fr/080.webp)

Maksutapahtuman tiedot tulevat uudelleen näkyviin tarkistusta varten. Paina "*ENTER*" allekirjoittaaksesi, jos olet tyytyväinen.

![CCQ](assets/fr/081.webp)

COLDCARD-korttisi näyttää sitten allekirjoitetun tapahtuman QR-koodina. Skannaa tämä QR-koodi tietokoneen web-kameran avulla valitsemalla Sparrow'ssa "*Scan QR*".

![CCQ](assets/fr/082.webp)

Allekirjoittamasi tapahtuma näkyy nyt Sparrow'ssa. Tarkista vielä kerran, että kaikki on oikein, ja lähetä se sitten Bitcoin-verkkoon klikkaamalla "*Broadcast Transaction*".

![CCQ](assets/fr/083.webp)

Voit seurata tapahtumaasi Sparrow Walletin "*Tapahtumat*"-välilehdellä.

![CCQ](assets/fr/084.webp)

Onneksi olkoon, olet nyt perehtynyt COLDCARD Q:n peruskäyttöön Sparrow Walletin kanssa!

Jos löysit tämän ohjeen hyödylliseksi, olisin hyvin kiitollinen, jos jättäisit vihreän peukalon alle. Voit myös vapaasti jakaa tätä opetusohjelmaa sosiaalisissa verkostoissa. Kiitos paljon!

Suosittelen myös tutustumaan tähän toiseen opetusohjelmaan, jossa käsitellään COLDCARD Q:n lisäasetuksia:

https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0