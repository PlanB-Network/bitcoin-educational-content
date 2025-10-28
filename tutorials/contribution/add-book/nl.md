---
name: Een boek toevoegen aan PlanB Network
description: Hoe voeg ik een nieuw boek toe aan PlanB Network?
---
![book](assets/cover.webp)


De missie van PlanB is om eersteklas educatieve bronnen aan te bieden over Bitcoin in zoveel mogelijk talen. Alle inhoud die op de site wordt gepubliceerd is open-source en wordt gehost op GitHub, zodat iedereen kan bijdragen aan de verrijking van het platform.


**Wil je een boek gerelateerd aan Bitcoin toevoegen op de PlanB Network site en de zichtbaarheid van je werk vergroten, maar weet je niet hoe? Dan is deze tutorial voor jou!**

![book](assets/01.webp)


- Eerst moet je een GitHub account hebben. Als je niet weet hoe je een account aanmaakt, hebben we een gedetailleerde tutorial gemaakt om je te begeleiden.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Ga naar [de GitHub repository van PlanB gewijd aan data](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/books) in de `resources/books/` sectie:

![book](assets/02.webp)


- Klik rechtsboven op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):

![book](assets/03.webp)


- Als je nog nooit hebt bijgedragen aan de inhoud van PlanB Network, zul je een fork van de originele repository moeten maken. Een repository forken betekent dat je een kopie van die repository maakt op je eigen GitHub account, zodat je aan het project kunt werken zonder de originele repository te beïnvloeden. Klik op de knop `Fork this repository`:

![book](assets/04.webp)


- Je komt dan op de GitHub bewerkingspagina:

![book](assets/05.webp)


- Maak een map voor je boek. Om dit te doen, schrijf je in het vak `Name your file...` (Geef je bestand een naam...) de naam van je boek in kleine letters met streepjes in plaats van spaties. Als je boek bijvoorbeeld "*My Bitcoin Book*" heet, dan moet je `my-bitcoin-book` noteren:

![book](assets/06.webp)


- Om het aanmaken van de map te valideren, voeg je gewoon een schuine streep toe na je boeknaam in hetzelfde vak, bijvoorbeeld: `my-bitcoin-book/`. Door een schuine streep toe te voegen, wordt automatisch een map aangemaakt in plaats van een bestand:

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


- `author`: Geef de naam van de auteur van het boek aan.
- `level`: Geef het vereiste niveau aan om het boek goed te kunnen lezen en begrijpen. Kies een van de volgende niveaus:
  - `beginner`
  - `intermediate`
  - `advanced`
  - `expert`
- `tags`: Voeg twee of drie tags toe die betrekking hebben op je boek. Bijvoorbeeld:
    - `bitcoin`
    - `history`
    - `technology`
    - `economy`
    - `education`...


Je YAML-bestand zou er bijvoorbeeld zo uit kunnen zien:


```yaml
author: Loïc Morel
level: beginner
tags:
- bitcoin
- technology
```


![book](assets/09.webp)


- Als je klaar bent met het maken van wijzigingen in dit bestand, sla ze dan op door te klikken op de knop `Commit changes...` (Wijzigingen vastleggen...):
![book](assets/10.webp)


- Voeg een titel toe voor je wijzigingen, evenals een korte beschrijving:
![book](assets/11.webp)


- Klik op de groene knop `Propose changes` (Wijzigingen voorstellen):
![book](assets/12.webp)


- Je komt dan op een pagina met een overzicht van al je wijzigingen:
![book](assets/13.webp)


- Klik op je GitHub profielfoto rechtsboven, dan op `Your Repositories`:
![book](assets/14.webp)


- Selecteer je fork van de PlanB Network repository:
![book](assets/15.webp)


- Je zou een melding bovenaan het venster moeten zien met je nieuwe branch. Het heet waarschijnlijk `patch-1`. Klik erop:
![book](assets/16.webp)


- Je bent nu op je eigen werk branch:
![book](assets/17.webp)


- Ga terug naar de map `resources/books/` en selecteer de map van je boek die je zojuist in de vorige commit hebt gemaakt:
![book](assets/18.webp)


- Klik in de map van je boek op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):
![book](assets/19.webp)


- Geef deze nieuwe map de naam `assets` en bevestig de aanmaak door een schuine streep `/` aan het einde te plaatsen:
![book](assets/20.webp)


- Maak in deze `assets` map een bestand aan met de naam `.gitkeep`:
![book](assets/21.webp)


- Klik op de knop `Commit changes...` (Wijzigingen vastleggen...):
![book](assets/22.webp)


- Laat de commit titel als standaard staan, en zorg ervoor dat het `Commit directly to the patch-1 branch` vakje aangevinkt is, klik dan op `Commit changes` (Wijzigingen committen):
![book](assets/23.webp)


- Ga terug naar de map `assets`:
![book](assets/24.webp)


- Klik op de knop `Add file` (Bestand toevoegen) en vervolgens op `Upload files` (Bestanden uploaden):
![book](assets/25.webp)


- Er wordt een nieuwe pagina geopend. Sleep de omslagafbeelding van je boek naar het gebied. Deze afbeelding wordt weergegeven op de PlanB Network site:
![book](assets/26.webp)


- Let op, de afbeelding moet het formaat van een boek hebben, zodat deze het beste past op onze website, zoals bijvoorbeeld:
![book](assets/27.webp)


- Zodra de afbeelding is geüpload, zorg er dan voor dat het `Commit directly to the patch-1 branch` vakje is aangevinkt, klik dan op `Commit changes`:
![book](assets/28.webp)

- Let op, je afbeelding moet `cover_en` heten als de omslag in het Engels is en moet het `.webp`-formaat hebben. Daardoor moet de volledige bestandsnaam `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, enzovoort zijn. Als je een andere omslagafbeelding wilt gebruiken voor elke taal, bijvoorbeeld in het geval van een boekvertaling, kun je ze op dezelfde locatie in de `assets` map plaatsen:
![book](assets/29.webp)


- Ga terug naar je `assets` map en klik op het `.gitkeep` tussenbestand:
![book](assets/30.webp)


- Klik op de 3 kleine puntjes rechtsboven in het bestand en vervolgens op `Delete file` (Bestand verwijderen):
![book](assets/31.webp)


- Zorg ervoor dat je nog steeds op dezelfde branch zit en klik dan op de knop `Commit changes...` (Wijzigingen vastleggen...):
![book](assets/32.webp)


- Voeg een titel en beschrijving toe aan je commit en klik dan op `Commit changes` (Wijzigingen vastleggen):
![book](assets/33.webp)


- Ga terug naar de map van je boek:
![book](assets/34.webp)


- Klik op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):
![book](assets/35.webp)


- Maak een nieuw YAML-bestand aan met de naam van de taalindicator van het boek. Dit bestand wordt gebruikt voor de beschrijving van het boek. Als ik mijn beschrijving bijvoorbeeld in het Engels wil schrijven, geef ik dit bestand de naam `en.yml`:
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


- `title`: Geef de naam van het boek aan tussen aanhalingstekens.
- `publication_year`: Geef het jaar aan waarin het boek is gepubliceerd.
- `cover`: Geef de naam op van het bestand dat overeenkomt met de coverafbeelding, in overeenstemming met de taal van het YAML-bestand dat je momenteel bewerkt. Als je bijvoorbeeld het `en.yml` bestand aan het bewerken bent en je hebt eerder de Engelse cover image toegevoegd met de titel `cover_en.webp`, geef dan simpelweg `cover_en.webp` aan in dit veld.
- `description`: Voeg een korte paragraaf toe die het boek beschrijft. De beschrijving moet in dezelfde taal zijn als aangegeven in de titel van het YAML-bestand.
- `contributors`: Voeg je medewerkers-ID toe als je er een hebt.


Je YAML-bestand zou er bijvoorbeeld zo uit kunnen zien:


```yaml
title: "My Bitcoin Book"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
Discover the groundbreaking world of Bitcoin with this comprehensive guide tailored for beginners. My Bitcoin Book demystifies the complexities of Bitcoin, providing a clear and concise introduction to how the protocol works. From its revolutionary technology to its potential impact on the global economy, this book offers invaluable insights and practical knowledge. Perfect for those new to Bitcoin, it covers the basics, security tips, and the future of digital finance. Dive into the future of money and empower yourself with the knowledge to navigate the digital age confidently.

contributors:
  - pretty-private

![book](assets/37.webp)
- Click on the `Commit changes...` button:
![book](assets/38.webp)
- Ensure the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![book](assets/39.webp)
- The book folder should now look like this:
![book](assets/40.webp)
- If everything looks good to you, return to the root of your fork:
![book](assets/41.webp)
- You should see a message indicating that your branch has been modified. Click on the `Compare & pull request` button:
![book](assets/42.webp)
- Add a clear title and a description to your PR:
![book](assets/43.webp)
- Click on the `Create pull request` button:
![book](assets/44.webp)
Congratulations! Your PR has been successfully created. An administrator will now review it and, if everything is in order, merge it into the main repository of the PlanB Network. You should see your book appear on the website a few days later.

Be sure to follow the progress of your PR. An administrator may leave a comment asking for additional information. As long as your PR is not validated, you can view it in the `Pull requests` tab on the PlanB Network's GitHub repository:
![book](assets/45.webp)
Thank you very much for your valuable contribution! :)
```
