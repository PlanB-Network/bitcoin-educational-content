---
name: BTC Pay Serverin hallinta
goal: Konfiguroi BTC Pay Server -instanssi paikalliselle yritykselle
objectives:
- Ymmärtää BTCPay Serverin roolin perusteet maksujen käsittelyssä
- Hallita BTCPay Serverin konfigurointiprosessin sisäinen toiminta
- Ottaa käyttöön BTCPay Server pilvi- ja solmupohjaisissa ympäristöissä
- Tulla BTC Pay Server -operaattoriksi
---
# Matka taloudelliseen suvereniteettiin

Luottamus on hauras, erityisesti kun kyse on rahasta. Tämä johdantokurssi opastaa sinut BTCPay Serverin läpi, tehokkaan työkalun, jonka avulla voit vastaanottaa Bitcoin-maksuja luottamatta kolmansiin osapuoliin. Opit BTCPay Server -operaattoriksi ryhtymisen perusteet

Alekoksen ja Basin luoma ja melontwistin ja asi0:n mukauttama kurssi paljastaa, kuinka yksityishenkilöt ja yritykset rakentavat vaihtoehtoja perinteisille maksujärjestelmille. Olitpa utelias Bitcoinista tai valmis pyörittämään maksuinfrastruktuureja yrityksille, löydät käytännön taitoja, jotka haastavat vallitsevan tilanteen. Oletko valmis tutkimaan, miltä taloudellinen riippumattomuus todella näyttää?
+++
# Johdanto


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Kurssin yleiskatsaus


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


Tervetuloa POS 305 -kurssille BTCPay Serverillä!


Tämän koulutuksen tavoitteena on opettaa sinulle, miten asennat, konfiguroit ja käytät BTCPay Serveriä yrityksessäsi tai organisaatiossasi. BTCPay Server on avoimen lähdekoodin ratkaisu, jonka avulla voit käsitellä Bitcoin-maksuja itsenäisesti, turvallisesti ja kustannustehokkaasti. Tämä kurssi on suunnattu ensisijaisesti edistyneille käyttäjille, jotka haluavat hallita BTCPay Serverin omatoimista isännöintiä, jotta se voidaan integroida täysin päivittäisiin toimintoihin.


**Luku 1: BTCPay-palvelimen esittely**

Aloitamme BTCPay Serverin yleisesittelyllä, johon kuuluu kirjautumisnäyttö, käyttäjätilien hallinta ja uuden kaupan luominen. Tämä esittely auttaa sinua ymmärtämään BTCPay Server Interface:n ja hahmottamaan perusominaisuudet, joita tarvitset tämän työkalun käytön aloittamiseen.


**Luku 2: Johdanto Bitcoin-avaimien suojaamiseen**

Bitcoin-varojesi turvallisuus on erittäin tärkeää. Tässä osiossa käsittelemme kryptografisten avainten tuottamista, laitteistolompakoiden käyttöä avainten suojaamiseen ja sitä, miten avainten kanssa voi olla vuorovaikutuksessa BTCPay Serverin kautta. Opit myös, miten konfiguroida BTCPay Server Lightning Wallet -palvelin maksutapahtumien optimoimiseksi.


**Luku 3: BTCPay-palvelin Interface**

Tämä osa opastaa sinut BTCPay Serverin käyttäjän Interface:n käyttöönotossa. Opit navigoimaan kojelaudalla, määrittämään myymälä- ja palvelinasetuksia, hallitsemaan maksuja ja hyödyntämään integroituja liitännäisiä. Tavoitteena on antaa sinulle tarvittavat työkalut, joilla voit mukauttaa asennuksesi omien tarpeidesi mukaan.


**Luku 4: BTCPay-palvelimen määrittäminen**

Lopuksi keskitymme BTCPay Serverin käytännön asennukseen eri ympäristöissä. Käytitpä sitten LunaNodea, Voltagea tai Umbrel-solmua, opit olennaiset vaiheet BTCPay Serverin käyttöönottoon ja konfigurointiin ottaen huomioon kunkin ympäristön erityispiirteet.


Oletko valmis hallitsemaan BTCPay Serveriä ja kasvattamaan liiketoimintaasi? Mennään!


## Kriittistä suosiota tekijän Bitcoin- ja BTCPay-palvelimelle


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


Aloitetaan ymmärtämällä, mikä BTCPay Server on ja mistä se on peräisin. Arvostamme läpinäkyvyyttä ja tiettyjä standardeja luottamuksen muodostamiseksi Bitcoin-avaruudessa.

Avaruushanke rikkoi nämä arvot. BTCPay Serverin johtava kehittäjä Nicolas Dorier otti tämän henkilökohtaisesti ja lupasi poistaa ne käytöstä. Tässä sitä nyt ollaan, monta vuotta myöhemmin, ja työskentelemme tätä tulevaisuutta kohti täysin avoimen lähdekoodin periaatteella joka päivä.


> Tämä on valhetta, luottamukseni sinuun on murtunut, teen sinusta tarpeettoman.
> Nicolas Dorier

Nicolasin sanojen jälkeen oli aika aloittaa rakentaminen. Merkittävä määrä työtä tehtiin sen eteen, mitä nyt kutsumme BTCPay Serveriksi. Useammat ihmiset halusivat osallistua tähän työhön. Tunnetuimpia ovat r0ckstardev, MrKukks, Pavlenex ja ensimmäinen ohjelmistoa käyttänyt kauppias, astupidmoose.


Mitä avoimella lähdekoodilla tarkoitetaan ja mitä tällaiseen hankkeeseen kuuluu?


FOSS on lyhenne sanoista Free & Open-Source Software. Ensin mainittu viittaa ehtoihin, joiden mukaan kuka tahansa voi kopioida, muokata ja jopa levittää ohjelmistoversioita (jopa voiton tavoittelemiseksi). Jälkimmäisellä tarkoitetaan lähdekoodin avointa jakamista ja yleisön kannustamista osallistumaan ja parantamaan sitä.

Tämä houkuttelee kokeneita käyttäjiä, jotka ovat innostuneita osallistumaan ohjelmistojen kehittämiseen, joita he jo käyttävät ja joista he saavat arvoa, ja tämä on lopulta osoittautunut onnistuneemmaksi käyttöönotossa kuin omistusoikeudelliset ohjelmistot. Se on yhdenmukainen Bitcoin:n eetoksen kanssa, jonka mukaan "tieto kaipaa vapautta" Se kokoaa yhteen intohimoisia ihmisiä, jotka muodostavat yhteisön, ja se on yksinkertaisesti hauskempaa. Kuten Bitcoin, FOSS on väistämätön.


### Ennen kuin aloitamme


Tämä kurssi koostuu useista osista. Monista osista huolehtii luokanopettajasi, demoympäristöt, joihin saat pääsyn, isännöidyn palvelimen itsellesi ja mahdollisesti verkkotunnuksen. Jos suoritat tämän kurssin itsenäisesti, ota huomioon, että DEMO-merkinnällä varustetut ympäristöt eivät ole käytettävissäsi.

HUOM. Jos seuraat tätä kurssia luokkahuoneessa, palvelimien nimet saattavat vaihdella luokkahuoneen kokoonpanosta riippuen. Palvelimien nimissä olevat muuttujat saattavat tästä syystä olla erilaisia.


### Kurssin rakenne


Jokaisessa luvussa on tavoitteet ja osaamisen arviointi. Tällä kurssilla käsittelemme kutakin näistä ja esitämme yhteenvedon keskeisistä ominaisuuksista kunkin oppituntikokonaisuuden (eli luvun) lopussa. Kuvituksilla annetaan visuaalista palautetta ja vahvistetaan keskeisiä käsitteitä visuaalisesti. Tavoitteet asetetaan kunkin oppituntilohkon alussa. Nämä tavoitteet ovat tarkistuslistaa laajempia. Ne antavat sinulle oppaan uusiin taitoihin. Osaamisen arvioinnit ovat asteittain haastavampia, kun BTCPay-palvelimen asennus on valmis.


### Mitä opiskelijat saavat kurssin mukana?


BTCPay-palvelinkurssin avulla opiskelija voi ymmärtää Bitcoin:n tekniset ja ei-tekniset perusperiaatteet. BTCPay Server -palvelimen kautta saatava laaja Bitcoin:n käyttökoulutus antaa opiskelijoille mahdollisuuden käyttää omaa Bitcoin-infrastruktuuriaan.


### Tärkeitä verkko-osoitteita tai yhteystietoja


BTCPay Server Foundation, jonka ansiosta Alekos ja Bas saivat kirjoittaa tämän kurssin, sijaitsee Tokiossa, Japanissa. BTCPay Server -säätiöön voi ottaa yhteyttä luetellun verkkosivuston kautta.



- https://foundation.btcpayserver.org
- Liity virallisiin keskustelukanaviin: https://chat.btcpayserver.org


## Johdanto Bitcoin:een


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Bitcoin:n ymmärtäminen luokkahuoneharjoituksen avulla


Tämä on luokkahuoneharjoitus, joten jos osallistut kurssille itse, et voi suorittaa sitä, mutta voit silti käydä tämän harjoituksen läpi. Tämän tehtävän suorittamiseen tarvitaan vähintään 9-11 henkilöä.


Harjoitus alkaa BBC:n esittelyn "How Bitcoin and the Blockchain works" katsomisen jälkeen.


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


Tähän harjoitukseen tarvitaan vähintään yhdeksän osallistujaa. Harjoituksen tavoitteena on antaa fyysinen käsitys Bitcoin:n toiminnasta. Pelaamalla kutakin roolia verkossa voitte oppia vuorovaikutteisesti ja leikkimielisesti. Tässä harjoituksessa ei käytetä Lightning Network:ää.


### Esimerkki: Vaatii 9 / 11 henkilöä


Roolit ovat:



- 1 asiakas
- 1 kauppias
- 7-9 Bitcoin-solmua


**Asetukset ovat seuraavat:**


Asiakkaat ostavat tuotteen kaupasta Bitcoin:llä.


**Skenaario 1 - Perinteinen pankkijärjestelmä**



- Järjestä:
  - Katso kaaviot/selitykset liitteenä olevasta Figjam - [toimintakaavio] (https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Hanki kolme vapaaehtoista opiskelijaa esittämään asiakkaan (Alice), kauppiaan (Bob) ja pankin rooleja.
- Näyttele tapahtumien kulku:
  - Asiakas - selaa verkkokauppaa ja löytää haluamansa tuotteen 25 dollarilla ja ilmoittaa kauppiaalle haluavansa ostaa sen
  - Kauppias pyytää maksua.
  - Asiakas lähettää korttitiedot kauppiaalle
  - Kauppias - välittää pankille tiedot (yksilöi sekä omat että henkilöllisyytensä/tiedot), joissa pyydetään maksamaan seuraavat maksut
  - Pankki kerää tietoja asiakkaasta ja kauppiaasta (Alice ja Bob) ja tarkistaa, että asiakkaan saldo on riittävä.
  - Vähentää 25 \$ Alice:n tililtä, lisää 24 \$ Bob:n tilille, ottaa 1 \$ palvelusta
  - Kauppias saa pankilta hyväksynnän ja lähettää tuotteen asiakkaalle.
- Kommentit:
  - Bob:lla ja Alice:llä on oltava pankkisuhde.
  - Pankki kerää tunnistetietoja sekä Bob:stä että Alice:stä.
  - Bank ottaa osuuden.
  - Pankin on luotettava siihen, että se säilyttää koko ajan jokaisen osallistujan rahat.


**Skenaario 2 - Bitcoin-järjestelmä**



- Järjestä:
  - Katso kaaviot/selitykset liitteenä olevasta Figjam - [toimintakaavio] (https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Korvaa pankki yhdeksällä oppilaalla, jotka toimivat tietokoneen (Bitcoin solmua/kaukoputkea) roolissa verkossa, joka korvaa pankin.
- Kullakin yhdeksästä tietokoneesta on täydellinen historiatieto kaikista koskaan tehdyistä tapahtumista (siten tarkat saldot ilman väärennöksiä) sekä joukko sääntöjä:
  - Tarkista, että tapahtuma on asianmukaisesti allekirjoitettu (thekeyfitsthelock)
  - Lähettää ja vastaanottaa päteviä transaktioita verkon vertaisverkoille ja hylätä virheelliset transaktiot (mukaan lukien sellaiset, joissa yritetään käyttää samat varat kahdesti)
- Päivitä/täydennä tietueita säännöllisesti "satunnaiselta" tietokoneelta saaduilla uusilla tapahtumilla, jos kaikki sisältö on kelvollinen (huom. jätämme toistaiseksi huomiotta Proof of Work-komponentin yksinkertaisuuden vuoksi), muutoin hylkäämme nämä ja jatkamme kuten ennenkin, kunnes seuraava "satunnainen" tietokone lähettää päivityksen
  - Oikea määrä palkittiin, jos sisältö oli pätevä.
- Näyttele tapahtumien kulku:
  - Asiakas - selaa verkkokauppaa ja löytää haluamansa 25 dollarin hintaisen tuotteen ja ilmoittaa kauppiaalle haluavansa ostaa sen
  - Kauppias pyytää maksua lähettämällä asiakkaalle Invoice/Address:n Wallet:sta.
  - Asiakas - rakentaa transaktion (lähettää 25 dollarin arvosta BTC:tä kauppiaan toimittamaan Address:ään) ja lähettää sen Bitcoin-verkkoon.
- Tietokoneet - vastaanottavat tapahtuman ja tarkistavat sen:
  - Address:ssä on vähintään 25 dollaria BTC:tä, joka lähetetään Address:stä
  - Tapahtuma on allekirjoitettu asianmukaisesti ("avattu" asiakkaan toimesta)
  - Jos näin ei ole, tapahtumaa ei siirretä verkon kautta, ja jos näin on, se siirretään ja pidetään odottamassa.
  - Kauppiaat voivat tarkistaa, että maksutapahtuma on vireillä ja odottaa.
- Yksi tietokone valitaan "satunnaisesti" ehdottamaan ehdotetun transaktion viimeistelyä lähettämällä sen sisältävä "lohko"; jos se on oikein, se saa BTC-palkkion.
  - VALINNAINEN/LISÄVALINTAINEN - sen sijaan, että tietokone valitaan satunnaisesti, voidaan simuloida Mining:tä antamalla tietokoneiden heittää noppaa, kunnes jokin ennalta määrätty tulos tulee (esim. valitaan se, joka heittää ensimmäisenä tuplakuutosia)
  - Se voi myös näytellä, mitä tapahtuisi, jos kaksi tietokonetta voittaisi suunnilleen samanaikaisesti, jolloin ketju jakautuisi.
  - Tietokoneet tarkistavat voimassaolon, päivittävät/lisäävät tietueita pääkirjoihinsa, jos säännöt täyttyvät, ja lähettävät transaktiolohkon vertaisverkoille.
  - Satunnaisesti valittu tietokone saa palkkion kelvollisen lohkon ehdottamisesta.
  - Kauppias tarkistaa, että maksutapahtuma saatiin päätökseen, joten varat vastaanotettiin ja tuote lähetettiin asiakkaalle.
- Kommentit:
  - Huomaa, että aiempaa pankkisuhdetta ei tarvittu.
  - Kolmatta osapuolta ei tarvita helpottamaan; korvataan säännöillä/kannustimilla.
  - Kukaan ei saa kerätä tietoja välittömän Exchange:n ulkopuolelta, ja osallistujien välillä on vaihdettava vain tarvittava määrä (esim. lähetys Address).
  - Ihmisten (muiden kuin tuotteen lähettävän kauppiaan) välillä ei tarvita luottamusta, kuten käteisostoksilla monin tavoin.
  - Raha on suoraan yksityishenkilöiden omistuksessa.
  - Bitcoin Ledger on kuvattu yksinkertaisuuden vuoksi dollareina, mutta todellisuudessa se on BTC.
  - Simuloimme yhden transaktion lähettämistä, mutta todellisuudessa verkossa on useita transaktioita vireillä, ja lohkoihin kuuluu tuhansia transaktioita kerralla. Solmut varmistavat myös, että vireillä ei ole kaksoiskuljetustransaktioita (tässä tapauksessa hylkäisin kaikki paitsi yhden).
- Huijausskenaariot:
  - Entä jos asiakkaalla ei olisi 25 BTC dollaria?
    - Ne eivät pystyisi luomaan tapahtumaa, koska "lukituksen avaaminen" ja "Ownership" ovat sama asia, ja tietokoneet tarkistavat, että tapahtuma on asianmukaisesti allekirjoitettu; muussa tapauksessa ne hylkäävät sen
  - Entä jos satunnaisesti valittu tietokone yrittää "muuttaa Ledger:n"?
    - Lohko hylättäisiin, koska kaikilla muilla tietokoneilla on täydellinen historia ja ne huomaisivat muutoksen, joka rikkoisi yhtä niiden säännöistä.
    - Satunnainen tietokone ei saisi palkkiota, eikä heidän lohkonsa transaktioita viimeisteltäisi.


## Tietojen arviointi


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### KA Luokkahuonekeskustelu


Keskustele joistakin luokkahuoneharjoituksessa tehdyistä liiallisista yksinkertaistuksista toisen skenaarion yhteydessä ja kuvaa tarkemmin, mitä varsinainen Bitcoin-järjestelmä tekee.


### KA Sanaston kertaaminen


Määrittele seuraavat edellisessä jaksossa esitellyt keskeiset termit:



- Solmu
- Mempool
- Vaikeusaste Tavoite
- Lohko


**Keskustelkaa ryhmässä joidenkin muiden termien merkityksestä:**


Blockchain, transaktio, tuplalaskutus, Bysantin kenraaliongelma, Mining, Proof of Work (PoW), Hash Funktio, Block reward, Blockchain, pisin ketju, 51% hyökkäys, ulostulo, ulostulon lukitus, muutos, Satoshi, julkinen/yksityinen avain, Address, julkisen avaimen salaus, digitaalinen allekirjoitus, Wallet


# BTCPay-palvelimen esittely


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## BTCPay Serverin kirjautumisnäytön ymmärtäminen


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### Työskentely BTCPay-palvelimen kanssa


Tämän kurssikokonaisuuden tavoitteena on saada yleinen ymmärrys BTCPay Server -ohjelmistosta. Jaetussa ympäristössä on suositeltavaa seurata opettajan esittelyä ja tutustua BTCPay Server -kurssikirjaan, jotta voit seurata opettajan mukana. Opit luomaan Wallet:n useiden eri menetelmien avulla. Esimerkkeinä ovat Hot Wallet-asetukset ja BTCPay Server Vaultin kautta yhdistetyt laitteistolompakot. Nämä tavoitteet tapahtuvat demoympäristössä, joka on esillä ja johon kurssin opettajasi antaa pääsyn.


Jos seuraat tätä kurssia itse, löydät luettelon kolmannen osapuolen isännistä demotarkoituksiin osoitteesta https://directory.btcpayserver.org/filter/hosts. Emme suosittele käyttämään näitä kolmannen osapuolen vaihtoehtoja tuotantoympäristöinä, mutta ne palvelevat kuitenkin tarkoituksenmukaisesti Bitcoin:n ja BTCPay Serverin käytön esittelyä.


BTCPay Server rockstar -harjoittelijana sinulla saattaa olla aiempaa kokemusta Bitcoin-solmun perustamisesta. Tämä kurssi on räätälöity erityisesti BTCPay Server -ohjelmistopinoa varten.


Monet BTCPay Serverin vaihtoehdoista ovat olemassa muodossa tai toisessa muissa Bitcoin Wallet-ohjelmistoissa.


### BTCPay-palvelimen kirjautumisnäyttö


Kun sinut toivotetaan tervetulleeksi demoympäristöön, sinua pyydetään kirjautumaan tai luomaan tili Palvelimen ylläpitäjät voivat poistaa uusien tilien luomisen käytöstä turvallisuussyistä. BTCPay Serverin logoja ja painikkeiden värejä voidaan muuttaa, koska BTCPay Server on avoimen lähdekoodin ohjelmisto. Kolmannen osapuolen isäntä voi tehdä ohjelmistolle White label -merkinnän ja muuttaa koko ulkoasua.


![image](assets/en/001.webp)


### Luo tili -ikkuna


Tilien luominen BTCPay-palvelimella edellyttää kelvollisia Address-sähköposti-merkkijonoja; example@email.com olisi kelvollinen merkkijono sähköpostille.


Salasanan on oltava vähintään 8 merkkiä pitkä, mukaan lukien kirjaimet, numerot ja merkit. Kun olet asettanut salasanan kerran, sinun on tarkistettava, että salasana on sama kuin ensimmäiseen salasanakenttään kirjoitettu salasana.


Kun sekä sähköpostiosoite- että salasanakentät on täytetty oikein, napsauta Luo tili -painiketta. Tämä tallentaa sähköpostiosoitteen ja salasanan ohjaajan BTCPay-palvelimen instanssiin.


![image](assets/en/002.webp)


**!Huom!**


Jos seuraat tätä kurssia itsenäisesti, tilin luominen tapahtuu todennäköisesti kolmannen osapuolen isännöimällä palvelimella, joten korostamme jälleen kerran, että näitä ei pidä käyttää tuotantoympäristöinä vaan ainoastaan koulutustarkoituksiin.


### Tilin luominen BTCPay-palvelimen ylläpitäjän toimesta


BTCPay-palvelininstanssin järjestelmänvalvoja voi myös luoda tilejä BTCPay-palvelimelle. BTCPay-palvelimen järjestelmänvalvoja voi napsauttaa "Palvelimen asetukset" (1), napsauttaa "Käyttäjät"-välilehteä (2) ja napsauttaa "+ Lisää käyttäjä" -painiketta (3) Käyttäjät-välilehden oikeassa yläkulmassa. Tavoitteessa (4.3) opit lisää tilien ylläpitäjän hallinnasta.


![image](assets/en/003.webp)


Järjestelmänvalvojana tarvitset käyttäjän sähköpostiosoitteen Address ja asetat vakiosalasanan. On suositeltavaa, että järjestelmänvalvoja ilmoittaa käyttäjälle, että hänen on vaihdettava tämä salasana ennen tilin käyttöä turvallisuussyistä. Jos järjestelmänvalvoja ei aseta salasanaa ja palvelimelle on määritetty SMTP, käyttäjä saa sähköpostiviestin, jossa on kutsulinkki tilin luomiseen ja salasanan asettamiseen itse.


### Esimerkki


Kun seuraat kurssia opettajan kanssa, seuraa opettajan antamaa linkkiä ja luo tilisi demoympäristöön. Varmista, että sähköpostiosoitteesi Address ja salasanasi on tallennettu turvallisesti; tarvitset näitä kirjautumistietoja kurssin lopuissa demotavoitteissa.


Kouluttajasi on saattanut kerätä Address-sähköpostin etukäteen ja lähettää kutsulinkin ennen tätä harjoitusta. Tarkista sähköpostiosoitteesi, jos sinua on ohjeistettu.


Kun osallistut kurssille ilman ohjaajaa, luo tilisi BTCPay Server -demoympäristön avulla; siirry osoitteeseen


https://Mainnet.demo.btcpayserver.org/login.


Tätä tiliä tulisi käyttää vain esittely- ja koulutustarkoituksiin eikä koskaan liiketoimintaan.


### Taitojen yhteenveto


Tässä jaksossa opit seuraavat asiat:



- Kuinka luoda tili isännöidylle palvelimelle Interface:n kautta.
- Miten palvelimen ylläpitäjä voi lisätä käyttäjiä manuaalisesti palvelimen asetuksissa.


### Tietojen arviointi


#### KA Käsitteellinen tarkastelu


Anna syitä siihen, miksi demopalvelimen käyttö tuotantotarkoituksiin on huono ajatus.


## Käyttäjätilien hallinta


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### Tilinhallinta BTCPay-palvelimella


Kun myymälän omistaja on luonut tilinsä, hän voi hallita sitä BTCPay-palvelimen käyttöliittymän vasemmassa alareunassa. Tili-painikkeen alapuolella on useita korkeamman tason asetuksia.



- Tumma/valo-tila.
- Piilota arkaluonteiset tiedot -vaihtoehto.
- Hallitse tiliä.


![image](assets/en/004.webp)


### Tumma ja vaalea tila


BTCPay Serverin käyttäjät voivat valita käyttöliittymän vaalean tai tumman tilan version. Asiakaskohtaiset sivut eivät muutu. Ne käyttävät asiakkaan suosimia asetuksia tumman tai vaalean tilan osalta.


### Piilota arkaluonteiset tiedot Toggle


Piilota arkaluonteiset tiedot -painike tarjoaa nopean ja yksinkertaisen Layer-suojauksen. Aina kun sinun on käytettävä BTCPay Serveriäsi, mutta ihmiset saattavat väijyä olkapääsi yli julkisessa tilassa, kytke Hide Sensitive Info päälle, ja kaikki BTCPay Serverin arvot ovat piilossa. Joku voi ehkä katsoa olkapääsi yli, mutta ei voi enää nähdä arvoja, joita käsittelet.


### Hallitse tiliä


Kun käyttäjätili on luotu, tässä voit hallita salasanoja, 2FA:ta tai API-avaimia.


### Tilin hallinta - Tili


Voit päivittää tilisi eri sähköpostiosoitteella Address. Varmistaaksesi, että sähköpostiosoitteesi Address on oikea, BTCPay Server antaa sinun lähettää vahvistussähköpostin. Napsauta Tallenna, jos käyttäjä asettaa uuden sähköpostiosoitteen Address ja vahvistaa, että vahvistus toimi. Käyttäjätunnus pysyy samana kuin edellisessä sähköpostissa.


Käyttäjä voi päättää poistaa koko tilinsä. Tämä voidaan tehdä napsauttamalla Tili-välilehden Poista-painiketta.


![image](assets/en/005.webp)


**!Huom!**


Sähköpostin vaihtamisen jälkeen tilin käyttäjänimi ei muutu. Aiemmin annettu sähköpostiosoite Address pysyy kirjautumisnimenä.


### Tilin hallinta - Salasana


Opiskelija voi haluta vaihtaa salasanansa. Hän voi tehdä sen menemällä Salasana-välilehdelle. Täällä hänen on kirjoitettava vanha salasanansa ja vaihdettava se uuteen.


![image](assets/en/006.webp)


### Kaksitekijätodennus (2fa)


Voit rajoittaa varastetun salasanan seurauksia käyttämällä kaksitekijätodennusta (2FA), joka on suhteellisen uusi tietoturvamenetelmä. Voit aktivoida kaksitekijätodennuksen Hallitse tiliä ja Kaksitekijätodennus-välilehden kautta. Sinun on suoritettava toinen vaihe kirjauduttuasi sisään käyttäjätunnuksella ja salasanalla.


BTCPay Server tukee kahta menetelmää 2FA:n käyttöönottoon: sovelluspohjainen 2FA (Authy, Google, Microsoft Authenticators) tai turvalaitteiden kautta (FIDO2 tai LNURL Auth).


### Kaksitekijätodennus - sovelluspohjainen


Matkapuhelimen käyttöjärjestelmän (Android tai iOS) mukaan käyttäjät voivat valita seuraavista sovelluksista;


1. Lataa kahden tekijän todennusohjelma.


   - Authy for [Android](https://play.google.com/store/apps/details?id=com.authy.authy) tai [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator for [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) tai [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator for [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) tai [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)

2. Kun olet ladannut ja asentanut Authenticator-sovelluksen.


   - Skannaa BTCPay-palvelimen tarjoama QR-koodi
   - Tai syötä BTCPay-palvelimen luoma avain manuaalisesti Authenticator-sovellukseesi.

3. Authenticator-sovellus antaa sinulle yksilöllisen koodin. Kirjoita yksilöllinen koodi BTCPay Serveriin vahvistaaksesi asetukset ja napsauta vahvista saadaksesi prosessin päätökseen.


![image](assets/en/007.webp)


### Taitojen yhteenveto


Tässä jaksossa opit seuraavat asiat:



- Tilinhallintavaihtoehdot ja eri tavat hallita tiliä BTCPay Server -instanssissa.
- Sovelluspohjaisen 2FA:n määrittäminen.


### Tietojen arviointi


#### KA Käsitteellinen tarkastelu


Kuvaile, miten sovelluspohjainen 2FA auttaa turvaamaan tilisi.


## Uuden myymälän luominen


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Luo ohjattu myymälä


Kun uusi käyttäjä kirjautuu BTCPay-palvelimeen, ympäristö on tyhjä ja tarvitsee ensimmäisen tallennuksen. BTCPay Serverin ohjatun käyttöönoton yhteydessä käyttäjälle annetaan mahdollisuus "Luo myymälä" (1). Storea voidaan pitää Bitcoin-tarpeiden kotina. Uusi BTCPay Server Node aloittaa synkronoimalla Bitcoin Blockchain:n (2). Riippuen siitä, millaisessa infrastruktuurissa käytät BTCPay Serveriä, tämä voi kestää muutamasta tunnista muutamaan päivään. Instanssin nykyinen versio näkyy BTCPay Server -käyttöliittymän oikeassa alakulmassa. Tämä on hyödyllinen viite vianmäärityksessä.


![image](assets/en/008.webp)


### Luo ohjattu myymälä


Tämän kurssin seuraaminen alkaa hieman erilaisella näytöllä kuin edellisellä sivulla. Koska ohjaajasi on valmistellut demoympäristön, Bitcoin Blockchain on synkronoitu aiemmin, ja siksi et näe solmujen synkronointitilaa.


Käyttäjä voi päättää poistaa koko tilinsä. Tämä voidaan tehdä napsauttamalla Tili-välilehden Poista-painiketta.


![image](assets/en/009.webp)


**!Huom!**


BTCPay Server -tileillä voi luoda rajattoman määrän kauppoja. Jokainen myymälä on Wallet tai "koti".


### Esimerkki


Aloita klikkaamalla "Luo myymälä".


![image](assets/en/010.webp)


Tämä luo ensimmäisen kotisi ja kojelautasi BTCPay Serverin käyttöä varten.


(1) Kun olet napsauttanut "Luo myymälä", BTCPay Server pyytää sinua nimeämään myymälän; tämä voi olla mikä tahansa sinulle hyödyllinen nimi.


![image](assets/en/011.webp)


(2) Seuraavaksi on asetettava oletusarvoinen myymälävaluutta, joko fiat-valuutta tai Bitcoin- tai Sats-valuutta. Demoympäristöä varten asetamme sen arvoksi USD.


![image](assets/en/012.webp)


(3) Viimeisenä parametrina myymälän asetuksissa BTCPay Server edellyttää, että asetat "Preferred price source" (Suositeltava hintalähde), jotta voit verrata Bitcoin:n hintaa nykyiseen fiat-hintaan, jotta myymälässäsi näkyy oikea Exchange-kurssi Bitcoin:n ja myymälän asettaman fiat-valuutan välillä. Me pysymme demoesimerkissä oletusarvossa ja asetamme tämän Krakenin Exchange:ksi. BTCPay Server käyttää Krakenin API:ta Exchange-kurssien tarkistamiseen.


![image](assets/en/013.webp)


(4) Nyt kun nämä myymälän parametrit on asetettu, napsauta Luo-painiketta, jolloin BTCPay Server luo ensimmäisen myymälän kojelaudan, jossa ohjattu toiminto jatkuu.


![image](assets/en/014.webp)


Onneksi olkoon, olet luonut ensimmäisen kauppasi, ja tämä päättää tämän harjoituksen.


![image](assets/en/015.webp)


### Taitojen yhteenveto


Tässä jaksossa opit:



- Kaupan luominen ja oletusvaluutan määrittäminen yhdistettynä hintalähdeasetuksiin.
- Jokainen "Store" on uusi koti, joka on erotettu muista BTCPay Serverin asennuksen myymälöistä.


# Johdanto Bitcoin-avaimien suojaamiseen


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Bitcoin-avainten tuottamisen ymmärtäminen


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### Mitä Bitcoin-avainten tuottamiseen liittyy?


Bitcoin-lompakot luovat luodessaan niin sanotun "seed:n". Viimeisessä tavoitteessa luot "seed", Ennen luotu sanasarja tunnetaan myös nimellä Mnemonic-lauseet. seed:tä käytetään yksittäisten Bitcoin-avainten tuottamiseen ja sitä käytetään Bitcoin:n lähettämiseen tai vastaanottamiseen. seed-lauseita ei saa koskaan jakaa kolmansille osapuolille tai epäluotettaville vertaisille.


seed:n sukupolvi tuotetaan teollisuusstandardin mukaisesti, joka tunnetaan nimellä "hierarkkinen deterministinen" (HD) kehys.


![image](assets/en/016.webp)


### Osoitteet


BTCPay-palvelin on rakennettu generate:lle ja uudelle Address:lle. Tämä helpottaa julkisen avaimen tai Address:n uudelleenkäytön ongelmaa. Saman julkisen avaimen käyttäminen tekee koko maksuhistoriasi seuraamisesta erittäin helppoa. Avainten ajatteleminen kertakäyttöisinä tositteina parantaisi yksityisyyttäsi huomattavasti. Käytämme myös Bitcoin-osoitteita, mutta älä sekoita niitä julkisiin avaimiin.


Address johdetaan julkisesta avaimesta "hashausalgoritmin" avulla Useimmat lompakot ja transaktiot näyttävät kuitenkin Osoitteet eikä näitä julkisia avaimia. Osoitteet ovat yleensä lyhyempiä kuin julkiset avaimet, ja ne alkavat yleensä kirjaimilla `1`, `3` tai `bc1`, kun taas julkiset avaimet alkavat kirjaimilla `02`, `03` tai `04`.



- Osoitteet, jotka alkavat `1.....`, ovat edelleen hyvin yleisiä osoitteita. Kuten luvussa "Uuden kaupan luominen" mainittiin, nämä ovat vanhoja osoitteita. Tämä Address-tyyppi on tarkoitettu P2PKH-tapahtumiin. P2Pkh käyttää Base58-koodausta, mikä tekee Address:stä suur- ja pienaakkoset huomioivan. Sen rakenne perustuu julkiseen avaimeen, jossa on lisänumero tunnisteena.



- Osoitteet, jotka alkavat sanoilla `bc1...`, ovat hitaasti siirtymässä hyvin yleisiin osoitteisiin. Näitä kutsutaan (natiiveiksi) SegWit-osoitteiksi. Nämä tarjoavat paremman maksurakenteen kuin muut mainitut osoitteet. Natiivit SegWit-osoitteet käyttävät Bech32-koodausta ja sallivat vain pienet kirjaimet.



- Osoitteet, jotka alkavat kirjaimella `3...`, ovat edelleen yleisesti käytössä pörsseissä talletusosoitteina. Nämä osoitteet mainitaan luvussa "Uuden myymälän luominen", käärityt tai sisäkkäiset SegWit-osoitteet. Ne voivat kuitenkin toimia myös "Multisig Address" -osoitteina. SegWit Address -osoitteena käytettynä saadaan jonkin verran säästöjä transaktiomaksuissa, mutta vähemmän kuin natiivissa SegWit:ssä. P2SH-osoitteissa käytetään Base58-koodausta. Tämä tekee siitä tapauskohtaisesti herkän, kuten vanhasta Address:stä.



- Osoitteet, jotka alkavat kirjaimella `2...`, ovat Testnet-osoitteita. Ne on tarkoitettu vastaanottamaan Testnet Bitcoin (tBTC). Älä koskaan sekoita tätä ja lähetä Bitcoin:a näihin osoitteisiin. Kehitystarkoituksiin voit käyttää generate Testnet Wallet. Verkossa on useita hanoja Testnet Bitcoin:n saamiseksi. Älä koskaan osta Testnet Bitcoin. Testnet Bitcoin on louhittu. Tämä saattaa olla kehittäjälle syy käyttää sen sijaan Regtestiä. Tämä on kehittäjille tarkoitettu leikkiympäristö, josta puuttuvat tietyt verkkokomponentit. Bitcoin on kuitenkin erittäin hyödyllinen kehitystarkoituksiin.


### Julkiset avaimet


Julkisia avaimia käytetään nykyään käytännössä harvemmin. Bitcoin-käyttäjät ovat ajan myötä korvanneet ne osoitteilla. Niitä on kuitenkin edelleen olemassa, ja niitä käytetään edelleen satunnaisesti. Julkiset avaimet ovat yleensä paljon pidempiä merkkijonoja kuin osoitteet. Kuten osoitteetkin, ne alkavat tietyllä tunnisteella.



- Ensinnäkin `02...` ja `03...` ovat hyvin vakiomuotoisia SEC-muotoon koodattuja julkisen avaimen tunnuksia. Niitä voidaan käsitellä ja muuttaa vastaanotto-osoitteiksi, käyttää multi-sig-osoitteiden luomiseen tai allekirjoituksen tarkistamiseen. Varhaisvaiheen Bitcoin-tapahtumissa käytettiin julkisia avaimia osana P2PK-tapahtumia.



- HD-lompakoissa käytetään kuitenkin erilaista rakennetta. `xpub...`, `ypub...` tai `zpub...` kutsutaan laajennetuiksi julkisiksi avaimiksi eli xpubs. Näitä avaimia käytetään monien julkisten avainten johtamiseen osana HD Wallet:ää. Koska xpub-avaimesi sisältää koko historiasi eli aiemmat ja tulevat tapahtumat, älä koskaan jaa niitä epäluotettaville osapuolille.


### Taitojen yhteenveto


Tässä jaksossa opit seuraavat asiat:



- Osoitteiden ja julkisten avainten tietotyyppien väliset erot ja edut, joita osoitteiden käyttäminen julkisiin avaimiin verrattuna tuo mukanaan.


### Tietojen arviointi


Kuvaile, mitä hyötyä uusien osoitteiden käyttämisestä kussakin tapahtumassa on Address:n uudelleenkäyttöön tai julkisen avaimen menetelmiin verrattuna.


## Avainten varmistaminen Hardware Wallet:lla


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Bitcoin-avainten tallentaminen


seed-lauseen luomisen jälkeen tässä kirjassa luotu 12-24 sanan luettelo vaatii asianmukaisia varmuuskopioita ja suojausta, sillä nämä sanat ovat ainoa tapa palauttaa pääsy Wallet:ään. HD-lompakoiden rakenne ja se, miten se luo osoitteet deterministisesti käyttämällä yhtä seed:tä, tarkoittaa, että kaikki luodut osoitteet varmuuskopioidaan käyttämällä tätä yhtä Mnemonic-sanojen luetteloa, joka edustaa seed- tai palautuslausetta.


Pidä palautuslauseesi turvassa. Jos joku pääsee siihen käsiksi, erityisesti pahantahtoisesti, hän voi siirtää varojasi. Pidä seed turvassa, mutta muista samalla, että se on keskinäinen. Bitcoin:n yksityisten avainten säilyttämiseen on useita menetelmiä, joilla kullakin on omat etunsa ja haittansa turvallisuuden, yksityisyyden, mukavuuden ja fyysisen säilytyksen kannalta. Yksityisten avainten tärkeyden vuoksi Bitcoin-käyttäjät pyrkivät yleensä säilyttämään ja pitämään avaimet turvallisesti "omassa säilytyksessä" sen sijaan, että he käyttäisivät pankkien kaltaisia "säilytyspalveluja". Käyttäjästä riippuen heidän on käytettävä joko Cold-tallennusratkaisua tai Hot Wallet:ta.


### Hot ja Cold Bitcoin-avainten varastointi


Yleensä Bitcoin-lompakoissa on Hot Wallet tai Cold Wallet. Useimmat kompromissit liittyvät mukavuuteen, helppokäyttöisyyteen ja turvallisuusriskeihin. Kukin näistä menetelmistä voidaan nähdä myös säilytysratkaisussa. Kompromissit ovat kuitenkin enimmäkseen tietoturvaan ja yksityisyyteen perustuvia, ja ne eivät kuulu tämän kurssin aihepiiriin.


### Hot Wallet


Hot-lompakot ovat kätevin tapa olla vuorovaikutuksessa Bitcoin:n kanssa mobiili-, verkko- tai työpöytäohjelmiston kautta. Wallet on aina yhteydessä internetiin, jolloin käyttäjät voivat lähettää tai vastaanottaa Bitcoin:ta. Tämä on kuitenkin myös sen heikkous; koska Wallet on aina verkossa, se on nyt alttiimpi hakkereiden hyökkäyksille tai laitteessa oleville haittaohjelmille. BTCPay Serverissä Hot-lompakot tallentavat yksityiset avaimet instanssiin. Kuka tahansa, joka pääsee käsiksi BTCPay Server -varastoosi, voi mahdollisesti varastaa varoja tästä Address:stä, jos hän on pahansuopa. Kun BTCPay Server toimii isännöidyssä ympäristössä, sinun tulisi aina ottaa tämä huomioon turvallisuusprofiilissasi ja mieluiten olla käyttämättä Hot Wallet:ää tällaisessa tapauksessa. Kun BTCPay Server on asennettu omistamaasi ja suojaamaasi laitteistoon, riskiprofiili pienenee huomattavasti, mutta se ei koskaan katoa kokonaan.


### Cold Wallet


Yksityishenkilöt siirtävät Bitcoin:nsä Cold:een Wallet:een, koska se voi eristää yksityiset avaimet internetistä ja suojata niitä siten mahdollisilta verkkouhilta. Internet-yhteyden poistaminen yhtälöstä vähentää haittaohjelmien, vakoiluohjelmien ja SIM-korttien vaihtamisen riskiä. Cold-tallennuksen uskotaan olevan turvallisuudeltaan ja riippumattomuudeltaan parempi kuin Hot-tallennuksen, kunhan Bitcoin:n yksityisten avainten katoamisen estämiseksi on toteutettu riittävät varotoimet. Cold-tallennus soveltuu parhaiten suurille Bitcoin-määrille, joita ei ole tarkoitus käyttää usein Wallet-asetusten monimutkaisuuden vuoksi.


Bitcoin-avainten tallentamiseen Cold-varastoon on olemassa erilaisia menetelmiä paperilompakoista aivolompakoihin, laitteistolompakoihin tai alusta alkaen Wallet-tiedostoon. Useimmat lompakot käyttävät BIP 39 generate seed-lauseen BIP 39. Bitcoin core-ohjelmiston sisällä ei kuitenkaan ole vielä päästy yksimielisyyteen sen käytöstä. Bitcoin core-ohjelmisto käyttää edelleen generate Wallet.dat-tiedostoa, joka on tallennettava turvalliseen offline-sijaintiin.


### Taitojen yhteenveto


Tässä jaksossa opit:



- Hot- ja Cold-lompakoiden toiminnallisuuden erot ja niiden väliset kompromissit.


### Osaamisen arviointi Käsitteellinen tarkastelu



- Mikä on Wallet?



- Mitä eroa on Hot- ja Cold-lompakoiden välillä?



- Mitä tarkoitetaan "Wallet:n tuottamisella"?


## Bitcoin-näppäinten käyttäminen


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### BTCPay-palvelin Wallet


BTCPay Server sisältää seuraavat Wallet:n vakio-ominaisuudet:



- Tapahtumat
- Lähetä
- Vastaanota
- Tarkista
- Vedä maksut
- Maksut
- PSBT
- Yleiset asetukset


### Tapahtumat


Järjestelmänvalvojat näkevät tapahtumanäkymässä kyseiseen varastoon liitettyjen On-Chain Wallet:n saapuvat ja lähtevät tapahtumat. Jokaisessa tapahtumassa on eroteltu vastaanotetut ja lähetetyt summat. Vastaanotetut tapahtumat ovat Green, ja lähtevät tapahtumat ovat punaisia. BTCPay-palvelimen tapahtumanäkymässä ylläpitäjät näkevät myös joukon vakiotarroja.


| Transaction Type | Description                                          |
| ---------------- | ---------------------------------------------------- |
| App              | Payment was received through an app-created invoice  |
| invoice          | Payment was received through an invoice              |
| payjoin          | Not paid, invoice timer still has not expired        |
| payjoin-exposed  | UTXO was exposed through an invoice payjoin proposal |
| payment-request  | Payment was received through a payment request       |
| payout           | Payment was sent through a payout or refund          |

### Kuinka lähettää


BTCPay-palvelimen lähetystoiminto lähettää tapahtumia BTCPay-palvelimeltasi On-Chain Wallet. BTCPay-palvelin mahdollistaa useita tapoja allekirjoittaa tapahtumat varojen käyttämiseksi. Transaktio voidaan allekirjoittaa seuraavilla tavoilla;



- Hardware Wallet
- Lompakot, jotka tukevat PSBT
- HD:n yksityinen avain tai palautussiemenet.
- Hot Wallet


#### Hardware Wallet


BTCPay Serverissä on sisäänrakennettu Hardware Wallet-tuki, jonka avulla voit käyttää Hardware Wallet:ta BTCPay Vaultin kanssa vuotamatta tietoja kolmannen osapuolen sovelluksiin tai palvelimiin. BTCPay Serverin Hardware Wallet-integraatio mahdollistaa Hardware Wallet:n tuonnin ja saapuvien varojen käyttämisen yksinkertaisella vahvistuksella laitteellasi. Yksityiset avaimesi eivät koskaan poistu laitteesta, ja kaikki varat varmennetaan Full node:lla, mikä varmistaa, ettei tietoja vuoda.


#### Allekirjoittaminen Wallet:ää tukevan PSBT:n kanssa


PSBT (Osittain allekirjoitetut Bitcoin-tapahtumat) on vaihtomuoto Bitcoin-tapahtumille, jotka on vielä allekirjoitettava kokonaan. PSBT on tuettu BTCPay Serverissä, ja se voidaan allekirjoittaa yhteensopivilla laitteisto- ja ohjelmistolompakoilla.


Täysin allekirjoitetun Bitcoin-tapahtuman rakentaminen tapahtuu seuraavien vaiheiden kautta:



- PSBT rakennetaan, ja siinä on tietyt tulot ja lähdöt, mutta ei allekirjoituksia
- Viety PSBT voidaan tuoda Wallet:llä, joka tukee tätä muotoa
- Tapahtumatiedot voidaan tarkastaa ja allekirjoittaa Wallet:n avulla
- Allekirjoitettu PSBT-tiedosto viedään Wallet:sta ja tuodaan BTCPay-palvelimelle
- BTCPay-palvelin tuottaa lopullisen Bitcoin-tapahtuman
- Tarkistat tuloksen ja lähetät sen verkkoon


#### Allekirjoittaminen HD Private Key -avaimella tai Mnemonic seed:llä


Jos olet luonut Wallet:n ennen BTCPay-palvelimen käyttöä, voit käyttää varat syöttämällä yksityisen avaimesi asianmukaiseen kenttään. Aseta asianmukainen "AccountKeyPath" kohdassa Wallet> Asetukset, muuten et voi käyttää.


#### Allekirjoittaminen Hot Wallet:n kanssa


Jos olet luonut uuden Wallet:n myymälääsi perustettaessa ja ottanut sen käyttöön Hot Wallet:nä, se käyttää automaattisesti palvelimelle tallennettua seed:ta allekirjoittamiseen.


### RBF (Replace-by-fee)


Replace-by-fee (RBF) on Bitcoin-protokollan ominaisuus, jonka avulla voit korvata aiemmin lähetetyn tapahtuman (kun se on vielä vahvistamaton). Tämä mahdollistaa Wallet:n tapahtuman sormenjäljen satunnaistamisen tai sen korvaamisen korkeammalla maksuprosentilla, jotta tapahtuma siirtyy korkeammalle vahvistusjonossa (Mining) prioriteettiasemassa. Tämä korvaa tehokkaasti alkuperäisen tapahtuman, koska korkeampi maksuprosentti asetetaan etusijalle, ja kun se on vahvistettu, se mitätöi alkuperäisen tapahtuman (ei kaksinkertaista kulutusta).


Paina "Lisäasetukset"-painiketta nähdäksesi RBF-vaihtoehdot.


![image](assets/en/017.webp)



- Randomize for higher privacy (Satunnaistaminen yksityisyyden suojaamiseksi) mahdollistaa tapahtuman korvaamisen automaattisesti tapahtuman sormenjäljen satunnaistamiseksi.
- Kyllä, merkitse tapahtuma RBF:lle ja korvaa se nimenomaisesti (ei korvata oletusarvoisesti, vain syötteen perusteella)
- Ei, älä salli tapahtuman korvaamista.


### Coin Valinta


Coin-valinta on kehittynyt yksityisyyden suojaa parantava ominaisuus, jonka avulla voit valita kolikot, jotka haluat käyttää, kun teet maksutapahtuman. Esimerkiksi maksaminen kolikoilla, jotka ovat tuoreita conjoin mixistä.


Coin-valinta toimii luonnostaan Wallet-tarratoiminnon kanssa. Näin voit merkitä saapuvat varat, mikä helpottaa UTXO:n hallintaa ja käyttöä.


BTCPay Server tukee BIP-329:ää etikettien hallintaa varten. Jos siirrät Wallet:stä, joka tukee BIP-329:ää, ja sinulla on määritetyt tarrat, BTCPay Server tunnistaa ja tuo ne automaattisesti. Kun palvelimia siirretään, nämä tiedot voidaan myös viedä ja tuoda uuteen ympäristöön.


### Miten vastaanottaa


Kun napsautat vastaanottopainiketta BTCPay Serverissä, se luo käyttämättömän Address:n, jota voidaan käyttää maksujen vastaanottamiseen. Järjestelmänvalvojat voivat myös luoda uuden Address:n luomalla uuden "Invoice:n"


BTCPay-palvelin pyytää sinua aina generate seuraavaan käytettävissä olevaan Address:ään Address:n uudelleenkäytön estämiseksi. Kun olet napsauttanut "generate seuraava käytettävissä oleva BTC Address", BTCPay Server luo uuden Address:n ja QR:n. Sen avulla voit myös asettaa suoraan tarran Address:ään, jotta voit hallita osoitteitasi paremmin.


![image](assets/en/018.webp)


![image](assets/en/019.webp)


#### Skannaa uudelleen


Rescan-ominaisuus perustuu Bitcoin core 0.17.0:n "Scantxoutset"-ominaisuuteen, jolla Blockchain:n (nimeltään UTXO Set) nykyinen tila skannataan konfiguroituun johdannaisjärjestelmään kuuluvien kolikoiden varalta. Wallet:n uudelleentarkistus ratkaisee kaksi yleistä ongelmaa, joita BTCPay Serverin käyttäjät usein kohtaavat.


1. Aukkorajoitusongelma - Useimmat kolmannen osapuolen lompakot ovat kevyitä lompakoita, jotka jakavat solmun monien käyttäjien kesken. Kevyet ja Full node:een tukeutuvat lompakot rajoittavat niiden osoitteiden määrää (yleensä 20), joilla ei ole saldoa, joita ne seuraavat Blockchain:ssä suorituskykyongelmien välttämiseksi. BTCPay Server luo uuden Address:n jokaista Invoice:ta varten. Edellä esitetyn perusteella BTCPay Server tuottaa 20 peräkkäistä maksamatonta laskua, minkä jälkeen ulkoinen Wallet lopettaa tapahtumien noutamisen olettaen, että uusia tapahtumia ei ole tapahtunut. Ulkoinen Wallet ei näytä niitä, kun laskut on maksettu 21., 22. jne. päivänä. Toisaalta sisäisesti BTCPay-palvelimen Wallet seuraa kaikkia tuottamiaan Address-laskuja sekä huomattavasti korkeampaa välirajaa. Se ei ole riippuvainen kolmannesta osapuolesta ja voi aina näyttää oikean saldon.

2. Aukkorajaratkaisu - Jos [ulkoinen/olemassa oleva Wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) sallii aukkorajakonfiguraation, helppo ratkaisu on lisätä sitä. Suurin osa lompakoista ei kuitenkaan salli tätä. Ainoat lompakot, jotka tietojemme mukaan tukevat tällä hetkellä gap limit -asetuksia, ovat Electrum, Wasabi ja Sparrow wallet. Valitettavasti kohtaat todennäköisesti ongelman monien muiden lompakoiden kanssa. Parhaan käyttökokemuksen ja yksityisyyden takaamiseksi kannattaa harkita BTCPay-palvelimen sisäisen Wallet:n käyttöä ulkoisten lompakoiden sijaan.


#### BTCPay-palvelin käyttää "mempoolfullrbf=1"


BTCPay Server käyttää "mempoolfullrbf=1"; olemme lisänneet tämän oletusarvoksi BTCPay Server -asetuksiin. Olemme kuitenkin tehneet siitä myös ominaisuuden, jonka voit itse poistaa käytöstä. Ilman "mempoolfullrbf=1", jos asiakas käyttää maksun tuplasti tapahtumalla, joka ei ole RBF-merkki, kauppias saisi tietää siitä vasta vahvistuksen jälkeen.


Järjestelmänvalvoja voi halutessaan poistaa tämän asetuksen käytöstä. Seuraavalla merkkijonolla voit muuttaa oletusasetusta.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i
```


### BTCPay-palvelimen Wallet asetukset


Wallet-asetukset BTCPay Serverissä tarjoavat selkeän ja tiiviin yleiskatsauksen Wallet:n yleisistä asetuksista. Kaikki nämä asetukset on täytetty valmiiksi, jos Wallet on luotu BTCPay Serverillä.


![image](assets/en/020.webp)


Wallet-asetukset BTCPay Serverissä tarjoavat selkeän ja tiiviin yleiskatsauksen Wallet:n yleisistä asetuksista. Kaikki nämä asetukset on täytetty valmiiksi, jos Wallet on luotu BTCPay Serverillä. BTCPay Serverin Wallet-asetukset alkavat Wallet:n tilasta. Onko se vain Watch-only- vai Hot Wallet? Wallet-tyypistä riippuen toimet voivat vaihdella, mukaan lukien Wallet:n tarkistaminen uudelleen puuttuvien tapahtumien varalta, vanhojen tapahtumien karsiminen historiasta, Wallet:n rekisteröinti maksulinkkejä varten tai nykyisen kauppaan liitetyn Wallet:n korvaaminen ja poistaminen. BTCPay Serverin Wallet-asetuksissa ylläpitäjät voivat asettaa Wallet:lle tunnisteen Wallet:n hallinnan parantamiseksi. Täällä ylläpitäjä näkee myös Derivation Scheme (johdantojärjestelmä), tiliavaimen (xpub), Fingerprint (sormenjälki) ja Keypath (avaintietopolku). Wallet:n asetuksissa on vain kaksi pääasiallista asetusta. Maksu on pätemätön, jos tapahtuma ei vahvistu (asetettujen minuuttien kuluessa) Invoice:n voimassaolon päättymisestä. Invoice katsotaan vahvistetuksi, kun maksutapahtumalla on X määrä vahvistuksia. Järjestelmänvalvojat voivat myös asettaa vaihtokytkimen näyttämään suositellut maksut maksunäytössä tai asettaa manuaalisen vahvistustavoitteen lohkojen lukumäärälle.


![image](assets/en/021.webp)


**!Huom!**


Jos seuraat tätä kurssia itsenäisesti, tilin luominen tapahtuu todennäköisesti kolmannen osapuolen isännän kautta. Siksi suosittelemme jälleen kerran, että näitä ei käytetä tuotantoympäristöinä, vaan ainoastaan koulutustarkoituksiin.


### Esimerkki


#### Bitcoin Wallet:n perustaminen BTCPay-palvelimeen


BTCPay Server tarjoaa kaksi tapaa Wallet:n määrittämiseen. Yksi tapa on tuoda olemassa oleva Bitcoin Wallet. Tuonti voidaan tehdä liittämällä Hardware Wallet, tuomalla Wallet-tiedosto, syöttämällä laajennettu julkinen avain, skannaamalla Wallet:n QR-koodi tai, mikä on epäedullisinta, syöttämällä aiemmin luotu Wallet:n palautus seed käsin. BTCPay Serverissä on myös mahdollista luoda uusi Wallet. BTCPay Serverin konfigurointi on mahdollista tehdä kahdella tavalla uutta Wallet:ta luotaessa.


BTCPay Serverin Hot Wallet -vaihtoehto mahdollistaa PayJoin:n tai Liquid:n kaltaiset ominaisuudet. Siinä on kuitenkin haittapuoli: tätä Wallet:a varten luotu palautus seed tallennetaan palvelimelle, josta kuka tahansa, jolla on järjestelmänvalvojan oikeudet, voi hakea sen. Koska yksityinen avaimesi on johdettu palautus-seed:stä, pahantahtoinen toimija voi päästä käsiksi nykyisiin ja tuleviin varoihisi!


Tämän riskin pienentämiseksi BTCPay Server -palvelimessa järjestelmänvalvoja voi asettaa arvoksi kohdassa Palvelimen asetukset > Käytännöt > "Salli muiden kuin järjestelmänvalvojien luoda Hot-lompakoita myymälöihinsä" "ei", koska se on oletusarvo. Parantaakseen näiden Hot-lompakoiden turvallisuutta palvelimen ylläpitäjän tulisi ottaa käyttöön 2FA-todennus tileillä, joilla saa olla Hot-lompakoita. Yksityisten avainten tallentaminen julkiselle palvelimelle on vaarallinen käytäntö, ja siihen liittyy merkittäviä riskejä. Jotkin niistä ovat samankaltaisia kuin Lightning Network:n riskit (katso Lightning Network:n riskit seuraavassa luvussa).


Toinen vaihtoehto, jonka BTCPay Server tarjoaa uuden Wallet:n luomiseksi, on Watch-only wallet:n luominen. BTCPay Server luo generate yksityiset avaimesi kerran. Kun käyttäjä on vahvistanut kirjoittaneensa seed-lauseensa, BTCPay Server pyyhkii yksityiset avaimet palvelimelta. Tämän seurauksena myymälääsi on nyt liitetty Watch-only wallet. Jos haluat käyttää Watch-only wallet:lla saamasi varat, katso luku Miten lähetetään, joko käyttämällä BTCPay Server Vaultia, PSBT:ää (Partially Signed Bitcoin Transaction) tai, mikä on vähiten suositeltavaa, antamalla seed-lauseesi manuaalisesti.


Loit uuden "Kaupan" viimeisessä osassa. Ohjattu asennus jatkuu pyytämällä "Set up a Wallet" tai "Set up a Lightning node". Tässä esimerkissä noudatat ohjatun "Set up a Wallet" -prosessia (1).


![image](assets/en/022.webp)


Kun olet napsauttanut "Wallet:n perustaminen", ohjattu toiminto jatkaa kysymällä, miten haluat jatkaa; BTCPay Server tarjoaa nyt mahdollisuuden liittää olemassa olevan Bitcoin Wallet:n uuteen myymälääsi. Jos sinulla ei ole Wallet:a, BTCPay Server ehdottaa uuden Wallet:n luomista. Tässä esimerkissä noudatetaan ohjeita "luo uusi Wallet" (2). Seuraa vaiheita oppiaksesi, miten "Yhdistä olemassa oleva Wallet (1).


![image](assets/en/023.webp)


**!Huom!**


Jos suoritat tämän kurssin luokkahuoneessa, ota huomioon, että nykyinen esimerkki ja seed, jonka olemme luoneet, on tarkoitettu vain opetustarkoituksiin. Näissä osoitteissa ei pitäisi koskaan olla mitään muuta merkittävää määrää kuin mitä harjoituksissa vaaditaan.


(1) Jatka "Uusi Wallet" -ohjattua toimintoa napsauttamalla "Luo uusi Wallet" -painiketta.


![image](assets/en/024.webp)


(2) Kun olet napsauttanut "Create a new Wallet" (Luo uusi Wallet), ohjatun toiminnon seuraava ikkuna antaa vaihtoehdot "Hot Wallet" ja "Watch-only wallet" Jos seuraat ohjaajan kanssa, ympäristösi on jaettu Demo, ja voit luoda vain Watch-only wallet:n. Huomaa ero kahden alla olevan kuvan välillä. Kun olet demoympäristössä ja seuraat kouluttajan mukana, luo "Watch-only wallet" ja jatka ohjatulla "New Wallet" -ohjatulla toiminnolla.


![image](assets/en/025.webp)


![image](assets/en/026.webp)


(3) Jatka ohjatun uuden Wallet:n luomista, ja olet nyt Create BTC Watch-only wallet -osiossa. Tässä pääsee asettamaan Wallet:n "Address-tyypin" BTCPay Server antaa sinun valita haluamasi Address-tyypin; tätä kurssia kirjoitettaessa suositellaan edelleen bech32-osoitteiden käyttöä. Voit tutustua osoitteisiin tarkemmin tämän osan ensimmäisessä luvussa.



- SegWit (bech32)
  - Alkuperäiset SegWit-osoitteet alkavat kirjaimella `bc1q`.
  - Esimerkki: `bc1qXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- Legacy
  - Legacy-osoitteet ovat osoitteita, jotka alkavat numerolla `1`.
  - Esimerkki: `15e15hXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- Taproot (edistyneille käyttäjille)
  - Taproot-osoitteet alkavat kirjaimella "bc1p".
  - Esimerkki: `bc1pXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- SegWit kääritty
  - SegWit-koteloidut osoitteet alkavat numerolla "3".
  - Esimerkki: `37BBXXXXXXXXXXXXXXXXXXXXXXX`


Valitse SegWit (suositeltava) Wallet Address -tyypiksi.


![image](assets/en/027.webp)


(4) Kun asetat Wallet:n parametria, BTCPay-palvelin antaa käyttäjille mahdollisuuden asettaa valinnaisen passphrase:n BIP39:n kautta; varmista salasanasi.


![image](assets/en/028.webp)


(5) Kun olet asettanut Wallet:n Address-tyypin ja mahdollisesti joitakin lisäasetuksia, napsauta Luo, ja BTCPay Server generate uusi Wallet:si. Huomaa, että tämä on viimeinen vaihe ennen seed-lauseen luomista. Varmista, että teet tämän vain ympäristössä, jossa joku ei voi varastaa seed-lauseen katsomalla näyttöäsi.


![image](assets/en/029.webp)


(6) Ohjatun toiminnon seuraavassa näytössä BTCPay Server näyttää sinulle juuri luotua Wallet:aa koskevan Recovery seed -lausekkeen; nämä ovat avaimia Wallet:n palauttamiseen ja tapahtumien allekirjoittamiseen. BTCPay Server luo seed-lauseen, jossa on 12 sanaa. Nämä sanat poistetaan palvelimelta tämän asetusnäytön jälkeen. Tämä Wallet on nimenomaan Watch-only wallet. Tätä seed-lausetta ei suositella tallennettavaksi digitaalisesti tai valokuvana. Käyttäjät voivat edetä ohjatussa toiminnossa eteenpäin vain, jos he aktiivisesti vahvistavat kirjoittaneensa seed-lausekkeensa muistiin.


![image](assets/en/030.webp)


(7) Kun olet napsauttanut Done (Valmis) ja varmistanut äskettäin luodun Bitcoin seed-lauseen, BTCPay Server päivittää kauppasi liitetyn uuden Wallet:n ja on valmis vastaanottamaan maksuja. Huomaa, että Bitcoin on nyt korostettuna ja aktivoituna Wallet:n alla käyttäjän Interface vasemmanpuoleisessa navigointivalikossa.


![image](assets/en/031.webp)


### Esimerkki: seed-lauseen kirjoittaminen


Tämä on erityisen turvallinen hetki käyttää Bitcoin:tä. Kuten aiemmin mainittiin, vain sinulla pitäisi olla pääsy seed-lauseeseesi tai tieto siitä. Koska seuraat opettajan ja luokkahuoneen mukana, tuotettua seed:ta tulisi käyttää vain tällä kurssilla. Liian monet tekijät, kuten luokkatovereiden uteliaat katseet, turvattomat järjestelmät ja muut, tekevät näistä avaimista vain opetuksellisia ja epäluotettavia. Luodut avaimet olisi kuitenkin säilytettävä kurssin esimerkkejä varten.


Ensimmäinen menetelmä, jota käytämme tässä tilanteessa ja joka on myös vähiten turvallinen, on seed-lauseen kirjoittaminen oikeassa järjestyksessä. seed-lauseen kortti sisältyy opiskelijalle annettuun kurssimateriaaliin tai se löytyy BTCPay Server GitHubista. Käytämme tätä korttia edellisessä vaiheessa luotujen sanojen kirjoittamiseen. Varmista, että kirjoitat ne ylös oikeassa järjestyksessä. Kun olet kirjoittanut ne ylös, tarkista ne ohjelmiston antamien tietojen perusteella varmistaaksesi, että kirjoitit ne oikeassa järjestyksessä. Kun olet kirjoittanut ne ylös, napsauta valintaruutua, jossa ilmoitetaan, että olet kirjoittanut seed-lauseen oikein.


### Esimerkki: seed-lauseen tallentaminen Hardware Wallet:aan


Tällä kurssilla käsittelemme seed-lauseen tallentamista Hardware Wallet:een. Tämän kurssin seuraaminen ohjaajan kanssa saattaa joskus sisältää tällaisen laitteen. Kurssin oppaan materiaaleihin on koottu luettelo laitteistokukkaroista, jotka soveltuisivat tähän harjoitukseen.


Käytämme tässä esimerkissä BTCPay Server -holvia ja Blockstream Jade Hardware Wallet:ta.


Voit myös seurata Hardware Wallet:n liittämistä koskevaa videoopasta.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


Lataa BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases


Varmista, että lataat oikeat tiedostot järjestelmääsi varten. Windows-käyttäjien tulisi ladata [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe) paketti, Mac-käyttäjien tulisi ladata [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg) ja Linux-käyttäjien tulisi ladata [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)


Kun olet asentanut BTCPay Server Vaultin, käynnistä ohjelmisto napsauttamalla työpöydällä olevaa kuvaketta. Kun BTCPay Server Vault on asennettu oikein ja käynnistetty ensimmäisen kerran, se pyytää lupaa käyttää sitä verkkosovellusten kanssa. Se pyytää antamaan käyttöoikeuden tiettyyn BTCPay Server -palvelimeen, jonka kanssa työskentelet. Hyväksy nämä ehdot. BTCPay Server Vault etsii nyt laitteistolaitteen. Kun laite on löydetty, BTCPay Server tunnistaa, että Vault on käynnissä ja on hakenut laitteesi.


**!Huom!**


Älä anna SSH-avaimia tai palvelimen hallintatiliä muille kuin järjestelmänvalvojille, kun käytät Hot Wallet:ää. Kuka tahansa, jolla on pääsy näihin tileihin, pääsee käsiksi Hot Wallet:n varoihin.


### Taitojen yhteenveto


Tässä jaksossa opit seuraavat asiat:



- Bitcoin Wallet:n ja sen eri luokittelujen transaktionäkymä.
- Bitcoin Wallet:stä lähetettäessä on käytettävissä erilaisia vaihtoehtoja laitteistosta Hot-lompakkoihin.
- Useimpia lompakoita käytettäessä ilmenevä kuilurajoitusongelma ja sen korjaaminen.
- Miten generate uusi Bitcoin Wallet luodaan BTCPay Serverissä, mukaan lukien avainten tallentaminen Hardware Wallet:een ja palautuslauseen varmuuskopiointi.


Tässä tavoitteessa olet oppinut, miten generate uusi Bitcoin Wallet luodaan BTCPay Serverissä. Emme ole vielä käsitelleet, miten näitä avaimia suojataan tai käytetään. Tämän tavoitteen nopeassa yleiskatsauksessa olet oppinut, miten ensimmäinen myymälä perustetaan. Olet oppinut, miten generate Bitcoin Recovery seed -lausetta käytetään.


### Osaamisen arviointi Käytännön tarkastelu


Kuvaile menetelmä avainten tuottamiseksi ja niiden suojausjärjestelmä sekä suojausjärjestelmän kompromissit/riskit.


## BTCPay-palvelimen salama Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


Kun palvelimen ylläpitäjä perustaa uuden BTCPay Server -instanssin, hän voi määrittää Lightning Network-toteutuksen, kuten LND:n, Core Lightningin tai Eclairin; katso tarkemmat asennusohjeet kohdasta BTCPay Serverin konfigurointi.


Jos seuraat luokkahuoneessa, Lightning-solmun yhdistäminen BTCPay-palvelimeen toimii Custom-solmun kautta. Käyttäjä, joka ei ole BTCPay Serverin palvelimen ylläpitäjä, ei voi oletusarvoisesti käyttää sisäistä Lightning-solmua. Tämä on tehty palvelimen omistajan suojaamiseksi varojen menettämiseltä. Palvelimen ylläpitäjät voivat asentaa lisäosan, jolla he voivat myöntää pääsyn Lightning-solmuunsa LNBankin kautta; tämä ei kuulu tämän kirjan aihepiiriin. Lisätietoja LNBankista on virallisella lisäosasivulla.


### Yhdistä sisäinen solmu (palvelimen ylläpitäjä)


Palvelimen ylläpitäjä voi käyttää BTCPay Serverin sisäistä Lightning Nodea. Lightning-toteutuksesta riippumatta yhteyden muodostaminen sisäiseen Lightning-solmuun on sama.


Siirry edelliseen asennuskauppaan ja napsauta vasemmanpuoleisessa valikossa olevaa "Lightning" Wallet:a. BTCPay Server antaa kaksi asetusvaihtoehtoa: sisäisen solmun käyttö (oletusarvoisesti vain palvelimen ylläpitäjä) tai mukautetun solmun käyttö (ulkoinen yhteys). Palvelimen ylläpitäjät voivat napsauttaa "Käytä sisäistä solmua" -vaihtoehtoa. Muita asetuksia ei tarvita. Napsauta "tallenna"-painiketta ja huomaa ilmoitus, jossa lukee "BTC Lightning node updated". Kauppa on nyt saanut onnistuneesti Lightning Network-ominaisuudet.


### Yhdistä ulkoinen solmu (palvelimen käyttäjä/varaston omistaja)


Oletusarvoisesti myymälän omistajat eivät saa käyttää palvelimen ylläpitäjän Lightning Nodea. Yhteys on muodostettava ulkoiseen solmuun, joko solmuun, jonka myymälän omistaja omistaa ennen BTCPay-palvelimen perustamista, LNBank-lisäosaan, jos palvelimen ylläpitäjä on antanut sen käyttöön, tai säilytysratkaisuun, kuten Albyyn.


Siirry edelliseen asetuskauppaan ja napsauta vasemmanpuoleisessa valikossa lompakoiden alapuolella olevaa kohtaa "Salama". Koska myymälän omistajat eivät oletusarvoisesti saa käyttää sisäistä solmua, tämä vaihtoehto on harmaana. Mukautetun solmun käyttäminen on ainoa oletusarvoisesti kaupan omistajille tarjolla oleva vaihtoehto.


BTCPay-palvelin vaatii yhteystietoja; esivalmistettu (tai säilytysratkaisu) toimittaa nämä tiedot erityisesti Lightning-toteutukseen räätälöitynä. BTCPay Serverissä kaupan omistajat voivat käyttää seuraavia yhteyksiä;



- C-salama TCP- tai Unixdomainsocket-yhteyden kautta.
- Lightning Charge HTTPS:n kautta
- Eclair HTTPS:n kautta
- LND REST-välityspalvelimen kautta
- LNDhub REST API:n kautta


![image](assets/en/032.webp)


Napsauta "testaa yhteys" varmistaaksesi, että olet syöttänyt yhteystiedot oikein. Kun yhteys on vahvistettu hyväksi, napsauta "Tallenna", ja BTCPay-palvelin näyttää, että myymälä on päivitetty Lightning-solmulla.


### Sisäisen Lightning-solmun LND hallinta (palvelimen ylläpitäjä)


Sisäisen Lightning-solmun yhdistämisen jälkeen palvelimen ylläpitäjät huomaavat Dashboardissa uusia laatoituksia, jotka sisältävät erityisesti Lightning-tietoja.



- Salama tasapaino
- BTC kanavissa
  - BTC:n avauskanavat
  - BTC paikallinen saldo
  - BTC etätasapaino
  - BTC:n kanavien sulkeminen
- BTC On-Chain
  - BTC vahvisti
  - BTC vahvistamaton
  - BTC varattu
- Salama-palvelut
  - Ride the Lightning (RTL).


Palvelimen ylläpitäjät pääsevät RTL:n Lightning-solmujen hallintaan napsauttamalla joko Ride the Lightning -logoa Lightning-palvelut -laatassa tai vasemmanpuoleisen valikon lompakoiden alapuolella olevaa Lightning-kohtaa.


**Huomautus!**


Sisäisen salamasolmun yhdistäminen ei onnistu - Jos sisäinen yhteys ei onnistu, vahvista:


1. Bitcoin On-Chain-solmu on täysin synkronoitu

2. Sisäinen salamasolmu on "Käytössä" kohdassa "Salama" > "Asetukset" > "BTC Lightning Settings"


Jos et pysty muodostamaan yhteyttä Lightning-solmuun, voit yrittää käynnistää palvelimen uudelleen tai lukea lisätietoja BTCPay Serverin virallisesta dokumentaatiosta; https://docs.btcpayserver.org/Troubleshooting/. Et voi hyväksyä Lightning-maksuja kaupassasi ennen kuin Lightning-solmusi näkyy "Online". Yritä testata Lightning-yhteytesi napsauttamalla "Public Node Info" -linkkiä.


### Salama Wallet


Vasemman valikkopalkin Lightning Wallet -vaihtoehdossa palvelimen ylläpitäjät pääsevät helposti käsiksi RTL:ään, julkiseen solmuunsa ja BTCPay-palvelimen myymälän Lightning-asetuksiin.


#### Solmun sisäiset tiedot


Palvelimen ylläpitäjät voivat napsauttaa sisäisen solmun tietoja nähdäkseen palvelimen tilan (Online/Offline) ja yhteysmerkkijonon Clearnetiin tai Toriin.


![image](assets/en/033.webp)


#### Vaihda yhteys


Voit vaihtaa ulkoisen Lightning-solmun siirtymällä kohtaan "Lightning-asetukset" ja napsauttamalla "Vaihda yhteys" (kohdan "Julkisen solmun tiedot" vieressä). Tämä nollaa nykyiset asetukset. Syötä uudet solmun tiedot, napsauta Tallenna, ja kauppa päivittyy vastaavasti.


![image](assets/en/034.webp)


#### Palvelut


Jos palvelimen ylläpitäjä päättää asentaa useita palveluja Lightning-toteutusta varten, ne luetellaan tässä. LND-standarditoteutuksen kanssa ylläpitäjillä on Ride The Lightning (RTL) vakiovälineenä solmujen hallintaan.


#### BTC Lightning Wallet asetukset


Kun olet lisännyt Lightning-solmun kauppaan edellisessä vaiheessa, kaupan omistajat voivat vielä poistaa sen käytöstä myymälässään käyttämällä Lightning-asetusten yläosassa olevaa Vaihda-vaihtoehtoa.


![image](assets/en/035.webp)


#### Lightning Maksuvaihtoehdot


Kaupan omistajat voivat asettaa seuraavat parametrit parantaakseen Lightning-kokemusta asiakkailleen.



- Näyttää salamamaksujen summat Satoshisina.
- Lisää hyppyvihjeitä yksityisiä kanavia varten Lightning Invoice:een.
- Yhtenäistä On-Chain- ja Lightning-maksun URL/QR-koodit kassalla.
- Aseta kuvausmalli salamalaskuille.


#### LNURL


Kaupan omistajat voivat valita, käyttävätkö he LNURL:ää vai eivät. Lightning Network URL eli LNURL on ehdotettu standardi Lightning Payerin ja maksunsaajan väliselle vuorovaikutukselle. Lyhyesti sanottuna LNURL on bech32-koodattu URL-osoite, jonka etuliitteenä on LNURL. Lightning Wallet:n odotetaan purkavan URL-osoitteen, ottavan yhteyttä URL-osoitteeseen ja odottavan JSON-objektia, jossa on lisäohjeita, erityisesti tunniste, joka määrittelee LNURL:n käyttäytymisen.



- Ota LNURL käyttöön
- LNURL Klassinen tila
  - Wallet-yhteensopivuutta varten, Bech32-koodattu (klassinen) vs. selkeätekstinen URL-osoite (tulossa)
- Salli maksunsaajan antaa kommentti.


### Esimerkki 1


#### Muodosta yhteys Lightningiin sisäisen solmun kautta (järjestelmänvalvoja)


Tämä vaihtoehto on käytettävissä vain, jos olet tämän instanssin järjestelmänvalvoja tai jos järjestelmänvalvoja on muuttanut oletusasetuksia niin, että käyttäjät voivat käyttää sisäistä salamasolmua.


Napsauta ylläpitäjänä Lightning Wallet vasemmanpuoleisessa valikkopalkissa. BTCPay Server pyytää sinua valitsemaan toisen kahdesta vaihtoehdosta Lightning-solmun liittämiseksi: sisäinen solmu tai mukautettu ulkoinen solmu. Napsauta "Käytä sisäistä solmua" ja napsauta sitten "Tallenna"


#### Lightning-solmun hallinta (RTL)


Kun olet muodostanut yhteyden sisäiseen Lightning-solmuun, BTCPay Server päivittyy ja näyttää ilmoituksen "BTC Lightning node updated", joka vahvistaa, että olet nyt yhdistänyt Lightningin myymälääsi.


Salamasolmun hallinta on palvelimen ylläpitäjän tehtävä. Siihen kuuluu seuraavaa:


- Hallitse tapahtumaa
- Maksuvalmiuden hallinta
  - Saapuva likviditeetti
  - Lähtevä likviditeetti
- Vertaisten ja kanavien hallinta
  - Liitetyt vertaisvertaisvertaisvertaisvertaisvertaisvertaisvertaiset
  - Kanavamaksut
  - Kanavan tila
- Kanavan tilojen varmuuskopiointi usein.
- Reititysraporttien tarkistaminen
- Vaihtoehtoisesti voit käyttää Loopin kaltaisia palveluja.


Kaikki salamasolmujen hallinta tapahtuu vakiona RTL:n kanssa (olettaen, että käytät LND-toteutusta). Järjestelmänvalvojat voivat napsauttaa Lightning Wallet -solmua BTCPay Serverissä ja löytää painikkeen RTL:n avaamiseksi. BTCPay Serverin tärkein kojelauta on nyt päivitetty Lightning Network-laatoilla, mukaan lukien nopea pääsy RTL:ään.


### Esimerkki 2


#### Yhdistä salama Albyn kanssa


Albyn kaltaiseen säilyttäjään yhteyttä ottaessaan kauppojen omistajien on ensin luotava tili ja käytävä osoitteessa https://getalby.com/


![image](assets/en/036.webp)


Kun olet luonut Alby-tilin, siirry BTCPay Server -myymälääsi.


Vaihe 1: Napsauta "Set up a Lightning node" (Lightning-solmun perustaminen) kojelaudalla tai "Lightning" (Lightning) lompakoiden alapuolella.


![image](assets/en/037.webp)


Vaihe 2: Aseta Albyn toimittamat Wallet-yhteystietosi. Napsauta Albyn kojelaudalla Wallet:ta. Täältä löydät "Wallet Connection Credentials". Kopioi nämä tunnistetiedot. Liitä Albyn valtakirjat BTCPay Serverin Connection configuration -kenttään.


![image](assets/en/038.webp)


Vaihe 3: Kun olet antanut BTCPay-palvelimelle yhteyden tiedot, napsauta "Testaa yhteys" -painiketta varmistaaksesi, että yhteys toimii oikein. Huomaa näytön yläreunassa oleva viesti "Yhteys salaman solmuun onnistui". Tämä vahvistaa, että kaikki toimii odotetulla tavalla.


![image](assets/en/039.webp)


Vaihe 4: Napsauta "Tallenna", ja kauppasi on nyt yhdistetty Albyn Lightning-solmuun.


![image](assets/en/040.webp)


**!Huom!**


Älä koskaan luota säilyttäjän Lightning-ratkaisuun enempää arvoa kuin olet valmis menettämään.


### Taitojen yhteenveto


Tässä jaksossa opit:



- Sisäisen tai ulkoisen Lightning-solmun liittäminen
- Kojelaudan eri salamoihin liittyvien laatikoiden sisältö ja toiminta
- Lightning Wallet:n konfigurointi käyttämällä Voltage Surge- tai Alby-jännitettä


### Tietojen arviointi Käytännön tarkastelu


Kuvaile joitakin eri vaihtoehtoja Lightning Wallet:n liittämiseksi myymälääsi.


# BTCPay-palvelin Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Yleiskatsaus kojelautaan


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay Server on modulaarinen ohjelmistopaketti. On kuitenkin olemassa standardeja, joita jokaisen BTCPay Serverin on noudatettava, ja nämä standardit ohjaavat järjestelmänvalvojan ja käyttäjien välistä vuorovaikutusta. Aloitetaan kojelaudasta. Jokaisen BTCPay Server -palvelimen tärkein sisäänkirjautumiskohta kirjautumisen jälkeen. Dashboard tarjoaa yleiskatsauksen kauppasi suorituskyvystä, Wallet:n tämänhetkisestä saldosta ja viimeisten 7 päivän tapahtumista. Koska kyseessä on modulaarinen näkymä, liitännäisohjelmat voivat käyttää tätä näkymää hyödykseen ja luoda omia laatoituksiaan Dashboardiin. Tällä kurssilla käsittelemme vain vakiolisäosia ja -sovelluksia sekä niiden näkymiä koko BTCPay Serverissä.


### Kojelaudan laatat


BTCPay Serverin kojelaudan päänäkymässä on käytettävissä pari vakiolaattaa. Nämä laatat on suunniteltu niin, että myymälän omistaja tai ylläpitäjä voi hallita myymäläänsä nopeasti yhdellä yleiskatsauksella.



- Wallet tasapaino
- Transaktiotoiminta
- Lightning-saldo (jos Lightning on käytössä kaupassa)
- Lightning-palvelut (jos Lightning on käytössä kaupassa)
- Viimeaikaiset liiketoimet.
- Viimeisimmät laskut
- Nykyiset aktiiviset joukkorahoitukset
- Myymälän suorituskyky / myydyimmät tuotteet.


### Wallet tasapaino


Wallet:n saldolaatta antaa nopean yleiskuvan Wallet:n varoista ja suorituskyvystä. Sitä voidaan tarkastella joko BTC- tai Fiat-valuutassa viikoittaisena, kuukausittaisena tai vuosittaisena kuvaajana.


![image](assets/en/041.webp)


### Transaktiotoiminta


Wallet-saldolaatan vieressä BTCPay Server näyttää nopean yleiskatsauksen vireillä olevista maksuista, tapahtumien määrästä viimeisten 7 päivän aikana ja siitä, onko myymäläsi myöntänyt palautuksia. Napsauttamalla Hallitse-painiketta pääset vireillä olevien maksujen hallintaan (lisätietoja maksuista on luvussa BTCPay Server - Maksut).


![image](assets/en/042.webp)


### Salama tasapaino


Tämä näkyy vain, kun Salama on aktivoitu.


Kun järjestelmänvalvoja on sallinut Lightning Network:n käyttöoikeuden, BTCPay Serverin kojelaudalla on nyt uusi laatta, jossa on Lightning-solmun tiedot. Kuinka paljon BTC:tä on kanavissa, miten tämä on tasapainotettu paikallisesti tai etänä (saapuva tai lähtevä likviditeetti), ovatko kanavat sulkeutumassa tai avautumassa ja kuinka paljon Bitcoin:aa On-Chain:lla on Lightning-solmussa.


![image](assets/en/043.webp)


### Salama-palvelut


Tämä näkyy vain, kun salama on aktiivinen.


Sen lisäksi, että ylläpitäjät näkevät Lightning-saldosi BTCPay-palvelimen kojelaudalla, he näkevät myös Lightning-palveluiden laatan. Täältä ylläpitäjät löytävät pikapainikkeet työkaluille, joita he käyttävät Lightning-solmunsa hallintaan; esimerkiksi Ride the Lightning on yksi BTCPay Serverin vakiotyökalu Lightning-solmun hallintaan.


![image](assets/en/044.webp)


### Viimeaikaiset liiketoimet


Viimeisimmät tapahtumat -laatta näyttää kauppasi viimeisimmät tapahtumat. Yhdellä napsautuksella BTCPay-palvelimen ylläpitäjä näkee viimeisimmän tapahtuman ja näkee, onko siihen kiinnitettävä huomiota.


![image](assets/en/045.webp)


### Viimeisimmät laskut


Viimeisimmät laskut -laatta näyttää 6 viimeisintä BTCPay-palvelimen luomaa laskua, mukaan lukien tila ja Invoice-summa. Laatassa on myös "Näytä kaikki" -painike, jolla pääset helposti koko Invoice-yleiskatsaukseen.


![image](assets/en/046.webp)


### Myyntipiste ja joukkorahoitus


Koska BTCPay Server tarjoaa joukon vakiolisäosia tai -sovelluksia, Point Of Sale ja Crowdfund ovat BTCPay Serverin kaksi tärkeintä lisäosaa. Jokaisen myymälän ja Wallet:n kanssa BTCPay Serverin käyttäjä voi generate käyttää niin monta myyntipistettä tai joukkorahoitusta kuin parhaaksi näkee. Kukin luo uuden kojelautalaatan, joka näyttää liitännäisten suorituskyvyn.


![image](assets/en/047.webp)


Huomaa pieni ero myyntipisteen ja joukkorahoituslaatan välillä. Ylläpitäjä näkee myydyimmät myytävät kohteet Myyntipiste-laatassa. Joukkorahoituslaatassa tästä tulee Top Perks. Molemmissa laatikoissa on pikapainikkeet, joiden avulla voit hallita kyseistä sovellusta ja tarkastella viimeisimpiä laskuja, jotka on luotu suosituimpien kohteiden tai suosituimpien etujen perusteella.


![image](assets/en/048.webp)


**!?Huomautus!?**


Saldokaaviot ja viimeaikaiset maksutapahtumat ovat käytettävissä vain On-Chain-maksutavoille. Lightning Network-saldoja ja maksutapahtumia koskevat tiedot ovat työlistalla. BTCPay-palvelimen versiosta 1.6.0 alkaen Lightning Network:n perussaldot ovat saatavilla.


### Taitojen yhteenveto


Tässä jaksossa opit seuraavat asiat:



- Tärkeimmän aloitussivun laattojen perusasettelua kutsutaan nimellä Dashboard.
- Perusymmärrys kunkin laatan sisällöstä.


### Osaamisen arvioinnin arviointi


Luettele muistista niin monta laattaa kuin mahdollista Dashboardista.


## BTCPay Server - Tallennusasetukset


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


BTCPay Server -ohjelmistossa on kahdenlaisia asetuksia. BTCPay Server -kauppakohtaiset asetukset, asetuspainike, joka löytyy vasemmasta valikkorivistä Dashboardin alapuolelta, ja BTCPay Server -asetukset, jotka löytyvät valikkorivin alareunasta, suoraan Accountin yläpuolelta. BTCPay Server -palvelinkohtaisia asetuksia voivat tarkastella vain palvelimen ylläpitäjät.


Kaupan asetukset koostuvat monista välilehdistä, joilla kukin asetuskokonaisuus voidaan luokitella.



- Yleistä
- Hinnat
- Kassan ulkonäkö
- Access Tokens
- Käyttäjät
- Roolit
- Verkkokoukut
- Maksujen käsittelijät
- Sähköpostit
- Lomakkeet


### Yleistä


Yleiset asetukset -välilehdellä kaupan omistajat asettavat brändin ja maksujen oletusasetukset. Myymälän alkuasetusten yhteydessä annettiin myymälän nimi; tämä näkyy Yleiset asetukset -kohdassa Myymälän nimi. Täällä myymälän omistaja voi myös asettaa verkkosivustonsa vastaamaan brändäystä ja myymälätunnuksen, jonka ylläpitäjä tunnistaa tietokannassa.


#### Brändäys


Koska BTCPay Server on FOSS, kaupan omistaja voi tehdä mukautetun brändäyksen, joka sopii hänen kauppaansa. Aseta brändin väri, tallenna brändisi logot ja lisää mukautettu CSS julkisille/asiakkaille suunnatuille sivuille (laskut, maksupyynnöt, pull-maksut)


#### Maksu


Kaupan omistajat voivat asettaa maksujen asetuksissa kaupan oletusvaluutan (joko Bitcoin tai mikä tahansa fiat-valuutta).


#### Anna kenen tahansa luoda laskuja


Tämä asetus on tarkoitettu kehittäjille tai BTCPay Serverin päälle rakentajille. Kun tämä asetus on käytössä kaupassasi, se sallii ulkopuolisen maailman luoda laskuja BTCPay Server -instanssissasi.


#### Lisämaksun (verkkomaksu) lisääminen laskuihin


BTCPayn ominaisuus, joka suojaa kauppiaita Dust-hyökkäyksiltä tai asiakkaita kalliilta maksuilta myöhemmin, kun kauppiaan on siirrettävä suuri määrä Bitcoin:tä kerralla. Esimerkiksi asiakas loi Invoice:n 20$:n arvosta ja maksoi sen osittain maksamalla 1$ 20 kertaa, kunnes Invoice oli maksettu kokonaan. Kauppiaalla on nyt suurempi maksutapahtuma, mikä lisää Mining-kustannuksia, jos kauppias päättää siirtää kyseiset varat myöhemmin. Oletusarvoisesti BTCPay soveltaa ylimääräistä verkkokustannusta Invoice:n kokonaissummaan, jotta tämä kulu katetaan kauppiaalle, kun Invoice maksetaan useissa transaktioissa. BTCPay tarjoaa useita vaihtoehtoja tämän suojaustoiminnon mukauttamiseksi. Voit soveltaa verkkomaksua:



- Vain jos asiakas maksaa Invoice:stä useamman kuin yhden maksun (yllä olevassa esimerkissä, jos asiakas on luonut Invoice:n 20\$:n arvosta ja maksanut 1\$:n, maksettava Invoice:n kokonaismäärä on nyt 19\$ + verkkomaksu. Verkkomaksu peritään ensimmäisen maksun jälkeen)
- Jokaisella maksulla (myös ensimmäisellä maksulla, esimerkissämme summa on 20\$ + verkkomaksu heti, jopa ensimmäisellä maksulla)
- Älä koskaan lisää verkkomaksua (poistaa verkkomaksun kokonaan käytöstä)


Vaikka se suojaa Dust-tapahtumilta, se voi myös vaikuttaa kielteisesti yrityksiin, jos siitä ei tiedoteta asianmukaisesti. Asiakkailla voi olla lisäkysymyksiä ja he voivat luulla, että veloitat heiltä liikaa.


#### Invoice raukeaa, jos koko summaa ei ole maksettu sen jälkeen?


Invoice:n ajastin on oletusarvoisesti asetettu 15 minuuttiin. Ajastin toimii suojamekanismina volatiliteettia vastaan, sillä se lukitsee Bitcoin-määrän Bitcoin:n ja Exchange:n välille asetettujen Bitcoin:n ja Exchange:n välisten hintojen mukaisesti. Jos asiakas ei maksa Invoice-maksua määritellyn ajan kuluessa, Invoice katsotaan vanhentuneeksi. Invoice katsotaan "maksetuksi" heti, kun transaktio näkyy Blockchain:ssä (ilman vahvistuksia), ja se on "valmis", kun se saavuttaa kauppiaan määrittelemän vahvistusten määrän (yleensä 1-6). Ajastin on muokattavissa minuuteittain.


#### Pidätkö Invoice:tä maksettuna, vaikka maksettu määrä olisi X prosenttia odotettua pienempi?


Kun asiakas käyttää Exchange Wallet:ää maksaakseen suoraan Invoice:sta, Exchange perii pienen maksun. Tämä tarkoittaa, että tällaista Invoice:a ei pidetä täysin valmiina. Invoice merkitään "maksettu osittain". Voit asettaa tässä prosenttiosuuden, jos kauppias haluaa hyväksyä vajaasti maksetut laskut.


### Hinnat


BTCPay-palvelimella, kun Invoice generoidaan, se tarvitsee aina ajantasaisimman ja tarkimman Bitcoin-to-fiat-hinnan. Kun ylläpitäjät luovat uuden myymälän BTCPay Serverissä, heitä pyydetään asettamaan haluamansa hintalähde. Kun kauppa on perustettu, kaupan omistajat voivat muuttaa hintalähdettä tällä välilehdellä milloin tahansa.


#### Kehittynyt korkosäännön skriptaaminen


Pääasiassa tehokäyttäjien käytössä. Jos se on kytketty päälle, kaupan omistajat voivat luoda skriptejä hintakäyttäytymisen ja asiakkaiden veloittamisen ympärille.


#### Testaus


Nopea testauspaikka haluamillesi valuuttapareille. Tämä ominaisuus sisältää myös mahdollisuuden tarkistaa oletusvaluuttaparit REST-kyselyn avulla.


### Kassan ulkonäkö


Kassan ulkonäkö -välilehti alkaa Invoice-kohtaisilla asetuksilla ja oletusmaksutavalla, ja se ottaa käyttöön tietyt maksutavat, kun asetetut vaatimukset täyttyvät.


#### Invoice asetukset


Oletusmaksutavat. BTCPay-palvelin tarjoaa vakiokokoonpanossaan kolme vaihtoehtoa.



- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain & Lightning)


Voimme asettaa myymäläämme parametreja, joiden mukaan asiakas on vuorovaikutuksessa Lightningin kanssa vain silloin, kun hinta on pienempi kuin X-määrä, ja päinvastoin On-Chain-tapahtumien osalta, kun X on suurempi kuin Y, On-Chain-maksuvaihtoehto esitetään aina.


![image](assets/en/049.webp)


#### Kassa


BTCPay Server -versiossa 1.7 otettiin käyttöön uusi Checkout Interface, Checkout V2. Koska julkaisu 1.9 standardoitiin, ylläpitäjät ja kauppojen omistajat voivat edelleen asettaa kassan edelliseen julkaisuun. Käyttämällä vaihtokytkintä "Käytä klassista kassakäytäntöä", kaupan omistaja voi palauttaa kaupan aiempaan kassakäytäntöön. BTCPay Serverissä on myös valikoituja esiasetuksia verkkokauppaa tai myymäläkokemusta varten.


![image](assets/en/050.webp)


Kun asiakas on vuorovaikutuksessa myymälän kanssa ja luo Invoice:n, Invoice:lle on asetettu voimassaoloaika. Oletusarvoisesti BTCPay Server asettaa sen 5 minuutiksi, ja järjestelmänvalvojat voivat säätää sen mieleisekseen. Kassasivua voidaan edelleen mukauttaa tarkistamalla seuraavat parametrit:



- Juhli maksua näyttämällä konfettia
- Näytä kaupan otsikko (nimi ja logo)
- Näytä "Maksa Wallet:ssä" -painike
- Yhtenäistetään On-Chain- ja off-chain-maksut URL/QR-osoitteet
- Näytä salamamaksujen määrät Satoshisina
- Automaattinen kielen tunnistaminen kassalla


![image](assets/en/051.webp)


Kun automaattista kielen tunnistusta ei ole asetettu, BTCPay Server näyttää oletusarvoisesti englannin kielen. Kaupan omistaja voi muuttaa tämän oletusarvon haluamakseen kieleksi.


![image](assets/en/052.webp)


Napsauta pudotusvalikkoa, ja myymälän omistajat voivat asettaa kassasivulla näytettävän mukautetun HTML-otsikon.


![image](assets/en/053.webp)


Varmistaakseen, että asiakkaat tietävät maksutapansa, myymälän omistaja voi nimenomaisesti asettaa kassan aina vaatimaan käyttäjiä valitsemaan haluamansa maksutavan. Kun Invoice on maksettu, BTCPay Server antaa asiakkaan palata verkkokauppaan. Kaupan omistajat voivat asettaa tämän uudelleenohjauksen toimimaan automaattisesti sen jälkeen, kun asiakas on maksanut.


![image](assets/en/054.webp)


#### Julkinen vastaanotto


Kaupan omistaja voi asettaa kuittisivut julkisiksi julkisten kuittien asetuksissa, jolloin kuittisivulla näkyy maksuluettelo ja QR-koodi, jonka avulla asiakas pääsee helposti käsiksi kuittiin.


![image](assets/en/055.webp)


### Access Tokens


Pääsykoodeja käytetään tiettyjen sähköisen kaupankäynnin integraatioiden tai räätälöityjen integraatioiden kanssa.


![image](assets/en/056.webp)


### Käyttäjät


Myymälän käyttäjät ovat paikka, jossa myymälän omistaja voi hallinnoida työntekijöitään, heidän tilejään ja pääsyä myymälään. Kun henkilökunnan jäsenet ovat luoneet tilinsä, myymälän omistaja voi lisätä tiettyjä käyttäjiä myymälään vieraskäyttäjiksi tai omistajiksi. Jos haluat määritellä tarkemmin henkilökunnan jäsenen roolin, katso seuraava osio "BTCPay-palvelimen myymäläasetukset - Roolit"


![image](assets/en/057.webp)


### Roolit


Kaupan omistaja ei ehkä pidä käyttäjän vakiorooleja tarpeeksi merkittävinä. Mukautettujen roolien asetuksissa kaupan omistaja voi määritellä kunkin roolin tarkat tarpeet liiketoiminnassaan.


(1) Voit luoda uuden roolin napsauttamalla "+ Lisää rooli" -painiketta.


![image](assets/en/058.webp)


(2) Kirjoita roolin nimi, esimerkiksi "Cashier".


![image](assets/en/059.webp)


(3) Määritä roolin yksittäiset käyttöoikeudet.



- Muokkaa myymälöitäsi.
- Hallitse myymälöihisi liitettyjä Exchange-tilejä.
  - Näytä myymälöihisi liitetyt Exchange-tilit.
- Hallitse vetomaksuja.
- Luo pull-maksuja.
  - Luo hyväksymättömiä pull-maksuja.
- Muokkaa laskuja.
  - Tarkastele laskuja.
  - Luo Invoice.
  - Luo laskuja myymälöihisi liittyvistä salamasolmuista.
- Näytä myymälät.
  - Tarkastele laskuja.
  - Tarkastele maksupyyntöjäsi.
  - Muokkaa kauppojen verkkokoukkuja.
- Muokkaa maksupyyntöjäsi.
  - Tarkastele maksupyyntöjäsi.
- Käytä myymälöihisi liittyviä salamasolmuja.
  - Näytä myymälöihisi liittyvät salamalaskut.
  - Luo laskuja myymälöihisi liittyvistä salamasolmuista.
- Talleta varoja myymälöihisi liitetyille Exchange-tileille.
- Nosta varoja Exchange-tileiltä myymälääsi.
- Vaihda varoja myymäläsi Exchange-tileillä.


Kun rooli luodaan, nimi on kiinteä, eikä sitä voi muuttaa sen jälkeen, kun se on muokkaustilassa.


![image](assets/en/060.webp)


### Verkkokoukut


BTCPay Serverissä on kohtuullisen helppoa luoda uusi "Webhook". BTCPay Serverin Kaupan asetukset - Webhooks-välilehdellä kaupan omistaja voi helposti luoda uuden webhookin napsauttamalla "+ Create Webhook". Webhookien avulla BTCPay Server voi lähettää kauppaan liittyviä HTTP-tapahtumia muille palvelimille tai verkkokauppaintegraatioille.


![image](assets/en/061.webp)


Olet nyt Webhookin luomisen näkymässä. Varmista, että tiedät hyötykuorman URL-osoitteen ja liitä se BTCPay-palvelimeen. Kun olet liittänyt hyötykuorman URL-osoitteen, sen alla näkyy webhookin salaisuus. Kopioi webhookin salaisuus ja anna se päätepisteessä. Kun kaikki on asetettu, voit vaihtaa BTCPay Serverissä "Automaattisen uudelleentoimituksen" BTCPay Server yrittää toimittaa uudelleen kaikki epäonnistuneet toimitukset 10 sekunnin, 1 minuutin ja enintään 6 kertaa 10 minuutin kuluttua. Voit vaihtaa jokaisen tapahtuman välillä tai määrittää tapahtumat tarpeidesi mukaan. Varmista, että otat webhookin käyttöön ja paina "Add webhook" -painiketta tallentaaksesi sen.


![image](assets/en/062.webp)


Webhookien ei ole tarkoitus olla yhteensopivia Bitpayn API:n kanssa. BTCPay Serverissä on kaksi erillistä IPN:ää (BitPayn termein: "Instant Payment Notifications").



- Webhookp
- Ilmoitukset


Käytä ilmoitus-URL-osoitetta vain, kun luot laskuja Bitpayn API:n kautta.


### Maksujen käsittelijät


Maksuprosessorit toimivat yhdessä BTCPay Serverin Maksut-käsitteen kanssa. Payout-aggregaattorin avulla voit koota useita maksutapahtumia ja lähettää ne kerralla. Payout-prosessoreiden avulla myymälän omistaja voi automatisoida eräpohjaiset maksut. BTCPay Server tarjoaa kaksi tapaa automatisoituja maksuja varten: On-Chain ja off-chain (LN).


Kaupan omistaja voi klikata ja määrittää molemmat maksuprosessorit erikseen. Myymälän omistaja saattaa haluta käyttää On-Chain-prosessoria vain kerran X tunnin välein, kun taas off-chain-prosessori saattaa toimia muutaman minuutin välein. On-Chain:lle voidaan myös asettaa tavoite, mihin lohkoon se sisällytetään. Oletusarvoisesti tämä on asetettu arvoon 1 (tai seuraavaan käytettävissä olevaan lohkoon). Huomaa, että off-chain-maksuprosessorin asettamisessa on vain intervalliajastin eikä lohkokohtaista tavoitetta. Lightning Network-maksut ovat välittömiä.


![image](assets/en/063.webp)

![image](assets/en/064.webp)


Myymälän omistajat voivat määrittää On-Chain-prosessorin vain, jos heidän myymäläänsä on liitetty Hot Wallet.


![image](assets/en/065.webp)


Kun olet määrittänyt maksuprosessorin, voit nopeasti poistaa tai muuttaa sitä palaamalla BTCPay-palvelinkaupan asetusten Maksuprosessori-välilehdelle.


**Huomautus**


Maksuprosessori On-Chain - Maksuprosessori On-Chain voi toimia vain myymälässä, johon on liitetty Hot Wallet. Jos Hot Wallet:ää ei ole liitetty, BTCPay-palvelimella ei ole Wallet-avaimia eikä se pysty käsittelemään maksuja automaattisesti.


### Sähköpostit


BTCPay Server voi käyttää sähköposteja ilmoituksiin tai, kun ne on asetettu oikein, tilien palauttamiseen, jotka on luotu instanssissa. Vakiona BTCPay Server ei lähetä sähköpostia, kun esimerkiksi salasana on kadonnut.


![image](assets/en/066.webp)


Ennen kuin myymälän omistaja voi asettaa sähköpostisääntöjä tiettyjen tapahtumien käynnistämiseksi myymälässään, hänen on ensin määritettävä sähköpostin perusasetukset. BTCPay Server tarvitsee nämä asetukset, jotta voit lähettää sähköposteja myymälääsi liittyvistä tapahtumista tai salasanan nollaamisesta.


BTCPay Server on helpottanut näiden tietojen täyttämistä käyttämällä "Quick Fill" -vaihtoehtoa:



- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid


Käyttämällä pikatäyttöä BTCPay Server täyttää SMTP-palvelimen ja portin kentät valmiiksi. Nyt myymälän omistajan tarvitsee vain täyttää tunnistetietonsa, mukaan lukien sähköpostiosoite Address, kirjautuminen (joka on yleensä sama kuin sähköpostiosoitteesi Address) ja salasana. BTCPay-palvelimen sähköpostiasetusten lisäasetuksena on poistaa TLS-varmenteen turvatarkastukset käytöstä; oletusarvoisesti tämä on käytössä.


![image](assets/en/067.webp)


Sähköpostisääntöjen avulla myymälän omistaja voi asettaa tietyt tapahtumat käynnistämään sähköpostiviestit tiettyihin sähköpostiosoitteisiin.



- Invoice Luotu
- Invoice Saatu maksu
- Invoice käsittely
- Invoice Vanhentunut
- Invoice Sovittu
- Invoice Virheellinen
- Invoice Maksu suoritettu


Jos asiakas on antanut sähköpostiosoitteen Address, nämä laukaisimet voivat myös lähettää tiedot asiakkaalle. Myymälän omistajat voivat esitäyttää otsikkorivin tehdäkseen selväksi, miksi sähköpostiviesti lähetettiin ja mikä sen laukaisi.


![image](assets/en/068.webp)


### Lomakkeet


Koska BTCPay-palvelin ei kerää mitään tietoja, kaupan omistaja voi haluta lisätä mukautetun lomakkeen kassakokemukseensa; näin kaupan omistaja voi kerätä asiakkaalta lisätietoja. BTCPay Server Form builder koostuu kahdesta osasta: lomakkeiden visuaalisesta ja kehittyneemmästä koodinäkymästä.


Kun luot uuden lomakkeen, BTCPay Server avaa uuden ikkunan, jossa pyydetään perustiedot siitä, mitä haluat uuden lomakkeen kysyvän. Aluksi myymälän omistajan on annettava uudelle lomakkeelle selkeä nimi; tätä nimeä ei voi muuttaa sen jälkeen, kun se on asetettu.


![image](assets/en/069.webp)


Kun myymälän omistaja on antanut lomakkeelle nimen, voit myös kytkeä kytkimen "Salli lomakkeen julkinen käyttö" asentoon ON, jolloin se muuttuu Green:ksi. Näin varmistetaan, että lomaketta käytetään jokaisessa asiakaskohtaisessa toimipisteessä. Jos esimerkiksi myymälän omistaja luo erillisen Invoice-lomakkeen ei myyntipisteen kautta, hän saattaa silti haluta kerätä tietoja asiakkaalta. Tämä kytkin mahdollistaa näiden tietojen keräämisen.


![image](assets/en/070.webp)


Jokainen lomake alkaa vähintään yhdellä Uusi lomakekentällä. Kaupan omistaja voi valita, minkä tyyppinen kenttä sen pitäisi olla.



- Teksti
- Numero
- Salasana
- Sähköposti
- URL
- Puhelinnumerot
- Päivämäärä
- Piilotetut kentät
- Fieldset
- Tekstialue avoimia kommentteja varten.
- Vaihtoehtojen valitsin


Jokaisella tyypillä on omat täytettävät parametrit. Kaupan omistaja voi asettaa sen mieleisekseen. Ensimmäisen luodun kentän alapuolella myymälän omistajat voivat lisätä uusia kenttiä tähän lomakkeeseen.


![image](assets/en/071.webp)


#### Edistyneet mukautetut lomakkeet


BTCPay Serverin avulla voit myös rakentaa lomakkeita koodilla. Erityisesti JSON. Sen sijaan, että katsoisit editoria, kaupan omistajat voivat klikata CODE-painiketta editorin vieressä ja päästä lomakkeidensa koodiin. Kenttämäärittelyssä voidaan asettaa vain seuraavat kentät; kenttien arvot tallennetaan Invoice:n metatietoihin:


| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | If true, the .value must be set in the form definition, and the user will not be able to change the field's value. ( example: the form definition's version)                                                                                                                                                                                                                                                                                                       |
| .fields.type          | The HTML input type text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                |
| .fields.options       | If .fields.type is select, the list of selectable values                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.options.text  | The text displayed for this option                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.value | The value of the field if this option is selected                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.type=fieldset | Create a HTML fieldset around the children .fields.fields (see below)                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.name          | The JSON property name of the field as it will appear in the invoice's metadata                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.value         | The default value of the field                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.required      | if true, the field will be required                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.label         | The label of the field                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.helpText      | Additional text to provide an explanation for the field.                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.fields        | You can organize your fields in a hierarchy, allowing child fields to be nested within the invoice’s metadata. This structure can help you better organize and manage the collected information, making it easier to access and interpret. For example, if you have a form that collects customer information, you can group the fields under a parent field called customer. Within this parent field, you might have child fields like name, Email, and address. |

Kentän nimi edustaa JSON-ominaisuuden nimeä, joka tallentaa käyttäjän antaman arvon Invoice:n metatietoihin. Joitakin tunnettuja nimiä voidaan tulkita ja muuttaa Invoice:n asetusten mukauttamiseksi.


| Field name       | Description            |
| ---------------- | ---------------------- |
| invoice_amount   | The invoice's amount   |
| invoice_currency | The invoice's currency |

Voit esitäyttää Invoice-lomakkeen kentät automaattisesti lisäämällä lomakkeen URL-osoitteeseen kyselymerkkijonoja, kuten "?your_field=value".


Seuraavassa on muutamia käyttötapauksia tälle ominaisuudelle:



- Käyttäjän syötön avustaminen: Esitäytä kentät tunnetuilla asiakastiedoilla, jotta asiakkaan on helpompi täyttää lomake. Jos esimerkiksi tiedät jo asiakkaan sähköpostiosoitteen Address, voit esitäyttää sähköpostikentän ja säästää näin aikaa.
- Henkilökohtaistaminen: Mukauta lomake asiakkaan mieltymysten tai segmentoinnin perusteella. Jos sinulla on esimerkiksi eri asiakastasoja, voit esitäyttää lomakkeen asiaankuuluvilla tiedoilla, kuten heidän jäsenyystasollaan tai tietyillä tarjouksilla.
- Seuranta: Seuraa asiakaskäyntien lähdettä piilokenttien ja esitäytettyjen arvojen avulla. Voit esimerkiksi luoda linkkejä, joissa on esitäytetyt utm_media-arvot kutakin markkinointikanavaa varten (esim. Twitter, Facebook, sähköposti). Näin voit analysoida markkinointitoimien tehokkuutta.
- A/B-testaus: Esitäytä kentät eri arvoilla testataksesi eri lomakeversioita, jolloin voit optimoida käyttäjäkokemuksen ja konversioluvut.


### Taitojen yhteenveto


Tässä jaksossa opit seuraavat asiat:



- Kaupan asetusten välilehtien ulkoasu ja toiminnot
- Useita vaihtoehtoja, joilla voidaan hienosäätää taustalla olevien Exchange-maksujen, osittaisten maksujen, pienten alimaksujen ja muiden maksujen käsittelyä.
- Mukauta kassan ulkoasua, mukaan lukien hintariippuvainen pääketju vs. Lightning-aktivointi laskuissa.
- Hallitse myymälän käyttöoikeustasoja ja käyttöoikeuksia eri rooleissa.
- Määritä automaattiset sähköpostiviestit ja niiden laukaisijat
- Luo mukautettuja lomakkeita asiakkaan lisätietojen keräämistä varten kassalla.


### Osaamisen arviointi


#### KA arvostelu


Mitä eroa on myymäläasetuksilla ja palvelinasetuksilla?


#### KA Hypoteettinen


Kuvaile joitakin vaihtoehtoja, jotka voit valita kohdassa Kassan ulkoasu > Invoice-asetukset, ja kerro, miksi.


## BTCPay Server - Palvelimen asetukset


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


BTCPay Server koostuu kahdesta eri asetusnäkymästä. Toinen on omistettu Store-asetuksille ja toinen Server-asetuksille. Jälkimmäinen on vain palvelimen ylläpitäjien käytettävissä, ei myymälän omistajien. Palvelimen ylläpitäjät voivat lisätä käyttäjiä, luoda mukautettuja rooleja, määrittää sähköpostipalvelimen, asettaa käytäntöjä, suorittaa ylläpitotehtäviä, tarkistaa kaikki BTCPay Serveriin liitetyt palvelut, ladata tiedostoja palvelimelle tai tarkistaa lokit.


### Käyttäjät


Kuten edellisessä osassa mainittiin, palvelimen ylläpitäjät voivat kutsua käyttäjiä palvelimelleen lisäämällä heidät Käyttäjät-välilehdelle.


### Palvelimen laajuiset mukautetut roolit


BTCPay Serverillä on kahdenlaisia mukautettuja rooleja: myymäläkohtaiset mukautetut roolit ja koko palvelimen kattavat mukautetut roolit BTCPay Serverin asetuksissa. Molemmat sisältävät samanlaiset oikeudet; jos ne kuitenkin asetetaan BTCpay Server Settings - Roles -välilehdellä, sovellettu rooli on koko palvelimen laajuinen ja koskee useita kauppoja. Huomaa "Server-wide"-merkintä palvelimen asetuksissa olevissa mukautetuissa rooleissa.


![image](assets/en/072.webp)


### Palvelimen laajuiset mukautetut roolit


Palvelimen laajuinen mukautettujen roolien käyttöoikeusjoukko;



- Muokkaa myymälöitäsi.
- Hallitse myymälöihisi liitettyjä Exchange-tilejä.
  - Näytä myymälöihisi liitetyt Exchange-tilejä.
- Hallitse vetomaksuja.
- Luo pull-maksuja.
  - Luo hyväksymättömiä pull-maksuja.
- Muokkaa laskuja.
  - Tarkastele laskuja.
  - Luo Invoice.
  - Luo laskuja myymälöihisi liittyvistä salamasolmuista.
- Näytä myymälät.
  - Tarkastele laskuja.
  - Tarkastele maksupyyntöjäsi.
  - Muokkaa kauppojen verkkokoukkuja.
- Muokkaa maksupyyntöjäsi.
  - Tarkastele maksupyyntöjäsi.
- Käytä myymälöihisi liittyviä salamasolmuja.
  - Näytä myymälöihisi liittyvät salamalaskut.
  - Luo laskuja myymälöihisi liittyvistä salamasolmuista.
- Talleta varoja myymälöihisi liitetyille Exchange-tileille.
- Nosta varoja Exchange-tileiltä myymälääsi.
- Vaihda varoja myymäläsi Exchange-tileillä.


**!?Huomautus!?**


Kun rooli luodaan, nimi on kiinteä, eikä sitä voi muuttaa sen jälkeen, kun se on muokkaustilassa.


### Sähköposti


Palvelimen laajuiset sähköpostiasetukset näyttävät samankaltaisilta kuin myymäläkohtaiset sähköpostiasetukset. Tämä asetus ei kuitenkaan käsittele vain myymälöiden tai järjestelmänvalvojan lokien laukaisuja vaan myös muiden tapahtumien laukaisuja. Tämä sähköpostiasetus mahdollistaa myös salasanan palautuksen BTCPay-palvelimella kirjautumisen yhteydessä. Se toimii samalla tavalla kuin myymäläkohtaiset asetukset; ylläpitäjät voivat nopeasti täyttää sähköpostiparametrit ja syöttää sähköpostitietonsa, jolloin palvelin voi lähettää sähköposteja.


![image](assets/en/073.webp)


### Politiikat


BTCPay Server -käytäntöjen ylläpitäjät voivat määrittää erilaisia asetuksia aiheisiin, kuten Olemassa olevien käyttäjien asetukset, uusien käyttäjien asetukset, ilmoitusasetukset ja ylläpitoasetukset. Nämä on tarkoitettu uusien käyttäjien rekisteröimiseen ylläpitäjiksi tai tavallisiksi käyttäjiksi tai BTCPay Serverin piilottamiseen hakukoneilta lisäämällä se palvelimen otsikkoon.


![image](assets/en/074.webp)


#### Olemassa oleva käyttäjä Asetukset


Tässä käytettävissä olevat vaihtoehdot ovat erillisiä mukautetuista rooleista. Nämä lisäoikeudet voivat tehdä kaupasta tai sen omistajasta haavoittuvan hyökkäyksille. Käytännöt, jotka voidaan lisätä olemassa oleville käyttäjille:



- Salli muiden kuin pääkäyttäjien käyttää sisäistä Lightning-solmua myymälöissään.
  - Tämä antaisi kauppojen omistajille mahdollisuuden käyttää palvelimen ylläpitäjän Lightning-solmua ja siten hänen varojaan! Varo, tämä ei ole ratkaisu Lightningin käyttöoikeuden antamiseen.
- Salli muiden kuin pääkäyttäjien luoda Hot-lompakoita myymälöitään varten.
  - Näin kuka tahansa, jolla on tili BTCPay-palvelimesi instanssissa, voi luoda Hot-lompakoita ja tallentaa niiden palautus seed:n järjestelmänvalvojan palvelimelle. Tämä saattaa tehdä ylläpitäjästä vastuullisen kolmannen osapuolen varojen hallussapidosta!
- Salli muiden kuin pääkäyttäjien tuoda Hot-lompakoita myymälöihinsä.
  - Samoin kuin edellisessä Hot-lompakoiden luomista käsittelevässä kohdassa, tämä käytäntö mahdollistaa Hot Wallet:n tuonnin, mutta siinä on samat vaarat kuin Hot-lompakoiden luomista käsittelevässä kohdassa.


![image](assets/en/075.webp)


#### Uuden käyttäjän asetukset


Voimme määrittää joitakin tärkeitä asetuksia palvelimelle tulevien uusien käyttäjien hallintaa varten. Voimme asettaa uusille rekisteröinneille vahvistussähköpostin, poistaa uusien käyttäjien luomisen kirjautumisnäytön kautta ja rajoittaa muiden kuin järjestelmänvalvojien pääsyn käyttäjien luomiseen API:n kautta.



- Vaadi vahvistussähköposti rekisteröintiä varten.
  - Palvelimen ylläpitäjän on määritettävä sähköpostipalvelin.
- Poista uusien käyttäjien rekisteröinti palvelimella käytöstä
- Poista muiden kuin järjestelmänvalvojien pääsy käyttäjän luomisen API-päätepisteeseen.


Oletusarvoisesti BTCPay-palvelin on kytkenyt pois päältä kohdan "Poista uusien käyttäjien rekisteröinti palvelimella" ja poistanut muiden kuin järjestelmänvalvojien pääsyn käyttäjän luomisen API-päätepisteeseen. Tämä tehdään turvallisuuden vuoksi, jotta satunnaiset ihmiset, jotka törmäävät BTCPay-tunnukseesi, eivät voi luoda tilejä.


![image](assets/en/076.webp)


#### Ilmoitusasetukset


![image](assets/en/077.webp)


#### Huoltoasetukset


BTCPay Server on avoimen lähdekoodin projekti, joka on GitHubissa. Aina kun BTCPay Server julkaisee uuden version ohjelmistosta, ylläpitäjät voivat saada ilmoituksen, että uusi versio on saatavilla. Järjestelmänvalvojat saattavat myös haluta välttää hakukoneita (kuten Google, Yahoo ja DuckDuckGo) indeksoimasta BTCPay Server -verkkotunnusta. Koska BTCPay Server on FOSS, kehittäjät ympäri maailmaa voivat haluta luoda uusia ominaisuuksia. BTCPay Serverissä on kokeellinen ominaisuus, joka kytkettynä päälle antaa ylläpitäjille mahdollisuuden käyttää ominaisuuksia, joita ei ole tarkoitettu tuotantoon vaan testaukseen.



- Tarkista julkaisut GitHubista ja ilmoita, kun uusi BTCPay Server -versio on saatavilla.
- Estää hakukoneita indeksoimasta tätä sivustoa
- Ota kokeelliset ominaisuudet käyttöön.


![image](assets/en/078.webp)


#### Liitännäiset


BTCPay Server voi lisätä liitännäisiä ja laajentaa ominaisuuksiensa valikoimaa. Lisäosat ladataan oletusarvoisesti BTCPay Serverin plugin-builder-arkistosta. Ylläpitäjä voi kuitenkin halutessaan nähdä liitännäiset Pre-release-tilassa, ja jos liitännäisten kehittäjä sallii sen, palvelimen ylläpitäjä voi nyt asentaa liitännäisten beta-versioita.


![image](assets/en/079.webp)


##### Mukautusasetukset


Tavallinen BTCPay Server -käyttöönotto on käytettävissä asennuksen aikana määritetyn verkkotunnuksen kautta. Palvelimen ylläpitäjä voi kuitenkin määrittää pääkäyttäjätoimialueen uudelleen ja näyttää jonkin tietyn kaupan luoduista sovelluksista. Palvelimen ylläpitäjä voi myös määrittää tietyt verkkotunnukset tietyille sovelluksille.



- Näytä sovellus verkkosivuston juuressa
  - Näyttää luettelon mahdollisista sovelluksista, jotka voidaan näyttää pääkäyttäjätoimialueella.


![image](assets/en/080.webp)



- Kohdista tietyt verkkotunnukset tiettyihin sovelluksiin.
  - Kun napsautat määrittääksesi tietyn toimialueen tietyille sovelluksille, järjestelmänvalvoja voi määrittää niin monta tiettyihin sovelluksiin osoittavaa toimialuetta kuin on tarpeen.


![image](assets/en/081.webp)


#### Lohkon tutkimusmatkailijat


BTCPay-palvelimen vakiovarusteena on Mempool.space, koska sen Block explorer on transaktioita varten. Kun BTCPay Server luo uuden Invoice:n ja siihen on sidottu transaktio, kaupan omistaja voi avata transaktion napsauttamalla sitä. BTCPay Server osoittaa oletusarvoisesti Mempool.spacea Block explorer:ksi; palvelimen ylläpitäjä voi kuitenkin muuttaa tämän haluamakseen vaihtoehdoksi.


![image](assets/en/082.webp)


### Palvelut


"BTCPay-palvelimen asetukset: Palvelut"-välilehdellä on yleiskatsaus BTCPay-palvelimesi käyttämistä komponenteista. BTCPay-palvelimesi tarjoamat palvelut saattavat vaihdella käyttöönottomenetelmästä riippuen.


BTCPay-palvelimen ylläpitäjä voi avata kunkin palvelun ja määrittää erityisasetukset napsauttamalla kunkin palvelun takana olevaa "Katso tiedot"-painiketta.


![image](assets/en/083.webp)


#### LND (gRPC)


BTCPay tarjoaa LND:n GRPC-palvelun ulkopuolista kulutusta varten; löydät yhteystiedot tästä erityisestä asetusvalikosta; yhteensopivat lompakot on lueteltu täällä. BTCPay-palvelin tarjoaa myös QR-koodin yhteyttä varten, joka voidaan skannata ja soveltaa mobiilissa Wallet:ssä.


Palvelimen ylläpitäjät voivat avata lisätietoja.



- Isännän tiedot
- SSL:n käyttö
- Makaroonit
- AdminMacaroon
- LaskuMacaroon
- ReadonlyMacaroon
- GRPC SSL -salaussarja (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


BTCPay tarjoaa LND:n REST-palvelun ulkopuolisille; löydät yhteystiedot täältä; yhteensopivat lompakot on lueteltu täällä. Yhteensopiviin lompakoihin kuuluvat Joule, Alby ja ZeusLN. BTCPay-palvelin tarjoaa yhteyden muodostamista varten QR-koodin, joka voidaan skannata ja soveltaa yhteensopivassa Wallet:ssa.



- REST URI
- Makaroonit
- AdminMacaroon
- LaskuMacaroon
- ReadonlyMacaroon


#### LND seed Varmuuskopiointi


LND seed varmuuskopio on hyödyllinen, kun haluat palauttaa varoja LND Wallet:sta, jos palvelin vahingoittuu. Koska Lightning-solmu on Hot-Wallet, löydät luottamukselliset seed-tiedot tältä sivulta.


LND dokumentoi palautusprosessin. Katso dokumentaatio osoitteesta https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md.


#### Ride The Lightning


Ride the Lightning on avoimen lähdekoodin ohjelmistoksi rakennettu Lightning-solmujen hallintatyökalu. BTCPay Server käyttää RTL:ää Lightning-solmujen hallintakomponenttina pinossaan. BTCPay Serverin ylläpitäjät pääsevät RTL:ään Palvelimen asetukset - Palvelut-välilehden kautta tai napsauttamalla Lightning Wallet:tä.


#### Full node P2P


Palvelimen ylläpitäjät saattavat haluta yhdistää Bitcoin-solmunsa liikkuvaan Wallet:ään. Tällä sivulla on tietoa siitä, miten Full node:een voidaan muodostaa etäyhteys P2P-protokollan avulla. Tätä kurssia kirjoitettaessa BTCPay Server listaa Blockstream Green- ja Wasabi-lompakot yhteensopiviksi lompakoiksi. BTCPay Server tarjoaa yhteyden muodostamista varten QR-koodin, joka voidaan skannata ja soveltaa yhteensopivassa Wallet:ssä.


#### Full node RPC


Tällä sivulla on tietoja, joiden avulla voit muodostaa etäyhteyden Full node-laitteeseen RPC-protokollan avulla.


#### SSH


SSH:ta käytetään ylläpitotarkoituksiin. BTCPay Server näyttää alkuperäisen yhteyden muodostuskomennon, jolla palvelimesi tavoitetaan, ja SSH-avaimet, joilla on lupa muodostaa yhteys palvelimeesi. Palvelimen ylläpitäjät voivat halutessaan poistaa SSH-muutokset käytöstä BTCPay Serverin käyttöliittymän kautta.


#### Dynaaminen DNS


Dynaamisen DNS:n avulla sinulla on vakaa DNS-nimi, joka osoittaa palvelimeesi, vaikka IP Address muuttuisi säännöllisesti. Tätä suositellaan, jos isännöit BTCPay-palvelinta kotona ja haluat selkeän verkkotunnuksen, jolla voit käyttää palvelintasi.


Huomaa, että sinun on määritettävä NAT ja BTCPay Server -asennus oikein saadaksesi HTTPS-varmenteen.


### Teema


BTCPay Serverissä on vakiona kaksi teemaa: Teemoja: Vaalea ja Tumma. Niitä voi vaihtaa napsauttamalla vasemmalla alhaalla olevaa Account (Tili) -painiketta ja vaihtamalla Dark (Tumma) ja Light (Vaalea) -teemojen välillä. BTCPay Serverin ylläpitäjät voivat lisätä oman teemansa antamalla mukautetun CSS-teeman.


Järjestelmänvalvojat voivat laajentaa Light/Dark-teemaa lisäämällä oman mukautetun CSS:n tai asettamalla mukautetun teeman täysin mukautetuksi.


![image](assets/en/084.webp)


#### Palvelimen brändäys


Palvelimen ylläpitäjät voivat muuttaa BTCPay-palvelimen brändiä asettamalla yrityksesi koko palvelimen kattavan brändin. Koska BTCPay Server on FOSS-versio, palvelimen ylläpitäjät voivat merkitä ohjelmiston valkoisella tarralla ja mukauttaa sen ulkoasun yritykselleen sopivaksi.


![image](assets/en/085.webp)


### Huolto


Palvelimen ylläpitäjänä käyttäjät odottavat, että pidät palvelimesta hyvää huolta. BTCPay Serverin Maintenance-välilehdellä ylläpitäjä voi tehdä joitakin tärkeitä huoltotoimenpiteitä. Aseta verkkotunnus BTCPay Server -instanssille, käynnistä palvelin uudelleen tai siivoa se. Mahdollisesti tärkeintä on päivitysten suorittaminen.


BTCPay Server on avoimen lähdekoodin projekti, jota päivitetään usein. Jokaisesta uudesta julkaisusta ilmoitetaan joko BTCPay Server -ilmoituksissa tai virallisissa kanavissa, joiden kautta BTCPay Server kommunikoi.


![image](assets/en/086.webp)


#### Verkkotunnus


Kun BTCPay Server on perustettu, järjestelmänvalvoja saattaa haluta vaihtaa pois alkuperäisestä verkkotunnuksesta. Ylläpitäjä voi vaihtaa verkkotunnuksen Maintenance-välilehdellä. Kun olet napsauttanut Vahvista ja määrittänyt oikeat DNS-tietueet verkkotunnukselle, BTCPay Server päivittyy ja käynnistyy uudelleen palatakseen uuteen verkkotunnukseen.


![image](assets/en/087.webp)


#### Käynnistä uudelleen


Käynnistä BTCPay Server ja siihen liittyvät palvelut uudelleen.


![image](assets/en/088.webp)


#### Puhdas


BTCPay Server toimii Docker-komponenttien kanssa; päivitysten yhteydessä saattaa jäädä Docker-kuvien jäänteitä, väliaikaisia tiedostoja jne. jäljelle. Palvelimen ylläpitäjät voivat vapauttaa tilaa suorittamalla Clean-skriptin.


![image](assets/en/089.webp)


#### Päivitys


Se on ylläpito -välilehden tärkein vaihtoehto. BTCPay Server on yhteisön rakentama, ja siksi sen päivityssyklit ovat useimpia ohjelmistotuotteita tiheämpiä. Kun BTCPay Serveriin tulee uusi julkaisu, ylläpitäjät saavat siitä ilmoituksen ilmoituskeskukseensa. Napsauttamalla päivityspainiketta BTCPay Server tarkistaa GitHubista uusimman julkaisun, päivittää palvelimen ja käynnistää sen uudelleen. Ennen päivittämistä palvelimen ylläpitäjiä kehotetaan aina lukemaan BTCPay Serverin virallisten kanavien kautta jaetut julkaisutiedotteet.


![image](assets/en/090.webp)


### Lokit


Ongelman kohtaaminen ei ole koskaan hauskaa. Tässä asiakirjassa kuvataan yleisimmät työnkulut ja vaiheet, joiden avulla ongelma voidaan tunnistaa ja ratkaista tehokkaasti joko itsenäisesti tai yhteisön avustuksella.


Ongelman tunnistaminen on ratkaisevan tärkeää.


#### Ongelman toistaminen


Yritä ennen kaikkea selvittää, milloin ongelma ilmenee. Yritä toistaa ongelma. Yritä päivittää ja käynnistää palvelimesi uudelleen varmistaaksesi, että voit toistaa ongelman. Jos se kuvaa paremmin ongelmaasi, ota kuvakaappaus.


##### Palvelimen päivittäminen


Tarkista BTCPay Server -versiosi, jos se on paljon vanhempi kuin BTCPay Serverin [uusin versio](https://github.com/btcpayserver/btcpayserver/releases). Palvelimen päivittäminen voi ratkaista ongelman.


##### Palvelimen uudelleenkäynnistäminen


Palvelimen uudelleenkäynnistäminen on helppo tapa ratkaista monet yleisimmistä BTCPay-palvelimen ongelmista. Sinun on ehkä otettava SSH-yhteys palvelimeesi, jotta voit käynnistää sen uudelleen.


##### Palvelun uudelleenkäynnistäminen


BTCPay Serverin käyttöönotossa saattaa olla tarpeen käynnistää uudelleen vain tietty palvelu joidenkin ongelmien vuoksi, kuten letsencrypt-säiliön käynnistäminen uudelleen SSL-varmenteen uusimiseksi.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Käytä docker ps:ää löytääksesi sen palvelun nimen, jonka haluat käynnistää uudelleen.


#### Lokien läpikäynti


Lokit voivat tarjota tärkeää tietoa. Seuraavissa kappaleissa kuvaamme, miten saat lokitietoja BTCPayn eri osista.


##### BTCPay lokit


V1.0.3.8:sta lähtien voit helposti käyttää BTCPay-palvelimen lokeja etupäässä. Jos olet palvelimen ylläpitäjä, valitse Palvelimen asetukset > Lokit ja avaa lokitiedosto. Jos et tiedä, mitä tietty lokien virhe tarkoittaa, mainitse se vianmäärityksen yhteydessä.


Jos haluat yksityiskohtaisempia lokitietoja ja käytät Docker-käyttöönottoa, voit tarkastella tiettyjen Docker-säiliöiden lokitietoja komentorivillä. Katso nämä [ssh-ohjeet](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) VPS:llä toimivaan BTCPay-instanssiin.


Seuraavalla sivulla on yleinen luettelo BTCPay Serverissä käytetyistä konttien nimistä.


Suorita alla olevat komennot tulostaaksesi lokit säiliön nimen mukaan. Korvaa kontin nimi, jos haluat tarkastella muita konttien lokitietoja.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```


| Logs for     | Container Name                    |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Telakka


LND-lokeihin pääsee käsiksi muutamalla tavalla, kun käytät Dockeria. Kirjaudu ensin sisään pääkäyttäjänä:


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Vaihtoehtoisesti voit tulostaa lokit nopeasti käyttämällä säiliön tunnusta (tarvitaan vain ensimmäiset yksilölliset tunnuksen merkit, kuten kaksi vasemmanpuoleisinta merkkiä):


```bash
docker logs 'add your container ID'
```


Jos jostain syystä tarvitset lisää tukkeja, -


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


Näet jotain sellaista kuin


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


Jos haluat käyttää näiden lokien pakkaamattomia lokeja, tee `cat LND.log` tai jos haluat toisen, käytä `cat LND.log.15`.


Jos haluat käyttää pakattuja lokitietoja muodossa `.gzip`, käytä `gzip -d LND.log.16.gz` (tässä tapauksessa käytämme `LND.log.16.gz`). Tämän pitäisi antaa sinulle uusi tiedosto, jossa voit tehdä `cat LND.log.16`. Jos edellä mainittu ei toimi, sinun on ehkä asennettava gzip ensin komennolla `sudo apt-get install gzip`.


###### Lightning Network c-lightning - Telakka


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


Vaihtoehtoisesti voit käyttää tätä:


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Voit myös saada lokitiedot c-lightning CLI -komennolla.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Bitcoin-solmun lokit


bitcoind-säiliön [lokien tarkastelun](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) lisäksi voit myös käyttää mitä tahansa [bitcoin-cli-komentoja](https://developer.Bitcoin.org/reference/RPC/index.html)


[(avaa uuden ikkunan)](https://developer.Bitcoin.org/reference/RPC/index.html) saadaksesi tietoja Bitcoin-solmusta. BTCPay sisältää skriptin, jonka avulla voit kommunikoida Bitcoin-solmun kanssa helposti.


Hae btcpayserver-docker-kansion sisältä Blockchain-tiedot solmun avulla:


```bash
bitcoin-cli.sh getblockchaininfo
```


### Tiedostot


BTCPay-palvelimessa on paikallinen tiedostojärjestelmä, jonka avulla voit ladata myymälä- (tuote-) omaisuuseriä, logoja ja tuotemerkkejä suoraan palvelimelle. Palvelimen tiedostojärjestelmään pääsevät käsiksi vain palvelimen ylläpitäjät; myymälän omistajat voivat ladata logonsa tai brändinsä myymälätasolla.


Kun palvelimen ylläpitäjä on Tiedostotallennus-välilehdellä, on mahdollista ladata suoraan palvelimelle tai vaihtaa tiedoston tallennuspalvelun tarjoaja paikalliseen tiedostojärjestelmään tai Azure Blob Storageen.


![image](assets/en/091.webp)


![image](assets/en/092.webp)


### Taitojen yhteenveto


Tässä jaksossa opit seuraavat asiat:



- Kaupan ja palvelimen asetusten välinen ero, erityisesti käyttäjien, roolien ja sähköpostien osalta
- Aseta koko palvelimen kattavat käytännöt Lightning- tai Bitcoin Hot Wallet -käytölle ja -luonnille, uusien käyttäjien rekisteröinnille ja sähköposti-ilmoituksille.
- Miten lisätä mukautettuja teemoja (pelkkien vaaleiden ja tummien vaihtoehtojen sijaan) sekä luoda mukautettuja logoja?
- Suorita yksinkertaisia palvelimen ylläpitotehtäviä mukana toimitetun graafisen käyttöliittymän avulla
- Vianmääritysongelmat, mukaan lukien tietojen hakeminen mistä tahansa Docker-säiliöstä tai solmusta
- Hallitse tiedostojen tallennusta


### Tietojen arviointi


#### KA Käsitteellinen tarkastelu


Mitä eroa on palvelimen ja myymäläasetusten kautta määritetyillä rooleilla, ja mikä on mahdollista, että jompaa kumpaa käytetään enemmän kuin toista?


#### KA Käytännön katsaus


Kuvaile joitakin mahdollisia käyttötapauksia, jotka on otettu käyttöön Käytännöt-välilehdellä.


#### KA Käytännön katsaus


Kuvaile joitakin toimia, joita järjestelmänvalvoja voi tehdä rutiininomaisesti Ylläpito-välilehdellä.


## BTCPay-palvelin - Maksut


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


Invoice on asiakirja, jonka myyjä antaa ostajalle maksun perimiseksi.


BTCPay Serverissä Invoice edustaa asiakirjaa, joka on maksettava määritellyn ajan kuluessa kiinteällä Exchange-kurssilla. Laskuilla on voimassaolopäivämäärät, koska ne lukitsevat Exchange-kurssin tietylle aikavälille ja suojaavat vastaanottajaa hinnanvaihteluilta.


BTCPay Serverin ydin on kyky toimia Bitcoin Invoice-hallintajärjestelmänä. Invoice on olennainen työkalu vastaanotettujen maksujen seurantaan ja hallintaan.


Ellet käytä sisäänrakennettua [Wallet](https://docs.btcpayserver.org/Wallet/) maksujen vastaanottamiseen manuaalisesti, kaikki myymälän sisällä olevat maksut näkyvät Laskut-sivulla. Tällä sivulla maksut lajitellaan kumulatiivisesti päivämäärän mukaan, ja se toimii keskeisenä resurssina Invoice hallintaa ja maksujen vianmääritystä varten.


![image](assets/en/093.webp)


### Yleistä


#### Invoice:n tilat


Alla olevassa taulukossa luetellaan ja kuvataan BTCPayn Invoice-standarditilat sekä ehdotetut yleiset toimenpiteet. Toimenpiteet ovat vain suosituksia. Käyttäjien on itse määriteltävä omaan käyttötilanteeseensa ja liiketoimintaansa parhaiten sopiva toimintatapa.


| Invoice Status             | Description                                                                                                                             | Action                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New                        | Not paid, invoice timer still has not expired                                                                                           | None                                                                                                                        |
| New (paidPartial)          | Paid, not in full, invoice timer still has not expired                                                                                  | None                                                                                                                        |
| Expired                    | Not paid, invoice timer expired                                                                                                         | None                                                                                                                        |
| Expired (paidPartial) \*\* | Paid, not in full amount, and expired                                                                                                   | Contact buyer to arrange a refund or ask for them to pay their due. Optionally mark the invoice as settled or invalid           |
| Expired (paidLate)         | Paid, in full amount, after the invoice timer has expired                                                                               | Contact buyer to arrange a refund or process order if late confirmations are acceptable.                                    |
| Settled (paidOver)         | Paid more than the invoice amount, settled, received sufficient amount of confirmations                                                 | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing                 | Paid in full, but has not received sufficient amount of confirmations specified in the store settings                                   | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing (paidOver)      | Paid more than the invoice amount, not received sufficient amount of confirmations                                                      | Wait to be settled, then contact the  buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Settled                    | Paid, in full, received sufficient amount of confirmations in store                                                                     | Fulfil the order                                                                                                            |
| Settled (marked)           | Status was manually changed to settled from a processing or invalid status                                                             | Store admin has marked the payment as settled                                                                               |
| Invalid\*                  | Paid, but failed to receive sufficient amount of confirmations within the time specified in store settings                              | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |
| Invalid (marked)           | Status was manually changed to invalid from a settled or expired status                                                                 | Store admin has marked the payment as invalid                                                                               |
| Invalid (paidOver)         | Paid more than the invoice amount, but failed to receive sufficient amount of confirmations within the time specified in store settings | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |

#### Invoice tiedot


Invoice:n tietosivu sisältää kaikki Invoice:een liittyvät tiedot.


Invoice-tiedot luodaan automaattisesti Invoice-tilan, Exchange-asteen jne. perusteella. Tuotetiedot luodaan automaattisesti, jos Invoice on luotu tuotetietojen kanssa, esimerkiksi Point of Sale -sovelluksessa.


#### Invoice suodatus


Laskuja voidaan suodattaa hakupainikkeen vieressä olevien pikasuodattimien tai tarkennettujen suodattimien avulla, joita voi vaihtaa napsauttamalla yläreunassa olevaa (Ohje) -linkkiä. Käyttäjät voivat suodattaa laskuja myymälän, tilaustunnuksen, nimiketunnuksen, tilan tai päivämäärän mukaan.


#### Invoice vienti


BTCPay Server -laskut voidaan viedä CSV- tai JSON-muodossa. Lisätietoja Invoice viennistä ja kirjanpidosta.


#### Invoice:n palauttaminen


Jos jostain syystä haluat antaa palautuksen, voit helposti luoda palautuksen Invoice-näkymästä.


#### Laskujen arkistointi


Koska BTCPay Serverin Address uudelleenkäyttöä ei sallita, on tavallista, että kauppasi Invoice-sivulla näkyy paljon vanhentuneita laskuja. Voit piilottaa ne näkyvistäsi valitsemalla ne luettelosta ja merkitsemällä ne arkistoiduksi. Arkistoiduksi merkittyjä laskuja ei poisteta. BTCPay-palvelimesi havaitsee edelleen maksun arkistoidulle Invoice:lle (paidLate-tila). Voit tarkastella myymälän arkistoituja laskuja milloin tahansa valitsemalla arkistoidut laskut hakusuodattimen pudotusvalikosta.


#### Oletusvaluutta


Kaupan oletusvaluutta, joka asetettiin ohjatussa kaupan luomisessa.


#### Kuka tahansa voi luoda Invoice:n


Tämä vaihtoehto kannattaa ottaa käyttöön, jos haluat antaa ulkopuolisten luoda laskuja kaupassasi. Tämä vaihtoehto on hyödyllinen vain, jos käytät maksupainiketta tai jos laadit laskuja API:n tai kolmannen osapuolen HTML-sivuston kautta. PoS-sovellus on ennakkovaltuutettu, eikä tämän asetuksen ottamista käyttöön tarvita, jotta satunnainen vierailija voi avata kassakauppasi ja luoda Invoice-laskun.


#### Lisää lisämaksu (verkkomaksu) Invoice:ään



- Vain jos asiakas maksaa Invoice:stä useamman kuin yhden maksun
- Jokaisen maksun yhteydessä
- Älä koskaan lisää verkkomaksua


#### Invoice raukeaa, jos koko summaa ei ole maksettu ... pöytäkirjan jälkeen.


Invoice:n ajastin on oletusarvoisesti asetettu 15 minuuttiin. Ajastin toimii suojamekanismina volatiliteettia vastaan, sillä se lukitsee kryptovaluuttamäärän krypto-fiat-kurssien perusteella. Jos asiakas ei maksa Invoice-maksua määritellyn ajan kuluessa, Invoice katsotaan vanhentuneeksi. Invoice katsotaan "maksetuksi" heti, kun transaktio näkyy Blockchain:ssä (ilman vahvistuksia), ja se katsotaan "suoritetuksi", kun se saavuttaa kauppiaan määrittelemän vahvistusten määrän (yleensä 1-6). Ajastin on muokattavissa.


#### Pidä Invoice maksettuna, vaikka maksettu määrä olisi ..% odotettua pienempi.


Tilanteessa, jossa asiakas käyttää Exchange Wallet:ta maksaakseen suoraan Invoice:stä, Exchange ottaa pienen maksun. Tämä tarkoittaa, että tällaista Invoice:tä ei pidetä täysin valmiina. Invoice merkitään "maksettu osittain" Jos kauppias haluaa hyväksyä vajaasti maksetut laskut, voit asettaa prosenttimäärän tässä kohdassa


### Pyynnöt


Maksupyynnöt ovat ominaisuus, jonka avulla BTCPay-kaupan omistajat voivat luoda pitkäaikaisia laskuja. Varat maksetaan maksupyynnön mukaisesti käyttäen maksuhetkellä voimassa olevaa Exchange-kurssia. Näin käyttäjät voivat suorittaa maksuja haluamallaan tavalla ilman, että heidän tarvitsee neuvotella tai tarkistaa Exchange-kursseja kaupan omistajan kanssa maksuhetkellä.


Käyttäjät voivat maksaa pyynnöt osamaksuina. Maksupyyntö pysyy voimassa, kunnes se on maksettu kokonaan tai jos kaupan omistaja vaatii päättymisajan. Osoitteita ei koskaan käytetä uudelleen. Uusi Address luodaan joka kerta, kun käyttäjä klikkaa maksa-painiketta luodakseen maksupyynnöstä Invoice:n.


Kaupan omistajat voivat tulostaa maksupyyntöjä (tai viedä Invoice-tietoja) kirjanpitoa ja kirjanpitoa varten. BTCPay merkitsee laskut automaattisesti maksupyynnöiksi kauppasi Invoice-luettelossa.


#### Mukauta maksupyyntöjäsi



- Invoice Amount - Aseta pyydetty maksun määrä
- Nimellisarvo - Näytä pyydetty summa fiat- tai kryptovaluuttana
- Maksun määrä - Salli vain yksittäiset maksut tai osittaiset maksut
- Päättymisaika - Salli maksut tiettyyn päivämäärään asti tai ilman päättymispäivää
- Kuvaus - Tekstieditori, datataulukot, upota valokuvia ja videoita
- Ulkonäkö - Väri ja tyyli CSS-teemojen avulla


![image](assets/en/094.webp)


#### Luo maksupyyntö


Siirry vasemmanpuoleisessa valikossa kohtaan Maksupyyntö ja valitse "Luo maksupyyntö".


![image](assets/en/095.webp)


Anna pyynnön nimi, summa, näytön nimellisarvo, liittyvä myymälä, voimassaoloaika ja kuvaus (valinnainen)


Valitse vaihtoehto Salli maksunsaajan laatia laskuja omalla nimellisarvollaan, jos haluat sallia osamaksut.


Klikkaa Save & View (Tallenna & Näytä) tarkastellaksesi maksupyyntöäsi.


BTCPay luo URL-osoitteen maksupyyntöä varten. Jaa tämä URL-osoite nähdäksesi maksupyyntösi. Tarvitsetko useita samoja pyyntöjä? Voit monistaa maksupyyntöjä käyttämällä päävalikon Kloonaa-vaihtoehtoa.


![image](assets/en/096.webp)


**VAROITUS**


Maksupyynnöt ovat myymälästä riippuvaisia, mikä tarkoittaa, että jokainen maksupyyntö liitetään myymälään luomisen yhteydessä. Varmista, että Wallet on liitetty kauppaan, johon maksupyyntö kuuluu.


#### Maksettu pyyntö


Maksunsaaja ja maksupyynnön tekijä voivat tarkastella maksupyynnön tilaa sen jälkeen, kun maksu on lähetetty. Tilaksi tulee Selvitetty, jos maksu on vastaanotettu kokonaisuudessaan. Jos maksuja on suoritettu vain osittain, Amount Due näyttää jäljellä olevan saldon.


![image](assets/en/097.webp)


#### Mukauta maksupyyntöjä


Kuvauksen sisältöä voidaan muokata maksupyynnön tekstieditorilla. Molemmat vaihtoehdot ovat käytettävissä, jos haluat käyttää muita väriteemoja tai mukautettua CSS-muotoilua.


Ei-tekniset käyttäjät voivat käyttää [bootstrap-teemaa](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Muita mukautuksia voidaan tehdä antamalla ylimääräistä CSS-koodia, kuten alla on esitetty.


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### Vedä maksut


Perinteisesti vastaanottaja jakaa Bitcoin Address:nsä Bitcoin-maksua varten, ja lähettäjä lähettää myöhemmin rahaa tähän Address:ään. Tällaista järjestelmää kutsutaan Push-maksuksi, koska lähettäjä aloittaa maksun, kun vastaanottaja ei ehkä ole saatavilla, ja työntää maksun vastaanottajalle.


Entä jos rooli kuitenkin käännetään?


Entä jos sen sijaan, että lähettäjä työntää maksun, lähettäjä antaa vastaanottajan vetää maksun vastaanottajan kannalta sopivana ajankohtana? Tämä on Pull-maksun käsite. Tämä mahdollistaa useita uusia sovelluksia, kuten



- Tilauspalvelu (jossa tilaaja sallii palvelun vetää rahaa x ajan välein)
- Palautukset (kun kauppias antaa asiakkaan nostaa palautusrahan Wallet-järjestelmäänsä silloin, kun hän katsoo sen tarpeelliseksi)
- Aikaperusteinen laskutus freelancereille (kun palkkaava henkilö antaa freelancerin vetää rahaa Wallet:eensa sitä mukaa kuin aikaa raportoidaan)
- Mesenaatti (kun mesenaatti antaa vastaanottajan nostaa rahaa joka kuukausi jatkaakseen työnsä tukemista)
- Automaattinen myynti (Exchange:n asiakas voi antaa Exchange:n ottaa rahaa Wallet:stä myyntiin joka kuukausi automaattisesti)
- Saldonostojärjestelmä (kun suuren volyymin palvelu antaa käyttäjien pyytää nostoja saldostaan, palvelu voi sitten helposti erätä kaikki maksut monille käyttäjille tietyin väliajoin)


### Maksut


Maksutoiminto on sidottu [Pull Payments] (https://docs.btcpayserver.org/PullPayments/) -toimintoon. Tämän ominaisuuden avulla voit luoda maksuja BTCPayn sisällä. Tämän ominaisuuden avulla voit käsitellä pull-maksuja (palautuksia, palkanmaksuja tai nostoja).


#### Esimerkki 1: Palautus


Aloitetaan palautusta koskevasta esimerkistä. Asiakas on ostanut tuotteen kaupastasi, mutta valitettavasti hänen on palautettava se. Hän haluaa hyvityksen. BTCPayn sisällä voit luoda [Palautus](https://docs.btcpayserver.org/Refund/) ja antaa asiakkaalle linkin, jonka kautta hän voi lunastaa rahansa. Kun asiakas on antanut Address-tietonsa ja lunastanut varat, ne näkyvät Maksut-osiossa.


Sen ensimmäinen tila on Odottaa hyväksyntää. Myymälävirkailijat voivat tarkistaa, jos useampi on odottamassa, ja kun olet tehnyt valinnan, käytät Toiminnot-painiketta.


Toimintopainikkeen vaihtoehdot



- Hyväksy valitut maksut
- Hyväksy ja lähetä valitut maksut
- Peruuta valitut maksut


Seuraava vaihe on hyväksyä ja lähettää valitut maksut, koska haluamme palauttaa asiakkaalle rahat. Tarkista asiakkaan Address, josta näkyy summa ja se, haluammeko, että maksut vähennetään palautuksesta vai ei. Kun olet suorittanut tarkistukset, tapahtuman allekirjoittaminen on ainoa jäljellä oleva vaihe.


Asiakas päivitetään nyt Vaatimus-sivulle. Hän voi seurata tapahtumaa, koska hänelle annetaan linkki Block explorer:ään ja hänen tapahtumaansa. Kun maksutapahtuma on vahvistettu, sen tila muuttuu tilaksi "Completed".


#### Esimerkki 2: Palkka


Seuraavaksi käsitellään palkanmaksua, sillä sitä ohjataan myymälän sisältä eikä asiakkaan pyynnön mukaan. Peruskonsepti on sama; siinä hyödynnetään pull-maksuja. Mutta sen sijaan, että luomme palautuksen, teemme [Pull Payment] (https://docs.btcpayserver.org/PullPayments/).


Siirry BTCPay-palvelimesi Pull Payments -välilehdelle. Napsauta oikeassa yläkulmassa Create Pull Payment -painiketta.


Nyt olemme luomisessa Payout, anna sille nimi ja haluamasi määrä valitun valuutan. Täytä Kuvaus, jotta työntekijä tietää, mistä on kyse. Seuraava osa on samanlainen kuin palautukset. Työntekijä täyttää Kohde Address:n ja summan, jonka hän haluaa vaatia tästä Payoutista. Hän voi päättää tehdä siitä 2 erillistä korvausvaatimusta, eri osoitteisiin tai jopa osittain korvausvaatimuksen salaman aikana.


Jos useita maksuja on odottamassa, voit erottaa ne allekirjoitettaviksi ja lähetettäviksi. Kun maksut on allekirjoitettu, ne siirretään Käynnissä-välilehdelle ja näyttävät Tapahtuman. Kun verkko on hyväksynyt maksun, se siirtyy Valmis-välilehdelle. Valmis-välilehti on pelkästään historiallisia tarkoituksia varten. Siihen tallennetaan käsitellyt maksut ja siihen kuuluvat tapahtumat


### Vedä maksut


#### Konsepti


Kun lähettäjä määrittää Pull-maksun, hän voi määrittää useita ominaisuuksia:



- Pull request Nimi
- Rajamäärä
- Yksikkö (kuten BTC, SAT, USD)
- Maksutavat
  - BTC On-Chain
  - BTC off-chain
- Kuvaus
- Mukautettu CSS
- Loppupäivä (valinnainen Lightning Network BOLT11:lle)


Tämän jälkeen lähettäjä voi jakaa pull-maksun linkin avulla vastaanottajan kanssa, jolloin vastaanottaja voi luoda maksun. Vastaanottaja valitsee maksun:



- Mitä maksutapaa käyttää
- Minne rahat lähetetään


Kun maksu on luotu, se lasketaan mukaan kuluvan kauden vetomaksun rajaan. Tämän jälkeen lähettäjä hyväksyy maksun asettamalla maksun lähetysnopeuden ja jatkaa maksua.


Tarjoamme lähettäjälle helppokäyttöisen menetelmän useiden maksujen yhdistämiseen [BTCPay Internal Wallet](https://docs.btcpayserver.org/Wallet/).


#### Greenfield API


BTCPay Server tarjoaa sekä lähettäjälle että vastaanottajalle täydellisen API:n, joka on dokumentoitu instanssin `/docs`-sivulla. (tai dokumentointisivustolla https://docs.btcpayserver.org)


Koska sovellusliittymämme tarjoaa kaikki mahdollisuudet pull-maksuihin, lähettäjä voi automatisoida maksut omien tarpeidensa mukaan.


### Taitojen yhteenveto


Tässä jaksossa opit seuraavat asiat:



- Syvällinen ymmärrys BTCPay Serverin Invoice-tiloista ja niihin kohdistuvista toimista
- Mukauta ja hallitse pidennetyn käyttöiän Invoice-mekanismeja, joita kutsutaan pyynnöiksi.
- BTCPay Serverin ainutlaatuisen Pull Payment -ominaisuuden myötä avautuvat joustavat lisämaksumahdollisuudet erityisesti palautusten ja palkanmaksun käsittelyssä.


### Tietojen arviointi


#### KA Käsitteellinen tarkastelu


Mitä eroja on laskujen ja maksupyyntöjen välillä, ja mikä voisi olla hyvä syy käyttää jälkimmäisiä?


#### KA Käsitteellinen tarkastelu


Miten vetomaksut laajentavat sitä, mitä tyypillisesti voidaan tehdä On-Chain:ssä? Kuvaile joitakin käyttötapauksia, jotka ne mahdollistavat.


## BTCPay-palvelimen oletusliitännäiset


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Oletusliittimet ja -sovellukset


BTCPay-palvelimen mukana tulee vakiovarusteena liitännäisiä (sovelluksia), jotka voivat tehdä BTCPay-palvelimesta sähköisen kaupankäynnin maksuportin. Myyntipisteen, joukkorahoitusalustan ja helpon maksupainikkeen lisäyksillä BTCPay Serveristä tulee helposti käyttöönotettava ratkaisu.


### Myyntipiste


Yksi BTCPay-palvelimen vakiolaajennuksista on myyntipiste (Point of Sale, PoS). PoS-lisäosan avulla kaupan omistaja voi luoda verkkokaupan suoraan BTCPay Serveristä; kaupan omistaja ei tarvitse kolmannen osapuolen verkkokaupparatkaisuja verkkokaupan ylläpitämiseen. Verkkopohjaisen PoS-sovelluksen avulla käyttäjät, joilla on kivijalkamyymälöitä, voivat helposti hyväksyä Bitcoin:n suoraan Wallet:ään ilman maksuja tai kolmatta osapuolta. PoS voidaan helposti näyttää tableteilla tai muilla laitteilla, jotka tukevat verkkoselausta. Käyttäjät voivat helposti luoda aloitusnäytön pikakuvakkeen, jonka avulla he pääsevät nopeasti verkkosovellukseen.


#### Uuden myyntipisteen luominen


BTCPay Serverin avulla myymälän omistajat voivat luoda nopeasti myyntipisteen useilla eri ulkoasuilla. BTCPay Server ymmärtää, että kaikki myymälät eivät ole verkkokauppoja eivätkä kaikki myymälät ole baareja tai ravintoloita, ja se sisältää useita vakioasetuksia myyntipisteellesi.


Kun myymälän omistaja napsauttaa vasemmanpuoleisen valikkopalkin "Myyntipiste" -painiketta, BTCPay Server kysyy nyt nimeä; tämä nimi näkyy vasemmanpuoleisessa valikkopalkissa. Luo myyntipiste napsauttamalla Luo.


![image](assets/en/098.webp)


#### Päivitä äskettäin luotu myyntipiste


Kun olet luonut uuden myyntipisteen, voit päivittää myyntipisteesi ja lisätä tuotteita myymälääsi seuraavassa näytössä.


##### Sovelluksen nimi


Myyntipisteellesi tässä annettu nimi näkyy BTCPay-palvelimen päävalikossa.


##### Näytön otsikko


Yleisö näkee myymäläsi otsikon tai nimen, kun se vierailee siellä. BTCPay-palvelin antaa oletusarvoisesti kaupallesi nimen "Teekauppa" Korvaa tämä kaupan nimellä.


![image](assets/en/099.webp)


#### Valitse myyntipisteen tyyli


BTCPay-palvelin pystyy näyttämään myyntipisteensä useilla eri tavoilla.



- Tuoteluettelo
  - Myymälänäkymä, jossa asiakkaat voivat ostaa vain 1 tuotteen kerrallaan.
- Tuoteluettelo, jossa on ostoskori.
  - Myymälänäkymä, jossa asiakkaat voivat ostaa useita tuotteita kerralla ja saada ostoskorin yleiskatsauksen näytön oikealle puolelle.
- Vain näppäimistö
  - Ei tuoteluetteloa, vain näppäimistö suoraa laskutusta varten.
- Tulostusnäyttö (tulostettava tuoteluettelo QR:llä)
  - Jos et voi aina näyttää tuoteluetteloasi digitaalisesti, tarvitset "offline-ratkaisun" tuotteille; BTCPay Serverissä on tulostusnäyttö, joka toimii offline-kauppana.


![image](assets/en/100.webp)


#### Point Of Sale Style - Tuoteluettelo


![image](assets/en/101.webp)


#### Point Of Sale Style - Tuoteluettelo + Ostoskori


![image](assets/en/102.webp)


#### Point Of Sale Style - vain näppäimistö


![image](assets/en/103.webp)


#### Point Of Sale Style - Tulosta näyttö


![image](assets/en/104.webp)


#### Valuutta


Myymälän omistaja voi asettaa myyntipisteen valuutaksi eri valuutan kuin yleinen oletusvaluutta. Kaupan oletusvaluutta täyttää tämän kentän automaattisesti.


#### Kuvaus


Kerro maailmalle kaupastasi; mitä myyt ja kuinka paljon? Kaikki myymälääsi selittävät asiat tulevat tänne.


![image](assets/en/105.webp)


#### Tuotteet


Kun myyntipiste luodaan, tavallinen BTCPay-palvelin lisää kauppaan pari kohdetta viitteeksi. Napsauta minkä tahansa vakiokohteen Muokkaa-painiketta ymmärtääksesi paremmin kohteen kaikki mahdolliset vaihtoehdot.


Uuden tuotteen luominen myymälääsi koostuu seuraavista kentistä;



- Otsikko
- Hinta (kiinteä, vähimmäishinta tai mukautettu)
- Kuvan URL-osoite
- Kuvaus
- Inventaario
- ID
- Osta Button Text.
- Ota käyttöön/poista käytöstä


Kun myymälän omistaja on täyttänyt kaikki uudet tuotekentät, napsauta Tallenna, ja huomaat, että Myyntipisteen Tuotteet-osio täyttyy. Tallenna aina näytön oikeaan yläkulmaan, jotta myymälän omistajat eivät menetä edistymistään tuotteita lisätessään.


Myymälän omistajat voivat myös käyttää "Raw Editoria" tuotteidensa konfigurointiin. Raakaeditori edellyttää JSON-rakenteiden peruskäsitystä.


![image](assets/en/106.webp)


#### Kassa


BTCPay Server mahdollistaa pienen PoS-kohtaisen kassan mukauttamisen. Kaupan omistaja voi asettaa "Osta x:llä" -tekstin tai pyytää tiettyjä asiakastietoja lisäämällä ne lomakkeisiin.


#### Vinkkejä


Vain jotkin kaupat tarvitsevat myyntiä koskevan Tips-vaihtoehdon. Kaupan omistajat voivat kytkeä tämän päälle tai pois päältä myymälänsä kannalta sopivaksi katsomallaan tavalla. Jos myymälä käyttää vinkkejä päälle kytkettynä, myymälän omistaja voi asettaa kenttään haluamansa tekstin vinkkejä varten. BTCPay-palvelimen vinkit toimivat prosentuaalisen summan perusteella. Kaupan omistajat voivat lisätä useita prosenttilukuja pilkulla erotettuna.


#### Alennukset


Myymälän omistajana saatat haluta antaa asiakkaalle mukautetun alennuksen kassalla; Alennukset-vaihtoehto tulee saataville myymälän kassalla. Tätä on kuitenkin erittäin suositeltavaa välttää käyttämällä itsekassausjärjestelmiä.


#### Mukautetut maksut


Kun Mukautetut maksut -vaihtoehto on kytketty päälle, asiakas voi syöttää hinnan, joka on yhtä suuri tai suurempi kuin myymälän luoma alkuperäinen Invoice.


#### Lisävaihtoehdot


Kun olet määrittänyt kaiken myyntipisteesi, jäljellä on vielä joitakin lisävaihtoehtoja. Myymälän omistajat voivat helposti upottaa myyntipisteensä Iframen kautta tai upottaa maksupainikkeen, joka linkittää tiettyyn myymälän tuotteeseen. Juuri luodun PoS-myymälän tyylittelemiseksi omistajat voivat lisätä mukautetun CSS:n lisävaihtoehtojen alareunaan.


#### Poista tämä sovellus


Jos myymälän omistaja haluaa poistaa myyntipisteen kokonaan BTCPay-palvelimelta, myymälän omistajat voivat napsauttaa Poista tämä sovellus -painiketta myyntipistesovelluksen päivittämisen alareunassa, jolloin myyntipistesovellus tuhoutuu kokonaan. Kun napsautat "Poista tämä sovellus", BTCPay Server pyytää vahvistusta kirjoittamalla `DELETE` ja vahvistamalla napsauttamalla Poista-painiketta. Poistamisen jälkeen kaupan omistaja palaa BTCPay Serverin kojelautaan.


### BTCPay-palvelin - Joukkorahoitus


Myyntipisteen lisäosan lisäksi BTCPay Serverissä on mahdollisuus luoda joukkorahoitus. Aivan kuten muutkin joukkorahoitusalustat, myymälän omistajat voivat asettaa tavoitteen, luoda etuisuuksia panoksille ja mukauttaa sen omiin tarpeisiinsa.


#### Kuinka perustaa uusi joukkorahoitus


Napsauta Crowdfund-lisäosaa BTCPay-palvelimesi vasemmanpuoleisessa päävalikossa, Plugin-osion alapuolella. BTCPay Server pyytää nyt nimeä Crowdfundille; tämä nimi näkyy myös vasemmassa valikkopalkissa.


![image](assets/en/107.webp)


#### Päivitä äskettäin luotu myyntipiste


Kun sovellukselle on annettu nimi, seuraavassa näytössä sovellus päivitetään kontekstin saamiseksi.


#### Sovelluksen nimi


Joukkorahastollesi annettu nimi näkyy BTCPay Serverin päävalikossa.


#### Näytön otsikko


Otsikko on annettu joukkorahoitukselle yleisölle.


#### Tagline


Anna joukkorahoitukselle yksiviivainen sana, jolla tunnistat, mistä varainkeruussa on kyse.


![image](assets/en/108.webp)


#### Esitetyn kuvan URL-osoite


Jokaisella joukkorahoituksella on pääkuvansa, yksi banneri, jonka tunnistat suoraan. Tämä kuva voidaan tallentaa palvelimellesi, jos sinulla on hallinnointioikeudet. Ylläpitäjät voivat ladata kuvan BTCPay-palvelimen asetuksista - Tiedostot. Kun olet myymälän omistaja, kuva on ladattava verkkoon kolmannen osapuolen palvelimen kautta (esimerkiksi Imgur).


#### Tee joukkorahoitus julkiseksi


Tämä kytkin tekee joukkorahoituksestasi julkista ja siten näkyvää ulkomaailmalle. Jos haluat testata tai nähdä, onko teemaa sovellettu oikein, pidä tämä pois päältä joukkorahoituksen rakentamisen ajan.


#### Kuvaus


Kerro maailmalle joukkorahoituksestasi. Mitä varten keräät varoja? Kaikki joukkorahoitustasi selittävät asiat tulevat tänne.


![image](assets/en/109.webp)


#### Joukkorahoituksen tavoite


Aseta tavoite sille, kuinka paljon varainkeräyksen tulisi tuottaa projektille, ja määritä, missä valuutassa tavoite tulisi ilmaista. Varmista, että jos tavoitteesi asetetaan päivämäärien välille, sisällytä nämä tavoite- ja päättymispäivät joukkorahoituksen kohdasta Tavoitteet.


![image](assets/en/110.webp)


#### Etuudet


Etuisuudet voivat parantaa joukkorahoituspyrkimyksiäsi merkittävästi. Tämä johtuu siitä, että edut antavat ihmisille mahdollisuuden osallistua kampanjaasi. Ne hyödyntävät sekä itsekkäitä että hyväntahtoisia motiiveja. Ja niiden avulla pääset käsiksi tukijoittesi rahankäyttöön, etkä vain heidän hyväntekeväisyyskukkaroonsa - voit arvata, kumpi on merkittävämpi.


Uuden etuuden luominen koostuu seuraavista kentistä.



- Otsikko
- Hinta (kiinteä, vähimmäishinta tai mukautettu)
- Kuvan URL-osoite
- Kuvaus
- Inventaario
- ID
- Osta Button Text.
- Ota käyttöön/poista käytöstä


Kun myymälän omistaja on täyttänyt kaikki uuden etuuden kentät, napsauta Tallenna, ja huomaat, että Joukkorahoituksen etuudet-osiossa on nyt kaikki kentät täytetty.


![image](assets/en/111.webp)


### BTCPay-palvelin - myyntipiste


#### Maksut


Kaupan omistajat voivat valita, miten edut näytetään, miten ne lajitellaan tai jopa asettaa ne paremmuusjärjestykseen suhteessa muihin etuuksiin. Kun joukkorahoitustavoitteet on saavutettu, myymälän omistajat saattavat kuitenkin haluta lopettaa lahjoitusten virtaamisen tähän varainkeruuseen. Siksi hän voi kytkeä päälle "Älä salli lisämaksuja tavoitteen saavuttamisen jälkeen". Tämä estää Crowdfundia vastaanottamasta lahjoituksia.


##### Joukkorahoituskäyttäytyminen


Crowdfundin standardi laskee tavoitteeseen vain Crowdfundilla luodut laskut. Saattaa kuitenkin olla tapauksia, joissa kaupan omistaja haluaa, että kaikki kyseisessä kaupassa tehdyt laskut lasketaan mukaan crowdfundiin.


#### Muita vaihtoehtoja räätälöintiä varten


BTCpay Server tarjoaa pari ylimääräistä mukautusta. Lisää ääniä, animaatioita tai jopa keskusteluketjuja joukkorahoitukseen. Kaupan omistajat voivat myös muokata Crowdfundin ulkoasua syöttämällä oman mukautetun CSS:n.


#### Poista tämä sovellus


Jos myymälän omistaja haluaa poistaa joukkorahoituksen kokonaan BTCPay-palvelimelta, hän voi klikata joukkorahoituksen päivittämisen alareunassa "Poista tämä sovellus" -painiketta poistaakseen joukkorahoitussovelluksensa kokonaan. Kun napsautat "Poista tämä sovellus", BTCPay Server pyytää vahvistusta kirjoittamalla `DELETE` ja vahvistamalla napsauttamalla Poista-painiketta. Poistamisen jälkeen kaupan omistaja palaa BTCPay Serverin kojelautaan.


### BTCPay-palvelin - Maksa-painike


Helposti upotettavan HTML-muotoisen ja helposti muokattavan maksupainikkeen avulla myymälän omistajat voivat vastaanottaa vinkkejä ja lahjoituksia. BTCPay Serverin vasemmassa valikkopalkissa, Plugins-osion alapuolella, myymälän omistajat voivat napsauttaa "Pay Button" (maksupainike) ja napsauttaa Enable (Ota käyttöön) luodaksesi maksupainikkeen.


#### Yleiset asetukset


Maksupainikkeen yleisissä asetuksissa kaupan omistajat voivat määrittää seuraavat asetukset



- Vakiohinta
- Oletusvaluutta
- Oletusmaksutapa
  - Käytä myymälän oletusarvoa
  - BTC On-Chain
  - BTC off-chain (salama)
  - BTC off-chain (LNURL-maksu)
- Kassan kuvaus
- Tilaus ID


#### Näytön vaihtoehdot


BTCPay Serverin Maksa-painike voidaan määrittää eri tyyleihin sopivaksi. Painikkeilla voi olla kiinteä tai mukautettu summa, joka näytetään joko liukusäätimellä tai plus- ja miinusvalitsimilla.


#### Käytä modaalia


Luodessaan maksupainiketta kaupan omistajat voivat valita sen käyttäytymisen, kun asiakas napsauttaa sitä, ja näyttää sen modaalissa tai uutena sivuna.


**!?Huomautus!?**


Varoitus: Maksu-painiketta tulee käyttää vain juomarahojen ja lahjoitusten maksamiseen


Maksupainikkeen käyttäminen verkkokauppaintegraatioissa ei ole suositeltavaa, koska käyttäjä voi muuttaa tilaukseen liittyviä tietoja. Verkkokauppaa varten kannattaa käyttää Greenfield API:ta. Jos tämä kauppa käsittelee kaupallisia tapahtumia, suosittelemme luomaan erillisen kaupan ennen maksupainikkeen käyttöä.


#### Mukauta maksupainikkeen tekstiä


Oletusarvoisesti BTCPay-palvelimen maksupainikkeessa lukee "Pay With BTCPay". Kaupan omistajat voivat asettaa tämän tekstin haluamakseen ja vaihtaa BTCPay Serverin logon omakseen. Aseta teksti käyttämällä "Pay Button Text" -kohtaa ja liitä kuvan URL-osoite "Pay Button Image URL" -kohdan alle.


##### Kuvan koko


Painikkeessa olevan kuvan koon voi asettaa vain kolmeen oletusarvoon.



- 146x40px
- 168x46px
- 209x57px


#### Painikkeen tyyppi


BTCPay-palvelin tuntee kolme tilaa maksupainikkeelle.



- Kiinteä määrä
  - Edellinen asetettu hinta on painikkeen yleisissä asetuksissa.
- Mukautettu määrä
  - BTCPay-palvelimen Maksa-painikkeessa on +- ja --vaihtimet mukautetun hinnan asettamiseksi.
  - Kun käytät mukautettua summaa, BTCPay-palvelin pyytää Min- ja Max-arvoja sekä sitä, kuinka asteittain summan tulisi kasvaa.
  - Painikkeet voidaan asettaa "Käytä yksinkertaista syöttötyyliä ".Tämä poistaa +/- kytkimet.
  - Sovita painike riviin, jolloin painike ja vaihtovalikot näkyvät rivissä.
- Slider
  - Samanlainen kuin mukautettu määrä, mutta se on visuaalisesti erilainen, koska siinä on liukusäädin +/- kytkimien sijasta.
  - Kun käytät liukusäädintä, BTCPay-palvelin pyytää Min- ja Max-arvoja sekä sitä, kuinka asteittain sen tulisi kasvaa.


**!?Huomautus!?**


Maksupainike voidaan poistaa varoituksen kuvauksen yläosasta.


#### Maksuilmoitukset


Palvelimen IPN (Instant Payment Notification) on suunniteltu webhookeja varten, ja siihen voidaan määrittää URL-osoite oston jälkeisiä tietoja varten.


#### Sähköposti-ilmoitukset


Aina kun maksu on suoritettu, BTCPay-palvelin voi ilmoittaa siitä kaupan omistajalle.


#### Selaimen uudelleenohjaus


Kun asiakas suorittaa ostoksen, hänet ohjataan tähän linkkiin, jos kaupan omistaja on sen asettanut.


#### Lisäasetukset maksupainikkeelle


Määritä kyselymerkkijonon lisäparametrit, jotka liitetään kassasivulle, kun Invoice on luotu. Esimerkiksi `lang=da-DK` lataisi kassasivun oletusarvoisesti tanskaksi.


#### Sovelluksen käyttäminen päätepisteenä


Voit linkittää maksupainikkeen suoraan johonkin aiemmin käyttämääsi PoS- tai Crowdfund-sovellukseen.


Kaupan omistajat voivat napsauttaa pudotusvalikkoa ja valita haluamansa sovelluksen; kun sovellus on valittu, kaupan omistaja voi lisätä linkitettävän tuotteen.


#### Generoitu koodi


Koska BTCPay Serverin maksupainike on helposti upotettavissa oleva HTML-muoto, BTCPay Server näyttää alareunassa luodun koodin, jonka voit kopioida verkkosivustolle maksupainikkeen määrittämisen jälkeen.


Kaupan omistajat voivat kopioida luodun koodin verkkosivustolleen, ja BTCPay-palvelimen maksupainike on suoraan aktiivinen heidän verkkosivustollaan.


#### Maksuilmoitukset


Palvelimen IPN (Instant Payment Notification) on suunniteltu webhookeja varten, ja siihen voidaan määrittää URL-osoite ostotietojen lähettämistä varten.


#### Sähköposti-ilmoitukset


Aina kun maksu suoritetaan, BTCPay-palvelin voi ilmoittaa siitä kaupan omistajalle.


#### Selaimen uudelleenohjaus


Kun asiakas suorittaa ostoksen, hänet ohjataan tähän linkkiin, jos kaupan omistaja on sen asettanut.


#### Lisäasetukset maksupainikkeelle


Määritä kyselymerkkijonon lisäparametrit, jotka liitetään kassasivulle, kun Invoice on luotu. Esimerkiksi `lang=da-DK` lataisi kassasivun oletusarvoisesti tanskaksi.


#### Sovelluksen käyttäminen päätepisteenä


Voit linkittää maksupainikkeen suoraan johonkin aiemmin käyttämääsi PoS- tai Crowdfund-sovellukseen. Kaupan omistajat voivat napsauttaa pudotusvalikkoa ja valita haluamansa sovelluksen. Kun sovellus on valittu, myymälän omistaja voi lisätä kohteen, joka on linkitettävä.


#### Generoitu koodi


Koska BTCPay Serverin maksupainike on helposti upotettavissa oleva HTML-muoto, BTCPay Server näyttää alareunassa luodun koodin, jonka voit kopioida verkkosivustolle maksupainikkeen määrittämisen jälkeen. Kaupan omistajat voivat kopioida luodun koodin verkkosivustolleen, ja BTCPay Serverin maksupainike on suoraan aktiivinen heidän verkkosivustollaan.


### Taitojen yhteenveto


Tässä jaksossa opit:



- Kuinka käyttää BTCPay Serverin integroitua PoS-lisäosaa mukautetun myymälän luomiseen helposti?
- Kuinka käyttää BTCPay Serverin integroitua Crowdfund-liitännäistä, jotta voit luoda mukautetun crowdfund-sovelluksen helposti?
- Koodin luominen mukautettua maksupainiketta varten Pay Button -lisäosan avulla


### Tietojen arviointi


#### KA arvostelu


Mitkä ovat BTCPay Serverin kolme sisäänrakennettua lisäosaa? Kuvaile muutamalla sanalla, miten kutakin voidaan käyttää.


# BTCPay-palvelimen määrittäminen


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## Perusymmärrys BTCPay-palvelimen asentamisesta LunaNode-ympäristöön


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### BTCPay-palvelimen asentaminen isännöidylle ympäristölle (LunaNode)


Nämä vaiheet tarjoavat kaikki tarvittavat tiedot BTCPay-palvelimen käytön aloittamiseksi LunaNodella. Ohjelmiston käyttöönottoon on monia vaihtoehtoja.

Löydät kaikki BTCPay-palvelimen tiedot osoitteesta https://docs.btcpayserver.org.


#### Mistä aloitamme?


Tässä osassa tutustut LunaNodeen hosting-palveluntarjoajana, opit BTCPay-palvelimen käytön ensimmäiset vaiheet ja opit käyttämään Lightning Network:ää. Kun olemme käyneet läpi kaikki vaiheet, voit ylläpitää verkkokauppaa tai joukkorahoitusalustaa, joka hyväksyy Bitcoin:n!


Tämä on yksi monista tavoista ottaa BTCPay Server käyttöön. Lue lisätietoja dokumentaatiostamme.


https://docs.btcpayserver.org.


### BTCPay-palvelin - LunaNoden käyttöönotto


#### LunaNoden käyttöönotto


Mene ensin LunaNode.com-sivustolle, jossa luomme uuden tilin. Napsauta oikealla ylhäällä olevaa Sign Up (Rekisteröidy) -painiketta tai käytä kotisivulla olevaa Get Started (Aloita) -ohjattua toimintoa.


![image](assets/en/112.webp)


Kun olet luonut uuden tilin, LunaNode lähettää vahvistussähköpostin. Kun olet vahvistanut tilin, verrattuna Voltageen, sinulle esitetään välittömästi mahdollisuus täydentää tilisi saldoa. Tämä saldo on tarpeen palvelintilan ja hosting-kustannusten kattamiseksi.


![image](assets/en/113.webp)


#### Lisää luottoa LunaNode-tilillesi


Kun olet napsauttanut "Talleta luottoa", voit määrittää, kuinka paljon haluat ladata tilillesi ja miten haluat maksaa sen. LunaNode ja BTCPay Server maksavat 10-20 dollaria kuukaudessa.

Voltage.cloudiin verrattuna saat täyden pääsyn virtuaaliseen yksityispalvelimeesi (VPS), jolloin voit hallita palvelintasi paremmin. Kun olet luonut uuden tilisi, LunaNode lähettää vahvistussähköpostin.

Kun olet vahvistanut tilisi, sinulle tarjotaan heti mahdollisuus täydentää tilisi saldoa Voltageen verrattuna. Tämä saldo on tarpeen palvelintilan ja hosting-kustannusten kattamiseksi.


#### Miten uusi palvelin otetaan käyttöön?


Tässä oppaassa käymme läpi asennusprosessin luomalla API-avaimet ja käyttämällä LunaNoden kehittämää BTCPay Server -käynnistysohjelmaa.


Klikkaa LunaNode-kojelaudassa oikeassa yläkulmassa API. Tämä avaa uuden sivun. Meidän on vain määritettävä API-avaimelle nimi. LunaNode huolehtii muusta, eikä sitä käsitellä tässä oppaassa. Napsauta Create API Credential -painiketta.

Kun olet luonut API-tunnukset, saat pitkän kirjain- ja merkkijonon. Tämä on API-avaimesi.


![image](assets/en/114.webp)


#### Miten uusi palvelin otetaan käyttöön?


Näissä tunnuksissa on kaksi osaa, API-avain ja API-tunnus; tarvitsemme molemmat. Ennen kuin siirrytään seuraavaan vaiheeseen, avataan selaimessa toinen välilehti ja siirrytään osoitteeseen https://launchbtcpay.lunanode.com/


Tässä sinua pyydetään antamaan API-avaimesi ja API-tunnuksesi. Tämän tarkoituksena on kertoa, että sinä olet se, joka on tarjonnut tämän uuden palvelimen. API-avaimen pitäisi olla edelleen auki edellisessä välilehdessäsi; jos selaat alla olevaa taulukkoa alaspäin, löydät API-tunnuksen.


Voit palata käynnistimen sivulle, täyttää kentät API-avaimellasi ja tunnuksellasi ja napsauttaa Jatka.


![image](assets/en/115.webp)


Seuraavassa vaiheessa voit antaa verkkotunnuksen. Jos omistat jo verkkotunnuksen ja haluat käyttää sitä BTCPay-palvelimessa, varmista, että lisäät myös DNS-tietueen (nimeltään `A`-tietue) verkkotunnuksellesi. Jos et omista verkkotunnusta, käytä sen sijaan LunaNoden tarjoamaa verkkotunnusta (voit muuttaa tämän myöhemmin BTCPay Server -asetuksissa) ja napsauta Jatka.


Lue lisää BTCPay-palvelimen DNS-tietueen asettamisesta tai muuttamisesta; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### Käynnistä BTCPay-palvelin LunaNodessa


Kun olemme suorittaneet edellä mainitut vaiheet, voimme asettaa kaikki asetukset uudelle palvelimellemme. Tässä valitsemme tuetuksi valuutaksi Bitcoin (BTC). Voimme myös asettaa sähköpostin, jolla saamme ilmoituksia salausvarmenteiden uusimisesta, mikä on valinnaista.


Tämän oppaan tarkoituksena on määrittää Mainnet-ympäristö (todellinen Bitcoin); LunaNode antaa kuitenkin myös mahdollisuuden määrittää sen Testnet- tai Regtest-ympäristöksi kehitystarkoituksia varten. Jätämme sen Mainnet-vaihtoehdon tähän oppaaseen.


Voit valita Lightning-toteutuksen. LunaNode tarjoaa kaksi eri toteutusta, LND ja Core Lightning. Tässä oppaassa käytämme LND:tä. Molemmissa toteutuksissa on vain vähän mutta todellisia eroja; jos haluat lisätietoja, suosittelemme lukemaan laajan dokumentaation: https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/116.webp)


LunaNode tarjoaa useita virtuaalikonepaketteja (VM). Ne eroavat toisistaan hintaluokan ja palvelinmäärittelyjen suhteen. Tähän oppaaseen riittää m2-suunnitelma; jos olet kuitenkin valinnut valuutaksi muutakin kuin Bitcoin:n, harkitse vähintään m4-suunnitelmaa.


Nopeuta Blockchain:n alkuperäistä synkronointia; tämä on valinnainen ja riippuu tarpeistasi. On olemassa edistyneempiä vaihtoehtoja, kuten Lightning Aliaksen asettaminen, tiettyyn GitHub-julkaisuun osoittaminen tai SSH-avaimien asettaminen; mitään näistä ei käsitellä tässä oppaassa.


Kun olet täyttänyt lomakkeen, sinun on klikattava Launch VM, ja Lunanode alkaa luoda uutta VM:ääsi, johon on asennettu BTCPay Server. Tämä prosessi kestää muutaman minuutin; kun palvelimesi on valmis, LunaNode antaa sinulle linkin uuteen BTCPay Serveriin.


Luomisprosessin jälkeen napsauta BTCPay-palvelimen linkkiä; tässä sinua pyydetään luomaan järjestelmänvalvojan tili.


![image](assets/en/117.webp)


### Taitojen yhteenveto


Tässä jaksossa opit:



- Tilin luominen ja rahoittaminen LunaNodessa
- BTCPay Server Launcherin käyttäminen oman palvelimen luomiseen


### Tietojen arviointi


#### KA Käsitteellinen tarkastelu


Kuvaile joitakin eroja BTCPay Server -palvelimen käyttämisen välillä VPS:llä ja tilin luomisen välillä isännöidyllä palvelimella.


## BTCPay Serverin asentaminen Voltage-ympäristöön


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


Tutustut Voltage.cloudiin hosting-palveluntarjoajana, opit BTCPay-palvelimen käytön ensimmäiset vaiheet ja Lightning Network:n käytön. Kun olemme käyneet läpi kaikki vaiheet, voit ylläpitää verkkokauppaa tai joukkorahoitusalustaa, joka hyväksyy Bitcoin:n!


Tämä on yksi monista tavoista ottaa BTCPay Server käyttöön. Lue lisätietoja dokumentaatiostamme.

https://docs.btcpayserver.org.


### BTCPay-palvelin - Voltage.cloud käyttöönotto


Mene ensin Voltage.cloud-sivustolle ja rekisteröi uusi tili. Kun luot tilin, voit rekisteröityä 7 päivän ilmaiseen kokeilujaksoon. Napsauta joko oikealla ylhäällä olevaa Sign Up (Rekisteröidy) -painiketta tai käytä heidän kotisivullaan olevaa "Kokeile ilmaista 7 päivän kokeilujaksoa" -painiketta.


![image](assets/en/118.webp)


Kun olet tehnyt tilin, napsauta kojelaudan `NODES`-painiketta. Kun olemme valinneet Solmut ja luoneet uuden solmun, meille näytetään mahdolliset solmun jännitetarjoukset. Koska tämä opas kattaa myös Lightning Network:n, Voltagessa meidän on ensin valittava Lightning-toteutuksemme ennen BTCPay-palvelimen luomista. Klikkaa LightningNode.


![image](assets/en/119.webp)


Tässä sinun on valittava, millaisen Lightning-solmun haluat. Voltage on erilaisia vaihtoehtoja valaistusasetuksiasi varten. Tämä on erilaista, kun otat käyttöön esimerkiksi LunaNoden kanssa. Tämän oppaan tarkoitukseen riittää Lite Node. Lue lisää eroista Voltage.cloudista.


![image](assets/en/120.webp)


Anna solmulle nimi, aseta salasana ja suojaa salasana. Jos salasana katoaa, menetät pääsyn varmuuskopioihisi, eikä Voltage voi palauttaa sitä. Luo solmu, ja Voltage näyttää edistymisen. Voltage on luonut Lightning-solmusi. Voimme nyt luoda BTCPay-palvelininstanssin ja käyttää suoraan Lightning Network:ta.


Napsauta kojelaudan vasemmassa yläkulmassa olevaa Nodes (Solmut) -painiketta. Täällä voit määrittää BTCPay Server -instanssisi seuraavan osan. Napsauta "create new" (luo uusi), kun olet solmujen yleiskatsauksessa. Saat samanlaisen näytön kuin aiemmin. Nyt valitsemme Lightning Node -solmun sijaan BTCPay Serverin.


Voltage näyttää BTCPay-palvelimesi maantieteellisen sijainnin, joka sijaitsee Yhdysvaltain länsiosassa. Täältä näet myös palvelimen isännöintikustannukset. Napsauta Luo ja anna BTCPay-palvelimelle nimi. Ota Lightning käyttöön ja Voltage näyttää sinulle edellisessä vaiheessa luodun Lightning-solmun. Napsauta Create, ja Voltage luo BTCPay Server -instanssin.


![image](assets/en/121.webp)


Kun olet painanut create, Voltage näyttää sinulle oletuskäyttäjätunnuksen ja salasanan. Nämä ovat samanlaiset kuin aiemmin Voltagessa asettamasi salasana. Napsauta Kirjaudu tilille -painiketta, jolloin sinut ohjataan BTCPay-palvelimelle.


Tervetuloa uuteen BTCPay-palvelimen instanssiin. Koska olemme jo ottaneet Lightningin käyttöön luomisprosessin aikana, Lightning on jo käytössäsi!


### Taitojen yhteenveto


Tässä luvussa opit:



- Tilin luominen Voltage.cloudissa
- Vaiheet BTCPay-palvelimen käyttämiseksi yhdessä Lightning-solmun kanssa tililläsi


### Tietojen arviointi


#### KA Käsitteellinen tarkastelu


Mitkä ovat keskeiset erot Voltage- ja LunaNode-asetusten välillä?


## BTCPay-palvelimen asentaminen Umbrel-solmuun


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


Näiden vaiheiden päätteeksi voit hyväksyä salamamaksuja BTCPay-kauppaan paikallisessa verkossa. Tätä prosessia sovelletaan myös, jos ylläpidät sateenvarjosolmua ravintolassa tai yrityksessä. Jos haluat liittää tämän kaupan julkiseen verkkosivustoon, noudata harjoitusta Edistyneet, jotta voit paljastaa umbrel-solmusi yleisölle.


https://umbrel.com/


![image](assets/en/122.webp)


### BTCPay-palvelin - Umbrelin käyttöönotto


Kun Umbrel-solmusi on täysin synkronoitu Bitcoin Blockchain:n kanssa, siirry Umbrelin sovelluskauppaan ja etsi BTCPay-palvelin sovellusten alta.


![image](assets/en/123.webp)


Napsauta BTCPay-palvelinta nähdäksesi sovelluksen tiedot. Kun BTCPay Serverin tiedot ovat avoinna, oikeassa alakulmassa näkyvät vaatimukset, joiden mukaan sovellus toimii oikein. Sen mukaan se vaatii Bitcoin:n ja Lightning-solmun. Jos et ole asentanut Lightning-solmua Umbreliin, napsauta Asenna. Tämä prosessi voi kestää muutaman minuutin.


![image](assets/en/124.webp)


Kun olet asentanut Lightning Node:


1. Napsauta Avaa sovelluksen tiedoissa tai Sovellus Umbrelsin kojelaudassa.

2. Napsauta setup a new node; sinulle näytetään 24 sanaa salamasolmun palautusta varten.

3. Kirjoita nämä ylös.


![image](assets/en/125.webp)


Umbrel pyytää vahvistamaan juuri kirjoitetut sanat. Kun Lightning-solmu on perustettu, palaa Umbrelin sovelluskauppaan ja etsi BTCPay Server. Napsauta asennuspainiketta, ja Umbrel näyttää, onko tarvittavat komponentit asennettu ja että BTCPay Server vaatii pääsyn näihin komponentteihin. Asennuksen jälkeen napsauta Avaa oikeassa yläkulmassa App details -osassa tai avaa BTCPay Server Umbrelin kojelaudan kautta.


Umbrel pyytää vahvistamaan juuri kirjoitetut sanat.


![image](assets/en/126.webp)


**!?Huomautus!?**


Varmista, että säilytät ne turvallisessa paikassa, kuten aiemmin opit avainten säilytyksen yhteydessä.


Kun Lightning-solmu on perustettu, palaa Umbrel App Storeen ja etsi BTCPay Server. Napsauta asennuspainiketta, ja Umbrel näyttää, onko tarvittavat komponentit asennettu ja että BTCPay Server vaatii pääsyn näihin komponentteihin.


![image](assets/en/127.webp)


Asennuksen jälkeen napsauta Avaa sovelluksen tietojen oikeassa yläkulmassa tai avaa BTCPay Server Umbrels-kojelaudan kautta.


![image](assets/en/128.webp)


### Taitojen yhteenveto


Tässä jaksossa opit:



- Vaiheet BTCPay-palvelimen asentamiseksi Lightning-toiminnolla Umbrel-solmuun


### Tietojen arviointi


#### KA Käsitteellinen tarkastelu


Miten Umbrelin asetukset eroavat kahdesta edellisestä isännöintivaihtoehdosta?


# Viimeinen jakso


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Arvostelut & arvostelut

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Kurssin johtopäätökset


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>