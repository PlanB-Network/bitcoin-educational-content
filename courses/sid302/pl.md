---
name: Liquid Bootcamp Essentials
goal: Uzyskaj kompleksowe zrozumienie projektu Liquid Network i Elements oraz dowiedz się, jak wdrażać zaawansowane rozwiązania w zakresie poufnych transakcji, tokenizacji i zdecentralizowanej architektury sieci.
objectives: 

  - Zrozumienie podstaw architektury Liquid i jej związku z Bitcoin.
  - Naucz się konfigurować i obsługiwać węzły Liquid za pomocą oprogramowania Elements.
  - Zbadanie wykorzystania poufnych transakcji i emisji aktywów na Liquid Network.
  - Zrozumienie biznesowych i technicznych aspektów Liquid dla zastosowań na rynkach kapitałowych.

---

# Wprowadzenie do sieci Liquid


Wyrusz w podróż edukacyjną zaprojektowaną, aby zapewnić dogłębne zrozumienie Liquid Network i projektu Elements. Ten bootcamp łączy teorię i praktykę, aby nauczyć cię technicznych, architektonicznych i biznesowych podstaw niezbędnych do wdrożenia i wykorzystania możliwości Liquid. Od poufnych transakcji po projektowanie ekosystemów, ten kurs jest idealny dla tych, którzy chcą poszerzyć swoją wiedzę na temat zaawansowanych narzędzi w ekosystemie Bitcoin.


Dzięki prezentacjom ekspertów branżowych kurs obejmuje takie tematy, jak architektura Liquid, aplikacje do tokenizacji, koncepcje techniczne Elements i innowacyjne przypadki użycia, takie jak Breez SDK. Zaprojektowany tak, aby był dostępny dla początkujących i średnio zaawansowanych użytkowników, kurs oferuje również wartość dla doświadczonych programistów, którzy chcą opanować Liquid jako platformę do optymalizacji swoich projektów.

+++

# Wprowadzenie


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Przegląd kursu


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Witamy w Liquid Bootcamp, kompleksowym szkoleniu zaprojektowanym w celu wyposażenia w wiedzę i umiejętności pozwalające skutecznie wykorzystać Liquid Network i Elements. Kurs ten oferuje kompleksową eksplorację charakterystycznych cech Liquid, w tym Confidential Transactions, emisji zasobów i architektury sieci federacyjnej, a także wprowadza podstawowe koncepcje Elements, oprogramowania, które zasila Liquid.


Podczas obozu szkoleniowego poznasz praktyczne zastosowania Liquid Network, od konfiguracji i obsługi węzłów po zrozumienie jego wykorzystania na rynkach kapitałowych i tokenizacji Bitcoin. Dzięki prezentacjom ekspertów branżowych uzyskasz również wgląd w zaawansowane tematy, takie jak HTLC, Breez SDK i projekt Blockstream AMP.


Ten bootcamp został pierwotnie przeprowadzony jako wydarzenie osobiste, zgodnie z ustrukturyzowanym harmonogramem (jak pokazano na obrazku) zaprojektowanym dla sesji na żywo. Jednak w przypadku tej adaptacji kursu treść została zreorganizowana, aby lepiej pasowała do formatu online i ułatwiała zrozumienie przez uczniów. Nowa kolejność zapewnia logiczne przejście od podstawowych pojęć do bardziej zaawansowanych i technicznych tematów, maksymalizując w ten sposób doświadczenie edukacyjne.


Ta podróż jest zorganizowana tak, aby pomieścić uczestników o różnym poziomie wiedzy specjalistycznej, oferując połączenie wiedzy teoretycznej i praktycznego doświadczenia. Pod koniec tego obozu będziesz miał solidne zrozumienie architektury Liquid, jego integracji z Bitcoin oraz sposobu wykorzystania jego innowacyjnych funkcji do tworzenia i optymalizacji rozwiązań finansowych.


Zanurz się w świecie łańcucha bocznego Liquid i uwolnij jego pełny potencjał już teraz!

# Podstawy


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Architektura Liquid


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Architektura Liquid Network i model konsensusu


Liquid Network to sfederowany łańcuch boczny zbudowany na bazie kodu Elements, zaprojektowany w celu rozszerzenia możliwości Bitcoin przy jednoczesnym oparciu się na jego podstawowym bezpieczeństwie. W przeciwieństwie do Bitcoin, Proof-of-Work, Liquid działa w oparciu o model Federated Consensus. Sieć jest utrzymywana przez globalnie rozproszoną grupę członków, w tym giełdy, biura handlowe i dostawców infrastruktury. Spośród tych członków wybieranych jest piętnastu "funkcjonariuszy", którzy działają jako sygnatariusze bloków.


Funkcjonariusze ci tworzą bloki w deterministyczny sposób, generując nowy blok co minutę. Ten precyzyjny czas kontrastuje z probabilistycznymi dziesięciominutowymi interwałami Bitcoin. Aby blok był ważny, wymaga podpisów od co najmniej 11 z 15 funkcjonariuszy (próg dwie trzecie plus jeden). Mechanizm ten zapewnia Liquid "ostateczność dwóch bloków", co oznacza, że gdy transakcja uzyska dwa potwierdzenia (około dwóch minut), reorganizacja łańcucha jest matematycznie niemożliwa. Ta szybkość i pewność mają kluczowe znaczenie dla arbitrażu, zautomatyzowanego handlu i szybkiego rozliczenia między giełdami.


