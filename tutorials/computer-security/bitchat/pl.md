---
name: Bitchat
description: Zdecentralizowane, wolne od Internetu wiadomości do swobodnej komunikacji
---

![cover](assets/cover.webp)


![video](https://youtu.be/WfzcKAzgB9s)


*Ten samouczek wideo od BTC Sessions przeprowadzi Cię przez proces konfiguracji i korzystania z Bitchat!*


Bitchat wyłonił się z szybkiego prototypowania, w którym [@jack](https://primal.net/jack) opracował wstępną koncepcję podczas weekendowej sesji kodowania. [@calle](https://primal.net/calle) dołączył do projektu wkrótce potem, aby współtworzyć implementację Androida. Jack prowadzi obecnie rozwój wersji na iOS, podczas gdy Calle nadzoruje wersję na Androida przy wsparciu wielu innych współpracowników.


## Wprowadzenie: Czatuj swobodnie, bez sieci


Wyobraź sobie wysyłanie wiadomości, gdy internet przestaje działać, podczas klęski żywiołowej lub w miejscach, w których komunikacja jest ograniczona. Bitchat sprawia, że jest to możliwe. Jest to zdecentralizowana aplikacja do przesyłania wiadomości peer-to-peer, która pomija centralne serwery, pozwalając urządzeniom rozmawiać ze sobą bezpośrednio, całkowicie offline, za pomocą Bluetooth i sieci mesh. Zaprojektowany z myślą o prywatności i odporności, Bitchat jest idealny do stosowania w obszarach, w których tradycyjna łączność jest zawodna lub niedostępna - na przykład podczas katastrof, w odległych lokalizacjach lub dla tych, którzy chcą uniknąć nadzoru. W swoim rdzeniu Bitchat wykorzystuje kryptografię, aby zapewnić, że każda wiadomość jest zaszyfrowana od końca do końca, zweryfikowana i odporna na manipulacje.


W tym samouczku pokażemy, jak działa Bitchat i jak można go używać do prawdziwie prywatnej komunikacji offline.


## najważniejsze cechy


Bitchat umożliwia przesyłanie wiadomości offline dzięki tym [funkcjom](https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features):



- Kompatybilność między platformami**: Pełna kompatybilność z protokołami iOS i Android.
- Zdecentralizowana sieć mesh**: Automatyczne wykrywanie równorzędnych użytkowników i przekazywanie wiadomości w trybie multi-hop przez Bluetooth Low Energy (BLE)
- Kompleksowe szyfrowanie**: Wymiana kluczy X25519 + AES-256-GCM dla prywatnych wiadomości
- Czaty oparte na kanałach**: Wiadomości grupowe oparte na tematach z opcjonalną ochroną hasłem
- Store & Forward**: Wiadomości buforowane dla użytkowników offline i dostarczane po ponownym nawiązaniu połączenia
- Prywatność przede wszystkim**: Brak kont, brak numerów telefonów, brak trwałych identyfikatorów
- Polecenia w stylu IRC: Znany interfejs w stylu `/join, /msg, /who`.
- Przechowywanie wiadomości**: Opcjonalne zapisywanie wiadomości w całym kanale kontrolowane przez właścicieli kanałów
- Awaryjne czyszczenie**: Trzykrotne dotknięcie logo w celu natychmiastowego wyczyszczenia wszystkich danych
- Nowoczesny interfejs użytkownika Androida**: Jetpack Compose z Material Design 3
- Ciemne/jasne motywy**: Estetyka inspirowana terminalem dopasowana do wersji iOS
- Optymalizacja baterii**: Adaptacyjne skanowanie i zarządzanie energią


## 1️⃣ Jak działa Bitchat - po prostu


Bitchat umożliwia wysyłanie wiadomości do pobliskich telefonów bezpośrednio przez Bluetooth (`BLE` jak poniżej), bez konieczności korzystania z Internetu lub sygnału komórkowego. Po rozpoczęciu czatu telefony wykonują bezpieczny uścisk dłoni, aby utworzyć unikalny, tymczasowy klucz szyfrowania dla rozmowy. Każda wiadomość jest chroniona za pomocą szyfrowania end-to-end, a dla każdej z nich używany jest nowy klucz, aby zapewnić, że poprzednie wiadomości pozostaną bezpieczne, nawet jeśli telefon zostanie później przejęty. Wreszcie, aplikacja dzieli wiadomości na małe części i miesza je z losowymi fałszywymi danymi, aby ukryć aktywność użytkownika w wiadomościach. W przypadku bezpośrednich czatów między urządzeniami działa to tylko w zasięgu do ~100 m. Przypomina to przekazywanie zaszyfrowanych notatek w zatłoczonym pokoju - urządzenia szepczą bezpośrednio do siebie, niszcząc klucze po każdej wiadomości.


Bitchat umożliwia również dołączanie do czatów opartych na lokalizacji przy użyciu protokołu Nostr i `#geohashes`. Geohash to krótki kod, taki jak `#u33d`, który reprezentuje określony obszar geograficzny, od pojedynczej dzielnicy, aż po całe miasto lub region. Możesz "teleportować się" do dowolnego pokoju czatu geohash na całym świecie, po prostu wprowadzając jego tag. Wiadomości są wysyłane przez zdecentralizowaną sieć przekaźników, która chroni dokładną lokalizację użytkownika. Co więcej, za każdym razem, gdy dołączasz do pokoju geohash, otrzymujesz nową, tymczasową tożsamość, dodając dodatkową warstwę prywatności do rozmów opartych na lokalizacji.


Więcej szczegółów technicznych można znaleźć w [oficjalnym dokumencie](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).


## 2️⃣ Instalacja i konfiguracja


### Gdzie kupić Bitchat?


Możesz zainstalować Bitchat poprzez:



- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (dla urządzeń z systemem iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (dla urządzeń z systemem Android)


Użytkownicy Androida mają również alternatywne opcje:



- Pobierz APK bezpośrednio ze strony [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) lub
- Instalacja przez kompatybilny z Nostr [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)


![image](assets/en/01.webp)


**Uwaga**: _Ten samouczek skupia się przede wszystkim na implementacji w systemie Android. Wersja na iOS może się różnić


### Proces konfiguracji


Po instalacji otwórz Bitchat, aby zobaczyć początkowy ekran uprawnień. Oto, co należy zrobić:


1. **Udziel tych wymaganych uprawnień:**


   - Dostęp przez Bluetooth** (do wykrywania pobliskich użytkowników Bitchat)
   - Precyzyjna lokalizacja** (Android wymaga tej funkcji do działania Bluetooth)
   - Powiadomienia** (aby otrzymywać powiadomienia o prywatnych wiadomościach)

2. **Wyłącz optymalizację baterii**:


   - Dzięki temu Bitchat może działać w tle
   - Utrzymuje połączenia sieciowe mesh w sposób ciągły


Stuknij w `Udziel uprawnienia`, postępuj zgodnie z `prompts` i `Wyłącz optymalizację baterii`, aby przejść do następnego ekranu.


![image](assets/en/02.webp)


Witamy na ekranie głównym Bitchat. Zorientujmy się:


### Ustawienia


Po pierwsze. Menu ustawień można otworzyć, dotykając logo `Bitchat`.  Dostępne są następujące opcje:



- Ustaw "wygląd" (system/jasny/ciemny).
- włączenie funkcji `Dowód pracy` dla geohash w celu odstraszania spamu (opcjonalnie)
- Włącz `Tor`, aby zwiększyć prywatność.


![image](assets/en/16.webp)


### Ustaw swoją tożsamość


Stuknij pole `bitchat/anonXXXX` u góry, aby wybrać swoją nazwę użytkownika. W ten sposób inni będą cię widzieć zarówno w trybie Bluetooth, jak i internetowym. Możesz na przykład zmienić "anon2022" na wybraną przez siebie nazwę użytkownika.


![image](assets/en/03.webp)


### Wybór kanałów sieciowych


Użyj menu `#location channels` (po prawej stronie nazwy użytkownika), aby przełączać się między typami połączeń:



- BLE Mesh***: Domyślny tryb Bluetooth (bez Internetu, zasięg od 10 do 50 metrów)
- #geohashes**: Internetowe społeczności geograficzne wykorzystujące [protokół Nostr](https://nostr.com/)


Po wybraniu trybu `#geohashes`, Bitchat integruje się z protokołem Nostr, aby włączyć społeczności geograficzne. Twoje wiadomości są publikowane do `zdecentralizowanych przekaźników Nostr`, a nie do sieci peer-to-peer Bitchat, umożliwiając szersze, ale filtrowane lokalizacyjnie rozmowy. Co najważniejsze, klucze tożsamości Bitchat kryptograficznie podpisują wszystkie zdarzenia Nostr w celu utrzymania uwierzytelniania, podczas gdy znaczniki geohash (takie jak `#u4pruyd` dla sąsiedztwa) filtrują wiadomości do wybranego poziomu precyzji. Oznacza to, że możesz uczestniczyć w lokalnych dyskusjach bez ujawniania dokładnych współrzędnych, choć wymagany jest dostęp do Internetu.


![image](assets/en/04.webp)


### Monitorowanie rówieśników

licencja: CC-BY-SA-V4

Licznik peer pokazuje użytkowników:



- W pobliżu (BLE Mesh) lub
- W strefie geohash (#geohashes)


![image](assets/en/05.webp)


## 3️⃣ Globalny czat i prywatne wiadomości


Bitchat zapewnia dwa różne tryby komunikacji dostosowane do różnych potrzeb:



- Kanały publiczne:** Do otwartych rozmów z innymi. Możesz łączyć się za pośrednictwem lokalnej sieci BLE mesh dla pobliskich użytkowników lub za pośrednictwem globalnego #geohash dla społeczności internetowych opartych na lokalizacji.
- Prywatne wiadomości:** Do bezpiecznych rozmów jeden na jeden. Ustanawiają one bezpośrednie, szyfrowane połączenie, aby zachować poufność wymiany.


Zrozumienie obu trybów pomoże ci w prowadzeniu rozmów.


### Kanały publiczne: Centrum społeczności


Menu `#location channels` (prawy górny róg) kontroluje widoczność publiczną. Wybranie opcji `mesh` łączy cię ze wszystkimi pobliskimi użytkownikami za pośrednictwem sieci BLE mesh, zazwyczaj z urządzeniami znajdującymi się w odległości 10-50 metrów. Tworzy to otwarte forum, na którym wiadomości są nadawane do wszystkich w zasięgu, idealne do ogłaszania wydarzeń lub lokalnych alertów.


Aby uzyskać szerszy zasięg geograficzny, wybierz dowolny tag `#geohash`, aby dołączyć do społeczności internetowych filtrowanych według lokalizacji. Kanały te wykorzystują przekaźniki protokołu Nostr, umożliwiając komunikację między miastami lub regionami przy jednoczesnym zachowaniu znaczenia opartego na lokalizacji. Twoje wiadomości pojawiają się na żywo innym osobom na tym samym kanale, a nowi uczestnicy automatycznie widzą historię ostatnich wiadomości po dołączeniu.


![image](assets/en/06.webp)


### Prywatne rozmowy: Bezpieczne i szyfrowane


Aby rozpocząć prywatną rozmowę, stuknij bezpośrednio w dowolną `nazwę użytkownika` wyświetlaną w `Peers Overview`. Możesz także stuknąć w ikonę `gwiazdki`, aby oznaczyć tego użytkownika jako ulubionego, co sprawi, że będzie on widoczny na Twojej liście kontaktów, nawet gdy jest offline.


![image](assets/en/07.webp)


Bitchat automatycznie inicjuje `security handshake` po rozpoczęciu prywatnego czatu. Urządzenia wymieniają efemeryczne klucze, aby utworzyć zaszyfrowany tunel specjalnie dla rozmowy. Proces ten zapewnia, że wszystkie wiadomości i udostępniane pliki pozostają poufne dzięki ciągłemu szyfrowaniu end-to-end. Prywatne wiadomości obsługują udostępnianie tekstu i plików.


![image](assets/en/08.webp)


## 4️⃣ Dodatkowe funkcje


Możesz uzyskać natychmiastowy dostęp do panelu akcji, wpisując `/` w dowolnym miejscu w Bitchat. Spowoduje to wyświetlenie menu poleceń dla szybkich akcji.



- Zarządzanie połączeniami**: `Odblokuj użytkowników` lub `Odblokuj użytkowników równorzędnych`
- Kontrolki kanałów**: `Pokaż kanały` lub `Dołącz/utwórz kanał`
- Interakcje społeczne**: `wysłanie ciepłego uścisku` lub `poklepanie pstrągiem` 🎣
- Obsługa czatu**: `Wyczyść wiadomości czatu`
- Narzędzia prywatności**: `Sprawdź, kto jest online` lub `Wyślij prywatną wiadomość`


Polecenia wykonują się natychmiast - jak `/block Satoshi`, aby uciszyć krytyków lub `/hug Hal`, aby szerzyć pozytywne nastawienie 🫂.


![image](assets/en/09.webp)


## 5️⃣ Tworzenie kanału


Kanały w Bitchat umożliwiają zorganizowaną komunikację wokół tematów, lokalizacji lub społeczności. Aby utworzyć własny kanał, wykonaj poniższe czynności:


### Krok 1: Utwórz kanał


Aby utworzyć kanał, wpisz `/j` lub `/join`, a następnie `/nazwę kanału` na dowolnym czacie (np. `/j <nazwa kanału>`). Po utworzeniu pojawi się nowa ikona ⧉` wskazująca nowy kanał. Inni użytkownicy mogą dołączyć wpisując to samo polecenie (np. `/j bitchat_tutorial`).


![image](assets/en/10.webp)


### Krok 2: Konfiguracja ustawień


Oprócz poleceń domyślnych, w ramach kanału dostępne są następujące ustawienia:



- `/save` do zapisywania wiadomości lokalnie
- `/transfer`, aby przenieść własność kanału i
- `/pass`, aby zmienić hasło kanału.


W przypadku społeczności prywatnych polecenie to włącza ochronę hasłem, wymagając od zatwierdzonych członków wprowadzenia niestandardowego hasła przed dołączeniem.


## 6️⃣ Tryb paniki


Porozmawiajmy teraz o "trybie paniki": trzykrotne dotknięcie logo "Bitchat" inicjuje całkowite wyczyszczenie wszystkich lokalnych wiadomości i danych w aplikacji. Jest to najlepsze zabezpieczenie prywatności, idealne w sytuacjach wymagających natychmiastowej dyskrecji.


**Ważne przypomnienie:** _Tryb paniki jest trwały. Po jego aktywacji nie można odzyskać danych. Używaj ostrożnie


![image](assets/en/11.webp)


## 7️⃣ Geohashes


Kanały Geohash umożliwiają ukierunkowane rozmowy w oparciu o `lokalizacje geograficzne`, a nie tradycyjne połączenia sieciowe. Ta funkcja przekształca bitcoat w narzędzie komunikacji uwzględniające lokalizację, idealne do lokalnej koordynacji, budowania społeczności i dyskusji specyficznych dla lokalizacji.


### Jak działają `#geohashes


System dzieli świat na kwadraty siatki przy użyciu [systemu Geohash](https://en.wikipedia.org/wiki/Geohash), gdzie każdy znak w skrócie oznacza większą precyzję:



- Poziom 4** (np. `u33d`): Obejmuje około 25 km × 25 km - idealny do dyskusji w całym mieście
- Poziom 6** (np. `u33d8z`): Obejmuje około 1,2 km × 1,2 km - precyzja sąsiedztwa
- Poziom 8** (np. `u33d8z1k`): Obejmuje około 150 m × 150 m - dokładność segmentu ulicy


Precyzyjny wybór równoważy prywatność z użytecznością: wyższe poziomy tworzą bardziej ekskluzywne strefy, ale dokładniej ujawniają Twoją lokalizację.


### Dołączanie do kanałów `#geohash


1. Dostęp do menu `#location channels`.

2. Wybierz żądany poziom precyzji i wprowadź `#geohash` (np. #u33d)

3. Naciśnij przycisk `Teleport`, aby dołączyć do kanału `#location`.


![image](assets/en/12.webp)


Alternatywnie, możesz dotknąć ikony `map`, aby użyć widoku mapy do określenia poziomu precyzji i dotknąć `select`, aby dołączyć do kanału `#location`.


![image](assets/en/13.webp)


**Ważne przypomnienie**: funkcjonalność _#geohash wymaga aktywnego połączenia z Internetem - w przeciwieństwie do BLE mesh, który działa w trybie offline przez Bluetooth


## 8️⃣ Heatmaps


Mapy cieplne to fajny sposób na odkrywanie wydarzeń i kanałów Bitchat na całym świecie. [Bitmap](https://bitmap.lat/) wizualizuje i śledzi anonimowe, oparte na lokalizacji wiadomości w sieci Nostr, wyświetlając efemeryczne wydarzenia Nostr. Rzuć okiem i dołącz do kanałów i czatów specyficznych dla lokalizacji.


![image](assets/en/15.webp)


## wnioski


Bitchat umożliwia bezpieczną, zdecentralizowaną komunikację w scenariuszach, w których tradycyjne wiadomości zawodzą. Jest w stanie działać bez infrastruktury internetowej przy użyciu sieci BLE mesh, dzięki czemu nadaje się do protestów, stref katastrof i odległych obszarów, w których łączność jest ograniczona lub cenzurowana. Aplikacja zapewnia prywatność dzięki szyfrowaniu kluczem efemerycznym, kanałom lokalizacji opartym na geohash i usuwaniu danych w trybie paniki.


Aplikacja jest wciąż na wczesnym etapie rozwoju, ale już teraz wygląda obiecująco. Użytkownicy powinni spodziewać się sporadycznych błędów i zgłaszać je za pośrednictwem [GitHub](https://github.com/permissionlesstech/bitchat-android/issues). Planowane są ulepszenia, w tym integracja `ecash` dla prywatnych transakcji w aplikacji przy użyciu protokołu Cashu.


![image](assets/en/14.webp)


## zasoby Bitchat


[Github](https://github.com/permissionlesstech) | [Website ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)