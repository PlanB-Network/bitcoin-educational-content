---
name: Programowanie Bitcoin
goal: Zbuduj kompletną bibliotekę Bitcoin od podstaw i zrozum podstawy kryptograficzne Bitcoin
objectives: 

 - Implementacja arytmetyki pól skończonych i operacji na krzywych eliptycznych w Pythonie
 - Programowe konstruowanie i analizowanie transakcji Bitcoin
 - Tworzenie adresów testnet i rozgłaszanie transakcji w sieci
 - Opanuj podstawy matematyczne leżące u podstaw modelu bezpieczeństwa Bitcoin

---
# Podróż do skryptów i programów Bitcoin


Ten intensywny dwudniowy kurs, prowadzony przez Jimmy'ego Songa, pozwala zagłębić się w techniczne podstawy Bitcoin, budując kompletną bibliotekę Bitcoin od podstaw. Zaczynając od podstawowej matematyki pól skończonych i krzywych eliptycznych, przejdziesz przez parsowanie transakcji, wykonywanie skryptów i komunikację sieciową. Dzięki praktycznym ćwiczeniom kodowania w notatnikach Jupyter stworzysz własny adres testnet, ręcznie skonstruujesz transakcje i wyślesz je bezpośrednio do sieci - a wszystko to przy jednoczesnym dogłębnym zrozumieniu zasad kryptograficznych, które sprawiają, że Bitcoin jest bezpieczny i pozbawiony zaufania.


Miłej podróży!


+++

# Wprowadzenie


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Przegląd kursu


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Witamy w kursie PRO 202 _**Programowanie Bitcoin**_, intensywnej podróży, która zabierze Cię od arytmetyki pól skończonych aż do budowania i nadawania rzeczywistych transakcji na Bitcoin Testnet.


W tym kursie będziesz stopniowo budować bibliotekę Bitcoin w Pythonie, jednocześnie zdobywając podstawy kryptograficzne, protokoły i oprogramowanie niezbędne do precyzyjnego rozumowania na temat bezpieczeństwa i wewnętrznego działania Bitcoin. Podejście PRO 202 jest całkowicie praktyczne: każda koncepcja jest natychmiast wdrażana w notatnikach Jupyter, zapewniając, że teoria i kod wzmacniają się nawzajem.


### Podstawowe pojęcia matematyczne dla Bitcoin


Ta pierwsza sekcja ustanawia niezbędne podstawy matematyczne. Zaimplementujesz arytmetykę pól skończonych i operacje na krzywych eliptycznych (prawo grup, dodawanie, podwajanie, mnożenie skalarne...) - warunki wstępne dla ECDSA. Cel jest dwojaki: zrozumienie struktury algebraicznej, która umożliwia podpisy kryptograficzne i zbudowanie niezawodnych narzędzi Pythona do manipulowania nimi.


Następnie sformalizujesz komponenty ECDSA: generowanie kluczy, formatowanie punktów, haszowanie, tworzenie podpisów i weryfikację. Ta sekcja bezpośrednio łączy teorię z praktyką, podkreślając szczegóły implementacji i solidność podstawowego modelu bezpieczeństwa.


### Wewnętrzne działanie transakcji Bitcoin


W drugiej sekcji przeanalizujemy strukturę transakcji Bitcoin: UTXO, wejścia/wyjścia, sekwencje, skrypty, kodowania i inne. Napiszesz kod, aby skonstruować, podpisać i zweryfikować transakcje, uzyskując dokładne zrozumienie tego, co jest zatwierdzane przez hash i dlaczego.


Następnie zaimplementujesz minimalny executor _Script_, przejrzysz kluczowe kody operacyjne i zweryfikujesz ścieżki wydatków. Celem jest umożliwienie audytu zachowania transakcji, diagnozowania błędów walidacji i wnioskowania o bezpieczeństwie polityk wydatków.


### Wewnętrzne działanie sieci Bitcoin


W trzeciej sekcji umieścisz transakcje w szerszym systemie: strukturze bloków, nagłówkach, trudnościach i mechanizmie Proof-of-Work. Zajmiemy się komunikatami protokołu, nagłówkami bloków i drzewami Merkle'a.


Na koniec zapoznasz się z komunikacją między węzłami peer-to-peer, optymalizacją wiadomości i wprowadzeniem SegWit.


Podobnie jak w przypadku każdego kursu Plan ₿ Academy, ostatnia sekcja zawiera ocenę zaprojektowaną w celu utrwalenia zrozumienia. Gotowy, aby odkryć wewnętrzne działanie Bitcoin i napisać kod, który go zasila? Zaczynajmy!










# Podstawowe pojęcia matematyczne dla Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematyka dla wdrożenia Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Podstawy programowania: Podstawowe struktury matematyczne


Kurs ten kondensuje podstawową matematykę stojącą za systemami kryptograficznymi Bitcoin w wysoce praktyczny przepływ pracy. Pojęcia są wyjaśnione, zademonstrowane na przykładach, a następnie zaimplementowane w Jupyter Notebook. Idea przewodnia jest prosta: kryptograficzny prymityw można naprawdę zrozumieć dopiero po jego zakodowaniu. W trakcie dwudniowych zajęć studenci tworzą adresy sieci testowej generate, budują i transmitują transakcje, a ostatecznie wchodzą w interakcję z siecią bez użycia eksploratorów bloków. Wszystko to wymaga solidnych podstaw w dziedzinie pól skończonych i krzywych eliptycznych.


### Pola skończone: Arytmetyczny silnik kryptografii


