---
name: Ciasto Wallet
description: Samouczek na temat Cake Wallet i cichych płatności
---

![cover](assets/cover.webp)


Niniejszy przewodnik omawia [**Cake Wallet**](https://cakewallet.com/): open-source'ową, nieobciążającą, skoncentrowaną na prywatności wielowalutową wallet dostępną dla systemów Android, iOS, macOS, Linux i Windows. Zagłębimy się w jego funkcje prywatności specyficzne dla Bitcoin, przejdziemy przez wysyłanie/odbieranie Bitcoin za pośrednictwem **Silent Payments** (ulepszony protokół prywatności on-chain) i przyjrzymy się implementacji PayJoin v2 dla transakcji asynchronicznych.


## kluczowe cechy



- [**Silent Payments (BIP-352)**](https://bips.dev/352/) ulepsza poprzedni [BIP 47 kodów płatności](https://silentpayments.xyz/docs/comparing-proposals/bip47/) zwany również "PayNyms" z adresami wielokrotnego użytku. Gdy nadawca używa adresu cichej płatności, jego wallet uzyskuje unikalny jednorazowy adres przy użyciu różnych kluczy, które zostaną połączone w unikalny jednorazowy adres Taproot. Zapisy blockchain pokazują niepowiązane transakcje, zapobiegając powiązaniu płatności przychodzących. Silent Payments oferuje szereg korzyści, w tym:
    - Adresy wielokrotnego użytku: Nie ma potrzeby generate nowego adresu dla każdej transakcji, co zapewnia lepsze wrażenia użytkownika i większą prywatność
    - Zerowy wzrost kosztów: Ciche płatności nie zwiększają rozmiaru ani kosztów transakcji.
    - Zwiększona anonimowość: Zewnętrzni obserwatorzy nie mogą powiązać transakcji z adresem Silent Payment.
    - Nie jest wymagana interakcja między nadawcą a odbiorcą: Transakcje mogą być dokonywane bez jakiejkolwiek komunikacji między stronami.
    - Unikalne adresy dla każdej płatności: Eliminacja ryzyka przypadkowego ponownego użycia adresu.
    - Serwer nie jest wymagany: Ciche płatności mogą być realizowane bez konieczności posiadania dedykowanego serwera.
- PayJoin v2** łagodzi analizę wykresu transakcji poprzez łączenie danych wejściowych nadawców i odbiorców w jedną transakcję. Cake Wallet wprowadza dwa krytyczne ulepszenia:
    - Transakcje asynchroniczne**: Nadawca i odbiorca nie muszą już być jednocześnie online, aby ukończyć prywatną transakcję.
    - Komunikacja bezserwerowa**: Żadna ze stron nie musi uruchamiać serwera Payjoin, usuwając główną barierę techniczną.
- Coin Control** umożliwia ręczny wybór UTXO podczas transakcji. Zapobiega to przypadkowemu powiązaniu adresów podczas wydawania wielu UTXO o różnym pochodzeniu.
- Obsługa TOR**, umożliwiająca użytkownikom kierowanie ruchu sieciowego przez sieć Tor
- RBF** (Replace-By.Fee) umożliwia dostosowanie opłaty po wysłaniu transakcji.


## 1️⃣ Konfiguracja Wallet


Cake Wallet oferuje szeroki zakres obsługi platform. Do wyboru są systemy `Android`, `iOS / macOS`, `Linux` i `Windows`.  Aby rozpocząć, odwiedź stronę https://docs.cakewallet.com/get-started/ i wybierz swój system operacyjny.


![image](assets/en/01.webp)


Po instalacji należy ustawić `PIN` (4 lub 6 cyfr). Następnie zobaczysz:


1. `Utwórz nowy Wallet` (dla nowych użytkowników)

2. `Przywróć Wallet` (dla istniejących portfeli)


![image](assets/en/02.webp)


Na następnym ekranie możesz wybierać spośród szerokiej gamy kryptowalut. Wybierz `Bitcoin` i dotknij `Next` i podaj `Nazwę Wallet`, aby zidentyfikować wallet. Po dotknięciu `Ustawień zaawansowanych` pojawi się szereg `Ustawień prywatności`. Wprowadź te zmiany:



- Fiat API:** wybierz `Tor Only` (przekierowuje zapytania o cenę przez Tor)
- Swap:** wybierz `Tor Only` (anonimizuje ruch na giełdzie)


Domyślnie generowany jest typ BIP-39 seed, z opcją zmiany na Electrum seed. Ścieżki pochodne są następujące:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Jeśli chcesz dodać dodatkową warstwę bezpieczeństwa, możesz skonfigurować `passphrase`.  Głównym celem passphrase jest zapewnienie dodatkowej ochrony przed atakami fizycznymi. Nawet jeśli atakujący znajdzie frazę seed, nie może uzyskać dostępu do wallet bez prawidłowego passphrase. Innymi słowy, sama fraza seed reprezentuje jeden wallet, podczas gdy fraza seed plus passphrase tworzy zupełnie inny wallet bez połączenia z oryginałem. Ta funkcja umożliwia również "tajne portfele" chronione przez passphrase i zapewnia wiarygodne zaprzeczenie. W sytuacji przymusu można ujawnić frazę seed, jednocześnie przechowując większe aktywa w wallet chronionym przez passphrase.


Jeśli masz już uruchomiony własny węzeł, przełącz `Add New Custom Node` i podaj swój `Node Address` do walidacji transakcji i bloków w ramach własnej infrastruktury. Po zakończeniu dotknij `Continue` i `Next`, aby utworzyć wallet.


![image](assets/en/03.webp)


Na następnym ekranie pojawi się zrzeczenie się odpowiedzialności:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Aby poznać najlepsze praktyki dotyczące zapisywania frazy mnemonicznej, zapoznaj się z tym samouczkiem:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Stuknij `Rozumiem. Pokaż mi mój seed` i zapisz te słowa w bezpiecznym miejscu! Następnie dotknij `Weryfikuj seed` i po weryfikacji `Otwórz Wallet`.


## 2️⃣ Ustawienia


Zanim zanurzymy się głębiej, rzućmy okiem na `Ekran główny` i `Ustawienia`.


Na ekranie głównym możemy zobaczyć różne wyświetlane elementy:



- menu `Hamburger` przenosi nas do `Ustawień`
- Dostępne saldo
- Karta cichej płatności, aby rozpocząć skanowanie transakcji wysyłanych na adres cichej płatności
- Karta Payjoin do `Włączenia` Payjoin jako funkcja chroniąca prywatność i oszczędzająca opłaty
- na dole znajdują się skróty do `Wallet Overview`, `Receive`, `Swap` pomiędzy Bitcoin i innymi walutami, `Send` i `Buy`


![image](assets/en/11.webp)


Stuknięcie ikony `Hamburger menu` otwiera menu ustawień. Przejrzyjmy dostępne opcje.


![image](assets/en/05.webp)


### A - Połączenie i synchronizacja 🔗


Tutaj możemy ponownie podłączyć wallet, zarządzać węzłami i połączyć się z własnym węzłem (zalecane). Opcja `Silent Payments Scanning` pozwala nam dostosować skanowanie poprzez określenie `Scan from block height` lub `Scan from date`.


![image](assets/en/06.webp)


Jako funkcja `Alpha` dostępna jest również opcja `Włącz wbudowany Tor`, aby kierować ruch przez sieć Tor.


### B - Ustawienia cichej płatności 🔈


Możemy włączyć kartę Silent Payments na ekranie głównym, aby wyświetlić tę funkcję. Włączenie funkcji "Zawsze skanuj" umożliwia wallet ciągłe monitorowanie łańcucha bloków pod kątem przychodzących cichych płatności. Możemy określić parametry skanowania, aby dostosować proces skanowania do naszych potrzeb, jak opisano powyżej.


![image](assets/en/07.webp)


### C - Bezpieczeństwo i kopie zapasowe 🗝️


Aby zabezpieczyć nasz wallet, możemy utworzyć kopię zapasową, postępując zgodnie z instrukcjami w aplikacji. Dzięki temu będziemy mieć bezpieczną kopię naszych kluczy prywatnych, co pozwoli nam odzyskać wallet w przypadku jego zgubienia lub kradzieży. Dodatkowo możemy wyświetlić naszą frazę seed i klucze prywatne, zmienić nasz kod PIN, włączyć uwierzytelnianie biometryczne, podpisać / zweryfikować i skonfigurować 2FA dla dodatkowej warstwy ochrony.


![image](assets/en/08.webp)


**Uwaga**: Od września 2025 r. uwierzytelnianie biometryczne odcisków palców na urządzeniach z systemem Android musi działać z co najmniej implementacją biometryczną klasy 2, aby uzyskać więcej informacji, zobacz [tutaj](https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Wymóg ten może jednak ulec zmianie w przyszłości.


### D - Ustawienia prywatności 🔒


Możemy również zwiększyć bezpieczeństwo naszego wallet, używając Tor do szyfrowania naszego połączenia internetowego i ochrony naszej prywatności podczas uzyskiwania dostępu do źródeł zewnętrznych. Dodatkowo, możemy zapobiec wykonywaniu zrzutów ekranu, aby zachować poufność naszych informacji wallet, włączyć automatyczne generowanie adresów, aby tworzyć nowe dla każdej transakcji, oraz wyłączyć akcje kupna/sprzedaży, aby zapobiec nieautoryzowanym transakcjom. Ponadto możemy `Włączyć PayJoin`, co jest kolejną funkcją prywatności, którą omówimy później.


![image](assets/en/09.webp)


### E - Inne ustawienia 🔧


Inne ustawienia pozwalają nam zarządzać priorytetem opłat i ustawić domyślny poziom opłat dla naszych transakcji. Pozwala nam to kontrolować opłaty transakcyjne związane z naszymi Cichymi Płatnościami, biorąc pod uwagę bieżące wykorzystanie sieci.


![image](assets/en/10.webp)


## 3️⃣ Odbieranie ₿itcoinów za pomocą Silent Payments


Istnieje kilka opcji i typów adresów dostępnych do odbierania Bitcoin. domyślną opcją jest `Segwit (P2WPKH)` *(zaczynający się od bc1q....)*.  W tym przykładzie wybierzmy `Silent Payments`.


Aby otrzymać cichą płatność, najpierw dotknij ikony "Odbierz" w Cake Wallet. Następnie wprowadź kwotę, którą chcesz otrzymać. Aby określić typ adresu, ponownie dotknij `Odbierz` w górnej części ekranu, a następnie wybierz `Ciche płatności` z opcji.


Na ekranie głównym wyświetlony zostanie kod QR Silent Payment wielokrotnego użytku oraz adres. Zgodnie z oczekiwaniami, adres jest dość długi:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Teraz użyj BIP-352 kompatybilnego z wallet (takiego jak Blue Wallet), aby zeskanować ten kod QR i wysłać płatność. Zobaczysz, że wallet wyprowadza unikalny adres docelowy z Twojego cichego adresu.


![image](assets/en/13.webp)


## 4️⃣ Wysyłanie ₿itcoin przy użyciu Silent Payments


Ponieważ Blue Wallet może tylko "wysyłać" ciche płatności, użyjemy innego BIP 352 kompatybilnego wallet jako strony odbierającej. Proces ten jest identyczny jak w przypadku zwykłej transakcji Bitcoin.



- Stuknij w `Wyślij` na ekranie głównym
- wklejając nasz adres wielokrotnego użytku `sp1qq...` lub skanując kod QR bezpośrednio w aplikacji.
- Wybierz kwotę, którą chcesz wydać z dostępnego salda
- Stuknij w "Wyślij" na dole ekranu, aby potwierdzić transakcję


Po wprowadzeniu adresu `sp1qq...`, wallet automatycznie wyprowadzi odpowiadający mu adres `bc1p...` Taproot (P2TR) w tle, który zostanie użyty do cichej płatności.


Opcjonalnie możemy napisać wewnętrzną notatkę dla każdej transakcji, dostosować ustawienia opłat lub wybrać określone UTXO dla transakcji za pomocą funkcji `Coin Control`.


![image](assets/en/14.webp)


przesuń palcem w prawo, aby potwierdzić transakcję.


Po wysłaniu transakcji zostaniesz zapytany, czy chcesz dodać ten kontakt do swojej książki adresowej.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Przyjrzyjmy się, czym jest PayJoin (https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


_Payjoin v2 to chroniąca prywatność i oszczędzająca opłaty funkcja Bitcoin, która pozwala nadawcy i odbiorcy transakcji współpracować w celu utworzenia pojedynczej transakcji. Ta transakcja ma dane wejściowe od *obu* nadawców i odbiorców, łamiąc najbardziej powszechne techniki nadzoru przeciwko Bitcoin i pozwalając na lepsze skalowanie i oszczędność opłat w niektórych okolicznościach


Aby dowiedzieć się więcej o PayJoin, możesz również odwiedzić poniższy samouczek.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Aby korzystać z PayJoin, obie strony potrzebują PayJoin kompatybilnego z wallet, a odbiorca musi mieć co najmniej jedną monetę lub wyjście w swoim wallet. Aby rozpocząć, wykonaj następujące kroki:


1. Stuknij w `Hamburger Menu` i stuknij w przycisk `Prywatność`

2. Przełącz opcję `Użyj Payjoin`

3.  Stuknij w `Odbierz` na ekranie głównym, a zostanie wyświetlony kod QR PayJoin i przycisk kopiowania (po wybraniu Segwit)


![image](assets/en/16.webp)


## 6️⃣ Inne funkcje


Istnieje kilka innych funkcji, takich jak wielowalutowe `Swapy`, opcje `Kup i Sprzedaj` z różnymi połączeniami sprzedawców oraz programy specyficzne dla Cake, takie jak `Cake Pay`, który pozwala na zakup kart przedpłaconych lub kart podarunkowych.


![image](assets/en/17.webp)


## wnioski


Oto nasza recenzja Cake Wallet, który oferuje praktyczną prywatność Bitcoin dzięki takim funkcjom jak Silent Payments (BIP-352) i Payjoin v2.


Ciche płatności zastępują jednorazowe adresy adresami wielokrotnego użytku, aby zapobiec powiązaniu przychodzących transakcji z on-chain. Chociaż kwestie synchronizacji w poprzednich wersjach uległy znacznej poprawie, istnieją pewne zwiększone wymagania obliczeniowe dotyczące skanowania i wykrywania Silent Payments, wymagające większej ilości zasobów i przepustowości.


Payjoin v2 zakłóca analizę łańcucha, łącząc dane wejściowe nadawcy i odbiorcy w pojedyncze transakcje bez dodatkowych opłat lub centralnej koordynacji. Łamie to powszechną heurystykę własności danych wejściowych, co jest znaczącą zaletą, ponieważ oznacza, że nie można założyć, że wszystkie dane wejściowe należą do nadawcy.


Dla użytkowników, dla których priorytetem jest anonimowość finansowa, Cake Wallet jest realną opcją. Zawiera on protokoły prywatności bezpośrednio w swojej podstawowej funkcjonalności, dzięki czemu są one dostępne bez żadnych technicznych komplikacji. Wraz ze wzrostem nadzoru nad publicznymi blockchainami, narzędzia takie jak to pomagają zachować prywatność transakcji tam, gdzie ma to największe znaczenie. Szersze wdrożenie tych standardów w ramach wallet byłoby mile widziane.


## zasoby


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/