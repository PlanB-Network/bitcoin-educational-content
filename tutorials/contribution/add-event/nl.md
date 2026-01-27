---
name: Een evenement toevoegen op Plan ₿ Academy
description: Hoe stel ik voor om een nieuw evenement toe te voegen op Plan ₿ Academy?
---
![event](assets/cover.webp)


De missie van PlanB is om eersteklas educatieve bronnen aan te bieden over Bitcoin in zoveel mogelijk talen. Alle inhoud die op de site wordt gepubliceerd is open-source en wordt gehost op GitHub, waardoor iedereen de kans krijgt om bij te dragen aan de verrijking van het platform.


Wil je een Bitcoin conferentie toevoegen aan de Plan ₿ Academy site en de zichtbaarheid van je evenement vergroten, maar weet je niet hoe? Dan is deze tutorial voor jou!

![event](assets/01.webp)


- Eerst moet je een account hebben op GitHub. Als je niet weet hoe je een account aanmaakt, hebben we een gedetailleerde tutorial gemaakt om je te begeleiden.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Ga naar [de GitHub repository van PlanB gewijd aan data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) in de `resources/conference/` sectie:

![event](assets/02.webp)


- Klik rechtsboven op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):
![event](assets/03.webp)


- Als je nog nooit hebt bijgedragen aan de inhoud van Plan ₿ Academy, zul je een fork van de originele repository moeten maken. Een repository forken betekent dat je een kopie van die repository maakt op je eigen GitHub account, zodat je aan het project kunt werken zonder de originele repository te beïnvloeden. Klik op de knop `Fork this repository`:
![event](assets/04.webp)


- Je komt dan op de GitHub bewerkingspagina:
![event](assets/05.webp)


- Maak een map aan voor je conferentie. Om dit te doen, schrijf je in het vak `Name your file...` (Naam van je bestand...) de naam van je conferentie in kleine letters met streepjes in plaats van spaties. Als je conferentie bijvoorbeeld "Paris Bitcoin Conference" heet, moet je `paris-Bitcoin-conference` noteren. Voeg ook het jaar van je conferentie toe, bijvoorbeeld: `paris-Bitcoin-conference-2024`:
![event](assets/06.webp)


- Om het aanmaken van de map te valideren, noteer je gewoon een schuine streep na je naam in hetzelfde vak, bijvoorbeeld: `paris-Bitcoin-conference-2024/`. Door een schuine streep toe te voegen wordt automatisch een map aangemaakt in plaats van een bestand:
![event](assets/07.webp)


- In deze map maak je een eerste YAML-bestand met de naam `events.yml`:
![event](assets/08.webp)


- Vul dit bestand met informatie over je conferentie met behulp van deze sjabloon:


