---
name: Wprowadzenie do kryptografii
goal: Zrozumienie tworzenia portfela Bitcoin z perspektywy kryptograficznej
objectives:
  - Rozszyfrowanie terminologii kryptograficznej związanej z Bitcoinem.
  - Opanowanie tworzenia portfela Bitcoin.
  - Zrozumienie struktury portfela Bitcoin.
  - Zrozumienie adresów i ścieżek pochodzenia.
---

# Podróż do świata kryptografii

Czy fascynuje Cię Bitcoin? Zastanawiasz się, jak działa portfel Bitcoin? Przygotuj się na fascynującą podróż do świata kryptografii! Loïc, nasz ekspert, poprowadzi Cię przez zawiłości tworzenia portfela Bitcoin, odkrywając tajemnice zastraszających terminów technicznych takich jak hashowanie, pochodzenie kluczy i krzywe eliptyczne.

To szkolenie nie tylko wyposaży Cię w wiedzę potrzebną do zrozumienia struktury portfela Bitcoin, ale także przygotuje do głębszego zanurzenia się w ekscytujący świat kryptografii. Czy jesteś gotowy, aby wyruszyć w tę podróż? Dołącz do nas i przekształć swoją ciekawość w ekspertyzę!

+++

# Wprowadzenie

## Wprowadzenie do kryptografii

### Czy to szkolenie jest dla Ciebie? TAK!

![wprowadzenie przez Rogzy](https://youtu.be/ul8zU5QWIXg)

Z przyjemnością witamy Cię na nowym kursie szkoleniowym zatytułowanym "Crypto 301: Wprowadzenie do kryptografii i portfeli HD", prowadzonym przez samego eksperta, Loïca Morela. Ten kurs zanurzy Cię w fascynujący świat kryptografii, fundamentalnej dyscypliny matematyki, która zapewnia szyfrowanie i bezpieczeństwo Twoich danych.

W naszym codziennym życiu, a szczególnie w świecie Bitcoina, kryptografia odgrywa kluczową rolę. Pojęcia związane z kryptografią, takie jak klucze prywatne, klucze publiczne, adresy, ścieżki pochodzenia, seed i entropia, są w sercu używania i tworzenia portfela Bitcoin. W trakcie tego kursu, Loïc szczegółowo wyjaśni, jak generowane są klucze prywatne i jak są one powiązane z adresami. Loïc poświęci również godzinę na wyjaśnienie matematycznych szczegółów krzywych eliptycznych, tej złożonej krzywej matematycznej. Dodatkowo, zrozumiesz, dlaczego użycie HMAC SHA512 jest ważne dla zabezpieczenia Twojego portfela i jaka jest różnica między seed a frazą mnemoniczną.

Ostatecznym celem tego szkolenia jest umożliwienie Ci zrozumienia technicznych procesów tworzenia portfela HD i używanych metod kryptograficznych. Na przestrzeni lat, portfele Bitcoin ewoluowały, stając się łatwiejsze w użyciu, bardziej bezpieczne i ustandaryzowane dzięki konkretnym BIPom. Loïc pomoże Ci zrozumieć te BIPy, aby pojąć wybory dokonane przez deweloperów Bitcoina i kryptografów. Jak wszystkie szkolenia oferowane przez naszą uczelnię, to jest całkowicie darmowe i open source. Oznacza to, że możesz swobodnie wziąć udział i używać go, jak chcesz. Czekamy na Twoją opinię na koniec tego ekscytującego kursu.

### Słowo przekazuję profesorowi!

![wprowadzenie przez Loïca](https://youtu.be/mwuxXLk4Kws)

Witajcie wszyscy, jestem Loïc Morel, Waszym przewodnikiem przez ten techniczny eksplorację kryptografii używanej w portfelach Bitcoin.

Nasza podróż zaczyna się od zagłębienia w głąb funkcji skrótu kryptograficznego. Razem zbadamy działanie niezbędnego SHA256 i zbadamy różne algorytmy dedykowane pochodzeniu.

Kontynuując naszą przygodę, odszyfrujemy tajemniczy świat podpisów cyfrowych. Odkryjecie, jak magia krzywych eliptycznych stosuje się do tych podpisów, i rzucimy światło na to, jak obliczyć klucz publiczny z klucza prywatnego. I oczywiście, zajmiemy się aktem podpisywania kluczem prywatnym.
Następnie cofniemy się w czasie, aby zobaczyć ewolucję portfeli Bitcoin, i zagłębimy się w koncepcje entropii i liczb losowych. Przeanalizujemy słynną frazę mnemoniczną, jednocześnie zagłębiając się w temat haseł. Będziesz miał nawet okazję doświadczyć czegoś wyjątkowego, tworząc ziarno z 128 rzutów kośćmi!
Z tym solidnym fundamentem będziemy gotowi na kluczową część: tworzenie portfela Bitcoin. Od narodzin ziarna i klucza głównego, po studium rozszerzonych kluczy i wyprowadzanie par kluczy potomnych, każdy krok zostanie szczegółowo omówiony. Omówimy również strukturę portfela i ścieżki pochodzenia.

Na koniec naszej podróży zbadamy adresy Bitcoin. Wyjaśnimy, jak są tworzone i jak odgrywają kluczową rolę w funkcjonowaniu portfeli Bitcoin.

Dołącz do mnie w tej fascynującej podróży i przygotuj się na eksplorację świata kryptografii jak nigdy dotąd. Zostaw swoje uprzedzenia za drzwiami i otwórz umysł na nowy sposób rozumienia Bitcoina i jego fundamentalnej struktury.

# Funkcje skrótu

## Wprowadzenie do funkcji skrótu kryptograficznego związanych z Bitcoinem

![2.1 - Funkcje skrótu kryptograficznego](https://youtu.be/dvnGArYvVr8)

Witaj na dzisiejszej sesji poświęconej dogłębnemu zanurzeniu w kryptograficzny świat funkcji skrótu, niezbędnego filaru bezpieczeństwa protokołu Bitcoina. Wyobraź sobie funkcję skrótu jako ultraefektywnego kryptograficznego robota dekodującego, który przekształca informacje wszelkich rozmiarów w unikalny i stały cyfrowy odcisk palca zwany "skrótem". Podczas naszej eksploracji przedstawimy profil funkcji skrótu kryptograficznego, podkreślając ich zastosowanie w protokole Bitcoina i definiując specyficzne cele, które te funkcje kryptograficzne muszą osiągnąć.

![obraz](assets/image/section1/0.JPG)

Przedstawienie profilu funkcji skrótu kryptograficznego wymaga zrozumienia dwóch kluczowych cech: ich nieodwracalności i odporności na fałszerstwa. Każda funkcja skrótu kryptograficznego jest jak unikalny artysta, produkujący odrębny "skrót" dla każdego wejścia. Nawet nieznacznie odmienny pociągnięcie pędzla znacząco zmienia finalny obraz, czyli skrót. Te funkcje działają jak cyfrowi strażnicy, weryfikując integralność pobieranego oprogramowania. Inną kluczową cechą, którą posiadają, jest ich odporność na kolizje. Z pewnością, w uniwersum skrótów, kolizje są nieuniknione, ale doskonała funkcja skrótu kryptograficznego minimalizuje je znacząco. To tak, jakby każdy skrót był domem w ogromnym mieście; pomimo ogromnej liczby domów, dobra funkcja skrótu zapewnia, że każdy dom ma unikalny adres.

![obraz](assets/image/section1/1.JPG)

Przejdźmy teraz przez burzliwe wody przestarzałych funkcji skrótu. SHA0, SHA1 i MD5 są obecnie uważane za zardzewiałe relikty w oceanie kryptograficznego hashowania. Są często odradzane, ponieważ straciły swoją odporność na kolizje. Zasada szuflad wyjaśnia, dlaczego pomimo naszych najlepszych starań, uniknięcie kolizji jest niemożliwe ze względu na ograniczenie rozmiaru wyjścia. Ważne jest również zauważenie, że odporność na drugi preobraz zależy od odporności na kolizje. Aby funkcja skrótu była uważana za naprawdę bezpieczną, musi być odporna na kolizje, drugi preobraz i preobraz.

Kluczowy element w protokole Bitcoina, funkcja skrótu SHA-256 jest kapitanem statku. Inne funkcje, takie jak SHA-512, są używane do wyprowadzania z HMAC i PBKDF. Ponadto, RIPMD160 jest używany do redukcji odcisku palca do 160 bitów. Gdy mówimy o HASH256 i HASH160, odnosimy się do użycia podwójnego hashowania z SHA-256 i RIPMD. Użycie HASH160 jest szczególnie korzystne, ponieważ pozwala na bezpieczeństwo SHA-256 przy jednoczesnym zmniejszeniu rozmiaru odcisku palca.
Podsumowując, ostatecznym celem funkcji skrótu kryptograficznego jest przekształcenie informacji o dowolnym rozmiarze w odcisk o stałym rozmiarze. Aby była uznana za bezpieczną, musi posiadać kilka zalet: nieodwracalność, odporność na fałszowanie, odporność na kolizje oraz odporność na drugi obraz.
![image](assets/image/section1/2.JPG)

Na koniec tego eksplorowania rozwialiśmy tajemnice funkcji skrótu kryptograficznego, podkreśliliśmy ich zastosowanie w protokole Bitcoina i przeanalizowaliśmy ich konkretne cele. Dowiedzieliśmy się, że aby funkcje skrótu były uznane za bezpieczne, muszą być odporne na preobraz, drugi obraz, kolizje i fałszowanie. Omówiliśmy również różne funkcje skrótu używane w protokole Bitcoina. W naszej następnej sesji zagłębimy się w rdzeń funkcji skrótu SHA256 i odkryjemy fascynującą matematykę, która nadaje jej unikalne cechy.

## Wewnętrzne mechanizmy SHA256

![Wewnętrzne mechanizmy SHA256](https://youtu.be/74SWg_ZbUj4)

Witamy w kontynuacji naszej fascynującej podróży przez kryptograficzne labirynty funkcji skrótu. Dziś odkrywamy tajemnice SHA256, skomplikowanego, lecz genialnego procesu, który wprowadziliśmy w naszej poprzedniej dyskusji na temat funkcji skrótu. Zróbmy kolejny krok w tym labiryncie, zaczynając od wstępnego przetwarzania SHA256. Wyobraź sobie wstępne przetwarzanie jako przygotowanie pysznego dania, gdzie dodajemy "bity dopełnienia", aby rozmiar naszego głównego składnika, wejścia, osiągnął idealną wielokrotność 512 bitów. Wszystko to z ostatecznym celem wygenerowania smakowitego 256-bitowego skrótu z składnika o zmiennej wielkości.

![image](assets/image/section1/3.JPG)
![image](assets/image/section1/4.JPG)

W tej kryptograficznej recepturze bawimy się bitami, mając początkowy rozmiar wiadomości, który nazwiemy M. Jeden bit jest zarezerwowany na separator, podczas gdy bity P są używane do dopełnienia. Dodatkowo, odłożymy na bok 64 bity na drugą fazę przetwarzania wstępnego. Całość musi być wielokrotnością 512 bitów. To trochę jak upewnienie się, że wszystkie składniki doskonale się łączą w naszym daniu.

![image](assets/image/section1/5.JPG)

Przechodzimy teraz do drugiej fazy przetwarzania wstępnego, która polega na dodaniu binarnej reprezentacji początkowego rozmiaru wiadomości, w bitach. W tym celu używamy naszych 64 zarezerwowanych bitów z poprzedniego kroku. Dodajemy zera, aby zaokrąglić nasze 64 bity do naszego zbilansowanego wejścia. Następnie łączymy początkową wiadomość, bity dopełnienia i dopełnienie rozmiaru, jak składniki w blenderze, aby uzyskać nasze zbilansowane wejście.

![image](assets/image/section1/6.JPG)

Teraz przygotowujemy się do pierwszych kroków przetwarzania funkcji SHA-256. Jak w każdym dobrym przepisie, potrzebujemy kilku podstawowych składników, które nazywamy stałymi i wektorami inicjalizacji. Wektory inicjalizacji, od A do H, to pierwsze 32 bity części dziesiętnych pierwiastków kwadratowych pierwszych 8 liczb pierwszych. Stałe K, od 0 do 63, reprezentują pierwsze 32 bity części dziesiętnych pierwiastków sześciennych pierwszych 64 liczb pierwszych.

![image](assets/image/section1/7.JPG)

W funkcji kompresji używamy specyficznych operatorów, takich jak XOR, AND i NOT. Przetwarzamy bity jeden po drugim zgodnie z ich rangą, używając operatora XOR i tabeli prawdy. Operator AND jest używany do zwrócenia 1 tylko wtedy, gdy oba operandy są równe 1, a operator NOT do zwrócenia przeciwnej wartości operandu. Używamy również operacji SHR do przesunięcia bitów w prawo o wybraną liczbę.

![image](assets/image/section1/8.JPG)
Ostatecznie, po podzieleniu zbilansowanego wejścia na różne bloki wiadomości 512-bitowych, wykonujemy 64 rundy obliczeń w funkcji kompresji. Podobnie jak w wyścigu kolarskim, każde okrążenie poprawia naszą pozycję. Dodajemy modulo 2^32 stan pośredni do stanu początkowego funkcji kompresji. Dodawania w funkcji kompresji to dodawania modulo 2^32, aby ograniczyć rozmiar sum do 32 bitów.

Aby zakończyć, chcielibyśmy podkreślić kluczową rolę obliczeń wykonywanych w blokach CH, MAJ, σ0 i σ1. Te operacje, wśród innych, są strażnikami, które zapewniają odporność funkcji skrótu SHA256 na ataki, czyniąc ją preferowanym wyborem do zabezpieczania licznych systemów cyfrowych, szczególnie w protokole Bitcoin. Jest oczywiste, że, pomimo złożoności, piękno SHA256 leży w jego odporności na znalezienie wejścia z hasha, podczas gdy weryfikacja hasha dla danego wejścia jest mechanicznie prostą czynnością.

## Algorytmy używane do wyprowadzania

![Algorytmy używane do wyprowadzania](https://youtu.be/ZF1_BMsOJXc)

Algorytmy wyprowadzania HMAC i PBKDF2 są kluczowymi elementami mechanizmu bezpieczeństwa protokołu Bitcoin. Zapobiegają one różnorodnym potencjalnym atakom i zapewniają integralność portfeli Bitcoin.

HMAC i PBKDF2 to narzędzia kryptograficzne używane do różnych zadań w Bitcoinie. HMAC jest głównie używany do przeciwdziałania atakom na rozszerzenie długości podczas wyprowadzania hierarchicznie deterministycznych (HD) portfeli, podczas gdy PBKDF2 jest używany do konwersji frazy mnemonicznej na ziarno.

HMAC, który przyjmuje wiadomość i klucz jako dane wejściowe, generuje wyjście o stałym rozmiarze. Aby zapewnić jednolitość, klucz jest dostosowywany w oparciu o rozmiar bloku używany w funkcji skrótu. W kontekście wyprowadzania portfeli HD, używany jest HMAC-SHA-512. Ten ostatni operuje na blokach 1024-bitowych (128-bajtowych) i odpowiednio dostosowuje klucz. Używa stałych OPAD (0x5c) i IPAD (0x36), powtarzanych w razie potrzeby, aby zwiększyć bezpieczeństwo.

Proces HMAC-SHA-512 polega na łączeniu wyniku zastosowania SHA-512 do klucza XOR OPAD i klucza XOR IPAD z wiadomością. Gdy używane są bloki 1024-bitowe (128-bajtowe), klucz wejściowy jest w razie potrzeby dopełniany zerami, a następnie XORowany z IPAD i OPAD. Zmodyfikowany klucz jest następnie łączony z wiadomością.

Użycie soli, poprzez włączenie dodatkowego źródła entropii, zwiększa bezpieczeństwo wyprowadzonych kluczy. Bez niej atak mógłby skompromitować cały portfel i ukraść wszystkie bitcoiny.
PBKDF2 jest używany do konwersji frazy mnemonicznej na ziarno. Algorytm ten wykonuje 2048 rund korzystając z HMAC SHA512. Dzięki tym algorytmom pochodnym, dwa różne wejścia mogą wyprodukować unikalne i stałe wyjście, co łagodzi problem możliwych ataków rozszerzenia długości na funkcje rodziny SHA-2. Atak rozszerzenia długości wykorzystuje specyficzną właściwość niektórych funkcji skrótu kryptograficznego. W takim ataku, atakujący, który już posiada skrót nieznanego komunikatu, może go użyć do obliczenia skrótu dłuższego komunikatu, który jest rozszerzeniem oryginalnego komunikatu. Często jest to możliwe bez znajomości treści oryginalnego komunikatu, co może prowadzić do znaczących luk w bezpieczeństwie, jeśli tego typu funkcja skrótu jest używana do zadań takich jak weryfikacja integralności.
![image](assets/image/section1/16.JPG)

Podsumowując, algorytmy HMAC i PBKDF2 odgrywają kluczowe role w zabezpieczeniach pochodzenia portfeli HD w protokole Bitcoin. HMAC-SHA-512 jest używany do ochrony przed atakami rozszerzenia długości, podczas gdy PBKDF2 umożliwia konwersję frazy mnemonicznej na ziarno. Kod łańcucha dodaje dodatkowe źródło entropii w pochodzeniu klucza, zapewniając solidność systemu.

# Podpisy cyfrowe

## Podpisy cyfrowe i krzywe eliptyczne

![Podpisy cyfrowe i krzywe eliptyczne](https://youtu.be/gOjYiPkx4z8)

W świecie kryptowalut, bezpieczeństwo transakcji jest najważniejsze. W samym rdzeniu protokołu Bitcoin, podpisy cyfrowe są używane jako matematyczne dowody demonstrujące posiadanie klucza prywatnego powiązanego z określonym kluczem publicznym. Ta technika ochrony danych opiera się zasadniczo na fascynującej dziedzinie kryptografii zwanej kryptografią krzywych eliptycznych (ECC).

![image](assets/image/section2/0.JPG)

Kryptografia krzywych eliptycznych jest kręgosłupem bezpieczeństwa transakcji Bitcoin. Te krzywe eliptyczne, przypominające matematyczne krzywe, które studiowaliśmy w szkole, są użyteczne w różnorodnych zastosowaniach kryptograficznych, od wymiany kluczy po asymetryczne szyfrowanie po tworzenie podpisów cyfrowych. Interesującym szczegółem, który odróżnia krzywe eliptyczne, jest ich symetria: każda niepionowa linia przecinająca dwa punkty na krzywej przetnie trzeci punkt.

Teraz zagłębmy się nieco głębiej: protokół Bitcoin używa specyficznej krzywej eliptycznej zwanej SecP256K1 do wykonywania swoich operacji kryptograficznych. Ta krzywa, zdefiniowana na skończonym zbiorze dodatnich liczb całkowitych modulo liczba pierwsza o 256 bitach, może być wizualizowana jako chmura punktów, a nie tradycyjna krzywa. To unikalne projektowanie pozwala Bitcoinowi skutecznie zabezpieczać swoje transakcje.

![image](assets/image/section2/1.JPG)

Jeśli chodzi o wybór krzywej secp256k1 dla Bitcoina, warto zauważyć, że została ona wybrana zamiast krzywej secp256r1. Ta krzywa jest zdefiniowana przez parametry a=0 i b=7, a jej równanie to y² = x³ + 7 modulo n, gdzie n reprezentuje liczbę pierwszą, która określa porządek krzywej.

Gdy mówimy o stałych używanych w systemie Bitcoina, ogólnie odnosimy się do specyficznych parametrów Algorytmu Cyfrowego Podpisu Krzywej Eliptycznej (ECDSA) i systemu krzywych eliptycznych używanego przez Bitcoina, którym jest krzywa secp256k1. Oto te parametry:
- pole pierwsze (p): Bitcoin używa krzywej nad polem pierwszym, więc p jest pierwszą liczbą używaną do zdefiniowania tego pola. Dla krzywej secp256k1, p jest równe `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` w systemie szesnastkowym lub p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 w systemie dziesiętnym.
- rząd krzywej (n): Jest to liczba punktów na krzywej, włączając punkt w nieskończoności. Dla secp256k1, n jest równe `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` w systemie szesnastkowym lub n = 2^256 - 432420386565659656852420866394968145599 w systemie dziesiętnym.
- punkt generatora (G): Punkt bazowy, czyli generator, to punkt na krzywej, z którego generowane są wszystkie inne klucze publiczne. Ma on określone współrzędne x i y, zazwyczaj reprezentowane w systemie szesnastkowym. Dla secp256k1, współrzędne G są, w systemie szesnastkowym:
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

![obraz](assets/image/section2/2.JPG)

Zauważ, że wszystkie wartości szesnastkowe są generalnie reprezentowane w systemie bazowym 16, podczas gdy wartości dziesiętne są w systemie bazowym 10. Ponadto, wszystkie operacje na tych stałych są wykonywane modulo p dla współrzędnych punktów na krzywej i modulo n dla operacji z kluczami i podpisami.

Więc gdzie przechowywane są te słynne bitcoiny? Nie w portfelu Bitcoin, jak mogłoby się wydawać. W rzeczywistości, portfel Bitcoin przechowuje klucze prywatne niezbędne do udowodnienia posiadania bitcoinów. Same bitcoiny są zapisane na blockchainie, zdecentralizowanej bazie danych, która archiwizuje wszystkie transakcje.

W systemie Bitcoin, jednostką rozliczeniową jest bitcoin (zwróć uwagę na małą literę "b"). Jest on podzielny do ośmiu miejsc dziesiętnych, z najmniejszą jednostką będącą satoshi. UTXO, czyli "Unspent Transaction Outputs", reprezentują niewykorzystane wyjścia transakcji należące do użytkownika. Aby wydać te bitcoiny, należy wykazać posiadanie klucza prywatnego odpowiadającego kluczowi publicznemu powiązanemu z każdym UTXO.

Aby zapewnić bezpieczeństwo transakcji, Bitcoin opiera się na dwóch protokołach podpisu cyfrowego: ECDSA (Elliptic Curve Digital Signature Algorithm) i Schnorr. ECDSA to protokół podpisu zintegrowany z Bitcoinem od jego uruchomienia w 2009 roku, podczas gdy podpisy Schnorra zostały dodane stosunkowo niedawno, w listopadzie 2021 roku. Chociaż oba protokoły opierają się na kryptografii krzywych eliptycznych i używają podobnych mechanizmów matematycznych, różnią się głównie strukturą podpisu.

Zanim zagłębimy się głębiej w te mechanizmy podpisu, ważne jest, aby zrozumieć, czym jest krzywa eliptyczna. Krzywa eliptyczna jest zdefiniowana przez równanie y² = x³ + ax + b. Każdy punkt na tej krzywej ma charakterystyczną symetrię, która jest kluczowa dla jej użyteczności w kryptografii.
Ostatecznie, różne krzywe eliptyczne są uznawane za bezpieczne do użytku kryptograficznego. Być może najbardziej znaną jest krzywa secp256r1. Jednak dla Bitcoina, Satoshi Nakamoto wybrał inną krzywą: secp256k1.
W następnej sekcji tego kursu przyjrzymy się bliżej kluczowi publicznemu i kluczowi prywatnemu, aby dokładnie zrozumieć kryptografię na krzywych eliptycznych oraz algorytm podpisu cyfrowego. Będzie to czas na ugruntowanie wiedzy i zrozumienie, jak wszystkie te informacje łączą się, aby zapewnić bezpieczeństwo protokołu Bitcoina.

## Obliczanie klucza publicznego z klucza prywatnego

![Obliczanie klucza publicznego z klucza prywatnego](https://youtu.be/NJENwFU889Y)

W kolejnej sekcji tego kursu zagłębimy się w mechanizmy kluczy publicznych i prywatnych, dwóch kluczowych elementów protokołu Bitcoina. Te klucze są nierozerwalnie połączone przez Algorytm Podpisu Cyfrowego Krzywej Eliptycznej (ECDSA). Zrozumienie ich da nam głęboki wgląd w to, jak Bitcoin zabezpiecza transakcje na swojej platformie.

![image](assets/image/section2/3.JPG)
![image](assets/image/section2/4.JPG)

Na początek, zanurkujmy w świat algorytmu ECDSA. Bitcoin wykorzystuje ten algorytm podpisu cyfrowego do łączenia kluczy prywatnych i publicznych. W tym systemie, klucz prywatny to losowa lub pseudolosowa liczba 256-bitowa. Teoretyczna liczba możliwości dla klucza prywatnego to 2^256, ale w rzeczywistości jest nieco mniejsza. Dokładniej, niektóre 256-bitowe klucze prywatne nie są ważne dla Bitcoina.

![image](assets/image/section2/5.JPG)

Aby być kompatybilnym z Bitcoinem, klucz prywatny musi znajdować się w przedziale od 1 do n-1, gdzie n reprezentuje rząd krzywej eliptycznej. Oznacza to, że całkowita liczba możliwości dla klucza prywatnego Bitcoina jest prawie równa 1.158 x 10^77. Dla porównania, jest to mniej więcej taka sama liczba atomów obecnych we wszechświecie obserwowalnym. Unikalny klucz prywatny jest następnie używany do wygenerowania 512-bitowego klucza publicznego.

![image](assets/image/section2/6.JPG)

Klucz publiczny, oznaczony jako K, to punkt na krzywej eliptycznej, który jest pochodną klucza prywatnego za pomocą operacji punktowych na krzywej. Ważne jest, aby zauważyć, że funkcja ECDSA jest nieodwracalna, co oznacza, że niemożliwe jest odzyskanie klucza prywatnego z klucza publicznego. Ta nieodwracalność jest kamieniem węgielnym bezpieczeństwa portfela Bitcoin.

Klucz publiczny składa się z dwóch 256-bitowych punktów, co daje łącznie 512 bitów. Jednak może być skompresowany do 264-bitowej liczby. Punkt G jest punktem wyjścia do obliczania wszystkich kluczy publicznych użytkowników w systemie.

![image](assets/image/section2/7.JPG)

Jedną z niezwykłych właściwości krzywych eliptycznych jest to, że linia przecinająca krzywą w dwóch punktach przetnie również trzeci punkt, nazywany punktem O. Właściwość ta jest wykorzystywana do określenia punktu U, który jest przeciwny do punktu O. Dodawanie punktu do siebie odbywa się poprzez narysowanie stycznej do krzywej w tym punkcie, co skutkuje nowym unikalnym punktem o nazwie j. Mnożenie skalarnie punktu przez n jest równoważne dodaniu tego punktu do siebie n razy.

![image](assets/image/section2/8.JPG)
Operacje na punktach krzywej eliptycznej stanowią podstawę do obliczania kluczy publicznych. Znając klucz prywatny, łatwo jest obliczyć klucz publiczny. Jednakże, znając klucz publiczny, nie można obliczyć klucza prywatnego, co zapewnia bezpieczeństwo systemu Bitcoin. W rzeczywistości bezpieczeństwo kluczy publicznych i prywatnych opiera się na problemie dyskretnego logarytmu, skomplikowanym zagadnieniu matematycznym.
![image](assets/image/section2/9.JPG)

W naszej kolejnej lekcji zbadamy, jak osiągnąć podpis cyfrowy, używając algorytmu ECDSA z kluczem prywatnym do odblokowania bitcoinów. Czekajcie na to ekscytujące odkrywanie świata kryptowalut i kryptografii.

## Podpisywanie kluczem prywatnym

![Podpisywanie kluczem prywatnym](https://youtu.be/h2hIyGgPqkM)

Proces podpisu cyfrowego to kluczowa metoda udowodnienia, że jesteś posiadaczem klucza prywatnego, nie ujawniając go. Osiąga się to za pomocą algorytmu ECDSA, który obejmuje określenie unikalnego nonce, obliczenie określonej liczby V oraz stworzenie podpisu cyfrowego składającego się z dwóch części, S1 i S2. Kluczowe jest zawsze używanie unikalnego nonce, aby uniknąć ataków na bezpieczeństwo. Notorycznym przykładem tego, co może się zdarzyć, gdy tej zasady nie przestrzega się, jest przypadek hakowania PlayStation 3, które zostało skompromitowane z powodu ponownego użycia nonce.

Konkretnie, aby zweryfikować podpis cyfrowy za pomocą algorytmu ECDSA (Elliptic Curve Digital Signature Algorithm), zazwyczaj wykonuje się następujące kroki:

1. Zweryfikuj, czy wartości podpisu, S1 i S2, mieszczą się w zakresie [1, n-1]. Jeśli nie, podpis jest nieważny.
2. Oblicz odwrotność S2 mod n. Nazwiemy to u. Często oblicza się to w następujący sposób: u = (S2)^-1 mod n.
3. Oblicz H, która jest wartością hash podpisywanej wiadomości.
4. Oblicz u1 = H _ u mod n i u2 = S1 _ u mod n.
5. Oblicz punkt P na krzywej eliptycznej, używając u1, u2 i klucza publicznego K: P = u1*G + u2*K, gdzie G jest punktem generatora krzywej.
6. Jeśli P jest punktem w nieskończoności, podpis jest nieważny.
7. Oblicz I = współrzędną x punktu P mod n.
8. Podpis jest ważny, jeśli I jest równe S1.

![image](assets/image/section2/10.JPG)
![image](assets/image/section2/11.JPG)

Ważne jest, aby zauważyć, że każde oprogramowanie może używać różnych notacji, a niektóre kroki mogą być łączone lub przestawiane, ale podstawowa logika pozostaje ta sama. Należy również zauważyć, że wszystkie operacje arytmetyczne są wykonywane w skończonym polu określonym przez krzywą eliptyczną (mod n, gdzie n jest rzędem krzywej). Przypominamy, że krzywa secp256k1 (używana w Bitcoinie) ma n = 2^256 - 432420386565659656852420866394968145599.
Jeśli chodzi o generowanie kluczy publicznych i prywatnych, istotne jest zapoznanie się z krzywą eliptyczną i punktem generatora. Aby uzyskać klucz publiczny, należy wybrać losową liczbę jako klucz prywatny, często nazywaną `nonce`, i użyć jej w równaniu krzywej eliptycznej.
Krzywa eliptyczna jest potężnym narzędziem do generowania bezpiecznych kluczy publicznych i prywatnych. Na przykład, aby uzyskać klucz publiczny 3G, rysujesz styczną do punktu G, obliczasz przeciwność -G, aby uzyskać 2G, a następnie dodajesz G i 2G. Aby przeprowadzić transakcję, musisz udowodnić, że znasz liczbę 3, odblokowując bitcoiny powiązane z kluczem publicznym 3G.
Aby stworzyć podpis cyfrowy i udowodnić, że znasz klucz prywatny powiązany z kluczem publicznym 3G, najpierw obliczasz nonce, a następnie punkt V powiązany z tym nonce (w danym przykładzie jest to 4G). Następnie obliczasz punkt T, dodając klucz publiczny 3G i punkt V, co daje 7G.

![image](assets/image/section2/12.JPG)

Weryfikacja podpisu cyfrowego jest kluczowym krokiem w użyciu algorytmu ECDSA, który pozwala potwierdzić autentyczność podpisanego komunikatu bez potrzeby klucza prywatnego nadawcy. Oto jak to działa w szczegółach:

W naszym przykładzie mamy dwie ważne wartości: T i V. T to wartość numeryczna (7 w tym przykładzie), a V to punkt na krzywej eliptycznej (reprezentowany tutaj przez 4G). Te wartości są produkowane podczas tworzenia podpisu cyfrowego i są następnie wysyłane wraz z wiadomością, aby umożliwić weryfikację.

Gdy weryfikator otrzyma wiadomość, otrzyma również te dwie wartości, T i V.

Oto kroki, które weryfikator będzie musiał wykonać, aby zweryfikować podpis:

1. Najpierw obliczą hash wiadomości, który nazwiemy H.
2. Następnie obliczą u1 i u2. Aby to zrobić, użyją następujących wzorów:
   - u1 = H \* (S2)^-1 mod n
   - u2 = T \* (S2)^-1 mod n'

# Mnemoniczna fraza

## Ewolucja portfeli Bitcoin

![Ewolucja portfeli Bitcoin](https://youtu.be/6tmu1R9cXyk)

Hierarchiczny Portfel Deterministyczny, znany bardziej jako portfel HD, odgrywa wybitną rolę w ekosystemie kryptowalut. Termin "portfel" może być mylący dla osób nowych w tej dziedzinie, ponieważ nie oznacza trzymania pieniędzy czy waluty. Raczej odnosi się do zbioru prywatnych kluczy kryptograficznych pochodzących z jednego klucza głównego, dzięki pomysłowemu procesowi arytmetyki algorytmicznej. Te prywatne klucze, które mają stałą długość 256 bitów, są istotą posiadania kryptowaluty i czasami są określane nieco bardziej prozaiczną nazwą "Po prostu Zbioru Kluczy" (JBOC).

![image](assets/image/section3/0.JPG)

Jednak złożoność zarządzania tymi kluczami jest równoważona przez zestaw protokołów, znanych jako Propozycje Ulepszeń Bitcoin (BIPs). Te propozycje ulepszeń są w sercu funkcjonalności i bezpieczeństwa portfeli HD. Na przykład, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), uruchomiony w 2012 roku, zrewolucjonizował sposób generowania i przechowywania tych kluczy, wprowadzając koncepcję deterministycznie i hierarchicznie pochodnych kluczy. To znacznie upraszcza proces zapisywania tych kluczy, jednocześnie utrzymując ich poziom bezpieczeństwa.

![image](assets/image/section3/1.JPG)
Następnie, [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) wprowadził przełomową innowację: frazę mnemoniczną składającą się z 24 słów. Ten system umożliwił przekształcenie skomplikowanej, trudnej do zapamiętania sekwencji cyfr w serię zwykłych słów, znacznie łatwiejszych do zapamiętania i przechowywania. Dodatkowo, [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) zaproponował dodanie dodatkowej frazy hasła w celu wzmocnienia bezpieczeństwa indywidualnych kluczy. Te kolejne ulepszenia doprowadziły do BIP43 i BIP44, które ustandaryzowały strukturę i hierarchię portfeli HD, czyniąc je bardziej dostępnymi i łatwiejszymi w użyciu dla ogółu społeczeństwa.
W następnych sekcjach dokładniej przyjrzymy się, jak działają portfele HD. Omówimy zasady pochodzenia kluczy i zbadamy podstawowe pojęcia entropii i generowania liczb losowych, które są niezbędne do gwarantowania bezpieczeństwa twojego portfela HD.
Hierarchiczny Portfel Deterministyczny, znany bardziej jako portfel HD, odgrywa wybitną rolę w ekosystemie kryptowalut. Termin "portfel" może być mylący dla osób nowych w tej dziedzinie, ponieważ nie oznacza posiadania pieniędzy czy waluty. Odnosi się raczej do zbioru prywatnych kluczy kryptograficznych pochodzących z jednego klucza głównego, dzięki pomysłowemu procesowi arytmetyki algorytmicznej. Te prywatne klucze, które mają stałą długość 256 bitów, są istotą posiadania kryptowalut i czasami określane są nieco prostacką nazwą "Just a Bunch Of Keys" (JBOC).

![image](assets/image/section3/0.JPG)

Jednakże, złożoność zarządzania tymi kluczami jest równoważona przez zestaw protokołów, znanych jako Propozycje Ulepszeń Bitcoina (BIPs). Te propozycje ulepszeń stanowią rdzeń funkcjonalności i bezpieczeństwa portfeli HD. Na przykład, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), uruchomiony w 2012 roku, zrewolucjonizował sposób generowania i przechowywania tych kluczy, wprowadzając koncepcję deterministycznie i hierarchicznie pochodnych kluczy. To znacznie upraszcza proces zapisywania tych kluczy, jednocześnie utrzymując ich poziom bezpieczeństwa.![image](assets/image/section3/1.JPG)

Podsumowując, istotne jest podkreślenie centralnej roli BIP32 i BIP39 w projektowaniu i bezpieczeństwie portfeli HD. Te protokoły umożliwiają generowanie wielu kluczy z jednego ziarna, które ma być liczbą losową lub pseudolosową. Dziś te standardy są przyjęte przez większość portfeli kryptowalutowych, niezależnie od tego, czy są one dedykowane pojedynczej kryptowalucie, czy obsługują wiele rodzajów walut.

Mam nadzieję, że to wprowadzenie pomogło ci lepiej zrozumieć podstawy portfeli HD i ich różne charakterystyki. Naszym celem jest pomóc ci opanować te kluczowe koncepcje i poruszać się bardziej efektywnie w skomplikowanym świecie kryptowalut. Więc zostań z nami, gdy będziemy kontynuować eksplorację zawiłości i niuansów tego fascynującego świata w nadchodzących lekcjach.

## Entropia i Generowanie Liczb Losowych

![Entropia i Generowanie Liczb Losowych](https://youtu.be/k18yH18w2TE)
Znaczenie bezpieczeństwa klucza prywatnego w ekosystemie Bitcoina jest niezaprzeczalne. Są one rzeczywiście kamieniem węgielnym, który zapewnia bezpieczeństwo transakcji Bitcoin. Aby uniknąć jakiejkolwiek podatności związanej z przewidywalnością, te klucze muszą być generowane w sposób całkowicie losowy, co może szybko stać się żmudnym zadaniem dla użytkownika. Jednym z rozwiązań tej zagadki jest Hierarchiczny Portfel Deterministyczny, czyli portfel HD. Ta metoda pozwala na deterministyczne i hierarchiczne generowanie par kluczy potomnych z pojedynczego elementu informacji u podstawy portfela. To tutaj losowość staje się kluczowa, aby zagwarantować bezpieczeństwo pochodnych kluczy.
![image](assets/image/section3/2.JPG)

Generowanie liczb losowych jest rzeczywiście kluczowym elementem w kryptografii, aby zapewnić integralność kluczy prywatnych. Aby zapobiec jakiejkolwiek podatności związanej z przewidywalnością, klucz prywatny musi być produkowany losowo. Użycie nowej pary kluczy dla każdej transakcji dodatkowo zwiększa bezpieczeństwo, chociaż komplikuje ich kopię zapasową i tylko częściowo zachowuje poufność. Podsumowując, bezpieczeństwo kluczy prywatnych jest absolutnym priorytetem, wymagającym rygorystycznego i losowego generowania. Portfele HD oferują rozwiązanie ułatwiające generowanie i zarządzanie kluczami, jednocześnie utrzymując wysoki poziom bezpieczeństwa.

Jednak generowanie liczb losowych na komputerach stanowi znaczące wyzwanie, ponieważ uzyskane wyniki nie są prawdziwie losowe. Dlatego istotne jest użycie Generatora Liczb Losowych (RNG). Typy RNG różnią się, począwszy od Pseudo-Losowych Generatorów Liczb (PRNG) po Prawdziwe Generatory Liczb Losowych (TRNG), jak również PRNG, które włączają źródło entropii.

![image](assets/image/section3/3.JPG)

W przypadku Bitcoina klucze prywatne są generowane z pojedynczego elementu informacji u podstawy portfela. Ta informacja pozwala na deterministyczne i hierarchiczne wyprowadzanie par kluczy potomnych. Entropia jest fundamentem każdego portfela HD, chociaż nie ma standardu generowania tej losowej liczby. Dlatego generowanie liczb losowych jest głównym zagadnieniem dla zabezpieczenia transakcji Bitcoin.

Faza weryfikacji generowania kluczy jest kluczowa, aby zapewnić bezpieczeństwo i autentyczność generowania liczb losowych, fundamentalny krok w zapobieganiu jakiejkolwiek podatności związanej z przewidywalnością. Zdecydowanie zaleca się używanie portfeli open-source, aby umożliwić tę weryfikację.

Jednak ważne jest, aby zauważyć, że niektóre portfele sprzętowe mogą być "zamkniętego źródła", co uniemożliwia weryfikację generowania liczby losowej. Możliwym obejściem byłoby wygenerowanie własnej frazy mnemonicznej za pomocą kości, chociaż podejście to może przedstawiać pewne ryzyka.

![image](assets/image/section3/4.JPG)

Użycie losowo wygenerowanej frazy hasła może pomóc zminimalizować te ryzyka.

Przykładem zastosowania tej metody jest opcja "rzutu kością" oferowana przez CoinKit do generowania fraz mnemonicznych. Inną możliwością byłoby użycie bardzo dużej początkowej informacji i zredukowanie tej informacji do 256 bitów za pomocą funkcji haszującej SHA-256, zdolnej do generowania dobrej liczby losowej. Ważne jest, aby wspomnieć, że funkcja haszująca SHA-256 opiera się na kolizjach, fałszowaniu oraz atakom na obraz i drugi obraz.

Ostatecznie, losowość odgrywa centralną rolę w kryptografii i informatyce, a zdolność do bezpiecznego generowania losowości jest kluczowa dla zapewnienia bezpieczeństwa kluczy prywatnych i transakcji Bitcoin. Entropia, która jest w sercu portfela Bitcoin HD, jest niezbędna dla jego bezpieczeństwa. W naszej kolejnej lekcji będziemy kontynuować eksplorację tego tematu, zagłębiając się w to, jak entropia przyczynia się do bezpieczeństwa portfeli HD.

## Fraza mnemoniczna

![Fraza mnemoniczna](https://youtu.be/uJERqH9Xp7I)

Bezpieczeństwo portfela Bitcoin jest głównym zmartwieniem wszystkich jego użytkowników. Istotnym sposobem na zapewnienie kopii zapasowej portfela jest wygenerowanie frazy mnemonicznej opartej na entropii i sumie kontrolnej.
![obraz](assets/image/section3/5.JPG)
Entropia jest kamieniem węgielnym bezpieczeństwa portfela HD. Istnieje kilka metod generowania tej entropii, w tym za pomocą generatorów liczb pseudolosowych (PRNGs), generatorów prawdziwie losowych (TRNGs) lub ręcznie. Kluczowe jest, aby ta entropia była losowa lub pseudolosowa, aby zagwarantować bezpieczeństwo portfela.

![obraz](assets/image/section3/6.JPG)

Z drugiej strony, suma kontrolna zapewnia weryfikację dokładności frazy odzyskiwania. Bez tej sumy kontrolnej, błąd w frazie mógłby skutkować utworzeniem innego portfela, a co za tym idzie, utratą środków. Suma kontrolna jest uzyskiwana przez przepuszczenie entropii przez funkcję SHA256 i pobranie pierwszych 8 bitów hasha.

Istnieją różne standardy dla frazy mnemonicznej w zależności od rozmiaru entropii. Najczęściej używany standard dla frazy odzyskiwania składającej się z 24 słów to entropia 256 bitów. Rozmiar sumy kontrolnej jest określany przez podzielenie rozmiaru entropii przez 32.

Na przykład, entropia 256 bitów generuje sumę kontrolną 8 bitów. Konkatenacja entropii i sumy kontrolnej prowadzi następnie do odpowiednich rozmiarów 128 bitów, 160 bitów itd. W zależności od rozmiaru entropii, fraza odzyskiwania będzie składać się z 12 słów dla 128 bitów, 15 słów dla 160 bitów i 24 słów dla 256 bitów.

![obraz](assets/image/section3/7.JPG)

Aby przekształcić bity na frazy, każdy segment jest kojarzony ze słowem z listy 2048 słów. Ważne jest, aby zauważyć, że żadne słowo nie ma takiego samego porządku pierwszych czterech liter.

Istotne jest, aby zrobić kopię zapasową 24-słownej frazy odzyskiwania, aby zachować integralność portfela Bitcoin. Dwa najczęściej używane standardy opierają się na entropii 128 lub 256 bitów i konkatenacji 12 lub 24 słów. Dodanie hasła dodatkowego jest dodatkową opcją zwiększającą bezpieczeństwo portfela.

Podsumowując, generowanie frazy mnemonicznej w celu zabezpieczenia portfela Bitcoin jest kluczowym procesem. Ważne jest, aby przestrzegać standardów frazy mnemonicznej w zależności od rozmiaru entropii. Wykonanie kopii zapasowej 24-słownej frazy odzyskiwania jest kluczowe, aby zapobiec jakiejkolwiek utracie środków. Dziękujemy za uwagę i czekamy na nasz kolejny kurs kryptowalut.

## Hasło dodatkowe

![Hasło dodatkowe](https://youtu.be/dZkOYO7MXwc)

Hasło dodatkowe to dodatkowe hasło, które może być zintegrowane z portfelem Bitcoin, aby zwiększyć jego bezpieczeństwo. Jego użycie jest opcjonalne i zależy od decyzji użytkownika. Dodając arbitralne informacje, które wraz z frazą mnemoniczną pozwalają na obliczenie ziarna portfela, hasło dodatkowe zwiększa jego bezpieczeństwo.

![obraz](assets/image/section3/8.JPG)

Aby wygenerować klucze portfela HD, konieczne są zarówno fraza mnemoniczna, jak i hasło dodatkowe. Hasło dodatkowe jest darmowe i może osiągnąć niemal nieskończony rozmiar. Nie jest ono zawarte w frazie mnemonicznej, która jest standaryzowana i musi spełniać pewne ograniczenia rozmiaru, sumy kontrolnej i kodowania. Atakujący nie może uzyskać dostępu do bitcoinów użytkownika bez znajomości hasła dodatkowego. Hasło dodatkowe odgrywa rolę w konstrukcji i obliczaniu wszystkich kluczy portfela.

Funkcja pbkdf2 jest używana do generowania ziarna z hasła dodatkowego. To ziarno pozwala na wygenerowanie wszystkich par kluczy potomnych portfela. Jeśli hasło dodatkowe zostanie zmienione, portfel Bitcoin staje się całkowicie inny.
Hasło jest niezbędnym narzędziem do zwiększenia bezpieczeństwa portfeli Bitcoin. Może umożliwić stosowanie różnych strategii bezpieczeństwa. Na przykład, może być użyte do tworzenia duplikatów i ułatwienia tworzenia kopii zapasowych frazy mnemonicznej. Może również poprawić bezpieczeństwo portfela, zmniejszając ryzyko związane z losowym generowaniem frazy mnemonicznej.
Skuteczne hasło powinno być długie (20 do 40 znaków) i zróżnicowane (używając wielkich liter, małych liter, cyfr i symboli). Nie powinno być bezpośrednio związane z użytkownikiem lub jego otoczeniem. Bezpieczniej jest użyć losowej sekwencji znaków niż proste słowo jako hasło.

![image](assets/image/section3/9.JPG)

Hasło jest bezpieczniejsze niż proste hasło. Idealne hasło jest długie, zróżnicowane i losowe. Może zwiększyć bezpieczeństwo portfela lub oprogramowania typu hot. Może również być użyte do tworzenia redundantnych i bezpiecznych kopii zapasowych.

Kluczowe jest dbanie o kopie zapasowe hasła, aby uniknąć utraty dostępu do portfela. Hasło jest opcją dla portfela HD. Może być generowane losowo za pomocą kości do gry lub innego pseudo-losowego generatora liczb. Nie zaleca się zapamiętywania hasła lub frazy mnemonicznej.

W naszej następnej lekcji szczegółowo przyjrzymy się funkcjonowaniu ziarna i pierwszej pary kluczy generowanych z niego. Zapraszamy do śledzenia tego kursu, aby kontynuować naukę. Czekamy na Ciebie z niecierpliwością.

# Tworzenie portfeli Bitcoin

## Tworzenie ziarna i klucza głównego

![Tworzenie ziarna i klucza głównego](https://youtu.be/56yAt_JDWhY)

W tej części kursu zbadamy kroki pochodzenia Hierarchicznie Deterministycznego Portfela (HD Wallet), który umożliwia tworzenie i zarządzanie kluczami prywatnymi i publicznymi w sposób hierarchiczny.

![image](assets/image/section4/0.JPG)

Podstawą portfela HD są dwa kluczowe elementy: fraza mnemoniczna i hasło (opcjonalne dodatkowe hasło). Razem stanowią one ziarno, 512-bitową sekwencję alfanumeryczną, która służy jako podstawa do wyprowadzania kluczy portfela. Z tego ziarna możliwe jest wyprowadzenie wszystkich par kluczy potomnych portfela Bitcoin. Ziarno jest kluczem, który daje dostęp do wszystkich bitcoinów powiązanych z portfelem, niezależnie od tego, czy używasz hasła, czy nie.

Aby uzyskać ziarno, używana jest funkcja pbkdf2 (Password-Based Key Derivation Function 2) z frazą mnemoniczną i hasłem. Wynik pbkdf2 to 512-bitowe ziarno. Klucz prywatny główny i główny kod łańcucha są określane za pomocą algorytmu HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512). Algorytm ten wymaga wiadomości i klucza do wygenerowania wyniku. Klucz prywatny główny jest obliczany z ziarna i frazy "Bitcoin SEED". Ta fraza jest identyczna dla wszystkich pochodzeń portfela HD, zapewniając spójność między portfelami.

![image](assets/image/section4/1.JPG)

Początkowo funkcja SHA-512 nie była wdrożona w protokole Bitcoin, dlatego używany jest HMAC SHA-512. Użycie HMAC SHA-512 z frazą "Bitcoin SEED" ogranicza użytkownika do generowania portfela specyficznego dla Bitcoina. Wynik HMAC SHA-512 to 512-bitowa liczba, podzielona na dwie części: lewych 256 bitów reprezentuje klucz prywatny główny, podczas gdy prawych 256 bitów reprezentuje główny kod łańcucha.
Klucz prywatny główny jest kluczem nadrzędnym wszystkich przyszłych kluczy w portfelu, podczas gdy główny kod łańcucha jest zaangażowany w wyprowadzanie kluczy potomnych. Ważne jest, aby zauważyć, że niemożliwe jest wyprowadzenie pary kluczy potomnych bez znajomości odpowiadającego kodu łańcucha pary nadrzędnej. Kod łańcucha dodaje źródło entropii do procesu wyprowadzania.

Para kluczy w portfelu składa się z klucza prywatnego, klucza publicznego i kodu łańcucha. Kod łańcucha umożliwia wprowadzenie losowości w procesie wyprowadzania kluczy potomnych i izoluje każdą parę kluczy, aby zapobiec wyciekom informacji.

![image](assets/image/section4/2.JPG)

Ważne jest, aby podkreślić, że klucz prywatny główny jest pierwszym kluczem prywatnym wyprowadzonym z ziarna i nie ma żadnego połączenia z rozszerzonymi kluczami portfela. Dlatego ziarno jest podstawowym elementem do wyprowadzania wszystkich kluczy portfela. Różni się to od frazy mnemonistycznej i hasła, które są używane do tworzenia ziarna.

W następnej lekcji szczegółowo zbadamy rozszerzone klucze, takie jak xPub, xPRV, zPub, i zrozumiemy, dlaczego są używane i jak są konstruowane.

## Rozszerzone Klucze

![Rozszerzone Klucze](https://youtu.be/TRz760E_zUY)

W tej części lekcji zbadamy rozszerzone klucze (xPub, zPub, yPub) i ich prefiksy, które odgrywają ważną rolę w wyprowadzaniu kluczy potomnych w portfelu HD (Hierarchicznie Deterministycznym).

![image](assets/image/section4/3.JPG)

Rozszerzone klucze różnią się od kluczy głównych. Portfel HD generuje frazę mnemonistyczną i ziarno, aby uzyskać klucz główny i główny kod łańcucha. Rozszerzone klucze są używane do wyprowadzania kluczy potomnych i wymagają zarówno klucza nadrzędnego, jak i odpowiadającego kodu łańcucha. Rozszerzony klucz łączy te dwie informacje, aby uprościć proces wyprowadzania.

Rozszerzone klucze są identyfikowane przez specyficzne prefiksy (XPRV, XPUB, YPUB, ZPUB), które wskazują, czy jest to rozszerzony klucz prywatny czy publiczny, oraz ich konkretny cel. Metadane związane z rozszerzonym kluczem obejmują wersję (prefiks), głębokość, odcisk palca klucza publicznego, indeks i ładunek (kod łańcucha i klucz nadrzędny).

![image](assets/image/section4/4.JPG)

Ładunek składa się z kodu łańcucha (32 bajty) i klucza nadrzędnego (33 bajty). Te elementy są niezbędne do wyprowadzania kluczy potomnych. Klucz prywatny jest generowany z liczby losowej lub pseudolosowej, podczas gdy klucz publiczny jest generowany za pomocą algorytmu ECDSA (Elliptic Curve Digital Signature Algorithm).

Każda para rozszerzonych kluczy jest związana z unikalnym kodem łańcucha, co umożliwia specyficzne wyprowadzenia. Łącząc klucz nadrzędny z kodem łańcucha, uzyskuje się rozszerzony klucz prywatny lub publiczny.

![image](assets/image/section4/5.JPG)

Rozszerzone klucze publiczne mogą być wyprowadzane tylko z normalnych kluczy publicznych potomnych, podczas gdy rozszerzone klucze prywatne mogą być wyprowadzane zarówno z kluczy publicznych, jak i prywatnych potomnych, zarówno przez normalne, jak i utwardzone wyprowadzanie. Używanie rozszerzonych kluczy z prefiksem XPUB umożliwia wyprowadzanie nowych adresów bez powrotu do odpowiadających kluczy prywatnych, zapewniając lepsze bezpieczeństwo. Metadane związane z rozszerzonymi kluczami dostarczają ważnych informacji o ich roli i pozycji w hierarchii kluczy.

Skrócone klucze publiczne mają rozmiar 33 bajtów, podczas gdy nieskrócone klucze publiczne mają 512 bitów. Skrócone klucze publiczne zachowują te same informacje co nieskrócone, ale w zredukowanym rozmiarze. Rozszerzone klucze mają rozmiar 82 bajtów, a ich prefiks jest reprezentowany w bazie 58 przez konwersję szesnastkową. Suma kontrolna jest obliczana za pomocą funkcji haszującej HASH256.

![image](assets/image/section4/6.JPG)
Utworzone pochodne kluczy zaczynają się od indeksów, które są potęgami liczby 2 (2^31). Rozszerzone klucze publiczne pozwalają tylko na pochodzenie normalnych kluczy publicznych dzieci, podczas gdy rozszerzone klucze prywatne pozwalają na pochodzenie dowolnego klucza dziecka. Warto zauważyć, że najczęściej używane prefiksy to xpub i zpub, które odpowiadają odpowiednio standardom legacy oraz segwit v1 i segwit v0.
W naszej następnej lekcji zbadamy pochodzenie par kluczy dzieci, korzystając z wiedzy zdobytej na temat rozszerzonych kluczy oraz głównego klucza portfela.

Podsumowując, rozszerzone klucze odgrywają kluczową rolę w kryptografii i działaniu portfeli HD. Zrozumienie ich zastosowania i obliczeń jest kluczowe, aby zapewnić bezpieczeństwo transakcji i ochronę aktywów cyfrowych. Prefiksy i metadane związane z rozszerzonymi kluczami pozwalają na efektywne wykorzystanie i dokładne pochodzenie niezbędnych kluczy dzieci.

## Pochodzenie Par Kluczy Dzieci

![Pochodzenie Par Kluczy Dzieci](https://youtu.be/FXhI-GmE9Aw)

Następnie omówimy obliczenie ziarna i klucza głównego, które są pierwszymi kluczowymi elementami dla hierarchicznej organizacji i pochodzenia portfela HD (Hierarchical Deterministic Wallet). Ziarno, o długości od 128 do 256 bitów, jest generowane losowo lub z tajnej frazy. Odgrywa ono deterministyczną rolę w pochodzeniu wszystkich innych kluczy. Klucz główny to pierwszy klucz pochodzący z ziarna, który pozwala na pochodzenie wszystkich innych par kluczy dzieci.

Główny kod łańcucha odgrywa ważną rolę w odzyskiwaniu portfela z ziarna. Należy zauważyć, że wszystkie klucze pochodzące z tego samego ziarna będą miały ten sam główny kod łańcucha.

![obraz](assets/image/section4/7.JPG)

Hierarchiczny i deterministyczny portfel (HD wallet) zapewnia bardziej efektywne zarządzanie kluczami i strukturami portfela. Rozszerzone klucze pozwalają na pochodzenie pary kluczy dzieci z pary kluczy rodziców, używając obliczeń matematycznych i specyficznych algorytmów.

Istnieją różne typy par kluczy dzieci, w tym klucze utwardzone i normalne. Rozszerzony klucz publiczny pozwala tylko na pochodzenie normalnych kluczy publicznych dzieci, podczas gdy rozszerzony klucz prywatny pozwala na pochodzenie wszystkich kluczy dzieci, zarówno publicznych, jak i prywatnych, w trybie normalnym lub utwardzonym. Każda para kluczy ma indeks, który odróżnia je od siebie.

![obraz](assets/image/section4/8.JPG)

Pochodzenie kluczy dzieci wykorzystuje funkcję HMAC-SHA512, używając klucza rodzica skonkatenowanego z indeksem i kodem łańcucha związanym z parą kluczy. Normalne klucze dzieci mają indeks w zakresie od 0 do 2 do potęgi 31 minus 1, podczas gdy utwardzone klucze dzieci mają indeks w zakresie od 2 do potęgi 31 do 2 do potęgi 32 minus 1.

![obraz](assets/image/section4/9.JPG)
![obraz](assets/image/section4/10.JPG)

Istnieją dwa typy par kluczy dzieci: utwardzone pary i normalne pary. Proces pochodzenia kluczy dzieci wykorzystuje klucze publiczne do generowania warunków wydatkowania, podczas gdy klucze prywatne są używane do podpisywania. Rozszerzony klucz publiczny pozwala tylko na pochodzenie normalnych kluczy publicznych dzieci, podczas gdy rozszerzony klucz prywatny pozwala na pochodzenie wszystkich kluczy dzieci, zarówno publicznych, jak i prywatnych, w trybie normalnym lub utwardzonym.

![obraz](assets/image/section4/11.JPG)
![obraz](assets/image/section4/12.JPG)

Pochodzenie utwardzone wykorzystuje prywatny klucz rodzica, podczas gdy pochodzenie normalne wykorzystuje publiczny klucz rodzica. Funkcja HMAC-SHA512 jest używana do pochodzenia utwardzonego, podczas gdy pochodzenie normalne wykorzystuje 512-bitowy hash. Publiczny klucz dziecka jest uzyskiwany przez pomnożenie prywatnego klucza dziecka przez generator krzywej eliptycznej.

![obraz](assets/image/section4/13.JPG)
## Struktura Portfela i Ścieżki Pochodzenia

![Struktura Portfela i Ścieżki Pochodzenia](https://youtu.be/etO9UxwyE2I)

W tym rozdziale przyjrzymy się strukturze drzewa pochodzenia w Hierarchicznym Portfelu Deterministycznym (HD Wallet). Już wcześniej zbadaliśmy obliczanie ziarna, klucza głównego oraz pochodzenie par kluczy potomnych. Teraz skupimy się na organizacji kluczy wewnątrz portfela.

Portfel HD używa warstw głębokości do organizacji kluczy. Każde pochodzenie od pary rodzica do pary dziecka odpowiada warstwie głębokości. Głębokość 0 odpowiada kluczowi głównemu i głównemu kodowi łańcucha.

- Głębokość 1 jest używana do wyprowadzania kluczy potomnych dla określonego celu, który jest określony przez indeks. Cele są zgodne ze standardami BIP 84 i Segwit v0/v1.

- Głębokość 2 pozwala na różnicowanie kont dla różnych kryptowalut lub sieci. Pozwala to na organizację portfela na podstawie różnych źródeł środków.

- Głębokość 3 jest używana do organizacji portfela na różne konta, zapewniając bardziej przejrzystą i zorganizowaną strukturę.

- Głębokość 4 odpowiada zewnętrznym i wewnętrznym łańcuchom, które są używane dla adresów przeznaczonych do publicznego komunikowania. Indeks 0 jest powiązany z łańcuchem zewnętrznym, podczas gdy indeks 1 jest powiązany z łańcuchem wewnętrznym. Każde konto ma dwa łańcuchy: zewnętrzny (0) i wewnętrzny (1). Głębokość 4 jest również używana do zarządzania typami skryptów w przypadku portfeli wielopodpisowych.

- Głębokość 5 jest używana dla adresów odbiorczych w standardowym portfelu. W następnej sekcji przyjrzymy się bardziej szczegółowo pochodzeniu par kluczy potomnych.

Dla każdej warstwy głębokości używamy indeksów do różnicowania par kluczy potomnych. Utwierdzone indeksy są używane z apostrofem dla niektórych pochodzeń. Klucz publiczny na rok jest używany jako dane wejściowe dla funkcji HMAC. Indeks w ścieżce pochodzenia wskazuje wartość używaną w funkcji HMAC.
Indeks bez apostrofu odpowiada rzeczywistemu indeksowi używanemu, podczas gdy indeks z apostrofem odpowiada rzeczywistemu indeksowi + 2^31. Wzmocnione pochodzenia używają indeksów od 2^31 do 2^32-1. Na przykład, indeks 44' odpowiada rzeczywistemu indeksowi 2^31 + 44.
Aby wygenerować określony adres odbiorczy, wyprowadzamy parę kluczy potomnych z klucza głównego i głównego kodu łańcucha. Następnie używamy indeksu do różnicowania między różnymi parami kluczy potomnych na tej samej głębokości.

Rozszerzone klucze, takie jak XPUB, pozwalają na udostępnianie portfela wielu osobom. Ścieżka pochodzenia jest używana do różnicowania między łańcuchem zewnętrznym (adresy przeznaczone do komunikacji) a łańcuchem wewnętrznym (adresy reszty).

Ważne jest, aby zauważyć, że różne głębokości są używane w portfelu HD w zależności od różnych standardów. Wyprowadzanie kluczy rodzica do kluczy potomnych pozwala na przejście z jednej głębokości na inną. Użycie różnych gałęzi w portfelu HD wskazuje na różne standardy, które są przestrzegane.

W następnym rozdziale przyjrzymy się adresom odbiorczym, ich zaletom użytkowania oraz krokom zaangażowanym w ich konstrukcji.

# Co to jest adres Bitcoin?

## Adresy Bitcoin

![Adresy Bitcoin](https://youtu.be/nqGBMjPtFNI)
W tym rozdziale zbadamy adresy odbiorcze, które odgrywają kluczową rolę w systemie Bitcoin. Pozwalają one na otrzymywanie środków na monetę i są generowane z par kluczy prywatnych i publicznych. Chociaż istnieje typ skryptu o nazwie Pay2PublicKey, który pozwala na blokowanie bitcoinów do klucza publicznego, użytkownicy generalnie wolą używać adresów odbiorczych zamiast tego skryptu.
![image](assets/image/section5/0.JPG)

Kiedy odbiorca chce otrzymać bitcoiny, podaje adres odbiorczy nadawcy zamiast swojego klucza publicznego. Adres jest tak naprawdę haszem klucza publicznego, z określonym formatem. Klucz publiczny jest pochodną klucza prywatnego dziecka, używając operacji matematycznych takich jak dodawanie punktów i podwajanie na krzywych eliptycznych.

![image](assets/image/section5/1.JPG)

Ważne jest, aby zauważyć, że nie jest możliwe odwrócenie z adresu na klucz publiczny, ani z klucza publicznego na klucz prywatny. Używanie adresu pomaga zmniejszyć rozmiar informacji o kluczu publicznym, który początkowo wynosi 512 bitów. Możliwe jest skompresowanie klucza publicznego, zachowując tylko wartość x i dodając prefiks, ale ta technika nie była znana w czasie powstania Bitcoina. Dlatego używanie adresu nie oszczędza miejsca w blokach.

## Jak stworzyć adres Bitcoin?

![Jak stworzyć adres Bitcoin?](https://youtu.be/ewMGTN8dKjI)

W tym rozdziale omówimy konstrukcję adresu odbiorczego dla transakcji Bitcoin. Adres odbiorczy to alfanumeryczna reprezentacja skompresowanego klucza publicznego. Konwersja klucza publicznego na adres odbiorczy przechodzi przez kilka etapów.

![image](assets/image/section5/3.JPG)

Jedną z korzystnych cech adresów odbiorczych jest obecność sumy kontrolnej, która pozwala na wykrywanie błędów. W tym celu używamy technologii sumy kontrolnej BCH (Bose-Chaudhuri-Hocquenghem), która zapewnia dokładne wykrywanie błędów. Ta technologia przyczynia się również do zmniejszenia liczby znaków wymaganych do reprezentowania adresu, co ułatwia jego użycie.

Aby rozpocząć budowanie adresu, musimy skompresować odpowiadający mu klucz publiczny. Surowy klucz publiczny zajmuje 520 bitów, ale dzięki symetrii używanej krzywej eliptycznej, krzywa eliptyczna może mieć współrzędną x związaną z dwoma możliwymi wartościami dla y: dodatnią lub ujemną. W sieci Bitcoin pracujemy z skończonym zbiorem liczb całkowitych dodatnich, a nie ze zbiorem liczb rzeczywistych. Aby reprezentować klucz publiczny z x, dodajemy prefiks wskazujący wartość y (parzystą lub nieparzystą). Kompresowanie klucza publicznego redukuje jego rozmiar z 520 do 264 bitów. Parzystość y w skończonym zbiorze liczb całkowitych dodatnich odpowiada parzystości y w zbiorze liczb rzeczywistych.

![image](assets/image/section5/4.JPG)
![image](assets/image/section5/5.JPG)

Weźmy na przykład klucz publiczny należący do Satoshi Nakamoto, z prefiksem 0,3 wskazującym nieparzystą wartość y. Możemy wtedy przejść do drugiego etapu konstruowania adresu z kompresowanych kluczy publicznych. Możliwe jest obliczenie dwóch adresów dla każdego klucza publicznego. W tym celu używamy funkcji SHA256, aby uzyskać hasz klucza publicznego. Następnie stosujemy funkcję ripemd160 do wyniku SHA256, aby uzyskać ciąg znaków. Ten ciąg jest następnie kodowany w formacie binarnym w grupach po 5 bitów, do których dodaje się metadane do obliczenia sumy kontrolnej przy użyciu programu BCH.

![image](assets/image/section5/6.JPG)
W przypadku adresów dziedzicznych używamy podwójnego haszowania SHA256 do wygenerowania sumy kontrolnej adresu. Jednak dla adresów Segwit V0 i V1 polegamy na technologii sumy kontrolnej BCH, aby zapewnić wykrywanie błędów. Program BCH jest zdolny do sugerowania i korygowania błędów z niezwykle niskim prawdopodobieństwem błędu. Obecnie program BCH jest używany do wykrywania i sugerowania modyfikacji, ale nie dokonuje ich automatycznie w imieniu użytkownika. Obliczanie sumy kontrolnej za pomocą kodu BCH opiera się na arytmetyce wielomianowej Chien-Chauffage.
![image](assets/image/section5/7.JPG)

Program BCH wymaga kilku informacji wejściowych, w tym HRP (Human Readable Part), który musi zostać rozszerzony. Rozszerzenie HRP polega na kodowaniu każdej litery w bazie 2, wzięciu pierwszych trzech bitów każdego znaku przez wstawienie separatora 0, a następnie skonkatenowaniu ostatnich pięciu bitów każdego znaku. Niebieskie znaki przekonwertowane na bazę 10 odpowiadają 3 i 3 w systemie dziesiętnym, podczas gdy pięć innych pomarańczowych znaków odpowiada 2 i 3 w bazie 10. Rozszerzenie HRP w bazie 10 pozwala na izolację ostatnich pięciu bitów każdego znaku, wzmacniając tym samym sumę kontrolną.

![image](assets/image/section5/8.JPG)

Wersja Segwit V0 jest reprezentowana przez kod 00, a "payload" jest w kolorze czarnym, w bazie 10. Następuje sześć znaków zarezerwowanych dla sumy kontrolnej. Dane zawierające metadane są następnie przekazywane do programu BCH, aby uzyskać sumę kontrolną w bazie 10. Skonkatenowanie wersji, payloadu i sumy kontrolnej pozwala na zbudowanie adresu. Znaki w bazie 10 są następnie konwertowane na znaki bech32 za pomocą tabeli mapowania. Alfabet bech32 obejmuje wszystkie znaki alfanumeryczne, z wyjątkiem 1, b, i oraz o, aby uniknąć zamieszania.

![image](assets/image/section5/9.JPG)
![image](assets/image/section5/10.JPG)

Aby zbudować adres zaczynający się od bc1q, musimy zastosować funkcję haszującą (H160) do skompresowanego klucza publicznego, a następnie dodać sumę kontrolną, wersję (q), HRP (bc) i separator (1). Z drugiej strony, adresy Taproot zaczynają się od bc1p, ponieważ ich wersja (Segwit V1) odpowiada 0+1=1, stąd użycie znaku p. Wszystkie te elementy są następnie konwertowane na BCH32, wariant Bitcoin-specific base 32.

W ten sposób przeszliśmy przez etapy konstruowania adresu odbiorczego, użycie technologii sumy kontrolnej BCH, jak również konstrukcję adresu zaczynającego się od bc1q lub bc1p przy użyciu wariantu BCH32 Bitcoin-specific base 32.

## Podsumowanie kryptografii dla portfeli Bitcoin

![training summary](https://youtu.be/NkAYoVUMvOs)

W trakcie tego szkolenia szczegółowo zbadaliśmy Hierarchiczny Deterministyczny (HD) portfel z BIP32. Entropia odgrywa centralną rolę w tym typie portfela, ponieważ jest używana do generowania frazy mnemonicznej z losowej liczby. Dzięki liście 2048 słów dostarczonych w BIP39, tę frazę mnemoniczną można zakodować w serię łatwych do zapamiętania słów. Frazy mnemoniczna wraz z opcjonalną frazą hasła jest niezbędna do wygenerowania ziarna portfela. Fraza hasła działa jako kryptograficzna sól, dodając dodatkową warstwę ochrony do portfela.

![image](assets/image/section5/11.JPG)
Funkcja pbkdf2 jest używana do generowania ziarna z frazy mnemonicznej i hasła, używając hmacha512 i 2048 iteracji. Klucz główny i główny kod łańcucha są następnie wyprowadzane z tego ziarna, używając ponownie funkcji hmacha512 z frazą "bitcoin seed". Klucz prywatny główny i główny kod łańcucha są najwyższymi elementami w hierarchii portfela HD.
![image](assets/image/section5/12.JPG)

Wyprowadzenie klucza potomnego zależy od kilku czynników, w tym od klucza rodzica i odpowiadającego mu kodu łańcucha. Rozszerzony klucz jest uzyskiwany przez połączenie klucza rodzica z jego kodem łańcucha, podczas gdy klucz główny jest oddzielnym kluczem. Aby wyprowadzić adres, skompresowany klucz publiczny jest najpierw haszowany przy użyciu SHA256 i RIPMD160, a następnie obliczany jest sum kontrolna. Podwójne haszowanie SHA256 jest używane do obliczenia sumy kontrolnej w przypadku standardu legacy, podczas gdy program BCH (Bose-Chaudhuri-Hocquenghem) jest używany do obliczenia sumy kontrolnej w przypadku standardu segwit. Następnie, reprezentacja w formacie base 58 jest używana dla standardu legacy, podczas gdy format bech32 jest używany dla standardu segwit, aby uzyskać adres portfela HD.

![image](assets/image/section5/13.JPG)

Podsumowując, szczegółowo zbadaliśmy funkcje haszujące i ich charakterystykę, jak również cyfrowe podpisy i krzywe eliptyczne. Następnie zagłębiliśmy się w świat Hierarchicznych Portfeli Deterministycznych (HD) z BIP32, używając entropii i hasła do generowania ziarna portfela. Nauczyliśmy się również, jak wyprowadzać klucze potomne i uzyskać adres portfela HD. Mam nadzieję, że te informacje były dla Ciebie pomocne i teraz zachęcam Cię do przejścia do oceny, aby przetestować wiedzę zdobytą podczas kursu Crypto 301. Dziękuję za uwagę.

# Idź dalej

## Tworzenie ziarna z 128 rzutów kostką!

![Tworzenie ziarna z 128 rzutów kostką!](https://youtu.be/lUw-1kk75Ok)

Tworzenie frazy mnemonicznej jest kluczowym krokiem w zabezpieczaniu Twojego portfela kryptowalutowego. Istnieje kilka metod generowania frazy mnemonicznej, jednak skupimy się na manualnej metodzie generowania przy użyciu kostki. Ważne jest, aby zauważyć, że ta metoda nie jest odpowiednia dla portfela o wysokiej wartości. Zaleca się używanie oprogramowania open-source lub portfela sprzętowego do generowania frazy mnemonicznej. Aby stworzyć frazę mnemoniczną, użyjemy kostki do generowania informacji binarnych. Celem jest zrozumienie procesu tworzenia frazy mnemonicznej.

**Krok 1 - Przygotowanie:**
Upewnij się, że masz zainstalowaną amnezyczną dystrybucję Linuxa, taką jak Tails OS, na pendrive'ie dla dodatkowego bezpieczeństwa. Zauważ, że ten poradnik nie powinien być używany do tworzenia głównego portfela.

**Krok 2 - Generowanie losowej liczby binarnej:**
Użyjemy kostki do generowania informacji binarnych. Rzuć kostką 128 razy i zanotuj każdy wynik (1 dla nieparzystych, 0 dla parzystych).

**Krok 3 - Organizowanie liczb binarnych:**
Organizuj uzyskane liczby binarne w rzędy po 11 cyfr, aby ułatwić dalsze obliczenia. Dwunasty rząd powinien mieć tylko 7 cyfr.

**Krok 4 - Obliczanie sumy kontrolnej:**
Ostatnie 4 cyfry dla dwunastego wiersza odpowiadają sumie kontrolnej. Aby obliczyć tę sumę kontrolną, musimy użyć terminala z dystrybucji Linuxa. Zaleca się użycie [TailOs](https://tails.boum.org/index.fr.html), który jest dystrybucją bez pamięci, uruchamianą z napędu USB. Po uruchomieniu terminala, wprowadź polecenie `echo <liczba binarna> | shasum -a 254 -0`. Zastąp `<liczba binarna>` swoją listą 128 zer i jedynek. Wynikiem jest szesnastkowy hash. Zanotuj pierwszy znak tego hasha i przekonwertuj go na binarny. Możesz użyć tej [tabeli](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) w celu pomocy. Dodaj binarną sumę kontrolną (4 cyfry) do dwunastego wiersza swojego arkusza.

**Krok 5 - Konwersja na dziesiętne:**
Aby znaleźć słowa powiązane z każdym z twoich wierszy, najpierw musisz przekonwertować każdą serię 11 bitów na liczby dziesiętne. Tutaj nie możesz użyć konwertera online, ponieważ te bity reprezentują twoją frazę mnemoniczną. Więc będziesz musiał przekonwertować używając kalkulatora i pewnego triku, jak następuje: każdy bit jest powiązany z potęgą 2, więc od lewej do prawej mamy 11 rang odpowiadających 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Aby przekonwertować twoją serię 11 bitów na dziesiętne, wystarczy dodać rangi, które zawierają 1. Na przykład, dla serii 00110111011, odpowiada to następującemu dodaniu: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Teraz możesz przekonwertować każdy wiersz na dziesiętne. I zanim przejdziesz do kodowania na słowa, musisz dodać +1 do wszystkich wierszy, ponieważ indeks listy słów BIP39 zaczyna się od 1, a nie od 0.

**Krok 8 - Generowanie frazy mnemonicznej:**
Zacznij od wydrukowania [listy 2048 słów](https://seedxor.com/files/wordlist.pdf), aby przekonwertować między twoimi liczbami dziesiętnymi a słowami BIP39. Cechą charakterystyczną tej listy jest to, że żadne słowo nie ma wspólnych pierwszych 4 liter ze wszystkimi innymi słowami w tym słowniku. Następnie, dla każdego z twoich wierszy, poszukaj słowa powiązanego z liczbą dziesiętną.

**Krok 9 - Testowanie frazy mnemonicznej:**
Natychmiast przetestuj swoją frazę mnemoniczną na Sparrow Wallet, tworząc z niej portfel. Jeśli otrzymasz błąd nieprawidłowej sumy kontrolnej, prawdopodobnie popełniłeś błąd w obliczeniach. Popraw ten błąd, wracając do kroku 4 i testuj ponownie na Sparrow Wallet. Oto i ty! Właśnie stworzyłeś nowy portfel Bitcoin z 128 rzutów kostką.

Generowanie frazy mnemonicznej jest ważnym procesem w zabezpieczaniu twojego portfela kryptowalutowego. Zaleca się używanie bezpieczniejszych metod, takich jak użycie oprogramowania open source lub portfeli sprzętowych, do generowania frazy mnemonicznej. Jednak ukończenie tego warsztatu pomaga lepiej zrozumieć, jak możemy stworzyć portfel Bitcoin z losowej liczby.

## Podsumowanie i zakończenie

### Podziękowania i kontynuowanie eksploracji

Chcielibyśmy serdecznie podziękować za udział w szkoleniu Crypto 301. Mamy nadzieję, że to doświadczenie było dla ciebie wzbogacające i edukacyjne. Omówiliśmy wiele ekscytujących tematów, od matematyki, przez kryptografię, po działanie protokołu Bitcoin.
Jeśli chcesz zagłębić się dalej w temat, mamy do zaoferowania dodatkowe źródło. Przeprowadziliśmy wyłączny wywiad z Théo Pantamis i Loïc Morel, dwoma renomowanymi ekspertami w dziedzinie kryptografii. Ten wywiad zagłębia się w różne aspekty tematu i oferuje interesujące perspektywy.
Zachęcamy do obejrzenia tego wywiadu, aby kontynuować eksplorację fascynującego świata kryptografii. Mamy nadzieję, że będzie to dla Ciebie użyteczne i inspirujące w Twojej podróży. Jeszcze raz dziękujemy za Twoje uczestnictwo i zaangażowanie podczas tego szkolenia.

### Wspieraj Nas

Ten kurs, wraz ze wszystkimi dostępnymi treściami na tej uniwersytecie, został udostępniony Ci za darmo przez naszą społeczność. Aby nas wspierać, możesz podzielić się nim z innymi, zostać członkiem uniwersytetu, a nawet przyczynić się do jego rozwoju poprzez GitHub. W imieniu całego zespołu, dziękujemy!

### Oceń Szkolenie

System oceniania szkolenia zostanie wkrótce zintegrowany z tą nową platformą E-learningową! W międzyczasie bardzo dziękujemy za udział w kursie i jeśli Ci się podobał, prosimy o rozważenie podzielenia się nim z innymi.