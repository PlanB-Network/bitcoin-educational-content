---
name: RGB CLI
description: Jak utworzyć inteligentne kontrakty Exchange na RGB?
---
![cover](assets/cover.webp)


W tym samouczku prześledzimy krok po kroku proces pisania Contract przy użyciu narzędzia wiersza poleceń `RGB` stworzonego przez stowarzyszenie LNP/BP. Celem jest pokazanie, jak zainstalować i manipulować CLI, skompilować Schema, zaimportować Interface i Interface Implementation, a następnie wydać zasób RGB. Przyjrzymy się również podstawowej logice, w tym kompilacji i walidacji stanu. Pod koniec tego samouczka powinieneś być w stanie odtworzyć proces i stworzyć własne kontrakty RGB.


## Przypomnienie o protokole RGB


RGB to protokół, który działa na szczycie Bitcoin i emuluje funkcjonalność Smart contract oraz zarządzanie zasobami cyfrowymi, bez przeciążania Blockchain, na którym się opiera. W przeciwieństwie do konwencjonalnych inteligentnych kontraktów On-Chain (jak na przykład na Ethereum), RGB opiera się na systemie "*Client-side Validation*": większość danych i historii statusu jest wymieniana i przechowywana wyłącznie przez zaangażowanych uczestników, podczas gdy Bitcoin Blockchain obsługuje jedynie niewielkie zobowiązania kryptograficzne (za pośrednictwem mechanizmów takich jak *Tapret* lub *Opret*). W protokole RGB Bitcoin Blockchain służy zatem jedynie jako serwer znaczników czasu i system ochrony Double-spending.


RGB Contract ma strukturę ewolucyjnej maszyny stanów. Rozpoczyna się od Genesis, który definiuje stan początkowy (opisujący na przykład Supply, ticker lub inne metadane) zgodnie ze ściśle wpisanym i skompilowanym Schema. Przejścia stanu i, w razie potrzeby, rozszerzenia stanu są następnie stosowane w celu modyfikacji lub rozszerzenia tego stanu. Każda operacja, niezależnie od tego, czy przenosi aktywa zamienne (RGB20), czy tworzy unikalne aktywa (RGB21), obejmuje *Single-use Seals*. Łączą one Bitcoin UTXO ze stanami off-chain i zapobiegają podwójnym wydatkom, zapewniając jednocześnie poufność i skalowalność.


Aby dowiedzieć się więcej na temat działania protokołu RGB, polecam udział w tym kompleksowym szkoleniu:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Wewnętrzna logika RGB opiera się na bibliotekach Rust, które programiści mogą importować do swoich projektów w celu zarządzania częścią *Client-side Validation*. Ponadto zespół LNP/BP pracuje nad powiązaniami dla innych języków, ale nie zostało to jeszcze sfinalizowane. Ponadto inne podmioty, takie jak Bitfinex, opracowują własne stosy integracyjne, ale omówimy je w innym samouczku. Na chwilę obecną `RGB` CLI jest oficjalnym odniesieniem, nawet jeśli pozostaje stosunkowo nieoszlifowany.


## Instalacja i prezentacja narzędzia RGB CLI


Główne polecenie nazywa się po prostu `RGB`. Została zaprojektowana tak, by przypominać `git`, z zestawem podkomend do manipulowania kontraktami, wywoływania ich, wydawania zasobów i tak dalej. Bitcoin Wallet nie jest obecnie zintegrowany, ale będzie w nadchodzącej wersji (0.11). Ta następna wersja umożliwi użytkownikom tworzenie i zarządzanie portfelami (za pośrednictwem deskryptorów) bezpośrednio z `RGB`, w tym generowanie PSBT, kompatybilność z zewnętrznym sprzętem (np. Hardware Wallet) do podpisywania i interoperacyjność z oprogramowaniem takim jak Sparrow. Uprości to cały scenariusz emisji i transferu aktywów.


### Instalacja za pośrednictwem Cargo


Instalujemy narzędzie w Rust z :


```bash
cargo install rgb-contracts --all-features
```


(Uwaga: skrzynia nazywa się `RGB-contracts`, a zainstalowane polecenie będzie nosiło nazwę `RGB`. Jeśli skrzynka o nazwie `RGB` już istniała, mogło dojść do kolizji, stąd nazwa)


Instalacja kompiluje dużą liczbę zależności (np. parsowanie poleceń, integracja Electrum, zarządzanie dowodami wiedzy zerowej itp.)


Po zakończeniu instalacji aplikacja :


```bash
rgb
```


Uruchomienie `RGB` (bez argumentów) wyświetla listę dostępnych podkomend, takich jak `interfaces`, `Schema`, `import`, `export`, `issue`, `Invoice`, `transfer`, itd. Możesz zmienić lokalny katalog przechowywania (Stash, który przechowuje wszystkie logi, schematy i implementacje), wybrać sieć (Testnet, Mainnet) lub skonfigurować serwer Electrum.


![RGB-CLI](assets/fr/01.webp)


### Pierwszy przegląd elementów sterujących


