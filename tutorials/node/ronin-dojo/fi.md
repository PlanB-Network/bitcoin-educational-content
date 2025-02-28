---
name: RoninDojo

description: RoninDojo Bitcoin-solmun asentaminen ja käyttäminen.
---
***VAROITUS:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta, tietyt RoninDojon ominaisuudet, kuten Whirlpool, eivät ole enää toiminnassa. On kuitenkin mahdollista, että nämä työkalut voidaan palauttaa tai käynnistää uudelleen eri tavalla tulevina viikkoina. Lisäksi, koska RoninDojon koodi oli isännöity Samourain GitLabiin, joka myös takavarikoitiin, koodin etälataus ei tällä hetkellä ole mahdollista. RoninDojon tiimit työskentelevät todennäköisesti koodin uudelleenjulkaisemiseksi.*

_Seuraamme tarkasti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voit olla varma, että päivitämme tämän oppaan, kun uutta tietoa tulee saataville._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme tue tai kannusta näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

_Tämä opas on omistettu RoninDojo v1:n asentamiselle. Jotta voit hyödyntää viimeisimpiä parannuksia ja ominaisuuksia, suosittelen vahvasti tutustumista oppaaseemme, joka on omistettu RoninDojo v2:n suoralle asentamiselle Raspberry Pi -laitteellesi:_ https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Oman solmun käyttäminen on olennaista todelliseen osallistumiseen Bitcoin-verkkoon. Vaikka Bitcoin-solmun pyörittäminen ei tuo käyttäjälle taloudellisia etuja, se mahdollistaa yksityisyyden säilyttämisen, itsenäisen toiminnan ja luottamuksen hallinnan verkossa.

Tässä artikkelissa tarkastelemme yksityiskohtaisesti RoninDojoa, joka on erinomainen ratkaisu oman Bitcoin-solmun pyörittämiseen.

### Sisällysluettelo:

- Mikä on RoninDojo?
- Minkä laitteiston valita?
- Kuinka asentaa RoninDojo?
- Kuinka käyttää RoninDojoa?
- Yhteenveto

Jos et ole tuttu Bitcoin-solmun toiminnan ja roolin kanssa, suosittelen aloittamaan lukemalla tämän artikkelin: Bitcoin-solmu - Osa 1/2: Tekniset käsitteet.

![Samourai](assets/1.webp)

## Mikä on RoninDojo?

Dojo on täysi Bitcoin-solmupalvelin, jonka Samourai Wallet -tiimi on kehittänyt. Voit vapaasti asentaa sen mille tahansa koneelle.

RoninDojo on asennusavustaja ja hallintatyökalu Dojolle ja useille muille työkaluille. RoninDojo ottaa Dojon alkuperäisen toteutuksen ja lisää siihen monia muita työkaluja, samalla helpottaen asennusta ja hallintaa.

He tarjoavat myös "plug-and-play" -laitteiston, RoninDojo Tanton, jossa RoninDojo on esiasennettuna tiimin kokoamaan koneeseen. Tanto on maksullinen ratkaisu, joka sopii niille, jotka eivät halua "sotkea käsiään".

RoninDojon koodi on avoimen lähdekoodin, joten on myös mahdollista asentaa tämä ratkaisu omalle laitteistollesi. Tämä vaihtoehto on kustannustehokas, mutta vaatii hieman enemmän käsittelyä, jota käsittelemme tässä artikkelissa.

RoninDojo on Dojo, joten se mahdollistaa Whirlpool CLI:n helpon integroinnin Bitcoin-solmuusi, jotta voit saada parhaan mahdollisen CoinJoin-kokemuksen. Whirlpool CLI:n avulla voit antaa bitcoiniesi remixautua 24/7 tarvitsematta pitää henkilökohtaista tietokonettasi päällä, mutta voit myös parantaa yksityisyyttäsi merkittävästi.
RoninDojo integroi monia muita työkaluja, jotka luottavat Dojoosi, kuten Boltzmann-laskimen, joka määrittää transaktion yksityisyystason, Electrum-palvelimen, jotta voit yhdistää eri Bitcoin-lompakkosi solmuusi, tai Mempool-palvelimen, jotta voit yksityisesti tarkkailla transaktioitasi. Toiseen solmuratkaisuun, kuten Umbrel, josta kerroin sinulle tässä artikkelissa, verrattuna RoninDojo keskittyy syvästi "On Chain" -ratkaisuihin ja työkaluihin, jotka optimoivat käyttäjän yksityisyyttä. Siksi RoninDojo ei salli vuorovaikutusta Lightning Networkin kanssa.
RoninDojo tarjoaa vähemmän työkaluja verrattuna Umbreliin, mutta Roninissa olevat muutamat olennaiset ominaisuudet Bitcoinerin kannalta ovat uskomattoman vakaita.

Joten jos et tarvitse kaikkia Umbrel-palvelimen ominaisuuksia ja haluat vain yksinkertaisen ja vakaan solmun muutamalla olennaisella työkalulla, kuten Whirlpool tai Mempool, RoninDojo on todennäköisesti hyvä ratkaisu sinulle.

Mielestäni Umbrelin kehityksen painopiste on vahvasti Lightning Networkissa ja monipuolisissa työkaluissa. Se on edelleen Bitcoin-solmu, mutta tavoitteena on tehdä siitä monitoiminen mini-palvelin. Sitä vastoin RoninDojon kehityksen painopiste on enemmän linjassa Samourai Walletin tiimien kanssa ja keskittyy olennaisiin työkaluihin Bitcoinerin kannalta, mahdollistaen täyden riippumattomuuden ja yksityisyyden hallinnan optimoinnin Bitcoinissa.

Huomaa, että RoninDojon solmun asettaminen on hieman monimutkaisempaa kuin Umbrel-solmun.

Nyt kun olemme pystyneet maalaamaan kuvan RoninDojosta, katsotaan, miten asetamme tämän solmun yhdessä.