Federacja jest dynamiczna. Dzięki protokołowi Dynamic Federation (Dynafed) sieć może zmieniać osoby funkcyjne lub aktualizować parametry bez konieczności stosowania twardego fork. Pozwala to systemowi na płynną ewolucję i wymianę sprzętu lub członków przy jednoczesnym zachowaniu ciągłości działania.


### Confidential Transactions i zarządzanie aktywami


Cechą charakterystyczną Liquid jest natywna obsługa Confidential Transactions (CT) i wielu aktywów. W głównym łańcuchu Bitcoin wszystkie szczegóły transakcji - nadawca, odbiorca i kwota - są publiczne. W Liquid CT wykorzystuje zobowiązania kryptograficzne, aby ukryć typ aktywów i kwotę przed księgą publiczną, jednocześnie umożliwiając sieci weryfikację, czy transakcja jest ważna (tj. nie wystąpiła inflacja). Tylko uczestnicy posiadający klucze zaślepiające mogą zobaczyć konkretne wartości, oferując poziom prywatności handlowej niezbędny dla instytucji przenoszących duże pozycje.


Liquid traktuje wszystkie aktywa jako "natywnych" obywateli łańcucha bloków. Obejmuje to Liquid Bitcoin (LBTC), stablecoiny, takie jak USDT, oraz tokeny zabezpieczające. Emisja aktywów nie wymaga skomplikowanych inteligentnych kontraktów; jest to podstawowa funkcja protokołu.


#### Aktywa regulowane i AMP

W przypadku aktywów wymagających zgodności, takich jak tokeny bezpieczeństwa, Liquid wykorzystuje platformę Blockstream Asset Management Platform (AMP). Wprowadza to warstwę uprawnień, w której transakcje wymagają drugiego podpisu z serwera autoryzacji. Umożliwia to emitentom egzekwowanie zasad - takich jak Whitelisting lub wymagania KYC - na poziomie szczegółowym, łącząc wydajność łańcucha bloków z kontrolą regulacyjną tradycyjnych finansów.


### Dwukierunkowy Peg i infrastruktura bezpieczeństwa


Połączenie między Liquid i Bitcoin jest utrzymywane przez dwukierunkowy peg. Aby "peg-in", użytkownik wysyła Bitcoin na wygenerowany adres na mainchain. Środki te są zablokowane na 102 potwierdzenia (około 17 godzin), aby wyeliminować ryzyko reorganizacji. Po potwierdzeniu równoważna ilość LBTC jest wybijana w łańcuchu bocznym Liquid.


Proces "peg-out" umożliwia użytkownikom wymianę LBTC na Bitcoin. Wymaga to spalenia LBTC i autoryzacji kryptograficznej od federacji. Aby zapobiec kradzieży, peg-out są ściśle kontrolowane przez klucze autoryzacji Peg-out (PAK) posiadane przez członków federacji. Ponadto środki mogą być natychmiastowo wymieniane za pośrednictwem zewnętrznych dostawców, takich jak SideSwap, omijając opóźnienie rozliczenia w celu uzyskania szybszej płynności.


#### Sprzętowe moduły bezpieczeństwa (HSM)

Bezpieczeństwo jest ściśle egzekwowane przez sprzęt. Osoby funkcyjne nie przechowują kluczy prywatnych na standardowych serwerach; zamiast tego obsługują sprzętowe moduły bezpieczeństwa (HSM). Urządzenia te są odseparowane od logiki serwera hosta i są zaprogramowane według ścisłych reguł. Na przykład, HSM odmówi podpisania bloku, jeśli jego wysokość nie jest większa niż poprzednia, zapobiegając przepisywaniu historii. Ten "kontradyktoryjny" model bezpieczeństwa zakłada, że serwer hosta może zostać naruszony, zapewniając, że klucze pozostaną bezpieczne, nawet jeśli fizyczna lokalizacja zostanie naruszona.


## Podstawy Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Fundament Liquid


Elements to platforma blockchain o otwartym kodzie źródłowym wywodząca się z bazy kodu Bitcoin Core. Rozszerza ona funkcjonalność Bitcoin, umożliwiając niezależne od łańcuchów bocznych łańcuchy bloków, które mogą przesyłać aktywa do i z Bitcoin. Podczas gdy Bitcoin Core zasila sieć Bitcoin, Elements jest silnikiem oprogramowania stojącym za Liquid Network i innymi niestandardowymi łańcuchami bocznymi.


Zależność jest prosta: Liquid jest specyficzną "instancją" łańcucha bocznego Elements, skonfigurowaną do użytku produkcyjnego z federacyjnym modelem konsensusu. Programiści zaznajomieni z Bitcoin uznają Elements za intuicyjny, ponieważ zachowuje ten sam interfejs RPC (Remote Procedure Call) i strukturę wiersza poleceń (`elements-cli`, `elements-d`, `elements-qt`). Kluczowa różnica tkwi w konfiguracji: ustawienie `chain=liquidv1` łączy węzeł z główną siecią Liquid, podczas gdy `chain=elementsregtest` uruchamia lokalne środowisko testowania regresji, w którym deweloperzy mogą natychmiast tworzyć bloki generate i testować bez zewnętrznych zależności.


