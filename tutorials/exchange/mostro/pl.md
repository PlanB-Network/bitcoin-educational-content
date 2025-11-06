---
name: Mostro
description: Wolna od KYC platforma wymiany Bitcoin P2P za pośrednictwem Lightning i Nostr
---

![cover](assets/cover.webp)



Jak nabywać lub sprzedawać bitcoiny bez narażania swojej suwerenności finansowej? Scentralizowane platformy narzucają inwazyjne procedury KYC ujawniające dane osobowe, z możliwością arbitralnego zamrożenia konta lub nadzoru państwa.



**Mostro P2P** oferuje zdecentralizowaną alternatywę łączącą Lightning Network, protokół Nostr i przechowywanie faktur. Jego główną innowacją jest zautomatyzowany system depozytowy, w którym bitcoiny pozostają pod kontrolą użytkownika przez cały czas trwania wymiany, eliminując ryzyko kradzieży, bankructwa giełdy lub arbitralnej konfiskaty.



## Czym jest Mostro P2P?



Mostro P2P to protokół wymiany Bitcoin typu open source stworzony przez **grunch**, twórcę popularnego bota Telegram **lnp2pbot** uruchomionego w 2021 roku. Podczas gdy lnp2pbot umożliwił już wymianę P2P bez KYC za pośrednictwem Lightning, przedstawiał on poważną lukę w zabezpieczeniach: **Telegram stanowi scentralizowany punkt awarii** podatny na cenzurę ze strony rządów.



Mostro reprezentuje **zdecentralizowaną ewolucję** tej koncepcji: zastępując Telegram protokołem **Nostr** (nieocenzurowaną siecią rozproszonych przekaźników), Mostro eliminuje to ryzyko systemowe. Protokół łączy Lightning Network do natychmiastowych transakcji, Nostr do komunikacji odpornej na cenzurę i **zatrzymywanie faktur** w celu stworzenia prawdziwie nie-ustawowego zautomatyzowanego depozytu.



### Architektura techniczna



Mostro działa w oparciu o trzy komponenty:




- Daemon Mostrod**: koordynuje wymianę między użytkownikami i Lightning Network
- Węzeł Lightning**: tworzy wstrzymane faktury (~24-godzinny depozyt kryptograficzny)
- Klienci Mostro**: interfejsy użytkownika (CLI, Mobile, Web)



Zlecenia są publikowane na Nostr jako zdarzenia publiczne (typ 38383), podczas gdy prywatne transakcje są przesyłane za pośrednictwem szyfrowanych wiadomości typu end-to-end (NIP-59, NIP-44). Każda instancja Mostro definiuje własne opłaty (zazwyczaj od 0,3% do 1%) i limity transakcji (od kilku tysięcy do kilkuset tysięcy sats, w zależności od instancji).



### Decydujące zalety



**Odporny na cenzurę**: Żaden rząd nie może zamknąć Mostro, dopóki gdzieś na świecie istnieją przekaźniki Nostr. W przeciwieństwie do podatnego na ataki lnp2pbot za pośrednictwem Telegrama, Mostro umożliwia wymianę, która jest **odporna na cenzurę**.



**Escrow non-custodial**: Faktury Lightning Hold blokują Twoje bitcoiny bez przenoszenia ich na stałe. Twoje środki pozostają pod Twoją kontrolą i są automatycznie zwracane w przypadku wystąpienia problemu (~24 godziny).



**Poufność w założeniu**: Dostępne są dwa tryby dostosowane do potrzeb użytkownika. Tryb reputacji** łączy twoją reputację z kluczem Nostr, aby budować trwałe zaufanie. Tryb w pełni prywatny** zapewnia całkowitą anonimowość dzięki jednorazowym kluczom efemerycznym.



## Główne cechy



**Zdecentralizowana komunikacja**: Wszystkie zamówienia są publikowane na Nostr za pośrednictwem kryptograficznie podpisanych zdarzeń. Prywatne negocjacje są przesyłane za pomocą zaszyfrowanych wiadomości typu end-to-end, co gwarantuje absolutną poufność.



**System reputacji**: 5-gwiazdkowa ocena z iteracyjnymi obliczeniami na stałe zapisana w Nostr. Pozwala stopniowo budować reputację wiarygodnego tradera.



**Zdecentralizowany arbitraż**: W przypadku sporu bezstronny arbiter bada dowody i podejmuje decyzję w oparciu o przejrzyste kryteria. Każdy spór generuje unikalny token w celu zapewnienia identyfikowalności.



**Elastyczność płatności**: Obsługa wielu walut fiducjarnych za pośrednictwem usługi kursów wymiany yadio.io. Akceptuje przelewy SEPA, PayPal, Revolut, gotówkę i wszelkie metody uzgodnione między stronami.



## Dostępni klienci Mostro



Mostro oferuje dwóch głównych klientów operacyjnych dla giełd P2P.



### Mostro CLI - Klient wiersza poleceń



Mostro CLI** jest najbardziej dojrzałym i funkcjonalnym klientem. Napisany w Rust, oferuje pełen zakres funkcji Mostro za pośrednictwem interfejsu wiersza poleceń. Kompatybilny z systemami macOS, Linux i Windows.



**Główne elementy sterujące** :




- `listorders`: Wyświetla wszystkie dostępne zamówienia
- `neworder` : Utwórz nowe zlecenie kupna lub sprzedaży
- `takesell` / `takebuy`: Przyjmij zlecenie kupna lub sprzedaży
- `fiatsent`: Potwierdź wysłanie płatności fiat
- `release`: Zwolnienie depozytu i sfinalizowanie wymiany
- `getdm`: Wyświetl bezpośrednie wiadomości
- `rate` : Oceń swojego kontrahenta po wymianie



Idealny dla użytkowników technicznych, automatyki i środowisk wymagających maksymalnego bezpieczeństwa.



### Mostro Mobile - aplikacja na smartfony



**Aplikacja mobilna** w wersji alfa umożliwia handel P2P bezpośrednio ze smartfona. Intuicyjny graficzny Interface z nawigacją w zakładkach, przeglądaniem zleceń, zaawansowanymi filtrami i zintegrowanym czatem do komunikacji z kontrahentami.



Dostępny dla **Androida** (za pośrednictwem APK na GitHub), jest optymalnym wyborem dla użytkowników preferujących prostotę i okazjonalny handel mobilny.



### Mostro-web - Interface web (w przygotowaniu)



Interface zaawansowana aplikacja internetowa JavaScript w trakcie aktywnego rozwoju. Zaprojektowana tak, aby oferować pełne doświadczenie użytkownika z rozbudowanymi funkcjami handlowymi i zarządzania portfelem. Dostęp przez przeglądarkę bez konieczności instalacji.



## Instalacja i konfiguracja



Ten samouczek poprowadzi Cię przez instalację i korzystanie z dwóch głównych klientów Mostro: CLI i aplikacji mobilnej.



### Niezbędne warunki wstępne



Zanim zaczniesz, będziesz potrzebować :





