---
name: Pears
description: Miten asennan ja käytän Pearsin sovelluksia?
---

![cover](assets/cover.webp)



Tässä opetusohjelmassa opettelemme, miten sovelluksia ajetaan **Pearsissa**, joka on **Holepunchin** kehittämä ja **Tetherin** tukema vertaisverkkoteknologia (P2P). Tavoite on yksinkertainen: mahdollistaa verkkosovellusten jakelu ja käyttö ilman keskitettyä infrastruktuuria (ei palvelimia, ei isäntiä, ei välikäsiä). Toisin sanoen, vaikka pilvipalveluntarjoaja sulkeutuisi tai jokin maa estäisi verkkotunnuksen käytön, sovellus jatkaa elämäänsä verkon vertaisverkkojen kesken.



## 1. Mitä päärynät ovat?



Pears on ajoympäristö, kehitystyökalu ja jakelualusta vertaissovelluksille. Tämä avoimen lähdekoodin työkalu mahdollistaa ohjelmistojen rakentamisen, jakamisen ja suorittamisen ilman palvelinta tai infrastruktuuria suoraan käyttäjien kesken. Konkreettisesti tämä tarkoittaa sitä, että sen sijaan, että sovellus sijaitsisi keskitetysti palvelimella, jokaisesta käyttäjästä tulee verkon solmu, joka jakaa osan sovelluksesta ja dataa muiden vertaisten kanssa. Koko järjestelmä muodostaa hajautetun verkon, jossa kukin instanssi tekee yhteistyötä pitääkseen palvelun saatavilla.



![Image](assets/fr/01.webp)



Tämä lähestymistapa perustuu Holepunchin kehittämiin modulaarisiin ohjelmistokiviin:




- Hypercore**: hajautettu loki, joka takaa tietojen yhdenmukaisuuden ja turvallisuuden ilman keskustietokantaa.
- Hyperbee**: Hypercoren päällä oleva indeksoija, joka mahdollistaa tehokkaan tietojen organisoinnin ja selaamisen.
- Hyperdrive**: hajautettu tiedostojärjestelmä, jota käytetään sovellustiedostojen tallentamiseen ja synkronointiin vertaisverkon välillä.
- Hyperswarm** ja **HyperDHT**: verkkokerrokset, jotka mahdollistavat vertaisverkkojen löytämisen ja yhteydenpidon maailmanlaajuisesti ilman keskuspalvelinta.
- Secretstream**: E2E-salausprotokolla, jolla suojataan kahden vertaisverkon välinen vaihto.



Näitä komponentteja yhdistämällä Pears mahdollistaa itsenäisten, salattujen ja hajautettujen sovellusten luomisen, joissa jokainen käyttäjä osallistuu aktiivisesti verkkoon. Tämä hajautettu arkkitehtuuri poistaa infrastruktuurikustannukset, sensuuririskit ja SPOF:t (*Single Point of Failure*).



## 2. Hankkeen alkuperä ja filosofia



Pears on Mathias Buusin ja Paolo Ardoinon (Tetherin toimitusjohtaja ja Bitfinexin teknologiajohtaja) perustaman Holepunchin kehittämä yritys, jonka tehtävänä on laajentaa vertaisvertaislogiikkaa Bitcoin:n ulkopuolelle. Heidän tavoitteenaan on rakentaa "vertaisverkkopohjainen internet", jossa jokainen sovellus voi toimia ilman lupia, palvelimia ja välikäsiä. Holepunch on jo **Keet**:n, täysin P2P:n videoneuvottelu- ja viestisovelluksen takana.



*Tämä Pearsin asennusopas on jaettu useisiin osiin käyttöjärjestelmästäsi riippuen. Siirry suoraan ympäristöäsi vastaavaan osioon ja noudata asianmukaisia ohjeita :*




- Linux (Debian)** → Osa **3**
- Ikkunat** → Osa **4**
- macOS** → Osa **5**



## 3. Kuinka asentaa Pears Linuxiin (Debian)



Pearsin asentaminen Debian-järjestelmään on suhteellisen suoraviivaista, mutta se vaatii muutamia ennakkoedellytyksiä, joista kerromme tarkemmin tässä osiossa.



### 3.1. päivitä järjestelmä



Ensinnäkin on tärkeää varmistaa, että järjestelmäsi on ajan tasalla.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. asenna riippuvuudet



Pears luottaa tiettyihin järjestelmäkirjastoihin, erityisesti `libatomic1`, jota Bare JavaScript -ajoaika käyttää. Asenna se seuraavalla komennolla:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. asenna Node.js ja npm NVM:n kautta



Pears jaetaan *npm*:n, *Node.js*-paketinhallintaohjelman, kautta. Vaikka Pears ei ole suoraan riippuvainen *Node.js*:stä toimiakseen, sitä tarvitaan asennuksessa. Suositeltava tapa asentaa *Node.js* Linuxiin on *NVM* (*Node Version Manager*), jonka avulla voit hallita useita Node-versioita rinnakkain.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Lataa sitten pääte uudelleen aktivoidaksesi *NVM* :



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Tarkista, että *NVM* on asennettu:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Asenna sitten vakaa versio *Node.js:stä* (esim. nykyinen LTS):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Tarkista *Node.js*- ja *npm*-asennukset:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



### 3.4 Pearsin asentaminen npm:n avulla



Kun *npm* on käytettävissä, voit asentaa Pears CLI:n globaalisti järjestelmääsi. Tällöin voit ajaa `pear`-komennon mistä tahansa hakemistosta.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5. Päärynöiden alustaminen



Asennuksen jälkeen suorita terminaalissa seuraava komento:



```bash
pear
```



Ensimmäisen käynnistyksen yhteydessä Pears muodostaa yhteyden vertaisverkkoon ladatakseen tarvittavat komponentit. 



![Image](assets/fr/10.webp)



Kun lataus on valmis, suorita komento uudelleen tarkistaaksesi, että kaikki toimii:



```bash
pear
```



![Image](assets/fr/11.webp)



Jos kaikki on asennettu oikein, Pearsin ohje näyttää luettelon käytettävissä olevista komennoista.



### 3.6. Päärynöiden testaaminen Keetillä



Voit tarkistaa, että Pears on täysin toimintakunnossa, käynnistämällä verkossa jo käytettävissä olevan P2P-sovelluksen, kuten Holepunchin avoimen lähdekoodin Keet-viesti- ja videoneuvotteluohjelmiston.



```bash
pear run pear://keet
```



Tämä komento lataa Keet-sovelluksen suoraan Pears-verkosta ilman keskitetyn palvelimen kautta kulkemista. Jos Keet käynnistyy oikein, Pears-asennuksesi on täysin toimiva.



![Image](assets/fr/12.webp)



Linux-järjestelmäsi on nyt valmis ajamaan ja isännöimään vertaisverkkosovelluksia Pearsin avulla.



## 4. Kuinka asentaa Pears Windowsissa



Pearsin asentaminen Windowsiin on yhtä helppoa kuin Linuxiin, mutta se vaatii muutamia erikoistyökaluja.



*Jos käytät Linuxia, voit siirtyä vaiheeseen 6.*



### 4.1. avaa PowerShell järjestelmänvalvojan tilassa



Suorita PowerShell ensin järjestelmänvalvojan oikeuksin :




- Napsauta Käynnistä-valikkoa;
- Kirjoita PowerShell ;
- Napsauta hiiren kakkospainikkeella "*Windows PowerShell*" ;
- Valitse "*Ajeta järjestelmänvalvojana*".



![Image](assets/fr/15.webp)



### 4.2. lataa NVS



Pears asennetaan *npm*:n, *Node.js*-paketinhallintaohjelman, kautta. Windowsissa Holepunchin suosittelema menetelmä on käyttää *NVS*:ää (*Node Version Switcher*), joka on vakaampi kuin *NVM* tässä järjestelmässä.



Asenna uusin versio *NVS*:stä PowerShellissä suorittamalla seuraava komento :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. asenna Node.js



Käynnistä PowerShell uudelleen asennuksen jälkeen ja anna seuraava komento:



```powershell
nvs
```



Näet luettelon saatavilla olevista *Node.js*-versioista. Valitse ensimmäinen painamalla näppäimistön a-näppäintä.



![Image](assets/fr/17.webp)



*Node.js* on asennettu.



![Image](assets/fr/18.webp)



### 4.4. Tarkista asennukset



Varmista, että *Node.js* ja *npm* ovat käytettävissä:



```powershell
node -v
npm -v
```



Molempien komentojen on palautettava versionumero.



![Image](assets/fr/19.webp)



### 4.5. Pearsin asentaminen npm:n avulla



Kun *Node.js* ja *npm* ovat käytettävissä, asenna **Pears CLI** globaalisti järjestelmääsi:



```powershell
npm install -g pear
```



Tämä asentaa `pear`-binaryn globaaliin *npm*-hakemistoosi.



![Image](assets/fr/20.webp)



### 4.6. Tarkista ja aloita päärynät



Kun asennus on valmis, suorita :



```powershell
pear
```



Ensimmäisellä käynnistyskerralla Pears lataa tarvittavat komponentit automaattisesti vertaisverkosta. Tämä prosessi voi kestää muutaman hetken.



![Image](assets/fr/21.webp)



Jos kaikki on mennyt hyvin, sinun pitäisi nähdä CLI Pears -apuikkuna, jossa on luettelo käytettävissä olevista alakäskyistä (run, seed, info...).



### 4.7. Päärynöiden testaaminen Keetillä



Voit tarkistaa, että Pears on täysin toimintakykyinen, käynnistämällä verkossa jo käytettävissä olevan P2P-sovelluksen, kuten Holepunchin avoimen lähdekoodin Keet-viesti- ja videokonferenssiohjelmiston.



```bash
pear run pear://keet
```



