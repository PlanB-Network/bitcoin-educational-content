---
name: PayJoin - Sparrow wallet
description: Hoe maak ik een PayJoin transactie op Sparrow wallet?
---

![tutorial cover image sparrow payjoin](assets/cover.webp)


na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, werken Payjoins Stowaway op Samourai Wallet nu alleen nog door handmatig PSBT uit te wisselen tussen de betrokken partijen, mits beide gebruikers verbonden zijn met hun eigen Dojo. Voor Sparrow geldt dat Payjoins via BIP78 nog steeds werken. Het is echter mogelijk dat deze tools in de komende weken opnieuw worden opgestart. In de tussentijd kun je altijd dit artikel lezen om de theoretische werking van payjoins te begrijpen


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

> *Dwing Blockchain spionnen om alles wat ze denken te weten te heroverwegen.*

PayJoin is een specifieke Bitcoin transactiestructuur die de privacy van gebruikers tijdens uitgaven verbetert door samen te werken met de ontvanger van de betaling. Er zijn verschillende implementaties die het opzetten en automatiseren van PayJoin vergemakkelijken. Van deze implementaties is de bekendste Stowaway, ontwikkeld door het Samourai Wallet team. Deze tutorial leidt u door het proces van het maken van een Stowaway PayJoin transactie met behulp van de Sparrow wallet software.


## Hoe werkt Stowaway?


Zoals eerder vermeld, biedt Samourai Wallet een PayJoin hulpmiddel genaamd "Stowaway." Het is toegankelijk via de Sparrow wallet software op PC of de Samourai Wallet applicatie op Android. Om een PayJoin uit te voeren, moet de ontvanger, die ook optreedt als medewerker, software gebruiken die compatibel is met Stowaway, namelijk Sparrow of Samourai Wallet. Deze twee software is interoperabel met elkaar. Deze twee software zijn interoperabel, waardoor Stowaway transacties mogelijk zijn tussen een Sparrow wallet en een Samourai Wallet, en vice versa.


Stowaway vertrouwt op een categorie transacties die Samourai "Cahoots" noemt Een Cahoot is in wezen een gezamenlijke transactie tussen meerdere gebruikers die off-chain informatie Exchange vereist. Op dit moment biedt Samourai twee Cahoots tools: Stowaway (Payjoins) en StonewallX2 (die we in een toekomstig artikel zullen bespreken).


Bij Cahoots-transacties worden gedeeltelijk ondertekende transacties tussen gebruikers uitgewisseld. Dit proces kan lang duren en omslachtig zijn, vooral als het op afstand gebeurt. Het kan echter nog steeds handmatig worden gedaan met een andere gebruiker, wat handig kan zijn als de medewerkers fysiek in de buurt zijn. In de praktijk betekent dit het handmatig uitwisselen van vijf QR-codes die achtereenvolgens moeten worden gescand.


Wanneer dit op afstand gebeurt, wordt dit proces te complex. Om dit probleem Address aan te pakken, heeft Samourai een versleuteld communicatieprotocol ontwikkeld op basis van Tor, genaamd "Soroban." Met Soroban worden de noodzakelijke uitwisselingen voor een PayJoin geautomatiseerd achter een gebruiksvriendelijke Interface. Dit is de tweede methode die we in dit artikel zullen onderzoeken.


Deze versleutelde uitwisselingen vereisen het opzetten van een verbinding en authenticatie tussen Cahoots deelnemers. Soroban communicatie vertrouwt op de Paynyms van de gebruikers. Als je niet bekend bent met Paynyms, raadpleeg dan dit artikel voor meer details: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)

Simpel gezegd is een Paynym een unieke identificatiecode gekoppeld aan je Wallet die verschillende functionaliteiten mogelijk maakt, waaronder versleutelde berichtenuitwisseling. De Paynym wordt gepresenteerd in de vorm van een identifier en een afbeelding van een robot. Hier is een voorbeeld van de mijne op de Testnet: ![Paynym Sparrow](assets/nl/1.webp)


**Samengevat:**



- _Payjoin_ = Specifieke structuur van collaboratieve transactie;
- _Stowaway_ = PayJoin implementatie beschikbaar op Samourai en Sparrow wallet;
- _Cahoots_ = Naam gegeven door Samourai aan al hun soorten samenwerkingsverbanden, inclusief PayJoin Stowaway;
- _Soroban_ = Versleuteld communicatieprotocol vastgelegd op Tor, dat samenwerking met andere gebruikers mogelijk maakt in de context van een Cahoots-transactie.
- _Paynym_ = Unieke identificatiecode van een Wallet die communicatie mogelijk maakt met een andere gebruiker op Soroban, om

een Cahoots-transactie uitvoeren.


[**-> Meer informatie over PayJoin transacties en hun nut**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## Hoe maak je een verbinding tussen Paynyms?


Om een Cahoots-transactie op afstand uit te voeren, specifiek een PayJoin (Stowaway) via Samourai of Sparrow, is het noodzakelijk om de gebruiker met wie je wilt samenwerken te "volgen" met behulp van hun Paynym. In het geval van een verstekeling, betekent dit het volgen van de persoon naar wie je bitcoins wilt sturen.


**Hier volgt de procedure om deze verbinding tot stand te brengen:**


Eerst moet u de Paynym-identificatie van de ontvanger verkrijgen. Dit kan met behulp van hun nickname of betaalcode. Selecteer hiervoor in de Sparrow wallet van de ontvanger de tab `Tools` en klik vervolgens op `Show PayNym`.

![Show Paynym](assets/notext/2.webp)

![Paynym Sparrow](assets/en/1.webp)

Open aan uw kant uw Sparrow wallet en ga naar hetzelfde menu `Show PayNym`. Als je je Paynym voor de eerste keer gebruikt, moet je een identifier verkrijgen door op `Retrieve PayNym` te klikken.

![Retrieve paynym](assets/notext/3.webp)

Voer vervolgens de Paynym-identificatie van uw medewerker in (ofwel hun bijnaam `+...` of hun betaalcode `PM...`) in het vak `Vind contact` en klik vervolgens op de knop `Voeg contact toe`.

![add contact](assets/notext/4.webp)

De software zal je dan een `Link Contact` knop aanbieden. Voor onze handleiding is het niet nodig om op deze knop te klikken. Deze stap is alleen nodig als je van plan bent betalingen te doen aan Paynym in het kader van BIP47, wat niets te maken heeft met onze handleiding.


Zodra de Paynym van de ontvanger gevolgd wordt door jouw Paynym, herhaal je deze handeling in de tegenovergestelde richting zodat de ontvanger jou ook volgt. Je kunt dan een PayJoin uitvoeren.


## Hoe voer je een PayJoin op Sparrow wallet uit?


Als u deze paar voorbereidende stappen hebt doorlopen, bent u eindelijk klaar om de PayJoin transactie uit te voeren! Volg hiervoor onze videotutorial:

![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)


**Externe bronnen:**



- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.