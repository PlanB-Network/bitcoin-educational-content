---
name: Aplikacja Blockstream - Onchain
description: Skonfiguruj aplikację Blockstream na telefonie komórkowym i zarządzaj transakcjami onchain
---
![cover](assets/cover.webp)


## 1. Wprowadzenie


### 1.1 Cel samouczka





- Ten samouczek wyjaśnia, jak używać aplikacji mobilnej **Blockstream App** do zarządzania Bitcoin **onchain** Wallet, tj. transakcjami zarejestrowanymi bezpośrednio na głównym Blockchain Bitcoin.
- Obejmuje on instalację, początkową konfigurację, tworzenie Software Wallet oraz operacje odbierania i wysyłania bitcoinów.
- Uwaga: Inne samouczki w dodatkach obejmują Liquid, Watch-Only i wersję desktopową.



![image](assets/fr/01.webp)



### 1.2 Grupa docelowa





- Początkujący**: Użytkownicy chcący zarządzać swoimi bitcoinami za pomocą intuicyjnej aplikacji mobilnej.
- Użytkownicy średniozaawansowani**: Osoby chcące zrozumieć funkcje onchain i opcje prywatności, takie jak Tor lub SPV.



### 1.3. Przypomnienie o portfelach Hot





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: wszystkie nazwy dla aplikacji instalowanej na smartfonie, komputerze lub dowolnym urządzeniu podłączonym do Internetu, umożliwiającej zarządzanie i zabezpieczanie kluczy prywatnych z Bitcoin Wallet.
- W przeciwieństwie do **portfeli sprzętowych**, znanych również jako **portfele Cold**, które izolują klucze w trybie offline, portfele programowe działają w połączonym środowisku, co czyni je bardziej podatnymi na cyberataki.





- Zalecane zastosowanie** :
    - Idealny do zarządzania umiarkowanymi ilościami Bitcoin, szczególnie w przypadku codziennych transakcji.
    - Odpowiedni dla początkujących lub użytkowników z ograniczonymi zasobami, dla których Hardware Wallet może wydawać się zbędny.





- Ograniczenia**: Mniej bezpieczny do przechowywania dużych środków lub długoterminowych oszczędności. W takim przypadku należy wybrać Hardware Wallet.




## 2. Przedstawiamy aplikację Blockstream





