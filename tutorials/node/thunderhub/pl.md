---
name: ThunderHub
description: Interface Sieć zarządzania węzłami Lightning LND
---
![cover](assets/cover.webp)



## Wprowadzenie



ThunderHub to **menedżer open-source dla węzłów Lightning (LND)**, oferujący intuicyjny Interface dostępny z dowolnego urządzenia lub przeglądarki.



**Główne cechy:**




- **Monitorowanie**: Globalny widok sald, kanałów, transakcji, statystyk routingu
- **Zarządzanie**: Otwieranie/zamykanie kanałów, płatności przychodzące/wychodzące, bilansowanie kanałów
- **Integracje**: Obsługa LNURL, zamiany za pośrednictwem Boltz, kopia zapasowa Amboss
- **Interface responsywny**: Kompatybilny z urządzeniami mobilnymi, tabletami i komputerami stacjonarnymi z ciemnymi/jasnymi motywami



ThunderHub łatwo integruje się z **Umbrel**, **Voltage**, **RaspiBlitz** i **MyNode**, upraszczając codzienne zarządzanie węzłem.



**ThunderHub jest szczególnie odpowiedni dla operatorów poszukujących ergonomicznego interfejsu do zarządzania swoimi kanałami, kontrolowania płynności (rebalansowania), monitorowania transakcji i integracji usług stron trzecich, takich jak Amboss. Bezpieczeństwo jest zapewnione przez połączenie lokalne lub Tor.**



Jeśli nie masz jeszcze węzła Lightning, zalecamy skorzystanie z naszego samouczka LND Umbrel:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalacja



ThunderHub można zainstalować na wiele różnych sposobów, w zależności od środowiska hostingowego węzła Lightning. Niezależnie od tego, czy korzystasz z gotowego rozwiązania (Umbrel, Voltage, RaspiBlitz, MyNode, Start9 itp.), czy z ręcznej instalacji, ThunderHub jest często dostępny bez większego wysiłku. Poniżej opisujemy dwa typowe podejścia: za pośrednictwem Umbrel App Store i poprzez ręczną instalację (dotyczy serwera lub dystrybucji hostowanej samodzielnie).



### Instalacja przez Umbrel



Umbrel integruje ThunderHub ze swoim **App Store**, dzięki czemu instalacja jest niezwykle prosta. Nie ma potrzeby korzystania z wiersza poleceń ani ręcznej konfiguracji: wszystko odbywa się za pośrednictwem Interface Umbrel. Wystarczy wykonać następujące kroki:





- Otwórz pulpit nawigacyjny **Umbrel**: Połącz się z siecią Interface swojego węzła Umbrel (np. `http://umbrel.local` w sieci lokalnej lub przez jego Address `.onion`, jeśli używasz Tora).
- **Dostęp do App Store**: W menu głównym Umbrel kliknij "App Store" (lub "App"). Wyszukaj **ThunderHub** na liście dostępnych aplikacji.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Zainstaluj ThunderHub**: Kliknij aplikację ThunderHub, a następnie przycisk instalacji. Potwierdź, jeśli to konieczne. Umbrel automatycznie pobierze i wdroży ThunderHub w węźle.





- **Uruchom aplikację**: Po zakończeniu instalacji (kilkadziesiąt sekund) ThunderHub pojawi się na stronie głównej. Kliknij ikonę, aby ją otworzyć. ThunderHub uruchamia się w przeglądarce.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Ważne:** Gdy ThunderHub jest otwierany po raz pierwszy, automatycznie wyświetla **domyślne hasło** wymagane do zalogowania się. Opcja "Nie pokazuj tego ponownie" pozwala ukryć ten ekran dla przyszłych połączeń. **Zdecydowanie zalecamy:**




- Zapisz to hasło natychmiast **w menedżerze haseł**
- Skopiuj go do użycia w następnym kroku
- Po zapisaniu hasła zaznacz opcję "Nie pokazuj tego ponownie"



![Page de connexion de ThunderHub](assets/fr/03.webp)



Następnie zostaniesz przeniesiony na stronę logowania, gdzie musisz wprowadzić hasło skopiowane w poprzednim kroku, aby odblokować Interface.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel dba o dostarczanie ThunderHub informacji o połączeniu LND (certyfikat TLS, makaron administracyjny itp.) w tle, więc nie trzeba wykonywać żadnej dodatkowej konfiguracji. Wystarczy kilka kliknięć, aby uruchomić ThunderHub na węźle Umbrel.



### Instalacja ręczna (na własnym hostingu, z wyłączeniem Umbrel)



