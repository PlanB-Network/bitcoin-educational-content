---
name: Lisäämässä Opetusvälineitä
description: Miten lisätä uusia opetusmateriaaleja PlanB-verkkoon?
---
![tapahtuma](assets/cover.webp)

PlanB:n tehtävänä on tarjota johtavia opetusresursseja Bitcoinista mahdollisimman monella kielellä. Kaikki sivustolla julkaistu sisältö on avoimen lähdekoodin ja isännöity GitHubissa, mikä mahdollistaa kenen tahansa osallistumisen alustan rikastuttamiseen.

Opastusten ja koulutuksen lisäksi PlanB-verkosto tarjoaa myös laajan kirjaston monipuolista opetussisältöä Bitcoinista, joka on kaikkien saatavilla [BET (_Bitcoin Educational Toolkit_) -osiossa](https://planb.network/resources/bet). Tämä tietokanta sisältää opetusjulisteita, meemejä, humoristisia propagandajulisteita, teknisiä kaavioita, logoja ja muita työkaluja käyttäjille. Tämän aloitteen tavoitteena on tukea yksilöitä ja yhteisöjä, jotka opettavat Bitcoinista ympäri maailmaa, tarjoamalla heille tarvittavat visuaaliset resurssit.

Haluatko osallistua tämän tietokannan rikastuttamiseen, mutta et tiedä miten? Tämä opas on sinua varten!

*On ehdottoman tärkeää, että sivustoon integroitu sisältö on oikeuksista vapaa tai kunnioittaa lähdetiedoston lisenssiä. Lisäksi kaikki PlanB-verkostossa julkaistut visuaalit ovat saatavilla [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) -lisenssin alaisina.*
![tapahtuma](assets/01.webp)
- Ensimmäiseksi sinun on oltava tili GitHubissa. Jos et tiedä, miten tili luodaan, olemme tehneet yksityiskohtaisen oppaan, joka opastaa sinua.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Mene [PlanB:n GitHub-repositorioon, joka on omistettu datalle](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet) `resources/bet/` -osiossa:
![tapahtuma](assets/02.webp)
- Klikkaa oikeassa yläkulmassa `Add file` -painiketta, sitten `Create new file`:
![tapahtuma](assets/03.webp)
- Jos et ole aiemmin osallistunut PlanB-verkon sisältöön, sinun on luotava oma haarasi alkuperäisestä repositoriosta. Repositorion haarauttaminen tarkoittaa sen kopion luomista omalle GitHub-tilillesi, mikä mahdollistaa projektissa työskentelyn vaikuttamatta alkuperäiseen repositorioon. Klikkaa `Fork this repository` -painiketta:
![tapahtuma](assets/04.webp)
- Tämän jälkeen päädyt GitHubin muokkaussivulle:
![tapahtuma](assets/05.webp)
- Luo kansio sisällöllesi. Tee tämä kirjoittamalla `Name your file...` -kenttään sisältösi nimi pienillä kirjaimilla ja välilyönneillä sijasta käytä viivoja. Esimerkissäni, sanotaan että haluan lisätä PDF-visuaalin 2048 sanan BIP39-listasta. Joten, kutsun kansioni `bip39-wordlist`: ![tapahtuma](assets/06.webp)
- Vahvistaaksesi kansion luomisen, lisää vain kauttaviiva nimen perään samassa kentässä, esimerkiksi: `bip39-wordlist/`. Kauttaviivan lisääminen luo automaattisesti kansion tiedoston sijaan:
![tapahtuma](assets/07.webp)
- Tässä kansiossa luot ensimmäisen YAML-tiedoston nimeltä `bet.yml`:
![tapahtuma](assets/08.webp)
- Täytä tämä tiedosto sisältösi tiedoilla käyttäen tätä mallia:

```yaml
builder: 
type: 
links:
  download: 
  view: 
    - en: 
tags:
  - 
  - 
contributors:
  - 
```

Tässä ovat tiedot, jotka sinun tulee täyttää kullekin kentälle:
- **`builder`**: Ilmoita organisaatiosi tunniste PlanB-verkostossa. Jos sinulla ei vielä ole "builder"-tunnistetta yrityksellesi, voit luoda sellaisen seuraamalla tätä opasta.

https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

 Jos sinulla ei ole tunnistetta, voit yksinkertaisesti käyttää nimeäsi, nimimerkkiäsi tai yrityksesi nimeä ilman, että olet luonut builder-profiilia.
- **`type`**: Valitse sisältösi luonne seuraavista kahdesta vaihtoehdosta:
	- `Educational Content` opetussisällölle.
	- `Visual Content` muun tyyppisille moninaisille sisällöille.

- **`links`**: Tarjoa linkit sisältöösi. Sinulla on kaksi vaihtoehtoa:
	- Jos päätät isännöidä sisältöäsi suoraan PlanB:n GitHubissa, sinun tulee lisätä linkit tähän tiedostoon seuraavissa vaiheissa.
	- Jos sisältösi on isännöity muualla, kuten henkilökohtaisella verkkosivustollasi, ilmoita vastaavat linkit tässä:
	    - `download`: Linkki sisältösi lataamiseen.
	    - `view`: Linkki sisältösi katseluun (voi olla sama kuin latauslinkki). Jos sisältösi on saatavilla useilla kielillä, lisää linkki kullekin kielelle.

- **`tags`**: Lisää kaksi sisältöösi liittyvää tagia. Esimerkkejä:
	- bitcoin
	- teknologia
	- talous
	- koulutus
	- meemi...

- **`contributors`**: Mainitse avustajatunnisteesi, jos sinulla on sellainen.

Esimerkiksi YAML-tiedostosi voisi näyttää tältä:

```yaml
builder: PlanB-Network
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
- Esimerkissäni jätän linkit toistaiseksi tyhjiksi, sillä lisään PDF:ni suoraan GitHubiin:
![event](assets/09.webp)
- Kun olet saanut tiedoston muokkaukset valmiiksi, tallenna ne napsauttamalla `Commit changes...` -painiketta:
![event](assets/10.webp)
- Lisää otsikko muutoksillesi sekä lyhyt description:
![event](assets/11.webp)
- Napsauta vihreää `Propose changes` -painiketta:
![event](assets/12.webp)
- Tämän jälkeen päädyt sivulle, joka tiivistää kaikki muutoksesi:
![event](assets/13.webp)
- Napsauta GitHub-profiilikuvakettasi oikeassa yläkulmassa, sitten `Your Repositories`:
![event](assets/14.webp)
- Valitse PlanB Network -repositoriosi haarasi:
![event](assets/15.webp)
- Sinun pitäisi nähdä ilmoitus ikkunan yläosassa uudesta haarastasi. Sen nimi on todennäköisesti `patch-1`. Napsauta sitä:
![event](assets/16.webp)
- Olet nyt työhaarassasi (**varmista, että olet samassa haarassa kuin aiemmat muutoksesi, tämä on tärkeää!**):
![event](assets/17.webp)
- Palaa takaisin `resources/bet/`-kansioon ja valitse sisältökansiosi, jonka loit edellisessä commitissa:
![event](assets/18.webp)
- Sisältökansiossasi, napsauta `Add file` -painiketta, sitten `Create new file`:
![event](assets/19.webp)
- Nimeä tämä uusi kansio `assets` ja vahvista sen luominen laittamalla kauttaviiva `/` loppuun:
![event](assets/20.webp)
- Tässä `assets`-kansiossa, luo tiedosto nimeltä `.gitkeep`: ![event](assets/21.webp)
- Klikkaa `Commit changes...` -painiketta: ![event](assets/22.webp)- Jätä commit-otsikko oletusarvoiseksi ja varmista, että `Commit directly to the patch-1 branch` -ruutu on valittuna, sitten klikkaa `Commit changes`: ![event](assets/23.webp)
- Palaa `assets`-kansioon: ![event](assets/24.webp)
- Klikkaa `Add file` -painiketta, sitten `Upload files`: ![event](assets/25.webp)
- Uusi sivu avautuu. Vedä ja pudota pikkukuva, joka edustaa sisältöäsi, alueelle. Tämä kuva näytetään PlanB Network -sivustolla: ![event](assets/26.webp)
- Se voi olla esikatselu, logo tai ikoni: ![event](assets/27.webp)
- Kun kuva on ladattu, varmista, että `Commit directly to the patch-1 branch` -ruutu on valittuna, sitten klikkaa `Commit changes`: ![event](assets/28.webp)
- Ole varovainen, kuvan nimen tulee olla `logo` ja sen tulee olla `.webp`-muodossa. Täydellinen tiedostonimi tulee siis olla: `logo.webp`: ![event](assets/29.webp)
- Palaa `assets`-kansioosi ja klikkaa välitiedostoa `.gitkeep`: ![event](assets/30.webp)
- Kun olet tiedostossa, klikkaa kolmea pientä pistettä oikeassa yläkulmassa ja sitten `Delete file`: ![event](assets/31.webp)
- Varmista, että olet edelleen samalla työhaaraalla, sitten klikkaa `Commit changes` -painiketta: ![event](assets/32.webp)
- Lisää otsikko ja kuvaus commitillesi, sitten klikkaa `Commit changes`: ![event](assets/33.webp)
- Palaa sisältökansioosi: ![event](assets/34.webp)
- Klikkaa `Add file` -painiketta, sitten `Create new file`: ![event](assets/35.webp)
- Luo uusi YAML-tiedosto nimittämällä se äidinkielesi indikaattorilla. Tätä tiedostoa käytetään sisällön kuvaukseen. Esimerkiksi, jos haluan kirjoittaa kuvaukseni englanniksi, nimeän tämän tiedoston `en.yml`: ![event](assets/36.webp)
- Täytä tämä YAML-tiedosto käyttäen tätä mallia:

```yaml
name: 
description: |
  
```

- `name`-avaimelle voit lisätä sisältösi nimen;
- `description`-avaimelle sinun tarvitsee vain lisätä lyhyt kappale, joka kuvailee sisältöäsi. Kuvaus tulee olla samalla kielellä kuin tiedostonimi. Sinun ei tarvitse kääntää tätä kuvausta kaikille sivuston tuetulle kielille, sillä PlanB-tiimit tekevät sen mallinsa avulla.
Esimerkiksi, tässä on miltä tiedostosi voisi näyttää:

```yaml
name: BIP39 WORDLIST
description: |
  Täydellinen ja numeroitu lista 2048 englanninkielisestä sanasta BIP39-sanakirjasta, jota käytetään muistilauseiden koodaamiseen. Asiakirja voidaan tulostaa yhdelle sivulle.
```

![event](assets/37.webp)
- Klikkaa `Commit changes...` -painiketta:
![event](assets/38.webp)
- Varmista, että `Commit directly to the patch-1 branch` -ruutu on valittuna, lisää otsikko, sitten klikkaa `Commit changes`:
![event](assets/39.webp)
- Sisältökansiosi pitäisi nyt näyttää tältä:
![event](assets/40.webp)
*Jos et halua lisätä sisältöä GitHubiin ja olet jo merkinnyt linkit `bet.yml`-tiedostoon aiemmissa vaiheissa, voit jättää tämän osion väliin ja siirtyä suoraan osioon, joka käsittelee vetopyynnön luomista.*
- Palaa `/assets`-kansioon:
![tapahtuma](assets/41.webp)
- Napsauta `Add file` -painiketta, sitten `Upload files`:
![tapahtuma](assets/42.webp)
- Uusi sivu avautuu. Vedä ja pudota alueelle sisältö, jonka haluat jakaa:
![tapahtuma](assets/43.webp)
- Esimerkiksi lisäsin PDF-tiedoston BIP39-listasta:
![tapahtuma](assets/44.webp)
- Kun sisältö on ladattu, varmista, että `Commit directly to the patch-1 branch` -ruutu on valittu, sitten napsauta `Commit changes`:
![tapahtuma](assets/45.webp)
- Palaa `/assets`-kansioosi ja napsauta juuri lataamaasi tiedostoa:
![tapahtuma](assets/46.webp)
- Hae tiedostosi väliaikainen URL. Esimerkiksi minun tapauksessani URL on:

```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Säilytä URL:sta vain viimeinen osa alkaen `/resources`:

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Lisää URL:n perään seuraavat tiedot saadaksesi oikean linkin:

```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

Mitä tässä teemme, on tulevan tiedostosi linkin ennakoiminen, kun ehdotuksesi on yhdistetty PlanB Networkin lähdevarastoon.
- Palaa `bet.yml`-tiedostoosi ja napsauta kynäkuvaketta: ![tapahtuma](assets/47.webp)
- Lisää linkkisi sinne:
![tapahtuma](assets/48.webp)
- Kun muutoksesi ovat valmiit, napsauta `Commit changes...` -painiketta:
![tapahtuma](assets/49.webp)
- Lisää muutoksillesi otsikko sekä lyhyt description:
![tapahtuma](assets/50.webp)
- Napsauta vihreää `Commit changes` -painiketta:
![tapahtuma](assets/51.webp)

---

- Jos kaikki näyttää hyvältä, palaa haarasi juureen:
![tapahtuma](assets/52.webp)
- Sinun pitäisi nähdä viesti, joka ilmoittaa haarasi muuttuneen. Napsauta `Compare & pull request` -painiketta:
![tapahtuma](assets/53.webp)
- Lisää selkeä otsikko ja kuvaus PR:lle:
![tapahtuma](assets/54.webp)
- Napsauta `Create pull request` -painiketta:
![tapahtuma](assets/55.webp)
Onnittelut! PR:si on luotu onnistuneesti. Ylläpitäjä tarkistaa sen nyt ja jos kaikki on kunnossa, yhdistää sen PlanB Networkin päävarastoon. BETisi pitäisi näkyä verkkosivustolla muutaman päivän kuluttua.

Muista seurata PR:si etenemistä. Ylläpitäjä saattaa jättää kommentin pyytäen lisätietoja. Niin kauan kuin PR:si ei ole vahvistettu, voit tarkastella sitä PlanB Networkin GitHub-repositorion Pull requests -välilehdessä:
![tapahtuma](assets/56.webp)
Suurkiitokset arvokkaasta panoksestasi! :)
