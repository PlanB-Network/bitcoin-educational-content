---
name: Bitaxen avoimen lähdekoodin Mining-mestaruus
goal: Hallitse koko Bitaxe-ekosysteemi laitteiston kokoonpanosta edistyneeseen räätälöintiin ja suorituskyvyn optimointiin
objectives: 

  - Ymmärtää avoimen lähdekoodin Bitcoin mining -laitteiston filosofian
  - Bitaxe mining -laitteiden rakentaminen tyhjästä alkaen
  - mining-ohjelmiston konfigurointi ja optimointi, mukaan lukien AxeOS ja Public Pool
  - Suorituskyvyn edistyneiden optimointien toteuttaminen, mukaan lukien ylikellotus ja vertailuanalyysit

---

# Bitaxe Mining -oppaasi


Tervetuloa kattavalle Bitaxe-kurssille, jossa opit hallitsemaan vallankumouksellisen avoimen lähdekoodin Bitcoin mining-laitteiston, joka demokratisoi mining-teknologian saatavuuden. Tämä kurssi vie sinut hajautetun mining:n filosofisten perusteiden ymmärtämisestä edistyneisiin laitteiston räätälöinti- ja suorituskyvyn optimointitekniikoihin.


Bitaxe-projekti edustaa Bitcoin mining:n paradigman muutosta, sillä se murtaa ASIC-valmistajien monopolin tarjoamalla täysin avoimen lähdekoodin malleja, laiteohjelmistoja ja ohjelmistoja. Näiden käytännönläheisten lukujen avulla saat käytännön taitoja laitteiston kokoonpanosta, ohjelmistokokoonpanosta, piirilevysuunnittelusta ja suorituskyvyn optimoinnista.


Aiempaa mining-kokemusta ei vaadita, mutta elektroniikan perustiedot ja GitHubin tuntemus ovat hyödyllisiä. Kurssilla muutut uteliaasta tarkkailijasta kyvykkääksi Bitaxen rakentajaksi ja tekijäksi.


+++


# Johdanto


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Kurssin yleiskatsaus


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Tervetuloa kurssille MIN 306 _**Bitaxe Open Source Mining Mastery**_, joka on kattava matka Bitaxe mining:n maailmaan. Tämä kurssi on suunniteltu niille, jotka haluavat ymmärtää, rakentaa ja optimoida oman Bitaxe mining -laitteistonsa ja tutkia samalla filosofisia ja teknisiä perusteita, jotka tekevät tästä projektista ainutlaatuisen Bitcoin-ekosysteemissä.


### Bitaxen ymmärtäminen


Ensimmäisessä osiossa luodaan olennainen perusta: tutustut Bitaxe-projektin syntyyn, sen kehitykseen ja sitä määrittäviin hajauttamisen ja avoimuuden arvoihin. Opit, mikä Bitaxe on, miten se eroaa omistetuista ASIC-piirilevyistä ja mistä löydät yhteisön resursseja tietojesi syventämiseksi. Tämä osio tarjoaa kontekstin, jota tarvitaan ymmärtämään, miksi Bitaxe edustaa käännekohtaa Bitcoin mining:n historiassa.


### Ohjelmistot ja toiminnot


Toisessa osassa keskitytään ohjelmistoympäristöön ja esitellään yksityiskohtaisesti *AxeOS*: erityisesti Bitaxe-laitteille suunniteltu avoimen lähdekoodin käyttöjärjestelmä. Opit sen pääominaisuudet sekä sen, miten konfiguroit ja olet vuorovaikutuksessa laitteesi kanssa, jotta voit aloittaa ensimmäisen mining-toiminnon.


### Yhteisö ja yhteistyö


Kolmannessa jaksossa korostetaan hankkeen yhteistoiminnallista ulottuvuutta. Tutustut avoimen lähdekoodin filosofiaan, jota sovellettiin sekä Bitaxen laitteiston että ohjelmistojen kehittämiseen. Käytännön harjoitusten avulla opit, miten voit osallistua suoraan lähdekoodin kehittämiseen, ja tutustut myös _Public Pooliin_, joka on yhteisöllinen alusta laskentatehon yhdistämiseen. Opit myös, miten se asennetaan Umbrel-solmuun paikallista ja suvereenia integrointia varten.


### Laitteiston kokoonpano ja vianmääritys


Neljännessä osiossa tutustut itse laitteistoon. Opit tunnistamaan Bitaxen kokoamiseen tarvittavat työkalut, korjaamaan juotosongelmat ja suorittamaan täydellisen diagnoosin *AxeOS*:n ja USB-työkalujen avulla. Tässä osiossa painotetaan käytännön harjoittelua ja syvällistä ymmärrystä siitä, miten laitteiston ja ohjelmiston osat ovat vuorovaikutuksessa keskenään.


### Kehittynyt räätälöinti


Viides osio on omistettu räätälöinnille. Opit muokkaamaan piirilevyä (PCB), luomaan tehdastiedoston ja käyttämään _Bitaxe Web Flasheriä_. Tämä osio on suunnattu niille, jotka haluavat mennä yksinkertaista kokoonpanoa pidemmälle ja todella suunnitella räätälöityjä versioita omasta laitteestaan.


### Suorituskyvyn optimointi


Kuudennessa osassa käsitellään kehittyneitä optimointitekniikoita. Opit, miten voit suorittaa Bitaxe-vertailun sen suorituskyvyn arvioimiseksi ja miten voit ylikellottaa sitä tehokkaasti. Näiden taitojen avulla saat laitteistostasi kaiken irti kunnioittaen sen fyysisiä rajoituksia.


Kuten jokaisella Plan ₿ Academyn kurssilla, loppuosa sisältää arvioinnin, jonka tarkoituksena on vahvistaa tietojasi.


Sukella suoraan tähän tekniseen seikkailuun - Bitcoin mining:n tulevaisuus on sinun käsissäsi!


# Bitaxen ymmärtäminen

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## Historia

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

