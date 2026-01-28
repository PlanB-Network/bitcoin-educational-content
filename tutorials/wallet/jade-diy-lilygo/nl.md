---
name: Jade DIY
description: Verander een dev board van $15 in een volledig functionele Bitcoin hardware wallet
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Beginnersgebouw


**Doelgroep:** Nieuwsgierige bouwers met weinig tot geen embedded ervaring.


**Duur:** 2 uur (flexibel)


**Resultaten:** Aan het eind zullen de studenten:



- Het beveiligingsmodel herkennen van doe-het-zelf hardware wallets versus commerciële apparaten.
- Zet een microcontrollergebaseerd ondertekeningsapparaat in elkaar.
- Flash open-source firmware en controleer de build checksum.
- Een mainnet transactie ondertekenen en uitzenden met hun nieuwe apparaat.


---

## Abstract


Deze 2 uur durende workshop leert beginners een functionele Bitcoin hardware wallet te bouwen door open-source Jade firmware te flashen op een $15 LilyGO T-Display bord. Studenten transformeren generieke ontwikkelhardware in een ondertekeningsapparaat dat vergelijkbaar is met commerciële portemonnees van $150 en leren beveiligingsprincipes door middel van praktijkervaring in plaats van theorie alleen.


### Filosofie


Je eigen ondertekeningsapparaat bouwen gaat niet alleen over geld besparen-het gaat over het begrijpen van de technologie die je Bitcoin beschermt. Deze workshop omarmt "veiligheid door begrip" in plaats van black-box vertrouwen. Door zelf onderdelen te kopen, open-source firmware te flashen en zelf entropie te genereren, verminderen studenten het risico van de toeleveringsketen terwijl ze leren om beveiligingsclaims kritisch te evalueren. Het doel is geïnformeerde autonomie: studenten moeten zowel de kracht als de beperkingen van hun doe-het-zelf apparaat begrijpen in vergelijking met geharde commerciële alternatieven.


---

## Concept inleiding (15 min)


### Wat is zelfbewaarneming en waarom is het belangrijk?


Bitcoin werd gecreëerd om vertrouwde derde partijen, zoals banken en bedrijven, uit ons geldsysteem te verwijderen. In plaats van vertrouwen te gebruiken, gebruikt bitcoin wiskunde, natuurkunde en cryptografie om iedereen de macht te geven om zijn geld te bezitten en te controleren zonder dat iemand toestemming nodig heeft.


De manier waarop dit werkt is dat bitcoin bestaat op een wereldwijd digitaal grootboek genaamd de blockchain aka de bitcoin timechain, wat een openbaar en transparant grootboek is dat gerund wordt door computers, in plaats van een gecentraliseerd grootboek zoals een bankrekening.


Het belangrijkste om te begrijpen is dat om bitcoin van de ene plaats naar de andere te verplaatsen, je die transactie moet ondertekenen met een zogenaamde privésleutel. Zie het als het ontgrendelen van een kluis met een wachtwoord, en de bitcoin naar de kluis van iemand anders verplaatsen. Bitcoin geeft je de macht om zelf de sleutels van die kluis te bezitten, in plaats van te vertrouwen op een bank om je geld voor je te verplaatsen.


Met grote macht komt grote verantwoordelijkheid, verlies je sleutels en je geld is voor altijd weg. Op deze manier kun je de sleutels van de kluis zien als het geld zelf. Hoewel sleutels niet hetzelfde zijn als bitcoin, vormen ze wel het mechanisme om je geld te verplaatsen en zijn ze daarom uiterst belangrijk om te beschermen. Daarom zeggen we "niet je sleutels, niet je munten".


De term self-custody klinkt misschien verwarrend, maar het betekent alleen dat je je eigen privésleutels bezit en je eigen bitcoin beheert. Als je die sleutel niet bezit, vertrouw je erop dat iemand anders hem voor je bewaart. Als je bitcoin in een ETF zit of op een beurs (Mt. Gox, FTX, Coinbase, Binance, etc.), dan bezit je geen bitcoin, maar een claim op bitcoin. Dit introduceert allerlei risico's, zoals beurzen die gehackt worden en je bitcoin kwijtraken of bedrijven die je geld uitlenen en je slechts een fractie als reserve geven. Bovendien zouden vertrouwde derde partijen volledige controle over je geld hebben en opnames kunnen beperken of bevriezen.


![image](assets/fr/01.webp)