Tämä komento lataa Keet-sovelluksen suoraan Pears-verkosta ilman keskitetyn palvelimen kautta kulkemista. Jos Keet käynnistyy oikein, Pears-asennuksesi on täysin toimiva.



![Image](assets/fr/22.webp)



Windows-järjestelmäsi on nyt valmis ajamaan ja isännöimään vertaisverkkosovelluksia Pearsin avulla.



## 5. Miten asennan Pearsin macOS-käyttöjärjestelmään?



Pearsin asentaminen macOS-käyttöjärjestelmään on samanlaista kuin sen asentaminen Linuxiin, mutta se vaatii muutamia Apple-ympäristöön liittyviä mukautuksia. Tutustutaan näihin vaiheisiin yhdessä.



*Jos käytät Linuxia tai Windowsia ja olet jo asentanut Pearsin, voit siirtyä suoraan **vaiheeseen 6**. *



### 5.1. Tarkista järjestelmävaatimukset



Varmista ennen asennusta, että *Xcode Command Line Tools* on järjestelmässäsi. Tämä paketti tarjoaa tarvittavat kääntämistyökalut _Node.js_:lle ja sen riippuvuuksille.



Avaa pääteasema näppäimistön pikanäppäimillä `Cmd + välilyönti`, kirjoita `Terminaali` ja paina `Enter`-näppäintä. Voit sitten syöttää tämän komennon terminaaliin käynnistääksesi asennuksen:



```bash
xcode-select --install
```



Jos työkalut on jo asennettu järjestelmääsi, macOS ilmoittaa sinulle siitä.



### 5.2. asenna NVM



Pears jaetaan *npm*:n, *Node.js*-paketinhallintaohjelman, kautta. Vaikka Pears ei ole suoraan riippuvainen *Node.js*:stä toimiakseen, sitä tarvitaan asennuksessa. Suositeltava tapa asentaa *Node.js* macOS:lle on *NVM* (*Node Version Manager*), jonka avulla voit hallita useita Node-versioita rinnakkain.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Lataa sitten pääte uudelleen aktivoidaksesi *NVM* :



```bash
source ~/.zshrc
```



Jos käytät *bash*:ia *zsh*:n sijasta, suorita :



```bash
source ~/.bashrc
```



Tarkista sitten, että *NVM* on asennettu:



```bash
nvm --version
```



Terminaalin pitäisi palauttaa järjestelmään asennetun *NVM*-version.



### 5.3. asenna Node.js ja npm



Asenna sitten vakaa versio *Node.js:stä* (esim. nykyinen LTS):



```bash
nvm install --lts
```



Kun asennus on valmis, tarkista asennetut versiot:



```bash
node -v
npm -v
```



Molempien komentojen on palautettava versionumero.



### 5.4 Pearsin asentaminen npm:n avulla



Kun *npm* on käytettävissä, voit asentaa Pears CLI:n globaalisti järjestelmääsi. Tällöin voit ajaa `pear`-komennon mistä tahansa hakemistosta.



```bash
npm install -g pear
```



### 5.5. Päärynöiden alustaminen



Asennuksen jälkeen suorita terminaalissa seuraava komento:



```bash
pear
```



Ensimmäisen käynnistyksen yhteydessä Pears muodostaa yhteyden vertaisverkkoon ladatakseen tarvittavat komponentit. 



Kun lataus on valmis, suorita komento uudelleen tarkistaaksesi, että kaikki toimii:



```bash
pear
```



Jos kaikki on asennettu oikein, Pearsin ohje näyttää luettelon käytettävissä olevista komennoista.



### 5.6. Päärynöiden testaaminen Keetillä



Voit tarkistaa, että Pears on täysin toimintakunnossa, käynnistämällä verkossa jo käytettävissä olevan P2P-sovelluksen, kuten Holepunchin avoimen lähdekoodin Keet-viesti- ja videoneuvotteluohjelmiston.



```bash
pear run pear://keet
```



Tämä komento lataa Keet-sovelluksen suoraan Pears-verkosta ilman keskitetyn palvelimen kautta kulkemista. Jos Keet käynnistyy oikein, Pears-asennuksesi on täysin toimiva.



MacOS-järjestelmäsi on nyt valmis ajamaan ja isännöimään vertaisverkkosovelluksia Pearsin avulla.



## 6. Miten käytän sovellusta päärynöissä?



Kun Pears on käytössä, voit ajaa haluamasi sovelluksen suoraan seuraavalla komennolla:



```bash
pear run pear://[KEY]
```



Korvaa `[KEY]` yksinkertaisesti haluamallasi sovellusavaimella.



![Image](assets/fr/13.webp)



Jos haluat oppia, miten Plan ₿ Academy -alustaa käytetään Pearsissä, tutustu tähän kattavaan oppaaseen:



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

Ja jos haluat tietää, miten käyttää juuri käynnistämääsi Keet-viestisovellusta Pearsissä, tutustu tähän ohjeeseen :



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b