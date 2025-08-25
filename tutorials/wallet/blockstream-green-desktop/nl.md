---
name: Blockstream Green - Desktop
description: Green Wallet op uw computer gebruiken
---
![cover](assets/cover.webp)


In deze tutorial onderzoeken we hoe je Blockstream Green software op je computer kunt gebruiken om een beveiligde Wallet op een Hardware Wallet te beheren. Wanneer je een Hardware Wallet gebruikt, is het essentieel om software op je computer te gebruiken om de Wallet te beheren. Deze beheersoftware heeft geen toegang tot privésleutels; het wordt alleen gebruikt om uw Wallet saldo te raadplegen, generate ontvangstadressen, en transacties te maken en te distribueren die door de Hardware Wallet ondertekend moeten worden. Green is slechts één van de vele beschikbare oplossingen voor het beheren van uw Bitcoin Hardware Wallet.


In 2024 is Blockstream Green alleen compatibel met Ledger Nano S (oude versie), Ledger Nano X, Trezor One, Trezor T en Blockstream Jade apparaten.


## Maak kennis met Blockstream Green


Blockstream Green is een softwaretoepassing die beschikbaar is op mobiel en desktop. Voorheen bekend als Green Address, werd deze Wallet een Blockstream-project na de overname in 2016.


Green is een zeer eenvoudig te gebruiken applicatie, waardoor het bijzonder geschikt is voor beginners. Het biedt verschillende functionaliteiten, zoals het beheer van Hot wallets, hardware wallets, maar ook wallets op de Liquid Sidechain. Je kunt het ook gebruiken om een Watch-only wallet op te zetten.


![GREEN-DESKTOP](assets/fr/01.webp)


In deze tutorial concentreren we ons alleen op het gebruik van de software op de computer. Om andere toepassingen van Green te ontdekken, kun je onze andere tutorials raadplegen:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

## Blockstream Green software installeren en configureren


Begin met het installeren van de Blockstream Green software op je computer. Ga naar [de officiële website](https://blockstream.com/Green/) en klik op de knop "*Download Nu*". Volg dan het installatieproces volgens jouw besturingssysteem.


![GREEN-DESKTOP](assets/fr/02.webp)


Start de applicatie en vink het vakje "Ik accepteer de voorwaarden...*" aan.


![GREEN-DESKTOP](assets/fr/03.webp)


Wanneer je Green voor de eerste keer opent, verschijnt het beginscherm zonder een geconfigureerde Wallet. Als je later wallets aanmaakt of importeert, verschijnen ze in deze Interface. Voordat je een Wallet aanmaakt, raad ik je aan om de instellingen van de applicatie aan te passen aan je behoeften. Klik op het pictogram Instellingen linksonder.


![GREEN-DESKTOP](assets/fr/04.webp)


In het menu "*General*" kun je de softwaretaal wijzigen en desgewenst experimentele functies activeren.


![GREEN-DESKTOP](assets/fr/05.webp)


In het menu "*Netwerk*" kun je verbinding via Tor inschakelen, een netwerk dat al je verbindingen versleutelt en je activiteiten moeilijk traceerbaar maakt. Hoewel deze optie de werking van de applicatie enigszins kan vertragen, is het zeer aan te raden om je privacy te beschermen, vooral als je niet je eigen complete node gebruikt.


![GREEN-DESKTOP](assets/fr/06.webp)


Voor gebruikers die hun eigen complete knooppunt hebben, biedt Green de optie om er via een Electrum server verbinding mee te maken, zodat ze totale controle over Bitcoin netwerkinformatie en transactieverspreiding hebben. Klik hiervoor op het menu "*Aangepaste servers en validatie*" en voer de gegevens van je Electrum-server in.


![GREEN-DESKTOP](assets/fr/07.webp)


Een andere alternatieve functie is de "*SPV Verification*" optie, waarmee je bepaalde Blockchain data direct kunt verifiëren en dus de noodzaak om Blockstream's standaard node te vertrouwen kunt verminderen, hoewel deze methode niet alle garanties van een Full node biedt. Deze optie is ook te vinden in het "*Custom servers and validation*" menu.


![GREEN-DESKTOP](assets/fr/08.webp)


Als je deze parameters hebt aangepast aan je behoeften, kun je deze Interface afsluiten.


## Een Bitcoin Wallet op Blockstream Green importeren


Je bent nu klaar om je Bitcoin Wallet te importeren. Klik op de knop "**Get Started**".


![GREEN-DESKTOP](assets/fr/09.webp)


Je kunt kiezen tussen het maken van een lokale Software Wallet of het beheren van een Cold Wallet via een Hardware Wallet. Voor deze tutorial concentreren we ons op het beheren van een Hardware Wallet, dus je moet de optie "*Op Hardware Wallet*" kiezen.


Met de optie "*Watch-only*" kunt u een uitgebreide openbare sleutel (`xpub`) importeren om Wallet transacties te bekijken zonder het bijbehorende geld te kunnen uitgeven.


![GREEN-DESKTOP](assets/fr/10.webp)


Als je een Jade gebruikt, klik je op de bijbehorende knop. Selecteer anders "*Een ander hardwareapparaat aansluiten*". In mijn geval gebruik ik een Ledger Nano S. Ledger gebruikers moeten de "*Bitcoin Legacy*" toepassing op hun Hardware Wallet installeren, omdat Green alleen deze versie ondersteunt.


![GREEN-DESKTOP](assets/fr/11.webp)


Sluit je Hardware Wallet aan op de computer en selecteer Green.


![GREEN-DESKTOP](assets/fr/12.webp)


Wacht tot Green uw Wallet informatie heeft geïmporteerd, waarna u toegang hebt.


![GREEN-DESKTOP](assets/fr/13.webp)


Op dit moment zijn er twee mogelijke scenario's. Als je je Hardware Wallet al eerder hebt gebruikt, zou je je account in de software moeten zien verschijnen. Maar als je, zoals ik, je Hardware Wallet net hebt geïnitialiseerd door een Mnemonic zin te genereren zonder hem al te hebben gebruikt, moet je een account aanmaken. Klik op "*Account aanmaken*".


![GREEN-DESKTOP](assets/fr/14.webp)


Kies "*Standaard*" als je een klassieke Wallet wilt gebruiken.


![GREEN-DESKTOP](assets/fr/15.webp)


Je hebt nu toegang tot je account.


![GREEN-DESKTOP](assets/fr/16.webp)


## Een Hardware Wallet met Blockstream Green gebruiken


Nu je Bitcoin Wallet is ingesteld, ben je klaar om je eerste Sats te ontvangen! Klik gewoon op de knop "*Ontvangen*".


![GREEN-DESKTOP](assets/fr/17.webp)


Klik op de knop "*Kopieer Address*" om de Address te kopiëren of scan de QR-code.


![GREEN-DESKTOP](assets/fr/18.webp)


Zodra de transactie is uitgezonden op het netwerk, verschijnt deze in je Wallet. Wacht tot je genoeg bevestigingen hebt ontvangen om de transactie als onveranderbaar te beschouwen.


![GREEN-DESKTOP](assets/fr/19.webp)


Met bitcoins in je Wallet, ben je nu klaar om ze te versturen. Klik op de knop "*Versturen*".


![GREEN-DESKTOP](assets/fr/20.webp)


Voer op de volgende pagina de Address van de ontvanger in. Je kunt het handmatig invoeren of een QR-code scannen met je webcam.


![GREEN-DESKTOP](assets/fr/21.webp)


Kies het betalingsbedrag.


![GREEN-DESKTOP](assets/fr/22.webp)


Onderaan het scherm kun je het tarief voor deze transactie selecteren. Je hebt de keuze om de aanbevelingen van de applicatie te volgen of je eigen kosten aan te passen. Hoe hoger de vergoeding in verhouding tot andere lopende transacties, hoe sneller uw transactie wordt verwerkt. Voor informatie over de kostenmarkt, zie [Mempool.space] (https://Mempool.space/) in het gedeelte "*Transactiekosten*".


![GREEN-DESKTOP](assets/fr/23.webp)


Als je specifiek wilt selecteren welke UTXO's je in je transactie wilt gebruiken, klik dan op de knop "*Handmatige Coin selectie*".


![GREEN-DESKTOP](assets/fr/24.webp)


Controleer je transactieparameters en als alles naar wens is, klik je op "*Next*".


![GREEN-DESKTOP](assets/fr/25.webp)


Controleer of de Address, het bedrag en de kosten correct zijn en klik dan op "*Transactie bevestigen*".


![GREEN-DESKTOP](assets/fr/26.webp)


Controleer of alle transactieparameters correct zijn op je Hardware Wallet scherm en onderteken de transactie ermee.


![GREEN-DESKTOP](assets/fr/27.webp)


Zodra de transactie is ondertekend vanaf de Hardware Wallet, zendt de Green deze automatisch uit naar het Bitcoin netwerk. Je transactie verschijnt dan op je Bitcoin Wallet dashboard, wachtend op bevestiging.


![GREEN-DESKTOP](assets/fr/28.webp)


Nu weet je hoe je Blockstream Green eenvoudig kunt configureren om je Bitcoin Wallet op een Hardware Wallet te beheren.


Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Ik raad je ook aan deze andere uitgebreide tutorial over de Blockstream Green mobiele app voor het instellen van een Hot Wallet te bekijken:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143