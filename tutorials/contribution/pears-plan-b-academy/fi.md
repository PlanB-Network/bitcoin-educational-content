---
name: Kartta ₿ Akatemia - Pears App
description: Miten asennan ja käytän Plan ₿ Academy -sovellusta Pearsissä?
---

![cover](assets/cover.webp)



Kuten luultavasti tiedät, Plan ₿ Academy on suurin Bitcoin:lle omistettu koulutustietokanta, johon on koottu kursseja, opetusohjelmia ja tuhansia avoimella lisenssillä julkaistuja resursseja. Alun perin Plan ₿ Academy oli verkkosivusto. Mutta mitä tapahtuisi, jos siihen ei enää pääsisi normaalisti käsiksi, esimerkiksi sensuurin vuoksi?



Tässä opetusohjelmassa opimme, miten **Plan ₿ Academy** -alustaa voidaan käyttää todella mittaamattomalla tavalla **Pearsin**, **Holepunchin** kehittämän ja **Tetherin** tukeman vertaisverkkoteknologian (P2P) ansiosta.



Pears on ohjelmisto, jonka avulla voimme käyttää Plan ₿ Academy -alustaa ilman keskitettyä verkkosivustoa. Tässä opetusohjelmassa asennamme Pearsin tietokoneellesi, jotta voit käyttää Plan ₿ Academya Pearsin kautta.



Pearsin tavoite on yksinkertainen: mahdollistaa verkkosovellusten jakelu ja käyttö ilman keskitettyä infrastruktuuria (ei palvelimia, ei isäntiä, ei välikäsiä). Toisin sanoen, vaikka pilvipalveluntarjoaja sulkeutuisi tai jokin maa estäisi verkkotunnuksen käytön, sovellus jatkaa elämäänsä verkon vertaisverkkojen kesken. Tämän lähestymistavan ansiosta koulutusalustamme Plan ₿ Academy on käytettävissä kaikkialla maailmassa ilman yksittäistä vikapistettä.



---

**TL;DR :**





- Asenna päärynät ;





- Käynnistä Plan ₿ Academy -sovellus seuraavalla komennolla:



```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



---

## 1. Asenna päärynät



### 1.1 Mitä päärynät ovat?



Pears on ajoympäristö, kehitystyökalu ja jakelualusta vertaissovelluksille. Tämä avoimen lähdekoodin työkalu mahdollistaa ohjelmistojen rakentamisen, jakamisen ja suorittamisen ilman palvelinta tai infrastruktuuria suoraan käyttäjien kesken. Konkreettisesti tämä tarkoittaa sitä, että sen sijaan, että sovellus sijaitsisi keskitetysti palvelimella, jokaisesta käyttäjästä tulee verkon solmu, joka jakaa osan sovelluksesta ja dataa muiden vertaisten kanssa. Koko järjestelmä muodostaa hajautetun verkon, jossa kukin instanssi tekee yhteistyötä pitääkseen palvelun saatavilla.



![Image](assets/fr/01.webp)



Tämä lähestymistapa perustuu Holepunchin kehittämiin modulaarisiin ohjelmistokiviin:




- Hypercore**: hajautettu loki, joka takaa tietojen yhdenmukaisuuden ja turvallisuuden ilman keskustietokantaa.
- Hyperbee**: Hypercoren päällä oleva indeksoija, joka mahdollistaa tehokkaan tietojen organisoinnin ja selaamisen.
- Hyperdrive**: hajautettu tiedostojärjestelmä, jota käytetään sovellustiedostojen tallentamiseen ja synkronointiin vertaisverkon välillä.
- Hyperswarm** ja **HyperDHT**: verkkokerrokset, jotka mahdollistavat vertaisverkkojen löytämisen ja yhteydenpidon maailmanlaajuisesti ilman keskuspalvelinta.
- Secretstream**: E2E-salausprotokolla, jolla suojataan kahden vertaisverkon välinen vaihto.



Näitä komponentteja yhdistämällä Pears mahdollistaa itsenäisten, salattujen ja hajautettujen sovellusten luomisen, joissa jokainen käyttäjä osallistuu aktiivisesti verkkoon. Tämä hajautettu arkkitehtuuri poistaa infrastruktuurikustannukset, sensuuririskit ja SPOF:t (*Single Point of Failure*).



Pears on Mathias Buusin ja Paolo Ardoinon (Tetherin toimitusjohtaja ja Bitfinexin teknologiajohtaja) perustaman Holepunchin kehittämä yritys, jonka tehtävänä on laajentaa vertaisvertaislogiikkaa Bitcoin:n ulkopuolelle. Heidän tavoitteenaan on rakentaa "vertaisverkkopohjainen internet", jossa jokainen sovellus voi toimia ilman lupia, palvelimia ja välikäsiä. Holepunch on jo **Keet**:n, täysin P2P-videokonferenssi- ja viestisovelluksen takana.



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Tämä Pearsin asennusopas on jaettu useisiin osiin käyttöjärjestelmästäsi riippuen. Siirry suoraan ympäristöäsi vastaavaan osioon ja noudata asianmukaisia ohjeita :*




- Linux (Debian)** → Osa **1.2.**
- Windows** → Osa **1.3.**
- macOS** → Osa **1.4.**




### 1.2 - Miten asennan Pearsin Linuxiin (Debian)?



Pearsin asentaminen Debian-järjestelmään on suhteellisen suoraviivaista, mutta vaatii muutamia ennakkoedellytyksiä, jotka selitämme yksityiskohtaisesti tässä osiossa.



#### 1.2.1. Järjestelmän päivittäminen



Ensinnäkin on tärkeää varmistaa, että järjestelmäsi on ajan tasalla.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



#### 1.2.2 Riippuvuuksien asentaminen



Pears luottaa useisiin järjestelmäkirjastoihin, kuten `libatomic1`, jota Bare JavaScript -ajoaika käyttää. Asenna se seuraavalla komennolla:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



#### 1.2.3 Node.js:n ja npm:n asentaminen NVM:n kautta



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



#### 1.2.4 Pearsin asentaminen npm:n avulla



Kun *npm* on käytettävissä, voit asentaa Pears CLI:n globaalisti järjestelmääsi. Tällöin voit suorittaa `pear`-komennon mistä tahansa hakemistosta.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



#### 1.2.5. Päärynöiden alustaminen



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



#### 1.2.6. Päärynöiden testaaminen Keetillä



Voit tarkistaa, että Pears on täysin toimintakykyinen, käynnistämällä verkossa jo käytettävissä olevan P2P-sovelluksen, kuten Holepunchin avoimen lähdekoodin Keet-viesti- ja videoneuvotteluohjelmiston.



```bash
pear run pear://keet
```



Tämä komento lataa Keet-sovelluksen suoraan Pears-verkosta ilman keskitetyn palvelimen kautta kulkemista. Jos Keet käynnistyy oikein, Pears-asennuksesi on täysin toimiva.



![Image](assets/fr/12.webp)



Linux-järjestelmäsi on nyt valmis ajamaan ja isännöimään vertaisverkkosovelluksia Pearsin avulla.



### 1.3 - Miten asennan Pearsin Windowsiin?



Pearsin asentaminen Windowsiin on yhtä helppoa kuin Linuxiin, mutta se vaatii muutamia erikoistyökaluja.



*Jos käytät Linuxia ja olet jo asentanut Pearsin, voit siirtyä suoraan vaiheeseen 2



#### 1.3.1. Avaa PowerShell järjestelmänvalvojan tilassa



Suorita PowerShell ensin järjestelmänvalvojan oikeuksin :




- Napsauta Käynnistä-valikkoa;
- Kirjoita PowerShell ;
- Napsauta hiiren kakkospainikkeella "*Windows PowerShell*" ;
- Valitse "*Ajeta järjestelmänvalvojana*".



![Image](assets/fr/15.webp)



#### 1.3.2. Lataa NVS



Pears asennetaan *npm*:n, *Node.js*-paketinhallintaohjelman, kautta. Windowsissa Holepunchin suosittelema menetelmä on käyttää *NVS*:ää (*Node Version Switcher*), joka on vakaampi kuin *NVM* tässä järjestelmässä.



Asenna uusin versio *NVS*:stä PowerShellissä suorittamalla seuraava komento :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



#### 1.3.3. Node.js:n asentaminen



Käynnistä PowerShell uudelleen asennuksen jälkeen ja anna seuraava komento:



```powershell
nvs
```



Näet luettelon saatavilla olevista *Node.js*-versioista. Valitse ensimmäinen painamalla näppäimistön a-näppäintä.



![Image](assets/fr/17.webp)



*Node.js* on asennettu.



![Image](assets/fr/18.webp)



#### 1.3.4. Tarkista asennukset



Varmista, että *Node.js* ja *npm* ovat käytettävissä:



```powershell
node -v
npm -v
```



Molempien komentojen on palautettava versionumero.



![Image](assets/fr/19.webp)



#### 1.3.5. Pearsin asentaminen npm:llä



Kun *Node.js* ja *npm* ovat käytettävissä, asenna **Pears CLI** globaalisti järjestelmääsi:



```powershell
npm install -g pear
```



Tämä asentaa `pear`-binaryn globaaliin *npm*-hakemistoosi.



![Image](assets/fr/20.webp)



#### 1.3.6. Tarkista ja aloita päärynät



Kun asennus on valmis, suorita :



```powershell
pear
```



Ensimmäisellä käynnistyskerralla Pears lataa tarvittavat komponentit automaattisesti vertaisverkosta. Tämä prosessi voi kestää muutaman hetken.



![Image](assets/fr/21.webp)



Jos kaikki on mennyt hyvin, sinun pitäisi nähdä CLI Pears -apuikkuna, jossa on luettelo käytettävissä olevista alakäskyistä (run, seed, info...).



#### 1.3.7. Päärynöiden testaaminen Keetillä



Voit tarkistaa, että Pears on täysin toimintakykyinen, käynnistämällä verkossa jo käytettävissä olevan P2P-sovelluksen, kuten Holepunchin avoimen lähdekoodin Keet-viesti- ja videokonferenssiohjelmiston.



```bash
pear run pear://keet
```



Tämä komento lataa Keet-sovelluksen suoraan Pears-verkosta ilman keskitetyn palvelimen kautta kulkemista. Jos Keet käynnistyy oikein, Pears-asennuksesi on täysin toimiva.



![Image](assets/fr/22.webp)



Windows-järjestelmäsi on nyt valmis ajamaan ja isännöimään vertaisverkkosovelluksia Pearsin avulla.



### 1.4. Kuinka asentaa Pears macOS:lle?



Pearsin asentaminen macOS-käyttöjärjestelmään on samanlaista kuin sen asentaminen Linuxiin, mutta se vaatii muutamia Apple-ympäristöön liittyviä mukautuksia. Tutustutaan näihin vaiheisiin yhdessä.



*Jos käytät Linuxia tai Windowsia ja olet jo asentanut Pearsin, voit siirtyä suoraan vaiheeseen 2



#### 1.4.1. Tarkista järjestelmävaatimukset



Varmista ennen asennusta, että *Xcode Command Line Tools* on järjestelmässäsi. Tämä paketti tarjoaa tarvittavat kääntämistyökalut _Node.js_:lle ja sen riippuvuuksille.



Avaa pääteasema näppäimistön pikanäppäimillä `Cmd + välilyönti`, kirjoita `Terminaali` ja paina `Enter`-näppäintä. Voit sitten syöttää tämän komennon terminaaliin käynnistääksesi asennuksen:



```bash
xcode-select --install
```



Jos työkalut on jo asennettu järjestelmääsi, macOS ilmoittaa sinulle siitä.



#### 1.4.2. NVM:n asentaminen



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



#### 1.4.3 Node.js:n ja npm:n asentaminen



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



#### 1.4.4 Pearsin asentaminen npm:n avulla



Kun *npm* on käytettävissä, voit asentaa Pears CLI:n globaalisti järjestelmääsi. Tällöin voit suorittaa `pear`-komennon mistä tahansa hakemistosta.



```bash
npm install -g pear
```



#### 1.4.5. Päärynöiden alustaminen



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



#### 1.4.6. Päärynöiden testaaminen Keetillä



Voit tarkistaa, että Pears on täysin toimintakykyinen, käynnistämällä verkossa jo käytettävissä olevan P2P-sovelluksen, kuten Holepunchin avoimen lähdekoodin Keet-viesti- ja videoneuvotteluohjelmiston.



```bash
pear run pear://keet
```



Tämä komento lataa Keet-sovelluksen suoraan Pears-verkosta ilman keskitetyn palvelimen kautta kulkemista. Jos Keet käynnistyy oikein, Pears-asennuksesi on täysin toimiva.



MacOS-järjestelmäsi on nyt valmis ajamaan ja isännöimään vertaisverkkosovelluksia Pearsin avulla.



## 2. Miten käytän Plan ₿ Academya päärynöissä?



Kun Pears on asennettu ja käynnissä, voit käyttää **Plan ₿ Academy** -alustaa suoraan P2P-verkon kautta. Suorita vain seuraava komento päätelaitteessa (sama komento Linuxissa, Windowsissa ja macOS:ssä):



```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```



![Image](assets/fr/13.webp)



Kun Plan ₿ Academy on ladattu, se avautuu Pears-ympäristöön, ja sitä voidaan käyttää kuten alkuperäistä verkkosivustoa, mutta ilman riippuvuutta keskitetystä palvelimesta.



![Image](assets/fr/14.webp)