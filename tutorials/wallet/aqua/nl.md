---
name: Aqua
description: Bitcoin, Lightning en Liquid in één wallet
---
![cover](assets/cover.webp)


Aqua is een mobiele applicatie die het eenvoudig maakt om een hot wallet te maken voor Bitcoin en Liquid. Dankzij geïntegreerde swaps biedt de app ook de mogelijkheid om Lightning te gebruiken zonder de complexiteit van het beheren van een node. Bovendien kun je er USDT-stablecoins mee beheren op verschillende netwerken.


De Aqua-app, ontwikkeld door het bedrijf JAN3 onder leiding van Samson Mow, is in eerste instantie specifiek ontworpen voor de behoeften van gebruikers in Latijns-Amerika, hoewel de app wereldwijd voor iedereen geschikt is. De app is vooral interessant voor beginners en mensen die Bitcoin dagelijks gebruiken voor hun betalingen.


In deze tutorial gaan we uitzoeken hoe je de vele functies van Aqua kunt gebruiken. Maar voordat we dat doen, nemen we even de tijd om te begrijpen wat een Bitcoin-sidechain is en hoe Liquid werkt, zodat je de waarde van Aqua volledig kunt begrijpen.


![AQUA](assets/fr/01.webp)


## Wat is een sidechain?


Het Bitcoin-protocol heeft opzettelijke technische beperkingen die helpen de decentralisatie van het netwerk te behouden en de veiligheid over alle gebruikers te verdelen. Deze beperkingen kunnen voor gebruikers soms echter frustrerend zijn, vooral tijdens congestieperioden als gevolg van een hoog volume aan gelijktijdige transacties. Het debat over de schaalbaarheid van Bitcoin heeft de gemeenschap lang verdeeld gehouden, met name tijdens de Blocksize War. Sinds deze episode wordt binnen de Bitcoin-gemeenschap algemeen aanvaard dat schaalbaarheid door off-chain oplossingen, oftewel second-layer-systemen, moet worden verzekers. Deze oplossingen omvatten sidechains, die nog relatief onbekend zijn en in vergelijking met andere systemen zoals het Lightning Network weinig gebruikt worden.


Een sidechain is een onafhankelijke blockchain die parallel aan de hoofd-Bitcoin-blockchain werkt. Het gebruikt bitcoin als rekeneenheid, dankzij een mechanisme genaamd "*two-way peg*". Dit systeem maakt het mogelijk om bitcoins vast te zetten op de hoofdketen om hun waarde te reproduceren op de sidechain, waar ze circuleren in de vorm van tokens die gedekt worden door de originele bitcoins. Deze tokens behouden normaal gesproken dezelfde waarde als de bitcoins die op de hoofdketen zijn vergrendeld, en het proces kan worden omgekeerd om geld terug te krijgen op Bitcoin.


Het doel van sidechains is om extra functionaliteiten of technische verbeteringen te bieden, zoals snellere transacties, lagere kosten of ondersteuning voor smart contracts (slimme contracten). Deze innovaties kunnen niet altijd direct op Bitcoin geïmplementeerd worden zonder de decentralisatie of veiligheid in gevaar te brengen. Sidechains maken het daarom mogelijk om nieuwe oplossingen te testen en te verkennen, terwijl de integriteit van Bitcoin behouden blijft. Deze protocollen vereisen echter vaak compromissen, vooral op het gebied van decentralisatie en veiligheid, afhankelijk van het gekozen bestuursmodel en consensusmechanisme.


## Wat is Liquid?


Liquid is een gefedereerde sidechain-laag voor Bitcoin, ontwikkeld door Blockstream om de transactiesnelheid, privacy en functionaliteit te verbeteren. Het maakt gebruik van een bilateraal verankeringsmechanisme op een federatie om bitcoins op de hoofdketen te vergrendelen en in ruil daarvoor Liquid-bitcoins (L-BTC) te creëren. Dit zijn tokens die circuleren op Liquid terwijl ze gedekt blijven door de oorspronkelijke bitcoins.


![AQUA](assets/fr/02.webp)


Liquid Network vertrouwt op een federatie van deelnemers, bestaande uit erkende entiteiten uit het Bitcoin-ecosysteem, die blokken valideren en bilaterale pegging beheren. Naast L-BTC maakt Liquid ook de uitgifte van andere digitale activa mogelijk, zoals USDT stablecoin en andere cryptocurrencies.


![AQUA](assets/fr/03.webp)


## De Aqua-toepassing installeren


