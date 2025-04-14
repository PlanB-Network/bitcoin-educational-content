---
name: Budowanie z Elements i Liquid Network
goal: Naucz się korzystać z platformy Elements o otwartym kodzie źródłowym Blockchain i jej kluczowych funkcji
objectives: 

  - Zrozumienie podstawowych koncepcji platformy Elements Blockchain i łańcuchów bocznych Liquid.
  - Naucz się konfigurować i uruchamiać węzły Elements dla konfiguracji autonomicznych i Sidechain.
  - Zdobądź praktyczne doświadczenie z federacyjnymi block signing i Federated 2-Way Peg.
  - Skonfiguruj i zarządzaj bezpiecznymi, wydajnymi środowiskami Blockchain dla rzeczywistych przypadków użycia.

---

# Wykorzystanie Liquid i Elements


Odkryj zaawansowane funkcje i możliwości Liquid i Elements oraz dowiedz się, jak skutecznie wykorzystać te narzędzia do ulepszenia swoich projektów programistycznych. Szkolenie to zapewnia kompletne podstawy teoretyczne i praktyczne, umożliwiając opanowanie funkcji takich jak Confidential Transactions, Issued Assets i Federated block signing.


Liquid, oparty na frameworku Elements, został zaprojektowany w celu poprawy prywatności, skalowalności i funkcjonalności rozwiązań finansowych i technicznych. W tym kursie zdobędziesz praktyczne doświadczenie w zakresie wydawania i zarządzania aktywami, Federated 2-Way Peg oraz korzystania z narzędzi takich jak elementsd i elements-cli, umożliwiając tworzenie innowacyjnych rozwiązań dostosowanych do Twoich potrzeb.


Ten kurs jest dostosowany do programistów na wszystkich poziomach doświadczenia. Początkujący i średnio zaawansowani użytkownicy znajdą przystępne wyjaśnienia i praktyczne przykłady, podczas gdy zaawansowani użytkownicy mogą zagłębić się w szczegóły techniczne i mniej znane funkcje Liquid i Elements.


Dołącz do nas, aby podnieść swoje umiejętności, uwolnić pełny potencjał Liquid i Elements oraz stworzyć wpływowe narzędzia dla przyszłości innowacji Liquid.

+++

# Wprowadzenie


<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>


## Przegląd kursu


<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>


:::video id=e0166470-5561-4b3b-9d0d-4edee69b64d8:::


Witamy na kursie SID202!


Celem *Elements Academy* jest wprowadzenie i wyjaśnienie kluczowych pojęć *Elements*, platformy open-source, na której zbudowany jest Liquid Sidechain. Pod koniec tego kursu powinieneś mieć solidne zrozumienie głównych cech Elements, takich jak Confidential Transactions i Issued Assets, a także procesów związanych z obsługą Elements Core. Każda sekcja kursu zawiera lekcje z tekstami objaśniającymi i filmami, po których następuje quiz.


Szkolenie to ma na celu nauczenie, jak korzystać i rozwijać platformę Elements o otwartym kodzie źródłowym, ze szczególnym uwzględnieniem Liquid Network. Dowiesz się, w jaki sposób technologie te mogą zwiększyć prywatność, skalowalność i funkcjonalność twoich projektów rozwojowych. Niezależnie od tego, czy jesteś początkującym, czy doświadczonym programistą, ten kurs zapewni ci solidne podstawy do opanowania podstawowych koncepcji Elements i Liquid, a także ich praktycznych zastosowań.


**Sekcja 1: Wprowadzenie**

Zaczniemy od kompleksowego przeglądu koncepcji Elements. Dowiesz się, w jaki sposób platforma ta została zaprojektowana, aby zapewnić modułową i elastyczną podstawę do tworzenia łańcuchów bocznych, takich jak Liquid. Celem jest zrozumienie struktury Elements przed zagłębieniem się w jego praktyczne zastosowania.


**Sekcja 2: Elements**

Ta sekcja skupia się na działaniu Elements. Dowiesz się, jak skonfigurować węzeł Elements, obsługiwać go w trybie autonomicznym lub używać go jako Sidechain.


**Sekcja 3: Korzystanie z Elements - praktyczne przypadki użycia**

Po opanowaniu podstaw teoretycznych zajmiemy się praktycznymi zastosowaniami Elements. Dowiesz się, jak wykonać Confidential Transactions, wydać aktywa i zarządzać ponownym wydaniem aktywów.


**Sekcja 4: Federacja Elements**

Tutaj zbadamy zaawansowane mechanizmy, w tym sfederowane block signing, wykorzystanie Elements jako Sidechain i tworzenie niezależnych łańcuchów bloków. Ta sekcja pomoże ci zrozumieć, jak zapewnić bezpieczeństwo, integralność i interoperacyjność blockchainów opartych na Elements.


Gotowy do odkrycia potencjału Elements i Liquid Sidechain? Zaczynajmy!



## Przegląd Elements


<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>


:::video id=eae666b4-eddc-4e00-adea-2a5f94396044:::


Elements to platforma typu open source, obsługująca Sidechain, zapewniająca dostęp do zaawansowanych funkcji opracowanych przez członków społeczności, takich jak Confidential Transactions i Issued Assets.


Elements jest w swej istocie protokołem, który umożliwia osiągnięcie konsensusu wokół historii transakcji i zasad, które regulują transfer i tworzenie aktywów przechowywanych w rozproszonym Blockchain Ledger.


