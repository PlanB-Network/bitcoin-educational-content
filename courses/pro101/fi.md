---
name: Bitcoinin kehityksen perusteet
goal: Hanki kaikki perusteet Bitcoin:n kehittämisen aloittamiseksi
objectives:
- Ymmärtää Bitcoinin peruskäsitteet ja taustalla oleva teknologia
- Hankkia käytännön taitoja Bitcoin-turvallisuudessa, ohjelmistokehityksessä ja verkon hallinnossa
- Kehittää Lightning Networkin ja siihen liittyvien protokollien hallinta
- Löytää kryptografiset periaatteet, jotka tukevat transaktioturvallisuutta ja verkon eheyttä
---
# Matka CUBO+ kehityskursseihin Bitcoinille!

Mitä tarvitaan Bitcoinin päälle rakentamiseen? Tämä 20 tunnin kurssi vie sinut Bitcoinin ja Lightning Networkin pinnan alle, tutkien protokollia, jotka voimistavat maailman kestävintä rahoitusinfrastruktuuria. Olitpa sitten kiinnostunut osallistumaan avoimen lähdekoodin projekteihin tai rakentamaan seuraavan sukupolven Bitcoin-sovelluksia, saat teknisen syvyyden, jota tarvitset työskennelläksesi luottavaisesti tässä ekosysteemissä.

Tallennettu CUBO+ 2023 bootcampin aikana El Salvadorissa, tämä kurssi kokoaa yhteen johtavien Bitcoin-kehittäjien ja kouluttajien näkökulmat, jotka ovat muovanneet teknologiaa. Paras osa? Se on täysin ilmainen, mahdollistettu Fulgure Venturen, Bitcoin Officen ja DecouvreBitcoinin toimesta. Jos olet ollut utelias siitä, miten Bitcoin todella toimii protokollatasolla, tämä on tilaisuutesi selvittää se.
+++
# Johdanto ja valmistavat kurssit


<partId>43a835de-c4e7-542b-9d1a-c92f049e88e6</partId>


## Johdatus CUBO+-kursseihin


<chapterId>dcf2d37e-b32a-5eb8-aaa3-41ac92475ba9</chapterId>


:::video id=9b6aa5cf-245e-4a66-b3b8-c4860ab51e90:::

Filippo ja Mario esittelevät CUBO+ 2023:n ja luovat pohjan tulevalle kattavalle oppimismatkalle. He keskustelevat kurssien rakenteesta, oppimistuloksista ja siitä, miten ne antavat opiskelijoille valmiuksia Bitcoin-kehitysalalla.


### Tavoitteet


Kurssin tavoitteena on antaa osallistujille syvällinen ymmärrys Bitcoin:n perusperiaatteista, käytännön kehitystaidot sekä kyky liikkua Bitcoin-ekosysteemissä ja osallistua siihen tehokkaasti. Teoriatiedon ja käytännön harjoitusten yhdistelmän avulla opiskelijat hallitsevat Bitcoin:n tietoturvan perusasiat, sen ohjelmistopinon hienoudet ja sen hallintamekanismit.


### Edellytykset


Osallistujien odotetaan tuovan mukanaan vahvaa uteliaisuutta, innokkuutta oppia ammatillisella tasolla ja jonkin verran perustietoa kehittämisestä. Vaikka yksityiskohtaista Bitcoin-taustaa ei vaadita, koodauksen periaatteiden perusymmärrys ja avoimuus monimutkaisten teknisten käsitteiden käsittelyyn ovat välttämättömiä, jotta kiihdyttämöstä voi ottaa kaiken hyödyn irti.


#### Työkalut


Kurssin aikana osallistujat hyödyntävät keskeisiä työkaluja, jotka auttavat heitä ymmärtämään ja tehostavat heidän oppimiskokemustaan. Linuxin, komentorivin Interface, GitHubin ja Dockerin käyttö on olennainen osa käytännönläheistä lähestymistapaa Bitcoin-kehitykseen. Nämä työkalut helpottavat työskentelyä Bitcoin-ohjelmistopinon kanssa, kehitysympäristöjen hallintaa ja yhteistyötä projekteissa todellisessa ympäristössä.


## Miksi Bitcoin


<chapterId>89a0aa8b-90bd-58b2-82b3-bc5e1f82eaeb</chapterId>


### Miksi El Salvador tarvitsee Bitcoin:tä


:::video id=ff820fb2-83d4-450f-bda0-17cc5044a902:::

Tervetuloa **Cubo Plus** -koulutusohjelman ensimmäiselle luennolle. Tänään sukellamme Bitcoin:n maailmaan Rickyn, **Bitcoin Italia Podcastin** perustajan, johdolla. Ricky on intohimoinen ihmisoikeusaktivisti, joka käyttää Bitcoin:ta välineenä ihmisoikeuksien suojelemiseksi ja edistämiseksi. Yli kuuden vuoden kokemuksella Ricky on matkustanut paljon ja dokumentoinut Bitcoin:n käyttöönottoa kehittyvillä markkinoilla, kuten El Salvadorissa ja Guatemalassa. Hänen työnsä on muutakin kuin podcastia; hän on aktiivinen myös YouTubessa (**Bitcoin Explorers**) ja Twitterissä (**BTC Explorer**, **Ricky6**). Rickyn Commitment:n ja Bitcoin:n välinen suhde johtuu hänen vakaumuksestaan, että se tarjoaa taloudellista vapautta ja yksityisyyttä ja haastaa perinteiset, keskitetyt pankkijärjestelmät.


![Unbanked Population](assets/en/001.webp)

maailmanlaajuinen pankkitoiminnan ulkopuolelle jäävä väestö


### Bitcoin: taloudellinen vapaus ja sen vaikutus El Salvadoriin


Tämä luento, **"Miksi El Salvador tarvitsee Bitcoin:n "**, tarjoaa yleiskatsauksen **Bitcoin-protokollaan**, sen juuriin **Cypherpunk-liikkeessä** ja sen rooliin vapautta edistävänä välineenä, joka mahdollistaa **sensuroimattoman rahan**, **rahoituksellisen osallisuuden** ja paljon muuta.


**Määritelmät:**


- _Bitcoin-protokolla:_ Säännöt ja rakenne, jotka ohjaavat Bitcoin:n toimintaa hajautettuna digitaalisena valuuttana.
- __Cypherpunk-liike:_ Ryhmä, joka kannattaa salakirjoituksen käyttöä yksityisyyden ja vapauden varmistamiseksi digitaalisissa tiloissa.
- _Rahoitusmarkkinoille osallistaminen:_ Rahoituspalvelujen tarjoaminen ihmisille, jotka ovat jääneet perinteisten pankkijärjestelmien ulkopuolelle ja joihin usein viitataan nimellä "ilman pankkitoimintaa"
- _ Sensuroimaton raha:_ Raha, jota hallitukset tai rahoituslaitokset eivät voi valvoa tai rajoittaa.

#### Rickyn tausta ja Bitcoin:n puolustaminen


Rickyn matka Bitcoin:een juontaa juurensa hänen työhönsä ihmisoikeuksien puolustajana. Hän uskoo, että Bitcoin voi antaa yksilöille mahdollisuuden hallita raha-asioitaan, jolloin he voivat suojella yksityisyyttään ja välttää keskitettyjen pankkien rajoitukset. Hänen tutkimuksensa Bitcoin:n käyttöönotosta El Salvadorin kaltaisissa paikoissa korostaa, miten tämä teknologia voi antaa kehittyvien markkinoiden ihmisille mahdollisuuden saavuttaa taloudellinen riippumattomuus.


### Bitcoin:n maailmanlaajuinen merkitys ja haasteet


Bitcoin on paljon muutakin kuin digitaalinen valuutta. Se on väline yksityisyyden suojaamiseen ja taloudellisen vapauden varmistamiseen. Käyttämällä **yksityisiä avaimia**, jotka toimivat ikään kuin pääsalasanojen tavoin, käyttäjät voivat hallita Bitcoin:ttä turvallisesti ja hallita varojaan täysin.


Autoritaarisissa järjestelmissä, joissa taloudellinen sorto on yleistä, Bitcoin:n **sensoimaton luonne** antaa ihmisille mahdollisuuden tehdä liiketoimia ilman pelkoa siitä, että heidän varansa jäädytetään tai takavarikoidaan. Sen **avoimen lähdekoodin** luonne rohkaisee maailmanlaajuista osallistumista ja edistää yhteisöä, joka parantaa verkkoa jatkuvasti.


![Image](assets/en/002.webp)


Bitcoin:lla on potentiaalistaan huolimatta merkittäviä haasteita. Afrikan ja Intian kaltaisilla alueilla perusinfrastruktuuri, kuten sähkö- ja internet-yhteydet, puuttuvat usein, mikä rajoittaa käyttöönottoa. Lisäksi **digitaalinen osallisuus** - sen varmistaminen, että kaikenikäiset ja koulutustasoltaan erilaiset ihmiset voivat käyttää teknologiaa - on edelleen suuri este.


**Määritelmät:**


- _Private keys:_ Salaiset koodit, joilla pääsee käsiksi käyttäjän Bitcoin:ään.
- _Avoin lähdekoodi:_ Ohjelmisto, jota kuka tahansa voi tarkastaa, muokata ja parantaa.

### El Salvadorin tapaus


El Salvadorin päätös ottaa Bitcoin käyttöön laillisena maksuvälineenä osoittaa sen muutosvoiman. Käyttämällä Bitcoin:ää maa pyrkii houkuttelemaan ulkomaisia investointeja ja edistämään rahoitusvakautta. Bitcoin Beachin** kaltaiset hankkeet osoittavat, miten paikallistaloudet voivat kasvaa ottamalla Bitcoin käyttöön Exchange:n välineenä.


Bitcoin:n maailmanlaajuista käyttöönottoa haittaavat kuitenkin esimerkiksi tietämättömyys, uuden teknologian vastustaminen ja infrastruktuurin haasteet. Tie kohti osallistavampaa rahoitusjärjestelmää, jossa Bitcoin voi auttaa kehitysmaita nousemaan, on pitkä mutta lupaava. Bitcoin:n hajautettu ja avoimen lähdekoodin luonne antaa toivoa tulevaisuudesta, jossa taloudellinen oikeudenmukaisuus on kaikkien saatavilla.


#### Päätelmä


Yhteenvetona voidaan todeta, että Bitcoin on valtavan lupaava rahoitusalan voimaannuttamisen ja osallisuuden kannalta, mutta edessä on vielä merkittäviä haasteita. Bitcoin-yhteisössä mukana pysyminen, oppiminen ja kysymysten esittäminen ovat avainasemassa hajautetun rahoitustulevaisuuden toteuttamisessa. Yhteistyön ja edunvalvonnan avulla visio oikeudenmukaisemmasta rahoitusjärjestelmästä kaikille voi toteutua.


### Cypherpunk-liike ja itävaltalainen taloustiede


![video](https://youtube.com/live/KIaC31YQLBA)


#### Cypherpunk-liike


Cypherpunk-liike** syntyi 1900-luvun loppupuolella, ja se ajoi yksityisyyden ja vapauden säilyttämistä salakirjoituksen avulla. Edelläkävijät, kuten **Eric Hughes** ja **Tim May**, uskoivat, että vahva salaus oli välttämätöntä henkilökohtaisen vapauden suojelemiseksi digitaalisessa maailmassa. Heidän ajatuksensa vaikuttivat suuresti Bitcoin:n luomiseen.


**Määritelmä:**


- __Cypherpunk:_ Liike, joka edistää yksityisyyttä ja vapautta kryptografian avulla.

#### Itävaltalainen taloustiede


Samaan aikaan **australialainen taloustiede** loi perustan Bitcoin:n rahapoliittisille periaatteille. Taloustieteilijät, kuten **Ludwig von Mises** ja **Friedrich Hayek**, väittivät, että terveen rahan pitäisi olla niukkaa, kestävää ja hyvää arvon säilyttäjää - nämä keskeiset periaatteet muokkasivat Bitcoin:n suunnittelua.


**Määritelmä:**


- _Puute:_ Rajoitettu saatavuus, joka luo arvoa huolellisen jakamisen tarpeen vuoksi.

### Bitcoin:n luominen


**Satoshi Nakamoto** yhdisti nämä ideat ja loi Bitcoin:n vuonna 2008 hajautetuksi, sensuurin kestäväksi digitaaliseksi valuutaksi. Yhdistämällä Cypherpunk:n yksityisyyden ihanteet ja itävaltalaiset terveen rahan periaatteet Bitcoin tarjoaa rahoitusjärjestelmän, joka haastaa perinteiset pankit ja hallituksen valvonnan.


**Määritelmä:**


- _Sensuurin kestävä:_ Raha, jota ulkoiset voimat eivät voi valvoa tai estää.

#### Keskeiset taloudelliset periaatteet



- Niukkuus:** Bitcoin:n kiinteä Supply takaa sen arvon pitkällä aikavälillä.
- Aikapreferenssi:** Kannustaa säästämään tulevaisuutta varten sen sijaan, että käyttäisi rahaa heti.
- Säästäminen:** Arvon varastointi tulevia tarpeita varten, mikä johtaa investointeihin ja innovaatioihin.


**Määritelmät:**


- _Aikapreferenssi:_ Nykyisten hyödykkeiden arvostaminen tuleviin nähden.
- _Säästäminen:_ Arvon tallentaminen tulevaa käyttöä varten.

### Bitcoin El Salvadorissa


Bitcoin:n käyttöönotto El Salvadorissa kuvastaa sen potentiaalia taloudellisen vapauden välineenä, ja se on linjassa **Austrian Economicsin** kanssa edistämällä vapaaehtoista käyttöönottoa ja hajauttamista. Tällä toimenpiteellä haastetaan perinteiset rahoitusjärjestelmät puuttumalla keskeisiin kysymyksiin: kilpailuun, monopoliin ja konfiskaatioon.


![Image](assets/en/003.webp)



- Kilpailu**: Bitcoin tuo kilpailua rahoitusmaailmaan tarjoamalla vaihtoehdon perinteiselle pankkitoiminnalle, jolloin salvadorilaiset voivat ohittaa rahoitusalan portinvartijat ja valita tarpeitaan paremmin vastaavat palvelut.



- Monopoli**: Hajauttamalla rahoituksen saatavuutta Bitcoin murtaa pankkien ja valtion liikkeeseen laskemien valuuttojen monopolin, vähentää riippuvuutta keskitetyistä instituutioista ja edistää taloudellista osallisuutta.



- Takavarikointi**: Bitcoin:n vastustus takavarikointia vastaan antaa salvadorilaisille mahdollisuuden hallita omaisuuttaan, suojelee heidän varallisuuttaan ulkopuoliselta takavarikolta ja lisää taloudellista itsemääräämisoikeutta.


El Salvadorin omaksuma Bitcoin edistää osallistavampaa, kilpailukykyisempää ja turvallisempaa rahoitusjärjestelmää ja haastaa perinteisen rahoituksen rajoitukset.


#### Päätelmä


Bitcoin:n perustana on **Cypherpunk-liike** ja **Austrian Economics**, mikä tekee siitä ainutlaatuisen ja vallankumouksellisen rahan. Näiden periaatteiden ymmärtäminen auttaa ymmärtämään, miksi Bitcoin luotiin ja miten se toimii nykyään. Lisälukemiseksi kannattaa tutustua **Saifedean Ammousin** kirjoittamaan **The Bitcoin Standard**.


Kiitos, että olette paneutuneet tähän aineistoon!


## Miten Bitcoin


<chapterId>d800970a-0d8e-5557-810a-7aef845d4a34</chapterId>


### Bitcoin:n teknologiapino


:::video id=2c008198-7f4e-4e60-87a0-0af17528ad2f:::

"Miten Bitcoin" -kurssin ensimmäisellä luennolla aloimme tutkia Bitcoin-verkon perustana olevaa teknologiapinoa. Käsittelimme muun muassa **Hashcash**, **transaktiot**, **Blockchain**, **Lightning Network** ja muita Bitcoin-protokollan keskeisiä komponentteja.


### Bitcoin:n teknologinen pino osa 2


:::video id=752343b8-aa78-4bd3-9320-efe2a7e9d88f:::
Toisella luennolla "Miten Bitcoin" tutustuimme syvällisemmin Bitcoin:n teknologiapinoon.


### Bitcoin rakenne


Bitcoin:n juuret perustuvat useisiin keskeisiin innovaatioihin, alkaen **Adam Backin Hashcashista**, Proof-of-Work (PoW) -järjestelmästä, joka on suunniteltu estämään sähköpostiroskapostia ja palvelunestohyökkäyksiä vaatimalla lähettäjiä suorittamaan laskutehtäviä. Tästä PoW-konseptista tuli Bitcoin:n turvallisuuden kulmakivi.


Bitcoin perustuu **digitaalisiin allekirjoituksiin**, joissa käytetään **elliptisen käyrän salausta** tapahtumien suojaamiseksi ja todentamiseksi. **Elliptic Curve Digital Signature Algorithm (ECDSA)** varmistaa, että vain Bitcoin:n laillinen omistaja voi valtuuttaa tapahtumat paljastamatta yksityisiä avaimiaan.


**Satoshi Nakamoto**, Bitcoin:n pseudonyymi, laajensi näitä ajatuksia siirtymällä PoW-mallista hajautettuun **Blockchain**-malliin. Tämä mahdollisti sen, että solmujen hajautettu verkko voi validoida ja kirjata transaktioita ilman keskusviranomaista, mikä merkitsi merkittävää kehitystä aiemmista digitaalisen valuutan yrityksistä.


**Määritelmät:**


- _Proof-of-Work (PoW):_ Järjestelmä, jossa osallistujien on ratkaistava laskennallisia pulmia transaktioiden vahvistamiseksi ja verkon suojaamiseksi.
- _Elliptic Curve Cryptography:_ Kryptografinen menetelmä, joka mahdollistaa turvalliset ja tehokkaat digitaaliset allekirjoitukset.

### Blockchain-mekaniikka ja tapahtumien validointi


Bitcoin-transaktiot validoidaan ja lisätään lohkoihin **minereiden** toimesta, jotka kilpailevat Proof-of-Work-algoritmia käyttävän salakirjoituspalapelin ratkaisemisesta. Tehtävänä on löytää Hash, jossa on tietty määrä etunollia, muuttamalla **Nonce**-arvoa, kunnes oikea Hash on löydetty.


Jokainen **lohko** Blockchain:ssä koostuu **otsikosta** (jossa on edellisen lohkon Hash:n kaltaisia tietoja) ja luettelosta tapahtumista. Ensimmäinen lohko, joka tunnetaan nimellä **Genesis-lohko**, on ainutlaatuinen, koska sillä ei ole edeltäjää.


![Image](assets/en/004.webp)


Ennen kuin tapahtumat sisällytetään lohkoon, ne ovat **Mempool**:ssä, jossa ne odottavat validointia. Kun transaktiot on validoitu, ne lisätään juuri louhittuun lohkoon ja sen jälkeen Blockchain:een.


**Määritelmät:**


- _Mining:_ Prosessi, jossa kryptografisia arvoituksia ratkotaan uusien lohkojen lisäämiseksi Blockchain:een.
- _Nonce:_ Arvo, jota käytetään oikean Hash:n löytämiseen Mining:n aikana.
- _Mempool:_ Odotusalue vahvistamattomille transaktioille ennen niiden lisäämistä lohkoon.

### Skaalautuvuus, yksityisyys ja kehitys Bitcoin:ssa


Bitcoin:n haasteet liittyvät skaalautuvuuteen ja yksityisyyteen. Blockchain:n rajallinen tapahtumakapasiteetti vaikeuttaa suurten tapahtumamäärien käsittelyä. Address:n kaltaiset ratkaisut, kuten **Lightning Network** Address, ratkaisevat nämä haasteet mahdollistamalla off-chain-tapahtumat maksukanavien kautta, mikä lisää nopeutta ja yksityisyyttä.


**Full node:n** käyttäminen on välttämätöntä hajauttamisen ja turvallisuuden varmistamiseksi, mutta **Simplified Payment Verification (SPV) -solmut** mahdollistavat kevyemmän osallistumisen jonkin verran turvallisuuden kustannuksella.


Bitcoin:n kehitys on kehittynyt suorituskyvyn ja turvallisuuden parantamiseksi. Tärkeimpiä parannuksia ovat **Segregated Witness (SegWit)**, joka puuttuu transaktioiden muokattavuuteen ja kasvattaa tehokasta lohkokokoa, sekä **Taproot**, joka parantaa yksityisyyttä ja mahdollistaa monimutkaisemmat sopimukset käyttämällä **Merkleized Abstract Syntax Trees (MAST)**.


**Määritelmät:**


- _SegWit:_ Bitcoin-päivitys, joka erottaa allekirjoitustiedot tapahtumatiedoista ja parantaa tehokkuutta.
- _Taproot:_ Päivitys, joka parantaa Bitcoin:n yksityisyyttä ja skaalautuvuutta mahdollistamalla monimutkaisemmat älykkäät sopimukset.
- _Lightning Network:_ Toinen Layer -ratkaisu nopeampiin ja halvempiin Bitcoin-tapahtumiin maksukanavia käyttäen.

#### Päätelmä


Bitcoin:n rakenne ja jatkuva kehitys ovat osoitus sen teknologian innovatiivisuudesta ja mukautuvuudesta. **Hashcashista** hajautettuun Blockchain:een ja **SegWit:sta** **Taproot:een** Bitcoin jatkaa Address:n haasteita, jotka liittyvät skaalautuvuuteen, yksityisyyteen ja turvallisuuteen. Yhteisön jatkuvat ponnistelut varmistavat, että Bitcoin pysyy joustavana ja hajautettuna ja kehittyy samalla vastaamaan tulevaisuuden vaatimuksia.


## Bitcoin:n kumoaminen


<chapterId>171ec71d-3028-5820-9b4f-36682113fc81</chapterId>


### Bitcoin:n kumoaminen


:::video id=c5e2e575-fa9d-4430-805f-205c2cf6f2a5:::

Tällä luennolla kumotaan yleisiä myyttejä, jotka liittyvät **Bitcoin:aan**, **lohkoketjuihin** ja **kryptovaluuttoihin**. Käydään läpi Address:n harhaluuloja Bitcoin:n energiankulutuksesta, rikollisesta käytöstä ja laajemmasta "FUD" (pelko, epävarmuus, epäilys) -ilmiöstä, joka on levinnyt tästä teknologiasta.


### Bitcoin vs. Blockchain


Yleinen väärinkäsitys on, että **Bitcoin** ja **Blockchain** ovat samat. Bitcoin on digitaalinen valuutta, mutta **Blockchain** on teknologia, jolla se toimii. Lohkoketjut tarjoavat todennetun tallenteen transaktioista, mutta niihin liittyy kompromisseja, kuten hitaampi nopeus ja korkeammat kustannukset, joita **Lightning Network** Address:n kaltaiset ratkaisut tarjoavat.


**Määritelmät:**


- _Lohkoketju:_ Taustalla oleva teknologia, jota käytetään transaktioiden tallentamiseen hajautettuun, muuttumattomaan Ledger:ään.
- _Lightning Network:_ Toinen Layer-ratkaisu, joka parantaa Bitcoin:n tapahtumien tehokkuutta mahdollistamalla off-chain-tapahtumat.

### Bitcoin vs. Crypto


Toinen tärkeä ero on se, että **Bitcoin** luotiin ainoastaan tarjoamaan hajautettu, sensuurin kestävä rahamuoto, joka ei ole minkään yrityksen tai hallituksen valvonnassa. Kryptovaluutat **shitcoins** sen sijaan on usein suunniteltu keskitetysti valvottaviksi, ja ne ovat ensisijaisesti olemassa rikastuttaakseen niiden takana olevia yrityksiä saalistuskäytännöillä, pumppaus- ja myyntijärjestelmillä tai suoranaisilla huijauksilla. Näillä rahakkeilla ei tyypillisesti ole muuta todellista tarkoitusta kuin tuottaa nopeaa voittoa niiden luojille tietämättömien sijoittajien kustannuksella. Bitcoin on kuitenkin ainoa aidosti hajautettu digitaalinen valuutta, jonka turvallisuus ja kestävyys on todistetusti todistettu.


**Määritelmät:**


- _Shitcoinit:_ Shitcoinit ovat arvoltaan vähäisiä tai laadultaan kyseenalaisia kryptovaluuttoja, joista puuttuu todellinen hyöty. Ne ovat usein hyvin spekulatiivisia, ja ne luodaan joskus vilpillisiin tarkoituksiin tai ilman selkeää tarkoitusta kryptovaluuttamarkkinoiden noususuhdannetta hyväksikäyttäen.

![Image](assets/en/005.webp)


### Energiankulutus ja ympäristövaikutukset


Yksi Bitcoin:n yleisimmistä kritiikeistä on sen **energiankulutus**. Vaikka Bitcoin Mining kuluttaa energiaa, sen osuus on alle 1 % maailmanlaajuisesta sähkönkulutuksesta ja alle 3 % hukkaenergiasta. Lisäksi **Bitcoin Mining** hyödyntää usein käyttämättömiä tai uusiutuvia energialähteitä, mikä tekee siitä usein esitettyä vihreämmän.


**Määritelmät:**


- _Bitcoin Mining:_ Transaktioiden validointi ja verkon turvaaminen ratkaisemalla kryptografisia arvoituksia, mikä vaatii laskentatehoa.

### Rikollista käyttöä koskevat väärinkäsitykset


Bitcoin:ää kritisoidaan usein siitä, että sitä käytetään rikollisessa toiminnassa. Blockchain-analyysi osoittaa kuitenkin, että vain pieni osa Bitcoin-tapahtumista liittyy rikollisuuteen. Todellisuudessa perinteisiä rahoitusjärjestelmiä käytetään rikollisiin tarkoituksiin paljon enemmän kuin Bitcoin:ää.


### Yksityisyys ja korvattavuus


*gW-118:n olennaisia ominaisuuksia ovat *Salaisuus** ja **siitettävyys**. Yksityisyys suojaa käyttäjiä sortohallinnoissa, ja korvattavuus varmistaa, että jokainen Bitcoin on samanarvoinen sen historiasta riippumatta. Tämä tekee Bitcoin:sta luotettavan ja oikeudenmukaisen rahan.


**Määritelmät:**


- _Korvattavuus:_ Rahan ominaisuus, jossa jokainen yksikkö on vaihdettavissa toiseen, mikä takaa yhtäläisen arvon.

### FUD:n ja markkinadynamiikan käsittely


Bitcoin:n ympärillä vallitsevassa pelossa liioitellaan usein huolia sen ympäristövaikutuksista, rikollisesta käytöstä ja turvallisuudesta. Vaikka markkinoiden vaihteluita esiintyykin, Bitcoin:n hajautettu ja luotettava teknologia tarjoaa vankan perustan pitkän aikavälin vakaudelle ja taloudelliselle vapaudelle erityisesti Venezuelan kaltaisissa rajoittavissa ympäristöissä.


#### Päätelmä


Bitcoin:n energiankulutuksen, yksityisyyden suojaominaisuuksien ja rikosten ehkäisyn merkityksen ymmärtäminen auttaa hälventämään siihen liittyviä myyttejä. Kun pääsemme eroon valheista, voimme arvostaa Bitcoin:n potentiaalia vallankumouksellisena terveen rahan muotona, joka edistää yksityisyyttä, turvallisuutta ja hajauttamista.


## Bitcoin käynnissä


<chapterId>5f638ec9-a6c1-5716-b27f-d837ab896eb1</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


### Bitcoin core:n asennus


:::video id=4a5253cf-b863-466a-8506-0506b28a28de:::

Neljännen moduulin ensimmäisellä luennolla tutustuimme Bitcoin:n arkkitehtuuriin ja Bitcoin core-solmun asennukseen.


### Bitcoin-solmun käyttäminen


**1. Johdanto yhteenveto**

Tervetuloa takaisin! Edellisessä istunnossa käsiteltiin Bitcoin:n arkkitehtuurin peruskäsitteitä, mukaan lukien sen kryptografiset perusteet ja vertaisverkon rakenne. Tänään siirrymme teoriasta käytäntöön esittelemällä, miten Bitcoin-solmu asennetaan ja konfiguroidaan.


**2. Käytännön istunnon yleiskatsaus**

Tässä istunnossa Alekos opastaa meitä Bitcoin-solmun perustamisessa virtuaalikoneen avulla. Tämä käytännönläheinen opetusohjelma on suunniteltu tutustuttamaan sinut vaiheisiin, jotka liittyvät solmun konfigurointiin Bitcoin-verkkoon osallistumista varten.


Bitcoin-solmun pyörittämiseen kuuluu transaktioiden ja lohkojen validointi, konsensussääntöjen noudattaminen ja verkon hajauttamisen tukeminen. Solmun perustaminen varmistaa, että sinulla on suora yhteys Bitcoin-verkkoon, jolloin voit edistää sen turvallisuutta ja eheyttä.


Tällä luennolla saat oppaan oman Bitcoin core:n asentamiseen ja käyttämiseen, opit, miten Blockchain:n karsiminen säästää tilaa, ja aloitat ohjelmiston kokeilun. Alekos opastaa sinua askel askeleelta tässä jännittävässä prosessissa.


### Mitä voit tehdä Bitcoin core:n avulla ja sen hyödyt


Käyttämällä Bitcoin core:ta saat seuraavat valmiudet:



- Validoi omat transaktiosi ja lohkosi**: Varmista, että Bitcoin-verkon sääntöjä noudatetaan turvautumatta kolmansiin osapuoliin.
- Verkoston vahvistaminen**: Osallistumalla verkkoon autat pitämään sen hajautettuna, mikä tekee Bitcoin:stä vastustuskykyisemmän hyökkäyksiä vastaan.
- Karsitaan Blockchain**: Vähennä tallennustilavaatimuksia säilyttämällä vain viimeisimmät tapahtumat, mikä on ihanteellista, jos levytilaa on rajoitetusti.
- Käytä Wallet:n kehittyneitä ominaisuuksia**: Hallitse Bitcoin:ääsi yksityisesti ja turvallisesti, käytä generate:n yksityisiä avaimia offline-tilassa ja allekirjoita tapahtumia turvallisesti.
- Ole suoraan yhteydessä Bitcoin-verkkoon**: Bitcoin core:n avulla voit muodostaa yhteyden suoraan verkkoon ilman välikäsiä, mikä takaa, että saat tarkimmat tiedot.
- Hyödy lisääntyneestä yksityisyydestä**: Full node-operaattorina sinun ei tarvitse luottaa ulkoisiin palveluihin, mikä suojaa tapahtumien yksityisyyttä ulkopuoliselta valvonnalta.


Bitcoin-solmun käyttämisestä saatava hyöty on merkittävä kaikille Bitcoin-asiakkaille. Sen lisäksi, että autat verkon turvaamisessa ja sen hajauttamisen vahvistamisessa, parannat myös yksityisyyttäsi, varmistat omien tapahtumiesi eheyden ja otat ennakoivan roolin Bitcoin-ekosysteemissä. Solmupisteen pyörittäminen on tärkeä askel kohti taloudellista riippumattomuutta ja Bitcoin:n hajautetun luonteen täydellistä omaksumista.


### Peruskäskyt


Nämä ovat joitakin peruskomentoja, kun konfiguroit solmua:



- Tarkista Bitcoin daemon**:n tila:


```bash
sudo systemctl status bitcoind
```



- Käynnistä Bitcoin daemon:**:


```bash
systemctl start bitcoind
```



- Pysäytä Bitcoin daemon:**:


```bash
sudo systemctl stop bitcoind
```



  - Hanki yksityiskohtaiset tiedot**:


```bash
bitcoin-cli getblockchaininfo
```



- Blockchain:n karsiminen säästää levytilaa säilyttämällä vain viimeisimmät lohkot:**:


```bash
prune=550
```



- Ota Bitcoin core-palvelin käyttöön ja määritä RPC-asetukset:**:


```bash
server=1
rpcuser=yourusername
rpcpassword=yourpassword
```



- Tarkista Bitcoin daemon**:n tila:


```bash
sudo systemctl status bitcoind
```



- Tarkista Bitcoin Wallet:n tasapaino:**:

```bash
sudo systemctl status bitcoind
```


### C-salaman asennus


:::video id=e13a1407-46e3-4b03-9a7a-b0f4a338c3c7:::

#### 1. **Bitcoin core recap**


Aloitetaan lyhyellä yhteenvedolla vaiheista, jotka liittyvät Bitcoin core:n asentamiseen pilvipalvelimen VM:ään, sillä tämä on ratkaisevan tärkeää C-Lightningin myöhemmän asennuksen kannalta.


** Bitcoin core:n uudelleenasentaminen pilvipalvelun VM:ään**

Aluksi asenna Bitcoin core uudelleen virtuaalikoneeseesi. Tässä istunnossa ohitamme binääritiedostojen tarkistamisen ajan säästämiseksi, mutta muista, että tuotantoympäristössä binääritiedostojen tarkistaminen on kriittinen vaihe turvallisuuden varmistamiseksi.


**Lataa ja tarkista tiedostojen hashit**

Lataa ensin uusin Bitcoin core-julkaisu ja tarkista tiedostojen hashit varmistaaksesi, ettei niitä ole peukaloitu.


```sh
wget https://bitcoin.org/bin/bitcoin-core-22.0/bitcoin-22.0-x86_64-linux-gnu.tar.gz
sha256sum bitcoin-22.0-x86_64-linux-gnu.tar.gz
# Compare the output hash with the official hash
```


**Asenna binääri ja määritä automaattinen käynnistys systemd:llä**

Asenna sitten binääri ja aseta se käynnistymään automaattisesti systemd:n avulla.


```sh
tar -xzf bitcoin-22.0-x86_64-linux-gnu.tar.gz
sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-22.0/bin/*
```


**Luo systemd-palvelutiedosto:**


```sh
sudo nano /etc/systemd/system/bitcoind.service
```


**Lisää seuraavat asetukset:**


```ini
[Unit]
Description=Bitcoin daemon
After=network.target

[Service]
ExecStart=/usr/local/bin/bitcoind -daemon
User=bitcoin
Group=bitcoin
Type=forking
PIDFile=/var/lib/bitcoind/bitcoind.pid
Restart=on-failure

[Install]
WantedBy=multi-user.target
```


**Luo ja määritä Bitcoin-käyttäjä ja hakemistot**

Luo oma käyttäjä ja määritä hakemistot Bitcoin core:lle.


```sh
sudo adduser --disabled-login --gecos "" bitcoin
sudo mkdir -p /var/lib/bitcoind
sudo chown bitcoin:bitcoin /var/lib/bitcoind
```


**Käytä mahdollisimman vähän levytilaa karsimalla Blockchain**:aa

Voit säästää levytilaa ottamalla karsinnan käyttöön asetustiedostossa.


```sh
sudo nano /var/lib/bitcoind/bitcoin.conf
```


Lisää seuraavat rivit:


```ini
prune=550
```


Näiden vaiheiden jälkeen Bitcoin core:n pitäisi olla toiminnassa minimaalisella levynkäytöllä ja valmiina toimimaan C-Lightningin kanssa.


#### 2. **C-salaman yleiskatsaus ja asennus**


**C-salaman yleiskatsaus**


C-Lightning, joka tunnetaan myös nimellä Core-Lightning, on Layer 2 -protokolla, joka mahdollistaa nopeammat ja halvemmat transaktiot off-chain-kanavia käyttäen. Se erottuu edukseen modulaarisen ja kehittäjäystävällisen arkkitehtuurinsa ansiosta, joka mahdollistaa laajan räätälöinnin lisäosien avulla.


**Modulaarisuuden ja laajennettavuuden merkitys lisäosien avulla**

C-Lightningin modulaarinen rakenne tarkoittaa, että ominaisuuksia voidaan lisätä tai poistaa tarpeen mukaan, jolloin järjestelmä voidaan räätälöidä tiettyihin käyttötarkoituksiin. Esimerkkejä käyttötapauksista ovat:



- Maksujen käsittely**: Mukautetut lisäosat voivat käsitellä tiettyjä maksuehtoja.
- Reititysmaksut**: Säädä reititysmaksuja dynaamisesti verkko-olosuhteiden mukaan.
- Automaatio**: Automatisoi tehtävät, kuten kanavien hallinta ja likviditeetin tarjoaminen.


### C-salaman asennus


Siirrytään C-Lightningin asentamiseen.


**Käytä viimeisintä vakaata versiota**

Tällä luennolla käytämme viimeisintä vakaata versiota, esimerkiksi 22.11.1.


```sh
wget https://github.com/ElementsProject/lightning/releases/download/v22.11.1/clightning-v22.11.1.tar.gz
sha256sum clightning-v22.11.1.tar.gz
# Verify the hash against the provided hash
```


**Varmista eheys GPG-avaimilla**

Varmista aina ladatun tiedoston eheys GPG-avaimilla.


```sh
gpg --recv-keys <developer-key-id>
gpg --verify clightning-v22.11.1.tar.gz.asc clightning-v22.11.1.tar.gz
```


**Asenna riippuvuudet ja käännä lähdekoodista**

Asenna tarvittavat riippuvuudet ja käännä C-Lightning lähdekoodista.


```sh
sudo apt-get update
sudo apt-get install -y autoconf automake build-essential git libtool libgmp-dev \
libsqlite3-dev python3 python3-mako net-tools zlib1g-dev
tar -xzf clightning-v22.11.1.tar.gz
cd clightning-v22.11.1
./configure
make
sudo make install
```


**Konfiguroi systemd-palvelu automaattista käynnistystä varten**

Luo systemd-palvelutiedosto C-Lightningille:


```sh
sudo nano /etc/systemd/system/lightningd.service
```


Lisää seuraava kokoonpano:


```ini
[Unit]
Description=C-Lightning daemon
After=network.target bitcoind.service

[Service]
ExecStart=/usr/local/bin/lightningd
User=bitcoin
Group=bitcoin
Type=simple
Restart=on-failure

[Install]
WantedBy=multi-user.target
```


#### 3. **Konfigurointi ja asennus**


**Luo tarvittavat hakemistot ja asetustiedostot**

Luo C-Lightningin tarvitsemat hakemistot ja asetustiedostot.


```sh
sudo mkdir -p /var/lib/lightning
sudo chown bitcoin:bitcoin /var/lib/lightning
sudo -u bitcoin nano /var/lib/lightning/config
```


Lisää seuraavat rivit asetustiedostoon:


```ini
network=testnet
log-level=debug
plugin=/usr/local/libexec/c-lightning/plugins
```


**Konfiguroi C-Lightning muodostamaan yhteys Bitcoin core:ään Testnet:lla**

Varmista, että C-Lightning voi muodostaa yhteyden Bitcoin core:ään lisäämällä seuraavat rivit:


```ini
bitcoin-datadir=/var/lib/bitcoind
bitcoin-rpcuser=<rpcusername>
bitcoin-rpcpassword=<rpcpassword>
```


**Varmista yhteensopivuus ja synkronointi**

Käynnistä palvelut ja varmista, että ne ovat yhteensopivia ja synkronoituja.


```sh
sudo systemctl start bitcoind
sudo systemctl start lightningd
sudo systemctl enable bitcoind
sudo systemctl enable lightningd
```


**Address tiedostopolut ja käyttöoikeudet, erityisesti Tor-integraatiota varten**

Määritä tiedostopolut ja käyttöoikeudet sujuvan toiminnan varmistamiseksi, etenkin jos käytät Tor-verkkoa yksityisyyden suojaamiseksi.


```sh
sudo apt-get install tor
sudo -u bitcoin nano /var/lib/lightning/config
```


Lisää seuraava Tor-integraatiota varten:


```ini
proxy=127.0.0.1:9050
```


**Backup HSM secret for fund recovery**

Varmuuskopioi HSM:n salaisuus rahaston palauttamista varten.


```sh
sudo cp /var/lib/lightning/hsm_secret /path/to/secure/location
```


**Testaa yhteydet ja vahvistaa solmun toimintatilan**

Varmista lopuksi solmun toimintatila testaamalla yhteyksiä ja varmistamalla, että kaikki toimii odotetulla tavalla.


```sh
lightning-cli getinfo
```


Näiden vaiheiden jälkeen sinulla on täysin toimiva C-Lightning-asetus, joka on liitetty Bitcoin core-solmuun ja joka on valmis Testnet-tapahtumia varten.


#### Johtopäätökset ja kysymykset


Lopuksi käsittelimme tänään Bitcoin core:n uudelleenasennuksen keskeiset vaiheet, minkä jälkeen käsittelimme yksityiskohtaisesti C-Lightningin asennuksen ja konfiguroinnin. Jos sinulla on kysyttävää, voit kysyä sen nyt tai valmistella sitä seuraavassa istunnossa tapahtuvaa lisäselvitystä varten. Muista, että käytännön kokemus on ratkaisevan tärkeää, joten käytä Testnet-asennusta, josta keskustelimme, saadaksesi lisää tietoa.


### Turvallisuus ja laitteistot


:::video id=8b4baf24-1350-46b8-a87b-18678ed219ed:::

### Specter ja Ledger-laite


#### Johdanto


Tervetuloa luennolle Bitcoin:n tietoturvasta ja laiteasetuksista. Tänään keskitymme ymmärtämään tietoturvatyökalujen, erityisesti Specter-työpöydän Wallet ja Ledger Hardware Wallet, hyödyntämistä ja niiden tehokasta konfigurointia Bitcoin:n turvallisuuden parantamiseksi.


**Työkalut: Wallet- ja Ledger-emulaattori**


Specter on Wallet-työpöytäohjelma, joka on suunniteltu helpottamaan Bitcoin-lompakoiden luomista ja hallintaa, erityisesti laitteistolaitteita käyttävien lompakoiden osalta. Käytämme esittelyssä Ledger-emulaattoria, joka jäljittelee Ledger Hardware Wallet:n toimintoja.


**Ero Ledger-laitteen ja yrityksen kiistan välillä** *Ero Ledger-laitteen ja yrityksen kiistan välillä**


Ledger-laite, suosittu Hardware Wallet, on tunnettu vankasta turvallisuudestaan. Ledger:n takana oleva yritys on kuitenkin joutunut tarkastelun kohteeksi erilaisten käyttäjätietojen yksityisyyttä koskevien kiistojen vuoksi. Tietoon perustuvan käytön kannalta on tärkeää ymmärtää fyysisen laitteen turvallisuuden ja yrityksen käytäntöjen välinen ero.


**Turvamallit: multi-sig-lompakoiden ja erilaisten laitteistojen merkitys**


Bitcoin-turvallisuuden keskeinen näkökohta on usean allekirjoituksen (multi-sig) lompakoiden hyödyntäminen. multi-sig-lompakot vaativat useita yksityisiä avaimia tapahtuman hyväksymiseksi, mikä parantaa turvallisuutta merkittävästi. Lisäksi erityyppisten laitteistolompakoiden käyttö monipuolistaa riskejä ja vahvistaa turvamallia.


### Asennus ja konfigurointi


**Specterin lataaminen ja käyttöönotto**


Ensimmäinen vaihe asennusprosessissa on Specterin lataaminen sen virallisesta arkistosta. On erittäin tärkeää tarkistaa latauksen eheys, jotta vältytään vaarallisilta ohjelmistoilta. Kun olet ladannut Specterin, asenna se työpöydällesi ja käynnistä sovellus.


** Specterin konfigurointi yhteyden muodostamiseksi Bitcoin core- tai Electrum-palvelimiin**


Specterin konfiguroimiseksi se on yhdistettävä Bitcoin core- tai Electrum-palvelimeen. Nämä palvelimet tarjoavat Blockchain:n toiminnoissa tarvittavat Blockchain-tiedot. Konfigurointiin kuuluu Address-palvelimen asettaminen Specterin asetuksissa ja vakaan yhteyden varmistaminen.


**Johdannaispolkujen ja julkisen avaimen haun selittäminen**


Johdannaispolkujen ymmärtäminen on olennaista Wallet:n hallinnassa. Johdannaispolut määrittelevät, miten avaimet luodaan pääavaimesta. Specterissä voit hakea julkisia avaimia yhdistämällä Hardware Wallet:n (tai emulaattorin) ja navigoimalla Wallet:n Interface:n kautta. Varmista, että dokumentoit nämä polut tulevaa käyttöä varten.


**Käytännön demonstraatio: Ledger-emulaattorin käyttö**


Käytämme nyt Ledger-emulaattoria avainten hakemiseen. Tämä edellyttää emulaattorin liittämistä Specteriin, siirtymistä avainten hallintaosioon ja sopivien avainten valitsemista Wallet:n luomista varten.


**Lompakoiden luominen ja hallinta Specterissä**


Wallet:n luominen Specterissä on suoraviivaista. Siirry Wallet:n luomiseen Interface:een, syötä tarvittavat tiedot ja liitä mukaan haetut julkiset avaimesi. Kun olet luonut Wallet:n, voit hallita sitä, valvoa tapahtumia ja varmistaa vankat turvallisuuskäytännöt.


**Tapahtumien vastaanottaminen ja seuranta**


Wallet:n asennuksen jälkeen tapahtumien vastaanottaminen on yhtä helppoa kuin Wallet:n Address:n jakaminen. Specter tarjoaa reaaliaikaista saapuvien tapahtumien seurantaa, mikä varmistaa, että olet aina ajan tasalla Wallet:n tilasta.


### Edistyneet määritykset


**Specter daemon -kaukosäätimen käyttöönotto** *Specter daemon -kaukosäätimen käyttöönotto**


Edistyneemmille käyttäjille Specter daemon:n etäkäytön määrittäminen voi parantaa käytettävyyttä ja turvallisuutta. Tämä tarkoittaa etäpalvelimen määrittämistä Specterin taustapalvelinta varten, mikä mahdollistaa turvallisen käytön eri laitteista.


**Torin käyttöönotto yksityisyyden suojaamiseksi**


Yksityisyyden suojaamiseksi on erittäin suositeltavaa määrittää Specter käyttämään Tor-verkkoa. Tor anonymisoi verkkoliikenteesi ja suojaa IP-osoitteesi Address mahdolliselta tarkkailulta. Tämä on erityisen tärkeää yksityisyydestä ja turvallisuudesta huolestuneille käyttäjille.


**Yhteyden muodostaminen etäyhteyksiin turvallisesti**


Kun muodostat yhteyden etäsolmuihin, varmista, että yhteys on suojattu. Tämä edellyttää SSL/TLS-varmenteiden käyttöä ja solmun aitouden tarkistamista. Suojatut yhteydet estävät man-in-the-middle-hyökkäykset ja varmistavat tietojen eheyden.


**Virheenkorjausongelmat: käytännön tekniikat**


Ongelmien kohtaaminen on väistämätöntä. Käytännön virheenkorjaukseen kuuluu käyttäjien oikeuksien tarkistaminen, tietohakemiston käytön varmistaminen ja lokien tarkastelu virheiden varalta. Varmista esimerkiksi, että Specterillä on tarvittavat oikeudet käyttää Bitcoin core-tietohakemistoa, jotta vältät käyttöhäiriöt.


**Esimerkki ongelmasta: tietohakemiston käyttö**


Yleinen ongelma on virheellinen tietohakemiston käyttö. Tarkista, että Bitcoin core-tietohakemiston polku on asetettu oikein Specterin konfiguraatiossa. Näin varmistetaan, että Specterillä on pääsy Blockchain-tietoihin, joita tarvitaan Wallet-toimintoja varten.


**Jatkotoimet ja integrointi**


Seuraavaksi Specter integroidaan Lightning Network:ään. Tämä mahdollistaa varojen lähettämisen Specteristä Lightning-solmuun, mikä helpottaa nopeampia ja halvempia transaktioita. Tulevilla oppitunneilla käsitellään tätä integraatiota yksityiskohtaisesti ja parannetaan Bitcoin:n transaktio-ominaisuuksia.


**Lohkon ajoituksen vaihtelu**


Lohkojen ajoituksen vaihtelun ymmärtäminen on ratkaisevan tärkeää. Bitcoin-lohkoja voidaan louhia vaihtelevin väliajoin, mikä vaikuttaa transaktioiden vahvistusaikoihin. Tämä vaihtelu on otettava huomioon kaikissa kokoonpanoissa ja Wallet-toiminnoissa.


**Oppimisresurssit**


Jos haluat lisäoppia, tutustu esimerkiksi "Mastering the Lightning Network" -julkaisuun ja Rusty Russellin opetusohjelmiin. Nämä materiaalit tarjoavat syvällistä tietoa Lightning-solmuista ja Bitcoin:n edistyneistä konfiguraatioista.


**Solmujen asennus ja Tor-turva**


Solmujen asentaminen paikallisesti tai etäyhteydellä hyötyy Torin käytöstä turvallisuuden parantamiseksi. Oman solmun käyttäminen takaa henkilökohtaisen tapahtuman validoinnin, mikä parantaa turvallisuutta ja yksityisyyttä.


**Filosofia: omatoiminen oppiminen**


Omaksu omavaraisuusfilosofia. Käytännön taidot ja itseopiskelu ovat ensiarvoisen tärkeitä, ja ne ylittävät usein muodollisen koulutuksen hyödyt. Harjoitellaan käytännönläheisesti Bitcoin-turvallisuuden ymmärtämistä.


**Tietosuojanäkökohdat**


Säilytä yksityisyys välttämällä palveluita, jotka seuraavat tai kirjaavat tapahtumia. Anonymiteetti on ratkaisevan tärkeää Bitcoin-toimintojen turvallisuuden kannalta, ja huolellinen palveluvalikoima auttaa suojaamaan henkilöllisyytesi ja tapahtumahistoriasi.


Tähän päättyy luento Bitcoin:n tietoturvasta ja laiteasetuksista Specterin ja Ledger:n avulla. Voit vapaasti esittää kysymyksiä tai pyytää selvennyksiä käsiteltäviin kohtiin.


## Bitcoin:n parantaminen


<chapterId>4fdd032f-2b05-5f24-a094-297d64f939de</chapterId>


### Avoimet ongelmat Bitcoin-ekosysteemissä


:::video id=6d771eca-3f53-493d-8937-db6ddb2cf172:::

Bitcoin on yli vuosikymmenen ajan osoittautunut rahoitusmaailmaa mullistavaksi innovaatioksi, joka toimii menestyksekkäästi globaalissa mittakaavassa ja avaa uusia mahdollisuuksia digitaalisessa taloudessa. Se kohtaa kuitenkin edelleen haasteita, jotka edellyttävät luovia ja yhteistoiminnallisia ratkaisuja. Bitcoin:n jatkuva kehitys tarjoaa ainutlaatuisen tilaisuuden niille, jotka ovat kiinnostuneita hajautetun rahoituksen tulevaisuuden muokkaamisesta.


![Image](assets/en/006.webp)


#### Bitcoin:n käytettävyyteen liittyvät avoimet ongelmat


Bitcoin:lla on yli vuosikymmenen kestäneestä olemassaolostaan huolimatta edelleen merkittäviä käytettävyyshaasteita. Käyttäjien käytettävissä olevat työkalut ja käyttöliittymät eivät useinkaan ole yhtä kehittyneitä ja käyttäjäystävällisiä kuin perinteisemmissä rahoitusjärjestelmissä. Tämä on erityisen ilmeistä El Salvadorin kaltaisilla alueilla, joilla Bitcoin:n käyttöönotto on saanut hallituksen tuen. Ensisijaisesti tarvitaan parempia abstraktioita, joilla voidaan yksinkertaistaa käyttäjäkokemusta ja tehdä Bitcoin:sta helppokäyttöinen myös henkilöille, joilla on vain vähän teknistä osaamista.


#### Skaalautuvuuteen liittyvät avoimet ongelmat


Skaalautuvuus on ollut jatkuva ongelma Bitcoin:n kehityksessä. Verkon kyky käsitellä suuria transaktiomääriä on edelleen rajallinen, mikä johtaa usein korkeisiin On-Chain-maksuihin, jotka voivat estää joitakin käyttäjiä osallistumasta. Vaikka Lightning Network:n kaltaiset ratkaisut tarjoavat jonkin verran helpotusta mahdollistamalla off-chain transaktiot, ne eivät täysin ratkaise Address skaalautuvuusongelmia. On ilmeistä, että tarvitaan kattavampia ratkaisuja, joilla voidaan käsitellä kasvavia transaktiomääriä vaarantamatta verkon eheyttä.


#### Avoimet turvallisuusongelmat


Bitcoin:n omaisuuden turvaaminen on monimutkainen tehtävä, joka on täynnä haasteita. Hot-lompakot, joita käytetään usein jokapäiväisiin liiketoimiin, aiheuttavat merkittäviä tietoturvariskejä erityisesti Lightning-solmuja ylläpitäville henkilöille. Lisäksi Bitcoin-varojen perimisen suunnittelu on edelleen monimutkainen ja usein epävarma prosessi. Näiden turvatoimien monimutkaisuus voi pelottaa potentiaalisia käyttäjiä ja vaikeuttaa laajamittaista käyttöönottoa.


#### Yksityisyyden suojaan liittyvät avoimet ongelmat


Yksityisyys on toinen kriittinen kysymys Bitcoin-ekosysteemissä. Vaikka yksityisyys on turvallisuuden kannalta olennaisen tärkeää, Bitcoin:n nykyinen kehys tarjoaa vain vähän yksityisyyden suojaa koskevia ominaisuuksia. On-Chain-tapahtumat ovat helposti jäljitettävissä, mikä vaarantaa käyttäjien anonymiteetin. Vaikka Lightning Network:lla on mahdollisuus parantaa yksityisyyttä, se vaatii vielä huomattavia parannuksia. Avoimuuden ja yksityisyyden välinen tasapaino on herkkä ja vaatii innovatiivisia ratkaisuja käyttäjien turvallisuuden ja yksityisyyden varmistamiseksi.


#### Avoimet ongelmat joustavuuden alalla


Bitcoin-protokollan joustavuus on tarpeen, jotta yksityisyyden suojaa, turvallisuutta ja skaalautuvuutta voidaan parantaa. Liiallinen joustavuus voi kuitenkin muuttua haavoittuvuudeksi, joka voi toimia hyökkäysvektorina ja uhata verkon hajautuneisuutta. Oikean tasapainon löytäminen on ratkaisevan tärkeää Bitcoin-protokollan eheyden ja joustavuuden säilyttämiseksi.


### Bitcoin:n parantamiseen liittyvät kompromissit


#### Käytettävyys vs. turvallisuus ja yksityisyys


![Image](assets/en/007.webp)


Bitcoin:n käytettävyyden parantaminen tapahtuu usein turvallisuuden ja yksityisyyden kustannuksella. Esimerkiksi Satoshi:n Wallet:n kaltaiset käyttäjäystävälliset säilytyslompakot tarjoavat helppokäyttöisen Interface:n, mutta tinkivät merkittävästi turvallisuudesta ja yksityisyydestä. Yksinkertaistetut järjestelmät voivat lisätä käytettävyyttä, mutta ne voivat johtaa Address:n uudelleenkäytön kaltaisiin ongelmiin, jotka heikentävät yksityisyyttä. Sen vuoksi käytettävyyden parantamista on punnittava huolellisesti suhteessa mahdollisiin turvallisuuteen ja yksityisyyteen liittyviin kompromisseihin.


#### Skaalautuvuuden ja yksityisyyden suojaa koskevat kompromissit


Bitcoin-verkossa skaalautuvuus ja yksityisyys ovat usein ristiriidassa keskenään. Parannukset, jotka parantavat skaalautuvuutta, kuten suuremmat UTXO:t tai vähäisempi salauksen peittäminen, heikentävät yleensä yksityisyyttä. Toisaalta yksityisyyteen keskittyvät tekniikat, kuten Moneron rengasallekirjoitukset, parantavat käyttäjien anonymiteettiä, mutta vaikuttavat negatiivisesti skaalautuvuuteen. Lisäksi tilatietosopimusten käyttöönotto, kuten Ethereumissa, lisää joustavuutta turvallisuuden ja skaalautuvuuden heikkenemisen kustannuksella. Näiden kompromissien tasapainottaminen on monimutkainen haaste, joka vaatii huolellista harkintaa.


### Yksityisyyden suojaa koskevat tekniikat


Bitcoin:n eri lähestymistavat yksityisyyden suojaan tuovat mukanaan omat kompromissinsa. Yksityisyyden suojaaminen hämärryttämällä, jossa lisätään lisätietoa asiaankuuluvien tietojen peittämiseksi, voi parantaa yksityisyyttä, mutta saattaa monimutkaistaa verkkoa. Esimerkkejä ovat Monero ja Zcash. Toisaalta yksityisyys pois jättämällä, jossa pyritään vähentämään On-Chain:n tietoja, kuten Lightning Network:ssä, voi parantaa sekä yksityisyyttä että skaalautuvuutta. Kullakin menetelmällä on omat etunsa ja haittansa, mikä edellyttää vivahteikasta lähestymistapaa yksityisyyden parantamiseen.


### Konsensuksen muutokset ja haasteet


Bitcoin:n konsensusmekanismin muuttaminen on harvinainen ja haastava tehtävä verkon hajautetun luonteen vuoksi. ChISA:n (cross-input signature aggregation) ja covenanttien kaltaisilla ehdotuksilla pyritään ottamaan käyttöön monimutkaisempia transaktiosääntöjä, mutta niiden toteuttaminen on ongelmallista. Konsensusmuutokset edellyttävät laajaa yhteisymmärrystä yhteisössä, ja tarvittava koordinointi voi johtaa huomattavaan turhautumiseen ja loppuunpalamiseen, jos ehdotettuja muutoksia ei hyväksytä. Tämä korostaa, että pöytäkirjoja kehitettäessä on toimittava huolellisesti ja yhteistyössä.


### Innovaatiot ja standardit Bitcoin:n kehittämisessä


Standardoitujen käytäntöjen noudattaminen Bitcoin Wallet -kehityksessä on ratkaisevan tärkeää helppokäyttöisyyden ja turvallisuuden varmistamiseksi. Monet lompakot eivät tällä hetkellä noudata vakiintuneita standardeja, mikä johtaa hajanaisuuteen ja mahdollisiin haavoittuvuuksiin. Standardoinnilla voidaan merkittävästi parantaa käyttäjäkokemusta ja Bitcoin-transaktioiden yleistä turvallisuutta.


Perinteiset 12 sanan varalauseet ovat tehokkaita Bitcoin:n peruskäytössä, mutta ne eivät sovellu off-chain-protokolliin, kuten Lightning Network:ään. Tulevaisuuden varmuuskopiointistandardeja on kehitettävä, jotta ne tarjoavat paremman turvallisuuden ja käytettävyyden näille kehittyneille ominaisuuksille ja varmistavat, että käyttäjät voivat turvallisesti hallita omaisuuttaan Bitcoin-ekosysteemin eri kerroksissa.


Maksuprosessin yksinkertaistaminen yhtenäisten protokollien avulla on tärkeää käyttäjäkokemuksen parantamiseksi. Nykyiset protokollat, kuten BIP70, BIP78 ja Payneem, tarjoavat erilaisia ratkaisuja, mutta innovaatioille on vielä tilaa. Virtaviivaisempi ja käyttäjäystävällisempi maksuprotokolla voi helpottaa laajempaa käyttöönottoa ja helppokäyttöisyyttä.


Parempien työkalujen ja laitteistojen kehittäminen on välttämätöntä Bitcoin:n käytettävyyden ja turvallisuuden parantamiseksi. Innovaatiot, kuten laitteistolompakot (esim. Ledger ja Trezor), tarjoavat vankkoja turvallisuusratkaisuja, mutta niitä on edelleen kehitettävä Address uusien uhkien vuoksi. Parannetut työkalut voivat tehdä Bitcoin:sta helpommin lähestyttävän ja turvallisemman laajemmalle yleisölle.


Hardware Wallet:n jakeluun liittyvien riskien vähentäminen ja niiden eheyden varmistaminen on ratkaisevan tärkeää. Supply-ketjuun kohdistuvat hyökkäykset aiheuttavat merkittäviä uhkia näiden laitteiden turvallisuudelle. Tiukkojen turvatoimien toteuttaminen ja avoimuuden varmistaminen tuotanto- ja jakeluprosessissa voivat auttaa lieventämään näitä riskejä.


Keskeinen tavoite on yksinkertaistaa käyttäjien vuorovaikutusta Bitcoin:n ja Lightning Network:n kanssa säilyttäen samalla turvallisuus ja tehokkuus. Paremmat käyttöliittymäabstraktiot voivat tehdä Bitcoin:sta helpommin lähestyttävän muille kuin teknisille käyttäjille, mikä edistää laajempaa käyttöönottoa turvallisuudesta tinkimättä.


Bitcoin:n käytettävyyttä, turvallisuutta ja yksityisyyttä parantavan koulutusmateriaalin luominen on vaikuttavaa. Käyttäjien valistaminen parhaista käytännöistä ja Bitcoin:n perusperiaatteista voi auttaa heitä tekemään tietoon perustuvia päätöksiä ja parantaa heidän yleistä kokemustaan verkosta.


![Image](assets/en/008.webp)


**Layer 1 ja Layer 2 muutokset** *Layer 1 ja Layer 2 muutokset**


Innovaatiot Layer:n pohjalla (Layer 1) ovat haastavia mutta ratkaisevan tärkeitä Bitcoin:n pitkän aikavälin kehityksen kannalta. Layer 2 -ratkaisut, kuten Lightning Network, mahdollistavat enemmän kokeellisia muutoksia ja voivat Address skaalautuvuus- ja yksityisyyskysymyksiä joustavammin. Molemmilla kerroksilla on ratkaiseva rooli Bitcoin:n jatkuvassa kehityksessä.


**Konsensuksen koordinointi**


Bitcoin:n protokollaan tehtävät muutokset edellyttävät merkittävää koordinointia ja yhteisön yksimielisyyttä. Bitcoin:n hajautettu luonne tekee tästä prosessista luonnostaan haastavan. Tehokas koordinointi ja selkeä viestintä ovat olennaisen tärkeitä, jotta protokollamuutosten monimutkaisuudesta selviydytään ja parannusten onnistunut käyttöönotto varmistetaan.


**Skaalautuvuuden haasteet**


Maailmanlaajuisen konsensuksen saavuttaminen ja monimutkaisten toissijaisten kerrosten, kuten Lightning Network:n, hallinta asettavat haasteita skaalautuvuudelle. Näihin ongelmiin on puututtava, jotta Bitcoin voi vastata kasvaviin transaktiovolyymeihin ja säilyttää samalla turvallisuuden ja hajauttamisen keskeiset periaatteet.


Johtopäätöksenä voidaan todeta, että näiden avoimien ongelmien jatkuva käsittely ja innovointi Bitcoin-ekosysteemissä on ratkaisevan tärkeää sen kehittymisen kannalta. Käytettävyyden, turvallisuuden, yksityisyyden suojan ja skaalautuvuuden välinen tasapaino edellyttää huolellista harkintaa ja yhteistoimintaa. Osallistumalla tähän kehitykseen osallistujat voivat auttaa muokkaamaan Bitcoin:n tulevaisuutta ja sen roolia maailmanlaajuisessa rahoitusympäristössä.


# Bitcoin Perusteet


<partId>6c0a3691-3ce4-5309-8ad7-e16e4b63c734</partId>


## Turvallisuusajattelu Bitcoin:ssä


<chapterId>0b97af0c-015a-54e3-a7f0-0f62ceb96c07</chapterId>

<professorId>7dfc5865-a0f6-4c3b-9b05-83e0d807ac59</professorId>


:::video id=08101af2-1ded-4f3a-b1db-d4477c6ab63e:::

Tervetuloa tämän päivän luennolle aiheesta **Turvallisuus ja luotettavuus**. Tavoitteenamme on tutkia näiden kahden perustavanlaatuisen järjestelmän suunnittelun ja soveltamisen vivahteikasta suhdetta reaalimaailman skenaarioissa.


### Johdatus turvallisuusajatteluun


Turvallisuusajattelu perustuu periaatteisiin, joiden tarkoituksena on suojata järjestelmiä tahallisilta hyökkäyksiltä. Siihen kuuluu mahdollisten uhkien tunnistaminen ja toimenpiteiden toteuttaminen niiden lieventämiseksi. Luotettavuusajattelussa sen sijaan keskitytään varmistamaan, että järjestelmät toimivat oikein tietyissä olosuhteissa, ja siinä otetaan huomioon pikemminkin todennäköiset viat kuin tahalliset yritykset rikkoa turvallisuutta.


#### Turvallisuuden ja luotettavuuden välinen suhde


Vaikka sekä turvallisuuden että luotettavuuden tavoitteena on järjestelmän eheyden säilyttäminen, niiden lähestymistavat eroavat toisistaan merkittävästi. Luotettavuussuunnittelussa käsitellään satunnaisten tapahtumien aiheuttamien järjestelmävikojen todennäköisyyttä ja käytetään usein tilastollisia menetelmiä näiden vikojen ennustamiseen ja lieventämiseen. Toisaalta tietoturvan on otettava huomioon hyökkäysten tarkoituksellinen ja älykäs luonne, mikä edellyttää monikerroksista puolustusstrategiaa, joka tunnetaan nimellä "syvyyspuolustus"


#### Turvallisuus vs. luotettavuus


Keskeinen esimerkki luotettavuussuunnittelusta voidaan jäljittää 1700-luvulle, jolloin rakennettiin silta. Käytetyn teräksen laatu, mukaan lukien sen koostumus ja valmistusprosessi, vaikutti ratkaisevasti sillan luotettavuuteen. Insinöörien oli otettava huomioon yksittäiset vikapisteet ja käytettävä todennäköisyyttä ja tilastoja arvioidakseen ja varmistaakseen sillan luotettavuuden ajan mittaan.


![Image](assets/en/009.webp)


Toisin kuin luotettavuus, turvallisuus käsittelee tahallisia uhkia. Esimerkiksi 256-bittinen salausavain tarjoaa matemaattisen takuun turvallisuudesta, koska sen murtaminen on mahdotonta. Turvallisuustoimenpiteissä on otettava huomioon erilaiset uhkamallit fyysisestä peukaloinnista kehittyneisiin verkkohyökkäyksiin.


### Reaalimaailman sovellukset


Tarkastellaan Bitcoin-avainten luomista ja tallentamista paperilompakoilla. Vaikka paperilompakot voivat olla turvallisia, ne ovat alttiita fyysisille vaurioille ja peukaloinnille. Tällaisten lompakoiden eheyden varmistaminen edellyttää väärentämisen estäviä menetelmiä ja vankkoja todentamisprotokollia.


Toisessa skenaariossa kuvitellaan, että kuljettaja käyttää salaista koodia todentaakseen matkustajan henkilöllisyyden. Tämä yksinkertainen mutta tehokas turvatoimenpide estää huijareita huijaamasta molempia osapuolia.


Guatemalassa vaalitulosten ajoituksella oli ratkaiseva merkitys vaaliprosessin luotettavuuden varmistamisessa. Käyttämällä kryptografisia menetelmiä Timestamp-tietoihin vaaliviranomaiset pystyivät antamaan väärentämisen varman todisteen tulosten aitoudesta, mikä esti mahdollisia manipuloijia, joita ajoivat merkittävät taloudelliset kannustimet.


![Image](assets/en/010.webp)


### Mahdollisten uhkien tunnistaminen ja lieventäminen


Uhkamallinnus on prosessi, jossa tunnistetaan mahdolliset tietoturvauhat ja luodaan strategioita niiden lieventämiseksi. Tähän kuuluu järjestelmän ympäristön ymmärtäminen, mahdollisten hyökkääjien tunnistaminen ja oletuksiin ja todennäköisyysanalyysiin perustuvien turvallisten protokollien kehittäminen.


#### Turvallisten protokollien luominen


Vaalien turvaamiseksi voidaan esimerkiksi toteuttaa puolueetonta valvontaa tai puoluerajat ylittävää seurantaa avoimuuden ja rehellisyyden varmistamiseksi. Kryptografiset menetelmät, kuten aikaleimaus ja ristiinverifiointi, auttavat säilyttämään tietojen aitouden ja estämään peukaloinnin.


#### Luottamuksen todentaminen


Luottamuksen todentaminen voidaan havainnollistaa PGP (Pretty Good Privacy) -varmennuksella. PGP-avainten sormenjälkien ja allekirjoitusten todentamisella käyttäjät voivat varmistaa digitaalisten identiteettien aitouden. Samanlaiset käytännöt ovat olennaisia, kun ohjelmistojen eheyttä todennetaan Hash-vertailun avulla (esim. SHA-256).


#### Luottamuspolkujen luominen


Luottamuksen rakentaminen ei tapahdu hetkessä, vaan se edellyttää useiden luottamuspolkujen yhdistämistä ja redundanssin varmistamista. Esimerkiksi HTTPS:n ja Blockchain-varmenteen tukeman varmenteen avoimuuden käyttö varmistaa verkkolähteiden aitouden, jolloin hyökkääjien on vaikea rikkoa luottamusta.


#### Turvallisuuskannustimet


Kannustimien roolin ymmärtäminen on ratkaisevan tärkeää turvallisuuden ylläpitämisessä. Esimerkiksi Bitcoin:n turvallisuusmalli perustuu louhijoiden kannustimiin ja verkon osallistujien validointiin, mikä korostaa taloudellisten kannustimien merkitystä digitaalisten ekosysteemien suojaamisessa.


#### Bitcoin-lompakoiden suojaaminen


Bitcoin-lompakoiden turvaamiseen liittyviä strategioita ovat muun muassa usean allekirjoituksen asetukset ja monipuolinen varastointi. Näillä menetelmillä varmistetaan, että kokonaisturvallisuus säilyy ennallaan, vaikka yksi komponentti vaarantuisi.


#### Validoinnin merkitys


Käyttäjien validointi on ratkaisevan tärkeää turvallisen verkon ylläpitämiseksi. Jokaisen käyttäjän rooli tapahtumien validoinnissa ja ohjelmisto- ja laitteistokomponenttien varmentamisessa auttaa säilyttämään verkon eheyden ja torjumaan mahdollisia uhkia.


Yhteenvetona voidaan todeta, että turvallisuus- ja luotettavuusperiaatteiden ymmärtäminen ja yhdistäminen on olennaisen tärkeää luotettavien järjestelmien suunnittelussa. Oppimalla historiallisista esimerkeistä, soveltamalla reaalimaailman strategioita ja validoimalla luottamusta jatkuvasti voimme rakentaa järjestelmiä, jotka ovat sekä turvallisia että luotettavia.


## Vapaat ja avoimen lähdekoodin ohjelmistot (FLOSS) Bitcoin:ssa


<chapterId>2c59d609-f1ef-53f4-9575-df62e4d066e9</chapterId>

<professorId>7dfc5865-a0f6-4c3b-9b05-83e0d807ac59</professorId>


:::video id=4544ef7a-685e-4aaf-98a0-8a10dce06172:::

Vapaan ja avoimen lähdekoodin ohjelmistojen (FLOSS) käyttö on ratkaisevan tärkeää Bitcoin:n ekosysteemissä. Peter Todd tutkii FLOSSin merkitystä Bitcoin:lle, tutustuu FLOSSin historiaan ja tarkastelee, miten Github mahdollistaa Bitcoin:n kaltaisten avoimen lähdekoodin ohjelmistojen rakentamisen yhteistyössä.


### Ohjelmistojen luonne ja merkitys


Ohjelmisto on pohjimmiltaan kokoelma koodia ja dataa, joka ohjaa tietokonelaitteita suorittamaan tiettyjä tehtäviä. Toisin kuin laitteisto, jonka kopiointi edellyttää fyysisiä materiaaleja ja valmistusprosesseja, ohjelmisto voidaan helposti kopioida ja levittää lähes ilmaiseksi. Tämä perustavanlaatuinen ero on ratkaisevassa asemassa ohjelmistojen yleistymisen ja kehityksen kannalta.


Yksi tärkeimmistä ohjelmistojen ja laitteistojen välisistä eroista on avoimen lähdekoodin käsite. Vaikka avoimen lähdekoodin laitteistoja on olemassa, ne eivät ole yhtä yleisiä fyysisten esineiden kopiointiin liittyvien monimutkaisuuksien vuoksi. Sen sijaan avoimen lähdekoodin ohjelmistot menestyvät, koska niiden monistaminen ja jakelu on helppoa. Avoimen lähdekoodin ohjelmistojen ansiosta kuka tahansa voi tarkastella, muokata ja levittää koodia, mikä edistää yhteistoimintaympäristöä, joka nopeuttaa innovointia ja ongelmanratkaisua.


Ohjelmistoja koskeva oikeudellinen kehys pyörii pääasiassa tekijänoikeuslakien ympärillä. Nämä lait myöntävät ohjelmiston tekijälle yksinoikeuden käyttää, muokata ja levittää teosta. Avoimen lähdekoodin lisenssit tarjoavat kuitenkin mekanismin, jolla nämä oikeudet voidaan jakaa yleisön kanssa tietyin ehdoin. Tämä oikeudellinen rakenne on olennaisen tärkeä ohjelmistojen jakelun ja muokkaamisen dynamiikan ymmärtämiseksi.


Yhteenvetona voidaan todeta, että ohjelmistojen luonne helposti kopioitavana koodina ja datana sekä avoimen lähdekoodin lisenssien tarjoamat oikeudelliset mekanismit korostavat niiden ratkaisevaa merkitystä nykyaikaisessa digitaalisessa ympäristössä. Nämä puitteet eivät ainoastaan edistä innovointia vaan myös varmistavat, että maailmanlaajuinen yhteisö voi vapaasti jakaa ja parantaa ohjelmistoja.


### Vapaiden ohjelmistojen liikkeen historia


Vapaiden ohjelmistojen liikkeen juuret ovat 1980-luvun alussa, ja sen taustalla on pääasiassa Richard Stallmanin näkemys ohjelmistojen vapaudesta. Stallman oli turhautunut omistusoikeudellisten ohjelmistojen rajoittavaan luonteeseen ja ryhtyi luomaan ohjelmistoja, joita käyttäjät voisivat vapaasti käyttää, muokata ja jakaa. Tämä johti Free Software Foundationin (FSF) perustamiseen vuonna 1985.


Yksi Stallmanin merkittävistä panoksista oli GNU-projektin kehittäminen, jonka tavoitteena oli luoda vapaa Unixin kaltainen käyttöjärjestelmä. GNU, joka on lyhenne sanoista "GNU's Not Unix", tarjosi monia täysin vapaan käyttöjärjestelmän keskeisiä osia. Siitä puuttui kuitenkin ydin, joka on käyttöjärjestelmän ydinosa.


Linus Torvaldsin vuonna 1991 luoma Linux-ydin täytti tämän aukon. Torvaldsin ydin yhdistettynä GNU-komponentteihin johti täysin toimivaan vapaaseen käyttöjärjestelmään, joka tunnetaan nimellä GNU/Linux. Tämä yhteistyö Stallmanin ohjelmistovapauden filosofisen Commitment:n ja Torvaldsin käytännön panoksen välillä on esimerkki avoimen lähdekoodin lähestymistavan voimasta.


![Image](assets/en/011.webp)


Vapaat ohjelmistot -liike on vaikuttanut syvällisesti ohjelmistoalaan ja edistänyt ajatusta, jonka mukaan ohjelmistojen tulisi olla vapaasti kaikkien käytettävissä, muokattavissa ja jaettavissa. Sen periaatteet ovat luoneet perustan monille nykyään kukoistaville avoimen lähdekoodin hankkeille ja yhteisöille.


### Avoimen lähdekoodin talous ja rahoitus


Avoimen lähdekoodin hankkeiden rahoitus ja ylläpito tarjoavat ainutlaatuisia haasteita ja mahdollisuuksia. Toisin kuin omat ohjelmistot, jotka tuottavat tuloja myynnin ja lisenssimaksujen kautta, avoimen lähdekoodin hankkeet ovat usein riippuvaisia vaihtoehtoisista rahoitusmalleista.


Yksi onnistunut esimerkki on Bitcoin core, joka on tärkeä osa Bitcoin-infrastruktuuria. Bitcoin core:n parissa työskentelevät kehittäjät saavat usein rahoitusta avustuksista, lahjoituksista ja sponsoroinneista organisaatioilta, jotka hyötyvät hankkeen menestyksestä. Tämän mallin ansiosta kehittäjät voivat keskittyä ohjelmiston parantamiseen ilman perinteisen kaupallisen rahoituksen asettamia rajoituksia.


![Image](assets/en/012.webp)


Toinen merkittävä esimerkki on Linux-käyttöjärjestelmä. Monet yritykset, kuten IBM, Red Hat ja Intel, osallistuvat Linuxin kehittämiseen, koska niiden tuotteet ja palvelut ovat riippuvaisia vankasta ja turvallisesta käyttöjärjestelmästä. Nämä yritykset antavat taloudellista tukea, toimittavat koodia ja tarjoavat resursseja Linux-ekosysteemin ylläpitoon ja kehittämiseen.


Avoimen lähdekoodin lisensseillä, kuten MIT-, GPL- ja AGPL-lisensseillä, on myös ratkaiseva rooli avoimen lähdekoodin ohjelmistojen taloudellisessa dynamiikassa. Sallivat lisenssit, kuten MIT, mahdollistavat koodin joustavamman käytön, myös kaupallistamisen. Sitä vastoin copyleft-lisenssit, kuten GPL, varmistavat, että kaikkien johdannaisteosten on oltava myös avoimen lähdekoodin ohjelmistoja, mikä edistää yhteistyöhön perustuvaa ympäristöä.


![Image](assets/en/013.webp)


Yhteenvetona voidaan todeta, että avoimen lähdekoodin ohjelmistojen taloudelliset vaikutukset perustuvat yhteisön panoksiin, yritysten sponsorointiin ja innovatiivisiin rahoitusmalleihin. Nämä mekanismit varmistavat avoimen lähdekoodin hankkeiden kestävyyden ja jatkuvan parantamisen, mistä hyötyvät sekä kehittäjät että käyttäjät.


## Salaus Bitcoin:ssa


<chapterId>71867dd2-912c-55ad-b59c-9dbca8a39469</chapterId>

<professorId>6cfd206c-53b8-47a0-bbf4-44fd84e6ee1d</professorId>


:::video id=b482b0f0-4468-4eaf-bcd6-eb4748bdfa3a:::

Tervetuloa! Tänään perehdymme salakirjoituksen tärkeimpiin näkökohtiin, jotka jokaisen Bitcoin-kehittäjän tulisi tuntea. Keskitymme peruskäsitteisiin ja käytännön sovelluksiin hukuttamatta sinua liiallisilla teoreettisilla yksityiskohdilla. Ensisijaisena tavoitteena on antaa sinulle tiedot, joiden avulla voit ymmärtää, toteuttaa ja korjata Bitcoin:n kryptografisia mekanismeja tehokkaasti.


### Keskeiset salauskäsitteet Bitcoin-kehittäjille


Tässä osassa perehdymme Bitcoin-kehittäjille olennaisiin kryptografisiin avainkäsitteisiin, kuten Hash-funktioihin, Merkle-puihin, digitaalisiin allekirjoituksiin ja elliptisiin käyriin.


![Image](assets/en/014.webp)


**Hash-toiminnot**: Hash-funktio ottaa syötteen ja tuottaa kiinteän pituisen tavujonon. Bitcoin:ssä Hash-funktiot ovat olennaisen tärkeitä tietojen eheyden ja turvallisuuden kannalta. Salausfunktioiden Hash on oltava tehokkaita, generate näennäisesti satunnaisia ja tuotettava kiinteän pituisia tulosteita syötteen koosta riippumatta. Niitä käytetään tiedostojen eheyden tarkistamiseen, jolla varmistetaan, että tietoja ei ole muutettu ilkivaltaisesti.


![Image](assets/en/015.webp)


**Turvallisuusominaisuudet**: Kryptografisten Hash-toimintojen on noudatettava useita turvallisuusominaisuuksia. Esikuvankestävyys varmistaa, että Hash:n tulosteesta ei ole laskennallisesti mahdollista muuntaa alkuperäistä syötettä. Toiseksi pre-image-resistenssi tarkoittaa, että on oltava vaikeaa löytää eri syötettä, joka tuottaa saman Hash-tulosteen. Törmäysresistenssi varmistaa, että on epätodennäköistä löytää kaksi erilaista syötettä, jotka tuottavat saman Hash-tuloksen.


**Merkle-puut**: Merkle Tree on tietorakenne, joka mahdollistaa suurten tietokokonaisuuksien tehokkaan ja turvallisen todentamisen. Tietoelementit hakataan pareittain, ja saadut hakat yhdistetään iteratiivisesti yhdeksi juureksi Hash:ksi. Bitcoin:ssa Merkle-puut ovat ratkaisevan tärkeitä lohkojen luomisessa ja tapahtumien todentamisessa, erityisesti yksinkertaistetun maksujen todentamisen (SPV) asiakkaissa ja Taproot:ssä (Mast).


![Image](assets/en/016.webp)


**Digitaaliset allekirjoitukset (ECDSA)**: Elliptic Curve Digital Signature Algorithm (ECDSA) -algoritmia käytetään Bitcoin-tapahtumien aitouden ja eheyden varmistamiseen. Siinä luodaan allekirjoitus yksityisellä avaimella, joka voidaan todentaa vastaavalla julkisella avaimella. Keskeisiä käsitteitä ovat äärellisten kenttien, diskreettien logaritmien ja nonceen merkityksen ymmärtäminen.


**Elliptiset käyrät**: Elliptisiä käyriä käytetään julkisen avaimen salauksessa niiden tehokkuuden ja turvallisuuden vuoksi. Elliptisten käyrien salauksen turvallisuus perustuu diskreetin logaritmin ongelman ratkaisemisen vaikeuteen.


![Image](assets/en/017.webp)


### Käytännön kryptografiasovellukset ja turvallisuuskäytännöt Bitcoin:ssa


Tässä osassa tarkastelemme näiden käsitteiden soveltamista Bitcoin:n käytännön kehitystyössä ja parhaita turvallisuuskäytäntöjä.


**Salaaminen = vaara**: Kryptografia on kaksiteräinen miekka. Vaikka se suojaa vahingossa tapahtuvilta tietovahingoilta ja pahantahtoisilta toimilta, virheellinen toteutus voi johtaa vakaviin haavoittuvuuksiin. Kehittäjien on ymmärrettävä syvällisesti salausmekanismeja, jotta voidaan varmistaa sekä turvallinen toteutus että kyky korjata mahdollisia ongelmia. Esimerkiksi SHA-2:n 256-bittinen ulostulo varmistaa, että preimage-hyökkäykset vaativat noin 2^256 työtä ja törmäyssuojaus noin 2^128 työtä.


![Image](assets/en/018.webp)


**Merkle Tree-sovellukset**: Hash: Logaritmisen todisteen koon ymmärtäminen ja huolellinen puun suunnittelu on olennaista, jotta voidaan välttää virheet, kuten Hash kaksoiskappaleet tapahtumien todentamisessa. Merkle-puita käytetään lohkojen luomisessa, tapahtumien todentamisessa ja Taproot:n kaltaisissa parannuksissa.


**Julkisen avaimen salaus**: Diskreetit logaritmit ja äärelliset kentät ovat perustavanlaatuisia Bitcoin:n kryptografisissa laskutoimituksissa. Haaste-vastaus-protokollia käytetään yksityisen avaimen tietämyksen todentamiseen paljastamatta sitä.


![Image](assets/en/019.webp)


**Turvallisuusvaikutukset**: Nonce:n uudelleenkäytöstä johtuvat merkittävät taloudelliset tappiot. Yksilöllisten tunnusten luomisen tärkeyden ymmärtäminen on ratkaisevan tärkeää. LibSecP256k1:n kaltaisten luotettavien kirjastojen käyttäminen takaa vankat ja turvalliset salausoperaatiot.


**Elliptic Curve Cryptography (ECC)**: Allekirjoitusjärjestelmät ovat kehittyneet identiteettiprotokollista Schnorrin allekirjoitusten kaltaisiin järjestelmiin, joita käytetään tällä hetkellä Bitcoin:ssä (BIP 340). Elliptisten käyrien ja äärellisten kenttien aritmetiikan tuntemus takaa turvalliset kryptografiset toteutukset.


**Yleisiä neuvoja kehittäjille**: Salausprotokollat on arvioitava perusteellisesti vertaisarvioinneissa. Kehittäjien on oltava tarkkoja ja ymmärrettävä kaikki kryptografisten menettelyjen vaiheet. Tietoisuus kryptografisten toteutusten yleisistä sudenkuopista voi ehkäistä merkittäviä haavoittuvuuksia.


**Elliptiset käyrät kryptografiassa**: Esimerkiksi julkisen avaimen muokkaaminen käyttämällä ylimääräistä yksityistä avainta ja varmistamalla samalla turvallisuus. Bitcoin:n erityinen elliptinen käyrä, SECP256K1, ja sen parametrit (P ja N) ovat perustavanlaatuisia sen toteutuksen kannalta.


#### Päätelmä


Tällä luennolla tutustuimme kryptografisiin peruskäsitteisiin, jotka ovat Bitcoin:n turvallisuuden ja toiminnallisuuden perustana. Hash-funktioiden, Merkle-puiden ja digitaalisten allekirjoitusten kriittisistä rooleista elliptisten käyrien kryptografian monimutkaiseen matematiikkaan nämä Elements muodostavat Bitcoin:n hajautetun verkon selkärangan. Näiden käsitteiden ymmärtämisessä ei ole kyse vain teorian ymmärtämisestä, vaan myös käytännön vaikutusten ja mahdollisten sudenkuoppien tunnistamisesta reaalimaailman kehityksessä.


Bitcoin:n kehittäjinä on tärkeää lähestyä salausteknisiä toteutuksia varovaisesti ja tarkasti. Bitcoin-verkon turvallisuus riippuu suuresti näiden salausperiaatteiden oikeasta ja turvallisesta soveltamisesta. Olitpa sitten vahvistamassa tapahtumia, suunnittelemassa uusia ominaisuuksia tai varmistamassa Blockchain:n eheyttä, syvällinen kryptografian tuntemus auttaa sinua rakentamaan vankempia, turvallisempia ja innovatiivisempia ratkaisuja Bitcoin-ekosysteemiin.


Kun hallitset nämä käsitteet ja noudatat parhaita käytäntöjä, sinulla on hyvät valmiudet osallistua tehokkaasti Bitcoin:n jatkuvaan kehittämiseen ja varmistaa sen kestävyys ja turvallisuus tulevaisuudessa.


## Bitcoin:n hallintomalli


<chapterId>a30ec3e7-b290-5145-a9a9-042224ab20d2</chapterId>

<professorId>7dfc5865-a0f6-4c3b-9b05-83e0d807ac59</professorId>


:::video id=91a38c17-5801-4a5c-baf2-c9e4cc24fd84:::

### Bitcoin:n luonne


Bitcoin on digitaalinen valuutta, joka toimii konsensusprotokollan eli verkon osallistujien hyväksymien sääntöjen avulla, joilla varmistetaan yhdenmukaisuus ja toimivuus. Ytimeltään Bitcoin on hajautettu Ledger, joka tunnetaan nimellä Blockchain, jossa verkon solmut tallentavat ja varmentavat transaktiot. Täydelliset solmut, jotka tallentavat Bitcoin Blockchain:n koko historian, ovat ratkaisevassa asemassa tämän Ledger:n eheyden ylläpitämisessä. Myös muuntyyppiset solmut, kuten arkistointisolmut, pruned-solmut ja SPV-solmut (Simplified Payment Verification), osallistuvat verkon toimintaan eri tavoin. Konsensusprotokolla varmistaa, että kaikki nämä solmut ovat yhtä mieltä Blockchain:n tilasta, mikä tekee Bitcoin:stä vankan sensuuria ja petoksia vastaan.


#### Muutosten estäminen


Bitcoin:n hallinto on elintärkeää, jotta voidaan estää mielivaltaiset tai ilkivaltaiset muutokset protokollaan. Tämä saavutetaan konsensusmekanismilla, joka edellyttää yhteisön laajaa yhteisymmärrystä. Ohjelmointiosaamista omaavilla kehittäjillä on merkittävä rooli muutosten ehdottamisessa, mutta näiden muutosten on oltava laajemman yhteisön hyväksymiä, jotta ne voidaan toteuttaa.


Bitcoin core:llä ja vaihtoehtoisilla toteutuksilla on ylläpitäjät, jotka valvovat ohjelmiston kehittämistä ja ylläpitoa. Nämä ylläpitäjät vastaavat koodimuutosten yhdistämisestä ja varmistavat, että ne noudattavat konsensussääntöjä eivätkä aiheuta haavoittuvuuksia.


#### Soft haarukat vs Hard haarukat


Soft-haarat ovat muutoksia, jotka tiukentavat Bitcoin-protokollan nykyisiä sääntöjä ja tekevät joistakin aiemmin voimassa olleista tapahtumista pätemättömiä. Ne ovat taaksepäin yhteensopivia, mikä tarkoittaa, että päivittämättömät solmut tunnistavat edelleen uudet säännöt. Esimerkki Soft Fork:sta on vuonna 2010 tehty korjaus ylivuotovirheeseen, joka esti rahan luomisen tyhjästä.


Hard-haarat ovat muutoksia, jotka löysäävät nykyisiä sääntöjä ja mahdollistavat uudenlaisia transaktioita. Ne eivät ole taaksepäin yhteensopivia, mikä tarkoittaa, että päivittämättömät solmut eivät tunnista uusia sääntöjä. Esimerkki Hard Fork:stä saattaisi olla tarpeen vuoden 2106 ongelmaa varten, jotta voidaan varmistaa Bitcoin:n toiminnan jatkuminen tämän päivämäärän jälkeen.


![Image](assets/en/020.webp)


![Image](assets/en/021.webp)


### Esimerkkejä hallintotavasta


Useat käytännön esimerkit havainnollistavat Bitcoin:n hallintotapaa käytännössä. Vuonna 2010 tehty ylivuotovirheen korjaus oli Soft Fork, jolla korjattiin kriittinen virhe. Vuoden 2106 ongelma vaatii todennäköisesti Hard Fork:n Address:n, jotta sen vaikutukset voidaan korjata. Siirtyminen pisimmästä ketjusta eniten työtä tekevään ketjuun kuvastaa merkittävää hallintopäätöstä, joka vaikutti siihen, miten konsensus saavutetaan.


Bitcoin:n hallinnossa otetaan huomioon myös protokollan käytössä tapahtuneet todelliset muutokset. Esimerkiksi ordinaalien ja merkintöjen käyttöönotto havainnollistaa, miten protokollan muutokset voivat epäonnistua tapahtumien sensuroinnissa. Vastaavasti Full RBF:n (Replace-by-fee) toteuttaminen muutti transaktioiden korvausmenettelyjä muuttamatta konsensussääntöjä.


#### Muutoksen ja konsensuksen motiivit


Bitcoin:een tehtäviin muutoksiin voi olla erilaisia syitä, kuten kriittisten virheiden korjaaminen, uusien ominaisuuksien käyttöönotto tai muutosten rajoittaminen taloudellisista tai poliittisista syistä. Nämä motiivit johtavat usein yhteisön sisällä keskusteluihin siitä, mikä on vika ja mikä ominaisuus ja mikä on kokonaisvaikutus verkkoon.


Bitcoin:n konsensusmekanismi tekee siitä luonnostaan poliittisen, sillä se edellyttää laajaa yhteisymmärrystä, jotta muutokset voidaan hyväksyä. Tämä poliittinen näkökulma on ratkaisevan tärkeä, jotta voidaan säilyttää verkon hajautettu luonne ja varmistaa, että muutokset ovat yhteisön edun mukaisia.


Käynnissä olevat solmut voivat validoida Bitcoin-säännöt ja osallistua verkkoon myös erilaisilla viestintäprotokollilla, kuten Blockstream Satellite. Tämä korostaa Bitcoin:n konsensusmekanismin ja verkon käyttämien tiedonsiirtomenetelmien erottamista toisistaan. Solmujen taloudellinen merkitys, erityisesti Binance-yhtiön kaltaisten suurten yksiköiden ylläpitämien solmujen, voi vaikuttaa muutosten hyväksymiseen. Näillä yhteisöillä on merkittäviä taloudellisia etuja verkossa, ja ne voivat vaikuttaa päätöksiin pyörittämällä vaikutusvaltaisia solmuja.


### Lohkokokokeskustelu


Lohkokokokeskustelu oli merkittävä hallintokysymys, joka koski sitä, pitäisikö Bitcoin:n lohkokokoa kasvattaa. Tämä kiista ratkaistiin toteuttamalla SegWit, Soft Fork, joka kasvatti tehokasta lohkokokoa ja mahdollisti Lightning Network:n käytön.


![Image](assets/en/022.webp)


### Pakkomuutokset ja enemmistösääntö


Bitcoin:n kehittäjiä on yritetty oikeudellisesti pakottaa muuttamaan Blockchain-sääntöjä henkilökohtaisen edun vuoksi, kuten Craig Wrightin nostamassa kanteessa. Nämä yritykset korostavat Bitcoin-hallintaan liittyviä haasteita ja eettisiä näkökohtia.


Bitcoin:ssa enemmistösäännöllä on tärkeä rooli. Jos 60 prosenttia louhijoista hyväksyy uuden säännön, alkuperäistä Bitcoin core:tä käyttävät louhijat hylkäävät heidän lohkonsa, mikä johtaa jakoon. Esimerkki yhteisön tuen puutteesta johtuvasta epäonnistuneesta Hard Fork:stä on Bitcoin Satoshi:n visio (BSV).


Käydään lyhyesti läpi joitakin tärkeitä käsitteitä.


**Pakotettu Soft Fork**: Bitcoin:n muuttamista koskevien rajoittavien sääntöjen käyttöönotto voi johtaa uusiin hajaannuksiin ja hallintokysymyksiin. Tämä lähestymistapa havainnollistaa Bitcoin-yhteisön monimutkaisuutta ja mahdollisia ristiriitoja.


**51% hyökkäys**: 51 prosentin hyökkäys kuvaa skenaariota, jossa suurin osa hashing-tehosta voisi hyökätä Bitcoin:n ja Mining:n tyhjiin lohkoihin. Tämä voisi käytännössä tappaa verkon, ellei yhteisö hyväksy uusia konsensussääntöjä Address hyökkäyksen torjumiseksi.


**Check-Lock-Time-Verify (CLTV)**: Check-Lock-Time-Verify (CLTV) on esimerkki hallintomuutoksesta, joka on toteutettu Soft Fork:nä. CLTV varmistaa, että tapahtumat ovat voimassa vasta tietyn ajan kuluttua, mikä on hyödyllistä maksukanavien ja vara-avainten kannalta. Tällä muutoksella tiukennettiin sääntöjä käyttämällä op-koodia, joka ei aiemmin tehnyt mitään.


Yhteenvetona voidaan todeta, että Bitcoin:n tulevaisuus ja muutokset määräytyvät sen käyttäjien yhteisen tahdon mukaan. Merkittävät muutokset edellyttävät laajaa yksimielisyyttä, mikä kuvastaa Bitcoin:n hallinnon hajautettua ja poliittista luonnetta.


## Bitcoin Mining Perusteet


<chapterId>a4eacfc3-7b37-5fa3-abd1-b1fc48b645f0</chapterId>

<professorId>e320ccda-be59-492b-a81b-243d9acb592f</professorId>


:::video id=161d074d-4a81-48da-b2c9-9bde041a0da5:::

#### Johdanto


Ajelex keskittyy Bitcoin Mining:n liiketoiminnallisiin näkökohtiin ja tarkastelee strategioita kannattavuuden säilyttämiseksi kilpailluilla markkinoilla. Keskusteluun sisältyy analyysi toimintakustannuksista, tehostamistoimenpiteistä ja Mining-teollisuutta ohjaavista taloudellisista tekijöistä.


### 1. Mining monimutkaisuus ja kannattavuustekijät


#### Tekniset ja strategiset tekijät


Mining monimutkaisuus Bitcoin yhteydessä tarkoittaa ensisijaisesti teknisiä ja strategisia Elements tekijöitä, jotka määrittävät Mining toiminnan kannattavuuden. On ratkaisevan tärkeää ymmärtää, että Mining ei ole pelkkää onnenpeliä vaan monimutkainen prosessi, joka vaatii huolellista suunnittelua ja jatkuvaa optimointia.


#### Keskeiset kannattavuustekijät


![energy cost](assets/en/056.webp)


1. **Sähkökustannukset**: Yksi merkittävimmistä Mining:n kannattavuuteen vaikuttavista tekijöistä on sähkön hinta. Ranskan kaltaisilla alueilla sähkö voi olla suhteellisen kallista verrattuna El Salvadorin kaltaisiin maihin, joissa alhaisemmat kustannukset tarjoavat kaivostoiminnan harjoittajille kilpailuetua.

2. **Hardware-tehokkuus**: Mining-laitteiston tehokkuus, jota mitataan Hash-nopeudella ja virrankulutuksella, on ratkaisevassa asemassa. Kehittyneet ASIC-kaivurit, kuten S19J Pro, ovat paljon tehokkaampia kuin vanhemmat mallit, kuten Antminer S9.

3. **Ajanjakso**: Bitcoin Mining kannustaa pitkän aikavälin suunnitteluun.

4. **BTC-hinta**: Mining:n kannattavuuden määrittämisessä on olennaista BTC-hinta.

5. **Verkon vaikeus**: Hashrate:n määrä, joka tarvitaan keskimäärin lohkon louhimiseen 10 minuutissa.

6. **Strategiset työkalut**: [braiins.com](https://insights.braiins.com) kaltaiset työkalut ovat korvaamattomia kannattavuuden laskemisessa ja auttavat kaivostyöntekijöitä tekemään tietoon perustuvia päätöksiä.


#### Käytännön soveltaminen


 Tämä esimerkki korostaa Mining-toimintojen integroimisen käytännöllisyyttä jokapäiväiseen elämään, mikä tuo lisähyötyjä.


#### Mining:n pullonkaulat


Kaivostoiminnan harjoittajilla on kolme ensisijaista pullonkaulaa: laitteistojen saatavuus, energian saatavuus ja toiminnan ylläpitämiseen tarvittava pääoma. Suuren kysynnän aiheuttama ASIC-piirien niukkuus johtaa usein pitkiin odotusaikoihin ja kohonneisiin hintoihin, mikä vaikeuttaa Mining-maisemaa entisestään.



- Esimerkki **energian pullonkaulasta**.

Vuonna 2021 Kiinan hallitus kielsi Mining:n käytön alueellaan, minkä vuoksi Mining-yritykset Kiinassa menettivät energiansaannin. Tämä johti Hashrate:n **50 prosentin** laskuun kahdessa viikossa.


![hashrate drop](assets/en/057.webp)


---

### 2. Mining-laitteiston kehitys ja tehokkuus


#### Historiallinen kehitys


Mining-laitteiston matka on ollut monumentaalinen, alkaen yksinkertaisesta CPU Mining:sta nykyisin käyttämiimme erittäin erikoistuneisiin ASIC-kaivoksiin.


![evolution hardware](assets/en/058.webp)


1. **CPU Mining**: Mining suoritettiin alkuaikoina tavallisilla tietokoneprosessoreilla (CPU). Tämä menetelmä oli nopeasti ohi, kun verkko kasvoi.

2. **GPU Mining**: Grafiikkasuorittimet (GPU) lisäsivät Mining:n tehokkuutta merkittävästi, mikä teki suorittimista tarpeettomia Mining:n kannalta.

3. **FPGA Mining**: Kenttäohjelmoitavat porttiryhmät (FPGA) tarjosivat vielä parempaa suorituskykyä ja energiatehokkuutta kuin näytönohjaimet.

4. **ASIC Mining**: Sovelluskohtaiset integroidut piirit (ASIC) edustavat Mining-laitteiston tehokkuuden huippua, ja ne on suunniteltu erityisesti Mining-toimintoja varten, joiden suorituskyky on vertaansa vailla.


#### Yksityiskohtainen vertailu: S19J Pro vs. Antminer S9



- S19J Pro**: S19J Pro on tunnettu korkeasta tehokkuudestaan ja luotettavuudestaan, ja se tarjoaa ylivoimaisen Hash-nopeuden alhaisemmalla virrankulutuksella, joten se sopii erinomaisesti laajamittaisiin toimintoihin.
- Antminer S9**: Vaikka Antminer S9 on vanhempi ja tehottomampi, se on edelleen suosittu pienempien kokoonpanojen ja harrastajien keskuudessa edullisuutensa ja kohtuullisen suorituskykynsä ansiosta.


![s19j pro vs antminer s9](assets/en/059.webp)


#### Mining tehokkuus ja oppiminen


Mining ei tarjoa ainoastaan taloudellisia palkkioita vaan myös arvokasta käytännön kokemusta. KYC-vapaiden bitcoinien hankkiminen Mining:n kautta voi olla houkutteleva ehdotus niille, jotka ovat huolissaan yksityisyydestä.


#### Edistyneet työkalut ja tekniikat


Jälkiohjelmistot voivat parantaa Mining-laitteiston tehokkuutta ja toimivuutta. Optimointi- ja automaattiviritysominaisuuksia tarjoavat työkalut varmistavat, että jokainen siru toimii mahdollisimman tehokkaasti ja tasapainottaa Hash-taajuuden ja virrankulutuksen tehokkaasti.


---

### 3. Mining-toiminnan sääntely- ja markkinadynamiikka


#### Sääntelyn vaikutus


Sääntelyllä on merkittävä rooli Mining:n maiseman muokkaamisessa. Esimerkiksi Kiinan Mining-kiellolla oli syvällisiä vaikutuksia maailmanlaajuisiin Mining-toimintoihin, sillä se aiheutti merkittävän laskun Hash-verkon käyttöasteessa ja johti Mining-tehon uudelleenjakoon eri alueiden välillä.


#### Markkinoiden dynamiikka


1. **Laitteiston saatavuus ja hinta**: Bitcoin:n markkinahinta vaikuttaa ASIC:n louhinten hintaan ja saatavuuteen. Suuri kysyntä noususuhdanteiden aikana johtaa niukkuuteen ja paisuneisiin hintoihin.

2. **Hash arvo ja Hash hinta**: Hash-arvon (terahashia kohti päivässä ansaitut satoshit) ja Hash-hinnan (Hash-kurssin rahallinen arvo) välisen eron ymmärtäminen on olennaista. Molempiin vaikuttavat verkon vaikeudet ja Bitcoin:n markkinahinta.


#### Mining-altaat ja palkitsemismekanismit


1. **Mining allas**: Yhdistämällä resursseja Mining-poolit tarjoavat vakaammat palkinnot, mikä vähentää yksin pelattavaan Mining:een liittyvää vaihtelua ja riskiä.

2. **Palkkiojärjestelmät**: Erilaiset palkitsemismekanismit, kuten Pay-Per-Share (PPS) ja suhteelliset palkkiot, tarjoavat erilaisia riski- ja palkitsemisprofiileja louhijoille.



   - Osakekohtainen palkka**: Pay-Per-Share palkitsee louhijat jokaisesta lähettämästään kelvollisesta osakkeesta riippumatta siitä, löytääkö pooli lohkon. **Sharet** ovat todisteyksiköitä siitä, että louhijat ovat tehneet vaaditun työn, ja pool tarkistaa nämä osakkeet.


![pps](assets/en/060.webp)



   - Suhteellinen**: Se riippuu lohkon Mining poolista, jaetaanko palkkio tasan sen mukaan, kuinka paljon Miner on osallistunut poolin Hashrate kokonaismäärään.


![prop](assets/en/061.webp)


#### Mining:n tulevaisuus


Kun lohkopalkkiot vähenevät, louhijat turvautuvat yhä enemmän transaktiomaksuihin. Tämä muutos herättää huolta siitä, ovatko pelkät transaktiopalkkiot riittäviä kannustimia louhijoille jatkaa verkon turvaamista.


#### Isännöity Mining


Isännöidyt Mining-palvelut voivat tarjota alhaisempia käyttökustannuksia, mutta niihin liittyy riskejä, kuten valvonnan puute ja petosvaara. Näiden riskien vähentäminen edellyttää asianmukaista huolellisuutta.


#### Turvallisuus ja tehokkuus


Kehittyneet turvallisuusprotokollat ja uusiutuvan energian käyttö eivät ainoastaan paranna kannattavuutta, vaan edistävät myös Mining-ekosysteemin kestävää kasvua.


Yhteenvetona voidaan todeta, että Bitcoin Mining on monimutkainen ja monitahoinen alue, joka edellyttää teknisten, strategisten, lainsäädännöllisten ja markkinadynamiikan syvällistä ymmärtämistä. Olitpa sitten kokenut Miner tai vasta aloittelija, tiedon ja sopeutumiskyvyn säilyttäminen on avainasemassa menestyäksesi tällä jatkuvasti kehittyvällä alalla. Kiitos huomiostanne, ja odotan mielenkiinnolla kysymyksiä ja keskusteluja.



# Layer Yksi käsite


<partId>5300855f-e5e4-5bca-9afe-2397f7c76260</partId>


## Bitcoin:n solmukomponentit


<chapterId>75ea1d88-ee6f-5f98-af90-e4758c55e606</chapterId>

<professorId>6cfd206c-53b8-47a0-bbf4-44fd84e6ee1d</professorId>


:::video id=6fae79f6-da81-4870-927b-923bd1672176:::

Adam Gibson esittelee Bitcoin-solmun eri osat. Luvussa keskitytään kunkin komponentin rooliin verkon toimivuuden ja eheyden ylläpitämisessä. Hän keskittyy erityisesti siihen, miksi Bitcoin-solmua pitäisi käyttää, mitä Bitcoin-solmu tekee ja miten Bitcoin-solmun eri komponentit toimivat.


### Johdanto Bitcoin-solmuihin


Bitcoin-solmujen roolin ymmärtäminen on ratkaisevan tärkeää kaikille Bitcoin-verkkoon osallistuville. Bitcoin-solmun käyttäminen antaa käyttäjille mahdollisuuden validoida transaktioita, osallistua konsensukseen ja säilyttää yksityisyytensä hallinnassa. Tällä luennolla perehdytään siihen, miksi Bitcoin-solmun käyttäminen on hyödyllistä ja miten se edistää Bitcoin-verkon yleistä turvallisuutta ja hajauttamista.


### Miksi käyttää Bitcoin-solmua?


Bitcoin-solmun käyttäminen on tärkeää useista syistä:


1. **Varmennus**: Näin varmistat, että saamasi Bitcoin on pätevä ilman, että joudut turvautumaan kolmansiin osapuoliin.

2. **Konsensukseen osallistuminen**: Solmut ovat ratkaisevassa asemassa Bitcoin-verkon sääntöjen määrittelyssä, joten konsensukseen osallistuminen auttaa ylläpitämään Blockchain:n eheyttä ja turvallisuutta.

3. **Salaisuus ja valvonta**: Ne voivat vaarantaa yksityisyytesi seuraamalla transaktioitasi ja Wallet-saldoasi.


### Mitä Bitcoin-solmu tekee?



- Pitää luetteloa vertaisosaajista**: Solmujen on löydettävä muut verkon solmut ja muodostettava niihin yhteys Exchange-tietojen saamiseksi.
- Vastaanottaa ja lähettää kelvollisia tapahtumia ja lohkoja**: Bitcoin-solmut ovat vastuussa kelvollisten transaktioiden ja lohkojen välittämisestä verkossa.
- Säilyttää lohkojen ja raskaimman ketjun historiaa**: Solmut tallentavat oman kopionsa Blockchain:stä, jonka avulla ne voivat validoida transaktioiden ja lohkojen aitouden.
- Pitää yllä luetteloa pätevistä ehdokkaista; Mempool**: Solmujen on pidettävä luetteloa mahdollisista transaktioehdokkaista Mempool:ssa, jotta ne voidaan sisällyttää lohkoihin.


![nodes network](assets/en/023.webp)


**HUOMAUTUS**: Mempool on väliaikainen säilytysalue tapahtumille, jotka on validoitu mutta joita ei ole vielä sisällytetty lohkoon.


### Solmun komponentit


#### Bitcoin core-moduulit


![Bitcoin core modules](assets/en/024.webp)



- Vertaislöytö**: Vertaisten löytäminen on prosessi, jossa solmu löytää muita solmuja, joihin se voi muodostaa yhteyden.
- Validointimoottori**: Validointimoottori vastaa transaktioiden ja lohkojen pätevyyden tarkistamisesta verkon sääntöjen mukaisesti.
- RPC (etämenettelykutsu)**: Bitcoin core sisältää RPC Interface, jonka avulla ulkoiset sovellukset, kuten lompakot, voivat olla vuorovaikutuksessa solmun kanssa.
- Lohkojen ja ketjun tilan tallentaminen**: Bitcoin core voi tallentaa koko Blockchain:n tai ei, olipa kyseessä arkisto- tai pruned-solmu. Se tallentaa myös verkon nykyisen tilan (The UTXO set) levylle.


#### Mitä voimme poistaa?



- Miner**: Bitcoin: Useimmat Bitcoin-solmut eivät osallistu Mining:ään vaaditun suuren laskentatehon vuoksi.
- RPC (palvelin)**: Bitcoin core toteuttaa JSON-RPC Interface, jota voidaan käyttää komentoriviavustajan bitcoin-cli avulla.
- Wallet (disablewallet)**: Jos haluat käyttää ulkoista Wallet:ää, voit poistaa Wallet-toiminnon käytöstä Bitcoin core:ssa. Näin voit hallita yksityisiä avaimia erikseen.
- Mempool (blocksonly)**: Käyttäjille, jotka haluavat minimoida kaistanleveyden käytön, "blocksonly"-solmun käyttäminen voi olla ratkaisu, jossa solmu käsittelee vain lohkoja ja jättää transaktiot huomiotta.


### Ketjun tila


#### Missä kolikot ovat?


Kolikoita ei tallenneta osoitteisiin, vaan ne sijaitsevat UTXO:issa, jotka edustavat kaikkia transaktioiden tuotoksia, joita ei ole käytetty. Voit hakea nämä tiedot komennolla:


```Bash
bitcoin-cli gettxoutsetinfo
```


![utxoset info command](assets/en/025.webp)


Voimme tarkastaa, että Bitcoinien määrä on oikea.


#### Kunkin UTXO:n osalta ketjutila on:



- txid.
- Lähtöindeksi.
- Missä lohkossa UTXO on.
- Onko se kolikkopankki UTXO.


**TÄRKEÄÄ**: Transaktiot eivät ole sama asia kuin UTXO:t.


![Txs and UTXOs](assets/en/026.webp)


#### Mempool


Se on luettelo kussakin solmussa olevista vahvistamattomista transaktioista, joita kutsutaan ehdokas transaktioiksi. Tallennetaan RAM-muistiin nopeaa käyttöä varten, eikä se ole osa konsensusta.


#### Bitcoin-solmuja koskevat turvallisuusnäkökohdat


Bitcoin-solmua käytettäessä turvallisuus on ensiarvoisen tärkeää. Seuraavassa on muutamia keskeisiä huomioita, jotka on syytä pitää mielessä:


#### Keskittämisen välttäminen


Blockchain-tietojen hankkiminen yhdestä lähteestä, kuten kaikkien lohkojen lataaminen keskitetystä palvelimesta, aiheuttaa merkittäviä riskejä. Bitcoin:n hajautetun luonteen säilyttämiseksi solmujen olisi muodostettava yhteys useisiin vertaisverkkoihin ja validoitava saamansa tiedot.


#### Eristyshyökkäysten estäminen


Eristämishyökkäykset tapahtuvat, kun solmua huijataan muodostamaan yhteys rajoitettuun joukkoon vertaisverkkopalveluja, jolloin hyökkääjä voi syöttää solmulle vääriä tietoja. 


#### Vertaisyhteyksien hallinta


Solmujen on hallinnoitava vertaisyhteyksiään huolellisesti varmistaakseen, etteivät ne ole yhteydessä pahansuoviin toimijoihin. 


#### UTXO-sarjan merkitys


UTXO-sarja edustaa Bitcoin:n nykytilaa, ja siinä luetellaan kaikki käyttämättömät tapahtumatulosteet. Se on ratkaisevan tärkeä tapahtumien validoinnissa ja sen varmistamisessa, että kolikoita ei käytetä useammin kuin kerran. Tämän joukon pitäminen pienenä ja helposti saatavilla on tärkeää verkon tehokkuuden ylläpitämiseksi.


#### Päätelmä


Bitcoin-solmun ylläpitäminen on tehokas tapa osallistua Bitcoin-verkkoon, sillä se antaa sinulle mahdollisuuden todentaa transaktioita, ylläpitää yksityisyyttä ja edistää Blockchain:n turvallisuutta ja hajauttamista. Riippumatta siitä, valitsetko Full node:n tai muokkaat asetustasi karsimalla Blockchain:a tai poistamalla tiettyjä komponentteja käytöstä, Bitcoin-solmun ydintoimintojen ja turvallisuusnäkökohtien ymmärtäminen antaa sinulle mahdollisuuden tehdä tietoon perustuvia päätöksiä ja osallistua Bitcoin:n jatkuvaan kehitykseen.


## Bitcoin:n tietorakenteet


<chapterId>5ed314b1-8293-567d-bf03-730e8c9c774b</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=1790e5fb-33f5-4e0e-982e-41589cd02965:::

Tämän luennon päätavoitteena on opastaa sinua Bitcoin-lohkon jäsentämisprosessissa koodaamalla jäsentäjä Rust:lla. Tämä edellyttää Bitcoin-lohkojen ja transaktioiden rakenteen ymmärtämistä ja tarvittavan logiikan toteuttamista näiden tietojen poimimiseksi ja tulkitsemiseksi.


### Bitcoin-lohkojen ja transaktioiden jäsentäminen Rust:ssä


#### Parseerattavat komponentit


Bitcoin-lohkon analysoimiseksi sinun on keskityttävä seuraaviin osiin:


1. **Lohko-otsikko**

2. **Transaktiot lohkon sisällä**

3. **Transaktioiden tulot ja lähdöt**


#### Lohkon otsikkorakenne


Lohkootsikko on Bitcoin-lohkon kulmakivi, ja se sisältää seuraavat kentät:



- Versio**: Ilmoittaa lohkon version.
- Edellinen lohko**: Viittaus Blockchain:n edelliseen lohkoon.
- Merkle Root**: Hash: Hash, joka edustaa lohkon kaikkien transaktioiden yhteenlaskettua Hash:ta.
- Timestamp**: Aika, jolloin lohko louhittiin.
- Bits**: Kelvollisen lohkon tavoitekynnys Hash.
- Nonce**: Arvo, jota kaivostyöläiset säätävät saavuttaakseen Hash:n tavoitekynnyksen alapuolelle.
- Tapahtumien määrä**: Transaktioiden määrä lohkossa.


**Huomautus**: Vain ensimmäiset 80 tavua (jotka sisältävät lohkon otsikon) hashedataan Mining:n aikana.


![Block header structure](assets/en/027.webp)


#### Yksinkertaistukset


Pitääksemme esimerkkimme hallittavana:



- Keskitymme SegWit:ta edeltävien (legacy) lohkojen analysointiin, jolloin vältämme Segregated Witnessin tuoman monimutkaisuuden.
- Ohitamme Bitcoin-skriptikielen tietyt opcoodit ja keskitymme muutamaan, joita tarvitsemme koko lohkon analysoimiseksi.


#### Transaktiorakenne


Jokainen Bitcoin-lohkon tapahtuma sisältää seuraavat tiedot:



- Versio**: Tapahtuman versio.
- Tulojen määrä**: Tapahtuman syötteiden lukumäärä.
- Tulot**: Luettelo syötteistä.
  - Edellinen ulostulo (outpoint)**: Edellinen lähtöviite.
    - Hash**: Hash viitetyssä tapahtumassa.
    - Indeksi**: Tapahtuman tietyn tuotoksen indeksi, nimeltään "vout".
  - Käsikirjoituksen pituus**: Allekirjoituskäsikirjoituksen pituus.
  - Allekirjoituskäsikirjoitus**: Skripti tapahtuman valtuutuksen vahvistamiseksi.
  - Järjestys**: Lähettäjän määrittelemä tapahtumaversio.
- Lähtöjen määrä**: Tapahtuman ulostulojen lukumäärä.
- Lähdöt**: Sisältää Value ja ScriptPubKey.
  - Arvo**: Transaktion arvo.
  - PubKey-skriptin pituus**: PubKey-skriptin pituus.
  - PubKey script**: Sisältää julkisen avaimen, joka on asetelma tuotoksen vaatimista varten.
- Lukitusaika**: Osoittaa lohkon korkeuden tai Timestamp, jolla tämä tapahtuma voidaan sisällyttää lohkoon.


![Transaction structure](assets/en/028.webp)

![TxIn structure](assets/en/029.webp)

![Outpoint structure](assets/en/030.webp)

![TxOut structure](assets/en/031.webp)


#### Parsing-tekniikat


Rust:ssä voimme käyttää erilaisia tekniikoita näiden rakenteiden jäsentämiseen:



- Hyödynnä `from_le_bytes` Little Endian -tietojen lukemiseen.
- Toteuta mukautettu `parse`-ominaisuus käsittelemään eri rakenteiden jäsentämislogiikkaa.


```Rust
trait Parse: Sized {
fn parse(bytes: &[u8]) -> Result<(Self, &[u8]), Error>;
}
```



- Toteuta jäsentely yleisesti listoille ja tietyille tyypeille, kuten `VarInt`, `U32`, `U64` jne.


```Rust
impl Parse for i32 {
fn parse(bytes: &[u8]) -> Result<(Self, &[u8]), Error> {
let val = i32::from_le_bytes(bytes[0..4].try_into()?);
Ok((val, &bytes[4..]))
}
}
```


### Virheenkorjaus ja testaus


Varmistaaksemme, että jäsentäjämme toimii oikein:



- Vertaa jäsenneltyjä tietoja tunnettuihin lohkotietoihin (esim. Mempool.space).
- Tarkista, että analysoidut tapahtumien lukumäärät ja lohkotiedot vastaavat odotettuja arvoja.


### Erikoistapausten käsittely ja komentosarjan jäsentäminen


#### 'parse'-funktion toteutus


Toteutamme `parse`-funktion käsittelemään koko lohkon, mukaan lukien lohkon otsikko ja transaktiot. Tämä edellyttää lohkon tietojen lukemista ja asiaankuuluvien kenttien poimimista.


```Rust
impl Parse for Block {
fn parse(bytes: &[u8]) -> Result<(Self, &[u8]), Error> {
let (header, bytes) = Parse::parse(bytes)?;
let (transactions, bytes) = Parse::parse(bytes)?;

let block = Block {
header, transactions
};

Ok((block, bytes))
}
}
```


#### Lohkootsikon muuttaminen


Meidän on mukautettava jäsentämislogiikkaamme, jotta voimme poistaa transaktioiden lukumäärän lohkon otsikkorakenteesta ja käsitellä sitä erillisenä kokonaisuutena.


```Rust
impl Parse for BlockHeader {
fn parse(bytes: &[u8]) -> Result<(Self, &[u8]), Error> {
let (version, bytes) = Parse::parse(bytes)?;
let (prev_block, bytes) = Parse::parse(bytes)?;
let (merkle_root, bytes) = Parse::parse(bytes)?;
let (timestamp, bytes) = Parse::parse(bytes)?;
let (bits, bytes) = Parse::parse(bytes)?;
let (nonce, bytes) = Parse::parse(bytes)?;

let header = BlockHeader {
version, prev_block, merkle_root, timestamp, bits, nonce,
};

Ok((header, bytes))
}
}
```


#### Rakenteen määritelmä


Määritä uusi rakenne `Block`, joka sisältää sekä lohkootsikon että luettelon tapahtumista.


```Rust
struct Block {
header: BlockHeader,
transactions: Vec<Transaction>,
}
```


#### Rust syntaksi Elements


Otetaan käyttöön Rust-syntaksi Elements, kuten kysymysmerkki (`?`) virheiden käsittelyä varten. Tämä yksinkertaistaa koodia ja tekee siitä luettavampaa.


#### Väitteet


Lisää väitteitä, joilla varmistetaan, että koko lohkon käsittelyn jälkeen ei jätetä tavuja käsittelemättä. Tämä varmistaa jäsentelyprosessin eheyden.


#### Erikoistapaukset, kuten coinbase-tapahtumat


Coinbase-tapahtumilla, jotka ovat ensimmäinen tapahtuma lohkossa, jota käytetään Block reward:n lunastamiseen, on ainutlaatuisia ominaisuuksia. Meidän on käsiteltävä nämä erityistapaukset asianmukaisesti.


```Rust
struct OutPoint {
txid: [u8; 32],
vout: u32,
}

impl OutPoint {
fn is_coinbase(&self) -> bool {
self.txid == [0; 32] && self.vout == 0xFFFFFFFF
}
}
```


#### Käsikirjoituksen jäsentämisstrategia


Jotta voimme analysoida skriptin transaktioissa, keskitymme yleisiin op-koodeihin, kuten `OP_CHECKSIG`, `OP_HASH160` ja `OP_PUSH`. Näiden skriptien jäsentäminen on ratkaisevan tärkeää transaktioiden validoinnin ja virheiden käsittelyn kannalta.


```Rust
enum OpCode {
False,
Return,
Dup,
Equal,
CheckSig,
Hash160,
EqualVerify,
Push(Vec<u8>),
}

impl Parse for OpCode {
fn parse(bytes: &[u8]) -> Result<(Self, &[u8]), Error> {
match bytes[0] {
v @ 1..=75 => {
let data = bytes[1..(v as usize + 1)].iter().cloned().collect();
Ok((OpCode::Push(data), &bytes[(v as usize + 1)..]))
},
76 => {
let len = bytes[1] as usize;
let data = bytes[2..(len + 2)].iter().cloned().collect();
Ok((OpCode::Push(data), &bytes[(len + 2)..]))
},

0 => Ok((OpCode::False, &bytes[1..])),

106 => Ok((OpCode::Return, &bytes[1..])),
118 => Ok((OpCode::Dup, &bytes[1..])),
135 => Ok((OpCode::Equal, &bytes[1..])),

136 => Ok((OpCode::EqualVerify, &bytes[1..])),
169 => Ok((OpCode::Hash160, &bytes[1..])),
172 => Ok((OpCode::CheckSig, &bytes[1..])),

_ => todo!()
}
}
}
```


![op_checksig](assets/en/032.webp)

![op_hash160](assets/en/033.webp)

![op_push](assets/en/034.webp)


#### Skriptien jäsentämiseen liittyvät haasteet


Skriptien jäsentäminen voi aiheuttaa haasteita erityisesti coinbase-tapahtumien kanssa. On tärkeää ottaa huomioon ääripäätapaukset ja käsitellä ne oikein tarkan jäsennyksen varmistamiseksi.


```Rust
impl Parse for Script {
fn parse(bytes: &[u8]) -> Result<(Self, &[u8]), Error> {
let (len, bytes) = VarInt::parse(bytes)?;
let mut script_bytes = &bytes[..len.0 as usize];
let mut opcodes = Vec::new();
while !script_bytes.is_empty() {
let (opcode, bytes) = OpCode::parse(script_bytes)?;
script_bytes = bytes;
opcodes.push(opcode);
}

Ok((Script(opcodes), &bytes[len.0 as usize..]))
}
}
```


#### Kompaktit lohkot


Kompaktilohkojen käyttöä käytetään nykyisin solmujen välisen tiedonsiirron tehostamiseen. Tämä vähentää kaistanleveyden käyttöä ja nopeuttaa synkronointia lähettämällä Mempool:sta puuttuvat transaktiot, täyttämällä ne transaktiolla, joka solmulla oli jo lohkossa, ja validoimalla se sitten.


#### Olemassa olevien kirjastojen käyttö


Konsensuskriittisissä sovelluksissa on suositeltavaa käyttää olemassa olevia kirjastoja virheiden välttämiseksi ja turvallisuuden varmistamiseksi, kuten [Rust-Bitcoin](https://docs.rs/Bitcoin/latest/Bitcoin/) tai [Bitcoin-dev-kit](https://docs.rs/BDK/latest/BDK/). Oman jäsentimen toteuttaminen voi olla opettavaista mutta myös riskialtista tuotantoympäristöissä.


![libraries](assets/en/035.webp)


### Tehokkuus ja turvallisuus Bitcoin:ssa Mining:ssa


#### Tehokkuus Mining:ssä


Mining tyhjät lohkot voivat olla tehokkaampia louhijoille:



- Louhijat aloittavat Mining:n tyhjillä lohkoilla ajan säästämiseksi.
- Tyhjiä lohkoja voidaan louhia nopeasti ennen kuin siirrytään täyteen lohkoon, kun edellinen lohko on vahvistettu.


#### Mining tyhjien lohkojen syyt


Tyhjiä lohkoja louhitaan joskus ajoitusongelmien vuoksi. Louhijat eivät ehkä ole saaneet täydellistä transaktioluetteloa, kun he aloittavat Mining:n seuraavan lohkon louhinnan, joten he päättävät louhia tyhjän lohkon sen sijaan.


![empty block](assets/en/036.webp)


#### Tyhjien lohkojen haitallinen Mining


Vaikka tyhjien lohkojen Mining vahingoittaminen on mahdollista, sitä ei ole havaittu. Tyhjien lohkojen ensisijainen syy on pikemminkin ajoitusrajoitus kuin ilkivalta.


#### Tyhjien lohkojen vaikutukset


Tyhjien lohkojen esiintyminen on normaali osa Mining-prosessia, ja se johtuu pääasiassa ajoitusongelmista. Vaikka ne eivät sisällä transaktioita, ne kuitenkin laajentavat Blockchain:tä ja edistävät verkon turvallisuutta.


#### Turvallisuuden merkitys


Bitcoin Mining:n turvallisuus on ensiarvoisen tärkeää. Noudattamalla parhaita käytäntöjä ja käyttämällä hyvin testattuja kirjastoja louhijat ja kehittäjät voivat varmistaa Blockchain:n eheyden ja suojautua mahdollisilta haavoittuvuuksilta.


Johtopäätöksenä voidaan todeta, että Bitcoin-lohkojen ja Rust:n transaktioiden jäsentäminen edellyttää monimutkaisten rakenteiden ymmärtämistä ja tehokkaiden jäsentämistekniikoiden toteuttamista. Erikoistapausten ja skriptien jäsentäminen vaatii huolellista harkintaa, ja keskittymällä tehokkuuteen ja turvallisuuteen varmistetaan Bitcoin-verkon kestävyys.


## Bitcoin-ohjelmiston yleiskatsaus ja solmutoteutukset


<chapterId>96d64781-fc27-5209-88d8-2acf00d05ea8</chapterId>

<professorId>0b05838c-24af-43ff-93be-896c907e0bc1</professorId>


:::video id=1d148008-9197-446f-afb5-628d4c3a5015:::

Daniela Brozzoni tarjoaa kattavan yleiskatsauksen Bitcoin Layer 1 -ohjelmistopinoon ja selittää kerrokset, jotka muodostavat Bitcoin-protokollan perustan (eli Bitcoin-solmut ja Bitcoin-lompakot), ja miten Bitcoin-ohjelmistoja rakennetaan Bitcoin-kirjastojen esittelyn ja Bitcoin Development Kitin (BDK) syväsukelluksen avulla.


### Bitcoin-ohjelmiston yleiskatsaus


Bitcoin:n ohjelmistopino on sen toiminnan kannalta olennainen, ja se koostuu erilaisista Elements:sta, kuten solmuista ja lompakoista. Kriittinen osa tätä ekosysteemiä on Bitcoin Development Kit (BDK), johon tutustumme yksityiskohtaisesti myöhemmin. Keskitytään ensin solmujen rooliin Bitcoin-verkossa.


#### Bitcoin solmut


Bitcoin-solmut muodostavat Bitcoin-verkon runkoverkon. Ne muodostavat yhteyden toisiinsa, Exchange-tapahtumiin ja -lohkoihin ja validoivat saapuvat tiedot. Solmuja on erityyppisiä, ja jokaisella on oma tarkoituksensa:



- Täydet solmut**: Nämä solmut tallentavat koko Blockchain:n ja validoivat kaikki transaktiot ja lohkot. Ne tarjoavat korkean turvallisuustason ja ovat välttämättömiä verkon hajauttamisen kannalta.



  - Arkistosolmut**: Arkistointisolmut säilyttävät kaikki Blockchain-tiedot, joten ne ovat arvokkaita historiallisen analyysin ja virheenkorjauksen kannalta.


![archival node](assets/en/037.webp)



  - pruned-solmut**: pruned-solmut säästävät levytilaa säilyttämällä vain osan Blockchain:stä ja poistamalla vanhemmat tiedot, joita ei enää tarvita validointiin.


![pruned node](assets/en/038.webp)


#### Bitcoin core


Bitcoin core on yleisimmin käytetty Full node-toteutus. Se toimii sekä Full node:nä että Wallet:na. Bitcoin core:n keskeisiä piirteitä ovat seuraavat:



- Käytettävyys**: Interface (CLI) ja graafisen käyttäjän Interface (GUI) kautta.
- Avoimen lähdekoodin luonne**: Koodi on avointa lähdekoodia, joten kehittäjät voivat osallistua ja tutkia sen toimintaa.
- Kieli**: Kirjoitettu C++-kielellä ja testit Python-kielellä, mikä takaa vankan suorituskyvyn ja luotettavuuden.


![cli-gui](assets/en/039.webp)


##### Bitcoin core:n tutkiminen


Bitcoin core:stä voi saada käytännön kokemusta kääntämällä ja suorittamalla testejä Gitin avulla. Tähän prosessiin kuuluu:



- Koodikannan kääntäminen suoritettavan version luomiseksi. [Bitcoin github](https://github.com/Bitcoin/Bitcoin) ohjeet löytyvät doc/build-\*.md:stä.


```Bash
./autogen.sh
./configure
make # use "-j N" for N parallel jobs
make install # optional
```



- Testien suorittaminen sen varmistamiseksi, että kaikki toimii oikein. Ohjeet löytyvät [täältä](https://github.com/Bitcoin/Bitcoin/blob/master/test/README.md)


```Bash
make check

#individual tests can be run directly calling the test script e.g:
test/functional/feature_rbf.py

#run all possible tests
test/functional/test_runner.py
```



- Testin luominen ja suorittaminen Pythonilla tietyn toiminnallisuuden validoimiseksi. Tiedosto [example.py](https://github.com/Bitcoin/Bitcoin/blob/master/test/functional/example_test.py) on vahvasti kommentoitu esimerkki testitapauksesta, jossa käytetään sekä RPC- että P2P-rajapintoja.


#### Vaihtoehtoiset solmutoteutukset


Bitcoin core:n lisäksi on olemassa useita vaihtoehtoisia solmutoteutuksia:



- Bitcoin Knots**: Bitcoin core: Se tarjoaa kehittyneempiä ominaisuuksia kuin Bitcoin core ja vie enemmän tilaa ja muistia.
- LibBitcoin**: Joustava ja modulaarinen toteutus.
- btcd**: Se on kirjoitettu Go-kielellä ja tarjoaa erilaisia suunnittelufilosofioita.


Näiden vaihtoehtojen toteuttamiseen liittyy omat riskinsä, erityisesti konsensussääntöjen osalta. Vakiintuneista validointisäännöistä poikkeaminen voi johtaa haarautumisiin tai epäjohdonmukaisuuksiin. Bitcoin Kernel -hankkeessa näitä riskejä pyritään pienentämään keskittämällä konsensuskoodia ja varmistamalla yhdenmukaisuus kaikissa toteutuksissa.


![implementation](assets/en/040.webp)


### Bitcoin lompakot ja turvallisuus


Bitcoin-lompakot ovat ratkaisevan tärkeitä Bitcoin-varantojesi turvallisen hallinnan kannalta. Niitä on eri muodoissaan, ja jokaisella on omat ominaisuutensa ja turvallisuusnäkökohtansa.


#### Bitcoin-lompakoiden tyypit


1. **Säilyttäjä vs. ei-säilyttäjä**:



   - Säilytyslompakot**: Kolmannen osapuolen hallinnoimat, tarjoavat mukavuutta, mutta edellyttävät luottamusta säilyttäjään.
   - Muut kuin säilytysyhteisön lompakot**: Käyttäjien hallinnassa, mikä tarjoaa korkeamman turvallisuuden ja yksityisyyden suojan.


2. **Desktop vs. mobiili**:



   - Työpöytälompakot**: Tyypillisesti monipuolisempia ja turvallisempia.
   - Mobiililompakot**: Tarjoavat mukavuutta ja siirrettävyyttä.


3. **On-Chain vs. salama**:



   - On-Chain-lompakot**: Bitcoin Blockchain.
   - Salamalompakot**: off-chain.


4. **Cold-lompakot vs. Hot-lompakot**:


   - Cold-lompakot**: Ei yhteyttä internetiin, mikä tarjoaa erinomaisen suojan hakkerointia vastaan.
   - Hot-lompakot**: Yhdistetty internetiin, joka tarjoaa paremman saatavuuden mutta vähemmän turvallisuutta.


#### Cold Wallet turvallisuus


Cold-lompakoita arvostetaan niiden turvallisuudesta. Koska ne pysyvät offline-tilassa, ne ovat luonnostaan vastustuskykyisiä verkkohakkereita vastaan. On kuitenkin erittäin tärkeää varmistaa, että Cold-lompakoiden kautta suoritettavat maksutapahtumat ovat turvallisia ja tarkkoja, jotta Bitcoin:ää ei vahingossa lähetetä pahansuoville toimijoille.


#### Vain kelloa käyttävät lompakot


Vain kelloa käyttävät lompakot sisältävät vain julkisia avaimia, joten käyttäjät voivat vastaanottaa Bitcoin:n ja seurata saldoaan ilman, että he voivat käyttää rahaa. Tämä ominaisuus lisää Layer-turvallisuutta niille, joiden on pidettävä omistuksiaan tarkasti silmällä.


#### Bitcoin Wallet:n perustoiminnot


Tyypistä riippumatta jokaisella Bitcoin Wallet:llä on kolme perustoimintoa:


1. **Vastaanota Bitcoin**: generate-osoitteet ja seurata saapuvia tapahtumia.

2. **lähettää Bitcoin**: Luo ja lähetä tapahtumia verkkoon.

3. **Näyttötasapaino**: Näyttää Wallet:n nykyisen saldon.


#### Bitcoin-lompakoiden rooli



- Bitcoin-lompakot toimivat avainketjuina, joissa säilytetään ja luodaan salausavaimia.


![keychain](assets/en/041.webp)



- Ne tarkkailevat Blockchain:n saapuvia tapahtumia.


![monitor](assets/en/042.webp)



- Luo tapahtumia valitsemalla käyttämättömät tapahtumalähdöt (UTXO), asettamalla tulot ja lähdöt sekä optimoimalla yksityisyyden suoja ja maksut.


![tx_builder](assets/en/043.webp)


#### Wallet-logiikan uudelleenkäytettävyys


Koska kaikilla Bitcoin-lompakoilla on samankaltaisia toimintoja, Wallet-logiikan toistuva uudelleenkirjoittaminen on tehotonta. Tässä kohtaa Bitcoin Development Kit (BDK) astuu kuvaan.


### Bitcoin-kehityssarja (BDK) ja tekniset konseptit


Bitcoin Development Kit (BDK) on kirjasto, joka on suunniteltu yksinkertaistamaan Bitcoin-lompakoiden luomista ja hallintaa.


#### BDK:n yleiskatsaus


BDK yksinkertaistaa Wallet:n luomista tarjoamalla korkeamman tason toimintoja, jotka on rakennettu Rust Bitcoin:n päälle. Se tukee useita ohjelmointikieliä, kuten Kotlinia, Swiftiä ja Pythonia, sidosten avulla.


#### Muut Bitcoin-kirjastot


Lukuisat Bitcoin-kirjastot sopivat eri ohjelmointikielille, kuten Python, JavaScript, Java, Go ja C. Nämä kirjastot tarjoavat monipuolisia työkaluja Bitcoin-kehitykseen.


#### Keskeiset tekniset käsitteet


1. **Descriptors**: Kuvaajat kuvaavat, miten Bitcoin-skriptit ja osoitteet johdetaan avaimista, mikä mahdollistaa joustavammat ja tehokkaammat Wallet-toiminnot.

2. **PSBT (Osittain allekirjoitetut Bitcoin-tapahtumat)**: PSBT on formaatti tapahtumille, jotka edellyttävät useita allekirjoituksia, mikä helpottaa yhteistoiminnallisia tapahtumia ja parantaa turvallisuutta.

3. **Rust-syntaksi**: Rust:n keskeiset käsitteet, kuten `Option` nollaturvallisuutta varten ja `Result`-tyyppi virheiden käsittelyä varten, ovat olennainen osa BDK:n ymmärtämistä ja tehokasta käyttöä.


#### Tapahtumien luominen ja hallinta


BDK tehostaa transaktioiden luomista, allekirjoittamista ja lähettämistä:


1. **Rakenna liiketoimet**: Määritä vastaanottajat, määrät ja maksut.

2. **Kirjoita liiketoimet**: Käytä PSBT:tä allekirjoitusten keräämiseen.

3. **Lähetystapahtumat**: Lähetä valmiit tapahtumat verkkoon.


#### Esimerkki työnkulusta BDK:ssa



- Aseta Wallet**: Wallet:n alustaminen kuvaajilla.


```Rust
use bdk::{Wallet, SyncOptions};
use bdk::database::MemoryDatabase;
use bdk::blockchain::ElectrumBlockchain;
use bdk::electrum_client::Client;
use bdk::bitcoin;

fn main() -> Result<(), bdk::Error> {
let wallet = Wallet::new(
"tr(tprv8ZgxMBicQKsPf6WJ1Rr8Zmdsr6MaACS5K3tHw3QDQmFbkEsdnG3zAZzhjEgEtetL1jwZ5VAL85UaaFzUpAZPrS7aGkQ3GdM75xPu4sUxSiF/*)",
None,
bitcoin::Network::Testnet,
MemoryDatabase::default(),
)?;

Ok(())
}
```



- generate-osoitteet**: Luo uusia osoitteita Bitcoin:n vastaanottamiseksi Testnet:lta Faucet:ltä.


```Rust
//import AddressIndex outside the main function
use bdk::wallet::AddressIndex;

//Function to add isnide main function
let address = wallet.get_address(AddressIndex::New)?;

```



- Tarkista saldo**: Tarkkaile Wallet:n tasapainoa yhdistämällä ensin electrumiin, synkronoimalla Wallet ja hakemalla tasapaino Wallet:lta.


```Rust
//connect to Electrum server and save the blockchain
let client = Client::new("ssl://electrum.blockstream.info:60002")?;
let blockchain = ElectrumBlockchain::from(client);

//sync wallet to the blockchain received
wallet.sync(&blockchain, SyncOptions::default())?;

//get the balance from your wallet
let balance = wallet.get_balance()?;
println!("This is your wallet balance: {}", balance);
```



- Rakenna, allekirjoita ja lähetä liiketoimet**: Rakenna ja viimeistele transaktiot ja lähetä ne sitten verkkoon.


```Rust
//Add to the imports
use bdk::bitcoin::Address;
use bdk::{SignOptions};
use std::str::FromStr;
use bdk::blockchain::Blockchain;

//build a transaction psbt
let mut builder = wallet.build_tx();
let recipient_address = Address::from_str("tb1qlj64u6fqutr0xue85kl55fx0gt4m4urun25p7q").unwrap();

builder
.drain_wallet()
.drain_to(recipient_address.script_pubkey())
.fee_rate(FeeRate::from_sat_per_vb(2.0))
.enable_rbf();
let (mut psbt, tx_details) = builder.finish()?;
println!("This is our psbt: {}", psbt);
println!("These are the details of the tx: {:?}", tx_details);

//Sign the PSBT
let finalized = wallet.sign(&mut psbt, SignOptions::default())?;
println!("Is my PSBT Signed? {}", finalized);
println!("This is my PSBT finalized: {}", psbt);


let tx = psbt.extract_tx();
let tx_id = tx.txid();
println!("this is my Bitcoin tx: {}", bitcoin::consensus::encode::serialize_hex(&tx));
println!("this is mny tx id: {}", tx_id);

//Broadcast the transaction
blockchain.broadcast(&tx)?;
```


#### Tulosta txid ja lähetä tapahtuma


transaction ID:n (txid) osoittaminen ja tulostaminen mahdollistaa seurannan alustoilla kuten Mempool.space. Tapahtuman lähettäminen voidaan toteuttaa menetelmällä `Blockchain.broadcast`, ja tapahtuman yksityiskohtien ja tilan tarkistaminen on ratkaisevan tärkeää, jotta voidaan varmistaa tapahtuman onnistunut leviäminen.


#### BDK:n hyödyllisyys ja yksityisyyden suoja


BDK on korvaamaton Bitcoin Wallet -kehityksen yksinkertaistamisessa. Yksityisyyden parantamiseen suositellaan työkaluja, kuten Electrumia, Exploraa ja henkilökohtaisia Bitcoin core-solmuja.


#### Ohjelmointikielet


Bitcoin-hankkeita kehitettäessä suositaan usein Rust:tä sen turvallisuuden ja tehokkuuden vuoksi. Kielen valinta voi kuitenkin vaihdella hankkeen erityisvaatimusten ja kehittäjän asiantuntemuksen perusteella.


#### BDK-riippuvuudet


BDK perustuu useisiin keskeisiin riippuvuussuhteisiin, kuten Rust-Bitcoin ja Rust-Miniscipt. Muita kirjastoja voidaan käyttää tietokantojen hallintaan ja salaukseen.


Kun ymmärrät nämä komponentit Bitcoin-solmuista ja lompakoista Bitcoin Development Kitiin (BDK), voit liikkua Bitcoin-ekosysteemissä entistä varmemmin ja pätevämmin. Tämän tiedon avulla voit kehittää vankkoja ja turvallisia Bitcoin-sovelluksia ja edistää tämän vallankumouksellisen teknologian jatkuvaa kehitystä.


# Lightning Network


<partId>d7ac2ad7-a4b3-564f-8a8d-cfec5297b3a5</partId>


## Maksukanavien historia


<chapterId>a0b11c6e-c0ff-5e65-b809-b2ab9a2fc37b</chapterId>

<professorId>880c7fa7-8d4c-4c9b-81b4-bc61ed256516</professorId>


:::video id=b90f19a3-a95e-4cd1-8c55-41016f3339cb:::

### Maksukanavien historia


Tervetuloa luennollemme nykyaikaisista maksuratkaisuista Blockchain-teknologian puitteissa. Tänään tarkastelemme monisatamalukkojen (MHL) ja Lightning Network:n historiallista taustaa ja keskeistä kehitystä.


#### Yleiskatsaus ja historiallinen tausta


MHL-lukot (Multi-hop-lukot) ja Lightning Network ovat Blockchain-teknologian edistyksellisiä konsepteja, jotka helpottavat tehokkaita ja turvallisia mikromaksuja verkossa. Näiden innovaatioiden tarve johtui Blockchain-teknologioiden, erityisesti Bitcoin:n, alkuperäisessä käyttöönotossa havaituista tehottomuuksista ja rajoituksista. Kun syvennymme syvemmälle, ymmärrät, miten aihekohtaiset rakenteet ja kerroksittaiset lähestymistavat ovat mullistaneet Blockchain-transaktiot.


### Aihekohtainen rakenne


MHL:ien ja Lightning Network:n käyttöönotto merkitsee paradigman muutosta perinteisistä, lineaarisista Blockchain transaktioista kehittyneempiin, monikerroksisiin järjestelmiin. Nämä innovaatiot mahdollistavat skaalautuvamman ja turvallisemman maksuinfrastruktuurin, jossa ratkaistaan monia varhaisiin Blockchain-toteutuksiin sisältyviä ongelmia, koska maksutapahtumat on jaettu tiettyihin aiheisiin tai segmentteihin.


### Bitcoin:n ongelmat


Bitcoin, Blockchain-teknologian edelläkävijä, otti käyttöön hajautetun järjestelmän, jossa tapahtumat lähetetään koko verkkoon. Vaikka tämä menetelmä on vallankumouksellinen, se on luonnostaan tehoton. Verkon jokaisen solmun on validoitava jokainen transaktio, mikä johtaa merkittäviin viiveisiin ja pullonkauloihin erityisesti suurten transaktiomäärien aikana.


Bitcoin:n hajautettu validointiprosessi vaatii huomattavia laskentaresursseja. Jokaisen tapahtuman on oltava useiden solmujen varmentama ja tallentama, mikä kuluttaa valtavasti energiaa ja laskentatehoa. Tämä ei ainoastaan lisää toimintakustannuksia, vaan myös rasittaa verkon kaistanleveyttä, mikä johtaa transaktiomaksujen nousuun ja hitaampiin käsittelyaikoihin.


Bitcoin:n hajauttaminen on yksi sen keskeisistä vahvuuksista, mutta siihen liittyy myös merkittäviä haasteita. Blockchain:n julkinen luonne tarkoittaa, että kaikki transaktiot ovat kaikkien nähtävillä, mikä herättää huolta yksityisyydestä. Lisäksi tarve päästä yhteisymmärrykseen lukuisten solmujen kesken voi johtaa keskittämispaineisiin, kun Mining valta keskittyy muutamien suurten yksiköiden käsiin.


### Maksukanavat ratkaisuna


![Gold coin](assets/en/044.webp)_Gold Standard Metaphor_


Address Bitcoin:n tehottomuuden ja yksityisyyden suojaan liittyvien ongelmien ratkaisemiseksi on ehdotettu maksukanavia toimivaksi ratkaisuksi. Mikromaksukanavat mahdollistavat maksutapahtumat off-chain ja vähentävät tarvetta jatkuvaan tietojen jakamiseen koko verkossa. Tämä keventää merkittävästi Blockchain:n taakkaa ja mahdollistaa nopeammat ja halvemmat maksutapahtumat.


Maksukanavien perusperiaatteena on käsite, jonka mukaan maksutapahtumat otetaan off-chain. Sen sijaan, että jokainen maksutapahtuma lähetettäisiin koko verkkoon, osapuolet voivat avata maksukanavan ja suorittaa lukuisia maksutapahtumia keskenään. Vain kanavan avaaminen ja sulkeminen tallennetaan Blockchain:een, mikä parantaa huomattavasti tehokkuutta ja yksityisyyttä.


Maksukanavien off-chain luonteesta huolimatta on edelleen mahdollista pakottaa maksutapahtumat On-Chain. Jos syntyy riita tai jos toinen osapuoli yrittää huijata, kanavan viimeisin tila voidaan lähettää Blockchain:lle, jolloin voidaan varmistaa, että sovitut maksutapahtumat toteutetaan ja että varat jaetaan oikein.


Maksukanavat ovat merkittävä edistysaskel Blockchain-teknologiassa, sillä ne tarjoavat skaalautuvan ja turvallisen menetelmän liiketoimien suorittamiseen ja ratkaisevat samalla monia Bitcoin:een liittyviä perustavanlaatuisia ongelmia. Kun jatkamme innovointia ja rakentamista näille perustuksille, Blockchain:n tulevaisuus näyttää yhä lupaavammalta.


Johtopäätöksenä voidaan todeta, että Bitcoin:n historiallisen taustan ja haasteiden sekä MHL:n, Lightning Network:n ja maksukanavien kautta ehdotettujen innovatiivisten ratkaisujen ymmärtäminen antaa kattavan kuvan Blockchain-teknologian nykyisestä tilanteesta ja tulevaisuuden mahdollisuuksista.


## Atomireitityksen historia


<chapterId>28be7b31-e6b2-5eea-a5ed-62ce0a154b6e</chapterId>

<professorId>880c7fa7-8d4c-4c9b-81b4-bc61ed256516</professorId>


:::video id=059a714b-4fe9-4266-acb0-6fe5af491662:::

Edellisissä keskusteluissamme käsittelimme perusmaksukanavien perusteita. Näiden kanavien avulla kaksi osallistujaa, vaikkapa Alice ja Bob, voivat käydä kauppaa suoraan toistensa kanssa saumattomasti. Tässä mallissa on kuitenkin räikeä rajoitus: Alice voi tehdä liiketoimia vain Bob:n kanssa eikä muiden osallistujien, kuten Charlien, kanssa, ellei hän luo erillisiä kanavia kunkin osallistujan kanssa. Tämä useiden kanavien tarve johtaa tehottomuuteen ja skaalautuvuusongelmiin, koska Alice:n olisi epäkäytännöllistä avata suora kanava kaikkien niiden kanssa, joiden kanssa hän haluaa käydä kauppaa.


### Keskitetyt humalat


Address Manny Rosenfeld ehdotti vuonna 2012 näiden rajoitusten poistamiseksi keskitetyn hopsin käsitettä. Tässä mallissa otettiin käyttöön keskitetyt maksuprosessorit, kuten TrustPay, reitittämään maksuja käyttäjien välillä. Vaikka tämä menetelmä voi vähentää useiden suorien kanavien tarvetta, se tuo mukanaan merkittäviä haittoja. Keskitetyt hopsit kärsivät turvallisuusongelmista, luottamusongelmista, yksityisyyden loukkauksista, mahdollisista huijauksista, sensuurista ja luotettavuusongelmista. Käyttäjien on luotettava näihin keskitettyihin yksiköihin helpottaakseen transaktioitaan, mikä on hajauttamisen eetoksen vastaista.


### Hashed Time Lock Contract (HTLC) ja toteutus


Keskitettyjen hopsien rajoitukset ja haitat edellyttivät turvallisempaa ja hajautetumpaa ratkaisua. Tämä tarve johti Hashed Time Lock Contract:n (HTLC) kehittämiseen, jota Joseph Poon ja Thaddeus Dreijer ehdottivat vuonna 2015 osana Lightning Network:tä. HTLC:ssä yhdistyvät aikalukkojen ja Hash-lukkojen periaatteet, joilla varmistetaan transaktioiden atomisuus ja luotettavuus. Tämä tarkoittaa, että transaktio joko suoritetaan kokonaan tai sitä ei tapahdu lainkaan, mikä vähentää epätäydellisiin maksuihin liittyviä riskejä.


HTLC:n työnkulkuun kuuluu monivaiheinen prosessi, joka varmistaa turvallisen reitityksen useiden välittäjien kautta. Oletetaan, että Alice haluaa maksaa Ericille välittäjien Bob, Carol ja Diana kautta. Jokaisessa prosessin vaiheessa luodaan Commitment:n tapahtumia, joiden aikasulut ja summat pienenevät. Tarvittaessa viimeinen vaihe voidaan lähettää Bitcoin-verkkoon tapahtuman viimeistelemiseksi.


HTLC:ssä Alice lukitsee maksun Hash:lla salaisen "R:n" Bob, Carol ja Diana luovat kukin samanlaiset sopimukset myöhempien välittäjiensä kanssa varmistaen, että he voivat vaatia varojaan vain, jos he esittävät oikean salaisen "R":n Tämä mekanismi varmistaa atomisuuden; maksu suoritetaan kokonaan tai epäonnistuu, mikä suojaa osittaisilta rahastojen menetyksiltä.


![Hash lock](assets/en/045.webp)_Hash lock function_


### Käytännön näkökohdat ja verkon dynamiikka


Käytännön skenaariossa Alice:n maksuvirta käsittää Ericin maksamisen useiden välittäjien, kuten Bob:n, Carolin ja Dianan, kautta. Ketjun jokainen osallistuja on vastuussa varojen ottamisesta edelliseltä osallistujalta.


#### Kanavan tilan päivitykset


Kanavat päivittävät tilansa osallistujien keskinäisten sopimusten ja allekirjoitusten perusteella. Esimerkiksi Alice ja Bob voivat päivittää kanavatilansa käyttämättä välttämättä salaisuutta "R", kunhan ne sopivat tapahtuman ehdoista.


#### Atomisuus varmistettu


HTLC-mekanismi varmistaa atomisuuden aikalukkojen ja allekirjoitusten avulla. Tämä suojaus varmistaa, että maksuprotokolla takaa joko täydellisen onnistumisen tai epäonnistumisen, mikä suojaa osittaisilta varojen menetyksiltä.


![Time lock and signatures](assets/en/046.webp)_Combine restrictions_


#### Kannustimet ja vastuualueet


Dianan ja Carolin kaltaisia välittäjiä kannustetaan toimimaan oikein verkostossa. Jos he epäonnistuvat, seuraukset kohdistuvat yleensä vain välittäjään itseensä, mikä edistää vastuullista käyttäytymistä.


### Käytännön näkökohtia


Maksureitin useampi siirtymävaihe voi kuitenkin lisätä viiveaikaa, maksuja ja mahdollista epäluotettavuutta. Useiden kanavien avaaminen voi auttaa vähentämään reititykseen tarvittavien siirtymisten määrää, mikä parantaa kokonaistehokkuutta.


#### Kanavan kuvaaja ja likviditeetti


Verkon solmut voivat joko kuulua julkisesti ilmoitettuun kanavagraafiin tai jäädä ilmoittamatta. Näiden kanavien likviditeetti on ratkaisevassa asemassa tehokkaan reitityksen kannalta, sillä solmut tarvitsevat riittävästi saldoa välittääkseen maksut onnistuneesti eteenpäin.


#### Lähteen reititys ja yksityisyys


Alice:n on tunnettava verkon topologia, jotta se voi päättää maksureitistä. Lähteen reititystä käytetään yksityisyyden säilyttämiseksi, vaikka maksujen reitittäminen useiden välittäjien kautta on monimutkaista.


![Source Routing](assets/en/047.webp)_Source Routing Path_


#### Päätelmä


Yhteenvetona voidaan todeta, että solmun asianmukainen toiminta takaa atomiset maksut, ja Lightning Network pyrkii ratkaisemaan Address monia ongelmia, joita perinteiset maksujärjestelmät, kuten Ripple, kohtaavat. Hyödyntämällä HTLC:tä ja strategista reititystä Lightning Network tarjoaa skaalautuvamman, tehokkaamman ja turvallisemman ratkaisun hajautettuihin maksuihin.


## Bolt arvostelu


<chapterId>ba4b09ae-81de-53f2-8c15-316f037aaea9</chapterId>


:::video id=f0d17fe4-d793-4b90-924e-b551db501fbb:::

Bitcoin-verkko toimii Trustless-arvo- Exchange-järjestelmänä, joka toimii ensisijaisesti selvitys-Layer-järjestelmänä, jossa tapahtumat kirjataan julkiseen Ledger-järjestelmään. Tämä takaa turvallisuuden ja muuttumattomuuden, mutta siihen liittyy rajoituksia erityisesti transaktioiden nopeuden ja maksujen osalta. Tämän vuoksi Bitcoin voi olla tehoton jokapäiväisissä pienissä transaktioissa.


Lightning Network, joka toimii toisena Layer:na Bitcoin Blockchain:n päällä. Tämä maksuverkko on suunniteltu nopeiden ja edullisten maksutapahtumien helpottamiseksi. Avaamalla maksukanavan kahden osapuolen välille ne voivat tehdä liiketoimia off-chain:ssä ja kirjata vain alku- ja loppusaldot Bitcoin Blockchain:ään. Tämä vähentää merkittävästi pääverkon kuormitusta, parantaa skaalautuvuutta ja tekee mikrotransaktioista mahdollisia.


Jotta käsite hahmottuisi paremmin, ajattele analogisesti baarilaskua. Kun avaat laskun baarissa, voit tilata juomia jatkuvasti maksamatta jokaisen juoman jälkeen. Lopulta maksat loppusumman illan päätteeksi. Vastaavasti Lightning-kanava mahdollistaa useita tapahtumia off-chain, jotka maksetaan On-Chain vasta, kun kanava suljetaan. Toinen analogia on lentokenttä, jossa maksun ohjaaminen useiden solmujen kautta on kuin jatkolentojen käyttäminen määränpäähän pääsemiseksi. Jokainen solmu (tai "lento") auttaa ohjaamaan maksun sinne, minne sen on mentävä, ja varmistaa näin tehokkaan reitityksen.


![airport analogy](assets/en/048.webp)_The airport analogy of LN_


Pohjimmiltaan Lightning Network täydentää Bitcoin-verkkoa puuttumalla sen rajoituksiin ja tekee siitä pelkän selvitysjärjestelmän Layer:n sijaan monipuolisen järjestelmän, joka pystyy käsittelemään tehokkaasti jokapäiväisiä liiketoimia.


### **Lightning Network tekniset tiedot**


Lightning Network-protokolla on määritelty huolellisesti 10 BOLT:n (Basis of Lightning Technology) avulla. Nämä BOLTit sovittiin Milanossa pidetyssä konferenssissa, ja ne toimivat perustana Lightning Network:n eri toteutuksille.


![bolt](assets/en/049.webp)_BOLT Diagram _


#### Bolt 1 (perusprotokolla)


Bolt 1 hahmottelee sanoman muotoilun käyttäen Type-Length-Value (TLV) -rakennetta, jolla varmistetaan, että sanomat ymmärretään yhdenmukaisesti eri toteutuksissa. Viestintä tapahtuu yleensä tietyn TCP-portin kautta, ja viestit voidaan luokitella seuraavasti:



- Viestintäviestit**: Näihin kuuluvat `Init`-, `Error`-, `Warning`-, `Ping`- ja `Pong`-viestit, jotka luovat yhteyksiä, käsittelevät virheitä, tutkivat yhteyden tilaa ja häivyttävät liikennettä.
- Kanavan asetusviestit**: Nämä ovat ratkaisevia kanavan perustamisvaiheessa.
- Kanavan tilaviestit**: Nämä viestit käsittelevät aktiivisten kanavien päivityksiä ja varmistavat, että molemmat osapuolet ovat ajan tasalla.
- Juoruviestit**: Näitä käytetään verkon topologian löytämiseen ja päivittämiseen.
- Kokeelliset viestit**: Nämä mahdollistavat uusien ominaisuuksien testaamisen verkkoa häiritsemättä.


#### Bolt 2 (kanavan elinkaari)


Bolt 2 käsittelee kanavan elinkaarta perustamisesta normaaliin toimintaan ja lopulta selvitykseen. Keskeisiä prosesseja ovat mm:



- Kanavan perustaminen**: Tässä vaiheessa osapuolet avaavat kanavan, Exchange allekirjoitukset ja luovat rahoitustapahtuman.
- Normaali toiminta**: Tässä kanavan tila päivitetään jatkuvasti Hash-aikarajoitettujen sopimusten (HTLC) avulla. Commitment- ja peruutussanomien avulla varmistetaan, että molemmat osapuolet ovat yhtä mieltä tämänhetkisestä tilasta.
- Selvitys**: Tähän kuuluu kanavan sulkeminen, yleensä keskinäisen sopimuksen ja palkkioneuvottelujen avulla, jotta liiketoimet saadaan päätökseen ilman, että joudutaan loputtomaan sulkemissilmukkaan.


#### Päivitysmekanismi


HTLC:t ovat keskeisessä asemassa verkon maksujen reitityksessä, ja ne mahdollistavat turvalliset maksutapahtumat ilman luottamusta. Commitment- ja peruutusviestit varmistavat keskinäisen yhteisymmärryksen kanavan tilasta ja estävät petokset.


#### Erityisviestit


Erityisviestit, kuten `Update Fee` (päivitysmaksu), säätävät Miner-maksuja Commitment-tapahtumien osalta, kun taas `Channel Reestablish` (kanavan palauttaminen) -viestit varmistavat, että molemmat vertaisverkot pysyvät synkronoituina yhteyden katkeamisen jälkeen.


#### Kanavien sulkeminen


Kanavat voidaan sulkea keskinäisellä sopimuksella, yksipuolisin toimin tai rangaistuksella, jos huijaaminen havaitaan. Asianmukainen sulkeminen viimeistelee liiketoimet turvallisesti.


#### Swapit likviditeetin hallintaan


Swapit mahdollistavat On-Chain-nostot ja tehokkaan likviditeetinhallinnan ilman kanavien sulkemista. Tulevaisuuden ratkaisuja, kuten liitosprosessia, kehitetään tämän prosessin tehostamiseksi.


#### Turvatoimet


Commitment-tapahtumissa käytetään mekanismeja, kuten nLockTime, OPCheckSequenceVerify ja peruutusavaimet, varojen suojaamiseksi ja varkauksien estämiseksi.


### Reititys ja sipulireititys


![onion routing](assets/en/050.webp)_Onion Routing diagram _


Maksut reititetään käyttäen Onion-reititystä, jossa luodaan salattuja paketteja, jotka lähetetään useiden solmujen kautta. HTLC:t suojaavat maksutapahtuman, mikä takaa yksityisyyden ja turvallisuuden.


### Invoice rakenne


Lightning Network-laskut (Bolt 11) on koodattu Bech32-koodilla, ja ne sisältävät yksityiskohtia, kuten maksun Hash, kuvauksen ja voimassaoloajan. Jokaista Invoice on käytettävä kerran uudelleenkäytön estämiseksi.


![Invoice structure](assets/en/051.webp)_BOLT11 Invoice_


#### Salaus ja todentaminen


Kättelymenettelyt ja salaus (Chacha20) sekä todennus (Poly1305) varmistavat viestin eheyden ja yksityisyyden Lightning-transaktioissa.


#### Vaihtoehdot


Muut maksupyyntömenetelmät, kuten LNURL, Keysend ja Bolt 12, tarjoavat erilaisia ominaisuuksia ja hyväksynnän tasoja, mikä tarjoaa joustavuutta verkkoon.


#### Verkon löytäminen


Lightning Network:n verkon löytäminen on kehittynyt alkuperäisestä IRC:n (Internet Relay Communication) käytöstä kehittyneempään protokollaan, joka on määritelty Bolt 7:ssä. Tämä protokolla käyttää erityisiä Lightning-viestejä, joita kutsutaan yleisesti juoruviesteiksi, verkkotopologian löytämiseksi ja ylläpitämiseksi.


#### Bolt7 viestejä


Tärkeimmät Bolt 7-viestit ovat:



- Solmun ilmoitus**: Tämä viesti ilmoittaa solmun olemassaolosta.
- Kanavan ilmoitus**: Tämä viesti ilmoittaa verkolle uuden kanavan luomisesta.
- Ilmoituksen allekirjoitus**: Tällä varmistetaan lähetysviestien aitous.
- Kanavapäivitys**: Tämä viesti välittää kanavaa koskevia päivityksiä, kuten maksurakenteet ja HTLC:n enimmäismäärät.


#### Kanavan ilmoitusprosessi


Prosessi alkaa, kun paikalliset vertaisverkot vaihtavat identiteetti- ja kanavatiedot. Allekirjoitusten tarkistamisen ja transaktioiden rahoittamisen jälkeen ne ilmoittavat kanavasta verkon vertaisverkoilleen varmistaen, että koko verkko pysyy ajan tasalla viimeisimmistä topologian muutoksista.


#### DNS bootstrap


Lightning-vertaisverkon löytämistä helpottavat DNS- ja Bitcoin DNS seed -kyselyt, jotka antavat IP- ja solmutiedot. Tämä alkuvaiheen havaintomekanismi auttaa solmuja liittymään verkkoon nopeasti.


#### Ominaisuusilmoitukset


Solmut voivat lähettää tuettuja ominaisuuksiaan, mikä varmistaa taaksepäin yhteensopivuuden ja mahdollistaa valinnaiset parannukset. Tämä joustavuus varmistaa, että kaikki solmut voivat olla sujuvasti vuorovaikutuksessa, vaikka protokolla kehittyisi.


#### Bolt11-laskujen käsittely


Verkko varmistaa Bolt 11 -laskujen ainutkertaisuuden, jotta vältetään samasta Invoice:stä aiheutuvat moninkertaiset maksut. Jos Invoice-lasku käytetään uudelleen, verkon solmut pysäyttävät ja estävät päällekkäiset maksut, jolloin tapahtuman eheys säilyy.


#### Puhe Tiedonsiirto


Vaikka puhedatan lähettäminen Lightning Network:n kautta on mahdollista, se on voimakkaasti pakattua ja viestin koon mukaan rajoitettua. Esimerkkisovellus on Sphinx, jossa tutkitaan Lightningin innovatiivista käyttöä tiedonsiirtoon.


#### Käyttötapaukset ja keskustelut


Lightning Network:n käyttötarkoituksesta käydään jatkuvasti keskustelua. Vaikka se on ensisijaisesti suunniteltu maksamiseen, myös muita käyttötarkoituksia, kuten tiedonsiirtoa, tutkitaan, vaikkei niitä olekaan yleisesti hyväksytty. Yhteisö keskustelee jatkuvasti mahdollisista verkkosovelluksista ja protokollan parannuksista.


#### Yhteisön keskustelut


Lightning Network-yhteisö on elinvoimainen, ja se käy jatkuvaa keskustelua käyttötapauksista, protokollasovelluksista ja mahdollisista parannuksista. Tämä yhteistoimintaympäristö edistää innovointia ja varmistaa samalla, että verkko kehittyy vastaamaan käyttäjien tarpeita.


Yhteenvetona voidaan todeta, että toisen Layer:n merkityksen, Lightning Network:n eritelmien ja verkonhakujärjestelmien ymmärtäminen on ratkaisevan tärkeää kaikille, jotka haluavat perehtyä Lightning Network:n monimutkaisuuksiin. Kyseessä on monimutkainen mutta erittäin antoisa ala, joka lupaa muuttaa digitaalisten liiketoimien tulevaisuutta.


## Tärkeimmät LN-asiakkaat


<chapterId>a2ad8db4-aea2-5231-927c-616c53db31bf</chapterId>


:::video id=90240cb6-a942-4015-b0c2-b721c48309ec:::

Lightning Network (LN) edustaa merkittävää läpimurtoa Bitcoin:n skaalautuvuudessa ja transaktionopeudessa. LN-asiakkaat, joita yleensä kutsutaan Lightning-lompakoiksi, ovat erikoistuneita ohjelmistoja tai sovelluksia, joiden avulla käyttäjät voivat suorittaa liiketoimia Lightning Network:n kautta. Nämä lompakot toimivat ratkaisevana Interface välittäjänä käyttäjän ja LN:n välillä ja helpottavat off-chain polkuja hyödyntämällä välittömästi suoritettavia, edullisia transaktioita.


Lightning-lompakot on suunniteltu käyttäjäystävällisiksi, ja jopa teknisesti vähän tietävät voivat hyödyntää Bitcoin:n kehittyneitä toimintoja. Koska nämä lompakot mahdollistavat nopeat ja kustannustehokkaat mikrotransaktiot, ne edistävät merkittävästi Bitcoin:n laajempaa käyttöönottoa jokapäiväisissä liiketoimissa.


![LN Clients](assets/en/052.webp)_Lightning Wallets_


### Bitcoin-lompakot vs. Lightning-lompakot


Bitcoin-lompakot ja Lightning-lompakot eroavat perustavanlaatuisesti toisistaan arkkitehtuuriltaan ja käyttötapauksiltaan, vaikka niillä onkin yhteistä yksityisten avainten hallinta:


#### Bitcoin-lompakot:



- Yksityisen avaimen huoli**: Bitcoin-lompakoissa on ensisijaisesti kyse siitä, kenellä on yksityinen avain. Tämä määrittää käyttäjän varojen turvallisuuden ja valvonnan.
- Tapahtuman monimutkaisuus**: Bitcoin-lompakot käsittelevät erilaisia tapahtumakäsikirjoituksia, kuten Segregated Witness (SegWit) ja Taproot, jotka optimoivat tapahtumakoot ja parantavat yksityisyyttä ja turvallisuutta.


#### Salamalompakot:



- Yksityisen avaimen hallinta**: Samoin kuin Bitcoin-lompakoissa, yksityisten avainten hallinta on edelleen ratkaisevan tärkeää.
- Likviditeetin hallinta**: Tämä edellyttää paikallisen (lähtevän) ja kaukaisen (saapuvan) likviditeetin tasapainottamista, jotta transaktioiden reititys olisi sujuvaa. Tämä edellyttää, että käyttäjät ymmärtävät ja optimoivat kanavansa tehokkaan maksujen välittämisen helpottamiseksi.


#### Likviditeetin hallinta salamalompakoissa


Tehokas likviditeetinhallinta on Lightning Network:n onnistuneen toiminnan kulmakivi. Siihen kuuluu kahden ensisijaisen likviditeettityypin strateginen tasapaino:


#### Paikallinen (lähtevä) likviditeetti:



- Tämä edustaa Bitcoin-määrää, jonka käyttäjä voi lähettää Lightning-kanavistaan. Se on ratkaisevan tärkeää maksujen käynnistämisessä ja sen varmistamisessa, että maksutapahtumat voidaan ohjata vastaanottajalle.


#### Kauko- (saapuva) likviditeetti:



- Tämä edustaa Bitcoin:n määrää, jonka käyttäjä voi vastaanottaa kanaviensa kautta. Se on yhtä tärkeä, sillä se varmistaa, että muut voivat lähettää käyttäjälle maksuja.


#### Esimerkki likviditeetin hallinnasta:


![Example of Liquidity](assets/en/053.webp)_Lightning Liquidity_


Tarkastellaan skenaariota, jossa Alice, Bob, Charlie ja Dan ovat tyypillisiä LN-käyttäjiä, jotka ovat yhteydessä toisiinsa eri kanavien kautta:



- Alice haluaa maksaa Danille, mutta sillä ei ole riittävästi paikallista likviditeettiä kanavallaan Bob:n kanssa.
- Jos Bob:lla on riittävä saldo ja kanava Charlien kanssa ja Charliella on kanava Danin kanssa, Alice:n maksu voidaan ohjata Bob:n ja Charlien kautta Danille.


![Example of Liquidity](assets/en/054.webp)_Lightning Liquidity_


Jos jokin näistä kanavista kuitenkin tyhjenee tai yhteysongelmia ilmenee, tapahtuma voi epäonnistua. Tämä osoittaa, kuinka tärkeää on ylläpitää tasapainoista likviditeettiä koko verkossa.


#### Lightning Network:n haasteet:



- Kanavien tyhjeneminen**: Ajan myötä kanavat voivat muuttua epätasapainoisiksi, jolloin varat keskittyvät yhdelle puolelle, mikä rajoittaa transaktiomahdollisuuksia.
- Yhteysongelmat**: Tehokas tapahtumien reititys edellyttää vankkoja verkkoyhteyksiä, joiden ylläpito voi olla haastavaa.


Address näitä haasteita varten likviditeettipalveluntarjoajat tarjoavat palveluja, jotka auttavat hallinnoimaan likviditeettiä, usein maksua vastaan, ja varmistavat, että käyttäjät säilyttävät optimaaliset kanavasaldot sujuvien transaktioiden mahdollistamiseksi.


### Eri lompakot ja niiden ominaisuudet


Saatavilla on erilaisia Lightning-lompakoita, joista jokainen vastaa erilaisiin käyttäjien tarpeisiin ja mieltymyksiin. Tässä on muutamia esimerkkejä:


#### Satoshi:n Wallet:



- Ominaisuudet**: Täysin huoltajapohjainen, käyttäjäystävällinen, mutta suljettu lähdekoodi, joka saattaa aiheuttaa huolta yksityisyydestä.


#### Albi:



- Ominaisuudet**: Selainlaajennus, avoin lähdekoodi, tukee sekä huoltajamalleja että muita malleja, mikä lisää monipuolisuutta.


#### Tuuli:



- Ominaisuudet**: Kevyt solmu puhelimessa, avoin lähdekoodi, yhdistää itsesäilytyksen ja hallinnoidun likviditeetin, mikä tarjoaa tasapainon hallinnan ja mukavuuden välillä.


#### Phoenix:



- Ominaisuudet**: Avoin lähdekoodi, keskittyy käyttäjän yksinkertaisuuteen ja tehokkaaseen likviditeetinhallintaan.


#### Avaa Bitcoin Wallet (OBW):



- Ominaisuudet**: Avoimen lähdekoodin ja kehittyneiden ominaisuuksien avulla, sopii tehokäyttäjille: Integroi On-Chain- ja Lightning-lompakot, tukee isännöityjä kanavia.


### Säilytys- ja likviditeetinhallintamatriisi


Lompakot voidaan luokitella sen mukaan, kenellä on yksityiset avaimet ja kuka hallinnoi likviditeettiä. Tämä matriisi auttaa käyttäjiä valitsemaan lompakot, jotka vastaavat heidän mieltymyksiään turvallisuuden ja mukavuuden suhteen:



- Huoltajan lompakot**: Kolmannen osapuolen hallussa olevat yksityiset avaimet, tarjoavat yleensä automaattisen likviditeetinhallinnan. Esimerkkejä ovat Wallet ja Satoshi.
- Muiden kuin huoltajien lompakot**: Käyttäjillä on yksityiset avaimet, voi vaatia manuaalista likviditeetin hallintaa. Esimerkkejä ovat Breez ja OBW.


![Liquidity Lightning](assets/en/055.webp)_2x2 Matrix of LN Clients_


### Kritiikki ja parannusehdotukset


Lightning-lompakoita arvostellaan niiden hyödyistä huolimatta monin tavoin, ja niissä on parantamisen varaa:



- Yksityisyys**: Suljetun lähdekoodin lompakot ja tietyt säilytysmallit herättävät huolta yksityisyydestä.
- Helppokäyttöisyys**: Edistyksellisten ominaisuuksien ja käyttäjäystävällisyyden tasapainottaminen on edelleen haaste.
- Avoimen lähdekoodin kehitys**: Avoimen lähdekoodin eri tasot vaikuttavat käyttäjien luottamukseen ja innovaatiovauhtiin.


### Lisätietoa ja käyttötapauksia


#### Algoritmin haasteet:


Nykyiset algoritmit optimaalisen reitin löytämiseksi Lightning Network:n sisällä ovat usein epäoptimaalisia ja edellyttävät kokeilua ja erehdystä. Reitityksen tehokkuuden parantamiseksi tarvitaan parannuksia.


#### Moniosaiset maksut:


Suurempien maksujen jakaminen pienempiin tapahtumiin voi lieventää likviditeetti- ja polunhakukysymyksiä ja varmistaa sujuvammat tapahtumat.


#### Reitityksestä saatavat tulot:


Reititysmaksuista saatavat tulot ovat yleensä minimaalisia, joten yksittäisten käyttäjien ei ole yhtä houkuttelevaa ylläpitää reitityssolmuja voiton tavoittelemiseksi.


#### Erilaisia Wallet-esimerkkejä:



- Vilkku Wallet**: Sats:n ominaisuudet ovat vakaat, mutta Lightning Network:n kehittyneet ominaisuudet puuttuvat.
- Blitz Wallet**: Avoimen lähdekoodin, itsesäilytettävä, vaatii käyttäjän hallinnoimaa likviditeettiä, tarjoaa kattavat tiedot tehokäyttäjille.
- SwissBitcoinPay**: Vähäiset maksut suurille käyttäjille.


#### Wallet-käyttötapaukset:


Eri lompakot palvelevat eri tarkoituksia, aloittelijoiden helppokäyttöisyydestä tehokäyttäjien kehittyneisiin ominaisuuksiin. Ei ole olemassa yhtä "parasta" Wallet:aa; valinta riippuu yksilöllisistä tarpeista ja mieltymyksistä.


#### Avoimen lähdekoodin osuus:


Käyttäjien palaute ja osallistuminen avoimen lähdekoodin projekteihin ovat korvaamattomia kehityksen ja henkilökohtaisten taitojen kasvun kannalta, ja ne edistävät yhteistoiminnallista ja innovatiivista ympäristöä.


Johtopäätöksenä voidaan todeta, että Lightning Network-asiakkaiden eri näkökohtien, niiden erojen perinteisiin Bitcoin-lompakoihin verrattuna ja tehokkaan likviditeetinhallinnan merkityksen ymmärtäminen on ratkaisevan tärkeää, jotta Lightning Network:n koko potentiaali voidaan hyödyntää. Valitsemalla oikean Wallet:n ja osallistumalla aktiivisesti ekosysteemiin käyttäjät voivat parantaa Bitcoin-tapahtumakokemustaan merkittävästi.


# LN:n haasteet


<partId>ca58c9d7-ba7e-5392-8488-6a21a9850e6a</partId>


## LN:n käytännön haasteet


<chapterId>014c7c40-aef7-58ac-b51f-33784463f482</chapterId>


**(video on saatavilla pian)**


Tässä istunnossa Asi0 käsittelee Lightning Network:n (LN) kanssa työskentelyyn liittyviä käytännön haasteita. Huolimatta Bitcoin-tapahtumien skaalautumista koskevasta vallankumouksellisesta lähestymistavasta Lightning Network:ssä on useita käytännön haasteita, jotka sekä käyttäjien että kehittäjien on ratkaistava. Tarkastelemme erityisesti neljää päähaastetta: **Layer 1/Layer 2 -abstraktio**, **off-line-maksujen vastaanottaminen** ja **varmistusten hallinta**.


Kutakin näistä haasteista tarkastellaan kahdesta näkökulmasta: **käyttäjän** ja **kehittäjän** näkökulmasta, sillä haasteet ja ratkaisut eroavat toisistaan sen mukaan, millainen rooli sinulla on ekosysteemissä.


---

### Haaste 1: likviditeetin hallinta


#### **Käyttäjän näkökulmasta:**


Lightning Network:ssa **maksuvalmiudella** tarkoitetaan maksujen suorittamiseen tai vastaanottamiseen tarvittavien varojen saatavuutta maksukanavissa. Käyttäjien on varmistettava, että heillä on riittävästi likviditeettiä saapuviin ja lähteviin maksutapahtumiin. Jos esimerkiksi haluat vastaanottaa maksuja, sinulla on oltava käytettävissä saapuvaa likviditeettiä, mikä tarkoittaa, että toisen solmun on osoitettava osa saldostaan sinun kanavallesi. Vastaavasti jos haluat lähettää maksuja, tarvitset kanavassasi lähtevää likviditeettiä.



- Käytännön kysymys**: Käyttäjien on usein vaikea tasapainottaa kanaviaan ja säilyttää riittävä likviditeetti. Lisäksi kanavien tasapainottaminen voi aiheuttaa kustannuksia.
- Mahdolliset ratkaisut**: Jotkut Lightning-lompakot ovat alkaneet integroida automaattista kanavien uudelleentasapainotusta, mutta tätä ominaisuutta kehitetään edelleen. Käyttäjät tukeutuvat myös **Lightning-palveluntarjoajiin (LSP)**, jotka auttavat likviditeetin hallinnassa.


#### **Kehittäjän näkökulmasta:**


Kehittäjien haasteena on toteuttaa saumaton likviditeetinhallinta sovelluksissa. Heidän on luotava työkaluja, jotka automatisoivat uudelleentasapainottamisen ja vähentävät käyttäjien kitkaa samalla kun optimoidaan maksut ja vältetään likviditeettipulmat.



- Käytännön kysymys**: Maksujen reitittämiseen verkossa, jonka likviditeetti vaihtelee, tarkoitettujen tehokkaiden algoritmien toteuttaminen voi olla monimutkaista ja laskentaintensiivistä.
- Mahdolliset ratkaisut**: Kehittäjät tutkivat kehittyneitä algoritmeja **likviditeetin reititystä** varten ja hyödyntävät **kaksinkertaisesti rahoitettuja kanavia** varmistaakseen, että likviditeetti on saatavilla transaktion molemmissa päissä.


**Määritelmät:**


- **Liquidius**: Varojen saatavuus salamakanavassa maksujen suorittamiseksi tai vastaanottamiseksi.
- **LSP (Lightning Service Provider)**: Palvelu, joka auttaa käyttäjiä hallitsemaan likviditeettiä ja kanavia Lightning Network:ssä.

---

### Haaste 2: L1/L2-abstraktio


#### **Käyttäjän näkökulmasta:**


**Layer 1 (L1)** (Bitcoin:n perus-Layer) ja **Layer 2 (L2)** (Lightning Network) välinen vuorovaikutus ei useinkaan ole täysin ymmärrettävissä käyttäjille. Esimerkiksi kanavien avaaminen ja sulkeminen edellyttää On-Chain Bitcoin -tapahtumia (L1), ja käyttäjien on maksettava On-Chain -maksuja näistä toimista. Tämä lisää monimutkaisuutta ja mahdollisia viiveitä, kun Bitcoin -verkko on ruuhkautunut.



- Käytännön kysymys**: Käyttäjät kamppailevat usein sen ymmärtämisen vaikeuden kanssa, milloin he ovat vuorovaikutuksessa Bitcoin-perus Layer:n ja milloin Lightning Layer:n kanssa. Tämä voi aiheuttaa sekaannusta maksujen, tapahtuma-aikojen ja turvallisuuden suhteen.
- Mahdolliset ratkaisut**: Parannetut Wallet-mallit, jotka abstrahoivat L1/L2-vuorovaikutukset ja hallitsevat kanavien avautumisia/sulkeutumisia taustalla. Jotkin lompakot sallivat jo nyt käyttäjien vaihtaa saumattomasti On-Chain- ja Lightning-tapahtumien välillä olosuhteista riippuen.


#### **Kehittäjän näkökulmasta:**


Kehittäjien tehtävänä on abstrahoida L1:n ja L2:n monimutkaisuus käyttäjille ja luoda sujuvia ja intuitiivisia käyttöliittymiä, jotka käsittelevät tapahtumia tehokkaasti. Haasteena on optimoida käyttäjäkokemus ja säilyttää samalla Lightning-protokollan eheys ja turvallisuus.



- Käytännön kysymys**: On-Chain-tapahtumien hallinnan teknisiltä monimutkaisuuksilta ja säilyttää samalla avoimuus tarvittaessa.
- Mahdolliset ratkaisut**: (joka mahdollistaa varojen lisäämisen tai poistamisen kanavasta sulkematta sitä) ja automaattisia kanavien hallintatyökaluja.


**Määritelmät:**


- **L1 (Layer 1)**: Bitcoin: Blockchain Layer.
- **L2 (Layer 2)**: Lightning Network, joka toimii Bitcoin:n päällä ja mahdollistaa nopeammat ja halvemmat maksutapahtumat.
- **Splicing**: Tekniikka, joka mahdollistaa salamakanavan tasapainon muuttamisen sulkematta sitä.

---

### Haaste 3: offline-maksujen vastaanottaminen


#### **Käyttäjän näkökulmasta:**


Yksi Lightning Network:n haasteista on **maksujen vastaanottaminen, kun käyttäjä on offline-tilassa**. Toisin kuin Bitcoin:n perusversiossa Layer, jossa maksutapahtumia voi vastaanottaa milloin tahansa, Lightning edellyttää, että sekä maksajan että maksunsaajan on oltava verkossa, jotta maksutapahtuma voidaan suorittaa. Tämä on merkittävä rajoitus monille käyttäjille, jotka haluavat käyttää Lightning-maksuja jokapäiväisissä tilanteissa.



- Käytännön kysymys**: Tämä on hankalaa niille, jotka haluavat käyttää Lightningia päivittäisenä maksutapana.
- Mahdolliset ratkaisut**: Joitakin kiertoteitä ovat esimerkiksi säilytyslompakoiden käyttäminen tai kolmannen osapuolen palveluihin turvautuminen, jotka toimivat maksujen välittäjinä, kunnes vastaanottajan solmu tulee verkkoon.


#### **Kehittäjän näkökulmasta:**


Kehittäjät tutkivat tapoja, joilla käyttäjät voivat vastaanottaa Lightning-maksuja myös silloin, kun heidän solmunsa ovat offline-tilassa. Tämä edellyttää luovia ratkaisuja, jotta Lightningin hajautettu luonne säilyy ja samalla ratkaistaan käytännön ongelma, joka liittyy jatkuvaan yhteydenpitoon.



- Käytännön kysymys**: On huomattava tekninen haaste kehittää protokolla tai järjestelmä, jonka avulla käyttäjät voivat vastaanottaa maksuja offline-tilassa vaarantamatta turvallisuutta tai hajauttamista.
- Mahdolliset ratkaisut**: Tutkimukset **offline-maksusetelistä**, joiden avulla vastaanottajat voisivat hakea maksuja, kun he ovat jälleen yhteydessä verkkoon, ovat käynnissä.


**Määritelmät:**


- **Offline-maksut**: Maksut, jotka lähetetään tai vastaanotetaan, kun toinen osapuoli ei ole yhteydessä Lightning Network:een.
- **Huoltajan lompakot**: Lompakot, joissa kolmas osapuoli hallitsee yksityisiä avaimia ja hoitaa transaktioita käyttäjän puolesta.

---

### Haaste 4: varmuuskopioiden hallinta


#### **Käyttäjän näkökulmasta:**


Lightning-kanavien varmuuskopiointi on tärkeää, jotta käyttäjät voivat palauttaa varansa, jos heidän solmunsa kaatuu tai tietoja menetetään. Lightning-kanavien varmuuskopiointiprosessi on kuitenkin monimutkaisempi kuin Bitcoin-kanavien, koska kanavat ovat tilatietoja, eli ne muuttuvat jokaisen tapahtuman yhteydessä.



- Käytännön kysymys**: Käyttäjien on varmistettava, että heidän kanavansa varmuuskopiot ovat ajan tasalla, sillä vanhentuneen varmuuskopion käyttäminen voi johtaa varojen menetykseen tai verkon rangaistukseen.
- Mahdolliset ratkaisut**: Lompakot, kuten Phoenix ja muut, ovat toteuttaneet automaattisia kanavien varmuuskopioita, mutta nämä ominaisuudet eivät ole vielä yleisiä kaikissa Lightning-lompakoissa.


#### **Kehittäjän näkökulmasta:**


Kehittäjien on otettava käyttöön varmuuskopiointiratkaisuja, joiden avulla käyttäjät voivat palauttaa varansa turvallisesti ja luotettavasti jopa katastrofaalisten vikojen jälkeen. Haasteena on varmistaa, että nämä ratkaisut ovat turvallisia ja helppokäyttöisiä ja että Lightning-protokollan eheys säilyy.



- Käytännön kysymys**: Varmistusjärjestelmien suunnittelu turvallisiksi, hajautetuiksi ja käyttäjäystävällisiksi on merkittävä haaste, koska varmuuskopiot on pidettävä ajan tasalla jokaisen kanavan tilanmuutoksen yhteydessä.
- Mahdolliset ratkaisut**: **mutta täysin automatisoituja ja turvallisia varmuuskopioita varten tarvitaan kehittyneempiä ratkaisuja.


**Määritelmät:**


- **Static Channel Backup (SCB)**: Varmuuskopiointityyppi, jonka avulla käyttäjät voivat palauttaa varojaan salamakanavalta vikatilanteessa palauttamalla kanavan viimeisimmän tilan.

---

#### Päätelmä


Lightning Network tarjoaa valtavia etuja Bitcoin-tapahtumien nopeuden ja kustannustehokkuuden kannalta, mutta se asettaa myös useita käytännön haasteita. Nämä haasteet - **likviditeetin hallinta**, **L1/L2-abstraktio**, **off-line-maksujen vastaanottaminen** ja **varmistuksen hallinta** - edellyttävät innovatiivisia ratkaisuja sekä käyttäjiltä että kehittäjiltä. Kun verkko kehittyy edelleen, näiden esteiden voittaminen on avainasemassa, jotta se voidaan ottaa laajasti käyttöön ja parantaa yleistä käyttäjäkokemusta.


Näiden haasteiden ratkaisemisen myötä Lightning Network:n kypsyminen jatkuu, ja siitä tulee entistä vankempi ja luotettavampi ratkaisu Bitcoin:n skaalausta varten.


## LN Tulevaisuuden kehitys


<chapterId>c06763dd-bb26-5fec-8ac4-3e446e9517cd</chapterId>

<professorId>880c7fa7-8d4c-4c9b-81b4-bc61ed256516</professorId>


:::video id=ab5f65f1-0b0d-4ca9-8ff7-d42764c1e915:::

### Bitcoin:n kestävyys ja kehitys


**Bitcoin maskotti: hunajamäyrä**

Bitcoin:n henkilöityy usein hunajamäyrään, joka on tunnettu sitkeydestään ja kestävyydestään. Tämä symboli edustaa osuvasti Bitcoin:n vankkaa ja periksiantamatonta luonnetta. Aivan kuten hunajamäyrä kestää myrkyllisiä puremia ja jatkaa menestymistään, Bitcoin on osoittanut huomattavaa kestävyyttä erilaisia vastoinkäymisiä, kuten sääntelyhaasteita, markkinoiden epävakautta ja teknisiä hyökkäyksiä vastaan.


**Bitcoin:n luonne: kehittyy jatkuvasti**

Vastoin käsitystä staattisuudesta Bitcoin on jatkuvassa kehityksessä. Sen protokollaa ja ekosysteemiä hiotaan ja parannetaan jatkuvasti maailmanlaajuisen kehittäjä- ja tutkijayhteisön toimesta. Tätä kehitysprosessia ohjaa tarve parantaa turvallisuutta, skaalautuvuutta ja toiminnallisuutta, mikä varmistaa, että Bitcoin pysyy kryptovaluuttamaiseman eturintamassa.


### Lightning Network:n innovaatiot


**Lightning Network: nopea kehitys**

Lightning Network, Bitcoin:n toinen Layer-ratkaisu liiketoimien skaalaamiseen ja nopeuttamiseen, on nopeassa kehityksessä. Tämä Layer mahdollistaa nopeat ja edulliset maksutapahtumat mahdollistamalla off-chain-maksukanavat. Merkittäviä innovaatioita on integroitu sen tehokkuuden ja käytettävyyden parantamiseksi.


**Kaksoisrahoitteiset kanavat**

Perinteisesti salamakanavan rahoittaa yksi osapuoli. Kaksoisrahoitteiset kanavat antavat kuitenkin molemmille osapuolille (esim. Alice ja Bob) mahdollisuuden osallistua kanavan maksuvalmiuteen. Tämä parannus mahdollistaa suuremman joustavuuden sekä lähetys- että vastaanottokapasiteetin suhteen ja edellyttää ennakkoviestintää ja uusia protokollia yhteisen rahoituksen hallinnoimiseksi.


**Splicing**

Splicing on ominaisuus, jonka avulla käyttäjät voivat muuttaa Lightning-kanavan kokoa sulkematta sitä. Tämä toiminto mahdollistaa varojen lisäämisen tai poistamisen olemassa olevasta kanavasta, mikä tarjoaa saumattoman tavan hallita kanavan likviditeettiä. Splicing edistää On-Chain-tapahtumien ja Lightning-kanavien yhteentoimivuutta ja parantaa verkon yleistä tehokkuutta.


**L2-mekanismi**

L2-mekanismissa otetaan käyttöön uusi menetelmä vanhojen kanavatilojen mitätöimiseksi ilman rangaistusmekanismia. Tämä päivitys riippuu SIGHASH_ANYPREVOUT-ominaisuudesta, joka edellyttää Bitcoin Soft Fork. L2-mekanismin luvataan yksinkertaistavan kanavanhallintaa ja parantavan turvallisuutta.


**Bolt 12**

Bolt 12:ssa käsitellään Lightning Network:ssä käytettyjen nykyisten Bolt 11 -laskujen rajoituksia. Se ottaa käyttöön uudelleenkäytettäviä laskuja ja automatisoi prosesseja poistamalla HTTP- ja verkkopalvelimien tarpeen toimimalla ainoastaan Lightning Network:n sisällä. Tämä innovaatio tehostaa liiketoimia ja parantaa käyttäjäkokemusta.


### Yksityisyyden suojan ja tehokkuuden parantaminen Bitcoin-tapahtumissa


**Taproot, muSig ja Schnorr-allekirjoitukset****

Taproot on merkittävä päivitys, joka vähentää tapahtumien monimutkaisuutta ja parantaa yksityisyyttä. Kun Taproot yhdistetään MuSigiin (protokolla usean allekirjoituksen transaktioita varten) ja Schnorr Signatures -protokollaan, se parantaa transaktioiden tehokkuutta. Näiden parannusten ansiosta Lightning-tapahtumat muistuttavat tavallisia Bitcoin-tapahtumia, mikä yksinkertaistaa prosessia ja vahvistaa yksityisyyttä.


**PTLC-reititys**

PTLC-sopimukset (Point Time Locked Contracts) ovat parannus nykyisiin Hash Time Lock Contracts -sopimuksiin (HTLC). PTLC-sopimuksissa käytetään Schnorr-allekirjoituksia, ja ne parantavat yksityisyyttä korvaamalla jaetut salaisuudet julkisilla avaimilla, mikä vähentää maksujen korrelaation ja väärinkäytön mahdollisuutta.


**Kanavatehtaat**

Kanavatehtaat mahdollistavat usean osapuolen kanavien luomisen (esim. 4-of-4 Multisig), jotka voivat synnyttää uusia 2-of-2-maksukanavia off-chain. Tämä järjestelmä mahdollistaa nopean ja maksuttoman kanavien luomisen ja sulkemisen, vaikka se edellyttääkin kaikkien osallistujien yhteistyötä. Kanavatehtaat lisäävät Lightning Network:n yleistä skaalautuvuutta ja joustavuutta.


**Watchtowers**

Vartiotornit ovat kolmannen osapuolen yksiköitä, jotka valvovat Blockchain:ää vanhojen kanavatilojen varalta. Jos rikkomus havaitaan, ne julkaisevat rangaistustapahtumia verkon turvallisuuden varmistamiseksi. Vaikka vahtitornit parantavat turvallisuutta estämällä väärinkäytökset, ne aiheuttavat myös yksityisyyden suojaan liittyviä ongelmia, jotka liittyvät tapahtumien seurantaan.


**blinded Polut**

blinded-reitit on suunniteltu parantamaan vastaanottimen yksityisyyttä Lightning Network:ssä. Ne peittävät lopullisen vastaanottajan Address:n ja varmistavat, että vain lähettäjä tuntee välipisteen ja että kukin solmu tuntee vain viereiset solmut. Tämä menetelmä suojaa vastaanottajan henkilöllisyyttä ja parantaa yleistä yksityisyyttä.


**Salamapalveluntarjoajat (LSP) **

Breez Wallet:n ideoimien Lightning-palveluntarjoajien (LSP) tavoitteena on parantaa käyttäjäkokemusta mahdollistamalla välittömät vastaanottotoiminnot. LSP:t avaavat käyttäjille kanavia samaan tapaan kuin internet-palveluntarjoajat tarjoavat yhteyspalveluja. Tämä innovaatio yksinkertaistaa käyttäjän käyttöönottoprosessia ja varmistaa saumattoman vuorovaikutuksen Lightning Network:lla.


**Lähteet, joiden avulla pysyt ajan tasalla**

Bitcoin:n ja Lightning Network:n uusimpien teknisten innovaatioiden seuraaminen edellyttää arvokkaiden resurssien hyödyntämistä. Bitcoin OpTec -uutiskirje, Lightning Dev -postituslista ja Jason Loppin kaltaisten alan asiantuntijoiden materiaalit tarjoavat tietoa ja päivityksiä tämän nopeasti kehittyvän alan jatkuvasta kehityksestä ja tutkimuksesta.


Ymmärtämällä ja arvostamalla näitä kehityskulkuja voimme tunnistaa sekä Bitcoin:n että Lightning Network:n monipuoliset edistysaskeleet ja mahdollisuudet digitaalisen kaupankäynnin tulevaisuudelle.


## LN:n päällä olevat protokollat


<chapterId>f4d147bb-f146-5b36-a994-b9b70da83744</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=ffee9682-1bfa-4717-9f22-9bc1baff0722:::

### Lightning-maksujen laajentaminen ja integrointi


#### Lightning-maksujen ymmärtäminen


Ennen Lightning-maksujen laajennuksiin ja integraatioihin syventymistä on tärkeää ymmärtää Lightning-maksun perustoiminta. Tavalliseen Lightning-maksuun kuuluu useita keskeisiä osia: **maksaja**, **maksunsaaja** ja itse **Lightning Network**. Maksaja käynnistää maksun maksunsaajalle luomalla **Invoice**, joka sisältää kriittiset tiedot, kuten maksettavan summan ja määränpään (maksunsaajan solmun).


Prosessi perustuu **Hash Time-Locked Contracts (HTLC) -sopimuksiin**, joilla varmistetaan, että maksuja voi hakea vain oikeutettu vastaanottaja tietyn ajan kuluessa. Kaksi tärkeää Elements tässä mekanismissa ovat **Onion eouting** ja **HTLC-ketju**:



- Sipulin reititys**: Tarjoaa yksityisyyden suojaa kapseloimalla transaktiotiedot kerroksiin ja varmistamalla, että kukin välittäjä tietää vain edeltävän ja seuraavan solmun mutta ei koko reittiä.
- HTLC-ketju**: Sarja sopimuksia, jotka lukitsevat varat, kunnes maksu on joko suoritettu tai peruutettu.


Uudempi protokolla, joka parantaa Lightning Network:n ominaisuuksia, on **Keysend**. Toisin kuin perinteiset menetelmät, jotka edellyttävät lähettäjän ja vastaanottajan välistä ennakkoviestintää generate:n ja Invoice:n välille, Keysend mahdollistaa **lähettäjän aloitteesta tapahtuvat maksut**, mikä sujuvoittaa prosessia ja parantaa käyttäjäkokemusta.


Perinteisillä laskuilla on kuitenkin rajoituksensa. Esimerkiksi:



- Kertakäyttöinen**: Laskuja käytetään yleensä vain yhteen tapahtumaan, mikä voi olla hankalaa.
- Kokorajoitukset**: Suuria laskuja voi olla vaikea käsitellä QR-koodin muodossa, mikä tekee niistä epäkäytännöllisiä tietyissä sovelluksissa.


**Määritelmät:**


- **Invoice**: Lightning Network:n maksupyyntö, joka sisältää yleensä summan ja vastaanottajan tiedot.
- **HTLC (Hash aikalukittu Contract)**: Smart contract-tyyppi, jota käytetään varmistamaan ehdolliset maksut määräajassa.
- **Sipulireititys**: Sipulireititys: Tietosuojaustekniikka, jossa transaktiotiedot kerrostetaan sipulin tavoin lähettäjän ja vastaanottajan henkilöllisyyden suojaamiseksi.

### Protokollat ja käyttötapaukset


Liiketoimintamallit ja kehittyneet protokollat

perinteisten laskujen rajoituksista huolimatta on kehitetty useita protokollia, joilla laajennetaan ja parannetaan salamamaksuja.



- LNURL**: Protokolla, joka yksinkertaistaa Invoice:n tuottamista mahdollistamalla laskujen luomisen dynaamisesti, tukemalla fiat-nimityksiä ja mahdollistamalla **Lightning-osoitteiden** käytön. Tämä lähestymistapa parantaa huomattavasti käyttäjäkokemusta tarjoamalla joustavampia maksutapoja ja integroitumista erilaisiin käyttötapauksiin.



- Bolt 12 tarjousta**: Tämä protokolla on samankaltainen kuin LNURL, mutta se käyttää **Sipuliviestintää** parantamaan yksityisyyttä. Bolt 12:n avulla käyttäjät voivat hakea laskut automaattisesti ilman manuaalisia toimenpiteitä, mikä parantaa sekä yksityisyyttä että käytettävyyttä.


Yksi merkittävä Lightning-maksujen integrointi on **Nostr**, joka on hajautettu sosiaalisen median alusta. Nostr integroi Lightning-maksut mahdollistamaan juomarahat ja mikrotransaktiot, mikä osoittaa, miten Lightning voidaan integroida erilaisiin sovelluksiin.


Toinen protokolla, **RGB**, laajentaa Lightningin toimintoja entisestään mahdollistamalla **omaisuuden siirrot** Lightning Network:n kautta. RGB mahdollistaa erilaisten omaisuuserien, myös tokeneiden, siirron Lightning-kanavien kautta, mikä laajentaa transaktioiden soveltamisalaa.


*myös *Lightning Liquidity Service Providers (LSP)** ovat ratkaisevassa asemassa Lightning-maksujen laajentamisessa. LSP:t tarjoavat likviditeettiä maksujen vastaanottamiseen, auttavat avaamaan **kaksinkertaisesti rahoitettuja kanavia** ja varmistavat saumattomat transaktiot pysäyttämällä maksut ja avaamalla kanavia lennossa.


**Määritelmät:**


- **LNURL**: Protokolla, joka mahdollistaa dynaamisen Invoice:n luomisen ja tekee maksamisesta helpompaa ja joustavampaa.
- **Bolt 12**: Lightningin laajennus, joka hyödyntää Onion-viestintää yksityisyyden suojaamiseksi ja automatisoi Invoice noutoa.
- **Nostr**: Hajautettu alusta, joka integroi LProtokollat ja käyttötapaukset
- Lightning-maksut mikrotransaktioista.
- **RGB-protokolla**: Protokolla, joka mahdollistaa varojen, kuten polettien, siirron Lightning Network:n kautta.
- **LSP (Lightning Service Provider)**: Yhteisö, joka tarjoaa likviditeettiä ja avaa kanavia Lightning-tapahtumille, jolloin verkko on paremmin käyttäjien käytettävissä.

### Liiketoimintamallit ja kehittyneet protokollat


Salamamaksujen kehittyminen on avannut tietä uusille liiketoimintamalleille, erityisesti **Valopalveluntarjoajille (LSP)**. LSP-palveluntarjoajat parantavat käyttäjäkokemusta avaamalla kanavat vain silloin, kun maksuja havaitaan, ja vähentävät näin esiasetusten monimutkaisuutta.


Yksi esimerkki Lightningin mahdollistamasta liiketoimintamallista on **huutokauppamalli**. Tässä palvelin pitää korkeimman tarjouksen ja hylkää alhaisemmat tarjoukset, jolloin maksut pysyvät odottamassa huutokaupan päättymiseen asti. Näin vältetään palautusten tarve ja tehostetaan huutokauppaprosessia.


Toinen käytännön esimerkki on **pokeripelit**, joissa palvelin hallinnoi maksuja pidättämällä panoksia pelin päättymiseen asti, mikä varmistaa vedonlyönnin sujuvuuden.


Lightning-maksuja integroidaan myös alustoihin, kuten **Nostr**:iin ja podcast-palveluihin, mikä osoittaa näiden protokollien monipuolisuuden. Lisäksi maksujen **esikuvia** voidaan käyttää **pääsyavaimina** sisällön tai palvelujen avaamiseksi, mikä lisää Lightning Network:n hyödyllisyyttä.


Edistyneet protokollat, kuten **Point Time-Locked Contracts (PTLCs)**, vievät Lightningin vielä pidemmälle mahdollistamalla monimutkaisemmat salausoperaatiot. PTLC:t tarjoavat parannuksia reititykseen ja maksujen jakamiseen, mikä parantaa sekä turvallisuutta että tehokkuutta.


Protokollat, kuten **LNURL** ja **Bolt 12**, virtaviivaistavat maksuja vähentämällä manuaalista vuorovaikutusta ja varmistavat, että Lightning Network on käyttäjäystävällisempi ja laajemmin käytössä.


**Määritelmät:**


- **PTLC (Point Time-Locked Contract)**: Salausmenetelmä, joka parantaa HTLC:tä ja mahdollistaa joustavammat ja turvallisemmat maksut.
- **Esi-kuva**: Arvo, jota käytetään HTLC:n lukituksen avaamiseen ja joka voi toimia myös palveluiden pääsyavaimena.
- **Huutokauppamalli**: Maksumalli, jossa maksuja odotetaan huutokaupan aikana ja ne vapautetaan vasta, kun korkein tarjous on hyväksytty.

### Päätelmä


Lightning-maksujen laajentaminen ja integrointi eri protokollien ja käyttötapausten avulla osoittaa Lightning Network:n dynaamisen kehityksen. Maksujen perustoimintojen parantamisesta kehittyneiden liiketoimintamallien ja salausprotokollien käyttöönottoon Lightningin tulevaisuus lupaa paljon innovaatioita ja laajaa käyttöönottoa.




## Joinmarketin ymmärtäminen


<chapterId>f109f64f-9b73-5fbf-8870-5d34d5b69df8</chapterId>

<professorId>6cfd206c-53b8-47a0-bbf4-44fd84e6ee1d</professorId>


:::video id=b89f2064-f2e1-49c3-97d0-580891eee1dd:::

Adam Gibson tarjoaa tietoa Joinmarketista ja kertoo yksityiskohtaisesti, miten tämä CoinJoin-toteutus parantaa Bitcoin:n yksityisyyttä ja vaihdettavuutta. Hän kertoo, miten Joinmarket helpottaa Trustless-yhteistyötä, Trustless ja anonyymejä liiketoimia Bitcoin-ekosysteemissä. Toisessa osassa hän näyttää, miten Joinmarketia käytetään Signetissä.

