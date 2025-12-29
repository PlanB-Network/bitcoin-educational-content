---
name: Bijdrage - tutorial met GitHub Desktop (intermediair)
description: Complete handleiding om een tutorial voor te stellen op Plan ₿ Academy met GitHub Desktop
---
![cover](assets/cover.webp)


Voordat je deze tutorial over het toevoegen van een nieuwe tutorial volgt, moet je een aantal voorbereidende stappen hebben doorlopen. Als je dat nog niet gedaan hebt, raadpleeg dan eerst deze inleidende handleiding en kom dan hier terug:


https://planb.academy/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Dat heb je al gedaan:


- Kies het thema van je tutorial;
- Neem contact op met het Plan ₿ Academy team via [de Telegram groep](https://t.me/PlanBNetwork_ContentBuilder) of paolo@planb.network;
- Kies je bijdragehulpmiddelen.


In deze tutorial zullen we zien hoe je je tutorial op Plan ₿ Academy kunt toevoegen door je lokale omgeving in te stellen met GitHub Desktop. Als je al bedreven bent met Git, is deze zeer gedetailleerde tutorial misschien niet nodig voor je. Ik zou eerder aanraden om deze andere tutorial te raadplegen, waar ik alleen de belangrijkste richtlijnen presenteer, zonder gedetailleerde stap-voor-stap begeleiding:



- **Ervaren gebruikers**:


https://planb.academy/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

Als je liever niet je lokale omgeving instelt, volg dan deze andere tutorial, ontworpen voor beginners, waar we de wijzigingen direct via GitHub's web interface maken:



- **Beginners (web interface)**:


https://planb.academy/tutorials/contribution/content/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

## Vereisten


Software vereist om deze tutorial te volgen:



- [GitHub Desktop](https://desktop.github.com/);
- Een markdown-bestandseditor zoals [Obsidian](https://obsidian.md/);
- Een code editor ([VSC](https://code.visualstudio.com/) of [Sublime Text](https://www.sublimetext.com/)).


![TUTO](assets/fr/01.webp)


Vereisten voordat u de tutorial start:



- Een [GitHub account] hebben (https://github.com/signup);
- Neem een fork van het [Plan ₿ Academy bronarchief](https://github.com/PlanB-Network/Bitcoin-educational-content);
- Heb [een professorprofiel op Plan ₿ Academy](https://planb.academy/professors) (alleen als je een complete tutorial voorstelt).


Als je hulp nodig hebt bij het verkrijgen van deze vereisten, kun je terecht in mijn andere tutorials:



Zodra alles klaar is en je lokale omgeving goed is ingesteld met je eigen fork van Plan ₿ Academy, kun je beginnen met het toevoegen van de tutorial.


## 1 - Maak een nieuwe tak


Open je browser en ga naar de pagina van je fork van de Plan ₿ Academy repository. Dit is de fork die je hebt aangemaakt op GitHub. De URL van je fork zou er als volgt uit moeten zien: `https://github.com/[your-username]/bitcoin-educational-content`:


![TUTO](assets/fr/03.webp)


Zorg ervoor dat je op de hoofd branch `dev` zit en klik dan op de knop `Sync fork`. Als je fork niet up-to-date is, zal GitHub aanbieden om je branch bij te werken. Ga verder met deze update. Als je branch daarentegen al bijgewerkt is, zal GitHub je hierover informeren:


![TUTO](assets/fr/04.webp)


Open de GitHub Desktop software en zorg ervoor dat je fork correct geselecteerd is in de linkerbovenhoek van het venster:


![TUTO](assets/fr/05.webp)


Klik op de knop `Fetch origin`. Als je lokale repository al up to date is, zal GitHub Desktop geen extra actie voorstellen. Anders zal de `Pull origin` optie verschijnen. Klik op deze knop om je lokale repository bij te werken:


![TUTO](assets/fr/06.webp)


Controleer of je inderdaad op de hoofdbranch `dev` zit:


![TUTO](assets/fr/07.webp)


Klik op deze branch en klik vervolgens op de knop `New branch`:


![TUTO](assets/fr/08.webp)


Zorg ervoor dat de nieuwe branch gebaseerd is op de bronrepository, namelijk `Plan ₿ Academy/Bitcoin-educational-content`.


Geef je branch een naam zodat de titel duidelijk is over het doel en gebruik streepjes om elk woord te scheiden. Bijvoorbeeld, laten we zeggen dat ons doel is om een tutorial te schrijven over het gebruik van de Sparrow wallet software. In dit geval zou de werk branch die gewijd is aan het schrijven van deze tutorial de naam `tuto-Sparrow-Wallet-loic` kunnen krijgen. Zodra de juiste naam is ingevoerd, klik je op `Create branch` om het aanmaken van de branch te bevestigen:


![TUTO](assets/fr/09.webp)


Klik nu op de knop `Publish branch` om je nieuwe werk branch op te slaan in je online fork op GitHub:

![TUTORIAL](assets/fr/10.webp)

Nu, op GitHub Desktop, zou je jezelf op je nieuwe branch moeten bevinden. Dit betekent dat alle wijzigingen die lokaal op je computer gemaakt zijn, uitsluitend op deze specifieke branch opgeslagen zullen worden. Bovendien, zolang deze branch geselecteerd blijft op GitHub Desktop, corresponderen de bestanden die lokaal op je machine zichtbaar zijn met die van deze branch (`tuto-Sparrow-Wallet-loic`), en niet met die van de hoofd branch (`dev`).


![TUTORIAL](assets/fr/11.webp)


Voor elk nieuw artikel dat je wilt publiceren, zul je een nieuwe branch van `dev` moeten maken. Een branch in Git is een parallelle versie van het project, waarmee je wijzigingen kunt maken zonder de hoofdbranch te beïnvloeden, totdat het werk klaar is om samengevoegd te worden.


## 2 - De tutorialbestanden toevoegen


Nu de werk branch is aangemaakt, is het tijd om je nieuwe tutorial te integreren. Je hebt twee opties: mijn Python script gebruiken, dat het aanmaken van de benodigde documenten automatiseert, of handmatig elk bestand aanmaken. We zullen kijken naar de te volgen stappen voor elke optie.


### Met mijn Python-script


Je moet het volgende installeren op je machine:


- Python 3.8 of hoger.


Om het script te gebruiken, navigeer je naar de map waar het is opgeslagen. Het script bevindt zich in de Plan ₿ Academy data repository op het pad: `Bitcoin-educational-content/scripts/tutorial-related/data-creator`.


Van zodra je in de map bent, installeer je de afhankelijkheden:


```
pip install -r requirements.txt
```


Start vervolgens de software met het commando:


```
python3 main.py
```


Een grafische gebruiker interface (GUI) wordt geopend. De eerste keer moet je alle benodigde informatie invoeren, maar bij volgend gebruik onthoudt het script je persoonlijke informatie, zodat je die niet opnieuw hoeft in te voeren.


![DATA-CREATOR-PY](assets/fr/37.webp)


Begin met het invoeren van het lokale pad naar de map `/tutorials` in je gekloonde archief (`.../Bitcoin-educational-content/tutorials/`). Je kunt het handmatig invoeren of op de knop "Browse" klikken om te navigeren met je bestandsverkenner.


![DATA-CREATOR-PY](assets/fr/38.webp)


Selecteer de taal waarin je je tutorial wilt schrijven.


![DATA-CREATOR-PY](assets/fr/39.webp)


Voer in het veld "Contributor's GitHub ID" je GitHub gebruikersnaam in.


![DATA-CREATOR-PY](assets/fr/40.webp)


Vervolgens moet je je docentprofiel invullen. Er zijn verschillende opties beschikbaar:


- Voer de eerste letters van je naam in het veld "Professor Name" in. Je naam verschijnt dan in de vervolgkeuzelijst "Prof. Suggestions" hieronder. Selecteer deze door erop te klikken;
- Je kunt ook rechtstreeks op de vervolgkeuzelijst "Prof. Suggestions" klikken en de naam van je docent kiezen.


Deze actie vult automatisch je docent UUID in in het overeenkomstige veld.



![DATA-CREATOR-PY](assets/fr/41.webp)


Als je nog geen docentprofiel hebt, bekijk dan deze tutorial:


https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Klik dan op de knop "New Tutorial".


![DATA-CREATOR-PY](assets/fr/42.webp)


Kies een hoofdcategorie voor je tutorial. Kies vervolgens een relevante subcategorie op basis van je gekozen hoofdcategorie.


![DATA-CREATOR-PY](assets/fr/43.webp)


Bepaal de moeilijkheidsgraad van de tutorial.


![DATA-CREATOR-PY](assets/fr/44.webp)


Kies een naam voor de map die speciaal voor je tutorial is gemaakt. De naam van deze map moet overeenkomen met de software die in de tutorial behandeld wordt, gebruik koppeltekens om woorden te scheiden. De map kan bijvoorbeeld `red-Wallet` heten:


![DATA-CREATOR-PY](assets/fr/45.webp)


Het `project_id` is de UUID van het bedrijf of de organisatie achter de tool die in de tutorial behandeld wordt, beschikbaar [in de lijst van projecten](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Bijvoorbeeld, voor een tutorial over Sparrow wallet, kun je het `project_id` vinden in het bestand: `Bitcoin-educational-content/resources/projects/Sparrow/project.yml`. Deze informatie is toegevoegd aan het YAML-bestand van je tutorial, omdat Plan ₿ Academy een database bijhoudt van bedrijven en organisaties die actief zijn in Bitcoin of gerelateerde projecten. Door het bijbehorende `project_id` toe te voegen, koppel je je inhoud aan de relevante entiteit.


***Update:*** In de nieuwe versie van het script hoef je niet langer handmatig het `project_id` in te voeren. Er is een zoekfunctie toegevoegd om het project op naam te vinden en automatisch de bijbehorende `project_id` op te halen. Typ het begin van de naam van het project in het veld "Project Name" om het te zoeken en selecteer vervolgens het gewenste bedrijf in het vervolgkeuzemenu. Het `project_id` wordt automatisch ingevuld in het onderstaande veld. Je kunt het indien nodig ook handmatig invoeren.


![DATA-CREATOR-PY](assets/fr/46.webp)


Voor tags selecteer je 2 of 3 relevante trefwoorden die verband houden met de inhoud van je tutorial en kies je uitsluitend uit [de Plan ₿ Academy taglijst](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md). De software biedt ook een zoekfunctie voor trefwoorden met een vervolgkeuzelijst.


![DATA-CREATOR-PY](assets/fr/47.webp)


Zodra alle informatie is ingevoerd en gecontroleerd, klik je op "Create Tutorial" om de aanmaak van je tutorialbestanden te bevestigen. Dit zal je tutorialmap en alle benodigde bestanden in de geselecteerde categorie lokaal aanmaken.


![DATA-CREATOR-PY](assets/fr/48.webp)


Je kunt nu de subsectie "Zonder mijn Python script" overslaan, evenals stap 3, "Vul het YAML-bestand in", aangezien het script deze handelingen al voor je heeft uitgevoerd. Ga direct door naar stap 4 en begin met het schrijven van je tutorial.


Voor meer informatie over dit Python-script kun je ook de [README](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/scripts/tutorial-related/new-tutorial-creation/README.md) bekijken.


### Zonder mijn Python-script


Open je bestandsbeheerder en navigeer naar de `Bitcoin-educational-content` map, die de lokale kloon van je repository representeert. Je kunt deze map normaal gesproken vinden onder `Documents\GitHub\Bitcoin-educational-content`.


In deze map moet je de juiste submap vinden om je tutorial in te plaatsen. De mapindeling weerspiegelt de verschillende secties van de Plan ₿ Academy website. In ons voorbeeld, omdat we een tutorial over Sparrow wallet willen toevoegen, moeten we naar het volgende pad navigeren: `bitcoin-educational-content\tutorials\wallet`, wat overeenkomt met de `Wallet` sectie op de website:


![TUTO](assets/fr/12.webp)


Binnen de `Wallet` map moet je een nieuwe map maken die specifiek gewijd is aan je tutorial. De naam van deze map moet verwijzen naar de software die in de tutorial behandeld wordt, zorg ervoor dat woorden met streepjes verbonden worden. In mijn voorbeeld krijgt de map de naam `Sparrow-Wallet`:


![TUTO](assets/fr/13.webp)


In deze nieuwe submap, gewijd aan je tutorial, moeten verschillende elementen worden toegevoegd:


- Maak een map `assets` aan voor alle illustraties die nodig zijn voor je tutorial;
- Binnen deze `assets` map moet je een submap maken met de naam van de oorspronkelijke taalcode van de tutorial. Als de tutorial bijvoorbeeld in het Engels geschreven is, moet deze submap `en` heten. Plaats daar al het beeldmateriaal van de tutorial (diagrammen, afbeeldingen, screenshots, enz.).
- Een `tutorial.yml` bestand moet aangemaakt worden om de details van je tutorial op te slaan;
- Er moet een markdown-bestand worden aangemaakt om de feitelijke inhoud van je tutorial te schrijven. Dit bestand moet een titel krijgen die overeenkomt met de taalcode van de tekst. Bijvoorbeeld, voor een tutorial geschreven in het Frans, moet het bestand `fr.md` heten.


![TUTO](assets/fr/14.webp)


Samengevat is dit de hiërarchie van de bestanden die je moet maken:


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (to be modified with the correct category)
└── sparrow-wallet/ (to be modified with the name of the tutorial)
├── assets/
│   ├── en/ (to be modified according to the appropriate language code)
├── tutorial.yml
└── en.md (to be modified according to the appropriate language code)
```


## 3 - Vul het YAML-bestand in


Vul het bestand `tutorial.yml` in door het volgende sjabloon te kopiëren:


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



- **id**: Een UUID (_Universally Unique Identifier_) die de tutorial uniek identificeert. Je kunt dit genereren met behulp van [een online tool](https://www.uuidgenerator.net/version4). De enige vereiste is dat deze UUID willekeurig is om conflicten met een andere UUID op het platform te vermijden;



- **project_id**: De UUID van het bedrijf of de organisatie achter de tool die in de tutorial wordt gepresenteerd [uit de projectlijst](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Als je bijvoorbeeld een tutorial maakt over de Green Wallet software, kun je het overeenstemmend `project_id` vinden in het volgende bestand: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Deze informatie wordt toegevoegd aan het YAML-bestand van je tutorial, omdat Plan ₿ Academy een database bijhoudt van alle bedrijven en organisaties die werken aan Bitcoin of gerelateerde projecten. Door het `project_id` van de entiteit die gelinkt is aan je tutorial toe te voegen, creëer je een link tussen de twee elementen;



- **tags**: 2 of 3 relevante trefwoorden die verband houden met de inhoud van de tutorial, exclusief gekozen [uit de Plan ₿ Academy taglijst](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- **category**: De subcategorie die overeenkomt met de tutorialinhoud, volgens de Plan ₿ Academy websitestructuur (bijvoorbeeld voor wallets: `desktop`, `hardware`, `mobile`, `backup`);



- **level**: De moeilijkheidsgraad van de tutorial, gekozen uit:
  - `beginner`
  - `intermediair`
  - `geavanceerd`
  - `expert`



- **professor_id**: je `professor_id` (UUID) zoals weergegeven op [uw professorprofiel](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors);



- **original_language**: De oorspronkelijke taal van de tutorial (bijv. `fr`, `en`, enz.);



- **proofreading**: Informatie over het proefleesproces. Maak het eerste deel af, want het proeflezen van je eigen tutorial telt als een eerste validatie:
  - **language**: Taalcode van het proeflezen (bijv. `fr`, `en`, enz.).
  - **last_contribution_date**: Datum van de dag.
  - **urgency**: 1
  - **contributor_names**: Je GitHub ID.
  - **reward**: 0


Raadpleeg de bijbehorende handleiding voor meer informatie over je docenten-ID:


https://planb.academy/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

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


Als je klaar bent met het aanpassen van je `tutorial.yml` bestand, sla je document dan op door te klikken op `File > Save` (Bestand > Opslaan):


![TUTO](assets/fr/16.webp)


Je kunt nu je code editor sluiten.


## 4 - Vul het Markdown-bestand in


Nu kun je het bestand openen dat je tutorial zal hosten, met de naam van de code van je taal, zoals `fr.md`. Ga naar Obsidian, aan de linkerkant van het venster, scroll door de mappenstructuur tot je de map van je tutorial en het bestand dat je zoekt vindt:


![TUTO](assets/fr/18.webp)


Klik op het bestand om het te openen:


![TUTO](assets/fr/19.webp)


We beginnen met het invullen van het gedeelte `Properties` (Eigenschappen) bovenaan het document.


![TUTO](assets/fr/20.webp)


Voeg het volgende codeblok handmatig toe en vul het in:


```
---
name: [Title]
description: [Description]
---
```


![TUTO](assets/fr/21.webp)


Vul de naam van je tutorial in en een korte beschrijving ervan:


![TUTO](assets/fr/22.webp)


Voeg vervolgens het pad van de omslagafbeelding toe aan het begin van je tutorial. Om dit te doen, noteer:


```
![cover-sparrow](assets/cover.webp)
```


Deze syntaxis is handig wanneer je een afbeelding aan je tutorial moet toevoegen. Het uitroepteken geeft aan dat het om een afbeelding gaat, met de alternatieve tekst (alt) gespecificeerd tussen de haakjes. Het pad naar de afbeelding wordt aangegeven tussen de haakjes:


![TUTO](assets/fr/23.webp)


## 5 - Logo en omslag toevoegen


In de map `assets` moet je een bestand met de naam `logo.webp` toevoegen, dat zal dienen als thumbnail voor je artikel. Deze afbeelding moet in `.webp` formaat zijn en moet een vierkante afmeting hebben om te passen in de gebruikersinterface. Je bent vrij om het logo van de software in de tutorial of een andere relevante afbeelding te kiezen, mits deze vrij is van rechten. Voeg daarnaast ook een afbeelding met de titel `cover.webp` toe op dezelfde plaats. Deze afbeelding wordt bovenaan de tutorial weergegeven. Zorg ervoor dat deze afbeelding, net als het logo, de gebruiksrechten respecteert en geschikt is voor de context van je tutorial:

## 6 - De tutorial schrijven en afbeeldingen toevoegen


Ga verder met het schrijven van je tutorial door je inhoud op te stellen. Als je een ondertitel wilt toevoegen, pas dan de juiste markdown-opmaak toe door de tekst vooraf te laten gaan door `##`:


![TUTO](assets/fr/24.webp)


De taalsubmap in de map `assets` wordt gebruikt om diagrammen en afbeeldingen op te slaan die bij je tutorial horen. Vermijd zoveel mogelijk tekst in je afbeeldingen om je inhoud toegankelijk te maken voor een internationaal publiek. Natuurlijk zal de software die wordt gepresenteerd tekst bevatten, maar als je diagrammen of extra aanduidingen toevoegt op software screenshots, doe dit dan zonder tekst of, als het onmisbaar blijkt, gebruik Engels.


![TUTO](assets/fr/25.webp)


Om je afbeeldingen een naam te geven, gebruik je nummers die overeenkomen met de volgorde waarin ze in de tutorial voorkomen, geformatteerd met twee cijfers (of drie cijfers als je tutorial meer dan 99 afbeeldingen bevat). Bijvoorbeeld, noem je eerste afbeelding `01.webp`, je tweede `02.webp`, enzovoort.


Je afbeeldingen moeten uitsluitend in `.webp` formaat zijn. Indien nodig kun je [mijn beeldconversiesoftware] gebruiken (https://github.com/LoicPandul/ImagesConverter).


![TUTO](assets/fr/26.webp)


Om een diagram in je document in te voegen, gebruik je de volgende markdown opdracht, waarbij je ervoor zorgt dat je de juiste alternatieve tekst en het juiste pad van de afbeelding opgeeft:


```
![sparrow](assets/fr/01.webp)
```


Het uitroepteken aan het begin geeft aan dat het om een afbeelding gaat. De alternatieve tekst, die helpt bij toegankelijkheid en SEO, wordt tussen de haakjes geplaatst. Tenslotte wordt het pad naar de afbeelding aangegeven tussen de haakjes.


Als je je eigen diagrammen wilt maken, zorg er dan voor dat je je houdt aan het grafische handvest van Plan ₿ Academy om visuele consistentie te garanderen:


- **Font**: Gebruik [Rubik](https://fonts.google.com/specimen/Rubik);
- **Colors**:
  - Orange: #FF5C00
  - Black: #000000
  - White: #FFFFFF


**Het is noodzakelijk dat alle afbeeldingen die je in je tutorials opneemt vrij zijn van rechten of de licentie van het bronbestand respecteren**. Ook worden alle diagrammen die op Plan ₿ Academy gepubliceerd zijn, beschikbaar gesteld onder de CC-BY-SA-licentie, op dezelfde manier als de tekst.

**-> Tip:** Als je bestanden, zoals afbeeldingen, openbaar deelt, is het belangrijk om onnodige metadata te verwijderen. Deze kunnen gevoelige informatie bevatten, zoals locatiegegevens, aanmaakdata of details over de auteur. Om je privacy te beschermen, is het aan te raden om deze metadata te verwijderen. Om dit proces te vereenvoudigen, kun je gespecialiseerde tools gebruiken zoals [Exif Cleaner](https://exifcleaner.com/), waarmee je de metadata van een document kunt opschonen met een eenvoudige sleep-en neerzetprocedure.

## 7 - De tutorial opslaan en verzenden


Zodra je klaar bent met het schrijven van je handleiding in de taal van je keuze, is de volgende stap het indienen van een **Pull Request** (PR). De beheerder zal er dan voor zorgen dat de ontbrekende vertalingen van je handleiding worden toegevoegd, dankzij onze geautomatiseerde vertaalmethode met menselijke controle.


Om verder te gaan met de Pull Request, open je de GitHub Desktop software. De software zou automatisch de wijzigingen moeten detecteren die je lokaal op je branch hebt gemaakt, vergeleken met de originele repository. Voordat je verder gaat, controleer zorgvuldig aan de linkerkant van de interface of deze wijzigingen overeenkomen met wat je verwachtte:


![TUTO](assets/fr/28.webp)


Voeg een titel toe voor je commit, klik dan op de blauwe knop `Commit to [jouw branch]`  om deze wijzigingen te valideren:


![TUTO](assets/fr/29.webp)


Een commit is een opslag van de wijzigingen die in de branch zijn aangebracht, vergezeld van een beschrijvend bericht, waardoor de evolutie van een project in de loop van de tijd gevolgd kan worden. Het is een soort tussentijds controlepunt.


Klik dan op de knop `Push origin`. Dit zal je commit naar je fork sturen:


![TUTO](assets/fr/30.webp)


Als je je tutorial nog niet af hebt, kun je er later op terugkomen en nieuwe commits maken. Als je je wijzigingen voor deze branch hebt voltooid, klik dan nu op de knop `Preview Pull Request`:


![TUTO](assets/fr/31.webp)


Je kunt nog een laatste keer controleren of je wijzigingen correct zijn en dan op de knop `Create pull request` klikken:


![TUTO](assets/fr/32.webp)


Een Pull Request is een verzoek om de wijzigingen van jouw branch te integreren in de hoofdbranch van de Plan ₿ Academy repository, waardoor de wijzigingen bekeken en besproken kunnen worden voordat ze samengevoegd worden.


Je wordt automatisch doorgestuurd naar je browser op GitHub naar de voorbereidingspagina van je Pull Request:


![TUTO](assets/fr/33.webp)

Geef een titel op die kort de wijzigingen samenvat die je wilt samenvoegen met het bronrepository. Voeg een korte opmerking toe die deze wijzigingen beschrijft (als je een issue nummer hebt dat geassocieerd is met het maken van je tutorial, vergeet dan niet om in de opmerking `Closes #{issue nummer}` te vermelden), klik dan op de groene knop `Create pull request` om het samenvoeg verzoek te bevestigen:

![TUTO](assets/fr/34.webp)


Je PR zal dan zichtbaar zijn op het tabblad `Pull Request` van de Plan ₿ Academy repository. Je hoeft alleen maar te wachten tot een beheerder contact met je opneemt om de samenvoeging van je bijdrage te bevestigen of om aanvullende wijzigingen aan te vragen.


![TUTO](assets/fr/35.webp)


Nadat je PR is samengevoegd met de hoofdbranch, wordt het aangeraden om je werkbranch (`tuto-Sparrow-Wallet`) te verwijderen om een schone geschiedenis op je fork te behouden. GitHub zal je deze optie automatisch voorstellen op je PR pagina:


![TUTO](assets/fr/36.webp)


Op de GitHub Desktop software kun je terugschakelen naar de hoofdbranch van je fork (`dev`).


![TUTO](assets/fr/07.webp)


Als je je bijdrage wilt wijzigen nadat je je PR al hebt ingediend, hangt de procedure af van de huidige status van je PR:


- Als je PR nog open is en nog niet samengevoegd, voer de wijzigingen dan lokaal door terwijl je op dezelfde branch blijft. Als de wijzigingen afgerond zijn, gebruik dan de `Push origin` knop om een nieuwe commit toe te voegen aan je nog open PR;
- Als je PR al samengevoegd is met de hoofdbranch, dan moet je het proces opnieuw beginnen door een nieuwe branch aan te maken en dan een nieuw PR in te dienen. Zorg ervoor dat je lokale repository gesynchroniseerd is met de Plan ₿ Academy broncode repository voordat je verder gaat.


Als je technische problemen ondervindt bij het indienen van je tutorial, aarzel dan niet om hulp te vragen op [onze speciale Telegram-groep voor bijdragen](https://t.me/PlanBNetwork_ContentBuilder). Hartelijk dank!
