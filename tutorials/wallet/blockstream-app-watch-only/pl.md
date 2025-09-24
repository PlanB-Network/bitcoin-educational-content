---
name: Blockstream App - Watch-Only
description: Jak skonfigurować Watch-only wallet w aplikacji Blockstream?
---

![cover](assets/cover.webp)


## 1. Wprowadzenie


### 1.1 Cel samouczka





- Ten samouczek wyjaśnia, jak skonfigurować i używać funkcji **Watch-Only** aplikacji mobilnej **Blockstream App** do monitorowania Bitcoin Wallet bez dostępu do jego kluczy prywatnych.
- Obejmuje on instalację, początkową konfigurację, importowanie rozszerzonego klucza publicznego i używanie go do śledzenia sald i adresów odbiorczych generate.
- Uwaga: Inne samouczki, zawarte w dodatku, dotyczą Onchain, Liquid i wersji desktopowej.



### 1.2. Docelowi odbiorcy





- **Początkujący**: Użytkownicy chcący monitorować portfel Bitcoin (często powiązany z Hardware Wallet) za pośrednictwem intuicyjnej aplikacji mobilnej.
- **Użytkownicy średniozaawansowani**: Osoby, które chcą zarządzać portfelami tylko do odczytu, korzystając z opcji prywatności, takich jak Tor lub SPV.
- **Właściciele Hardware Wallet**: Aby sprawdzić swoje salda i adresy generate bez podłączania urządzenia.
- **Firmy i sklepy**:
 - Śledzenie transakcji do celów księgowych bez ujawniania kluczy prywatnych.
 - Weryfikacja transakcji otrzymanych bez wprowadzania kluczy prywatnych w systemach płatności online.
 - Umożliwienie pracownikom generate nowych adresów odbiorczych bez dostępu do kluczy prywatnych.
- **Organizacje i finansowanie społecznościowe**: Przejrzyste wyświetlanie salda darczyńcom bez zezwalania na dostęp do środków.



### 1.3. Wprowadzenie Watch-Only



Wallet **Watch-Only** pozwala monitorować transakcje i saldo Bitcoin Wallet bez dostępu do kluczy prywatnych. W przeciwieństwie do konwencjonalnego Wallet, przechowuje on tylko dane publiczne, takie jak **rozszerzony klucz publiczny** (który dał początek "**xpub**", a następnie "zpub", "ypub" itd.), co umożliwia mu uzyskanie adresów odbiorczych i śledzenie historii transakcji na Blockchain Bitcoin. Brak kluczy prywatnych uniemożliwia wypłatę środków z aplikacji, gwarantując zwiększone bezpieczeństwo.



![image](assets/fr/10.webp)



**Dlaczego warto używać Watch-only wallet?**





- **Bezpieczeństwo**: Idealny do monitorowania portfela zabezpieczonego przez **Hardware Wallet** bez ujawniania kluczy prywatnych na podłączonym urządzeniu.
- **Wygoda**: Umożliwia sprawdzenie salda i generate nowych adresów odbiorców bez podłączania Hardware Wallet.
- **Poufność**: Kompatybilny z opcjami takimi jak **Tor** lub **SPV** w celu ograniczenia zależności od serwerów innych firm.
- **Przypadki użycia**: Śledzenie środków w ruchu, generowanie adresów do otrzymywania płatności lub weryfikowanie transakcji bez ryzykowania kluczy prywatnych.



![image](assets/fr/01.webp)



### 1.4. Rozszerzone klucze publiczne



**Rozszerzony klucz publiczny** (xpub, ypub, zpub itp.) to fragment danych pochodzący z Bitcoin Wallet, który generuje wszystkie podrzędne klucze publiczne i powiązane z nimi adresy odbioru, bez udostępniania kluczy prywatnych.





- **Jak to działa**: Rozszerzony klucz publiczny jest generowany z frazy seed w procesie deterministycznym (BIP-32). Tworzy on hierarchiczne drzewo podrzędnych kluczy publicznych, z których każdy może zostać przekształcony w otrzymany Address. Używając tej samej ścieżki derywacji (np. `m/44'/0'/0'`) co obserwowany Wallet, Watch-only wallet generuje te same adresy, umożliwiając śledzenie środków i tworzenie nowych adresów odbiorczych.



![image](assets/fr/11.webp)





- Rozszerzone typy kluczy publicznych
- **xpub**: Używany dla portfeli Legacy (adresy zaczynające się od "1", BIP-44) i portfeli Taproot (adresy zaczynające się od "bc1p", BIP-86).
- **ypub**: Zaprojektowany dla kompatybilnych portfeli SegWit (adresy zaczynające się od "3", BIP-49).
- **zpub**: Związane z natywnymi portfelami SegWit (adresy zaczynające się od "bc1q", BIP-84).
- **Inne (tpub, upub, vpub itp.)**: Używane dla alternatywnych sieci (takich jak Testnet) lub określonych standardów. Na przykład tpub dotyczy sieci Testnet.





- **Rozróżnienie**: Wybór między xpub, ypub lub zpub zależy od typu Address (starszy, SegWit, Taproot lub zagnieżdżony SegWit) i standardu BIP używanego przez Wallet. Sprawdź format wymagany przez portfel źródłowy, aby zapewnić zgodność z aplikacją Blockstream.





- **Bezpieczeństwo i poufność**: Rozszerzony klucz publiczny nie jest wrażliwy pod względem bezpieczeństwa, ponieważ nie pozwala na wydawanie środków (brak dostępu do kluczy prywatnych). Jest jednak wrażliwy pod względem poufności, ponieważ ujawnia wszystkie adresy publiczne i powiązaną historię transakcji.



**Zalecenie**: Chroń swój rozszerzony klucz publiczny jako informacje poufne.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet przypomnienie





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: wszystkie nazwy aplikacji instalowanej na smartfonie, komputerze lub dowolnym urządzeniu podłączonym do Internetu, umożliwiającej zarządzanie i zabezpieczanie kluczy prywatnych z Bitcoin Wallet.
- W przeciwieństwie do **portfeli sprzętowych**, znanych również jako **portfele Cold**, które izolują klucze w trybie offline, portfele programowe działają w połączonym środowisku, co czyni je bardziej podatnymi na cyberataki.





- **Zalecane zastosowanie**:
    - Idealny do zarządzania umiarkowanymi ilościami Bitcoin, szczególnie w przypadku codziennych transakcji.
    - Odpowiedni dla początkujących lub użytkowników z ograniczonymi zasobami, dla których Hardware Wallet może wydawać się zbędny.





- **Ograniczenia**: Mniej bezpieczny do przechowywania dużych środków lub długoterminowych oszczędności. W takim przypadku należy wybrać Hardware Wallet.




## 2. Przedstawiamy aplikację Blockstream





- **Blockstream App** to aplikacja mobilna (iOS, Android) i stacjonarna do zarządzania portfelami Bitcoin i aktywami na Liquid Network. Przejęta przez [Blockstream](https://blockstream.com/) w 2016 roku, wcześniej nosiła nazwę *Green Address*, a następnie *Blockstream Green*.
- **Kluczowe cechy**:
- Transakcje **onchain** na Blockchain Bitcoin.
    - Transakcje w sieci **Liquid** (Sidechain dla szybkich, poufnych wymian).
- Portfele typu **Watch-only** do monitorowania funduszy bez dostępu do kluczy.
    - Opcje prywatności: połączenie przez **Tor**, połączenie z **osobistym węzłem** przez Electrum lub weryfikacja **SPV** w celu zmniejszenia zależności od węzłów innych firm.
    - Funkcje **Replace-by-fee (RBF)** w celu przyspieszenia niepotwierdzonych transakcji.
- **Kompatybilność**: Integruje portfele sprzętowe, takie jak **Blockstream Jade**.
- **Interface**: Intuicyjny dla początkujących, z zaawansowanymi opcjami dla ekspertów.
- **Uwaga**: Niniejszy przewodnik koncentruje się na korzystaniu z Onchain. Inne samouczki w dodatkach obejmują Onchain, Watch-Only i wersję desktopową.




## 3. Instalowanie i konfigurowanie aplikacji Blockstream



### 3.1. pobierz





- Dla systemu **Android**:
    - Pobierz aplikację [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) ze sklepu Google Play.
    - Alternatywa: Zainstalować za pomocą pliku APK dostępnego na stronie [Blockstream's official GitHub](https://github.com/Blockstream/green_android).
- Dla systemu **iOS**:
    - Pobierz aplikację [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) ze sklepu App Store.
- **Uwaga**: Pamiętaj, aby pobierać z oficjalnych źródeł, aby uniknąć nieuczciwych aplikacji.



### 3.2. początkowa konfiguracja





- **Ekran główny**: Po pierwszym otwarciu aplikacja wyświetla ekran bez skonfigurowanego Wallet. Utworzone lub zaimportowane portfele pojawią się tutaj później.



![image](assets/fr/02.webp)





- **Dostosuj ustawienia**: Kliknij "Ustawienia aplikacji", dostosuj poniższe opcje, kliknij "Zapisz", uruchom ponownie aplikację i utwórz swoje portfolio.



![image](assets/fr/03.webp)



#### 3.2.1. Zwiększona prywatność (tylko Android)





- **Funkcja**: Wyłącza zrzuty ekranu, ukrywa podglądy aplikacji w menedżerze zadań i blokuje dostęp, gdy telefon jest zablokowany.
- **Dlaczego**: Chroni dane przed nieautoryzowanym dostępem fizycznym lub złośliwym oprogramowaniem przechwytującym ekran.



#### 3.2.2. Połączenie przez Tor





- **Funkcja**: Przekierowywanie ruchu sieciowego przez **Tor**, anonimową sieć szyfrującą połączenia.
- Dlaczego? **Ukryj swoje IP Address i chroń swoją prywatność, idealne rozwiązanie, jeśli nie ufasz swojej sieci (na przykład publicznej sieci Wi-Fi).**
- **Wada**: Może spowolnić działanie aplikacji ze względu na szyfrowanie.
- **Zalecenie**: Aktywuj Tor, jeśli poufność jest priorytetem, ale przetestuj prędkość połączenia.



#### 3.2.3. Łączenie z węzłem osobistym





- **Funkcja**: Łączy aplikację z własnym **kompletnym węzłem Bitcoin** za pośrednictwem **serwera Electrum**.
- **Dlaczego?**: Zapewnia całkowitą kontrolę nad danymi Blockchain, eliminując zależność od serwerów Blockstream.
- **Wymagania wstępne**: Skonfigurowany węzeł Bitcoin.
- **Zalecenie**: Zaawansowani użytkownicy, którym zależy na maksymalnej suwerenności.



#### 3.2.4. Weryfikacja SPV





- **Funkcja**: Wykorzystuje **Uproszczoną Weryfikację Płatności (SPV)** do bezpośredniej weryfikacji niektórych danych Blockchain bez pobierania całego łańcucha.
- **Dlaczego**: Zmniejsza zależność od domyślnego węzła Blockstream, pozostając lekkim dla urządzeń mobilnych.
- **Wada**: Mniej bezpieczny niż Full node, ponieważ opiera się na węzłach innych firm w zakresie niektórych informacji.
- **Zalecenie**: Aktywuj SPV, jeśli nie możesz użyć węzła osobistego, ale wolisz Full node dla optymalnego bezpieczeństwa.





## 4. Tworzenie portfela Bitcoin "tylko do oglądania"



### 4.1. Odzyskaj rozszerzony klucz publiczny



Aby skonfigurować Watch-only wallet, należy najpierw uzyskać rozszerzony klucz publiczny (xpub, ypub, zpub itp.) Wallet, który ma być monitorowany. Informacje te są zazwyczaj dostępne w ustawieniach lub sekcji "Informacje o Wallet" oprogramowania lub Hardware Wallet.





- Przykład z aplikacją Blockstream: Na ekranie głównym Wallet przejdź do "Ustawienia", a następnie "Szczegóły Wallet" i skopiuj plik zpub :



![image](assets/fr/09.webp)





- Alternatywa 1: generate kod QR zawierający rozszerzony klucz publiczny do zeskanowania w następnym kroku.
- Alternatywa 2: Użyj output descriptor, jeśli Wallet zapewnia taką możliwość.



### 4.2. import Wallet Watch-only





- **Uwaga**: Skonfiguruj swoje portfolio w prywatnym środowisku, bez kamer i obserwatorów.
- Na ekranie głównym kliknij "Utwórz nowe portfolio", a następnie "Rozpocznij" :



![image](assets/fr/04.webp)





- Zostanie wyświetlony następny ekran:



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"** : Utwórz nowy Hot Wallet. Zobacz samouczek "Blockstream App - Onchain" w dodatku.
- (2) **"Przywróć z kopii zapasowej "**: Import istniejącego portfela przy użyciu frazy Mnemonic (12 lub 24 słowa). Uwaga: Nie należy importować frazy z Cold Wallet, ponieważ zostanie ona ujawniona na podłączonym urządzeniu, unieważniając jego zabezpieczenia.
- (3) **"Watch-Only "**: opcja, która interesuje nas w tym samouczku.





- Następnie wybierz "**Pojedynczy podpis**" i sieć "**Bitcoin**":



![image](assets/fr/12.webp)





- Wklej rozszerzony klucz publiczny (xpub, ypub, zpub itp.), zeskanuj odpowiedni kod QR lub wprowadź output descriptor. Nawet jeśli aplikacja określa "xpub", klucze ypub, zpub itp. są również autoryzowane. Następnie kliknij "Połącz":



![image](assets/fr/13.webp)




### 4.3. Korzystanie z Wallet Watch-only



Po zaimportowaniu Watch-only wallet wyświetla całkowite saldo i historię transakcji adresów pochodzących z rozszerzonego klucza publicznego. Widoczne są tylko transakcje onchain (transakcje Liquid są ignorowane). Aby monitorować Liquid Wallet, powtórz import, wybierając "Liquid" w poprzednim kroku.





- **Wyświetlanie salda i historii**: na ekranie głównym można wyświetlić całkowite saldo i historię transakcji onchain:



![image](assets/fr/14.webp)





- generate jako odbierający **Address**: Kliknij "Transact", a następnie "Receive", aby utworzyć nowy onchain Address. Udostępnij go za pomocą kodu QR lub skopiuj, aby otrzymać środki:



![image](assets/fr/15.webp)





- Wyślij środki: Kliknij **"Transact"**, a następnie **"Send"**. Możesz wprowadzić :
 - Address odbiorcy.
 - Kwota transakcji.
 - Opłaty transakcyjne.



Ponieważ jednak Watch-only wallet nie posiada kluczy prywatnych, nie można bezpośrednio wysyłać środków. Aby podpisać transakcję, należy podłączyć Hardware Wallet lub Exchange PSBT, skanując kody QR (opcja dostępna na przykład w Coldcard Q).



![image](assets/fr/16.webp)





- **Uwaga**: Aby uniknąć błędów, należy zawsze sprawdzać odbierający Address i szczegóły transakcji. Środki wysłane do niewłaściwego Address nie mogą zostać odzyskane.




## Załączniki



### A1. Inne samouczki dotyczące aplikacji Blockstream





- Korzystanie z sieci Onchain :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Korzystanie z Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Wersja na komputery stacjonarne :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Rozszerzone klucze publiczne





- Słowniczek :
 - [Rozszerzone klucze publiczne](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Kurs :
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3. Najlepsze praktyki



Aby bezpiecznie i wydajnie korzystać z **Aplikacji Blockstream**, należy przestrzegać poniższych zaleceń. Pomogą one chronić środki, zoptymalizować transakcje i zachować poufność w sieciach **Bitcoin (onchain)**, **Liquid** i **Lightning**.





- **Zabezpiecz swoją frazę odzyskiwania**:
 - Samouczek: Zapisywanie frazy Mnemonic



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Użyj **bezpiecznego uwierzytelniania**:
 - Aktywuj **silny kod PIN** lub **uwierzytelnianie biometryczne** (odcisk palca lub rozpoznawanie twarzy), aby chronić dostęp do aplikacji.
 - Nigdy nie udostępniaj swojego kodu PIN ani danych biometrycznych.





- **Chroń swoją prywatność**:
 - generate nowy Address dla każdego odbioru onchain lub Liquid w celu ograniczenia śledzenia na Blockchain.
 - Aktywuj funkcje "Zwiększona prywatność", "Tor" i "SPV".
 - Aby zapewnić maksymalną poufność, połącz Wallet z własnym węzłem Bitcoin za pośrednictwem serwera Electrum, zamiast korzystać z węzła publicznego





- **Wybierz sieć najlepiej dopasowaną do Twoich potrzeb**:
- **Onchain**: Preferowany w przypadku długoterminowego przechowywania lub transakcji o dużej wartości (opłaty nieistotne w stosunku do kwoty).
- **Liquid**: Służy do szybkich, tanich transferów o zwiększonej poufności.
- **Błyskawica**: Wybierz natychmiastowe, tanie przelewy dla małych kwot.





- **Zawsze sprawdzaj adresy wysyłki**:
 - Przed wysłaniem środków należy dokładnie sprawdzić Address. Środki wysłane na niewłaściwy Address zostaną bezpowrotnie utracone. Używaj funkcji kopiuj/wklej lub skanowania kodów QR, nigdy nie kopiuj/modyfikuj Address ręcznie.





- **Optymalizacja kosztów**:
 - W przypadku transakcji onchain należy wybrać odpowiednie opłaty (wolne, średnie, szybkie) w zależności od pilności i przeciążenia sieci.
 - Użyj Liquid lub Lightning dla małych ilości.





- Aktualizuj aplikację na bieżąco




### A4. Dodatkowe zasoby





- Oficjalne linki Blockstream:
- [Oficjalna strona internetowa](https://blockstream.com/)
- [Wsparcie dla aplikacji mobilnej](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentacja i czat
- [GitHub](https://github.com/Blockstream/green_android)





- **Block Explorers:**
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Błyskawica: **[1ML (Lightning Network)](https://1ml.com/)**





- Nauka i samouczki: **[Plan ₿ Network](https://planb.network/)**
  - Zabezpieczanie frazy odzyskiwania



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Glosariusz](https://planb.network/fr/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Glosariusz](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb