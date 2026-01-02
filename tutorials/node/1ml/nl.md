---
name: 1ML
description: Leer hoe je de 1ML verkenner kunt gebruiken om het Lightning netwerk van Bitcoin te begrijpen en te analyseren.
---
![cover](assets/cover.webp)



## Inleiding



Lightning Network is een snelle, goedkope betalingsoplossing die bovenop Bitcoin is gebouwd en directe, veilige transacties mogelijk maakt. Het observeren van dit netwerk is essentieel om te begrijpen hoe het werkt, de topologie en de status van de knooppunten waaruit het bestaat. Een Lightning-verkenner, zoals 1ML, wordt gebruikt om de openbare gegevens van het netwerk te visualiseren, inclusief actieve knooppunten, open kanalen en beschikbare capaciteit, wat een waardevol overzicht biedt voor gebruikers, ontwikkelaars en knooppuntbeheerders.



## Ga naar 1ML en begrijp de startpagina



Om toegang te krijgen tot 1ML, open je gewoon je webbrowser en typ je [https://1ml.com](https://1ml.com) in. Dit brengt je naar de startpagina, die dienst doet als het globale dashboard van de Lightning Network.



![capture](assets/fr/03.webp)



Deze pagina toont verschillende belangrijke statistieken bovenaan het scherm, waaronder :





- Het **totaal aantal actieve nodes** op het netwerk, d.w.z. de computers die betrokken zijn bij het verzenden en ontvangen van Lightning-betalingen.
- Het **aantal open kanalen**, die overeenkomen met de verbindingen tussen deze knooppunten waardoor geldoverdrachten mogelijk zijn.
- De **totale netwerkcapaciteit**, uitgedrukt in bitcoin (BTC), die de som aangeeft van de capaciteiten van alle publieke kanalen.



Deze cijfers worden regelmatig bijgewerkt om de huidige staat van het netwerk weer te geven. Ze geven een idee van de omvang, groei en robuustheid van het netwerk.



![capture](assets/fr/04.webp)



Net daaronder biedt de pagina lijsten met ranglijsten:





- De **meest verbonden knooppunten**, die de meeste open kanalen naar andere knooppunten hebben.
- De **hoogste capaciteiten** op de knooppunten, die aangeven welke knooppunten de grootste hoeveelheden kunnen overdragen.
- De belangrijkste kanalen in termen van capaciteit.



Er kunnen ook filters worden gebruikt om deze lijsten te verfijnen op geografische locatie of andere criteria.



Deze pagina is een ideaal startpunt om Lightning Network te verkennen en de algemene topologie ervan te begrijpen.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Lightning-knooppunten verkennen



Om een knooppunt op 1ML te verkennen, gebruik je de zoekbalk bovenaan de pagina. Je kunt de **Node ID** invoeren, de unieke identificatie van het knooppunt, of de **alias**, wat een gemakkelijker te onthouden naam is.



Zodra het zoeken is voltooid, klik je op het bijbehorende knooppunt om de detailpagina te openen.



![capture](assets/fr/07.webp)



Op deze pagina worden verschillende belangrijke gegevens weergegeven:





- Node ID**: deze unieke identificatie is een lange reeks karakters waarmee het knooppunt nauwkeurig geïdentificeerd kan worden in het hele netwerk.



![capture](assets/fr/08.webp)





- Alias**: dit is de naam die de eigenaar van het knooppunt kiest om het knooppunt publiekelijk weer te geven.



![capture](assets/fr/09.webp)





- Het **aantal kanalen** geeft aan hoeveel verbindingen het knooppunt heeft met andere knooppunten, terwijl de **totale capaciteit** de som van de bitcoins weergeeft die beschikbaar zijn in deze kanalen. Een knooppunt met een groot aantal kanalen en een hoge capaciteit is over het algemeen goed verbonden en in staat om snel grote hoeveelheden geld over het netwerk te versturen.



![capture](assets/fr/10.webp)





- De **uptime**, of beschikbaarheid, geeft aan hoe lang een node actief en online toegankelijk is gebleven, wat de betrouwbaarheid weergeeft. De **leeftijd** van het knooppunt daarentegen geeft aan hoe lang het al op het netwerk aanwezig is, wat de stabiliteit en ervaring binnen Lightning Network weergeeft.



![capture](assets/fr/11.webp)



Deze gegevens helpen je het belang en de betrouwbaarheid van een node in Lightning Network te begrijpen. Een knooppunt met een groot aantal kanalen, een hoge capaciteit en een hoge uptime is bijvoorbeeld vaak een belangrijke speler in het netwerk.



## Bliksemkanalen verkennen



### Wat is een Lightning-kanaal?



Een Lightning-kanaal is een directe verbinding tussen twee netwerkknooppunten. Het stelt deze twee knooppunten in staat om directe, goedkope betalingen uit te wisselen zonder voor elke transactie door de Bitcoin hoofdketen te gaan. Kanalen zijn de basis die Lightning Network snel en schaalbaar maken.



### Lees kanaalinformatie op 1ML



Op 1ML heeft elk kanaal een eigen pagina of beschrijvingsblad met een aantal belangrijke gegevens:



Vanaf de pagina van een knooppunt kun je een lijst met kanalen openen. Als je op een kanaal klikt, geeft 1ML een speciale pagina weer met belangrijke informatie.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



De belangrijkste zichtbare gegevens zijn als volgt:





- Partner nodes**: elk kanaal verbindt twee nodes. 1ML geeft beide identifiers en hun respectieve aliassen weer.



![capture](assets/fr/14.webp)





- Kanaalcapaciteit**: Dit is het totale aantal bitcoins dat in dit kanaal is vergrendeld. Deze capaciteit vertegenwoordigt de maximale limiet van betalingen die door dit kanaal kunnen gaan.



![capture](assets/fr/15.webp)





- Leeftijd kanaal**: geeft aan hoe lang het kanaal al open is. Een oud kanaal is vaak een teken van een stabiele relatie tussen twee knooppunten.



![capture](assets/fr/16.webp)



### Zichtbaarheidsbeperkingen kanaal



Het is belangrijk om te begrijpen dat 1ML alleen **een deel** van Lightning Network laat zien. De verkenner toont alleen **publieke kanalen**, d.w.z. kanalen die zijn aangekondigd op het netwerk. Privé-kanalen, die vaak om redenen van vertrouwelijkheid of strategie worden gebruikt, zijn niet zichtbaar. Bovendien toont 1ML niet de exacte verdeling van fondsen aan elke kant van een kanaal, noch de betalingen die zijn gedaan, noch de liquiditeit die op een bepaald moment daadwerkelijk beschikbaar is. De weergegeven informatie kan daarom worden gebruikt om de algemene structuur van het netwerk** te analyseren, maar niet de daadwerkelijke financiële activiteit of gedetailleerde liquiditeitsstatus.



## Verken Lightning Network per locatie



### Knooppunten per land en regio



met 1ML kun je Lightning Network verkennen volgens een **geografische indeling**. Vanaf de startpagina of via speciale secties is het mogelijk om knooppunten per land of regio weer te geven. Deze functie is gebaseerd op locatie-informatie die is opgegeven door knooppuntbeheerders.


In de navigatiebalk zie je de link **Locatie**. Op de pagina zijn de knooppunten gegroepeerd per continent, land en stad.



![capture](assets/fr/17.webp)



Door een land te selecteren toont 1ML een lijst met bijbehorende knooppunten, samen met geaggregeerde statistieken zoals het aantal knooppunten en de totale zichtbare capaciteit voor dat geografische gebied.



#### Wat dit zegt over lokale adoptie





- Technologie adoptie**: Een groot aantal knooppunten in een regio geeft aan dat Bitcoin gebruikers, bedrijven of diensten actief Lightning Network adopteren. Dit duidt op technologische volwassenheid en een bereidheid om te profiteren van de voordelen van Lightning (snelle transacties, lagere kosten).
- Economisch ecosysteem** : De dichte aanwezigheid van knooppunten kan ook wijzen op een lokaal economisch weefsel rond Bitcoin: handelaars die Lightning accepteren, startups die tools ontwikkelen, gemeenschapsevenementen, enz.
- Veiligheid en veerkracht**: Een diverse geografische spreiding vergroot de veerkracht van het netwerk bij lokale uitval of beperkingen. Hoe meer de nodes verspreid zijn, hoe decentraler en moeilijker het netwerk te censureren is.
- Beleid en regelgeving**: Sommige landen zullen sneller overstappen dankzij een gunstig regelgevend kader of een proactieve gemeenschap. Omgekeerd zal het aantal nodes lager zijn in gebieden waar de regelgeving streng of vijandig is.



#### Grenzen van geografische gegevens



Houd er echter rekening mee dat de geolocatie van Lightning-knooppunten zijn beperkingen en vooroordelen heeft:





- Geschatte IP-locatie**: 1ML gebruikt over het algemeen het openbare IP-adres van nodes om hun locatie te schatten. Deze methode kan echter worden verstoord door het gebruik van VPN's, cloudservers (AWS, Google Cloud) of hosting in landen die verschillen van de werkelijke woonplaats van de eigenaar van het knooppunt.
- Virtuele nodes**: Sommige operators hosten hun nodes om redenen van betrouwbaarheid en beschikbaarheid op externe servers, wat een vals gevoel van fysieke locatie kan geven.
- Mobiliteit van gebruikers**: Een exploitant van een knooppunt kan van locatie veranderen, zijn infrastructuur verplaatsen of meerdere knooppunten in verschillende regio's openen, waardoor het lezen van gegevens complexer wordt.
- Onzichtbaarheid van privéknooppunten**: Sommige nodes publiceren hun IP-adres niet of gebruiken methoden om hun locatie te verbergen, waardoor geolocatie onmogelijk wordt.



## 1ML concrete gebruikssituaties



### Netwerktopologie begrijpen



met 1ML kun je de algemene structuur van Lightning Network** visualiseren. Door de verbindingen tussen knooppunten, het aantal kanalen en de totale capaciteit te bekijken, kun je begrijpen hoe het netwerk is georganiseerd, welke knooppunten een centrale rol spelen en hoe betalingsstromen theoretisch kunnen circuleren.



Dit begrip is essentieel als we willen begrijpen hoe de Lightning Network werkt, en niet alleen voor portefeuillegebruik.



### Identificeer belangrijke knooppunten



Dankzij de ranglijsten die 1ML aanbiedt (meest verbonden knooppunten, hoogste capaciteit, leeftijd), is het mogelijk om de knooppunten te identificeren die een belangrijke plaats innemen in het netwerk. Deze knooppunten dienen vaak als belangrijke gateways voor Lightning-betalingen.



![capture](assets/fr/18.webp)



### De publieke zichtbaarheid van een knooppunt controleren



Voor een node operator kun je met 1ML controleren of je node **publiekelijk geadverteerd** is op Lightning Network. Als een knooppunt op 1ML verschijnt, betekent dit dat het zichtbaar en toegankelijk is voor andere knooppunten voor het openen van openbare kanalen.


Dit kan handig zijn voor het diagnosticeren van zichtbaarheids- of connectiviteitsproblemen.



### Lightning Network in de loop der tijd zien evolueren



Door globale statistieken over verschillende periodes te vergelijken, stelt 1ML ons in staat om de evolutie van Lightning Network te observeren: toename of afname van het aantal knooppunten, variaties in de totale capaciteit of veranderingen in de geografische spreiding.


Deze observaties bieden een interessant perspectief op de groei, volwassenheid en trends van Lightning Network.



## 1ML best practices en beperkingen



### Openbare gegevens ≠ volledige realiteit



1ML is uitsluitend gebaseerd op de **publiekelijk aangekondigde** gegevens over Lightning Network. Dit betekent dat de tool slechts een deel van de werkelijkheid laat zien. Veel kanalen kunnen privé zijn, sommige knooppunten worden niet geadverteerd en de werkelijke liquiditeit die beschikbaar is in kanalen is niet zichtbaar. Het is daarom essentieel om 1ML te gebruiken als een globaal analyse-instrument, niet als een volledige weergave van het netwerk.



### Privacy en bliksem



Lightning Network is ontworpen met een sterke focus op **betalingsprivacy**. Individuele transacties zijn niet zichtbaar op 1ML en exacte kanaalsaldi zijn niet openbaar. Deze beperking is geen fout van de explorer, maar een fundamentele functie van Lightning Network, ontworpen om de privacy van gebruikers te beschermen.



### Trek niet te snel conclusies



Een knooppunt met een hoge capaciteit of veel kanalen is niet noodzakelijk in alle gevallen "betrouwbaarder" of "efficiënter". Evenzo betekent een tijdelijke daling van de totale netwerkcapaciteit niet noodzakelijkerwijs dat er een structureel probleem is. Cijfers moeten altijd achteraf worden geïnterpreteerd en in de juiste context worden geplaatst.



### Complementariteit met andere tools



1ML is een uitstekend startpunt voor het verkennen van Lightning Network, maar het kan het beste gebruikt worden in combinatie met andere tools zoals Lightning portfolio's, node management interfaces en andere explorers. Deze aanpak geeft een completer en genuanceerder beeld van het netwerk.



## 1ML aansluitoptie (geavanceerde functionaliteit)



1ML biedt een **inlog / maak account** optie, zichtbaar op de site, maar dit is **niet noodzakelijk** om Lightning Network gegevens te bekijken. Alle functies die tot nu toe in deze tutorial zijn besproken, zijn beschikbaar **zonder account**.



De verbinding is primair gericht op **Lightning node operators**. Het maakt het met name mogelijk om een knooppunt te koppelen aan een 1ML-account om bepaalde openbare informatie te beheren, zoals de presentatie van het knooppunt, contactkoppelingen en andere metagegevens. Deze functie is ontworpen om de zichtbaarheid en identificatie van een knooppunt in de verkenner te verbeteren.



Het is belangrijk op te merken dat 1ML **geen bewaarservice** is. Het aanmaken van een account geeft geen toegang tot fondsen, kanalen of betalingen van een knooppunt. Het dient alleen voor interactie met de explorer vanuit een declaratief en informatief oogpunt.



In de context van het leren of ontdekken van de Lightning Network, kan deze optie daarom worden beschouwd als **optioneel** en gereserveerd voor meer gevorderd gebruik.



## Conclusie



1ML is een waardevol hulpmiddel voor het observeren en begrijpen van Lightning Network op basis van openbare gegevens. Het laat je de structuur van het netwerk verkennen, knooppunten en kanalen analyseren en de algemene evolutie van Lightning Network adoptie in de loop van de tijd volgen. Zonder de noodzaak van een account of het omgaan met geld, biedt 1ML een toegankelijke toegangspoort voor iedereen die zijn begrip van de werking van Lightning wil verdiepen.


Als je verder wilt gaan met de Lightning Network, raad ik je de complete Inleiding tot Lightning Network cursus aan:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb