---
name: Ashigaru
description: De fork van Samourai Wallet om je bitcoins te beveiligen, beheren en mixen
---

![cover](assets/cover.webp)



Ashigaru is een Bitcoin mobiele wallet toepassing die voortborduurt op het Samourai Wallet project, maar in een nieuwe vorm. Deze software ontstond in een bijzondere context: in april 2024 werden de oprichters van Samourai Wallet gearresteerd door de Amerikaanse autoriteiten en hun servers werden in beslag genomen. Hoewel de Samurai-toepassing zelf bruikbaar bleef, wordt ze momenteel niet meer onderhouden. Ashigaru is een gratis fork versie van Samurai Wallet, onderhouden door een anoniem team om de continuïteit van de functionaliteit van Samurai te garanderen en de oorspronkelijke filosofie te waarborgen: het verdedigen van de privacy en soevereiniteit van Bitcoin gebruikers.



Ashigaru neemt veel van het DNA van Samourai over: een vergelijkbare interface, een duidelijk zelfbehoudende aanpak, open source en een focus op privacy. De code wordt gedistribueerd onder de GNU GPLv3 licentie, die ervoor zorgt dat iedereen de software kan controleren, wijzigen of herdistribueren.



De Ashigaru-toepassing integreert een set geavanceerde tools voor vertrouwelijkheid en beheer van uw UTXO's:




- Whirlpool**, een coinjoin-protocol gebaseerd op Zerolink, waarmee je de deterministische links tussen transactie-entrees en -exits kunt verbreken, zonder de soevereiniteit over je fondsen te verliezen.
- PayNym**, dat herbruikbare betaalcodes (BIP47) implementeert, nu weergegeven via een "*Pepehash*" avatar systeem.
- Ricochet**, een functie die tussenliggende sprongen aan transacties toevoegt om ze moeilijker te traceren te maken.
- En natuurlijk ***Coin Control*** om je UTXO's nauwkeurig te selecteren, bevriezen en labelen.
- Batch Spending***, om kosten te verlagen door meerdere betalingen in één transactie te groeperen.
- De **Stealth Mode**, die de applicatie op je mobiel verbergt achter een dummy launcher om onopgemerkt te blijven tijdens een fysieke inspectie van je telefoon.
- Geavanceerde bestedingstools om je vertrouwelijkheid te optimaliseren (payjoin, stonewall...).
- Een geoptimaliseerd herstelsysteem met Passphrase BIP39.
- Een systeem voor het automatisch optimaliseren van de keuze van transactiekosten.



![Image](assets/fr/01.webp)



Ashigaru is daarom gericht op gebruikers die zich bewust zijn van de problemen rondom traceerbaarheid van transacties op Bitcoin. Of je nu een privacy-bewuste gebruiker bent, een doorgewinterde bitcoiner die zich inzet voor zelfbehoud, of een individu dat blootgesteld wordt aan de risico's van toegenomen toezicht, deze wallet applicatie biedt je de tools die je nodig hebt om weer controle te krijgen over je activiteiten op Bitcoin.



Ashigaru is beschikbaar in een mobiele versie via de app, die we in deze tutorial zullen verkennen. Maar het kan ook op de PC gebruikt worden met ***Ashigaru Terminal***, die we in een toekomstige tutorial zullen introduceren.



![Image](assets/fr/02.webp)



In deze tutorial wil ik je kennis laten maken met het basisgebruik van Ashigaru: installatie, verbinding maken met de Dojo, back-up, bitcoins ontvangen en versturen. Geavanceerde tools worden in andere tutorials gepresenteerd.



## 1. Vereisten voor Ashigaru



De applicatie vereist een paar vereisten om goed te werken. Ten eerste is het geen applicatie die beschikbaar is in klassieke winkels zoals de Google Play Store of App Store. Het installeert alleen handmatig op je telefoon vanuit het `.apk` bestand, te downloaden via het Tor netwerk. Dus als je een iPhone gebruikt, werkt deze methode niet: je hebt een Android-toestel nodig.



