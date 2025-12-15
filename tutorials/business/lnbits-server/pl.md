---
name: LNbits Server
description: Instalacja i konfiguracja samodzielnie hostowanego serwera LNbits na Ubuntu VPS z Phoenixd lub na Umbrel
---

![cover](assets/cover.webp)



LNbits to interfejs sieciowy typu open source, który przekształca dowolny backend Lightning (LND, Core Lightning, Phoenixd) w kompletną platformę usługową. To samoobsługowe rozwiązanie umożliwia zarządzanie wieloma portfelami Lightning w izolacji, wdrażanie punktów sprzedaży, tworzenie systemów darowizn lub usług rozliczeniowych, przy jednoczesnym zachowaniu całkowitej kontroli nad funduszami.



Ten samouczek obejmuje dwa podejścia do instalacji: **VPS Ubuntu z Phoenixd** (lekkie rozwiązanie bez pełnego węzła Bitcoin) i **Umbrel** (integracja z istniejącym węzłem LND). W przeciwieństwie do ogólnego samouczka LNbits Plan ₿ Academy, który obejmuje koncepcje i rozszerzenia, ten przewodnik koncentruje się na technicznych procedurach instalacji krok po kroku.



## Czym jest LNbits?



LNbits to system księgowy Lightning opracowany w języku Python (FastAPI), który łączy się z istniejącym backendem (LND, Core Lightning, Phoenixd). W przeciwieństwie do tradycyjnych węzłów Lightning, LNbits oferuje przystępny interfejs do zarządzania kilkoma odizolowanymi portfelami z własnymi kluczami API. Możesz tworzyć subkonta dla swojej rodziny, pracowników lub projektów, nie dając im dostępu do wszystkich swoich środków.



Oddzielona architektura przechowuje informacje w SQLite (domyślnie) lub PostgreSQL (produkcyjnie), podczas gdy fundusze pozostają zarządzane przez backend Lightning. Ta separacja gwarantuje przenośność: można migrować z Phoenixd do LND bez utraty danych użytkownika.



## Najważniejsze cechy



LNbits oferuje wszechstronny **system rozszerzeń**: TPoS (punkt sprzedaży), Paywall (monetyzacja treści), Events (sprzedaż biletów), LndHub (serwer dla BlueWallet), Bolt Cards (płatności NFC), Split Payments (automatyczna dystrybucja) oraz User Manager (zarządzanie użytkownikami z uwierzytelnianiem).



Pulpit nawigacyjny** wyświetla salda w czasie rzeczywistym, historię transakcji i narzędzia rozliczeniowe. Każdy wallet ma unikalny adres URL zawierający klucze API, umożliwiając dostęp bez tradycyjnego logowania. Trzypoziomowy system kluczy API** (administrator, faktura, tylko do odczytu) oferuje szczegółową kontrolę uprawnień dla bezpiecznych integracji.



LNbits natywnie implementuje **LNURL** (LNURL-pay, LNURL-withdraw, LNURL-auth) i obsługuje **Lightning Address**, gwarantując kompatybilność z nowoczesnymi portfelami Lightning i ułatwiając wdrażanie profesjonalnych usług.



## Obsługiwane platformy



**Ubuntu VPS**: Lekkie rozwiązanie bez pełnego węzła Bitcoin. Wymagania wstępne: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + nazwa domeny wymagana do publicznej ekspozycji (usługi LNURL).



**Umbrel**: Łatwa instalacja z App Store. Wymagania wstępne: funkcjonalny węzeł Umbrel ze zsynchronizowanym LND i otwartymi kanałami. Automatyczna konfiguracja.



Poniżej znajdują się linki do naszych samouczków Umbrel i Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalacja na Ubuntu VPS z Phoenixd



### Krok 1: Zabezpieczenie serwera VPS



**Przed jakąkolwiek instalacją**, musisz zabezpieczyć swój serwer Ubuntu VPS zgodnie z zasadami sztuki. Ten krok jest **krytyczny** dla ochrony infrastruktury i funduszy Lightning.



