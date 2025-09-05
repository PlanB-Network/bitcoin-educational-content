---
name: PayJoin - Samourai Wallet
description: Hoe voer je een PayJoin transactie uit op Samourai Wallet?
---
![samourai payjoin cover](assets/cover.webp)


***Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, werken Payjoins Stowaway op Samourai Wallet alleen nog door handmatig PSBT uit te wisselen tussen de betrokken partijen, op voorwaarde dat beide gebruikers verbonden zijn met hun eigen Dojo. Wat Sparrow betreft, werken Payjoins via BIP78 nog steeds. Het is echter mogelijk dat deze tools in de komende weken opnieuw worden gelanceerd. In de tussentijd kun je nog steeds dit artikel lezen om de theoretische werking van Stowaway te begrijpen.*


als u van plan bent om een Stowaway handmatig uit te voeren, is de procedure zeer vergelijkbaar met die beschreven in deze handleiding. Het belangrijkste verschil zit in de keuze van het type verstekverrichting: in plaats van `Online` te selecteren, klikt u op `In Person / Manual`. Vervolgens moet u handmatig Exchange de PSBTs om de Stowaway transactie te construeren. Als u fysiek dicht bij uw medewerker bent, kunt u de QR-codes achtereenvolgens scannen. Als u op afstand bent, kunnen JSON-bestanden worden uitgewisseld via een beveiligd communicatiekanaal. De rest van de tutorial blijft ongewijzigd._


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

> *Dwing Blockchain spionnen om alles wat ze denken te weten te heroverwegen.*

PayJoin is een specifieke Bitcoin transactiestructuur die de privacy van gebruikers tijdens een uitgave verbetert door samen te werken met de ontvanger van de betaling. Er zijn verschillende implementaties die het opzetten en automatiseren van PayJoin vergemakkelijken. Van deze implementaties is de meest bekende Stowaway, ontwikkeld door de teams van Samourai Wallet. Deze tutorial legt uit hoe je een Stowaway PayJoin transactie uitvoert met de Samourai Wallet applicatie.


## Hoe werkt Stowaway?


Zoals eerder vermeld, biedt Samourai Wallet een PayJoin hulpmiddel genaamd "Stowaway." Het is toegankelijk via de Sparrow wallet software op PC of de Samourai Wallet applicatie op Android. Om een PayJoin uit te voeren, moet de ontvanger, die ook optreedt als medewerker, software gebruiken die compatibel is met Stowaway, namelijk Sparrow of Samourai. Deze twee software zijn interoperabel, waardoor een Stowaway transactie mogelijk is tussen een Sparrow wallet en een Samourai Wallet, en vice versa.


Stowaway vertrouwt op een categorie transacties die Samourai "Cahoots" noemt Een Cahoot is in wezen een gezamenlijke transactie tussen meerdere gebruikers, waarvoor off-chain informatie Exchange nodig is. Tot op heden biedt Samourai twee Cahoots tools: Stowaway (Payjoins) en StonewallX2 (die we in een toekomstig artikel zullen bespreken).


Bij Cahoots-transacties worden gedeeltelijk ondertekende transacties tussen gebruikers uitgewisseld. Dit proces kan lang duren en omslachtig zijn, vooral als het op afstand gebeurt. Het kan echter nog steeds handmatig worden uitgevoerd met een andere gebruiker, wat handig kan zijn als de medewerkers fysiek in de buurt zijn. In de praktijk betekent dit het handmatig uitwisselen van vijf QR-codes die achtereenvolgens moeten worden gescand.


Wanneer dit op afstand gebeurt, wordt dit proces te complex. Om dit probleem Address aan te pakken, heeft Samourai een versleuteld communicatieprotocol ontwikkeld op basis van Tor, genaamd "Soroban." Met Soroban worden de uitwisselingen die nodig zijn voor een PayJoin geautomatiseerd achter een gebruiksvriendelijke Interface. Dit is de tweede methode die we in dit artikel zullen bestuderen.


Deze versleutelde uitwisselingen vereisen het opzetten van een verbinding en authenticatie tussen de Cahoots deelnemers. Soroban communicatie is daarom gebaseerd op de Paynyms van de gebruikers. Als je niet bekend bent met Paynyms, nodig ik je uit om dit artikel te raadplegen voor meer details: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)



