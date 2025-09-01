---
name: Bijdrage - Git tutorial (gevorderd)
description: Gids voor gevorderde gebruikers met een tutorial over Plan ₿ Network met Git
---
![cover](assets/cover.webp)


Voordat je deze tutorial over het toevoegen van een nieuwe tutorial volgt, moet je een paar voorbereidende stappen hebben doorlopen. Als je dat nog niet gedaan hebt, bekijk dan eerst deze inleidende handleiding en kom dan hier terug:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Je hebt al:



- Kies een thema voor je zelfstudie;
- Neem contact op met het Plan ₿ Network team via [Telegram groep](https://t.me/PlanBNetwork_ContentBuilder) of paolo@planb.network ;
- Kies je bijdragehulpmiddelen.


In deze tutorial voor ervaren Git gebruikers, zullen we kort de belangrijkste stappen en essentiële richtlijnen samenvatten voor het aanbieden van een nieuwe Plan ₿ Network tutorial. Als je niet bekend bent met Git en GitHub, raad ik je aan om in plaats daarvan een van deze andere 2 meer gedetailleerde tutorials te volgen, die je stap voor stap zullen helpen:



- Intermediair (GitHub Desktop):


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957


- Beginners (web Interface):


https://planb.network/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Voorgestelde hulpmiddelen


Markdown-bestanden bewerken:



- Obsidian (gratis, niet open-source)
- Mark Text (gratis, open-source)
- Zettlr (gratis, open-source)
- Typora (Payware, ~€15, niet open-source)


Voor Git:



- Git (gratis, open-source)
- GitHub Desktop (gratis, open-source)
- Sourcetree (gratis, niet open-source)


Voor het bewerken van YAML-bestanden:



- Visual Studio Code (gratis, open-source)
- Sublime Text (gratis met beperkingen, niet open-source)


Diagrammen en visuals maken:



- Canva (gratis met betaalde opties, niet open-source)
- Inkscape (gratis, open-source)
- Penpot (gratis, open-source)


## Werkstromen


### 1 - Uw lokale omgeving configureren



- Je moet je eigen Fork van de [Plan ₿ Network repository op GitHub] (https://github.com/PlanB-Network/Bitcoin-educational-content) hebben.
- Synchroniseer de hoofdbranch (`dev`) van je Fork met het bronrepository.
- Werk je lokale kloon bij.


```
# Clone your fork (if not already done)
git clone https://github.com/<your-username>/bitcoin-educational-content.git
cd bitcoin-educational-content

# Add the source repository as a remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git

# Fetch the latest changes from the source repository
git fetch upstream

# Switch to the main 'dev' branch
git checkout dev

# Merge the changes from the source repository's 'dev' branch into your fork
git merge upstream/dev

# Push the updates to your fork on GitHub
git push origin dev
```


### 2 - Maak een nieuwe tak



- Zorg ervoor dat je op de `dev` tak zit.
- Maak een nieuwe tak aan met een beschrijvende naam (bijvoorbeeld `tuto-Green-Wallet-loic`).
- Publiceer deze tak op je online Fork.


```
# Make sure you are on the 'dev' branch
git checkout dev

# Create a new branch with a descriptive name
git checkout -b tuto-green-wallet-loic

# Publish this branch to your online fork
git push -u origin tuto-green-wallet-loic
```


### 3 - De zelfstudiedocumenten toevoegen


***Noot:*** Je kunt stappen 3 en 4 automatiseren met [mijn Python GUI-script] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/scripts/tutorial-related/new-tutorial-creation). Start het direct vanuit de map in je lokale kloon en vul dan de vereiste velden in op de GUI. Zie de [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md) voor meer informatie over de installatie en het gebruik ervan.


Als je het liever handmatig doet, volg dan deze stappen:



- Zoek de juiste map in het lokale archief (bijvoorbeeld `tutorials/Wallet`).
- Maak een map aan voor de zelfstudie met een duidelijke naam (bijvoorbeeld `Green-Wallet`). Deze mapnaam zal ook het URL-pad van de zelfstudie bepalen. De naam moet in kleine letters zijn, zonder speciale tekens (behalve koppeltekens) en zonder spaties.
- Voeg de volgende items toe aan deze map:
    - Een submap met de naam `assets` die:
        - Twee `.webp` afbeeldingen:
            - `logo.webp`: Het tutoriallogo (vierkant formaat met achtergrond). Dit logo moet de gepresenteerde software of het gereedschap voorstellen. Als de tutorial niet specifiek is voor een tool (bijv.: een algemene gids voor het genereren van een Mnemonic zin), kun je een geschikte visual kiezen (bijv.: een generiek icoon).
            - `cover.webp`: Een coverafbeelding die aan het begin van de tutorial wordt weergegeven.
        - Een submap met de code van de oorspronkelijke taal van de zelfstudie. Als de handleiding bijvoorbeeld in het Engels is geschreven, moet deze submap `en' heten. Plaats al het beeldmateriaal van de handleiding (diagrammen, afbeeldingen, screenshots, enz.) in deze map.
    - Een `tutorial.yml` bestand met metadata (auteur, tags, categorie, moeilijkheidsgraad, etc.).
    - Een Markdown bestand met de tutorial, genoemd naar de taalcode (bijv. `fr.md`, `en.md`, etc.).


```
# Navigate to the appropriate folder
cd tutorials/wallet

# Create the directory dedicated to the tutorial
mkdir green-wallet
cd green-wallet

# Create the 'assets' subfolder
mkdir -p assets

# Create the subfolder for the original language code (e.g., 'en' for English)
mkdir -p assets/en

# Create the metadata file and the Markdown tutorial file (e.g., 'en.md' for English)
touch tutorial.yml en.md
```


### 4 - Vul het YAML-bestand in



- Vul het `tutorial.yml` bestand als volgt aan:


```
id:

project_id:

tags:
-
-
-

category:

level:

professor_id:

# Proofreading metadata

original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributor_names:
-
reward:
```


Dit zijn de verplichte velden:



- id**: Een UUID (_Universally Unique Identifier_) die de zelfstudie uniek identificeert. Je kunt generate gebruiken met [een online tool] (https://www.uuidgenerator.net/version4). De enige vereiste is dat deze UUID willekeurig is om conflicten met een andere UUID op het platform te vermijden;



- project_id**: De UUID van het bedrijf of de organisatie achter het gereedschap dat in de tutorial wordt gepresenteerd [uit de projectlijst] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Als je bijvoorbeeld een tutorial maakt over de Green Wallet software, kun je deze `project_id` vinden in het volgende bestand: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Deze informatie wordt toegevoegd aan het YAML-bestand van je tutorial, omdat Plan ₿ Network een database bijhoudt van alle bedrijven en organisaties die op Bitcoin of gerelateerde projecten werken. Door de `project_id` toe te voegen van de entiteit die gelinkt is aan je zelfstudie, creëer je een link tussen de twee Elements;



- tags**: 2 of 3 relevante trefwoorden die verband houden met de inhoud van de zelfstudie, exclusief gekozen [uit de Plan ₿ Network taglijst] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- categorie**: De subcategorie die overeenkomt met de inhoud van de tutorial, volgens de Plan ₿ Network website structuur (bijvoorbeeld, voor wallets: `desktop`, `hardware`, `mobiel`, `backup`);



- level**: De moeilijkheidsgraad van de zelfstudie, gekozen uit:
    - beginner
    - gemiddeld
    - geavanceerd
    - `expert`



- professor_id**: Uw `professor_id` (UUID) zoals weergegeven op [uw professorprofiel] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors);



- oorspronkelijke_taal**: De oorspronkelijke taal van de zelfstudie (bijv. `fr`, `en`, enz.);



- proeflezen**: Informatie over het proefleesproces. Maak het eerste deel af, want het proeflezen van je eigen zelfstudie telt als een eerste validatie:
    - language**: Taalcode van het proeflezen (bijv. `fr`, `en`, enz.).
    - last_contribution_date**: Datum van de dag.
    - urgentie**: 1
    - contributor_names**: Je GitHub ID.
    - beloning**: 0


Raadpleeg de bijbehorende handleiding voor meer informatie over je leraren-ID:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
- wallets
- software
- keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributor_names:
- LoicPandul
reward: 0
```


### 5 - De inhoud schrijven



- Vul de Markdown bestandseigenschappen aan met:
    - De titel (`naam`).
    - Een korte beschrijving (`description`).
- Voeg de omslagafbeelding bovenaan de tutorial toe met Markdown syntaxis (vervang "Green" door de naam van het getoonde gereedschap):


```
![cover-green](assets/cover.webp)
```



- Schrijf de inhoud van de tutorial in Markdown:
    - Gebruik goed gestructureerde koppen (`##`), lijsten en alinea's.
    - Visuals invoegen met Markdown syntaxis:


```
![nom-image](assets/en/001.webp)
```




- Plaats diagrammen en afbeeldingen in de corresponderende taalsubmap in `/assets`.


### 6 - De zelfstudie opslaan en verzenden



- Sla je wijzigingen lokaal op door een commit aan te maken met een beschrijvend bericht.
- Push de wijzigingen naar je GitHub Fork.


```
# Create a commit with a descriptive message
git commit -m "Added green-wallet tutorial"

# Push your changes to your fork
git push origin tuto-green-wallet-loic
```



- Als je klaar bent, maak dan een Pull Request (PR) aan op GitHub om de integratie van je wijzigingen voor te stellen.
- Voeg een titel en een korte beschrijving toe aan het PR. Vermeld het bijbehorende probleemnummer in de opmerking.


### 7 - Proeflezen en samenvoegen



- Wacht op validatie of feedback van een beheerder.
- Breng indien nodig correcties aan en push nieuwe commits.


```
# Create a commit describing the corrections made
git commit -m "Corrections following the review of the green-wallet tutorial"

# Push the corrections to your fork
git push origin tuto-green-wallet-loic
```



- Als de PR samengevoegd is, kun je je werktak verwijderen.


## Normen voor het maken van inhoud



- Opmaak ondersteund op het platform**:
    - Klassieke Markdown: lijsten, links, afbeeldingen, citaten, vet, cursief enz.
    - LaTeX (alleen blok, niet inline): begrensd door `$$`.
    - Inline code: Syntaxis met een enkele backtick.
    - Codeblokken: Syntaxis met drie backticks, bijvoorbeeld:


```
print("Hello, Bitcoin!")
```



- Illustraties en diagrammen**:
    - Alle afbeeldingen moeten het WebP-formaat hebben. Gebruik deze gratis tool om ze indien nodig te converteren: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Geef visuals een naam met 2 of 3 cijfers (bijvoorbeeld `001.webp`, `002.webp`).
    - Gebruik mock-ups voor mobiele of Hardware Wallet tutorials.
    - Gebruik alleen zelfgemaakte of rechtenvrije afbeeldingen.
    - Zorg ervoor dat ze relevant en van hoge kwaliteit zijn.
- Grafisch charter**:
    - Lettertype: [Rubik](https://fonts.google.com/specimen/Rubik).
    - Kleuren Plan ₿ Network:
        - Oranje: `#FF5C00`
        - Zwart: `#000000`
        - Wit: `#FFFFFF`


Als je technische problemen ondervindt bij het indienen van je tutorial, aarzel dan niet om hulp te vragen op [onze speciale Telegram-groep voor bijdragen](https://t.me/PlanBNetwork_ContentBuilder). Hartelijk dank!