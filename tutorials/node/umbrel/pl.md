---
name: Umbrel
description: Odkryj i zainstaluj Umbrel - Twój węzeł Bitcoin i serwer domowy
---

![cover](assets/cover.webp)



## Wprowadzenie



### Co to jest węzeł Bitcoin?



Węzeł Bitcoin to komputer, który uczestniczy w sieci Bitcoin poprzez uruchomienie oprogramowania Bitcoin Core lub alternatywnego klienta. Jego rola jest kluczowa dla działania i bezpieczeństwa sieci:





- **Przechowywanie Blockchain**: Utrzymuje kompletną, aktualną kopię Blockchain Bitcoin
- **Weryfikacja transakcji**: weryfikuje każdą transakcję i blok zgodnie z zasadami protokołu
- **Rozpowszechnianie informacji**: Udostępnia nowe transakcje i bloki innym węzłom
- **Budowanie konsensusu**: Przyczynia się do stosowania zasad sieciowych



Prowadzenie własnego węzła Bitcoin jest kluczowym krokiem w kierunku suwerenności finansowej, oferując kilka kluczowych korzyści:





- **Poufność**: Udostępniaj swoje transakcje bez ujawniania informacji stronom trzecim
- **Odporność na cenzurę**: Nikt nie może powstrzymać cię przed korzystaniem z Bitcoin
- **Niezależna weryfikacja**: Nie trzeba ufać węzłom innych osób, aby zweryfikować swoje transakcje
- **Budowanie konsensusu**: Przyczynianie się do stosowania zasad sieci Bitcoin
- **Wsparcie sieci**: Zostań aktywnym uczestnikiem dystrybucji i decentralizacji sieci



### Umbrel: Proste rozwiązanie do uruchamiania węzła Bitcoin



Umbrel to system operacyjny typu open source, który upraszcza instalację i zarządzanie węzłem Bitcoin. Przekształca również komputer w osobisty i prywatny serwer domowy, ułatwiając hostowanie :





- Kompletny węzeł Bitcoin
- Bitcoin podstawowe aplikacje (Electrs, Mempool.space)
- Inne usługi osobiste (przechowywanie w chmurze, streaming, VPN itp.)



Dzięki eleganckiemu i intuicyjnemu użytkownikowi Interface, Umbrel sprawia, że usługi self-hosted są dostępne dla wszystkich, przy zachowaniu pełnej kontroli nad danymi.



## Opcje instalacji parasola



Umbrel oferuje dwa główne sposoby korzystania ze swojego rozwiązania: opcję "pod klucz" (Umbrel Home) i bezpłatną wersję open source (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: Rozwiązanie pod klucz



Umbrel Home to wstępnie skonfigurowany serwer domowy, zaprojektowany specjalnie z myślą o optymalnym użytkowaniu. To kompleksowe rozwiązanie sprzętowe obejmuje:



**Cechy sprzętu**




- Wydajny procesor zoptymalizowany pod kątem samodzielnego hostingu
- Preinstalowana szybka pamięć masowa SSD
- Cichy system chłodzenia
- Kompaktowa, elegancka konstrukcja
- Zintegrowane porty USB i Ethernet



**Ekskluzywne korzyści**




- Instalacja plug-and-play: podłącz i pracuj
- Wsparcie premium z dedykowaną pomocą techniczną
- Gwarantowane automatyczne aktualizacje
- Zintegrowany kreator migracji
- Pełna gwarancja na sprzęt
- Pełne wsparcie dla wszystkich funkcjonalności



**Cena**: 399 € (cena może się różnić w zależności od sezonu)



### UmbrelOS: wersja open source



UmbrelOS to darmowa, otwarta wersja systemu operacyjnego Umbrel. To elastyczne rozwiązanie pozwala korzystać z własnego sprzętu, jednocześnie czerpiąc korzyści z podstawowych funkcji Umbrel.



**Korzyści**




- Całkowicie za darmo
- Otwarty, weryfikowalny kod źródłowy
- Wolność wyboru
- Zaawansowane opcje dostosowywania



**Obsługiwane platformy**




- Raspberry Pi 5: popularne i niedrogie rozwiązanie
- Systemy X86: Dla standardowych komputerów PC lub serwerów
- Maszyna wirtualna: Do testowania lub używania w istniejącej infrastrukturze



**Ograniczenia**




- Tylko wsparcie społeczności
- Niektóre zaawansowane funkcje zarezerwowane dla Umbrel Home
- Bardziej techniczna konfiguracja początkowa
- Wydajność zależy od wybranego sprzętu



Ta wersja jest idealna dla :




- Użytkownicy techniczni
- Ci, którzy już posiadają kompatybilny sprzęt
- Ludzie, którzy chcą się uczyć i eksperymentować
- Deweloperzy pragnący wnieść swój wkład w projekt



Oficjalne linki instalacyjne :




- [Instalacja na Raspberry Pi 5](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Instalacja na systemach x86 (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Instalacja maszyny wirtualnej](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



W tym poradniku skoncentrujemy się na instalacji UmbrelOS na Raspberry Pi 5, ale podstawowe zasady pozostają podobne dla innych platform.



## Instalacja Umbrel OS na Raspberry Pi 5



### Wymagane komponenty



Do tej instalacji potrzebne będą :





- Raspberry Pi 5 (4 GB lub 8 GB pamięci RAM)
- Oficjalne zasilanie Raspberry Pi Supply (kluczowe dla stabilności!)
- Karta microSD (minimum 32 GB)
- Czytnik kart microSD
- Zewnętrzny dysk SSD do przechowywania danych
- Kabel Ethernet
- Kabel USB do podłączenia dysku SSD



### Kroki instalacji



**Pobierz UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Odwiedź [oficjalną stronę internetową] (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Pobierz najnowszą wersję UmbrelOS dla Raspberry Pi 5



*instalacja **Balena Etcher***



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Pobierz i zainstaluj [Balena Etcher](https://www.balena.io/etcher/) na swoim komputerze



**Przygotowanie karty microSD**



![Insertion carte microSD](assets/fr/03.webp)




- Włóż kartę microSD do czytnika kart w komputerze



**Image flashing**



![Flashage UmbrelOS](assets/fr/04.webp)




- Uruchomienie Balena Etcher
- Wybierz pobrany obraz systemu UmbrelOS
- Wybierz kartę microSD jako miejsce docelowe
- Kliknij "Flash!" i poczekaj na zakończenie procesu
- Bezpieczne wysuwanie karty



**instalacja karty microSD**



![Installation microSD](assets/fr/05.webp)




- Włóż kartę microSD do Raspberry Pi 5



**Połączenie peryferyjne**



![Connexion périphériques](assets/fr/06.webp)




- Podłącz zewnętrzny dysk SSD do dostępnego portu USB
- Podłącz kabel Ethernet między komputerem Pi a routerem



**Włącz zasilanie**



![Démarrage du Pi](assets/fr/07.webp)




- Podłącz oficjalne zasilanie Raspberry Pi Supply
- Poczekaj kilka minut na uruchomienie systemu



**Pierwszy dostęp**



![Accès interface web](assets/fr/08.webp)




- Na urządzeniu podłączonym do tej samej sieci otwórz przeglądarkę
- Dostęp do strony internetowej Interface firmy Umbrel pod adresem: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Jeśli `umbrel.local` nie działa, należy znaleźć adres IP Address Raspberry Pi w sieci lokalnej. Możesz :




- Zapoznaj się z instrukcją obsługi routera Interface
- Korzystanie ze skanera sieciowego, takiego jak nmap
- Użyj polecenia `arp -a` w terminalu komputera



## Pierwszy krok na Umbrel



Po uruchomieniu aplikacji Umbrel i uzyskaniu do niej dostępu za pośrednictwem przeglądarki, wykonaj następujące kroki, aby rozpocząć:



### Konfiguracja początkowa



**Załóż konto**



![Création compte](assets/fr/10.webp)




- Wybierz nazwę użytkownika
- Ustaw bezpieczne hasło
- Będziesz potrzebować tych poświadczeń, aby uzyskać dostęp do Umbrel



**Potwierdzenie konta**



![Confirmation compte](assets/fr/11.webp)




- Kliknij "Dalej", aby uzyskać dostęp do pulpitu nawigacyjnego



**Odkrycie Interface**



![Interface Umbrel](assets/fr/12.webp)




- Dostęp do Umbrel App Store
- Odkryj wiele dostępnych aplikacji
- Zacznijmy od zainstalowania niezbędnych aplikacji dla Bitcoin



### Instalowanie aplikacji Bitcoin



**Węzeł Bitcoin**



![Bitcoin Node](assets/fr/13.webp)




- Pierwsza aplikacja do zainstalowania
- Pobierz i sprawdź cały Blockchain Bitcoin



**Elektorzy**



![Installation Electrs](assets/fr/14.webp)




- Serwer Electrum do łączenia portfeli Bitcoin
- Synchronizuje się z węzłem Bitcoin



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Wyświetlacz Interface dla Blockchain
- Śledzi transakcje i bloki w czasie rzeczywistym



## Śledzenie transakcji za pomocą Mempool.space



Mempool.space to eksplorator Blockchain o otwartym kodzie źródłowym, który zapewnia wizualizację sieci Bitcoin w czasie rzeczywistym. Pozwala śledzić transakcje i zrozumieć, w jaki sposób transakcje rozprzestrzeniają się w sieci.



### Zrozumienie Mempool i potwierdzeń



"Mempool" (pula pamięci) jest jak wirtualna poczekalnia, w której przechowywane są wszystkie niepotwierdzone transakcje Bitcoin, zanim zostaną włączone do bloku. Oto jak przetwarzana jest transakcja:



1. **Rozgłaszanie**: Po wysłaniu transakcji jest ona najpierw rozgłaszana w sieci Bitcoin


2. ** Oczekiwanie w Mempool**: Oczekiwanie na wybór przez Miner na podstawie kosztów


3. **Pierwsze potwierdzenie**: Małoletni włącza go do bloku (1. potwierdzenie)


4. **Dodatkowe potwierdzenia**: Każdy nowy blok wydobyty po bloku zawierającym transakcję użytkownika dodaje potwierdzenie



Zalecana liczba potwierdzeń zależy od ilości :




- W przypadku małych kwot: 1-2 potwierdzenia mogą wystarczyć
- W przypadku dużych kwot: 6 potwierdzeń jest ogólnie uważanych za bardzo bezpieczne



### Eksploruj Interface z Mempool.space



1. **Strona główna** zawiera przegląd sieci Bitcoin:




   - Ostatnio wydobyte bloki
   - Szacunki kosztów dla różnych priorytetów
   - Obecny stan Mempool



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Wyszukaj transakcję**: Aby śledzić konkretną transakcję, wklej jej identyfikator (txid) do paska wyszukiwania w górnej części strony.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Analiza szczegółów transakcji



Po znalezieniu transakcji Mempool.space przedstawia pełną analizę:



1. **Najważniejsze informacje** :




   - Status (potwierdzony lub nie)
   - Wydatki zapłacone (w Sats/vB)
   - Szacowany czas potwierdzenia



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Struktura transakcji** :




   - Wizualna reprezentacja wejść i wyjść
   - Szczegółowa lista zaangażowanych adresów
   - Przeniesione kwoty



3. **Dane techniczne** :




   - Waga transakcji
   - Rozmiar wirtualny
   - Używany format i wersja
   - Inne specyficzne metadane



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Zalety korzystania z Mempool.space na Umbrel



1. **Poufność**: Twoje żądania przechodzą przez Twój własny węzeł


2. **Niezależność**: Nie trzeba polegać na usługach innych firm


3. **Niezawodność**: Dostęp do danych nawet w przypadku awarii przeglądarek publicznych



Dzięki tej aplikacji możesz skutecznie monitorować swoje transakcje, zrozumieć, w jaki sposób opłaty wpływają na szybkość potwierdzeń i lepiej zrozumieć, jak działa sieć Bitcoin.



## Podłączanie Wallet Bitcoin do węzła



### Konfiguracja elektryków



**Połączenie lokalne**



![Connexion locale](assets/fr/18.webp)




- Do użytku w sieci lokalnej
- Szybsza i łatwiejsza konfiguracja



**Zdalne połączenie przez Tor**



![Connexion Tor](assets/fr/19.webp)




- Aby uzyskać dostęp do węzła z dowolnego miejsca
- Większe bezpieczeństwo i prywatność



### Połączenie z Sparrow Wallet



**Dostęp do parametrów**



![Paramètres Sparrow](assets/fr/20.webp)




- Open Sparrow Wallet
- Przejdź do Preferencje > Serwer
- Kliknij "Modyfikuj istniejące połączenie"



**Wybór typu połączenia**



Sparrow oferuje trzy tryby połączenia:



***Serwer publiczny***




- Połączenie z publicznymi serwerami (np. blockstream.info, Mempool.space)
- Prosty, ale mniej prywatny



***Bitcoin Core***




- Bezpośrednie połączenie z węzłem Bitcoin
- Prywatny, ale wolniejszy



***Prywatne Electrum***




- Połączenie z serwerem Electrs
- Łączy w sobie poufność i wydajność



*konfiguracja* *wyborców*



Wybierz typ połączenia, korzystając z informacji wyświetlanych w aplikacji Electrs, którą widzieliśmy wcześniej:



W obu przypadkach pozostaw opcje "Użyj SSL" i "Użyj proxy" niezaznaczone.



**Połączenie lokalne**


Host: umbrel.local


Numer portu: 50001



**Połączenie zdalne (Tor)**


Host : [your-Address-onion]


Numer portu: 50001



Połączenie Tor jest niezbędne, jeśli chcesz uzyskać dostęp do węzła poza siecią lokalną.



![Configuration connexion](assets/fr/21.webp)


Aby uzyskać więcej informacji na temat oprogramowania Sparrow Wallet, przygotowaliśmy obszerny samouczek:


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Wnioski



Twój Umbrel jest teraz gotowy do użycia. Aktywnie uczestniczysz w sieci Bitcoin, zachowując pełną kontrolę nad swoimi danymi. Zachęcamy do zapoznania się z wieloma innymi aplikacjami dostępnymi w Umbrel App Store, aby rozszerzyć możliwości swojego domowego serwera.



## Przydatne zasoby



### Oficjalna dokumentacja




- [Oficjalna strona Umbrel](https://umbrel.com)
- [Dokumentacja Umbrel](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Zastosowania Bitcoin




- [Bitcoin Core](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sparrow Wallet](https://sparrowwallet.com)



### Wspólnota




- [Forum Umbrel](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Umbrel](https://twitter.com/umbrel)