---
name: Ledger Flex
description: De Ledger Flex instellen en gebruiken
---
![cover](assets/cover.webp)


![video](https://youtu.be/V3wnS9_Ieyc)


Een Hardware Wallet is een elektronisch apparaat dat de private sleutels van een Bitcoin Wallet beheert en beveiligt. In tegenstelling tot software wallets (of Hot wallets) die geïnstalleerd zijn op algemene machines die vaak verbonden zijn met het internet, maken hardware wallets de fysieke isolatie van private sleutels mogelijk, waardoor de risico's van hacken en diefstal beperkt worden.


Het hoofddoel van een Hardware Wallet is het minimaliseren van de functionaliteiten van het apparaat om het aanvalsoppervlak te verkleinen. Minder aanvalsoppervlak betekent ook minder potentiële aanvalsvectoren, d.w.z. minder zwakke punten in het systeem die aanvallers kunnen uitbuiten om toegang te krijgen tot bitcoins.


Het is aan te raden om een Hardware Wallet te gebruiken om je bitcoins te beveiligen, vooral als je aanzienlijke hoeveelheden hebt, in absolute waarde of als deel van je totale vermogen.


Hardware wallets worden gebruikt in combinatie met Wallet beheersoftware op een computer of smartphone. Deze software beheert de aanmaak van transacties, maar de cryptografische handtekening die nodig is om deze transacties te valideren, wordt alleen binnen de Hardware Wallet gezet. Dit betekent dat de privésleutels nooit worden blootgesteld aan een potentieel kwetsbare omgeving.


Hardware wallets bieden een dubbele bescherming voor de gebruiker: aan de ene kant beveiligen ze je bitcoins tegen aanvallen op afstand door de privésleutels offline te houden, en aan de andere kant bieden ze over het algemeen een betere fysieke weerstand tegen pogingen om de sleutels te ontfutselen. En het is precies op deze 2 veiligheidscriteria dat je de verschillende modellen op de markt kunt beoordelen en rangschikken.


In deze tutorial stel ik voor om een van deze oplossingen te ontdekken: de **Ledger Flex**.


![LEDGER FLEX](assets/notext/01.webp)


## Inleiding tot de Ledger Flex


De Ledger Flex is een Hardware Wallet geproduceerd door het Franse bedrijf Ledger, op de markt gebracht voor 249 €.


![LEDGER FLEX](assets/notext/02.webp)


Het heeft een groot E Ink touchscreen, een zwart-wit displaytechnologie. Dit is dezelfde technologie als in elektronische lezers. Het E Ink scherm zorgt voor een helder en leesbaar scherm, zelfs in fel zonlicht, en verbruikt zeer weinig energie, of helemaal geen energie als het scherm statisch is. Het werkt met microcapsules die zwarte en witte pigmentdeeltjes bevatten. Wanneer er een elektrische lading wordt toegepast, bewegen de zwarte of witte deeltjes naar het oppervlak van het scherm, waardoor tekst of afbeeldingen kunnen worden gevormd.

De Ledger Flex is uitgerust met een CC EAL6+ gecertificeerde "secure element" chip, die je geavanceerde bescherming biedt tegen fysieke aanvallen op de hardware. Het scherm wordt rechtstreeks door deze chip aangestuurd. Een veelgehoord punt van kritiek is dat de code voor deze chip niet open-source is, waardoor je een zeker vertrouwen in de integriteit van dit onderdeel moet hebben. Dit onderdeel wordt echter gecontroleerd door onafhankelijke experts.


Qua gebruik biedt de Ledger Flex verschillende connectiviteitsopties: Bluetooth, USB-C en NFC. Dankzij het grote scherm kun je gemakkelijk je transactiegegevens verifiëren. De Ledger onderscheidt zich ook van zijn concurrenten door de snelle toepassing van nieuwe Bitcoin functies, zoals Miniscript.


Na het testen ben ik onder de indruk van de kwaliteit van het product. De gebruikerservaring is uitstekend en het apparaat werkt intuïtief. Het is een uitstekende Hardware Wallet. Het heeft naar mijn mening echter 2 grote nadelen: het onvermogen om de code van de chip te verifiëren en natuurlijk de prijs, die aanzienlijk hoger ligt dan die van de concurrenten. Ter vergelijking: het meest geavanceerde model van Foundation wordt verkocht voor $199, dat van Coinkite voor $219,99, terwijl de nieuwste Trezor, ook uitgerust met een groot touchscreen, wordt aangeboden voor 169€.


## Hoe koop ik een Ledger Flex?


De Ledger Flex is te koop [op de officiële website](https://shop.Ledger.com/pages/Ledger-flex). Om hem in een fysieke winkel te kopen, kun je ook [de lijst van gecertificeerde wederverkopers](https://www.Ledger.com/reseller) vinden op de Ledger website.


## Vereisten


Zodra je je Ledger Flex hebt ontvangen, is de eerste stap de verpakking te onderzoeken om er zeker van te zijn dat deze niet geopend is.


![LEDGER FLEX](assets/notext/03.webp)


De verpakking van de Ledger moet 2 sealstrips bevatten. Als deze strips ontbreken of beschadigd zijn, kan dit erop wijzen dat de Hardware Wallet beschadigd is en mogelijk niet authentiek is.


![LEDGER FLEX](assets/notext/04.webp)


Bij het openen zou je de volgende items in de doos moeten vinden:


- De Ledger Flex;
- Een USB-C kabel;
- Een gebruikershandleiding;
- Kaarten om je Mnemonic zin op te schrijven.


![LEDGER FLEX](assets/notext/05.webp)


Voor deze tutorial heb je 2 stukjes software nodig: Ledger Live om de Ledger Flex te initialiseren, en Sparrow wallet om je Bitcoin Wallet te beheren. Download [Ledger Live] (https://www.Ledger.com/Ledger-live) en [Sparrow wallet] (https://sparrowwallet.com/download/) van hun officiële websites.


![LEDGER FLEX](assets/notext/06.webp)

We zullen binnenkort een tutorial aanbieden over hoe je de authenticiteit en integriteit van software die je downloadt kunt verifiëren. Ik raad je aan dit hier te doen voor Ledger Live en Sparrow.

## Hoe initialiseer ik een Ledger Flex met Ledger Live?


Zet je Ledger Flex aan door enkele seconden op de knop aan de rechterkant te drukken.


![LEDGER FLEX](assets/notext/07.webp)


Blader door de verschillende introductiepagina's.


![LEDGER FLEX](assets/notext/08.webp)


Selecteer de optie "*Instellen zonder Ledger Live*" en klik dan op de knop "*Skip Ledger Live*".


![LEDGER FLEX](assets/notext/09.webp)


Vervolgens wordt u gevraagd een naam te kiezen voor uw Ledger. Klik op "*Naam instellen*" en voer de naam van uw keuze in.


![LEDGER FLEX](assets/notext/10.webp)


Kies de pincode voor uw toestel, die zal worden gebruikt om uw Ledger te ontgrendelen. Dit is dus een bescherming tegen ongeautoriseerde fysieke toegang. Deze PIN-code speelt geen rol bij het afleiden van de cryptografische sleutels van uw Wallet. Dus zelfs zonder toegang tot deze PIN-code, kunt u met uw Mnemonic zin van 24 woorden weer toegang krijgen tot uw bitcoins.


Het is aan te raden om een 8-cijferige PIN-code te kiezen, zo willekeurig mogelijk. Zorg er ook voor dat je deze code op een andere plaats opslaat dan waar je Ledger Flex is opgeslagen (bijvoorbeeld in een wachtwoordmanager).


![LEDGER FLEX](assets/notext/11.webp)


Voer uw pincode een tweede keer in om deze te bevestigen.


![LEDGER FLEX](assets/notext/12.webp)


Je wordt dan gevraagd om te kiezen tussen het herstellen van een bestaande Wallet of het maken van een nieuwe. In deze tutorial behandelen we het maken van een nieuwe Wallet vanaf nul, dus kies de optie "*Instellen als een nieuwe Ledger*" om generate een nieuwe Mnemonic zin te geven.


![LEDGER FLEX](assets/notext/13.webp)


Je Flex zal je instructies geven over hoe je je herstelfase kunt beheren.


**Deze Mnemonic zin geeft volledige en onbeperkte toegang tot al je bitcoins**. Iedereen die in het bezit is van deze zin kan uw fondsen stelen, zelfs zonder fysieke toegang tot uw Ledger. De 24-woord zin maakt het mogelijk om de toegang tot je bitcoins te herstellen in geval van verlies, diefstal of schade aan je Ledger Flex. Het is daarom erg belangrijk om het zorgvuldig te bewaren en op te slaan op een veilige locatie.


Je kunt het opschrijven op het kartonnen papier dat bij je Ledger wordt geleverd, of voor extra veiligheid raad ik aan het te graveren op een roestvrijstalen drager om het te beschermen tegen de risico's van branden, overstromingen of instortingen.


Je kunt door deze instructies bladeren en pagina's overslaan door het scherm aan te raken.


![LEDGER FLEX](assets/notext/14.webp)

De Ledger zal uw Mnemonic zin creëren met behulp van zijn willekeurige nummergenerator. Zorg ervoor dat je niet geobserveerd wordt tijdens deze handeling. Schrijf de door de Ledger gegeven woorden op een fysiek medium naar keuze. Afhankelijk van je beveiligingsstrategie, kun je overwegen om meerdere volledige fysieke kopieën van de zin te maken (maar het belangrijkste is, splits ze niet). Het is belangrijk om de woorden genummerd en in volgorde te houden.

***Het spreekt voor zich dat je deze woorden nooit mag delen op het internet, in tegenstelling tot wat ik doe in deze tutorial. Dit voorbeeld Wallet zal alleen gebruikt worden op de Testnet en zal aan het einde van de tutorial verwijderd worden.***


![LEDGER FLEX](assets/notext/15.webp)


Klik op de knop "*Volgende*" om naar de volgende groep woorden te gaan. Als alle woorden zijn genoteerd, klik je op de knop "*Done*" om door te gaan naar de volgende stap.


![LEDGER FLEX](assets/notext/16.webp)


Klik op de knop "*Start bevestiging*" en selecteer de woorden uit je Mnemonic zin in hun volgorde om te bevestigen dat je ze correct hebt genoteerd. Ga door met deze procedure tot het 24e woord.


![LEDGER FLEX](assets/notext/17.webp)


Als de zin die je bevestigt precies overeenkomt met de zin die de Flex je in de vorige stap heeft gegeven, kun je doorgaan. Zo niet, dan is je fysieke back-up van de Mnemonic-zin onjuist en moet je het proces opnieuw starten.


![LEDGER FLEX](assets/notext/18.webp)


En daar heb je het, je seed is correct aangemaakt op je Ledger Flex. Voordat we verder gaan met het maken van een nieuwe Bitcoin Wallet vanuit deze seed, gaan we samen de apparaatinstellingen bekijken.


## Hoe wijzig je de instellingen van je Ledger?


Om je Ledger te vergrendelen en ontgrendelen, druk je op de zijknop. Je wordt dan gevraagd om de PIN-code in te voeren die je in de vorige stap hebt ingesteld.


![LEDGER FLEX](assets/notext/19.webp)


Om de instellingen te openen, klik je op het tandwiel-symbool linksonder op je apparaat.


![LEDGER FLEX](assets/notext/20.webp)


In het menu "*Naam*" kunt u de naam van uw Ledger wijzigen.


![LEDGER FLEX](assets/notext/21.webp)


In "*Over deze Ledger*" vind je informatie over je Flex.


![LEDGER FLEX](assets/notext/22.webp)


In het menu "*Vergrendelscherm*" kun je de afbeelding op het vergrendelscherm wijzigen door "*Vergrendelschermafbeelding aanpassen*" te selecteren. Dankzij de E Ink schermtechnologie van het apparaat is het mogelijk om het scherm constant aan te laten zonder batterijverbruik. E Ink-schermen verbruiken geen energie om een statisch beeld te behouden. Ze verbruiken echter wel energie wanneer het scherm verandert.

Met het submenu "*Auto-lock*" kunt u de automatische vergrendeling van uw Ledger na een bepaalde periode van inactiviteit configureren en activeren.

![LEDGER FLEX](assets/notext/23.webp)


In het menu "*Geluiden*" kun je de geluiden van je Flex aan- of uitzetten. En in het menu "Taal" kun je de displaytaal wijzigen.


![LEDGER FLEX](assets/notext/24.webp)


Door op de pijl naar rechts te klikken, krijgt u toegang tot andere instellingen. met "*Wijzig PIN*" kunt u uw PIN-code wijzigen.


![LEDGER FLEX](assets/notext/25.webp)


Met de menu's "*Bluetooth*" en "*NFC*" kunt u deze communicatie beheren.


![LEDGER FLEX](assets/notext/26.webp)


In "*Batterij*" kun je een automatische uitschakeling van de Ledger instellen.


![LEDGER FLEX](assets/notext/27.webp)


Het gedeelte "*Geavanceerd*" geeft je toegang tot geavanceerdere beveiligingsinstellingen. Het is aan te raden om de optie "*PIN shuffle*" geactiveerd te houden om de beveiliging te verbeteren. Het is ook in dit menu dat je een BIP39 passphrase kunt configureren.


![LEDGER FLEX](assets/notext/28.webp)


Het passphrase is een optioneel wachtwoord dat, in combinatie met de herstelzin, een extra Layer beveiliging voor uw Wallet biedt.


Momenteel wordt je Wallet gegenereerd uit een Mnemonic zin bestaande uit 24 woorden. Deze herstelzin is erg belangrijk, omdat je hiermee alle sleutels van je Wallet kunt herstellen in geval van verlies. Het is echter een Single Point of Failure (SPOF). Als het gecompromitteerd is, zijn de bitcoins in gevaar. Hier komt de passphrase om de hoek kijken. Het is een optioneel wachtwoord, dat je willekeurig kunt kiezen, dat aan de Mnemonic zin wordt toegevoegd om de beveiliging van de Wallet te versterken.


De passphrase moet niet verward worden met de PIN-code. Het speelt een rol bij de afleiding van uw cryptografische sleutels. Hij werkt samen met de Mnemonic-zin en wijzigt de seed waaruit de sleutels worden gegenereerd. Dus zelfs als iemand uw 24-woordzin bemachtigt, heeft hij zonder de passphrase geen toegang tot uw geld. Het gebruik van een passphrase creëert in wezen een nieuwe Wallet met verschillende sleutels. Als je de passphrase (ook al is het maar een klein beetje) verandert, krijg je een andere generate.


De passphrase is een zeer krachtig hulpmiddel om de veiligheid van je bitcoins te verbeteren. Het is echter erg belangrijk om te begrijpen hoe het werkt voordat je het implementeert, om te voorkomen dat je de toegang tot je Wallet verliest. Ik zal uitleggen hoe je de passphrase gebruikt in een andere specifieke tutorial.


![LEDGER FLEX](assets/notext/29.webp)


De passphrase is een zeer krachtig hulpmiddel om de beveiliging van je bitcoins te versterken. Het is echter cruciaal om te begrijpen hoe het werkt voordat je het implementeert, om te voorkomen dat je de toegang tot je Wallet verliest. Daarom leg ik alles uit in een speciale tutorial:


https://planb.academy/tutorials/wallet/backup/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Tenslotte kun je op de laatste instellingenpagina je Ledger resetten. Voer deze reset alleen uit als je zeker weet dat er geen sleutels in zitten die bitcoins beveiligen, omdat je dan voorgoed de toegang tot je geld zou kunnen verliezen.

![LEDGER FLEX](assets/notext/30.webp)


## Hoe installeer ik de Bitcoin toepassing?


Start eerst de Ledger Live software op uw computer en sluit vervolgens uw Ledger Flex aan en ontgrendel deze.


![LEDGER FLEX](assets/notext/31.webp)


Ga in Ledger Live naar het menu "*Mijn Ledger*". Je wordt gevraagd om toegang tot je Flex te autoriseren.


![LEDGER FLEX](assets/notext/32.webp)


Bevestig de toegang op je Ledger door op de knop "*Toelaten*" te klikken.


![LEDGER FLEX](assets/notext/33.webp)


Ten eerste, als de firmware van uw Ledger Flex niet up-to-date is, zal Ledger Live automatisch aanbieden om deze te updaten. Klik, indien van toepassing, op "*Update firmware*" en vervolgens op "*Install update*" om de installatie te starten.


![LEDGER FLEX](assets/notext/34.webp)


Klik op uw Ledger op de knop "*Installeren*" en wacht tijdens de installatie.


![LEDGER FLEX](assets/notext/35.webp)


De firmware van je Ledger Flex is nu up-to-date.


![LEDGER FLEX](assets/notext/36.webp)


Als je wilt, kun je de achtergrond van het vergrendelscherm van je Ledger Flex wijzigen. Klik hiervoor op "*Toevoegen >*".


![LEDGER FLEX](assets/notext/37.webp)


Klik op de knop "*Upload van computer*" en kies je achtergrond uit je foto's.


![LEDGER FLEX](assets/notext/38.webp)


Je kunt je afbeelding bijsnijden.


![LEDGER FLEX](assets/notext/39.webp)


Kies een contrast uit de verschillende opties en klik vervolgens op "*Confirm contrast*".


![LEDGER FLEX](assets/notext/40.webp)


Klik op je Flex op de knop "*Foto laden*".


![LEDGER FLEX](assets/notext/41.webp)


Als je tevreden bent met de afbeelding, klik dan op "*Keep*" om het in te stellen als de achtergrond van je vergrendelscherm.


![LEDGER FLEX](assets/notext/42.webp)


Tenslotte voegen we de Bitcoin toepassing toe. Klik hiervoor op Ledger Live op de knop "*Installeren*" naast "*Bitcoin (BTC)*".


![LEDGER FLEX](assets/notext/43.webp)


De applicatie wordt geïnstalleerd op je Flex.


![LEDGER FLEX](assets/notext/44.webp)


Vanaf nu hebt u de Ledger Live software niet meer nodig voor het reguliere beheer van uw Wallet. U kunt er af en toe naar terugkeren om de firmware bij te werken als er nieuwe versies beschikbaar zijn. Voor al het andere gebruiken we Sparrow wallet, een veel uitgebreider hulpmiddel om een Bitcoin Wallet efficiënt te beheren.


## Hoe stel ik een nieuwe Bitcoin Wallet in met Sparrow?

Open Sparrow wallet en sla de introductiepagina's over om naar het beginscherm te gaan. Controleer of je goed verbonden bent met een knooppunt door naar de schakelaar rechtsonder in het scherm te kijken.

![LEDGER FLEX](assets/notext/45.webp)


Ik raad sterk aan om je eigen Bitcoin node te gebruiken. In deze tutorial gebruik ik een publieke node (geel) omdat ik op de Testnet zit, maar voor normaal gebruik kun je beter kiezen voor een lokale Bitcoin core (Green) of een Electrum server verbonden met een remote node (blauw).


Klik op het "*Bestand*" menu en dan op "*Nieuw Wallet*".


![LEDGER FLEX](assets/notext/46.webp)


Kies een naam voor deze Wallet en klik dan op "*Creëer Wallet*".


![LEDGER FLEX](assets/notext/47.webp)


Selecteer in het vervolgkeuzemenu "*Script Type*" het type script dat zal worden gebruikt om je bitcoins te beveiligen. Ik raad aan te kiezen voor "*Taproot*", of indien niet beschikbaar, "*Native SegWit*".


![LEDGER FLEX](assets/notext/48.webp)


Klik op de knop "*Gekoppeld Hardware Wallet*".


![LEDGER FLEX](assets/notext/49.webp)


Sluit je Ledger Flex aan op de computer, ontgrendel hem met je pincode en open dan de "*Bitcoin*"-toepassing. In deze tutorial gebruik ik de "*Bitcoin Testnet*" applicatie, maar de procedure blijft hetzelfde voor de Mainnet.


![LEDGER FLEX](assets/notext/50.webp)


Klik op Sparrow op de knop "*Scan*".


![LEDGER FLEX](assets/notext/51.webp)


Klik vervolgens op "*Import Keystore*".


![LEDGER FLEX](assets/notext/52.webp)


U ziet nu de details van uw Wallet, inclusief de uitgebreide publieke sleutel van uw eerste account. Klik op de knop "*Toepassen*" om het aanmaken van de Wallet te voltooien.


![LEDGER FLEX](assets/notext/53.webp)


Kies een sterk wachtwoord om de toegang tot Sparrow wallet te beveiligen. Dit wachtwoord verzekert de veiligheid van de toegang tot uw Wallet-gegevens op Sparrow, wat helpt om uw openbare sleutels, adressen, labels en transactiegeschiedenis te beschermen tegen onbevoegde toegang.


Ik raad je aan om dit wachtwoord op te slaan in een wachtwoordmanager zodat je het niet vergeet.


![LEDGER FLEX](assets/notext/54.webp)


En daar heb je het, je Wallet is nu gemaakt!


![LEDGER FLEX](assets/notext/55.webp)

Voordat je je eerste bitcoins in je Wallet ontvangt, raad ik je ten zeerste aan om een dry-run hersteltest uit te voeren. Noteer een referentiegegeven, zoals je xpub, en reset dan je Ledger Flex terwijl de Wallet nog leeg is. Probeer daarna je Wallet te herstellen op de Ledger met behulp van je papieren back-ups. Controleer of de gegenereerde xpub na het herstel overeenkomt met degene die je in eerste instantie hebt genoteerd. Als dit het geval is, kun je er zeker van zijn dat je papieren back-ups betrouwbaar zijn.


## Hoe kan ik bitcoins ontvangen met de Ledger Flex?


Klik op het tabblad "*Ontvangen*".


![LEDGER FLEX](assets/notext/56.webp)


Sluit je Ledger Flex aan op de computer, ontgrendel hem met je PIN-code en open dan de "*Bitcoin*"-toepassing.


![LEDGER FLEX](assets/notext/57.webp)


Voordat je de Address gebruikt die je van Sparrow wallet krijgt, moet je deze verifiëren op het scherm van je Ledger Flex. Hierdoor kunt u bevestigen dat de Address die wordt weergegeven op de Sparrow niet frauduleus is en dat de Ledger inderdaad de privésleutel bezit die nodig is om de bitcoins die met deze Address zijn beveiligd, later uit te geven.


Om deze verificatie uit te voeren, klik je op de knop "*Weergave Address*".


![LEDGER FLEX](assets/notext/58.webp)


Controleer of de Address die op je Ledger Flex staat, overeenkomt met de Sparrow wallet. Het is ook aan te raden om deze controle uit te voeren vlak voordat je de Address aan de verzender geeft, om zeker te zijn van de geldigheid.


![LEDGER FLEX](assets/notext/59.webp)


Je kunt een "*Label*" toevoegen om de bron te beschrijven van de bitcoins die beveiligd zullen worden met deze Address. Dit is een goede manier om je UTXO's beter te beheren.


![LEDGER FLEX](assets/notext/60.webp)


Voor meer informatie over labelen raad ik je ook aan om deze andere tutorial te bekijken:


https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Je kunt deze Address dan gebruiken om bitcoins te ontvangen.


![LEDGER FLEX](assets/notext/61.webp)


## Hoe verstuur ik bitcoins met de Ledger Flex?


Nu je je eerste Sats hebt ontvangen in je Wallet die beveiligd is met de Flex, kun je ze ook uitgeven! Sluit je Ledger aan op je computer, ontgrendel hem, start Sparrow wallet op en ga dan naar het tabblad "*Versturen*" om een nieuwe transactie te maken.


![LEDGER FLEX](assets/notext/62.webp)


Als je "*Coin controle*" wilt doen, d.w.z. specifiek wilt kiezen welke UTXO's je in de transactie wilt gebruiken, ga dan naar het tabblad "*UTXO's*". Selecteer de UTXO's die je wilt uitgeven en klik vervolgens op "*Verstuur Geselecteerd*". Je wordt doorgestuurd naar hetzelfde scherm van het tabblad "*Versturen*", maar met je UTXO's al geselecteerd voor de transactie.

![LEDGER FLEX](assets/notext/63.webp)

Voer de bestemming Address in. Je kunt ook meerdere adressen invoeren door op de knop "*+ Toevoegen*" te klikken.


![LEDGER FLEX](assets/notext/64.webp)


Noteer een "*Label*" om het doel van deze uitgave te onthouden.


![LEDGER FLEX](assets/notext/65.webp)


Kies het bedrag dat naar deze Address wordt gestuurd.


![LEDGER FLEX](assets/notext/66.webp)


Pas het tarief van je transactie aan volgens de huidige markt.


![LEDGER FLEX](assets/notext/67.webp)


Controleer of alle instellingen van je transactie correct zijn en klik dan op "*Transactie maken*".


![LEDGER FLEX](assets/notext/68.webp)


Als alles naar wens is, klik je op "*Transactie voltooien voor ondertekening*".


![LEDGER FLEX](assets/notext/69.webp)


Klik op "*Teken*".


![LEDGER FLEX](assets/notext/70.webp)


Klik op "*Aanmelden*" naast je Ledger Flex.


![LEDGER FLEX](assets/notext/71.webp)


Controleer de transactie-instellingen op het scherm van je Flex, inclusief de ontvangende Address van de ontvanger, het verzonden bedrag en het bedrag aan kosten.


![LEDGER FLEX](assets/notext/72.webp)


Om te ondertekenen houdt u uw vinger op de knop "*houden om te ondertekenen*".


![LEDGER FLEX](assets/notext/73.webp)


Je transactie is nu ondertekend. Klik op "*Transactie uitzenden*" om het uit te zenden op het Bitcoin netwerk.


![LEDGER FLEX](assets/notext/74.webp)


Je kunt het vinden in het tabblad "*Transacties*" van Sparrow wallet.


![LEDGER FLEX](assets/notext/75.webp)


Gefeliciteerd, je bent nu op de hoogte van het basisgebruik van de Ledger Flex met Sparrow wallet! In een volgende tutorial zullen we zien hoe je de Ledger Flex kunt gebruiken met Liana om Miniscript te gebruiken.


Als je deze handleiding nuttig vond, zou ik een duim omhoog hieronder op prijs stellen. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!