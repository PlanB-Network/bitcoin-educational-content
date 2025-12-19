---
name: Satochip x SeedSigner
description: Hoe gebruik je een Satochip met je SeedSigner?
---

![cover](assets/cover.webp)



*Met dank aan [Crypto Guide](https://www.youtube.com/@CryptoGuide/) voor de fork van de SeedSigner firmware voor smartcard-ondersteuning, die we in deze tutorial zullen gebruiken



---

De Satochip is een wallet smartcard-formaat hardware met een EAL6+ gecertificeerd beveiligingselement, een van de hoogste beveiligingsstandaarden. Het is ontworpen en geproduceerd door het gelijknamige Belgische bedrijf: Satochip.



De Satochip kost ongeveer €25 en onderscheidt zich van de concurrentie door zijn uitstekende prijs-kwaliteitverhouding. Dankzij de beveiligde chip is hij bestand tegen fysieke aanvallen. Bovendien is de broncode van de applet volledig open-source, gelicenseerd onder *AGPLv3*.



Aan de andere kant legt het formaat bepaalde functionele beperkingen op. Het grootste nadeel van de Satochip is de afwezigheid van een geïntegreerd scherm: gebruikers moeten dus blindelings transacties ondertekenen en vertrouwen alleen op het beeldscherm van hun computer.



Om deze zwakte te overwinnen is het bijzonder interessant om de Satochip te gebruiken in combinatie met een SeedSigner. In deze opstelling vindt de communicatie niet langer rechtstreeks plaats tussen de computer en de Satochip, maar via QR code uitwisselingen tussen de computer en de SeedSigner. De SeedSigner fungeert dan als een vertrouwensscherm: het toont de informatie die moet worden ondertekend, terwijl de handtekening zelf wordt uitgevoerd door de Satochip. In tegenstelling tot conventioneel gebruik van de SeedSigner (of zelfs gebruik in combinatie met Seedkeeper), wordt de seed nooit in de SeedSigner geladen. De SeedSigner wordt dus het scherm van de Satochip, waardoor de risico's van blind ondertekenen worden geëlimineerd.



Als we het probleem andersom bekijken, vult het gebruik van de SeedSigner met een Satochip een belangrijk gat in de SeedSigner: de mogelijkheid om de seed binnen een secure element op te slaan en te gebruiken.



Naar mijn mening biedt deze configuratie verschillende voordelen ten opzichte van conventionele hardware wallets:




- De Satochip kost ongeveer €25, en aangezien de applet open-source is, kun je hem zelf installeren op een lege smartcard. Daar komen dan nog de kosten van de SeedSigner componenten en de extensie voor het lezen van smartcards bij: afhankelijk van waar je deze hardware koopt, zou het totaal tussen de €70 en €100 moeten liggen.
- Alle software die betrokken is bij de installatie is open-source: de SeedSigner firmware en de Satochip applet.
- U profiteert van een gecertificeerd beveiligingselement.
- De configuratie kan volledig DIY uitgevoerd worden, zonder gebruik te maken van hardware die expliciet bedoeld is voor Bitcoin gebruik, wat een vorm van plausibele ontkenning kan bieden en weerstand tegen bepaalde externe bedreigingen (inclusief, afhankelijk van het land, staatsdruk). Dit is ook een interessante oplossing als de toegang tot commerciële hardware wallets beperkt of onmogelijk is in jouw regio.




## 1. Benodigde materialen



Om deze installatie uit te voeren, heb je het volgende nodig:




- De gebruikelijke apparatuur die een klassieke SeedSigner nodig heeft:
 - een Raspberry Pi Zero met GPIO-pinnen,
 - 1.3" Waveshare-scherm,
 - een compatibele camera,
 - een microSD-kaart.



![Image](assets/fr/01.webp)





- De SeedSigner uitbreidingskit, verkrijgbaar [bij de officiële Satochip winkel](https://satochip.io/product/seedsigner-extension-kit/), waarmee je direct vanaf je SeedSigner naar een smartcard kunt lezen en schrijven. Een andere optie is om [een externe smartcardlezer](https://satochip.io/product/chip-card-reader/) te gebruiken, die je met een kabel kunt aansluiten op een Micro-USB poort van de Raspberry Pi. Ik heb deze oplossing echter nog niet zelf getest;
- [Een Satochip](https://satochip.io/product/satochip/), of als alternatief een [blanco smartcard](https://satochip.io/product/card-for-diy-project/) waarop je de Satochip applet kunt installeren (de uitbreidingskit die door Satochip wordt verkocht bevat al een blanco smartcard). De uitbreidingskit van Satochip ondersteunt ook het formaat [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). Je kunt dus voor dit formaat kiezen als je dat liever hebt.



![Image](assets/fr/02.webp)



Voor meer details over de apparatuur die nodig is om een SeedSigner in elkaar te zetten, verwijzen we naar deel 1 van deze andere handleiding:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Firmware installeren



Om je SeedSigner met een Satochip te gebruiken, moet je een alternatieve firmware installeren, anders dan die van de originele SeedSigner, om het lezen van smartcards te ondersteunen. Hiervoor [raad ik aan fork van "**3rdIteration**" te gebruiken] (https://github.com/3rdIteration/seedsigner). Download [de laatste versie van de image](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) die overeenkomt met het Raspberry Pi-model dat je gebruikt.



![Image](assets/fr/03.webp)



Download de [Balena Etcher] software (https://etcher.balena.io/) als je die nog niet hebt en ga dan als volgt te werk:




- Plaats de microSD-kaart in uw computer;
- Lanceer Etcher ;
- Selecteer het bestand `.zip` dat je zojuist hebt gedownload;
- Selecteer de microSD-kaart als doel;
- Klik op `Flash!`.



![Image](assets/fr/04.webp)



Wacht tot het proces is voltooid: je microSD is nu klaar voor gebruik. Je kunt nu verder gaan met het in elkaar zetten van je apparaat.



Voor meer details over het installeren van de firmware en het verifiëren van de software (een stap die ik ten zeerste aanraad), zie de volgende tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. De smartcardlezer monteren



Begin met het installeren van de camera op de Raspberry Pi Zero, door deze voorzichtig in de camera-pen te steken en te vergrendelen met het zwarte lipje. Plaats vervolgens de Pi op de bodem van de behuizing en zorg ervoor dat de poorten uitgelijnd zijn met de corresponderende openingen.



![Image](assets/fr/05.webp)



Sluit vervolgens de smartcardlezer aan op de GPIO-pinnen van de Raspberry Pi Zero.



![Image](assets/fr/06.webp)



Schuif het plastic afdekplaatje over de smartcardlezer tot het correct geplaatst is.



![Image](assets/fr/07.webp)



Voeg vervolgens het scherm toe aan de GPIO-pinnen van de uitbreiding.



![Image](assets/fr/08.webp)



Plaats ten slotte de microSD-kaart met de firmware in de poort aan de zijkant van de Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Je kunt je SeedSigner nu aansluiten via de Micro-USB poort van de Raspberry Pi Zero, of via de USB-C poort van de uitbreiding. Beide opties werken. Wacht een paar seconden voor het opstarten, dan zou je het welkomstscherm moeten zien verschijnen.



![Image](assets/fr/10.webp)



Voor meer details over de initiële setup van je SeedSigner, raad ik je aan om deel 4 van de volgende tutorial te raadplegen:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Flash een smartcard met de Satochip applet (optioneel)



Als je al een Satochip hebt, kun je deze stap overslaan en direct naar stap 4 gaan. In dit gedeelte bekijken we hoe je de Satochip-applet op een lege smartcard installeert (doe-het-zelf-methode). De applet is gewoon een klein programma dat op de smartcard draait en waarmee we specifieke functies kunnen beheren.



Open om te beginnen het menu `Tools > Smartcard Tools` op uw SeedSigner.



![Image](assets/fr/11.webp)



Selecteer vervolgens `DIY Tools > Install Applet`.



![Image](assets/fr/12.webp)



Steek je smartcard in de SeedSigner lezer, met de chip naar beneden, en selecteer de `Satochip` applet.



![Image](assets/fr/13.webp)



Wees geduldig tijdens de installatie: het proces kan enkele tientallen seconden duren.



![Image](assets/fr/14.webp)



Als de applet met succes is geïnstalleerd, kun je doorgaan naar stap 4.



![Image](assets/fr/15.webp)




## 5. seed aanmaken en opslaan



### 5.1. seed genereren



Nu al je hardware en software naar behoren werken, kun je overgaan tot het aanmaken van je Bitcoin portfolio. Om dit te doen, sluit je je SeedSigner aan en dan generate je seed zoals met een conventionele SeedSigner, door de dobbelstenen te gooien of door een foto te nemen:




- Ga naar het menu `Tools > Camera / Dice Rolls`;
- Volg dan het entropiegeneratieproces volgens de gekozen methode;
- Maak tenslotte een back-up van de seed op fysieke media en controleer de back-up zorgvuldig.



![Image](assets/fr/16.webp)



Als je de details van deze procedure wilt zien, volg dan deel 5 van deze tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. De seed opslaan op een Seedkeeper



Zodra de seed is gegenereerd, is dit de enige keer dat het in het RAM van de SeedSigner verblijft. In mijn geval wil ik het opslaan op een [Seedkeeper](https://satochip.io/product/seedkeeper/), een ander Satochip product dat ontworpen is om geheimen op te slaan. Ik gebruik dit apparaat als laatste redmiddel, in geval van verlies van mijn Satochip.



De gekozen back-upstrategie hangt af van je voorkeuren, maar het is noodzakelijk om ten minste één kopie van je mnemonische zin te hebben, op fysieke media (papier of metaal) of, zoals hier, in een Seedkeeper. Je kunt het aantal back-ups naar behoefte ook vermenigvuldigen. Voor meer informatie over back-upstrategieën voor portfolio's, raad ik je aan deze tutorial te lezen:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Om een back-up te maken van je seed op een Seedkeeper, ga je direct naar het `Backup Seed` menu.



![Image](assets/fr/17.webp)



Steek dan je Seedkeeper in de smartcardlezer en selecteer `To SeedKeeper`.



![Image](assets/fr/18.webp)



Voer uw PIN-code in om te ontgrendelen.



![Image](assets/fr/19.webp)



Kies een `label` om gemakkelijk je verschillende geheimen te identificeren die op Seedkeeper zijn opgeslagen. Je kunt bijvoorbeeld gewoon de wallet opdruk behouden of expliciet `Zaad` aangeven. De keuze hangt af van je voorkeur en risico.



![Image](assets/fr/20.webp)



Als je back-up strategie alleen op deze Seedkeeper vertrouwt, raad ik je sterk aan om nu een lege hersteltest uit te voeren en dan de fingerprints te vergelijken om te controleren of de back-up werkt.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

De PIN-code van Seedkeeper moet zo lang en willekeurig mogelijk zijn, om brute force pogingen te voorkomen in het geval van fysieke compromittering van de kaart. Je moet ook een reservekopie van deze PIN-code bewaren, op een andere locatie dan Seedkeeper. Zonder deze PIN-code heb je geen toegang tot het mnemotechnisch geheugen dat is opgeslagen in Seedkeeper, en zijn je bitcoins voorgoed verloren.



### 5.3. seed besparen op de Satochip



Nu je portfolio gegenereerd, opgeslagen en geverifieerd is, gaan we het overbrengen naar de Satochip. Om dit te doen, zorg je ervoor dat de seed geladen is in het RAM van de SeedSigner. Ga dan naar `Tools > Smartcard Tools > Satochip Functions`.



![Image](assets/fr/21.webp)



Plaats je Satochip in de smartcardlezer en selecteer vervolgens `Initialiseren met zaad`.



![Image](assets/fr/22.webp)



Het apparaat vraagt je om de Satochip PIN-code in te voeren; omdat de kaart nieuw en nog niet geïnitialiseerd is, bestaat er nog geen PIN-code. Voer een willekeurige code in om deze stap over te slaan (het is geen blokkeringscode).



![Image](assets/fr/23.webp)



De SeedSigner detecteert dat uw Satochip niet is geïnitialiseerd. Klik op `Ik begrijp het` om te bevestigen.



![Image](assets/fr/24.webp)



Vervolgens kun je de Satochip PIN-code instellen, van 4 tot 16 tekens. Om de beveiliging van je wallet te versterken, kies je een lange, willekeurige code: het is de enige bescherming tegen fysieke toegang tot je geheugensteuntje.



Vergeet niet om deze PIN-code op te slaan zodra deze is aangemaakt, in een beveiligde wachtwoordmanager of op een fysieke drager, afhankelijk van uw persoonlijke strategie. In het laatste geval moet u ervoor zorgen dat u de gegevensdrager met de PIN nooit op dezelfde plaats bewaart als uw Satochip, anders is de bescherming nutteloos. Het is belangrijk om een reservekopie te hebben: **zonder deze PIN heb je geen toegang tot je seed, en zijn je bitcoins voor altijd verloren**.



![Image](assets/fr/25.webp)



De SeedSigner vraagt je vervolgens welke seed je wilt importeren in de Satochip. Selecteer degene waarvan de vingerafdruk overeenkomt met de portefeuille die je zojuist hebt aangemaakt.



![Image](assets/fr/26.webp)



Je seed is nu geïmporteerd in het Satochip.



![Image](assets/fr/27.webp)



Je kunt nu je SeedSigner uitschakelen.



Als je een passphrase BIP39 wilt gebruiken om de beveiliging van je wallet te verbeteren, raadpleeg dan deel 6 van deze tutorial:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. wallet importeren in Sparrow



Nu je portefeuille klaar is voor gebruik, importeren we de openbare informatie (de "*keystore*") in Sparrow Wallet of een andere software voor portefeuillebeheer. Deze software wordt gebruikt om je transacties aan te maken, te distribueren en bij te houden. Het zal ze echter niet kunnen ondertekenen, omdat alleen de Satochip (en eventuele back-ups) de privésleutels bevat die hiervoor nodig zijn.



### 6.1 De SeedSigner en Satochip voorbereiden



Plaats de microSD-kaart met het besturingssysteem en zet dan je SeedSigner aan. Op dit moment kan hij nog niets doen, omdat hij jouw seed nog niet kent. Je moet beginnen met de Satochip in de smartcardlezer te steken, want daar zit jouw seed op.



Open in het beginscherm het menu `Tools > Smartcard Tools > Satochip Functions`.



![Image](assets/fr/28.webp)



Klik vervolgens op `Export Xpub`.



![Image](assets/fr/29.webp)



Selecteer het type portefeuille. In ons geval is het een enkele portefeuille: selecteer `Single Sig`.



![Image](assets/fr/30.webp)



Nu komt de keuze van de scriptingstandaard. Kies de nieuwste: `Native SegWit`.



![Image](assets/fr/31.webp)



Selecteer ten slotte de `coördinator`, d.w.z. de software voor portefeuillebeheer die je wilt gebruiken. Hier gebruiken we Sparrow Wallet.



![Image](assets/fr/32.webp)



Er verschijnt een waarschuwing: dit is volkomen normaal. Met de uitgebreide publieke sleutel (`xpub`) kunt u alle adressen bekijken die zijn afgeleid van uw seed (op het eerste account). Het geeft echter geen toegang tot je fondsen: de onthulling ervan zou je privacy in gevaar brengen, maar niet de veiligheid van je bitcoins. Met andere woorden, je kunt je tegoeden bekijken, maar niet uitgeven.



Klik op `Ik begrijp het`.



![Image](assets/fr/33.webp)



Voer vervolgens de PIN-code van je Satochip in om deze te ontgrendelen. Dit is de code die je in stap 5 hebt gedefinieerd en opgeslagen.



![Image](assets/fr/34.webp)



Klik ten slotte op `Export Xpub` als je tevreden bent met de weergegeven informatie.



![Image](assets/fr/35.webp)



De SeedSigner genereert dan uw xpub in de vorm van een dynamische QR-code, die alle gegevens bevat die u nodig hebt om uw portfolio in Sparrow Wallet te beheren. Je kunt de helderheid van het scherm aanpassen met de joystick om het scannen van de QR-code te vergemakkelijken.



### 6.2 Een nieuw portfolio importeren in Sparrow Wallet



Zorg ervoor dat de Sparrow Wallet software op je computer is geïnstalleerd. Als je niet weet hoe je het moet downloaden, de echtheid ervan controleren en het correct installeren, raadpleeg dan onze volledige tutorial over dit onderwerp:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Open op je computer Sparrow Wallet en klik in de menubalk op `Bestand → Wallet importeren`.



![Image](assets/fr/36.webp)



Scroll naar beneden naar `SeedSigner` en selecteer vervolgens `Scan...`. Je webcam wordt geactiveerd: scan de dynamische QR-code die wordt weergegeven op je SeedSigner-scherm.



![Image](assets/fr/37.webp)



Geef je portfolio een naam en klik dan op `Creëer Wallet`. Sparrow zal je dan vragen een wachtwoord in te stellen om de lokale toegang tot deze wallet te vergrendelen. Kies een sterk wachtwoord: het beschermt uw gegevens in Sparrow (publieke sleutels, adressen, labels en transactiegeschiedenis). Dit wachtwoord is echter niet nodig om de wallet in de toekomst te herstellen: alleen je mnemotechnische zin (en mogelijk je passphrase) is dat nodig.



Ik raad je aan om dit wachtwoord op te slaan in een wachtwoordmanager, zodat je het niet kwijtraakt.



![Image](assets/fr/38.webp)



Uw sleutelbewaarplaats is met succes geïmporteerd.



![Image](assets/fr/39.webp)



Controleer nu of de `Master fingerprint` weergegeven in Sparrow Wallet overeenkomt met degene die eerder op jouw SeedSigner is gevonden.



De SeedSigner zal je dan vragen om een willekeurig ontvangstadres van je Sparrow wallet te scannen om de geldigheid van de import te bevestigen.



![Image](assets/fr/40.webp)



Uw Satochip (via SeedSigner) en Sparrow Wallet zijn nu veilig met elkaar verbonden. De Sparrow fungeert als volledige beheerinterface, terwijl de Satochip het enige apparaat blijft dat uw transacties kan ondertekenen. U bent nu klaar om bitcoins te ontvangen en te verzenden in een volledig air-gapped configuratie.



![Image](assets/fr/41.webp)



## 7. Bitcoins ontvangen en versturen



Je Satochip en Sparrow Wallet zijn nu geconfigureerd om samen te werken. In dit hoofdstuk leggen we stap voor stap uit hoe je in deze modus bitcoins kunt ontvangen en versturen.



### 7.1 Bitcoins ontvangen



#### 7.1.1 Een ontvangstadres genereren



Open op je computer Sparrow Wallet en ontgrendel je `Satochip-SeedSigner` wallet met je wachtwoord. Controleer of de software verbonden is met een server (indicator rechtsonder). Klik dan in de zijbalk op `Ontvangen`.



![Image](assets/fr/42.webp)



Er verschijnt een nieuw Bitcoin adres. U vindt :




- Het adres in tekstformaat (beginnend met `bc1q...` als je P2WPKH gebruikt, zoals in dit voorbeeld) ;
- De bijbehorende QR-code ;
- Een `Label` veld, handig voor het traceren van je transacties.



Ik raad je sterk aan om een label toe te voegen aan elk bitcoin-ontvangstbewijs in je wallet. Zo kun je de herkomst van elke UTXO gemakkelijk identificeren en je privacy beter beheren. Als je meer wilt weten over dit belangrijke onderwerp, bekijk dan de speciale training op Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Als u een label wilt toevoegen, voert u een naam in het veld `Label` in en bevestigt u.



Bijvoorbeeld:



```txt
Label : Sale of the Raspberry Pi Zero
```



Je adres is nu gekoppeld aan dit label in alle Sparrow secties.



![Image](assets/fr/43.webp)



#### 7.1.2 Address verificatie op de SeedSigner



Voordat je je ontvangstadres doorgeeft aan de betaler, is het belangrijk om te controleren of het bij je seed hoort. Deze stap zorgt ervoor dat je Satochip vervolgens transacties kan ondertekenen die aan dit adres gekoppeld zijn. Het voorkomt ook mogelijke aanvallen waarbij Sparrow een frauduleus adres zou weergeven. Houd er rekening mee dat Sparrow draait op een onveilige omgeving (jouw computer), waarvan het aanvalsoppervlak veel groter is dan dat van je Satochip, die volledig geïsoleerd is. Daarom moet je nooit blindelings vertrouwen op de adressen die in Sparrow worden weergegeven, voordat je ze op je wallet hardware hebt gecontroleerd.



Klik in Sparrow op de QR-code van het adres om het te vergroten: het wordt dan schermvullend weergegeven.



![Image](assets/fr/44.webp)



Plaats de Satochip op je SeedSigner in de lezer en selecteer `Scan` in het hoofdmenu. Scan de QR-code die wordt weergegeven op je computer en selecteer vervolgens `Gebruik Satochip kaart`.



![Image](assets/fr/45.webp)



Bevestig dan het type script dat is gebruikt (in dit geval `Native SegWit`), voer de Satochip PIN-code in om het te ontgrendelen en valideer de `xpub` informatie.



![Image](assets/fr/46.webp)



Als het gescande adres overeenkomt met het adres dat is afgeleid van jouw seed, zal de SeedSigner het bericht weergeven: `Address geverifieerd`.



![Image](assets/fr/47.webp)



Je kunt er dan zeker van zijn dat het adres bij je portfolio hoort.



#### 7.1.3 Ontvangst van fondsen



Je kunt dit adres nu in tekstvorm of via de QR-code doorsturen naar de persoon of afdeling die je satss moet sturen. Zodra de transactie is uitgezonden op het netwerk, verschijnt deze op het tabblad `Transacties` van Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Bitcoins versturen



Bitcoins versturen met de Satochip-SeedSigner configuratie bestaat uit 3 stappen:




- Transactie creëren in Sparrow ;
- Het ondertekenen van deze transactie op de Satochip, via de SeedSigner ;
- Tenslotte wordt de transactie over het netwerk uitgezonden vanaf Sparrow.



Alle uitwisselingen tussen de twee apparaten vinden uitsluitend plaats via QR-codes.



#### 7.2.1 De transactie in Sparrow aanmaken



In Sparrow Wallet kun je een transactie maken door op het tabblad `Versturen` in de linker zijbalk te klikken. Ik gebruik echter liever het tabblad `UTXO's`, waarmee je *Coin Controle* kunt uitoefenen. Deze methode biedt precieze controle over de UTXO's die worden uitgegeven, om de informatie die wordt onthuld tijdens je transacties te beperken.



Selecteer in het tabblad `UTXO's` de munten die u wilt uitgeven en klik vervolgens op `Verstuur Geselecteerd`.



![Image](assets/fr/49.webp)



Vul vervolgens de transactievelden in:




- Plak in `Betaal aan` het adres van de ontvanger of scan hun QR-code met het camerapictogram ;
- Voeg in `Label` een label toe om deze uitgave te traceren;
- Voer in `Bedrag` het bedrag in dat moet worden verzonden;
- Kies ten slotte de oplaadsnelheid volgens de huidige netwerkomstandigheden (schattingen zijn beschikbaar op [mempool.space](https://mempool.space/)).



Als je alle velden hebt ingevuld, bekijk je de informatie zorgvuldig en klik je op `Transactie maken >>`.



![Image](assets/fr/50.webp)



Controleer de transactiegegevens nog een laatste keer op juistheid en klik dan op `Transactie voltooien voor ondertekening`.



![Image](assets/fr/51.webp)



De transactie is nu klaar, maar nog niet ondertekend. Om de [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) als QR code weer te geven, klik op `Show QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 De transactie met Satochip ondertekenen



Zet je SeedSigner aan en plaats je Satochip zoals gewoonlijk. Selecteer op het beginscherm `Scan` en scan de QR-code die op de Sparrow staat.



![Image](assets/fr/53.webp)



Selecteer de optie `Satochipkaart gebruiken`.



![Image](assets/fr/54.webp)



Voer uw PIN-code in om de smartcard te ontgrendelen.



![Image](assets/fr/55.webp)



De SeedSigner detecteert dat dit een PSBT is en geeft een samenvatting van de transactie weer:




   - Het verzonden bedrag,
   - Bestemmingsadressen,
   - Gerelateerde transactiekosten.



Klik op `Bekijk Details` en bekijk alle informatie direct op het scherm van SeedSigner. De belangrijkste punten om te controleren zijn de verzonden bedragen, de bestemmingsadressen en de transactiekosten.



![Image](assets/fr/56.webp)



Als alles in orde is, selecteer dan `Approveer PSBT` om de transactie te ondertekenen met de Satochip.



![Image](assets/fr/57.webp)



Zodra de ondertekening voltooid is, genereert de SeedSigner een nieuwe QR-code met de ondertekende transactie, klaar om gescand te worden door Sparrow.



#### 7.2.3 De transactie uitzenden vanaf Sparrow



Nu de transactie ondertekend en gevalideerd is, hoeft deze alleen nog maar uitgezonden te worden op het Bitcoin netwerk, zodat een miner deze in een blok kan opnemen. Klik in Sparrow op `Scan QR`.



![Image](assets/fr/58.webp)



Presenteer de QR-code die op je SeedSigner staat (degene die de ondertekende transactie bevat) aan de webcam. Sparrow toont dan alle details van de transactie. Controleer of alle informatie correct is en klik dan op "Transactie uitzenden" om het uit te zenden op het Bitcoin netwerk.



![Image](assets/fr/59.webp)



Uw transactie wordt nu naar het netwerk verzonden. U kunt de bevestiging volgen op het tabblad `Transacties` van Sparrow Wallet.



![Image](assets/fr/60.webp)



## 8. Krijg je wallet terug



Zoals we in de vorige secties hebben gezien, zijn er, afhankelijk van je beveiligingsstrategie, verschillende manieren om een back-up te maken van je herstelzin naast je Satochip :




- Een klassieke *SeedQR* gebruiken met de SeedSigner ;
- Door de geheugensteunzin op een fysieke drager op te nemen;
- Of door het op te slaan op een Seedkeeper, zoals uitgelegd in sectie 5.2.



In elk geval zijn er 2 belangrijke situaties waarin je moet ingrijpen: verlies van de Satochip of verlies van de SeedSigner. Laten we eens kijken hoe je in elk van deze scenario's moet reageren.



### 8.1. Uw wallet ophalen met Satochip



Als je nog steeds je Satochip hebt, maar je SeedSigner is kapot of verloren, is de situatie vrij eenvoudig te beheren, omdat je wallet nog steeds in het Satochip zit.



De beste optie is om de benodigde onderdelen aan te bevelen en een nieuwe SeedSigner helemaal opnieuw op te bouwen. Aangezien dit een "stateless" apparaat is, maakt het niet uit of je dezelfde of een andere SeedSigner gebruikt: zolang je je Satochip kunt plaatsen, werkt alles normaal.



Als je er geen wilt herbouwen, kun je je Satochip ook op de klassieke manier gebruiken, d.w.z. direct vanaf je computer, zonder via de SeedSigner te gaan. Deze methode werkt perfect, maar vermindert de veiligheid van je Bitcoin wallet aanzienlijk: je verliest de "*air-gapped*" isolatie en moet nu blind ondertekenen, aangezien de SeedSigner als vertrouwd scherm fungeerde. Dit kan echter een tijdelijke oplossing zijn in een noodgeval, of als je niet in staat bent om een SeedSigner te herbouwen.



Hiervoor heb je een USB smartcard- of NFC-lezer nodig. Open de wallet die je wilt herstellen in Sparrow, ga dan naar het tabblad `Instellingen` en klik op `Vervangen`.



![Image](assets/fr/61.webp)



Plaats je Satochip in de smartcardlezer die op de computer is aangesloten en klik vervolgens op `Import` naast `Satochip`.



![Image](assets/fr/62.webp)



Voer tot slot de PIN-code van je smartcard in om hem te ontgrendelen. Vervolgens heb je toegang tot je wallet, kun je transacties aanmaken en direct ondertekenen met de aangesloten Satochip.



### 8.2. Haal je portfolio op met SeedSigner



Het andere, meer delicate scenario is wanneer u de toegang tot uw Satochip met seed verliest: of hij nu kapot, verloren of gestolen is, of u bent de PIN-code vergeten. Als je Satochip is gestolen of kwijtgeraakt, raden we je ten zeerste aan om, zodra de toegang tot je fondsen is hersteld, je bitcoins onmiddellijk over te boeken naar een gloednieuwe wallet, gegenereerd met een andere seed. Dit zorgt ervoor dat een potentiële aanvaller geen bitcoins meer kan stelen. Dit zorgt ervoor dat een potentiële aanvaller nooit toegang kan krijgen tot je satss.



Om opnieuw toegang te krijgen tot uw portefeuille en uw fondsen te verplaatsen, laadt u gewoon uw seed in SeedSigner. Afhankelijk van het back-upmedium dat u hebt gebruikt, hebt u verschillende opties:





- Voer uw mnemonische zin handmatig in in het menu `Zaden > seed van 12 woorden invoeren`.



![Image](assets/fr/63.webp)





- Scan je *SeedQR* door op de knop `Scan` te klikken op de startpagina.



![Image](assets/fr/64.webp)





- Of laad je seed van een Seedkeeper, via het `Seeds > From SeedKeeper` menu (dit is de methode die ik in deze tutorial gebruik). Je hoeft alleen maar de PIN van de Seedkeeper in te voeren en het geheim te selecteren dat gebruikt moet worden als seed op de SeedSigner.



![Image](assets/fr/65.webp)



Zodra de seed in de SeedSigner geladen is, welke methode je ook gebruikt, kun je één of meer scantransacties ondertekenen om je bitcoins naar een nieuwe, ongecompromitteerde wallet te verplaatsen. Om uit te vinden hoe je dit doet, zie deel 7.2 van de volgende tutorial:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Nu weet je hoe je Satochip kunt gebruiken om je Bitcoin portfolio veilig te beheren in combinatie met SeedSigner.



Als deze opstelling je heeft overtuigd, aarzel dan niet om de projecten te steunen die dit mogelijk maken:




- Door uw apparatuur rechtstreeks [op de website van Satochip] te kopen (https://satochip.io/shop/);
- Door [een donatie te doen aan het SeedSigner project](https://seedsigner.com/donate/);
- Door u te abonneren op het YouTube-kanaal van [Crypto Guide] (https://www.youtube.com/@CryptoGuide/), dat wordt beheerd door de persoon die de GitHub repository onderhoudt waarin de aangepaste firmware staat die we in deze tutorial hebben gebruikt.