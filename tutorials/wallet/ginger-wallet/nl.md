---
name: Gember Wallet
description: Open-source, zelfbehoudende Bitcoin Wallet software, Fork van Wasabi Wallet, integratie van Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet is een open source, niet-custodial Bitcoin portfolio gericht op vertrouwelijkheid en privacy. Het begon zijn leven als Fork van Wasabi Wallet (na versie 2.0.7.2 - MIT licentie).



Ginger Wallet behoudt Wasabi's technische architectuur, maar voegt enkele specifieke mogelijkheden toe. Volgens de [Ginger Wallet documentatie](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet) legt Wasabi de nadruk op **autonomie en controle**, terwijl Ginger zich richt op **eenvoudig gebruik, beveiliging en een vereenvoudigde ervaring**, waardoor het toegankelijk is voor mensen die minder bekend zijn met technische aspecten.



Ginger Wallet is Wallet software alleen voor computers (geen mobiele toepassing).



## Wat is CoinJoin?



CoinJoin** is een bepaald type Bitcoin transactiestructuur die meerdere deelnemers samenbrengt in één gezamenlijke transactie. Dit mechanisme mengt de invoer van verschillende gebruikers in een gemeenschappelijke transactie, waardoor het extreem moeilijk wordt - zo niet vaak onmogelijk als het goed wordt gedaan - om fondsen te traceren. Hierdoor wordt het bijna onmogelijk voor een buitenstaander om met zekerheid de herkomst en bestemming van de betrokken bitcoins te bepalen, in tegenstelling tot conventionele Bitcoin transacties.



Voor u, de gebruiker, helpt CoinJoin uw vertrouwelijkheid te bewaren. Als je bijvoorbeeld een donatie van 10.000 Sats ontvangt op een Bitcoin Address, kan de verzender deze fondsen traceren en, in sommige gevallen, afleiden dat je een grotere hoeveelheid bitcoins bezit, of je activiteiten observeren. Door na deze donatie van 10.000 Sats een CoinJoin te maken, verbreek je de traceerbaarheid: de verzender kan uit deze betaling geen informatie over jou meer afleiden.



De Chaumian CoinJoin biedt een hoge mate van veiligheid, omdat de fondsen te allen tijde onder de exclusieve controle van de gebruiker blijven. Zelfs de beheerders van de coördinerende servers kunnen de bitcoins van de deelnemers onder geen enkele omstandigheid omleiden. Gebruikers noch coördinatoren hoeven elkaar te vertrouwen: ieder behoudt de controle over zijn of haar privésleutels en blijft als enige gemachtigd om transacties te valideren. Geen enkele derde partij kan zich dus uw bitcoins toe-eigenen tijdens een CoinJoin, noch een directe link leggen tussen uw inputs en outputs.



Om meer te leren over CoinJoin, bekijk je de BTC 204-cursus van Plan ₿ Academy:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ginger Wallet installeren



