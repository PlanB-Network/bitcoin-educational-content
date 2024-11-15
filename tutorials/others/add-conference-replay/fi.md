---
name: Konferenssin Uusinnan Lisääminen
description: Kuinka lisätä konferenssin uusinta PlanB-verkkoon?
---
![konferenssi](assets/cover.webp)

PlanB:n tehtävänä on tarjota huipputason koulutusresursseja Bitcoinista mahdollisimman monella kielellä. Kaikki sivustolla julkaistu sisältö on avoimen lähdekoodin ja isännöity GitHubissa, mikä mahdollistaa kenen tahansa osallistumisen alustan rikastuttamiseen.

Haluatko lisätä Bitcoin-konferenssisi uusinnan PlanB-verkon sivustolle ja antaa tälle tapahtumalle näkyvyyttä, mutta et tiedä miten? Tämä opas on sinua varten!

Jos kuitenkin haluat lisätä tulevaisuudessa tapahtuvan konferenssin, suosittelen lukemaan tämän toisen oppaan, jossa selitämme, kuinka lisätä uusi tapahtuma sivustolle.

https://planb.network/tutorials/others/add-event


![konferenssi](assets/01.webp)
- Ensimmäiseksi sinun on oltava tili GitHubissa. Jos et tiedä, kuinka luoda tiliä, olemme tehneet yksityiskohtaisen oppaan sinua varten.

https://planb.network/tutorials/others/create-github-account


- Siirry [PlanB:n GitHub-repositorioon, joka on omistettu datalle](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) `resources/conference/`-osiossa:
![konferenssi](assets/02.webp)
- Klikkaa oikeassa yläkulmassa `Add file`-painiketta, sitten `Create new file`:
![konferenssi](assets/03.webp)
- Jos et ole aiemmin osallistunut PlanB-verkon sisältöön, sinun on luotava oma haarasi alkuperäisestä repositoriosta. Repositorion haaroittaminen tarkoittaa sen kopion luomista omalle GitHub-tilillesi, mikä mahdollistaa projektissa työskentelyn alkuperäistä repositoriota muuttamatta. Klikkaa `Fork this repository` -painiketta:
![konferenssi](assets/04.webp)
- Tämän jälkeen päädyt GitHubin muokkaussivulle:
![konferenssi](assets/05.webp)
- Luo kansio konferenssillesi. Tee tämä kirjoittamalla `Name your file...`-kenttään konferenssisi nimi pienillä kirjaimilla ja väliviivat välilyöntien sijaan. Esimerkiksi, jos konferenssisi nimi on "Paris Bitcoin Conference", sinun tulisi merkitä `paris-bitcoin-conference`. Lisää myös konferenssisi vuosi, esimerkiksi: `paris-bitcoin-conference-2024`:
![konferenssi](assets/06.webp)
- Kansion luomisen vahvistamiseksi kirjoita vain kauttaviiva nimesi perään samassa kentässä, esimerkiksi: `paris-bitcoin-conference-2024/`. Kauttaviivan lisääminen luo automaattisesti kansion tiedoston sijaan:
![konferenssi](assets/07.webp)
- Tässä kansiossa luot ensimmäisen YAML-tiedoston nimeltä `conference.yml`:
![konferenssi](assets/08.webp)
Täytä tämä tiedosto konferenssiisi liittyvillä tiedoilla käyttäen tätä mallia:
```yaml
year: 
name: 
builder: 
location: 
language: 
  - 
links:
  website: 
  twitter: 
tags: 
  - 
  - 
```

Esimerkiksi YAML-tiedostosi voisi näyttää tältä:

```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
builder: Paris Bitcoin Conference
location: Pariisi, Ranska
language: 
  - fr
  - en
links:
  website: https://paris.bitcoin.fr/conference
  twitter: https://twitter.com/ParisBitcoinConference
tags: 
  - Kansainvälinen
  - Kaikki Yleisöt
```

![konferenssi](assets/09.webp)
Jos organisaatiollasi ei vielä ole "*builder*" tunnistetta, voit lisätä sen seuraamalla tätä toista opasta.
https://planb.network/tutorials/others/add-builder

- Kun olet valmis tekemään muutoksia tähän tiedostoon, tallenna ne napsauttamalla `Commit changes...` -painiketta:
![konferenssi](assets/10.webp)
- Lisää otsikko muutoksillesi sekä lyhyt kuvaus:
![konferenssi](assets/11.webp)
- Napsauta vihreää `Propose changes` -painiketta:
![konferenssi](assets/12.webp)
- Tämän jälkeen päädyt sivulle, joka tiivistää kaikki muutoksesi:
![konferenssi](assets/13.webp)
- Napsauta GitHub-profiilikuvakettasi oikeassa yläkulmassa, sitten `Your Repositories`:
![konferenssi](assets/14.webp)
- Valitse PlanB Network -repositoriosi forkki:
![konferenssi](assets/15.webp)
- Sinun pitäisi nähdä ilmoitus ikkunan yläosassa uudesta haarastasi. Se on todennäköisesti nimeltään `patch-1`. Napsauta sitä:
![konferenssi](assets/16.webp)
- Olet nyt työhaarassasi:
![konferenssi](assets/17.webp)
- Palaa `resources/conference/` -kansioon ja valitse konferenssisi kansio, jonka juuri loit edellisessä commitissa:
![konferenssi](assets/18.webp)
- Konferenssisi kansiosta, napsauta `Add file` -painiketta, sitten `Create new file`:
![konferenssi](assets/19.webp)
- Nimeä tämä uusi kansio `assets` ja vahvista sen luominen laittamalla kauttaviiva `/` loppuun:
![konferenssi](assets/20.webp)
- Tässä `assets` -kansiossa, luo tiedosto nimeltä `.gitkeep`:
![konferenssi](assets/21.webp)
- Napsauta `Commit changes...` -painiketta:
![konferenssi](assets/22.webp)
- Jätä commit-otsikko oletusarvoiseksi ja varmista, että `Commit directly to the patch-1 branch` -ruutu on valittuna, sitten napsauta `Commit changes`:
![konferenssi](assets/23.webp)
- Palaa `assets` -kansioon:
![konferenssi](assets/24.webp)
- Napsauta `Add file` -painiketta, sitten `Upload files`:
![konferenssi](assets/25.webp)
- Uusi sivu avautuu. Vedä ja pudota kuva, joka edustaa konferenssiasi ja joka näytetään PlanB Network -sivustolla: ![konferenssi](assets/26.webp)
- Se voi olla logo, pikkukuva tai jopa juliste:
![konferenssi](assets/27.webp)
- Kun kuva on ladattu, tarkista, että `Commit directly to the patch-1 branch` -ruutu on valittuna, sitten napsauta `Commit changes`:
![konferenssi](assets/28.webp)
- Ole varovainen, kuvan on oltava nimeltään `thumbnail` ja sen on oltava `.webp` -muodossa. Täydellinen tiedostonimi olisi siis: `thumbnail.webp`:
![konferenssi](assets/29.webp)
- Palaa `assets` -kansioosi ja napsauta `.gitkeep` välitiedostoa:
![konferenssi](assets/30.webp)
- Tiedostossa ollessasi, napsauta kolmea pientä pistettä oikeassa yläkulmassa ja sitten `Delete file`:
![konferenssi](assets/31.webp)
- Varmista, että olet edelleen samalla työhaaralla, sitten napsauta `Commit changes` -painiketta:
![konferenssi](assets/32.webp)
- Lisää otsikko ja kuvaus commitillesi, sitten napsauta `Commit changes`:
![konferenssi](assets/33.webp)
- Palaa konferenssikansioosi: ![konferenssi](assets/34.webp)
- Klikkaa `Add file` -nappia, sitten `Create new file`:
![konferenssi](assets/35.webp)
- Luo uusi markdown (.md) tiedosto antamalla sille nimi kohdekielen tunnuksella. Tätä tiedostoa käytetään konferenssiesi uusintojen tallentamiseen. Esimerkiksi, jos haluan kirjoittaa konferenssien kuvaukset englanniksi, nimenän tämän tiedoston en.md:
![konferenssi](assets/36.webp)
- Täytä tämä markdown-tiedosto käyttäen tätä mallia, jonka voit mukauttaa konferenssisi asetuksiin:

```markdown
---
name: Pariisin Bitcoin-konferenssi 2024
description: Suurin Bitcoin-konferenssi Ranskassa, jossa on yli 8 000 osallistujaa joka vuosi!
--- 

# Pääareena

## Perjantaiaamu

![video](https://youtu.be/XXXXXXXXXXXX)

## Perjantai-iltapäivä

![video](https://youtu.be/XXXXXXXXXXXX)

## Lauantaiaamu

![video](https://youtu.be/XXXXXXXXXXXX)

## Lauantai-iltapäivä

![video](https://youtu.be/XXXXXXXXXXXX)

# Työpaja-alue

## Bitcoin-louhinnan tulevaisuus: Haasteet ja innovaatiot

![video](https://youtu.be/XXXXXXXXXXXX)

Puhuja: Satoshi Nakamoto, Satoshi Nakamoto

## Onko yksityisyys vielä mahdollista Bitcoinissa?

![video](https://youtu.be/XXXXXXXXXXXX)

Puhuja: Satoshi Nakamoto

## Bitcoin Core: Syväsukellus koodikantaan

![video](https://youtu.be/XXXXXXXXXXXX)

Puhuja: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Bitcoin-lompakoiden rakentaminen ja turvaaminen Miniscriptin avulla

![video](https://youtu.be/XXXXXXXXXXXX)

Puhuja: Satoshi Nakamoto
```

![konferenssi](assets/37.webp)
- Dokumenttisi alussa "front matter" -osiossa, täytä `name:`-kenttä konferenssisi nimellä ja uusintojen vuodella. `description:`-kentässä kirjoita lyhyt kuvaus tapahtumastasi tiedoston kielen mukaisesti. Esimerkiksi tiedostolle nimeltä `en.md`, kuvaus tulisi olla englanniksi. PlanB Network -tiimi huolehtii kuvauksesi kääntämisestä käyttäen heidän malliaan.
- Ensimmäisen tason otsikot, merkitty `#`, käytetään konferenssin järjestämiseen kohtauksittain. Esimerkiksi `# Pääareena` pääareenalle ja `# Työpaja-alue` työpajoille omistetulle areenalle.

- Toisen tason otsikot, merkitty kaksinkertaisella `##`, käytetään eri uusintavideoiden erotteluun. Jos konferenssit kuvattiin jatkuvasti puolen päivän ajan, merkitse esimerkiksi `## Perjantaiaamu`. Jos konferenssit kuvattiin ja lähetettiin erikseen, nimeä konferenssi suoraan toisen tason otsikolla.

- Jokaisen toisen tason otsikon alle, lisää linkki vastaavaan uusintavideoon. Syntaksi tulisi olla: `![video](https://youtu.be/XXXXXXXXXXXX)`, korvaten `XXXXXXXXXXXX` todellisella videolinkillä.

- Jos formaatti sallii (yksittäiset konferenssit), voit lisätä puhujien nimet. Tee tämä lisäämällä `Speaker:`-kenttä seurattuna puhujan nimellä tai nimimerkillä videolinkin alle. Useiden puhujien tapauksessa, erota kunkin nimi pilkulla, esimerkiksi näin: `Puhuja: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.

---

- Kun olet saanut muutokset tähän tiedostoon valmiiksi, tallenna ne klikkaamalla `Commit changes...` -nappia:
![konferenssi](assets/38.webp)
- Lisää muutoksillesi otsikko sekä lyhyt kuvaus:
![konferenssi](assets/39.webp)
- Klikkaa `Commit changes` -painiketta: ![konferenssi](assets/40.webp)
- Konferenssikansiosi pitäisi nyt näyttää tältä:
![konferenssi](assets/41.webp)
- Jos kaikki on mielestäsi kunnossa, palaa takaisin haarasi juureen:
![konferenssi](assets/42.webp)
- Sinun pitäisi nähdä viesti, joka ilmoittaa haaraasi tehdyistä muutoksista. Klikkaa `Compare & pull request` -painiketta:
![konferenssi](assets/43.webp)
- Lisää selkeä otsikko ja kuvaus PR:lle:
![konferenssi](assets/44.webp)
- Klikkaa `Create pull request` -painiketta:
![konferenssi](assets/45.webp)
Onnittelut! PR:si on luotu onnistuneesti. Ylläpitäjä tarkistaa sen nyt ja, jos kaikki on kunnossa, yhdistää sen PlanB Networkin päärepositoryyn. Konferenssiesi tallenteet ilmestyvät verkkosivustolle muutaman päivän kuluttua.

Muista seurata PR:si etenemistä. On mahdollista, että ylläpitäjä jättää kommentin pyytäen lisätietoja. Niin kauan kuin PR:si ei ole vahvistettu, voit tarkastella sitä PlanB Networkin GitHub-repositoryn `Pull requests` -välilehdellä:
![konferenssi](assets/46.webp)

Suurkiitokset arvokkaasta panoksestasi! :)
