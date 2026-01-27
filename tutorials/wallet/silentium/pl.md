---
name: Silentium
description: Progresywny wallet z obsługą cichych płatności (BIP-352)
---

![cover](assets/cover.webp)



Ponowne wykorzystanie adresów Bitcoin jest jednym z najbardziej bezpośrednich zagrożeń dla poufności użytkownika. Gdy odbiorca udostępnia jeden adres w celu otrzymania wielu płatności, każdy obserwator może prześledzić wszystkie powiązane transakcje i odtworzyć ich historię finansową. Problem ten dotyczy w szczególności twórców treści, organizacji charytatywnych lub aktywistów, którzy chcą publicznie wyświetlać adres darowizny bez narażania swojej prywatności.



Silentium odpowiada na ten problem eleganckim rozwiązaniem dostępnym bezpośrednio z przeglądarki. Ta progresywna aplikacja internetowa (PWA) o otwartym kodzie źródłowym, uruchomiona w maju 2024 r. przez Louisa Singera, implementuje Silent Payments (BIP-352): statyczny adres wielokrotnego użytku, w którym każda płatność kończy się na osobnym adresie blockchain, bez wcześniejszej interakcji lub obserwowalnego powiązania między transakcjami.



**Ważne ostrzeżenie**: Silentium to eksperymentalny projekt służący jako *proof-of-concept* dla lekkich portfeli Silent Payments. Nie powinien być używany jako codzienny wallet lub do przechowywania znacznych kwot. Deweloperzy wyraźnie stwierdzają:



> Używaj na własne ryzyko.

Należy pamiętać, że wallet może być używany jako testnet lub regtest.



## Czym jest Silentium?



### Filozofia i cele



Silentium służy jako techniczna demonstracja implementacji Silent Payments w lekkiej przeglądarce wallet. Chociaż obsługuje również konwencjonalne adresy Bitcoin, nacisk kładziony jest na Silent Payments, aby umożliwić użytkownikom eksperymentowanie z tą technologią prywatności w prosty sposób.



### Jak działają ciche płatności?



Ciche płatności (BIP-352) używają klucza eliptycznej krzywej Diffie-Hellmana Exchange (ECDH). Odbiorca generuje statyczny adres (`sp1...` w mainnet, `tsp1...` w testnet) składający się z dwóch kluczy publicznych: klucza skanowania do wykrywania płatności i klucza wydawania do ich używania.



Nadawca łączy swoje prywatne klucze wejściowe z kluczem skanowania odbiorcy, aby obliczyć wspólny sekret generujący kryptograficzną "poprawkę". Ta poprawka, dodana do klucza wydawania, tworzy unikalny adres Taproot dla każdej transakcji. Odbiorca odtwarza te obliczenia za pomocą swojego prywatnego klucza skanowania, aby wykryć i wydać środki bez wcześniejszej interakcji.



Zalety: zwiększona poufność dla nadawcy i odbiorcy, nie jest wymagany serwer strony trzeciej, transakcje nie do odróżnienia od konwencjonalnych płatności Taproot. Główna wada: intensywne skanowanie łańcucha bloków w celu wykrycia płatności.



Aby dowiedzieć się więcej o teoretycznym działaniu Silent Payments, zobacz ostatnią część kursu BTC,204 na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Obsługiwane platformy



Silentium to progresywna aplikacja internetowa (PWA) dostępna z dowolnej nowoczesnej przeglądarki (mobilnej lub stacjonarnej). Można jej używać bezpośrednio na stronie `app.silentium.dev`, zainstalować jako natywną aplikację za pośrednictwem przeglądarki lub wdrożyć lokalnie. Instalacja odbywa się bezpośrednio z przeglądarki, bez konieczności przechodzenia przez oficjalne sklepy.



## Korzystanie z aplikacji internetowej



### Dostęp i instalacja



