---
name: Een boek toevoegen aan PlanB Network
description: Hoe voeg ik een nieuw boek toe aan PlanB Network?
---
![book](assets/cover.webp)


De missie van PlanB is om eersteklas educatieve bronnen aan te bieden op Bitcoin in zoveel mogelijk talen. Alle inhoud die op de site wordt gepubliceerd is open-source en wordt gehost op GitHub, zodat iedereen kan bijdragen aan de verrijking van het platform.


**Wil je een boek gerelateerd aan Bitcoin toevoegen op de PlanB Network site en de zichtbaarheid van je werk vergroten, maar weet je niet hoe? Deze tutorial is voor jou!**

![book](assets/01.webp)


- Eerst moet je een GitHub account hebben. Als je niet weet hoe je een account aanmaakt, hebben we een gedetailleerde tutorial gemaakt om je te begeleiden.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Ga naar [de GitHub repository van PlanB gewijd aan data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/books) in de `resources/bookss/` sectie:

![book](assets/02.webp)


- Klik rechtsboven op de knop `Bestand toevoegen` en vervolgens op `Nieuw bestand maken`:

![book](assets/03.webp)


- Als je nog nooit hebt bijgedragen aan de inhoud van PlanB Network, zul je een Fork van het originele repository moeten maken. Een repository forken betekent dat je een kopie van die repository maakt op je eigen GitHub account, zodat je aan het project kunt werken zonder de originele repository te beïnvloeden. Klik op de `Fork this repository` knop:

![book](assets/04.webp)


- Je komt dan op de GitHub bewerkingspagina:

![book](assets/05.webp)


- Maak een map voor je boek. Om dit te doen, schrijf je in het vak `Naam je bestand...` de naam van je boek in kleine letters met streepjes in plaats van spaties. Als je boek bijvoorbeeld "*Mijn Bitcoin-boek*" heet, moet je `mijn Bitcoin-boek` noteren:

![book](assets/06.webp)


- Om het aanmaken van de map te valideren, voeg je gewoon een schuine streep toe na je boeknaam in hetzelfde vak, bijvoorbeeld: `mijn-Bitcoin-boek/`. Door een schuine streep toe te voegen, wordt automatisch een map aangemaakt in plaats van een bestand:

![book](assets/07.webp)


- In deze map maak je een eerste YAML-bestand met de naam `book.yml`:

![book](assets/08.webp)


- Vul dit bestand met informatie over je boek met behulp van deze sjabloon:


```yaml
author:
level:
tags:
-
-
```


Hier zijn de gegevens die je voor elk veld moet invullen:


- `auteur`**: Geef de naam van de auteur van het boek aan.
- niveau`**: Geef het vereiste niveau aan om het boek goed te kunnen lezen en begrijpen. Kies een van de volgende niveaus:
 - beginner
 - gemiddeld
- `gevorderd` - `expert`
- `tags`**: Voeg twee of drie tags toe die betrekking hebben op je boek. Bijvoorbeeld:
    - gW-6
    - `geschiedenis`
    - `technologie`
    - economie
    - `onderwijs`...


Je YAML-bestand zou er bijvoorbeeld zo uit kunnen zien:


```yaml
author: Loïc Morel
level: beginner
tags:
- bitcoin
- technology
```


![book](assets/09.webp)


- Als je klaar bent met het maken van wijzigingen in dit bestand, sla ze dan op door te klikken op de knop `Wijzigingen vastleggen...`:

![book](assets/10.webp)


- Voeg een titel toe voor je wijzigingen, evenals een korte beschrijving:

![book](assets/11.webp)


- Klik op de Green `Wijzigingen voorstellen` knop:

![book](assets/12.webp)


- Je komt dan op een pagina met een overzicht van al je wijzigingen:

![book](assets/13.webp)


- Klik op je GitHub profielfoto rechtsboven, dan op `Your Repositories`:

![book](assets/14.webp)


- Selecteer je Fork van de PlanB Network repository:

![book](assets/15.webp)


- Je zou een melding bovenaan het venster moeten zien met je nieuwe branch. Het heet waarschijnlijk `patch-1`. Klik erop:

![book](assets/16.webp)


- Je bent nu op je werktak:

![book](assets/17.webp)


- Ga terug naar de map `resources/bookss/` en selecteer de map van je boek die je zojuist in de vorige vastlegging hebt gemaakt:

![book](assets/18.webp)


- Klik in de map van je boek op de knop `Bestand toevoegen` en vervolgens op `Nieuw bestand maken`:

![book](assets/19.webp)


- Geef deze nieuwe map de naam `assets` en bevestig de aanmaak door een schuine streep `/` aan het einde te plaatsen:

![book](assets/20.webp)


- Maak in deze `assets` map een bestand aan met de naam `.gitkeep`:

![book](assets/21.webp)


- Klik op de knop `Wijzigingen vastleggen...`:

![book](assets/22.webp)


- Laat de commit titel als standaard staan, en zorg ervoor dat het `Direct naar de patch-1 tak committen` vakje aangevinkt is, klik dan op `Wijzigingen committen`:

![book](assets/23.webp)


- Ga terug naar de map `assets`:

![book](assets/24.webp)


- Klik op de knop `Bestand toevoegen` en vervolgens op `Bestanden uploaden`:

![book](assets/25.webp)


- Er wordt een nieuwe pagina geopend. Sleep de omslagafbeelding van je boek naar het gebied. Deze afbeelding wordt weergegeven op de PlanB Network site:

![book](assets/26.webp)


- Let op, de afbeelding moet het formaat van een boek hebben, zodat deze het beste past op onze website, zoals bijvoorbeeld:

![book](assets/27.webp)


- Zodra de afbeelding is geüpload, zorg er dan voor dat het `Direct committen naar de patch-1 tak` vakje is aangevinkt, klik dan op `Commit changes`:

![book](assets/28.webp)- Please note, your image must be named `cover_en` if the cover is in English and must be in `.webp` format. Therefore, the complete file name should be `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, etc. If you wish to use a different cover image for each language, for example in the case of a book translation, you can place them in the same location in the `assets` folder:

![book](assets/29.webp)


- Ga terug naar je `assets` map en klik op het `.gitkeep` tussenbestand:

![book](assets/30.webp)


- Klik op de 3 kleine puntjes rechtsboven in het bestand en vervolgens op `Bestand verwijderen`:

![book](assets/31.webp)


- Zorg ervoor dat je nog steeds op dezelfde branch zit en klik dan op de `Wijzigingen vastleggen...` knop:

![book](assets/32.webp)


- Voeg een titel en beschrijving toe aan je vastlegging en klik dan op `Wijzigingen vastleggen`:

![book](assets/33.webp)


- Ga terug naar de map van je boek:

![book](assets/34.webp)


- Klik op de knop `Bestand toevoegen` en vervolgens op `Nieuw bestand maken`:

![book](assets/35.webp)


- Maak een nieuw YAML-bestand met de naam van de taalindicator van het boek. Dit bestand wordt gebruikt voor de beschrijving van het boek. Als ik mijn beschrijving bijvoorbeeld in het Engels wil schrijven, geef ik dit bestand de naam `en.yml`:

![book](assets/36.webp)


- Vul dit YAML-bestand in met behulp van deze sjabloon:

```yaml
title: ""
publication_year:
cover: cover_en.webp
original: true
description: |

contributors:
-
```


Hier zijn de gegevens die je voor elk veld moet invullen:


- `titel`**: Geef de naam van het boek aan tussen aanhalingstekens.
- `publicatie_jaar`**: Geef het jaar aan waarin het boek is gepubliceerd.
- `cover`**: Geef de naam op van het bestand dat overeenkomt met de coverafbeelding, in overeenstemming met de taal van het YAML-bestand dat u momenteel bewerkt. Als je bijvoorbeeld het `en.yml` bestand aan het bewerken bent en je hebt eerder de Engelse cover image toegevoegd met de titel `cover_en.webp`, geef dan simpelweg `cover_en.webp` aan in dit veld.
- `description`**: Voeg een korte paragraaf toe die het boek beschrijft. De beschrijving moet in dezelfde taal zijn als aangegeven in de titel van het YAML-bestand.
- `contributors`**: Voeg uw medewerkers-ID toe als u er een hebt.


Je YAML-bestand zou er bijvoorbeeld zo uit kunnen zien:


```yaml