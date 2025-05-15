---
name: Wróbel Wallet
description: Instalowanie, konfigurowanie i używanie Sparrow Wallet
---
![cover](assets/cover.webp)


Sparrow Wallet to oprogramowanie do samodzielnego zarządzania Bitcoin Wallet opracowane przez Craiga Raw. To oprogramowanie o otwartym kodzie źródłowym jest cenione przez bitcoinerów za wiele funkcji i intuicyjną obsługę Interface.


Istnieją dwa sposoby korzystania z aplikacji Sparrow:




- Podobnie jak Hot Wallet, gdzie klucze prywatne są przechowywane na komputerze.
- Jako menedżer Cold Wallet, gdzie klucze prywatne są przechowywane na Hardware Wallet. W tym trybie Sparrow manipuluje tylko publicznymi informacjami Wallet, śledzi fundusze, generuje adresy i tworzy transakcje, ale podpis Hardware Wallet jest wymagany, aby te transakcje były ważne. Może zatem zastąpić aplikacje takie jak Ledger Live lub Trezor Suite.


Sparrow obsługuje portfele z jednym i wieloma podpisami oraz umożliwia płynne zarządzanie wieloma portfelami. Na przykład można jednocześnie kontrolować jeden Wallet podłączony do Ledger, inny do Trezora, a także mieć Hot Wallet.


Oprogramowanie oferuje również zaawansowane funkcje kontroli monet, pozwalając precyzyjnie wybrać, które UTXO mają być używane w transakcjach, aby zoptymalizować poufność.


Jeśli chodzi o połączenie, Sparrow pozwala połączyć się z własnym węzłem Bitcoin, zdalnie za pośrednictwem serwera Electrum lub za pomocą Bitcoin Core. Możliwe jest również użycie węzła publicznego, jeśli nie masz jeszcze własnego. Zdalne połączenia są nawiązywane za pośrednictwem sieci Tor.


## Zainstaluj Sparrow Wallet


Przejdź do [oficjalnej strony pobierania Sparrow Wallet] (https://sparrowwallet.com/download/) i wybierz wersję oprogramowania odpowiadającą Twojemu systemowi operacyjnemu.


![Image](assets/fr/01.webp)


Ważne jest, aby sprawdzić integralność i autentyczność oprogramowania przed jego zainstalowaniem. Jeśli nie wiesz, jak to zrobić, tutaj znajdziesz kompletny samouczek:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Po zainstalowaniu Sparrow można pominąć początkowe ekrany objaśniające i przejść bezpośrednio do ekranu zarządzania połączeniami.


![Image](assets/fr/02.webp)


![video](https://www.youtube.com/watch?v=MyDMvjGFdDE)



![video](https://youtu.be/IThaolnDgSo)


## Podłączanie do sieci Bitcoin


Aby wchodzić w interakcje z siecią Bitcoin i transmitować swoje transakcje, Sparrow musi być połączony z węzłem Bitcoin. Istnieją trzy główne sposoby nawiązania takiego połączenia:



- korzystanie z węzła publicznego, tj. łączenie się z węzłem innej firmy, który zezwala na takie połączenia. Jeśli nie masz własnego węzła Bitcoin, ta opcja pozwala szybko rozpocząć korzystanie ze Sparrow. Jednak węzeł, z którym się łączysz, będzie widział wszystkie twoje transakcje, co może zagrozić twojej poufności. Kontrola nad kluczami jest niezbędna, ale posiadanie własnego węzła jest jeszcze lepsze. Korzystaj więc z tej opcji tylko wtedy, gdy dopiero zaczynasz, mając świadomość ryzyka dla swojej prywatności.
- podłączanie do węzła Bitcoin Core. Jeśli masz własny węzeł Bitcoin Core, możesz podłączyć go do Sparrow Wallet, lokalnie, jeśli Bitcoin Core jest zainstalowany na tym samym komputerze, lub zdalnie.
- połączenie przez serwer Electrum. Jeśli twój węzeł Bitcoin jest wyposażony w Electrs, tak jak w przypadku rozwiązań node-in-a-box, takich jak Umbrel lub Start9, możesz połączyć się z nim zdalnie ze Sparrow.


**Zaleca się korzystanie z połączenia za pośrednictwem Electrs lub Bitcoin Core na własnym węźle, aby zmniejszyć potrzebę zaufania stronie trzeciej i zoptymalizować poufność**


### Połączenie z węzłem publicznym 🟡


Łączenie się z węzłem publicznym jest bardzo proste. Kliknij zakładkę "*Public Server*".


![Image](assets/fr/03.webp)


Wybierz węzeł z listy rozwijanej.


![Image](assets/fr/04.webp)


Następnie kliknij "*Testuj połączenie*".


![Image](assets/fr/05.webp)


Po połączeniu, Sparrow Wallet wyświetli żółty haczyk w prawym dolnym rogu Interface, aby wskazać, że jesteś połączony z węzłem publicznym.


![Image](assets/fr/06.webp)


### Podłączenie do Bitcoin Core 🟢


Drugą metodą połączenia z węzłem Bitcoin jest połączenie Sparrow z Bitcoin Core. Jeśli Bitcoin Core jest zainstalowany na tym samym komputerze, uwierzytelnianie będzie odbywać się za pomocą pliku cookie. Jeśli Bitcoin Core znajduje się na zdalnej maszynie, będziesz musiał użyć hasła zdefiniowanego w pliku `Bitcoin.conf`.


Należy pamiętać, że jeśli użyjesz przyciętego węzła Bitcoin Core, nie będziesz w stanie przywrócić Wallet zawierającego transakcje poprzedzające lokalnie przechowywane bloki. Jednak w przypadku nowego Wallet utworzonego na Sparrow nie będzie to problemem: nowe transakcje będą widoczne, nawet w przypadku przyciętego węzła.


Aby skonfigurować węzeł Bitcoin Core, można skorzystać z jednego z poniższych samouczków, w zależności od systemu operacyjnego:


https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

W aplikacji Sparrow przejdź do zakładki "*Bitcoin Core*".


![Image](assets/fr/07.webp)


**Z Bitcoin Core local:**


Jeśli Bitcoin Core jest zainstalowany na komputerze, zlokalizuj plik `Bitcoin.conf` wśród plików oprogramowania. Jeśli plik ten nie istnieje, można go utworzyć. Otwórz go za pomocą edytora tekstu i wstaw następującą linię:


```ini
server=1
```


Następnie zapisz zmiany.


Można to również zrobić za pomocą grafiki Interface w Bitcoin-QT, przechodząc do "*Ustawienia*" > "*Opcje...*" i aktywując opcję "*Włącz serwer RPC*".


Nie zapomnij ponownie uruchomić oprogramowania po wprowadzeniu tych zmian.


![Image](assets/fr/08.webp)


Następnie wróć do Sparrow Wallet i wprowadź ścieżkę do pliku cookie, zwykle znajdującego się w tym samym folderze co `Bitcoin.conf`, w zależności od systemu operacyjnego:


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)


Pozostaw pozostałe parametry jako domyślne, URL `127.0.0.1` i port `8332`, a następnie kliknij na "*Test Connection*".


![Image](assets/fr/10.webp)


Połączenie zostało nawiązane. W prawym dolnym rogu pojawi się znacznik Green wskazujący na połączenie z węzłem Bitcoin Core.


![Image](assets/fr/11.webp)


**Z pilotem Bitcoin Core:**


Jeśli Bitcoin Core jest zainstalowany na innym komputerze podłączonym do tej samej sieci, najpierw zlokalizuj plik `Bitcoin.conf` wśród plików oprogramowania. Jeśli plik ten jeszcze nie istnieje, można go utworzyć. Otwórz ten plik za pomocą edytora tekstu i dodaj następującą linię:


```ini
server=1
```


Po edycji pliku upewnij się, że zapisałeś go w odpowiednim folderze dla swojego systemu operacyjnego:


| **macOS** | ~/Library/Application Support/Bitcoin |
| ----------- | ------------------------------------- |
| **Windows** | %APPDATA%\Bitcoin |
| **Linux** | ~/.Bitcoin |

Tę operację można również wykonać za pomocą graficznego Bitcoin-QT Interface. Przejdź do menu "*Ustawienia*", a następnie "*Opcje...*" i aktywuj opcję "*Włącz serwer RPC*", zaznaczając odpowiednie pole. Jeśli plik `Bitcoin.conf` nie istnieje, można go utworzyć bezpośrednio z tego Interface klikając na "*Open Configuration File*".


![Image](assets/fr/12.webp)


Znajdź adres IP Address maszyny hostującej Bitcoin Core w sieci lokalnej. Aby to zrobić, możesz użyć narzędzia takiego jak [Angry IP Scanner](https://angryip.org/). Załóżmy, dla celów argumentacji, że adres IP Address węzła to `192.168.1.18`.


W pliku `Bitcoin.conf` dodaj następujące linie, ustawiając `rpcbind=192.168.1.18`, aby pasowały do adresu IP Address węzła.


```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```


![Image](assets/fr/13.webp)


W pliku `Bitcoin.conf` dodaj nazwę użytkownika i hasło dla połączeń zdalnych. Upewnij się, że zastąpiłeś `loic` swoją nazwą użytkownika, a `my_password` silnym hasłem:


```ini
rpcuser=loic
rpcpassword=my_password
```


![Image](assets/fr/14.webp)


Po zmodyfikowaniu i zapisaniu pliku należy ponownie uruchomić oprogramowanie Bitcoin-QT.


Możesz teraz powrócić do Sparrow Wallet. Przejdź do zakładki "*User / Pass*". Wprowadź nazwę użytkownika i hasło skonfigurowane w pliku `Bitcoin.conf`. Pozostałe parametry pozostaw domyślne, tj. adres URL `127.0.0.1` i port `8332`. Następnie kliknij na "*Test Connection*".


![Image](assets/fr/15.webp)


Połączenie zostało nawiązane. W prawym dolnym rogu pojawi się znacznik Green wskazujący na połączenie z węzłem Bitcoin Core.


![Image](assets/fr/16.webp)


![video](https://www.youtube.com/watch?v=9Aw6OAXxE_Y)


### Łączenie się z serwerem Electrum 🔵


Ostatnią opcją połączenia jest użycie zdalnego serwera Electrum. Ta metoda pozwala połączyć się z węzłem za pośrednictwem sieci Tor z innego urządzenia i wykorzystuje indeksator do szybszego przeglądania portfeli na Sparrow. Jest to szczególnie przydatne, jeśli masz rozwiązanie typu node-in-a-box, takie jak Umbrel lub Start9, które pozwalają zainstalować Electrum za pomocą jednego kliknięcia.


Aby to zrobić, uzyskaj Address Tor `.onion' swojego serwera Electrum. Na przykład w przypadku Umbrel można go znaleźć w aplikacji Electrs.


![Image](assets/fr/17.webp)


W Sparrow Wallet przejdź do zakładki "*Private Electrum*".


![Image](assets/fr/18.webp)


Wprowadź Tor Address w odpowiednim miejscu. Inne ustawienia mogą pozostać domyślne. Następnie kliknij "*Testuj połączenie*".


![Image](assets/fr/19.webp)


Połączenie zostało potwierdzone. Jeśli zamkniesz to okno, w prawym dolnym rogu pojawi się niebieski haczyk, wskazujący, że jesteś połączony z serwerem Electrum.


![Image](assets/fr/20.webp)


## Utwórz Hot Wallet


Teraz, gdy Sparrow Wallet jest skonfigurowany do komunikacji z siecią Bitcoin, możesz utworzyć swój pierwszy Wallet. Ta sekcja poprowadzi Cię przez proces tworzenia Hot Wallet, tj. Wallet, którego klucze prywatne są przechowywane na Twoim komputerze. Ponieważ komputer jest złożoną maszyną podłączoną do Internetu, stanowi bardzo dużą powierzchnię ataku. W związku z tym Hot Wallet powinien być używany tylko do ograniczonych ilości bitcoinów. Aby przechowywać większe kwoty, wybierz bezpieczny Wallet z Hardware Wallet. Jeśli to jest to, czego szukasz, możesz przejść do następnej sekcji.


Aby utworzyć Hot Wallet, na ekranie głównym Sparrow Wallet kliknij zakładkę "*Plik*", a następnie "*Nowy Wallet*".


![Image](assets/fr/21.webp)


Wprowadź nazwę swojego Wallet i kliknij "*Create Wallet*".


![Image](assets/fr/22.webp)


W górnej części Interface można wybrać, czy ma zostać utworzony "*Podpis pojedynczy*" czy "*Podpis wielokrotny*" Wallet. Tuż poniżej należy wybrać typ skryptu do blokowania UTXO. Zalecam użycie najnowszego standardu: "*Taproot (P2TR)*".


![Image](assets/fr/23.webp)


Następnie kliknij "*Nowy lub zaimportowany Software Wallet*".


![Image](assets/fr/24.webp)


Wybierz standard BIP39, ponieważ jest on obsługiwany przez praktycznie całe oprogramowanie Bitcoin Wallet. Następnie wybierz długość frazy odzyskiwania. Obecnie 12-wyrazowa fraza jest wystarczająca, ponieważ obie oferują podobne bezpieczeństwo, ale 12-wyrazowa fraza jest łatwiejsza do zapisania.


![Image](assets/fr/25.webp)


Kliknij przycisk "*generate New*", aby uzyskać frazę generate dla Wallet w Mnemonic. Ta fraza daje pełny, nieograniczony dostęp do wszystkich bitcoinów. Każdy, kto posiada tę frazę, może ukraść twoje środki, nawet bez fizycznego dostępu do twojego komputera.


12-wyrazowa fraza przywraca dostęp do bitcoinów w przypadku utraty, kradzieży lub uszkodzenia komputera. Dlatego bardzo ważne jest, aby zapisać ją ostrożnie i przechowywać w bezpiecznym miejscu.


Można umieścić go na papierze lub, w celu zwiększenia bezpieczeństwa, wygrawerować go na stali nierdzewnej, aby chronić go przed pożarem, powodzią lub zawaleniem. Wybór nośnika dla Mnemonic zależy od strategii bezpieczeństwa, ale jeśli używasz Sparrow jako ciepłego Wallet zawierającego umiarkowane ilości, papier powinien być wystarczający.


Aby uzyskać więcej informacji na temat prawidłowego sposobu zapisywania i zarządzania frazą Mnemonic, zdecydowanie polecam skorzystanie z tego samouczka, zwłaszcza jeśli jesteś początkującym:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
![Image](assets/fr/26.webp)


**Oczywiście nigdy nie wolno udostępniać tych słów w Internecie, tak jak robię to w tym samouczku. Ten przykład Wallet będzie używany tylko na Testnet i zostanie usunięty po zakończeniu samouczka


Możesz również dodać passphrase BIP39, klikając pole "*Użyj passphrase*". Ostrzeżenie: korzystanie z passphrase może być bardzo przydatne, ale jeśli nie rozumiesz, jak to działa, może być bardzo ryzykowne. Dlatego zdecydowanie radzę przeczytać ten krótki artykuł teoretyczny na ten temat:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Po zapisaniu Mnemonic i dowolnego passphrase na nośniku fizycznym kliknij "*Potwierdź kopię zapasową*".


![Image](assets/fr/27.webp)


Ponownie wprowadź 12 słów, aby potwierdzić, że zostały poprawnie zapisane, a następnie kliknij "*Create Keystore*".


![Image](assets/fr/28.webp)


Następnie kliknij "*Import Keystore*", aby generate klucze Wallet z frazy Mnemonic.


![Image](assets/fr/29.webp)


Kliknij "*Zastosuj*", aby sfinalizować tworzenie Wallet.


![Image](assets/fr/30.webp)


Ustaw silne hasło, aby zabezpieczyć dostęp do urządzenia Sparrow Wallet. Dobrym pomysłem jest przechowywanie tego hasła w menedżerze haseł, aby go nie zapomnieć. Należy pamiętać, że to hasło nie odgrywa żadnej roli w tworzeniu kluczy. Jest ono używane tylko w celu uzyskania dostępu do Wallet za pośrednictwem Sparrow Wallet. Tak więc, nawet bez tego hasła, fraza Mnemonic wystarczy, aby uzyskać dostęp do bitcoinów z dowolnej aplikacji kompatybilnej z BIP39.


![Image](assets/fr/31.webp)


Twój Hot Wallet został utworzony. Możesz pominąć sekcję *Odbieranie Bitcoinów* tego samouczka, jeśli nie planujesz używać Hardware Wallet ze Sparrow.


## Zarządzanie Cold Wallet


Drugim sposobem użycia Sparrow Wallet jest skonfigurowanie go jako menedżera Wallet z Hardware Wallet. W tej konfiguracji klucze prywatne Bitcoin Wallet pozostają wyłącznie na Hardware Wallet, podczas gdy Sparrow uzyskuje dostęp tylko do informacji publicznych. Takie podejście zapewnia wyższy poziom bezpieczeństwa niż portfele Hot omówione powyżej, ponieważ klucze prywatne są przechowywane na wyspecjalizowanym urządzeniu, często z bezpiecznym chipem, które nie jest podłączone do Internetu, a zatem stanowi znacznie mniejszą powierzchnię ataku niż tradycyjny komputer.


Istnieją dwa główne sposoby podłączenia Hardware Wallet do Sparrow:




- Kabel, powszechnie używany z podstawowymi modelami, takimi jak Trezor Safe 3 lub Ledger Nano S Plus;
- W trybie Air-Gap, tj. bez bezpośredniego połączenia przewodowego, za pośrednictwem karty MicroSD lub kodu QR Exchange.


Sparrow obsługuje wszystkie te metody komunikacji i jest kompatybilny z większością portfeli sprzętowych dostępnych na rynku.


W tym samouczku będę używał Ledger Nano S z kablem, ale procedura jest podobna w trybie Air-Gap. Szczegóły dotyczące Hardware Wallet znajdziesz w dedykowanym samouczku na temat Plan ₿ Network.


Przed rozpoczęciem upewnij się, że Wallet jest już skonfigurowany na Hardware Wallet. Jeśli korzystasz z połączenia przewodowego, podłącz go do komputera za pomocą kabla.


Aby zaimportować tak zwany "*Keystore*" (informacje publiczne potrzebne do zarządzania Wallet) do Sparrow Wallet, kliknij zakładkę "*File*", a następnie "*New Wallet*".


![Image](assets/fr/32.webp)


Nazwij swój Wallet i kliknij "*Create Wallet*". Radzę wpisać nazwę Hardware Wallet, aby później łatwo go zidentyfikować.


![Image](assets/fr/33.webp)


W górnej części Interface, wybierz pomiędzy "*Single Signature*" lub "*Multi Signature*" Wallet. W naszym przykładzie skonfigurujemy Wallet z pojedynczym podpisem.


Tuż poniżej wybierz typ skryptu do blokowania UTXO. Jeśli twój Hardware Wallet to obsługuje, sugeruję wybrać "*Taproot (P2TR)*".


![Image](assets/fr/34.webp)


Następnie procedura różni się w zależności od metody połączenia. Jeśli używasz metody Air-Gap, wybierz "*Airgapped Hardware Wallet*". Następnie postępuj zgodnie z instrukcjami dotyczącymi Twojego urządzenia.


![Image](assets/fr/35.webp)


Jeśli korzystasz z połączenia kablowego, tak jak w moim przypadku, wybierz "*Podłączony Hardware Wallet*".


![Image](assets/fr/36.webp)


Kliknij "*Scan*", aby aplikacja Sparrow wykryła urządzenie. Upewnij się, że jest ono podłączone i odblokowane. W przypadku niektórych modeli, takich jak Ledger, należy otworzyć aplikację "*Bitcoin*", aby włączyć wykrywanie.


![Image](assets/fr/37.webp)


Wybierz opcję "*Import Keystore*".


![Image](assets/fr/38.webp)


Kliknij "*Zastosuj*", aby sfinalizować tworzenie Wallet.


![Image](assets/fr/39.webp)


Ustaw silne hasło, aby zabezpieczyć dostęp do Sparrow Wallet. Hasło to będzie chronić klucze publiczne, adresy i historię transakcji. Zalecamy zapisanie go w menedżerze haseł. Należy pamiętać, że to hasło nie odgrywa żadnej roli w uzyskiwaniu kluczy. Nawet bez niego można odzyskać dostęp do bitcoinów za pomocą Mnemonic za pośrednictwem dowolnego oprogramowania kompatybilnego z BIP39.


![Image](assets/fr/40.webp)


Zarządzany Wallet jest teraz skonfigurowany w Sparrow.


![Image](assets/fr/41.webp)


## Odbieranie bitcoinów


Teraz, gdy Wallet jest skonfigurowany w Sparrow, możesz otrzymywać bitcoiny. Wystarczy wejść do menu "*Odbierz*".


![Image](assets/fr/42.webp)


Sparrow wyświetli pierwszy nieużywany Address w Wallet. Możesz dodać "*Label*" do tego Address, aby przypomnieć sobie o pochodzeniu tych satoshis w przyszłości.


![Image](assets/fr/43.webp)


Jeśli korzystasz z Hot Wallet, wyświetlony Address może być użyty natychmiast, poprzez skopiowanie go lub zeskanowanie powiązanego kodu QR.


Jeśli używasz Hardware Wallet, bardzo ważne jest sprawdzenie Address na ekranie urządzenia przed jego użyciem. W przypadku urządzeń przewodowych podłącz i odblokuj Hardware Wallet, a następnie w aplikacji Sparrow kliknij "*Wyświetl Address*". Upewnij się, że Address wyświetlany na Hardware Wallet jest zgodny z tym wyświetlanym w Sparrow.


![Image](assets/fr/44.webp)


W przypadku użytkowników Hardware Wallet Air-Gap weryfikacja Address różni się w zależności od modelu urządzenia. Dokładne instrukcje można znaleźć w dedykowanym samouczku Plan ₿ Network.


Gdy transakcja zostanie nadana przez płatnika, pojawi się w zakładce "*Transakcje*". Możesz kliknąć na nią, aby uzyskać więcej szczegółów, takich jak txid.


![Image](assets/fr/45.webp)


W zakładce "*Adresy*" znajduje się lista wszystkich adresów skrzynki odbiorczej. Możesz sprawdzić, czy zostały one już użyte i czy dodano do nich etykietę. *Adresy "Receive*" to te, które Sparrow pokazuje po kliknięciu "*Receive*" i są przeznaczone dla płatności przychodzących. Adresy "*Change*" są używane do Exchange w transakcjach, tj. do odzyskiwania niewykorzystanej części UTXO w wejściach.


![Image](assets/fr/46.webp)


Zakładka "*UTXOs*" pokazuje wszystkie posiadane UTXOs, tj. posiadane fragmenty Bitcoin. Możesz zobaczyć ilość każdego UTXO i powiązaną etykietę.


![Image](assets/fr/47.webp)


## Wysyłanie bitcoinów


Teraz, gdy masz już kilka satoshi w swoim Wallet, masz również możliwość ich wysłania. Chociaż istnieje kilka sposobów na zrobienie tego, zalecam skorzystanie z menu "*UTXOs*", aby uzyskać bardziej precyzyjną kontrolę nad wydawanymi monetami (*coin control*), zamiast przechodzenia bezpośrednio do menu "*Send*" (chociaż to drugie może wystarczyć, jeśli jesteś początkującym graczem).


![Image](assets/fr/48.webp)


Wybierz UTXO, których chcesz użyć jako danych wejściowych dla tej transakcji, a następnie kliknij "*Wyślij wybrane*". Takie podejście pozwala wybrać najbardziej odpowiednie źródła spośród UTXO, zgodnie z wydatkami i etykietami zastosowanymi po ich otrzymaniu, w celu zoptymalizowania poufności płatności. Upewnij się, że suma wybranych UTXO jest większa niż kwota, którą chcesz wysłać.


![Image](assets/fr/49.webp)


Wprowadź numer Address odbiorcy w polu "*Pay to*". Możesz również zeskanować Address za pomocą kamery internetowej, klikając ikonę kamery. Przycisk "*+Add*" umożliwia opłacenie wielu adresów w ramach jednej transakcji.


![Image](assets/fr/50.webp)


Dodaj etykietę do transakcji, aby przypomnieć o jej celu. Etykieta ta będzie również powiązana z ewentualnym Exchange.


![Image](assets/fr/51.webp)


Wprowadź kwotę, która ma zostać wysłana do tego Address.


![Image](assets/fr/52.webp)


Dostosuj stawkę opłaty do aktualnych warunków rynkowych. Można to zrobić, wprowadzając bezwzględną wartość opłaty lub dostosowując stawkę opłaty za pomocą suwaka.


![Image](assets/fr/53.webp)


W dolnej części Interface można wybrać pomiędzy opcjami "*Efficiency*" i "*Privacy*". W moim przypadku opcja "*Prywatność*" nie jest dostępna, ponieważ mam tylko jeden UTXO w tym Wallet. "*Efficiency*" odpowiada klasycznej transakcji, podczas gdy "*Privacy*" to transakcja typu Stonewall, struktura transakcji, która wzmacnia poufność poprzez symulację mini-CoinJoin, co sprawia, że analiza łańcucha jest bardziej złożona.


![Image](assets/fr/54.webp)


Sparrow wyświetla diagram podsumowujący pokazujący dane wejściowe, wyjściowe i opłaty transakcyjne (należy pamiętać, że opłaty nie są w rzeczywistości wynikiem, w przeciwieństwie do tego, co sugeruje ten diagram). Jeśli wszystko ci odpowiada, kliknij "*Twórz transakcję*".


![Image](assets/fr/55.webp)


Spowoduje to przejście do strony zawierającej szczegóły transakcji Elements. Sprawdź, czy wszystkie informacje są poprawne, a następnie kliknij "*Finalizuj transakcję do podpisania*".


![Image](assets/fr/56.webp)


Ważne jest, aby zachować domyślny Sighash. Aby zrozumieć dlaczego, zapoznaj się z tym szkoleniem, w którym wyjaśniam wszystko, co musisz wiedzieć o Sighash:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
Na następnym ekranie opcje różnią się w zależności od używanego typu Wallet:




- W przypadku Hardware Wallet Air-Gap kliknij "*Pokaż QR*", aby wyświetlić PSBT, który możesz podpisać swoim urządzeniem, a następnie załaduj podpisany PSBT do Sparrow za pomocą "*Skanuj QR*". Opcja "*Zapisz transakcję*" działa w podobny sposób, ale z wymianami na karcie microSD;
- W przypadku Hot Wallet wystarczy kliknąć "*Podpisz*" i wprowadzić hasło Wallet, aby podpisać;
- W przypadku przewodowego Hardware Wallet należy również kliknąć "*Podpisz*", aby wysłać niepodpisaną transakcję do urządzenia.


![Image](assets/fr/57.webp)


Na swoim Hardware Wallet sprawdź Address odbiorcy, wysłaną kwotę i opłaty. Jeśli wszystko się zgadza, przejdź do podpisu.


Po podpisaniu transakcji pojawi się ona ponownie w Sparrow, gotowa do transmisji w sieci Bitcoin w celu późniejszego włączenia do bloku. Jeśli wszystko jest w porządku, kliknij "*Broadcast Transaction*".


![Image](assets/fr/58.webp)


Twoja transakcja jest teraz transmitowana i oczekuje na potwierdzenie.


![Image](assets/fr/59.webp)


![video](https://youtu.be/7QCKSPIq0Ac)


## Zarządzanie i konfiguracja portfeli w Sparrow


W zakładce "*Ustawienia*" znajdują się szczegółowe informacje na temat urządzenia Wallet, takie jak :



- Typ portfela (single-sig lub multi-sig) ;
- Typ używanego skryptu ;
- Nazwa przypisana do urządzenia Wallet;
- Nadruk klucza głównego;
- Ścieżka obejścia;
- Rozszerzony klucz publiczny konta.


![Image](assets/fr/60.webp)


Przycisk "*Export*" umożliwia wyeksportowanie informacji Wallet, aby można było ich używać w innym oprogramowaniu, zachowując informacje skonfigurowane w aplikacji Sparrow.


Przycisk "*Dodaj konto*" umożliwia dodanie dodatkowego konta do Wallet. Konto odpowiada oddzielnemu zestawowi adresów skrzynki odbiorczej. Ta funkcja może być przydatna, na przykład, jeśli chcesz oddzielić konto osobiste i firmowe, za pomocą jednej frazy Mnemonic.


Przycisk "*Zaawansowane*" daje dostęp do zaawansowanych ustawień, takich jak dostosowanie wyszukiwania Address Sparrow i zmiana hasła Wallet.


![Image](assets/fr/61.webp)


Po zamknięciu Sparrow Wallet, Wallet zablokuje się automatycznie. Przy następnym otwarciu oprogramowania pojawi się okno z prośbą o odblokowanie Wallet za pomocą hasła.


![Image](assets/fr/62.webp)


Jeśli to okno się nie otworzy lub jeśli chcesz otworzyć inny Wallet w Sparrow, kliknij zakładkę "*File*" i wybierz "*Open Wallet*".


![Image](assets/fr/63.webp)


Spowoduje to otwarcie menedżera plików w folderze, w którym Sparrow przechowuje portfele. Po prostu wybierz Wallet, który chcesz otworzyć i wprowadź hasło, aby go odblokować.


![Image](assets/fr/64.webp)


W menu "*File*" w sekcji "*Settings*" znajdują się parametry połączenia sieciowego Bitcoin, które zostały już omówione w poprzednich sekcjach. Można również dostosować różne parametry, takie jak używana jednostka, waluta fiducjarna do konwersji i źródła informacji.


![Image](assets/fr/65.webp)


Zakładka "*View*" oferuje opcje dostosowywania i dostęp do kilku przydatnych poleceń, takich jak "*Refresh Wallet*", które odświeża wyszukiwanie transakcji dla Wallet.


![Image](assets/fr/66.webp)


Zakładka "*Narzędzia*" grupuje kilka zaawansowanych narzędzi, w tym :



- "*Podpisz/Weryfikuj wiadomość*" pozwala udowodnić posiadanie otrzymanego Address lub zweryfikować podpis.
- "*Send To Many*" oferuje uproszczony Interface do wykonywania transakcji na wiele adresów odbiorczych jednocześnie, co jest wygodne w przypadku wydatków wsadowych.
- "*Sweep Private Key*" pozwala odzyskać bitcoiny zabezpieczone prostym kluczem prywatnym i przenieść je do Sparrow Wallet. Może to być szczególnie przydatne dla osób posiadających bitcoiny z początku 2010 roku, przed erą portfeli HD.
- "Verify Download" weryfikuje integralność i autentyczność pobranego oprogramowania przed zainstalowaniem go na urządzeniu.
- "*Restart In*" pozwala przełączyć się na portfele w sieciach Testnet lub Signet. Może to być przydatne, jeśli chcesz uzyskać dostęp do sieci testowych z monetami bez rzeczywistej wartości.


![Image](assets/fr/67.webp)


Wiesz już wszystko o oprogramowaniu Sparrow Wallet, doskonałym narzędziu do codziennego zarządzania portfelami Bitcoin.


Jeśli uznałeś ten poradnik za przydatny, będę bardzo wdzięczny, jeśli zostawisz poniżej kciuk Green. Zapraszam do udostępnienia go w sieciach społecznościowych. Dziękuję bardzo!


Polecam również ten samouczek, w którym wyjaśniam, jak skonfigurować Hardware Wallet COLDCARD Q ze Sparrow Wallet :


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3