---
name: RGB
description: Wprowadzenie i tworzenie zasobów na RGB
---

![RGB vs Ethereum](assets/0.webp)


## wprowadzenie


W dniu 3 stycznia 2009 r. Satoshi Nakamoto uruchomił pierwszy węzeł Bitcoin, od tego momentu dołączyły nowe węzły i Bitcoin zaczął zachowywać się tak, jakby był nową formą życia, formą życia, która nie przestała ewoluować, krok po kroku stała się najbezpieczniejszą siecią na świecie w wyniku unikalnego projektu, bardzo dobrze przemyślanego przez Satoshi, ponieważ poprzez zachęty ekonomiczne przyciąga użytkowników powszechnie nazywanych górnikami do inwestowania w energię i moc obliczeniową, co przyczynia się do bezpieczeństwa sieci.


W miarę jak Bitcoin kontynuuje swój rozwój i adopcję, napotyka problemy ze skalowalnością, sieć Bitcoin pozwala na wydobycie nowego bloku z transakcjami w przybliżonym czasie 10 minut, zakładając, że mamy 144 bloki w ciągu dnia z maksymalnymi wartościami 2700 transakcji na blok, Bitcoin pozwoliłby tylko na 4,5 transakcji na sekundę, Satoshi był świadomy tego ograniczenia, możemy to zobaczyć w e-mailu1 wysłanym do Mike'a Hearna w marcu 2011 r., w którym wyjaśnia, jak działa to, co znamy dzisiaj jako kanał płatności. mikropłatności szybko i bezpiecznie bez czekania na potwierdzenia. W tym miejscu wkraczają protokoły off-chain.


Według Christiana Deckera2 protokoły off-chain to zazwyczaj systemy, w których użytkownicy wykorzystują dane z Blockchain i zarządzają nimi bez dotykania samego Blockchain aż do ostatniej chwili. W oparciu o tę koncepcję narodził się Lightning Network, sieć wykorzystująca protokoły off-chain, aby umożliwić niemal natychmiastowe dokonywanie płatności Bitcoin, a ponieważ nie wszystkie te operacje są zapisywane w łańcuchu bloków, umożliwia tysiące transakcji na sekundę i skalowanie Bitcoin.


Badania i rozwój w obszarze protokołów off-chain na Bitcoin otworzyły puszkę pandory, dziś wiemy, że możemy osiągnąć znacznie więcej niż transfer wartości w sposób zdecentralizowany, stowarzyszenie non-profit LNP/BP Standards Association koncentruje się na rozwoju protokołów Layer 2 i 3 na Bitcoin i Lightning Network, wśród tych projektów wyróżnia się RGB.


## Co to jest RGB?


RGB wyłonił się z badań Petera Todda3 nad uszczelnieniami jednorazowego użytku i walidacją po stronie klienta, które zostały ukute w latach 2016-2019 przez Giacomo Zucco i społeczność w lepszy protokół aktywów dla Bitcoin i Lightning Network. Dalsza ewolucja tych pomysłów doprowadziła do rozwinięcia RGB w pełnoprawny system Smart contract przez Maxima Orlovsky'ego, który kieruje jego wdrożeniem od 2019 roku przy udziale społeczności.


Możemy zdefiniować RGB jako zestaw protokołów open source, który pozwala nam wykonywać złożone inteligentne kontrakty w skalowalny i poufny sposób. Nie jest to konkretna sieć (jak Bitcoin lub Lightning); każdy Smart contract jest po prostu zbiorem uczestników Contract, którzy mogą wchodzić w interakcje za pomocą różnych kanałów komunikacji (domyślnie Lightning Network). RGB wykorzystuje Bitcoin Blockchain jako Layer stanu Commitment i utrzymuje kod Smart contract i dane off-chain, co czyni go skalowalnym, wykorzystując transakcje Bitcoin (i skrypt) jako system kontroli Ownership dla inteligentnych kontraktów; podczas gdy ewolucja Smart contract jest określona przez schemat off-chain, na koniec należy zauważyć, że wszystko jest walidowane po stronie klienta.


Mówiąc prościej, RGB to system, który pozwala użytkownikowi na audyt Smart contract, wykonanie go i zweryfikowanie indywidualnie w dowolnym momencie bez ponoszenia dodatkowych kosztów, ponieważ nie wykorzystuje do tego Blockchain, jak robią to "tradycyjne" systemy. Złożone systemy inteligentnych kontraktów były pionierami Ethereum, ale ponieważ wymagają od użytkownika wydania znacznych ilości gazu na każdą operację, nigdy nie osiągnęły skalowalności, którą obiecały, w konsekwencji nigdy nie były opcją bankową dla użytkowników wykluczonych z obecnego systemu finansowego.


Obecnie branża Blockchain promuje, że zarówno kod inteligentnych kontraktów, jak i dane muszą być przechowywane w Blockchain i wykonywane przez każdy węzeł sieci, niezależnie od nadmiernego wzrostu rozmiaru lub niewłaściwego wykorzystania zasobów obliczeniowych. Schemat zaproponowany przez RGB jest znacznie bardziej inteligentny i wydajny, ponieważ odcina się od paradygmatu Blockchain poprzez oddzielenie inteligentnych kontraktów i danych od Blockchain, a tym samym unika nasycenia sieci obserwowanego na innych platformach, z kolei nie zmusza każdego węzła do wykonywania każdego Contract, ale raczej zaangażowanych stron, co zwiększa poufność do poziomu nigdy wcześniej nie widzianego.


![RGB vs Ethereum](assets/1.webp)


## Inteligentne kontrakty w RGB


W RGB deweloper Smart contract definiuje schemat określający zasady ewolucji Contract w czasie. Schemat ten jest standardem dla budowy inteligentnych kontraktów w RGB, a zarówno emitent definiujący Contract do emisji, jak i Wallet lub Exchange muszą przestrzegać określonego schematu, względem którego muszą walidować Contract. Tylko jeśli walidacja jest prawidłowa, każda ze stron może akceptować żądania i pracować z aktywem.


Smart contract w RGB jest Directed Acyclic Graph (DAG) zmian stanu, gdzie tylko część grafu jest zawsze znana i nie ma dostępu do reszty. Schemat RGB jest podstawowym zestawem reguł dla ewolucji tego grafu, od którego zaczyna Smart contract. Każdy Contract Participant może dodać do tych reguł (jeśli jest to dozwolone przez Schema), a wynikowy graf jest budowany z iteracyjnego stosowania tych reguł.


## Aktywa trwałe


Aktywa zamienne w RGB są zgodne ze specyfikacją LNPBP RGB-204, gdy RGB-20 jest zdefiniowany, dane aktywów znane jako "dane Genesis" są dystrybuowane za pośrednictwem Lightning Network, który zawiera to, co jest wymagane do korzystania z aktywów. Najbardziej podstawowa forma aktywów nie pozwala na wtórną emisję, spalanie tokenów, renominację lub wymianę.


Czasami emitent będzie musiał wydać więcej tokenów w przyszłości, tj. stablecoinów, takich jak USDT, które utrzymują wartość każdego tokena związaną z wartością waluty inflacyjnej, takiej jak USD. Aby to osiągnąć, istnieją bardziej złożone schematy RGB-20, które oprócz danych Genesis wymagają od emitenta produkcji partii, które będą również krążyć w Lightning Network; dzięki tym informacjom możemy poznać całkowity obieg Supply aktywów. To samo dotyczy spalania aktywów lub zmiany ich nazwy.


Informacje związane z aktywem mogą być publiczne lub prywatne: jeśli emitent wymaga poufności, może nie udostępniać informacji o tokenie i wykonywać operacje z zachowaniem całkowitej prywatności, ale mamy też odwrotny przypadek, w którym emitent i posiadacze potrzebują, aby cały proces był przejrzysty. Osiąga się to poprzez udostępnianie danych tokena.


## Procedury RGB-20


Procedura wypalania wyłącza tokeny, wypalone tokeny nie mogą być już używane.


Procedura wymiany ma miejsce, gdy tokeny są spalane i tworzona jest nowa ilość tego samego tokena. Pomaga to zmniejszyć rozmiar danych historycznych aktywów, co jest ważne dla utrzymania szybkości aktywów.


Aby wesprzeć przypadek użycia, w którym możliwe jest wypalanie zasobów bez konieczności ich wymiany, używany jest pod-schemat RGB-20, który pozwala tylko na wypalanie zasobów.


## Aktywa niezamienne


