---
name: Kirjan lisääminen PlanB-verkkoon
description: Miten lisätä uusi kirja PlanB-verkkoon?
---
![kirja](assets/cover.webp)

PlanB:n tehtävänä on tarjota huipputason koulutusresursseja Bitcoinista mahdollisimman monella kielellä. Kaikki sivustolla julkaistu sisältö on avoimen lähdekoodin ja isännöity GitHubissa, mikä mahdollistaa kenen tahansa osallistumisen alustan rikastuttamiseen.

**Haluatko lisätä Bitcoin-aiheisen kirjan PlanB-verkon sivustolle ja lisätä työsi näkyvyyttä, mutta et tiedä miten? Tämä opas on sinua varten!**
![kirja](assets/01.webp)
- Ensimmäiseksi sinun tarvitsee olla GitHub-tili. Jos et tiedä, miten tili luodaan, olemme tehneet yksityiskohtaisen oppaan sinua varten.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Mene [PlanB:n GitHub-repositorioon, joka on omistettu datalle](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/books) osiossa `resources/books/`:
![kirja](assets/02.webp)
- Klikkaa oikeassa yläkulmassa `Add file` -nappia, sitten `Create new file`:
![kirja](assets/03.webp)
- Jos et ole aiemmin osallistunut PlanB-verkon sisältöön, sinun tarvitsee luoda oma haarasi alkuperäisestä repositoriosta. Repositorion haarauttaminen tarkoittaa sen kopion luomista omalle GitHub-tilillesi, mikä mahdollistaa projektissa työskentelyn alkuperäistä repositoriota muuttamatta. Klikkaa `Fork this repository` -nappia:
![kirja](assets/04.webp)
- Tämän jälkeen päädyt GitHubin muokkaussivulle:
![kirja](assets/05.webp)
- Luo kansio kirjallesi. Tee tämä kirjoittamalla `Name your file...` -kenttään kirjasi nimi pienillä kirjaimilla ja välilyönnit korvaten viivoilla. Esimerkiksi, jos kirjasi nimi on "*My Bitcoin Book*", sinun tulisi kirjoittaa `my-bitcoin-book`:
![kirja](assets/06.webp)
- Kansion luomisen vahvistamiseksi lisää vain kauttaviiva kirjasi nimen perään samassa kentässä, esimerkiksi: `my-bitcoin-book/`. Kauttaviivan lisääminen luo automaattisesti kansion tiedoston sijaan:
![kirja](assets/07.webp)
- Tässä kansiossa luot ensimmäisen YAML-tiedoston nimeltä `book.yml`:
![kirja](assets/08.webp)
- Täytä tämä tiedosto tiedoilla kirjastasi käyttäen tätä mallia:

```yaml
author: 
level: 
tags:
  - 
  - 
```

Tässä ovat kentät, jotka sinun tulee täyttää:
- **`author`**: Ilmoita kirjan kirjoittajan nimi.
- **`level`**: Ilmoita vaadittu taso, jotta kirjan voi ymmärtää hyvin. Valitse taso seuraavista:
	- `beginner`
	- `intermediate`
- `advanced` - `expert`
- **`tags`**: Lisää kaksi tai kolme kirjaasi liittyvää tagia. Esimerkiksi:
    - `bitcoin`
    - `history`
    - `technology`
    - `economy`
    - `education`...

Esimerkiksi, YAML-tiedostosi voisi näyttää tältä:

```yaml
author: Loïc Morel
level: beginner
tags:
  - bitcoin
  - technology
```

