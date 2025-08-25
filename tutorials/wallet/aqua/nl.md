---
name: Aqua
description: Bitcoin, Lightning en Liquid in één Wallet
---
![cover](assets/cover.webp)


Aqua is een mobiele applicatie die het eenvoudig maakt om een Hot Wallet te maken voor Bitcoin en Liquid, en biedt ook de mogelijkheid om Lightning te gebruiken zonder de complexiteit van het beheren van een node, dankzij geïntegreerde swaps. Het maakt het ook mogelijk om USDT stablecoins te beheren op verschillende netwerken.


De Aqua app, ontwikkeld door het bedrijf JAN3 onder leiding van Samson Mow, is in eerste instantie specifiek ontworpen voor de behoeften van gebruikers in Latijns-Amerika, hoewel hij geschikt is voor elke gebruiker wereldwijd. De app is vooral interessant voor beginners en mensen die Bitcoin dagelijks gebruiken voor hun betalingen.


In deze tutorial gaan we uitzoeken hoe we de vele functies van Aqua kunnen gebruiken. Maar voordat we dat doen, nemen we even de tijd om te begrijpen wat een Sidechain is op Bitcoin en hoe Liquid werkt, zodat we de waarde van Aqua volledig kunnen begrijpen.


![AQUA](assets/fr/01.webp)


## Wat is een Sidechain?


Het Bitcoin protocol heeft opzettelijke technische beperkingen die helpen om de decentralisatie van het netwerk te behouden en om ervoor te zorgen dat de veiligheid verdeeld wordt over alle gebruikers. Deze beperkingen kunnen gebruikers echter soms frustreren, vooral tijdens congestie als gevolg van een hoog volume aan gelijktijdige transacties. Het debat over de schaalbaarheid van Bitcoin heeft de gemeenschap lang verdeeld, vooral tijdens de Blocksize War. Sinds deze episode wordt algemeen erkend binnen de Bitcoin gemeenschap dat de schaalbaarheid verzekerd moet worden door off-chain oplossingen, op tweede Layer systemen. Deze oplossingen omvatten sidechains, die nog relatief onbekend zijn en weinig gebruikt worden in vergelijking met andere systemen zoals de Lightning Network.


Een Sidechain is een onafhankelijke Blockchain die parallel aan de hoofd Bitcoin Blockchain werkt. Het gebruikt Bitcoin als rekeneenheid, dankzij een mechanisme genaamd "*two-way peg*". Dit systeem maakt het mogelijk om bitcoins vast te zetten op de hoofdketen om hun waarde te reproduceren op de Sidechain, waar ze circuleren in de vorm van tokens die worden ondersteund door de originele bitcoins. Deze tokens behouden normaal gesproken dezelfde waarde als de bitcoins die op de hoofdketen zijn vergrendeld, en het proces kan worden omgekeerd om geld terug te krijgen op Bitcoin.


Het doel van sidechains is om extra functionaliteiten of technische verbeteringen te bieden, zoals snellere transacties, lagere kosten of ondersteuning voor slimme contracten. Deze innovaties kunnen niet altijd direct op Bitcoin geïmplementeerd worden zonder de decentralisatie of veiligheid in gevaar te brengen. Sidechains maken het daarom mogelijk om nieuwe oplossingen te testen en te onderzoeken, terwijl de integriteit van Bitcoin behouden blijft. Deze protocollen vereisen echter vaak compromissen, vooral op het gebied van decentralisatie en veiligheid, afhankelijk van het gekozen bestuursmodel en consensusmechanisme.


## Wat is Liquid?


Liquid is een gefedereerde Sidechain overlay voor Bitcoin, ontwikkeld door Blockstream om de transactiesnelheid, privacy en functionaliteit te verbeteren. Het maakt gebruik van een bilateraal verankeringsmechanisme op een federatie om bitcoins op de hoofdketen te vergrendelen en in ruil daarvoor Liquid-bitcoins (L-BTC) te creëren, tokens die circuleren op Liquid terwijl ze ondersteund blijven door de oorspronkelijke bitcoins.


![AQUA](assets/fr/02.webp)


Liquid Network vertrouwt op een federatie van deelnemers, bestaande uit erkende entiteiten uit het Bitcoin ecosysteem, die blokken valideren en bilaterale pegging beheren. Naast L-BTC maakt Liquid ook de uitgifte van andere digitale activa mogelijk, zoals USDT stablecoin en andere cryptocurrencies.


![AQUA](assets/fr/03.webp)


## De Aqua-toepassing installeren


