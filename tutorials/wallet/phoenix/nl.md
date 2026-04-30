---
name: Phoenix
description: Phoenix wallet installeren en gebruiken
---
![cover](assets/cover.webp)


![video](https://youtu.be/TpwnoPUyumA)


Phoenix is een self-custodial Lightning-wallet en node ontwikkeld door ACINQ, een Frans bedrijf gespecialiseerd in Lightning-gebaseerde software-oplossingen. In tegenstelling tot custodial Lightning-wallets zoals Wallet of Satoshi, waar bitcoins worden bewaard door een derde partij, stelt Phoenix gebruikers in staat om de volledige controle over hun privésleutels te behouden.


Phoenix werkt als een echte Lightning-node in je telefoon en opent automatisch een kanaal met ACINQ's Lightning-node. De applicatie is gebaseerd op Lightning-KMP, een cross-platform implementatie van het Lightning Network in Kotlin, geoptimaliseerd voor mobiele wallets. In tegenstelling tot andere Lightning-node-oplossingen vereenvoudigt Phoenix het beheer aanzienlijk. De gebruiker hoeft niet te zorgen voor het openen en sluiten van kanalen, een Bitcoin-node te draaien of liquiditeit op het Lightning Network te beheren. Phoenix zorgt voor al deze technische handelingen op de achtergrond.


Deze toepassing combineert het gebruiksgemak en gemak van mobiele Lightning wallets met de veiligheid en soevereiniteit van een echt persoonlijke Lightning-node. Phoenix maakt het mogelijk om het Lightning Network veilig, efficiënt en autonoom te gebruiken, terwijl je geniet van een vloeiende, intuïtieve gebruikerservaring.


Daar staan bepaalde kosten tegenover:




- Versturen via Lightning kost 0,4% van het bedrag plus 4 sats ;
- Als er contant geld nodig is om via Lightning te ontvangen, wordt 1% van het bedrag in rekening gebracht;
- Elk kanaal kost 1000 sats om te openen.


Naar mijn mening is Phoenix een uitstekende tussenoplossing tussen custodial Lightning-wallets en het handmatig beheren van een Lightning-node. Deze toepassing is even geschikt voor beginners als voor gevorderde gebruikers die zich liever niet bezighouden met de details van het beheer van hun eigen LND of Core Lightning. Laten we eens kijken hoe we het kunnen gebruiken!


![Image](assets/fr/01.webp)


## De toepassing installeren


Installeer Phoenix via de app store van je telefoon:




- In de [Google Play Store](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.Mainnet);
- In de [App Store](https://apps.apple.com/fr/app/phoenix-Wallet/id1544097028?l=en-GB).


![Image](assets/fr/02.webp)


Je kunt de applicatie ook installeren [met het apk-bestand op hun GitHub repository](https://github.com/ACINQ/phoenix/releases).


![Image](assets/fr/03.webp)


## Wallet aanmaken


Zodra de toepassing is gestart, klik je op de knop "*Volgende*" om de presentatie over te slaan en vervolgens op "*Start*".


![Image](assets/fr/04.webp)


Selecteer "*Maak een nieuwe wallet*".


![Image](assets/fr/05.webp)


En dat is het, je Lightning-wallet en node zijn nu aangemaakt.


![Image](assets/fr/06.webp)


## Mnemonische zin (seed phrase) opslaan


Voordat we beginnen, moeten we onze mnemonische zin van 12 woorden opslaan. Deze zin geeft volledige en onbeperkte toegang tot al je bitcoins. Iedereen die in het bezit is van deze zin kan je tegoeden stelen, zelfs zonder fysieke toegang tot je telefoon.


De 12-woorden zin herstelt de toegang tot je bitcoins in geval van verlies, diefstal of een defecte telefoon. Het is daarom erg belangrijk om het zorgvuldig op te slaan en op een veilige plek te bewaren.


Je kunt het op papier schrijven of, voor extra veiligheid, op roestvrij staal graveren om het te beschermen tegen brand, overstroming of instorting. De keuze van het medium voor je mnemonische zin hangt af van je beveiligingsstrategie. Als je Phoenix gebruikt als een portemonnee voor uitgaven met gematigde bedragen, zou papier voldoende moeten zijn.


Voor meer informatie over de juiste manier om je mnemonische zin op te slaan en te beheren, raad ik je aan deze andere tutorial te volgen, vooral als je een beginner bent:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Klik op het bericht bovenaan het scherm "*Sla je Wallet op...*".


![Image](assets/fr/07.webp)


Klik dan op "*Bewaar mijn wallet*".


![Image](assets/fr/08.webp)


Klik dan op "*Bekijk mijn sleutel*" en sla je mnemonische zin op op een fysieke drager.


![Image](assets/fr/09.webp)


Controleer de twee selectievakjes onderaan het scherm om te bevestigen dat de back-up met succes is voltooid.


![Image](assets/fr/10.webp)


## Toepassing instellen


Voordat je je eerste transacties maakt, kun je de instellingen aanpassen door op het tandwielpictogram linksonder op het scherm te klikken.


![Image](assets/fr/11.webp)


In het menu "*Display*" kun je het thema van de applicatie kiezen, de denominatie die gebruikt wordt voor bitcoin en je lokale fiatvaluta.


![Image](assets/fr/12.webp)


In "*Betalingsopties*" vind je verschillende geavanceerde instellingen voor Lightning-betalingen. Je kunt de standaardinstellingen behouden.


![Image](assets/fr/13.webp)


In "*Channel management*" stel je de maximale vergoeding in die je bereid bent te betalen voor het openen van een Lightning-kanaal.


![Image](assets/fr/14.webp)


In het menu "*App Access*" raad ik je sterk aan om een authenticatiesysteem te activeren om de toegang tot de applicatie op je telefoon te beveiligen. Dit voorkomt dat iemand met toegang tot je niet-vergrendelde telefoon Phoenix kan openen en je bitcoins kan stelen.


![Image](assets/fr/15.webp)


In het menu "*Electrum server*" kun je, als je een Electrs-server hebt, deze verbinden om je transacties uit te zenden.


![Image](assets/fr/16.webp)


Om de vertrouwelijkheid van je verbindingen te verbeteren, kun je verbindingen via Tor inschakelen in het menu "*Tor*". Hoewel het gebruik van Tor je betalingen enigszins kan vertragen en vereist dat de Phoenix-toepassing op de voorgrond is geopend tijdens het ontvangen, verhoogt het je privacy aanzienlijk.


![Image](assets/fr/17.webp)


## On-chain bitcoins ontvangen 


Bij het eerste gebruik heb je de optie om je Phoenix-wallet te laden met nn-chain fondsen. Je kunt deze eerste storting ook direct vanuit Lightning doen (zie volgende sectie), maar in beide gevallen betaal je extra kosten voor het openen van je eerste kanaal.


Klik op de knop "*Receive*".


![Image](assets/fr/18.webp)


Veeg de QR-code naar links om een ontvangstadres voor Bitcoin te onthullen. Stuur het bedrag dat je in Phoenix wilt storten naar dat adres.


![Image](assets/fr/19.webp)


Het ontvangen on-chain bedrag verschijnt in je wallet-saldo eerst als 'pending'. Het duurt 3 bevestigingen voordat het geld beschikbaar is voor gebruik.


![Image](assets/fr/20.webp)


Zodra het geld is ontvangen, opent Phoenix automatisch een Lightning-kanaal voor je. Je kunt nu bitcoins verzenden en ontvangen via het Lightning Network.


![Image](assets/fr/21.webp)


## Bitcoins ontvangen via Lightning


Om sats via het Lightning Network te ontvangen, klik je op de knop "*Receive*".


![Image](assets/fr/22.webp)


Phoenix genereert een Lightning-invoice. Je kunt het scannen of opsturen naar de persoon die sats aan jou wil overdragen.


![Image](assets/fr/23.webp)


Door op de "*Edit*" knop te klikken, kun je een omschrijving toevoegen die zichtbaar zal zijn voor de betaler op de invoice, en een specifiek bedrag definiëren dat de betaler moet overmaken.


![Image](assets/fr/24.webp)


De bovengenoemde klassieke facturen kunnen slechts één keer worden gebruikt. Voor een herbruikbare betalingsoptie kun je je herbruikbare QR-code gebruiken, wat een BOLT12-aanbieding is.


![Image](assets/fr/25.webp)


Zodra de invoice of BOLT12-aanbieding is vereffend, verschijnt de transactie op je Lightning-wallet.


![Image](assets/fr/26.webp)


## Bitcoins versturen via Lightning


Nu je sats op Phoenix hebt, ben je klaar om betalingen via het Lightning Network te doen. Klik eerst op de knop "*Send*".


![Image](assets/fr/27.webp)


Je hebt verschillende opties tot je beschikking. Door op "*Scan QR code*" te klikken, kun je een Lightning-invoice, een BOLT12-aanbieding of zelfs een on-chain ontvangstadres scannen om te betalen.


![Image](assets/fr/28.webp)


Je kunt deze informatie ook handmatig invoeren via het toetsenbord in het veld bovenaan het scherm, of een Lightning-adres (BOLT12 of LNURL) invoeren. Je kunt de informatie ook direct plakken met de knop "*Paste*".


![Image](assets/fr/29.webp)


In dit voorbeeld heb ik een invoice gescand voor 10.000 sats. Om de betaling uit te voeren, klik je op "*Pay*".


![Image](assets/fr/30.webp)


De transactie is voltooid.


![Image](assets/fr/31.webp)


Gefeliciteerd, je weet nu hoe je Phoenix moet configureren en gebruiken. Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een groene duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Bedankt voor het delen!


Als je nog een stapje verder wilt gaan, bekijk dan deze tutorial over Alby Hub, een andere innovatieve en gebruiksvriendelijke oplossing voor het lanceren van je eigen Lightning-node:


https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

En om meer te weten te komen over de technische werking van de Lightning Network, kun je Fanis Michalakis' uitstekende gratis training over Plan ₿ Academy vinden:


https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
