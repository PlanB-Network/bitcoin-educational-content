---
name: RoninDojo v2
description: Installatie van je RoninDojo v2 Bitcoin knooppunt op een Raspberry Pi
---
![cover RoninDojo v2](assets/cover.webp)


**WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, zijn bepaalde functies van RoninDojo, zoals Whirlpool, niet langer operationeel. Het is echter mogelijk dat deze tools in de komende weken worden hersteld of op een andere manier opnieuw worden gelanceerd. Bovendien, omdat de RoninDojo code werd gehost op Samourai's GitLab, dat ook in beslag werd genomen, is het momenteel niet mogelijk om de code op afstand te downloaden. De RoninDojo teams werken waarschijnlijk aan het opnieuw publiceren van de code.*


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

> Gebruik Bitcoin met privacy.

In een vorige tutorial hebben we al uitgelegd hoe je RoninDojo v1 installeert en gebruikt. Het afgelopen jaar hebben de RoninDojo teams echter versie 2 van hun implementatie gelanceerd, wat een belangrijk keerpunt betekende in de architectuur van de software. Ze zijn namelijk afgestapt van de Linux Manjaro distributie ten gunste van Debian. Daarom bieden ze niet langer een voorgeconfigureerd image voor automatische installatie op de Raspberry Pi. Maar er is nog wel een methode voor handmatige installatie. Dit is wat ik heb gebruikt voor mijn eigen node, en sindsdien werkt RoninDojo v2 fantastisch op mijn Raspberry Pi 4. Daarom bied ik een nieuwe tutorial aan over hoe je RoninDojo v2 handmatig installeert op een Raspberry Pi.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0

## Inhoudsopgave:


- Wat is RoninDojo?
- Welke hardware moet ik kiezen om RoninDojo v2 te installeren?
- Hoe zet je de Raspberry Pi 4 in elkaar?
- Hoe installeer ik RoninDojo v2 op een Raspberry Pi 4?
- Hoe gebruik je je RoninDojo v2 knooppunt?


## Wat is RoninDojo?

Dojo is in eerste instantie een volledige Bitcoin node implementatie, gebaseerd op Bitcoin core en ontwikkeld door de Samourai Wallet teams. Deze oplossing kan op alle apparatuur geïnstalleerd worden. In tegenstelling tot andere Core implementaties, is Dojo specifiek geoptimaliseerd om te integreren met de Android applicatieomgeving van Samourai Wallet. RoninDojo is een hulpprogramma dat is ontworpen om de installatie en het beheer van een Dojo te vergemakkelijken, evenals verschillende andere aanvullende tools. Kortom, RoninDojo verrijkt de basisimplementatie van Dojo door een groot aantal aanvullende tools te integreren, terwijl het de installatie en het beheer vereenvoudigt.


Ronin biedt ook [een node-in-box oplossing, genaamd de "*Tanto*"](https://ronindojo.io/en/products), een apparaat waarop RoninDojo al is geïnstalleerd op een systeem dat door hun team is samengesteld. De Tanto is een betaalde optie, die interessant kan zijn voor degenen die technische complicaties willen vermijden. Maar omdat de broncode van RoninDojo open is, is het ook mogelijk om het op je eigen hardware te installeren. Dit alternatief is voordeliger, maar vereist wel enkele extra manipulaties, die we in deze tutorial zullen behandelen.

RoninDojo is een Dojo, waardoor Whirlpool CLI gemakkelijk geïntegreerd kan worden in je Bitcoin node om de best mogelijke CoinJoin ervaring te bieden. Met Whirlpool CLI wordt het mogelijk om continu je bitcoins te remixen, 24 uur per dag, 7 dagen per week, zonder dat je pc aan hoeft te staan.


Buiten Whirlpool CLI, bevat RoninDojo een verscheidenheid aan gereedschappen om de functionaliteit van je Dojo te verbeteren. De Boltzmann calculator analyseert het privacy niveau van je transacties, de Electrum server maakt het mogelijk om je Bitcoin wallets met je node te verbinden en de Mempool server maakt het mogelijk om je transacties lokaal te bekijken, zonder informatie te lekken.


Vergeleken met andere node-oplossingen zoals Umbrel, is RoninDojo duidelijk gericht op On-Chain oplossingen en privacy tools. In tegenstelling tot Umbrel biedt RoninDojo geen ondersteuning voor het opzetten van een Lightning node of de integratie van meer generalistische servertoepassingen. Hoewel RoninDojo minder veelzijdige tools biedt dan Umbrel, heeft het alle essentiële functionaliteiten voor het beheren van je On-Chain activiteit.


Als je geen behoefte hebt aan generalistische functionaliteiten of functionaliteiten gerelateerd aan Lightning Network zoals aangeboden door Umbrel, en je bent op zoek naar een eenvoudige, stabiele node met essentiële tools zoals Whirlpool of Mempool, dan kan RoninDojo de ideale oplossing zijn. Terwijl Umbrel de neiging heeft om een mini multitasking server te worden, gericht op de Lightning Network en veelzijdigheid, richt RoninDojo zich, in lijn met de filosofie van Samourai Wallet, op fundamentele tools voor de privacy van de gebruiker.


Nu we RoninDojo hebben geschetst, laten we samen kijken hoe we dit knooppunt kunnen opzetten.


## Welke hardware moet ik kiezen om RoninDojo v2 te installeren?

RoninDojo biedt een afbeelding voor de automatische installatie van zijn software op een [RockPro64] (https://ronindojo.io/en/download). Onze handleiding richt zich echter op de handmatige installatieprocedure op een Raspberry Pi 4. Hoewel de Raspberry Pi 5 onlangs gelanceerd is, en deze handleiding theoretisch compatibel zou moeten zijn met dit nieuwe model, heb ik nog niet de kans gehad om het persoonlijk te testen, en ik heb geen feedback uit de gemeenschap gevonden. Zodra ik de Pi 5 en compatibele onderdelen heb, zal ik deze handleiding bijwerken om jullie op de hoogte te houden. In de tussentijd raad ik aan om voorrang te geven aan de Pi 4, omdat die perfect werkt voor mijn knooppunt.

Zelf draai ik RoninDojo op een Raspberry Pi met 8 GB RAM. Hoewel sommige leden van de gemeenschap erin geslaagd zijn om het werkend te krijgen op apparaten met slechts 4 GB RAM, heb ik deze configuratie zelf niet getest. Gezien het kleine prijsverschil lijkt het verstandig om te kiezen voor de 8 GB RAM versie. Dit kan ook handig zijn als je van plan bent om je Raspberry Pi in de toekomst voor andere doeleinden te gebruiken.

Het is belangrijk om op te merken dat de RoninDojo teams regelmatig problemen hebben gemeld met betrekking tot de behuizing en de SSD-adapter. Ik heb deze problemen zelf ook ondervonden. **Daarom wordt het sterk aangeraden om behuizingen met een USB-kabel voor de SSD van je node te vermijden.** Geef in plaats daarvan de voorkeur aan een opslaguitbreidingskaart die speciaal is ontworpen voor je Raspberry Pi:


![storage expansion card RPI4](assets/notext/1.webp)


Om de Bitcoin Blockchain op te slaan, heb je een SSD nodig die compatibel is met de opslaguitbreidingskaart die je hebt gekozen. Op dit moment (februari 2024) bevinden we ons in een overgangsfase. Er wordt verwacht dat over een paar maanden schijven van 1 TB niet meer voldoende zullen zijn om de groeiende omvang van de Blockchain te bevatten, vooral gezien de verschillende toepassingen die je in je node wilt integreren. Sommigen raden daarom aan om te investeren in een 2 TB SSD voor de gemoedsrust op de lange termijn. Echter, met de dalende trend in SSD prijzen jaar na jaar, stellen anderen voor om genoegen te nemen met een 1 TB schijf, die voldoende zou moeten zijn voor één of twee jaar, met het argument dat tegen de tijd dat deze verouderd is, de kosten van 2 TB modellen waarschijnlijk gedaald zullen zijn. De keuze hangt dus af van je persoonlijke voorkeuren. Als je van plan bent om je RoninDojo voor een lange tijd te houden en technische problemen in de komende jaren wilt vermijden, lijkt de optie van een 2 TB SSD het meest verstandig, omdat het je een comfortabele marge voor de toekomst biedt.


Daarnaast heb je verschillende kleine onderdelen nodig:


- Een behuizing met een ventilator voor je Raspberry Pi en je opslaguitbreidingskaart. Kits met zowel de SSD uitbreidingskaart als een compatibele behuizing zijn online verkrijgbaar;
- Een voedingskabel voor je Raspberry Pi;
- Een micro SD-kaart van minstens 16 GB (hoewel 8 GB technisch gezien zou kunnen volstaan, is het prijsverschil tussen kaarten van 8 en 16 GB vaak verwaarloosbaar);
- Een RJ45 Ethernetkabel voor netwerkaansluiting.


![node material](assets/notext/2.webp)


## Hoe zet je de Raspberry Pi 4 in elkaar?

De assemblage van je node zal variëren afhankelijk van de gekozen hardware, vooral het type behuizing. Het algemene overzicht van de te volgen stappen blijft echter over het algemeen gelijk in de assemblage.

Installeer eerst je SSD op de opslaguitbreidingskaart en zorg ervoor dat je de twee vergrendelingsschroeven aan de achterkant goed vastzet.


![assembly1](assets/notext/3.webp)


Sluit vervolgens je Raspberry Pi aan op de uitbreidingskaart.


![assembly2](assets/notext/4.webp)


Bevestig ook de ventilator aan de Raspberry Pi.


![assembly3](assets/notext/5.webp)


Sluit de verschillende onderdelen aan en let er daarbij op dat je de juiste pinnen gebruikt, waarbij je de handleiding van je behuizing raadpleegt. Fabrikanten van behuizingen bieden vaak videotutorials om je te helpen bij de montage. In mijn geval heb ik een extra uitbreidingskaart met een aan/uit-knop. Dit is niet essentieel voor het maken van een Bitcoin node. Ik gebruik hem vooral om een aan/uit-knop te hebben.


Als je, net als ik, een uitbreidingskaart hebt met een aan/uit-knop, vergeet dan niet de kleine "Auto Power On"-jumper te installeren. Hierdoor zal je node automatisch opstarten zodra deze wordt ingeschakeld. Deze functie is vooral handig in het geval van een stroomstoring, omdat je node dan vanzelf opnieuw opstart, zonder handmatige tussenkomst van jouw kant.


![assembly4](assets/notext/6.webp)


Voordat je alle hardware in de behuizing plaatst, is het belangrijk om de goede werking van je Raspberry Pi, de opslaguitbreidingskaart en de ventilator te controleren door ze aan te zetten.


![assembly5](assets/notext/7.webp)


Installeer ten slotte je Raspberry Pi in zijn behuizing. Let op, in een latere stap moet je de micro SD-kaart in de juiste poort van de Raspberry Pi steken. Als je behuizing een opening heeft waardoor je de SD-kaart erin kunt steken zonder dat je de behuizing hoeft te openen (zoals het geval is bij de mijne op de foto), dan kun je de behuizing nu sluiten. Als je behuizing echter geen directe toegang tot de micro SD-poort heeft, moet je wachten tot je de micro SD-kaart hebt voorbereid om deze te plaatsen voordat je de assemblage afrondt.


![assembly6](assets/notext/8.webp)


## Hoe installeer ik RoninDojo v2 op een Raspberry Pi 4?


### Stap 1: De opstartbare micro SD voorbereiden

Na het assembleren van je hardware, is de volgende stap het installeren van RoninDojo. Hiervoor bereiden we een opstartbare micro SD-kaart van je computer voor, door de juiste schijfimage erop te branden.

Je hebt de _**Raspberry Pi Imager**_ software nodig, ontworpen om het downloaden, configureren en schrijven van besturingssystemen op een micro SD-kaart voor gebruik met een Raspberry Pi te vergemakkelijken. Begin met het installeren van deze software op je pc:


- Voor Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Voor Windows: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Voor Mac: https://downloads.raspberrypi.org/imager/imager_latest.dmg


Zodra de software geïnstalleerd is, open je deze en steek je de micro SD-kaart in je pc. Selecteer op de Raspberry Pi Imager Interface `CHOOSE OS`:


![choose OS](assets/notext/9.webp)


Ga vervolgens naar het `Raspberry Pi OS (other)` menu:


![choose OS others](assets/notext/10.webp)


Kies het besturingssysteem genaamd `Raspberry Pi OS (Legacy, 64-bit) Lite`, dat `0,3 GB` groot is:


![choose OS Legacy Lite](assets/notext/11.webp)


Nadat je het besturingssysteem hebt geselecteerd, kom je in het hoofdmenu van Raspberry Pi Imager. Klik op `CHOOSE STORAGE`:


![choose storage](assets/notext/12.webp)


Selecteer je micro SD-kaart:


![choose micro sd](assets/notext/13.webp)


Nadat je het besturingssysteem en de micro SD-kaart hebt gekozen, klik je op `NEXT`:


![choose next](assets/notext/14.webp)


Er verschijnt een nieuw venster. Selecteer `EDIT CONFIGURATION`:


![edit settings](assets/notext/15.webp)


Ga in dit venster naar het tabblad `GENERAL` en maak de volgende instellingen (die erg belangrijk zijn voor de werking):


- Schakel de optie in en wijs `RoninDojo` toe als hostnaam;
- Schakel `Gebruikersnaam en wachtwoord instellen` in, voer `pi` in als gebruikersnaam, kies een wachtwoord en noteer deze informatie, want die is later nodig. Deze gegevens zijn tijdelijk en worden later verwijderd;
- Schakel `Wi-Fi configureren` uit;
- Schakel `Lokale instellingen instellen` in en selecteer uw tijdzone en het type toetsenbord dat overeenkomt met uw computer;


![general settings](assets/notext/16.webp)


Klik in het tabblad SERVICES op het vakje `SHS inschakelen` en selecteer `Een wachtwoord gebruiken voor verificatie`:


![services settings](assets/notext/17.webp)


Zorg er ook voor dat telemetrie is uitgeschakeld op het tabblad `OPTIONS`:


![options settings](assets/notext/18.webp)


Klik op `Opslaan`:


![settings save](assets/notext/19.webp)

Bevestig door op `YES` te klikken om te beginnen met het maken van de opstartbare micro SD-kaart:

![settings yes](assets/notext/20.webp)


Er verschijnt een bericht dat alle gegevens op de micro SD-kaart worden gewist. Bevestig door op `YES` te klikken om het proces te starten:


![overwrite micro SD](assets/notext/21.webp)


Wacht tot de software klaar is met het voorbereiden van je micro SD-kaart:


![writing micro SD](assets/notext/22.webp)


Wanneer het bericht verschijnt dat het einde van het proces aangeeft, kun je de micro SD-kaart uit je computer verwijderen:


![writing micro SD completed](assets/notext/23.webp)


### Stap 2: Voltooi de montage van het knooppunt

Je kunt nu de micro SD-kaart in de juiste poort van je Raspberry Pi steken.


![micro SD](assets/notext/24.webp)


Sluit vervolgens je Raspberry Pi aan op je router met de Ethernet-kabel. Zet ten slotte je knooppunt aan door de voedingskabel aan te sluiten en op de aan/uit-knop te drukken (als je er een hebt).


### Stap 3: Een SSH-verbinding maken met het knooppunt

Eerst moet het IP Address van je node gevonden worden. Je hebt de mogelijkheid om een tool zoals _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ of _[Angry IP Scanner](https://angryip.org/)_ te gebruiken, of om de Interface van je router te controleren. Het IP Address moet de vorm `192.168.1.??` hebben. **Vervang voor alle volgende commando's `[IP]` door het werkelijke IP Address van je knooppunt**, (verwijder de haakjes).


Start een terminal.


Om een mogelijke sleutel te verwijderen die al geassocieerd is met het IP Address van je knooppunt, voer je het commando uit:

`ssh-keygen -R [IP]`.


Een foutmelding na dit commando is niet ernstig; het betekent gewoon dat de sleutel niet bestaat in je lijst met bekende hosts (wat vrij waarschijnlijk is). Bijvoorbeeld, als het IP van je node `192.168.1.40` is, dan wordt het commando: `ssh-keygen -R 192.168.1.40`.


Maak vervolgens een SSH-verbinding met je knooppunt door het commando uit te voeren:

`ssh pi@[IP]`.

Er verschijnt een bericht over de authenticiteit van de host: `De authenticiteit van host '[IP]' kan niet worden vastgesteld.` Dit geeft aan dat de authenticiteit van het apparaat waarmee je probeert te verbinden niet kan worden geverifieerd vanwege het ontbreken van een bekende publieke sleutel. Wanneer voor de eerste keer via SSH verbinding wordt gemaakt met een nieuwe host, zal deze melding altijd verschijnen. Je moet `yes` antwoorden om de publieke sleutel toe te voegen aan je lokale directory, waardoor deze waarschuwing niet meer verschijnt tijdens toekomstige SSH-verbindingen met dit knooppunt. Typ daarom `yes` en druk op `enter` om te valideren.

Vervolgens wordt u gevraagd uw wachtwoord in te voeren, het wachtwoord dat eerder als tijdelijk was ingesteld in stap 1. Valideer met `enter`. Je bent dan verbonden met je node via SSH.


Samengevat zijn dit de commando's om uit te voeren:


- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `ja`
- Voer het tijdelijke wachtwoord in en bevestig.


### Stap 4: Bijwerken en voorbereiden

Je bent nu verbonden met je knooppunt via een SSH-sessie. Op je terminal zou de opdrachtprompt moeten zijn: `pi@RoninDojo:~ $`. Werk om te beginnen de lijst met beschikbare pakketten bij en installeer updates voor bestaande pakketten met het volgende commando:

`sudo apt update && sudo apt upgrade -y`


Zodra de updates zijn voltooid, kunt u *Git* en *Dialog* installeren met het commando:

`sudo apt install git dialog -y`


Kloon vervolgens de `master` branch van de _RoninOS_ Git repository door uit te voeren:

`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`


Voer het script `customize-image.sh` uit met de opdracht:

`cd /opt/RoninOS/ && sudo ./customize-image.sh`


**Het is belangrijk om het script ononderbroken te laten draaien en geduldig te wachten op het einde van het proces**, dat ongeveer 10 minuten duurt. Wanneer het bericht `Setup is voltooid` verschijnt, kunt u verder gaan met de volgende stap.


### Stap 5: RoninOS starten

Start RoninOS met het commando:

`sudo systemctl start ronin-setup`


Geef de regels van het logbestand weer met de opdracht:

`tail -f /home/ronindojo/.logs/setup.logs`


In dit stadium **is het belangrijk om RoninOS te laten starten en te wachten tot het** klaar is met draaien. Dit duurt ongeveer 40 minuten. Wanneer `Alle RoninDojo functie-installaties voltooid!` verschijnt, kun je verder gaan met stap 6.


### Stap 6: RoninUI openen en referenties wijzigen

Om na de installatie via een browser verbinding te maken met je knooppunt, moet je ervoor zorgen dat je computer verbonden is met hetzelfde lokale netwerk als je knooppunt. Als u een VPN gebruikt op uw computer, schakel deze dan tijdelijk uit. Om toegang te krijgen tot het knooppunt Interface in uw browser, voert u in de URL-balk in:


- Direct het IP Address van je knooppunt, bijvoorbeeld `192.168.1.??`;
- Of typ `ronindojo.local`.


Eenmaal op de RoninUI homepage, zal je gevraagd worden om de setup te starten. Klik hiervoor op de `Laat ons beginnen` knop.


![lets start](assets/notext/25.webp)


In dit stadium geeft RoninUI je je `root` wachtwoord. Het is essentieel om het veilig te bewaren. Je kunt kiezen voor een fysieke back-up, op papier, of sla het op in een [wachtwoordmanager] (https://planb.network/courses/99c46148-7080-4915-a7e0-9df0e145cd47/0b3c69b2-522c-56c8-9fb8-1562bd55930f).


![root password](assets/notext/26.webp)


Nadat u het `root`-wachtwoord hebt opgeslagen, vinkt u het vakje `Ik heb een back-up gemaakt van de referenties van de rootgebruiker` aan en klikt u op `Doorgaan` om verder te gaan.


![confirm root password](assets/notext/27.webp)


De volgende stap is het aanmaken van een gebruikerswachtwoord, dat zowel gebruikt zal worden voor toegang tot het RoninUI web Interface als voor het opzetten van SSH sessies met je knooppunt. Kies een sterk wachtwoord en sla het veilig op. U moet dit wachtwoord twee keer invoeren voordat u op `Finish` klikt om het te valideren. Wat betreft de gebruikersnaam is het aan te raden om de standaardkeuze, `ronindojo`, te behouden. Als je besluit om het te veranderen, vergeet dan niet om de commando's in de volgende stappen aan te passen.


![user credentials](assets/notext/28.webp)


Wacht tot het knooppunt geïnitialiseerd is. Je krijgt dan toegang tot de RoninUI web Interface. Je bent bijna aan het einde van het proces, nog maar een paar kleine stappen!

![Ronin UI](assets/notext/29.webp)


### Stap 7: Tijdelijke referenties verwijderen

Open een nieuwe terminal op uw computer en maak een SSH-verbinding met uw knooppunt met het volgende commando:

`SSH ronindojo@[IP]`


Als bijvoorbeeld het IP Address van je knooppunt `192.168.1.40` is, dan is het juiste commando:

`SSH ronindojo@192.168.1.40`


Als je tijdens de vorige stap je gebruikersnaam hebt veranderd, door de standaard gebruikersnaam (`ronindojo`) te vervangen door een andere, zorg er dan voor dat je deze nieuwe naam gebruikt in het commando. Als je bijvoorbeeld `planb` als gebruikersnaam hebt gekozen en het IP Address is `192.168.1.40`, dan zal het commando dat je moet invoeren zijn:

`SSH planb@192.168.1.40`

U wordt gevraagd om het gebruikerswachtwoord in te voeren. Voer het in en druk op `enter` om te valideren. Je krijgt dan toegang tot de RoninCLI Interface. Gebruik de pijltjestoetsen op je toetsenbord om naar de `Exit RoninDojo` optie te gaan en druk op `enter` om deze te selecteren.

![RoninCLI](assets/notext/30.webp)


Op dit punt ben je in de terminal van je node, met een opdrachtprompt die lijkt op: `ronindojo@RoninDojo:~ $`. Om de tijdelijke gebruiker te verwijderen die is aangemaakt tijdens de configuratie van de opstartbare micro SD-kaart, voer je het volgende commando in en druk je op `enter`:

`sudo deluser --remove-home pi`


U wordt gevraagd om uw gebruikerswachtwoord te bevestigen. Voer het in en bevestig door op `enter` te drukken. Wacht tot de bewerking is voltooid en gebruik dan het `exit` commando om de terminal te verlaten.


Gefeliciteerd! Je RoninDojo v2 knooppunt is nu geconfigureerd en klaar voor gebruik. Het zal beginnen met zijn IBD (*Initial Block Download*), het downloaden en verifiëren van Bitcoin Blockchain van het Genesis blok. Deze stap omvat het ophalen van alle Bitcoin transacties die sinds 3 januari 2009 zijn gedaan en neemt enige tijd in beslag. Zodra de Blockchain volledig is gedownload, gaat de indexeerder verder met het comprimeren van de database. De duur van de IBD kan aanzienlijk variëren. Je RoninDojo node zal volledig operationeel zijn zodra dit proces is voltooid.


**Als je migreert van een oud RoninDojo v1 knooppunt** naar deze nieuwe versie met deze tutorial en je behoudt dezelfde SSD, dan zou je knooppunt automatisch de bestaande gegevens op de schijf moeten detecteren en hergebruiken, zodat je de IBD niet opnieuw hoeft uit te voeren. In dit geval hoef je alleen maar te wachten tot je node opnieuw synchroniseert met de nieuwste blokken.


### Stap 8: "veth fix"

Als je een bug tegenkomt met je RoninDojo v2 op Raspberry Pi, waar na een probleemloze installatie, je node plotseling onbereikbaar wordt via SSH maar herstelt na een eenvoudige herstart, dan moet je deze stap 8 volgen. Deze veelvoorkomende bug kan eenvoudig verholpen worden met een oplossing ontwikkeld door de gemeenschap: de "_veth fix_". Deze kleine correctie verhelpt de abrupte verbroken verbinding permanent. Dit is hoe je het toepast.


Open een nieuwe terminal op uw computer en maak een SSH-verbinding met uw knooppunt met het volgende commando:

`SSH ronindojo@[IP]`


Als bijvoorbeeld het IP Address van je knooppunt `192.168.1.40` is, dan zou het juiste commando zijn:

`SSH ronindojo@192.168.1.40`


U wordt gevraagd om het gebruikerswachtwoord in te voeren. Voer het in en druk op `enter` om te bevestigen. Je krijgt dan toegang tot de RoninCLI Interface. Gebruik de pijltjes van je toetsenbord om naar de `Exit RoninDojo` optie te gaan en druk op `enter` om deze te selecteren.


Op dit punt ben je in de terminal van je node, met een opdrachtprompt die lijkt op: `ronindojo@RoninDojo:~ $`. Om de **veth** fix toe te passen typ je het volgende commando en druk je op `enter`:

`sudo nano /etc/dhcpcd.conf`


Bevestig je wachtwoord nogmaals en druk op `enter`.


Je komt dan bij het `dhcpcd.conf` bestand. Kopieer de volgende tekst, zorg ervoor dat je het sterretje meeneemt, en voeg het toe aan de onderkant van het bestand:

`denyinterfaces veth*`


Ga hiervoor naar de onderkant van het bestand met de pijl omlaag op je toetsenbord en gebruik vervolgens de rechtermuisknop om de tekst op een onafhankelijke regel te plakken.


Druk na het toevoegen van de tekst op `ctrl X` om het afsluiten te starten, gevolgd door `ctrl Y` om het opslaan van de wijzigingen te bevestigen en druk op `enter` om af te sluiten en terug te keren naar de opdrachtprompt. Open het `dhcpcd.conf` bestand opnieuw met het juiste commando om er zeker van te zijn dat de wijziging correct is toegepast.


Om de toepassing van de fix te voltooien, herstart u uw node door uit te voeren:

`sudo nu opnieuw opstarten`


Op dit punt kun je je terminal sluiten. Geef je RoninDojo de tijd om opnieuw op te starten, waarna je opnieuw verbinding zou moeten kunnen maken via de grafische Interface van je browser. Dit proces zou de gevonden bug moeten verhelpen.


## Hoe gebruik je je RoninDojo v2 knooppunt?


### Je Wallet software aansluiten op Electrs

Het eerste gebruik van je vers geïnstalleerde en gesynchroniseerde node zal zijn om je transacties uit te zenden naar het Bitcoin netwerk. Je zult waarschijnlijk je verschillende wallets met je node willen verbinden om je transacties vertrouwelijk uit te zenden. Je kunt dit doen via Electrum Rust Server (electrs). Deze applicatie is meestal voorgeïnstalleerd op je RoninDojo knooppunt. Zo niet, dan kun je het handmatig installeren via de RoninCLI Interface in `Toepassingen > Toepassingen beheren > Electrum Server installeren`.


Om de Tor Address van je Electrum Server te verkrijgen, ga je vanuit het RoninUI web Interface naar:

`Koppelen > Electrum server > Nu koppelen`

![Pairing](assets/notext/31.webp)

![Electrs](assets/notext/32.webp)

Je moet dan de `Hostname` Address eindigend op `.onion` invoeren in je Wallet software, samen met poort `50001`. hostnaam](assets/notext/33.webp)

Ga bijvoorbeeld op Sparrow wallet gewoon naar het tabblad:

bestand > Voorkeuren > Server > Privé Electrum`


![Sparrow](assets/notext/34.webp)


### Uw Wallet software verbinden met Samourai Dojo

Als alternatief voor het gebruik van Electrs, kun je met Dojo je compatibele Software Wallet rechtstreeks op je RoninDojo knooppunt aansluiten. Portemonnees zoals Samourai Wallet en Sentinel bieden deze functionaliteit.


Om de verbinding tot stand te brengen hoef je alleen maar de QR-code van je Dojo te scannen. Om toegang te krijgen tot deze QR-code via RoninUI, navigeer je naar:

`Koppelen > Samourai Dojo > Nu koppelen`

![Samourai Dojo](assets/notext/35.webp)

Om je Samourai Wallet aan je Dojo te koppelen, scan je gewoon deze QR-code tijdens de installatie van de app:


![Samourai Wallet connection](assets/notext/36.webp)


Als je al een Samourai Wallet had voordat je je Ronin Dojo instelde, is het nodig om een back-up te maken van je Wallet, de Samourai Wallet app te verwijderen en vervolgens opnieuw te installeren, voordat je je Wallet herstelt. Na het starten van de opnieuw geïnstalleerde app, heb je de optie om verbinding te maken met een nieuwe Dojo. **Zorg ervoor dat je de back-up van je Samourai Wallet in je bestanden hebt en controleer de geldigheid van je passphrase via** `Instellingen > Problemen oplossen > passphrase`. **Het is ook belangrijk om een leesbare back-up van je herstelzin en je passphrase te hebben. Voor meer precisie in deze handeling, is het aan te raden om deze gedetailleerde tutorial te volgen:** [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).


### Uw eigen Mempool.ruimte Block explorer gebruiken

Een Block explorer zet de ruwe informatie van de Bitcoin Blockchain om in een gestructureerd en gemakkelijk leesbaar formaat. Met tools als *Mempool.space* is het mogelijk om transacties te analyseren, naar specifieke adressen te zoeken of zelfs de gemiddelde tarieven van de mempools van het netwerk in real-time te raadplegen.


Het gebruik van online block explorers brengt echter risico's met zich mee voor je privacy en houdt in dat je moet vertrouwen op de gegevens die door derden worden verstrekt. Door deze diensten te gebruiken zonder via je eigen node te gaan, kun je namelijk onbedoeld informatie over je transacties vrijgeven en moet je vertrouwen op de nauwkeurigheid van de informatie die door de site-eigenaar wordt gepresenteerd.

Om deze risico's te beperken, wordt het aanbevolen om je eigen instantie van *Mempool.space* te gebruiken via het Tor-netwerk, direct gehost op je node. Deze oplossing garandeert het behoud van je privacy en de autonomie van je gegevens.

Om dit te doen, installeer je eerst *Mempool Space Visualizer* van RoninUI. Ga op het web Interface naar de `Dashboard` tab en klik op `Manage` onder `Mempool Space`:

dashboard > Mempool Ruimte > Beheren`

![Manage mempool](assets/notext/37.webp)

Klik vervolgens op de knop `Installeer Mempool visualizer`:

![install mempool](assets/notext/38.webp)

Bevestig je gebruikerswachtwoord:

![password mempool](assets/notext/39.webp)

Wacht tot de installatie is voltooid en klik dan opnieuw op de knop `Beheer`:

![Mempool Manage](assets/notext/40.webp)

Je krijgt een `.onion` link om toegang te krijgen tot je eigen instantie van *Mempool.space* via het Tor netwerk.

![Mempool link](assets/notext/41.webp)

Ik raad je aan om deze link op te slaan in je favorieten op de Tor browser of toe te voegen aan de Tor Browser app op je smartphone voor gemakkelijke en veilige toegang vanaf elke locatie. Als je de Tor browser nog niet hebt, kun je deze hier downloaden: [https://www.torproject.org/download/](https://www.torproject.org/download/)

![Mempool Tor](assets/notext/42.webp)


### Whirlpool gebruiken om je bitcoins te mixen

Jouw RoninDojo node integreert ook _WhirlpoolCLI_, een opdrachtregel Interface die het automatiseren van Whirlpool coinjoins mogelijk maakt, en _WhirlpoolGUI_, een grafische Interface ontworpen voor interactie met _WhirlpoolCLI_.


Het uitvoeren van een CoinJoin via Whirlpool vereist dat de gebruikte toepassing actief is om remixen uit te voeren. Deze voorwaarde kan beperkend zijn voor wie hoge niveaus van anonimisering wil bereiken. Het apparaat dat de toepassing host die Whirlpool integreert, moet namelijk continu aan staan. Dit betekent dat om 24 uur per dag deel te nemen aan remixen, je computer of smartphone aan moet blijven staan met Samourai of Sparrow continu open. Een oplossing voor deze beperking is om _WhirlpoolCLI_ te gebruiken op een machine die altijd aan staat, zoals een Bitcoin node, waardoor je munten kunt remixen zonder onderbreking en zonder dat je een ander apparaat aan hoeft te houden.


Een gedetailleerde tutorial is in voorbereiding om je stap voor stap door het proces van coinjoining met Samourai Wallet en RoninDojo v2 te leiden, van A tot Z.


Voor een dieper begrip van CoinJoin en het gebruik ervan op Bitcoin, nodig ik je ook uit om dit andere artikel te raadplegen: CoinJoin begrijpen en gebruiken op Bitcoin, waar ik alles wat je moet weten over deze techniek in detail beschrijf.




### Whirlpool Stat Tool (WST) gebruiken


Na het uitvoeren van coinjoins met Whirlpool is het handig om het bereikte privacyniveau voor je gemengde UTXO's nauwkeurig te evalueren. Hiervoor kun je de Python tool *Whirlpool Stat Tool* gebruiken. Met deze tool kun je zowel de prospectieve als retrospectieve scores van je UTXO's meten, terwijl je hun verspreidingsgraad in de pool analyseert.


Om de berekeningsmechanismen van deze anonsets beter te begrijpen, raad ik je aan het artikel te lezen: REMIX - Whirlpool, waarin de werking van deze indices gedetailleerd wordt beschreven.


https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



Om toegang te krijgen tot de WST tool, ga je naar RoninCLI. Open hiervoor een terminal op je pc en maak een SSH-verbinding met je knooppunt met het volgende commando:

`SSH ronindojo@[IP]`


Als bijvoorbeeld het IP Address van je knooppunt `192.168.1.40` is, dan zou het juiste commando zijn:

`SSH ronindojo@192.168.1.40`


Als je tijdens stap 6 je gebruikersnaam veranderde en de standaard gebruikersnaam (`ronindojo`) verving door een andere, zorg er dan voor dat je deze nieuwe naam gebruikt in het commando. Bijvoorbeeld, als je `planb` als gebruikersnaam hebt gekozen en het IP van Address is `192.168.1.40`, dan zou het commando zijn:

`SSH planb@192.168.1.40`


U wordt gevraagd om het gebruikerswachtwoord in te voeren. Voer het in en druk op `enter` om te valideren. Je krijgt dan toegang tot de RoninCLI Interface. Gebruik de pijltjestoetsen op je toetsenbord om naar het `Samourai Toolkit` menu te gaan en druk op `enter` om het te selecteren:


![Samourai Toolkit](assets/notext/43.webp)


Selecteer vervolgens `Whirlpool Stat Tool`:


![WST](assets/notext/44.webp)


Na het initialiseren van WST zal het programma doorgaan met de automatische installatie. Wacht tijdens deze stap. De gebruiksinstructies zullen doorlopen. Zodra de installatie voltooid is, druk je op een willekeurige toets om de WST-terminal te openen:


![WST commands](assets/notext/45.webp)


De volgende opdrachtprompt wordt weergegeven:

`wst#/tmp>`


Als je deze Interface wilt verlaten en wilt terugkeren naar het RoninCLI menu, geef dan gewoon enter:

kappen


Eerst is het nodig om de proxy te configureren om Tor te gebruiken, om privacy te garanderen bij het extraheren van gegevens uit OXT. Voer het commando in:

`socks5 127.0.0.1:9050`


Download vervolgens de poolgegevens die je transactie bevatten:

`download 0001`

Vervang `0001` door de denominatiecode van de pool waarin je geïnteresseerd bent. De denominatiecodes zijn als volgt op WST:


- Pool 0,5 bitcoins: `05`
- Pool 0.05 bitcoins: `005`
- Pool 0.01 bitcoins: `001`
- Pool 0.001 bitcoins: `0001`


Na het downloaden laad je de gegevens door `0001` te vervangen door de code van je pool in deze opdracht: `load 0001`


![WST loading](assets/notext/46.webp)


Wacht tot het laden is voltooid, wat een paar minuten kan duren. Zodra de gegevens geladen zijn, kunt u de anonset-scores van uw Coin opvragen door het commando `score` uit te voeren, gevolgd door uw txid (zonder de haakjes):

`score [txid]`


![WST score](assets/notext/47.webp)


WST toont dan de retrospectieve score (_Backward-looking metrics_), gevolgd door de prospectieve score (_Forward-looking metrics_). Naast de anonset-scores geeft WST ook de verspreidingsgraad van je transactie binnen de pool aan, ten opzichte van de anonset.


**Het is belangrijk op te merken dat de prospectieve score van uw Coin berekend moet worden op basis van de txid van uw eerste mix, en niet op basis van uw meest recente mix. Omgekeerd wordt de retrospectieve score van een UTXO berekend op basis van de txid van de laatste cyclus.**


### De Boltzmann-berekenmachine gebruiken

De Boltzmann calculator is een hulpmiddel voor het analyseren van een Bitcoin transactie en biedt de mogelijkheid om het niveau van entropie te meten naast andere geavanceerde meetgegevens. Deze gegevens geven een gekwantificeerde beoordeling van de privacy van een transactie en helpen bij het identificeren van mogelijke fouten. Deze tool is al geïntegreerd in je RoninDojo knooppunt, waardoor het eenvoudig te gebruiken is.


Voordat de procedure voor het gebruik van de Boltzmann Calculator wordt beschreven, is het belangrijk om de betekenis van deze indicatoren, hun berekeningsmethode en hun nut te begrijpen. Hoewel deze indicatoren van toepassing zijn op elke Bitcoin transactie, zijn ze vooral nuttig om de kwaliteit van een CoinJoin transactie te beoordelen.


**De eerste indicator** die de software berekent is het totale aantal mogelijke combinaties, aangegeven onder `nb combinaties` in de tool. Op basis van de waarden van de betrokken UTXO's kwantificeert deze indicator het aantal manieren waarop inputs kunnen worden geassocieerd met outputs. Met andere woorden, hij bepaalt het aantal plausibele interpretaties dat een transactie generate kan hebben. Bijvoorbeeld, een CoinJoin gestructureerd volgens het Whirlpool 5x5 model laat `1496` mogelijke combinaties zien:

![combinations](assets/notext/50.webp)

Krediet: KYCP


**De tweede indicator** die wordt berekend is de entropie van een transactie, aangeduid met `Entropie`. Als een transactie een groot aantal mogelijke combinaties heeft, is het vaak relevanter om naar de entropie te verwijzen. Dit wordt gedefinieerd als de binaire logaritme van het aantal mogelijke combinaties. Hier is de gebruikte formule:


- $E$: de entropie van de transactie;
- $C$: het aantal mogelijke combinaties voor de transactie.

$$E = \log_2(C)$$


In de wiskunde komt de binaire logaritme (logaritme van basis 2) overeen met de inverse bewerking van het verheffen van 2 tot een macht. Met andere woorden, de binaire logaritme van $x$ is de exponent waartoe 2 verheven moet worden om $x$ te verkrijgen. Daarom wordt deze indicator uitgedrukt in bits. Laten we het voorbeeld nemen van het berekenen van de entropie voor een CoinJoin transactie gestructureerd volgens het Whirlpool 5x5 model, dat, zoals eerder vermeld, een aantal mogelijke combinaties van `1496` biedt:

$$ C = 1496 $$

$$ E = \log_2(1496) $$

$$ E approx 10.5469 \text{ bits}$$


Deze CoinJoin transactie vertoont dus een entropie van 10,5469 bits, wat als zeer bevredigend wordt beschouwd. Hoe hoger deze waarde, hoe meer verschillende interpretaties de transactie toelaat, waardoor het niveau van privacy toeneemt.


Laten we nog een voorbeeld nemen met een meer conventionele transactie, met één invoer en twee uitgangen: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)

In het geval van deze transactie is de enige mogelijke interpretatie: `(inp 0) > (Outp 0 ; Outp 1)`. Bijgevolg wordt de entropie vastgesteld op `0`:

$$ C = 1 $$

$$ E = \log_2(1) $$

$$ E approx 0 \text{ bits}$$

**De derde indicator** van de Boltzmann Calculator heet `Wallet Efficiëntie`. Deze indicator beoordeelt de efficiëntie van de transactie door deze te vergelijken met de optimale transactie die denkbaar is in een identieke opstelling. Dit leidt ons naar het concept van maximale entropie, dat overeenkomt met de hoogste entropie die een specifieke transactiestructuur theoretisch kan bereiken. Dus voor een Whirlpool 5x5 CoinJoin structuur is de maximale entropie vastgesteld op `10,5469`. De efficiëntie van de transactie wordt dan berekend door deze maximale entropie te vergelijken met de werkelijke entropie van de geanalyseerde transactie. De gebruikte formule is als volgt:


- $ER$: de werkelijke entropie van de transactie, uitgedrukt in bits;
- $EM$: de maximaal mogelijke entropie voor een gegeven transactiestructuur, ook in bits;
- $Ef$: de efficiëntie van de transactie, in bits.

$$Ef = ER - EM$$ $$Ef = 10,5469 - 10,5469$$

$$Ef = 0 \text{ bits}$$


Deze indicator wordt ook uitgedrukt als percentage, de formule is dan:


- $CR$: het aantal mogelijke combinaties;
- $CM$: het maximum aantal mogelijke combinaties met dezelfde structuur;
- $Ef$: de efficiëntie uitgedrukt als een percentage.

$$Ef = \frac{CR}{CM}$$

$$Ef = \frac{1496}{1496}$$

$$Ef = 100%$$


Een efficiëntie van `100%` geeft dus aan dat de transactie haar potentieel voor privacy maximaliseert op basis van haar structuur.


**De vierde indicator**, de entropiedichtheid, of `Entropy Density`, biedt een perspectief op de entropie ten opzichte van elke invoer of uitvoer van de transactie. Deze indicator is handig voor het evalueren en vergelijken van de efficiëntie van transacties van verschillende grootte. Om de indicator te berekenen, deel je simpelweg de totale entropie van de transactie door het totaal aantal inputs en outputs. Als we het voorbeeld nemen van een Whirlpool 5x5 CoinJoin:


- $ED$: de entropiedichtheid uitgedrukt in bits;
- $E$: de entropie van de transactie uitgedrukt in bits;
- $T$: het totale aantal in- en uitgangen in de transactie.

$$T = 5 + 5 = 10$$

$$ED = \frac{E}{T}$$

$$ED = \frac{10.5469}{10}$$

$$ED = 1,054 \text{ bits}$$

**Het vijfde stukje informatie** dat de Boltzmann Calculator levert is de tabel met overeenkomende waarschijnlijkheden tussen inputs en outputs. Deze tabel geeft, door middel van de `Boltzmann score`, de waarschijnlijkheid aan dat een specifieke ingang verbonden is met een bepaalde uitgang. Als we het voorbeeld nemen van een Whirlpool CoinJoin, dan geeft de waarschijnlijkheidstabel de kans op een koppeling tussen elke ingang en uitgang aan, wat een kwantitatieve maat is voor de dubbelzinnigheid of voorspelbaarheid van de associaties in de transactie:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Hier is het duidelijk dat elke input een gelijke kans heeft om geassocieerd te worden met elke output, wat de ambiguïteit en privacy van de transactie versterkt. In het geval van een eenvoudige transactie met een enkele invoer en twee uitgangen is de situatie echter anders:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Hier zien we dat de kans dat elke output afkomstig is van input 0 100% is. Een lagere waarschijnlijkheid leidt dus tot meer privacy, doordat de directe links tussen inputs en outputs verwateren.


**Het zesde stukje informatie** dat wordt gegeven is het aantal deterministische verbanden, aangevuld met de verhouding van deze verbanden. Deze indicator laat zien hoeveel verbindingen tussen de inputs en outputs in de geanalyseerde transactie onbetwistbaar zijn, met een waarschijnlijkheid van 100%. De ratio biedt op zijn beurt een perspectief op het gewicht van deze deterministische koppelingen binnen het totaal aan koppelingen van de transactie.


Een transactie van het Whirlpool type bijvoorbeeld heeft geen deterministische koppelingen en heeft daarom een indicator en ratio van 0%. Aan de andere kant, in onze tweede onderzochte transactie (met één input en twee outputs), is de indicator ingesteld op 2 en de ratio bereikt 100%. Een nulindicator duidt dus op een uitstekende privacy dankzij de afwezigheid van directe en onbetwistbare links tussen inputs en outputs.


**Hoe krijg ik toegang tot de Boltzmann Calculator op RoninDojo?**

Om toegang te krijgen tot het gereedschap *Boltzmann Calculator* ga je naar RoninCLI. Open hiervoor een terminal op je computer en maak een SSH-verbinding met je knooppunt met het volgende commando: `SSH ronindojo@[IP]`


Als bijvoorbeeld het IP-adres van je knooppunt Address `192.168.1.40` is, dan zou het juiste commando zijn:

`SSH ronindojo@192.168.1.40`


Als u tijdens stap 6 uw gebruikersnaam veranderde en de standaard gebruikersnaam (`ronindojo`) verving door een andere, zorg er dan voor dat u deze nieuwe naam gebruikt in het commando. Bijvoorbeeld, als je `planb` als gebruikersnaam hebt gekozen en het IP van Address is `192.168.1.40`, dan zou het commando zijn:

`SSH planb@192.168.1.40`


U wordt gevraagd om het gebruikerswachtwoord in te voeren. Voer het in en druk op `enter` om te valideren. Je krijgt dan toegang tot de RoninCLI Interface. Gebruik de pijltjes op je toetsenbord om naar het `Samourai Toolkit` menu te gaan en druk op `enter` om het te selecteren:


![Samourai Toolkit](assets/notext/43.webp)


Selecteer vervolgens `Boltzmann Calculator`:


![boltzmann](assets/notext/49.webp)


Je komt dan op de startpagina van de software:


![boltzmann home](assets/notext/51.webp)


Voer de txid in van de transactie die je wilt bestuderen en druk op de `enter` toets:


![boltzmann txid](assets/notext/52.webp)


De calculator geeft je vervolgens alle indicatoren die we eerder hebben besproken:


![boltzmann result](assets/notext/53.webp)


### Andere functies van RoninDojo v2

Je RoninDojo knooppunt integreert verschillende andere functies. In het bijzonder heb je de mogelijkheid om specifieke informatie te scannen om er rekening mee te houden. Bijvoorbeeld, soms geeft je Samourai Wallet, verbonden met RoninDojo, niet de bitcoins weer die je werkelijk bezit. Als het saldo 0 aangeeft, terwijl je zeker weet dat je bitcoins hebt in deze Wallet, kunnen verschillende redenen deze situatie verklaren, zoals een fout in de afleidingspaden. Maar een van de oorzaken kan ook zijn dat je node je adressen niet goed controleert. Om dit probleem op te lossen, kun je ervoor zorgen dat je node inderdaad je `xpub` volgt met behulp van de _xpub tool_. Om toegang te krijgen tot deze tool via RoninUI volg je het pad:

`Onderhoud > XPUB Gereedschap`


Voer de `xpub` in die het probleem veroorzaakt en klik op de knop `Check` om deze informatie te controleren:

![xpub tool](assets/notext/54.webp)

Controleer of alle transacties correct zijn vermeld. Het is ook belangrijk om te controleren of het gebruikte afleidingstype overeenkomt met dat van uw Wallet. Als dit niet het geval is, klik dan op `Retype` en kies uit `BIP44`, `BIP49`, of `BIP84` afhankelijk van uw behoeften.

Naast deze tool zit het tabblad `Onderhoud` van RoninUI vol met andere handige functies:


- **Transactietool**: Hiermee kunnen de details van een bepaalde transactie worden bekeken;
- **Address-tool**: Hiermee kun je de tracking van een bepaalde Address door je Dojo bevestigen;
- **Blokken opnieuw scannen**: Forceert je knooppunt om een nieuwe scan uit te voeren van een opgegeven blokbereik.


De `Push Tx` tab is een andere interessante functie van RoninUI, die het mogelijk maakt om een ondertekende transactie uit te zenden op het Bitcoin netwerk. De transactie moet in hexadecimale vorm worden ingevoerd.


Wat betreft de andere tabbladen die beschikbaar zijn op je RoninUI dashboard:


- `Apps`: Host de Whirlpool toepassing, en zal in de toekomst zeker gebruikt worden om nieuwe toepassingen te integreren;
- `Logs`: Biedt real-time toegang tot de gebeurtenislogboeken van je software;
- `Systeeminfo`: Geeft algemene informatie over je node, zoals CPU-temperatuur, opslagruimtegebruik of RAM-gegevens. Je vindt hier ook de opties `Reboot` en `Uitschakelen` om je node opnieuw op te starten of uit te schakelen;
- instellingen: Hiermee kunt u uw gebruikerswachtwoord wijzigen.


Daar heb je het! Bedankt dat je deze tutorial tot het einde hebt gevolgd. Als je het leuk vond, moedig ik je aan om het te delen op sociale media. Bovendien, als je de mogelijkheid hebt, overweeg dan om de ontwikkelaars die deze gratis en open-source software beschikbaar maken voor onze gemeenschap te steunen met een donatie: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). Om je kennis van RoninDojo te verdiepen en meer bronnen te ontdekken, raad ik je ten zeerste aan om de onderstaande links naar externe bronnen te raadplegen.


**Externe bronnen:**


- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)

