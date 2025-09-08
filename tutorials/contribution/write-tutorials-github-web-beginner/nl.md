---
name: Bijdrage - GitHub Web tutorial (beginner)
description: Complete gids voor Plan ₿ Network tutorials met GitHub Web
---
![cover](assets/cover.webp)


Voordat je deze tutorial over het toevoegen van een nieuwe tutorial volgt, moet je een paar voorbereidende stappen hebben doorlopen. Als je dat nog niet gedaan hebt, bekijk dan eerst deze inleidende handleiding en kom dan hier terug:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Je hebt al:




- Kies een thema voor je zelfstudie;
- Neem contact op met het Plan ₿ Network team via [Telegram groep](https://t.me/PlanBNetwork_ContentBuilder) of paolo@planb.network ;
- Kies je bijdragehulpmiddelen.


In deze tutorial bekijken we hoe je een tutorial aan Plan ₿ Network kunt toevoegen met de webversie van GitHub. Als je Git al onder de knie hebt, is deze zeer gedetailleerde tutorial misschien niet nodig voor je. In plaats daarvan raad ik je aan om een van deze andere 2 tutorials te bekijken, waar ik de te volgen richtlijnen en de stappen voor het maken van wijzigingen vanaf een lokale:




- Ervaren gebruikers**:


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410


- Intermediair (GitHub Desktop)**:


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## Vereisten


Vereisten voordat u de zelfstudie start:




- Een [GitHub account] hebben (https://github.com/signup);
- Neem een Fork van de [Plan ₿ Network bronopslagplaats] (https://github.com/PlanB-Network/Bitcoin-educational-content);
- Heb [een leraarsprofiel op Plan ₿ Network](https://planb.network/professors) (alleen als je een volledige bijles aanbiedt).


Als je hulp nodig hebt bij het verkrijgen van deze vereisten, kunnen mijn andere tutorials je helpen:



https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.network/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Als alles klaar is en je Fork van de Plan ₿ Network repository hebt, kun je beginnen met het toevoegen van de tutorial.


## 1 - Maak een nieuwe tak


Open je browser en navigeer naar je Fork pagina in de Plan ₿ Network repository. Dit is de Fork die je hebt aangemaakt op GitHub. De URL van je Fork zou er als volgt uit moeten zien: `https://github.com/[jouw-gebruikersnaam]/Bitcoin-onderwijsinhoud`:


![GITHUB](assets/fr/01.webp)


Zorg ervoor dat je op de hoofd `dev` branch zit, klik dan op de "*Sync Fork*" knop. Als je Fork niet up-to-date is, zal GitHub je vragen om je branch bij te werken. Ga verder met deze update:


![GITHUB](assets/fr/02.webp)


Klik op de `dev` tak, noem dan je werktak zo dat de titel duidelijk het doel weergeeft, gebruik streepjes om woorden te scheiden. Bijvoorbeeld, als het ons doel is om een tutorial te schrijven over het gebruik van Green Wallet, dan zou de branch kunnen heten: `tuto-Green-Wallet-loic`. Na het invoeren van een geschikte naam, klik je op "*Create branch*" om het aanmaken van je nieuwe tak op basis van `dev` te bevestigen:


![GITHUB](assets/fr/03.webp)


Je zou nu op je nieuwe tak van werk moeten zijn:


![GITHUB](assets/fr/04.webp)


Dit betekent dat alle wijzigingen die je maakt alleen op die specifieke tak worden opgeslagen.


Maak voor elk nieuw artikel dat je van plan bent te publiceren een nieuwe branch aan van `dev`.


Een branch in Git vertegenwoordigt een parallelle versie van het project, waardoor je aan wijzigingen kunt werken zonder de hoofdbranch te beïnvloeden, totdat je werk klaar is om geïntegreerd te worden.


## 2 - Zelfstudiebestanden toevoegen


Nu de werkende branch is aangemaakt, is het tijd om je nieuwe tutorial te integreren.


Binnen je vertakkingsbestanden moet je de juiste submap vinden voor het plaatsen van je zelfstudie. De organisatie van de mappen weerspiegelt de verschillende secties van de Plan ₿ Network website. In ons voorbeeld, omdat we een zelfstudie toevoegen aan Green Wallet, ga je naar het volgende pad: `Bitcoin-educational-content\tutorialsWallet`, wat overeenkomt met de `Wallet` sectie van de website:


![GITHUB](assets/fr/05.webp)


Maak in de `Wallet` map een nieuwe map aan die specifiek gewijd is aan je tutorial. De naam van deze map moet duidelijk de software aangeven die in de tutorial behandeld wordt, waarbij je koppeltekens gebruikt om woorden te verbinden. In mijn voorbeeld krijgt de map de naam `Green-Wallet`. Klik op "*Add File*" en vervolgens op "*Create new file*":


![GITHUB](assets/fr/06.webp)


Voer de mapnaam in gevolgd door een schuine streep `/` om de aanmaak als map te bevestigen.


![GITHUB](assets/fr/07.webp)


In deze nieuwe submap voor je zelfstudie moet je verschillende items toevoegen:




- Maak een map `assets` aan voor alle illustraties die nodig zijn voor je zelfstudie;
- Maak in deze map `assets` een submap met de naam van de oorspronkelijke taal van de zelfstudie. Als de handleiding bijvoorbeeld in het Engels is geschreven, moet deze submap `en` heten. Plaats al het beeldmateriaal van de handleiding (diagrammen, afbeeldingen, screenshots, enz.) in deze map.
- Een `tutorial.yml` bestand moet worden aangemaakt om de details van je tutorial vast te leggen;
- Er moet een markdown-bestand gemaakt worden om de eigenlijke inhoud van je zelfstudie te schrijven. Dit bestand moet de naam krijgen van de taal waarin het geschreven is. Voor een handleiding in het Frans moet het bestand bijvoorbeeld `fr.md` heten.


Samengevat is dit de hiërarchie van de bestanden (we gaan verder met het maken ervan in de volgende sectie):


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```


## 3 - Vul het YAML-bestand in


Laten we beginnen met het YAML-bestand. Voer in het vak voor het maken van een nieuw bestand `tutorial.yml` in:


![GITHUB](assets/fr/08.webp)


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



- id**: Een UUID (_Universally Unique Identifier_) die de zelfstudie uniek identificeert. Je kunt het generate met behulp van [een online tool] (https://www.uuidgenerator.net/version4). De enige vereiste is dat deze UUID willekeurig is om conflicten met een andere UUID op het platform te vermijden;



- project_id**: De UUID van het bedrijf of de organisatie achter het gereedschap dat in de tutorial wordt gepresenteerd [uit de projectlijst] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Als je bijvoorbeeld een tutorial maakt over de Green Wallet software, kun je deze `project_id` vinden in het volgende bestand: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Deze informatie is toegevoegd aan het YAML-bestand van je tutorial, omdat Plan ₿ Network een database bijhoudt van alle bedrijven en organisaties die werken op Bitcoin of gerelateerde projecten. Door de `project_id` van de entiteit die gelinkt is aan je zelfstudie toe te voegen, creëer je een link tussen de twee Elements;



- tags**: 2 of 3 relevante sleutelwoorden gerelateerd aan de inhoud van de zelfstudie, exclusief gekozen [uit de Plan ₿ Network tag lijst] (https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- categorie**: De subcategorie die overeenkomt met de tutorialinhoud, volgens de Plan ₿ Network websitestructuur (bijvoorbeeld voor wallets: `desktop`, `hardware`, `mobiel`, `backup`);



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


Als je klaar bent met het aanpassen van je `tutorial.yml` bestand, sla dan je document op door te klikken op de "*Wijzigingen vastleggen...*" knop:


![GITHUB](assets/fr/09.webp)


Voeg een titel en beschrijving toe, en zorg ervoor dat de commit wordt gedaan op de branch die je aan het begin van deze tutorial hebt aangemaakt. Bevestig dan door op "*Wijzigingen vastleggen*" te klikken.


![GITHUB](assets/fr/10.webp)


## 4 - Submappen voor afbeeldingen maken


Klik nogmaals op "*Bestand toevoegen*" en vervolgens op "*Nieuw bestand maken*":


![GITHUB](assets/fr/11.webp)


Voer `assets` in gevolgd door een schuine streep `/` om de map aan te maken:


![GITHUB](assets/fr/12.webp)


Herhaal deze stap in de map `/assets` om de submap voor de taal aan te maken, bijvoorbeeld `fr` als je tutorial in het Frans is:


![GITHUB](assets/fr/13.webp)


Maak in deze map een dummy bestand om GitHub te dwingen je map te bewaren (die anders leeg zou zijn). Noem dit bestand `.gitkeep`. Klik dan op "*Commit changes...*".


![GITHUB](assets/fr/14.webp)


Controleer nogmaals of je op de juiste branch zit en klik dan op "*Wijzigingen vastleggen*".


![GITHUB](assets/fr/15.webp)


## 5 - Het Markdown-bestand maken


Nu gaan we het bestand maken dat je tutorial zal hosten, met de naam van je taalcode, bijvoorbeeld `fr.md` als we in het Frans schrijven. Ga naar de tutorial map:


![GITHUB](assets/fr/16.webp)


Klik op "Bestand toevoegen*" en vervolgens op "Nieuw bestand maken*".


![GITHUB](assets/fr/17.webp)


Geef het bestand een naam met je taalcode. In mijn geval, omdat de tutorial in het Frans is geschreven, noem ik mijn bestand `fr.md`. De extensie `.md` geeft aan dat het bestand in Markdown formaat is.


![GITHUB](assets/fr/18.webp)


We beginnen met het invullen van de `Eigenschappen` sectie bovenaan het document. Voeg handmatig het volgende blok code toe en vul het in (de `name:` en `description:` sleutels moeten in het Engels blijven, maar hun waarden moeten worden geschreven in de taal die wordt gebruikt voor je tutorial):


```
---
name: [Titre]
description: [Description]
---
```


![GITHUB](assets/fr/19.webp)


Vul de naam van je tutorial en een korte beschrijving in:


![GITHUB](assets/fr/20.webp)


Voeg dan het pad toe aan de omslagafbeelding aan het begin van je zelfstudie. Om dit te doen, noteer:


```
![cover-green](assets/cover.webp)
```


Deze syntaxis is handig wanneer je een afbeelding moet toevoegen aan je tutorial. Het uitroepteken geeft een afbeelding aan, waarvan de alternatieve tekst (alt) tussen de vierkante haakjes staat. Het pad naar de afbeelding wordt aangegeven tussen de haakjes:


![GITHUB](assets/fr/21.webp)


Klik op de knop "*Wijzigingen vastleggen...*" om dit bestand op te slaan.


![GITHUB](assets/fr/22.webp)


Controleer of je op de juiste branch zit en bevestig dan de commit.


![GITHUB](assets/fr/23.webp)


Je tutorialmap zou er nu zo uit moeten zien, volgens je taalcode:


![GITHUB](assets/fr/24.webp)


## 6 - Logo en omslag toevoegen


In de map `assets` moet je een bestand met de naam `logo.webp` toevoegen, dat zal dienen als thumbnail voor je artikel. Deze afbeelding moet het formaat `.webp` hebben en moet vierkant zijn om overeen te komen met de Interface van de gebruiker.


Je bent vrij om het softwarelogo te kiezen dat in de tutorial wordt gebruikt, of een andere relevante afbeelding, zolang het maar rechtenvrij is. Voeg daarnaast op dezelfde plaats een afbeelding toe met de titel `cover.webp`. Deze wordt bovenaan de handleiding weergegeven. Zorg ervoor dat deze afbeelding, net als het logo, de gebruiksrechten respecteert en geschikt is voor de context van je handleiding.


Om afbeeldingen toe te voegen aan de `/assets` map, kun je ze slepen vanuit je lokale bestanden. Zorg ervoor dat je in de `/assets` map bent en op de juiste branch, klik dan op "*Wijzigingen vastleggen*".


![GITHUB](assets/fr/26.webp)


Je zou nu de afbeeldingen in de map moeten zien verschijnen.


![GITHUB](assets/fr/27.webp)


## 7 - De zelfstudie schrijven


Ga verder met het schrijven van je tutorial door je inhoud te noteren in het Markdown bestand met de taalcode (in mijn voorbeeld, in het Frans, is het het `fr.md` bestand). Ga naar het bestand en klik op het potloodpictogram:


![GITHUB](assets/fr/28.webp)


Begin met het schrijven van je zelfstudie. Als je een ondertitel toevoegt, gebruik dan de juiste Markdown-opmaak door de tekst vooraf te laten gaan door `##`:


![GITHUB](assets/fr/29.webp)


Wissel tussen "*Edit*" en "*Preview*" weergaven om de rendering beter te visualiseren.


![GITHUB](assets/fr/30.webp)


Om je werk op te slaan, klik je op "*Commit Changes...*", controleer je of je op de juiste branch zit en bevestig je door nogmaals op "*Commit Changes*" te klikken.


![GITHUB](assets/fr/31.webp)


## 8 - Visuals toevoegen


De taalsubmap in de map `/assets` (in mijn voorbeeld: `/assets/nl`) wordt gebruikt om de diagrammen en afbeeldingen op te slaan die bij je zelfstudie horen. Vermijd zoveel mogelijk tekst in je afbeeldingen om je inhoud toegankelijk te maken voor een internationaal publiek. Natuurlijk zal de gepresenteerde software tekst bevatten, maar als je schema's of extra aanduidingen toevoegt aan de softwareschermen, doe dit dan zonder tekst of, indien essentieel, gebruik Engels.


Om je afbeeldingen een naam te geven, gebruik je nummers die overeenkomen met de volgorde waarin ze in de zelfstudie voorkomen, geformatteerd als twee cijfers (of drie cijfers als je zelfstudie meer dan 99 afbeeldingen bevat). Bijvoorbeeld, noem je eerste afbeelding `01.webp`, je tweede `02.webp`, enzovoort.


Je afbeeldingen moeten alleen in `.webp` formaat zijn. Indien nodig kun je [mijn beeldconversiesoftware] gebruiken (https://github.com/LoicPandul/ImagesConverter).


![GITHUB](assets/fr/32.webp)


Nu je je afbeeldingen aan de submap hebt toegevoegd, kun je het dummy bestand `.gitkeep` verwijderen. Open dit bestand, klik op de drie kleine puntjes in de rechter bovenhoek, en dan op "*Delete file*".


![GITHUB](assets/fr/33.webp)


Sla je wijzigingen op door te klikken op "*Wijzigingen vastleggen...*".


![GITHUB](assets/fr/34.webp)


Om een diagram uit je submap in te voegen in je redactionele document, gebruik je de volgende Markdown opdracht, waarbij je ervoor zorgt dat je de juiste alternatieve tekst en het juiste afbeeldingspad voor je taal opgeeft:


```
![green](assets/fr/01.webp)
```


Het uitroepteken aan het begin duidt op een afbeelding. De alternatieve tekst, die helpt bij toegankelijkheid en verwijzingen, staat tussen vierkante haakjes. Ten slotte wordt het pad naar de afbeelding tussen haakjes aangegeven.


![GITHUB](assets/fr/35.webp)


Als u uw eigen schema's wilt maken, zorg er dan voor dat u de grafische richtlijnen van Plan ₿ Network volgt om visuele consistentie te garanderen:




- Lettertype**: Gebruik [Rubik] (https://fonts.google.com/specimen/Rubik);
- Kleuren**:
 - Oranje: #FF5C00
 - Zwart: #000000
 - Wit: #FFFFFF


**Het is noodzakelijk dat alle afbeeldingen die je in je tutorials opneemt vrij zijn van copyright of de licentie van het bronbestand respecteren**. Daarom zijn alle diagrammen die gepubliceerd zijn op Plan ₿ Network beschikbaar onder een CC-BY-SA-licentie, op dezelfde manier als de tekst.


**-> Tip:** Wanneer je bestanden in het openbaar deelt, zoals afbeeldingen, is het belangrijk om overbodige metadata te verwijderen. Deze kunnen gevoelige informatie bevatten, zoals locatiegegevens, aanmaakdata en auteurgegevens. Om je privacy te beschermen, is het een goed idee om deze metadata te verwijderen. Om dit te vereenvoudigen, kun je gespecialiseerde tools gebruiken zoals [Exif Cleaner] (https://exifcleaner.com/), waarmee je de metadata van een document kunt opschonen met een simpele drag-and-drop.


## 9 - Stel de zelfstudie voor


Als je klaar bent met het schrijven van je handleiding in de taal van je keuze, is de volgende stap het indienen van een **Trekverzoek**. De beheerder zal dan de ontbrekende vertalingen aan je handleiding toevoegen, met behulp van onze geautomatiseerde vertaalmethode met menselijke proeflezing.


Om door te gaan met de Pull Request, klik je na het opslaan van al je wijzigingen op de knop "*Dragen*" en vervolgens op "*Open pull request*":


![GITHUB](assets/fr/36.webp)


Een Pull Request is een verzoek om wijzigingen van jouw branch te integreren in de hoofdbranch van het Plan ₿ Network repository, waardoor wijzigingen bekeken en besproken kunnen worden voordat ze samengevoegd worden.


Controleer voordat u verdergaat zorgvuldig onderaan de Interface of deze wijzigingen zijn wat u verwachtte:


![GITHUB](assets/fr/37.webp)


Zorg ervoor, bovenaan de Interface, dat je werktak is samengevoegd met de `dev` tak van het Plan ₿ Network repository (dat is de hoofd tak).


Voer een titel in die kort de wijzigingen samenvat die je wilt samenvoegen met het bronrepository. Voeg een korte opmerking toe die deze wijzigingen beschrijft (als je een issue nummer hebt dat geassocieerd is met het maken van je tutorial, vergeet dan niet om `sluit #{issue nummer}` als opmerking te noteren), klik dan op de Green "*Create pull request*" knop om het samenvoeg verzoek te bevestigen:


![GITHUB](assets/fr/38.webp)


Je PR zal dan zichtbaar zijn op het "*Pull Request*" tabblad van het Plan ₿ Network repository. Je hoeft nu alleen nog maar te wachten tot een beheerder contact met je opneemt om te bevestigen dat je bijdrage is samengevoegd, of om verdere wijzigingen aan te vragen.


![GITHUB](assets/fr/39.webp)


Na het samenvoegen van je PR met de hoofdbranch, raden we aan om je werkbranch te verwijderen (in mijn voorbeeld: `tuto-Green-Wallet`) om een schone geschiedenis van je Fork te behouden. GitHub zal je deze optie automatisch aanbieden op je PR pagina:


![GITHUB](assets/fr/40.webp)


Als u wijzigingen wilt aanbrengen in uw bijdrage nadat u uw PR al hebt ingediend, zijn de te volgen stappen afhankelijk van de huidige status van uw PR:




- Als je PR nog open is en nog niet samengevoegd, voer de wijzigingen dan door op dezelfde workbranch. De commit wijzigingen zullen worden toegevoegd aan je nog open PR;
- In het geval dat je PR al samengevoegd is met de hoofdbranch, moet je het proces vanaf het begin overdoen door een nieuwe branch aan te maken en dan een nieuw PR in te dienen. Zorg ervoor dat je Fork gesynchroniseerd is met het Plan ₿ Network bronrepository op de `dev` tak voordat je verder gaat.


Als je technische problemen ondervindt bij het indienen van je tutorial, aarzel dan niet om hulp te vragen op [onze speciale Telegram-groep voor bijdragen](https://t.me/PlanBNetwork_ContentBuilder). Hartelijk dank!