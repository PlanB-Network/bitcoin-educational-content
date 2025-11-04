---
name: Dojo
description: Avoimen lähdekoodin Bitcoin-solmu yksityisyyttä ja autonomiaa varten
---

![cover](assets/cover.webp)



*Tämä opetusohjelma perustuu [viralliseen Ashigaru-dokumentaatioon](https://ashigaru.rs/docs/), jonka olen ottanut haltuun ja laajentanut. Olen kirjoittanut kaikki osiot uudelleen selkeyden parantamiseksi, lisännyt yksityiskohtaisempia selityksiä sekä kuvia aloittelijoille, jotta asennus ja käyttö olisi helpommin ymmärrettävää.*



---

Dojo on avoimen lähdekoodin ohjelma, joka on suunniteltu toimimaan tiettyjen yksityisyyteen keskittyvien Bitcoin-lompakoiden taustapalvelimena Bitcoin core-solmun pohjalta. Historiallisesti se kehitettiin toimimaan Samourai Wallet:n kanssa, joka oli mobiili Wallet, joka tarjosi kehittyneitä yksityisyysominaisuuksia, kuten Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... Samourai Wallet on nyt suljettu sen kehittäjien pidätyksen jälkeen, mutta sen yhteisöllinen seuraaja, **Ashigaru Wallet**, on ottanut sen haltuunsa ja luottaa edelleen Dojoon tarjotakseen täydellisen käyttökokemuksen käyttäjille, jotka haluavat pitää tietonsa hallinnassa Bitcoin:ää käyttäessään.



![Image](assets/fr/01.webp)



Käytännössä Dojo toimii yhdyskäytävänä Wallet:n ja Bitcoin-verkon välillä. Ilman Dojoa kevyt mobiili Wallet joutuisi kyselemään kolmannen osapuolen palvelimilta saadakseen UTXO:n ja historian tilan tai lähettääksesi tapahtumia. Tämä merkitsee riippuvuutta ja arkaluonteisten tietojen vuotamista kolmannen osapuolen palvelimelle (käytetyt osoitteet, summat, maksutiheys jne.). Dojon avulla isännöit itse tätä palvelinta, joka on suoraan yhteydessä omaan Bitcoin-solmuun. Näin kaikki salkkupyynnöt kulkevat hallitsemasi infrastruktuurin kautta ilman välikäsiä, mikä vahvistaa luottamuksellisuuttasi ja riippumattomuuttasi.



## Dojon perustamisen vaatimukset



Dojo-palvelimen perustaminen ei vaadi erittäin tehokasta konetta. Kuka tahansa, jolla on alkeistason tietokone, vakaa Internet-yhteys ja kyky jättää se jatkuvasti (24/7) päälle, voi perustaa toimivan Dojon.



### Valitse konetyyppi



Voit käyttää :




- kannettava tietokone ;
- pöytätietokone ;
- mini-PC (esim. Intel NUC, Lenovo Thincentre Tiny...).



Jokaisella vaihtoehdolla on omat etunsa ja haittansa:




- Hinta: kunnostettu mini-PC tai pöytäkone on usein halvempi kuin uusi kannettava tietokone.
- Jalanjälki: Mini-PC vie vähemmän tilaa.
- Virta Supply: kannettavan tietokoneen etuna on akku, joka tarkoittaa, että se ei sammu sähkökatkoksen sattuessa, toisin kuin minitietokone.
- Päivitettävyys: barboneihin voi yleensä lisätä muistia tai vaihtaa Hard-levyn helposti.



Jos haluat lisätietoja laitteiden valinnasta, suosittelen tätä kurssia:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Suositellut varusteet



Uutta konetta ei tarvitse ostaa. Kunnostettu tietokone, jonka tekniset tiedot ovat alla, tarjoaa paljon paremman suorituskyvyn kuin yhden piirilevyn elektroniikka (kuten Raspberry Pi).



**Vähimmäisvaatimukset:**




- X86-64-arkkitehtuuri (64-bittinen prosessori).
- 2 GHz:n kaksiytiminen prosessori tai nopeampi.
- vähintään 8 GB RAM-muistia.
- vähintään 2 TB:n NVMe SSD-levy (Blockchain:n ja Bitcoin:n sekä tarvittavien indeksien tallentamiseen).



**Suositeltu käyttöjärjestelmä: **




- Debian-pohjainen jakelu, kuten Ubuntu 24.04 LTS.



**Suositellut varusteet:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- jne.



Dojo-palvelimen käyttäminen muilla laitteistokokoonpanoilla on täysin mahdollista. Parhaan suorituskyvyn saamiseksi ja ongelmien rajoittamiseksi suosittelemme kuitenkin noudattamaan yllä olevia suosituksia.



Tässä ohjeessa käytän vanhaa ThinkCentre Tiny -tietokonetta, jossa on Intel Pentium Dual-Core G4400T -suoritin, 8 Gt RAM-muistia ja 2 TB SSD-levy.



## 1 - Ubuntun asentaminen



*Jos haluat asentaa Dojon laitteeseen, joka on jo määritetty, voit ohittaa tämän vaiheen ja siirtyä suoraan vaiheeseen 2.*



Kun olet valmistellut valitun laitteiston, on aika asentaa käyttöjärjestelmä. Voit käyttää käytännössä mitä tahansa Debian-jakelua, mutta suosittelen Ubuntun LTS-versiota, koska se sopii täydellisesti tarkoituksiimme. Tässä ovat seuraavat vaiheet:



### 1.1. luo käynnistettävä USB-levy



Lataa jo toimivalta tietokoneelta (tavalliselta koneeltasi) Ubuntu LTS ISO-kuva [viralliselta sivustolta](https://ubuntu.com/download/desktop) (tätä kirjoitettaessa versio on 24.04, mutta ota uusin, jos toinen on saatavilla).



![Image](assets/fr/02.webp)



Aseta vähintään 8 Gt:n USB-levy tähän tietokoneeseen ja luo käynnistyskelpoinen levy esimerkiksi [Balena Etcher] (https://etcher.balena.io/) -ohjelmalla. Valitse juuri lataamasi Ubuntu-ISO-kuva, valitse USB-tikku kohdelaitteeksi ja käynnistä sitten luomisprosessi (ole kärsivällinen, se voi kestää useita minuutteja).



![Image](assets/fr/03.webp)



Aseta käynnistettävä USB-levy tietokoneeseen, joka on sammutettu (siihen, jossa haluat käyttää Dojoa). Käynnistä kone ja paina heti **F12** tai **F10** näppäimistöllä (mallista riippuen) päästäksesi käynnistysvalikkoon. Valitse sitten USB-avaimesi ensisijaiseksi laitteeksi tietokoneen käynnistysjärjestyksessä.



![Image](assets/fr/04.webp)



### 1.2. asenna käyttöjärjestelmä



Ubuntun aloitusnäyttö tulee näkyviin. Valitse "Kokeile tai asenna Ubuntu*".



![Image](assets/fr/05.webp)



Seuraa sitten klassista Ubuntun asennusprosessia:




- Valitse kieli.
- Valitse näppäimistön tyyppi.
- Jos yhteys on muodostettu RJ45-kaapelilla, Wi-Fi-yhteyttä ei tarvitse määrittää.
- Napsauta "*Asenna Ubuntu*" ja valitse vaihtoehto, jossa voit asentaa kolmannen osapuolen ohjelmistoja (Wi-Fi-ajurit, multimediakoodekit jne.).
- Kun ohjattu asennusohjelma kysyy asennustyyppiä, valitse "*Poista levy ja asenna Ubuntu*". **Varoitus**: Tämä toiminto poistaa levyn sisällön kokonaan. Tarkista huolellisesti, että valitsemasi levy vastaa Dojoa varten tarkoitettua NVMe SSD-levyä.
- Luo yksinkertainen käyttäjänimi (esim. "*loic*").
- Määritä koneelle nimi (esim. "*dojo-node*").
- Aseta vahva salasana ja pidä se turvassa.
- Ota käyttöön "*Pyydä salasanaa kirjautuaksesi sisään*" -vaihtoehto turvallisuuden vahvistamiseksi.
- Ilmoita aikavyöhykkeesi ja napsauta sitten "*Asenna*".
- Odota, että asennus on valmis. Kun asennus on valmis, järjestelmä käynnistyy automaattisesti uudelleen.
- Poista USB-asennusavain, kun käynnistät tietokoneen uudelleen.



Lisätietoja Ubuntun asennusprosessista on erillisessä opetusohjelmassamme :



https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. järjestelmän päivitys



Avaa ensimmäisen käynnistyksen jälkeen pääte käyttämällä näppäinyhdistelmää ***Ctrl + Alt + T*** ja suorita seuraavat komennot järjestelmän päivittämiseksi:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Ulkorakennuksen asennus



Jotta Dojo toimisi kunnolla, järjestelmässäsi on oltava tietyt ohjelmistokivet. Niitä käytetään ohjelmistovarastojen hallintaan, viestintään, arkistojen purkamiseen ja Dojon suorittamiseen Docker-konttien sisällä. Kaikki nämä toiminnot suoritetaan terminaalissa.



### 2.1. Valmistelu



Seuraava komento palauttaa sinut henkilökohtaiseen kansioosi. Tämä on hyvä käytäntö ennen asennussarjan suorittamista.



```bash
cd ~/
```



Varmista ennen minkään ohjelmiston asentamista, että koneellasi käytettävissä olevien ohjelmistojen tietokanta on ajan tasalla. Näin vältytään vanhentuneiden versioiden asentamiselta.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. asenna apuohjelmat



Järjestelmään on lisättävä useita työkaluja:




- `apt-transport-https`: mahdollistaa pakettien lataamisen turvallisesti HTTPS:n kautta
- `ca-certificates`: hallitsee salattujen yhteyksien edellyttämiä varmenteita
- `curl`: tiedostojen hakeminen Internetistä
- `gnupg-agent`: GPG-avainten hallintaan
- software-properties-common`: tarjoaa apuohjelmia APT-tietovarastojen käsittelyyn
- `unzip`: purkaa ZIP-muotoiset tiedostot



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Asennuksen aikana järjestelmä saattaa pyytää sinulta vahvistusta. Paina "*y*"-näppäintä ja paina sitten "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. asenna Torsocks



Torsocks mahdollistaa tiettyjen komentojen suorittamisen Tor-verkon kautta, mikä parantaa viestinnän luottamuksellisuutta.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. asenna Docker ja Docker Compose



Dojo toimii Docker-konttien sisällä. Tämä tarkoittaa, että jokainen palvelu on eristetty itsenäiseen ympäristöön, mikä helpottaa ylläpitoa ja turvallisuutta. Tätä varten sinun on asennettava Docker ja Docker Compose -työkalu, jonka avulla voit hallita useita kontteja samanaikaisesti.



#### Lisää Dockerin allekirjoitusavain



Docker tarjoaa oman digitaalisen allekirjoitusavaimensa. Sen lisääminen varmistaa ladattujen pakettien aitouden.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Virallinen Docker-repository lisätty



Seuraavaksi sinun on kerrottava järjestelmälle, mistä viralliset Docker-paketit löytyvät. Tämä komento lisää uuden arkiston paketinhallinnan kokoonpanoon.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Dockerin ja Docker Composen asentaminen



Dockerin pääkomponentit voidaan nyt asentaa.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Käyttäjän valtuutus



Oletusarvoisesti vain järjestelmänvalvojan oikeuksilla suoritetut komennot voivat käynnistää Dockerin. Paremman mukavuuden vuoksi suosittelen, että lisäät nykyisen käyttäjän "*docker*"-ryhmään. Näin voit käyttää Dockeria ilman, että sinun tarvitsee kirjoittaa `sudo` joka kerta.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Yhden käyttäjän luominen (valinnainen)



Jos haluat parantaa järjestelmäsi turvallisuutta, suosittelen, että luot erillisen käyttäjän yksinomaan Dojon käyttöä varten. Tämä erottelu rajoittaa riskejä: jos Dojossa ilmenee tietoturvaongelma, se ei suoraan vaaranna päätiliäsi.



### 3.1. käyttäjätilin luominen



Seuraava komento luo uuden käyttäjän nimeltä "*dojo*". Tällä käyttäjällä on kotihakemisto `/home/dojo` ja pääsy bash-terminaaliin. Hänet lisätään myös sudo-ryhmään, jotta hän voi suorittaa admin-komentoja.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Salasanan asettaminen



On tärkeää antaa tälle tilille vahva salasana. Ihannetapauksessa sinun tulisi käyttää Bitwardenin kaltaista salasanahallintaohjelmaa generate:n pitkän, Hard:n arvoittavan yhdistelmän muodostamiseen.



```bash
sudo passwd dojo
```



Tämän jälkeen järjestelmä pyytää sinua syöttämään valitsemasi salasanan ja vahvistamaan sen toisen kerran.



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Käyttäjän valtuuttaminen Dockerin käyttöön



Jotta käyttäjä "*dojo*" voi käynnistää Dojon käyttämiseen tarvittavat kontit, hänet on lisättävä Docker-ryhmään. Näin vältytään siltä, että jokaista komentoa edeltää `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Järjestelmän uudelleenkäynnistys



Jotta ryhmämuutokset tulevat voimaan, kone on käynnistettävä uudelleen.



```bash
sudo reboot
```



### 3.5. Kirjaudu sisään uudella käyttäjällä



Kun järjestelmä käynnistyy uudelleen, kirjaudu sisään ***dojo***-tunnuksella ja aiemmin määrittelemälläsi salasanalla. Kaikki myöhemmät vaiheet on suoritettava tältä tililtä.



## 4. Lataa ja tarkista Dojo



Ennen Dojon asentamista on tärkeää varmistaa, että tiedostot ovat peräisin viralliselta kehittäjältä ja että niitä ei ole muutettu. Tämä vaihe perustuu PGP:n ja hashien käyttöön tiedostojen aitouden ja eheyden tarkistamiseksi.



### 4.1. tuo kehittäjän PGP-avain



Lataa kehittäjän julkinen avain Torin kautta ja tuo se paikalliseen avainketjuusi. Tätä avainta käytetään Dojo-tiedostoihin liittyvien allekirjoitusten tarkistamiseen.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. lataa Dojon uusin versio



Hae Dojon lähdekoodin sisältävä pakattu arkisto. Tässä esimerkissä uusin versio on `1.27.0`: muuta komentoa [uusin versio täällä virallisessa GitHub-arkistossa](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Lataa sormenjäljet ja allekirjoitus



Kehittäjät julkaisevat tiedoston, jossa luetellaan arkistojen digitaaliset sormenjäljet, sekä tiedoston, joka on allekirjoitettu heidän PGP-avaimellaan. Lataa ne, jotta voit vertailla tiedostoja paikallisesti.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Tarkista PGP-allekirjoitus



Tarkista, että sormenjälkitiedosto on allekirjoitettu tuodulla avaimella.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Oikea tulos näyttää kelvollisen allekirjoituksen, jossa on avain `E53AD419B242822F19E23C6D3033D463D6E544F6` ja siihen liittyvä Address `dojocoder@pm.me`. Näyttöön saattaa tulla varoitus, jonka mukaan avainta ei ole varmennettu: voit jättää sen huomiotta.



Jos taas allekirjoitus on virheellinen, lopeta asennusprosessi välittömästi ja aloita alusta.



![Image](assets/fr/17.webp)



### 4.5. Tarkista arkiston eheys



Laske ladatun tiedoston SHA256-sormenjälki ja avaa sitten sormenjälkitiedosto vertaillaksesi näitä kahta arvoa.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Jos nämä kaksi sormenjälkeä ovat identtiset, voit olla varma, että arkistoa ei ole muutettu. Jos ne eroavat toisistaan, älä jatka ja poista tiedostot.



![Image](assets/fr/18.webp)



### 4.6. Tiedostojen poimiminen ja järjestäminen



Kun varmennus on suoritettu onnistuneesti, voit purkaa arkiston ja valmistella Dojon asennukselle tarkoitetun kansion.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Siivoa tarpeettomat tiedostot



Poista väliaikaiset tiedostot ja arkistot, joita ei enää tarvita, jotta ympäristö pysyy siistinä.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Dojon konfigurointi



Dojo on taustapalvelin, joka kokoaa yhteen useita palveluja, joiden avulla voit olla vuorovaikutuksessa salkkusi kanssa ja hallita Bitcoin-solmua. Sen konfigurointi voi olla monimutkaista, mutta projekti tarjoaa yksinkertaistetun menetelmän, joka asentaa ja konfiguroi seuraavat komponentit automaattisesti:




- Dojo (tärkein API)
- Bitcoin core (täydellinen Bitcoin-solmu)
- BTC-RPC Explorer (verkko Block explorer)
- Fulcrum Indexer (lohkojen ja transaktioiden nopea indeksointi)
- Fulcrum Electrum Server saatavilla Tor-verkossa
- Fulcrum Electrum Server käytettävissä paikallisverkossa
- Hallinnon valtakirjat



### 5.1. hallintatiedot



Eri palveluihin pääsyn turvaamiseksi sinun on annettava generate useita yksilöllisiä tunnisteita:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_SALASANA`
- mYSQL_USER
- `MYSQL_PASSWORD`
- nODE_API_KEY`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SECRET` (SOLMU_JWT-SALAISUUS)



Näiden tunnusten **on oltava yksilöllisiä** (tämä on erittäin tärkeää: et saa käyttää samaa salasanaa useissa palveluissa), koostuttava ainoastaan numeroista, isoista ja pienistä kirjaimista (aakkosnumeerisia) ja oltava noin 40 merkkiä pitkiä korkean turvallisuustason takaamiseksi. Suosittelen jälleen kerran vahvasti salasanahallintaohjelman käyttöä.



### 5.2. Pääsy konfiguraatiotiedostoihin



Dojon asetustiedostot sijaitsevat `conf/`-kansiossa. Siirry tähän hakemistoon:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Bitcoin core-konfiguraatio



Avaa Bitcoin core-konfiguraatiotiedosto nano-tekstieditorilla:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



Kirjoita tähän tiedostoon luodut tunnukset:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Korvaa `your-ID-here` ja `your-password-here` omilla tunnuksillasi (vahvalla salasanalla).***



Voit myös säätää Bitcoin core:n käyttämän välimuistin kokoa parantaaksesi suorituskykyä (voit käyttää jopa enemmän, jos käytettävissä on paljon RAM-muistia):



```
BITCOIND_DB_CACHE=2048
```



Voit tallentaa muutokset ja sulkea editorin :




- paina `Ctrl + X
- tyyppi `y`
- paina sitten "*Enter*"



### 5.4. MySQL-konfiguraatio



Avaa sitten MySQL-tietokannan kokoonpano:



```bash
nano docker-mysql.conf.tpl
```



Anna kirjautumistietosi:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Korvaa `tunnuksesi-täällä` ja `salasanasi-täällä` omilla tunnuksillasi (vahvoilla, uniikeilla salasanoilla).*** ***



Tallenna samalla tavalla (`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. Fulcrum-indeksilaitteen kokoonpano



Avaa seuraava tiedosto:



```bash
nano docker-indexer.conf.tpl
```



Lisää parametrit Fulcrumin aktivoimiseksi ja sen integroimiseksi oikein Dojoon :



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Seuraavaksi on kaksi vaihtoehtoa, jotka riippuvat kokoonpanostasi. Jos Dojo on asennettu koneeseen, joka on erillään jokapäiväisestä tietokoneestasi (oma kone, palvelin...), anna sen IP Address lähiverkossasi, esimerkiksi :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Voit selvittää koneesi paikallisen IP Address:n avaamalla toisen päätteen ja kirjoittamalla seuraavan komennon:



```bash
hostname -I
```



Toinen mahdollisuus: jos Dojoa käytetään suoraan jokapäiväisellä tietokoneella, pidä oletusarvo, joka on jo olemassa asetustiedostossa :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Tallenna ja poistu editorista (`Ctrl + X`, `y`, "*Enter*").



### 5.6. Solmupalvelun konfigurointi



Avaa lopuksi Dojo-pääpalvelun konfiguraatio:



```bash
nano docker-node.conf.tpl
```



Anna kirjautumistietosi:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Korvaa `your-password-here` omilla tunnuksillasi (vahvoilla, uniikeilla salasanoilla).***



![Image](assets/fr/26.webp)



Aktivoi sitten paikallinen indeksoija:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Tallenna ja poistu editorista (`Ctrl + X`, `y`, "*Enter*").



### 5.7. Kirjautumisen hallinta



Kun konfigurointi on valmis, kaikkia luotuja tunnisteita ei tarvitse tallentaa. Ainoa, joka on ehdottomasti tallennettava, on :



```
NODE_ADMIN_KEY
```



Tämän käyttäjätunnuksen avulla voit myöhemmin kirjautua Dojon ylläpitotyökaluun. Kaikki muut kirjautumistunnukset voidaan poistaa salasanahallinnasta tai käsinkirjoitetuista muistiinpanoista. Ne pysyvät saatavilla Dojon asetustiedostoista, jos tarvitset niitä tulevaisuudessa.



## 6. Dojon asennus



Tässä vaiheessa Dojo asennetaan ja käynnistetään koneellesi. Toiminto käynnistää useita palveluja (Bitcoin core, Fulcrum-indeksoija, Dojon taustapalvelu jne.) ja aloittaa Blockchain Bitcoin:n täydellisen synkronoinnin. Tämä voi kestää useita päiviä laitteistostasi ja Internet-yhteydestäsi riippuen.



### 6.1. Tarkista, että Docker toimii oikein



Varmista ennen asennuksen aloittamista, että Docker on toiminnassa. Suorita seuraava komento:



```bash
docker run hello-world
```



Tämä komento lataa ja käynnistää pienen testisäiliön. Jos kaikki toimii oikein, sinun pitäisi nähdä samanlainen viesti kuin :



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Jos tämä viesti ei tule näkyviin, aloita koneen uudelleenkäynnistäminen komennolla :



```bash
sudo reboot
```



Kirjaudu sitten takaisin **dojo**-tilillesi ja suorita testikomento uudelleen. Jos virhe jatkuu, Dockeria ei ole asennettu oikein. Tässä tapauksessa palaa vaiheeseen `2.4.` Dockerin asentamisesta ja tarkista jokainen komento huolellisesti.



### 6.2. Siirry Dojon asennushakemistoon



Asennuksessa tarvittavat skriptit sijaitsevat `my-dojo`-kansiossa. Siirry tähän hakemistoon:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Tarkista komennolla `ls`, että tiedosto `dojo.sh` on olemassa. Tämä on pääskripti, joka automatisoi Dojon asennuksen ja kaikkien sen palveluiden käynnistämisen.



![Image](assets/fr/29.webp)



### 6.3. Aloita asennus



Aloita asennus suorittamalla :



```bash
./dojo.sh install
```



Vahvista asennus painamalla `y` ja sitten "*Enter*".



![Image](assets/fr/30.webp)



Tämä skripti :




- lataa ja käynnistä tarvittavat Docker-säiliöt,
- alustaa Bitcoin core ja aloittaa Blockchain:n synkronoinnin,
- käynnistää Fulcrum-indeksointiohjelman tapahtumien ja osoitteiden seuraamiseksi,
- aktivoida Dojon taustapalvelun ja sen API:t.



Tulet näkemään tasaisen virran lokitietoja, joissa on värikkäitä viittauksia kuten `bitcoind`, `soroban`, `nodejs` tai `fulcrum`. Tämä vieritys osoittaa, että Dojo on käynnissä ja alkaa suorittaa eri palveluita.



![Image](assets/fr/31.webp)



### 6.4. Poistu lokinäytöstä



Lokit näkyvät reaaliajassa päätelaitteessasi. Voit palata komentoriville Dojon ollessa käynnissä taustalla kirjoittamalla :



```
Ctrl + C
```



Älä huoli: lokinäytön pysäyttäminen ei pysäytä palveluita. Docker jatkaa Dojon suorittamista taustalla (tietokonetta ei tietenkään tarvitse pysäyttää, jos haluat IBD:n jatkuvan).



### 6.5. Ymmärtäminen *Initial Block Download* (IBD) (alkulohkolataus)



Käynnistettäessä Bitcoin core:n on ladattava ja tarkistettava koko Blockchain vuodesta 2009 lähtien. Tätä vaihetta kutsutaan nimellä ***Initial Block Download* (IBD)**. Se on olennaisen tärkeää, sillä sen avulla Dojo-solmu voi tarkistaa jokaisen Bitcoin-lohkon ja transaktion itsenäisesti.



Tämän synkronoinnin kesto riippuu useista tekijöistä:




- prosessorin teho ja käytettävissä olevan RAM-muistin määrä,
- levyn nopeus,
- solmun yhteyden muodostavien vertaisverkkojen määrä ja laatu,
- internet-yhteytesi nopeus.



Käytännössä tämä toimenpide kestää yleensä **2-7 päivää**. Tänä aikana voit jättää koneen jatkuvasti käyntiin. Mitä pidempään kone on päällä, sitä nopeammin synkronointi valmistuu. Suosittelen tarkistamaan synkronoinnin tilan säännöllisesti katsomalla Bitcoin core:n lokitietoja tai käyttämällä Dojon ylläpitotyökalua, kun se on asennettu (katso seuraava kohta).



Jos haluat syventää tietämystäsi IBD:stä ja yleisemmin Bitcoin-solmun toiminnasta ja roolista, suosittelen, että katsot tämän kurssin:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Synkronoinnin valvonta



Kun asennat Dojon ensimmäistä kertaa, sinun on odotettava, että kaksi pääasiallista toimenpidettä on suoritettu loppuun: Blockchain Bitcoin:n (*IBD*) täydellinen lataaminen ja Fulcrumin suorittama Blockchain:n indeksointi. Yhteydestäsi ja koneesi tehosta riippuen tämä voi kestää useita päiviä. Tänä aikana voit seurata prosessin etenemistä varmistaaksesi, että kaikki sujuu ongelmitta.



Synkronoinnin tilaa voidaan seurata kahdella tavalla:




- dojon ylläpitotyökalun (DMT) käyttö, joka on yksinkertainen mutta antaa vain vähän tietoja IBD:n aikana;
- suora kuuleminen koneesi Dojo-lokeista, teknisempi mutta paljon tarkempi.



### 7.1. Tarkista Dojon ylläpitotyökalun (DMT) avulla



Dojo-huoltotyökalu on suojattu, verkkopohjainen Interface, jonka avulla voit seurata laitoksesi tilaa ja suorittaa tiettyjä toimintoja. Se on helpoin ja helppokäyttöisin tapa seurata IBD:n edistymistä. Alkuvaiheen synkronointivaiheessa näytettävät tiedot voivat olla rajoitettuja. DMT ei esimerkiksi näytä yksityiskohtaisesti Fulcrum-indeksoinnin edistymistä. Toisaalta, kun synkronointi on valmis, DMT näyttää selvästi :




- kaikki Green:n valot;
- kunkin palvelun (solmu, indeksoija, Dojo DB) viimeinen validoitu lohko.



Jotta voit käyttää sitä, sinun on tiedettävä DMT:n URL-osoite ja muodostettava yhteys siihen [Tor-selaimen kautta](https://www.torproject.org/download/). Avaa terminaali ja siirry hakemistoon `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Suorita sitten seuraava komento:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Sen jälkeen sinulla on pääsy kaikkiin tietoihin, jotka liittyvät Dojoon Torin kautta tehtyihin yhteyksiin. Tässä meitä kiinnostaa seuraava URL-osoite:



```
Dojo API and Maintenance Tool =
```



Jos haluat käyttää DMT:tä mistä tahansa koneesta missä tahansa verkossa (jopa etänä), avaa Tor Browser ja kirjoita tämä URL-osoite, jota seuraa `/admin`. Jos URL-osoitteesi on esimerkiksi `wo4zobymdl45gmmzzmpoypepeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, sinun on syötettävä [Tor Browser](https://www.torproject.org/download/) -palkkiin:



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Pitäkää tämä Address ehdottoman luottamuksellisena



Tämän jälkeen sinut ohjataan todennussivulle. DMT:hen kirjaudutaan sisään aiemmin luomallasi `NODE_ADMIN_KEY`-salasanalla.



![Image](assets/fr/33.webp)



Kun olet kirjautunut sisään, pääset käyttämään *Dojon ylläpitotyökalua*! IBD:n aikana näet "*Latest Block*" -tiedot "*Full node*"-valikossa, josta tiedät Bitcoin-solmusi nykyisen tilan.



![Image](assets/fr/34.webp)



Muista merkitä tämä Address kirjanmerkiksi Tor Browserissa, jotta se on helppo hakea myöhemmin.



Kun Dojo on täysin synkronoitu, sinun pitäisi nähdä Green check ✅ kaikissa DMT:n etusivun indikaattoreissa.



### 7.2. Varmennus Dojon lokien avulla



Toinen tapa seurata IBD:n etenemistä on tarkastella suoraan koneen lokitietoja. Tämä lähestymistapa tarjoaa paljon tarkempaa reaaliaikaista seurantaa. Näet, miten Bitcoin core edistyy lohkojen lataamisessa ja miten Fulcrum indeksoi ne.



Yhdistä koneeseen, jossa Dojo sijaitsee, ja avaa terminaali. Kaikki komennot on suoritettava hakemistosta `my-dojo`. Asetu tähän kansioon:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Bitcoin core lokit



Tarkastele Bitcoin core-lokeja IBD:n edistymisen seuraamiseksi:



```bash
./dojo.sh logs bitcoind
```



Alussa näet lohkootsikoiden esisynkronointivaiheen:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Kun tämä luku saavuttaa 100 prosenttia, Bitcoin core aloittaa Blockchain:n täydellisen lataamisen. Näet IBD:n edistymisen. Voit selvittää lohkon nykyisen korkeuden katsomalla `height=`-arvolla ilmoitettua arvoa. Voit myös seurata avainta `progress=`, joka ilmoittaa IBD:n edistymisen prosentuaalisen osuuden.



![Image](assets/fr/36.webp)



Kuten aina, voit sulkea lokit ja palata komentokehotteeseen näppäinyhdistelmällä `Ctrl + C`.



#### Fulcrum lokit



Kun Bitcoin core on suorittanut otsikon esisynkronoinnin, Fulcrum aloittaa Blockchain:n indeksoinnin sitä mukaa kuin se etenee. Tarkastele sen lokitietoja :



```bash
./dojo.sh logs fulcrum
```



Näet sitten viimeisimmän indeksoidun lohkon korkeuden, joka näkyy `height:` jälkeen, sekä indeksoinnin edistymisprosentin.



![Image](assets/fr/37.webp)



### 7.3. Fulcrum-tietokannan korruptoituminen



Fulcrum on erityisen tehokas indeksoija, mutta sen asennus voi olla monimutkaista, eikä vähiten sen herkän tietokannan hallinnan vuoksi. Jos sähköt katkeavat tai kone pysähtyy äkillisesti synkronoinnin alkuvaiheessa, indeksoijan tietokanta voi vahingoittua. Tämän voi huomata esimerkiksi seuraavista lokitiedostoista:



```bash
fulcrum | The database has been corrupted etc...
```



**Huomautus:** Tämän tyyppinen virhe pitäisi korjata Fulcrum 2.0:n tulevassa julkaisussa.



Jos sinulle käy näin, sillä ei ole vaikutusta bitcoind:een (Bitcoin-solmuun): sen IBD etenee Fulcrumista riippumatta. Et kuitenkaan voi käyttää Fulcrumia ennen kuin olet poistanut sen vioittuneet tiedot ja käynnistänyt sen synkronoinnin alusta. Näin se toimii:



Lopeta Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Poista vain Fulcrum-säiliö ja -tilavuus:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Normaalisti nimi on `my-dojo_data-fulcrum`, jos tämä ei ole sinun tapauksessasi, sovita edellisen komennon palauttamaa nimeä.



Käynnistä sitten Dojo uudelleen ja rakenna Fulcrum uudelleen tyhjästä:



```bash
./dojo.sh upgrade
```



Tämän jälkeen voit tarkistaa, että Fulcrum toimii oikein, tarkastelemalla lokitietoja:



```bash
docker logs -f fulcrum
```




## 8. Dojon ylläpitotyökalun käyttäminen



Kun Bitcoin-solmusi on synkronoitu loimipäähän eniten Proof of Work:llä ja Fulcrum on indeksoinut Blockchain:n 100-prosenttisesti, voit aloittaa Dojon käytön.



Dojo tarjoaa laajan valikoiman ominaisuuksia, joita parannetaan säännöllisesti jokaisen uuden version myötä. Mielestäni 2 tärkeintä ovat :




- mahdollisuus liittää Ashigaru Wallet -laitteesi omaan solmuun Blockchain:n tietojen käyttämiseksi ja tapahtumien lähettämiseksi,
- ja Block explorer, jonka avulla saat Blockchain Bitcoin:n tiedot käyttöösi ilman, että paljastat tietojasi ulkopuoliselle instanssille, jota et hallitse.



Selvitetään, miten niitä käytetään.


### 8.1. Yhdistä Ashigaru Dojoon



Ashigaru Wallet:n liittäminen Dojoon on hyvin yksinkertaista: kun olet DMT:ssä, avaa "*Pairing*"-valikko. Näyttöön ilmestyy QR-koodi, jonka voit skannata suoraan Ashigaru-sovelluksella.



![Image](assets/fr/38.webp)



Kun käynnistät Ashigaru-sovelluksen ensimmäisen kerran Wallet:n luomisen tai palauttamisen jälkeen, sinut ohjataan "*Konfiguroi Dojo-palvelimesi*" -sivulle. Paina "*Scan QR*" ja skannaa sitten DMT:ssäsi näkyvä QR-koodi.



![Image](assets/fr/39.webp)



Napsauta sitten painiketta "*Jatka*".



![Image](assets/fr/40.webp)



Olet nyt yhteydessä Dojoon.



![Image](assets/fr/41.webp)



### 8.2. Block explorer:n käyttö



Dojo asentaa automaattisesti Block explorer:n, [BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer), joka käyttää suoraan oman Bitcoin-solmusi tietoja. Explorerin avulla pääset käsiksi Blockchain:n ja oman Mempool:n raakatietoihin helppotajuisen Interface-verkon kautta. Näin voit esimerkiksi tarkistaa vireillä olevan transaktion tilan, tarkastella Address:n saldoa tai tutkia lohkon koostumusta helposti.



Voit käyttää sitä yksinkertaisesti hakemalla Tor Address:n selaimellasi. Suorita tätä varten sama komento, jota käytit saadaksesi DMT:n Address:n:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Pääset käsiksi kaikkiin Dojo-yhteystietoihisi Torin kautta. Tässä meitä kiinnostaa seuraava URL-osoite:



```
Block Explorer =
```



Jos olet jo yhteydessä DMT:hen, löydät tämän Address:n myös "*Pairing*"-valikosta, yhteyden JSONin sisältä:



![Image](assets/fr/43.webp)



Jos haluat käyttää selainta mistä tahansa koneesta missä tahansa verkossa (jopa etänä), avaa [Tor Browser](https://www.torproject.org/download/) ja syötä juuri hakemasi URL-osoite.



⚠️ **Pitäkää tämä Address ehdottoman luottamuksellisena



Sen jälkeen saat käyttöösi oman Block explorer:n.



![Image](assets/fr/44.webp)



*Kuvan luotto: https://ashigaru.rs/.*



Jos haluat seurata tapahtumaa, kirjoita sen txid oikeassa yläkulmassa olevaan hakupalkkiin.



![Image](assets/fr/45.webp)



*Kuvan luotto: https://ashigaru.rs/.*



Jos haluat tarkistaa Address:aan liittyvät liikkeet, toimi samalla tavalla syöttämällä Address hakupalkkiin.



![Image](assets/fr/46.webp)



*Kuvan luotto: https://ashigaru.rs/.*



Voit myös syöttää lohkon Hash tai korkeuden hakupalkkiin saadaksesi näkyviin yksityiskohdat.



![Image](assets/fr/47.webp)



*Kuvan luotto: https://ashigaru.rs/.*



## 9. Dojon ylläpito



### 9.1 Pysäytä Dojo



Älä koskaan katkaise Dojon virtaa äkillisesti, sillä se voi vahingoittaa tiettyjä tietokantoja, erityisesti Fulcrum-indeksointia. Jos joudut sammuttamaan sen, sammuta Dojo aina puhtaasti ja sammuta myös kone, kun kaikki toimenpiteet on suoritettu:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Päivitä Dojosi



Dojo kehittyy säännöllisesti ja uusia versioita julkaistaan virheiden korjaamiseksi, vakauden parantamiseksi ja ominaisuuksien lisäämiseksi. Siksi on tärkeää [tarkistaa säännöllisesti päivitykset](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) ja päivittää Dojo. Prosessi on samanlainen kuin alkuperäinen asennus, mutta se edellyttää tiettyjen tiedostojen korvaamista uusimmalla saatavilla olevalla versiolla säilyttäen samalla kokoonpanosi. Tässä ovat yksityiskohtaiset vaiheet, joita on noudatettava puhdasta ja turvallista päivitystä varten:



Voit selvittää Dojon nykyisen version suorittamalla komennon :



```bash
./dojo.sh version
```



Vaikka tämä vaihe on vapaaehtoinen, suosittelen, että aloitat päivittämällä käyttöjärjestelmäsi. Tämä vähentää yhteensopimattomuuksien riskiä ja varmistaa, että Dojon käyttämät riippuvuudet ovat ajan tasalla:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Siirry Dojo-hakemistoon ja pysäytä nykyiset palvelut:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Käynnistä sitten järjestelmä uudelleen, jotta saat puhtaalta pöydältä:



```bash
sudo reboot
```



Dojon mukana toimitetaan digitaalisesti allekirjoitetut tiedostot. Nämä PGP-allekirjoitukset varmistavat, että tiedostot ovat peräisin kehittäjältä eikä niitä ole muutettu millään tavalla. On tärkeää tarkistaa ne joka kerta, kun päivität Dojon, aivan kuten teit, kun asensit sen ensimmäisen kerran. Aloita lataamalla kehittäjän julkinen avain Torin kautta ja tuo se sitten :



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Palaa henkilökohtaiseen hakemistoosi:



```bash
cd ~/
```



Lataa Dojon uusin versio GitHubista Torin kautta. Tässä esimerkissä se on versio `1.28.0` (jota ei ole vielä olemassa tätä kirjoitettaessa: tämä on vain esimerkki). Muista korvata tiedosto ja linkki [haluamallasi versiolla](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Lataa myös tiedosto, joka sisältää PGP-sormenjäljet ja allekirjoituksen (muista jälleen kerran säätää versio komennossa):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Tarkista, että ladattu sormenjälkitiedosto on allekirjoitettu kehittäjän avaimella:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Oikean tuloksen pitäisi näkyä :



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Näyttöön saattaa tulla varoitus siitä, että avain ei ole varmennettu, mutta sillä ei ole merkitystä. Jos taas allekirjoitus on virheellinen tai vastaa toista avainta, älä jatka eteenpäin vaan aloita alusta ja tarkista linkit.



Laske sitten arkiston SHA256-sormenjälki ja vertaa sitä viralliseen sormenjälkitiedostoon :



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Jos molemmat sormenjäljet täsmäävät täydellisesti, arkisto on aito ja ehjä. Jos ne eroavat toisistaan, poista tiedostot välittömästi äläkä jatka.



Pura arkisto kotihakemistossasi:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Kopioi sitten sisältö Dojo-hakemistoon ja korvaa vanha :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Tämä toiminto säilyttää konfiguraatiotiedostot, jotka sijaitsevat osoitteessa `~/dojo-app/docker/my-dojo/conf`, mutta korvaa kaikki muut tiedostot päivitetyillä versioilla.



Poista tarpeettomat tiedostot, jotta ympäristö pysyy siistinä :



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Palaa Dojon skriptihakemistoon ja suorita päivityskomento:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Tämä komento ohjaa Dockeria rakentamaan kuvat uudelleen uusilla tiedostoilla ja käynnistämään kaikki palvelut automaattisesti uudelleen. Tarkista prosessin lopussa lokit varmistaaksesi, että Bitcoin core, Fulcrum ja Dojo toimivat oikein:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Jos palvelut käynnistyvät virheettömästi ja lokit osoittavat, että lohkoja käsitellään, Dojo on nyt ajan tasalla ja toiminnassa.