Dla użytkowników spoza Umbrel (np. na osobistym serwerze, Raspberry Pi z RaspiBlitz lub *samodzielnej* instalacji), instalacja ThunderHub wymaga kilku dodatkowych kroków. Poniżej opisujemy instalację ze źródła i konfigurację, zgodnie z [oficjalną dokumentacją ThunderHub](https://docs.thunderhub.io).



#### Instalacja



**Wymagania wstępne:** Upewnij się, że twój system spełnia minimalne wymagania zgodnie z [dokumentacją konfiguracji](https://docs.thunderhub.io/setup):




- **Node.js** w wersji 18 lub wyższej
- **npm** zainstalowany
- Dostęp do plików uwierzytelniających LND :
  - Certyfikat LND TLS (`tls.cert`)
  - LND makaron administracyjny (`admin.macaroon`)
  - LND usługa gRPC Address (nazwa hosta:port) (domyślnie `127.0.0.1:10009` lokalnie)



**1. Pobierz kod ThunderHub:** Sklonuj repozytorium GitHub projektu zgodnie z opisem w [dokumentacji instalacyjnej] (https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. zainstalować zależności i zbudować aplikację:**



```bash
npm install
npm run build
```



Polecenia te instalują wszystkie wymagane moduły, a następnie kompilują aplikację (ThunderHub jest napisany w TypeScript/React).



**3. Późniejsza aktualizacja:** ThunderHub oferuje kilka metod przyszłych aktualizacji:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Konfiguracja (Setup)



**1. Główny plik konfiguracyjny:** Utwórz plik `.env.local` w katalogu głównym folderu ThunderHub, aby dostosować konfigurację (zapobiegnie to nadpisywaniu ustawień podczas aktualizacji). Główne zmienne zgodnie z [dokumentacją konfiguracji] (https://docs.thunderhub.io/setup):



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Konfiguracja kont serwera:** Utwórz plik YAML określony w `ACCOUNT_CONFIG_PATH`:



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Zdalny dostęp:** Aby połączyć się ze zdalnym węzłem LND, dodaj do `LND.conf` :



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Bezpieczeństwo:** Przy pierwszym uruchomieniu ThunderHub **automatycznie** ukrywa `masterPassword` i wszystkie hasła do kont w pliku YAML, aby uniknąć posiadania haseł w postaci czystego tekstu na serwerze.



**5. Uruchom ThunderHub:**



```bash
npm start
```



Domyślnie serwer nasłuchuje na porcie 3000. Dostęp do `http://localhost:3000` (lub `http://ip-serveur:3000` z sieci lokalnej).



**6. Alternatywa Docker:** ThunderHub udostępnia oficjalne obrazy Docker:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



Zostanie wyświetlona strona logowania ThunderHub. Wybierz skonfigurowane konto i wprowadź hasło, aby uzyskać dostęp do pulpitu nawigacyjnego.



**Instalacja na innych dystrybucjach:** Gotowe dystrybucje węzłów (RaspiBlitz, MyNode, Start9 itp.) zazwyczaj oferują natywną obsługę ThunderHub za pośrednictwem odpowiednich interfejsów administracyjnych.



**Więcej informacji:** Zapoznaj się z pełną oficjalną dokumentacją:




- **Instalacja:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Konfiguracja:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Zasoby te szczegółowo opisują zaawansowane opcje, takie jak konta SSO, szyfrowane makarony, konfiguracja TOR i wiele innych.



Po zainstalowaniu ThunderHub i uzyskaniu do niego dostępu, możesz korzystać ze wszystkich jego funkcji. W poniższej sekcji przyjrzymy się Interface ThunderHub i jego różnym zakładkom, aby poprowadzić Cię przez jego użycie.



## Prezentacja Interface



Interface ThunderHub ma strukturę opartą na menu głównym (zwykle wyświetlanym w kolumnie po lewej stronie) składającym się z kilku kluczowych sekcji. Każda z nich odpowiada aspektowi zarządzania węzłem Lightning. Przejdźmy przez nie jeden po drugim:





- **Strona główna** - karta Strona główna z ogólnym pulpitem nawigacyjnym (przegląd węzła i szybkie działania).
- **Pulpit nawigacyjny** - Konfigurowalny pulpit nawigacyjny z widżetami i zaawansowanymi wskaźnikami.
- **Peers** - błyskawiczne zarządzanie peerami (połączeniami z innymi węzłami).
- **Kanały** - Szczegółowe zarządzanie kanałami Lightning.
- **Rebalance** - narzędzie do równoważenia kanałów (płatności cykliczne).
- **Transakcje** - historia płatności Lightning (transakcje LN).
- **Forwards** - statystyki routingu (płatności przekazywane przez węzeł).
- **Łańcuch** - portfel On-Chain Node (On-Chain BTC: UTXO, transakcje).
- **Amboss** - Integracja z Amboss (monitorowanie węzłów, kopie zapasowe itp.).
- **Narzędzia** - Różne narzędzia (kopie zapasowe, podpisane wiadomości, makarony, raporty itp.)
- **Zamiana** - funkcje zamiany On-Chain/Pioruna za pośrednictwem Boltza.
- **Statystyki** - zaawansowane statystyki i metryki wydajności węzłów.



*(Uwaga: W zależności od wersji ThunderHub, niektóre sekcje mogą mieć nieco inne nagłówki lub dodatkowe funkcje, ale ogólne zasady pozostają takie same)*



### Strona główna (ogólny panel sterowania)



Zakładka **Home** w ThunderHub to strona główna, która pojawia się po zalogowaniu. Zawiera ona **General Dashboard**, który oferuje **globalny przegląd** stanu węzła Lightning i sugeruje **szybkie działania** dla rutynowych operacji. Oto, co zazwyczaj można znaleźć:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Salda i pojemności:** W górnej części strony ThunderHub wyświetla dostępne salda. W tym miejscu zazwyczaj wyświetlane jest saldo On-Chain (Bitcoin On-Chain w Wallet węzła, symbolizowane przez Anchor ⚓) i saldo Lightning (możliwości kanałów, symbolizowane przez błyskawicę Bolt ⚡). Daje to natychmiastowy obraz środków posiadanych w On-Chain i Lightning. Jeśli masz kilka kont lub kanałów, upewnij się, że jesteś na właściwym (np. Mainnet vs Testnet).





- **Kluczowe statystyki:** Pulpit nawigacyjny może pokazywać pewne globalne wskaźniki dla węzła - na przykład liczbę otwartych kanałów, liczbę połączonych peerów, zarobione opłaty za routing (jeśli dotyczy) itp. Jest to podsumowanie ostatniej aktywności i stanu węzła.





- **Szybkie akcje:** Pulpit nawigacyjny zawiera przyciski do szybkiego wykonywania najczęstszych zadań, bez konieczności nawigowania po menu. Te szybkie akcje obejmują :





- **Ghost**: Skonfiguruj niestandardowy Lightning Address za pośrednictwem Amboss.
- **Darowizna**: Przekaż darowiznę za pośrednictwem Lightning.
- **Login/Go To**: Połącz się ze swoim kontem Amboss (Quick Connect) i przejdź bezpośrednio do Amboss.space, aby wyświetlić informacje o swoim węźle.
- **Address**: Wprowadź Lightning Address, aby dokonać płatności.
- **Otwórz**: Otwiera nowy kanał Lightning. Kliknięcie powoduje otwarcie formularza umożliwiającego wprowadzenie identyfikatora URI zdalnego węzła, do którego ma zostać otwarty kanał, kwoty i, w stosownych przypadkach, maksymalnej opłaty On-Chain, która ma zostać wykorzystana.
- **Dekodowanie**: Odkoduj Lightning Invoice lub LNURL, aby wyświetlić szczegóły przed dokonaniem płatności.
- **LNURL**: Przetwarzanie adresów LNURL dla płatności lub wypłat Lightning.
- **LnMarkets Login**: Zaloguj się do LnMarkets, aby handlować.



Te szybkie działania pozwalają na wykonywanie najczęstszych operacji bezpośrednio ze strony głównej, bez konieczności nawigowania po różnych zakładkach Interface.



Krótko mówiąc, pulpit nawigacyjny ThunderHub umożliwia **szybkie spojrzenie** na węzeł i pozwala wykonywać najczęstsze operacje (wysyłanie/odbieranie, otwieranie kanału) za pomocą jednego kliknięcia. Jest to idealny punkt wyjścia do codziennej administracji.



### Pulpit nawigacyjny



Sekcja **Dashboard** jest oddzielona od karty Home i oferuje bardziej zaawansowany, konfigurowalny pulpit nawigacyjny. Ta sekcja umożliwia utworzenie niestandardowego widoku z określonymi widżetami zgodnie z potrzebami operatora węzła.





- **Konfigurowalne widżety:** W przeciwieństwie do strony głównej, która ma stały układ, pulpit nawigacyjny pozwala dokładnie wybrać, które Elements mają być wyświetlane i jak je zorganizować.



![Dashboard sans widgets activés](assets/fr/06.webp)



Jeśli żadne widżety nie są włączone, pojawi się komunikat "Brak włączonych widżetów!" z przyciskiem "Ustawienia", aby uzyskać dostęp do parametrów dostosowywania.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



W ustawieniach można wybierać spośród szerokiej gamy widżetów podzielonych na kategorie: "Lightning - Info", "Lightning - Table", "Lightning - Graph" itd. Każdy widżet można indywidualnie aktywować lub dezaktywować za pomocą przycisków "Pokaż/Ukryj".



![Bas de la page des paramètres](assets/fr/08.webp)



W dolnej części ustawień znajduje się przycisk "Do pulpitu nawigacyjnego" umożliwiający powrót do pulpitu nawigacyjnego oraz przycisk "Resetuj widżety" umożliwiający zresetowanie domyślnego wyświetlania.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Po skonfigurowaniu pulpit nawigacyjny może wyświetlać różne wykresy i wskaźniki: Wykresy płatności Lightning, liczbę wystawionych faktur, statystyki forwardów, szczegółowe salda itp.





- **Zaawansowane metryki:** Dostęp do bardziej szczegółowych statystyk dotyczących wydajności węzła, z wykresami i danymi w czasie rzeczywistym.





- **Konfigurowalny przegląd:** Dostosuj wyświetlacz do swoich potrzeb, niezależnie od tego, czy jesteś zwykłym użytkownikiem, czy profesjonalnym operatorem zarządzającym wieloma kanałami routingu.





- **Modułowy Interface:** Dodawaj lub usuwaj widżety w zależności od potrzeb: wykresy do przodu, wskaźniki płynności, alerty o stanie węzła itp.



Ta sekcja jest szczególnie przydatna dla zaawansowanych użytkowników, którzy chcą monitorować określone metryki lub uzyskać bardziej techniczny przegląd swojego węzła Lightning. Uzupełnia ona sekcję Home, oferując większą elastyczność i kontrolę nad sposobem wyświetlania informacji.



### Rówieśnicy



Sekcja **Peers** zawiera listę wszystkich węzłów Lightning aktualnie połączonych z węzłem użytkownika jako węzły równorzędne. **Węzeł równorzędny** jest bezpośrednim połączeniem między węzłami na Lightning Network. Twój węzeł może być połączony z węzłami równorzędnymi nawet bez otwartego kanału (np. tylko do informacji plotkarskich Exchange w sieci), lub oczywiście każdy otwarty kanał automatycznie implikuje podłączonego węzła równorzędnego.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



W zakładce Rówieśnicy zobaczysz :





- **Kolumny informacyjne:** Interface wyświetla przydatne szczegóły, takie jak stan synchronizacji, typ połączenia (Clearnet lub Tor), ping, odebrane/wysłane satoshi i ilość wymienianych danych.
- Dodaj peera: ThunderHub pozwala ręcznie połączyć się z nowym peerem za pomocą przycisku **"Dodaj"** w prawym górnym rogu. Musisz wprowadzić URI węzła (format `<public_key>@<socket>`). Po zatwierdzeniu ThunderHub wysyła odpowiednie polecenie `lncli connect`. Jeśli węzeł jest online i dostępny, zostanie dodany do listy urządzeń równorzędnych.



### Kanały



Zakładka **Kanały** jest sercem zarządzania kanałami Lightning. Jest to prawdopodobnie najczęściej odwiedzana sekcja. Przedstawia **wszystkie kanały Lightning** wraz z ich szczegółami i umożliwia wykonywanie działań związanych z zarządzaniem tymi kanałami.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Oto, co można znaleźć na stronie Kanały:





- Widok listy kanałów: Każdy otwarty (lub otwierany/zamykany) kanał jest wyświetlany na liście, zwykle z aliasem zdalnego węzła, całkowitą pojemnością kanału i kolorowym paskiem ilustrującym rozkład płynności lokalnej i zdalnej. ThunderHub używa kodu koloru (często niebieskiego/Green) lub wartości procentowej do wskazania równowagi kanału: na przykład niebieski dla udziału lokalnego, Green dla udziału zdalnego. Jeśli kanał jest idealnie zrównoważony (50/50), pasek będzie miał połowę każdego koloru. Pozwala to na szybkie określenie, które kanały są niezrównoważone (wszystkie niebieskie = prawie wszystkie lokalne, wszystkie Green = prawie wszystkie zdalne).





- **Kolumny informacyjne:** Interface wyświetla szczegółowe kolumny, w tym Status, Dostępne akcje, Informacje o peerze, ID kanału, Pojemność, Aktywność, Opłaty i Saldo z graficznym wyświetlaniem płynności.





- **Konfiguracja wyświetlacza:** Koło zębate w prawym górnym rogu umożliwia dostosowanie wyświetlania kanałów do własnych preferencji.





- **Status:** Zobaczysz również wskaźniki statusu - np. `Active` (kanał jest otwarty i działa), `Offline` (peer jest odłączony, więc kanał jest chwilowo bezużyteczny), `Pending` (dla otwarć lub zamknięć oczekujących na potwierdzenie On-Chain).





- **Akcje na kanale:** Dla każdego kanału ThunderHub udostępnia przyciski akcji (często w postaci ikon):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- **Edytuj opłaty:** Funkcja Interface "Aktualizuj zasady kanału" umożliwia dostosowanie wszystkich parametrów kanału: Opłata podstawowa, Stawka opłaty (w ppm), Delta CLTV, Max HTLC i Min HTLC. Pozwala to na dostosowanie zasad opłat indywidualnie dla każdego kanału, w celu przyciągnięcia (lub zniechęcenia) ruchu routingu. *(Uwaga: ThunderHub nie zastępuje automatycznego narzędzia do zarządzania opłatami, ale do ręcznego dostosowywania jest bardzo skuteczny)*
- Kanał zamknięcia (*Close*): Interface "Kanał zamknięcia" daje wybór pomiędzy **współpracującym zamknięciem** (domyślnie) lub **wymuszonym zamknięciem** (*Wymuś zamknięcie*) poprzez zdefiniowanie opłat (w Sats/vByte). **Ważne:** W miarę możliwości zawsze preferuj zamknięcie kooperacyjne, aby uniknąć opóźnień w rozliczeniach On-Chain i wyższych opłat. ThunderHub poinformuje Cię, czy peer jest online (możliwa współpraca), czy nie. W przypadku wymuszenia zamknięcia, należy potwierdzić, ponieważ jest to nieodwracalne i spowoduje zamiatanie transakcji z blokadą czasową (zazwyczaj 144 bloki lub ~ 1 dzień na Bitcoin Mainnet).
- **Otwieranie nowego kanału:** Aby otworzyć nowy kanał, kliknij koło zębate w prawym górnym rogu strony Kanały, a następnie wybierz opcję "Otwórz". Następnie można zainicjować kanał do nowego lub istniejącego urządzenia równorzędnego. Zaletą korzystania z tej strony jest to, że masz przed sobą listę istniejących kanałów, co może pomóc w podjęciu decyzji, gdzie otworzyć nowy kanał.



Krótko mówiąc, sekcja Kanały zapewnia **dokładną kontrolę nad każdym kanałem**. To tutaj zarządzasz alokacją płynności, decydujesz, które kanały zachować, a które zamknąć, i ustawiasz parametry routingu dla każdego kanału. ThunderHub oferuje przejrzysty Interface dla tych kluczowych operacji zarządzania węzłami.



### Równowaga



Zakładka **Rebalance** poświęcona jest **balansowaniu kanałów**. Równoważenie (lub *rebalansowanie*) polega na ponownym dostosowaniu dystrybucji środków między kanałami wychodzącymi i przychodzącymi poprzez dokonanie **okrągłej płatności** z jednego z kanałów na inny kanał za pośrednictwem Lightning Network. Pozwala to, bez wprowadzania nowych funduszy, przenieść płynność z kanału, który jest zbyt pełny, do kanału, który jest zbyt pusty, czyniąc kanały bardziej użytecznymi (zrównoważony kanał może zarówno wysyłać, jak i odbierać płatności).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub znacznie ułatwia tę operację, która w przeciwnym razie byłaby żmudna w wierszu poleceń. Oto jak korzystać z sekcji Rebalance:





- **Początkowy widok kanału:** Po wejściu do Rebalance, ThunderHub wyświetla listę kanałów, ze wskaźnikiem salda dla każdego z nich (podobnym do tego na stronie Kanały). Od razu widać, które kanały są niezrównoważone. ThunderHub może sortować kanały w kolejności rosnącej równowagi, tak aby najbardziej niezrównoważone kanały wyróżniały się na górze listy (0,0 oznacza całkowicie lokalne lub zdalne).





- **Wybór urządzeń równorzędnych:** Interface ułatwia wybór wychodzących i przychodzących urządzeń równorzędnych do równoważenia.





- **Ustawienia parametrów:** Można ustawić :
  - **Maksymalna opłata** (w Sats i ppm), którą jesteś skłonny zapłacić
- **Kwota do przywrócenia równowagi** z opcją "Stała" lub "Docelowa"
- **Węzły, których należy unikać** podczas routingu
- **Maksymalny czas próby** wyszukiwania trasy





- Wybierz kanał **źródłowy**: Najpierw wybierz **kanał wychodzący (źródłowy)**, tj. kanał, z którego masz zbyt dużą płynność lokalną, aby się przenieść. W praktyce jest to kanał, w którym lokalny udział jest wysoki (> 50%). Wyobraźmy sobie kanał A z 1 000 000 satelitów, z których 900 000 to satelity lokalne - dobry kandydat do wysłania satelitów gdzie indziej. Klikając ten kanał A jako "wychodzący", ThunderHub oznacza go jako źródło.





- Wybierz **kanał docelowy**: Następnie należy wybrać **kanał przychodzący (docelowy)**, który musi otrzymać płynność. Zazwyczaj będzie to kanał, w którym jest odwrotnie - większość funduszy znajduje się po drugiej stronie (np. tylko 100 000 lokalnych satelitów z 1 000 000). ThunderHub, po wybraniu kanału źródłowego, posortuje inne kanały w odwrotnej kolejności (malejące saldo), aby pomóc zidentyfikować najbardziej komplementarne kanały. Wybierz kanał B, który ma miejsce po stronie lokalnej. ThunderHub wyświetli wtedy wyraźnie, które dwa kanały zostały wybrane (źródłowy A i docelowy B).





- **Ustaw kwotę opłaty i tolerancję:** Formularz umożliwia wprowadzenie :





- **Kwota** do zrównoważenia (w Sats). Często wybieramy kwotę równą temu, co zrównoważyłoby oba kanały przy \~50/50. ThunderHub może na przykład wstępnie wypełnić połowę nadwyżki pojemności kanału źródłowego.
  - **Maksymalna opłata**, jaką użytkownik jest skłonny zapłacić za tę operację (opcjonalnie). Opłata ta jest wyrażona w Sats (całkowity koszt routingu okrężnego). Jeśli pozostawisz to pole puste, ThunderHub wyszuka ścieżkę niezależnie od kosztu, co generalnie nie jest wskazane (lepiej ustawić limit, np. 10 Sats dla małego rebalansu lub maksymalną wartość ppm).





- **Znajdź trasę:** Kliknij przycisk, aby znaleźć trasę. ThunderHub odpytuje LND, aby obliczyć trasę z kanału źródłowego przez sieć do własnego kanału docelowego. Jeśli znajdzie możliwą trasę, która spełnia kryteria opłaty, wyświetli ją ze szczegółami dotyczącymi przeskoków i kosztu opłaty. Na przykład, może wskazać, że znalazł ścieżkę z 3 przeskokami i łączną opłatą 2 Sats.





- **Rozpocznij równoważenie:** Jeśli jesteś zadowolony z proponowanej trasy, kliknij **Balance Channel**. ThunderHub zainicjuje płatność cykliczną za pośrednictwem LND. Jeśli płatność się powiedzie, zobaczysz powiadomienie o powodzeniu, a salda kanałów A i B zostaną zmodyfikowane w czasie rzeczywistym. ThunderHub zaktualizuje wskaźnik salda dla tych kanałów (w idealnym przypadku będą one bardziej zielone niż wcześniej, wskazując na lepsze saldo).





- **Dostosowania i iteracje:** Jeśli trasa nie zostanie znaleziona przy pierwszej próbie (lub jeśli jest zbyt droga), można dostosować parametry:





  - Wypróbuj mniejszą kwotę (czasami częściowe przywrócenie równowagi przechodzi, podczas gdy duża kwota kończy się niepowodzeniem).
  - Zwiększaj maksymalną opłatę stopniowo, ale uważaj, aby nie płacić więcej niż jest to warte.
  - Użyj przycisku **Pobierz inną trasę**, jeśli jest dostępny, aby wypróbować alternatywę.
  - Wypróbuj inną parę kanałów, jeśli sytuacja stanie się naprawdę trudna.



ThunderHub sprawia, że proces ten jest bardzo **intuicyjny i wizualny**. W zaledwie 4 krokach (wybór kanału wychodzącego, wybór kanału przychodzącego, kwota, zatwierdzenie) można zrobić to, co wcześniej wymagało skomplikowanych poleceń ręcznych. Narzędzie to jest nieocenione dla utrzymania dobrze zbalansowanego węzła, poprawy wydajności routingu i doświadczenia (łatwiejsze wysyłanie i odbieranie płatności we wszystkich kanałach).



Wreszcie, należy pamiętać, że równoważenie zużywa koszty routingu (płacone węzłom pośrednim), więc jest to **inwestycja**, aby zwiększyć płynność węzła. Używaj go mądrze, na przykład do obsługi kanału do często używanej usługi (płynność przychodząca) lub do równoważenia dużego kanału routingu. ThunderHub pozwala to zrobić **prosto i wydajnie**.



### Transakcje



Sekcja **Transakcje** w ThunderHub odpowiada historii transakcji węzła **Lightning**, tj. płatnościom i fakturom zapłaconym lub otrzymanym za pośrednictwem kanałów. Jest to rodzaj wyciągu z konta dla operacji LN.



![Historique des transactions Lightning](assets/fr/14.webp)



W tej zakładce znajdują się :





- Wykres **Invoice**: W prawym górnym rogu znajduje się wykres przedstawiający ewolucję otrzymanych faktur w czasie, umożliwiający wizualizację aktywności węzła.





- Chronologiczna lista wszystkich transakcji Lightning wykonanych *z* lub *do* węzła. Każdy wpis może zawierać :





  - Typ operacji: **wysłana płatność** (płatność wychodząca) lub **otrzymana płatność** (płatność przychodząca, za pośrednictwem płatnego Invoice).
  - Kwota w Sats.
  - Data/godzina.
  - Identyfikator płatności (obraz wstępny Hash lub RHash) lub komentarz (jeśli dodano notatkę do Invoice).
  - Status: **zakończona** lub ewentualnie **w toku**/*nieudana* (np. płatność oczekująca na rozwiązanie, ale generalnie LND przetwarza to szybko, więc jest tu niewiele "oczekujących" w porównaniu z transakcjami On-Chain).



Krótko mówiąc, sekcja Transakcje służy jako **dziennik aktywności LN**. Jest bardzo przydatna do sprawdzania, czy płatność została zrealizowana, ile opłat kosztowała lub śledzenia historii wymiany Lightning. W połączeniu z sekcją Forward (opisaną poniżej), będziesz mieć pełny wgląd w pieniądze, które przeszły przez Twój węzeł.



### Naprzód



Zakładka **Przekazywanie** jest poświęcona **aktywności routingu** twojego węzła, tj. płatnościom, które **tranzytują** przez twoje kanały (gdy działasz jako węzeł pośredniczący na Lightning Network). Jeśli obsługujesz swój węzeł jako węzeł routingu, jest to ważna sekcja do śledzenia wydajności.



![Statistiques de routage Lightning](assets/fr/15.webp)



W Forwards, ThunderHub prezentuje :





- **Filtry i opcje wyświetlania:** W prawym górnym rogu filtry umożliwiają sortowanie danych według dnia/tygodnia/miesiąca/roku oraz wybór między wyświetlaniem graficznym lub tabelarycznym.





- **Komunikat o aktywności:** Jeśli w wybranym okresie nie wykonano routingu, Interface wyświetli komunikat "No forwards for this period", jak pokazano w tym przykładzie.





- **Tabela ostatnich przekierowań**: każdy wpis odpowiada płatności, która została **przekierowana** przez twój węzeł. Dla każdego przekazu widzimy zazwyczaj :





  - Timestamp,
  - kwota skierowana (w Sats),
  - **opłata zarobiona** na tym przekierowaniu (w Sats jest to różnica między tym, co otrzymałeś na kanale przychodzącym i wysłałeś na kanale wychodzącym),
  - używane kanały przychodzące i wychodzące (często identyfikowane przez alias peer lub identyfikator kanału).
  - status (zwykle *zakończone* lub niepowodzenie, jeśli przekazywanie nie powiodło się w trasie).





- **Zagregowane statystyki**: ThunderHub oblicza i wyświetla w górnej części strony sumy i statystyki w danym okresie (np. ostatnie 24 godziny lub 7 dni itp., czasami konfigurowalne).



Krótko mówiąc, sekcja Forwards oferuje **przegląd w czasie rzeczywistym aktywności routingu węzła Lightning**. W połączeniu z sekcjami Channels i Rebalance tworzy to kompletny pakiet do optymalizacji węzła: Channels/Rebalance dla płynności, Forwards dla obserwacji wyników (przepływów i zysków).



### Łańcuch



Sekcja **Chain** odpowiada zarządzaniu portfelem Bitcoin On-Chain węzła LND. Ten Interface umożliwia przeglądanie i zarządzanie funduszami Bitcoin, które są używane do otwierania kanałów lub otrzymywania funduszy z zamkniętych kanałów.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



W Chain znajdziesz :





- Saldo On-Chain: **Wyświetla całkowite saldo BTC dostępne w Wallet LND.**





- **Lista UTXO:** Wyświetl wszystkie niewydane produkty (UTXO) z kwotą, potwierdzeniami, Address i formatem dla każdego produktu.





- **Historia transakcji:** Szczegółowa tabela wszystkich transakcji Bitcoin z typem (wejście/wyjście), datą, kwotą, opłatami, potwierdzeniami, blokiem włączenia, adresami i txid.



### Amboss



ThunderHub integruje się z platformą **Amboss** (amboss.space), która oferuje szczegółowe informacje na temat węzłów Lightning, rynek płynności i przydatne funkcje, takie jak szyfrowane tworzenie kopii zapasowych kanałów i monitorowanie dostępności.



![Intégration Amboss avec ses options](assets/fr/17.webp)



W ThunderHub sekcja Amboss umożliwia **połączenie** węzła z kontem Amboss:





- **Ghost Address:** Skonfiguruj **spersonalizowany Lightning Address** dla swojego węzła, ułatwiając płatności przychodzące.





- Automatyczne kopie zapasowe kanałów:** Flagowa funkcja szyfrowanych kopii zapasowych kanałów** (pliki SCB) w Amboss. Aktywuj **Amboss Auto Backup = Tak** w ustawieniach, aby automatycznie wysyłać zaszyfrowane aktualizacje kopii zapasowych przy każdej zmianie kanałów. W przypadku awarii będziesz mógł odzyskać swoje środki dzięki tej zewnętrznej kopii zapasowej.





- Kontrole zdrowia: Aktywuj **Amboss Healthcheck = Yes**, aby twój węzeł wysyłał regularne pingi do Amboss. Otrzymasz powiadomienia, jeśli twój węzeł wydaje się być offline.





- **Inne funkcje:** Automatyczne wypychanie salda, **integracja Magma/Hydro** (rynek płynności) i dostęp do szczegółowych statystyk wydajności.



Integracja Amboss dodaje niezbędne **bezpieczeństwo Layer** z automatycznym zewnętrznym tworzeniem kopii zapasowych i monitorowaniem dostępności, dostępnym bezpośrednio z ThunderHub.



### Narzędzia



Sekcja **Narzędzia** grupuje różne zaawansowane narzędzia do zarządzania węzłem. Oto główne Elements:



![Interface des outils disponibles](assets/fr/18.webp)





- **Kopie zapasowe:** Ręczne zarządzanie kopiami zapasowymi kanałów (SCB). ThunderHub umożliwia **pobranie pełnego pliku kopii zapasowej** kanałów (opcja "Kopia zapasowa wszystkich kanałów -> Pobierz"). Przechowuj ten plik `channel-all.bak` w bezpiecznym miejscu - jest on niezbędny do odzyskania środków w przypadku awarii. Możesz również **zaimportować** plik kopii zapasowej podczas ponownego wdrażania węzła.





- **Księgowość:** Narzędzie do eksportowania raportów finansowych, w tym zarobionych/zapłaconych opłat i wolumenów kierowanych w danym okresie.
- **Podpisane wiadomości:** Podpisz lub zweryfikuj wiadomości za pomocą węzła, aby udowodnić Ownership węzła Lightning za pomocą podpisu kryptograficznego.
- Makarony (sekcja "Piekarnia"):** Zarządzaj makaronami LND**, aby utworzyć spersonalizowany dostęp. "Piekarnia" Interface pozwala precyzyjnie wybrać każde uprawnienie: "Dodaj lub usuń Peers", "Utwórz Adresy Łańcuchowe", "Utwórz Faktury", "Utwórz Makarony", "Pochodne Klucze", "Uzyskaj Klucze Dostępu", "Uzyskaj Transakcje Łańcuchowe", "Uzyskaj Faktury", "Uzyskaj Informacje Wallet", "Get Payments", "Get Peers", "Pay Invoices", "Revoke Access Ids", "Send to Chain Addresses", "Sign bytes", "Sign Messages", "Stop daemon", "Verify bytes signature", "Verify messages" itd. Każde uprawnienie można aktywować indywidualnie za pomocą przycisków "Tak/Nie", aby utworzyć makaron dostosowany do indywidualnych potrzeb.
- **Informacje o systemie:** Wyświetlanie wersji Wallet i aktywowanych RPC.



Krótko mówiąc, sekcja Narzędzia łączy zaawansowane funkcje administracyjne - kopie zapasowe, księgowość, bezpieczeństwo i zarządzanie dostępem - w ujednoliconym Interface.



### Zamiana



Zakładka **Swap** w ThunderHub umożliwia wymianę satoshi Lightning na Bitcoin On-Chain za pośrednictwem usługi Boltz. Ta funkcja jest przydatna do "zrzucania" nadmiaru płynności Lightning do kanału bez zamykania kanału.



![Interface de swap via Boltz](assets/fr/19.webp)



Proces ten jest prosty:





- **Kwota**: Określ kwotę do wymiany
- **Address**: Wprowadź Bitcoin odbiór Address
- **Wykonanie**: ThunderHub komunikuje się z Boltz, aby automatycznie przetwarzać Exchange



**Korzyści:**




- Usługa bez zatrzymania (bez zatrzymania gotówki)
- Zachowanie istniejących kanałów
- Łatwy w użyciu zintegrowany Interface



Boltz pobiera niewielką prowizję, a Ty płacisz standardową opłatę transakcyjną Bitcoin. ThunderHub wyświetla wszystkie koszty przed potwierdzeniem.



### Statystyki



Sekcja **Stats** w ThunderHub oferuje **zaawansowane statystyki** węzła Lightning do analizy wydajności i optymalizacji routingu.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Ta sekcja jest niezbędna do optymalizacji kosztów, identyfikacji skutecznych kanałów i planowania ekspansji węzła.



## Wnioski



**ThunderHub** stał się niezbędnym narzędziem do łatwego administrowania węzłem Lightning **LND**. Ten nowoczesny Interface oferuje wszystkie niezbędne funkcje: zarządzanie kanałami, płatności, monitorowanie, z zaawansowanymi funkcjami, takimi jak automatyczne równoważenie i integracja Amboss.



**Kluczowe korzyści:**




- Interface elegancki i intuicyjny
- Potężne narzędzia (rebalansowanie, zamiany Boltza, automatyczne kopie zapasowe)
- Kompatybilny z Umbrel, Voltage, RaspiBlitz i innymi dystrybucjami



ThunderHub demokratyzuje zaawansowane zarządzanie węzłami Lightning, udostępniając to, co wcześniej wymagało skomplikowanych poleceń technicznych. Niezależnie od tego, czy jesteś początkującym, czy doświadczonym operatorem, ThunderHub pozwala efektywnie zarządzać węzłem Lightning za pośrednictwem nowoczesnego, wszechstronnego Interface.



## Zasoby



**Oficjalne linki:**




- **Oficjalna strona:** [thunderhub.io](https://thunderhub.io)
- **Dokumentacja:** [docs.thunderhub.io](https://docs.thunderhub.io)
- **Kod źródłowy GitHub:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)