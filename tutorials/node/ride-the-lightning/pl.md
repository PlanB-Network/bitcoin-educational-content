---
name: Ride The Lightning (RTL)
description: Użyj Ride The Lightning (RTL) do zarządzania węzłem Lightning
---
![cover](assets/cover.webp)


## 1. Wprowadzenie



**Ride The Lightning (RTL)** to kompletna aplikacja internetowa Interface do zarządzania węzłem Lightning Network. Ta samoobsługowa aplikacja internetowa oferuje **kokpit Lightning** dostępny z poziomu przeglądarki. RTL współpracuje ze wszystkimi głównymi implementacjami Lightning (LND, Core Lightning/CLN i Eclair) i zapewnia pełną kontrolę nad węzłem i kanałami. RTL jest domyślnie zintegrowany z wieloma gotowymi rozwiązaniami dla węzłów (RaspiBlitz, MyNode, Umbrel itp.).



**Bez graficznego interfejsu, węzłami Lightning można zarządzać tylko za pomocą przyjaznych dla użytkownika poleceń CLI. RTL upraszcza te operacje dzięki ergonomicznemu interfejsowi. Oto główne zastosowania:**





- **Wyświetlanie kanałów i węzłów** - Pulpit nawigacyjny wyświetla saldo On-Chain, płynność Lightning (lokalną/zdalną), stan synchronizacji, alias węzła i nie tylko. Można wyświetlić listę kanałów, pojemność, dystrybucję lokalną/zdalną i status. RTL oferuje kontekstowe pulpity nawigacyjne do analizowania aktywności pod różnymi kątami.





- **Błyskawiczne zarządzanie kanałami** - Otwieranie/zamykanie kanałów za pomocą kilku kliknięć. RTL pozwala połączyć się z peerem i otworzyć kanał bez polecenia. Możesz dostosować opłaty za routing, wyświetlić wynik salda lub zainicjować cykliczne równoważenie w celu zrównoważenia środków między kanałami.





- **Śledź i dokonuj płatności** - RTL zarządza transakcjami Lightning: wysyłaj płatności za pomocą faktur, generuj faktury do odbioru, śledź transakcje (płatności, routing) ze szczegółową historią. Interface analizuje również routing, aby zobaczyć, które płatności przechodzą przez węzeł.





- **Zarządzanie Wallet On-Chain i tworzenie kopii zapasowych** - Zakładka On-Chain umożliwia tworzenie adresów generate i wysyłanie transakcji. RTL ułatwia zapisywanie kanałów poprzez eksport pliku SCB dla LND, z automatyczną aktualizacją dla każdej modyfikacji kanału.



Krótko mówiąc, RTL to **potężny pulpit nawigacyjny dla Lightning Network**, oferujący edukacyjny Interface do codziennego pilotowania węzła. Ten samouczek poprowadzi Cię przez jego instalację i wykorzystanie do zarządzania kanałami i płatnościami.



## 2. Techniczne działanie RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Zanim przejdziemy do szczegółów, warto pokrótce zrozumieć **jak RTL współdziała z węzłem Lightning** na poziomie technicznym.



**Ogólna architektura:** RTL to aplikacja internetowa zbudowana przy użyciu Node.js (backend) i Angular (frontend). Mówiąc konkretnie, RTL działa jako mały lokalny serwer WWW (domyślnie na porcie 3000), który komunikuje się z implementacją Lightning za pośrednictwem interfejsów API. W zależności od typu :





- W przypadku **LND** RTL używa interfejsu API REST LND (port 8080) do wykonywania poleceń Lightning. Połączenie jest zabezpieczone przez TLS i wymaga pliku **admin macaroon** LND do uwierzytelnienia.





- Z **Core Lightning (CLN)**, RTL używa albo API REST dostarczonego przez *c-lightning-REST*, albo **access run** poprzez wtyczkę `commando`. Rozwiązania takie jak Umbrel automatycznie konfigurują te Elements.





- W przypadku **Eclair** RTL łączy się z Eclair REST API przy użyciu skonfigurowanego hasła uwierzytelniania.



**Konfiguracja i bezpieczeństwo:** RTL jest konfigurowany za pomocą pliku JSON (`RTL-Config.json`), w którym definiuje się port sieciowy, hasło dostępu i informacje o połączeniu z węzłem. Sieć Interface jest chroniona loginem/hasłem (domyślne `password` do zmiany) i obsługuje 2FA. Domyślnie RTL działa jako lokalny HTTP (`http://localhost:3000`), ale w przypadku dostępu zdalnego zawsze należy używać bezpiecznego połączenia (HTTPS przez reverse-proxy, Tor lub VPN).



Krótko mówiąc, RTL to dodatkowy komponent, który łączy się z węzłem za pośrednictwem bezpiecznych interfejsów API, wymaga odpowiednich tokenów dostępu i oferuje własne zabezpieczenia Layer. Ta modułowa architektura pozwala nawet zarządzać **kilkoma węzłami Lightning za pomocą jednej instancji RTL**.



## 3. Instalacja RTL



Ponieważ RTL jest dystrybuowany jako oprogramowanie open-source, istnieje kilka sposobów na zainstalowanie go w systemie. W tej sekcji omówimy dwa główne podejścia: instalację ręczną i instalację za pośrednictwem Umbrel.



### Metoda ręczna



Ręczna instalacja jest odpowiednia, jeśli chcesz zachować szczegółową kontrolę lub jeśli integrujesz RTL z niestandardową konfiguracją. Poniższe kroki dotyczą węzła LND z systemem Linux (np. Raspberry Pi lub VPS z systemem Ubuntu/Debian), ale są podobne dla CLN/Eclair.



**Wymagania wstępne:** upewnij się, że masz **zsynchronizowany** węzeł Bitcoin i działający węzeł Lightning (LND, CLN lub Eclair) na komputerze. RTL nie zawiera węzła Lightning jako takiego, łączy się z istniejącym węzłem. Potrzebny jest również **Node.js** (zalecana wersja 14+). Możesz sprawdzić za pomocą `node -v` lub zainstalować Node z oficjalnej strony (https://nodejs.org/en/download/) lub menedżera pakietów.



Główne etapy instalacji to :



**Pobierz kod RTL**: Sklonuj oficjalne repozytorium RTL GitHub w wybranym przez siebie katalogu. Na przykład:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Instalacja zależności**: RTL jest aplikacją Node.js, więc należy zainstalować jej wymagane moduły. W folderze RTL uruchom :



```bash
npm install --omit=dev --legacy-peer-deps
```



To polecenie instaluje niezbędne pakiety NPM (ignorując zależności deweloperskie). Opcja `--legacy-peer-deps` jest zalecana w celu uniknięcia możliwych konfliktów zależności Node.



**RTL-Config**: Gdy zależności są już na miejscu, przygotuj plik konfiguracyjny. Skopiuj/zmień nazwę pliku `Sample-RTL-Config.json` w katalogu głównym projektu na `RTL-Config.json`. Otwórz go w swoim :





- **Hasło UI**: wybierz bezpieczne hasło i wprowadź je w `multiPass` (zamiast domyślnego `"password"`).
- **Port**: domyślnie `3000`. Możesz go zmienić, jeśli ten port jest już zajęty na twoim komputerze.
- **Node**: w sekcji `nodes[0]` dostosuj parametry dla swojego węzła:
     - `lnNode`: opisowa nazwa węzła (np. `"LND Node Maison"`).
     - lnImplementation`: `"LND"` (lub odpowiednio `"CLN"`/`"ECL"`).
     - Pod `authentication` (uwierzytelnianie):
       - macaroonPath`: określa pełną ścieżkę do folderu zawierającego administratora macaroon LND.
       - `configPath`: ścieżka do pliku konfiguracyjnego węzła (`LND.conf` dla LND).
     - W `ustawieniach`:
       - `fiatConversion`: ustaw na `true` jeśli chcesz konwersji waluty fiat.
       - `unannouncedChannels`: ustaw na `true`, aby zobaczyć niezapowiedziane kanały.
       - themeColor` i `themeMode`: Dostosowanie Interface.
       - channelBackupPath`: ścieżka dla kopii zapasowych kanału LND.
       - `lnServerUrl`: Adres URL węzła Lightning (np. `https://127.0.0.1:8080`).



**Uruchom serwer RTL**: W folderze RTL uruchom :



```bash
node rtl
```



Aplikacja uruchamia się i jest dostępna pod adresem `http://localhost:3000`.



**(Opcjonalnie) Uruchom RTL jako usługę**: W celu automatycznego uruchomienia utwórz usługę systemd :



Aby to zrobić:




- Otwórz terminal na swoim komputerze.
- Utwórz nowy plik usługi za pomocą poniższego polecenia (zastąp `nano` swoim ulubionym edytorem):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Skopiuj i wklej poniższą zawartość do tego pliku:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Zastąp `/path/to/RTL/rtl` rzeczywistą ścieżką do pliku `rtl` na komputerze, a `<your_user>` nazwą użytkownika systemu Linux.
- Zapisz i zamknij plik.
- Przeładowanie konfiguracji systemd:


```bash
sudo systemctl daemon-reload
```




- Aktywuj i uruchom usługę RTL:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL będzie teraz uruchamiany automatycznie przy każdym ponownym uruchomieniu komputera. Jego status można sprawdzić za pomocą :


```bash
sudo systemctl status RTL
```



### Instalacja przez Umbrel



Jeśli używasz [Umbrel](https://getumbrel.com), instalacja RTL jest znacznie prostsza:





- Dostęp do Interface Umbrel (zwykle przez `http://umbrel.local`)
- Przejdź do **App Store**
- Szukaj "Ride The Lightning"



**Ważna uwaga: w Umbrel App Store dostępne są dwie oddzielne aplikacje RTL:**




- **Ride The Lightning** (dla LND): do użytku z domyślnym węzłem błyskawic Umbrel (LND).
- **Ride The Lightning (Core Lightning)**: używaj tylko wtedy, gdy zainstalowałeś aplikację *Core Lightning* na Umbrel i chcesz zarządzać tym węzłem za pomocą RTL.



*Każda wersja RTL jest wstępnie skonfigurowana do dialogu z odpowiednią implementacją (LND lub Core Lightning). Jeśli nie zmieniłeś węzła Lightning, po prostu wybierz klasyczną wersję LND*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Kliknij na **Install**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Ważne: Po instalacji RTL wyświetli ekran z domyślnym hasłem.** **Skopiuj i zapisz to hasło** - będzie ono potrzebne do zalogowania się do Interface RTL. Hasło to będzie wyświetlane przy każdym uruchomieniu RTL, dopóki nie zaznaczysz opcji "Nie pokazuj go ponownie".



Umbrel automatycznie zajmuje się :




- Pobierz i skonfiguruj RTL
- Konfigurowanie dostępu do węzła Lightning
- Zarządzanie aktualizacjami
- Zabezpieczenie dostępu do Interface



Po zainstalowaniu aplikacja pojawi się w menu *Apps* na Umbrel. Kliknij na **Ride The Lightning**, aby ją uruchomić.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



Na ekranie logowania wprowadź skopiowane wcześniej hasło. Po zalogowaniu Interface web RTL będzie dostępny bezpośrednio z pulpitu nawigacyjnego Umbrel, bez konieczności dodatkowej konfiguracji!



## 4. Wprowadzenie i wykorzystanie Interface RTL



Teraz, gdy RTL jest już uruchomiony, przyjrzyjmy się jego sieci Interface i kluczowym funkcjom. Przejdziemy przez różne sekcje aplikacji, aby dać ci pełny przegląd.



### Główny panel sterowania



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Natychmiast po zalogowaniu uzyskujesz dostęp do **głównego pulpitu nawigacyjnego**, który zapewnia przegląd węzła Lightning. Ta strona centralizuje najważniejsze informacje:




- Całkowite saldo Lightning
- Dostępne saldo On-Chain
- Podział płynności (przychodzące/wychodzące)
- Szybki dostęp do wysyłania i odbierania Satss za pośrednictwem węzła Lightning



### Zarządzanie funduszami On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



Zakładka **On-Chain** umożliwia zarządzanie bitcoinami bezpośrednio w głównym łańcuchu:




- Wyświetlanie salda w różnych jednostkach (Sats, BTC, USD)
- Pełna lista transakcji
- Address generacji Taproot (P2TR), P2SH (NP2WKH) lub Bech32 (P2WKH)
- Zarządzanie UTXO, odbieranie i wysyłanie bitcoinów



### Lightning: szczegółowa prezentacja podmenu



Interface RTL posiada menu boczne dedykowane dla Lightning Network, łączące wszystkie niezbędne funkcje do zarządzania węzłem. Poniżej znajdują się szczegóły każdego podmenu, w kolejności przedstawionej na zrzucie ekranu:



#### 1. Rówieśnicy/kanały



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



To podmenu umożliwia :




- Wyświetlanie listy połączonych urządzeń równorzędnych i otwartych lub oczekujących kanałów Lightning.
- Dodaj nowego peera (połącz się z innym węzłem Lightning).
- Otwieranie, zamykanie lub zarządzanie istniejącymi kanałami.
- Wyświetl szczegóły każdego kanału: pojemność, salda lokalne/zdalne, status, historię transakcji, wynik salda itp.



#### 2. Transakcje



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



W tym podmenu można :




- Wyślij płatności Lightning (przez Invoice).
- generate i zarządzanie fakturami w celu otrzymywania płatności.
- Wyświetlanie pełnej historii wysłanych i otrzymanych płatności wraz ze szczegółami (kwota, data, status, opłaty, liczba pominięć itp.).



#### 3. Routing



To podmenu wyświetla :




- Płatności kierowane przez węzeł dla innych użytkowników Lightning Network.
- Statystyki routingu: liczba przekazanych transakcji, naliczone opłaty, napotkane błędy.
- Możliwość eksportu historii w celu zaawansowanej analizy.



#### 4. Odroczenia



To podmenu oferuje :




- Szczegółowe raporty dotyczące aktywności węzła Lightning.
- Wykresy i tabele dotyczące kanałów, płatności, opłat, pojemności itp.
- Narzędzia pozwalające lepiej zrozumieć wydajność węzła.



#### 5. Wyszukiwanie wykresów



To podmenu umożliwia :




- Poznaj topologię Lightning Network.
- Wyszukiwanie określonych węzłów lub kanałów.
- Uzyskanie informacji na temat łączności i ogólnej przepustowości sieci.



#### 6. Podpisz/weryfikuj



To podmenu oferuje :




- Możliwość podpisania wiadomości kluczem węzła (dowód Ownership).
- Weryfikacja podpisu w celu uwierzytelnienia wiadomości z innych węzłów.



#### 7. Kopia zapasowa



To podmenu jest przeznaczone do tworzenia kopii zapasowych:




- Eksport pliku kopii zapasowej kanału (SCB dla LND).
- W razie potrzeby przywróć konfigurację lub kanały.
- Wskazówki dotyczące zabezpieczania kopii zapasowych.



#### 8. Węzeł/sieć



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



W tym podmenu znajdują się :




- Pełne podsumowanie statusu węzła Lightning: alias, wersja, kolor, status synchronizacji.
- Statystyki kanałów (aktywne, oczekujące, zamknięte), całkowita przepustowość, łączność.
- Informacje o globalnym Lightning Network i pozycji węzła w nim.



### Usługi: Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz to przyjazna dla prywatności, bezobsługowa usługa Exchange, która konwertuje bitcoiny między Lightning Network i Blockchain Bitcoin (On-Chain). Oferuje ona dwa rodzaje operacji: Reverse Submarine Swap (**Swap Out**) i Submarine Swap (**Swap In**).



#### Swap Out (odwrócona zamiana łodzi podwodnych)



Swap Out konwertuje Satss dostępne na Lightning Network na bitcoiny On-Chain. Mechanizm ten jest przydatny, gdy węzłowi kończy się przepustowość przychodząca lub gdy chcesz odzyskać środki z On-Chain Address. Proces ten działa w następujący sposób:




- Użytkownik wybiera kwotę do wymiany
- Węzeł wysyła płatność Lightning do Boltza
- W Exchange Boltz blokuje równoważną kwotę w bitcoinach On-Chain
- Po potwierdzeniu transakcji użytkownik może odebrać środki, ujawniając sekret wykorzystany w wymianie



Proces ten ma charakter nieizolacyjny, a Boltz nigdy nie przechowuje środków użytkownika.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (Zamiana łodzi podwodnych)



Z drugiej strony, funkcja Swap In umożliwia ponowne wstrzyknięcie środków On-Chain do Lightning Network. Jest to szczególnie przydatne do przywracania przepustowości wyjściowej na kanałach. Procedura jest następująca:




- Użytkownik wysyła bitcoiny do określonego Address wygenerowanego przez Boltz
- Środki te mogą zostać uwolnione przez Boltza tylko wtedy, gdy zapłaci on Lightning Invoice wygenerowany przez węzeł użytkownika
- Po opłaceniu Invoice środki są dostępne w kanale Lightning, zwiększając wydajność wyjściową węzła



![Configuration d'un swap-in](assets/fr/12.webp)



Te dwa mechanizmy umożliwiają efektywne zarządzanie płynnością kanału Lightning, przy jednoczesnym zachowaniu suwerenności użytkownika nad jego środkami.



### Konfiguracja i dostosowywanie



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



Zakładka **Konfiguracja węzła** umożliwia dostosowanie doświadczenia:




- Aktywacja niezapowiedzianych kanałów
- Dostosuj wyświetlanie sprzedaży
- Konfiguracja Block explorer
- Regulacja Interface



### Dokumentacja i pomoc



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Wreszcie, sekcja **Pomoc** oferuje kompleksową dokumentację dotyczącą :




- Konfiguracja początkowa
- Zarządzanie rówieśnikami i kanałami
- Płatności i transakcje
- Kopie zapasowe i przywracanie
- Raporty i statystyki
- Podpisy i weryfikacje
- Parametry węzła i aplikacji



Ten wszechstronny Interface umożliwia wydajne zarządzanie węzłem Lightning, od podstawowych operacji po zaawansowane funkcje, a wszystko to w intuicyjnym, dobrze zorganizowanym Interface.



## 5. Zaawansowane przypadki użycia i bezpieczeństwo



W tej sekcji dowiesz się, co musisz wiedzieć, aby przejść dalej z RTL i zabezpieczyć swój węzeł Lightning:



### Monitorowanie i rozwiązywanie problemów



Aby monitorować węzeł, można eksportować dane RTL (logi, CSV) i wyświetlać je w narzędziach takich jak Grafana. W przypadku wystąpienia problemu (zablokowana płatność, nieaktywny kanał) należy sprawdzić logi LND/CLN i użyć poleceń diagnostycznych (`lncli listchannels`, `lncli pendingchannels` itp.). RTL oferuje również dzienniki Interface do monitorowania zdarzeń routingu.



### Bezpieczny dostęp zdalny



Nigdy nie wystawiaj RTL bezpośrednio w Internecie. Daj pierwszeństwo :




- **VPN** (np. Tailscale) dla prywatnego, szyfrowanego dostępu
- **Tor** dla bezpiecznego, anonimowego dostępu
- Odwrotne proxy **HTTPS** (Nginx/Caddy) tylko jeśli wiesz jak je skonfigurować



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Dobre praktyki bezpieczeństwa





- **Chroń swój dostęp**: nigdy nie udostępniaj admin.macaroon ani hasła RTL. Ogranicz uprawnienia do wrażliwych plików.
- **Regularne kopie zapasowe**: eksport pliku kopii zapasowej kanału (SCB) po każdej modyfikacji i przechowywanie go poza węzłem.
- **Aktualizacje**: aktualizuj RTL, swój węzeł i Umbrel o najnowsze poprawki bezpieczeństwa.
- **Poufność**: anonimizuj logi i zrzuty ekranu przed ich udostępnieniem. Nigdy nie udostępniaj publicznie swoich sald ani list użytkowników.
- **Pojedynczy dostęp**: RTL nie obsługuje wielu użytkowników. Nie należy współdzielić dostępu administratora. Aby uzyskać dostęp tylko do odczytu, w razie potrzeby użyj dedykowanego makarona.



Stosując te zasady, można znacznie ograniczyć ryzyko i zachować kontrolę nad węzłem Lightning.



## 7. Wnioski



**Ride The Lightning** jest niezbędnym narzędziem do efektywnego zarządzania węzłem Bitcoin/Lightning, niezależnie od tego, czy jesteś początkującym, czy zaawansowanym użytkownikiem. Zapewnia przejrzysty Interface do kontrolowania kanałów, płatności i stanu węzła, jednocześnie pogłębiając zrozumienie Lightning Network.



RTL wyróżnia się kompatybilnością z wieloma wdrożeniami, zaawansowanymi funkcjami (równoważenie, zamiany, raporty) i podejściem pedagogicznym. W przypadku prostych potrzeb wystarczy Interface Umbrel lub Wallet mobile, ale RTL ma doskonały sens w przypadku aktywnego, zoptymalizowanego zarządzania węzłami.



Aby dowiedzieć się więcej :




- Oficjalna strona RTL: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Dyskusje techniczne, ogłoszenia o projektach, opinie i zasoby edukacyjne
- **Forum społeczności Umbrel**: [community.getumbrel.com](https://community.getumbrel.com) - Oficjalne forum z dedykowaną sekcją Bitcoin/Lightning, poradnikami i rozwiązaniami typowych problemów
- **Deweloperzy Lightning Network**: [github.com/lightning](https://github.com/lightning) - Oficjalne repozytorium GitHub do śledzenia rozwoju i udostępniania kodu źródłowego
- **Stack Exchange Bitcoin**: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Techniczne Q&A z deweloperami i zaawansowanymi użytkownikami



Krótko mówiąc, RTL zapewnia pełną kontrolę nad węzłem Lightning w nowoczesnym, w pełni funkcjonalnym Interface.



**Źródła :** Oficjalna strona RTL; RTL GitHub; Umbrel App Store; Społeczność Umbrel; Zasoby Plan ₿ Academy.



Aby lepiej zrozumieć sposób działania Lightning Network, polecam również skorzystanie z tego bezpłatnego kursu:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb