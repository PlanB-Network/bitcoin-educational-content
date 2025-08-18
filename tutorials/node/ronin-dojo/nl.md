---
name: RoninDojo

description: Het installeren en gebruiken van je RoninDojo Bitcoin knooppunt.
---
***WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, zijn bepaalde functies van RoninDojo, zoals Whirlpool, niet langer operationeel. Het is echter mogelijk dat deze tools in de komende weken worden hersteld of op een andere manier opnieuw worden gelanceerd. Bovendien, omdat de RoninDojo code werd gehost op Samourai's GitLab, dat ook in beslag werd genomen, is het momenteel niet mogelijk om de code op afstand te downloaden. De RoninDojo teams werken waarschijnlijk aan het opnieuw publiceren van de code.*


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


deze tutorial is gewijd aan de installatie van RoninDojo v1. Om te profiteren van de nieuwste verbeteringen en functies, raad ik je aan om onze tutorial te raadplegen over de directe installatie van RoninDojo v2 op je Raspberry Pi:_

https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Het runnen en gebruiken van je eigen node is essentieel om echt deel te nemen aan het Bitcoin netwerk. Hoewel het runnen van een Bitcoin node geen financiële voordelen oplevert voor de gebruiker, stelt het hem in staat om zijn privacy te bewaren, onafhankelijk te handelen en controle te hebben over zijn vertrouwen in het netwerk.


In dit artikel zullen we een gedetailleerde blik werpen op RoninDojo, een geweldige oplossing om je eigen Bitcoin node te draaien.


### Inhoudsopgave:



- Wat is RoninDojo?
- Welke hardware kiezen?
- Hoe RoninDojo installeren?
- Hoe gebruik je RoninDojo?
- Conclusie


Als je niet weet hoe een Bitcoin node werkt en wat zijn rol is, raad ik je aan om eerst dit artikel te lezen: De Bitcoin Node - Deel 1/2: Technische concepten.


![Samourai](assets/1.webp)


## Wat is RoninDojo?


Dojo is een volledige Bitcoin node server ontwikkeld door het Samourai Wallet team. Je kunt hem vrij installeren op elke machine.


RoninDojo is een installatieassistent en beheertool voor Dojo en verschillende andere tools. RoninDojo neemt de originele implementatie van Dojo en voegt er vele andere tools aan toe, terwijl het ook de installatie en het beheer makkelijker maakt.


Ze bieden ook een "plug-and-play" hardware, de RoninDojo Tanto, met RoninDojo voorgeïnstalleerd op een machine die door hun team is samengesteld. De Tanto is een betaalde oplossing, geschikt voor wie zijn handen niet vuil wil maken.


De code voor RoninDojo is open-source, dus het is ook mogelijk om deze oplossing op je eigen hardware te installeren. Deze optie is kosteneffectief, maar vereist wat meer manipulatie, wat we in dit artikel zullen doen.


RoninDojo is een Dojo, dus je kunt Whirlpool CLI gemakkelijk integreren in je Bitcoin node om de best mogelijke CoinJoin ervaring te hebben. Met Whirlpool CLI kun je niet alleen je bitcoins 24/7 laten remixen zonder je pc aan te hoeven laten staan, maar je kunt ook je privacy sterk verbeteren.


RoninDojo integreert vele andere tools die afhankelijk zijn van je Dojo, zoals de Boltzmann calculator, die het privacy niveau van een transactie bepaalt, de Electrum server om je verschillende Bitcoin wallets met je node te verbinden, of de Mempool server om je transacties privé te observeren.

Vergeleken met een andere node oplossing zoals Umbrel, die ik in dit artikel aan je heb gepresenteerd, is RoninDojo sterk gericht op "on chain" oplossingen en gereedschappen die de privacy van gebruikers optimaliseren. Daarom staat RoninDojo geen interactie met de Lightning Network toe.

RoninDojo biedt minder tools dan Umbrel, maar de weinige essentiële functies voor een Bitcoiner op Ronin zijn ongelooflijk stabiel.


Dus als je niet alle mogelijkheden van een Umbrel server nodig hebt en alleen een eenvoudige en stabiele node wilt met een paar essentiële tools zoals Whirlpool of Mempool, dan is RoninDojo waarschijnlijk een goede oplossing voor jou.


Naar mijn mening is de ontwikkelingsfocus van Umbrel sterk gericht op de Lightning Network en veelzijdige hulpmiddelen. Het is nog steeds een Bitcoin node, maar het doel is om er een multitasking miniserver van te maken. De ontwikkelingsfocus van RoninDojo ligt daarentegen meer op één lijn met de teams van Samourai Wallet en richt zich op de essentiële tools voor een Bitcoiner, waardoor volledige onafhankelijkheid en geoptimaliseerd beheer van privacy op Bitcoin mogelijk is.


Houd er rekening mee dat het opzetten van een RoninDojo knooppunt iets ingewikkelder is dan een Umbrel knooppunt.


Nu we een beeld hebben kunnen schetsen van RoninDojo, laten we eens kijken hoe we dit knooppunt samen kunnen opzetten.


## Welke hardware kiezen?


Om de machine te kiezen die RoninDojo host en draait, heb je verschillende opties.


Zoals eerder uitgelegd is de eenvoudigste keuze om de Tanto te bestellen, een plug-and-play machine die speciaal voor dit doel is ontworpen. Om de jouwe te bestellen, ga hier: [link](https://shop.ronindojo.io/product-category/nodes/).


Omdat de RoninDojo teams open-source code produceren, is het ook mogelijk om RoninDojo op andere machines te implementeren. Je kunt de laatste versies van de installatiewizard op deze pagina vinden: [link](https://ronindojo.io/en/downloads.html), en de laatste versies van de code op deze pagina: [link](https://code.samourai.io/ronindojo/RoninDojo).


Persoonlijk heb ik het geïnstalleerd op een Raspberry Pi 4 8GB en alles werkt perfect.


Houd er echter rekening mee dat de RoninDojo teams aangeven dat er vaak problemen zijn met de case en SSD adapter. Het is daarom niet aan te raden om een behuizing met een kabel voor de SSD van je machine te gebruiken. In plaats daarvan is het beter om een opslaguitbreidingskaart te gebruiken die speciaal ontworpen is voor je moederbord, zoals deze: Raspberry Pi 4 Uitbreidingskaart voor opslag.


Hier is een voorbeeld van hoe je je eigen RoninDojo knooppunt kunt opzetten:



- Een Raspberry Pi 4.
- Een kast met een ventilator.
- Een compatibele geheugenuitbreidingskaart.
- Een voedingskabel.
- Een industriële micro SD-kaart van 16 GB of meer.
- Een SSD van 1 TB of groter.
- Een RJ45 Ethernetkabel, categorie 8 aanbevolen.


## Hoe RoninDojo installeren?


### Stap 1: Maak de opstartbare micro SD-kaart klaar.


Zodra je je machine in elkaar hebt gezet, kun je beginnen met de installatie van RoninDojo. Om dit te doen, begin je met het maken van een opstartbare micro SD kaart door de juiste disk image erop te branden.


Plaats je micro SD kaart in je computer en ga dan naar de officiële RoninDojo website om de RoninOS disk image te downloaden: https://ronindojo.io/en/downloads.html.


Download de schijfimage die overeenkomt met je hardware. In mijn geval heb ik de image "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ" gedownload:


![Download RoninOS disk image](assets/2.webp)


Zodra de image is gedownload, controleer je de integriteit ervan met behulp van het bijbehorende .SHA256-bestand. In dit artikel beschrijf ik in detail hoe je dat doet: Hoe de integriteit van Bitcoin software op Windows controleren?


Specifieke instructies voor het controleren van de integriteit van RoninOS zijn ook beschikbaar op deze pagina: https://wiki.ronindojo.io/en/extras/verify.


Om deze image op je micro SD-kaart te branden, kun je software gebruiken zoals Balena Etcher, die je hier kunt downloaden: https://www.balena.io/etcher/.


Selecteer hiervoor de image in Etcher en flash deze naar de micro SD-kaart:


![Burn disk image with Etcher](assets/3.webp)


Zodra de bewerking voltooid is, kun je de opstartbare micro SD-kaart in de Raspberry Pi steken en de machine inschakelen.


### Stap 2: RoninOS configureren.


RoninOS is het besturingssysteem van je RoninDojo knooppunt. Het is een aangepaste versie van Manjaro, een Linux distributie. Nadat je je machine hebt opgestart en een paar minuten hebt gewacht, kun je beginnen met de configuratie.


Om er op afstand verbinding mee te maken, moet je het IP Address van je RoninDojo machine vinden. Om dit te doen, kun je bijvoorbeeld verbinding maken met het administratiepaneel van je internetbox, of je kunt software downloaden zoals https://angryip.org/ om je lokale netwerk te scannen en het IP van de machine te vinden.


Zodra je het IP hebt gevonden, kun je de controle over je machine overnemen vanaf een andere computer die is aangesloten op hetzelfde lokale netwerk met SSH.


Vanaf een computer met macOS of Linux open je gewoon de terminal. Vanaf een computer met Windows kun je een gespecialiseerd hulpprogramma zoals Putty gebruiken of direct Windows PowerShell gebruiken.


Zodra de terminal geopend is, typt u het volgende commando:

```
ssh root@192.168.?.?
```


Vervang gewoon de twee vraagtekens door het IP-adres van je eerder gevonden RoninDojo.

Tip: Klik in een Shell met de rechtermuisknop om een item te plakken.


Vervolgens kom je in het Manjaro configuratiescherm. Kies de juiste toetsenbordindeling met de pijltjes om het doel te wijzigen in de vervolgkeuzelijst.


![Manjaro Keyboard Configuration](assets/4.webp)


Kies een gebruikersnaam en wachtwoord voor je sessie. Gebruik een sterk wachtwoord en maak een veilige back-up. Je kunt optioneel een zwak wachtwoord gebruiken tijdens de installatie, en het later gemakkelijk wijzigen door het te "kopiëren-plakken" in RoninUI. Hierdoor kun je een heel sterk wachtwoord gebruiken zonder al te veel tijd te besteden aan het handmatig intypen ervan tijdens de installatie van Manjaro.


![Manjaro Username Configuration](assets/5.webp)


Vervolgens wordt u ook gevraagd om een root-wachtwoord te kiezen. Voer voor het root wachtwoord direct een sterk wachtwoord in. Je kunt het niet wijzigen vanuit RoninUI. Vergeet ook niet om een veilige back-up te maken van dit root-wachtwoord.


Voer vervolgens je locatie en tijdzone in.


![Manjaro Time Zone Configuration](assets/6.webp)


![Manjaro Location Configuration](assets/7.webp)


Kies vervolgens een hostnaam.


![Manjaro Hostname Configuration](assets/8.webp)


Controleer tenslotte de configuratie-informatie van Manjaro en bevestig.


![Verification of ManjaroOS Configuration Information](assets/9.webp)


### Stap 3: Download RoninDojo.


De initiële configuratie van RoninOS wordt uitgevoerd. Eenmaal klaar, zoals te zien is in de schermafbeelding hierboven, zal de machine herstarten. Wacht even en voer dan het volgende commando in om opnieuw verbinding te maken met je RoninDojo machine:

```
ssh username@192.168.?.?
```


Vervang gewoon "gebruikersnaam" door de gebruikersnaam die je eerder hebt gekozen en vervang de vraagtekens door het IP-adres van je RoninDojo.


Voer vervolgens uw gebruikerswachtwoord in.


In de terminal ziet het er als volgt uit:


![SSH Connection to RoninOS](assets/10.webp)


Je bent nu verbonden met je machine, die op dit moment alleen RoninOS heeft. Nu moet je RoninDojo erop installeren.


Download de laatste versie van RoninDojo door het volgende commando in te voeren:

```
git clone https://code.samourai.io/ronindojo/RoninDojo
```


Het downloaden zal snel gaan. In de terminal zie je dit:


![Cloning RoninDojo](assets/11.webp)


Wacht tot de download is voltooid, installeer en open dan de RoninDojo gebruiker Interface met het volgende commando:

```
~/RoninDojo/ronin
```


U wordt gevraagd om uw gebruikerswachtwoord in te voeren:


![Bitcoin Node Password Verification](assets/12.webp)


Dit commando is alleen nodig de eerste keer dat je toegang krijgt tot je RoninDojo. Daarna, om toegang te krijgen tot RoninCLI via SSH, moet je gewoon het commando [SSH username@192.168.?.?] invoeren waarbij je "gebruikersnaam" vervangt door je gebruikersnaam en het IP Address van je knooppunt invoert. Je wordt gevraagd om je gebruikerswachtwoord.


Vervolgens zie je deze prachtige animatie:


![RoninCLI launch animation](assets/13.webp)


Dan kom je uiteindelijk bij de RoninDojo CLI gebruiker Interface.


### Stap 4: Installeer RoninDojo.


Navigeer in het hoofdmenu naar het menu "Systeem" met behulp van de pijltjestoetsen op je toetsenbord. Druk op de enter-toets om je keuze te bevestigen.


![RoninCLI navigation menu to System](assets/14.webp)


Ga vervolgens naar het menu "Systeem instellen en installeren".


![RoninCLI navigation menu to RoninDojo system installation](assets/15.webp)


Vink tot slot "System Setup" en "Install RoninDojo" aan met de spatiebalk en selecteer dan "Accept" om de installatie te starten.


![RoninDojo installation confirmation](assets/16.webp)


Laat de installatie rustig doorgaan. In mijn geval duurde het ongeveer 2 uur. Houd je terminal open tijdens het proces.


Controleer af en toe je terminal, omdat je in bepaalde stadia van de installatie wordt gevraagd om op een toets te drukken, zoals hier bijvoorbeeld:


![RoninDojo installation in progress](assets/17.webp)


Aan het einde van de installatie zie je de verschillende containers starten:


![Node container startup](assets/18.webp)


Dan zal je knooppunt herstarten. Maak opnieuw verbinding met RoninCLI voor de volgende stap.


![Bitcoin node restart](assets/19.webp)


### Stap 5: Download de Proof-of-Work keten en open RoninUI.


Zodra de installatie voltooid is, zal je node beginnen met het downloaden van de Bitcoin Proof-of-Work keten. Dit wordt de Initial Block Download (IBD) genoemd. Dit duurt meestal tussen de 2 en 14 dagen, afhankelijk van je internetverbinding en apparaat.


Je kunt de voortgang van het downloaden van de ketting volgen door naar het RoninUI web Interface te gaan.


Om toegang te krijgen vanaf een lokaal netwerk, typ je het volgende in de Address balk van je browser:



- Ofwel voer je direct het IP Address van je machine in (192.168.?.?)
- Of voer in: ronindojo.local


Vergeet niet je VPN uit te schakelen als je er een gebruikt.


### Mogelijke wending


Als je geen verbinding kunt maken met RoninUI vanuit je browser, controleer dan de goede werking van de applicatie vanaf je Terminal die verbonden is met je knooppunt via SSH. Maak verbinding met het hoofdmenu door de vorige stappen te volgen:



- Type: SSH username@192.168.?. vervangen door je referenties.



- Voer uw gebruikerswachtwoord in.


Ga in het hoofdmenu naar: **RoninUI > Opnieuw opstarten**


Als de applicatie correct herstart, is er een probleem met de verbinding vanuit je browser. Controleer of je geen VPN gebruikt en of je verbinding hebt met hetzelfde netwerk als je knooppunt.


Als de herstart een fout oplevert, probeer dan het besturingssysteem bij te werken en vervolgens RoninUI opnieuw te installeren. Om het besturingssysteem bij te werken: **Systeem > Software-updates > Besturingssysteem bijwerken**


Zodra de update en herstart voltooid zijn, maak je opnieuw verbinding met je knooppunt via SSH en installeer je RoninUI opnieuw: **RoninUI > Opnieuw installeren**


Nadat je RoninUI opnieuw hebt gedownload, probeer je verbinding te maken met RoninUI via je browser.


**Tip:** Als je RoninCLI per ongeluk verlaat en je bevindt je op de Manjaro terminal, voer dan het commando "ronin" in om direct terug te keren naar het hoofdmenu van RoninCLI.


### Inloggen op het web


Je kunt ook inloggen op de RoninUI web Interface vanaf elk netwerk met behulp van Tor. Haal hiervoor de Tor Address van je RoninUI op uit RoninCLI: **Credentials > Ronin UI**


Haal de Tor Address eindigend op .onion op en log dan in op Ronin UI door deze Address in te voeren in je Tor browser. Wees voorzichtig dat je verschillende referenties niet uitlekken, aangezien dit gevoelige informatie is.


![RoninUI web login interface](assets/20.webp)


Eenmaal ingelogd, wordt je gevraagd om je gebruikerswachtwoord. Dit is hetzelfde wachtwoord dat je gebruikt om in te loggen via SSH.


![RoninUI web interface management panel](assets/21.webp)


We kunnen de voortgang van de IBD (Initial Block Download) hier zien. Wees geduldig, je haalt alle transacties op die sinds 3 januari 2009 op Bitcoin zijn gedaan.


Na het downloaden van de volledige Blockchain zal de indexer de database comprimeren. Deze operatie duurt ongeveer 12 uur. Je kunt ook de voortgang volgen onder "Indexer" op RoninUI.


Je RoninDojo node zal hierna volledig functioneel zijn:


![Indexer synchronized at 100% functional node](assets/22.webp)


Als je het gebruikerswachtwoord wilt veranderen in een sterker wachtwoord, kun je dat nu doen via het tabblad "Instellingen". Op RoninDojo is er geen extra Layer beveiliging, dus ik raad aan om een echt sterk wachtwoord te kiezen en te zorgen voor een back-up.


## Hoe gebruik je RoninDojo?


Zodra de keten gedownload en gecomprimeerd is, kun je gebruik maken van de diensten die je nieuwe RoninDojo node aanbiedt. Laten we eens kijken hoe je ze kunt gebruiken.


### Wallet software aansluiten op elektrs.


De eerste functie van je nieuw geïnstalleerde en gesynchroniseerde knooppunt is het uitzenden van je transacties naar het Bitcoin netwerk. Daarom zul je waarschijnlijk je verschillende Wallet beheersoftware erop willen aansluiten.


Je kunt dit doen met Electrum Rust Server (electrs). De applicatie is normaal gesproken voorgeïnstalleerd op je RoninDojo knooppunt. Zo niet, dan kun je het handmatig installeren vanuit de RoninCLI Interface.


Ga gewoon naar: **Toepassingen > Toepassingen beheren > Electrum Server installeren**


Om de Tor Address van je Electrum Server te verkrijgen, ga je vanuit het RoninCLI menu naar:

**Credentials > Electrs**


Je hoeft alleen maar de .onion link in te voeren in je Wallet software. Ga bijvoorbeeld in Sparrow wallet naar het tabblad:

**Bestand > Voorkeuren > Server**


Selecteer `Private Electrum` in het servertype en voer vervolgens de Tor Address van je Electrum Server in het corresponderende veld in. Klik ten slotte op "Test verbinding" om je verbinding te testen en op te slaan.


![Sparrow Wallet connection interface to an electrs](assets/23.webp)


### Wallet software aansluiten op Samourai Dojo.


In plaats van Electrs te gebruiken, kun je ook Samourai Dojo gebruiken om je compatibele Software Wallet aan te sluiten op je RoninDojo knooppunt. De Samourai Wallet biedt bijvoorbeeld deze optie.


Om dit te doen scan je gewoon de QR-code van je Dojo. Om toegang te krijgen vanuit RoninUI, klik je op het tabblad "Dashboard" en vervolgens op de knop "Beheren" in het vak van je Dojo. Je ziet dan de QR-codes voor je Dojo en BTC-RPC Explorer. Om ze weer te geven, klik je op "Waarden weergeven".


![Retrieving the connection QR code to Dojo](assets/24.webp)


Om je Samourai Wallet met je Dojo te verbinden, moet je deze QR-code scannen tijdens de installatie van de applicatie:


![Connecting to Dojo from the Samourai Wallet application](assets/25.webp)


### Gebruik je eigen Mempool Explorer.


De verkenner is een essentieel hulpmiddel voor Bitcoiners en stelt u in staat om verschillende informatie over de Bitcoin-keten te controleren. Met Mempool kunt u bijvoorbeeld in real-time de kosten controleren die andere gebruikers in rekening brengen, zodat u uw eigen kosten hierop kunt afstemmen. U kunt ook de bevestigingsstatus van een van uw transacties controleren of het saldo van een Address bekijken.


Deze verkennerstools kunnen je blootstellen aan privacyrisico's en vereisen dat je de database van een derde partij vertrouwt. Als je deze online tool gebruikt zonder je eigen knooppunt te doorlopen:



- Je loopt het risico informatie over je Wallet te lekken.



- Je vertrouwt de websitebeheerder voor de Proof-of-Work keten die ze hosten.


Om deze risico's te vermijden, kun je je eigen Mempool instantie op je node gebruiken via het Tor netwerk. Met deze oplossing behoud je niet alleen je privacy bij het gebruik van de dienst, maar hoef je ook niet langer een provider te vertrouwen omdat je je eigen database raadpleegt.


Om dit te doen, begin je met het installeren van Mempool Space Visualizer vanuit RoninCLI:


**Toepassingen > Toepassingen beheren > Mempool Ruimtevisualisator installeren**


Eenmaal geïnstalleerd, haal je de link naar je Mempool op. Met de Tor Address heb je toegang vanaf elk netwerk. Op dezelfde manier halen we deze link op via RoninCLI:


**Credentials > Mempool**


![Retrieve Tor Mempool address](assets/26.webp)


Voer gewoon je Mempool Tor Address in de Tor browser in om te genieten van je eigen Mempool instantie, gebaseerd op je eigen gegevens. Ik raad aan om deze Tor Address toe te voegen aan je favorieten voor snellere toegang. Je kunt ook een snelkoppeling maken op je bureaublad.


![Mempool Space interface](assets/27.webp)


Als je de Tor browser nog niet hebt, kun je deze hier downloaden: https://www.torproject.org/download/


Je hebt ook toegang vanaf je smartphone door Tor Browser te installeren en dezelfde Address in te voeren. Van overal kun je de toestand van de Bitcoin keten bekijken met je eigen node.


### Whirlpool CLI gebruiken.


Je RoninDojo node bevat ook WhirlpoolCLI, een remote command-line Interface voor het automatiseren van Whirlpool mixen.


Wanneer je een CoinJoin uitvoert met de Whirlpool implementatie, moet de applicatie die je gebruikt open blijven om mixen en remixen uit te voeren. Dit proces kan vervelend zijn voor gebruikers die hoge anon-sets willen hebben, omdat het apparaat dat de toepassing met Whirlpool host constant aan moet blijven. Praktisch gezien betekent dit dat als je je UTXO's wilt betrekken bij 24/7 remixen, je je eigen computer of telefoon constant aan moet houden met de applicatie open.


Een oplossing voor deze beperking is om WhirlpoolCLI te gebruiken op een machine die bedoeld is om constant aan te staan, zoals een Bitcoin knooppunt. Hierdoor kunnen onze UTXO's 24/7 worden geremixed zonder dat het nodig is om een andere machine dan ons Bitcoin knooppunt draaiende te houden.

WhirlpoolCLI wordt gebruikt in combinatie met WhirlpoolGUI, een grafisch Interface programma dat op een pc geïnstalleerd moet worden om Coinjoins eenvoudig te beheren. In dit artikel leg ik in detail uit hoe je Whirlpool CLI kunt instellen met je eigen dojo: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).


Om meer te weten te komen over CoinJoin in het algemeen, leg ik alles uit in dit artikel: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).


### Whirlpool Stat Tool gebruiken.


Na het uitvoeren van CoinJoins met Whirlpool, wilt u misschien weten wat het werkelijke niveau van privacy van uw gemengde UTXO's is. Met Whirlpool Stat Tool kunt u dit eenvoudig doen. Met deze tool kunt u de prospectieve score en de retrospectieve score van uw gemengde UTXO's berekenen. Om meer te weten te komen over het berekenen van deze Anon Sets en hoe ze werken, raad ik je aan deze sectie te lezen: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).


De tool is vooraf geïnstalleerd op je RoninDojo. Op dit moment is het alleen beschikbaar via RoninCLI. Om het te starten vanuit het hoofdmenu, ga naar:

**Samourai Toolkit > Whirlpool Stat Tool**


De gebruiksaanwijzing verschijnt. Als je klaar bent, druk je op een willekeurige toets om de commandoregels te openen:


![Whirlpool Stats Tool software home](assets/28.webp)


De terminal geeft weer:

**wst#/tmp>**


Om deze Interface te verlaten en terug te keren naar het RoninCLI menu, voer je gewoon het commando in:

```
quit
```


Om te beginnen stellen we de proxy in op Tor om OXT-gegevens met volledige privacy te extraheren. Voer het commando in:

```
socks5 127.0.0.1:9050
```


Download vervolgens de gegevens van de pool die je transactie bevat:

```
download 0001
```


**Noot:** vervang `0001` door de zwembad denominatie code die je interesseert.


De denominatiecodes zijn als volgt op WST:



- Pool 0,5 bitcoins: 05
- Pool 0,05 bitmunten: 005
- Pool 0,01 bitcoins: 001
- Pool 0,001 bitcoins: 0001


![Downloading data from pool 0001 from OXT](assets/29.webp)


Zodra de gegevens zijn gedownload, laadt u ze met de opdracht:

```
load 0001
```


**Noot:** vervang `0001` door de zwembad denominatie code die je interesseert.


![Loading data from pool 0001](assets/30.webp)

Laat het laadproces plaatsvinden, dit kan een paar minuten duren. Typ na het laden van de gegevens het scorecommando gevolgd door je txid (transactie-ID) om de Anon Sets te verkrijgen:

```
score TXID
```


**Noot:** vervang `txid` door de identificatie van je transactie.


![Printing the prospective and retrospective scores of the given TXID](assets/31.webp)


WST toont dan de retrospectieve score (Backward-looking metrics) gevolgd door de prospectieve score (Forward-looking metrics). Naast de scores van de Anon Sets geeft WST je ook de verspreidingsgraad van je output in de pool op basis van de Anon Set.


Let op: de prospectieve score van je UTXO wordt berekend op basis van de txid van je eerste mix, niet je laatste mix. Omgekeerd wordt de retrospectieve score van een UTXO berekend op basis van de txid van de laatste cyclus.


Nogmaals, als je deze concepten van Anon Sets niet begrijpt, raad ik je aan dit deel van mijn artikel over CoinJoin te lezen, waar ik alles in detail uitleg met diagrammen: [https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)


### Met behulp van de Boltzmann-calculator.


De Boltzmann calculator is een tool waarmee je eenvoudig verschillende geavanceerde statistieken van een Bitcoin transactie kunt berekenen, waaronder het entropie niveau. Met al deze gegevens kun je het niveau van privacy van een transactie kwantificeren en mogelijke fouten detecteren. Deze tool is vooraf geïnstalleerd op je RoninDojo node.


Om toegang te krijgen vanuit RoninCLI, maak je verbinding via SSH en ga je naar het menu:

**Samourai Toolkit > Boltzmann-berekenaar**


Voordat ik uitleg hoe je deze kunt gebruiken op RoninDojo, zal ik uitleggen wat deze statistieken voorstellen, hoe ze worden berekend en waar ze voor worden gebruikt.


Deze indicatoren kunnen worden gebruikt voor elke Bitcoin transactie, maar ze zijn vooral interessant om de kwaliteit van een CoinJoin transactie te bestuderen.


1. De eerste indicator die deze software berekent is het aantal mogelijke combinaties. Dit wordt op de rekenmachine genoteerd als "nb combinaties". Gegeven de waarden van de UTXO's vertegenwoordigt deze indicator het aantal mogelijke toewijzingen van ingangen naar uitgangen.


**note:** als je niet bekend bent met de term `UTXO`, raad ik je aan dit korte artikel te lezen:


> Mechanisme van een Bitcoin transactie: UTXO, ingangen en uitgangen.

Met andere woorden, deze indicator vertegenwoordigt het aantal mogelijke interpretaties voor een gegeven transactie. Bijvoorbeeld, een Whirlpool 5x5 CoinJoin structuur heeft een aantal mogelijke combinaties gelijk aan 1496:


![Schema of a Coinjoin transaction on kycp.org](assets/32.webp)


Krediet: KYCP


2. De tweede berekende indicator is de entropie van een transactie. Omdat het aantal mogelijke combinaties voor een transactie erg hoog kan zijn, kan ervoor gekozen worden om in plaats daarvan entropie te gebruiken. Entropie vertegenwoordigt de binaire logaritme van het aantal mogelijke combinaties. De formule is als volgt:



- E: entropie van de transactie.
- C: aantal mogelijke combinaties voor de transactie.


**E = log2(C)**


In de wiskunde is de binaire logaritme (basis 2) de inverse functie van de macht van 2-functie. Met andere woorden, de binaire logaritme van x is de macht waartoe het getal 2 verheven moet worden om de waarde x te verkrijgen.


Dus:


**E = log2(C)**


**C = 2^E**


Deze indicator wordt uitgedrukt in bits. Hier is bijvoorbeeld de berekening van de entropie van een Whirlpool 5x5 CoinJoin transactie, met een eerder genoemd aantal mogelijke combinaties gelijk aan 1496:


**C = 1496**


**E = log2(1496)**


**E = 10,5469 bits**


Daarom heeft deze CoinJoin transactie een entropie van 10,5469 bits, wat erg goed is.


Hoe hoger deze indicator is, hoe meer verschillende interpretaties van de transactie er zijn en hoe vertrouwelijker de transactie dus is.


Laten we een ander voorbeeld nemen. Hier is een "klassieke" transactie met één invoer en twee uitgangen:


![Bitcoin transaction schema on oxt.me](assets/34.webp)


Krediet: OXT


Deze transactie kan maar op één manier worden geïnterpreteerd:


**[(inp 0) > (Outp 0 ; Outp 1)]**


Dus zal de entropie gelijk zijn aan 0:


**C = 1**,

**E = log2(C)**,

**E = 0**


3. De derde indicator die de Boltzmann calculator teruggeeft is de efficiëntie van de Tx genaamd "Wallet Efficiëntie". Deze indicator vergelijkt eenvoudig de ingevoerde transactie met de best mogelijke transactie in dezelfde configuratie.


We zullen nu het concept van maximale entropie introduceren, dat de hoogst haalbare entropie voor een gegeven transactiestructuur vertegenwoordigt. Bijvoorbeeld, een Whirlpool 5x5 CoinJoin structuur zal een maximale entropie van 10,5469 hebben. De efficiëntie indicator vergelijkt deze maximale entropie met de werkelijke entropie van de invoer transactie. De formule is als volgt:



- ER: Werkelijke entropie uitgedrukt in bits.
- EM: Maximale entropie met dezelfde structuur uitgedrukt in bits.
- Ef: Efficiëntie uitgedrukt in bits.


**Ef = ER - EM**


**Ef = 10,5469 - 10,5469**


**Ef = 0 bits**


Deze indicator wordt ook uitgedrukt als percentage, dus de formule wordt:



- CR: Werkelijk aantal mogelijke combinaties.
- CM: Maximaal aantal mogelijke combinaties met dezelfde structuur.
- Ef: Efficiëntie uitgedrukt als percentage.


**Ef = CR/CM**


**Ef = 1496/1496**


**Ef = 100%**


Een efficiëntie van 100% betekent dat deze transactie de hoogst mogelijke privacy heeft in verhouding tot de structuur.


4. De vierde berekende indicator is entropiedichtheid. Hiermee kunnen we de entropie relateren aan elke invoer of uitvoer. Deze indicator kan worden gebruikt om de efficiëntie tussen transacties van verschillende grootte te vergelijken.


De berekening is heel eenvoudig: we delen de entropie van de transactie door het aantal aanwezige in- en uitgangen. Bijvoorbeeld, voor een Whirlpool 5x5 CoinJoin, zouden we hebben:


ED: Entropiedichtheid uitgedrukt in bits.

E: Transactie-entropie uitgedrukt in bits.

T: Totaal aantal in- en uitgangen in de transactie.


T = 5 + 5 = 10

ED = E / T

ED = 10,5469 / 10

ED = 1,054 bits


Het vijfde stukje informatie dat de Boltzmann calculator geeft is de waarschijnlijkheidstabel van verbanden tussen inputs en outputs. Deze tabel geeft je simpelweg de waarschijnlijkheid (Boltzmann score) dat een bepaalde invoer overeenkomt met een bepaalde uitvoer.


Als we ons voorbeeld nemen met een Whirlpool CoinJoin, dan zou de waarschijnlijkheidstabel zijn:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Hier kunnen we zien dat elke ingang een gelijke waarschijnlijkheid heeft om gekoppeld te worden aan elke uitgang.


Als we echter het voorbeeld nemen van een transactie met één invoer en twee uitgangen, dan zou het er als volgt uitzien:


| Input | Output 0 | Output 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

In dit voorbeeld kunnen we zien dat de waarschijnlijkheid dat elke uitgang van ingang 0 komt 100% is.


Hoe lager deze waarschijnlijkheid, hoe hoger het niveau van privacy.


6. De zesde informatie die wordt berekend is het aantal deterministische links. De verhouding van deterministische koppelingen wordt ook gegeven. Deze indicator geeft het aantal links aan tussen inputs en outputs van de gegeven transactie die een waarschijnlijkheid van 100% hebben, wat betekent dat ze onbetwistbaar zijn.


De ratio geeft het aantal deterministische links in de transactie aan ten opzichte van het totale aantal links.


Bijvoorbeeld, een CoinJoin Whirlpool transactie heeft geen deterministische verbanden tussen inputs en outputs. De indicator zal nul zijn en de ratio ook 0%.


Voor de tweede bestudeerde transactie (1 input en 2 output) is de indicator echter 2 en is de ratio 100%.


Als deze indicator nul is, wijst dat dus op een goede privacy.


Nu we de indicatoren hebben bestudeerd, laten we eens kijken hoe we ze kunnen berekenen met deze software. Ga vanuit RoninCLI naar het menu:

**Samourai Toolkit > Boltzmann-berekenaar**


![Boltzmann Calculator software homepage](assets/35.webp)


Zodra de software is opgestart, voer je de transaction ID in die je wilt bestuderen. Je kunt meerdere transacties tegelijk invoeren door ze te scheiden met een komma en vervolgens op enter te drukken:


![Enter a TXID to study on Boltzmann Calculator](assets/36.webp)


De calculator zal dan alle indicatoren teruggeven die we eerder hebben gezien:


![Printing of Boltzmann Calculator data for this TXID](assets/37.webp)


Typ het commando "Afsluiten" om de software af te sluiten en terug te keren naar het RoninCLI menu.


Om meer te leren over de Boltzmann-calculator, raad ik aan deze artikelen te lezen:



- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159



- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf


### Bisq verbinden.


Bisq is een peer-to-peer Exchange platform waarmee je bitcoins kunt kopen en verkopen. Het wordt gebruikt met een desktopsoftware die op Tor draait en waarmee je Exchange bitcoins kunt kopen zonder dat je je identiteit hoeft op te geven.

Bisq beveiligt peer-to-peer uitwisselingen door middel van een 2/2 multi-handtekening systeem. Je kunt deze software gebruiken met je eigen RoninDojo knooppunt om de privacy van je uitwisselingen te optimaliseren en de gegevens van de Blockchain van je eigen knooppunt te vertrouwen.


Ga om de Bisq-software te downloaden naar hun officiële website: https://bisq.network/


Om met de software aan de slag te gaan, raad ik aan deze pagina te lezen: https://bisq.network/getting-started/


Om de verbindingslink van je RoninDojo op te halen, moet je verbinding maken met RoninCLI via SSH. Ga dan naar het menu:

**Toepassingen > Toepassingen beheren**


Voer je wachtwoord in en vink het vakje aan met de spatietoets:

**[ ] Bisq-verbinding inschakelen**


Bevestig je keuze. Laat je node installeren en haal dan de Tor V3 Address op uit:

**Credentials > bitcoind**


Kopieer de Address onder "Bitcoin daemon".


Je kunt ook je bitcoind Tor V3 Address uit de RoninUI Interface halen door simpelweg op "Beheren" te klikken in het vak "Bitcoin core" op het "Dashboard":


![Retrieve TorV3 Bitcoin Daemon address on RoninUI](assets/38.webp)


Om je knooppunt vanuit Bisq aan te sluiten, ga je naar het menu:

**Instellingen > Netwerkinfo**


![Access the node connection interface from the Bisq software](assets/39.webp)


Klik op de bel "Gebruik aangepaste Bitcoin core nodes". Voer dan je Bitcoin TorV3 Address in in het daarvoor bestemde vak, met de ".onion" maar zonder de "http://".


![Box to enter the TorV3 address of your node in the Bisq software](assets/40.webp)


Start de Bisq-software opnieuw op. Uw knooppunt is nu verbonden met uw Bisq.


### Andere kenmerken.


Je RoninDojo knooppunt bevat ook andere basisfuncties. Je hebt de mogelijkheid om specifieke informatie te scannen om er zeker van te zijn dat er rekening mee wordt gehouden.


Bijvoorbeeld, het is soms mogelijk dat je Wallet verbonden met je RoninDojo de bitcoins die van jou zijn niet vindt. Het saldo is 0, ook al weet je zeker dat je Bitcoin in deze Wallet hebt. Er zijn veel mogelijke oorzaken, waaronder een fout in de afleidingspaden, en het is ook mogelijk dat je node je adressen niet waarneemt.


Om dit op te lossen kun je controleren of je knooppunt je xpub volgt met de "xpub tool". Om het te openen vanuit RoninUI, ga naar het menu:

**Onderhoud > XPUB Gereedschap**


Voer de problematische xpub in en klik op "Controleren" om deze informatie te verifiëren.


![XPUB Tool from RoninUI](assets/41.webp)


Als je xpub wordt gevolgd door het knooppunt, zie je dit verschijnen:


![XPUB Tool result showing successful analysis](assets/42.webp)


Controleer of alle transacties correct worden weergegeven. Controleer ook of het afleidingstype overeenkomt met dat van je Wallet. Hier zien we dat het knooppunt deze xpub interpreteert als een BIP44-derivaat. Als dit afleidingstype niet overeenkomt met dat van uw Wallet, klik dan op de knop "Retype" en selecteer vervolgens BIP44/BIP49/BIP84, afhankelijk van uw keuze:


![Change the derivation type of the studied xpub from RoninUI](assets/43.webp)


Als je xpub niet wordt bijgehouden door je knooppunt, zie je dit scherm waarin je wordt uitgenodigd om het te importeren:


![Import an xpub with XPUB Tool on RoninUI](assets/44.webp)


Je kunt ook andere onderhoudshulpmiddelen gebruiken:



- Transactietool: Hiermee kunt u de details van een specifieke transactie bekijken.
- Address Tool: Hiermee kun je controleren of een specifieke Address wordt gevolgd door je Dojo.
- Blokken opnieuw scannen: Forceert je knooppunt om een geselecteerd bereik van blokken opnieuw te scannen.


Je vindt ook de "Push Tx" tool op RoninUI. Hiermee kun je een ondertekende transactie uitzenden naar het Bitcoin netwerk. Het moet worden ingevoerd in hexadecimaal formaat:


![Tool for broadcasting a signed transaction from RoninUI](assets/45.webp)


## Conclusie.


We hebben gezien hoe je RoninDojo installeert en ermee aan de slag gaat. Het is een uitstekende keuze voor het runnen van je eigen Bitcoin node. Het is een stabiele oplossing die alle essentiële tools voor een Bitcoiner integreert en up-to-date houdt.


Als het gebruik van de terminal je niet afschrikt en als je geen tools nodig hebt die gerelateerd zijn aan de Lightning Network, dan kan RoninDojo je aanspreken.


Als je kunt, overweeg dan om een donatie te doen aan de ontwikkelaars die deze open-source software gratis voor je maken: https://donate.ronindojo.io/


Om meer te weten te komen over RoninDojo, raad ik je aan om de links in mijn externe bronnen hieronder te bekijken.


### Verder lezen:



- CoinJoin begrijpen en gebruiken op Bitcoin.
- Hash functies - uittreksel uit het ebook Bitcoin Démocratisé 1.
- Alles wat je moet weten over de Bitcoin passphrase.


### Externe bronnen:



- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/