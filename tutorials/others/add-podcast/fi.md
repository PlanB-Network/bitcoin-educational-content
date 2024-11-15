---
name: Podcastin lisääminen PlanB-verkkoon
description: Kuinka lisätä uusi podcast PlanB-verkkoon?
---
![podcast](assets/cover.webp)

PlanB:n tehtävänä on tarjota huipputason koulutusresursseja Bitcoinista mahdollisimman monella kielellä. Kaikki sivustolla julkaistu sisältö on avoimen lähdekoodin ja isännöity GitHubissa, mikä mahdollistaa kenen tahansa osallistumisen alustan rikastuttamiseen.

Haluatko lisätä Bitcoin-podcastisi PlanB-verkon sivustolle ja lisätä ohjelmasi näkyvyyttä, mutta et tiedä miten? Tämä opas on sinua varten!
![podcast](assets/01.webp)
- Ensimmäiseksi tarvitset GitHub-tilin. Jos et tiedä, miten sellainen luodaan, olemme tehneet yksityiskohtaisen oppaan, joka opastaa sinua.

https://planb.network/tutorials/others/create-github-account


- Mene [PlanB:n GitHub-repositorioon, joka on omistettu dataan](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts) osiossa `resources/podcasts/`:
![podcast](assets/02.webp)
- Klikkaa oikeassa yläkulmassa `Add file` -painiketta, sitten `Create new file`:
![podcast](assets/03.webp)
- Jos et ole aiemmin osallistunut PlanB-verkon sisällön tuottamiseen, sinun täytyy luoda oma haarasi alkuperäisestä repositoriosta. Repositorion haarauttaminen tarkoittaa sen kopion luomista omalle GitHub-tilillesi, mikä mahdollistaa projektissa työskentelyn alkuperäistä repositoriota muuttamatta. Klikkaa `Fork this repository` -painiketta:
![podcast](assets/04.webp)
- Tämän jälkeen päädyt GitHubin muokkaussivulle:
![podcast](assets/05.webp)
- Luo kansio podcastillesi. Tee tämä kirjoittamalla `Name your file...` -kenttään podcastisi nimi pienillä kirjaimilla ja välilyönnit korvaten viivoilla. Esimerkiksi, jos ohjelmasi on nimeltään "Super Podcast Bitcoin", sinun tulisi kirjoittaa `super-podcast-bitcoin`:
![podcast](assets/06.webp)
- Vahvistaaksesi kansion luomisen, lisää vain kauttaviiva podcastisi nimen perään samassa kentässä, esimerkiksi: `super-podcast-bitcoin/`. Kauttaviivan lisääminen luo automaattisesti kansion tiedoston sijaan:
![podcast](assets/07.webp)
- Tässä kansiossa luot ensimmäisen YAML-tiedoston nimeltä `podcast.yml`:
![podcast](assets/08.webp)
- Täytä tämä tiedosto tiedoilla podcastistasi käyttäen tätä mallia:

```yaml
name: 
host: 
language: 
links:
  podcast: 
  twitter: 
  website: 
description: |
  
tags:
  - 
  - 
contributors:
  - 
```

Tässä ovat tiedot, jotka tulee täyttää kullekin kentälle:

- **`name`**: Ilmoita podcastisi nimi.
- **`host`**: Luettele puhujien tai juontajan nimet tai nimimerkit. Jokainen nimi tulee erottaa pilkulla.
- **`language`**: Ilmoita podcastissasi puhutun kielen kielikoodi. Esimerkiksi englanniksi `en`, italiaksi `it`...

- **`links`**: Tarjoa linkit sisältöösi. Sinulla on kaksi vaihtoehtoa:
	- `podcast`: linkki podcastiisi,
	- `twitter`: linkki podcastin tai sitä tuottavan organisaation Twitter-profiiliin,
	- `website`: linkki podcastin tai sitä tuottavan organisaation verkkosivustolle.
- **`description`**: Lisää lyhyt kappale, joka kuvaa podcastiasi. Kuvaus on oltava samalla kielellä kuin `language:`-kentässä on ilmoitettu.
- **`tags`**: Lisää kaksi tagia, jotka liittyvät podcastiisi. Esimerkkejä:
    - `bitcoin`
    - `teknologia`
    - `talous`
    - `koulutus`...

- **`contributors`**: Mainitse avustajasi ID, jos sinulla on sellainen.

Esimerkiksi YAML-tiedostosi voisi näyttää tältä:

```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
  podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
  twitter: https://twitter.com/decouvrebitcoin
  website: https://decouvrebitcoin.fr
description: |
  Super Podcast Bitcoin on tekninen LIVE-istunto, joka pidetään kerran viikossa Twitterissä syventymään Bitcoin-protokollaan, toisen kerroksen ratkaisuihin ja kaikkeen, mikä hämmästyttää. Isäntämme Lounes, Pantamis, Loïc ja Sosthene vastaavat kysymyksiisi ja tarjoavat maailman teknisimmän shown Bitcoinista.

tags:
  - bitcoin
  - teknologia
contributors:
  - rabbit-hole
```

