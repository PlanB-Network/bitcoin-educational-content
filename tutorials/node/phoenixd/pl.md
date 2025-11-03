---
name: Phoenixd
description: Wdrażanie własnego minimalistycznego węzła Lightning za pomocą Phoenixd
---

![cover](assets/cover.webp)



Autonomia finansowa oznacza również kontrolowanie infrastruktury Lightning. Dla deweloperów i firm, które chcą zintegrować Bitcoin Lightning ze swoimi aplikacjami, **Phoenixd** stanowi idealne rozwiązanie: minimalistyczny, wyspecjalizowany węzeł Lightning z automatycznym zarządzaniem płynnością.



Phoenixd to serwer Lightning opracowany przez ACINQ, zaprojektowany specjalnie do wysyłania i odbierania płatności Lightning za pośrednictwem interfejsu API HTTP. W przeciwieństwie do w pełni funkcjonalnych implementacji, takich jak LND lub Core Lightning, Phoenixd abstrahuje całą złożoność zarządzania kanałami, zachowując przy tym samodzielną ochronę środków.



W tym samouczku przyjrzymy się, jak zainstalować, skonfigurować i używać Phoenixd do tworzenia aplikacji Lightning z samodzielnie hostowaną infrastrukturą i łatwym w użyciu interfejsem API.



## Czym jest Phoenixd?



Phoenixd to minimalny, wyspecjalizowany węzeł Lightning opracowany przez ACINQ. Jest to rozwiązanie przeznaczone dla programistów i przedsiębiorstw, które chcą zintegrować Lightning ze swoimi aplikacjami bez złożoności zarządzania Full node.



### Zasada działania



**Phoenixd to minimalny węzeł Lightning, który wykorzystuje ACINQ jako dostawcę usług LSP (Lightning Service Provider) w celu zapewnienia automatycznej płynności. Po otrzymaniu płatności Lightning automatycznie otwiera kanały z węzłami ACINQ, aby przydzielić niezbędną przepustowość przychodzącą. Ta płynność "w locie" jest natychmiastowa, ale naliczana w wysokości dokładnie **1% + opłaty Mining** otrzymanej kwoty.



**Zautomatyzowane zarządzanie:** System zarządza trzema kluczowymi Elements:




- Kanały Lightning**: Otwieraj, zamykaj i zarządzaj automatycznie zgodnie z potrzebami
- Płynność przychodząca/wychodząca**: Automatyczne dostarczanie poprzez łączenie i otwieranie kanałów
- Kredyt na opłaty** : Małe płatności niewystarczające do uzasadnienia kanału są przechowywane jako rezerwa na przyszłe opłaty



### Korzyści Phoenixd



**Użytkownik kontroluje swoje klucze prywatne (12-wyrazowe seed) i fundusze. Phoenixd generuje lokalnie Wallet bez udostępniania kluczy.



**Osobista infrastruktura:** Phoenixd działa na Twoim serwerze, dając Ci dostęp do szczegółowych dzienników, konfiguracji i kontroli API. Nie jesteś już zależny od usług stron trzecich w zakresie dostępu do swoich środków.



**Zintegrowane API:** Phoenixd posiada API HTTP do integracji z innymi usługami, natywną obsługę LNURL i tworzenie niestandardowych aplikacji.



**Łatwość integracji:** Dzięki prostemu interfejsowi API REST, Phoenixd można zintegrować z dowolną aplikacją lub usługą wymagającą płatności Lightning.



**Ważna uwaga:** Automatyczna płynność nadal pochodzi z ACINQ jako LSP (Lightning Service Provider). Phoenixd wykorzystuje ten sam mechanizm co Phoenix mobile do automatycznego zarządzania kanałami.



## Instalacja Phoenixd



### Wymagania wstępne



Phoenixd wymaga środowiska Linux (zalecane Ubuntu/Debian), z podstawowymi umiejętnościami obsługi wiersza poleceń. Aby uzyskać optymalną wydajność, będziesz potrzebować :





- Serwer Linux**: VPS lub lokalna maszyna ze stabilnym połączeniem
- OpenJDK 21** : Środowisko uruchomieniowe Java
- Stabilne połączenie internetowe**: Do synchronizacji z Lightning Network
- Nazwa domeny** (opcjonalnie) : Dla bezpiecznego dostępu HTTPS do API



### Pobieranie i instalacja



**1. Pobierz Phoenixd**



Przejdź do strony [GitHub releases] (https://github.com/ACINQ/phoenixd/releases) i pobierz najnowszą wersję dla swojej architektury:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Pierwsze uruchomienie



Uruchomienie Phoenixd w celu inicjalizacji:



```bash
./phoenixd
```



Przy pierwszym uruchomieniu zostaniesz poproszony o potwierdzenie dwóch ważnych kroków poprzez wpisanie "Rozumiem" :



**Komunikat 1 - Kopia zapasowa:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Zapisz te 12 słów** - to jedyna gwarancja powrotu do zdrowia.



**Komunikat 2 - Automatyczna płynność:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Wpisz "Rozumiem" dla każdego potwierdzenia.



![Premier démarrage](assets/fr/01.webp)



*Pierwsze uruchomienie Phoenixd: potwierdzenie kopii zapasowej i automatyczna płynność*



**3. Konfiguracja eksploatacyjna** (tylko w języku francuskim)



W przypadku pracy ciągłej należy utworzyć systemd :



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Usługa Phoenixd aktywna i działająca poprzez systemd i `auto-liquidity` przy 2m sat*



## Konfiguracja i bezpieczeństwo



### Plik konfiguracyjny



Phoenixd automatycznie tworzy `~/.phoenix/phoenix.conf` z podstawowymi parametrami:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**Kluczowe parametry:**




- `auto-liquidity`: Rozmiar automatycznie otwieranych kanałów (domyślnie: 2M Sats)
- http-password`: Hasło administratora dla API (tworzenie Invoice ORAZ wysyłanie płatności)
- http-password-limited-access`: Ograniczone hasło (tylko tworzenie Invoice)



### Bezpieczny dostęp dzięki HTTPS



Domyślnie interfejs API Phoenixd jest dostępny tylko za pośrednictwem lokalnego protokołu HTTP (`http://127.0.0.1:9740`). Aby korzystać z węzła z zewnątrz (aplikacje mobilne, inne serwery, integracje internetowe), należy skonfigurować bezpieczny dostęp HTTPS.



**Odwrotna zasada proxy:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** działa jako **reverse proxy**: nasłuchuje żądań HTTPS z Internetu na porcie 443, przekierowuje je do Phoenixd lokalnie (port 9740), a następnie wysyła zaszyfrowane odpowiedzi z powrotem do klienta.



**Certyfikat SSL/TLS** jest plikiem cyfrowym, który :




- Potwierdzenie tożsamości serwera** (zapobiega atakom typu man-in-the-middle)
- Włącza szyfrowanie HTTPS**: wszystkie dane, w tym hasła API, są szyfrowane podczas transportu
- Wydawane bezpłatnie** przez Let's Encrypt za pośrednictwem narzędzia certbot



Ta konfiguracja umożliwia :




- Bezpieczny dostęp do API z Internetu**
- Szyfrowanie haseł API** podczas transportu (aby zapobiec przesyłaniu ich w postaci zwykłego tekstu)
- Integracja Phoenixd** z zewnętrznymi aplikacjami wymagającymi HTTPS
- Zgodność ze standardami bezpieczeństwa** dla finansowych interfejsów API



Skonfiguruj ten odwrotny serwer proxy HTTPS za pomocą nginx:



**1. Konfiguracja Nginx**



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. Certyfikat SSL**



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Test działania



Sprawdź, czy Phoenixd działa prawidłowo:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Polecenia te powinny zwracać informacje JSON o stanie i saldzie węzła (początkowo puste).



![Commandes CLI](assets/fr/03.webp)



*Polecenia getinfo i getbalance do sprawdzania stanu węzła*



## Korzystanie z interfejsu API



### Pierwszy test odbioru



**1. Utwórz Błyskawicę** Invoice



Użyj interfejsu API, aby utworzyć swój pierwszy Invoice:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Zrozumienie automatycznego mechanizmu płynności



**Podstawowa zasada:** Kiedy otrzymujesz płatność Lightning, Phoenixd czasami musi otworzyć nowy kanał, aby móc ją odebrać. Otwarcie kanału wiąże się z opłatą, która jest **automatycznie odejmowana** od otrzymanej kwoty.



**Konkretny przykład z 100 000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Pierwszy test akceptacyjny: Sats 100 tys. otrzymane, saldo końcowe Sats 75.561 po odjęciu kosztów płynności*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Kalkulacja opłaty:**




- Opłata za usługę**: 1% przepustowości kanału (2 115 000 Sats) = 21 150 Sats
- Opłaty Mining**: ~3,289 Sats (za transakcję On-Chain)
- Razem**: 24 439 Sats odliczone automatycznie



**Weryfikacja za pomocą poleceń CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Saldo końcowe po wysłaniu płatności: 257 Sats pozostałe po wysyłce Lightning*



**Kredyt opłat za małe płatności:** Jeśli otrzymujesz płatności zbyt małe, aby uzasadnić otwarcie kanału (< ok. 25 tys. Sats), są one przechowywane w bezzwrotnym "kredycie opłat". Kredyt ten zostanie wykorzystany do uiszczenia przyszłych opłat za kanał, gdy otrzymasz wystarczającą kwotę.



**2. Postępuj zgodnie z otwarciem kanału**



Oglądaj dzienniki Phoenixd:



```bash
journalctl -u phoenixd -f
```



Zobaczysz otwarcie kanału i automatyczne potrącenie opłat za płynność. Opłaty różnią się w zależności od warunków Mempool Bitcoin, ale zawsze obejmują 1% opłaty za usługę plus bieżącą opłatę Mining.



**3. Sprawdź kanał**



```bash
./phoenix-cli listchannels
```



To polecenie wyświetla aktywne kanały wraz z ich statusem i saldem.



### Kompletne operacje API



Phoenixd udostępnia interfejs API REST na porcie 9740, umożliwiając :



**Podstawowe operacje:**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**Ważne dla kosztów:**




- Odbiór**: 1% + opłata Mining za automatyczną płynność
- Wysyłka**: 0.4% opłaty trasowej na Lightning Network



**Webhooks:** Webhooks umożliwiają Phoenixd **automatyczne powiadamianie** aplikacji o wystąpieniu zdarzenia (otrzymana płatność, zapłacony Invoice, otwarty kanał itp.) Zamiast stale prosić Phoenixd o aktualizacje, aplikacja otrzymuje natychmiastowe powiadomienie HTTP.



**Twój sklep internetowy automatycznie otrzymuje powiadomienie, gdy klient płaci za zamówienie, umożliwiając natychmiastowe zatwierdzenie transakcji.



Konfiguracja w pliku `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Zaawansowane aplikacje



### Integracje LNURL



Phoenixd natywnie obsługuje protokoły LNURL w celu zaawansowanej integracji:



**LNURL-Pay:** Płać za usługi kompatybilne z LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Pobieranie środków z usług LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Uwierzytelnianie przez Lightning w celu uzyskania dostępu do usług


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integracja z LNbits



LNbits może korzystać z Phoenixd jako źródła finansowania zgodnie z [oficjalną dokumentacją] (https://docs.lnbits.org/guide/wallets.html):



*konfiguracja *LNbits:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Ta integracja umożliwia tworzenie subkont LNbits obsługiwanych przez węzeł Phoenixd, zapewniając internetowy Interface do zarządzania wieloma portfelami Lightning.



### Aplikacje niestandardowe



Dzięki wszechstronnemu interfejsowi API REST można tworzyć aplikacje :



**E-commerce:** Bezpośrednia integracja płatności Lightning z Twoim sklepem


**Usługi darowizn:** Systemy darowizn z fakturami i automatycznymi webhookami


**Boty społecznościowe:** Boty Telegram/Discord z funkcjami napiwków


**Paywall Lightning:** Zawartość premium dostępna za opłatą Lightning



## Bezpieczeństwo i najlepsze praktyki



### Ochrona dostępu



**Hasła API:** Automatycznie generowane hasła są kluczami do skarbca Lightning. Nigdy ich nie udostępniaj i zmieniaj je w razie wątpliwości.



**Firewall:** Nigdy nie pozostawiaj portu 9740 otwartego bezpośrednio do Internetu. Zawsze używaj nginx z HTTPS.



**Zaawansowane uwierzytelnianie:** Rozważ VPN lub Tailscale, aby ograniczyć dostęp do serwera tylko do autoryzowanych urządzeń.



### Niezbędne kopie zapasowe



**Odzyskiwanie seed:** Zapisz swoje 12 słów w bezpiecznym miejscu, poza serwerem. To jedyna gwarancja odzyskania danych.



*katalog ~/.phoenix:** Regularnie twórz kopie zapasowe tego folderu (po zamknięciu Phoenixd), aby zachować stan kanału i przyspieszyć przywracanie.



**Kody odzyskiwania usług:** Zachowaj również kody zapasowe dla wszystkich usług, w których aktywowałeś 2FA za pomocą Phoenix.



### Monitorowanie i konserwacja



**Dzienniki monitorowania:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Aktualizacje:** Obserwuj [GitHub releases](https://github.com/ACINQ/phoenixd/releases) dla nowych wersji. Aktualizacja jest tak prosta, jak zastąpienie pliku binarnego i ponowne uruchomienie usługi.



## Porównanie z alternatywnymi rozwiązaniami



### Phoenixd vs Phoenix standard



**Standard Phoenix (mobilny) :**




- natychmiastowa instalacja, zero konfiguracji
- intuicyjny telefon komórkowy Interface
- automatyczne zapisywanie takie samo jak w Phoenixd
- brak API dla deweloperów
- ❌ Brak dostępu do szczegółowych dzienników



**Phoenixd (serwer) :**




- aPI HTTP dla integracji
- pełny dostęp do logów
- infrastruktura osobista
- wymaga umiejętności technicznych
- wymagana konserwacja serwera



**Oba używają ACINQ jako LSP dla automatycznej płynności.



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- całkowita kontrola, pełny protokół Lightning
- duża społeczność, dojrzały ekosystem
- złożone ręczne zarządzanie płynnością
- duża krzywa uczenia się



**Phoenixd :**




- automatyczne zarządzanie płynnością (jak Phoenix mobile)
- aPI dla deweloperów
- uproszczona konfiguracja
- używa ACINQ jako LSP (brak niezależnego routingu)
- mniej elastyczny niż kompletne węzły



## Rozwiązywanie typowych problemów



### Problemy z dostępem do API



**Autoryzacja nie powiodła się" błąd:**


1. Sprawdź hasło w pliku `~/.phoenix/phoenix.conf`


2. Sprawdź format uwierzytelniania `-u:password`


3. Upewnij się, że Phoenixd jest uruchomiony (`./phoenix-CLI getinfo`)



**Czas oczekiwania na połączenie:**




- Sprawdź, czy Phoenixd nasłuchuje na prawidłowym porcie (9740)
- Przetestuj dostęp lokalny przed skonfigurowaniem HTTPS
- Sprawdź logi: `journalctl -u phoenixd -f`



### Problemy z płynnością



**Płatności nie docierają :**


1. Sprawdź, czy kwota przekracza minimalny próg (~30 tys. Sats)


2. Sprawdź dzienniki, aby zidentyfikować błędy kanału


3. W razie potrzeby uruchom ponownie Phoenixd



**Saldo w pozycji "kredyt na wydatki":**


Małe płatności są przechowywane jako rezerwa. Otrzymanie większej kwoty spowoduje otwarcie kanału i zwolnienie tych środków.



## Wnioski



Phoenixd stanowi doskonały kompromis między łatwością użytkowania a techniczną niezależnością dla deweloperów. Oferuje proste, ale potężne API Lightning z automatycznym zarządzaniem płynnością, eliminując złożoność tradycyjnych węzłów Lightning.



Rozwiązanie to jest szczególnie przydatne dla deweloperów i firm, które chcą :




- Zintegruj Bitcoin Lightning ze swoimi aplikacjami
- Uniknięcie złożoności zarządzania kanałem Lightning
- Korzyści z samodzielnie hostowanej infrastruktury
- Prosty, niezawodny interfejs API



Dzięki Phoenixd możesz zbudować własną prywatną infrastrukturę Lightning z nowoczesnym interfejsem API REST i automatycznym zarządzaniem aspektami technicznymi. Jest to idealne rozwiązanie do demokratyzacji integracji Lightning w projektach.



## Przydatne zasoby



### Oficjalna dokumentacja




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Kod źródłowy i wydania
- Strona Phoenix Server**: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Pełna dokumentacja
- FAQ Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Często zadawane pytania



### Wsparcie społeczności




- Problemy GitHub** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Wsparcie techniczne
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Wiadomości i ogłoszenia