Met self-custody haal je vertrouwen uit de vergelijking. Niemand kan je tegoeden bevriezen of een transactie weigeren, je kunt geld over de grens sturen, naar iedereen, op elk moment, en je hebt geen bankrekening, ID of goedkeuring nodig. Niemand kan je tegenhouden, censureren of van je stelen, waardoor de volledige kracht van bitcoin als vrijheidsgeld wordt ontsloten. Daarom zeggen we: met bitcoin kun je je eigen bank zijn.


Bitcoin werd gecreëerd om het probleem van de manipulatie van vertrouwen en geld op te lossen, een opt-out van ons huidige systeem, maar de uitgang werkt alleen als je de sleutels pakt. Daarom is zelfbehoud zo belangrijk.


### Wat is een Wallet?


De term wallet is een beetje een verkeerde benaming en kan daarom verwarrend zijn. Ja, het is waar dat een bitcoin wallet, net als een fysieke wallet, waarde opslaat. Maar het belangrijkste verschil is dat bitcoin wallets eigenlijk geen bitcoin opslaan.


Bitcoin bestaat alleen als een vermelding in het grootboek op de publieke blockchain, of binnen de metaforische kluizen in cyberspace. Om bitcoin te verplaatsen, moet je jouw sleutels gebruiken om de kluis te openen en de munten ergens anders naartoe te verplaatsen. Als je een transactie doet met je wallet, gebruik je eigenlijk alleen je sleutels om de transactie te ondertekenen. Dit is hoe je bewijst dat je het geld bezit en het recht hebt om die munten uit te geven.


Bitcoin wallets slaan eigenlijk alleen je privésleutels op, dus het zou nauwkeuriger zijn om ze sleutelhangers te noemen.


### Hot vs Cold portemonnees


Een hot wallet is een software-app op je telefoon of computer. Het is verbonden met het internet, dus het is gemakkelijker te gebruiken en sneller om transacties te ondertekenen, maar dit betekent ook dat het meer blootgesteld is aan hackers, malware en phishing. Het wordt "hot" genoemd omdat het verbonden is met het internet, aangesloten is en aan staat. Een voorbeeld hiervan is een telefoon wallet of een browser wallet.


Aan de andere kant is een koude wallet, of hardware wallet, een apparaat dat je sleutel offline aanmaakt en opslaat. Dit verwijdert de mogelijkheid voor iemand om je fondsen te hacken en is veel veiliger voor langetermijnsparen, maar het is een apparaat dat nodig is om elke transactie te ondertekenen en kan minder handig zijn.


### Hardware Wallet Bedreigingsmodel


Hardware wallets bestaan om een fundamenteel probleem op te lossen: hoe onderteken je Bitcoin transacties zonder je privésleutels bloot te stellen aan een computer met internetverbinding die gecompromitteerd kan worden door malware of aanvallers op afstand? Het kernbedreigingsmodel gaat ervan uit dat je alledaagse laptop of telefoon potentieel vijandig is. Een hardware wallet creëert een geïsoleerde omgeving waar private sleutels nooit het apparaat verlaten en het ondertekenen van transacties gebeurt in een secure element of microcontroller die alleen de handtekening teruggeeft aan de hostcomputer, niet de sleutel zelf. Zelfs als je computer volledig gecompromitteerd is, kan een aanvaller je Bitcoin niet stelen zonder fysieke toegang tot het apparaat en je PIN-code.


Hardware wallets introduceren echter hun eigen bedreigingen. Je moet erop vertrouwen dat de fabrikant geen achterdeurtjes heeft ingebracht, dat er niet geknoeid is met de toeleveringsketen en dat de willekeurige nummergeneratie echt willekeurig is. Fysieke aanvallers kunnen sleutels ontfutselen via side-channel aanvallen of chipmanipulatie en iemand met tijdelijke toegang kan je apparaat aanpassen. Het bouwen van je eigen hardware wallet helpt je om deze afwegingen te begrijpen-je zult beslissingen nemen over veilige elementen versus algemene microcontrollers, hoe je transacties op een display kunt verifiëren en hoe je bescherming kunt bieden tegen zowel externe als fysieke bedreigingen. Het doel is niet perfecte beveiliging, maar begrijpen tegen welke bedreigingen je je beschermt en welke er overblijven.


### Sleutelconcepten



