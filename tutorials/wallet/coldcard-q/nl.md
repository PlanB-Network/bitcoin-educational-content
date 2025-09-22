---
name: COLDCARD Q
description: Een COLDCARD instellen en gebruiken Q
---
![cover](assets/cover.webp)


Een Hardware Wallet is een elektronisch apparaat dat de private sleutels van een Bitcoin Wallet beheert en beveiligt. In tegenstelling tot software wallets (of Hot wallets) die geïnstalleerd zijn op algemene machines die vaak verbonden zijn met het internet, maken hardware wallets het mogelijk om private sleutels fysiek te isoleren, wat het risico op piraterij en diefstal vermindert.


Het belangrijkste doel van een Hardware Wallet is om de functionaliteit van het apparaat zoveel mogelijk te beperken om het aanvalsoppervlak te minimaliseren. Minder aanvalsoppervlak betekent ook minder potentiële aanvalsvectoren, d.w.z. minder zwakke punten in het systeem die aanvallers zouden kunnen uitbuiten om toegang te krijgen tot bitcoins.


Het is raadzaam om een Hardware Wallet te gebruiken om je bitcoins te beveiligen, vooral als je grote hoeveelheden hebt, in absolute waarde of als deel van je totale vermogen.


Hardware wallets worden gebruikt in combinatie met Wallet beheersoftware op een computer of smartphone. Deze laatste beheert het aanmaken van transacties, maar de cryptografische handtekening die nodig is om deze transacties geldig te maken, wordt uitsluitend binnen de Hardware Wallet uitgevoerd. Dit betekent dat privé-sleutels nooit worden blootgesteld aan een potentieel kwetsbare omgeving.


Hardware wallets bieden een dubbele bescherming voor de gebruiker: aan de ene kant beveiligen ze je bitcoins tegen aanvallen op afstand door de privésleutels offline te houden, en aan de andere kant bieden ze over het algemeen een grotere fysieke weerstand tegen pogingen om de sleutels te ontfutselen. En het is precies op deze 2 veiligheidscriteria dat we de verschillende modellen op de markt kunnen beoordelen en classificeren.


In deze tutorial wil ik je kennis laten maken met zo'n oplossing: de **COLDCARD Q**.


---
Omdat de COLDCARD Q een veelheid aan functies biedt, stel ik voor om het gebruik ervan op te splitsen in 2 tutorials. In deze eerste tutorial kijken we naar de eerste configuratie en basisfuncties van het apparaat. Daarna, in een tweede tutorial, bekijken we hoe je gebruik kunt maken van alle geavanceerde opties van je COLDCARD.


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

---
## Kennismaking met COLDCARD Q


De COLDCARD Q is een Bitcoin Hardware Wallet ontwikkeld door het Canadese bedrijf Coinkite, bekend van de eerdere MK modellen. De Q is hun meest geavanceerde product tot nu toe en wordt gepositioneerd als de ultieme Bitcoin Hardware Wallet.


Qua hardware is de COLDCARD Q uitgerust met alle functies die nodig zijn voor een optimale gebruikerservaring:




- Een groot LCD-scherm vereenvoudigt navigatie en bediening;
- Een volledig QWERTY-toetsenbord;
- Geïntegreerde camera voor het scannen van QR-codes;
- Twee microSD-kaartsleuven ;
- Een volledig geïsoleerde voedingsoptie via drie AAA-batterijen (niet meegeleverd) of via een USB-C-kabel ;
- Twee Secure Elements van twee verschillende fabrikanten voor extra veiligheid;
- De mogelijkheid om te communiceren via NFC.


Naar mijn mening heeft de COLDCARD Q maar twee nadelen. Ten eerste is hij door zijn vele functies vrij volumineus. Hij meet bijna 13 cm lang en 8 cm breed, wat bijna het formaat van een kleine smartphone is. Hij is ook vrij dik vanwege het batterijcompartiment. Als je op zoek bent naar een kleinere, mobielere Hardware Wallet, dan is de veel compactere MK4 misschien een betere optie. Het tweede nadeel is natuurlijk de prijs van het apparaat, die op de officiële website **$239,99** kost, dat is $72 meer dan de MK4, waardoor de Q rechtstreeks concurreert met premium hardware wallets zoals de Ledger Flex of Foundation's Passport.


![CCQ](assets/fr/001.webp)


