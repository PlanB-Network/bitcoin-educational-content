---
name: Rakentaminen elementtien ja nestemäisen verkon avulla
goal: Opi käyttämään ja kehittämään Elementsin avoimen lähdekoodin lohkoketjualustaa ja sen keskeisiä ominaisuuksia
objectives: 

  - Ymmärrät Elements-lohkoketjualustan ja Liquid-sivuketjujen peruskäsitteet.
  - Opi perustamaan ja käyttämään Elements-solmuja itsenäisiä ja sivuketjukokoonpanoja varten.
  - Hanki käytännön kokemusta federoidusta lohkojen allekirjoittamisesta ja federoidusta 2-Way Pegistä.
  - Turvallisen ja tehokkaan lohkoketjuympäristön perustaminen ja hallinnointi todellisia käyttötapauksia varten.

---
# Rakenna nesteen ja elementtien varaan

Tutustu Liquidin ja Elementsin edistyneisiin ominaisuuksiin ja mahdollisuuksiin ja opi hyödyntämään näitä työkaluja tehokkaasti kehitysprojekteissasi. Tämä koulutus tarjoaa täydellisen teoreettisen ja käytännöllisen perustan, jonka avulla hallitset sellaiset ominaisuudet kuin Confidential Transactions, Issued Assets ja Federated Block Signing.

Elements-kehykseen perustuva Liquid on suunniteltu parantamaan yksityisyyden suojaa, skaalautuvuutta ja toiminnallisuutta taloudellisten ja teknisten ratkaisujen osalta. Tällä kurssilla saat käytännön kokemusta varojen liikkeeseenlaskusta ja hallinnasta, Federated 2-Way Pegistä sekä elementsd:n ja elements-cli:n kaltaisten työkalujen käytöstä, mikä antaa sinulle mahdollisuuden luoda innovatiivisia, tarpeisiisi räätälöityjä ratkaisuja.

Tämä kurssi on räätälöity kaikkien kokemustasojen kehittäjille. Aloittelijoille ja keskitason käyttäjille on tarjolla helppotajuisia selityksiä ja käytännön esimerkkejä, kun taas edistyneet käyttäjät voivat syventyä Liquidin ja Elementsin teknisiin yksityiskohtiin ja vähemmän tunnettuihin ominaisuuksiin.

Tule mukaan kehittämään taitojasi, vapauttamaan Liquidin ja Elementsin koko potentiaali ja luomaan vaikuttavia työkaluja Liquid-innovaatioiden tulevaisuutta varten.

+++
# Johdanto

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Kurssit Johdanto

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

