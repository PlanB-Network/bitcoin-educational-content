---
name: Ledger Nano S Plus
description: Instelling en gebruik van de Ledger Nano S Plus
---
![cover](assets/cover.webp)


Een Hardware Wallet is een elektronisch apparaat dat de private sleutels van een Bitcoin Wallet beheert en beveiligt. In tegenstelling tot software wallets (of Hot wallets) die geïnstalleerd zijn op algemene machines die vaak verbonden zijn met het internet, maken hardware wallets de fysieke isolatie van private sleutels mogelijk, waardoor de risico's van hacken en diefstal beperkt worden.


Het belangrijkste doel van een Hardware Wallet is om de functionaliteiten van het apparaat zo klein mogelijk te houden om het aanvalsoppervlak te verkleinen. Een kleiner aanvalsoppervlak betekent ook minder potentiële aanvalsvectoren, d.w.z. minder zwakke plekken in het systeem die aanvallers kunnen uitbuiten om toegang te krijgen tot bitcoins.


Het is aan te raden om een Hardware Wallet te gebruiken om je bitcoins te beveiligen, vooral als je aanzienlijke hoeveelheden hebt, in absolute waarde of als deel van je totale vermogen.


Hardware wallets worden gebruikt in combinatie met een Wallet beheersoftware op een computer of smartphone. Deze software beheert de aanmaak van transacties, maar de cryptografische handtekening die nodig is om deze transacties te valideren, wordt alleen binnen de Hardware Wallet gezet. Dit betekent dat de privésleutels nooit worden blootgesteld aan een potentieel kwetsbare omgeving.


Hardware wallets bieden een dubbele bescherming voor de gebruiker: aan de ene kant beveiligen ze je bitcoins tegen aanvallen op afstand door de privésleutels offline te houden, en aan de andere kant bieden ze over het algemeen een betere fysieke weerstand tegen pogingen om de sleutels te ontfutselen. En het is precies op deze 2 veiligheidscriteria dat je de verschillende modellen op de markt kunt beoordelen en rangschikken.


In deze tutorial stel ik voor om een van deze oplossingen te ontdekken: de **Ledger Nano S Plus**.


![NANO S PLUS LEDGER](assets/notext/01.webp)


## Inleiding tot de Ledger Nano S Plus


De Ledger Nano S Plus is een Hardware Wallet geproduceerd door het Franse bedrijf Ledger, op de markt gebracht voor 79 €.


![NANO S PLUS LEDGER](assets/notext/02.webp)


De Nano S Plus is uitgerust met een CC EAL6+ gecertificeerde chip ("*secure element*"), die je geavanceerde bescherming biedt tegen fysieke aanvallen op de hardware. Het scherm en de knoppen worden rechtstreeks door deze chip aangestuurd. Een punt van kritiek dat vaak naar voren wordt gebracht is dat de code van deze chip niet open-source is, wat een zeker vertrouwen in de integriteit van dit onderdeel vereist. Toch wordt dit onderdeel gecontroleerd door onafhankelijke experts.


Qua gebruik werkt de Ledger Nano S Plus alleen via een bekabelde USB-C-verbinding.


Ledger onderscheidt zich van zijn concurrenten door de altijd zeer snelle overname van nieuwe Bitcoin functies, zoals Taproot of Miniscript, wat zeer gewaardeerd wordt.

Na het testen vind ik dat de Ledger Nano S Plus een uitstekend instapmodel Hardware Wallet is. Het biedt een hoog beveiligingsniveau voor een redelijke prijs. Het grootste nadeel ten opzichte van andere apparaten in dezelfde prijsklasse is het feit dat de firmwarecode niet open-source is. Ook is het scherm van de Nano S Plus relatief klein in vergelijking met duurdere modellen, zoals de Ledger Flex of de Coldcard Q1. Desalniettemin is de Interface erg goed ontworpen: ondanks de twee knoppen en het kleine scherm, blijft hij makkelijk te gebruiken, ook voor geavanceerde functies zoals de BIP39 passphrase. De Ledger Nano S Plus heeft geen batterij, Air-gap aansluiting, camera of micro SD-poort, maar dat is vrij normaal voor deze prijsklasse.


