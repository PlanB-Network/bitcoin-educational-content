---
name: RaspiBlitz
description: Handleiding voor het instellen van je RaspiBlitz
---

![image](assets/0.webp)


De RaspiBlitz is een doe-het-zelf Lightning Node (LND en/of Core Lightning) die samen met een Bitcoin-Fullnode draait op een RaspberryPi (1TB SSD) en een mooi display voor eenvoudige setup & monitoring.


RaspiBlitz is vooral bedoeld om te leren hoe je je eigen node gedecentraliseerd vanuit huis kunt beheren - omdat: Niet jouw node, niet jouw regels. Ontdek & ontwikkel het groeiende ecosysteem van de Lightning Network door er volledig deel van uit te maken. Bouw het als onderdeel van een workshop of als een weekendproject voor jezelf.


![video](https://youtu.be/DTHlSPMz3ns)

RASPIBLITZ - Hoe een Lightning en Bitcoin Full node draaien door BTC-sessie


# Parman's Raspiblitz installatiegids


De Raspiblitz is een uitstekend systeem voor het draaien van een Bitcoin-node en bijbehorende apps. Ik raad dit en de MyNode-node aan voor de meeste gebruikers (idealiter twee nodes voor redundantie). Een groot voordeel is dat de Raspiblitz-node "Free Open Source Software" is, in tegenstelling tot MyNode of Umbrel. [Waarom is dat belangrijk? Vlad Costa legt uit.](https://bitcoin-takeover.com/why-bitcoin-free-open-source-software-matters/amp/?__twitter_impression=true) Je kunt de Raspiblitz ook met een WiFi-verbinding in plaats van ethernet draaien – hier is een [aanvullende gids](https://armantheparman.com/headless-wifi/) daarvoor. (Ik heb geen manier gevonden om dit met MyNode te doen).


Je kunt een kant-en-klaar knooppunt kopen met een bevestigd minischerm, of je kunt het zelf bouwen (je hebt geen scherm nodig).


De [handleiding op de GitHub-pagina](https://github.com/rootzoll/raspiblitz) is uitstekend, maar mogelijk te gedetailleerd voor een gebruiker met gemiddelde ervaring. Mijn instructies zullen beknopter zijn en hopelijk makkelijker te volgen.


In wezen is het proces erg vergelijkbaar met het instellen van een [MyNode-node](https://armantheparman.com/mynode-bitcoin-node-easy-setup-guide-raspberry-pi/) met een Raspberry Pi 4. De Raspiblitz-gids stelt voor dat je een monitor koopt, maar je hebt er echt geen nodig, en ik zou het niet aanbevelen. Je hebt niet eens een extra toetsenbord of muis nodig. Toegang krijgen tot het terminalmenu van het apparaat via een computer op hetzelfde thuisnetwerk en gebruik de ssh-opdracht in de terminal. Dit is mogelijk met Linux/Mac (gemakkelijk) en iets moeilijker met Windows.


## Stap 1: Koop de apparatuur.


Je hebt precies dezelfde apparatuur nodig als voor een MyNode node. Je kunt het een of het ander proberen, het enige verschil is de data op de micro SD kaart.



- Raspberry Pi 4, 4Gb geheugen of 8Gb (4Gb is genoeg)
- Officiële Raspberry Pi-voeding (Heel belangrijk! Zorg dat je geen generieke krijgt, echt waar)
- Een hoes voor de Pi. (FLIRC behuizing is geweldig. De hele behuizing is een koellichaam en je hebt geen ventilator nodig, die lawaaierig kan zijn)
- 32 Gb microSD-kaart (je hebt er één nodig, maar een paar zijn handig. )
- Een geheugenkaartlezer (de meeste computers hebben geen sleuf voor een microSD-kaart).
- Externe SSD 1Tb Hard schijf.
- Een ethernetkabel (om verbinding te maken met je thuisrouter).


Je hebt geen monitor (of toetsenbord of muis) nodig


Opmerking: Dit is de verkeerde Hard schijf: Dit is een draagbare externe Hard schijf. Het is geen SSD. SSD is cruciaal. Daarom is hij goedkoop (Prijs in AUD)


![image](assets/1.webp)


Dit is het juiste type:


![image](assets/2.webp)


Dit is sneller, maar onnodig duur:


![image](assets/3.webp)


## Stap 2: Raspiblitz Afbeelding downloaden


Ga naar de [Raspiblitz GitHub-website](https://github.com/rootzoll/raspiblitz) en zoek de link “download image”:


![image](assets/4.webp)


De sha-256-hash van het gedownloade bestand wordt op de website vermeld. Deze verandert bij elke update. Als u niet begrijpt waar dit over gaat, zou u dat wel moeten doen, daarom heb ik een [handleiding geschreven die u hier kunt lezen.](https://armantheparman.com/gpg/)


![image](assets/5.webp)


## Stap 3: Afbeelding verifiëren


Voordat we verder gaan, als je nog geen weg weet in het bestandssysteem op de commandoregel, het is makkelijk te leren en je zou het moeten doen.


Hier is een [nuttige video voor Linux, maar die geldt ook voor Mac](https://youtu.be/id3DGvljhT4?list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK).


Voor Windows is hier een [eenvoudige handleiding](https://www.youtube.com/watch?v=MBBWVgE0ewk&t=1s).


_UPDATE: pgp/gpg-verificatie is nu beschikbaar. Je hebt de openbare sleutel van Openoms nodig. [Hier](http://parman.org/downloadable/openoms.txt) is deze (mogelijk moet je incognitomodus gebruiken zodat de link werkt – http, niet https)_
Mac/Linux


Wacht tot het downloaden van het bestand is voltooid (belangrijk!), navigeer dan met terminal open naar de plek waar je het bestand hebt gedownload en typ het volgende commando:

```bash
shasum -a 256 xxxxxxxxxxxxxx
```


waarbij `xxxxxxxxxxxxxx` de naam is van het bestand dat je zojuist hebt gedownload. Als u zich niet in de map bevindt waar dat bestand zich bevindt, moet u het volledige pad invoeren.


De computer denkt ongeveer 20 seconden na. Controleer of het uitvoer-hashbestand overeenkomt met het bestand dat in de vorige stap van de website is gedownload. Als het identiek is, kun je doorgaan.

Windows


Open de opdrachtprompt, navigeer naar de plaats waar het bestand is gedownload en typ deze opdracht:


```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```


waarbij `xxxxxxxxxxxxxxxxxx` de naam is van het bestand dat je zojuist hebt gedownload. Als je niet in de director bent waar dat bestand is, moet je het volledige pad intypen.


De computer denkt ongeveer 20 seconden na. Controleer of het uitvoer-hashbestand overeenkomt met het bestand dat in de vorige stap van de website is gedownload. Als het identiek is, kun je doorgaan.


## Stap 4: De SD-kaart flashen


Je kunt Balena Etcher gebruiken om dit te doen. [Download het hier](https://www.balena.io/etcher/).


Het gebruik van Etcher spreekt voor zich. Plaats je micro SD kaart en flash de Raspiblitz software (.img bestand) op de SD kaart.


![image](assets/6.webp)


![image](assets/7.webp)


![image](assets/8.webp)


![image](assets/9.webp)


Als dat gebeurd is, is de schijf niet langer leesbaar. Het besturingssysteem kan een foutmelding geven en de schijf zou van het bureaublad moeten verdwijnen. Trek de kaart eruit.


## Stap 5: Stel de Pi in en plaats de SD-kaart


De onderdelen (behuizing niet afgebeeld):


![image](assets/10.webp)


![image](assets/11.webp)


Sluit de ethernetkabel aan en de Hard drive USB-connector (nog geen stroom). Sluit niet aan op de blauwgekleurde USB-poorten in het midden. Deze zijn USB 3. Gebruik de USB 2-poort, ook al is de drive geschikt voor USB 3 (betrouwbaarder).


![image](assets/12.webp)


De micro SD-kaart moet hier:


![image](assets/13.webp)


Sluit ten slotte de voeding aan:


![image](assets/14.webp)


## Stap 6: Zoek het IP Address van de Pi


Je hebt nooit een monitor nodig met de Raspiblitz. Je hebt echter wel een andere computer in het thuisnetwerk nodig. Als je Pi niet is aangesloten via ethernet en je wilt vertrouwen op WiFi, dan vereist het vinden van het IP-adres enige computerkennis. Ik kan je niet helpen, sorry. Je hebt een ethernetverbinding nodig. (Het probleem is dat je toegang moet hebben tot een monitor en het besturingssysteem om verbinding te maken met WiFi en een wachtwoord in te voeren)


Controleer je router voor een lijst met alle IP's van alle aangesloten apparaten.


Ik typte 192.168.0.1 in de browser (instructies die bij mijn router zaten), logde in en kon mijn apparaat met het IP 192.168.0.191 zien. Let op: deze IP-adressen zijn niet zichtbaar voor het internet (ze gaan eerst door de router), het zijn slechts identificaties voor apparaten in je thuisnetwerk.


Het vinden van de IP is cruciaal.


**Note:** Je kunt de terminal op een Mac of Linux machine gebruiken om de IP Address van alle Ethernet-apparaten in het thuisnetwerk te vinden met het commando "arp -a". De uitvoer is niet zo mooi als wat de router weergeeft, maar alle informatie die je nodig hebt is er. Als het niet duidelijk is welke de Pi is, voer dan trial and error uit.


## Stap 7: SSH naar de Pi


Vergeet niet om de SD-kaart in de Pi te stoppen voordat je hem aanzet. Wacht een paar minuten en open dan op een andere Linux/Mac de terminal.


Voor Mac/Linux typt u in de terminal:


```bash
ssh admin@You_Pi's_IP_address
```


Voor Windows moet je [putty](http://putty.org/) installeren om via ssh in te loggen op de Pi. Typ hetzelfde commando als hierboven.


De eerste keer dat je dit doet, of telkens wanneer je het besturingssysteem van de Pi verandert door de SD-kaart te verwisselen, kun je deze foutmelding wel of niet krijgen..


![image](assets/15.webp)


De manier om het op te lossen is om naar het bestand "known_hosts" te navigeren (dit staat in de foutmelding) en het te verwijderen. Het commando is "rm known_hosts"


Herhaal dan het ssh-commando om in te loggen. Dit zal gebeuren..


![image](assets/16.webp)


Typ ja (volledig woord) om verder te gaan.


Als dit lukt, wordt er om een wachtwoord gevraagd. Dit is niet voor je computer, maar voor de raspiblitz. Het algemene wachtwoord is "raspiblitz", en dat zul je later veranderen. Het terminalvenster wordt blauw en je krijgt menuopties zoals de oude DOS-menu's. Navigeer met de pijltjestoetsen of de muis.


![image](assets/17.webp)


Volg de prompts, stel je wachtwoorden in en dan zal het je Hard schijf detecteren en je de optie geven om deze te formatteren indien nodig.


Dan wordt je gevraagd of je de Blockchain data van een andere bron wilt kopiëren of opnieuw wilt downloaden. Het kopiëren is een leerproces en de instructies zijn vrij goed, en goed om bij de hand te houden....


![image](assets/18.webp)


De eenvoudige maar langzamere manier is om de hele keten helemaal opnieuw te downloaden..


![image](assets/19.webp)


Veel tekst flitst over het scherm van de terminal. Je zou het kunnen verwarren met het proces van de Blockchain download, maar voor mij lijkt het erop dat het een privésleutel genereert voor communicatie.


Dan verschijnen er bliksemopties.


![image](assets/20.webp)


Maak een nieuw wachtwoord om je verlichting Wallet te vergrendelen, dan wordt er een nieuwe Wallet aangemaakt en krijg je 24 woorden om op te schrijven..


![image](assets/21.webp)


Zorg er wel voor dat je het opschrijft en goed bewaart. Ik hoorde van iemand die dat niet deed omdat hij niet van plan was om bliksem te gebruiken, maar een jaar later besloot om het te gebruiken en kanalen opende. Toen hij zich realiseerde dat er geen back-up was van zijn woorden, en ik herinner me dat het niet mogelijk was om de woorden weer van het apparaat te halen, moest hij al zijn kanalen sluiten en opnieuw beginnen. Hij kwam ermee weg, maar anderen hebben misschien minder geluk.


Hierna rolt er een paar minuten tekst over het terminalvenster. En dan..


![image](assets/22.webp)


Je wordt uitgelogd uit de ssh-sessie. Log weer in, deze keer met je nieuwe wachtwoord, wachtwoord A. Eenmaal ingelogd wordt om wachtwoord C gevraagd om je lightning Wallet te ontgrendelen.


Nu wachten we. Tot over 2 weken. Je kunt de terminal sluiten, het doet niets met de Pi, het is slechts een communicatievenster.


![image](assets/23.webp)


Als je om wat voor reden dan ook de Pi wilt afsluiten voordat de Blockchain klaar is met downloaden, is dat prima, zolang je het maar goed doet. De Blockchain gaat door met downloaden waar hij gebleven was zodra je weer verbinding maakt.


Druk op CTRL+c om het blauwe scherm af te sluiten. Je komt nu in de Linux terminal van de Pi. Hier kun je "menu" typen dat het volgende scherm laadt en van daaruit kun je de Pi uitschakelen.


![image](assets/24.webp)


EINDE van de gids


Dus vanaf nu is je node si klaar om te gaan. Als je nog steeds hulp nodig hebt bij het navigeren door meer opties, raadpleeg dan de github voor meer tutoriel en gids https://github.com/raspiblitz/raspiblitz#feature-documentation