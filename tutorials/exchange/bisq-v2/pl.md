---
name: Bisq 2
description: Kompletny przewodnik po korzystaniu z Bisq 2 i wymianie bitcoinów P2P
---
![cover](assets/cover.webp)


## Wprowadzenie


Pozbawione KYC giełdy peer-to-peer (P2P) mają zasadnicze znaczenie dla zachowania poufności i autonomii finansowej użytkowników. Umożliwiają one bezpośrednie transakcje między osobami fizycznymi bez konieczności weryfikacji tożsamości, co ma kluczowe znaczenie dla tych, którzy cenią sobie prywatność. Aby uzyskać bardziej dogłębne zrozumienie koncepcji teoretycznych, zapoznaj się z kursem BTC204:


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Czym jest Bisq 2?


Bisq 2 to nowa wersja popularnego zdecentralizowanego Bisq Exchange, wprowadzonego na rynek w 2024 roku. W przeciwieństwie do swojego poprzednika, Bisq 2 został opracowany w celu obsługi wielu protokołów Exchange, oferując użytkownikom większą elastyczność.


**Najważniejsze nowe funkcje:**




- Obsługa wielu sieci prywatności (Tor, I2P)
- Wiele tożsamości dla większej poufności
- REST API dla botów handlowych
- Obsługa wielu typów Wallet
- System ról z obowiązkowym depozytem w BSQ


Niniejszy przewodnik skupia się wyłącznie na "Bisq Easy", jedynym obecnie dostępnym protokole. Bisq Easy został zaprojektowany specjalnie dla nowych użytkowników Bitcoin. Protokół ten umożliwia użytkownikom kupowanie i sprzedawanie Bitcoinów za waluty fiducjarne na zdecentralizowanej platformie peer-to-peer. Transakcje są ograniczone do równowartości 600 USD (przy minimum 6 USD), a bezpieczeństwo Exchange opiera się na reputacji sprzedawców BTC. Bisq Easy nie ma opłat transakcyjnych ani wymagań dotyczących depozytu zabezpieczającego. Oczekuje się, że Bisq Easy zastąpi Bisq 1 dla wymian gotówkowych poniżej 600 USD (lub równowartości).


**Główne cechy:**




- Wieloplatformowa aplikacja desktopowa
- Dostępnych jest kilka protokołów Exchange
- Zdecentralizowana sieć P2P
- Nacisk na poufność (brak KYC, korzystanie z Tor)
- Non-custodial (zachowujesz kontrolę nad swoimi środkami)
- Open source (AGPL)


### Różnice w stosunku do Bisq 1


**Dla kupujących:**




- Kaucja nie jest wymagana
- Brak opłat transakcyjnych
- Brak opłat za Mining
- Bezpieczeństwo oparte na reputacji dostawcy
- Niższe limity handlowe (równowartość 600 USD)


**Dla sprzedawców:**




- Kaucja nie jest wymagana
- Budowanie reputacji
- Możliwość spalania BSQ lub tworzenia wiązań BSQ
- Potencjalnie wyższa premia za sprzedaż (10-15% powyżej rynku)


**Ważna uwaga:** Po wdrożeniu protokołu Bisq Multisig w Bisq 2, stara wersja Bisq może zostać wycofana. Jednak Bisq 1 będzie nadal używany jako narzędzie do zarządzania Bisq CAD i giełdami BSQ-BTC.


### Proces Exchange




- Twórca oferty określa warunki Exchange
- Gdy inwestorzy uzgodnią warunki (metodę płatności i cenę), rozpoczyna się Exchange
- Sprzedający wysyła swoje dane bankowe do kupującego, a kupujący wysyła swoje Bitcoin Address do sprzedającego
- Kupujący dokonuje płatności gotówką i powiadamia o tym sprzedawcę
- Po otrzymaniu płatności sprzedawca wysyła bitcoiny do Address kupującego
- Transakcja Exchange jest zakończona, gdy kupujący otrzyma bitcoiny


### Ważne zasady




- Przed wymianą szczegółów płatności Exchange może zostać anulowany bez uzasadnienia
- Po wymianie szczegółów, niewypełnienie zobowiązań może skutkować banicją
- W przypadku przelewów bankowych **nigdy nie używaj terminów "Bisq" lub "Bitcoin"** w przyczynie płatności (może to doprowadzić do zamrożenia środków lub nawet zablokowania konta bankowego odbiorcy lub płatnika)
- Inwestorzy muszą logować się co najmniej raz dziennie, aby śledzić proces
- W przypadku problemów, przedsiębiorcy mogą skorzystać z usług mediatora


## Instalacja i konfiguracja


### 1. Pobierz i zweryfikuj Bisq 2


![Téléchargement de Bisq 2](assets/fr/01.webp)




- Przejdź do [bisq.network](https://bisq.network/downloads/)
- Pobierz wersję Bisq 2 odpowiadającą Twojemu systemowi operacyjnemu (przewiń stronę w dół)
- Zweryfikuj autentyczność pobranego pliku (zdecydowanie zalecane). Szczegółowy przewodnik po weryfikacji podpisu znajduje się w poniższym samouczku:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### 2. Instalacja zgodnie z posiadanym systemem


Postępuj zgodnie z krokami instalacji odpowiednimi dla twojego systemu operacyjnego. Jeśli napotkasz jakiekolwiek trudności podczas instalacji, możesz zapoznać się ze szczegółowym przewodnikiem na [oficjalnej wiki Bisq] (https://bisq.wiki/Downloading_and_installing).


### 3. Pierwsze uruchomienie




- Uruchom Bisq 2 i zaakceptuj warunki użytkowania


![Conditions d'utilisation](assets/fr/01.webp)




- Utwórz nowy profil, wybierając nazwę i awatar


![Création du profil](assets/fr/02.webp)




- Następnie zostaniesz przeniesiony do głównego pulpitu aplikacji, gdzie możesz uruchomić Bisq Easy, aby kupić lub sprzedać swoje pierwsze bitcoiny


![Page d'accueil de Bisq 2](assets/fr/03.webp)


### 4. Konfigurowanie metod płatności




- Przejdź do sekcji rachunków płatniczych z menu głównego


![Liste des comptes de paiement](assets/fr/04.webp)




- Dodaj nową metodę płatności, wypełniając wymagane informacje


![Création d'un nouveau compte de paiement](assets/fr/05.webp)


Wstępna konfiguracja metod płatności jest opcjonalna, ale zalecana w celu zaoszczędzenia czasu podczas handlu. Metody płatności można również skonfigurować bezpośrednio podczas transakcji, kontaktując się z partnerem Exchange.


### 5. Bezpieczeństwo konta


**Kopia zapasowa danych:**


W przeciwieństwie do Bisq 1, Bisq 2 nie integruje obecnie Bitcoin Wallet: transakcje są zatem przeprowadzane za pośrednictwem własnych portfeli zewnętrznych. Niemniej jednak zalecamy regularne tworzenie kopii zapasowych folderu danych Bisq 2. Aby zlokalizować folder danych, zapoznaj się z [oficjalną wiki Bisq](https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory).


**Zarządzanie tożsamością:**


Bisq 2 umożliwia tworzenie wielu tożsamości. Każda tożsamość może być używana do różnych typów transakcji. Tożsamości są przechowywane w folderze danych.


## Kupowanie i sprzedawanie bitcoinów


### Jak kupić Bitcoiny


**Opcja 1: Skorzystaj z istniejącej oferty**




- Na ekranie głównym wybierz "Bisq Easy", zakładkę "Pierwsze kroki", a następnie kliknij "Uruchom kreatora transakcji"


![Lancer trade wizard](assets/fr/06.webp)




- Wybierz "Kup Bitcoin" i wybierz walutę


![Sélection achat Bitcoin](assets/fr/07.webp)


![Choix de la devise](assets/fr/08.webp)




- Skonfiguruj preferowane metody płatności (SEPA, Revolut itp.)


![Configuration méthodes de paiement](assets/fr/09.webp)




- W tym momencie albo masz listę ofert odpowiadających poprzednim kryteriom, albo musisz przejść do "Księgi ofert"


![Liste des offres](assets/fr/10.webp)




- W drugim przypadku można wyświetlać i filtrować oferty za pomocą przycisków w prawym górnym rogu Interface


![Filtres des offres](assets/fr/11.webp)




- Po wybraniu oferty wystarczy wybrać metodę płatności, a następnie zatwierdzić podsumowanie transakcji


![Choix modalités de paiement](assets/fr/12.webp)


![Configuration du trade](assets/fr/13.webp)


![Récapitulatif du trade](assets/fr/14.webp)


**Opcja 2: Stwórz własną ofertę**




- Wybierz "Bisq Easy", a następnie "Offerbook"
- Wybierz swoją parę handlową (np. BTC/EUR)
- Kliknij "Utwórz ofertę
- Postępuj zgodnie z kreatorem tworzenia oferty: Zdefiniuj kwotę (stałą lub z zakresu)


![Configuration du montant](assets/fr/20.webp)




- Wybierz akceptowane metody płatności


![Sélection méthodes de paiement](assets/fr/21.webp)




  - Sprawdź podsumowanie i opublikuj ofertę


![Récapitulatif et publication](assets/fr/22.webp)


Po zainicjowaniu Exchange:




- Wyślij swój Bitcoin Address lub Lightning Invoice do sprzedawcy


![Envoi adresse Bitcoin](assets/fr/15.webp)




- Otrzymanie danych bankowych sprzedawcy


![Réception coordonnées bancaires](assets/fr/16.webp)


![Détails coordonnées bancaires](assets/fr/17.webp)




- Dokonaj płatności (bez podawania "Bisq" lub "Bitcoin")
- Powiadomienie sprzedawcy o dokonaniu płatności


![Notification paiement](assets/fr/18.webp)




- Poczekaj na nadejście bitcoinów


![Attente réception](assets/fr/19.webp)


### Jak sprzedawać Bitcoiny?


Proces sprzedaży w Bisq 2 przebiega podobnie do procesu zakupu, z tymi samymi głównymi krokami, ale w odwrotnej kolejności. Możesz utworzyć własną ofertę sprzedaży lub odpowiedzieć na istniejącą ofertę kupna. Oto zestawienie różnych opcji i etapów procesu:


**Opcja 1: Stworzenie oferty sprzedaży**




- Wybierz "Bisq Easy", a następnie "Offerbook"
- Kliknij "Utwórz ofertę" i wybierz "Sprzedaj Bitcoin"
- Skonfiguruj swoją ofertę :
 - Wybierz walutę (EUR, USD itp.)
 - Wybierz akceptowane metody płatności
 - Ustaw kwotę (od 6 do równowartości 600 USD)
 - Ustal cenę (stałą lub jako % rynku)
- Sprawdź szczegóły i opublikuj ofertę


**Opcja 2: Skorzystanie z istniejącej oferty**




- Przeglądaj oferty w zakładce "Księga ofert"
- Filtruj według waluty i metody płatności
- Wybierz ofertę, która Ci odpowiada
- Sprawdź szczegóły i zaakceptuj ofertę


**Proces sprzedaży:**


Po zainicjowaniu Exchange:




   - Wyślij kupującemu swoje dane bankowe
   - Oczekiwanie na kupującego Bitcoin Address
   - Sprawdź, czy Address jest ważny


Po powiadomieniu o płatności:




   - Sprawdź, czy na Twoje konto wpłynęła płatność
   - Potwierdź zgodność kwoty i szczegółów
   - Wysyłaj bitcoiny na podany adres Address
   - Oznacz transakcję jako zakończoną


Finalizacja :




   - Oczekiwanie na potwierdzenie od kupującego
   - Zostaw opinię na temat transakcji
   - Zbuduj swoją reputację dla przyszłej sprzedaży


**Ważna uwaga:** Jako sprzedawca musisz być szczególnie czujny na ryzyko obciążeń zwrotnych. Preferuj bezpieczne metody płatności i zawsze sprawdzaj, czy płatność została otrzymana przed wysłaniem bitcoinów.


## Dobre praktyki i bezpieczeństwo


### Wskazówki dotyczące bezpieczeństwa


**Dla kupujących:**




- Zacznij od małych ilości
- Sprawdź reputację sprzedawców (minimalny wynik 30 000)
- Używaj tylko sugerowanych metod płatności
- Przed wysłaniem płatności sprawdź, czy sprzedawca jest aktywny
- Używaj wyłącznie danych bankowych podanych na czacie Exchange
- Nigdy nie komunikuj się poza platformą Bisq 2
- Zachowaj dowód płatności
- Nigdy nie wysyłaj poufnych informacji


**Dla sprzedawców:**




- Bądź ostrożny z nowymi kontami
- Unikaj metod płatności wrażliwych na obciążenia zwrotne (PayPal, Venmo)
- Sprawdź, czy dane konta odpowiadają kupującemu
- Ograniczenie komunikacji do czatu Bisq 2
- Otwarcie mediacji w przypadku wątpliwości


### Budowanie reputacji (dla sprzedawców)


Aby poprawić swoją reputację na Bisq jako sprzedawcy, przeprowadzaj regularne transakcje i utrzymuj profesjonalną komunikację z kupującymi. Szybko reaguj na prośby kupujących, aby zapewnić pozytywne doświadczenia. Możesz także utworzyć więź BSQ, aby pokazać swoje Commitment na platformie. Działania te zbudują zaufanie i przyciągną więcej kupujących.


### Rozstrzyganie sporów




- Kontakt z kontrahentem za pośrednictwem czatu
- W razie potrzeby otwórz spór
- Dostarczenie wszystkich wymaganych dowodów
- Postępuj zgodnie z instrukcjami mediatora


### Polityka prywatności :




- Nie jest wymagana rejestracja ani scentralizowana weryfikacja tożsamości
- Wszystkie połączenia przechodzą przez sieć Tor (a wkrótce I2P)
- Brak centralnego serwera do przechowywania danych
- Szczegóły transakcji są czytelne tylko dla zaangażowanych stron


### Ochrona przed cenzurą :




- W pełni rozproszona sieć P2P
- Korzystanie z sieci Tor (a wkrótce I2P) w celu przeciwstawienia się cenzurze
- Projekt open source zarządzany przez DAO, bez scentralizowanego podmiotu prawnego


## Zalety i wady


### Zalety Bisq 2




- Maksymalna poufność**: Brak KYC, korzystanie z sieci Tor
- Decentralizacja**: Brak centralnego serwera
- Bezpieczeństwo**: Otwarty kod źródłowy, bez ograniczeń
- Intuicyjny Interface**: prostszy niż Bisq 1
- Elastyczność**: Wiele protokołów Exchange


### Wady Bisq 2




- Ograniczona płynność** (na chwilę obecną):
 - Nowy protokół w fazie rozruchu
 - Dostępnych jest kilka ofert sprzedaży
 - Potencjalnie długi czas oczekiwania na znalezienie nabywcy
- Limity handlowe**: Maksymalnie 600 USD na transakcję (z Bisq easy)
- Tylko komputer stacjonarny**: Brak aplikacji mobilnej


## Przyszłe protokoły


Chociaż Bisq Easy jest obecnie jedynym dostępnym protokołem, kilka innych protokołów jest w trakcie opracowywania dla Bisq 2 :




- Bisq Lightning**: Protokół Exchange oparty na systemie escrow wykorzystującym wielostronną kryptografię obliczeniową na Lightning Network.
- Bisq MuSig**: Migracja głównego protokołu z Bisq 1 do Bisq 2, przy użyciu Multisig 2 na 2 z depozytami zabezpieczającymi.
- Swapy BSQ**: Natychmiastowe swapy atomowe między BSQ i BTC.
- Liquid Swapy**: Exchange aktywów na Liquid Network (USDT, BTC-L) poprzez swapy atomowe.
- Swapy Monero**: Atomowe wymiany między Bitcoin i Monero.
- Liquid MuSig**: Wersja protokołu Multisig wykorzystująca L-BTC dla niższych kosztów i większej poufności.
- Wymiana podwodna**: Wymiany między Bitcoin na Lightning Network i Bitcoin On-Chain.
- Swapy stablecoinów**: Atomowe wymiany między stablecoinami Bitcoin i USD.
- Opcje Multisig**: Utworzenie opcji sprzedaży i kupna P2P z blokadą BTC w transakcji On-Chain Multisig.
- Multisig Open Contracts**: Umożliwia tworzenie niestandardowych kontraktów warunkowych przy użyciu systemu Multisig 2 na 3 z arbitrażem.


Protokoły te są obecnie opracowywane i będą stopniowo integrowane z Bisq 2, oferując użytkownikom większą elastyczność zgodnie z ich specyficznymi potrzebami.


## Przydatne zasoby




- Oficjalna strona internetowa: [bisq.network](https://bisq.network)
- Dokumentacja: [Bisq Wiki](https://bisq.wiki)
- Wsparcie: [Forum Bisq](https://bisq.community)
- Kod źródłowy : [GitHub](https://github.com/bisq-network)