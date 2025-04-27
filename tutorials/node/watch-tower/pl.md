---
name: Watch Tower
description: Zrozumienie i używanie Watch Tower
---

## Jak działają wieże strażnicze?


Wieże strażnicze, będące istotną częścią ekosystemu Lightning Network, zapewniają dodatkowy stopień ochrony kanałom piorunowym użytkowników. Ich głównym zadaniem jest monitorowanie stanu kanałów i interweniowanie, gdy jedna ze stron kanału próbuje oszukać drugą.


Jak więc Watchtower może określić, czy kanał został naruszony? Watchtower otrzymuje potrzebne informacje od klienta, jednej ze stron kanału, w celu prawidłowej identyfikacji i reagowania na wszelkie naruszenia. Najnowsze szczegóły transakcji, aktualny stan kanału i informacje wymagane do utworzenia transakcji karnych są często zawarte w tych informacjach. Przed przesłaniem danych do Watchtower, klient może je zaszyfrować w celu ochrony prywatności i poufności. Zapobiega to odszyfrowaniu zaszyfrowanych danych przez Watchtower, chyba że rzeczywiście doszło do naruszenia, nawet jeśli otrzyma on dane. Prywatność klienta jest chroniona przez ten system szyfrowania, który również uniemożliwia Watchtower dostęp do prywatnych danych bez autoryzacji.


## Jak założyć własne Eye of Satoshi i zacząć wnosić swój wkład?


The Eye of Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos?ref=blog.summerofbitcoin.org)) to bezobsługowa Błyskawica Watchtower zgodna z [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Ma dwa główne komponenty:


1. teos: zawiera CLI i podstawową funkcjonalność wieży po stronie serwera. Dwa pliki binarne - teosd i teos-CLI - zostaną utworzone po zbudowaniu tej skrzynki.

2. teos-common: Zawiera współdzielone funkcje po stronie serwera i klienta (pomocne przy tworzeniu klienta).


Aby pomyślnie uruchomić wieżę, należy uruchomić bitcoind przed uruchomieniem wieży za pomocą polecenia teosd. Przed uruchomieniem obu tych poleceń należy skonfigurować plik Bitcoin.conf. Oto kroki, jak to zrobić:-


1. Zainstaluj Bitcoin core ze źródła lub pobierz go. Po pobraniu umieść plik Bitcoin.conf w katalogu użytkownika Bitcoin core. Sprawdź ten link, aby uzyskać więcej informacji na temat tego, gdzie umieścić plik, ponieważ zależy to od używanego systemu operacyjnego.

2. Po określeniu miejsca, w którym plik ma zostać utworzony, dodaj następujące opcje:-


```
#RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

#chain
regtest=1```

- server: For RPC requests
- rpcuser and rpcpassword: RPC clients can authenticate with the server
- regtest: Not required but useful if you're planning for development.

rpcuser and rpcpassword need to be picked by you. They must be written without quotes. Eg:-

```

rpcuser=aniketh

rpcpassword=strongpassword```


Teraz, jeśli uruchomisz bitcoind, powinien on rozpocząć uruchamianie węzła.


1. Jeśli chodzi o część wieżową, najpierw musisz zainstalować teos ze źródła. Postępuj zgodnie z instrukcjami podanymi w tym linku.

2. Po pomyślnym zainstalowaniu teos w systemie i uruchomieniu testów, możesz przejść do ostatniego kroku, którym jest skonfigurowanie pliku teos.toml w katalogu użytkownika teos. Plik musi być umieszczony w folderze o nazwie .teos (pamiętaj o kropce) w folderze domowym. Jest to na przykład /home/<twoja-nazwa-użytkownika>/.teos dla Linuksa. Po znalezieniu miejsca, utwórz plik teos.toml i ustaw opcje odpowiadające rzeczom, które zmieniliśmy w bitcoind.


```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>```

Notice that here the username and password need to be written quoted, that is, for the same example as before:

```

btc_rpc_user = "aniketh"

btc_rpc_password = "strongpassword"```


Gdy to zrobisz, powinieneś być gotowy do uruchomienia wieży. Biorąc pod uwagę, że działamy na regtest, prawdopodobnie nie będzie żadnych bloków wydobytych w naszej sieci testowej Bitcoin przy pierwszym połączeniu wieży z nią (jeśli są, coś z pewnością jest nie tak). Wieża buduje wewnętrzną pamięć podręczną ostatnich 100 bloków z bitcoind, więc przy pierwszym uruchomieniu możemy otrzymać następujący błąd:


_ERROR [teosd] Za mało bloków, aby uruchomić wieżę (wymagane: 100). Wydobądź co najmniej 100 więcej_


Biorąc pod uwagę, że działamy na regtest, możemy wydobywać bloki, wydając polecenie RPC, bez konieczności czekania na 10-minutowy czas mediany, który zwykle widzimy w innych sieciach (takich jak Mainnet lub Testnet). Sprawdź pomoc bitcoin-cli i dowiedz się, jak wydobywać bloki. Jeśli potrzebujesz pomocy, możesz przejrzeć ten artykuł.


![image](assets/2.webp)


To wszystko, udało ci się uruchomić wieżę. Gratulacje. 🎉