#### Emisja aktywów

Cechą wyróżniającą Elements jest natywna emisja aktywów. W przeciwieństwie do Ethereum, gdzie tokeny są złożonymi inteligentnymi kontraktami, aktywa w Elements są obywatelami pierwszej kategorii tworzonymi za pomocą prostego polecenia RPC (`issueasset`).


- Unikalne identyfikatory:** Każdy zasób otrzymuje unikalny 64-znakowy identyfikator szesnastkowy.
- Tokeny ponownego wydania:** Emitenci mogą opcjonalnie tworzyć tokeny ponownego wydania, które przyznają posiadaczowi prawo do późniejszego wybicia większej ilości aktywów (przydatne w przypadku stablecoinów lub tokenów zabezpieczających).
- Rejestr aktywów:** Ponieważ identyfikatory szesnastkowe nie są czytelne dla człowieka, rejestr aktywów Blockstream mapuje te identyfikatory na nazwy i tickery (np. "USDT"), podobnie jak DNS dla aktywów.


### Prywatność przez Confidential Transactions


Elements rozwiązuje jedno z głównych ograniczeń publicznych łańcuchów bloków: brak prywatności handlowej. Na Bitcoin każda kwota transakcji jest widoczna dla całego świata. Elements wprowadza **Confidential Transactions (CT)**, który kryptograficznie ukrywa kwotę i rodzaj aktywów, jednocześnie umożliwiając sieci weryfikację ważności transakcji.


Osiąga się to za pomocą **Pedersen Commitments** i **Range Proofs**.


- Zobowiązania Pedersena** zastępują widoczną kwotę zobowiązaniem kryptograficznym. Ze względu na homomorficzne szyfrowanie, walidatorzy mogą sprawdzić, czy *Input Commitments = Output Commitments + Fees* bez zobaczenia rzeczywistych wartości.
- Range Proofs** uniemożliwiają użytkownikowi tworzenie pieniędzy z powietrza (np. przy użyciu liczb ujemnych) poprzez matematyczne udowodnienie, że ukryta wartość jest dodatnią liczbą całkowitą w prawidłowym zakresie.


Dla zewnętrznego obserwatora Transakcja Poufna pokazuje prawidłowe dane wejściowe i wyjściowe, ale ukrywa *co* jest wysyłane i *jak dużo*. Tylko nadawca i odbiorca (którzy posiadają klucze zaślepiające) mogą przeglądać dane w postaci czystego tekstu.


### Rozwój i przepływ pracy RPC


Interakcja z węzłem Elements odbywa się głównie za pośrednictwem interfejsu JSON-RPC. Pozwala to aplikacjom napisanym w Pythonie, JavaScript lub Go na komunikację z blockchainem.



- Konfiguracja:** Deweloper zazwyczaj rozpoczyna pracę w trybie `regtest`. Pozwala to na natychmiastowe generowanie bloków (`generateblock`) w celu natychmiastowego potwierdzenia transakcji, z pominięciem 1-minutowego czasu bloku w sieci na żywo.
- Komendy:** Dostępne są standardowe komendy Bitcoin, takie jak `getblockchaininfo`, wraz z komendami specyficznymi dla Elements, takimi jak `dumpblindingkey` (do audytu CT) lub `pegin` (do przenoszenia BTC do łańcucha bocznego).
- Aby zarządzać wieloma węzłami (np. "nadawcą" i "odbiorcą" do testowania), programiści często używają aliasów powłoki, takich jak `e1-cli` i `e2-cli` wskazujących na różne katalogi danych, symulując sieć peer-to-peer na jednej maszynie.


Architektura ta umożliwia programistom tworzenie zaawansowanych aplikacji finansowych - takich jak platformy papierów wartościowych lub prywatne bramki płatnicze - przy użyciu solidnych i znanych narzędzi ekosystemu Bitcoin.


## Łączenie warstw Bitcoin


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Infrastruktura Cross-Layer i sterowniki HTLC


Ekosystem Bitcoin przekształcił się w wielowarstwową architekturę, w której Mainchain zapewnia rozliczenia, Lightning oferuje szybkość, a Liquid umożliwia zaawansowane możliwości aktywów. Przenoszenie wartości między tymi warstwami bez scentralizowanych pośredników wymaga niezaufanego prymitywu kryptograficznego: Hash Time Locked Contract (HTLC).


HTLC tworzy warunkowy kanał płatności, który atomowo łączy niezależne systemy. Działa poprzez dwa podstawowe ograniczenia: **hash lock** i **time lock**.


- Blokada Hash:** Środki można wydać natychmiast, jeśli odbiorca ujawni tajny "obraz wstępny", który pasuje do określonego skrótu kryptograficznego.
- Blokada czasowa:** Jeśli odbiorca nie ujawni sekretu w określonym czasie (wysokość bloku), pierwotny nadawca może odzyskać środki.


Ta dwuścieżkowa struktura zapewnia bezpieczeństwo. W wymianie międzywarstwowej ta sama blokada hash jest używana w obu sieciach. Gdy odbiorca ujawnia sekret, aby zażądać środków na jednej warstwie (np. Liquid), sekret ten staje się widoczny dla nadawcy, który może następnie użyć go do żądania wzajemnych środków na drugiej warstwie (np. Lightning). To kryptograficzne powiązanie gwarantuje, że wymiana zakończy się sukcesem dla obu stron lub zakończy się niepowodzeniem dla obu stron, eliminując ryzyko utraty środków przez jedną stronę, podczas gdy druga je zyskuje.


### Aktualizacja Taproot i MuSig2


Starsze HTLC (SegWit v0) działały dobrze, ale miały wady związane z prywatnością i wydajnością. Wymagały one opublikowania całej logiki skryptu on-chain, dzięki czemu transakcje swap były łatwe do zidentyfikowania dla analityków blockchain i droższe ze względu na rozmiar danych. Wprowadzenie Taproot (SegWit v1) i protokołu MuSig2 zrewolucjonizowało tę architekturę.


Taproot pozwala na **Key Aggregation** poprzez MuSig2. Zamiast ujawniać złożony skrypt z wieloma kluczami publicznymi, MuSig2 pozwala uczestnikom wymiany połączyć swoje klucze w jeden zagregowany klucz publiczny.


- Współpracująca "ścieżka klucza":** Jeśli obie strony zgadzają się na wymianę ("szczęśliwa ścieżka"), podpisują transakcję. Dla sieci wygląda to identycznie jak standardowa płatność z jednym podpisem. Zużywa minimalną przestrzeń blokową i nie ujawnia absolutnie żadnych informacji o warunkach wymiany.
- "Ścieżka skryptu" adwersarza:** Jeśli jedna ze stron przestanie reagować lub stanie się złośliwa, podstawowy skrypt (zawierający hash / blokady czasowe) jest ujawniany tylko wtedy. Jest on zorganizowany w drzewo Merkle'a, dzięki czemu uczciwa strona może ujawnić tylko określoną gałąź potrzebną do odzyskania środków, utrzymując resztę logiki kontraktu w ukryciu.


### Praktyczne zastosowanie: Liquid-Lightning Swaps


W praktyce protokoły te umożliwiają płynną wymianę między warstwami Bitcoin. Typowa wymiana Liquid na Lightning rozpoczyna się od żądania wymiany przez klienta od dostawcy usług. Klient dostarcza fakturę Lightning, a dostawca blokuje ekwiwalent Liquid Bitcoin (L-BTC) na adres HTLC z obsługą Taproot.


Atomowość jest egzekwowana, gdy płatność zostanie rozliczona. Aby ubiegać się o L-BTC, usługodawca musi mieć obraz wstępny. Otrzymuje go tylko wtedy, gdy pomyślnie opłaci fakturę Lightning klienta. W momencie sfinalizowania płatności Lightning obraz wstępny zostaje ujawniony, umożliwiając dostawcy odblokowanie środków Liquid.


#### Abstrakcja Wallet i zarządzanie UTXO

Dla użytkowników końcowych ta złożoność jest całkowicie abstrakcyjna. Nowoczesne portfele, takie jak Aqua, obsługują procesy generowania kluczy, tworzenia faktur i podpisywania w tle. Użytkownik po prostu "płaci" fakturę Lightning przy użyciu swojego salda Liquid. Za kulisami usługa zarządza konsolidacją UTXO, okresowo zamiatając małe, nieodebrane lub zwrócone dane wyjściowe, aby utrzymać wydajność wallet i zminimalizować wpływ opłat w okresach dużego ruchu.


## Przegląd Liquid Network


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Architektura i konsensus Liquid Network


Liquid Network działa jako federacyjny łańcuch boczny zbudowany na bazie kodu **Elements**. Podczas gdy Elements - fork rdzenia Bitcoin - zapewnia podstawę oprogramowania, Liquid jest implementacją sieci produkcyjnej. W przeciwieństwie do Bitcoin Proof-of-Work, który opiera się na konkurencyjnym mining, Liquid wykorzystuje model **Federated Consensus**.


Sieć jest utrzymywana przez piętnastu globalnie rozproszonych "funkcjonariuszy" Podmioty te obsługują wyspecjalizowane serwery, które pełnią dwie krytyczne role:

1.  **Produkcja bloków:** Osoby funkcyjne na zmianę tworzą bloki w deterministycznym harmonogramie round-robin, generując nowy blok dokładnie co minutę.

2.  **Podpisywanie bloków:** Aby blok był ważny, musi zostać podpisany przez co najmniej 11 z 15 osób funkcyjnych.


Ten próg 11 z 15 zapewnia, że sieć może tolerować awarię do czterech węzłów bez zatrzymania. Główną zaletą tego kompromisu jest **deterministyczny finał**. Podczas gdy Bitcoin zajmuje się prawdopodobieństwem, Liquid osiąga pewność rozliczenia po dwóch blokach (około dwóch minut). Gdy blok ma jedno potwierdzenie, łańcuch nie może zostać zreorganizowany, co czyni go wysoce skutecznym w arbitrażu i szybkim rozliczaniu.


### Confidential Transactions i rodzime aktywa


Cechą charakterystyczną Liquid jest domyślne użycie **Confidential Transactions (CT)**. W Bitcoin mainchain nadawca, odbiorca i kwota są jawne. Liquid poprawia to, kryptograficznie zaślepiając kwotę i typ aktywów, pozostawiając adresy nadawcy i odbiorcy widoczne do weryfikacji.


Aby zapewnić, że użytkownik nie może wydrukować pieniędzy (np. wysyłając ujemne kwoty), Liquid wykorzystuje **Pedersen Commitments** i **Range Proofs**. Te prymitywy kryptograficzne pozwalają sieci zweryfikować, że *wejścia = wyjścia + opłaty* i że wszystkie wartości są dodatnimi liczbami całkowitymi, bez ujawniania konkretnych liczb w księdze publicznej. Tylko uczestnicy posiadający klucze oślepiające mogą przeglądać odszyfrowane dane.


#### Emisja aktywów

Liquid traktuje wszystkie aktywa jako "natywne" Niezależnie od tego, czy jest to Liquid Bitcoin (L-BTC), stablecoin taki jak USDT, czy papier wartościowy token, wszystkie mają tę samą architekturę. Emisja aktywów nie wymaga żadnych inteligentnych kontraktów - tylko prostego wywołania RPC.


- Nieuregulowane aktywa:** Mogą być emitowane bez pozwolenia przez każdego.
- Aktywa regulowane:** Korzystając z platformy Blockstream Asset Management Platform (AMP), emitenci mogą egzekwować zasady zgodności (takie jak KYC/AML), wymagając drugiego podpisu z serwera autoryzacji przed przeniesieniem aktywów.


### Dwukierunkowy kołek i dynamiczna federacja


Pomostem między Bitcoin i Liquid jest **Two-Way Peg**. Umożliwia on użytkownikom przenoszenie BTC na łańcuch boczny (Peg-in) i z powrotem do mainchain (Peg-out).


**Proces Peg-in:**

Odbywa się to bez zezwoleń. Użytkownik wysyła BTC na adres kontrolowany przez federację. Aby zabezpieczyć się przed reorganizacją blockchaina Bitcoin, środki te muszą poczekać na **102 potwierdzenia** (około 17 godzin), zanim odpowiednik L-BTC zostanie wybity w łańcuchu bocznym.


**Proces Peg-out:**

Aby powrócić do Bitcoin, L-BTC jest spalany. Jednak, aby zapobiec kradzieży podstawowych rezerw Bitcoin, peg-out nie jest w pełni zautomatyzowany. Wymagają one autoryzacji od członka posiadającego **Peg-Out Authorization Key (PAK)**. Same fundusze Bitcoin są zabezpieczone w wielopodpisowym wallet 11 z 15, z kluczami przechowywanymi w sprzętowych modułach bezpieczeństwa (HSM), które są hermetyzowane z głównych serwerów funkcjonariuszy.


**Dynamic Federation (Dynafed):**

Aby zapewnić długowieczność, Liquid wykorzystuje Dynafed, protokół, który pozwala sieci na rotację funkcjonariuszy lub aktualizację parametrów bez twardego fork. Jeśli osoba funkcyjna musi zostać zastąpiona, sieć transmituje transakcję przejścia. Po dwutygodniowym okresie nakładania się nowa konfiguracja zostaje przejęta, umożliwiając federacji płynną ewolucję przy jednoczesnym utrzymaniu ciągłego czasu pracy.


## Ekosystem i rynki kapitałowe


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Strategia biznesowa i ekosystem


Liquid to coś więcej niż techniczny łańcuch boczny; jest to warstwa infrastruktury skoncentrowana na biznesie, zaprojektowana do obsługi złożonych wymagań rynków kapitałowych, których Bitcoin mainchain nie może skutecznie obsługiwać. Podczas gdy Lightning Network optymalizuje płatności o wysokiej częstotliwości i niskiej wartości, Liquid jest ukierunkowany na transfery o wysokiej wartości, emisję aktywów i rozliczenia między giełdami.


Ekosystem jest napędzany przez **Liquid Federation**, konsorcjum ~73 firm, w tym giełd, biur handlowych i dostawców infrastruktury. Ten model współpracy odzwierciedla tradycyjne finansowe izby rozliczeniowe, ale działa z większą przejrzystością i znacznie krótszym czasem rozliczenia (2 minuty w porównaniu do T + 2 dni).


### Tokenizacja aktywów świata rzeczywistego (RWA)


Podstawowym uzasadnieniem biznesowym dla Liquid jest "tokenizacja" - reprezentowanie rzeczywistej wartości (akcje, obligacje, kontrakty mining) jako cyfrowych tokenów w łańcuchu bloków. Oferuje to trzy podstawowe korzyści:

1.  **Globalne rynki 24/7:** Usunięcie godzin pracy i ograniczeń geograficznych.

2.  **Efektywność operacyjna:** Eliminacja błędów uzgodnień dzięki współdzielonej, niezmiennej księdze.

3.  **Rozliczenie atomowe:** Zmniejszenie ryzyka kontrahenta poprzez zapewnienie, że dostawa następuje jednocześnie z płatnością.


#### Aktywa regulowane i AMP

Większość aktywów instytucjonalnych nie może handlować bez zezwoleń ze względu na wymogi prawne. Platforma **Asset Management Platform (AMP)** jest standardem technicznym, który egzekwuje te zasady.


- Biała lista:** Emitenci mogą ograniczyć posiadanie i handel do adresów zweryfikowanych przez KYC.
- Kontrola Multisig:** Działania związane ze zgodnością (takie jak zamrażanie skradzionych środków lub ponowne wydawanie utraconych tokenów) są zarządzane za pomocą autoryzacji wielopodpisowej, dzięki czemu żaden pracownik nie może działać jednostronnie.


Infrastruktura ta działa już dziś. Platformy takie jak **Stalker** świadczą kompleksowe usługi tokenizacji w Europie, podczas gdy **Sideswap** działa jako zdecentralizowana giełda i nieuwierzytelniony wallet, umożliwiając handel peer-to-peer aktywami, takimi jak **Blockstream Mining Note (BMN)** i tokenizowane akcje MicroStrategy (CMSTR).


### Sukces w świecie rzeczywistym: Studium przypadku Mayfell


Najbardziej przekonujący dowód użyteczności Liquid pochodzi od **Mayfell** w Meksyku. Na rynku, na którym tradycyjne finansowanie opiera się na papierowych wekslach - które są podatne na straty, oszustwa i powolne przetwarzanie - Mayfell przeniósł całą infrastrukturę na Liquid.



- Skala:** Ponad 25 000 wystawionych weksli o wartości ponad **1,5 mld USD**.
- Prywatność:** Korzystając z Liquid's Confidential Transactions, kwoty pożyczek są widoczne tylko dla pożyczkodawcy i pożyczkobiorcy, zachowując prywatność handlową, jednocześnie umożliwiając audytorom weryfikację integralności księgi.
- Wpływ:** Łącząc niebankowych pożyczkodawców z globalnymi rynkami kapitałowymi za pośrednictwem blockchain, Mayfell obniżył koszty i rozszerzył dostęp do kredytów dla meksykańskich MŚP, pokazując, że propozycja wartości Liquid wykracza daleko poza handel spekulacyjny.


### Pozycjonowanie strategiczne na tle innych sieci


Liquid konkuruje na zatłoczonym rynku platform tokenizacyjnych (Ethereum, Solana itp.), ale ma wyraźną przewagę strategiczną:


- Przejrzystość regulacyjna:** Liquid wykorzystuje Bitcoin (L-BTC) jako swoje natywne aktywo. Nie ma wstępnie wydobytego token ani ICO, unikając ryzyka "niezarejestrowanego zabezpieczenia", które nęka inne łańcuchy bloków L1.
- Stabilność:** W przeciwieństwie do modelu konta Ethereum, w którym nieudane transakcje nadal generują opłaty za gaz, model Liquid UTXO jest deterministyczny i niezawodny w przypadku krytycznych danych finansowych.
- Prywatność:** Domyślna poufność jest wymogiem dla większości instytucji finansowych, a funkcja Liquid oferuje ją natywnie, co publiczne sieci mają trudności z wdrożeniem bez skomplikowanych dodatków.


Dla deweloperów ten ekosystem oferuje wyraźną szansę: tworzenie narzędzi (pulpitów nawigacyjnych, portfeli, integracji zgodności), które łączą tradycyjne finanse z bezpieczną warstwą rozliczeniową Bitcoin.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Dozwolona kontrola aktywów na Liquid


Blockstream AMP (Asset Management Platform) służy jako krytyczna warstwa infrastruktury na Liquid Network, zaprojektowana specjalnie dla emitentów regulowanych cyfrowych papierów wartościowych i stablecoinów. Podczas gdy Liquid zapewnia warstwę bazową bez zezwoleń z natywną emisją aktywów, podmioty regulowane często wymagają ścisłego nadzoru i możliwości zapewnienia zgodności. AMP wypełnia tę lukę, wprowadzając dozwoloną warstwę kontroli nad określonymi aktywami bez poświęcania korzyści w zakresie prywatności Liquid Confidential Transactions.


Podstawowa propozycja wartości platformy opiera się na dwóch podstawowych funkcjach: kompleksowej widoczności emitenta i autoryzacji transakcji. W przeciwieństwie do standardowych aktywów Liquid, w których kwoty i typy są blinded dla wszystkich oprócz uczestników, aktywa AMP pozwalają emitentowi na utrzymanie pełnej ścieżki audytu unblinded. Ta przejrzystość jest niezbędna dla sprawozdawczości regulacyjnej i audytów wewnętrznych. Ponadto AMP egzekwuje ścisły model autoryzacji poprzez mechanizm współpodpisywania. Każdy transfer aktywów AMP wymaga podpisu z serwera AMP. Umożliwia to emitentom egzekwowanie złożonych zasad off-chain - takich jak zamrażanie kont, umieszczanie na białej liście akredytowanych inwestorów lub nakładanie limitów transferu - skutecznie działając jako scentralizowany strażnik w zdecentralizowanej sieci.


#### Kompromisy operacyjne

Architektura ta wprowadza określone kompromisy. System opiera się na dostępności serwera AMP; jeśli serwer działa jako współsygnatariusz i przechodzi w tryb offline, płynność aktywów zostaje wstrzymana. Ponadto, chociaż prywatność między użytkownikami jest zachowana, inwestorzy muszą zaakceptować fakt, że emitent ma pełny wgląd w ich zasoby. Model ten jest idealny dla zgodnych tokenów zabezpieczających, ale nieodpowiedni dla kryptowalut odpornych na cenzurę.


### Ewolucja architektury i ścieżki integracji


Ekosystem AMP przechodzi obecnie od swojej pierwszej iteracji do bardziej elastycznej, interoperacyjnej architektury "wersji 2". Starszy system wymagał od emitentów utrzymywania w pełni zsynchronizowanych węzłów Elements i zmuszał programistów do polegania w dużej mierze na monolitycznym Green SDK. Choć funkcjonalne, stworzyło to wysokie bariery techniczne wejścia na rynek i ograniczyło wybór wallet.


Architektura nowej generacji zasadniczo upraszcza te wymagania, przenosząc złożoność na serwer. W tym nowym modelu serwer AMP zajmuje się konstruowaniem transakcji, wyborem UTXO i obliczaniem opłat. Przedstawia emitentowi częściowo podpisaną transakcję Elements (PSET), która wymaga jedynie podpisu. To podejście "inteligentny serwer, głupi wallet" eliminuje potrzebę uruchamiania przez emitentów pełnych węzłów i umożliwia korzystanie z portfeli sprzętowych i standardowych konfiguracji wielopodpisowych do zarządzania środkami finansowymi.


Dla deweloperów ewolucja ta oznacza odejście od zastrzeżonych zestawów SDK na rzecz standardowych deskryptorów i przepływów pracy PSET. Portfele mogą teraz rejestrować deskryptory z wieloma podpisami na serwerze AMP w celu ustanowienia praw do autoryzacji. Dostosowuje to rozwój AMP do szerszych standardów Bitcoin wallet, dzięki czemu integracja jest dostępna dla każdej aplikacji obsługującej formaty PSBT/PSET. Deweloperzy tworzący obecnie aplikacje są zachęcani do korzystania z narzędzi takich jak Liquid Wallet Kit (LWK), które obsługują te nowoczesne, oparte na deskryptorach architektury, zapewniając, że ich aplikacje są przyszłościowo przystosowane do nowych standardów AMP.


### Ekosystem Liquid Wallet i poufność


Tworzenie aplikacji na Liquid wymaga poruszania się po bardziej złożonym stosie niż standardowy rozwój Bitcoin ze względu na funkcje takie jak zasoby natywne i Confidential Transactions. Ekosystem jest wspierany przez warstwową architekturę: biblioteki niskiego poziomu, takie jak `secp256k1-zkp`, obsługują prymitywy kryptograficzne, podczas gdy zestawy narzędzi wyższego poziomu zarządzają logiką wallet.


W przeszłości Green Development Kit (GDK) zapewniał kompleksowe, ale sztywne rozwiązanie. Nowoczesną alternatywą jest Liquid Wallet Kit (LWK), który oferuje podejście modułowe. LWK dzieli problemy na odrębne skrzynki - niezależnie obsługując deskryptory, podpisywanie i komunikację sprzętową - dając programistom elastyczność w tworzeniu niestandardowych rozwiązań bez narzutu monolitycznej biblioteki.


#### Obsługa Confidential Transactions

Największym wyzwaniem w tym ekosystemie jest zarządzanie cyklem życia zaślepienia. W Liquid dane wyjściowe transakcji są szyfrowane przy użyciu wymiany kluczy Elliptic Curve Diffie-Hellman (ECDH). Nadawca używa klucza publicznego odbiorcy do szyfrowania kwot i typów aktywów, generując dowód zakresu, który weryfikuje ważność transakcji bez ujawniania wartości.


Aby wallet działał, musi pomyślnie odwrócić ten proces. Gdy wallet wykryje przychodzącą transakcję, próbuje odblokować dane wyjściowe za pomocą swojego prywatnego klucza blokującego. Jeśli wspólny klucz tajny pasuje, wallet może odszyfrować wartość i dodać ją do salda użytkownika. Proces ten jest intensywny obliczeniowo i wymaga precyzyjnego zarządzania współczynnikami zaślepienia, aby zapewnić matematyczną równowagę transakcji, co jest złożonością, którą narzędzia takie jak LWK mają na celu abstrahować dla dewelopera.


# Techniczne


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - Nodeless


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Wprowadzenie do Breez Liquid SDK


Breez Liquid SDK to samowystarczalny zestaw narzędzi o otwartym kodzie źródłowym, zaprojektowany w celu wypełnienia luki między Liquid Network a szerszym ekosystemem Bitcoin. Jego główną misją jest abstrahowanie od złożoności zarządzania węzłami Lightning Network i swapów atomowych, umożliwiając programistom tworzenie beztarciowych aplikacji finansowych.


Zbudowana zgodnie z filozofią "mobile-first", podstawowa logika jest napisana w Rust dla wydajności i bezpieczeństwa, ale wykorzystuje UniFFI (Unified Foreign Function Interface), aby zapewnić natywne powiązania dla Kotlin, Swift, Python, C#, Dart i Flutter. Dzięki temu deweloperzy mogą zintegrować funkcjonalność Bitcoin z preferowanym środowiskiem bez konieczności zarządzania niskopoziomowymi operacjami kryptograficznymi.


**Obsługiwane typy transakcji:**

SDK działa z Liquid jako swoją "bazą domową" Wyróżnia się trzema konkretnymi operacjami:

1.  **Liquid-to-Liquid:** Bezpośrednie transfery on-chain.

2.  **Liquid-to-Lightning:** Opłacanie faktur Lightning przy użyciu środków Liquid.

3.  **Liquid-to-Bitcoin:** Zamiana środków bezpośrednio na Bitcoin mainchain.


*Uwaga: SDK nie obsługuje bezpośrednich transakcji Lightning-to-Lightning lub Bitcoin-to-Bitcoin. Jest to narzędzie ściśle skoncentrowane na Liquid


### Architektury płatności: Swapy podmorskie


Aby osiągnąć interoperacyjność między Liquid, Lightning i Bitcoin bez scentralizowanych opiekunów, Breez opiera się na **Submarine Swaps**. Są to operacje atomowe, w których transakcja kończy się pomyślnie w obu sieciach lub kończy się niepowodzeniem w obu sieciach, zapewniając, że środki nigdy nie zostaną utracone w tranzycie.


#### Lightning Send (Zamiana okrętów podwodnych)

Gdy użytkownik płaci fakturę Lightning, zestaw SDK transmituje transakcję "lock-up" na Liquid Network. To skutecznie umieszcza środki w depozycie. Dostawca swapu (Boltz) wykrywa to, opłaca fakturę Lightning, a następnie wykorzystuje obraz wstępny płatności (paragon kryptograficzny), aby zażądać zablokowanych środków Liquid.


#### Lightning Receive (odwrócona zamiana okrętów podwodnych)

Odbieranie Lightning jest procesem odwrotnym. Użytkownik generuje fakturę, a dostawca swapu blokuje środki na Lightning Network. Zestaw SDK monitoruje ten proces za pośrednictwem WebSockets. Po potwierdzeniu blokady zestaw SDK automatycznie wykonuje transakcję roszczenia, aby przenieść równoważne środki do Liquid wallet użytkownika.


#### Cross-Chain Bitcoin

W przypadku transferów Liquid-Bitcoin architektura wykorzystuje mechanizm "podwójnej wymiany". Transakcje lock-up występują jednocześnie w obu łańcuchach. Nadawca żąda środków na Bitcoin, podczas gdy odbiorca żąda środków na Liquid. Umożliwia to bezzaufane pomostowanie bez polegania na wyjściach federated peg lub scentralizowanych wymianach.


### Deweloper Interface i zautomatyzowane zarządzanie


Breez SDK upraszcza doświadczenie dewelopera poprzez skondensowanie złożonych przepływów finansowych w znormalizowany trzyetapowy proces: **Połącz, Przygotuj i Wykonaj**.


1.  **Connect:** Inicjalizuje wallet, synchronizuje się z blockchainem za pomocą Liquid Wallet Kit (LWK) i ustanawia połączenia WebSocket do monitorowania w czasie rzeczywistym.

2.  **Przygotowanie:** Przed przekazaniem środków, ten krok oblicza i zwraca wszystkie powiązane opłaty sieciowe i koszty swapów, umożliwiając interfejsowi użytkownika przedstawienie użytkownikowi jasnej sumy.

3.  **Execute:** Ten krok konstruuje transakcję, rozgłasza ją i inicjuje wymianę.


#### Zautomatyzowane mechanizmy bezpieczeństwa

Jedną z najważniejszych funkcji SDK jest **Automated Refund Management**. W przypadku awarii sieci lub braku współpracy ze strony kontrahenta, środki mogą teoretycznie utknąć w kontrakcie z blokadą czasową. SDK całkowicie abstrahuje od logiki odzyskiwania. Monitoruje stan każdego swapu; jeśli swap się nie powiedzie lub przekroczy limit czasu, SDK automatycznie konstruuje i transmituje transakcję zwrotu środków, aby zwrócić środki do wallet użytkownika.


Dodatkowo SDK obsługuje **Rozdzielczość metadanych**. Łączy dane off-chain swap (dostarczone przez Boltz swapper) z historią transakcji on-chain. Zapewnia to, że historia transakcji użytkownika jest czytelna dla człowieka, wyświetlając szczegóły faktury i kontekst płatności, a nie tylko surowe szesnastkowe skróty transakcji.


# Sekcja końcowa


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Recenzje i oceny


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Egzamin końcowy


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Wnioski


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>