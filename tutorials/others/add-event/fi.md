---
name: Lisää tapahtuma PlanB-verkkoon
description: Miten ehdotan uuden tapahtuman lisäämistä PlanB-verkkoon?
---
![event](assets/cover.webp)

PlanB:n tehtävänä on tarjota huipputason koulutusresursseja Bitcoinista mahdollisimman monella kielellä. Kaikki sivustolla julkaistu sisältö on avoimen lähdekoodin ja isännöity GitHubissa, tarjoten kenelle tahansa mahdollisuuden osallistua alustan rikastuttamiseen.

Jos haluat lisätä Bitcoin-konferenssin PlanB-verkon sivustolle ja lisätä näkyvyyttä tapahtumallesi, mutta et tiedä miten? Tämä opas on sinua varten!
![event](assets/01.webp)
- Ensimmäiseksi sinun on oltava GitHub-tili. Jos et tiedä, miten tili luodaan, olemme tehneet yksityiskohtaisen oppaan, joka opastaa sinua.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c


- Mene [PlanB:n GitHub-repositorioon, joka on omistettu datalle](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) osiossa `resources/conference/`:
![event](assets/02.webp)
- Klikkaa oikeassa yläkulmassa `Add file` -painiketta, sitten `Create new file`:
![event](assets/03.webp)
- Jos et ole aiemmin osallistunut PlanB-verkon sisältöön, sinun on luotava oma haarasi alkuperäisestä repositoriosta. Repositorion haarauttaminen tarkoittaa kyseisen repositorion kopion luomista omalle GitHub-tilillesi, mikä mahdollistaa projektissa työskentelyn alkuperäistä repositoriota muuttamatta. Klikkaa `Fork this repository` -painiketta:
![event](assets/04.webp)
- Tämän jälkeen saavut GitHubin muokkaussivulle:
![event](assets/05.webp)
- Luo kansio konferenssillesi. Tee tämä kirjoittamalla `Name your file...` -kenttään konferenssisi nimi pienillä kirjaimilla ja väliviivat välilyöntien sijaan. Esimerkiksi, jos konferenssisi on nimeltään "Paris Bitcoin Conference", sinun tulisi merkitä `paris-bitcoin-conference`. Lisää myös konferenssisi vuosi, esimerkiksi: `paris-bitcoin-conference-2024`:
![event](assets/06.webp)
- Kansion luomisen vahvistamiseksi kirjoita vain kauttaviiva nimesi perään samassa kentässä, esimerkiksi: `paris-bitcoin-conference-2024/`. Kauttaviivan lisääminen luo automaattisesti kansion tiedoston sijaan:
![event](assets/07.webp)
- Tässä kansiossa luot ensimmäisen YAML-tiedoston nimeltä `events.yml`:
![event](assets/08.webp)
- Täytä tämä tiedosto konferenssisi tiedoilla käyttäen tätä mallia:

```yaml
- start_date:
  end_date:
  address_line_1:
  address_line_2: 
  address_line_3: 
  name:
  builder:
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
  description:
  language: 
    - 
  links:
    website:
    replay_url:    
    live_url :
  tags: 
    - 
```

Esimerkiksi, YAML-tiedostosi voisi näyttää tältä:

```yaml
- start_date: 2024-08-15
  end_date: 2024-08-18
  address_line_1: Pariisi, Ranska
  address_line_2: 
  address_line_3: 
  name: Paris Bitcoin Conference 2024
  builder: Paris Bitcoin Conference
  type: conference
  book_online: false
  book_in_person: false
  price_dollars: 0
description: Ranskan suurin Bitcoin-konferenssi, jossa on yli 8 000 osallistujaa joka vuosi! kieli:
    - fr
    - en
    - es
    - it
  linkit:
    verkkosivusto: https://paris.bitcoin.fr/conference
    uusintalähetys_url:
    suora_url:
  tagit:
    - Bitcoiner
    - Yleinen
    - Kansainvälinen
```
![tapahtuma](assets/09.webp)
Jos organisaatiollasi ei vielä ole "*builder*" tunnistetta, voit lisätä sen seuraamalla tätä toista opasta.

https://planb.network/tutorials/others/contribution/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d



- Kun olet valmis tekemään muutoksia tähän tiedostoon, tallenna ne napsauttamalla `Commit changes...` -painiketta:
![tapahtuma](assets/10.webp)
- Lisää otsikko muutoksillesi sekä lyhyt description:
![tapahtuma](assets/11.webp)
- Napsauta vihreää `Propose changes` -painiketta:
![tapahtuma](assets/12.webp)
- Tämän jälkeen päädyt sivulle, joka tiivistää kaikki muutoksesi:
![tapahtuma](assets/13.webp)
- Napsauta GitHub-profiilikuvakettasi oikeassa yläkulmassa, sitten `Your Repositories`:
![tapahtuma](assets/14.webp)
- Valitse PlanB Network -repositoriosi haarautuma:
![tapahtuma](assets/15.webp)
- Sinun pitäisi nähdä ilmoitus ikkunan yläosassa uudesta haarastasi. Sen nimi on todennäköisesti `patch-1`. Napsauta sitä:
![tapahtuma](assets/16.webp)
- Olet nyt työhaarassasi:
![tapahtuma](assets/17.webp)
- Palaa takaisin `resources/conference/` -kansioon ja valitse konferenssisi kansio, jonka juuri loit edellisessä commitissa:
![tapahtuma](assets/18.webp)
- Konferenssisi kansiosta, napsauta `Add file` -painiketta, sitten `Create new file`:
![tapahtuma](assets/19.webp)
- Nimeä tämä uusi kansio `assets` ja vahvista sen luominen laittamalla kauttaviiva `/` loppuun:
![tapahtuma](assets/20.webp)
- Tässä `assets` -kansiossa, luo tiedosto nimeltä `.gitkeep`:
![tapahtuma](assets/21.webp)
- Napsauta `Commit changes...` -painiketta:
![tapahtuma](assets/22.webp)
- Jätä commit-otsikko oletusarvoiseksi ja varmista, että `Commit directly to the patch-1 branch` -ruutu on valittu, sitten napsauta `Commit changes`:
![tapahtuma](assets/23.webp)
- Palaa takaisin `assets` -kansioon:
![tapahtuma](assets/24.webp)
- Napsauta `Add file` -painiketta, sitten `Upload files`: ![tapahtuma](assets/25.webp)
- Uusi sivu avautuu. Vedä ja pudota kuva, joka edustaa konferenssiasi ja näytetään PlanB Network -sivustolla:
![tapahtuma](assets/26.webp)
- Se voi olla logo, pikkukuva tai jopa juliste:
![tapahtuma](assets/27.webp)
- Kun kuva on ladattu, varmista, että `Commit directly to the patch-1 branch` -ruutu on valittu, sitten napsauta `Commit changes`:
![tapahtuma](assets/28.webp)
- Ole varovainen, kuvan on oltava nimeltään `thumbnail` ja sen on oltava `.webp` -muodossa. Täydellinen tiedostonimi olisi siis: `thumbnail.webp`:
![tapahtuma](assets/29.webp)
- Palaa `assets` -kansioosi ja napsauta välitiedostoa `.gitkeep`:
![tapahtuma](assets/30.webp)
- Kun olet tiedostossa, klikkaa yläoikealla olevia kolmea pientä pistettä ja sitten `Poista tiedosto`: ![tapahtuma](assets/31.webp)
- Varmista, että olet edelleen samalla työhaaralla, ja klikkaa sitten `Sitoumuksen muutokset`-painiketta:
![tapahtuma](assets/32.webp)
- Lisää otsikko ja kuvaus sitoumukseesi, ja klikkaa sitten `Sitoumuksen muutokset`:
![tapahtuma](assets/33.webp)
- Palaa takaisin repositoriosi juureen:
![tapahtuma](assets/34.webp)
- Sinun pitäisi nähdä viesti, joka ilmoittaa haarasi kokeneen muutoksia. Klikkaa `Vertaa & tee vetopyyntö`-painiketta:
![tapahtuma](assets/35.webp)
- Lisää selkeä otsikko ja kuvaus PR:ääsi:
![tapahtuma](assets/36.webp)
- Klikkaa `Luo vetopyyntö`-painiketta:
![tapahtuma](assets/37.webp)
Onnittelut! PR:äsi on luotu onnistuneesti. Ylläpitäjä tarkistaa sen nyt, ja jos kaikki on kunnossa, yhdistää sen PlanB Networkin päärepositoryyn. Sinun pitäisi nähdä tapahtumasi ilmestyvän verkkosivustolle muutaman päivän kuluttua.

Muista seurata PR:si edistymistä. Ylläpitäjä saattaa jättää kommentin pyytäen lisätietoja. Niin kauan kuin PR:äsi ei ole vahvistettu, voit konsultoida sitä `Vetopyynnöt`-välilehdessä PlanB Networkin GitHub-repositoriossa:
![tapahtuma](assets/38.webp)
Suurkiitokset arvokkaasta panoksestasi! :)