## Minkä laitteiston valita?

RoninDojon isännöimiseen ja ajamiseen sopivan koneen valitsemiseksi sinulla on useita vaihtoehtoja.

Kuten aiemmin selitettiin, yksinkertaisin valinta on tilata Tanto, plug-and-play -laite, joka on suunniteltu erityisesti tähän tarkoitukseen. Tilataksesi omasi, mene tänne: [linkki](https://shop.ronindojo.io/product-category/nodes/).

Koska RoninDojon tiimit tuottavat avoimen lähdekoodin, on myös mahdollista toteuttaa RoninDojo muilla koneilla. Voit löytää asennusvelhon uusimmat versiot tältä sivulta: [linkki](https://ronindojo.io/en/downloads.html), ja koodin uusimmat versiot tältä sivulta: [linkki](https://code.samourai.io/ronindojo/RoninDojo).

Henkilökohtaisesti asensin sen Raspberry Pi 4 8GB:lle ja kaikki toimii täydellisesti.

Huomaa kuitenkin, että RoninDojon tiimit ilmoittavat, että koteloissa ja SSD-sovittimissa on usein ongelmia. Siksi ei suositella käyttämään koteloa kaapelilla koneesi SSD:lle. Sen sijaan on suositeltavaa käyttää tallennuslaajennuskorttia, joka on erityisesti suunniteltu emolevyllesi, kuten tämä: Raspberry Pi 4 Storage Expansion Card.

Tässä on esimerkki siitä, miten voit asettaa oman RoninDojo-solmusi:

- Raspberry Pi 4.
- Kotelo tuulettimella.
- Yhteensopiva tallennuslaajennuskortti.
- Virtajohto.
- Industriaalinen micro SD -kortti, 16GB tai enemmän.
- 1TB tai suurempi SSD.
- RJ45 Ethernet-kaapeli, suositellaan kategoriaa 8.

## Miten asentaa RoninDojo?

### Vaihe 1: Valmistele käynnistettävä micro SD -kortti.

Kun olet koonnut koneesi, voit aloittaa RoninDojon asennuksen. Tee tämä aloittamalla käynnistettävän micro SD -kortin luominen polttamalla sopiva levykuva siihen.

Aseta micro SD -korttisi henkilökohtaiseen tietokoneeseesi, mene sitten viralliselle RoninDojo-verkkosivustolle ladataksesi RoninOS-levykuvan: https://ronindojo.io/en/downloads.html.
Lataa levykuva, joka vastaa laitteistosi. Minun tapauksessani latasin "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ" kuvan:
![Lataa RoninOS levykuva](assets/2.webp)

Kun kuva on ladattu, varmista sen eheys vastaavalla .SHA256-tiedostolla. Kuvaan yksityiskohtaisesti, miten tämä tehdään tässä artikkelissa: Kuinka varmistaa Bitcoin-ohjelmiston eheys Windowsissa?

Erityisohjeet RoninOS:n eheyden varmistamiseksi ovat myös saatavilla tällä sivulla: https://wiki.ronindojo.io/en/extras/verify.

Polta tämä kuva micro SD -kortillesi käyttämällä ohjelmistoa, kuten Balena Etcher, jonka voit ladata täältä: https://www.balena.io/etcher/.

Tee tämä valitsemalla kuva Etcherissä ja polttamalla se micro SD -kortille:

![Polta levykuva Etcherillä](assets/3.webp)

Kun toimenpide on valmis, voit asettaa käynnistettävän micro SD -kortin Raspberry Pi:hin ja käynnistää koneen.

### Vaihe 2: Määritä RoninOS.

RoninOS on RoninDojo-noodisi käyttöjärjestelmä. Se on muokattu versio Manjarosta, Linux-jakelusta. Koneesi käynnistyttyä ja odotettuasi muutaman minuutin, voit aloittaa sen määrittämisen.

Yhdistääksesi siihen etänä, sinun on löydettävä RoninDojo-koneesi IP-osoite. Voit tehdä tämän esimerkiksi yhdistämällä internet-laitteesi hallintapaneeliin, tai voit myös ladata ohjelmiston, kuten https://angryip.org/, skannataksesi paikallisen verkkosi ja löytääksesi koneen IP:n.

Kun olet löytänyt IP:n, voit ottaa koneesi hallintaan toiselta samassa paikallisverkossa olevan tietokoneelta käyttäen SSH:ta.

macOS- tai Linux-tietokoneella avaa vain terminaali. Windows-tietokoneella voit käyttää erikoistyökalua, kuten Puttya, tai suoraan käyttää Windows PowerShellia.

Kun terminaali on avattu, kirjoita seuraava komento:

> ssh root@192.168.?.?

Korvaa vain kaksi kysymysmerkkiä aiemmin löytämäsi RoninDojon IP:llä.
Vinkki: Shellissä, oikea klikkaus liittää kohteen.

Seuraavaksi saavut Manjaron hallintapaneeliin. Valitse oikea näppäimistöasettelu käyttämällä nuolia muuttaaksesi kohdetta pudotusvalikossa.

![Manjaron näppäimistöasettelun määrittäminen](assets/4.webp)

Valitse käyttäjänimi ja salasana istunnollesi. Käytä vahvaa salasanaa ja tee siitä turvallinen varmuuskopio. Voit valinnaisesti käyttää heikkoa salasanaa asennuksen aikana ja myöhemmin vaihtaa sen helposti "kopioimalla ja liittämällä" sen RoninUI:hin. Tämä mahdollistaa erittäin vahvan salasanan käytön ilman, että kulutat paljon aikaa sen manuaaliseen kirjoittamiseen Manjaron asetuksissa.

![Manjaron käyttäjänimen määrittäminen](assets/5.webp)

Seuraavaksi sinua pyydetään myös valitsemaan root-salasana. Root-salasanaksi, syötä suoraan vahva salasana. Et pysty muuttamaan sitä RoninUI:sta. Muista myös turvallisesti varmuuskopioida tämä root-salasana.

Syötä sitten sijaintisi ja aikavyöhykkeesi.

![Manjaron aikavyöhykkeen määrittäminen](assets/6.webp)

![Manjaron sijainnin määrittäminen](assets/7.webp)

Seuraavaksi valitse isäntänimi.

![Manjaron isäntänimen määrittäminen](assets/8.webp)

Lopuksi, tarkista Manjaron konfiguraatiotiedot ja vahvista.

![ManjaroOS:n konfiguraatiotietojen tarkistus](assets/9.webp)

### Vaihe 3: Lataa RoninDojo.
RoninOS:n alkukonfiguraatio suoritetaan. Kun se on valmis, kuten yllä olevassa kuvakaappauksessa näkyy, kone käynnistyy uudelleen. Odota hetki, ja syötä sitten seuraava komento muodostaaksesi yhteyden uudelleen RoninDojo-laitteeseesi:
> ssh käyttäjänimi@192.168.?.?

Korvaa vain "käyttäjänimi" aiemmin valitsemallasi käyttäjänimellä ja korvaa kysymysmerkit RoninDojon IP-osoitteella.

Syötä sen jälkeen käyttäjäsalasanasi.

Terminaalissa näyttää tältä:

![SSH-yhteys RoninOS:iin](assets/10.webp)

Olet nyt yhteydessä koneeseesi, jossa on tällä hetkellä vain RoninOS. Nyt sinun täytyy asentaa siihen RoninDojo.

Lataa RoninDojon uusin versio syöttämällä seuraava komento:

> git clone https://code.samourai.io/ronindojo/RoninDojo

Lataus on nopea. Terminaalissa näet tämän:

![RoninDojon kloonaus](assets/11.webp)

Odota, että lataus on valmis, asenna sitten ja pääse käsiksi RoninDojon käyttöliittymään käyttämällä seuraavaa komentoa:

> ~/RoninDojo/ronin

Sinua pyydetään syöttämään käyttäjäsalasanasi:

![Bitcoin-solmun salasanan varmistus](assets/12.webp)

Tämä komento on tarpeen vain ensimmäisellä kerralla, kun pääset käsiksi RoninDojoosi. Myöhemmin, päästäksesi käsiksi RoninCLI:hin SSH:n kautta, sinun tarvitsee vain syöttää komento [SSH käyttäjänimi@192.168.?.?] korvaten "käyttäjänimi" omalla käyttäjänimelläsi ja syöttämällä solmusi IP-osoite. Sinua pyydetään syöttämään käyttäjäsalasanasi.

Seuraavaksi näet tämän upean animaation:

![RoninCLI:n käynnistysanimaatio](assets/13.webp)

Sitten saavut viimein RoninDojon CLI-käyttöliittymään.

### Vaihe 4: Asenna RoninDojo.

Päävalikosta siirry "System" (Järjestelmä) -valikkoon käyttämällä näppäimistösi nuolinäppäimiä. Vahvista valintasi painamalla enter-näppäintä.

![RoninCLI:n navigointivalikko Järjestelmään](assets/14.webp)

Siirry sitten "System Setup & Install" (Järjestelmän asennus ja asetukset) -valikkoon.

![RoninCLI:n navigointivalikko RoninDojon järjestelmäasennukseen](assets/15.webp)

Lopuksi valitse "System Setup" (Järjestelmän asetukset) ja "Install RoninDojo" (Asenna RoninDojo) käyttämällä välilyöntinäppäintä, ja valitse "Accept" (Hyväksy) aloittaaksesi asennuksen.

![RoninDojon asennuksen vahvistus](assets/16.webp)

Anna asennuksen sujua rauhassa. Omassa tapauksessani se kesti noin 2 tuntia. Pidä terminaalisi avoinna prosessin ajan.

Tarkista terminaalisi silloin tällöin, sillä tietyissä asennuksen vaiheissa sinua pyydetään painamaan näppäintä, kuten tässä esimerkiksi:

![RoninDojon asennus käynnissä](assets/17.webp)

Asennuksen lopussa näet eri konttien käynnistyvän:

![Solmukonttien käynnistys](assets/18.webp)

Sitten solmusi käynnistyy uudelleen. Yhdistä uudelleen RoninCLI:hin seuraavaa vaihetta varten.

![Bitcoin-solmun uudelleenkäynnistys](assets/19.webp)

### Vaihe 5: Lataa proof-of-work-ketju ja pääse käsiksi RoninUI:hin.

Asennuksen valmistuttua solmusi alkaa ladata Bitcoinin proof-of-work-ketjua. Tätä kutsutaan alkuperäisen lohkotiedon lataukseksi (Initial Block Download, IBD). Se kestää yleensä 2–14 päivää riippuen internet-yhteydestäsi ja laitteestasi.

Voit seurata ketjun latauksen edistymistä pääsemällä käsiksi RoninUI:n web-käyttöliittymään.

Päästäksesi siihen paikallisverkosta, kirjoita selaimen osoitekenttään joko:

- Suoraan koneesi IP-osoite (192.168.?.?)

- Tai kirjoita: ronindojo.local
Muista poistaa VPN-käytöstä, jos käytät sellaista.
### Mahdollinen ongelma

Jos et pysty muodostamaan yhteyttä RoninUI:hin selaimellasi, tarkista sovelluksen toiminta Terminaalin kautta, joka on yhdistetty solmuusi SSH:n kautta. Yhdistä päävalikkoon seuraamalla aiempia vaiheita:

- Kirjoita: SSH käyttäjänimi@192.168.?.? korvaten omilla tunnuksillasi.

- Anna käyttäjäsalasanasi.

Päävalikossa siirry kohtaan:

> RoninUI > Käynnistä uudelleen

Jos sovellus käynnistyy oikein, ongelma on yhteydessä selaimestasi. Tarkista, ettet käytä VPN:ää ja varmista, että olet yhdistetty samaan verkkoon kuin solmusi.

Jos uudelleenkäynnistys tuottaa virheen, yritä päivittää käyttöjärjestelmä ja sen jälkeen asentaa RoninUI uudelleen. Käyttöjärjestelmän päivittämiseksi:

> Järjestelmä > Ohjelmistopäivitykset > Päivitä käyttöjärjestelmä

Kun päivitys ja uudelleenkäynnistys ovat valmiit, yhdistä solmuusi uudelleen SSH:n kautta ja asenna RoninUI uudelleen:

> RoninUI > Asenna uudelleen

RoninUI:n uudelleenlataamisen jälkeen yritä yhdistää RoninUI:hin selaimellasi.

> Vinkki: Jos poistut vahingossa RoninCLI:stä ja löydät itsesi Manjaro-terminaalista, kirjoita komento "ronin" palataksesi suoraan RoninCLI:n päävalikkoon.

### Web-kirjautuminen

Voit myös kirjautua RoninUI:n web-käyttöliittymään mistä tahansa verkosta käyttäen Toria. Tee tämä noutamalla RoninUI:n Tor-osoite RoninCLI:stä:

> Tunnukset > Ronin UI

Nouda Tor-osoite, joka päättyy .onion, ja kirjaudu sitten Ronin UI:hin syöttämällä tämä osoite Tor-selaimeesi. Ole varovainen, ettet vuoda erilaisia tunnuksiasi, sillä ne ovat arkaluonteisia tietoja.

![RoninUI:n web-kirjautumisliittymä](assets/20.webp)

Kirjautumisen jälkeen sinua pyydetään käyttäjäsalasanaasi. Se on sama salasana, jota käytät kirjautuessasi SSH:n kautta.

![RoninUI:n web-hallintapaneeli](assets/21.webp)

Täällä voimme nähdä IBD:n (Initial Block Download) edistymisen. Ole kärsivällinen, olet lataamassa kaikkia Bitcoinissa tehdyt transaktiot tammikuun 3. päivästä 2009 lähtien.

Koko lohkoketjun lataamisen jälkeen indeksoija tiivistää tietokannan. Tämä toimenpide kestää noin 12 tuntia. Voit myös seurata sen edistymistä "Indeksoija" -kohdassa RoninUI:ssa.

RoninDojo-solmusi on täysin toiminnallinen tämän jälkeen:

![Indeksoija synkronoitu 100% toimiva solmu](assets/22.webp)

Jos haluat vaihtaa käyttäjäsalasanasi vahvempaan, voit tehdä sen nyt "Asetukset"-välilehdeltä. RoninDojossa ei ole lisäkerrosta turvallisuudessa, joten suosittelen valitsemaan todella vahvan salasanan ja huolehtimaan sen varmuuskopiosta.

## Kuinka käyttää RoninDojoa?

Kun ketju on ladattu ja tiivistetty, voit aloittaa nauttimaan uuden RoninDojo-solmusi tarjoamista palveluista. Katsotaan, miten niitä käytetään.

### Lompakko-ohjelmiston yhdistäminen electrs:iin.

Uuden asennetun ja synkronoidun solmusi ensimmäinen hyöty on transaktioidesi lähettäminen Bitcoin-verkkoon. Siksi haluat todennäköisesti yhdistää eri lompakonhallintaohjelmistosi siihen.

Voit tehdä tämän käyttämällä Electrum Rust Serveria (electrs). Sovellus on yleensä esiasennettu RoninDojo-solmuusi. Jos ei, voit asentaa sen manuaalisesti RoninCLI-käyttöliittymästä.

Siirry vain kohtaan:

> Sovellukset > Hallitse sovelluksia > Asenna Electrum-palvelin

Saadaksesi Electrum-palvelimesi Tor-osoitteen, siirry RoninCLI-valikossa kohtaan:

> Tunnukset > Electrs
Sinun tarvitsee vain syöttää .onion-linkki lompakko-ohjelmistoosi. Esimerkiksi Sparrow Walletissa, mene välilehteen:
> Tiedosto > Asetukset > Palvelin

Palvelintyypissä valitse "Yksityinen Electrum", ja syötä sitten Tor-osoitteesi Electrum Serverille vastaavaan kenttään. Lopuksi klikkaa "Testaa yhteys" testataksesi ja tallentaaksesi yhteytesi.

![Sparrow Walletin yhteysliittymä electrs:iin](assets/23.webp)

### Lompakko-ohjelmiston yhdistäminen Samourai Dojoon.

Electrs:n sijaan voit myös käyttää Samourai Dojoa yhdistääksesi yhteensopivan ohjelmistolompakkosi RoninDojo-noodiisi. Esimerkiksi Samourai Wallet tarjoaa tämän vaihtoehdon.

Tehdäksesi tämän, skannaa yksinkertaisesti Dojosi yhteys-QR-koodi. Päästäksesi siihen RoninUI:ssa, klikkaa "Hallintapaneeli"-välilehteä ja sitten "Hallitse"-painiketta Dojosi laatikossa. Sen jälkeen voit nähdä Dojosi ja BTC-RPC Explorerin yhteys-QR-koodit. Näyttääksesi ne, klikkaa "Näytä arvot".

![Dojon yhteys-QR-koodin noutaminen](assets/24.webp)

Yhdistääksesi Samourai Walletisi Dojoosi, sinun tulee skannata tämä QR-koodi sovelluksen asennuksen aikana:

![Yhdistäminen Dojoon Samourai Wallet -sovelluksesta](assets/25.webp)

### Oman Mempool Explorerin käyttäminen.

Oleellinen työkalu Bitcoin-käyttäjille, explorer mahdollistaa erilaisten tietojen tarkistamisen Bitcoin-ketjusta. Mempoolin avulla voit esimerkiksi tarkistaa reaaliajassa muiden käyttäjien soveltamia maksuja, jotta voit säätää omasi vastaavasti. Voit myös tarkistaa yhden transaktiosi vahvistustilan tai tarkastella osoitteen saldoa.

Nämä explorer-työkalut voivat altistaa sinut yksityisyyden riskeille ja vaativat sinua luottamaan kolmannen osapuolen tietokantaan. Kun käytät tätä online-työkalua käymättä läpi omaa noodiasi:

- Riskinä on lompakkotietojesi vuotaminen.

- Luotat verkkosivuston ylläpitäjään heidän isännöimänsä proof-of-work-ketjun osalta.

Välttääksesi nämä riskit, voit käyttää omaa Mempool-instanssiasi noodissasi Tor-verkon kautta. Tällä ratkaisulla et ainoastaan säilytä yksityisyyttäsi palvelua käyttäessäsi, mutta sinun ei myöskään tarvitse luottaa tarjoajaan, koska kyselyt tehdään omasta tietokannastasi.

Tehdäksesi tämän, aloita asentamalla Mempool Space Visualizer RoninCLI:stä:

> Sovellukset > Hallitse Sovelluksia > Asenna Mempool Space Visualizer

Asennuksen jälkeen, nouda linkki Mempooliisi. Tor-osoite mahdollistaa pääsyn siihen mistä tahansa verkosta. Samoin, haemme tämän linkin RoninCLI:n kautta:

> Tunnukset > Mempool

![Hae Tor Mempool -osoite](assets/26.webp)

Syötä vain Mempool Tor -osoitteesi Tor-selaimeen nauttiaksesi omasta Mempool-instanssistasi, joka perustuu omiin tietoihisi. Suosittelen lisäämään tämän Tor-osoitteen suosikkeihisi nopeampaa pääsyä varten. Voit myös luoda pikakuvakkeen työpöydällesi.

![Mempool Space -käyttöliittymä](assets/27.webp)

Jos sinulla ei vielä ole Tor-selainta, voit ladata sen täältä: https://www.torproject.org/download/

Voit myös käyttää sitä älypuhelimellasi asentamalla Tor-selaimen ja syöttämällä saman osoitteen. Missä tahansa voit tarkastella Bitcoin-ketjun tilaa käyttäen omaa noodiasi.

### Whirlpool CLI:n käyttäminen.

RoninDojo-noodisi sisältää myös WhirlpoolCLI:n, etäkomentoriviliittymän Whirlpool-sekoitusten automatisointiin.
Kun suoritat CoinJoinin Whirlpool-toteutuksen avulla, sovelluksen, jota käytät, on pysyttävä avoinna sekoitusten ja uudelleensekoitusten suorittamiseksi. Tämä prosessi voi olla työläs käyttäjille, jotka haluavat korkeita anonimiteettisettejä, sillä laitteen, jossa Whirlpool-sovellus on, on pysyttävä jatkuvasti päällä. Käytännön termein tämä tarkoittaa, että jos haluat osallistua UTXO:idesi 24/7 uudelleensekoituksiin, sinun on pidettävä henkilökohtaista tietokonettasi tai puhelintasi jatkuvasti päällä sovelluksen ollessa avoinna.
Yksi ratkaisu tähän rajoitteeseen on käyttää WhirlpoolCLI:tä koneella, joka on tarkoitettu olemaan jatkuvasti päällä, kuten Bitcoin-noodilla. Näin UTXO:mme voidaan sekoittaa uudelleen 24/7 ilman, että tarvitsee pitää toista konetta käynnissä Bitcoin-noodimme lisäksi.
WhirlpoolCLI:tä käytetään yhdessä WhirlpoolGUI:n kanssa, joka on graafinen käyttöliittymä, joka asennetaan henkilökohtaiseen tietokoneeseen Coinjoinien helppoa hallintaa varten. Selitän yksityiskohtaisesti, miten asettaa Whirlpool CLI omassa dojossasi tässä artikkelissa: [linkki](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).

Jos haluat oppia lisää Coinjoinista yleensä, selitän kaiken tässä artikkelissa: [linkki](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).

### Whirlpool Stat Toolin käyttö.

Suoritettuasi CoinJoinit Whirlpoolin avulla, saatat haluta tietää sekoitettujen UTXO:idesi todellisen yksityisyyden tason. Whirlpool Stat Tool mahdollistaa tämän helposti. Tällä työkalulla voit laskea sekoitettujen UTXO:idesi tulevaisuuden ja menneisyyden arvosanat. Jos haluat oppia lisää näiden Anon Settien laskemisesta ja siitä, miten ne toimivat, suosittelen lukemaan tämän osion: [linkki](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).

Työkalu on esiasennettu RoninDojoosi. Toistaiseksi se on saatavilla vain RoninCLI:stä. Käynnistääksesi sen päävalikosta, mene:

> Samourai Toolkit > Whirlpool Stat Tool

Käyttöohjeet ilmestyvät. Kun olet valmis, paina mitä tahansa näppäintä päästäksesi komentoriveille:

![Whirlpool Stats Tool -ohjelmiston koti](assets/28.webp)

Terminaali näytetään:

> wst#/tmp>

Poistuaksesi tästä käyttöliittymästä ja palataksesi RoninCLI-valikkoon, kirjoita komento:

> quit

Aloitamme asettamalla proxyn Toriin, jotta voimme hakea OXT-tiedot täydellisessä yksityisyydessä. Anna komento:

> socks5 127.0.0.1:9050

Lataa sitten tiedot altaasta, joka sisältää transaktiosi:

> download 0001
>
> Korvaa 0001 altaan nimikoodilla, joka kiinnostaa sinua.

Nimikoodit WST:ssä ovat seuraavat:

- Allas 0.5 bitcoinit: 05

- Allas 0.05 bitcoinit: 005

- Allas 0.01 bitcoinit: 001

- Allas 0.001 bitcoinit: 0001
![Lataa tietoja altaasta 0001 OXT:stä](assets/29.webp)
Kun tiedot on ladattu, lataa ne komennolla:

> load 0001
>
> Korvaa 0001 kiinnostuksesi kohteen altaan tunnuskoodilla.

![Lataa tietoja altaasta 0001](assets/30.webp)
Anna latausprosessin tapahtua, se saattaa kestää muutaman minuutin. Tietojen lataamisen jälkeen kirjoita score-komento seurattuna TXID:lläsi (transaktion tunniste) saadaksesi sen Anon Setsit:

> score TXID
>
> Korvaa TXID transaktiosi tunnisteella.

![Tulostaa annetun TXID:n prospektiiviset ja retrospektiiviset pisteet](assets/31.webp)

WST näyttää sitten retrospektiivisen pistemäärän (taaksepäin katsovat mittarit) seurattuna prospektiivisesta pistemäärästä (eteenpäin katsovat mittarit). Anon Setsien pisteiden lisäksi WST tarjoaa sinulle myös tietoa lähtösi diffuusioasteesta altaassa perustuen anon settiin.

Huomaa, että UTXO:si prospektiivinen pistemäärä lasketaan perustuen TXID:iisi ensimmäisestä sekoituksestasi, ei viimeisestä sekoituksestasi. Toisaalta UTXO:n retrospektiivinen pistemäärä lasketaan perustuen TXID:iin viimeisestä syklistä.

Jos et ymmärrä näitä Anon Setsien konsepteja, suosittelen lukemaan tämän osan artikkelistani Coinjoinista, jossa selitän kaiken yksityiskohtaisesti diagrammien avulla: [https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)

### Boltzmann-laskimen käyttö.

Boltzmann-laskin on työkalu, joka mahdollistaa erilaisten edistyneiden mittareiden, mukaan lukien entropiatason, helpon laskemisen Bitcoin-transaktiolle. Kaikki nämä tiedot auttavat sinua mittaamaan transaktion yksityisyyden tasoa ja havaitsemaan mahdolliset virheet. Tämä työkalu on esiasennettu RoninDojo-noodiisi.

Päästäksesi siihen RoninCLI:n kautta, yhdistä SSH:n kautta, sitten siirry valikkoon:

> Samourai Toolkit > Boltzmann Calculator

Ennen kuin selitän, miten sitä käytetään RoninDojossa, selitän, mitä nämä mittarit edustavat, miten ne lasketaan ja mihin niitä käytetään.

Nämä indikaattorit voidaan käyttää mihin tahansa Bitcoin-transaktioon, mutta ne ovat erityisen mielenkiintoisia Coinjoin-transaktion laadun tutkimiseen.

1. Ensimmäinen tämän ohjelmiston laskema indikaattori on mahdollisten yhdistelmien määrä. Se on merkitty laskimessa "nb combinations". Ottaen huomioon UTXO:iden arvot, tämä indikaattori edustaa mahdollisten syötteiden ja tulosteiden yhdistelmien määrää.

> Jos et ole tuttu termillä "UTXO", suosittelen lukemaan tämän lyhyen artikkelin: Bitcoin-transaktion mekanismi: UTXO, syötteet ja tulosteet.

Toisin sanoen, tämä indikaattori edustaa mahdollisten tulkintojen määrää tietylle transaktiolle. Esimerkiksi Whirlpool 5x5 Coinjoin-rakenteella on mahdollisten yhdistelmien määrä yhtä suuri kuin 1496:

![Coinjoin-transaktion kaavio kycp.org:ssa](assets/32.webp)

Lähde: KYCP
2. Toinen laskettava indikaattori on transaktion entropia. Koska transaktion mahdollisten yhdistelmien määrä voi olla hyvin suuri, voidaan sen sijaan käyttää entropiaa. Entropia edustaa mahdollisten yhdistelmien määrän binäärilogaritmia. Sen kaava on seuraava:
- E: transaktion entropia.
- C: transaktion mahdollisten yhdistelmien määrä.

> E = log2(C)

Matematiikassa binäärilogaritmi (kantaluku 2) on kahden potenssin funktion käänteisfunktio. Toisin sanoen, x:n binäärilogaritmi on eksponentti, johon luku 2 on korotettava saadakseen arvon x.

Näin ollen:

> E = log2(C)
> C = 2^E

Tämä indikaattori ilmaistaan bitteinä. Esimerkiksi tässä on laskettu Whirlpool 5x5 Coinjoin -transaktion entropia, kun aiemmin mainittu mahdollisten yhdistelmien määrä on 1496:

> C = 1496
>
> E = log2(1496)
>
> E = 10.5469 bittiä

Tämän Coinjoin-transaktion entropia on siis 10.5469 bittiä, mikä on erittäin hyvä.

Mitä korkeampi tämä indikaattori on, sitä enemmän erilaisia tulkintoja transaktiosta on, ja siten transaktio on luottamuksellisempi.

Otetaan toinen esimerkki. Tässä on "klassinen" transaktio, jolla on yksi sisääntulo ja kaksi ulostuloa:

![Bitcoin transaktion kaavio oxt.me:ssä](assets/34.webp)

Lähde: OXT

Tällä transaktiolla on vain yksi mahdollinen tulkinta:

> [(inp 0) > (Outp 0 ; Outp 1)]

Joten sen entropia on yhtä suuri kuin 0:

> C = 1
>
> E = log2(C)
>
> E = 0

3. Kolmas indikaattori, jonka Boltzmann-laskin palauttaa, on Tx:n tehokkuus, jota kutsutaan "Wallet Efficiencyksi". Tämä indikaattori mahdollistaa yksinkertaisesti sisääntulotransaktion vertaamisen parhaaseen mahdolliseen transaktioon samassa konfiguraatiossa.

Esittelemme nyt maksimaalisen entropian käsitteen, joka edustaa annetun transaktiorakenteen saavutettavissa olevaa korkeinta entropiaa. Esimerkiksi Whirlpool 5x5 Coinjoin -rakenteella olisi maksimaalinen entropia 10.5469. Tehokkuusindikaattori vertaa tätä maksimaalista entropiaa sisääntulotransaktion todelliseen entropiaan. Sen kaava on seuraava:

- ER: Todellinen entropia ilmaistuna bitteinä.
- EM: Maksimaalinen entropia samalla rakenteella ilmaistuna bitteinä.
- Ef: Tehokkuus ilmaistuna bitteinä.

> Ef = ER - EM
>
> Ef = 10.5469 - 10.5469
>
> Ef = 0 bittiä

Tämä indikaattori ilmaistaan myös prosentteina, joten kaava muuttuu:

- CR: Todellisten mahdollisten yhdistelmien määrä.
- CM: Maksimaalisten mahdollisten yhdistelmien määrä samalla rakenteella.
- Ef: Tehokkuus ilmaistuna prosentteina.

> Ef = CR/CM
>
> Ef = 1496/1496
>
> Ef = 100%

Tehokkuus 100% tarkoittaa, että tällä transaktiolla on korkein mahdollinen yksityisyys suhteessa sen rakenteeseen.

4. Neljäs laskettava indikaattori on entropian tiheys. Sen avulla voimme suhteuttaa entropian kuhunkin sisääntuloon tai ulostuloon. Tätä indikaattoria voidaan käyttää tehokkuuden vertaamiseen eri kokoisten transaktioiden välillä.

Sen laskeminen on hyvin yksinkertaista: jaamme transaktion entropian läsnä olevien sisääntulojen ja ulostulojen määrällä. Esimerkiksi Whirlpool 5x5 Coinjoinille meillä olisi:

    ED: Entropian tiheys ilmaistuna bitteinä.
    E: Transaktion entropia ilmaistuna bitteinä.
    T: Transaktion sisääntulojen ja ulostulojen kokonaismäärä.

T = 5 + 5 = 10
ED = E / TED = 10.5469 / 10
ED = 1.054 bittiä

Boltzmann-laskurin antaman viidennen tiedon kappale on linkkien todennäköisyystaulukko syötteiden ja tulosteiden välillä. Tämä taulukko antaa yksinkertaisesti todennäköisyyden (Boltzmann-pisteet) sille, että tietty syöte vastaa tiettyä tulostetta.

Jos otamme esimerkkimme Whirlpool Coinjoinista, todennäköisyystaulukko näyttäisi tältä:

| %       | Tuloste 0 | Tuloste 1 | Tuloste 2 | Tuloste 3 | Tuloste 4 |
|---------|-----------|-----------|-----------|-----------|-----------|
| Syöte 0 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Syöte 1 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Syöte 2 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Syöte 3 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Syöte 4 | 34%       | 34%       | 34%       | 34%       | 34%       |

Tästä näemme, että jokaisella syötteellä on yhtä suuri todennäköisyys linkittyä mihin tahansa tulosteeseen.

Jos kuitenkin otamme esimerkin transaktiosta, jossa on yksi syöte ja kaksi tulostetta, se näyttäisi tältä:

| Syöte | Tuloste 0 | Tuloste 1 |
| ----- | --------- | --------- |
| 0     | 100%      | 100%      |

Tässä esimerkissä näemme, että kummankin tulosteen tuleminen syötteestä 0 on 100% todennäköistä.

Mitä pienempi tämä todennäköisyys on, sitä korkeampi on luottamuksellisuuden taso.

6. Laskettava kuudes tieto on determinististen linkkien määrä. Myös determinististen linkkien suhde annetaan. Tämä indikaattori korostaa linkkien määrää tietyn transaktion syötteiden ja tulosteiden välillä, joilla on 100% todennäköisyys, eli ne ovat kiistattomia.

Suhde osoittaa determinististen linkkien määrän transaktiossa verrattuna linkkien kokonaismäärään.

Esimerkiksi Coinjoin Whirlpool -transaktiossa ei ole deterministisiä linkkejä syötteiden ja tulosteiden välillä. Indikaattori on nolla ja suhde on myös 0%.

Kuitenkin toisessa tutkitussa transaktiossa (1 syöte ja 2 tulostetta) indikaattori on 2 ja suhde on 100%.

Jos siis tämä indikaattori on nolla, se osoittaa hyvää luottamuksellisuutta.

Nyt kun olemme tutkineet indikaattoreita, katsotaan miten niitä lasketaan käyttämällä tätä ohjelmistoa. RoninCLI:ssä, siirry valikkoon:

> Samourai Toolkit > Boltzmann Calculator

![Boltzmann Calculator -ohjelmiston kotisivu](assets/35.webp)

Kun ohjelmisto on käynnistetty, syötä tutkittavan transaktion ID. Voit syöttää useita transaktioita kerralla erottelemalla ne pilkulla, sitten paina enter:

![Syötä TXID tutkittavaksi Boltzmann-laskurissa](assets/36.webp)

Laskin palauttaa sitten kaikki aiemmin näkemämme indikaattorit:

![Boltzmann-laskurin tulosteen tulostus tälle TXID:lle](assets/37.webp)

Kirjoita komento "Quit" poistuaksesi ohjelmistosta ja palataksesi RoninCLI-valikkoon.

Jos haluat tietää lisää Boltzmann-laskurista, suosittelen lukemaan nämä artikkelit:

- https://medium.com/@laurentmt/esittelyssä-boltzmann-85930984a159

- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
### Yhdistäminen Bisqiin.
Bisq on vertaisverkkoon perustuva vaihtoalusta, joka mahdollistaa bitcoinien ostamisen ja myymisen. Sitä käytetään työpöytäohjelmiston kanssa, joka toimii Tor-verkossa ja mahdollistaa bitcoinien vaihtamisen ilman, että sinun tarvitsee antaa henkilöllisyyttäsi.
Bisq turvaa vertaisverkkovaihdot 2/2 moniallekirjoitusjärjestelmän avulla. Voit käyttää tätä ohjelmistoa oman RoninDojo-solmusi kanssa optimoidaksesi vaihtojesi yksityisyyden ja luottaa oman solmusi lohkoketjun tietoihin.

Ladataksesi Bisq-ohjelmiston, mene heidän viralliselle verkkosivustolleen: https://bisq.network/

Aloittaaksesi ohjelmiston käytön, suosittelen lukemaan tämän sivun: https://bisq.network/getting-started/

Hankkiaksesi yhteyslinkin RoninDojostasi, sinun on yhdistettävä RoninCLI:hin SSH:n kautta. Mene sitten valikkoon:

> Sovellukset > Hallitse Sovelluksia

Syötä salasanasi, sitten merkitse ruutu välilyöntinäppäimellä:

> [ ] Ota käyttöön Bisq-yhteys

Vahvista valintasi. Anna solmusi asentua, sitten hanki Tor V3 -osoite kohdasta:

> Tunnistetiedot > Bitcoind

Kopioi osoite "Bitcoin Daemon" -kohdan alta.

Voit myös hankkia Bitcoind Tor V3 -osoitteesi RoninUI-käyttöliittymästä yksinkertaisesti klikkaamalla "Hallitse" "Bitcoin Core" -laatikossa "Kojelaudalla":

![Hanki TorV3 Bitcoin Daemon -osoite RoninUI:sta](assets/38.webp)

Yhdistääksesi solmusi Bisqiin, mene valikkoon:

> Asetukset > Verkkotiedot

![Pääsy solmun yhteyskäyttöliittymään Bisq-ohjelmistosta](assets/39.webp)

Klikkaa kuplaa "Käytä mukautettuja Bitcoin Core -solmuja". Syötä sitten Bitcoin TorV3 -osoitteesi määrättyyn laatikkoon, ".onion"-päätteellä mutta ilman "http://".

![Laatikko, johon syötetään solmusi TorV3-osoite Bisq-ohjelmistossa](assets/40.webp)

Käynnistä Bisq-ohjelmisto uudelleen. Solmusi on nyt yhdistetty Bisqiisi.

### Muita ominaisuuksia.

RoninDojo-solmusi sisältää myös muita perusominaisuuksia. Sinulla on mahdollisuus skannata tiettyjä tietoja varmistaaksesi, että ne otetaan huomioon.

Esimerkiksi joskus voi olla mahdollista, että RoninDojoon yhdistetty lompakkosi ei löydä sinulle kuuluvia bitcoineja. Saldo on 0, vaikka olet varma, että sinulla on bitcoineja tässä lompakossa. Mahdollisia syitä on monia, mukaan lukien virhe johdannaispoluissa, ja niiden joukossa on myös mahdollista, että solmusi ei tarkkaile osoitteitasi.

Korjataksesi tämän, voit tarkistaa, että solmusi seuraa xpubiasi "xpub-työkalulla". Päästäksesi siihen RoninUI:ssa, mene valikkoon:

> Ylläpito > XPUB Työkalu

Syötä ongelmallinen xpub ja klikkaa "Tarkista" vahvistaaksesi tämän tiedon.

![XPUB Työkalu RoninUI:ssa](assets/41.webp)

Jos xpubiasi seurataan solmussa, näet tämän näkyvän:

![XPUB Työkalun tulos näyttää onnistuneen analyysin](assets/42.webp)

Tarkista, että kaikki tapahtumat näkyvät oikein. Tarkista myös, että johdannaisen tyyppi vastaa lompakkosi tyyppiä. Tässä näemme, että solmu tulkitsee tämän xpubin BIP44-johdannaiseksi. Jos tämä johdannaisen tyyppi ei vastaa lompakkosi tyyppiä, klikkaa "Kirjoita uudelleen" -painiketta, sitten valitse BIP44/BIP49/BIP84 valintasi mukaan:

![Vaihda tutkitun xpubin johdannaistyyppiä RoninUI:ssa](assets/43.webp)

Jos xpubiasi ei seurata solmussasi, näet tämän näytön, joka kutsuu sinua tuomaan sen:
![Tuo xpub XPUB Toolilla RoninUI:ssa](assets/44.webp)
Voit myös käyttää muita ylläpitotyökaluja:

- Transaction Tool: Mahdollistaa tietyn transaktion yksityiskohtien tarkastelun.
- Address Tool: Mahdollistaa tarkistaa, että tietty osoite on Dojon seurannassa.
- Rescan Blocks: Pakottaa noden skannaamaan uudelleen valitun lohkoalueen.

Löydät myös "Push Tx" -työkalun RoninUI:sta. Sen avulla voit lähettää allekirjoitetun transaktion Bitcoin-verkkoon. Sen on oltava hexadesimaalimuodossa:

![Työkalu allekirjoitetun transaktion lähettämiseen RoninUI:sta](assets/45.webp)

## Yhteenveto.

Olemme nähneet, miten asentaa ja aloittaa tämän upean työkalun, RoninDojon, käyttö. Se on erinomainen valinta oman Bitcoin-noden pyörittämiseen. Se on vakaa ratkaisu, joka integroi ja pitää ajan tasalla kaikki olennaiset työkalut Bitcoin-käyttäjälle.

Jos terminaalin käyttö ei pelota sinua ja jos et tarvitse Lightning Networkiin liittyviä työkaluja, RoninDojo saattaa kiinnostaa sinua.

Jos voit, harkitse lahjoittamista kehittäjille, jotka tuottavat näitä avoimen lähdekoodin ohjelmistoja vapaasti käyttöösi: https://donate.ronindojo.io/

Lisätietoja RoninDojosta suosittelen tarkistamaan alla olevat linkit ulkoisista resursseistani.

### Lisälukemista:

- CoinJoinin ymmärtäminen ja käyttäminen Bitcoinissa.
- Hash-funktiot - ote e-kirjasta Bitcoin Démocratisé 1.
- Kaikki mitä sinun tarvitsee tietää Bitcoin Passphrasesta.

### Ulkoiset resurssit:

- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/esittelyssä-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/
