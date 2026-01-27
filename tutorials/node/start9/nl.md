---
name: Start9

description: Handleiding voor het opzetten van een Start9 privéserver

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Hier is een videotutorial van Southern Bitcoiner, een videogids die laat zien hoe je een Start9 / StartOS persoonlijke server instelt en gebruikt, en hoe je een bitcoin node draait.*


## 1️⃣ Introductie


### Wat is Start9 precies?


Start9 is een bedrijf opgericht in 2020, vooral bekend voor het ontwikkelen van [**StartOS**,](https://github.com/Start9Labs/start-os) een Linux-gebaseerd besturingssysteem ontworpen voor persoonlijke servers. Het stelt gebruikers in staat om eenvoudig zelf een breed scala aan softwareservices te hosten, zoals Bitcoin en Lightning nodes, messaging apps of wachtwoordmanagers, terwijl ze de volledige controle over hun gegevens behouden en niet afhankelijk zijn van gecentraliseerde technologieplatforms. StartOS heeft een gebruiksvriendelijke, browsergebaseerde interface, een samengestelde Marketplace voor het installeren van diensten en ingebouwde privacytools zoals Tor-integratie en systeembrede HTTPS-encryptie. Start9 levert ook hardware-apparaten die vooraf zijn geladen met het OS, maar de software kan ook worden geïnstalleerd op compatibele hardware of virtuele machines (VM's).


### Welke opties zijn beschikbaar?


Start9 biedt zowel voorgebouwde als doe-het-zelf implementatieopties. De [**Server One**](https://store.start9.com/collections/servers/products/server-one) en [**Server Pure** ](https://store.start9.com/collections/servers/products/server-pure) zijn officiële hardwareapparaten met krachtige componenten: de Server One maakt gebruik van een **AMD Ryzen 7 5825U** processor met configureerbare RAM (16GB-64GB) en opslag (2TB-4TB NVMe SSD), terwijl de Server Pure is uitgerust met een **Intel i7-10710U**, die ook configureerbare RAM en opslagopties biedt. Beide zijn inclusief **levenslange technische ondersteuning** bij aankoop direct bij Start9. Voor gebruikers die de voorkeur geven aan flexibiliteit, kan StartOS gratis worden geïnstalleerd op een breed scala aan bestaande hardware, waaronder laptops, desktops, mini-pc's en single-board computers, of binnen VM's.


![image](assets/en/01.webp)


### Wat zijn de verschillen met Umbrel?


StartOS en Umbrel vereenvoudigen beide de installatie van self-hosted services, maar verschillen in architectuur en functies. Umbrel werkt als een applicatielaag op Debian/Ubuntu-systemen of VM's, terwijl Start9 een specifiek besturingssysteem is dat een directe hardware- of VM-installatie vereist. Umbrel heeft een gepolijste, op macOS geïnspireerde interface, terwijl Start9 de voorkeur geeft aan een functioneel, minimaal ontwerp. Umbrel biedt een grotere [selectie van applicaties](https://apps.umbrel.com/), terwijl de [Start9 Marketplace](https://marketplace.start9.com/) dit compenseert met geavanceerde technische mogelijkheden. Start9 vereenvoudigt de toegang tot geavanceerde instellingen via gevalideerde UI-formulieren, waardoor er minder behoefte is aan commandoregelinteractie. Het blinkt ook uit in back-upbeheer met één-klik versleutelde systeemback-ups, een functie die Umbrel van nature mist. StartOS biedt ingebouwde bewakingstools en dwingt HTTPS-encryptie af voor lokale netwerktoegang, waardoor de beveiliging wordt verbeterd. Umbrel gebruikt lokaal onversleutelde HTTP, hoewel beide platformen veilige toegang op afstand via Tor ondersteunen. Umbrel is geschikt voor gebruikers die prioriteit geven aan een rijk app ecosysteem en een gepolijste UI. Start9 is een sterke keuze voor diegenen die waarde hechten aan beveiliging, configureerbaarheid, back-up betrouwbaarheid en geavanceerd servicebeheer zonder commandoregel expertise. Ga naar deze cursus voor meer informatie over Umbrel en de verschillen met Start9:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ doe-het-zelf-vereisten: Minimale en aanbevolen specificaties


Voor basisgebruik met minimale services zijn de **minimale specificaties**: **1 vCPU core (2.0GHz+ boost), 4GB RAM, 64GB opslag** en een Ethernetpoort. Dat gezegd hebbende, zou ik aanraden om veel verder te gaan, vooral als je een Bitcoin Node draait. Persoonlijk begon ik met 1TB en kwam al snel ruimte tekort. Je kunt beter streven naar **minimaal 2TB opslag**, samen met een **quad-core CPU (2.5GHz+)** en **8GB+ RAM**. Dit maakt een enorm verschil in prestaties en levensduur. Als je diep wilt duiken, is hier een actuele community thread over [Hardware die StartOS kan draaien](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ De firmware downloaden en flashen


Om de installatie te beginnen, gebruikt u een aparte computer om de [Start9 website](https://start9.com/) te bezoeken en navigeert u naar de documentatiesectie door op `DOCS` te klikken. Van daaruit gaat u naar de `Flashing Guides` om de juiste versie van StartOS te vinden. Er zijn twee opties beschikbaar:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Deze tutorial behandelt de `x86/ARM` optie.


De nieuwste OS-versie kan worden gedownload van de [Github release page](https://github.com/Start9Labs/start-os/releases/latest). [Pre-release](https://github.com/Start9Labs/start-os/releases) versies zijn ook beschikbaar voor gebruikers die nieuwe functies willen testen. Download onderaan de pagina, onder `Assets`, de `x86_64` of `x86_64-nonfree.iso`.  Het `x86_64-nonfree.iso` image bevat niet-vrije (closed-source) software die nodig is voor de Server One en de meeste doe-het-zelf hardware, met name voor ondersteuning van grafische en netwerkapparaten.


De integriteit van het bestand controleren door zijn SHA256 hash te vergelijken met die op GitHub wordt aangeraden. Voor Linux kan het commando `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso` gebruikt worden, andere besturingssystemen worden in de documentatie behandeld.


Na het downloaden en verifiëren van het StartOS image, moet het geflasht worden op een USB drive. `BalenaEtcher` is aanbevolen software voor deze taak. Het is een gratis, open-source hulpprogramma voor het schrijven van OS-imagebestanden naar USB-drives en SD-kaarten, beschikbaar voor Windows, macOS en Linux. Download de juiste versie van de officiële [Balena Etcher website](https://www.balena.io/etcher/) en voer het installatieprogramma uit. Sluit de USB-drive of SD-kaart aan, open Balena Etcher en klik op `Flash from file` om de gedownloade OS-image te selecteren. Etcher zal automatisch aangesloten drives detecteren; selecteer de juiste target als er meerdere aanwezig zijn. Klik op `Flash!` om te beginnen met het schrijven van de image. Etcher valideert automatisch het schrijfproces na voltooiing. Eenmaal klaar kunt u de schijf veilig verwijderen en gebruiken om het apparaat op te starten.


![image](assets/en/19.webp)


## 4️⃣ Eerste installatie


Raadpleeg voor de eerste installatie de Start9 [documentatie](https://docs.start9.com/0.3.5.x/) pagina onder `USER MANUAL` gevolgd door `Getting Started - Initial Setup`.  Deze officiële handleiding moet worden geraadpleegd voor de meest recente informatie.


Er worden twee opties gepresenteerd:



- Fris beginnen
- Herstelopties


Voor een nieuwe serverinstallatie selecteert u `Start Fresh`. Sluit de server eerst aan op voeding en een Ethernet-kabel. Zorg ervoor dat de computer die wordt gebruikt voor de installatie zich in hetzelfde lokale netwerk bevindt. Haal het nieuw geflashte USB-station uit de computer en plaats het in het basisstation.


Je kunt de server op afstand bedienen vanaf elke computer in hetzelfde netwerk. Open een webbrowser en navigeer naar `http://start.local`.


**Noot**: Als er verbindingsproblemen optreden met dit adres, komt dit vaak doordat thuisnetwerken de `.local` domeinnamen niet kunnen omzetten. Het probleem kan worden opgelost door de server rechtstreeks via het IP-adres te benaderen. Het IP-adres kan worden gevonden door in te loggen op de beheerinterface van de router (meestal op `192.168.1.1` of een vergelijkbaar adres) en het apparaat te vinden in de lijst met DHCP-clients of netwerkkaarten. Voer vervolgens het volledige IP-adres (bijv. `http://192.168.1.105`) in de browser in. Dit omzeilt DNS-resolutie. Als er problemen blijven bestaan, raadpleeg dan de pagina [Algemene problemen](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) of [neem contact op met hun ondersteuning](https://start9.com/contact/)


Het StartOS installatiescherm zou moeten verschijnen. Klik op `Start Fresh` om te beginnen met het instellen van de nieuwe server.


![image](assets/en/03.webp)


De volgende stap is het selecteren van de opslagschijf waar de StartOS-gegevens zullen worden opgeslagen.


![image](assets/en/04.webp)


Stel een sterk `wachtwoord` in voor de server. Leg het vast zoals geadviseerd door Start9 en klik dan op `FINISH`.


![image](assets/en/05.webp)


Een scherm zal laten zien dat StartOS bezig is met het initialiseren en instellen van de server. De volgende stap is het `Downloaden van adresinfo` aangezien het `start.local` adres alleen voor installatiedoeleinden is en daarna niet meer zal werken.


![image](assets/en/06.webp)


Het configuratiebestand bevat twee kritieke toegangsadressen: één voor het `lokale netwerk (LAN)` en één voor beveiligde toegang via `Tor`. Beide adressen moeten worden opgeslagen in een veilige wachtwoordmanager. De volgende stap is `Trust your Root CA`. Open een nieuw browserscherm en volg de instructies om de Root CA te vertrouwen en in te loggen. Het Root CA certificaat kan ook gedownload worden door te klikken op `Download certificaat` in het gedownloade bestand.


## 5️⃣ Uw root-CA vertrouwen


Na het downloaden van het certificaat moet de `Root CA` van de server worden vertrouwd door het besturingssysteem. Klik op `View Instructions` en vind de richtlijnen voor het specifieke besturingssysteem.


![image](assets/en/07.webp)


Voor een Linux-systeem worden de volgende commando's gebruikt. Open eerst een Terminal en installeer de benodigde pakketten:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Navigeer naar de map waar het certificaat is gedownload, meestal `~/Downloads` . Voer deze commando's uit om het certificaat toe te voegen aan de vertrouwenswinkel van het OS. Ga naar de downloads map met `cd ~/Downloads`. Maak de benodigde map aan met `sudo mkdir -p /usr/share/ca-certificates/start9`. Kopieer het certificaatbestand, waarbij u `uw-filename.crt` vervangt door de werkelijke bestandsnaam, met `sudo cp "uw-filename.crt" /usr/share/ca-certificates/start9/`. Registreer het certificaat permanent door het pad ervan toe te voegen aan de systeemconfiguratie met `sudo bash -c "echo 'start9/uw-filename.crt' >> /etc/ca-certificates.conf"`. Herbouw tenslotte de trust store met `sudo update-ca-certificates`. Het is cruciaal om de werkelijke bestandsnaam van het certificaat te gebruiken en alle paden te verifiëren voordat deze commando's worden uitgevoerd. Dit proces zorgt voor permanent vertrouwen voor de HTTPS-verbindingen van de Start9-server.


Een succesvolle installatie wordt aangegeven met de melding `1 toegevoegd`. De meeste applicaties kunnen dan veilig verbinding maken via `https`. Bij gebruik van Firefox is een extra [laatste stap](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff) nodig. Voor Chrome of Brave is een andere [laatste stap](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) nodig om de browser te configureren om de root-CA te respecteren. Test de verbinding door de pagina te vernieuwen. Als het probleem zich blijft voordoen, sluit u de browser af en opent u deze opnieuw voordat u de pagina opnieuw bezoekt.


![image](assets/en/08.webp)


## 6️⃣ Aan de slag met StartOS


Het zou nu mogelijk moeten zijn om in te loggen via een beveiligde HTTPS-verbinding. Voer het `wachtwoord` in om toegang te krijgen tot het `welkomstscherm`.


![image](assets/en/09.webp)


Dit scherm biedt handige snelkoppelingen om aan de slag te gaan. De linker zijbalk bevat de hoofdmenu-items voor navigatie.


## 7️⃣ Systeem


Het tabblad Systems in StartOS biedt toegang tot de belangrijkste systeemfuncties voor het beheren van de persoonlijke server. Het biedt tools voor systeemonderhoud, beveiliging, diagnostiek en configuratie zonder dat commandoregelkennis nodig is.


De `Backups` sectie maakt het mogelijk om volledige systeembackups te maken, inclusief services, configuraties en gegevens, die later hersteld kunnen worden. Dit is essentieel voor disaster recovery of het migreren naar nieuwe hardware. Back-ups kunnen worden opgeslagen op externe schijven en worden versleuteld met het hoofdwachtwoord.


Het `Beheer` gedeelte in het tabblad Systemen biedt controle over de belangrijkste systeemfuncties. Gebruikers kunnen handmatig controleren op StartOS-updates en deze toepassen, zodat ze controle houden over het updateproces van het systeem. Het is mogelijk om aangepaste diensten of diensten van derden die niet beschikbaar zijn op de officiële markt, te sideloaden. Als de server niet is verbonden via Ethernet, kunnen de Wi-Fi-instellingen worden geconfigureerd vanuit deze sectie. Geavanceerde gebruikers kunnen SSH-toegang inschakelen voor systeembeheer op terminalniveau.


![image](assets/en/10.webp)


De `Insights` sectie biedt real-time monitoring van de prestaties en gezondheid van de server en toont CPU, RAM en schijfgebruik in grafieken. Het toont ook de systeemtemperatuur, wat handig is voor apparaten zoals de Raspberry Pi die geen actieve koeling hebben. Uptime en belastingsgemiddelden helpen bij het beoordelen van de stabiliteit van het systeem en er zijn live logboeken beschikbaar voor het oplossen van service- of systeemproblemen.


De `Support` sectie biedt toegang tot ingebouwde FAQ's, officiële documentatie en community support kanalen. Debug logs kunnen gedownload worden van deze sectie om te delen met Start9 support voor een snellere oplossing van problemen.


![image](assets/en/11.webp)


## 8️⃣ Marktplaats


De `Marktplaats` wordt gebruikt om diensten op de persoonlijke server te ontdekken, installeren en beheren. Het biedt toegang tot software zoals Bitcoin Core, BTCPay Server en electrs. StartOS ondersteunt meerdere marktplaatsen, waaronder de officiële Start9 Registry en community-gerunde registers. Deze kunnen worden toegevoegd door te klikken op `CHANGE` en over te schakelen naar de `Community Registry`, die toegang biedt tot een breder scala aan diensten.


![image](assets/en/12.webp)


## 9️⃣ Een Bitcoin full node installeren


Het installeren van een Bitcoin full node op StartOS biedt volledige soevereiniteit over de Bitcoin ervaring. Het maakt de validatie van transacties mogelijk en verbetert de privacy en veiligheid door niet meer afhankelijk te zijn van externe diensten die activiteiten kunnen loggen. Er is volledige controle over transacties, zodat ze direct naar het netwerk kunnen worden uitgezonden. De standaardoptie is `Bitcoin Core`, die integreert met StartOS en verbinding mogelijk maakt met wallets zoals Specter, Sparrow of Electrum voor een self-custody setup. Een alternatief, `Bitcoin Knots`, is ook beschikbaar via het Gemeenschapsregister.


Navigeer naar de Marketplace om Bitcoin Core te installeren. Zoek en installeer de Bitcoin Core service in het standaard register. Na de installatie verschijnt een `Needs Config` prompt, die vereist dat instellingen worden voltooid voordat de service kan draaien. Dit gebeurt meestal na updates of nieuwe installaties en vraagt om een controle van de `RPC instellingen`. Ga verder met de standaardconfiguratie en klik op `Opslaan`.


![image](assets/en/13.webp)


Eenmaal volledig gesynchroniseerd, kan je node dienen als een private backend voor wallets zoals Sparrow, wat verbeterde privacy en transactie validatie biedt. Voor gebruikers die grote hoeveelheden opslaan, is het echter belangrijk om de veiligheidsrisico's van deze directe verbinding te begrijpen. Wanneer een wallet direct verbinding maakt met Bitcoin Core, kan het gevoelige gegevens blootleggen, aangezien Bitcoin Core publieke sleutels (xpubs) en wallet balansen onversleuteld opslaat op de host machine. Een gecompromitteerd systeem kan een aanvaller in staat stellen je holdings te ontdekken en je als doelwit te nemen.


Om dit risico te beperken en een robuuster beveiligingsmodel te bereiken, kun je een Private Electrum Server opzetten. Deze server fungeert als tussenpersoon, indexeert de blockchain zonder wallet-specifieke informatie op te slaan. Door je wallet te verbinden met je eigen Electrum server in plaats van direct met Bitcoin Core, voorkom je dat de wallet toegang heeft tot de gevoelige gegevens van de node.


![image](assets/en/14.webp)


## elektrs instellen


electrs` (Electrum Rust Server) is een snelle, efficiënte indexer die verbinding maakt met uw Bitcoin Core node en Electrum-compatibele wallets in staat stelt de transactiegeschiedenis en saldi in realtime op te vragen. Door electrs op StartOS te draaien, elimineer je de afhankelijkheid van Electrum servers van derden en verbeter je de privacy en veiligheid aanzienlijk - je wallet queries gaan rechtstreeks naar je zelf gehoste node.


Om het in te stellen, installeer je eerst de electrs service van de StartOS Marketplace. Het systeem vereist dat Bitcoin Core volledig gesynchroniseerd is voordat je verder gaat. Na de installatie bevestig je de `Needs Config` instellingen met de aanbevolen standaardwaarden en electrs begint met het indexeren van de blockchain, wat afhankelijk van je hardware tot een dag kan duren.


![image](assets/en/15.webp)


Eenmaal voltooid, kun je wallets zoals Sparrow of Specter aansluiten. Een succesvolle verbinding zorgt ervoor dat je wallet direct synchroniseert met je node, waardoor je een veilige, private en zelf gehoste Bitcoin ervaring krijgt.


## 1️⃣1️⃣ Sparrow Wallet


Om `Sparrow Wallet` te verbinden met je StartOS knooppunt met behulp van de electrs implementatie, moet je er eerst voor zorgen dat Bitcoin Core volledig gesynchroniseerd is en electrs geïnstalleerd en actief is. Open Sparrow Wallet op je apparaat en navigeer naar `Bestand` -> `Instellingen` -> `Server`. Kies dan `Private Electrum Server`. Voer in het URL-veld de `Tor hostname` en `Port` voor electrs in, die je in StartOS kunt vinden onder `Services` -> `electrs` -> `Eigenschappen` (meestal eindigend op `.onion:50001`).


![image](assets/en/16.webp)


Schakel vervolgens Tor in door `Use Proxy` aan te vinken, het proxyadres in te stellen op `127.0.0.1` en de poort op `9050`. Klik op `Test verbinding` en wacht even. Een succesvolle verbinding zal een bevestigingsbericht weergeven zoals `Connected to electrs`. Sluit na verificatie de instellingen en ga verder met het aanmaken of herstellen van uw wallet. Deze instelling zorgt ervoor dat uw wallet uw eigen knooppunt bevraagt via electrs, wat volledige privacy en een werking zonder vertrouwen biedt.


![image](assets/en/17.webp)


## conclusie


StartOS van Start9 is een gebruiksvriendelijk, privacy-gericht platform ontworpen voor het zelf hosten van essentiële diensten zoals Bitcoin en Lightning nodes, wallets en persoonlijke apps. Het elimineert de noodzaak voor commandoregelvaardigheden door het aanbieden van een schone grafische interface, geautomatiseerde back-ups, gezondheidsmonitoring en veilige Tor-toegang, waardoor het ideaal is voor niet-technische gebruikers. De modulaire architectuur ondersteunt naadloze integratie met tools zoals electrs of Sparrow, waardoor je volledige controle hebt over je financiële en digitale soevereiniteit. Met een sterke focus op transparantie, lokale controle en uitbreidbaarheid stelt StartOS gebruikers in staat om het eigendom terug te winnen van gecentraliseerde platformen en hun eigen privé, veerkrachtige infrastructuur te beheren.