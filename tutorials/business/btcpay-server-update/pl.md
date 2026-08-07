---
name: Aktualizacja BTCPay Server
description: Zastosuj aktualizację bezpieczeństwa w swojej instancji BTCPay Server i wymień dane uwierzytelniające, które mają znaczenie
---

![cover](assets/cover.webp)

Prowadzenie własnego procesora płatności oznacza, że jesteś także własnym zespołem bezpieczeństwa. Kiedy opiekunowie BTCPay Server publikują wydanie naprawiające lukę bezpieczeństwa, nikt nie załata Twojej instancji za Ciebie: aktualizacja, weryfikacja i następująca po nich wymiana danych uwierzytelniających należą do Ciebie.

Ten poradnik przeprowadza Cię przez całą procedurę, niezależnie od sposobu, w jaki wdrożyłeś BTCPay Server: sprawdzenie działającej wersji, zastosowanie aktualizacji odpowiedniej dla Twojego typu wdrożenia, weryfikację, że rzeczywiście się powiodła, oraz wymianę sekretów, które atakujący mógł przechwycić, gdy Twoja instancja była podatna.

Jeśli jeszcze nie wdrożyłeś BTCPay Server, zacznij od przewodnika instalacji:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Krytyczna podatność z sierpnia 2026

⚠️ **Krytyczny alert bezpieczeństwa (7 sierpnia 2026):** krytyczna podatność dotycząca BTCPay Server jest aktywnie wykorzystywana i może prowadzić do utraty środków. Natychmiast zaktualizuj swoją instancję do **wersji 2.4.2** przez `Admin Dashboard > Server > Maintenance > Update`, a następnie sprawdź, czy w stopce wyświetla się `2.4.2`. Jeśli nie możesz zaktualizować od razu, wyłącz swój BTCPay Server. Po aktualizacji musisz również całkowicie odświeżyć swoje macaroons oraz plik `macaroons.db`, całkowicie odświeżyć ciągi uwierzytelniające wszelkich innych backendów Lightning, a jeśli wygenerowałeś gorący portfel on-chain wewnątrz BTCPay Server — przenieś te środki i utwórz portfel od nowa. Integratorzy powinni dodatkowo zaktualizować NBXplorer do wersji 2.6.10. Źródło: [Informacje o wydaniu BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Wersja 2.4.2 została opublikowana 7 sierpnia 2026 roku. Informacje o wydaniu podają, że naprawia ona krytyczną podatność, która była już wykorzystywana na wolności, zgłoszoną przez `brunoerg` i `benthecarman` w ramach inicjatywy Bitcoin Red Team. To samo wydanie naprawia również obejście uwierzytelniania dwuskładnikowego TOTP przez uwierzytelnianie Greenfield Basic oraz domyślnie wyłącza uwierzytelnianie Greenfield Basic pięć minut po utworzeniu konta.

Z określenia „aktywnie wykorzystywana” wynikają dwie konsekwencje:

- **Aktualizacja nie jest opcjonalna ani nie jest czymś, co można zaplanować na przyszły tydzień.** Niezałatana instancja dostępna z internetu musi zostać albo zaktualizowana, albo wyłączona.
- **Sama aktualizacja nie wystarcza.** Jeśli Twoja instancja została skompromitowana przed załataniem, atakujący może już mieć kopie Twoich danych uwierzytelniających Lightning oraz materiału kluczy gorącego portfela, który BTCPay Server wygenerował dla Ciebie. Te sekrety pozostają ważne po aktualizacji, dopóki ich nie wymienisz. Poniższa sekcja o wymianie to część, którą ludzie pomijają, i właśnie ona rzeczywiście chroni Twoje środki.

## Krok 1 — Ustal, jaką wersję uruchamiasz

Zaloguj się do swojego BTCPay Server i spójrz na **stopkę dowolnej strony**: wyświetla się tam ciąg z numerem wersji. Możesz również otworzyć `Admin Dashboard > Server > Maintenance`, gdzie widoczna jest bieżąca wersja oraz elementy sterujące aktualizacją.

Jeśli Twoja instancja udostępnia API Greenfield, `GET /api/v1/server/info` również zwraca wersję.

Wszystko poniżej `2.4.2` jest podatne.

## Krok 2 — Zaktualizuj

### Samodzielnie hostowane wdrożenie Docker (standardowa instalacja)

Dotyczy to oficjalnego wdrożenia Docker, czyli tego, które otrzymujesz zgodnie z dokumentacją BTCPay Server, z instalatora LunaNode działającego jednym kliknięciem oraz z większości instalacji na VPS.

Najprostsza droga to interfejs internetowy:

1. Przejdź do `Admin Dashboard > Server > Maintenance`.
2. Kliknij **Update**.
3. Poczekaj, aż kontenery zostaną pobrane i uruchomione ponownie. Interfejs będzie niedostępny przez kilka minut.

Jeśli interfejs internetowy jest nieosiągalny lub wolisz widzieć logi, zrób to przez SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

W domyślnej instalacji `$BTCPAY_BASE_DIRECTORY` to `/root`, więc katalogiem jest `/root/btcpayserver-docker`. Skrypt pobiera najnowsze obrazy, odtwarza kontenery i wypisuje wynikowe wersje.

Wdrożenie Docker dostarcza NBXplorer razem z BTCPay Server, więc standardowa aktualizacja podnosi także NBXplorer do zalecanej wersji `2.6.10`. Jeśli uruchamiasz NBXplorer oddzielnie — co jest typowe dla integratorów i niestandardowych stosów — zaktualizuj go jawnie.

### Umbrel

Otwórz pulpit Umbrel, przejdź do **App Store**, znajdź BTCPay Server i zastosuj aktualizację, jeśli jest dostępna.

⚠️ **Ważne:** paczki z app store są przepakowywane przez zespół Umbrel i mogą być opóźnione względem wydania nadrzędnego o godziny lub dni. Po aktualizacji sprawdź wersję w stopce BTCPay Server. Jeśli nadal jest niższa niż `2.4.2`, **zatrzymaj aplikację** z pulpitu Umbrel i poczekaj na przepakowane wydanie, zamiast pozostawiać działającą podatną instancję.

Dedykowany przewodnik Umbrel opisuje samą aplikację:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Ta sama logika: zaktualizuj BTCPay Server z marketplace StartOS, a następnie zweryfikuj wersję w stopce. Jeśli przepakowana wersja to jeszcze nie `2.4.2`, zatrzymaj usługę, dopóki nią nie będzie.

### Hosting zarządzany i zewnętrzny

Jeśli Twoją instancją zarządza ktoś inny (dostawca hostingu, stowarzyszenie, serwer znajomego), potwierdzenie nadal jest Ci potrzebne. Poproś operatora o ciąg z numerem wersji widoczny w stopce i zapytaj wprost, czy przeprowadzono opisaną poniżej wymianę danych uwierzytelniających po aktualizacji. „Zaktualizowaliśmy” to nie ta sama odpowiedź co „wymieniliśmy Twoje macaroons”.

## Krok 3 — Zweryfikuj, że aktualizacja rzeczywiście się powiodła

Odśwież interfejs BTCPay Server i odczytaj wersję w stopce. Musi pokazywać `2.4.2` lub wyższą.

Nie polegaj na tym, że polecenie aktualizacji zakończyło się bez błędu: na maszynach o ograniczonych zasobach pobieranie obrazu może zawieść po cichu i pozostawić działający poprzedni kontener. Sprawdzaj wersję, za każdym razem.

## Krok 4 — Wymień swoje dane uwierzytelniające

To krok, który zamienia „załatane” w „bezpieczne”. Ponieważ podatność była wykorzystywana jeszcze przed wydaniem poprawki, traktuj każdy sekret przechowywany przez Twoją instancję jako potencjalnie znany atakującemu.

### Lightning: LND

Wygeneruj ponownie macaroons **oraz** plik `macaroons.db`. Usunięcie samych plików macaroon nie wystarcza — LND wyprowadza macaroons z klucza głównego przechowywanego w `macaroons.db`, więc atakujący posiadający kopię starego macaroona zachowuje dostęp, dopóki ta baza danych nie zostanie odtworzona.

Procedura jest następująca: zatrzymaj LND, usuń `macaroons.db` oraz pliki `*.macaroon` z katalogu sieci (dla sieci głównej jest to `data/chain/bitcoin/mainnet/` w katalogu danych LND), a następnie uruchom ponownie i odblokuj LND, co je odtworzy. Najpierw wykonaj kopię zapasową katalogu i ponownie sparuj każdą aplikację, która używała starych macaroons — sam BTCPay Server, Zeus, Thunderhub, RTL, Alby oraz każdy napisany przez Ciebie skrypt.

Jeśli udostępniasz LND również przez internet, przy tej samej okazji przejrzyj jego certyfikat TLS oraz wszelkie dane uwierzytelniające w `lnd.conf`.

### Lightning: inne backendy

Wszystko, co uwierzytelnia się w Twoim węźle za pomocą ciągu znaków, musi otrzymać nowy ciąg:

- **Core Lightning**: wygeneruj ponownie rune lub dane uwierzytelniające dostępu używane przez połączenie.
- **Phoenixd**: wymień hasło HTTP.
- **LNbits i podobne**: unieważnij i wystaw ponownie klucze administratora oraz klucze do faktur.
- **Ciągi połączenia ze zdalnym węzłem** przechowywane w ustawieniach sklepu BTCPay Server: przepisz je z nowymi sekretami.

### Gorący portfel on-chain wygenerowany wewnątrz BTCPay Server

Jeśli pozwoliłeś BTCPay Server wygenerować dla siebie portfel on-chain — w przeciwieństwie do podłączenia portfela sprzętowego lub zaimportowania xpub, którego klucze nigdy nie dotknęły serwera — ten seed znajdował się na tej maszynie.

Uznaj go za spalony:

1. Utwórz nowy portfel, najlepiej z portfelem sprzętowym, aby klucze nigdy więcej nie znajdowały się na serwerze.
2. Przenieś wszystkie środki ze starego portfela do nowego.
3. Zastąp schemat derywacji w ustawieniach sklepu nowym portfelem.
4. Nigdy nie używaj ponownie starego seeda.

Konfiguracje typu watch-only (xpub lub portfel sprzętowy) tego nie wymagają: klucze prywatne nigdy nie znajdowały się na serwerze. Właśnie dlatego przewodnik instalacji je zaleca.

### Konta BTCPay Server i klucze API

Przy tej samej okazji:

- Zmień hasła wszystkich kont użytkowników w instancji.
- Unieważnij i wystaw ponownie wszystkie **klucze API** Greenfield.
- Skonfiguruj od nowa uwierzytelnianie dwuskładnikowe, biorąc pod uwagę, że 2.4.2 naprawia obejście 2FA.
- Otwórz `Admin Dashboard > Server > Users` i sprawdź, czy nie istnieje żadne nieoczekiwane konto.
- Przejrzyj ostatnie **wypłaty**, **pull payments** i **zwroty** w poszukiwaniu wpisów, których nie utworzyłeś.
- Przejrzyj swoje webhooki i ich sekrety.

## Krok 5 — Bądź na bieżąco przed następnym razem

Wydania bezpieczeństwa pomagają tylko tym operatorom, którzy o nich usłyszą:

- Obserwuj [wydania BTCPay Server na GitHubie](https://github.com/btcpayserver/btcpayserver/releases) — GitHub może wysyłać Ci e-mail o każdym nowym wydaniu repozytorium.
- Śledź kanały ogłoszeń projektu oraz [oficjalny blog](https://blog.btcpayserver.org/).
- Utrzymuj swoją instancję na wersji, którą możesz szybko zaktualizować: im większe masz zaległości, tym bardziej bolesna staje się awaryjna aktualizacja.

Samodzielne hostowanie daje Ci suwerenność nad Twoimi płatnościami. Kosztem tej suwerenności jest właśnie to: czytanie informacji o wydaniach i bycie tym, kto łata.
