---
name: Trezor Shamir Backup
description: Enkelvoudige en meervoudige Mnemonic-zinnen op Trezor
---
![cover](assets/cover.webp)



*Afbeelding credit: [Trezor.io](https://trezor.io/)*



## Nieuwe back-upopties op Trezor



Sinds 2023 biedt Trezor een nieuw back-upformaat genaamd ***Single-share Backup***, dat geleidelijk de klassieke BIP39-gebaseerde aanpak vervangt die op de meeste wallets te vinden is. In tegenstelling tot de traditionele 12- of 24-woord Mnemonic zinnen, is dit nieuwe formaat gebaseerd op een enkele 20-woord zin afgeleid van een standaard ontwikkeld door SatoshiLabs: **SLIP39**. Het doel is om de robuustheid en leesbaarheid van back-ups te verbeteren en tegelijkertijd een soepele migratie naar een gedistribueerd back-upmodel mogelijk te maken.



Dit gedistribueerde model heet ***Multi-share Backup***. Het is gebaseerd op hetzelfde principe, maar in plaats van een enkele Mnemonic frase te genereren, splitst het deze op in verschillende fragmenten, ***shares*** genaamd, die elk op zich een Mnemonic frase zijn. Om de Wallet te herstellen, moet een bepaald aantal van deze *shares* (gedefinieerd door een *drempel*) herenigd worden. Bijvoorbeeld, in een 3-of-5 schema, zullen 3 *aandelen* van de 5 de Wallet herstellen. Het gedistribueerde back-upsysteem van Trezor verschilt van Multisig wallets. Om bitcoins uit te geven is alleen een Hardware Wallet Trezor nodig. Er is slechts één handtekening nodig. Distributie is alleen van toepassing op het niveau van de Mnemonic zin, d.w.z. de back-up.



![Image](assets/fr/01.webp)



Dit systeem lost het probleem op van het single point of failure van de Mnemonic phrase zonder de nadelen die gepaard gaan met het beheer van een Multisig of passphrase BIP39. Het herstelproces is niet langer gebaseerd op een enkel stuk informatie, maar op meerdere, met als bijkomend voordeel verliesbestendigheid dankzij de drempelwaarde.



Gebruikers die een Wallet met *Single-share Backup* hebben gemaakt, kunnen op elk moment overschakelen naar *Multi-share Backup* zonder hun Wallet te hoeven migreren. Ontvangstadressen en accounts blijven identiek. Het *Multi-share* systeem heeft alleen invloed op de back-up, terwijl de rest van de Wallet ongewijzigd blijft.



Multi-share Backup is beschikbaar op de Trezor Model T, Safe 3 en Safe 5. Deze functie wordt niet ondersteund door de Trezor Model One.



**Belangrijke opmerking:** Trezors *Multi-share* systeem is cryptografisch veilig, omdat het gebruik maakt van het *Shamir's Secret Sharing* schema voor distributie. We raden ten zeerste af om een soortgelijk systeem handmatig toe te passen, door zelf een klassieke Mnemonic zin te verdelen. Het is een slechte praktijk die het risico op diefstal en verlies van je bitcoins aanzienlijk verhoogt, dus doe het niet. Een klassieke Mnemonic zin wordt in zijn geheel opgeslagen.



## Het geheime delen van Shamir in SLIP39



Het cryptografische mechanisme dat ten grondslag ligt aan *Multi-share* back-ups op Trezor is het *Shamir's Secret Sharing Scheme* (SSSS). Het principe is als volgt: geheime informatie (in dit geval de seed van de Wallet) wordt omgezet in een wiskundige polynoom. Vervolgens worden verschillende punten van deze polynoom berekend, die elk een share worden. Het originele geheim wordt gereconstrueerd door polynomiale interpolatie, door een minimum aantal punten te verzamelen (de drempel).



Er kan geen geheime informatie worden afgeleid uit een aantal aandelen onder de drempelwaarde, waardoor een perfecte theoretische beveiliging van de geheime informatie wordt gegarandeerd. Met andere woorden, zelfs een aanvaller met onbeperkte rekenkracht kan seed niet raden als de drempelwaarde niet wordt bereikt.



SLIP39 gebruikt dit schema om de seed Wallet te verdelen. Elk deel is een zin van 20 woorden, opgebouwd uit een lijst van 1024 woorden (anders dan de BIP39-lijst).



## Een back-up met meerdere delen instellen op een Trezor



Bij het maken van je Wallet op Trezor heb je drie verschillende opties:




- Gebruik een klassieke BIP39 Mnemonic zin van 12 of 24 woorden;
- Gebruik een enkelvoudige Mnemonic zinsdeel (SLIP39);
- Meerdere Mnemonic zinnen configureren in Multi-share (SLIP39).



Als je kiest voor een SLIP39 Mnemonic frase met één woord, kun je later upgraden naar een Multi-share zonder de Wallet opnieuw in te stellen. Als je daarentegen begint met een klassieke BIP39 Wallet (12- of 24-woorden zin), kun je die niet direct omzetten naar een Multi-share. Je moet dan helemaal opnieuw een nieuwe Multi-share Wallet aanmaken en je geld van de oude Wallet overzetten naar de nieuwe via één of meer Bitcoin transacties. Dit is een complexere en duurdere operatie. Als je deze migratie wilt doen, raad ik je aan een nieuwe Hardware Wallet Trezor te kopen om te voorkomen dat je je seed moet invoeren op een Wallet software.



In deze tutorial bekijken we eerst hoe je een Multi-share instelt bij het aanmaken van een Wallet. Daarna zien we hoe je een Single-share omzet in een Multi-share op een bestaande Wallet.



Als je hulp nodig hebt bij de eerste installatie van je apparaat, hebben we ook een gedetailleerde handleiding voor elk Trezor-model:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Op een nieuwe Wallet



Je hebt nu de eerste configuratie van je Trezor voltooid en bent klaar om de Wallet aan te maken. Klik in Trezor Suite op de knop "*Nieuw Wallet maken*".



![Image](assets/fr/02.webp)



Kies de optie "*Multi-share Backup*" en klik dan op "*Creëer Wallet*".



![Image](assets/fr/03.webp)



Accepteer de gebruiksvoorwaarden op uw Trezor en bevestig het aanmaken van de Wallet.



![Image](assets/fr/04.webp)



Klik in Trezor Suite op "*Doorgaan met back-up*".



![Image](assets/fr/05.webp)



Lees de instructies zorgvuldig, bevestig ze en klik dan op "*Create Wallet backup*".



![Image](assets/fr/06.webp)



Voor meer informatie over de juiste manier om je Mnemonic zinnen op te slaan en te beheren, raad ik je aan deze andere tutorial te volgen, vooral als je een beginner bent:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Selecteer op de Trezor het totale aantal aandelen dat je wilt configureren. De meest voorkomende configuraties zijn 2-de-3 en 3-de-5. Voor dit voorbeeld maak ik een 2-de-3, dus selecteer ik 3 shares. Elk share vertegenwoordigt een Mnemonic-zin van 20 woorden.



*Voor Safe 5-gebruikers staat er op het scherm weliswaar "Tik om door te gaan", maar u moet omhoog vegen om te bevestigen*



![Image](assets/fr/07.webp)



Bevestig dan de drempel, d.w.z. het aantal aandelen dat nodig is om weer toegang te krijgen tot het Wallet en de bitcoins die het bevat.



![Image](assets/fr/08.webp)



De Trezor maakt je verschillende shares (Mnemonic zinnen) aan met behulp van zijn random nummergenerator. Zorg ervoor dat je niet in de gaten wordt gehouden tijdens deze operatie. Schrijf de woorden op het scherm op een fysieke drager naar keuze. Het is belangrijk om de woorden genummerd en in volgorde te houden.



Ik raad je aan om elk aandeel op een apart medium te noteren en de opslag zorgvuldig te beheren om te voorkomen dat er meerdere op dezelfde plaats toegankelijk zijn. Bijvoorbeeld, voor een 2-van-3 configuratie zoals de mijne, zou een optie zijn om een deel bij mij thuis te bewaren, een ander bij een vertrouwde vriend en de laatste in een bankkluis. De keuze van opslaglocaties hangt af van je persoonlijke beveiligingsstrategie.



Bovenaan het scherm zie je welke share je momenteel bekijkt.



natuurlijk mag je deze woorden nooit delen op het internet, zoals ik in deze tutorial doe. Dit voorbeeld Wallet wordt alleen gebruikt op de Testnet en wordt verwijderd aan het einde van de tutorial.



![Image](assets/fr/09.webp)



Klik onderaan het scherm om naar de volgende woorden te gaan. Je kunt achteruit gaan door naar beneden te schuiven. Als je alle woorden hebt opgeschreven, houd je je vinger op het scherm om naar het volgende deel te gaan en herhaal de handeling.



![Image](assets/fr/10.webp)



Aan het einde van elke share-opname wordt je gevraagd om de woorden in je Mnemonic-zin te selecteren om te bevestigen dat je ze correct hebt opgeschreven.



![Image](assets/fr/11.webp)



En dat is het, je hebt met succes een back-up gemaakt van je Wallet met de Multi-share optie. U kunt nu doorgaan met de rest van de configuratie-instructies.



### Op een bestaande Wallet met één aandeel



Als je al een Trezor Wallet hebt met een single-share back-up (een SLIP39 Mnemonic zin, niet de klassieke BIP39 zin), en je wilt de beschikbaarheid en veiligheid van je Wallet back-up verbeteren, dan kun je een multi-share systeem opzetten zonder je bitcoins over te dragen.



Om dit te doen, sluit je je Hardware Wallet aan en ontgrendel je deze. Ga in Trezor Suite naar Instellingen.



![Image](assets/fr/12.webp)



Ga naar het tabblad "*Device*".



![Image](assets/fr/13.webp)



Klik vervolgens op "*Multi-share back-up maken*".



![Image](assets/fr/14.webp)



Lees de instructies en klik vervolgens op "*Multi-share back-up maken*".



![Image](assets/fr/15.webp)



Je moet dan je huidige Mnemonic-zin (single-share) invoeren op je Trezor-scherm. Selecteer het aantal woorden (standaard 20).



![Image](assets/fr/16.webp)



Gebruik vervolgens het schermtoetsenbord van de Trezor om elk woord van je huidige Mnemonic zin in te voeren.



![Image](assets/fr/17.webp)



Je kunt dan de configuratie van je Multi-share Backup kiezen door de instructies in de vorige sectie te volgen.



![Image](assets/fr/18.webp)



Als je eenmaal je Multi-share Backup hebt gemaakt, moet je beslissen wat je doet met je originele Single-share Mnemonic zinsdeel. Aangezien de Bitcoin Wallet hetzelfde blijft, zal deze enkele zin altijd toegang verlenen. Dit zal afhangen van je beveiligingsstrategie, maar in het algemeen is het aan te raden om deze zin te vernietigen om dit enkele punt van mislukking te elimineren, wat precies het doel is van Multi-share Backup. Als je besluit om het te vernietigen, zorg er dan voor dat je dit veilig doet, want **het geeft nog steeds toegang tot je bitcoins**.



Gefeliciteerd, je bent nu op de hoogte van het gebruik van Single-share en Multi-share Backups op Trezor hardware wallets. Als je je Wallet beveiliging nog een stapje verder wilt brengen, bekijk dan deze tutorial over BIP39 wachtzinnen:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!



## Extra middelen





- [SLIP-0039: Shamir's Secret-Sharing voor Mnemonic Codes](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share back-up op Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamir's geheim delen](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).