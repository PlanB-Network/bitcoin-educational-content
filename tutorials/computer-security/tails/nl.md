---
name: Tails

description: Installeer Tails op een USB-stick
---

![image](assets/cover.webp)


Een draagbaar en amnesisch besturingssysteem dat je beschermt tegen bewaking en censuur.


## Waarom heb je een USB-sleutel waarop Tails is geïnstalleerd?


Tails (https://tails.boum.org/) is de eenvoudigste manier om altijd een beveiligde computer tot je beschikking te hebben, die geen sporen achterlaat op de computer waarmee je hem gebruikt.


Om Tails te gebruiken, zet je de computer uit waar je toegang tot hebt (bij je ouders, bij je vrienden, in een internetcafé...) en start je hem op met je Tails USB-stick in plaats van Windows, macOS of Linux.


Daarna heb je een werkruimte en communicatieomgeving die onafhankelijk is van het gebruikelijke besturingssysteem en nooit de Hard schijf gebruikt.


Tails schrijft nooit naar de Hard schijf en gebruikt alleen het RAM-geheugen van de computer om te functioneren. Dit geheugen wordt volledig gewist wanneer Tails wordt afgesloten, waardoor alle mogelijke sporen worden verwijderd.


## Enkele concrete gebruikssituaties


Om je een concreet idee te geven van de voordelen van het altijd hebben van een USB-sleutel met Tails, is hier een kleine niet-uitputtende lijst samengesteld door het Agora256 team:



- Maak op een ongecensureerde en anonieme manier verbinding met internet en Tor om websites te bekijken zonder sporen achter te laten;
- Open een PDF van een verdachte website;
- Test je Bitcoin private key back-up met de Electrum Wallet;
- Gebruik een kantoorpakket (LibreOffice) en werk op een computer die niet van jou is;
- Zet je eerste stappen in een Linux-omgeving en leer hoe je de wereld van Microsoft en Apple kunt verlaten.


## Hoe kun je Tails vertrouwen?


Er is altijd een element van vertrouwen in het gebruik van software, maar het hoeft niet blind te zijn. Een tool als Tails moet ernaar streven om zijn gebruikers middelen te bieden om betrouwbaar te zijn. Voor Tails betekent dit:



- Openbare broncode: https://gitlab.tails.boum.org/;
- Een project gebaseerd op gerenommeerde projecten: Tor en Debian;
- Verifieerbare en reproduceerbare downloads;
- Aanbevelingen van verschillende personen en organisaties.


## Installatie- en gebruiksaanwijzing


Het doel van deze installatiegids is om je door elke stap van de installatie te leiden. We zullen niet meer acties beschrijven dan de officiële gids, maar we zullen je in de juiste richting wijzen en je tips en trucs geven.


Om redenen van praktische ervaring zullen deze tips gericht zijn op macOS- en Linux-platformen.

🛠️

Voordat je deze procedure start, moet je ervoor zorgen dat je een USB-stick hebt met een minimale leessnelheid van 150 MB/s en een capaciteit van minstens 8 GB, idealiter USB 3.0.


Vereisten:



- 1 USB-stick, alleen voor Tails, met een capaciteit van minstens 8 GB
- Een computer met internetverbinding met Linux, macOS (of Windows)
- Ongeveer een uur vrije tijd, afhankelijk van de snelheid van je internetverbinding, inclusief ½ uur voor de installatie (1,3 GB bestand om te downloaden)


## Stap 1: Download Tails van je computer


![image](assets/1.webp)


🔗 **Officiële staartensectie:** https://tails.boum.org/install/linux/index.fr.html#download


Het downloaden van het installatiebestand met de extensie .img kan even duren, afhankelijk van de downloadsnelheid van je internet. Met een moderne en efficiënte verbinding duurt het minder dan 5 minuten.


Sla het bestand op in een bekende map, zoals Downloads, omdat dit nodig is voor de volgende stap.


## Stap 2: Controleer uw download


![image](assets/2.webp)


🔗 **Officiële staartensectie:** https://tails.boum.org/install/linux/index.fr.html#verify


Het verifiëren van de download zorgt ervoor dat deze is uitgegeven door de ontwikkelaars van Tails en niet is beschadigd of onderschept tijdens het downloaden.


Het is mogelijk om handmatig te controleren of het bestand dat je net hebt gedownload het verwachte bestand is met PGP, maar zonder geavanceerde kennis biedt deze verificatie hetzelfde beveiligingsniveau als de JavaScript-verificatie op de downloadpagina, terwijl het veel ingewikkelder is en vatbaar voor fouten.


Gebruik de knop "Selecteer uw download..." in het officiële gedeelte om het bestand te verifiëren!


## Stap 3: Installeer Tails op je USB-stick


![image](assets/3.webp)


🔗 **Officiële staartensectie:**



- **Linux:** https://tails.boum.org/install/linux/index.fr.html#install
- **macOS:** https://tails.boum.org/install/mac/index.fr.html#etcher en https://tails.boum.org/install/mac/index.fr.html#install


Deze stap van het installeren van Tails op je USB-stick is de moeilijkste in de hele handleiding, vooral als je het nog nooit gedaan hebt. Het belangrijkste is om de juiste procedure te kiezen in de officiële sectie voor je besturingssysteem: Linux of macOS.


Zodra de tools geïnstalleerd en voorbereid zijn zoals aanbevolen, kan het bestand met de .img extensie gekopieerd worden naar je sleutel (waarbij alle bestaande gegevens gewist worden) om het zelfstandig "bootable" te maken.


Veel succes en tot bij stap 4.


## Stap 4: Herstart op je Tails USB-sleutel


![image](assets/4.webp)


🔗 **Officiële staartensectie:** https://tails.boum.org/install/linux/index.en.html#restart


Het is tijd om een van je computers op te starten met je nieuwe USB-stick. Steek hem in een van de USB-poorten en start opnieuw op!


**Note💡: De meeste computers starten niet automatisch op vanaf de Tails USB-stick, maar u kunt op de opstartmenutoets drukken om een lijst weer te geven met mogelijke apparaten om van op te starten.**


Om te bepalen op welke toets je moet drukken om ervoor te zorgen dat je het opstartmenu krijgt waarmee je de USB-stick kunt selecteren in plaats van je gebruikelijke Hard schijf, volgt hier een niet-uitputtende lijst per fabrikant:


| Manufacturer | Key              |
| ------------ | ---------------- |
| Acer         | F12, F9, F2, Esc |
| Apple        | Option           |
| Asus         | Esc              |
| Clevo        | F7               |
| Dell         | F12              |
| Fujitsu      | F12, Esc         |
| HP           | F9               |
| Huawei       | F12              |
| Intel        | F10              |
| Lenovo       | F12              |
| MSI          | F11              |
| Samsung      | Esc, F12, F2     |
| Sony         | F11, Esc, F10    |
| Toshiba      | F12              |
| others...    | F12, Esc         |

Zodra de USB-stick is geselecteerd, zou je dit nieuwe opstartscherm moeten zien, wat een heel goed teken is, dus laat de computer verder opstarten...


![image](assets/5.webp)


## Stap 5: Welkom bij Tails!


![image](assets/6.webp)


🔗 **Officiële staartensectie:** https://tails.boum.org/install/linux/index.en.html#tails


Een of twee minuten na de bootloader en het laadscherm verschijnt het welkomstscherm.


![image](assets/7.webp)


Selecteer in het welkomstscherm je taal en toetsenbordindeling in het gedeelte Taal en regio. Klik op Start Tails.


![image](assets/8.webp)


Als je computer niet is aangesloten op je netwerk, raadpleeg dan de officiële Tails instructies om je te helpen verbinding te maken met je netwerk zonder Wi-Fi (sectie "Test je Wi-Fi").


Eenmaal verbonden met het lokale netwerk, verschijnt de Tor Connection wizard om je te helpen verbinden met het Tor netwerk.


![image](assets/9.webp)


Je kunt anoniem gaan browsen en de opties en software van Tails verkennen. Geniet ervan, je hebt genoeg ruimte voor fouten, omdat er niets wordt gewijzigd op de USB-stick... Bij de volgende herstart zult u al uw ervaringen vergeten zijn!


## In een toekomstige gids...


Als je eenmaal wat meer hebt geëxperimenteerd met je eigen Tails USB-stick, zullen we in een ander artikel dieper ingaan op andere, meer geavanceerde onderwerpen, zoals:



- Update een sleutel met de **laatste versie van Tails**;
- Configureer en gebruik **persistente opslag**;
- Installeer **extra software**.


Tot dan, zoals altijd, als je vragen hebt, voel je vrij om ze te delen met de Agora256 gemeenschap. We leren samen om morgen beter te zijn dan vandaag!