Aktywa niewymienialne w RGB są zgodne ze specyfikacją LNPBP RGB-215, kiedy pracujemy z NFT, mamy również schemat główny i schemat podrzędny. Schematy te mają procedurę grawerowania, która pozwala nam dołączać niestandardowe dane przez część właściciela tokena, najczęstszym przykładem, jaki widzimy obecnie w NFT, jest sztuka cyfrowa powiązana z tokenem. Wystawca tokena może zabronić grawerowania tych danych za pomocą pod-schematu RGB-21. W przeciwieństwie do innych systemów NFT Blockchain, RGB pozwala na dystrybucję dużych danych tokenów medialnych w sposób całkowicie zdecentralizowany i odporny na cenzurę, wykorzystując rozszerzenie sieci Lightning P2P o nazwie Bifrost, która jest również wykorzystywana do budowania wielu innych form funkcjonalności RGB specyficznych dla Smart contract.


Oprócz aktywów zamiennych i NFT, RGB i Bifrost mogą być wykorzystywane do tworzenia innych form inteligentnych kontraktów, w tym DEX, pul płynności, algorytmicznych stabilnych monet itp.


## NFT z RGB vs NFT z innych platform



- Nie ma potrzeby stosowania drogiego magazynu Blockchain
- Nie ma potrzeby stosowania IPFS, zamiast tego używane jest rozszerzenie Lightning Network (zwane Bifrost) (i jest ono w pełni szyfrowane end-to-end)
- Nie ma potrzeby stosowania specjalnego rozwiązania do zarządzania danymi - ponownie, Bifrost przejmuje tę rolę
- Nie ma potrzeby ufania stronom internetowym w zakresie przechowywania danych dotyczących tokenów NFT lub aktywów emisyjnych / ABI Contract
- Wbudowane szyfrowanie DRM i zarządzanie Ownership
- Infrastruktura do tworzenia kopii zapasowych przy użyciu Lightning Network (Bifrost)
- Sposoby monetyzacji treści (nie tylko sprzedaż samego NFT, ale także wielokrotny dostęp do treści)


## Wnioski


Od czasu uruchomienia Bitcoin, prawie 13 lat temu, przeprowadzono wiele badań i eksperymentów w tej dziedzinie, zarówno sukcesy, jak i błędy pozwoliły nam nieco lepiej zrozumieć, jak zdecentralizowane systemy zachowują się w praktyce, co czyni je naprawdę zdecentralizowanymi i jakie działania prowadzą je do centralizacji, wszystko to doprowadziło nas do wniosku, że prawdziwa decentralizacja jest zjawiskiem rzadkim i trudnym do osiągnięcia, prawdziwa decentralizacja została osiągnięta tylko przez Bitcoin i właśnie z tego powodu koncentrujemy nasze wysiłki na budowaniu na nim.


RGB ma swoją własną króliczą norę wewnątrz króliczej nory Bitcoin, podczas gdy ja spadam w dół przez nie, opublikuję to, czego się nauczyłem, w następnym artykule będziemy mieli wprowadzenie do węzłów LNP i RGB i jak z nich korzystać.



- 1 https://plan99.net/~mike/Satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md


# Samouczek węzła RGB


## Wprowadzenie


W tym samouczku wyjaśniamy, jak używać RGB-node do tworzenia zamiennych tokenów i jak je przesyłać, ten dokument jest oparty na demo RGB-node i różni się tym, że ten samouczek wykorzystuje prawdziwe dane Testnet i do tego musimy zbudować własne Partially Signed Bitcoin Transaction, PSBT od teraz.


## Wymagania


Zaleca się korzystanie z dystrybucji Linuksa, ten poradnik został napisany przy użyciu Pop!OS, który jest oparty na Ubuntu i będzie potrzebny:



- ładunek
- Rdzeń Bitcoin
- git


Uwaga: Ten samouczek pokazuje wykonywanie poleceń w terminalu Linuksa, aby odróżnić to, co użytkownik pisze, od odpowiedzi, którą otrzymuje w terminalu, dodajemy $ symbolizujący znak zachęty bash.


Będziesz musiał zainstalować kilka zależności:


```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```


Build & Run


RGB-node jest work in progress (WIP), dlatego musimy zlokalizować się w konkretnym commicie (3f3c520c19d84c66d430e76f0fc68c5a66d79c84), aby móc go poprawnie skompilować i używać, w tym celu wykonujemy następujące polecenia.


```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```


Teraz kompilujemy go, nie zapominając o użyciu flagi --locked, ponieważ w wersji clap wprowadzono przełomową zmianę.


```
$ cargo install --path . --all-features --locked

....
....
Finished release [optimized] target(s) in 2m 14s
Installing /home/user/.cargo/bin/fungibled
Installing /home/user/.cargo/bin/rgb-cli
Installing /home/user/.cargo/bin/rgbd
Installing /home/user/.cargo/bin/stashd
Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```


Jak mówi nam kompilator Rust, binaria zostały skopiowane do katalogu $HOME/.cargo/bin, jeśli twój kompilator skopiował je w inne miejsce, musisz upewnić się, że katalog ten musi być uwzględniony w $PATH.


Wśród zainstalowanych binariów możemy zobaczyć trzy demony lub usługi (pliki kończące się na d) oraz CLI (linia poleceń Interface), CLI pozwala nam na interakcję z głównym rgbd daemon. Ponieważ w tym samouczku zamierzamy uruchomić dwa węzły, będziemy również potrzebować dwóch klientów, z których każdy musi łączyć się z własnym węzłem, w tym celu tworzymy dwa aliasy.


```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```


Możemy po prostu uruchomić aliasy lub dodać je na końcu pliku $HOME/.bashrc i uruchomić źródło $HOME/.bashrc.

Założenie


Węzeł RGB nie obsługuje żadnych funkcji związanych z Wallet, wykonuje jedynie zadania specyficzne dla RGB na danych, które zostaną dostarczone przez zewnętrzny Wallet, taki jak rdzeń Bitcoin. W szczególności, aby zademonstrować podstawowy przepływ pracy z wystawianiem i przesyłaniem, będziemy potrzebować:



- Issuance_utxo, z którym RGB-node-0 powiąże nowo wyemitowany zasób
- A receive_utxo, gdzie RGB-node-1 odbiera zasób
- A change_utxo, gdzie RGB-node-0 otrzymuje zmianę zasobu
- Partially Signed Bitcoin Transaction (tx.PSBT), którego wyjściowy klucz publiczny zostanie zmodyfikowany w celu dołączenia Commitment do transferu.


Będziemy używać Bitcoin core CLI, musimy mieć bitcoind daemon działający na Testnet, to da nam interoperacyjność i na koniec będziemy mogli wysyłać własne zasoby do innych użytkowników RGB, którzy postępowali zgodnie z tym samouczkiem.


Dla uproszczenia dodamy ten alias na końcu naszego pliku ~/.bashrc.


```
alias bcli="bitcoin-cli -testnet"
```


Wymieńmy nasze niewydane transakcje wyjściowe i wybierzmy dwie, jedna będzie issuance_utxo, a druga change_utxo, nie ma znaczenia, która jest która, ważne jest to, że emitent ma kontrolę nad tymi dwoma UTXO.


```
$ bcli listunspent
[
{
"txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
"vout": 1,
"address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
"label": "",
"scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
"amount": 0.01703963,
"confirmations": 62432,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
"safe": true
},
{
"txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
"vout": 1,
"address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
"scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
"amount": 0.02877504,
"confirmations": 189184,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
"safe": true
}
]
```


Zanim przejdziemy dalej, musimy porozmawiać o punktach wyjścia, pojedyncza transakcja może zawierać wiele wyjść, punkt wyjścia zawiera zarówno 32-bajtowy txid, jak i 4-bajtowy numer indeksu wyjścia (vout), aby odnieść się do konkretnego wyjścia oddzielonego dwukropkiem :. W naszym wyjściu listunspent możemy znaleźć dwa UTXO, na każdym z nich możemy zobaczyć txid i vout, są to punkty wyjścia issuance_utxo i change_utxo.


receive_utxo to UTXO kontrolowany przez odbiornik, w tym przypadku użyjemy e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0, który jest punktem wyjścia z innego Wallet.



- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0


Utworzymy teraz częściowo podpisaną transakcję (tx.PSBT), której dane wyjściowe zostaną zmodyfikowane tak, aby zawierały commit do transferu, pamiętaj, aby zastąpić txid i vout własnymi, docelowy Address tak naprawdę nie ma znaczenia, może być twój lub może pochodzić od innej osoby, nie ma znaczenia, gdzie trafiają te Sats, ważne jest to, że używamy issuance_utxo.


```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
"psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
"fee": 0.00000280,
"changepos": 0
}
```


Dane wyjściowe dały nam PSBT w kodowaniu base64, którego użyjemy do utworzenia tx.PSBT.


```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```


Utwórzmy nowy katalog o nazwie rgbdata, w którym przechowywane będą dane każdego węzła.


```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```


Znajdując się już w $HOME/rgbdata uruchamiamy każdy węzeł w innym terminalu, gdzie ~/.cargo/bin jest katalogiem, do którego cargo skopiowało wszystkie binaria po instalacji RGB-node.


```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```


## Emisja


Aby wyemitować aktywa, uruchamiamy rgb0-CLI z zamiennymi podkomendami emisji, a następnie argumentami, tickerem USDT, nazwą "USD Tether", aw alokacji użyjemy kwoty emisji i issuance_utxo, jak widzimy poniżej:


```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```


Zasób został pomyślnie wydany. Użyj tych informacji do udostępniania:

Informacje o aktywach:


```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"


genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```


Otrzymujemy assetId, potrzebujemy go do przeniesienia zasobu.


```
$ rgb0-cli fungible list

- name: USD Tether
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
```


## generate blinded UTXO


Aby otrzymać nowe USDT, RGB-węzeł-1 musi generate blinded UTXO odpowiadający receive_utxo do przechowywania aktywów.


```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```


Aby móc akceptować przelewy związane z tym UTXO, będziemy potrzebować oryginalnego receive_utxo i blinding_factor.


## Transfer


Aby przenieść pewną ilość aktywów do RGB-węzła-1, musimy wysłać je do blinded UTXO, RGB-węzeł-0 musi utworzyć Consignment i ujawnienie, a następnie zatwierdzić je w transakcji Bitcoin. Następnie będziemy potrzebować PSBT, który zmodyfikujemy, aby zawierał zatwierdzenie. Ponadto opcje -i i -a pozwalają nam podać wejściowy punkt wyjścia, który byłby źródłem zasobu i alokacją, w której otrzymamy zmianę, musimy wskazać ją w następujący sposób @<change_utxo>.


```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1

Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```


Spowoduje to zapisanie trzech nowych plików, Consignment, ujawnienie i PSBT zawierający poprawkę, ten PSBT nazywa się Witness Transaction, Consignment jest wysyłany do RGB-węzła-1.


## Świadek


Witness Transaction powinien zostać podpisany i rozesłany, w tym celu musimy go zakodować base64.


```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```


Podpisz go za pomocą podkomendy walletprocesspsbt.


```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
{
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
"complete": true
}
```


Teraz sfinalizuj to i zdobądź hex.


```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="
{
"hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
"complete": true
}
```


## Transmisja


Prześlij go za pomocą podkomendy sendrawtransaction, aby potwierdzić go w Blockchain.


```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```


## Akceptuj


Aby zaakceptować transfer przychodzący, RGB-węzeł-1 powinien otrzymać plik Consignment z RGB-węzła-0, posiadać receive_utxo i odpowiedni blinding_factor wygenerowany podczas generowania blinding UTXO.


```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Asset transfer successfully accepted.
```


Możemy teraz zobaczyć (w polu knownAllocations) nową alokację 100 jednostek aktywów w <receive_utxo> po uruchomieniu:


```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 1
outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
revealedAmount:
value: 100
blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```


Ponieważ receive_utxo był blinded, gdy dokonano transferu, płatnik RGB-node-0 nie ma informacji o tym, gdzie wysłano 100 USDT, więc lokalizacja nie jest wyświetlana w knownAllocations .


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```


Ale jak widać RGB-node-0 nie widzi zmiany zasobu 900, którą dostarczyliśmy do polecenia transferu z argumentem -a. Aby zarejestrować zmianę RGB-node-0 musi zaakceptować ujawnienie.


```
$ rgb0-cli fungible enclose disclosure.rgb

Disclosure data successfully enclosed.
```


Jeśli RGB-node-0 się powiedzie, możesz zobaczyć zmianę, wyświetlając zasób.


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 0
outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
revealedAmount:
value: 900
blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```


## Wnioski


Byliśmy w stanie stworzyć zamienny zasób i przenieść go z jednej transakcji do drugiej w sposób prywatny, jeśli sprawdzimy potwierdzoną transakcję w Block explorer, nie znajdziemy niczego innego niż zwykła transakcja, to dzięki temu, że RGB używa jednorazowych pieczęci do modyfikowania transakcji, W tym poście robię wprowadzenie do tego, jak działa RGB.


Ten post może zawierać błędy, jeśli coś znajdziesz, daj mi znać, aby ulepszyć ten przewodnik, sugestie i krytyka są również mile widziane, szczęśliwego hakowania! 🖖