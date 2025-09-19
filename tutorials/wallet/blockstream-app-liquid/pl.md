---
name: Blockstream App - Liquid
description: Jak skonfigurować aplikację Blockstream i korzystać z Liquid Network
---
![cover](assets/cover.webp)


## 1. Wprowadzenie


### 1.1 Cel samouczka





- Ten samouczek wyjaśnia, jak korzystać z aplikacji mobilnej **Blockstream App** do zarządzania portfelem **Bitcoin Liquid**, tj. transakcjami zarejestrowanymi bezpośrednio w łańcuchu bocznym Bitcoin "Liquid".
- Obejmuje on instalację, początkową konfigurację, tworzenie Software Wallet oraz operacje odbierania i wysyłania bitcoinów na Liquid.
- Uwaga: Inne samouczki w dodatkach obejmują Onchain, Watch-Only i wersję desktopową.



### 1.2 Grupa docelowa





- **Początkujący**: Użytkownicy chcący zarządzać swoimi bitcoinami za pomocą intuicyjnej aplikacji mobilnej, integrującej Liquid Network.
- **Użytkownicy średniozaawansowani**: Osoby chcące zrozumieć funkcje onchain i opcje prywatności, takie jak Tor lub SPV.



### 1.3 Przedstawiamy Liquid



