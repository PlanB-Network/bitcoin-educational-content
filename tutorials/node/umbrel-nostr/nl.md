---
name: Umbrel Nostr
description: Nostr-toepassingen configureren en gebruiken op Umbrel
---

![cover](assets/cover.webp)



## Vereisten: Paraplu-installatie



Umbrel is een open-source platform waarmee je eenvoudig Bitcoin toepassingen en andere diensten kunt hosten op je eigen persoonlijke server. Het is een alles-in-één oplossing die het zelf hosten van Bitcoin nodes en gedecentraliseerde toepassingen sterk vereenvoudigt.



Zorg ervoor dat u Umbrel hebt geïnstalleerd door onze installatiehandleiding te volgen:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Inleiding tot Nostr



**Nostr** is een open, gedecentraliseerd netwerkprotocol ontworpen voor sociale netwerken. De naam staat voor _"Notes and Other Stuff Transmitted by Relays"_. Iedereen kan berichten (notities) publiceren, beheerd als JSON-gebeurtenissen, en ze verspreiden via relaisservers in plaats van een gecentraliseerd platform. Elke gebruiker bezit een paar cryptografische sleutels (privaat/publiek) die dienen als identificatie: de publieke sleutel (npub) identificeert de gebruiker en de privésleutel (nsec) maakt het mogelijk om berichten te ondertekenen. Dankzij deze gedistribueerde architectuur biedt **Nostr censuurbestendigheid** en grote flexibiliteit: je kunt verschillende clients gebruiken en verbinding maken met zoveel relays als je wilt, zonder afhankelijk te zijn van één enkele server.



In het kort is Nostr een gedecentraliseerd communicatieprotocol waarbij **clients** (gebruikerstoepassingen) gebeurtenissen verzenden en ontvangen via **relayers** (servers). Dit protocol is sinds 2023 bijzonder populair bij de Bitcoin gemeenschap, vanwege de waarden van decentralisatie en gegevenssoevereiniteit.



**Noot:** Om Nostr te gebruiken, hebt u uw privésleutel nodig (gegenereerd door een Nostr-client of via een specifieke extensie). **Deel nooit uw privésleutel**, want dan kan iedereen zich voordoen als u. Bewaar de sleutel op een veilige plaats en gebruik veilige sleutelbeheertools (zie Tip hieronder). Bewaar hem op een veilige plaats en gebruik veilige sleutelbeheerprogramma's (zie Tip hieronder).



## Toepassingen voor Nostr



Umbrel biedt een ecosysteem van geïntegreerde toepassingen om ten volle te profiteren van Nostr op je persoonlijke node. We gaan het gebruik van de belangrijkste Nostr-gerelateerde applicaties in detail bespreken: **Nostr Relay**, **noStrudel**, **Snort** en **Nostr Wallet Connect**. Elk voorziet in een specifieke behoefte: _Nostr Relay_ is een **private relay server**, _noStrudel_ en _Snort_ zijn **Nostr clients** (interfaces voor het lezen/publiceren van notities), terwijl _Nostr Wallet Connect_ een hulpmiddel is om je **Lightning Wallet** aan Nostr te koppelen.



### Nostr Relais - Jouw privé relais op Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** is Umbrel's officiële applicatie voor het draaien van je **eigen Nostr relais** op je knooppunt. Het belangrijkste doel is om een **privé** en betrouwbaar relais te hebben om **een back-up te maken van al je Nostr** activiteiten in realtime. Met andere woorden, door dit persoonlijke relais naast de publieke relais te gebruiken, zorg je ervoor dat al je notities, berichten en reacties naar huis worden gekopieerd, veilig voor censuur of gegevensverlies.



**Installatie:** In de Umbrel App Store (categorie _Social_) installeer je _Nostr Relay_. Eenmaal gestart, draait de applicatie op de achtergrond (docker service).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Je ziet het Interface web via Umbrel: het geeft basisinformatie en vooral de URL van je relais (rechtsboven), die je moet kopiëren voor verder gebruik. Er is ook een synchronisatieknop (wereldbolpictogram) beschikbaar.



**Om te profiteren van uw Umbrel-relais:**



**Voeg de relay toe aan je Nostr client:** Voeg in je clientapplicatie (bijv. Damus op iOS, Amethyst op Android, Snort of noStrudel op Umbrel, enz.) de URL toe van je privé relay die je eerder hebt gekopieerd. Standaard luistert de Umbrel relay op poort **4848**. Als je het via het lokale netwerk benadert, geeft dit een URL als: `ws://umbrel.local:4848` (of gebruik het lokale IP van de Umbrel).



Als je Tailscale gebruikt (zie hieronder), kun je zelfs de MagicDNS DNS alias gebruiken (meestal `umbrel` of een automatisch gegenereerde naam) om er overal toegang toe te krijgen, altijd op poort 4848.



Als je de voorkeur geeft aan Tor, haal dan je Umbrel's .onion Address op en gebruik het met poort 4848 via een Tor-compatibele browser of client (zie Tor sectie)



Zodra de URL is toegevoegd aan de Relay-configuratie van je Nostr-client, maak je verbinding met dit relais. Je zou in je client moeten zien dat het Umbrel relais verbonden is (meestal aangegeven met een Green punt of iets dergelijks).



**Geschiedenis synchroniseren (optioneel)**: In het Interface web van _Nostr Relay_ op Umbrel, klik op het **globe** 🌐 icoon (bovenaan de pagina). Deze actie zal je Umbrel relais dwingen om verbinding te maken met je andere relais (die geconfigureerd zijn in je client) om **je oude publieke** activiteiten te importeren. Dit betekent dat notities die u in het verleden hebt gepubliceerd of gelezen via openbare relais, ook worden gedownload en opgeslagen op uw privérelais. Wacht tot de synchronisatie heeft plaatsgevonden.



**Gebruik Nostr zoals gewoonlijk:** Vanaf nu zal elke nieuwe activiteit (gepubliceerde notities, reacties, versleutelde privéberichten, enz.) die je uitvoert op Nostr zoals gewoonlijk worden doorgestuurd naar de publieke relais **en parallel naar je Umbrel relais**. Als je Nostr-client goed is geconfigureerd, zal hij elke gebeurtenis naar alle relais sturen (inclusief die van jou). Uw privérelais zal fungeren als een real-time back-up. Zelfs als de verbinding tijdelijk wordt verbroken, kunnen uw klanten de ontbrekende gegevens later opnieuw synchroniseren dankzij dit relais



Op de achtergrond is Umbrel's _Nostr Relay_ gebaseerd op het open-source **nostr-rs-relay** project (Rust protocol implementatie). Het ondersteunt het volledige Nostr-protocol en talrijke standaard NIP's (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, enz.), waardoor maximale compatibiliteit met klanten wordt gegarandeerd.



### noStrudel - Nostr-client voor verkenners



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** is een gebruiksvriendelijke Nostr webclient, ideaal om het Nostr-netwerk in detail te begrijpen en te verkennen. Het is een soort zandbak voor het inspecteren van gebeurtenissen en relays, en voor het experimenteren met de geavanceerde functies van het protocol. Interface is Engelstalig en relatief technisch, waardoor het ideaal is voor ervaren gebruikers die nieuwsgierig zijn naar de innerlijke werking van Nostr.



**Installatie:** Installeer _noStrudel_ uit de Umbrel App Store (categorie _Social_). Eenmaal gestart, is het toegankelijk via je browser op je Umbrel's Address (bijv. `http://umbrel.local` of via zijn .onion/Tailscale, zie externe toegang sectie).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Relais configureren:** Als je NoStrudel opent, zie je rechtsboven een knop "Relais instellen". Klik erop om je relais te configureren.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Plak op deze pagina de URL van uw Umbrel relais die u eerder hebt gekopieerd. U kunt ook andere relais toevoegen die standaard door de applicatie worden voorgesteld. Zodra u uw relais hebt geconfigureerd, klikt u op "Aanmelden" linksonder om verder te gaan.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Connectie:** noStrudel biedt je verschillende verbindingsopties. In ons geval kiezen we "Private Key" en plakken we je eerder gegenereerde Nostr-privésleutel erin. Als je nog geen sleutel hebt, kun je de [Nostr Connect] extensie installeren (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) om je Nostr-sleutels aan te maken en/of op te slaan en zo veiliger te communiceren met de verschillende Nostr-toepassingen.



![Interface principale de noStrudel](assets/fr/07.webp)



Eenmaal verbonden kun je noStrudel gebruiken om je notities te delen via Nostr. Interface geeft je toegang tot :





- Compleet Nostr dashboard met notities tijdlijn, notificaties, berichten, profiel zoeken
- Relaisbeheer en verbindingsstatus
- Geavanceerde tools voor het onderzoeken van gebeurtenissen en hun JSON-inhoud
- Configuratieopties voor tijdlijnfilters en PIN's



**Tip:** Op _noStrudel_ kun je _tijdlijnfilters_ instellen of verschillende _NIP's (Nostr Implementation Possibilities)_ testen. Controleer bijvoorbeeld de ondersteuning voor NIP-05 (gedecentraliseerde identifiers) of recentere functies. Dit maakt _noStrudel_ een uitstekend hulpmiddel om te experimenteren in een gecontroleerde omgeving.



### Snort - Moderne Nostr-klant op Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** is een andere Nostr webclient beschikbaar op Umbrel en biedt een moderne, snelle en overzichtelijke **Interface** voor interactie met het gedecentraliseerde sociale netwerk. In tegenstelling tot noStrudel, dat zich richt op krachtige gebruikers, streeft _Snort_ naar eenvoud in gebruik zonder functionaliteit op te offeren. Het is gebouwd in React en biedt een verzorgde UX die doet denken aan klassieke sociale netwerken, waardoor het geschikt is voor dagelijks gebruik.



**Installatie:** Installeer _Snort_ uit de Umbrel App Store (categorie _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Als je Snort opent, zie je linksonder een knop "Registreren".



![Options de connexion dans Snort](assets/fr/10.webp)



Je kunt kiezen om je te registreren of om verbinding te maken met een bestaande account (wat we in deze tutorial gaan doen).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort biedt verschillende verbindingsmethoden. Je kunt de eerder geïnstalleerde Nostr Connect-extensie of andere beschikbare methoden gebruiken. Eenmaal verbonden, kun je de applicatie volledig gebruiken.



De Interface van _Snort_ biedt :





- Een **Posts/Conversations/Global**-weergave om te navigeren tussen je notities, discussies in een draadje of de globale feed
- Tabbladen voor **Meldingen**, **Berichten** (DM), **Zoeken**, **Profiel**, enz.
- Een **+** of _Schrijf_ knop om een nieuwe notitie te publiceren
- Beheer van **abonnementen (volgen)** en **lijsten**
- Relaisbeheermenu om relais toe te voegen/te verwijderen en hun beschikbaarheid bij te houden



**Aanbevolen relaisconfiguratie:** Om uw Umbrel relais toe te voegen, gaat u naar Instellingen - Relais. Voer de URL van je relais in (`ws://umbrel:4848` of een andere URL afhankelijk van je configuratie) in de lijst met relais van Snort. Op deze manier publiceert Snort je notities op je privé relay naast de publieke.



### Nostr Wallet Connect - Koppel je Lightning Wallet aan Nostr



**Nostr Wallet Connect (NWC)** is een applicatie die je Umbrel **(Lightning) knooppunt** verbindt met compatibele Nostr applicaties om Lightning betalingen te doen (bijvoorbeeld *zaps* sturen, die microbetalingen voor het "liken" van inhoud). In deze tutorial bekijken we hoe je noStrudel kunt verbinden met je Lightning-node om betalingen rechtstreeks vanuit de Interface te doen.



**Installatie en configuratie:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Installeer _Nostr Wallet Connect_ uit de Alby Store op Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



Klik in noStrudel rechtsboven op je profiel en vervolgens op de knop "beheren".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Klik op "Lightning" en dan op "Wallet aansluiten".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Kies "Umbrel" uit de beschikbare verbindingsopties.



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Klik op "Verbinden" om automatisch doorgestuurd te worden naar uw Umbrel Nostr Wallet Connect sessie.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Op de Nostr Wallet Connect pagina kun je :




   - Bepaal je maximale budget
   - Autorisaties valideren
   - Stel een verlooptijd in voor de verbinding


Klik op "verbinden" om af te ronden.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Je wordt doorgestuurd naar noStrudel met een bevestigingsbericht: je kunt nu de hele wereld zappen vanaf je Wallet/LND knooppunt!



Dankzij NWC starten je **Lightning-betalingen via Nostr** (zaps naar beloningsposten, *Value for Value* betalingen, enz.) vanuit je eigen knooppunt. Je hoeft je transacties niet langer via externe diensten te routeren of elke keer een QR op je telefoon te scannen. De gebruikerservaring is sterk verbeterd, terwijl het *niet-bewaard* en privacy-vriendelijk blijft.



Als je wilt weten hoe je je eigen Lightning-node instelt op Umbrel, raad ik je aan deze andere uitgebreide tutorial te bekijken:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Geavanceerde configuratie en beveiliging



Umbrel en Nostr samen gebruiken op een geavanceerd niveau vereist speciale aandacht voor **beveiliging** en **connectiviteit**. Hier zijn een paar tips over hoe u uw configuratie kunt beschermen en er optimaal toegang toe kunt krijgen, waar u ook bent.



### Beveiligde externe toegang: Tor en Tailscale



Om veiligheidsredenen is je Umbrel standaard alleen toegankelijk op je lokale netwerk (en via Tor). Om met Nostr te communiceren als je niet thuis bent, heb je twee voorkeursoplossingen: **Tor** (anonieme toegang via een ui-netwerk) en **Tailscale** (privé VPN-netwerk).





- **Toegang via Tor:** Umbrel configureert automatisch een **Tor service (.onion)** voor haar Interface web en applicaties. Dit betekent dat je overal toegang hebt tot Interface Umbrel (inclusief *noStrudel* of *Snort*) met behulp van de Tor-browser, zonder je publieke IP-adres bloot te geven. Tor wordt gebruikt om toegang te krijgen tot je Umbrel-diensten van buiten je lokale netwerk, zonder je apparaat bloot te stellen aan het internet ([Tor instellen op je systeem - Gidsen - Umbrel Community](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww.tor.org)). Om deze optie te gebruiken, ga je naar de Umbrel-instellingen en haal je de .onion URL van je Umbrel op (of scan je de meegeleverde QR-code). Open deze .onion Address in een Tor-browser: je krijgt dezelfde Interface als lokaal. Je kunt dan je Nostr-apps gebruiken zoals thuis.


**Nostr relay via Tor:** Als je wilt dat je Nostr relay bereikbaar is via Tor door je klanten (of geautoriseerde vrienden), dan is dit mogelijk. Umbrel levert de .onion Address van het relais niet direct, maar omdat het op poort 4848 draait, kun je :





    - Gebruik de UI Umbrel's .onion Address en configureer je client om via deze Interface te verbinden (onpraktisch voor WebSocket),





- Of poort 4848 blootstellen als een aparte onion service. Dit vereist geklungel met de Tor configuratie op Umbrel (gereserveerd voor gevorderde gebruikers die bekend zijn met SSH). Als alternatief kun je een **Tor tunnel** op een andere server overwegen die doorverwijst naar Umbrel: voor persoonlijk gebruik is het echter het makkelijkst om Tailscale te gebruiken.





- Toegang via **Tailscale:** [Tailscale](https://tailscale.com/) is een mesh VPN-oplossing die een virtueel privénetwerk creëert tussen uw apparaten en Umbrel. Het voordeel: het werkt alsof u op een LAN zit, maar dan via het internet, versleuteld en zonder complexe configuratie. **Tailscale wijst je Umbrel een vast IP-adres en een privédomeinnaam toe, ongeacht de netwerklocatie** ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard)). In de praktijk, zodra je Tailscale hebt geïnstalleerd op Umbrel (in de Umbrel App Store, categorie *Networking*) **en** op je apparaten (mobiel, PC...), kun je Umbrel bereiken via een Address als `100.x.y.z` (Tailscale IP) of een naam als `umbrel.tailnet123.ts.net`.


voor Nostr_ is Tailscale extreem nuttig: je mobiel, als het Tailscale actief heeft, zal verbinding kunnen maken met `ws://umbrel:4848` (dankzij MagicDNS) of direct met het Tailscale IP en poort 4848 om de relay te gebruiken. Clients zoals Damus of Amethyst zullen je Umbrel zien alsof deze zich op hetzelfde lokale netwerk bevindt. **Tip:** Schakel de **MagicDNS** optie in Tailscale in om de hostnaam `umbrel` te gebruiken in plaats van het IP te onthouden. Dit zorgt voor een soepele verbinding met uw relais, zelfs als u onderweg bent ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Bovendien kun je met Tailscale de Interface Umbrel (en dus de _noStrudel/Snort_ webclients) benaderen via een eenvoudige browser, door gebruik te maken van het privé IP of de toegewezen domeinnaam. Je hebt geen Tor Browser nodig en de snelheid van gegevensoverdracht is over het algemeen beter dan via het Tor netwerk.




**Opmerking: Tor en Tailscale sluiten elkaar niet uit. Je kunt Tor actief houden voor geanonimiseerde toegang of specifieke diensten en Tailscale dagelijks gebruiken vanwege de eenvoud. In beide gevallen hoef je geen poort te openen op je router, wat de beveiliging versterkt.**



### Uw Nostr-relais beveiligen (aanbevolen werkwijzen)



Als u een Nostr relais host op Umbrel, vooral in een geavanceerde context, zorg er dan voor dat u een paar goede praktijken toepast:





- Privérelais of relais met beperkingen: Standaard is uw Umbrel-relais privé (niet publiekelijk aangekondigd) en als u er alleen toegang toe hebt via Tailscale of uw LAN, blijft het ontoegankelijk voor vreemden. **Houd de link vertrouwelijk** Zend het niet uit op openbare Nostr-netwerken tenzij u vrijwillig andere gebruikers wilt hosten, wat een heel ander probleem is (moderatie, bandbreedte, enz.). Voor persoonlijk gebruik raden we aan de toegang te beperken tot uzelf en, indien nodig, tot een paar vertrouwde vrienden en familie.





- **Whitelist / Auth**: De nostr-rs-relay implementatie ondersteunt een **NIP-42** authenticatiemechanisme en *whitelists* van publieke sleutels. Door deze opties in te schakelen, kun je je relay beperken zodat hij **alleen events accepteert die zijn ondertekend door bepaalde sleutels (de jouwe)**, of dat clients zich moeten authenticeren om te publiceren. Het instellen hiervan vereist het bewerken van het `config.toml` configuratiebestand van de relay in Umbrel (via SSH in de Docker-container). Het is een geavanceerde manipulatie, maar je kunt bijvoorbeeld een lijst maken met toegestane advertenties (`pubkey_whitelist`). Op deze manier, zelfs als iemand je relais ontdekt, zullen ze niet in staat zijn om daar iets te publiceren als ze niet op de lijst staan.





- **Updates en onderhoud:** Houd je Umbrel en de _Nostr Relay_ app up-to-date. Updates kunnen prestatieverbeteringen (bijv. betere spamverwerking) en beveiligingsfixes bevatten. Controleer op Umbrel regelmatig de App Store op updates voor _Nostr Relay_ en pas deze indien nodig toe.





- **Bewaking en limieten:** Houd in de gaten hoe je relais wordt gebruikt. Als je het openstelt voor anderen, houd dan de belasting (CPU/RAM opslag) op je Umbrel in de gaten, aangezien een relay snel veel data kan verzamelen. nostr-rs-relay biedt configureerbare **snelheid en opslaglimieten** (`limieten` in de configuratie, bijv. aantal events per seconde, max event grootte, verwijderen van oude events...). Voor privégebruik hoef je deze waarschijnlijk niet aan te raken, maar wees je ervan bewust dat deze parameters bestaan als je ze nodig hebt ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- **Nostr-sleutels beveiligen:** Dit punt is al genoemd, maar het is cruciaal: voer uw Nostr-privésleutels nooit in een Interface in die u niet volledig vertrouwt. Gebruik in plaats daarvan browserextensies of externe apparaten (zoals Nostr *signers* op aparte telefoons) om gevoelige acties te ondertekenen. Op Umbrel kunnen uw webclients zoals *Snort* en *noStrudel* werken zonder uw geheime sleutel te kennen, via NIP-07. Maak gebruik van deze mogelijkheid om comfort en veiligheid te combineren.




Door deze tips te volgen, zal uw integratie van een Umbrel knooppunt met Nostr zowel krachtig **als** veilig zijn. U zult een complete omgeving hebben: een Bitcoin knooppunt voor Lightning betalingen, een private Nostr relais voor gegevenssoevereiniteit en krachtige Nostr web clients om door dit nieuwe gedecentraliseerde sociale netwerk te navigeren. Veel plezier met het verkennen van Nostr met Umbrel!