![kirja](assets/09.webp)
- Kun olet valmis tekemään muutokset tähän tiedostoon, tallenna ne klikkaamalla `Commit changes...` -nappia:
![kirja](assets/10.webp)
- Lisää muutoksillesi otsikko sekä lyhyt description: ![kirja](assets/11.webp)
- Klikkaa vihreää `Ehdota muutoksia` -painiketta: ![kirja](assets/12.webp)
- Tämän jälkeen päädyt sivulle, joka tiivistää kaikki tekemäsi muutokset: ![kirja](assets/13.webp)
- Klikkaa GitHub-profiilikuvakettasi oikeassa yläkulmassa, sitten `Omat Repositoriot`: ![kirja](assets/14.webp)
- Valitse PlanB Network -repositoriosi haara: ![kirja](assets/15.webp)
- Näet ikkunan yläosassa ilmoituksen uudesta haarastasi. Sen nimi on todennäköisesti `patch-1`. Klikkaa sitä: ![kirja](assets/16.webp)
- Olet nyt työhaarassasi: ![kirja](assets/17.webp)
- Palaa takaisin `resources/books/` -kansioon ja valitse juuri edellisessä sitoumuksessa luomasi kirjan kansio: ![kirja](assets/18.webp)
- Kirjasi kansion sisällä klikkaa `Lisää tiedosto` -painiketta, sitten `Luo uusi tiedosto`: ![kirja](assets/19.webp)
- Nimeä tämä uusi kansio `assets` ja vahvista sen luominen laittamalla kauttaviiva `/` loppuun: ![kirja](assets/20.webp)
- Tässä `assets` -kansiossa, luo tiedosto nimeltä `.gitkeep`: ![kirja](assets/21.webp)
- Klikkaa `Tee muutokset...` -painiketta: ![kirja](assets/22.webp)
- Jätä sitoumuksen otsikko oletusarvoiseksi ja varmista, että `Tee muutokset suoraan patch-1 -haaraan` -ruutu on valittu, sitten klikkaa `Tee muutokset`: ![kirja](assets/23.webp)
- Palaa takaisin `assets` -kansioon: ![kirja](assets/24.webp)
- Klikkaa `Lisää tiedosto` -painiketta, sitten `Lataa tiedostoja`: ![kirja](assets/25.webp)
- Uusi sivu avautuu. Vedä ja pudota kirjasi kansikuva alueelle. Tämä kuva näytetään PlanB Network -sivustolla: ![kirja](assets/26.webp)
- Ole varovainen, kuvan tulee olla kirjan muodossa, jotta se sopeutuu parhaiten sivustollemme, kuten esimerkiksi: ![kirja](assets/27.webp)
- Kun kuva on ladattu, varmista, että `Tee muutokset suoraan patch-1 -haaraan` -ruutu on valittu, sitten klikkaa `Tee muutokset`: ![kirja](assets/28.webp)- Huomaa, että kuvan tulee olla nimetty `cover_en` jos kansi on englanniksi ja sen tulee olla `.webp` -muodossa. Näin ollen täydellinen tiedostonimi olisi `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, jne. Jos haluat käyttää eri kansikuvaa kielellä, esimerkiksi kirjan käännöksen yhteydessä, voit sijoittaa ne samaan paikkaan `assets` -kansiossa: ![kirja](assets/29.webp)
- Palaa takaisin `assets` -kansioosi ja klikkaa `.gitkeep` välitiedostoa: ![kirja](assets/30.webp)
- Tiedostolla ollessasi, klikkaa kolmea pientä pistettä oikeassa yläkulmassa ja sitten `Poista tiedosto`: ![kirja](assets/31.webp)
- Varmista, että olet edelleen samassa työhaarassa, sitten klikkaa `Tee muutokset...` -painiketta: ![kirja](assets/32.webp)
- Lisää otsikko ja kuvaus sitoumukseesi, sitten klikkaa `Tee muutokset`: ![kirja](assets/33.webp)
- Palaa kirjasi kansioon: ![kirja](assets/34.webp)
- Klikkaa `Add file` -nappia, sitten `Create new file`:
![kirja](assets/35.webp)
- Luo uusi YAML-tiedosto antamalla sille nimi kirjan kielikoodin mukaan. Tätä tiedostoa käytetään kirjan kuvaukseen. Esimerkiksi, jos haluan kirjoittaa kuvaukseni englanniksi, nimeän tämän tiedoston `en.yml`:
![kirja](assets/36.webp)
- Täytä tämä YAML-tiedosto käyttäen tätä mallia:
```yaml
title: ""
publication_year: 
cover: cover_en.webp
original: true
description: |

