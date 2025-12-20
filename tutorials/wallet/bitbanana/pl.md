---
name: BitBanana
description: Mobilny menedżer dla węzła Lightning
---

![cover](assets/cover.webp)



W tym samouczku dowiesz się, jak zainstalować i skonfigurować BitBanana na Androida, aby kontrolować węzeł Lightning ze smartfona. Zobaczymy, jak połączyć aplikację z istniejącą infrastrukturą (Umbrel, RaspiBlitz, myNode lub dowolnym węzłem LND/Core Lightning), dokonywać płatności Lightning, zdalnie zarządzać kanałami, przeglądać przychody z routingu i tworzyć kopie zapasowe konfiguracji. Dowiesz się również o najlepszych praktykach bezpieczeństwa w celu ochrony dostępu do węzła i jak wypada on w porównaniu z Zeus, popularną alternatywą.



## Przedstawiamy BitBanana



BitBanana to aplikacja mobilna o otwartym kodzie źródłowym na Androida, która zamienia smartfon w kompletny pulpit nawigacyjny do zdalnego sterowania węzłem Lightning. W przeciwieństwie do portfeli Lightning, które osadzają lokalny węzeł w telefonie, BitBanana przyjmuje filozofię 100% zdalnej kontroli: aplikacja nie posiada satoshi i łączy się tylko z istniejącą infrastrukturą.



Opracowana przez Michaela Wünscha na licencji MIT, aplikacja gwarantuje całkowitą przejrzystość przy zerowym gromadzeniu danych osobowych i zweryfikowanych, powtarzalnych kompilacjach. BitBanana natywnie wspiera LND i Core Lightning poprzez standardowe URI (`lndconnect://` i `clngrpc://`), drastycznie upraszczając początkową konfigurację. Aplikacja rozpoznaje również LndHub i Nostr Wallet Connect dla użytkowników bez osobistego węzła, chociaż tryby te działają w trybie custodial z ograniczoną funkcjonalnością.



Interfejs oferuje pełny dostęp do wszystkich krytycznych funkcji węzła: wysyłania i odbierania płatności (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), zarządzania kanałami Lightning (otwieranie, zamykanie, dostosowywanie opłat, równoważenie), zaawansowanej kontroli monet i zarządzania wieżą strażniczą. BitBanana implementuje również kilka solidnych warstw bezpieczeństwa: blokadę biometryczną, tryb ukrycia, awaryjny kod PIN i natywną obsługę Tora w celu anonimizacji połączeń.



## Obsługiwane platformy i instalacja



### Instalacja



BitBanana jest dostępna wyłącznie dla systemu Android 8.0 lub nowszego. Aplikacja nie istnieje na iOS, a jej wersja nie jest planowana. Ograniczenie to wynika z historii projektu: BitBanana jest bezpośrednim następcą Zap Android, pierwotnie opracowanego przez Michaela Wünscha, który zdecydował się kontynuować pracę pod własną marką. Zap był rodziną oddzielnych aplikacji (Zap Android, Zap iOS, Zap Desktop) opracowanych przez różnych współpracowników z oddzielnymi bazami kodu. BitBanana kontynuuje tylko gałąź Android.



Ponadto ekosystem iOS stwarza znaczące ograniczenia regulacyjne i techniczne dla aplikacji Lightning nieobjętych nadzorem. W 2023 r. Apple odrzucił aktualizację Zeus z powodu "naruszenia licencji", a w 2024 r. Phoenix Wallet opuścił amerykański App Store w obliczu niepewności regulacyjnych dotyczących dostawców usług Lightning. Przeszkody te wyjaśniają, dlaczego wielu deweloperów Lightning preferuje Androida, który oferuje bardziej otwartą politykę dla aplikacji nieobjętych nadzorem.



Dla systemu Android dostępne są trzy metody instalacji: Google Play Store (ponad 5000 instalacji, automatyczne aktualizacje), F-Droid (odtwarzalne kompilacje, weryfikacja kodu źródłowego) lub ręczny APK z GitHub.



![BitBanana](assets/fr/01.webp)



Oficjalna strona bitbanana.app (po lewej) chwali się "100% samoobsługą z ZERO gromadzeniem danych". Centralny ekran pokazuje trzy opcje pobierania: F-Droid (zalecane), Google Play i APK. Ekran po prawej stronie pokazuje uprawnienia do powiadomień o płatnościach.



Aplikacja żąda uprawnień: sieć (połączenie węzła), kamera (kody QR), NFC (LNURL), usługi w tle (powiadomienia), biometria (bezpieczeństwo) i WireGuard VPN. Brak trackerów, zero gromadzenia danych. Włącz hasło lub blokadę biometryczną, aby zabezpieczyć dostęp.



## Konfiguracja początkowa



### Podłączanie do węzła LND



Aby połączyć BitBanana z węzłem LND (Umbrel, RaspiBlitz, myNode), uzyskaj URI `lndconnect` lub kod QR zawierający adres, certyfikat TLS i makaron uwierzytelniający.



W tym samouczku używamy węzła LND za pośrednictwem parasola. Więcej szczegółów można znaleźć w naszym dedykowanym samouczku :



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



W aplikacji Lightning Node przejdź do menu w prawym górnym rogu i wybierz "Connect wallet".



![BitBanana](assets/fr/04.webp)



Wybierz **gRPC (Tor)**, aby połączyć się przez Tor (zalecane). Wyświetlony zostanie kod QR i szczegóły (Host .onion, Port 10009, Macaroon).



![BitBanana](assets/fr/02.webp)



W BitBanana naciśnij "CONNECT NODE", zeskanuj kod QR lub wklej URI. Autoryzuj dostęp do kamery, a następnie sprawdź wyświetlony adres .onion przed potwierdzeniem.



*połączenie *Core Lightning**



Jeśli używasz Core Lightning (CLN) zamiast LND, proces pozostaje identyczny, z URI `clngrpc://` zawierającym wzajemne certyfikaty TLS. Core Lightning natywnie obsługuje BOLT12 (oferty), umożliwiając faktury wielokrotnego użytku i płatności cykliczne niedostępne w LND.



**Połączenie bez węzła osobistego (LNbits/hosted)**



Jeśli nie masz węzła Lightning, BitBanana może łączyć się z usługami hostowanymi za pośrednictwem LndHub (protokół używany przez BlueWallet i LNbits) lub Nostr Wallet Connect (NWC). Uwaga: tryby te działają w trybie powierniczym (usługa hostuje twoje fundusze) z ograniczoną funkcjonalnością. Nie będziesz w stanie zarządzać kanałami ani konfigurować opłat za routing i będziesz mógł tylko wysyłać i odbierać płatności Lightning.



Aby uzyskać więcej informacji na temat LNbits lub Nostr Wallet Connect, zapoznaj się z naszymi różnymi samouczkami:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Codzienne użytkowanie



### Interface główny



Ekran główny wyświetla saldo Lightning, a menu w lewym górnym rogu zapewnia dostęp do następujących sekcji: Kanały, Routing, Podpisz/Weryfikuj, Węzły, Kontakty, Ustawienia, Kopia zapasowa. Ikona zegara (w prawym górnym rogu) otwiera historię transakcji. Przyciski "Wyślij" i "Odbierz" na dole umożliwiają wysyłanie i odbieranie satoshis.



![BitBanana](assets/fr/05.webp)



### Piorun i płatności on-chain



![BitBanana](assets/fr/10.webp)



**Wysyłanie płatności:** Naciśnij przycisk "Wyślij" na ekranie głównym. Ekran płatności (po lewej) oferuje wklejenie adresu lub danych płatności w polu "Address lub dane płatności", ze skanerem QR w prawym górnym rogu do skanowania kodów. Można również wybrać kontakt zapisany w sekcji Kontakty, aby uniknąć konieczności skanowania za każdym razem.



BitBanana inteligentnie rozpoznaje wszystkie formaty płatności: klasyczne faktury Lightning (ciągi znaków zaczynające się od `lnbc`), Lightning Address (format e-mail, taki jak `utilisateur@domaine.com`), kody LNURL-pay do dynamicznych płatności, LNURL-withdraw do wypłaty środków, a nawet płatności Keysend bezpośrednio na klucz publiczny Lightning bez wcześniejszej faktury. Aplikacja automatycznie wykonuje niezbędne rozdzielczości LNURL w tle.



Po załadowaniu faktury BitBanana wyświetla pełne szczegóły: dokładną kwotę, szacowane opłaty za przekierowanie, opis płatności (jeśli został podany przez odbiorcę) i datę wygaśnięcia faktury. Po potwierdzeniu płatność jest kierowana przez kanały Lightning. W szczegółach transakcji można następnie wyświetlić trasę pokonywaną skok po skoku oraz faktycznie uiszczone opłaty.



