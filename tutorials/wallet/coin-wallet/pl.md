---
name: Coin Wallet
description: Samouczek na temat Coin Wallet i sposobów zwiększenia prywatności i bezpieczeństwa
---

![cover](assets/cover.webp)


Ten samouczek obejmuje [Coin Wallet](https://coin.space/) - samokontrola kryptograficzna wallet dla urządzeń mobilnych oraz jak zwiększyć bezpieczeństwo i prywatność podczas korzystania z mobilnych aplikacji wallet.



## O Coin Wallet


**Coin Wallet** to samozatrzymujący się / niezatrzymujący się, open-source wallet stworzony przez zespół entuzjastów Bitcoin w 2015 roku. Zaczęło się jako aplikacja internetowa, a następnie aplikacja na iOS w 2017 roku i aplikacja na Androida w 2020 roku - dostępna w Google Play, Samsung Galaxy Store i Huawei AppGallery.


Główne zalety:


- Architektura bez nadzoru
- W pełni [kod open-source] (https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Prosta i przejrzysta konstrukcja
- Skoncentrowany na głównym celu - bezpiecznym przechowywaniu kryptowalut, bez zbędnych funkcji
- Obsługa wielu platform: mobilna (iOS i Android), stacjonarna, internetowa
- Obsługa RBF (Replace-By-Fee) - przyspiesz zablokowane transakcje w dowolnym momencie
- Sprzętowe 2FA z [YubiKey] (https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / kluczem FIDO2
- Wbudowana obsługa sieci Tor - kierowanie całego ruchu przez sieć Tor w celu zapewnienia maksymalnej prywatności



## 1️⃣ Instalacja Coin Wallet

Coin Wallet jest dostępny na wszystkich głównych platformach.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Wszystkie linki do wydania](https://github.com/CoinSpace/CoinSpace/releases)


Dostępna również na komputery stacjonarne (Windows, Linux, macOS), jako aplikacja internetowa i przez Tor.


![image](assets/en/01.webp)


## 2️⃣ Tworzenie Wallet i ustawianie kodu PIN


wallet jest tworzony przy użyciu passphrase - losowej sekwencji 12 słów oddzielonych spacjami, wygenerowanej z [listy 2048 słów] (https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin Wallet obsługuje 12-, 15-, 18-, 21- lub 24-wyrazowe hasła importowane z innych portfeli.


passphrase jest czytelną dla człowieka formą głównego klucza prywatnego. Musi być bezpiecznie przechowywany. passphrase jest wszystkim, co jest potrzebne do uzyskania dostępu lub przywrócenia wallet. Jeśli passphrase zostanie utracony, wallet i wszystkie środki zostaną trwale utracone. passphrase nie może być nigdy udostępniany. Coin Wallet nie przechowuje kluczy na żadnym serwerze ani w bazie danych.


**Czy 12-słowny passphrase jest bezpieczny?

Przy 2048 możliwych słowach na pozycję, istnieje 2048¹² ≈ 10³⁹ kombinacji - zapewniając ~128 bitów bezpieczeństwa, porównywalnych z kluczami prywatnymi Bitcoin. Poziom ten jest powszechnie uważany za wystarczający.


![image](assets/en/02.webp)


Po zapisaniu i potwierdzeniu passphrase, aplikacja poprosi o ustawienie **4-cyfrowego kodu PIN** dla codziennego dostępu. Dla większej wygody można włączyć uwierzytelnianie biometryczne (odcisk palca lub rozpoznawanie twarzy) zamiast używania kodu PIN.


![image](assets/en/03.webp)



Nie ma konta, odzyskiwania klucza, resetowania passphrase ani cofania transakcji. Pełna odpowiedzialność za bezpieczeństwo spoczywa na użytkowniku.


Szczegółowe najlepsze praktyki dotyczące zapisywania frazy mnemonicznej:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Hasło + PIN. Kiedy i jak są używane


**Kiedy wymagany jest passphrase?

Tylko w tych rzadkich przypadkach:


- Konfiguracja wallet na nowym urządzeniu
- Ponowna instalacja aplikacji Coin Wallet
- Czyszczenie danych aplikacji/przeglądarki (pamięć lokalna)
- Usuwanie klucza sprzętowego z konta
- Trzykrotne wprowadzenie błędnego kodu PIN (aplikacja blokuje się dla bezpieczeństwa)


W codziennym użytkowaniu 4-cyfrowy kod PIN jest wystarczający do odblokowania wallet.


**Passphrase + PIN: Jak to działa**

passphrase jest prawdziwym głównym kluczem prywatnym i działa na każdym urządzeniu.

Ponieważ wpisywanie 12-24 słów za każdym razem byłoby niewygodne, Coin Wallet używa 4-cyfrowego kodu PIN do szybkiego, codziennego dostępu na bieżącym urządzeniu.

Sam prosty kod PIN nie jest wystarczająco bezpieczny, aby bezpośrednio chronić klucz główny, więc nigdy nie jest używany do szyfrowania. Zamiast tego:



- PIN jest wysyłany do serwera i wymieniany na długi kryptograficzny token.
- Ten token odszyfrowuje zaszyfrowany klucz główny przechowywany tylko na urządzeniu.


Jeśli kod PIN zostanie wprowadzony nieprawidłowo trzy razy, serwer trwale usunie token. Lokalnie zapisany klucz staje się bezużyteczny, a jedynym sposobem na odzyskanie wallet jest wprowadzenie oryginalnego passphrase.

Taka konstrukcja zapewnia zarówno wygodę, jak i silną ochronę awaryjną.



## 4️⃣ Odbieranie ₿itcoin - typy Address i prywatność


Coin Wallet obsługuje wszystkie trzy formaty adresów Bitcoin:



- Natywny SegWit (Bech32)** - zaczyna się od **bc1q** - najniższe opłaty, zalecane
- Zagnieżdżony SegWit (P2SH)** - zaczyna się od **3**
- Legacy (P2PKH)** - zaczyna się od **1**


![image](assets/en/04.webp)


**Dlaczego adres zmienia się po każdej wpłacie?

Jest to celowe i chroni prywatność. Za każdym razem, gdy otrzymywane są monety, Coin Wallet automatycznie generuje nowy nieużywany adres. Gdyby ten sam adres został ponownie użyty (na przykład do miesięcznego wynagrodzenia), każdy mógłby łatwo zsumować wszystkie przychodzące transakcje w eksploratorze blockchain i poznać całkowity dochód.


Stare adresy pozostają ważne na zawsze - nadal można na nie otrzymywać wiadomości - ale używanie nowego adresu za każdym razem jest zalecaną najlepszą praktyką w zakresie prywatności.


**Jak otrzymać Bitcoin:**

1. Otwórz monetę

2. Dotknij **Odbierz**

3. Wybierz żądany typ adresu (najlepiej **bc1q** - `Native SegWit`)

4. Pokaż kod QR lub skopiuj adres i wyślij go do płatnika


**Opcjonalnie - Mecto (dla płatności osobistych):**

Na tym samym ekranie Receive znajduje się przycisk `Mecto`.

Po włączeniu:


- Zostaniesz poproszony o wprowadzenie **nickuname** (gravatar)
- Twoja bieżąca lokalizacja + adres odbiorczy są tymczasowo udostępniane innym użytkownikom Coin Wallet, którzy również mają włączoną funkcję Mecto
- Mogą odkryć cię na małej mapie i wysłać monety bez wpisywania lub skanowania


Dane są widoczne tylko dla innych użytkowników Mecto i są automatycznie usuwane po 1 godzinie (lub natychmiast po wyłączeniu).

Mecto jest całkowicie opcjonalne - pozostaw je wyłączone, jeśli wolisz maksymalną prywatność.


![image](assets/en/05.webp)


## 5️⃣ Wysyłanie ₿itcoinów


Aby wysłać Bitcoin:


1. Otwórz monetę → dotknij **Wyślij**

2. Wklej adres lub zeskanuj kod QR

3. Wprowadź kwotę (lub naciśnij **Max**)

4. Wybierz szybkość transakcji:


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5. Potwierdź 4-cyfrowym kodem PIN → transakcja jest transmitowana


### Jak przyspieszyć oczekującą transakcję ₿itcoin (RBF)


Jeśli wybrałeś powolną opłatę i transakcja utknęła:


1. Przejdź do zakładki **Historia**

2. Stuknij oczekującą transakcję

3. Dotknij **Accelerate** (Zastąp za opłatą)

4. Potwierdź → transakcja zostanie ponownie przesłana z wyższą opłatą


Akceleracja RBF jest obecnie obsługiwana dla:

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


Więcej informacji o Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Eksport kluczy prywatnych


**Kiedy tak naprawdę potrzebny jest klucz prywatny?

(99% użytkowników nigdy tego nie robi - wystarczy 12 słów passphrase)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Jak wyeksportować klucze prywatne w Coin Wallet


1. Otwarte **Bitcoin (BTC)**

2. Przewiń do dołu strony - dotknij **Eksportuj klucze prywatne**

3. Aplikacja pokazuje każdy adres z saldem + jego klucz prywatny w formacie **WIF** (zaczyna się od 5, K lub L) oraz kod QR.


Wyświetlane są tylko niepuste adresy.


**Przykładowy klucz WIF**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Co robić dalej (zalecane)**


- Otwórz Electrum, Sparrow, BlueWallet lub dowolny sprzęt wallet
- Importowanie/wymienianie klucza prywatnego
- Wszystkie środki są natychmiast przenoszone na nowy bezpieczny adres w ramach bieżącego seed


Nigdy nie przechowuj klucza prywatnego cyfrowo w postaci zwykłego tekstu. Po zamiataniu można go bezpiecznie usunąć.


Kompletny przewodnik po kluczach prywatnych i ścieżkach derywacji: [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Szczegóły techniczne - BIP39, BIP32 i ścieżki pochodne


Coin Wallet ściśle przestrzega oficjalnych standardów Bitcoin, które są używane przez prawie wszystkie poważne portfele.


`BIP39` - jak passphrase staje się głównym kluczem prywatnym


- Domyślna liczba słów: 12
- Opcjonalne passphrase/hasło: brak ("")
- Początkowa entropia: 128 bitów (12 słów) → 256 bitów (24 słowa)
- Implementacja open-source: https://github.com/paulmillr/scure-bip39
- Lista słów: standardowa angielska lista 2048 słów
- Obsługuje import 12-, 15-, 18-, 21- i 24-wyrazowych fraz z dowolnego innego urządzenia BIP39 wallet


`BIP32 + BIP44/BIP49/BIP84` - deterministyczne generowanie wszystkich adresów

Z jednego klucza głównego wallet może generate miliardy adresów w ściśle określonej kolejności. To dlatego te same 12 słów wprowadzonych do Electrum, Sparrow, Trezor, Ledger, BlueWallet itd. pokaże dokładnie te same adresy i salda.


**Ścieżki derywacyjne używane w Coin Wallet dla Bitcoin**


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

Wewnątrz każdej ścieżki:


- `/0` - łańcuch zewnętrzny (adresy wskazane do otrzymywania płatności)
- `/1` - wewnętrzny łańcuch (zmiana adresów, których używa sam wallet)


Ponieważ Coin Wallet jest zgodny z tymi publicznymi standardami bez żadnych zmian, Twoje środki pozostaną odzyskiwalne w każdym innym kompatybilnym wallet nawet za 10-20-30 lat.


## 8️⃣ Zwiększanie anonimowości za pomocą aplikacji Tor


**Dlaczego warto używać Tora w Coin Wallet**?

Tor ukrywa prawdziwy adres IP użytkownika przed węzłami Bitcoin, giełdami i obserwatorami.

Cały ruch (salda, transakcje, swapy) przechodzi przez sieć Tor - bez bezpośrednich połączeń, bez wycieków IP.

Jest to zaimplementowane bezpośrednio w kodzie źródłowym aplikacji (patrz [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet ma ukryty adres .onion i, od wersji 6.6.3 (grudzień 2024 r.), **wbudowaną obsługę Tora bezpośrednio w aplikacji mobilnej**.


### Jak włączyć Tor na Androidzie i iOS


1. **Zainstaluj Orbot** - oficjalną aplikację Tor Project (darmowa)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Otwórz Orbot → dotknij Start**

Wybierz **Coin Wallet** z listy, aby tylko wallet korzystał z sieci Tor (opcjonalne, ale zalecane)

Poczekaj, aż pojawi się komunikat **"Połączono "** (10-30 sekund)


3. **Otwórz Coin Wallet → Ustawienia → Sieć**

Włącz **Użyj Tor**


4. **Sprawdź status**

Na górnym pasku pojawia się **fioletowa ikona cebuli Tor** → cały ruch jest teraz kierowany przez Tor


![image](assets/en/06.webp)


To wszystko - Twój mobilny Coin Wallet jest w pełni anonimowy.


Ciesz się prywatnym zarządzaniem kryptowalutami!


## wnioski


[Coin Wallet](https://coin.space/) - jeden z prawdziwych pionierów Bitcoin wallet z 10-letnią historią rozwoju.

Jest celowo prosty i koncentruje się na swojej podstawowej misji: bezpiecznym przechowywaniu kryptowalut.

Nie ma reklam, kanału informacyjnego, subskrypcji, funkcji społecznościowych, żadnych rozpraszaczy - tylko czysty, szybki, samowystarczalny wallet, który robi dokładnie to, co powinien.

Coin Wallet stawia prostotę i bezpieczeństwo na pierwszym miejscu - zawsze tak było, zawsze tak będzie.


## zasoby


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39