```yaml
start_date:
end_date:
address_line_1:
address_line_2:
address_line_3:
name:
project:
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


Je YAML-bestand zou er bijvoorbeeld zo uit kunnen zien:


```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2:
address_line_3:
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants each year!
language:
- fr
- en
- es
- it
links:
website: https://paris.bitcoin.fr/conference
replay_url:
live_url :
tags:
- Bitcoiner
- General
- International
```

![event](assets/09.webp)

Als je nog geen "*project*" identifier hebt voor je organisatie, kun je die toevoegen door deze andere tutorial te volgen.


https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- Als je klaar bent met het maken van wijzigingen in dit bestand, sla ze dan op door te klikken op de knop `Commit changes...` (Wijzigingen vastleggen...):
![event](assets/10.webp)


- Voeg een titel toe voor je wijzigingen, evenals een korte beschrijving:
![event](assets/11.webp)


- Klik op de groene knop `Propose changes` (Wijzigingen voorstellen):
![event](assets/12.webp)


- Je komt dan op een pagina met een overzicht van al je wijzigingen:
![event](assets/13.webp)


- Klik op je GitHub profielfoto rechtsboven, dan op `Your Repositories`:
![event](assets/14.webp)


- Selecteer je fork van de Plan ₿ Academy repository:
![event](assets/15.webp)


- Je zou een melding bovenaan het venster moeten zien met je nieuwe branch. Het heet waarschijnlijk `patch-1`. Klik erop:
![event](assets/16.webp)


- Je bent nu op je branch:
![event](assets/17.webp)


- Ga terug naar de `resources/conference/` map en selecteer de map van je conferentie die je zojuist in de vorige commit hebt aangemaakt:
![event](assets/18.webp)


- Klik in de map van je conferentie op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):
![event](assets/19.webp)


- Geef deze nieuwe map de naam `assets` en bevestig de aanmaak door een schuine streep `/` aan het einde te plaatsen:
![event](assets/20.webp)


- Maak in deze `assets` map een bestand aan met de naam `.gitkeep`:
![event](assets/21.webp)


- Klik op de knop `Commit changes...` (Wijzigingen vastleggen...):
![event](assets/22.webp)


- Laat de commit titel als standaard staan, en zorg ervoor dat het `Commit directly to the patch-1 branch` vakje aangevinkt is, klik dan op `Commit changes` (Wijzigingen vastleggen):
![event](assets/23.webp)


- Ga terug naar de map `assets`:
![event](assets/24.webp)


- Klik op de knop `Add file` (Bestand toevoegen) en vervolgens op `Upload files` (Bestanden uploaden):
![event](assets/25.webp)

- Er wordt een nieuwe pagina geopend. Sleep een afbeelding die je conferentie voorstelt en die zal worden weergegeven op de Plan ₿ Academy site:
![event](assets/26.webp)


- Het kan het logo, een miniatuur of zelfs een poster zijn:
![event](assets/27.webp)


- Zodra de afbeelding is geüpload, controleer dan of het `Commit directly to the patch-1 branch` vakje is aangevinkt, klik dan op `Commit changes` (Wijzigingen vastleggen):

![event](assets/28.webp)


- Let op, je afbeelding moet `thumbnail` heten en het formaat `.webp` hebben. De volledige bestandsnaam moet daarom zijn: `thumbnail.webp`:
![event](assets/29.webp)


- Ga terug naar je `assets` map en klik op het tussenliggende bestand `.gitkeep`:
![event](assets/30.webp)


- Klik op de 3 kleine puntjes rechtsboven in het bestand en vervolgens op `Delete file` (Bestand verwijderen):
![event](assets/31.webp)


- Controleer of je nog steeds op dezelfde branch zit en klik dan op de knop `Commit changes` (Wijzigingen vastleggen):
![event](assets/32.webp)


- Voeg een titel en een beschrijving toe aan je commit en klik dan op `Commit changes` (Wijzigingen vastleggen):
![event](assets/33.webp)


- Ga terug naar de root van je repository:
![event](assets/34.webp)


- Je zou een bericht moeten zien dat aangeeft dat je branch wijzigingen heeft ondergaan. Klik op de knop  `Compare & pull request` (Vergelijk & pull verzoek):
![event](assets/35.webp)


- Voeg een duidelijke titel en beschrijving toe aan je PR:
![event](assets/36.webp)


- Klik op de knop `Create pull request`:
![event](assets/37.webp)

Gefeliciteerd! Je PR is succesvol aangemaakt. Een beheerder zal het nu controleren en, als alles in orde is, samenvoegen in de hoofdrepository van Plan ₿ Academy. Je zou je evenement een paar dagen later op de website moeten zien verschijnen.


Zorg ervoor dat je de voortgang van je PR volgt. Een beheerder kan een opmerking achterlaten waarin om aanvullende informatie wordt gevraagd. Zolang je PR niet gevalideerd is, kun je het raadplegen in de `Pull requests` tab op de Plan ₿ Academy GitHub repository:
![event](assets/38.webp)

Hartelijk dank voor je waardevolle bijdrage! :)
