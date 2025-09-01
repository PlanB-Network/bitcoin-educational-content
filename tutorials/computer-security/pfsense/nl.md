---
name: pfSense
description: Pfsense installeren
---
![cover](assets/cover.webp)



___



*Deze zelfstudie is gebaseerd op originele inhoud van Florian BURNEL gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er zijn belangrijke wijzigingen aangebracht in de oorspronkelijke tekst van de auteur om de zelfstudie up-to-date te maken.*



___



![Image](assets/fr/027.webp)



## I. Presentatie



pfSense is een gratis, open source besturingssysteem dat elke computer, dedicated server of hardware-apparaat verandert in een krachtige, zeer configureerbare router en firewall. Gebaseerd op FreeBSD en bekend om zijn stabiele, robuuste netwerkarchitectuur, zet pfSense al meer dan vijftien jaar de standaard voor open source firewalls voor bedrijven, lokale overheden en veeleisende thuisgebruikers.



De belangrijkste functies zijn in de loop der jaren aanzienlijk geëvolueerd en met elke nieuwe versie verbeterd. Tot op heden biedt pfSense:





- Volledig, gecentraliseerd beheer via een modern, intuïtief en veilig Interface web Interface.
- Krachtige stateful firewall met geavanceerde NAT-ondersteuning (inclusief NAT-T) en granulair regelbeheer.
- Native multi-WAN ondersteuning, waardoor aggregatie of redundantie van internetverbindingen mogelijk is.
- Geïntegreerde DHCP-server en -relais.
- Hoge beschikbaarheid dankzij het CARP-protocol voor failover en de mogelijkheid om pfSense-clusters te configureren.
- Load balancing tussen verschillende verbindingen of servers.
- Volledige ondersteuning voor VPN: IPsec, OpenVPN en WireGuard (vervangt L2TP, nu verouderd).
- Configureerbare captive portal voor toegangscontrole van gasten, vooral in openbare omgevingen of hotels.



pfSense heeft ook een uitbreidbaar pakketsysteem dat het makkelijk maakt om geavanceerde functies toe te voegen, zoals een transparante proxy (Squid), URL filtering of IDS/IPS (Snort of Suricata) direct vanuit het Interface web.



pfSense wordt alleen gedistribueerd voor 64-bit platforms, in overeenstemming met de huidige aanbevelingen van FreeBSD. Het kan geïnstalleerd worden op standaard hardware (PC's, rekservers) of op embedded platformen met een laag vermogen, zoals Netgate appliances of bepaalde x86-boxen met een laag profiel, die veel krachtiger zijn dan oudere Alix-boxen.



Tot slot is het goed om te onthouden dat pfSense minstens twee fysieke netwerkinterfaces nodig heeft: één voor de externe zone (WAN) en één voor het interne netwerk (LAN). Afhankelijk van de complexiteit van je infrastructuur (DMZ, VLAN, meerdere WAN's), kunnen meerdere extra interfaces nodig zijn om de mogelijkheden ten volle te benutten.



## II. Afbeelding downloaden



De laatste stabiele versie van pfSense, op het moment van schrijven van deze tutorial, is 2.8 (uitgebracht in juni 2025). Je kunt het ISO-image of het installatiebestand, aangepast aan jouw hardwareomgeving, rechtstreeks downloaden van de officiële website:





- [Download pfSense](https://www.pfsense.org/download/)



Via het downloadportaal kunt u:





- Architectuur (over het algemeen **AMD64** voor alle moderne hardware).
- Type afbeelding (**Installer USB Memstick** voor installatie via USB-stick, **ISO Installer** voor branden of virtueel bewerken).
- De dichtstbijzijnde downloadspiegel om de overdrachtssnelheid te optimaliseren.



Voor degenen die pfSense willen implementeren in een gevirtualiseerde omgeving (Proxmox, VMware ESXi, VirtualBox...) is er ook een **OVA** image beschikbaar. Deze kant-en-klare virtuele machine vereenvoudigt de installatie en eerste configuratie aanzienlijk. Zorg er alleen voor dat je de toegewezen bronnen (CPU, RAM, netwerkinterfaces) aanpast aan de verwachte belasting en je netwerktopologie.



Voor de installatie raden we aan de integriteit van het gedownloade bestand te controleren door de **SHA256** te verifiëren die op de officiële downloadpagina staat. Dit zorgt ervoor dat de afbeelding niet is gewijzigd of beschadigd.



## III. Installatie



In dit voorbeeld wordt de installatie uitgevoerd op een virtuele machine met VirtualBox. De procedure blijft strikt identiek op een fysieke machine of een andere hypervisor, behalve voor het beheer van virtuele apparaten.



### 1. Minimale hardwarevereisten



Voor een standaardimplementatie raden we:





- minimaal 1 GB RAM** (2 GB of meer wordt aanbevolen om extra pakketten of ZFS-ondersteuning mogelijk te maken).
- 8 GB schijfruimte** (20 GB of meer is te verkiezen voor meer geavanceerde configuraties, vooral als je een proxy cache, IDS/IPS of gedetailleerde logs installeert).
- Ten minste twee virtuele netwerkinterfaces** (één voor het WAN, één voor het LAN). Voeg ze in VirtualBox toe aan de VM-instellingen voor het opstarten.



### 2. Installateur opstarten



Koppel het gedownloade ISO-image aan als een virtueel optisch station in VirtualBox, of plaats de USB-sleutel als je op een fysieke machine installeert. Bij het opstarten verschijnt een opstartmenu:



Als u geen opties selecteert, zal pfSense na een paar seconden automatisch opstarten met de standaardopties. Druk op de toets "**Enter**" om normaal opstarten te starten.



![Image](assets/fr/027.webp)



Wanneer het hoofdmenu verschijnt, druk je snel op de knop "**I**" om de installatie te starten.



![Image](assets/fr/001.webp)



### 3. Oorspronkelijke instellingen installatieprogramma



In het eerste scherm kun je een paar regionale parameters instellen, zoals het lettertype van het scherm en de tekencodering. Deze instellingen zijn nuttig in specifieke gevallen (niet-standaard toetsenborden, seriële schermen, oosterse talen). Voor de meeste installaties behoud je de standaardwaarden en selecteer je "**Accepteer deze instellingen**".



![Image](assets/fr/002.webp)



### 4. Keuze van installatiemodus



Selecteer "**Snelle/Eenvoudige installatie**" om een geautomatiseerde installatie uit te voeren met de aanbevolen opties. Deze methode verwijdert de geselecteerde schijf en configureert pfSense met de standaard partitionering.



![Image](assets/fr/003.webp)



Er verschijnt een waarschuwing die aangeeft dat alle gegevens op de schijf worden verwijderd. Bevestig met "**OK**".



Het installatieprogramma kopieert vervolgens de benodigde bestanden naar de schijf. Afhankelijk van je hardware kan dit enkele seconden tot enkele minuten duren.



### 5. Kernselectie



Wanneer het installatieprogramma je vraagt om het kerneltype te kiezen, laat dan "**Standard Kernel**" geselecteerd. Deze generieke kernel is perfect geschikt voor standaard implementaties, of het nu op een pc, server of VM is.



### 6. Einde installatie en herstart



Zodra de installatie voltooid is, selecteer je "**Reboot**" om je machine opnieuw op te starten op je nieuwe pfSense-instantie.



**Belangrijke opmerking**: verwijder het ISO-image of koppel de installatie-USB los voordat je opnieuw opstart, om te voorkomen dat het installatieprogramma de volgende keer dat je opstart opnieuw opstart.



## IV. PfSense voor de eerste keer starten



Bij de eerste opstart moet pfSense geconfigureerd worden om zijn netwerkinterfaces (WAN, LAN, DMZ, VLAN's, enz.) te herkennen en correct toe te wijzen. Zorgvuldige identificatie van je netwerkkaarten is essentieel om configuratiefouten te vermijden die je de toegang tot Interface web zouden kunnen ontnemen of je firewall buiten werking zouden kunnen stellen.



Bij het opstarten detecteert pfSense automatisch alle beschikbare netwerkinterfaces en maakt er een lijst van, met de MAC Address voor elke interface. Dit maakt het gemakkelijk om ze van elkaar te onderscheiden.



### 1. VLAN's



De eerste vraag betreft de configuratie van VLANs. In dit stadium, voor een basisconfiguratie, zullen we geen VLAN's activeren. Druk dus op de toets "**N**" om deze stap over te slaan.



![Image](assets/fr/004.webp)



### 2. WAN en LAN Interface Assignment



pfSense vraagt je dan om te definiëren welke Interface gebruikt zal worden voor WAN (internettoegang). Je kunt kiezen tussen:





- Voer de Interface naam handmatig in (aanbevolen voor virtuele omgevingen).
- Gebruik automatische detectie door op "**A**" te drukken. Deze optie is nuttig op een fysieke host, op voorwaarde dat je netwerkkabels zijn aangesloten en de links actief zijn.



![Image](assets/fr/005.webp)



In dit voorbeeld configureren we het WAN handmatig. Voer de exacte naam van de Interface in. Voor een Intel-bord zal de naam vaak "**em0**" zijn onder FreeBSD, maar het kan variëren afhankelijk van de hardware. Een Realtek kaart wordt bijvoorbeeld vaak weergegeven als "**re0**".



![Image](assets/fr/006.webp)



Herhaal dezelfde handeling om het Interface LAN te definiëren. Hier gebruiken we "**em1**".



pfSense bevestigt dat de Interface LAN zowel firewall als NAT activeert om je interne netwerk te beschermen en de Address vertaling te beheren.



Als je andere fysieke interfaces hebt, kun je in dit stadium extra interfaces configureren (DMZ, Wi-Fi, specifieke VLAN's). Elke logische Interface heeft een bijbehorende netwerkkaart of virtuele Interface nodig. Voor de eerste configuratie beperken we ons tot WAN en LAN.



Zodra de toewijzingen zijn voltooid, toont pfSense een duidelijk overzicht van de correspondenties tussen fysieke interfaces en toegewezen rollen. Bevestig met "**Y**".



### 3. PfSense console



Wanneer deze stap voltooid is, verschijnt het hoofdmenu van de pfSense console. Het biedt verschillende handige opties voor direct beheer, zoals het resetten van het webwachtwoord, herstarten, opnieuw laden van de configuratie of het opnieuw toewijzen van interfaces.



![Image](assets/fr/007.webp)



Je ziet ook een overzicht van de huidige netwerkinstellingen, inclusief het standaard IP-adres Address van het Interface LAN, meestal **192.168.1.1**. Dit is de Address die je in je browser moet invoeren om toegang te krijgen tot het Interface administratieweb.



**Noot**: Als uw interne netwerk een ander Address bereik gebruikt, selecteer dan "**2)** Stel Interface(s) IP Address in" in het menu om een IP Address toe te wijzen die geschikt is voor uw omgeving.



Als uw Interface WAN standaard verbonden is met een DHCP-geconfigureerde box of modem, zal pfSense automatisch een openbaar IP-adres Address ophalen. Je zou dus moeten profiteren van onmiddellijke internettoegang door een client aan te sluiten op het pfSense Interface LAN.



## V. Eerste toegang tot Interface web



Zodra de initiële opstart voltooid is en de netwerkinterfaces geconfigureerd zijn, kunt u toegang krijgen tot het Interface web van pfSense om uw configuratie af te ronden en te fine-tunen.



### 1. Eerste aansluiting



Sluit een computer aan op de LAN-poort (of het virtuele Interface LAN in uw hypervisor) en wijs indien nodig een IP Address toe in hetzelfde bereik (standaard distribueert pfSense automatisch een Address via DHCP op het LAN).



Ga in je browser naar de Address die de console aangeeft (standaard `https://192.168.1.1`). Merk op dat pfSense HTTPS vereist, zelfs voor de eerste verbinding - verwacht dus een waarschuwing voor een zelfondertekend certificaat, die je kunt negeren door een uitzondering toe te voegen.



Het inlogscherm verschijnt. De standaardgegevens zijn:




- Gebruikersnaam:** `admin`
- Wachtwoord:** `pfsense`



Deze identifiers worden gewijzigd tijdens de eerste configuratiewizard.



## VI. Setup Wizard



Bij de eerste verbinding vraagt pfSense je om de **Setup Wizard** te volgen. We raden je ten zeerste aan deze te gebruiken om er zeker van te zijn dat alle essentiële parameters correct zijn gedefinieerd.



### 1. Algemene parameters



U kunt:




- Geef een hostnaam en een lokaal domein op (voorbeeld: `pfsense` en `lan.local`).
- Definieer DNS-servers en kies of pfSense de DNS van je ISP of een externe service (Cloudflare, OpenDNS, Quad9...) moet gebruiken.



### 2. Tijdzone



Geef de tijdzone van je site aan zodat logs en schema's consistent zijn (bijvoorbeeld `Europa/Parijs`).



### 3. WAN-configuratie



De WAN-verbinding configureren:




- Staat standaard op **DHCP** (voldoende als je achter een doos zit).
- Als je een vast IP hebt, voer je de parameters (statisch IP, masker, gateway, DNS) handmatig in.
- Definieer indien nodig een VLAN of PPPoE-authenticatie (gebruikelijk bij sommige ISP's).



### 4. LAN-configuratie



De wizard stelt voor om het standaard LAN-subnet te wijzigen. Als je een specifiek adresseringsplan hebt, is dit het moment om het aan te passen.



### 5. Beheerderswachtwoord wijzigen



Beveilig je pfSense door direct een sterk wachtwoord in te stellen voor de `admin` gebruiker.



## VII. Verificatie en updates



Voordat u uw firewall inzet, moet u ervoor zorgen dat u de nieuwste versie van:





- Ga naar **Systeem > Update**.
- Selecteer het updatekanaal (meestal **Stable**).
- Controleer op updates en pas ze toe.



Het is een goed idee om updatemeldingen in te schakelen zodat je op de hoogte blijft van beveiligingspatches.



## VIII. De configuratie opslaan



Implementeer een back-upbeleid voordat je grote veranderingen doorvoert:





- Ga naar **Diagnostiek > Back-up en herstel**.
- Download een kopie van de huidige configuratie (`config.xml`).
- Bewaar het op een veilige plaats (versleutelde externe media).



Overweeg voor missiekritische omgevingen een automatische back-up van de configuratie op een externe server of via een geprogrammeerd script.



## IX. Beste praktijken na installatie



Om je uitzending met een gerust hart te beëindigen:





- Pas firewallregels** aan: standaard staat pfSense al het uitgaande verkeer op het LAN toe en blokkeert het inkomend verkeer op het WAN. Pas deze regels naar wens aan.
- Configureer veilige toegang op afstand**: indien nodig, schakel toegang tot Interface web vanaf het WAN alleen in via VPN of met IP beperkingen.
- Meldingen** inschakelen: configureer een SMTP-server voor het ontvangen van meldingen (storingen, updates, fouten).
- Installeer nuttige extensies**: bijvoorbeeld IDS/IPS (Snort, Suricata), proxy (Squid), DNS-filtering (pfBlockerNG).



Je pfSense firewall is nu klaar om je netwerk te beschermen. Dankzij de flexibiliteit en actieve community beschikt u over een krachtige, schaalbare tool die zich kan aanpassen aan uw toekomstige behoeften (multi-WAN, VLAN, site-to-site VPN, captive portal, enz.).



Raadpleeg de officiële documentatie ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) regelmatig om nieuwe functies te ontdekken en ervoor te zorgen dat uw configuratie up-to-date en veilig is.