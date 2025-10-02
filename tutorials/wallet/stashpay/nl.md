---
name: StashPay
description: De minimalistische Bitcoin Wallet voor iedereen
---

![cover](assets/cover.webp)



Gebruikerservaring is een sleutelfactor in de adoptie van Bitcoin oplossingen over de hele wereld. Het bieden van een soepele, eenvoudige en technisch onbelemmerde ervaring is de prioriteit voor veel portemonnees en Exchange platforms. In dit opzicht valt StashPay op door zijn minimalistische aanpak, terwijl het tegelijkertijd de kracht van Lightning Network laat zien.



In deze tutorial bekijken we dit portfolio om te zien hoe het werkt en hoe het ideaal is voor kleine bedrijven of zelfstandige ondernemers.



## Aan de slag met StashPay



StashPay is een Lightning self-custodial Wallet die vooral bekend staat om zijn minimalistische, gebruikersgerichte gebruikerservaring.  Met deze Wallet heb je geen technische kennis nodig om je eerste satoshis te ontvangen en te versturen.



StashPay is een open-source project ontwikkeld in React Native en heeft als doel het probleem van hoge transactiekosten op te lossen, zelfs met transacties op de hoofdketen van het Bitcoin protocol. Het is beschikbaar als mobiele app op Android- en iOS-platforms via downloadlinks op de [website](https://stashpay.me/).



![introduce](assets/fr/01.webp)



Het is belangrijk om de Android-applicatie van de website te downloaden, omdat deze niet beschikbaar is in de Google Play Store.


Als het downloaden is voltooid, geef dan de benodigde machtigingen zodat je de applicatie op je Android-telefoon kunt installeren.



Zodra de applicatie is geïnstalleerd, maakt StashPay een initiële Bitcoin Wallet voor je aan, de eerste keer dat je de applicatie opent. Voor elke transactie raden we je aan een back-up te maken van deze Wallet. Hieronder vindt u al onze richtlijnen om ervoor te zorgen dat er een goede back-up wordt gemaakt van uw herstelzinnen.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ga naar de StashPay-instellingen door te klikken op het pictogram "Instellingen" en klik vervolgens op de optie **Back-up maken**. Geef vervolgens toestemming voor het weergeven van herstelzinnen. Kopieer uw herstelzinnen niet naar het klembord van uw telefoon, omdat ze toegankelijk kunnen zijn voor andere frauduleuze toepassingen die op uw mobiel zijn geïnstalleerd.



![backup](assets/fr/02.webp)



Je kunt ook een Bitcoin Wallet die je al gebruikt terughalen door op de optie **Wallet terughalen** te klikken en je 12 of 24 herstelwoorden in te voeren.



### Ontvang je eerste satoshis op StashPay



Klik op het beginscherm op de knop **Ontvangen** en stel een bedrag in dat groter is dan het bedrag dat in rood is aangegeven. In ons geval kunnen we niet minder dan 0,11 USD ontvangen met de StashPay Wallet.



![receive](assets/fr/03.webp)



Zodra je het bedrag hebt bepaald, kun je op de knop **Creëer Invoice** klikken en vervolgens de Invoice scannen of kopiëren om deze naar je satoshisverzender te sturen.



![receive_sats](assets/fr/04.webp)



Je kunt je transactiegeschiedenis bekijken door op het "klok"-pictogram op de startpagina te klikken.



![network_fee](assets/fr/05.webp)



Je zult gemerkt hebben dat je voor het ontvangen van satoshis netwerkkosten moet betalen. Deze kosten worden afgetrokken van de satoshi's die je gaat ontvangen. Dit komt omdat StashPay een Wallet is gebaseerd op de Breez Development Kit. Om satoshis te ontvangen met de Lightning node-vrije implementatie van de Kit, brengt Breez de klant (StashPay in ons geval) `0,25% + 40 satoshis` in rekening. Lees meer in onze Misty Breez-handleiding.



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Bitcoins versturen met StashPay



Bitcoins versturen met StashPay is redelijk intuïtief dankzij de minimalistische Interface. Klik op het beginscherm op de knop **Versturen**. Scan de QR-code of plak de Address waarnaar je satoshi's wilt sturen. StashPay detecteert automatisch de Bitcoin protocolketen waarnaar je bitcoins wilt sturen.



![send](assets/fr/06.webp)



Aangezien StashPay een Wallet is gebaseerd op de Breez Development Kit, profiteert het van een interessant voordeel: het versturen van bitcoins op de hoofdketen tegen lage kosten. Breez gebruikt de Boltz-service om transacties tussen de verschillende ketens van het Bitcoin protocol uit te voeren, waardoor klanten die de Development Kit implementeren direct in hun applicatie van deze service kunnen profiteren.



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Breez SDK legt echter een minimumbedrag op waarbij je bitcoins naar een Address op de hoofdketen kunt sturen.



![onchain](assets/fr/07.webp)



Je kunt ook bitcoins versturen met de Lightning Address van je ontvanger. Controleer je transactiegegevens en bevestig door op de knop **Versturen** te klikken.



![confirm](assets/fr/08.webp)



## Meer configuraties



In de StashPay-instellingen kunt u configuraties aanpassen om uw gebruik van de Wallet te personaliseren.



Met StashPay kun je Exchange satoshis wisselen op basis van de lokale valuta van je keuze. Klik op de **Koersen** optie en zoek dan je valuta in de lijst van +113 valuta's die worden aangeboden door StashPay.



![currencies](assets/fr/09.webp)



In het **Ontvangstopties** menu, vind je alle instellingen voor het ontvangen van bitcoins met StashPay. Door bijvoorbeeld **Kies Lightning of Onchain** te selecteren, schakel je Wallet in om bitcoins te ontvangen van de hoofdketen.



![receive-onchain](assets/fr/10.webp)



Met de optie **Scan OnChain adressen** kun je het saldo van je Wallet verversen door alle UTXO's (bitcoins die je nog niet hebt uitgegeven) te controleren die aan je verschillende adressen zijn gekoppeld.



![rescan](assets/fr/11.webp)



Het **Export logboek** menu geeft een overzicht van alle Breez en Boltz infrastructuur acties met betrekking tot je transacties en atomaire uitwisselingen tussen de verschillende Bitcoin protocolketens.



![export](assets/fr/12.webp)



Je hebt net de minimalistische Bitcoin Wallet van StashPay onder de knie. Als je deze handleiding nuttig vond, raden we je onze handleiding aan over hoe je aan de slag gaat met Bitcoin en je eerste bitcoins verdient.



https://planb.network/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f