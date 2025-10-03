---
name: Labelling UTXO
description: Hoe label je je UTXO op de juiste manier?
---
![cover](assets/cover.webp)


In deze tutorial ontdek je alles wat je moet weten over het labelen van UTXO's in je Bitcoin Wallet en over Coin besturing. We beginnen met een theoretisch gedeelte om deze concepten volledig te begrijpen, voordat we overgaan naar een praktisch gedeelte waarin we onderzoeken hoe je labels concreet kunt gebruiken in de Bitcoin Wallet hoofdsoftware.


## Wat is UTXO etikettering?

"Labelen" is een techniek waarbij een annotatie of label geassocieerd wordt met een specifieke UTXO binnen een Bitcoin Wallet. Deze annotaties worden lokaal opgeslagen door de Wallet software en nooit verzonden over het Bitcoin netwerk. Deze annotaties worden lokaal opgeslagen door de Wallet software en worden nooit verzonden via het Bitcoin netwerk. Labelen is dus een hulpmiddel voor persoonlijk beheer.


Als ik bijvoorbeeld een UTXO ontvang van een P2P transactie via Bisq met Charles, zou ik het het label `Bisq P2P Aankoop Charles` kunnen geven.


Etikettering maakt het mogelijk om de herkomst of beoogde bestemming van de UTXO te onthouden, wat het beheer van fondsen vereenvoudigt en de privacy van de gebruiker optimaliseert. Labelen wordt nog relevanter in combinatie met de "Coin controle" functionaliteit. Coin controle is een optie die beschikbaar is in goede Bitcoin wallets, die de gebruiker de mogelijkheid geeft om handmatig te kiezen welke specifieke UTXO's worden gebruikt als input bij het creëren van een transactie.


Het gebruik van een Wallet met Coin controle, gekoppeld aan UTXO etikettering, stelt gebruikers in staat om UTXO's voor hun transacties nauwkeurig te onderscheiden en te selecteren, waardoor het samenvoegen van UTXO's uit verschillende bronnen wordt vermeden. Deze praktijk vermindert de risico's van de Common Input Ownership Heuristic (CIOH), die gemeenschappelijke Ownership van de ingangen van een transactie suggereert, wat de privacy van de gebruiker in gevaar kan brengen.


Laten we teruggaan naar het voorbeeld van mijn no-KYC UTXO van Bisq; ik wil voorkomen dat het gecombineerd wordt met een UTXO die bijvoorbeeld afkomstig is van een gereguleerd Exchange platform dat mijn identiteit kent. Door een verschillend label te plaatsen op mijn no-KYC UTXO en op mijn KYC UTXO, zal ik gemakkelijk kunnen identificeren welke UTXO ik moet gebruiken als input om te voldoen aan een uitgave, met behulp van de Coin controlefunctionaliteit.


## Hoe label je je UTXO op de juiste manier?

Er is geen universele methode voor het labelen van UTXO's die voor iedereen geschikt is. Het is aan jou om een labelsysteem te definiëren zodat je gemakkelijk je weg kunt vinden in je Wallet.

Een cruciaal criterium bij het labelen is de bron van de UTXO. Je moet gewoon aangeven hoe deze Coin in je Wallet terecht is gekomen. Komt het van een Exchange platform? Een afrekening door een klant? Een peer-to-peer Exchange? Of vertegenwoordigt het wisselgeld van een aankoop? Je zou dus kunnen specificeren:


- intrekking Exchange.com`;
- `Betalingsklant David`;
- `P2P Aankoop Charles`;
- verandering van aankoop bankstel`.

![labelling](assets/en/1.webp)

Om je UTXO beheer te verfijnen en je te houden aan je fondsscheidingsstrategieën binnen je Wallet, zou je je labels kunnen verrijken met een extra indicator die deze scheidingen weergeeft. Als uw Wallet twee categorieën UTXO's bevat die u niet wilt mengen, kunt u een markering in uw labels opnemen om deze groepen duidelijk te onderscheiden.


Deze scheidingsmarkeringen hangen af van je eigen criteria, zoals het onderscheid tussen KYC UTXO (je identiteit kennen) en no-KYC (anoniem), of tussen professionele en persoonlijke fondsen. Als we de eerder genoemde labelvoorbeelden nemen, zou dit vertaald kunnen worden als:


- kYC - Geldopname Exchange.com`;
- `KYC - Betaalcliënt David`;
- `NO KYC - P2P Aankoop Charles`;
- `NO KYC - Wijziging van bankaankoop`.

![labelling](assets/en/2.webp)

Houd er in elk geval rekening mee dat een goede etikettering een etikettering is die u begrijpt wanneer u hem nodig hebt. Als je Bitcoin Wallet vooral bedoeld is om mee te sparen, kan het zijn dat je pas over tientallen jaren iets aan de labels hebt. Zorg er daarom voor dat ze duidelijk, nauwkeurig en uitgebreid zijn.


Het is ook aan te raden om het labelen van een Coin te bestendigen tijdens transacties. Bijvoorbeeld, tijdens een no-KYC UTXO consolidatie, zorg ervoor dat je de resulterende UTXO niet alleen markeert als `consolidatie`, maar specifiek als `no-KYC consolidatie` om een duidelijk spoor van de oorsprong van de Coin te behouden.


Tot slot is het niet verplicht om een datum op een etiket te zetten. De meeste Wallet software geeft de transactiedatum al weer, en het is altijd mogelijk om deze informatie op een Block explorer op te vragen met behulp van de txid.


## Handleiding: Labelen op Specter Desktop


Verbind en open je Wallet op Specter Desktop, selecteer dan het tabblad `Adressen`.


![labelling](assets/notext/3.webp)

Hier zie je een lijst met al je adressen en bitcoins die erop vergrendeld zijn. Standaard worden adressen geïdentificeerd door hun index in de kolom `Label`. Om een label te veranderen klik je erop, voer je het gewenste label in en bevestig je door op het blauwe icoontje te klikken.

![labelling](assets/notext/4.webp)


Je label verschijnt dan in de lijst met adressen.


![labelling](assets/notext/5.webp)


U kunt ook vooraf een label toewijzen, wanneer u uw ontvangende Address deelt met de verzender. Ga hiervoor naar het tabblad `Ontvangen` en noteer uw label in het daarvoor bestemde veld.


![labelling](assets/notext/6.webp)


## Lesprogramma: Labelen op Electrum


Op Electrum Wallet, na het inloggen op uw Wallet, klikt u op de transactie waaraan u een label wilt toekennen op het tabblad `Geschiedenis`.


![labelling](assets/notext/7.webp)


Er wordt een nieuw venster geopend. Klik op het vak `Beschrijving` en typ je label.


![labelling](assets/notext/8.webp)


Zodra het label is ingevoerd, kunt u dit venster sluiten.


![labelling](assets/notext/9.webp)


Uw label is succesvol opgeslagen. U kunt het vinden onder het tabblad `Beschrijving`.


![labelling](assets/notext/10.webp)


In het tabblad `Munten`, van waaruit je Coin controle kunt uitvoeren, staat je label in de kolom `Label`.


![labelling](assets/notext/11.webp)


## Tutorial: Labelen op Green Wallet


Ga in de Green Wallet app naar je Wallet en selecteer de transactie die je wilt labelen. Klik vervolgens op het kleine potloodpictogram om uw label te noteren.


![labelling](assets/notext/12.webp)


Typ je label en klik dan op de Green `Opslaan` knop.


![labelling](assets/notext/13.webp)


U vindt uw label zowel in de details van uw transactie als op het dashboard van uw Wallet.


![labelling](assets/notext/14.webp)


## Lesprogramma: Labelen op Samourai Wallet


In Samourai Wallet zijn er verschillende methoden waarmee u een label aan een transactie kunt toekennen. Voor de eerste methode opent u eerst uw Wallet en selecteert u de transactie waaraan u een label wilt toevoegen. Druk vervolgens op de knop `Toevoegen`, die zich naast het vak `Noten` bevindt.


![labelling](assets/notext/15.webp)


Typ je label en bevestig door op de blauwe knop `Toevoegen` te klikken.


![labelling](assets/notext/16.webp)


Je vindt je label in de details van je transactie, maar ook op het dashboard van je Wallet.


![labelling](assets/notext/17.webp)

Voor de tweede methode klik je op de drie kleine puntjes rechtsboven in het scherm en vervolgens op het menu `Ongebruikte transactie-uitgangen weergeven`.

![labelling](assets/notext/18.webp)


Hier vind je een uitgebreide lijst van alle UTXO's die in je Wallet aanwezig zijn. De getoonde lijst heeft betrekking op mijn depositorekening, maar deze handeling kan worden gerepliceerd voor Whirlpool rekeningen door te navigeren vanuit het speciale menu.


Klik dan op de UTXO die je wilt labelen, gevolgd door de knop `Toevoegen`.


![labelling](assets/notext/19.webp)


Typ je label en bevestig door op de blauwe knop `Toevoegen` te klikken. Je vindt je label dan zowel in de details van je transactie als op het dashboard van je Wallet.


![labelling](assets/notext/20.webp)


## Zelfstudie: Labelen op Sparrow wallet


Met Sparrow wallet software is het mogelijk om op meerdere manieren labels toe te wijzen. De eenvoudigste methode is om vooraf een label toe te voegen, wanneer je een ontvangende Address communiceert met de verzender. Klik hiervoor in het menu `Ontvangen` op het veld `Label` en voer het gewenste label in. Dit wordt bewaard en is in de hele software toegankelijk zodra er bitcoins op de Address worden ontvangen.


![labelling](assets/notext/21.webp)


Als je vergeten bent om je Address bij ontvangst te labelen, is het nog steeds mogelijk om er later een toe te voegen via het `Transacties` menu. Klik gewoon op je transactie in de kolom `Label` en voer het gewenste label in.


![labelling](assets/notext/22.webp)


Je hebt ook de optie om labels toe te voegen of te wijzigen via het menu `Adressen`.


![labelling](assets/notext/23.webp)


Tenslotte kun je je labels bekijken in het `UTXOs` menu. Sparrow wallet voegt automatisch tussen haakjes achter je label de aard van de uitvoer toe, wat helpt om UTXO's die het gevolg zijn van verandering te onderscheiden van rechtstreeks ontvangen UTXO's.


![labelling](assets/notext/24.webp)