---
name: Start9

description: Tutoriaali yksityisen Start9-palvelimen perustamisesta

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Tässä on video-opas Southern Bitcoinerilta, video-opas, jossa näytetään, miten asentaa ja käyttää Start9 / StartOS henkilökohtaista palvelinta ja miten ajaa bitcoin-solmua.*


## 1️⃣ Johdanto


### Mitä Start9 tarkalleen ottaen on?


Start9 on vuonna 2020 perustettu yritys, joka tunnetaan parhaiten [**StartOS**,](https://github.com/Start9Labs/start-os) - henkilökohtaisille palvelimille tarkoitetun Linux-pohjaisen käyttöjärjestelmän kehittämisestä. Sen avulla käyttäjät voivat helposti itse isännöidä monenlaisia ohjelmistopalveluja - kuten Bitcoin- ja Lightning-solmuja, viestisovelluksia tai salasanojen hallintaa - ja säilyttää samalla tietojensa täyden hallinnan ja poistaa riippuvuuden keskitetyistä teknologia-alustoista. StartOS:ssä on käyttäjäystävällinen, selainpohjainen käyttöliittymä, kuratoitu Marketplace palveluiden asentamista varten ja sisäänrakennettuja yksityisyydensuojatyökaluja, kuten Tor-integraatio ja koko järjestelmän laajuinen HTTPS-salaus. Start9 tarjoaa myös laitteistolaitteita, joihin käyttöjärjestelmä on ladattu valmiiksi, vaikka ohjelmisto voidaan asentaa yhteensopivaan laitteistoon tai virtuaalikoneisiin (VM).


### Mitä vaihtoehtoja on tarjolla?


Start9 tarjoaa sekä valmiiksi rakennettuja että DIY-käyttöönottovaihtoehtoja. [**Server One**](https://store.start9.com/collections/servers/products/server-one) ja [**Server Pure** ](https://store.start9.com/collections/servers/products/server-pure) ovat virallisia laitteistoja, joissa on suorituskykyisiä komponentteja: Server One käyttää **AMD Ryzen 7 5825U** -suoritinta, jossa on konfiguroitavissa olevaa RAM-muistia (16GB-64GB) ja tallennustilaa (2TB-4TB NVMe SSD), kun taas Server Pure on varustettu **Intel i7-10710U** -prosessorilla, jossa on niin ikään konfiguroitavissa olevaa RAM-muistia ja tallennustilaa. Molempiin sisältyy **elinikäinen tekninen tuki**, kun ne ostetaan suoraan Start9:ltä. Käyttäjät, jotka haluavat joustavuutta, voivat asentaa StartOS:n ilmaiseksi monenlaiseen olemassa olevaan laitteistoon, kuten kannettaviin tietokoneisiin, pöytätietokoneisiin, mini-PC:hen ja yhden piirilevyn tietokoneisiin, tai VM-tietokoneisiin.


![image](assets/en/01.webp)


### Mitä eroja Umbreliin on?


StartOS ja Umbrel helpottavat molemmat itse isännöidyn palvelun asennusta, mutta eroavat toisistaan arkkitehtuuriltaan ja ominaisuuksiltaan. Umbrel toimii sovelluskerroksena Debian/Ubuntu-järjestelmissä tai VM:ssä, kun taas Start9 on oma käyttöjärjestelmä, joka vaatii suoran laitteisto- tai VM-asennuksen. Umbrelissa on kiiltävä, macOS-vaikutteinen käyttöliittymä, kun taas Start9:ssä painotetaan toiminnallista, minimaalista suunnittelua. Umbrel tarjoaa laajemman [sovellusvalikoiman](https://apps.umbrel.com/), kun taas [Start9 Marketplace](https://marketplace.start9.com/) kompensoi sen kehittyneillä teknisillä ominaisuuksilla. Start9 yksinkertaistaa pääsyä lisäasetuksiin validoitujen käyttöliittymälomakkeiden avulla, mikä vähentää tarvetta komentorivillä tapahtuvaan vuorovaikutukseen. Se on erinomainen myös varmuuskopioiden hallinnassa, sillä se tarjoaa yhdellä napsautuksella salattuja järjestelmävarmuuskopioita, mikä on ominaisuus, joka puuttuu Umbrelista. StartOS tarjoaa sisäänrakennettuja valvontatyökaluja ja käyttää HTTPS-salausta lähiverkkoyhteyksiä varten, mikä parantaa turvallisuutta. Umbrel käyttää salaamatonta HTTP:tä paikallisesti, vaikka molemmat alustat tukevat suojattua etäkäyttöä Torin kautta. Umbrel soveltuu käyttäjille, jotka pitävät tärkeimpinä runsasta sovellusekosysteemiä ja hiottua käyttöliittymää. Start9 on vahva valinta niille, jotka arvostavat tietoturvaa, konfiguroitavuutta, varmuuskopioiden luotettavuutta ja kehittynyttä palvelujen hallintaa ilman komentoriviosaamista. Jos haluat lisätietoja Umbrelista ja sen eroista Start9:ään, käy tällä kurssilla:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ DIY Edellytykset: Tekniset tiedot: Vähimmäis- ja suositellut tiedot


Peruskäyttöön, jossa on vain vähän palveluja, **minimiarvot** ovat seuraavat: **1 vCPU-ydin (2,0 GHz+ boost), 4 Gt RAM-muistia, 64 Gt tallennustilaa** ja Ethernet-portti. Suosittelen kuitenkin, että menisit huomattavasti pidemmälle, varsinkin jos käytät Bitcoin-solmua. Itse aloitin 1TB:llä ja tila loppui nopeasti kesken. Tavoittele mieluummin **vähintään 2 Tt tallennustilaa** sekä **neliydinsuoritinta (2,5 GHz tai enemmän)** ja **8 Gt tai enemmän RAM-muistia**. Se tekee valtavan eron suorituskykyyn ja pitkäikäisyyteen. Jos haluat sukeltaa syvemmälle, tässä on ajantasainen yhteisön keskusteluketju aiheesta [Hardware Capable of Running of StartOS](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Lataa ja flashaa laiteohjelmisto


Aloita asennus erillisellä tietokoneella [Start9-sivustolla](https://start9.com/) ja siirry dokumentaatio-osioon napsauttamalla `DOCS`. Sieltä löydät sopivan StartOS-version kohdasta `Flashing Guides`. Käytettävissä on kaksi vaihtoehtoa:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Tämä opetusohjelma kattaa vaihtoehdon `x86/ARM`.


Uusin käyttöjärjestelmäversio on ladattavissa [Githubin julkaisusivulta](https://github.com/Start9Labs/start-os/releases/latest). [Pre-release](https://github.com/Start9Labs/start-os/releases) -versiot ovat myös saatavilla käyttäjille, jotka haluavat testata uusia ominaisuuksia. Sivun alareunassa, kohdassa `Assets`, lataa `x86_64` tai `x86_64-nonfree.iso`.  `x86_64-nonfree.iso`-kuva sisältää ei-vapaita (suljetun lähdekoodin) ohjelmistoja, joita tarvitaan Server One -laitteistoon ja useimpiin DIY-laitteistoihin, erityisesti grafiikka- ja verkkolaitetukeen.


On suositeltavaa tarkistaa tiedoston eheys tarkistamalla sen SHA256-hashtunnus GitHubissa olevaan tiedostoon verrattuna. Linuxissa voidaan käyttää komentoa `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso`, ja muita käyttöjärjestelmiä käsitellään dokumentaatiossa.


StartOS-kuvan lataamisen ja tarkistamisen jälkeen se on siirrettävä USB-asemaan. `BalenaEtcher` on suositeltava ohjelmisto tähän tehtävään. Se on ilmainen, avoimen lähdekoodin työkalu käyttöjärjestelmän kuvatiedostojen kirjoittamiseen USB-asemiin ja SD-kortteihin, ja se on saatavilla Windowsille, macOS:lle ja Linuxille. Lataa sopiva versio viralliselta [Balena Etcherin verkkosivulta](https://www.balena.io/etcher/) ja suorita asennusohjelma. Liitä kohde-USB-asema tai SD-kortti, avaa Balena Etcher ja valitse ladattu käyttöjärjestelmäkuva valitsemalla `Flash from file`. Etcher tunnistaa automaattisesti liitetyt asemat; valitse oikea kohde, jos niitä on useita. Aloita kuvan kirjoittaminen napsauttamalla `Flash!`. Etcher validoi kirjoitusprosessin automaattisesti sen päätyttyä. Kun olet valmis, irrota asema turvallisesti ja käytä sitä laitteen käynnistämiseen.


![image](assets/en/19.webp)


## 4️⃣ Alkuasetukset


Katso alkuasetukset Start9 [documentation](https://docs.start9.com/0.3.5.x/) -sivulta kohdasta `USER MANUAL` ja sen jälkeen kohdasta `Getting Started - Initial Setup`.  Tässä virallisessa oppaassa on oltava uusimmat tiedot.


Esitetään kaksi vaihtoehtoa:



- Aloita alusta
- Elvytysvaihtoehdot


Jos haluat asentaa uuden palvelimen, valitse `Start Fresh`. Kytke palvelimeen ensin virta ja Ethernet-kaapeli. Varmista, että asennukseen käytettävä tietokone on samassa lähiverkossa. Poista juuri flashattu USB-asema tietokoneesta ja aseta se palvelimeen.


Voit ohjata palvelinta etänä mistä tahansa samassa verkossa olevasta tietokoneesta. Avaa verkkoselain ja siirry osoitteeseen `http://start.local`.


**Huomautus**: Jos yhteysongelmia ilmenee tämän osoitteen kanssa, se johtuu usein siitä, että kotiverkot eivät pysty ratkaisemaan .local-verkkotunnuksia. Ongelma voidaan ratkaista ottamalla yhteys palvelimeen suoraan sen IP-osoitteen kautta. IP-osoite löytyy kirjautumalla reitittimen hallintaliittymään (yleensä osoitteessa `192.168.1.1.1` tai vastaavassa osoitteessa) ja etsimällä laite DHCP-asiakkaat- tai verkkokarttaluettelosta. Kirjoita sitten koko IP-osoite (esim. `http://192.168.1.105`) selaimeen. Tämä ohittaa DNS-resoluution. Jos ongelmat jatkuvat, tutustu [Common Issues -sivuun](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) tai [ota yhteyttä heidän tukeensa](https://start9.com/contact/)


StartOS-asetusnäytön pitäisi avautua. Napsauta `Start Fresh` aloittaaksesi uuden palvelimen asennuksen.


![image](assets/en/03.webp)


Seuraavaksi valitaan levyasema, jolle StartOS-tiedot tallennetaan.


![image](assets/en/04.webp)


Aseta palvelimelle vahva salasana. Tallenna se Start9:n ohjeiden mukaisesti ja napsauta sitten `FINISH`.


![image](assets/en/05.webp)


Näyttöön tulee ilmoitus, että StartOS alustaa ja määrittää palvelimen. Seuraava vaihe on `Lataa osoitetiedot`, sillä `start.local`-osoite on vain asennusta varten, eikä se toimi sen jälkeen.


![image](assets/en/06.webp)


Konfiguraatiotiedosto sisältää kaksi kriittistä yhteysosoitetta: yksi lähiverkkoa (LAN) varten ja toinen suojattua pääsyä varten Torin kautta. Molemmat osoitteet on tallennettava turvalliseen salasanahallintaan. Seuraava vaihe on `Luottaa Root CA:han`. Avaa uusi selainvälilehti ja noudata ohjeita Root CA:n luottamisesta ja kirjautumisesta. Root CA -varmenteen voi myös ladata napsauttamalla `Download certificate` (lataa varmenne) ladatusta tiedostosta.


## 5️⃣ Luota Root CA:han


Kun varmenne on ladattu, käyttöjärjestelmän on luotettava palvelimen `Root CA`:han. Napsauta `View Instructions` (Katso ohjeet) ja etsi käyttöjärjestelmäkohtaiset ohjeet.


![image](assets/en/07.webp)


Linux-järjestelmässä käytetään seuraavia komentoja. Avaa ensin terminaali ja asenna tarvittavat paketit:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Siirry hakemistoon, josta varmenne ladattiin, yleensä `~/Downloads` . Suorita nämä komennot lisätäksesi varmenteen käyttöjärjestelmän luotettavuusvarastoon. Siirry latauskansioon `cd ~/Downloads`. Luo tarvittava hakemisto komennolla `sudo mkdir -p /usr/share/ca-certificates/start9`. Kopioi varmennetiedosto korvaamalla `your-filename.crt` todellisella tiedostonimellä käyttäen `sudo cp "your-filename.crt" /usr/share/ca-certificates/start9/`. Rekisteröi varmenne pysyvästi liittämällä sen polku järjestelmän kokoonpanoon komennolla `sudo bash -c "echo 'start9/your-filename.crt' >> /etc/ca-certificates.conf"`. Rakenna lopuksi luottamusvarasto uudelleen komennolla `sudo update-ca-certificates`. On tärkeää käyttää todellista varmenteen tiedostonimeä ja tarkistaa kaikki polut ennen näiden komentojen suorittamista. Tämä prosessi luo pysyvän luottamuksen Start9-palvelimen HTTPS-yhteyksille.


Onnistuneesta asennuksesta ilmoitetaan tulosteessa `1 added`. Useimmat sovellukset pystyvät tämän jälkeen muodostamaan turvallisen yhteyden `https`:n kautta. Jos käytät Firefoxia, tarvitaan ylimääräinen [viimeinen vaihe](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff). Jos käytät Chromea tai Bravea, tarvitaan toinen [viimeinen vaihe](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome), jotta selain voidaan määrittää kunnioittamaan Root CA:ta. Testaa yhteys päivittämällä sivu. Jos ongelma ei poistu, lopeta selain ja avaa se uudelleen ennen sivun uudelleenkatsomista.


![image](assets/en/08.webp)


## 6️⃣ StartOS:n käytön aloittaminen


Nyt pitäisi olla mahdollista kirjautua sisään käyttämällä suojattua HTTPS-yhteyttä. Syötä "salasana" päästäksesi "tervetuloruutuun".


![image](assets/en/09.webp)


Tässä näytössä on hyödyllisiä pikanäppäimiä alkuun pääsyä varten. Vasemmassa sivupalkissa on tärkeimmät valikkokohdat navigointia varten.


## 7️⃣ Järjestelmä


StartOS:n Järjestelmät-välilehti tarjoaa pääsyn henkilökohtaisen palvelimen hallinnan keskeisiin järjestelmätoimintoihin. Se tarjoaa työkaluja järjestelmän ylläpitoon, tietoturvaan, diagnostiikkaan ja konfigurointiin ilman komentorivin asiantuntemusta.


"Varmuuskopiot"-osio mahdollistaa täydellisten järjestelmävarmuuskopioiden luomisen, mukaan lukien palvelut, määritykset ja tiedot, jotka voidaan palauttaa myöhemmin. Tämä on tärkeää katastrofien jälkeistä palautusta tai uuteen laitteistoon siirtymistä varten. Varmuuskopiot voidaan tallentaa ulkoisille asemille, ja ne salataan pääsalasanalla.


Järjestelmät-välilehden Hallinta-osiossa voit hallita järjestelmän keskeisiä toimintoja. Käyttäjät voivat manuaalisesti tarkistaa StartOS-päivitykset ja soveltaa niitä, jolloin järjestelmän päivitysprosessi pysyy hallinnassa. Mukautettuja tai kolmannen osapuolen palveluja, joita ei ole saatavilla virallisella markkinapaikalla, on mahdollista ladata sivulatauksena. Jos palvelinta ei ole yhdistetty Ethernetin kautta, Wi-Fi-asetukset voidaan määrittää tästä osiosta. Edistyneet käyttäjät voivat ottaa käyttöön SSH-yhteyden päätelaitetason järjestelmänhallintaa varten.


![image](assets/en/10.webp)


"Insights"-osio tarjoaa reaaliaikaista palvelimen suorituskyvyn ja kunnon seurantaa, ja siinä näytetään prosessorin, RAM-muistin ja levyn käyttö graafisesti. Se näyttää myös järjestelmän lämpötilan, mikä on hyödyllistä Raspberry Pi:n kaltaisissa laitteissa, joissa ei ole aktiivista jäähdytystä. Käyntiaika- ja kuormituskeskiarvomittarit auttavat arvioimaan järjestelmän vakautta, ja live-lokit ovat käytettävissä palvelin- tai järjestelmäongelmien vianmääritystä varten.


Tuki-osio tarjoaa pääsyn sisäänrakennettuihin usein kysyttyihin kysymyksiin, viralliseen dokumentaatioon ja yhteisön tukikanaviin. Tästä osiosta voi ladata virheenkorjauslokeja, jotka voi jakaa Start9-tuen kanssa ongelmien nopeampaa ratkaisua varten.


![image](assets/en/11.webp)


## 8️⃣ Markkinapaikka


Markkinapaikkaa käytetään henkilökohtaisen palvelimen palveluiden löytämiseen, asentamiseen ja hallintaan. Se tarjoaa pääsyn ohjelmistoihin, kuten Bitcoin Core, BTCPay Server ja electrs. StartOS tukee useita markkinapaikkoja, mukaan lukien virallinen Start9-rekisteri ja yhteisön ylläpitämät rekisterit. Nämä voidaan lisätä napsauttamalla `CHANGE` ja siirtymällä `Community Registry` -rekisteriin, joka tarjoaa pääsyn laajempaan palveluvalikoimaan.


![image](assets/en/12.webp)


## 9️⃣ Bitcoin Full Node -solmun asentaminen


Bitcoin full node:n asentaminen StartOS-käyttöjärjestelmään antaa täyden määräysvallan Bitcoin:n käyttökokemuksesta. Se mahdollistaa tapahtumien validoinnin ja parantaa yksityisyyttä ja turvallisuutta poistamalla riippuvuuden ulkoisista palveluista, jotka saattavat kirjautua toimintaan. Tapahtumat ovat täysin hallinnassa, ja ne voidaan lähettää suoraan verkkoon. Oletusvaihtoehto on `Bitcoin Core`, joka integroituu natiivisti StartOS:ään ja mahdollistaa yhteyden Specterin, Sparrow:n tai Electrum:n kaltaisiin lompakoihin, jotta voidaan tehdä itsesäilytysasetus. Vaihtoehto, `Bitcoin Knots`, on myös saatavilla yhteisön rekisterin kautta.


Asenna Bitcoin Core siirtymällä Marketplaceen. Etsi ja asenna Bitcoin Core -palvelu oletusrekisteristä. Asennuksen jälkeen näyttöön tulee `Needs Config` -kehote, joka vaatii asetusten tekemistä ennen palvelun käyttämistä. Tämä tapahtuu yleensä päivitysten tai uusien asennusten jälkeen ja kehottaa tarkistamaan RPC-asetukset. Jatka oletusasetusten mukaisesti ja napsauta `Save` (Tallenna).


![image](assets/en/13.webp)


Kun solmusi on täysin synkronoitu, se voi toimia Sparrow:n kaltaisten lompakoiden yksityisenä taustapalveluna, joka tarjoaa paremman yksityisyyden suojan ja tapahtumien validoinnin. Merkittäviä summia tallentavien käyttäjien on kuitenkin tärkeää ymmärtää tämän suoran yhteyden turvallisuushaitat. Kun wallet muodostaa yhteyden suoraan Bitcoin Coreen, se voi paljastaa arkaluonteisia tietoja, sillä Bitcoin Core tallentaa julkiset avaimet (xpubs) ja wallet:n saldot salaamattomina isäntäkoneeseen. Vaarantuneen järjestelmän avulla hyökkääjä voi saada selville omistuksesi ja kohdistaa hyökkäyksen sinuun.


Voit pienentää tätä riskiä ja saada aikaan vankemman turvallisuusmallin määrittämällä yksityisen Electrum Server:n. Tämä palvelin toimii välittäjänä, joka indeksoi lohkoketjun tallentamatta wallet-kohtaisia tietoja. Yhdistämällä wallet:n omaan Electrum-palvelimeesi sen sijaan, että se kytkettäisiin suoraan Bitcoin Coreen, estät wallet:n pääsyn solmun arkaluonteisiin tietoihin.


![image](assets/en/14.webp)


## 🔟 Aseta valitsijat


`electrs` (Electrum Rust Server) on nopea ja tehokas indeksoija, joka muodostaa yhteyden Bitcoin Core-solmuun ja mahdollistaa Electrum-yhteensopivien lompakoiden kyselyn tapahtumahistoriasta ja saldoista reaaliajassa. Käyttämällä electrs:ää StartOS-käyttöjärjestelmässä poistat riippuvuuden kolmannen osapuolen Electrum-palvelimista, mikä parantaa merkittävästi yksityisyyttä ja turvallisuutta - wallet-kyselyt menevät suoraan itse isännöimääsi solmuun.


Asenna ensin electrs-palvelu StartOS Marketplace -palvelusta. Järjestelmä edellyttää, että Bitcoin Core on täysin synkronoitu, ennen kuin jatkat. Asennuksen jälkeen vahvista `Needs Config`-asetukset suositelluilla oletusasetuksilla ja electrs alkaa indeksoida lohkoketjua, mikä voi kestää laitteistostasi riippuen jopa päivän.


![image](assets/en/15.webp)


Kun olet valmis, voit liittää lompakot, kuten Sparrow tai Specter. Onnistuneen yhteyden avulla wallet voi synkronoida suoraan solmun kanssa, mikä tarjoaa turvallisen, yksityisen ja itse isännöidyn Bitcoin-kokemuksen.


## 1️⃣1️⃣ Connect Sparrow Wallet


Jos haluat yhdistää Sparrow Wallet:n StartOS-solmuun electrs-toteutuksen avulla, varmista ensin, että Bitcoin Core on täysin synkronoitu ja electrs on asennettu ja käynnissä. Avaa Sparrow Wallet laitteellasi ja siirry kohtaan `File` -> `Settings` -> `Server`. Valitse sitten `Private Electrum Server`. Kirjoita URL-kenttään electrs:n `Torin isäntänimi` ja `Portti`, jotka löydät StartOS:n kohdasta `Services` -> `electrs` -> `Properties` (tyypillisesti päättyy `.onion:50001`).


![image](assets/en/16.webp)


Seuraavaksi ota Tor käyttöön valitsemalla `Käytä välityspalvelinta`, asettamalla välityspalvelimen osoitteeksi `127.0.0.1` ja portiksi `9050`. Napsauta `Test Connection` ja odota hetki. Onnistunut yhteys näyttää vahvistusviestin, kuten `Connected to electrs`. Kun olet varmistanut yhteyden, sulje asetukset ja jatka wallet:n luomista tai palauttamista. Tämä asetus varmistaa, että wallet kysyy omaa solmua electrs:n kautta, mikä takaa täydellisen yksityisyyden ja luotettavan toiminnan.


![image](assets/en/17.webp)


## 🎯 Päätelmät


Start9:n StartOS on käyttäjäystävällinen, yksityisyyteen keskittyvä alusta, joka on suunniteltu keskeisten palveluiden, kuten Bitcoin- ja Lightning-solmujen, lompakoiden ja henkilökohtaisten sovellusten, omatoimiseen isännöintiin. Se poistaa komentorivitaitojen tarpeen tarjoamalla selkeän graafisen käyttöliittymän, automaattiset varmuuskopiot, kunnonvalvonnan ja suojatun Tor-yhteyden, joten se sopii erinomaisesti muille kuin teknisille käyttäjille. Sen modulaarinen arkkitehtuuri tukee saumatonta integrointia electrs:n tai Sparrow:n kaltaisten työkalujen kanssa, jolloin saat täyden hallinnan taloudelliseen ja digitaaliseen itsemääräämisoikeuteesi. StartOS keskittyy vahvasti avoimuuteen, paikalliseen hallintaan ja laajennettavuuteen, ja sen avulla käyttäjät voivat ottaa omistusoikeuden takaisin keskitetyiltä alustoilta ja käyttää omaa yksityistä, joustavaa infrastruktuuriaan.