---
name: Cake Wallet
description: Tutorial over Cake Wallet en Stille Betalingen
---

![cover](assets/cover.webp)


Deze gids verkent [**Cake Wallet**](https://cakewallet.com/): een open-source, niet-custodial, privacy-gerichte multi-valuta wallet beschikbaar voor Android, iOS, macOS, Linux en Windows. We duiken in de Bitcoin-specifieke privacyfuncties, doorlopen het verzenden/ontvangen van Bitcoin via **Silent Payments** (een verbeterd on-chain privacyprotocol) en bekijken de implementatie van PayJoin v2 voor asynchrone transacties.


## belangrijkste kenmerken



- [**Silent Payments (BIP-352)**](https://bips.dev/352/) verbetert de vorige [BIP 47 betaalcodes](https://silentpayments.xyz/docs/comparing-proposals/bip47/) ook wel "PayNyms" genoemd, met herbruikbare geheime adressen. Wanneer een verzender jouw Stille Betaling adres gebruikt, leidt zijn wallet een uniek eenmalig adres af met behulp van verschillende sleutels die gecombineerd worden tot een uniek eenmalig Taproot adres. De blockchain records tonen niet-gerelateerde transacties, waardoor inkomende betalingen niet gelinkt kunnen worden. Stille Betalingen bieden een reeks voordelen, waaronder:
    - Herbruikbare adressen: Je hoeft niet voor elke transactie een nieuw generate adres in te voeren, wat zorgt voor een betere gebruikerservaring en meer privacy
    - Geen kostenstijging: Stille betalingen verhogen de omvang of de kosten van transacties niet.
    - Verbeterde anonimiteit: Externe waarnemers kunnen transacties niet koppelen aan een Silent Payment-adres.
    - Geen interactie tussen zender en ontvanger vereist: Transacties kunnen worden uitgevoerd zonder enige communicatie tussen de partijen.
    - Unieke adressen voor elke betaling: Elimineert het risico van onbedoeld hergebruik van adressen.
    - Geen server nodig: Silent Payments kunnen worden uitgevoerd zonder dat er een speciale server nodig is.
- PayJoin v2** beperkt de analyse van transactiegrafieken door de invoer van verzenders en ontvangers samen te voegen in een enkele transactie. Cake Wallet implementeert twee cruciale verbeteringen:
    - Asynchrone transacties**: Verzender en ontvanger hoeven niet langer tegelijkertijd online te zijn om een privétransactie te voltooien.
    - Serverloze communicatie**: Geen van beide partijen hoeft een Payjoin-server te draaien, wat een grote technische barrière wegneemt.
- Coin Controle** maakt handmatige UTXO selectie mogelijk tijdens transacties. Dit voorkomt het per ongeluk koppelen van adressen bij het uitgeven van meerdere UTXO's met verschillende oorsprong.
- Ondersteuning voor TOR**, zodat gebruikers hun netwerkverkeer door het Tor-netwerk kunnen leiden
- Met RBF** (Replace-By.Fee) kun je de vergoeding aanpassen na het verzenden van een transactie.


## 1️⃣ Uw Wallet instellen


Cake Wallet biedt een breed scala aan platformondersteuning. Je kunt kiezen uit `Android`, `iOS / macOS` , `Linux` en `Windows`.  Ga om te beginnen naar https://docs.cakewallet.com/get-started/ en selecteer je besturingssysteem.


![image](assets/en/01.webp)


Stel na de installatie een `PIN` in (4 of 6 cijfers). Je ziet dan:


1. `Maak een nieuwe Wallet` (voor nieuwe gebruikers)

2. gW-19 herstellen` (voor bestaande portemonnees)


![image](assets/en/02.webp)


Op het volgende scherm kun je kiezen uit een groot aantal cryptocurrencies. Selecteer `Bitcoin` en tik op `Volgende` en geef een `Wallet naam` op om de wallet te identificeren. Door op `Geavanceerde instellingen` te tikken, verschijnt er een reeks `Privacyinstellingen`. Breng deze wijzigingen aan:



- Fiat API:** selecteer `Tor Only` (routeert prijsaanvragen via Tor)
- Swap:** selecteer `Tor Only` (anonimiseert uitwisselingsverkeer)


BIP-39 seed type wordt standaard gegenereerd, met een optie om te veranderen naar Electrum seed type. De afleidingspaden zijn de volgende:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Als je een extra beveiligingslaag wilt toevoegen, kun je een `passphrase` instellen.  Het belangrijkste doel van een passphrase is om extra bescherming te bieden tegen fysieke aanvallen. Zelfs als een aanvaller de seed zin vindt, heeft hij geen toegang tot je wallet zonder de juiste passphrase. Met andere woorden, de seed frase alleen vertegenwoordigt één wallet, terwijl de seed frase plus passphrase een geheel andere wallet creëert zonder verbinding met het origineel. Deze eigenschap maakt ook `geheime portemonnees` mogelijk, beschermd door de passphrase, en geeft je aannemelijke ontkenbaarheid. In een dwangsituatie kun je de seed zin onthullen, terwijl je grotere bezittingen veilig houdt in de passphrase beschermde wallet.


Als je al je eigen node draait, schakel dan `Add New Custom Node` in en geef je `Node Address` om transacties en blokken binnen je eigen infrastructuur te valideren. Zodra je klaar bent, tik je op `Doorgaan` en `Volgende` om je wallet aan te maken.


![image](assets/en/03.webp)


Op het volgende scherm krijg je een disclaimer:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Om te leren hoe u uw geheugensteunzin het beste kunt opslaan, kunt u deze tutorial raadplegen:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Tik op `Ik begrijp het. Toon me mijn seed` en bewaar deze woorden op een veilige plaats! Tik dan op `Verifieer seed` en na verificatie op `Open Wallet`.


## 2️⃣ Instellingen


Voordat we dieper duiken, kijken we eerst naar het `Home Screen` en `Settings`.


Op het beginscherm zien we verschillende items weergegeven:



- het `Hamburger menu` brengt ons naar de `instellingen`
- Beschikbaar Saldo
- Silent Payments Card om te beginnen met het scannen van transacties die naar uw Silent Payment-adres zijn verzonden
- Payjoin-kaart om Payjoin in te schakelen als privacybeschermende en kostenbesparende functie
- onderaan staan snelkoppelingen naar `Wallet Overzicht`, `Ontvangen`, `Wisselen` tussen Bitcoin en andere valuta, `Versturen` en `Kopen`


![image](assets/en/11.webp)


Als je op het pictogram `Hamburger menu` tikt, wordt het instellingenmenu geopend. Laten we de opties bekijken.


![image](assets/en/05.webp)


### A - Verbinding & synchronisatie 🔗


Hier kunnen we de wallet opnieuw verbinden, knooppunten beheren en verbinding maken met ons eigen knooppunt (aanbevolen). Met `Silent Payments Scanning` kunnen we het scannen aanpassen door `Scan from block height` of `Scan from date` op te geven.


![image](assets/en/06.webp)


Als `Alpha` functie is er ook de optie om `Ingebouwde Tor` in te schakelen om verkeer door het Tor netwerk te leiden.


### B - Instellingen voor stille betalingen 🔈


We kunnen de Stille Betalingen kaart op het Beginscherm aanzetten om deze functie weer te geven. Door `Altijd scannen` in te schakelen, kan wallet de blockchain continu controleren op inkomende Stille Betalingen. We kunnen scanparameters specificeren om het scanproces aan te passen aan onze behoeften, zoals hierboven beschreven.


![image](assets/en/07.webp)


### C - Beveiliging en back-up 🗝️


Om onze wallet te beveiligen, kunnen we een back-up maken door de aanwijzingen in de app te volgen. Dit zorgt ervoor dat we een veilige kopie van onze privésleutels hebben, zodat we onze wallet kunnen terugvinden als hij verloren of gestolen is. Daarnaast kunnen we onze seed zinsdeel en privésleutels bekijken, onze PIN wijzigen, biometrische verificatie inschakelen, ondertekenen/verifiëren en 2FA instellen voor een extra beschermingslaag.


![image](assets/en/08.webp)


**Noot**: Vanaf september 2025 is het vereist dat vingerafdrukbiometrische verificatie op Android-apparaten werkt met ten minste een klasse 2 biometrische implementatie, zie voor meer informatie [hier](https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Deze vereiste kan echter in de toekomst veranderen.


### D - Privacy-instellingen 🔒


We kunnen ook de veiligheid van onze wallet verbeteren door Tor te gebruiken om onze internetverbinding te versleutelen en onze privacy te beschermen bij toegang tot externe bronnen. Daarnaast kunnen we screenshots voorkomen om onze wallet informatie vertrouwelijk te houden, automatisch gegenereerde adressen inschakelen om bij elke transactie nieuwe adressen aan te maken, en koop/verkoop acties uitschakelen om ongeautoriseerde transacties te voorkomen. Verder kunnen we PayJoin` inschakelen, een andere privacyfunctie die we later zullen bespreken.


![image](assets/en/09.webp)


### E - Overige instellingen 🔧


Met andere instellingen kunnen we de kostenprioriteit beheren en het standaardkostenniveau voor onze transacties instellen. Hierdoor kunnen we de transactiekosten voor onze Stille Betalingen beheren, rekening houdend met het huidige netwerkgebruik.


![image](assets/en/10.webp)


## 3️⃣ ₿itcoin ontvangen met Silent Payments


Er zijn verschillende opties en adrestypes beschikbaar voor het ontvangen van Bitcoin. `Segwit (P2WPKH)` *(beginnend met bc1q....)* is de standaard optie.  Laten we in dit voorbeeld `Silent Payments` selecteren.


Om een Stille Betaling te ontvangen, tik je eerst op het pictogram `Ontvangen` in Cake Wallet. Voer vervolgens het bedrag in dat je verwacht te ontvangen. Om het type adres te specificeren, tikt u nogmaals op `Ontvangen` bovenaan het scherm, en selecteert u vervolgens `Stille Betalingen` uit de opties.


Op het hoofdscherm worden de QR-code en het adres van je herbruikbare Silent Payment weergegeven. Zoals verwacht is het adres vrij lang:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Gebruik nu een BIP-352 compatibele wallet (zoals Blue Wallet) om deze QR-code te scannen en de betaling te verzenden. Je zult zien dat de wallet een uniek bestemmingsadres afleidt van jouw stille adres.


![image](assets/en/13.webp)


## 4️⃣ ₿itcoin verzenden met Silent Payments


Omdat Blue Wallet alleen Stille Betalingen kan `Versturen`, gebruiken we een andere BIP 352 compatibele wallet als ontvangende partij. Dit proces is identiek aan dat van een gewone Bitcoin transactie.



- Tik op `Versturen` op het Beginscherm
- of je plakt ons herbruikbare `sp1qq...` adres of scant de QR code direct in de app.
- Selecteer hoeveel je wilt uitgeven van je beschikbare saldo
- Tik op `Verstuur` onderaan het scherm om de transactie te bevestigen


Zodra we het `sp1qq...` adres hebben ingevoerd, leidt de wallet automatisch op de achtergrond een corresponderend `bc1p...` Taproot adres (P2TR) af, dat zal worden gebruikt voor de Stille Betaling.


We kunnen optioneel een interne notitie schrijven voor elke transactie, de tariefinstellingen aanpassen of bepaalde UTXO's selecteren voor de transactie met behulp van de `Coin Control` functie.


![image](assets/en/14.webp)


veeg naar rechts om de transactie te bevestigen.


Nadat je de transactie hebt verzonden, wordt je gevraagd of je deze contactpersoon wilt toevoegen aan je adresboek.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Laten we eens kijken waar PayJoin over gaat (https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


payjoin v2 is een privacybeschermende en kostenbesparende functie in Bitcoin die de verzender en ontvanger van een transactie laat samenwerken om een enkele transactie te creëren. Deze transactie heeft zowel input van de verzender als van de ontvanger, waardoor de meest gebruikte bewakingstechnieken tegen Bitcoin doorbroken worden en er in sommige omstandigheden ook beter geschaald kan worden en kosten bespaard kunnen worden._


Om meer te leren over PayJoin kun je ook de volgende tutorial bezoeken.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Om PayJoin te gebruiken, hebben beide partijen een wallet nodig die compatibel is met PayJoin, en de ontvanger moet minstens één munt of uitgang in zijn wallet hebben. Volg deze stappen om te beginnen:


1. Tik op het `Hamburger Menu` en tik op de knop `Privacy`

2. Schakel de optie `Gebruik Payjoin` in

3.  Tik op `Ontvangen` op het beginscherm en je krijgt een PayJoin QR Code en een kopieer knop (wanneer Segwit geselecteerd is)


![image](assets/en/16.webp)


## 6️⃣ Overige functies


Er zijn verschillende andere functies zoals Multi currency `Swaps`, `Koop en Verkoop` opties met verschillende verkopers connecties en Cake specifieke programma's zoals `Cake Pay`, waarmee je prepaid kaarten of cadeaubonnen kunt kopen.


![image](assets/en/17.webp)


## conclusie


Dit is onze review van Cake Wallet, die praktische Bitcoin privacy biedt dankzij functies als Silent Payments (BIP-352) en Payjoin v2.


Silent Payments vervangen wegwerpadressen door herbruikbare stealth-adressen om de on-chain koppeling van inkomende transacties te voorkomen. Hoewel de synchronisatieproblemen van vorige versies aanzienlijk zijn verbeterd, zijn er enkele verhoogde computationele vereisten voor het scannen en detecteren van Silent Payments vereist, die meer bronnen en bandbreedte vereisen.


Payjoin v2 doorbreekt de ketenanalyse door de input van zender en ontvanger samen te voegen tot één transactie zonder extra kosten of centrale coördinatie. Dit doorbreekt de gangbare heuristiek van input-eigendom, wat een belangrijk voordeel is omdat het betekent dat je er niet van uit kunt gaan dat alle inputs aan de verzender toebehoren.


Voor gebruikers die financiële anonimiteit belangrijk vinden, is Cake Wallet een haalbare optie. Het integreert privacy protocollen direct in de kernfunctionaliteit, waardoor ze toegankelijk zijn zonder enige technische complexiteit. Naarmate het toezicht op publieke blockchains toeneemt, helpen tools als deze de transactieprivacy te behouden waar dat het belangrijkst is. Een bredere implementatie van deze standaarden binnen het wallet landschap zou een welkome ontwikkeling zijn.


## hulpbronnen


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/