---
name: RoninDojo v2
description: RoninDojo v2 Bitcoin-solmun asentaminen Raspberry Pi:lle
---
![cover RoninDojo v2](assets/cover.webp)

***VAROITUS:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta, tietyt RoninDojon ominaisuudet, kuten Whirlpool, eivät ole enää toiminnassa. On kuitenkin mahdollista, että nämä työkalut voidaan palauttaa tai käynnistää uudelleen eri tavalla tulevina viikkoina. Lisäksi, koska RoninDojon koodi oli isännöity Samourain GitLabiin, joka myös takavarikoitiin, koodin etälataus ei tällä hetkellä ole mahdollista. RoninDojon tiimit työskentelevät todennäköisesti koodin uudelleenjulkaisemiseksi.*

_Seuraamme tiiviisti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voit olla varma, että päivitämme tämän oppaan, kun uutta tietoa tulee saataville._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme kannusta tai hyväksy näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

> "*Käytä Bitcoinia yksityisesti.*"

Edellisessä oppaassa olimme jo selittäneet menettelyn RoninDojo v1:n asentamiseksi ja käyttämiseksi. Viime vuoden aikana RoninDojon tiimit ovat kuitenkin julkaisseet version 2 heidän toteutuksestaan, mikä merkitsi merkittävää käännekohtaa ohjelmiston arkkitehtuurissa. Todellakin, he siirtyivät pois Linux Manjaro -jakelusta Debianin hyväksi. Tämän seurauksena he eivät enää tarjoa esiasennettua kuvaa automaattiseen asennukseen Raspberry Pi:lle. Mutta on edelleen olemassa menetelmä manuaaliseen asennukseen. Tätä menetelmää käytin oman solmun asentamiseen, ja siitä lähtien RoninDojo v2 on toiminut upeasti Raspberry Pi 4:ssäni. Tarjoan siis uuden oppaan RoninDojo v2:n manuaaliseen asentamiseen Raspberry Pi:lle.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0



## Sisällysluettelo:
- Mikä on RoninDojo?
- Minkä laitteiston valita RoninDojo v2:n asentamiseen?
- Kuinka koota Raspberry Pi 4?
- Kuinka asentaa RoninDojo v2 Raspberry Pi 4:ään?
- Kuinka käyttää RoninDojo v2 -solmuasi?

## Mikä on RoninDojo?
Dojo on alun perin täysi Bitcoin-solmun toteutus, joka perustuu Bitcoin Coreen ja on kehitetty Samourai Wallet -tiimien toimesta. Tämä ratkaisu voidaan asentaa mille tahansa laitteistolle. Toisin kuin muut Core-toteutukset, Dojo on erityisesti optimoitu integroitumaan Samourai Walletin Android-sovellusympäristöön. RoninDojon osalta se on työkalu, joka on suunniteltu helpottamaan Dojon sekä erilaisten muiden täydentävien työkalujen asentamista ja hallintaa. Lyhyesti sanottuna, RoninDojo rikastaa Dojon perustoteutusta integroimalla lukuisia lisätyökaluja, samalla yksinkertaistaen sen asentamista ja hallintaa.

Ronin tarjoaa myös [solmu-boksi-ratkaisun, nimeltään "*Tanto*"](https://ronindojo.io/en/products), laite, jossa RoninDojo on jo asennettuna tiimin kokoamaan järjestelmään. Tanto on maksullinen vaihtoehto, joka voi olla kiinnostava niille, jotka haluavat välttää tekniset komplikaatiot. Mutta koska RoninDojon lähdekoodi on avoin, on myös mahdollista ottaa se käyttöön omalla laitteistolla. Tämä vaihtoehto, joka on taloudellisempi, vaatii kuitenkin joitakin lisätoimenpiteitä, joita käsittelemme tässä oppaassa.
RoninDojo on Dojo, joten se mahdollistaa Whirlpool CLI:n helpon integroinnin Bitcoin-noodiisi tarjoten parhaan mahdollisen coinjoin-kokemuksen. Whirlpool CLI:n avulla on mahdollista jatkuvasti sekoittaa bitcoinejasi, 24 tuntia vuorokaudessa, 7 päivää viikossa, ilman että henkilökohtaisen tietokoneesi tarvitsee pysyä päällä.

Whirlpool CLI:n lisäksi RoninDojo sisältää erilaisia työkaluja Dojosi toiminnallisuuksien parantamiseen. Näiden joukossa Boltzmann-laskin analysoi transaktioidesi yksityisyystason, Electrum-palvelin mahdollistaa Bitcoin-lompakkojesi yhdistämisen noodisi kanssa, ja Mempool-palvelin mahdollistaa transaktioidesi paikallisen tarkastelun, ilman tietojen vuotamista.

Verrattuna muihin noodiratkaisuihin, kuten Umbrel, RoninDojo keskittyy selkeästi on-chain-ratkaisuihin ja yksityisyyden suojaustyökaluihin. Toisin kuin Umbrel, RoninDojo ei tue Lightning-noodin pystyttämistä eikä yleisempien palvelinsovellusten integrointia. Vaikka RoninDojo tarjoaa vähemmän monipuolisia työkaluja kuin Umbrel, sillä on kaikki olennaiset toiminnallisuudet on-chain-toimintasi hallintaan.

Jos et tarvitse yleisiä toiminnallisuuksia tai niitä, jotka liittyvät Lightning Networkiin, kuten Umbrel tarjoaa, ja etsit yksinkertaista, vakaata noodia olennaisilla työkaluilla, kuten Whirlpool tai Mempool, RoninDojo voisi olla ihanteellinen ratkaisu. Siinä missä Umbrel pyrkii muodostumaan mini-monitoimipalvelimeksi, joka on suunnattu Lightning Networkille ja monipuolisuudelle, RoninDojo keskittyy Samourai Walletin filosofian mukaisesti käyttäjän yksityisyyden kannalta olennaisiin työkaluihin.

Nyt kun olemme hahmotelleet RoninDojon, katsotaan yhdessä, miten tämä noodi pystytetään.

## Minkä laitteiston valita RoninDojo v2:n asentamiseen?
RoninDojo tarjoaa automaattisen asennuksen ohjelmistonsa [RockPro64](https://ronindojo.io/en/download) -laitteistolle. Tämä opas keskittyy kuitenkin manuaaliseen asennusmenetelmään Raspberry Pi 4:lle. Vaikka Raspberry Pi 5 on äskettäin julkaistu, ja tämän oppaan pitäisi teoriassa olla yhteensopiva tämän uuden mallin kanssa, en ole vielä henkilökohtaisesti päässyt testaamaan sitä, enkä ole löytänyt palautetta yhteisöltä. Heti kun hankin Pi 5:n ja yhteensopivat komponentit, päivitän tämän oppaan pitääkseni sinut ajan tasalla. Siihen asti suosittelen priorisoimaan Pi 4:n, sillä se toimii täydellisesti noodilleni.
Osa yhteisön jäsenistä on onnistunut saamaan sen toimimaan laitteilla, joissa on vain 4 GB RAM-muistia, mutta en ole itse testannut tätä konfiguraatiota. Pienen hintaeron vuoksi vaikuttaa viisaalta valita 8 GB RAM-muistin versio. Tämä voi myös osoittautua hyödylliseksi, jos suunnittelet Raspberry Pin uudelleenkäyttöä muissa tulevaisuuden projekteissa.
On tärkeää huomata, että RoninDojo-tiimit ovat raportoineet usein ongelmista, jotka liittyvät kotelo- ja SSD-sovittimeen. Olen kohdannut näitä ongelmia itse. **Siksi on erittäin suositeltavaa välttää koteloita, jotka on varustettu USB-kaapelilla noodisi SSD:lle.** Sen sijaan suosi Raspberry Pi:lle suunniteltua tallennuslaajennuskorttia:

![storage expansion card RPI4](assets/notext/1.webp)
Bitcoin-lohkoketjun tallentamiseen tarvitset SSD:n, joka on yhteensopiva valitsemasi tallennuslaajennuskortin kanssa. Tällä hetkellä (helmikuu 2024) olemme siirtymävaiheessa. Odotetaan, että muutaman kuukauden kuluttua 1 TB:n levyt eivät enää riitä kattamaan lohkoketjun kasvavaa kokoa, erityisesti kun otetaan huomioon erilaiset sovellukset, jotka aiot integroida solmuusi. Jotkut suosittelevat siksi sijoittamaan 2 TB:n SSD:hen pitkän aikavälin mielenrauhan vuoksi. Kuitenkin, SSD:n hintojen laskusuuntauksen vuoksi vuosi vuodelta, toiset ehdottavat tyytymistä 1 TB:n levyyn, joka pitäisi riittää yhdeksi tai kahdeksi vuodeksi, väittäen, että siihen mennessä kun se tulee vanhentuneeksi, 2 TB:n mallien hinta on todennäköisesti laskenut. Valinta riippuu siis henkilökohtaisista mieltymyksistäsi. Jos aiot pitää RoninDojo:si merkittävän ajan ja haluat välttää teknisen käsittelyn tulevina vuosina, 2 TB:n SSD:n vaihtoehto vaikuttaa järkevimmältä, sillä se tarjoaa sinulle mukavan varan tulevaisuuteen.

Lisäksi tarvitset erilaisia pieniä komponentteja:
- Kotelo, jossa on tuuletin Raspberry Pi:lle ja tallennuslaajennuskortillesi. Verkossa on saatavilla sarjoja, jotka sisältävät sekä SSD-laajennuskortin että yhteensopivan kotelon;
- Virtajohto Raspberry Pi:lle;
- Vähintään 16 GB:n micro SD -kortti (vaikka teknisesti 8 GB voisi riittää, 8 ja 16 GB:n korttien hintaero on usein merkityksetön);
- RJ45 Ethernet-kaapeli verkkoyhteyttä varten.

![node material](assets/notext/2.webp)

## Kuinka koota Raspberry Pi 4?
Solmusi kokoaminen vaihtelee valitsemasi laitteiston mukaan, erityisesti kotelon tyypin osalta. Kuitenkin yleinen vaiheiden rakenne pysyy suurin piirtein samanlaisena kokoamisessa.
Aloita asentamalla SSD tallennuslaajennuskorttiin, varmistaen, että kiinnität kaksi lukitusruuvia takana.

![assembly1](assets/notext/3.webp)

Kiinnitä sitten Raspberry Pi laajennuskorttiin.

![assembly2](assets/notext/4.webp)

Kiinnitä myös tuuletin Raspberry Pi:hin.

![assembly3](assets/notext/5.webp)

Yhdistä eri komponentit, kiinnittäen huomiota oikeiden nastojen käyttöön, viitaten kotelosi manuaaliin. Kotelovalmistajat tarjoavat usein video-oppaita auttaakseen sinua kokoamisessa. Minun tapauksessani minulla on lisälaajennuskortti, jossa on on/off-kytkin. Tämä ei ole välttämätön Bitcoin-solmun tekemiseen. Käytän sitä pääasiassa saadakseni virtapainikkeen.

Jos sinulla, kuten minulla, on laajennuskortti, jossa on on/off-kytkin, älä unohda asentaa pientä "Auto Power On" -hyppääjää. Tämä mahdollistaa solmusi automaattisen käynnistymisen heti, kun se saa virtaa. Tämä ominaisuus on erityisen hyödyllinen sähkökatkoksen sattuessa, sillä se mahdollistaa solmusi itsestään uudelleenkäynnistymisen ilman manuaalista toimenpidettä puoleltasi.

![assembly4](assets/notext/6.webp)

Ennen kaiken laitteiston asettamista koteloon on tärkeää tarkistaa Raspberry Pi:n, tallennuslaajennuskortin ja tuulettimen oikea toiminta kytkeessä ne päälle.

![assembly5](assets/notext/7.webp)
Lopuksi asenna Raspberry Pi sen koteloon. Huomioi, että myöhemmässä vaiheessa sinun tulee lisätä mikro-SD-kortti sopivaan porttiin Raspberry Pi:ssä. Jos kotelossasi on aukko, joka mahdollistaa SD-kortin lisäämisen avaamatta sitä (kuten omassani kuvassa esitetään), voit sulkea kotelon nyt. Jos kotelossasi ei kuitenkaan ole suoraa pääsyä mikro-SD-porttiin, sinun tulee odottaa kunnes olet valmistellut mikro-SD-kortin ja lisätä sen ennen kokoonpanon viimeistelyä.
![assembly6](assets/notext/8.webp)

## Miten asentaa RoninDojo v2 Raspberry Pi 4:ään?

### Vaihe 1: Valmistele käynnistettävä mikro-SD
Kun olet koonnut laitteistosi, seuraava vaihe on asentaa RoninDojo. Tätä varten valmistamme käynnistettävän mikro-SD-kortin tietokoneellasi polttamalla sopivan levykuvan sille.
Sinun tulee käyttää _**Raspberry Pi Imager**_ -ohjelmistoa, joka on suunniteltu käyttöjärjestelmien lataamisen, määrittämisen ja kirjoittamisen helpottamiseen mikro-SD-kortille käytettäväksi Raspberry Pi:n kanssa. Aloita asentamalla tämä ohjelmisto henkilökohtaiseen tietokoneeseesi:
- Ubuntu/Debianille: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Windowsille: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Macille: https://downloads.raspberrypi.org/imager/imager_latest.dmg

Kun ohjelmisto on asennettu, avaa se ja työnnä mikro-SD-korttisi henkilökohtaiseen tietokoneeseesi. Raspberry Pi Imager -käyttöliittymästä valitse `CHOOSE OS`:

![choose OS](assets/notext/9.webp)

Seuraavaksi siirry `Raspberry Pi OS (other)` -valikkoon:

![choose OS others](assets/notext/10.webp)

Valitse käyttöjärjestelmä nimeltä `Raspberry Pi OS (Legacy, 64-bit) Lite`, jonka koko on `0.3 GB`:

![choose OS Legacy Lite](assets/notext/11.webp)

Käyttöjärjestelmän valinnan jälkeen sinut ohjataan takaisin Raspberry Pi Imagerin päävalikkoon. Klikkaa `CHOOSE STORAGE`:

![choose storage](assets/notext/12.webp)

Valitse mikro-SD-korttisi:

![choose micro sd](assets/notext/13.webp)

Käyttöjärjestelmän ja mikro-SD-kortin valinnan jälkeen klikkaa `NEXT`:

![choose next](assets/notext/14.webp)

Uusi ikkuna ilmestyy. Valitse `EDIT CONFIGURATION`:

![edit settings](assets/notext/15.webp)

Tässä ikkunassa siirry `GENERAL`-välilehteen ja tee seuraavat asetukset (jotka ovat erittäin tärkeitä sen toiminnan kannalta):
- Ota käyttöön vaihtoehto ja anna `RoninDojo` isäntänimenä;
- Ota käyttöön `Set username and password`, syötä `pi` käyttäjänimenä, valitse salasana ja merkitse tämä tieto muistiin, sillä sitä tarvitaan myöhemmin. Nämä tunnistetiedot ovat väliaikaisia ja ne poistetaan myöhemmin;
- Poista käytöstä `Configure Wi-Fi`;
- Ota käyttöön `Set locale settings` ja valitse aikavyöhykkeesi sekä näppäimistötyyppi, joka vastaa tietokonettasi;

![general settings](assets/notext/16.webp)

SERVICES-välilehdessä, klikkaa `Enable SSH` ruutua ja valitse `Use a password for authentication`:

![services settings](assets/notext/17.webp)

Varmista myös, että `OPTIONS`-välilehdessä telemetria on poistettu käytöstä:

![options settings](assets/notext/18.webp)

Klikkaa `SAVE`:
![asetukset tallenna](assets/notext/19.webp)Vahvista klikkaamalla `KYL` aloittaaksesi käynnistyskelpoisen micro SD -kortin luomisen:
![asetukset kyllä](assets/notext/20.webp)

Viesti ilmoittaa, että kaikki tiedot micro SD -kortilla poistetaan. Vahvista klikkaamalla `KYL` aloittaaksesi prosessin:

![kirjoita uudelleen micro SD](assets/notext/21.webp)

Odota kunnes ohjelmisto on valmis valmistelemaan micro SD -korttiasi:

![kirjoittaa micro SD](assets/notext/22.webp)

Kun viesti prosessin päättymisestä ilmestyy, voit poistaa micro SD -kortin tietokoneestasi:

![kirjoittaminen micro SD valmis](assets/notext/23.webp)

### Vaihe 2: Viimeistele solmun kokoaminen
Voit nyt asettaa micro SD -kortin sopivaan porttiin Raspberry Pi:ssäsi.

![micro SD](assets/notext/24.webp)

Yhdistä sen jälkeen Raspberry Pi reitittimeesi Ethernet-kaapelilla. Lopuksi, käynnistä solmusi yhdistämällä virtajohto ja painamalla virtapainiketta (jos asetukseesi kuuluu sellainen).

### Vaihe 3: Muodosta SSH-yhteys solmuun
Ensiksi, on tarpeen löytää solmusi IP-osoite. Voit käyttää työkalua kuten _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ tai _[Angry IP Scanner](https://angryip.org/)_, tai tarkistaa reitittimesi hallintaliittymän. IP-osoitteen tulisi olla muodossa `192.168.1.??`. **Kaikissa seuraavissa komennossa korvaa `[IP]` todellisella solmusi IP-osoitteella**, (poistaen hakasulkeet).

Käynnistä terminaali.

Poistaaksesi mahdollisen jo IP-osoitteeseen liitetyn avaimen, suorita komento: 
`ssh-keygen -R [IP]`. 

Virhe tämän komennon jälkeen ei ole vakava; se yksinkertaisesti tarkoittaa, että avainta ei ole listallasi tunnetuista isännöistä (mikä on melko todennäköistä). Esimerkiksi, jos solmusi IP on `192.168.1.40`, komento muuttuu: `ssh-keygen -R 192.168.1.40`.

Seuraavaksi, muodosta SSH-yhteys solmuusi suorittamalla komento: 
`ssh pi@[IP]`.
Viesti isännän aitouden vahvistamisesta ilmestyy: `Isännän '[IP]' aitoutta ei voida vahvistaa.` Tämä osoittaa, että yritettävän yhdistää olevan laitteen aitoutta ei voida varmistaa, koska tunnettua julkista avainta ei ole. Kun yhdistetään SSH:n kautta uuteen isäntään ensimmäistä kertaa, tämä viesti ilmestyy aina. Sinun on vastattava `kyllä` lisätäksesi sen julkisen avaimen paikalliseen hakemistoosi, mikä estää tämän varoitusviestin ilmestymisen tulevissa SSH-yhteyksissä tähän solmuun. Kirjoita siis `kyllä` ja paina `enter` vahvistaaksesi.
Sinulta pyydetään sen jälkeen syöttämään salasanasi, se joka asetettiin aiemmin väliaikaiseksi vaiheessa 1. Vahvista painamalla `enter`. Olet nyt yhteydessä solmuusi SSH:n kautta.

Yhteenvetona, tässä ovat suoritettavat komennot:
- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `kyllä`
- Syötä väliaikainen salasana ja vahvista.

### Vaihe 4: Päivitys ja valmistelu
Olet nyt yhteydessä solmuusi SSH-istunnon kautta. Terminaalissasi komentokehote pitäisi olla: `pi@RoninDojo:~ $`. Aloittaaksesi, päivitä saatavilla olevien pakettien luettelo ja asenna päivityksiä olemassa oleville paketeille seuraavalla komennolla:
`sudo apt update && sudo apt upgrade -y`
Kun päivitykset on saatu päätökseen, jatka asentamalla *Git* ja *Dialog* komennolla: `sudo apt install git dialog -y`

Seuraavaksi, kloonaa `master` haara _RoninOS_ Git-repositoriosta suorittamalla:
`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`

Suorita skripti `customize-image.sh` komennolla:
`cd /opt/RoninOS/ && sudo ./customize-image.sh`

**On tärkeää antaa skriptin suorittaa loppuun keskeytyksettä ja odottaa kärsivällisesti sen prosessin päättymistä**, mikä kestää noin 10 minuuttia. Kun viesti `Setup is complete` ilmestyy, voit siirtyä seuraavaan vaiheeseen.

### Vaihe 5: RoninOS:n käynnistäminen
Käynnistä RoninOS komennolla:
`sudo systemctl start ronin-setup`

Näytä lokitiedoston rivit komennolla:
`tail -f /home/ronindojo/.logs/setup.logs`

Tässä vaiheessa **on tärkeää antaa RoninOS:n käynnistyä ja odottaa sen** suorituksen päättymistä. Tämä kestää noin 40 minuuttia. Kun `All RoninDojo feature installations complete!` ilmestyy, voit siirtyä vaiheeseen 6.

### Vaihe 6: RoninUI:n käyttöönotto ja tunnusten vaihtaminen
Asennuksen päätyttyä, jotta voit yhdistää solmuusi selaimen kautta, varmista, että henkilökohtainen tietokoneesi on yhdistetty samaan paikalliseen verkkoon kuin solmusi. Jos käytät VPN:ää koneellasi, poista se väliaikaisesti käytöstä. Päästäksesi solmun käyttöliittymään selaimessasi, syötä URL-kenttään:
- Suoraan solmusi IP-osoite, esimerkiksi, `192.168.1.??`;
- Tai kirjoita `ronindojo.local`.

RoninUI:n kotisivulla sinua pyydetään aloittamaan asetusten määrittäminen. Tee tämä napsauttamalla `Let's start` -painiketta.

![lets start](assets/notext/25.webp)

Tässä vaiheessa RoninUI esittelee sinulle `root` salasanasi. On olennaista pitää se turvassa. Voit valita fyysisen varmuuskopion, paperille, tai tallentaa sen [salasananhallintaohjelmaan](https://planb.network/courses/secu101/4/2).

![root password](assets/notext/26.webp)

`Root` salasanan tallentamisen jälkeen, merkitse ruutu `I have backed up Root user credentials` ja napsauta `Continue` jatkaaksesi.

![confirm root password](assets/notext/27.webp)

Seuraavassa vaiheessa luodaan käyttäjän salasana, jota käytetään sekä RoninUI-verkkoliittymään pääsyyn että SSH-istuntojen muodostamiseen solmuusi. Valitse vahva salasana ja varmista, että tallennat sen turvallisesti. Sinun on syötettävä tämä salasana kahdesti ennen kuin napsautat `Finish` vahvistaaksesi. Käyttäjänimen osalta suositellaan pitämään oletusvalinta, `ronindojo`. Jos päätät vaihtaa sitä, muista säätää seuraavien vaiheiden komentoja vastaavasti.

![user credentials](assets/notext/28.webp)

Kun nämä toimenpiteet on suoritettu, odota, että solmusi alustaa. Sen jälkeen pääset RoninUI-verkkoliittymään. Olet melkein prosessin lopussa, vain muutama pieni vaihe jäljellä!
![Ronin UI](assets/notext/29.webp)

### Vaihe 7: Väliaikaisten tunnusten poistaminen
Avaa uusi terminaali henkilökohtaisella tietokoneellasi ja muodosta SSH-yhteys solmuusi seuraavalla komennolla:
`SSH ronindojo@[IP]`
Jos esimerkiksi solmusi IP-osoite on `192.168.1.40`, sopiva komento on: `SSH ronindojo@192.168.1.40`

Jos vaihdoit käyttäjänimesi edellisessä vaiheessa, korvaten oletuskäyttäjänimen (`ronindojo`) toisella, varmista että käytät tätä uutta nimeä komennossa. Esimerkiksi, jos valitsit käyttäjänimeksi `planb` ja IP-osoite on `192.168.1.40`, komento on:
`SSH planb@192.168.1.40`
Sinua pyydetään syöttämään käyttäjän salasana. Syötä se ja paina `enter` vahvistaaksesi. Tämän jälkeen pääset RoninCLI-käyttöliittymään. Käytä näppäimistösi nuolinäppäimiä navigoidaksesi `Exit RoninDojo` -vaihtoehtoon ja paina `enter` valitaksesi sen.
![RoninCLI](assets/notext/30.webp)

Tässä vaiheessa olet solmusi terminaalissa, komentokehotteen ollessa samankaltainen kuin: `ronindojo@RoninDojo:~ $`. Poistaaksesi väliaikaisen käyttäjän, joka luotiin käynnistettävän mikro SD-kortin konfiguroinnin aikana, syötä seuraava komento ja paina `enter`:
`sudo deluser --remove-home pi`

Sinua pyydetään vahvistamaan käyttäjän salasana. Syötä se ja vahvista painamalla `enter`. Odota toimenpiteen valmistumista, sitten käytä `exit`-komentoa poistuaksesi terminaalista.

Onnittelut! RoninDojo v2 -solmusi on nyt konfiguroitu ja valmis käytettäväksi. Se aloittaa IBD:n (*Initial Block Download*), jatkaen Bitcoin-lohkoketjun lataamista ja varmistamista Genesis-lohkosta lähtien. Tämä vaihe sisältää kaikkien Bitcoin-siirtojen noutamisen tammikuun 3. päivästä 2009 lähtien ja vie jonkin aikaa. Kun lohkoketju on täysin ladattu, indeksoija jatkaa tietokannan tiivistämistä. IBD:n kesto voi vaihdella huomattavasti. RoninDojo-solmusi on täysin toiminnallinen, kun tämä prosessi on saatu päätökseen.

**Jos olet siirtymässä vanhasta RoninDojo v1 -solmusta** tähän uuteen versioon tätä opasta käyttäen säilyttäen saman SSD:n, solmusi pitäisi automaattisesti havaita ja uudelleenkäyttää levyllä olevat olemassa olevat tiedot, säästäen sinut IBD:n suorittamisen tarpeesta. Tässä tapauksessa sinun tarvitsee vain odottaa, että solmusi synkronoituu uusimpien lohkojen kanssa.

### Vaihe 8: "veth* korjaus"
Jos kohtaat bugin RoninDojo v2:ssa Raspberry Pilla, jossa asennuksen jälkeen solmusi yhtäkkiä muuttuu SSH:n kautta tavoittamattomaksi, mutta palautuu yksinkertaisen uudelleenkäynnistyksen jälkeen, sinun tulee noudattaa tätä vaihetta 8. Tämä yleinen bugi voidaan helposti korjata yhteisön kehittämällä ratkaisulla: "_veth korjaus_". Tämä pieni korjaus poistaa äkilliset katkokset pysyvästi. Näin voit soveltaa sitä.

Avaa uusi terminaali henkilökohtaisella tietokoneellasi ja muodosta SSH-yhteys solmuusi käyttäen seuraavaa komentoa:
`SSH ronindojo@[IP]`

Jos esimerkiksi solmusi IP-osoite on `192.168.1.40`, sopiva komento olisi:
`SSH ronindojo@192.168.1.40`

Sinua pyydetään syöttämään käyttäjän salasana. Syötä se ja paina `enter` vahvistaaksesi. Tämän jälkeen pääset RoninCLI-käyttöliittymään. Käytä näppäimistösi nuolia navigoidaksesi `Exit RoninDojo` -vaihtoehtoon ja paina `enter` valitaksesi sen.
Tässä vaiheessa olet solmusi terminaalissa, komentokehotteen ollessa samankaltainen kuin: `ronindojo@RoninDojo:~ $`. Sovellaksesi veth*-korjauksen, kirjoita seuraava komento ja paina `enter`: `sudo nano /etc/dhcpcd.conf`

Vahvista salasanasi uudelleen ja paina `enter`.

Saavut `dhcpcd.conf` tiedostoon. Sinun täytyy kopioida seuraava teksti, varmistaen että sisällytät tähtimerkin, ja lisätä se tiedoston loppuun:
`denyinterfaces veth*`

Tehdäksesi tämän, siirry tiedoston loppuun käyttäen näppäimistösi alanuolta, sitten käytä hiiren oikeaa klikkausta liittääksesi tekstin omalle rivilleen.

Tekstin lisäämisen jälkeen, paina `ctrl X` aloittaaksesi poistumisen, seuraa `ctrl Y` vahvistaaksesi muutosten tallentamisen, ja paina `enter` viimeistelläksesi ja palataksesi komentokehotteeseen. Varmistaaksesi, että muutos on sovellettu oikein, avaa `dhcpcd.conf` tiedosto uudelleen käyttäen asianmukaista komentoa.

Korjauksen soveltamisen viimeistelemiseksi, käynnistä solmusi uudelleen suorittamalla:
`sudo reboot now`

Tässä vaiheessa voit sulkea terminaalisi. Anna tarvittava aika RoninDojosi uudelleenkäynnistykselle, jonka jälkeen sinun pitäisi pystyä yhdistämään uudelleen selaimen graafisen käyttöliittymän kautta. Tämä prosessi pitäisi korjata kohdattu bugi.

## Kuinka käyttää RoninDojo v2 solmuasi?

### Lompakkosoftasi yhdistäminen Electrsiin
Ensimmäinen käyttökertasi vasta asennetulla ja synkronoidulla solmullasi tulee olemaan transaktioidesi lähettäminen Bitcoin-verkkoon. Haluat todennäköisesti yhdistää erilaiset lompakkosi solmuusi lähettääksesi transaktiosi luottamuksellisesti. Voit tehdä tämän Electrum Rust Serverin (electrs) kautta. Tämä sovellus on yleensä esiasennettuna RoninDojo solmullesi. Jos ei, voit asentaa sen manuaalisesti RoninCLI käyttöliittymän kautta `Applications > Manage Applications > Install Electrum Server`.

Saadaksesi Electrum Serverisi Tor-osoitteen, RoninUI web-käyttöliittymästä, mene kohtaan:
`Pairing > Electrum server > Pair now`
![Pairing](assets/notext/31.webp)
![Electrs](assets/notext/32.webp)
Sinun täytyy sitten syöttää `Hostname`-osoite, joka päättyy `.onion` lompakkosoftaasi, portin `50001` kanssa. ![hostname](assets/notext/33.webp)
Esimerkiksi Sparrow Walletissa, mene vain välilehteen:
`File > Preferences > Server > Private Electrum`

![Sparrow](assets/notext/34.webp)

### Lompakkosoftasi yhdistäminen Samourai Dojoon
Vaihtoehtona Electrsin käytölle, Dojo mahdollistaa yhteensopivan ohjelmistolompakkosi suoran yhdistämisen RoninDojo solmuusi. Lompakot kuten Samourai Wallet ja Sentinel tarjoavat tämän toiminnallisuuden.

Yhteyden muodostamiseksi sinun tarvitsee vain skannata Dojosi QR-koodi. Päästäksesi tähän QR-koodiin RoninUI:n kautta, navigoi kohtaan:
`Pairing > Samourai Dojo > Pair now`
![Samourai Dojo](assets/notext/35.webp)
Yhdistääksesi Samourai Walletisi Dojoosi, skannaa tämä QR-koodi sovelluksen asennuksen aikana:

![Samourai Wallet connection](assets/notext/36.webp)
Jos sinulla oli jo Samourai Wallet ennen Ronin Dojon asentamista, on tarpeen varmuuskopioida lompakkosi, poistaa ja sitten asentaa Samourai Wallet -sovellus uudelleen ennen lompakkosi palauttamista. Käynnistäessäsi uudelleenasennetun sovelluksen, sinulla on mahdollisuus yhdistää uuteen Dojoon. **Ole varovainen, tässä prosessissa on riski menettää bitcoinsisi, jos sitä ei suoriteta oikein!** Varmista, että sinulla on Samourai-lompakkosi varmuuskopio tiedostoissasi ja tarkista tunnuslauseesi pätevyys kohdasta `Asetukset > Vianmääritys > Tunnuslause`. On myös tärkeää, että sinulla on luettavissa oleva varmuuskopio palautuslauseestasi ja tunnuslauseestasi. Tarkemman toiminnan varmistamiseksi on suositeltavaa seurata tätä yksityiskohtaista opasta: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).
### Oman Mempool.space-lohkoketjuselaimen käyttö
Lohkoketjuselain muuttaa Bitcoin-lohkoketjun raakatiedot rakenteelliseen ja helposti luettavaan muotoon. Työkalujen, kuten *Mempool.space*, avulla on mahdollista analysoida transaktioita, etsiä tiettyjä osoitteita tai jopa konsultoida verkon mempoolien keskimääräisiä maksutaksoja reaaliajassa.

Kuitenkin online-lohkoketjuselainten käyttöön liittyy riskejä yksityisyydellesi ja se edellyttää luottamusta kolmansien osapuolien tarjoamiin tietoihin. Todellakin, käyttämällä näitä palveluita omien nodien kautta kulkematta, saatat tahattomasti paljastaa tietoja transaktioistasi ja sinun on luotettava sivuston omistajan esittämän tiedon tarkkuuteen.
Näiden riskien lieventämiseksi suositellaan oman *Mempool.space*-instanssin käyttöä Tor-verkon kautta, suoraan isännöitynä nodellasi. Tämä ratkaisu varmistaa yksityisyytesi säilymisen ja tietojesi autonomian.
Tehdäksesi tämän, aloita asentamalla *Mempool Space Visualizer* RoninUI:sta. Verkkokäyttöliittymässä siirry `Dashboard`-välilehdelle ja klikkaa `Manage` alla `Mempool Space`:
`Dashboard > Mempool Space > Manage`
![Manage mempool](assets/notext/37.webp)
Klikkaa sitten `Install Mempool visualizer` -painiketta:
![install mempool](assets/notext/38.webp)
Vahvista käyttäjäsalasanasi:
![password mempool](assets/notext/39.webp)
Odota asennuksen valmistumista, klikkaa sitten uudelleen `Manage`-painiketta:
![Mempool Manage](assets/notext/40.webp)
Saat `.onion`-linkin päästäksesi omaan *Mempool.space*-instanssiisi Tor-verkon kautta.
![Mempool link](assets/notext/41.webp)
Neuvon sinua tallentamaan tämän linkin suosikkeihisi Tor-selaimessa tai lisäämään sen Tor Browser -sovellukseen älypuhelimellasi, jotta pääset siihen helposti ja turvallisesti mistä tahansa. Jos sinulla ei vielä ole Tor-selainta, voit ladata sen täältä: [https://www.torproject.org/download/](https://www.torproject.org/download/)
![Mempool Tor](assets/notext/42.webp)

### Whirlpoolin käyttäminen bitcoiniesi sekoittamiseen
RoninDojo-nodesi integroi myös _WhirlpoolCLI_:n, komentorivikäyttöliittymän, joka mahdollistaa Whirlpool-coinjoinien automatisoinnin, ja _WhirlpoolGUI_:n, graafisen käyttöliittymän, joka on suunniteltu toimimaan yhdessä _WhirlpoolCLI_:n kanssa.
Coinjoinin suorittaminen Whirlpoolin kautta vaatii, että käytössä oleva sovellus on aktiivinen remixien suorittamiseksi. Tämä ehto voi olla rajoittava niille, jotka haluavat saavuttaa korkeita anonset-tasoja. Todellakin, laitteen, joka isännöi Whirlpoolia integroivaa sovellusta, on pysyttävä päällä jatkuvasti. Tämä tarkoittaa, että osallistuaksesi remixeihin 24 tuntia vuorokaudessa, tietokoneesi tai älypuhelimesi on pysyttävä päällä Samourain tai Sparrown ollessa avoinna jatkuvasti. Ratkaisu tähän rajoitteeseen on käyttää _WhirlpoolCLI_:tä koneella, joka on aina päällä, kuten Bitcoin-noodilla, mahdollistaen kolikkojesi remixauksen keskeytyksettä, ilman tarvetta pitää toista laitetta päällä.
Yksityiskohtainen opas on valmisteilla, joka opastaa sinut askel askeleelta läpi prosessin coinjoinin suorittamisesta Samourai Walletin ja RoninDojo v2:n kanssa, A:sta Z:aan.

Syvemmän ymmärryksen saamiseksi coinjoinista ja sen käytöstä Bitcoinissa, kutsun sinut myös tutustumaan tähän toiseen artikkeliin: Ymmärtäminen ja coinjoinin käyttö Bitcoinissa, jossa kerron kaiken mitä sinun tarvitsee tietää tästä tekniikasta.

https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2
### Whirlpool Stat Toolin (WST) käyttö

Suoritettuasi coinjoineja Whirlpoolin kanssa, on hyödyllistä arvioida tarkasti saavutettu yksityisyyden taso sekoitetuille UTXO:illesi. Tätä varten voit käyttää Python-työkalua *Whirlpool Stat Tool*. Tämä työkalu mahdollistaa sekä tulevien että menneiden anonset-pisteiden mittaamisen, samalla kun se analysoi niiden leviämistä altaassa.

Syvemmän ymmärryksen saamiseksi näiden anonsettien laskentamekanismeista suosittelen lukemaan artikkelin: REMIX - WHIRLPOOL, joka yksityiskohtaisesti käsittelee näiden indeksien toimintaa.

https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



Päästäksesi WST-työkaluun, siirry RoninCLI:hin. Tee tämä avaamalla terminaali henkilökohtaisella tietokoneellasi ja muodostamalla SSH-yhteys noodisi kanssa seuraavalla komennolla:
`SSH ronindojo@[IP]`

Jos esimerkiksi noodisi IP-osoite on `192.168.1.40`, sopiva komento olisi:
`SSH ronindojo@192.168.1.40`

Jos vaihdoit käyttäjänimesi vaiheessa 6, korvaten oletuskäyttäjänimen (`ronindojo`) toisella, varmista että käytät tätä uutta nimeä komennossa. Esimerkiksi, jos valitsit käyttäjänimeksi `planb` ja IP-osoite on `192.168.1.40`, komento, jonka syötät olisi:
`SSH planb@192.168.1.40`

Sinua pyydetään syöttämään käyttäjän salasana. Anna se ja paina `enter` vahvistaaksesi. Tämän jälkeen pääset RoninCLI-käyttöliittymään. Käytä näppäimistösi nuolinäppäimiä navigoidaksesi `Samourai Toolkit` -valikkoon ja paina `enter` valitaksesi sen:

![Samourai Toolkit](assets/notext/43.webp)

Valitse sitten `Whirlpool Stat Tool`:

![WST](assets/notext/44.webp)

WST:n alustamisen yhteydessä työkalu aloittaa automaattisen asennuksen. Odota tämän vaiheen ajan. Käyttöohjeet vierivät näytöllä. Kun asennus on valmis, paina mitä tahansa näppäintä päästäksesi WST-terminaaliin:

![WST komentorivi](assets/notext/45.webp)

Seuraava komentokehote näytetään:
`wst#/tmp>`

Jos haluat poistua tästä käyttöliittymästä ja palata RoninCLI-valikkoon, kirjoita yksinkertaisesti:
`quit`

Ensin on tarpeen määrittää proxy käyttämään Toria, varmistaaksesi luottamuksellisuuden kun haet tietoja OXT:stä. Kirjoita komento:
`socks5 127.0.0.1:9050`
Tämän jälkeen jatka lataamalla allastiedot, jotka sisältävät transaktiosi:
`download 0001`
Korvaa `0001` kiinnostuksesi kohteen altaan tunnuskoodilla. Altaiden tunnuskoodit ovat seuraavat WST:ssä:
- Allas 0.5 bitcoineja: `05`
- Allas 0.05 bitcoineja: `005`
- Allas 0.01 bitcoineja: `001`
- Allas 0.001 bitcoineja: `0001`

Ladattuasi tiedot, lataa data korvaamalla `0001` altaasi koodilla tässä komennossa: `load 0001`

![WST lataus](assets/notext/46.webp)

Odota latauksen valmistumista, mikä saattaa kestää muutaman minuutin. Kun data on ladattu, suorita komento `score` seurattuna TXID:lläsi (ilman hakasulkeita) saadaksesi kolikkosi anonset-pisteet:
`score [TXID]`

![WST pisteet](assets/notext/47.webp)

WST näyttää tämän jälkeen retrospektiivisen pistemäärän (_Takautuvat mittarit_), jonka jälkeen tulee prospektiivinen pistemäärä (_Eteenpäin katsovat mittarit_). Anonset-pisteiden lisäksi WST näyttää myös transaktiosi diffuusioasteen altaassa suhteessa sen anonsetiin.

**On tärkeää huomata, että kolikkosi prospektiivinen pistemäärä tulee laskea alkuperäisen sekoituksesi TXID:stä, ei viimeisimmästä sekoituksestasi. Toisaalta UTXO:n retrospektiivinen pistemäärä lasketaan viimeisen kierroksen TXID:stä.**

### Boltzmann-laskimen käyttäminen
Boltzmann-laskin on työkalu Bitcoin-transaktion analysointiin, joka tarjoaa mahdollisuuden mitata sen entropiatasoa muiden edistyneiden mittareiden joukossa. Nämä tiedot tarjoavat kvantifioidun arvion transaktion yksityisyydestä ja auttavat tunnistamaan mahdolliset puutteet. Tämä työkalu on jo integroitu RoninDojo-noodiisi, mikä tekee sen käytöstä helppoa ja saavutettavaa.

Ennen Boltzmann-laskimen käyttömenetelmän yksityiskohtien esittämistä on tärkeää ymmärtää näiden indikaattorien merkitys, niiden laskentatapa ja hyödyllisyys. Vaikka nämä indikaattorit soveltuvat mihin tahansa Bitcoin-transaktioon, ne ovat erityisen hyödyllisiä coinjoin-transaktion laadun arvioimisessa.

**Ensimmäinen indikaattori**, jonka ohjelmisto laskee, on mahdollisten yhdistelmien kokonaismäärä, joka on merkitty `nb combinations` työkalussa. UTXO:iden arvojen perusteella tämä indikaattori kvantifioi tapoja, joilla syötteitä voidaan yhdistää tulosteisiin. Toisin sanoen, se määrittää kuinka monta uskottavaa tulkintaa transaktio voi tuottaa. Esimerkiksi Whirlpool 5x5 -mallin mukaisesti rakennettu coinjoin esittää `1496` mahdollista yhdistelmää:
![yhdistelmät](assets/notext/50.webp)
Lähde: KYCP

**Toinen laskettava indikaattori** on transaktion entropia, joka on merkitty `Entropy`. Kun transaktiolla on suuri määrä mahdollisia yhdistelmiä, on usein relevantimpaa viitata sen entropiaan. Tämä määritellään mahdollisten yhdistelmien lukumäärän binäärilogaritmina. Tässä on käytetty kaava:
- $E$: transaktion entropia;
- $C$: transaktion mahdollisten yhdistelmien lukumäärä.
$$E = \log_2(C)$$
Matematiikassa binäärilogaritmi (kantaluku 2 logaritmi) vastaa käänteistoimintoa, kun 2 nostetaan johonkin potenssiin. Toisin sanoen, $x$:n binäärilogaritmi on eksponentti, johon 2 on nostettava saadakseen $x$. Siksi tämä indikaattori ilmaistaan bitteinä. Otetaan esimerkki entropian laskemisesta kolikoiden yhdistämistapahtumalle, joka on rakennettu Whirlpool 5x5 -mallin mukaisesti, ja kuten aiemmin mainittiin, tarjoaa `1496` mahdollista yhdistelmää:$$ C = 1496 $$
$$ E = \log_2(1496) $$
$$ E \approx 10.5469 \text{ bittiä}$$

Näin ollen tämän kolikoiden yhdistämistapahtuman entropia on 10.5469 bittiä, mikä katsotaan erittäin tyydyttäväksi. Mitä korkeampi tämä arvo on, sitä enemmän erilaisia tulkintoja tapahtuma sallii, parantaen näin sen yksityisyyden tasoa.

Otetaan lisäesimerkki tavanomaisemmasta tapahtumasta, jossa on yksi sisääntulo ja kaksi ulostuloa: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)
Tässä tapauksessa ainoa mahdollinen tulkinta on: `(inp 0) > (Outp 0 ; Outp 1)`. Näin ollen sen entropia on vahvistettu arvoon `0`:
$$ C = 1 $$
$$ E = \log_2(1) $$
$$ E \approx 0 \text{ bittiä}$$
**Kolmas indikaattori**, jonka Boltzmann-laskin tarjoaa, on nimeltään `Lompakon Tehokkuus`. Tämä indikaattori arvioi tapahtuman tehokkuutta vertaamalla sitä optimaaliseen tapahtumaan samassa asetelmassa. Tämä johtaa meidät keskustelemaan maksimaalisen entropian käsitteestä, joka vastaa korkeinta entropiaa, jonka tietty tapahtumarakenne voi teoreettisesti saavuttaa. Näin ollen Whirlpool 5x5 -kolikoiden yhdistämistapahtuman maksimaalinen entropia on asetettu arvoon `10.5469`. Tapahtuman tehokkuus lasketaan sitten vertaamalla tätä maksimaalista entropiaa analysoitavan tapahtuman todelliseen entropiaan. Käytetty kaava on seuraava:
- $ER$: tapahtuman todellinen entropia, ilmaistuna bitteinä;
- $EM$: tietyn tapahtumarakenteen mahdollinen maksimaalinen entropia, myös bitteinä;
- $Ef$: tapahtuman tehokkuus, bitteinä.
$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$
$$Ef = 0 \text{ bittiä}$$

Tämä indikaattori ilmaistaan myös prosentteina, sen kaava on silloin:
- $CR$: todellisten mahdollisten yhdistelmien määrä;
- $CM$: saman rakenteen mahdollisten yhdistelmien maksimimäärä;
- $Ef$: tehokkuus ilmaistuna prosentteina.
$$Ef = \frac{CR}{CM}$$
$$Ef = \frac{1496}{1496}$$
$$Ef = 100\%$$

Tehokkuus `100%` siis osoittaa, että tapahtuma maksimoi yksityisyyden potentiaalinsa perustuen sen rakenteeseen.
**Neljäs indikaattori**, entropian tiheys eli `Entropy Density`, tarjoaa näkökulman entropiaan suhteutettuna jokaiseen siirron syötteeseen tai tulosteeseen. Tämä indikaattori on hyödyllinen siirtojen tehokkuuden arvioimisessa ja eri kokoisten siirtojen vertailussa. Sen laskemiseksi jaa yksinkertaisesti siirron kokonaisentropia syötteiden ja tulosteiden kokonaismäärällä. Otetaan esimerkiksi Whirlpool 5x5 coinjoin:
- $ED$: entropian tiheys ilmaistuna bitteinä;
- $E$: siirron entropia ilmaistuna bitteinä;
- $T$: siirron syötteiden ja tulosteiden kokonaismäärä.
$$T = 5 + 5 = 10$$
$$ED = \frac{E}{T}$$
$$ED = \frac{10.5469}{10}$$
$$ED = 1.054 \text{ bittiä}$$
**Viides tieto**, jonka Boltzmann-laskin tarjoaa, on syötteiden ja tulosteiden välisen vastaavuuden todennäköisyyksien taulukko. Tämä taulukko osoittaa `Boltzmann-pisteytyksen` kautta todennäköisyyden, että tietty syöte on yhteydessä tiettyyn tulosteeseen. Ottaen esimerkiksi Whirlpool coinjoinin, todennäköisyystaulukko korostaisi kunkin syötteen ja tulosteen välisen yhteyden mahdollisuuksia, tarjoten kvantitatiivisen mittarin siirron yhteyksien epämääräisyydelle tai ennustettavuudelle:

| %       | Tuloste 0 | Tuloste 1 | Tuloste 2 | Tuloste 3 | Tuloste 4 |
|---------|-----------|-----------|-----------|-----------|-----------|
| Syöte 0 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Syöte 1 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Syöte 2 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Syöte 3 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Syöte 4 | 34%       | 34%       | 34%       | 34%       | 34%       |

Tässä on selvää, että jokaisella syötteellä on yhtäläinen mahdollisuus olla yhteydessä mihin tahansa tulosteeseen, mikä vahvistaa siirron epämääräisyyttä ja luottamuksellisuutta. Kuitenkin yksinkertaisessa siirrossa, jossa on yksi syöte ja kaksi tulostetta, tilanne on erilainen:

| %       | Tuloste 0 | Tuloste 1 |
|---------|-----------|-----------|
| Syöte 0 | 100%      | 100%      |

Tässä näemme, että kummankin tulosteen todennäköisyys tulla syötteestä 0 on 100%. Pienempi todennäköisyys siis tarkoittaa suurempaa luottamuksellisuutta, hajottamalla suorat yhteydet syötteiden ja tulosteiden välillä.

**Kuudes tieto** on determinististen linkkien määrä, täydennettynä näiden linkkien suhteella. Tämä indikaattori paljastaa, kuinka monta yhteyttä analysoitavan siirron syötteiden ja tulosteiden välillä on kiistattomia, 100% todennäköisyydellä. Suhde puolestaan tarjoaa näkökulman näiden determinististen linkkien painoarvoon siirron kokonaislinkkien sisällä.

Esimerkiksi Whirlpool-tyyppisessä coinjoin-siirrossa ei ole deterministisiä linkkejä, ja siksi näyttää indikaattorin ja suhteen 0%. Toisaalta toisessa tarkastellussa siirrossa (yhdellä syötteellä ja kahdella tulosteella) indikaattori on asetettu 2:een ja suhde saavuttaa 100%. Näin ollen nolla-indikaattori merkitsee erinomaista luottamuksellisuutta kiitos suorien ja kiistattomien linkkien puuttumisen syötteiden ja tulosteiden välillä.
**Kuinka pääset käsiksi Boltzmann-laskimeen RoninDojo:ssa?** Päästäksesi *Boltzmann-laskimen* työkaluun, siirry RoninCLI:hin. Tee tämä avaamalla terminaali henkilökohtaisella tietokoneellasi ja muodostamalla SSH-yhteys solmuusi käyttämällä seuraavaa komentoa: `SSH ronindojo@[IP]`

Jos esimerkiksi solmusi IP-osoite on `192.168.1.40`, sopiva komento olisi:
`SSH ronindojo@192.168.1.40`

Jos muutit käyttäjänimeäsi vaiheessa 6, korvaten oletuskäyttäjänimen (`ronindojo`) toisella, varmista että käytät tätä uutta nimeä komennossa. Esimerkiksi, jos valitsit käyttäjänimeksi `planb` ja IP-osoite on `192.168.1.40`, komento jonka syötät olisi:
`SSH planb@192.168.1.40`

Sinua pyydetään syöttämään käyttäjän salasana. Syötä se ja paina sitten `enter` vahvistaaksesi. Tämän jälkeen pääset RoninCLI-käyttöliittymään. Käytä näppäimistösi nuolia navigoidaksesi `Samourai Toolkit` -valikkoon ja paina `enter` valitaksesi sen:

![Samourai Toolkit](assets/notext/43.webp)

Valitse sitten `Boltzmann-laskin`:

![boltzmann](assets/notext/49.webp)

Saatavillesi avautuu ohjelmiston kotisivu:

![boltzmann home](assets/notext/51.webp)

Syötä tutkittavan transaktion TXID ja paina `enter`-näppäintä:

![boltzmann txid](assets/notext/52.webp)

Laskin tarjoaa sinulle kaikki aiemmin keskustellut indikaattorit:

![boltzmann result](assets/notext/53.webp)

### Muita ominaisuuksia RoninDojo v2:ssa
RoninDojo-solmusi integroi useita muita ominaisuuksia. Erityisesti sinulla on mahdollisuus skannata tiettyjä tietoja ottaaksesi ne huomioon. Esimerkiksi joskus Samourai-lompakkosi, joka on yhdistetty RoninDojoon, ei ehkä näytä hallussasi olevia bitcoineja. Jos saldo näyttää 0 vaikka olet varma, että sinulla on bitcoineja tässä lompakossa, useat syyt voivat selittää tämän tilanteen, kuten virhe johdannaispoluissa. Mutta yksi syy voi myös olla, että solmusi ei seuraa osoitteitasi asianmukaisesti. Tämän ongelman ratkaisemiseksi voit varmistaa, että solmusi todella seuraa `xpub`-osoitettasi käyttämällä _xpub-työkalua_. Päästäksesi tähän työkaluun RoninUI:n kautta, seuraa polkua:
`Huolto > XPUB-työkalu`

Syötä ongelmaa aiheuttava `xpub` ja napsauta `Tarkista`-painiketta tarkistaaksesi tämän tiedon:
![xpub tool](assets/notext/54.webp)
Varmista, että kaikki transaktiot on listattu asianmukaisesti. On myös tärkeää varmistaa, että käytetty johdannaispolkutyyppi vastaa lompakkosi tyyppiä. Jos näin ei ole, napsauta `Kirjoita uudelleen`, ja valitse sitten `BIP44`, `BIP49`, tai `BIP84` tarpeidesi mukaan.
RoninUI:n `Huolto`-välilehdellä on muitakin hyödyllisiä ominaisuuksia:
- *Transaktiotyökalu*: Mahdollistaa tietyn transaktion yksityiskohtien tutkimisen;
- *Osoitetyökalu*: Mahdollistaa tietyn osoitteen seurannan vahvistamisen Dojossasi;
- *Uudelleenskannaa lohkot*: Pakottaa solmusi suorittamaan uuden skannauksen määritellylle lohkoalueelle.

`Push Tx`-välilehti on toinen mielenkiintoinen ominaisuus RoninUI:ssa, joka mahdollistaa allekirjoitetun transaktion lähettämisen Bitcoin-verkkoon. Transaktio on syötettävä heksadesimaalimuodossa.
RoninUI-käyttöliittymäsi muiden välilehtien osalta:
- `Apps`: Isännöi Whirlpool-sovellusta ja tulee varmasti olemaan käytössä uusien sovellusten integroimiseen tulevaisuudessa;
- `Logs`: Tarjoaa reaaliaikaisen pääsyn ohjelmistosi tapahtumalokeihin;
- `System Info`: Tarjoaa yleistä tietoa solmustasi, kuten CPU:n lämpötilan, tallennustilan käytön tai RAM-tiedot. Löydät myös `Reboot` ja `Shut down` vaihtoehdot solmun uudelleenkäynnistämiseen tai sammuttamiseen;
- `Settings`: Mahdollistaa käyttäjäsalasanasi vaihtamisen.

Siinä se! Kiitos, että seurasit tätä opasta loppuun. Jos pidit siitä, kannustan jakamaan sitä sosiaalisessa mediassa. Lisäksi, jos sinulla on mahdollisuus, harkitse kehittäjien tukemista lahjoituksella, jotka tekevät nämä vapaat ja avoimen lähdekoodin ohjelmistot saataville yhteisöllemme: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). Syventääksesi tietämystäsi RoninDojosta ja löytääksesi lisää resursseja, suosittelen lämpimästi alla mainittujen ulkoisten resurssien linkkien konsultointia.

**Ulkoiset resurssit:**
- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/esittelyssä-boltzmann-85930984a159](https://medium.com/@laurentmt/esittelyssä-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)