Oto szczegółowy przewodnik, który pomoże ci zacząć: **[Początkowa konfiguracja serwera Ubuntu - przewodnik krok po kroku](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** autorstwa Daniela P. Costasa.



Ten przewodnik obejmuje konfigurację użytkownika, bezpieczne SSH, zaporę sieciową (UFW), fail2ban, automatyczne aktualizacje i dobre praktyki w zakresie bezpieczeństwa systemu.



### Krok 2: Instalacja Phoenixd



Po zabezpieczeniu serwera należy zainstalować i skonfigurować Phoenixd. Plan ₿ Academy oferuje kompleksowy dedykowany samouczek obejmujący instalację, generowanie seed i konfigurację usługi systemd:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Po uruchomieniu Phoenixd (sprawdź za pomocą `./phoenix-cli getinfo`), zanotuj **hasło HTTP** w `~/.phoenix/phoenix.conf` - będzie ono potrzebne do połączenia LNbits z Phoenixd.



### Wdrożenie LNbits



Zainstaluj UV i sklonuj LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Konfiguracja backendu Phoenixd:


```bash
cp .env.example .env && nano .env
```



Dodaj do `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Przetestuj za pomocą `uv run lnbits --host 0.0.0.0 --port 5000`, a następnie utwórz usługę systemd z `Wants=phoenixd.service`.



## Początkowa konfiguracja i pierwsze użycie



### Aktywacja superużytkownika



Aktywuj interfejs administratora w pliku `.env`:


```
LNBITS_ADMIN_UI=true
```



Zrestartuj LNbits (`sudo systemctl restart lnbits`) i odzyskaj identyfikator SuperUser ID:


```bash
cat ~/lnbits/data/.super_user
```



Przejdź do `http://<IP-VPS>:5000/wallet?usr=<SuperUserID>`, aby uzyskać dostęp do panelu administracyjnego. Menu "Serwer" pozwala skonfigurować źródła finansowania, rozszerzenia i konta użytkowników.



### Bezpieczne tworzenie konta



**Ważne dla publicznej ekspozycji**: Jeśli wystawiasz swoją instancję LNbits na publiczną nazwę domeny dostępną z Internetu, **krytyczne** jest wyłączenie swobodnego tworzenia kont użytkowników.



W interfejsie administracyjnym SuperUser przejdź do "Ustawień", a następnie do sekcji "Zarządzanie użytkownikami". Znajdziesz tam opcję "Zezwalaj na tworzenie nowych użytkowników".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Dla wystawy publicznej z nazwą domeny** :




- Musisz wyłączyć** opcję "Zezwalaj na tworzenie nowych użytkowników"
- Bez tej ochrony każdy w Internecie może utworzyć konto w instancji użytkownika
- Osoba atakująca może tworzyć konta i korzystać z płynności węzła Lightning bez wiedzy użytkownika
- Konieczne będzie ręczne utworzenie kont użytkowników z poziomu interfejsu SuperUser



**Tylko do użytku lokalnego** :




- Ta opcja jest mniej krytyczna, jeśli instancja jest dostępna tylko lokalnie (http://localhost:5000)
- Wyłączenie tej opcji jest jednak dobrą ogólną praktyką bezpieczeństwa



Po skonfigurowaniu tylko administrator SuperUser może tworzyć nowe konta użytkowników za pośrednictwem interfejsu "Użytkownicy". Takie podejście gwarantuje całkowitą kontrolę nad tym, kto może uzyskać dostęp do infrastruktury Lightning i korzystać z funduszy.



### Otwieranie pierwszego kanału



Phoenixd automatycznie zarządza kanałami poprzez automatyczną płynność. Wygeneruj fakturę Lightning na kwotę ~30 000 sats z LNbits i opłać ją z innego wallet. Phoenixd automatycznie otwiera kanał do ACINQ. Opłata za otwarcie (~20-23 tys. sats) zostaje odjęta, pozostałe saldo (~7-10 tys. sats) pojawia się po potwierdzeniu on-chain.



Sprawdź status za pomocą `./phoenix-cli getinfo`. Następnie należy rozważyć wyłączenie auto-liquidity (`auto-liquidity=off` w `phoenix.conf`), aby kontrolować otwarcia kanałów.



### Wyświetlanie publiczne i HTTPS



**Ważne**: HTTPS obowiązkowy dla publicznego wyświetlania (bezpieczeństwo klucza API + zgodność z LNURL). Pomiń ten krok tylko do użytku lokalnego.



**Caddy (zalecane)**: automatyczny SSL. `sudo apt install -y caddy`, edytuj `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Uruchom ponownie: `sudo systemctl restart caddy`.



**Nginx** : Więcej kontroli. Zainstaluj `nginx certbot python3-certbot-nginx`, utwórz `/etc/nginx/sites-available/lnbits`:


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


Aktywacja: `sudo ln -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Dodaj do `.env`: `FORWARDED_ALLOW_IPS=*`



## Instalacja parasola



### Wdrożenie z App Store



Przejdź do Umbrel App Store, wyszukaj "LNbits" i kliknij "Zainstaluj".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel automatycznie sprawdza wymagane zależności. LNbits wymaga Lightning Node (LND) do działania. Jeśli węzeł Lightning już działa, kliknij "Zainstaluj LNbits", aby potwierdzić.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel pobiera obraz Docker, automatycznie konfiguruje połączenia z LND i uruchamia kontener (2-5 minut). Instalacja odbywa się całkowicie w tle.



### Początkowa konfiguracja SuperUser



Przy pierwszym uruchomieniu LNbits wyświetli monit o utworzenie konta administratora SuperUser. Wprowadź nazwę użytkownika i bezpieczne hasło, aby zabezpieczyć dostęp do interfejsu administracyjnego.



![Configuration SuperUser](assets/fr/03.webp)



**Ważne**: To konto SuperUser ma pełne uprawnienia w instancji LNbits. Wybierz silne hasło i przechowuj je w bezpiecznym miejscu.



Po utworzeniu konta zostaniesz automatycznie przeniesiony do głównego interfejsu administracyjnego. Umbrel skonfigurował już LND jako źródło finansowania - wszystkie płatności Lightning będą przechodzić przez istniejące kanały.



### Dostęp do interfejsu administratora



W menu po lewej stronie kliknij "Ustawienia", aby uzyskać dostęp do pełnego panelu administracyjnego.



![Interface Settings](assets/fr/04.webp)



Sekcja "Zarządzanie portfelami" wyświetla kluczowe informacje o konfiguracji:




- Źródło finansowania** : LndBtcRestWallet (bezpośrednie połączenie z węzłem LND Umbrel)
- Saldo węzła** : Całkowita płynność dostępna w kanałach Lightning
- Saldo LNbits**: Środki przydzielone do systemu LNbits (początkowo 0 sats)



Możesz teraz bezpośrednio wykorzystać płynność swojego węzła Umbrel dla wszystkich utworzonych portfeli LNbits. Nie jest wymagana żadna dodatkowa konfiguracja - LNbits działa.



### Zarządzanie użytkownikami



Jedną z najpotężniejszych funkcji LNbits jest możliwość tworzenia wielu niezależnych użytkowników, każdy z uwierzytelnianiem hasłem i izolowanymi portfelami. Taka architektura umożliwia korzystanie z płynności węzła Umbrel, oferując jednocześnie całkowicie odizolowane subkonta do różnych zastosowań: biznesowych, rodzinnych, pracowniczych, projektowych itp.



W menu bocznym kliknij "Użytkownicy", aby uzyskać dostęp do zarządzania użytkownikami. Kliknij "CREATE ACCOUNT", aby dodać nowego użytkownika.



![Gestion des utilisateurs](assets/fr/05.webp)



Wypełnij formularz tworzenia użytkownika:




- Nazwa użytkownika**: Nazwa użytkownika logowania (przykład: "satoshi")
- Ustaw hasło**: Aktywuj tę opcję, aby ustawić hasło uwierzytelniania
- Hasło** i **Powtórz hasło**: Ustaw hasło dla tego użytkownika



![Création utilisateur satoshi](assets/fr/06.webp)



Opcjonalne pola (klucz publiczny Nostr, e-mail, imię, nazwisko) można pozostawić puste w celu minimalnej konfiguracji. Kliknij "UTWÓRZ KONTO", aby potwierdzić.



![Confirmation utilisateur créé](assets/fr/07.webp)



Nowy użytkownik pojawi się teraz na liście użytkowników ze swoim unikalnym identyfikatorem i nazwą użytkownika.



![Liste des utilisateurs](assets/fr/08.webp)



**Ważna uwaga**: Każdy użytkownik może zalogować się całkowicie niezależnie przy użyciu własnego hasła. Administrator SuperUser zachowuje pełną kontrolę za pośrednictwem interfejsu administracyjnego.



### Zarządzanie wallet użytkownika



Teraz, gdy użytkownik "satoshi" został utworzony, musisz przypisać mu wallet Lightning. Kliknij ikonę wallet (druga ikona) dla danego użytkownika, a następnie "CREATE NEW WALLET".



![Gestion des wallets](assets/fr/09.webp)



Zostanie wyświetlone okno dialogowe z monitem o nadanie nazwy wallet. Wprowadź opisową nazwę (np. "Wallet of Satoshi") i wybierz wyświetlaną walutę (CUC, USD, EUR itp.).



![Création wallet](assets/fr/10.webp)



Kliknij na "CREATE". LNbits natychmiast wygeneruje działający wallet Lightning dla tego użytkownika.



![Confirmation wallet créé](assets/fr/11.webp)



Zobaczysz teraz dwa istniejące portfele: domyślny wallet "LNbits wallet" utworzony automatycznie i nowy "Wallet Of Satoshi". Aby uprościć obsługę, możesz usunąć domyślny wallet, klikając ikonę usuwania (czerwony kosz na śmieci).



![Wallet final unique](assets/fr/12.webp)



Użytkownik "satoshi" ma teraz pojedynczy, wyraźnie zidentyfikowany wallet. Każdy użytkownik wallet działa całkowicie autonomicznie, korzystając z płynności bazowego węzła LND.



**Kluczowa koncepcja**: Wszystkie te portfele współdzielą globalną płynność Twojego węzła Umbrel. Nie tworzysz nowych kanałów Lightning dla każdego wallet - LNbits działa jako inteligentna warstwa księgowa, która zarządza alokacją środków w ramach istniejącej infrastruktury Lightning. Na tym polega moc systemu multi-wallet LNbits.



### Logowanie użytkownika



Wyloguj się z konta SuperUser (ikona w prawym górnym rogu) i wróć do strony logowania LNbits. Możesz teraz zalogować się przy użyciu poświadczeń nowego użytkownika.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Wprowadź nazwę użytkownika ("satoshi") i hasło zdefiniowane wcześniej, a następnie kliknij "LOGIN". Użytkownik uzyskuje bezpośredni dostęp do swojego osobistego wallet, całkowicie odizolowanego od interfejsu administracyjnego.



### Interface od użytkownika wallet



Po zalogowaniu użytkownik uzyskuje dostęp do pełnego interfejsu wallet Lightning.



![Interface wallet utilisateur](assets/fr/14.webp)



Funkcje interfejsu :




- Bieżące saldo**: Wyświetlane w sats i w wybranej walucie (w tym przykładzie CUC)
- Główne działania**: PASTE REQUEST, CREATE INVOICE, ikona QR (szybkie skanowanie)
- Historia transakcji** : Pełna lista wszystkich płatności i wpływów
- Prawy panel boczny**: Opcje konfiguracji i dostępu



### Mobilny dostęp do wallet



Prawy panel boczny oferuje szczególnie praktyczną funkcję: mobilny dostęp do wallet. Rozwiń sekcję "Dostęp mobilny", aby odkryć dostępne opcje.



![Mobile Access](assets/fr/15.webp)



LNbits oferuje kilka sposobów korzystania z wallet na smartfonie:



**Opcja 1: Kompatybilne aplikacje mobilne




- Pobierz **Zeus** lub **BlueWallet** z App Store lub Google Play
- Aktywuj rozszerzenie **LndHub** w LNbits dla tego wallet
- Zeskanuj kod QR LndHub za pomocą aplikacji mobilnej, aby podłączyć wallet



**Opcja 2: Bezpośredni dostęp przez przeglądarkę mobilną**




- Kod QR wyświetlany w opcji "Export to Phone with QR Code" zawiera pełny adres URL wallet ze zintegrowanym uwierzytelnianiem
- Zeskanuj ten kod QR za pomocą smartfona, aby otworzyć wallet bezpośrednio w przeglądarce mobilnej
- Dodawanie strony do ekranu głównego w celu szybkiego dostępu



**Ważne zabezpieczenia**: Ten adres URL zawiera klucze API umożliwiające pełny dostęp do wallet. Nigdy nie udostępniaj go publicznie. Traktuj ten kod QR tak samo jak klucze prywatne Bitcoin - każdy, kto zeskanuje ten kod QR, uzyska pełny dostęp do wallet.



Ta mobilna funkcja zamienia instancję LNbits Umbrel w prawdziwy serwer Lightning wallet dla Ciebie i Twoich znajomych, zachowując przy tym pełną suwerenność nad Twoimi środkami dzięki samodzielnie hostowanemu węzłowi.



### Udostępnianie dostępu użytkownikom



Głównym przypadkiem użycia tej konfiguracji dla wielu użytkowników jest **współdzielenie portfeli z rodziną lub bliskim kręgiem**. Po utworzeniu użytkownika z dedykowanym wallet (takim jak "satoshi" w naszym przykładzie), można udostępnić te dane logowania zaufanym członkom gospodarstwa domowego.



**Bezpieczeństwo dostępu na Umbrel**: Dostęp do instancji LNbits na Umbrel jest naturalnie chroniony, ponieważ można uzyskać do niej dostęp tylko :




- W sieci lokalnej** : Członkowie gospodarstwa domowego podłączeni do tej samej sieci Wi-Fi/Ethernet mogą uzyskać dostęp do instancji
- Przez VPN**: Jeśli korzystasz z sieci VPN, takiej jak Tailscale skonfigurowanej na serwerze Umbrel, autoryzowani użytkownicy mogą uzyskać bezpieczny dostęp zdalny



Ta podwójna warstwa ochrony (dostęp do sieci + uwierzytelnianie użytkownika) sprawia, że opcja "Zezwalaj na tworzenie nowych użytkowników" jest mniej krytyczna w Umbrel. Tylko osoby, które mają już dostęp do sieci lub VPN, mogą uzyskać dostęp do interfejsu logowania.



**Typowy scenariusz**: Tworzysz konto "taty", konto "mamy", konto "biznesowe" i tak dalej. Każdy członek rodziny ma swój własny odizolowany wallet Lightning, jednocześnie korzystając ze wspólnej płynności węzła Umbrel. Wystarczy udostępnić nazwę użytkownika i hasło - użytkownik może następnie połączyć się z dowolnego urządzenia w sieci lokalnej lub za pośrednictwem sieci VPN Tailscale. Więcej informacji można znaleźć w naszym dedykowanym samouczku Tailscale:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Poznaj dostępne rozszerzenia



Wróć do interfejsu SuperUser i przejdź do menu "Rozszerzenia" w lewym panelu bocznym, aby odkryć cały ekosystem rozszerzeń LNbits.



![Extensions disponibles](assets/fr/16.webp)



LNbits oferuje bogaty katalog rozszerzeń, które przekształcają instancję w prawdziwą platformę usług Lightning:





- Szafa grająca**: System szaf grających zasilany przez sats (płatności Spotify)
- Bilety wsparcia**: Płatny system wsparcia (otrzymuj powiadomienia, aby odpowiadać na pytania)
- TPoS**: Bezpieczny, mobilny terminal dla sprzedawców detalicznych
- User Manager**: zaawansowane zarządzanie użytkownikami i wallet (z którego właśnie skorzystaliśmy)
- Wydarzenia**: Sprzedaż i zatwierdzanie biletów na wydarzenia
- LNURLDevices**: Zarządzanie punktami sprzedaży, bankomaty, podłączone przełączniki
- SMTP**: Umożliwia użytkownikom wysyłanie wiadomości e-mail i zdobywanie punktów
- Boltcards**: Programowanie kart NFC do płatności Lightning tap-to-pay
- NostrNip5**: Tworzenie adresów NIP5 dla domen
- Splitpayments**: Automatyczna dystrybucja płatności między wieloma portfelami



Każde rozszerzenie jest aktywowane jednym kliknięciem z poziomu tego interfejsu. Rozszerzenia oznaczone jako "FREE" są bezpłatne, a niektóre są dostępne w wersji "PAID". Zapoznaj się z katalogiem, aby zidentyfikować te, które odpowiadają Twoim potrzebom - niezależnie od tego, czy chodzi o biznes, zarządzanie rodziną, czy eksperymentowanie z możliwościami Lightning Network.



## Zalety i ograniczenia



**Korzyści**: Suwerenność finansowa (całkowita kontrola środków/kluczy/danych), elastyczność architektoniczna (bezstratna migracja VPS→full node), profesjonalny system rozszerzeń, intuicyjny interfejs.



**Ograniczenia** : Oprogramowanie w wersji beta (ostrożność co do ilości), bezpieczeństwo na odpowiedzialność administratora, adresy URL zawierające poufne klucze API (HTTPS obowiązkowy), zarządzanie wieloma użytkownikami wymaga odpowiedzialności administratora.



## Najlepsze praktyki



**Kopie zapasowe**: Poświadczenia Phoenixd Seed/LND, baza danych LNbits, pliki .env. Automatyzacja codzienna, przechowywanie poza serwerem produkcyjnym, szyfrowanie. Regularne testowanie przywracania.



**Konserwacja**: Regularnie sprawdzaj dostępność aktualizacji (LNbits, Lightning backend, system operacyjny). Zawsze sprawdzaj informacje o wydaniu przed ważnymi aktualizacjami.





- Na Umbrel**: App Store automatycznie powiadamia o nowych wersjach. Synchronizacja rozszerzeń poprzez "Zarządzaj rozszerzeniami" > "Aktualizuj wszystko". Sprawdzanie uwzględniania bazy danych SQLite w automatycznych kopiach zapasowych Umbrel.
- Na VPS**: Zaktualizuj ręcznie za pomocą `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Monitoruj logi systemowe: `sudo journalctl -u lnbits -f`.



## Wnioski



Własny hosting LNbits oferuje konkretną ścieżkę do suwerenności finansowej Lightning. VPS+Phoenixd oferuje lekkie rozwiązanie dla szybkich usług, Umbrel pełną integrację z istniejącym węzłem Bitcoin. Skalowalna architektura umożliwia ewolucję od prostego wallet dla wielu użytkowników do zaawansowanych przypadków użycia biznesowego.



Samodzielny hosting oznacza odpowiedzialność: tworzenie kopii zapasowych nasion, ochrona dostępu, rozpoczęcie od skromnych kwot. Dzięki tym środkom ostrożności LNbits staje się solidnym rozwiązaniem dla gospodarki Lightning, zachowując jednocześnie decentralizację i autonomię.



## Zasoby



### Oficjalna dokumentacja




- [Dokumentacja LNbits](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [Phoenixd GitHub](https://github.com/ACINQ/phoenixd)
- [Oficjalna instrukcja instalacji](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Przewodniki dla społeczności




- [Początkowa konfiguracja serwera Ubuntu](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) autor: Daniel P. Costas (bezpieczeństwo VPS krok po kroku)
- [Instalacja LNbits + Phoenixd na Ubuntu VPS](https://danielpcostas.dev/install-lnbits-phoenixd-vps-ubuntu/) by Daniel P. Costas (kompletny przewodnik)
- [LNbits Server on Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) by Axel
- [LNbits na VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes