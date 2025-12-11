---
name: Plan ₿ Academy - Pears App
description: Miten Plan ₿ Academy -sovellus asennetaan ja käytetään Pearsissä?
---

![cover](assets/cover.webp)


Tiedät varmaan jo, että Plan ₿ Academy on suurin Bitcoin:lle omistettu koulutustietokanta, johon on koottu kursseja, opetusohjelmia ja tuhansia avoimen lähdekoodin resursseja. Alun perin Plan ₿ Academy oli verkkosivusto. Mutta mitä tapahtuisi, jos siihen ei enää pääsisi normaalisti käsiksi, esimerkiksi sensuurin vuoksi?


Tässä opetusohjelmassa opettelemme, miten **Plan ₿ Academy** -alustaa voidaan käyttää todella sensuurin kestävällä tavalla käyttäen **Pears**:ia, **Holepunchin** kehittämää ja **Tetherin** tukemaa vertaisverkkoteknologiaa (P2P).


Pears on ohjelmisto, jonka avulla voimme käyttää Plan ₿ Academy -alustaa ilman keskitettyä verkkosivustoa. Tässä ohjeessa asennamme Pearsin tietokoneellesi, jotta voit käyttää Plan ₿ Academya Pearsin kautta.


Pearsin tavoite on yksinkertainen: mahdollistaa verkkosovellusten jakelu ja käyttö ilman keskitettyä infrastruktuuria (ei palvelimia, ei isäntiä, ei välikäsiä). Toisin sanoen, vaikka pilvipalveluntarjoaja sulkeutuisi tai jokin maa estäisi verkkotunnuksen käytön, sovellus jatkaa elämäänsä verkon vertaisverkkojen kesken. Tämän lähestymistavan ansiosta koulutusalustamme Plan ₿ Academy pysyy käytettävissä maailmanlaajuisesti ilman yksittäistä vikapistettä.


---

**TL;DR:**



- Asenna päärynät;



- Käynnistä Plan ₿ Academy -sovellus seuraavalla komennolla:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Mitä päärynät ovat?


Pears on yhtä aikaa ajoympäristö, kehitystyökalu ja jakelualusta vertaissovelluksille. Tämän avoimen lähdekoodin työkalun avulla voit rakentaa, jakaa ja käyttää ohjelmistoja ilman palvelimia tai infrastruktuuria suoraan käyttäjien kesken. Käytännössä tämä tarkoittaa sitä, että sen sijaan, että sovellus olisi keskitetysti palvelimella, jokaisesta käyttäjästä tulee verkon solmu: hän jakaa osan sovelluksesta ja dataa muiden vertaisvertaisten kanssa. Koko järjestelmä muodostaa hajautetun verkon, jossa kukin instanssi tekee yhteistyötä pitääkseen palvelun saatavilla.


![Image](assets/fr/01.webp)


Tämä lähestymistapa perustuu Holepunchin kehittämiin modulaarisiin ohjelmistokomponentteihin:



- Hypercore**: hajautettu loki, joka varmistaa tietojen yhdenmukaisuuden ja turvallisuuden ilman keskustietokantaa.
- Hyperbee**: Hypercoren päälle rakennettu indeksi, jonka avulla tietoja voidaan järjestää ja hakea tehokkaasti.
- Hyperdrive**: hajautettu tiedostojärjestelmä, jota käytetään sovellustiedostojen tallentamiseen ja synkronointiin vertaisverkon kesken.
- Hyperswarm** ja **HyperDHT**: verkkokerrokset, jotka mahdollistavat vertaisten löytämisen ja yhteydet maailmanlaajuisesti ilman keskitettyä palvelinta.
- Secretstream**: päästä päähän -salausprotokolla, joka turvaa vertaisverkkojen välisen viestinnän.


Näitä komponentteja yhdistämällä Pears mahdollistaa itsenäisten, salattujen ja hajautettujen sovellusten luomisen, joissa jokainen käyttäjä osallistuu aktiivisesti verkkoon. Tämä hajautettu arkkitehtuuri poistaa infrastruktuurikustannukset, sensuuririskit ja SPOF:t (*Single Points of Failure*).


Pearsin on kehittänyt Holepunch, Mathias Buusin ja Paolo Ardoinon (Tetherin toimitusjohtaja ja Bitfinexin teknologiajohtaja) perustama yritys, jonka tehtävänä on laajentaa vertaisvertaislogiikkaa Bitcoin:n ulkopuolelle. Heidän tavoitteenaan on rakentaa "vertaisverkon* internet", jossa jokainen sovellus voi toimia ilman lupaa, ilman palvelimia ja ilman välikäsiä. Holepunch on jo **Keet**:n takana, joka on täysin P2P-videoneuvottelu- ja viestisovellus.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Tämä Pearsin asennusopas on jaettu useisiin osiin käyttöjärjestelmästäsi riippuen. Siirry suoraan ympäristöäsi vastaavaan osaan ja seuraa asianmukaisia ohjeita:*



- Linux (Debian)** → Jakso **2**
- Ikkunat** → jakso **3**
- macOS** → jakso **4**


## 2. Kuinka asentaa Pears Linuxiin (Debian)?


Pearsin asentaminen Debianiin on suhteellisen yksinkertaista, mutta se vaatii muutamia ennakkoedellytyksiä, joista kerromme tarkemmin tässä osiossa.


### 2.1. Päivitä järjestelmä


Ennen kaikkea on tärkeää varmistaa, että järjestelmäsi on ajan tasalla.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Asenna riippuvuudet


Pears luottaa joihinkin järjestelmäkirjastoihin, kuten `libatomic1`, jota Bare JavaScript -ajoaikamoottori käyttää. Asenna se seuraavalla komennolla:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Asenna Node.js ja npm NVM:n kautta


Pears jaetaan *npm*:n, *Node.js*-pakettihallinnan* kautta. Vaikka Pears ei ole suoraan riippuvainen *Node.js*:stä toimiakseen, sitä tarvitaan asennuksessa. Suositeltava tapa asentaa *Node.js* Linuxiin on *NVM* (*Node Version Manager*), jonka avulla voit hallita useita Node-versioita rinnakkain.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Lataa sitten päätelaite uudelleen aktivoidaksesi *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Tarkista, että *NVM* on asennettu oikein:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Asenna seuraavaksi *Node.js*:n vakaa versio (esimerkiksi nykyinen LTS-versio):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Tarkista, että *Node.js* ja *npm* on asennettu oikein:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Asenna Pears npm:llä


Kun *npm* on käytettävissä, voit asentaa Pears CLI:n järjestelmääsi. Näin voit ajaa `pear`-komennon mistä tahansa hakemistosta.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Päärynöiden alustaminen


Asennuksen jälkeen suorita terminaalissa seuraava komento:


```bash
pear
```


Ensimmäisellä käynnistyskerralla Pears muodostaa yhteyden vertaisverkkoon ladatakseen tarvittavat komponentit. Tämä prosessi ei perustu mihinkään keskitettyyn palvelimeen - tiedostot haetaan suoraan muilta vertaisvertaisverkoilta.


![Image](assets/fr/10.webp)


Kun lataus on valmis, suorita komento uudelleen varmistaaksesi, että kaikki toimii:


```bash
pear
```


![Image](assets/fr/11.webp)


Jos kaikki on asennettu oikein, Pearsin ohjevalikko tulee näkyviin, ja siinä on luettelo käytettävissä olevista komennoista.


### 2.6. Testaa päärynät Keetillä


Voit tarkistaa, että Pears on täysin toimintakykyinen, käynnistämällä verkossa olevan P2P-sovelluksen, kuten Holepunchin kehittämän avoimen lähdekoodin Keet-viesti- ja videoneuvotteluohjelmiston.


```bash
pear run pear://keet
```


Tämä komento lataa Keet-sovelluksen suoraan Pears-verkosta ilman keskitettyä palvelinta. Jos Keet käynnistyy oikein, se tarkoittaa, että Pears-asennus on täysin toimiva.


![Image](assets/fr/12.webp)


Linux-järjestelmäsi on nyt valmis ajamaan ja isännöimään vertaisverkkosovelluksia Pearsin avulla.


## 3. Kuinka asentaa Pears Windowsissa


Pearsin asentaminen Windowsille on yhtä helppoa kuin Linuxille, mutta se vaatii muutamia erityisiä työkaluja.


*Jos käytät Linuxia ja olet jo asentanut Pearsin, voit siirtyä suoraan **vaiheeseen 5**.*


### 3.1. Avaa PowerShell järjestelmänvalvojana


Käynnistä ensin PowerShell järjestelmänvalvojan oikeuksin:



- Napsauta Käynnistä-valikkoa;
- Kirjoita "PowerShell";
- Napsauta hiiren kakkospainikkeella "*Windows PowerShell*";
- Valitse "*Ajeta järjestelmänvalvojana*".


![Image](assets/fr/15.webp)


### 3.2. Lataa NVS


Pears asennetaan *npm*:n, *Node.js*-paketinhallintaohjelman, kautta. Windowsissa Holepunchin suosittelema menetelmä on käyttää *NVS*:ää (*Node Version Switcher*), joka on vakaampi kuin *NVM* tässä järjestelmässä.


Asenna *NVS*:n uusin versio PowerShellissä suorittamalla seuraava komento:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Asenna Node.js


Käynnistä PowerShell uudelleen asennuksen jälkeen ja anna sitten seuraava komento:


```powershell
nvs
```


Näet luettelon saatavilla olevista *Node.js*-versioista. Valitse ensimmäinen painamalla näppäimistön a-näppäintä.


![Image](assets/fr/17.webp)


*Node.js* on nyt asennettu.


![Image](assets/fr/18.webp)


### 3.4. Tarkista asennukset


Varmista, että *Node.js* ja *npm* ovat käytettävissä:


```powershell
node -v
npm -v
```


Molempien komentojen pitäisi palauttaa versionumero.


![Image](assets/fr/19.webp)


### 3.5. Asenna Pears npm:llä


Kun *Node.js* ja *npm* ovat käytettävissä, asenna **Pears CLI** globaalisti järjestelmääsi:


```powershell
npm install -g pear
```


Tämä asentaa `pear`-binaryn globaaliin *npm*-hakemistoosi.


![Image](assets/fr/20.webp)


### 3.6. Päärynöiden tarkistaminen ja alustaminen


Kun asennus on valmis, suorita:


```powershell
pear
```


Ensimmäisellä käynnistyskerralla Pears lataa tarvittavat komponentit automaattisesti vertaisverkosta. Tämä prosessi voi kestää muutaman hetken.


![Image](assets/fr/21.webp)


Jos kaikki sujui hyvin, sinun pitäisi nähdä Pearsin CLI-apuvalikko ja luettelo käytettävissä olevista alakomennoista (run, seed, info...).


### 3.7. Testaa päärynät Keetillä


Voit tarkistaa, että Pears on täysin toimintakykyinen, käynnistämällä verkossa olevan P2P-sovelluksen, kuten Holepunchin kehittämän avoimen lähdekoodin Keet-viesti- ja videoneuvotteluohjelmiston.


```bash
pear run pear://keet
```


Tämä komento lataa Keet-sovelluksen suoraan Pears-verkosta ilman keskitettyä palvelinta. Jos Keet käynnistyy onnistuneesti, se tarkoittaa, että Pears-asennus on täysin toimiva.


![Image](assets/fr/22.webp)


Windows-järjestelmäsi on nyt valmis ajamaan ja isännöimään vertaisverkkosovelluksia Pearsin avulla.


## 4. Kuinka asentaa Pears macOS:lle


Pearsin asentaminen macOS-käyttöjärjestelmään on samanlaista kuin Linuxissa, mutta se vaatii muutamia Applen ympäristöön liittyviä mukautuksia. Käydään nämä vaiheet läpi yhdessä.


*Jos käytät Linuxia tai Windowsia ja olet jo asentanut Pearsin, voit siirtyä suoraan **vaiheeseen 5**.*


### 4.1. Tarkista järjestelmän edellytykset


Varmista ennen asennusta, että *Xcode Command Line Tools* on asennettu järjestelmääsi. Tämä paketti tarjoaa tarvittavat rakennustyökalut *Node.js:lle* ja sen riippuvuuksille.


Voit tehdä tämän avaamalla terminaalin pikanäppäimellä `Cmd + välilyönti`, kirjoittamalla `Terminaali` ja painamalla `Enter`. Suorita sitten terminaalissa seuraava komento sen asentamiseksi:


```bash
xcode-select --install
```


Jos työkalut on jo asennettu järjestelmääsi, macOS ilmoittaa siitä sinulle.


### 4.2. Asenna NVM


Pears jaetaan *npm*:n, *Node.js*-paketinhallintaohjelman, kautta. Vaikka Pears ei ole suoraan riippuvainen *Node.js*:stä toimiakseen, sitä tarvitaan asennuksessa. Suositeltava tapa asentaa *Node.js* macOS:lle on *NVM* (*Node Version Manager*), jonka avulla voit hallita useita Node-versioita samanaikaisesti.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Lataa sitten päätelaite uudelleen aktivoidaksesi *NVM*:


```bash
source ~/.zshrc
```


Jos käytät *bash*:a *zsh*:n sijasta, suorita:


```bash
source ~/.bashrc
```


Tarkista seuraavaksi, että *NVM* on asennettu oikein:


```bash
nvm --version
```


Päätelaitteesi pitäisi näyttää asennetun *NVM*-version.


### 4.3. Asenna Node.js ja npm


Asenna seuraavaksi *Node.js*:n vakaa versio (esimerkiksi nykyinen LTS-versio):


```bash
nvm install --lts
```


Kun asennus on valmis, tarkista asennetut versiot:


```bash
node -v
npm -v
```


Molempien komentojen pitäisi palauttaa versionumero.


### 4.4. Asenna Pears npm:llä


Kun *npm* on käytettävissä, voit asentaa Pears CLI:n järjestelmääsi. Näin voit suorittaa `pear`-komennon mistä tahansa hakemistosta.


```bash
npm install -g pear
```


### 4.5. Päärynöiden alustaminen


Asennuksen jälkeen suorita terminaalissa seuraava komento:


```bash
pear
```


Ensimmäisellä käynnistyskerralla Pears muodostaa yhteyden vertaisverkkoon ladatakseen tarvittavat komponentit. 


Kun lataus on valmis, suorita komento uudelleen varmistaaksesi, että kaikki toimii:


```bash
pear
```


Jos kaikki on asennettu oikein, Pearsin ohjevalikko tulee näkyviin, ja siinä on luettelo käytettävissä olevista komennoista.


### 4.6. Testaa päärynät Keetillä


Voit tarkistaa, että Pears on täysin toimintakykyinen, käynnistämällä verkossa jo käytettävissä olevan P2P-sovelluksen, kuten Holepunchin avoimen lähdekoodin Keet-viesti- ja videoneuvotteluohjelmiston.


```bash
pear run pear://keet
```


Tämä komento lataa Keet-sovelluksen suoraan Pears-verkosta ilman keskitettyä palvelinta. Jos Keet käynnistyy onnistuneesti, se tarkoittaa, että Pears-asennus on täysin toimiva.


MacOS-järjestelmäsi on nyt valmis ajamaan ja isännöimään vertaisverkkosovelluksia Pearsin avulla.


## 5. Plan ₿ Academyn käyttö päärynöissä


Kun Pears on asennettu ja käynnissä, voit käynnistää suoraan **Plan ₿ Academy** -alustan P2P-verkon kautta. Suorita vain seuraava komento päätelaitteessa (sama komento toimii Linuxissa, Windowsissa ja macOS:ssä):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Kun lataus on valmis, Plan ₿ Academy avautuu Pears-ympäristöön, ja sitä voidaan käyttää aivan kuten alkuperäistä verkkosivustoa - mutta ilman riippuvuutta keskitetystä palvelimesta.


![Image](assets/fr/14.webp)


## 6. Miten kylvösuunnitelma ₿ Akatemia päärynöistä


Pears-verkossa *seed*-sovelluksen jakaminen tarkoittaa sen uudelleenjakamista muille vertaisverkoille omalta koneeltasi. Käytännössä, kun seed Plan ₿ Academy, tietokoneestasi tulee tietolähde, jonka avulla muut käyttäjät voivat ladata sovelluksen ilman, että he ovat riippuvaisia keskitetystä palvelimesta.


Tämä mekanismi vahvistaa sovelluksemme kestävyyttä ja sensuurinsietokykyä Pears-verkossa. 


Voit auttaa Plan ₿ Academyn levittämisessä suorittamalla seuraavan komennon:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Niin kauan kuin tämä komento on aktiivinen, laite osallistuu sovelluksen tiedostojen jakeluun. Jos suljet päätelaitteen, jakoprosessi pysähtyy.


Jos haluat jatkaa kylvämistä uudelleenkäynnistyksen jälkeen, voit suorittaa komennon taustalla tai luoda järjestelmäpalvelun - esimerkiksi systemd-palvelun Linuxissa, LaunchAgent-ohjelman macOS:ssä tai ajastetun tehtävän Windowsissa. Näillä menetelmillä varmistetaan, että Plan ₿ Academy -sovellus jatkaa kylvämistä automaattisesti järjestelmän käynnistyksen yhteydessä.


Kiitos, että osallistut Plan ₿ Academyn hajautettuun jakeluun Päärynöissä ja autat tekemään Bitcoin-koulutuksesta todella sensuurin kestävää!