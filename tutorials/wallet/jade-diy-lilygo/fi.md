---
name: Jade DIY
description: Käännä 15 dollarin dev board täysin toimivaksi Bitcoin-laitteistoksi wallet:ksi
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Aloittelijan rakentaminen


**Audience:** Uteliaat rakentajat, joilla on vain vähän tai ei lainkaan kokemusta sulautetuista järjestelmistä.


**Kesto:** 2 tuntia (joustavasti)


**Tulokset:** Opiskelijat oppivat loppuun mennessä:



- Tunnista kotitekoisten laitteistolompakoiden ja kaupallisten laitteiden turvallisuusmalli.
- Kokoa mikrokontrolleripohjainen allekirjoitusväline.
- Flashaa avoimen lähdekoodin laiteohjelmisto ja tarkista rakennuksen tarkistussumma.
- Allekirjoita ja lähetä mainnet-tapahtuma uudella laitteellaan.


---

## Abstrakti


Tässä 2-tuntisessa työpajassa aloittelijoille opetetaan rakentamaan toimiva Bitcoin-laitteisto wallet vilkkumalla avoimen lähdekoodin Jade-firmwarea 15 dollarin hintaiselle LilyGO T-Display -levylle. Opiskelijat tekevät yleisestä kehityslaitteistosta 150 dollaria maksaviin kaupallisiin lompakoihin verrattavissa olevan allekirjoituslaitteen ja oppivat tietoturvan perusteita käytännön kokemuksen eikä pelkän teorian avulla.


### Filosofia


Oman allekirjoituslaitteen rakentamisessa ei ole kyse vain rahan säästämisestä, vaan myös Bitcoin:ää suojaavan teknologian ymmärtämisestä. Tässä työpajassa "turvallisuus ymmärryksen kautta" on tärkeämpää kuin mustan laatikon luottamus. Hankkimalla komponentteja, vilkuttamalla avoimen lähdekoodin laiteohjelmistoa ja tuottamalla itse entropiaa opiskelijat vähentävät toimitusketjun riskejä ja oppivat samalla arvioimaan turvallisuusväitteitä kriittisesti. Tavoitteena on tietoon perustuva itsenäisyys: oppilaiden pitäisi ymmärtää sekä oman laitteen teho että sen rajoitukset verrattuna kaupallisiin vaihtoehtoihin.


---

## Konseptin pohjustus (15 min)


### Mitä on omaishuoltajuus ja miksi sillä on merkitystä?


Bitcoin luotiin poistamaan luotettavien kolmansien osapuolten, kuten pankkien ja yritysten, tarve rahajärjestelmästämme. Luottamuksen sijaan bitcoin käyttää matematiikkaa, fysiikkaa ja kryptografiaa, jotta kuka tahansa voi omistaa ja hallita rahojaan tarvitsematta kenenkään lupaa.


Tämä toimii siten, että bitcoin on olemassa maailmanlaajuisessa digitaalisessa pääkirjassa, jota kutsutaan lohkoketjuksi eli bitcoin timechainiksi, joka on julkinen ja läpinäkyvä tietokoneiden ylläpitämä pääkirja, eikä keskitetty pääkirja kuten pankkitili.


Tärkeää on ymmärtää, että bitcoinien siirtäminen paikasta toiseen edellyttää, että transaktio allekirjoitetaan niin sanotulla yksityisellä avaimella. Ajattele sitä ikään kuin avaisit holvin salasanalla ja siirtäisit bitcoinit jonkun toisen holviin. Bitcoin antaa sinulle valtuudet pitää holvin avaimet hallussasi itse sen sijaan, että luotat pankin siirtävän rahasi puolestasi.


Suuren vallan myötä tulee suuri vastuu, jos kadotat avaimesi, varasi ovat poissa ikuisesti. Voit siis ajatella, että holvin avaimet ovat itse rahaa. Vaikka avaimet eivät ole sama asia kuin bitcoinit, ne ovat mekanismi, jonka avulla varoja siirretään, ja siksi niiden suojaaminen on äärimmäisen tärkeää. Siksi sanomme "ei avaimia, ei kolikoita".


Termi "itsesäilytys" saattaa kuulostaa hämmentävältä, mutta se tarkoittaa vain omien yksityisten avainten hallussapitoa ja omien bitcoinien hallintaa. Jos sinulla ei ole kyseistä avainta, luotat siihen, että joku muu pitää sitä puolestasi. Jos bitcoinisi on ETF:ssä tai pörssissä (Mt. Gox, FTX, Coinbase, Binance jne.), et omista bitcoinia, vaan omistat vaatimuksen bitcoiniin. Tämä tuo mukanaan kaikenlaisia riskejä, kuten pörssien hakkerointi ja bitcoinisi menettäminen tai yritykset, jotka lainaavat rahojasi ja antavat sinulle vain murto-osan varoiksi. Lisäksi luotettavat kolmannet osapuolet voisivat täysin hallita rahojasi ja rajoittaa tai jäädyttää kotiutukset.


![image](assets/fr/01.webp)


Omahuoltajuus poistaa luottamuksen yhtälöstä. Kukaan ei voi jäädyttää rahojasi tai kieltää maksutapahtumaa, voit lähettää rahaa rajojen yli, kenelle tahansa, milloin tahansa, etkä tarvitse pankkitiliä, henkilöllisyystodistusta tai kenenkään hyväksyntää. Kukaan ei voi pysäyttää, sensuroida tai varastaa sinua, mikä vapauttaa bitcoinin täyden voiman vapausrahana. Siksi sanomme, että bitcoinilla voit olla oma pankkisi.


Bitcoin luotiin ratkaisemaan luottamuksen ja rahan manipulointia koskeva ongelma, opt-out nykyisestä järjestelmästämme, mutta exit toimii vain, jos otat avaimet. Tämän vuoksi omahuoltajuus on niin tärkeää.


### Mikä on Wallet?


Termi wallet on hieman harhaanjohtava nimitys, ja siksi se voi olla sekava. On totta, että bitcoin wallet, kuten fyysinen wallet, tallentaa arvoa. Tärkein ero on kuitenkin se, että bitcoin-lompakot eivät itse asiassa säilytä bitcoineja.


Bitcoin on olemassa vain kirjauksena julkisessa lohkoketjussa tai kyberavaruuden metaforisissa holveissa. Muista, että bitcoinien siirtämiseksi sinun on käytettävä avaimiasi avataksesi holvin ja siirtääksesi kolikot jonnekin muualle, yksityiset avaimet ovat niitä, joita käytetään bitcoinien kuluttamiseen. Kun teet transaktion wallet:lläsi, käytät oikeastaan vain avaimiasi transaktion allekirjoittamiseen. Näin todistat, että omistat rahat ja sinulla on oikeus käyttää kolikoita.


Bitcoin-lompakot oikeastaan vain säilyttävät yksityisiä avaimia, joten olisi oikeampaa kutsua niitä avainketjuiksi.


### Hot vs. Cold Lompakot


Hot wallet on ohjelmistosovellus puhelimessa tai tietokoneessa. Se on yhteydessä internetiin, joten sen käyttö on helpompaa ja maksutapahtumien allekirjoittaminen nopeampaa, mutta tämä tarkoittaa myös sitä, että se on alttiimpi hakkereille, haittaohjelmille ja tietojenkalastelulle. Sitä kutsutaan "kuumaksi", koska se on liitetty internetiin, kytketty verkkoon ja kytketty päälle. Esimerkkinä voidaan mainita puhelin wallet tai selain wallet.


Kylmä wallet eli laitteisto-wallet on laite, joka luo ja tallentaa avaimesi offline-tilassa. Tämä poistaa jonkun mahdollisuuden murtautua varoihisi ja on paljon turvallisempi pitkän aikavälin säästöjen kannalta, mutta se on laite, jota tarvitaan jokaisen tapahtuman allekirjoittamiseen, ja se voi olla vähemmän kätevä.


### Hardware Wallet uhkamalli


Laitteistolompakoiden tarkoituksena on ratkaista perustavanlaatuinen ongelma: miten voit allekirjoittaa Bitcoin-tapahtumia paljastamatta yksityisiä avaimiasi internetiin liitetylle tietokoneelle, johon haittaohjelmat tai etähyökkääjät voivat päästä käsiksi? Keskeisessä uhkamallissa oletetaan, että jokapäiväinen kannettava tietokone tai puhelin on mahdollisesti vihamielinen. wallet-laitteisto luo eristetyn ympäristön, jossa yksityiset avaimet eivät koskaan poistu laitteesta, ja tapahtumien allekirjoittaminen tapahtuu secure element:ssä tai mikrokontrollerissa, joka välittää isäntätietokoneelle vain allekirjoituksen, ei itse avainta. Vaikka tietokoneesi olisi täysin vaarassa, hyökkääjä ei voi varastaa Bitcoin:ta ilman fyysistä pääsyä laitteeseen ja PIN-koodiin.


Laitteistolompakot tuovat kuitenkin omat uhkansa. Sinun on luotettava siihen, että valmistaja ei ole ottanut käyttöön takaovia, että toimitusketjuun ei ole puututtu ja että satunnaislukujen generointi on todella satunnaista. Fyysiset hyökkääjät voivat poimia avaimia sivukanavahyökkäysten tai sirun manipuloinnin avulla, ja joku, jolla on tilapäinen pääsy, voi muokata laitettasi. Oman wallet-laitteiston rakentaminen auttaa sinua ymmärtämään näitä kompromisseja - teet päätöksiä suojatuista elementeistä verrattuna yleiskäyttöisiin mikrokontrollereihin, miten tapahtumat todennetaan näytöllä ja miten suojaudut sekä etä- että fyysisiltä uhkilta. Tavoitteena ei ole täydellinen turvallisuus, vaan sen ymmärtäminen, miltä uhilta suojaudut ja mitkä uhat ovat jäljellä.


### Keskeiset käsitteet



- Entropia ja seed-lauseet:** wallet on vain niin turvallinen kuin sen synnyttämä satunnaisuus. Sekoitamme laitteen satunnaislukugeneraattorin ihmisystävällisiin temppuihin, kuten nopanheittoon, muunnamme tuon entropian 12- tai 24-sanaiseksi [BIP39-lauseeksi](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) ja poistumme huoneesta kirjallisen tai metallisen varmuuskopion kanssa, johon luotat.
- Siemenlauseen hygienia:** Kohtele seed:ää kuin säästöjesi yleisavaimia. Älä koskaan kirjoita sanoja puhelimeen tai tietokoneeseen - keyloggerit, kuvakaappaukset ja pilvivarmistukset voivat vuotaa ne ikuisesti. Pidä lause offline-tilassa, säilytä sitä jossakin, mihin vain sinä pääset käsiksi, ja harjoittele sen lukemista ääneen ennen lähtöäsi.
- Turvallinen elementti + mikrokontrolleri:** Ajattele secure element:a holvina ja mikrokontrolleria aivoina. secure element vartioi yksityisiä avaimia peukaloinninestolla, kun taas mikrokontrolleri hoitaa näytön, painikkeet ja laiteohjelmiston logiikan. Huomaa, että nykyisin rakentamissamme laitteistolompakoissa ei ole secure element:aa. Tämä ei tarkoita sitä, että se olisi turvaton, mutta siinä on vain yksi suojaustaso vähemmän.
- Luottaminen laiteohjelmaan:** Laiteohjelma on wallet:n näkymätön käyttöjärjestelmä. Lataa aina merkittyjä julkaisuja, tarkista julkaistu hash ja ymmärrä, että toistettavat versiot antavat useiden ihmisten kääntää saman koodin ja saada täsmälleen saman binäärin. Jos tarkistussumma ei täsmää, et allekirjoita.


---

## Mitä me rakennamme?


Käytämme yleistä laitteistoa, LilyGo T-Display -näyttöä, ja vilautamme siihen Jade SDK -firmwarea. [Jade Plus](https://blockstream.com/jade/jade-plus/) on avoimen lähdekoodin wallet, joka yleensä maksaa 150 dollaria:


![image](assets/fr/02.webp)


Tänään vilautamme heidän laiteohjelmistonsa 15 dollarin laitteistoon.


### Mitä ostaa


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB ja kuori, malli K164)** - [Tilaa suoraan LilyGO:lta](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) noin 15 dollarilla. Tämä ESP32-levy tarjoaa näytön, painikkeet ja USB-liitännän, jotka heijastavat Blockstreamin Jade Plus -järjestelmää. ESP32:ssa on myös Wi-Fi- ja Bluetooth-radiot; toimitamme laiteohjelmiston, joka pitää ne poissa käytöstä, mutta ne muokkaavat uhkamalliasi, koska haitallinen koodi voi kytkeä ne takaisin päälle.
- USB-C-kaapeli** - Ota mukaan datakäyttöön soveltuva kaapeli, jotta voit flashata laiteohjelmiston ja syöttää virran suoraan kannettavasta tietokoneesta (sopii täysin luokkakäyttöön).


### Miksi rakentaa oma Hardware Wallet?



