---
name: Bitcoin Keeper
description: Bitcoin mobilny wallet dla bezpieczeństwa i multi-sig
---

![cover](assets/cover.webp)



Bezpieczne zarządzanie bitcoinami stanowi poważne wyzwanie dla każdego posiadacza świadomego stawki związanej z suwerennością finansową. Pomiędzy prostotą mobilnego wallet a solidnością rozwiązania multi-sig, luka techniczna może wydawać się zniechęcająca dla wielu użytkowników. Bitcoin Keeper znajduje się dokładnie na tym przecięciu, oferując progresywne podejście do bezpieczeństwa, które towarzyszy użytkownikom w miarę ich ewolucji.



Bitcoin Keeper to aplikacja mobilna typu open source, dedykowana wyłącznie Bitcoin, opracowana przez zespół BitHyve. Jej ambicją jest udostępnienie zaawansowanego zarządzania portfelem, zwłaszcza konfiguracji z wieloma podpisami, przy jednoczesnym zachowaniu intuicyjnego interfejsu dla początkujących. Aplikacja przyjmuje hasło "Secure today, Plan for tomorrow", odzwierciedlając filozofię długoterminowego wsparcia.



W przeciwieństwie do portfeli ogólnych, które zarządzają wieloma kryptowalutami, Bitcoin Keeper koncentruje się wyłącznie na Bitcoin. Takie podejście ogranicza potencjalną powierzchnię ataku i znacznie upraszcza doświadczenie użytkownika. Aplikacja wyróżnia się również natywną integracją najbardziej rozpowszechnionych portfeli sprzętowych i zaawansowanymi funkcjami zarządzania UTXO.



## Czym jest Bitcoin Keeper?



### Filozofia i cele



Bitcoin Keeper został zaprojektowany w celu zaspokojenia specyficznych potrzeb użytkowników bitcoinów, którzy chcą zachować pełną kontrolę nad swoimi kluczami prywatnymi. Projekt w pełni uwzględnia podstawowe zasady Bitcoin: otwarty i możliwy do skontrolowania kod źródłowy, poszanowanie prywatności i suwerenność użytkownika. Do korzystania z aplikacji nie jest wymagana rejestracja ani podawanie danych osobowych, a może ona nawet działać w trybie offline w celu podpisywania operacji.



Głównym celem jest zaoferowanie elastycznego, przyszłościowego narzędzia do przechowywania BTC przez kilka lat, a nawet kilka pokoleń, dzięki dziedziczonym funkcjom. Aplikacja umożliwia użytkownikom rozpoczęcie od mobilnego wallet, a następnie stopniową ewolucję w kierunku bezpieczniejszych rozwiązań z wieloma podpisami.



### Architektura aplikacji



Bitcoin Keeper organizuje zarządzanie funduszami wokół dwóch różnych koncepcji. Hot Wallet** to prosty wallet z jednym kluczem, przechowywany w telefonie, przeznaczony do codziennych wydatków i skromnych kwot. Skarbce** to sejfy z wieloma podpisami (Multi-Key) wymagające kilku kluczy do autoryzacji wydatków, przeznaczone do długoterminowego bezpiecznego przechowywania.



### Główne cechy



Bitcoin Keeper obsługuje prawie wszystkie portfele sprzętowe na rynku: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport i Tapsigner firmy Coinkite. Integracja odbywa się za pomocą różnych metod w zależności od urządzenia: Skanowanie kodu QR, połączenie NFC lub import pliku.



Aplikacja oferuje również zaawansowane zarządzanie UTXO z etykietowaniem transakcji, kontrolę monet do ręcznego wybierania danych wejściowych podczas wysyłania oraz obsługę formatu PSBT dla częściowo podpisanych transakcji.



## Instalacja i wstępna konfiguracja



Bitcoin Keeper jest dostępna za darmo na Androida w Google Play Store i na iOS w App Store. Wydawcą aplikacji jest BitHyve. Przed instalacją upewnij się, że Twoje urządzenie jest wolne od złośliwego oprogramowania, aktualne i nie jest zrootowane ani po jailbreaku.



Przy pierwszym uruchomieniu aplikacja prosi o utworzenie zabezpieczającego kodu PIN. Kod ten chroni dostęp do wallet i szyfruje poufne dane lokalnie. Wybierz silny kod i zapamiętaj go. Następnie można aktywować uwierzytelnianie biometryczne (odcisk palca lub Face ID) w celu szybszego odblokowania.



![Installation et configuration du PIN](assets/fr/01.webp)



Następnie aplikacja prezentuje kilka ekranów wprowadzających wyjaśniających jej trzy filary: Tworzenie wallet w celu wysyłania i odbierania bitcoinów, zarządzanie kluczami z kompatybilnością sprzętową wallet oraz planowanie legacy w celu przekazywania bitcoinów. Naciśnij "Rozpocznij", a następnie wybierz "Rozpocznij od nowa", aby utworzyć nową konfigurację.



![Écrans d'introduction](assets/fr/02.webp)



## Odkrywanie interfejsu



Interfejs Bitcoin Keeper jest zorganizowany wokół czterech głównych zakładek dostępnych z dolnego paska nawigacyjnego:



![Les quatre onglets de l'application](assets/fr/03.webp)



Zakładka **Wallets** wyświetla portfele i ich salda. To tutaj uzyskujesz dostęp do swoich portfeli, aby wysyłać i odbierać bitcoiny. Tagi "Hot Wallet" i "Single-Key" lub "Multi-Key" pozwalają szybko zidentyfikować typ każdego wallet.



Zakładka **Keys** centralizuje zarządzanie kluczami podpisu. Znajduje się tutaj klucz mobilny wygenerowany przez aplikację, a także wszystkie klucze zaimportowane z portfeli sprzętowych. Jest to również miejsce dodawania nowych urządzeń do podpisu.



Zakładka **Concierge** oferuje usługi wsparcia: przesyłanie pytań do zespołu wsparcia i łączenie się z doradcami Bitcoin w celu uzyskania spersonalizowanej pomocy.



Zakładka **More** (Więcej opcji) daje dostęp do ustawień takich jak połączenie z serwerem osobistym, tworzenie kopii zapasowych kluczy, dziedziczenie dokumentów, preferencje wyświetlania i zarządzanie wallet.



## Połączenie z własnym serwerem



Aby wzmocnić poufność, Bitcoin Keeper umożliwia połączenie aplikacji z własnym serwerem Electrum, zamiast korzystania z domyślnych serwerów publicznych.



![Configuration du serveur Electrum](assets/fr/04.webp)



Na karcie Więcej przewiń w dół, aby znaleźć ustawienia serwera. Naciśnij "Dodaj serwer", aby skonfigurować nowe połączenie. Do wyboru są opcje "Serwer publiczny" (wstępnie skonfigurowane serwery publiczne) i "Prywatny Electrum" (własny serwer).



W przypadku serwera prywatnego wprowadź adres URL (np. umbrel.local dla węzła Umbrel) i numer portu (zwykle 50001). Aktywuj protokół SSL, jeśli serwer go obsługuje. Możesz także zeskanować kod QR konfiguracji. Po wprowadzeniu parametrów naciśnij przycisk "Połącz z serwerem".



Jeśli nie masz jeszcze własnego węzła Bitcoin, zapoznaj się z naszym samouczkiem dotyczącym Umbrel, prostego i niedrogiego sposobu na stworzenie własnego węzła:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Odbieranie bitcoinów



Na karcie Portfele wybierz wallet, z którego chcesz otrzymywać środki, naciskając go. Ekran wallet wyświetla saldo i trzy przyciski akcji: Wyślij Bitcoin, Odbierz Bitcoin i Wyświetl wszystkie monety.



![Réception de bitcoins](assets/fr/05.webp)



Naciśnij "Odbierz Bitcoin". Bitcoin Keeper wygeneruje nowy adres odbiorczy w formacie Bech32 (zaczynający się od bc1...) wraz z kodem QR. Możesz dodać etykietę do tego adresu, aby zidentyfikować źródło środków. Udostępnij adres nadawcy, wyświetlając kod QR lub kopiując adres tekstowy.



Aplikacja automatycznie generuje nowy adres dla każdego odbioru, zachowując prywatność użytkownika. W razie potrzeby użyj opcji "Get New Address", aby uzyskać pusty adres.



## Zarządzanie UTXO



Bitcoin Keeper oferuje pełną widoczność UTXO (niewydanych transakcji) składających się na saldo. Na ekranie wallet naciśnij "Wyświetl wszystkie monety", aby uzyskać dostęp do menedżera narożników.



![Gestion des UTXO](assets/fr/06.webp)



Ekran "Zarządzaj monetami" zawiera listę monet UTXO wraz z ich ilością i etykietą. Widok ten pozwala śledzić pochodzenie monet i porządkować je. Możesz wybrać określone UTXO poprzez "Wybierz do wysłania", aby wysłać je z kontrolą monet, unikając w ten sposób mieszania monet różnego pochodzenia.



## Wysyłanie bitcoinów



Aby wysłać, wybierz portfel źródłowy i naciśnij "Wyślij Bitcoin". Wprowadź adres docelowy (wklejony lub zeskanowany za pomocą kodu QR) i opcjonalnie dodaj etykietę, aby zidentyfikować odbiorcę.



![Envoi de bitcoins](assets/fr/07.webp)



Następny ekran umożliwia wprowadzenie kwoty do wysłania. Interfejs wyświetla dostępne saldo i przeliczenie waluty fiducjarnej. Wybierz priorytet ładowania: Niski (ekonomiczny, ~60 minut), Średni lub Wysoki (priorytetowy). Szacowane opłaty w sats/vbyte są wyświetlane w czasie rzeczywistym. Naciśnij "Wyślij", aby kontynuować.



![Confirmation et envoi](assets/fr/08.webp)



Ekran podsumowania wyświetla wszystkie szczegóły: wallet źródło, adres docelowy, priorytet transakcji, opłaty sieciowe, wysłana kwota i suma. Należy dokładnie sprawdzić te informacje, ponieważ transakcje Bitcoin są nieodwracalne. Naciśnij "Potwierdź i wyślij", aby wysłać transakcję.



Pojawi się potwierdzenie "Wyślij pomyślnie" z pełnym podsumowaniem. Transakcja jest widoczna w historii "Ostatnie transakcje" wraz z etykietą.



## Zapisywanie kluczy



Tworzenie kopii zapasowej klucza odzyskiwania jest kluczowym krokiem. Na karcie Więcej przejdź do sekcji "Kopia zapasowa i odzyskiwanie" i kliknij "Klucz odzyskiwania".



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



Na ekranie wyświetlany jest stan kopii zapasowych. Aby zweryfikować kopię zapasową, aplikacja prosi o potwierdzenie określonego słowa we frazie (np. siódmego słowa). Ta weryfikacja gwarantuje, że fraza odzyskiwania została poprawnie zapisana.



W "Ustawieniach klucza odzyskiwania" można wyświetlić pełną frazę za pomocą opcji "Wyświetl klucz odzyskiwania" i zobaczyć odcisk palca sygnatariusza klucza. Przechowuj 12-wyrazową frazę na papierze, w bezpiecznym miejscu, z dala od wilgoci i ognia. Nigdy nie przechowuj go na podłączonym urządzeniu.



## Dodanie klucza zewnętrznego (sprzęt wallet)



Jednym z głównych atutów Bitcoin Keeper jest integracja portfeli sprzętowych. Na karcie Klucze naciśnij przycisk "Dodaj klucz", aby dodać nowe urządzenie do podpisu.



![Ajout d'une clé hardware](assets/fr/10.webp)



Wybierz "Dodaj klucz ze sprzętu", aby podłączyć sprzęt wallet. Aplikacja obsługuje szeroką gamę urządzeń: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner i Specter Solutions.



### Konfiguracja Tapsigner



Tapsigner to karta NFC od Coinkite, szczególnie przystosowana do użytku mobilnego. Jeśli chcesz dowiedzieć się więcej, mamy dedykowany samouczek :



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Aby dodać Tapsigner, wybierz go z listy portfeli sprzętowych.



![Configuration du Tapsigner](assets/fr/11.webp)



Najpierw wprowadź 6-32-cyfrowy kod PIN wydrukowany z tyłu karty (domyślny w przypadku nowych kart) lub swój kod PIN, jeśli został już skonfigurowany. Naciśnij "Kontynuuj", a następnie zbliż Tapsigner do tylnej części telefonu, gdy wyświetlony zostanie komunikat "Gotowy do skanowania". Komunikacja NFC automatycznie importuje klucz publiczny. Następnie można dodać opis (np. "Métro Card"), aby zidentyfikować ten klucz.



## Tworzenie portfolio multisig



Po skonfigurowaniu kluczy można utworzyć wielopodpisowy wallet łączący kilka urządzeń. Na karcie Portfele kliknij opcję "Dodaj Wallet".



![Création d'un nouveau wallet](assets/fr/12.webp)



Dostępne są trzy opcje: "Utwórz Wallet" dla nowego portfela, "Importuj Wallet", aby przywrócić istniejący wallet, lub "Współpracuj Wallet" dla skarbca współdzielonego. Wybierz "Utwórz Wallet", a następnie "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



Następny ekran oferuje różne konfiguracje: "Pojedynczy przycisk", "2 z 3 przycisków wieloklawiszowych" lub "3 z 5 przycisków wieloklawiszowych". Aby dostosować multi-sig, naciśnij "Wybierz konfigurację niestandardową". Na przykład wybierz "1 z 2": wymagany jest pojedynczy podpis z dwóch możliwych kluczy.



Następnie wybierz klucze, które utworzą skarbiec. W naszym przykładzie połączyliśmy "Mobile Key" (klucz oprogramowania telefonu) z "TAPSIGNER" (karta Metro). Taka konfiguracja zapewnia redundancję: jeśli jeden z kluczy stanie się niedostępny, zawsze możesz wydać środki za pomocą drugiego.



![Finalisation du wallet multisig](assets/fr/14.webp)



Nadaj nazwę swojemu wallet (np. "Test PlanB"), dodaj opcjonalny opis i zaznacz wybrane przyciski. Naciśnij przycisk "Utwórz Wallet". Pojawi się komunikat potwierdzający "Wallet Created Successfully", przypominający o zapisaniu pliku odzyskiwania wallet.



Twój nowy multisig wallet pojawi się teraz w zakładce Portfele ze znacznikiem "Multi-key" i oznaczeniem "1 z 2".



### Zapisz plik konfiguracyjny



**W przeciwieństwie do prostego wallet, gdzie fraza odzyskiwania wystarcza do przywrócenia dostępu, wallet multisig wymaga również pliku konfiguracyjnego, który opisuje strukturę sejfu (które klucze biorą udział, ile wymaganych podpisów). Bez tego pliku, nawet ze wszystkimi frazami odzyskiwania, nie będzie można odbudować wallet.



![Export du fichier de configuration](assets/fr/15.webp)



Aby wyeksportować ten plik, wybierz swój wallet multisig w zakładce Wallets, a następnie naciśnij ikonę Settings (koło zębate) w prawym górnym rogu. W "Ustawieniach Wallet" kliknij "Plik konfiguracyjny Wallet". Dostępnych jest kilka opcji eksportu:





- Export PDF**: generuje dokument PDF zawierający wszystkie informacje wallet
- Pokaż QR**: wyświetla kod QR, który można zeskanować w celu zaimportowania konfiguracji do innego urządzenia
- Airdrop / File Export**: eksportuje plik za pośrednictwem opcji udostępniania w telefonie
- NFC**: udostępnianie przez NFC za pomocą kompatybilnego urządzenia



Przechowuj ten plik konfiguracyjny oddzielnie od fraz odzyskiwania, najlepiej na zaszyfrowanym lub wydrukowanym nośniku. W przypadku utraty telefonu plik ten w połączeniu z frazami odzyskiwania dla każdego klucza uczestniczącego umożliwi odtworzenie wallet multisig na Bitcoin Keeper lub innym kompatybilnym oprogramowaniu.



## Najlepsze praktyki



### Organizacja funduszu



Ustrukturyzuj swoje bitcoiny zgodnie z ich przeznaczeniem: gorący wallet Single-Key dla bieżących wydatków z ograniczonymi kwotami i jeden lub więcej Vaults Multi-Key dla długoterminowych oszczędności. Systematyczne oznaczanie UTXO pomoże ci śledzić, skąd pochodzą twoje fundusze, co jest szczególnie przydatne do zarządzania poufnością i unikania mieszania monet różnego pochodzenia.



Dbaj o bezpieczeństwo swojego telefonu: aktywuj blokadę biometryczną, regularnie aktualizuj system i zachowaj czujność wobec zainstalowanych aplikacji. I aktualizuj Bitcoin Keeper za pomocą łatek bezpieczeństwa.



### Bezpieczeństwo kopii zapasowych



Przechowuj co najmniej dwie kopie każdej frazy odzyskiwania na papierze, przechowywane w geograficznie oddzielnych lokalizacjach. W przypadku dużych kwot warto rozważyć grawerowany, odporny na katastrofy metal. Nigdy nie przechowuj tych zwrotów na urządzeniu podłączonym do Internetu i nigdy ich nie fotografuj.



W przypadku skarbców multi-sig należy również zapisać plik konfiguracyjny (plik odzyskiwania Wallet), który zawiera uczestniczące klucze publiczne i strukturę skarbca. Plik ten, w połączeniu z frazami odzyskiwania kluczy, umożliwia odbudowę wallet na dowolnym kompatybilnym oprogramowaniu, takim jak Sparrow lub Specter.



## Zalety i ograniczenia



### Najważniejsze wydarzenia





- Aplikacja oparta wyłącznie na Bitcoin zmniejsza złożoność i ryzyko
- Natywna integracja skarbców multisig ze wskazówkami krok po kroku
- Rozszerzona sprzętowa obsługa wallet (Tapsigner, Coldcard, Ledger, Jade itp.)
- Zaawansowane zarządzanie UTXO i kontrola monet
- Możliwość podłączenia do osobistego serwera Electrum
- Otwarty, możliwy do skontrolowania kod źródłowy



### Ograniczenia do rozważenia





- Interface głównie w języku angielskim
- Niektóre funkcje premium (Cloud Backup, Assisted Server) wymagają aktualizacji
- Konfiguracja Multisig wymaga wstępnego szkolenia



## Wnioski



Bitcoin Keeper wyróżnia się jako skalowalne rozwiązanie do zarządzania bitcoinami. Jego progresywne podejście, od prostego gorącego wallet do skarbców z wieloma podpisami, oznacza, że bezpieczeństwo można aktualizować w miarę zmieniających się potrzeb. Możliwość łatwej integracji portfeli sprzętowych, takich jak Tapsigner, toruje drogę do solidnych konfiguracji bez nadmiernej złożoności.



Orientacja wyłącznie na bitcoiny, otwarty kod źródłowy i poszanowanie prywatności sprawiają, że jest to wybór zgodny z podstawowymi wartościami ekosystemu Bitcoin.



Niniejszy poradnik obejmuje podstawowe funkcje Bitcoin Keeper w wersji darmowej. Aplikacja oferuje również funkcje premium (Cloud Backup, Assisted Server Backup, Canary Wallets), które będą przedmiotem dedykowanego poradnika. W nadchodzącym przewodniku będziemy również badać funkcję planowania spadkowego, która umożliwia przygotowanie transmisji bitcoinów do bliskich, dzięki ulepszonym skarbcom i towarzyszącym im dokumentom zintegrowanym z aplikacją.



## Zasoby





- Oficjalna strona internetowa: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Centrum pomocy: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Kod źródłowy: [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram: [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)