- Działający Lightning Network** wallet z wystarczającą płynnością (lub kompatybilny z Lightning)
 - Zalecane: Phoenix, Breez, Wallet of Satoshi...
 - Minimum 1000 satoshis płynności do przetestowania



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Klucz prywatny Nostr** (format `nsec1...`)
 - Utwórz dedykowany klucz handlowy na [nostrkeygen.com](https://nostrkeygen.com/)
 - Ważne**: Nigdy nie używaj głównego klucza osobistego Nostr
 - Przechowuj klucz prywatny w bezpiecznym miejscu (menedżer haseł)





- Opcjonalne, ale zalecane**: Połączenie VPN lub Tor w celu zamaskowania adresu IP



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Instalacja Mostro CLI



#### Na macOS



**Krok 1: Sprawdzenie Rust**



Sprawdź, czy Rust jest zainstalowany (wymagana wersja 1.64+):



```bash
rustc --version
```



Jeśli Rust nie jest zainstalowany:



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Krok 2: Klonowanie repozytorium**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Krok 3: Konfiguracja**



Skopiuj i edytuj plik :



```bash
cp .env-sample .env
```



Otwórz `.env` i skonfiguruj ustawienia:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Ważne dla synchronizacji CLI/Mobile**: Aby uzyskać dostęp do tych samych zleceń na CLI i w aplikacji mobilnej, należy użyć **tego samego klucza publicznego Mostro** i **tych samych przekaźników Nostr** w obu klientach. Sprawdź te ustawienia w Ustawieniach w aplikacji mobilnej.



![Configuration .env](assets/fr/02.webp)



**Krok 4: Instalacja**



Skompiluj i zainstaluj CLI :



```bash
cargo install --path .
```



Kompilacja zajmuje 1-2 minuty. Plik wykonywalny `mostro-cli` zostanie zainstalowany w `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Krok 5: Sprawdź**



Sprawdź, czy wszystko działa:



```bash
mostro-cli --help
```



Powinieneś zobaczyć pełną listę zamówień.



![Vérification avec --help](assets/fr/04.webp)



#### W systemie Linux (Ubuntu/Debian)



Instalacja identyczna jak w macOS, z dodatkiem :



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Następnie wykonaj kroki 3 i 4 w sekcji macOS.



#### W systemie Windows



Najpierw zainstaluj Rust przez [rustup.rs](https://rustup.rs/), a następnie użyj PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Identyczna konfiguracja: skopiuj `.env-sample` do `.env` i wprowadź swoje parametry.



### Instalacja Mostro Mobile



#### Na Androida



**Krok 1**: Wejdź na stronę [GitHub releases page](https://github.com/MostroP2P/mobile/releases) i pobierz plik **app-release.apk** (ok. 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**Krok 2: Po pobraniu otwórz plik APK z pobranych plików. Android poprosi o autoryzację instalacji z tego źródła.



![Téléchargement et installation APK](assets/fr/11.webp)



**Krok 3**: Postępuj zgodnie z ekranami onboardingu, które przedstawiają funkcjonalności:




- Swobodny handel Bitcoin - bez KYC** : Handel bez weryfikacji tożsamości dzięki Nostr
- Prywatność domyślnie**: Wybierz między trybem reputacji a trybem pełnej prywatności
- Bezpieczeństwo na każdym kroku**: Ochrona za pomocą faktur bez blokady



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Krok 4**: Kontynuuj wdrażanie, aby odkryć :




- W pełni szyfrowany czat**: Szyfrowana komunikacja typu end-to-end
- Wybierz ofertę**: Przejrzyj książkę zamówień i wybierz ofertę
- Nie możesz znaleźć tego, czego potrzebujesz **: Stwórz własne, spersonalizowane zamówienie



![Suite onboarding](assets/fr/13.webp)



**Krok 5: Po zakończeniu wdrażania aplikacja automatycznie wygeneruje parę kluczy Nostr. Przejdź do menu (☰), a następnie **Konto**, aby zapisać **Secret Words** (frazę odzyskiwania). Na tym ekranie masz również możliwość zmiany wspomnianego wcześniej trybu prywatności.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Ważne**: Zapisz swoją frazę odzyskiwania w bezpiecznym miejscu (menedżer haseł, sejf papierowy).



### Początkowa konfiguracja zabezpieczeń



Niezależnie od używanej platformy:





- Klucz dedykowany**: Używaj oddzielnej tożsamości Nostr do handlu
- Małe kwoty**: Zacznij od mniej niż 10 000 sats, aby rozpocząć
- Wiele przekaźników**: Konfiguracja 3-5 geograficznie zróżnicowanych przekaźników
- Ochrona sieci**: Aktywuj VPN lub Tor, aby ukryć swój adres IP
- Wallet secure**: Aktywacja automatycznego blokowania wallet Lightning



## Używaj z CLI



Ta sekcja demonstruje zakup bitcoinów za pośrednictwem Mostro CLI na podstawie rzeczywistego przypadku użycia.



### Krok 1: Lista dostępnych zamówień



Komenda `listorders` wyświetla wszystkie aktywne zlecenia:



```bash
mostro-cli listorders
```



Zobaczysz tabelę ze szczegółami każdego zamówienia: ID, typ (kupno/sprzedaż), kwota, waluta, metoda płatności.



![Liste des ordres disponibles](assets/fr/05.webp)



W tym przykładzie widoczne jest zlecenie sprzedaży 5 EUR za pośrednictwem Revolut (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Krok 2: Przyjęcie zamówienia



Aby kupić te bitcoiny, należy przyjąć zamówienie z `takesell` :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro poprosi Cię o dostarczenie **faktury Lightning**, aby otrzymać BTC. Podana jest dokładna kwota w satoshis (tutaj: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Krok 3: Dostarczenie faktury Lightning



Wygeneruj fakturę Lightning z wallet (Phoenix, Breez itp.) na dokładną kwotę, a następnie wyślij ją :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



System potwierdza wysyłkę i informuje, że przed aktywacją escrow należy poczekać, aż sprzedawca opłaci fakturę wstrzymującą.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Krok 4: Kontakt ze sprzedawcą



Po aktywacji escrow, użyj `dmtouser`, aby zażądać szczegółów płatności od sprzedawcy:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Krok 5: Uzyskanie odpowiedzi



Sprawdź bezpośrednie wiadomości, aby zobaczyć odpowiedź sprzedawcy:



```bash
mostro-cli getdm
```



Sprzedawca podaje swój identyfikator płatności (tutaj jego Revtag: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Krok 6: Dokonanie płatności fiat



Wyślij płatność za pomocą uzgodnionej metody (w tym przykładzie Revolut) na podane dane kontaktowe. **Zachowaj wszystkie dokumenty potwierdzające** (zrzuty ekranu, referencje transakcji).



### Krok 7: Potwierdzenie wysyłki płatności



Po dokonaniu płatności powiadom Mostro :



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Krok 8: Otrzymanie bitcoinów



Gdy tylko sprzedawca potwierdzi otrzymanie fiat i zwolni depozyt za pomocą polecenia `release`, natychmiast otrzymasz swoje bitcoiny na podanej fakturze Lightning.



### Krok 9: Ocena



Oceń sprzedawcę, aby przyczynić się do zdecentralizowanej reputacji:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Przydatne polecenia



**Anulowanie zamówienia** (przed jego przyjęciem):


```bash
mostro-cli cancel -o <order-id>
```



**Utwórz nowe zlecenie sprzedaży** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Otwórz spór** :


```bash
mostro-cli dispute -o <order-id>
```



## Korzystanie z aplikacji mobilnej



W tej sekcji zademonstrowano sprzedaż bitcoinów za pośrednictwem Mostro Mobile na podstawie rzeczywistego przypadku użycia.



### Interface główny



Aplikacja posiada 3 główne zakładki:





- Księga zamówień**: Przeglądaj dostępne zlecenia kupna (BUY BTC) i sprzedaży (SELL BTC)
- Moje transakcje**: Wyświetlanie aktywnych i historycznych zleceń
- Czat**: Komunikuj się ze swoimi kontrahentami za pomocą liczb



![Interface principale](assets/fr/14.webp)



### Zalecana konfiguracja



Przed rozpoczęciem handlu należy skonfigurować kilka ustawień w menu (☰) > **Ustawienia** :





- Lightning Address** (opcjonalnie): Aby otrzymywać płatności bezpośrednio
- Przekaźniki**: Dodanie kilku przekaźników Nostr dla odporności (np. `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Sprawdź klucz publiczny używanej instancji Mostro



![Paramètres de l'application](assets/fr/16.webp)



**Ważne dla synchronizacji CLI/Mobile**: Jeśli korzystasz zarówno z CLI, jak i aplikacji mobilnej, skonfiguruj **dokładnie te same przekaźniki Nostr i Mostro Pubkey** w obu klientach. Bez tej identycznej konfiguracji nie zobaczysz tych samych zleceń dostępnych na obu interfejsach. Przekaźniki i Mostro Pubkey widoczne w Ustawieniach (zrzut ekranu powyżej) muszą być zgodne z tymi w pliku `.env' CLI.



### Krok 1: Utwórz zlecenie sprzedaży



Naciśnij zielony przycisk **"+"** w prawym dolnym rogu, a następnie wybierz **Sprzedaż** (czerwony przycisk).



![Boutons de création d'ordre](assets/fr/17.webp)



Wypełnij formularz tworzenia:



1. **Waluta**: Wybierz walutę, którą chcesz otrzymać (EUR, USD itp.)


2. **Kwota** : Wprowadź kwotę w fiat (np. od 1 do 3 EUR)


3. **Metody płatności** : Wybierz metodę (np. "Revolut")


4. **Typ ceny**: Wybierz "Cena rynkowa"


5. **Premia**: Dostosuj premię (suwak od -10% do +10%, zalecane: 0% do szybkiej sprzedaży)



Naciśnij **Prześlij**, aby opublikować zamówienie.



### Krok 2: Potwierdzenie publikacji



Twoje zamówienie zostało opublikowane! Będzie ono dostępne przez 24 godziny. Możesz je anulować w dowolnym momencie, zanim kupujący je odbierze, wykonując polecenie `cancel`.



![Ordre publié](assets/fr/18.webp)



Zlecenie pojawi się w zakładce **Moje transakcje** ze statusem "Oczekujące" i plakietką "Utworzone przez Ciebie".



### Krok 3: Kupujący przyjmuje zamówienie



Gdy kupujący przyjmie Twoje zamówienie, otrzymasz powiadomienie. Zobacz szczegóły w **Moje transakcje**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Ważna instrukcja**: Musisz teraz **opłacić wyświetloną fakturę hold**, aby zablokować swoje bitcoiny (tutaj 4674 sats za 1-5 EUR) w depozycie. Masz **maksymalnie 15 minut**, w przeciwnym razie wymiana zostanie anulowana.



Skopiuj fakturę za wstrzymanie i opłać ją za pomocą wallet Lightning (Phoenix, Breez itp.).



### Krok 4: Komunikacja z kupującym



Po aktywacji escrow, naciśnij **CONTACT**, aby otworzyć szyfrowany czat z kupującym.



Kupujący (tutaj "anonymous-gloriaZhao") skontaktuje się z Tobą, aby poprosić o szczegóły płatności. Prosimy o odpowiedź z podaniem danych (Revtag, IBAN itp.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Krok 5: Otrzymanie płatności fiat



Poczekaj, aż otrzymasz płatność fiat na swoje konto Revolut (lub inną uzgodnioną metodą). **Sprawdź dokładnie**:




- Dokładna kwota
- Nadawca
- Referencje, jeśli są wymagane



Kupujący poinformuje Cię za pośrednictwem czatu, że wysłał płatność. Mostro wyświetli również wiadomość potwierdzającą, że fiat został wysłany.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Krok 6: Zwolnienie depozytu



Po **potwierdzeniu otrzymania** płatności fiat na swoim koncie, naciśnij zielony przycisk **RELEASE** i potwierdź, aby wysłać satss do kupującego.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoiny są natychmiast przekazywane kupującemu za pośrednictwem faktury Lightning.



### Krok 7: Ocena rozważań



Po wydaniu naciśnij **RATE**, aby ocenić kupującego. Wybierz od 1 do 5 gwiazdek (tutaj 5/5) i naciśnij **Prześlij ocenę**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Wymiana została zakończona!



### Kup bitcoiny za pomocą aplikacji mobilnej



Proces **kupowania** bitcoinów jest podobny, ale odwrócony:



1. Przejrzyj zakładkę **Księga zleceń** > **KUP BTC**, aby wyświetlić zlecenia sprzedaży


2. Kliknij interesujące zamówienie, aby wyświetlić szczegóły


3. Naciśnij **Przyjmij zamówienie**


4. Dostarczyć fakturę Lightning (wygenerowaną z wallet)


5. Oczekiwanie na aktywację escrow przez sprzedającego


6. Skontaktuj się ze sprzedawcą przez **KONTAKT**, aby uzyskać szczegóły płatności


7. Wyślij płatność fiat (zachowaj dowód)


8. Sprzedawca zwalnia depozyt po weryfikacji


9. Natychmiastowe otrzymywanie bitcoinów na fakturze Lightning


10. Oceń sprzedawcę (1-5 gwiazdek)



### Zarządzanie problemami



**Anulowanie zlecenia**: W **My Trades** naciśnij swoje zlecenie, a następnie przycisk **CANCEL** (dostępny tylko przed jego przyjęciem).



**Otwórz spór**: Jeśli dojdzie do sporu, naciśnij **DISPUTE** w szczegółach zamówienia. Dołącz wszystkie dowody (zrzuty ekranu czatu, referencje transakcji bankowych).



## Zalety i ograniczenia



### Korzyści



**Suwerenność finansowa**: Twoje bitcoiny nigdy nie opuszczają Twojej bezpośredniej kontroli dzięki mechanizmowi hold invoice, eliminując ryzyko bankructwa giełdy lub piractwa.



**Odporny na cenzurę**: Żaden organ nie może wyłączyć sieci ani cenzurować poleceń użytkownika. System działa tak długo, jak długo działają przekaźniki Nostr.



**Domyślna anonimowość**: Tylko pseudonimowy klucz Nostr identyfikuje użytkownika, bez KYC lub danych osobowych. Kompleksowe szyfrowanie komunikacji.



**Elastyczność płatności**: Możliwe są wszelkie wzajemnie akceptowane metody płatności (przelewy, aplikacje mobilne, gotówka, barter).



### Ograniczenia



**Wczesny rozwój**: Wymagane podstawowe interfejsy i techniczna krzywa uczenia się.



**Ograniczona płynność**: Ograniczona liczba zleceń, szczególnie w przypadku dużych kwot lub rzadkich walut.



**Wymagania techniczne**: Wymagana podstawowa znajomość Lightning i Nostr.



**Indywidualna odpowiedzialność**: Brak scentralizowanego wsparcia w przypadku problemów, wymagana ostrożność.



## Wnioski



Mostro P2P stanowi obiecującą alternatywę dla scentralizowanych giełd, łącząc Lightning Network, Nostr i automatyczny escrow dla prawdziwie zdecentralizowanego handlu. Pomimo wczesnego rozwoju i ograniczonej płynności, platforma już teraz oferuje suwerenność finansową, odporność na cenzurę i domyślną anonimowość.



Dla bitcoinerów, którzy preferują autonomię i poufność, Mostro jest realną opcją wartą stopniowej eksploracji. Jego zdecentralizowana architektura gwarantuje raczej ewolucję społecznościową niż komercyjną, torując drogę do przyszłości prawdziwie wolnych giełd Bitcoin.



## Zasoby



### Oficjalna dokumentacja




- [Oficjalna strona Mostro](https://mostro.network)
- [Dokumentacja techniczna](https://mostro.network/docs-english/index.html)
- [Fundacja Mostro](https://mostro.foundation)



### Kod źródłowy i rozwój




- [Główne repozytorium GitHub](https://github.com/MostroP2P/mostro)
- [Klient internetowy](https://github.com/MostroP2P/mostro-web)
- [Klient CLI](https://github.com/MostroP2P/mostro-cli)



### Wspólnota




- [Protokół Nostr](https://nostr.com)
- [Lightning Network Guides](https://lightning.network)