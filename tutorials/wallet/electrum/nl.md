---
name: Electrum

description: Volledige Electrum Gids, van 0 tot held
---

![cover](assets/cover.webp)


Hieronder staan enkele beschrijvingsbronnen voor Electrum:



- [X](https://twitter.com/ElectrumWallet)
- [Electrum website](https://electrum.org/)
- [Electrum documentatie](https://electrum.readthedocs.io/)


Dit is wat Rogzy van deze tutorial vindt:


> Ik moet zeggen dat ik geschokt was toen ik deze gids tegenkwam. Felicitaties aan Arman the Parman voor dit. Het zou zonde zijn geweest om het niet hier te hosten en het in zoveel mogelijk talen te vertalen. Echt, tips die gast.

De originele post is de volgende:


![Electrum Desktop Wallet (Mac / Linux) - download, verify, connect to your node.](https://youtu.be/wHmQNcRWdHM)


![Making a Bitcoin transaction with Electrum](https://youtu.be/-d_Zd7VcAfQ)


## Waarom Electrum?


Dit is een gedetailleerde gids over het gebruik van de Electrum Bitcoin Wallet, met oplossingen voor al zijn valkuilen en eigenaardigheden -iets wat ik heb ontwikkeld na een aantal jaren gebruik, en het onderwijzen van studenten over Bitcoin beveiliging/privacy. Electrum is niet de beste Bitcoin Wallet voor iemand die alles zo eenvoudig mogelijk wil houden, en liever op beginnersniveau blijft. In plaats daarvan is het voor de persoon die een "power" gebruiker is, of wil worden.


Voor de nieuwe Bitcoiner is het alleen uitstekend als hij onder toezicht staat van een ervaren gebruiker die hem de weg wijst. Als je het alleen leert gebruiken, is het veilig als je er de tijd voor neemt en het in het begin gebruikt in een testomgeving met slechts een klein aantal Sats. Deze gids ondersteunt dat streven, maar is ook een goede referentie voor ieder ander. Deze gids ondersteunt dat streven, maar is ook een goede referentie voor ieder ander.


**Waarschuwing:** deze gids is vrij lang, dus probeer niet alle beschreven stappen in één dag uit te voeren. Het is raadzaam om de gids bij de hand te houden en na verloop van tijd gestaag vooruitgang te boeken.


**Note:** je kunt ook de volgende Electrum volledige video gids bekijken (let op dat het niet de geschreven tutorial vervangt, maar het is een integratie ervan):


![video](https://youtu.be/NNZdbYd8PUQ)


## Electrum downloaden


Idealiter gebruik je een dedicated Bitcoin computer voor je Bitcoin transacties (Mijn gids hiervoor https://armantheparman.com/mint/) _(ALSO beschikbaar op privacy sectie)_. Het is prima om te oefenen met kleine bedragen op een "vuile" computer wanneer je het voor het eerst leert (wie weet hoeveel verborgen malware je gewone computer in de loop der jaren heeft verzameld - je wilt je Bitcoin wallets daar niet aan blootstellen).


Haal Electrum van https://electrum.org/.


Klik bovenaan op het tabblad Downloaden.


Klik op de downloadlink die overeenkomt met je computer. Elke Linux- of Mac-computer kan de Python-link (rode cirkel) gebruiken. Een Linux computer met een Intel of AMD chip kan het Appimage gebruiken (Green cirkel; dit is als een Windows uitvoerbaar bestand). Een Raspberry Pi heeft een ARM microprocessor en kan alleen de Python versie (rode cirkel) gebruiken, niet Appimage, ook al draaien Pi's Linux. De blauwe cirkel is voor Windows en de zwarte cirkel is voor Mac.


![image](assets/1.webp)


## Electrum verifiëren


Het doel van het "verifiëren" van de download is om er zeker van te zijn dat er met geen enkel bit gegevens is geknoeid. Het voorkomt dat je een "gehackte" kwaadaardige versie van de software gebruikt. Het is prima om dit over te slaan, mits je de gedownloade kopie alleen gebruikt om te oefenen, dus geen wallets gebruikt waar serieus geld in zit. Als je dan klaar bent om Electrum te gebruiken voor je echte geld, moet je je kopie verwijderen en opnieuw beginnen, waarbij je deze keer je download moet verifiëren.


Om dit te doen, gebruiken we publieke/private sleutel cryptografie tools - gpg, waar we hier een gids over hebben geschreven (https://armantheparman.com/gpg/). De gpg tool wordt geleverd bij alle Linux besturingssystemen. Voor Mac en Windows, zie de gpg link voor download instructies.


Naast het downloaden van de Electrum software, heb je voor de veiligheid ook de digitale SIGNATUUR van de software nodig. Dit is een tekenreeks (eigenlijk een getal gecodeerd met tekst) die de ontwikkelaar heeft gemaakt met zijn PRIVÉ gpg-sleutel. Met behulp van het gpg-programma kunnen we dan de SIGNATURE "testen" tegen zijn PUBLIEKE sleutel (gemaakt van de private sleutel van de ontwikkelaar) waar iedereen toegang toe heeft, versus het downloadBESTAND.


Met andere woorden, met de drie ingangen (handtekening, openbare sleutel en gegevensbestand) krijgen we een waar of onwaar resultaat om te bevestigen dat er niet met het bestand geknoeid is.


Om de handtekening te krijgen, klik je op de link die overeenkomt met het bestand dat je hebt gedownload (zie gekleurde pijlen):


![image](assets/2.webp)


Als je op de link klikt, wordt het bestand automatisch gedownload naar je downloadmap of wordt het geopend in de browser. Als het bestand in de browser wordt geopend, moet je het bestand opslaan. Je kunt met de rechtermuisknop klikken en "opslaan als" selecteren. Afhankelijk van het besturingssysteem of de browser, moet je met de rechtermuisknop klikken op de witte ruimte en niet op de tekst.


Hieronder zie je hoe de gedownloade tekst eruit ziet. Je kunt zien dat er meerdere handtekeningen zijn - dit zijn handtekeningen van verschillende mensen. Je kunt elke handtekening of elke handtekening verifiëren. Ik zal je laten zien hoe je alleen die van de ontwikkelaar kunt verifiëren.


![image](assets/3.webp)


Vervolgens moet je de publieke sleutel van ThomasV krijgen - hij is de hoofdontwikkelaar. Je kunt die direct van hem krijgen, van zijn Keybase account, Github, of van iemand anders, van een keyserver, of van de Electrum website.


Het verkrijgen van de Electrum website is eigenlijk de minst veilige manier, want als deze website kwaadaardig is (precies waar we op controleren) waarom krijgen we dan een publieke sleutel van deze website (de publieke sleutel zou nep kunnen zijn)?


Om het voor nu eenvoudig te houden, laat ik je zien hoe je het toch van de website kunt halen, maar houd dit in gedachten. Hier is de kopie (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc ) op GitHub waarmee je het kunt vergelijken.


Scroll een beetje naar beneden om de link naar de publieke sleutel van ThomasV te vinden (rode cirkel hieronder). Klik erop en download het, of als er tekst wordt geopend in een browser, klik dan met de rechtermuisknop om het op te slaan.


![image](assets/4.webp)


Je hebt nu 3 nieuwe bestanden, waarschijnlijk allemaal in de map downloads. Het maakt niet uit waar ze staan, maar het maakt het proces makkelijker als je ze allemaal in dezelfde map zet.


De drie bestanden:


1. De Electrum download

2. Het handtekeningbestand (meestal is het dezelfde bestandsnaam als de Electrum download met een ".asc" toevoeging

3. De openbare sleutel van ThomasV.


Open een terminal in Mac of Linux, of opdrachtprompt (CMD) in Windows.


Navigeer naar de map Downloads (of waar je de drie bestanden ook hebt geplaatst). Als je geen idee hebt wat dit betekent, leer dan van deze korte video voor Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) en deze voor Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). Onthoud dat op Linux-computers mapnamen hoofdlettergevoelig zijn.


Typ dit in de terminal om de publieke sleutel van ThomasV te importeren in de "sleutelring" van je computer (de sleutelring is een abstract concept - het is eigenlijk gewoon een bestand op je computer):


```bash
gpg --import ThomasV.asc
```


Zorg ervoor dat de bestandsnaam overeenkomt met wat je hebt gedownload. Merk ook op dat het een dubbel streepje is en geen enkel streepje. Merk ook op dat er een spatie staat voor en na "-import". Druk vervolgens op <enter>.


Het bestand zou geïmporteerd moeten worden. Als je een foutmelding krijgt, controleer dan of je in de map bent waar het bestand echt bestaat. Om te controleren in welke map je zit (op Mac of Linux), typ je pwd. Om te zien welke bestanden er in je map staan (op Mac of Linux), typ je ls. Je zou het tekstbestand "ThomasV.asc" moeten zien, mogelijk tussen andere bestanden.


Daarna voeren we het commando uit om de handtekening te verifiëren.


```bash
gpg –verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```


Merk op dat er hier 4 "Elements" zijn, elk gescheiden door een spatie. Ik heb de tekst om en om vet gemaakt om je te helpen het te zien. De vier Elements zijn:


1. het gpg-programma

2. de optie -verifiëren

3. de bestandsnaam van de handtekening

4. de bestandsnaam van het programma


Interessant is dat je soms het 4e element weg kunt laten en de computer raadt wat je bedoelt. Ik weet het niet zeker, maar ik geloof dat het alleen werkt als de bestandsnamen alleen verschillen door de "asc" aan het einde.


Kopieer niet zomaar de bestandsnamen die ik hier heb laten zien - zorg ervoor dat ze overeenkomen met de bestandsnaam van wat je op je systeem hebt staan.


Druk op <enter> om het commando uit te voeren. Je zou een "goede handtekening van ThomasV" moeten zien om succes aan te geven. Er zullen enkele foutmeldingen zijn omdat we niet de publieke sleutels hebben voor de handtekeningen van anderen die in het handtekeningenbestand staan (dit systeem om handtekeningen in één bestand te combineren kan in latere versies veranderen). Er staat ook een waarschuwing onderaan die we kunnen negeren (dit waarschuwt ons dat we de computer niet expliciet hebben verteld dat we de publieke sleutel van ThomasV vertrouwen).


Nu hebben we een geverifieerde kopie van Electrum die veilig te gebruiken is.


## Lopend Electrum


### Electrum uitvoeren als je Python gebruikt


Als je de Python-versie hebt gedownload, kun je het op deze manier laten werken. Op de downloadpagina zie je dit:


![image](assets/5.webp)


Voor Linux is het een goed idee om eerst je systeem bij te werken:


```bash
sudo apt-get update
sudo apt-get upgrade
```


Kopieer de geel gemarkeerde tekst, plak het in de terminal en druk op <enter>. Je wordt om je wachtwoord gevraagd, mogelijk een bevestiging om door te gaan, en dan worden die bestanden ("dependencies") geïnstalleerd.


Je moet het gezipte bestand ook uitpakken in een map naar keuze. Je kunt dit doen met de grafische gebruiker Interface, of vanaf de opdrachtregel (roze gemarkeerde opdracht) - onthoud dat je bestandsnamen kunnen verschillen. (Merk op dat toen we de download in de vorige sectie controleerden, we het zip-bestand controleerden, niet de uitgepakte map)


Er is een optie om te "installeren" met het PIP-programma, maar dit is onnodig en voegt extra stappen en installatie van bestanden toe. Voer het programma gewoon uit via de terminal om dat allemaal te omzeilen.


De stappen (Linux) zijn:


1. navigeer naar de map waar de bestanden zijn uitgepakt

2. type: ./run_electrum


Op een Mac zijn de stappen hetzelfde, maar moet je misschien eerst Python3 installeren en dit commando uitvoeren:


```bash
python3 ./run_electrum
```


Als Electrum eenmaal draait, blijft het terminalvenster open. Als je het sluit, wordt het Electrum-programma afgesloten. Minimaliseer het gewoon terwijl je Electrum gebruikt.


### Electrum uitvoeren met Appimage


Dit is een beetje makkelijker, maar niet zo makkelijk als een Windows uitvoerbaar bestand. Afhankelijk van de versie van Linux die je gebruikt, kunnen Appimage bestanden standaard attributen hebben die zo zijn ingesteld dat ze niet mogen worden uitgevoerd door het systeem. Dit moeten we veranderen. Als je Appimages werkt, kun je deze stap overslaan. Navigeer naar de locatie van het bestand met de terminal en voer dan dit commando uit:


```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```


"sudo" geeft superuser-privileges; "chmod" is een commando om de modus te wijzigen, om te veranderen wie kan lezen, schrijven of uitvoeren; "ug+x" betekent dat we de gebruiker en groep wijzigen om uitvoering toe te staan.


Pas de bestandsnaam aan zodat deze overeenkomt met jouw versie.


Vervolgens wordt Electrum uitgevoerd door te dubbelklikken op het Appimage pictogram.


### Electrum draaien met Mac


Dubbelklik gewoon op het gedownloade bestand (het is een "station"). Er wordt een venster geopend. Sleep het Electrum pictogram in het venster naar je bureaublad, of waar je het programma ook wilt bewaren. Vervolgens kun je het station "uitwerpen" en het station (gedownloade bestand) verwijderen.


Dubbelklik op het programma om het uit te voeren. Je kunt enkele Mac-specifieke "nanny" fouten krijgen die omzeild moeten worden.


### Electrum draaien met Windows


Ondanks het feit dat ik Windows het meeste haat, is dit de eenvoudigste methode. Dubbelklik gewoon op het uitvoerbare bestand om het uit te voeren.


## Begin met een dummy Wallet


Wanneer u Electrum voor het eerst laadt, wordt een venster als dit geopend:


![image](assets/6.webp)


We zullen je server later handmatig selecteren, maar voor nu laat je de standaardinstelling staan en maak je automatisch verbinding.


Maak vervolgens een dummy Wallet - stop nooit geld in deze Wallet. Het doel van deze dummy Wallet is om de software te doorlopen en te controleren of alles goed werkt, voordat je je echte Wallet oplaadt. We proberen te voorkomen dat je per ongeluk je privacy opgeeft met een echte Wallet. Als je alleen oefent, kan de Wallet die je maakt sowieso als een dummy Wallet worden beschouwd.


Je kunt de naam "default_wallet" laten staan of veranderen in wat je maar wilt, en op volgende klikken. Als je later meerdere portemonnees hebt, kun je ze in dit stadium vinden en openen door eerst op "Kies..." te klikken


![image](assets/7.webp)


Kies "Standaard Wallet" en <Volgende>:


![image](assets/8.webp)


Selecteer dan "Ik heb al een seed". Ik wil niet dat je er een gewoonte van maakt om een Electrum seed aan te maken, omdat het een eigen protocol gebruikt dat niet compatibel is met andere wallets - daarom klikken we niet op "nieuwe seed".


![image](assets/9.webp)


Ga naar https://iancoleman.io/bip39/ en maak een dummy seed. Verander eerst het woordnummer in 12 (wat gebruikelijk is), klik dan op "generate" en kopieer de woorden in het vak naar je klembord.


![image](assets/10.webp)


Plak de woorden vervolgens in Electrum. Hier is een voorbeeld:


![image](assets/11.webp)


Electrum zoekt naar woorden die overeenkomen met zijn eigen protocol. Dat moeten we omzeilen. Klik op opties en selecteer BIP39 seed:


![image](assets/12.webp)


De seed wordt dan geldig. (Voordat je dit deed, verwachtte Electrum een Electrum seed, dus deze seed werd als ongeldig gezien). Voordat je op next klikt, zie je de tekst "Checksum OK". Het is belangrijk (voor de echte Wallet die je later gebruikt) dat je dit ziet voordat je verder gaat, want het bevestigt de geldigheid van de seed die je hebt ingevoerd. De waarschuwing onderaan kun je negeren, het is het gezeur van de Electrum ontwikkelaar over BIP39 en hun "FUD'ey" claims dat hun versie (die niet compatibel is met andere wallets) superieur is.


**Een snelle omweg voor een belangrijke waarschuwing:** het doel van de controlesom is om er zeker van te zijn dat je je seed zonder typefouten hebt ingevoerd. De controlesom is het laatste deel van de seed (het 12e woord wordt uiteindelijk het controlesomwoord) dat mathematisch bepaald wordt door het eerste deel van de seed (11 woorden). Als je aan het begin iets verkeerd typt, zal het checksum woord mathematisch niet overeenkomen en zal de Wallet software je waarschuwen. Dit betekent niet dat de seed niet gebruikt kan worden om een functionele Bitcoin Wallet te maken. Stel je voor dat je een Wallet maakt met een typefout, dat je de Wallet laadt met Bitcoin, dat je dan op een dag de Wallet moet herstellen, maar dat je dan niet de typefout herstelt - je herstelt de verkeerde Wallet! Het is heel gevaarlijk dat Electrum je door laat gaan met het maken van een Wallet als je checksum ongeldig is, dus wees gewaarschuwd, het is jouw verantwoordelijkheid om het zeker te weten. Andere wallets laten je niet doorgaan, wat veel veiliger is. Dit is een van de dingen die ik bedoel als ik zeg dat Electrum prima te gebruiken is, als je het eenmaal goed leert gebruiken (Electrum devs zouden dit moeten oplossen).


Merk op dat als je een passphrase zou willen toevoegen, de kans om dat te selecteren in dit venster staat, helemaal bovenaan.


Nadat je op OK hebt geklikt, ga je terug naar waar je de seed zin hebt ingetypt. Als je een passphrase optie hebt geselecteerd, voer je die NIET in met de seed woorden (de prompt daarvoor komt hierna).


Als je geen passphrase hebt aangevraagd, zie je hierna dit scherm - meer opties voor je Wallet scripttype en afleidingspad waarover je hier meer kunt leren (https://armantheparman.com/public-and-private-keys/), maar laat de standaardinstellingen staan en ga verder.


![image](assets/13.webp)


**Voor extra informatie** Met de eerste optie kun je kiezen tussen:



- legacy (adressen die beginnen met "1"),
- Pay-to-Script-Hash (adressen beginnend met "3"),
- bech32/native SegWit (adressen die beginnen met "bc1q").


Op het moment van schrijven ondersteunt Electrum nog geen Taproot (adressen die beginnen met "bc1p"). Met de tweede optie in dit venster kun je het afleidingspad aanpassen. Ik raad je aan dit nooit aan te passen, zeker niet voordat je begrijpt wat het betekent. Mensen zullen benadrukken hoe belangrijk het is om het afleidingspad op te schrijven, zodat je je Wallet kunt herstellen als dat nodig is, maar als je het laat zoals het standaard is, komt het waarschijnlijk wel goed, dus geen paniek - maar het is nog steeds een goede gewoonte om het afleidingspad op te schrijven.


Vervolgens krijg je de optie om een WACHTWOORD toe te voegen. Dit is niet te verwarren met "passphrase". Een wachtwoord vergrendelt het bestand op je computer. Een passphrase maakt deel uit van de samenstelling van de private sleutel. Aangezien dit een dummy Wallet is, kun je het wachtwoord leeg laten en doorgaan.


![image](assets/14.webp)


Je krijgt een pop-up over meldingen van nieuwe versies (ik stel voor dat je nee selecteert). De Wallet zal dan zelf generate maken en klaar zijn voor gebruik (maar onthoud, deze Wallet is bestemd om verwijderd te worden, het is slechts een dummy Wallet).


![image](assets/15.webp)


Er zijn een aantal dingen die je moet doen om de softwareomgeving in te stellen (slechts één keer nodig):


### Verander de eenheden in BTC


Ga naar het bovenste menu, tools -> electrum preferences, en daar onder de algemene tab vind je de optie om de "basiseenheid" te veranderen in BTC.

Het tabblad Adressen en munten inschakelen


Ga naar het bovenste menu, weergave en selecteer "adressen weergeven". Ga dan terug naar weergave en selecteer "toon munten".


### Een server inschakelen


Standaard maakt Electrum verbinding met een willekeurig knooppunt. Het maakt ook verbinding met veel andere secundaire knooppunten. Ik weet niet zeker welke gegevens worden uitgewisseld met deze secundaire knooppunten, maar we willen niet dat dit gebeurt, voor de privacy. Zelfs als je een knooppunt opgeeft, bijvoorbeeld je eigen knooppunt, worden deze meerdere andere knooppunten ook verbonden en ik weet niet zeker welke informatie wordt gedeeld. Hoe dan ook, het is eenvoudig te voorkomen. Voordat ik je laat zien hoe je je eigen node kunt opgeven, zullen we Electrum dwingen om slechts met één server tegelijk te verbinden.


**Note:** Er is een manier om dit te doen door "oneserver" op te geven vanaf de commandoregel, maar ik raad deze manier niet aan. Ik zal een alternatief laten zien waarvan ik denk dat het op de lange termijn gemakkelijker is en dat het waarschijnlijker is dat je niet per ongeluk verbinding maakt met andere nodes.


De reden dat we een dummy Wallet gebruiken is dat als we onze echte Wallet hadden geladen, met onze echte Bitcoin, we nu per ongeluk verbinding zouden hebben gemaakt met een willekeurig knooppunt (zelfs als we "set server manually" hebben geselecteerd bij de start, maakt het om de een of andere reden nog steeds verbinding met deze andere secundaire knooppunten (hey Electrum devs, jullie zouden dit moeten oplossen). Als onze Wallet privé was, zou dit een ramp zijn.


We kunnen de stappen die ik je hieronder laat zien ook niet uitvoeren zonder eerst een soort Wallet te laden. (We gaan een configuratiebestand bewerken dat pas wordt ingevuld en klaar is voor bewerking als er een Wallet is geladen).


Sluit nu Electrum af **(BELANGRIJK: als je dit niet doet, worden de volgende wijzigingen die je maakt gewist)**.


### LINUX/MAC-configuratiebestand


Open de terminal in Linux of Mac (Windows instructies later):


Je zou automatisch in de thuismap moeten zijn. Van daaruit navigeer je naar de verborgen electrum instellingenmap (dit is anders dan waar de applicatie staat).


```bash
cd .electrum
```


Let op de punt voor "electrum" die aangeeft dat het een verborgen map is.


Een andere manier om er te komen is door te typen:


```bash
cd ~/.electrum
```


waarbij "~" het pad van je thuismap is. Je kunt het volledige pad van je huidige map zien met het commando "pwd".


Eenmaal in de ".electrum" directory, typ "nano config" en druk op <enter>.


Er wordt een teksteditor geopend (genaamd nano) met het config-bestand open. De muis werkt hier niet veel. Gebruik de pijltjestoetsen om bij de regel te komen die zegt:


```json
"oneserver": false,
```


Verander "false" in "true"; en verstoor de syntaxis niet (verwijder de komma of puntkomma niet).


Druk op <ctrl> x, om af te sluiten, dan op "y" om op te slaan, dan op <enter> om het wijzigen te bevestigen zonder de bestandsnaam te wijzigen.


Start Electrum nu opnieuw. Klik dan op de cirkel rechtsonder, die de netwerkinstellingen opent. Bovenaan in het overzichtstabblad zie je "verbonden met 1 knooppunt" - dit duidt op succes.


Net daaronder zie je een tekstveld met daarin de Address van de server. Je bent momenteel verbonden met dat willekeurige knooppunt. Meer over het verbinden met een knooppunt in de volgende sectie.


### Windows-configuratiebestand


Het windows config bestand is iets moeilijker te vinden. De directory is: `C:/Users/Parman/AppData/Roaming/Electrum`


Uiteraard moet je "Parman" veranderen in je eigen gebruikersnaam voor de computer.


In die map vind je het config-bestand. Open het met een teksteditor en bewerk de regel:


```json
"oneserver": false,
```


Verander "false" in "true"; verstoor de syntaxis niet (verwijder de komma of puntkomma niet).


Sla het bestand vervolgens op en sluit het af.


## Verbind Electrum met een knooppunt


Vervolgens willen we onze dummy Wallet verbinden met een knooppunt naar keuze. Als je nog niet klaar bent voor een node, kun je een van de volgende dingen doen:


1. Verbinding maken met het persoonlijke knooppunt van een vriend (Tor vereist)

2. Verbinding maken met het knooppunt van een vertrouwd bedrijf

3. Maak verbinding met een willekeurig knooppunt (niet aanbevolen).


Hier zijn trouwens instructies om je eigen node te draaien, en dit zijn de redenen waarom je dat zou moeten doen. (Bekijk de tutorials in de Node-sectie of in onze gratis cursussen)


### Verbinding maken met het knooppunt van een vriend via Tor (Gids verschijnt binnenkort)


### Verbinding maken met het knooppunt van een vertrouwd bedrijf


De enige reden om dit te doen is als je toegang moet hebben tot Blockchain en je geen eigen node beschikbaar hebt (of die van een vriend).


Laten we verbinding maken met het knooppunt van Bitaroo - Ons is verteld dat zij geen gegevens verzamelen. Ze zijn een Bitcoin Alleen Exchange, gerund door een gepassioneerde Bitcoiner. Verbinden met hen vereist een beetje vertrouwen, maar het is beter dan verbinden met een willekeurig knooppunt, dat een bewakingsbedrijf zou kunnen zijn.


Ga naar de netwerkinstellingen door op de cirkel rechtsonder in het venster van de Wallet te klikken (rood geeft aan dat er geen verbinding is, Green geeft aan dat er verbinding is en blauw geeft aan dat er verbinding is via Tor).


![image](assets/16.webp)


Zodra je op het cirkelpictogram klikt, verschijnt er een pop-upvenster: Je Wallet zal "verbonden met 1 knooppunt" tonen, omdat we dat eerder hebben afgedwongen.


Schakel het selectievakje "server automatisch selecteren" uit en typ de gegevens van Bitaroo in het serverveld, zoals weergegeven:


![image](assets/17.webp)


Sluit het venster en nu zouden we verbonden moeten zijn met Bitaroo's knooppunt. Ter bevestiging zou de cirkel Green moeten zijn. Klik er nogmaals op en controleer of de servergegevens niet zijn veranderd in een willekeurig knooppunt.


### Verbinding maken met je eigen knooppunt


Als je een eigen node hebt, is dat geweldig. Als je alleen Bitcoin core hebt, en niet ook een Electrum SERVER, kun je nog geen Electrum Wallet op je node aansluiten.


**Let op: Electrum Server en Electrum Wallet zijn verschillende dingen:** de server is software die nodig is voor Electrum Wallet om te kunnen communiceren met de Bitcoin Blockchain - ik weet niet waarom het zo ontworpen is - mogelijk voor de snelheid, maar ik kan het mis hebben.


Als je een node-softwarepakket gebruikt zoals MyNode (degene die ik mensen aanraad om mee te beginnen), Raspiblitz (aanbevolen als je meer gevorderd bent), of Umbrel (persoonlijk raad ik het nog niet aan omdat ik te veel problemen heb ondervonden), dan kun je je Wallet aansluiten door eenvoudigweg het IP Address van de computer (Raspberry Pi) waarop de node draait in te voeren, plus een dubbele punt, en 50002, zoals te zien is in de afbeelding in de vorige sectie. (Verderop zal ik laten zien hoe u het IP Address van uw node kunt vinden).


Open de Netwerkinstellingen (klik op de Green of rode cirkel rechtsonder). Haal het vinkje weg bij "select server automatically", voer dan je IP Address in zoals ik heb gedaan, die van jou zal anders zijn, maar de dubbele punt en "50002" moeten hetzelfde zijn.


![image](assets/18.webp)


Sluit het venster en nu zouden we verbonden moeten zijn met jouw knooppunt. Ter bevestiging klik je nogmaals op de cirkel en controleer je of de servergegevens niet terug zijn veranderd naar een willekeurig knooppunt.


Soms lijkt het alsof hij weigert verbinding te maken, ondanks dat hij alles goed doet. Hier zijn dingen die je kunt proberen..



- Upgrade naar een nieuwere versie van Electrum en je knooppuntsoftware;
- Probeer de cache-map in de map ".electrum" te verwijderen;
- Probeer de poort te wijzigen van 50002 naar 50001 in de netwerkinstellingen;
- Gebruik [deze gids](https://armantheparman.com/tor/) om verbinding te maken met Tor als alternatief;
- Installeer Electrum Server opnieuw op het knooppunt.


## Het IP-adres van uw Node vinden Address


Een IP Address is niet iets dat een gewone gebruiker vaak weet op te zoeken en te gebruiken. Ik heb veel mensen geholpen met het opstarten van een knooppunt en vervolgens hun portemonnee op het knooppunt aan te sluiten - een struikelblok lijkt vaak het vinden van het IP Address te zijn.


Voor MyNode kun je in een browservenster typen: `mynode.local`


Soms werkt "mynode.local" niet (zorg ervoor dat je het niet in een Google zoekbalk typt. Om de navigatiebalk te dwingen je tekst te herkennen als een Address en niet als een zoekopdracht, moet je de tekst vooraf laten gaan door `http://`, zoals dit: `http://mynode.local`. Als dat niet werkt, probeer het dan met een "s", zoals dit: `https://mynode.local`.


Hierdoor krijg je toegang tot het apparaat en kun je op de instellingenlink klikken (zie mijn blauwe "cirkel" hieronder) om dit scherm te laten zien waar het IP Address zich bevindt:


![image](assets/19.webp)


Deze pagina wordt geladen en je ziet het IP-adres van het knooppunt (blauwe "cirkel")


![image](assets/20.webp)


Vervolgens kun je in de toekomst 192.168.0.150, of http://192.168.0.150, in je browser typen.


Voor de Raspiblitz (als je geen scherm aansluit) heb je een andere methode nodig (die ook werkt voor de MyNode):


Log in op de webpagina van je router - hier vinden we de IP Address van al je aangesloten apparaten. De webpagina van de router is een IP Address die je invoert in een webbrowser. De mijne ziet er zo uit:


http://192.168.0.1


Je kunt de inloggegevens voor de router opzoeken in de gebruikershandleiding of soms zelfs op een sticker op de router zelf. Zoek naar de gebruikersnaam en het wachtwoord. Als je die niet kunt vinden, probeer dan Gebruiker: "admin" Wachtwoord: "password"


Als je in staat bent om in te loggen, zie je je aangesloten apparaten en aan de hand van hun namen kan het duidelijk zijn welk knooppunt dat is. De IP Address zal erbij staan.


### Als de eerste twee methoden mislukken, werkt de laatste wel, maar het is vervelend:


Zoek eerst de IP Address van een apparaat in je netwerk (de huidige computer is voldoende).


Op een Mac vind je dit in Netwerkvoorkeuren:


![image](assets/21.webp)


We zijn geïnteresseerd in de eerste 4 Elements (192.168.0), niet in het 4e element, de "166" die je in de afbeelding ziet (die van jou zal anders zijn).


Gebruik voor Linux de opdrachtregel:


```bash
ifconfig | grep inet
```


Die verticale lijn is het "pipe" symbool en vind je onder de <delete> toets. Je ziet nu wat uitvoer en een IP Address. (Negeer 127.0.0.1, dat is het niet, en negeer het netmask)


Voor Windows opent u de opdrachtprompt (cmd) en typt u:


```bash
ipconfig/all
```


en druk op Enter. De IP Address kan worden gevonden in de uitvoer.


Dat was het makkelijke deel. Het Hard deel is nu om het IP Address van jouw node te vinden - we moeten het brute-force raden. Laten we bijvoorbeeld zeggen dat het IP Address van jouw computer begint met 192.168.0.xxx, probeer dan voor jouw knooppunt, in een browser: `https://192.168.0.2`


Het kleinst mogelijke getal is 2 (0 betekent een willekeurig apparaat en 1 is van de router) en het hoogste getal is geloof ik 255 (dit is toevallig 11111111 in binair, het grootste getal dat door 1 byte wordt vastgehouden).


Werk één voor één naar 255 toe. Uiteindelijk zul je stoppen bij het juiste nummer dat je MyNode pagina (of RaspiBlitz pagina) laadt. Dan weet je welk nummer je moet invoeren in je Electrum netwerkinstellingen om verbinding te maken met je node.


Het ziet er ongeveer zo uit (zorg ervoor dat je de dubbele punt en het nummer toevoegt):


![image](assets/22.webp)


**Noot** het is handig om te weten dat deze IP-adressen INTERN zijn binnen je thuisnetwerk. Niemand buiten het netwerk kan ze zien en ze zijn niet gevoelig. Het zijn een beetje zoals extensies in een grote organisatie die je naar verschillende telefoons leiden.


## Verwijder dummy Wallet


Nu hebben we met succes verbinding gemaakt met één en slechts één knooppunt. Dit is hoe Electrum vanaf nu standaard wordt geladen. Je moet nu de dummy Wallet verwijderen (Menu: bestand -> verwijderen), voor het geval je per ongeluk geld stuurt naar deze onveilige Wallet (Hij is onveilig omdat we hem niet op een veilige manier hebben gemaakt).


## Maak een oefen Wallet


Na het verwijderen van de dummy Wallet, begin je opnieuw en maak je een nieuwe, op dezelfde manier, alleen schrijf je deze keer de seed woorden op en bewaar je ze redelijk veilig.


Het is een goed idee om te leren hoe Electrum werkt met deze oefen-WG-72, zonder de omslachtige Hardware Wallet (nodig voor hoge veiligheid). Stop slechts een klein bedrag aan Bitcoin in deze Wallet - ga ervan uit dat je dit geld zult verliezen. Als je het eenmaal onder de knie hebt, leer dan Electrum te gebruiken met een Hardware Wallet.


In de nieuwe Wallet die je hebt gemaakt, zie je een lijst met adressen. De Green adressen worden "ontvangende adressen" genoemd. Ze zijn een product van 3 dingen:



- De seed zin
- De passphrase
- Het afleidingspad


Jullie nieuwe Wallet heeft een set ontvangstadressen die wiskundig en reproduceerbaar kan worden aangemaakt door elke Software Wallet die de seed, passphrase en het afleidingspad heeft. Het zijn er 4,3 miljard! Meer dan je nodig hebt. Electrum laat je alleen de eerste 20 zien, en daarna meer als je de eerste gebruikt.


Meer informatie over Bitcoin private sleutels is te vinden in deze handleiding.


![image](assets/23.webp)


Dit is heel anders dan sommige andere portemonnees die slechts 1 Address per keer presenteren.


Omdat je de seed zin hebt ingevoerd bij het aanmaken van deze Wallet, heeft Electrum de privésleutel voor elk van de adressen en is het mogelijk om geld uit te geven vanaf deze adressen.


Merk ook op dat er gele adressen zijn, "wisselgeldadressen" genaamd - Dit zijn gewoon andere adressen van een andere wiskundige tak (er bestaan er nog eens 4,3 miljard van). Ze worden gebruikt door de Wallet om automatisch overtollig geld terug te sturen naar de Wallet als wisselgeld. Als je bijvoorbeeld 1,5 Bitcoin neemt en 0,5 uitgeeft aan een winkelier, moet de resterende 1,0 ergens naartoe. Je Wallet zal het uitgeven aan de volgende lege gele Address - anders gaat het naar de Miner! Voor meer informatie hierover (UTXO's) zie ![deze gids](https://armantheparman.com/UTXO/).


Ga vervolgens terug naar de Ian Colman private key website en voer de seed in (in plaats van er een te genereren). Je zult zien dat hieronder de informatie over de private en public key verandert; alles hieronder is afhankelijk van wat er boven op de pagina staat.


**Onthoud:** je moet "nooit" de seed van je echte Bitcoin Wallet of een computer invoeren, een malware kan het stelen. We gebruiken alleen een oefen-Wallet om te leren, dus dat is voorlopig prima.


Scroll naar beneden en verander het afleidingspad in BIP84 (SegWit) om overeen te komen met je Electrum Wallet door op de BIP84 tab te klikken.


![image](assets/24.webp)


Daaronder zie je de uitgebreide privésleutel en de uitgebreide openbare sleutel:


![image](assets/25.webp)


Ga naar Electrum en vergelijk dat ze overeenkomen. Er is een menu bovenaan, Wallet ->informatie:


![image](assets/26.webp)


Dit verschijnt:


![image](assets/27.webp)


Merk op dat de twee publieke sleutels overeenkomen.


Vergelijk vervolgens de adressen. Ga terug naar de site van Ian Coleman en scroll naar beneden:


![image](assets/28.webp)


Zie dat ze overeenkomen met de adressen in Electrum.


Nu gaan we de wijzigingsadressen controleren. Scroll iets omhoog naar het afleidingspad en verander de laatste 0 in een 1:


![image](assets/29.webp)


Scroll nu naar beneden en vergelijk de adressen met de gele adressen in Electrum


Waarom hebben we dit allemaal gedaan?


We hebben de seed woorden door twee verschillende onafhankelijke softwareprogramma's gehaald om er zeker van te zijn dat ze ons dezelfde informatie gaven. Dit vermindert het risico aanzienlijk dat kwaadwillende code op de loer ligt en ons valse private of publieke sleutels of adressen geeft.


Het volgende dat je moet doen is een kleine test ontvangen en deze binnen de Wallet uitgeven van de ene Address naar de andere.


## De Wallet testen (leren gebruiken)


Hier laat ik je zien hoe je een UTXO kunt ontvangen in je Wallet en het dan kunt verplaatsen (uitgeven) naar een andere Address binnen de Wallet. Dit is een heel klein bedrag, dat we best willen verliezen.


Dit heeft een aantal doelen.



- Het zal bewijzen dat je de macht hebt om munten uit te geven in de nieuwe Wallet.
- Er wordt gedemonstreerd hoe je de Electrum software gebruikt om een uitgave te maken (en enkele functies), voordat we extra complexiteit toevoegen voor de veiligheid (met behulp van een Hardware Wallet of air-gapped computer)
- Het versterkt het idee dat je veel adressen hebt om uit te kiezen om te ontvangen en uit te geven, binnen dezelfde Wallet.


Open je test Electrum Wallet en klik op het tabblad Adressen, klik dan met de rechtermuisknop op de eerste Address en selecteer Kopiëren -> Address:


![image](assets/30.webp)


De Address zit nu in het geheugen van je computer.


Ga nu naar een Exchange waar je wat Bitcoin hebt, en laten we een klein bedrag opnemen in deze Address, zeg 50.000 Sats. Ik ga Coinbase als voorbeeld gebruiken, omdat het de meest gebruikte Exchange is, ook al zijn ze een vijand van Bitcoin, en ik walg ervan om voor dit doel in te loggen op een oude verlaten account.


Log in en klik op de knop Verzenden/Ontvangen, die vanaf vandaag in de rechterbovenhoek van de webpagina staat.


![image](assets/31.webp)


Ik heb natuurlijk geen tegoeden bij Coinbase, maar stel je voor dat er hier wel tegoeden zijn en volg het proces: Plak de Address van Electrum in het veld "To" zoals ik heb gedaan. Je moet ook een bedrag selecteren (ik stel 50.000 Sats of zo voor). Zet geen "optioneel bericht" - Coinbase verzamelt al genoeg van jouw gegevens (en verkoopt ze), je hoeft ze niet te helpen. Klik ten slotte op "Doorgaan". Daarna weet ik niet welke pop-ups je nog meer krijgt, je bent op jezelf aangewezen, maar de methode is vergelijkbaar voor alle exchanges.


![image](assets/32.webp)


Afhankelijk van de Exchange, kun je de Sats onmiddellijk zien in je Wallet, of enkele uren/dagen.


Merk op dat Electrum je ontvangen munten toont, zelfs als ze niet bevestigd zijn op de Blockchain. De munten die je hebt, worden gelezen van de wachtlijst van een Bitcoin Node, of "Mempool". Wanneer het een blok bereikt, zie je de fondsen als bevestigd.


Nu we een UTXO in onze Wallet hebben, moeten we het labelen. Alleen wij kunnen dit label zien, het heeft niets te maken met de openbare Ledger. Al onze Electrum Labels zijn alleen zichtbaar op de computer die we gebruiken. We kunnen een bestand opslaan en het gebruiken om al onze labels terug te zetten op een andere computer met dezelfde Wallet.


### Maak een label voor een UTXO


Ik had een donatie nodig voor deze test Wallet, met dank aan @Sathoarder voor het leveren van een live UTXO (10.000 Sats), en een andere persoon (anon) doneerde aan dezelfde Address (5000 Sats). Merk op dat er 15.000 Sats in de eerste Address balans staan, en een totaal van 2 transacties (uiterst rechtse kolom). Onderaan is de balans 10.000 Sats bevestigd, en nog eens 5.000 Sats zijn onbevestigd (nog steeds in de Mempool).


![image](assets/33.webp)


Als we nu naar het tabblad Munten gaan, kunnen we twee "ontvangen munten" of UTXO's zien. Ze bevinden zich allebei in dezelfde Address.


![image](assets/34.webp)


Terug naar de Address tab, als je dubbelklikt op het "labels" gebied naast de Address, kun je wat tekst invoeren en vervolgens op <enter> drukken om op te slaan:


![image](assets/35.webp)


Dit is een goede gewoonte, zodat je kunt bijhouden waar je munten vandaan komen, of ze KYC-vrij zijn of niet, en hoeveel elke UTXO je heeft gekost (voor het geval je ze moet verkopen en de belasting moet berekenen die door je overheid van je wordt gestolen).


Idealiter vermijd je het verzamelen van meerdere munten in dezelfde Address. Als je dat toch doet (doe het niet), kun je elke Coin labelen in plaats van ze allemaal met hetzelfde label te labelen volgens de Address methode. Je kunt niet naar het tabblad "munten" gaan en daar de labels bewerken (nee, dat zou te intuïtief zijn!). Je moet naar het tabblad Geschiedenis gaan, de transactie zoeken, die labelen en dan zie je de labels in het Coin gedeelte. Alle labels die je ziet in het muntgedeelte zijn van de Address labels OF de geschiedenislabels, maar elk geschiedenislabel heeft voorrang op elk Address label. Om een back-up te maken van je labels naar een bestand, kun je ze exporteren via het menu bovenaan, Wallet->labels->exporteren.


Laten we vervolgens de munten van de eerste Address uitgeven aan de tweede Address. Rechtsklik op de eerste Address en selecteer "uitgeven van" (Dit is eigenlijk niet nodig in dit scenario, maar stel je voor dat we veel munten op veel adressen hebben; met deze functie kunnen we de Wallet dwingen alleen de munten uit te geven die we willen. Als we meerdere munten op meerdere adressen willen selecteren, kunnen we de adressen selecteren met een klik met de linkermuisknop terwijl we de opdrachttoets ingedrukt houden, dan met de rechtermuisknop klikken en "uitgeven van" selecteren:


![image](assets/36.webp)


Zodra je dat hebt gedaan, verschijnt er een Green balk onderaan het Wallet venster die het aantal munten aangeeft dat je hebt geselecteerd en het totaal dat beschikbaar is om uit te geven.


Je kunt ook individuele munten in een Address uitgeven en andere munten in dezelfde Address uitsluiten, maar dit wordt afgeraden omdat je munten in een Address laat zitten die cryptografisch verzwakt is door het uitgeven van één van de munten (een andere reden om niet meerdere munten in één Address te stoppen, naast privacyredenen, is dat gezien je ze allemaal moet uitgeven als je er één uitgeeft, dit onnodig duur wordt). Hier staat hoe je een enkele Coin kunt selecteren uit een gedeelde Address, maar doe het niet:


![image](assets/37.webp)


Nu hebben we de twee munten geselecteerd om uit te geven. Vervolgens hebben we besloten waar we ze gaan uitgeven. Laten we ze naar de tweede Address sturen. We moeten de Address als volgt kopiëren:


![image](assets/38.webp)


Ga dan naar het tabblad "Verzenden" en plak de tweede Address in het veld "Betalen aan". Je hoeft geen beschrijving toe te voegen; dat zou wel kunnen, maar dat kun je later doen door labels te bewerken. Voor het bedrag selecteer je "Max" om alle munten uit te geven die we hebben geselecteerd. Klik dan op "Betalen" en klik op de knop "Geavanceerd" in het pop-upvenster dat verschijnt.


![image](assets/39.webp)


Klik in dit stadium altijd op "geavanceerd" zodat we de transactie nauwkeurig kunnen controleren. Hier is de transactie:


![image](assets/40.webp)


We zien twee interne witte vakken/vensters. Het bovenste is het invoervenster (welke munten worden uitgegeven) en het onderste is het uitvoervenster (waar de munten naartoe gaan).


Merk op dat de status (linksboven) voorlopig "niet ondertekend" is. Het "Verzonden bedrag" is 0 omdat de munten binnen Wallet worden overgemaakt. De vergoeding is 481 Sats. Merk op dat als het 480 Sats was, de laatste nul eraf zou vallen, zoals dit, 0.0000048 en voor het vermoeide oog kan dit eruit zien als 48 Sats - wees voorzichtig (iets dat Electrum devs zouden moeten oplossen).


De grootte van de transactie verwijst naar de datagrootte in bytes, niet naar de hoeveelheid Bitcoin. De "Replace by fee" staat standaard aan en hiermee kun je de transactie opnieuw versturen met een hogere vergoeding als dat nodig is. Met de LockTime kun je instellen wanneer de transactie geldig is - daar heb ik nog niet mee gespeeld, maar ik raad het gebruik ervan af tenzij je volledig begrijpt wat je doet en wat ervaring hebt met kleine bedragen.


Onderaan hebben we een aantal handige Mining hulpmiddelen om de kosten aan te passen. Het enige wat je hoeft te doen voor interne transfers is het instellen op het minimumtarief van 1 sat/byte. Typ gewoon handmatig het getal in het Target fee veld. Om een geschikte vergoeding voor een externe betaling te controleren, kun je https://Mempool.space raadplegen om te zien hoe druk de Mempool is, en er worden enkele voorgestelde vergoedingen weergegeven.


![image](assets/41.webp)


Ik heb 1 sat/byte geselecteerd.


In het invoervenster zien we twee invoergegevens. De eerste is de donatie van 5000 sat. We zien links de transactie Hash (die we kunnen opzoeken op Blockchain). Ernaast staat een "21" - dit geeft aan dat het uitgang 21 is in die transactie (het is eigenlijk de 22e uitgang, omdat de eerste nul is).


Iets om op te merken hier: UTXO's bestaan alleen binnen een transactie. Om een UTXO uit te geven, moeten we er naar verwijzen en die verwijzing in de invoer van een nieuwe transactie stoppen. De uitvoer wordt dan een nieuwe UTXO en de oude UTXO wordt een STXO (uitvoer van een uitgegeven transactie).


De tweede regel is de donatie van 10.000 sat. Het heeft een "0" naast de transactie Hash waar het vandaan kwam, omdat het de eerste (en mogelijk enige) uitvoer voor die transactie is.


In het onderste venster zien we onze Address. Het totaal van de ingangen van de Bitcoin komt niet helemaal overeen met het totaal van de uitgangen. Het verschil gaat naar de Miner. De Miner kijkt naar het verschil in alle transacties in het blok dat hij probeert te mijnen, en voegt dat getal toe aan zijn beloning. (Mining vergoedingen worden op deze manier volledig losgekoppeld van de transactieketen en beginnen een nieuw leven).


Als we de Mining vergoeding aanpassen, zal de uitvoerwaarde automatisch veranderen.


**Let op de kleur van de adressen in het transactievenster. Vergeet niet dat de Green adressen in je Address tabblad staan. Als een Address Green (of geel) gemarkeerd is in een transactievenster, dan heeft Electrum de Address herkend als één van zijn eigen adressen. Als de Address geen highlight heeft, dan is het een externe Address (extern aan de op dat moment geopende Wallet), en moet je het met extra zorg controleren.


Zodra je alles in de transactie hebt gecontroleerd en zeker weet dat je tevreden bent met welke munten je uitgeeft en waar de munten naartoe gaan, kun je op "afronden" klikken


![image](assets/42.webp)


Nadat je op "afronden" hebt geklikt, kun je geen bewerkingen meer maken - als dat nodig is, moet je dit sluiten en opnieuw beginnen. Merk op dat de knop "voltooien" is veranderd in "exporteren" en dat er nieuwe knoppen zijn verschenen: "opslaan", "combineren", "ondertekenen" en "uitzenden". De "broadcast" knop is grijs omdat de transactie in dit stadium nog niet ondertekend en dus ongeldig is.


Als je op "Sign" klikt, wordt er gevraagd of je een wachtwoord hebt voor de Wallet, waarna de status (rechtsboven) verandert van "Unsigned" in "Signed". Daarna is de knop "Broadcast" beschikbaar.


Nadat je hebt uitgezonden, kun je het transactievenster sluiten. Als je naar de Address tab gaat, zie je nu dat de eerste Address leeg is en dat de tweede Address 1 UTXO heeft.


Opmerking: Je ziet al deze veranderingen zelfs voordat de transactie is gemined tot een blok, of "bevestigd". Dit komt omdat Electrum saldi/transacties bijwerkt op basis van niet alleen de Blockchain gegevens, maar ook de Mempool gegevens. Niet alle wallets doen dit.


Iets om op te wijzen is dat we in plaats van broadcasten, de transactie kunnen opslaan voor later. Het kan worden opgeslagen in de niet-ondertekende of ondertekende status.


Klik op de knop "exporteren" (klik paradoxaal genoeg NIET op de knop "opslaan") en je ziet een aantal opties. De transactie is gecodeerd met tekst en kan daarom op verschillende manieren worden opgeslagen.


![image](assets/43.webp)


Opslaan in een QR-code is erg interessant. Als je hiervoor kiest, verschijnt er een QR:


![image](assets/44.webp)


Je kunt dan een foto maken van de QR code. Er zijn een aantal dingen die je hiermee kunt doen, maar voor nu, laten we zeggen dat je het later terug in de Wallet laadt. Je kunt Electrum afsluiten, de Wallet opnieuw laden en naar het menu Extra gaan:


![image](assets/45.webp)


Hierdoor wordt de camera van je computer geladen. Vervolgens laat je de camera de foto van de QR-code in je telefoon zien en wordt de transactie terug geladen, precies zoals je hem achterliet.


Het is niet intuïtief hoe je een opgeslagen transactie kunt laden, dus let goed op. Het laden van een transactie is geen "tool", maar de optie is verborgen in het tools menu (nog iets dat de Electrum devs zouden moeten oplossen).


Een soortgelijk proces is mogelijk met een transactie die als bestand is opgeslagen. Probeer te oefenen met beide methoden, binnen dezelfde Wallet. Ik zal er hier niet verder op ingaan, maar je kunt deze functie gebruiken om een transactie door te geven tussen dezelfde Wallet op verschillende computers, tussen wallets met meerdere handtekeningen en van en naar hardware wallets. Hier zijn wat instructies.


Terugkomend op de "opslaan" knop - dit is niet de manier om de transactietekst op te slaan. Wat dit eigenlijk doet is de Electrum Wallet vertellen om deze transactie op de lokale computer te herkennen als zijnde ingediend als een betaling. Als je dat per ongeluk doet, zie je de transactie met een klein computericoontje. Je kunt met de rechtermuisknop klikken en de transactie verwijderen - maak je geen zorgen, op deze manier kun je Bitcoin niet verwijderen. Electrum zal dan vergeten dat deze transactie ooit heeft plaatsgevonden, en zal de Sats "terugbetalen" en weergeven op de juiste locatie waar ze werkelijk bestaan.


### Adressen wijzigen


Wijzigingsadressen zijn interessant. Je moet UTXO's begrijpen om deze uitleg te begrijpen. Als je aan een Address een bedrag uitgeeft dat kleiner is dan UTXO, dan gaat de overgebleven Bitcoin naar de Miner, tenzij er een wisseluitgang wordt opgegeven.


Je hebt misschien 6,15 Bitcoin UTXO en je wilt 0,15 Bitcoin uitgeven om te doneren aan demonstranten die worden onderdrukt door de tirannieke "democratische" regering ergens in de wereld. Je zou dan de 6,15 Bitcoin nemen (met behulp van de "spend from" functie in Electrum), en het in een transactie stoppen.


Je plakt de Address van de demonstranten in het veld "pay to", misschien zet je "EndTheFed & WEF" in het veld "description" en bij het bedrag zet je 0,15 Bitcoin en klik je op "pay" en vervolgens op "advanced".


In het transactiescherm zie je voor het invoerscherm de 6,15 Bitcoin UTXO. Voor het uitvoervenster zie je een Address die niet is gemarkeerd (dit is de Address van de protesterende partij) met 0,15 Bitcoin ernaast. Je ziet ook een gele Address met iets minder dan 6,0 Bitcoin. Dit is de verandering Address die automatisch geselecteerd wordt door de Wallet uit een van zijn eigen gele veranderadressen. Het doel van de wisselgeld Address is dat de Wallet er wisselgeldmunten in kan stoppen zonder de beschikbaarheid van de ontvangstadressen te verknoeien waar je misschien plannen voor hebt, of facturen voor hebt gestuurd. Als ze later bijvoorbeeld door klanten gebruikt gaan worden, wil je niet dat je Wallet ze automatisch gebruikt en opvult. Dat is rommelig en slecht voor de privacy.


Merk op dat wanneer je de Mining vergoeding aanpast, het uitvoerbedrag automatisch wordt aangepast, niet het betalingsbedrag.


### Handmatig wisselen of te veel betalen


Dit is echt een interessante functie van Electrum. Je opent het op deze manier.


![image](assets/46.webp)


Je kunt dan meerdere bestemmingen invoeren voor het UTXO saldo dat je uitgeeft, zoals dit:


![image](assets/47.webp)


Plak de Address, typ een komma, dan een spatie, dan het bedrag, dan <enter> en doe het nog een keer. GEEN BEDRAGEN IN HET "BEDRAG" venster invoeren - Electrum zal hier het totaal invullen terwijl je de individuele bedragen in het "Betaal aan" venster invoert.


Hierdoor kun je handmatig bepalen waar het wisselgeld naartoe gaat (bijvoorbeeld een specifieke Address in je Wallet, of een andere Wallet), of je kunt veel mensen tegelijk betalen. Als je totaal niet hoog genoeg is om overeen te komen met de grootte van de UTXO, zal Electrum nog steeds een extra wisselgelduitvoer voor je aanmaken.


De Pay to Many functie biedt ook de mogelijkheid om je eigen "PayJoins" of "CoinJoins" te maken - buiten het bereik van dit artikel, maar ik heb hier een handleiding. (https://armantheparman.com/cj/)


## Portemonnees


Ik wil een Watching Only Wallet demonstreren met behulp van Electrum. Om dat te doen, moet ik eerst "Wallet" definiëren. Er zijn twee manieren waarop "Wallet" wordt gebruikt in Bitcoin:



- Type A, "Wallet" - verwijst naar de software die je adressen en saldi laat zien, bijv. Electrum, Blue Wallet, Sparrow wallet etc.



- Type B, "Wallet" - verwijst naar de unieke verzameling adressen die geassocieerd zijn met de combinatie van onze seed_phrase/passphrase/derivation_path. Er zijn 8,6 miljard adressen in een Wallet (4,3 miljard ontvangende adressen en 4,3 miljard wijzigingsadressen). Als je iets verandert in de seed frase, passphrase of het afleidingspad, krijg je een ongebruikte Wallet met nieuwe, en allemaal unieke, 8,6 miljard lege adressen.


Welk type iemand bedoelt als hij het woord "Wallet" gebruikt, is duidelijk in de context.


## Kijken naar Wallet - een oefening


Het is niet helemaal duidelijk waar een toekijkende Wallet voor dient, maar ik zal eerst uitleggen wat het is, hoe je een oefenwand maakt, en dan komen we later terug op het doel als ik meer uitleg over hardware wallets. (Voor een uitgebreide uitleg over het gebruik van een Hardware Wallet en verschillende specifieke merken, zie hier)


We gaan een gewone dummy Wallet maken (deze keer iets ingewikkelder met een passphrase), en dan de Wallet die erbij hoort. Als je wilt, kun je degene die ik gemaakt heb precies kopiëren, of je eigen Wallet maken - deze Wallet moet je weggooien; gebruik hem niet echt. Begin met het genereren van een seed van 12 woorden met behulp van de Ian Coleman website.


Let op de 12 willekeurige woorden in de schermafbeelding hieronder, en dat ik een passphrase heb ingevoerd in het passphrase veld:


passphrase: "Craig Wright is een leugenaar en een oplichter en hoort in de gevangenis. Ook Ross Ulbricht zou onmiddellijk vrijgelaten moeten worden uit de gevangenis."


De passphrase kan tot 100 karakters lang zijn, en moet idealiter ondubbelzinnig en niet te kort zijn - Degene die ik heb gebruikt is gewoon voor de lol - ik raad over het algemeen aan om hoofdletters en symbolen te vermijden, gewoon om je stress te verminderen bij het proberen van combinaties als je ooit een probleem hebt gehad met het onthouden van je passphrase.


![image](assets/48.webp)


Ga vervolgens in Electrum naar het menu file->new/restore. Typ een unieke naam om een nieuwe Wallet aan te maken en klik op "volgende".


![image](assets/49.webp)


De volgende stappen moet je nu wel kennen, dus ik zal ze zonder foto's opnoemen:



- Standaard Wallet
- Ik heb al een seed
- Kopieer en plak de 12 woorden in het vak of typ ze handmatig in.
- Klik op opties en selecteer BIP39, en klik ook op het passphrase vinkje ("deze seed uitbreiden met aangepaste woorden")
- Voer je passphrase precies zo in als op de Ian Coleman pagina
- Laat de standaard scriptsemantiek en het afleidingspad staan
- U hoeft geen wachtwoord toe te voegen (vergrendelt de Wallet)


Ga nu terug naar de Ian Coleman site, naar de "derivation path" sectie, en klik op de "BIP 84" tab om dezelfde script semantiek te selecteren als de standaard in Electrum (Native SegWit).


![image](assets/50.webp)


De uitgebreide private en publieke sleutels staan hieronder en veranderen wanneer je wijzigingen aanbrengt in het afleidingspad (of iets anders hoger op de pagina).


![image](assets/51.webp)


U ziet ook "BIP32 extended private/public" sleutels - deze moeten voorlopig genegeerd worden.


De Account extended private key kan worden gebruikt om je Wallet volledig te regenereren. De account extended public key kan echter alleen een beperkte versie van dezelfde Wallet produceren (kijken naar Wallet) - Als je deze sleutel in Electrum stopt, zal het nog steeds alle 8,6 miljard adressen produceren die de seed of extended private key zou hebben, maar er zullen geen private keys beschikbaar zijn voor Electrum, dus er is geen uitgave mogelijk. Laten we het nu doen om het punt te demonstreren:


Kopieer de "account extended public key" naar het klembord.


Ga dan naar Electrum, laat de huidige Wallet die we maakten open, en ga naar bestand->nieuw/herstellen. Het proces om de Wallet te maken is een beetje anders dan voorheen:



- Standaard Wallet
- Gebruik een hoofdsleutel
- Plak de uitgebreide openbare sleutel in het vak en ga verder
- Het is niet nodig om een passphrase in te voeren; deze is al onderdeel van de uitgebreide publieke sleutel
- Het is niet nodig om de scriptsemantiek en het afleidingspad in te voeren
- U hoeft geen wachtwoord toe te voegen (vergrendelt de Wallet)


Wanneer de Wallet laadt, moet je merken dat precies dezelfde adressen geladen worden als voorheen, toen de seed werd ingevoerd. Je moet ook zien dat helemaal bovenaan in de titelbalk "Wallet bekijken" staat. Deze Wallet kan je adressen laten zien, en saldi (door saldi te controleren via een node), maar je kunt geen transacties SIGNEREN (omdat de watch Wallet geen privé sleutels heeft).


Wat heeft het dan voor zin?


Eén reden, en niet de belangrijkste, is dat je mogelijk je Wallet en de balans op een computer kunt observeren zonder je privésleutels bloot te stellen aan malware op de computer.


Een andere is dat het VERPLICHT is om betalingen te doen als je ervoor kiest om je privésleutels van de computer te houden; ik zal het uitleggen:


**Hardware wallets (HWW)** werden gemaakt zodat een apparaat je privésleutels veilig kan bewaren (vergrendeld met een PIN), de sleutels nooit kan blootstellen aan een computer (zelfs niet als ze via een kabel verbonden zijn met een computer) en zelf geen verbinding kan maken met het internet. Zo'n apparaat kan zelf geen transacties maken, omdat alle Bitcoin transacties beginnen met een verwijzing naar een UTXO(s) op de Blockchain (die zich op een knooppunt bevindt). Een Wallet moet specificeren in welke transaction ID de UTXO zich bevindt, en welke uitgang van de transactie de uitgang is die uitgegeven moet worden. Pas na het specificeren van de input kan een nieuwe transactie worden aangemaakt, laat staan ondertekend. Hardware wallets kunnen geen transacties aanmaken, omdat ze geen toegang hebben tot UTXO's - ze zijn nergens mee verbonden!


Een uitgebreide publieke sleutel wordt meestal uit de HWW gehaald, en adressen worden dan weergegeven op een computer - veel mensen zullen bekend zijn met de Ledger software of Trezor Suite die adressen en saldi op hun computer laat zien - dit is een kijkende Wallet. Deze programma's kunnen transacties aanmaken, maar niet ondertekenen. Ze kunnen alleen transacties laten ondertekenen door HWW's die met hen verbonden zijn. De HWW neemt de nieuw gegenereerde transactie van de meekijkende Wallet, ondertekent het en stuurt het dan terug naar de computer om het naar een knooppunt te zenden. **Het HWW kan zelf niet uitzenden**, dat doet de verbonden watchende Wallet. Op deze manier werken de twee portemonnees (publieke sleutel Wallet op de computer, en private sleutel Wallet in de HWW) samen om generate te ondertekenen en uit te zenden, terwijl ze ervoor zorgen dat de private sleutels geïsoleerd blijven en uit de buurt blijven van een apparaat met een internetverbinding.


## Gedeeltelijk ondertekende Bitcoin transacties (PSBT's)


Het is mogelijk om een transactie aan te maken en op te slaan in een bestand, later opnieuw te laden, te ondertekenen, op te slaan, later opnieuw te laden en dan uiteindelijk uit te zenden - ik zeg niet dat iemand dit zou moeten doen; het is gewoon iets dat mogelijk is.


Beschouw nu een 3 van 5 multisignature Wallet - 5 private sleutels creëren een Wallet, en 3 zijn er nodig om een transactie volledig te ondertekenen (Zie hier voor meer informatie over multisignature Wallet sleutels). Het is mogelijk om 5 verschillende computers te hebben met elk één van de vijf private sleutels.


Computer één kan een transactie generate maken en ondertekenen. Hij kan het dan opslaan in een bestand en per e-mail naar Computer 2 sturen. Computer 2 kan dan ondertekenen, en zou het bestand kunnen opslaan in een QR-code, en de QR via een Zoom-oproep naar Computer 3 aan de andere kant van de wereld kunnen sturen. Computer 3 kan de QR vastleggen, de transactie in electrum laden en de transactie ondertekenen. Na de eerste 2 handtekeningen was de transactie een PSBT (Partially Signed Bitcoin Transaction). Na de 3e handtekening was de transactie volledig ondertekend en geldig, klaar voor uitzending.


Raadpleeg deze gids voor meer informatie over PSBTS. (https://armantheparman.com/PSBT/)


## Hardware-wallets gebruiken met Electrum


Ik heb een gids over het gebruik van hardware wallets in het algemeen, waarvan ik denk dat het belangrijk is voor mensen die nieuw zijn met HWW's, om te lezen. (https://armantheparman.com/using-hwws/)


Er zijn hier ook handleidingen te vinden over verschillende merken HWW's die op de Sparrow Bitcoin Wallet aangesloten moeten worden. (https://armantheparman.com/hwws/)


Dit wordt mijn eerste gids die laat zien hoe je een Hardware Wallet gebruikt met Electrum - ik ga de ColdCard Hardware Wallet gebruiken om het te demonstreren. Dit is niet bedoeld als een gedetailleerde gids over de ColdCard specifiek, die gids is hier. Ik laat alleen Electrum-specifieke punten zien. (https://armantheparman.com/cc/)


### Verbinding maken via de micro SD-kaart (air-gapped)


Voordat je je echte Wallet aansluit via de ColdCard, hoop ik dat je de eerdere stappen van het laden van een Electrum dummy Wallet en het instellen van de netwerkparameters hebt doorlopen.


Plaats vervolgens de SD-kaart op de ColdCard. Ik ga ervan uit dat je de seed al hebt aangemaakt. Als je toegang hebt tot de Wallet met een passphrase, pas deze dan nu toe. Scroll naar beneden en selecteer het menu Geavanceerd/Tools -> Wallet exporteren -> Electrum Wallet.


Je kunt naar beneden scrollen en het bericht lezen. Het biedt je altijd aan om "1" te selecteren om een niet-nul rekeningnummer in te voeren (iets dat deel uitmaakt van het afleidingspad), maar als je mijn advies hebt opgevolgd, heb je niet gerommeld met de standaard afleidingspaden en wil je dus geen niet-nul rekeningnummer; druk gewoon op het vinkje om verder te gaan.


Selecteer dan de script semantiek. De meeste mensen zullen "Native SegWit" selecteren.


Het zal zeggen "Electrum Wallet bestand geschreven", en de bestandsnaam weergeven. Maak er een notitie van.


Haal dan de micro SD-kaart eruit en stop deze in de computer met Electrum.


Sommige besturingssystemen openen automatisch de bestandsverkenner wanneer u de microSD plaatst. Veel mensen zullen het nieuwe Wallet bestand zien, erop dubbelklikken en zich afvragen waarom het niet werkt. Dat is geen goed ontwerp. Eigenlijk moet u de bestandsverkenner negeren (sluiten) en het Wallet bestand openen met Electrum:


Open Electrum. Als het al open is met een andere Wallet, selecteer dan bestand -> nieuw. We zoeken dit venster:


![image](assets/52.webp)


Hier is de truc, het is niet intuïtief. Klik op "kiezen". Navigeer dan door het bestandssysteem op de microSD-kaart en zoek het Wallet-bestand en open het.


Nu heb je de overeenkomstige Hardware Wallet's geopend om Wallet te bekijken. Leuk.


### Aansluiten via de USB-kabel.


Deze manier zou eenvoudiger moeten zijn, maar voor Linux computers is het veel moeilijker. Iets genaamd "Udev rules" moet worden bijgewerkt. Hier staat hoe (gedetailleerde handleiding https://armantheparman.com/gpg-articles/ ), en in het kort:


Het is een goed idee om te controleren of het systeem up-to-date is. Dan:


```bash
sudo apt-get install libusb-1.0-0-dev libudev-dev
```


dan...


```bash
python3 -m pip install ckcc-protocol
```


Als je een foutmelding krijgt, controleer dan of pip is geïnstalleerd. Je kunt dit controleren met (pip -version), en je kunt het installeren met (sudo apt install pythron3-pip)


Maak of wijzig het bestaande bestand /etc/udev/rules.d/


Zoals dit:


```bash
sudo nano /etc/udev/rules.d
```


Een teksteditor zal openen. Kopieer de tekst van hier en plak het in het bestand rules.d, sla op en sluit af.


![image](assets/53.webp)


Voer dan deze commando's achter elkaar uit:


```bash
sudo groupadd plugdev
sudo usermod -aG plugdev $(whoami)
sudo udevadm control –reload-rules && sudo udevadm trigger
```


Als je de melding "group plugdev" al bestaat, is dat prima, ga verder. Na het tweede commando krijg je geen feedback/antwoord, ga gewoon verder met het derde commando.


Mogelijk moet u de ColdCard loskoppelen van de computer en vervolgens weer aansluiten.


Als u na dit alles nog steeds niet in staat bent om de ColdCard aan te sluiten, zou ik proberen de firmware te updaten (gids binnenkort, maar voor nu kunt u instructies vinden op de website van de fabrikant).


Maak vervolgens een nieuwe Wallet:



- Standaard Wallet
- Een hardwareapparaat gebruiken
- Het zal uw ColdCard scannen en detecteren. Ga verder.
- Selecteer de scriptsemantiek en het afleidingspad
- Beslis of het Wallet bestand versleuteld moet worden (aanbevolen)


### Transacties met de ColdCard


Als de kabel is aangesloten, zijn transacties eenvoudig. Het ondertekenen van transacties verloopt naadloos.


Als je het apparaat in de lucht gebruikt, moet je de opgeslagen transactie handmatig doorgeven tussen apparaten met behulp van de microSD-kaart. Er zijn enkele trucjes.


Nadat je een transactie hebt gemaakt en afgerond, moet je linksonder op de knop Exporteren klikken. Je ziet "opslaan in bestand", wat tegen de verwachting in niet is wat we willen. Je moet eigenlijk eerst naar de allerlaatste menu-optie gaan die zegt "voor hardware wallets", en dan, vanuit die selectie, de andere "opslaan naar bestand" vinden en dat selecteren. Sla vervolgens het bestand op de microSD op, haal de kaart eruit en plaats deze in de ColdCard. Vergeet niet dat u mogelijk een passphrase moet toepassen om de juiste Wallet te selecteren. Het scherm zal zeggen klaar om te ondertekenen. Klik op het vinkje, controleer de transactie en bevestig met het vinkje. Als je klaar bent, haal je de kaart eruit en stop je hem terug in de computer.


Dan moeten we de transactie openen met electrum. De functie is verborgen in het menu tools -> load transaction. Navigeer door het bestandssysteem en zoek het bestand. Elke keer dat je ondertekent, zullen er drie bestanden zijn. Het origineel opgeslagen bestand dat de Watching Wallet maakte, en twee gemaakt door de ColdCard (ik weet niet waarom het dit doet). Op de ene staat "ondertekend" en op de andere "definitief". Het is niet intuïtief, maar de "ondertekende" is niet bruikbaar, we moeten de "definitieve" transactie openen.


Zodra je dat hebt geladen, kun je op "Uitzenden" klikken en wordt de betaling uitgevoerd.


## Electrum en de verborgen ".electrum" map bijwerken


Electrum staat op twee plaatsen op je computer. Er is de applicatie zelf, en er is een verborgen configuratiemap. Die map bevindt zich op verschillende plaatsen, afhankelijk van je besturingssysteem:


Windows:


```bash
C:/Users/your_user_name_goes_here/AppData/Roaming/Electrum
```


Mac:


```bash
/Users/your_user_name_goes_here/.electrum
```


Linux:


```bash
/home/your_user_name_goes_here/.electrum
```


Merk op dat `.` voor `electrum` staat in Linux en Mac - dat geeft aan dat de director verborgen is. Merk ook op dat deze directory pas (automatisch) wordt aangemaakt als je Electrum voor de eerste keer start. De map bevat het configuratiebestand van electrum en ook de map met de wallets die je hebt opgeslagen.


Als je het Electrum-programma van je computer verwijdert, blijft de verborgen map bestaan, tenzij je die ook actief verwijdert.


Om electrum te upgraden, doorloop je dezelfde procedure als ik in het begin beschreef om te downloaden en te verifiëren. Je hebt dan twee kopieën van het programma op je computer, en je kunt ze allebei draaien - elk programma heeft toegang tot dezelfde verborgen electrum map voor zijn configuratie en Wallet toegang. Alle dingen die we hebben opgeslagen, zoals het basisstation, het standaardknooppunt om verbinding mee te maken, andere voorkeuren en toegang tot wallets, blijven bewaard omdat dat allemaal in die map is opgeslagen.


### Je Electrum en Wallets verplaatsen naar een andere computer


Om dit te doen, kun je de programmabestanden kopiëren naar een USB-stick en ook de map .electrum kopiëren. Kopieer of verplaats ze vervolgens naar de nieuwe computer. Je hoeft het programma niet opnieuw te verifiëren. Zorg ervoor dat je de .electrum map kopieert naar de standaard locatie (vergeet niet om deze te kopiëren VOORDAT je Electrum voor de eerste keer start op die computer, anders wordt er een lege standaard .electrum map aangemaakt, en kun je in de war raken).


## Etiketten


Zoals ik al eerder heb uitgelegd, is er op het Address tabblad een labelkolom. Je kunt daar dubbelklikken en notities voor jezelf invoeren (het is alleen op jouw computer, niet openbaar, en niet op de Blockchain).


![image](assets/54.webp)


Als je je Electrum Wallet verplaatst naar een andere computer, wil je misschien niet al deze notities kwijtraken. Je kunt ze opslaan in een bestand met het menu, Wallet > labels > export, en dan op de nieuwe computer, Wallet > labels > import gebruiken.


## Tips:


Als je deze bron nuttig vindt en je wilt ondersteunen wat ik doe voor Bitcoin, dan kun je hier Sats doneren:


Statische bliksem Address: dandysack84@walletofsatoshi.com

https://armantheparman.com/electrum/