**Liquid** to **Sidechain** Bitcoin, opracowany przez **[Blockstream](https://blockstream.com/Liquid/)**, zaprojektowany, aby oferować szybsze, bardziej Confidential Transactions i zaawansowane funkcje, pozostając jednocześnie połączonym z głównym Blockchain Bitcoin.



Sidechain to niezależny Blockchain, który działa równolegle z Bitcoin, wykorzystując mechanizm znany jako **two-way peg**. System ten blokuje bitcoiny na głównym Blockchain, aby utworzyć **Liquid-Bitcoins (L-BTC)**, tokeny, które krążą na Liquid Network, zachowując parytet wartości z oryginalnymi bitcoinami. Środki mogą zostać zwrócone do Blockchain Bitcoin w dowolnym momencie.



![image](assets/fr/17.webp)






- (1) **Peg-in**: Bitcoiny (BTC) są blokowane na głównym Blockchain przez federację Liquid. W zamian równoważna ilość bitcoinów Liquid (L-BTC), zapewniająca parytet między dwoma łańcuchami, jest emitowana na Blockchain Liquid i wysyłana do użytkownika.





- (2) **Niezależne transakcje**: Transakcje mogą być uruchamiane jednocześnie i niezależnie na głównym Blockchain (BTC) i Sidechain Liquid (L-BTC), w zależności od wymagań użytkownika.





- (3) **Peg-out**: Użytkownik wysyła Liquid-Bitcoiny (L-BTC) z powrotem do federacji Liquid. Federacja następnie odblokowuje równoważną ilość bitcoinów (BTC) na głównym Blockchain i przekazuje je użytkownikowi.



Liquid opiera się na **federacji** zaufanych uczestników (giełdy, uznane firmy Bitcoin), którzy zarządzają walidacją bloków i dwustronnym kotwiczeniem. W przeciwieństwie do Blockchain Bitcoin, który jest zdecentralizowany i opiera się na górnikach, Liquid jest siecią **federacyjną**, co oznacza, że jej bezpieczeństwo i zarządzanie zależy od tych uczestników. Chociaż oznacza to kompromis w zakresie decentralizacji, umożliwia zoptymalizowaną wydajność i zaawansowaną funkcjonalność.



![image](assets/fr/18.webp)



##### Dlaczego warto używać Liquid?





- **Szybkość**: Transakcje na Liquid są potwierdzane w około **1 minutę**, w porównaniu do 10 minut lub więcej w przypadku transakcji onchain, dzięki blokom generowanym co minutę przez federację walidatorów.
- **Zwiększona poufność**: Liquid korzysta z **Confidential Transactions**, który ukrywa ilość i rodzaj transferowanych aktywów, czyniąc transakcje bardziej prywatnymi (choć adresy pozostają widoczne).
- **Niskie opłaty**: Transakcje na Liquid są generalnie tańsze, co czyni je idealnymi do częstych przelewów lub niewielkich kwot.
- **Wiele aktywów**: Oprócz L-BTC, Liquid obsługuje emisję innych aktywów cyfrowych, takich jak stablecoiny lub tokeny, do wykorzystania w określonych zastosowaniach.
- **Przypadki użycia**: Liquid jest szczególnie odpowiedni dla międzyplatformowych giełd, szybkich płatności lub aplikacji wymagających inteligentnych kontraktów, pozostając jednocześnie powiązanym z bezpieczeństwem Bitcoin.



**Uwaga: Ten samouczek koncentruje się na korzystaniu z Liquid za pośrednictwem aplikacji Blockstream. Aby dogłębnie zrozumieć Liquid Network, znajdziesz zasoby w dodatku.**



### 1.4. Hot Wallet przypomnienie





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: wszystkie nazwy aplikacji instalowanej na smartfonie, komputerze lub dowolnym urządzeniu podłączonym do Internetu, umożliwiającej zarządzanie i zabezpieczanie kluczy prywatnych z Bitcoin Wallet.
- W przeciwieństwie do **portfeli sprzętowych**, znanych również jako **portfele Cold**, które izolują klucze w trybie offline, portfele programowe działają w połączonym środowisku, co czyni je bardziej podatnymi na cyberataki.





- **Zalecane zastosowanie**:
    - Idealny do zarządzania umiarkowanymi ilościami Bitcoin, szczególnie w przypadku codziennych transakcji.
    - Odpowiedni dla początkujących lub użytkowników z ograniczonymi zasobami, dla których Hardware Wallet może wydawać się zbędny.





- **Ograniczenia**: Mniej bezpieczny do przechowywania dużych środków lub długoterminowych oszczędności. W takim przypadku należy wybrać Hardware Wallet.




## 2. Przedstawiamy aplikację Blockstream





- **Blockstream App** to aplikacja mobilna (iOS, Android) i stacjonarna do zarządzania portfelami Bitcoin i aktywami na Liquid Network. Przejęta przez [Blockstream](https://blockstream.com/) w 2016 roku, wcześniej nosiła nazwę *Green Address*, a następnie *Blockstream Green*.
- **Kluczowe cechy**:
- **Transakcje Onchain** na Blockchain Bitcoin.
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
- **Dlaczego?**: Ukryj swoje IP Address i chroń swoją prywatność, idealne rozwiązanie, jeśli nie ufasz swojej sieci (na przykład publicznej sieci Wi-Fi).
- **Wada**: Może spowolnić działanie aplikacji ze względu na szyfrowanie.
- **Zalecenie**: Aktywuj Tor, jeśli poufność jest priorytetem, ale przetestuj prędkość połączenia.



#### 3.2.3. Łączenie z węzłem osobistym





- **Funkcja**: Łączy aplikację z własnym **kompletnym węzłem Bitcoin** za pośrednictwem **serwera Electrum**.
- **Dlaczego?**: Zapewnia całkowitą kontrolę nad danymi Blockchain, eliminując zależność od serwerów Blockstream.
- **Wymagania wstępne**: Skonfigurowany węzeł Bitcoin.
- **Zalecenie**: Zaawansowani użytkownicy, którym zależy na maksymalnej suwerenności.



#### 3.2.4. Weryfikacja SPV





- **Funkcja**: Wykorzystuje **Uproszczoną Weryfikację Płatności (SPV)** do bezpośredniej weryfikacji określonych danych Blockchain bez konieczności pobierania całego łańcucha.
- **Dlaczego**: Zmniejsza zależność od domyślnego węzła Blockstream, pozostając lekkim dla urządzeń mobilnych.
- **Wada**: Mniej bezpieczny niż Full node, ponieważ opiera się na węzłach innych firm w zakresie niektórych informacji.
- **Zalecenie**: Aktywuj SPV, jeśli nie możesz użyć węzła osobistego, ale wolisz Full node dla optymalnego bezpieczeństwa.





## 4. Tworzenie portfela Bitcoin onchain



### 4.1. Rozpocznij tworzenie





- **Uwaga**: Skonfiguruj swoje portfolio w prywatnym środowisku, bez kamer i obserwatorów.
- Na ekranie głównym kliknij "Rozpocznij" :



![image](assets/fr/04.webp)





- Jeśli chcesz zarządzać **Cold Wallet** (offline Wallet): kliknij **"Connect Jade "**, aby użyć Hardware Wallet Blockstream Jade lub innych kompatybilnych portfeli Cold.



![image](assets/fr/05.webp)






- Zostanie wyświetlony następny ekran:



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"** : Utwórz nowy Hot Wallet (Hot Wallet).
- (2) **"Przywróć z kopii zapasowej "**: Import istniejącego portfolio przy użyciu frazy Mnemonic (12 lub 24 słowa). Ostrzeżenie: Nie należy importować frazy z Cold Wallet, ponieważ zostanie ona ujawniona na podłączonym urządzeniu, unieważniając jego zabezpieczenia.
- (3) **"Watch-Only "**: Import istniejącego portfela tylko do odczytu, aby wyświetlić saldo (np. Cold Wallet) bez ujawniania frazy Mnemonic. Zobacz samouczek "Tylko obserwacja" w dodatku.



**W tym samouczku**: Kliknij **"Setup Mobile Wallet"**, aby utworzyć Hot Wallet.


Wallet zostanie automatycznie utworzony i wyświetlona zostanie strona główna Wallet, tutaj nazwana "My Wallet 5":



![image](assets/fr/07.webp)



**Ważne**: Aplikacja Blockstream uprościła tworzenie Wallet, nie wyświetlając automatycznie 12-wyrazowej frazy seed. *Mimo że portfel jest teraz tworzony jednym kliknięciem, ryzykujesz utratę dostępu do swoich funduszy, jeśli nie zapiszesz frazy seed*.



### 4.2. Zapisz frazę seed





- Na ekranie głównym Wallet kliknij zakładkę "Bezpieczeństwo", a następnie opcję "Utwórz kopię zapasową" lub menu "Fraza odzyskiwania":



![image](assets/fr/08.webp)



Zostanie wyświetlona 12-wyrazowa fraza seed, którą można zapisać.





- Zapisz swoją frazę odzyskiwania z najwyższą starannością. Zapisz ją na papierze lub metalu i przechowuj w bezpiecznym miejscu (bezpiecznej lokalizacji offline). Ta fraza jest jedynym sposobem na uzyskanie dostępu do bitcoinów w przypadku utraty urządzenia lub usunięcia aplikacji.
- Ważne jest również, aby pamiętać, że każdy, kto ma tę frazę, może ukraść wszystkie twoje bitcoiny. Nigdy nie przechowuj ich cyfrowo:
 - Brak zrzutu ekranu
 - Brak kopii zapasowych w chmurze, poczcie e-mail lub wiadomościach
 - Brak funkcji kopiuj/wklej (ryzyko zapisania w schowku)



**! Ten punkt jest krytyczny**. Więcej informacji na temat tworzenia kopii zapasowych :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Sprawdź zdanie seed



Przed wysłaniem środków do Address powiązanego z tą frazą seed należy przetestować kopię zapasową 12 słów.


Aby to zrobić, zapiszemy referencję, usuniemy Wallet, przywrócimy ją za pomocą kopii zapasowej i sprawdzimy, czy referencja pozostała niezmieniona.





- Na ekranie głównym Wallet kliknij zakładkę "Ustawienia", a następnie "Szczegóły Wallet" i skopiuj zPub ([rozszerzony klucz publiczny] (https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):



![image](assets/fr/09.webp)



Uwaga: zpub Address można zaimportować do aplikacji Blockstream dla funkcji "Watch Only" (patrz Dodatek).





- Usuń aplikację, a następnie przywróć Wallet za pomocą **"Przywróć z kopii zapasowej "**, wpisując frazę Mnemonic i sprawdź, czy zpub jest niezmieniony. Jeśli tak, to kopia zapasowa jest poprawna i można wysyłać środki do Wallet.





- Aby dowiedzieć się więcej o tym, jak wykonać test odzyskiwania, tutaj znajduje się dedykowany samouczek :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Zabezpieczenie dostępu do aplikacji



Zablokuj dostęp do aplikacji silnym kodem PIN:




- Na ekranie głównym Wallet przejdź do **"Bezpieczeństwo "**, a następnie kliknij **"PIN "**
- Wprowadź i potwierdź **losowy 6-cyfrowy kod PIN**.



**Opcja biometryczna**: Dostępna dla dodatkowej wygody, ale mniej bezpieczna niż solidny kod PIN (ryzyko nieautoryzowanego dostępu, np. odcisk palca lub skan twarzy podczas snu).



**Uwaga**: PIN zabezpiecza urządzenie, ale tylko fraza seed może być użyta do odzyskania środków.





## 5. Korzystanie z Liquid Wallet



### 5.1. Otrzymywanie bitcoinów "L-BTC"



Aby otrzymać Liquid-Bitcoiny (L-BTC), dostępnych jest kilka opcji. Możesz poprosić kogoś o przesłanie Ci ich bezpośrednio, udostępniając Liquid otrzymując Address, co zostało szczegółowo opisane poniżej.



Alternatywnie, Exchange swoje bitcoiny onchain lub za pośrednictwem Lightning Network dla L-BTC przy użyciu [mostu takiego jak Boltz](https://boltz.Exchange/): wprowadź swój Liquid odbierający Address, dokonaj płatności zgodnie z preferencjami i odbierz swój L-BTC.





- Na ekranie głównym portfela kliknij "**Transact**", a następnie **"Receive**.



![image](assets/fr/19.webp)





- Domyślnie aplikacja wyświetla pusty **pokwitowanie Address, onchain** (format SegWit v0, zaczynający się od `bc1q...`). Kliknij "Bitcoin", aby wybrać **Liquid Bitcoin** :



![image](assets/fr/20.webp)





- **Opcje**:
 - (1) Kliknij strzałki, aby wybrać inny nowy Address powiązany z tym zdaniem seed.
    - (2) Możesz także wybrać Address spośród już używanych/wyświetlanych, klikając na trzy kropki w prawym górnym rogu, a następnie na "List of Addresses"
    - (3) Aby zażądać określonej kwoty, kliknij trzy kropki w prawym górnym rogu, wybierz "Żądaj kwoty" i wprowadź żądaną kwotę. QR zostanie zaktualizowany, a Address zostanie zastąpiony przez URI płatności Bitcoin.



![image](assets/fr/21.webp)





- Udostępnij Address/URI, klikając "**Share**", kopiując tekst lub skanując kod QR.
- **Weryfikacja**: Sprawdź Address udostępniony odbiorcy w jak największym stopniu, aby uniknąć błędów lub ataków (np. złośliwego oprogramowania modyfikującego schowek).



### 5.2. wysyłanie bitcoinów





- Na ekranie głównym portfolio kliknij "**Transact**", a następnie **"Send "**:



![image](assets/fr/22.webp)





- Wprowadź **szczegóły**:
    - (1) Wprowadź **Address odbiorcy**, przyklejając go lub skanując kod QR.
    - (2) Sprawdź aktywa i konto, z którego wysyłane są środki.
    - (3) Wskaż **kwotę** do wysłania. Możesz wybrać jednostkę: L-BTC, L-satoshis, USD, ...



![image](assets/fr/23.webp)





- **Sprawdź**:
    - Sprawdź Address, kwotę i opłaty na ekranie podsumowania.
    - Błąd Address może spowodować nieodwracalną utratę środków. Należy uważać na złośliwe oprogramowanie, które modyfikuje schowek.



![image](assets/fr/24.webp)





- **Potwierdzenie**: Przesuń przycisk "Wyślij", aby podpisać i rozpowszechnić transakcję.
- **Kontynuacja**: W zakładce "Transakcja" Wallet transakcja pojawia się jako "Niepotwierdzona", następnie "Potwierdzona", a następnie "Zakończona":



![image](assets/fr/25.webp)





- Czas między 2 blokami wynosi 1 minutę na Liquid, więc transakcja jest szybko potwierdzana i finalizowana.




## Załączniki



### A1. Inne samouczki dotyczące aplikacji Blockstream



Korzystanie z sieci Onchain



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Importowanie i śledzenie Wallet w trybie "Tylko zegarek"



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Wersja na komputery stacjonarne



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Najlepsze praktyki



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
 - Aby zapewnić maksymalną poufność, połącz swój Wallet z własnym węzłem Bitcoin za pośrednictwem serwera Electrum zamiast korzystać z węzła publicznego





- **Wybierz sieć najlepiej dopasowaną do Twoich potrzeb**:
- **Onchain**: Preferowany w przypadku długoterminowego przechowywania lub transakcji o dużej wartości (opłaty nieistotne w stosunku do kwoty).
- **Liquid**: Służy do szybkich, tanich transferów o zwiększonej poufności.
- **Błyskawica**: Wybierz natychmiastowe, tanie przelewy dla małych kwot.





- **Zawsze sprawdzaj adresy wysyłki**:
 - Przed wysłaniem środków należy dokładnie sprawdzić Address. Środki wysłane na niewłaściwy numer Address zostaną bezpowrotnie utracone. Używaj funkcji kopiuj/wklej lub skanowania kodów QR, nigdy nie kopiuj/modyfikuj Address ręcznie.





- **Optymalizacja kosztów**:
 - W przypadku transakcji onchain należy wybrać odpowiednie opłaty (wolne, średnie, szybkie) w zależności od pilności i przeciążenia sieci.
 - Użyj Liquid lub Lightning dla małych ilości.





- Aktualizuj aplikację na bieżąco




### A3. Dodatkowe zasoby





- **Oficjalne linki:**
- [Oficjalna strona internetowa](https://blockstream.com/)
- [Wsparcie dla aplikacji mobilnej](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentacja i czat
- [GitHub](https://github.com/Blockstream/green_android)





- **Block Explorers:**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid: **[Blockstream Info](https://blockstream.info/Liquid)**
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