---
name: Een podcast toevoegen aan Plan ₿ Academy
description: Hoe voeg je een nieuwe podcast toe aan Plan ₿ Academy?
---
![podcast](assets/cover.webp)


De missie van PlanB is om eersteklas educatieve bronnen aan te bieden over Bitcoin in zoveel mogelijk talen. Alle inhoud die op de site wordt gepubliceerd is open-source en wordt gehost op GitHub, zodat iedereen kan deelnemen aan het verrijken van het platform.


Wil je een Bitcoin podcast toevoegen aan de Plan ₿ Academy site en de zichtbaarheid van je show vergroten, maar weet je niet hoe? Dan is deze tutorial voor jou!
![podcast](assets/01.webp)


- Eerst moet je een GitHub account hebben. Als je niet weet hoe je er een moet aanmaken, hebben we een gedetailleerde tutorial gemaakt om je te begeleiden.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Ga naar [de GitHub repository van PlanB gewijd aan data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/podcasts) in de `resources/podcasts/` sectie:
![podcast](assets/02.webp)


- Klik rechtsboven op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken:
![podcast](assets/03.webp)


- Als je nog nooit hebt bijgedragen aan de inhoud van Plan ₿ Academy, zul je een fork van de originele repository moeten maken. Een repository forken betekent dat je een kopie van die repository maakt op je eigen GitHub account, zodat je aan het project kunt werken zonder de originele repository te beïnvloeden. Klik op de knop `Fork this repository`:
![podcast](assets/04.webp)


- Je komt dan op de GitHub bewerkingspagina:
![podcast](assets/05.webp)


- Maak een map aan voor je podcast. Om dit te doen, schrijf je in het vak `Name your file...` (Naam van je bestand...) de naam van je podcast in kleine letters met streepjes in plaats van spaties. Als je show bijvoorbeeld "Super Podcast Bitcoin" heet, schrijf je `super-podcast-Bitcoin`:
![podcast](assets/06.webp)


- Om de aanmaak van de map te valideren, voeg je gewoon een schuine streep toe na de naam van je podcast in hetzelfde vak, bijvoorbeeld: `super-podcast-Bitcoin/`. Door een schuine streep toe te voegen, wordt automatisch een map aangemaakt in plaats van een bestand:
![podcast](assets/07.webp)


- In deze map maak je een eerste YAML-bestand met de naam `podcast.yml`:
![podcast](assets/08.webp)


- Vul dit bestand in met informatie over je podcast met behulp van dit sjabloon:


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


Hier zijn de gegevens die je voor elk veld moet invullen:



- `name`: Geef de naam van je podcast aan.
- `host`: Vermeld de namen of pseudoniemen van de sprekers of de host van de podcast. Elke naam moet gescheiden worden door een komma.
- `language`: Geef de taalcode aan van de taal die in je podcast wordt gesproken. Bijvoorbeeld, voor Engels, noteer `en`, voor Italiaans `it`...
- `links`: Geef links naar je inhoud. Je hebt twee opties:
  - `podcast`: de link naar je podcast,
  - `twitter`: de link naar het Twitter-profiel van de podcast of de organisatie die hem produceert,
  - `website`: de link naar de website van de podcast of de organisatie die hem produceert.
- `description`: Voeg een korte paragraaf toe die je podcast beschrijft. De beschrijving moet in dezelfde taal zijn als aangegeven in het `language:` veld.
- `tags`: Voeg twee tags toe die bij je podcast horen. Voorbeelden:
  - `bitcoin`
  - `technology`
  - `economy`
  - `education`...

- `contributors`: Vermeld je contribuant ID als je die hebt.


Je YAML-bestand zou er bijvoorbeeld zo uit kunnen zien:


```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
twitter: https://twitter.com/decouvrebitcoin
website: https://decouvrebitcoin.fr
description: |
Super Podcast Bitcoin is a technical LIVE session held once a week on Twitter to delve deep into the Bitcoin protocol, layer two solutions, and all things that blow minds. Our hosts Lounes, Pantamis, Loïc, and Sosthene will answer your questions and offer the most technical show on Bitcoin in the world.

tags:
- bitcoin
- technology
contributors:
- rabbit-hole
```


![podcast](assets/09.webp)



- Als je klaar bent met het maken van wijzigingen in dit bestand, sla ze dan op door te klikken op de knop `Commit changes...` (Wijzigingen vastleggen...):
![podcast](assets/10.webp)


- Voeg een titel toe voor je wijzigingen, evenals een korte beschrijving:
![podcast](assets/11.webp)


- Klik op de groene knop `Propose changes` (Wijzigingen voorstellen):
![podcast](assets/12.webp)


- Je komt dan op een pagina die al je wijzigingen samenvat:
![podcast](assets/13.webp)


- Klik op je GitHub profielfoto rechtsboven, dan op `Your Repositories`:
![podcast](assets/14.webp)


- Selecteer je fork van de Plan ₿ Academy repository:
![podcast](assets/15.webp)


- Je zou een melding bovenaan het venster moeten zien met je nieuwe branch. Het heet waarschijnlijk `patch-1`. Klik erop:
![podcast](assets/16.webp)


- Je bent nu op je branch:
![podcast](assets/17.webp)


- Ga terug naar de `resources/podcast/` map en selecteer de podcast map die je zojuist hebt aangemaakt in de vorige commit:
![podcast](assets/18.webp)

- Klik in je podcastmap op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):
![podcast](assets/19.webp)


- Geef deze nieuwe map de naam `assets` en bevestig de aanmaak door een schuine streep `/` aan het einde toe te voegen:
![podcast](assets/20.webp)


- Maak in deze `assets` map een bestand aan met de naam `.gitkeep`:
![podcast](assets/21.webp)


- Klik op de knop `Commit changes...` (Wijzigingen vastleggen...):
![podcast](assets/22.webp)


- Laat de commit titel als standaard staan, en zorg ervoor dat het `Commit directly to the patch-1 branch` vakje aangevinkt is, klik dan op `Commit changes...` (Wijzigingen vastleggen...):
![podcast](assets/23.webp)


- Ga terug naar de map `assets`:
![podcast](assets/24.webp)


- Klik op de knop `Add file` (Bestand toevoegen) en vervolgens op `Upload files` (Bestanden uploaden):
![podcast](assets/25.webp)


- Er wordt een nieuwe pagina geopend. Sleep je podcastlogo naar het gebied. Deze afbeelding zal getoond worden op de Plan ₿ Academy site:
![podcast](assets/26.webp)


- Let op, de afbeelding moet vierkant zijn, zodat deze het beste op onze website past:
![podcast](assets/27.webp)


- Zodra de image geüpload is, controleer dan of het `Commit directly to the patch-1 branch` vakje aangevinkt is en klik dan op `Commit changes` (Wijzigingen vastleggen):
![podcast](assets/28.webp)


- Let op, je afbeelding moet `logo` heten en het formaat `.webp` hebben. De volledige bestandsnaam moet daarom zijn: `logo.webp`:
![podcast](assets/29.webp)


- Ga terug naar je `assets` map en klik op het tussenliggende bestand `.gitkeep`:
![podcast](assets/30.webp)


- Klik op de drie kleine puntjes rechtsboven in het bestand en vervolgens op `Delete file` (Bestand verwijderen):
![podcast](assets/31.webp)


- Controleer of je nog steeds op dezelfde branch zit en klik dan op de knop `Commit changes` (Wijzigingen vastleggen):
![podcast](assets/32.webp)


- Voeg een titel en beschrijving toe aan je vastlegging en klik dan op `Commit changes` (Wijzigingen vastleggen):
![podcast](assets/33.webp)


- Ga terug naar de root van je repository:
![podcast](assets/34.webp)


- Je zou een bericht moeten zien dat aangeeft dat je branch wijzigingen heeft ondergaan. Klik op de knop `Compare & pull request` (Vergelijk & pull verzoek):
![podcast](assets/35.webp)


- Voeg een duidelijke titel en beschrijving toe aan je PR:
![podcast](assets/36.webp)


- Klik op de knop `Create pull request`:
![podcast](assets/37.webp)

Gefeliciteerd! Je PR is succesvol aangemaakt. Een beheerder zal het nu bekijken en, als alles in orde is, samenvoegen in de hoofdrepository van Plan ₿ Academy. Je zou je podcast enkele dagen later op de website moeten zien verschijnen.


Zorg ervoor dat je de voortgang van je PR volgt. Een beheerder kan een opmerking achterlaten waarin om extra informatie wordt gevraagd. Zolang je PR niet gevalideerd is, kun je het bekijken in de `Pull requests` tab op de Plan ₿ Academy GitHub repository:
![podcast](assets/38.webp)

Hartelijk dank voor je waardevolle bijdrage! :)
