---
name: Pi-Hole
description: Een advertentieblokker voor je hele netwerk
---
![cover](assets/cover.webp)



___



*Deze zelfstudie is gebaseerd op originele inhoud van Florian Duchemin gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er kunnen wijzigingen zijn aangebracht in de oorspronkelijke tekst.*



___



## I. Presentatie



We hebben het allemaal wel eens gedaan zodra we onze favoriete browser opstarten: een **adblocker** (advertentieblokker) installeren. Maar als we de tv-browser gebruiken of een Android-toestel, enz... Is het wat lastiger om iets te vinden dat werkt. En als er meer dan één apparaat in huis is, moet je de handeling voor elke browser herhalen!



In deze tutorial gaan we een eenvoudig probleem oplossen**: alle machines in ons netwerk voorzien van een advertentieblokker en deze centraal beheren.**



Om dit te doen, gebruiken we een hulpmiddel dat voor dit doel is ontwikkeld: **Pi-Hole**



Pi-Hole is een DNS sinkhole. Het gebruikt de DNS-verzoeken van je apparaten om verkeer te valideren of te weigeren en beschermt je zo tegen adressen en domeinen waarvan bekend is dat ze reclame, malware enzovoort verspreiden.



DNS staat voor Domain Name System. Dus wat is een domeinnaam? Nou, "it-connect.fr" is slechts één voorbeeld. Een domeinnaam is een unieke identificatie voor een of meer bronnen, meestal beheerd door een enkele entiteit.



De machinenaam plus de domeinnaam wordt FQDN genoemd voor *Fully Qualified Domain Name*. Hiermee kun je een specifieke machine bereiken door deze gewoon "aan te roepen". Als je bijvoorbeeld "www.trucmachin.com" typt, bel je in feite de machine "www", die behoort tot het domein "trucmachin.com".



Maar onze computers begrijpen geen mensentaal, het enige wat ze begrijpen is binair, dus hebben ze een IP Address nodig, wat het equivalent is van een telefoonnummer, om de website te bereiken.



Dus elke keer dat je de naam van een website in je browser invoert of op een link klikt, vraagt je computer eerst aan een DNS-server naar het IP Address dat bij die naam hoort.



**Pi-Hole inspecteert deze aanvragen (er zijn er honderden per dag!) en blokkeert automatisch de aanvragen waarvan bekend is dat ze advertenties of zelfs kwaadaardige bestanden hosten



## II. Pi-Hole installeren



Met een naam als Pi-Hole ga je er misschien vanuit dat je een Raspberry-Pi nodig hebt... Maar dat is niet helemaal waar. **Pi-Hole kan op elke Linux-computer worden geïnstalleerd (Debian, Fedora, Rocky, Ubuntu, enz.)



Aan de andere kant moet je er rekening mee houden dat **dit apparaat 24 uur per dag moet draaien om een eenvoudige reden: geen DNS, geen internet!** De Raspberry is daarom een goed idee, omdat het bijna geen energie verbruikt.



Om te installeren maak je gewoon verbinding met je Linux machine via SSH en voer je het volgende commando in als "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Noot**: onder normale omstandigheden is het niet aan te raden om een script te "hacken" zonder eerst te weten wat het doet. Als je het niet zeker weet, ga dan naar de pagina met een browser of download de inhoud als een bestand.
>


> **Note: op minimale versies van Debian 11 is Curl niet geïnstalleerd, dus je moet het handmatig installeren met het **apt-get install curl** commando voordat je het bovenstaande commando typt.

Nadat het script is uitgevoerd, wordt er een reeks tests uitgevoerd en de installatie zelf gaat vanzelf:



![Image](assets/fr/019.webp)



Pi-Hole installeren



Zodra de installatie is voltooid, wordt u naar dit scherm geleid:



![Image](assets/fr/020.webp)



Pi-Hole startscherm



> **Note**: als je DHCP gebruikt op je machine, krijg je hier een waarschuwing over. Voor goed gebruik raden we je natuurlijk sterk aan om een vast IP toe te wijzen aan je machine.

Na dit scherm krijg je een paar informatieberichten en dan ga je naar de configuratiewizard, die je eerst vraagt naar welke DNS-server Pi-Hole verzoeken zal doorsturen. Ik heb gekozen voor Quad9, die een gebruikers privacy charter heeft.



![Image](assets/fr/021.webp)



DNS-selectie - Pi-Hole



> **Noot: als je in een bedrijf zit, is de kans groot dat je huidige DNS-server de Active Directory domeincontroller is. Maar maak je geen zorgen, je kunt later een voorwaardelijke omleiding opgeven voor een domein naar keuze. Normaal gesproken kun je elk verzoek met betrekking tot je lokale domein omleiden naar je DNS-server.

Je zult zien dat sommige keuzes een DNSSEC optie bevatten. In principe is het DNS-protocol niet veilig (het is destijds niet ontworpen met dit in gedachten). DNSSEC lost dit probleem op door een Layer beveiliging toe te voegen via encryptie en ondertekening van uitwisselingen, zoals uitgelegd in het bijbehorende artikel: [DNS Beveiliging](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Elke advertentieblokkeraar vertrouwt op een of meer lijsten om zijn werk te doen. Pi-Hole wordt standaard geleverd met één lijst, dus selecteer deze en voeg later meer lijsten toe.



![Image](assets/fr/022.webp)



Kom op de vraag over Interface web, de installatie ervan is optioneel, omdat de tool zijn eigen opdrachtregel heeft voor beheer en visualisatie. Maar deze Interface is nogal prettig en goed gedaan, dus ik raad je aan om het tegelijkertijd te installeren:



![Image](assets/fr/023.webp)



Als je Pi-Hole installeert op een machine die al een webserver heeft, kun je "nee" antwoorden op de volgende vraag. Merk echter op dat PHP en verschillende modules nodig zijn om dit te laten werken. Anders wordt **lighttpd geïnstalleerd met alle nodige modules**.



![Image](assets/fr/024.webp)



Vervolgens wordt u gevraagd of u DNS-verzoeken wilt registreren. **Als je een geschiedenis wilt bijhouden, zet dit dan op ja; anders op nee, maar dan verlies je een deel van de functionaliteit** (zie volgende scherm).



![Image](assets/fr/025.webp)



Voor zijn Interface web gebruikt Pi-Hole een eigen functie genaamd FTLDNS, die een API biedt en statistieken genereert van DNS verzoeken. Deze functie kan een "privacy" modus bevatten die de aangevraagde domeinen maskeert, de klanten achter het verzoek, of beide. Handig als u wilt monitoren zonder inbreuk te maken op de privacy van mensen, of gewoon als u wilt voldoen aan de relevante regelgeving in het geval van gebruik op een openbaar netwerk.



![Image](assets/fr/026.webp)



Keuze van privélevensstijl



Zodra deze laatste vraag beantwoord is, zal het script doen wat het moet doen: de GitHub repositories downloaden en Pi-Hole configureren. Aan het einde van de installatie wordt een samenvattend scherm getoond met de belangrijke informatie:



![Image](assets/fr/027.webp)



Overzichtsscherm installatie



Noteer het Interface webwachtwoord en de netwerkinformatie. Nu is het tijd om de DHCP-service op onze huidige locatie te configureren.



## III. DHCP-configuratie



Om te kunnen functioneren moet Pi-Hole DNS verzoeken van clients "omzetten", zodat ze weten dat zij degene is waar ze naartoe gestuurd moeten worden. Er zijn verschillende manieren om dit te doen:





- DNS-instellingen wijzigen in uw DHCP-server (bijv. uw Box)
- Schakel deze server uit en gebruik de server geleverd door Pi-Hole
- Elk apparaat handmatig aanpassen om Pi-Hole als DNS te gebruiken



Persoonlijk kies ik voor de eerste oplossing. De kans is groot dat **je een DHCP-server hebt waar je bent** (meestal je box). Dus je hoeft geen moeite te doen.



Aangezien er een groot aantal mogelijkheden zijn, tussen de verschillende boxen van operators (die ik niet allemaal ken) en degenen die hun eigen router hebben, ga ik geen screenshot geven voor deze aanpassingen. In ieder geval moet je naar de DHCP-instellingen gaan en de parameter "DNS" wijzigen om het IP Address van je Pi-Hole op te nemen.



Als dit is gebeurd, zullen apparaten die eerder zijn ingeschakeld de oude instellingen hebben behouden, dus je moet het configuratieverzoek opnieuw starten.



Op Windows-werkstations, met een opdrachtprompt:



```
ipconfig /renew
```



Op een Linux-werkstation:



```
dhclient
```



Alle andere apparaten moeten uit- en weer ingeschakeld worden.



Ze moeten dus de juiste parameters krijgen om te controleren:



```
ipconfig /all
```



In het DNS-veld moet de Address van je Pi-Hole staan, in mijn geval 192.168.1.42:



![Image](assets/fr/029.webp)



## IV. Het Interface web Pi-Hole gebruiken



Om het beheer te vereenvoudigen, beschikt **Pi-Hole** over een goed ontworpen Interface web Interface. Gebruiksvriendelijk en toegankelijk, het laat je:





- Bekijk het aantal verzoeken, geblokkeerde verzoeken, enz. in realtime.
- Beheer uw witte en zwarte lijst
- Statische vermeldingen, aliassen, enz. toevoegen.
- Lijsten toevoegen
- En nog veel meer functies!



Van mijn kant ga ik een blokkadelijst toevoegen. Zoals hierboven vermeld, is er maar één lijst tegelijk met Soft geïnstalleerd. Er zijn veel lijsten voor advertentiesites, maar je kunt er het beste minstens één kiezen die specifiek is voor het land waarin je woont. Een van de bekendste lijsten is **EasyList**, en een daarvan is specifiek voor Frankrijk: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Om het toe te voegen, maak je eerst verbinding met de Interface admin: **http://<ip_du_PiHole>/admin**



Het beheerderswachtwoord is al gegenereerd (zie screenshot aan het einde van de installatie), dus je hoeft het alleen maar in te voeren om toegang te krijgen tot Interface:



![Image](assets/fr/030.webp)



Interface van Pi-Hole



We kunnen bijvoorbeeld zien dat er twee klanten verbonden zijn met de Pi-Hole, dat het 442 verzoeken heeft verwerkt en dat 8 daarvan zijn geblokkeerd. Deze grafieken kunnen een goede bron van informatie zijn, vooral in een professionele context.



Ga naar de menu's "**Groepsbeheer**" en "**Lijsten**" om onze lijst toe te voegen:



![Image](assets/fr/031.webp)



We zien onze eerste lijst "**StevenBlack**", om de onze toe te voegen kopieer je de link die ik je hierboven gaf en voeg je die in het veld "**Address**" in, voor de beschrijving kies ik ervoor om de naam van de lijst te zetten:



![Image](assets/fr/032.webp)



Een lijst toevoegen in Pi-Hole



We hoeven alleen nog maar op "**Add**" te klikken om het toe te voegen. Om het te activeren, moeten we een extra stap uitvoeren om Pi-Hole te "waarschuwen" om deze lijst over te nemen. Om dit te doen:





- Gebruik de ingebouwde opdrachtregel
- Ofwel de Interface web



Persoonlijk heb ik voor de tweede gekozen, want als je goed hebt gekeken, staat de link naar het PHP-script dat de update uitvoert direct op de pagina waar we ons bevinden (het woord "online"). Je hoeft er dus alleen maar op te klikken, waardoor je op een pagina komt met maar één optie:



![Image](assets/fr/033.webp)



De pagina toont het resultaat van het script zodra dit is voltooid, wat betekent dat er rekening is gehouden met de lijst (tenzij er een foutmelding wordt weergegeven, natuurlijk).



Zoals aangekondigd aan het begin van deze tutorial, kun je met Pi-Hole ook **domeinen blokkeren waarvan bekend is dat ze malware verspreiden. Om deze functie te versterken, stel ik voor dat je ook de regelmatig bijgewerkte domeinenlijst, verspreid door Abuse.ch**, toevoegt. Dit zal de beveiliging van je netwerk aanzienlijk versterken, beschikbaar op [deze Address](https://urlhaus.abuse.ch/downloads/hostfile/).



Je kunt natuurlijk lijsten toevoegen waarvan je denkt dat ze relevant zijn, of je zwarte lijst handmatig beheren via het zwarte lijst-menu.



## V. Pi-gat testen



Nu alles op zijn plaats staat, hoef je alleen nog maar te testen of de oplossing goed werkt.



Ik zal bijvoorbeeld proberen het domein *http://admin.gentbcn.org/* te bereiken dat op de Abuse.ch-lijst staat omdat bekend is dat het malware host:



![Image](assets/fr/034.webp)



Kennelijk ben ik ergens geblokkeerd. Om er zeker van te zijn dat het de Pi-Hole is die de klus heeft geklaard, kunnen we het querylogboek in het Interface web "Query Log" controleren om te zien dat het een blokkade van een lijstvermelding is:



![Image](assets/fr/035.webp)



## VI. Conclusie



In deze tutorial laten we je zien hoe je een DNS-server instelt die niet alleen de meeste advertenties voor je surfgemak elimineert, maar ook **een Layer aan beveiliging toevoegt door phishing- en malwaredomeinen** te blokkeren.



Allemaal gratis en zuinig als je ze installeert op een Raspberry-Pi (qua stroomverbruik).