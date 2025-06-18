---
name: RGB Lightning Node
description: Jak uruchomić węzeł Lightning kompatybilny z RGB za pomocą RLN?
---
![cover](assets/cover.webp)


W tym samouczku krok po kroku dowiesz się, jak skonfigurować węzeł Lightning RGB w środowisku Regtest. Zobaczymy, jak tworzyć tokeny RGB i rozpowszechniać je w kanałach.


## Projekt RLN


Zespół RGB Bitfinex pracuje od 2022 roku nad wzbogaceniem ekosystemu RGB poprzez opracowanie kompletnego stosu technologicznego. Zamiast dążyć do stworzenia pojedynczego produktu komercyjnego, jego wysiłki koncentrują się na udostępnianiu cegiełek oprogramowania typu open source, przyczynianiu się do specyfikacji protokołu RGB i tworzeniu referencji wdrożeniowych.


Wśród znaczących wkładów Bitfinex w ekosystem RGB jest [biblioteka *RGBlib*](https://github.com/RGB-Tools/RGB-lib), napisana w Rust i dostępna za pośrednictwem powiązań w Kotlin i Python, która znacznie upraszcza tworzenie aplikacji RGB poprzez hermetyzację złożonych mechanizmów walidacji i zaangażowania.


Zespół Bitfinex zaprojektował również RGB mobilny Wallet, zwany "[*Iris Wallet*](https://iriswallet.com/)", dostępny na Androida. Ten Wallet integruje wykorzystanie serwera proxy RGB do łatwego zarządzania wymianą danych off-chain (*consignments*) dla *Client-side Validation* na RGB.


Bitfinex opracował również projekt `RGB-lightning-node` (RLN). Jest to Rust daemon oparty na Fork `Rust-lightning` (LDK), zmodyfikowany w celu uwzględnienia istnienia aktywów RGB w kanale. Po otwarciu kanału można określić obecność tokenów RGB, a za każdym razem, gdy stan kanału jest aktualizowany, tworzony jest State Transition, który odzwierciedla dystrybucję tokenów w wyjściach Lightning. Umożliwia to :




- Na przykład otwarte kanały Lightning w USDT;
- Przekierować te tokeny przez sieć, pod warunkiem, że ścieżki routingu mają wystarczającą płynność;
- Wykorzystaj logikę kary i blokady czasowej Lightning bez modyfikacji: po prostu Anchor przejście RGB w dodatkowym wyjściu Commitment Transaction.


Kod RLN jest wciąż w fazie alfa: zalecamy używanie go wyłącznie w **regtest** lub na **Testnet**.


## Przypomnienie o protokole RGB


RGB to protokół, który działa na szczycie Bitcoin i emuluje funkcjonalność Smart contract oraz zarządzanie zasobami cyfrowymi, bez przeciążania Blockchain, na którym jest oparty. W przeciwieństwie do konwencjonalnych inteligentnych kontraktów On-Chain (jak na przykład na Ethereum), RGB opiera się na systemie "*Client-side Validation*": większość danych i historii statusu jest wymieniana i przechowywana wyłącznie przez zaangażowanych uczestników, podczas gdy Bitcoin Blockchain obsługuje tylko niewielkie zobowiązania kryptograficzne (za pośrednictwem mechanizmów takich jak *Tapret* lub *Opret*). W protokole RGB Bitcoin Blockchain służy zatem jedynie jako serwer znaczników czasu i system ochrony Double-spending.


RGB Contract ma strukturę ewolucyjnej maszyny stanów. Zaczyna się od Genesis, który definiuje stan początkowy (opisujący na przykład Supply, ticker lub inne metadane) zgodnie ze ściśle wpisanym i skompilowanym Schema. Przejścia stanu i, w razie potrzeby, rozszerzenia stanu są następnie stosowane w celu modyfikacji lub rozszerzenia tego stanu. Każda operacja, niezależnie od tego, czy przenosi aktywa zamienne (RGB20), czy tworzy unikalne aktywa (RGB21), obejmuje *Single-use Seals*. Łączą one Bitcoin UTXO ze stanami off-chain i zapobiegają podwójnym wydatkom, zapewniając jednocześnie poufność i skalowalność.


Aby dowiedzieć się więcej na temat działania protokołu RGB, polecam udział w tym kompleksowym szkoleniu:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## Instalacja węzła Lightning zgodnego z RGB


Aby skompilować i zainstalować binarkę `RGB-lightning-node`, zaczynamy od sklonowania repozytorium i jego submodułów, a następnie uruchamiamy :


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- Opcja `--recurse-submodules` również klonuje niezbędne urządzenia podrzędne (włączając w to zmodyfikowaną wersję `Rust-lightning`);
- Opcja `--shallow-submodules` ogranicza głębokość klonu, aby przyspieszyć pobieranie, jednocześnie zapewniając dostęp do istotnych commitów.


Z katalogu głównego projektu uruchom następujące polecenie, aby skompilować i zainstalować plik binarny :


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--locked` zapewnia, że wersja zależności jest przestrzegana;
- `--debug` nie jest obowiązkowe, ale może pomóc ci się skupić (możesz użyć `--release` jeśli wolisz);
- `--path .` mówi `cargo install`, aby zainstalować z bieżącego katalogu.


Po zakończeniu tego polecenia, plik wykonywalny `RGB-lightning-node` będzie dostępny w katalogu `$CARGO_HOME/bin/`. Upewnij się, że ta ścieżka znajduje się w `$PATH`, abyś mógł wywołać polecenie z dowolnego katalogu.


## Wymagania wstępne


Aby działać, `RGB-lightning-node` daemon potrzebuje obecności i konfiguracji :




- Węzeł `bitcoind`**


Każda instancja RLN będzie musiała komunikować się z `bitcoind`, aby transmitować i monitorować transakcje On-Chain. Uwierzytelnianie (login/hasło) i adres URL (host/port) będą musiały być dostarczone do daemon.




- Indeksator** (Electrum lub Esplora)


daemon musi być w stanie wyświetlać i eksplorować transakcje On-Chain, w szczególności w celu znalezienia UTXO, na którym zakotwiczono aktywa. Konieczne będzie podanie adresu URL serwera Electrum lub Esplora.




- Serwer proxy RGB**


Serwer proxy jest komponentem (opcjonalnym, ale wysoce zalecanym) upraszczającym przesyłanie Exchange z RGB *przesyłek* między urządzeniami równorzędnymi Lightning. Ponownie należy określić adres URL.


Identyfikatory i adresy URL są wprowadzane po *odblokowaniu* daemon za pośrednictwem interfejsu API.


## Uruchomienie Regtestu


Do prostego użytku służy skrypt `regtest.sh`, który automatycznie uruchamia, za pośrednictwem Dockera, zestaw usług: `bitcoind`, `electrs` (indeksator), `RGB-proxy-server`.


![RLN](assets/fr/03.webp)


Pozwala to na uruchomienie lokalnego, izolowanego, wstępnie skonfigurowanego środowiska. Tworzy i niszczy kontenery i katalogi danych przy każdym ponownym uruchomieniu. Zaczniemy od uruchomienia środowiska :


```bash
./regtest.sh start
```


Ten skrypt będzie :




- Utwórz katalog `docker/` do przechowywania ;
- Uruchom `bitcoind` w regtest, jak również indeksator `electrs` i `RGB-proxy-server`;
- Poczekaj, aż wszystko będzie gotowe do użycia.


![RLN](assets/fr/04.webp)


Następnie uruchomimy kilka węzłów RLN. W oddzielnych powłokach uruchom na przykład (aby uruchomić 3 węzły RLN) :


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RLN](assets/fr/05.webp)




- Parametr `--network regtest` wskazuje na użycie konfiguracji regtest;
- `--daemon-listening-port` wskazuje, na którym porcie REST węzeł Lightning będzie nasłuchiwał wywołań API (JSON);
- `--ldk-peer-listening-port` określa, na którym porcie Lightning P2P ma nasłuchiwać;
- `dataldk0/`, `dataldk1/` to ścieżki do katalogów przechowywania (każdy węzeł przechowuje swoje informacje oddzielnie).


Dzięki API można teraz wykonywać polecenia na węzłach RLN z poziomu przeglądarki. W szczególności jest to miejsce, w którym można *odblokować* demony. Wystarczy otworzyć przeglądarkę na tym samym komputerze co węzły i wpisać adres URL :


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


Aby węzeł mógł otworzyć kanał, musi najpierw posiadać bitcoiny na Address wygenerowane za pomocą następującego polecenia (na przykład dla węzła nr 1):


```bash
curl -X POST http://localhost:3001/address
```


W odpowiedzi otrzymasz Address.


![RLN](assets/fr/06.webp)


Na `bitcoind` Regtest, będziemy wydobywać kilka bitcoinów. Uruchom :


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


Wyślij środki do węzła Address wygenerowanego powyżej:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


Następnie wydobądź blok, aby potwierdzić transakcję:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## Uruchomienie Testnet (bez Dockera)


Jeśli chcesz przetestować bardziej realistyczny scenariusz, możesz uruchomić węzły RLN na Testnet zamiast w Regtest, wskazując usługi publiczne lub usługi, które kontrolujesz:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


Domyślnie, jeśli nie zostanie znaleziona żadna konfiguracja, daemon spróbuje użyć pliku :




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


Z loginem :




- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`


Można również dostosować te Elements poprzez API `init`/`unlock`.


## Wydawanie tokena RGB


Aby wydać token, zaczniemy od stworzenia "kolorowych" UTXO:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RLN](assets/fr/10.webp)


Można oczywiście dostosować zamówienie. Aby potwierdzić transakcję, wydobywamy plik :


```bash
./regtest.sh mine 1
```


Możemy teraz utworzyć zasób RGB. Polecenie będzie zależeć od typu zasobu, który chcemy utworzyć i jego parametrów. Tutaj tworzę token NIA (*Non Inflatable Asset*) o nazwie "PBN" z Supply wynoszącym 1000 jednostek. Parametr `precision` pozwala zdefiniować podzielność jednostek.


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RLN](assets/fr/11.webp)


Odpowiedź zawiera identyfikator nowo utworzonego zasobu. Pamiętaj, aby zanotować ten identyfikator. W moim przypadku jest to :


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


Następnie można przesłać On-Chain lub przydzielić go do kanału Lightning. Dokładnie to zrobimy w następnej sekcji.


## Otwieranie kanału i przesyłanie zasobu RGB


Najpierw należy połączyć węzeł z urządzeniem równorzędnym na Lightning Network za pomocą polecenia `/connectpeer`. W moim przykładzie kontroluję oba węzły. Za pomocą tego polecenia odzyskam klucz publiczny mojego drugiego węzła Lightning:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


Polecenie zwraca klucz publiczny mojego węzła n°2:


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


Następnie otworzymy kanał, określając odpowiedni zasób (`PBN`). Polecenie `/openchannel` pozwala zdefiniować rozmiar kanału w satoshis i zdecydować się na dołączenie zasobu RGB. Zależy to od tego, co chcesz utworzyć, ale w moim przypadku polecenie to :


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


Więcej informacji można znaleźć tutaj:




- `peer_pubkey_and_opt_addr`: Identyfikator peera, z którym chcemy się połączyć (klucz publiczny, który znaleźliśmy wcześniej);
- `capacity_sat`: Całkowita pojemność kanału w sat;
- `push_msat`: Kwota w milisatoshis początkowo przesłana do peera, gdy kanał jest otwarty (tutaj natychmiast przesyłam 10 000 Sats, aby mógł później dokonać przelewu RGB);
- `asset_amount`: Kwota aktywów RGB, która ma zostać przekazana do kanału;
- `asset_id`: Unikalny identyfikator zasobu RGB zaangażowanego w kanał;
- `public`: Wskazuje, czy kanał powinien być publiczny dla routingu w sieci.


![RLN](assets/fr/14.webp)


Aby potwierdzić transakcję, wydobywanych jest 6 bloków:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


Kanał Lightning jest teraz otwarty i zawiera również 500 tokenów `PBN` po stronie węzła n°1. Jeśli węzeł n°2 chce otrzymać tokeny `PBN`, musi wykonać generate i Invoice. Oto jak to zrobić:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


Z :




- `amt_msat`: Ilość Invoice w milisatoshis (minimum 3000 Sats) ;
- `expiry_sec` : czas wygaśnięcia Invoice w sekundach ;
- `asset_id`: Identyfikator zasobu RGB powiązanego z Invoice;
- `asset_amount`: Kwota aktywów RGB, które mają zostać przeniesione z tym Invoice.


W odpowiedzi otrzymasz RGB Invoice:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


Teraz zapłacimy ten Invoice z pierwszego węzła, który posiada niezbędną gotówkę za pomocą tokena `PBN`:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


Płatność została dokonana. Można to zweryfikować, wykonując polecenie :


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


Oto jak wdrożyć węzeł Lightning zmodyfikowany do przenoszenia zasobów RGB. Ta demonstracja jest oparta na :




- Środowisko regtest (poprzez `./regtest.sh`) lub Testnet ;
- Węzeł Lightning (`RGB-lightning-node`) oparty na `bitcoind`, indeksatorze i `RGB-proxy-server`;
- Seria interfejsów API JSON REST do otwierania/zamykania kanałów, wydawania tokenów, przesyłania zasobów za pośrednictwem Lightning itp.


Dzięki temu procesowi:




- Transakcje Lightning Engagement zawierają dodatkowe wyjście (OP_RETURN lub Taproot) z zakotwiczeniem przejścia RGB;
- Przelewy są dokonywane dokładnie w taki sam sposób, jak tradycyjne płatności Lightning, ale z dodatkiem tokena RGB;
- Wiele węzłów RLN może być połączonych w celu kierowania i eksperymentowania z płatnościami w wielu węzłach, pod warunkiem, że istnieje wystarczająca płynność zarówno w bitcoinach, jak i aktywach RGB na ścieżce.


Jeśli uważasz, że ten poradnik był przydatny, będę bardzo wdzięczny, jeśli umieścisz poniżej kciuk Green. Zachęcam również do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Polecam również ten samouczek, w którym wyjaśniam, jak używać narzędzia RGB CLI opracowanego przez stowarzyszenie LNP/BP do tworzenia RGB Contract:


https://planb.network/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4