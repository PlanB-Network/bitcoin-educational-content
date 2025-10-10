---
name: Blockstream App - Desktop
description: Jak używać Hardware Wallet z aplikacją Blockstream na komputerze?
---
![cover](assets/cover.webp)



## 1. Wprowadzenie



### 1.1 Cel samouczka





- Ten samouczek wyjaśnia, jak używać **Aplikacji Blockstream** na komputerze do zarządzania Bitcoin **onchain** Wallet z **Hardware Wallet**, umożliwiając bezpieczne transakcje rejestrowane na głównym Blockchain Bitcoin.
- Obejmuje on instalację, wstępną konfigurację, podłączenie Hardware Wallet oraz odbieranie i wysyłanie bitcoinów onchain.
- Uwaga: Inne samouczki w dodatkach obejmują Liquid, Watch-Only i aplikację mobilną.



### 1.2 Grupa docelowa





- **Początkujący**: Użytkownicy, którzy chcą zarządzać swoimi bitcoinami za pomocą bezpiecznego oprogramowania komputerowego i Hardware Wallet.
- **Użytkownicy średniozaawansowani**: Osoby, które chcą zrozumieć, jak używać Hardware Wallet do transakcji onchain i opcji prywatności, takich jak Tor lub SPV.



### 1.3. Kontekst portfeli sprzętowych





- **Hardware Wallet**, **Cold Wallet**: Fizyczne urządzenie, które przechowuje klucze prywatne w trybie offline, oferując wysoki poziom bezpieczeństwa przed cyberatakami, w przeciwieństwie do **portfeli Hot** (portfeli programowych na podłączonych urządzeniach).
- **Zalecane zastosowanie**:
    - Idealny do zabezpieczania dużych kwot lub długoterminowych oszczędności.
    - Odpowiedni dla użytkowników skupionych na bezpieczeństwie, którzy chcą chronić swoje fundusze przed zagrożeniami związanymi z podłączonymi urządzeniami.
- **Ograniczenia**: Wymaga oprogramowania takiego jak Blockstream App do przeglądania sald, adresów generate i nadawania transakcji podpisanych przez Hardware Wallet.



## 2. Przedstawiamy aplikację Blockstream





- **Blockstream App** to aplikacja mobilna (iOS, Android) i stacjonarna do zarządzania portfelami Bitcoin i aktywami na Liquid Network. Przejęta przez Blockstream w 2016 roku, nosiła nazwę *GreenAddress*, została przemianowana na *Blockstream Green* (2019), a obecnie nosi nazwę *Blockstream app* (2025).
- **Kluczowe cechy**:
- Transakcje **onchain** na Blockchain Bitcoin.
    - Transakcje w sieci **Liquid** (Sidechain dla szybkich, poufnych wymian).
- Portfele typu **Watch-only** do monitorowania funduszy bez dostępu do kluczy.
    - Opcje prywatności: połączenie przez **Tor**, połączenie z **osobistym węzłem** przez Electrum lub weryfikacja **SPV** w celu zmniejszenia zależności od węzłów innych firm.
    - Funkcje **Replace-by-fee (RBF)** w celu przyspieszenia niepotwierdzonych transakcji.
- **Kompatybilność**: Integruje portfele sprzętowe, takie jak **Blockstream Jade**.
- **Interface**: Intuicyjny dla początkujących, z zaawansowanymi opcjami dla ekspertów.
- **Uwaga**: Niniejszy przewodnik koncentruje się na korzystaniu z onchain z Hardware Wallet w wersji na komputery stacjonarne. Inne samouczki dostarczone jako załączniki obejmują korzystanie z aplikacji mobilnej, funkcji onchain, Liquid i Watch-Only.



## 3. Instalacja i konfiguracja aplikacji Blockstream App Desktop



### 3.1. pobierz





- Przejdź do [oficjalnej strony internetowej] (https://blockstream.com/app/) i kliknij "_Download Now_". Pobierz wersję odpowiadającą Twojemu systemowi operacyjnemu (Windows, macOS, Linux).
- **Uwaga**: Upewnij się, że pobierasz z oficjalnego źródła, aby uniknąć nieuczciwego oprogramowania.



### 3.2. początkowa konfiguracja





- **Ekran główny**: Po pierwszym otwarciu aplikacja wyświetla ekran bez skonfigurowanego Wallet. Utworzone lub zaimportowane portfele pojawią się tutaj później.



![image](assets/fr/02.webp)





- **Dostosowywanie ustawień**: Kliknij ikonę ustawień w lewym dolnym rogu, dostosuj poniższe opcje, a następnie wyjdź z Interface, aby kontynuować.



![image](assets/fr/03.webp)



#### 3.2.1. Parametry ogólne





- W menu ustawień kliknij "**Ogólne**".
- **Funkcja**: Zmiana języka oprogramowania i aktywacja funkcji eksperymentalnych w razie potrzeby.



![image](assets/fr/04.webp)



#### 3.2.2. Połączenie przez Tor





- W menu Ustawienia kliknij "**Sieć**".
- **Funkcja**: Przekierowywanie ruchu sieciowego przez **Tor**, anonimową sieć szyfrującą połączenia.
- Dlaczego? **Ukryj swoje IP Address i chroń swoją prywatność, idealne rozwiązanie, jeśli nie ufasz swojej sieci (na przykład publicznej sieci Wi-Fi).**
- **Wada**: Może spowolnić działanie aplikacji ze względu na szyfrowanie.
- **Zalecenie**: Aktywuj Tor, jeśli poufność jest priorytetem, ale przetestuj prędkość połączenia.



![image](assets/fr/05.webp)



#### 3.2.3. Łączenie z węzłem osobistym





- W menu Ustawienia kliknij "**Serwery niestandardowe i walidacja**".
- **Funkcja**: Łączy aplikację z własnym **kompletnym węzłem Bitcoin** za pośrednictwem **serwera Electrum**.
- **Dlaczego?**: Zapewnia całkowitą kontrolę nad danymi Blockchain, eliminując zależność od serwerów Blockstream.
- **Wymagania wstępne**: Skonfigurowany węzeł Bitcoin.
- **Zalecenie**: Zaawansowani użytkownicy, którym zależy na maksymalnej suwerenności.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. Weryfikacja SPV





- W menu Ustawienia kliknij "**Serwery niestandardowe i walidacja**".
- **Funkcja**: Wykorzystuje **Uproszczoną Weryfikację Płatności (SPV)**, która pobiera nagłówki bloków i weryfikuje transakcje poprzez dowód włączenia (Merkle), bez przechowywania pełnego Blockchain.
- Dlaczego? Zmniejsza zależność od domyślnego węzła Blockstream, pozostając lekkim dla urządzeń.
- **Wada**: Mniej bezpieczny niż Full node, ponieważ opiera się na węzłach innych firm w zakresie niektórych informacji.
- **Zalecenie**: Aktywuj SPV, jeśli nie możesz użyć węzła osobistego, ale wolisz Full node dla optymalnego bezpieczeństwa.



![image](assets/fr/07.webp)



## 4. Podłączanie Hardware Wallet do aplikacji Blockstream



### 4.1. Uwagi wstępne



#### 4.1.1. Dla użytkowników Ledger





- Blockstream Green obsługuje tylko aplikację **Bitcoin Legacy** na urządzeniach Ledger (Nano S, Nano X).
- Kroki, które należy wykonać w **Ledger Live** przed podłączeniem urządzenia :


1. Przejdź do **"Ustawienia "** → **"Funkcje eksperymentalne "** i aktywuj **tryb deweloperski**.


2. Przejdź do **"My Ledger"** → **"App Catalogue "**, a następnie zainstaluj aplikację **Bitcoin Legacy**


3. Otwórz aplikację **Bitcoin Legacy** na Ledger przed uruchomieniem Blockstream Green w celu nawiązania połączenia.




- **Uwaga**: Upewnij się, że Ledger jest odblokowany kodem PIN i że aplikacja Bitcoin Legacy jest aktywna podczas łączenia.



#### 4.1.2 Inicjalizacja Hardware Wallet





- Jeśli urządzenie Hardware Wallet (Ledger, Trezor lub Blockstream Jade) nie było nigdy używane (ani z Blockstream Green, ani z innym oprogramowaniem, takim jak Ledger Live), należy je najpierw zainicjować. Krok ten należy wykonać w bezpiecznym środowisku, bez kamer i obserwatorów:


1. **Generacja frazy seed / fraza Mnemonic** (12, 18 lub 24 słowa): Zapisz ją starannie na kartce papieru.


2. **Weryfikacja frazy seed**: Przetestuj import Wallet z odnotowanych słów, np. poprzez weryfikację rozszerzonego klucza publicznego. Do wykonania przed wysłaniem środków do Wallet i trwałym zabezpieczeniem frazy seed.


3. **Zabezpieczenie frazy seed**: Frazę należy przechowywać na nośniku fizycznym (papier lub metal) w bezpiecznym miejscu. Nigdy nie przechowuj jej w formie cyfrowej (żadnych zrzutów ekranu, chmury ani wiadomości e-mail).




- **Ważne**: Zwrot seed jest jedynym sposobem na odzyskanie środków w przypadku utraty lub awarii urządzenia. Każdy, kto ma do niego dostęp, może ukraść twoje bitcoiny.
- **Zasoby** do tworzenia kopii zapasowych i sprawdzania zdania seed :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Konfiguracja dla tego samouczka :





- Zakładamy, że Hardware Wallet został już zainicjowany za pomocą frazy seed i blokującego kodu PIN.
- Zakładamy, że urządzenie Hardware Wallet nigdy nie było połączone z aplikacją Blockstream App, co wymaga utworzenia nowego konta. Jeśli Hardware Wallet był już używany z aplikacją Blockstream, konto pojawi się automatycznie po otwarciu aplikacji.



### 4.2. Rozpocznij połączenie





- Na ekranie głównym kliknij "**Setup a New Wallet**", a następnie potwierdź warunki i kliknij "**Get Started**":



![image](assets/fr/08.webp)





- Wybierz opcję "**On Hardware Wallet**":



![image](assets/fr/09.webp)





- Jeśli używasz **Blockstream Jade**, kliknij odpowiedni przycisk. W przeciwnym razie wybierz "**Podłącz inne urządzenie sprzętowe**" :



![image](assets/fr/10.webp)





- Podłącz Hardware Wallet do komputera przez USB i wybierz go w aplikacji Blockstream:



![image](assets/fr/22.webp)





- Poczekaj, aż aplikacja Blockstream zaimportuje informacje o Twoim portfelu:



![image](assets/fr/23.webp)



### 4.3. Utwórz konto





- Jeśli Twój Hardware Wallet był już używany z aplikacją Blockstream, Twoje konto pojawi się automatycznie w Interface po zaimportowaniu. W przeciwnym razie należy utworzyć konto, klikając przycisk "**Utwórz konto**":



![image](assets/fr/24.webp)





- Wybierz "**Standard**", aby skonfigurować klasyczny portfel Bitcoin:



![image](assets/fr/25.webp)





- Po utworzeniu konta można uzyskać dostęp do głównego portfela Interface:



![image](assets/fr/26.webp)





## 5. Używanie Wallet onchain z Hardware Wallet



### 5.1. Otrzymywanie bitcoinów





- Na głównym ekranie portfolio kliknij "**Odbierz**" :



![image](assets/fr/27.webp)





- Aplikacja wyświetla **pusty odbiór Address**. Używanie nowego Address dla każdego odbioru zwiększa poufność. Kliknij "**Kopiuj Address**", aby skopiować Address, lub pozwól nadawcy zeskanować wyświetlony kod QR:



![image](assets/fr/12.webp)



**Opcje** :




- (1) Kliknij strzałki, aby generate utworzył nowy Address powiązany z Twoim portfelem.
- (2) Aby zażądać określonej kwoty, kliknij "**Więcej opcji**", a następnie "**Zażądaj kwoty**". QR zostanie zaktualizowany, a Address zostanie zastąpiony przez URI płatności Bitcoin, np: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Aby ponownie użyć poprzedniego Address, kliknij "**Więcej opcji**", a następnie "**Lista adresów**":



![image](assets/fr/14.webp)





- **Weryfikacja**: Dokładnie sprawdź udostępniony Address, aby uniknąć błędów lub ataków (np. złośliwego oprogramowania modyfikującego schowek).
- Gdy transakcja zostanie wyemitowana w sieci, pojawi się w Wallet. Odczekaj od 1 do 6 potwierdzeń, aby uznać transakcję za niezmienną.



![image](assets/fr/28.webp)



### 5.2. wysyłanie bitcoinów





- Na głównym ekranie portfolio kliknij "**Wyślij**".



![image](assets/fr/29.webp)





- Wprowadź **szczegóły**:
    - (1) Sprawdź, czy wybrany zasób to **Bitcoin** (onchain).
    - (2) Wprowadź **Address odbiorcy**, wklejając go lub skanując kod QR za pomocą kamery internetowej.
    - (3) Wskaż **kwotę** do wysłania (w BTC, satoshis lub innych jednostkach).




![image](assets/fr/16.webp)





- Wybierz **opłaty transakcyjne** (opcjonalnie) :
 - Wybierz jedną z sugerowanych opcji (szybko, średnio, wolno) w zależności od pilności, z szacowanym czasem potwierdzenia.
 - W przypadku niestandardowych opłat należy ręcznie dostosować liczbę satoshi na bajt. Są one wyświetlane na ekranie głównym. Patrz także [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **Ręczny wybór UTXO** (opcjonalnie): Kliknij "**Ręczny wybór Coin**", aby wybrać konkretne UTXO, które mają być użyte w transakcji.



![image](assets/fr/18.webp)





- **Wstępna weryfikacja**: Sprawdź Address, kwotę i opłaty na ekranie podsumowania, a następnie kliknij "**Potwierdź transakcję**". W rzeczywistości transakcja nie zostanie przekazana do sieci, dopóki nie zostanie podpisana za pomocą Hardware Wallet, który jako jedyny posiada tajne klucze powiązane z adresami, z których zostaną pobrane UTXO (satoshi).



![image](assets/fr/19.webp)





- **Końcowe sprawdzenie i podpis**: Upewnij się, że wszystkie parametry transakcji są prawidłowe **na ekranie Hardware Wallet**, a następnie podpisz transakcję za jego pomocą. Błąd Address może spowodować nieodwracalną utratę środków.





- **Transmisja**: Po podpisaniu, aplikacja Blockstream automatycznie rozgłasza transakcję w sieci Bitcoin.



![image](assets/fr/20.webp)





- **Kontynuacja**:
 - Transakcja pojawia się na ekranie głównym Wallet jako "oczekująca" do momentu potwierdzenia.
 - Dopóki transakcja nie zostanie potwierdzona, funkcja **Replace-by-fee (RBF)** może zostać użyta do przyspieszenia potwierdzenia poprzez zwiększenie opłaty (patrz Załącznik).



![image](assets/fr/21.webp)



## Załączniki



### A1. Inne samouczki Blockstream





- Korzystanie z Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Importowanie i śledzenie portfela w trybie "Tylko do oglądania" :



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- Korzystanie z aplikacji Blockstream na telefonach komórkowych (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Wyjaśnienie Replace-by-fee (RBF)





- **Definicja**: Replace-by-fee (RBF) to funkcja sieci Bitcoin, która pozwala nadawcy przyspieszyć potwierdzenie transakcji **onchain** poprzez zwiększenie opłaty.
- **Limity**:
    - RBF nie jest dostępny dla transakcji Liquid lub Lightning.
    - Początkowa transakcja musi być oznaczona jako zgodna z RBF, co Blockstream App robi automatycznie.
- Więcej informacji można znaleźć w [naszym słowniku] (https://planb.network/resources/glossary/rbf-replacebyfee).



### A3. Najlepsze praktyki





- **Zabezpiecz swoją frazę odzyskiwania**:
    - Zapisz frazę Hardware Wallet Mnemonic na nośniku fizycznym (papier, metal) w bezpiecznym miejscu.
    - Nigdy nie przechowuj go w formie cyfrowej (chmura, e-mail, zrzut ekranu).
    - Samouczek : Zapisz swoją frazę Mnemonic :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Chroń swoją prywatność**:





    - generate nowy Address dla każdego odbioru onchain.
    - Aktywuj **Tor** lub **SPV**, aby ograniczyć śledzenie.
    - Połącz się z własnym węzłem Bitcoin za pośrednictwem Electrum, aby uzyskać maksymalną suwerenność.
- **Zawsze sprawdzaj adresy wysyłki**:





    - Przed podpisaniem sprawdź Address na ekranie Hardware Wallet.
    - Użyj funkcji kopiuj/wklej lub kodu QR, aby uniknąć błędów ręcznych.
- **Optymalizacja kosztów**:





    - Dostosowanie opłat w zależności od pilności i przeciążenia sieci (patrz [Mempool.space](https://Mempool.space/)).
    - Użyj Liquid lub Lightning do szybkich, tanich transakcji, które nie wymagają zabezpieczeń onchain.
- **Aktualizacja oprogramowania**:





    - Aktualizuj swoją aplikację Blockstream i oprogramowanie sprzętowe Hardware Wallet o najnowsze funkcje i poprawki zabezpieczeń.



### A4. Dodatkowe zasoby





- **Oficjalne linki**:
    - [Oficjalna strona internetowa](https://blockstream.com/)
    - [Wsparcie dla aplikacji Blockstream](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentacja i czat
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Odkrywcy bloków**:
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Blockstream Info](https://blockstream.info/Liquid)
    - Błyskawica : [1ML (Lightning Network)](https://1ml.com/)





- **Zabezpieczenie frazy odzyskiwania:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Glosariusz](https://planb.network/fr/resources/glossary/liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Glosariusz](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb