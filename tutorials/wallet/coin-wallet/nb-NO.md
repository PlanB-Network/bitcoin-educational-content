---
name: Coin Wallet
description: Opplæring om Coin Wallet og måter å forbedre personvern og sikkerhet på
---

![cover](assets/cover.webp)


Denne opplæringen dekker [Coin Wallet](https://coin.space/) - en selvforvaltende krypto-wallet for mobile enheter, og hvordan du kan øke sikkerheten og personvernet ved bruk av mobile wallet-apper.



## Om Coin Wallet


**Coin Wallet** er en wallet med åpen kildekode som er selvfengslet / ikke-fengslet, opprettet av et team av Bitcoin-entusiaster i 2015. Den startet som en webapplikasjon, etterfulgt av iOS-appen i 2017 og Android-appen i 2020 - tilgjengelig på Google Play, Samsung Galaxy Store og Huawei AppGallery.


Viktige fordeler:


- Ikke-frihetsberøvende arkitektur
- Fullstendig [åpen kildekode](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Enkel og ren design
- Fokusert på kjerneformålet - sikker lagring av kryptovaluta, uten unødvendige funksjoner
- Støtte på tvers av plattformer: mobil (iOS og Android), desktop, web
- Støtte for RBF (Replace-By-Fee) - fremskynde fastlåste transaksjoner når som helst
- Maskinvare 2FA med [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2-nøkkel
- Innebygd Tor-støtte - diriger all trafikk gjennom Tor-nettverket for maksimalt personvern



## 1️⃣ Installering av Coin Wallet

Coin Wallet er tilgjengelig på alle større plattformer.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Alle utgivelseslenker](https://github.com/CoinSpace/CoinSpace/releases)


Også tilgjengelig for PC (Windows, Linux, macOS), som en webapp og via Tor.


![image](assets/en/01.webp)


## 2️⃣ Opprette en Wallet og angi PIN-kode


En wallet opprettes ved hjelp av en passphrase - en tilfeldig sekvens med 12 ord atskilt med mellomrom, generert fra en [liste med 2048 ord](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin Wallet støtter passordfraser på 12, 15, 18, 21 eller 24 ord som importeres fra andre lommebøker.


passphrase er den menneskelesbare formen av den private hovednøkkelen. Den må lagres på en sikker måte. passphrase er alt som trengs for å få tilgang til eller gjenopprette wallet. Hvis passphrase går tapt, er wallet og alle midler tapt for alltid. passphrase må aldri deles. Coin Wallet lagrer ikke nøkler på noen server eller database.


**Er en passphrase på 12 ord sikker?

Med 2048 mulige ord per posisjon er det 2048¹² ≈ 10³⁹ kombinasjoner - noe som gir ~128 bits sikkerhet, som kan sammenlignes med Bitcoin private nøkler. Dette nivået anses generelt som tilstrekkelig.


![image](assets/en/02.webp)


Etter at passphrase er skrevet ned og bekreftet, ber appen deg om å angi en **4-sifret PIN-kode** for daglig tilgang. For ekstra bekvemmelighet kan du aktivere biometrisk autentisering (fingeravtrykk eller ansiktsgjenkjenning) i stedet for å bruke en PIN-kode.


![image](assets/en/03.webp)



Det finnes ingen konto, ingen nøkkelgjenoppretting, ingen tilbakestilling av passphrase og ingen reversering av transaksjoner. Brukeren har det fulle ansvaret for sikkerheten.


For detaljert informasjon om beste praksis for lagring av minnefrasen:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Passord + PIN-kode. Når og hvordan de brukes


**Når er passphrase påkrevd?

Bare i disse sjeldne tilfellene:


- Konfigurere wallet på en ny enhet
- Installere Coin Wallet-appen på nytt
- Tømme app-/nettleserdata (lokal lagring)
- Fjerne en maskinvarenøkkel fra kontoen
- Tast inn feil PIN-kode tre ganger (appen låses av sikkerhetshensyn)


I daglig bruk er den firesifrede PIN-koden tilstrekkelig for å låse opp wallet.


**Passord + PIN-kode: Slik fungerer det**

passphrase er den ekte private hovednøkkelen og fungerer på alle enheter.

Siden det er upraktisk å skrive 12-24 ord hver gang, bruker Coin Wallet en firesifret PIN-kode for rask, daglig tilgang på den aktuelle enheten.

En enkel PIN-kode alene er ikke sikker nok til å beskytte hovednøkkelen direkte, så den brukes aldri til kryptering. Den brukes i stedet:



- PIN-koden sendes til serveren og byttes mot en lang kryptografisk token.
- Denne token dekrypterer den krypterte hovednøkkelen som kun er lagret på enheten.


Hvis PIN-koden tastes inn feil tre ganger, sletter serveren token permanent. Den lokalt lagrede nøkkelen blir ubrukelig, og den eneste måten å gjenopprette wallet på er ved å taste inn den opprinnelige passphrase.

Denne utformingen gir både bekvemmelighet og sterk reservebeskyttelse.



## 4️⃣ Mottak av bitcoin - Address-typer og personvern


Coin Wallet støtter alle de tre Bitcoin-adresseformatene:



- Native SegWit (Bech32)** - starter med **bc1q** - laveste avgifter, anbefales
- Nestede SegWit (P2SH)** - begynner med **3**
- Legacy (P2PKH)** - begynner med **1**


![image](assets/en/04.webp)


**Hvorfor endres adressen etter hvert innskudd?

Dette er tilsiktet og beskytter personvernet. Hver gang mynter mottas, genererer Coin Wallet automatisk en ny ubrukt adresse. Hvis den samme adressen ble gjenbrukt (for eksempel for månedslønn), kunne hvem som helst enkelt summere opp alle innkommende transaksjoner på en blockchain explorer og vite den totale inntekten.


Gamle adresser forblir gyldige for alltid - du kan fortsatt motta til dem - men det er anbefalt å bruke en ny adresse hver gang.


**Hvordan du mottar Bitcoin:**

1. Åpne mynten

2. Trykk på **Mottak**

3. Velg ønsket adressetype (fortrinnsvis **bc1q** - `Native SegWit`)

4. Vis QR-koden eller kopier adressen og send den til betaleren


**Valgfritt - Mecto (for personlig betaling):**

På samme mottaksskjermbilde er det en "Mecto"-knapp.

Når du slår den på:


- Du vil bli bedt om å oppgi et **nickname** (gravatar)
- Din nåværende posisjon + mottaksadresse deles midlertidig med andre Coin Wallet-brukere som også har Mecto aktivert
- De kan finne deg på et lite kart og sende mynter uten å skrive eller skanne


Dataene er kun synlige for andre Mecto-brukere og slettes automatisk etter én time (eller umiddelbart når du slår den av).

Mecto er helt valgfritt - la det være av hvis du foretrekker maksimalt privatliv.


![image](assets/en/05.webp)


## 5️⃣ Sende ₿itcoin


For å sende Bitcoin:


1. Åpne mynten → trykk på **Send**

2. Lim inn adressen eller skann QR-koden

3. Angi beløp (eller trykk på **Max**)

4. Velg transaksjonshastighet:


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5. Bekreft med din firesifrede PIN-kode → transaksjonen sendes


### Slik fremskynder du en ventende ₿itcoin-transaksjon (RBF)


Hvis du velger et tregt gebyr og transaksjonen blir stående fast:


1. Gå til fanen **Historikk**

2. Trykk på den ventende transaksjonen

3. Trykk på **Accelerate** (Erstatt mot avgift)

4. Bekreft → transaksjonen vil bli sendt på nytt med et høyere gebyr


RBF-akselerasjon støttes for øyeblikket for:

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


Mer om Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Eksportere private nøkler


**Når trenger du egentlig en privat nøkkel?

(99 % av brukerne gjør det aldri - det er nok med 12 ord i passphrase)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Slik eksporterer du private nøkler i Coin Wallet


1. Åpen **Bitcoin (BTC)**

2. Bla til bunnen av siden - trykk på **Eksporter private nøkler**

3. Appen viser hver adresse med saldo + den private nøkkelen i **WIF**-format (starter med 5, K eller L) og en QR-kode.


Bare ikke-tomme adresser vises.


**Eksempel på WIF-nøkkel**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Hva du bør gjøre videre (anbefalt)**


- Åpne Electrum, Sparrow, BlueWallet eller hvilken som helst maskinvare wallet
- Importer/sveip privat nøkkel
- Alle midler flyttes umiddelbart til en ny sikker adresse under din nåværende seed


Den private nøkkelen må aldri lagres digitalt i klartekst. Etter feiing kan den trygt slettes.


For en komplett veiledning om private nøkler og avledningsstier: [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Tekniske detaljer - BIP39, BIP32 og avledningsstier


Coin Wallet følger strengt de offisielle Bitcoin-standardene som brukes av nesten alle seriøse lommebøker.


`BIP39` - hvordan passphrase blir den private hovednøkkelen


- Standard antall ord: 12
- Valgfritt passphrase/passord: ingen ("")
- Opprinnelig entropi: 128 bits (12 ord) → 256 bits (24 ord)
- Implementering med åpen kildekode: https://github.com/paulmillr/scure-bip39
- Ordliste: standard engelsk ordliste med 2048 ord
- Støtter import av fraser på 12, 15, 18, 21 og 24 ord fra en hvilken som helst annen BIP39 wallet


`BIP32 + BIP44/BIP49/BIP84` - deterministisk generering av alle adresser

Fra én hovednøkkel kan wallet generate milliarder av adresser i en strengt definert rekkefølge. Dette er grunnen til at de samme 12 ordene som tastes inn i Electrum, Sparrow, Trezor, Ledger, BlueWallet osv. vil vise nøyaktig de samme adressene og saldoene.


**Avledningsveier som brukes i Coin Wallet for Bitcoin**


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

Inne i hver sti:


- `/0` - ekstern kjede (adresser du viser for å motta betalinger)
- `/1` - intern kjede (endre adresser som wallet bruker selv)


Fordi Coin Wallet følger disse offentlige standardene uten endringer, vil midlene dine fortsatt kunne gjenvinnes i en hvilken som helst annen kompatibel wallet, selv om 10-20-30 år.


## 8️⃣ Forbedre anonymiteten med Tor


**Hvorfor bruke Tor i Coin Wallet**

Tor skjuler den virkelige IP-adressen din for Bitcoin-noder, sentraler og observatører.

All trafikk (saldoer, transaksjoner, bytter) går gjennom Tor-nettverket - ingen direkte tilkoblinger, ingen IP-lekkasjer.

Dette er implementert direkte i appens kildekode (se [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet har en skjult .onion-adresse og, siden v6.6.3 (desember 2024), **innebygd Tor-støtte direkte i mobilappen**.


### Slik aktiverer du Tor på Android og iOS


1. **Installer Orbot** - offisiell Tor Project-app (gratis)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Åpne Orbot → trykk på Start**

Velg **Coin Wallet** fra listen, slik at bare wallet bruker Tor (valgfritt, men anbefalt)

Vent til det står **"Connected"** (10-30 sekunder)


3. **Åpne Coin Wallet → Innstillinger → Nettverk**

Slå på **Bruk Tor**


4. **Sjekk status**

Et **lilla Tor-løkikon** vises i topplinjen → all trafikk rutes nå gjennom Tor


![image](assets/en/06.webp)


Det var det - din mobile Coin Wallet er helt anonym.


Nyt privat kryptostyring!


## 📝 Konklusjon


[Coin Wallet](https://coin.space/) - en av de virkelige Bitcoin wallet-pionerene med en 10-årig utviklingshistorie.

Den er bevisst enkel og fokuserer på kjerneoppgaven: å lagre kryptovalutaen din på en sikker måte.

Det er ingen reklame, ingen nyhetsfeed, ingen abonnementer, ingen sosiale funksjoner, ingen distraksjoner - bare en ren, rask, selvbeherskende wallet som gjør akkurat det den skal gjøre.

Coin Wallet setter enkelhet og sikkerhet først - det har den alltid gjort, og det vil den alltid gjøre.


## 📖 Ressurser


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39