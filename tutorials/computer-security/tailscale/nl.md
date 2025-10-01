---
name: Tailscale
description: Tips voor gevorderde Tailscale
---
![cover](assets/cover.webp)



## 1. Inleiding



Tailscale is een VPN van de volgende generatie dat een versleuteld mesh-netwerk tussen je apparaten creëert. Hiermee kun je externe machines verbinden alsof ze zich op hetzelfde lokale netwerk bevinden, zonder complexe configuratie of het openen van poorten.



Voor self-hosting wijst Tailscale elk apparaat een vast privé IP toe in een virtueel netwerk, waardoor je stabiele toegang tot je diensten hebt, zelfs als je publieke IP verandert. Dit betekent dat u uw servers op afstand kunt beheren, zonder uw diensten direct aan het internet bloot te stellen.



**Voornaamste toepassingen:**




- Een persoonlijke server van buitenaf beheren
- Umbrel/Lightning-knooppunten sneller beheren dan Tor
- Beveiligde toegang tot een Raspberry Pi of NAS
- Maak verbinding met je services via SSH of HTTP zonder complexe netwerkconfiguratie



Deze op eenvoud gerichte aanpak stelt self-hosters in staat om veilig toegang te krijgen tot hun services, waarbij de valkuilen van traditionele VPN's worden vermeden.



## 2. Hoe Tailscale werkt



In tegenstelling tot traditionele VPN's, die al het verkeer via een centrale server leiden, creëert Tailscale een mesh-netwerk waar apparaten rechtstreeks met elkaar communiceren. De centrale server zorgt alleen voor authenticatie en sleuteldistributie, zonder gebruikersgegevens te zien.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Figuur 1: Traditioneel VPN met hub-and-spoke architectuur waarbij al het verkeer via een centrale server gaat*



Op basis van WireGuard genereert elk apparaat zijn eigen cryptografische sleutels. De coördinatieserver verdeelt de openbare sleutels onder de knooppunten, die vervolgens rechtstreeks onderling end-to-end versleutelde tunnels opzetten. Om door firewalls heen te komen, gebruikt Tailscale NAT traversal en, als laatste redmiddel, DERP relais die de versleuteling handhaven.



![VPN maillé (mesh)](assets/fr/02.webp)


*Figuur 2: Tailscale mesh-netwerk waarbij apparaten rechtstreeks met elkaar communiceren*



Alle communicatie wordt versleuteld met WireGuard. Tailscale ziet alleen metadata (verbindingen) maar nooit de inhoud van uitwisselingen. Voor meer soevereiniteit maakt Headscale het mogelijk om de coördinatieserver zelf te hosten.



**Veiligheid en vertrouwelijkheid:** Dankzij WireGuard is alle communicatie op Tailscale end-to-end versleuteld. Tailscale kan uw verkeer niet lezen - alleen uw apparaten hebben de benodigde privésleutels. De service ziet alleen metadata: IP-adressen, apparaatnamen, verbindingstijdstempels en peer-to-peer verbindingslogs (zonder inhoud).



Deze architectuur is echter afhankelijk van Tailscale Inc. voor netwerkcoördinatie. Om deze afhankelijkheid te elimineren, biedt Headscale een open-source alternatief waarmee je de controleserver zelf kunt hosten terwijl je de officiële Tailscale clients gebruikt, waardoor je volledige soevereiniteit over je netwerkinfrastructuur kunt garanderen, ten koste van een meer technische configuratie.



**Voor een gedetailleerde uitleg over de innerlijke werking van Tailscale, inclusief control plane management, NAT traversal en DERP relays, raden we het uitstekende artikel [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) op de officiële blog aan. Dit artikel legt in detail de technische concepten uit die Tailscale zo krachtig maken.**



## 3. Tailscale installeren



Tailscale draait op de **meest voorkomende** besturingssystemen (Windows, macOS, Linux, iOS, Android). De installatie is naar verluidt "snel en eenvoudig" op alle platforms. Laten we eerst eens kijken naar Interface en hoe je een account aanmaakt, en daarna naar de installatieprocedures voor verschillende omgevingen.