- Entropie en seed zinnen:** Je wallet is slechts zo veilig als de willekeur die het voortbrengt. We mengen de willekeurige getallengenerator van het apparaat met mensvriendelijke trucs zoals dobbelen, zetten die entropie om in een 12- of 24-woord [BIP39 zin](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) en verlaten de kamer met een geschreven of metalen back-up die je vertrouwt.
- Zaad zinshygiëne:** Behandel de seed als de sleutels van je spaargeld. Typ de woorden nooit in een telefoon of computer - keyloggers, screenshots en cloud backups kunnen ze voor altijd lekken. Bewaar de zin offline, bewaar hem ergens waar alleen jij bij kunt en oefen het hardop voorlezen voordat je weggaat.
- Beveiligd element + microcontroller:** Zie de secure element als de kluis en de microcontroller als het brein. De secure element bewaakt de privésleutels met knoeiweerstand, terwijl de microcontroller het scherm, de knoppen en de firmwarelogica regelt. Merk op dat de hardware wallets die we vandaag bouwen geen secure element hebben. Dit betekent niet dat het onveilig is, alleen dat het een beschermingsniveau minder heeft.
- Vertrouw firmware:** Firmware is het onzichtbare besturingssysteem van de wallet. Download altijd van gelabelde releases, controleer de gepubliceerde hash en begrijp dat reproduceerbare builds meerdere mensen dezelfde code laten compileren en op exact dezelfde binary uitkomen. Als de checksum niet overeenkomt, teken je niet.


---

## Wat zijn we aan het bouwen?


We nemen generieke hardware, het LilyGo T-Display, en flashen er Jade SDK-firmware op. De [Jade Plus](https://blockstream.com/jade/jade-plus/) is een open-source wallet, die normaal $150 kost:


![image](assets/fr/02.webp)


Vandaag flashen we hun firmware op een $15 hardware.


### Wat te kopen


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB met omhulsel, model K164)** - [Bestel rechtstreeks bij LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) voor ongeveer $15. Dit ESP32-bord biedt het display, de knoppen en de USB-interface die de Jade Plus van Blockstream weerspiegelen. De ESP32 aan boord bevat ook Wi-Fi en Bluetooth radio's; we leveren firmware die ze uitgeschakeld houdt, maar ze vormen je bedreigingsmodel omdat kwaadwillende code ze weer kan inschakelen.
- USB-C kabel** - Neem een datacapabele kabel mee zodat je firmware kunt flashen en het bord rechtstreeks vanaf je laptop van stroom kunt voorzien (prima voor gebruik in de klas).


### Waarom je eigen Hardware Wallet bouwen?



- Bespaar ruwweg $ 135 in vergelijking met het kopen van een commercieel apparaat.
- Zorg voor comfort met het flashen van firmware, beveiligde elementen en wallet hygiëne.
- Zet extra ondertekeningsapparaten op om besparingen te spreiden over meerdere portemonnees.
- Verminder de risico's van de toeleveringsketen door elk onderdeel zelf in te kopen en te assembleren.
- Houd de mantra van Lopp in gedachten: soevereiniteit en gemak staan altijd op gespannen voet met elkaar.


## Fysieke opstelling


### Uw zaak voorbereiden


Je hebt twee opties voor het onderbrengen van je LilyGO T-Display-bord: een 3D-geprinte behuizing of de officiële LilyGO-behuizing. De geprinte behuizing kun je vinden en printen op [dit model](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Het biedt een lichtgewicht en aanpasbaar omhulsel voor je apparaat.


![image](assets/fr/04.webp)


Je kunt ook de officiële LilyGO case gebruiken, die een iets andere pasvorm en afwerking heeft en een robuustere bescherming en een gepolijste look biedt.


![image](assets/fr/05.webp)


Merk op dat de gedrukte en officiële behuizingen lichtjes verschillen in ontwerp en assemblage. Welke optie je ook kiest, zorg ervoor dat het bord goed in de behuizing zit om losse verbindingen of schade te voorkomen.


### Inspecteer de printplaat


Voordat je verder gaat, controleer je het LilyGO T-Display-bord zorgvuldig op zichtbare defecten of vuil. Controleer of het scherm, de toetsen en de USB-C poort schoon zijn en vrij van stof of soldeerspatten. Ga voorzichtig om met het bord en neem de veiligheid van elektrostatische ontlading (ESD) in acht door jezelf te aarden of een ESD-polsband te gebruiken om schade aan gevoelige onderdelen te voorkomen.


### Aansluiten op uw laptop


Verbind het LilyGO bord met je laptop via een USB-C kabel die geschikt is voor data. Deze verbinding zorgt voor stroom en maakt het mogelijk om de firmware te flashen.


Bij het opstarten wordt u begroet met het volgende scherm:


![image](assets/fr/06.webp)



Wanneer de LilyGO ingeschakeld is, toont het een kleurentestscherm dat door effen kleuren loopt. Dit bevestigt dat het scherm en de printplaat correct functioneren voordat de firmware wordt geflasht.


Zodra de kleurentest voltooid is, zal het scherm een standaardstatus aannemen, wat aangeeft dat het bord klaar is voor de volgende stappen in het bouwproces.


![image](assets/fr/07.webp)


## De makkelijke weg of de Hard weg


Er zijn twee benaderingen voor het flashen van uw hardware wallet firmware: de gemakkelijke en de moeilijke manier. De gemakkelijke manier maakt gebruik van voorgeconfigureerde tools of web-gebaseerde flashers die automatisch de firmware op je apparaat laden met minimale invoer. Deze methode is ideaal voor beginners die snel willen winnen of de complexiteit van debuggen en commandoregelinteracties willen vermijden. Het vereenvoudigt het proces en zorgt ervoor dat je sneller aan de slag kunt, waardoor het toegankelijk wordt voor mensen die nieuw zijn in embedded ontwikkeling of hardware wallets.


De moeilijke manier houdt in dat u handmatig commandoregeltools gebruikt om de firmware te flashen. Bij deze aanpak moeten handtekeningen en checksums van de firmware worden geverifieerd om de authenticiteit en integriteit te garanderen, waardoor u meer inzicht krijgt in het flashproces en hoe de firmware met de hardware interageert. Hoewel het meer inspanning vergt en bekendheid met terminalcommando's, biedt het meer controle, transparantie en vertrouwen in de beveiliging van je apparaat.


Elke methode heeft zijn nadelen: de makkelijke manier offert een zekere mate van vertrouwen en begrip op voor snelheid en gemak, terwijl de moeilijke manier meer tijd en technische vaardigheid vereist, maar je beloont met flexibiliteit en een beter begrip van de onderliggende technologie. Docenten moeten leerlingen aanmoedigen om het pad te kiezen dat het beste past bij hun comfortniveau en nieuwsgierigheid.


## De gemakkelijke manier


De eenvoudigste manier om een ESP32 te flashen



- Ga naar de officiële Blockstream Github: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Je kunt het bronbestand downloaden en de website lokaal uitvoeren, maar GitHub host het al op [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub serveert de HTML, CSS, JavaScript, etc. direct naar je browser, zodat je het apparaat kunt flashen zonder ontwikkelaarstools te installeren.


![image](assets/fr/09.webp)



- Open het vervolgkeuzemenu (waarschijnlijk staat het standaard op `M5Stack Core2`) en selecteer je ontwikkelboard - voor deze klasse kies je `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Wanneer je op flash klikt, verschijnt dit. Om te weten welk apparaat de LILYGO is, koppel je de lilygo los en sluit je hem weer aan. De COM-poort van de lilygo verschijnt en verdwijnt weer. Klik op de COM-poort waarop de Jade is aangesloten


![image](assets/fr/11.webp)



- Dat is het, er zou een voortgangsbalk moeten verschijnen en als het klaar is, ben je klaar om het in te stellen


## De Jade Wallet instellen


Zodra de firmware succesvol is geflashed, is je LilyGO T-Display een volledig functionele Jade hardware wallet. Dit hoofdstuk leidt je door het eerste installatieproces, van het genereren van je seed zinsdeel tot het verbinden van het apparaat met wallet software zoals Sparrow of de Blockstream Green mobiele app.


### Initiële opstart en apparaatinstelling



- Zet het apparaat aan:** Met de LilyGO nog steeds via USB-C aangesloten op je laptop, zou de Jade-firmware automatisch moeten opstarten. Je ziet het Jade-logo op het scherm verschijnen.



- Instelmodus openen:** Het apparaat zal je een beginmenu tonen. Gebruik de twee fysieke knoppen op het bord om te navigeren:
 - Linkerknop:** Omhoog/terug
 - Rechter knop:** Ga omlaag/vooruit
 - Beide knoppen tegelijk:** Selecteren/bevestigen



- Selecteer "Setup":** Navigeer naar de optie Setup en druk op beide knoppen om te bevestigen. Het apparaat leidt je door het eerste configuratieproces.


### Je Wallet maken



- Kies "Begin Setup":** Het apparaat vraagt je om te beginnen met de wallet aanmaakprocedure. Bevestig je keuze.



- Selecteer "Nieuw Wallet aanmaken":** Je krijgt twee opties:
 - Create New Wallet:** Genereert een nieuwe seed zin (kies deze voor de workshop)
 - Wallet herstellen:** een bestaande wallet van een seed zin herstellen (voor gevorderde gebruikers)



- Selecteer "Nieuw Wallet aanmaken" en bevestig.



- Entropie genereren:** Het apparaat gebruikt zijn willekeurige getallengenerator om cryptografische entropie te creëren. Dit proces duurt een paar seconden omdat het apparaat willekeurigheid uit meerdere bronnen verzamelt.


### Je zaadzin opnemen



- Schrijf uw seed zin op:** Het apparaat zal nu een BIP39 seed zin van 12 woorden weergeven, één woord per keer. Dit is de belangrijkste stap in het hele proces.


**Belangrijke beveiligingsprocedures:**


- Schrijf elk woord duidelijk op papier (gebruik indien beschikbaar de bijgeleverde seed zinnenkaarten)
- Dubbelcheck elk woord terwijl je het schrijft
- Fotografeer de seed zin nooit met je telefoon
- Typ de woorden nooit in een computer of telefoon
- Houd je seed zin privé - deel je scherm niet en laat het niet aan anderen zien



- Controleer uw seed-zin:** Nadat u alle 12 woorden hebt opgeschreven, vraagt het apparaat u een aantal woorden uit de zin te bevestigen, om er zeker van te zijn dat u ze correct hebt opgenomen. Gebruik de toetsen om het juiste woord voor elke vraag te selecteren.


**Pro tip:** Voordat je verder gaat, oefen je met het hardop voorlezen van je seed zin (stil, zodat anderen het niet kunnen horen). Dit helpt om eventuele handschriftfouten of dubbelzinnigheden op te sporen.


### Verbindingsmethode



- Verbindingstype kiezen:** De Jade-firmware ondersteunt twee verbindingsmethoden:
 - USB:** Bekabelde verbinding via USB-C kabel (aanbevolen voor deze workshop)
 - Bluetooth:** Draadloze verbinding met mobiele apparaten



- Kies voorlopig **USB**, omdat dit de meest eenvoudige optie is voor desktop wallet software en geen draadloze aanvalsvectoren introduceert.



- Naamgeving apparaat:** De Jade zal een unieke identificatie weergeven zoals "Connect Jade A7D924". Deze identificatie helpt je onderscheid te maken tussen meerdere hardware wallets als je er uiteindelijk meer dan één bouwt. Noteer deze identificatie indien gewenst.


### Verbinding maken met Wallet-software


Je hebt nu twee hoofdopties voor de interface met je nieuw aangemaakte hardware wallet: de mobiele Blockstream Green app (voor gebruik onderweg) of Sparrow Wallet (voor desktopgebruik met meer geavanceerde functies). Voor deze workshop richten we ons op Sparrow Wallet, omdat het beter inzicht biedt in de technische details van Bitcoin transacties.


#### Optie 1: Blockstream Green mobiele app (Snel aan de slag)


Als je je apparaat snel wilt testen met een mobiel apparaat:



- Download de **Blockstream Green** app van de App Store (iOS) of Google Play (Android)
- Open de app en selecteer "Hardware Wallet verbinden"
- Kies "Jade" uit de lijst met ondersteunde apparaten
- Sluit je Jade aan op je telefoon met een USB-C naar USB-C kabel (of USB-C naar Lightning adapter voor iPhone 15+)
- Volg de aanwijzingen op het scherm om verbinding te maken en uw eerste wallet aan te maken


**Opmerking over Liquid:** De Blockstream Green app ondersteunt zowel Bitcoin als Liquid (een Bitcoin sidechain). Als je Liquid functies gebruikt, kan je gevraagd worden om "Export master blinding key" - hierdoor kan de app transactiebedragen zien op het Liquid netwerk, die anders vertrouwelijk zijn. Voor deze workshop kun je de Liquid functies overslaan en je richten op standaard Bitcoin transacties.


#### Optie 2: Sparrow Wallet (aanbevolen voor werkplaats)


Sparrow Wallet is een krachtige desktopapplicatie die je gedetailleerde controle geeft over je Bitcoin transacties en naadloos aansluit op je Jade hardware wallet.


**Installatie:**



- Download Sparrow Wallet van de officiële website: [sparrowwallet.com](https://sparrowwallet.com)
- Controleer de downloadhandtekening (zie de Sparrow documentatie voor details)
- De applicatie installeren en starten


**Je Jade aansluiten op Sparrow:**



- Ga in Sparrow naar **Bestand → Nieuw Wallet**
- Geef je wallet een naam (bijvoorbeeld "Mijn Jade Wallet")
- Klik op **Gekoppeld Hardware Wallet**
- Sparrow detecteert automatisch uw ingeplugde Jade-apparaat
- Bevestig de verbinding op het Jade-display door op beide knoppen te drukken als daarom wordt gevraagd
- Selecteer het gewenste scripttype:
 - Native Segwit (P2WPKH):** Aanbevolen voor beginners-laagste kosten, breedste compatibiliteit met moderne wallets
 - Geneste Segwit (P2SH-P2WPKH):** Voor compatibiliteit met oudere services
 - Taproot (P2TR):** Meest geavanceerd, biedt de beste privacy en de laagste tarieven, maar vereist geavanceerde wallet ondersteuning
- Klik op **Import Keystore** om de verbinding te voltooien


**Serververbinding van Sparrow configureren:**


Voordat u uw saldo kunt zien of transacties kunt uitzenden, moet Sparrow verbinding maken met een Bitcoin knooppunt om blockchaingegevens op te halen. Je hebt verschillende opties, elk met verschillende afwegingen tussen gemak, privacy en vertrouwen:



- Publieke Electrum Server (Gemakkelijkst, minst privé):** Verbindt met een publieke server, beheerd door een derde partij. Snel op te zetten, maar de server kan de adressen van je wallet zien en mogelijk linken aan jouw IP-adres. Goed voor testen op testnet.
 - Ga in Sparrow naar **Tools → Voorkeuren → Server**
 - Selecteer **Publieke server** en kies een server uit de lijst
 - Klik op **Test verbinding** om te controleren



- Bitcoin Core of Knots Node (meest privé, meeste werk):** Draai je eigen volledige Bitcoin node. Dit is de gouden standaard voor privacy en verificatie, omdat je elke transactie zelf valideert en niet vertrouwt op de server van iemand anders. Het vereist echter het downloaden van de volledige blockchain (~600GB) en het gesynchroniseerd houden van je node.
 - Bitcoin Kern of Knopen installeren en synchroniseren
 - Ga in Sparrow naar **Tools → Voorkeuren → Server**
 - Selecteer **Bitcoin Core of Knots** en voer de verbindingsgegevens van uw knooppunt in



- Private Electrum Server (Goede balans):** Host je eigen Electrum server (zoals Fulcrum of Electrs) verbonden met je Bitcoin Core of Knots node. Biedt volledige privacy zonder Sparrow op dezelfde machine als uw node te hoeven draaien.
 - Zet een Electrum server op die naar uw Bitcoin Core of Knots knooppunt wijst
 - Ga in Sparrow naar **Tools → Voorkeuren → Server**
 - Selecteer **Private Electrum** en voer de URL van je server in


Voor deze workshop is het gebruik van een **Publieke Electrum Server** prima voor testnet transacties. In een productieomgeving met echt geld kun je overwegen om je eigen node te gebruiken of een vertrouwde privéserver voor maximale privacy.


#### Optie 3: Blockstream Green Desktop App (Snel aan de slag)


Blockstream Green is de software om het instellen van JadeDIY te voltooien en het moet de desktopversie zijn



- Download de officiële Blockstream-toepassing - dit is de link van hun website. Klik daar op [Nu downloaden](https://blockstream.com/app/).


![image](assets/fr/12.webp)



- Afhankelijk van waar je downloads naartoe gaan, staat het bestand waarschijnlijk in je Downloads-map. Controleer die map en dubbelklik op het uitvoerbare bestand om de software te installeren.


![image](assets/fr/13.webp)



- Het kan zijn dat je adminrechten moet geven om het installatieprogramma uit te voeren. Zodra je dat hebt gedaan, verschijnt er een venster dat eruit moet zien als de volgende afbeelding - klik op **Next**.


![image](assets/fr/14.webp)



- Kies waar u de geïnstalleerde toepassing wilt plaatsen (een locatie bij uw andere programma's of ergens waar u ze gemakkelijk kunt vinden) en klik vervolgens op **Volgende**.


![image](assets/fr/15.webp)



- Het installatieprogramma vraagt om een snelkoppelingsnaam. Voer er een in of houd de standaardwaarde aan en klik op **Next**.


![image](assets/fr/16.webp)



- Als u een snelkoppeling op het bureaublad wilt, vinkt u het vakje aan. Klik anders op **Volgende**.


![image](assets/fr/17.webp)



- Klik ten slotte op **Installeren** en wacht een paar minuten tot de installatie is voltooid.


![image](assets/fr/18.webp)



- De voortgangsbalk moet tot het einde gevuld zijn.


![image](assets/fr/19.webp)



- Als het klaar is, verschijnt er een nieuwe pagina - klik op **Voltooien**.


![image](assets/fr/20.webp)



- Zoek je nieuw geïnstalleerde Blockstream-toepassing (voorbeeld in het Windows 11 Start-menu).


![image](assets/fr/21.webp)



- Als je het hebt gevonden, klik je op om het te starten - er zou een splash-scherm moeten verschijnen.


### Uw installatie controleren


Eenmaal verbonden met Sparrow (of een andere wallet-toepassing):



- Controleer uw adressen:** Sparrow geeft ontvangstadressen weer die zijn afgeleid van uw seed-zin. U kunt een adres op uw Jade-apparaat controleren door naar het tabblad "Ontvangen" in Sparrow te gaan en op "Address weergeven" te klikken - het adres moet zowel op uw computerscherm als op het Jade-scherm verschijnen.



- Een ontvangstadres genereren:** Klik op het tabblad **Ontvangen** in Sparrow en kopieer uw eerste Bitcoin ontvangstadres.



- Klaar voor transacties:** Uw wallet hardware is nu volledig geconfigureerd en klaar om Bitcoin transacties te ontvangen en te ondertekenen. Ga verder naar het volgende hoofdstuk om het ondertekenen van een testnet transactie te oefenen.



---

### Checklist snelle installatie



- Jade firmware start succesvol op
- Nieuwe wallet gemaakt met 12-woord seed-zin
- Zaadzin duidelijk opgeschreven en gecontroleerd
- USB-verbindingsmodus geselecteerd
- Wallet-software (Sparrow) geïnstalleerd en aangesloten
- Serververbinding geconfigureerd (openbaar Electrum voor mainnet)
- Eerste ontvangstadres gegenereerd en geverifieerd op apparaat



---

**MIT-licentie**


**auteursrecht (c) 2025 Het Bitcoin Netwerk NYC**


Hierbij wordt gratis toestemming verleend aan iedereen die een kopie van deze software en bijbehorende documentatiebestanden (de "Software") verkrijgt, om zonder beperkingen met de Software om te gaan, inclusief en zonder beperking de rechten om kopieën van de Software te gebruiken, te kopiëren, te wijzigen, samen te voegen, te publiceren, te distribueren, in sublicentie te geven en/of te verkopen, en om personen aan wie de Software is geleverd toe te staan dit te doen, onder de volgende voorwaarden:


De bovenstaande copyrightmelding en deze toestemmingsmelding moeten worden opgenomen in alle kopieën of substantiële delen van de Software.


DE SOFTWARE WORDT GELEVERD "ZOALS DEZE IS", ZONDER ENIGE GARANTIE, EXPLICIET OF IMPLICIET, INCLUSIEF MAAR NIET BEPERKT TOT DE GARANTIES VAN VERKOOPBAARHEID, GESCHIKTHEID VOOR EEN BEPAALD DOEL EN NIET-INBREUK. IN GEEN GEVAL ZULLEN DE AUTEURS OF AUTEURSRECHTHEBBENDEN AANSPRAKELIJK ZIJN VOOR ENIGE CLAIM, SCHADE OF ANDERE AANSPRAKELIJKHEID, HETZIJ IN EEN CONTRACTUELE ACTIE, ONRECHTMATIGE DAAD OF ANDERSZINS, VOORTVLOEIEND UIT, UIT OF IN VERBAND MET DE SOFTWARE OF HET GEBRUIK VAN OF ANDERE OMGANG MET DE SOFTWARE.


---