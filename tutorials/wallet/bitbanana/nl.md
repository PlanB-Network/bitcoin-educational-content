---
name: BitBanana
description: Mobiele manager voor je Lightning-knooppunt
---

![cover](assets/cover.webp)



In deze tutorial leer je hoe je BitBanana installeert en configureert op Android om je Lightning-node te besturen vanaf je smartphone. We zien hoe je de app kunt verbinden met je bestaande infrastructuur (Umbrel, RaspiBlitz, myNode of een LND/Core Lightning-knooppunt), Lightning-betalingen kunt doen, je kanalen op afstand kunt beheren, je routing-inkomsten kunt bekijken en een back-up kunt maken van je configuraties. Je leert ook over de beste beveiligingspraktijken om de toegang tot je knooppunt te beschermen en hoe het zich verhoudt tot Zeus, een populair alternatief.



## Kennismaking met BitBanana



BitBanana is een open source mobiele Android-applicatie die uw smartphone verandert in een compleet dashboard voor controle op afstand van uw Lightning-node. In tegenstelling tot Lightning-wallets, die een lokaal knooppunt in de telefoon inbouwen, werkt BitBanana 100% op afstand: de app heeft geen satoshi en maakt alleen verbinding met uw bestaande infrastructuur.



De applicatie is ontwikkeld door Michael Wünsch onder MIT-licentie en garandeert volledige transparantie zonder verzameling van persoonlijke gegevens en geverifieerde reproduceerbare builds. BitBanana ondersteunt LND en Core Lightning via standaard URI's (`lndconnect://` en `clngrpc://`), wat de initiële configuratie drastisch vereenvoudigt. De applicatie herkent ook LndHub en Nostr Wallet Connect voor gebruikers zonder persoonlijk knooppunt, hoewel deze modi custodially werken met beperkte functionaliteit.



De interface biedt volledige toegang tot alle cruciale functies van uw node: verzenden en ontvangen van betalingen (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), beheer van Lightning-kanalen (openen, sluiten, vergoeding aanpassen, herbalanceren), geavanceerde muntcontrole en wachttorenbeheer. BitBanana implementeert ook verschillende robuuste beveiligingslagen: biometrische vergrendeling, stealth-modus, Emergency PIN en native Tor-ondersteuning om verbindingen te anonimiseren.



## Ondersteunde platforms en installatie



### Installatie



BitBanana is uitsluitend beschikbaar voor Android 8.0 of hoger. De applicatie bestaat niet op iOS en er is geen versie gepland. Deze beperking wordt verklaard door de geschiedenis van het project: BitBanana is de directe opvolger van Zap Android, oorspronkelijk ontwikkeld door Michael Wünsch, die besloot zijn werk voort te zetten onder zijn eigen merk. Zap was een familie van afzonderlijke toepassingen (Zap Android, Zap iOS, Zap Desktop) ontwikkeld door verschillende medewerkers met afzonderlijke codebases. BitBanana werkt alleen aan de Android-tak.



Bovendien stelt het iOS-ecosysteem aanzienlijke regelgevende en technische beperkingen aan Lightning-toepassingen die niet onder toezicht staan. In 2023 wees Apple een Zeus-update af wegens "licentieovertredingen" en in 2024 verliet Phoenix Wallet de Amerikaanse App Store vanwege onzekerheden in de regelgeving met betrekking tot Lightning-dienstverleners. Deze obstakels verklaren waarom veel Lightning-ontwikkelaars de voorkeur geven aan Android, dat een meer open beleid biedt voor niet-Custodial-toepassingen.



Er zijn drie installatiemethoden beschikbaar voor Android: Google Play Store (5000+ installaties, automatische updates), F-Droid (reproduceerbare builds, broncode verificatie), of handmatige APK van GitHub.



![BitBanana](assets/fr/01.webp)



De officiële bitbanana.app website (links) gaat prat op "100% Self-Custodial with ZERO data collection". Het centrale scherm toont de drie downloadopties: F-Droid (aanbevolen), Google Play en APK. Het scherm rechts toont de toestemming voor meldingen voor betalingswaarschuwingen.



De applicatie vraagt om rechten: netwerk (knooppuntverbinding), camera (QR-codes), NFC (LNURL), achtergronddiensten (meldingen), biometrie (beveiliging) en WireGuard VPN. Geen trackers, geen gegevensverzameling. Schakel een wachtwoord of biometrische vergrendeling in om de toegang te beveiligen.



## Eerste configuratie



### Verbinden met een LND knooppunt



Om BitBanana te verbinden met uw LND knooppunt (Umbrel, RaspiBlitz, myNode), verkrijgt u een `lndconnect` URI of QR-code die het adres, het TLS-certificaat en de authenticatiemacaron bevat.



Voor deze tutorial gebruiken we een LND knooppunt via umbrel. Zie voor meer details onze speciale tutorial :



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Open in de Lightning Node-toepassing het menu rechtsboven en selecteer "wallet verbinden".



![BitBanana](assets/fr/04.webp)



Selecteer **gRPC (Tor)** om verbinding te maken via Tor (aanbevolen). De QR code en details (Host .onion, Poort 10009, Macaroon) worden weergegeven.



![BitBanana](assets/fr/02.webp)



Druk in BitBanana op "CONNECT NODE", scan de QR-code of plak de URI. Autoriseer de toegang tot de camera en controleer het weergegeven .onion-adres voordat u bevestigt.



**Core Lightning**-verbinding



Als je Core Lightning (CLN) gebruikt in plaats van LND, blijft het proces identiek, met de URI `clngrpc://` die de wederzijdse TLS-certificaten bevat. Core Lightning ondersteunt BOLT12 (offertes), waardoor herbruikbare facturen en terugkerende betalingen mogelijk zijn die niet beschikbaar zijn op LND.



**Verbinding zonder persoonlijk knooppunt (LNbits/hosted)**



Als u geen Lightning-knooppunt heeft, kan BitBanana verbinding maken met gehoste diensten via LndHub (het protocol dat wordt gebruikt door BlueWallet en LNbits) of Nostr Wallet Connect (NWC). Let op: deze modi werken in custodial mode (de dienst host uw fondsen) met beperkte functionaliteit. U kunt geen kanalen beheren of routeringskosten configureren en u kunt alleen Lightning-betalingen verzenden en ontvangen.



Raadpleeg voor meer informatie over LNbits of Nostr Wallet Connect onze verschillende tutorials:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Dagelijks gebruik



### Interface hoofd



Het beginscherm toont je Lightning-balans, met het menu linksboven dat toegang geeft tot de volgende secties: Kanalen, Routing, Ondertekenen/Verifiëren, Knooppunten, Contacten, Instellingen, Back-up. Het klokpictogram (rechtsboven) opent de transactiegeschiedenis. Met de knoppen "Verzenden" en "Ontvangen" onderaan kun je satoshis verzenden en ontvangen.



![BitBanana](assets/fr/05.webp)



### Bliksem en on-chain betalingen



![BitBanana](assets/fr/10.webp)



**Een betaling verzenden:** Druk op de knop "Verzenden" in het beginscherm. In het betalingsscherm (links) kun je een adres of betalingsgegevens plakken in het veld "Address of betalingsgegevens", met rechtsboven een QR-scanner om codes te scannen. Je kunt ook een contact selecteren dat is opgeslagen in het gedeelte Contacten, zodat je niet elke keer hoeft te scannen.



BitBanana herkent op intelligente wijze alle betalingsformaten: klassieke Lightning-facturen (tekenreeksen beginnend met `lnbc`), Lightning Address (e-mailformaat zoals `utilisateur@domaine.com`), LNURL-pay codes voor dynamische betalingen, LNURL-withdraw voor het opnemen van geld, en zelfs Keysend betalingen direct naar een Lightning publieke sleutel zonder voorafgaande factuur. De applicatie voert automatisch de nodige LNURL-resoluties uit op de achtergrond.



Zodra de factuur is geladen, toont BitBanana alle details: het exacte bedrag, de geschatte routeringskosten, de omschrijving van de betaling (indien aangeleverd door de ontvanger) en de vervaldatum van de factuur. Na bevestiging wordt de betaling gerouteerd via uw Lightning-kanalen. U kunt de afgelegde route hop voor hop en de daadwerkelijk betaalde kosten bekijken in de transactiedetails.



**Betaling ontvangen:** Druk op de knop "Ontvangen". Met een keuzeschakelaar (rechterscherm) kun je kiezen tussen Lightning (onmiddellijke betaling via je kanalen) en On-Chain. Voor een Lightning-ontvangst voer je het gewenste bedrag in satoshis in (of laat je op 0 staan om een factuur te maken zonder vast bedrag dat de betaler moet invullen), en voeg je een optionele omschrijving toe die op de factuur moet komen te staan. BitBanana genereert direct een Lightning-factuur met QR-code om te scannen. U kunt de factuur ook als tekst kopiëren en per e-mail versturen. Zodra de betaling is ontvangen, krijgt u een pushmelding en verschijnt de transactie onmiddellijk in de geschiedenis met alle details.



### Kanalen en routing



![BitBanana](assets/fr/06.webp)



De "Kanalen" sectie toont je zend/ontvang mogelijkheden en toont je kanalen met unieke avatars. Elk kanaal toont zijn liquiditeit opgesplitst in lokaal en extern saldo. Raak een kanaal aan voor volledige details en acties (sluiten, routeringskosten wijzigen). De drie stippen rechtsboven geven toegang tot de optie "Herbalanceren" om de liquiditeit van je kanalen opnieuw in balans te brengen. De "+" knop opent een nieuw kanaal.



Het Routing-gedeelte (centrale scherm) toont doorstuurinkomsten per periode (1D, 1W, 1M, 3M, 6M, 1Y) met gedetailleerde doorstuurgeschiedenis om je strategie te optimaliseren.



Met Ondertekenen/Verifiëren (rechterscherm) kun je berichten cryptografisch ondertekenen/verifiëren om knooppuntcontrole aan te tonen.



### Multi-knooppunten en parameters



![BitBanana](assets/fr/07.webp)



**Manage Nodes**: geeft een overzicht van je knooppunten, met knoppen om handmatig toe te voegen, QR te scannen of tussen knooppunten te schakelen. Je kunt met name verschillende soorten verbindingen instellen met hetzelfde knooppunt: LAN, VPN of Tor.



**Beheer Contacten**: slaat je Lightning-contacten op voor snelle betalingen.



**Instellingen**: valuta, taal, avatars aanpassen. Beveiliging en privacy: App Lock (PIN/biometrie), Verberg saldo (stealth-modus), Tor (IP-anonimisering). Configuratie van price oracles, block explorers, custom fee estimators.



## Voordelen en beperkingen



**Highlights:**




- Totale mobiliteit: bedien uw Lightning-knooppunt overal vandaan
- Volledige functionaliteit: betalingen (LNURL, Lightning Address, BOLT 12), kanaalbeheer, muntenbeheer, wachttorens, meerdere knooppunten
- Beveiliging: PIN/biometrie, stealth-modus, nood-PIN, Tor, schermopname blokkeren
- Gratis, open bron (MIT), geen commissies, geen gegevensverzameling



**Beperkingen:**




- Vereist een actief Lightning-knooppunt (of LNbits in bewaarmodus)
- Geen iOS-versie gepland
- Beveiligen van toegang tot de telefoon is cruciaal (macaroon admin = volledige toegang tot het knooppunt)



## Beste praktijken



**Veiligheid:**




- Activeer PIN/biometrische vergrendeling (voorkomt onbevoegde toegang tot knooppunt)
- Een nood-PIN instellen (verwijdert gevoelige gegevens in geval van nood)
- Deel nooit uw login URI of macaron
- Stealth-modus in vijandige omgevingen



**Inloggen:**




- VPN mesh (Tailscale, ZeroTier): beste compromis tussen snelheid en beveiliging
- Tor: maximale vertrouwelijkheid, hogere latentie
- Clearnet: vermijden tenzij noodzakelijk (IP blootstelling, open poorten)



