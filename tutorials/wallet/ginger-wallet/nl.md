---
name: Ginger Wallet
description: Open-source, zelfbehoudende Bitcoin wallet software, fork van Wasabi Wallet, integratie van Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet is een open source, niet-custodial Bitcoin portfolio gericht op vertrouwelijkheid en privacy. Het begon zijn leven als fork van Wasabi Wallet (na versie 2.0.7.2 - MIT licentie).



Ginger Wallet behoudt Wasabi's technische architectuur, maar voegt enkele specifieke mogelijkheden toe. Volgens de [Ginger Wallet documentatie](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet) legt Wasabi de nadruk op **autonomie en controle**, terwijl Ginger zich richt op **eenvoudig gebruik, beveiliging en een vereenvoudigde ervaring**, waardoor het toegankelijk is voor mensen die minder bekend zijn met technische aspecten.



Ginger Wallet is wallet software alleen voor computers (geen mobiele toepassing).



## Wat is Coinjoin?



De **coinjoin** is een speciale Bitcoin transactiestructuur die verschillende deelnemers samenbrengt in één gezamenlijke transactie. Dit mechanisme mengt de invoer van verschillende gebruikers in een gemeenschappelijke transactie, waardoor het extreem moeilijk wordt - zo niet vaak onmogelijk, als het goed wordt gedaan - om fondsen te traceren. Hierdoor wordt het bijna onmogelijk voor een buitenstaander om met zekerheid de herkomst en bestemming van de betrokken bitcoins te achterhalen, in tegenstelling tot conventionele Bitcoin transacties.



Voor jou als gebruiker helpt coinjoin je vertrouwelijkheid te bewaren. Als je bijvoorbeeld een donatie van 10.000 sats ontvangt op een Bitcoin adres, kan de verzender deze fondsen traceren en, in sommige gevallen, afleiden dat je een grotere hoeveelheid bitcoins bezit, of je activiteiten observeren. Door na deze donatie van 10.000 sats een coinjoin te doen, verbreek je de traceerbaarheid: de verzender kan uit deze betaling geen informatie over jou meer afleiden.



De Chaumian coinjoin biedt een hoge mate van veiligheid, omdat de fondsen te allen tijde onder de exclusieve controle van de gebruiker blijven. Zelfs de beheerders van de coördinerende servers kunnen de bitcoins van de deelnemers onder geen enkele omstandigheid omleiden. Gebruikers noch coördinatoren hoeven elkaar te vertrouwen: ieder behoudt de controle over zijn of haar privésleutels en blijft als enige gemachtigd om transacties te valideren. Daarom kan geen enkele derde partij zich jouw bitcoins toe-eigenen tijdens een coinjoin, noch een directe link leggen tussen jouw inputs en outputs.



Om meer te leren over coinjoin, bekijk je de BTC 204-cursus van Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

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



Open Ginger Wallet, kies de taal van je voorkeur.



![screen](assets/fr/06.webp)



Ginger herinnert je vanaf het begin aan de kosten die het coinjoin-proces met zich meebrengt.



![screen](assets/fr/07.webp)



Druk vervolgens op **Start** en vervolgens op **Nieuw** om een nieuwe portfolio aan te maken.



![screen](assets/fr/08.webp)



Sla vervolgens je seedphrase op en bevestig.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Voor extra veiligheid biedt Ginger Wallet de optie om een passphrase toe te voegen.



![screen](assets/fr/11.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Deze passphrase zal, eenmaal toegevoegd, elke keer gevraagd worden wanneer je je portfolio probeert te openen.



![screen](assets/fr/12.webp)



Ginger activeert automatisch de standaard **Coinjoin** wanneer je je portefeuille aanmaakt. Je wordt hiervan op de hoogte gebracht en kunt dan de instelling aanpassen aan jouw behoeften.



![screen](assets/fr/13.webp)




### Algemene instellingen



Zodra je je eerste portfolio hebt aangemaakt, kom je in de interface van Ginger Wallet terecht.



![screen](assets/fr/14.webp)



Activeer de **Discrete modus** als je de saldi in je portemonnees wilt verbergen.



![screen](assets/fr/15.webp)



Je kunt meerdere portfolio's aanmaken op Ginger Wallet. Klik gewoon op **Een portfolio toevoegen**.



![screen](assets/fr/16.webp)



Ginger ondersteunt het gebruik van hardware portfolio's via de standaard Bitcoin Core interface, hoewel directe integratie van of naar een hardware portfolio nog niet beschikbaar is.



Compatibele hardwareportefeuilles omvatten (maar zijn niet beperkt tot) :




- Blokstroom Jade
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



Op dit tabblad kun je onder andere de taal, de valuta en de weergave-eenheid voor de kosten (BTC/Satoshi) wijzigen.



![screen](assets/fr/19.webp)





- Bitcoin**



Op dit tabblad kun je Bitcoin Knots inschakelen om te draaien bij het opstarten van de toepassing, je netwerk kiezen (Main/RegTest) en je laadtariefprovider (Mempool Space/Blockstream info/Full Node), enz.



![screen](assets/fr/20.webp)





- Veiligheidsfuncties**



Op het tabblad Beveiliging kun je twee-factor authenticatie inschakelen, Tor activeren of deactiveren en zelfs uitschakelen zodra de Ginger-toepassing is gesloten.



![screen](assets/fr/21.webp)



**NB** :




- Voor twee-factor authenticatie moet je ervoor zorgen dat je authenticatietoepassing het SHA256 protocol en 8-cijferige codes ondersteunt. Ginger Wallet vereist een 8-cijferige 2FA-code om de beveiliging te verbeteren. Dit langere formaat maakt het veel moeilijker om de code te raden of te kraken en biedt zo een betere bescherming tegen ongeautoriseerde toegang.
- Standaard gaat al het netwerkverkeer van Ginger via Tor, waardoor handmatige configuratie niet nodig is. Als Tor al actief is op je systeem, zal Ginger het automatisch prioriteit geven.



Maar zodra je Tor uitschakelt in de instellingen, blijft je privacy over het algemeen behouden, behalve in twee situaties:




- tijdens een Coinjoin zou de coördinator je inputs en outputs kunnen koppelen aan je IP-adres;
- wanneer je een transactie uitzendt, kan een kwaadwillende node waarmee je verbinding maakt je transactie associëren met je IP.



Vergeet niet elke keer op **Done** (rechtsonder) te drukken om je instellingen op te slaan. Sommige instellingen vereisen dat Ginger Wallet opnieuw wordt opgestart om van kracht te worden.



Bovendien kun je met de zoekbalk bovenaan de portfolio's elke parameter zoeken en openen, enz.



![screen](assets/fr/22.webp)




### Configuratie portefeuille



Er kunnen meerdere portfolio's worden aangemaakt in de applicatie, zodat elke portfolio kan worden geconfigureerd volgens uw behoeften. Klik hiervoor op de **drie puntjes** voor de naam van de portfolio en vervolgens op **Portefeuille-instellingen**.



![screen](assets/fr/23.webp)



Zoals je kunt zien, kun je behalve de wallet parameter ook je UTXO's (lijst van tokens die je bezit), statistieken en wallet informatie (bijvoorbeeld de uitgebreide publieke sleutel) zien.



Om terug te keren naar onze portefeuilleconfiguratie, klik je op portefeuilleparameters en kom je op de volgende tabbladen:




- Algemeen** (waar je de naam van de portefeuille kunt wijzigen) ;



![screen](assets/fr/24.webp)





- Coinjoin** (waar je de coinjoin-instellingen voor deze wallet kunt aanpassen) ;



![screen](assets/fr/25.webp)





- Tools** (waar je je seedphrase kunt controleren, je portfolio opnieuw kunt synchroniseren of verwijderen).



![screen](assets/fr/26.webp)




## Bitcoins ontvangen



![video](https://youtu.be/cqv35wBDWMQ)



Om bitcoins te ontvangen in je wallet op Ginger Wallet:




- druk op **Ontvangen** ;



![screen](assets/fr/27.webp)





- Voer de naam in van de bron waaraan je het adres wilt koppelen. Dit is labeling om je betalingen bij te houden. Dit heeft geen on-chain implicaties; het is gewoon traceerbaarheidsinformatie die lokaal in je applicatie is opgeslagen;



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- klik op het pijltje links van **Genereren** om je adresformaat te kiezen (**SegWit** /**Taproot**), klik dan op **Genereren**, om generate een adres en QR-code te maken.



![screen](assets/fr/29.webp)



Dit adres of deze QR-code wordt door de afzender gebruikt om je bitcoins te sturen.



![screen](assets/fr/30.webp)




## Bitcoins versturen




![video](https://youtu.be/2nf5aAimfhg)



Om dit te doen :




- Druk op de knop **Versturen**;
- voer het adres van de ontvanger in, het bedrag dat moet worden verzonden en een label;
- controleer het transactieoverzicht en bevestig om te verzenden.



![screen](assets/fr/31.webp)




## Bitcoins uitgeven



Het is gemakkelijk om Bitcoin te kopen en verkopen met Ginger Wallet. In slechts een paar stappen kun je je bitcoins uitgeven.



### Bitcoins kopen



![video](https://youtu.be/lEqTBzm5MEA)



Ginger Wallet gebruikers kunnen bitcoins kopen.





- Druk op de **Koop** knop. Deze knop blijft zichtbaar, zelfs als de wallet leeg is.



![screen](assets/fr/32.webp)





- Selecteer je land, of zelfs je staat (in sommige regio's zoals Canada), voordat je verder gaat met een bitcoin aankoop. Als je voor de eerste keer op de **Koop** functie klikt, moet je ook je regio opgeven.



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



In de rechterbovenhoek van het scherm, met het label **Alle**, kun je aanbiedingen filteren op betaalmethode. De door jou geselecteerde betaalmethode wordt standaard ingesteld, maar kan op elk moment worden gewijzigd.



![screen](assets/fr/36.webp)



Als je een geschikt aanbod vindt, klik je op de knop **Aanvaarden** om door te gaan met de aankoop. Je wordt dan doorgestuurd naar de pagina van de verkoper, waar je de transactie kunt afronden.



### Bitcoins verkopen



Ginger Wallet gebruikers kunnen Bitcoin verkopen. De **Verkoop** knop is alleen zichtbaar als er geld beschikbaar is in de portefeuille.





- Klik op **Verkopen**.



![screen](assets/fr/37.webp)





- Net als bij de **Koop** optie moet je, wanneer je de Verkoopfunctie voor de eerste keer gebruikt, je land selecteren voordat je verder gaat met een Bitcoin verkoop.





- Vervolgens moet u het aantal Bitcoins invoeren dat u wilt verkopen. U kunt dit bedrag invoeren in BTC of in een fiatvaluta zoals de Amerikaanse dollar (USD).





- Zodra je dit hebt gedaan, zie je een lijst met beschikbare aanbiedingen. Kies een aanbieding die bij je past en klik op **Aanvaarden** om verder te gaan.





- Nu moet je de transactie afronden:
 - Zodra je een aanbieding hebt geaccepteerd, word je doorgestuurd naar de pagina van de leverancier;
 - Volg de instructies op de leverancierspagina ;
 - Op een bepaald moment ontvang je een ontvangstadres en het exacte bedrag dat je moet sturen;
 - Ga dan terug naar Ginger Wallet om het proces voort te zetten;
 - Eenmaal terug in Ginger Wallet, verschijnt er een dialoogvenster waarmee je verder kunt gaan door op **Versturen** te klikken.



Hierdoor wordt het scherm **Versturen** geopend waarin het adres en het bedrag van de ontvanger al zijn ingevuld. Je kunt ook de knop **Versturen** op het beginscherm gebruiken. Hoewel je de transactie handmatig kunt verzenden, raden we je aan om deze via het dialoogvenster te voltooien voor een optimaal proces.



## Een coinjoin maken op Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Bescherm de vertrouwelijkheid van je bitcoins met **Coinjoin**, direct geïntegreerd in Ginger Wallet. De wallet gebruikt **WabiSabi**, een Chaumian coinjoin protocol dat is ontworpen om meer toegankelijke en efficiënte coinjoins te faciliteren.



Het is aan jou om de coinjoin-strategie (automatisch of handmatig) te kiezen die het beste bij je past.



Ginger Coinjoin is klaar voor gebruik zodra je het hebt gedownload (geen extra stappen nodig). Ginger Coinjoin draait automatisch op de achtergrond om je privacy bij elke transactie te beschermen. In de praktijk zal de Coinjoin speler verschijnen wanneer je een saldo hebt dat geanonimiseerd kan worden.



Wat betreft het handmatig opstarten van coinjoin, dat kan met één klik. Start de ronde en wacht tot de coinjoin transactie is opgebouwd en bevestigd. Je ziet de anonimiseringsscore in de interface.



Er kunnen meerdere mixen worden uitgevoerd tot het gewenste niveau van anonimiteit is bereikt. Je kunt ook bepaalde delen uitsluiten van de mix.



Standaard gebruikt Ginger zijn eigen coördinator met alle voorgeconfigureerde parameters en gegarandeerde vergoedingen. Coinjoins van tokens met een waarde van meer dan 0,03 BTC hebben een coördinatorvergoeding van 0,3% bovenop de mining vergoeding. Inschrijvingen van 0,03 BTC of minder, evenals remixen, zijn vrijgesteld van coördinator vergoedingen, zelfs na een enkele transactie. Daarom stelt een betaling met Coinjoin-fondsen zowel verzender als ontvanger in staat om hun munten te remixen zonder coördinatorkosten.



Ginger verkiest coinjoins met meer deelnemers boven kleinere, snellere rondes. Grotere coinjoins bieden meer anonimiteit, lagere kosten en een grotere efficiëntie van de blokruimte.




## Veiligheid en best practices



De wens tot decentralisatie en het behoud van privacy vereisen de toepassing van verschillende best practices:




- Bewaar uw seedphrase altijd op een veilige plaats off-line;
- Als u uw computer verliest of onbevoegde toegang vermoedt, maak dan onmiddellijk een nieuwe wallet aan. Zet uw fondsen over naar deze nieuwe portefeuille en verwijder de oude;
- Gebruik voor elke ontvangst een ander adres om hergebruik van adressen te voorkomen;
- Download je portfolioapplicaties altijd uitsluitend van het officiële GitHub account of de officiële website.



Nu ben je vertrouwd met het gebruik van de Ginger Wallet applicatie om je bitcoins te versturen, ontvangen en uit te geven.



Als je deze tutorial nuttig vond, laat dan hieronder een groene duim achter. Voel je vrij om dit artikel te delen via je sociale media. Heel erg bedankt!



Ik raad je ook aan om deze tutorial te bekijken over hoe je de Liana computerapplicatie kunt gebruiken om bitcoins te versturen en ontvangen, en om een geautomatiseerd nalatenschapsplan te implementeren.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04