Po uruchomieniu poniższego polecenia zobaczysz, że `RGB20` Interface jest już domyślnie zintegrowany:


```bash
rgb interfaces
```


Jeśli ten Interface nie jest zintegrowany, sklonuj :


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


Skompiluj go:


```bash
cargo run
```


Następnie zaimportuj wybrany Interface:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-CLI](assets/fr/02.webp)


Powiedziano nam jednak, że żaden Schema nie został jeszcze zaimportowany do oprogramowania. Nie ma też Contract w Stash. Aby to sprawdzić, należy uruchomić polecenie :


```bash
rgb schemata
```


Następnie można sklonować repozytorium, aby pobrać określone schematy:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-CLI](assets/fr/03.webp)


To repozytorium zawiera, w katalogu `src/`, kilka plików Rust (na przykład `nia.rs`), które definiują schematy (NIA dla "*Non Inflatable Asset*", UDA dla "*Unique Digital Asset*", itp.) Aby skompilować, można następnie uruchomić :


```bash
cd rgb-schemata
cargo run
```


Spowoduje to wygenerowanie kilku plików `.RGB` i `.rgba` odpowiadających skompilowanym schematom. Na przykład, można znaleźć `NonInflatableAsset.RGB`.


### Importowanie Schema i Interface Implementation


Możesz teraz zaimportować schemat do `RGB`:


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-CLI](assets/fr/04.webp)


Spowoduje to dodanie go do lokalnego Stash. Jeśli uruchomimy następujące polecenie, zobaczymy, że Schema jest teraz wyświetlany:


```bash
rgb schemata
```


## Tworzenie Contract (emisja)


Istnieją dwa podejścia do tworzenia nowego zasobu:




- Albo używamy skryptu lub kodu w Rust, który buduje Contract poprzez wypełnienie pól Schema (Global State, Owned States, itp.) i tworzy plik `.RGB` lub `.rgba`;
- Można też użyć bezpośrednio podkomendy `issue` z plikiem YAML (lub TOML) opisującym właściwości tokena.


Przykłady można znaleźć w Rust w folderze `examples`, który ilustruje jak zbudować `ContractBuilder`, wypełnić `Global State` (nazwa aktywa, ticker, Supply, data, itp.), zdefiniować Owned State (do którego UTXO jest przypisany), a następnie skompilować to wszystko do *Contract Consignment*, który można wyeksportować, zatwierdzić i zaimportować do Stash.


Innym sposobem jest ręczna edycja pliku YAML, aby dostosować `ticker`, `name`, `Supply` i tak dalej. Załóżmy, że plik nazywa się `RGB20-demo.yaml`. Możesz określić :




- `spec`: ticker, nazwa, precyzja ;
- `terms`: pole dla informacji prawnych;
- `issuedSupply`: ilość wydanych tokenów;
- `assignments`: wskazuje Single-Use Seal (*Seal Definition*) i odblokowaną ilość.


Oto przykład pliku YAML do utworzenia:


```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```


![RGB-CLI](assets/fr/05.webp)


Następnie wystarczy uruchomić polecenie :


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-CLI](assets/fr/06.webp)


W moim przypadku unikalny identyfikator Schema (ujęty w pojedyncze cudzysłowy) to `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` i nie podałem żadnego emitenta. Więc moje zamówienie to :


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Jeśli nie znasz identyfikatora Schema, uruchom polecenie :


```bash
rgb schemata
```


CLI odpowiada, że nowy Contract został wydany i dodany do Stash. Jeśli wpiszemy następujące polecenie, zobaczymy, że istnieje teraz dodatkowy Contract, odpowiadający właśnie wydanemu:


```bash
rgb contracts
```


![RGB-CLI](assets/fr/07.webp)


Następnie kolejne polecenie wyświetla globalne stany (nazwa, ticker, Supply...) oraz listę Owned States, czyli alokacji (na przykład 1 milion tokenów `PBN` zdefiniowanych w UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).


```bash
rgb state '<ContractId>'
```


![RGB-CLI](assets/fr/08.webp)


## Eksport, import i walidacja


Aby udostępnić Contract innym użytkownikom, można go wyeksportować z Stash do pliku :


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-CLI](assets/fr/09.webp)


Plik `myContractPBN.RGB` może zostać przekazany innemu użytkownikowi, który może dodać go do swojego Stash za pomocą komendy :


```bash
rgb import myContractPBN.rgb
```


Podczas importu, jeśli jest to prosty *Contract Consignment*, otrzymamy komunikat "`Importowanie Consignment RGB`". Jeśli jest to większy *State Transition Consignment*, polecenie będzie inne (`RGB accept`).


Aby zapewnić poprawność, można również użyć lokalnej funkcji sprawdzania poprawności. Na przykład, można uruchomić :


```bash
rgb validate myContract.rgb
```


### Użycie, weryfikacja i wyświetlanie Stash


Dla przypomnienia, Stash jest lokalnym spisem schematów, interfejsów, implementacji i kontraktów (Genesis + przejścia). Każde uruchomienie polecenia "import" powoduje dodanie elementu do Stash. Ten Stash można wyświetlić szczegółowo za pomocą polecenia :


```bash
rgb dump
```


![RGB-CLI](assets/fr/10.webp)


Spowoduje to utworzenie folderu generate ze szczegółami całego Stash.


## Transfer i PSBT


Aby wykonać transfer, będziesz musiał manipulować lokalnym Bitcoin Wallet, aby zarządzać zobowiązaniami `Tapret` lub `Opret`.


### generate i Invoice


W większości przypadków interakcja między uczestnikami Contract (np. Alicją i Bobem) odbywa się poprzez generowanie Invoice. Jeśli Alicja chce, aby Bob coś wykonał (transfer tokena, ponowne wydanie, akcja w DAO itp.), Alicja tworzy Invoice szczegółowo opisujący jej instrukcje dla Boba. Mamy więc :




- Alice** (emitent Invoice) ;
- Bob** (który odbiera i wykonuje Invoice).


W przeciwieństwie do innych ekosystemów, RGB Invoice nie ogranicza się do pojęcia płatności. Może zawierać dowolne żądanie powiązane z Contract: odwołanie klucza, głosowanie, utworzenie grawerunku (*grawerunek*) na NFT itp. Odpowiednia operacja może być opisana w Contract Interface. Odpowiednia operacja może być opisana w Contract Interface.


Poniższe polecenie generuje RGB Invoice:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Z :




- `$Contract`: Identyfikator Contract (*ContractId*) ;
- `$Interface`: Interface, który ma zostać użyty (np. `RGB20`);
- `$ACTION`: nazwa operacji określonej w Interface (dla prostego zamiennego transferu tokena może to być "Transfer"). Jeśli Interface zapewnia już domyślną akcję, nie trzeba jej tutaj ponownie wprowadzać;
- `$STATE`: dane statusu, które mają zostać przesłane (na przykład ilość tokenów, jeśli przesyłany jest token zamienny);
- `$Seal`: Single-Use Seal beneficjenta (Alicji), tj. wyraźne odniesienie do UTXO. Bob użyje tych informacji do zbudowania Witness Transaction, a odpowiednie dane wyjściowe będą następnie należeć do Alicji (w * blinded UTXO* lub w postaci niezaszyfrowanej).


Na przykład za pomocą następujących poleceń


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI będzie generate i Invoice jak :


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Może on zostać przesłany do Boba dowolnym kanałem (tekst, kod QR itp.).


### Dokonywanie przelewu


Aby przenieść z tego Invoice :




- Bob (który posiada tokeny w swoim Stash) ma Bitcoin Wallet. Musi przygotować transakcję Bitcoin (w formie PSBT, np. `tx.PSBT`), która wydaje UTXO, gdzie znajdują się wymagane tokeny RGB, plus jeden UTXO dla waluty (Exchange);
- Bob wykonuje następujące polecenie:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Spowoduje to wygenerowanie pliku `Consignment.RGB`, który zawiera :
 - Historia przejścia udowadnia Alice, że tokeny są autentyczne;
 - Nowe przejście, które przenosi tokeny do Single-Use Seal Alice;
 - Witness Transaction (bez znaku).
- Bob wysyła ten plik `Consignment.RGB` do Alicji (przez e-mail, serwer udostępniania lub protokół RGB-RPC, Storm itp;)
- Alice otrzymuje `Consignment.RGB` i akceptuje go w swoim własnym Stash:


```bash
alice$ rgb accept consignment.rgb
```




- CLI sprawdza ważność przejścia i dodaje je do Stash Alice. Jeśli jest nieprawidłowe, polecenie kończy się niepowodzeniem ze szczegółowymi komunikatami o błędach. W przeciwnym razie kończy się sukcesem i informuje, że przykładowa transakcja nie została jeszcze rozgłaszana w sieci Bitcoin (Bob czeka na kontrolkę Green Alicji);
- Jako potwierdzenie, polecenie `accept` zwraca podpis (*payslip*), który Alice może wysłać do Boba, aby pokazać mu, że zatwierdziła *Consignment*;
- Bob może następnie podpisać i opublikować (`--publish`) swoją transakcję Bitcoin:


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Gdy tylko ta transakcja zostanie potwierdzona On-Chain, Ownership składnika aktywów zostanie uznany za przekazany Alice. Wallet Alicji, monitorujący Mining transakcji, widzi nowy Owned State pojawiający się w jego Stash.


Wiesz już, jak wystawić i przenieść RGB Contract. Jeśli ten poradnik okazał się przydatny, będę bardzo wdzięczny za umieszczenie poniżej kciuka Green. Zapraszam do udostępnienia tego artykułu w sieciach społecznościowych. Dziękuję bardzo!


Polecam również ten samouczek, w którym wyjaśniam, jak niemal natychmiast uruchomić węzeł Lightning kompatybilny z RGB do tokenów Exchange:


https://planb.network/tutorials/node/others/rln-ffc02528-329b-4e16-bd83-873d0299feea