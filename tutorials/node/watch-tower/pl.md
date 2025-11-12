---
name: Lightning Watchtower
description: Zrozumienie i używanie Watchtower na węźle Lightning
---
![cover](assets/cover.webp)



## Jak działają wieże strażnicze?



Istotna część ekosystemu Lightning Network, _Watchtowers_ zapewniają dodatkowy poziom ochrony kanałów Lightning użytkowników. Ich główną rolą jest monitorowanie statusu kanału i interweniowanie, jeśli jedna strona kanału próbuje oszukać drugą.



W jaki sposób Watchtower może ustalić, czy kanał został naruszony? Otrzymuje od klienta (jednej ze stron kanału) informacje potrzebne do prawidłowej identyfikacji i postępowania w przypadku naruszenia. Informacje te obejmują szczegóły ostatniej transakcji, aktualny status kanału i Elements wymagany do utworzenia transakcji karnych. Przed przesłaniem tych danych do Watchtower klient może je zaszyfrować w celu zachowania poufności. Tak więc, nawet jeśli Watchtower otrzyma dane, nie będzie w stanie ich odszyfrować, dopóki nie dojdzie do naruszenia. Ten mechanizm szyfrowania chroni prywatność klienta i uniemożliwia Watchtower uzyskanie nieautoryzowanego dostępu do poufnych informacji.



W tym poradniku przyjrzymy się 3 sposobom korzystania z **Watchtower** :




- po pierwsze, klasyczna metoda surowa za pośrednictwem LND,
- następnie kolejne podejście z Eye of Satoshi,
- i wreszcie uproszczona konfiguracja Watchtower na węźle Lightning hostowanym przez Umbrel.



## 1 - Konfiguracja Watchtower lub klienta przez LND



*Ten samouczek pochodzi z [oficjalnej dokumentacji LND] (https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Niektóre zmiany mogły zostać wprowadzone do oryginalnej wersji



Od wersji 0.7.0, `LND` obsługuje wykonywanie prywatnego altruistycznego Watchtower jako w pełni zintegrowanego podsystemu `LND`. Wieże strażnicze zapewniają drugą linię obrony przed złośliwymi lub przypadkowymi scenariuszami naruszenia, gdy węzeł klienta jest w trybie offline lub nie jest w stanie odpowiedzieć w momencie naruszenia, oferując zwiększony stopień bezpieczeństwa funduszy kanału.



W przeciwieństwie do _reward watchtower_, która żąda części funduszy kanału w zamian za swoją usługę, _altruist watchtower_ zwraca wszystkie fundusze ofiary (minus opłaty On-Chain) bez pobierania prowizji. Wieże strażnicze z nagrodami zostaną aktywowane w późniejszej wersji; są one nadal w fazie testów i ulepszeń.



Dodatkowo, `LND` można teraz skonfigurować tak, aby działał jako _klient_ wieży strażniczej, zapisując zaszyfrowane transakcje naprawy naruszeń (tak zwane "transakcje sprawiedliwości") z innych altruistycznych wież strażniczych. Watchtower przechowuje zaszyfrowane bloby o stałym rozmiarze i może odszyfrować i opublikować transakcję sprawiedliwości dopiero po tym, jak strona naruszająca rozgłosi odwołany stan Commitment. Komunikacja klient ↔ Watchtower jest szyfrowana i uwierzytelniana przy użyciu efemerycznych par kluczy, co ogranicza zdolność Watchtower do śledzenia swoich klientów za pomocą długoterminowych danych uwierzytelniających.



Należy pamiętać, że zdecydowaliśmy się wdrożyć w tym wydaniu ograniczony zestaw funkcji, które już zapewniają znaczne bezpieczeństwo użytkownikom `LND`. Wiele innych funkcji związanych z Watchtower jest bliskich ukończenia lub zaawansowanych; będziemy je nadal dostarczać w miarę ich testowania i gdy tylko zostaną uznane za bezpieczne.



uwaga: na razie watchtowers zapisują tylko dane wyjściowe `to_local` i `to_remote` odwołanych zobowiązań; zapisywanie danych wyjściowych HTLC zostanie wdrożone w przyszłej wersji, ponieważ protokół może zostać rozszerzony o dodatkowe dane podpisu w zaszyfrowanych blobach



### Konfiguracja Watchtower



Aby skonfigurować Watchtower, użytkownicy wiersza poleceń muszą skompilować opcjonalny podserwer `watchtowerrpc`, który pozwala na interakcję z Watchtower poprzez gRPC lub `lncli`. Opublikowane binaria domyślnie zawierają pod-serwer `watchtowerrpc`.



Minimalna konfiguracja do aktywacji Watchtower to `Watchtower.active=1`.



Informacje o konfiguracji Watchtower można pobrać za pomocą `lncli tower info` :



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



Pełny zestaw opcji konfiguracyjnych Watchtower jest dostępny poprzez `LND -h` :



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Interfejsy odsłuchowe



Domyślnie Watchtower nasłuchuje na `:9911`, co odpowiada portowi `9911` na wszystkich dostępnych interfejsach. Użytkownicy mogą zdefiniować własne interfejsy nasłuchujące poprzez opcję `--Watchtower.listen=`. Konfigurację można sprawdzić w polu `"listeners"` programu `lncli tower info`. Jeśli masz problemy z połączeniem się z Watchtower, upewnij się, że `<port>` jest otwarty lub że proxy jest poprawnie skonfigurowane do aktywnego Interface.



#### Zewnętrzne adresy IP



Użytkownicy mogą również określić zewnętrzny adres IP Watchtower za pomocą `Watchtower.externalip=`, który ujawnia pełny URI Watchtower (pubkey@host:port) poprzez RPC lub `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Identyfikatory URI Watchtower mogą być przekazywane klientom w celu połączenia i użycia za pomocą następującego polecenia:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Jeśli klienci Watchtower potrzebują zdalnego dostępu do niego, upewnij się, że :




- Otwórz port 9911 (lub port zdefiniowany przez `Watchtower.listen`).
- Użyj proxy, aby przekierować ruch z otwartego portu do nasłuchującego Address Watchtower.



#### Ukryte usługi Tor



Watchtowers obsługuje ukryte usługi Tor i może automatycznie generate jedną z nich podczas uruchamiania z następującymi opcjami:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



Następnie .onion Address pojawia się w polu `"uris"` podczas zapytania `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



uwaga: klucz publiczny Watchtower różni się od klucza publicznego węzła `LND`. Na razie działa on jako "biała lista Soft", ponieważ klienci muszą znać klucz publiczny Watchtower, aby używać go jako kopii zapasowej, w oczekiwaniu na bardziej zaawansowane mechanizmy białej listy. Zalecamy, aby NIE ujawniać tego klucza publicznego otwarcie, chyba że jesteś przygotowany na ujawnienie swojego Watchtower całemu Internetowi



#### Katalog bazy danych Watchtower



Baza danych Watchtower może zostać przeniesiona przy użyciu opcji `Watchtower.towerdir=`. Należy pamiętać, że do wybranej ścieżki zostanie dodany sufiks `/Bitcoin/Mainnet/Watchtower.db` w celu odizolowania baz danych według łańcucha. Tak więc ustawienie `Watchtower.towerdir=/path/to/towerdir` spowoduje utworzenie bazy danych w `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



Na przykład w systemie Linux domyślna baza danych Watchtower znajduje się pod adresem :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Konfiguracja klienta Watchtower



Do skonfigurowania klienta Watchtower potrzebne są dwa elementy:





- Aktywuj klienta Watchtower za pomocą opcji `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- Identyfikator URI aktywnego Watchtower.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



W ten sposób można skonfigurować kilka wież strażniczych.



#### Stawki opłat za czynności prawne



Użytkownicy mogą opcjonalnie ustawić stawkę opłaty za transakcje sprawiedliwości za pomocą opcji `wtclient.sweep-fee-rate`, która akceptuje wartości w sat/bajt. Domyślną wartością jest 10 sat/bajt, ale można dążyć do wyższych stawek, aby osiągnąć wyższy priorytet podczas szczytowych obciążeń. Zmiana `sweep-fee-rate` dotyczy wszystkich nowych aktualizacji po restarcie daemon.



#### Nadzór



Dzięki poleceniu `lncli wtclient` użytkownicy mogą teraz wchodzić w interakcje bezpośrednio z klientem Watchtower, aby uzyskać lub zmodyfikować informacje o wszystkich zarejestrowanych wieżach strażniczych.



Na przykład, za pomocą `lncli wtclient tower` można sprawdzić liczbę sesji aktualnie negocjowanych z Watchtower dodanym powyżej i określić, czy jest on używany do tworzenia kopii zapasowych dzięki polu `active_session_candidate`.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Aby uzyskać informacje o sesjach Watchtower, należy użyć opcji `--include_sessions`.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Wszystkie opcje konfiguracji klienta Watchtower są dostępne poprzez `lncli wtclient -h` :



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Instalacja własnego oka Satoshi



*Ten poradnik został częściowo zaczerpnięty z artykułu na blogu [Summer of Bitcoin Blog](https://blog.summerofbitcoin.org/). Wprowadzono modyfikacje do oryginalnej wersji*



Oko Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) jest nie-depozytowym Watchtower Lightning, zgodnym z [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Składa się z dwóch głównych komponentów:





- teos**: zawiera wiersz poleceń Interface (CLI) i podstawowe funkcje serwera Watchtower. Podczas kompilacji tego _crate_ tworzone są dwa pliki binarne - **teosd** i **teos-CLI**.





- teos-common**: zawiera współdzielone funkcje po stronie serwera i klienta (przydatne przy tworzeniu klienta).



Aby poprawnie uruchomić Watchtower, należy uruchomić **bitcoind** przed uruchomieniem Watchtower za pomocą komendy **teosd**. Przed uruchomieniem tych dwóch poleceń, należy skonfigurować plik **Bitcoin.conf**. Oto jak to zrobić:





- Zainstaluj Bitcoin core ze źródła lub pobierz go. Po pobraniu, umieść plik **Bitcoin.conf** w katalogu użytkownika Bitcoin core. Więcej informacji na temat miejsca umieszczenia pliku można znaleźć pod tym linkiem, ponieważ zależy to od używanego systemu operacyjnego.





- Po zidentyfikowaniu lokalizacji dodaj następujące opcje:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- serwer**: dla żądań RPC





- rpcuser** i **rpcpassword**: uwierzytelniają klientów RPC na serwerze





- regtest**: nie jest wymagany, ale przydatny, jeśli planujesz rozwój.



Wartości **rpcuser** i **rpcpassword** są wybierane przez użytkownika. Muszą być zapisane bez cudzysłowów. Na przykład:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Teraz, jeśli uruchomisz **bitcoind**, węzeł powinien się uruchomić.





- W przypadku części Watchtower należy najpierw zainstalować **teos** ze źródła. Postępuj zgodnie z instrukcjami podanymi w tym linku.





- Po pomyślnym zainstalowaniu **teos** w systemie i uruchomieniu testów, możesz przejść do ostatniego kroku: skonfigurowania pliku **teos.toml** w katalogu użytkownika teos. Plik powinien być umieszczony w folderze o nazwie **.teos** (uwaga na kropkę) w katalogu domowym. Na przykład **/home//.teos** w systemie Linux. Po znalezieniu lokalizacji należy utworzyć plik **teos.toml** i ustawić opcje zgodnie ze zmianami wprowadzonymi w **bitcoind** :



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Należy pamiętać, że tutaj nazwa użytkownika i hasło muszą być zapisane **w cudzysłowie**. Używając poprzedniego przykładu :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Gdy to zrobisz, powinieneś być gotowy do uruchomienia Watchtower. Ponieważ działamy na **regtest**, prawdopodobnie żadne bloki nie były wydobywane w naszej sieci testowej Bitcoin podczas pierwszego połączenia Watchtower (jeśli były, coś jest nie tak). Watchtower buduje wewnętrzną pamięć podręczną ostatnich 100 bloków **bitcoind**; więc przy pierwszym uruchomieniu może pojawić się następujący błąd:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Ponieważ używamy **regtest**, możemy Miner bloków wydając komendę RPC, bez konieczności czekania na średnie 10-minutowe opóźnienie widoczne w innych sieciach (takich jak Mainnet lub Testnet). Zobacz pomoc **bitcoin-cli**, aby uzyskać szczegółowe informacje na temat bloków Miner.



![Image](assets/fr/01.webp)



To wszystko: pomyślnie uruchomiłeś Watchtower. Gratulacje. 🎉




## 3 - Konfiguracja Watchtower na Umbrel



W Umbrel połączenie z Watchtower w celu ochrony węzła Lightning jest niezwykle proste, ponieważ wszystko odbywa się za pośrednictwem graficznego Interface. Po zdalnym połączeniu się z węzłem, otwórz aplikację "**Lightning Node**".



![Image](assets/fr/02.webp)



Kliknij trzy małe kropki w prawym górnym rogu Interface, a następnie wybierz "**Ustawienia zaawansowane**".



![Image](assets/fr/03.webp)



W menu "**Watchtower**" dostępne są dwie opcje:





- Usługa Watchtower**: ta opcja umożliwia obsługę Watchtower, tj. usługi, która monitoruje kanały innych węzłów w celu wykrycia wszelkich prób oszustwa. W przypadku naruszenia Watchtower publikuje transakcję na Blockchain, umożliwiając użytkownikom odzyskanie zablokowanych środków. Po aktywacji pojawia się identyfikator URI Watchtower i można go przekazać innym węzłom, aby mogły dodać go do swojego klienta Watchtower;





- Klient Watchtower**: ta opcja umożliwia łączenie się z zewnętrznymi wieżami strażniczymi w celu ochrony własnych kanałów. Po aktywacji można dodać usługi Watchtower, do których węzeł będzie przekazywał niezbędne informacje o swoich kanałach. Te wieże strażnicze będą następnie monitorować ich status i interweniować w przypadku próby oszustwa.



Priorytetem jest oczywiście aktywacja *Watchtower Client*, aby chronić swój węzeł, ale zalecam również aktywację *Watchtower Service*, aby w zamian przyczynić się do bezpieczeństwa innych użytkowników.



![Image](assets/fr/04.webp)



Następnie kliknij przycisk Green "**Zapisz i uruchom ponownie węzeł**". LND uruchomi się ponownie.



W tym samym menu znajduje się również URI usługi Watchtower, jeśli została ona aktywowana. Możesz również dodać URI zewnętrznego Watchtower, aby chronić swoje kanały. Kliknij "**ADD**", aby potwierdzić.



![Image](assets/fr/05.webp)



Istnieje kilka wież strażniczych dostępnych online. Na przykład [LN+ i Voltage oferują altruistyczne Watchtower](https://lightningnetwork.plus/Watchtower), z którymi można się połączyć:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Inną opcją jest Exchange URI Watchtower z innymi bitcoinerami, tak aby każdy chronił węzeł drugiego.



Zalecam również skonfigurowanie kilku wież strażniczych, aby zmniejszyć ryzyko w przypadku, gdy jedna z nich stanie się niedostępna.



Na koniec można dostosować parametr "**Watchtower Client Sweep Fee Rate**". Określa on maksymalną stawkę opłaty, jaką jesteś skłonny zapłacić za transakcję kary transmisji Watchtower, która ma zostać uwzględniona w bloku. Upewnij się, że ustawiłeś wystarczająco wysoką wartość, dostosowaną do kwot zablokowanych w Twoich kanałach.