De eerste stap is natuurlijk het downloaden van de Aqua-applicatie. Ga naar de app store van je telefoon:



- [Voor Android](https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [Voor Apple](https://apps.apple.com/us/app/Aqua-Wallet/id6468594241).

![AQUA](assets/fr/04.webp)


Voor Android gebruikers heb je ook de optie om de applicatie te installeren via het `.apk` bestand [beschikbaar op hun GitHub](https://github.com/AquaWallet/Aqua-Wallet/releases).


![AQUA](assets/fr/05.webp)


Start de applicatie en vink het vakje "*Ik heb de Servicevoorwaarden en het Privacybeleid gelezen en ga ermee akkoord*" aan.


![AQUA](assets/fr/06.webp)


## Maak je wallet aan op Aqua


Klik op de knop "*Create wallet*".


![AQUA](assets/fr/07.webp)


En voilà, je wallet is al aangemaakt!


![AQUA](assets/fr/08.webp)


Maar allereerst: aangezien dit een self-custodial wallet is, is het essentieel om een fysieke back-up van je mnemonische zin (seed phrase) te maken. **Deze zin geeft je volledige, onbeperkte toegang tot al je bitcoins**. Iedereen die in het bezit is van deze zin kan je fondsen stelen, zelfs zonder fysieke toegang tot je telefoon.


Hiermee kun je de toegang tot je bitcoins herstellen in geval van verlies, diefstal of een defecte telefoon. Het is daarom cruciaal om het zorgvuldig op te slaan op een fysieke drager (niet digitaal) en het op een veilige locatie te bewaren. Je kunt de zin opschrijven op een stuk papier of, voor extra veiligheid als dit een grote wallet is, zou ik aanraden om hem in roestvrij staal te graveren om hem te beschermen tegen het risico van brand, overstroming of instorting. (Voor een hot wallet die is ontworpen om een kleine hoeveelheid bitcoins te beveiligen, is een eenvoudige back-up op papier waarschijnlijk voldoende.)


Klik hiervoor op het menu "*Settings*".


![AQUA](assets/fr/09.webp)


Klik dan op "*View Seed Phrase*". Maak een fysieke back-up van deze 12-woorden zin.


![AQUA](assets/fr/10.webp)


In hetzelfde instellingenmenu kun je ook de taal van de applicatie en de gebruikte fiatvaluta wijzigen.


![AQUA](assets/fr/11.webp)


Voordat je je eerste bitcoins ontvangt in je wallet, **raad ik je sterk aan om een lege hersteltest uit te voeren**. Noteer enkele referentiegegevens, zoals je xpub of het eerste ontvangstadres, wis dan je wallet op de Aqua-app terwijl hij nog leeg is. Probeer dan je wallet in Aqua te herstellen met je papieren back-ups. Controleer of de gegenereerde gegevens na het herstellen overeenkomen met de informatie die je oorspronkelijk hebt opgeschreven. Als dat zo is, kun je er zeker van zijn dat je papieren back-ups betrouwbaar zijn. Voor meer informatie over het uitvoeren van een testherstel kun je deze andere tutorial raadplegen:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Je kunt het op mijn scherm niet zien omdat ik een emulator gebruik, maar in de instellingen vind je een optie om de app te vergrendelen met een biometrisch authenticatiesysteem. Ik raad ten zeerste aan om deze beveiligingsfunctie in te schakelen, omdat iedereen met toegang tot je ontgrendelde telefoon anders je bitcoins kan stelen. Je kunt Face ID gebruiken op iOS of je vingerafdruk op Android. Als deze methoden mislukken tijdens de verificatie, kun je nog steeds toegang krijgen tot de app met behulp van de PIN-code van je telefoon.


## Bitcoins ontvangen op Aqua


Nu je wallet is ingesteld, ben je klaar om je eerste sats te ontvangen! Klik gewoon op de knop "*Receive*" in het menu "*Wallet*".


![AQUA](assets/fr/12.webp)


Je kunt ervoor kiezen om bitcoins onchain, op Liquid of via Lightning te ontvangen.


![AQUA](assets/fr/13.webp)


Voor onchain-transacties zal Aqua een specifieke ontvangstadres aanmaken, waar je je sats kunt ontvangen.


![AQUA](assets/fr/14.webp)


Op dezelfde manier, als je Liquid kiest, dan krijg je van Aqua een Liquid-adres.


![AQUA](assets/fr/15.webp)


Als je liever geld ontvangt via Lightning, moet je eerst het gewenste bedrag opgeven.


![AQUA](assets/fr/16.webp)


Klik dan op "*Generate Invoice*".


![AQUA](assets/fr/17.webp)


Aqua zal een invoice aanmaken om fondsen te ontvangen van een Lightning-wallet. Merk op dat, in tegenstelling tot de onchain- en Liquid-opties, fondsen die via Lightning ontvangen automatisch worden omgezet naar L-BTC op Liquid met behulp van de Boltz-tool, omdat Aqua geen Lightning-node heeft. Met dit proces kan je geld ontvangen en verzenden via Lightning, maar zonder ooit je bitcoins op Lightning op te slaan.


![AQUA](assets/fr/18.webp)


Persoonlijk begin ik met het versturen van bitcoins via Lightning naar Aqua. Zodra de transactie met de invoice is voltooid, ontvangen we een bevestiging.


![AQUA](assets/fr/19.webp)


Om de voortgang van de swap te volgen, ga je terug naar de startpagina van je wallet en klik je op het "*L2 Bitcoin*" account, waar Lightning (via swap) en Liquid-transacties staan.


![AQUA](assets/fr/20.webp)


Hier kun je je transactie en je L-BTC saldo bekijken.


![AQUA](assets/fr/21.webp)


## Bitcoin omwisseling (swap) met Aqua


Nu je activa hebt in je Aqua-wallet, kun je deze direct vanuit de app omwisselen. Dit kun je doen om ze over te zetten naar de Bitcoin-blockchain, of naar Liquid, of om je bitcoins om te wisselen naar een USDT-stablecoin (of andere). Je kunt ook je bitcoins omzetten in USDT stablecoin (of andere). Ga hiervoor naar het menu "*Marketplace*".


![AQUA](assets/fr/22.webp)


Klik op "*Swaps*".


![AQUA](assets/fr/23.webp)


Selecteer in het vak "*Transfer from*" de activa die je wilt verhandelen. Momenteel bezit ik alleen L-BTC, dus dat selecteer ik.


![AQUA](assets/fr/24.webp)


Kies in het vak "*Transfer to*" de doelactiva voor je swap. Ik koos voor USDT op het Liquid Network.


![AQUA](assets/fr/25.webp)


Voer het bedrag in dat je wilt converteren.


![AQUA](assets/fr/26.webp)


Bevestig door op "*Continue*" te klikken.


![AQUA](assets/fr/27.webp)


Controleer of je tevreden bent met de wisselinstellingen en bevestig dit door de knop "*Swap*" onderaan het scherm te slepen.


![AQUA](assets/fr/28.webp)


Je ruil is nu bevestigd.


![AQUA](assets/fr/29.webp)


Als we terugkijken naar onze wallet, zien we dat we nu USDT op Liquid hebben.


![AQUA](assets/fr/30.webp)


## Bitcoins versturen met Aqua


Nu je bitcoins in je Aqua-wallet hebt, kun je ze versturen. Klik op de knop "*Send*".


![AQUA](assets/fr/31.webp)


Kies de activa die je wilt verzenden of selecteer het netwerk om de transactie uit te voeren. Ik ga bijvoorbeeld bitcoins versturen via Lightning.


![AQUA](assets/fr/32.webp)


Voer vervolgens de benodigde informatie in om de betaling te verzenden: voor onchain- of Liquid-bitcoins moet je een ontvangstadres invoeren; voor Lightning is een invoice vereist. Je kunt deze informatie rechtstreeks in het daarvoor bestemde veld plakken, of het QR-codepictogram gebruiken om je camera te openen en het invoice-adres te scannen. Klik vervolgens op "*Continue*".


![AQUA](assets/fr/33.webp)


Klik opnieuw op "*Continue*" als alle informatie correct lijkt.


![AQUA](assets/fr/34.webp)


Aqua toont je vervolgens een samenvatting van de transactie. Controleer of alle informatie correct is, inclusief het bestemmingadres, kosten en bedrag. Om de transactie te bevestigen, schuif je op de knop "*Slide to send*" onderaan het scherm.


![AQUA](assets/fr/35.webp)


Je ontvangt dan een bevestiging van de verzending.


![AQUA](assets/fr/36.webp)


Nu weet je dus hoe je de Aqua-app kunt gebruiken om geld te ontvangen en uit te geven op Bitcoin, Lightning en Liquid, allemaal vanaf één interface.


Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een groene duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Ik raad je ook aan deze andere uitgebreide tutorial over de Blockstream Green mobiele app te bekijken, wat een andere interessante oplossing is voor het instellen van je Liquid-wallet:


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a
