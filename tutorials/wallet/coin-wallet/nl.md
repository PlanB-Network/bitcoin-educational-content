---
name: Coin Wallet
description: Leerprogramma over Coin Wallet en manieren om privacy en veiligheid te verbeteren
---

![cover](assets/cover.webp)


Deze tutorial behandelt [Coin Wallet](https://coin.space/) - een zelf-custodiale crypto wallet voor mobiele apparaten, en hoe je de veiligheid en privacy kunt verhogen bij het gebruik van mobiele wallet apps.



## Over Coin Wallet


**Coin Wallet** is een open-source wallet die zelf wordt gemaakt / niet zelf wordt gemaakt, gemaakt door een team van Bitcoin enthousiastelingen in 2015. Het begon als een webapplicatie, gevolgd door de iOS app in 2017, en de Android app in 2020 - beschikbaar op Google Play, Samsung Galaxy Store, en Huawei AppGallery.


Belangrijkste voordelen:


- Niet-vrijheidsberovende architectuur
- Volledig [open-source code](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Eenvoudig en strak ontwerp
- Gericht op het hoofddoel - cryptocurrency veilig opslaan, zonder onnodige functies
- Ondersteuning voor meerdere platforms: mobiel (iOS & Android), desktop, web
- RBF (Replace-By-Fee) ondersteuning - versnelt vastgelopen transacties op elk moment
- Hardware 2FA met [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2 sleutel
- Ingebouwde Tor-ondersteuning - routeer al het verkeer via het Tor-netwerk voor maximale privacy



## 1️⃣ Coin installeren Wallet

Coin Wallet is beschikbaar op alle belangrijke platforms.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Alle release-links](https://github.com/CoinSpace/CoinSpace/releases)


Ook beschikbaar voor desktop (Windows, Linux, macOS), als webapp en via Tor.


![image](assets/en/01.webp)


## 2️⃣ Een Wallet aanmaken en de PIN instellen


Een wallet wordt gemaakt met behulp van een passphrase - een willekeurige reeks van 12 woorden gescheiden door spaties, gegenereerd uit een [lijst van 2048 woorden](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin Wallet ondersteunt 12, 15, 18, 21 of 24-woord wachtzinnen geïmporteerd van andere portemonnees.


De passphrase is de door mensen leesbare vorm van de master private key. Deze moet veilig worden opgeslagen. De passphrase is alles wat nodig is om toegang te krijgen tot de wallet of deze te herstellen. Als de passphrase verloren gaat, zijn de wallet en alle fondsen permanent verloren. De passphrase mag nooit gedeeld worden. Coin Wallet slaat geen sleutels op een server of database op.


**Is een passphrase van 12 woorden veilig?

Met 2048 mogelijke woorden per positie zijn er 2048¹² ≈ 10³⁹ combinaties - wat ~128 bits aan beveiliging oplevert, vergelijkbaar met Bitcoin privésleutels. Dit niveau wordt algemeen als voldoende beschouwd.


![image](assets/en/02.webp)


Nadat de passphrase is opgeschreven en bevestigd, vraagt de app om een **4-cijferige PIN** in te stellen voor dagelijkse toegang. Voor extra gemak kun je biometrische verificatie inschakelen (vingerafdruk of gezichtsherkenning) in plaats van een PIN-code te gebruiken.


![image](assets/en/03.webp)



Er is geen account, geen sleutelherstel, geen passphrase reset en geen terugdraaien van transacties. Beveiliging is de volledige verantwoordelijkheid van de gebruiker.


Voor gedetailleerde best practices voor het opslaan van de mnemonische zin:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Passphrase + PIN. Wanneer en hoe ze worden gebruikt


**Wanneer is de passphrase vereist?

Alleen in deze zeldzame gevallen:


- De wallet instellen op een nieuw apparaat
- De Coin Wallet app opnieuw installeren
- De app-/browsergegevens wissen (lokale opslag)
- Een hardwaresleutel uit de account verwijderen
- Drie keer de verkeerde PIN-code invoeren (de app vergrendelt voor de veiligheid)


Bij dagelijks gebruik is de 4-cijferige pincode voldoende om de wallet te ontgrendelen.


**Passphrase + PIN: zo werkt het**

De passphrase is de echte master private key en werkt op elk apparaat.

Omdat elke keer 12-24 woorden typen onhandig zou zijn, gebruikt Coin Wallet een 4-cijferige PIN voor snelle, dagelijkse toegang op het huidige apparaat.

Een eenvoudige PIN alleen is niet veilig genoeg om de hoofdsleutel direct te beschermen, dus wordt deze nooit gebruikt voor encryptie. In plaats daarvan:



- De PIN wordt naar de server gestuurd en uitgewisseld voor een lange cryptografische token.
- Deze token ontcijfert de versleutelde hoofdsleutel die alleen op het apparaat is opgeslagen.


Als de PIN drie keer verkeerd wordt ingevoerd, verwijdert de server permanent de token. De lokaal opgeslagen sleutel wordt onbruikbaar. De lokaal opgeslagen sleutel wordt onbruikbaar en de enige manier om de wallet te herstellen is door de originele passphrase in te voeren.

Dit ontwerp biedt zowel gemak als een sterke fallback bescherming.



## 4️⃣ ₿itcoin ontvangen - Address types en privacy


Coin Wallet ondersteunt alle drie de Bitcoin adresformaten:



- Native SegWit (Bech32)** - begint met **bc1q** - laagste tarieven, aanbevolen
- Geneste SegWit (P2SH)** - begint met **3**
- Legacy (P2PKH)** - begint met **1**


![image](assets/en/04.webp)


**Waarom verandert het adres na elke storting? **

Dit is opzettelijk en beschermt de privacy. Telkens wanneer munten worden ontvangen, genereert Coin Wallet automatisch een nieuw ongebruikt adres. Als hetzelfde adres zou worden hergebruikt (bijvoorbeeld voor het maandsalaris), zou iedereen gemakkelijk alle binnenkomende transacties kunnen optellen op een blockchainverkenner en het totale inkomen weten.


Oude adressen blijven altijd geldig - je kunt ze nog steeds ontvangen - maar het gebruik van steeds een nieuw adres is de beste manier om je privacy te beschermen.


**Hoe Bitcoin te ontvangen:**

1. Open de munt

2. Tik op **Ontvangen**

3. Kies het gewenste adrestype (bij voorkeur **bc1q** - `Native SegWit`)

4. Toon de QR-code of kopieer het adres en stuur het naar de betaler


**Optioneel - Mecto (voor betalingen in persoon):**

Op hetzelfde scherm Ontvangst staat een knop `Mecto`.

Wanneer je het inschakelt:


- Je wordt gevraagd om een **nickname** (gravatar) in te voeren
- Je huidige locatie + ontvangstadres worden tijdelijk gedeeld met andere Coin Wallet gebruikers die ook Mecto hebben ingeschakeld
- Ze kunnen je ontdekken op een kleine kaart en munten sturen zonder te typen of te scannen


Gegevens zijn alleen zichtbaar voor andere Mecto-gebruikers en worden automatisch na 1 uur verwijderd (of onmiddellijk wanneer je het uitschakelt).

Mecto is volledig optioneel - laat het uit als je de voorkeur geeft aan maximale privacy.


![image](assets/en/05.webp)


## 5️⃣ ₿itcoin verzenden


Bitcoin verzenden:


1. Open de munt → tik op **Verstuur**

2. Plak het adres of scan de QR-code

3. Voer bedrag in (of tik op **Max**)

4. Kies transactiesnelheid:


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5. Bevestig met je 4-cijferige PIN → transactie is uitgezonden


### Hoe een hangende ₿itcoin-transactie versnellen (RBF)


Als je een langzame vergoeding hebt gekozen en de transactie blijft steken:


1. Ga naar het tabblad **Geschiedenis**

2. Tik op de lopende transactie

3. Tik **Versnellen** (vervangen tegen betaling)

4. Bevestigen → de transactie wordt opnieuw verzonden met een hogere vergoeding


RBF versnelling wordt momenteel ondersteund voor:

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


Meer over Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Privé sleutels exporteren


**Wanneer heb je eigenlijk een privésleutel nodig?

(99% van de gebruikers doet dit nooit - het 12-woord passphrase is genoeg)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Hoe privésleutels exporteren in Coin Wallet


1. Open **Bitcoin (BTC)**

2. Scroll naar de onderkant van de pagina - tik op **Privésleutels exporteren**

3. De app toont elk adres met saldo + zijn privésleutel in **WIF**-formaat (begint met 5, K of L) en een QR-code.


Alleen niet-lege adressen worden weergegeven.


**Voorbeeld WIF-sleutel**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Wat nu te doen (aanbevolen)**


- Open Electrum, Sparrow, BlueWallet of elke hardware wallet
- Particuliere sleutel importeren/verwijderen
- Alle fondsen verhuizen direct naar een nieuw beveiligd adres onder je huidige seed


Sla de privésleutel nooit digitaal op in platte tekst. Na het vegen kan deze veilig worden verwijderd.


Voor een complete gids over privésleutels en afleidingspaden: [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Technische details - BIP39, BIP32 en afleidingstrajecten


Coin Wallet volgt strikt de officiële Bitcoin standaarden die door bijna alle serieuze portemonnees worden gebruikt.


`BIP39` - hoe de passphrase de privé-hoofdsleutel wordt


- Standaard aantal woorden: 12
- Optioneel passphrase/wachtwoord: geen ("")
- Initiële entropie: 128 bits (12 woorden) → 256 bits (24 woorden)
- Open-source implementatie: https://github.com/paulmillr/scure-bip39
- Woordenlijst: standaard Engelse lijst van 2048 woorden
- Ondersteunt het importeren van 12, 15, 18, 21 en 24-woordzinnen van elke andere BIP39 wallet


`BIP32 + BIP44/BIP49/BIP84` - deterministisch genereren van alle adressen

Vanaf één hoofdsleutel kan de wallet generate miljarden adressen in een strikt gedefinieerde volgorde. Daarom zullen dezelfde 12 woorden die worden ingevoerd in Electrum, Sparrow, Trezor, Ledger, BlueWallet, enz. precies dezelfde adressen en saldi laten zien.


**Derivatiepaden gebruikt in Coin Wallet voor Bitcoin**


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

Binnen elk pad:


- `/0` - externe keten (adressen die je toont om betalingen te ontvangen)
- `/1` - interne keten (wijzig adressen die de wallet zelf gebruikt)


Omdat Coin Wallet deze publieke standaarden ongewijzigd volgt, blijft je geld terugvorderbaar in elk ander compatibel wallet, zelfs over 10-20-30 jaar.


## 8️⃣ Anonimiteit verbeteren met Tor


**Waarom Tor gebruiken in Coin Wallet**

Tor verbergt je echte IP-adres voor Bitcoin nodes, exchanges en waarnemers.

Al het verkeer (balansen, transacties, swaps) gaat via het Tor netwerk - geen directe verbindingen, geen IP lekken.

Dit is direct geïmplementeerd in de broncode van de app (zie [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet heeft een verborgen .onion adres en, sinds v6.6.3 (december 2024), **ingebouwde Tor ondersteuning direct in de mobiele app**.


### Hoe Tor inschakelen op Android en iOS


1. **Installeer Orbot** - officiële Tor Project-app (gratis)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Open Orbot → tik op Start**

Selecteer **Coin Wallet** uit de lijst zodat alleen de wallet Tor gebruikt (optioneel maar aanbevolen)

Wacht tot **"Verbonden"** staat (10-30 seconden)


3. **Open Coin Wallet → Instellingen → Netwerk**

Schakel **Gebruik Tor** in


4. **Status controleren**

Een **paars Tor onion icoon** verschijnt in de bovenste balk → al het verkeer wordt nu door Tor geleid


![image](assets/en/06.webp)


Dat is het - je mobiele Coin Wallet is volledig anoniem.


Geniet van privé cryptobeheer!


## conclusie


[Coin Wallet](https://coin.space/) - een van de echte Bitcoin wallet pioniers met een ontwikkelingsgeschiedenis van 10 jaar.

Het is bewust eenvoudig en blijft gefocust op zijn kerntaak: het veilig opslaan van je cryptocurrency.

Er is geen reclame, geen nieuwsfeed, geen abonnementen, geen sociale functies, geen afleidingen - gewoon een schone, snelle, zelfbehoudende wallet die precies doet wat het moet doen.

Coin Bij Wallet komen eenvoud en veiligheid op de eerste plaats - altijd al geweest, zal altijd zo blijven.


## hulpbronnen


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39