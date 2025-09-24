---
name: Umbrel
description: Umbrel ontdekken en installeren - Uw Bitcoin knooppunt en thuisserver
---

![cover](assets/cover.webp)


![video](https://youtu.be/qFfhr4sApso)


## Inleiding



### Wat is een Bitcoin knooppunt?



Een Bitcoin knooppunt is een computer die deelneemt aan het Bitcoin netwerk door Bitcoin core software of een alternatieve client te draaien. Zijn rol is essentieel voor de werking en de veiligheid van het netwerk:





- **Blockchain opslag**: Behoudt een volledige, actuele kopie van de Blockchain Bitcoin
- **Transactieverificatie**: valideert elke transactie en elk blok volgens de protocolregels
- **Informatieverspreiding**: Deelt nieuwe transacties en blokken met andere nodes
- **Consensusvorming**: Draagt bij aan de toepassing van netwerkregels



Het runnen van je eigen Bitcoin node is een cruciale stap op weg naar financiële soevereiniteit en biedt verschillende belangrijke voordelen:





- **Vertrouwelijkheid**: Deel uw transacties zonder uw informatie aan derden te onthullen
- **Weerstand tegen censuur**: Niemand kan je tegenhouden om Bitcoin te gebruiken
- **Onafhankelijke verificatie**: Je hoeft niet te vertrouwen op andermans nodes om je transacties te verifiëren
- **Consensusvorming**: Bijdragen aan de toepassing van Bitcoin netwerkregels
- **Netwerkondersteuning**: Actief deelnemen aan netwerkdistributie en decentralisatie



### Umbrel: Een eenvoudige oplossing voor een Bitcoin knooppunt



Umbrel is een open source besturingssysteem dat de installatie en het beheer van een Bitcoin node vereenvoudigt. Het verandert je computer ook in een persoonlijke en privé thuisserver, waardoor het hosten van :





- Een compleet Bitcoin knooppunt
- Bitcoin essentiële toepassingen (Electrs, Mempool.ruimte)
- Andere persoonlijke diensten (cloudopslag, streaming, VPN, enz.)



Met de elegante en intuïtieve Interface gebruiker maakt Umbrel self-hosted diensten toegankelijk voor iedereen, terwijl je de volledige controle over je gegevens behoudt.



## Opties voor installatie van de paraplu



Umbrel biedt twee manieren om hun oplossing te gebruiken: een kant-en-klare optie (Umbrel Home) en een gratis open source versie (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: De kant-en-klare oplossing



Umbrel Home is een vooraf geconfigureerde homeserver, speciaal ontworpen voor een optimale ervaring. Deze alles-in-één hardwareoplossing bevat:



**Hardwarefuncties**




- Krachtige processor geoptimaliseerd voor zelf hosten
- Vooraf geïnstalleerde SSD-opslag met hoge snelheid
- Stil koelsysteem
- Compact, elegant ontwerp
- Geïntegreerde USB- en ethernetpoorten



**Exclusieve voordelen**




- Plug-and-play-installatie: aansluiten en klaar
- Premium ondersteuning met speciale assistentie
- Gegarandeerde automatische updates
- Geïntegreerde migratiewizard
- Volledige hardwaregarantie
- Volledige ondersteuning voor alle functionaliteiten



**Prijs**: €399 (prijs kan variëren afhankelijk van het seizoen)



### UmbrelOS: de open source versie



UmbrelOS is de gratis, open source versie van het Umbrel besturingssysteem. Met deze flexibele oplossing kun je je eigen hardware gebruiken en toch profiteren van de essentiële functies van Umbrel.



**Voordelen**




- Helemaal gratis
- Open, controleerbare broncode
- Keuzevrijheid
- Geavanceerde aanpassingsopties



**Ondersteunde platforms**




- Raspberry Pi 5: een populaire en betaalbare oplossing
- X86-systemen: Voor standaard pc's of servers
- Virtuele machine: Voor testen of gebruik op bestaande infrastructuur



**Beperkingen**




- Alleen communautaire steun
- Sommige geavanceerde functies zijn voorbehouden aan Umbrel Home
- Meer technische initiële configuratie
- Prestaties zijn afhankelijk van geselecteerde hardware



Deze versie is ideaal voor :




- Technische gebruikers
- Degenen die al compatibele apparatuur bezitten
- Mensen die willen leren en experimenteren
- Ontwikkelaars die willen bijdragen aan het project



Officiële installatielinks :




- [Installatie op Raspberry Pi 5](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Installatie op x86-systemen (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Installatie virtuele machine](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



In deze tutorial concentreren we ons op het installeren van UmbrelOS op een Raspberry Pi 5, maar de basisprincipes blijven vergelijkbaar voor andere platformen.



## Umbrel OS installeren op Raspberry Pi 5



### Vereiste onderdelen



Voor deze installatie heb je nodig :





- Raspberry Pi 5 (4 GB of 8 GB RAM)
- Een officiële Raspberry Pi voeding Supply (cruciaal voor stabiliteit!)
- MicroSD-kaart (minimaal 32 GB)
- Een microSD-kaartlezer
- Een externe SSD voor gegevensopslag
- Ethernetkabel
- Een USB-kabel om de SSD aan te sluiten



### Installatiestappen



**Download UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Bezoek de [officiële website] (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Download de nieuwste versie van UmbrelOS voor Raspberry Pi 5



**Balena Etcher** installatie



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Download en installeer [Balena Etcher] (https://www.balena.io/etcher/) op uw computer



**De microSD-kaart voorbereiden**



![Insertion carte microSD](assets/fr/03.webp)




- Plaats uw microSD-kaart in de kaartlezer van uw computer



**Beelden knipperen**



![Flashage UmbrelOS](assets/fr/04.webp)




- Lancering Balena Etcher
- Selecteer het gedownloade UmbrelOS-image
- Kies uw microSD-kaart als bestemming
- Klik op "Flash!" en wacht tot het proces is voltooid
- De kaart veilig uitwerpen



**Installatie microSD-kaart**



![Installation microSD](assets/fr/05.webp)




- Plaats de microSD-kaart in je Raspberry Pi 5



**Perifere aansluiting**



![Connexion périphériques](assets/fr/06.webp)




- Sluit de externe SSD aan op een beschikbare USB-poort
- Sluit de Ethernet-kabel aan tussen de Pi en je router



**Aanzetten**



![Démarrage du Pi](assets/fr/07.webp)




- Sluit de officiële Raspberry Pi-voeding Supply aan
- Wacht een paar minuten tot het systeem is opgestart



**Eerste toegang**



![Accès interface web](assets/fr/08.webp)




- Open uw browser op een apparaat dat is aangesloten op hetzelfde netwerk
- Ga naar de Interface website van Umbrel op: http://umbrel.local



![Page d'accueil Umbrel](assets/fr/09.webp)



Als `umbrel.local` niet werkt, moet je het IP Address van je Raspberry Pi op je lokale netwerk vinden. Je kunt :




- Raadpleeg de Interface van uw router
- Een netwerkscanner zoals nmap gebruiken
- Gebruik het `arp -a` commando in de terminal van uw computer



## Eerste stap op Umbrel



Zodra je Umbrel is opgestart en toegankelijk is via je browser, volg je deze stappen om aan de slag te gaan:



### Eerste configuratie



**Maak je account aan**



![Création compte](assets/fr/10.webp)




- Kies een gebruikersnaam
- Stel een veilig wachtwoord in
- U hebt deze gegevens nodig om toegang te krijgen tot uw Umbrel



**Accountbevestiging**



![Confirmation compte](assets/fr/11.webp)




- Klik op "Volgende" om naar je dashboard te gaan



**Ontdekking van de Interface**



![Interface Umbrel](assets/fr/12.webp)




- Toegang tot de Umbrel App Store
- Ontdek de vele beschikbare toepassingen
- Laten we beginnen met het installeren van de essentiële toepassingen voor Bitcoin



### Bitcoin toepassingen installeren



**Bitcoin knooppunt**



![Bitcoin Node](assets/fr/13.webp)




- Eerste toepassing om te installeren
- De volledige Blockchain Bitcoin downloaden en controleren



**Electrs**



![Installation Electrs](assets/fr/14.webp)




- Electrum server voor het verbinden van Bitcoin wallets
- Synchroniseert met uw Bitcoin knooppunt



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Interface scherm voor Blockchain
- Volgt transacties en blokken in realtime



## Een transactie volgen met Mempool.space



Mempool.space is een open-source Blockchain verkenner die real-time visualisatie van het Bitcoin netwerk biedt. Het laat je transacties volgen en begrijpen hoe transacties zich voortplanten op het netwerk.



### Mempool en bevestigingen begrijpen



De "Mempool" (geheugenpool) is als een virtuele wachtkamer waar alle onbevestigde Bitcoin transacties worden opgeslagen voordat ze in een blok worden opgenomen. Zo wordt een transactie verwerkt:



1. **Broadcast**: Wanneer je een transactie verstuurt, wordt deze eerst uitgezonden op het Bitcoin netwerk


2. **Wachtend in Mempool**: Wachtend om geselecteerd te worden door een Miner op basis van kosten


3. **Eerste bevestiging**: Een minderjarige neemt het op in een blok (1e bevestiging)


4. **Extra bevestigingen**: Elk nieuw blok dat wordt gedolven na het blok dat uw transactie bevat, voegt een bevestiging toe



Het aanbevolen aantal bevestigingen hangt af van de hoeveelheid :




- Voor kleine hoeveelheden: 1-2 bevestigingen kunnen voldoende zijn
- Voor grote bedragen: 6 bevestigingen worden over het algemeen als zeer veilig beschouwd



### Verken Interface vanuit Mempool.space



1. **De startpagina** geeft je een overzicht van het Bitcoin netwerk:




   - Recent gedolven blokken
   - Kostenramingen voor verschillende prioriteiten
   - De huidige staat van Mempool



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Zoek naar een transactie**: Om een specifieke transactie te volgen, plakt u de identificatiecode (txid) in de zoekbalk boven aan de pagina.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Analyseer transactiegegevens



Zodra uw transactie is gevonden, presenteert Mempool.space u een complete analyse:



1. **Essentiële informatie** :




   - Status (bevestigd of niet)
   - Betaalde uitgaven (in Sats/vB)
   - Geschatte bevestigingstijd



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Transactiestructuur** :




   - Visuele weergave van inputs en outputs
   - Gedetailleerde lijst van betrokken adressen
   - Overgedragen bedragen



3. **Technische gegevens** :




   - Gewicht transactie
   - Virtueel formaat
   - Formaat en gebruikte versie
   - Andere specifieke metagegevens



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Voordelen van het gebruik van Mempool.space op Umbrel



1. **Vertrouwelijkheid**: Uw verzoeken gaan via uw eigen knooppunt


2. **Onafhankelijkheid**: Je hoeft niet afhankelijk te zijn van een service van derden


3. **Betrouwbaarheid**: Toegang tot gegevens zelfs wanneer publieke browsers down zijn



Met deze applicatie kunt u uw transacties efficiënt controleren, begrijpen hoe kosten de bevestigingssnelheid beïnvloeden en beter begrijpen hoe het Bitcoin netwerk werkt.



## Een Wallet Bitcoin op uw knooppunt aansluiten



### Electrs configuratie



**Lokale verbinding**



![Connexion locale](assets/fr/18.webp)




- Voor gebruik op uw lokale netwerk
- Sneller en gemakkelijker op te zetten



**Remote verbinding via Tor**



![Connexion Tor](assets/fr/19.webp)




- Om overal toegang te krijgen tot je knooppunt
- Veiliger en meer privé



### Verbinding met Sparrow wallet



**Toegang tot parameters**



![Paramètres Sparrow](assets/fr/20.webp)




- Open Sparrow wallet
- Ga naar Voorkeuren > Server
- Klik op "Bestaande verbinding wijzigen"



**Kies type verbinding**



Sparrow biedt drie verbindingsmodi:



***Publieke server***




- Verbinding met openbare servers (bijv. blockstream.info, Mempool.space)
- Eenvoudig maar minder privé



***Bitcoin core***




- Directe verbinding met een Bitcoin-knooppunt
- Privé maar langzamer



***Privé Electrum***




- Maak verbinding met uw Electrs-server
- Combineert privacy en prestaties



**Electrs** configuratie



Kies je verbindingstype aan de hand van de informatie die wordt weergegeven in de Electrs-toepassing die we eerder hebben gezien:



Laat in beide gevallen de opties "SSL gebruiken" en "Proxy gebruiken" uitgevinkt.



**Lokale verbinding**


Host: umbrel.local


Poortnummer: 50001



**Verbinding op afstand (Tor)**


Gastheer : [uw-Address ui]


Poortnummer: 50001



De Tor-verbinding is nodig als je toegang wilt tot je node buiten je lokale netwerk.



![Configuration connexion](assets/fr/21.webp)


Voor meer informatie over Sparrow wallet software hebben we een uitgebreide handleiding:


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Conclusie



Uw Umbrel is nu klaar voor gebruik. U neemt actief deel aan het Bitcoin netwerk en behoudt de volledige controle over uw gegevens. Voel je vrij om de vele andere toepassingen te verkennen die beschikbaar zijn in de Umbrel App Store om de mogelijkheden van je homeserver uit te breiden.



## Nuttige bronnen



### Officiële documentatie




- [Officiële website van Umbrel](https://umbrel.com)
- [Umbrel documentatie](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Bitcoin toepassingen




- [Bitcoin core] (https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool] (https://Mempool.space)
- [Sparrow wallet] (https://sparrowwallet.com)



### Gemeenschap




- [Forum Paraplu](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Paraplu](https://twitter.com/umbrel)