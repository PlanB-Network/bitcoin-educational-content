---
name: LNP2PBot
description: Complete gids voor LNP2PBot en P2P Bitcoin handel
---
![cover](assets/cover.webp)


## Inleiding


KYC-vrije peer-to-peer (P2P) uitwisselingen zijn essentieel voor het behoud van de privacy en financiële autonomie van gebruikers. Ze maken directe transacties tussen individuen mogelijk zonder de noodzaak voor identiteitsverificatie, wat cruciaal is voor diegenen die waarde hechten aan privacy. Voor een meer diepgaand begrip van de theoretische concepten, bekijk de BTC204 cursus:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Het kopen en verkopen van Bitcoin peer-to-peer (P2P) is een van de meest privé methoden om bitcoins te verkrijgen of te verkopen. LNP2PBot is een open source Telegram bot die P2P uitwisselingen op Lightning Network mogelijk maakt, waardoor snelle, goedkope, KYC-vrije transacties mogelijk zijn.


### Waarom Lnp2pbot gebruiken?




- Geen KYC vereist
- Snelle transacties op de Lightning Network
- Lage kosten
- Eenvoudig Interface via Telegram, een populaire berichtentoepassing die overal ter wereld toegankelijk is
- Geïntegreerd reputatiesysteem
- Automatische escrow voor veilig handelen
- Ondersteuning voor meerdere valuta
- Actieve en groeiende gemeenschap


### Vereisten


Om Lnp2pbot te gebruiken, heb je nodig :


1. Lightning Network Wallet (Breez, Phoenix of Blixt aanbevolen)


