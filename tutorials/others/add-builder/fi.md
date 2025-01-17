---
name: Lisäämässä Rakentajaa
description: Kuinka ehdottaa uuden rakentajan lisäämistä PlanB-verkkoon?
---
![builder](assets/cover.webp)

PlanB:n tehtävänä on tarjota huipputason koulutusresursseja Bitcoinista mahdollisimman monella kielellä. Kaikki sivustolla julkaistu sisältö on avoimen lähdekoodin ja isännöity GitHubissa, mikä mahdollistaa kenen tahansa osallistumisen alustan rikastuttamiseen.

Haluatko lisätä uuden Bitcoin "rakentajan" PlanB-verkon sivustolle ja antaa näkyvyyttä yrityksellesi tai ohjelmistollesi, mutta et tiedä miten? Tämä opas on sinua varten!
![builder](assets/01.webp)
- Ensimmäiseksi sinulla täytyy olla GitHub-tili. Jos et tiedä, miten tili luodaan, olemme tehneet yksityiskohtaisen oppaan, joka opastaa sinua.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Mene [PlanB:n GitHub-repositorioon, joka on omistettu datalle](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/builders) `resources/builder/` osiossa:
![builder](assets/02.webp)
- Klikkaa oikeassa yläkulmassa `Add file` -nappia, sitten `Create new file`:
![builder](assets/03.webp)
- Jos et ole aiemmin osallistunut PlanB-verkon sisältöön, sinun täytyy luoda oma haarasi alkuperäisestä repositoriosta. Repositorion haarauttaminen tarkoittaa sen kopion luomista omalle GitHub-tilillesi, mikä mahdollistaa projektissa työskentelyn alkuperäistä repositoriota muuttamatta. Klikkaa `Fork this repository` -nappia:
![builder](assets/04.webp)
- Tämän jälkeen saavut GitHubin muokkaussivulle:
![builder](assets/05.webp)
- Luo kansio yrityksellesi. Tee tämä kirjoittamalla `Name your file...` -kenttään yrityksesi nimi pienillä kirjaimilla ja väliviivat välilyöntien sijaan. Esimerkiksi, jos yrityksesi on nimeltään "Bitcoin Baguette", sinun tulisi kirjoittaa `bitcoin-baguette`:
![builder](assets/06.webp)
- Kansion luomisen vahvistamiseksi lisää vain kauttaviiva nimesi perään samassa kentässä, esimerkiksi: `bitcoin-baguette/`. Kauttaviivan lisääminen luo automaattisesti kansion tiedoston sijaan:
![builder](assets/07.webp)
- Tässä kansiossa luot ensimmäisen YAML-tiedoston nimeltä `builder.yml`:
![builder](assets/08.webp)
- Täytä tämä tiedosto yrityksesi tiedoilla käyttäen tätä mallia:

```yaml
name:

address_line_1:
address_line_2:
address_line_3: 

language:
  - 

links:
  website:
  twitter:
  Github:
  youtube:
  nostr:

tags:
  - 
  - 

category:
```

Tässä mitä kullekin avaimelle tulee täyttää:
- `name`: Yrityksesi nimi (pakollinen);
- `address` : Yrityksesi sijainti (valinnainen);
- `language` : Maat, joissa yrityksesi toimii tai kielet, joita tuetaan (valinnainen);
- `links` : Yrityksesi erilaiset viralliset linkit (valinnainen);
- `tags` : 2 termiä, jotka kuvaavat yritystäsi (pakollinen);
- `category` : Kategoria, joka parhaiten kuvaa alaa, jolla yrityksesi toimii seuraavien vaihtoehtojen joukosta:
	- `wallet`,
	- `infrastructure`,
	- `exchange`,
	- `education`,
	- `service`,
	- `communities`,
	- `conference`,
	- `privacy`,
	- `investment`,
	- `node`,
	- `mining`,
	- `news`,
	- `manufacturer`.
