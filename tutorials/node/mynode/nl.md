---
name: My Node
description: Uw Bitcoin MyNode instellen
---

![image](assets/0.webp)


[Mijn Knooppunt] (https://mynodebtc.com/) is de eenvoudigste, krachtigste manier om een Bitcoin en Lightning knooppunt te beheren! Wij combineren de beste open source software met onze Interface, beheer en ondersteuning, zodat u Bitcoin en Lightning eenvoudig, privé en veilig kunt gebruiken.


## Typen Node-opstellingen


Er zijn verschillende Node-opstellingen. MyNode is uitstekend. Er worden veel apps meegeleverd, en nog meer als je betaalt voor de premium versie. Het is anders erg vervelend om al die apps zelf te downloaden. De MyNode maakt het je heel gemakkelijk, zoals je zult zien.


Een alternatieve en vergelijkbare optie is RaspiBlitz. De GUI is niet zo mooi en de apps overlappen veel met de apps die bij MyNode worden geleverd, maar Raspiblitz is gratis open source software (FOSS) en MyNode is dat niet helemaal. Een ander verschil is dat MyNode in een Docker-container draait. Ik vind Docker ontmoedigend en Hard om problemen mee op te lossen. Dit is alleen een probleem als je fouten of bugs tegenkomt. De ontwikkelaar biedt hulp voor premium gebruikers en er is ook een chatgroep op Telegram.


De RaspiBlitz is gewoon meerdere programma's geïnstalleerd op Linux, zonder Docker. De externe Hard schijf kan eenvoudig worden aangesloten op een andere Linux machine met Bitcoin core, en weg ben je, mocht dat nodig zijn.


Een andere optie is om gewoon Bitcoin core en een Electrum Server variant (er zijn er verschillende) te installeren op een besturingssysteem. Ik heb gidsen voor Linux (Raspberry Pi), Mac en Windows.


## Boodschappenlijst



- Raspberry Pi 4, 4Gb geheugen of 8Gb (4Gb is genoeg)
- Officiële Raspberry Pi-voeding (Heel belangrijk! Zorg dat je geen generieke krijgt, echt waar)
- Een behuizing voor de Pi. FLIRC behuizing is geweldig. De hele behuizing is een koellichaam en je hebt geen ventilator nodig, die lawaaierig kan zijn
- 16 Gb microSD-kaart (je hebt er één nodig, maar een paar zijn handig)
- Een geheugenkaartlezer (de meeste computers hebben geen sleuf voor een microSD-kaart).
- Externe SSD 1Tb Hard schijf.

Opmerking: SSD is cruciaal. Gebruik geen draagbare externe Hard schijf, ook al is die goedkoper


- Een ethernetkabel (voor aansluiting op je thuisrouter)
- Je hebt geen monitor nodig


## MyNode-afbeelding downloaden


Navigeer naar de MyNode-website Link


![image](assets/1.webp)


Klik op `Download nu`


Download de Raspberry Pi 4-versie:


![image](assets/2.webp)


Het is een groot bestand:


![image](assets/3.webp)


De SHA 256 hashes downloaden


![image](assets/4.webp)


Open de terminal op Mac of Linux of Command Prompt voor Windows. Type:


```bash
shasum -a 256 DOWNLOADEDFILENAME # <--- Mac/Linux
certUtil -hashfile DOWNLOADEDFILENAME SHA256 # <--- Windows
```


De computer denkt ongeveer 20 seconden na. Controleer dan of het uitvoer hashbestand overeenkomt met het bestand dat in de vorige stap van de website is gedownload. Als het identiek is, kun je doorgaan.

De SD-kaart flashen


## Balena Etcher downloaden en installeren. Link


Ik kon de digitale handtekening hiervoor niet vinden. Als je weet hoe, laat het me dan weten en ik zal dit artikel bijwerken.


Het gebruik van Etcher wijst zichzelf. Plaats je micro SD-kaart en flash de Raspberry Pi software (.img bestand) op de SD-kaart.


![image](assets/5.webp)

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

![image](assets/10.webp)

![image](assets/11.webp)


Als dat gebeurd is, is de schijf niet langer leesbaar. Het besturingssysteem kan een foutmelding geven en de schijf zou van het bureaublad moeten verdwijnen. Trek de kaart eruit.


## Stel de Pi in en plaats de SD-kaart


De onderdelen (behuizing niet afgebeeld):


![image](assets/12.webp)

![image](assets/13.webp)


Sluit de ethernetkabel aan en de Hard drive USB-connector (nog geen stroom). Sluit niet aan op de blauwgekleurde USB-poorten in het midden. Deze zijn USB 3. MyNode raadt aan om de USB 2-poort te gebruiken, ook al is de drive geschikt voor USB 3.


![image](assets/14.webp)


De micro SD-kaart moet hier:


![image](assets/15.webp)


Sluit ten slotte de voeding aan:


![image](assets/16.webp)


## Zoek het IP Address van de Pi


Je hebt nooit een monitor nodig met de MyNode. Je hebt echter wel een andere computer in het thuisnetwerk nodig. Als je Pi niet is aangesloten via ethernet en je wilt vertrouwen op WiFi, dan vereist het vinden van het IP-adres computervaardigheden op hoog niveau. Ik kan je niet helpen, sorry. Je hebt een ethernetverbinding nodig. (Het probleem is dat je toegang moet hebben tot een monitor en het besturingssysteem om verbinding te maken met WiFi en een wachtwoord in te voeren).


Controleer je router voor een lijst met alle IP's van alle aangesloten apparaten.


Ik typte 192.168.0.1 in de browser (instructies die bij mijn router zaten), logde in en zag een apparaat "MyNode" met het IP 192.168.0.18. Deze IP-adressen zijn niet zichtbaar voor het internet (ze gaan eerst door de router). Merk op dat deze IP-adressen niet zichtbaar zijn voor het internet (ze gaan eerst door de router), het zijn slechts identificaties voor apparaten op je thuisnetwerk.


Het vinden van de IP is cruciaal.


**Note:** Je kunt de terminal op een Mac of Linux machine gebruiken om de IP Address van alle Ethernet-apparaten in het thuisnetwerk te vinden met het commando "arp -a". De uitvoer is niet zo mooi als wat de router weergeeft, maar alle informatie die je nodig hebt is er. Als het niet duidelijk is welke de Pi is, voer dan trial and error uit.


## SSH naar de Pi


Je hebt de optie om op afstand in te loggen op het apparaat met het SSH commando, maar dat is niet verplicht (wel als RaspiBlitz Node). Ik zal je toch laten zien hoe, want het is erg handig.


Open een Mac of Linux computer (voor Windows download je putty, een SSH-programma) en typ:


```bash
ssh admin@192.168.0.18
```


Gebruik je eigen IP Address. De gebruikersnaam voor het MyNode-apparaat is standaard "admin". Het wachtwoord is standaard "Bolt".


Als je je Pi eerder hebt gebruikt en de micro SD-kaart hebt verwisseld, krijg je deze foutmelding:


![image](assets/17.webp)


Wat je moet doen is navigeren naar waar het "known_hosts" bestand is en het verwijderen. Het is veilig. De foutmelding laat het pad zien. Bij mij was het /Users/MijnUserNaam/.ssh/


Vergeet de "." voor ssh niet, dit geeft aan dat het een verborgen map is.


Probeer dan het ssh-commando opnieuw.


Deze keer zie je deze uitvoer:


![image](assets/18.webp)


Het bestand dat je hebt verwijderd is verwijderd en je voegt een nieuwe vingerafdruk toe. Typ ja en <enter>.


Je wordt gevraagd om het wachtwoord in te voeren. Het is "Bolt"


U hebt nu terminal toegang tot de MyNode Pi, zonder monitor, en kunt bevestigen dat alles probleemloos wordt geladen.


![image](assets/19.webp)


## Toegang via de webbrowser


Open een browser. Het moet een computer in je thuisnetwerk zijn, je kunt dit niet van buitenaf doen. Er is een manier, maar het is Hard. Ik heb het niet getest.


Typ het IP Address in het venster van de browser Address. Dit zal gebeuren:


![image](assets/20.webp)


Voer het wachtwoord "Bolt" in - verander het later.


Dan zal dit gebeuren:


![image](assets/21.webp)


Kies Station formatteren


![image](assets/22.webp)


Nu wachten we.


Op een gegeven moment wordt je gevraagd of je je productsleutel wilt invoeren, of de gratis "community edition" wilt gebruiken - ik ga de Premium edition laten zien. Ik raad je aan om voor de premium versie te betalen als je het je kunt veroorloven, het is het zeker waard.


![image](assets/23.webp)


Je ziet dan de voortgang van de gedownloade blokken. Het duurt dagen:


![image](assets/24.webp)


Het is veilig om de machine uit te schakelen tijdens het downloaden als dat nodig is. Ga naar instellingen en zoek de knop om de machine uit te schakelen. Trek niet zomaar aan het snoer, je zou de installatie of de Hard schijf kunnen beschadigen.


Zorg ervoor dat je in het begin naar "Instellingen" gaat en quicksync uitschakelt. Dan begint het downloaden van de eerste blokken vanaf het begin.


![image](assets/25.webp)


Ik wilde doorgaan met het maken van de gids, dus hier is een andere MyNode die ik eerder had voorbereid. Zo ziet de pagina eruit wanneer de Blockchain is gesynchroniseerd en verschillende "apps" zijn ingeschakeld en gesynchroniseerd:


![image](assets/26.webp)


Merk op dat Electrum Server ook moet synchroniseren, dus zodra Bitcoin Blockchain is gesynchroniseerd, klik je op de knop om dat proces te starten - duurt een dag of twee. Al het andere is binnen een paar minuten ingeschakeld zodra je ervoor kiest om het in te schakelen. Je kunt op dingen klikken en ze verkennen. Je zult niets kapot maken. Als er toch iets kapot gaat (dit is mij overkomen, maar ik denk omdat ik goedkope onderdelen had) moet je opnieuw flashen en opnieuw beginnen met downloaden. Het probleem dat ik heb met MyNode is dat als je moet "re-flashen" je uiteindelijk de Blockchain synchronisatie weer van voren af aan moet beginnen. Er zijn technische manieren om dit te omzeilen, maar het is niet eenvoudig.


Als je ook een ander knooppunt wilt proberen, bijvoorbeeld een RaspiBlitz, dan heb je een extra SSD externe Hard schijf nodig en nog een micro SD kaart om te flashen. Voor de rest is het dezelfde apparatuur, je kunt alleen MyNode en RaspiBlitz natuurlijk niet tegelijkertijd gebruiken. Als je dat wilt doen, is het tijd om een andere Raspberry Pi te kopen.


Nu je een node hebt draaien, gebruik hem dan, laat hem niet gewoon niets voor je doen. Volg mijn artikel (en video) over hoe je je Electrum Desktop Wallet aansluit op Electrum Server en Bitcoin core hier.