contributors:
  - 
```

Tässä ovat tiedot, jotka tulee täyttää kullekin kentälle:
- **`title`**: Ilmoita kirjan nimi lainausmerkeissä.
- **`publication_year`**: Ilmoita vuosi, jona kirja julkaistiin.
- **`cover`**: Ilmoita tiedoston nimi, joka vastaa kansikuvaa, kieleen sopien, jota parhaillaan muokkaat olevaa YAML-tiedostoa varten. Esimerkiksi, jos muokkaat `en.yml` tiedostoa ja olet aiemmin lisännyt englanninkielisen kansikuvan nimeltä `cover_en.webp`, ilmoita vain `cover_en.webp` tässä kentässä.
- **`description`**: Lisää lyhyt kappale, joka kuvailee kirjaa. Kuvaus tulee olla samalla kielellä kuin YAML-tiedoston otsikossa ilmoitettu.
- **`contributors`**: Lisää kontribuutori-ID, jos sinulla on sellainen.

Esimerkiksi, YAML-tiedostosi voisi näyttää tältä:

```yaml
title: "Oma Bitcoin Kirjani"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
Löydä Bitcoinin mullistava maailma tämän kattavan oppaan avulla, joka on räätälöity aloittelijoille. Oma Bitcoin Kirjani tekee Bitcoinin monimutkaisuudesta ymmärrettävää, tarjoten selkeän ja tiiviin johdatuksen siihen, miten protokolla toimii. Sen vallankumouksellisesta teknologiasta sen mahdolliseen vaikutukseen maailmantalouteen, tämä kirja tarjoaa arvokkaita oivalluksia ja käytännön tietoa. Täydellinen niille, jotka ovat uusia Bitcoinin parissa, se kattaa perusteet, turvallisuusvinkit ja digitaalisen rahoituksen tulevaisuuden. Sukella rahan tulevaisuuteen ja varusta itsesi tiedolla, jotta voit luottavaisesti navigoida digitaalisessa iässä.

contributors:
  - pretty-private

![kirja](assets/37.webp)
- Klikkaa `Commit changes...` -nappia:
![kirja](assets/38.webp)
- Varmista, että `Commit directly to the patch-1 branch` -ruutu on valittu, lisää otsikko, sitten klikkaa `Commit changes`:
![kirja](assets/39.webp)
- Kirjakansion pitäisi nyt näyttää tältä:
![kirja](assets/40.webp)
- Jos kaikki näyttää hyvältä sinulle, palaa forkkisi juureen:
![kirja](assets/41.webp)
- Sinun pitäisi nähdä viesti, joka ilmoittaa, että haaraasi on tehty muutoksia. Klikkaa `Compare & pull request` -nappia:
![kirja](assets/42.webp)
- Lisää selkeä otsikko ja kuvaus PR:ääsi:
![kirja](assets/43.webp)
- Klikkaa `Create pull request` -nappia:
![kirja](assets/44.webp)
Onnittelut! PR:äsi on luotu onnistuneesti. Ylläpitäjä tarkistaa sen nyt ja, jos kaikki on kunnossa, yhdistää sen PlanB Networkin päärepositoryyn. Kirjasi pitäisi ilmestyä verkkosivustolle muutaman päivän kuluttua.

Muista seurata PR:äsi edistymistä. Ylläpitäjä saattaa jättää kommentin pyytäen lisätietoja. Niin kauan kuin PR:äsi ei ole vahvistettu, voit tarkastella sitä `Pull requests` -välilehdessä PlanB Networkin GitHub-repositoryssä.
Kiitos arvokkaasta panoksestasi! :)
