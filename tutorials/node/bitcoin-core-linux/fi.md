---
name: Bitcoin Core (Linux)
description: Oman solmun käyttäminen Bitcoin core:llä Linuxissa
---

![cover](assets/cover.webp)


## Oman solmun käyttäminen Bitcoin core:lla


Johdatus Bitcoin:een ja solmun käsitteeseen, jota täydentää kattava asennusopas Linuxille.


Yksi Bitcoin:n jännittävimmistä puolista on mahdollisuus ajaa ohjelmaa itse ja siten osallistua rakeisella tasolla verkkoon ja julkisen transaktion Ledger todentamiseen.


Bitcoin on ollut avoimen lähdekoodin projektina vapaasti saatavilla ja julkisesti jaossa vuodesta 2009 lähtien. Lähes 17 vuotta perustamisensa jälkeen Bitcoin on nyt vankka ja pysäyttämätön digitaalinen rahaverkko, joka hyötyy voimakkaasta orgaanisesta verkostovaikutuksesta. Satoshi Nakamoto ansaitsee kiitoksemme ponnisteluistaan ja näkemyksestään. Muuten, me isännöimme Bitcoin:n whitepaperia täällä Agora 256:ssa (huom. myös yliopistossa).


### Oman pankin perustaminen


Oman solmun pyörittämisestä on tullut olennaisen tärkeää Bitcoin-etiikan kannattajille. Kyselemättä keneltäkään lupaa on mahdollista ladata Blockchain alusta alkaen ja siten todentaa kaikki transaktiot A:sta Z:hen Bitcoin-protokollan mukaisesti.


Ohjelmaan kuuluu myös oma Wallet. Siten voimme valvoa tapahtumia, joita lähetämme muuhun verkkoon, ilman välikäsiä tai kolmansia osapuolia. Sinä olet oma pankkisi.


Tämän artikkelin loppuosa on siis opas Bitcoin core:n - yleisimmin käytetyn Bitcoin-ohjelmistoversion - asentamiseen erityisesti Debian-yhteensopiviin Linux-jakeluihin, kuten Ubuntuun ja Pop!OS:ään. Seuraa tätä opasta ottaaksesi askeleen lähemmäs yksilöllistä itsemääräämisoikeuttasi.


## Bitcoin core Asennusopas Debian/Ubuntu -käyttöjärjestelmälle


**Edellytykset**


- Vähintään 6 Gt tallennustilaa (pruned-solmu) - 1 Tt tallennustilaa (Full node)
- Odota, että *Initial Block Download* (IBD) kestää vähintään 24 tuntia. Tämä toiminto on pakollinen jopa pruned-solmulle.
- Anna IBD:lle ~600 Gt kaistanleveyttä, jopa pruned-solmulle.


**Huomautus:💡** seuraavat komennot on määritetty valmiiksi Bitcoin core-versiossa 24.1.


### Tiedostojen lataaminen ja tarkistaminen



- [Lataa](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, sekä `SHA256SUMS` ja `SHA256SUMS.asc`-tiedostot (sinun on luonnollisesti ladattava uusin versio ohjelmistosta).



- Avaa pääte siihen hakemistoon, jossa ladatut tiedostot sijaitsevat. Esimerkki: `cd ~/Downloads/`.



- Tarkista, että versiotiedoston tarkistussumma on lueteltu tarkistussummatiedostossa komennolla `sha256sum --ignore-missing --check SHA256SUMS`.



- Tämän komennon tulosteessa pitäisi olla ladatun versiotiedoston nimi ja sen jälkeen `OK`. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Asenna git komennolla `sudo apt install git`. Kloonaa sitten Bitcoin core-signaajien PGP-avaimet sisältävä arkisto komennolla `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Tuo kaikkien allekirjoittajien PGP-avaimet komennolla `gpg --import guix.sigs/builder-keys/*`



- Tarkista, että tarkistussummatiedosto on allekirjoitettu allekirjoittajien PGP-avaimilla komennolla `gpg --verify SHA256SUMS.asc`.



Jokaisessa kelvollisessa allekirjoituksessa näkyy rivi, joka alkaa seuraavalla: `gpg: Hyvä allekirjoitus` ja toinen rivi, joka päättyy: `Primary key fingerprint: b794 860F EB80 4E66 9320` (esimerkki Pieter Wuillen PGP-avaimen sormenjäljestä).


**Huomautus💡:** Kaikkien allekirjoitusavainten ei tarvitse palauttaa "OK". Itse asiassa vain yksi voi olla tarpeen. Käyttäjä voi itse määritellä PGP-varmistuksen validointikynnyksen.


Voit jättää varoitukset huomiotta:



- "Tätä avainta ei ole varmennettu luotettavalla allekirjoituksella!



- "Ei ole mitään viitteitä siitä, että allekirjoitus kuuluisi omistajalle


### Bitcoin core:n graafisen Interface:n asennus



- Pura arkiston sisältämät tiedostot päätelaitteessa, edelleen siinä hakemistossa, jossa Bitcoin core-versiotiedosto sijaitsee, komennolla `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz`.



- Asenna aiemmin puretut tiedostot komennolla `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Asenna tarvittavat riippuvuudet komennolla `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Käynnistä _bitcoin-qt_ (Bitcoin core graafinen Interface) komennolla `Bitcoin-qt`.



- Jos haluat valita pruned-solmun, valitse _Limit Blockchain storage_ ja määritä tallennettavan tiedon raja:


![welcome](assets/fr/02.webp)


### Osa 1: Asennusopas


Kun Bitcoin core on asennettu, on suositeltavaa pitää se käynnissä mahdollisimman paljon, jotta se voi osallistua Bitcoin-verkon toimintaan tarkistamalla transaktioita ja lähettämällä uusia lohkoja muille vertaisverkoille.


Solmun ajaminen ja synkronointi ajoittain, vaikka vain vastaanotettujen ja lähetettyjen tapahtumien validoimiseksi, on kuitenkin edelleen hyvä käytäntö.


![Creation wallet](assets/fr/03.webp)


## Torin määrittäminen Bitcoin core-solmulle


**Huomautus💡:** Tämä opas on suunniteltu Bitcoin core 24.0.1:lle Ubuntu/Debian-yhteensopivissa Linux-jakeluissa.


### Torin asentaminen ja määrittäminen Bitcoin core:lle


Ensin meidän on asennettava Tor-palvelu (The Onion Router), anonyymiin viestintään käytettävä verkko, jonka avulla voimme anonymisoida vuorovaikutuksemme Bitcoin-verkon kanssa. Tutustu yksityisyydensuojatyökaluihin verkossa, Tor mukaan lukien, tätä aihetta käsittelevässä artikkelissamme.


Asenna Tor avaamalla terminaali ja kirjoittamalla `sudo apt -y install tor`. Kun asennus on valmis, palvelu käynnistyy normaalisti automaattisesti taustalla. Tarkista, että se toimii oikein komennolla `sudo systemctl status tor`. Vastauksena pitäisi näkyä `Active: active (exited)`. Poistu tästä toiminnosta painamalla `Ctrl+C`.


**Vinkki:** Voit joka tapauksessa käyttää seuraavia komentoja terminaalissa Torin käynnistämiseen, pysäyttämiseen tai uudelleenkäynnistämiseen:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Seuraavaksi käynnistetään Bitcoin core-grafinen Interface komennolla `Bitcoin-qt`. Ota sitten käyttöön ohjelmiston automaattinen ominaisuus reitittää yhteytemme Tor-välityspalvelimen kautta: _Settings > Network_, ja valitse sieltä _Connect through SOCKS5 proxy (default proxy)_ sekä _Use a separate SOCKS5 proxy to reach peers via Tor onion services_.


![option](assets/fr/04.webp)


Bitcoin core havaitsee automaattisesti, onko Tor asennettu, ja jos on, se luo oletusarvoisesti lähteviä yhteyksiä muihin solmuihin, jotka myös käyttävät Toria, sekä yhteyksiä solmuihin, jotka käyttävät IPv4/IPv6-verkkoja (clearnet).


**Huomautus💡:** Jos haluat vaihtaa näyttökielen ranskaksi, siirry Asetukset-välilehdelle Näyttö.


### Edistynyt Tor-konfiguraatio (valinnainen)


Bitcoin core on mahdollista konfiguroida käyttämään vain Tor-verkkoa yhteyden muodostamiseen vertaisverkkoihin, jolloin anonymiteettimme solmun kautta optimoituu. Koska graafisessa Interface:ssä ei ole tätä varten sisäänrakennettua toimintoa, meidän on luotava manuaalisesti konfigurointitiedosto. Siirry kohtaan Asetukset ja sitten Asetukset.


![option 2](assets/fr/05.webp)


Napsauta tässä kohtaa _Open configuration file_. Kun olet `Bitcoin.conf`-tekstitiedostossa, lisää rivi `onlynet=onion` ja tallenna tiedosto. Sinun on käynnistettävä Bitcoin core uudelleen, jotta tämä komento tulee voimaan.


Tämän jälkeen konfiguroimme Tor-palvelun niin, että Bitcoin core voi vastaanottaa saapuvia yhteyksiä välityspalvelimen kautta, jolloin muut verkon solmut voivat käyttää solmua Blockchain:n tietojen lataamiseen vaarantamatta koneemme turvallisuutta.


Kirjoita päätelaitteessa `sudo nano /etc/tor/torrc` päästäksesi käsiksi Tor-palvelun asetustiedostoon. Etsi tiedostosta rivi `#ControlPort 9051` ja poista `#` ottaaksesi sen käyttöön. Lisää nyt tiedostoon kaksi uutta riviä:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Voit poistua tiedostosta tallentamisen aikana painamalla `Ctrl+X > Y > Enter`. Käynnistä Tor uudelleen terminaalissa komennolla `sudo systemctl restart tor`.


Tällä kokoonpanolla Bitcoin core pystyy luomaan saapuvia ja lähteviä yhteyksiä muihin verkon solmuihin vain Tor-verkon (Onion) kautta. Vahvista tämä napsauttamalla _Window_-välilehteä ja sitten _Peers_.


![Nodes Window](assets/fr/06.webp)


### Lisäresurssit


Jos käytät vain Tor-verkkoa (`onlynet=onion`), voit olla altis Sybil Attack:lle. Siksi jotkut suosittelevat usean verkon konfiguraation ylläpitämistä tämäntyyppisten riskien vähentämiseksi. Lisäksi kaikki IPv4/IPv6-yhteydet ohjataan Tor-välityspalvelimen kautta, kun se on konfiguroitu, kuten aiemmin todettiin.


Vaihtoehtoisesti, jos haluat pysyä pelkästään Tor-verkossa ja vähentää Sybil Attack:n riskiä, voit lisätä toisen luotetun solmun Address:n Bitcoin.conf-tiedostoosi lisäämällä rivin `addnode=trusted_address.onion`. Voit lisätä tämän rivin useita kertoja, jos haluat muodostaa yhteyden useisiin luotettuihin solmuihin.


Jos haluat tarkastella Bitcoin-solmusi lokitietoja, jotka liittyvät erityisesti sen vuorovaikutukseen Torin kanssa, lisää `debug=tor` Bitcoin.conf-tiedostoon. Debug-lokissasi on nyt Toriin liittyviä tietoja, joita voit tarkastella _Information_-ikkunassa _Debug File_-painikkeella. Näitä lokeja on mahdollista tarkastella myös suoraan terminaalissa komennolla `bitcoind -debug=tor`.


**Vinkki💡:** Tässä on muutamia mielenkiintoisia linkkejä:


- [Wikisivu, jossa selitetään Tor ja sen suhde Bitcoin:een](https://en.Bitcoin.it/wiki/Tor)
- [Bitcoin core konfigurointitiedoston generaattori Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Jon Atackin Tor-konfigurointiopas](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Kuten aina, jos sinulla on kysyttävää, voit jakaa sen Agora256-yhteisön kanssa. Opimme yhdessä, jotta voisimme olla huomenna parempia kuin tänään!