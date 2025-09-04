---
name: Jade Plus - Green
description: Jade Plus eenvoudig configureren met Green
---
![cover](assets/cover.webp)


![video](https://youtu.be/rv_cN7F7-TM)


Jade Plus is een Bitcoin-only Hardware Wallet ontworpen door Blockstream. Het is de opvolger van de klassieke Jade, met softwareverbeteringen, meer opties en opnieuw ontworpen ergonomie voor intuïtiever gebruik. Deze nieuwe versie heeft een prachtig 1,9 inch LCD-scherm, met een breder kleurengamma dan zijn voorganger. Knoppen en menunavigatie zijn ook geoptimaliseerd.


De Jade Plus kan op verschillende manieren worden gebruikt: via een USB-C bedrade verbinding, in "*Air-Gap*" modus met een micro SD-kaart (adapter vereist), via Bluetooth of zelfs door QR-codes uit te wisselen dankzij de geïntegreerde camera. Deze Hardware Wallet werkt op batterijen.


Hij is verkrijgbaar vanaf 149,99 dollar in de zwarte basisversie, en de prijs kan tot 20 dollar stijgen voor de versies "*Genesis Grey*" of "*Lunar Silver*". De Jade Plus is daarom een interessante keuze, met geavanceerde functionaliteiten die vergelijkbaar zijn met die van high-end hardware wallets zoals Coldcard Q of Passport V2, maar tegen een vrij lage prijs, dicht bij mid-range modellen.


![JADE-PLUS-GREEN](assets/fr/01.webp)


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

In deze tutorial gaan we de Jade Plus instellen en gebruiken met Blockstream's Green Wallet mobiele app via een Bluetooth verbinding. Deze opstelling is ideaal voor beginners. Als je op zoek bent naar een meer geavanceerde aanpak, raad ik je aan deze tutorial te bekijken, waarin we de Jade Plus gebruiken met Sparrow wallet in QR-codes modus:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Het Jade Plus-veiligheidsmodel


De Jade Plus gebruikt een beveiligingsmodel gebaseerd op een "virtueel secure element", gematerialiseerd door een "blind orakel". Concreet combineert dit mechanisme de door de gebruiker gekozen PIN-code, een geheim dat gehost wordt op de Jade en een geheim dat bewaard wordt door het orakel (een server die onderhouden wordt door Blockstream), om een AES-256-sleutel te maken die verdeeld wordt over twee entiteiten. Tijdens de initiatie beveiligt een ECDH Exchange de communicatie met het orakel en versleutelt de herstelzin op de Hardware Wallet. Praktisch gezien, wanneer je toegang wilt tot de seed om transacties te ondertekenen, heb je toegang nodig tot :




- Naar het Jade Plus-apparaat zelf;
- Naar PIN om het apparaat te ontgrendelen ;
- En het geheim van het orakel.


Het grote voordeel van deze aanpak is de afwezigheid van een single point of failure op hardwareniveau, want als een aanvaller ooit toegang krijgt tot je Jade, moet je voor het extraheren van de sleutels tegelijkertijd de Jade en het orakel compromitteren. Dit model betekent ook dat Jade Plus volledig open-source is, waardoor de beperkingen die gepaard gaan met het gebruik van echt fysiek beveiligde Elements, zoals die bijvoorbeeld gebruikt worden op Ledger, vermeden worden.


Het nadeel van dit systeem is dat het gebruik van Jade Plus afhankelijk is van het orakel dat door Blockstream wordt onderhouden. Als dit orakel ontoegankelijk wordt, is het niet langer mogelijk om de Hardware Wallet direct met de PIN te gebruiken. Dit betekent echter niet dat uw bitcoins verloren zijn, want ze kunnen nog steeds worden teruggehaald met uw herstelzin, die u in Jade Plus in de "*stateless*" modus kunt invoeren. Om deze afhankelijkheid te omzeilen, kunt u ook uw eigen oracle server configureren en beheren.


## De Jade Plus uit de verpakking


Wanneer u uw Jade Plus ontvangt, controleer dan of de doos en Seal in goede staat zijn om er zeker van te zijn dat uw pakket niet geopend is.


![JADE-PLUS-GREEN](assets/fr/02.webp)


In de doos vind je :




- Le Jade Plus;
- USB-C kabel;
- Kaarten om je Mnemonic zin op te nemen als woorden of als "*CompactSeedQR*";
- Enkele gebruiksaanwijzingen ;
- Een koord;
- Enkele stickers.


![JADE-PLUS-GREEN](assets/fr/03.webp)


Het apparaat heeft 4 navigatieknoppen:




- De knop rechtsonder zet de Jade aan;
- De grote knop aan de voorkant van het apparaat wordt gebruikt om een item te selecteren;
- Met de twee kleine knoppen bovenaan kun je naar links en rechts navigeren;
- Je kunt ook een item selecteren door tegelijkertijd op de twee knoppen bovenaan het apparaat te klikken.


![JADE-PLUS-GREEN](assets/fr/04.webp)


## Een nieuwe Bitcoin Wallet instellen


Klik op de startknop.


![JADE-PLUS-GREEN](assets/fr/05.webp)


Klik op "*Setup Jade*".


![JADE-PLUS-GREEN](assets/fr/06.webp)


Kies "Begin Setup". De optie "*Advanced Setup*" doet hetzelfde, maar met toegang tot geavanceerde instellingen.


![JADE-PLUS-GREEN](assets/fr/07.webp)


Klik dan op "*Create a New Wallet*" om generate een nieuwe seed te maken.


![JADE-PLUS-GREEN](assets/fr/08.webp)


Klik op de knop "*Doorgaan*" om je nieuwe herstelzin weer te geven.


![JADE-PLUS-GREEN](assets/fr/09.webp)


Je Jade Plus toont je 12-woorden Mnemonic zin. **Deze Mnemonic geeft u volledige, onbeperkte toegang tot al uw bitcoins. Iedereen die in het bezit is van deze zin kan uw fondsen stelen, zelfs zonder fysieke toegang tot uw Jade Plus. De 12-woorden zin herstelt de toegang tot uw bitcoins in geval van verlies, diefstal of breuk van uw Jade. Het is daarom erg belangrijk om het zorgvuldig te bewaren en op een veilige locatie op te bergen.


Je kunt het op het meegeleverde karton schrijven, of voor extra veiligheid raad ik aan om het op een roestvrijstalen basis te graveren om het te beschermen tegen brand, overstroming of instorting.


![JADE-PLUS-GREEN](assets/fr/10.webp)


Voor meer informatie over de juiste manier om je Mnemonic zin op te slaan en te beheren, raad ik je aan om deze andere tutorial te volgen, vooral als je een beginner bent:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***Het spreekt voor zich dat je deze woorden nooit mag delen op het Internet, zoals ik doe in deze tutorial. Dit voorbeeld Wallet wordt alleen gebruikt op Testnet en wordt verwijderd aan het einde van de tutorial


Klik op de pijl aan de rechterkant van het scherm om de volgende woorden weer te geven.


![JADE-PLUS-GREEN](assets/fr/11.webp)


Zodra je je zin hebt opgeslagen, vraagt Jade Plus je om de zin te bevestigen. Selecteer het juiste woord volgens de volgorde met de knoppen bovenaan het apparaat en klik op de middelste knop om naar het volgende woord te gaan.


![JADE-PLUS-GREEN](assets/fr/12.webp)


## Jade Plus aansluiten op Green Wallet


In deze tutorial gebruiken we de Green Wallet toepassing om de Wallet gehost op de Jade Plus te beheren. Deze methode is vooral geschikt voor beginners. Als je je Bitcoin Wallet gedetailleerder wilt beheren, kun je ook Sparrow wallet gebruiken, die we in een aparte tutorial behandelen:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Voor instructies over het installeren en instellen van de Blockstream Green toepassing, zie het eerste deel van deze andere tutorial:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Klik in de Blockstream Green-toepassing op de knop '*Een nieuwe Wallet configureren*'.


![JADE-PLUS-GREEN](assets/fr/13.webp)


Selecteer "*Op Hardware Wallet*".


![JADE-PLUS-GREEN](assets/fr/14.webp)


Activeer Bluetooth op je smartphone en klik vervolgens op de knop "*Connect your Jade*".


![JADE-PLUS-GREEN](assets/fr/15.webp)


Autoriseer de Green toepassing voor toegang tot Bluetooth verbindingen.


![JADE-PLUS-GREEN](assets/fr/16.webp)


De applicatie is op zoek naar je Jade Plus.


![JADE-PLUS-GREEN](assets/fr/17.webp)


Klik op de Jade Plus op het menu "*Bluetooth*".


![JADE-PLUS-GREEN](assets/fr/18.webp)


Selecteer uw apparaat in de Green toepassing.


![JADE-PLUS-GREEN](assets/fr/19.webp)


Bevestig de koppelcode op uw Jade Plus.


![JADE-PLUS-GREEN](assets/fr/20.webp)


Green biedt u een test om te controleren of uw Jade echt is. Klik op de knop om dit te doen.


![JADE-PLUS-GREEN](assets/fr/21.webp)


Bevestig op de Jade.


![JADE-PLUS-GREEN](assets/fr/22.webp)


Green bevestigt dat uw apparaat echt is.


![JADE-PLUS-GREEN](assets/fr/23.webp)


## De pincode instellen


Klik op de knop "*Doorgaan*" om de pincode van je Jade te kiezen.


![JADE-PLUS-GREEN](assets/fr/24.webp)


De PIN-code ontgrendelt uw Jade. Het is daarom een bescherming tegen ongeautoriseerde fysieke toegang. Deze PIN-code is niet betrokken bij de afleiding van de cryptografische sleutels van uw Wallet. Dus zelfs zonder toegang tot deze PIN-code, kunt u met uw 12-woord Mnemonic zin weer toegang krijgen tot uw bitcoins. We raden aan een PIN-code te kiezen die zo willekeurig mogelijk is. En zorg ervoor dat u deze code opslaat op een andere locatie dan waar uw Jade is opgeslagen (bijvoorbeeld in een wachtwoordmanager).


Kies de 6-cijferige pincode op uw Jade door met de knoppen rechts en links door de cijfers te bladeren en met de middelste knop de invoer van een cijfer te bevestigen.


![JADE-PLUS-GREEN](assets/fr/25.webp)


Bevestig uw pincode een tweede keer.


![JADE-PLUS-GREEN](assets/fr/26.webp)


Uw Bitcoin Wallet is aangemaakt.


![JADE-PLUS-GREEN](assets/fr/27.webp)


## Maak een Bitcoin account aan


Je moet nu een account aanmaken in je Wallet. Klik op de knop "*Account aanmaken*".


![JADE-PLUS-GREEN](assets/fr/28.webp)


Kies "*Standaard*" als u een klassieke single-sig Wallet wilt maken.


![JADE-PLUS-GREEN](assets/fr/29.webp)


Voor meer informatie over de "*2FA*" optie kun je deze andere tutorial volgen:


https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Je account is aangemaakt.


![JADE-PLUS-GREEN](assets/fr/30.webp)


Als je je Green Wallet wilt personaliseren, klik dan op de drie kleine puntjes rechtsboven.


![JADE-PLUS-GREEN](assets/fr/31.webp)


Met de optie "*Rename*" kun je de naam van je Wallet aanpassen, wat vooral handig is als je meerdere wallets beheert met dezelfde applicatie. Met het menu "*Unit*" kunt u de basiseenheid van uw Wallet wijzigen. Je kunt er bijvoorbeeld voor kiezen om het weer te geven in satoshis in plaats van bitcoins. Tot slot geeft het menu "*Parameters*" je toegang tot andere opties. Hier vind je bijvoorbeeld je uitgebreide publieke sleutel en zijn Descriptor, handig als je van plan bent een Watch-only wallet van je Jade op te zetten.


![JADE-PLUS-GREEN](assets/fr/32.webp)


Om opnieuw verbinding te maken met je Jade nadat je hem hebt uitgeschakeld, druk je op de aan/uit-knop aan de onderkant van het apparaat. In de Green-toepassing selecteert u uw apparaat op de startpagina:


![JADE-PLUS-GREEN](assets/fr/33.webp)


Voer vervolgens de pincode op je Jade in en je bent weer verbonden.


![JADE-PLUS-GREEN](assets/fr/34.webp)


Je Jade wordt ontgrendeld via Blockstream's "virtuele secure element" (zie het eerste deel van deze tutorial). Dit vereist een Bluetooth-verbinding met de Green-toepassing. Als u problemen ondervindt met de Bluetooth-verbinding tijdens het ontgrendelen, probeer dan de twee apparaten te ontkoppelen en opnieuw te koppelen. Als het probleem zich blijft voordoen, kunt u toch uw Jade ontgrendelen door de optie "*QR Scan*" te selecteren en de instructies te volgen die beschikbaar zijn [op de Blockstream website] (https://jadefw.blockstream.com/pinqr/index.html).


Voordat je je eerste bitcoins ontvangt in je Wallet, **raad ik je sterk aan om een lege hersteltest uit te voeren**. Maak een notitie van wat referentie-informatie, zoals je xpub of de eerste Address die je ontvangt, wis dan je Wallet op de Green app en op de Jade Plus terwijl hij nog leeg is (`Options -> Device -> Factory Reset`). Probeer vervolgens je Wallet te herstellen met je papieren back-ups van de Mnemonic-zin. Controleer of de cookie-informatie die na het herstellen wordt gegenereerd, overeenkomt met de informatie die je oorspronkelijk hebt opgeschreven. Als dit het geval is, kunt u er zeker van zijn dat uw papieren back-ups betrouwbaar zijn. Om meer te weten te komen over hoe je een testherstel uitvoert, kun je deze andere tutorial raadplegen:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Bitcoins ontvangen


Nu je Bitcoin Wallet is ingesteld, ben je klaar om je eerste Sats te ontvangen! Klik gewoon op de knop "*Ontvangen*" op de Green-toepassing.


![JADE-PLUS-GREEN](assets/fr/35.webp)


Green geeft een ontvangst Address weer, maar voordat je het gebruikt, is het essentieel om het op de Jade te controleren om te bevestigen dat het eigenlijk bij onze Wallet hoort. Klik hiervoor op de knop "*Verify on device*".


![JADE-PLUS-GREEN](assets/fr/36.webp)


Controleer op de Jade dat de Address hetzelfde is als op Green en klik dan op de knop om te bevestigen.


![JADE-PLUS-GREEN](assets/fr/37.webp)


Je kunt nu de Address delen met de betaler om bitcoins te ontvangen in je Wallet. Wanneer de transactie wordt uitgezonden op het netwerk, verschijnt deze in jouw Wallet. Wacht tot je genoeg bevestigingen hebt ontvangen om de transactie als definitief te beschouwen.


![JADE-PLUS-GREEN](assets/fr/38.webp)


## Bitcoins versturen


Met bitcoins in je Wallet kun je nu ook bitcoins versturen. Klik op "*Versturen*".


![JADE-PLUS-GREEN](assets/fr/39.webp)


Voer op de volgende pagina de Address van de ontvanger in. Je kunt het handmatig invoeren of een QR-code scannen.


![JADE-PLUS-GREEN](assets/fr/40.webp)


Kies het betalingsbedrag.


![JADE-PLUS-GREEN](assets/fr/41.webp)


Onderaan het scherm kun je het tarief voor deze transactie selecteren. Je hebt de keuze om de aanbevelingen van de applicatie te volgen of je eigen kosten aan te passen. Hoe hoger de vergoeding in verhouding tot andere lopende transacties, hoe sneller uw transactie wordt verwerkt. Voor informatie over de kostenmarkt, ga naar [Mempool.space] (https://Mempool.space/) in het gedeelte "*Transactiekosten*".


![JADE-PLUS-GREEN](assets/fr/42.webp)


Klik op "*Volgende*" om naar het overzichtsscherm van de transactie te gaan. Controleer of Address, het bedrag en de kosten correct zijn.


![JADE-PLUS-GREEN](assets/fr/43.webp)


Als alles goed gaat, schuif je de Green knop onderaan het scherm naar rechts om de transactie te ondertekenen en uit te zenden op het Bitcoin netwerk.


![JADE-PLUS-GREEN](assets/fr/44.webp)


Je wordt nu gevraagd om de transactie op de Jade te bevestigen.


![JADE-PLUS-GREEN](assets/fr/45.webp)


Controleer of de Address van de ontvanger correct is. Klik op het vinkje om te bevestigen.


![JADE-PLUS-GREEN](assets/fr/46.webp)


Controleer of het bedrag correct is en valideer vervolgens.


![JADE-PLUS-GREEN](assets/fr/47.webp)


Je transactie is ondertekend en uitgezonden vanaf Green.


![JADE-PLUS-GREEN](assets/fr/48.webp)


Gefeliciteerd, je weet nu hoe je de Jade Plus kunt instellen en gebruiken met de Blockstream Green mobiele applicatie, via Bluetooth verbinding. Als je deze tutorial nuttig vond, zou ik je dankbaar zijn als je hieronder een Green duim achterlaat. Voel je vrij om dit artikel te delen op je sociale netwerken. Bedankt voor het delen!


Om nog een stapje verder te gaan, raad ik je deze tutorial over de Jade Plus aan, waarin we hem configureren met Sparrow wallet software in QR-modus. Je leert ook hoe je de geavanceerde instellingen van je Hardware Wallet kunt gebruiken:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

