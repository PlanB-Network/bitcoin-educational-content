---
name: Tapsigner
description: Een Tapsigner instellen en gebruiken met Nunchuk
---
![cover](assets/cover.webp)


Een Hardware Wallet is een elektronisch apparaat dat gewijd is aan het beheer en de beveiliging van de private sleutels van een Bitcoin Wallet. In tegenstelling tot software wallets (of Hot wallets) die geïnstalleerd zijn op algemene machines die vaak verbonden zijn met het internet, maken hardware wallets de fysieke isolatie van private sleutels mogelijk, waardoor de risico's van hacken en diefstal worden verminderd.


Het hoofddoel van een Hardware Wallet is het minimaliseren van de functionaliteiten van het apparaat om het aanvalsoppervlak te verkleinen. Een kleiner aanvalsoppervlak betekent ook minder potentiële aanvalsvectoren, d.w.z. minder zwakke punten in het systeem die aanvallers kunnen uitbuiten om toegang te krijgen tot de bitcoins.


Het wordt aanbevolen om een Hardware Wallet te gebruiken om je bitcoins te beveiligen, vooral als je aanzienlijke hoeveelheden hebt, in absolute waarde of als deel van je totale vermogen.


Hardware wallets worden gebruikt in combinatie met een Wallet beheersoftware op een computer of smartphone. Deze software beheert de aanmaak van transacties, maar de cryptografische handtekening die nodig is om deze transacties te valideren, wordt uitsluitend binnen de Hardware Wallet gezet. Dit betekent dat de privésleutels nooit worden blootgesteld aan een potentieel kwetsbare omgeving.


Hardware wallets bieden een dubbele bescherming voor de gebruiker: aan de ene kant beveiligen ze je bitcoins tegen aanvallen op afstand door de privésleutels offline te houden, en aan de andere kant bieden ze over het algemeen een betere fysieke weerstand tegen pogingen om de sleutels te ontfutselen. En het is precies op deze 2 veiligheidscriteria dat je de verschillende modellen op de markt kunt beoordelen en rangschikken.


In deze tutorial stel ik voor om een van deze oplossingen te ontdekken: de Tapsigner van Coinkite.


## Inleiding tot de Tapsigner


De Tapsigner is een Hardware Wallet ontworpen in de vorm van een NFC-kaart door het bedrijf Coinkite, ook bekend van de productie van Coldcards.


![TAPSIGNER NUNCHUK](assets/notext/01.webp)


De Tapsigner maakt het mogelijk om een paar bestaande uit een master private key en een chain code op te slaan in overeenstemming met BIP32, om zo een boom van cryptografische sleutels af te leiden. Deze sleutels kunnen worden gebruikt om transacties te ondertekenen door de Tapsigner tegen een telefoon of een NFC-kaartlezer te plaatsen.

Deze NFC-kaart wordt verkocht voor $19,99, wat erg betaalbaar is vergeleken met andere hardware wallets die op de markt verkrijgbaar zijn. Vanwege het formaat biedt de Tapsigner echter niet zoveel opties als andere apparaten. Er is duidelijk geen batterij, geen camera en geen micro SD-kaartlezer, omdat het een kaart is. Naar mijn mening is het grootste nadeel het ontbreken van een scherm op de Hardware Wallet, waardoor het kwetsbaarder is voor bepaalde soorten aanvallen op afstand. Dit dwingt de gebruiker om blind te tekenen en te vertrouwen op wat hij op zijn computerscherm ziet.


Ondanks zijn beperkingen kan de Tapsigner interessant zijn vanwege zijn lage prijs. Deze Wallet kan met name worden gebruikt om de beveiliging van een Wallet die geld uitgeeft te verbeteren, naast een Wallet die wordt beschermd door een Hardware Wallet die is uitgerust met een scherm. Het is ook een goede oplossing voor mensen die kleine hoeveelheden bitcoins bezitten en geen honderd euro willen investeren in een geavanceerder apparaat. Bovendien kan het gebruik van Tapsigner in Multisig configuraties, of mogelijk in Wallet systemen met tijdslot in de toekomst, interessante voordelen bieden.


## Hoe koop ik een Tapsigner?


