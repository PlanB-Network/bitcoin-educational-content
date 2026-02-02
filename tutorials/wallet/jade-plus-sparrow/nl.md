---
name: Jade Plus - Sparrow
description: Geavanceerde configuratie van Jade Plus met Sparrow wallet
---
![cover](assets/cover.webp)


Jade Plus is een Bitcoin-only Hardware Wallet ontworpen door Blockstream. Het is de opvolger van de klassieke Jade, met softwareverbeteringen, meer opties en opnieuw ontworpen ergonomie voor intuïtiever gebruik. Deze nieuwe versie heeft een prachtig 1,9 inch LCD-scherm, met een breder kleurengamma dan zijn voorganger. Knoppen en menunavigatie zijn ook geoptimaliseerd.


De Jade Plus kan op verschillende manieren worden gebruikt: via een USB-C bedrade verbinding, in "*Air-Gap*" modus met een micro SD-kaart (adapter vereist), via Bluetooth of zelfs door QR-codes uit te wisselen dankzij de geïntegreerde camera. Deze Hardware Wallet werkt op batterijen.


Hij is verkrijgbaar vanaf 149,99 dollar in de zwarte basisversie, en de prijs kan tot 20 dollar stijgen voor de versies "*Genesis Grey*" of "*Lunar Silver*". De Jade Plus is daarom een interessante keuze, met geavanceerde functionaliteiten die vergelijkbaar zijn met die van high-end hardware wallets zoals Coldcard Q of Passport V2, maar tegen een vrij lage prijs, dicht bij mid-range modellen.


![JADE-PLUS-SPARROW](assets/fr/01.webp)


Jade Plus is compatibel met de meeste Wallet beheersoftware. Hier is een overzicht van de compatibiliteit op het moment van schrijven (januari 2025):


| Management Software  | Desktop | Mobile | USB | Bluetooth   | QR  | JadeLink |
| -------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green    | 🟢      | 🟢     | 🟢  | 🟢 (Mobile) | 🟢  | 🔴       |
| Liana                | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Sparrow              | 🟢      | 🔴     | 🟢  | 🔴          | 🟢  | 🟢       |
| Nunchuk              | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Specter              | 🟢      | 🔴     | 🔴  | 🔴          | 🟢  | 🟢       |
| BlueWallet           | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Electrum             | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Keeper               | 🔴      | 🟢     | 🔴  | 🔴          | 🟢  | 🔴       |

In deze tutorial gaan we een geavanceerde configuratie van de Jade Plus opzetten met de Sparrow wallet software in QR-codes modus. Deze configuratie is ideaal voor gemiddelde of ervaren gebruikers. Als je op zoek bent naar een eenvoudigere aanpak voor beginners, raad ik je aan deze tutorial te bekijken, waarin we de Jade Plus gebruiken met Green Wallet via een Bluetooth-verbinding:


https://planb.academy/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Het Jade Plus-veiligheidsmodel


De Jade Plus gebruikt een beveiligingsmodel gebaseerd op een "virtueel secure element", gematerialiseerd door een "blind orakel". Concreet combineert dit mechanisme de door de gebruiker gekozen PIN-code, een geheim dat gehost wordt op de Jade en een geheim dat bewaard wordt door het orakel (een server die onderhouden wordt door Blockstream), om een AES-256-sleutel te maken die verdeeld wordt over twee entiteiten. Tijdens de initiatie beveiligt een ECDH Exchange de communicatie met het orakel en versleutelt de herstelzin op de Hardware Wallet. Praktisch gezien, wanneer je toegang wilt tot de seed om transacties te ondertekenen, heb je toegang nodig tot :




- Het Jade Plus-apparaat zelf;
- Naar PIN om het apparaat te ontgrendelen ;
- En het geheim van het orakel.


Het grote voordeel van deze aanpak is de afwezigheid van een single point of failure op hardwareniveau, want als een aanvaller ooit toegang krijgt tot je Jade, moet je voor het extraheren van de sleutels tegelijkertijd de Jade en het orakel compromitteren. Dit model betekent ook dat Jade Plus volledig open-source is, waardoor de beperkingen die gepaard gaan met het gebruik van echt fysiek beveiligde Elements, zoals die bijvoorbeeld gebruikt worden op Ledger, vermeden worden.


Het nadeel van dit systeem is dat het gebruik van Jade Plus afhankelijk is van het orakel dat door Blockstream wordt onderhouden. Als dit orakel ontoegankelijk wordt, is het niet langer mogelijk om de Hardware Wallet direct met de PIN te gebruiken. Dit betekent echter niet dat uw bitcoins verloren zijn, want ze kunnen nog steeds worden teruggehaald met uw herstelzin, die u in Jade Plus in de "*stateless*" modus kunt invoeren. Om deze afhankelijkheid te omzeilen, kunt u ook uw eigen oracle server configureren en beheren.


Een andere optie voor het beheren van uw seed is om deze gewoon niet te registreren op de Jade Plus. In dit geval wordt de Jade alleen een apparaat voor handtekeningen. Tijdens de initialisatie sla je de herstelzin niet alleen op als woorden, maar ook als een met de hand gegenereerde QR-code. Op deze manier kun je elke keer dat je je Wallet gebruikt, de seed importeren met de camera van je Jade. Dit kan een interessante optie zijn voor gevorderde gebruikers, afhankelijk van je beveiligingsstrategie, maar je moet voorzichtig zijn om je seed zowel op te slaan als te beschermen, want zelfs als QR-code zou iedereen je geld kunnen stelen. We bekijken deze optie in deze tutorial, maar het is niet verplicht.


## De Jade Plus uit de verpakking


Als je je Jade Plus ontvangt, controleer dan of de doos en Seal in goede staat zijn om er zeker van te zijn dat je pakket niet geopend is.


![JADE-PLUS-SPARROW](assets/fr/02.webp)


In de doos vind je :




- Le Jade Plus;
- USB-C kabel;
- Kaarten om je Mnemonic zin op te nemen als woorden of als "*CompactSeedQR*";
- Enkele gebruiksaanwijzingen ;
- Een koord;
- Enkele stickers.


![JADE-PLUS-SPARROW](assets/fr/03.webp)


Het apparaat heeft 4 navigatieknoppen:




- De knop rechtsonder zet de Jade aan;
- De grote knop aan de voorkant van het apparaat wordt gebruikt om een item te selecteren;
- Met de twee kleine knoppen bovenaan kun je naar links en rechts navigeren;
- Je kunt ook een item selecteren door tegelijkertijd op de twee knoppen bovenaan het apparaat te klikken.


![JADE-PLUS-SPARROW](assets/fr/04.webp)


## Een nieuwe Bitcoin Wallet opzetten


Klik op de startknop.


![JADE-PLUS-SPARROW](assets/fr/05.webp)


Klik op "*Setup Jade*".


![JADE-PLUS-SPARROW](assets/fr/06.webp)


Selecteer "**Advanced Setup**".


![Image](assets/fr/07.webp)


Klik dan op "*Maak een nieuwe Wallet*" om generate een nieuwe seed te maken. Je kunt kiezen tussen een Mnemonic zin van 12 of 24 woorden. De beveiliging van je Wallet blijft gelijk met beide opties, dus het kan handiger zijn om de eenvoudigste optie te kiezen om op te slaan, d.w.z. 12 woorden.


![Image](assets/fr/08.webp)


Klik op de knop "*Doorgaan*" om je nieuwe herstelzin weer te geven.


![Image](assets/fr/09.webp)


Uw Jade Plus toont uw 12-woord Mnemonic zin. **Deze Mnemonic geeft u volledige, onbeperkte toegang tot al uw bitcoins. Iedereen die in het bezit is van deze zin kan uw fondsen stelen, zelfs zonder fysieke toegang tot uw Jade Plus. De 12-woorden zin herstelt de toegang tot uw bitcoins in geval van verlies, diefstal of breuk van uw Jade. Het is daarom erg belangrijk om het zorgvuldig te bewaren en op een veilige locatie op te bergen.**


Je kunt het op het meegeleverde karton schrijven, of voor extra veiligheid raad ik aan om het op een roestvrijstalen basis te graveren om het te beschermen tegen brand, overstroming of instorting.


![Image](assets/fr/10.webp)


Voor meer informatie over de juiste manier om je Mnemonic zinnen op te slaan en te beheren, raad ik je aan deze andere tutorial te volgen, vooral als je een beginner bent:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

natuurlijk mag je deze woorden nooit delen op het Internet, zoals ik in deze tutorial doe. Dit voorbeeld Wallet zal alleen gebruikt worden op Testnet en zal verwijderd worden aan het einde van de tutorial.


Klik op de pijl aan de rechterkant van het scherm om de volgende woorden weer te geven.


![Image](assets/fr/11.webp)


Zodra je je zin hebt opgeslagen, vraagt Jade Plus je om de zin te bevestigen. Selecteer het juiste woord volgens de volgorde met de knoppen bovenaan het apparaat en klik op de middelste knop om naar het volgende woord te gaan.


![Image](assets/fr/12.webp)


Je hebt dan 2 opties. Zoals uitgelegd in de inleiding, kun je ervoor kiezen om je seed direct op het apparaat op te slaan en Blockstream's "*Virtuele secure element*" beveiligingssysteem te gebruiken om toegang te krijgen tot je Wallet (Optie 1), of je seed op te slaan als een QR-code en deze elke keer te scannen als je hem gebruikt (Optie 2).


Selecteer voor optie 1 "*Nee*" en voor optie 2 "*Yes*".


![Image](assets/fr/13.webp)


### Optie 1: QR PIN ontgrendelen


Als je optie 1 hebt gekozen (CompactSeedQR: "*No*"), ga je direct naar de selectie van de verbindingsmethode. In deze tutorial willen we het apparaat gebruiken in Air-Gap modus via QR code uitwisselingen, dus selecteer "*QR*".


![Image](assets/fr/27.webp)


Klik op "*Doorgaan*".


![Image](assets/fr/28.webp)


De PIN-code wordt gebruikt om uw Jade te ontgrendelen en biedt bescherming tegen onbevoegde fysieke toegang. Deze PIN-code is niet betrokken bij de afleiding van de cryptografische sleutels van uw Wallet. Dus zelfs zonder toegang tot deze PIN-code, kunt u met uw 12-woord Mnemonic zin weer toegang krijgen tot uw bitcoins. We raden u aan een PIN-code te kiezen die zo willekeurig mogelijk is. Zorg er ook voor dat u deze code opslaat op een andere plaats dan waar uw Jade is opgeslagen, zoals in een wachtwoordmanager.


Kies een 6-cijferige pincode op je Jade, gebruik de linker- en rechterknop om door de cijfers te bladeren en de middelste knop om elk cijfer te bevestigen.


![Image](assets/fr/29.webp)


Bevestig uw pincode een tweede keer.


![Image](assets/fr/30.webp)


Zoals uitgelegd in de inleiding, wordt uw seed versleuteld opgeslagen op de Jade Plus. Om het te decoderen, moet u :




- De geldige PIN-code (die we zojuist hebben ingesteld) ;
- Het geheim van het orakel dat door Blockstream wordt onderhouden.


In deze geavanceerde tutorial gebruiken we Sparrow wallet om onze Bitcoin Wallet te beheren. In tegenstelling tot de Green Wallet software van Blockstream, heeft Sparrow echter geen toegang tot het orakel op de servers van Blockstream. Daarom gebruiken we de website van Blockstream om het orakelgeheim op te halen telkens als we Jade Plus ontgrendelen.


Bezoek https://jadefw.blockstream.com/pinqr/index.html


Klik op "*Start QR Unlock*".


![Image](assets/fr/31.webp)