Om het `.apk` bestand via Tor te downloaden, heb je een browser nodig die toegang heeft tot `.onion` sites. De makkelijkste manier is om de Tor Browser applicatie op je telefoon te installeren, beschikbaar via de [Google Play Store](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) of direct [via de `.apk`](https://www.torproject.org/download/#android).



![Image](assets/fr/03.webp)



De meeste recente smartphones blokkeren standaard de installatie van applicaties van onbekende bronnen. Je moet deze optie voor Tor Browser tijdelijk activeren in de instellingen van je apparaat om installatie toe te staan. Zodra de applicatie is geïnstalleerd, vergeet dan niet om deze functie uit te schakelen om de beveiliging van je telefoon te versterken.



Een andere essentiële voorwaarde voor het gebruik van Ashigaru is een Bitcoin Dojo knooppunt. Om redenen van veiligheid en soevereiniteit onderhoudt het Ashigaru team geen gecentraliseerde server om je applicatie op aan te sluiten. Dus je moet je eigen Dojo instantie draaien, of verbinding maken met een vertrouwde.



Met de Dojo kan je Ashigaru-toepassing blockchaininformatie raadplegen, je adresbalansen bekijken en je transacties uitzenden op het Bitcoin netwerk.



Om meer te weten te komen over Dojo en te leren hoe je het installeert, nodig ik je uit om deze speciale tutorial te volgen:



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Als je het je echt niet kunt veroorloven om je eigen Dojo te beheren, kun je mensen vinden die bereid zijn om hun instantie gratis te delen op [dojobay.pw](https://www.dojobay.pw/mainnet/). Dit kan een tijdelijke oplossing zijn, maar op de lange termijn raad ik je aan om je eigen Dojo te gebruiken om je soevereiniteit en vertrouwelijkheid te garanderen.



## 2. Controleer en installeer de Ashigaru-toepassing



### 2.1. Download de Ashigaru-toepassing



Open Tor Browser op je telefoon en ga naar [de officiële Ashigaru website](https://ashigaru.rs/download/), in de `Download` sectie. Klik vervolgens op de knop `Download voor Android` om het installatiebestand te downloaden.



![Image](assets/fr/04.webp)



Voordat we de applicatie op je apparaat installeren, controleren we de authenticiteit en integriteit ervan. Dit is een zeer belangrijke stap, vooral wanneer je een applicatie rechtstreeks vanuit een `.apk'-bestand installeert.



### 2.2. Controleer Ashigaru-toepassing



Ga terug naar [de officiële Ashigaru website](https://ashigaru.rs/download/) in de `Download` sectie, kopieer dan het bericht dat wordt weergegeven onder de titel `SHA-256 Hash van het APK-bestand`. Kopieer het hele blok, van `BEGIN PGP SIGNED MESSAGE` tot `END PGP SIGNATURE`.



![Image](assets/fr/05.webp)



Open nog steeds op je telefoon een nieuw tabblad in Tor Browser en ga naar [de Keybase verificatietool](https://keybase.io/verify). Plak het bericht dat je zojuist hebt gekopieerd in het daarvoor bestemde veld en klik dan op de `Verifieer` knop.



![Image](assets/fr/06.webp)



Als de handtekening echt is, zal Keybase een bericht weergeven dat bevestigt dat het bestand is ondertekend door de ontwikkelaars van Ashigaru. U kunt ook klikken op het `ashigarudev` profiel dat wordt aangegeven door Keybase en controleren of hun sleutelvingerafdruk exact overeenkomt met : `A138 06B1 FA2A 676B`.



Als er in dit stadium echter een foutmelding verschijnt, betekent dit dat de handtekening ongeldig is. In dit geval, **installeer de APK** niet. Begin opnieuw vanaf het begin of vraag de community om hulp voordat je verder gaat.



![Image](assets/fr/07.webp)



Keybase heeft je de hash van de applicatie gegeven. We zullen nu controleren of de hash van het `.apk` bestand dat je hebt gedownload overeenkomt met de hash die is geverifieerd op Keybase. Ga hiervoor naar [HASH FILE ONLINE](https://hash-file.online/).



![Image](assets/fr/08.webp)



Klik op de knop `BROUW...` en selecteer het bestand `.apk` dat je in stap 2.1 hebt gedownload.


Kies dan de hashfunctie `SHA-256` en klik op `CALCULATE HASH` om de hash van je bestand te berekenen.



![Image](assets/fr/09.webp)



De site zal de hash van je `.apk` bestand weergeven. Vergelijk deze met de hash die je hebt geverifieerd op Keybase.io. Als de twee hashes identiek zijn, is de echtheids- en integriteitscontrole geslaagd. Je kunt nu doorgaan met het installeren van de applicatie.



![Image](assets/fr/10.webp)



### 2.3. Installeer de Ashigaru-toepassing



Om de applicatie te installeren, open je bestandsbeheer van je telefoon en ga je naar de map downloads. Klik vervolgens op het bestand `.apk` dat je zojuist hebt gecontroleerd en bevestig de installatie wanneer daarom wordt gevraagd.



![Image](assets/fr/11.webp)



Ashigaru is nu geïnstalleerd op uw telefoon.



## 3. De app initialiseren en een Bitcoin portfolio aanmaken



Selecteer `MAINNET` wanneer u de toepassing voor de eerste keer start.



![Image](assets/fr/12.webp)



Klik vervolgens op `Get Started`.



![Image](assets/fr/13.webp)



We gaan nu een nieuwe Bitcoin portfolio aanmaken. Druk op de knop `Maak een nieuwe wallet`.



![Image](assets/fr/14.webp)



### 3.1. creëer een Bitcoin portfolio



Ashigaru heeft een passphrase BIP39 nodig. Kies je passphrase en voer het in de juiste velden in. Het moet zo lang en willekeurig mogelijk zijn om een brute-force aanval te weerstaan.



Maak onmiddellijk een fysieke back-up van deze passphrase. Dit is een zeer belangrijke stap: als je je telefoon verliest, **als je deze passphrase niet meer hebt, heb je geen toegang meer tot je bitcoins** die opgeslagen zijn met je Ashigaru wallet. Deze passphrase wordt ook gebruikt om het wallet herstelbestand te versleutelen.



Als je niet weet wat een passphrase is, of niet volledig begrijpt hoe het werkt, raad ik je ten zeerste aan om deze extra handleiding te lezen. Dit is belangrijk, want de passphrase is een kritisch element van uw beveiliging: als u het verkeerd gebruikt, kan dit leiden tot het permanente verlies van uw fondsen.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Zodra je je passphrase hebt ingevoerd, klik je op `NEXT`.



![Image](assets/fr/15.webp)



Kies dan een pincode. Deze code wordt gebruikt om uw Ashigaru wallet te ontgrendelen en te beschermen tegen ongeautoriseerde fysieke toegang. Hij is niet betrokken bij de cryptografische afleiding van uw wallet sleutels. Dit betekent dat, zelfs zonder de PIN-code te kennen, iedereen met uw geheugensteuntje en passphrase weer toegang kan krijgen tot uw bitcoins.



Kies voor een lange, willekeurige pincode. Vergeet niet om een reservekopie op een andere locatie te bewaren dan je telefoon, om te voorkomen dat ze tegelijkertijd worden gecompromitteerd.



![Image](assets/fr/16.webp)



Zodra de PIN-code is aangemaakt, toont Ashigaru de mnemonische zin van je wallet. Waarschuwing: deze zin, gecombineerd met je passphrase, geeft volledige toegang tot je bitcoins. Iedereen die het in zijn bezit heeft, kan bezit nemen van je fondsen, zelfs als ze geen toegang hebben tot je telefoon. Deze 12-woordenreeks kan worden gebruikt om je wallet te herstellen in geval van verlies, diefstal of breuk van je telefoon. Het is daarom belangrijk om het met de grootste zorg op een fysieke drager (papier of metaal) te bewaren.



Bewaar deze zin nooit in digitale vorm, anders loop je het risico dat je geld wordt gestolen. Afhankelijk van je beveiligingsstrategie kun je meerdere fysieke kopieën maken, maar verdeel ze nooit. Bewaar de woorden in hun exacte volgorde en zorg ervoor dat ze genummerd zijn.



Tenslotte, bewaar de mnemonic en passphrase nooit op dezelfde plaats. Als beide tegelijk in gevaar komen, kan een aanvaller toegang krijgen tot je wallet.



![Image](assets/fr/17.webp)



Raadpleeg deze aanvullende tutorial voor meer informatie over het beveiligen van uw mnemonische zin:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Ashigaru vraagt je dan om je passphrase te herbevestigen. Maak van deze gelegenheid gebruik om te controleren of je fysieke back-up correct is.



![Image](assets/fr/18.webp)



### 3.2. een dojo aansluiten



Vervolgens moet je verbinding maken met je Dojo. Zoals uitgelegd in de inleiding, moet Ashigaru verbonden zijn met een Dojo om te kunnen communiceren met het Bitcoin netwerk.



Log in op de "Onderhoudstool" van je Dojo en open het menu `PAIRING`.



![Image](assets/fr/19.webp)



Druk op Ashigaru op de knop `Scan QR` en scan de QR-code die wordt weergegeven door uw DMT. Klik vervolgens op `Doorgaan` om te bevestigen.



![Image](assets/fr/20.webp)



Voer uw PIN-code in om de wallet te ontgrendelen. Dit brengt je naar de synchronisatiepagina. Het is normaal om in dit stadium *PayNym* fouten te zien, omdat de wallet nieuw is. Klik gewoon op `Doorgaan`.



![Image](assets/fr/21.webp)



Je wordt dan naar de startpagina van je portfolio gebracht.



![Image](assets/fr/22.webp)



Voordat je verder gaat, raad ik je aan om een testherstel uit te voeren terwijl de wallet nog geen bitcoin bevat. Zo kun je controleren of je papieren back-ups goed werken. Volg deze tutorial om uit te vinden hoe:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. De Ashigaru-toepassing instellen



Om de applicatie-instellingen te openen, klik je op de afbeelding van je *PayNym* in de linkerbovenhoek en selecteer je vervolgens `Instellingen`.



![Image](assets/fr/23.webp)



Hier vindt u verschillende opties om de werking van Ashigaru aan te passen aan uw behoeften. Ik raad u echter sterk aan om meteen vanaf het begin 2 belangrijke parameters te activeren.



Open eerst het menu `Veiligheid > Sluipmodus` en activeer deze functie als u die nodig hebt. Het verbergt de Ashigaru-toepassing achter de naam, het logo en de interface van een gewone toepassing die op uw telefoon is geïnstalleerd. Het doel is om te voorkomen dat iemand Ashigaru kan identificeren bij een fysieke inspectie van uw telefoon.



![Image](assets/fr/24.webp)



Elke nepapplicatie heeft een specifieke methode om de echte Ashigaru interface te ontgrendelen. Als je bijvoorbeeld de rekenmachine kiest, verdwijnt de Ashigaru-applicatie van je startscherm en wordt deze vervangen door een neprekenmachine. Als je die opent, zie je een klassieke werkende rekenmachine-interface, maar om toegang te krijgen tot Ashigaru hoef je alleen maar vijf keer snel op het `=`-symbool te tikken.



De tweede belangrijke parameter om te activeren is [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Met deze optie kun je de kosten van een transactie verhogen als deze vastloopt in de mempools omdat de kosten te laag zijn. Je kunt het activeren via het menu `Transacties > Uitgeven met RBF`.



![Image](assets/fr/25.webp)



Tip: Je kunt de weergave-eenheid van je portefeuille veranderen van `BTC` naar `sat` door simpelweg te klikken op het totale saldo dat wordt weergegeven op de startpagina.



## 5. Bitcoins ontvangen op Ashigaru



Nu je portefeuille operationeel is, kun je satss ontvangen. Druk hiervoor op de knop `+` rechtsonder in de interface en vervolgens op de groene knop `ontvangen`.



![Image](assets/fr/26.webp)



Ashigaru toont u dan het eerste ongebruikte ontvangstadres in uw wallet, om hergebruik van adressen te voorkomen (hergebruik van adressen is een zeer slechte praktijk voor uw privacy). Je kunt dit adres dan doorsturen naar de persoon of dienst die je bitcoins moet sturen.



![Image](assets/fr/27.webp)



Zodra de transactie is uitgezonden op het netwerk, verschijnt deze automatisch op de startpagina van de applicatie.



![Image](assets/fr/28.webp)



## 6. Bitcoins versturen met Ashigaru



Nu je bitcoins in je Ashigaru wallet hebt, kun je ze ook versturen. Druk daarvoor op de `+` knop rechtsonder en selecteer dan de rode `Verstuur` knop.



![Image](assets/fr/29.webp)



Kies vervolgens de account van waaruit je de uitgave wilt doen. Op dit moment hebben we nog niet de `Postmix` rekening behandeld, die gereserveerd is voor coinjoins, die we in een latere tutorial zullen bekijken. We gaan dus geld sturen vanaf de hoofdrekening.



![Image](assets/fr/30.webp)



Voer je transactiegegevens in: het te verzenden bedrag en het Bitcoin adres van de ontvanger.



![Image](assets/fr/31.webp)



Door op de drie kleine puntjes in de rechterbovenhoek te klikken en vervolgens op `Toon ongebruikte outputs`, kun je ook precies kiezen welke UTXO's je wilt uitgeven om je privacy te verbeteren.



![Image](assets/fr/32.webp)



Zodra je alle gegevens hebt ingevuld, klik je op de witte pijl onderaan de interface om verder te gaan.



Je komt dan op een overzichtspagina met alle details van je transactie. Er worden verschillende belangrijke elementen weergegeven:




- Controleer in het blok `Bestemming` nog een laatste keer of het adres van de ontvanger en het verzonden bedrag correct zijn;
- In het blok `Fees` kunt u het tarief bekijken dat automatisch door Ashigaru wordt geselecteerd en indien nodig wijzigen door op `MANAGE` te klikken;
- Het `Transaction` blok geeft het type transactie aan dat je gaat uitvoeren. Hier hebben we het over een eenvoudige transactie, maar Ashigaru ondersteunt ook andere soorten privacy-geoptimaliseerde transacties, die we in detail zullen behandelen in een toekomstige tutorial;
- Het rode blok `Transactie Alert` waarschuwt u als uw transactie patronen vertoont die kunnen worden herkend door de ketenanalyseprogramma's en die uw privacy in gevaar kunnen brengen. Door erop te klikken kunt u de details bekijken. In mijn geval vertelt Ashigaru me bijvoorbeeld dat het verzonden bedrag rond is (`3000 sats`), waardoor ik kan afleiden welke uitvoer overeenkomt met de uitgave en welke de uitwisseling is. Om meer te weten te komen over deze ketenanalyse heuristiek, nodig ik je uit om mijn BTC 204 training te volgen op Plan ₿ Academy ;
- Tot slot kun je een label toevoegen aan je transactie om het doel ervan bij te houden.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Zodra je alle informatie hebt gecontroleerd, gebruik je de groene pijl om de bitcoins te versturen. Houd de pijl ingedrukt en sleep hem naar rechts om de upload te bevestigen.



![Image](assets/fr/33.webp)



Uw transactie is uitgezonden op het Bitcoin netwerk.



![Image](assets/fr/34.webp)



## 7. Je Ashigaru wallet terugkrijgen



Het herstellen van een Ashigaru wallet verschilt een beetje van dat van een klassieke Bitcoin, omdat de applicatie dezelfde methodes gebruikt als Samurai Wallet. Als je de toegang tot je wallet verliest (omdat je je PIN bent vergeten, de installatie ongedaan hebt gemaakt of je telefoon bent kwijtgeraakt), zijn er verschillende manieren om je bitcoins terug te krijgen.



Als je nog toegang hebt tot je telefoon, of als je een back-up van dit bestand had gemaakt, is de eenvoudigste methode om het back-upbestand `ashigaru.txt` te gebruiken. Dit bestand bevat alle informatie die je nodig hebt om je portfolio te herstellen op een nieuwe instantie van Ashigaru (of op Sparrow Wallet), maar het is versleuteld met de passphrase die je in stap 3.1 van deze tutorial gedefinieerd hebt. Je moet dus zowel het `ashigaru.txt` bestand als je passphrase hebben om deze methode te gebruiken.



Met deze twee elementen kun je bijvoorbeeld je portfolio op Sparrow Wallet herstellen.



![Image](assets/fr/35.webp)



Als je geen toegang hebt tot het `ashigaru.txt` bestand, kun je nog steeds toegang krijgen tot je fondsen met behulp van je passphrase mnemonic phrase, net zoals je zou doen voor elke andere Bitcoin portefeuille. Ik raad aan dat u dit herstel uitvoert op een nieuwe Ashigaru instantie, of direct op Sparrow Wallet, om gemakkelijk de omleidingspaden van Whirlpool te herstellen als u die gebruikte. Als alternatief kunt u deze informatie in elke andere BIP39-compatibele software importeren door de afleidingspaden handmatig in te voeren.



Raadpleeg voor meer informatie over dit proces de complete tutorial die ik heb geschreven over het herstellen van een Wallet Samurai wallet. Aangezien Ashigaru een fork is, is de procedure identiek:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Zoals je ziet, welke herstelmethode je ook gebruikt, de passphrase is onmisbaar. Maak dus zorgvuldig een back-up. Je kunt ook meerdere kopieën maken, afhankelijk van je beveiligingsstrategie.



## 8. Toepassing bijwerken



Om de Ashigaru app bij te werken, moet je, omdat je hem hebt geïnstalleerd vanuit een `.apk` bestand en niet via de Play Store zoals een gewone app, het nieuwe `.apk` bestand downloaden dat overeenkomt met de bijgewerkte versie en vervolgens handmatig installeren.



Herhaal de stappen beschreven in deel 2 van deze tutorial, behalve dat wanneer je op het `.apk` bestand klikt om de installatie te starten, **je Android telefoon je de `Update` optie moet bieden, niet `Installeren`**.



![Image](assets/fr/41.webp)



Dit is een heel belangrijk punt: als Android `Installeren` weergeeft in plaats van `Updaten`, installeer je waarschijnlijk een frauduleuze versie. Onderbreek in dat geval onmiddellijk de installatieprocedure.



Net als bij de eerste installatie moet je de authenticiteit en integriteit van het `.apk` bestand controleren voordat je verder gaat met de update.



Om te weten te komen wanneer er een nieuwe versie beschikbaar is, kun je van tijd tot tijd de officiële Ashigaru website bezoeken. Wees gerust, Ashigaru is een stabiele, volwassen applicatie, geërfd van Samourai Wallet, en updates zijn relatief zeldzaam in vergelijking met jongere software.



## 9. Doneer aan het Ashigaru project



Ashigaru is een open-source project. Als u de ontwikkeling ervan wilt steunen, kunt u rechtstreeks vanuit de applicatie een donatie doen via PayNym.



Klik hiervoor op je PayNym rechtsboven in de interface en selecteer vervolgens je betaalcode die begint met `PM...`.



![Image](assets/fr/36.webp)



Druk vervolgens op de knop `+` rechtsonder in het scherm.



![Image](assets/fr/37.webp)



Selecteer `Ashigaru Open Source Project` als ontvanger.



![Image](assets/fr/38.webp)



Klik op de knop `CONNECT` om het BIP47-communicatiekanaal tot stand te brengen (meer over dit protocol in de tutorial hieronder).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Zodra de meldingstransactie is bevestigd, kun je je donaties naar het project sturen door op de kleine witte pijl in de rechterbovenhoek van de interface te klikken.



![Image](assets/fr/40.webp)



Je weet nu hoe je de basisfuncties van de Ashigaru-applicatie kunt gebruiken. In toekomstige tutorials zullen we kijken hoe je voordeel kunt halen uit geavanceerde uitgaven transacties, evenals Whirlpool, de coinjoin implementatie geërfd van Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