**Odbierz płatność:** Naciśnij przycisk "Odbierz". Selektor (prawy ekran) pozwala wybrać między Lightning (natychmiastowa płatność za pośrednictwem kanałów) i On-Chain. W przypadku paragonu Lightning wprowadź żądaną kwotę w satoshis (lub pozostaw 0, aby utworzyć fakturę bez ustalonej kwoty do wypełnienia przez płatnika) i dodaj opcjonalny opis, który pojawi się na fakturze. BitBanana natychmiast wygeneruje fakturę Lightning z kodem QR do zeskanowania. Można również skopiować fakturę jako tekst i wysłać ją e-mailem. Gdy tylko płatność zostanie otrzymana, otrzymasz powiadomienie push, a transakcja pojawi się natychmiast w historii wraz ze wszystkimi szczegółami.



### Kanały i routing



![BitBanana](assets/fr/06.webp)



Sekcja "Kanały" wyświetla możliwości wysyłania/odbierania i zawiera listę kanałów z unikalnymi awatarami. Każdy kanał pokazuje podział płynności między saldo lokalne i zdalne. Dotknij kanału, aby uzyskać pełne szczegóły i działania (zamknięcie, zmiana opłat za routing). Trzy kropki w prawym górnym rogu zapewniają dostęp do opcji "Rebalance" w celu przywrócenia równowagi płynności kanałów. Przycisk "+" otwiera nowy kanał.



Sekcja Routing (ekran centralny) wyświetla przychody z przekierowań według okresu (1D, 1W, 1M, 3M, 6M, 1Y) ze szczegółową historią przekierowań w celu optymalizacji strategii.



Sign/Verify (prawy ekran) umożliwia kryptograficzne podpisywanie/weryfikację wiadomości w celu udowodnienia kontroli węzła.



### Wiele węzłów i parametry



![BitBanana](assets/fr/07.webp)



**Manage Nodes**: wyświetla listę węzłów, z przyciskami do ręcznego dodawania, skanowania QR lub przełączania między węzłami. W szczególności można skonfigurować różne typy połączeń z tym samym węzłem: LAN, VPN lub Tor.



**Manage Contacts**: przechowuje kontakty Lightning w celu szybkich płatności.



**Ustawienia**: dostosuj walutę, język, awatary. Sekcja bezpieczeństwa i prywatności: App Lock (PIN/biometria), Hide balance (tryb stealth), Tor (anonimizacja IP). Konfiguracja wyroczni cenowych, eksploratorów bloków, niestandardowych estymatorów opłat.



## Zalety i ograniczenia



**Najważniejsze cechy:**




- Całkowita mobilność: kontroluj swój węzeł Lightning z dowolnego miejsca
- Pełna funkcjonalność: płatności (LNURL, Lightning Address, BOLT 12), zarządzanie kanałami, kontrola monet, wieże strażnicze, wiele węzłów
- Bezpieczeństwo: PIN/biometria, tryb ukrycia, awaryjny PIN, natywny Tor, blokowanie zrzutów ekranu
- Darmowy, open source (MIT), zero prowizji, zero gromadzenia danych



**Ograniczenia:**




- Wymaga aktywnego węzła Lightning (lub LNbits w trybie powierniczym)
- Wersja na iOS nie jest planowana
- Zabezpieczenie dostępu do telefonu jest krytyczne (administrator macaroon = całkowity dostęp do węzła)



## Najlepsze praktyki



**Bezpieczeństwo:**




- Aktywuj blokadę PIN/biometryczną (zapobiega nieautoryzowanemu dostępowi do węzła)
- Skonfiguruj awaryjny kod PIN (usuwa poufne dane w przypadku przymusu)
- Nigdy nie udostępniaj swojego identyfikatora URI logowania ani makaronu
- Tryb ukrycia we wrogim środowisku



**Login:**




- VPN mesh (Tailscale, ZeroTier): najlepszy kompromis między szybkością i bezpieczeństwem
- Tor: maksymalna poufność, większe opóźnienia
- Clearnet: unikać, chyba że jest to konieczne (ujawnienie IP, otwarte porty)



### Kopia zapasowa i przywracanie



Na koniec dostępne jest menu "Kopia zapasowa", które umożliwia zapisanie konfiguracji w celu migracji telefonu lub ponownej instalacji.



![BitBanana](assets/fr/08.webp)



**Ważne:** Kopia zapasowa NIE zawiera seed ani kopii zapasowych kanałów (do wykonania na węźle). Zawiera: konfiguracje węzła (adresy, certyfikaty, makra), etykiety, kontakty, parametry. Przycisk Przywróć umożliwia zaimportowanie istniejącej kopii zapasowej. Przed zapisaniem wymagane jest potwierdzenie.



![BitBanana](assets/fr/09.webp)



Wprowadź hasło szyfrowania (prawy ekran). System otworzy selektor plików (lewy ekran), aby zapisać plik `BitBananaBackup_2025-XX-XX.dat`. Potwierdzenie "Utworzono kopię zapasową".



**Bezpieczeństwo:** Przechowuj kopie zapasowe zaszyfrowane (chmura osobista, USB, NAS). Nigdy nie udostępniaj plików ani haseł. Regularnie testuj przywracanie. Kopia zapasowa odzyskuje połączenia, a nie środki.



## BitBanana vs Zeus: Jaka jest różnica?



Jeśli szukasz aplikacji mobilnych do zarządzania węzłem Lightning, prawdopodobnie natkniesz się na Zeus, popularną alternatywę dla BitBanana. W przeciwieństwie do BitBanana, która koncentruje się wyłącznie na zdalnym sterowaniu istniejącym węzłem, Zeus przyjmuje bardziej kompleksowe podejście, oferując dwa tryby działania: węzeł Lightning osadzony bezpośrednio w aplikacji (tryb osadzony ze zintegrowanym LND) i zdalne połączenie z węzłem zewnętrznym, podobnie jak BitBanana.



Ta podwójna funkcjonalność sprawia, że Zeus jest szczególnie atrakcyjny dla początkujących, którzy chcą eksperymentować z Lightning bez wcześniejszej infrastruktury. Tryb wbudowany umożliwia natychmiastowe uruchomienie z kompletnym węzłem mobilnym, podczas gdy zaawansowani użytkownicy mogą przełączyć się na połączenie zdalne po skonfigurowaniu węzła osobistego. Zeus obsługuje również LND i Core Lightning do połączeń zdalnych, takich jak BitBanana.



Kolejną ważną zaletą Zeusa jest jego wieloplatformowa dostępność (iOS i Android), podczas gdy BitBanana pozostaje oparty wyłącznie na systemie Android. Zeus zawiera również infrastrukturę Olympus LSP, aby ułatwić otrzymywanie płatności Lightning za pośrednictwem kanałów just-in-time, system Point of Sale dla sprzedawców oraz zintegrowaną funkcję swap do zarządzania płynnością.



BitBanana zachowuje jednak swoje mocne strony: prostszy, bardziej usprawniony interfejs, lepsze wrażenia użytkownika (UX) dzięki wyłącznemu skupieniu się na zdalnym sterowaniu oraz podejście edukacyjne z kontekstowymi wyjaśnieniami. Zeus oferuje większą funkcjonalność, ale kosztem bardziej złożonego interfejsu. Aplikacja pozostaje szczególnie odpowiednia dla użytkowników, którzy chcą kontrolować węzeł wyłącznie na odległość, bez funkcji nadzorczych.



Aby dowiedzieć się więcej o Zeus, zapoznaj się z poniższymi samouczkami:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Wnioski



BitBanana zamienia smartfon z systemem Android w kompletny pulpit nawigacyjny Lightning, oferując operatorom węzłów niespotykaną dotąd mobilność. Aplikacja obejmuje wszystkie funkcje: płatności (wszystkie formaty), zarządzanie kanałami, kontrolę monet, wieże strażnicze, wiele węzłów, ze zwiększonym bezpieczeństwem (PIN/biometria, Tor, Emergency PIN).



Całkowicie suwerenna BitBanana nie gromadzi żadnych danych i nie narusza ani poufności, ani kontroli nad Twoimi środkami. Otwarty kod źródłowy (MIT) gwarantuje przejrzystość.



## Zasoby



### Oficjalna dokumentacja




- [strona BitBanana](https://bitbanana.app)
- [Pełna dokumentacja](https://docs.bitbanana.app)
- [kod źródłowy GitHub](https://github.com/michaelWuensch/BitBanana)



### Instalacja




- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)