### Back-up en herstel



Tot slot is er het menu "Back-up", waarmee je je configuraties kunt opslaan voor telefoonmigratie of herinstallatie.



![BitBanana](assets/fr/08.webp)



**Belangrijk:** De backup bevat GEEN seed of kanaalbackups (die op het knooppunt moeten worden gemaakt). Het bevat: knooppuntconfiguraties (adressen, certificaten, macarons), labels, contacten, parameters. Met de knop Restore kun je een bestaande back-up importeren. Bevestiging vereist voor het opslaan.



![BitBanana](assets/fr/09.webp)



Voer een coderingswachtwoord in (rechter scherm). Het systeem opent de bestandskeuzeknop (linkerscherm) om `BitBananaBackup_2025-XX-XX.dat` op te slaan. Bevestiging "Backup gemaakt".



**Veiligheid:** Sla de back-up versleuteld op (persoonlijke cloud, USB, NAS). Deel nooit bestanden of wachtwoorden. Test het herstel regelmatig. De back-up herstelt verbindingen, geen fondsen.



## BitBanana vs Zeus: Wat is het verschil?



Als je mobiele apps onderzoekt voor het beheren van een Lightning-knooppunt, kom je waarschijnlijk Zeus tegen, een populair alternatief voor BitBanana. In tegenstelling tot BitBanana, dat zich uitsluitend richt op het op afstand beheren van een bestaand knooppunt, biedt Zeus een uitgebreidere aanpak en twee manieren van werken: een Lightning-knooppunt dat direct is ingebed in de applicatie (ingebedde modus met geïntegreerde LND) en verbinding op afstand met een extern knooppunt, net als BitBanana.



Deze dubbele functionaliteit maakt Zeus bijzonder aantrekkelijk voor beginners die met Lightning willen experimenteren zonder enige voorafgaande infrastructuur. Embedded mode maakt het mogelijk om direct te starten met een compleet mobiel knooppunt, terwijl gevorderde gebruikers kunnen overschakelen naar verbinding op afstand zodra hun persoonlijke knooppunt is geconfigureerd. Zeus ondersteunt ook LND en Core Lightning voor verbinding op afstand, zoals BitBanana.



Een ander groot voordeel van Zeus is de platformonafhankelijke beschikbaarheid (iOS en Android), terwijl BitBanana uitsluitend Android-gebaseerd blijft. Zeus bevat ook de LSP-infrastructuur van Olympus om de ontvangst van Lightning-betalingen via just-in-time-kanalen te vergemakkelijken, een Point-of-Sale-systeem voor handelaren en geïntegreerde swapfunctionaliteit om de liquiditeit te beheren.



BitBanana behoudt echter zijn specifieke sterke punten: een eenvoudigere, meer gestroomlijnde interface, een betere gebruikerservaring (UX) dankzij de exclusieve focus op afstandsbediening en een educatieve aanpak met contextuele uitleg. Zeus biedt meer functionaliteit, maar ten koste van een complexere interface. De toepassing blijft vooral geschikt voor gebruikers die een knooppunt uitsluitend op afstand willen bedienen, zonder bewaarfuncties.



Bekijk de volgende tutorials om meer te weten te komen over Zeus:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Conclusie



BitBanana verandert uw Android smartphone in een compleet Lightning dashboard en biedt ongekende mobiliteit voor node operators. De applicatie biedt alle functionaliteiten: betalingen (alle formaten), kanaalbeheer, muntcontrole, wachttorens, multi-node, met verbeterde beveiliging (PIN/biometrie, Tor, Emergency PIN).



BitBanana is volledig soeverein, verzamelt geen gegevens en compromitteert noch de vertrouwelijkheid noch de controle van uw geld. De open broncode (MIT) garandeert transparantie.



## Bronnen



### Officiële documentatie




- [BitBanana website](https://bitbanana.app)
- [Volledige documentatie](https://docs.bitbanana.app)
- [GitHub broncode](https://github.com/michaelWuensch/BitBanana)



### Installatie




- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold] (https://f-droid.org/packages/app.michaelwuensch.bitbanana)