2. Telegram-toepassing geïnstalleerd (https://telegram.org/)


3. Een Telegram-account met een bepaalde gebruikersnaam


## Installatie en configuratie


### 1. Uw Lightning Wallet configureren


Begin met het installeren van een compatibele Lightning Wallet. Hier zijn onze gedetailleerde aanbevelingen:


**Aanbevolen portemonnees**




- [Breez](https://breez.technology)**:
  - Uitstekend voor beginners
  - Intuïtieve, moderne Interface
  - Non-custodial (je behoudt de controle over je geld)
  - Perfect compatibel met Lnp2pbot
  - Beschikbaar op iOS en Android


Hieronder staat de link naar de tutorial voor deze Wallet:


https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06


- [Phoenix](https://phoenix.acinq.co)** :
  - Eenvoudig en betrouwbaar
  - Automatische kanaalconfiguratie
  - Native ondersteuning voor BOLT11-facturen
  - Uitstekend voor alledaagse transacties
  - Beschikbaar op iOS en Android


Hieronder staat de link naar de tutorial voor deze Wallet:


https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


- [Blixt](https://blixtwallet.github.io)** :
  - Meer technisch maar zeer compleet
  - Geavanceerde configuratie-opties
  - Perfect voor ervaren gebruikers
  - Open bron
  - Beschikbaar op Android


Hieronder staat de link naar de tutorial voor deze Wallet:


https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

**Belangrijke opmerkingen over andere portefeuilles**


⚠️ **Belangrijk**: Voordat u Sats verkoopt, moet u ervoor zorgen dat uw Wallet "hold" facturen ondersteunt, die door de bot worden gebruikt als borgsysteem.




- Wallet of Satoshi**: Werkt goed voor het ontvangen van Sats, maar kan vertragingen hebben bij het bijwerken van het saldo als een verkoop wordt geannuleerd.
- Muun**: Niet aanbevolen omdat betalingen kunnen mislukken vanwege de limieten voor routeringskosten voor bots (maximaal 0,2%).
- Aqua**: Werkt om Sats te ontvangen, maar kan grote vertragingen hebben (tot 48 uur) voor saldo-updates in het geval van een annulering van een verkoop.


**Tip**: Kies voor de aanbevolen portemonnees (Breez, Phoenix of Blixt) voor een optimale ervaring.


⚠️ **Belangrijk**: Vergeet niet om je herstelzinnen op een veilige plaats op te slaan.


### 2. Aan de slag met Lnp2pbot


1. Klik op deze link om toegang te krijgen tot de bot: [@lnp2pBot](https://t.me/lnp2pbot)


2. Telegram wordt automatisch geopend


3. Klik op "Start" of stuur het commando "/start"


4. De bot zal je vragen om een gebruikersnaam aan te maken als je die nog niet hebt


5. De bot leidt je door de eerste configuratie


### 3. Word lid van de gemeenschap




- Word lid van het hoofdkanaal: [@p2plightning](https://t.me/p2plightning)
- Ondersteuning: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)


## Bitcoins kopen en verkopen


Er zijn twee belangrijke manieren om Exchange bitcoins op Lnp2pbot:


1. Bladeren door en reageren op bestaande aanbiedingen op de markt


2. Maak je eigen koop- of verkoopaanbod


In deze gids bekijken we in detail hoe :




- Bitcoins kopen van een bestaand aanbod
- Bitcoins verkopen door je eigen aanbieding te maken


### Hoe Bitcoins kopen


**1. Zoek en selecteer een aanbieding**


![Sélection d'une offre de vente](assets/fr/01.webp)


Blader door de aanbiedingen in [@p2plightning](https://t.me/p2plightning) en klik op de knop "Satoshis kopen" onder de advertentie waarin je geïnteresseerd bent.


**2. Bevestig aanbod en bedrag**


![Validation de l'offre](assets/fr/02.webp)


1. Terug naar botchat


2. Bevestig je keuze van aanbod


3. Voer het bedrag in fiatvaluta in dat je wilt kopen


4. De bot zal je vragen om een Lightning Invoice op te geven voor het bedrag in satoshis


**3. Neem contact op met de verkoper**


![Mise en relation](assets/fr/03.webp)


Zodra de Invoice is verzonden, brengt de bot je in contact met de verkoper.


**4. Communicatie met de verkoper**


![Chat privé](assets/fr/04.webp)


Klik op de bijnaam van de verkoper om een privéchatkanaal te openen waar je Exchange fiat-betalingsgegevens kunt invoeren.


**5. Bevestiging van betaling


![Confirmation du paiement](assets/fr/05.webp)


Nadat je de fiatbetaling hebt gedaan, gebruik je het `/fiatsent` commando in de botchat. Zodra de transactie is voltooid, kun je de verkoper beoordelen en wordt de transactie gesloten.


### Hoe Bitcoins verkopen


**1. Maak een verkoopaanbieding**


![Création d'une offre de vente](assets/fr/06.webp)


Om een verkoopaanbieding te maken, gebruik je gewoon de opdracht :


`/verkopen`


De bot zal je dan stap voor stap begeleiden:


1. Kies je valuta


2. Geef aan hoeveel satoshis je wilt verkopen


3. Voor de prijs heb je twee opties:




   - Stel een vaste prijs in voor de hoeveelheid satoshi's
   - Gebruik de marktprijs met de mogelijkheid om een premie toe te passen (positief of negatief)


tip**: Met de premie kun je je prijs aanpassen ten opzichte van de marktprijs. Een premie van -1% betekent bijvoorbeeld dat je voor 1% minder verkoopt dan de marktprijs.


**2. Bevestiging van bestelling**


![Confirmation de l'ordre de vente](assets/fr/07.webp)


Zodra de bestelling is aangemaakt, zie je een bevestiging met de optie om de bestelling te annuleren met de opdracht `/cancel`.


**3. Verkoop beheren**


![Prise de l'ordre par un acheteur](assets/fr/08.webp)




- Wanneer een koper op je bod reageert, ontvang je een melding met een QR-code en een Invoice om te betalen.
- Controleer het profiel en de reputatie van de koper.


![Mise en relation avec l'acheteur](assets/fr/09.webp)




- Klik op de bijnaam van de koper om een privédiscussiekanaal te openen.
- Geef de betalingsgegevens van fiat door aan de koper.
- Wacht op bevestiging van fiatbetaling van de koper.
- Controleer of de betaling op je account is ontvangen.


![Confirmation de la fin de l'ordre](assets/fr/10.webp)




- Bevestig de transactie met `/release` en rond de bestelling af. Je krijgt de mogelijkheid om de koper te beoordelen.


## Goede praktijken en veiligheid


### Veiligheidstips




- Begin met kleine hoeveelheden
- Controleer altijd de reputatie van gebruikers
- Gebruik alleen de voorgestelde betalingsmethoden
- Houd alle communicatie in botchat
- Deel nooit gevoelige informatie


### Reputatiesysteem




- Elke gebruiker heeft een reputatiescore
- Succesvolle transacties verhogen je score
- Kies gebruikers met een goede reputatie
- Rapporteer verdacht gedrag aan de moderators


### Geschillen oplossen


1. Blijf kalm en professioneel bij problemen


2. Gebruik het `/dispute` commando om een ticket te openen


3. Lever alle benodigde bewijzen


4. Wacht op een moderator


## Vergelijking met andere oplossingen


Lnp2pbot heeft verschillende voor- en nadelen ten opzichte van andere P2P Exchange oplossingen zoals Peach, Bisq, HodlHodl en Robosat:


### Voordelen van Lnp2pbot




- Geen KYC vereist** : In tegenstelling tot sommige platforms vereist Lnp2pbot geen identiteitsverificatie, waardoor de privacy van de gebruiker behouden blijft.
- Snelle transacties**: Dankzij de Lightning Network verlopen transacties bijna onmiddellijk.
- Lage kosten** : Transactiekosten zijn lager dan bij traditionele beurzen.
- Mobiele beschikbaarheid**: LNP2PBot is toegankelijk via Telegram, waardoor het gemakkelijk te gebruiken is op mobiele apparaten.
- Gebruiksvriendelijk** : Lnp2pbot's intuïtieve Interface maakt het makkelijk te gebruiken, zelfs voor minder ervaren gebruikers.


### Nadelen van Lnp2pbot




- Telegram-afhankelijkheid**: Het gebruik van Lnp2pbot vereist een Telegram-account, wat misschien niet voor alle gebruikers geschikt is.
- Minder liquiditeit**: In vergelijking met meer gevestigde platforms zoals Bisq kan de liquiditeit beperkter zijn.


Ter vergelijking, oplossingen zoals Bisq bieden een grotere liquiditeit en een desktop Interface, maar kunnen hogere kosten en langere transactietijden met zich meebrengen. HodlHodl en Robosat bieden ondertussen ook KYC-vrije handel, maar met verschillende kostenstructuren en interfaces.


## Nuttige bronnen




- Officiële website: https://lnp2pbot.com/
- Documentatie: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Ondersteuning: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)