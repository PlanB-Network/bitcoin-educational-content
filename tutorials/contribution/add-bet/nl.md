---
name: Educatieve hulpmiddelen toevoegen
description: Hoe voeg je nieuw onderwijsmateriaal toe op Plan ₿ Academy?
---
![event](assets/cover.webp)


De missie van PlanB is om toonaangevende educatieve bronnen aan te bieden op Bitcoin, in zoveel mogelijk talen. Alle inhoud die op de site wordt gepubliceerd is open-source en wordt gehost op GitHub, waardoor iedereen kan deelnemen aan het verrijken van het platform.


Naast tutorials en training biedt Plan ₿ Academy ook een uitgebreide bibliotheek aan met gevarieerde educatieve inhoud over Bitcoin, toegankelijk voor iedereen, [in de "BET" (_Bitcoin Educational Toolkit_) sectie](https://planb.academy/resources/bet). Deze database bevat educatieve posters, memes, humoristische propagandaposters, technische diagrammen, logo's en andere hulpmiddelen voor gebruikers. Het doel van dit initiatief is om individuen en gemeenschappen die wereldwijd Bitcoin onderwijzen te ondersteunen door hen te voorzien van de nodige visuele middelen.


Wil je meewerken aan het verrijken van deze database, maar weet je niet hoe? Dan is deze tutorial voor jou!


*Het is noodzakelijk dat alle inhoud die in de site wordt geïntegreerd vrij is van rechten of de licentie van het bronbestand respecteert. Alle visuals gepubliceerd op Plan ₿ Academy zijn beschikbaar onder de [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) licentie.*

![event](assets/01.webp)


- Eerst moet je een account hebben op GitHub. Als je niet weet hoe je een account aanmaakt, hebben we een gedetailleerde tutorial gemaakt om je te begeleiden.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c




- Ga naar [de GitHub repository van PlanB gewijd aan gegevens](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/bet) in de `resources/bet/` sectie:

![event](assets/02.webp)


- Klik rechtsboven op de knop `Add file` (Bestand toevoegen) en vervolgens op `Create new file` (Nieuw bestand maken):

![event](assets/03.webp)


- Als je nog nooit hebt bijgedragen aan de inhoud van Plan ₿ Academy, zul je een fork van de originele repository moeten maken. Een repository forken betekent dat je een kopie van die repository maakt op je eigen GitHub account, waarmee je aan het project kunt werken zonder de originele repository te beïnvloeden. Klik op de knop `Fork this repository`:

![event](assets/04.webp)


- Je komt dan op de GitHub bewerkingspagina:

![event](assets/05.webp)


- Maak een map voor je inhoud. Om dit te doen, schrijf je in het vak `Name your file...` de naam van je inhoud in kleine letters met streepjes in plaats van spaties. Laten we in mijn voorbeeld zeggen dat ik een PDF-visual van de BIP39-lijst van 2048 woorden wil toevoegen. Dus noem ik mijn map `bip39-wordlist`: ![event](assets/06.webp)
- Om de aanmaak van de map te bevestigen, voeg je gewoon een schuine streep toe na de naam in hetzelfde vak, bijvoorbeeld: `bip39-wordlist/`. Door een schuine streep toe te voegen, wordt automatisch een map aangemaakt in plaats van een bestand:

![event](assets/07.webp)


- In deze map maak je een eerste YAML-bestand met de naam `bet.yml`:

![event](assets/08.webp)


- Vul dit bestand met informatie over uw inhoud met behulp van deze sjabloon:


```yaml
project:
type:
links:
download:
view:
- en:
tags:
-
-
contributors:
-
```


Hier zijn de gegevens die je voor elk veld moet invullen:



- `project`: Geef de identificatiecode van je organisatie op Plan ₿ Academy aan. Als je nog geen "project" identificatiecode hebt voor je bedrijf, kun je er een aanmaken door deze tutorial te volgen.


https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

Als je er geen hebt, kun je gewoon je naam, je pseudoniem of de naam van je bedrijf gebruiken zonder een projectprofiel aan te maken.



- `type`: Selecteer de aard van uw inhoud uit de volgende twee opties:
  - `Educational Content` voor educatieve inhoud.
  - `Visual Content` voor andere soorten van diverse inhoud.



- `links`: Geef links naar je inhoud. Je hebt twee opties:
  - Als je ervoor kiest om je inhoud direct op PlanB's GitHub te hosten, moet je de links naar dit bestand toevoegen tijdens de volgende stappen.
  - Als je inhoud elders wordt gehost, bijvoorbeeld op je persoonlijke website, geef dan hier de bijbehorende links aan:
     - `download`: Een link om je inhoud te downloaden.
     - `view`: Een link om je inhoud te bekijken (kan dezelfde zijn als de downloadlink). Als je inhoud in meerdere talen beschikbaar is, voeg dan voor elke taal een link toe.



- `tags`: Voeg twee tags toe die aan je inhoud zijn gekoppeld. Voorbeelden:      
  - Bitcoin
  - technologie
  - economie
  - onderwijs
  - meme...



- `contributors`: Vermeld je contributor identifier als je die hebt.


Je YAML-bestand zou er bijvoorbeeld zo uit kunnen zien:


```yaml
project: Plan ₿ Academy
type: Educational Content
links:
download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
view:
- In my example, I will leave the links empty for now, as I will add my PDF directly on GitHub:
![event](assets/09.webp)
- Once your modifications to this file are complete, save them by clicking on the `Commit changes...` button:
![event](assets/10.webp)
- Add a title for your modifications, as well as a short description:
![event](assets/11.webp)
- Click on the green `Propose changes` button:
![event](assets/12.webp)
- You will then arrive on a page that summarizes all your changes:
![event](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![event](assets/14.webp)
- Select your fork of the Plan ₿ Academy repository:
![event](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It is probably called `patch-1`. Click on it:
![event](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![event](assets/17.webp)
- Go back to the `resources/bet/` folder and select the folder of your content that you just created in the previous commit:
![event](assets/18.webp)
- In the folder of your content, click on the `Add file` button, then on `Create new file`:
![event](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![event](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`: ![event](assets/21.webp)
- Click on the `Commit changes...` button: ![event](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/23.webp)
- Return to the `assets` folder: ![event](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`: ![event](assets/25.webp)
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the Plan ₿ Academy site: ![event](assets/26.webp)
- It can be a preview, a logo, or an icon: ![event](assets/27.webp)
- Once the image is uploaded, make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![event](assets/28.webp)
- Be careful, your image must be named `logo` and must be in `.webp` format. The full file name should therefore be: `logo.webp`: ![event](assets/29.webp)
- Return to your `assets` folder and click on the intermediary file `.gitkeep`: ![event](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`: ![event](assets/31.webp)
- Make sure you are still on the same working branch, then click on the `Commit changes` button: ![event](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`: ![event](assets/33.webp)
- Return to the folder of your content: ![event](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`: ![event](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the content description. For example, if I want to write my description in English, I will name this file `en.yml`: ![event](assets/36.webp)
- Fill out this YAML file using this template:

```yaml
name:
description: |

```

- Voor de `name` sleutel kun je de naam van je inhoud toevoegen;
- Voor de `description` sleutel moet je slechts een korte alinea toevoegen die je inhoud beschrijft. De beschrijving moet in dezelfde taal zijn als de bestandsnaam. Je hoeft deze beschrijving niet te vertalen naar alle ondersteunde talen op de site, aangezien de PlanB-teams dit met hun model zullen doen. Bijvoorbeeld, hier is een voorbeeld van hoe je bestand eruit zou kunnen zien:

```

name: BIP39 WORDLIST
description: |
 \Complete and numbered list of the 2048 English words from the BIP39 dictionary used to encode mnemonic phrases. The document can be printed on a single page.

```

![event](assets/37.webp)
- Klik op de `Commit changes...` knop:
![event](assets/38.webp)
- Zorg ervoor dat het vakje `Commit directly to the patch-1 branch` is aangevinkt, voeg een titel toe, en klik vervolgens op `Commit changes`:
![event](assets/39.webp)
- De inhoud van je map zou er nu zo moeten uitzien:
![event](assets/40.webp)

---

*Als je de inhoud niet wilt toevoegen aan GitHub en je hebt de links al genoteerd in het `bet.yml` bestand tijdens de vorige stappen, dan kun je dit gedeelte overslaan en rechtstreeks doorgaan naar het deel over het maken van de Pull Request.*

- Ga terug naar de `/assets` folder:
![event](assets/41.webp)
- Klik op de `Add file` knop, dan op `Upload files`:
![event](assets/42.webp)
- Er wordt een nieuwe pagina geopend. Sleep en zet de inhoud die je wilt delen in het aangewezen gebied:
![event](assets/43.webp)
- Als voorbeeld heb ik het PDF-bestand van de BIP39 lijst toegevoegd: 
![event](assets/44.webp)
- Zodra de inhoud is geüpload, zorg ervoor dat het vakje `Commit directly to the patch-1 branch` is aangevinkt, en klik vervolgens op `Commit changes`: 
![event](assets/45.webp)
- Ga terug naar je `/assets` folder en klik op het bestand dat je zonet hebt geüpload:
![event](assets/46.webp)
- Haal de tussenliggende URL van je bestand op. Bijvoorbeeld, in mijn geval is de URL:

```

https://github.com/tutorial-pandul/Bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Behoud alleen het laatste deel van de URL vanaf `/resources`:

```

/bronnen/bet/bip39-wordlijst/assets/BIP39-WORDLIST.pdf

```

- Voeg aan het einde van de URL de volgende informatie toe om de juiste link te krijgen:

```

https://github.com/DiscoverBitcoin/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

Wat we hier doen is het toekomstige link naar je bestand voorspellen, nadat je voorstel is samengevoegd (merged) met de bronrepository van het Plan ₿ Academy.

- Ga terug naar je `bet.yml` bestand en klik op het potloodpictogram:
![event](assets/47.webp)

- Voeg je link daar toe:
![event](assets/48.webp)

- Zodra je wijzigingen klaar zijn, klik op de knop `Commit changes...`:
![event](assets/49.webp)

- Voeg een titel toe voor je wijzigingen, evenals een korte beschrijving:
![event](assets/50.webp)

- Klik op de groene knop `Commit changes...`:
![event](assets/51.webp)

- Als alles naar je zin lijkt, keer terug naar de root van je fork:
![event](assets/52.webp)

- Je zou een bericht moeten zien dat aangeeft dat je branch is gewijzigd. Klik op de knop `Compare & pull request`:
![event](assets/53.webp)

- Voeg een duidelijke titel en een beschrijving toe voor je Pull Request (PR):
![event](assets/54.webp)

- Klik op de knop `Create pull request`:
![event](assets/55.webp)
Gefeliciteerd! Je PR is succesvol aangemaakt. Een beheerder zal het nu beoordelen en, als alles in orde is, het samenvogen met de hoofdrepository van het Plan ₿ Academy. Je zou je BET een paar dagen later op de website moeten zien verschijnen.

Zorg ervoor dat je de voortgang van je PR volgt. Een beheerder kan een opmerking plaatsen met een verzoek om aanvullende informatie. Zolang je PR niet is gevalideerd, kun je het raadplegen in het tabblad "Pull requests" in de Plan ₿ Academy GitHub repository:

![event](assets/56.webp)

Bedankt voor je waardevolle bijdrage! :)
