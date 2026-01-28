---
name: Een project toevoegen
description: Hoe stel je voor om een nieuw project toe te voegen aan Plan ₿ Academy?
---
![project](assets/cover.webp)


De missie van PlanB is om eersteklas educatieve bronnen aan te bieden over Bitcoin, in zoveel mogelijk talen. Alle inhoud die op de site wordt gepubliceerd is open-source en wordt gehost op GitHub, waardoor iedereen kan deelnemen aan het verrijken van het platform.


Wil je een nieuw Bitcoin "project" toevoegen aan de Plan ₿ Academy site en zichtbaarheid geven aan je bedrijf of software, maar weet je niet hoe? Dan is deze tutorial voor jou!

![project](assets/01.webp)


- Eerst moet je een GitHub account hebben. Als je niet weet hoe je een account aanmaakt, hebben we een gedetailleerde tutorial gemaakt om je te begeleiden.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Ga naar [de GitHub repository van PlanB gewijd aan data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects) in de `resources/project/` sectie:

![project](assets/02.webp)


- Klik rechtsboven op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):

![project](assets/03.webp)


- Als je nog nooit hebt bijgedragen aan de inhoud van Plan ₿ Academy, zul je een fork van de originele repository moeten maken. Een repository forken betekent dat je een kopie van die repository maakt op je eigen GitHub account, waarmee je aan het project kunt werken zonder de originele repository te beïnvloeden. Klik op de knop `Fork this repository`:

![project](assets/04.webp)


- Je komt dan op de GitHub bewerkingspagina:

![project](assets/05.webp)


- Maak een map voor je bedrijf. Om dit te doen, schrijf je in het vak `Name your file...` (Geef je bestand een naam...) de naam van je bedrijf in kleine letters met streepjes in plaats van spaties. Als je bedrijf bijvoorbeeld "Bitcoin Baguette" heet, schrijf je `Bitcoin-baguette`:

![project](assets/06.webp)


- Om het aanmaken van de map te valideren, voeg je gewoon een schuine streep toe na je naam in hetzelfde vak, bijvoorbeeld: `Bitcoin-baguette/`. Door een schuine streep toe te voegen, wordt automatisch een map aangemaakt in plaats van een bestand:

![project](assets/07.webp)


- In deze map maak je een eerste YAML-bestand met de naam `project.yml`:

![project](assets/08.webp)


- Vul dit bestand met informatie over je bedrijf met behulp van deze sjabloon:


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


Hier staat wat je voor elke sleutel moet invullen:


- `name`: De naam van je bedrijf (verplicht);
- `address` : De locatie van je bedrijf (optioneel);
- `language`: de landen waarin je bedrijf actief is of de talen die worden ondersteund (optioneel);
- `links` : De verschillende officiële links van je bedrijf (optioneel);
- `tags` : 2 termen die je bedrijf kwalificeren (verplicht);
- `category` : De categorie die het best het gebied beschrijft waarin je bedrijf actief is uit de volgende keuzes:
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
  - `neuws`,
  - `manufacturer`.


Je YAML-bestand zou er bijvoorbeeld zo uit kunnen zien:


```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3:

language:
- fr
- en

links:
website: https://bitcoin-baguette.com
twitter: https://twitter.com/bitcoinbaguette
Github:
youtube:
nostr:

tags:
- bitcoin
- education

category: education
```


![project](assets/09.webp)


- Als je klaar bent met het maken van wijzigingen in dit bestand, sla ze dan op door te klikken op de knop `Commit changes...` (Wijzigingen vastleggen...):
![project](assets/10.webp)


- Voeg een titel toe voor je wijzigingen, samen met een korte beschrijving:
![project](assets/11.webp)


- Klik op de groene knop `Propose changes` (Wijzigingen voorstellen):
![project](assets/12.webp)


- Je komt dan op een pagina met een overzicht van al je wijzigingen:
![project](assets/13.webp)


- Klik op je GitHub profielfoto rechtsboven, dan op `Your Repositories`:
![project](assets/14.webp)


- Selecteer je fork van de Plan ₿ Academy repository:
![project](assets/15.webp)


- Je zou een melding bovenaan het venster moeten zien met je nieuwe branch. Het heet waarschijnlijk `patch-1`. Klik erop:
![project](assets/16.webp)


- Je bent nu op je working branch (**zorg ervoor dat je op dezelfde branch zit als je vorige wijzigingen, dit is belangrijk!**):
![project](assets/17.webp)


- Ga terug naar de map `resources/projects/` en selecteer de map van je bedrijf die je zojuist in de vorige commit hebt gemaakt:
![project](assets/18.webp)


- Klik in de map van je bedrijf op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):
![project](assets/19.webp)


- Geef deze nieuwe map de naam `assets` en bevestig de aanmaak door een schuine streep `/` aan het einde te plaatsen:
![project](assets/20.webp)