Simpel gezegd is een Paynym een unieke identificatiecode gekoppeld aan je Wallet die verschillende functionaliteiten mogelijk maakt, waaronder versleutelde berichtenuitwisseling. De Paynym wordt gepresenteerd in de vorm van een identifier en een afbeelding die een robot voorstelt. Hier is een voorbeeld van de mijne op de Testnet: ![paynym samourai Wallet](assets/nl/1.webp)


**Samengevat:**


- _Payjoin_ = Specifieke structuur van collaboratieve transacties;
- _Stowaway_ = PayJoin implementatie beschikbaar op Samourai en Sparrow wallet;
- _Cahoots_ = Naam gegeven door Samourai aan al hun soorten gezamenlijke transacties, inclusief PayJoin Stowaway;
- _Soroban_ = Versleuteld communicatieprotocol vastgelegd op Tor, dat samenwerking met andere gebruikers mogelijk maakt in de context van een Cahoots-transactie;
- _Paynym_ = Unieke identificatie van een Wallet die communicatie mogelijk maakt met een andere gebruiker op Soroban, om een Cahoots transactie uit te voeren.


[**-> Meer informatie over PayJoin transacties en hun nut**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## Hoe maak je een verbinding tussen Paynyms?


Om een Cahoots transactie op afstand uit te voeren, specifiek een PayJoin (Stowaway) via Samourai, is het noodzakelijk om de gebruiker met wie u van plan bent om samen te werken te "volgen", met behulp van hun Paynym. In het geval van een Stowaway, betekent dit het volgen van de persoon naar wie u bitcoins wilt sturen.


**Hier volgt de procedure om deze verbinding tot stand te brengen:**


Om te beginnen, moet je de betaalcode van de Paynym van de ontvanger voor de PayJoin verkrijgen. In de Samourai Wallet applicatie, moet de ontvanger op het icoontje van zijn Paynym (het robotje) linksboven in het scherm tikken, en dan op zijn Paynym nickname klikken, beginnend met `+...`. De mijne is bijvoorbeeld `+namelessmode0aF`. Als je medewerker Sparrow wallet gebruikt, raadpleeg dan onze speciale handleiding door hier te klikken.


![connexion paynym samourai](assets/notext/2.webp)


Uw medewerker zal dan worden doorgestuurd naar hun Paynym pagina. Vanaf daar kunnen ze hun Paynym gegevens met u delen of hun QR code delen zodat u deze kunt scannen. Om dit te doen, moeten ze klikken op het kleine "delen" icoontje rechtsboven in hun scherm.

![partager paynym samourai](assets/en/1.webp)


Start aan uw kant uw Samourai Wallet applicatie en ga op dezelfde manier naar het "PayNyms" menu. Als dit de eerste keer is dat je je Paynym gebruikt, moet je de identifier verkrijgen.


![demander un paynym](assets/notext/3.webp)


Klik vervolgens op de blauwe "+" rechtsonder in het scherm.

![ajouter paynym collaborateur](assets/notext/4.webp)

Je kunt dan de betalingscode van je medewerker plakken door `COLLER LE CODE PAIEMENT` te selecteren, of open de camera om hun QR-code te scannen door op `SCANNEZ LE CODE QR` te drukken.![paynym identifier plakken](assets/notext/5.webp)


Klik op de knop `SUIVRE`.

![follow paynym](assets/notext/6.webp)

Bevestig door op `YES` te klikken.

![confirm follow paynym](assets/notext/7.webp)

De software zal je dan een `SE CONNECTER` knop aanbieden. Voor onze tutorial is het niet nodig om op deze knop te klikken. Deze stap is alleen nodig als je van plan bent om betalingen te doen aan de andere Paynym als onderdeel van de BIP47, wat niet gerelateerd is aan onze handleiding.

![connect paynym](assets/notext/8.webp)

Zodra de Paynym van de ontvanger gevolgd wordt door jouw Paynym, herhaal je deze handeling in tegenovergestelde richting zodat de ontvanger jou ook volgt. Je kunt dan een PayJoin uitvoeren.


## Hoe doe je een PayJoin op een Samourai Wallet?


Als je deze voorbereidende stappen hebt doorlopen, ben je eindelijk klaar om de PayJoin transactie uit te voeren! Volg hiervoor onze videotutorial:


![Payjoin Video Tutorial - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)


**Externe bronnen:**


- https://docs.samourai.io/en/spend-tools#stowaway.