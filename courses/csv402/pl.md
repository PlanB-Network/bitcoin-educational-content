---
name: Protokół RGB, od teorii do praktyki
goal: Zdobycie umiejętności potrzebnych do zrozumienia i korzystania z RGB
objectives: 

  - Zrozumienie podstawowych pojęć protokołu RGB
  - Opanowanie zasad zobowiązań Client-side Validation i Bitcoin
  - Dowiedz się, jak tworzyć, zarządzać i przenosić umowy RGB
  - Jak obsługiwać węzeł Lightning kompatybilny z RGB


---
# Odkrywanie protokołu RGB


Zanurz się w świecie RGB, protokołu zaprojektowanego do wdrażania i egzekwowania praw cyfrowych w formie kontraktów i aktywów, w oparciu o zasady konsensusu i operacje Bitcoin Blockchain. Ten kompleksowy kurs szkoleniowy poprowadzi Cię przez techniczne i praktyczne podstawy RGB, od koncepcji "Client-side Validation" i "Pieczęci jednorazowego użytku", po wdrażanie zaawansowanych inteligentnych kontraktów.


Dzięki ustrukturyzowanemu programowi krok po kroku odkryjesz mechanizmy Client-side Validation, deterministyczne zobowiązania na Bitcoin i wzorce interakcji między użytkownikami. Dowiesz się, jak tworzyć, zarządzać i przesyłać tokeny RGB na Bitcoin lub Lightning Network.


Niezależnie od tego, czy jesteś programistą, entuzjastą Bitcoin, czy po prostu chcesz dowiedzieć się więcej o tej technologii, ten kurs szkoleniowy zapewni Ci narzędzia i wiedzę potrzebne do opanowania RGB i tworzenia innowacyjnych rozwiązań na Bitcoin.


Kurs opiera się na seminarium na żywo zorganizowanym przez Fulgur'Ventures i prowadzonym przez trzech renomowanych nauczycieli i ekspertów RGB.


+++
# Wprowadzenie


<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>


## Prezentacja kursu


<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>


Witam wszystkich i zapraszam na ten kurs szkoleniowy poświęcony RGB, zweryfikowanemu po stronie klienta systemowi Smart contract działającemu na Bitcoin i Lightning Network. Struktura tego kursu została zaprojektowana tak, aby umożliwić dogłębną eksplorację tego złożonego tematu. Oto jak zorganizowany jest kurs:


**Sekcja 1: Teoria


Pierwsza sekcja poświęcona jest koncepcjom teoretycznym potrzebnym do zrozumienia podstaw Client-side Validation i RGB. Jak dowiesz się w tym kursie, RGB wprowadza wiele koncepcji technicznych, które zwykle nie są widoczne w Bitcoin. W tej sekcji znajdziesz również słowniczek zawierający definicje wszystkich terminów specyficznych dla protokołu RGB.


**Sekcja 2: Praktyka


Druga sekcja skupi się na zastosowaniu koncepcji teoretycznych przedstawionych w sekcji 1. Nauczymy się tworzyć i manipulować kontraktami RGB. Zobaczymy również, jak programować za pomocą tych narzędzi. Te dwie pierwsze sekcje zostały zaprezentowane przez Maxima Orlovsky'ego.


**Sekcja 3: Aplikacje


Ostatnia sekcja jest prowadzona przez innych prelegentów, którzy prezentują konkretne aplikacje oparte na RGB, aby podkreślić rzeczywiste przypadki użycia.


