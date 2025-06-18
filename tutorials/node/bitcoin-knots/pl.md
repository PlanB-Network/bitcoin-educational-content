---
name: Węzły Bitcoin
description: Jak uruchomić węzeł za pomocą alternatywnego klienta Bitcoin Knots?
---
![cover](assets/cover.webp)


Bitcoin Knots to alternatywna implementacja protokołu Bitcoin, wywodząca się z Bitcoin Core. Zaprojektowany i utrzymywany przez Luke'a Dashjra, oferuje kilka dodatkowych funkcji i dostosowań reguł z Mempool, pozostając jednocześnie kompatybilnym z innymi węzłami w sieci. Bitcoin Knots integruje Bitcoin Wallet, ale może być również używany jako prosty węzeł Bitcoin wraz z innym oprogramowaniem Wallet.


## Dlaczego warto używać węzłów zamiast rdzenia?


Obecnie Core stanowi większość implementacji protokołu Bitcoin w sieci. Protokół Bitcoin to tylko zestaw reguł. Wymaga oprogramowania do ich stosowania. Maszyna z uruchomionym oprogramowaniem implementującym protokół Bitcoin nazywana jest węzłem, a wszystkie te węzły razem tworzą sieć Bitcoin.


W całej historii Bitcoin pojawiło się wiele klientów wywodzących się z początkowego oprogramowania opracowanego przez Satoshi Nakamoto. Obecnie (marzec 2025 r.) Bitcoin Core stanowi przytłaczającą większość, a prawie 98% węzłów w sieci Bitcoin korzysta z tego klienta.


Dostępne jest jednak również alternatywne oprogramowanie. Nie są to węzły połączone z Altcoin, takie jak Bitcoin Cash, ale alternatywne klienty kompatybilne z prawdziwą siecią Bitcoin. Spośród nich najbardziej znany jest Bitcoin Knots. Stanowi on obecnie około 1,4% sieci. Inni alternatywni klienci wciąż stanowią mniejszość.


![Image](assets/fr/01.webp)


Istnieją dwa główne powody, dla których warto używać alternatywnego klienta, takiego jak Knots, zamiast Core:




- Techniczne**: Klienci ci często oferują różne opcje dla Core, zwłaszcza w zakresie zarządzania Mempool, określając, które transakcje są akceptowane i transmitowane przez węzeł.
- Polityka**: Niektórzy ludzie wolą używać alternatywnych klientów, takich jak Knots, z powodów nietechnicznych, zwłaszcza w celu wspierania alternatywy dla Core, a tym samym zmniejszenia jego monopolu. Jeśli Core zostałby kiedykolwiek skompromitowany, przydatne byłoby nie tylko posiadanie solidnych, dobrze utrzymanych alternatywnych klientów, ale także wiedza, jak z nich korzystać. Inni używają Knots w celach protestacyjnych, ponieważ stracili zaufanie do programistów Core lub nie pochwalają zarządzania klientem większościowym.


## Jak zainstalować węzły Bitcoin?


Przejdź do [oficjalnej strony Bitcoin Knots] (https://bitcoinknots.org/#download), aby pobrać wersję dla swojego systemu operacyjnego. Nie zapomnij pobrać odcisku palca i podpisów, aby zweryfikować oprogramowanie. Pliki te są również dostępne [na repozytorium Bitcoin Knots GitHub](https://github.com/bitcoinknots/Bitcoin).


![Image](assets/fr/02.webp)


Przed zainstalowaniem oprogramowania na komputerze zdecydowanie zalecamy sprawdzenie jego autentyczności i integralności. Jeśli nie wiesz, jak to zrobić, zapoznaj się z tym samouczkiem:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Po zweryfikowaniu oprogramowania należy je zainstalować, wykonując czynności wskazane w panelu instalacyjnym.


![Image](assets/fr/03.webp)


## Uruchomienie IBD


Przy pierwszym uruchomieniu Bitcoin Knots będziesz mógł wybrać lokalny katalog, w którym przechowywane będą dane węzła (w tym zestaw Blockchain, UTXO i parametry).


![Image](assets/fr/04.webp)


Można również wybrać opcję przycinania danych Blockchain, aby zachować tylko najnowsze bloki. Opcja ta umożliwia węzłowi sprawdzanie każdego bloku w całości w ramach ustalonego limitu miejsca, a tym samym stopniowe usuwanie najstarszych bloków. Jeśli masz wystarczającą ilość miejsca na dysku (obecnie około 650 GB, ale liczba ta rośnie), pozostaw tę opcję niezaznaczoną. Jeśli przestrzeń dyskowa jest ograniczona, należy aktywować przycinanie i określić maksymalną dozwoloną pojemność.


Uwaga: Jeśli węzeł zostanie przycięty i użyjesz go do synchronizacji odzyskanego Wallet, nie będziesz w stanie pobrać transakcji sprzed najstarszego lokalnie przechowywanego bloku.


![Image](assets/fr/05.webp)


Inną dostępną opcją jest "*Assume Valid*". Przyspiesza ona początkową synchronizację poprzez pominięcie weryfikacji podpisu dla transakcji zawartych w blokach poprzedzających określony blok.


Celem "*Assume Valid*" jest przyspieszenie pierwszej synchronizacji węzła bez znaczącego zmniejszania bezpieczeństwa, poprzez założenie, że transakcje te zostały już wcześniej masowo zweryfikowane przez sieć. Jedynym ważnym kompromisem jest to, że węzeł nie wykryje żadnych wcześniejszych kradzieży Bitcoin, ale nadal będzie gwarantował dokładność całkowitej liczby wydanych bitcoinów. Twój węzeł zweryfikuje wszystkie podpisy transakcji po określonym bloku. Podejście to opiera się na założeniu, że transakcja, która przez długi czas była akceptowana przez sieć bez kwestionowania, jest najprawdopodobniej ważna.


Na przykład tutaj "*Assume Valid*" jest ustawione na blok nr. 855 000 `00000000000000000000000233ea80aa10d38aa4486cd7033fffc2c4df556d0b9138`, opublikowany 1 sierpnia 2024 roku. Podczas IBD mój węzeł rozpocznie zatem pełną weryfikację podpisu tylko od tego bloku.


![Image](assets/fr/06.webp)


Następnie kliknij przycisk "*OK*", aby uruchomić *Initial Block Download*. Podczas początkowej synchronizacji węzłów należy uzbroić się w cierpliwość. Jeśli chcesz wznowić synchronizację później, po prostu zamknij oprogramowanie i wyłącz komputer. Synchronizacja zostanie wznowiona przy następnym uruchomieniu programu.


![Image](assets/fr/07.webp)


## Konfiguracja węzła Bitcoin


Kliknij zakładkę "*Ustawienia*", a następnie wybierz "*Opcje*".


![Image](assets/fr/08.webp)


W zakładce "*Main*" można uzyskać dostęp do głównych parametrów węzła:




- "*Start...*" automatycznie uruchamia węzeł po uruchomieniu komputera, aby natychmiast rozpocząć synchronizację;
- "*Prune...*" dostosowuje limit pamięci, jeśli wybrano przycinanie Blockchain;
- "*Database cache...*" ustawia maksymalną ilość pamięci RAM dozwoloną dla węzła;
- Na koniec aktywuj opcję "*Włącz serwer RPC*", jeśli chcesz połączyć węzeł Bitcoin Knots z innym oprogramowaniem Wallet, takim jak na przykład Sparrow Wallet lub Liana.


![Image](assets/fr/09.webp)


W zakładce "*Wallet*" znajdziesz ustawienia dla zintegrowanego Wallet, który możesz utworzyć później na Knots. Zalecam aktywowanie RBF i kontroli monet. Możesz również zdefiniować typ skryptu, który ma być używany.


![Image](assets/fr/10.webp)


Zakładka "*Network*" zawiera parametry sieciowe, które można dostosować do własnych potrzeb.


![Image](assets/fr/11.webp)


Zakładka "*Mempool*" pozwala skonfigurować *Memory Pool*, czyli zarządzanie niepotwierdzonymi transakcjami przechowywanymi w pamięci oraz maksymalny rozmiar przypisany do tej funkcjonalności (domyślnie 300 MB).


![Image](assets/fr/12.webp)


Zakładka "Filtrowanie spamu" to funkcja Bitcoin Knots. Znajduje się tutaj szereg ustawień, które pozwalają wybrać, które transakcje będą akceptowane lub odrzucane. Głównym celem jest ograniczenie pewnych marginalnych zastosowań Bitcoin, w szczególności meta-protokołów, w celu zwalczania tych praktyk przy jednoczesnym uniknięciu przeciążenia węzła. Jest to wybór polityczny, w zależności od osobistej wizji Bitcoin.


Znajdziesz tu również klasyczne parametry, takie jak definicja progu "*Dust*".


Parametry te wpływają jednak tylko na zasady standaryzacji. Twój węzeł będzie nadal akceptował niepotwierdzone transakcje tylko wtedy, gdy są one zawarte w bloku, aby zachować zgodność z resztą sieci Bitcoin. Ustawienia te modyfikują jedynie sposób, w jaki węzeł przetwarza i dystrybuuje niepotwierdzone transakcje do swoich rówieśników. W praktyce, ponieważ Knots jest w mniejszości, to zasady ustalone domyślnie w Bitcoin Core definiują standaryzację w sieci.


![Image](assets/fr/13.webp)


Zakładka "*Mining*" pozwala skonfigurować możliwy udział węzła w Mining, jeśli chcesz aktywować tę funkcję.


![Image](assets/fr/14.webp)


Wreszcie, zakładka "*Display*" dotyczy parametrów związanych z grafiką Interface, w tym języka oprogramowania.


![Image](assets/fr/15.webp)


## Tworzenie Bitcoin Wallet


Po zakończeniu początkowej synchronizacji węzeł Bitcoin Knots jest w pełni funkcjonalny. Masz teraz możliwość podłączenia tego węzła do innego oprogramowania Wallet lub bezpośredniego użycia wbudowanego Hot Wallet. Aby to zrobić, kliknij przycisk "*Utwórz nowy Wallet*".


![Image](assets/fr/16.webp)


Nadaj swojemu Wallet nazwę. Możesz również zabezpieczyć go za pomocą passphrase BIP39, klikając "*Encrypt Wallet*". Gdy wszystko będzie gotowe, kliknij przycisk "*Create*".


![Image](assets/fr/17.webp)


passphrase BIP39 to opcjonalne hasło, które można dowolnie wybrać, oprócz frazy Mnemonic, w celu zwiększenia bezpieczeństwa Wallet. Przed skonfigurowaniem tej funkcji zdecydowanie zalecamy przeczytanie poniższego artykułu, który szczegółowo wyjaśnia, jak w teorii działa passphrase i jak uniknąć błędów, które mogą doprowadzić do trwałej utraty bitcoinów:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Jeśli aktywowałeś opcję passphrase, wybierz solidną i ostrożnie zapisz ją na jednym lub kilku bezpiecznych nośnikach fizycznych.


![Image](assets/fr/18.webp)


Twój Bitcoin Wallet został utworzony.


![Image](assets/fr/19.webp)


## Tworzenie kopii zapasowej Bitcoin Wallet


Jeszcze przed otrzymaniem pierwszych bitcoinów należy wykonać kopię zapasową Bitcoin Wallet, aby móc odzyskać środki w przypadku utraty lub awarii komputera. Aby to zrobić, kliknij zakładkę "*File*", a następnie "*Backup Wallet*".


![Image](assets/fr/20.webp)


Ta operacja generuje pojedynczy plik, który może zostać użyty do przywrócenia wszystkich bitcoinów. Bądź więc bardzo ostrożny i zapisz go na bezpiecznym nośniku zewnętrznym.


## Odbieranie bitcoinów


Aby otrzymać bitcoiny bezpośrednio na konto Knots Wallet, kliknij przycisk "*Odbierz*".


![Image](assets/fr/21.webp)


Przypisz "*Label*" do swojego Address, aby łatwo zidentyfikować jego przeznaczenie i ułatwić przyszłe korzystanie z *Coin Control*. Możesz także z góry określić dokładną kwotę, która ma zostać odebrana na tym Address, lub dodać wiadomość dla płatnika. Po ustawieniu parametrów kliknij "*Request payment*".


![Image](assets/fr/22.webp)


Bitcoin Knots wyświetla następnie otrzymany Address, który można skopiować lub zeskanować i wysłać do płatnika.


![Image](assets/fr/23.webp)


Po nadaniu transakcji można śledzić jej status bezpośrednio w menu "*Transakcje*".


![Image](assets/fr/24.webp)


## Wysyłanie bitcoinów


Teraz, gdy masz już bitcoiny w swoim Knots Wallet, możesz je wysłać. Aby to zrobić, kliknij przycisk "*Wyślij*".


![Image](assets/fr/25.webp)


Kliknij przycisk "*Inputs...*", aby wybrać dokładny UTXO, który chcesz wydać na tę transakcję.


![Image](assets/fr/26.webp)


Wprowadź Bitcoin Address odbiorcy.


![Image](assets/fr/27.webp)


Dodaj etykietę, aby zapamiętać cel tej transakcji.


![Image](assets/fr/28.webp)


Wprowadź kwotę, którą chcesz wysłać do tego Address.


![Image](assets/fr/29.webp)


Kliknij przycisk "*Wybierz...*", aby wybrać odpowiednią stawkę opłaty za transakcję, w oparciu o aktualny status sieci.


![Image](assets/fr/30.webp)


Jeśli wszystko się zgadza, kliknij przycisk "*Wyślij*". Jeśli korzystasz z passphrase, na tym etapie zostaniesz poproszony o jego wypełnienie.


![Image](assets/fr/31.webp)


Sprawdź parametry transakcji po raz ostatni, a następnie, jeśli wszystko się zgadza, ponownie kliknij przycisk "*Wyślij*", aby podpisać i rozpowszechnić transakcję.


![Image](assets/fr/32.webp)


Twoja transakcja oczekująca na potwierdzenie pojawi się teraz w zakładce "*Transakcje*".


![Image](assets/fr/33.webp)


## Podłączanie węzła do innego programu


Zintegrowany Bitcoin Knots do zarządzania Bitcoin Wallet niekoniecznie jest najbardziej intuicyjny, a jego funkcjonalność pozostaje stosunkowo ograniczona. Można jednak podłączyć węzeł Bitcoin Knots do specjalistycznego oprogramowania do zarządzania Wallet, aby łatwo uzyskać dostęp do danych Blockchain Bitcoin i transmitować transakcje.


Procedura będzie zależeć od używanego oprogramowania, ale istnieją dwa główne scenariusze: albo Bitcoin Knots jest zainstalowany na tym samym komputerze co oprogramowanie Wallet, albo działa na oddzielnym komputerze.


### Z lokalnymi węzłami Bitcoin:


Jeśli Bitcoin Knots jest zainstalowany na komputerze, zlokalizuj plik `Bitcoin.conf` wśród plików oprogramowania. Jeśli plik ten nie istnieje, można go utworzyć. Otwórz go za pomocą edytora tekstu i wstaw następującą linię:


```ini
server=1
```


Następnie zapisz zmiany.


Można to również zrobić za pomocą grafiki Interface Bitcoin-QT, przechodząc do "*Ustawienia*" > "*Opcje...*" i włączając opcję "*Włącz serwer RPC*".


Nie zapomnij ponownie uruchomić oprogramowania po wprowadzeniu tych zmian.


![Image](assets/fr/34.webp)


Następnie przejdź do oprogramowania zarządzającego Wallet (np. Sparrow Wallet lub Liana) i wprowadź ścieżkę do pliku cookie, zwykle znajdującego się w tym samym folderze co `Bitcoin.conf`, w zależności od systemu operacyjnego:


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

![Image](assets/fr/35.webp)


Pozostaw pozostałe parametry jako domyślne, URL `127.0.0.1` i port `8332`, a następnie kliknij na "*Test Connection*".


![Image](assets/fr/36.webp)


### Ze zdalnym Bitcoin Knots :


Jeśli Bitcoin Knots jest zainstalowany na innym komputerze podłączonym do tej samej sieci, najpierw zlokalizuj plik `Bitcoin.conf` wśród plików oprogramowania. Jeśli plik ten jeszcze nie istnieje, można go utworzyć. Otwórz ten plik za pomocą edytora tekstu i dodaj następującą linię:


```ini
server=1
```


Po edycji pliku upewnij się, że zapisałeś go w odpowiednim folderze dla swojego systemu operacyjnego:


|**macOS**|~/Library/Application Support/Bitcoin|
|---|---|
|**Windows**|%APPDATA%\Bitcoin|
|**Linux**|~/.Bitcoin|

Tę operację można również wykonać za pomocą grafiki Bitcoin-QT Interface. Przejdź do menu "*Ustawienia*", a następnie "*Opcje...*" i aktywuj opcję "*Włącz serwer RPC*", zaznaczając odpowiednie pole. Jeśli plik `Bitcoin.conf` nie istnieje, można go utworzyć bezpośrednio z tego Interface klikając na "*Open Configuration File*".


![Image](assets/fr/37.webp)


Znajdź adres IP Address urządzenia hostującego Bitcoin Knots w sieci lokalnej. Aby to zrobić, możesz użyć narzędzia takiego jak [Angry IP Scanner](https://angryip.org/). Załóżmy, dla celów argumentacji, że adres IP Address węzła to `192.168.1.18`.


W pliku `Bitcoin.conf` dodaj następujące linie, ustawiając `rpcbind=192.168.1.18`, aby pasowały do IP Address twojego węzła.


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/38.webp)


Dodaj również nazwę użytkownika i hasło dla połączeń zdalnych do pliku `Bitcoin.conf`. Pamiętaj, aby zastąpić `loic` swoją nazwą użytkownika, a `my_password` silnym hasłem:


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/39.webp)


Po zmodyfikowaniu i zapisaniu pliku uruchom ponownie Bitcoin Knots.


Teraz można przejść do oprogramowania do zarządzania Wallet (np. Sparrow Wallet lub Liana). W Sparrow przejdź do zakładki "*User / Pass*". Wprowadź nazwę użytkownika i hasło skonfigurowane w pliku `Bitcoin.conf`. Pozostałe parametry pozostaw domyślne, tj. adres URL `127.0.0.1` i port `8332`. Następnie kliknij na "*Test Connection*".


![Image](assets/fr/40.webp)


Połączenie zostało nawiązane.


Teraz wiesz już wszystko o alternatywnej implementacji Bitcoin Knots.


Jeśli uznałeś ten poradnik za przydatny, będę bardzo wdzięczny, jeśli zostawisz poniżej kciuk Green. Zapraszam do udostępnienia go w sieciach społecznościowych. Dziękuję bardzo!


Polecam również ten samouczek, w którym wyjaśniam, jak skonfigurować własny węzeł Lightning:


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a