![podcast](assets/09.webp)

- Kun olet valmis tekemään muutoksia tähän tiedostoon, tallenna ne napsauttamalla `Commit changes...` -painiketta:
![podcast](assets/10.webp)
- Lisää muutoksillesi otsikko sekä lyhyt description:
![podcast](assets/11.webp)
- Napsauta vihreää `Propose changes` -painiketta:
![podcast](assets/12.webp)
- Tämän jälkeen päädyt sivulle, joka tiivistää kaikki muutoksesi:
![podcast](assets/13.webp)
- Napsauta GitHub-profiilikuvakettasi oikeassa yläkulmassa ja sitten `Your Repositories`:
![podcast](assets/14.webp)
- Valitse forkkaamasi PlanB Network -repositorio:
![podcast](assets/15.webp)
- Sinun pitäisi nähdä ilmoitus ikkunan yläosassa uudesta haarastasi. Se on todennäköisesti nimeltään `patch-1`. Napsauta sitä:
![podcast](assets/16.webp)
- Olet nyt työhaarassasi:
![podcast](assets/17.webp)
- Palaa takaisin `resources/podcast/`-kansioon ja valitse podcast-kansio, jonka loit edellisessä commitissa: ![podcast](assets/18.webp)
- Podcast-kansiossasi napsauta `Add file` -painiketta ja sitten `Create new file`:
![podcast](assets/19.webp)
- Nimeä tämä uusi kansio `assets` ja vahvista sen luominen lisäämällä loppuun kauttaviiva `/`:
![podcast](assets/20.webp)
- Tässä `assets`-kansiossa, luo tiedosto nimeltä `.gitkeep`:
![podcast](assets/21.webp)
- Napsauta `Commit changes...` -painiketta:
![podcast](assets/22.webp)
- Jätä commit-otsikko oletusarvoiseksi ja varmista, että `Commit directly to the patch-1 branch` -ruutu on valittuna, sitten napsauta `Commit changes`:
![podcast](assets/23.webp)
- Palaa takaisin `assets`-kansioon:
![podcast](assets/24.webp)
- Napsauta `Add file` -painiketta ja sitten `Upload files`:
![podcast](assets/25.webp)
- Uusi sivu avautuu. Vedä ja pudota podcast-logosi alueelle. Tämä kuva näytetään PlanB Network -sivustolla: ![podcast](assets/26.webp)
- Ole varovainen, kuvan tulee olla neliön muotoinen, jotta se sopii parhaiten verkkosivustollemme:
![podcast](assets/27.webp)
- Kun kuva on ladattu, varmista, että `Commit directly to the patch-1 branch` -ruutu on valittu, ja klikkaa sitten `Commit changes`:
![podcast](assets/28.webp)
- Ole varovainen, kuvan nimen tulee olla `logo` ja sen tulee olla `.webp`-muodossa. Täydellinen tiedostonimi tulee siis olla: `logo.webp`:
![podcast](assets/29.webp)
- Palaa `assets`-kansioosi ja klikkaa välitiedostoa `.gitkeep`:
![podcast](assets/30.webp)
- Tiedostolla ollessasi klikkaa oikeassa yläkulmassa olevia kolmea pientä pistettä ja sitten `Delete file`:
![podcast](assets/31.webp)
- Varmista, että olet edelleen samalla työhaaralla, ja klikkaa sitten `Commit changes` -nappia:
![podcast](assets/32.webp)
- Lisää otsikko ja kuvaus commitillesi, ja klikkaa sitten `Commit changes`:
![podcast](assets/33.webp)
- Palaa takaisin repositoriosi juureen:
![podcast](assets/34.webp)
- Sinun pitäisi nähdä viesti, joka ilmoittaa, että haarassasi on tapahtunut muutoksia. Klikkaa `Compare & pull request` -nappia:
![podcast](assets/35.webp)
- Lisää selkeä otsikko ja kuvaus PR:ääsi:
![podcast](assets/36.webp)
- Klikkaa `Create pull request` -nappia:
![podcast](assets/37.webp)
Onnittelut! PR:äsi on luotu onnistuneesti. Ylläpitäjä tarkistaa sen nyt ja, jos kaikki on kunnossa, yhdistää sen PlanB Networkin päärepositoryyn. Sinun pitäisi nähdä podcastisi ilmestyvän verkkosivustolle muutaman päivän kuluttua.

Muista seurata PR:äsi edistymistä. Ylläpitäjä saattaa jättää kommentin pyytäen lisätietoja. Niin kauan kuin PR:äsi ei ole vahvistettu, voit tarkastella sitä PlanB Network GitHub -repositorion `Pull requests` -välilehdessä:
![podcast](assets/38.webp)
Kiitos arvokkaasta panoksestasi! :)