- Säästät noin 135 dollaria verrattuna kaupallisen laitteen ostamiseen.
- Luo mukavuutta laiteohjelmiston vilkkumisen, turvallisten elementtien ja wallet-hygienian avulla.
- Ota käyttöön lisää allekirjoitusvälineitä, jotta voit jakaa säästöt useille lompakoille.
- Vähennä toimitusketjuriskiä hankkimalla ja kokoamalla kaikki osat itse.
- Pidä Loppin mantra mielessä: suvereniteetti ja mukavuus ovat aina ristiriidassa keskenään.


## Fyysiset asetukset


### Valmistele tapauksesi


Sinulla on kaksi vaihtoehtoa LilyGO T-Display -näytön koteloimiseksi: 3D-tulostettu kotelo tai virallinen LilyGO-kotelo. Tulostettu kotelo löytyy ja tulostetaan osoitteesta [tämä malli](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Se tarjoaa kevyen ja mukautettavan kuoren laitteellesi.


![image](assets/fr/04.webp)


Vaihtoehtoisesti voit käyttää virallista LilyGO-koteloa, joka tarjoaa hieman erilaisen istuvuuden ja viimeistelyn, joka tarjoaa vankemman suojan ja kiillotetun ulkonäön.


![image](assets/fr/05.webp)


Huomaa, että painetut ja viralliset kotelot eroavat hieman toisistaan suunnittelun ja kokoonpanon osalta. Riippumatta siitä, minkä vaihtoehdon valitset, varmista, että piirilevy on kunnolla kotelon sisällä, jotta vältetään löysät liitännät tai vauriot.


### Tarkasta hallitus


Ennen kuin jatkat, tarkista LilyGO T-Display -näyttötaulu huolellisesti mahdollisten näkyvien vikojen tai roskien varalta. Tarkista, että näyttö, painikkeet ja USB-C-portti ovat puhtaita ja että niissä ei ole pölyä tai juotosroiskeita. Käsittele piirilevyä varovasti ja noudata sähköstaattisen purkauksen (ESD) turvallisuutta maadoittamalla itsesi tai käyttämällä ESD-rannehihnaa, jotta herkät komponentit eivät vaurioidu.


### Yhdistä kannettavaan tietokoneeseen


Kytke LilyGO-levy kannettavaan tietokoneeseen dataan soveltuvalla USB-C-kaapelilla. Tämä yhteys antaa virtaa ja mahdollistaa laiteohjelmiston flashaamisen.


Käynnistyessäsi näytölle avautuu seuraava ruutu:


![image](assets/fr/06.webp)



Kun virta on kytketty päälle, LilyGO näyttää väritestinäytön, joka käy läpi kiinteitä värejä. Näin varmistetaan, että näyttö ja piirilevy toimivat oikein ennen laiteohjelmiston vilkkumista.


Kun väritesti on suoritettu, näyttö asettuu oletustilaan, joka osoittaa, että levy on valmis rakentamisprosessin seuraaviin vaiheisiin.


![image](assets/fr/07.webp)


## Helppo tapa vai Hard tapa


wallet-laitteiston laiteohjelmiston flashaamiseen on kaksi päätapaa: helppo ja vaikea tapa. Helppo tapa käyttää valmiiksi konfiguroituja työkaluja tai verkkopohjaisia flash-ohjelmia, jotka lataavat laiteohjelmiston automaattisesti laitteeseen minimaalisella syötöllä. Tämä menetelmä on ihanteellinen aloittelijoille, jotka haluavat nopean voiton tai jotka haluavat välttää virheenkorjauksen ja komentorivillä tapahtuvan vuorovaikutuksen monimutkaisuutta. Se yksinkertaistaa prosessia ja nopeuttaa käyttöönottoa, joten se on käytettävissä myös niille, jotka ovat vasta-alkajia sulautetun kehityksen tai laitteistolompakoiden parissa.


Vaikea tapa taas tarkoittaa, että laiteohjelmiston flashaaminen tapahtuu manuaalisesti komentorivityökalujen avulla. Tämä lähestymistapa edellyttää laiteohjelmiston allekirjoitusten ja tarkistussummien tarkistamista aitouden ja eheyden varmistamiseksi, mikä antaa sinulle syvemmän ymmärryksen flash-prosessista ja siitä, miten laiteohjelmisto on vuorovaikutuksessa laitteiston kanssa. Vaikka se vaatii enemmän vaivaa ja perehtyneisyyttä päätepääkomentoihin, se tarjoaa paremman hallinnan, avoimuuden ja luottamuksen laitteesi turvallisuuteen.


Kummassakin menetelmässä on omat kompromissinsa: helppo tapa uhraa jonkin verran luottamusta ja ymmärrystä nopeuden ja mukavuuden hyväksi, kun taas vaikea tapa vaatii enemmän aikaa ja teknistä taitoa, mutta palkitsee sinut joustavuudella ja paremmalla ymmärryksellä taustalla olevasta teknologiasta. Kouluttajien tulisi kannustaa oppilaita valitsemaan polku, joka vastaa parhaiten heidän mukavuustasoaan ja uteliaisuuttaan, ja edistää näin sekä luottamusta että tutkimista.


## Helppo tapa


Helpoin tapa flashata ESP32



- Siirry viralliseen Blockstream Githubiin: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Voit ladata lähdetiedoston ja ajaa verkkosivuston paikallisesti, mutta GitHubissa se on jo osoitteessa [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub tarjoilee HTML:n, CSS:n, JavaScriptin jne. suoraan selaimeen, joten voit väläyttää laitteen ilman kehittäjätyökalujen asentamista.


![image](assets/fr/09.webp)



- Avaa pudotusvalikko (oletusasetuksena on todennäköisesti `M5Stack Core2`) ja valitse kehityskorttisi - tässä luokassa valitse `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Kun napsautat flashia, tämä tulee näkyviin. Jos haluat tietää, mikä laite on LILYGO, irrota lilygo ja kytke se takaisin. Lilygon com-portti ilmestyy ja katoaa. Napsauta COM-porttia, johon Jade on kytketty


![image](assets/fr/11.webp)



- Se on siinä, edistymispalkin pitäisi näkyä, ja kun se on valmis, voit ottaa sen käyttöön


## Jade Wallet:n asettaminen paikalleen


Kun laiteohjelmiston välähdys on onnistunut, LilyGO T-Display on nyt täysin toimiva Jade-laitteisto wallet. Tässä osiossa käydään läpi alkuasennusprosessi seed-lauseen luomisesta laitteen yhdistämiseen wallet-ohjelmistolla, kuten Sparrow:llä tai Blockstream Green-mobiilisovelluksella.


### Alkukäynnistys ja laiteasetukset



- Käynnistä laite:** Kun LilyGO on edelleen liitetty kannettavaan tietokoneeseen USB-C:n kautta, Jade-ohjelmiston pitäisi käynnistyä automaattisesti. Näet Jade-logon ilmestyvän näyttöön.



- Siirry asetustilaan:** Laite näyttää sinulle aloitusvalikon. Käytä navigointiin kahta fyysistä painiketta:
 - Vasen painike:** Siirry ylös/taakse
 - Oikea painike:** Siirry alas/eteenpäin
 - Molemmat painikkeet samanaikaisesti:** Valitse/vahvista



- Valitse "Setup":** Siirry Setup (Asetukset) -vaihtoehtoon ja vahvista painamalla molempia painikkeita. Laite opastaa sinut alkukonfigurointiprosessin läpi.


### Wallet:n luominen



- Valitse "Begin Setup":** Laite pyytää sinua aloittamaan wallet:n luomisprosessin. Vahvista valintasi.



- Valitse "Create New Wallet":** Sinulle esitetään kaksi vaihtoehtoa:
 - Luo uusi Wallet:** Luo uuden seed-lauseen (valitse tämä työpajaa varten)
 - Palauta Wallet:** Palauta olemassa oleva wallet seed-lauseesta (edistyneille käyttäjille)



- Valitse "Luo uusi Wallet" ja vahvista.



- Entropian luominen:** Laite käyttää satunnaislukugeneraattoriaan kryptografisen entropian luomiseen. Tämä prosessi kestää muutaman sekunnin, kun laite kerää satunnaislukuja useista lähteistä.


### Siemenlauseen tallentaminen



- Kirjoita seed-lauseesi:** Laite näyttää nyt 12-sanaisen BIP39 seed -lauseen sana kerrallaan. Tämä on koko prosessin kriittisin vaihe.


**Tärkeitä turvallisuuskäytäntöjä:**


- Kirjoita jokainen sana selvästi paperille (käytä mukana toimitettuja seed-lausekortteja, jos niitä on saatavilla)
- Tarkista jokainen sana kahteen kertaan kirjoittaessasi sitä
- Älä koskaan kuvaa seed-lausetta puhelimella
- Älä koskaan kirjoita sanoja mihinkään tietokoneeseen tai puhelimeen
- Pidä seed-lauseesi yksityisenä - älä jaa näyttöäsi tai näytä sitä muille



- seed-lauseen tarkistaminen:** Kun olet kirjoittanut kaikki 12 sanaa, laite pyytää sinua vahvistamaan useita sanoja lauseesta varmistaaksesi, että olet tallentanut ne oikein. Valitse painikkeilla oikea sana kuhunkin kehotukseen.


**Pro-vinkki:** Ennen kuin jatkat, harjoittele lukemaan seed-lauseesi ääneen (hiljaa, jotta muut eivät kuule). Tämä auttaa havaitsemaan mahdolliset kirjoitusvirheet tai epäselvyydet.


### Yhteysmenetelmä



- Valitse yhteystyyppi:** Jade-laiteohjelmisto tukee kahta yhteystapaa:
 - USB:** Langallinen yhteys USB-C-kaapelilla (suositellaan tähän työpajaan)
 - Bluetooth:** Langaton yhteys mobiililaitteisiin



- Valitse toistaiseksi **USB**, koska se on suoraviivaisin vaihtoehto työpöydän wallet-ohjelmistolle, eikä se aiheuta langattomia hyökkäysväyliä.



- Laitteen nimeäminen:** Jade näyttää yksilöllisen tunnuksen, kuten "Connect Jade A7D924". Tämä tunniste auttaa sinua erottamaan useamman laitteiston lompakot toisistaan, jos päädyt rakentamaan useamman kuin yhden. Merkitse tämä tunniste muistiin, jos haluat.


### Yhdistäminen Wallet-ohjelmistoon


Sinulla on nyt kaksi päävaihtoehtoa liittyä juuri luotuun wallet-laitteistoon: Blockstream Green-mobiilisovellus (mobiilikäyttöön) tai Sparrow Wallet (työpöytäkäyttöön, jossa on kehittyneempiä ominaisuuksia). Tässä työpajassa keskitymme Sparrow Wallet:een, koska se tarjoaa paremman näkyvyyden Bitcoin-tapahtumien teknisiin yksityiskohtiin.


#### Vaihtoehto 1: Blockstream Green-mobiilisovellus (Pikakäynnistys)


Jos haluat testata laitteen nopeasti mobiililaitteella:



- Lataa **Blockstream Green**-sovellus App Storesta (iOS) tai Google Playsta (Android)
- Avaa sovellus ja valitse "Connect Hardware Wallet"
- Valitse "Jade" tuettujen laitteiden luettelosta
- Kytke Jade puhelimeen USB-C-USB-C-kaapelilla (tai USB-C-Lightning-sovittimella iPhone 15+ -puhelimelle)
- Seuraa näytön ohjeita muodostaaksesi yhteyden ja luodaksesi ensimmäisen wallet:n


**Huomautus Liquid:** Blockstream Green-sovellus tukee sekä Bitcoin:ää että Liquid:a (Bitcoin-sivuketju). Jos käytät Liquid-ominaisuuksia, sinua saatetaan kehottaa "Vie pääsalausavain" - tämän avulla sovellus näkee Liquid-verkossa tapahtuvien transaktioiden summat, jotka muuten ovat luottamuksellisia. Tässä työpajassa voit jättää Liquid-ominaisuudet väliin ja keskittyä tavallisiin Bitcoin-tapahtumiin.


#### Vaihtoehto 2: Sparrow Wallet (suositellaan työpajaan)


Sparrow Wallet on tehokas työpöytäsovellus, joka antaa sinulle yksityiskohtaisen hallinnan Bitcoin-tapahtumiin ja yhdistää saumattomasti Jade-laitteistoon wallet.


**Asennus:**



- Lataa Sparrow Wallet viralliselta verkkosivustolta: [sparrowwallet.com](https://sparrowwallet.com)
- Tarkista latauksen allekirjoitus (katso lisätietoja Sparrow:n dokumentaatiosta)
- Asenna ja käynnistä sovellus


**Jaden liittäminen Sparrow:aan:**



- Siirry Sparrow:ssä kohtaan **Tiedosto → Uusi Wallet**
- Anna wallet:lle nimi (esim. "My Jade Wallet")
- Napsauta **Kytketty Hardware Wallet**
- Sparrow:n pitäisi automaattisesti havaita kytketty Jade-laitteesi
- Vahvista yhteys Jade-näytössä painamalla molempia painikkeita, jos sinua kehotetaan siihen
- Valitse haluamasi käsikirjoitustyyppi:
 - Native Segwit (P2WPKH):** Suositellaan aloittelijoille - alhaisimmat maksut, laajin yhteensopivuus nykyaikaisten lompakoiden kanssa
 - Nested Segwit (P2SH-P2WPKH):** Yhteensopivuus vanhempien palvelujen kanssa
 - Taproot (P2TR):** Edistyksellisin, tarjoaa parhaan yksityisyyden suojan ja alhaisimmat maksut, mutta vaatii huippuluokan wallet-tuen
- Napsauta **Import Keystore** saadaksesi yhteyden valmiiksi


**Sparrow:n palvelinyhteyden konfigurointi:**


Ennen kuin voit nähdä saldosi tai lähettää transaktioita, Sparrow:n on muodostettava yhteys Bitcoin-solmuun lohkoketjutietojen hakemista varten. Sinulla on useita vaihtoehtoja, joista kullakin on erilaisia kompromisseja mukavuuden, yksityisyyden ja luottamuksen välillä:



- Julkinen Electrum Server (helpoin, vähiten yksityinen):** Yhteys kolmannen osapuolen ylläpitämään julkiseen palvelimeen. Nopea asentaa, mutta palvelin voi nähdä wallet:n osoitteet ja mahdollisesti yhdistää ne IP-osoitteeseesi. Hyvä testiverkon testaukseen.
 - Siirry Sparrow:ssa kohtaan **Työkalut → Asetukset → Palvelin**
 - Valitse **Julkinen palvelin** ja valitse palvelin luettelosta
 - Tarkista yhteys napsauttamalla **Testaa yhteys**



- Bitcoin Core tai Knots Node (yksityisin, eniten työtä):** Suorita oma täysi Bitcoin-solmusi. Tämä on yksityisyyden ja varmennuksen kultainen standardi, koska varmennat jokaisen tapahtuman itse etkä luota kenenkään muun palvelimeen. Se edellyttää kuitenkin koko lohkoketjun (~600 Gt) lataamista ja solmun synkronointia.
 - Asenna ja synkronoi Bitcoin Core tai Knots
 - Siirry Sparrow:ssä kohtaan **Työkalut → Asetukset → Palvelin**
 - Valitse **Bitcoin Core tai Knots** ja syötä solmun yhteystiedot



- Yksityinen Electrum Server (hyvä tasapaino):** Isännöi omaa Electrum-palvelinta (kuten Fulcrum tai Electrs), joka on yhdistetty Bitcoin Core- tai Knots-solmuun. Tarjoaa täyden yksityisyyden ilman, että sinun tarvitsee käyttää Sparrow:tä samalla koneella kuin solmusi.
 - Määritä Electrum-palvelin, joka osoittaa Bitcoin Core- tai Knots-solmuun
 - Siirry Sparrow:ssa kohtaan **Työkalut → Asetukset → Palvelin**
 - Valitse **Private Electrum** ja syötä palvelimesi URL-osoite


Tässä työpajassa **Julkinen Electrum Server** sopii täydellisesti testiverkkotapahtumiin. Tuotantoympäristössä, jossa on todellisia varoja, kannattaa harkita oman solmun käyttämistä tai luotettavan yksityisen palvelimen käyttämistä maksimaalisen yksityisyyden takaamiseksi.


#### Vaihtoehto 3: Blockstream Green Desktop App (Pika-aloitus)


Blockstream Green on ohjelmisto, jolla JadeDIY:n asetukset viimeistellään, ja sen on oltava työpöytäversiossa



- Hanki virallinen Blockstream-sovellus - tämä on linkki siihen heidän verkkosivustoltaan. Kun olet siellä, klikkaa [Lataa nyt](https://blockstream.com/app/).


![image](assets/fr/12.webp)



- Riippuen siitä, minne latauksesi menevät, tiedosto on todennäköisesti Lataukset-kansiossasi. Tarkista sieltä ja asenna ohjelmisto kaksoisnapsauttamalla suoritettavaa tiedostoa.


![image](assets/fr/13.webp)



- Sinun on ehkä annettava järjestelmänvalvojan oikeudet asennusohjelman suorittamiseen. Kun olet suorittanut asennuksen, avautuu seuraavan kuvan kaltainen ikkuna - napsauta **Seuraava**.


![image](assets/fr/14.webp)



- Valitse, mihin haluat asennetun sovelluksen sijoittaa (paikkaan, jossa on muita ohjelmia tai johonkin helposti löydettävään paikkaan), ja napsauta sitten **Seuraava**.


![image](assets/fr/15.webp)



- Asennusohjelma kysyy pikakuvakkeen nimeä. Kirjoita sellainen tai pidä oletusarvo ja napsauta sitten **Seuraava**.


![image](assets/fr/16.webp)



- Jos haluat työpöydän pikakuvakkeen, ruksaa ruutu; muussa tapauksessa valitse **Seuraava**.


![image](assets/fr/17.webp)



- Napsauta lopuksi **Asenna** ja odota muutama minuutti, kunnes asennus on valmis.


![image](assets/fr/18.webp)



- Edistymispalkin pitäisi täyttyä loppuun asti.


![image](assets/fr/19.webp)



- Kun se on valmis, näyttöön tulee uusi sivu - napsauta **Viimeistele**.


![image](assets/fr/20.webp)



- Etsi juuri asennettu Blockstream-sovellus (esimerkki näkyy Windows 11:n Käynnistä-valikossa).


![image](assets/fr/21.webp)



- Kun olet löytänyt sen, käynnistä se napsauttamalla - aloitusnäytön pitäisi tulla näkyviin.


### Asetusten tarkistaminen


Kun yhteys on muodostettu Sparrow:een (tai toiseen wallet-sovellukseen):



- Tarkista osoitteet:** Sparrow näyttää seed-lausekkeesta johdetut vastaanotto-osoitteet. Voit tarkistaa osoitteen Jade-laitteestasi menemällä Sparrow:n "Vastaanota"-välilehdelle ja napsauttamalla "Näytä Address" - osoitteen pitäisi näkyä sekä tietokoneen näytöllä että Jade-näytöllä.



- Luo vastaanottoosoite:** Napsauta Sparrow:n **Vastaanotto**-välilehteä ja kopioi ensimmäinen Bitcoin-vastaanottoosoitteesi.



- Valmis tapahtumia varten:** wallet-laitteistosi on nyt täysin konfiguroitu ja valmis vastaanottamaan ja allekirjoittamaan Bitcoin-tapahtumia. Jatka seuraavaan osioon harjoitellaksesi testnet-tapahtuman allekirjoittamista.



---

### Pika-asetusten tarkistuslista



- Jade firmware käynnistyy onnistuneesti
- Uusi wallet luotu 12-sanaisella seed-lauseella
- Siemenlause kirjataan selvästi ja tarkistetaan
- USB-yhteystila valittu
- Wallet-ohjelmisto (Sparrow) asennettu ja liitetty
- Palvelinyhteys määritetty (julkinen Electrum mainnet:lle)
- Ensimmäinen vastaanotto-osoite luodaan ja tarkistetaan laitteessa



---

**MIT License**


**Tekijänoikeus (c) 2025 The Bitcoin Network NYC**


Kuka tahansa henkilö, joka hankkii kopion tästä ohjelmistosta ja siihen liittyvistä dokumentaatiotiedostoista ("Ohjelmisto"), saa täten maksutta oikeuden käsitellä ohjelmistoa rajoituksetta, mukaan lukien rajoituksetta oikeudet käyttää, kopioida, muuttaa, yhdistää, julkaista, jakaa, alilisensoida ja/tai myydä ohjelmistokopioita, ja sallia henkilöiden, joille ohjelmisto on toimitettu, tehdä niin seuraavin ehdoin:


Yllä oleva tekijänoikeusilmoitus ja tämä lupailmoitus on sisällytettävä kaikkiin ohjelmiston kopioihin tai merkittäviin osiin.


OHJELMISTO TARJOTAAN SELLAISENAAN ILMAN MINKÄÄNLAISTA TAKUUTA, NIMENOMAISTA TAI EPÄSUORAA, MUKAAN LUKIEN MUTTA EI RAJOITTUEN TAKUISIIN KAUPALLISESTA KELPOISUUDESTA, SOVELTUVUUDESTA TIETTYYN TARKOITUKSEEN JA LOUKKAAMATTOMUUDESTA. TEKIJÄT TAI TEKIJÄNOIKEUKSIEN HALTIJAT EIVÄT MISSÄÄN TAPAUKSESSA OLE VASTUUSSA MISTÄÄN VAATEISTA, VAHINGOISTA TAI MUUSTA VASTUUSTA, OLIPA KYSE SITTEN SOPIMUKSESTA, VAHINGONKORVAUSVELVOLLISUUDESTA TAI MUUSTA VAHINGOSTA, JOTKA JOHTUVAT OHJELMISTOSTA, SEN KÄYTÖSTÄ TAI MUUSTA OHJELMISTOON LIITTYVÄSTÄ TOIMINNASTA TAI LIITTYVÄT SIIHEN.


---