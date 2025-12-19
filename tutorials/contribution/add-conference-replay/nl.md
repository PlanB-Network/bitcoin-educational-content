---
name: Een conferentie replay toevoegen
description: Hoe voeg ik een conferentie replay toe op Plan ₿ Academy?
---
![conference](assets/cover.webp)


De missie van PlanB is om eersteklas educatieve bronnen aan te bieden over Bitcoin in zoveel mogelijk talen. Alle inhoud die op de site wordt gepubliceerd is open-source en wordt gehost op GitHub, zodat iedereen kan bijdragen aan de verrijking van het platform.


Wil je de replay van je Bitcoin conferentie toevoegen op de Plan ₿ Academy site en zichtbaarheid geven aan dit evenement, maar weet je niet hoe? Dan is deze tutorial voor jou!


Als je echter een conferentie wilt toevoegen die in de toekomst zal plaatsvinden, raad ik je aan deze andere tutorial te lezen waarin we uitleggen hoe je een nieuw evenement toevoegt aan de site.


https://planb.academy/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- Eerst moet je een account hebben op GitHub. Als je niet weet hoe je een account aanmaakt, hebben we een gedetailleerde tutorial gemaakt om je te begeleiden.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Ga naar [de GitHub repository van PlanB gewijd aan data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/conference) in de `resources/conference/` sectie:

![conference](assets/02.webp)


- Klik rechtsboven op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):
![conference](assets/03.webp)


- Als je nog nooit hebt bijgedragen aan de inhoud van Plan ₿ Academy, zul je een fork van de originele repository moeten maken. Een repository forken betekent dat je een kopie van die repository maakt op je eigen GitHub account, waarmee je aan het project kunt werken zonder de originele repository te beïnvloeden. Klik op de kno `Fork this repository`:
![conference](assets/04.webp)


- Je komt dan op de GitHub bewerkingspagina:
![conference](assets/05.webp)


- Maak een map aan voor je conferentie. Om dit te doen, schrijf je in het vak `Name your file...' (Naam van je bestand...` de naam van je conferentie in kleine letters met streepjes in plaats van spaties. Als je conferentie bijvoorbeeld "Paris Bitcoin Conference" heet, moet je `paris-Bitcoin-conference` noteren. Voeg ook het jaar van je conferentie toe, bijvoorbeeld: `paris-Bitcoin-conference-2024`:
![conference](assets/06.webp)


- Om het aanmaken van de map te valideren, noteer je gewoon een schuine streep na je naam in hetzelfde vak, bijvoorbeeld: `paris-Bitcoin-conference-2024/`. Door een schuine streep toe te voegen wordt automatisch een map aangemaakt in plaats van een bestand:
![conference](assets/07.webp)


- In deze map maak je een eerste YAML bestand met de naam `conference.yml`:
![conference](assets/08.webp)

Vul dit bestand met informatie over je conferentie met behulp van deze sjabloon:

```yaml
year:
name:
project:
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


Je YAML-bestand zou er bijvoorbeeld zo uit kunnen zien:


```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
location: Paris, France
language:
- fr
- en
links:
website: https://paris.bitcoin.fr/conference
twitter: https://twitter.com/ParisBitcoinConference
tags:
- International
- All Public
```


![conference](assets/09.webp)


Als je nog geen "*project*" identifier hebt voor je organisatie, kun je die toevoegen door deze andere tutorial te volgen.


https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- Als je klaar bent met het maken van wijzigingen in dit bestand, sla ze dan op door te klikken op de knop `Commit changes...` (Wijzigingen vastleggen):
![conference](assets/10.webp)


- Voeg een titel toe voor je wijzigingen, evenals een korte beschrijving:
![conference](assets/11.webp)


- Klik op de groene knop `Propose changes` (Wijzigingen voorstellen):
![conference](assets/12.webp)


- Je komt dan op een pagina met een overzicht van al je wijzigingen:
![conference](assets/13.webp)


- Klik op je GitHub profielfoto rechtsboven, dan op `Your Repositories`:
![conference](assets/14.webp)


- Selecteer je fork van de Plan ₿ Academy repository:
![conference](assets/15.webp)


- Je zou een melding bovenaan het venster moeten zien met je nieuwe branch. Het heet waarschijnlijk `patch-1`. Klik erop:
![conference](assets/16.webp)


- Je bent nu op je branch:
![conference](assets/17.webp)


- Ga terug naar de map `resources/conference/` en selecteer de map van je conferentie die je zojuist hebt aangemaakt bij de vorige commit:
![conference](assets/18.webp)


- Klik in de map van je conferentie op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):
![conference](assets/19.webp)


- Geef deze nieuwe map de naam `assets` en bevestig de aanmaak door een schuine streep `/` aan het einde te plaatsen:
![conference](assets/20.webp)


- Maak in deze `assets` map een bestand aan met de naam `.gitkeep`:
![conference](assets/21.webp)


- Klik op de knop `Commit changes...` (Wijzigingen vastleggen...):
![conference](assets/22.webp)


- Laat de commit titel als standaard staan, en zorg ervoor dat het `Commit directly to the patch-1 branch` vakje aangevinkt is, klik dan op `Commit changes` (Wijzigingen committen):
![conference](assets/23.webp)


- Ga terug naar de map `assets`:
![conference](assets/24.webp)


- Klik op de knop `Add file` (Bestand toevoegen) en vervolgens op `Upload files` (Bestanden uploaden):
![conference](assets/25.webp)


- Er wordt een nieuwe pagina geopend. Sleep een afbeelding die je conferentie voorstelt en die zal worden weergegeven op de Plan ₿ Academy site:
![conference](assets/26.webp)

- Het kan een logo, een miniatuur of zelfs een poster zijn:
![conference](assets/27.webp)


- Zodra de afbeelding is geüpload, controleer dan of het vakje `Commit directly to the patch-1 branch` is aangevinkt en klik dan op `Commit changes` (Wijzigingen vastleggen):
![conference](assets/28.webp)


- Let op, je afbeelding moet `thumbnail` heten en het formaat `.webp` hebben. De volledige bestandsnaam moet daarom zijn: `thumbnail.webp`:
![conference](assets/29.webp)


- Ga terug naar je `assets` map en klik op het `.gitkeep` tussenbestand:
![conference](assets/30.webp)


- Klik in het bestand op de 3 kleine puntjes in de rechterbovenhoek en vervolgens op `Delete file` (Bestand verwijderen):
![conference](assets/31.webp)


- Controleer of je nog steeds op dezelfde branch zit en klik dan op de knop `Commit changes` (Wijzigingen vastleggen):
![conference](assets/32.webp)


- Voeg een titel en een beschrijving toe aan je commit en klik dan op `Commit changes` (Wijzigingen vastleggen):
![conference](assets/33.webp)


- Ga terug naar je conferentiemap:
![conference](assets/34.webp)


- Klik op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):
![conference](assets/35.webp)


- Maak een nieuw markdown (.md) bestand aan door het een naam te geven met de indicator van je moedertaal. Dit bestand wordt gebruikt voor de herhalingen van je conferentie. Als ik bijvoorbeeld de beschrijvingen van de conferenties in het Engels wil schrijven, geef ik dit bestand de naam en.md:
![conference](assets/36.webp)


- Vul dit markdown-bestand in met behulp van dit sjabloon dat je kunt aanpassen aan de configuratie van je conferentie:


```markdown
---
name: Paris Bitcoin Conference 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
---

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```


![conference](assets/37.webp)


- Aan het begin van je document, in de "front matter", vul je het veld `name:` in met de naam van je conferentie en het jaar van de herhalingen. Schrijf in het `description:` veld een korte beschrijving van je evenement in de taal van het bestand. Bijvoorbeeld, voor een bestand met de naam `en.md`, moet de beschrijving in het Engels zijn. Het Plan ₿ Academy team zal je beschrijving vertalen met behulp van hun model.
- Titels van het eerste niveau, gemarkeerd met een `#`, worden gebruikt om de conferentie per scène in te delen. Bijvoorbeeld, `# Main Stage` voor het hoofdpodium en `# Workshop Room` voor een podium gewijd aan workshops.



- Titels van een tweede niveau, gemarkeerd met een dubbele `##`, worden gebruikt om de verschillende herhalingsvideo's van elkaar te scheiden. Als de conferenties continu gedurende een halve dag werden gefilmd, geef dan bijvoorbeeld `## vrijdagochtend` aan. Als de conferenties afzonderlijk zijn gefilmd en uitgezonden, benoem de conferentie dan direct met een titel op het tweede niveau.



- Voeg onder elke titel op het tweede niveau een link toe naar de bijbehorende herhalingsvideo. De syntaxis moet zijn: `![video](https://youtu.be/XXXXXXXXXXXX)`, waarbij `XXXXXXXXXX` wordt vervangen door de eigenlijke videolink.



- Als het formaat het toelaat (individuele conferenties), kun je de namen van de sprekers toevoegen. Voeg hiervoor het veld `speaker:` toe, gevolgd door de naam of het pseudoniem van de spreker onder de videolink. In het geval van meerdere sprekers, scheidt je elke naam met een komma, bijvoorbeeld: `Spreker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.


---


- Als je wijzigingen in dit bestand zijn voltooid, sla ze dan op door op de knop Commit changes... (Wijzigingen vastleggen...) te klikken:
![conference](assets/38.webp)


- Voeg een titel toe voor je wijzigingen, evenals een korte beschrijving:
![conference](assets/39.webp)


- Klik op `Commit changes` (Wijzigingen vastleggen):
![conference](assets/40.webp)


- Je conferentiemap zou er nu zo uit moeten zien:
![conference](assets/41.webp)


- Als alles naar wens is, keer dan terug naar de root van je fork:
![conference](assets/42.webp)


- Je zou een bericht moeten zien dat aangeeft dat je branch wijzigingen heeft ondergaan. Klik op de knop `Compare & pull request` (Vergelijk & pull verzoek):
![conference](assets/43.webp)


- Voeg een duidelijke titel en beschrijving toe voor je PR:
![conference](assets/44.webp)


- Klik op de knop `Compare & pull request` (Create pull request):
![conference](assets/45.webp)

Gefeliciteerd! Je PR is succesvol aangemaakt. Een beheerder zal het nu beoordelen en, als alles in orde is, samenvoegen in de hoofd repository van Plan ₿ Academy. Je zou de herhalingen van je conferentie een paar dagen later op de website moeten zien verschijnen.


Zorg ervoor dat je de voortgang van je PR volgt. Het is mogelijk dat een beheerder een opmerking achterlaat waarin om extra informatie wordt gevraagd. Zolang je PR niet gevalideerd is, kun je het bekijken onder de `Pull requests` tab op de GitHub repository van het Plan ₿ Academy:
![conference](assets/46.webp)


Hartelijk dank voor je waardevolle bijdrage! :)