- Blockstream App** to aplikacja mobilna (iOS, Android) i stacjonarna do zarządzania portfelami Bitcoin i aktywami na Liquid Network. Przejęta przez [Blockstream](https://blockstream.com/) w 2016 roku, wcześniej nosiła nazwę *Green Address*, a następnie *Blockstream Green*.
- Kluczowe cechy** :
    - Transakcje onchain** na Blockchain Bitcoin.
    - Transakcje sieciowe **Liquid** (Sidechain do szybkiej, poufnej wymiany).
    - Portfele typu Watch-only** do monitorowania funduszy bez dostępu do kluczy.
    - Opcje prywatności: połączenie przez **Tor**, połączenie z **osobistym węzłem** przez Electrum lub weryfikacja **SPV** w celu zmniejszenia zależności od węzłów innych firm.
    - Funkcje **Replace-by-fee (RBF)** w celu przyspieszenia niepotwierdzonych transakcji.
- Kompatybilność**: Integruje portfele sprzętowe, takie jak **Blockstream Jade**.
- Interface**: Intuicyjny dla początkujących, z zaawansowanymi opcjami dla ekspertów.
- Uwaga**: Niniejszy przewodnik koncentruje się na korzystaniu z onchain. Inne samouczki w dodatkach obejmują Liquid, Watch-Only i wersję desktopową.



## 3. Instalowanie i konfigurowanie aplikacji Blockstream



### 3.1. pobierz





- Dla systemu Android** :
    - Pobierz aplikację [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) ze sklepu Google Play.
    - Alternatywa: Zainstalować za pomocą pliku APK dostępnego na stronie [Blockstream's official GitHub](https://github.com/Blockstream/green_android).
- Dla systemu iOS** :
    - Pobierz aplikację [Blockstream App](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) ze sklepu App Store.
- Uwaga**: Pamiętaj, aby pobierać z oficjalnych źródeł, aby uniknąć nieuczciwych aplikacji.



### 3.2. początkowa konfiguracja





- Ekran główny**: Po pierwszym otwarciu aplikacja wyświetla ekran bez skonfigurowanego Wallet. Utworzone lub zaimportowane portfele pojawią się tutaj później.



![image](assets/fr/02.webp)





- Dostosuj ustawienia**: Kliknij "Ustawienia aplikacji", dostosuj poniższe opcje, kliknij "Zapisz", uruchom ponownie aplikację i utwórz swoje portfolio.



![image](assets/fr/03.webp)



#### 3.2.1. Zwiększona prywatność (tylko Android)





- Funkcja**: Wyłącza zrzuty ekranu, ukrywa podglądy aplikacji w menedżerze zadań i blokuje dostęp, gdy telefon jest zablokowany.
- Dlaczego** : Chroni dane przed nieautoryzowanym dostępem fizycznym lub złośliwym oprogramowaniem przechwytującym ekran.


#### 3.2.2. Połączenie przez Tor





- Funkcja**: Przekierowywanie ruchu sieciowego przez **Tor**, anonimową sieć szyfrującą połączenia.
- Dlaczego? **: Ukryj swoje IP Address i chroń swoją prywatność, idealne rozwiązanie, jeśli nie ufasz swojej sieci (na przykład publicznej sieci Wi-Fi).
- Wada**: Może spowolnić działanie aplikacji ze względu na szyfrowanie.
- Zalecenie**: Aktywuj Tor, jeśli poufność jest priorytetem, ale przetestuj prędkość połączenia.


#### 3.2.3. Łączenie z węzłem osobistym





- Funkcja**: Łączy aplikację z własnym **kompletnym węzłem Bitcoin** za pośrednictwem serwera **Electrum**.
- Dlaczego?**: Zapewnia całkowitą kontrolę nad danymi Blockchain, eliminując zależność od serwerów Blockstream.
- Wymagania wstępne**: Skonfigurowany węzeł Bitcoin.
- Zalecenie**: Zaawansowani użytkownicy poszukujący maksymalnej suwerenności.


#### 3.2.4. Weryfikacja SPV





- Funkcja**: Wykorzystuje **Uproszczoną Weryfikację Płatności (SPV)** do bezpośredniej weryfikacji niektórych danych Blockchain bez pobierania całego łańcucha.
- Dlaczego**: Zmniejsza zależność od domyślnego węzła Blockstream, pozostając lekkim dla urządzeń mobilnych.
- Wada**: Mniej bezpieczny niż Full node, ponieważ opiera się na węzłach innych firm w zakresie niektórych informacji.
- Zalecenie**: Aktywuj SPV, jeśli nie możesz użyć węzła osobistego, ale wolisz Full node dla optymalnego bezpieczeństwa.





## 4. Tworzenie portfela Bitcoin onchain



### 4.1. Rozpocznij tworzenie





- Uwaga**: Skonfiguruj swoje portfolio w prywatnym środowisku, bez kamer i obserwatorów.
- Na ekranie głównym kliknij "Rozpocznij" :



![image](assets/fr/04.webp)





- Jeśli chcesz zarządzać **Cold Wallet** (offline Wallet): kliknij **"Connect Jade "**, aby użyć Hardware Wallet Blockstream Jade lub innych kompatybilnych portfeli Cold.



![image](assets/fr/05.webp)





- Zostanie wyświetlony następny ekran:



![image](assets/fr/06.webp)





- (1) **"Setup Mobile Wallet"** : Utwórz nowy Hot Wallet (Hot Wallet).
- (2) **"Przywróć z kopii zapasowej "**: Import istniejącego portfela przy użyciu frazy Mnemonic (12 lub 24 słowa). Uwaga: Nie należy importować frazy Cold Wallet, ponieważ zostanie ona ujawniona na podłączonym urządzeniu, unieważniając jego zabezpieczenia.
- (3) **"Tylko do obserwacji "**: Zaimportuj istniejący portfel tylko do odczytu, aby wyświetlić saldo (np. swojego Cold Wallet) bez ujawniania frazy Mnemonic. Zobacz samouczek Watch Only w załączniku.



**W tym samouczku**: Kliknij **"Setup Mobile Wallet"**, aby utworzyć Hot Wallet.


Urządzenie Wallet zostanie automatycznie utworzone i wyświetlona zostanie strona główna Wallet o nazwie "My Wallet 5":



![image](assets/fr/07.webp)



**Ważne**: Aplikacja Blockstream uprościła tworzenie Wallet, nie wyświetlając automatycznie 12-wyrazowej frazy seed. *Mimo że portfel jest teraz tworzony jednym kliknięciem, ryzykujesz utratę dostępu do swoich funduszy, jeśli nie zapiszesz frazy seed*.



### 4.2. Zapisz zdanie seed





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

### 4.3. Potwierdzenie zdania seed



Przed wysłaniem środków do Address powiązanego z tym zdaniem seed należy przetestować kopię zapasową 12 słów.



Aby to zrobić, zapiszemy odniesienie, usuniemy Wallet, przywrócimy go za pomocą kopii zapasowej i sprawdzimy, czy odniesienie pozostało niezmienione.





- Na ekranie głównym Wallet kliknij zakładkę "Ustawienia", a następnie "Szczegóły Wallet" i skopiuj zPub ([rozszerzony klucz publiczny](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602):



![image](assets/fr/09.webp)



Uwaga: urządzenie zpub Address może zostać zaimportowane do aplikacji Blockstream dla funkcji "Watch Only" (patrz Dodatek).





- Usuń aplikację, a następnie przywróć Wallet za pomocą **"Przywróć z kopii zapasowej "**, wprowadzając frazę Mnemonic i sprawdź, czy zpub jest niezmieniony. Jeśli tak, to kopia zapasowa jest poprawna i można wysyłać środki do Wallet.





- Aby dowiedzieć się więcej o tym, jak wykonać test odzyskiwania, tutaj znajduje się dedykowany samouczek :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5. Zabezpieczenie dostępu do aplikacji



Zablokuj dostęp do aplikacji silnym kodem PIN:




- Na ekranie głównym Wallet przejdź do **"Bezpieczeństwo "**, a następnie kliknij **"PIN "**
- Wprowadź i potwierdź **losowy 6-cyfrowy kod PIN**.



**Opcja biometryczna**: Dostępna dla dodatkowej wygody, ale mniej bezpieczna niż solidny kod PIN (ryzyko nieautoryzowanego dostępu, np. odcisk palca lub skan twarzy podczas snu).



**Uwaga**: PIN zabezpiecza urządzenie, ale tylko fraza seed może być użyta do odzyskania środków.





## 5. Korzystanie z onchain Wallet



### 5.1. Otrzymywanie bitcoinów





- Na ekranie głównym portfela kliknij "**Transact**", a następnie **"Receive**.



![image](assets/fr/10.webp)





- Aplikacja wyświetla **pusty odbiór Address** (format SegWit v0, zaczynający się od `bc1q...`). Używanie nowego Address za każdym razem, gdy odbierasz Bitcoin, poprawia poufność.





- Opcje** :
    - (1) "Bitcoin": kliknij, aby wybrać przesyłkę onchain lub Liquid, a następnie wybierz zasób.
    - (2) Kliknij strzałki, aby wybrać kolejny nowy Address powiązany z tym zdaniem seed.
    - (3) Możesz także wybrać Address spośród już używanych/wyświetlanych, klikając trzy kropki w prawym górnym rogu, a następnie "List of Addresses" (Lista adresów)
    - (4) Aby zażądać określonej kwoty, kliknij trzy kropki w prawym górnym rogu, wybierz "Żądaj kwoty" i wprowadź żądaną kwotę. QR zostanie zaktualizowany, a identyfikator Address zostanie zastąpiony identyfikatorem URI płatności Bitcoin.




![image](assets/fr/11.webp)





- Udostępnij Address/URI, klikając "**Share**", kopiując tekst lub skanując kod QR.
- Weryfikacja**: Sprawdzenie Address udostępnionego odbiorcy w jak największym stopniu, aby uniknąć błędów lub ataków (np. złośliwego oprogramowania modyfikującego schowek).



### 5.2. wysyłanie bitcoinów





- Na ekranie głównym portfolio kliknij "**Transact**", a następnie **"Send "**:



![image](assets/fr/12.webp)





- Wprowadź szczegóły** :
    - (1) Wprowadź **Address odbiorcy**, przyklejając go lub skanując kod QR.
    - (2) Sprawdź aktywa i konto, z którego wysyłane są środki.
    - (3) Wskaż **kwotę** do wysłania. Możesz wybrać jednostkę: BTC, satoshis, USD, ...


Minimalna kwota (limit dush) na dzień 03/08/2025 wynosi 546 Sats.




    - (4) Wybierz **opłaty transakcyjne** :
        - Wybierz jedną z sugerowanych opcji (np. szybko, średnio, wolno) w zależności od pilności, a zostanie wyświetlony przybliżony czas transferu.
        - W przypadku niestandardowych opłat należy ręcznie dostosować liczbę Satoshi na vbytes (patrz [Mempool.space](https://Mempool.space/) dla stawek rynkowych).




![image](assets/fr/13.webp)





- Sprawdź** :
    - Sprawdź Address, kwotę i opłaty na ekranie podsumowania.
    - Błąd Address może spowodować nieodwracalną utratę środków. Należy uważać na złośliwe oprogramowanie, które modyfikuje schowek.



![image](assets/fr/14.webp)





- Potwierdzenie**: Przesuń przycisk "Wyślij", aby podpisać i rozpowszechnić transakcję.
- Kontynuacja**: W zakładce "Transakcja" Wallet transakcja pojawia się jako "oczekująca" do momentu potwierdzenia (od 1 do 6 potwierdzeń):



![image](assets/fr/15.webp)





- Dopóki transakcja nie zostanie potwierdzona, funkcja "Replace by fee" (patrz dodatek) umożliwia przyspieszenie jej obsługi poprzez zwiększenie opłat transakcyjnych:



![image](assets/fr/16.webp)




## Załączniki



### A1. Inne samouczki Blockstream



Korzystanie z Liquid Network



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Importowanie i śledzenie Wallet w trybie "Tylko oglądanie"



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Wersja na komputery stacjonarne



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Wyjaśnienie Replace-by-fee (RBF)



**Definicja**: Replace-by-fee (RBF) to funkcja sieci Bitcoin, która umożliwia nadawcy przyspieszenie potwierdzenia transakcji **onchain** poprzez wyrażenie zgody na uiszczenie wyższej opłaty.



**Limity** :




- RBF nie jest dostępny dla transakcji Liquid lub Lightning.
- Początkowa transakcja musi zostać oznaczona jako zgodna z RBF podczas jej tworzenia, co Blockstream App robi automatycznie.



**Więcej informacji:**




- [Glosariusz](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Najlepsze praktyki



Aby bezpiecznie i wydajnie korzystać z **Aplikacji Blockstream**, należy przestrzegać poniższych zaleceń. Pomogą one chronić środki, zoptymalizować transakcje i zachować poufność w sieciach **Bitcoin (onchain)**, **Liquid** i **Lightning**.





- Zabezpiecz swoją frazę odzyskiwania** :
 - Samouczek: Zapisywanie frazy Mnemonic



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Użyj bezpiecznego uwierzytelniania** :
 - Aktywuj **silny kod PIN** lub **uwierzytelnianie biometryczne** (odcisk palca lub rozpoznawanie twarzy), aby chronić dostęp do aplikacji.
 - Nigdy nie udostępniaj swojego kodu PIN ani danych biometrycznych.





- Chroń swoją prywatność** :
 - generate nowy Address dla każdego odbioru onchain lub Liquid w celu ograniczenia śledzenia na Blockchain.
 - Aktywuj funkcje "Zwiększona prywatność", "Tor" i "SPV".
 - Aby zapewnić maksymalną poufność, połącz swój Wallet z własnym węzłem Bitcoin za pośrednictwem serwera Electrum zamiast korzystać z węzła publicznego





- Wybierz sieć najlepiej dopasowaną do Twoich potrzeb** :
 - Onchain**: Preferowany w przypadku długoterminowego przechowywania lub transakcji o dużej wartości (opłaty nieistotne w stosunku do kwoty).
 - Liquid**: Służy do szybkich, tanich transferów o zwiększonej poufności.
 - Błyskawica**: Wybierz natychmiastowe, tanie przelewy dla małych kwot.





- Zawsze sprawdzaj adresy wysyłki**:
 - Przed wysłaniem środków należy dokładnie sprawdzić Address. Środki wysłane na niewłaściwy Address zostaną bezpowrotnie utracone. Używaj funkcji kopiuj/wklej lub skanowania kodów QR, nigdy nie kopiuj/modyfikuj Address ręcznie.





- Optymalizacja kosztów** :
 - W przypadku transakcji onchain należy wybrać odpowiednie opłaty (wolne, średnie, szybkie) w zależności od pilności i przeciążenia sieci.
 - Użyj Liquid lub Lightning dla małych ilości.





- Aktualizuj aplikację na bieżąco




### A4. Dodatkowe zasoby





- Oficjalne linki:**
 - [Oficjalna strona internetowa](https://blockstream.com/)**
 - [Wsparcie dla aplikacji mobilnej](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : dokumentacja i czat
 - [GitHub](https://github.com/Blockstream/green_android)**





- Block Explorers :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Błyskawica: **[1ML (Lightning Network)](https://1ml.com/)**





- Nauka i samouczki:** **[Plan ₿ Network](https://planb.network/)** :
 - Zabezpieczanie frazy odzyskiwania



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Glosariusz](https://planb.network/fr/resources/glossary/liquid-network)**



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Glosariusz](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb