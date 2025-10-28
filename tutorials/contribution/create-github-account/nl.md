---
name: GitHub account
description: Hoe maak je je eigen account op GitHub?
---

![cover](assets/cover.webp)


De missie van Plan ₿ is om eersteklas educatieve bronnen over Bitcoin aan te bieden, beschikbaar in zoveel mogelijk talen. Alle inhoud die op de site wordt gepubliceerd is open-source en wordt gehost op GitHub, waardoor iedereen de kans krijgt om bij te dragen aan de verrijking van het platform. Bijdragen kunnen verschillende vormen aannemen: het corrigeren en proeflezen van bestaande teksten, vertalingen in andere talen, het bijwerken van informatie of het creëren van nieuwe tutorials die nog niet beschikbaar zijn op onze site.


Als je wilt bijdragen aan Plan ₿ Network, zul je Git en GitHub moeten gebruiken, dus, als deze tools onbekend voor je zijn of als hun werking onduidelijk lijkt, geen paniek, dit artikel is voor jou! We zullen samen de basisprincipes van Git en GitHub doornemen, evenals het bijbehorende technische jargon, zodat je ze daarna effectief kunt gebruiken.


## Wat is Git?


Git is een versiebeheersysteem, speciaal ontworpen om softwareprojecten te beheren. Git is in 2005 gecreëerd door Linus Torvalds en is snel de standaard geworden in de softwareontwikkelingsindustrie voor versiebeheer. Maar wat houdt het precies in?

![git](assets/11.webp)

In de kern stelt Git ontwikkelaars in staat om veranderingen in de broncode van een project in de loop van de tijd bij te houden. Dit betekent dat Git bij elke wijziging in de code een nieuwe versie van het project vastlegt. Als er een fout optreedt of als een experimentele functie niet werkt zoals verwacht, is het mogelijk om terug te gaan naar een eerdere staat van de code, als een soort tijdmachine, maar dan voor bestanden.


Een van de belangrijkste functies van Git is branch management. Een branch is een soort parallelle lijn waar ontwikkelaars onafhankelijk van de rest van het project kunnen werken. Dit vergemakkelijkt het toevoegen van nieuwe functies of het corrigeren van bugs enorm zonder de hoofdcode te verstoren. Zodra de wijzigingen getest en gevalideerd zijn, kunnen ze samengevoegd worden met de hoofdbranch.


Een van de bijzonderheden van Git is de mogelijkheid om gedistribueerd te werken. Elke ontwikkelaar heeft een complete kopie van het project op de harde schijf van zijn eigen computer, waardoor ze offline kunnen werken en wijzigingen later kunnen samenvoegen als er een internetverbinding beschikbaar is. Dit vermindert het risico op conflicten en staat meerdere ontwikkelaars toe om tegelijkertijd aan hetzelfde project te werken zonder op elkaars tenen te trappen.

Git is in eerste instantie vooral ontworpen voor softwareontwikkelingsprojecten. Het kan echter ook gebruikt worden om projecten voor het schrijven van inhoud te beheren. In plaats van samen te werken aan code, werken we samen aan tekst. En het is precies deze methode die Plan ₿ Network gebruikt om haar inhoud te beheren! Git vergemakkelijkt de samenwerking bij het schrijven van cursussen en tutorials, omdat het het nauwkeurig bijhouden van wijzigingen en efficiënt versiebeheer mogelijk maakt, evenals het beoordelen en verbeteren van inhoud door andere bijdragers.


## Wat is GitHub?


GitHub is een broncodebeheer- en hostingplatform gebaseerd op het versiebeheersysteem Git dat we zojuist hebben besproken. GitHub, gelanceerd in 2008, won snel aan populariteit en is een essentiële referentie geworden voor ontwikkelaars wereldwijd. Maar waarin verschilt GitHub van Git, en waarom is het zo cruciaal in onze methode voor het produceren van content?

![github](assets/12.webp)

Allereerst is het belangrijk om te begrijpen dat GitHub is gebouwd op Git (wat we in het vorige gedeelte hebben besproken). Terwijl Git de tool is die veranderingen in de code bijhoudt, is GitHub de online service die deze code host, deelt en beheert.


Stel je Git voor als een soort logboek dat elke ontwikkelaar op zijn eigen computer gebruikt om alle wijzigingen in zijn project op te slaan. GitHub, aan de andere kant, is als een openbare bibliotheek waar al deze logboeken gedeeld, vergeleken en gecombineerd kunnen worden.


Het fundamentele verschil tussen Git en GitHub ligt in hun functie: Git is de tool die elke ontwikkelaar lokaal gebruikt om hun codeversies te beheren, terwijl GitHub het online platform is dat deze versies host en samenwerking vergemakkelijkt.


GitHub is veel meer dan alleen een service voor het hosten van code. Het is een samenwerkingsplatform dat ontwikkelaars in staat stelt om efficiënt samen te werken. En inderdaad, Plan ₿ Network gebruikt dit platform niet alleen om alle code te hosten die de website aandrijft, maar ook, en dit is wat ons interesseert, alle inhoud (tutorials, training, bronnen...).


## Enkele technische termen


Op Git en GitHub zul je commando's en functies tegenkomen waarvan de namen ingewikkeld lijken. In dit laatste deel zal ik wat eenvoudige definities geven om de technische termen te begrijpen die je tegen kunt komen als je Git en GitHub gebruikt:



- **Fetch origin:** Commando dat recente informatie en wijzigingen van een remote repository ophaalt zonder ze samen te voegen met je lokale werk. Het werkt je lokale repository bij met nieuwe branches en commits die aanwezig zijn in de remote repository.



- **Pull origin:** Commando dat updates ophaalt van een remote repository en deze direct integreert in je lokale branch om deze te synchroniseren. Dit combineert de stappen van fetch en merge in een enkel commando.
- **Sync Fork:** Een functie op GitHub waarmee je je fork van een project kunt bijwerken met de laatste wijzigingen uit de bronrepository. Dit zorgt ervoor dat jouw kopie van het project up-to-date blijft met de hoofdontwikkeling.
- **Push origin:** Commando om je lokale wijzigingen naar een remote repository te sturen.



- **Pull Request:** Een verzoek gestuurd door een bijdrager om aan te geven dat ze wijzigingen naar een branch in een remote repository hebben gepushed en dat ze willen dat deze wijzigingen worden bekeken en mogelijk worden samengevoegd in de hoofdbranch van de repository.



- **Commit:** Je wijzigingen opslaan. Een commit is als een momentopname van je werk op een bepaald moment, waarmee je een geschiedenis van wijzigingen kunt bijhouden. Elke commit bevat een beschrijvende boodschap die uitlegt wat er gewijzigd is.



- **Branch:** Een parallelle versie van de repository, waarmee je aan wijzigingen kunt werken zonder de hoofd branch (vaak "main" of "master" genoemd) te beïnvloeden. Branches faciliteren de ontwikkeling van nieuwe functies en de correctie van bugs zonder het risico te lopen om stabiele code te verstoren.



- **Merge:** Merging (samenvoegen) bestaat uit het integreren van de wijzigingen van de ene branch in de andere. Het wordt bijvoorbeeld gebruikt om de wijzigingen van een werk branch toe te voegen aan de hoofd branch, waardoor de verschillende bijdragen toegevoegd kunnen worden.



- **Fork:** Forken van een repository betekent een kopie maken van dat repository op je eigen GitHub account, waarmee je aan het project kunt werken zonder het originele repository te beïnvloeden. De fork kan zijn eigen weg gaan en een ander project worden los van het origineel, of het kan regelmatig synchroniseren met het originele project om eraan bij te dragen.



- **Clone:** Een repository klonen betekent dat je een lokale kopie op je computer maakt, die je toegang geeft tot alle bestanden en de geschiedenis. Hierdoor kun je direct lokaal aan het project werken.



- **Repository:** Opslagruimte voor een project op GitHub. Een repository bevat alle projectbestanden en ook de geschiedenis van alle wijzigingen die eraan gemaakt zijn. Het is de basis van opslag en samenwerking op GitHub.



- **Issue:** Een tool voor het bijhouden van taken en bugs op GitHub. Met issues kun je problemen melden, verbeteringen voorstellen of nieuwe functies bespreken. Elk issue kan worden toegewezen, gelabeld en becommentarieerd.


Deze lijst is natuurlijk niet volledig. Er zijn veel andere technische termen die specifiek zijn voor Git en GitHub. Maar degene die hier genoemd zijn, zijn de belangrijkste die je vaak zult tegenkomen.


Na het lezen van dit artikel is het mogelijk dat sommige aspecten van Git en GitHub nog onduidelijk voor je zijn, dus moedig ik je aan om deze tools zelf te gaan gebruiken. Oefening baart vaak de meeste opzien! En om te beginnen kun je deze 2 andere tutorials ontdekken:


## Hoe een GitHub account aanmaken


Als je wilt bijdragen aan het PlanB Network, heb je een GitHub account nodig. In deze tutorial zullen we je stap voor stap begeleiden bij het aanmaken, instellen en goed beveiligen van je eigen account.



- Ga naar [https://github.com/signup](https://github.com/signup).
- Voer je e-mail adres in en klik dan op de groene knop `Continue` (Doorgaan):

![github](assets/1.webp)


- Kies een sterk wachtwoord en klik op de groene knop `Continue` (Doorgaan):

![github](assets/12.webp)


- Kies vervolgens je gebruikersnaam. Je kunt je echte identiteit onthullen of een pseudoniem gebruiken. Klik dan op de groene knop `Continue` (Doorgaan):

![github](assets/3.webp)


- Voltooi de Captcha:

![github](assets/4.webp)


- Je ontvangt een e-mail met een bevestigingscode die je moet invoeren om het aanmaken van je account te voltooien:

![github](assets/5.webp)


- Vul de vragen in als je wilt dat GitHub je naar bepaalde tools leidt, of klik op `skip personalization` om over te slaan:

![github](assets/6.webp)


- Kies het gratis plan door te klikken op de knop `Continue for free` (Gratis verder):

![github](assets/7.webp)


- Je wordt dan doorverwezen naar je dashboard.
- Als je wilt, kun je je account aanpassen door op je profielfoto rechtsboven in het scherm te klikken en vervolgens naar het menu `Settings` (Instellingen) te gaan:

![github](assets/8.webp)


- In dit gedeelte heb je de mogelijkheid om een nieuwe profielfoto toe te voegen, een naam te kiezen, je biografie aan te passen of een link naar je persoonlijke website toe te voegen:

![github](assets/9.webp)


- Ik raad ook aan om naar het menu `Password and authentication` (Wachtwoord en verificatie) te gaan om op zijn minst tweefactorauthenticatie in te stellen:

![github](assets/10.webp)