Skończone pole F(p) to system arytmetyczny zdefiniowany przez liczbę pierwszą p, zawierający elementy od 0 do p-1. Pola pierwsze zapewniają, że każdy element niezerowy ma odwrotność, a wszystkie operacje pozostają w obrębie pola. Arytmetyka owija się wokół używania modulo p do dodawania, odejmowania i mnożenia. Pythonowe `pow(base, exp, mod)` umożliwia wydajne modularne potęgowanie, kluczowe dla dużych wykładników używanych w prawdziwych operacjach kryptograficznych.


#### Zachowanie multiplikatywne

Mnożenie dowolnego niezerowego elementu k przez wszystkie elementy pola pierwszorzędnego daje permutację pola. Właściwość ta gwarantuje jednorodność i zapobiega słabościom strukturalnym, dzięki czemu pola pierwsze są idealne do bezpiecznego generowania kluczy i [podpisów cyfrowych](https://planb.academy/resources/glossary/digital-signature).


#### Dzielenie i małe twierdzenie Fermata

Dzielenie jest realizowane za pomocą odwrotności mnożenia. Małe Twierdzenie Fermata mówi, że

n^(p-1) ≡ 1 (mod p),

więc odwrotnością jest n^(p-2). Python obsługuje to bezpośrednio za pomocą `pow(n, -1, p)`. Operacje te pojawiają się stale w procedurach kryptograficznych [ECDSA](https://planb.academy/resources/glossary/ecdsa) i Bitcoin.


### Krzywe eliptyczne: Nieliniowe struktury dla bezpieczeństwa kluczy publicznych


Krzywe eliptyczne są zgodne z równaniem y² = x³ + ax + b. Bitcoin używa secp256k1, zdefiniowanego jako y² = x³ + 7 w skończonym polu. Punkty na krzywej eliptycznej tworzą grupę matematyczną w ramach dodawania punktów. Prosta poprowadzona przez dwa punkty P i Q przecina krzywą w trzecim punkcie R; odbicie R przez oś x daje P + Q. Ten system jest asocjatywny i zawiera element tożsamości: punkt w nieskończoności.


Podwojenie punktu wykorzystuje linię styczną zamiast linii siecznej, z nachyleniem wyprowadzonym z pochodnej krzywej. Chociaż formuły te obejmują rachunek na liczbach rzeczywistych, stają się one w pełni dyskretne i dokładne, gdy krzywa jest zdefiniowana w skończonym polu - kontekście używanym w Bitcoin.


### Od matematyki do kryptografii Bitcoin


Pola skończone zapewniają deterministyczną, odwracalną arytmetykę; krzywe eliptyczne zapewniają nieliniową strukturę, w której obliczenie k-P jest łatwe, ale odwrócenie go jest obliczeniowo niewykonalne. Połączenie obu daje podstawę dla kluczy publicznych/prywatnych Bitcoin, podpisów ECDSA i bezpieczeństwa [transakcji](https://planb.academy/resources/glossary/transaction-tx). Zrozumienie tych podstaw przygotowuje studentów do bezpośredniej implementacji kluczy, transakcji i podpisów - bez abstrakcji lub narzędzi zewnętrznych.


## Kryptografia krzywych eliptycznych

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


W tym rozdziale przedstawiono krzywe eliptyczne zdefiniowane na skończonych polach i wyjaśniono, dlaczego stanowią one matematyczny szkielet [kryptografii](https://planb.academy/resources/glossary/cryptography) Bitcoin. Podczas gdy krzywe eliptyczne na liczbach rzeczywistych wydają się gładkie i ciągłe, zastosowanie tych samych równań na skończonym polu tworzy dyskretny, rozproszony zestaw punktów. Pomimo wizualnej różnicy, wszystkie formuły dodawania punktów, nachylenia i reguły algebraiczne zachowują się dokładnie tak samo - zmienia się tylko arytmetyka na arytmetykę modularną. Bitcoin wykorzystuje krzywą y² = x³ + 7 (secp256k1), która zachowuje symetrię i nieliniowe zachowanie istotne dla bezpieczeństwa kryptograficznego.


### Weryfikacja punktów i implementacja pola skończonego


Punkt leży na krzywej eliptycznej o skończonym polu, jeśli jego współrzędne spełniają równanie krzywej modulo p. Weryfikacja punktu takiego jak (73,128) na F₁₃₇ wymaga sprawdzenia, czy y² mod p równa się x³ + 7 mod p. Implementacja tego w kodzie wymaga utworzenia klas dla elementów skończonego pola i punktów krzywej. Przeciążanie operatorów zapewnia, że cała arytmetyka - dodawanie, mnożenie, potęgowanie, dzielenie - jest automatycznie wykonywana modulo p. Gdy te abstrakcje już istnieją, bardziej zaawansowane operacje kryptograficzne stają się proste do napisania i uzasadnienia.


#### Właściwości grupy i dodawanie punktów

Punkty krzywej eliptycznej tworzą grupę matematyczną pod wpływem dodawania. Grupa ta spełnia warunki domknięcia, asocjatywności, tożsamości (punkt w nieskończoności) i odwrotności (odbicie w poprzek osi x). Konstrukcje geometryczne potwierdzają te właściwości, sprawiając, że mnożenie skalarne (P wielokrotnie dodawane do siebie) jest dobrze zdefiniowane. Te reguły grupowe umożliwiają kryptografię krzywych eliptycznych i zapewniają spójne, przewidywalne zachowanie podczas powtarzających się operacji punktowych.


### Grupy cykliczne i problem logarytmu dyskretnego


Wybór punktu generatora G na krzywej pozwala nam na generate grupy cyklicznej: G, 2G, 3G, ..., nG = 0. Punkty wydają się nieliniowe i nieprzewidywalne, nawet gdy są generowane sekwencyjnie. Ta nieprzewidywalność stanowi podstawę problemu logarytmu dyskretnego: obliczenie P = sG jest łatwe, ale wyznaczenie s z P jest niewykonalne obliczeniowo dla dużych grup. Ta jednokierunkowa funkcja sprawia, że kryptografia klucza publicznego jest bezpieczna. Skale ([klucze prywatne](https://planb.academy/resources/glossary/private-key)) są zapisywane małymi literami; punkty ([klucze publiczne](https://planb.academy/resources/glossary/public-key)) wielkimi literami.


#### Wydajne mnożenie skalarne

Aby efektywnie obliczyć sG, implementacje wykorzystują algorytm podwójnego dodawania: skanowanie binarnej reprezentacji skalara, podwajanie punktu w każdym kroku i dodawanie G tylko wtedy, gdy bit wynosi 1. Zmniejsza to obliczenia z O(n) dodawania do O(log n), umożliwiając praktyczne operacje kryptograficzne nawet z 256-bitowymi skalarami.


#### Krzywa secp256k1 w Bitcoin


Bitcoin używa krzywej secp256k1, zdefiniowanej przez y² = x³ + 7 w polu pierwszym, gdzie p = 2²⁵⁶ - 2³² - 977. Punkt generatora G ma stałe współrzędne wybrane za pomocą deterministycznej procedury NUMS ("nothing up my sleeve"). Rząd grupy n jest dużą liczbą pierwszą bliską 2²⁵⁶, co zapewnia, że każdy niezerowy punkt generuje tę samą grupę. Rozmiar 2²⁵⁶ (~10⁷⁷) jest astronomicznie duży, co sprawia, że brutalne wymuszanie kluczy prywatnych jest fizycznie niemożliwe. Nawet trylion superkomputerów działających przez trylion lat nie zmniejszyłby znacząco przestrzeni kluczy.


### Klucze publiczne, klucze prywatne i serializacja SEC


Klucz prywatny to losowy skalar s; klucz publiczny to P = sG. Ponieważ rozwiązanie problemu dyskretnego logu jest niewykonalne, P może być współdzielony bez ujawniania s. Klucze publiczne muszą być serializowane do transmisji przy użyciu formatu SEC. Nieskompresowany format SEC wykorzystuje 65 bajtów: prefiks 0x04 + współrzędna x + współrzędna y. Skompresowany format wykorzystuje tylko 33 bajty: prefiks 0x02 lub 0x03 (w zależności od parzystości y) + współrzędna x. Bitcoin pierwotnie używał kluczy nieskompresowanych, ale obecnie preferuje klucze skompresowane ze względu na wydajność.


#### Bitcoin Address Tworzenie


Adresy Bitcoin są hashami kluczy publicznych, a nie samymi kluczami. Aby uzyskać adres generate, należy serializować klucz publiczny w formacie SEC, obliczyć hash160 ([SHA-256](https://planb.academy/resources/glossary/sha256), a następnie RIPEMD-160), dodać prefiks sieci (0x00 dla mainnet, 0x6F dla testnet), obliczyć sumę kontrolną przy użyciu podwójnego SHA-256, dołączyć pierwsze cztery bajty sumy kontrolnej i zakodować wynik przy użyciu Base58. Kodowanie to usuwa niejednoznaczne znaki i zawiera sumę kontrolną, aby zapobiec błędom transkrypcji. Wieloetapowy potok ukrywa klucz publiczny do momentu wydania, dodaje identyfikację sieci i zapewnia czytelne dla człowieka, odporne na błędy adresy.


# Wewnętrzne działanie transakcji Bitcoin

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Parsowanie transakcji i podpisy ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### Zrozumienie ECDSA: podstawa podpisu cyfrowego Bitcoin


Bitcoin opiera się na ECDSA, schemacie podpisu opartym na krzywej eliptycznej, oferującym silne bezpieczeństwo przy znacznie mniejszych rozmiarach kluczy niż RSA. Jego bezpieczeństwo wynika z problemu logarytmu dyskretnego krzywej eliptycznej: biorąc pod uwagę P = eG, obliczenie P jest łatwe, ale wyprowadzenie e z P jest niewykonalne obliczeniowo. Ta asymetria umożliwia kryptografię klucza publicznego przy jednoczesnym zachowaniu bezpieczeństwa kluczy prywatnych.


#### Kodowanie DER podpisów ECDSA


Bitcoin koduje podpisy ECDSA przy użyciu formatu DER:


- 0x30 (znacznik sekwencji)
- długość bajtu
- 0x02 + długość + R bajtów
- 0x02 + długość + S bajtów


Zwiększa to narzut, rozszerzając 64-bajtową sygnaturę do ~71-72 bajtów. [Taproot](https://planb.academy/resources/glossary/taproot) eliminuje tę nieefektywność, przyjmując podpisy [Schnorra](https://planb.academy/resources/glossary/schnorr-protocol) o stałym rozmiarze.


### Podpisywanie zobowiązań i proces podpisywania


Podpisy ECDSA opierają się na równaniu zobowiązania: UG + VP = KG. Podpisujący wybiera niezerowe wartości U i V oraz losowy [nonce](https://planb.academy/resources/glossary/nonce) K, udowadniając znajomość klucza prywatnego bez ujawniania go. Wiadomość jest hashowana do Z, generowany jest losowy K, R jest współrzędną x KG, a S = (Z + RE)/K. Podpisem jest para (R, S). Bezpieczeństwo zależy w dużej mierze od użycia unikalnego, nieprzewidywalnego K - jeśli K zostanie ponownie użyte lub wycieknie, klucz prywatny zostanie naruszony. Nowoczesne implementacje wykorzystują deterministyczne generowanie K (RFC 6979), aby uniknąć awarii RNG.


#### Weryfikacja podpisu

Biorąc pod uwagę Z, (R, S) i klucz publiczny P, weryfikator oblicza U = Z/S i V = R/S, a następnie sprawdza, czy współrzędna x UG + VP jest równa R. Działa to, ponieważ algebra weryfikacji rekonstruuje KG bez konieczności posiadania klucza prywatnego. Fałszowanie podpisów wymagałoby rozwiązania problemu dyskretnego logu lub złamania funkcji skrótu.


#### Podpisy Schnorr i kontekst historyczny


Podpisy Schnorra są matematycznie czystsze i obsługują funkcje agregacji, ale zostały opatentowane w momencie uruchomienia Bitcoin. ECDSA oferował darmową alternatywę, choć z większą złożonością i większymi podpisami. Po wygaśnięciu patentów, Bitcoin dodał podpisy Schnorra poprzez Taproot, zapewniając stałe 64-bajtowe podpisy i lepszą prywatność. ECDSA pozostaje obsługiwany ze względu na starszą kompatybilność.



### Struktura transakcji i dane wejściowe/wyjściowe


Transakcja Bitcoin składa się z:


- version (4 bajty, little-endian)
- lista wejściowa
- lista wyjściowa
- locktime (4 bajty)


Dane wejściowe odnoszą się do poprzednich [UTXO](https://planb.academy/resources/glossary/utxo) poprzez ich hash transakcji i indeks wyjściowy oraz zawierają skrypt odblokowujący (scriptSig) i numer sekwencji używany do blokad czasowych lub RBF. Wyjścia określają kwotę (8 bajtów) i skrypt blokujący (scriptPubKey), definiując warunki wydatków. Adresy Bitcoin są reprezentacjami tych skryptów.


#### Model UTXO

Bitcoin śledzi niewydane produkty, a nie salda kont. UTXO muszą być wydane w całości - częściowe wydanie jest niemożliwe. Aby wydać 1 BTC ze 100 BTC UTXO, transakcja musi zawierać wyjście zmiany. Zapomnienie wyjścia zmiany zamienia pozostałą część w opłatę górniczą.


#### Serializacja i parsowanie transakcji


Transakcje używają kompaktowego formatu binarnego. Po polu wersji, varint koduje liczbę wejść. Dane wejściowe obejmują:


- poprzedni hash tx (32 bajty)
- indeks wyjściowy (4 bajty)
- scriptSig (varstr)
- sekwencja (4 bajty)


Dane wyjściowe obejmują 8-bajtową kwotę i scriptPubKey (varstr). Locktime kontroluje, kiedy transakcja staje się ważna. Serializacja używa porządku little-endian dla większości liczb całkowitych. Parsery zużywają bajty sekwencyjnie i delegują do wyspecjalizowanych klas dla wejść, wyjść i skryptów.


### Opłaty, zmiany i plastyczność


Opłaty są domyślne:

fee = suma (wartości wejściowe) - suma (wartości wyjściowe).

Każda nieprzypisana wartość staje się opłatą, co sprawia, że prawidłowa konstrukcja wyjścia zmiany jest niezbędna. Przed [SegWit](https://planb.academy/resources/glossary/segwit) podpisy pozwalały na zmienność - modyfikacja S do N-S tworzyła nową ważną transakcję z innym identyfikatorem. Bitcoin wymusza teraz regułę niskiego S, a SegWit izoluje podpisy od obliczeń txid, dzięki czemu identyfikatory są stabilne i umożliwiają protokoły drugiej warstwy, takie jak [Lightning](https://planb.academy/resources/glossary/lightning-network).


## Skrypt Bitcoin i walidacja transakcji

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script to mały, oparty na stosie język inteligentnych kontraktów, który definiuje sposób wydawania monet. Każde wyjście zawiera scriptPubKey (skrypt blokujący), a każde wejście zawiera scriptSig (skrypt odblokowujący). Razem tworzą one program, który musi zostać oceniony jako "prawdziwy", aby wydanie było ważne. Skrypt celowo nie jest kompletny w sensie Turinga, aby wszystkie ścieżki wykonania były przewidywalne i łatwe do zweryfikowania w sieci.


### Operacje skryptu i model wykonania


Skrypt jest sekwencją elementów danych i kodów operacyjnych. Pchnięcia danych (podpisy, klucze publiczne, hashe) są umieszczane na stosie, podczas gdy kody operacyjne zaczynające się od `OP_` przekształcają stos. Po wykonaniu, górny element stosu musi być niezerowy dla powodzenia. Przykłady: `OP_DUP` duplikuje górny element, `OP_HASH160` stosuje SHA256, a następnie RIPEMD160, a `OP_CHECKSIG` weryfikuje podpis względem sighash transakcji i klucza publicznego, przesuwając 1 dla poprawnego, 0 dla niepoprawnego. Reguły parsowania rozróżniają surowe dane (z prefiksem długości) i kody operacyjne (wyszukiwane według wartości bajtów), a mała maszyna wirtualna wykonuje je deterministycznie na każdym węźle.


### P2PK i P2PKH: podstawowe wzorce płatności


Najwcześniejszy wzorzec, Pay-to-Public-Key (P2PK), blokował monety bezpośrednio do pełnego klucza publicznego: scriptPubKey to `<pubkey> OP_CHECKSIG`, a scriptSig to tylko podpis. Jest to proste, ale zajmuje mało miejsca i ujawnia klucz publiczny przed wydaniem monet.


#### P2PKH i adresy

Pay-to-Public-Key-Hash (P2PKH) poprawia to poprzez blokowanie do 20-bajtowego skrótu klucza publicznego. SkryptPubKey to `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, a scriptSig dostarcza `<signature> <pubkey>`. Wykonanie sprawdza, czy dostarczony klucz publiczny został skrócony do zatwierdzonej wartości, a następnie weryfikuje podpis. Ukrywa to klucz publiczny do czasu wydania, zmniejsza rozmiar i pasuje do znanego "1..." mainnet.


### Walidacja transakcji i haszowanie podpisów


[Węzeł](https://planb.academy/resources/glossary/node) walidujący transakcję musi zapewnić:

1) Każde wejście odwołuje się do istniejącego, niewydanego wyjścia.

2) Całkowita wartość wejściowa ≥ całkowita wartość wyjściowa (różnica to opłata).

3) Każdy scriptSig poprawnie odblokowuje powiązany z nim scriptPubKey.


Weryfikacja podpisu wymaga skonstruowania dokładnej wiadomości, która została podpisana, zwanej sighash. W przypadku starszego ECDSA, walidacja opróżnia wszystkie scriptSigs, zastępuje bieżący scriptSig wejścia odpowiednim scriptPubKey, dołącza 4-bajtowy typ hash (zwykle `SIGHASH_ALL`) i podwójnie hashuje wynik. Ta 256-bitowa wartość jest tym, czego używa `OP_CHECKSIG`. Alternatywne typy hashowania (np. `SINGLE`, `NONE`, z lub bez `ANYONECANPAY`) zmieniają, które części transakcji są zatwierdzane, umożliwiając niszowe przypadki użycia, takie jak wspólne finansowanie lub częściowo określone transakcje, ale są one rzadko używane w praktyce.


#### Quadratic Hashing i SegWit

Ponieważ każde wejście w starszej transakcji wymaga własnych obliczeń sighash w strukturze obejmującej wszystkie wejścia, czas walidacji może rosnąć czterokrotnie wraz z liczbą wejść. Duże transakcje z wieloma wejściami powodowały kiedyś zauważalne opóźnienia walidacji. SegWit przeprojektował obliczenia sighash, aby buforować współdzielone części i zmniejszyć złożoność do czasu liniowego, poprawiając skalowalność i utrudniając ataki typu denial-of-service.


### Zagadki skryptowe i lekcje bezpieczeństwa


Skrypt może wyrażać znacznie więcej niż proste "jeden podpis odblokowuje te monety" Łamigłówki Script pokazują to poprzez kodowanie dowolnych warunków - problemów matematycznych, wyzwań hash preimage, a nawet nagród za kolizje - w których każdy, kto dostarczy poprawne dane, może wydać monety. Jednak wyniki, które opierają się wyłącznie na danych publicznych (bez podpisów), są podatne na front-running górników: gdy prawidłowe rozwiązanie pojawi się w [mempool](https://planb.academy/resources/glossary/mempool), każdy [górnik](https://planb.academy/resources/glossary/miner) może je skopiować i przekierować wypłatę do siebie.


Praktyczny wniosek jest taki, że rzeczywiste kontrakty prawie zawsze zawierają kontrolę podpisów, nawet jeśli zawierają bardziej złożoną logikę, taką jak multisig, timelocks lub hashlocks. Podpisy wiążą rozwiązanie z konkretną stroną, zachowując zachęty i uniemożliwiając innym kradzież wypłaty. Zrozumienie modelu stosu Script, standardowych wzorców i subtelnych pułapek jest niezbędne do projektowania bezpiecznych inteligentnych kontraktów Bitcoin oraz do wnioskowania o tym, w jaki sposób transakcje są faktycznie weryfikowane w sieci.


## Budowa transakcji i płatność skryptem Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Budowanie transakcji Bitcoin i P2SH


Konstrukcja transakcji Bitcoin łączy teoretyczną wiedzę o protokole z praktyczną implementacją. Transakcja wybiera UTXO do wydania, tworzy dane wyjściowe za pomocą skryptów blokujących, tworzy podpisy dla każdego wejścia i serializuje wszystko w dokładnie takim formacie, jakiego oczekują węzły. Proces ten wymaga zrozumienia generowania sighash, zachowania skryptów oraz prawidłowej obsługi opłat i zmian.


### Podstawowa konstrukcja transakcji


Każde wejście transakcji odwołuje się do poprzedniego wyjścia przez txid i indeks. Wyjścia określają kwoty w satoshis i skryptach blokujących. Różnica między sumą wejść i sumą wyjść stanowi opłatę. Aby podpisać dane wejściowe, zmodyfikowana wersja transakcji jest serializowana, jej sighash jest obliczany, a klucz prywatny podpisuje ją. Wynikowy podpis i klucz publiczny tworzą ScriptSig. Po podpisaniu każdego wejścia, nieprzetworzona transakcja może zostać rozesłana do sieci.


### Transakcje z wieloma podpisami


Bare multisig używa `OP_CHECKMULTISIG` by wymagać m-of-n podpisów. Z powodu wczesnego błędu off-by-one, OP_CHECKMULTISIG zużywa dodatkowy element stosu, wymagając początkowego `OP_0` w ScriptSig. Bare multisig jest funkcjonalny, ale nieefektywny: wszystkie klucze publiczne pojawiają się on-chain, przez co scriptPubKeys są duże, drogie i trudne do zakodowania jako adresy. Ograniczenia te zmotywowały wprowadzenie pay-to-script-hash.


#### Architektura P2SH

P2SH ukrywa złożone skrypty za 20-bajtowym HASH160. Klucz scriptPubKey jest stały: `OP_HASH160 <20-bajtowy hash> OP_EQUAL`. Podstawowy skrypt redeem - zawierający multisig, timelocki lub inne warunki - jest ujawniany i wykonywany tylko podczas wydawania. Nadawca widzi tylko hash, podczas gdy odbiorca zarządza skryptem redeem prywatnie. Taka konstrukcja zmniejsza rozmiar on-chain, poprawia prywatność i umożliwia zawieranie złożonych umów bez obciążania nadawców.


### Wydatki i wdrożenie P2SH


Aby wydać dane wyjściowe P2SH, ScriptSig musi zawierać niezbędne dane odblokowujące *plus* sam skrypt wykupu. Walidacja odbywa się w dwóch etapach:

1) HASH160(redeem_script) musi być zgodny z hashem scriptPubKey.

2) Po weryfikacji skrypt redeem jest wykonywany z podanymi danymi.


Podczas generowania podpisów dla danych wejściowych P2SH proces sighash używa skryptu redeem zamiast klucza scriptPubKey. Każdy podpisujący musi posiadać pełny skrypt redeem, aby generate podpisy były prawidłowe. Adresy P2SH używają bajtu wersji 0x05 w mainnet (adresy "3...") i 0xC4 w testnet (adresy "2...").


#### Praktyczne względy bezpieczeństwa


Utrata skryptu redeem oznacza utratę środków: wydawanie wymaga zarówno kluczy prywatnych, jak i samego skryptu redeem. Uczestnicy Multisig muszą sprawdzić, czy ich klucze publiczne są poprawnie dołączone przed zaakceptowaniem depozytów. P2SH obsługuje zaawansowane konstrukcje, takie jak multisig, timelocks i hashlocks, ale błędy w logice skryptu mogą trwale zablokować środki, więc testowanie w sieci testowej jest niezbędne.


P2SH poprawia prywatność, ukrywając warunki wydatków do momentu pierwszego wydania, ale po pojawieniu się skryptu wykupu on-chain staje się on stale widoczny. Pomimo tego, korzyści płynące ze zmniejszonego rozmiaru, kompatybilności wstecznej i elastycznej obsługi kontraktów sprawiły, że P2SH stał się kamieniem milowym, wpływając na późniejsze aktualizacje, takie jak SegWit i Taproot.


# Wewnętrzne działanie sieci Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bloki Bitcoin i Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bloki Bitcoin grupują transakcje i zabezpieczają je za pomocą [proof of work](https://planb.academy/resources/glossary/proof-of-work). Każdy blok zawiera 80-bajtowy [nagłówek](https://planb.academy/resources/glossary/block-header) oraz listę transakcji. Pomimo dużego kosztu energii związanego z wytworzeniem ważnego bloku, jego weryfikacja jest tania: przechowywanie wszystkich ~900 tys. nagłówków wymaga tylko ~72 MB, co pozwala nawet małym urządzeniom na wydajną weryfikację łańcucha proof of work.


### Transakcje Coinbase i nagrody blokowe


Każdy blok rozpoczyna się od dokładnie jednej [transakcji Coinbase](https://planb.academy/resources/glossary/coinbase-transaction) - jedynego sposobu, w jaki nowe bitcoiny wchodzą do obiegu. Ma on wyzerowany hash prev-tx i indeks 0xffffff, jednoznacznie go identyfikujący. Dotacja rozpoczęła się od 50 BTC i zmniejsza się o połowę co 210 000 [bloków](https://planb.academy/resources/glossary/block) (50, 25, 12,5, 6,25, 3,125, ...). Górnicy uwzględniają również opłaty transakcyjne. Ponieważ 4-bajtowy nonce jest zbyt mały dla nowoczesnych układów ASIC, górnicy modyfikują dane w transakcji Coinbase, aby zmienić korzeń [Merkle](https://planb.academy/resources/glossary/merkle-tree) i stworzyć dodatkową przestrzeń wyszukiwania. BIP34 wymaga osadzenia wysokości bloku w skrypcie Coinbase scriptSig, aby zapewnić, że każdy txid Coinbase jest unikalny.


### Pola nagłówka bloku i sygnalizacja Soft Fork


80-bajtowy nagłówek zawiera:


- wersja (4 bajty)
- poprzedni skrót bloku (32 bajty)
- Korzeń Merkle (32 bajty)
- znacznik czasu (4 bajty)
- bitów (cel trudności, 4 bajty)
- nonce (4 bajty)


Numery wersji przekształciły się w system sygnalizacji bit-field za pośrednictwem [BIP9](https://planb.academy/resources/glossary/bip), umożliwiając górnikom koordynację gotowości [soft-fork](https://planb.academy/resources/glossary/soft-fork). Znacznik czasu jest 32-bitową uniksową wartością czasu i będzie wymagał aktualizacji około 2106 roku.


#### Pole bitów i cele

Pole bitów koduje cel w kompaktowej formie: cel = współczynnik × 256^(wykładnik-3). Prawidłowe skróty bloków muszą znajdować się liczbowo poniżej tego celu. Ponieważ skróty są interpretowane jako liczby całkowite little-endian, prawidłowe skróty często pojawiają się z wieloma końcowymi zerami, gdy są wyświetlane w systemie szesnastkowym.


### Trudność, walidacja i korekty


[Trudność](https://planb.academy/resources/glossary/difficulty) jest zdefiniowana jako lowest_target / current_target, wyrażając o ile trudniejszy jest obecnie mining w porównaniu do najłatwiejszego możliwego poziomu trudności. Weryfikacja wymaga jedynie porównania skrótu nagłówka z celem - niezwykle tanie w porównaniu do mining.


Co 2016 bloków, Bitcoin dostosowuje trudność do docelowych ~10-minutowych interwałów bloków. Dostosowanie porównuje rzeczywisty czas dla poprzednich bloków 2016 z oczekiwanymi dwoma tygodniami. Limity ograniczają korekty do czterokrotności. Poważne wydarzenia w świecie rzeczywistym - takie jak zakaz mining w Chinach - wykazały odporność tego mechanizmu, gdy wskaźnik hashowania gwałtownie spadł, a trudność dostosowała się w dół, aby to zrekompensować.


### Subwencja blokowa i łączna kwota Supply


Dotacja na wysokości h jest obliczana jako: dotacja = 5_000_000_000 >> (h // 210_000). Daje to harmonogram zmniejszania o połowę, który zbiega się w kierunku całkowitej podaży ~ 21 milionów BTC. Zsumowanie szeregu geometrycznego (50 + 25 + 12,5 + ...) × 210 000 wyjaśnia limit. Górnicy mogą żądać mniej niż dozwolona dotacja, ale nigdy więcej, w przeciwnym razie blok staje się nieważny. W miarę jak subsydia zmniejszają się w kolejnych halvingach, opłaty transakcyjne stają się coraz ważniejszym składnikiem przychodów górników i długoterminowego bezpieczeństwa sieci.


## Komunikacja sieciowa i drzewa Merkle'a

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Architektura sieci Bitcoin


Sieć [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) Bitcoin działa jako zdecentralizowany system plotek, w którym węzły przekazują transakcje i bloki bez wzajemnego zaufania. Nowe węzły uruchamiają się, kontaktując się z zakodowanymi na stałe nasionami DNS utrzymywanymi przez głównych programistów. Te nasiona DNS zwracają adresy IP aktywnych komputerów równorzędnych, umożliwiając węzłom wykrycie sieci, a następnie zażądanie dodatkowych komputerów równorzędnych za pośrednictwem getaddr. Sieć celowo nie jest krytyczna dla [konsensusu](https://planb.academy/resources/glossary/consensus), więc implementacje mogą się różnić, o ile zasady konsensusu pozostają niezmienione.


### Struktura wiadomości i Handshake


Wszystkie komunikaty Bitcoin P2P używają stałej koperty: 4-bajtowej wartości magicznej (F9BEB4D9 dla mainnet), 12-bajtowego polecenia ASCII, 4-bajtowej długości ładunku little-endian, 4-bajtowej sumy kontrolnej (pierwsze 4 bajty hash256) i ładunku. Typowe polecenia obejmują version, verack, inv, getdata, tx, block, getheaders, headers, ping i pong.


Uścisk dłoni rozpoczyna się, gdy łączący się węzeł wysyła komunikat o wersji. Odbiorca odpowiada komunikatem verack i własną wersją. Gdy obie strony wymienią te dwie wiadomości, połączenie jest aktywne i węzły mogą rozpocząć przekazywanie zapasów i danych.


### Drzewa Merkle i korzenie Merkle


Bitcoin przechowuje pojedynczy 32-bajtowy korzeń Merkle w nagłówku każdego bloku jako zobowiązanie do wszystkich transakcji w bloku. Transakcje są [hashowane](https://planb.academy/resources/glossary/hash-function) (hash256), parowane, łączone i hashowane wielokrotnie, aż pozostanie jeden hash. Gdy poziom ma nieparzystą liczbę, ostatni hash jest duplikowany. Wewnętrznie, hashe są big-endian, podczas gdy serializowane dane blokowe używają little-endian, co wymaga odwrócenia przed i po konstrukcji drzewa.


#### Dowody Merkle'a i SPV

Dowody Merkle pozwalają zweryfikować, czy transakcja jest zawarta w bloku bez pobierania całego bloku. Dowód składa się z hashy rodzeństwa wzdłuż ścieżki do korzenia. Lekcy klienci SPV przechowują tylko nagłówki bloków i żądają tych dowodów od [pełnych węzłów](https://planb.academy/resources/glossary/full-node). Ponieważ drzewo Merkle rośnie logarytmicznie, udowodnienie włączenia do bloku z tysiącami transakcji wymaga tylko kilkuset bajtów.


Taproot rozszerza tę koncepcję, przypisując warunki wydawania do drzewa skryptów Merklized (MAST), ujawniając tylko wykonaną gałąź wraz z dowodem Merkle. Poprawia to zarówno wydajność, jak i prywatność.


### Operacje sieciowe i synchronizacja bloków


Węzły używają getdata do żądania transakcji lub bloków, określając identyfikator typu (1=tx, 2=block, 3=filtered block, 4=compact block) plus 32-bajtowy identyfikator. W przypadku synchronizacji łańcuchowej węzły wysyłają getheaders z początkowym hashem bloku, otrzymując w odpowiedzi do 2000 nagłówków. Każdy zwrócony nagłówek to 80 bajtów, po których następuje fikcyjna liczba transakcji równa zero.


Pełna weryfikacja otrzymanych bloków wymaga dwóch kontroli:

1. Hash bloku musi znajdować się poniżej wartości docelowej zakodowanej w polu bitów.

2. Korzeń Merkle obliczony ze wszystkich transakcji (z odpowiednią obsługą endianness) musi być zgodny z korzeniem nagłówka.


Tylko jeśli oba warunki się spełnią, węzeł akceptuje blok, odzwierciedlając zasadę Bitcoin "nie ufaj, weryfikuj".


## Zaawansowana komunikacja z węzłami i oddzielny świadek

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Ta sesja łączy zaawansowaną sieć P2P z Segregated Witness, pokazując, jak nowoczesne oprogramowanie Bitcoin współdziała bezpośrednio z węzłami, wykorzystując struktury transakcji świadome SegWit. Programiści uczą się pobierać bloki, skanować w poszukiwaniu odpowiednich transakcji i konstruować transakcje przy użyciu jedynie nieprzetworzonej komunikacji sieciowej - nie są wymagane eksploratory bloków.


### Pobieranie transakcji oparte na blokach i prywatność


[Portfele](https://planb.academy/resources/glossary/wallet) muszą wykrywać przychodzące płatności, skanując bloki w poszukiwaniu danych wyjściowych pasujących do ich klucza scriptPubKey. Pobieranie całych bloków chroni prywatność lepiej niż żądanie pojedynczych transakcji, które wycieka silne sygnały o aktywności użytkownika. Nawet żądania bloków mogą powodować wyciek informacji o łańcuchach o niskim wolumenie, co sprawia, że kompaktowe filtry bloków (BIP158) są niezbędne dla lekkich klientów chroniących prywatność. Filtry mogą generować wyniki fałszywie dodatnie, ale nigdy fałszywie ujemne, umożliwiając klientom pobieranie tylko potencjalnie istotnych bloków bez ujawniania konkretnych adresów.


### Trustless Interakcja sieciowa


Przepływ pracy `get_block` demonstruje prawidłowe użycie sieci: wyślij getdata, odbierz blok, a następnie niezależnie zweryfikuj jego korzeń Merkle i proof of work. Blok jest akceptowany tylko wtedy, gdy otrzymany hash nagłówka pasuje do żądanego hasha, a jego obliczony korzeń Merkle pasuje do nagłówka. Uosabia to zasadę "nie ufaj, weryfikuj", zapewniając, że nawet złośliwi użytkownicy nie mogą nakłonić węzłów do zaakceptowania zmienionych danych.


#### Pobieranie transakcji z bloków

Transakcje bloku mogą być skanowane w poszukiwaniu pasujących kluczy scriptPubKeys przy użyciu prostej iteracji. Portfele produkcyjne wykonują to w sposób ciągły w miarę pojawiania się nowych bloków, udowadniając własność danych wyjściowych wyłącznie poprzez walidację kryptograficzną, a nie polegając na interfejsach API innych firm.


### Cele i projekt SegWit


Segregated Witness (SegWit) naprawił podatność transakcji na manipulacje poprzez usunięcie danych podpisu z obliczeń txid. Umożliwiło to tworzenie niezawodnych, wstępnie podpisanych łańcuchów transakcji i sprawiło, że Lightning Network stał się praktyczny. SegWit zwiększył również pojemność bloków za pomocą "wagi bloku": stare węzły nadal widzą bloki ≤1 MB, podczas gdy zmodernizowane węzły zatwierdzają do 4 MB, w tym dane świadka. Wersjonowane programy świadków (dotychczas v0-v1) tworzą ustrukturyzowaną ścieżkę aktualizacji dla przyszłych typów skryptów.


#### P2WPKH (rodzimy SegWit)


P2WPKH zastępuje starszą strukturę P2PKH 22-bajtowym skryptem: OP_0 + push20 + hash160(pubkey). Spending przenosi podpis i pubkey do osobnego pola świadka.


- Węzły sprzed SegWit: patrz "każdy może wydać", traktuj to jako prawidłowe.
- Węzły po SegWit: rozpoznają OP_0 + 20-bajtowy hash i sprawdzają poprawność przy użyciu danych świadków.


Ta separacja poprawia plastyczność i zmniejsza opłaty. Świadek używa liczby varint, po której następuje podpis i klucz publiczny.


#### P2SH-P2WPKH (wstecznie kompatybilny z SegWit)


Aby umożliwić starym portfelom wysyłanie na adresy SegWit, skrypty P2WPKH mogą być opakowane w P2SH.


- scriptPubKey: standardowy P2SH hash160(redeemScript)
- scriptSig: skrypt odkupienia (program P2WPKH)
- świadek: podpis + klucz publiczny


Warstwy walidacyjne:

1. Węzły sprzed BIP16 akceptują redeemScript jako prawidłowy.

2. Węzły po BIP16 oceniają go, pozostawiając OP_0 + hash na stosie.

3. Węzły SegWit wykonują pełną weryfikację świadków.


#### P2WSH dla złożonych skryptów


P2WSH uogólnia SegWit dla multisig i zaawansowanych skryptów poprzez zatwierdzenie SHA256(script) zamiast hash160. Typowy stos świadków multisig 2 na 3:


- pusty element (błąd CHECKMULTISIG)
- sig1
- sig2
- skrypt świadka (skrypt multisig)


Węzły SegWit weryfikują zgodność SHA256(witnessScript) z hashem scriptPubKey, a następnie wykonują go. Użycie SHA256 i 32-bajtowego skrótu pozwala odróżnić P2WSH od P2WPKH i wzmacnia bezpieczeństwo.


#### P2SH-P2WSH (maksymalna kompatybilność)


Złożone skrypty SegWit mogą być również opakowane w P2SH:


- scriptSig: redeemScript (OP_0 + 32-bajtowy hash)
- świadek: podpisy + witnessScript


Walidacja przechodzi przez trzy generacje reguł dokładnie tak, jak w przypadku P2SH-P2WPKH. Ten wrapper był niezbędny dla wczesnych wdrożeń Lightning wymagających multisig bez możliwości modyfikacji. Podczas gdy natywny P2WSH jest obecnie preferowany, zawinięta forma zapewnia kompatybilność ze starszymi systemami wallet.


### Wpływ SegWit


SegWit:


- stabilne identyfikatory transakcji
- niższe opłaty dzięki zniżkom na dane świadków
- wyższa przepustowość bloków dzięki wadze bloków
- kompatybilność dla starych węzłów
- czysta ścieżka aktualizacji dla Taproot i przyszłych rozszerzeń


Wraz z pozbawioną zaufania interakcją sieciową, narzędzia te stanowią podstawę nowoczesnego rozwoju Bitcoin.



# Sekcja końcowa


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Recenzje i oceny


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Egzamin końcowy


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Wnioski



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>