Aan de softwarekant is de COLDCARD Q net zo goed uitgerust als de andere apparaten van Coinkite, met een groot aantal geavanceerde functies:




- Dobbel om generate je eigen herstelzin te geven;
- PIN-code ;
- Aftellen tot laatste PIN-slot ;
- BIP39 passphrase ;
- Definitieve sluitpin ;
- Aftellen verbinding ;
- SeedXOR;
- BIP85...


Kortom, de COLDCARD Q biedt een verbeterde gebruikerservaring ten opzichte van de MK4 en kan ideaal zijn voor gemiddelde tot gevorderde gebruikers die op zoek zijn naar meer gebruiksgemak.


De COLDCARD Q is te koop [op de officiële website van Coinkite] (https://store.coinkite.com/store/coldcard). Hij kan ook worden gekocht bij een detailhandelaar.


## De zelfstudie voorbereiden


Als je je COLDCARD hebt ontvangen, is de eerste stap om de verpakking te inspecteren om er zeker van te zijn dat deze niet geopend is. Als de verpakking beschadigd is, kan dit erop wijzen dat de Hardware Wallet beschadigd is en misschien niet echt is.


![CCQ](assets/fr/002.webp)


Als je de doos opent, moet je de volgende items vinden:




- De COLDCARD Q in een verzegelde zak;
- Een kaart om je Mnemonic zin op te schrijven.


![CCQ](assets/fr/003.webp)


Zorg ervoor dat de zak niet is opengemaakt of beschadigd. Controleer ook of het nummer op de zak overeenkomt met het nummer op het papier in de zak. Bewaar dit nummer voor toekomstig gebruik.


![CCQ](assets/fr/004.webp)


Als je je COLDCARD liever van stroom voorziet zonder hem op een computer aan te sluiten (air-gap), stop dan drie AAA-batterijen in de achterkant van het apparaat. Je kunt hem ook op je computer aansluiten via een USB-C kabel.


![CCQ](assets/fr/005.webp)


Voor deze tutorial heb je ook Sparrow wallet nodig om je Bitcoin Wallet op je computer te beheren. Download [Sparrow wallet](https://sparrowwallet.com/download/) van de officiële website. Ik raad je sterk aan om zowel de authenticiteit (met GnuPG) als de integriteit (via Hash) te controleren voordat je verder gaat met de installatie. Als je niet weet hoe je dit moet doen, volg dan deze tutorial:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## PIN-code selecteren


Je kunt nu je COLDCARD inschakelen door op de knop linksboven te drukken.


![CCQ](assets/fr/006.webp)


Druk op de knop "*ENTER*" om de gebruiksvoorwaarden te accepteren.


![CCQ](assets/fr/007.webp)


Je COLDCARD Q toont dan een nummer bovenaan het scherm. Controleer of dit nummer overeenkomt met het nummer op de verzegelde zak en op het stuk plastic in de zak. Zo weet je zeker dat je pakket niet is geopend tussen het moment dat het door Coinkite werd verpakt en het moment dat jij het opende. Druk op "*ENTER*" om verder te gaan.


![CCQ](assets/fr/008.webp)


Navigeer naar het menu "*Choose PIN Code*" en bevestig met de knop "*ENTER*".


![CCQ](assets/fr/009.webp)


Deze PIN-code wordt gebruikt om je COLDCARD te ontgrendelen. Het is daarom een bescherming tegen ongeautoriseerde fysieke toegang. Deze PIN-code is niet betrokken bij de afleiding van de cryptografische sleutels van uw Wallet. Dus zelfs zonder toegang tot deze PIN-code, kunt u met het bezit van uw Mnemonic zin weer toegang krijgen tot uw bitcoins.


PIN-codes voor COLDCARDs bestaan uit twee delen: een prefix en een suffix, die elk 2 tot 6 cijfers kunnen bevatten, voor een totaal van 4 tot 12 cijfers. Wanneer je je COLDCARD ontgrendelt, moet je eerst de prefix invoeren, waarna het apparaat je 2 woorden laat zien. Voer vervolgens het achtervoegsel in. Deze twee woorden krijg je tijdens deze configuratiestap en moet je zorgvuldig bewaren, want je hebt ze elke keer nodig als je je COLDCARD ontgrendelt. Als de twee woorden die tijdens het ontgrendelen worden weergegeven overeenkomen met de woorden die je tijdens de configuratie hebt opgeslagen, dan bevestigt dit dat je apparaat niet gecompromitteerd is sinds het voor het laatst is gebruikt.


Klik opnieuw op "*Kies PIN*"


![CCQ](assets/fr/010.webp)


Bevestig dat u de waarschuwingen hebt gelezen.


![CCQ](assets/fr/011.webp)


U kiest nu uw pincode. Wij raden een lange, willekeurige PIN-code aan. Zorg ervoor dat je deze code op een andere plaats bewaart dan waar je COLDCARD is opgeslagen. Je kunt de bijgeleverde kaart gebruiken om deze code op te slaan.


Voer de prefix van uw keuze in en druk vervolgens op de knop "*ENTER*" om het eerste deel van de PIN-code te bevestigen.


![CCQ](assets/fr/012.webp)


De twee anti-phishing woorden worden dan op je scherm weergegeven. Bewaar ze zorgvuldig voor toekomstig gebruik. Je kunt het kaartje in je pakket gebruiken om ze op te schrijven.


![CCQ](assets/fr/013.webp)


Voer vervolgens het tweede deel van uw PIN-code in en druk op "*ENTER*".


![CCQ](assets/fr/014.webp)


Bevestig uw pincode door deze een tweede keer in te voeren en controleer of de twee anti-phishing woorden overeenkomen met de woorden die u eerder hebt opgeslagen.


![CCQ](assets/fr/015.webp)


Vanaf nu, elke keer dat je je COLDCARD ontgrendelt, moet je de geldigheid controleren van de twee anti-phishing woorden die op het scherm verschijnen nadat je de prefix van je PIN-code hebt ingevoerd.


## Firmware bijwerken


Als je je apparaat voor het eerst gebruikt, is het belangrijk om de firmware te controleren en bij te werken. Ga hiervoor naar het menu "*Geavanceerd/Tools*".


![CCQ](assets/fr/016.webp)


**Belangrijk:** Als je van plan bent om je firmware te upgraden en dit is niet de eerste keer dat je COLDCARD gebruikt (d.w.z. je hebt al een Wallet aangemaakt op COLDCARD), zorg er dan voor dat je Mnemonic zin en dat het functioneel is (evenals de optionele passphrase, indien van toepassing). Dit is belangrijk om te voorkomen dat je je bitcoins verliest in het geval van een probleem tijdens de apparaatupdate.


Selecteer "*Upgrade Firmware*".


![CCQ](assets/fr/017.webp)


Selecteer "*Show Version*".


![CCQ](assets/fr/018.webp)


Je kunt de huidige firmwareversie van je COLDCARD controleren. In mijn geval is de versie bijvoorbeeld "*1.2.3Q*".


![CCQ](assets/fr/019.webp)


Kijk [op de officiële COLDCARD website] (https://coldcard.com/downloads) om te zien of er een nieuwere versie beschikbaar is. Klik op "*Download*" om de nieuwe firmware te downloaden.


![CCQ](assets/fr/020.webp)


Op dit punt raden we sterk aan om de integriteit en authenticiteit van de gedownloade firmware te controleren. Om dit te doen, downloadt u [het document met de hashes van alle versies, ondertekend door de ontwikkelaars](https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt), verifieert u de handtekening met [de publieke sleutel van de ontwikkelaar](https://keybase.io/dochex) en controleert u of de Hash in het ondertekende document overeenkomt met die van de firmware die u van de site hebt gedownload. Als alles correct is, kunt u doorgaan met de update.


Als je niet bekend bent met dit verificatieproces, raad ik je aan deze tutorial te volgen:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Neem een microSD-kaart en zet het firmwarebestand (document in `.dfu`) erop. Plaats de microSD-kaart in een van de poorten van je COLDCARD.


![CCQ](assets/fr/021.webp)


Selecteer vervolgens in het menu voor het bijwerken van de firmware "*Van MicroSD*".


![CCQ](assets/fr/022.webp)


Selecteer het bestand dat overeenkomt met de firmware.


![CCQ](assets/fr/023.webp)


Bevestig je selectie door op de knop "*ENTER*" te drukken.


![CCQ](assets/fr/024.webp)


Wacht even terwijl de firmware wordt bijgewerkt.


![CCQ](assets/fr/025.webp)


Zodra de update is voltooid, voert u uw PIN-code in om het apparaat te ontgrendelen.


![CCQ](assets/fr/026.webp)


Je firmware is nu up-to-date.


## COLDCARD Q parameters


Als je wilt, kun je de instellingen van je COLDCARD bekijken door naar het menu "*Instellingen*" te gaan.


![CCQ](assets/fr/027.webp)


In dit menu vind je verschillende aanpassingsopties, zoals het instellen van de helderheid van het scherm of het selecteren van de standaard maateenheid.


![CCQ](assets/fr/028.webp)


In de volgende tutorial bekijken we andere geavanceerde instellingen:


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

## Een Bitcoin Wallet maken


Nu is het tijd om generate een nieuwe Bitcoin Wallet te maken! Om dit te doen, moet je een Mnemonic zin aanmaken. Op Coldcard heb je drie methoden om deze zin te genereren:




- Gebruik alleen de interne willekeurige getallengenerator (TRNG);
- Gebruik een combinatie van TRNG en dobbelstenen om entropie toe te voegen;
- Gebruik alleen dobbelstenen.


**Voor beginners en gevorderde gebruikers raden we aan om alleen de interne willekeurige getallengenerator van COLDCARD te gebruiken**


Ik raad de optie met alleen dobbelstenen niet aan, omdat een slechte uitvoering kan leiden tot een zin met onvoldoende entropie, waardoor de veiligheid van je Wallet in gevaar komt.


De beste optie is echter zeker de tweede, die het gebruik van TRNG combineert met een externe entropiebron. Deze methode garandeert een minimale entropie gelijk aan die van de TRNG alleen, en voegt een extra beveiligingsniveau toe in het geval van een mogelijk falen van de interne generator (vrijwillig of niet). Door voor deze optie te kiezen, die TRNG en dobbelstenen rollen combineert, heb je meer controle over het genereren van de zin, zonder de risico's te vergroten in het geval van slechte uitvoering van jouw kant.


Klik op "*Nieuwe seed Woorden*".


![CCQ](assets/fr/029.webp)


Je kunt de lengte van je zin kiezen. Ik raad je aan om te kiezen voor een zin van 12 woorden, omdat dit minder complex is om te beheren en niet minder Wallet zekerheid biedt dan een zin van 24 woorden.


![CCQ](assets/fr/030.webp)


De COLDCARD zal dan je TRNG-gegenereerde herstelzin weergeven. Als je extra externe entropie wilt toevoegen, druk je op de "*4*" toets.


![CCQ](assets/fr/031.webp)


Dit brengt je naar een pagina waar je entropie kunt toevoegen door met de dobbelstenen te gooien. Gooi zoveel mogelijk (een minimum van 50 is aanbevolen, maar minder is niet erg omdat je al profiteert van de entropie van de TRNG) en noteer de resultaten met de "*1*" tot "*6*" toetsen. Als je klaar bent, druk je op "*ENTER*" om te bevestigen.


![CCQ](assets/fr/032.webp)


Er wordt een nieuwe Mnemonic zin weergegeven, gebaseerd op de entropie die je zojuist hebt opgegeven en die van de TRNG.


**Waarschuwing: Deze Mnemonic geeft volledige, onbeperkte toegang tot al je bitcoins**. Iedereen die in het bezit is van deze zin kan je fondsen stelen, zelfs zonder fysieke toegang tot je COLDCARD. De 12-woorden zin herstelt de toegang tot je bitcoins in geval van verlies, diefstal of breuk van je COLDCARD. Het is daarom heel belangrijk om deze zorgvuldig te bewaren en op een veilige plaats op te bergen.


Je kunt het opschrijven op het karton dat bij je COLDCARD wordt geleverd, of voor extra veiligheid raad ik je aan om het op een roestvrijstalen drager te graveren om het te beschermen tegen het risico van brand, overstroming of instorting. Sla het in ieder geval nooit op een digitaal medium op, anders kun je je bitcoins kwijtraken.


Schrijf de woorden op het scherm op een fysieke drager naar keuze. Afhankelijk van je beveiligingsstrategie kun je overwegen om meerdere volledige fysieke kopieën van de zin te maken (maar splits hem vooral niet op). Het is belangrijk om de woorden genummerd en in volgorde te houden.


Het is duidelijk dat **je deze woorden** nooit mag delen op het Internet, in tegenstelling tot deze tutorial. Dit voorbeeld Wallet wordt alleen gebruikt op Testnet en wordt verwijderd aan het einde van de tutorial.


Nadat je de woorden hebt opgeschreven, druk je op "*ENTER*".


![CCQ](assets/fr/033.webp)


Om er zeker van te zijn dat je je zin correct hebt opgeslagen, zal het systeem je vragen om bepaalde woorden te bevestigen. Selecteer het nummer dat overeenkomt met elk woord op het toetsenbord.


![CCQ](assets/fr/034.webp)


Je Wallet is nu aangemaakt! In de rechterbovenhoek van het scherm zie je de vingerafdruk van je master private key. Druk op "*ENTER*".


![CCQ](assets/fr/035.webp)


Je gaat nu naar het hoofdmenu van je COLDCARD.


![CCQ](assets/fr/036.webp)


## Een nieuwe Wallet op Sparrow instellen


Er zijn verschillende mogelijkheden om communicatie tot stand te brengen tussen de Sparrow wallet software en je COLDCARD. De meest eenvoudige is om een USB-C kabel te gebruiken. Standaard zijn de kabel- en NFC-communicatie van je COLDCARD echter uitgeschakeld. Om deze weer in te schakelen, ga je naar "*Instellingen*", dan "*Hardware Aan/Uit*" en activeer je de gewenste communicatieoptie.


![CCQ](assets/fr/037.webp)


Als je je COLDCARD liever helemaal geïsoleerd houdt van je computer, kun je kiezen voor indirecte "air-gap" communicatie, met behulp van QR-codes of een microSD-kaart. Dit is de methode die we in deze tutorial zullen gebruiken.


Ga naar "*Geavanceerd/Tools*".


![CCQ](assets/fr/038.webp)


Selecteer "*Export Wallet*".


![CCQ](assets/fr/039.webp)


Selecteer vervolgens "*Sparrow wallet*".


![CCQ](assets/fr/040.webp)


Druk op "*ENTER*" om het configuratiebestand generate te maken.


![CCQ](assets/fr/041.webp)


Kies vervolgens hoe je dit bestand naar Sparrow wilt sturen. In dit voorbeeld heb ik een microSD in sleuf "*A*" geplaatst, dus selecteer ik de "*1*" knop. Je kunt de informatie ook als QR-code op je COLDCARD-scherm weergeven door op de "*QR*"-knop te drukken en deze QR-code te scannen met de webcam van je computer.


![CCQ](assets/fr/042.webp)


Start Sparrow wallet en sla de inleidende pagina's over om bij het hoofdscherm te komen. Controleer of u correct verbonden bent met een knooppunt door de schakelaar rechtsonder in het scherm te controleren.


![CCQ](assets/fr/043.webp)


Het wordt sterk aangeraden om je eigen Bitcoin node te gebruiken. Voor deze tutorial gebruik ik een publieke node (geel), omdat ik op Testnet zit, maar voor productiegebruik kun je het beste Bitcoin core lokaal (Green) of een Electrum server op een remote node (blauw) gebruiken.


Ga naar het menu "*Bestand*" en selecteer "*Nieuw Wallet*".


![CCQ](assets/fr/044.webp)


Geef je Wallet een naam en klik op "*Creëer Wallet*".


![CCQ](assets/fr/045.webp)


Kies in het vervolgkeuzemenu "*Script Type*" het type script dat uw bitcoins zal beveiligen.


![CCQ](assets/fr/046.webp)


Klik op "*Airgapped Hardware Wallet*".


![CCQ](assets/fr/047.webp)


Klik onder het tabblad "*Coldcard*" op "*Scan...*" als je van plan bent om de QR-code die op je COLDCARD staat te scannen, of op "*Import File...*" om het bestand van de microSD te importeren (dit is het `.json` bestand).


![CCQ](assets/fr/048.webp)


Controleer na het importeren of de "*Master fingerprint*" op Sparrow overeenkomt met die op je COLDCARD. Bevestig het aanmaken door op "*Apply*" te klikken.


![CCQ](assets/fr/049.webp)


Stel een sterk wachtwoord in om de toegang tot je Sparrow wallet te beveiligen. Dit wachtwoord beschermt je publieke sleutels, adressen, tags en transactiegeschiedenis tegen ongeautoriseerde toegang.


Het is een goed idee om dit wachtwoord op te slaan zodat je het niet vergeet (bijvoorbeeld in een wachtwoordmanager).


![CCQ](assets/fr/050.webp)


Uw Wallet is nu ingesteld op Sparrow wallet.


![CCQ](assets/fr/051.webp)


Voordat je je eerste bitcoins in je Wallet ontvangt, raad ik je sterk aan om een **lege hersteltest** uit te voeren. Schrijf wat referentie-informatie op, zoals je xpub, en reset dan je COLDCARD Q terwijl de Wallet nog leeg is. Probeer dan je Wallet op de COLDCARD te herstellen met je papieren back-ups. Controleer of de xpub die na het herstellen wordt gegenereerd, overeenkomt met de xpub die je oorspronkelijk hebt opgeschreven. Als dat zo is, kun je er zeker van zijn dat je papieren back-ups betrouwbaar zijn.


Om meer te leren over hoe je een hersteltest uitvoert, raad ik je aan deze andere tutorial te raadplegen:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bitcoins ontvangen


Om je eerste bitcoins te ontvangen, begin je met het inschakelen en ontgrendelen van je COLDCARD.


![CCQ](assets/fr/052.webp)


Klik op Sparrow wallet op het tabblad "*Ontvangen*".


![CCQ](assets/fr/053.webp)


Voordat je de Address gebruikt die Sparrow wallet voorstelt, controleer je deze op je COLDCARD-scherm. Hierdoor kun je bevestigen dat de Address die op Sparrow wordt weergegeven niet frauduleus is, en dat de Hardware Wallet inderdaad de privésleutel bevat die nodig is om vervolgens de bitcoins uit te geven die met deze Address zijn beveiligd. Dit helpt je om verschillende soorten aanvallen te voorkomen.


Om deze controle uit te voeren, klik je op het menu "*Address Explorer*" op de COLDCARD.


![CCQ](assets/fr/054.webp)


Selecteer het type script dat je gebruikt op Sparrow. In mijn geval is dat SegWit P2WPKH. Ik klik erop.


![CCQ](assets/fr/055.webp)


Je kunt dan je verschillende afgeleide adressen op volgorde zien.


![CCQ](assets/fr/056.webp)


Controleer met Sparrow of de Address overeenkomt. In mijn geval is de Address met afleidingspad `m/84'/1'/0'/0/0` inderdaad `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr` op zowel Sparrow als COLDCARD.


![CCQ](assets/fr/057.webp)


Een andere manier om Ownership van deze Address te verifiëren is door de QR-code direct op Sparrow te scannen vanaf je COLDCARD. Selecteer in het beginscherm van je COLDCARD "*Scan Any QR Code*". Je kunt ook de "*QR*" toets op het toetsenbord gebruiken.


![CCQ](assets/fr/058.webp)


Scan de QR-code van de Address die wordt weergegeven op de Sparrow wallet.


![CCQ](assets/fr/059.webp)


Zorg ervoor dat de Address die wordt weergegeven op uw COLDCARD overeenkomt met de Sparrow. Druk dan op de knop "*1*".


![CCQ](assets/fr/060.webp)


De Address is dus met succes bevestigd.


![CCQ](assets/fr/061.webp)


Je kunt nu een "*Label*" toevoegen om de bron van bitcoins te beschrijven die beveiligd zullen worden met deze Address. Dit is een goede manier om je UTXO's beter te beheren.


![CCQ](assets/fr/062.webp)


Voor meer informatie over labelen raad ik je ook deze andere tutorial aan:


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Je kunt deze Address dan gebruiken om bitcoins te ontvangen.


![CCQ](assets/fr/063.webp)


## Bitcoins versturen


Nu je je eerste Sats hebt ontvangen in je COLDCARD-beveiligde Wallet, kun je ze ook uitgeven!


Zoals altijd begin je met het inschakelen en ontgrendelen van je COLDCARD Q, open dan Sparrow wallet en navigeer naar het tabblad "*Versturen*" om een nieuwe transactie voor te bereiden.


![CCQ](assets/fr/064.webp)


Als je "Coin controle" wilt, d.w.z. specifiek wilt kiezen welke UTXO's je in de transactie wilt gebruiken, ga dan naar het tabblad "*UTXO's*". Selecteer de UTXO's die je wilt uitgeven en klik dan op "*Verstuur Geselecteerd*". Je wordt doorgestuurd naar hetzelfde scherm in het tabblad "*Versturen*", maar met je UTXO's al geselecteerd voor de transactie.


![CCQ](assets/fr/065.webp)


Voer de bestemming Address in. Je kunt ook meerdere adressen invoeren door op de knop "*+ Add*" te klikken.


![CCQ](assets/fr/066.webp)


Schrijf een "*Label*" op om het doel van deze uitgave te onthouden.


![CCQ](assets/fr/067.webp)


Selecteer het bedrag dat naar deze Address moet worden gestuurd.


![CCQ](assets/fr/068.webp)


Pas het tarief van je transactie aan volgens de huidige markt.


![CCQ](assets/fr/069.webp)


Zorg ervoor dat al je transactieparameters juist zijn en klik dan op "*Create Transaction*".


![CCQ](assets/fr/070.webp)


Als alles naar wens is, klik je op "*Transactie voltooien voor ondertekening*".


![CCQ](assets/fr/071.webp)


Als je je transactie in Sparrow hebt opgebouwd, is het tijd om hem te ondertekenen met je COLDCARD. Om de PSBT (niet-ondertekende transactie) naar je apparaat te sturen, heb je verschillende opties. Als bekabelde datatransmissie is ingeschakeld, kun je de transactie direct via een USB-C verbinding versturen, net zoals je met elke andere Hardware Wallet zou doen. In dit geval moet u op de Sparrow op de knop "*Tekenen*" rechtsonder klikken. In mijn voorbeeld is deze knop geblokkeerd omdat de COLDCARD niet met een kabel is verbonden.


![CCQ](assets/fr/072.webp)


Als je liever een "air-gap" verbinding hebt zonder direct contact tussen de Hardware Wallet en je computer, heb je 2 opties. De eerste, en meer complexe, is het gebruik van een microSD-kaart. Plaats de microSD-kaart in je computer, neem de transactie op via de toets "*Transactie opslaan*" op de Sparrow, en breng deze kaart vervolgens over naar een poort op je COLDCARD.


![CCQ](assets/fr/073.webp)


Ga vervolgens naar het menu "*Klaar om te ondertekenen*".


![CCQ](assets/fr/074.webp)


Bekijk de transactiegegevens op je COLDCARD, inclusief de ontvangende Address, het verzonden bedrag en de transactiekosten.


![CCQ](assets/fr/075.webp)


Als alles correct is, druk je op de knop "*ENTER*" om de transactie te ondertekenen.


![CCQ](assets/fr/076.webp)


Plaats dan de microSD terug in je computer en klik op Sparrow op "*Load Transaction*" om de ondertekende transactie van de microSD te laden. Je kunt dan een laatste controle uitvoeren voordat je het uploadt naar het Bitcoin netwerk.


![CCQ](assets/fr/077.webp)


De tweede methode om te ondertekenen met je COLDCARD in Air-Gap, die veel eenvoudiger is dan de microSD-methode, is om de PSBT direct via de camera van het apparaat te scannen. Selecteer op de Sparrow "*Show QR*".


![CCQ](assets/fr/078.webp)


Selecteer op de COLDCARD "*Scan Any QR Code*". Je kunt ook de "*QR*" toets op het toetsenbord gebruiken.


![CCQ](assets/fr/079.webp)


Gebruik de camera van de COLDCARD om de QR-code te scannen die op de Sparrow wordt weergegeven.


![CCQ](assets/fr/080.webp)


De transactiegegevens verschijnen opnieuw ter verificatie. Druk op "*ENTER*" om te ondertekenen als alles naar wens is.


![CCQ](assets/fr/081.webp)


Je COLDCARD toont de ondertekende transactie dan als een QR-code. Gebruik de webcam van je computer om deze QR-code te scannen door "*Scan QR*" te selecteren op Sparrow.


![CCQ](assets/fr/082.webp)


Je ondertekende transactie is nu zichtbaar op Sparrow. Controleer nog een laatste keer of alles correct is en klik dan op "*Broadcast Transaction*" om het uit te zenden op het Bitcoin netwerk.


![CCQ](assets/fr/083.webp)


U kunt uw transactie volgen in Sparrow wallet's tabblad "*Transacties*".


![CCQ](assets/fr/084.webp)


Gefeliciteerd, je bent nu op de hoogte van het basisgebruik van COLDCARD Q met Sparrow wallet!


Als je deze tutorial nuttig vond, zou ik je erg dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om deze tutorial te delen op je sociale netwerken. Hartelijk dank!


Ik raad je ook aan om deze andere tutorial te bekijken, waarin we de geavanceerde opties van de COLDCARD Q bespreken:


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0