Bitaxe-hanke edustaa uraauurtavaa muutosta Bitcoin [mining](https://planb.academy/resources/glossary/mining)-laitteistojen kehittämisessä, sillä se tuo avoimen lähdekoodin periaatteet alalle, jota hallitsevat omistajakohtaiset ratkaisut. Tässä koulutussarjassa tutustutaan Bitaxen kattavaan historiaan, teknisiin innovaatioihin ja yhteisölähtöiseen kehitykseen ja nähdään, miten yhden insinöörin visio muuttui kukoistavaksi hajautetun mining-laitteiston ekosysteemiksi. Tarkastelemalla projektin alkuperää, haasteita ja saavutuksia saamme arvokasta ymmärrystä sekä [ASIC](https://planb.academy/resources/glossary/asic)-kehityksen teknisistä monimutkaisuuksista että avoimen lähdekoodin yhteistyön voimasta Bitcoin-alalla.


### Alkuperätarina: Solar Mining -visioon


Bitaxen perustaja Skot aloitti matkansa Bitcoin:n pariin collegen juhlissa, jossa hän sai tietää Bitcoin:stä jonkun Silkkitien kautta ostaneen henkilön kautta. Tämä ensimmäinen altistuminen Bitcoin:lle, jonka hinta oli noin 20 dollaria kolikolta, herätti uteliaisuuden, joka myöhemmin kehittyi vallankumoukselliseksi mining-projektiksi. Tekninen perusta hänen tulevalle työlleen luotiin hänen opiskeluaikanaan yliopistossa, jossa hänellä oli käytössään laajat FPGA-resurssit laboratorioympäristössä. Työskennellessään yhdessä ohjaajansa kanssa Skot alkoi kokeilla avoimen lähdekoodin FPGA-bittivirtoja Bitcoin mining:tä varten, aluksi vaatimattomana tavoitteena oli saada mining:lle tarpeeksi Bitcoin:tä, jotta he voisivat ostaa pizzan toimistoonsa.


Siirtyminen akateemisesta kokeilusta vakavaan kehitystyöhön tapahtui vuosia myöhemmin, kun Skot työskenteli aurinkoenergialla toimivien yhdyskäytävien parissa etäluentatietojen keräämistä varten Afrikassa. Tämä ammattikokemus aurinkoenergiajärjestelmistä herätti ymmärryksen siitä, että Bitcoin mining ASIC:t, jotka ovat pohjimmiltaan pienjännitteisiä tasavirtalaitteita, sopivat täydellisesti yhteen aurinkopaneelien kanssa. Konsepti vaikutti luonnolliselta ja tyylikkäältä. Kun Skot alkoi tutkia olemassa olevia ratkaisuja, hän havaitsi kuitenkin merkittävän aukon markkinoilla: toisin kuin Bitcoin mining:n alkuaikoina, jolloin FPGA-mallit olivat avoimesti saatavilla, ASIC-piirien tulo oli siirtänyt alan kohti täysin omia, suljetun lähdekoodin ratkaisuja.


Avoimen lähdekoodin mining-laitteiston puute alkoi turhauttaa Skotia, etenkin kun otetaan huomioon hänen taustansa avoimen lähdekoodin ohjelmistokehityksessä ja hänen uskonsa siihen, että Bitcoin:n avoimen lähdekoodin luonteen pitäisi ulottua myös mining-infrastruktuuriin. Tämä filosofinen linjaus avoimen lähdekoodin periaatteisiin yhdistettynä tekniseen haasteeseen, joka liittyi ASIC:n omien mallien käänteiseen suunnitteluun, loi pohjan sille, mistä tuli Bitaxe-projekti. Alkuperäinen visio oli kunnianhimoinen mutta käytännöllinen: luoda aurinkoenergialla toimiva Bitcoin-kaivoslaite, joka voisi toimia itsenäisesti tarvitsematta erillistä tietokonetta ohjaukseen, jolloin se soveltuisi käytettäväksi syrjäisissä paikoissa aurinkopaneelien alla.


### Tekniset haasteet ja käänteistekniikan läpimurrot


Bitaxen kehittäminen vaati huomattavien teknisten esteiden voittamista, jotka keskittyivät pääasiassa Bitmainin ASIC-sirujen dokumentoinnin täydelliseen puuttumiseen. Skotin lähestymistapa tähän haasteeseen oli esimerkki määrätietoisuudesta ja kekseliäisyydestä, joita tarvitaan onnistuneeseen reverse engineeringiin. Ilman virallisia tietolehtiä tai teknisiä eritelmiä hän turvautui sirujen tutkimiseen mikroskoopilla, nastojen etäisyyksien mittaamiseen mittatikulla ja jopa sirujen skannaamiseen määrittääkseen niiden tarkat pohjapintavaatimukset. Tämä vaivalloinen prosessi johti useisiin epäonnistuneisiin prototyyppeihin, ja kaksi ensimmäistä "day miner" -iteraatiota eivät toimineet kunnolla virheellisten jalanjälkilaskelmien vuoksi.


Läpimurto tapahtui kolmannessa iteraatiossa toukokuussa 2022, jolloin Skot onnistui luomaan toimivan kahden sirun mallin käyttämällä Antminer S9 -yksiköistä kerättyjä BM1387-siruja. Tämä saavutus merkitsi Bitaxe-nimen syntyä, joka oli saanut inspiraationsa Bitcoin mining:n kiikarikonseptista. Suunnittelun onnistuminen vahvisti käänteisen suunnittelun lähestymistavan ja osoitti, että riippumattomat kehittäjät voivat luoda toimivia mining-laitteita ilman valmistajan tukea. Tekniset haasteet ulottuivat kuitenkin sirurajapinnan lisäksi monimutkaiseen virtalähteen suunnitteluun, sillä ASIC-piirien jännitteen säätö oli tarkkaa suurilla virroilla, ja ne toimivat usein vain 0,6 voltin jännitteellä ja ottivat samalla huomattavan paljon virtaa.


Laiteohjelmiston kehittäminen oli toinen monimutkainen vaihe, sillä hankkeessa oli luotava mining-ohjelmisto, jota voitiin käyttää suoraan ESP32-mikrokontrollerissa sen sijaan, että olisi tarvittu ulkoisia tietokoneita, joissa oli CGMinerin kaltainen ohjelmisto. Tämä itsenäinen lähestymistapa oli olennaisen tärkeä Skotin visiolle käyttöönotettavista, itsenäisistä mining-yksiköistä. Laitteiston reverse engineeringin ja sulautetun laiteohjelmiston kehittämisen yhdistelmä loi kattavan teknisen haasteen, joka vaati asiantuntemusta useilta eri aloilta, sähkötekniikasta ja piirilevysuunnittelusta sulautettuun ohjelmointiin ja verkkoprotokolliin.


### Yhteisön muodostaminen ja avoimen lähdekoodin yhteistyö


Bitaxen muuttuminen sooloprojektista kukoistavaksi yhteisöaloitteeksi on yksi sen menestyksen merkittävimmistä tekijöistä. Aluksi Skot yritti saada generate:tä kiinnostumaan Bitcoin:n foorumeilla ja sosiaalisessa mediassa, mutta vaste oli vähäistä ja ajoittain epäilevää. Läpimurto tapahtui, kun SirVapesAlotin kaltaiset yhteisön jäsenet tunnistivat avoimen lähdekoodin mining potentiaalin ja perustivat Open Source Miners United (OSMU) Discord-palvelimen. Tämä foorumi tarjosi projektin kukoistukselle välttämättömän yhteistyöympäristön, joka houkutteli erilaisista taustoista tulevia osallistujia, jotka jakoivat yhteisen kiinnostuksen Bitcoin mining -teknologian demokratisointiin.


Yhteisölähtöinen kehitysmalli osoittautui huomattavan tehokkaaksi, ja johnny9:n ja Benin kaltaiset avainhenkilöt ryhtyivät ratkaisemaan erityisiä teknisiä haasteita. Johnny9:n asiantuntemus laiteohjelmistokehityksessä ratkaisi kriittiset ohjelmistototeutusongelmat, kun taas Benin front-end-kehitystaidot loivat intuitiivisen AxeOS-kojelaudan, joka yksinkertaisti laitteen konfigurointia ja seurantaa. Benin lisäpanokseen kuului myös valmistusvalmiuksien luominen ja Public Poolin, Bitaxe-laitteille optimoidun avoimen lähdekoodin [mining-poolin](https://planb.academy/resources/glossary/pool-mining), luominen. Tämä yhteistyöhön perustuva lähestymistapa osoitti, miten avoimen lähdekoodin periaatteet voivat nopeuttaa kehitystä enemmän kuin mihin yksittäinen tekijä yksin pystyisi.


OSMU-yhteisö edisti myös osallistavaa ympäristöä, jossa uudet tulokkaat pystyivät oppimaan ja antamaan panoksensa alkuperäisestä teknisestä asiantuntemuksestaan riippumatta. Benin oma matka juottamisen aloittelijasta suureksi valmistajaksi on esimerkki tästä tervetulleesta lähestymistavasta taitojen kehittämiseen. Yhteisön sitoutuminen koulutukseen ja keskinäiseen tukeen loi myönteisen kierteen, jossa kokeneet jäsenet opastivat uusia tulokkaita, joista tuli sitten itsekin osallistujia. Tämä malli osoittautui olennaisen tärkeäksi, jotta hanke voitiin skaalata alkuperäistä laajemmaksi ja luoda kestävä ekosysteemi jatkuvaa innovointia ja kasvua varten.


### Hajautetun Mining:n visio ja tuleva vaikutus


Skotin pitkän aikavälin visio Bitaxesta on paljon laajempi kuin uuden mining-laitteen luominen: se on Bitcoin:n mining-maiseman perustavanlaatuinen muutos. Kunnianhimoinen tavoite tuottaa miljoona yhden terahashin [louhijaa](https://planb.academy/resources/glossary/miner) loisi mining:n hajautetun tehon exahashin, mikä olisi merkittävä askel kohti mining:n hajauttamista. Tämä visio vastaa kriittisiin huolenaiheisiin, jotka liittyvät mining:n keskittämiseen, jossa suuret altaat ja teolliset toiminnot saattavat joutua hallituksen painostuksen tai sääntelyn kohteeksi. Jakamalla mining:n teho lukemattomien kotikaivostoimijoiden kesken verkosta tulee joustavampi ja Bitcoin:n hajautettujen periaatteiden mukainen.


Tätä visiota tukeva talousmalli perustuu koti-mining:n ainutlaatuisiin ominaisuuksiin, joissa infrastruktuurikustannukset ovat lähes olemattomat ja kaivostyöntekijät voivat toimia minimaalisella valvonnalla. Toisin kuin teolliset mining-toiminnot, jotka edellyttävät massiivisia pääomasijoituksia laitoksiin, sähköinfrastruktuuriin ja jäähdytysjärjestelmiin, kotikaivostoiminnan harjoittajat voivat yksinkertaisesti kytkeä laitteet olemassa oleviin pistorasioihin ja internet-yhteyksiin. Tämä lähestymistapa voisi teoriassa tuoda merkittävän [hash-asteen](https://planb.academy/resources/glossary/hashrate) verkkoon ilman perinteisiä markkinoille pääsyn esteitä, jotka ovat tyypillisiä laajamittaisille mining-toiminnoille.


Hankkeen menestys on jo alkanut vaikuttaa laajempaan Bitcoin mining-ekosysteemiin, ja se voi innostaa muitakin valmistajia omaksumaan avoimen lähdekoodin kehitysmalleja. Bitaxe-valmistajien osoittama taloudellinen elinkelpoisuus osoittaa, että avoimen lähdekoodin laitteisto voi olla kaupallisesti menestyksekäs ja samalla säilyttää avoimuuden ja yhteisön osallistumisen. Kun hanke kehittyy edelleen uusien siruintegraatioiden, parempien mallien ja laajempien valmistuskumppanuuksien myötä, se toimii konseptitodisteena siitä, miten Bitcoin mining voi palata hajautettuihin juuriinsa samalla kun se omaksuu nykyaikaista ASIC-teknologiaa. Perimmäinen tavoite ulottuu pelkkää hash-nopeuden levittämistä pidemmälle ja sisältää myös koulutusvaikutuksia, jolloin yhä useammat ihmiset pääsevät suoraan kosketuksiin Bitcoin:n mining:n perusprosessin kanssa ja edistävät syvempää ymmärrystä verkon turvallisuusmallista.


## Mikä on Bitaxe?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Laitteiston yleiskatsaus ja ominaisuudet


Bitaxe-ekosysteemi käsittää useita laitteistokierroksia, joista jokainen on suunniteltu optimoimaan mining-kokemuksen eri osa-alueita säilyttäen samalla avoimen lähdekoodin saavutettavuuden perusfilosofian. Nämä laitteet toimivat paitsi toimivina mining-laitteistoina myös opetusvälineinä, joiden avulla käyttäjät voivat ymmärtää ASIC-sirujen, mikrokontrollereiden ja Bitcoin mining-prosessin välisen monimutkaisen suhteen. Bitaxen suunnittelufilosofian ja teknisen toteutuksen ymmärtäminen antaa arvokasta tietoa siitä, miten nykyaikainen mining-laitteisto toimii sekä komponentti- että järjestelmätasolla.



### Bitaxe Max, ensimmäisen sukupolven toteutus


Bitaxe Max edustaa Bitaxe-konseptin perustoteutusta, jossa käytetään BM1397 ASIC -sirua, jonka Bitmain on alun perin kehittänyt S17 mining -sarjaansa varten. Tämä siruintegraatio osoittaa, miten avoimen lähdekoodin laitteisto voi käyttää uudelleen olemassa olevaa ASIC-teknologiaa helppokäyttöisten mining-ratkaisujen luomiseksi. Bitaxe Max tuottaa arviolta 300-400 gigahashia sekunnissa, mikä tekee siitä pikemminkin koulutus- ja kokeilualustan kuin kaupallisen mittakaavan mining-ratkaisun.


BM1397-sirun integrointi Bitaxe Maxiin vaati virranhallinnan, lämmönsäätelyn ja viestintäprotokollien huolellista harkintaa. Piirilevyn suunnittelu vastaa tämän ASIC:n erityisvaatimuksia ja tarjoaa samalla vakaan toiminnan edellyttämät tukipiirit. Tämä toteutus osoittaa, miten avoimen lähdekoodin laitteistokehityksessä voidaan hyödyntää olemassa olevaa puolijohdeteknologiaa uusien sovellusten ja oppimismahdollisuuksien luomiseksi mining-yhteisössä.


### Bitaxe Ultra, kehittynyt sirutekniikka


Bitaxe Ultra edustaa Bitaxe-alustan evoluutiota, ja se sisältää Bitmainin S19-sarjan kehittyneemmän BM1366 ASIC -piirin. Tämä uudempi siruteknologia tuo Bitaxe-alustaan entistä paremmat tehokkuus- ja suorituskykyominaisuudet säilyttäen kuitenkin saman suunnittelun perusfilosofian. Päivitys BM1366-piiriin osoittaa alustan mukautumiskykyä ja yhteisön sitoutumista teknologisen kehityksen sisällyttämiseen avoimen lähdekoodin mining-ratkaisuihin.


Siirtyminen BM1397-sirusta BM1366-siruun vaati muutoksia piirilevyn virransyöttöjärjestelmiin, lämmönhallintaan ja ohjausalgoritmeihin. Nämä muutokset ovat osoitus laitteistokehityksen iteratiivisesta luonteesta ja yhteensopivuuden säilyttämisen tärkeydestä samalla kun suorituskykyä parannetaan. Bitaxe Ultra -toteutus tarjoaa käyttäjille mahdollisuuden käyttää uusinta ASIC-teknologiaa säilyttäen samalla alustan opetuksellisen ja kokeellisen luonteen.


### Mikrokontrolleri ja viestintäjärjestelmät


Jokaisen Bitaxe-laitteen ytimessä on ESP-mikrokontrolleri, joka toimii ensisijaisena käyttöliittymänä käyttäjän ja ASIC-sirun välillä. Tällä mikrokontrollerilla toimii Open Source Miners United (OSMU) -yhteisön kehittämä erikoisohjelmisto, joka mahdollistaa ASIC:n toimintaparametrien tarkan hallinnan. Mikrokontrollerin ja ASIC:n välinen viestintä tapahtuu huolellisesti suunniteltujen sarjaliikennelinjojen kautta, jotka on kaiverrettu suoraan piirilevylle näkyviksi jäljiksi.


Mikrokontrollerin rooli on laajempi kuin pelkkä ASIC:n ohjaus: siihen kuuluu virranhallinta, lämpötilan seuranta ja käyttöliittymätoiminnot. Integroidun näytön kautta käyttäjät voivat seurata kriittisiä toimintaparametreja, kuten lämpötilaa, hash-nopeutta, IP-osoitetta ja muita tärkeitä mining-tilastoja. Tämä reaaliaikainen palautejärjestelmä tarjoaa arvokasta tietoa laitteen suorituskyvystä ja auttaa käyttäjiä optimoimaan mining:n toimintaa samalla kun he oppivat laitteiston taustalla olevasta käyttäytymisestä.


### Virranhallinta ja turvallisuusnäkökohdat


Bitaxe-alusta toimii tiukalla 5 voltin virtavaatimuksella, joten oikea virtalähteen valinta on ratkaisevan tärkeää laitteen pitkäikäisyyden ja turvallisuuden kannalta. Bitaxe-levyjen virranhallintajärjestelmä sisältää kehittyneitä piirejä, jotka on suunniteltu säätelemään jännitteen syöttöä ASIC-sirulle ja valvomaan samalla virrankulutusta eri toimintatiloissa. Tämän virranhallintaominaisuuden ansiosta laite toimii tehokkaasti eri sisäisten taajuuksien ja jännitteiden välillä ja kuluttaa tyypillisesti 5-25 wattia kokoonpanosta riippuen.


Tehovaatimusten ymmärtäminen on ratkaisevan tärkeää, kun otetaan huomioon, että väärä jännitteen käyttö voi vahingoittaa laitetta pysyvästi. Taajuuden, jännitteen, virrankulutuksen ja hash-nopeuden välinen suhde osoittaa ASIC:n toiminnan perusperiaatteet, joita sovelletaan kaikkiin mining-laitteisiin. Käyttäjät voivat kokeilla eri tehoasetuksia ymmärtääkseen mining-toimintoihin liittyvät tehokkuuskompromissit ja saada käytännön kokemusta käsitteistä, joita sovelletaan laajempiin mining-toteutuksiin.


### Solo Mining Focus ja verkostoon osallistuminen


Bitaxe-alusta on suunnattu erityisesti mining-sovelluksiin, joissa yksittäiset louhijat yrittävät ratkaista [Bitcoin-lohkoja](https://planb.academy/resources/glossary/block) itsenäisesti sen sijaan, että osallistuisivat suuriin mining-pooleihin. Vaikka Bitaxe-laitteiden hash-nopeus tekee onnistuneen lohkojen löytämisen tilastollisesti epätodennäköiseksi, tämä lähestymistapa palvelee tärkeitä koulutuksellisia ja filosofisia tarkoituksia Bitcoin-yhteisössä. mining:n yksinlukeminen Bitaxe-laitteilla auttaa käyttäjiä ymmärtämään Bitcoin:n [proof-of-work](https://planb.academy/resources/glossary/proof-of-work)-järjestelmän perusmekaniikkaa ja edistää samalla verkon hajauttamista.


mining:n painottaminen soolona kuvastaa OSMU-yhteisön sitoutumista yksilöllisen osallistumisen edistämiseen Bitcoin:n turvallisuusmallissa. Tarjoamalla käytettävissä olevia laitteistoja, jotka voivat toimia itsenäisesti, Bitaxe-alusta antaa käyttäjille mahdollisuuden suorittaa omia mining-toimintojaan ilman, että he ovat riippuvaisia poolin infrastruktuurista. Tämä lähestymistapa edistää Bitcoin:n [konsensusmekanismin](https://planb.academy/resources/glossary/consensus) syvempää ymmärtämistä ja tukee samalla verkon hajautettua luonnetta lisäämällä louhijoiden monimuotoisuutta.


### Laitteiston kehitys ja tuotannon parannukset


Bitaxe-alusta kehittyy jatkuvasti yhteisön palautteen ja tuotannon optimoinnin avulla, ja uusimmat versiot sisältävät parannuksia, jotka parantavat valmistettavuutta ja käyttäjäkokemusta. Versiopäivityksissä keskitytään yleensä tuotannon tehokkuuteen eikä niinkään perustavanlaatuisiin suorituskykymuutoksiin, mikä varmistaa, että nykyiset käyttäjät eivät joudu kohtaamaan vanhentumispaineita. Ominaisuudet, kuten siirtyminen micro-USB-liittimistä USB-C-liittimiin ja parannetut virtaliitäntäjärjestelmät, heijastavat yhteisön huomiota käytännön käytettävyyden parannuksiin.


Tämä evolutiivinen lähestymistapa on osoitus avoimen lähdekoodin laitteistokehityksen hyödyistä, sillä yhteisön panos johtaa asteittaisiin parannuksiin, jotka hyödyttävät kaikkia käyttäjiä. Filosofia "if it hashes, it hashes" korostaa alustan keskittymistä toiminnallisuuteen jatkuvien päivitysten sijasta ja kannustaa käyttäjiä ylläpitämään ja käyttämään laitteitaan uusimpien versioiden tavoittelun sijasta. Tämä lähestymistapa tukee kestäviä laitteistokäytäntöjä ja säilyttää samalla Bitaxen koulutusarvon.


## Mistä saan lisätietoja?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

Bitaxe-projekti edustaa kattavaa avoimen lähdekoodin mining-aloitetta, joka ulottuu paljon yksittäistä laitetta laajemmalle. Sen ymmärtäminen, mistä löytää luotettavaa tietoa, teknisiä resursseja ja yhteisön tukea, on ratkaisevan tärkeää kaikille, jotka haluavat osallistua tähän ekosysteemiin. Tässä luvussa on kattava opas olennaisista alustoista ja resursseista, jotka muodostavat Bitaxe- ja Open Source Miners United (OSMU) -yhteisön perustan.


### Bitaxe.org, keskushubi


Bitaxe.org-sivusto toimii ensisijaisena porttina kaikkiin hankkeeseen liittyviin tietoihin ja resursseihin. Tämä keskitetty foorumi toimii ensimmäisenä viitepisteenä aina, kun haluat oppia lisää Bitaxe-laitteista tai tutustua muihin OSMU-yhteisön hankkeisiin. Verkkosivuston suunnittelussa on asetettu etusijalle helppokäyttöisyys ja organisointi, ja kävijöille esitetään huolellisesti kuratoituja linkkejä, jotka johtavat erilaisiin erikoistuneisiin resursseihin koko ekosysteemissä.


Tämän keskitetyn keskuksen merkitystä ei voi liioitella, sillä se poistaa sekaannuksen, joka usein liittyy hajautettuihin avoimen lähdekoodin projekteihin. Käyttäjät voivat luottaa siihen, että Bitaxe.org tarjoaa ajantasaiset ja tarkistetut linkit kaikkiin tärkeimpiin resursseihin sen sijaan, että he etsisivät tietoja useilta eri alustoilta tai luottaisivat epävirallisista lähteistä saataviin, mahdollisesti vanhentuneisiin tietoihin. Tämä lähestymistapa varmistaa, että sekä uudet tulokkaat että kokeneet yhteisön jäsenet voivat tehokkaasti löytää projektinsa tarvitsemat tiedot.


### Tekniset resurssit ja kehittämismateriaalit


GitHubissa oleva laitteiston suunnittelutiedostojen arkisto on yksi arvokkaimmista resursseista kaikille, jotka ovat kiinnostuneita Bitaxe-laitteiden ymmärtämisestä tai rakentamisesta. Tämä julkinen arkisto sisältää kattavan dokumentaation, joka kattaa kaikki laitteiston suunnitteluprosessin osa-alueet alkuperäisistä konsepteista lopullisiin valmistusmäärittelyihin. Arkisto sisältää yksityiskohtaisia kuvia, projektin tavoitteita, ominaisuuksien kuvauksia ja sisäänrakennettujen komponenttien selityksiä, jotka tarjoavat sekä teknistä syvyyttä että käytännön ohjeita.


Niille, jotka ovat kiinnostuneita valmistamaan omia laitteitaan, arkisto sisältää erityisiä dokumentaatiotiedostoja, kuten building.md, jossa annetaan vaiheittaiset ohjeet koko tuotantoprosessista. Tämä dokumentaatio kattaa piirilevysuunnitteluun tarvittavat ohjelmistotyökalut, menettelyt tiedostojen lähettämiseksi valmistajille sekä vaiheet, jotka liittyvät valmistettujen piirilevyjen vastaanottamiseen ja validointiin. Tämä yksityiskohtaisuuden taso takaa, että yksittäiset henkilöt tai pienet organisaatiot voivat menestyksekkäästi navigoida valmistusprosessissa ilman laajaa aiempaa kokemusta laitteistotuotannosta.


ESP-Miner-tietovarasto toimii kaiken laiteohjelmistoon liittyvän koodin ja dokumentaation keskitettynä säilytyspaikkana. Tämä GitHub-arkisto sisältää jokaisen Bitaxe-ohjelmistoon kirjoitetun koodirivin sekä kattavan dokumentaation, jossa selitetään järjestelmävaatimukset, laitteistomääritykset ja konfigurointivaihtoehdot. Arkiston rakenne on suunniteltu niin, että se sopii sekä käyttäjille, jotka haluavat valmiiksi käännettyjä binääritiedostoja, että kehittäjille, jotka haluavat rakentaa laiteohjelmiston lähdekoodista.


Tämän arkiston dokumentaatio sisältää yksityiskohtaisia osioita laitteistovaatimuksista, esikonfigurointivaihtoehdoista ja eri asetusten suositelluista arvoista. Nämä tiedot ovat korvaamattomia käyttäjille, jotka haluavat mukauttaa laitteitaan tai korjata tiettyjä ongelmia. Lisäksi arkisto sisältää tietoa uudemmista kehityskohteista, kuten Raspberry Pi -integraatiosta, mikä varmistaa, että dokumentaatio pysyy ajan tasalla projektin jatkuvan kehityksen myötä.


### Laitteiden hallinta- ja ylläpitotyökalut


Bitaxe-verkkovälähtö on käytännöllinen ratkaisu laitteiden ylläpitoon ja päivityksiin. Tämän verkkopohjaisen työkalun avulla käyttäjät voivat flashata laiteohjelmiston laitteisiinsa ilman erikoisohjelmia tai monimutkaisia komentorivikäytäntöjä. Flasher tukee useita laitevaihtoehtoja, kuten Bitaxe Ultraa eri porttiversioilla ja vanhempia Bitaxe Max -malleja. Käyttäjät voivat valita, päivittävätkö he olemassa olevan laiteohjelmiston web-käyttöliittymän kautta vai suorittavatko he täydellisen tehdasasetusten palautuksen USB-liitännän avulla.


Tämä työkalu vastaa yhteen laitteistoharrastajien yleisimmistä haasteista: laitteiden laiteohjelmistojen ylläpitoon ja päivittämiseen. Käyttäjäystävällisen web-käyttöliittymän avulla flasher poistaa monia teknisiä esteitä, jotka muutoin saattaisivat estää käyttäjiä pitämästä laitteitaan ajan tasalla uusimpien laiteohjelmistoversioiden kanssa. Työkalun suunnittelussa on asetettu etusijalle yksinkertaisuus, mutta samalla on säilytetty joustavuus, jota tarvitaan erilaisissa laitekokoonpanoissa ja päivitysskenaarioissa.


### Yhteisön foorumit ja viestintäkanavat


Discord-palvelin on Bitaxen ekosysteemin reaaliaikaisen vuorovaikutuksen ja tuen ydin. Palvelimen organisaatio heijastaa yhteisön jäsenten erilaisia kiinnostuksen kohteita ja tarpeita, ja sen tarkkaan jäsennellyt kanavat helpottavat kohdennettuja keskusteluja tietyistä aiheista. Uudet jäsenet joutuvat vahvistusprosessiin, joka edellyttää yhteisön sääntöjen lukemista ja hyväksymistä. Näin varmistetaan, että kaikki osallistujat ymmärtävät kunnioittavan ja tuottavan vuorovaikutuksen odotukset.


Palvelimen kanavarakenteeseen kuuluu yleisiä keskustelualueita, joissa käsitellään esimerkiksi aurinkoenergian integrointia, mining-altaita ja Bitcoin:ään liittyviä keskusteluja. Erikoistuneemmissa osioissa keskitytään tiettyihin laitteisiin, mukaan lukien Bitaxe Ultra-, Hex- ja Supra-muunnoksille omistetut kanavat. Firmware-kanava tarjoaa keskitetyn tilan teknisille keskusteluille ohjelmistokehityksestä ja vianmäärityksestä, kun taas viralliset tiedotteet -kanava varmistaa, että yhteisön jäsenet saavat ajoissa ilmoituksia uusista kehityskohteista.


Siinä on myös tilaajakohtainen alue, joka tarjoaa lisäetuja yhteisön jäsenille, jotka haluavat tukea hanketta taloudellisesti. Tämä porrastettu lähestymistapa antaa yhteisölle mahdollisuuden tarjota tehostettuja palveluja ja säilyttää samalla avoimen pääsyn tärkeisiin tieto- ja tukikanaviin. Avustuskanava on oma tilansa vianmääritykselle ja tekniselle avulle, mikä varmistaa, että käyttäjät saavat nopeaa tukea ongelmatilanteissa.



Open Source Miners United -wiki (osmu.wiki) tarjoaa kattavaa dokumentaatiota, joka täydentää Discordissa käytäviä reaaliaikaisia keskusteluja. Toisin kuin chat-pohjaiset alustat, wiki tarjoaa jäsenneltyä, haettavissa olevaa dokumentaatiota, joka kattaa kaikki Bitaxe-projektin ja siihen liittyvien aloitteiden näkökohdat. Sen organisointitapa heijastaa projektin rakennetta, ja siinä on omat osiot eri laitesarjoille ja kattavat asennusoppaat.


Wiki on luonteeltaan avointa lähdekoodia, joten yhteisön jäsenet voivat osallistua suoraan dokumentaation kehittämiseen. Käyttäjät voivat muokata sivuja, lähettää korjauksia ja lisätä uusia tietoja GitHub-integraation kautta, mikä varmistaa tietopohjan pysymisen ajan tasalla ja avoimena. Tämä yhteistyöhön perustuva lähestymistapa hyödyntää yhteisön kollektiivista asiantuntemusta ja ylläpitää samalla laadunvalvontaa toimitettujen muutosten tarkistusprosessin avulla.


Wiki sisältää käytännön resursseja, kuten PDF-asennusoppaita, joissa annetaan vaiheittaiset ohjeet laitteen konfigurointiin ja käyttöön. Nämä oppaat toimivat arvokkaina viitteinä sekä uusille käyttäjille että kokeneille yhteisön jäsenille, jotka tarvitsevat nopeasti tietoa tietyistä menettelyistä tai konfigurointitiedoista.


### Osto- ja myyjätiedot


Bitaxen legit-luettelo vastaa avoimen lähdekoodin laitteistoyhteisön kriittiseen tarpeeseen: luotettavien myyjien tunnistamiseen ja vilpillisten myyjien välttämiseen. Tämä kuratoitu luettelo sisältää todennettuja jälleenmyyjiä ja valmistajia, jotka täyttävät tietyt laillisuus- ja yhteisön tukikriteerit. Jokainen luettelo sisältää suorat linkit myyjien verkkosivustoille, alueellisia tietoja ja yrityskuvauksia, jotka auttavat käyttäjiä tekemään tietoon perustuvia ostopäätöksiä.


Tärkeää on, että luettelosta käy ilmi, osallistuuko kukin myyjä OSMU-yhteisön toimintaan joko taloudellisesti tai muunlaisen tuen kautta. Tämä avoimuus auttaa yhteisön jäseniä ymmärtämään, mitkä myyjät tukevat aktiivisesti hankkeen kehittämistä ja kestävyyttä. Luettelo toimii myös suojana yleisiltä huijauksilta, kuten julkaisemattomien tuotteiden luvattomilta ennakkotilauksilta, jotka ovat perinteisesti aiheuttaneet ongelmia yhteisössä.


Se, että painotetaan muita kuin etuyhteydessä olevia linkkejä, osoittaa, että yhteisö on sitoutunut tarjoamaan puolueettomia myyjäsuosituksia. Käyttäjät voivat luottaa siihen, että suositukset perustuvat pikemminkin myyjän laillisuuteen ja yhteisön panokseen kuin taloudellisiin kannustimiin, mikä varmistaa, että ostopäätökset tukevat sekä yksilöllisiä tarpeita että yhteisön kestävyyttä.



# Ohjelmistot ja toiminnot

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## Mikä on AxeOS?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS on Bitaxe mining -laitteiden laiteohjelmisto- ja web-käyttöliittymä, joka tarjoaa käyttäjille täydelliset ohjaus- ja valvontaominaisuudet intuitiivisen selainpohjaisen kojelaudan kautta. Tämä järjestelmä muuttaa ASIC:n monimutkaisen hallintatehtävän helppokäyttöiseksi kokemukseksi, jonka avulla kaivostyöntekijät voivat seurata suorituskykyä, säätää asetuksia ja hallita useita laitteita yhdestä käyttöliittymästä. AxeOS:n ymmärtäminen on olennaista, jotta voit maksimoida Bitaxe-laitteesi potentiaalin ja ylläpitää optimaalista mining-toimintaa.


### Mittariston yleiskatsaus ja keskeiset mittarit


AxeOS-kojelauta toimii ensisijaisena ikkunana Bitaxe-laitteesi suorituskykyyn, ja se esittää mining:n kriittiset mittarit järjestetyssä, reaaliaikaisessa muodossa. Kun siirryt Bitaxe-laitteesi IP-osoitteeseen, näet heti neljä keskeistä suorituskykymittaria, jotka määrittelevät mining:n toiminnan nykytilan. Hash rate -näyttö näyttää todellisen laskentanopeuden, jonka ASIC-sirusi tuottaa käsitellessään nykyistä lohkomallia, ja antaa välitöntä palautetta laitteesi ydintoiminnoista.


Hash-nopeuden vieressä osakelaskuri seuraa jokaista kelvollista ratkaisua, jonka Bitaxe-laitteesi lähettää mining-pooliin, ja se kasvaa jokaisen onnistuneen lähetyksen myötä ja toimii suorana mittarina laitteesi panoksesta poolin mining-ponnisteluihin. Tehokkuusmittari antaa ratkaisevan tärkeää tietoa laitteesi energiatehokkuudesta laskemalla hash-nopeuden ja virrankulutuksen suhteen, mikä auttaa sinua optimoimaan toimintasi kannattavuuden. Paras vaikeusaste -indikaattori säilyttää tietueen korkeimmasta vaikeusasteesta, jonka laitteesi on koskaan löytänyt, ja säilyttää tämän saavutuksen jopa uudelleenkäynnistysten ja päivitysten aikana, ja nollaa sen vain, kun teet täydellisen tehdasflashin.


Kojelaudan laajennettava valikkojärjestelmä, jota ohjataan vaihtopainikkeella, tarjoaa pääsyn kaikkiin AxeOS-toimintoihin säilyttäen samalla selkeän käyttöliittymän. Live hash rate -kaavio on yksi sen arvokkaimmista ominaisuuksista, sillä se näyttää reaaliaikaiset suorituskykytiedot, jotka ovat sitä tarkempia ja informatiivisempia, mitä pidempään pidät istuntoa yllä. Virta-, lämpö- ja suorituskykyosiot tarjoavat kattavan seurannan laitteesi toimintatilasta, mukaan lukien tulojännitevaroitukset, jotka varoittavat mahdollisista virtalähdeongelmista ja varmistavat samalla, että toiminta jatkuu turvallisten parametrien sisällä.


### Edistynyt valvonta ja järjestelmätiedot


AxeOS:n seurantaominaisuudet ulottuvat paljon pidemmälle kuin perus hash-taajuuden seuranta, sillä se tarjoaa yksityiskohtaista tietoa Bitaxe-laitteesi toiminnan jokaisesta osa-alueesta. Virtaosio näyttää integroiduista piiristä johdetun laskennallisen virrankulutuksen, virtalähteen liitännästä mitatut tulojännitteet ja pyydetyt ASIC-jännitetasot. Jännitteen laskiessa AxeOS esittää välittömästi varoitusilmoituksia, jotka eivät kuitenkaan yleensä vaikuta mining:n toimintaan vaan osoittavat vain mahdollisia virtalähteen optimointimahdollisuuksia.


Lämpötilan seurannassa keskitytään ASIC-sirun lämmönhallintaan, ja lukemat otetaan laitteen strategisista paikoista, jotta saadaan tarkat lämpötiedot, joissa on asianmukaiset offsetit sirutason tarkkuuden varmistamiseksi. Taajuus- ja jännitenäytöt tarjoavat reaaliaikaista palautetta ASIC:n viritysparametreista, ja mitattu jännite edustaa tarkinta saatavilla olevaa lukemaa, joka on otettu suoraan ASIC-piirin sijainnista. Tämä tarkkuus mahdollistaa suorituskykyparametrien hienosäädön säilyttäen samalla turvalliset käyttöolosuhteet.


Yhteyden tila -osio tarjoaa välittömän näkyvyyden mining-poolin konfiguraatioon ja näyttää nykyisen stratumin URL-osoitteen, portin ja käyttäjätunnuksen. AxeOS luo julkisiin pooleihin liitetyille laitteille käteviä pikalinkkejä, jotka vievät sinut suoraan poolien verkkokäyttöliittymään, jossa voit tarkastella yksityiskohtaisia tilastoja, laiteluetteloita ja historiallisia suorituskykytietoja. Tämä integraatio tehostaa valvontaprosessia yhdistämällä laite- ja allastason tiedot saumattomaksi työnkuluksi.


### Parvenhallinta ja usean laitteen hallinta


Swarm-toiminnallisuus on AxeOS:n ratkaisu useiden Bitaxe-laitteiden hallinnan monimutkaisuuteen verkossa, sillä sen avulla ei tarvitse muistaa lukuisia IP-osoitteita ja siirtyä niihin. Tämän keskitetyn hallintajärjestelmän avulla voit lisätä laitteita yksinkertaisesti syöttämällä niiden IP-osoitteet, havaita automaattisesti aktiiviset Bitaxe-kaivurit ja sisällyttää ne yhtenäiseen hallintapaneeliin. Kun Swarm on konfiguroitu, se tarjoaa kattavan hallinnan koko mining-toiminnalle yhdestä käyttöliittymästä.


Swarm-käyttöliittymän kautta voit suorittaa kriittisiä hallintatehtäviä useille laitteille samanaikaisesti tai erikseen, mukaan lukien poolin kokoonpanon muutokset, laitteiden uudelleenkäynnistykset, taajuuden säädöt ja suorituskyvyn seuranta. Tämä keskitetty lähestymistapa vähentää merkittävästi suurten mining-operaatioiden hallinnointiin liittyviä hallinnollisia kuluja ja varmistaa samalla johdonmukaisen kokoonpanon kaikissa laitteissa. Järjestelmä säilyttää yksittäisten laitteiden identiteetin ja tarjoaa samalla yhteisiä hallintaominaisuuksia, mikä on optimaalinen tasapaino yksityiskohtaisen hallinnan ja toiminnan tehokkuuden välillä.


Swarm-kojelauta esittää kunkin hallinnoidun laitteen senhetkisen tilan, suorituskykymittarit ja pikakäyttöiset ohjaimet, mikä mahdollistaa nopean reagoinnin suorituskykyongelmiin tai määritysmuutoksiin. Tämä toiminto on erityisen arvokas kaivostyöntekijöille, jotka käyttävät useita laitteita eri paikoissa tai jotka säätävät mining-parametreja usein markkinaolosuhteiden tai poolin suorituskyvyn perusteella.


### Konfiguraation hallinta ja järjestelmäasetukset


AxeOS:n Asetukset-osiossa voit hallita kattavasti kaikkia Bitaxe-laitteesi konfiguroitavissa olevia seikkoja verkkoyhteyksistä mining-parametreihin ja laitteiston optimointiin. Verkkokonfigurointi alkaa Wi-Fi-asetuksista, joissa määrität verkon nimen ja salasanan, ja AxeOS suosittelee yksisanaista verkkonimeä ilman välilyöntejä luotettavan yhteyden varmistamiseksi. Järjestelmä hoitaa koko langattoman konfigurointiprosessin ja mahdollistaa etähallinta- ja valvontaominaisuudet.


Mining-konfigurointi keskittyy stratum-asetuksiin, joissa määrität valitsemasi mining-poolin URL-osoitteen ilman protokollan etuliitteitä tai porttinumeroita, jotka käsitellään erillisissä kentissä. Stratum-käyttäjä-kenttä vastaa erilaisiin poolivaatimuksiin, sillä se tukee sekä Bitcoin-osoitteita mining-sooloa varten että mining-poolin käyttäjätunnusjärjestelmiä, ja siihen voidaan liittää laitetunnuksia usean laitteen toimintoja varten. Hiljattain lisätty stratum-salasanatoiminto tukee tunnistautumista vaativia pooleja, vaikka useimmat julkiset poolit toimivat ilman tätä vaatimusta.


Laitteiston optimointi taajuuden ja ydinjännitteen säätämisen avulla on AxeOS:n tehokkain suorituskyvyn viritysominaisuus. Laiteversiosta ja selaimesta riippuen nämä asetukset voivat näkyä pudotusvalikkoina, joissa on esiasetettuja asetuksia, tai avoimina kenttinä, jotka mahdollistavat mukautetut arvot. Oletusasetukset 485 MHz:n taajuus ja 1200 mV:n ydinjännite takaavat vakaan toiminnan ensimmäisiä testejä varten, kun taas edistyneet käyttäjät voivat optimoida nämä parametrit maksimisuorituskyvyn tai -tehokkuuden saavuttamiseksi omien erityisvaatimustensa ja käyttöolosuhteidensa perusteella.


### Järjestelmän ylläpito ja lisäominaisuudet


AxeOS sisältää kehittyneitä järjestelmän ylläpito-ominaisuuksia, jotka on suunniteltu pitämään Bitaxe-laitteesi huipputehokkaana ja tarjoamaan samalla vianmääritystietoja vianmääritystä ja optimointia varten. Päivitysjärjestelmä tehostaa laiteohjelmistojen hallintaa näyttämällä uusimman saatavilla olevan version suoraan käyttöliittymässä ja tarjoamalla suorat latauslinkit virallisiin laiteohjelmistotiedostoihin. Tämä integrointi poistaa tarpeen navigoida manuaalisesti GitHub-tietovarastoissa tai hallita tiedostojen latauksia, mikä yksinkertaistaa päivitysprosessin muutamaan napsautukseen.


Päivitysliittymä hyväksyy oikein nimetyt laiteohjelmistotiedostot, erityisesti esp-miner.bin ja www.bin, mikä varmistaa yhteensopivuuden ja estää asennusvirheet. Käyttäjille, joilla on vaikeuksia vakiopäivitysprosessin kanssa, AxeOS tarjoaa viitteitä kattaviin tehdasflash-menettelyihin, joilla voidaan palauttaa laitteiden alkuperäinen toimintakyky. Tämä kaksitahoinen lähestymistapa sopii sekä rutiinipäivityksiin että palautusskenaarioihin.


Kirjausjärjestelmä antaa reaaliaikaisen kuvan laitteen toiminnasta ja näyttää yksityiskohtaiset tiedot ASIC-sirumalleista, järjestelmän käyttöajasta, Wi-Fi-yhteyden tilasta, käytettävissä olevasta muistista, laiteohjelmistoversioista ja piirilevyn versioista. Nämä lokit ovat korvaamattomia kehittäjille ja edistyneille käyttäjille, jotka haluavat ymmärtää laitteen käyttäytymistä, diagnosoida ongelmia tai optimoida suorituskykyä. Reaaliaikainen lokin katseluohjelma esittää reaaliaikaisia toimintatietoja, kuten [nonce](https://planb.academy/resources/glossary/nonce)-käsittelyn, vaikeuslaskennan ja mining:n lähetysparametrit, ja tarjoaa näin ennennäkemättömän näkymän itse mining-prosessiin.


Järjestelmän lisäominaisuuksiin kuuluu näytön suuntauksen säätö mukautetuissa koteloissa käytettäviä laitteita varten, tuulettimen napaisuuden kääntäminen erikoisjäähdytyskokoonpanoja varten ja automaattinen tuulettimen ohjaus, joka säätää jäähdytystä ASIC:n lämpötilan perusteella. Manuaalinen tuulettimen nopeuden säätö mahdollistaa tarkan jäähdytyksen hallinnan silloin, kun automaattiset järjestelmät eivät täytä erityisvaatimuksia. Kaikki konfiguraatiomuutokset edellyttävät tallentamista ja laitteen uudelleenkäynnistystä tullakseen voimaan, mikä takaa vakaan toiminnan ja estää mining:n suorituskykyyn mahdollisesti vaikuttavien osittaisten konfiguraatiotilojen syntymisen.



# Yhteisö ja yhteistyö

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Avoimen lähdekoodin panos Yleiskatsaus

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub ja sen rooli ohjelmistokehityksessä


GitHub edustaa perustavanlaatuista muutosta siinä, miten ohjelmistokehitysprojekteja hallitaan ja jaetaan maailmanlaajuisessa ohjelmointiyhteisössä. GitHub on pilvipohjainen alusta, joka isännöi ohjelmistokehitysprojekteja hajautetun versionhallintajärjestelmän Gitin avulla, ja sen avulla kehittäjät voivat tehdä saumatonta yhteistyötä projekteissa fyysisestä sijainnistaan riippumatta. Alusta toimii sekä teknisenä työkaluna että ohjelmoijien sosiaalisena verkostona, jonka avulla he voivat seurata muutoksia, yhdistää päivityksiä, ylläpitää koodinsa eri versioita ja osallistua Open Source Miners Unitedin BitX-projektin kaltaisiin avoimen lähdekoodin aloitteisiin.


GitHubin vahvuus on sen kyky yksinkertaistaa monimutkaista yhteistoiminnallista kehitysprosessia. Kun useat kehittäjät työskentelevät saman projektin parissa, GitHub tarjoaa infrastruktuurin, jonka avulla voidaan hallita panoksia, tarkastella muutoksia, käsitellä projektin ongelmia ja ylläpitää kattavaa dokumentaatiota. Tämä yhteistyöhön perustuva lähestymistapa on tehnyt GitHubista olennaisen osan nykyaikaisia ohjelmistokehityksen työnkulkuja, mikä on muuttanut sekä yksittäisten kehittäjien että suurten organisaatioiden lähestymistapaa projektinhallintaan ja koodin jakamiseen.


### Navigointi GitHub Interface:ssa ja arkiston rakenteessa


GitHubin käyttöliittymän ymmärtäminen alkaa tunnistamalla keskeiset elementit, joista mikä tahansa arkistosivu koostuu. Ylänavigaatiopalkki sisältää useita kriittisiä osioita, kuten Koodi, Ongelmat, Pull Requests, Keskustelut, Toiminnot, Projektit, Turvallisuus ja Insights. Kullakin osiolla on tietty tarkoitus projektinhallinnan ekosysteemissä, ja Code-osiossa näkyvät varsinaiset tiedostot ja kansiot, joista projekti koostuu.


Arkiston rakenne itsessään kuvastaa projektin ylläpitäjien organisatorista lähestymistapaa. Jotkut arkistot sisältävät vain yhden tiedoston, ehkä yksinkertaisen komentosarjakomentosarjan, kun taas toiset, kuten BitX-laitteistoprojekti, sisältävät lukuisia tiedostoja, jotka on järjestetty hakemistoihin ja alihakemistoihin. Arkiston nimi on näkyvästi esillä, ja se toimii sekä tunnisteena että lyhyenä kuvauksena projektin tarkoituksesta. Olennaisia vuorovaikutteisia elementtejä ovat Watch-painike, jolla voi vastaanottaa ilmoituksia arkiston päivityksistä, Fork-painike, jolla voi luoda henkilökohtaisia kopioita arkistosta, ja Star-painike, joka toimii yhteisön hyväksymisjärjestelmänä, joka muistuttaa "peukut ylös" -toimintoa.


Tietoja-osiossa on keskeiset projektitiedot tiivistetyssä muodossa, mukaan lukien yksirivinen kuvaus, lisensointitiedot ja keskeiset projektitiedot. BitX-projektin osalta tämä osio määrittää sen "avoimen lähdekoodin ASIC Bitcoin-kaivoslaitteistoksi" ja määrittää GPL 3.0 -lisenssin. Lisensoinnin ymmärtäminen on erityisen tärkeää, koska GitHub toimii avoimen lähdekoodin alustana, jossa julkiset arkistot ovat koko yhteisön käytettävissä, mutta sisältöä voi käyttää ja jakaa vain kunkin lisenssin noudattamissääntöjen mukaisesti.


### Työskentely haarojen ja projektiversioiden kanssa


Haarojen käsite on yksi GitHubin tehokkaimmista ominaisuuksista eri versioiden ja kehityspolkujen hallinnassa yhden projektin sisällä. Haaralla luodaan kopio tai muokattu versio pääkoodipohjasta, jolloin kehittäjät voivat työskennellä tiettyjen ominaisuuksien, virheiden korjausten tai kokeellisten muutosten parissa vaikuttamatta pääkehityslinjaan. Päähaara toimii yleensä projektin vakaana ja vakaana versiona, kun taas lisähaaroja käytetään eri iteraatioita, testausvaiheita tai täysin erilaisia tuotevaihtoehtoja varten.


BitX-laitteistoprojektissa on useita haaroja eri laitteistoversioiden ja -kokoonpanojen hallintaa varten. Esimerkiksi Ultra v2 -haara sisältää kyseiselle laitteistoversiolle ominaisia tiedostoja, kun taas Super 401 -haara keskittyy toteutuksiin, joissa käytetään S21 ASIC -piiriä tehokkuuden parantamiseksi. Kukin haara voi olla useita komentoja edellä tai jäljessä päähaarasta, mikä kertoo muutosten ja kehitystoiminnan laajuudesta. Eri haaroja tutkiessaan käyttäjät huomaavat täysin erilaiset tiedostorakenteet, dokumentaation ja jopa visuaaliset esitykset, jotka heijastavat kunkin laitteistovaihtoehdon ainutlaatuisia vaatimuksia ja eritelmiä.


Haarajärjestelmä estää sekaannuksia tekijöiden ja käyttäjien välillä erottamalla selkeästi eri kehityslinjat toisistaan. Sen sijaan, että sekoitettaisiin kokeellisia ominaisuuksia ja vakaita julkaisuja tai yhdistettäisiin eri laitteistoversioita yhteen paikkaan, haarat mahdollistavat selkeän erottelun, mutta samalla säilytetään mahdollisuus yhdistää onnistuneet muutokset takaisin pääkehityslinjaan tarvittaessa. Tämä organisatorinen lähestymistapa varmistaa, että käyttäjät löytävät helposti tarvitsemansa version, kun taas kehittäjät voivat työskennellä parannusten parissa häiritsemättä pääprojektia.


### Myötävaikuttaminen kysymysten kautta


Ongelmat-osio toimii ensisijaisena viestintäkanavana käyttäjien ja projektin ylläpitäjien välillä ongelmien raportoinnissa, parannusehdotuksissa ja vikojen dokumentoinnissa. On kuitenkin tärkeää ymmärtää, että Issues-osio on tarkoitettu nimenomaan laillisiin teknisiin ongelmiin eikä niinkään yleisiin kysymyksiin tai tukipyyntöihin. Kun käyttäjät kohtaavat todellisia toimintahäiriöitä, odottamatonta käyttäytymistä tai tunnistavat mahdollisia parannuksia, hyvin dokumentoidun ongelman luominen auttaa koko yhteisöä kiinnittämällä huomiota ongelmiin, jotka voivat vaikuttaa useisiin käyttäjiin.


Tehokas ongelmaraportointi edellyttää ongelman yksityiskohtaista dokumentointia, mukaan lukien olosuhteet, jotka johtivat ongelmaan, toimenpiteet ongelman toistamiseksi ja kaikki asiaankuuluvat tekniset yksityiskohdat. BitX-hanke osoittaa tämän periaatteen useiden suljettujen ongelmien avulla, jotka osoittavat ratkaisuprosessin ongelman tunnistamisesta yhteisön keskustelun kautta lopulliseen ratkaisuun. Jotkin ongelmat johtavat laitteiston parantamiseen, kuten kiinnitysreikien lisäämiseen jäähdytysmahdollisuuksien parantamiseksi, kun taas toiset ongelmat voidaan ratkaista käyttäjäkoulutuksen tai ohjelmistopäivitysten avulla.


Ongelmien ja keskustelujen erottaminen toisistaan on tärkeää, jotta yhteisön vuorovaikutus pysyy järjestäytyneenä. Issues-osiossa keskitytään tiettyihin teknisiin ongelmiin, kun taas Discussions-osio tarjoaa foorumin kaltaisen ympäristön kysymyksille, ideoille ja yhteisön yleiselle osallistumiselle. Vaikka Discord-palvelimesta on tullut BitX-yhteisön ensisijainen viestintäkanava, GitHubin Discussions-osio on edelleen käytettävissä muodollisempia tai hakukelpoisia keskusteluja varten, jotka hyötyvät pysyvästä dokumentaatiosta ja helposta viittauksesta.


### Pull-pyyntöjen ymmärtäminen


Pull requestit ovat mekanismi, jonka avulla ulkopuoliset tekijät ehdottavat muutoksia projektin arkistoon. Kun joku havaitsee parannuksen, virheenkorjauksen tai uuden ominaisuuden, joka hyödyttäisi projektia, hän voi luoda vetopyynnön ja lähettää muutokset tarkistettavaksi ja mahdollisesti sisällytettäväksi pääkoodipohjaan. Tällä prosessilla varmistetaan, että kaikki muutokset käydään läpi ennen kuin niistä tulee osa virallista projektia, mikä ylläpitää koodin laatua ja projektin johdonmukaisuutta ja mahdollistaa samalla yhteisön osallistumisen.


Pull request -työnkulku alkaa tyypillisesti, kun tekijä haarauttaa arkiston, luo oman kopionsa, jossa hän voi tehdä muutoksia, ja lähettää muutokset takaisin alkuperäiseen projektiin pull request -pyynnön kautta. Projektin ylläpitäjät voivat sitten tarkastella ehdotettuja muutoksia, keskustella muutoksista avustajan kanssa ja lopulta päättää, yhdistetäänkö muutokset pääprojektiin. Tämä yhteistoiminnallinen tarkistusprosessi auttaa ylläpitämään projektin standardeja ja kannustaa samalla yhteisöä osallistumaan ja parantamaan toimintaa.


Tunnisteiden ja julkaisujen ymmärtäminen lisää projektinhallintaan ja versionhallintaan uuden tason. Tunnisteet toimivat merkkeinä kehitysaikataulussa, ja ne yksilöivät tiettyjä pisteitä, jotka edustavat tiettyjä versioita tai virstanpylväitä. BitX:n kaltaisissa laitteistoprojekteissa tunnisteet vastaavat usein tiettyjä mallinumeroita tai laitteistoversioita, mikä antaa käyttäjille, jotka etsivät tiettyjä versioita, selkeät vertailukohteet. Ohjelmistoprojekteissa yleisemmin käytetyt julkaisut edustavat valmiiden ominaisuuksien ja virheiden korjausten virallisia jakeluja, joihin liittyy usein yksityiskohtaisia julkaisutiedotteita ja ladattavia paketteja.


GitHub-ekosysteemi luo kattavan ympäristön avoimen lähdekoodin yhteistyölle, joka ulottuu paljon pelkkää tiedostojen jakamista pidemmälle. Ymmärtämällä nämä eri komponentit ja niiden asianmukaisen käytön osallistujat voivat osallistua tehokkaasti projekteihin, auttaa parantamaan ohjelmisto- ja laitteistosuunnitelmia ja hyötyä maailmanlaajuisen kehitysyhteisön kollektiivisesta tiedosta ja ponnisteluista. Olipa kyse ongelmien raportoinnista, parannusehdotuksista tai koodin tuottamisesta, GitHub tarjoaa työkalut ja rakenteen, joita tarvitaan mielekkääseen yhteistyöhön avoimen lähdekoodin maailmassa.


## Avoimen lähdekoodin osallistuminen käytännönläheisesti

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Tässä luvussa keskitytään ongelmien luomisen ja avoimen lähdekoodin projektien tutkimisen pohjalta suoran osallistumisen käytännön näkökohtiin vetopyyntöjen ja arkistojen hallinnan avulla. fork-tietovarastojen ymmärtäminen, muutosten tekeminen ja vetopyyntöjen lähettäminen on ratkaisevan tärkeä taito kaikille kehittäjille, jotka haluavat osallistua mielekkäästi avoimen lähdekoodin projekteihin, olipa kyse sitten ohjelmistokehityksestä tai laitteistosuunnittelusta.


Koodimuutosten tekeminen noudattaa standardoitua työnkulkua, joka varmistaa projektin eheyden ja mahdollistaa samalla yhteistoiminnallisen kehityksen. Työnkulkuun kuuluu oman kopion luominen projektin arkistosta, muutosten tekeminen valvotussa ympäristössä ja muutosten ehdottaminen takaisin alkuperäiseen projektiin virallisen tarkistusprosessin kautta. Vaikka tämän luvun esimerkeissä keskitytäänkin ensisijaisesti ohjelmisto-osuuteen, samat periaatteet ja menettelyt soveltuvat yhtä lailla myös laitteistoprojekteihin, joihin sisältyy piirilevysuunnitelmia, kaaviokuvia ja muuta teknistä dokumentaatiota.


### Haarukoiden ja arkiston rakenteen ymmärtäminen


Avoimen lähdekoodin projektiin osallistumisen perusta on fork:n luominen, joka on henkilökohtainen kopio alkuperäisestä arkistosta. Kun siirryt GitHub-arkistoon ja napsautat "fork"-painiketta, luot oman GitHub-tilisi alle riippumattoman kopion, joka säilyttää selkeän yhteyden alkuperäiseen lähteeseen. Tämä haarautunut arkisto näkyy tililläsi selkeällä merkinnällä sen alkuperästä, ja arkiston otsikon alla näkyy teksti, kuten "forked from [original-owner]/[repository-name]".


Haarukoitu arkistosi toimii alkuperäisestä riippumatta, joten voit tehdä muutoksia vaikuttamatta pääprojektiin. Se on kuitenkin tietoinen alkuperäisen arkiston päivityksistä GitHubin synkronointiominaisuuksien avulla. Kun alkuperäinen arkisto saa päivityksiä, joita fork:stäsi puuttuu, GitHub näyttää tilatietoja, kuten "Tämä haara on X komitusta jäljessä" tai "X komitusta edellä", mikä antaa selkeän näkyvyyden fork:n ja edeltävän arkiston välisestä suhteesta. Voit synkronoida fork:n alkuperäisen arkiston kanssa milloin tahansa napsauttamalla "Synkronoi fork" -painiketta, joka vetää uusimmat muutokset lähdekoodista.


fork:n ja alkuperäisen arkiston välinen suhde on erityisen tärkeä, kun alat tehdä muutoksia. Kun toteutat muutoksia ja toimitat niitä fork:een, GitHub seuraa näitä eroja ja näyttää ne toimituksina alkuperäisen arkiston edellä. Tämä seurantajärjestelmä mahdollistaa pull request -prosessin, jossa voit ehdottaa muutoksiasi sisällytettäväksi pääprojektiin ja samalla säilyttää selkeän historian siitä, mitä on muutettu.


### Kehitysympäristön määrittäminen


Tehokkaan kehitysympäristön luominen edellyttää huolellista huomiota sekä yleisiin kehitystyökaluihin että projektikohtaisiin vaatimuksiin. Visual Studio Code toimii erinomaisena integroituna kehitysympäristönä (IDE) useimmille avoimen lähdekoodin projekteille, sillä se tarjoaa keskeiset ominaisuudet koodin muokkaukseen, versionhallinnan integrointiin ja projektinhallintaan. Ensimmäinen kriittinen osa on Git-laajennuksen asentaminen ja konfigurointi, joka mahdollistaa saumattoman integroinnin GitHub-tietovarastoihin suoraan kehitysympäristöstäsi.


Nykyaikaisissa Visual Studio Code -versioissa on yleensä Git-tuki oletuksena, mutta sinun on tunnistauduttava GitHub-tililläsi, jotta voit käyttää kaikkia toimintoja. Tämä todennusprosessi edellyttää kirjautumista GitHubiin IDE:n kautta, minkä jälkeen voit kloonata arkistoja, tehdä muutoksia ja työntää päivityksiä suoraan kehitysympäristöstäsi. GitHub-integraatio näkyy kuvakkeena vasemmassa sivupalkissa, ja se tarjoaa pääsyn arkistojen kloonaus-, haarojen hallinta- ja synkronointiominaisuuksiin ilman komentorivitoimintoja.


Sulautettuja järjestelmiä tai erityisiä laitteistoalustoja koskevissa hankkeissa tarvitaan lisätyökaluja. ESP-IDF-laajennus on ratkaisevan tärkeä osa ESP32-mikrokontrollereihin kohdistuvissa hankkeissa, jotka vaativat tietyn version yhteensopivuutta asianmukaisen toiminnan varmistamiseksi. Asennusprosessi sisältää sopivan ESP-IDF-version valinnan, työkalupolkujen määrittämisen ja kehityskonttiympäristön määrittämisen. Versio 5.1.3 on tällä hetkellä suositeltu kokoonpano monille ESP32-pohjaisille projekteille, mutta nämä vaatimukset voivat muuttua, kun projektit päivittävät riippuvuuksiaan ja työkaluketjujaan.


### Muutosten tekeminen ja komitusten hallinta


Kun kehitysympäristösi on oikein konfiguroitu, mielekkään panoksen tekeminen alkaa lataamalla tai kloonaamalla haarautunut arkisto paikalliselle koneellesi. Voit tehdä tämän joko lataamalla arkiston sisällön sisältävän ZIP-tiedoston tai käyttämällä Visual Studio Codeen integroitua kloonaustoimintoa, joka tarjoaa virtaviivaisemman työnkulun jatkuvaan kehitykseen. Kloonausprosessi luo arkistostasi paikallisen kopion, joka pysyy synkronoituna GitHub fork:n kanssa, jolloin voit työskennellä offline-tilassa säilyttäen samalla versionhallintaominaisuudet.


Kun työskentelet paikallisen arkiston kanssa, saat käyttöösi koko projektirakenteen, mukaan lukien lähdekooditiedostot, määritystiedostot, dokumentaation ja kaikki laitteiston suunnittelutiedostot. Useimmissa laiteohjelmistoprojekteissa käytetään ohjelmointikieliä, kuten C:tä, perustoiminnoissa ja TypeScript-kielellä kirjoitettuja lisäkomponentteja käyttöliittymiä varten tai Java-kielellä kirjoitettuja erityisiä apuohjelmia varten. Projektin rakenteen ymmärtäminen auttaa sinua tunnistamaan sopivia tiedostoja, joita voit muokata, ja varmistaa, että muutokset ovat linjassa projektin arkkitehtuurimallien ja koodausstandardien kanssa.


Sitouttamisprosessi on versionhallinnan perustavanlaatuinen osa-alue, joka vaatii huolellista huomiota sekä tekniseen tarkkuuteen että viestinnän selkeyteen. Ennen kuin teet muutoksia, sinun tulisi ymmärtää olemassa oleva koodi perusteellisesti ja testata muutokset paikallisessa ympäristössäsi. Avoimen lähdekoodin osallistumisen perussääntö korostaa, että koskaan ei saa julkaista testaamatonta koodia, sillä se voi tuoda mukanaan virheitä tai tietoturva-aukkoja, jotka vaikuttavat koko projektiyhteisöön. Lisäksi et saa koskaan luovuttaa arkaluonteisia tietoja, kuten salasanoja, API-tunnisteita tai henkilökohtaisia tunnistetietoja, julkisiin arkistoihin, sillä nämä tiedot tulevat pysyvästi kaikkien niiden saataville, joilla on pääsy arkistoon.


### Pull-pyyntöjen luominen ja hallinta


Osallistumisesi huipentuma on pull request -pyynnön luominen, joka on virallinen ehdotus muutosten yhdistämisestä alkuperäiseen projektivarastoon. Tämä prosessi alkaa GitHub fork:ssa, jossa voit tarkastella arkistosi ja lähdekoodin välisiä eroja. GitHubin käyttöliittymässä näkyy selvästi, kuinka monta komitusta on edellä tai jäljessä, mikä antaa välittömän kuvan ehdotettujen muutosten laajuudesta. Ennen pull requestin luomista kannattaa varmistaa, että fork on synkronoitu viimeisimpien upstream-muutosten kanssa mahdollisten ristiriitojen minimoimiseksi.


Tehokkaan pull requestin luominen vaatii muutakin kuin pelkän koodimuutosten lähettämisen. Pull request -pyynnön kuvaus on tilaisuutesi kertoa projektin ylläpitäjille ja yhteisölle muutosten tarkoituksesta, laajuudesta ja vaikutuksesta. Hyvin kirjoitetussa kuvauksessa kerrotaan, mihin ongelmiin muutoksesi kohdistuvat, miten toteutit ratkaisun ja mitkä ovat mahdolliset vaikutukset projektin muihin osiin. Tämä dokumentointi on erityisen tärkeää monimutkaisissa muutoksissa, jotka eivät ehkä käy heti ilmi pelkästään koodin eroja tarkastelemalla.


Tarkastusprosessi edustaa avoimen lähdekoodin kehitystyön yhteistoiminnallista puolta, jossa projektin ylläpitäjät ja kokeneet avustajat arvioivat ehdotettuja muutoksia. Voit pyytää tiettyjä arvioijia, joilla on asiantuntemusta muutosten kohteena olevilta aloilta, ja varmistaa näin, että asiantuntevat yhteisön jäsenet tarkastavat työsi. Tarkastusprosessiin voi sisältyä useita iteraatioita, joissa tarkastajat antavat palautetta, pyytävät muutoksia tai pyytävät lisätestausta. Tämä yhteistoiminnallinen tarkistusprosessi auttaa ylläpitämään koodin laatua ja tarjoaa samalla arvokkaita oppimismahdollisuuksia kaiken kokemuksen omaaville osallistujille.


Ymmärrys siitä, että kaikkia pull-pyyntöjä ei hyväksytä, auttaa asettamaan asianmukaiset odotukset osallistumisprosessille. Projektin ylläpitäjät voivat hylätä vetoomukset eri syistä, kuten siitä, että ne eivät vastaa projektin tavoitteita, testauksen riittämättömyys tai jo kehitteillä olevien vaihtoehtoisten ratkaisujen olemassaolo. Hylkäämistä ei pidä pitää epäonnistumisena, vaan se olisi nähtävä mahdollisuutena oppia palautteesta, tarkentaa lähestymistapaa ja mahdollisesti tarjota vaihtoehtoisia ratkaisuja, jotka vastaavat paremmin projektin tarpeita. Avoimen lähdekoodin yhteisö kukoistaa tästä iteratiivisesta ehdotusten, tarkistusten ja parannusten prosessista, joka viime kädessä vie hankkeita eteenpäin yhteisten ponnistelujen ja jaetun asiantuntemuksen avulla.



## Mikä on Public-Pool?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool edustaa vallankumouksellista lähestymistapaa Bitcoin mining:een, joka ratkaisee monet niistä huolenaiheista, joita kaivostyöläisillä on perinteisten mining-poolien kanssa. Täysin avoimen lähdekoodin Bitcoin mining-soolopoolina Public Pool muuttaa perustavanlaatuisesti palkkioiden jakomallia, johon louhijat ovat tottuneet. Toisin kuin perinteiset mining-altaat, joissa osallistujat jakavat palkkiot, kun kuka tahansa poolin louhijoista löytää lohkon, Public Pool toimii soolo- mining-periaatteella, jossa yksittäiset louhijat saavat 100 prosenttia lohkonsa palkkiosta, kun he louhivat onnistuneesti lohkon.


Public Poolin houkuttelevin ominaisuus on sen maksuttomuus. Kun louhijat löytävät onnistuneesti lohkon Public Poolin avulla, he saavat koko lohkon palkkion sekä kaikki siihen liittyvät [transaktiomaksut](https://planb.academy/resources/glossary/transaction-fees) ilman, että poolin käyttökustannuksia vähennetään. Tämä on jyrkässä ristiriidassa perinteisten mining-poolien kanssa, jotka tyypillisesti veloittavat 1-3 prosenttia mining-palkkioista. Nollamaksumalli tekee Public Poolista erityisen houkuttelevan kaivostoimijoille, jotka haluavat maksimoida potentiaalisen tuottonsa ja samalla säilyttää täyden hallinnan mining-toiminnoissaan.


Public Poolin ainutlaatuisen aseman ymmärtämiseksi on tärkeää ymmärtää, mikä on perustavanlaatuinen ero yksin hankitun mining:n ja yhdistetyn mining:n välillä. Todellinen solo mining tarkoittaa, että louhit itsenäisesti ja saat täyden lohkopalkkion (tällä hetkellä 3,125 BTC + maksut), jos löydät lohkon, mutta todennäköisyys on verrannollinen hash-asteeseesi verrattuna koko verkostoon, mikä aiheuttaa äärimmäistä vaihtelua, joka voi kestää kuukausia tai vuosia palkintojen välillä. Perinteiset poolit yhdistävät hash-tehoja löytääkseen lohkoja useammin, jolloin palkkiot jakautuvat suhteellisesti ja tulot ovat tasaisia ja ennustettavia. Kaivostoiminnan harjoittajille, joilla on huomattavia investointeja laitteistoon ja käyttökustannuksiin, pelkkä mining-soolo on yleensä epäkäytännöllinen sen filosofisista eduista huolimatta - vaihtelu tekee sähkökustannusten kattamisen ja investointien takaisin saamisen lähes mahdottomaksi. Tämä taloudellinen realiteetti tarkoittaa, että useimmat kaivostyöläiset valitsevat yhdistetyn mining:n käytännön taloudellisista syistä. Public Pool toimii yksin louhivan mining:n poolina, mikä tarkoittaa, että sinulla on edelleen yksin louhittavan mining:n varianssi (saat palkkion vain, kun löydät lohkon henkilökohtaisesti), mutta hyödyt poolin infrastruktuurista ja läpinäkyvästä, maksuttomasta toiminnasta.


### Avoimen lähdekoodin etu ja tekninen toteutus


Public Poolin sitoutuminen avoimen lähdekoodin kehitykseen tarjoaa louhijoille ennennäkemätöntä avoimuutta ja mining-toimintojen hallintaa. Koko koodipohja on saatavilla GitHubissa, joten louhijat voivat tutkia tarkkaan, miten ohjelmisto toimii, muokata sitä omien tarpeidensa mukaan ja jopa osallistua sen kehittämiseen. Tämä avoimuus vastaa mining-yhteisön merkittävään huoleen, joka liittyy perinteisten mining-poolien tuntemattomiin kokoonpanoihin ja käytäntöihin.


Ohjelmistoarkkitehtuuri sisältää sekä mining-altaan ydintoiminnot että erillisen käyttöliittymävaraston, jotka molemmat ovat vapaasti ladattavissa ja muokattavissa. Louhijat voivat käyttää Public Poolia erilaisissa kokoonpanoissa, kuten Docker-kontteina, joten se on mukautettavissa erilaisiin laitteistoasetuksiin ja teknisiin mieltymyksiin. GitHub-tietovarastoissa oleva kattava dokumentaatio tarjoaa yksityiskohtaisia asennusoppaita, konfigurointivaihtoehtoja ja muokkausohjeita, minkä ansiosta se on käytettävissä eriasteista teknistä asiantuntemusta omaaville louhijoille.


Yhteyden muodostaminen Public Pooliin vaatii vain vähän konfigurointia verrattuna perinteisiin mining-asetuksiin. Louhijoiden tarvitsee vain määrittää mining-laitteisiinsa [Stratum](https://planb.academy/resources/glossary/stratum)-yhteyden tiedot ja antaa Bitcoin-osoitteensa käyttäjätunnukseksi. Valinnainen työntekijän nimi voidaan lisätä pisteen erottimen jälkeen organisointitarkoituksiin.


### Yhteisön ominaisuudet ja kestävyysmalli


Public Pool sisältää useita innovatiivisia ominaisuuksia, jotka vahvistavat Bitcoin mining-yhteisöä ja säilyttävät samalla sen maksuttoman toiminnan. Alusta näyttää kattavat tilastot, mukaan lukien liitettyjen louhijoiden kokonaishashtinopeus, joka oli tyypillisesti 1-2 PetaHashia sekunnissa vuonna 2024 ja noin 40 PH/s marraskuussa 2025, ja tarjoaa yksityiskohtaisia tietoja liitetyistä mining-laitteista. Erityisen huomionarvoista on alustan painotus avoimen lähdekoodin mining-laitteistoon, sillä tähdillä merkityt laitteet osoittavat täysin avoimen lähdekoodin malleja, ja niissä on linkit niiden GitHub-tietovarastoihin.


Public Poolin maksuttoman toiminnan kestävyys perustuu luovaan kumppanuusohjelmakumppanuuteen mining-laitetoimittajien kanssa. Kun kaivosmiehet ostavat laitteita kumppaniyrityksiltä käyttämällä alennuskoodia "SOLO", 50 prosenttia kumppanuustuloista tukee Public Poolin toimintakuluja, kun taas loput 50 prosenttia jaetaan palkintoina kaivosmiehille, jotka saavuttavat kuukausittain korkeimmat vaikeusasteet. Tämä malli luo symbioottisen suhteen, jossa kaivostyöntekijät saavat alennuksia laitehankinnoista, myyjät saavat asiakkaita ja Public Pool ylläpitää toimintaansa perimättä suoria maksuja.


### Hajauttamisen filosofia ja parhaat käytännöt


Vaikka Public Pool tarjoaa erinomaisen vaihtoehdon perinteisille mining-altaille, on tärkeää ymmärtää sen rooli Bitcoin-hallinnon hajauttamisen laajemmassa kontekstissa. Alusta toimii ponnahduslautana kohti perimmäistä tavoitetta, jonka mukaan yksittäiset louhijat ylläpitävät omia mining-poolejaan. Oman mining-altaan pyörittäminen edustaa hajauttamisen korkeinta tasoa, sillä se poistaa riippuvuuden kolmannen osapuolen infrastruktuurista tai ohjelmistosta riippumatta siitä, kuinka läpinäkyvä tai hyvää tarkoittava kolmas osapuoli onkaan.


Public Poolin avoimen lähdekoodin luonne tekee siitä ihanteellisen oppimisalustan louhijoille, jotka haluavat ymmärtää poolin toimintaa ennen omien ratkaisujensa toteuttamista. Asennusoppaiden saatavuus useille käyttöjärjestelmille ja kattava dokumentaatio antavat kaivostyöntekijöille tarvittavat tiedot, jotta he voivat siirtyä Public Poolin käytöstä oman mining-infrastruktuurinsa käyttämiseen. Tämä koulutuksellinen näkökulma vastaa Bitcoin:n perusperiaatteita, jotka koskevat itsehallintoa ja hajauttamista, ja antaa yksittäisille louhijoille mahdollisuuden hallita mining-toimintojaan täysin ja edistää samalla Bitcoin-verkon yleistä turvallisuutta ja hajauttamista.


Alustan käyttöliittymä tarjoaa louhijoille yksityiskohtaiset seurantaominaisuudet, kuten työntekijöiden tilan, hash rate -tilastot ja suorituskykymittarit. Näiden ominaisuuksien avulla louhijat voivat optimoida toimintojaan ja samalla oppia poolinhallintaperiaatteista, joita he voivat myöhemmin soveltaa omiin mining pool-toteutuksiinsa.


## Miten Public-Pool asennetaan Umbreliin?

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Bitcoin mining-altaan käyttäminen kotona on nykyaikaisen laitteiston ja yksinkertaistettujen ohjelmistoratkaisujen ansiosta yhä helpompaa. Tässä luvussa tarkastellaan kotipohjaisen julkisen uima-altaan käytännön toteutusta käyttämällä kohtuuhintaista mini-PC-laitteistoa ja virtaviivaistettua solmunhallintaohjelmistoa. Tämän oppaan loppuun mennessä ymmärrät laitteistovaatimukset, ohjelmistojen asennusprosessin ja peruskonfiguroinnin, joita tarvitaan oman mining-allasinfrastruktuurin perustamiseen.


### Laitteistovaatimukset ja asennus


Kaikkien mining-allasasennusten perusta alkaa valitsemalla sopiva laitteisto, jossa suorituskyky, kustannukset ja energiatehokkuus ovat tasapainossa. Minitietokone on ihanteellinen ratkaisu tähän sovellukseen, sillä se tarjoaa riittävästi prosessointitehoa ja on samalla pienikokoinen ja kuluttaa kohtuullisesti virtaa. Suositeltu kokoonpano sisältää Intel N100 -prosessorin, joka tarjoaa riittävät laskentaresurssit poolitoimintoja varten, ja vähintään yhden teratavun NVMe-tallennustilan Bitcoin-[lohkoketjua](https://planb.academy/resources/glossary/blockchain) ja siihen liittyviä tietoja varten.


Tallennusvaatimus on erityisen kriittinen, koska mining-poolin käyttäminen edellyttää täysin synkronoidun Bitcoin-[solmun](https://planb.academy/resources/glossary/node) ylläpitoa. Yhden teratavun NVMe-asema takaa nopeat luku- ja kirjoitustoiminnot, jotka ovat välttämättömiä lohkoketjun synkronoinnille ja [transaktioiden](https://planb.academy/resources/glossary/transaction-tx) jatkuvalle käsittelylle. Lisäksi riittävä RAM-muistin varaus tukee sekä taustalla olevan Linux-käyttöjärjestelmän että poolitoimintoja koordinoivan solmunhallintaohjelmiston sujuvaa toimintaa.


### Ohjelmistoarkkitehtuuri ja solmujen hallinta


Kotikäyttöön tarkoitetun mining-poolin ohjelmistopino rakentuu Linux-pohjaan, joka tarjoaa Bitcoin-toiminnoille tarvittavan vakauden ja turvallisuuden. Tämän perusjärjestelmän päälle erikoistunut solmujen hallintaohjelmisto, kuten Umbrel, luo intuitiivisen käyttöliittymän Bitcoin-infrastruktuurin hallintaan. Tämä lähestymistapa poistaa suuren osan Bitcoin-solmujen käyttämiseen perinteisesti liittyvästä monimutkaisuudesta, jolloin myös käyttäjät, joilla ei ole laaja-alaista teknistä taustaa, voivat käyttää poolia.


Umbrel toimii kattavana solmunhallinta-alustana, joka hoitaa [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core) -järjestelmän asennuksen, synkronoinnin ja jatkuvan ylläpidon verkkopohjaisen käyttöliittymän avulla. Alustan sovelluskauppamalli mahdollistaa lisäpalveluiden, kuten mining-allasohjelmiston, helpon asentamisen yksinkertaisilla osoita ja napsauta -toiminnoilla. Tämä arkkitehtuuri varmistaa, että käyttäjät voivat keskittyä poolin toimintaan järjestelmänhallinnan sijasta, mutta säilyttävät silti Bitcoin-infrastruktuurinsa täydellisen hallinnan.


### Julkisen uima-altaan asennus ja konfigurointi


Julkisten uima-allasohjelmistojen asentaminen Umbrel-alustan kautta osoittaa nykyaikaisen Bitcoin-infrastruktuurin käyttöönoton virtaviivaistetun luonteen. Prosessi alkaa Umbrelin sovelluskauppaan pääsemisellä web-käyttöliittymän kautta, jossa yksinkertainen haku "public pool" paljastaa käytettävissä olevat mining-allasohjelmistot. Asennus vaatii vain muutaman napsautuksen: sovelluksen valitseminen, asennuksen vahvistaminen ja automaattisen asennusprosessin loppuun saattamisen odottaminen.


Asennusprosessi määrittää automaattisesti tarvittavat yhteydet julkisen pool-ohjelmiston ja taustalla olevan Bitcoin-solmun välille. Tämä integraatio varmistaa, että pooli voi validoida transaktioita, rakentaa lohkomalleja ja jakaa työtä yhdistetyille louhijoille ilman monimutkaisten verkko-ominaisuuksien manuaalista konfigurointia. Kun asennus on valmis, poolin käyttöliittymään pääsee välittömästi käsiksi paikallisverkon kautta, mikä tarjoaa reaaliaikaiset valvonta- ja hallintamahdollisuudet.


### Louhijoiden yhdistäminen ja verkkoa koskevat näkökohdat


mining-laitteiston liittäminen vasta perustettuun pooliin edellyttää, että louhijan pooliasetukset määritetään osoittamaan paikallista infrastruktuuria. Tämä edellyttää poolin oletusosoitteen korvaamista paikallisella IP-osoitteella ja asianmukaisella porttinumerolla, jotka on määritetty julkisen poolin asennuksen aikana. Konfiguraatiomuutos ohjaa mining-laitteistosi laskentaponnistukset ulkoisista pooleista koti-infrastruktuuriin, jolloin voit säilyttää täyden hallinnan mining-toiminnoista ja mahdollisista palkkioista.


Verkkokonfiguraatioilla on ratkaiseva merkitys uima-altaan käytettävyyden ja toimivuuden kannalta. Paikallisverkon asetuksiin kuuluu yleensä vakio IP-osoite, mutta DNS-resoluutiossa saattaa esiintyä vaihtelua reitittimen kokoonpanosta riippuen. Jotkin reitittimet tarjoavat paikallisia DNS-palveluja, jotka luovat ystävällisiä nimiä paikallisille palveluille, kun taas toiset vaativat suoraa IP-osoitteen käyttöä. Jos halutaan laajempi pääsy paikallisen verkon ulkopuolelle, reitittimen porttien välitysmääritys voi olla tarpeen, mutta tämä tuo mukanaan lisää turvallisuusnäkökohtia, jotka edellyttävät riskien ja hyötyjen huolellista arviointia.


Onnistunut mining-kotipoolin perustaminen on merkittävä askel kohti hajautettua Bitcoin-infrastruktuuria, joka tarjoaa sekä koulutuksellista arvoa että käytännön mining-ominaisuuksia ja säilyttää samalla Bitcoin-toimintojen täydellisen hallinnan.


# Laitteiston kokoonpano ja vianmääritys

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Mitä työkaluja käyttää?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

Pinta-asennettavien laitteiden (SMD) juottamisessa, erityisesti Bitaxe-projekteissa, oikeat työkalut ratkaisevat turhautumisen ja menestyksen välillä. Tässä kattavassa oppaassa käsitellään SMD-juotosprojektien tehokkaaseen hoitamiseen tarvittavat olennaiset välineet, aina peruskäsityökaluista erikoislaitteisiin, jotka parantavat juotosvalmiuksiasi.


Jos haluat tutustua kaaviota koskevaan dokumentaatioon, katso tämä [GitHub-repo](https://github.com/skot/bitaxe-doc/tree/main).


### Perustyökalut ja tarkkuusinstrumentit


Kaikkien SMD-juotosasennusten perusta alkaa laadukkailla pinseteillä, jotka toimivat ensisijaisina komponenttien sijoittelutyökaluina. Kaksi pinsettityyppiä osoittautuu tässä työssä arvokkaimmiksi: tavalliset suorakärkiset pinsetit ja pinsetit, joiden kärki on hieman kaareva. Suorakärkiset pinsetit sopivat useimpiin SMD-komponentteihin, joita tyypillisissä Bitaxe-sarjoissa on, kun taas taivutetun kärjen pinsetit ovat erinomaisia, kun työskentelet erittäin pienten komponenttien kanssa, jotka vaativat tarkkaa sijoittelua. Nämä työkalut sisältyvät usein korjaussarjoihin, kuten puhelinten korjaamiseen tarkoitettuihin iFixit-sarjoihin, joten ne ovat helposti useimpien harrastajien saatavilla.


Pinsettien lisäksi hyvät sakset ovat välttämättömät sähköteipin leikkaamiseen, sillä sähköteippiä käytetään moniin tarkoituksiin elektroniikkaprojekteissa. Sähköteippi on välttämätön eristys kaapeleille ja komponenteille, ja laadukkaan teipin helppo saatavuus tehostaa juotosprosessia. Näitä perustarvikkeita voi hankkia rautakaupoista tai verkkokauppiailta ilman, että tarvitaan erikoistuneita elektroniikkatoimittajia.


### Juotospastan käyttö ja hallinta


Juotospastan levitys on yksi SMD-juottamisen kriittisimmistä osa-alueista, ja oikeat työkalut tekevät tästä prosessista sekä tarkan että miellyttävän. Pienet, teräväkärkiset ruiskut, jotka on täytetty juotospastalla, mahdollistavat pastan sijoittamisen poikkeuksellisen hyvin. Tällä menetelmällä voidaan levittää täsmällisesti kutakin liitosta varten tarvittava määrä juotospastaa, ja useimmat oppivat nopeasti oikean tekniikan paineen ja virtausnopeuden hallitsemiseksi käytännön harjoittelun avulla.


Juotospastan valinta vaikuttaa merkittävästi juottamisen onnistumiseen. ChipQuik TS391SNL50 on poikkeuksellinen juotospasta Bitaxe-projekteihin ja yleisiin SMD-töihin. Tämä tahna säilyttää oikean konsistenssin ja sulamisominaisuudet, jolloin vältetään ongelmat, jotka liittyvät halvempiin vaihtoehtoihin, joiden sulamispisteet ovat liian alhaiset. Huonolaatuiset juotospastat voivat aiheuttaa ongelmia, joissa aiemmin juotetut liitokset muuttuvat uudelleen nestemäisiksi viereisiä alueita lämmitettäessä, mikä johtaa komponenttien siirtymiseen ja huonoihin liitoksiin. Vaikka laadukas juotospasta on suurempi alkuinvestointi, paremmat tulokset ja vähentynyt turhautuminen oikeuttavat kustannukset.


### Ongelmanratkaisu- ja siivoustyökalut


Jopa kokeneet juottajat kohtaavat ongelmia, jotka vaativat korjausta, joten juotoksenpoistolaitteet ovat välttämättömiä kaikissa täydellisissä työkalupaketeissa. Juotoksenpoistolaitteisto, joka on pohjimmiltaan lämmitetty tyhjiötyökalu, poistaa ylimääräisen juotteen ja korjaa komponenttien nastojen väliset silloitetut liitokset. Nämä työkalut toimivat tehokkaimmin, kun ne yhdistetään juotosvirtaan, joka parantaa juotteen virtausta ja auttaa juotteenpoistoprosessia toimimaan tehokkaammin.


Juoksevaa ainetta on eri muodoissa, kuten kiinteitä ja nestemäisiä lajikkeita, ja sillä on useita muita tarkoituksia kuin juottamisen avustaminen. Kun juotospasta alkaa menettää tehoaan pitkien työjaksojen aikana, lisävuoksella palautetaan oikeat virtausominaisuudet ja varmistetaan luotettavat liitokset. Pieni lusikanmuotoinen työkalu, joka löytyy usein tarkkuuskorjaussarjoista, helpottaa fluksin tarkkaa levittämistä tietyille alueille saastuttamatta ympäröiviä komponentteja.


Levyjen puhdistaminen on ammattilaistason työn viimeinen vaihe, ja siihen tarvitaan isopropanolialkoholia ja siihen tarkoitettua puhdistusharjaa. Vanha hammasharja sopii tähän tarkoitukseen erinomaisesti, ja isopropanolia sisältävä puristuspullo mahdollistaa puhdistusliuoksen hallitun levittämisen. Tämä yhdistelmä poistaa vuonijäämät ja pastajäämät, jolloin levyt näyttävät puhtailta ja ammattimaisilta, mikä helpottaa myös juotosliitosten tarkastusta.


### Erikoislaitteet ja kehittyneet työkalut


Monimutkaisia integroituja piirejä, erityisesti ASIC-piirejä, sisältävissä projekteissa kaavat muuttavat juotosprosessin työlästä käsin asettelusta tehokkaaksi ja tarkaksi tahnan levittämiseksi. Nämä tarkasti leikatut mallit varmistavat pastan tasaisen paksuuden ja sijoittelun, mikä lyhentää huomattavasti monimutkaisten komponenttien vaatimaa aikaa ja parantaa samalla luotettavuutta. Investointi laadukkaisiin sabloneihin maksaa itsensä takaisin sekä ajansäästönä että parempina tuloksina.


Lämmönhallinnasta tulee ratkaisevan tärkeää, kun työskennellään tehokomponenttien kanssa, jolloin lämpöliima tai lämpörasva on välttämätön tarvike. Nämä materiaalit varmistavat asianmukaisen lämmönsiirron jäähdytyslevyjen ja integroitujen piirien välillä, estävät lämpövaurioita ja takaavat luotettavan toiminnan. Laadukkaat lämpörajapintamateriaalit ovat pieni investointi, joka suojaa paljon kalliimpia komponentteja.


Kaikkien SMD-juotosasennusten sydän on kuumailmapuhdistusasema, joka tuottaa pinta-asennustöissä tarvittavan hallitun lämmön. Vaikka 30-50 dollarin hintaiset asemat voivat olla riittäviä, niistä puuttuu usein korkeamman hintaluokan laitteiden luotettavuus ja tarkkuus. Nämä aloittelevan tason asemat toimivat yleensä tehokkaasti 355 °C:n lämpötilassa, ja niissä on automaattinen lämpötilan alennus, kun käsikappale palautetaan pidikkeeseen. Niiden luotettavuus voi kuitenkin olla epäjohdonmukainen, ja jotkin yksiköt vioittuvat ennenaikaisesti. Vakavissa töissä investoiminen laadukkaampiin laitteisiin erikoistuneilta elektroniikan toimittajilta tarjoaa paremman pitkän aikavälin arvon paremman luotettavuuden ja tarkemman lämpötilan säädön ansiosta.


Näiden työkalujen yhdistelmä luo täydelliset SMD-juotosvalmiudet, jotka ulottuvat paljon laajemmalle kuin Bitaxe-projekteihin ja yleisiin elektroniikkatöihin. Kunkin työkalun roolin ymmärtäminen ja taitotasoon ja projektivaatimuksiin sopivien laadukkaiden laitteiden valitseminen takaa onnistuneet tulokset ja miellyttävän juottokokemuksen.



## Korjaa juotosongelmat

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


Bitaxe-lähetinvastaanotinpaketti asettaa kokoonpanon aikana ainutlaatuisia haasteita, jotka edellyttävät huolellista huomiota komponenttien suuntaamiseen, juotosiltojen estämiseen ja asianmukaiseen lämmönhallintaan. Näiden yleisten ongelmien ja niiden ratkaisujen ymmärtäminen on välttämätöntä, jotta sarjan rakentaminen onnistuu ja vältytään kalliilta komponenttivaurioilta. Tässä luvussa tarkastellaan yleisimpiä Bitaxe-kokoonpanon aikana esiintyviä juotosongelmia ja annetaan käytännön tekniikoita niiden tunnistamiseksi ja ratkaisemiseksi.


### Komponenttien suuntaaminen ja tunnistaminen


Komponenttien oikea suuntaus on yksi kriittisimmistä tekijöistä onnistuneessa Bitaxe-kokoonpanossa, erityisesti MOSFETien Q1 ja Q2 kohdalla. Näissä komponenteissa on erottuvat suuntausmerkit, joita on noudatettava huolellisesti asennuksen aikana. Jokaisessa MOSFET:ssä on pieni pistemerkintä, joka vastaa piirilevyn erityisiä pad-järjestelyjä. Avain oikeaan suuntaukseen on näiden komponenttien fyysisen rakenteen ymmärtäminen, sillä niissä on neljä nastaa, jotka on järjestetty siten, että niissä on yksi suuri nasta ja kolme pienempää nastaa, joilla ei ole yhteyttä suureen nastaan.


Kun asennat Q1:n ja Q2:n, tutki sekä komponentti että piirilevy huolellisesti. Piirilevyn ulkoasu osoittaa selvästi aiotun suuntauksen sen pad-konfiguraation kautta, jossa neljä nastaa on sijoitettu MOSFET-rakenteen mukaisesti. Varmista suuntaus aina ennen suuren komponentin juottamista vertaamalla komponentin fyysisiä merkintöjä piirilevyn tyynyjärjestykseen. Tämä yksinkertainen tarkistusvaihe estää turhautumista, joka aiheutuu väärin suunnattujen komponenttien juottamisesta ja asentamisesta uudelleen.


Väärän suuntauksen seuraukset ulottuvat pelkkiä toiminnallisia ongelmia laajemmalle. Väärin suunnatut MOSFETit voivat aiheuttaa piirin toimintahäiriöitä, joita on vaikea diagnosoida ja jotka voivat vaatia komponenttien täydellistä vaihtoa. Jos suuntauksen tarkistamiseen käytetään aikaa ennen lämmityksen aloittamista, varmistetaan piirin moitteeton toiminta ja estetään tarpeeton vianmääritys myöhemmin kokoonpanoprosessissa.


### Juotossiltojen ja ylimääräisen juotteen hallinta


Juotosillat ovat toinen yleinen haaste Bitaxe-kokoonpanossa, erityisesti U10:n kaltaisten hienojakoisten komponenttien kohdalla. Nämä vierekkäisten nastojen väliset ei-toivotut liitokset voivat aiheuttaa piirin toimintahäiriöitä ja vaativat huolellista poistotekniikkaa. Tehokkain lähestymistapa on käyttää juotteenpoistoköyttä, kuparipunosta valmistettua materiaalia, joka imee ylimääräisen juotteen, kun sitä kuumennetaan. Tämä tekniikka vaatii kärsivällisyyttä ja asianmukaista työkalun valintaa, jotta herkät komponentit eivät vahingoitu.


Kun käsittelet integroitujen piirien juotosiltoja, käytä piirilevyn pidikettä tai nivellettyä puristinta pitämään komponenttia turvallisesti kiinni työskentelyn aikana. Kuumenna vaurioitunutta aluetta hellävaraisesti ja vedä juotoslankaa varovasti silloitettujen liitosten yli. Kuparipunos imee luonnollisesti ylimääräisen juotteen ja erottaa ei-toivotut liitokset. Tämä prosessi voi vaatia useita yrityksiä, mutta sinnikkyydellä saadaan aikaan puhtaat, kunnolla erotetut liitokset.


Ennaltaehkäisy on edelleen paras lähestymistapa juotosiltojen hallintaan. Sopivien juotospastamäärien käyttäminen ja käden vakauden säilyttäminen komponenttien sijoittamisen aikana vähentävät merkittävästi sillan muodostumista. Kun siltoja syntyy, niihin on puututtava välittömästi sen sijaan, että toivotaan, etteivät ne vaikuta piirin toimintaan. Jopa näennäisen pienetkin sillat voivat aiheuttaa merkittäviä toiminnallisia ongelmia, joita on vaikea diagnosoida, kun levy on koottu valmiiksi.


### Kriittiset komponentit ja erityishuomioita


Buck-muunnin U9 ansaitsee erityisen huomion, koska se muuntaa 5 voltin jännitteen 1,2 voltiksi ASIC-sirua varten. Tämä komponentti asettaa ainutlaatuisia haasteita viiden pienen liitäntänsä ja vikaantumistaipumuksensa vuoksi. Asianmukainen asennus edellyttää tarkkaa juotospastan levitystä ja huolellista lämmönhallintaa. Riittämätön juotospasta U9:n alla voi johtaa huonoihin liitäntöihin, jotka estävät jännitteen asianmukaisen muuntamisen, kun taas liiallinen tahna voi luoda siltoja, jotka aiheuttavat piirin toimintahäiriöitä.


U9 tuottaa erottuvia äänimerkkejä, kun juotosiltaongelmia ilmenee, ja tuottaa korkeataajuista kohinaa, joka poikkeaa ASIC:n normaalista toiminnasta. Tämä auditiivinen diagnostiikkatekniikka voi auttaa ongelmien tunnistamisessa, vaikka sen havaitseminen edellyttääkin hyvää korkeataajuuskuuloa. Kun audiodiagnoosi ei ole mahdollista, visuaalinen tarkastus on välttämätöntä. Tutki kaikki liitännät huolellisesti ja etsi siltoja tai riittämättömiä juotospeitteitä.


Jos U9 ei anna vaadittua 1,2 voltin ulostuloa, vaikka se vaikuttaa oikein juotetulta, todennäköisenä syynä on riittämätön juotospasta. Irrota komponentti, levitä pieni määrä lisää juotospastaa ja asenna se uudelleen. Jos yksittäisten nastojen juotospeitto on riittämätön, levitä pinseteillä varovasti pieniä määriä juotospastaa tiettyihin kohtiin. Juotospasta virtaa luonnollisesti komponentin alle, kun sitä lämmitetään, ja luo kapillaarisesti asianmukaiset liitokset.


### Lämmönhallinta ja komponenttien suojaus


Asianmukainen lämmönhallinta suojaa herkkiä komponentteja lämpövaurioilta ja varmistaa samalla luotettavat juotosliitokset. Komponentit, kuten kideoskillaattori Y1 ja U1, ovat erityisen herkkiä pitkäaikaiselle lämpöaltistukselle ja vaativat huolellista lämpötilan hallintaa. Pidä juotosraudan lämpötila 350 celsiusasteessa, mutta minimoi lämmön käyttöaika komponenttien vaurioitumisen estämiseksi. Nopeat ja tehokkaat juottotekniikat suojaavat näitä herkkiä komponentteja ja saavat aikaan luotettavia liitoksia.


ASIC-siru vaatii erityisiä käsittelytekniikoita, koska sen tappirakenne on monimutkainen ja se on herkkä mekaaniselle rasitukselle. Kun käytät juotospastan levittämiseen kaavoja, varmista, että kaikki nastat peittyvät tasaisesti, jotta komponentit eivät istu epätasaisesti. Jos liiallinen juotospasta aiheuttaa ASIC:n epätasaisen istuvuuden, anna kokoonpanon jäähtyä kokonaan ennen korjausten tekemistä. Paina varovasti vain komponentin merkittyjä reunoja, ei koskaan keskimmäistä muotin aluetta, uudelleenlämmityksen aikana, jotta saavutetaan oikea istuvuus.


Komponentti U8 asettaa ainutlaatuisia haasteita sen lukuisien nastojen ja mahdollisesti taivutettujen johtojen vuoksi. Kun nastat taipuvat käsittelyn aikana, käytä piirilevyn pidikettä tai nivelpidikettä komponentin kiinnittämiseen ja suorista kyseiset nastat varovasti. Työskentele hitaasti ja kärsivällisesti, jotta herkät johtimet eivät katkea. Sen ymmärtäminen, että U8:n tietyt nastaryhmät ovat sisäisesti kytkettyjä, voi yksinkertaistaa vianetsintää, sillä näiden tiettyjen nastojen väliset sillat eivät vaikuta piirin toimintaan. Muiden nastojen väliset sillat on kuitenkin poistettava varovasti, jotta voidaan varmistaa asianmukainen toiminta.


## Kuinka debugata Bitaxe AxeOS:n avulla?

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Bitaxe mining -laitteiden kanssa työskenneltäessä laitteistoviat voivat ilmetä monin eri tavoin, jotka eivät välttämättä ole heti ilmeisiä. Ymmärtämällä, miten näitä ongelmia voidaan järjestelmällisesti diagnosoida AxeOS-käyttöjärjestelmän avulla, voidaan säästää merkittävästi aikaa ja estää tarpeettomat komponenttien vaihdot. Tässä luvussa tarkastellaan diagnostiikkatekniikoita ja vianetsintämenetelmiä, joita kokeneet teknikot käyttävät tiettyjen laitteisto-ongelmien tunnistamiseen ohjelmistoanalyysin avulla.


### Virrankulutuksen ilmaisimien ymmärtäminen


AxeOS:n ensimmäinen ja kriittisin diagnostinen indikaattori on virrankulutuksen seuranta. Normaalit Bitaxe-laitteet, mukaan lukien Bitaxe Ultra- ja Bitaxe Supra -mallit, kuluttavat normaalikäytössä tyypillisesti 10-17 wattia. Tämä perusmittaus toimii koko järjestelmän ensisijaisena terveysindikaattorina. Kun virrankulutus laskee merkittävästi tämän alueen alle, erityisesti alle 3 watin, se on merkki ASIC-sirun tai sitä tukevan piirin perustavanlaatuisesta ongelmasta.


Alhaisen virrankulutuksen skenaariot vaativat välitöntä huomiota, koska ne osoittavat, että mining-siru on joko täysin toimintakyvytön tai toimii vakavasti heikentyneessä tilassa. Pelkästään tämän mittauksen avulla voit nopeasti erottaa toisistaan suorituskykyongelmat ja täydelliset laitteistoviat. AxeOS:n teholukema antaa reaaliaikaista palautetta, jonka avulla voit seurata laitteelle tekemiesi korjausyritysten tehokkuutta.


### ASIC:n jännitemittausten analysointi


AxeOS:n ASIC-jännitteenmittausominaisuus tarjoaa ratkaisevan tärkeää diagnostiikkatietoa, joka auttaa määrittämään laitteisto-ongelmien tarkan luonteen. Kun tutkit jännitelukemia, sinun on ymmärrettävä mitatun jännitteen ja pyydetyn jännitteen välinen suhde, jotta voit diagnosoida ongelmat oikein. Järjestelmä näyttää sekä ASIC-sirulle syötetyn jännitteen että jännitteen, jota siru pyytää virranhallintajärjestelmältä.


Kun ASIC:n jännitemittaus on tasan 1,2 volttia ja virrankulutus on alle 3 wattia, tämä yhdistelmä viittaa joko juotosongelmaan ASIC-sirussa tai ASIC:n täydelliseen vikaantumiseen. Tämä jännitemittaus viittaa siihen, että virta saavuttaa sirun sijainnin, mutta itse siru ei toimi kunnolla. ASIC-piirin fyysinen tarkastus voi paljastaa halkeamia tai muita näkyviä vaurioita, jotka selittäisivät tämän käyttäytymismallin.


Erilainen diagnostiikkaskenaario syntyy, kun näet alhaisen virrankulutuksen ja hyvin alhaiset pyydetyt jännitelukemat, kuten 100 millivolttia tai 0,5 volttia. Tämä kuvio osoittaa, että ASIC-siru ei saa riittävää jännitesyöttöä, mikä tyypillisesti viittaa ongelmiin U9-syöksymuuntimen komponentissa. Buck-muunnin on vastuussa tarkasta jännitteensäädöstä, jota ASIC-sirut tarvitsevat toimiakseen moitteettomasti.


### Lokitietojen tulkinta ja ASIC-viestintä


AxeOS-lokitusjärjestelmä antaa arvokasta tietoa siitä, onko ASIC-sirusi yhteydessä ohjausjärjestelmään. Kun pääset lokitietoihin "show logs" -toiminnon kautta, "ASIC results" -merkinnät vahvistavat, että siru ei ole vain kytketty virtalähteeseen, vaan se myös käsittelee aktiivisesti työtä ja palauttaa tuloksia. Tämä tiedonsiirto osoittaa, että ASIC on juotettu oikein ja että se pitää yhteyttä ohjauspiiriin.


ASIC-tulosten puuttuminen lokitiedostoista, erityisesti kun ne yhdistetään muihin oireisiin, auttaa rajaamaan ongelman tiettyihin komponentteihin tai yhteysongelmiin. Tämän diagnoosimenetelmän avulla voidaan erottaa toisistaan piirit, jotka eivät vastaa lainkaan, ja piirit, joilla voi olla ajoittaisia yhteysongelmia. Lokianalyysi on erityisen arvokas, kun ratkaistaan monimutkaisia ongelmia, joissa useat oireet saattavat viitata eri perimmäisiin syihin.


### Järjestelmällinen vianmääritysmenetelmä


Kun diagnosoit Bitaxe-laitteisto-ongelmia, systemaattisen lähestymistavan noudattaminen estää kriittisten ongelmien huomaamatta jättämisen ja varmistaa tehokkaan korjausprosessin. Aloita dokumentoimalla virrankulutus- ja jännitelukemat ja korreloi sitten nämä mittaukset lokitietojen kanssa, jotta saat kokonaiskuvan järjestelmän käyttäytymisestä. Tämä metodinen lähestymistapa auttaa tunnistamaan, johtuvatko ongelmat itse ASIC-sirusta, virransyöttöjärjestelmästä vai komponenttien välisistä tiedonsiirtoreiteistä.


Tapauksissa, joissa U9-syöksymuunnin näyttää olevan ongelmana, fyysinen tarkastus ja mahdollinen uudelleenjuottaminen voi olla tarpeen. U9-komponentti on erityisen altis juotosongelmille, erityisesti ensikokoonpanotilanteissa. Kun jännitteen säätöongelmia epäillään, virransyöttöongelmien lopullinen vahvistus saadaan käyttämällä yleismittaria, jolla voidaan varmistaa, että ASIC-nastoissa todella on 1,2 volttia. Jos nastoissa on jännite, mutta ASIC ei silti toimi, eikä fyysinen tarkastus paljasta vaurioita, seuraava looginen askel on ASIC-sirun vaihtaminen. Jos ongelmat jatkuvat ASIC:n vaihdon jälkeenkin, ASIC-sirua ohjaava U2-komponentti saattaa vaatia huomiota vianmäärityksen viimeisenä vaiheena.


## Miten vianmääritys tapahtuu USB:n avulla?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Bitaxe mining -laitteiden vianmäärityksessä suora pääsy laitteen sisäiseen lokijärjestelmään tarjoaa korvaamattomia tietoja, joita verkkopohjaiset käyttöliittymät eivät voi tarjota. Tässä luvussa selvitetään, miten Bitaxe-laitteeseen voidaan luoda suora USB-sarjaliitäntä ESP-IDF-kehyksen avulla, mikä mahdollistaa järjestelmän lokien, käynnistyssekvenssien ja virheilmoitusten reaaliaikaisen seurannan. Tämä virheenkorjausmenetelmä on erityisen tärkeä, kun kyseessä ovat laitteet, jotka käynnistyvät usein uudelleen tai joissa on laitteistovikoja, sillä se tallentaa kaikki diagnostiikkatiedot, jotka saattavat kadota järjestelmän uudelleenkäynnistyksen aikana.


Debuggausprosessi edellyttää Visual Studio Codea ESP-IDF-laajennuksella, vaikka mitä tahansa yhteensopivaa IDE:tä voidaan käyttää. Tämä menetelmä toimii kaikkien Bitaxe-mallien kanssa, joissa on USB-portti, mukaan lukien Bitaxe Ultra 204 ja muut sarjan mallit. Suora sarjaliitäntä ohittaa mahdolliset web-käyttöliittymän rajoitukset ja tarjoaa suodattamattoman pääsyn laitteen sisäisiin tilatietoihin.


### Sarjaliikenteen määrittäminen


Yhteyden luominen Bitaxe-laitteen kanssa alkaa USB-kaapelin liittämisellä ja ESP-IDF-päätteen avaamisella kehitysympäristössäsi. Komento `idf.py monitor` käynnistää yhteysprosessin ja etsii automaattisesti käytettävissä olevat COM-portit UART-yhteyden luomiseksi Bitaxe-laitteesi ESP32-sirun kanssa. Järjestelmä käy tyypillisesti läpi käytettävissä olevat portit (COM3, COM4, COM16 jne.), kunnes se löytää oikean yhteyden.


Kun yhteys on muodostettu, päätelaite näyttää koko käynnistyssekvenssin ja käynnissä olevat toimintalokit. Alkuvaiheen yhteysprosessi voi kestää useita hetkiä, kun järjestelmä tunnistaa oikean viestintäportin. Jos automaattinen portin tunnistus epäonnistuu, voit määrittää COM-portin manuaalisesti IDE:n portinvalintaliitännän kautta. Tämä suora viestintäkanava pysyy aktiivisena koko laitteen toiminnan ajan, jolloin järjestelmän diagnostiikka ja suorituskykymittarit ovat jatkuvasti käytettävissä.


### Käynnistyssekvenssin ja normaalin toiminnan lokien tulkinta


Käynnistyssekvenssi antaa kriittisiä tietoja Bitaxe-laitteen laitteiston kokoonpanosta ja alustamisprosessista. Normaalit käynnistyslokit alkavat ESP-IDF-versiotiedoilla, joita seuraa tunnusomainen "Welcome to the Bitaxe. Hack the planet" -viesti, joka vahvistaa onnistuneen laiteohjelmiston latauksen. Tämän jälkeen järjestelmä näyttää ASIC-taajuuskonfiguraation, laitteen mallitunnuksen ja piirilevyn versiotiedot.


Oikein toimiva laite näyttää onnistuneen I2C-initialisoinnin ja ASIC-jännitteen asetuksen 1,2 volttiin. Lokit näyttävät GPIO:n tilatiedot ja Wi-Fi:n alustussekvenssit, minkä jälkeen seuraa DHCP-palvelimen konfigurointi ja IP-osoitteen määritys. Yksi tärkeimmistä indikaattoreista on ASIC-sirun tunnistusviesti, jonka pitäisi ilmoittaa "detected one ASIC chip" (havaittu yksi ASIC-siru), jos kyseessä on yksisiruinen laite. Tämä vahvistus vahvistaa, että mining-laitteisto on liitetty oikein ja kommunikoi ESP32-ohjaimen kanssa.


Toimintalokeista käy ilmi, että laitteessa on käynnissä useita samanaikaisia tehtäviä, kuten kerroksen API viestintä, päätehtävien koordinointi, ASIC-tehtävien hallinta ja kerroksen tehtävien käsittely. Nämä eri tehtävätunnisteet auttavat eristämään ongelmat tiettyihin järjestelmäkomponentteihin. Normaaliin toimintaan kuuluvat pool-yhteyden muodostaminen, vaikeusasteen säätöviestit, tehtävien jonottaminen ja jonon poistaminen sekä nonce-luonnoksen raportointi. Onnistuneet mining-toiminnot näyttävät ASIC-tulokset vaikeuslaskelmineen ja mining-lähetysvahvistukset, kun osuudet täyttävät vaaditun kynnysarvon.


### Laitteistovikojen ja virhemallien tunnistaminen


Laitteistoviat näkyvät lokitiedostoissa erityisinä virhemalleina, jotka osoittavat, mitkä komponentit eivät toimi oikein. Yleisin vikaantumistapa on I2C-viestintävirhe, joka liittyy tiettyihin Bitaxe-piirilevyn integroituihin piireihin. Esimerkiksi DS4432U:n tiedonsiirtovirheet näkyvät "ESP_ERROR_CHECK failed" -viesteinä, joissa on aikakatkaisuindikaattorit, mikä viittaa jännitteen säätöongelmiin tai juotosongelmiin, jotka vaikuttavat näytön tiedonsiirrosta vastaavaan U10-komponenttiin.


Näissä virheilmoituksissa on yksityiskohtaisia virheenkorjaustietoja, kuten tietty lähdetiedosto (main_ds4432u.c), epäonnistunut funktiokutsu ja tehtävää käsittelevä prosessoriydin. Takautumatiedot tarjoavat lisäyhteyttä edistyneeseen vianmääritykseen. EMC2101-lämpötilan- ja tuulettimenohjaussirun kanssa voi esiintyä samanlaisia virhemalleja, joista kumpikin tuottaa omanlaisensa lokimerkinnät, jotka auttavat tunnistamaan vikaantuneen komponentin.


Fyysiset laitteisto-ongelmat ilmenevät usein toistuvina virhesykleinä, joita seuraavat järjestelmän uudelleenkäynnistykset. Jos laitteesta kuuluu ääniä käytön aikana, se viittaa yleensä juotosongelmiin, kuten komponenttien nastojen välisiin siltoihin tai puutteellisiin juotosliitoksiin. Vaikka nämä mekaaniset ongelmat eivät välttämättä aina ole generate-kohtaisia lokimerkintöjä, ne luovat epävakaita käyttöolosuhteita, jotka näkyvät toistuvina kaatumisten ja uudelleenkäynnistysten jaksoina valvontatulosteissa.


### Edistyneet vianmääritysstrategiat


Sarjavalvonta tarjoaa useita etuja verkkopohjaisiin vianmääritysliittymiin verrattuna, erityisesti ajoittaisten vikojen tai usein uudelleenkäynnistyvien laitteiden tapauksessa. Jatkuva lokin tallennus varmistaa, että diagnostiikkatietoja ei menetetä järjestelmän uudelleenkäynnistyksen aikana, toisin kuin web-käyttöliittymissä, jotka saattavat menettää tietoja yhteyden katkaisutapahtumien aikana. Tämän kattavan lokitiedoston avulla on mahdollista tunnistaa vikaantumismalleja ja korreloida tietyt virhetilanteet laitteisto- tai ympäristötekijöihin.


Kun analysoit ongelmallisia laitteita, keskity yksittäisten virheilmoitusten sijasta vikoihin johtaneiden tapahtumien sarjaan. Onnistuneessa ASIC-viestinnässä pitäisi näkyä säännöllistä työnkäsittelyä, nonce-tunnisteiden luomista ja jakosyklien lähettämistä. Puuttuvat ASIC-tulokset lokitiedostoissa viittaavat ESP32:n ja mining-sirun välisiin kommunikaatiohäiriöihin, jotka johtuvat usein virransyöttöongelmista, vaurioituneista johtimista tai komponenttivioista.


Järjestelmällistä vianmääritystä varten dokumentoi virhemallit ja komponenttikohtaiset viat ennen kuin haet yhteisön tukea. Yksityiskohtaiset virhelokit, mukaan lukien sirun erityiset tunnisteet ja vikatilat, antavat kokeneille käyttäjille mahdollisuuden antaa kohdennettuja korjausohjeita, kuten komponenttien vaihtomenetelmiä tai juotoskorjauksia. Tämä menetelmällinen lähestymistapa laitteiston vianmääritykseen parantaa merkittävästi korjausten onnistumisprosenttia ja lyhentää monimutkaisten ongelmien vianmääritykseen kuluvaa aikaa.


# Kehittynyt räätälöinti

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Muokkaa piirilevyä

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad on yksi tehokkaimmista avoimen lähdekoodin työkaluista piirilevyn (PCB) suunnitteluun ja reititykseen. Tämän ammattilaistason ohjelmiston avulla insinöörit ja harrastajat voivat luoda monimutkaisia elektroniikkasuunnitelmia sijoittamalla komponentteja virtuaalisille levyille ja reitittämällä monimutkaiset jäljet, jotka yhdistävät nämä komponentit toisiinsa. KiCadin tekee erityisen arvokkaaksi koulutus- ja kehitystarkoituksiin sen täydellinen avoimen lähdekoodin luonne, jonka ansiosta käyttäjät voivat muokata, mukauttaa ja oppia olemassa olevista malleista ilman lisenssirajoituksia.


Bitaxe-projekti on esimerkki avoimen lähdekoodin laitteistokehityksen voimasta, sillä se tarjoaa täydellisen piirilevysuunnittelun, jota käyttäjät voivat tutkia, muokata ja räätälöidä omien tarpeidensa mukaan. Tämä saavutettavuus luo erinomaisen oppimisympäristön, jossa opiskelijat ja ammattilaiset voivat tutkia todellisia piirilevymalleja ja samalla kehittää ymmärrystään elektroniikkajärjestelmistä. Kyky muokata visuaalisia elementtejä, kuten logoja, tarjoaa helposti lähestyttävän lähtökohdan käyttäjille, joita elektroniikan suunnittelun tekninen monimutkaisuus saattaa pelottaa.


### KiCad-ympäristön määrittäminen


Ennen kuin aloitat räätälöintityöt, kehitysympäristön asianmukainen asennus on välttämätöntä. Bitaxe-arkisto on ladattava paikalliselle koneellesi, mikä tapahtuu yleensä GitHubin ZIP-lataustoiminnolla. Tämä arkisto sisältää kaikki tarvittavat projektitiedostot, mukaan lukien KiCad-projektitiedostot, komponenttikirjastot ja suunnitteludokumentaatio, joita tarvitaan onnistuneeseen muokkaukseen.


KiCadin asennus on suoritettava KiCadin verkkosivuston virallisen jakelun avulla, jolloin varmistetaan yhteensopivuus projektitiedostojen kanssa ja uusimpien ominaisuuksien käyttö. Kun sekä arkisto että KiCad on asennettu oikein, projektin avaaminen edellyttää navigointia Bitaxe Ultra KiCad -projektitiedostoon ladatun arkistorakenteen sisällä. Tämä projektitiedosto toimii keskeisenä keskuksena, joka linkittää kaikki siihen liittyvät suunnittelutiedostot, komponenttikirjastot ja kokoonpanoasetukset.


Monimutkaisen piirilevysuunnittelun ensimmäinen näkymä voi tuntua ylivoimaiselta, kun lukuisat komponentit, jäljet ja kerrokset luovat tiheän visuaalisen maiseman. KiCadin 3D-katselutoiminto on kuitenkin korvaamaton työkalu fyysisen asettelun ja tilasuhteiden ymmärtämiseen suunnittelussa. Tämä kolmiulotteinen näkökulma muuttaa abstraktin kaaviokuvan realistiseksi visualisoinniksi lopullisesta valmistetusta tuotteesta, mikä helpottaa komponenttien sijoittelun ja yleisen suunnittelun estetiikan ymmärtämistä.


### Logon räätälöintiprosessi


Logojen mukauttaminen piirilevymalleihin on yksi helpoimmista muutoksista KiCadin uusille käyttäjille, sillä se vaatii vain vähän teknistä osaamista ja tarjoaa välittömiä visuaalisia tuloksia. Prosessi alkaa kuvanmuunnin-työkalulla, joka muuntaa tavalliset kuvatiedostot piirilevysuunnitteluohjelmiston kanssa yhteensopiviin jalanjälkiformaatteihin. Muunnosprosessi vaatii huolellista huomiota mitoitusparametreihin, jotka mitataan yleensä millimetreinä, jotta varmistetaan oikea skaalaus lopullisessa valmistetussa levyssä.


Kuvamuuntimen työnkulkuun kuuluu useita kriittisiä vaiheita, jotka määrittävät mukautettujen logojen lopullisen ulkoasun ja sijoittelun. Lähdekuvan valinnassa olisi asetettava etusijalle kontrastikkaat mallit, jotka soveltuvat hyvin piirilevyjen valmistuksessa käytettävään silkkipainomenetelmään. Koon määrittely on ratkaisevan tärkeää, sillä logojen on oltava riittävän suuria, jotta ne ovat luettavissa valmistuksen jälkeen, mutta eivät saa häiritä komponenttien sijoittelua tai toiminnallisuutta. Valinta etu- ja takapuolen silkkipainokerrosten välillä vaikuttaa sekä näkyvyyteen että valmistukseen liittyviin näkökohtiin.


Jalanjälkikirjaston hallinta on KiCadin räätälöinnin perustavanlaatuinen osa-alue, joka edellyttää, että käyttäjät ymmärtävät, miten ohjelmisto järjestää ja käyttää suunnitteluelementtejä. Mukautettujen logojen lisääminen edellyttää uusien jalanjälkikirjastojen luomista tai olemassa olevien muokkaamista ja sitten näiden kirjastojen asianmukaista linkittämistä projektirakenteeseen. Tällä prosessilla varmistetaan, että mukautetut elementit pysyvät käytettävissä eri suunnitteluistunnoissa ja että niitä voidaan helposti jakaa muiden tiimin jäsenten tai yhteistyökumppaneiden kanssa.


### Edistynyt suunnittelun tutkiminen ja ymmärtäminen


Yksinkertaisen logon mukauttamisen lisäksi KiCad tarjoaa tehokkaita työkaluja monimutkaisten PCB-mallien tutkimiseen ja ymmärtämiseen. Kerrosten hallintajärjestelmän avulla käyttäjät voivat tarkastella valikoivasti suunnittelun eri näkökohtia komponenttien sijoittelusta ja reitityksestä valmistusmäärittelyihin ja kokoonpanotietoihin. Tämä kerroksittainen lähestymistapa mahdollistaa tiettyjen suunnitteluelementtien yksityiskohtaisen analysoinnin ilman toisiinsa liittymättömien komponenttien aiheuttamaa visuaalista sekaannusta.


Jäljen reititysanalyysi on yksi piirilevyjen tutkimisen opettavaisimmista näkökohdista, sillä se paljastaa, miten sähköiset yhteydet kulkevat komponenttien ja osajärjestelmien välillä. Seuraamalla yksittäisiä jälkiä tai toisiinsa liittyvien signaalien ryhmiä käyttäjät voivat kehittää ymmärrystä piirin toiminnallisuudesta ja suunnittelupäätöksistä. Esimerkiksi tehonjakeluverkkojen tutkiminen paljastaa, miten jännitteensäätö- ja suodatinkomponentit toimivat yhdessä tuottaakseen puhdasta ja vakaata virtaa herkille elektroniikkakomponenteille.


Kaaviosuunnittelun ja fyysisen asettelun välinen suhde käy ilmi tarkastelemalla huolellisesti komponenttien sijoittelua ja reitityspäätöksiä. Ymmärtäminen, miksi tietyt komponentit on sijoitettu tiettyihin paikkoihin, miten termiset näkökohdat vaikuttavat asettelupäätöksiin ja miten signaalin eheysvaatimukset ohjaavat reititysvalintoja, tarjoaa arvokasta tietoa ammattimaisista PCB-suunnittelukäytännöistä. Nämä tiedot ovat korvaamattomia käyttäjille, jotka kehittävät omia suunnitelmiaan tai muokkaavat olemassa olevia suunnitelmia tiettyjä sovelluksia varten.


KiCadin kattavat suunnittelusääntöjen tarkistus- ja verifiointityökalut varmistavat, että muutokset säilyttävät sähköisen ja valmistuksellisen yhteensopivuuden. Nämä automatisoidut järjestelmät auttavat ehkäisemään yleisiä suunnitteluvirheitä ja opastavat samalla käyttäjiä alan standardeista ja parhaista käytännöistä. 3D-visualisoinnin integrointi sähkösuunnittelutietoihin luo tehokkaan oppimisympäristön, jossa teoreettisista käsitteistä tulee konkreettisia visuaalisen esityksen ja interaktiivisen tutkimisen avulla.


## Kuinka luoda tehdastiedosto?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

Räätälöidyn laiteohjelmiston rakentaminen ESP-pohjaisille mining-laitteille vaatii huolellista huomiota konfigurointiin, riippuvuuksiin ja asianmukaiseen rakentamisprosessiin. Tässä kattavassa oppaassa käydään läpi koko prosessi, jossa luodaan sekä vakiofirmware-binääritiedostoja että tehdasasetukset sisältäviä tiedostoja, jotka sisältävät valmiiksi konfiguroituja asetuksia, mikä tekee käyttöönotosta tehokkaampaa ja vähentää loppukäyttäjien asennusaikaa.


Huomaa, että tämä luku on melko tekninen, ja sen voi vain ohittaa, jos olet siitä utelias.


### Kehitysympäristön määrittäminen


Jos haluat aloittaa ESP-Miner-firmware-kehityksen, sinun pitäisi luoda asianmukainen kehitysympäristö Visual Studio Code -ohjelmistolla, mieluiten linux-jakelussa. ESP-IDF-laajennus on tämän asennuksen kulmakivi, joka tarjoaa tarvittavat työkalut ja kehysintegraation ESP32-kehitystä varten. Kun ESP-IDF-laajennusta asennetaan ensimmäistä kertaa, käyttäjät saavat käyttöönsä asennusoppaan, joka helpottaa konfigurointiprosessia.


Kriittinen seikka asennusprosessissa on sopivan ESP-IDF-version valitseminen. Aiemmin suositeltiin versiota 5.1.3, mutta käytännön kokemukset ovat osoittaneet, että tämä versio voi aiheuttaa rakentamisongelmia, jotka vaikeuttavat kehitysprosessia. Nyt suositellaan ESP-IDF:n version 5.3 Beta 1 käyttöä, joka on osoittautunut ratkaisevaksi näissä rakennuskomplikaatioissa ja varmistaa, että Bitaxe-laitteet toimivat oikein. Asennusprosessi edellyttää Express-asennusvaihtoehdon valitsemista ja erityisesti version 5.3 Beta 1 valitsemista käytettävissä olevista vaihtoehdoista.


Kehitysympäristön asetukset ulottuvat ESP-IDF:n asennusta pidemmälle ja sisältävät myös päätelaitteen asianmukaisen konfiguroinnin. Visual Studio Code tarjoaa useita menetelmiä ESP-IDF:n toimintojen käyttämiseen, mukaan lukien komentopalettivaihtoehto ESP-IDF:n päätelaitteen avaamiseksi tai käyttöliittymässä olevan erityisen päätelaitekuvakkeen käyttäminen. Tämä erikoistunut pääteympäristö varmistaa, että kaikki ESP-IDF-komennot toimivat oikein, ja tarjoaa pääsyn koko työkaluketjuun.


### ESP-Miner:n asetusten määrittäminen


Konfigurointitiedosto on ESP-Miner:n räätälöintiprosessin ydin, sillä se sisältää kaikki olennaiset parametrit, jotka määrittelevät laitteen toiminnan kohdeympäristössä. Konfiguraatio sisältää verkkoasetukset, mining-pooliyhteydet ja laitteistokohtaiset parametrit, jotka on räätälöitävä tietyn käyttöönottoskenaarion mukaan.


Verkon määritys on asennusprosessin tärkein osa, ja se edellyttää Wi-Fi-tiedot, kuten SSID-tunnuksen ja salasanan, määrittämistä. Tuotantokokoonpanojen tulisi sisältää todelliset verkkotunnukset, joita laite käyttää käyttöympäristössään, eikä käyttää paikanpitäjiä, kuten "testi". Konfiguraatio mukautuu myös erilaisiin mining-allasasetuksiin, jotka tukevat sekä yksityisiä allaskonfiguraatioita, joissa on tietyt IP-osoitteet, että julkisia pooleja, kuten public-pool.io, ja niitä vastaavia porttiasetuksia.


Mining-kohtaisiin konfigurointiparametreihin kuuluu stratum user -asetus, joka vastaa yleensä Bitcoin-osoitetta, johon mining-palkkiot pitäisi ohjata. Laitteiston lisäparametrien, kuten taajuusasetusten, jännitekonfiguraatioiden ja ASIC-tyyppimääritysten, on vastattava kohdelaitteistoalustaa. GitHub-tietovarastossa on valmiiksi konfiguroituja esimerkkejä eri laitteistovaihtoehtoja varten, kuten Super-laitteille suunniteltu BM1368-konfiguraatio ja BM1366-asetukset Ultra-vaihtoehtoja varten. Piirilevyn versiomääritykset, kuten porttiversion asettaminen arvoon 401 uudempia laitteistoversioita varten, varmistavat yhteensopivuuden kohdelaitteen erityisominaisuuksien kanssa.


### Web Interface:n ja ydinohjelmiston rakentaminen


ESP-Miner-projektissa on kehittynyt web-käyttöliittymä, joka vaatii erillisen kääntämisen ennen kuin laiteohjelmiston pääasiallista rakentamisprosessia voidaan aloittaa. Tämä web-käyttöliittymä, josta käytetään nimitystä AxeOS-firmaohjelmisto, tarjoaa käyttäjille kattavan hallintaliittymän mining-laitteiden valvontaan ja ohjaukseen.


Verkkokäyttöliittymän rakentamisprosessi alkaa siirtymällä HTTP-palvelimen hakemistoon päätietovarastorakenteen sisällä, erityisesti AxeOS-alihakemistoon. Tämä sijainti sisältää Node.js-pohjaisen verkkosovelluksen, joka edellyttää riippuvuuksien asentamista npm install -komennolla. Rakennusjärjestelmä olettaa, että Node.js on asennettu kunnolla kehitysjärjestelmään, sillä se on perustavanlaatuinen edellytys web-käyttöliittymän kokoamisprosessille.


Riippuvuuksien asentamisen jälkeen npm run build -komennolla käännetään web-käyttöliittymän komponentit ja luodaan tarvittavat tiedostot, jotka upotetaan ESP32:n laiteohjelmistoon. Tämä kääntämisprosessi tuottaa optimoidut web-ominaisuudet, jotka tarjoavat käyttöliittymän toiminnallisuuden säilyttäen samalla tehokkaan muistinkäytön rajoitetulla ESP32-alustalla. Tämän rakennusvaiheen onnistunut suorittaminen on välttämätöntä ennen kuin siirrytään pääasialliseen laiteohjelmiston kokoamiseen, sillä ESP-Miner-ohjelmisto sisältää nämä web-käyttöliittymäkomponentit kiinteänä toimintona.


### Tehdastiedostojen luominen sulautetulla konfiguraatiolla


Tehdastiedostojen luominen edustaa kehittynyttä käyttöönottostrategiaa, jossa konfigurointiasetukset sisällytetään suoraan laiteohjelmiston binääritiedostoon, jolloin manuaalista konfigurointia ei tarvita laitteen asennuksen aikana. Tämä lähestymistapa on erityisen arvokas laajamittaisissa käyttöönotoissa tai tilanteissa, joissa yhdenmukainen konfigurointi useissa laitteissa on välttämätöntä.


Tehdastiedoston luontiprosessi alkaa luomalla konfiguraatiobinäärin CSV-konfiguraatiotiedostosta ESP-IDF:n NVS-osion generointityökalulla. Tämä työkalu, joka sijaitsee ESP-IDF:n komponenttihakemistossa osoitteessa nvs-flash/nvs-partition-generator, muuntaa ihmisen luettavissa olevan konfiguraation suoraan flash-muistiin tallennettavaksi sopivaan binäärimuotoon. Skripti nvs-partition-gen.py käsittelee config.csv-tiedoston ja luo config.binary-tiedoston, joka kohdistuu 0x6000-muistin osoiteavaruuteen.


Tehdastiedostojen lopullisessa kokoonpanossa käytetään erikoistuneita yhdistämisskriptejä, jotka yhdistävät laiteohjelmiston binääritiedostot konfigurointitietoihin. Arkisto tarjoaa useita yhdistämisvaihtoehtoja, mukaan lukien vakiomuotoinen yhdistämiskomentosarja perustehdastiedostoja varten ja konfiguraation sisältävä yhdistämiskomentosarja kattavia tehdastiedostoja varten. Merge-bin-with-config.sh-skripti luo tehdastiedostot, jotka sisältävät sekä laiteohjelmiston toiminnot että valmiiksi konfiguroidut asetukset, jolloin tuloksena on täydellinen käyttöönottopaketti. Tämä lähestymistapa mahdollistaa laitekohtaisten tehdastiedostojen luomisen, kuten Bitaxe Ultra -laitteille räätälöityjen versioiden, joissa on tietyt piirilevyn versiot, mutta samalla säilytetään joustavuus generate:n yleisten tehdastiedostojen luomiseen ilman upotettuja konfiguraatioita skenaarioita varten, jotka edellyttävät manuaalista asetusten joustavuutta.


Valmiit tehdastiedostot tarjoavat käyttöönottotiimille valmiit flash-binäärit, jotka sisältävät kaikki tarvittavat laiteohjelmistokomponentit ja konfigurointiasetukset, virtaviivaistavat laitteen käyttöönottoprosessia ja varmistavat johdonmukaiset toimintaparametrit kaikissa käyttöönotetuissa mining-laitteissa.


## Miten Bitaxe Web Flasheria käytetään?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

Bitaxe Web Installer on virtaviivaistettu lähestymistapa Bitaxe-laitteiden laiteohjelmistojen hallintaan, ja se tarjoaa käyttäjille useita asennusvaihtoehtoja verkkopohjaisen käyttöliittymän kautta. Tämä kattava työkalu poistaa monimutkaisuuden, joka perinteisesti liittyy laiteohjelmistopäivityksiin ja uusiin asennuksiin, ja tekee laitteiden hallinnasta helppokäyttöistä käyttäjille heidän teknisestä osaamisestaan riippumatta. Tämän asennusohjelman oikean käytön ymmärtäminen on ratkaisevan tärkeää, jotta voidaan ylläpitää laitteen optimaalista suorituskykyä ja välttää yleiset sudenkuopat, jotka voivat tehdä laitteista tilapäisesti toimintakyvyttömiä.


### Pääsy- ja selainyhteensopivuusvaatimukset


Bitaxe Web Installer on käytettävissä erillisen URL-osoitteen [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) kautta (videolla esitetty URL-osoite on nyt poistettu käytöstä), ja se toimii kaikkien laiteohjelmiston asennustoimintojen keskuksena. Tämän verkkopohjaisen työkalun menestyksekäs käyttö edellyttää kuitenkin selainyhteensopivuutta, sillä asennusohjelma perustuu tiettyihin verkkotekniikoihin, joita kaikki selaimet eivät tue. Chrome on ensisijaisesti suositeltava selain asennusohjelmalle, sillä se tarjoaa täyden yhteensopivuuden kaikkien ominaisuuksien ja toimintojen kanssa. Vaikka muut Chromium-pohjaiset selaimet saattavat tarjota samankaltaisia toimintoja, suositut vaihtoehdot, kuten Brave ja Firefox, eivät tarjoa tarvittavaa API-tukea, joten ne eivät ole yhteensopivia asennusohjelman ydintoimintojen kanssa.


Tämä selainrajoitus johtuu siitä, että asennusohjelma käyttää suoraa sarjaliikennettä Bitaxe-laitteiden kanssa web-käyttöliittymän kautta. API, joka mahdollistaa tämän viestinnän, on suhteellisen uusi web-standardi, joka ei ole vielä yleistynyt selaimissa. Käyttäjät, jotka yrittävät käyttää asennusohjelmaa tukemattomilla selaimilla, kohtaavat yhteyshäiriöitä ja eivät pysty kommunikoimaan laitteidensa kanssa, minkä vuoksi heidän on vaihdettava yhteensopivaan selaimeen ennen asennustoimien jatkamista.


### Virtavaatimukset ja laitteen valmistelu


Bitaxe-laitteilla on erilaiset virtavaatimukset niiden mallista ja versiosta riippuen, joten asianmukainen virranhallinta on olennaisen tärkeää laiteohjelmiston asennuksen onnistumisen kannalta. Laitteet, joissa on versio 204 tai sitä nuorempi, voivat toimia pelkästään USB-virran avulla, ja ne ottavat riittävästi virtaa liitetystä tietokoneesta toiminnan ylläpitämiseksi vilkkumisprosessin aikana. Tämä yksinkertaistettu virtajärjestely tekee näistä aikaisemmista versioista erityisen käteviä laiteohjelmistopäivityksiä varten, koska käyttäjien tarvitsee vain liittää yksi USB-kaapeli asennusprosessin aloittamiseksi.


Laitteet, joissa käytetään versiota 205 ja uudempia versioita, vaativat kuitenkin USB-liitännän lisäksi ulkoisia virtalähteitä, mikä heijastaa uudempien laitteistoversioiden virrankulutuksessa ja piirisuunnittelussa tapahtuneita muutoksia. Nämä laitteet eivät voi ottaa riittävästi virtaa pelkästään USB:n kautta, joten ne on liitettävä vakiovirtalähteisiin laiteohjelmiston asennuksen aikana. Jos näille uudemmille laitteille ei anneta riittävästi virtaa, asennus epäonnistuu ja laiteohjelmiston päivitysprosessi saattaa häiriintyä.


Fyysinen kytkentäprosessi edellyttää erityistä ajoitusta ja painikkeiden käsittelyä, jotta voidaan varmistaa asianmukainen viestintä asentajan ja laitteen välillä. Käyttäjien on painettava Bitaxe-laitteen käynnistyspainiketta ja pidettävä sitä painettuna ennen USB-C-kaapelin liittämistä tietokoneeseen. Tämä sekvenssi asettaa laitteen bootloader-tilaan, jolloin asentaja voi kommunikoida suoraan laitteen laiteohjelmistovaraston kanssa. USB-kaapelin liittäminen ennen käynnistyspainikkeen painamista johtaa laitteen normaaliin toimintaan eikä laiteohjelmiston asentamiseen vaadittavaan käynnistyslataustilaan, mikä estää asentajaa muodostamasta tarvittavaa viestintäkanavaa.


### Asennusvaihtoehdot ja niiden sovellukset


Bitaxe Web Installer tarjoaa neljä erilaista asennusvaihtoehtoa, joista jokainen on suunniteltu tiettyihin käyttötapauksiin ja laitekokoonpanoihin. Bitaxe Superboardin versio 4.0.1 on uusin laiteohjelmisto Super-mallin laitteille, ja versio 4.0.2 on tarkoitus julkaista tulevaisuudessa. Tämä vaihtoehto sisältää sekä tehdas- että päivitysvaihtoehdot, mikä tarjoaa joustavuutta asennustavassa käyttäjän tarpeiden ja laitteen tilan mukaan.


Tehdasasasennukset ovat täydellisiä laiteohjelmiston vaihtoja, jotka vastaavat alkuperäistä valmistusprosessia ja sisältävät kattavat itsetestausmenettelyt, joilla varmistetaan laitteen toimivuus kaikissa järjestelmissä. Kun käyttäjät valitsevat tehdasasennuksen, asentaja poistaa olemassa olevan laiteohjelmiston ja konfigurointitiedot kokonaan ja korvaa ne tuoreella, puhtaalla asennuksella, joka on identtinen sen kanssa, mitä käytetään valmistuksen aikana. Prosessi sisältää automaattisen itsetestauksen, joka varmistaa laitteiston asianmukaisen toiminnan ja vaatii käyttäjiä käynnistämään laitteensa uudelleen sen päätyttyä, ennen kuin normaali toiminta voi jatkua. Tehdasasennukset ovat erityisen arvokkaita silloin, kun laitteissa ilmenee jatkuvia ongelmia tai kun käyttäjät haluavat palauttaa laitteensa alkuperäisiin tehdasasetuksiin.


Päivitysasennukset tarjoavat varovaisemman lähestymistavan, jossa säilytetään olemassa olevat konfigurointitiedot ja päivitetään vain keskeiset laiteohjelmistokomponentit. Tämä vaihtoehto on ihanteellinen käyttäjille, jotka ovat mukauttaneet laiteasetuksiaan ja haluavat säilyttää henkilökohtaiset määrityksensä samalla kun he hyötyvät laiteohjelmiston parannuksista ja vikakorjauksista. Päivitysprosessi kohdistuu vain muutosta vaativiin laiteohjelmistokomponentteihin, jolloin käyttäjäkohtaiset asetukset, WiFi-tunnukset ja Bitcoin-osoitteet säilyvät koskemattomina koko asennusprosessin ajan.


### Kriittiset asennuskysymykset ja tietosuoja


Tehdas- ja päivitysasennusten erottaminen toisistaan vaikuttaa merkittävästi laitteen kokoonpanoon ja käyttäjätietojen säilyttämiseen. Tehdasasennukset poistavat laitteen kokonaan, jolloin kaikki käyttäjän määrittämät asetukset, kuten WiFi-tunnukset, Bitcoin-osoitteet ja kaikki henkilökohtaiset laiteparametrit, poistetaan. Tehdasasennuksen jälkeen käyttäjien on yhdistettävä laite uudelleen sen oletusarvoiseen WiFi-verkkoon ja määritettävä kaikki henkilökohtaiset asetukset alusta alkaen, jolloin laitetta kohdellaan käytännössä kuin se olisi tullut valmistajalta aivan uutena.


Päivitysasennukset edellyttävät, että asennuksen aikana esitetty laitteen poistaminen -vaihtoehto otetaan tarkkaan huomioon. Asennusohjelma kysyy käyttäjältä kysymyksen "Haluatko poistaa laitteen ennen Bitaxe Flasherin asentamista?" ja varoittaa, että kaikki laitteen tiedot menetetään. Käyttäjien, jotka suorittavat päivitysasennuksia, on hylättävä tämä vaihtoehto napsauttamalla "Seuraava" sen sijaan, että he vahvistaisivat pyyhkimistoiminnon. Poistovaihtoehdon hyväksyminen päivitysasennuksen aikana poistaa laitteen konfigurointitiedoston, jolloin laite ei mahdollisesti toimi, kunnes asianmukainen konfigurointi on palautettu. Vaikka tämä tilanne ei vahingoita laitetta pysyvästi, se aiheuttaa tarpeettomia hankaluuksia ja vaatii ylimääräisiä konfigurointivaiheita normaalin toiminnan palauttamiseksi.


Itse asennusprosessi etenee automaattisesti, kun käyttäjät ovat tehneet valintansa ja vahvistaneet valintansa. Asennusohjelma huolehtii kaikista laiteohjelmiston siirtoon ja tarkistukseen liittyvistä teknisistä näkökohdista ja tarjoaa edistymisindikaattoreita ja tilapäivityksiä koko prosessin ajan. Tämän automaattisen lähestymistavan ansiosta käyttäjien ei tarvitse ymmärtää monimutkaisia laiteohjelmiston asennusmenettelyjä, ja samalla varmistetaan luotettavat ja yhdenmukaiset tulokset eri laitemalleissa ja laiteohjelmistoversioissa.


## Miten luoda ja tilata PCB?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Tässä luvussa keskitytään valmistustiedostojen tuottamiseen KiCad-projekteista ja ammattimaisten piirilevyjen tilaamiseen verkkovalmistajilta. Käymme Bitaxe-projektia esimerkkinä käyttäen läpi koko työnkulun tiedostojen luomisesta tilauksen tekemiseen piirilevyvalmistajalle.


### PCB-valmistusprosessin ymmärtäminen


Matka valmiista KiCad-suunnittelusta fyysiselle piirilevylle sisältää useita kriittisiä vaiheita, jotka kurovat umpeen digitaalisen suunnittelun ja fyysisen valmistuksen välisen kuilun. Kun työskentelet Bitaxen kaltaisten monimutkaisten projektien parissa, KiCadin piirilevyeditori tarjoaa kattavan näkymän suunnittelustasi ja näyttää kaikki komponentit ja niiden keskinäiset yhteydet värillisten jälkien avulla. Näkyvät punaiset ja siniset viivat kuvaavat piirilevyn eri integroitujen piirien ja komponenttien välisiä sähköisiä yhteyksiä. KiCadin 3D-katseluominaisuuden avulla voit visualisoida, miltä lopullinen koottu piirilevy näyttää, ja saada arvokasta tietoa komponenttien sijoittelusta ja mahdollisista mekaanisista ristiriidoista.


Valmistusprosessi edellyttää erityisiä tiedostomuotoja, joita PCB-valmistajat voivat tulkita ja käyttää levyjen valmistamiseen. Nämä tiedostot sisältävät tarkat tiedot kuparikerroksista, porausrei'istä, komponenttien sijoittelusta ja muista valmistusmäärittelyistä. Tämän työnkulun ymmärtäminen on olennaista riippumatta siitä, työskenteletkö Bitaxen vakiosuunnittelun kanssa vai teetkö muutoksia, kuten lisäät mukautettuja logoja, muutat komponenttien arvoja tai mukautat piirilevyn asettelua vastaamaan erityisvaatimuksia.


### Gerber-tiedostojen luominen valmistusta varten


Gerber-tiedostot ovat alan standardi PCB-suunnittelutietojen välittämiseen valmistajille. Nämä tiedostot sisältävät kaikki tarvittavat tiedot PCB:n valmistukseen, mukaan lukien kuparikerroskuviot, juotosmaskin määritelmät ja porausreikien sijainnit. Jos haluat generate nämä tiedostot KiCadissa, siirry PCB-editoriin ja siirry valmistuslähtöihin Tiedostot-valikon kautta. Ohjelmisto määrittää automaattisesti asianmukaiset asetukset tavanomaisia valmistusprosesseja varten, mukaan lukien oikea ulostulojen hakemistorakenne, joka on yleensä järjestetty nimellä "valmistustiedostot/gerberit"


Generointiprosessi luo useita Gerber-tiedostoja, joista kukin edustaa PCB-suunnittelun eri näkökohtia. Nämä tiedostot toimivat yhdessä, jotta valmistajat saavat täydelliset valmistusohjeet. Kun tiedostot on luotu, ne on pakattava ZIP-arkistoon, sillä tämä on useimpien piirilevyvalmistajien odottama vakiomuoto. ZIP-tiedosto sisältää kaikki tarvittavat valmistustiedot ja varmistaa, että tiedostoja ei menetetä tai vahingoiteta valmistajan verkkosivustolle lataamisen aikana.


On syytä huomata, että monet avoimen lähdekoodin projektit, kuten Bitaxe, sisältävät usein valmiiksi luotuja valmistustiedostoja arkistoissaan. On kuitenkin ratkaisevan tärkeää ymmärtää, miten generate näitä tiedostoja voi käyttää itse, kun tehdään suunnittelumuutoksia tai työskennellään eri piirilevyversioiden kanssa. Tämä osaaminen on erityisen arvokasta, kun mukautetaan malleja tai ratkaistaan valmistusongelmia.


### PCB-valmistajien valinta ja vaihtoehtojen ymmärtäminen


PCB-valmistusympäristö tarjoaa useita hyvämaineisia vaihtoehtoja, ja JLCPCB ja PCBWay ovat suosituimpia valintoja sekä harrastajien että ammattilaisten keskuudessa. Molemmat valmistajat tarjoavat samanlaisia palveluja kilpailukykyisellä hinnoittelulla ja luotettavalla laadulla, vaikka kummallakin on erityisiä etuja projektisi vaatimuksista riippuen. JLCPCB houkuttelee usein ensikäyttäjiä tarjoushinnoittelulla ja käyttäjäystävällisillä käyttöliittymillä, kun taas PCBWay voi tarjota erilaisia materiaalivaihtoehtoja tai erikoistuneita palveluja.


Kun lataat Gerber-tiedostot valmistajan verkkosivustolle, järjestelmä analysoi automaattisesti suunnittelusi ja esittää erilaisia valmistusvaihtoehtoja. Näiden alustojen tarjoamat oletusasetukset sopivat yleensä useimmille vakiomalleille, ja on yleensä suositeltavaa säilyttää nämä asetukset, ellei sinulla ole erityisiä vaatimuksia. Tärkeimpiä parametreja ovat piirilevyn paksuus, kuparin paino, pintakäsittely ja vähimmäismäärät. Useimmat valmistajat vaativat viiden piirilevyn vähimmäistilauksia, mikä toimii itse asiassa hyvin harrastelijaprojekteissa, joissa varalevyjen pitäminen tai jakaminen ystävien kanssa on hyödyllistä.


Värivaihtoehdot ovat yksi harvoista esteettisistä vaihtoehdoista, jotka ovat käytettävissä valmistusprosessin aikana. Vaikka vihreä on edelleen perinteinen ja kustannustehokkain vaihtoehto, valmistajat tarjoavat yleensä myös sinisiä, punaisia, keltaisia, violetteja ja mustia vaihtoehtoja. Värivalinta on puhtaasti esteettinen eikä vaikuta piirilevyn sähköiseen suorituskykyyn, vaikka joillakin väreillä voi olla pieniä kustannusvaikutuksia tai pidempiä valmistusaikoja.


### Kehittyneeseen valmistukseen liittyvät näkökohdat ja kokoonpanovaihtoehdot


Peruspiirilevyjen valmistuksen lisäksi nykyaikaiset valmistajat tarjoavat lisäpalveluita, jotka voivat virtaviivaistaa projektin loppuunsaattamista merkittävästi. Stencilit ovat yksi arvokkaimmista lisäpalveluista, erityisesti kun on kyse suunnitelmista, joissa on hienojakoisia komponentteja, kuten Bitcoin mining -projekteissa käytetyt ASIC-sirut. Sablooni on pohjimmiltaan tarkkaan leikattu alumiinimalli, jonka aukot vastaavat täsmälleen piirilevyn juotosalustojen paikkoja. Tämä työkalu mahdollistaa juotospastan johdonmukaisen ja tarkan levityksen, mikä parantaa huomattavasti kokoonpanon laatua ja vähentää juotosvirheiden todennäköisyyttä.


Stencil-vaihtoehtoja ovat yleensä yksittäiset stensiilit, joissa on sekä ylä- että alakuvio, tai erilliset stensiilit levyn kummallekin puolelle. Useimmissa projekteissa yhdistetty sablooni on kätevämpi ja kustannustehokkaampi. Sabluunan paksuus lasketaan huolellisesti, jotta juotospastan määrä on sopiva komponenttityyppejä ja tyynyjen kokoja varten. Sabluunan käyttö muuttaa työlästä ja virhealtista manuaalista prosessia nopeaksi ja ammattimaiseksi kokoonpanovaiheeksi.


Vaikka jotkut valmistajat tarjoavat osittaisia tai täydellisiä kokoonpanopalveluja, nämä vaihtoehdot vaativat huolellista harkintaa Bitaxen kaltaisissa monimutkaisissa projekteissa. Päätöksessä on otettava huomioon komponenttien saatavuus, kustannusvaikutukset ja itsekokoonpanon opettavainen arvo. Monia Bitcoin mining -hankkeissa tarvittavia erikoiskomponentteja ei välttämättä ole helposti saatavilla tavallisista piirilevykokoonpanopalveluista, jolloin komponenttien hankinta ja manuaalinen kokoonpano ovat käytännöllisempi lähestymistapa. Tämän sarjan tulevissa jaksoissa käsitellään komponenttien hankintastrategioita ja kokoonpanotekniikoita, joiden avulla saat Bitaxe-projektisi onnistuneesti valmiiksi paljaasta piirilevystä toimivaan laitteeseen.


Valmistus- ja kokoonpanoprosessi on ratkaiseva silta digitaalisen suunnittelun ja fyysisen toteutuksen välillä. Näiden työnkulkujen ymmärtäminen antaa sinulle mahdollisuuden hallita projektejasi, vähentää kustannuksia ja saada arvokasta käytännön kokemusta ammattimaisista valmistusprosesseista. Näiden taitojen hallitseminen avaa uusia mahdollisuuksia elektroniikkasuunnitelmiesi toteuttamiseen, olipa kyseessä sitten yksittäisen prototyypin rakentaminen tai pienen tuotantoerän suunnittelu.


# Suorituskyvyn optimointi

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Bitaxen vertailuarviointi

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

Optimaalisen mining-suorituskyvyn tavoittelu edellyttää järjestelmällistä lähestymistapaa laitteiston konfigurointiin, jossa hashrate, tehokkuus ja lämmönhallinta ovat tasapainossa. Bitaxe tarjoaa lukuisia konfigurointiparametreja, jotka voivat vaikuttaa merkittävästi suorituskykyyn, mutta jokaisen asetusyhdistelmän testaaminen manuaalisesti olisi epäkäytännöllistä ja aikaa vievää. Tässä luvussa tarkastellaan, miten automatisoituja vertailuanalyysityökaluja voidaan hyödyntää Bitaxen suorituskyvyn tieteelliseen optimointiin turvalliset käyttöolosuhteet säilyttäen.


### Bitaxen suorituskykymittareiden ymmärtäminen ja perustason määritys


Ennen optimointitekniikoihin paneutumista on tärkeää ymmärtää keskeiset suorituskykyindikaattorit, jotka määrittelevät Bitaxen toiminnan tehokkuuden. Ensisijaisia mittareita ovat hashrate terahashina sekunnissa mitattuna, tehotehokkuus jouleina terahashia kohti, ASIC taajuus megahertseinä ja ydinjännite voltteina. Hyvin konfiguroitu Bitaxe saattaa saavuttaa noin 1,1 terahashin tehon, jonka hyötysuhde on noin 17 joulea terahashia kohti, ja se toimii 550 megahertsin taajuudella, kun mitattu ASIC-jännite on 1,14 volttia. Nämä perusluvut tarjoavat vertailupisteen, jonka avulla voidaan ymmärtää systemaattisen optimoinnin avulla saatavissa olevat mahdolliset parannukset.


Näiden mittareiden välinen suhde on monimutkainen ja riippuvainen toisistaan. Korkeammat taajuudet lisäävät tyypillisesti hashrate:ta, mutta lisäävät myös virrankulutusta ja lämmöntuotantoa. Vastaavasti jännitesäädöt vaikuttavat sekä suorituskykyyn että lämpöominaisuuksiin. Haasteena on löytää optimaalinen tasapaino, joka maksimoi joko hashrate:n tai hyötysuhteen ja säilyttää samalla vakaan toiminnan turvallisten lämpötilarajojen sisällä. Tämä optimointiprosessi edellyttää metodista testausta useilla parametriyhdistelmillä, minkä vuoksi automatisoidut työkalut ovat korvaamattomia optimaalisten tulosten saavuttamiseksi.


### Bitaxe Hashrate -vertailutyökalun arkkitehtuuri


[Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) -työkalu edustaa kehittynyttä Python-pohjaista ratkaisua, jonka WhiteCookie on alun perin kehittänyt ja jota mrv777 on sittemmin parantanut. Tämä avoimen lähdekoodin työkalu, jota jaetaan GPLv3-lisenssillä, automatisoi monimutkaisen prosessin, jossa testataan useita konfiguraatioyhdistelmiä, jotta voidaan tunnistaa optimaaliset asetukset tietylle laitteistolle. Työkalun ensisijainen vahvuus on sen systemaattinen lähestymistapa parametrien testaamiseen, jossa taajuus- ja jänniteasetuksia säädetään asteittain samalla kun suorituskykymittareita ja lämpöolosuhteita seurataan jatkuvasti.


Vertailuanalyysiprosessi kestää tyypillisesti 30-40 minuuttia, ja sen aikana työkalu testaa menetelmällisesti erilaisia ASIC-taajuus- ja jänniteasetusten yhdistelmiä. Työkalu aloittaa konservatiivisilla perusasetuksilla, jotka ovat tyypillisesti 1,15 volttia ja 500 megahertsiä, ja lisää sitten asteittain näitä parametreja samalla kun hashrate:tä, lämpötilaa ja vakautta seurataan. Tärkeää on, että työkalu asettaa turvallisen toiminnan maksimisuorituskyvyn edelle ja vähentää automaattisesti asetuksia, jotka aiheuttavat liiallista lämmöntuotantoa tai epävakautta. Tämä konservatiivinen lähestymistapa varmistaa, että optimointiprosessi ei vaaranna laitteiston pitkäikäisyyttä tai luotettavuutta.


### Asennus- ja asennusvaatimukset


Bitaxe Hashrate Benchmark -työkalun käyttöönotto edellyttää useita ohjelmistokomponentteja paikallisella tietokoneella. Ensisijaisia vaatimuksia ovat Python vertailuarvoskriptien suorittamista varten, Git arkiston hallintaa varten ja valinnaisesti Visual Studio Code laajennettuja kehitysympäristöominaisuuksia varten. Vaikka työkalua voidaan käyttää komentoriviliitännöistä, VS Code -ohjelman kaltaisen integroidun kehitysympäristön käyttö antaa paremman näkyvyyden vertailuanalyysiprosessiin ja tulosten analysointiin.


Asennusprosessi noudattaa tavanomaisia Python-kehityskäytäntöjä, ja se aloitetaan kloonaamalla arkisto GitHubista paikalliselle koneellesi. Kun arkisto on ladattu, sinun on luotava virtuaaliympäristö, jotta voit eristää työkalun riippuvuudet järjestelmäsi Python-asennuksesta. Tämä eristäminen estää mahdolliset ristiriidat muiden Python-sovellusten kanssa ja varmistaa johdonmukaisen toiminnan. Kun olet aktivoinut virtuaaliympäristön, asennat tarvittavat riippuvuudet käyttämällä mukana toimitettua vaatimustiedostoa, joka määrittää automaattisesti kaikki työkalun asianmukaista toimintaa varten tarvittavat kirjastot ja moduulit.


### Vertailuarvojen suorittaminen ja tulosten tulkinta


Vertailun suorittaminen edellyttää yhden Python-komennon suorittamista, joka sisältää Bitaxen IP-osoitteen parametrina. Työkalu muodostaa automaattisesti yhteyden louhintalaitteesi verkkokäyttöliittymään ja aloittaa järjestelmällisen testausprosessin. Suorittamisen aikana työkalu antaa yksityiskohtaisia lokitietoja, joista näkyvät nykyinen testin iteraatio, käytetyt jännite- ja taajuusasetukset, tuloksena saatu hashrate, tulojännite, lämpötilalukemat ja kriittisten komponenttien, kuten buck-muuntimen, lämpötiedot. Tämän reaaliaikaisen palautteen avulla voit seurata vertailuanalyysin edistymistä ja ymmärtää, miten eri asetukset vaikuttavat louhintalaitteesi suorituskykyyn.


Työkalun älykäs lämmönhallinta tulee esiin, kun lämpötila lähestyy 66 celsiusasteen turvarajaa. Sen sijaan, että se ylittäisi turvalliset toimintarajat, vertailulaboratorio vähentää automaattisesti asetuksia lämpövakauden säilyttämiseksi. Tämä konservatiivinen lähestymistapa varmistaa, että optimointiprosessi asettaa laitteiston pitkän aikavälin luotettavuuden lyhytaikaisen suorituskyvyn kasvun edelle. Työkalu tuottaa lopuksi kattavat tulokset JSON-muodossa ja asettaa viisi parasta konfiguraatiota paremmuusjärjestykseen sekä hashrate:n maksimimäärän että optimaalisen tehokkuuden suhteen. Tulokset antavat selkeät ohjeet, joiden avulla voit valita konfiguraation, joka vastaa parhaiten toiminnallisia prioriteettejasi, olipa kyse sitten maksimitehosta tai energiatehokkuudesta.


Benchmarking-työkalu tarjoaa myös mukautusvaihtoehtoja edistyneille käyttäjille, jotka haluavat muokata testausparametreja. Komentoriviargumenttien avulla voit määrittää mukautettuja aloitusjännitteitä ja -taajuuksia, mikä mahdollistaa kohdennetumman optimoinnin tiettyihin käyttötapauksiin. Jos esimerkiksi tiedät jo, että laitteistosi toimii hyvin korkeammilla taajuuksilla, voit aloittaa vertailuanalyysin korkeammilla asetuksilla sen sijaan, että aloittaisit konservatiivisista oletusasetuksista. Tämä joustavuus tekee työkalusta arvokkaan sekä aloitteleville käyttäjille, jotka etsivät automaattista optimointia, että kokeneille louhijoille, jotka haluavat hienosäätää tiettyjä suorituskykyominaisuuksia.


## Ylikellota Bitaxe

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

Bitaxe-laitteen ylikellottaminen edellyttää sekä laitteiston rajoitusten että jäähdytysvaatimusten huolellista huomioon ottamista. Vaikka monet käyttäjät haluavat alikellottaa laitteensa hiljaisemman toiminnan vuoksi, asianmukaisten ylikellotustekniikoiden ymmärtäminen on tärkeää niille, jotka haluavat maksimaalista suorituskykyä vahingoittamatta laitteistoaan. Prosessi edellyttää taajuuden nostamista ja mahdollisesti jänniteasetusten säätämistä tehdasasetuksia suuremmiksi, mikä luonnostaan lisää lämmönmuodostusta ja komponenttien rasitusta.


Onnistuneen ylikellotuksen perusta on riittävä jäähdytysinfrastruktuuri. Ennen kuin yrität tehdä taajuusmuutoksia, sinun on varmistettava, että Bitaxellasi on asianmukaiset lämmönpoistokyvyt. Laadukkaalla jäähdytyslevyllä ja tuulettimella varustettu Bitaxe Gamma tarjoaa turvalliseen ylikellottamiseen tarvittavan lämmönhallinnan. Laitteita, joissa on pienet jäähdytyslevyt ja riittämättömät tuulettimet, ei pitäisi ylikellottaa, sillä huono jäähdytysteho johtaa lämpökuristukseen ja mahdollisiin laitteistovaurioihin. Lämmön ja komponenttien pitkäikäisyyden välinen suhde on tärkeä ymmärtää - liiallinen lämpö aiheuttaa stressiä, joka heikentää elektroniikkakomponentteja ajan mittaan, mikä lyhentää merkittävästi laitteesi käyttöikää.


### Strateginen jäähdytyselementin sijoittelu


Kriittisin lisäjäähdytystä vaativa komponentti on buck-muunnin, pieni musta komponentti, joka sijaitsee Bitaxen takapuolella lähellä suurta kelaa. Tämä laite muuntaa tulevan 5 voltin virransyötön ASIC-sirulle sopivaksi jännitteeksi, joka on yleensä noin 1,2 V. Buck-muunnin, johon usein viitataan myös nimellä TPS, tuottaa toiminnassa huomattavaa lämpöä ja muodostaa lämpökaulan, joka rajoittaa ylikellotusmahdollisuuksia. Pienen liimattavan jäähdytyselementin asentaminen tähän komponenttiin ei ainoastaan mahdollista suurempaa ylikellotusvaraa, vaan myös parantaa yleistä tehokkuutta vähentämällä lämpöhäviöitä.


Lisäjäähdytyselementtien sijoittelusta voi olla hyötyä levyn muille suurivirtaisille alueille. Jännitteensäätöpiiriin kohdistuu huomattavaa sähköistä rasitusta, kun virta virtaa tulo-osasta eri johtojen kautta alaspäin piirilevyn eri johtojen kautta ASIC-sirun syöttämiseksi. Monet kokeneet ylikellottajat asentavat jäähdytyslevyjä Bitaxen etupuolelle näille suurivirtaisille alueille parantaakseen lämmönhukkaa entisestään. Vaikka nämä lisäjäähdytystoimenpiteet eivät ole varsinaisesti välttämättömiä maltillisessa ylikellotuksessa, niistä tulee tärkeitä, kun taajuuksia nostetaan äärimmäisille tasoille.


### Jäähdytysjärjestelmän näkökohdat ja rajoitukset


ESP32-ohjain, joka näkyy hopeanvärisenä komponenttina piirilevyssä, ei yleensä tarvitse lisäjäähdytystä. Tämä komponentti tuottaa itsenäisesti vain vähän lämpöä, ja se lämpenee vain ympäröivien komponenttien lämmönsiirron vuoksi. Jäähdytyselementtien asentaminen ESP32:n lähelle voi mahdollisesti häiritä viereistä Wi-Fi-antennia, mikä heikentää langatonta yhteyttä ja signaalin laatua. Keskitä jäähdytystoimet tehonsäätökomponentteihin ja ASIC-alueeseen ohjauspiirin sijaan.


Kahden tuulettimen kokoonpanot tarjoavat sekä mahdollisuuksia että rajoituksia. Vaikka toisen tuulettimen lisääminen puhaltamaan ilmaa Bitaxen takaosaan voi parantaa jäähdytystehoa, laitteen laiteohjelmisto voi ohjata vain yhtä tuuletinta kunnolla. Bitaxessa on kaksi tuuletinliitäntää mutta vain yksi tuuletinohjain, joten kahden tuulettimen liittäminen sekoittaa laiteohjelmiston, kun se saa ristiriitaisia kierrosnopeussignaaleja. Tämä konfiguraatio toimii, mutta se voi johtaa arvaamattomaan tuulettimen ohjauskäyttäytymiseen.


### Suorituskyvyn perusarviointi


Ennen kuin yrität tehdä ylikellotusmuutoksia, määritä suorituskyvyn perusarvot ajamalla Bitaxea perusasetuksilla useita tunteja. Seuraa ASIC:n lämpötilaa, jännitteensäätimen lämpötilaa ja tuulettimen nopeusprosenttia verkkokäyttöliittymän kautta. Optimaalisen käyttölämpötilan tulisi pitää ASIC:n lämpötila alle 60 °C:n ja jännitteensäätimen lämpötila alle 60 °C:n normaaliolosuhteissa. Jos laitteesi toimii jo yli 65 °C:n lämpötilassa ASIC:n osalta tai 70-80 °C:n lämpötilassa jännitteensäätimen osalta tehdasasetuksilla, lisäjäähdytyslaitteisto on pakollinen ennen ylikellottamisen aloittamista.


Järjestelmällinen lähestymistapa taajuuden lisäämiseen sisältää vaiheittaisia vaiheita käyttämällä asetusvalikon ennalta määritettyjä taajuusvaihtoehtoja. Aloita valitsemalla seuraava käytettävissä oleva taajuusaskel nykyistä asetusta korkeammalla tasolla säilyttäen samalla oletusarvoisen ydinjännitteen. Tämän konservatiivisen lähestymistavan avulla voit arvioida lämpö- ja vakausvaikutukset ennen lisämuutosten tekemistä. Anna laitteen toimia kullakin uudella taajuusasetuksella vähintään 30 minuutista yhteen tuntiin ja tarkkaile lämpötilakehitystä ja hash-nopeuden vakautta koko arviointijakson ajan.


### Kehittynyt mukautettu konfigurointi


Mukautettujen taajuus- ja jänniteasetusten käyttäminen edellyttää kehittyneen ylikellotuksen käyttöliittymän käyttöönottoa lisäämällä "?OC" laitteen web-käyttöliittymän URL-osoitteeseen. Tämä avaa manuaaliset syöttökentät tarkkaa taajuuden ja jännitteen säätöä varten, ja lisäksi annetaan asianmukaiset varoitukset suunniteltujen parametrien ulkopuolisen käytön riskeistä. Mukautettu käyttöliittymä mahdollistaa hienosäädön vakiotaajuusvaiheita pidemmälle, jolloin kokeneet käyttäjät voivat optimoida suorituskyvyn omille jäähdytyskokoonpanoilleen.


Kun käytät mukautettuja asetuksia, säilytä konservatiivinen 10-15 MHz:n suuruinen askelarvo säätövaihetta kohti. Tämä metodinen lähestymistapa estää äkilliset lämpöpiikit ja mahdollistaa asianmukaisen vakaustestauksen kullakin taajuusalueella. Jotkut edistyneet käyttäjät saavuttavat noin 700 MHz:n taajuuksia 1,175 V:n tai vastaaviin arvoihin säädetyillä ydinjännitteillä, mutta nämä ääriasetukset edellyttävät laajoja jäähdytysmuutoksia ja huolellista seurantaa. Jännitteensäädin voi toimia jopa 100 °C:n lämpötiloissa ilman välitöntä vaurioitumista, mutta korkeammat lämpötilat heikentävät tehokkuutta ja pitkän aikavälin luotettavuutta. Onnistunut ylikellotus vaatii kärsivällisyyttä, järjestelmällistä testausta ja jatkuvaa seurantaa, jotta saavutetaan vakaita suorituskyvyn parannuksia laitteiston eheyden säilyttäen.


# Viimeinen jakso

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Arvioi tätä kurssia

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Päätelmä

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>