![Video](https://youtu.be/gkQfnwYLyI0?si=H6cIPhgZaSAwHaHI)

Elements Academyn tarkoituksena on esitellä ja selittää Liquidin perustana olevan avoimen lähdekoodin Elements-alustan keskeiset käsitteet. Kurssin loppuun mennessä sinulla pitäisi olla hyvä käsitys Elementsin tärkeimmistä ominaisuuksista, kuten Confidential Transactions ja Issued Assets, sekä Elements Coren käyttämiseen liittyvistä prosesseista.

Jokaisessa osiossa on oppitunteja, joissa on selittävä teksti ja video, joka päättyy tietokilpailuun. Kysymysten määrä liittyy edeltävän aiheen laajuuteen. Osiossa 10 tehdään yhteenveto kurssin sisällöstä ja se päättyy suurempaan tietokilpailuun.

Kaikki kysymykset, lisätietopyynnöt tai kyselyiden vastauksia koskevat kysymykset voit osoittaa opettajallesi James Dorfmanille.

## Elementtien yleiskatsaus

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

![Video](https://youtu.be/ns-JLGdkNig?si=fmWye_boRSvVF1Bt)

Elements on avoimen lähdekoodin, sivuketjuihin soveltuva lohkoketjualusta, joka tarjoaa pääsyn yhteisön jäsenten kehittämiin tehokkaisiin ominaisuuksiin, kuten luottamuksellisiin transaktioihin ja liikkeeseen laskettuihin varoihin.

Elements on pohjimmiltaan protokolla, joka mahdollistaa konsensuksen muodostamisen transaktiohistoriasta ja säännöistä, jotka ohjaavat hajautettuun lohkoketjuun tallennettujen varojen siirtoa ja luomista.

Lisää taustatietoa Elementsistä löytyy helposti Elements-projektin verkkosivuilta (https://elementsproject.org/), virallisesta Liquid-blogista (https://blog.liquid.net/) ja kehittäjäportaalista (https://liquid.net/devs).

### Elementit

Vuonna 2015 lanseerattu Elements vähentää sisäisiä kehitys- ja tutkimuskustannuksia ja hyödyntää uusinta lohkoketjuteknologiaa, mikä avaa monia uusia käyttömahdollisuuksia. Elements-pohjainen lohkoketju voi toimia joko itsenäisenä lohkoketjuna tai se voidaan liittää toiseen lohkoketjuun ja käyttää sivuketjuna. Elementsin käyttäminen sivuketjuna mahdollistaa varojen todentavan siirron eri lohkoketjujen välillä.

Se perustuu Bitcoinin koodipohjaan ja laajentaa sitä, ja sen avulla bitcoind API:n tuntevat kehittäjät voivat nopeasti ja kustannustehokkaasti luoda toimivia lohkoketjuja ja testata proof-of-concept -projekteja. Koska Elements on rakennettu Bitcoinin koodipohjalle, se voi myös toimia testialustana itse Bitcoin-protokollaan tehtäville muutoksille.

Seuraavassa luetellaan joitakin Elementsin tärkeimpiä ominaisuuksia.

#### Luottamukselliset liiketoimet

Oletusarvoisesti kaikki Elementsin osoitteet on suojattu käyttämällä Luottamuksellisia tapahtumia. Sulkeminen on prosessi, jossa siirrettävän omaisuuden määrä ja tyyppi on kryptografisesti piilotettu kaikilta muilta paitsi osallistujilta ja niiltä, joille he haluavat paljastaa sulkemisavaimen.

#### Liikkeeseenlasketut varat

Issued Assets on Elements mahdollistaa monentyyppisten omaisuuserien myöntämisen ja siirtämisen verkon osallistujien välillä. Liikkeeseen laskettu omaisuuserä hyötyy myös luottamuksellisista transaktioista, ja kuka tahansa, jolla on asianmukainen uudelleenjulkaisutunniste, voi laskea sen uudelleen liikkeeseen tai tuhota sen.

#### Federoitu 2-suuntainen tappi

Elements on yleiskäyttöinen lohkoketjualusta, joka voidaan myös "kiinnittää" olemassa olevaan lohkoketjuun (kuten Bitcoiniin), jotta omaisuuseriä voidaan siirtää kahteen suuntaan ketjusta toiseen. Toteuttamalla Elements sivuketjuna voit kiertää joitakin pääketjun luontaisia ominaisuuksia ja säilyttää samalla pääketjussa suojattujen omaisuuserien tarjoaman turvallisuuden.

#### Allekirjoitetut lohkot

Elements käyttää vahvaa allekirjoittajien liittoa, jota kutsutaan lohkojen allekirjoittajiksi, jotka allekirjoittavat ja luovat lohkoja luotettavasti ja ajallaan. Tämä poistaa PoW-louhintaprosessin transaktioviiveen, joka on altis suurelle lohkojen aikavaihtelulle sen satunnaisen poisson-jakauman vuoksi. Federated Block Signing -prosessilla saavutetaan luotettava lohkojen luominen ilman, että tarvitaan kolmannen osapuolen luottamusta tai laskennalliseen "algoritmiin" perustuvaa louhintaa.

Elements lisää kaikki nämä ominaisuudet Bitcoin Core -koodipohjan päälle, laajentaa pääketjun protokollan kykyä ja mahdollistaa uusia liiketoimintakäyttötapauksia, kun se otetaan käyttöön sivuketjuna tai itsenäisenä lohkoketjuratkaisuna.

# Elementti

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Miten Elements toimii

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

![Video](https://youtu.be/v0lzmfH81AY?si=V-xDWfmDLKyBcdPs)

Elements tarjoaa teknisen ratkaisun ongelmiin, joita lohkoketjun käyttäjät kohtaavat päivittäin: transaktioiden viive, yksityisyyden puute ja korvaavuuden riski.

Elements voittaa nämä ongelmat käyttämällä Federated Block Signing -järjestelmää ja Confidential Transactions -järjestelmää.

Toisin kuin Bitcoin-verkossa, Elementsin lohkojen allekirjoitusprosessi ei ole riippuvainen dynaamisista jäsenyyden moniosapuolista allekirjoituksista (DMMS) ja työn todisteista (PoW). Sen sijaan Elements käyttää allekirjoittajien vahvaa liittoa, jota kutsutaan lohkojen allekirjoittajiksi, jotka voivat allekirjoittaa ja luoda lohkoja luotettavasti ja oikea-aikaisesti. Tämä poistaa PoW-louhintaprosessin transaktioviiveen, joka on altis suurelle lohkojen aikavaihtelulle sen satunnaisen poisson-jakauman vuoksi. Federated Block Signing -prosessilla saavutetaan luotettava lohkojen luominen ilman, että tarvitaan kolmannen osapuolen luottamusta.

Elements voi toimia toisen lohkoketjun, kuten Bitcoinin, sivuketjuna tai itsenäisenä lohkoketjuna, joka ei ole riippuvainen muista verkoista.

Kun Strong Federationia käytetään sivuketjuna, se sisältää myös jäseniä, jotka mahdollistavat varojen turvallisen ja valvotun siirron pääketjun ja Elements-sivuketjun välillä. Varojen valvottua siirtoa kutsutaan Federated 2-Way Pegiksi, ja jäseniä, jotka suorittavat varainsiirron roolin, kutsutaan Watchmeneiksi.

Elements-verkon toimintaan liittyvät prosessit ja verkon osallistujien roolit ovat tärkeitä Elementsin toiminnan ymmärtämisen kannalta.

Riippumatta siitä, onko se toteutettu sivuketjuna vai itsenäisenä lohkoketjuna, Elements käyttää lohkojen tuottamiseen lohkojen allekirjoittajien vahvoja liittoja.

### Vahvat liitot

Elements käyttää konsensusmallia, jota Blockstream ehdotti ensimmäisenä, nimeltään Strong Federations. Vahva federaatio ei tarvitse todisteellista työtä (Proof of Work, PoW), vaan se luottaa ryhmän toisiaan epäluottavien osallistujien (Functionaries) yhteisiin toimiin.

Toimihenkilö voi toimia vahvassa federaatiossa seuraavissa tehtävissä: Lohkon allekirjoittajat ja vartijat. Lohkojen allekirjoittajia tarvitaan, jos käytät Elements-elementtejä joko sivuketju- tai erillisessä lohkoketjutilassa, kun taas vahteja tarvitaan vain sivuketjuasetuksissa.

Toiminnot, joita vahvan liiton jäsen voi suorittaa, on jaettu kahteen eri rooliin turvallisuuden parantamiseksi ja hyökkääjän aiheuttaman vahingon rajoittamiseksi.

Yhdistettynä näiden osallistujien roolit mahdollistavat sen, että Elements tarjoaa sekä nopean lohkojen luomisen (nopeampi ja lopullinen transaktiovahvistus) että varmoja, siirrettävissä olevia omaisuuseriä (sidotut omaisuuserät, jotka voidaan yhdistää suoraan toiseen lohkoketjuun).

Voit lukea Strong Federations -julkaisun täältä: https://blockstream.com/strong-federations.pdf

### Lohkon allekirjoittajat

Bitcoinin kaltainen lohkoketju laajenee, kun kuka tahansa lohkon allekirjoittajien dynaamiseen ryhmään kuuluva henkilö laajentaa ketjua osoittamalla, että hän on tehnyt työtä. Joukon dynaaminen luonne tuo mukanaan tällaisille järjestelmille ominaiset viiveongelmat.

Käyttämällä kiinteää allekirjoittajajoukkoa federoitu malli korvaa dynaamisen joukon tunnetulla joukolla, joka sisältää useita allekirjoituksia. Lohkoketjun laajentamiseen tarvittavien osallistujien määrän vähentäminen lisää järjestelmän nopeutta ja skaalautuvuutta, kun taas kaikkien osapuolten suorittama validointi varmistaa transaktiohistorian eheyden.

Federoitu lohkojen allekirjoittaminen koostuu useista vaiheista:


- Vaihe 1 - Lohkojen allekirjoittajat ehdottavat ehdokkaita lohkoiksi kiertävällä tavalla kaikille muille osallistuville lohkojen allekirjoittajille.
- Vaihe 2 - Kukin lohkon allekirjoittaja ilmoittaa aikomuksestaan allekirjoittamalla tietyn lohkoehdokkaan.
- Vaihe 3 - Jos ennakkositoumukselle asetettu kynnysarvo täyttyy, kukin lohkon allekirjoittaja allekirjoittaa lohkon.
- Vaihe 4 - Jos allekirjoituksen kynnysarvo (joka voi olla eri kuin vaiheessa 3) täyttyy, lohko hyväksytään ja lähetetään verkkoon. Vahva liitto on päässyt yhteisymmärrykseen viimeisimmästä transaktiolohkosta.
- Vaihe 5 - Seuraava lohkon allekirjoittaja ehdottaa seuraavaa lohkoa ja prosessi toistuu.

Koska vahvan liiton lohkojen muodostaminen ei ole todennäköistä ja perustuu kiinteään joukkoon allekirjoittajia, se ei koskaan joudu alttiiksi useiden lohkojen uudelleenjärjestelyille. Tämä vähentää merkittävästi transaktioiden vahvistamiseen liittyvää odotusaikaa. Se poistaa myös kannustimen louhia voittoa (eli lohkopalkkiot) ja korvaa sen kannustimella osallistua tuottavasti verkkoon, jossa kaikilla osallistujilla on sama yhteinen tavoite: varmistaa, että verkko toimii edelleen kaikkia hyödyttävällä tavalla. Tämä onnistuu ilman, että otetaan käyttöön yksittäinen vikapiste tai korkeampia luottamusvaatimuksia.

### Elementit sivuketjuna - Watchmen ja Federated 2-Way Pegin liitto

Sivuketjuna toimiessaan joillakin Vahvan liiton jäsenillä on ylimääräinen tehtävä, nimittäin vahtimestareiden rooli. Vartijat ovat vastuussa varojen siirtämisestä elementtien sivuketjuun ja sieltä pois, prosessit tunnetaan nimillä "Peg-In" ja "Peg-Out".

Jotta sivuketju toimisi luotettavalla tavalla, sen on annettava osallistujille mahdollisuus varmistaa, että omaisuuserien tarjonta on valvottua ja todennettavissa. Elements-sivuketju käyttää 2-Way Federated Peg -järjestelmää, joka mahdollistaa varojen kaksisuuntaisen siirron Elements-lohkoketjuun ja siitä pois. Tämä täyttää todistettavaa liikkeeseenlaskua ja ketjujen välisiä siirtoja koskevat vaatimukset.

Federated 2-way Peg -ominaisuuden ansiosta omaisuuserä voi olla yhteentoimiva muiden lohkoketjujen kanssa ja edustaa toisen lohkoketjun omaa omaisuuserää. Kiinnittämällä lohkoketjusi toiseen lohkoketjuun voit laajentaa pääketjun ominaisuuksia ja voittaa joitakin sen luontaisia rajoituksia.

Korkealla tasolla siirrot sivuketjuun tapahtuvat, kun joku lähettää pääketjun varoja osoitteeseen, jota kontrolloi Watchmen-lompakko, jossa on useita allekirjoituksia. Tämä käytännössä jäädyttää varat pääketjussa. Tämän jälkeen Watchmen validoi transaktion ja vapauttaa saman määrän siihen liittyvää omaisuutta sivuketjussa. Vapautetut varat lähetetään sivuketjun lompakkoon, joka voi todistaa, että se on oikeutettu alkuperäisiin pääketjun varoihin. Tämä prosessi siirtää tehokkaasti varoja pääketjusta sivuketjuun.

Siirtääkseen varoja takaisin pääketjuun käyttäjä tekee erityisen peg-out-transaktion sivuketjussa. Watchmen tarkastaa tämän transaktion ja allekirjoittaa sitten transaktiomenot pääketjussa hallitsemastaan monen allekirjoituksen lompakosta. Kynnysarvoisen määrän federaation osallistujia on allekirjoitettava, ennen kuin pääketjun transaktiosta tulee pätevä. Kun Watchmenit lähettävät omaisuuserän takaisin pääketjuun, he tuhoavat myös vastaavan määrän sivuketjussa, jolloin omaisuuserät siirtyvät tehokkaasti lohkoketjujen välillä.

## Elementtien määrittäminen ja käyttäminen

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

![Video](https://youtu.be/Frr_OjTEPAM?si=iq5XonJyQk8S5OAu)

Koska Elements perustuu Bitcoinin koodipohjaan, toimivan verkon osatekijät ovat hyvin samankaltaisia.

Itse Elements-solmun ohjelmisto on nimeltään `elementsd`, ja se toimii daemonina käyttäjän koneella. Daemon (tai palvelu Windowsissa) on ohjelma, joka toimii taustapalveluna ilman kirjautuneen käyttäjän suoraa ohjausta.

Huomautus: Tässä dokumentissa viitataan aina elementsd:hen daemon-versiona, mutta kaikki voidaan tehdä myös elements-qt:llä edellyttäen, että palvelinoptio on käytössä.

Elements-demoni muodostaa yhteyden verkon muihin solmuihin, jotta se voi vaihtaa transaktio- ja lohkotietoja, validoida ja laajentaa paikallista kopiota verkon lohkoketjusta.

Elements-ohjelmisto koostuu myös asiakasohjelmasta nimeltä `elements-cli`, jonka avulla voit lähettää RPC-komentoja (Remote Procedure Call) elementsd:lle komentoriviltä. Tätä voidaan käyttää esimerkiksi lompakon saldon kyselyyn, transaktio- tai lohkotietojen tarkasteluun tai transaktion lähettämiseen. Tämän asetusten pitäisi olla tuttuja kaikille, jotka ovat käyttäneet Bitcoinin vastaavia bitcoind- ja bitcoin-cli-ohjelmia.

Koska Elements-solmua voidaan konfiguroida syöttämällä parametreja käynnistyksen yhteydessä tai konfigurointitiedoston kautta, on mahdollista, että samassa koneessa on käynnissä useampi kuin yksi instanssi. Tämä on hyödyllistä testaus- ja kehitystarkoituksiin, sillä voit luoda oman paikallisen verkon yhdelle koneelle, jolloin jokaisella Elements-solmulla on oma kopio lohkoketjun tiedoista, se hallinnoi omaa vahvistamattomien voimassa olevien transaktioiden varastoaan ja kuuntelee RPC-pyyntöjä eri porteissa.

### Elementtien koodivarasto ja yhteisö

Elements on avoimen lähdekoodin projekti, ja sen lähdekoodi löytyy Elementsin GitHub-arkistosta osoitteessa https://github.com/ElementsProject/elements. Arkisto sisältää lähdekoodin elementsd- ja elements-cli-ohjelmille sekä niitä tukevat asennus- ja rakennustyökalut, testisarjan ja jonkin verran opetusdokumentaatiota.

Koodivarastoa täydentää myös https://elementsproject.org -sivusto, joka on yhteisölle suunnattu resurssi, joka sisältää selityksiä siitä, mikä Elements on ja miten se toimii, sekä kattavan opetusosion. Ohjeessa keskitytään Elementsin opetteluun komentoriviltä saatavien esimerkkien avulla ja näytetään, miten sen päälle voi rakentaa yksinkertaisia työpöytä- ja verkkosovelluksia. Sivustolla luetellaan myös suosittuja Elements-yhteisön keskustelufoorumeita, ja se on itse GitHubissa, mikä mahdollistaa yhteisön osallistumisen sivuston sisältöön.

Käyttääksesi Elements-ohjelmaa koneellasi sinun on ensin kloonattava (ladattava kopio) lähdekoodista, asennettava kaikki koodin sisältämät riippuvuudet ja lopuksi rakennettava demonin ja asiakkaan suoritettavat tiedostot. Tämän jälkeen Elements-ohjelmisto on valmis konfiguroitavaksi ja ajettavaksi.

## Solmujen ja verkon määrittäminen

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

Elements-solmulle voidaan antaa käynnistyksen yhteydessä konfiguraatioasetuksia, joilla voidaan muuttaa sen tapaa toimia, validoida tietoja, muodostaa yhteyksiä muihin solmuihin ja alustaa lohkoketjun tiedot.

Asetukset ladataan joko määritetystä `elements.conf`-tiedostosta tai annetaan parametreina komentorivin kautta.

Joitakin asioita voidaan muuttaa näiden parametrien avulla:


- Itsenäisissä lohkoketjutoteutuksissa käytettävän oletusvarallisuuden nimi.
- Alkuperäisen luodun omaisuuserän numero.
- Omaisuuserä, jota käytetään maksettaessa transaktiomaksuja verkossa.
- Lohkoketjun datatiedostojen säilytyspaikka.
- RPC-tunnukset, joita käytetään yhteyden muodostamiseen Bitcoin-solmuun.
- Kynnysarvo "n of m", joka on saavutettava, ja kelvolliset julkiset avaimet, jotka voivat allekirjoittaa lohkoja.
- Skripti, joka tarvitsee tyydytystä, jotta varoja voidaan siirtää sivuketjuun ja sieltä pois.
- Otetaanko yhteys Bitcoin-solmuun sivuketjuna vai ei.

Monet näistä ovat osa verkon konsensussääntöjä, joten on tärkeää, että niitä sovelletaan kaikkiin solmuihin käynnistyksen yhteydessä. Joitakin niistä voidaan muuttaa ketjun alustamisen jälkeen, mutta jotkin niistä on korjattava sen jälkeen, kun niitä on käytetty ketjun alustamiseen.

Parametrien käyttöä käsitellään myöhemmin kurssilla sitä mukaa kuin ne liittyvät kuhunkin osioon.

### Perustoiminnot komentorivillä

Tällä kurssilla näytetään esimerkkejä, joissa käytetään `elements-cli`-ohjelmaa tekemään RPC-kutsuja yhteen tai useampaan Elements-solmuun. Tämä tehdään terminaali-istunnosta käsin, ja komentojen lyhentämiseksi käytetään `alias`-olioita. Tämän sopimuksen mukaan, kun näet jotain seuraavien komentojen kaltaista:

```bash
e1-dae
e1-cli getnewaddress
```

`e1-dae` ja `e1-cli` ovat itse asiassa typografinen oikotie, joka käyttää terminaalin `alias`-ominaisuutta. `e1-dae` ja `e1-cli` todella korvataan, kun komento suoritetaan, ja suoritettava komento on samanlainen kuin:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

Yllä näemme kutsun käynnistää Elements-demoni ja kutsun elements-cli-ohjelmille, jotka sijaitsevat `$HOME/elements/src`-hakemistossa, sekä parametrin `datadir` arvon. `datadir`-parametrin avulla voimme kertoa daemonille ja asiakasohjelmille, missä niiden konfigurointitiedostot sijaitsevat, ja daemonille, missä sen kopio lohkoketjusta säilytetään. Koska ne jakavat konfigurointitiedoston, asiakas voi tehdä RPC-kutsuja daemonille.

Käyttämällä yllä olevaa komentoa uudestaan, mutta eri `datadir`-arvolla, voimme käynnistää useamman kuin yhden Elementsin instanssin, joista jokaisella on oma erillinen kopio lohkoketjusta ja konfiguraatioasetuksista. Tällä konventiolla käytämme kurssilla aliaksia `e2-dae` ja `e2-cli` viittaamaan eri datadir-hakemistoon kuin e1:n. Joten yllä oleva esimerkki toiselle `e2`-instanssillemme olisi:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

Tämän avulla voimme suorittaa kaikenlaisia toimintoja, kuten omaisuuserien välittämistä solmujen välillä, omaisuuserien myöntämistä ja sokeutumisen käytön tarkistamista saman verkon eri solmujen välisissä luottamuksellisissa transaktioissa.

# Elementin käyttäminen Käytännön käyttötapaus

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Luottamukselliset liiketoimet

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

![Video](https://youtu.be/-by2xBtXQeE?si=7bLo_geGn3qh7MXN)

Tässä osiossa opit käyttämään Elements-ohjelman Luottamukselliset tapahtumat -ominaisuutta.

Kaikki Elementsin osoitteet on oletusarvoisesti sokkoutettu käyttämällä luottamuksellisia transaktioita, jotka pitävät siirrettyjen varojen määrän ja tyypin näkyvissä vain transaktion osallistujille (ja niille, joille he haluavat paljastaa sokkoutusavaimen), mutta takaavat silti kryptografisesti, että kolikoita ei voida käyttää enempää kuin niitä on käytettävissä.

### Luottamukselliset osoitteet ja luottamukselliset liiketoimet

Kun luot uuden osoitteen Elementsissä komennolla `getnewaddress`, se luodaan oletusarvoisesti luottamuksellisena osoitteena.

Luottamuksellisten transaktioiden havainnollistamiseksi e2 lähettää itselleen varoja ja yrittää sitten tarkastella e1:n transaktiota. Tämä osoittaa Elementsin tapahtumien luottamuksellisen luonteen.

Jokainen Elements-solmun luoma uusi osoite on oletusarvoisesti luottamuksellinen. Voimme osoittaa tämän saamalla e2:n tuottamaan uuden osoitteen.

```
e2-cli getnewaddress
```

Huomaa, että osoite alkaa kirjaimella e1. Tämä tunnistaa sen luottamukselliseksi osoitteeksi. Osoitteen tarkempi tarkastelu getaddressinfo-komennolla antaa lisätietoja osoitteesta.

```
e2-cli getaddressinfo <address>
```

Näet, että on olemassa confidential_key-ominaisuus, joka kertoo, että kyseessä on luottamuksellinen osoite.

Confidential_key on julkinen sokaiseva avain, joka lisätään itse luottamukselliseen osoitteeseen. Tästä syystä luottamuksellinen osoite on niin pitkä.

Siihen liittyy myös ei-luottamuksellinen osoite. Jos haluat käyttää tavallisia, ei-luottamuksellisia tapahtumia Elementsissä, varat on lähetettävä tähän osoitteeseen lq1-etuliitteellä varustetun osoitteen sijasta.

Voimme nyt pyytää e2:ta lähettämään varoja luomaansa osoitteeseen. Tämä osoittaa myöhemmin, että e1, joka ei ole yksi transaktion osapuolista, ei voi nähdä transaktion yksityiskohtia.

```
e2-cli sendtoaddress <address>
```

Huomaa tapahtuman tunnus. Vahvista tapahtuma.

```
e2-cli -generate 101
```

Tarkastellaan tapahtumaa, jossa e2 lähetti itselleen varoja, e2:n itsensä näkökulmasta.

```
e2-cli gettransaction <txid>
```

Kun selaat tapahtuman tietoja ylöspäin, näet, että e2 voi tarkastella lähetettyjä ja vastaanotettuja summia sekä siirrettyä omaisuuserää. Näet myös amountblinder- ja assetblinder-ominaisuudet, joita käytetään yksityiskohtien sulkemiseen muilta solmuilta, jotka eivät ole mukana tapahtumassa.

Tarkistaaksemme saman tapahtuman tiedot e1:stä meidän on ensin saatava tapahtuman tiedot.

```
e1-cli getrawtransaction <txid>
```

Se palauttaa raa'at tapahtuman tiedot. Jos tarkastelet vout-osiota, näet, että siellä on kolme tapausta. Kaksi ensimmäistä ovat vastaanotto- ja vaihtomäärät, ja kolmas on transaktiomaksu. Näistä kolmesta summasta maksu on ainoa, jossa voit nähdä arvon, koska maksu on aina sokkouttamaton elementeissä.

### Sokeat avaimet

Kahdessa ensimmäisessä vout-osiossa näkyvät arvosummien "sokeat vaihteluvälit" ja maksusitoumustiedot, jotka toimivat todisteena toteutuneen omaisuuden todellisesta määrästä ja tyypistä.

Vaikka e2:n yksityinen avain tuotaisiin e1:n lompakkoon, e1 ei silti pystyisi näkemään siirrettyjen varojen määriä ja tyyppejä, koska se ei edelleenkään tiedä e2:n käyttämää sokeuttavaa avainta. Todistamme tämän tuomalla e2:n lompakon käyttämän yksityisen avaimen e1:n lompakkoon. Ensin meidän on vietävä avain e2:sta

```
e2-cli dumpprivkey <address>
```

Tuo se sitten e1:een.

```
e1-cli importprivkey <privkey>
```

Nyt voimme todistaa, että e1 ei edelleenkään näe arvoja.

```
e1-cli gettransaction <txid>
```

Se näyttää tx-määräksi 0, vaikka se oli itse asiassa 1.

Jotta voisimme nähdä todellisen, viivaamattoman arvon, tarvitsemme sokaisuavaimen. Tätä varten viemme ensin sokeusavaimen e2:sta.

```
e2-cli dumpblindingkey <address>
```

Tuo se sitten e1:een.

```
e1-cli importblindingkey <address> <blinding key>
```

Nyt kun saamme tapahtuman tiedot e1:stä.

```
e1-cli gettransaction <txid>
```

Se osoittaa, että kun sokaiseva avain on tuotu, voimme nyt nähdä tapahtuman todellisen arvon 1.

Tässä jaksossa olemme nähneet, että sulkemisavaimen käyttö piilottaa tapahtuman varojen määrän ja tyypin ja että oikean sulkemisavaimen tuominen paljastaa nämä arvot. Käytännössä sulkemisavain voidaan antaa esimerkiksi tilintarkastajalle, jos osapuolen hallussa olevien varojen määrät ja tyypit on tarkistettava. Elementsin Confidential Transactions -ominaisuus mahdollistaa myös "vaihteluvälien todentamisen". Valikoimatodisteilla voidaan todistaa, että omaisuuserän määrä on tietyllä alueella, ilman että varsinaista määrää tarvitsee paljastaa.

Olemme myös nähneet, että Luottamukselliset tapahtumat ovat valinnaisia, mutta ne ovat oletusarvoisesti käytössä, kun uusi osoite luodaan.

Siinä kaikki tältä oppitunnilta; onnea tietokilpailuun ja nähdään seuraavalla oppitunnilla!

## Liikkeeseenlasketut varat

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

![Video](https://youtu.be/XnY4WZUNSs4?si=dG8I5OoSh_0EBdvL)

Tässä osiossa opit käyttämään Elements-ohjelman Issued Assets -ominaisuutta.

Issued Assets mahdollistaa monentyyppisten omaisuuserien liikkeeseen laskemisen ja siirtämisen Elements-verkon osallistujien välillä. Mikä tahansa verkon solmu voi laskea liikkeeseen omia omaisuuseriä. Liikkeeseenlaskut voivat edustaa minkä tahansa omaisuuserän, kuten tositteiden, kuponkien, valuuttojen, talletusten, joukkovelkakirjojen, osakkeiden jne. vaihdettavaa omistusta. Issued Assets avaa mahdollisuuden rakentaa luotettavia pörssejä, optioita ja muita kehittyneitä älykkäitä sopimuksia, joissa käytetään itse liikkeeseen laskettuja omaisuuseriä.

Liikkeeseen laskettu omaisuuserä hyötyy myös luottamuksellisista transaktioista, ja kuka tahansa, jolla on siihen liittyvä token, voi laskea ne uudelleen liikkeeseen.

Ensimmäiseksi tarvitsemme pääsyn kahteen Elements-solmuun, joita kutsumme nimillä e1 ja e2. Solmujen lohkoketjut on nollattu ja oletusvarallisuus jaettu niiden kesken.

Nämä kaksi solmua ovat samassa paikallisverkossa ja yhteydessä toisiinsa, joten ne jakavat samat transaktiot transaktiomempoolissaan ja identtiset lohkoketjut. Vaikka ne toimivat samassa koneessa, on syytä huomata, että ne eivät jaa samoja varsinaisia lohkoketjutiedostoja. Kukin solmu hallinnoi omaa paikallista kopiotaan lohkoketjusta, joka sisältää saman transaktiohistorian, koska ne ovat konsensuksessa ja noudattavat samoja protokollasääntöjä keskenään.

Aloitetaan tarkistamalla kunkin solmun näkemys verkon nykyisistä omaisuuserien liikkeeseenlaskuista.

Tämä tehdään komennolla listissuances.

```
e1-cli listissuances
e2-cli listissuances
```

Kuten näet, molemmissa solmuissa on sama liikkeeseenlaskuhistoria. Molemmat näyttävät yhden omaisuuserän, 21 miljoonan Bitcoinin alkuperäisen liikkeeseenlaskun, joka luotiin ketjun perustamisen yhteydessä. Voit nähdä omaisuuserän heksatunnuksen yllä olevan komennon suorittamisen tuloksissa ja myös omaisuuserälle annetun merkinnän, joka on "bitcoin".

On syytä huomata, että oletusarvolle annetaan aina etiketti, kun ketju alustetaan. Kun julkaiset omia omaisuuseriäsi, voit asettaa niille itse nimilaput, minkä teemme pian. Ennen kuin voimme tehdä sen, meidän on julkaistava oma omaisuuserämme.

Pyydämme e1:tä antamaan uuden omaisuuserän. Tämä tehdään komennolla issueasset.

```
e1-cli issueasset 100 1 false
```

`issueasset` hyväksyy 3 parametria.

Liikkeeseen laskettavan uuden omaisuuserän määrä, olemme käyttäneet 100. Luotavien tokenien määrä (tokeneita käytetään omaisuuserän määrien uudelleen liikkeeseen laskemiseen), joista valitsimme 1. Viimeinen parametri kertoo Elementsille, luodaanko omaisuuserän liikkeeseenlasku joko sokkoutettuna vai sokkouttamattomana. Käytämme sokkouttamatonta vaihtoehtoa, koska haluamme tarkastella liikkeeseenlaskun määriä e2:sta hetken kuluttua, joten annamme arvoksi false.

Komennon suorittaminen palauttaa tietoja liikkeeseenlaskusta. Näihin kuuluvat transaktiotunniste, josta voit ottaa kopion myöhempää käyttöä varten, omaisuuserän yksilöllinen heksanarvo ja omaisuuserän merkin yksilöllinen heksanarvo.

Luo lohko liikkeeseenlaskutapahtuman vahvistamiseksi.

```
e1-cli -generate 1
```

Suorita komento `listissuances` uudelleen e1:n kohdalla.

```
e1-cli listissuances
```

Tämä osoittaa, että e1 on nyt tietoinen kahdesta liikkeeseenlaskusta, Bitcoinin alkuperäisestä liikkeeseenlaskusta ja äskettäin liikkeeseen lasketusta omaisuuserästä, josta näemme 100 kappaletta. Huomaa uuden omaisuuserän heksan arvo ja se, että siihen ei liity omaisuuserän nimikettä, kuten bitcoinin liikkeeseenlaskuun.

Tarkista e2:n luettelo tunnetuista liikkeeseenlaskuista uudelleen.

```
e2-cli listissuances
```

Tämä osoittaa, että e2 ei ole tietoinen e1:n tekemästä varojen liikkeeseenlaskusta. Se näkee vain bitcoinin alkuperäisen liikkeeseenlaskun, jonka se jo näki.

Tämä johtuu siitä, että e2 ei tiedä eikä tarkkaile osoitetta, johon uusi omaisuuserä lähetettiin, kun e1 antoi sen.

On syytä huomata, että vaikka e2 ei näe itse liikkeeseenlaskua, e1 voi silti lähettää e2:lle osan omaisuuserästä. Uusi omaisuuserä näkyisi tällöin käytettävissä olevana saldona e2:n lompakossa, vaikka se ei tietäisikään alkuperäisestä liikkeeseenlaskusta.

Jotta e2 voisi nähdä todellisen liikkeeseenlaskun (ja näin ollen liikkeeseenlasketun määrän), meidän on lisättävä osoite e2:een tarkkailtavaksi osoitteeksi.

Tätä varten meidän on selvitettävä osoite, johon omaisuuserä lähetettiin. Tätä varten käytämme aiemmin kopioitua transaktiotunnusta ja annamme e1:n hakea kyseisen transaktion tiedot, jotta voimme selvittää oikean osoitteen, jonka voimme lisätä e2:n lompakon tarkkailulistalle.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

Vierittämällä ylöspäin transaktiotietojen heksanarvon ohi näet osoitteen, joka sai 100 uutta hyödykettä, ja se tunnistetaan sen heksanarvon perusteella.

Ota osoite ja kopioi se, jotta voimme tuoda sen e2:een.

Tuodaan nyt tämä osoite e2:een. Tätä varten käytämme komentoa importaddress.

```
e2-cli importaddress <the-issued-to-address>
```

Tarkistetaan nyt e2:n liikkeeseenlaskijaluettelo.

```
e2-cli listissuances
```

Näet, että äskettäin liikkeeseen laskettu omaisuuserämme on nyt mukana luettelossa. E2-solmu pystyy myös määrittämään liikkeeseen lasketun omaisuuserän määrän sekä siihen liittyvän tokenin määrän, koska liikkeeseenlasku oli sokkouttamaton liikkeeseenlasku. Jos haluat ottaa käyttöön omaisuuserän ID:n ja nimen yhdistämisen Elementsissä, pysäytä ensin Elements.

```
e1-cli stop
```

Käynnistä se sitten uudelleen lisäparametrin avulla, joka yhdistää omaisuuserän heksan annettuun merkintään. Näin solmu voi näyttää meille tietoja omaisuuserästä ihmiselle ymmärrettävässä muodossa. Voit halutessasi lisätä tämän elementit.conf-tiedoston loppuun, jolloin sinun ei tarvitse lisätä argumenttia daemonille joka kerta, kun käynnistät sen. Esimerkiksi:

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

Käytämme tässä kuitenkin argumenttimenetelmää.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Kysytään solmusta uudelleen liikkeeseenlaskujen luetteloa.

```
e1-cli listissuances
```

Tämä osoittaa, että omaisuuserän heksamääräisen arvon yhdistäminen etikettiin toimii. Tarkistetaan uudelleen e2-solmun liikkeeseenlaskujen luettelo.

```
e2-cli listissuances
```

Näet, että e2-solmulla ei ole pääsyä tähän tarraan, koska tarrat ovat vain sen solmun käytettävissä, joka ne asetti. Voimme tosiaan määrittää samalle omaisuuserän kuusikolle eri merkinnän e2:ssa kuin e1:ssä. Pysäytä ensin solmu e2.

```
e2-cli stop
```

Käynnistetään uudestaan eri merkinnällä, joka on määritetty uuden omaisuuserän heksan kohdalle.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Luettelo e2:n liikkeeseenlaskuista.

```
e2-cli listissuances
```

Omaisuuserän merkinnät ovat paikallisia kussakin solmussa, ja muut verkon solmut tunnistavat vain omaisuuserän kuusikirjaimen.

Tunnisteen yhdistäminen omaisuuserän kuusikirjaimeksi on hyödyllistä, kun suoritetaan toimintoja, kuten transaktioita ja lompakon saldokyselyjä, koska se mahdollistaa lyhyen tavan viitata omaisuuserään. Jos esimerkiksi haluaisimme lähettää osan uudesta omaisuudestamme (määrän 10) e1:stä e2:een ilman etiketin käyttöä.

Ensin meidän on saatava osoite, johon lähetämme omaisuuserän.

```
e2-cli getnewaddress
```

Käytä sitten komentoa sendtoaddress.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Vahvista transaktio luomalla lohko.

```
generate 1
```

Tarkistetaan, että omaisuuserä vastaanotettiin e2:lla.

```
e2-cli getwalletinfo
```

Näemme, että omaisuuserä on todellakin vastaanotettu.

Huomaa, että e2 kartoittaa vastaanotetun omaisuuserän heksan ja näyttää sen omalla merkinnällään. Helpompi tapa tehdä sama asia olisi käyttää e1:n etikettiä lähetettäessä.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

Kulissien takana Elements muuntaa paikalliset merkinnät heksamääräisiksi arvoiksi, mikä helpottaa julkaistujen kohteiden käyttöä.

Tässä jaksossa olemme nähneet, miten omaisuuseriä annetaan ja merkitään. Seuraavassa jaksossa tarkastelemme liikkeeseen lasketun omaisuuserän uudelleen liikkeeseen laskemista ja hävittämistä.

## Omaisuuden uudelleenjulkaiseminen

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

![Video](https://youtu.be/5em79YHtYk0?si=rhponm6Hw9AB6RJp)

Tässä osiossa opit, miten voit laskea liikkeelle lisää jo liikkeelle laskettua omaisuuserää ja miten voit tuhota tietyn määrän liikkeelle laskettua omaisuuserää.

Tarve laskea omaisuuserä uudelleen liikkeeseen (luoda lisää) tai tuhota tietty määrä omaisuuserää on todennäköinen, kun omaisuuserä edustaa jotakin sellaista, jonka tarjonta ei ole kiinteää. Tämä voisi koskea esimerkiksi omaisuuseriä, jotka edustavat holvissa säilytettävää kultaa; kun kultayksikköjä liikkuu holviin ja sieltä pois, holvin tarjontaa edustavaa omaisuuserää on mukautettava vastaavasti ylös- tai alaspäin.

Omaisuuserän määrän uudelleen liikkeeseenlasku edellyttää, että omistat siihen liittyvän tokenin, joka luotiin omaisuuserän rinnalle, kun se alun perin laskettiin liikkeeseen.

Kun luodaan lisää omaisuuserää, Sillä ei ole väliä, mikä solmu antoi omaisuuserän alun perin, kunhan omaisuuserän määrän uudelleen liikkeeseen laskeva solmu omistaa sen, mitä kutsutaan yleisesti omaisuuserän uudelleenjulkaisu-tunnisteeksi. Tarkastelemme, miten uudelleenjulkaisutunniste luodaan alun perin, miten sitä käytetään omaisuuserän määrän uudelleenjulkaisemiseen ja miten uudelleenjulkaisutunniste siirretään muille solmuille, jotta myös niillä on oikeus laskea omaisuuserä uudelleen liikkeeseen.

Tarvitsemme pääsyn kahteen Elements-solmuun, joita kutsumme nimillä e1 ja e2. Solmujen lohkoketjut on nollattu ja oletusvarallisuus jaettu niiden kesken.

Annamme e1:n laskea liikkeelle 100 kappaletta uutta omaisuuserää ja luoda 1 uudelleen liikkeeseenlaskukuponki samaa omaisuuserää varten. Luomme liikkeeseenlaskun sokkouttamattomana esimerkin yksinkertaistamiseksi. Mennään siis eteenpäin ja lasketaan omaisuuserä ja siihen liittyvä uudelleenjulkaisutunniste liikkeeseen.

```
e1-cli issueasset 100 1 false
```

Huomaa omaisuuserän tunnus ja (uudelleen liikkeeseen laskettavan) tunnisteen tunnus.

Koska aiomme myöhemmin laskea uudelleen liikkeeseen lisää omaisuuseriä e2:sta, meidän on kirjattava muistiin transaktiotunniste, jolla omaisuuserä laskettiin liikkeeseen, ja käytettävä sitä tuodaksemme osoitteen, johon omaisuuserä lähetettiin.

Vahvista tapahtuma.

```
e1-cli -generate 1
```

Tarkistamme nyt tapahtuman tiedot komennolla gettransaction:

```
e1-cli gettransaction <txid>
```

Vierittämällä ylöspäin transaktion datan heksan ohi näet, että transaktiossa e1 sai 1 uudelleenjulkaisutunnisteen ja 100 siihen liittyvää omaisuuserää.

Ota kopio osoitteesta, jotta voimme tuoda sen e2:een.

Ja nyt tuon osoitteen e2:n lompakkoon.

```
e2-cli importaddress <address>
```

Nyt nähdään, että sekä e1 että e2 ovat tietoisia omaisuuserän liikkeeseenlaskusta.

```
e1-cli listissuances
e2-cli listissuances
```

Tällä hetkellä e1:llä on hallussaan tietty määrä omaisuuserää ja 1 uudelleenmyyntimerkki, mutta e2:lla ei.

```
e1-cli getwalletinfo
```

Huomaa myös, että e1:llä on vähemmän oletusvarallisuutta kuin aiemmin, koska se maksoi pienen summan transaktiomaksujen kattamiseksi. Tämän summan e1:n on määrä periä, kun luotu lohko erääntyy yli 100 lohkon syvyydessä.

```
e2-cli getwalletinfo
```

Koska e1:llä on hallussaan uudelleenmyyntimerkintä, se voi myydä sitä lisää. Tämä tehdään käyttämällä komentoa reissueasset. Annetaan e1:n laskea uudelleen liikkeelle 100 uutta omaisuuserää.

```
e1-cli reissueasset <asset-id> 100
```

Uudelleentarkastaminen toimi.

```
e1-cli getwalletinfo
```

Näet, että e1:n hallussa on nyt odotetusti 200 omaisuuserää.

Koska e2:lla ei ole hallussaan uudelleenjulkaisutunnuksen määrää, he saavat virheen, jos he yrittävät laskea omaisuuserän uudelleen liikkeeseen.

```
e2-cli reissueasset <asset-id> 100
```

Huomaa virheilmoitus.

Voimme tarkastella e1:n uudelleenjulkaisun yksityiskohtia komennolla listissuances.

```
e1-cli listissuances
```

Huomaa lippu `is_reissuance`.

Jos nyt lähetämme e2:lle määrän uudelleenjulkaisu-tokenia, he voivat itse laskea uudelleen liikkeeseen tietyn määrän omaisuuserää. Ensin tarvitsemme osoitteen, johon lähetämme sen. Kannattaa huomata, että uudelleenjulkaisu-tokenia kohdellaan saldojen lähettämisessä ja näyttämisessä samalla tavalla kuin mitä tahansa muuta omaisuuserää elementeissä ja että se voidaan myös jakaa pienempiin nimellisarvoihin kuten mikä tahansa muu omaisuuserä, joten meidän ei tarvitse lähettää yhtä uudelleenjulkaisu-tokenia e2:lle, jotta se voisi laskea omaisuuserän uudelleen liikkeeseen. Mikä tahansa nimellisarvo riittää. Luodaan e2:lle osoite, johon se voi vastaanottaa uudelleenmyyntimerkin.

```
e2-cli getnewaddress
```

Lähetä sitten osa RIT:stä e1:stä e2:een.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Vahvista tapahtuma.

```
e1-cli -generate 1
```

Näemme nyt, että e2:lla on hallussaan 0,1, joka sille lähetettiin.

```
e2-cli getwalletinfo
```

Tämä tarkoittaa sitä, että e2 voi nyt laskea liikkeeseen enemmän lompakossaan olevaan RIT:iin liittyviä varoja. Annamme e2:n laskea liikkeeseen 500 omaisuuserää.

```
e2-cli reissueasset <asset-id> 500
```

Tarkista uudelleentarkastuksen tulos.

```
e2-cli getwalletinfo
```

Näet, että e2:lla on nyt uudelleen liikkeeseen laskettu summa lompakkosaldossaan ja että itse RIT:tä ei kuluteta omaisuuserien uudelleenlaskutuksen yhteydessä.

Varojen määrän tuhoaminen on asia, jonka voi tehdä kuka tahansa, jolla on hallussaan vähintään tuhottava määrä, eikä sitä säännellä uudelleenjulkaisemisen merkillä.

```
e2-cli destroyamount <asset-id>
e2-cli getwalletinfo
```

Tässä osiossa olemme nähneet, miten omaisuuserä lasketaan liikkeeseen ja miten käytetään uudelleenjulkaisutunnusta, joka luodaan valinnaisesti osana omaisuuserän liikkeeseenlaskua. Olemme myös nähneet, miten uudelleenjulkaisu-tokenin siirtäminen on yhtä yksinkertaista kuin minkä tahansa muun omaisuuserän siirtäminen ja että minkä tahansa määrän uudelleenjulkaisu-tokenia hallussaan pitäessään sen haltija saa oikeuden laskea liikkeeseen lisää siihen liittyvää omaisuuserää. Siksi on erittäin tärkeää valvoa, kenellä on pääsy reissuance-tokeneihin verkostossasi. Olemme myös nähneet, miten omaisuuserän määrä voidaan tuhota ja että tätä prosessia ei valvota reissuance-tokenin hallussapidolla.

# Element Federation

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Lohkon allekirjoittaminen

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

![Video](https://youtu.be/kxWX91fCnus?si=KItm_Am3_RrBcLBN)

Elements tukee federoitua allekirjoitusmallia, jonka avulla voit määrittää niiden vahvan federaation jäsenten määrän, joiden on allekirjoitettava ehdotettu lohko, jotta lohko olisi kelvollinen.

Aikaisemmin ja esimerkin helpottamiseksi olemme luoneet lohkoja käyttämällä `generate`-komentoa, jonka ei ole tarvinnut täyttää usean allekirjoituksen vaatimusta, jotta verkko olisi hyväksynyt luodut lohkot kelvollisiksi.

Asetamme solmumme niin, että ne vaativat 2-of-2-monisignaalisten lohkojen luomista. Tämä asetetaan käyttämällä signblockscript-parametria, joka voidaan lisätä konfigurointitiedostoon tai siirtää solmuun käynnistyksen yhteydessä. Jotta voimme alustaa ketjun tällä parametrilla, meidän on ensin rakennettava skripti, josta se koostuu.

Teemme tämän käyttämällä joitakin olemassa olevia solmuja, tallennamme niiden tuottamat tiedot ja pyyhimme sitten ketjun, jotta voimme käynnistää sen uudelleen signblockscript-parametrin avulla. Tämä on tarpeen, koska skripti on osa verkon konsensussääntöjä, ja se on asetettava ketjun alustuksen yhteydessä. Sitä ei voi lisätä myöhemmin jo olemassa olevaan ketjuun.

Tarvitsemme pääsyn kahteen Elements-solmuun, joita kutsumme nimillä e1 ja e2. Solmujen lohkoketjut on nollattu ja oletusvarallisuus jaettu niiden kesken.

Varmista, että parametri con_max_block_sig_size on asetettu suureksi arvoksi elements.conf-tiedostossa, muuten lohkojen allekirjoittaminen epäonnistuu myöhemmin tässä osassa. Olemme asettaneet con_max_block_sig_size=2000 tätä opetusta varten.

Koska nollaamme lohkoketjun ja pyyhimme e1:een ja e2:een liittyvät lompakot, meidän on otettava kopio osoitteista, julkisista ja yksityisistä avaimista, joita käytämme lohkojen allekirjoituskomentosarjan luomiseen, jotta voimme käyttää niitä myöhemmin.

Ensin jokaisen lohkon allekirjoitussolmun on luotava uusi osoite, josta sinun on otettava kopio.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Sitten meidän on poimittava julkiset avaimet osoitteista ja kirjattava ne muistiin myöhempää käyttöä varten.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Pura sitten yksityiset avaimet, jotka tuomme myöhemmin uudelleen, jotta solmut voivat allekirjoittaa lohkot sen jälkeen, kun lohkoketju ja lompakkotiedot on alustettu uudelleen.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Nyt meidän on luotava lunastusskripti, jossa on 2:2 moninkertaista allekirjoitusta koskevat vaatimukset. Tämä tehdään käyttämällä komentoa createmultisig ja antamalla ensimmäiseksi parametriksi 2 ja sitten kaksi julkista avainta. Näiden avainten omistusoikeus on todistettava myöhemmin, kun lohko luodaan.

Kumpikin solmu, e1 tai e2, voi tuottaa multisigin.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

Näin saamme redeemscriptin, jonka voit kopioida myöhempää käyttöä varten.

Nyt meidän on pyyhittävä olemassa oleva lohkoketju ja lompakon tiedot, jotta voimme aloittaa alusta uudella signblockscriptillä osana ketjun konsensussääntöjä. Tämän vuoksi meidän piti ottaa aiemmin kopio joistakin tiedoista, kuten yksityisistä avaimista, joita käytetään uudessa ketjussa lohkojen allekirjoittamiseen. Sinun on tehtävä tämä ennen kuin jatkat.

Kun olemassa olevat lompakko- ja ketjutiedot on poistettu, voimme nyt käynnistää solmut ja saada ne alustamaan uuden ketjun käyttämällä signblockscript-parametria. Annetaan -evbparams=dynafed:0:::: poistaa dynafed-aktivointi käytöstä, koska emme tarvitse tätä kehittynyttä ominaisuutta tässä esimerkissä.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Nyt meidän on tuotava aiemmin tallentamamme yksityiset avaimet, jotta solmumme voivat allekirjoittaa ja auttaa täydentämään kaikki ehdotetut lohkot.

```
e1-cli importprivkey <e1-priv-key>
e2-cli importprivkey <e2-priv-key>
```

Generointikomennon käytön pitäisi nyt aiheuttaa virhe, koska se ei täytä vaadittuja lohkojen allekirjoitussääntöjä, joita solmumme nyt noudattavat.

```
e1-cli -generate 1
```

Ehdottaakseen uutta lohkoa kumpikin solmu voi kutsua komentoa getnewblockhex. Tämä palauttaa uuden lohkon heksadesimaalin, joka on allekirjoitettava, ennen kuin mikään verkon solmu hyväksyy sen.

```
e1-cli getnewblockhex
```

Muista, että komento vain luo ehdotetun lohkon, se ei luo sitä.

Vahvistaaksemme tämän voimme nähdä, että lohkoketjussamme ei tällä hetkellä ole lohkoja.

```
e1-cli getblockcount
```

Jos yritämme lähettää lohkon hex allekirjoittamatta sitä ensin.

```
e1-cli submitblock <block-hex>
```

Saamme viestin, jossa kerrotaan, että lohkotodiste on virheellinen. Tämä johtuu siitä, että kaksi vaaditusta kahdesta osapuolesta ei ole vielä allekirjoittanut sitä.

Pyydetään siis e1 allekirjoittamaan ehdotettu lohko.

```
e1-cli signblock <block-hex>
```

Pyydä e2:ta allekirjoittamaan kuusikirja.

```
e2-cli signblock <block-hex>
```

Huomaa, että e2 ei allekirjoita tulostetta, joka on luotu e1:n allekirjoitettua ehdotetun lohkon. Molemmat allekirjoittavat ehdotetun lohkon kuusikirjaimen riippumatta toistensa tuloksista.

Nyt meidän on yhdistettävä e1:n ja e2:n lohkosignaatiot. Kumpikin solmu voi tehdä tämän, ne tarvitsevat vain toisen solmun allekirjoitetun lohkon kuusiosoitteen.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

Näet, että combineblocksigs-komento antaa allekirjoitetun lohkon heksan sekä tilan complete, joka kertoo, että lohkon heksa on valmis lähetettäväksi.

Nyt kumpikin solmu voi lähettää valmiin lohkon hex. Annamme e1:n tehdä sen.

```
e1-cli submitblock <combined-signed-hex>
```

Tarkistetaan, että lähetys oli pätevä.

```
e1-cli getblockcount
e2-cli getblockcount
```

Näet, että sekä e1 että e2 ovat hyväksyneet lohkon kelvolliseksi ja lisänneet sen lohkoketjun paikallisten kopioidensa kärkeen.

Yhteenveto prosessista. Tässä jaksossa meillä on:


- Ehdotettu lohko.
- Jokainen solmu allekirjoitti sen.
- Yhdistetty allekirjoitukset.
- Tarkistetaan, että allekirjoitukset ovat kelvollisia ja täyttävät ketjun lunastuskynnyksen.
- Toimitettu kortteliin.

Jokainen verkon solmu validoi lohkon ja lisäsi sen lohkoketjun paikalliseen kopioonsa.

### Lohkon sijoittaminen

Vaikka prosessi vaikuttaa aluksi monimutkaiselta, lohkojen allekirjoittamisjärjestys Elementsissä on aina sama, ja alkuasetukset on tehtävä vain kerran:

1. Alkuasetukset (tehdään kerran)

2. Luodaan usean allekirjoituksen osoite nimeltä `signblockscript` käyttäen Federated Block Signersin julkisia avaimia.

3. Tämän lunastusskriptin avulla käynnistetään uusi lohkoketju.

4. Lohkotuotanto (käynnissä)

5. Ehdotetut lohkot luodaan ja vaihdetaan allekirjoitettaviksi.

Kun tietty määrä allekirjoittajia on allekirjoittanut ehdotetun lohkon, se yhdistetään ja toimitetaan verkkoon. Jos se täyttää ketjun `signblockscript`-kriteerit, solmut hyväksyvät sen kelvolliseksi lohkoksi.

## Elementti sivuketjuna

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

![Video](https://youtu.be/egYzj4N8CB8?si=v7_-IXsjHPE-ARDe)

Elements on avoimen lähdekoodin yleiskäyttöinen lohkoketjualusta, joka voidaan myös "liittää" olemassa olevaan lohkoketjuun, kuten Bitcoiniin. Kun Elements on liitetty toiseen lohkoketjuun, sen sanotaan toimivan "sivuketjuna". Sivuketjut mahdollistavat varojen kaksisuuntaisen siirron ketjusta toiseen. Kun Elements toteutetaan sivuketjuna, voit kiertää joitakin pääketjun luontaisia rajoituksia ja säilyttää samalla pääketjussa suojattujen varojen tarjoaman turvallisuuden.

Sivuketju on tietoinen pääketjusta ja sen transaktiohistoriasta, mutta pääketju ei ole tietoinen sivuketjusta, eikä sitä tarvita sen toimintaan. Näin sivuketjut voivat innovoida ilman rajoituksia tai pääketjun protokollan parannusehdotuksiin liittyviä viiveitä. Sen sijaan, että sitä yritettäisiin muuttaa suoraan, pääprotokollan laajentaminen antaa itse pääketjulle mahdollisuuden pysyä turvallisena ja erikoistuneena, mikä tukee sivuketjun sujuvaa toimintaa.

Laajentamalla Bitcoinin toiminnallisuutta ja hyödyntämällä sen taustalla olevaa tietoturvaa Elements-pohjainen sivuketju pystyy tarjoamaan uusia toimintoja, jotka eivät aiemmin olleet pääketjun käyttäjien saatavilla. Esimerkki tuotantokäytössä olevasta Elements-pohjaisesta sivuketjusta on Liquid Network.

Jotta voimme alustaa Elements-lohkoketjun sivuketjuksi, meidän on käytettävä federated peg -skriptiparametria. Tämä parametri voidaan asettaa solmun konfigurointitiedostossa tai välittää käynnistyksen yhteydessä.

Liitännäisliitännäiskäsikirjoituksessa määritellään, mitkä vahvan liitännäisliiton jäsenet voivat suorittaa liitännäisliitännäis- ja liitännäisliitännäistoimintoja. Näitä toimihenkilöitä kutsutaan "vartijoiksi", sillä he tarkkailevat pää- ja sivuketjua kelvollisten peg-in- ja peg-out-tapahtumien varalta ja toimivat, jos ne ovat kelvollisia. "Peg-out" tarkoittaa kiinnitetyn omaisuuden siirtämistä sivuketjusta pääketjuun ja "peg-in" tarkoittaa kiinnitetyn omaisuuden siirtämistä pääketjusta sivuketjuun. Kun sanomme `siirrä sivuketjuun`, tarkoitamme itse asiassa sitä, että varat lukitaan pääketjun monisignatuuriosoitteeseen ja vastaava määrä omaisuutta luodaan Elements-sivuketjuun. Kun sanomme `move out of the sidechain`, tarkoitamme sitä, että varat tuhotaan Elementsin sivuketjussa ja vastaava määrä vapautetaan pääketjussa olevista lukituista varoista. Lupa peg-in- ja peg-out-toimintojen suorittamiseen edellyttää, että funktionaaliset toimijat todistavat federoidussa peg-skriptissä käytettyjen julkisten avainten omistusoikeuden. Tämä tehdään käyttämällä vastaavia yksityisiä avaimia.

Luodaksemme federoidun peg-skriptin meidän on siis ensin luotava jokaiselle solmulle julkinen avain. Meidän on myös tallennettava niihin liittyvät yksityiset avaimet myöhempää käyttöä varten, sillä meidän on pyyhittävä kaikki olemassa olevat ketjutiedot ja alustettava uusi ketju federated peg -skriptin avulla. Tämä johtuu siitä, että federated peg -skripti on osa sivuketjun konsensussääntöjä, eikä sitä voi soveltaa olemassa olevaan, ei-pegattuihin lohkoketjuihin myöhemmin.

Luodaan siis jokaiselle solmulle osoite, tallennetaan tarvittavat tiedot myöhempää käyttöä varten ja luodaan federated peg -skripti, jota käytämme myöhemmin sivuketjun alustamiseen.

Ensin jokaisen solmun, jotka toimivat verkossamme vartijoina, on luotava uusi osoite.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Sitten validoimme osoitteen julkisten avainten saamiseksi.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Hae sitten kuhunkin osoitteeseen liittyvät yksityiset avaimet.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Tallenna yksityinen ja julkinen avain myöhempää käyttöä varten.

Nyt meidän on pyyhittävä olemassa olevat lohkoketju- ja lompakkotiedot, koska aloitamme uuden ketjun federated peg -skriptin avulla. Voit tehdä tämän nyt. Älä unohda käynnistää Bitcoin-demonia, jota tarvitsemme peg-iniin.

Nyt voimme alustaa uuden ketjun federoidulla peg-skriptillä, joka on luotu aiemmin tallennettujen julkisten avainten avulla. Syöttämämme numerot, jotka ympäröivät julkisia avaimiamme, määrittelevät ja rajaavat käytettävien avainten määrän sekä avainten omistusoikeuden, joka on todistettava, jotta sivuketjuun voidaan liittää ja siitä voidaan poistua.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Nyt tuomme aiemmin tallentamamme yksityiset avaimet, jotta solmumme voivat myöhemmin allekirjoittaa ja suorittaa varojen siirron ketjujen välillä ja täyttää federated peg -skriptin vaatimukset.

```
e1-cli importprivkey <priv-key-1>
e2-cli importprivkey <priv-key-1>
```

Meidän on nyt kypsytettävä joitakin esteitä molemmissa ketjuissa. Lohkojen kypsyminen on sidontaprosessin vaatimus, sillä se suojaa lohkojen uudelleenjärjestelyiltä pääketjussa, jotka johtavat sidottujen varojen tarjonnan inflaatioon sivuketjussa.

Jotta tämä jakso keskittyisi federoituun pegiin, luomme lohkoja ilman edellisessä jaksossa tarkasteltua lohkojen allekirjoitusmallia ja palaamme käyttämään komentoa 'generate' uusien lohkojen luomiseen.

```
b-cli generate 101
e1-cli generate 1
```

Meidän ei välttämättä tarvitse luoda lohkoja elementtejä varten juuri nyt. Mutta luodaan yksi kuitenkin. Se on hyvä käytäntö mahdollisten epäjohdonmukaisuuksien välttämiseksi.

Nyt ketjumme on valmis kiinnitettäväksi. Peg-iniä varten meidän on luotava erityinen osoite komennolla getpeginaddress. Huomaa, että peg-in-osoitteen generoimisen getpeginaddressilla ja sen lunastamisen claimpeginilla tulisi kestää mahdollisimman vähän aikaa. peg-in-osoitteet eivät ole pitkäaikaiskestäviä, eikä niitä tulisi käyttää uudelleen.

```
e1-cli getpeginaddress
```

Näet, että komento luo uuden pääketjun osoitteen sekä uuden skriptin, joka on täytettävä, jotta peg-in-varoja voidaan lunastaa. Mainchain-osoite on `pay to script hash` -osoite, jota Watchmen-roolia Elements-verkossa hoitavat toimihenkilöt käyttävät.

Kuten getnewaddress, myös getpeginaddress lisää uuden salaisuuden kutsuvan solmun lompakkoon, joten lompakkotiedoston varmuuskopiointi on tärkeää ottaa huomioon solmujen hallintaprosessissa.

Lähetämme nyt joitakin bitcoineja pääketjusta sivuketjuun. Pääketjun regressiotestilompakossamme on jo jonkin verran varoja.

```
b-cli getwalletinfo
```

Näemme, että lompakossa on 50 bitcoinia. Lähetämme yhden bitcoinin pääketjusta sivuketjuun. Meidän on lähetettävä varat pääketjun osoitteeseen, jonka solmumme loi aiemmin.

```
b-cli sendtoaddress <e1-pegin-address>
```

Meidän on säilytettävä tämän tapahtuman tunniste, sillä tarvitsemme sitä myöhemmin todisteena rahoituksesta.

Näemme nyt, että pääketjun lompakon saldo on pienentynyt lähettämämme summan verran ja lisäksi pienen summan, joka kattaa transaktiomaksut.

```
b-cli getwalletinfo
```

Meidän on kypsytettävä transaktio uudelleen.

```
b-cli generate 101
```

Jotta Elements-solmumme voisi vaatia peg-in-varoja, meidän on saatava "todiste" siitä, että peg-in-tapahtuma on tehty. Kryptografinen todiste käyttää rahoitustapahtuman tunnusta merkel-polun laskemiseen ja todistaa, että tapahtuma on vahvistetussa lohkossa.

```
b-cli gettxoutproof '["<tx-id>"]'
```

Tarvitsemme myös raakatapahtumatiedot.

```
b-cli getrawtransaction <tx-id>
```

Kun meillä on todiste ja raakatiedot peg-in-transaktiosta, elementtisolmumme voi nyt vaatia peg-in-transaktiota käyttämällä raakatransaktiota ja transaktiotodistetta.

```
e1-cli claimpegin <raw> <proof>
```

Huomaa, että claimpeginille olisi voinut antaa valinnaisen kolmannen argumentin. Tämän kolmannen parametrin avulla voidaan määrittää sivuketjun osoite, johon haetut varat lähetetään. Esimerkissämme tätä ei tarvittu, koska kutsuimme komentoa samasta solmusta, joka omistaa osoitteen, johon vaaditut varat lähetetään.

Tarkistetaan e1:n saldo.

```
e1-cli getwalletinfo
```

Lohkon luominen väitteen vahvistamiseksi.

```
e1-cli generate 1
```

Tarkistetaan e1:n saldo.

```
e1-cli getwalletinfo
```

Näemme, että peg-in on onnistuneesti lunastettu.

Prosessi on samankaltainen. Osoite luodaan, siihen lähetetään varoja ja varat vapautetaan, jos tapahtuma on pätevä. Emme käsittele koko peg-out-prosessia, koska siihen liittyy työtä pääketjussa, joka ei kuulu tämän kurssin piiriin. Elements-tapahtumien vaiheet ovat seuraavat: Mainchainissa luodaan osoite.

```
b-cli getnewaddress
```

Varat lähetetään mainchain-osoitteeseen Elements-solmusta komennolla sendtomainchain.

```
e1-cli sendtomainchain <new-address> 1
```

Lohkon luominen tapahtuman vahvistamiseksi.

```
e1-cli generate 1
```

Tarkista solmun lompakon saldo.

```
e1-cli getwalletinfo
```

Ja katso, että saldo on pienentynyt.

Tässä jaksossa olemme nähneet, miten:


- Luo federated peg -skripti.
- Alustaa uusi ketju, joka käyttää käsikirjoitusta verkkokonsensuksen parametrisääntönä.
- Lähetä varoja pääketjusta sivuketjuun.
- Lunasta varat Elements-sivuketjussa.
- Ymmärrä, miten varojen lähettäminen takaisin pääketjuun aloitetaan.

### FederatedPegScript

Jotta Elements voisi toimia sivuketjuna, sen lohkoketjun genesis-lohko on luotava siten, että `fedpegscript` on paikallaan. Tämä tehdään antamalla `fedpegscript`-parametri solmun käynnistyksen yhteydessä. Skripti on sitten osa Elements-lohkoketjun konsensussääntöjä ja mahdollistaa peg-in- ja peg-out-pyyntöjen validoinnin ja toteuttamisen.

`fedpegscript` koostuu julkisista avaimista, joita hallitsevat ne, joilla on oikeus suorittaa peg-toimintoja. Seuraavassa on esimerkki 2:sta 2:een monialkakirjoitetun fedpeg-skriptin muodosta:

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Huomautus: Julkisten avainten ulkopuolella olevat merkit ovat rajoja, jotka ilmaisevat julkisen avaimen ja "n of m" -vaatimuksia. Esimerkiksi 1:1 fedpegscriptin malli olisi "5121<pub key 1>51ae".

### Peg-in

Ennen kuin Elements-sivuketju voi hyväksyä peg-inin, sillä on oltava riittävästi vahvistuksia pääketjussa. Tämä on välttämätöntä, jotta vältettäisiin Elements-sivuketjussa peggatun omaisuuserän tarjonnan inflaatio, joka voisi aiheutua pääketjun uudelleenjärjestelyistä.

Bitcoin-lohkoketjun kärjen lyhyet uudelleenjärjestelyt ovat odotettavissa osana Proof of Work (PoW) -konsensusmekanismin normaalia toimintaa. Näin ollen Elements hyväksyy peg-inin päteväksi vain silloin, kun se on riittävän syvällä Bitcoin-lohkoketjussa. Tämä estää Elementsiä hyväksymästä samaa peg-iniä useammin kuin kerran.

### Peg-Out

Peg-out tapahtuu, kun Elements-solmu kutsuu komentoa `sendtomainchain`, joka ottaa syötteenä pääketjun osoitteen (peg-out-kohde) sekä pegged assetin määrän, joka halutaan `withdrawn`. Tämä luo peg-out-transaktion sivuketjuun. Kun vartijoina toimivat Functionaryt havaitsevat, että peg-out-transaktio on vahvistettu sivuketjussa, he huolehtivat siitä, että omaisuuserä vapautetaan pääketjussa peg-out-kohteeseen, kuten opimme kurssin aiemmissa osioissa.

## Elementit itsenäisenä lohkoketjuna

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

![Video](https://youtu.be/u-3rV7DGtD0?si=G1__H0Uelf4sTUDM)

Tähän mennessä olemme tarkastelleet, miten Elementsia voidaan käyttää sivuketjuna. Se voi kuitenkin toimia myös itsenäisenä lohkoketjuratkaisuna, jolla on oma oletusarvoinen natiivi omaisuuserä. Tässä kokoonpanossa Elements-lohkoketju säilyttää edelleen kaikki sivuketjutoteutuksen ominaisuudet, kuten luottamukselliset transaktiot ja liikkeeseen lasketut omaisuuserät, mutta se ei tarvitse peg-in- tai peg-out-toimintoa oletusomaisuuserien määrän lisäämiseksi tai poistamiseksi kierrosta.

Tässä jaksossa käsitellään:

Alustaa uusi Elements-lohkoketju oletusarvoisella omaisuuserällä nimeltä `newasset`.

Määritä luotavaksi 1 000 000 `newasset` ja 2 uudelleenkirjoituskuponkia sitä varten.

Lunasta kaikki kuka tahansa voi käyttää `newasset` -kolikot.

Lunasta kaikki "newasset"-tavaramerkit, jotka kuka tahansa voi käyttää.

Lähetä omaisuuserä ja sen uudelleenjulkaisemisen merkki toisen solmun lompakkoon.

Julkaise uudelleen lisää 'newasset' molemmista solmuista.

Jotta Elements-verkko voidaan alustaa toimimaan itsenäisenä lohkoketjuna, jokainen solmu on käynnistettävä joillakin perusparametreilla. Niitä käytetään kertomaan solmulle, ettei se yritä validoida toisesta lohkoketjusta tulevia peg-ins, verkon oletusvarallisuuden nimi sekä oletusvarallisuuden ja siihen liittyvän uudelleenjulkaisu-tokenin luomiseksi tarvittava määrä.

Aloitamme nyt uuden ketjun käyttämällä näitä parametreja kahdessa yhdistetyssä Elements-solmussa. Nimeämme oletusarvopaperin `newasset` ja laskemme liikkeelle miljoona kappaletta ja kaksi `newasset`-reissuance-tunnusta.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Huomaa, että tässä käytetyt summat ovat pienimpiä nimellisarvoja, joita verkko voi hyväksyä, joten kaksisataa miljoonaa uudelleenjulkaisemismerkkiä vastaa itse asiassa kahta kokonaista merkkiä. Sama pätee alkuperäisten ilmaisten kolikoiden nimellisarvoon.

Tarkista solmun nykyiset lompakkosaldot.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Voimme nähdä, että alustaminen toimi oikein.

Kun varojen alkuperäinen liikkeeseenlasku on luotu siten, että "kuka tahansa voi käyttää", pyydämme e1:tä lunastamaan ne kaikki, jotta voimme poistaa e2:lta oikeuden käyttää niitä.

```
e1-cli getnewaddress
e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Huomaa, että lähetettäväksi omaisuuseräksi ei tarvitse määritellä newasset, koska se on jo oletusarvoisesti käytössä ja siten myös oletusarvoisesti käytössä verkkomaksujen maksamiseen.

Elementsissä voit lähettää useita eri omaisuuserätyyppejä samaan osoitteeseen, joten voimme käyttää uudelleen juuri luotua osoitetta oletusomaisuuden vastaanottamiseen ja käyttää sitä uudelleen liikkeeseen laskettavien kuponkien kohdeosoitteena.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Vahvista tapahtumat.

```
e1-cli generate 101
```

Tarkistamme nyt, että e1 on omaisuuserän ja sen uudelleenjulkaisemisen merkin ainoa haltija.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Kuten näemme, asia on todellakin näin.

Nyt lähetämme osan "newasset"-varoista e2:lle, jonka saldo on tällä hetkellä nolla.

```
e2-cli getnewaddress
e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Huomaa, että meidän ei tarvinnut määritellä lähetettävän omaisuuserän tyyppiä, koska `newasset` on luotu verkon oletusarvoisena omaisuuseränä

Lähetetään myös osa `newasset`:n uudelleenjulkaisutunnisteista e2:een.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Vahvista tapahtumat.

```
e1-cli generate 101
```

Voimme tarkistaa, että lompakot on päivitetty vastaavasti.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Julkaisemme nyt uudelleen osan e1:n oletusarvoista. Huomaa, että tämä on mahdollista tehdä initialreissuancetokens-käynnistysparametrin avulla. Jos se jätetään pois tai asetetaan nollaksi, tuloksena on oletusarvoinen omaisuuserä, jota ei voi myöhemmin julkaista uudelleen.

```
e1-cli reissueasset newasset 100
```

Pystyimme käyttämään nimikettä `newasset` sen sijaan, että olisimme joutuneet antamaan heksan id-arvon, koska elementtiketju nimittää aina oletusarvonsa.

Tarkistetaan, että oletusarvopaperin uudelleenjulkaisu toimi:

```
e1-cli generate 101
e1-cli getwalletinfo
```

Todistamme nyt, että koska e2:lla on hallussaan joitakin `newasset`-uudelleenjulkaisutunnisteita, se voi myös laskea uudelleen liikkeeseen oletusvarallisuuden.

```
e2-cli reissueasset newasset 100
```

Tarkistetaan, että e2:n suorittama oletusarvopaperin uudelleenjulkaisu toimi.

```
e2-cli generate 101
e2-cli getwalletinfo
```

Tässä osassa olemme perustaneet Elementsin itsenäiseksi lohkoketjuksi ja tarkistaneet, että perustoiminnot toimivat odotetusti.

Käytimme käynnistysparametreja:

Alusta uusi Elements-lohkoketju oletusarvoisella omaisuuserällä nimeltä 'newasset'.

Määritä ketjun alustuksen yhteydessä luotavan oletusarvopaperin määrä.

Luo joitakin oletusarvopaperin uudelleenjulkaisemisen merkkejä ja laske uudelleen liikkeeseen lisää oletusarvopaperia molemmista solmuista.

Erillisessä lohkoketju-elementtiverkossamme kaikki muut transaktiot toimivat samalla tavalla kuin kurssin pääjaksoissa käsitellyt esimerkit, mutta oletus- ja maksuvälineenä käytetään "newasset" eikä "bitcoin".

### Solmun käynnistys- ja ketjun alustamisparametrit

Jotta Elements-solmua voidaan käskeä toimimaan itsenäisenä lohkoketjuna, on käytettävä muutamia parametreja yhdessä. Tutustumme nyt kuhunkin niistä ja selvitämme, mitä ne tekevät.

#### `validatepegin=0`

Koska itsenäisen lohkoketjun ei tarvitse vahvistaa mitään peg-in- tai peg-out-transaktioita, meidän on poistettava nämä tarkistukset käytöstä. Tällä asetuksella sinun ei tarvitse käyttää Bitcoin-asiakasohjelmistoa tai tallentaa kopiota Bitcoin-lohkoketjusta, sillä Elements-verkko toimii itsenäisesti.

#### `defaultpeggedassetname`

Tämän avulla voit määrittää lohkoketjun alustuksen yhteydessä luodun oletusomaisuuden nimen.

#### `initialfreecoins`

Luodun oletusvarallisuuden määrä (Bitcoinin Satoshi-yksikkönä).

#### "Alkuperäiset liikkeeseenlaskukynät"

Luodun oletusarvopaperin uudelleenjulkaisutunnisteiden määrä (Bitcoinin Satoshi-yksikköä vastaavana). Ilman tätä on mahdotonta luoda lisää oletusvarallisuutta. Jos et halua, että oletusvarallisuutta on mahdollista luoda lisää, tämä voidaan asettaa nollaan tai jättää pois.

Näiden parametrien avulla solmun käynnistäminen näyttää jotakuinkin tältä:

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Perustoiminnot

Parametrilla `defaultpeggedassetname` annetaan oletusarvoisen omaisuuserän nimi. Ilman tätä asetusta oletusarvopaperin nimi on automaattisesti `bitcoin`. Aiemmissa osioissa, kun lähetimme itse myöntämiämme omaisuuseriä toiseen solmuun, meidän oli määritettävä joko omaisuuserän heksanumero tai paikallisesti käytetty omaisuuserän nimike kertoaksemme Elementsille, minkä omaisuuserän lähetimme. Koska `defaultpeggedassetname` pätee kaikissa solmuissa, meidän ei tarvitse nimetä sitä lähettäessämme, vaikka sen nimi ei olisikaan `bitcoin`. Jokainen toiminto, joka olisi aiemmin lähettänyt oletusarvoisesti `bitcoinin`, lähettää nyt sen, minkä oletusarvoisen omaisuuserän nimeksi valitsit.

Joten 10 uuden oletusarvon lähettäminen osoitteeseen on yhtä yksinkertaista kuin:

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

Jos olet myös antanut solmulle arvon `initialreissuancetokens`, joka on suurempi kuin nolla, voit myös laskea liikkeeseen lisää oletusarvoista omaisuutta, mikä ei ole mahdollista, jos käytät Elementsia sivuketjuna.

Tätä varten minkä tahansa solmun, jolla on hallussaan tietty määrä oletusarvoon liittyvää tokenia, tarvitsee vain antaa komento muodossa:

```
e1-cli reissueasset <default asset name> <amount>
```

Käyttämällä edellä mainittuja parametreja voit käyttää Elementsia itsenäisenä lohkoketjuna, jolla on oma oletusarvoinen omaisuuserä ja joka on erotettu Bitcoinista ja muista lohkoketjuista.

## Päätelmä

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

![Video](https://youtu.be/CTMdamTZBBM?si=16LBcXvN4pBfC7lr)

Tällä kurssilla olemme oppineet, että Elements on avoimen lähdekoodin verkkoprotokolla, joka voidaan toteuttaa toisen lohkoketjun sivuketjuna tai itsenäisenä lohkoketjuratkaisuna.

Olemme nähneet, että Elementsin lähdekoodia ja verkkosivustoa (https://github.com/ElementsProject/elements) ylläpidetään GitHubissa ja että on olemassa yhteisön keskustelufoorumeita, kuten Build On L2 (https://community.liquid.net/c/developers/) tai Liquid Developers Telegram (https://t.me/liquid_devel), joilla voi oppia lisää sovellusten käyttöönotosta ja kehittämisestä Elementsissä ja Liquidissa. Keskeisiä ominaisuuksia, kuten luottamuksellisia transaktioita ja liikkeeseen laskettuja varoja, käsiteltiin, samoin kuin sitä, miten vahvan federaation jäsenet mahdollistavat federoidun lohkojen allekirjoittamisen ja 2-Way Peg -mekanismin.

Seuraava askel on haastaa itsesi kumulatiivisella tietokilpailulla, joka kattaa kaikki aiemmat osiot, ja aloittaa sitten Elementtien matka... onnea matkaan!

# Päätelmä

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Arvostelut & arvostelut

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Päätelmä

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

Onnittelut tämän kurssin suorittamisesta!

Olemme innoissamme siitä, että olet saavuttanut tämän virstanpylvään oppimismatkallasi. Olet saanut omistautumisesi ja sitoutumisesi ansiosta arvokkaita tietoja ja taitoja, jotka auttavat sinua ammatillisessa kehityksessäsi.