- Maak in deze `assets` map een bestand aan met de naam `.gitkeep`:
![project](assets/21.webp)


- Klik op de knop `Commit changes...` (Wijzigingen vastleggen...):
![project](assets/22.webp)


- Laat de commit titel als standaard staan, en zorg ervoor dat het `Commit directly to the patch-1 branch` vakje aangevinkt is, klik dan op `Commit changes`:
![project](assets/23.webp)

- Ga terug naar de map `assets`:
![project](assets/24.webp)


- Klik op de knop `Add file` (Bestand toevoegen) en vervolgens op `Upload files` (Bestanden uploaden):
![project](assets/25.webp)


- Er wordt een nieuwe pagina geopend. Sleep een afbeelding van je bedrijf of je software naar het gebied. Deze afbeelding wordt weergegeven op de Plan ₿ Academy site:
![project](assets/26.webp)


- Het kan het logo of een pictogram zijn:
![project](assets/27.webp)


- Zodra de image geüpload is, controleer dan of het `Commit directly to the patch-1 branch` vakje aangevinkt is en klik dan op `Commit changes`:
![project](assets/28.webp)


- Let op, je afbeelding moet vierkant zijn, moet `logo` heten en moet het formaat `.webp` hebben. De volledige bestandsnaam moet daarom zijn: `logo.webp`:
![project](assets/29.webp)


- Ga terug naar je `assets` map en klik op het `.gitkeep` tussenliggende bestand:
![project](assets/30.webp)


- Klik op de drie kleine puntjes rechtsboven in het bestand en vervolgens op `Delete file` (Bestand verwijderen):
![project](assets/31.webp)


- Controleer of je nog steeds op dezelfde branch zit en klik dan op de knop `Commit changes` (Wijzigingen vastleggen):
![project](assets/32.webp)


- Voeg een titel en een beschrijving toe aan je commit en klik dan op `Commit changes` (Wijzigingen vastleggen):
![project](assets/33.webp)


- Ga terug naar de map van je bedrijf:
![project](assets/34.webp)


- Klik op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):
![project](assets/35.webp)


- Maak een nieuw YAML-bestand aan door het de naam te geven met de indicator van je moedertaal. Dit bestand wordt gebruikt voor de beschrijving van het project. Bijvoorbeeld, als ik mijn beschrijving in het Engels wil schrijven, dan noem ik dit bestand `en.yml`:
![project](assets/36.webp)


- Vul dit YAML-bestand in met behulp van deze sjabloon:

```yaml
description: |

contributors:
-
```



- Voor de `contributors` sleutel kun je je Plan ₿ Academy contributor identifier toevoegen als je die hebt. Als je die niet hebt, laat dit veld dan leeg.
- Voor de `description` sleutel moet je gewoon een korte paragraaf toevoegen die je bedrijf of je software beschrijft. De beschrijving moet in dezelfde taal zijn als de bestandsnaam. Je hoeft deze beschrijving niet te vertalen in alle talen die worden ondersteund op de site, omdat de PlanB teams dit zullen doen met behulp van hun model. Zo zou je bestand er bijvoorbeeld uit kunnen zien:

```yaml
description: |
Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.

contributors:
-
```

![project](assets/37.webp)


- Klik op de knop `Commit changes` (Wijzigingen vastleggen):
![project](assets/38.webp)


- Zorg ervoor dat het vakje `Commit directly to the patch-1 branch` aangevinkt is, voeg een titel toe en klik dan op `Commit changes` (Wijzigingen vastleggen):
![project](assets/39.webp)


- Je bedrijfsmap zou er nu zo uit moeten zien:
![project](assets/40.webp)


- Als alles naar wens is, keer dan terug naar de root van je fork:
![project](assets/41.webp)


- Je zou een bericht moeten zien dat aangeeft dat je branch wijzigingen heeft ondergaan. Klik op de knop `Compare & pull request` (Vergelijk & pull verzoek):
![project](assets/42.webp)


- Voeg een duidelijke titel en beschrijving toe aan je PR:
![project](assets/43.webp)


- Klik op de knop `Create pull request`:
![project](assets/44.webp)
Gefeliciteerd! Je PR is succesvol aangemaakt. Een beheerder zal het nu beoordelen en, als alles in orde is, integreren in de hoofdrepository van Plan ₿ Academy. Je zou je projectprofiel een paar dagen later op de website moeten zien verschijnen.


Zorg ervoor dat je de voortgang van je PR volgt. Een beheerder kan een opmerking achterlaten waarin om aanvullende informatie wordt gevraagd. Zolang je PR niet gevalideerd is, kun je het raadplegen in de `Pull requests` tab op de Plan ₿ Academy GitHub repository:

![project](assets/45.webp)

Hartelijk dank voor je waardevolle bijdrage! :)
