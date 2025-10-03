---
name: Educatieve hulpmiddelen toevoegen
description: Hoe voeg je nieuw onderwijsmateriaal toe op PlanB Network?
---
![event](assets/cover.webp)


De missie van PlanB is om toonaangevende educatieve bronnen aan te bieden op Bitcoin, in zoveel mogelijk talen. Alle inhoud die op de site wordt gepubliceerd is open-source en wordt gehost op GitHub, waardoor iedereen kan deelnemen aan het verrijken van het platform.


Naast tutorials en training biedt PlanB Network ook een uitgebreide bibliotheek met gevarieerde educatieve inhoud op Bitcoin, toegankelijk voor iedereen, [in de "BET" (_Bitcoin Educational Toolkit_) sectie](https://planb.network/resources/bet). Deze database bevat educatieve posters, memes, humoristische propagandaposters, technische diagrammen, logo's en andere hulpmiddelen voor gebruikers. Het doel van dit initiatief is om individuen en gemeenschappen die wereldwijd Bitcoin onderwijzen te ondersteunen door hen te voorzien van de nodige visuele middelen.


Wil je meewerken aan het verrijken van deze database, maar weet je niet hoe? Deze tutorial is voor jou!


*Het is noodzakelijk dat alle inhoud die in de site wordt geïntegreerd vrij is van rechten of de licentie van het bronbestand respecteert. Alle visuals gepubliceerd op PlanB Network zijn beschikbaar onder de [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) licentie.*

![event](assets/01.webp)


- Eerst moet je een account hebben op GitHub. Als je niet weet hoe je een account aanmaakt, hebben we een gedetailleerde tutorial gemaakt om je te begeleiden.


https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- Ga naar [de GitHub repository van PlanB gewijd aan gegevens](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/bet) in de `resources/bet/` sectie:

![event](assets/02.webp)


- Klik rechtsboven op de knop `Bestand toevoegen` en vervolgens op `Nieuw bestand maken`:

![event](assets/03.webp)


- Als je nog nooit hebt bijgedragen aan de inhoud van PlanB Network, zul je een Fork van het originele repository moeten maken. Een repository forken betekent dat je een kopie van die repository maakt op je eigen GitHub account, waarmee je aan het project kunt werken zonder de originele repository te beïnvloeden. Klik op de `Fork this repository` knop:

![event](assets/04.webp)


- Je komt dan op de GitHub bewerkingspagina:

![event](assets/05.webp)


- Maak een map voor je inhoud. Om dit te doen, schrijf je in het vak `Naam je bestand...` de naam van je inhoud in kleine letters met streepjes in plaats van spaties. Laten we in mijn voorbeeld zeggen dat ik een PDF-visual van de BIP39-lijst van 2048 woorden wil toevoegen. Dus noem ik mijn map `bip39-wordlist`: ![event](assets/06.webp)
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



- `project`: Geef de identificatiecode van je organisatie op PlanB Network aan. Als je nog geen "project" identifier hebt voor je bedrijf, kun je er een aanmaken door deze tutorial te volgen.


https://planb.network/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d

Als je er geen hebt, kun je gewoon je naam, je pseudoniem of de naam van je bedrijf gebruiken zonder een projectprofiel aan te maken.



- `type`: Selecteer de aard van uw inhoud uit de volgende twee opties:
 - educatieve inhoud` voor educatieve inhoud.
 - `Visuele inhoud` voor andere soorten diverse inhoud.



- `links`: Geef links naar je inhoud. Je hebt twee opties:
 - Als je ervoor kiest om je inhoud direct op PlanB's GitHub te hosten, moet je de links naar dit bestand toevoegen tijdens de volgende stappen.
 - Als je inhoud elders wordt gehost, bijvoorbeeld op je persoonlijke website, geef dan hier de bijbehorende links aan:
     - `download`: Een link om je inhoud te downloaden.
     - `bekijken`: Een link om je inhoud te bekijken (kan dezelfde zijn als de downloadlink). Als je inhoud in meerdere talen beschikbaar is, voeg dan voor elke taal een link toe.



- `tags`: Voeg twee tags toe die aan je inhoud zijn gekoppeld. Voorbeelden:
 - Bitcoin
 - technologie
 - economie
 - onderwijs
 - meme...



- `contributors`**: Vermeld je contributor identifier als je die hebt.**


Je YAML-bestand zou er bijvoorbeeld zo uit kunnen zien:


```yaml
project: PlanB-Network
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
- Select your fork of the PlanB Network repository:
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
- A new page will open. Drag and drop a thumbnail that represents your content into the area. This image will be displayed on the PlanB Network site: ![event](assets/26.webp)
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

```

name:
description: |

```

- For the `name` key, you can add the name of your content;
- For the `description` key, you simply need to add a short paragraph that describes your content. The description must be in the same language as the file name. You do not need to translate this description into all the supported languages on the site, as the PlanB teams will do so with their model.
For example, here is what your file might look like:

```

name: BIP39 WORDLIST
description: |
Volledige en genummerde lijst van de 2048 Engelse woorden uit het BIP39 woordenboek die gebruikt worden om Mnemonic zinnen te coderen. Het document kan op één pagina worden afgedrukt.

```

![event](assets/37.webp)
- Click on the `Commit changes...` button:
![event](assets/38.webp)
- Ensure that the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![event](assets/39.webp)
- Your content folder should now look like this:
![event](assets/40.webp)

---

*If you prefer not to add the content on GitHub and you have already noted the links in the `bet.yml` file during the previous steps, you can skip this section and go directly to the part concerning the creation of the Pull Request.*

- Return to the `/assets` folder:
![event](assets/41.webp)
- Click on the `Add file` button, then on `Upload files`:
![event](assets/42.webp)
- A new page will open. Drag and drop into the area the content you wish to share:
![event](assets/43.webp)
- For example, I added the PDF file of the BIP39 list:
![event](assets/44.webp)
- Once the content is uploaded, ensure that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![event](assets/45.webp)
- Return to your `/assets` folder and click on the file you just uploaded:
![event](assets/46.webp)
- Retrieve the intermediate URL of your file. For example, in my case, the URL is:

```

https://github.com/tutorial-pandul/Bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```

- Keep only the last part of the URL from `/resources` onwards:

```

/bronnen/bet/bip39-wordlijst/assets/BIP39-WORDLIST.pdf

```

- Add to the base of the URL the following information to have the correct link:

```

https://github.com/DiscoverBitcoin/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf

```