Klik op "*Done*", omdat u uw PIN-code al op de Jade Plus hebt gekozen.


![Image](assets/fr/32.webp)


Gebruik de camera van je computer om de QR-codes op het scherm van je Jade te scannen.


![Image](assets/fr/33.webp)


Bevestig op je Jade om naar het volgende scherm te gaan.


![Image](assets/fr/34.webp)


Scan de QR-code die nu op de website staat om het geheim van het orakel te achterhalen.


![Image](assets/fr/35.webp)


Nu je Wallet is aangemaakt, kun je doorgaan met de volgende stappen en subsectie "*Optie 2: CompactSeedQR*" overslaan.


![Image](assets/fr/36.webp)


Elke keer dat je opstart, klik je op "*QR Mode*".


![Image](assets/fr/37.webp)


Selecteer "*QR PIN Unlock*".


![Image](assets/fr/38.webp)


Voer uw pincode in.


![Image](assets/fr/39.webp)


Ga dan naar [de Blockstream website](https://jadefw.blockstream.com/pinqr/qrpin.html) om Exchange QR-codes te Exchange met het orakel.


![Image](assets/fr/40.webp)


Je Jade is nu ontgrendeld.


![Image](assets/fr/41.webp)


### Optie 2: CompactSeedQR


Als je optie 2 hebt gekozen (CompactSeedQR: "*Yes*"), klik dan nogmaals op "*Yes*".


![Image](assets/fr/14.webp)


Klik op "*Start*".


![Image](assets/fr/15.webp)


Je kunt de QR-codebasis gebruiken die in de Jade Plus doos zit. Selecteer het juiste vakje, afhankelijk van of je hebt gekozen voor een zin van 12 of 24 woorden. Je kunt ook [de sjabloon van de Blockstream website afdrukken](https://help.blockstream.com/hc/article_attachments/41928319071769).


Uw Jade Plus zal elke zone van uw QR code weergeven.


![Image](assets/fr/16.webp)


Gebruik een pen om de vierkantjes in te kleuren en reproduceer je seed als een QR-code. Wees nauwkeurig zodat de Jade Plus camera het later kan scannen. Gebruik de pijl om naar het volgende gebied te gaan.


![Image](assets/fr/17.webp)


Klik op "*Done*" als je klaar bent.


![Image](assets/fr/18.webp)


Scan je handgemaakte QR-code met de Jade Plus om de geldigheid te controleren.


![Image](assets/fr/19.webp)


Als de back-up van je papier correct is, klik je op "*Doorgaan*".


![Image](assets/fr/20.webp)


In deze tutorial gebruiken we een verbindingsmodus die uitsluitend gebaseerd is op het scannen van QR-codes, dus selecteer "*QR*".


![Image](assets/fr/21.webp)


U kunt er ook voor kiezen om een PIN toe te voegen aan uw CompactSeedQR back-up, zoals in optie 1. Dit biedt twee manieren om toegang te krijgen tot uw Wallet: ofwel via de PIN en Blockstream's "Virtuele secure element" systeem, of via de CompactSeedQR.


Als u voor de dubbele PIN-optie kiest, selecteer dan "*PIN*" en volg dezelfde stappen als bij optie 1 om uw PIN-code in te stellen.


Als je liever alleen doorgaat met CompactSeedQR, selecteer dan "*SeedQR*".


![Image](assets/fr/22.webp)


Nu je Wallet is aangemaakt, kun je verder gaan met de volgende stappen.


![Image](assets/fr/23.webp)


Elke keer dat je opstart, klik je op de knop "*QR Mode*" en vervolgens op "*Scan SeedQR*".


![Image](assets/fr/24.webp)


Gebruik de camera van het apparaat om uw opgeslagen seed als QR-code te scannen.


![Image](assets/fr/25.webp)


Je Jade is nu ontgrendeld.


![Image](assets/fr/26.webp)


## Een BIP39 passphrase toevoegen


Een BIP39 passphrase is een optioneel wachtwoord dat u vrij kunt kiezen en dat aan uw Mnemonic zin wordt toegevoegd om de Wallet beveiliging te versterken. Als deze functie is ingeschakeld, is voor toegang tot uw Bitcoin Wallet zowel de Mnemonic als de passphrase vereist. Zonder één van beide is het onmogelijk om de Wallet te herstellen.


Voordat u deze optie configureert op uw Jade Plus, is het sterk aanbevolen dat u dit artikel leest om de theoretische werking van de passphrase volledig te begrijpen en fouten te vermijden die kunnen leiden tot het verlies van uw bitcoins:


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Terwijl je Jade nog steeds vergrendeld is (de passphrase kan alleen worden ingevoerd als het apparaat niet ontgrendeld is), ga je naar het menu "*Options*".


![Image](assets/fr/42.webp)


Selecteer "*BIP39 passphrase*".


![Image](assets/fr/43.webp)


In de optie "*Frequentie*" kun je kiezen of Jade Plus je elke keer als het opstart vraagt om je passphrase in te voeren:




- "*Disabled*" schakelt het gebruik van een passphrase uit;
- "*Next Login Only*" vereist dat u terugkeert naar dit menu om de aanvraag voor uw passphrase bij de volgende start te activeren. Met deze optie kunt u het gebruik ervan niet onthullen;
- "*Always Ask*" zorgt ervoor dat Jade bij elke opstart systematisch om je passphrase vraagt, en zo onthult dat je Wallet wordt beschermd door een passphrase.


Kies de optie op basis van je beveiligingsstrategie. Persoonlijk selecteer ik "*Altijd vragen*" voor het voorbeeld.


![Image](assets/fr/44.webp)


Je kunt dan kiezen uit twee methoden om je passphrase in te voeren:




- "*Handmatig*: Met een virtueel toetsenbord kun je letters (hoofdletters en kleine letters), cijfers en symbolen invoeren, teken voor teken. Dit is de standaardmethode voor alle hardware wallets;
- "*WordList*": Specifieke methode ontworpen door Blockstream voor Jade, die het invoeren van passphrase versnelt en de entropie ervan verhoogt. Tijdens de invoer suggereert het systeem woorden uit de BIP39-lijst, wat het ontgrendelen makkelijker maakt. Deze methode genereert automatisch een zin door de gekozen woorden, gescheiden door spaties, aan elkaar te rijgen (voorbeeld: `abandon ability able`).


Persoonlijk adviseer ik je om de eerste methode te gebruiken, omdat dit de standaard is die je zult vinden op alle andere Wallet dragers.


![Image](assets/fr/45.webp)


Je kunt dan terugkeren naar het beginscherm en je Wallet ontgrendelen zoals je gewend bent, met je PIN-code of je CompactSeedQR (zoals hierboven te zien is). Vervolgens wordt u gevraagd uw passphrase in te voeren.


![Image](assets/fr/46.webp)


Voer het in op het Jade toetsenbord en zorg ervoor dat je een of meer back-ups maakt op fysieke media (papier of metaal). In het voorbeeld gebruik ik een erg zwakke passphrase, maar jij moet een sterke, willekeurige passphrase kiezen die alle soorten tekens bevat en lang genoeg is (zoals een sterk wachtwoord).


![Image](assets/fr/47.webp)


Als je passphrase geldig is, bevestig dan.


![Image](assets/fr/48.webp)


Let op: BIP39 wachtzinnen zijn hoofdletter- en tikfoutgevoelig. Als u een passphrase invoert die net iets anders is dan de aanvankelijk geconfigureerde, zal Jade geen fout melden, maar een andere set cryptografische sleutels afleiden die niet overeenkomen met die in uw aanvankelijke Wallet.


Het is daarom belangrijk om bij het configureren je master key fingerprint te noteren, die kun je rechtsonder in het scherm vinden. Bijvoorbeeld, met mijn passphrase `Plan ₿ Academy`, is mijn master key fingerprint `3AD1AE65`.


![Image](assets/fr/49.webp)


Elke keer dat je je Jade ontgrendelt met je passphrase, controleer je of de vingerafdruk dezelfde is als die je tijdens de configuratie hebt ingevoerd. Als dat zo is, is je passphrase correct en heb je toegang tot de juiste Bitcoin Wallet. Als dat niet zo is, zit je op de verkeerde Wallet en moet je het opnieuw proberen. Zo niet, dan zit je op de verkeerde Wallet en moet je het opnieuw proberen, waarbij je moet opletten dat je geen invoerfouten maakt.


Voordat je je eerste bitcoins ontvangt in je Wallet, **raad ik je sterk aan om een lege hersteltest uit te voeren**. Noteer wat referentie informatie, zoals je xpub of de eerste ontvangen Address, wis dan je Wallet op de Jade Plus terwijl het nog leeg is (`Options -> Device -> Factory Reset`). Probeer dan je Wallet te herstellen met behulp van je papieren back-ups van de Mnemonic zin en eventuele passphrase. Controleer of de cookie-informatie die na het herstel wordt gegenereerd, overeenkomt met degene die je oorspronkelijk hebt opgeschreven. Als dat zo is, kun je er zeker van zijn dat je papieren back-ups betrouwbaar zijn. Als je meer wilt weten over hoe je een testherstel uitvoert, bekijk dan deze andere tutorial:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Wallet configureren op Sparrow wallet


In deze tutorial presenteer ik een geavanceerd gebruik van Jade Plus met Sparrow wallet. Deze Hardware Wallet is echter compatibel met vele andere programma's, zoals Liana, Nunchuk, Specter, Green en Keeper. Deze compatibiliteit varieert in termen van verbindingen: USB, Bluetooth of QR-code (zie de tabel in de inleiding voor details).


Begin met het downloaden en installeren van Sparrow wallet [van de officiële website](https://sparrowwallet.com/) op je computer, als je dat nog niet hebt gedaan.


![Image](assets/fr/50.webp)


Zorg ervoor dat je de authenticiteit en integriteit van de software controleert voordat je deze installeert. Als je niet weet hoe je dit moet doen, raadpleeg dan deze handleiding:


https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Als Sparrow wallet geopend is, klik dan op het tabblad "*Bestand*" en vervolgens op "*Nieuw Wallet*".


![Image](assets/fr/51.webp)


Geef je Wallet een naam en klik dan op "*Creëer Wallet*".


![Image](assets/fr/52.webp)


Selecteer "*Airgapped Hardware Wallet*".


![Image](assets/fr/53.webp)


Klik op "*Scan...*" naast de optie "*Jade*".


![Image](assets/fr/54.webp)


Ontgrendel je Jade Plus en, als je er een gebruikt, voer je passphrase in. Ga dan naar het menu "*Options*", selecteer "*Wallet*" en klik op "*Export Xpub*".


![Image](assets/fr/55.webp)


Je Jade toont je Keystore via verschillende QR-codes. Scan ze op je machine met Sparrow.


![Image](assets/fr/56.webp)


Je zou nu je xpub en je master key vingerafdruk moeten zien, die moet overeenkomen met die op je Jade Plus. Klik op "*Toepassen*".


![Image](assets/fr/57.webp)


Stel een sterk wachtwoord in om de toegang tot je Sparrow wallet te beveiligen. Dit wachtwoord beschermt je publieke sleutels, adressen, labels en transactiegeschiedenis tegen ongeautoriseerde toegang. Het is een goed idee om dit wachtwoord op te slaan in een wachtwoordmanager, zodat je het niet vergeet.


![Image](assets/fr/58.webp)


Uw Wallet is nu correct geconfigureerd op Sparrow.


![Image](assets/fr/59.webp)


## Bitcoins ontvangen


Nu je Jade Plus geconfigureerd is, ben je klaar om je eerste Sats te ontvangen op je nieuwe Bitcoin Wallet. Klik hiervoor op Sparrow op het menu "*Ontvangen*".


![Image](assets/fr/60.webp)


Sparrow toont de eerste lege ontvangst Address in uw Wallet.


![Image](assets/fr/61.webp)


Voordat we het gebruiken, controleren we het op het Jade Plus scherm om er zeker van te zijn dat het bij onze Bitcoin Wallet hoort. Klik op de Jade op "*Scan QR*" en scan de QR-code van de Address die op de Sparrow staat.


![Image](assets/fr/62.webp)


Controleer of de Address op het scherm van uw Jade overeenkomt met de Sparrow wallet. Als dat zo is, klik dan op het vinkje om verder te gaan.


![Image](assets/fr/63.webp)


Uw Hardware Wallet zal dan bevestigen dat deze Address deel uitmaakt van uw Wallet en dat het de bijbehorende privésleutel bezit.


![Image](assets/fr/64.webp)


Als de Address gevalideerd is door je Jade, kun je hem nu gebruiken om bitcoins te ontvangen. Wanneer de transactie wordt uitgezonden op het netwerk, verschijnt deze op Sparrow. Wacht tot je genoeg bevestigingen hebt ontvangen om de transactie als definitief te beschouwen.


![Image](assets/fr/65.webp)


## Bitcoins versturen


Nu je een paar Sats in je Wallet hebt, kun je er ook een paar versturen. Klik daarvoor op het menu "*UTXOs*".


![Image](assets/fr/66.webp)


Selecteer de UTXO's die je wilt gebruiken als invoer voor deze transactie en klik vervolgens op "*Send Selected*".


![Image](assets/fr/67.webp)


Voer de Address van de ontvanger in, een label om je te herinneren aan het doel van de transactie en het bedrag dat je naar deze Address wilt sturen.


![Image](assets/fr/68.webp)


Pas het tarief aan volgens de huidige marktomstandigheden en klik vervolgens op "*Creëer transactie*".


![Image](assets/fr/69.webp)


Controleer of alle transactieparameters correct zijn en klik dan op "*Transactie voltooien voor ondertekening*".


![Image](assets/fr/70.webp)


Klik op "*Toon QR*" om PSBT (*Partially Signed Bitcoin Transaction*) weer te geven. Sparrow heeft de transactie gebouwd, maar het mist nog de handtekeningen om de bitcoins te ontgrendelen die gebruikt zijn bij de invoer. Deze handtekeningen kunnen alleen worden uitgevoerd door Jade Plus, die uw seed host en toegang geeft tot de privésleutels die nodig zijn om de transactie te ondertekenen.


![Image](assets/fr/71.webp)


Klik op uw Jade Plus op "*Scan QR*" om de PSBT te scannen die wordt weergegeven op de Sparrow.


![Image](assets/fr/72.webp)


Controleer of de levering Address en het verzonden bedrag correct zijn en klik dan op de pijl om te valideren.


![Image](assets/fr/73.webp)


Controleer of het bedrag overeenkomt met het bedrag dat je hebt gekozen en klik vervolgens op het vinkje in de linkerbovenhoek van de Interface om de transactie te ondertekenen.


![Image](assets/fr/74.webp)


Klik op de Sparrow wallet op "*Scan QR*" en scan de QR-code die op je Jade staat.


![Image](assets/fr/75.webp)


Je ondertekende transactie is nu klaar om uitgezonden te worden op het Bitcoin netwerk en opgenomen te worden in een blok door een Miner. Als alles correct is, klik je op "*Transactie uitzenden*".


![Image](assets/fr/76.webp)


Je transactie is verzonden en wacht op bevestiging.


![Image](assets/fr/77.webp)


Gefeliciteerd, je weet nu hoe je de Jade Plus in QR modus kunt instellen en gebruiken. Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Bedankt voor het delen!


Om verder te gaan, raad ik deze andere tutorial over de Jade Plus aan, waar we hem via Bluetooth configureren met de Green mobiele app:


https://planb.academy/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0