De eerste stap is natuurlijk het downloaden van de Aqua applicatie. Ga naar je applicatiewinkel:



- [Voor Android](https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [Voor Apple](https://apps.apple.com/us/app/Aqua-Wallet/id6468594241).

![AQUA](assets/fr/04.webp)


Voor Android gebruikers heb je ook de optie om de applicatie te installeren via het `.apk` bestand [beschikbaar op hun GitHub] (https://github.com/AquaWallet/Aqua-Wallet/releases).


![AQUA](assets/fr/05.webp)


Start de applicatie en vink het vakje "*Ik heb de Servicevoorwaarden en het Privacybeleid gelezen en ga ermee akkoord*" aan.


![AQUA](assets/fr/06.webp)


## Maak uw Wallet op Aqua


Klik op de knop "*Creëer Wallet*".


![AQUA](assets/fr/07.webp)


En voilà, je Wallet is al gemaakt!


![AQUA](assets/fr/08.webp)


Maar allereerst, aangezien dit een zelfbewaarnemende Wallet is, is het noodzakelijk om een fysieke back-up van je Mnemonic te maken. **Deze Mnemonic geeft je volledige, onbeperkte toegang tot al je bitcoins**. Iedereen die in het bezit is van deze Mnemonic kan je fondsen stelen, zelfs zonder fysieke toegang tot je telefoon.


Hiermee kun je weer toegang krijgen tot je bitcoins in geval van verlies, diefstal of breuk van je telefoon. Het is daarom erg belangrijk om het zorgvuldig op te slaan op een fysieke drager (niet digitaal) en het op een veilige locatie te bewaren. Je kunt het opschrijven op een stuk papier, of voor extra veiligheid, als dit een grote Wallet is, zou ik aanraden om het te graveren op een roestvrijstalen steun om het te beschermen tegen het risico van brand, overstroming of instorting (voor een Hot die is ontworpen om een kleine hoeveelheid bitcoins te beveiligen, is een eenvoudige back-up op papier waarschijnlijk voldoende).


Klik hiervoor op het menu Instellingen.


![AQUA](assets/fr/09.webp)


Klik dan op "*View seed Phrase*". Maak een fysieke back-up van deze 12-woorden zin.


![AQUA](assets/fr/10.webp)


In hetzelfde instellingenmenu kun je ook de taal van de applicatie en de gebruikte fiatvaluta wijzigen.


![AQUA](assets/fr/11.webp)


Voordat je je eerste bitcoins ontvangt in je Wallet, **raad ik je sterk aan om een lege hersteltest uit te voeren**. Maak een notitie van wat referentie-informatie, zoals je xpub of de eerste Address die je ontvangt, wis dan je Wallet op de Aqua app terwijl hij nog leeg is. Probeer dan je Wallet op Aqua te herstellen met je papieren back-ups. Controleer of de cookie-informatie die na het herstellen wordt gegenereerd, overeenkomt met de informatie die je oorspronkelijk hebt opgeschreven. Als dat zo is, kunt u er zeker van zijn dat uw papieren back-ups betrouwbaar zijn. Om meer te weten te komen over hoe je een testherstel uitvoert, kun je deze andere tutorial raadplegen:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Je kunt het niet zien op mijn scherm omdat ik een emulator gebruik, maar in de instellingen vind je een optie om de app te vergrendelen met een biometrisch authenticatiesysteem. Ik raad ten zeerste aan om deze beveiligingsfunctie in te schakelen, omdat zonder deze functie iedereen met toegang tot je ontgrendelde telefoon je bitcoins kan stelen. Je kunt Face ID gebruiken op iOS of je vingerafdruk op Android. Als deze methoden mislukken tijdens de verificatie, kun je nog steeds toegang krijgen tot de app met behulp van de PIN-code van je telefoon.


## Bitcoins ontvangen op Aqua


Nu je Wallet is ingesteld, ben je klaar om je eerste Sats te ontvangen! Klik gewoon op de knop "*Ontvangen*" in het menu "*Wallet*".


![AQUA](assets/fr/12.webp)


Je kunt ervoor kiezen om bitcoins onchain, op Liquid of via Lightning te ontvangen.


![AQUA](assets/fr/13.webp)


Voor onchain-transacties zal Aqua generate een specifieke ontvangende Address zijn, waar je je Sats kunt ontvangen.


![AQUA](assets/fr/14.webp)


Op dezelfde manier, als je Liquid, Aqua kiest, krijg je een Liquid Address.


![AQUA](assets/fr/15.webp)


Als je liever geld ontvangt via Lightning, moet je eerst het gewenste bedrag opgeven.


![AQUA](assets/fr/16.webp)


Klik dan op "*generate Invoice*".


![AQUA](assets/fr/17.webp)


Aqua zal een Invoice aanmaken om fondsen te ontvangen van een Lightning Wallet. Merk op dat, in tegenstelling tot de onchain en Liquid opties, fondsen ontvangen via Lightning automatisch worden omgezet naar L-BTC op Liquid met behulp van de Boltz tool, aangezien Aqua geen Lightning node is. Met dit proces kunt u fondsen ontvangen en verzenden via Lightning, maar zonder ooit uw bitcoins op Lightning op te slaan.


![AQUA](assets/fr/18.webp)


Persoonlijk begin ik met het versturen van bitcoins via Lightning naar Aqua. Zodra de transactie met de Invoice is voltooid, ontvangen we een bevestiging.


![AQUA](assets/fr/19.webp)


Om de voortgang van de swap te volgen, ga je terug naar de startpagina van je Wallet en klik je op het "*L2 Bitcoin*" account, waar Lightning (via swap) en Liquid transacties staan.


![AQUA](assets/fr/20.webp)


Hier kun je je transactie en je L-BTC saldo bekijken.


![AQUA](assets/fr/21.webp)


## Bitcoin ruilen met Aqua


Nu je activa hebt in je Aqua Wallet, kun je ze direct vanuit de app omwisselen, ofwel om ze over te zetten naar de hoofd Bitcoin Blockchain, of naar Liquid. Je kunt ook Bitcoins omwisselen naar USDT stablecoin (of andere). Je kunt ook je bitcoins omzetten in USDT stablecoin (of andere). Ga hiervoor naar het menu "*Marktplaats*".


![AQUA](assets/fr/22.webp)


Klik op "*Swaps*".


![AQUA](assets/fr/23.webp)


Selecteer in het vak "*Omzetten van*" de activa die je wilt verhandelen. Momenteel bezit ik alleen L-BTC, dus dat selecteer ik.


![AQUA](assets/fr/24.webp)


Kies in het vak "*Transfer to*" de doelactiva voor je swap. Ik koos voor USDT op de Liquid Network.


![AQUA](assets/fr/25.webp)


Voer het bedrag in dat je wilt converteren.


![AQUA](assets/fr/26.webp)


Bevestig door op "*Doorgaan*" te klikken.


![AQUA](assets/fr/27.webp)


Controleer of je tevreden bent met de wisselinstellingen en bevestig dit door de knop "*Swap*" onderaan het scherm te slepen.


![AQUA](assets/fr/28.webp)


Je ruil is nu bevestigd.


![AQUA](assets/fr/29.webp)


Als we terugkijken naar onze Wallet, zien we dat we nu USDT op Liquid hebben.


![AQUA](assets/fr/30.webp)


## Bitcoins versturen met Aqua


Nu je bitcoins in je Aqua Wallet hebt, kun je ze versturen. Klik op de knop "*Versturen*".


![AQUA](assets/fr/31.webp)


Kies de activa die je wilt verzenden of selecteer het netwerk om de transactie uit te voeren. Voor mijn part ga ik bitcoins versturen via Lightning.


![AQUA](assets/fr/32.webp)


Voer vervolgens de informatie in die nodig is om de betaling te verzenden: voor onchain of Liquid bitcoins moet u een ontvangende Address invoeren; voor Lightning is een Invoice vereist. U kunt deze informatie rechtstreeks in het daarvoor bestemde veld plakken, of het QR-codepictogram gebruiken om uw camera te openen en de Address of Invoice te scannen. Klik vervolgens op "*Doorgaan*".


![AQUA](assets/fr/33.webp)


Klik opnieuw op "*Doorgaan*" als alle informatie correct lijkt.


![AQUA](assets/fr/34.webp)


Aqua toont je vervolgens een samenvatting van de transactie. Controleer of alle informatie correct is, inclusief de Address bestemming, kosten en bedrag. Om de transactie te bevestigen, schuif je op de knop "*Slide to send*" onderaan het scherm.


![AQUA](assets/fr/35.webp)


Je ontvangt dan een bevestiging van de verzending.


![AQUA](assets/fr/36.webp)


Nu weet je dus hoe je de Aqua app kunt gebruiken om geld te ontvangen en uit te geven op Bitcoin, Lightning en Liquid, allemaal vanaf één Interface.


Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Ik raad je ook aan deze andere uitgebreide tutorial over de Blockstream Green mobiele app te bekijken, wat een andere interessante oplossing is voor het instellen van je Liquid Wallet :


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a