Esimerkiksi YAML-tiedostosi voisi näyttää tältä:
```yaml
name: Bitcoin Baguette

osoite_rivi_1: Pariisi, Ranska
osoite_rivi_2:
osoite_rivi_3:

kieli:
  - fr
  - en

linkit:
  verkkosivusto: https://bitcoin-baguette.com
  twitter: https://twitter.com/bitcoinbaguette
  Github:
  youtube:
  nostr:

tagit:
  - bitcoin
  - koulutus

kategoria: koulutus
```

![rakentaja](assets/09.webp)
- Kun olet saanut muutokset valmiiksi tähän tiedostoon, tallenna ne napsauttamalla `Commit changes...` -painiketta:
![rakentaja](assets/10.webp)
- Lisää muutoksillesi otsikko sekä lyhyt description:
![rakentaja](assets/11.webp)
- Napsauta vihreää `Propose changes` -painiketta:
![rakentaja](assets/12.webp)
- Tämän jälkeen päädyt sivulle, joka tiivistää kaikki tekemäsi muutokset:
![rakentaja](assets/13.webp)
- Napsauta GitHub-profiilikuvakettasi oikeassa yläkulmassa, sitten `Your Repositories`:
![rakentaja](assets/14.webp)
- Valitse PlanB Network -repositoriosi haara:
![rakentaja](assets/15.webp)
- Sinun pitäisi nähdä ilmoitus ikkunan yläosassa uudesta haarastasi. Sen nimi on todennäköisesti `patch-1`. Napsauta sitä:
![rakentaja](assets/16.webp)
- Olet nyt työhaarassasi (**varmista, että olet samalla haaralla kuin aiemmat muutoksesi, tämä on tärkeää!**):
![rakentaja](assets/17.webp)
- Palaa takaisin `resources/builders/`-kansioon ja valitse yrityksesi kansio, jonka loit edellisessä commitissa:
![rakentaja](assets/18.webp)
- Yrityksesi kansiosta, napsauta `Add file` -painiketta, sitten `Create new file`:
![rakentaja](assets/19.webp)
- Nimeä tämä uusi kansio `assets` ja vahvista sen luominen laittamalla kauttaviiva `/` loppuun:
![rakentaja](assets/20.webp)
- Tässä `assets`-kansiossa, luo tiedosto nimeltä `.gitkeep`:
![rakentaja](assets/21.webp)
- Napsauta `Commit changes...` -painiketta:
![rakentaja](assets/22.webp)
- Jätä commit-otsikko oletusarvoiseksi ja varmista, että `Commit directly to the patch-1 branch` -ruutu on valittuna, sitten napsauta `Commit changes`:
![rakentaja](assets/23.webp)
- Palaa takaisin `assets`-kansioon:
![rakentaja](assets/24.webp)
- Napsauta `Add file` -painiketta, sitten `Upload files`:
![rakentaja](assets/25.webp)
- Uusi sivu avautuu. Vedä ja pudota yrityksesi tai ohjelmistosi kuva alueelle. Tämä kuva näytetään PlanB Network -sivustolla:
![rakentaja](assets/26.webp)
- Se voi olla logo tai ikoni:
![rakentaja](assets/27.webp)
- Kun kuva on ladattu, varmista, että `Commit directly to the patch-1 branch` -ruutu on valittuna, sitten napsauta `Commit changes`:
![rakentaja](assets/28.webp)
- Ole varovainen, kuvan tulee olla neliön muotoinen, sen tulee olla nimetty `logo`, ja sen tulee olla `.webp`-muodossa. Täydellinen tiedostonimi olisi siis: `logo.webp`:
![rakentaja](assets/29.webp)
- Palaa takaisin `assets`-kansioosi ja napsauta `.gitkeep`-väliketiedostoa:
![builder](assets/30.webp)- Kun olet tiedostossa, klikkaa oikeassa yläkulmassa olevia kolmea pientä pistettä ja sen jälkeen `Delete file`:
![builder](assets/31.webp)
- Varmista, että olet edelleen samalla työhaaralla, ja klikkaa sitten `Commit changes` -nappia:
![builder](assets/32.webp)
- Lisää otsikko ja kuvaus commitillesi, ja klikkaa sitten `Commit changes`:
![builder](assets/33.webp)
- Palaa takaisin yrityksesi kansioon:
![builder](assets/34.webp)
- Klikkaa `Add file` -nappia, ja sen jälkeen `Create new file`:
![builder](assets/35.webp)
- Luo uusi YAML-tiedosto nimetäksesi sen äidinkielesi indikaattorilla. Tätä tiedostoa käytetään rakentajan kuvaukseen. Esimerkiksi, jos haluan kirjoittaa kuvaukseni englanniksi, nimenän tämän tiedoston `en.yml`:
![builder](assets/36.webp)
- Täytä tämä YAML-tiedosto käyttäen tätä mallia:
```yaml
description: |
 
contributors:
 - 
```

- `contributors`-avaimen kohdalla voit lisätä PlanB-verkoston avustajatunnuksesi, jos sinulla on sellainen. Jos ei, jätä tämä kenttä tyhjäksi.
- `description`-avaimen kohdalla sinun tarvitsee vain lisätä lyhyt kappale, joka kuvailee yritystäsi tai ohjelmistoasi. Kuvaus tulee olla samalla kielellä kuin tiedostonimi. Sinun ei tarvitse kääntää tätä kuvausta kaikille sivuston tukemille kielille, sillä PlanB-tiimit tekevät sen käyttäen omaa malliaan. Esimerkiksi, tässä on miltä tiedostosi voisi näyttää:
```yaml
description: |
Perustettu vuonna 2017, Bitcoin Baguette on Pariisissa toimiva yhdistys, joka on omistautunut järjestämään Bitcoin-tapaamisia ja teknisiä työpajoja. Tuomme yhteen innostuneita, asiantuntijoita ja uteliaita mieliä tutkimaan ja keskustelemaan Bitcoin-teknologian monimutkaisuuksista. Tapahtumamme tarjoavat alustan tiedon jakamiselle, verkostoitumiselle ja syvemmän ymmärryksen saavuttamiselle Bitcoinin sisäisestä toiminnasta. Liity meihin Bitcoin Baguetten pariin ollaksesi osa Pariisin Bitcoin-yhteisöä ja pysyäksesi ajan tasalla alan viimeisimmistä edistysaskeleista.

contributors:
- 
```
![builder](assets/37.webp)
- Klikkaa `Commit changes` -nappia:
![builder](assets/38.webp)
- Varmista, että `Commit directly to the patch-1 branch` -ruutu on valittu, lisää otsikko, ja klikkaa sitten `Commit changes`:
![builder](assets/39.webp)
- Yrityksesi kansio pitäisi nyt näyttää tältä:
![builder](assets/40.webp)
- Jos kaikki on mielestäsi kunnossa, palaa takaisin haarasi juureen:
![builder](assets/41.webp)
- Sinun pitäisi nähdä viesti, joka ilmoittaa, että haarassasi on tapahtunut muutoksia. Klikkaa `Compare & pull request` -nappia:
![builder](assets/42.webp)
- Lisää selkeä otsikko ja kuvaus PR:ääsi:
![builder](assets/43.webp)
- Klikkaa `Create pull request` -nappia:
![builder](assets/44.webp)
Onnittelut! PR:äsi on luotu onnistuneesti. Ylläpitäjä tarkistaa sen nyt ja, jos kaikki on kunnossa, integroi sen PlanB-verkoston päärepositoryyn. Rakentajaprofiilisi pitäisi ilmestyä verkkosivustolle muutaman päivän kuluttua.

Varmista, että seuraat PR:äsi edistymistä. Ylläpitäjä saattaa jättää kommentin pyytäen lisätietoja. Niin kauan kuin PR:äsi ei ole vahvistettu, voit tarkastella sitä `Pull requests`-välilehdessä PlanB-verkoston GitHub-repositoryssa:
![builder](assets/45.webp)
Suurkiitokset arvokkaasta panoksestasi! :)