### 3.1 Tailscale account aanmaken



Ga naar [https://tailscale.com/](https://tailscale.com/) en klik op de knop "Aan de slag" rechtsboven op de pagina.




![Page d'accueil Tailscale](assets/fr/03.webp)


*De homepage van Tailscale legt het concept uit en biedt een gratis start*



Om Tailscale te gebruiken, moet je eerst een account aanmaken via een identity provider:



![Page de connexion Tailscale](assets/fr/04.webp)


*Keuze van identiteitsprovider om verbinding te maken met Tailscale (Google, Microsoft, GitHub, Apple, etc.)*



Na het inloggen vraagt Tailscale je om wat informatie over het beoogde gebruik:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Formulier om uw use case beter te begrijpen (persoonlijk of professioneel)*



Zodra je een account hebt aangemaakt, kun je Tailscale op je apparaten installeren:



![Ajout du premier appareil](assets/fr/07.webp)


*Met Tailscale kun je de applicatie op verschillende systemen installeren*



### 3.2 Installatie op verschillende platforms





- Op Windows en macOS: Download gewoon de grafische applicatie van de officiële Tailscale website en installeer deze (.msi bestand op Windows, .dmg bestand op Mac). Eenmaal geïnstalleerd, start de applicatie een grafische Interface waarmee je (via een browser) verbinding kunt maken met je Tailscale account om de machine te authenticeren.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*Sluit een MacBook aan op het achterklepje*



![Connexion réussie](assets/fr/09.webp)


*Bevestiging dat het apparaat is aangesloten op het Tailscale* netwerk





- Op Linux (Debian, Ubuntu, enz.): Je hebt verschillende opties. De eenvoudigste methode is om het officiële installatiescript uit te voeren: bijvoorbeeld op Debian/Ubuntu:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Dit script voegt de officiële Tailscale repository toe en installeert het pakket. Je kunt ook [handmatig de APT repository toevoegen] (https://pkgs.tailscale.com) of gewone Snap of apt pakketten gebruiken. Eenmaal geïnstalleerd, zal daemon `tailscaled` op de achtergrond draaien. Je moet dan de node **authenticeren** (zie Interface CLI vs web hieronder). Op andere distributies (Fedora, Arch...) is het pakket ook beschikbaar via de standaard repositories of het universele installatiescript. Voor een headless server, gebruik CLI: bijvoorbeeld `sudo tailscale up --auth-key <key>` als je een vooraf gegenereerde authenticatiesleutel gebruikt, of gewoon `tailscale up` voor een interactieve login (die een URL zal geven om te bezoeken om het apparaat te authenticeren).





- Op ARM-gebaseerde systemen (Raspberry Pi, enz.): We gebruiken over het algemeen Linux, dus dezelfde aanpak als hierboven (script of pakket). Merk op dat Tailscale de ARM32/ARM64-architectuur zonder problemen ondersteunt. Veel gebruikers installeren Tailscale op Raspberry Pi OS via apt of op lichtgewicht distributies (DietPi, etc.) om overal toegang te hebben tot hun Pi.





- **Op iOS en Android:** Tailscale biedt **officiële** mobiele applicaties. Installeer gewoon *Tailscale* in de [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) of de [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Stappen om Tailscale op iPhone te installeren: welkom, privacy, meldingen, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Maak verbinding met tailnet, selecteer account en valideer op iPhone*



Zodra de app is geïnstalleerd, zal hij je bij de eerste keer opstarten vragen om je te authenticeren via de gekozen provider (Google, Apple ID, Microsoft, etc., afhankelijk van wat je gebruikt voor Tailscale) - het is dezelfde procedure als op andere platforms, meestal een omleiding naar een OAuth webpagina. Daarna maakt de mobiele app de VPN aan (op iOS moet je de VPN-configuratie add-on accepteren). De app kan dan op de achtergrond draaien, zodat je overal toegang hebt tot je tailnet. *Let op:* op mobiel kun je maar **één actieve VPN tegelijk** hebben - dus zorg ervoor dat je niet tegelijkertijd een andere VPN hebt aangesloten, anders kan Tailscale zijn eigen VPN niet opzetten. Op Android kun je een apart werkprofiel instellen als je bepaalde toepassingen wilt isoleren (bijvoorbeeld een profiel met Tailscale actief voor een bepaalde app).



### 3.3 Meerdere apparaten toevoegen en valideren



Zodra je eerste apparaat is aangesloten, vraagt Tailscale je om andere apparaten aan je netwerk toe te voegen:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface toont het eerste apparaat dat is aangesloten en wacht op andere apparaten*



Zodra je verschillende apparaten hebt toegevoegd, kun je controleren of ze met elkaar kunnen communiceren:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Bevestiging dat apparaten met elkaar kunnen communiceren via ping*



Tailscale stelt vervolgens aanvullende configuraties voor om uw ervaring te verbeteren:



![Suggestions de configuration](assets/fr/14.webp)


*Suggesties voor het instellen van DNS, het delen van apparaten en het beheren van toegang*



### 3.4 Beheerdashboard



Met de beheerconsole op het web kun je al je aangesloten apparaten bekijken en beheren:



![Tableau de bord des machines](assets/fr/15.webp)


*Lijst van aangesloten apparaten met hun kenmerken en status*



**Interface Web vs Interface CLI:** Tailscale biedt twee complementaire manieren van interactie met het netwerk: de **Interface webadministratie** en de **command-line client (CLI)**.





- **Interface Web (Admin Console)**: toegankelijk via [https://login.tailscale.com](https://login.tailscale.com), deze webconsole is het centrale dashboard voor uw Tailscale netwerk. Het geeft een overzicht van alle apparaten (*machines*), hun online/offline status, hun Tailscale IP-adressen en meer. Hier kunt u **apparaten** beheren (hernoemen, sleutels verlopen, routes autoriseren, een node uitschakelen), **gebruikers** beheren (in een organisatorische context) en beveiligingsregels (ACL's) definiëren. Hier configureer je ook globale opties zoals MagicDNS, tags of auth keys (pre-generate auth keys voor het automatisch toevoegen van apparaten). Interface web is erg handig om een overzicht te krijgen en wijzigingen toe te passen die via de coördinatieserver naar alle knooppunten worden verspreid. *Voorbeeld:* Het activeren van een **subnet route** of een **exit node** gebeurt met een enkele klik in de console, zodra de node in kwestie zichzelf als zodanig heeft aangekondigd.





- **Interface commandoregel (CLI):** Het `tailscale` commando is beschikbaar in CLI op elk apparaat waar Tailscale is geïnstalleerd. Met deze CLI kun je alles lokaal doen: verbinden (`tailscale up`), status inspecteren (`tailscale status` om te zien welke peers verbonden zijn), debuggen (`tailscale ping <ip>`), enzovoort. Sommige functies zijn zelfs **exclusief voor CLI** of geavanceerder, bijvoorbeeld:





  - `tailscale up --advertise-routes=192.168.0.0/24` om een subnet route te adverteren,
  - `tailscale up --advertise-exit-node` om uw machine voor te stellen als een exit-node,
  - `tailscale set --accept-routes=true` (of `--exit-node=<IP>`) om een route te consumeren of een exit-node te gebruiken,
  - `tailscale ip -4` om het Tailscale IP van het apparaat weer te geven,
  - `tailscale lock/unlock` (bij gebruik van *tailnet-lock*, geavanceerde beveiligingsfunctie),
  - of `tailscale file send <node>` om **Taildrop** (bestandsoverdracht tussen apparaten) te gebruiken.


CLI is erg handig op servers zonder Interface afbeeldingen, en voor het scripten van bepaalde acties. **Verschillen in gebruik:** De meeste basisconfiguraties kunnen via het web of via de CLI gedaan worden. Bijvoorbeeld, het toevoegen van een apparaat kan via de console, of door het uitvoeren van `tailscale up` op het apparaat en valideren via het web. Op dezelfde manier kan een apparaat hernoemd worden via de console of met `tailscale set --hostname`. **Samengevat**, de web console is ideaal voor globaal netwerkbeheer (vooral met meerdere machines/gebruikers), terwijl de CLI handig is voor fijnmazige controle over een bepaalde machine, automatiseringsscripts, of gebruik op een systeem zonder GUI.



## 4. Tailscale gebruiken op Umbrel



Umbrel is een populair zelf-hosting platform (met name gebruikt voor Bitcoin/Lightning nodes en andere zelf-hosted diensten, via de App Store). Om Umbrel te installeren en te configureren, raden we je aan onze speciale tutorial te volgen:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Umbrel en Tailscale samen gebruiken is een bijzonder interessante use case, omdat Umbrel van nature een eenvoudig te implementeren Tailscale-module integreert. Dit is hoe Tailscale integreert met Umbrel en wat het oplevert:



### 4.1 Installatie en configuratie van de paraplu





- **Tailscale installeren op Umbrel:** Umbrel heeft een officiële Tailscale-applicatie in de App Store. Installatie kan niet eenvoudiger:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Tailscale applicatiepagina in de Umbrel App Store*



Open vanuit de Interface Web Umbrel de App Store, zoek naar **Tailscale** en klik op *Install*. Enkele seconden later is de applicatie geïnstalleerd op de Umbrel. Wanneer je het opent, toont de Umbrel een pagina waarmee je je knooppunt aan Tailscale kunt koppelen.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Scherm voor staartschaalverbinding in Umbrel's Interface*



Klik gewoon **op "Log in"**, waarna je wordt doorverwezen naar de verificatiepagina van Tailscale:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Maak verbinding met Tailscale via een identity provider*



Je kunt je authenticeren via je Tailscale account (Google/GitHub/etc.) of je e-mail invoeren. Op Umbrel vraagt Interface je meestal om naar [https://login.tailscale.com](https://login.tailscale.com) te gaan en in te loggen - dit authenticeert de Umbrel Tailscale app.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Bevestiging dat het Umbrel-apparaat is aangesloten op het Tailscale-netwerk*



Eenmaal gedaan, is uw Umbrel "in" uw Tailscale netwerk en verschijnt op uw console met een naam (bijv. *umbrel*). U kunt dan op de IP Address van uw apparaten klikken om deze te kopiëren, de IPv6 Address op te halen of uw MagicDNS gekoppeld aan uw apparaat.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Tailscale beheerconsole toont verschillende aangesloten apparaten, waaronder Umbrel*




### 4.2 Externe toegang tot Umbrel-diensten



Zodra Umbrel verbonden is met Tailscale, **heb je overal toegang tot Interface Umbrel en de applicaties die erop draaien, alsof je je op het lokale netwerk bevindt**. Dit is een van de belangrijkste voordelen ten opzichte van Tor.



Toegang is opmerkelijk eenvoudig: in plaats van `umbrel.local` te gebruiken (dat alleen op je lokale netwerk werkt), gebruik je je Umbrel's Tailscale IP Address (`http://100.x.y.z`) direct vanaf elk apparaat dat verbonden is met je tailnet. Dit werkt ongeacht waar je bent of welke internetverbinding je gebruikt (4G, openbaar Wi-Fi, bedrijfsnetwerk).



**Voorbeelden van Umbrel-gehoste applicaties die toegankelijk zijn via Tailscale:**





- **Interface hoofd Umbrel**: Toegang tot uw Umbrel-dashboard door eenvoudigweg `http://100.x.y.z` in uw browser te typen
- **Bitcoin knooppunt**: Beheer uw Bitcoin node zonder vertraging, bekijk synchronisatie en statistieken
- **Lightning Node**: Gebruik ThunderHub, RTL of andere Lightning-beheerinterfaces met onmiddellijke reactiesnelheid
- **Mempool**: Bitcoin transacties en Mempool bekijken zonder Tor-vertragingen
- **noStrudel**: Toegang tot uw Nostr-diensten die worden gehost op Umbrel



**Sluit externe wallets aan op je Bitcoin of lightning nodes via Tailscale:**



Tailscale maakt het ook mogelijk dat je Bitcoin en Lightning wallets die op andere apparaten geïnstalleerd zijn, direct verbinding maken met je Umbrel node:





- **Sparrow wallet (Bitcoin)**: Deze externe Wallet Bitcoin kan rechtstreeks verbinding maken met de Electrum-server van je Umbrel via de Tailscale IP Address:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Een privé Electrum server configureren in Sparrow wallet met behulp van Umbrel's Tailscale IP Address*



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Lijst van Electrum server aliassen in Sparrow met Umbrel Tailscale IP Address*



Lees onze volledige handleiding voor het configureren van Sparrow wallet met uw Bitcoin knooppunt:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- **Zeus (Bliksem)**: Deze Wallet mobiele Lightning kan verbinding maken met je Lightning-node op Umbrel. In plaats van het eindpunt te configureren als `.onion', stel je gewoon het Tailscale IP van je Umbrel en de Lightning API poort in. De verbinding zal onmiddellijk zijn in vergelijking met Tor.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Zeus configureren om verbinding te maken met het Lightning-knooppunt via de Tailscale* IP Address



Raadpleeg onze gedetailleerde tutorial om Zeus te configureren met je Lightning-node:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Om meer te weten te komen over de Lightning Network en hoe deze werkt op Umbrel, bezoek:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Voordelen ten opzichte van Tor



Umbrel biedt van nature toegang op afstand via Tor (door `.onion` adressen aan te bieden voor haar webdiensten). Hoewel Tor het voordeel heeft van vertrouwelijkheid (anonimiteit) en geen registratie vereist, vinden veel gebruikers **Tor traag en instabiel** voor dagelijks gebruik (pagina's laden traag, timeouts, etc.) - *"Umbrel via Tor is zo traag"* klagen sommigen.



Tailscale biedt over het algemeen een **snellere, low-latency** verbinding, omdat het verkeer direct (of via een snelle relay) gaat in plaats van langs 3 Tor nodes. Bovendien biedt Tailscale een "lokaal netwerk" ervaring: er worden privé IP's gebruikt en applicaties kunnen direct in kaart worden gebracht (bijv. SMB netwerkstation op 100.x.y.z).



Dat gezegd hebbende, Tor heeft het voordeel dat het gedecentraliseerd en "out of the box" is op Umbrel, terwijl je voor Tailscale een derde partij moet vertrouwen (of hosting headscale). Tor is ook handig voor clientloze toegang (vanuit elke Tor browser kun je de Umbrel UI raadplegen, terwijl je voor Tailscale de client moet installeren op het apparaat dat toegang zoekt).



**Samenvattend**, voor interactief gebruik (Lightning wallets, frequente webinterfaces) biedt Tailscale merkbaar comfort en snelheid vergeleken met Tor, tegen de prijs van een lichte externe afhankelijkheid. Veel mensen kiezen ervoor om *beide* te gebruiken: Tailscale op een dagelijkse basis, en Tor als fallback of om toegang met iemand te delen zonder ze uit te nodigen in hun VPN.



### 4.4 Veiligheid



Door Tailscale met Umbrel te gebruiken, vermijd je dat Umbrel wordt blootgesteld aan het internet. De Umbrel node is alleen toegankelijk voor je andere geauthenticeerde apparaten in het tailnet, waardoor het aanvalsoppervlak aanzienlijk wordt verkleind (geen poort open voor vreemden, geen risico op aanvallen op de webservice via het internet).



Communicatie wordt versleuteld (WireGuard) bovenop elke versleuteling die je diensten al doen (bijv. zelfs interne HTTP zit in de tunnel). Je kunt nog steeds Tailscale ACL's toepassen om bijvoorbeeld te voorkomen dat een bepaald tailnet apparaat toegang heeft tot Umbrel als je het netwerk wilt partitioneren. Umbrel zelf ziet het verschil niet - het denkt dat het lokaal serveert.



---

Om deze sectie af te sluiten, het integreren van Tailscale op Umbrel neemt slechts een paar klikken in beslag en **verbetert de toegankelijkheid** van je zelf gehoste node enorm. Je kunt Umbrel en haar diensten overal vandaan beheren, veilig en efficiënt, net alsof je thuis bent. Dit is een bijzonder nuttige oplossing voor realtime toepassingen (Lightning) die last hebben van Tor-latentie, of meer in het algemeen voor elke self-host die op zoek is naar een eenvoudige privéverbinding. Dit alles zonder ook maar **één poort** op je box bloot te stellen en zonder ingewikkelde netwerkconfiguratie.



## 5. Geavanceerd beheer en use cases



### 5.1 Tailscale geavanceerde functies



**Netwerkbeheer:** Via de beheerconsole (login.tailscale.com) kunt u uw apparaten beheren, verbindingen bekijken en toegangsregels configureren.



**MagicDNS:** Lost automatisch apparaatnamen op (bijv. `raspberrypi.tailnet.ts.net`) om te voorkomen dat je IP-adressen moet onthouden.



**ACL en toegangscontrole:** Definieer precies wie toegang heeft tot wat in je netwerk via JSON-regels, ideaal om bepaalde apparaten te isoleren of de toegang tot specifieke services te beperken.



*met *Device Sharing kun je iemand uitnodigen voor toegang tot een specifieke machine zonder hem toegang te geven tot je hele netwerk.



**Subnet Router:** Een Tailscale machine kan fungeren als gateway voor een heel subnet, waardoor toegang tot niet-Tailscale apparaten (IoT, printers, etc.) mogelijk is via een enkele geconfigureerde machine.



**Exit Node:** Gebruik een machine als een Internet gateway om af te sluiten met zijn IP. Nuttig voor openbare Wi-Fi of om geografische beperkingen te omzeilen.



**Taildrop:** Een veilig alternatief voor AirDrop, waarmee je bestanden kunt overzetten tussen je Tailscale-apparaten, ongeacht hun platform of locatie. In tegenstelling tot AirDrop, dat beperkt is tot het Apple ecosysteem en fysieke nabijheid, werkt Taildrop tussen al uw apparaten (Windows, Mac, Linux, Android, iOS), zelfs als ze zich in verschillende landen bevinden. Bestanden worden direct overgezet tussen apparaten met end-to-end encryptie, zonder langs een centrale server te gaan. Gebruik de opdrachtregel `taildrop bestand cp` of de grafische Interface toepassing, afhankelijk van je systeem.



### 5.2 Vergelijking met andere oplossingen



**Vs OpenVPN:** Tailscale is veel eenvoudiger te configureren (geen poorten te openen, geen certificaatbeheer) maar impliceert afhankelijkheid van een dienst van een derde partij. OpenVPN is volledig controleerbaar, maar vereist meer expertise.



**Als directe concurrent werkt ZeroTier op Layer 2 (Ethernet), waardoor broadcast/multicast mogelijk is, terwijl Tailscale op Layer 3 (IP) werkt. ZeroTier biedt meer flexibiliteit in het netwerk, terwijl Tailscale de voorkeur geeft aan eenvoud in gebruik.**



**Vs Tor:** Tor biedt anonimiteit die Tailscale niet biedt, maar is veel langzamer. Tor is gedecentraliseerd en vereist geen account, terwijl Tailscale sneller is en een LAN-achtige ervaring biedt.



**Vs WireGuard manual:** Tailscale automatiseert al het sleutel- en verbindingsbeheer dat u bij WireGuard raw handmatig moet doen. Het is in wezen WireGuard + een vereenvoudigd beheer Layer.



Concluderend positioneert Tailscale zichzelf als een moderne, op eenvoud gerichte oplossing, ideaal voor persoonlijk gebruik en kleine teams. Voor puristen van totale controle biedt Headscale een zelf-hosting alternatief.



## 6. Conclusie



**Voordelen van Tailscale:** Tailscale biedt verschillende voordelen voor zelf hosten:





- **Eenvoud en prestaties** - Snelle installatie op alle platformen zonder complexe netwerkconfiguratie. Het verkeer volgt het meest directe pad tussen uw machines (P2P mesh), met de prestaties van het WireGuard-protocol en zonder centrale server om de doorvoer te beperken.
- **Beveiliging en flexibiliteit** - End-to-end encryptie, verminderd aanvalsoppervlak en geavanceerde functies (ACL, SSO/MFA-verificatie). Werkt zelfs achter NAT's of onderweg, met subnet routers en exit nodes om het netwerk aan te passen aan je behoeften.



**Limieten:** Houd er ook rekening mee:





- **Externe afhankelijkheid** - In de standaardversie is de service afhankelijk van de infrastructuur van Tailscale Inc. Deze afhankelijkheid kan worden omzeild via Headscale (zelf hosten alternatief).
- **Andere beperkingen** - Gedeeltelijk gesloten broncode, beperkingen van de gratis versie voor bepaalde geavanceerde toepassingen, geen ondersteuning voor Layer 2 (broadcast/multicast) en toegang tot internet nodig om verbindingen tot stand te brengen.



**Tailscale is ideaal voor individuele self-hosts en kleine teams, ontwikkelaars die toegang nodig hebben tot verspreide bronnen, VPN-beginners en mobiele gebruikers. Voor bedrijven die totale controle nodig hebben, kunnen andere oplossingen zoals Headscale of WireGuard direct de voorkeur hebben.**



**Verken Headscale voor volledige zelf-hosting, API en DevOps integraties (Terraform), of alternatieven zoals Innernet (vergelijkbaar maar volledig zelf gehost) en Netmaker.**



Tailscale is een essentiële tool voor self-hosting, dankzij de eenvoud en efficiëntie, waardoor je privé-infrastructuur net zo toegankelijk is als in de cloud, terwijl je de controle thuis houdt.



## 7. Nuttige bronnen



### Officiële documentatie





- **Tailscale Documentatiecentrum**: [docs.tailscale.com](https://docs.tailscale.com) - Volledige Engelstalige documentatie, installatiegidsen, tutorials en technische referenties.
- **Hoe Tailscale werkt**: [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) - Gedetailleerd artikel over de werking van Tailscale.
- **Changelog**: [tailscale.com/changelog](https://tailscale.com/changelog) - updates en nieuwe functies bijhouden.



### Praktische gidsen





- **Homelab** tutorials: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Specifieke gidsen voor zelf hosten.
- **Een Exit Node configureren**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Gedetailleerde handleiding voor het configureren van Exit Nodes.
- **Gebruik Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Bestanden overzetten tussen Tailscale apparaten.



### Vergelijkingen





- **Tailscale vs. andere oplossingen**: [tailscale.com/compare](https://tailscale.com/compare) - Gedetailleerde vergelijkingen met andere VPN- en netwerkoplossingen (ZeroTier, OpenVPN, etc.).



### Gemeenschap





- **Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Discussies, vragen en feedback.
- **GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Broncode van de klant, waar u de ontwikkeling kunt volgen en problemen kunt melden.
- **Discord**: [discord.gg/tailscale](https://discord.gg/tailscale) - Community van gebruikers en ontwikkelaars.



Tailscale biedt regelmatig nieuwe inhoud en functies. Bekijk hun [officiële blog](https://tailscale.com/blog/) voor het laatste nieuws en case studies.