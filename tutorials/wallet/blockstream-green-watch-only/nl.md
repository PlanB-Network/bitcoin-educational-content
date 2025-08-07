---
name: Blockstream Green - Alleen kijken
description: Watch-only wallet configuratie
---
![cover](assets/cover.webp)


In deze tutorial ontdek je hoe je eenvoudig een "alleen kijken" Wallet op mobiel instelt met behulp van de Blockstream Green toepassing.


## Wat is een Watch-only wallet?


Een read-only Wallet, of "Watch-only wallet", is een type software ontworpen om de gebruiker in staat te stellen transacties te observeren die geassocieerd zijn met één of meer specifieke Bitcoin publieke sleutels, zonder toegang te hebben tot de corresponderende private sleutels.


Dit type applicatie slaat alleen de gegevens op die nodig zijn om een Bitcoin Wallet te bewaken, met name om het saldo en de transactiegeschiedenis te bekijken, maar het heeft geen toegang tot privésleutels. Hierdoor is het onmogelijk om Bitcoins uit te geven die de Wallet bezit op de watch-only applicatie.


![GREEN-WATCH-ONLY](assets/fr/01.webp)


Watch-only wordt meestal in combinatie met een Hardware Wallet gebruikt. Dit maakt het mogelijk om de private sleutels van de Wallet veilig op te slaan, op hardware die niet verbonden is met het Internet en een zeer klein aanvalsoppervlak heeft, waardoor de private sleutels geïsoleerd worden van mogelijk kwetsbare omgevingen. De watch-only toepassing slaat daarentegen uitsluitend de uitgebreide publieke sleutel (`xpub`, `zpub`, etc.) van de Bitcoin Wallet op. Deze oudersleutel kan niet worden gebruikt om de bijbehorende privésleutels te vinden en kan daarom niet worden gebruikt om Bitcoins uit te geven. Het maakt het echter wel mogelijk om publieke sleutels van kinderen en ontvangstadressen af te leiden. Dankzij de kennis van de Hardware Wallet over veilige Wallet adressen, kan de watch-only toepassing deze transacties op het Bitcoin netwerk volgen, zodat de gebruiker zijn saldo en generate nieuwe ontvangstadressen kan controleren, zonder telkens zijn Hardware Wallet te hoeven aansluiten.


In deze tutorial wil ik je kennis laten maken met een van de populairste mobiele Wallet oplossingen met alleen een horloge: **Blockstream Green**.


![GREEN-WATCH-ONLY](assets/fr/02.webp)


## Maak kennis met Blockstream Green


Blockstream Green is een softwaretoepassing die beschikbaar is op mobiel en desktop. Voorheen bekend als Green Address, werd dit Wallet een Blockstream-project na de overname in 2016.


Green is een zeer eenvoudig te gebruiken applicatie, waardoor het bijzonder geschikt is voor beginners. Het biedt een scala aan functies, zoals het beheer van Hot wallets, hardware wallets en Liquid Sidechain wallets.


In deze tutorial concentreren we ons alleen op het maken van een Watch-only wallet. Om andere toepassingen van Green te ontdekken, kun je onze andere tutorials raadplegen:


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

## De Blockstream Green toepassing installeren en configureren


De eerste stap is natuurlijk het downloaden van de Green applicatie. Ga naar je applicatiewinkel:



- [Voor Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN-WATCH-ONLY](assets/fr/03.webp)


Voor Android gebruikers kun je de applicatie ook installeren via het `.apk` bestand [beschikbaar op Blockstream's GitHub] (https://github.com/Blockstream/green_android/releases).


![GREEN-WATCH-ONLY](assets/fr/04.webp)


Start de applicatie en vink het vakje "Ik accepteer de voorwaarden...*" aan.


![GREEN-WATCH-ONLY](assets/fr/05.webp)


Wanneer je Green voor de eerste keer opent, verschijnt het beginscherm zonder een geconfigureerde Wallet. Later, als je wallets aanmaakt of importeert, verschijnen ze in deze Interface. Voordat je een Wallet aanmaakt, raad ik je aan de applicatie-instellingen aan te passen aan je behoeften. Klik op "Applicatie-instellingen".


![GREEN-WATCH-ONLY](assets/fr/06.webp)


De optie "*Geavanceerde privacy*", alleen beschikbaar op Android, verbetert de privacy door schermafbeeldingen uit te schakelen en voorvertoningen van applicaties te verbergen. De toegang tot applicaties wordt ook automatisch geblokkeerd zodra je telefoon wordt vergrendeld, waardoor het moeilijker wordt om je gegevens bloot te leggen.


![GREEN-WATCH-ONLY](assets/fr/07.webp)


Voor degenen die hun privacy willen verbeteren, biedt de applicatie de optie om je verkeer via Tor te routeren, een netwerk dat al je verbindingen versleutelt en je activiteiten moeilijk traceerbaar maakt. Hoewel deze optie de werking van de applicatie enigszins kan vertragen, is het zeer aan te raden om je privacy te beschermen, vooral als je niet je eigen complete node gebruikt.


![GREEN-WATCH-ONLY](assets/fr/08.webp)


Voor gebruikers die hun eigen complete node hebben, biedt Green Wallet de mogelijkheid om er verbinding mee te maken via een Electrum-server, waardoor totale controle over Bitcoin netwerkinformatie en de distributie van transacties gegarandeerd is.


![GREEN-WATCH-ONLY](assets/fr/09.webp)


Een andere alternatieve functie is de "*SPV Verification*" optie, waarmee je bepaalde Blockchain gegevens direct kunt verifiëren en dus de noodzaak om Blockstream's standaard knooppunt te vertrouwen kunt verminderen, hoewel deze methode niet alle garanties van een Full node biedt.


![GREEN-WATCH-ONLY](assets/fr/10.webp)


Zodra je deze instellingen naar wens hebt aangepast, klik je op de knop "*Opslaan*" en start je de toepassing opnieuw.


![GREEN-WATCH-ONLY](assets/fr/11.webp)


## Maak een Watch-only wallet op Blockstream Green


Je bent nu klaar om een Watch-only wallet aan te maken. Klik op de knop "*Get Started*".


![GREEN-WATCH-ONLY](assets/fr/12.webp)


Je kunt kiezen uit verschillende typen Wallet. Voor deze tutorial willen we een Watch-only wallet maken, dus klik op de bijbehorende knop.


![GREEN-WATCH-ONLY](assets/fr/13.webp)


Kies de optie "Enkele handtekening".


![GREEN-WATCH-ONLY](assets/fr/14.webp)


Selecteer dan "*Bitcoin*". Ik doe deze tutorial op een Testnet Wallet, maar de procedure blijft identiek op de Mainnet.


![GREEN-WATCH-ONLY](assets/fr/15.webp)


Er wordt gevraagd om ofwel een uitgebreide publieke sleutel (`xpub`, `zpub`, enz.) of een uitvoerscript Descriptor op te geven.


![GREEN-WATCH-ONLY](assets/fr/16.webp)


Daarom moet u deze informatie ophalen bij de Wallet die u via uw Watch-only wallet wilt volgen. De uitgebreide publieke sleutel is niet gevoelig voor beveiliging, omdat hij geen toegang geeft tot privésleutels, maar wel voor uw privacy, omdat hij al uw publieke sleutels en dus al uw Bitcoin-transacties onthult.


Stel dat je Sparrow wallet gebruikt om je Wallet op een Hardware Wallet te beheren, dan vind je deze informatie in de sectie "*Instellingen*". Het vinden van deze informatie hangt af van de Wallet managementsoftware die je gebruikt, maar meestal staat het in de instellingen.


![GREEN-WATCH-ONLY](assets/fr/17.webp)


Kopieer uw uitgebreide publieke sleutel en voer deze in de Green-toepassing in en klik vervolgens op "Verbinden".


![GREEN-WATCH-ONLY](assets/fr/18.webp)


Je kunt dan het saldo zien dat bij deze sleutel hoort, evenals de transactiegeschiedenis.


![GREEN-WATCH-ONLY](assets/fr/19.webp)


Door op "*Ontvangen*" te klikken, kun je generate een Address ontvangen om bitcoins op je Hardware Wallet te ontvangen. Ik raad je echter af om deze optie te gebruiken zonder eerst op het Hardware Wallet scherm te controleren of het de private key heeft die hoort bij de gegenereerde Address, voordat je het gebruikt om bitcoins te vergrendelen. Dit is een goede gewoonte.


![GREEN-WATCH-ONLY](assets/fr/20.webp)


Met de optie "*Balayer*" kunt u handmatig een privé sleutel invoeren om geld direct vanuit uw Green applicatie uit te geven. Behalve in zeer specifieke gevallen raad ik het gebruik van deze functie niet aan, omdat je dan je privésleutel op een telefoon moet invoeren, die veel kwetsbaarder is voor computeraanvallen dan je Hardware Wallet.


![GREEN-WATCH-ONLY](assets/fr/21.webp)


Nu weet je hoe je eenvoudig een Watch-only wallet op je smartphone kunt instellen! Het is een handig hulpmiddel om een Wallet op een Hardware Wallet te monitoren zonder hem telkens te moeten verbinden en ontgrendelen.


Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Ik raad je ook aan deze andere uitgebreide tutorial over de Blockstream Green toepassing te bekijken om een Hot Wallet in te stellen:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143