---
Ten kurs szkoleniowy pierwotnie wyrósł z dwutygodniowego zaawansowanego bootcampu programistycznego w Viareggio w Toskanii, zorganizowanego przez [Fulgur'Ventures] (https://fulgur.ventures/). Pierwszy tydzień, skoncentrowany na Rust i SDK, można znaleźć w tym innym kursie:


https://planb.network/courses/9fbd8b57-f278-4304-8d88-a2d384eaff58

W tym kursie skupiamy się na drugim tygodniu bootcampu, który koncentruje się na RGB.


**Tydzień 1 - LNP402:**


![RGB-Bitcoin](assets/fr/001.webp)


**Tydzień 2 - Bieżące szkolenie CSV402:**


![RGB-Bitcoin](assets/fr/002.webp)


Bardzo dziękujemy organizatorom tych kursów na żywo i 3 nauczycielom, którzy wzięli w nich udział:




- Maxim Orlovsky: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, AI, robotyka, transhumanizm. Twórca RGB, Prime, Radiant i lnp_bp, mycitadel_io & cyphernet_io* ;
- Hunter Trujilo: *Deweloper, Rust, Bitcoin, Błyskawica, RGB* ;
- Federico Tenga: *Robię swoje, by zmienić świat w dystopię Cypherpunk. Obecnie pracuje nad RGB w Bitfinex*.


Pisemna wersja tego szkolenia została opracowana przy użyciu 2 głównych zasobów:




- Filmy z seminarium Maxima Orlovsky'ego, Huntera Trujilo i Frederico Tengi na Lightning Bootcamp;
- Dokumentacja RGB, której produkcja była sponsorowana przez [Bitfinex] (https://www.bitfinex.com/).


Gotowy do zanurzenia się w złożonym i fascynującym świecie RGB? Do dzieła!


# RGB w teorii


<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>


## Wprowadzenie do koncepcji przetwarzania rozproszonego


<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>


:::video id=f27338bc-4210-4a2e-9b27-30278ed3282c:::


RGB to protokół zaprojektowany do stosowania i egzekwowania praw cyfrowych (w formie umów i aktywów) w skalowalny i poufny sposób, w oparciu o zasady konsensusu i operacje Bitcoin Blockchain. Celem tego pierwszego rozdziału jest przedstawienie podstawowych pojęć i terminologii związanej z protokołem RGB, podkreślając w szczególności jego ścisłe powiązania z podstawowymi koncepcjami przetwarzania rozproszonego, takimi jak Client-side Validation i Single-use Seals.


W tym rozdziale zbadamy podstawy **rozproszonych systemów konsensusu** i zobaczymy, jak RGB pasuje do tej rodziny technologii. Przedstawimy również główne zasady, które pomogą nam zrozumieć, dlaczego RGB ma być rozszerzalny i niezależny od własnego mechanizmu konsensusu Bitcoin, jednocześnie polegając na nim w razie potrzeby.


### Wprowadzenie


Informatyka rozproszona, specyficzna gałąź informatyki, bada protokoły używane do obiegu i przetwarzania informacji w sieci węzłów. Węzły te i reguły protokołów tworzą razem tak zwany system rozproszony. Do podstawowych właściwości charakteryzujących taki system należą :




- Możliwość niezależnej weryfikacji i walidacji** określonych danych przez każdy węzeł;
- Możliwość tworzenia przez węzły (w zależności od protokołu) pełnego lub częściowego widoku informacji. Te widoki są **stanami** systemu rozproszonego;
- **chronologiczna kolejność** operacji, dzięki czemu dane są niezawodnie znakowane czasem i istnieje konsensus co do sekwencji zdarzeń (sekwencji stanów).


W szczególności, pojęcie **konsensusu** w systemie rozproszonym obejmuje dwa aspekty:




- Uznanie ważności** zmian stanu (zgodnie z zasadami protokołu);
- **Zgoda na kolejność** tych zmian stanu, która uniemożliwia przepisanie lub odwrócenie zatwierdzonych operacji a posteriori (jest to również znane w Bitcoin jako "ochrona przed podwójnym wydaniem").


Pierwsza funkcjonalna, wolna od uprawnień implementacja rozproszonego mechanizmu konsensusu została wprowadzona przez Satoshi Nakamoto za pomocą Bitcoin, dzięki połączonemu wykorzystaniu struktury danych Blockchain i algorytmu Proof-of-Work (PoW). W tym systemie wiarygodność historii bloku zależy od mocy obliczeniowej poświęconej na nią przez węzły (górników). Bitcoin jest zatem głównym i historycznym przykładem rozproszonego systemu konsensusu otwartego dla wszystkich (*bez uprawnień*).


W świecie Blockchain i przetwarzania rozproszonego możemy wyróżnić dwa podstawowe paradygmaty: ***Blockchain*** w tradycyjnym rozumieniu oraz ***kanały stanowe***, których najlepszym przykładem w produkcji jest Lightning Network. Blockchain jest definiowany jako rejestr chronologicznie uporządkowanych zdarzeń, replikowanych w drodze konsensusu w ramach otwartej, wolnej od uprawnień sieci. Kanały stanowe, z drugiej strony, są kanałami peer-to-peer, które umożliwiają dwóm (lub więcej) uczestnikom utrzymywanie zaktualizowanego stanu off-chain, wykorzystując Blockchain tylko podczas otwierania i zamykania tych kanałów.


W kontekście Bitcoin bez wątpienia znasz zasady Mining, decentralizacji i ostateczności transakcji na Blockchain, a także sposób działania kanałów płatności. Wraz z RGB wprowadzamy nowy paradygmat o nazwie **Client-side Validation**, który w przeciwieństwie do Blockchain lub Lightning, polega na lokalnym (po stronie klienta) przechowywaniu i walidacji przejść stanu Smart contract. Różni się to również od innych technik "DeFi" (_rollups_, _plasma_, _ARK_ itp.), ponieważ Client-side Validation opiera się na Blockchain, aby zapobiec Double-spending i mieć system znaczników czasu, jednocześnie prowadząc rejestr stanów i przejść off-chain, tylko z zainteresowanymi uczestnikami.


![RGB-Bitcoin](assets/fr/003.webp)


Później wprowadzimy również ważny termin: pojęcie "**Stash**", które odnosi się do zestawu danych po stronie klienta wymaganych do zachowania stanu Contract, ponieważ dane te nie są replikowane globalnie w całej sieci. Na koniec przyjrzymy się uzasadnieniu RGB, protokołu, który wykorzystuje Client-side Validation i dlaczego uzupełnia istniejące podejścia (Blockchain i kanały stanu).


### Dylematy w obliczeniach rozproszonych


Aby zrozumieć, w jaki sposób Client-side Validation i RGB Address rozwiązują problemy nierozwiązane przez Blockchain i Lightning, odkryjmy 3 główne "trilemmas" w obliczeniach rozproszonych:




- Skalowalność, decentralizacja, prywatność** ;
- Twierdzenie CAP** (spójność, dostępność, tolerancja partycji) ;
- Trylemat CIA** (poufność, integralność, dostępność).


#### 1. Skalowalność, decentralizacja i poufność




- Blockchain (Bitcoin)**


Blockchain jest wysoce zdecentralizowany, ale niezbyt skalowalny. Co więcej, ponieważ wszystko znajduje się w globalnym, publicznym rejestrze, poufność jest ograniczona. Możemy próbować poprawić poufność za pomocą technologii zerowej wiedzy (Confidential Transactions, schematy mimblewimble itp.), ale publiczny łańcuch nie może ukryć wykresu transakcji.




- Kanały Lightning/State**


Kanały stanowe (podobnie jak Lightning Network) są bardziej skalowalne i bardziej prywatne niż Blockchain, ponieważ transakcje odbywają się off-chain. Jednak obowiązek publicznego ogłaszania niektórych Elements (transakcje finansowania, topologia sieci) i monitorowanie ruchu sieciowego może częściowo zagrozić poufności. Cierpi na tym również decentralizacja: routing wymaga dużych nakładów pieniężnych, a główne węzły mogą stać się punktami centralizacji. To jest właśnie zjawisko, które zaczynamy obserwować na Lightning.




- Client-side Validation (RGB)**


Ten nowy paradygmat jest jeszcze bardziej skalowalny i bardziej poufny, ponieważ nie tylko możemy zintegrować techniki dowodu wiedzy o zerowym ujawnieniu, ale także nie ma globalnego wykresu transakcji, ponieważ nikt nie posiada całego rejestru. Z drugiej strony oznacza to również pewien kompromis w zakresie decentralizacji: emitent Smart contract może pełnić centralną rolę (podobnie jak "wdrażający Contract" w Ethereum). Jednak w przeciwieństwie do Blockchain, w Client-side Validation przechowujesz i weryfikujesz tylko te kontrakty, którymi jesteś zainteresowany, co poprawia skalowalność, unikając konieczności pobierania i weryfikowania wszystkich istniejących stanów.


![RGB-Bitcoin](assets/fr/004.webp)


#### 2. Twierdzenie CAP (spójność, dostępność, tolerancja partycji)


Twierdzenie CAP podkreśla, że niemożliwe jest, aby system rozproszony jednocześnie spełniał wymagania spójności (*Consistency*), dostępności (*Availability*) i tolerancji partycji (*Partition tolerance*).




- Blockchain**


Blockchain faworyzuje spójność i dostępność, ale nie radzi sobie dobrze z partycjonowaniem sieci: jeśli nie widzisz bloku, nie możesz działać i mieć tego samego widoku, co cała sieć.




- Błyskawica** (w języku francuskim)


System kanałów stanowych ma tolerancję na dostępność i partycjonowanie (ponieważ dwa węzły mogą pozostać ze sobą połączone, nawet jeśli sieć jest pofragmentowana), ale ogólna spójność zależy od otwierania i zamykania kanałów na Blockchain.




- Client-side Validation (RGB)**


System taki jak RGB oferuje spójność (każdy uczestnik waliduje swoje dane lokalnie, bez dwuznaczności) i tolerancję partycjonowania (przechowujesz swoje dane autonomicznie), ale nie gwarantuje globalnej dostępności (każdy musi upewnić się, że ma odpowiednie fragmenty historii, a niektórzy uczestnicy mogą niczego nie publikować lub przestać udostępniać określone informacje).


![RGB-Bitcoin](assets/fr/005.webp)


#### 3. Trylemat CIA (poufność, integralność, dostępność)


Trylemat ten przypomina nam, że poufność, integralność i dostępność nie mogą być optymalizowane w tym samym czasie. Blockchain, Lightning i Client-side Validation w różny sposób wpisują się w tę równowagę. Chodzi o to, że żaden pojedynczy system nie może zapewnić wszystkiego; konieczne jest połączenie kilku podejść (znacznik czasu Blockchain, podejście synchroniczne Lightning i lokalna walidacja z RGB), aby uzyskać spójny pakiet oferujący dobre gwarancje w każdym wymiarze.


![RGB-Bitcoin](assets/fr/006.webp)


### Rola Blockchain i pojęcie shardingu


Blockchain (w tym przypadku Bitcoin) służy przede wszystkim jako mechanizm _stemplowania czasu_ i ochrona przed podwójnymi wydatkami. Zamiast wstawiać kompletne dane Smart contract lub zdecentralizowanego systemu, po prostu dołączamy **kryptograficzne zobowiązania** (_commitments_) do transakcji (w sensie Client-side Validation, które nazwiemy "przejściami stanu"). Tak więc :




- Uwalniamy Blockchain od dużej ilości danych i logiki;
- Każdy użytkownik przechowuje tylko historię wymaganą dla jego własnej części Contract (jego "*Shard*"), zamiast replikować Global State.


Sharding to koncepcja wywodząca się z rozproszonych baz danych (np. MySQL dla sieci społecznościowych, takich jak Facebook czy Twitter). Aby rozwiązać problem ilości danych i opóźnień synchronizacji, baza danych jest podzielona na segmenty (USA, Europa, Azja itd.). Każdy segment jest lokalnie spójny i tylko częściowo zsynchronizowany z innymi.


W przypadku inteligentnych kontraktów typu RGB, używamy Shard zgodnie z samymi kontraktami. Każdy Contract jest niezależnym _shardem_. Na przykład, jeśli posiadasz tylko tokeny USDT, nie musisz przechowywać ani weryfikować całej historii innego tokena, takiego jak USDC. W Bitcoin, Blockchain nie robi _shardingu_: masz globalny zestaw UTXO. W przypadku Client-side Validation każdy uczestnik zachowuje tylko dane Contract, które posiada lub wykorzystuje.


Możemy zatem wyobrazić sobie ekosystem w następujący sposób:




- Blockchain (Bitcoin)** jako podstawa, która zapewnia pełną replikację minimalnego rejestru i służy jako znacznik czasu Layer;
- Lightning Network** na szybko, Confidential Transactions, nadal w oparciu o zabezpieczenie i ostateczne rozliczenie Bitcoin Blockchain;
- RGB i Client-side Validation**, aby dodać bardziej złożoną logikę Smart contract, bez zaśmiecania Blockchain lub utraty poufności.


![RGB-Bitcoin](assets/fr/007.webp)


Te trzy Elements tworzą trójkątną całość, a nie liniowy stos "Layer 2", "Layer 3" i tak dalej. Lightning może łączyć się bezpośrednio z Bitcoin lub być powiązany z transakcjami Bitcoin, które zawierają dane RGB. Podobnie, użycie "BiFi" (finanse na Bitcoin) może łączyć się z Blockchain, Lightning i RGB zgodnie z potrzebami poufności, skalowalności lub logiki Contract.


![RGB-Bitcoin](assets/fr/008.webp)


### Pojęcie przejść między stanami


W każdym systemie rozproszonym celem mechanizmu walidacji jest możliwość **określenia ważności i chronologicznej kolejności zmian stanu**. Celem jest sprawdzenie, czy reguły protokołu były przestrzegane i udowodnienie, że zmiany stanu następują po sobie w ostatecznej, niepodważalnej kolejności.


Aby zrozumieć, jak ta walidacja działa w kontekście **Bitcoin** i, bardziej ogólnie, aby zrozumieć filozofię stojącą za Client-side Validation, najpierw spójrzmy wstecz na mechanizmy Bitcoin Blockchain, zanim zobaczymy, jak Client-side Validation różni się od nich i jakie optymalizacje umożliwia.


![RGB-Bitcoin](assets/fr/009.webp)


W przypadku Bitcoin Blockchain walidacja transakcji opiera się na prostej zasadzie:




- Wszystkie węzły sieci pobierają każdy blok i transakcję;
- Zatwierdzają te transakcje, aby zweryfikować prawidłowy rozwój zestawu UTXO (wszystkie niewydane wyniki);
- Przechowują one te dane (w formie bloków), aby w razie potrzeby można było odtworzyć historię.


![RGB-Bitcoin](assets/fr/010.webp)


Model ten ma jednak dwie główne wady:




- Skalowalność**: ponieważ każdy węzeł musi przetwarzać, weryfikować i archiwizować transakcje wszystkich użytkowników, istnieje oczywisty limit pojemności transakcji, powiązany w szczególności z maksymalnym rozmiarem bloku (średnio 1 MB w ciągu 10 minut dla Bitcoin, z wyłączeniem plików cookie);
- Prywatność**: wszystko jest transmitowane i przechowywane publicznie (kwoty, adresy docelowe itp.), co ogranicza poufność wymiany.


![RGB-Bitcoin](assets/fr/012.webp)


W praktyce model ten sprawdza się w przypadku Bitcoin jako bazowego Layer (Layer 1), ale może okazać się niewystarczający w przypadku bardziej złożonych zastosowań, które jednocześnie wymagają wysokiej przepustowości transakcji i pewnego stopnia poufności.


Client-side Validation opiera się na przeciwnym pomyśle: zamiast wymagać od całej sieci walidacji i przechowywania wszystkich transakcji, każdy uczestnik (klient) będzie walidował tylko tę część historii, która go dotyczy:




- Kiedy dana osoba otrzymuje zasób (lub jakąkolwiek inną własność cyfrową), musi jedynie znać i zweryfikować łańcuch operacji (przejścia stanów), które prowadzą do tego zasobu i udowodnić jego legalność;
- Ta sekwencja operacji, od ***Genesis*** (początkowa emisja) do najnowszej transakcji, tworzy acykliczny graf skierowany (DAG) lub Shard, tj. ułamek całej historii.


![RGB-Bitcoin](assets/fr/013.webp)


Jednocześnie, aby reszta sieci (a dokładniej bazowy Layer, taki jak Bitcoin) mogła zablokować stan końcowy bez wglądu w szczegóły tych danych, Client-side Validation opiera się na pojęciu ***Commitment***.


*Commitment* to kryptograficzny Commitment, zazwyczaj _hash_ (na przykład SHA-256) wstawiony do transakcji Bitcoin, który dowodzi, że prywatne dane zostały uwzględnione, bez ujawniania tych danych.


Dzięki tym _zobowiązaniom_ możemy udowodnić:




- Istnienie informacji (ponieważ są one przekazywane do Hash);
- Przedwczesność tych informacji (ponieważ są one zakotwiczone i oznaczone czasem w Blockchain, z datą i kolejnością bloków).


Dokładna treść nie jest jednak ujawniana, co pozwala zachować jej poufność.


Mówiąc konkretnie, oto jak działa RGB State Transition:




- Przygotowujesz nowy State Transition (np. transfer tokena RGB);
- generate kryptograficzny Commitment do tego przejścia i wstawia go do transakcji Bitcoin (te zobowiązania są nazywane "*anchors*" w protokole RGB);
- Kontrahent (odbiorca) pobiera historię po stronie klienta powiązaną z tym aktywem i weryfikuje spójność end-to-end, od Genesis z Smart contract do przejścia, które do niego przekazujesz.


![RGB-Bitcoin](assets/fr/014.webp)


Client-side Validation oferuje dwie główne korzyści:




- Skalowalność:**


Zobowiązania (*commitments*) zawarte w Blockchain są niewielkie (rzędu kilkudziesięciu bajtów). Zapewnia to, że przestrzeń blokowa nie jest nasycona, ponieważ tylko Hash musi być uwzględniony. Umożliwia to również ewolucję protokołu off-chain, ponieważ każdy użytkownik musi przechowywać tylko swój fragment historii (swój _stash_).




- Prywatność :**


Same transakcje (tj. ich szczegółowa treść) nie są publikowane On-Chain. Publikowane są jedynie ich odciski palców (*Hash*). W ten sposób kwoty, adresy i logika Contract pozostają prywatne, a odbiorca może lokalnie zweryfikować ważność swojego Shard, sprawdzając wszystkie poprzednie transakcje. Nie ma powodu, aby odbiorca upubliczniał te dane, z wyjątkiem sytuacji spornych lub wymagających dowodu.


W systemie takim jak RGB, wiele przejść stanu z różnych kontraktów (lub różnych aktywów) może zostać zagregowanych w pojedynczą transakcję Bitcoin za pośrednictwem pojedynczego _commitment_. Mechanizm ten ustanawia deterministyczne, znakowane czasem połączenie między transakcją On-Chain a danymi off-chain (zweryfikowane przejścia po stronie klienta) i umożliwia jednoczesne rejestrowanie wielu fragmentów w jednym punkcie Anchor, co dodatkowo zmniejsza koszt i ślad On-Chain.


W praktyce, gdy ta transakcja Bitcoin zostanie zatwierdzona, trwale "blokuje" stan kontraktów bazowych, ponieważ staje się niemożliwe zmodyfikowanie Hash już wpisanego w Blockchain.


![RGB-Bitcoin](assets/fr/015.webp)


### Koncepcja Stash


Stash** to zestaw danych po stronie klienta, które uczestnik musi bezwzględnie zachować, aby zachować integralność i historię RGB Smart contract. W przeciwieństwie do kanału Lightning, w którym pewne stany można odtworzyć lokalnie na podstawie udostępnionych informacji, Stash RGB Contract nie jest replikowany gdzie indziej: jeśli go utracisz, nikt nie będzie w stanie go przywrócić, ponieważ jesteś odpowiedzialny za swoją część historii. Dlatego właśnie należy przyjąć system z niezawodnymi procedurami tworzenia kopii zapasowych w RGB.


![RGB-Bitcoin](assets/fr/016.webp)


### Single-Use Seal: pochodzenie i działanie


Akceptując aktywa takie jak waluta, niezbędne są dwie gwarancje:




- Autentyczność otrzymanego przedmiotu;
- Unikalność otrzymanego przedmiotu, aby uniknąć podwójnych wydatków.


W przypadku aktywów fizycznych, takich jak banknot, fizyczna obecność wystarczy, aby udowodnić, że nie został on zduplikowany. Jednak w świecie cyfrowym, w którym aktywa mają charakter czysto informacyjny, weryfikacja ta jest bardziej złożona, ponieważ informacje mogą być łatwo powielane i duplikowane.


Jak widzieliśmy wcześniej, ujawnienie przez nadawcę historii przejść stanów pozwala nam zapewnić autentyczność tokena RGB. Mając dostęp do wszystkich transakcji od czasu transakcji Genesis, możemy potwierdzić autentyczność tokena. Zasada ta jest podobna do tej z Bitcoin, gdzie historię monet można prześledzić wstecz do oryginalnego Coinbase Transaction, aby zweryfikować ich ważność. Jednak w przeciwieństwie do Bitcoin, ta historia zmian stanu w RGB jest prywatna i przechowywana po stronie klienta.


Aby zapobiec Double-spending tokenów RGB, używamy mechanizmu o nazwie "**Single-Use Seal**". System ten zapewnia, że każdy token, raz użyty, nie może zostać ponownie wykorzystany w nieuczciwy sposób.


Jednorazowe plomby to kryptograficzne prymitywy, zaproponowane w 2016 roku przez Petera Todda, zbliżone do koncepcji fizycznych plomb: po umieszczeniu Seal na pojemniku niemożliwe staje się jego otwarcie lub zmodyfikowanie bez nieodwracalnego złamania Seal.


![RGB-Bitcoin](assets/fr/018.webp)


Podejście to, przeniesione do świata cyfrowego, umożliwia udowodnienie, że sekwencja zdarzeń rzeczywiście miała miejsce i że nie można jej już zmienić a posteriori. Pieczęcie jednorazowego użytku wykraczają zatem poza prostą logikę `Hash + Timestamp`, dodając pojęcie Seal, które można zamknąć **tylko raz**.


![RGB-Bitcoin](assets/fr/017.webp)


Aby Pieczęcie Jednorazowego Użytku działały, potrzebny jest nośnik dowodu publikacji, zdolny do udowodnienia istnienia lub braku publikacji i trudny (jeśli nie niemożliwy) do sfałszowania po rozpowszechnieniu informacji. **Blockchain** (podobnie jak Bitcoin) może pełnić tę rolę, podobnie jak na przykład papierowa gazeta o publicznym obiegu. Idea jest następująca:




- Chcemy udowodnić, że pewien Commitment dotyczący wiadomości `h(m)` został opublikowany publiczności bez ujawniania treści wiadomości `m`;
- Chcemy udowodnić, że żadna inna konkurencyjna wiadomość Commitment nie została opublikowana zamiast `h(m)`;
- Chcemy również mieć możliwość sprawdzenia, czy wiadomość `m` istnieje przed określoną datą.


Blockchain idealnie nadaje się do tej roli: gdy tylko transakcja zostanie zawarta w bloku, cała sieć ma ten sam niefalsyfikowalny dowód jej istnienia i treści (przynajmniej częściowo, ponieważ _commitment_ może ukryć szczegóły, jednocześnie udowadniając autentyczność wiadomości).


Single-Use Seal można zatem postrzegać jako formalną obietnicę opublikowania wiadomości (na tym etapie wciąż nieznanej) raz i tylko raz, w sposób, który może zostać zweryfikowany przez wszystkie zainteresowane strony.


W przeciwieństwie do prostych _commitments_ (Hash) lub znaczników czasu, które poświadczają datę istnienia, Single-Use Seal oferuje dodatkową gwarancję, że **żaden alternatywny Commitment** nie może współistnieć: nie można zamknąć tego samego Seal dwa razy, ani próbować zastąpić zapieczętowanej wiadomości.


Poniższe porównanie pomaga zrozumieć tę zasadę:




- Kryptograficzny Commitment (Hash)**: Za pomocą funkcji Hash można zobowiązać się do fragmentu danych (liczby), publikując jego Hash. Dane pozostają tajne do momentu ujawnienia wstępnego obrazu, ale można udowodnić, że znało się je z wyprzedzeniem;
- Timestamp (Blockchain)**: Wstawiając ten Hash do Blockchain, udowadniamy również, że znaliśmy go w precyzyjnym momencie (włączenia do bloku);
- Single-Use Seal**: W przypadku pieczęci jednorazowych idziemy o krok dalej, czyniąc Commitment unikalnym. Za pomocą pojedynczego Hash można równolegle utworzyć kilka sprzecznych zobowiązań (problem lekarza, który ogłasza rodzinie "*To chłopiec*" i "*To dziewczynka*" w swoim osobistym dzienniku). Single-Use Seal eliminuje tę możliwość, łącząc Commitment z nośnikiem dowodu publikacji, takim jak Bitcoin Blockchain, tak że wydatek UTXO ostatecznie pieczętuje Commitment. Raz wydany UTXO nie może być ponownie wydany w celu zastąpienia Commitment.


|                                                                                  | Simple commitment (digest/hash) | Timestamps | Single-use seals |
| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |
| Publishing the commitment does not reveal the message                           | Yes                             | Yes        | Yes              |
| Proof of the commitment date / existence of the message before a certain date  | Impossible                      | Possible   | Possible         |
| Proof that no alternative commitment can exist                                 | Impossible                      | Impossible | Possible         |

Uszczelki jednorazowe działają w trzech głównych etapach:


**Seal Definition :**




- Alice z góry określa zasady publikowania Seal (kiedy, gdzie i w jaki sposób wiadomość zostanie opublikowana);
- Bob akceptuje lub potwierdza te warunki.


![RGB-Bitcoin](assets/fr/021.webp)


**Seal Zamknięcie :**




- W czasie wykonywania, Alice zamyka Seal publikując rzeczywistą wiadomość (zwykle w formie _commitment_, np. Hash);
- Zapewnia również **świadka** (dowód kryptograficzny) potwierdzający, że Seal jest zamknięty i nieodwołalny.


![RGB-Bitcoin](assets/fr/019.webp)


**Weryfikacja Seal :**




- Po zamknięciu Seal Bob nie może już go otworzyć: może jedynie sprawdzić, czy został zamknięty;
- Bob zbiera Seal, **świadka** i wiadomość (lub jego Commitment), aby upewnić się, że wszystko się zgadza i że nie ma konkurujących ze sobą pieczęci lub różnych wersji.


Proces ten można podsumować w następujący sposób:


```txt
# Défini par Alice, validé ou accepté par Bob
seal <- Define()
# Fermeture du sceau par Alice avec le message
witness <- Close(seal, message)
# Vérification par Bob
bool <- Verify(seal, witness, message)
```


Client-side Validation idzie jednak o krok dalej: jeśli sama definicja Seal pozostaje poza Blockchain, możliwe jest (teoretycznie), aby ktoś zakwestionował istnienie lub legalność danego Seal. Aby przezwyciężyć ten problem, stosuje się łańcuch zazębiających się pieczęci jednorazowych:




- Każdy zamknięty Seal zawiera definicję następnego Seal;
- Rejestrujemy te zamknięcia (wraz z ich _commitments_) w Blockchain (w transakcji Bitcoin);
- W związku z tym każda próba modyfikacji poprzedniego Seal byłaby sprzeczna z historią zawartą w Bitcoin.


Dokładnie to robi system RGB:




- Opublikowane wiadomości są _zobowiązaniami_ do zatwierdzonych danych po stronie klienta;
- Seal Definition jest powiązany z Bitcoin UTXO;
- Seal zamyka się, gdy ten UTXO zostanie wydany lub gdy nowa produkcja zostanie przypisana do tego samego Commitment;
- Łańcuch transakcji, który wydaje te UTXO, odpowiada dowodowi publikacji: każde przejście lub zmiana stanu na RGB jest zatem zakotwiczona w Bitcoin.


Podsumowując:




- Definicja _seal_ to UTXO, który ma być Seal przyszłego Commitment;
- Zamknięcie _seal closing_ następuje po wydaniu UTXO, tworząc transakcję zawierającą Commitment;
- Świadectwem_ jest sama transakcja, która dowodzi, że zamknąłeś Seal o tej treści;
- Nie możesz udowodnić, że Seal nie został zamknięty (nie możesz być absolutnie pewien, że UTXO nie został już wydany lub nie zostanie wydany w bloku, którego jeszcze nie widziałeś), ale możesz udowodnić, że rzeczywiście został zamknięty.


Ta unikalność jest ważna dla Client-side Validation: podczas walidacji State Transition sprawdzasz, czy odpowiada on unikalnemu UTXO, który nie został wcześniej wydany w konkurencyjnym Commitment. To właśnie gwarantuje brak podwójnych wydatków w inteligentnych kontraktach off-chain.


### Wiele zobowiązań i korzeni


RGB Smart contract może wymagać jednoczesnego wydania kilku pieczęci jednorazowych (kilku UTXO). Co więcej, pojedyncza transakcja Bitcoin może odnosić się do kilku różnych kontraktów, z których każdy uszczelnia swój własny State Transition. Wymaga to mechanizmu **multi-Commitment**, aby udowodnić, deterministycznie i jednoznacznie, że żadne ze zobowiązań nie istnieje w duplikacie. W tym miejscu pojawia się pojęcie **Anchor** w RGB: specjalna struktura łącząca transakcję Bitcoin i jedno lub więcej zobowiązań po stronie klienta (przejścia stanu), z których każde potencjalnie należy do innego Contract. Przyjrzymy się bliżej tej koncepcji w następnym rozdziale.


![RGB-Bitcoin](assets/fr/023.webp)


Dwa z głównych repozytoriów GitHub projektu (w ramach organizacji LNPBP) grupują podstawowe implementacje tych koncepcji, które zostały przeanalizowane w pierwszym rozdziale:




- client_side_validation** : Zawiera prymitywy Rust dla lokalnej walidacji;
- single_use_seals**: Implementuje logikę do definiowania i bezpiecznego zamykania tych pieczęci.


![RGB-Bitcoin](assets/fr/020.webp)


Należy zauważyć, że te elementy oprogramowania są niezależne od Bitcoin; teoretycznie można je zastosować do dowolnego innego nośnika dowodu publikacji (innego rejestru, czasopisma itp.). W praktyce RGB opiera się na Bitcoin ze względu na jego solidność i szeroki konsensus.


![RGB-Bitcoin](assets/fr/021.webp)


### Pytania od publiczności


#### W kierunku szerszego wykorzystania uszczelek jednorazowych


Peter Todd stworzył również protokół _Open Timestamps_, a koncepcja Single-Use Seal jest naturalnym rozszerzeniem tych pomysłów. Poza RGB można przewidzieć inne przypadki użycia, takie jak budowa _sidechainów_ bez uciekania się do _merge mining_ lub propozycje związane z drivechainami, takie jak BIP300. Każdy system wymagający pojedynczego Commitment może w zasadzie wykorzystać ten kryptograficzny prymityw. Obecnie RGB jest pierwszą dużą implementacją na pełną skalę.


#### Problemy z dostępnością danych


Ponieważ w Client-side Validation każdy użytkownik przechowuje własną część historii, dostępność danych nie jest gwarantowana globalnie. Jeśli emitent Contract wstrzyma lub wycofa pewne informacje, użytkownik może nie być świadomy faktycznego rozwoju oferty. W niektórych przypadkach (takich jak stablecoiny) oczekuje się, że emitent będzie utrzymywał publiczne dane w celu udowodnienia wolumenu w obiegu, ale nie ma takiego technicznego obowiązku. Możliwe jest zatem celowe projektowanie nieprzejrzystych kontraktów z nieograniczonym Supply, co rodzi pytania o zaufanie.


#### Sharding i izolacja Contract


Każdy Contract reprezentuje odizolowany _shard_: USDT i USDC, na przykład, nie muszą dzielić się swoimi historiami. Atomowe swapy są nadal możliwe, ale nie wiąże się to z łączeniem ich rejestrów. Wszystko odbywa się za pomocą kryptograficznego Commitment, bez ujawniania całego wykresu historii każdemu uczestnikowi.


### Wnioski


Widzieliśmy, gdzie koncepcja Client-side Validation pasuje do Blockchain i _state channels_, jak reaguje na rozproszone dylematy obliczeniowe i jak wykorzystuje Bitcoin Blockchain w unikalny sposób, aby uniknąć Double-spending i do *stemplowania czasu*. Pomysł opiera się na pojęciu **Single-Use Seal**, umożliwiając tworzenie unikalnych zobowiązań, których nie można ponownie wydać do woli. W ten sposób każdy uczestnik przesyła tylko tę historię, która jest absolutnie niezbędna, zwiększając skalowalność i poufność inteligentnych kontraktów przy jednoczesnym zachowaniu bezpieczeństwa Bitcoin jako tła.


Następnym krokiem będzie bardziej szczegółowe wyjaśnienie, w jaki sposób ten mechanizm Single-Use Seal jest stosowany w Bitcoin (za pośrednictwem UTXO), w jaki sposób tworzone i walidowane są kotwice, a następnie w jaki sposób kompletne inteligentne kontrakty są budowane w RGB. W szczególności przyjrzymy się kwestii wielokrotnych zobowiązań, technicznemu wyzwaniu polegającemu na udowodnieniu, że transakcja Bitcoin jednocześnie uszczelnia wiele przejść stanów w różnych kontraktach, bez wprowadzania luk w zabezpieczeniach lub podwójnych zobowiązań.


Zanim zagłębimy się w bardziej techniczne szczegóły drugiego rozdziału, zachęcamy do ponownego przeczytania kluczowych definicji (Client-side Validation, Single-Use Seal, kotwice itp.) i pamiętania o ogólnej logice: staramy się pogodzić mocne strony Bitcoin Blockchain (bezpieczeństwo, decentralizacja, znakowanie czasem) z rozwiązaniami off-chain (szybkość, poufność, skalowalność) i właśnie to próbują osiągnąć RGB i Client-side Validation.


## Commitment Layer


<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>


:::video id=73ddea2d-c243-479d-a3dc-12d7db8eef70:::


W tym rozdziale przyjrzymy się implementacji Client-side Validation i uszczelnień jednorazowych w ramach Bitcoin Blockchain. Przedstawimy główne zasady **Commitment Layer** RGB (Layer 1), ze szczególnym uwzględnieniem schematu **TxO2**, którego RGB używa do definiowania i zamykania Seal w transakcji Bitcoin. Następnie omówimy dwa ważne punkty, które nie zostały jeszcze szczegółowo omówione:




- _deterministyczne zobowiązania Bitcoin_;
- Zobowiązania wieloprotokołowe.


To właśnie połączenie tych koncepcji umożliwia nam nałożenie kilku systemów lub umów na pojedynczy UTXO, a tym samym na pojedynczy Blockchain.


Należy pamiętać, że opisane operacje kryptograficzne można zastosować, w kategoriach bezwzględnych, do innych blockchainów lub mediów publikacyjnych, ale cechy Bitcoin (pod względem decentralizacji, odporności na cenzurę i otwartości dla wszystkich) sprawiają, że jest to idealna podstawa do rozwijania zaawansowanej programowalności, takiej jak ta wymagana przez **RGB**.


### Schematy Commitment w Bitcoin i ich wykorzystanie przez RGB


Jak widzieliśmy w pierwszym rozdziale kursu, pieczęcie jednorazowego użytku to ogólna koncepcja: składamy obietnicę umieszczenia Commitment (_commitment_) w określonej lokalizacji transakcji, a ta lokalizacja działa jak Seal, który zamykamy w wiadomości. Jednak w Bitcoin Blockchain istnieje kilka opcji wyboru miejsca umieszczenia tego _commitment_.


Aby zrozumieć logikę, przypomnijmy podstawową zasadę: aby zamknąć _single-use seal_, spędzamy zapieczętowany obszar poprzez wstawienie _commitment_ na danej wiadomości. W Bitcoin można to zrobić na kilka sposobów:




- Użyj klucza publicznego lub Address**


Możemy zdecydować, że określony klucz publiczny lub Address jest _pieczęcią jednorazowego użytku_. Gdy tylko ten klucz lub Address pojawi się On-Chain w transakcji, oznacza to, że Seal jest zamknięty z określoną wiadomością.




- Użyj wyjścia transakcji Bitcoin**


Oznacza to, że _plomba jednorazowego użytku_ jest zdefiniowana jako dokładny _punkt wyjścia_ (para txid + numer wyjścia). Gdy tylko ten _punkt wyjścia_ zostanie osiągnięty, Seal zostanie zamknięty.


Podczas pracy nad RGB zidentyfikowaliśmy co najmniej 4 różne sposoby wdrożenia tych uszczelnień w Bitcoin:




- Zdefiniuj Seal za pomocą klucza publicznego i zamknij go w _output_ ;
- Zdefiniuj Seal za pomocą _outpoint_ i zamknij go za pomocą _output_ ;
- Zdefiniuj Seal poprzez wartość klucza publicznego i zamknij go w _input_ ;
- Zdefiniuj Seal poprzez _outpoint_ i zamknij go w _input_.


| Schema Name | Seal Definition           | Seal Closure              | Additional Requirements                                        | Main Application            | Possible Commitment Schemes     |
| ----------- | ------------------------- | ------------------------- | -------------------------------------------------------------- | --------------------------- | -------------------------------- |
| PkO         | Public Key Value          | Transaction Output        | P2(W)PKH                                                       | None at the moment          | Keytweak, taptweak, opret       |
| TxO2        | Transaction Output        | Transaction Output        | Requires deterministic commitments on Bitcoin                  | RGBv1 (universal)           | Keytweak, tapret, opret         |
| PkI         | Public Key Value          | Transaction Input         | Taproot only & not compatible with legacy wallets              | Bitcoin-based identities    | Sigtweak, witweak               |
| TxO1        | Transaction Output        | Transaction Input         | Taproot only & not compatible with legacy wallets              | None at the moment          | Sigtweak, witweak               |


Nie będziemy zagłębiać się w szczegóły każdej z tych konfiguracji, ponieważ w RGB zdecydowaliśmy się użyć **punktu wyjścia_ jako definicji Seal** i umieścić _commitment_ na wyjściu transakcji wydającej ten _punkt wyjścia_. Możemy zatem wprowadzić następujące koncepcje dla sequela:




- "Seal Definition"** : Dany _outpoint_ (identyfikowany przez txid + nr wyjścia) ;
- "Seal zamknięcie "**: Transakcja, która spędza ten _outpoint_, w której _commitment_ jest dodawany do wiadomości.


Ten schemat został wybrany ze względu na jego kompatybilność z architekturą RGB, ale inne konfiguracje mogą być przydatne do różnych zastosowań.


"O2" w "TxO2" przypomina nam, że zarówno definicja, jak i zamknięcie opierają się na wydatkowaniu (lub tworzeniu) wyjścia transakcji.


### Przykład wykresu TxO2


Dla przypomnienia, zdefiniowanie _pieczęci jednorazowego użytku_ niekoniecznie wymaga opublikowania transakcji On-Chain. Wystarczy, że Alice, na przykład, ma już niewydany UTXO. Może zdecydować: "Ten _outpoint_ (już istniejący) jest teraz moim Seal". Odnotowuje to lokalnie (_po stronie klienta_) i dopóki ten UTXO nie zostanie wydany, Seal jest uważany za otwarty.


![RGB-Bitcoin](assets/fr/024.webp)


W dniu, w którym chce zamknąć Seal (aby zasygnalizować zdarzenie lub Anchor konkretną wiadomość), wydaje ten UTXO w nowej transakcji (transakcja ta jest często nazywana "_transakcją świadka_" (niezwiązaną z _segwit_, to tylko termin, który jej nadajemy). Ta nowa transakcja będzie zawierać _commitment_ do wiadomości.


![RGB-Bitcoin](assets/fr/025.webp)


Należy zauważyć, że w tym przykładzie :




- Nikt oprócz Boba (lub osób, którym Alicja zdecyduje się ujawnić pełny dowód) nie będzie wiedział, że w tej transakcji ukryta jest pewna wiadomość;
- Każdy może zobaczyć, że _outpoint_ został wydany, ale tylko Bob posiada dowód, że wiadomość jest faktycznie zakotwiczona w transakcji.


Aby zilustrować ten schemat TxO2, możemy użyć _pieczęci jednorazowego użytku_ jako mechanizmu unieważniania klucza PGP. Zamiast publikować certyfikat unieważnienia na serwerach, Alice może powiedzieć: "To wyjście Bitcoin, jeśli zostanie wydane, oznacza, że mój klucz PGP został unieważniony".


Alice ma zatem określony UTXO, z którym lokalnie (po stronie klienta) powiązany jest określony stan lub dane (znane tylko jej).


Alicja informuje Boba, że jeśli UTXO zostanie wydany, określone zdarzenie zostanie uznane za zaistniałe. Z zewnątrz widzimy tylko transakcję Bitcoin; ale Bob wie, że ten wydatek ma ukryte znaczenie.


![RGB-Bitcoin](assets/fr/026.webp)


Gdy Alicja wydaje UTXO, zamyka Seal na wiadomości wskazującej jej nowy klucz lub po prostu unieważnienie starego. W ten sposób każdy, kto monitoruje On-Chain, zobaczy, że UTXO został wydany, ale tylko ci, którzy mają pełny dowód, będą wiedzieć, że jest to właśnie unieważnienie klucza PGP.


![RGB-Bitcoin](assets/fr/027.webp)


Aby Bob lub ktokolwiek inny mógł sprawdzić ukrytą wiadomość, Alice musi dostarczyć mu informacje off-chain.


![RGB-Bitcoin](assets/fr/028.webp)


Alice musi zatem dostarczyć Bobowi :




- Sama wiadomość (na przykład nowy klucz PGP) ;
- Kryptograficzny dowód, że wiadomość była zaangażowana w transakcję (znany jako _extra transaction proof_ lub _anchor_).


![RGB-Bitcoin](assets/fr/029.webp)


Strony trzecie nie mają takich informacji. Widzą tylko, że wydano UTXO. Poufność jest zatem zapewniona.


Aby wyjaśnić strukturę, podsumujmy proces w dwóch transakcjach:




- Transakcja 1**: Zawiera _definicję uszczelnienia_, tj. _punkt wyjścia_, który będzie służył jako Seal.


![RGB-Bitcoin](assets/fr/031.webp)




- Transakcja 2**: Wydaje ten _outpoint_. Powoduje to zamknięcie Seal i, w tej samej transakcji, wstawia _commitment_ do wiadomości.


![RGB-Bitcoin](assets/fr/033.webp)


Dlatego drugą transakcję nazywamy "transakcją świadka".


Aby zilustrować to z innej perspektywy, możemy przedstawić dwie warstwy:




- Górny Layer (Blockchain, publiczny)**: wszyscy widzą transakcję i wiedzą, że _outpoint_ został wydany;
- Niższy Layer (po stronie klienta, prywatny)** : tylko Alicja (lub osoba zainteresowana) wie, że ten wydatek odpowiada takiej a takiej wiadomości, poprzez dowód kryptograficzny i wiadomość, którą przechowuje lokalnie.


![RGB-Bitcoin](assets/fr/034.webp)


Jednak przy zamykaniu Seal pojawia się pytanie, gdzie należy wstawić _zobowiązanie_


W poprzedniej sekcji krótko wspomnieliśmy, w jaki sposób model Client-side Validation można zastosować do RGB i innych systemów. Tutaj zajmiemy się częścią dotyczącą **deterministycznych zobowiązań Bitcoin** i tym, jak zintegrować je z transakcją. Chodzi o to, aby zrozumieć, dlaczego próbujemy wstawić pojedynczy Commitment do _transakcji świadka_, a przede wszystkim, jak zapewnić, że nie mogą istnieć żadne inne nieujawnione konkurencyjne zobowiązania.


### Lokalizacje Commitment w transakcji


Kiedy dajesz komuś dowód, że pewna wiadomość jest osadzona w transakcji, musisz być w stanie zagwarantować, że w tej samej transakcji nie ma innej formy Commitment (drugiej, ukrytej wiadomości), która nie została ci ujawniona. Aby Client-side Validation pozostał odporny, potrzebny jest **deterministyczny** mechanizm umieszczania pojedynczego _commitment_ w transakcji, która zamyka _single-use seal_.


Transakcja _świadka_ wydaje słynny UTXO (lub _definicję pieczęci_), a wydatek ten odpowiada zamknięciu Seal. Technicznie rzecz biorąc, wiemy, że każdy outpoint może być wydany tylko raz. To właśnie leży u podstaw odporności Bitcoin na podwójne wydatki. Ale transakcja wydatkowania może mieć kilka _wejść_, kilka _wyjść_ lub być złożona w złożony sposób (coinjoins, Lightning channels itp.). Dlatego musimy jasno zdefiniować, gdzie wstawić _commitment_ w tej strukturze, jednoznacznie i jednolicie.


Niezależnie od metody (PkO, TxO2 itp.), można wstawić _commitment_:




- Na wejściu** przez :
    - Sigtweak** (modyfikuje składnik `r` podpisu ECDSA, podobny do zasady "Sign-to-Contract") ;
    - Witweak** (dane _segregowanego świadka_ transakcji są modyfikowane).
- Na wyjściu** przez :
    - Keytweak** (klucz publiczny odbiorcy jest "modyfikowany" wraz z wiadomością);
    - Opret** (wiadomość jest umieszczana w niewydawalnym wyjściu `OP_RETURN`);
    - Tapret** (lub _Taptweak_), który opiera się na Taproot w celu wstawienia Commitment do części skryptowej klucza Taproot, modyfikując w ten sposób deterministycznie klucz publiczny.


![RGB-Bitcoin](assets/fr/035.webp)


Oto szczegóły każdej z metod:


![RGB-Bitcoin](assets/fr/038.webp)


***Sig tweak (sign-to-Contract) :***


Wcześniejszy schemat obejmował wykorzystanie losowej części podpisu (ECDSA lub Schnorr) w celu osadzenia _commitment_: jest to technika znana jako "**Sign-to-Contract**". Losowo wygenerowany Nonce zastępuje się Hash zawierającym dane. W ten sposób podpis niejawnie ujawnia twój Commitment, bez dodatkowego miejsca w transakcji. Takie podejście ma wiele zalet:




- Brak przeciążenia On-Chain (używasz tego samego miejsca co podstawowy Nonce);
- Teoretycznie może to być dość dyskretne, ponieważ Nonce jest początkowo losowym punktem odniesienia.


Pojawiły się jednak 2 główne wady:




- Multisig przed Taproot: gdy masz kilku sygnatariuszy, musisz zdecydować, który podpis będzie nosił _commitment_. Podpisy mogą być uporządkowane w różny sposób, a jeśli sygnatariusz odmówi, tracisz kontrolę nad wynikiem _commitment_;
- MuSig i współdzielony Nonce: w przypadku Schnorr Multisig (*MuSig*) generowanie Nonce jest algorytmem wielostronnym, a indywidualne dostosowanie Nonce staje się praktycznie niemożliwe.


W praktyce **sig tweak** nie jest również zbyt kompatybilny z istniejącym sprzętem (portfele sprzętowe) i formatami (Lightning itp.). Tak więc ten świetny pomysł to Hard do wprowadzenia w życie.


***Key tweak (pay-to-Contract) :***


Funkcja **key tweak** wykorzystuje historyczną koncepcję _pay-to-contract_. Bierzemy klucz publiczny `X` i modyfikujemy go poprzez dodanie wartości `H(message)`. W szczególności, jeśli `X = x * G` i `h = H(message)`, to nowym kluczem będzie `X' = X + h * G`. Ten zmodyfikowany klucz ukrywa Commitment do "wiadomości". Posiadacz oryginalnego klucza prywatnego może, dodając `h` do swojego klucza prywatnego `x`, udowodnić, że posiada klucz do wydania danych wyjściowych. W teorii jest to eleganckie, ponieważ :




- Polecenie _commitment_ jest wprowadzane bez dodawania dodatkowych pól;
- Nie przechowujesz żadnych dodatkowych danych On-Chain.


W praktyce napotykamy jednak na następujące trudności:




- Portfele nie rozpoznają już standardowego klucza publicznego, ponieważ został on "zmodyfikowany", więc nie mogą łatwo powiązać UTXO ze zwykłym kluczem;
- Portfele sprzętowe nie są przeznaczone do podpisywania kluczem, który nie pochodzi z ich standardowej derywacji;
- Musisz dostosować swoje skrypty, deskryptory itp.


W kontekście RGB ścieżka ta była przewidziana do 2021 r., ale okazała się zbyt skomplikowana, aby działała z obecnymi standardami i infrastrukturą.


***Witness tweak :***


Innym pomysłem, który niektóre protokoły, takie jak _inscriptions Ordinals_ wprowadziły w życie, jest umieszczenie danych bezpośrednio w sekcji "świadka" transakcji (stąd wyrażenie "witness tweak"). Jednak ta metoda :




- Sprawia, że zaangażowanie jest natychmiast widoczne (dosłownie wklejasz surowe dane do świadka);
- Może podlegać cenzurze (górnicy lub węzły mogą odmówić transmisji, jeśli jest zbyt duża lub ma inną arbitralną cechę);
- Zajmuje miejsce w blokach, co jest sprzeczne z celem RGB, jakim jest dyskrecja i lekkość.


Ponadto, witness został zaprojektowany tak, aby można go było przycinać w pewnych kontekstach, co może komplikować tworzenie solidnych dowodów.


***Open-return (opret) :***


Bardzo prosty w działaniu, `OP_RETURN` pozwala na przechowywanie Hash lub wiadomości w specjalnym polu transakcji. Ale jest to natychmiast wykrywalne: każdy widzi, że w transakcji jest _commitment_ i może to być ocenzurowane lub odrzucone, jak również dodanie dodatkowego wyjścia. Ponieważ zwiększa to przejrzystość i rozmiar, jest uważane za mniej satysfakcjonujące z punktu widzenia rozwiązania Client-side Validation.


```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|

1-byte       1-byte         32 bytes
```


### Tapret


Ostatnią opcją jest użycie **Taproot** (wprowadzonego w BIP341) ze schematem *Tapret*. *Tapret* jest bardziej złożoną formą deterministycznego Commitment, która przynosi poprawę w zakresie śladu na Blockchain i poufności operacji Contract. Główną ideą jest ukrycie Commitment w części `Script Path Spend` transakcji [Taproot] (https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki).


![RGB-Bitcoin](assets/fr/036.webp)


Przed opisaniem, w jaki sposób Commitment jest wstawiany do transakcji Taproot, przyjrzyjmy się **dokładnej formie** Commitment, która musi **imperatywnie** odpowiadać 64-bajtowemu ciągowi [skonstruowanemu] (https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) w następujący sposób:


```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|

TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```




- 29 bajtów `OP_RESERVED`, po których następuje `OP_RETURN`, a następnie `OP_PUSHBYTE_33`, tworzą 31-bajtową część _prefix_;
- Następnie pojawia się 32-bajtowy _commitment_ (zwykle Merkle Root z **MPC**), do którego dodajemy 1 bajt **Nonce** (łącznie 33 bajty dla tej drugiej części).


Tak więc 64-bajtowa metoda `Tapret` wygląda jak `Opret`, do której dodaliśmy 29 bajtów `OP_RESERVED` i dodatkowy bajt jako Nonce.


Aby zachować elastyczność w zakresie wdrażania, poufności i skalowania, schemat Tapret uwzględnia różne przypadki użycia, w zależności od wymagań:




- Unikalne włączenie transakcji Tapret Commitment do transakcji Taproot bez wcześniej istniejącej struktury ścieżki skryptu;
- Integracja Tapret Commitment z transakcją Taproot już wyposażoną w ścieżkę skryptu.


Przyjrzyjmy się bliżej każdemu z tych dwóch scenariuszy.


#### Włączenie Tapret bez istniejącej ścieżki skryptu


W tym pierwszym przypadku zaczynamy od klucza wyjściowego Taproot (*Taproot Output Key*) `Q`, który zawiera tylko wewnętrzny klucz publiczny `P` *(Internal Key*), bez powiązanej ścieżki skryptu (*Script Path*):


![RGB-Bitcoin](assets/fr/047.webp)




- `P`: wewnętrzny klucz publiczny dla _Key Path Spend_.
- `G`: punkt generujący krzywej eliptycznej [secp256k1](https://en.Bitcoin.it/wiki/Secp256k1).
- t = tH_TWEAK(P)` jest współczynnikiem tweak, obliczonym za pomocą _tagged hash_ (np. `SHA-256(SHA-256(TapTweak) || P)`), zgodnie z [BIP86](https://github.com/Bitcoin/bips/blob/master/bip-0086.mediawiki#Address-derivation). Dowodzi to, że nie ma ukrytego skryptu.


Aby dołączyć **Tapret** Commitment, dodaj **Ścieżkę skryptu wydatku** z **unikalnym skryptem** w następujący sposób:


![RGB-Bitcoin](assets/fr/048.webp)




- t = tH_TWEAK(P || Script_root)` staje się nowym współczynnikiem tweak, włączając **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` reprezentuje korzeń tego **skryptu**, który jest po prostu Hash typu `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.


Dowód włączenia i unikalności w drzewie Taproot sprowadza się tutaj do pojedynczego wewnętrznego klucza publicznego `P`.


#### Integracja Tapret z wcześniej istniejącą ścieżką skryptu


Drugi scenariusz dotyczy bardziej złożonego wyjścia `Q` Taproot**, które zawiera już kilka skryptów. Na przykład, mamy drzewo 3 skryptów:


![RGB-Bitcoin](assets/fr/049.webp)




- tH_LEAF(x)` oznacza znormalizowaną oznaczoną funkcję Hash skryptu liścia.
- a, B, C` reprezentują skrypty już zawarte w strukturze Taproot.


Aby dodać Tapret Commitment, musimy wstawić *niewydawalny skrypt* na pierwszym poziomie drzewa, przesuwając istniejące skrypty o jeden poziom w dół. Wizualnie drzewo staje się :


![RGB-Bitcoin](assets/fr/050.webp)




- tHABC` reprezentuje oznaczony Hash grupy najwyższego poziomu `A, B, C`.
- tHT` reprezentuje Hash skryptu odpowiadającego 64-bajtowemu `Tapret`.


Zgodnie z regułami Taproot, każda gałąź/liść musi być połączona zgodnie z porządkiem leksykograficznym Hash. Istnieją dwa możliwe przypadki:




- `tHT` > `tHABC`: Tapret Commitment przesuwa się na prawo od drzewa. Dowód wyjątkowości wymaga tylko `tHABC` i `P` ;
- tHT` < `tHABC`**: Tapret Commitment umieszczony jest po lewej stronie. Aby udowodnić, że nie istnieje żaden inny Tapret Commitment po prawej stronie, `tHAB` i `tHC` muszą zostać ujawnione aby zademonstrować brak jakiegokolwiek innego takiego skryptu.


Przykład wizualny dla pierwszego przypadku (`tHABC < tHT`):


![RGB-Bitcoin](assets/fr/051.webp)


Przykład dla drugiego przypadku (`tHABC > tHT`):


![RGB-Bitcoin](assets/fr/052.webp)


#### Optymalizacja za pomocą Nonce


Aby poprawić poufność, możemy "wydobyć" (bardziej trafnym określeniem byłoby "bruteforcing") wartość `<Nonce>` (ostatni bajt 64-bajtowego `Tapret`), próbując uzyskać Hash `tHT` taki, że `tHABC < tHT`. W tym przypadku Commitment jest umieszczany po prawej stronie, oszczędzając użytkownikowi konieczności ujawniania całej zawartości istniejących skryptów w celu udowodnienia unikalności Tapreta.


Podsumowując, `Tapret` oferuje dyskretny i deterministyczny sposób włączenia Commitment do transakcji Taproot, przy jednoczesnym poszanowaniu wymogu unikalności i jednoznaczności niezbędnej dla logiki RGB Client-side Validation i Single-Use Seal.


#### Prawidłowe wyjścia


W przypadku transakcji RGB Commitment główny wymóg dla ważnego schematu Bitcoin Commitment jest następujący: Transakcja (*Witness Transaction*) musi w sposób możliwy do udowodnienia zawierać pojedynczy Commitment. Wymóg ten uniemożliwia skonstruowanie alternatywnej historii dla zweryfikowanych danych po stronie klienta w ramach tej samej transakcji. Oznacza to, że komunikat, wokół którego zamyka się pieczęć _single-use_, jest unikalny.


Aby spełnić tę zasadę i niezależnie od liczby wyjść w transakcji, wymagamy, aby **jedno i tylko jedno wyjście** mogło zawierać Commitment (*Commitment*). Dla każdego z zastosowanych schematów (*Opret* lub *Tapret*), jedynymi poprawnymi wyjściami, które mogą zawierać RGB _commitment_ są :




- Pierwsze wyjście `OP_RETURN` (jeśli występuje) dla schematu *Opret*;
- Pierwsze wyjście Taproot (jeśli występuje) dla schematu *Tapret*.


Należy zauważyć, że jest całkiem możliwe, aby transakcja zawierała pojedynczy `Opret` Commitment i pojedynczy `Tapret` Commitment w dwóch oddzielnych wyjściach. Dzięki deterministycznej naturze Seal Definition, te dwa zobowiązania odpowiadają dwóm odrębnym fragmentom danych zatwierdzonych po stronie klienta.


### Analiza i praktyczne wybory w RGB


Kiedy rozpoczęliśmy RGB, przejrzeliśmy wszystkie te metody, aby określić, gdzie i jak umieścić _commitment_ w transakcji w deterministyczny sposób. Zdefiniowaliśmy pewne kryteria:




- Kompatybilność z różnymi scenariuszami (np. Multisig, Lightning, portfele sprzętowe itp.);
- Wpływ na przestrzeń On-Chain ;
- Trudność wdrożenia i utrzymania;
- Poufność i odporność na cenzurę.


| Method                                             | On-chain trace & size | Client-side size | Wallet Integration | Hardware Compatibility | Lightning Compatibility | Taproot Compatibility |
| -------------------------------------------------- | --------------------- | ---------------- | ------------------ | ---------------------- | ---------------------- | --------------------- |
| Keytweak (deterministic P2C)                      | 🟢                     | 🟡                 | 🔴                   | 🟠                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🟢 MuSig  |
| Sigtweak (deterministic S2C)                      | 🟢                     | 🟢                 | 🟠                   | 🔴                     | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🔴 MuSig  |
| Opret (OP_RETURN)                                 | 🔴                     | 🟢                 | 🟢                   | 🟠                     | 🔴 BOLT, 🟠 Bifrost     | -                     |
| Tapret Algorithm: top-left node                   | 🟠                     | 🔴                 | 🟠                   | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Tapret Algorithm #4: any node + proof             | 🟢                     | 🟠                 | 🟠                   | 🟢                     | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Deterministic Commitment Scheme                               | Standard       | On-Chain Cost                                                                                                          | Proof Size on Client Side                                                                                       |
| ------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Keytweak (Deterministic P2C)                                  | LNPBP-1, 2     | 0 bytes                                                                                                                | 33 bytes (non-tweaked key)                                                                                       |
| Sigtweak (Deterministic S2C)                                  | WIP (LNPBP-39) | 0 bytes                                                                                                                | 0 bytes                                                                                                          |
| Opret (OP_RETURN)                                             | -              | 36 (v)bytes (additional TxOut)                                                                                         | 0 bytes                                                                                                          |
| Tapret Algorithm: top-left node                               | LNPBP-6        | 32 bytes in the witness (8 vbytes) for any n-of-m multisig and spending through script path                           | 0 bytes on scriptless scripts taproot ~270 bytes in a single script case, ~128 bytes if multiple scripts       |
| Tapret Algorithm #4: any node + uniqueness proof              | LNPBP-6        | 32 bytes in the witness (8 vbytes) for single script cases, 0 bytes in the witness in most other cases                | 0 bytes on scriptless scripts taproot, 65 bytes until the Taptree contains a dozen scripts                      |


| Layer                          | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | On-Chain Cost (Bytes/vbytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) | Client-Side Cost (Bytes) |
| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| **Type**                       | **Tapret**                   | **Tapret #4**                | **Keytweak**                 | **Sigtweak**                 | **Opret**                    | **Tapret**               | **Tapret #4**            | **Keytweak**             | **Sigtweak**             | **Opret**                |
| Single-sig                     | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | 0?                       | 0                        |
| MuSig (n-of-n)                 | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | ? > 0                    | 0                        |
| Multi-sig 2-of-3               | 32/8                         | 32/8 or 0                    | 0                            | n/a                          | 32                           | ~270                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 3-of-5               | 32/8                         | 32/8 or 0                    | 0                            | n/a                          | 32                           | ~340                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 2-of-3 with timeouts | 32/8                         | 0                            | 0                            | n/a                          | 32                           | 64                       | 65                       | 32                       | n/a                      | 0                        |


| Layer                            | On-Chain Cost (vbytes) | On-Chain Cost (vbytes) | On-Chain Cost (vbytes) | Client-Side Cost (bytes) | Client-Side Cost (bytes) |
| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |
| **Type**                         | **Base**               | **Tapret #2**          | **Tapret #4**          | **Tapret #2**            | **Tapret #4**            |
| MuSig (n-of-n)                   | 16.5                   | 0                      | 0                      | 0                        | 0                        |
| FROST (n-of-m)                   | ?                      | 0                      | 0                      | 0                        | 0                        |
| Multi_a (n-of-m)                 | 1+16n+8m               | 8                      | 8                      | 33 * m                   | 65                       |
| Branch MuSig / Multi_a (n-of-m)  | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| With timeouts (n-of-m)           | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| Method                                    | Privacy & Scalability | Interoperability | Compatibility | Portability | Complexity |
| ----------------------------------------- | ---------------------- | ---------------- | ------------- | ----------- | ---------- |
| Keytweak (Deterministic P2C)              | 🟢                      | 🔴               | 🔴            | 🟡          | 🟡         |
| Sigtweak (Deterministic S2C)              | 🟢                      | 🔴               | 🔴            | 🟢          | 🔴         |
| Opret (OP_RETURN)                         | 🔴                      | 🟠               | 🔴            | 🟢          | 🟢         |
| Algo Tapret: Top-left node                | 🟠                      | 🟢               | 🟢            | 🔴          | 🟠         |
| Algo Tapret #4: Any node + proof          | 🟢                      | 🟢               | 🟢            | 🟠          | 🔴         |






W trakcie badania stało się jasne, że żaden ze schematów Commitment nie jest w pełni kompatybilny z obecnym standardem Lightning (który nie wykorzystuje Taproot, _muSig2_ ani dodatkowej obsługi _commitment_). Trwają prace nad modyfikacją konstrukcji kanału Lightning (*BiFrost*), aby umożliwić wstawianie zobowiązań RGB. Jest to kolejny obszar, w którym musimy dokonać przeglądu struktury transakcji, kluczy i sposobu podpisywania aktualizacji kanałów.


Analiza wykazała, że w rzeczywistości inne metody (key tweak, sig tweak, witness tweak itp.) powodowały inne formy komplikacji:




- Albo mamy duży wolumen On-Chain;
- Albo istnieje radykalna niezgodność z istniejącym kodem Wallet;
- Albo rozwiązanie nie jest opłacalne w przypadku braku współpracy Multisig.


W przypadku RGB wyróżniają się w szczególności dwie metody: ***Opret*** i ***Tapret***, obie sklasyfikowane jako "Transaction Output" i kompatybilne z trybem TxO2 używanym przez protokół.


### Zobowiązania wieloprotokołowe - MPC


W tej sekcji przyjrzymy się, jak **RGB** obsługuje agregację wielu kontraktów (lub, bardziej precyzyjnie, ich _transition bundles_) w ramach pojedynczego Commitment (*Commitment*) zarejestrowanego w transakcji Bitcoin poprzez deterministyczny schemat (zgodnie z `Opret` lub `Tapret`). Aby to osiągnąć, kolejność merkelizacji różnych kontraktów odbywa się w strukturze zwanej **MPC Tree** (_Multi Protocol Commitment Tree_). W tej sekcji przyjrzymy się konstrukcji tego drzewa MPC, jak uzyskać jego korzeń i jak wiele kontraktów może współdzielić tę samą transakcję w sposób poufny i jednoznaczny.


Multi Protocol Commitment (MPC) został zaprojektowany, aby zaspokoić dwie potrzeby:




- Konstrukcja `mpc::Commitment` Hash: zostanie ona włączona do Bitcoin Blockchain zgodnie ze schematem `Opret` lub `Tapret` i musi odzwierciedlać wszystkie zmiany stanu, które mają zostać zatwierdzone;
- Jednoczesne przechowywanie wielu kontraktów w pojedynczym _commitment_, umożliwiające zarządzanie oddzielnymi aktualizacjami wielu aktywów lub kontraktów RGB w pojedynczej transakcji Bitcoin.


Mówiąc konkretnie, każdy pakiet _transition bundle_ należy do konkretnego Contract. Wszystkie te informacje są wstawiane do **drzewa MPC**, którego korzeń (`mpc::Root`) jest następnie ponownie hashowany w celu uzyskania `mpc::Commitment`. To właśnie ten ostatni Hash jest umieszczany w transakcji Bitcoin (_witness transaction_), zgodnie z wybraną metodą deterministyczną.


![RGB-Bitcoin](assets/fr/042.webp)


#### MPC Root Hash


Wartość faktycznie zapisana On-Chain (w `Opret` lub `Tapret`) jest nazywana `mpc::Commitment`. Jest ona obliczana w postaci [BIP-341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki), zgodnie ze wzorem :


```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```


gdzie :




- `mpc_tag` jest tagiem: `urn:ubideco:mpc:Commitment#2024-01-31`, wybrany zgodnie z [RGB tagging conventions](https://github.com/RGB-WG/RGB-core/blob/master/doc/Commitments.md);
- `depth` (1 bajt) wskazuje głębokość *drzewa MPC*;
- cofactor` (16 bitów, w Little Endian) jest parametrem używanym do promowania unikalności pozycji przypisanych do każdego Contract w drzewie;
- `mpc::Root` jest korzeniem *MPC Tree*, obliczonym zgodnie z procesem opisanym w następnej sekcji.


![RGB-Bitcoin](assets/fr/044.webp)


#### Budowa drzewa MPC


Aby zbudować to drzewo MPC, musimy upewnić się, że każdy Contract odpowiada unikalnej pozycji liścia. Załóżmy, że mamy :




- c` kontrakty do uwzględnienia, indeksowane przez `i` w `i = {0,1,...,C-1}` ;
- Dla każdego Contract `c_i`, mamy identyfikator `ContractId(i) = c_i`.


Następnie konstruujemy drzewo o szerokości `w` i głębokości `d` takie, że `2^d = w`, z `w > C`, tak że każdy Contract może być umieszczony w osobnym _liściu_. Pozycja `pos(c_i)` każdego Contract w drzewie jest określona przez :


```txt
pos(c_i) = c_i mod (w - cofactor)
```


gdzie `kofaktor` jest liczbą całkowitą, która zwiększa prawdopodobieństwo uzyskania odrębnych pozycji dla każdego Contract. W praktyce budowa odbywa się w procesie iteracyjnym:




- Zaczynamy od minimalnej głębokości (umownie `d=3`, aby ukryć dokładną liczbę kontraktów);
- Próbujemy różnych `współczynników` (do `w/2` lub maksymalnie 500 ze względu na wydajność);
- Jeśli nie uda nam się ustawić wszystkich kontraktów bez kolizji, zwiększamy `d` i zaczynamy od nowa.


Celem jest uniknięcie zbyt wysokich drzew, przy jednoczesnym utrzymaniu ryzyka kolizji na minimalnym poziomie. Należy zauważyć, że zjawisko kolizji wynika z logiki rozkładu losowego, związanej z [Paradoksem rocznicowym] (https://en.wikipedia.org/wiki/Birthday_problem).


#### Zamieszkane liście


Po uzyskaniu `C` odrębnych pozycji `pos(c_i)` dla kontraktów `i = {0,1,...,C-1}`, każdy arkusz jest wypełniany funkcją Hash (*oznaczoną Hash*):


```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```


gdzie :




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, jest zawsze wybierany zgodnie z konwencjami Merkle RGB;
- `0x10` identyfikuje _liść kontraktu_ ;
- `c_i` to 32-bajtowy identyfikator Contract (pochodzący z Genesis Hash);
- bundleId(c_i)` jest 32-bajtowym Hash opisującym zbiór `State Transitions` względem `c_i` (zebranych w *Transition Bundle*).


#### Niezamieszkane liście


Pozostałe liście, które nie zostały przypisane do Contract (tj. liście `w - C`), są wypełnione wartością "fikcyjną" (_entropy leaf_):


```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```


gdzie :




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, jest zawsze wybierany zgodnie z konwencjami Merkle RGB;
- `0x11` oznacza _liść entropii_ ;
- `entropy` to losowa wartość 64 bajtów, wybrana przez osobę budującą drzewo;
- `j` jest pozycją (w 32 bitach Little Endian) tego liścia w drzewie.


#### Węzły MPC


Po wygenerowaniu liści `w` (zamieszkałych lub nie), przechodzimy do merkelizacji. Wszystkie wewnętrzne węzły są hashowane w następujący sposób:


```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```


gdzie :




- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, jest zawsze wybierany zgodnie z konwencjami Merkle RGB;
- b` jest _współczynnikiem rozgałęzienia_ (8 bitów). Najczęściej `b=0x02`, ponieważ drzewo jest binarne i kompletne;
- d` to głębokość węzła w drzewie;
- `w` to szerokość drzewa (w 256-bitowym binarnym Little Endian);
- tH1` i `tH2` to skróty węzłów potomnych (lub liści), już obliczone jak pokazano powyżej.


Postępując w ten sposób, otrzymujemy korzeń `mpc::Root`. Następnie możemy obliczyć `mpc::Commitment` (jak wyjaśniono powyżej) i wstawić go On-Chain.


Aby to zilustrować, wyobraźmy sobie przykład, w którym `C=3` (trzy kontrakty). Przyjmuje się, że ich pozycje to `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. Pozostałe liście (pozycje 0, 1, 3, 5, 6) są _liśćmi entropii_. Poniższy diagram pokazuje sekwencję skrótów do korzenia z :




- `BUNDLE_i`, który reprezentuje `BundleId(c_i)`;
- `tH_MPC_LEAF(A)` i tak dalej, które reprezentują liście (niektóre dla kontraktów, inne dla entropii);
- Każda gałąź `tH_MPC_BRANCH(...)` łączy skróty swoich dwóch dzieci.


Wynikiem końcowym jest **mpc::Root**, a następnie `mpc::Commitment`.


![RGB-Bitcoin](assets/fr/053.webp)


#### Kontrola wału MPC


Gdy weryfikator chce upewnić się, że `c_i` Contract (i jego `BundleId`) jest zawarty w końcowym `mpc::Commitment`, po prostu otrzymuje dowód Merkle. Dowód ten wskazuje węzły potrzebne do prześledzenia liści (w tym przypadku `c_i`'s _contract leaf_) z powrotem do korzenia. Nie ma potrzeby ujawniania całego *drzewa MPC*: chroni to poufność innych kontraktów.


W przykładzie, weryfikator `c_2` potrzebuje tylko pośredniego Hash (`tH_MPC_LEAF(D)`), dwóch `tH_MPC_BRANCH(...)`, dowodu pozycji `pos(c_2)` i wartości `cofactor`. Następnie może lokalnie zrekonstruować korzeń, a następnie ponownie obliczyć `mpc::Commitment` i porównać go z tym zapisanym w transakcji Bitcoin (w `Opret` lub `Tapret`).


![RGB-Bitcoin](assets/fr/054.webp)


Mechanizm ten zapewnia, że :




- Status odnoszący się do `c_2` jest rzeczywiście zawarty w zagregowanym bloku informacji (po stronie klienta);
- Nikt nie może zbudować alternatywnej historii z tą samą transakcją, ponieważ On-Chain _commitment_ wskazuje na pojedynczy korzeń MPC.


#### Podsumowanie struktury RPP


Multi Protocol Commitment* (MPC) jest zasadą, która umożliwia RGB agregację wielu kontraktów w pojedynczą transakcję Bitcoin, przy jednoczesnym zachowaniu unikalności zobowiązań i poufności wobec innych uczestników. Dzięki deterministycznej konstrukcji drzewa, każdemu Contract przypisana jest unikalna pozycja, a obecność "fikcyjnych" liści (*Entropy Leaves*) częściowo maskuje całkowitą liczbę kontraktów uczestniczących w transakcji.


Cały Merkle Tree nigdy nie jest przechowywany na kliencie. Po prostu generate _Ścieżka Merkle_ dla każdego Contract, który ma być przesłany do odbiorcy (który może następnie zweryfikować Commitment). W niektórych przypadkach może istnieć kilka zasobów, które przeszły przez ten sam UTXO. Można wtedy połączyć kilka ścieżek _Merkle_ w tak zwany _wieloprotokołowy blok Commitment_, aby uniknąć powielania zbyt dużej ilości danych.


Każdy dowód _Merkle'a_ jest zatem lekki, zwłaszcza że głębokość drzewa nie przekroczy 32 w RGB. Istnieje również pojęcie "bloku Merkle'a", który zachowuje więcej informacji (przekrój, entropia itp.), przydatnych do łączenia lub oddzielania kilku gałęzi.


Dlatego sfinalizowanie RGB zajęło tak dużo czasu. Mieliśmy ogólną wizję od 2019 roku: umieszczenie wszystkiego po stronie klienta, obieg tokenów off-chain. Ale szczegóły, takie jak sharding dla wielu kontraktów, struktura Merkle Tree, sposób obsługi kolizji i dowodów scalania... wszystko to wymagało iteracji.


### Kotwice: globalne zgromadzenie


Kontynuując konstrukcję naszych zobowiązań (`Opret` lub `Tapret`) i naszego MPC (*Multi Protocol Commitment*), musimy Address pojęcie **Anchor** w protokole RGB. Anchor jest strukturą walidowaną po stronie klienta, która łączy Elements potrzebne do zweryfikowania, czy Bitcoin Commitment faktycznie zawiera określone informacje umowne. Innymi słowy, Anchor podsumowuje wszystkie dane potrzebne do walidacji _zobowiązań_ opisanych powyżej.


Anchor składa się z trzech uporządkowanych pól:




- `txid`
- `MPC Proof`
- dodatkowy dowód transakcji - ETP


Każde z tych pól odgrywa rolę w procesie walidacji, niezależnie od tego, czy chodzi o odtworzenie podstawowej transakcji Bitcoin, czy też udowodnienie istnienia ukrytego Commitment (szczególnie w przypadku `Tapret`).


#### txid


Pole `txid` odpowiada 32-bajtowemu identyfikatorowi transakcji Bitcoin zawierającej `Opret` lub `Tapret` Commitment.


Teoretycznie możliwe byłoby znalezienie tego `txid` poprzez prześledzenie łańcucha przejść stanów, które same wskazują na każdy Witness Transaction, zgodnie z logiką Single-use Seals. Jednakże, aby ułatwić i przyspieszyć weryfikację, ten `txid` jest po prostu zawarty w Anchor, oszczędzając w ten sposób walidatorowi konieczności cofania się przez całą historię off-chain.


#### Dowód MPC


Drugie pole, `MPC Proof`, odnosi się do dowodu, że ten konkretny Contract (np. `c_i`) jest zawarty w _Multi Protocol Commitment_. Jest to kombinacja :




- `pos_i`, pozycja tego Contract w drzewie MPC;
- cofactor`, wartość zdefiniowana do rozwiązywania kolizji pozycji;
- `Merkle Proof`, tj. zestaw węzłów i skrótów używanych do rekonstrukcji korzenia MPC i sprawdzenia, czy identyfikator Contract i jego `Transition Bundle` są przypisane do korzenia.


Mechanizm ten został opisany w poprzedniej sekcji dotyczącej budowania *MPC Tree*, gdzie każdy Contract uzyskuje unikalny liść dzięki :


```txt
pos(c_i) = c_i mod (w - cofactor)
```


Następnie deterministyczny schemat merkelizacji jest używany do agregacji wszystkich liści (kontrakty + entropia). Na koniec, `MPC Proof` pozwala na lokalną rekonstrukcję korzenia i porównanie go z `mpc::Commitment` zawartym w On-Chain.


#### Dodatkowy dowód transakcji - ETP


Trzecie pole, **ETP**, zależy od typu używanego Commitment. Jeśli Commitment jest typu `Opret`, nie jest wymagany żaden dodatkowy dowód. Walidator sprawdza pierwsze wyjście `OP_RETURN` transakcji i znajduje tam bezpośrednio `mpc::Commitment`.


**Jeśli Commitment jest typu `Tapret`**, należy dostarczyć dodatkowy dowód zwany *Extra Transaction Proof - ETP*. Zawiera on :




- Wewnętrzny klucz publiczny (`P`) wyjścia Taproot, w którym osadzony jest *Commitment*;
- Węzły partnerskie `Script Path Spend` (gdy Tapret *Commitment* jest wstawiony do skryptu), aby udowodnić dokładną lokalizację tego skryptu w drzewie Taproot:
 - Jeśli `Tapret` *Commitment* znajduje się na prawej gałęzi, ujawniamy lewy węzeł (np. `tHABC`),
 - Jeśli `Tapret` *Commitment* znajduje się po lewej stronie, musisz ujawnić 2 węzły (np. `tHAB` i `tHC`), aby udowodnić, że żaden inny *Commitment* nie znajduje się po prawej stronie.
- Urządzenie `Nonce` może zostać użyte do "wydobycia" najlepszej konfiguracji, pozwalając na umieszczenie *Commitment* po prawej stronie drzewa (optymalizacja dowodu).


Ten dodatkowy dowód jest niezbędny, ponieważ w przeciwieństwie do `Opret`, `Tapret` Commitment jest zintegrowany ze strukturą skryptu Taproot, który wymaga ujawnienia części drzewa Taproot w celu poprawnej walidacji lokalizacji *Commitment*.


![RGB-Bitcoin](assets/fr/045.webp)


W związku z tym **Anchors** zawierają wszystkie informacje wymagane do walidacji Bitcoin Commitment w kontekście RGB. Wskazują one zarówno odpowiednią transakcję (`txid`), jak i dowód pozycjonowania Contract (`MPC Proof`), jednocześnie zarządzając dodatkowym dowodem (`ETP`) w przypadku `Tapret`. W ten sposób Anchor chroni integralność i unikalność stanu off-chain, zapewniając, że ta sama transakcja nie może zostać ponownie zinterpretowana dla innych danych umownych.


### Wnioski


W tym rozdziale omówimy :




- Jak zastosować koncepcję uszczelek jednorazowego użytku w Bitcoin (w szczególności poprzez _outpoint_);
- Różne metody deterministycznego wstawiania _commitment_ do transakcji (Sig tweak, Key tweak, witness tweak, OP_RETURN, Taproot/Tapret);
- Powody, dla których RGB koncentruje się na zobowiązaniach Tapret;
- Zarządzanie wieloma Contract poprzez _multi-protocol commitments_, niezbędne, jeśli nie chcesz ujawniać całego stanu lub innych umów, gdy chcesz udowodnić konkretny punkt;
- Widzieliśmy również rolę _Anchors_, które łączą wszystko razem (transakcja txid, Merkle Tree proof i Taproot proof) w jednym pakiecie.


W praktyce, techniczna implementacja jest podzielona pomiędzy kilka dedykowanych Rust _crates_ (w _client_side_validation_, _commit-verify_, _bp_core_, itp.) Podstawowe pojęcia są dostępne:


![RGB-Bitcoin](assets/fr/046.webp)


W następnym rozdziale przyjrzymy się czysto off-chain komponentowi RGB, a mianowicie logice Contract. Zobaczymy, w jaki sposób kontrakty RGB, zorganizowane jako częściowo replikowane _maszyny stanów nieskończonych_, osiągają znacznie wyższą ekspresywność niż skrypty Bitcoin, zachowując przy tym poufność swoich danych.


## Wprowadzenie do inteligentnych kontraktów i ich stanów


<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>


:::video id=db4ee09f-1352-4ad1-9f7a-c962df7ea9fa:::


W tym i następnym rozdziale przyjrzymy się pojęciu **Smart contract** w środowisku RGB i zbadamy różne sposoby, w jakie kontrakty te mogą definiować i ewoluować swój *stan*. Zobaczymy, dlaczego architektura RGB, wykorzystująca uporządkowaną sekwencję Pieczęci Jednorazowego Użytku, umożliwia wykonywanie różnych rodzajów ***Operacji Contract*** w skalowalny sposób i bez przechodzenia przez scentralizowany rejestr. Przyjrzymy się również fundamentalnej roli ***Business Logic*** w kształtowaniu ewolucji Contract State.


### Inteligentne kontrakty i cyfrowe prawa na okaziciela


Celem RGB jest zapewnienie infrastruktury do wdrażania inteligentnych kontraktów na Bitcoin. Przez "Smart contract" rozumiemy umowę między kilkoma stronami, która jest egzekwowana automatycznie i obliczeniowo, bez interwencji człowieka w celu egzekwowania klauzul. Innymi słowy, prawo Contract jest egzekwowane przez oprogramowanie, a nie przez zaufaną stronę trzecią.


Ta automatyzacja rodzi pytanie o decentralizację: w jaki sposób możemy uwolnić się od scentralizowanego rejestru (np. centralnej platformy lub bazy danych) w celu zarządzania wydajnością Ownership i Contract? Pierwotnym pomysłem, podjętym przez RGB, jest powrót do trybu Ownership znanego jako "instrumenty na okaziciela". W przeszłości niektóre papiery wartościowe (obligacje, akcje itp.) były emitowane na okaziciela, umożliwiając każdemu, kto fizycznie posiadał dokument, egzekwowanie swoich praw.


![RGB-Bitcoin](assets/fr/055.webp)


RGB stosuje tę koncepcję do świata cyfrowego: prawa (i obowiązki) są zawarte w danych, którymi się manipuluje off-chain, a status tych danych jest weryfikowany przez samych uczestników. Pozwala to, a priori, na znacznie większy stopień poufności i niezależności niż oferowany przez inne podejścia oparte na rejestrach publicznych.


### Wprowadzenie do statusu Smart contract RGB


Smart contract w RGB może być postrzegany jako maszyna stanów, zdefiniowana przez :




- A **State**, tj. zestaw informacji odzwierciedlających bieżącą konfigurację Contract;
- **Business Logic** (zestaw reguł), który opisuje, w jakich warunkach i przez kogo stan może być modyfikowany.


![RGB-Bitcoin](assets/fr/056.webp)


Ważne jest, aby zrozumieć, że umowy te nie ograniczają się do prostego transferu tokenów. Mogą one obejmować szeroką gamę zastosowań: od tradycyjnych aktywów (tokeny, akcje, obligacje) po bardziej złożoną mechanikę (prawa użytkowania, warunki handlowe itp.). W przeciwieństwie do innych blockchainów, w których kod Contract jest dostępny i wykonywalny przez wszystkich, podejście RGB dzieli dostęp i wiedzę o Contract na uczestników ("***Uczestnicy Contract***"). Istnieje kilka ról:




- Wystawca** lub twórca Contract, który definiuje Genesis Contract i jego zmienne początkowe;
- Strony z prawami** (*Ownership*) lub innymi możliwościami egzekwowania ;
- Obserwatorzy**, potencjalnie ograniczeni do oglądania pewnych informacji, ale którzy nie mogą wywoływać modyfikacji.


To rozdzielenie ról przyczynia się do odporności na cenzurę, zapewniając, że tylko upoważnione osoby mogą wchodzić w interakcje ze stanem umownym. Daje to również RGB możliwość skalowania horyzontalnego: większość walidacji odbywa się poza Blockchain, a tylko kotwice kryptograficzne (*zobowiązania*) są wpisane w Bitcoin.


### Status i Business Logic w RGB


Z praktycznego punktu widzenia, **Business Logic** Contract przyjmuje formę reguł i skryptów, zdefiniowanych w tym, co RGB nazywa **Schema**. Schema koduje :




- Struktura państwa (które pola są publiczne? Które pola są własnością których stron?
- Warunki ważności (co należy sprawdzić przed autoryzacją aktualizacji stanu?) ;
- Uprawnienia (kto może zainicjować *State Transition*? Kto może tylko obserwować?).


Jednocześnie **Contract State** często dzieli się na dwa komponenty:




- A **Global State**: część publiczna, potencjalnie obserwowalna przez wszystkich (w zależności od konfiguracji);
- Owned States**: części prywatne, przydzielone specjalnie właścicielom za pośrednictwem UTXO, o których mowa w logice Contract.


Jak zobaczymy w następnych rozdziałach, każda aktualizacja statusu (*Contract Operation*) musi zostać zadokowana do Bitcoin _commitment_ (poprzez `Opret` lub `Tapret`) i być zgodna ze skryptami *Business Logic*, aby została uznana za ważną.


### Contract Operacje: tworzenie i ewolucja państwa


We wszechświecie RGB, ***Contract Operation*** jest dowolnym zdarzeniem, które zmienia Contract ze **starego stanu** do **nowego stanu**. Operacje te przebiegają zgodnie z następującą logiką:




- Zwracamy uwagę na obecny status Contract;
- Stosujemy regułę lub operację (***State Transition***, ***Genesis***, jeśli jest to pierwszy stan, lub ***State Extension***, jeśli istnieje publiczny *Valency* do ponownego uruchomienia);
- Anchor modyfikujemy za pomocą nowego _commitment_ na Blockchain, zamykając jedną _single-use seal_ i tworząc kolejną;
- Zainteresowane podmioty praw zatwierdzają lokalnie (*po stronie klienta*), że przejście jest zgodne z *Schema* i że powiązana transakcja Bitcoin jest zarejestrowana On-Chain.


![RGB-Bitcoin](assets/fr/057.webp)


Wynikiem końcowym jest zaktualizowany Contract, teraz z innym stanem. To przejście nie wymaga, aby cała sieć Bitcoin była zainteresowana szczegółami, ponieważ tylko mały kryptograficzny odcisk palca (_commitment_) jest rejestrowany w Blockchain. Sekwencja Pieczęci Jednorazowego Użycia zapobiega jakiemukolwiek Double-spending lub podwójnemu użyciu stanu.


### Łańcuch operacyjny: od Genesis do Terminal State


Aby spojrzeć na to z perspektywy, RGB Smart contract zaczyna się od **Genesis**, pierwszego stanu. Następnie różne operacje Contract następują po sobie, tworząc DAG (*Directed Acyclic Graph*) operacji:




- Każde przejście opiera się na poprzednim stanie (lub kilku, w przypadku przejść zbieżnych);
- Porządek chronologiczny jest gwarantowany przez włączenie każdego przejścia do Bitcoin Anchor, oznaczonego czasem i niezmiennego dzięki konsensusowi Proof-of-Work ;
- Gdy nie są już wykonywane żadne operacje, osiągany jest **stan końcowy**: ostatni i kompletny stan Contract.


![RGB-Bitcoin](assets/fr/012.webp)


Ta topologia DAG (zamiast prostego łańcucha liniowego) odzwierciedla możliwość, że różne części Contract mogą ewoluować równolegle, o ile nie są ze sobą sprzeczne. RGB dba następnie o uniknięcie wszelkich niespójności poprzez weryfikację *po stronie klienta* każdego zaangażowanego uczestnika.


### Podsumowanie


Inteligentne kontrakty w RGB wprowadzają model cyfrowych instrumentów na okaziciela, zdecentralizowanych, ale zakotwiczonych w Bitcoin w celu oznaczania czasu i gwarantowania kolejności transakcji. Zautomatyzowana realizacja tych kontraktów opiera się na :




- A **Contract State*, wskazujący bieżącą konfigurację Contract (uprawnienia, salda, zmienne itp.);
- A **Business Logic** (*Schema*), definiujący, które przejścia są dozwolone i w jaki sposób muszą zostać zatwierdzone;
- Contract Operacje**, które aktualizują ten stan krok po kroku, dzięki zobowiązaniom zakotwiczonym w transakcjach Bitcoin.


W następnym rozdziale zajmiemy się bardziej szczegółowo konkretną reprezentacją tych ***stanów*** i ***przejść między stanami*** na poziomie off-chain oraz tym, jak odnoszą się one do UTXO i Single-use Seals wbudowanych w Bitcoin. Będzie to okazja, aby zobaczyć, jak wewnętrzna mechanika RGB, oparta na Client-side Validation, radzi sobie z utrzymaniem spójności inteligentnych kontraktów przy jednoczesnym zachowaniu poufności danych.


## Operacje RGB Contract


<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>


:::video id=1caec34d-f214-425b-a1a4-0a40ae7d3e0e:::


W tym rozdziale przyjrzymy się, jak działają operacje w inteligentnych kontraktach i przejścia stanów, ponownie w ramach protokołu RGB. Celem będzie również zrozumienie, w jaki sposób kilku uczestników współpracuje w celu przeniesienia Ownership aktywów.


### Przejścia stanów i ich mechanika


Ogólna zasada jest nadal taka sama jak w Client-side Validation, gdzie dane o stanie są przechowywane przez właściciela i zatwierdzane przez odbiorcę. Jednak specyfika RGB polega na tym, że Bob, jako odbiorca, prosi Alice o włączenie pewnych informacji do danych Contract, aby mieć rzeczywistą kontrolę nad otrzymanym zasobem, poprzez ukryte odniesienie do jednego z jego UTXO.


Aby zilustrować proces *State Transition* (który jest jedną z podstawowych operacji ***Contract*** w RGB), weźmy krok po kroku przykład transferu aktywów między Alice i Bobem:


**Sytuacja początkowa:**


Alice ma ***Stash RGB*** lokalnie zweryfikowanych danych (*po stronie klienta*). Ten Stash odnosi się do jednego z jej UTXO na Bitcoin. Oznacza to, że _seal definition_ w tych danych wskazuje na UTXO należący do Alice. Chodzi o to, aby umożliwić jej przeniesienie pewnych praw cyfrowych związanych z aktywem (np. tokenów RGB) na Boba.


![RGB-Bitcoin](assets/fr/058.webp)


**Bob ma również UTXO :**


Bob, z drugiej strony, ma co najmniej jeden własny UTXO, bez bezpośredniego połączenia z Alice. W przypadku, gdy Bob nie ma UTXO, nadal możliwe jest dokonanie transferu do niego przy użyciu samego *Witness Transaction*: wynik tej transakcji będzie wtedy zawierał Commitment (_commitment_) i domyślnie skojarzy Ownership nowego Contract z Bobem.


![RGB-Bitcoin](assets/fr/059.webp)


**Budowa nowej nieruchomości (*Nowy stan*) :**


Bob wysyła Alicji informacje zakodowane w postaci ***Invoice*** (bardziej szczegółowo omówimy budowę Invoice w późniejszych rozdziałach), prosząc ją o utworzenie nowego stanu zgodnego z regułami Contract. Stan ten będzie zawierał nowy *Seal Definition* wskazujący na jeden z UTXO Boba. W ten sposób Bob otrzymuje Ownership aktywów zdefiniowanych w tym nowym stanie, na przykład pewną ilość tokenów RGB.


![RGB-Bitcoin](assets/fr/060.webp)


**Przygotowanie przykładowej transakcji:**


Następnie Alice tworzy transakcję Bitcoin wydającą UTXO, do którego odwołano się w poprzednim Seal (tym, który legitymizował ją jako posiadacza). W wyniku tej transakcji, *Commitment* (poprzez `Opret` lub `Tapret`) jest wstawiany do Anchor nowego stanu RGB. Zobowiązania `Opret` lub `Tapret` pochodzą z drzewa *MPC* (jak pokazano w poprzednich rozdziałach), które może agregować kilka przejść z różnych kontraktów.


**Przesłanie *Consignment* do Boba:**


Przed rozgłaszaniem transakcji Alicja wysyła Bobowi ***Consignment*** zawierający wszystkie niezbędne dane *po stronie klienta* (jego *Stash*) i nowe informacje o stanie na korzyść Boba. W tym momencie Bob stosuje zasady konsensusu RGB:




- Zatwierdza on wszystkie dane RGB zawarte w *Consignment*, w tym nowy stan, który nadaje mu Ownership zasobu;
- Opierając się na *Anchors* zawartych w *Consignment*, weryfikuje chronologię transakcji świadków (od Genesis do ostatniego przejścia) i zatwierdza odpowiednie zobowiązania w Blockchain.


**Ukończenie przejścia:**


Jeśli Bob jest zadowolony, może wyrazić zgodę (na przykład podpisując *Consignment*). Alice może następnie rozgłosić przygotowaną przykładową transakcję. Po potwierdzeniu, zamyka to Seal poprzednio posiadany przez Alicję i formalizuje Ownership przez Boba. Zabezpieczenie przed Double-spending opiera się na tym samym mechanizmie, co w przypadku Bitcoin: UTXO jest wydawany, co dowodzi, że Alicja nie może go już ponownie wykorzystać.


![RGB-Bitcoin](assets/fr/061.webp)


Nowy stan odwołuje się teraz do UTXO Boba, dając Bobowi Ownership poprzednio posiadany przez Alicję. Wyjście Bitcoin, w którym zakotwiczone są dane RGB, staje się nieodwołalnym dowodem transferu Ownership.


Przykład minimalnej DAG (*Directed Acyclic Graph*) zawierającej dwie operacje Contract (**Genesis**, a następnie ***State Transition***) może zilustrować, w jaki sposób stan RGB (*po stronie klienta* Layer, na czerwono) łączy się z Bitcoin Blockchain (*Commitment* Layer, na pomarańczowo).


![RGB-Bitcoin](assets/fr/062.webp)


Pokazuje, że Genesis definiuje Seal (*Seal Definition*), a następnie *State Transition* zamyka ten Seal, aby utworzyć nowy w innym UTXO.


W tym kontekście, oto kilka przypomnień terminologii:




- Urządzenie ***Assignment*** łączy w sobie :
    - A ***Seal Definition*** (co wskazuje na UTXO);
    - Owned States**, tj. dane powiązane z Ownership (na przykład ilość przekazanych tokenów).
- A **Global State** łączy w sobie ogólne właściwości Contract, widoczne dla wszystkich i zapewniające globalną spójność ewolucji.


Przejścia stanów**, opisane w poprzednim rozdziale, są główną formą Contract Operation. Odnoszą się one do jednego lub więcej poprzednich stanów (z Genesis lub innego State Transition) i aktualizują je do nowego stanu.


![RGB-Bitcoin](assets/fr/063.webp)


Schemat ten pokazuje, jak w *Stanie Transition Bundle* można zamknąć kilka pieczęci w pojedynczej przykładowej transakcji, jednocześnie otwierając nowe pieczęcie. Rzeczywiście, interesującą cechą protokołu RGB jest jego zdolność do skalowania: kilka przejść można zagregować w Transition Bundle, przy czym każda agregacja jest powiązana z odrębnym liściem drzewa *MPC* (unikalny identyfikator pakietu). Dzięki mechanizmowi *Deterministic Bitcoin Commitment* (DBC), cała wiadomość jest wstawiana do wyjścia `Tapret` lub `Opret`, jednocześnie zamykając poprzednie pieczęcie i ewentualnie definiując nowe. Anchor* służy jako bezpośrednie połączenie pomiędzy Commitment przechowywanym w Blockchain a strukturą Client-side Validation (*po stronie klienta*).


W kolejnych rozdziałach przyjrzymy się wszystkim komponentom i procesom związanym z tworzeniem i walidacją State Transition. Większość z tych Elements jest częścią konsensusu RGB, zaimplementowanego w **RGB Core Library**.


### Transition Bundle


Na RGB możliwe jest powiązanie różnych przejść stanu należących do tego samego Contract (tj. dzielących ten sam **ContractId**, pochodzący z Genesis **OpId**). W najprostszym przypadku, tak jak między Alicją i Bobem w powyższym przykładzie, **Transition Bundle** zawiera tylko jedno przejście. Ale wsparcie dla operacji wielu graczy (takich jak coinjoins, otwarcia kanału Lightning itp.) oznacza, że kilku użytkowników może łączyć swoje przejścia stanu w jednym pakiecie.


Po zebraniu, przejścia te są zakotwiczone (przez mechanizm MPC + DBC) w pojedynczej transakcji Bitcoin:




- Każdy State Transition jest hashowany i grupowany w Transition Bundle;
- Transition Bundle jest hashowany i wstawiany do liścia drzewa MPC odpowiadającego temu Contract (BundleId);
- Drzewo MPC jest ostatecznie włączane przez `Opret` lub `Tapret` w Witness Transaction, co powoduje zamknięcie zużytych pieczęci i zdefiniowanie nowych pieczęci.


Technicznie rzecz biorąc, **BundleId** wstawiony do arkusza MPC jest uzyskiwany ze znacznika Hash zastosowanego do ścisłej serializacji pola *InputMap* pakietu:


```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```


W którym `bundle_tag = urn:lnp-bp:RGB:bundle#2024-02-03` na przykład.


*InputMap* jest strukturą danych, która wymienia, dla każdego wejścia `i` przykładowej transakcji, odniesienie do *OpId* odpowiedniego State Transition. Na przykład:


```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|

MapElement1                MapElement2                       MapElementN
```




- `N` to całkowita liczba wpisów w transakcji, które odnoszą się do `OpId`;
- opId(input_j)` jest identyfikatorem operacji jednego z przejść stanu obecnych w pakiecie.


Odwołując się do każdego wpisu tylko raz i w uporządkowany sposób, zapobiegamy dwukrotnemu wykorzystaniu tego samego Seal w dwóch jednoczesnych Przejściach Stanu.


### Generowanie stanu i stan aktywny


Przejścia stanów mogą być zatem wykorzystywane do przenoszenia Ownership aktywów z jednej osoby na drugą. Nie są to jednak jedyne możliwe operacje w protokole RGB. Protokół definiuje trzy **operacje Contract** :




- State Transition** ;
- Genesis** ;
- State Extension**.


Wśród nich, **Genesis** i **State Extension** są czasami nazywane "*operacjami generowania stanów*", ponieważ tworzą nowe stany bez natychmiastowego zamykania jakichkolwiek. Jest to bardzo ważny punkt: **Genesis** i **State Extension** nie wiążą się z zamknięciem Seal. Raczej definiują one nowy Seal, który następnie musi zostać wydany przez kolejny **State Transition**, aby został naprawdę zatwierdzony w historii Blockchain.


![RGB-Bitcoin](assets/fr/064.webp)


**Stan aktywny** Contract jest często definiowany jako zbiór najnowszych stanów wynikających z historii (DAG) transakcji, począwszy od Genesis i po wszystkich kotwicach w Bitcoin Blockchain. Wszelkie stare stany, które są już przestarzałe (tj. dołączone do zużytych UTXO), nie są już uważane za aktywne, ale pozostają niezbędne do sprawdzenia spójności historii.


### Genesis


Genesis jest punktem początkowym każdego RGB Contract. Jest on tworzony przez wystawcę Contract i określa parametry początkowe, zgodnie z **Schema**. W przypadku tokena RGB, Genesis może określać na przykład :




- Liczba pierwotnie utworzonych tokenów i ich właściciele;
- Całkowity możliwy pułap emisji ;
- Wszelkie zasady ponownego wydania i którzy uczestnicy są uprawnieni.


Będąc pierwszą transakcją w Contract, Genesis nie odnosi się do żadnego poprzedniego stanu, ani nie zamyka żadnego Seal. Jednak, aby pojawić się w historii i zostać zatwierdzonym, Genesis musi zostać ** skonsumowany** (zamknięty) przez pierwszy State Transition (często transakcja skanowania/autowydawania dla samego emitenta lub początkowa dystrybucja do użytkowników).


### State Extension


Rozszerzenia stanu** oferują oryginalną funkcję dla inteligentnych kontraktów. Umożliwiają one Redeem pewne prawa cyfrowe (*Valencies*) przewidziane w definicji Contract, bez natychmiastowego zamykania Seal. Najczęściej dotyczy to :




- Kwestie tokenów rozproszonych;
- Mechanizmy zamiany aktywów ;
- Warunkowe wznowienia (które mogą obejmować zniszczenie innych aktywów itp.).


Technicznie rzecz biorąc, State Extension odwołuje się do *Redeem* (szczególny rodzaj wejścia RGB), który odpowiada *Valency* zdefiniowanemu wcześniej (na przykład w Genesis lub innym State Transition). Definiuje on nowy Seal, dostępny dla osoby lub stanu, który z niego korzysta. Aby ten Seal stał się skuteczny, musi zostać wydany przez kolejny State Transition.


![RGB-Bitcoin](assets/fr/065.webp)


Na przykład: Genesis tworzy prawo do emisji (*Valency*). Może ono zostać wykonane przez uprawnionego uczestnika, który następnie tworzy State Extension :




- Odnosi się do Valency (Redeem);
- Tworzy on nowy *Assignment* (nowe dane *Owned State*) wskazujący na UTXO;
- Przyszły State Transition, wydany przez właściciela tego nowego UTXO, faktycznie przekaże lub rozprowadzi nowo wydane tokeny.


### Elementy składowe Contract Operation


Chciałbym teraz szczegółowo przyjrzeć się każdemu z Elements składających się na **Contract Operation** w RGB. Contract Operation to akcja, która modyfikuje stan Contract i która jest zatwierdzana po stronie klienta, w sposób deterministyczny, przez uprawnionego odbiorcę. W szczególności zobaczymy, w jaki sposób Contract Operation uwzględnia z jednej strony **stary stan** (*Old State*) Contract, a z drugiej definicję **nowego stanu** (*New State*).


```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |

+---------------------------------------------------------------------------------------------------------------------+
```


Jeśli spojrzymy na powyższy diagram, zobaczymy, że Contract Operation zawiera Elements odnoszące się do **Nowego Stanu** i inne odnoszące się do zaktualizowanego **Starego Stanu**.


Elements z **Nowego Stanu** to :




- Przypisania**, w których zdefiniowane są :
 - **Seal Definition**;
 - **Owned State**.
- **Global State**, który może być modyfikowany lub wzbogacany;
- Wartości**, ewentualnie zdefiniowane w State Transition lub Genesis.


**Stary stan** jest przywoływany przez :




- Wejścia**, które wskazują na *Przypisania* poprzednich przejść stanów (nieobecne w Genesis);
- Redeems**, które odnoszą się do wcześniej zdefiniowanych Valencies (tylko w State Extensions).


Ponadto Contract Operation zawiera bardziej ogólne pola specyficzne dla operacji:




- ffv` (*Fast-forward version*): 2-bajtowa liczba całkowita wskazująca wersję Contract;
- transitionType` lub ExtensionType`: 16-bitowa liczba całkowita określająca typ przejścia lub rozszerzenia, zgodnie z Business Logic;
- `ContractId`: 32-bajtowa liczba odnosząca się do *OpId* Contract Genesis. Zawarte w Transitions i Extensions, ale nie w Genesis;
- schemaId: obecny tylko w Genesis, jest to 32-bajtowy Hash reprezentujący strukturę (*Schema*) Contract;
- Testnet`: Wartość logiczna wskazująca, czy jesteś w sieci Testnet lub Mainnet. Tylko Genesis;
- altlayers1`: zmienna identyfikująca alternatywny Layer (Sidechain lub inny) użyty do danych Anchor oprócz Bitcoin. Występuje tylko w Genesis;
- metadata": pole, które może przechowywać tymczasowe informacje, przydatne do walidacji złożonego Contract, ale które nie mogą być rejestrowane w historii statusu końcowego.


Na koniec wszystkie te pola są kondensowane przez niestandardowy proces mieszania, aby uzyskać unikalny odcisk palca, `OpId`. Ten `OpId` jest następnie zintegrowany z Transition Bundle, umożliwiając jego uwierzytelnienie i walidację w ramach protokołu.


Każdy *Contract Operation* jest zatem identyfikowany przez 32-bajtowy Hash o nazwie `OpId`. Ten Hash jest obliczany przez SHA256 Hash wszystkich Elements składających się na operację. Innymi słowy, każdy *Contract Operation* ma swój własny kryptograficzny Commitment, który zawiera wszystkie dane potrzebne do weryfikacji autentyczności i spójności operacji.


RGB Contract jest następnie identyfikowany przez `ContractId`, pochodzący z `OpId` Genesis (ponieważ nie ma operacji przed Genesis). Konkretnie, bierzemy Genesis `OpId`, odwracamy kolejność bajtów i stosujemy kodowanie Base58. Kodowanie to sprawia, że `ContractId` jest łatwiejszy w obsłudze i rozpoznawaniu.


### Metody i reguły aktualizacji statusu


Contract State** reprezentuje zestaw informacji, które protokół RGB musi śledzić dla danego Contract. Składa się z :




- Pojedynczy Global State**: jest to publiczna, globalna część Contract, widoczna dla wszystkich;
- Jeden lub więcej stanów własnych**: każdy Owned State jest powiązany z unikalnym Seal (a zatem UTXO na Bitcoin). Rozróżnia się :
    - Stany należące do **państwa publicznego**,
    - Stany **prywatne** na własność.


![RGB-Bitcoin](assets/fr/066.webp)


*Global State* jest bezpośrednio zawarty w *Contract Operation* jako pojedynczy blok. *Owned States* są zdefiniowane w każdym *Assignment*, obok *Seal Definition*.


Główną cechą RGB jest sposób, w jaki modyfikowane są Global State i Owned States. Istnieją zasadniczo dwa rodzaje zachowań:




- Zmienny**: gdy element stanu jest opisany jako zmienny, każda nowa operacja zastępuje poprzedni stan nowym stanem. Stare dane są wtedy uważane za nieaktualne;
- Akumulacja**: gdy element stanu jest zdefiniowany jako akumulujący, każda nowa operacja dodaje nowe informacje do poprzedniego stanu, bez nadpisywania go. Rezultatem jest rodzaj skumulowanej historii.


Jeśli w Contract element stanu nie jest zdefiniowany jako zmienny lub kumulatywny, element ten pozostanie pusty dla kolejnych operacji (innymi słowy, nie ma nowych wersji dla tego pola). To Contract Schema (tj. kodowany Business Logic) określa, czy stan (globalny lub własny) jest zmienny, kumulatywny czy stały. Po zdefiniowaniu Genesis właściwości te można modyfikować tylko wtedy, gdy pozwala na to sam Contract, na przykład za pośrednictwem określonego State Extension.


Poniższa tabela ilustruje, w jaki sposób każdy typ Contract Operation może manipulować (lub nie) Global State i Owned State:


|                              | Genesis | State Extension | State Transition |
| ---------------------------- | :-----: | :-------------: | :--------------: |
| **Addition of Global State** |    +    |        -        |        +         |
| **Mutation of Global State** |   n/a   |        -        |        +         |
| **Addition of Owned State**  |    +    |        -        |        +         |
| **Mutation of Owned State**  |   n/a   |       No        |        +         |
| **Addition of Valencies**    |    +    |        +        |        +         |


**`+`** : działanie możliwe, jeśli pozwala na to Contract's Schema.


**`-`**: operacja musi zostać potwierdzona przez kolejny State Transition (sam State Extension nie zamyka Single-Use Seal).


Ponadto zakres czasowy i prawa do aktualizacji każdego typu danych można rozróżnić w poniższej tabeli:


|                                 | Metadata                                 | Global State                                  | Owned State                                                                                                |
| ------------------------------- | ---------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Scope**                       | Defined for a single Contract Operation | Defined globally for the contract            | Defined for each seal (*Assignment*)                                                                       |
| **Who can update it?**          | Non-updatable (ephemeral data)          | Operation issued by actors (issuer, etc.)    | Depends on the legitimate holder who owns the seal (the one who can spend it in a following transaction)  |
| **Temporal Scope**              | Only for the current operation          | State is established at the end of the operation | State is defined before the operation (by the *Seal Definition* of the previous operation)               |


### Global State


Global State jest często opisywany jako "nikt nie posiada, wszyscy wiedzą". Zawiera ogólne informacje o Contract, które są publicznie widoczne. Na przykład, w Contract wydającym token, potencjalnie zawiera on :




- Ticker (symboliczny skrót tokena): `ticker` ;
- Pełna nazwa tokena: `name` ;
- Precyzja (liczba miejsc dziesiętnych): `precision` ;
- Oferta początkowa (i/lub maksymalny limit tokenów): `issuedSupply` ;
- Data wydania: `created` ;
- Dane prawne lub inne informacje publiczne: `data`.


Ten Global State może być umieszczony na publicznych zasobach (strony internetowe, IPFS, Nostr, Torrent, itp.) i dystrybuowany do społeczności. Ponadto zachęta ekonomiczna (potrzeba posiadania i przesyłania tych tokenów itp.) w naturalny sposób skłania użytkowników Contract do samodzielnego utrzymywania i propagowania tych danych.


### Zadania


*Assignment* jest podstawową strukturą do definiowania :




- Seal (*Seal Definition*), który wskazuje na określony UTXO;
- *Owned State*, tj. właściwość lub dane powiązane z tym Seal.


*Assignment* może być postrzegany jako odpowiednik wyjścia transakcji Bitcoin, ale z większą elastycznością. W tym tkwi logika transferu własności: *Assignment* kojarzy określony typ aktywów lub praw (`AssignmentType`) z Seal. Ktokolwiek posiada klucz prywatny UTXO powiązany z tym Seal (lub ktokolwiek może wydać ten UTXO) jest uważany za właściciela tego *Owned State*.


Jedną z największych zalet RGB jest możliwość dowolnego ujawniania (*reveal*) lub ukrywania (*conceal*) pól *Seal Definition* i *Owned State*. Zapewnia to potężne połączenie poufności i selektywności. Na przykład, można udowodnić, że przejście jest ważne bez ujawniania wszystkich danych, dostarczając ujawnioną wersję osobie, która musi ją zatwierdzić, podczas gdy osoby trzecie widzą tylko ukrytą wersję (Hash). W praktyce `OpId` przejścia jest zawsze obliczany na podstawie *ukrytych* danych.


![RGB-Bitcoin](assets/fr/067.webp)


#### Seal Definition


*Seal Definition*, w swojej ujawnionej formie, ma cztery podstawowe pola: `txptr`, `vout`, `blinding` i `method` :




- txptr**: jest to odniesienie do UTXO na Bitcoin:
    - W przypadku **Genesis Seal** wskazuje bezpośrednio na istniejący UTXO (ten powiązany z Genesis);
    - W przypadku **Graph Seal**, możemy mieć :
        - Prosty `txid`, jeśli wskazuje na konkretny UTXO,
        - Lub `WitnessTx`, który oznacza samoodniesienie: Seal wskazuje na samą transakcję. Jest to szczególnie przydatne, gdy nie jest dostępny zewnętrzny UTXO, na przykład w transakcjach otwarcia kanału Lightning lub gdy odbiorca nie ma UTXO.
- vout** : numer wyjściowy transakcji wskazanej przez `txptr`. Obecny tylko dla standardowego wykresu Seal (nie dla `WitnessTx`);
- blinding**: losowa liczba 8 bajtów, aby wzmocnić poufność i zapobiec próbom brutalnej siły na tożsamość UTXO;
- method** : wskazuje zastosowaną metodę kotwiczenia (`Tapret` lub `Opret`).


*Ukryta* forma Seal Definition to SHA256 Hash (oznaczony) konkatenacji tych 4 pól, ze znacznikiem specyficznym dla RGB.


![RGB-Bitcoin](assets/fr/068.webp)


#### Stany posiadane


Drugim komponentem *Assignment* jest Owned State. W przeciwieństwie do Global State, może on istnieć w formie publicznej lub prywatnej:




- Publiczny Owned State**: każdy zna dane powiązane z Seal. Na przykład publiczny obraz;
- Prywatne Owned State**: dane są ukryte, znane tylko właścicielowi (i potencjalnie walidatorowi, jeśli to konieczne). Na przykład liczba posiadanych tokenów.


RGB definiuje cztery możliwe typy stanów (*StateTypes*) dla Owned State:




- Deklaratywny**: nie zawiera danych liczbowych, tylko deklaratywne prawo (np. prawo do głosowania). Ukryte i ujawnione formy są identyczne;
- Fungible**: reprezentuje ilość zamienną (jak żetony). W formie jawnej mamy `amount` i `blinding`. W formie ukrytej mamy pojedynczy *Pedersen commitment*, który ukrywa ilość i zaślepienie;
- Structured**: przechowuje dane strukturalne (do 64 kB). W formie jawnej jest to blob danych. W formie ukrytej jest to oznaczony Hash tego obiektu blob:


```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```


Na przykład :


```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```




- Attachments**: łączy plik (audio, obraz, binarny itp.) z Owned State, przechowując plik Hash `file_hash`, typ MIME `media type` i sól kryptograficzną `salt`. Sam plik jest hostowany gdzie indziej. W ukrytej formie jest to Hash oznaczony trzema poprzednimi elementami danych:


```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```


Na przykład :


```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```


Podsumowując, oto 4 możliwe typy stanu w formie jawnej i ukrytej:


```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |

+--------------------------+             +---------------------------------------+
```


| **Element**         | **Declarative**  | **Fungible**                         | **Structured**                 | **Attachments**                |
| ------------------- | -------------- | ------------------------------------ | ----------------------------- | ----------------------------- |
| **Data**           | None           | Signed or unsigned 64-bit integer    | Any strict data type          | Any file                      |
| **Info Type**      | None           | Signed or unsigned                   | Strict types                   | MIME Type                      |
| **Privacy**       | Not required    | Pedersen commitment                  | Hash with blinding            | Hashed file identifier         |
| **Size Limits**    | N/A            | 256 bytes                             | Up to 64 KB                    | Up to ~500 GB                  |


### Wejścia


Wejścia *Contract Operation* odnoszą się do *przypisań*, które są wykorzystywane w tej nowej operacji. Wejście wskazuje :




- prevOpId` : identyfikator (`OpId`) poprzedniej operacji, w której znajdował się *Assignment*;
- assignmentType` : typ *Assignment* (na przykład `assetOwner` dla tokena);
- `Index`: indeks *Assignment* na liście powiązanej z poprzednim `OpId`, określony po leksykograficznym sortowaniu ukrytych pieczęci.


Wejścia nigdy nie pojawiają się w Genesis, ponieważ nie ma wcześniejszych Przypisań. Nie pojawiają się również w rozszerzeniach stanów (ponieważ rozszerzenia stanów nie zamykają pieczęci; raczej redefiniują nowe pieczęcie w oparciu o walencje).


Gdy posiadamy Owned States typu `Fungible`, logika walidacji (poprzez skrypt AluVM dostarczony w Schema) sprawdza spójność sum: suma tokenów przychodzących (*Inputs*) musi być równa sumie tokenów wychodzących (w nowym *Assignments*).


### Metadane


Pole **Metadata** może mieć maksymalnie 64 KiB i jest używane do umieszczania tymczasowych danych przydatnych do walidacji, ale nie zintegrowanych z trwałym stanem Contract. Na przykład można tu przechowywać pośrednie zmienne obliczeniowe dla złożonych skryptów. Ta przestrzeń nie jest przeznaczona do przechowywania w globalnej historii, dlatego jest poza zakresem Owned States lub Global State.


### Wartości


Wartości** są oryginalnym mechanizmem protokołu RGB. Można je znaleźć w Genesis, State Transitions lub State Extensions. Reprezentują one prawa numeryczne, które mogą być aktywowane przez State Extension (poprzez *Redeems*), a następnie sfinalizowane przez kolejne Przejście. Każdy Valency jest identyfikowany przez `ValencyType` (16 bitów). Jego semantyka (prawo do wznowienia, zamiana tokenów, prawo do spalenia itp.) jest zdefiniowana w Schema.


Konkretnie, możemy sobie wyobrazić Genesis definiujący "prawo do ponownego wydania" Valency. State Extension zużyje go (*Redeem*), jeśli spełnione zostaną określone warunki, w celu wprowadzenia nowej ilości tokenów. Następnie State Transition pochodzący od posiadacza utworzonego w ten sposób Seal może przekazać te nowe tokeny.


### Odkupienia


Redeems to odpowiednik wejść dla przypisań w Valency. Pojawiają się one tylko w rozszerzeniach stanów, ponieważ tam aktywowany jest wcześniej zdefiniowany Valency. Redeem składa się z dwóch pól:




- `PrevOpId`: `OpId` operacji, w której określono Valency;
- `ValencyType`: typ Valency, który chcesz aktywować (każdy `ValencyType` może być użyty tylko raz przez State Extension).


Przykład: Redeem może odpowiadać wykonaniu CoinSwap, w zależności od tego, co zostało zakodowane w Valency.


### Charakterystyka stanu RGB


Przyjrzymy się teraz kilku podstawowym cechom stanu w RGB. W szczególności przyjrzymy się :




- **Strict Type System**, który narzuca precyzyjną i typową organizację danych;
- Znaczenie oddzielenia **walidacji** od **Ownership** ;
- System **konsensusu ewolucji** w RGB, który obejmuje pojęcia *szybkiego przewijania do przodu* i *push-back*.


Jak zawsze, należy pamiętać, że wszystko, co ma związek ze statusem Contract, jest weryfikowane po stronie klienta zgodnie z zasadami konsensusu określonymi w protokole, którego ostateczne odniesienie kryptograficzne jest zakotwiczone w transakcjach Bitcoin.


#### Ścisły system typów


RGB wykorzystuje *Strict Type System* i deterministyczny tryb serializacji (*Strict Encoding*). Organizacja ta ma na celu zagwarantowanie doskonałej powtarzalności i precyzji w definiowaniu, obsłudze i walidacji danych Contract.


W wielu środowiskach programowania (JSON, YAML...) struktura danych może być elastyczna, a nawet zbyt liberalna. Z drugiej strony w RGB struktura i typy każdego pola są zdefiniowane z wyraźnymi ograniczeniami. Na przykład :




- Każda zmienna ma określony typ (na przykład 8-bitowa liczba całkowita bez znaku `u8` lub 16-bitowa liczba całkowita ze znakiem itd;)
- Typy mogą być komponowane (typy zagnieżdżone). Oznacza to, że można zdefiniować typ oparty na innych typach (np. typ zagregowany zawierający pole `u8`, pole `bool` itp;)
- Można również określić kolekcje: listy (*list*), zbiory (*set*) lub słowniki (*map*), z deterministycznym porządkiem progresji;
- Każde pole jest ograniczone (*dolna granica* / *górna granica*). Nakładamy również ograniczenia na liczbę Elements w kolekcjach (hermetyzacja);
- Dane są wyrównane do bajtów, a serializacja jest ściśle zdefiniowana i jednoznaczna.


Dzięki temu rygorystycznemu protokołowi kodowania :




- Kolejność pól jest zawsze taka sama, niezależnie od implementacji lub używanego języka programowania;
- Hashy obliczone na tym samym zestawie danych są zatem powtarzalne i identyczne (ściśle deterministyczne *zobowiązania*);
- Granice zapobiegają niekontrolowanemu wzrostowi rozmiaru danych (np. zbyt wielu pól);
- Ta forma kodowania ułatwia weryfikację kryptograficzną, ponieważ każdy uczestnik dokładnie wie, jak serializować i Hash dane.


W praktyce struktura (*Schema*) i kod wynikowy (*Interface* i powiązana logika) są kompilowane. Język opisowy jest używany do definiowania Contract (typy, pola, reguły) i generate ścisłego formatu binarnego. Po skompilowaniu wynikiem jest :




- *Układ pamięci* dla każdego pola;
- Identyfikatory semantyczne (które wskazują, czy zmiana nazwy zmiennej ma wpływ na logikę, nawet jeśli struktura pamięci pozostaje taka sama).


Ścisły system typów umożliwia również precyzyjne monitorowanie zmian: każda modyfikacja struktury (nawet zmiana nazwy pola) jest wykrywalna i może prowadzić do zmiany ogólnego śladu.


Wreszcie, każda kompilacja tworzy odcisk palca, identyfikator kryptograficzny, który potwierdza dokładną wersję kodu (dane, reguły, walidację). Na przykład, identyfikator w postaci :


```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```


Umożliwia to zarządzanie konsensusem lub aktualizacjami implementacji, zapewniając jednocześnie szczegółową identyfikowalność wersji używanych w sieci.


Aby zapobiec sytuacji, w której stan RGB Contract staje się zbyt kłopotliwy do walidacji po stronie klienta, reguła konsensusu narzuca maksymalny rozmiar `2^16` bajtów (64 Kio) dla wszelkich danych zaangażowanych w obliczenia walidacyjne. Dotyczy to każdej zmiennej lub struktury: nie więcej niż 65536 bajtów lub odpowiednik w liczbach (32768 16-bitowych liczb całkowitych itp.). Dotyczy to również kolekcji (list, zestawów, map), które nie mogą przekraczać `2^16` Elements.


Limit ten gwarantuje :




- Kontroluje maksymalny rozmiar danych, którymi można manipulować podczas State Transition;
- Kompatybilność z maszyną wirtualną (*AluVM*) używaną do uruchamiania skryptów walidacyjnych.


#### Paradygmat walidacji != Ownership


Jedną z głównych innowacji RGB jest ścisłe oddzielenie dwóch koncepcji:




- Walidacja**: sprawdzenie, czy State Transition przestrzega zasad Contract (Business Logic, historia itp.);
- Ownership** (Ownership lub kontrola): fakt posiadania Bitcoin UTXO, który umożliwia wydanie (lub zamknięcie) Single-Use Seal, a tym samym wykonanie State Transition.


Walidacja** odbywa się na poziomie stosu oprogramowania RGB (biblioteki, protokół *commitments* itp.). Jego rolą jest zapewnienie, że wewnętrzne zasady Contract (kwoty, uprawnienia itp.) są przestrzegane. Obserwatorzy lub inni uczestnicy mogą również zatwierdzać historię danych.


Z drugiej strony Ownership** całkowicie opiera się na bezpieczeństwie Bitcoin. Posiadanie klucza prywatnego UTXO oznacza kontrolowanie możliwości uruchomienia nowego przejścia (zamknięcia Single-Use Seal). Tak więc, nawet jeśli ktoś może zobaczyć lub zweryfikować dane, nie może zmienić stanu, jeśli nie jest właścicielem danego UTXO.


![RGB-Bitcoin](assets/fr/069.webp)


Takie podejście ogranicza klasyczne luki napotykane w bardziej złożonych łańcuchach bloków (gdzie cały kod Smart contract jest publiczny i może być modyfikowany przez każdego, co czasami prowadziło do włamań). Na RGB atakujący nie może po prostu wejść w interakcję ze stanem On-Chain, ponieważ prawo do działania na stanie (*Ownership*) jest chronione przez Bitcoin Layer.


Co więcej, to oddzielenie pozwala RGB na naturalną integrację z Lightning Network. Kanały Lightning mogą być używane do angażowania i przenoszenia zasobów RGB bez konieczności angażowania *zobowiązań* On-Chain za każdym razem. Przyjrzymy się bliżej tej integracji RGB z Lightning w późniejszych rozdziałach kursu.


#### Rozwój konsensusu w RGB


Oprócz wersjonowania kodu semantycznego, RGB zawiera system ewolucji lub aktualizacji reguł konsensusu Contract w czasie. Istnieją dwie główne formy ewolucji:




- Szybko do przodu**
- Push-back** (w języku francuskim)


Szybkie przewijanie następuje, gdy poprzednio nieważna reguła staje się ważna. Na przykład, jeśli Contract ewoluuje, aby umożliwić nowy typ `AssignmentType` lub nowe pole :




- Nie można tego porównać do klasycznego hardforka Blockchain, ponieważ RGB działa w Client-side Validation i nie wpływa na ogólną kompatybilność Blockchain;
- W praktyce ten rodzaj zmiany jest wskazywany przez pole `Ffv` (*fast-forward version*) w Contract Operation;
- Obecni posiadacze nie są poszkodowani: ich status pozostaje ważny;
- Z drugiej strony nowi beneficjenci (lub nowi użytkownicy) muszą zaktualizować swoje oprogramowanie (Wallet), aby rozpoznać nowe zasady.


Odepchnięcie oznacza, że poprzednio ważna reguła staje się nieważna. Jest to zatem "utwardzenie" reguł, ale nie jest to softfork:




- Może to mieć wpływ na istniejących posiadaczy (mogą znaleźć się z aktywami, które staną się przestarzałe lub nieważne w nowej wersji);
- Możemy uznać, że w rzeczywistości tworzymy nowy protokół: ktokolwiek przyjmuje nową zasadę, odchodzi od starej;
- Emitent może zdecydować się na ponowne wydanie aktywów w nowym protokole, zmuszając użytkowników do utrzymywania dwóch oddzielnych portfeli (jednego dla starego protokołu, drugiego dla nowego), jeśli chcą zarządzać obiema wersjami.


W tym rozdziale na temat operacji RGB Contract zbadaliśmy podstawowe zasady leżące u podstaw tego protokołu. Jak zapewne zauważyłeś, złożoność protokołu RGB wymaga użycia wielu terminów technicznych. Dlatego w następnym rozdziale przedstawię słowniczek, który podsumuje wszystkie pojęcia omówione w tej pierwszej części teoretycznej, wraz z definicjami wszystkich terminów technicznych związanych z RGB. Następnie, w kolejnej części, przyjrzymy się praktycznej definicji i implementacji kontraktów RGB.


## Słowniczek RGB


<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>


Jeśli zajdzie potrzeba powrotu do tego krótkiego słownika ważnych terminów technicznych używanych w świecie RGB (wymienionych w kolejności alfabetycznej), okaże się on przydatny. Ten rozdział nie jest niezbędny, jeśli zrozumiałeś już wszystko, co omówiliśmy w pierwszej sekcji.


#### AluVM


Skrót AluVM oznacza "_Algorithmic logic unit Virtual Machine_", opartą na rejestrach maszynę wirtualną zaprojektowaną do walidacji Smart contract i obliczeń rozproszonych. Jest ona używana (ale nie wyłącznie zarezerwowana) do walidacji kontraktów RGB. Skrypty lub operacje zawarte w RGB Contract mogą być zatem wykonywane w środowisku AluVM.


Więcej informacji: [AluVM oficjalna strona internetowa](https://www.AluVM.org/)


#### Anchor


Anchor reprezentuje zestaw danych po stronie klienta używanych do udowodnienia włączenia unikalnego _commitment_ do transakcji. W protokole RGB, Anchor składa się z następujących Elements:




- Identyfikator transakcji Bitcoin (txid) dla **Witness Transaction**;
- **Multi Protocol Commitment (MPC)** ;
- **Deterministic Bitcoin Commitment (DBC)**;
- **Extra Transaction Proof (ETP)** w przypadku korzystania z mechanizmu **Tapret** Commitment (patrz sekcja poświęcona temu modelowi).


Anchor służy zatem do ustanowienia weryfikowalnego powiązania między konkretną transakcją Bitcoin a prywatnymi danymi zweryfikowanymi przez protokół RGB. Gwarantuje on, że dane te są rzeczywiście zawarte w Blockchain, a ich dokładna treść nie jest publicznie ujawniana.


#### Assignment


W logice RGB, Assignment jest odpowiednikiem wyjścia transakcji, które modyfikuje, aktualizuje lub tworzy pewne właściwości w ramach stanu Contract. Assignment składa się z dwóch Elements:




- A **Seal Definition** (odniesienie do konkretnego UTXO) ;
- An **Owned State** (dane opisujące stan powiązany z tym nowym właścicielem).


Assignment wskazuje zatem, że część stanu (na przykład aktywa) jest teraz przydzielona konkretnemu posiadaczowi, zidentyfikowanemu za pomocą Single-Use Seal połączonego z UTXO.


#### Business Logic


Business Logic grupuje wszystkie zasady i wewnętrzne operacje Contract, opisane przez jego **Schema** (tj. strukturę samego Contract). Określa, w jaki sposób stan Contract może ewoluować i w jakich warunkach.


#### Client-side Validation


Client-side Validation odnosi się do procesu, w którym każda strona (klient) weryfikuje zestaw danych wymienianych prywatnie, zgodnie z zasadami protokołu. W przypadku RGB, te wymieniane dane są grupowane w tak zwane **przesyłki**. W przeciwieństwie do protokołu Bitcoin, który wymaga, aby wszystkie transakcje były publikowane On-Chain, RGB pozwala na publiczne przechowywanie tylko _zobowiązań_ (zakotwiczonych w Bitcoin), podczas gdy istotne informacje Contract (przejścia, poświadczenia, dowody) pozostają off-chain, udostępniane tylko między zainteresowanymi użytkownikami.


#### Commitment


Commitment (w sensie kryptograficznym) jest obiektem matematycznym, oznaczanym jako `C`, wyprowadzonym deterministycznie z operacji na danych strukturalnych `m` (wiadomość) i wartości losowej `r`. Piszemy :


$$
C = \text{commit}(m, r)
$$


Mechanizm ten obejmuje dwie główne operacje:




- Commit**: funkcja kryptograficzna jest stosowana do wiadomości `m` i liczby losowej `r` w celu uzyskania `C`;
- Verify**: używamy `C`, komunikatu `m` i wartości `r`, aby sprawdzić, czy ten Commitment jest poprawny. Funkcja zwraca `True` lub `False`.


Commitment musi respektować dwie właściwości:




- Wiązanie**: znalezienie dwóch różnych wiadomości generujących to samo `C` musi być niemożliwe:


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Takich jak :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Ukrywanie**: znajomość `C` nie może ujawniać zawartości `m`.


W protokole RGB, Commitment jest zawarty w transakcji Bitcoin, aby udowodnić istnienie określonej informacji w danym czasie, bez ujawniania samej informacji.


#### Consignment


Consignment** grupuje dane wymieniane między stronami, z zastrzeżeniem Client-side Validation w RGB. Istnieją dwie główne kategorie Consignment:




- Contract Consignment**: dostarczany przez *emitenta* (emitenta Contract), zawiera informacje inicjalizacyjne, takie jak Schema, Genesis, Interface i Interface Implementation.
- Przelew Consignment**: dostarczany przez stronę płacącą (*płatnika*). Zawiera całą historię przejść stanów prowadzących do Terminal Consignment (tj. ostatecznego stanu otrzymanego przez płatnika).


Przesyłki te nie są rejestrowane publicznie na Blockchain; są one wymieniane bezpośrednio między zainteresowanymi stronami za pośrednictwem wybranego przez nie kanału komunikacji.


#### Contract


Contract to zestaw uprawnień wykonywanych cyfrowo między kilkoma podmiotami za pośrednictwem protokołu RGB. Ma stan aktywny i Business Logic, zdefiniowany przez Schema, który określa, które operacje są autoryzowane (przelewy, rozszerzenia itp.). Stan Contract, jak również zasady jego ważności, są wyrażone w Schema. W dowolnym momencie Contract ewoluuje tylko zgodnie z tym, co jest dozwolone przez Schema i skrypty walidacyjne (uruchamiane na przykład w AluVM).


#### Contract Operation


Contract Operation to aktualizacja stanu Contract wykonywana zgodnie z zasadami Schema. W RGB istnieją następujące operacje:




- State Transition** ;
- Genesis** ;
- State Extension**.


Każda operacja modyfikuje stan poprzez dodanie lub zastąpienie określonych danych (Global State, Owned State...).


#### Contract Participant


Contract Participant jest podmiotem, który bierze udział w operacjach związanych z Contract. W RGB rozróżnia się :




- Wystawca Contract, który tworzy Genesis (źródło Contract);
- Strony Contract, tj. posiadacze praw do stanu Contract;
- Strony publiczne, które mogą budować rozszerzenia stanowe, jeśli Contract oferuje walencje dostępne publicznie.


#### Contract Rights


Contract Rights odnoszą się do różnych praw, z których mogą korzystać osoby zaangażowane w RGB Contract. Dzielą się one na kilka kategorii:




- Prawa Ownership**, powiązane z Ownership określonego UTXO (poprzez _Seal Definition_);
- Uprawnienia wykonawcze**, tj. możliwość zbudowania jednego lub więcej przejść (State Transitions) zgodnie z Schema ;
- Prawa publiczne**, gdy Schema zezwala na określone zastosowania publiczne, na przykład utworzenie State Extension poprzez wykup Valency.


#### Contract State


Contract State odpowiada bieżącemu stanowi Contract w danym momencie. Może składać się zarówno z danych publicznych, jak i prywatnych, odzwierciedlając stan Contract. RGB rozróżnia :




- **Global State**, który zawiera publiczne właściwości Contract (skonfigurowane w Genesis lub dodane poprzez autoryzowane aktualizacje);
- Stany Własne**, które należą do określonych właścicieli, zidentyfikowanych przez ich UTXO.


#### Deterministic Bitcoin Commitment - DBC


Deterministic Bitcoin Commitment (DBC) to zestaw reguł używanych do udowodnionego i jednoznacznego rejestrowania _commitment_ w transakcji Bitcoin. W protokole RGB istnieją dwie główne formy DBC:




- Opret**
- Tapret**


Mechanizmy te precyzyjnie definiują sposób kodowania _commitment_ w danych wyjściowych lub strukturze transakcji Bitcoin, aby zapewnić, że Commitment jest deterministycznie identyfikowalny i weryfikowalny.


#### Directed Acyclic Graph - DAG


DAG (lub *Acykliczny Graf Kierowany*) jest grafem wolnym od cykli, umożliwiającym topologiczne planowanie. Blockchainy, podobnie jak _shardy_ kontraktów RGB, mogą być reprezentowane przez DAG.


Więcej informacji: [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)


#### Grawerowanie


Grawerowanie to opcjonalny ciąg danych, który kolejni właściciele Contract mogą wprowadzić do historii Contract. Funkcja ta istnieje na przykład w **RGB21** Interface i umożliwia dodawanie informacji pamiątkowych lub opisowych do historii Contract.


#### Dodatkowy dowód transakcji - ETP


ETP (*Extra Transaction Proof*) to część Anchor, która zawiera dodatkowe dane wymagane do walidacji **Tapret** *Commitment* (w kontekście _taproot_). Zawiera między innymi wewnętrzny klucz publiczny skryptu Taproot (_internal PubKey_) oraz informacje specyficzne dla _Script Path Spend_.


#### Genesis


Genesis odnosi się do zbioru danych, zarządzanego przez Schema, który tworzy stan początkowy dowolnego Contract w RGB. Można go porównać do koncepcji _Genesis Block_ Bitcoin lub koncepcji Coinbase Transaction, ale tutaj na poziomie _client-side_ i RGB tokena.


#### Global State


Global State jest zbiorem właściwości publicznych zawartych w Contract State. Jest on zdefiniowany w Genesis i, w zależności od zasad Contract, może być aktualizowany przez autoryzowane przejścia. W przeciwieństwie do Owned States, Global State nie należy do konkretnego podmiotu; jest bliższy rejestrowi publicznemu w ramach Contract.


#### Interface


Interface to zestaw instrukcji używanych do dekodowania danych binarnych skompilowanych w Schema lub w operacjach Contract i ich stanów, w celu uczynienia ich czytelnymi dla użytkownika lub jego Wallet. Działa jako interpretacja Layer.


#### Interface Implementation


Interface Implementation to zestaw deklaracji, które łączą **Interface** z **Schema**. Umożliwia tłumaczenie semantyczne wykonywane przez sam Interface, tak aby surowe dane Contract mogły być zrozumiane przez użytkownika lub oprogramowanie (portfele).


#### Invoice


Invoice ma postać adresu URL zakodowanego w [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), który zawiera dane niezbędne do skonstruowania **State Transition** (przez płatnika). Innymi słowy, jest to Invoice umożliwiający kontrahentowi (*płatnikowi*) utworzenie odpowiedniego przejścia w celu przeniesienia zasobu lub aktualizacji stanu Contract.


#### Lightning Network


Lightning Network to zdecentralizowana sieć kanałów płatności (lub _kanałów stanowych_) na Bitcoin, składająca się z 2/2 portfeli z wieloma podpisami. Umożliwia szybkie, tanie transakcje _off-chain_, jednocześnie polegając na Layer 1 Bitcoin w celu arbitrażu (lub zamknięcia) w razie potrzeby.


Więcej informacji na temat działania Lightning można znaleźć w tym kursie:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

#### Multi Protocol Commitment - MPC


Multi Protocol Commitment (MPC) odnosi się do struktury Merkle Tree używanej w RGB w celu włączenia, w ramach pojedynczej transakcji Bitcoin, kilku **Transition Bundles** z różnych kontraktów. Chodzi o to, aby zgrupować kilka zobowiązań (potencjalnie odpowiadających różnym kontraktom lub różnym aktywom) w jednym punkcie Anchor w celu optymalizacji wykorzystania przestrzeni blokowej.


#### Owned State


Owned State to część Contract State, która jest zamknięta w Assignment i powiązana z konkretnym posiadaczem (poprzez Single-Use Seal wskazujący na UTXO). Reprezentuje to na przykład zasób cyfrowy lub określone prawo umowne przypisane do tej osoby.


#### Ownership


Ownership odnosi się do możliwości kontrolowania i wydawania UTXO, do którego odnosi się Seal Definition. Gdy Owned State jest powiązany z UTXO, właściciel tego UTXO ma potencjalnie prawo do przeniesienia lub zmiany powiązanego stanu, zgodnie z zasadami Contract.


#### Partially Signed Bitcoin Transaction - PSBT


PSBT (_częściowo podpisana transakcja Bitcoin_) to transakcja Bitcoin, która nie jest jeszcze w pełni podpisana. Może być współdzielona przez kilka podmiotów, z których każdy może dodawać lub weryfikować określone Elements (podpisy, skrypty...), dopóki transakcja nie zostanie uznana za gotową do dystrybucji On-Chain.


Więcej informacji: [BIP-0174](https://github.com/Bitcoin/bips/blob/master/bip-0174.mediawiki)


#### Pedersen commitment


Pedersen commitment jest typem kryptograficznego Commitment z właściwością bycia **homomorficznym** w odniesieniu do operacji dodawania. Oznacza to, że możliwe jest zweryfikowanie sumy dwóch zobowiązań bez ujawniania poszczególnych wartości.


Formalnie, jeśli :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


następnie :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Ta właściwość jest przydatna na przykład do ukrywania ilości wymienianych tokenów, przy jednoczesnym zachowaniu możliwości weryfikacji sumy.


Więcej informacji: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)


#### Redeem


W State Extension, Redeem odnosi się do działania polegającego na odzyskaniu (lub wykorzystaniu) wcześniej zadeklarowanego **Valency**. Ponieważ Valency jest prawem publicznym, Redeem pozwala upoważnionemu uczestnikowi ubiegać się o określony Contract State Extension.


#### Schema


Schema w RGB jest deklaratywnym fragmentem kodu opisującym zestaw zmiennych, reguł i Business Logic (*Business Logic*), które regulują działanie Contract. Schema definiuje strukturę stanu, typy dozwolonych przejść i warunki walidacji.


#### Seal Definition


Seal Definition jest częścią Assignment, która kojarzy _zobowiązanie_ z UTXO należącym do nowego posiadacza. Innymi słowy, wskazuje, gdzie znajduje się warunek (w którym UTXO) i ustanawia Ownership składnika aktywów lub prawa.


#### Shard


Shard reprezentuje gałąź w DAG historii przejść stanu RGB Contract. Innymi słowy, jest to spójny podzbiór ogólnej historii Contract, odpowiadający na przykład sekwencji przejść wymaganych do udowodnienia ważności danego zasobu od czasu _Genesis_.


#### Single-Use Seal


Single-Use Seal jest kryptograficzną obietnicą Commitment dla nieznanej jeszcze wiadomości, która zostanie ujawniona tylko raz w przyszłości i musi być znana wszystkim członkom określonej grupy odbiorców. Celem jest zapobieganie tworzeniu wielu konkurencyjnych zobowiązań dla tego samego Seal.


#### Stash


Stash to zestaw danych po stronie klienta, które użytkownik przechowuje dla jednej lub więcej umów RGB w celu walidacji (*Client-side Validation*). Obejmuje to historię przejść, przesyłki, dowody ważności itp. Każdy posiadacz zachowuje tylko te części historii, których potrzebuje (*shards*).


#### State Extension


State Extension to Contract Operation używany do ponownego wyzwalania aktualizacji stanu poprzez odkupienie wcześniej zadeklarowanych **Walencji**. Aby State Extension był skuteczny, musi zostać zamknięty przez State Transition (który aktualizuje końcowy stan Contract).


#### State Transition


State Transition to operacja, która zmienia stan RGB Contract na nowy. Może ona modyfikować dane Global State i/lub Owned State. W praktyce każde przejście jest weryfikowane przez reguły Schema i zakotwiczone w Bitcoin Blockchain poprzez _commitment_.


#### Taproot


Odnosi się do formatu transakcji Bitcoin SegWit v1, wprowadzonego przez [BIP341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki) i [BIP342](https://github.com/Bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot poprawia poufność i elastyczność skryptów, w szczególności poprzez uczynienie transakcji bardziej zwartymi i trudniejszymi do odróżnienia od siebie.


#### Terminal Consignment - Consignment Endpoint


Terminal Consignment (lub _Consignment Endpoint_) jest *punktem końcowym transferu Consignment* zawierającym końcowy stan Contract, w tym State Transition utworzony z Invoice odbiorcy (*payee*). Jest to zatem punkt końcowy transferu, z danymi niezbędnymi do udowodnienia, że Ownership lub stan został przekazany.


#### Transition Bundle


Transition Bundle to zestaw przejść stanu RGB (należących do tego samego Contract), które są zaangażowane w ten sam ***Witness Transaction*** Bitcoin. Umożliwia to połączenie kilku aktualizacji lub transferów w jeden On-Chain Anchor.


#### UTXO


Bitcoin UTXO (*Unspent Transaction Output*) jest zdefiniowany przez Hash transakcji i indeks wyjścia (*vout*). Jest również czasami nazywany _outpoint_. W protokole RGB odniesienie do UTXO (poprzez **Seal Definition**) umożliwia lokalizację **Owned State**, tj. właściwości przechowywanej na Blockchain.


#### Valency


Valency jest prawem publicznym, które jako takie nie wymaga przechowywania przez państwo, ale które można zrealizować za pośrednictwem **State Extension**. Jest to zatem forma możliwości dostępna dla wszystkich (lub niektórych graczy), zadeklarowana w logice Contract, w celu przeprowadzenia określonego rozszerzenia w późniejszym terminie.


#### Witness Transaction


Witness Transaction jest transakcją Bitcoin, która zamyka Single-Use Seal wokół komunikatu zawierającego Multi Protocol Commitment (MPC). Transakcja ta wydaje UTXO lub tworzy jeden, tak aby Seal Commitment powiązany z protokołem RGB. Działa jako dowód On-Chain, że stan został ustawiony w określonym momencie.


# Programowanie na RGB


<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>


## Wdrażanie umów RGB


<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>


:::video id=97d81b85-5a82-40a5-b111-7d96be5afd0f:::


W tym rozdziale przyjrzymy się bliżej, w jaki sposób RGB Contract jest definiowany i wdrażany. Zobaczymy, jakie są komponenty RGB Contract, jakie są ich role i jak są zbudowane.


### Składniki RGB Contract


Do tej pory omówiliśmy już **Genesis**, który stanowi punkt wyjścia Contract, i widzieliśmy, jak pasuje on do logiki *Contract Operation* i stanu protokołu. Pełna definicja RGB Contract nie ogranicza się jednak do samego Genesis: obejmuje trzy uzupełniające się komponenty, które razem tworzą serce implementacji.


Pierwszy komponent nosi nazwę **Schema**. Jest to plik opisujący podstawową strukturę i Business Logic (*Business Logic*) Contract. Określa używane typy danych, zasady walidacji, dozwolone operacje (np. początkowe wydawanie tokenów, transfery, warunki specjalne itp.) - w skrócie, ogólne ramy, które dyktują sposób działania Contract.


Drugim komponentem jest **Interface**. Koncentruje się on na tym, w jaki sposób użytkownicy (a co za tym idzie, oprogramowanie portfela) będą wchodzić w interakcje z Contract. Opisuje semantykę, tj. czytelną reprezentację różnych pól i działań. Tak więc, podczas gdy Schema definiuje sposób, w jaki Contract działa technicznie, Interface definiuje sposób prezentacji i ekspozycji tych funkcji: nazwy metod, wyświetlanie danych itp.


Trzecim komponentem jest **Interface Implementation**, który uzupełnia poprzednie dwa, działając jako rodzaj pomostu między Schema i Interface. Innymi słowy, kojarzy semantykę wyrażoną przez Interface z podstawowymi regułami zdefiniowanymi w Schema. To właśnie ta implementacja będzie zarządzać na przykład konwersją między parametrem wprowadzonym do Wallet a strukturą binarną narzuconą przez protokół lub kompilacją reguł walidacji w języku maszynowym.


Ta modułowość jest interesującą cechą RGB, ponieważ pozwala różnym grupom programistów pracować oddzielnie nad tymi aspektami (*Schema*, *Interface*, *Implementation*), o ile przestrzegają zasad konsensusu protokołu.


Podsumowując, każdy Contract składa się z :




- Genesis**, który jest stanem początkowym Contract (i można go porównać do specjalnej transakcji definiującej pierwszy Ownership składnika aktywów, prawa lub innych danych, które można sparametryzować);
- Schema**, który opisuje Contract's Business Logic (typy danych, reguły walidacji itp.);
- Interface**, który zapewnia semantyczny Layer zarówno dla portfeli, jak i użytkowników, wyjaśniając odczyt i wykonanie transakcji;
- Wdrożenie** Interface, który wypełnia lukę między Business Logic a prezentacją, aby zapewnić spójność definicji Contract z doświadczeniem użytkownika.


![RGB-Bitcoin](assets/fr/070.webp)


Należy zauważyć, że aby Wallet mógł zarządzać aktywem RGB (czy to tokenem zamiennym, czy jakimkolwiek prawem), musi posiadać wszystkie te Elements skompilowane: *Schema*, *Interface*, *Interface Implementation* i *Genesis*. Jest to przekazywane za pośrednictwem ***Contract Consignment***, tj. pakietu danych zawierającego wszystko, co jest potrzebne do walidacji Contract po stronie klienta.


Aby pomóc wyjaśnić te pojęcia, poniżej znajduje się tabela podsumowująca porównująca komponenty RGB Contract z koncepcjami znanymi już w programowaniu obiektowym (OOP) lub w ekosystemie Ethereum:


| RGB Contract Component       | Meaning                               | OOP Equivalent                             | Ethereum Equivalent               |
| ---------------------------- | ------------------------------------- | ------------------------------------------ | --------------------------------- |
| **Genesis**                  | Initial state of the contract        | Class constructor                         | Contract constructor              |
| **Schema**                   | Business logic of the contract       | Class                                     | Contract                          |
| **Interface**                | Semantics of the contract            | Interface (Java) / Trait (Rust) / Protocol (Swift) | ERC Standard                      |
| **Interface Implementation** | Mapping semantics and logic          | Impl (Rust) / Implements (Java)           | Application Binary Interface (ABI) |


Kolumna po lewej stronie przedstawia Elements specyficzny dla protokołu RGB. Środkowa kolumna pokazuje konkretną funkcję każdego komponentu. Następnie w kolumnie "Odpowiednik OOP" znajdujemy równoważny termin w programowaniu obiektowym:




- Parametr **Genesis** pełni rolę podobną do konstruktora *Klasy*: to tutaj inicjowany jest stan Contract;
- **Schema** to opis klasy, tj. definicja jej właściwości, metod i podstawowej logiki;
- Interface** odpowiada *interfaces* (Java), *traits* (Rust) lub *protocols* (Swift): są to publiczne definicje funkcji, zdarzeń, pól... ;
- **Interface Implementation** odpowiada *Impl* w Rust lub *Implements* w Javie, gdzie określamy, w jaki sposób kod będzie faktycznie wykonywał metody ogłoszone w Interface.


W kontekście Ethereum, Genesis jest bliższy konstruktorowi *Contract*, Schema definicji Contract, Interface standardowi takiemu jak ERC-20 lub ERC-721, a Interface Implementation ABI (*Application Binary Interface*), który określa format interakcji z Contract.


Zaletą modułowości RGB jest również fakt, że różne zainteresowane strony mogą napisać, na przykład, własny Interface Implementation, o ile przestrzegają logiki *Schema* i semantyki *Interface*. W ten sposób emitent może opracować nowy, bardziej przyjazny dla użytkownika front-end (Interface), bez modyfikowania logiki Contract, lub odwrotnie, można rozszerzyć Schema w celu dodania funkcjonalności i dostarczyć nową wersję dostosowanego Interface Implementation, podczas gdy stare implementacje pozostaną ważne dla podstawowej funkcjonalności.


Kiedy kompilujemy nowy Contract, generate, Genesis (pierwszy krok w emisji lub dystrybucji zasobu), a także jego komponenty (Schema, Interface, Interface Implementation). Następnie Contract jest w pełni operacyjny i może być propagowany do portfeli i użytkowników. Ta metoda, w której Genesis jest połączony z tymi trzema komponentami, gwarantuje wysoki stopień dostosowania (każdy Contract może mieć własną logikę), decentralizacji (każdy może przyczynić się do danego komponentu) i bezpieczeństwa (walidacja pozostaje ściśle określona przez protokół, bez zależności od arbitralnego kodu On-Chain, jak to często ma miejsce w przypadku innych blockchainów).


Chciałbym teraz przyjrzeć się bliżej każdemu z tych komponentów: **Schema**, **Interface** i **Interface Implementation**.


### Schema


W poprzedniej sekcji widzieliśmy, że w ekosystemie RGB, Contract składa się z kilku Elements: Genesis, który ustanawia stan początkowy, oraz kilku innych uzupełniających komponentów. Celem Schema jest deklaratywne opisanie wszystkich Business Logic Contract, tj. struktury danych, używanych typów, dozwolonych operacji i ich warunków. Jest to zatem bardzo ważny element umożliwiający działanie Contract po stronie klienta, ponieważ każdy uczestnik (na przykład Wallet) musi sprawdzić, czy otrzymywane przez niego przejścia stanów są zgodne z logiką zdefiniowaną w Schema.


Schema można porównać do "klasy" w programowaniu obiektowym (OOP). Ogólnie rzecz biorąc, służy ona jako model definiujący komponenty Contract, takie jak :




- Różne typy stanów posiadania i przypisań ;
- Walencje, tj. specjalne prawa, które mogą być uruchamiane (*umarzane*) dla określonych operacji;
- Pola Global State, które opisują globalne, publiczne i współdzielone właściwości Contract;
- Struktura Genesis (pierwsza operacja, która aktywuje Contract);
- Dozwolone formy przejść między stanami i rozszerzeń stanów oraz sposób, w jaki te operacje mogą modyfikować ;
- Metadane powiązane z każdą operacją, do przechowywania tymczasowych lub dodatkowych informacji;
- Reguły określające, w jaki sposób wewnętrzne dane Contract mogą ewoluować (na przykład, czy pole jest zmienne czy kumulatywne);
- Sekwencje operacji uznawanych za ważne: na przykład kolejność przejść, których należy przestrzegać, lub zestaw warunków logicznych, które należy spełnić.


![RGB-Bitcoin](assets/fr/071.webp)


Kiedy *wydawca* aktywów na RGB publikuje Contract, dostarcza Genesis i Schema z nim powiązane. Użytkownicy lub portfele, które chcą wejść w interakcję z aktywem, pobierają ten Schema, aby zrozumieć logikę stojącą za Contract i móc później zweryfikować, czy przejścia, w których będą uczestniczyć, są legalne.


Pierwszym krokiem dla każdego, kto otrzymuje informacje o zasobie RGB (np. transfer tokena), jest sprawdzenie poprawności tych informacji względem Schema. Obejmuje to użycie kompilacji Schema do :




- Sprawdź, czy stany własne, przypisania i inne Elements są poprawnie zdefiniowane i czy przestrzegają narzuconych typów (tak zwany *ścisły system typów*);
- Sprawdzenie, czy reguły przejścia (skrypty walidacyjne) są spełnione. Skrypty te mogą być uruchamiane za pośrednictwem AluVM, który jest obecny po stronie klienta i jest odpowiedzialny za sprawdzanie spójności Business Logic (kwota przelewu, warunki specjalne itp.).


W praktyce Schema nie jest kodem wykonywalnym, co widać w blockchainach przechowujących kod On-Chain (EVM na Ethereum). Wręcz przeciwnie, RGB oddziela Business Logic (deklaratywny) od kodu wykonywalnego na Blockchain (który jest ograniczony do kotwic kryptograficznych). W ten sposób Schema określa zasady, ale stosowanie tych zasad odbywa się poza Blockchain, u każdego uczestnika, zgodnie z zasadą Client-side Validation.


Schema musi zostać skompilowany zanim będzie mógł być używany przez aplikacje RGB. Ta kompilacja tworzy plik binarny (np. `.RGB`) lub zaszyfrowany plik binarny (`.rgba`). Gdy Wallet importuje ten plik, wie, że :




- Jak wygląda każdy typ danych (liczby całkowite, struktury, tablice...) dzięki ścisłemu systemowi typów;
- Jak powinna wyglądać struktura Genesis (aby zrozumieć inicjalizację zasobów);
- Różne typy operacji (State Transitions, State Extensions) i sposób, w jaki mogą one modyfikować stan;
- Reguły skryptowe (wprowadzone w Schema), które silnik AluVM zastosuje do sprawdzenia poprawności operacji.


Jak wyjaśniono w poprzednich rozdziałach, *ścisły system typów* daje nam stabilny, deterministyczny format kodowania: wszystkie zmienne, czy to stany własne, stany globalne czy wartości, są dokładnie opisane (rozmiar, dolne i górne granice, jeśli to konieczne, typ podpisany lub niepodpisany itp.) Możliwe jest również definiowanie zagnieżdżonych struktur, na przykład w celu obsługi złożonych przypadków użycia.


Opcjonalnie Schema może odwoływać się do głównego `SchemaId`, co ułatwia ponowne wykorzystanie istniejącej podstawowej struktury (szablonu). W ten sposób można ewoluować Contract lub tworzyć wariacje (np. nowy typ tokena) na podstawie już sprawdzonego szablonu. Ta modułowość pozwala uniknąć konieczności ponownego tworzenia całych umów i zachęca do standaryzacji najlepszych praktyk.


Inną ważną kwestią jest to, że logika ewolucji stanu (transfery, aktualizacje itp.) jest opisana w Schema w postaci skryptów, reguł i warunków. Tak więc, jeśli projektant Contract chce autoryzować ponowne wydanie lub narzucić mechanizm spalania (niszczenie tokenów), może określić odpowiednie skrypty dla AluVM w części walidacyjnej Schema.


#### Różnica w stosunku do programowalnych blockchainów On-Chain


W przeciwieństwie do systemów takich jak Ethereum, gdzie kod Smart contract (wykonywalny) jest zapisany w samym Blockchain, RGB przechowuje Contract (jego logikę) off-chain, w formie skompilowanego dokumentu deklaratywnego. Oznacza to, że :




- Nie ma kompletnej maszyny wirtualnej Turinga działającej w każdym węźle sieci Bitcoin. Reguły RGB Contract nie są wykonywane na Blockchain, ale u każdego użytkownika, który chce zatwierdzić stan;
- Dane Contract nie zanieczyszczają Blockchain: tylko dowody kryptograficzne (*zobowiązania*) są osadzone w transakcjach Bitcoin (poprzez `Tapret` lub `Opret`);
- Schema może zostać zaktualizowany lub odrzucony (*fast-forward*, *push-back* itp.), bez konieczności Fork na Bitcoin Blockchain. Portfele muszą po prostu zaimportować nowy Schema i dostosować się do zmian konsensusu.


#### Wykorzystanie przez emitenta i użytkowników


Kiedy *emitent* tworzy aktywa (na przykład nieinflacyjny token zamienny), przygotowuje :




- Schema opisujący zasady emisji, transferu itp;
- Genesis dostosowany do tego Schema (z całkowitą liczbą wydanych żetonów, tożsamością pierwotnego właściciela, wszelkimi specjalnymi uprawnieniami do ponownego wydania itp.)


Następnie udostępnia użytkownikom skompilowany Schema (plik `.RGB`), aby każdy, kto otrzyma transfer tego tokena, mógł lokalnie sprawdzić spójność operacji. Bez tego Schema użytkownik nie byłby w stanie zinterpretować danych stanu ani sprawdzić, czy są one zgodne z regułami Contract.


Kiedy więc nowy Wallet chce obsługiwać zasób, musi po prostu zintegrować odpowiedni Schema. Mechanizm ten umożliwia dodanie kompatybilności do nowych typów zasobów RGB bez inwazyjnej zmiany bazy oprogramowania Wallet: wszystko, co jest wymagane, to zaimportowanie pliku binarnego Schema i zrozumienie jego struktury.


Schema definiuje Business Logic w RGB. Wymienia zasady ewolucji Contract, strukturę jego danych (Owned States, Global State, Valencies) i powiązane skrypty walidacyjne (wykonywalne przez AluVM). Dzięki temu deklaratywnemu dokumentowi definicja Contract (skompilowany plik) jest wyraźnie oddzielona od faktycznego wykonywania reguł (po stronie klienta). To oddzielenie zapewnia RGB dużą elastyczność, umożliwiając szeroki zakres przypadków użycia (tokeny zamienne, NFT, bardziej wyrafinowane kontrakty), unikając jednocześnie złożoności i wad typowych dla programowalnych On-Chain blockchainów.


#### Przykład Schema


Spójrzmy na konkretny przykład Schema dla RGB Contract. Jest to fragment Rust z pliku `nia.rs` (inicjały dla "*Non-Inflatable Assets*"), który definiuje model dla tokenów zamiennych, które nie mogą być ponownie wydane poza ich początkowym Supply (aktywa nieinflacyjne). Ten typ tokena może być postrzegany jako odpowiednik, we wszechświecie RGB, ERC20 na Ethereum, tj. tokeny zamienne, które przestrzegają pewnych podstawowych zasad (np. dotyczących transferów, inicjalizacji Supply itp.).


Zanim zagłębimy się w kod, warto przypomnieć ogólną strukturę RGB Schema. Znajduje się tam seria deklaracji z ramkami :




- Możliwy `SchemaId` wskazujący użycie innego podstawowego Schema jako szablonu;
- **Państwa globalne** i **Państwa własne** (z ich ścisłymi typami);
- Walencje** (jeśli występują);
- **Operacje** (Genesis, State Transitions, State Extensions), które mogą odwoływać się do tych stanów i walencji;
- **Ścisły system typów** używany do opisu i walidacji danych;
- Skrypty walidacyjne** (uruchamiane przez AluVM).


![RGB-Bitcoin](assets/fr/072.webp)


Poniższy kod przedstawia pełną definicję Rust Schema. Skomentujemy go część po części, zgodnie z adnotacjami (1) do (9) poniżej:


```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```




- (1) - Nagłówek funkcji i SubSchema**


Funkcja `nia_schema()` zwraca `SubSchema`, wskazując, że ten Schema może częściowo dziedziczyć z bardziej ogólnego Schema. W ekosystemie RGB ta elastyczność umożliwia ponowne wykorzystanie pewnych standardowych Elements głównego Schema, a następnie zdefiniowanie reguł specyficznych dla danego Contract. Tutaj zdecydowaliśmy się nie włączać dziedziczenia, ponieważ `subset_of` będzie `None`.




- (2) - Ogólne właściwości: ffv, subset_of, type_system**


Właściwość `ffv` odpowiada wersji *fast-forward* Contract. Wartość `zero!()` tutaj wskazuje, że jesteśmy w wersji 0 lub początkowej wersji tego Schema. Jeśli później chcesz dodać nowe funkcje (nowy typ operacji itp.), możesz zwiększyć tę wersję, aby wskazać zmianę konsensusu.


Właściwość `subset_of: None` potwierdza brak dziedziczenia. Pole `type_system` odnosi się do ścisłego systemu typów już zdefiniowanego w bibliotece `types`. Ten wiersz wskazuje, że wszystkie dane używane przez Contract używają ścisłej implementacji serializacji dostarczonej przez daną bibliotekę.




- (3) - Państwa globalne


W bloku `global_types` deklarujemy cztery Elements. Używamy klucza, takiego jak `GS_NOMINAL` lub `GS_ISSUED_SUPPLY`, aby odwołać się do nich później:




- `GS_NOMINAL` odnosi się do typu `DivisibleAssetSpec`, który opisuje różne pola utworzonego tokena (pełna nazwa, ticker, precyzja...);
- `GS_DATA` reprezentuje ogólne dane, takie jak wyłączenie odpowiedzialności, metadane lub inny tekst;
- `GS_TIMESTAMP` odnosi się do daty wydania;
- `GS_ISSUED_SUPPLY` ustawia całkowity Supply, tj. maksymalną liczbę tokenów, które można utworzyć.


Słowo kluczowe `once(...)` oznacza, że każde z tych pól może pojawić się tylko raz.




- (4) - Posiadane typy


W `owned_types` deklarujemy `OS_ASSET`, który opisuje stan zamienny. Używamy `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, wskazując, że ilość aktywów (tokenów) jest przechowywana jako 64-bitowa liczba całkowita bez znaku. W ten sposób każda transakcja wyśle określoną ilość jednostek tego tokena, która zostanie zweryfikowana zgodnie z tą ściśle wpisaną strukturą liczbową.




- (5) - Wartości**


Wskazujemy `valency_types: none!()`, co oznacza, że w tym Schema nie ma żadnych walencji, innymi słowy żadnych specjalnych lub dodatkowych praw (takich jak wznowienie, warunkowe wypalenie itp.). Gdyby Schema zawierał takie uprawnienia, zostałyby one zadeklarowane w tej sekcji.




- (6) - Genesis: pierwsze operacje


Tutaj wchodzimy do części, która deklaruje operacje Contract. Genesis jest opisany przez :




- Brak `metadata` (pole `metadata: Ty::<SemId>::UNIT.id(None)`) ;
- Stany globalne, które muszą być obecne tylko raz (`Once`);
- Lista przypisań, gdzie `OS_ASSET` musi pojawić się `OnceOrMore`. Oznacza to, że Genesis wymaga co najmniej jednego `OS_ASSET` Assignment (początkowego posiadacza);
- Brak Valency : `valencies: none!()`.


W ten sposób ograniczamy definicję początkowego wydania tokena: musimy zadeklarować wydany Supply (`GS_ISSUED_SUPPLY`) oraz co najmniej jednego posiadacza (Owned State typu `OS_ASSET`).




- (7) - Rozszerzenia


Pole `extensions: none!()` wskazuje, że żaden State Extension nie jest przewidziany w tym Contract. Oznacza to, że nie ma operacji Redeem prawa cyfrowego (Valency) lub wykonania State Extension przed przejściem. Wszystko odbywa się poprzez Genesis lub State Transitions.




- (8) - Przejścia: TS_TRANSFER


W `transitions` definiujemy typ operacji `TS_TRANSFER`. Wyjaśniamy, że :




- Nie zawiera metadanych;
- Nie modyfikuje Global State (który jest już zdefiniowany w Genesis);
- Jako dane wejściowe przyjmuje jeden lub więcej `OS_ASSETs`. Oznacza to, że musi wydać istniejące stany własne;
- Tworzy (`assignments`) co najmniej jeden nowy `OS_ASSET` (innymi słowy, odbiorca lub odbiorcy otrzymują tokeny);
- Nie generuje żadnych nowych Valency.


Modeluje to zachowanie podstawowego transferu, który zużywa tokeny na UTXO, a następnie tworzy nowe stany Owned na rzecz odbiorców, a tym samym zachowuje równość całkowitej kwoty między wejściami i wyjściami.




- (9) - Skrypt AluVM i punkty wejścia** (w języku francuskim)


Na koniec deklarujemy skrypt AluVM (`Script::AluVM(AluScript { ... })`). Skrypt ten zawiera :




- Jedna lub więcej zewnętrznych bibliotek (`libs`) do wykorzystania podczas walidacji;
- Punkty wejścia wskazujące na przesunięcia funkcji w kodzie AluVM, odpowiadające walidacji Genesis (`ValidateGenesis`) i każdej zadeklarowanej Transition (`ValidateTransition(TS_TRANSFER)`).


Ten kod walidacyjny jest odpowiedzialny za zastosowanie Business Logic. Na przykład, będzie on sprawdzał :




- Aby wartość `GS_ISSUED_SUPPLY` nie została przekroczona podczas Genesis ;
- Suma `wejść` (wydanych tokenów) jest równa sumie `przypisań` (otrzymanych tokenów) dla `TS_TRANSFER`.


Jeśli zasady te nie będą przestrzegane, przejście zostanie uznane za nieważne.


Ten przykład "*Nienadmuchiwanego Aktywa Zamiennego*" Schema pozwala nam lepiej zrozumieć strukturę prostego RGB zamiennego tokena Contract. Wyraźnie widzimy rozdział między opisem danych (Stany Globalne i Własne), deklaracją operacji (Genesis, Przejścia, Rozszerzenia) i implementacją walidacji (skrypty AluVM). Dzięki temu modelowi token zachowuje się jak klasyczny token zamienny, ale pozostaje walidowany po stronie klienta i nie zależy od infrastruktury On-Chain do wykonania swojego kodu. Jedynie zobowiązania kryptograficzne są zakotwiczone w Bitcoin Blockchain.


### Interface


Interface jest Layer zaprojektowanym w celu uczynienia Contract czytelnym i możliwym do manipulowania, zarówno przez użytkowników (czytanie przez człowieka), jak i przez portfele (czytanie przez oprogramowanie). Interface odgrywa zatem rolę porównywalną do Interface w obiektowym języku programowania (Java, cecha Rust itp.), ponieważ eksponuje i wyjaśnia strukturę funkcjonalną Contract, niekoniecznie ujawniając wewnętrzne szczegóły Business Logic.


W przeciwieństwie do Schema, który jest czysto deklaratywny i skompilowany do pliku binarnego, który jest trudny w użyciu, Interface zapewnia klucze odczytu potrzebne do :




- Wymień i opisz Stany Globalne i Stany Własne zawarte w Contract;
- Uzyskaj dostęp do nazw i wartości każdego pola, aby można je było wyświetlić (np. dla tokena, znajdź jego ticker, maksymalną kwotę itp;)
- Interpretuj i konstruuj operacje Contract (Genesis, State Transition lub State Extension), kojarząc dane ze zrozumiałymi nazwami (np. wykonaj przelew, wyraźnie określając "kwotę", a nie identyfikator binarny).


![RGB-Bitcoin](assets/fr/073.webp)


Dzięki Interface można na przykład napisać kod w Wallet, który zamiast manipulować polami, bezpośrednio manipuluje etykietami, takimi jak "liczba tokenów", "nazwa zasobu" itp. W ten sposób zarządzanie Contract staje się bardziej intuicyjne. W ten sposób zarządzanie Contract staje się bardziej intuicyjne.


#### Ogólne działanie


Metoda ta ma wiele zalet:




- Standaryzacja:**


Ten sam typ Contract może być obsługiwany przez standardowy Interface, współdzielony przez kilka implementacji Wallet. Ułatwia to kompatybilność i ponowne wykorzystanie kodu.




- Wyraźne rozdzielenie Schema i Interface:**


W projekcie RGB, Schema (Business Logic) i Interface (prezentacja i manipulacja) są dwoma niezależnymi bytami. Programiści, którzy piszą logikę Contract, mogą skoncentrować się na Schema, nie martwiąc się o ergonomię lub reprezentację danych, podczas gdy inny zespół (lub ten sam zespół, ale na innej osi czasu) może opracować Interface.




- Elastyczna ewolucja:**


Interface może być modyfikowany lub dodawany po wydaniu zasobu, bez konieczności zmiany samego Contract. Jest to zasadnicza różnica w porównaniu z niektórymi systemami On-Chain Smart contract, w których Interface (często zmieszany z kodem wykonawczym) jest zamrożony w Blockchain.




- Możliwość korzystania z wielu Interface


Ten sam Contract może być udostępniany za pośrednictwem różnych interfejsów dostosowanych do różnych potrzeb: prosty Interface dla użytkownika końcowego, inny bardziej zaawansowany dla emitenta, który musi zarządzać złożonymi operacjami konfiguracyjnymi. Wallet może następnie wybrać, który Interface zaimportować, w zależności od jego zastosowania.


![RGB-Bitcoin](assets/fr/074.webp)


W praktyce, gdy Wallet pobiera RGB Contract (poprzez plik `.RGB` lub `.rgba`), importuje również powiązany Interface, który również jest kompilowany. W czasie wykonywania Wallet może na przykład :




- Przeglądaj listę stanów i odczytuj ich nazwy, aby wyświetlić Ticker, Initial Amount, Issue Date itp. na Interface użytkownika, zamiast nieczytelnego identyfikatora numerycznego;
- Tworzy operację (taką jak przelew) przy użyciu jawnych nazw parametrów: zamiast pisać `assignments { OS_ASSET => 1 }`, może zaoferować użytkownikowi pole "Amount" w formularzu i przetłumaczyć te informacje na ściśle wpisane pola oczekiwane przez Contract.


#### Różnica w stosunku do Ethereum i innych systemów


W Ethereum, Interface (opisany poprzez ABI, *Application Binary Interface*) jest generalnie pochodną kodu przechowywanego w On-Chain (Smart contract). Modyfikacja określonej części Interface bez dotykania samego Contract może być kosztowna lub skomplikowana. Jednakże, RGB jest oparty na logice w całości off-chain, z danymi zakotwiczonymi w *commitments* na Bitcoin. Taka konstrukcja umożliwia modyfikację Interface (lub jego implementacji) bez wpływu na podstawowe bezpieczeństwo Contract, ponieważ walidacja reguł biznesowych pozostaje w Schema i odwołującym się do niego kodzie AluVM.


#### Kompilacja Interface


Podobnie jak Schema, Interface jest zdefiniowany w kodzie źródłowym (często w Rust) i kompilowany do pliku `.RGB` lub `.rgba`. Ten plik binarny zawiera wszystkie informacje wymagane przez Wallet do :




- Identyfikacja pól według nazwy ;
- Połącz każde pole (i jego wartość) ze ścisłym typem systemu zdefiniowanym w Contract;
- Poznaj różne dozwolone operacje i sposób ich tworzenia.


Po zaimportowaniu Interface, Wallet może poprawnie wyświetlać Contract i proponować użytkownikowi interakcje.


### Interfejsy standaryzowane przez stowarzyszenie LNP/BP


W ekosystemie RGB, Interface jest używany do nadania czytelnego i manipulowalnego znaczenia danym i operacjom Contract. W ten sposób Interface uzupełnia Schema, który wewnętrznie opisuje Business Logic (ścisłe typy, skrypty walidacyjne itp.). W tej sekcji przyjrzymy się standardowym interfejsom opracowanym przez stowarzyszenie LNP/BP dla popularnych typów Contract (tokeny zamienne, NFT itp.).


Dla przypomnienia, chodzi o to, że każdy Interface opisuje sposób wyświetlania i manipulowania Contract po stronie Wallet, wyraźnie nazywając pola (takie jak `spec`, `ticker`, `issuedSupply`...) i definiując możliwe operacje (takie jak `Transfer`, `Burn`, `Rename`...). Kilka interfejsów już działa, ale w przyszłości będzie ich coraz więcej.


#### Niektóre gotowe do użycia interfejsy


**RGB20** to Interface dla aktywów zamiennych, który można porównać do standardu ERC20 Ethereum. Idzie on jednak o krok dalej, oferując bardziej rozbudowaną funkcjonalność:




- Na przykład możliwość zmiany nazwy aktywa (zmiana *tickera* lub pełnej nazwy) po jego wyemitowaniu lub dostosowania jego precyzji (*podziały akcji*);
- Może również opisywać mechanizmy wtórnej reemisji (ograniczonej lub nieograniczonej) oraz spalenia, a następnie zastąpienia, w celu upoważnienia emitenta do zniszczenia, a następnie odtworzenia aktywów pod pewnymi warunkami;


Na przykład, RGB20 Interface może być połączony ze schematem **Non-Inflatable Asset (NIA)**, który narzuca początkowy Supply bez inflacji, lub z innymi bardziej zaawansowanymi schematami, zgodnie z wymaganiami.


**RGB21** dotyczy umów typu NFT lub szerzej, wszelkich unikalnych treści cyfrowych, takich jak reprezentacja mediów cyfrowych (obrazy, muzyka itp.). Oprócz opisu emisji i transferu pojedynczego zasobu, obejmuje on takie funkcje, jak :




- Zintegrowana obsługa bezpośredniego dołączania pliku (do 16 MB) do Contract (do pobierania po stronie klienta);
- Możliwość wprowadzenia przez właściciela "*grawerowania*" w historii, aby udowodnić przeszłość Ownership NFT.


**RGB25** to hybrydowy standard łączący aspekty zamienne i niezamienne. Został zaprojektowany dla częściowo zamiennych aktywów, takich jak tokenizacja nieruchomości, gdzie chcesz podzielić nieruchomość, zachowując link do jednego głównego zasobu (innymi słowy, masz zamienne części domu, połączone z niezamiennym domem). Technicznie rzecz biorąc, ten Interface może być powiązany z **Collectible Fungible Asset* (CFA)** Schema, który uwzględnia pojęcie podziału przy jednoczesnym śledzeniu oryginalnego zasobu.


#### Interfejsy w fazie rozwoju


Inne interfejsy są planowane do bardziej specjalistycznych zastosowań, ale nie są jeszcze dostępne:




- RGB22**, dedykowany tożsamościom cyfrowym, do zarządzania identyfikatorami i profilami On-Chain w ekosystemie RGB;
- RGB23**, do zaawansowanego znakowania czasem, z wykorzystaniem niektórych pomysłów *Opentimestamps*, ale z funkcjami identyfikowalności;
- RGB24**, którego celem jest stworzenie odpowiednika zdecentralizowanego systemu nazw domen (DNS) podobnego do *Ethereum Name Service*;
- RGB26**, zaprojektowany do zarządzania DAO (*Decentralized Autonomous Organization*) w bardziej złożonym formacie (zarządzanie, głosowanie itp.);
- RGB30**, bardzo podobny do RGB20, ale ze szczególną cechą uwzględnienia zdecentralizowanej emisji początkowej i wykorzystania rozszerzeń państwowych. Byłoby to stosowane w przypadku aktywów, których ponowna emisja jest zarządzana przez kilka podmiotów lub podlega bardziej rygorystycznym warunkom.


Oczywiście, w zależności od daty zapoznania się z tym kursem, interfejsy te mogą już działać i być dostępne.


#### Przykład Interface


Ten fragment kodu Rust pokazuje [RGB20](https://github.com/RGB-WG/RGB-std/blob/master/src/Interface/rgb20.rs) Interface (zasób zamienny). Kod ten pochodzi z pliku `rgb20.rs` w standardowej bibliotece RGB. Przyjrzyjmy się mu, aby zrozumieć strukturę Interface i sposób, w jaki stanowi on pomost między, z jednej strony, Business Logic (zdefiniowanym w Schema), a z drugiej strony, funkcjami dostępnymi dla portfeli i użytkowników.


```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```


W tym Interface zauważamy podobieństwa do struktury Schema: znajdujemy deklarację Global State, stany własne, operacje Contract (Genesis i przejścia), a także obsługę błędów. Jednak Interface koncentruje się na prezentacji i manipulacji tymi Elements dla Wallet lub dowolnej innej aplikacji.


Różnica w stosunku do Schema leży w naturze typów. Schema używa ścisłych typów (takich jak `FungibleType::Unsigned64Bit`) i bardziej technicznych identyfikatorów. Interface używa nazw pól, makr (`fname!()`, `tn!()`) i odniesień do klas argumentów (`ArgSpec`, `OwnedIface::Rights`...). Celem jest ułatwienie funkcjonalnego zrozumienia i organizacji Elements dla Wallet.


Ponadto Interface może wprowadzać dodatkowe funkcje do podstawowego Schema (np. zarządzanie prawem `burnEpoch`), o ile pozostaje to zgodne z ostateczną zatwierdzoną logiką po stronie klienta. Sekcja "skryptu" AluVM w Schema zapewni ważność kryptograficzną, podczas gdy Interface opisuje sposób interakcji użytkownika (lub Wallet) z tymi stanami i przejściami.


#### Global State i przypisania


W sekcji `global_state` znajdziemy pola takie jak `spec` (opis zasobu), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Są to pola, które Wallet może odczytać i przedstawić. Na przykład:




- `spec` wyświetli konfigurację tokena;
- `issuedSupply` lub `burnedSupply` podają nam całkowitą liczbę wydanych lub spalonych tokenów itp.


W sekcji `assignments` definiujemy różne role lub uprawnienia. Na przykład:




- `assetOwner` odpowiada posiadaniu tokenów (jest to zamienny *Owned State*);
- `burnRight` odpowiada możliwości spalania tokenów;
- updateRight` odpowiada prawu do zmiany nazwy zasobu.


Słowo kluczowe `public` lub `private` (np. `AssignIface::public(...)`) wskazuje czy te stany są widoczne (`public`) czy poufne (`private`). Jeśli chodzi o `Req::NoneOrMore`, `Req::Optional`, wskazują one na oczekiwane wystąpienie.


#### Genesis i przejścia


Część `Genesis` opisuje sposób inicjalizacji zasobu:




- Pola `spec`, `data`, `created`, `issuedSupply` są obowiązkowe (`ArgSpec::required()`);
- Przypisania takie jak `assetOwner` mogą być obecne w wielu kopiach (`ArgSpec::many()`), pozwalając na dystrybucję tokenów do wielu początkowych posiadaczy;
- Pola takie jak `inflationAllowance` lub `burnEpoch` mogą (ale nie muszą) być zawarte w Genesis.


Następnie, dla każdego Przejścia (`Transfer`, `Issue`, `Burn`...), Interface definiuje, których pól operacja oczekuje jako danych wejściowych, które pola operacja wygeneruje jako dane wyjściowe oraz wszelkie błędy, które mogą wystąpić. Na przykład:


**Przejście :**




- Wejścia: `previous` → musi być `assetOwner`;
- Przypisania: `beneficiary` → będzie nowym `assetOwner` ;
- Błąd: `NON_EQUAL_AMOUNTS` (Wallet będzie w stanie obsłużyć przypadki, w których suma wejściowa nie odpowiada sumie wyjściowej).


**Transition `Issue` :**




- Opcjonalne (`optional: true`), ponieważ dodatkowa emisja nie musi być aktywowana;
- Wejścia: `used` → an `inflationAllowance`, czyli pozwolenie na dodawanie kolejnych tokenów ;
- Przypisania: `beneficiary` (otrzymane nowe tokeny) i `future` (pozostałe `inflationAllowance`) ;
- Możliwe błędy: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE` itp.


**Poparz przejście :**




- Wejścia: `used` → a `burnRight` ;
- Globals : `burnedSupply` wymagane ;
- Przypisania: `future` → możliwa kontynuacja `burnRight`, jeśli nie spaliliśmy wszystkiego ;
- Błędy: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.


Każda operacja jest zatem opisana w sposób czytelny dla Wallet. Umożliwia to wyświetlenie graficznego Interface, gdzie użytkownik może wyraźnie zobaczyć: "Masz prawo do spalania. Czy chcesz spalić określoną ilość? Kod wie, że należy wypełnić pole `burnedSupply` i sprawdzić, czy `burnRight` jest ważne.


Podsumowując, ważne jest, aby pamiętać, że Interface, jakkolwiek kompletny, sam w sobie nie definiuje wewnętrznej logiki Contract. Sedno pracy jest wykonywane przez **Schema**, który zawiera ścisłe typy, strukturę Genesis, przejścia i tak dalej. Interface po prostu eksponuje te Elements w bardziej intuicyjny i nazwany sposób, do wykorzystania w aplikacji.


Dzięki modułowości RGB, Interface może zostać zaktualizowany (na przykład poprzez dodanie przejścia `Rename`, poprawienie wyświetlania pola itp.) bez konieczności przepisywania całego Contract. Użytkownicy Interface mogą natychmiast skorzystać z tych ulepszeń, gdy tylko zaktualizują plik `.RGB` lub `.rgba`.


Ale po zadeklarowaniu Interface, musisz połączyć go z odpowiednim Schema. Odbywa się to za pośrednictwem ***Interface Implementation***, który określa sposób mapowania każdego nazwanego pola (takiego jak `fname!("assetOwner")`) na ścisły identyfikator (taki jak `OS_ASSET`) zdefiniowany w Schema. Zapewnia to, na przykład, że gdy Wallet manipuluje polem `burnRight`, jest to stan, który w Schema opisuje zdolność do wypalania tokenów.


### Interface Implementation


W architekturze RGB widzieliśmy, że każdy komponent (Schema, Interface, itd.) może być rozwijany i kompilowany niezależnie. Jednak nadal istnieje jeden niezbędny element, który łączy te różne bloki konstrukcyjne: ***Interface Implementation***. To jest to, co wyraźnie mapuje identyfikatory lub pola zdefiniowane w Schema (po stronie Business Logic) na nazwy zadeklarowane w Interface (po stronie prezentacji i interakcji z użytkownikiem). Tak więc, gdy Wallet ładuje Contract, może dokładnie zrozumieć, które pole odpowiada czemu i jak operacja nazwana w Interface odnosi się do logiki Schema.


Ważną kwestią jest to, że Interface Implementation niekoniecznie ma na celu ujawnienie wszystkich funkcji Schema, ani wszystkich pól Interface: może być ograniczony do podzbioru. W praktyce umożliwia to ograniczenie lub filtrowanie niektórych aspektów Schema. Na przykład można mieć Schema z czterema typami operacji, ale implementację Interface, która mapuje tylko dwa z nich w danym kontekście. I odwrotnie, jeśli Interface proponuje dodatkowe punkty końcowe, możemy nie implementować ich tutaj.


Oto klasyczny przykład Interface Implementation, w którym kojarzymy *Non-Inflatable Asset* (NIA) Schema z RGB20 Interface:


```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```


W tym wdrożeniu Interface :




- Wyraźnie odwołujemy się do Schema, poprzez `nia_schema()`, i Interface, poprzez `Rgb20::iface()`. Wywołania `Schema.schema_id()` i `iface.iface_id()` są używane do Anchor Interface Implementation po stronie kompilacji (kojarzy to kryptograficzne identyfikatory tych dwóch komponentów);
- Ustanowiono mapowanie między Schema Elements i Interface Elements. Na przykład pole `GS_NOMINAL` w Schema jest powiązane z ciągiem `"spec"` po stronie Interface (`NamedField::with(GS_NOMINAL, fname!("spec"))`). To samo robimy dla operacji, takich jak `TS_TRANSFER`, które łączymy z `"Transfer"` w Interface... ;
- Widzimy, że nie ma żadnych walencji (`valencies: none!()`) ani rozszerzeń (`extensions: none!()`), co odzwierciedla fakt, że NIA Contract nie używa tych funkcji.


Wynikiem kompilacji jest oddzielny plik `.RGB` lub `.rgba`, który należy zaimportować do Wallet oprócz Schema i Interface. W ten sposób oprogramowanie wie, jak konkretnie połączyć Contract NIA (którego logika jest opisana przez Schema) z Interface "RGB20" (który zapewnia ludzkie nazwy i tryb interakcji dla zamiennych tokenów), stosując Interface Implementation jako bramę między nimi.


#### Dlaczego oddzielny Interface Implementation?


Separacja zwiększa elastyczność. Pojedynczy Schema może mieć kilka różnych implementacji Interface, z których każda mapuje inny zestaw funkcji. Co więcej, sam Interface Implementation może ewoluować lub zostać przepisany bez konieczności zmiany Schema lub Interface. Zachowuje to zasadę modułowości RGB: każdy komponent (Schema, Interface, Interface Implementation) może być wersjonowany i aktualizowany niezależnie, o ile przestrzegane są zasady kompatybilności narzucone przez protokół (te same identyfikatory, spójność typów itp.).


W konkretnym zastosowaniu, gdy Wallet ładuje Contract, musi :




- Załaduj skompilowany **Schema** (aby poznać strukturę Business Logic);
- Załaduj skompilowany **Interface** (aby zrozumieć nazwy i operacje po stronie użytkownika) ;
- Załaduj skompilowany **Interface Implementation** (aby połączyć logikę Schema z nazwami Interface, operacja po operacji, pole po polu).


Ta modułowa architektura umożliwia korzystanie z takich scenariuszy, jak :




- Ograniczenie niektórych operacji dla określonych użytkowników: zaoferowanie częściowej implementacji Interface, która daje dostęp tylko do podstawowych transferów, bez oferowania na przykład funkcji wypalania lub aktualizacji;
- Prezentacja zmiany: zaprojektuj Interface Implementation, który zmienia nazwę pola w Interface lub mapuje je w inny sposób, bez zmiany podstawy Contract;
- Obsługa wielu schematów: Wallet może załadować wiele implementacji Interface dla tego samego typu Interface, aby obsługiwać różne schematy (różne logiki tokenów), pod warunkiem, że ich struktura jest zgodna.


W następnym rozdziale przyjrzymy się, jak działa przelew Contract i jak generowane są faktury RGB.


## Przelewy Contract


<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>


:::video id=75eb5a8d-1910-4155-b5e3-81204c9a8901:::


W tym rozdziale przeanalizujemy proces transferu Contract w ekosystemie RGB. Aby to zilustrować, przyjrzymy się Alice i Bobowi, naszym zwykłym bohaterom, którzy chcą dokonać Exchange zasobu RGB. Pokażemy również kilka fragmentów poleceń z narzędzia wiersza poleceń `RGB`, aby zobaczyć, jak działa ono w praktyce.


### Zrozumienie transferu RGB Contract


Weźmy przykład transferu między Alice i Bobem. W tym przykładzie zakładamy, że Bob dopiero zaczyna korzystać z RGB, podczas gdy Alice posiada już aktywa RGB w swoim Wallet. Zobaczymy, jak Bob konfiguruje swoje środowisko, importuje odpowiedni Contract, a następnie żąda transferu od Alice i wreszcie, jak Alice przeprowadza faktyczną transakcję na Bitcoin Blockchain.


#### 1) Instalacja RGB Wallet


Przede wszystkim Bob musi zainstalować RGB Wallet, czyli oprogramowanie zgodne z protokołem. Na początku nie zawiera ono żadnych umów. Bob będzie również potrzebował :




- Bitcoin Wallet do zarządzania urządzeniami UTXO;
- Połączenie z węzłem Bitcoin (lub serwerem Electrum), aby można było zidentyfikować UTXO i propagować transakcje w sieci.


Dla przypomnienia, **Stany Własne** w RGB odnoszą się do UTXO Bitcoin. Dlatego zawsze musimy być w stanie zarządzać i wydawać UTXO w transakcji Bitcoin, która zawiera zobowiązania kryptograficzne (`Tapret` lub `Opret`) wskazujące na dane RGB.


#### 2) Pozyskiwanie informacji z Contract


Następnie Bob musi pobrać interesujące go dane Contract. Dane te mogą krążyć dowolnym kanałem: strona internetowa, e-mail, aplikacja do przesyłania wiadomości.... W praktyce są one grupowane w ***Consignment***, tj. mały pakiet danych zawierający :




- **Genesis**, który definiuje stan początkowy Contract;
- **Schema**, który opisuje Business Logic (ścisłe typy, skrypty walidacyjne itp.);
- **Interface**, który definiuje prezentację Layer (nazwy pól, dostępne operacje);
- **Interface Implementation**, który konkretnie łączy Schema z Interface.


![RGB-Bitcoin](assets/fr/075.webp)


Całkowity rozmiar jest często rzędu kilku kilobajtów, ponieważ każdy komponent zazwyczaj waży mniej niż 200 bajtów. Możliwe jest również nadawanie tego Consignment w Base58, za pośrednictwem kanałów odpornych na cenzurę (takich jak na przykład Nostr lub Lightning Network) lub jako kod QR.


#### 3) Import i walidacja Contract


Gdy Bob otrzyma Consignment, importuje go do swojego RGB Wallet. Spowoduje to :




- Sprawdź, czy Genesis i Schema są prawidłowe;
- Ładowanie Interface i Interface Implementation ;
- Zaktualizuj dane po stronie klienta Stash.


Bob może teraz zobaczyć zasób w swoim Wallet (nawet jeśli nie jest jeszcze jego właścicielem) i zrozumieć, jakie pola są dostępne, jakie operacje są możliwe ... Następnie musi skontaktować się z osobą, która faktycznie jest właścicielem zasobu, który ma zostać przeniesiony. W naszym przykładzie jest to Alice.


Proces odkrywania, kto posiada określony zasób RGB, jest podobny do znajdowania płatnika Bitcoin. Szczegóły tego połączenia zależą od zastosowania (rynki, prywatne kanały czatu, fakturowanie, sprzedaż towarów i usług, wynagrodzenie...).


#### 4) Wydanie Invoice


Aby zainicjować transfer aktywów RGB, Bob musi najpierw wystawić Invoice. Ten Invoice jest używany do :




- Poinformuj Alice o typie operacji do wykonania (na przykład `Transfer` z RGB20 Interface);
- Przekazanie Alicji *Seal Definition* Boba (tj. UTXO, na którym chce on otrzymać zasób);
- Określ wymaganą ilość aktywnego składnika (np. 100 jednostek).


Bob używa narzędzia `RGB` w linii poleceń. Załóżmy, że chce 100 jednostek tokena, którego `ContractId` jest znany, chce polegać na `Tapret` i określa jego UTXO (`456e3..dfe1:0`):


```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```


Na końcu tego rozdziału przyjrzymy się bliżej strukturze faktur RGB.


#### 5) Transmisja Invoice


Wygenerowany Invoice (np. jako URL: `RGB:2WBcas9.../RGB20/100+utxob:...`) zawiera wszystkie informacje potrzebne Alice do przygotowania transferu. Podobnie jak w przypadku Consignment, można go zakodować w kompaktowy sposób (Base58 lub inny format) i wysłać za pośrednictwem aplikacji do przesyłania wiadomości, poczty e-mail, Nostr...


![RGB-Bitcoin](assets/fr/076.webp)


#### 6) Przygotowanie transakcji po stronie Alice


Alicja otrzymuje Invoice Boba. W swoim RGB Wallet ma Stash zawierający aktywo, które ma zostać przekazane. Aby wydać UTXO zawierający aktywa, musi ona najpierw wykonać generate PSBT (*Partially Signed Bitcoin Transaction*), tj. niekompletną transakcję Bitcoin, używając UTXO, który posiada:


```bash
alice$ wallet construct tx.psbt
```


Ta podstawowa transakcja (na razie niepodpisana) zostanie wykorzystana do Anchor kryptograficznego Commitment związanego z przelewem do Boba. UTXO Alicji zostanie zatem wydany, a na wyjściu umieścimy Commitment `Tapret` lub `Opret` dla Boba.


#### 7) Generowanie transferu Consignment


Następnie Alice tworzy ***Terminal Consignment*** (czasami nazywany "transferem Consignment") za pomocą polecenia :


```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```


Ten nowy plik `Consignment.RGB` zawiera :




- Pełna historia przejść między stanami wymagana do zatwierdzenia zasobu do chwili obecnej (od Genesis);
- Nowy State Transition, który przenosi aktywa z Alice na Boba, zgodnie z Invoice wydanym przez Boba;
- Niekompletna transakcja Bitcoin (*Witness Transaction*) (`tx.PSBT`), która wydaje Single-Use Seal Alicji, zmodyfikowana tak, aby zawierała kryptograficzny Commitment dla Boba.


Na tym etapie transakcja nie jest jeszcze transmitowana w sieci Bitcoin. Consignment jest większy niż podstawowy Consignment, ponieważ zawiera całą historię (*łańcuch dowodowy*), aby udowodnić legalność aktywów.


#### 8) Bob sprawdza i akceptuje Consignment


Alice przesyła ten **Terminal Consignment** do Boba. Następnie Bob :




- Sprawdź ważność State Transition (upewnij się, że historia jest spójna, że zasady Contract są przestrzegane itp;)
- Dodaj go do lokalnego Stash;
- Ewentualnie generate podpis (`sig:...`) na Consignment, aby udowodnić, że został on sprawdzony i zatwierdzony (czasami nazywany "*payslip*").


```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```


![RGB-Bitcoin](assets/fr/077.webp)


#### 9) Opcja: Bob wysyła potwierdzenie z powrotem do Alice (*payslip*)


Jeśli Bob chce, może wysłać ten podpis z powrotem do Alicji. Oznacza to:




- Że uznaje przejście za ważne;
- Że zgadza się na transmisję transakcji Bitcoin.


Nie jest to obowiązkowe, ale może zapewnić Alice pewność, że nie będzie późniejszych sporów dotyczących transferu.


#### 10) Alice podpisuje i publikuje transakcję


Alice może wtedy :




- Sprawdź podpis Boba (`RGB check <sig>`) ;
- Podpisz *Witness Transaction*, który nadal jest PSBT (`Wallet sign`);
- Opublikuj Witness Transaction w sieci Bitcoin (`-publish`).


```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```


![RGB-Bitcoin](assets/fr/078.webp)


Po potwierdzeniu transakcja ta oznacza zakończenie transferu. Bob staje się nowym właścicielem aktywów: ma teraz Owned State wskazujący na UTXO, który kontroluje, co potwierdza obecność Commitment w transakcji.


Podsumowując, oto kompletny proces transferu:


![RGB-Bitcoin](assets/fr/079.webp)


### Zalety transferów RGB




- Poufność** :


Tylko Alicja i Bob mają dostęp do wszystkich danych State Transition. Informacje te Exchange przekazują poza Blockchain, za pośrednictwem przesyłek. Zobowiązania kryptograficzne w transakcji Bitcoin nie ujawniają rodzaju aktywów ani kwoty, co gwarantuje znacznie większą poufność niż inne systemy tokenów On-Chain.




- Walidacja po stronie klienta** :


Bob może sprawdzić spójność transferu, porównując *Consignment* z *anchors* w Bitcoin Blockchain. Nie potrzebuje walidacji przez stronę trzecią. Alicja nie musi publikować pełnej historii na Blockchain, co zmniejsza obciążenie protokołu bazowego i poprawia poufność.




- Uproszczona atomowość** :


Złożone wymiany (na przykład atomowe swapy między BTC a aktywem RGB) mogą być przeprowadzane w ramach jednej transakcji, unikając potrzeby stosowania skryptów HTLC lub PTLC. Jeśli umowa nie jest transmitowana, każdy może ponownie wykorzystać swoje UTXO w inny sposób.


### Diagram podsumowujący transfer


Zanim przyjrzymy się fakturom bardziej szczegółowo, poniżej znajduje się schemat ogólnego przepływu przelewu RGB:




- Bob instaluje RGB Wallet i otrzymuje początkowy Contract Consignment;
- Bob wystawia Invoice ze wskazaniem UTXO, gdzie należy odebrać zasób;
- Alice otrzymuje Invoice, buduje PSBT i generuje Terminal Consignment;
- Bob akceptuje go, sprawdza, dodaje dane do swojego Stash i podpisuje (*payslip*), jeśli to konieczne;
- Alice publikuje transakcję w sieci Bitcoin;
- Potwierdzenie transakcji czyni przelew oficjalnym.


![RGB-Bitcoin](assets/fr/080.webp)


Transfer ilustruje całą moc i elastyczność protokołu RGB: prywatny Exchange, zweryfikowany po stronie klienta, zakotwiczony minimalnie i dyskretnie na Bitcoin Blockchain i zachowujący najlepsze zabezpieczenia protokołu (brak ryzyka Double-spending). To sprawia, że RGB jest obiecującym ekosystemem dla transferów wartości, które są bardziej poufne i skalowalne niż programowalne łańcuchy bloków On-Chain.


### Faktury RGB


W tej sekcji wyjaśnimy szczegółowo, w jaki sposób **faktury** działają w ekosystemie RGB i w jaki sposób umożliwiają wykonywanie operacji (w szczególności przelewów) za pomocą Contract. Najpierw przyjrzymy się używanym identyfikatorom, następnie sposobowi ich kodowania, a na końcu strukturze Invoice wyrażonej jako adres URL (format, który jest wystarczająco przydatny do użycia w portfelach).


#### Identyfikatory i kodowanie


Unikalny identyfikator jest zdefiniowany dla każdego z następujących Elements:




- RGB Contract;
- Jego Schema (Business Logic) ;
- Są to Interface i Interface Implementation;
- Jego aktywa (tokeny, NFT itp.),


Ta unikalność jest bardzo ważna, ponieważ każdy element systemu musi być rozróżnialny. Na przykład Contract X nie może być mylony z innym Contract Y, a dwa różne interfejsy (na przykład RGB20 i RGB21) muszą mieć różne identyfikatory.


Aby identyfikatory te były zarówno wydajne (mały rozmiar), jak i czytelne, używamy :




- Kodowanie Base58, które pozwala uniknąć stosowania mylących znaków (np. `0` i litera `O`) i zapewnia stosunkowo krótkie ciągi znaków;
- Przedrostek wskazujący na charakter identyfikatora, zwykle w postaci `RGB:` lub podobnego URN.


Na przykład, `ContractId` może być reprezentowany przez coś takiego jak :


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```


Prefiks `RGB:` potwierdza, że jest to identyfikator RGB, a nie link HTTP lub inny protokół. Dzięki temu prefiksowi portfele są w stanie poprawnie zinterpretować ciąg znaków.


#### Segmentacja identyfikatorów


Identyfikatory RGB są często dość długie, ponieważ podstawowe (kryptograficzne) zabezpieczenia mogą wymagać pól o długości 256 bitów lub więcej. Aby ułatwić odczyt i weryfikację przez człowieka, *dzielimy* te ciągi na kilka bloków oddzielonych myślnikiem (`-`). Tak więc, zamiast długiego, nieprzerwanego ciągu znaków, dzielimy go na krótsze bloki. Ta praktyka jest powszechna w przypadku kart kredytowych lub numerów telefonów i ma również zastosowanie tutaj w celu ułatwienia weryfikacji. Na przykład, użytkownik lub partner może zostać poinformowany: "*Proszę sprawdzić, czy trzeci blok to `9GEgnyMj7`*", zamiast porównywać całość na raz. Ostatni blok jest często używany jako **suma kontrolna**, aby mieć system wykrywania błędów lub literówek.


Jako przykład, `ContractId` w kodowaniu base58 i segmentacji może mieć postać :


```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```


Każdy z myślników dzieli ciąg znaków na sekcje. Nie ma to wpływu na semantykę kodu, a jedynie na jego prezentację.


#### Używanie adresów URL dla faktur


RGB Invoice jest prezentowany jako adres URL. Oznacza to, że można go kliknąć lub zeskanować (jako kod QR), a Wallet może go bezpośrednio zinterpretować w celu przeprowadzenia transakcji. Ta prostota interakcji różni się od niektórych innych systemów, w których trzeba kopiować i wklejać różne dane do różnych pól w oprogramowaniu.


Invoice dla tokena zamiennego (np. tokena RGB20) może wyglądać następująco:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Przeanalizujmy ten adres URL:




- `RGB:`** (prefiks): wskazuje link wywołujący protokół RGB (analogiczny do `http:` lub `Bitcoin:` w innych kontekstach);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: reprezentuje `ContractId` tokena, którym chcesz manipulować;
- `/RGB20/100`**: wskazuje, że używany jest `RGB20` Interface i że wymagane jest 100 jednostek zasobu. Składnia jest następująca: `/Interface/amount` ;
- `+utxob:`**: określa, że dodawane są informacje o odbiorcy UTXO (a dokładniej definicja Single-Use Seal);
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: jest to *blinded* UTXO (lub Seal Definition). Innymi słowy, Bob zamaskował swój dokładny UTXO, więc nadawca (Alicja) nie wie, jaki jest dokładny Address. Wie tylko, że istnieje ważny Seal odnoszący się do UTXO kontrolowanego przez Boba.


Fakt, że wszystko mieści się w jednym adresie URL, ułatwia życie użytkownikowi: proste kliknięcie lub skanowanie w Wallet i operacja jest gotowa do wykonania.


Można sobie wyobrazić systemy, w których zamiast `ContractId` używany jest prosty ticker (np. `USDT`). To jednak spowodowałoby poważne problemy z zaufaniem i bezpieczeństwem: ticker nie jest unikalnym odniesieniem (kilka kontraktów mogłoby twierdzić, że nazywają się `USDT`). W RGB chcemy mieć unikalny, jednoznaczny identyfikator kryptograficzny. Stąd przyjęcie 256-bitowego ciągu, zakodowanego w base58 i podzielonego na segmenty. Użytkownik wie, że manipuluje dokładnie tym Contract, którego ID to `2WBcas9-yjz...`, a nie żadnym innym.


#### Dodatkowe parametry adresu URL


Można również dodać dodatkowe parametry do adresu URL, w taki sam sposób jak w przypadku HTTP, takie jak :


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```




- `?sig=...`: reprezentuje na przykład podpis powiązany z Invoice, który niektóre portfele mogą zweryfikować;
- Jeśli Wallet nie zarządza tą sygnaturą, po prostu ignoruje ten parametr.


Weźmy przypadek NFT za pośrednictwem RGB21 Interface. Na przykład, możemy mieć :


```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Tutaj widzimy :




- `RGB:`**: Prefiks URL ;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: Contract ID (NFT) ;
- rGB21**: Interface dla aktywów niewymienialnych (NFT) ;
- `DbwzvSu-4BZU81jEp-...`**: wyraźne odniesienie do unikalnej części NFT, na przykład Hash bloku danych (media, metadane...);
- `+utxob:egXsFnw-...`**: Seal Definition.


Idea jest taka sama: przesłać unikalne łącze, które Wallet może zinterpretować, wyraźnie identyfikując unikalny zasób, który ma zostać przeniesiony.


#### Inne operacje za pośrednictwem adresu URL


Adresy URL RGB są używane nie tylko do żądania transferu. Mogą również kodować bardziej zaawansowane operacje, takie jak wydawanie nowych tokenów (*issuance*). Na przykład:


```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```


Tutaj znajdujemy :




- `RGB:` : protokół ;
- `2WBcas9-...`: Contract ID ;
- `/RGB20/issue/100000`: wskazuje, że chcesz wywołać przejście "*Issue*", aby utworzyć dodatkowe 100 000 tokenów;
- `+utxob:`: Seal Definition.


Na przykład, Wallet może przeczytać: "Zostałem poproszony o przeprowadzenie operacji `wydania` z `RGB20` Interface, na takim a takim Contract, za 100,000 jednostek, na rzecz takiego a takiego Single-Use Seal.*"


Teraz, gdy przyjrzeliśmy się głównemu Elements programowania RGB, przeprowadzę cię przez następny rozdział, jak sporządzić RGB Contract.


## Tworzenie inteligentnych kontraktów


<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>


:::video id=a3ad6dcd-90b8-4272-9dfc-76c85c859167:::


W tym rozdziale podejdziemy krok po kroku do pisania Contract, używając narzędzia wiersza poleceń `RGB`. Celem jest pokazanie, jak zainstalować i manipulować CLI, skompilować **Schema**, zaimportować **Interface** i **Interface Implementation**, a następnie wydać (*wydać*) zasób. Przyjrzymy się również podstawowej logice, w tym kompilacji i walidacji stanu. Pod koniec tego rozdziału powinieneś być w stanie odtworzyć ten proces i stworzyć własne kontrakty RGB.


Przypominamy, że wewnętrzna logika RGB opiera się na bibliotekach Rust, które deweloperzy mogą importować do swoich projektów w celu zarządzania częścią Client-side Validation. Ponadto zespół LNP/BP Association pracuje nad powiązaniami dla innych języków, ale nie zostało to jeszcze sfinalizowane. Ponadto inne podmioty, takie jak Bitfinex, opracowują własne stosy integracyjne (omówimy je w ostatnich 2 rozdziałach kursu). W związku z tym na razie oficjalnym punktem odniesienia jest `RGB` CLI, nawet jeśli pozostaje on stosunkowo nieoszlifowany.


### Instalacja i prezentacja narzędzia RGB


Główne polecenie nazywa się po prostu `RGB`. Została zaprojektowana tak, by przypominać `git`, z zestawem podkomend do manipulowania kontraktami, wywoływania ich, wydawania zasobów i tak dalej. Bitcoin Wallet nie jest obecnie zintegrowany, ale będzie w nadchodzącej wersji (0.11). Ta następna wersja umożliwi użytkownikom tworzenie i zarządzanie portfelami (za pośrednictwem deskryptorów) bezpośrednio z RGB, w tym generowanie PSBT, kompatybilność z zewnętrznym sprzętem (np. Hardware Wallet) do podpisywania oraz interoperacyjność z oprogramowaniem takim jak Sparrow. Uprości to cały scenariusz wydawania i przesyłania zasobów.


#### Instalacja za pośrednictwem Cargo


Instalujemy narzędzie w Rust za pomocą :


```bash
cargo install rgb-contracts --all-features
```


(Uwaga: skrzynka nazywa się `RGB-contracts`, a zainstalowane polecenie będzie nosiło nazwę `RGB`. Jeśli skrzynka o nazwie `RGB` już istniała, mogło dojść do kolizji, stąd nazwa)


Instalacja kompiluje dużą liczbę zależności (np. parsowanie poleceń, integracja Electrum, zarządzanie dowodami wiedzy zerowej itp.)


Po zakończeniu instalacji aplikacja :


```bash
rgb
```


Uruchomienie `RGB` (bez argumentów) wyświetla listę dostępnych podkomend, takich jak `interfaces`, `Schema`, `import`, `export`, `issue`, `Invoice`, `transfer`, itd. Możesz zmienić lokalny katalog przechowywania (Stash, który przechowuje wszystkie logi, schematy i implementacje), wybrać sieć (Testnet, Mainnet) lub skonfigurować serwer Electrum.


![RGB-Bitcoin](assets/fr/081.webp)


#### Pierwszy przegląd elementów sterujących


Po uruchomieniu poniższego polecenia zobaczysz, że Interface `RGB20` jest już domyślnie zintegrowany:


```bash
rgb interfaces
```


Jeśli Interface nie jest zintegrowany, sklonuj :


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


![RGB-Bitcoin](assets/fr/082.webp)


Z drugiej strony, powiedziano nam, że żaden Schema nie został jeszcze zaimportowany do oprogramowania. Nie ma też Contract w Stash. Aby to sprawdzić, należy uruchomić polecenie :


```bash
rgb schemata
```


Następnie można sklonować repozytorium, aby pobrać określone schematy:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-Bitcoin](assets/fr/083.webp)


To repozytorium zawiera, w katalogu `src/`, kilka plików Rust (na przykład `nia.rs`), które definiują schematy (NIA dla "*Non Inflatable Asset*", UDA dla "*Unique Digital Asset*", itp.) Aby skompilować, można następnie uruchomić :


```bash
cd rgb-schemata
cargo run
```


Spowoduje to wygenerowanie kilku plików `.RGB` i `.rgba` odpowiadających skompilowanym schematom. Na przykład, znajdziesz `NonInflatableAsset.RGB`.


#### Importowanie Schema i Interface Implementation


Możesz teraz zaimportować schemat do `RGB`:


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-Bitcoin](assets/fr/084.webp)


Spowoduje to dodanie go do lokalnego Stash. Jeśli uruchomimy następujące polecenie, zobaczymy, że Schema jest teraz wyświetlany:


```bash
rgb schemata
```


### Utworzenie Contract (emisja)


Istnieją dwa podejścia do tworzenia nowego zasobu:




- Używamy skryptu lub kodu w Rust, który tworzy Contract poprzez wypełnienie pól Schema (Global State, Owned States, itp.) i tworzy plik `.RGB` lub `.rgba`;
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


![RGB-Bitcoin](assets/fr/085.webp)


Następnie wystarczy uruchomić polecenie :


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-Bitcoin](assets/fr/086.webp)


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


![RGB-Bitcoin](assets/fr/087.webp)


Następnie kolejne polecenie wyświetla globalne stany (nazwa, ticker, Supply...) oraz listę Owned States, czyli alokacji (na przykład 1 milion tokenów `PBN` zdefiniowanych w UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).


```bash
rgb state '<ContractId>'
```


![RGB-Bitcoin](assets/fr/088.webp)


### Eksport, import i walidacja


Aby udostępnić Contract innym użytkownikom, można go wyeksportować z Stash do pliku :


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-Bitcoin](assets/fr/089.webp)


Plik `myContractPBN.RGB` może zostać przekazany innemu użytkownikowi, który może dodać go do swojego Stash za pomocą komendy :


```bash
rgb import myContractPBN.rgb
```


Podczas importu, jeśli jest to prosty * Contract Consignment*, otrzymamy komunikat "`Importowanie Consignment RGB`". Jeśli jest to większy * State Transition Consignment*, polecenie będzie inne (`RGB accept`).


Aby zapewnić poprawność, można również użyć lokalnej funkcji sprawdzania poprawności. Na przykład, można uruchomić :


```bash
rgb validate myContract.rgb
```


#### Użycie, weryfikacja i wyświetlanie Stash


Dla przypomnienia, Stash jest lokalnym spisem schematów, interfejsów, implementacji i kontraktów (Genesis + przejścia). Każde uruchomienie polecenia "import" powoduje dodanie elementu do Stash. Ten Stash można wyświetlić szczegółowo za pomocą polecenia :


```bash
rgb dump
```


![RGB-Bitcoin](assets/fr/090.webp)


Będzie to generate folder ze szczegółami całego Stash.


### Transfer i PSBT


Aby wykonać transfer, będziesz musiał manipulować lokalnym Bitcoin Wallet, aby zarządzać zobowiązaniami `Tapret` lub `Opret`.


#### generate i Invoice


W większości przypadków interakcja między uczestnikami Contract (np. Alicją i Bobem) odbywa się poprzez generowanie Invoice. Jeśli Alicja chce, aby Bob coś wykonał (transfer tokena, ponowne wydanie, akcja w DAO itp.), Alicja tworzy Invoice szczegółowo opisujący jej instrukcje dla Boba. Mamy więc :




- Alice** (emitent Invoice) ;
- Bob** (który odbiera i wykonuje Invoice).


W przeciwieństwie do innych ekosystemów, RGB Invoice nie ogranicza się do pojęcia płatności. Może zawierać dowolne żądanie związane z Contract: odwołanie klucza, głosowanie, utworzenie grawerunku (*grawerunek*) na NFT itp. Odpowiednia operacja może być opisana w Contract Interface. Odpowiednia operacja może być opisana w Contract Interface.


Poniższe polecenie generuje RGB Invoice:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Z :




- `$Contract`: Identyfikator Contract (*ContractId*) ;
- `$Interface`: używany Interface (np. `RGB20`) ;
- `$ACTION`: nazwa operacji określonej w Interface (dla prostego zamiennego transferu tokenów może to być "Transfer"). Jeśli Interface zapewnia już domyślną akcję, nie trzeba jej tutaj ponownie wprowadzać;
- `$STATE`: dane statusu, które mają zostać przesłane (na przykład ilość tokenów, jeśli przesyłany jest token zamienny);
- `$ Seal`: Single-Use Seal beneficjenta (Alicji), tj. wyraźne odniesienie do UTXO. Bob użyje tych informacji do zbudowania Witness Transaction, a odpowiednie dane wyjściowe będą następnie należeć do Alicji (w * blinded UTXO* lub niezaszyfrowanej formie).


Na przykład za pomocą następujących poleceń


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI będzie podobny do generate i Invoice:


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Może on zostać przesłany do Boba dowolnym kanałem (tekst, kod QR itp.).


#### Dokonywanie przelewu


Aby przenieść z tego Invoice :




- Bob (który posiada tokeny w swoim Stash) ma Bitcoin Wallet. Musi przygotować transakcję Bitcoin (w formie PSBT, np. `tx.PSBT`), która wydaje UTXO, gdzie znajdują się wymagane tokeny RGB, plus jeden UTXO na walutę (Exchange);
- Bob wykonuje następujące polecenie:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Spowoduje to wygenerowanie pliku `Consignment.RGB`, który zawiera :
 - Historia przejścia udowadnia Alice, że tokeny są autentyczne;
 - Nowe przejście, które przenosi tokeny do Single-Use Seal Alice;
 - Witness Transaction (niepodpisany).
- Bob wysyła ten plik `Consignment.RGB` do Alicji (przez e-mail, serwer udostępniania lub protokół RGB-RPC, Storm itp;)
- Alice otrzymuje `Consignment.RGB` i akceptuje go w swoim własnym Stash:


```bash
alice$ rgb accept consignment.rgb
```




- CLI sprawdza ważność przejścia i dodaje je do Stash Alice. Jeśli jest nieprawidłowe, polecenie kończy się niepowodzeniem ze szczegółowymi komunikatami o błędach. W przeciwnym razie kończy się sukcesem i informuje, że przykładowa transakcja nie została jeszcze rozesłana w sieci Bitcoin (Bob czeka na kontrolkę Green Alicji);
- Jako potwierdzenie, polecenie `accept` zwraca podpis (*payslip*), który Alice może wysłać do Boba, aby pokazać mu, że zatwierdziła *Consignment*;
- Bob może następnie podpisać i opublikować (`--publish`) swoją transakcję Bitcoin:


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Gdy tylko ta transakcja zostanie potwierdzona On-Chain, Ownership składnika aktywów zostanie uznany za przekazany Alicji. Wallet Alicji, monitorujący Mining transakcji, widzi nowy Owned State pojawiający się w jej Stash.


W następnym rozdziale przyjrzymy się bliżej integracji RGB z Lightning Network.


## RGB na Lightning Network


<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>


:::video id=be25a165-6e23-488c-91d8-3dcfccc6eca1:::


W tym rozdziale proponuję zbadać, w jaki sposób RGB może być wykorzystywany w ramach Lightning Network, w celu integracji i przenoszenia aktywów RGB (tokenów, NFT itp.) za pośrednictwem kanałów płatności off-chain.


Podstawową ideą jest to, że RGB State Transition (*State Transition*) może zostać zatwierdzony do transakcji Bitcoin, która z kolei może pozostać off-chain do momentu zamknięcia kanału Lightning. Tak więc za każdym razem, gdy kanał jest aktualizowany, nowy RGB State Transition może zostać włączony do nowej transakcji zatwierdzającej, która następnie unieważnia stare przejście. W ten sposób kanały Lightning mogą być wykorzystywane do przesyłania aktywów RGB i mogą być kierowane w taki sam sposób, jak konwencjonalne płatności Lightning.


### Tworzenie i finansowanie kanałów


Aby utworzyć kanał Lightning, który przenosi zasoby RGB, potrzebujemy dwóch Elements:




- Finansowanie Bitcoin w celu utworzenia Multisig kanału 2/2 (podstawowy UTXO dla kanału);
- Finansowanie RGB, które wysyła aktywa do tego samego Multisig.


W kategoriach Bitcoin, transakcja finansowania musi istnieć, aby zdefiniować referencyjny UTXO, nawet jeśli zawiera tylko niewielką ilość Sats (to tylko kwestia tego, że każda produkcja w przyszłych transakcjach Commitment pozostanie powyżej limitu Dust). Na przykład Alice może zdecydować się na dostarczenie 10 tys. Sats i 500 USDT (wydanych jako aktywa RGB). W transakcji finansowania dodajemy Commitment (`Opret` lub `Tapret`), który zakotwicza RGB State Transition.


![RGB-Bitcoin](assets/fr/091.webp)


Gdy transakcja finansowania zostanie przygotowana (ale jeszcze nie wyemitowana), tworzone są transakcje Commitment, aby każda ze stron mogła jednostronnie zamknąć kanał w dowolnym momencie. Transakcje te przypominają klasyczne transakcje Commitment Lightning, z tym wyjątkiem, że dodajemy dodatkowe wyjście zawierające RGB Anchor (OP_RETURN lub Taproot) powiązane z nowym State Transition.


Następnie RGB State Transition przenosi aktywa z 2/2 Multisig finansowania do wyjść Commitment Transaction. Zaletą tego procesu jest to, że bezpieczeństwo stanu RGB dokładnie odpowiada mechanice karnej Lightning: jeśli Bob nadaje stary stan kanału, Alicja może go ukarać i wydać dane wyjściowe, aby odzyskać zarówno Sats, jak i tokeny RGB. Motywacja jest zatem jeszcze silniejsza niż w kanale Lightning bez aktywów RGB, ponieważ atakujący może stracić nie tylko Sats, ale także aktywa RGB kanału.


Commitment Transaction podpisany przez Alice i wysłany do Boba wyglądałby zatem następująco:


![RGB-Bitcoin](assets/fr/092.webp)


Towarzyszący Commitment Transaction, podpisany przez Boba i wysłany do Alice, będzie wyglądał następująco:


![RGB-Bitcoin](assets/fr/093.webp)


### Aktualizacja kanału


Gdy następuje płatność między dwoma uczestnikami kanału (lub chcą oni zmienić alokację aktywów), tworzą oni nową parę transakcji Commitment. Kwota w Sats na każdym wyjściu może pozostać niezmieniona lub nie, w zależności od implementacji, ponieważ jej główną rolą jest umożliwienie budowy ważnych UTXO. Z drugiej strony, wyjście OP_RETURN (lub Taproot) musi zostać zmodyfikowane, aby zawierało nowe RGB Anchor, reprezentujące nową dystrybucję aktywów w kanale.


Na przykład, jeśli Alicja przeleje 30 USDT do Boba w kanale, nowy State Transition będzie odzwierciedlał saldo 400 USDT dla Alicji i 100 USDT dla Boba. Transakcja zatwierdzenia jest dodawana do (lub modyfikowana przez) OP_RETURN/Taproot Anchor w celu uwzględnienia tego przejścia. Należy zauważyć, że z punktu widzenia RGB dane wejściowe do przejścia pozostają początkowym Multisig (gdzie aktywa On-Chain są faktycznie przydzielane do momentu zamknięcia kanału). Zmieniają się tylko wyniki (alokacje) RGB, w zależności od wybranej redystrybucji.


Commitment Transaction podpisany przez Alice, gotowy do dystrybucji przez Boba:


![RGB-Bitcoin](assets/fr/094.webp)


Commitment Transaction podpisany przez Boba, gotowy do dystrybucji przez Alice:


![RGB-Bitcoin](assets/fr/095.webp)


### Zarządzanie HTLC


W rzeczywistości Lightning Network umożliwia kierowanie płatności przez wiele kanałów przy użyciu HTLC (*Hashed Time-Locked Contracts*). To samo dotyczy RGB: dla każdej płatności w tranzycie przez kanał, wyjście HTLC jest dodawane do transakcji zatwierdzającej, a alokacja RGB jest powiązana z tym HTLC. W ten sposób każdy, kto wyda HTLC (dzięki sekretowi lub po wygaśnięciu blokady czasowej), odzyskuje zarówno Sats, jak i powiązane aktywa RGB. Z drugiej strony, oczywiście trzeba mieć wystarczającą ilość gotówki w postaci zarówno aktywów Sats, jak i RGB.


![RGB-Bitcoin](assets/fr/096.webp)


Działanie RGB na Lightning musi być zatem rozpatrywane równolegle z działaniem samego Lightning Network. Jeśli chcesz zagłębić się w ten temat, gorąco polecam zapoznanie się z tym innym kompleksowym kursem szkoleniowym:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Mapa kodów RGB


Na koniec, przed przejściem do następnej sekcji, chciałbym przedstawić przegląd kodu używanego w RGB. Protokół opiera się na zestawie bibliotek Rust i specyfikacji open source. Oto przegląd głównych repozytoriów i skrzynek:


![RGB-Bitcoin](assets/fr/097.webp)


#### Client-side Validation




- Repozytorium**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Skrzynki** : [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)


Zarządzanie walidacją off-chain i logiką uszczelnień jednorazowych.


#### Deterministyczne zobowiązania Bitcoin (DBC)




- Repozytorium**: [bp-core](https://github.com/BP-WG/bp-core)
- Crate**: [bp-dbc](https://crates.io/crates/bp-dbc)


Zarządzanie deterministycznym kotwiczeniem w transakcjach Bitcoin (Tapret, OP_RETURN itp.).


#### Multi Protocol Commitment (MPC)




- Repozytorium**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Crate** : [commit_verify](https://crates.io/crates/commit_verify)


Wiele kombinacji zaangażowania i integracja z różnymi protokołami.


#### Typy ścisłe i kodowanie ścisłe




- Specyfikacja**: [strona strict-types.org](https://www.strict-types.org/)
- Repozytoria**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Crates** : [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)


Ścisły system typowania i deterministyczna serializacja używane w Client-side Validation.


#### RGB Core




- Repozytorium**: [RGB-core](https://github.com/RGB-WG/RGB-core)
- Crate**: [RGB-core](https://crates.io/crates/RGB-core)


Rdzeń protokołu, który obejmuje główną logikę walidacji RGB.


#### Biblioteka standardowa RGB i Wallet




- Repozytorium**: [RGB-std](https://github.com/RGB-WG/RGB-std)
- Crate** : [RGB-std](https://crates.io/crates/RGB-std)


Standardowe wdrożenia, zarządzanie Stash i Wallet.


#### RGB CLI




- Repozytorium**: [RGB](https://github.com/RGB-WG/RGB)
- Skrzynki**: [RGB-CLI](https://crates.io/crates/RGB-CLI), [RGB-Wallet](https://crates.io/crates/RGB-Wallet)


`RGB` CLI i crate Wallet, do manipulowania kontraktami z linii poleceń.


#### RGB Schema




- Repozytorium**: [RGB-schemata](https://github.com/RGB-WG/RGB-schemata/)


Zawiera przykłady schematów (NIA, UDA itp.) i ich implementacji.


#### AluVM




- Info** : [AluVM.org](https://www.AluVM.org/)
- Repozytoria**: [AluVM-spec](https://github.com/AluVM/AluVM-spec), [alure](https://github.com/AluVM/alure)
- Skrzynki**: [AluVM](https://crates.io/crates/AluVM), [aluasm](https://crates.io/crates/aluasm)


Oparta na rejestrze maszyna wirtualna używana do uruchamiania skryptów walidacyjnych.


#### Protokół Bitcoin - BP




- Repozytoria** : [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-Wallet](https://github.com/BP-WG/bp-Wallet)


Dodatki do obsługi protokołu Bitcoin (transakcje, obejścia itp.).


#### Wszechobecne obliczenia deterministyczne - UBIDECO




- Repozytorium**: [UBIDECO](https://github.com/UBIDECO)


Ekosystem powiązany z deterministycznym rozwojem open-source.


# Opierając się na RGB


<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>


## DIBA i projekt Bitmask


<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>


:::video id=2ec9a181-a8b0-4da2-b7b5-9dfaaaeb10ba:::


Ta ostatnia część kursu opiera się na prezentacjach różnych prelegentów podczas bootcampu RGB. Obejmuje ona referencje i refleksje na temat RGB i jego ekosystemu, a także prezentacje narzędzi i projektów opartych na protokole. Pierwszy rozdział jest moderowany przez Hunter Beast, a kolejne dwa przez Frederico Tenga.


### Od JavaScript do Rust i do ekosystemu Bitcoin


Początkowo Hunter Beast pracował głównie w JavaScript. Potem odkrył **Rust**, którego składnia początkowo wydawała się nieatrakcyjna i frustrująca. Z czasem jednak docenił moc tego języka, kontrolę nad pamięcią (*heap* i *stack*) oraz bezpieczeństwo i wydajność, które się z tym wiążą. Podkreśla, że Rust jest doskonałym poligonem do dogłębnego zrozumienia działania komputera.


Hunter Beast opowiada o swoim doświadczeniu w różnych projektach w ekosystemie *Altcoin*, takich jak Ethereum (z Solidity, TypeScript itp.), a później Filecoin. Wyjaśnia, że początkowo był pod wrażeniem niektórych protokołów, ale ostatecznie poczuł się rozczarowany większością z nich, nie tylko z powodu ich tokenomiki. Potępia wątpliwe zachęty finansowe, inflacyjne tworzenie tokenów, które rozcieńcza inwestorów, oraz potencjalnie wyzyskujący aspekt tych projektów. Ostatecznie przyjął stanowisko **Bitcoin Maximalist**, między innymi dlatego, że niektórzy ludzie otworzyli mu oczy na zdrowsze mechanizmy ekonomiczne Bitcoin i solidność tego systemu.


### Atrakcyjność RGB i budowanie na warstwach


Jego zdaniem tym, co ostatecznie przekonało go o istotności Bitcoin, było odkrycie RGB i koncepcji warstw. Uważa on, że istniejące funkcje na innych blockchainach można odtworzyć na wyższych warstwach, powyżej Bitcoin, bez zmiany podstawowego protokołu.


W lutym 2022 roku dołączył do **DIBA**, aby pracować nad RGB, a w szczególności nad **Bitmask** Wallet. W tym czasie Bitmask był nadal w wersji 0.01 i działał RGB w wersji 0.4, tylko do zarządzania pojedynczymi tokenami. Zauważa, że było to mniej zorientowane na siebie niż obecnie, ponieważ logika była częściowo oparta na serwerze. Od tego czasu architektura ewoluowała w kierunku tego modelu, bardzo cenionego przez bitcoinerów.


### Podstawy protokołu RGB


Protokół **RGB** jest najnowszym i najbardziej zaawansowanym wcieleniem koncepcji _kolorowych monet_, badanej już w latach 2012-2013. W tym czasie kilka zespołów chciało powiązać różne wartości Bitcoin z UTXO, co doprowadziło do wielu rozproszonych implementacji. Ten brak standaryzacji i niski popyt w tamtym czasie uniemożliwiły tym rozwiązaniom zdobycie trwałego przyczółka.


Obecnie RGB wyróżnia się swoją koncepcyjną solidnością i ujednoliconymi specyfikacjami poprzez powiązanie LNP/BP. Zasada opiera się na Client-side Validation. Bitcoin Blockchain przechowuje jedynie zobowiązania kryptograficzne (_commitments_, za pośrednictwem Taproot lub OP_RETURN), podczas gdy większość danych (definicje Contract, historie transferów itp.) jest przechowywana przez zainteresowanych użytkowników. W ten sposób obciążenie pamięci masowej jest rozłożone, a poufność wymiany jest wzmocniona, bez obciążania Blockchain. Podejście to umożliwia tworzenie zasobów zamiennych (**standard RGB20**) lub unikalnych (**standard RGB21**) w ramach modułowej i skalowalnej struktury.


### Funkcja tokena (RGB20) i unikalne zasoby (RGB21)


W **RGB20** definiujemy zamienny token na Bitcoin. Emitent wybiera _dostawę_, _precyzję_ i tworzy _kontrakt_, w którym może następnie dokonywać przelewów. Każdy przelew odnosi się do Bitcoin UTXO, który działa jak *Single-Use Seal*. Ta logika zapewnia, że użytkownik nie będzie w stanie wydać tego samego zasobu dwa razy, ponieważ tylko osoba zdolna do wydania UTXO faktycznie posiada klucz do aktualizacji stanu Contract po stronie klienta.


**RGB21** dotyczy unikalnych zasobów (lub "NFT"). Zasób ma Supply równy 1 i może być powiązany z metadanymi (plik obrazu, audio itp.) opisanymi za pomocą określonego pola. W przeciwieństwie do NFT na publicznych blockchainach, dane i ich identyfikatory MIME mogą pozostać prywatne, dystrybuowane peer-to-peer według uznania właściciela.


### Rozwiązanie Bitmask: Wallet dla RGB


Aby wykorzystać możliwości RGB w praktyce, projekt **DIBA** zaprojektował Wallet o nazwie [Bitmask](https://bitmask.app/). Pomysł polega na dostarczeniu narzędzia opartego na Taproot, dostępnego jako aplikacja internetowa lub rozszerzenie przeglądarki. Bitmask zarządza zarówno zasobami RGB20, jak i RGB21 oraz integruje różne mechanizmy bezpieczeństwa:




- Podstawowy kod jest napisany w Rust, a następnie skompilowany w WebAssembly w celu uruchomienia w środowisku JavaScript (React);
- Klucze są generowane lokalnie, a następnie przechowywane w postaci zaszyfrowanej;
- Dane stanu (Stash) są przechowywane w pamięci, serializowane i szyfrowane za pośrednictwem biblioteki **Carbonado**, która wykonuje kompresję, korekcję błędów, szyfrowanie i weryfikację strumienia przy użyciu Blake3.


Dzięki tej architekturze wszystkie transakcje dotyczące aktywów odbywają się po stronie klienta. Z zewnątrz transakcja Bitcoin to nic innego jak klasyczna transakcja wydatkowa Taproot, co do której nikt nie miałby podejrzeń, że niesie ze sobą również transfer tokenów zamiennych lub NFT. Brak przeciążenia On-Chain (brak publicznie przechowywanych metadanych) gwarantuje pewien stopień dyskrecji i ułatwia oparcie się ewentualnym próbom cenzury.


### Bezpieczeństwo i architektura rozproszona


Ponieważ protokół RGB wymaga od każdego uczestnika zachowania historii transakcji (w celu udowodnienia ważności otrzymywanych przelewów), pojawia się kwestia przechowywania. Bitmask proponuje serializować ten Stash lokalnie, a następnie wysyłać go do kilku serwerów lub chmur (opcjonalnie). Dane pozostają zaszyfrowane przez użytkownika za pośrednictwem **Carbonado**, więc serwer nie może ich odczytać. W przypadku częściowego uszkodzenia, korekcja błędów Layer może odtworzyć zawartość.


Wykorzystanie CRDT (_Conflict-free replicated data type_) umożliwia łączenie różnych wersji Stash w przypadku ich rozbieżności. Każdy może hostować te dane w dowolnym miejscu, ponieważ żaden pojedynczy Full node nie zawiera wszystkich informacji związanych z aktywem. Odzwierciedla to dokładnie filozofię *Client-side Validation*, gdzie każdy właściciel jest odpowiedzialny za przechowywanie dowodów ważności swojego zasobu RGB.


### W kierunku szerszego ekosystemu: rynek, interoperacyjność i nowe funkcje


Firma stojąca za Bitmask nie ogranicza się do prostego rozwoju Wallet. DIBA zamierza opracować :




- **Rynek** wymiany tokenów, w szczególności w formie **RGB21**;
- Kompatybilność z innymi portfelami (takimi jak *Iris Wallet*);
- Techniki łączenia przelewów**, tj. możliwość włączenia kilku kolejnych przelewów RGB do jednej transakcji.


Jednocześnie pracujemy nad **WebBTC** lub **WebLN** (standardy umożliwiające stronom internetowym poproszenie Wallet o podpisanie transakcji Bitcoin lub Lightning), a także nad możliwością "teleburn" wpisów Ordinals (jeśli chcemy repatriować Ordinals do bardziej dyskretnego i elastycznego formatu RGB).


### Wnioski


Cały proces pokazuje, w jaki sposób można wdrożyć ekosystem RGB i udostępnić go użytkownikom końcowym za pomocą solidnych rozwiązań technicznych. Przejście od perspektywy Altcoin do wizji bardziej skoncentrowanej na Bitcoin, w połączeniu z odkryciem *Client-side Validation*, ilustruje dość logiczną ścieżkę: rozumiemy, że możliwe jest wdrożenie różnych funkcjonalności (tokeny zamienne, NFT, inteligentne kontrakty...) bez rozwidlania Blockchain, po prostu poprzez wykorzystanie zobowiązań kryptograficznych w transakcjach Taproot lub OP_RETURN.


**Bitmask** Wallet jest częścią tego podejścia: po stronie Blockchain wszystko, co widzisz, to zwykła transakcja Bitcoin; po stronie użytkownika manipulujesz Interface, gdzie tworzysz, Exchange i przechowujesz wszelkiego rodzaju aktywa off-chain. Model ten wyraźnie oddziela infrastrukturę monetarną (Bitcoin) od logiki emisji i transferu (RGB), zapewniając jednocześnie wysoki poziom poufności i lepszą skalowalność.


## Praca Bitfinex nad RGB


<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>


:::video id=04555813-516f-4eea-9767-7082c2ea6f01:::


W tym rozdziale, opartym na prezentacji Frederico Tengi, przyjrzymy się zestawowi narzędzi i projektów stworzonych przez zespół Bitfinex poświęcony RGB, w celu wspierania powstawania bogatego i zróżnicowanego ekosystemu wokół tego protokołu. Początkowym celem zespołu nie jest wydanie konkretnego produktu komercyjnego, ale raczej dostarczenie bloków konstrukcyjnych oprogramowania, wniesienie wkładu w sam protokół RGB i zaproponowanie konkretnych referencji wdrożeniowych, takich jak mobilny Wallet (*Iris Wallet*) lub węzeł Lightning kompatybilny z RGB.


### Kontekst i cele


Od około 2022 r. zespół Bitfinex RGB koncentruje się na rozwijaniu stosu technologii, który umożliwia efektywne wykorzystanie i testowanie RGB. Wniesiono kilka wkładów:




- Udział w specyfikacjach kodu źródłowego i protokołów, w tym pisanie propozycji ulepszeń, naprawianie błędów itp;
- Narzędzia dla programistów upraszczające integrację RGB z ich aplikacjami;
- Projekt mobilnego Wallet o nazwie [Iris](https://iriswallet.com/) do eksperymentowania i zilustrowania najlepszych praktyk korzystania z RGB ;
- Stworzenie niestandardowego węzła Lightning, zdolnego do zarządzania kanałami z zasobami RGB;
- Wspieranie innych zespołów tworzących rozwiązania na RGB, aby zachęcić do różnorodności i silnego ekosystemu.


Podejście to ma na celu pokrycie całego łańcucha potrzeb: od biblioteki niskiego poziomu (*[RGBlib](https://github.com/RGB-Tools/RGB-lib)*), umożliwiającej implementację Wallet, do aspektu produkcyjnego (węzeł Lightning, Wallet dla Androida itp.).


### Biblioteka RGBlib: uproszczenie tworzenia aplikacji RGB


Ważnym punktem w demokratyzacji tworzenia portfeli i aplikacji RGB jest udostępnienie abstrakcji na tyle prostej, aby programiści nie musieli uczyć się wszystkiego o wewnętrznej logice protokołu. Taki jest właśnie cel **RGBlib**, napisanego w Rust.


RGBlib działa jako pomost między wysoce elastycznymi (ale czasami złożonymi) wymaganiami RGB, które mogliśmy przeanalizować w poprzednich rozdziałach, a konkretnymi potrzebami twórcy aplikacji. Innymi słowy, Wallet (lub usługa), która chce zarządzać transferami tokenów, wydawaniem aktywów, weryfikacją itp., może polegać na RGBlib bez znajomości wszystkich szczegółów kryptograficznych lub każdego konfigurowalnego parametru RGB.


Księgarnia oferuje :




- Funkcje "pod klucz" do wydawania (_wydawania_) aktywów (zamiennych lub nie);
- Możliwość przesyłania (wysyłania/odbierania) aktywów poprzez manipulowanie prostymi obiektami (adresami, kwotami, UTXO itp.);
- Mechanizm przechowywania i ładowania informacji o stanie (*przypisania*) wymagany dla Client-side Validation.


RGBlib opiera się zatem na złożonych pojęciach specyficznych dla RGB (Client-side Validation, kotwice Tapret/Opret), ale hermetyzuje je, dzięki czemu końcowa aplikacja nie musi przeprogramowywać wszystkiego ani podejmować ryzykownych decyzji. Co więcej, RGBlib jest już powiązany w kilku językach (Kotlin i Python), otwierając drzwi do zastosowań wykraczających poza prosty wszechświat Rust.


### Iris Wallet: przykład RGB Wallet na Androida


Aby udowodnić skuteczność RGBlib, zespół Bitfinex opracował **Iris Wallet**, na tym etapie wyłącznie na Androida. Jest to mobilny Wallet, który ilustruje doświadczenie użytkownika podobne do zwykłego Bitcoin Wallet: możesz wydać zasób, wysłać go, odebrać i wyświetlić jego historię, pozostając w modelu samoprzechowywania.


Iris ma wiele interesujących funkcji:


**Korzystanie z serwera Electrum:**


Jak każdy Wallet, Iris musi wiedzieć o potwierdzeniach transakcji na Blockchain. Zamiast osadzać kompletny węzeł, Iris domyślnie korzysta z serwera Electrum utrzymywanego przez zespół Bitfinex. Użytkownicy mogą jednak skonfigurować własny serwer lub inną usługę innej firmy. W ten sposób transakcje Bitcoin mogą być walidowane, a informacje pobierane (indeksowanie) w sposób modułowy.


**Serwer proxy RGB:**


W przeciwieństwie do Bitcoin, RGB wymaga Exchange metadanych off-chain (*przypisania*) między nadawcą a odbiorcą. Aby uprościć ten proces, Iris oferuje rozwiązanie, w którym komunikacja odbywa się za pośrednictwem serwera proxy. Odbierający Wallet generuje *Invoice*, który wspomina, gdzie nadawca powinien wysłać dane *po stronie klienta*. Domyślnie adres URL wskazuje na serwer proxy hostowany przez zespół Bitfinex, ale można go zmienić (lub hostować własny). Pomysł polega na powrocie do znanego doświadczenia użytkownika, w którym odbiorca wyświetla kod QR, a nadawca skanuje ten kod w celu dokonania transakcji, bez żadnych skomplikowanych dodatkowych manipulacji.


**Ciągłe tworzenie kopii zapasowych:**


W kontekście ściśle Bitcoin, kopia zapasowa seed jest ogólnie wystarczająca (chociaż obecnie zalecamy tworzenie kopii zapasowych seed i deskryptorów). W przypadku RGB to nie wystarczy: musisz również zachować lokalną historię (*przypisania*) potwierdzającą, że naprawdę posiadasz zasób RGB. Za każdym razem, gdy otrzymujesz pokwitowanie, urządzenie przechowuje nowe dane, które są niezbędne do późniejszych wydatków. Iris automatycznie zarządza zaszyfrowaną kopią zapasową na Dysku Google użytkownika. Nie wymaga to specjalnego zaufania do Google, ponieważ kopia zapasowa jest zaszyfrowana, a w przyszłości planowane są bardziej niezawodne opcje (takie jak osobisty serwer), aby uniknąć ryzyka cenzury lub usunięcia przez operatora zewnętrznego.


**Inne cechy:**




- Utwórz Faucet, aby szybko testować lub dystrybuować tokeny w celach eksperymentalnych lub promocyjnych;
- System certyfikacji (obecnie scentralizowany) w celu odróżnienia legalnego tokena od fałszywego, kopiującego słynny ticker. W przyszłości certyfikacja ta może stać się bardziej zdecentralizowana (za pośrednictwem DNS lub innych mechanizmów).


Podsumowując, Iris oferuje doświadczenie użytkownika zbliżone do klasycznego Bitcoin Wallet, maskując dodatkową złożoność (zarządzanie Stash, historia *Consignment* itp.) dzięki RGBlib i wykorzystaniu serwera proxy.


### Serwer proxy i wrażenia użytkownika


Serwer proxy wprowadzony powyżej zasługuje na szczegółowe omówienie, ponieważ jest kluczem do płynnego doświadczenia użytkownika. Zamiast ręcznego przesyłania *przesyłek* przez nadawcę do odbiorcy, transakcja RGB odbywa się w tle za pośrednictwem pliku :




- Odbiorca generuje *Invoice* (zawierający między innymi proxy Address);
- Nadawca wysyła (za pośrednictwem żądania HTTP) projekt przejścia (*Consignment*) do serwera proxy;
- Odbiorca pobiera ten projekt, wykonuje walidację *po stronie klienta* lokalnie;
- Następnie odbiorca publikuje, za pośrednictwem proxy, akceptację (lub ewentualnie odrzucenie) State Transition ;
- Nadawca może wyświetlić status walidacji i, jeśli zostanie zaakceptowany, nadać transakcję Bitcoin finalizującą transfer.


W ten sposób Wallet zachowuje się prawie jak normalny Wallet. Użytkownik nie jest świadomy wszystkich etapów pośrednich. Co prawda obecne proxy nie jest szyfrowane ani uwierzytelniane (co pozostawia obawy o poufność i integralność), ale te ulepszenia są możliwe w późniejszych wersjach. Koncepcja proxy pozostaje niezwykle przydatna do odtworzenia doświadczenia "wysyłam kod QR, skanujesz, aby zapłacić".


### Integracja RGB z Lightning Network


Kolejnym kluczowym celem prac zespołu Bitfinex jest zapewnienie kompatybilności Lightning Network z aktywami RGB. Celem jest umożliwienie kanałów Lightning w USDT (lub dowolnym innym tokenie) i korzystanie z tych samych zalet, co Bitcoin na Lightning (niemal natychmiastowe transakcje, routing itp.). Mówiąc konkretnie, wiąże się to z utworzeniem węzła Lightning zmodyfikowanego do :




- Otwórz kanał, umieszczając nie tylko satoshis, ale także jeden lub więcej aktywów RGB w finansowaniu UTXO Multisig ;
- Transakcje generate Lightning Commitment (po stronie Bitcoin), którym towarzyszą odpowiednie przejścia stanu RGB. Za każdym razem, gdy kanał jest aktualizowany, przejście RGB redefiniuje dystrybucję aktywów w wyjściach Lightning;
- Umożliwienie jednostronnego zamknięcia, w którym zasób jest pobierany w wyłącznym UTXO, zgodnie z zasadami Lightning Network (HTLC, blokada czasowa, kara itp.).


Rozwiązanie to, nazwane "**RGB Lightning Node**", wykorzystuje LDK (*Lightning Dev Kit*) jako bazę i dodaje mechanizmy potrzebne do wstrzykiwania tokenów RGB do kanałów. Zobowiązania Lightning zachowują klasyczną strukturę (punktualne wyjścia, timelock...), a dodatkowo Anchor i RGB State Transition (poprzez `Opret` lub `Tapret`). Dla użytkownika otwiera to drogę do kanałów Lightning w stablecoinach lub w dowolnym innym zasobie emitowanym przez RGB.


### Potencjał DEX i wpływ na Bitcoin


Gdy kilka zasobów jest zarządzanych przez Lightning, możliwe staje się wyobrażenie sobie **atomowego Exchange** na pojedynczej ścieżce routingu Lightning, przy użyciu tej samej logiki sekretów i timelocków. Na przykład użytkownik A posiada Bitcoin na jednym kanale Lightning, a użytkownik B posiada USDT RGB na innym kanale Lightning. Mogą zbudować ścieżkę łączącą ich dwa kanały i jednocześnie Exchange BTC za USDT, bez potrzeby zaufania. Jest to nic innego jak **atomowy swap** odbywający się w kilku przeskokach, dzięki czemu zewnętrzni uczestnicy są prawie nieświadomi faktu, że dokonują transakcji, a nie tylko routingu. Takie podejście oferuje :




- Bardzo niskie opóźnienia, ponieważ wszystko pozostaje off-chain na Lightning.
- Najwyższa **prywatność**: nikt nie wie, że to handel, a nie zwykły routing;
- Unikanie frontrunningu, powtarzający się problem dla On-Chain DEX ;
- Niższe koszty (nie płacisz za przestrzeń blokową, tylko za routing Lightning).


Możemy zatem wyobrazić sobie ekosystem, w którym węzły Lightning oferują ceny swapowe (zapewniając płynność). Każdy węzeł, jeśli chce, może odgrywać rolę _market makera_, kupując i sprzedając różne aktywa na Lightning. Ta perspektywa _layer-2_ DEX wzmacnia ideę, że nie jest konieczne Fork lub korzystanie z blockchainów stron trzecich w celu uzyskania zdecentralizowanych giełd aktywów.


Wpływ na Bitcoin może być pozytywny: Infrastruktura Lightning (węzły, kanały i usługi) byłaby pełniej wykorzystywana dzięki wolumenom generowanym przez te *stablecoiny*, instrumenty pochodne i inne tokeny. Sprzedawcy zainteresowani płatnościami USDT na Lightning mechanicznie odkryliby płatności BTC na Lightning (zarządzane przez ten sam stos). Utrzymanie i finansowanie infrastruktury Lightning Network mogłoby również skorzystać na zwielokrotnieniu tych przepływów innych niż BTC, co pośrednio przyniosłoby korzyści użytkownikom Bitcoin.


### Wnioski i zasoby


Zespół Bitfinex zajmujący się RGB ilustruje swoją pracą różnorodność tego, co można zrobić na szczycie protokołu. Z jednej strony mamy RGBlib, bibliotekę ułatwiającą projektowanie portfeli i aplikacji. Z drugiej strony mamy Iris Wallet, praktyczną demonstrację na Androida zgrabnego Interface dla użytkownika końcowego. Wreszcie, integracja RGB z Lightning pokazuje, że kanały stablecoin są możliwe i otwiera drogę do potencjalnego zdecentralizowanego DEX na Lightning.


Podejście to pozostaje w dużej mierze eksperymentalne i nadal ewoluuje: biblioteka RGBlib jest udoskonalana na bieżąco, Iris Wallet otrzymuje regularne ulepszenia, a dedykowany węzeł Lightning nie jest jeszcze głównym klientem Lightning.


Dla tych, którzy chcą dowiedzieć się więcej lub wnieść swój wkład, dostępnych jest kilka zasobów, w tym :




- [Repozytoria narzędzi GitHub RGB](https://github.com/RGB-Tools);
- [Strona informacyjna poświęcona Iris Wallet](https://iriswallet.com/), aby przetestować Wallet na Androidzie.


W następnym rozdziale przyjrzymy się bliżej, jak uruchomić węzeł RGB Lightning.


## RLN - RGB Lightning Node


<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>


:::video id=d1e9753e-6093-4a47-bcdc-da1aebaefffc:::


W tym ostatnim rozdziale Frederico Tenga przeprowadzi Cię krok po kroku przez konfigurację węzła Lightning RGB w środowisku Regtest i pokaże, jak utworzyć na nim tokeny RGB. Uruchamiając dwa oddzielne węzły, dowiesz się również, jak otworzyć kanał Lightning między nimi a zasobami Exchange RGB.


Ten film służy jako samouczek, podobny do tego, co omówiliśmy w poprzednim rozdziale, ale tym razem koncentruje się na Lightning!


Głównym źródłem tego filmu jest repozytorium Github [RGB Lightning Node](https://github.com/RGB-Tools/RGB-lightning-node), które ułatwia uruchomienie tej konfiguracji w Regtest.


### Wdrażanie węzła Lightning zgodnego z RGB


Proces ten obejmuje i wykorzystuje w praktyce wszystkie koncepcje omówione w poprzednich rozdziałach:




- Pomysł, że **UTXO** zablokowany na 2/2 Multisig kanału Lightning może odbierać nie tylko bitcoiny, ale także być Single-Use Seal aktywów RGB (zamiennych lub nie);
- Dodanie, w każdej transakcji zaangażowania Lightning, wyjścia (`Tapret` lub `Opret`) dedykowanego do zakotwiczenia RGB State Transition;
- Powiązana infrastruktura (bitcoind/indexer/proxy) do walidacji transakcji Bitcoin i danych Exchange *po stronie klienta*.


### Przedstawiamy RGB-lightning-node


Projekt **`RGB-lightning-node`** jest Rust daemon opartym na ``Rust-lightning`` (LDK) Fork zmodyfikowanym w celu uwzględnienia istnienia zasobów RGB w kanale. Po otwarciu kanału można określić obecność zasobów, a za każdym razem, gdy stan kanału jest aktualizowany, tworzone jest przejście RGB, odzwierciedlające dystrybucję zasobu w wyjściach Lightning. Umożliwia to :




- Na przykład otwarte kanały Lightning w USDT;
- Przekierować te tokeny przez sieć, pod warunkiem, że ścieżki routingu mają wystarczającą płynność;
- Wykorzystaj logikę kary i blokady czasowej Lightning bez modyfikacji: po prostu Anchor RGB przejście w dodatkowym wyjściu Commitment Transaction.


Kod jest wciąż w fazie alfa: zalecamy używanie go tylko w **regtest** lub na **Testnet**.


### Instalacja węzła


Aby skompilować i zainstalować binarkę `RGB-lightning-node`, zaczynamy od sklonowania repozytorium i jego submodułów, a następnie uruchamiamy :


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RGB-Bitcoin](assets/fr/098.webp)




- Opcja `--recurse-submodules` również klonuje niezbędne urządzenia podrzędne (włączając w to zmodyfikowaną wersję `Rust-lightning`);
- Opcja `--shallow-submodules` ogranicza głębokość klonu, aby przyspieszyć pobieranie, jednocześnie zapewniając dostęp do istotnych commitów.


Z katalogu głównego projektu uruchom następujące polecenie, aby skompilować i zainstalować plik binarny :


```bash
cargo install --locked --debug --path .
```


![RGB-Bitcoin](assets/fr/099.webp)




- `--locked` zapewnia, że wersja zależności jest ściśle przestrzegana;
- `--debug` nie jest obowiązkowe, ale może pomóc ci się skupić (możesz użyć `--release` jeśli wolisz);
- `--path .` mówi `cargo install`, aby zainstalować z bieżącego katalogu.


Po zakończeniu tego polecenia, plik wykonywalny `RGB-lightning-node` będzie dostępny w katalogu `$CARGO_HOME/bin/`. Upewnij się, że ta ścieżka znajduje się w `$PATH`, abyś mógł wywołać polecenie z dowolnego katalogu.


### Wymagania dotyczące wydajności


Aby działać, `RGB-lightning-node` daemon wymaga obecności i konfiguracji :




- Węzeł `bitcoind`**


Każda instancja RLN będzie musiała komunikować się z `bitcoind`, aby nadawać i monitorować transakcje On-Chain. Uwierzytelnianie (login/hasło) i adres URL (host/port) będą musiały być dostarczone do daemon.




- Indeksator** (Electrum lub Esplora)


daemon musi być w stanie wyświetlać i eksplorować transakcje On-Chain, w szczególności w celu znalezienia UTXO, na którym zakotwiczono zasób. Konieczne będzie podanie adresu URL serwera Electrum lub Esplora.




- RGB** proxy


Jak widzieliśmy w poprzednich rozdziałach, **serwer proxy** jest komponentem (opcjonalnym, ale wysoce zalecanym) w celu uproszczenia Exchange *przypisań* między urządzeniami równorzędnymi Lightning. Po raz kolejny należy określić adres URL.


Identyfikatory i adresy URL są wprowadzane po _odblokowaniu_ daemon za pośrednictwem interfejsu API. Więcej na ten temat później.


### Uruchomienie Regtestu


Do prostego użytku służy skrypt `regtest.sh`, który automatycznie uruchamia, za pośrednictwem Dockera, zestaw usług: `bitcoind`, `electrs` (indeksator), `RGB-proxy-server`.


![RGB-Bitcoin](assets/fr/100.webp)


Pozwala to na uruchomienie lokalnego, izolowanego, wstępnie skonfigurowanego środowiska. Tworzy i niszczy kontenery i katalogi danych przy każdym ponownym uruchomieniu. Zaczniemy od uruchomienia środowiska :


```bash
./regtest.sh start
```


Ten skrypt będzie :




- Utwórz katalog `docker/` do przechowywania ;
- Uruchom `bitcoind` w regtest, jak również indeksator `electrs` i `RGB-proxy-server`;
- Poczekaj, aż wszystko będzie gotowe do użycia.


![RGB-Bitcoin](assets/fr/101.webp)


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


![RGB-Bitcoin](assets/fr/102.webp)




- Parametr `--network regtest` wskazuje na użycie konfiguracji regtest;
- `--daemon-listening-port` wskazuje, na którym porcie REST węzeł Lightning będzie nasłuchiwał wywołań API (JSON);
- `--ldk-peer-listening-port` określa, na którym porcie Lightning P2P ma nasłuchiwać;
- `dataldk0/`, `dataldk1/` to ścieżki do katalogów przechowywania (każdy węzeł przechowuje swoje informacje oddzielnie).


Można również uruchamiać polecenia na węzłach RLN z poziomu przeglądarki:


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


Aby węzeł mógł otworzyć kanał, musi najpierw posiadać bitcoiny na Address wygenerowanym za pomocą następującego polecenia (na przykład dla węzła nr 1):


```bash
curl -X POST http://localhost:3001/address
```


W odpowiedzi otrzymasz Address.


![RGB-Bitcoin](assets/fr/103.webp)


Na `bitcoind` Regtest, będziemy wydobywać kilka bitcoinów. Uruchom :


```bash
./regtest.sh mine 101
```


![RGB-Bitcoin](assets/fr/104.webp)


Wyślij środki do węzła Address wygenerowanego powyżej:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RGB-Bitcoin](assets/fr/105.webp)


Następnie wydobądź blok, aby potwierdzić transakcję:


```bash
./regtest.sh mine 1
```


![RGB-Bitcoin](assets/fr/106.webp)


### Uruchomienie Testnet (bez Dockera)


Jeśli chcesz przetestować bardziej realistyczny scenariusz, możesz uruchomić 3 węzły RLN na Testnet zamiast w Regtest, wskazując na usługi publiczne:


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


Można również dostosować Elements poprzez API `init`/`unlock`.


### Wydawanie tokena RGB


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


![RGB-Bitcoin](assets/fr/107.webp)


Można oczywiście dostosować zamówienie. Aby potwierdzić transakcję, wydobywamy plik :


```bash
./regtest.sh mine 1
```


Możemy teraz utworzyć zasób RGB. Polecenie będzie zależeć od typu zasobu, który chcesz utworzyć i jego parametrów. Tutaj tworzę token NIA (*Non Inflatable Asset*) o nazwie "PBN" z Supply wynoszącym 1000 jednostek. Parametr `precision` pozwala zdefiniować podzielność jednostek.


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


![RGB-Bitcoin](assets/fr/108.webp)


Odpowiedź zawiera identyfikator nowo utworzonego zasobu. Pamiętaj, aby zanotować ten identyfikator. W moim przypadku jest to :


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RGB-Bitcoin](assets/fr/109.webp)


Następnie można przesłać On-Chain lub przydzielić go do kanału Lightning. Dokładnie to zrobimy w następnej sekcji.


### Otwieranie kanału i przesyłanie zasobu RGB


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


![RGB-Bitcoin](assets/fr/110.webp)


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
- `push_msat`: Kwota w milisatoshis początkowo przesłana do peera, gdy kanał jest otwarty (tutaj natychmiast przesyłam 10 000 Sats, aby mógł później wykonać transfer RGB);
- `asset_amount`: Kwota aktywów RGB, która ma zostać przekazana do kanału;
- `asset_id`: Unikalny identyfikator zasobu RGB zaangażowanego w kanał;
- `public`: Wskazuje, czy kanał powinien być publiczny dla routingu w sieci.


![RGB-Bitcoin](assets/fr/111.webp)


Aby potwierdzić transakcję, wydobywanych jest 6 bloków:


```bash
./regtest.sh mine 6
```


![RGB-Bitcoin](assets/fr/112.webp)


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




- `amt_msat`: Invoice ilość w milisatoshis (minimum 3000 Sats) ;
- `expiry_sec` : czas wygaśnięcia Invoice w sekundach ;
- `asset_id`: Identyfikator zasobu RGB powiązanego z Invoice;
- `asset_amount`: Kwota aktywów RGB, która ma zostać przeniesiona z tym Invoice.


W odpowiedzi otrzymasz RGB Invoice (jak opisano w poprzednich rozdziałach):


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RGB-Bitcoin](assets/fr/113.webp)


Teraz zapłacimy Invoice z pierwszego węzła, który posiada niezbędną gotówkę za pomocą tokena `PBN`:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RGB-Bitcoin](assets/fr/114.webp)


Płatność została dokonana. Można to zweryfikować, wykonując polecenie :


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RGB-Bitcoin](assets/fr/115.webp)


Oto jak wdrożyć węzeł Lightning zmodyfikowany do przenoszenia zasobów RGB. Ta demonstracja jest oparta na :




- Środowisko regtest (poprzez `./regtest.sh`) lub Testnet ;
- Węzeł Lightning (`RGB-lightning-node`) oparty na `bitcoind`, indekserze i `RGB-proxy-server`;
- Seria interfejsów API JSON REST do otwierania/zamykania kanałów, wydawania tokenów, przesyłania zasobów za pośrednictwem Lightning itp.


Dzięki temu procesowi:




- Transakcje Lightning Engagement zawierają dodatkowe wyjście (OP_RETURN lub Taproot) z zakotwiczeniem przejścia RGB;
- Przelewy są dokonywane dokładnie w taki sam sposób, jak tradycyjne płatności Lightning, ale z dodatkiem tokena RGB;
- Wiele węzłów RLN można połączyć w celu kierowania i eksperymentowania z płatnościami w wielu węzłach, pod warunkiem, że istnieje wystarczająca płynność zarówno w bitcoinach, jak i aktywach RGB na ścieżce.


Projekt pozostaje w fazie alfa. Dlatego zdecydowanie zaleca się ograniczenie do środowisk testowych (regtest, Testnet).


Możliwości, jakie otwiera ta kompatybilność LN-RGB są znaczne: stablecoiny na Lightning, DEX Layer-2, transfer tokenów zamiennych lub NFT po bardzo niskich kosztach.... W poprzednich rozdziałach przedstawiono architekturę koncepcyjną i logikę walidacji. Teraz masz praktyczny pogląd na to, jak uruchomić taki węzeł na potrzeby przyszłego rozwoju lub testów.


# Sekcja końcowa


<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>


## Recenzje i oceny


<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>


<isCourseReview>true</isCourseReview>

## Wnioski


<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>


<isCourseConclusion>true</isCourseConclusion>