Więcej podstawowych informacji na temat Elements można znaleźć na stronie internetowej projektu Elements (https://elementsproject.org/), oficjalnym blogu Liquid (https://blog.Liquid.net/) i portalu deweloperskim (https://Liquid.net/devs).


### Elements


Wprowadzony na rynek w 2015 roku, Elements zmniejsza wewnętrzne koszty rozwoju i badań oraz wykorzystuje najnowszą technologię Blockchain, otwierając wiele nowych przypadków użycia do wdrożenia. Blockchain oparty na Elements może działać jako samodzielny Blockchain lub być podłączony do innego i działać jako Sidechain. Uruchomienie Elements jako Sidechain umożliwia weryfikowalne przenoszenie aktywów między różnymi łańcuchami bloków.


Zbudowany na bazie kodu Bitcoin i rozszerzający ją, pozwala programistom zaznajomionym z API bitcoind szybko i ekonomicznie tworzyć działające łańcuchy bloków i testować projekty proof-of-concept. Zbudowany na bazie kodu Bitcoin pozwala również Elements funkcjonować jako platforma testowa dla zmian w samym protokole Bitcoin.


Poniżej wymieniono niektóre z głównych cech Elements.


#### Confidential Transactions


Domyślnie wszystkie adresy w Elements są blinded przy użyciu Confidential Transactions. Zaślepienie to proces, w którym ilość i rodzaj transferowanych aktywów jest kryptograficznie ukryty przed wszystkimi, z wyjątkiem uczestników i tych, którym zdecydują się ujawnić klucz zaślepienia.


#### Issued Assets


Issued Assets na Elements umożliwia wydawanie i przekazywanie wielu rodzajów aktywów między uczestnikami sieci. Wyemitowany zasób korzysta również z Confidential Transactions i może zostać ponownie wydany lub zniszczony przez każdego, kto posiada odpowiedni reissuance token.


#### Federated 2-Way Peg


Elements to platforma Blockchain ogólnego przeznaczenia, którą można również "podpiąć" do istniejącego Blockchain (takiego jak Bitcoin), aby umożliwić dwukierunkowy transfer aktywów z jednego łańcucha do drugiego. Wdrożenie Elements jako Sidechain pozwala obejść niektóre nieodłączne właściwości głównego łańcucha, zachowując przy tym wysoki stopień bezpieczeństwa zapewniany przez aktywa zabezpieczone w głównym łańcuchu.


#### Podpisane bloki


Elements wykorzystuje Strong Federation sygnatariuszy, zwanych Block Signers, którzy podpisują i tworzą bloki w niezawodny i terminowy sposób. Eliminuje to opóźnienie transakcji procesu PoW Mining, który podlega dużej wariancji czasu bloku ze względu na losowy rozkład poisson. Sfederowany proces block signing osiąga niezawodne tworzenie bloków bez wprowadzania potrzeby zaufania strony trzeciej lub obliczeniowego `algorytmu` opartego na Mining.


Elements dodaje wszystkie te funkcje do bazy kodowej Bitcoin Core, rozszerzając możliwości protokołu mainchain i umożliwiając nowe biznesowe przypadki użycia po wdrożeniu jako Sidechain lub jako samodzielne rozwiązanie Blockchain.


# Element


<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>


## Jak działa Elements


<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>


:::video id=7c8c7981-11e5-47a2-a257-ef998f4892f5:::


Elements zapewnia techniczne rozwiązanie problemów, z którymi codziennie borykają się użytkownicy Blockchain: opóźnienia transakcji, brak prywatności i ryzyko zamienności.


Elements przezwycięża te problemy dzięki wykorzystaniu sfederowanych block signing i Confidential Transactions.


W przeciwieństwie do sieci Bitcoin, proces block signing w ramach Elements nie jest zależny od Dynamic Membership Multiparty Signatures (DMMS) i Proof of Work (PoW). Zamiast tego Elements wykorzystuje Strong Federation sygnatariuszy, zwanych Block Signers, którzy mogą podpisywać i tworzyć bloki w niezawodny i terminowy sposób. Eliminuje to opóźnienia transakcji procesu PoW Mining, który podlega dużej wariancji czasu bloku ze względu na jego losowy rozkład poisson. Sfederowany proces block signing umożliwia niezawodne tworzenie bloków bez wprowadzania potrzeby zaufania strony trzeciej.


Elements może działać jako Sidechain do innego Blockchain, takiego jak Bitcoin, lub jako samodzielny Blockchain bez zależności od innych sieci.


Gdy jest używany jako Sidechain, Strong Federation zawiera również elementy, które umożliwiają bezpieczny i kontrolowany transfer aktywów między głównym łańcuchem a Elements Sidechain. Kontrolowany transfer aktywów nazywany jest Federated 2-Way Peg, a elementy pełniące rolę transferu aktywów nazywane są watchmen.


Procesy zaangażowane w działanie sieci Elements i role uczestników sieci są ważne dla zrozumienia, jak działa Elements.


Niezależnie od tego, czy jest zaimplementowany jako Sidechain, czy samodzielny Blockchain, Elements wykorzystuje silne federacje sygnatariuszy bloków do tworzenia bloków.


### Silne federacje


Elements wykorzystuje model konsensusu zaproponowany po raz pierwszy przez Blockstream, zwany Strong Federations. Strong Federation nie potrzebuje Proof of Work (PoW) i zamiast tego polega na zbiorowych działaniach grupy wzajemnie nieufnych uczestników, zwanych Functionaries.


Role, jakie może pełnić osoba funkcyjna w ramach Strong Federation, to: Block Signers i watchmen. Sygnatariusze bloków są wymagani w przypadku uruchomienia Elements w trybie Sidechain lub samodzielnym Blockchain, natomiast watchmen są wymagane tylko w konfiguracji Sidechain.


Działania, które może wykonać członek Strong Federation, są podzielone między dwie różne role w celu zwiększenia bezpieczeństwa i ograniczenia szkód, jakie może wyrządzić atakujący.


W połączeniu role tych uczestników pozwalają Elements zapewnić zarówno szybkie tworzenie bloków (szybsze i ostateczne potwierdzenie transakcji), jak i bezpieczne, zbywalne aktywa (aktywa powiązane bezpośrednio z innym Blockchain).


Dokument Strong Federations można przeczytać tutaj: https://blockstream.com/strong-federations.pdf


### Sygnatariusze bloku


Blockchain, podobnie jak Bitcoin, jest przedłużany, gdy każdy, kto stanowi część dynamicznej grupy sygnatariuszy bloków, przedłuża łańcuch, demonstrując zużyty Proof of Work. Dynamiczny charakter zestawu wprowadza kwestie opóźnień nieodłącznie związane z takimi systemami.


Dzięki zastosowaniu stałego zestawu sygnatariuszy model federacyjny zastępuje zestaw dynamiczny znanym zestawem, schematem wielopodpisowym. Zmniejszenie liczby uczestników potrzebnych do rozszerzenia Blockchain zwiększa szybkość i skalowalność systemu, a walidacja przez wszystkie strony zapewnia integralność historii transakcji.


Federated block signing składa się z kilku faz:



- Krok 1 - Sygnatariusze bloków proponują kandydujące bloki w sposób rotacyjny wszystkim innym uczestniczącym sygnatariuszom bloków.



- Krok 2 - Każdy block signer sygnalizuje swój zamiar, wstępnie zobowiązując się do podpisania danego bloku kandydującego.



- Krok 3 - Jeśli dany próg dla pre-Commitment jest spełniony, każdy block signer podpisuje blok.



- Krok 4 - Jeśli próg podpisu (który może różnić się od progu z kroku 3) zostanie osiągnięty, blok zostanie zaakceptowany i wysłany do sieci. Strong Federation osiągnął konsensus w sprawie najnowszego bloku transakcji.



- Krok 5 - Następny blok jest następnie proponowany przez następny block signer w rundzie-robin i proces się powtarza.


Ponieważ generowanie bloków Strong Federation nie jest probabilistyczne i opiera się na stałym zestawie sygnatariuszy, nigdy nie będzie podlegać reorganizacji wielu bloków. Pozwala to na znaczne skrócenie czasu oczekiwania związanego z potwierdzaniem transakcji. Usuwa również zachętę do kopania dla zysku (tj. nagrody za blok) i zastępuje ją zachętą do produktywnego uczestnictwa w sieci, w której wszyscy uczestnicy mają ten sam wspólny cel; zapewnienie, że sieć nadal funkcjonuje w sposób korzystny dla wszystkich. Odbywa się to bez wprowadzania pojedynczego punktu awarii lub wyższych wymagań dotyczących zaufania.


### Elements jako Sidechain - watchmen i Federated 2-Way Peg


Gdy Sidechain jest uruchomiony, niektórzy członkowie Strong Federation mają dodatkową rolę do spełnienia, watchmen. watchmen są odpowiedzialni za transfer aktywów do i z Elements Sidechain, procesy znane jako `Peg-In` i `Peg-Out`.


Aby Sidechain działał w sposób godny zaufania, musi umożliwiać uczestnikom weryfikację, czy Supply aktywów jest kontrolowany i weryfikowalny. Elements Sidechain wykorzystuje 2-drożny Peg Federacyjny, aby umożliwić dwukierunkowy transfer aktywów do i z Elements Blockchain. Spełnia to wymagania dotyczące możliwej do udowodnienia emisji i transferów międzyłańcuchowych.


Funkcja Federated 2-Way Peg umożliwia interoperacyjność aktywów z innymi blockchainami i reprezentowanie natywnych aktywów innego Blockchain. Poprzez powiązanie swojego Blockchain z innym, można rozszerzyć możliwości mainchain i przezwyciężyć niektóre z jego nieodłącznych ograniczeń.


Na wysokim poziomie transfery do Sidechain mają miejsce, gdy ktoś wysyła aktywa mainchain do Address kontrolowanego przez watchmen Wallet z wieloma podpisami. To skutecznie zamraża aktywa na mainchain. Następnie watchmen zatwierdza transakcję i uwalnia taką samą ilość powiązanych aktywów w Sidechain. Zwolnione aktywa są wysyłane do Sidechain Wallet, który może udowodnić roszczenie do oryginalnych aktywów mainchain. Proces ten skutecznie przenosi aktywa z łańcucha nadrzędnego do Sidechain.


Aby przenieść aktywa z powrotem do mainchain, użytkownik dokonuje specjalnej transakcji peg-out na Sidechain. Transakcja ta jest sprawdzana przez watchmen, który następnie podpisuje transakcję wydatkowania z wielopodpisowego Wallet, który kontroluje na mainchain. Próg liczby uczestników federacji musi zostać podpisany, zanim transakcja mainchain stanie się ważna. Gdy watchmen wysyła aktywa z powrotem do mainchain, niszczy również odpowiednią kwotę na Sidechain, skutecznie przenosząc aktywa między łańcuchami bloków.


## Konfiguracja i uruchomienie Elements


<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>


:::video id=1f73dfee-3623-483b-ab42-07d9286ed999:::


Ponieważ Elements opiera się na bazie kodu Bitcoin, komponenty tworzące działającą sieć są bardzo podobne.


Samo oprogramowanie węzła Elements nazywa się `elementsd` i działa jako daemon na komputerze użytkownika. daemon (lub usługa w systemie Windows) to program, który działa jako usługa w tle, nie wymagając bezpośredniej kontroli zalogowanego użytkownika.


Uwaga: W całym tym dokumencie zawsze będziemy odnosić się do elementsd jako wersji daemon, ale wszystko można zrobić za pomocą Elements-qt, pod warunkiem, że opcja serwera jest włączona.


Elements daemon łączy się z innymi węzłami w sieci, dzięki czemu może Exchange dane transakcji i bloków, walidując i rozszerzając swoją lokalną kopię Blockchain sieci.


Oprogramowanie Elements składa się również z programu klienckiego o nazwie `elements-cli`, który umożliwia wysyłanie poleceń zdalnego wywołania procedur (RPC) do elementsd z linii poleceń. Można to wykorzystać na przykład do odpytywania o saldo Wallet, przeglądania danych transakcji lub bloków lub nadawania transakcji. Ta konfiguracja powinna być znana każdemu, kto korzystał z odpowiedników Bitcoin; bitcoind i bitcoin-cli.


Ponieważ węzeł Elements można skonfigurować poprzez przekazanie parametrów podczas uruchamiania lub za pośrednictwem pliku konfiguracyjnego, możliwe jest uruchomienie więcej niż jednej instancji na tej samej maszynie. Jest to przydatne do celów testowych i rozwojowych, ponieważ można skonfigurować własną sieć lokalną na jednym komputerze, przy czym każdy węzeł Elements ma własną kopię danych Blockchain, zarządza własną pulą niepotwierdzonych ważnych transakcji i nasłuchuje żądań RPC na różnych portach.


### Repozytorium kodu Elements i społeczność


Elements jest projektem typu open-source, a jego kod źródłowy można znaleźć w repozytorium Elements GitHub pod adresem https://github.com/ElementsProject/Elements. Repozytorium zawiera źródła programów elementsd i elements-cli wraz z narzędziami do instalacji i kompilacji, zestawem testów i dokumentacją instruktażową.


Uzupełnieniem repozytorium kodu jest strona internetowa https://elementsproject.org, skupiająca się na społeczności i zawierająca wyjaśnienia, czym jest Elements, jak działa oraz obszerną sekcję samouczków. Samouczek koncentruje się na poznawaniu Elements poprzez śledzenie przykładów z wiersza poleceń i pokazuje, jak budować na nim proste aplikacje desktopowe i internetowe. Witryna zawiera również listę popularnych forów dyskusyjnych społeczności Elements i sama jest hostowana na GitHub, umożliwiając społeczności wnoszenie wkładu w zawartość witryny.


Aby uruchomić Elements na swoim komputerze, należy najpierw sklonować (pobrać kopię) kod źródłowy, zainstalować wszelkie zależności, jakie posiada kod, a na koniec zbudować pliki wykonywalne daemon i klienta. Oprogramowanie Elements jest wtedy gotowe do skonfigurowania i uruchomienia.


## Konfigurowanie węzłów i sieci


<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>


Ustawienia konfiguracyjne mogą być przekazywane do węzła Elements podczas uruchamiania w celu zmiany sposobu jego działania, sprawdzania poprawności danych, łączenia się z innymi węzłami i inicjalizacji danych Blockchain.


Ustawienia są ładowane z wyznaczonego pliku `Elements.conf` lub przekazywane jako parametry za pomocą linii poleceń.


Niektóre rzeczy można zmienić za pomocą tych parametrów:



- Nazwa default asset używana w samodzielnych implementacjach Blockchain.
- Numer początkowego utworzonego zasobu.
- Zasób używany do uiszczania opłat transakcyjnych w sieci.
- Miejsce przechowywania plików danych Blockchain.
- Poświadczenia RPC używane do łączenia się z węzłem Bitcoin.
- Próg `n z m`, który musi być spełniony i ważne klucze publiczne, które mogą podpisywać bloki.
- Skrypt, który musi zostać spełniony w celu przeniesienia zasobów do i z Sidechain.
- Czy połączyć się z węzłem Bitcoin jako Sidechain, czy nie.


Wiele z nich stanowi część zasad konsensusu sieci, dlatego ważne jest, aby były one stosowane we wszystkich węzłach podczas uruchamiania. Niektóre z nich można zmienić po zainicjowaniu łańcucha, ale niektóre muszą zostać naprawione po ich użyciu do zainicjowania łańcucha.


Korzystanie z parametrów zostanie omówione w dalszej części kursu, gdy będą one związane z każdą sekcją.


### Podstawowe operacje przy użyciu wiersza poleceń


Ten kurs pokaże przykłady, które używają programu `elements-cli` do wykonywania połączeń RPC do jednego lub więcej węzłów Elements. Odbywa się to z sesji terminala i w celu skrócenia poleceń zostanie użyty `alias`. Zgodnie z tą konwencją, gdy zobaczysz coś takiego jak następujące polecenia:


```bash
e1-dae

e1-cli getnewaddress
```


`e1-dae` i `e1-CLI` są w rzeczywistości skrótem typograficznym, który wykorzystuje funkcję `alias` terminala. `e1-dae` i `e1-CLI` zostaną faktycznie zastąpione podczas wykonywania polecenia, a polecenie, które zostanie uruchomione będzie podobne do:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```


To, co widzimy powyżej, to wywołanie uruchomienia Elements daemon i wywołanie programów elements-cli znajdujących się w katalogu `$HOME/Elements/src` oraz wartość parametru `datadir`. Parametr `datadir` pozwala nam powiedzieć instancjom daemon i klienta, gdzie zlokalizować ich pliki konfiguracyjne, a w przypadku daemon, gdzie przechowywać jego kopię Blockchain. Ponieważ współdzielą one plik konfiguracyjny, klient będzie mógł wykonywać połączenia RPC do daemon.


Uruchamiając powyższe polecenie ponownie, ale z inną wartością `datadir`, możemy uruchomić więcej niż jedną instancję Elements, każdą z własną kopią Blockchain i ustawieniami konfiguracyjnymi. Zgodnie z tą konwencją będziemy używać aliasów `e2-dae` i `e2-CLI` w kursie, aby odnieść się do innego katalogu datadir niż e1. Tak więc powyższy przykład dla naszej drugiej instancji `e2` wyglądałby następująco:


```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2

$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```


Pozwoli nam to na wykonywanie wszelkiego rodzaju operacji, takich jak transakcje aktywów między węzłami, wydawanie aktywów i sprawdzanie użycia zaślepienia w Confidential Transactions między różnymi węzłami w tej samej sieci.


# Używanie elementu Praktyczny przypadek użycia


<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>


## Confidential Transactions


<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>


:::video id=ea2121b6-24a8-458d-91e6-0c92eaf4dc65:::


W tej sekcji dowiesz się, jak korzystać z funkcji Confidential Transactions w Elements.


Wszystkie adresy w Elements są domyślnie blinded przy użyciu Confidential Transactions, dzięki czemu ilość i rodzaj przeniesionych aktywów są widoczne tylko dla uczestników transakcji (i tych, którym zdecydują się ujawnić klucz zaślepiający), jednocześnie gwarantując kryptograficznie, że nie można wydać więcej monet niż jest dostępnych.


### Adresy poufne i Confidential Transactions


Domyślnie, po utworzeniu nowego Address w Elements za pomocą polecenia `getnewaddress`, jest on tworzony jako poufny Address.


Aby zademonstrować Confidential Transactions, poprosimy e2 o wysłanie sobie środków, a następnie spróbujemy wyświetlić transakcję z e1. Zademonstruje to poufny charakter transakcji w Elements.


Każdy nowy Address wygenerowany przez węzeł Elements jest domyślnie poufny. Możemy to zademonstrować, wysyłając e2 do generate nowy Address.


```
e2-cli getnewaddress
```


Należy zauważyć, że Address zaczyna się od e1. To identyfikuje go jako poufny Address. Bardziej szczegółowe sprawdzenie Address za pomocą polecenia getaddressinfo pokazuje więcej szczegółów Address.


```
e2-cli getaddressinfo <address>
```


Widać, że istnieje właściwość confidential_key, która mówi nam, że jest to poufny Address.


Poufny_klucz to publiczny klucz zaślepiający, który jest dodawany do samego poufnego Address. Jest to powód, dla którego poufny Address jest tak długi.


Ma również powiązany jawny Address. Jeśli chcesz używać zwykłych, jawnych transakcji w Elements, aktywa powinny być wysyłane do tego Address zamiast do tego z prefiksem lq1.


Możemy teraz zlecić e2 wysłanie środków na wygenerowany przez siebie Address. To później pokaże, że e1, ponieważ nie jest jedną ze stron transakcji, nie będzie w stanie wyświetlić szczegółów transakcji.


```
e2-cli sendtoaddress <address>
```


Zanotuj transaction ID. Potwierdź transakcję.


```
e2-cli -generate 101
```


Patrząc na transakcję, w której e2 wysłało pewne środki do siebie z perspektywy samego e2.


```
e2-cli gettransaction <txid>
```


Przewijając w górę szczegóły transakcji, można zobaczyć, że e2 może wyświetlać kwoty wysłane i otrzymane, a także aktywa będące przedmiotem transakcji. Możesz również zobaczyć właściwości amountblinder i assetblinder, które są używane do blokowania szczegółów z innych węzłów niezaangażowanych w transakcję.


Aby sprawdzić szczegóły tej samej transakcji z e1, musimy najpierw uzyskać nieprzetworzone szczegóły transakcji.


```
e1-cli getrawtransaction <txid>
```


To zwraca nieprzetworzone szczegóły transakcji. Jeśli spojrzysz na sekcję vout, zobaczysz, że istnieją trzy instancje. Pierwsze dwie instancje to kwoty otrzymania i zmiany, a trzecia to opłata transakcyjna. Z tych trzech kwot opłata jest jedyną, w której można zobaczyć wartość, ponieważ sama opłata jest zawsze unblinded w Elements.


### Oślepiające klucze


Pierwsze dwie sekcje vout pokazują "zakresy blinded" kwot wartości i dane Commitment, które działają jako dowód rzeczywistej kwoty i rodzaju aktywów będących przedmiotem transakcji.


Nawet gdybyśmy zaimportowali klucz prywatny e2 do Wallet e1, nadal nie byłby on w stanie zobaczyć kwot i rodzaju aktywów będących przedmiotem transakcji, ponieważ nadal nie ma wiedzy o kluczu zaślepiającym używanym przez e2. Udowodnimy to, importując klucz prywatny używany przez Wallet e2 do Wallet e1. Najpierw musimy wyeksportować klucz z e2


```
e2-cli dumpprivkey <address>
```


Następnie zaimportuj go do e1.


```
e1-cli importprivkey <privkey>
```


Teraz możemy udowodnić, że e1 nadal nie widzi wartości.


```
e1-cli gettransaction <txid>
```


Rzeczywiście, pokazuje 0 jako wartość tx, podczas gdy w rzeczywistości było to 1.


Aby móc zobaczyć rzeczywistą wartość bez zaślepienia, potrzebujemy klucza zaślepienia. Aby to zrobić, najpierw eksportujemy klucz zaślepienia z e2.


```
e2-cli dumpblindingkey <address>
```


Następnie zaimportuj go do e1.


```
e1-cli importblindingkey <address> <blinding key>
```


Teraz, gdy otrzymamy szczegóły transakcji z e1.


```
e1-cli gettransaction <txid>
```


Pokazuje, że po zaimportowaniu klucza oślepiającego możemy teraz wyświetlić rzeczywistą wartość 1 w transakcji.


W tej sekcji zobaczyliśmy, że użycie klucza zaślepiającego ukrywa kwotę i rodzaj aktywów w transakcji, a importując odpowiedni klucz zaślepiający, możemy ujawnić te wartości. W praktyce klucz zaślepiający może na przykład zostać przekazany audytorowi, jeśli zajdzie potrzeba zweryfikowania kwot i rodzajów aktywów posiadanych przez stronę. Funkcja Confidential Transactions w Elements umożliwia również przeprowadzanie "dowodów zakresu". Dowody zakresu mogą udowodnić, że kwota składnika aktywów mieści się w danym zakresie, bez konieczności ujawniania samej kwoty.


Widzieliśmy również, że Confidential Transactions są opcjonalne, ale włączane domyślnie, gdy generowany jest nowy Address.


To wszystko na tę lekcję; powodzenia w quizie i do zobaczenia w następnej!


## Issued Assets


<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>


:::video id=7ac63148-d730-496d-85d4-0032aaf09be1:::


W tej sekcji dowiesz się, jak korzystać z funkcji Issued Assets w Elements.


Issued Assets umożliwia wydawanie i przekazywanie wielu rodzajów aktywów pomiędzy uczestnikami sieci Elements. Każdy węzeł w sieci może emitować własne aktywa. Emisje mogą reprezentować zamienne Ownership dowolne aktywa, w tym bony, kupony, waluty, depozyty, obligacje, akcje itp. Issued Assets otwiera drzwi do budowania giełd Trustless, opcji i innych zaawansowanych inteligentnych kontraktów obejmujących samodzielne Issued Assets.


Wyemitowane aktywa również korzystają z Confidential Transactions i mogą być ponownie wydane przez każdego, kto posiada powiązany token.


Pierwszym krokiem jest uzyskanie dostępu do dwóch węzłów Elements, które nazwiemy e1 i e2. Węzły te zresetowały swoje łańcuchy bloków, a default asset został między nimi podzielony.


Oba węzły znajdują się w tej samej sieci lokalnej i są ze sobą połączone, a zatem współdzielą te same transakcje w swoich transakcyjnych Mempool i identycznych łańcuchach bloków. Chociaż działają na tej samej maszynie, warto zauważyć, że nie współdzielą tych samych rzeczywistych plików Blockchain. Każdy węzeł zarządza własną lokalną kopią Blockchain, która zawiera tę samą historię transakcji, ponieważ są one w konsensusie i przestrzegają tych samych zasad protokołu, co każdy inny.


Zacznijmy od sprawdzenia widoku każdego węzła na istniejące emisje aktywów w sieci.


Odbywa się to za pomocą polecenia listissuances.


```
e1-cli listissuances

e2-cli listissuances
```


Jak widać, oba węzły pokazują tę samą historię emisji. Oba wyświetlają jeden zasób, początkową emisję 21 milionów Bitcoin, które zostały utworzone podczas inicjalizacji on chain. Możesz zobaczyć identyfikator szesnastkowy zasobu w wynikach uruchomienia powyższego polecenia, a także etykietę przypisaną do zasobu, która brzmi "Bitcoin".


Warto zauważyć, że default asset zawsze otrzymuje etykietę podczas inicjalizacji łańcucha. Podczas wydawania własnych zasobów można samodzielnie ustawić dla nich etykiety, co wkrótce zrobimy. Zanim to zrobimy, musimy wydać nasz własny zasób.


Poprosimy e1 o wydanie nowego zasobu. Odbywa się to za pomocą polecenia issueasset.


```
e1-cli issueasset 100 1 false
```


`issueasset` akceptuje 3 parametry.


Ilość nowego aktywa do wydania, użyliśmy 100. Ilość tokenów do utworzenia (tokeny są używane do ponownego wydawania ilości aktywów), z których wybraliśmy 1. Ostatni parametr mówi Elements, aby utworzył emisję aktywów jako blinded lub unblinded. Użyjemy unblinded, ponieważ za chwilę chcemy wyświetlić kwoty emisji z e2, więc wprowadzimy wartość false.


Uruchomienie polecenia zwraca dane dotyczące wydania. Obejmują one transaction ID, którego kopię można pobrać do późniejszego wykorzystania, unikalną wartość szesnastkową zasobu i unikalną wartość szesnastkową tokena zasobu.


generate blok potwierdzający transakcję wydania.


```
e1-cli -generate 1
```


Uruchom ponownie polecenie `listissuances` dla e1.


```
e1-cli listissuances
```


To pokazuje nam, że e1 jest teraz świadomy 2 emisji, początkowej emisji Bitcoin i naszego nowo wyemitowanego zasobu, którego widzimy 100. Zwróć uwagę na wartość heksadecymalną nowego aktywa i brak powiązanej etykiety aktywa, tak jak w przypadku emisji Bitcoin.


Sprawdź ponownie listę znanych wydań e2.


```
e2-cli listissuances
```


To pokazuje nam, że e2 nie jest świadomy emisji aktywów dokonanej przez e1. Widzi tylko początkową emisję Bitcoin, którą mógł już zobaczyć.


Dzieje się tak, ponieważ e2 nie jest świadomy i nie obserwuje Address, do którego nowy zasób został wysłany, gdy został wydany przez e1.


Warto zauważyć, że nawet jeśli e2 nie widzi samej emisji, e1 może nadal wysyłać e2 część aktywów. Nowy składnik aktywów pojawiłby się wówczas jako dostępne saldo w Wallet e2, nawet jeśli nie jest on świadomy pierwotnej emisji.


Aby umożliwić e2 zobaczenie rzeczywistego wydania (a zatem wydanej kwoty), musimy dodać Address do e2 jako obserwowany Address.


Aby to zrobić, musimy znaleźć Address, do którego został wysłany zasób. W tym celu użyjemy transaction ID, który skopiowaliśmy wcześniej i poprosimy e1 o pobranie szczegółów tej transakcji, abyśmy mogli znaleźć właściwy Address, aby dodać go do listy obserwowanych Wallet w e2.


```
e1-cli gettransaction <the-issuance-transaction-id>
```


Przewijając w górę dane transakcji, zobaczysz Address, który otrzymał 100 naszych nowych zasobów, zidentyfikowanych przez jego wartość heksadecymalną.


Weź Address i skopiuj go, abyśmy mogli zaimportować go do e2.


Teraz zaimportujmy Address do e2. Aby to zrobić, użyjemy polecenia importaddress.


```
e2-cli importaddress <the-issued-to-address>
```


Jeśli teraz sprawdzimy listę emisji e2.


```
e2-cli listissuances
```


Widać, że nasz nowo wyemitowany zasób znajduje się teraz na liście. Węzeł e2 jest również w stanie określić kwotę aktywa, które zostało wyemitowane, wraz z kwotą powiązanego tokena, ponieważ emisja była emisją unblinded. Aby umożliwić użycie identyfikatora zasobu do mapowania nazw w Elements, najpierw zatrzymaj Elements.


```
e1-cli stop
```


Następnie uruchamiamy go ponownie z dodatkowym parametrem, który mapuje szesnastkowy kod zasobu na podaną etykietę. Umożliwia to węzłowi wyświetlanie nam danych o zasobie w bardziej czytelnym dla człowieka formacie. Jeśli wolisz, możesz dodać to na końcu Elements.conf, wtedy nie musisz dodawać argumentu do daemon za każdym razem, gdy go uruchamiasz. Na przykład:


```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```


Ale użyjemy tutaj metody argumentów.


```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```


Ponowne zapytanie węzła o listę wydań.


```
e1-cli listissuances
```


To pokazuje, że mapowanie wartości szesnastkowej zasobu na jego etykietę działa. Ponownie sprawdzamy listę wydań węzła e2.


```
e2-cli listissuances
```


Widać, że węzeł e2 nie ma dostępu do tej etykiety, ponieważ etykiety są dostępne tylko dla węzła, który je ustawił. Rzeczywiście, możemy przypisać inną etykietę do tego samego zasobu hex w węźle e2 niż w węźle e1. Najpierw zatrzymaj węzeł e2.


```
e2-cli stop
```


Ponowne uruchomienie z inną etykietą przypisaną do szesnastki naszego nowego zasobu.


```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```


Notowania emisji z e2.


```
e2-cli listissuances
```


Etykiety zasobów są lokalne dla każdego węzła, tylko sześciokąt zasobu jest rozpoznawany przez inne węzły w sieci.


Mapowanie etykiety na sześciokąt zasobu jest przydatne podczas wykonywania działań, takich jak transakcje i zapytania o saldo Wallet, ponieważ umożliwia skrócony sposób odwoływania się do zasobu. Na przykład, gdybyśmy chcieli wysłać część naszego nowego zasobu (kwotę 10) z e1 do e2 bez użycia etykiety.


Najpierw musimy uzyskać Address, aby wysłać zasób.


```
e2-cli getnewaddress
```


Następnie należy użyć polecenia sendtoaddress.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```


Potwierdź transakcję, generując blok.


```
generate 1
```


Sprawdzenie, czy zasób został odebrany na e2.


```
e2-cli getwalletinfo
```


Widzimy, że zasób rzeczywiście został odebrany.


Należy zauważyć, że e2 mapuje szesnastkowy kod odebranego zasobu i wyświetla go przy użyciu własnej etykiety. Łatwiejszym sposobem na zrobienie tego samego byłoby użycie etykiety zasobu e1 podczas wysyłania.


```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```


Za kulisami Elements mapuje lokalne etykiety na wartości szesnastkowe, aby uprościć korzystanie z Issued Assets.


W tej sekcji zobaczyliśmy, jak wydawać i oznaczać zasoby. W następnej sekcji przyjrzymy się ponownemu wydawaniu i niszczeniu ilości wydanego zasobu.


## Reemisja aktywów


<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>


:::video id=7df967b0-ffff-42e1-b1d5-868e76289faf:::


W tej sekcji dowiesz się, jak wyemitować więcej już wyemitowanego zasobu, a także jak zniszczyć daną ilość wyemitowanego zasobu.


Potrzeba ponownego wydania (utworzenia większej ilości) składnika aktywów lub zniszczenia jego ilości jest czymś, co może wystąpić, gdy składnik aktywów reprezentuje coś, co nie ma stałego Supply. Może to mieć zastosowanie na przykład do aktywów reprezentujących złoto przechowywane w skarbcu; gdy jednostki złota wpływają i wypływają ze skarbca, aktywa reprezentujące Supply skarbca muszą zostać odpowiednio skorygowane w górę lub w dół.


Ponowne wydanie kwoty aktywa wymaga Ownership powiązanego tokena, który został utworzony wraz z aktywem, gdy został pierwotnie wydany.


Podczas tworzenia większej ilości zasobu nie ma znaczenia, który węzeł wystawił zasób w pierwszej kolejności, o ile węzeł, który ponownie wystawia ilość zasobu, jest w posiadaniu tego, co jest powszechnie nazywane reissuance token zasobu. Przyjrzymy się, jak początkowo utworzyć reissuance token, jak użyć go do ponownego wydania ilości zasobu, a także jak przenieść reissuance token do innych węzłów, aby miały one również uprawnienia do ponownego wydania zasobu.


Będziemy potrzebować dostępu do dwóch węzłów Elements, które nazwiemy e1 i e2. Węzły te zresetowały swoje łańcuchy bloków, a default asset został między nimi podzielony.


W e1 wyemitujemy 100 sztuk nowego aktywa i utworzymy 1 reissuance token dla tego samego aktywa. Utworzymy emisję jako unblinded w celu uproszczenia przykładu. Przejdźmy więc do emisji aktywa i powiązanego z nim reissuance token.


```
e1-cli issueasset 100 1 false
```


Zwróć uwagę na identyfikator zasobu, a także identyfikator tokena (ponownego wydania).


Ponieważ później będziemy ponownie wydawać więcej zasobów z e2, będziemy musieli zanotować transaction ID, w którym zasób został wydany i użyć go do zaimportowania Address, do którego zasób został wysłany.


Potwierdź transakcję.


```
e1-cli -generate 1
```


Sprawdzimy teraz szczegóły transakcji za pomocą polecenia gettransaction:


```
e1-cli gettransaction <txid>
```


Przewijając w górę dane transakcji, zobaczysz, że w transakcji e1 otrzymał 1 reissuance token i 100 powiązanych aktywów.


Zrób kopię Address, abyśmy mogli zaimportować ją do e2.


A teraz import Address do Wallet e2.


```
e2-cli importaddress <address>
```


Widzimy teraz, że zarówno e1, jak i e2 są świadome emisji aktywów.


```
e1-cli listissuances

e2-cli listissuances
```


Obecnie e1 posiada kwotę aktywów i 1 reissuance token, ale e2 nie.


```
e1-cli getwalletinfo
```


Należy również zauważyć, że e1 ma mniej default asset niż wcześniej, ponieważ zapłacił niewielką kwotę na pokrycie opłat transakcyjnych. Kwota ta ma zostać pobrana przez e1, gdy utworzony blok zostanie dojrzały na głębokości ponad 100 bloków.


```
e2-cli getwalletinfo
```


Ponieważ e1 posiada reissuance token, może wydać ich więcej. Odbywa się to za pomocą polecenia reissueasset. Niech e1 ponownie wyda kolejne 100 sztuk tego zasobu.


```
e1-cli reissueasset <asset-id> 100
```


Sprawdzenie ponownego wydania zadziałało.


```
e1-cli getwalletinfo
```


Widać, że e1 posiada teraz 200 aktywów, zgodnie z oczekiwaniami.


Ponieważ e2 nie posiada kwoty reissuance token, otrzymają błąd, jeśli spróbują ponownie wydać zasób.


```
e2-cli reissueasset <asset-id> 100
```


Zwróć uwagę na komunikat o błędzie.


Możemy wyświetlić szczegóły ponownego wydania z e1 za pomocą polecenia listissuances.


```
e1-cli listissuances
```


Zwróć uwagę na flagę `is_reissuance`.


Jeśli teraz wyślemy e2 kwotę reissuance token, będą mogli sami ponownie wydać kwotę aktywa. Najpierw potrzebujemy Address, aby go wysłać. Warto zauważyć, że reissuance token jest traktowany tak samo jak każdy inny zasób w Elements podczas wysyłania i wyświetlania sald oraz że można go również podzielić na mniejsze nominały, jak każdy inny zasób, więc nie musimy wysyłać 1 reissuance token do e2, aby mógł on ponownie wystawić zasób. Wystarczy dowolny nominał. Generowanie Address dla e2 w celu otrzymania reissuance token.


```
e2-cli getnewaddress
```


Następnie wyślij część RIT z e1 do e2.


```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Potwierdź transakcję.


```
e1-cli -generate 1
```


Widzimy teraz, że e2 utrzymuje 0,1, które zostało wysłane.


```
e2-cli getwalletinfo
```


Oznacza to, że e2 może teraz ponownie wydać więcej aktywów powiązanych z RIT, które posiada w swoim Wallet. E2 ponownie wyda 500 aktywów.


```
e2-cli reissueasset <asset-id> 500
```


Sprawdź wynik ponownego wydania.


```
e2-cli getwalletinfo
```


Widać, że e2 utrzymuje teraz ponownie wydaną kwotę w swoim saldzie Wallet, a sam RIT nie jest zużywany w procesie ponownego wydania aktywów.


Zniszczenie kwoty aktywów jest czymś, co może zrobić każdy, kto posiada co najmniej kwotę, która ma zostać zniszczona, nie jest to regulowane przez reissuance token.


```
e2-cli destroyamount <asset-id>

e2-cli getwalletinfo
```


W tej sekcji zobaczyliśmy, jak wyemitować aktywo, a także jak wykorzystać reissuance token, który jest opcjonalnie tworzony jako część emisji aktywa. Zobaczyliśmy również, że transfer reissuance token jest tak prosty, jak transfer dowolnego innego aktywa, a posiadanie dowolnej ilości reissuance token daje posiadaczowi prawo do emisji większej ilości powiązanego aktywa. Dlatego bardzo ważne jest kontrolowanie, kto ma dostęp do tokenów reemisji w sieci. Widzieliśmy również, jak zniszczyć ilość aktywów i że proces ten nie jest kontrolowany przez posiadanie reissuance token.


# Element Federation


<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>


## block signing


<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>


:::video id=c5a81820-77d7-4a0c-9a4e-9323386a74ac:::


Elements obsługuje federacyjny model podpisywania, który umożliwia określenie liczby członków Strong Federation, którzy muszą podpisać proponowany blok w celu utworzenia ważnego bloku.


Wcześniej, dla ułatwienia, tworzyliśmy bloki za pomocą polecenia `generate`, które nie musiało spełniać wymogu wielopodpisu, aby utworzone bloki zostały zaakceptowane przez sieć jako ważne.


Skonfigurujemy nasze węzły tak, aby wymagały tworzenia bloków Multisig 2 na 2. Zostanie to skonfigurowane przy użyciu parametru signblockscript, który można dodać do pliku konfiguracyjnego lub przekazać do węzła podczas uruchamiania. Aby zainicjować łańcuch z tym parametrem, musimy najpierw zbudować skrypt, z którego się składa.


Zrobimy to przy użyciu niektórych istniejących węzłów, zapiszemy dane wyjściowe, a następnie wyczyścimy łańcuch, abyśmy mogli go ponownie uruchomić przy użyciu naszego parametru signblockscript. Jest to konieczne, ponieważ skrypt stanowi część reguł konsensusu sieci i będzie musiał zostać ustawiony podczas inicjalizacji on chain. Nie można go dodać w późniejszym terminie do już istniejącego łańcucha.


Będziemy potrzebować dostępu do dwóch węzłów Elements, które nazwiemy e1 i e2. Węzły te zresetowały swoje łańcuchy bloków, a default asset został między nimi podzielony.


Upewnij się, że parametr con_max_block_sig_size jest ustawiony na wysoką wartość w pliku Elements.conf, w przeciwnym razie block signing nie powiedzie się w dalszej części tej sekcji. W tym samouczku ustawiliśmy con_max_block_sig_size=2000.


Ponieważ będziemy resetować Blockchain i czyścić portfele powiązane z e1 i e2, będziemy musieli wykonać kopię adresów, kluczy publicznych i kluczy prywatnych, których używamy do generate skryptu block signing, abyśmy mogli z nich skorzystać później.


Po pierwsze, potrzebujemy każdego z węzłów block signing do generate nowego Address, którego kopię należy wykonać.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


Następnie musimy wyodrębnić klucze publiczne z adresów i zapisać je do późniejszego wykorzystania.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


Następnie wyodrębnij klucze prywatne, które później ponownie zaimportujemy, aby węzły mogły podpisać bloki po ponownej inicjalizacji naszych danych Blockchain i Wallet.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


Teraz musimy generate skrypt Redeem z wymaganiami multi-signature 2 z 2. Robimy to za pomocą polecenia createmultisig i przekazując pierwszy parametr jako 2, a następnie dostarczając dwa klucze publiczne. To właśnie te klucze Ownership musi udowodnić później, gdy blok zostanie utworzony.


Każdy węzeł, e1 lub e2, może generate z Multisig.


```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```


W ten sposób otrzymujemy redeemscript, który można skopiować do późniejszego wykorzystania.


Teraz musimy wyczyścić istniejące dane Blockchain i Wallet, abyśmy mogli zacząć od nowa z nowym signblockscript jako częścią reguł konsensusu łańcucha. Właśnie dlatego musieliśmy wcześniej wykonać kopię niektórych danych, takich jak klucze prywatne, które będą używane w nowym łańcuchu do podpisywania bloków. Należy to zrobić przed kontynuowaniem.


Po usunięciu istniejących danych Wallet i łańcucha możemy teraz uruchomić nasze węzły i zainicjować nowy łańcuch za pomocą parametru signblockscript. Przekażmy -evbparams=dynafed:0:::, aby wyłączyć aktywację dynafed, ponieważ nie potrzebujemy tej zaawansowanej funkcji w tym przykładzie.


```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::

e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```


Teraz musimy zaimportować klucze prywatne, które zapisaliśmy wcześniej, aby nasze węzły mogły podpisywać i pomagać w wypełnianiu proponowanych bloków.


```
e1-cli importprivkey <e1-priv-key>

e2-cli importprivkey <e2-priv-key>
```


Użycie polecenia generate powinno teraz powodować błąd, ponieważ nie spełnia ono wymaganych reguł block signing, które są teraz wymuszane przez nasze węzły.


```
e1-cli -generate 1
```


Aby zaproponować nowy blok, każdy węzeł może wywołać polecenie getnewblockhex. Zwraca ono hex nowego bloku, który będzie wymagał podpisania, zanim zostanie zaakceptowany przez jakiekolwiek węzły w naszej sieci.


```
e1-cli getnewblockhex
```


Należy pamiętać, że polecenie to tworzy tylko proponowany blok, a nie generate.


Aby to potwierdzić, widzimy, że w naszym Blockchain nie ma obecnie żadnych bloków.


```
e1-cli getblockcount
```


Jeśli spróbujemy przesłać blok hex bez wcześniejszego podpisania go.


```
e1-cli submitblock <block-hex>
```


Otrzymujemy komunikat informujący nas, że dowód bloku jest nieważny. Dzieje się tak, ponieważ nie został on jeszcze podpisany przez 2 z wymaganych 2 stron.


Niech więc e1 podpisze proponowany blok.


```
e1-cli signblock <block-hex>
```


Niech e2 podpisze heks.


```
e2-cli signblock <block-hex>
```


Zauważ, że e2 nie podpisuje danych wyjściowych utworzonych przez e1 podpisującego proponowany blok. Oboje podpisują proponowany blok hex niezależnie od swoich wyników.


Teraz musimy połączyć podpisy bloków e1 i e2. Każdy węzeł może to zrobić, wszystko czego potrzebuje to podpisany blok hex z drugiego węzła.


```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```


Widać, że polecenie combineblocksigs wyświetla szesnastkowy podpisany blok, a także status complete, informujący nas, że szesnastkowy blok jest gotowy do przesłania.


Teraz każdy węzeł może przesłać ukończony blok hex. Zrobi to węzeł e1.


```
e1-cli submitblock <combined-signed-hex>
```


Sprawdzenie, czy zgłoszenie było prawidłowe.


```
e1-cli getblockcount

e2-cli getblockcount
```


Widać, że zarówno e1, jak i e2 zaakceptowały blok jako prawidłowy i dodały go do końcówki swoich lokalnych kopii Blockchain.


Podsumowując proces. W tej sekcji mamy:


- Zaproponowano blok.
- Każdy węzeł musiał go podpisać.
- Połączone podpisy.
- Sprawdzono, czy podpisy są prawidłowe i spełniają próg redeemscript łańcucha.
- Zgłosił blok.


Każdy węzeł w sieci zatwierdził blok i dodał go do swojej lokalnej kopii Blockchain.


### block signing


Choć początkowo proces ten wydaje się skomplikowany, sekwencja block signing w Elements jest zawsze taka sama, a początkową konfigurację należy przeprowadzić tylko raz:


1. Konfiguracja początkowa (wykonywana raz)

2. Tworzony jest wielopodpisowy Address o nazwie `signblockscript` przy użyciu kluczy publicznych Federated Block Signers.

3. Skrypt Redeem jest używany do uruchomienia nowego Blockchain.

4. Produkcja blokowa (w toku)

5. Proponowane bloki są generowane i wymieniane w celu podpisania.


Po podpisaniu proponowanego bloku przez określoną liczbę sygnatariuszy jest on łączony i przesyłany do sieci. Jeśli spełnia kryteria łańcucha `signblockscript`, węzły akceptują go jako prawidłowy blok.


## Element jako łańcuch boczny


<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>


:::video id=c15e7eaf-9b5d-4696-bb36-bd10e7b56967:::


Elements to platforma Blockchain o otwartym kodzie źródłowym, ogólnego przeznaczenia, która może być również "podłączona" do istniejącego Blockchain, takiego jak Bitcoin. Po podłączeniu do innego Blockchain, mówi się, że Elements działa jako `Sidechain`. Łańcuchy boczne umożliwiają dwukierunkowy transfer aktywów z jednego łańcucha do drugiego. Wdrożenie Elements jako Sidechain pozwala obejść niektóre z nieodłącznych ograniczeń mainchain, zachowując przy tym wysoki stopień bezpieczeństwa zapewniany przez aktywa zabezpieczone na mainchain.


Podczas gdy Sidechain jest świadomy mainchain i jego historii transakcji, mainchain nie ma świadomości Sidechain i żadna nie jest wymagana do jego działania. Umożliwia to łańcuchom bocznym wprowadzanie innowacji bez ograniczeń lub opóźnień związanych z propozycjami ulepszeń protokołu mainchain. Zamiast próbować zmienić go bezpośrednio, rozszerzenie głównego protokołu pozwala samemu mainchain pozostać bezpiecznym i wyspecjalizowanym, stanowiąc podstawę płynnego działania Sidechain.


Rozszerzając funkcjonalność Bitcoin i wykorzystując jego bazowe zabezpieczenia, Sidechain oparty na Elements jest w stanie zapewnić nowe funkcje, które wcześniej nie były dostępne dla użytkowników mainchain. Przykładem Sidechain opartego na Elements w użyciu produkcyjnym jest Liquid Network.


Aby zainicjować Elements Blockchain jako Sidechain, musimy użyć parametru federated peg script. Parametr ten można ustawić w pliku konfiguracyjnym węzła lub przekazać podczas uruchamiania.


federated peg script definiuje, którzy członkowie Strong Federation mogą wykonywać funkcje peg-in i peg-out. Te osoby funkcyjne są określane jako `watchmen`, ponieważ obserwują mainchain i Sidechain pod kątem ważnych transakcji peg-in i peg-out i wykonują je, jeśli są ważne. Określenie "peg-out" oznacza przeniesienie powiązanych aktywów z Sidechain do mainchain, a "peg-in" oznacza przeniesienie powiązanych aktywów do Sidechain z mainchain. Kiedy mówimy "przenieść do Sidechain", w rzeczywistości mamy na myśli to, że środki zostają zablokowane w Address z wieloma podpisami na mainchain, a odpowiednia kwota aktywów jest tworzona na Elements Sidechain. Kiedy mówimy "wyjdź z Sidechain", mamy na myśli, że aktywa są niszczone na Elements Sidechain, a odpowiednia kwota jest uwalniana z zablokowanych środków przechowywanych na mainchain. Zezwolenie na wykonywanie funkcji peg-in i peg-out wymaga, aby osoby funkcyjne udowodniły Ownership kluczy publicznych używanych w federated peg script. Odbywa się to za pomocą odpowiednich kluczy prywatnych.


Aby utworzyć federated peg script, musimy najpierw mieć klucz publiczny generate dla każdego z naszych węzłów. Musimy również przechowywać powiązane klucze prywatne do późniejszego wykorzystania, ponieważ będziemy musieli wyczyścić wszelkie istniejące dane łańcucha i zainicjować nowy łańcuch przy użyciu federated peg script. Wynika to z faktu, że federated peg script stanowi część zasad konsensusu Sidechain i nie można go zastosować do istniejącego, niepegged, Blockchain w późniejszym terminie.


Tak więc generate i Address z każdym z naszych węzłów, przechowują odpowiednie dane do późniejszego wykorzystania i generate federated peg script, którego użyjemy do zainicjowania naszego Sidechain później.


Najpierw każdy z naszych węzłów, który będzie działał jako watchmen w naszej sieci, musi generate nowy Address.


```
e1-cli getnewaddress

e2-cli getnewaddress
```


Następnie walidujemy Address, aby uzyskać klucze publiczne.


```
e1-cli getaddressinfo <e1-address>

e2-cli getaddressinfo <e2-address>
```


A następnie pobrać klucze prywatne powiązane z każdym Address.


```
e1-cli dumpprivkey <e1-address>

e2-cli dumpprivkey <e2-address>
```


Przechowuj klucze prywatne i publiczne do późniejszego wykorzystania.


Teraz musimy wyczyścić istniejące dane Blockchain i Wallet, ponieważ będziemy inicjować nowy łańcuch przy użyciu federated peg script. Można to zrobić teraz. Nie zapomnij uruchomić Bitcoin daemon, który będziemy musieli wpiąć.


Teraz możemy zainicjować nowy łańcuch za pomocą federated peg script utworzonego przy użyciu kluczy publicznych, które zapisaliśmy wcześniej. Liczby, które wprowadzamy i które otaczają nasze klucze publiczne, definiują i ograniczają liczbę używanych kluczy oraz klucz Ownership, który musi zostać udowodniony w celu wpięcia i wypięcia naszego Sidechain.


```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae

e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```


Teraz zaimportujemy klucze prywatne, które zapisaliśmy wcześniej, aby nasze węzły mogły później podpisać i zakończyć transfer aktywów między łańcuchami i spełnić wymagania federated peg script.


```
e1-cli importprivkey <priv-key-1>

e2-cli importprivkey <priv-key-1>
```


Teraz musimy dojrzeć niektóre bloki w obu łańcuchach. Dojrzałość bloków jest wymogiem procesu peg, ponieważ chroni przed reorganizacją bloków na mainchain prowadzącą do inflacji pegged asset Supply w Sidechain.


Aby ta sekcja skupiała się na kołku federacyjnym, będziemy generować bloki bez użycia modelu block signing, któremu przyjrzeliśmy się w ostatniej sekcji, i powrócimy do używania polecenia "generate" do tworzenia nowych bloków.


```
b-cli generate 101

e1-cli generate 1
```


Niekoniecznie potrzebujemy teraz bloków generate dla Elements. Ale i tak zróbmy generate. To dobra praktyka, aby uniknąć potencjalnych niespójności.


Teraz nasz łańcuch jest gotowy do peg-in. W celu peg-in musimy generate specjalny rodzaj Address przy użyciu komendy getpeginaddress. Należy pamiętać, że czas pomiędzy wygenerowaniem peg-in Address za pomocą getpeginaddress i odebraniem go za pomocą claimpegin powinien być jak najkrótszy. Adresy peg-in nie są trwałe i nie powinny być ponownie wykorzystywane.


```
e1-cli getpeginaddress
```


Widać, że polecenie tworzy nowy mainchain Address, a także nowy skrypt, który będzie wymagał zaspokojenia w celu odebrania środków z peg-in. mainchain Address jest skryptem Hash, który będzie używany przez funkcjonariuszy pełniących rolę watchmen w sieci Elements.


Podobnie jak getnewaddress, getpeginaddress dodaje nowy sekret do Wallet węzła wywołującego, dlatego ważne jest uwzględnienie kopii zapasowej pliku Wallet w procesie zarządzania węzłem.


Wyślemy teraz trochę Bitcoin z mainchain do Sidechain. Nasz test regresji mainchain Wallet posiada już pewne środki.


```
b-cli getwalletinfo
```


Widzimy, że Wallet mieści 50 Bitcoin. Wyślemy jeden Bitcoin z mainchain do Sidechain. Musimy wysłać środki do mainchain Address, który nasz węzeł wygenerował wcześniej.


```
b-cli sendtoaddress <e1-pegin-address>
```


Musimy zachować identyfikator tej transakcji, ponieważ potrzebujemy go później do potwierdzenia finansowania.


Widzimy teraz, że saldo mainchain Wallet zmniejszyło się o kwotę, którą wysłaliśmy, plus dodatkową niewielką kwotę na pokrycie opłat transakcyjnych.


```
b-cli getwalletinfo
```


Musimy ponownie dojrzeć transakcję.


```
b-cli generate 101
```


Aby nasz węzeł Elements mógł zażądać funduszy peg-in, musimy uzyskać `dowód`, że transakcja peg-in została dokonana. Dowód kryptograficzny wykorzystuje finansowanie transaction ID do obliczenia ścieżki merkela i udowadnia, że transakcja jest obecna w potwierdzonym bloku.


```
b-cli gettxoutproof '["<tx-id>"]'
```


Potrzebujemy również nieprzetworzonych danych transakcyjnych.


```
b-cli getrawtransaction <tx-id>
```


Mając dowód i nieprzetworzone dane dla transakcji peg-in, nasz węzeł Elements może teraz żądać peg-in przy użyciu nieprzetworzonej transakcji i dowodu transakcji.


```
e1-cli claimpegin <raw> <proof>
```


Należy zauważyć, że istnieje opcjonalny trzeci argument, który można przekazać do claimpegin. Ten trzeci parametr może być użyty do określenia Sidechain Address, do którego mają zostać wysłane żądane środki. Nie było to potrzebne w naszym przykładzie, ponieważ wywołaliśmy polecenie z tego samego węzła, który jest właścicielem Address, do którego trafiają żądane środki.


Sprawdzanie salda e1.


```
e1-cli getwalletinfo
```


Generowanie bloku w celu potwierdzenia roszczenia.


```
e1-cli generate 1
```


Sprawdzanie salda e1.


```
e1-cli getwalletinfo
```


Widzimy, że peg-in został pomyślnie zażądany.


W przypadku peg-out proces jest podobny. Generowany jest Address, wysyłane są do niego środki, które są zwalniane, jeśli transakcja jest ważna. Nie będziemy omawiać całego procesu peg-out, ponieważ wymaga on pracy nad mainchain, co wykracza poza zakres tego kursu. Kroki w zakresie zdarzeń Elements są takie, że Address jest generowany na mainchain.


```
b-cli getnewaddress
```


Środki są wysyłane do mainchain Address z węzła Elements za pomocą polecenia sendtomainchain.


```
e1-cli sendtomainchain <new-address> 1
```


Wygenerowanie bloku potwierdzającego transakcję.


```
e1-cli generate 1
```


Sprawdź saldo Wallet węzła.


```
e1-cli getwalletinfo
```


I zobacz, że saldo się zmniejszyło.


W tej sekcji zobaczyliśmy, jak to zrobić:


- generate a federated peg script.
- Inicjuje nowy łańcuch, który używa skryptu jako reguły parametru konsensusu sieci.
- Wyślij środki z mainchain do Sidechain.
- Zażądaj środków w ramach Elements Sidechain.
- Zrozumienie, w jaki sposób rozpoczyna się wysyłanie środków z powrotem do mainchain.


### FederatedPegScript



Aby umożliwić Elements pracę jako Sidechain, blok Genesis w jego Blockchain musi zostać utworzony z `fedpegscript` na miejscu. Odbywa się to poprzez przekazanie parametru `fedpegscript` podczas uruchamiania węzła. Skrypt ten będzie następnie stanowił część reguł konsensusu Elements Blockchain i umożliwi zatwierdzanie i wykonywanie żądań peg-in i peg-out.


Skrypt `fedpegscript` składa się z kluczy publicznych kontrolowanych przez osoby upoważnione do wykonywania akcji peg. Poniżej przedstawiono przykładowy format fedpegscript z 2 na 2 wielopodpisami:


```
fedpegscript=5221<public key 1>21<public key 2>52ae
```


Uwaga: Znaki poza kluczami publicznymi są ogranicznikami, które wskazują klucz publiczny i wymagania `n z m`. Na przykład szablon dla fedpegscript 1-of-1 miałby postać "5121<pub key 1>51ae".


### Peg-in


Zanim transakcja peg-in zostanie zaakceptowana przez Elements Sidechain, musi mieć wystarczające potwierdzenia na mainchain. Jest to konieczne, aby uniknąć inflacji w Supply z pegged asset na Elements Sidechain, która mogłaby być spowodowana reorganizacją mainchain.


Krótkie reorganizacje wierzchołka Bitcoin Blockchain są oczekiwane jako część normalnego działania mechanizmu konsensusu Proof of Work (PoW). W związku z tym Elements akceptuje peg-in jako ważny tylko wtedy, gdy ma wystarczającą głębokość w Bitcoin Blockchain. Ma to na celu uniemożliwienie Elements zaakceptowania tego samego peg-in więcej niż jeden raz.


### Peg-Out


Wycofanie następuje, gdy węzeł Elements wywołuje polecenie `sendtomainchain`, które przyjmuje jako dane wejściowe mainchain Address (miejsce docelowe wycofania), jak również kwotę pegged asset, która ma być `wycofana`. Tworzy to transakcję peg-out na Sidechain. Gdy pracownicy funkcyjni działający jako watchmen wykryją, że transakcja peg-out została potwierdzona na Sidechain, zajmą się faktycznym zwolnieniem aktywów na mainchain do miejsca docelowego peg-out, jak dowiedzieliśmy się we wcześniejszych sekcjach kursu.


## Elements jako samodzielny Blockchain


<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>


:::video id=4955306b-4be3-429c-9d30-068f7644ea73:::


Do tej pory przyjrzeliśmy się, jak uruchomić Elements jako Sidechain. Jednak może on również działać jako samodzielne rozwiązanie Blockchain z własnym domyślnym zasobem natywnym. W tej konfiguracji Elements Blockchain nadal zachowuje wszystkie funkcje implementacji Sidechain, takie jak Confidential Transactions i Issued Assets, ale nie potrzebuje peg-in lub peg-out, aby dodawać lub usuwać kwoty default asset z obiegu.


W tej sekcji omówimy:


Inicjalizacja nowego Elements Blockchain z default asset o nazwie `newasset`.


Określ 1 000 000 `newasset`, który ma zostać utworzony wraz z 2 tokenami ponownego wydania.


Zdobądź wszystkie monety anyone-can-spend `newasset`.


Odbierz wszystkie tokeny anyone-can-spend do ponownego wydania dla "newasset".


Wyślij zasób i jego reissuance token do Wallet innego węzła.


Ponownie wystaw więcej "newasset" z obu węzłów.


Aby zainicjować sieć Elements do działania jako samodzielny Blockchain, każdy węzeł musi zostać uruchomiony z kilkoma podstawowymi parametrami. Są one używane do poinformowania węzła, aby nie próbował zatwierdzać połączeń peg-ins z innego Blockchain, nazwy default asset sieci oraz ilości default asset i powiązanego reissuance token do utworzenia.


Rozpoczniemy teraz nowy łańcuch przy użyciu tych parametrów na naszych dwóch połączonych węzłach Elements. Nazwiemy default asset `newasset` i wyemitujemy milion takich tokenów oraz dwa tokeny reemisji `newasset`.


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000

e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


Należy pamiętać, że kwoty użyte tutaj są w najmniejszym nominale, jaki sieć może zaakceptować, więc dwieście milionów tokenów reemisji w rzeczywistości równa się dwóm całym tokenom. To samo dotyczy nominału początkowych darmowych monet.


Sprawdź aktualne salda Wallet w naszym węźle.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Widzimy, że inicjalizacja przebiegła poprawnie.


Ponieważ początkowa emisja aktywów jest tworzona jako "każdy może wydać", będziemy kazać e1 odebrać je wszystkie, abyśmy mogli odebrać e2 dostęp do nich.


```
e1-cli getnewaddress

e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```


Zwróć uwagę, że nie musimy określać "newasset" jako zasobu do wysłania, ponieważ jest to już default asset, a zatem także default asset używany do uiszczania opłat sieciowych.


W Elements można wysyłać wiele typów aktywów do tego samego Address, więc możemy ponownie użyć Address, który właśnie wygenerowaliśmy, aby otrzymać default asset i użyć go jako docelowego Address dla tokenów ponownego wydania.


```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Potwierdź transakcje.


```
e1-cli generate 101
```


Sprawdzimy, czy e1 jest teraz jedynym posiadaczem aktywów i jego reissuance token.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Co, jak widzimy, rzeczywiście ma miejsce.


Teraz wyślemy część "newasset" do e2, który obecnie posiada saldo równe zero.


```
e2-cli getnewaddress

e1-cli sendtoaddress <e2-address> 500 "" "" false
```


Zauważ, że nie musieliśmy określać typu wysyłanego zasobu, ponieważ `newasset` został utworzony jako default asset sieci


Wyślijmy również kilka tokenów ponownego wydania dla `newasset` do e2.


```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```


Potwierdź transakcje.


```
e1-cli generate 101
```


Możemy sprawdzić, czy portfele zostały odpowiednio zaktualizowane.


```
e1-cli getwalletinfo

e2-cli getwalletinfo
```


Teraz ponownie wydamy niektóre default asset z e1. Należy pamiętać, że możliwość zrobienia tego jest włączona przez parametr startowy initialreissuancetokens. Który, jeśli zostanie pominięty lub ustawiony na zero, spowoduje, że default asset nie będzie można ponownie wydać w późniejszym terminie.


```
e1-cli reissueasset newasset 100
```


Byliśmy w stanie użyć etykiety `newasset` zamiast konieczności podawania wartości hex id, ponieważ łańcuch Elements zawsze etykietuje swój default asset.


Sprawdzenie, czy ponowne wydanie default asset zadziałało:


```
e1-cli generate 101

e1-cli getwalletinfo
```


Udowodnimy teraz, że ponieważ e2 posiada część tokenów ponownego wydania `newasset`, może również ponownie wydać default asset.


```
e2-cli reissueasset newasset 100
```


Sprawdzenie, czy ponowne wydanie default asset przez e2 zadziałało.


```
e2-cli generate 101

e2-cli getwalletinfo
```


W tej sekcji skonfigurowaliśmy Elements jako samodzielny Blockchain i sprawdziliśmy, że podstawowe funkcje działają zgodnie z oczekiwaniami.


Użyliśmy parametrów startowych do:


Inicjalizacja nowego Elements Blockchain z default asset o nazwie "newasset".


Określ ilość default asset do utworzenia inicjalizacji on chain.


Utwórz kilka tokenów ponownego wydania dla default asset i ponownie wydaj więcej default asset z obu węzłów.


W naszej autonomicznej sieci Blockchain Elements wszystkie inne operacje transakcyjne będą działać w taki sam sposób, jak przykłady omówione w głównych sekcjach kursu, ale będą używać "newasset" zamiast `Bitcoin` jako domyślnego i płatnego zasobu.


### Parametry uruchamiania węzła i inicjalizacji łańcucha


Aby powiedzieć węzłowi Elements, aby działał jako samodzielny Blockchain, należy użyć kilku parametrów. Przyjrzymy się teraz każdemu z nich i dowiemy się, co robią.


#### `validatepegin=0`

Ponieważ autonomiczny Blockchain nie musi sprawdzać poprawności żadnych transakcji peg-in lub peg-out, musimy wyłączyć te kontrole. Przy tym ustawieniu nie trzeba uruchamiać oprogramowania klienckiego Bitcoin ani przechowywać kopii Bitcoin Blockchain, ponieważ sieć Elements będzie działać niezależnie.


#### `defaultpeggedassetname`

Umożliwia określenie nazwy default asset utworzonej podczas inicjalizacji Blockchain.


#### `initialfreecoins`

Liczba (w odpowiedniku jednostki Bitcoin w Satoshi) jednostek default asset do utworzenia.


#### `initialreissuancetokens`

Liczba (w ekwiwalencie jednostki Bitcoin dla Satoshi) żetonów ponownego wydania dla default asset do utworzenia. Bez tego niemożliwe byłoby utworzenie większej liczby default asset. Jeśli nie chcesz, aby można było utworzyć więcej default asset, możesz ustawić tę wartość na zero lub pominąć.


Używając tych parametrów, wspólna procedura uruchamiania węzła wyglądałaby mniej więcej tak:


```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```


### Podstawowe operacje


Parametr `defaultpeggedassetname` stosuje etykietę do default asset. Bez tego ustawienia default asset zostanie automatycznie nazwany `Bitcoin`. W poprzednich sekcjach, gdy wysyłaliśmy zasoby, które sami wydaliśmy do innego węzła, musieliśmy określić albo hex zasobu, albo lokalnie zastosowaną etykietę zasobu, aby powiedzieć Elements, który zasób wysyłamy. Ponieważ `defaultpeggedassetname` ma zastosowanie we wszystkich węzłach, nie musimy go nazywać, gdy go wysyłamy, nawet jeśli jego nazwa nie brzmi `Bitcoin`. Każda funkcja, która wcześniej domyślnie wysyłała `Bitcoin`, teraz wyśle to, co wybrałeś do oznaczenia default asset.


Tak więc wysłanie 10 nowych default asset do Address jest bardzo proste:


```
e1-cli sendtoaddress <destination address> 10 "" "" true
```


Jeśli podałeś węzłowi wartość `initialreissuancetokens` większą od zera, będziesz mógł ponownie wydać więcej default asset, co nie jest możliwe, jeśli uruchomisz Elements jako Sidechain.


Aby to zrobić, dowolny węzeł posiadający ilość tokena powiązanego z default asset musi jedynie wydać polecenie w postaci:


```
e1-cli reissueasset <default asset name> <amount>
```


Korzystając z powyższych parametrów, można obsługiwać Elements jako samodzielny Blockchain z własnym default asset, oddzielony od Bitcoin i innych łańcuchów bloków.


## Wnioski


<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>


:::video id=bd5167d5-edba-40b0-a8b1-ba8b74493a08:::


W tym kursie dowiedzieliśmy się, że Elements jest protokołem sieciowym o otwartym kodzie źródłowym, który można wdrożyć jako Sidechain do innego Blockchain lub jako samodzielne rozwiązanie Blockchain.


Widzieliśmy, że kod źródłowy i strona internetowa Elements (https://github.com/ElementsProject/Elements) są hostowane na GitHub i że istnieją fora dyskusyjne społeczności, takie jak Build On L2 (https://community.Liquid.net/c/developers/) lub Liquid Developers Telegram (https://t.me/liquid_devel), które można wykorzystać, aby dowiedzieć się więcej o wdrażaniu i rozwijaniu aplikacji na Elements i Liquid. Omówiono kluczowe funkcje, takie jak Confidential Transactions i Issued Assets, a także sposób, w jaki członkowie Strong Federation umożliwiają federację block signing i mechanizm 2-Way Peg.


Następnym krokiem jest zmierzenie się z quizem obejmującym wszystkie poprzednie sekcje, a następnie rozpoczęcie podróży Elements... powodzenia!


# Sekcja końcowa


<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>


## Recenzje i oceny


<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Wnioski


<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

<isCourseConclusion>true</isCourseConclusion>