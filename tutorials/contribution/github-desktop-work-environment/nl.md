---
name: GitHub Desktop
description: Hoe stel je je lokale werkomgeving in?
---
![github](assets/cover.webp)


De missie van PlanB is om eersteklas onderwijsmateriaal over Bitcoin in zoveel mogelijk talen aan te bieden. Alle inhoud die op de site wordt gepubliceerd is open-source en wordt gehost op GitHub, waardoor iedereen kan deelnemen aan het verrijken van het platform. Bijdragen kunnen verschillende vormen aannemen: bestaande teksten corrigeren en proeflezen, vertalen naar andere talen, informatie bijwerken of nieuwe tutorials maken die nog niet beschikbaar zijn op onze site.


Als je wilt bijdragen aan het Plan ₿ Academy, moet je GitHub gebruiken om wijzigingen voor te stellen. Hiervoor heb je twee opties:


- **Rechtstreeks bijdragen via GitHub's web interface**: Dit is de eenvoudigste methode. Als je een beginner bent of als je van plan bent om slechts een paar kleine bijdragen te leveren, dan is deze optie waarschijnlijk het beste voor jou;
- **Lokaal bijdragen met Git**: Deze methode is meer geschikt als je van plan bent om regelmatig of veel bij te dragen aan het Plan ₿ Academy. Hoewel het opzetten van je lokale Git omgeving op je computer in eerste instantie complex lijkt, is deze aanpak op de lange termijn efficiënter. Het staat flexibeler beheer van veranderingen toe. Als dit nieuw voor je is, maak je dan geen zorgen, **we leggen het hele proces van het opzetten van je omgeving uit in deze tutorial** (beloofd, je hoeft geen commandoregels te typen ^^).


Als je geen idee hebt wat GitHub is, of als je meer wilt weten over de technische termen die met Git en GitHub te maken hebben, raad ik je aan ons inleidende artikel te lezen om vertrouwd te raken met deze concepten.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c




- Om te beginnen heb je natuurlijk een GitHub account nodig. Als je er al een hebt, kun je inloggen, anders kun je onze tutorial gebruiken om een nieuwe aan te maken.


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



## Stap 1: Installeer GitHub Desktop



- Ga naar https://desktop.github.com/ om de GitHub Desktop software te downloaden. Met deze software kun je eenvoudig communiceren met GitHub, zonder een terminal te hoeven gebruiken:

![github-desktop](assets/1.webp)


- Als je de software voor het eerst start, wordt je gevraagd om je GitHub account te verbinden. Om dit te doen, klik je op `Sign in to GitHub.com`:

![github-desktop](assets/2.webp)


- Er wordt een verificatiepagina geopend in je browser. Voer je e-mailadres en wachtwoord in dat je hebt gekozen bij het aanmaken van je account en klik vervolgens op de knop `Sign in` (Aanmelden):

![github-desktop](assets/3.webp)


- Klik op `Authorize desktop` om de verbinding tussen je account en de software te bevestigen:

![github-desktop](assets/4.webp)


- Je wordt automatisch doorgestuurd naar de GitHub Desktop software. Klik op `Finish`:
![github-desktop](assets/5.webp)

- Als je net je GitHub account aangemaakt hebt, zul je doorgestuurd worden naar een pagina die aangeeft dat je nog geen repositories aangemaakt hebt. Zet op dit punt de GitHub Desktop software opzij; we komen er later op terug:
![github-desktop](assets/6.webp)


## Stap 2: Obsidian installeren


Laten we verder gaan met het installeren van de schrijfsoftware. Hier heb je verschillende opties. Je hebt software nodig die Markdown-bestanden kan bewerken, omdat Plan ₿ Academy dit formaat gebruikt voor tekstbestanden in zijn repository.


Er is een veelheid aan software die gespecialiseerd is in het bewerken van Markdown-bestanden, zoals Typora, speciaal ontworpen om te schrijven. Hoewel het niet ideaal is, kun je ook kiezen voor een code editor, zoals Visual Studio Code (VSC) of Sublime Text. Als schrijver gebruik ik echter liever de Obsidian software. Laten we samen kijken hoe je het installeert en ermee aan de slag gaat.



- Ga naar https://obsidian.md/download en download de software:
![github-desktop](assets/7.webp)

- Installeer Obsidian, start de software, kies je taal en klik vervolgens op `Quick Start`:
![github-desktop](assets/8.webp)

- Je komt aan bij de Obsidian software. Op dit moment zijn er geen bestanden geopend:
![github-desktop](assets/9.webp)


## Stap 3: Fork de Plan ₿ Academy repository



- Ga naar de data repository van het Plan ₿ Academy op de volgende Address: [https://github.com/PlanB-Network/Bitcoin-educational-content](https://github.com/PlanB-Network/Bitcoin-educational-content):
![github-desktop](assets/10.webp)

- Klik op deze pagina op de knop `Fork` rechtsboven in het venster:
![github-desktop](assets/11.webp)

- In het creatiemenu kun je de standaardinstellingen laten staan. Zorg ervoor dat het `Copy the dev branch only` (Kopieer alleen de dev branch) vakje aangevinkt is, klik dan op de knop `Create fork` (Maak fork):
![github-desktop](assets/12.webp)

- Je komt dan uit bij je eigen fork van de Plan ₿ Academy repository:
![github-desktop](assets/13.webp)

Deze fork vormt een aparte repository van het origineel, hoewel het op dit moment dezelfde gegevens bevat. Je gaat nu aan deze nieuwe repository werken.


We hebben in zekere zin een kopie gemaakt van de Plan ₿ Academy bron repository. Jouw fork (de kopie) en het originele archief zullen nu onafhankelijk van elkaar evolueren. Op het originele archief kunnen andere bijdragers nieuwe gegevens toevoegen, terwijl jij, op jouw fork, verder gaat met je eigen aanpassingen.

Om de consistentie tussen deze twee repositories te behouden, is het nodig om ze periodiek te synchroniseren, zodat ze dezelfde informatie ophalen. Om je wijzigingen naar het bronrepository te sturen, gebruik je een zogenaamd **Pull Request**. En om veranderingen van de bronrepository in je fork te integreren, gebruik je het **Sync Fork** commando, beschikbaar in de GitHub web interface.

![github-desktop](assets/14.webp)


## Stap 4: Kloon de fork



- Ga terug naar de GitHub Desktop software. Nu zou je fork moeten verschijnen in de `Your repositories` sectie. Als je het niet meteen ziet, gebruik dan de dubbele pijlknop om de lijst te verversen. Als je fork verschijnt, klik er dan op om het te selecteren:

![github-desktop](assets/15.webp)


- Klik dan op de blauwe knop: `Clone [username]/Bitcoin-educational-content`:

![github-desktop](assets/16.webp)


- Houd het standaardpad aan. Klik op de blauwe knop `Clone` om te bevestigen:

![github-desktop](assets/17.webp)


- Wacht terwijl GitHub Desktop je fork lokaal kloont:

![github-desktop](assets/18.webp)


- Na het klonen van de repository biedt de software je twee opties. Je moet de eerste selecteren: `To contribute to the parent project`. Met deze keuze kun je je toekomstige werk presenteren als een bijdrage aan het bovenliggende project (`Plan ₿ Academy/Bitcoin-educational-content`), en niet uitsluitend als een aanpassing van je persoonlijke fork (`[username]/Bitcoin-educational-content`). Als de optie is gekozen, klik dan op `Continue` (Doorgaan):

![github-desktop](assets/19.webp)


- Je GitHub Desktop is nu correct geconfigureerd. Nu kun je de software op de achtergrond open laten staan om de wijzigingen die we zullen maken te volgen.

![github-desktop](assets/20.webp)

Wat we in dit stadium bereikt hebben is het maken van een lokale kopie van je repository, die gehost wordt op GitHub. Ter herinnering, deze repository is een fork van de bronrepository van Plan ₿ Academy. Je zult in staat zijn om wijzigingen aan te brengen in deze lokale kopie, zoals het toevoegen van tutorials, vertalingen of correcties. Zodra deze wijzigingen gemaakt zijn, zul je het **Push origin** commando gebruiken om je lokale wijzigingen naar je fork gehost op GitHub te sturen.


Je kunt ook wijzigingen ophalen van de fork, bijvoorbeeld tijdens een synchronisatie met de Plan ₿ Academy repository. Hiervoor gebruik je het **Fetch origin** commando om de wijzigingen te downloaden naar je lokale kopie (je kloon), en dan het **Pull origin** commando om ze samen te voegen met je werk. Hierdoor kun je op de hoogte blijven van de laatste ontwikkelingen van het project terwijl je effectief bijdraagt.


![github-desktop](assets/21.webp)

## Stap 5: Maak een nieuwe Obsidian-kluis aan



- Open de Obsidian-software en klik op het kleine kluispictogram linksonder in het venster:

![github-desktop](assets/22.webp)


- Klik op de knop `Openen` om een bestaande map als kluis te openen: ![github-desktop](assets/23.webp)
- Je bestandsverkenner wordt geopend. Je moet de map met de titel `GitHub` vinden en selecteren, die in je `Documents` map zou moeten staan tussen je bestanden. Dit pad komt overeen met het pad dat je tijdens stap 4 hebt gemaakt. Nadat je de map hebt gekozen, bevestig je de selectie. De creatie van je kluis op Obsidian zal dan starten op een nieuwe pagina van de software:


![github-desktop](assets/24.webp)

-> Let op, het is belangrijk om niet de `Bitcoin-educational-content` map te kiezen bij het aanmaken van een nieuwe kluis in Obsidian. Selecteer in plaats daarvan de bovenliggende map, `GitHub`. Als je de `Bitcoin-educational-content` map selecteert, wordt de configuratiemap `.obsidian`, met daarin je lokale Obsidian instellingen, automatisch geïntegreerd in de repository. We willen dit vermijden, omdat het niet nodig is om je Obsidian configuraties over te zetten naar de Plan ₿ Academy repository. Een alternatief is om de `.obsidian` map aan het `.gitignore` bestand toe te voegen, maar deze methode zou ook het `.gitignore` bestand van de bronrepository aanpassen, wat niet wenselijk is.



- Aan de linkerkant van het venster zie je de bestandsstructuur met je verschillende GitHub repositories die lokaal gekloond zijn.
- Door op de pijltjes naast de mapnamen te klikken, kun je ze uitvouwen om toegang te krijgen tot de submappen van de repositories en hun documenten:

![github-desktop](assets/25.webp)


- Vergeet niet om Obsidian in te stellen op de donkere modus: "Licht trekt bugs (insecten) aan" ;)


## Stap 6: Een code-editor installeren


De meeste van je wijzigingen zullen plaatsvinden in bestanden in Markdown formaat (`.md`). Om deze documenten te bewerken kun je Obsidian gebruiken, de software die we eerder hebben besproken. Plan ₿ Academy gebruikt echter andere bestandsformaten en je zult sommige van deze moeten aanpassen.


Als je bijvoorbeeld een nieuwe tutorial aanmaakt, moet je een YAML-bestand (`.yml`) maken om de tags in je tutorial, de titel en je leraar-ID in te voeren. Obsidian biedt niet de mogelijkheid om dit soort bestanden aan te passen, dus je zal een code editor nodig hebben.


Hiervoor zijn verschillende opties beschikbaar. Hoewel de standaard kladblok van je computer gebruikt kan worden voor deze aanpassingen, is deze oplossing niet ideaal voor netjes werk. Ik raad aan om software te kiezen die speciaal voor dit doel is ontworpen, zoals [VS Code](https://code.visualstudio.com/download) of [Sublime Text](https://www.sublimetext.com/download). Sublime Text is bijzonder licht en zal meer dan voldoende zijn voor onze behoeften.


- Installeer een van deze softwareprogramma's en houd het apart voor toekomstige aanpassingen.
![github-desktop](assets/26.webp)

Gefeliciteerd! Je werkomgeving is nu ingesteld om bij te dragen aan Plan ₿ Academy. Je kunt nu onze andere specifieke tutorials verkennen voor elk type bijdrage (vertalen, proeflezen, schrijven).


https://planb.academy/tutorials/contribution

..).