Om Ginger Wallet te installeren, bezoek je de website [Ginger Wallet](https://gingerwallet.io).



Druk op **Download** om de juiste versie voor je computer te downloaden (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Een andere optie is om naar de [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) van het project te gaan om het te downloaden.



![screen](assets/fr/04.webp)



Voer vervolgens het installatieprogramma uit.



![screen](assets/fr/05.webp)




## Parameterinstellingen



### Voorlopige configuraties



Open Ginger Wallet, kies de gewenste taal.



![screen](assets/fr/06.webp)



Ginger herinnert je vanaf het begin aan de kosten die het CoinJoin proces met zich meebrengt.



![screen](assets/fr/07.webp)



Druk vervolgens op **Start** en vervolgens op **Nieuw** om een nieuwe portfolio aan te maken.



![screen](assets/fr/08.webp)



Sla vervolgens je seedphrase op en bevestig.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Voor extra veiligheid biedt de Ginger Wallet de mogelijkheid om een passphrase toe te voegen.



![screen](assets/fr/11.webp)



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Deze passphrase zal, eenmaal toegevoegd, telkens gevraagd worden wanneer je je portfolio probeert te openen.



![screen](assets/fr/12.webp)



Ginger activeert automatisch de standaard **CoinJoin** wanneer je je portfolio aanmaakt. Je wordt hiervan op de hoogte gebracht en kunt dan de instelling aanpassen aan jouw behoeften.



![screen](assets/fr/13.webp)




### Algemene instellingen



Zodra je je eerste portfolio hebt gemaakt, ga je naar Ginger's Interface Wallet.



![screen](assets/fr/14.webp)



Activeer de **Discrete modus** als je de saldi in je portemonnees wilt verbergen.



![screen](assets/fr/15.webp)



Je kunt meerdere portfolio's aanmaken op Ginger Wallet. Klik gewoon op **Een portfolio toevoegen**.



![screen](assets/fr/16.webp)



Ginger ondersteunt het gebruik van hardware portfolio's via de Bitcoin core standaard Interface, hoewel directe integratie van of naar een hardware portfolio nog niet beschikbaar is.



Compatibele hardwareportefeuilles omvatten (maar zijn niet beperkt tot) :




- BLOCKSTREAM Jade
- Coldcard MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Model T
- Trezor Safe 3
- enz.



Klik nu op **Instellingen**.



![screen](assets/fr/17.webp)



Deze instellingen gelden voor de applicatie in het algemeen en de instellingen die u hier maakt, gelden voor alle portfolio's.



In **Instellingen** heb je de tabbladen :





- Algemeen**



![screen](assets/fr/18.webp)





- Uiterlijk



Op dit tabblad kunt u onder andere de taal, de valuta en de weergave-eenheid voor kosten (BTC/Satoshi) wijzigen.



![screen](assets/fr/19.webp)





- Bitcoin**



Op dit tabblad kun je Bitcoin Knots inschakelen om te draaien wanneer de toepassing start, je netwerk kiezen (Main/RegTest) en je laadtariefprovider (Mempool Space/BLOCKSTREAM info/Full node), enz.



![screen](assets/fr/20.webp)





- Veiligheidsfuncties**



Op het tabblad Beveiliging kun je twee-factor authenticatie inschakelen, Tor activeren of deactiveren en zelfs uitschakelen zodra de Ginger-toepassing is gesloten.



![screen](assets/fr/21.webp)



**NB** :




- Voor twee-factor authenticatie moet je ervoor zorgen dat je authenticatietoepassing het SHA256 protocol en 8-cijferige codes ondersteunt. Ginger Wallet vereist een 8-cijferige 2FA-code voor verbeterde beveiliging. Dit langere formaat maakt het veel moeilijker om de code te raden of te kraken en biedt zo een betere bescherming tegen ongeautoriseerde toegang.
- Standaard gaat al het netwerkverkeer van Ginger via Tor, waardoor handmatige configuratie niet nodig is. Als Tor al actief is op je systeem, zal Ginger het automatisch prioriteit geven.



Maar zodra je Tor uitschakelt in de instellingen, blijft je privacy over het algemeen behouden, behalve in twee situaties:




- tijdens een CoinJoin kan de coördinator je in- en uitgangen koppelen aan je IP Address;
- wanneer je een transactie uitzendt, kan een kwaadwillende node waarmee je verbinding maakt je transactie associëren met je IP.



Vergeet niet om elke keer op **Done** (rechtsonder in Coin) te drukken, om uw instellingen op te slaan. Sommige instellingen vereisen dat Ginger Wallet opnieuw wordt opgestart om van kracht te worden.



Bovendien kun je met de zoekbalk bovenaan de portfolio's elke parameter zoeken en openen, enz.



![screen](assets/fr/22.webp)




### Configuratie portefeuille



Er kunnen meerdere portfolio's worden aangemaakt in de applicatie, zodat elke portfolio kan worden geconfigureerd volgens uw behoeften. Klik hiervoor op de **drie puntjes** voor de naam van de portfolio en vervolgens op **Portefeuille-instellingen**.



![screen](assets/fr/23.webp)



Zoals je kunt zien, kun je behalve de Wallet parameter ook je UTXO's (lijst van tokens die je bezit), statistieken en Wallet informatie (bijvoorbeeld de uitgebreide publieke sleutel) zien.



Om terug te keren naar onze portefeuilleconfiguratie, klik je op portefeuilleparameters en kom je op de volgende tabbladen:




- Algemeen** (waar je de naam van de portefeuille kunt wijzigen) ;



![screen](assets/fr/24.webp)





- CoinJoin** (waar je de CoinJoin instellingen van deze portefeuille kunt aanpassen) ;



![screen](assets/fr/25.webp)





- Tools** (waar je je seedphrase kunt controleren, je portfolio opnieuw kunt synchroniseren of verwijderen).



![screen](assets/fr/26.webp)




## Bitcoins ontvangen



Om bitcoins te ontvangen in uw Wallet op Ginger Wallet :




- druk op **Ontvangen** ;



![screen](assets/fr/27.webp)





- Voer de naam in van de bron waaraan je de Address wilt koppelen. Dit is labeling om uw betalingen bij te houden. Dit heeft geen On-Chain implicaties; het is gewoon traceerbaarheidsinformatie die lokaal in uw toepassing is opgeslagen;



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- klik op het kleine pijltje links van **generate** om jouw Address formaat te kiezen (**SegWit** /**Taproot**), klik dan op **generate**, om generate een Address en QR code.



![screen](assets/fr/29.webp)



Deze Address of QR-code wordt door je afzender gebruikt om je bitcoins te sturen.



![screen](assets/fr/30.webp)




## Bitcoins versturen



Video tutorial over het verzenden via Ginger Wallet.



![Vidéo](https://youtu.be/2nf5aAimfhg)



Om dit te doen :




- Druk op de knop **Versturen**;
- voer de Address van de ontvanger in, het bedrag dat moet worden verzonden en een label;
- controleer het transactieoverzicht en bevestig om te verzenden.



![screen](assets/fr/31.webp)




## Bitcoins uitgeven



Het is gemakkelijk om Bitcoin te kopen en verkopen met Ginger Wallet. In slechts een paar stappen kun je je bitcoins uitgeven.



### Bitcoins kopen



Ginger Wallet gebruikers kunnen bitcoins kopen.





- Druk op de **Koop** knop. Deze knop blijft zichtbaar, zelfs als de Wallet leeg is.



![screen](assets/fr/32.webp)





- Selecteer je land, of zelfs je staat (in sommige regio's, zoals Canada), voordat je verder gaat met een Bitcoin aankoop. Wanneer je voor de eerste keer op de **Koop** functie klikt, moet je ook je regio opgeven.



![screen](assets/fr/33.webp)



Druk op **Doorgaan** om het aankoopproces te doorlopen.





- Voer vervolgens in het daarvoor bestemde veld het aantal bitcoins in dat je wilt kopen. Je kunt ook de transactievaluta kiezen.



![screen](assets/fr/34.webp)



Elke valuta heeft een minimum en maximum aankooplimiet. In USD is de maximale limiet bijvoorbeeld $30.000.



Als je al een aankoop hebt gedaan, kun je je transactiegeschiedenis bekijken door op de knop **Eerdere bestellingen** te klikken. Er wordt een lijst met eerdere transacties en hun status weergegeven.





- Kies de aanbieding die bij je past.



Op dit punt zie je een lijst met alle beschikbare aanbiedingen. Voor elke aanbieding heb je :




 - naam leverancier (1) ;
 - het aantal bitcoins dat overeenkomt met het eerder ingevoerde bedrag, de betalingsmethode en de aankoopkosten (2) ;
 - de knop **Accept** (3).



![screen](assets/fr/35.webp)



De kosten die in de offerte worden vermeld, vormen geen extra kosten. Ze zijn al inbegrepen in het totaalbedrag van de offerte.



Rechtsboven Coin van het scherm met het label **Alle** kun je aanbiedingen filteren op betaalmethode. De door jou geselecteerde betaalmethode wordt standaard ingesteld, maar kan op elk moment worden gewijzigd.



![screen](assets/fr/36.webp)



Als je een geschikt aanbod vindt, klik je op de knop **Aanvaarden** om door te gaan met de aankoop. Je wordt dan doorgestuurd naar de pagina van de verkoper, waar je de transactie kunt afronden.



### Bitcoins verkopen



Ginger Wallet gebruikers kunnen Bitcoin verkopen. De **Verkoop** knop is alleen zichtbaar als er geld beschikbaar is in de portefeuille.





- Klik op **Verkopen**.



![screen](assets/fr/37.webp)





- Net als bij de **Koop** optie, moet je, wanneer je de Verkoopfunctie voor de eerste keer gebruikt, je land selecteren voordat je verder gaat met een Bitcoin verkoop.





- Vervolgens moet u het aantal Bitcoins invoeren dat u wilt verkopen. U kunt dit bedrag invoeren in BTC of in een fiatvaluta zoals de Amerikaanse dollar (USD).





- Zodra je dit hebt gedaan, zie je een lijst met beschikbare aanbiedingen. Kies een aanbieding die bij je past en klik op **Aanvaarden** om verder te gaan.





- Nu moet je de transactie afronden:
 - Zodra je een aanbieding hebt geaccepteerd, word je doorgestuurd naar de pagina van de leverancier;
 - Volg de instructies op de leverancierspagina ;
 - Op een bepaald moment ontvang je een ontvanger Address en het exacte bedrag dat je moet sturen;
 - Ga dan terug naar Ginger Wallet om het proces voort te zetten;
 - Eenmaal terug in Ginger Wallet, verschijnt er een dialoogvenster waarmee je verder kunt gaan door op **Versturen** te klikken.



Dit opent het **Verstuur** scherm met de Address en het bedrag van de ontvanger al ingevuld. U kunt ook de knop **Versturen** op het beginscherm gebruiken. Hoewel je de transactie handmatig kunt verzenden, raden we je aan om het via het dialoogvenster te doen voor een optimaal proces.



## Maak een CoinJoin op Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Bescherm de vertrouwelijkheid van je bitcoins met **CoinJoin**, direct geïntegreerd in Ginger Wallet. De Wallet gebruikt **WABISABI**, een Chaumian CoinJoin protocol, ontworpen om meer toegankelijke en efficiënte coinjoins mogelijk te maken.



Het is aan jou om de CoinJoin strategie (automatisch of handmatig) te kiezen die het beste bij je past.



Ginger CoinJoin is klaar voor gebruik zodra je het downloadt (geen extra stappen nodig). Ginger CoinJoin draait automatisch op de achtergrond om je privacy bij elke transactie te beschermen. In de praktijk verschijnt de CoinJoin lezer telkens wanneer je een saldo hebt dat geanonimiseerd kan worden.



Wat het handmatig opstarten van CoinJoin betreft, dat gaat met één klik. Start de ronde en wacht tot de CoinJoin transactie is opgebouwd en bevestigd. Je ziet de anonimiseringsscore in Interface.



Er kunnen meerdere mixen worden uitgevoerd tot het gewenste niveau van anonimiteit is bereikt. Je kunt ook bepaalde delen uitsluiten van de mix.



Standaard gebruikt Ginger zijn eigen coördinator met alle voorgeconfigureerde parameters en gegarandeerde vergoedingen. Coinjoins van tokens met een waarde van meer dan 0,03 BTC brengen 0,3% coördinatorvergoeding met zich mee bovenop de Mining vergoeding. Inschrijvingen van 0,03 BTC of minder, evenals remixen, zijn vrijgesteld van coördinator vergoedingen, zelfs na een enkele transactie. Daarom staat een betaling met CoinJoin fondsen zowel verzender als ontvanger toe om hun munten te remixen zonder coördinator kosten.



Ginger geeft de voorkeur aan coinjoins met meer deelnemers boven kleinere, snellere rondes. Grotere coinjoins bieden meer anonimiteit, lagere kosten en een grotere efficiëntie van de BLOCK ruimte.




## Veiligheid en best practices



De wens tot decentralisatie en het behoud van privacy vereisen de toepassing van verschillende best practices:




- Bewaar uw seedphrase altijd op een veilige plaats off-line;
- Als u uw computer verliest of onbevoegde toegang vermoedt, maak dan onmiddellijk een nieuwe Wallet aan. Breng uw fondsen over naar deze nieuwe portefeuille en verwijder de oude;
- Gebruik voor elke ontvangst een andere Address om hergebruik van adressen te voorkomen;
- Download je portfolioapplicaties altijd uitsluitend van het officiële GitHub account of de officiële website.



Nu ben je bekend met het gebruik van de Ginger Wallet applicatie om je bitcoins te versturen, ontvangen en uit te geven.



Als je deze tutorial nuttig vond, laat dan hieronder een Green duimpje achter. Voel je vrij om dit artikel te delen via je sociale media. Heel erg bedankt!



Ik raad je ook aan om deze tutorial te bekijken over hoe je de Liana computerapplicatie kunt gebruiken om bitcoins te versturen en ontvangen, en om een geautomatiseerd nalatenschapsplan te implementeren.



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04