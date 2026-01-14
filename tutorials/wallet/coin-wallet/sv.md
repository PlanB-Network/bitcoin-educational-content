---
name: Coin Wallet
description: Handledning om Coin Wallet och olika sätt att förbättra integriteten och säkerheten
---

![cover](assets/cover.webp)


Denna handledning handlar om [Coin Wallet](https://coin.space/) - ett självförvaltande krypto wallet för mobila enheter, och hur man ökar säkerheten och integriteten när man använder mobila wallet-appar.



## Om Coin Wallet


** Coin Wallet** är en wallet med öppen källkod som är frihetsberövande/icke frihetsberövande och skapades av ett team Bitcoin-entusiaster 2015. Det började som en webbapplikation, följt av iOS-appen 2017 och Android-appen 2020 - tillgänglig på Google Play, Samsung Galaxy Store och Huawei AppGallery.


Viktiga fördelar:


- Arkitektur utan frihetsberövande
- Helt och hållet [öppen källkod](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Enkel och ren design
- Fokuserad på huvudsyftet - säker förvaring av kryptovaluta, utan onödiga funktioner
- Stöd för flera plattformar: mobil (iOS & Android), dator, webb
- RBF (Replace-By-Fee)-stöd - snabba upp fastnade transaktioner när som helst
- Hårdvara 2FA med [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2-nyckel
- Inbyggt Tor-stöd - dirigera all trafik genom Tor-nätverket för maximal integritet



## 1️⃣ Installera Coin Wallet

Coin Wallet finns tillgänglig på alla större plattformar.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Alla länkar till releasen](https://github.com/CoinSpace/CoinSpace/releases)


Finns även för desktop (Windows, Linux, macOS), som webbapp och via Tor.


![image](assets/en/01.webp)


## 2️⃣ Skapa en Wallet och ange PIN-kod


En wallet skapas med hjälp av en passphrase - en slumpmässig sekvens av 12 ord åtskilda av mellanslag, genererad från en [lista med 2048 ord](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin Wallet stöder lösenfraser med 12, 15, 18, 21 eller 24 ord som importeras från andra plånböcker.


passphrase är den mänskliga läsbara formen av den privata huvudnyckeln. Den måste sparas på ett säkert sätt. passphrase är allt som behövs för att komma åt eller återställa wallet. Om passphrase går förlorad är wallet och alla medel permanent förlorade. passphrase får aldrig delas. Coin Wallet lagrar inte nycklar på någon server eller databas.


**Är en passphrase med 12 ord säker?

Med 2048 möjliga ord per position finns det 2048¹² ≈ 10³⁹ kombinationer - vilket ger ~128 bitars säkerhet, jämförbart med Bitcoin privata nycklar. Denna nivå anses allmänt vara tillräcklig.


![image](assets/en/02.webp)


Efter att passphrase har skrivits ner och bekräftats ber appen dig att ange en **4-siffrig PIN-kod** för daglig åtkomst. För extra bekvämlighet kan du aktivera biometrisk autentisering (fingeravtryck eller ansiktsigenkänning) istället för att använda en PIN-kod.


![image](assets/en/03.webp)



Det finns inget konto, ingen nyckelåterställning, ingen återställning av passphrase och ingen reversering av transaktioner. Säkerheten är användarens fulla ansvar.


För detaljerade bästa metoder för att spara den mnemotekniska frasen:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Lösenord + PIN-kod. När och hur de används


**När krävs passphrase?**

Endast i dessa sällsynta fall:


- Konfigurera wallet på en ny enhet
- Ominstallation av appen Coin Wallet
- Rensning av app-/webbläsardata (lokal lagring)
- Ta bort en hårdvarunyckel från kontot
- Ange fel PIN-kod tre gånger (appen låser sig av säkerhetsskäl)


Vid daglig användning räcker det med den 4-siffriga PIN-koden för att låsa upp wallet.


**Passphrase + PIN: Hur det fungerar**

passphrase är den verkliga privata huvudnyckeln och fungerar på alla enheter.

Eftersom det skulle vara obekvämt att skriva 12-24 ord varje gång använder Coin Wallet en fyrsiffrig PIN-kod för snabb, daglig åtkomst på den aktuella enheten.

En enkel PIN-kod är inte tillräckligt säker för att skydda huvudnyckeln direkt, så den används aldrig för kryptering. Istället används



- PIN-koden skickas till servern och byts ut mot en lång kryptografisk token.
- Denna token dekrypterar den krypterade huvudnyckeln som endast lagras på enheten.


Om PIN-koden anges felaktigt tre gånger raderar servern token permanent. Den lokalt lagrade nyckeln blir oanvändbar och det enda sättet att återställa wallet är att ange den ursprungliga passphrase.

Denna design ger både bekvämlighet och ett starkt reservskydd.



## 4️⃣ Mottagning av ₿itcoin - Address-typer och integritet


Coin Wallet stöder alla tre adressformaten i Bitcoin:



- Native SegWit (Bech32)** - börjar med **bc1q** - lägsta avgifter, rekommenderas
- Nästlade SegWit (P2SH)** - börjar med **3**
- Legacy (P2PKH)** - börjar med **1**


![image](assets/en/04.webp)


**Varför ändras adressen efter varje insättning?**

Detta är avsiktligt och skyddar integriteten. Varje gång mynt tas emot genererar Coin Wallet automatiskt en ny oanvänd adress. Om samma adress återanvänds (t.ex. för månadslön) kan vem som helst enkelt summera alla inkommande transaktioner på en blockchain explorer och få reda på den totala inkomsten.


Gamla adresser är giltiga för evigt - du kan fortfarande ta emot meddelanden till dem - men att använda en ny adress varje gång är bästa praxis när det gäller sekretess.


**Hur man tar emot Bitcoin:**

1. Öppna myntet

2. Tryck på **Mottagning**

3. Välj önskad adresstyp (företrädesvis **bc1q** - `Native SegWit`)

4. Visa QR-koden eller kopiera adressen och skicka den till betalaren


**Valfritt - Mecto (för betalningar vid personligt besök):**

På samma mottagningsskärm finns en "Mecto"-knapp.

När du slår på den:


- Du kommer att bli ombedd att ange ett **nicknamn** (gravatar)
- Din nuvarande plats + mottagningsadress delas tillfälligt med andra Coin Wallet-användare som också har Mecto aktiverat
- De kan hitta dig på en liten karta och skicka mynt utan att behöva skriva eller skanna


Data är endast synlig för andra Mecto-användare och raderas automatiskt efter 1 timme (eller omedelbart när du stänger av den).

Mecto är helt valfritt - låt det vara avstängt om du föredrar maximal integritet.


![image](assets/en/05.webp)


## 5️⃣ Skicka bitcoin


För att skicka Bitcoin:


1. Öppna myntet → tryck på **Sänd**

2. Klistra in adressen eller skanna QR-koden

3. Ange belopp (eller tryck på **Max**)

4. Välj transaktionshastighet:


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5. Bekräfta med din 4-siffriga PIN-kod → transaktionen sänds


### Hur man påskyndar en väntande ₿itcoin-transaktion (RBF)


Om du väljer en långsam avgift och transaktionen fastnar:


1. Gå till fliken **Historia**

2. Tryck på den väntande transaktionen

3. Tap **Accelerera** (Ersättning mot avgift)

4. Bekräfta → transaktionen kommer att sändas på nytt med en högre avgift


RBF-acceleration stöds för närvarande för:

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


Mer om Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Exportera privata nycklar


**När behöver man egentligen en privat nyckel?

(99 % av användarna gör aldrig det - det räcker med 12 ord i passphrase)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Så här exporterar du privata nycklar i Coin Wallet


1. Öppen **Bitcoin (BTC)**

2. Bläddra längst ner på sidan - tryck på **Exportera privata nycklar**

3. Appen visar varje adress med saldo + dess privata nyckel i **WIF**-format (börjar med 5, K eller L) och en QR-kod.


Endast adresser som inte är tomma visas.


**Exempel på WIF-nyckel**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Vad ska jag göra härnäst (rekommenderas)**


- Öppna Electrum, Sparrow, BlueWallet eller någon hårdvara wallet
- Importera/Svepa privat nyckel
- Alla medel flyttas omedelbart till en ny säker adress under din nuvarande seed


Förvara aldrig den privata nyckeln digitalt i klartext. Efter svepningen kan den raderas på ett säkert sätt.


För en komplett guide om privata nycklar och härledningsvägar: [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Tekniska detaljer - BIP39, BIP32 och härledningsvägar


Coin Wallet följer strikt de officiella Bitcoin-standarderna som används av nästan alla seriösa plånböcker.


`BIP39` - hur passphrase blir den privata huvudnyckeln


- Standard antal ord: 12
- Valfritt passphrase/lösenord: inget ("")
- Initial entropi: 128 bitar (12 ord) → 256 bitar (24 ord)
- Implementering med öppen källkod: https://github.com/paulmillr/scure-bip39
- Ordlista: standard engelsk lista med 2048 ord
- Stödjer import av fraser med 12, 15, 18, 21 och 24 ord från alla andra BIP39 wallet


`BIP32 + BIP44/BIP49/BIP84` - deterministisk generering av alla adresser

Från en huvudnyckel kan wallet generate miljontals adresser i en strikt definierad ordning. Det är därför som samma 12 ord som matas in i Electrum, Sparrow, Trezor, Ledger, BlueWallet etc. kommer att visa exakt samma adresser och saldon.


**Derivationsvägar som används i Coin Wallet för Bitcoin**


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

Inuti varje väg:


- `/0` - extern kedja (adresser du visar för att ta emot betalningar)
- `/1` - intern kedja (ändra adresser som wallet använder själv)


Eftersom Coin Wallet följer dessa offentliga standarder utan några ändringar, kommer dina medel att förbli återvinningsbara i alla andra kompatibla wallet även om 10-20-30 år.


## 8️⃣ Förbättrad anonymitet med Tor


**Varför använda Tor i Coin Wallet**

Tor döljer din riktiga IP-adress från Bitcoin-noder, utbyten och observatörer.

All trafik (saldon, transaktioner, byten) går genom Tor-nätverket - inga direktanslutningar, inga IP-läckor.

Detta implementeras direkt i appens källkod (se [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet har en dold .onion-adress och, sedan v6.6.3 (december 2024), **inbyggt Tor-stöd direkt i mobilappen**.


### Så här aktiverar du Tor på Android & iOS


1. **Installera Orbot** - officiell Tor Project-app (gratis)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Öppen Orbot → tryck på Start**

Välj **Coin Wallet** från listan så att endast wallet använder Tor (valfritt men rekommenderas)

Vänta tills det står **"Connected"** (10-30 sekunder)


3. **Öppna Coin Wallet → Inställningar → Nätverk**

Slå på **Använd Tor**


4. **Kontrollera status**

En **lila Tor-lökikon** visas i det övre fältet → all trafik dirigeras nu genom Tor


![image](assets/en/06.webp)


Det är allt - din mobil Coin Wallet är helt anonym.


Njut av privat kryptohantering!


## 📝 Slutsats


[Coin Wallet](https://coin.space/) - en av de verkliga Bitcoin wallet-pionjärerna med en 10-årig utvecklingshistoria.

Den är medvetet enkel och håller sig laserfokuserad på sitt kärnuppdrag: att säkert lagra din kryptovaluta.

Det finns ingen reklam, inget nyhetsflöde, inga prenumerationer, inga sociala funktioner, inga distraktioner - bara en ren, snabb, självförvaltande wallet som gör exakt vad den ska göra.

Coin Wallet sätter enkelhet och säkerhet i första rummet - det har vi alltid gjort och kommer alltid att göra.


## 📖 Resurser


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39