De Tapsigner is te koop [op de officiële website van Coinkite](https://store.coinkite.com/store/category/tapsigner). Om hem in een fysieke winkel te kopen, kun je ook [de lijst van gecertificeerde wederverkopers](https://coinkite.com/resellers) op de site vinden.


U hebt ook een telefoon nodig die compatibel is met NFC-communicatie, of een USB-apparaat dat NFC-kaarten kan lezen op de standaardfrequentie van 13,56 MHz.


## Hoe initialiseer je een Tapsigner met Nunchuk?


Zodra je je Tapsigner hebt ontvangen, is de eerste stap om de verpakking te onderzoeken om er zeker van te zijn dat deze niet geopend is. Als de verpakking beschadigd is, kan dit erop wijzen dat de kaart gecompromitteerd is en misschien niet authentiek is. CoinKite levert je Tapsigner met een hoesje dat radiogolven blokkeert. Zorg ervoor dat het aanwezig is in je pakket.


![TAPSIGNER NUNCHUK](assets/notext/02.webp)


Om de Wallet te beheren, gebruiken we de **Nunchuk Wallet** mobiele app. Zorg ervoor dat uw smartphone NFC-compatibel is en download Nunchuk van de [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), de [App Store](https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) of direct via het [`.apk` bestand](https://github.com/nunchuk-io/nunchuk-android/releases).


![TAPSIGNER NUNCHUK](assets/notext/03.webp)

Als je de Nunchuk voor de eerste keer gebruikt, zal de app je vragen om een account aan te maken. Voor deze tutorial is het niet nodig om een account aan te maken. Selecteer dus "*Doorgaan als gast*" om verder te gaan zonder account.

![TAPSIGNER NUNCHUK](assets/notext/04.webp)


Klik dan op "*Unassisted Wallet*".


![TAPSIGNER NUNCHUK](assets/notext/05.webp)


Klik vervolgens op de knop "*Ik ga zelf op onderzoek uit*".


![TAPSIGNER NUNCHUK](assets/notext/06.webp)


Klik in de Nunchuk op de knop "*+*" naast het tabblad "*Keys*".


![TAPSIGNER NUNCHUK](assets/notext/07.webp)


Kies "*NFC-sleutel toevoegen*".


![TAPSIGNER NUNCHUK](assets/notext/08.webp)


Klik vervolgens op "*TAPSIGNER TOEVOEGEN*".


![TAPSIGNER NUNCHUK](assets/notext/09.webp)


Klik op "*Doorgaan*" en plaats vervolgens uw Tapsigner NFC-kaart tegen uw smartphone.


![TAPSIGNER NUNCHUK](assets/notext/10.webp)


Als uw Tapsigner nieuw is, zal de Nunchuk aanbieden om het te initialiseren. Klik op "*Ja*".


![TAPSIGNER NUNCHUK](assets/notext/11.webp)


Je moet nu kiezen hoe je generate je master chain code gaat maken.


De Tapsigner gebruikt de BIP32-standaard. Dit betekent dat de afleiding van je cryptografische sleutels die je bitcoins beveiligen niet afhankelijk is van een Mnemonic zin zoals bij BIP39 wallets, maar direct van de master private key en de master chain code. Deze 2 Elements worden door de HMAC functie gehaald om de rest van je Wallet determinatief en hiërarchisch af te leiden. Deze 2 Elements worden door de HMAC-functie gehaald om deterministisch en hiërarchisch de rest van je Wallet af te leiden.


De master private key wordt rechtstreeks gegenereerd door de TRNG (*True Random Number Generator*) die in je Tapsigner geïntegreerd is. De master chain code, aan de andere kant, moet van buitenaf worden aangeleverd. Bij deze stap heeft u de keuze: laat Nunchuk generate automatisch genereren door op "*Automatic*" te klikken, of generate het zelf door "*Advanced*" te selecteren en het in te voeren in het daarvoor bestemde veld.


![TAPSIGNER NUNCHUK](assets/notext/12.webp)


Vervolgens moet u een pincode kiezen. Voer in het gebied "*Begin PIN*" de PIN-code in die op de achterkant van uw Tapsigner staat.


![TAPSIGNER NUNCHUK](assets/notext/13.webp)


Kies een pincode om de fysieke toegang tot uw Tapsigner te beveiligen. Deze PIN-code speelt geen rol in het Wallet herstelproces. De enige functie is het ontgrendelen van uw Tapsigner om transacties te ondertekenen. Zorg ervoor dat u deze PIN-code bewaart, zodat u hem niet vergeet. Klik op "*Doorgaan*" om verder te gaan.


![TAPSIGNER NUNCHUK](assets/notext/14.webp)

Plaats nu uw Tapsigner-kaart aan de achterkant van uw telefoon om deze te initialiseren.

![TAPSIGNER NUNCHUK](assets/notext/15.webp)


Nunchuk zal dan generate het herstelbestand voor je Wallet maken, waarmee je weer toegang krijgt tot je bitcoins als je je NFC-kaart verliest. Dit bestand is versleuteld met de back-upcode die op de achterkant van je Tapsigner staat. Om je bitcoins terug te krijgen, heb je dit bestand en de code om het te ontsleutelen absoluut nodig. Het is daarom belangrijk om een papieren kopie van deze code te maken, want als je je NFC-kaart verliest, ben je ook de toegang tot deze code kwijt, omdat deze voorlopig alleen op de kaart staat. Zorg er ook voor dat je meerdere back-ups maakt van je versleutelde herstelbestand.


![TAPSIGNER NUNCHUK](assets/notext/16.webp)


Kies een naam voor je Wallet.


![TAPSIGNER NUNCHUK](assets/notext/17.webp)


De basis van je Wallet is nu gelegd. Om de authenticiteit van je Tapsigner te controleren, kun je op elk moment op de knop "*Run health check*" klikken.


![TAPSIGNER NUNCHUK](assets/notext/18.webp)


Voer uw pincode in.


![TAPSIGNER NUNCHUK](assets/notext/19.webp)


Plaats je kaart dan aan de achterkant van je telefoon.


![TAPSIGNER NUNCHUK](assets/notext/20.webp)


## Hoe maak ik een Wallet op een Tapsigner?


Terug op de startpagina van de Nunchuk, kunt u zien dat uw Tapsigner is geregistreerd bij de beschikbare ondertekeningsapparaten.


![TAPSIGNER NUNCHUK](assets/notext/21.webp)


Je moet nu generate de sleutels voor je Bitcoin Wallet maken. Klik hiervoor op de knop "*+*" rechts van de tab "*Wallets*".


![TAPSIGNER NUNCHUK](assets/notext/22.webp)


Klik op "*Nieuw Wallet* aanmaken".


![TAPSIGNER NUNCHUK](assets/notext/23.webp)


Kies dan de optie "*Maak een nieuwe Wallet met gebruik van bestaande sleutels*".


![TAPSIGNER NUNCHUK](assets/notext/24.webp)


Kies een naam voor je Wallet en klik dan op "*Doorgaan*".


![TAPSIGNER NUNCHUK](assets/notext/25.webp)


Selecteer je Tapsigner als het ondertekeningsapparaat voor deze nieuwe set sleutels en klik dan op "*Doorgaan*".


![TAPSIGNER NUNCHUK](assets/notext/26.webp)


Als alles naar wens is, bevestig je de creatie.


![TAPSIGNER NUNCHUK](assets/notext/27.webp)

Je kunt dan het configuratiebestand van je Wallet opslaan. Dit bestand bevat uitsluitend je publieke sleutels, wat betekent dat zelfs als iemand er toegang toe heeft, hij je bitcoins niet kan stelen. Ze kunnen echter wel al je transacties volgen. Daarom vormt dit bestand alleen een risico voor je privacy. In sommige gevallen kan het essentieel zijn om je Wallet terug te krijgen.

![TAPSIGNER NUNCHUK](assets/notext/28.webp)


En daar heb je het, je Wallet is succesvol aangemaakt!


![TAPSIGNER NUNCHUK](assets/notext/29.webp)


Als je je Tapsigner niet gebruikt, berg hem dan op in het hoesje dat wordt geleverd door Coinkite. Dit hoesje blokkeert radiogolven om onbevoegde metingen te voorkomen.


## Hoe kan ik bitcoins ontvangen op de Tapsigner?


Om bitcoins te ontvangen, klik je op je Wallet.


![TAPSIGNER NUNCHUK](assets/notext/30.webp)


Gebruik dan de gegenereerde Address om bitcoins te ontvangen. Als je al eerder bitcoins hebt ontvangen op deze Wallet, moet je op de knop "*Ontvangen*" klikken om een nieuwe lege ontvangende Address generate te maken.


![TAPSIGNER NUNCHUK](assets/notext/31.webp)


Zodra de transactie van de verzender is uitgezonden, zie je deze op je Wallet verschijnen.


![TAPSIGNER NUNCHUK](assets/notext/32.webp)


Klik op "*Munten bekijken*".


![TAPSIGNER NUNCHUK](assets/notext/33.webp)


Selecteer je nieuwe UTXO.


![TAPSIGNER NUNCHUK](assets/notext/34.webp)


Klik op de "*+*" naast "*Tags*" om een label aan je UTXO toe te voegen. Dit is een goede gewoonte, omdat het je helpt de herkomst van je munten te onthouden en je privacy te optimaliseren voor toekomstige uitgaven.


![TAPSIGNER NUNCHUK](assets/notext/35.webp)


Selecteer een bestaande tag of maak een nieuwe aan en klik vervolgens op "*Opslaan*". Je hebt ook de optie om "*verzamelingen*" aan te maken om je munten op een meer gestructureerde manier te organiseren.


![TAPSIGNER NUNCHUK](assets/notext/36.webp)


## Hoe verstuur je bitcoins met de Tapsigner?


Nu je bitcoins in je Wallet hebt, kun je ze ook versturen. Klik hiervoor op de Wallet van je keuze.


![TAPSIGNER NUNCHUK](assets/notext/37.webp)


Klik op de knop "*Versturen*".


![TAPSIGNER NUNCHUK](assets/notext/38.webp)


Selecteer het bedrag dat u wilt verzenden en klik vervolgens op "*Doorgaan*".


![TAPSIGNER NUNCHUK](assets/notext/39.webp)


Voeg een "*noot*" toe aan je toekomstige transactie om het doel ervan te onthouden.


![TAPSIGNER NUNCHUK](assets/notext/40.webp)

Voer vervolgens handmatig het Address van de ontvanger in het daarvoor bestemde veld in.

![TAPSIGNER NUNCHUK](assets/notext/41.webp)


Je kunt ook een Address met QR-code scannen door op het pictogram rechtsboven in het scherm te klikken.


![TAPSIGNER NUNCHUK](assets/notext/42.webp)


Klik op de knop "*Transactie maken*".


![TAPSIGNER NUNCHUK](assets/notext/43.webp)


Controleer de details van je transactie en klik vervolgens op de knop "*Teken*" naast je Tapsigner.


![TAPSIGNER NUNCHUK](assets/notext/44.webp)


Voer uw PIN-code in om te ontgrendelen.


![TAPSIGNER NUNCHUK](assets/notext/45.webp)


Plaats vervolgens de Tapsigner aan de achterkant van je smartphone.


![TAPSIGNER NUNCHUK](assets/notext/46.webp)


Je transactie is nu ondertekend. Controleer nog een laatste keer of alles correct is en klik dan op "*Uitzenden Transactie*" om het uit te zenden op het Bitcoin netwerk.


![TAPSIGNER NUNCHUK](assets/notext/47.webp)


Je transactie wacht nu op bevestiging.


![TAPSIGNER NUNCHUK](assets/notext/48.webp)


## Hoe kan ik de Wallet herstellen in geval van verlies van de Tapsigner?


Als je je Tapsigner kwijt bent, kun je je Wallet terugvinden met de code die op de achterkant van de kaart staat. Het is daarom belangrijk om deze code apart van de Tapsigner te bewaren, want als de kaart verloren gaat, gaat de toegang tot deze code ook verloren. Je hebt ook de versleutelde back-up van de Wallet nodig.


Voor herstel zullen we de Nunchuk app gebruiken, maar houd er rekening mee dat dit betekent dat je tijdelijk je tegoeden moet veiligstellen in een Hot Wallet. Als je Tapsigner aanzienlijke bedragen beveiligde, overweeg dan om hetzelfde herstelproces te volgen met een nieuwe Coldcard.


Open de Nunchuk-app en klik op de knop "*+*" naast het tabblad "*Keys*".


![TAPSIGNER NUNCHUK](assets/notext/49.webp)


Kies "*NFC-sleutel toevoegen*".


![TAPSIGNER NUNCHUK](assets/notext/50.webp)


Kies de optie "*Herstel TAPSIGNER sleutel van back-up*".


![TAPSIGNER NUNCHUK](assets/notext/51.webp)


Je wordt dan doorgestuurd naar de bestandsverkenner van je apparaat. Zoek en selecteer het versleutelde back-upbestand van je Wallet. Normaal gesproken begint de naam van dit bestand met `backup...`.


![TAPSIGNER NUNCHUK](assets/notext/52.webp)


Voer het wachtwoord in dat het back-upbestand decodeert. Dit wachtwoord komt overeen met het wachtwoord dat aanvankelijk op de achterkant van uw Tapsigner stond.


![TAPSIGNER NUNCHUK](assets/notext/53.webp)

Kies dan een naam voor je herstel Wallet.

![TAPSIGNER NUNCHUK](assets/notext/54.webp)


Je hebt nu weer toegang tot je bitcoins. Uw Wallet wordt nu beheerd als een Hot Wallet zichtbaar in de "*Keys*" tab van de Nunchuk app. Vervolgens moet u een nieuwe set cryptografische sleutels aanmaken in de "*Wallets*" sectie door deze sleutel eraan te koppelen. Om dit te doen, kun je de stappen opnieuw volgen in het "*Hoe maak ik een Wallet op een Tapsigner?*" deel van deze tutorial.


![TAPSIGNER NUNCHUK](assets/notext/55.webp)


Als je je Tapsigner kwijt bent, raad ik je sterk aan om je bitcoins onmiddellijk over te zetten naar een andere Wallet die je bezit, idealiter beschermd door een Hardware Wallet. De Tapsigner die je kwijt bent, kan namelijk in verkeerde handen vallen. Het is daarom belangrijk om de Wallet die je net hebt teruggevonden, leeg te maken en niet meer te gebruiken.


Gefeliciteerd, je bent nu op de hoogte van het gebruik van de Tapsigner! Als je deze handleiding nuttig vond, zou ik het waarderen als je hieronder een duim omhoog achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!