Naar mijn mening is de Ledger Nano S Plus een goede optie voor het beveiligen van je Bitcoin Wallet, en geschikt voor zowel beginners als gevorderden. In deze prijsklasse geef ik persoonlijk echter de voorkeur aan de Trezor Safe 3, die ongeveer dezelfde mogelijkheden biedt. Het voordeel van Trezor zit hem naar mijn mening in het beheer van de secure element: de Mnemonic zinnen en sleutels worden uitsluitend beheerd door open-source code, maar profiteren toch van de bescherming van de chip. Het nadeel van Trezor is dat ze soms erg traag zijn met het implementeren van nieuwe functies, in tegenstelling tot Ledger.


## Hoe koop ik een Ledger Nano S Plus?


De Ledger Nano S Plus is te koop [op de officiële website](https://shop.Ledger.com/products/Ledger-nano-s-plus). Om hem in een fysieke winkel te kopen, kunt u ook [de lijst van gecertificeerde wederverkopers](https://www.Ledger.com/reseller) op de Ledger website vinden.


## Vereisten


Zodra je je Ledger Nano hebt ontvangen, is de eerste stap om de verpakking te controleren om er zeker van te zijn dat deze niet geopend is. Als de verpakking beschadigd is, kan dit erop wijzen dat de Hardware Wallet beschadigd is en misschien niet authentiek is.


Bij het openen zou je de volgende items in de doos moeten vinden:


- De Ledger Nano S Plus;
- Een USB-C naar USB-A kabel;
- Een gebruikershandleiding;
- Kaarten om je Mnemonic zin op te schrijven.


Voor deze tutorial hebt u 2 softwaretoepassingen nodig: Ledger Live om de Ledger te initialiseren, en Sparrow wallet om uw Bitcoin Wallet te beheren. Download [Ledger Live](https://www.Ledger.com/Ledger-live) en [Sparrow wallet](https://sparrowwallet.com/download/) van hun officiële websites.


![NANO S PLUS LEDGER](assets/notext/03.webp)

Voor deze twee softwareprogramma's raad ik sterk aan om zowel hun authenticiteit (met GnuPG) als hun integriteit (via de Hash) te controleren voordat je ze op je machine installeert. Als je niet zeker weet hoe je dit moet doen, kun je deze andere tutorial volgen:

https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Hoe een Ledger Nano initialiseren?


Sluit je Nano aan op je computer waar Ledger Live en Sparrow wallet geïnstalleerd zijn. Om op je Ledger te navigeren, gebruik je de linkertoets om naar links te gaan en de rechtertoets om naar rechts te gaan. Om een optie te selecteren of te bevestigen, druk je tegelijkertijd op beide knoppen.


![NANO S PLUS LEDGER](assets/notext/04.webp)


Blader door de verschillende introductiepagina's en klik dan op de 2 knoppen om te beginnen.


![NANO S PLUS LEDGER](assets/notext/05.webp)


Selecteer de optie "*Instellen als nieuw apparaat*".


![NANO S PLUS LEDGER](assets/notext/06.webp)


Kies de PIN-code die gebruikt zal worden om uw Ledger te ontgrendelen. Dit is dus een bescherming tegen ongeautoriseerde fysieke toegang. Deze PIN-code speelt geen rol bij het afleiden van de cryptografische sleutels van uw Wallet. Dus zelfs zonder toegang tot deze PIN-code, kunt u met uw Mnemonic zin van 24 woorden weer toegang krijgen tot uw bitcoins.


![NANO S PLUS LEDGER](assets/notext/07.webp)


Het wordt aanbevolen om een 8-cijferige pincode te kiezen, zo willekeurig mogelijk. Zorg er ook voor dat u deze code op een andere plaats opslaat dan waar uw Ledger Nano S Plus is opgeslagen (bijvoorbeeld in een wachtwoordmanager).


Gebruik de knoppen om over de cijfers te bewegen en selecteer vervolgens elk cijfer door tegelijkertijd op beide knoppen te klikken.


![NANO S PLUS LEDGER](assets/notext/08.webp)


Voer uw pincode een tweede keer in om deze te bevestigen.


![NANO S PLUS LEDGER](assets/notext/09.webp)


Uw Nano geeft instructies over hoe u uw herstelzin kunt beheren.


**Deze Mnemonic zin geeft volledige en onbeperkte toegang tot al je bitcoins**. Iedereen die in het bezit is van deze zin kan uw fondsen stelen, zelfs zonder fysieke toegang tot uw Ledger. Met de 24-woorden zin kunt u de toegang tot uw bitcoins herstellen in geval van verlies, diefstal of schade aan uw Ledger Nano. Het is daarom erg belangrijk om het zorgvuldig op te slaan en te bewaren op een veilige locatie.


Je kunt het opschrijven op het kartonnen papier dat bij je Ledger wordt geleverd, of voor meer veiligheid raad ik aan om het te graveren op een roestvrijstalen drager om het te beschermen tegen de risico's van brand, overstromingen of instortingen.


Je kunt door deze instructies bladeren en pagina's overslaan door op de rechterknop te klikken.


![NANO S PLUS LEDGER](assets/notext/10.webp)

De Ledger zal uw Mnemonic zin creëren met behulp van zijn willekeurige nummergenerator. Zorg ervoor dat u tijdens deze handeling niet geobserveerd wordt. Schrijf de door de Ledger gegeven woorden op een fysieke drager van uw keuze. Afhankelijk van uw beveiligingsstrategie kunt u overwegen om meerdere volledige fysieke kopieën van de zin te maken (maar het is belangrijk dat u ze niet opsplitst). Het is cruciaal om de woorden genummerd en in volgorde te houden.

***Het spreekt voor zich dat je deze woorden nooit mag delen op het internet, in tegenstelling tot wat ik doe in deze tutorial. Dit voorbeeld Wallet zal alleen gebruikt worden op de Testnet en zal na de tutorial verwijderd worden.***


![NANO S PLUS LEDGER](assets/notext/11.webp)


Klik op de rechterknop om naar de volgende woorden te gaan.


![NANO S PLUS LEDGER](assets/notext/12.webp)


Zodra alle woorden zijn genoteerd, klik je op de 2 knoppen om naar de volgende stap te gaan.


![NANO S PLUS LEDGER](assets/notext/13.webp)


Klik op de twee knoppen "*Bevestig je Herstelzin*", selecteer dan de woorden van je Mnemonic zin in hun volgorde om te bevestigen dat je ze correct hebt genoteerd. Gebruik de linker- en rechterknop om tussen de opties te navigeren en selecteer dan het juiste woord door op de 2 knoppen te klikken. Ga door met deze procedure tot het 24e woord.


![NANO S PLUS LEDGER](assets/notext/14.webp)


Als de zin die je bevestigt precies overeenkomt met de zin die de Ledger je in de vorige stap gaf, kun je doorgaan. Zo niet, dan is uw fysieke back-up van de Mnemonic frase onjuist en moet u het proces opnieuw starten.


![NANO S PLUS LEDGER](assets/notext/15.webp)


En daar heb je het, je seed is correct aangemaakt op je Ledger Nano S Plus. Voordat we verder gaan met het maken van een nieuwe Bitcoin Wallet vanaf deze seed, gaan we samen de instellingen van het apparaat bekijken.


## Hoe wijzig je de instellingen van je Ledger?


Houd de 2 knoppen enkele seconden ingedrukt om de instellingen te openen.


![NANO S PLUS LEDGER](assets/notext/16.webp)


Klik op het menu "*Instellingen*".


![NANO S PLUS LEDGER](assets/notext/17.webp)


En kies "*Algemeen*".


![NANO S PLUS LEDGER](assets/notext/18.webp)


In het menu "*Language*" kunt u de displaytaal wijzigen.


![NANO S PLUS LEDGER](assets/notext/19.webp)


In het menu "*helderheid*" kun je de helderheid van het scherm aanpassen. We zijn nu niet geïnteresseerd in de rest van de algemene instellingen.


![NANO S PLUS LEDGER](assets/notext/20.webp)


Ga nu naar de instellingensectie "*Veiligheid*".


![NANO S PLUS LEDGER](assets/notext/21.webp)


met "*Change PIN*" kunt u uw pincode wijzigen.

![NANO S PLUS LEDGER](assets/notext/22.webp)

met "*passphrase*" kunt u een passphrase voor BIP39 instellen. De passphrase is een optioneel wachtwoord dat, in combinatie met uw herstelzin, een extra Layer beveiliging voor uw Wallet biedt.


![NANO S PLUS LEDGER](assets/notext/23.webp)


Op dit moment wordt je Wallet gegenereerd uit een Mnemonic zinsdeel dat uit 24 woorden bestaat. Deze herstelzin is erg belangrijk, omdat je hiermee alle sleutels van je Wallet kunt herstellen in geval van verlies. Het vormt echter een single point of failure (SPOF). Als het gecompromitteerd is, zijn je bitcoins in gevaar. Hier komt de passphrase om de hoek kijken. Het is een optioneel wachtwoord, dat je willekeurig kunt kiezen, dat de Mnemonic zin aanvult om de beveiliging van de Wallet te verbeteren.


De passphrase moet niet verward worden met de PIN-code. Het speelt een rol bij de afleiding van je cryptografische sleutels. Het werkt samen met de Mnemonic-zin en verandert de seed waaruit de sleutels worden gegenereerd. Dus zelfs als iemand je 24-woorden zin bemachtigt, zonder de passphrase, kunnen ze geen toegang krijgen tot je fondsen. Het gebruik van een passphrase creëert in wezen een nieuwe Wallet met verschillende sleutels. Als je de passphrase (ook al is het maar een klein beetje) verandert, krijg je een andere Wallet.


De passphrase is een zeer krachtig hulpmiddel om de veiligheid van je bitcoins te verbeteren. Het is echter erg belangrijk om te begrijpen hoe het werkt voordat je het implementeert, om te voorkomen dat je de toegang tot je Wallet verliest. Daarom raad ik je aan deze andere tutorial te raadplegen, speciaal als je een passphrase op je Ledger wilt installeren:


https://planb.academy/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Met het menu "*PIN lock*" kun je de automatische vergrendeling van je Ledger configureren en activeren na een bepaalde periode van inactiviteit.


![NANO S PLUS LEDGER](assets/notext/24.webp)


Met het menu "*Schermbeveiliging*" kunt u de slaapstand van uw Ledger Nano instellen. Merk op dat de schermbeveiliging bij het ontwaken geen PIN-invoer vereist, tenzij de optie "*PIN lock*" geactiveerd is om overeen te komen met de slaapstand. Deze functie is vooral handig voor Ledger Nano X apparaten met een batterij, om het energieverbruik te verminderen.


![NANO S PLUS LEDGER](assets/notext/25.webp)


Tenslotte kun je in het menu "*Reset device*" je Ledger resetten. Ga alleen verder met deze reset als je zeker weet dat het geen sleutels bevat die bitcoins beveiligen, omdat je permanent de toegang tot je fondsen zou kunnen verliezen. Deze optie kan handig zijn voor het uitvoeren van een lege hersteltest, maar daar zal ik later wat meer over vertellen.


![NANO S PLUS LEDGER](assets/notext/26.webp)

## Hoe installeer ik de Bitcoin toepassing?


Start eerst de Ledger Live software op uw computer, sluit dan uw Ledger Nano aan en ontgrendel deze. Ga in Ledger Live naar het menu "*Mijn Ledger*". U wordt gevraagd om de toegang tot uw Nano te autoriseren.


![NANO S PLUS LEDGER](assets/notext/27.webp)


Bevestig de toegang op uw Ledger door op de twee knoppen te klikken.


![NANO S PLUS LEDGER](assets/notext/28.webp)


Controleer eerst op Ledger Live of de "*Genuine check*" verschijnt. Dit bevestigt dat uw apparaat authentiek is.


![NANO S PLUS LEDGER](assets/notext/29.webp)


Als de firmware van uw Ledger Nano niet up-to-date is, zal Ledger Live automatisch aanbieden om deze te updaten. Klik indien nodig op "*Update firmware*" en vervolgens op "*Install update*" om de installatie te starten. Klik op uw Ledger op de twee knoppen om te bevestigen en wacht tijdens de installatie.


Tot slot voegen we de Bitcoin-toepassing toe. Klik hiervoor op Ledger Live op de knop "*Installeren*" naast "*Bitcoin (BTC)*".


![NANO S PLUS LEDGER](assets/notext/30.webp)


De toepassing wordt op je Nano geïnstalleerd.


![NANO S PLUS LEDGER](assets/notext/31.webp)


Vanaf nu hebt u de Ledger Live software niet meer nodig voor het reguliere beheer van uw Wallet. U kunt er af en toe naar terugkeren om de firmware bij te werken als er nieuwe versies beschikbaar zijn. Voor al het andere zullen we Sparrow wallet gebruiken, wat een veel uitgebreider hulpmiddel is voor het effectief beheren van een Bitcoin Wallet.


![NANO S PLUS LEDGER](assets/notext/32.webp)


## Hoe installeer ik een nieuwe Bitcoin Wallet met Sparrow?


Open Sparrow wallet en sla de introductiepagina's over om naar het beginscherm te gaan. Controleer of je correct verbonden bent met een knooppunt door de schakelaar rechtsonder in het scherm te zien.


![NANO S PLUS LEDGER](assets/notext/33.webp)


Ik raad sterk aan om je eigen Bitcoin node te gebruiken. In deze tutorial gebruik ik een publieke node (geel) omdat ik op de Testnet zit, maar voor normaal gebruik kun je beter kiezen voor een lokale Bitcoin core (Green) of een Electrum server verbonden met een remote node (blauw).


Klik op het menu "*Bestand*" en dan op "*Nieuw Wallet*".


![NANO S PLUS LEDGER](assets/notext/34.webp)


Kies een naam voor deze Wallet en klik dan op "*Create Wallet*".


![NANO S PLUS LEDGER](assets/notext/35.webp)


Selecteer in het vervolgkeuzemenu "*Script Type*" het type script dat zal worden gebruikt om je bitcoins te beveiligen. Ik raad aan te kiezen voor "*Taproot*", of indien niet beschikbaar, "*Native SegWit*".


![NANO S PLUS LEDGER](assets/notext/36.webp)

Klik op de knop "*Gekoppelde Hardware Wallet*".

![NANO S PLUS LEDGER](assets/notext/37.webp)


Als u dit nog niet gedaan heeft, sluit dan uw Ledger Nano S Plus aan op de computer, ontgrendel hem met uw pincode en open dan de "*Bitcoin*" applicatie door één keer op de 2 knoppen te klikken op het Bitcoin logo.


*In deze tutorial gebruik ik de Bitcoin Testnet toepassing, maar de procedure blijft hetzelfde voor de Mainnet.*


![NANO S PLUS LEDGER](assets/notext/38.webp)


Klik op Sparrow op de knop "*Scan*".


![NANO S PLUS LEDGER](assets/notext/39.webp)


Klik vervolgens op "*Import Keystore*".


![NANO S PLUS LEDGER](assets/notext/40.webp)


U ziet nu de details van uw Wallet, inclusief de uitgebreide publieke sleutel van uw eerste account. Klik op de knop "*Toepassen*" om het aanmaken van de Wallet te voltooien.


![NANO S PLUS LEDGER](assets/notext/41.webp)


Kies een sterk wachtwoord om de toegang tot Sparrow wallet te beveiligen. Dit wachtwoord verzekert de veiligheid van de toegang tot uw Wallet gegevens op Sparrow, wat helpt om uw publieke sleutels, adressen, labels en transactiegeschiedenis te beschermen tegen ongeautoriseerde toegang.


Ik raad je aan om dit wachtwoord op te slaan in een wachtwoordmanager zodat je het niet vergeet.


![NANO S PLUS LEDGER](assets/notext/42.webp)


En daar heb je het, je Wallet is nu gemaakt!


![NANO S PLUS LEDGER](assets/notext/43.webp)


Voordat u uw eerste bitcoins in uw Wallet ontvangt, **raad ik u ten zeerste aan om een dry-run hersteltest** uit te voeren. Noteer een referentiegegeven, zoals je xpub, en reset dan je Ledger Nano terwijl de Wallet nog leeg is. Probeer daarna uw Wallet op de Ledger te herstellen met behulp van uw papieren back-ups. Controleer of de gegenereerde xpub na het herstel overeenkomt met degene die je in eerste instantie hebt genoteerd. Als dat zo is, kun je er zeker van zijn dat je papieren back-ups betrouwbaar zijn.


Om meer te leren over hoe je een hersteltest uitvoert, raad ik je aan om deze andere tutorial te raadplegen:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Hoe ontvang ik bitcoins met de Ledger Nano?


Klik op het tabblad "*Ontvangen*".


![NANO S PLUS LEDGER](assets/notext/44.webp)


Sluit uw Ledger Nano S Plus aan op de computer, ontgrendel hem met uw pincode en open dan de "*Bitcoin*"-toepassing.


![NANO S PLUS LEDGER](assets/notext/45.webp)

Voordat u de Address gebruikt die door Sparrow wallet wordt verstrekt, moet u deze verifiëren op het scherm van uw Ledger. Met deze praktijk kunt u bevestigen dat de Address die wordt weergegeven op de Sparrow niet frauduleus is en dat de Hardware Wallet inderdaad de privésleutel bezit die nodig is om de bitcoins die met deze Address zijn beveiligd, later uit te geven. Dit helpt je om verschillende soorten aanvallen te vermijden.

Om deze verificatie uit te voeren, klik je op de knop "*Weergave Address*".


![NANO S PLUS LEDGER](assets/notext/46.webp)


Controleer of de Address die op je Ledger staat, overeenkomt met de Sparrow wallet. Het is ook aan te raden om deze controle uit te voeren vlak voordat je je Address aan de verzender geeft, om zeker te zijn van de geldigheid. Je kunt de knoppen gebruiken om de volledige Address te bekijken.


![NANO S PLUS LEDGER](assets/notext/47.webp)


Klik vervolgens op "*Approve*" als de adressen inderdaad identiek zijn.


![NANO S PLUS LEDGER](assets/notext/48.webp)


Je kunt een "*Label*" toevoegen om de bron te beschrijven van de bitcoins die beveiligd zullen worden met deze Address. Dit is een goede manier om je UTXO's beter te beheren.


![NANO S PLUS LEDGER](assets/notext/49.webp)


Voor meer informatie over labelen raad ik je ook aan om deze andere tutorial te bekijken:


https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Je kunt deze Address dan gebruiken om bitcoins te ontvangen.


![NANO S PLUS LEDGER](assets/notext/50.webp)


## Hoe verstuur ik bitcoins met de Ledger Nano?


Nu je je eerste Sats hebt ontvangen in je Wallet die beveiligd is met de Nano S Plus, kun je ze ook uitgeven! Sluit je Ledger aan op je computer, ontgrendel hem, start Sparrow wallet en ga dan naar het tabblad "*Versturen*" om een nieuwe transactie te maken.


![NANO S PLUS LEDGER](assets/notext/51.webp)


Als je "*Coin controle*" wilt doen, d.w.z. specifiek wilt kiezen welke UTXO's je in de transactie wilt gebruiken, ga dan naar het tabblad "*UTXO's*". Selecteer de UTXO's die je wilt uitgeven en klik vervolgens op "*Verstuur Geselecteerd*". Je wordt doorgestuurd naar hetzelfde scherm van het tabblad "*Versturen*", maar met je UTXO's al geselecteerd voor de transactie.


![NANO S PLUS LEDGER](assets/notext/52.webp)


Voer de bestemming Address in. Je kunt ook meerdere adressen invoeren door op de knop "*+ Toevoegen*" te klikken.


![NANO S PLUS LEDGER](assets/notext/53.webp)


Noteer een "*Label*" om het doel van deze uitgave te onthouden.


![NANO S PLUS LEDGER](assets/notext/54.webp)


Kies het bedrag dat naar deze Address wordt gestuurd.


![NANO S PLUS LEDGER](assets/notext/55.webp)


Pas de transactiekosten aan volgens de huidige markt.


![NANO S PLUS LEDGER](assets/notext/56.webp)

Controleer of alle instellingen van je transactie correct zijn en klik dan op "*Transactie maken*".

![NANO S PLUS LEDGER](assets/notext/57.webp)


Als alles er goed uitziet, klik je op "*Transactie voltooien voor ondertekening*".


![NANO S PLUS LEDGER](assets/notext/58.webp)


Klik op "*Teken*".


![NANO S PLUS LEDGER](assets/notext/59.webp)


Klik op "*Teken*" naast uw Ledger Nano S Plus.


![NANO S PLUS LEDGER](assets/notext/60.webp)


Controleer de transactie-instellingen op het scherm van je Ledger, inclusief de ontvangende Address van de ontvanger, het verzonden bedrag en het bedrag aan kosten.


![NANO S PLUS LEDGER](assets/notext/61.webp)


Als alles er goed uitziet, druk dan op de twee knoppen bij "*Teken transactie*" om te ondertekenen.


![NANO S PLUS LEDGER](assets/notext/62.webp)


Je transactie is nu ondertekend. Controleer of alles er goed uitziet en klik dan op "*Zend transactie uit*" om het uit te zenden op het Bitcoin netwerk.


![NANO S PLUS LEDGER](assets/notext/63.webp)


Je kunt het vinden in het tabblad "*Transacties*" van Sparrow wallet.


![NANO S PLUS LEDGER](assets/notext/64.webp)


Gefeliciteerd, u bent nu op de hoogte van het basisgebruik van de Ledger Nano S Plus met Sparrow wallet! In een toekomstige tutorial zullen we zien hoe we de Ledger met Liana kunnen gebruiken om Miniscript te gebruiken.


Als je deze handleiding nuttig vond, zou ik het waarderen als je hieronder een duim omhoog achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Ik raad je ook aan om deze complete tutorial over de Ledger Flex te bekijken:


https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a