[Przejdź do strony `https://app.silentium.dev/` w przeglądarce](https://app.silentium.dev/). Aplikacja załaduje się natychmiast i wyświetli ekran główny.



Aby zainstalować ją jako aplikację natywną w systemie iOS, należy nacisnąć przycisk udostępniania (kwadrat ze strzałką w górę), a następnie wybrać opcję "Na ekranie głównym". W systemie Android przeglądarka zazwyczaj oferuje bezpośrednio powiadomienie "Dodaj do ekranu głównego". Po zainstalowaniu Silentium pojawia się z dedykowaną ikoną i działa jako aplikacja natywna, ale wymaga połączenia z Internetem w celu synchronizacji transakcji.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Tworzenie portfolio



Przy pierwszym uruchomieniu wybierz "Utwórz Wallet", aby utworzyć nowy portfel generate, lub "Przywróć Wallet", aby przywrócić z istniejącej frazy odzyskiwania.



Wybierz "Utwórz Wallet". Aplikacja wygeneruje 12-wyrazową frazę, którą należy dokładnie zapisać. Ta fraza jest jedynym sposobem na odzyskanie środków. Nawet w sieci testowej należy stosować dobre praktyki tworzenia kopii zapasowych. Naciśnij "Kontynuuj" po zapisaniu frazy.



Następnie aplikacja poprosi o ustawienie hasła w celu zabezpieczenia dostępu do wallet. Wybierz silne hasło i potwierdź je.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Po potwierdzeniu frazy i ustawieniu hasła zostaniesz przeniesiony do głównego interfejsu.



### Interface główne i parametry



Główny interfejs wyświetla saldo w satoshis (początkowo 0 sats), z trzema przyciskami na dole:




- Sync**: synchronizuje wallet z blockchainem
- Receive**: otrzymywać fundusze
- Wyślij**: aby wysłać bitcoiny



Dostęp do Ustawień można uzyskać za pomocą ikony w prawym górnym rogu (trzy poziome paski). Menu Ustawienia oferuje kilka opcji:





- Informacje**: informacje o aplikacji
- Kopia zapasowa**: kopia zapasowa frazy odzyskiwania
- Explorer**: wybierz eksplorator blockchain (domyślnie Mempool) i serwer Silentiumd
- Sieć**: wybór sieci (mainnet/testnet)
- Hasło**: zmiana hasła
- Przeładowanie**: przeładowanie wallet
- Reset**: całkowity reset
- Motyw**: zmiana motywu



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Sekcja **Explorer** jest szczególnie ważna: pozwala wybrać używany eksplorator blockchain (domyślnie Mempool), a także wyświetla adres URL serwera Silentiumd (`https://bitcoin.silentium.dev/v1` dla mainnet). Jeśli hostujesz własny serwer Silentiumd lub chcesz korzystać z sieci testnet, tutaj konfigurujesz te parametry.



### Otrzymywanie środków



W głównym interfejsie naciśnij przycisk "Odbierz". Domyślnie Silentium wyświetla adres Silent Payment z kodem QR. Adres zaczyna się od `sp1...` na mainnet lub `tsp1...` na testnet.



Możesz przełączać się między cichą płatnością a klasycznym adresem Bitcoin za pomocą przycisku "Przełącz na klasyczny adres" / "Przełącz na cichy adres" u dołu ekranu.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Po nadaniu transakcji należy odczekać kilka minut. W przypadku Silent Payments, Silentium automatycznie skanuje blockchain w poszukiwaniu transakcji przeznaczonych dla Ciebie. Transakcje pojawiają się ze statusem "Niepotwierdzone", a następnie są stopniowo potwierdzane.



### Wyślij płatność



W interfejsie głównym naciśnij przycisk "Wyślij". Zostanie wyświetlony ekran wysyłania:



1. **Address**: wklej adres cichej płatności (`sp1...` lub `tsp1...`) lub klasyczny adres Bitcoin. Do zeskanowania adresu można użyć ikony skanowania QR.


2. **Amount**: wprowadź kwotę w satoshis, która ma zostać wysłana. W celu ułatwienia wprowadzania wyświetlana jest klawiatura numeryczna. Dostępne saldo jest wyświetlane w górnej części ekranu.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Po wprowadzeniu adresu i kwoty naciśnij "Kontynuuj", aby kontynuować. Aplikacja poprosi o wybranie żądanego poziomu opłaty przed potwierdzeniem transakcji.



## wallet self-hosting



### Dlaczego self-host?



Lokalny hosting Silentium oferuje całkowitą suwerenność, weryfikację kodu, środowisko programistyczne i odporność na awarie oficjalnej strony.



### Wymagania wstępne



Node.js (wersja 14+), npm lub yarn, Git i około 500 MB miejsca na dysku.



### Instalacja lokalna



Sklonuj repozytorium i zainstaluj plik :



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Uruchomienie i użytkowanie



Uruchom aplikację w trybie programowania:



```bash
yarn start
```



Przejdź do `http://localhost:3000` w przeglądarce. Zoptymalizowana wersja produkcyjna:



```bash
yarn build
```



Pliki wygenerowane w `build/` mogą być obsługiwane przez nginx, Apache lub dowolny serwer WWW. Domyślnie Silentium łączy się z publicznym serwerem `bitcoin.silentium.dev`. Zmodyfikuj to ustawienie w parametrach, aby używać testnet lub własnego serwera.



## Serwer Silentiumd



### Rola i działanie



Silentium używa serwera indeksującego **Silentiumd**, aby zoptymalizować wykrywanie płatności. Skanowanie wszystkich transakcji Taproot byłoby zbyt uciążliwe dla przeglądarki lub telefonu komórkowego.



Silentiumd wstępnie oblicza dane pośrednie (tweaki) dla każdej transakcji Taproot. wallet pobiera te poprawki (kilka bajtów na transakcję) i wykonuje ostateczne obliczenia lokalnie, weryfikując własność płatności. Serwer nigdy nie zna twoich kluczy ani nie może zidentyfikować twoich transakcji, w przeciwieństwie do konwencjonalnych serwerów Electrum.



Kompaktowe filtry BIP158 pozwalają wallet określić, które bloki skanować bez ujawniania adresów, zachowując w ten sposób poufność.



### Serwer publiczny



Publiczny serwer `bitcoin.silentium.dev` (mainnet), sponsorowany przez Vulpem Ventures, oferuje proste i natychmiastowe doświadczenie. Chociaż poufność jest zachowana, podejście to zakłada względne zaufanie do infrastruktury stron trzecich.



### Hostowanie własnego serwera Silentiumd



Aby uzyskać całkowitą suwerenność, hostuj własny serwer Silentiumd. Wymagania wstępne: Bitcoin Core non-elagged node z `txindex=1` i `blockfilterindex=1`, Go 1.21+, 10-20 GB miejsca na dysku, umiejętności administracji systemem.



**Instalacja:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Konfiguracja za pomocą zmiennych środowiskowych (szczegóły w pliku `config.md` repozytorium). Serwer indeksuje blockchain i udostępnia API, który może być odpytywany przez wallet.



Obecnie nie istnieją żadne pakietowe rozwiązania dla Umbrel lub Start9, co ogranicza dostępność dla użytkowników nietechnicznych.



## Zalety i ograniczenia



### Najważniejsze wydarzenia





- Maksymalna dostępność**: korzystanie z dowolnej przeglądarki, bez konieczności instalacji
- Wieloplatformowość**: działa na urządzeniach mobilnych (Android/iOS) i komputerach stacjonarnych dzięki technologii PWA
- Prosty hosting**: lokalna instalacja możliwa za pomocą kilku poleceń
- Open-source**: w pełni audytowalny kod w serwisie GitHub
- Koncentracja na prywatności**: brak śledzenia, brak analiz, lokalne obliczenia kryptograficzne
- Oddzielna architektura**: wyraźne oddzielenie wallet (klienta) od serwera indeksującego
- Bez konta**: nie wymaga rejestracji ani podawania danych osobowych



### Ograniczenia do rozważenia





- Projekt eksperymentalny**: tylko dowód słuszności koncepcji, nieprzeznaczony do codziennego użytku lub produkcji
- Brak gwarancji**: ryzyko błędów, luk w zabezpieczeniach, możliwa utrata środków
- Ograniczone wsparcie**: niewielka dokumentacja użytkownika, mała społeczność, brak oficjalnego wsparcia
- Zależność od serwera**: wymaga działającego serwera Silentiumd (publicznego lub hostowanego samodzielnie)
- Intensywne skanowanie**: Ciche wykrywanie płatności zużywa przepustowość
- Ograniczona funkcjonalność**: brak kontroli monet, brak Lightning, brak wielu podpisów



## Najlepsze praktyki



### Bezpieczeństwo seed



Nawet w sieci testowej traktuj swoją frazę odzyskiwania poważnie. Zapisz ją i przechowuj w bezpiecznym miejscu. Zachowaj oddzielne portfele dla sieci testowej i mainnet: nigdy nie używaj testowego seed na wallet przeznaczonym dla prawdziwych środków.



### Weryfikacja kodu źródłowego



Jedną z zalet samodzielnego hostingu jest możliwość sprawdzenia kodu źródłowego przed jego uruchomieniem. Jeśli planujesz używać Silentium z prawdziwymi środkami, poświęć trochę czasu na audyt kodu lub poproś o to zaufanego programistę. Porównaj również hash kodu wdrożonego na `app.silentium.dev` z tym z repozytorium GitHub, aby zapewnić autentyczność.



### Kopia zapasowa i przywracanie



Odzyskiwanie funduszy Silent Payments wymaga wallet kompatybilnego z protokołem BIP-352. Standardowy wallet nie może skanować łańcucha bloków w celu odzyskania UTXO Silent Payments. Zachowaj zainstalowane Silentium lub upewnij się, że masz dostęp do innego kompatybilnego wallet (takiego jak Cake Wallet lub inne przyszłe implementacje), aby w razie potrzeby przywrócić swoje środki.



## Wnioski



Silentium stanowi przystępny poligon doświadczalny dla zrozumienia Silent Payments bez przeszkód technicznych. Jako dowód słuszności koncepcji, pokazuje, w jaki sposób ta technologia prywatności może zostać zintegrowana z przeglądarką wallet przy jednoczesnym zachowaniu samokontroli. Eksperymentuj na testnet, aby odkryć ten obiecujący przełom w prywatności on-chain.



## Zasoby



### Oficjalna dokumentacja




- Repozytorium Silentium GitHub (wallet): https://github.com/louisinger/silentium
- Repozytorium Silentiumd GitHub (serwer): https://github.com/louisinger/silentiumd
- Aplikacja internetowa: https://app.silentium.dev/
- Strona społeczności Silent Payments: https://silentpayments.xyz
- Specyfikacja BIP-352: https://bips.dev/352



### Artykuły i zasoby




- Oficjalne ogłoszenie (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Ciche płatności: https://bitcoinops.org/en/topics/silent-payments/



### Narzędzia Testnet




- Bateria Testnet: https://testnet-faucet.com/
- Mempool testnet explorer: https://mempool.space/testnet