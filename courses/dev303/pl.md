---
name: Nauka Rust z Bitcoin
goal: Rozwijaj swoje umiejętności programowania Rust poprzez kodowanie Bitcoin
objectives: 

  - Przyzwyczaj się do języka Rust
  - Zrozumienie, dlaczego warto używać Rust do rozwijania Bitcoin
  - Uzyskaj podstawy Lightning SDK

---

# Wyprawa Rust dla twórców Bitcoin



W tym praktycznym kursie, który został sfilmowany podczas seminarium zorganizowanego przez Fulgur' Ventures w październiku 2023 r., rozwiniesz swoje umiejętności Rust, budując prawdziwe komponenty i mini-projekty skoncentrowane na Bitcoin. Omówimy podstawy Rust, dlaczego Rust jest używany do rozwoju Bitcoin (bezpieczeństwo pamięci, wydajność i bezpieczna współbieżność) oraz jak rozpocząć pracę z Lightning SDK w celu tworzenia funkcji płatności.


W poszczególnych rozdziałach będziesz ćwiczyć podstawowe wzorce Rust (własność, czas życia, cechy, asynchroniczność), pracować z prymitywami Bitcoin (klucze, transakcje, skrypty) i stopniowo integrować koncepcje Lightning (węzły, kanały, faktury).


Nie jest wymagany żaden wcześniejszy rozwój Rust lub Bitcoin, chociaż znajomość podstawowego programowania pomaga. Kurs jest przyjazny dla początkujących, ale wystarczająco praktyczny dla inżynierów przechodzących do Bitcoin.


+++

# Wprowadzenie

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Przegląd kursu

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Wprowadzenie**


Witamy w tym przyjaznym dla początkujących kursie programowania na temat SDK. W tym szkoleniu poznasz podstawy Rust, a następnie skupisz się na Rust zastosowanym do programowania Bitcoin i zakończysz kilkoma przypadkami użycia przy użyciu SDK.


Filmy ze szkolenia będą na razie dostępne tylko w języku angielskim i były częścią seminarium na żywo zorganizowanego w październiku ubiegłego roku w Toskanii przez Fulgure Venture. To szkolenie skupi się tylko na pierwszym tygodniu. Druga połowa była skierowana do RGB i można ją znaleźć w kursie RGB.


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

To szkolenie daje możliwość rozwijania umiejętności programowania na Lightning Network przy użyciu Rust i różnych zestawów SDK. Jest przeznaczony dla programistów z solidnym zapleczem programistycznym, którzy chcą zagłębić się w rozwój specyficzny dla Lightning Network. Poznasz podstawy Rust, dowiesz się, dlaczego jest on odpowiedni do rozwoju Bitcoin, a następnie przejdziesz do praktycznej implementacji przy użyciu specjalistycznych zestawów SDK.


**Sekcja 2: Nauka kodowania z Rust**

W tej części odkryjesz podstawy Rust poprzez serię progresywnych rozdziałów. Nauczysz się pisać kod Rust, zrozumiesz jego specyfikę i opanujesz jego podstawowe funkcje w siedmiu szczegółowych częściach. Moduł ten jest niezbędny do zrozumienia, dlaczego Rust jest preferowanym językiem do programowania Bitcoin.


**Sekcja 3: Rust i Bitcoin**

Tutaj dogłębnie zbadamy, dlaczego Rust jest odpowiednim wyborem dla rozwoju Bitcoin. Dowiesz się o jego modelu błędów, narzędziu UniFFI i cechach asynchronicznych - wszystkich kluczowych elementach w budowaniu solidnego i bezpiecznego oprogramowania.


**Sekcja 4: Rozwój LNP/BP za pomocą SDK**

Dowiesz się, jak rozwijać węzły LN przy użyciu różnych zestawów SDK, takich jak Breez SDK i Greenlight dla Lipa. Zobaczysz, jak zaimplementować aplikacje Lightning Network przy użyciu bibliotek zaprojektowanych w celu uproszczenia rozwoju Bitcoin i Lightning.


Gotowy, aby rozwinąć swoje umiejętności Lightning Network z Rust? Do dzieła!

# Naucz się kodować z książką o rdzy

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Wprowadzenie do Rust

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Instalacja i zarządzanie Rust za pomocą Rustup


Rozpoczynając swoją przygodę z Rust, pierwszym krokiem jest skonfigurowanie odpowiedniego środowiska programistycznego. Najbardziej zalecanym podejściem do instalacji Rust jest Rustup, system zarządzania toolchainem, który obsługuje instalację i aktualizacje w różnych projektach i platformach.


Rustup służy jako coś więcej niż tylko instalator - działa jako kompleksowe narzędzie do zarządzania środowiskiem programistycznym Rust. Dzięki Rustup można łatwo zainstalować dodatkowe cele kompilacji dla różnych platform, takich jak ARM64 dla rozwoju Androida lub innych architektur, które mogą wymagać wsparcia. Narzędzie płynnie obsługuje również aktualizacje Rust, co jest szczególnie cenne, biorąc pod uwagę, że Rust wydaje nową stabilną wersję mniej więcej co sześć tygodni. Gdy trzeba zaktualizować oprogramowanie do najnowszej wersji, proste polecenie `rustup update` załatwia wszystko automatycznie.


Podczas instalacji Rustup warto zrozumieć model bezpieczeństwa. Proces instalacji pobiera i wykonuje skrypt z oficjalnej strony Rust za pośrednictwem protokołu HTTPS, który zapewnia bezpieczeństwo kryptograficzne warstwy transportowej. Pakiety pobierane przez Rustup i Cargo pochodzą z zaufanych źródeł (crates.io i oficjalna infrastruktura Rust) i korzystają z szyfrowania HTTPS. Chociaż takie podejście jest bezpieczne dla większości scenariuszy programistycznych, niektóre organizacje o ścisłej polityce bezpieczeństwa mogą preferować instalację Rust za pośrednictwem menedżera pakietów swojej dystrybucji Linuksa, który zapewnia dodatkową warstwę zaufania dzięki własnej infrastrukturze podpisywania pakietów. Do celów edukacyjnych i ogólnego rozwoju, Rustup jest dobrze ugruntowanym i powszechnie zaufanym narzędziem w ekosystemie Rust.


W przypadku większości scenariuszy programistycznych można zainstalować Rustup, uruchamiając skrypt instalacyjny udostępniony na oficjalnej stronie Rust. Instalator wyświetli monit o wybór między różnymi opcjami toolchain, przy czym stabilny toolchain jest zalecanym wyborem dla większości użytkowników. Instalacja odbywa się w katalogu domowym, nie wymaga uprawnień administratora i ustawia wszystkie niezbędne zmienne środowiskowe do natychmiastowego użycia.


### Zrozumienie łańcuchów narzędzi i komponentów Rust


Ekosystem programistyczny Rust składa się z kilku kluczowych komponentów, które współpracują ze sobą, aby zapewnić kompletne środowisko programistyczne. Zrozumienie tych komponentów pomaga skuteczniej poruszać się po procesie programowania Rust i rozwiązywać problemy, gdy się pojawią.


Kompilator Rust, znany jako `rustc`, stanowi rdzeń łańcucha narzędzi Rust. Chociaż teoretycznie można użyć `rustc` bezpośrednio do kompilacji programów Rust, większość prac rozwojowych opiera się na Cargo, menedżerze pakietów Rust i systemie kompilacji. Cargo działa podobnie do npm w ekosystemie JavaScript, zarządzając zależnościami, koordynując kompilacje i zapewniając wygodne polecenia dla typowych zadań programistycznych. Po uruchomieniu poleceń takich jak `cargo build` lub `cargo run`, Cargo orkiestruje proces kompilacji, obsługuje rozwiązywanie zależności i zarządza ogólną strukturą projektu.


Clippy to linter, który analizuje kod i dostarcza sugestie dotyczące ulepszeń. W przeciwieństwie do podstawowych narzędzi do sprawdzania składni, Clippy rozumie idiomy Rust i może zalecić bardziej idiomatyczne sposoby wykonywania określonych zadań. Narzędzie to pomaga w nauce najlepszych praktyk Rust i pisaniu łatwiejszego w utrzymaniu kodu.


Łańcuch narzędzi Rust obejmuje również kompleksowe narzędzia dokumentacyjne oraz dokumentację biblioteki standardowej, dostępną za pośrednictwem oficjalnej strony internetowej z dokumentacją Rust. Dokumentacja ta służy jako niezbędny punkt odniesienia podczas programowania, dostarczając szczegółowych informacji na temat standardowych funkcji bibliotecznych, typów i modułów. Dokumentacja zawiera obszerne przykłady i objaśnienia, które pomagają zrozumieć nie tylko działanie funkcji, ale także sposób ich efektywnego wykorzystania w programach.


Rust obsługuje wiele kanałów wydań: stabilny, beta i nightly. Kanał stabilny zapewnia dokładnie przetestowane wydania odpowiednie do użytku produkcyjnego. Kanał beta oferuje podgląd następnego stabilnego wydania, używanego głównie do ostatecznych testów przed oficjalnym wydaniem. Kanał nightly zawiera eksperymentalne funkcje w trakcie aktywnego rozwoju, które mogą być przydatne do wypróbowania nowych możliwości Rust, choć funkcje te mogą ulec zmianie lub zostać usunięte w przyszłych wydaniach.


### Tworzenie i zarządzanie projektami Rust za pomocą Cargo


Nowoczesny rozwój Rust koncentruje się wokół Cargo, które usprawnia tworzenie projektów, zarządzanie zależnościami i proces kompilacji. Zamiast ręcznie tworzyć katalogi i pliki, Cargo udostępnia komendę `cargo new` do generate kompletnej struktury projektu z rozsądnymi wartościami domyślnymi.


Po utworzeniu nowego projektu za pomocą `cargo new project_name`, Cargo ustanawia standardową strukturę katalogów, tworzy podstawowy plik `main.rs` z programem "Hello, world!", inicjuje repozytorium Git i generuje plik `Cargo.toml` do konfiguracji projektu. Plik `Cargo.toml` służy jako centralny punkt konfiguracji projektu, zawierający metadane o projekcie i listę wszystkich zależności wymaganych przez kod.


Cargo zapewnia kilka niezbędnych poleceń do codziennej pracy programistycznej. Polecenie `cargo build` kompiluje projekt i jego zależności, tworząc pliki wykonywalne w katalogu `target`. Dla szybkiej iteracji podczas rozwoju, `cargo run` łączy budowanie i wykonywanie w jednym kroku. Polecenie `cargo check` wykonuje wszystkie kontrole kompilacji bez generowania końcowego pliku wykonywalnego, dzięki czemu jest znacznie szybsze niż pełna kompilacja, gdy chcesz po prostu sprawdzić, czy kod kompiluje się poprawnie.


Podczas przygotowywania kodu do wdrożenia produkcyjnego, flaga `--release` włącza optymalizacje i usuwa asercje debugowania. Wersje release działają szybciej i tworzą mniejsze pliki wykonywalne, ale ich kompilacja trwa dłużej i usuwają one pomocne informacje debugowania. Kompilator stosuje różne optymalizacje podczas kompilacji release i wyłącza kontrole runtime, takie jak wykrywanie przepełnienia liczb całkowitych, co poprawia wydajność, ale usuwa niektóre gwarancje bezpieczeństwa obecne w kompilacjach debugowania.


### Zmienne, zmienność i filozofia bezpieczeństwa Rust


Rust przyjmuje inne podejście do zarządzania zmiennymi niż większość języków. Domyślnie wszystkie zmienne w Rust są niezmienne, co oznacza, że ich wartości nie mogą zostać zmienione po początkowym przypisaniu. Ta decyzja projektowa ma na celu zapobieganie typowym błędom programistycznym, które powstają w wyniku nieoczekiwanych zmian stanu.


Po zadeklarowaniu zmiennej za pomocą `let x = 5`, zmienna ta staje się domyślnie niezmienna. Każda późniejsza próba modyfikacji jej wartości spowoduje błąd kompilacji. Ten wymóg niezmienności zmusza programistów do dokładnego przemyślenia, kiedy zmiany stanu są naprawdę konieczne i sprawia, że zachowanie kodu jest bardziej przewidywalne. Wiele błędów programistycznych wynika z nieoczekiwanych zmian zmiennych, a domyślna niezmienność Rust pomaga zapobiegać takim problemom.


Gdy naprawdę trzeba zmodyfikować wartość zmiennej, Rust wymaga jawnej deklaracji mutowalności przy użyciu słowa kluczowego `mut`: `let mut x = 5`. Ta wyraźna deklaracja służy jako wyraźny sygnał zarówno dla kompilatora, jak i innych programistów, że wartość tej zmiennej może ulec zmianie podczas wykonywania programu. Wymóg jawnego zadeklarowania mutowalności zachęca do przemyślenia, czy mutowalność jest naprawdę konieczna dla każdej zmiennej.


Rust obsługuje również shadowing, który pozwala zadeklarować nową zmienną o tej samej nazwie, co poprzednia zmienna. W przeciwieństwie do mutacji, shadowing tworzy zupełnie nową zmienną, która ma tę samą nazwę, skutecznie ukrywając poprzednią zmienną. Technika ta okazuje się szczególnie przydatna podczas przekształcania danych w wielu krokach, takich jak parsowanie ciągu znaków na liczbę, a następnie dalsze przetwarzanie tej liczby. Dzięki shadowingowi można zachować spójną nazwę zmiennej w całym procesie transformacji, jednocześnie zmieniając typ zmiennej na każdym kroku.


Rozróżnienie między shadowingiem a mutacją staje się ważne przy rozważaniu zmian typu. W przypadku shadowingu można zmienić zarówno wartość, jak i typ zmiennej, ponieważ tworzona jest nowa zmienna. W przypadku mutacji można zmienić tylko wartość, zachowując ten sam typ, ponieważ modyfikujemy istniejącą zmienną, a nie tworzymy nową.


```rust
// Shadowing: creating new variables with the same name
let amount = "100000";           // amount is a &str (string slice)
let amount = amount.parse::<u64>().unwrap();  // amount is now u64
let amount = amount * 100;       // amount is still u64, new value

// Mutation: modifying the same variable
let mut balance = 50000_u64;
balance = balance + amount;      // OK: same type, different value
// balance = "empty";            // ERROR: cannot change type with mutation

// Practical example: processing a Bitcoin amount input
let user_input = "  0.001 ";                    // &str with whitespace
let user_input = user_input.trim();            // &str, whitespace removed
let satoshis: u64 = (user_input.parse::<f64>().unwrap() * 100_000_000.0) as u64;
println!("Amount in satoshis: {}", satoshis);  // 100000
```


### Typy danych i podstawy systemu typów


Rust implementuje silny, statyczny system typów, w którym każda wartość musi mieć dobrze zdefiniowany typ znany w czasie kompilacji. Choć może się to wydawać restrykcyjne w porównaniu do języków dynamicznie typowanych, możliwości Rust w zakresie wnioskowania o typie oznaczają, że rzadko trzeba jawnie określać typy. Kompilator może zwykle określić odpowiedni typ na podstawie sposobu użycia wartości.


Jednakże, niektóre sytuacje wymagają jawnych adnotacji typu. Podczas korzystania z funkcji generycznych, takich jak `parse()`, które mogą konwertować ciągi znaków na różne typy liczbowe, kompilator musi wiedzieć, o jaki konkretny typ chodzi. W takich przypadkach, należy podać adnotacje typu używając składni dwukropka: `let guess: u32 = "42".parse().expect("Not a number!")`.


Typy skalarne Rust obejmują liczby całkowite, zmiennoprzecinkowe, logiczne i znaki. System typów całkowitych zapewnia precyzyjną kontrolę nad wykorzystaniem pamięci i charakterystyką wydajności. Typy całkowite są systematycznie nazywane: `i8`, `i16`, `i32`, `i64` i `i128` dla liczb całkowitych ze znakiem oraz `u8`, `u16`, `u32`, `u64` i `u128` dla liczb całkowitych bez znaku. Liczby wskazują szerokość bitową, dzięki czemu wykorzystanie pamięci i zakresy wartości są natychmiast jasne.


Typy `isize` i `usize` zasługują na szczególną uwagę, ponieważ dostosowują się do architektury docelowej. W systemach 64-bitowych typy te mają szerokość 64 bitów, podczas gdy w systemach 32-bitowych mają szerokość 32 bitów. Typy te są powszechnie używane do indeksowania tablic i przesunięć pamięci, ponieważ pasują do naturalnego rozmiaru słowa architektury docelowej, umożliwiając wydajną arytmetykę wskaźników i operacje na pamięci.


Rust zapewnia wiele sposobów zapisu liczb całkowitych, w tym formaty dziesiętne, szesnastkowe (`0x`), ósemkowe (`0o`) i binarne (`0b`). Można również używać podkreśleń w dowolnym miejscu w literałach liczbowych, aby poprawić czytelność, np. pisząc `1_000_000` zamiast `1000000`. Podkreślenia nie mają wpływu na wartość, ale mogą sprawić, że duże liczby będą bardziej czytelne.


Typy zmiennoprzecinkowe w Rust są proste: `f32` dla liczb o pojedynczej precyzji i `f64` dla liczb zmiennoprzecinkowych o podwójnej precyzji. Typ `f64` jest ogólnie preferowany ze względu na wyższą precyzję i fakt, że nowoczesne procesory mogą często obsługiwać 64-bitowe operacje zmiennoprzecinkowe równie wydajnie jak operacje 32-bitowe.


### Typy złożone i organizacja danych


Oprócz typów skalarnych, Rust udostępnia typy złożone, które grupują wiele wartości. Krotki pozwalają łączyć wartości różnych typów w jedną wartość złożoną. Krotki tworzy się za pomocą nawiasów i można określić typ każdego elementu: `let tup: (i32, f64, u8) = (500, 6.4, 1)`.


Krotki obsługują destrukturyzację, która pozwala wyodrębnić poszczególne wartości: `let (x, y, z) = tup`. Ta składnia tworzy trzy oddzielne zmienne ze składników krotki. Alternatywnie, można uzyskać bezpośredni dostęp do elementów krotki używając notacji kropkowej z indeksem elementu: `tup.0`, `tup.1`, `tup.2`.


```rust
// Creating a tuple with different types
let transaction: (&str, u64, bool) = ("abc123", 50000, true);

// Destructuring: extract all values at once
let (txid, amount, confirmed) = transaction;
println!("Transaction {} for {} sats", txid, amount);

// Dot notation: access individual elements by index
println!("Confirmed: {}", transaction.2);  // true

// Practical example: function returning multiple values
fn parse_utxo(data: &str) -> (String, u32, u64) {
// Returns (txid, output_index, value_in_sats)
("a]1b2c3".to_string(), 0, 100000)
}

let (txid, vout, value) = parse_utxo("raw_data");
println!("UTXO {}:{} = {} sats", txid, vout, value);
```


Tablice w Rust różnią się znacznie od tablic lub list w wielu innych językach, ponieważ mają stały rozmiar, który staje się częścią ich typu. Tablica pięciu liczb całkowitych ma typ `[i32; 5]`, gdzie średnik oddziela typ elementu od długości tablicy. Ta informacja o rozmiarze na poziomie typu umożliwia kompilatorowi sprawdzanie granic i zapewnia, że funkcje odbierające tablice dokładnie wiedzą, ilu elementów mogą się spodziewać.


Tablice można inicjować poprzez jawne wymienienie wszystkich elementów: `[1, 2, 3, 4, 5]` lub używając skróconej składni dla tablic z powtarzającymi się wartościami: `[3; 5]` tworzy tablicę składającą się z pięciu elementów, wszystkie z wartością 3. Ten skrót jest przydatny do inicjalizacji buforów lub tworzenia tablic z wartościami domyślnymi.


Dostęp do tablicy wykorzystuje notację nawiasów kwadratowych, jak większość języków, ale Rust zapewnia sprawdzanie granic zarówno w czasie kompilacji, jak i wykonywania. Gdy uzyskujesz dostęp do tablicy ze stałym indeksem, który kompilator może zweryfikować, wychwyci on dostęp poza granicami w czasie kompilacji. W przypadku indeksów dynamicznych określonych w czasie wykonywania, Rust wstawia kontrole granic, które spowodują, że program wpadnie w panikę, jeśli spróbujesz uzyskać dostęp do nieprawidłowego indeksu, zapobiegając naruszeniom bezpieczeństwa pamięci.



## Ownership i bezpieczeństwo pamięci w Rust

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


### Zrozumienie unikalnego podejścia Rust do zarządzania pamięcią


Ten rozdział obejmuje jedną z najważniejszych koncepcji Rust. Podczas gdy poprzednie koncepcje mogły wydawać się znajome programistom pochodzącym z innych języków, własność jest podejściem Rust do rozwiązania bezpieczeństwa pamięci bez zbierania śmieci.


Rust został zaprojektowany z myślą o zapobieganiu błędom związanym z pamięcią, które nękają języki niskiego poziomu, takie jak C i C++. Problemy te obejmują błędy typu use-after-free, w których pamięć jest wykorzystywana po jej zwolnieniu, oraz przepełnienia bufora, w których programy zapisują dane poza przydzielonymi granicami pamięci. Tradycyjne rozwiązania tych problemów wiązały się z kompromisami, które Rust stara się wyeliminować. Języki wyższego poziomu, takie jak Java i Go, rozwiązują problem bezpieczeństwa pamięci poprzez odśmiecanie, w którym automatyczny proces okresowo identyfikuje i zwalnia nieużywaną pamięć. Jednak garbage collectory wprowadzają narzut na wydajność i mogą powodować nieprzewidywalne przerwy podczas wykonywania programu, co czyni je nieodpowiednimi do programowania systemów, w których stała wydajność ma krytyczne znaczenie.


Rust osiąga bezpieczeństwo pamięci głównie poprzez analizę statyczną wykonywaną w czasie kompilacji. Kompilator bada kod źródłowy i jest w stanie określić, czy większość operacji na pamięci jest bezpieczna bez konieczności odśmiecania. W przypadkach, których nie można zweryfikować statycznie - takich jak dostęp do tablicy z indeksami obliczonymi w czasie wykonywania - Rust wstawia kontrole granic, które raczej wywołują panikę niż pozwalają na niezdefiniowane zachowanie. Podejście to różni się zasadniczo od analizatorów statycznych dostępnych dla języków C i C++, które zostały zmodernizowane w językach, które nie zostały pierwotnie zaprojektowane do kompleksowej analizy statycznej. Składnia i reguły języka Rust zostały stworzone od podstaw, aby umożliwić rozległą weryfikację w czasie kompilacji, zapewniając, że po pomyślnym skompilowaniu programu będzie on działał bezpiecznie lub wpadał w panikę, a nie wykazywał niezdefiniowane zachowanie.


### System Ownership: Zasady i reguły


Kamieniem węgielnym gwarancji bezpieczeństwa pamięci Rust jest system własności, który reguluje sposób zarządzania pamięcią podczas wykonywania programu. Ownership działa w oparciu o trzy podstawowe zasady, które kompilator egzekwuje przez cały czas:


1. Każda wartość w Rust ma właściciela (zmienną, która przechowuje wartość)

2. W danym momencie może być tylko jeden właściciel

3. Gdy właściciel wychodzi poza zakres, wartość jest usuwana


Zakresy w Rust są zwykle definiowane przez nawiasy klamrowe, czy to w ciałach funkcji, blokach warunkowych, czy też jawnie utworzonych blokach zakresu. Gdy zmienna jest zadeklarowana w zakresie, zakres ten staje się właścicielem wartości zmiennej. Zmienna pozostaje dostępna i ważna przez cały czas życia zakresu, ale gdy tylko wykonanie opuści zakres, wszystkie posiadane zmienne są automatycznie czyszczone w procesie zwanym upuszczaniem.


To automatyczne czyszczenie jest realizowane przez mechanizm drop Rust, w którym język niejawnie wywołuje funkcję drop dla zmiennych wychodzących poza zakres. W przypadku podstawowych typów oznacza to po prostu, że pamięć jest oznaczona jako dostępna do ponownego wykorzystania. W przypadku bardziej złożonych typów, które zarządzają zasobami, niestandardowe implementacje drop mogą wykonywać dodatkowe operacje czyszczenia, takie jak zamykanie uchwytów plików lub zwalnianie połączeń sieciowych. Ten wzorzec, zapożyczony z RAII (Resource Acquisition Is Initialization) języka C++, zapewnia, że zasoby są zawsze prawidłowo zwalniane bez konieczności jawnego kodu czyszczenia od programisty.


### Przenoszenie Ownership i układ pamięci


Zrozumienie sposobu przenoszenia własności między zmiennymi wymaga zbadania różnicy między typami prostymi i złożonymi pod względem układu pamięci i zachowania kopiowania. Proste typy, takie jak liczby całkowite, logiczne i zmiennoprzecinkowe, mają stały, znany rozmiar w czasie kompilacji i mogą być efektywnie kopiowane. Po przypisaniu jednej zmiennej całkowitej do drugiej, Rust tworzy kompletną, niezależną kopię wartości, umożliwiając jednoczesne istnienie obu zmiennych bez żadnych obaw o własność.


Złożone typy, takie jak ciągi znaków, stanowią inne wyzwanie, ponieważ zarządzają dynamicznie przydzielaną pamięcią. String w Rust składa się z trzech komponentów przechowywanych na stosie: wskaźnika do danych znakowych przydzielonych na stercie, bieżącej długości ciągu i całkowitej pojemności przydzielonego bufora. Struktura ta pozwala na efektywne zwiększanie i zmniejszanie łańcuchów znaków przy jednoczesnym zachowaniu wiedzy o ich granicach. Po przypisaniu jednej zmiennej String do drugiej, Rust staje przed wyborem: może skopiować tylko strukturę opartą na stosie (tworząc dwa wskaźniki do tych samych danych sterty) lub wykonać głęboką kopię wszystkich danych sterty.


Domyślnym zachowaniem Rust jest przeniesienie własności zamiast kopiowania, przeniesienie danych sterty ze zmiennej źródłowej do zmiennej docelowej i unieważnienie źródła. Takie podejście zapobiega niebezpiecznemu scenariuszowi, w którym wiele zmiennych może modyfikować tę samą pamięć sterty lub w którym ta sama pamięć może być wielokrotnie zwalniana, gdy zmienne wychodzą poza zakres. Operacja przenoszenia jest wydajna, ponieważ kopiuje tylko małą strukturę opartą na stosie, a nie potencjalnie duże dane sterty, przy jednoczesnym zachowaniu bezpieczeństwa pamięci poprzez zapewnienie pojedynczej własności.


### Referencje i pożyczki


Podczas gdy przesunięcia własności zapewniają bezpieczeństwo, mogą być restrykcyjne, gdy trzeba użyć wartości w wielu miejscach bez przenoszenia własności. Rust rozwiązuje ten problem poprzez pożyczanie, które pozwala funkcjom i zmiennym na tymczasowy dostęp do danych bez przejmowania własności. Odniesienie, utworzone przy użyciu operatora ampersand, zapewnia dostęp tylko do odczytu do wartości, pozostawiając własność oryginalnej zmiennej.


Referencje umożliwiają funkcjom operowanie na danych bez ich zużywania, dzięki czemu możliwe jest wielokrotne użycie tej samej wartości w całym programie. Przekazując referencję do funkcji, tymczasowo pożyczasz dane, a funkcja musi zwrócić referencję, zanim pierwotny właściciel będzie mógł odzyskać pełną kontrolę. Ta metafora pożyczania odzwierciedla tymczasowy charakter dostępu: tak jak można pożyczyć książkę przyjacielowi, zachowując prawo własności, tak referencje umożliwiają tymczasowy dostęp przy zachowaniu pierwotnej relacji własności.


Zmienne referencje rozszerzają tę koncepcję, umożliwiając modyfikację pożyczonych danych, ale ze ścisłymi ograniczeniami w celu zachowania bezpieczeństwa. Rust zezwala tylko na jedno mutowalne odwołanie do fragmentu danych w danym momencie, zapobiegając wyścigom danych, w których wiele części programu może jednocześnie modyfikować tę samą pamięć. Dodatkowo, nie można mieć jednocześnie mutowalnych i niezmiennych odniesień do tych samych danych, ponieważ może to prowadzić do sytuacji, w których kod zakłada, że dane są stabilne, podczas gdy inny kod aktywnie je modyfikuje. Reguły te są egzekwowane w czasie kompilacji, eliminując całe klasy błędów współbieżności, które nękają inne języki programowania systemowego.


```rust
fn main() {
let mut wallet_balance: u64 = 100_000; // 100,000 satoshis

// Immutable borrow: read the balance
let balance_ref = &wallet_balance;
println!("Current balance: {} sats", balance_ref);
// balance_ref goes out of scope here

// Mutable borrow: update the balance
let balance_mut = &mut wallet_balance;
*balance_mut += 50_000; // Receive payment
println!("After deposit: {} sats", balance_mut);
// balance_mut goes out of scope here

// Function that borrows immutably
fn display_balance(balance: &u64) {
println!("Balance check: {} sats", balance);
}

// Function that borrows mutably
fn deduct_fee(balance: &mut u64, fee: u64) {
*balance -= fee;
}

display_balance(&wallet_balance);
deduct_fee(&mut wallet_balance, 1_000);
println!("After fee: {} sats", wallet_balance); // 149,000
}
```


### Typy ciągów i plasterki


Rust rozróżnia literały łańcuchowe i typ String, odzwierciedlając różne strategie zarządzania pamięcią i przypadki użycia. Literały łańcuchowe są osadzone bezpośrednio w skompilowanym pliku binarnym i mają typ &str (string slice), reprezentujący widok na niezmienne dane łańcuchowe. Te literały są wydajne, ponieważ nie wymagają alokacji w czasie wykonywania, ale nie można ich modyfikować, ponieważ są częścią kodu programu.


Z kolei typ String zarządza dynamicznie przydzielaną pamięcią i może rosnąć, kurczyć się i być modyfikowany w czasie wykonywania. String można utworzyć z literału za pomocą String::from() lub podobnych metod, które alokują pamięć sterty i kopiują zawartość literału. To rozróżnienie pozwala Rust zoptymalizować zarówno wydajność (używając literałów, gdy jest to możliwe), jak i elastyczność (używając String, gdy potrzebna jest modyfikacja).


String slices (&str) zapewniają potężną abstrakcję do pracy z fragmentami łańcuchów bez kopiowania danych. Plasterek zawiera wskaźnik do początku danych łańcucha i długość, umożliwiając efektywne odwoływanie się do podłańcuchów. Składnia slice używa zakresów (np. &s[0..5]), aby określić, do której części łańcucha należy się odwołać. Ponieważ plasterki są referencjami, podlegają one regułom pożyczania, zapobiegając modyfikacji bazowego łańcucha, gdy plasterki istnieją. To wymuszenie w czasie kompilacji zapobiega powszechnym błędom, takim jak dostęp do nieprawidłowej pamięci po zwolnieniu lub zmodyfikowaniu oryginalnego ciągu.


### Tablice, wektory i ogólne plasterki


Koncepcja slice rozciąga się poza łańcuchy na dowolną sekwencję elementów, zapewniając jednolity sposób pracy zarówno z tablicami o stałym rozmiarze, jak i dynamicznymi wektorami. Tablice w Rust mają długość zakodowaną w ich typie (np. [i32; 5] dla tablicy pięciu 32-bitowych liczb całkowitych), dzięki czemu nadają się do sytuacji wymagających gwarancji rozmiaru w czasie kompilacji. Funkcje akceptujące tablice mogą wymuszać wymagania dotyczące dokładnej długości, co jest przydatne w operacjach takich jak funkcje kryptograficzne, które wymagają precyzyjnie zwymiarowanych danych wejściowych.


Slices (&[T]) zapewniają bardziej elastyczną alternatywę, reprezentując widok na dowolną ciągłą sekwencję elementów, niezależnie od podstawowego magazynu. Można tworzyć plasterki z tablic, wektorów lub innych plasterków, a ten sam plasterek może odwoływać się do różnych części danych przez cały okres jego istnienia. Ta elastyczność sprawia, że plasterki są idealne dla funkcji, które muszą przetwarzać sekwencje bez dbania o konkretny mechanizm przechowywania lub dokładny rozmiar.


Związek między posiadanymi typami (String, Vec<T>) i ich pożyczonymi odpowiednikami w postaci wycinków (&str, &[T]) jest spójny w całym Rust. Typy własne zarządzają swoją pamięcią i mogą być modyfikowane, podczas gdy plasterki zapewniają wydajny dostęp tylko do odczytu do części tych danych. Taka konstrukcja umożliwia interfejsy API, które są zarówno elastyczne (akceptując różne typy wejściowe za pomocą plasterków), jak i wydajne (unikając niepotrzebnego kopiowania), przy jednoczesnym zachowaniu gwarancji bezpieczeństwa Rust poprzez system pożyczania.



## Struktury, tworzenie złożonych typów danych

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

Struktury w Rust służą jako podstawa do tworzenia złożonych typów danych, podobnych do klas w innych językach programowania. Pozwalają one na grupowanie powiązanych danych w jedną, spójną jednostkę, która może zawierać wiele pól różnych typów. Składnia definiowania struktury jest prosta: używasz słowa kluczowego `struct`, po którym następuje nazwa struktury, a następnie definiujesz pola w nawiasach klamrowych, używając składni dwukropka do określenia typu każdego pola.


Rust przestrzega określonych konwencji nazewnictwa struktur, które kompilator będzie wymuszał poprzez ostrzeżenia. Nazwy struktur powinny używać CamelCase (znanej również jako PascalCase), podczas gdy nazwy pól w strukturze powinny używać snake_case z podkreślnikami. Konwencja ta pomaga zachować spójność między bazami kodu Rust i sprawia, że kod jest bardziej czytelny dla innych programistów.


Tworzenie instancji struktur wymaga określenia wartości dla wszystkich pól przy użyciu nazwy struktury, po której następują nawiasy klamrowe zawierające przypisania pól. Gdy masz już instancję struktury, możesz uzyskać dostęp do poszczególnych pól i modyfikować je za pomocą notacji kropkowej, pod warunkiem, że instancja jest zadeklarowana jako mutowalna. Notacja kropkowa działa spójnie w Rust, w przeciwieństwie do języków takich jak C++, w których można używać różnych operatorów dla wskaźników i obiektów bezpośrednich.


### Funkcje konstruktora i skróty do pól


Rust nie ma wbudowanych konstruktorów, jak niektóre języki obiektowe, ale można tworzyć funkcje, które zwracają instancje struktur, aby służyć temu samemu celowi. Te funkcje konstruktora zazwyczaj przyjmują parametry dla niektórych lub wszystkich pól i mogą ustawiać wartości domyślne dla innych. Podczas pisania takich funkcji, Rust zapewnia wygodny skrót: jeśli parametr ma taką samą nazwę jak pole struktury, można po prostu napisać nazwę pola raz, zamiast powtarzać ją w formacie `field: value`.


Instancje struktury mogą być również tworzone poprzez kopiowanie wartości z istniejących instancji przy użyciu składni struct update. Ta funkcja umożliwia utworzenie nowej instancji przy jednoczesnym określeniu tylko pól, które mają zostać zmienione, a wszystkie inne pola zostaną skopiowane z istniejącej instancji. Operacja ta jest jednak zgodna z regułami własności Rust, co oznacza, że typy inne niż kopiowane zostaną przeniesione z instancji źródłowej, potencjalnie czyniąc części oryginalnej instancji bezużytecznymi. Kompilator inteligentnie śledzi te częściowe przeniesienia, umożliwiając dalsze korzystanie z pól, które nie zostały przeniesione, jednocześnie uniemożliwiając dostęp do przeniesionych pól.


### Struktury krotek i struktury jednostek


Rust obsługuje struktury krotek, które są strukturami z nienazwanymi polami dostępnymi przez indeks, a nie przez nazwę. Są one przydatne w przypadku prostych typów wrapper lub gdy potrzebna jest struktura, ale nie są wymagane nazwane pola. Dostęp do pól struktur krotek uzyskuje się za pomocą notacji kropkowej, po której następuje indeks pola, na przykład `.0` dla pierwszego pola, `.1` dla drugiego itd. Podejście to sprawdza się dobrze w przypadku struktur, które zawierają pojedynczą wartość lub tylko kilka ściśle powiązanych wartości, gdzie nazwy mogą być zbędne.


Struktury jednostkowe reprezentują najprostszą formę struktur - nie zawierają żadnych danych. Choć początkowo może się to wydawać bezcelowe, struktury jednostkowe stają się cenne podczas pracy z systemem cech Rust, ponieważ mogą implementować zachowania bez przechowywania jakichkolwiek danych. Te puste struktury służą jako znaczniki lub symbole zastępcze w bardziej zaawansowanych wzorcach Rust.


### Metody i powiązane funkcje


Struktury zyskują dodatkową funkcjonalność, gdy dodasz zachowanie poprzez bloki implementacji. Używając słowa kluczowego `impl`, po którym następuje nazwa struktury, można zdefiniować metody, które działają na instancjach struktury. Metody są funkcjami, które przyjmują `self` jako swój pierwszy parametr, który może być posiadaną wartością (`self`), niezmienną referencją (`&self`) lub zmienną referencją (`&mut self`), w zależności od tego, co metoda musi zrobić z instancją.


Wybór typu parametru `self` określa zachowanie metody w odniesieniu do własności. Metody przyjmujące `&self` mogą czytać z instancji bez przejmowania własności, co czyni je odpowiednimi dla operacji, które nie modyfikują struktury. Metody przyjmujące `&mut self` mogą modyfikować instancję, jednocześnie pozwalając wywołującemu na zachowanie własności. Metody przyjmujące wartość `self` zużywają instancję, co jest odpowiednie dla operacji, które przekształcają strukturę w coś innego lub gdy metoda reprezentuje ostatnią operację na tej instancji.


Funkcje stowarzyszone to funkcje zdefiniowane w bloku implementacji, które nie przyjmują `self` jako parametru. Są one podobne do metod statycznych w innych językach i są powszechnie używane jako konstruktory lub funkcje użytkowe związane z typem. Funkcje stowarzyszone są wywoływane przy użyciu składni podwójnego dwukropka (`Type::function_name()`), co wyraźnie odróżnia je od metod wywoływanych na instancjach.


```rust
// Define a struct for a Lightning invoice
struct Invoice {
payment_hash: String,
amount_msat: u64,
description: String,
expiry_secs: u32,
}

impl Invoice {
// Associated function (constructor) - no self parameter
fn new(payment_hash: String, amount_msat: u64, description: String) -> Self {
Invoice {
payment_hash,
amount_msat,
description,
expiry_secs: 3600, // default 1 hour
}
}

// Method with &self - read-only access
fn amount_sats(&self) -> u64 {
self.amount_msat / 1000
}

// Method with &mut self - can modify the instance
fn extend_expiry(&mut self, additional_secs: u32) {
self.expiry_secs += additional_secs;
}

// Method with self - consumes the instance
fn into_payment_request(self) -> String {
format!("lnbc{}n1p{}", self.amount_msat, self.payment_hash)
}
}

fn main() {
// Use associated function to create instance
let mut invoice = Invoice::new(
"abc123".to_string(),
100_000_000, // 100,000 sats in millisats
"Coffee payment".to_string(),
);

println!("Amount: {} sats", invoice.amount_sats());
invoice.extend_expiry(1800); // Add 30 minutes

let request = invoice.into_payment_request();
// invoice is now consumed, cannot be used anymore
println!("Payment request: {}", request);
}
```


#### Wyliczenia: Modelowanie wyborów i wariantów


Wyliczenia w Rust mają więcej możliwości niż wyliczenia w wielu innych językach. Chociaż mogą reprezentować proste zestawy nazwanych stałych, wyliczenia Rust mogą również przenosić dane w każdym wariancie, dzięki czemu nadają się do modelowania sytuacji, w których wartość może być jednym z kilku różnych typów lub stanów. Każdy wariant wyliczenia może zawierać różne typy i ilości danych, od braku danych do złożonych struktur z nazwanymi polami.


Możliwość dołączania danych do wariantów wyliczeń eliminuje wiele typowych błędów programistycznych występujących w innych językach. Zamiast utrzymywać oddzielne zmienne dla wskaźnika typu i powiązanych danych - które mogą łatwo stać się niespójne - wyliczenia Rust łączą informacje o typie z samymi danymi. Taka konstrukcja zapewnia, że dane zawsze pasują do wariantu, zapobiegając niedopasowaniu, które może prowadzić do błędów w czasie wykonywania.


Warianty wyliczeń mogą zawierać dane w kilku formach: brak danych dla prostych flag, dane podobne do krotek dla nienazwanych pól lub dane podobne do struktur z nazwanymi polami. Można nawet mieszać te style w ramach jednego wyliczenia, wybierając najbardziej odpowiednią formę dla każdego wariantu. Ta elastyczność sprawia, że wyliczenia nadają się do modelowania złożonych koncepcji domen, w których różne przypadki wymagają różnych informacji.


#### Typ opcji: Bezpieczna obsługa nieobecności


Jednym z najważniejszych wyliczeń Rust jest `Option<T>`, które reprezentuje wartości, które mogą być obecne lub nie. Wyliczenie to ma dwa warianty: `Some(T)` zawierający wartość typu T, oraz `None` reprezentujący brak wartości. Typ Option służy jako rozwiązanie Rust dla problemów ze wskaźnikiem null, które nękają wiele innych języków, zmuszając programistów do jawnej obsługi przypadków, w których może brakować wartości.


Korzystanie z typów Option sprawia, że kod jest bardziej niezawodny, ponieważ kompilator wymaga obsługi zarówno obecności, jak i braku wartości. Nie można przypadkowo użyć potencjalnie brakującej wartości bez uprzedniego sprawdzenia jej istnienia. Ta jawna obsługa zapobiega wyjątkom wskaźnika null i podobnym błędom, które są częstym źródłem błędów w innych językach programowania.


Typ Option integruje się z systemem dopasowywania wzorców Rust, pozwalając na obsługę obu przypadków. Metody takie jak `unwrap_or()` zapewniają wygodne sposoby wyodrębniania wartości z domyślnymi wartościami, podczas gdy metody takie jak `map()` i `and_then()` umożliwiają funkcjonalne wzorce programowania do pracy z wartościami opcjonalnymi.


### Dopasowywanie wzorców za pomocą wyrażeń dopasowujących


Dopasowywanie wzorców za pomocą wyrażeń `match` zapewnia sposób pracy z wyliczeniami i innymi typami danych. Wyrażenie dopasowania bada wartość i wykonuje inny kod w oparciu o wzorzec, do którego pasuje wartość. Każdy wzorzec może destrukturyzować dopasowaną wartość, wiążąc jej części ze zmiennymi, które mogą być użyte w odpowiednim bloku kodu.


Wyrażenia dopasowujące muszą być wyczerpujące, co oznacza, że muszą obsługiwać każdy możliwy przypadek dla dopasowywanego typu. Wymóg ten zapobiega błędom, które mogłyby wystąpić, gdyby niektóre przypadki zostały przypadkowo pozostawione bez obsługi. Jeśli nie chcesz jawnie obsługiwać każdego przypadku, możesz użyć wzorca wieloznacznego (`_`), aby przechwycić wszystkie pozostałe przypadki lub powiązać nieobsługiwane przypadki ze zmienną, jeśli potrzebujesz dostępu do wartości.


Konstrukcja `if let` zapewnia bardziej zwięzłą alternatywę dla match, gdy zależy nam tylko na jednym konkretnym wzorcu. Ta składnia jest szczególnie przydatna podczas pracy z typami opcji lub gdy chcesz wykonać kod tylko wtedy, gdy wartość pasuje do określonego wariantu wyliczenia. Konstrukcja `if let` może zawierać klauzulę `else` dla przypadków, w których wzorzec nie pasuje, co czyni ją usprawnionym sposobem obsługi prostych scenariuszy dopasowywania wzorców.


#### Kolekcje: Zarządzanie grupami danych


Standardowa biblioteka Rust udostępnia kilka typów kolekcji do zarządzania grupami powiązanych danych. Kolekcje te są ogólne, co oznacza, że mogą przechowywać elementy dowolnego typu i automatycznie obsługują zarządzanie pamięcią. Najczęściej używanymi kolekcjami są wektory dla uporządkowanych list, mapy hash dla skojarzeń klucz-wartość i ciągi dla danych tekstowych.


#### Wektory: Tablice dynamiczne


Wektory reprezentują rosnące tablice, które mogą zmieniać rozmiar podczas wykonywania programu. W przeciwieństwie do tablic o stałym rozmiarze, wektory alokują pamięć na stercie i mogą się rozszerzać lub zmniejszać w zależności od potrzeb. Tworzenie wektora często wymaga jawnej adnotacji typu podczas rozpoczynania od pustego wektora, ponieważ kompilator musi wiedzieć, jaki typ elementów będzie zawierał wektor.


Wektory zapewniają wiele sposobów dostępu do elementów, każdy z inną charakterystyką bezpieczeństwa. Notacja indeksowa (`vec[0]`) zapewnia bezpośredni dostęp, ale spowoduje panikę, jeśli indeks jest poza granicami. Metoda `get()` zwraca `Option`, pozwalając na sprawną obsługę dostępu poza granicami. Wybór między tymi podejściami zależy od tego, czy można zagwarantować, że indeks jest prawidłowy, czy też trzeba obsłużyć potencjalne awarie.


Zasady pożyczania Rust mają zastosowanie do wektorów, zapobiegając typowym problemom związanym z bezpieczeństwem pamięci. Jeśli posiadasz odwołanie do elementu wektora, nie możesz modyfikować wektora, dopóki to odwołanie nie wyjdzie poza zakres. Zapobiega to sytuacjom, w których odniesienia mogą wskazywać na dealokowaną pamięć po operacjach wektorowych, takich jak wypychanie nowych elementów lub czyszczenie wektora.


#### Mapy Hash: Przechowywanie klucz-wartość


Mapy Hash zapewniają wydajne przechowywanie klucz-wartość, w którym można szybko wyszukiwać wartości na podstawie powiązanych z nimi kluczy. Zarówno klucze, jak i wartości mogą być dowolnego typu, choć klucze muszą implementować cechy niezbędne do haszowania i porównywania równości. Mapy Hash przejmują własność wstawionych wartości, chyba że wartości implementują cechę Copy.


Mapy Hash oferują kilka metod wstawiania i aktualizacji wartości. Podstawowa metoda `insert()` nadpisze istniejące wartości, podczas gdy `entry()` zapewnia bardziej elastyczną logikę wstawiania. Wpis API pozwala wstawiać wartości tylko wtedy, gdy jeszcze nie istnieją, lub aktualizować istniejące wartości w oparciu o ich aktualny stan. Ten API jest przydatny dla wzorców takich jak zliczanie wystąpień lub utrzymywanie bieżących sum.


Podczas pobierania wartości z hash map, metoda `get()` zwraca `Option`, ponieważ żądany klucz może nie istnieć. Możesz użyć metod takich jak `copied()` by przekonwertować z `Option<&T>` na `Option<T>` dla typów Copy i `unwrap_or()` by dostarczyć domyślne wartości gdy brakuje kluczy.


### Obsługa ciągów znaków i Unicode


Ciągi w Rust są kodowane w UTF-8, co zapewnia pełną obsługę Unicode, ale wprowadza złożoność w porównaniu do prostych ciągów ASCII. Typ `String` reprezentuje posiadane, rosnące dane tekstowe, podczas gdy string slices (`&str`) zapewniają zapożyczone widoki na dane łańcuchowe. Można konwertować między tymi typami w razie potrzeby, przy czym string slices są często używane w parametrach funkcji, aby akceptować zarówno własne ciągi znaków, jak i literały łańcuchowe.


Manipulacja łańcuchami zawiera metody dołączania tekstu, formatowania wielu wartości razem i wyodrębniania podciągów. Metoda `push_str()` dołącza fragmenty łańcucha bez przejmowania własności, podczas gdy makro `format!` zapewnia elastyczny sposób konstruowania łańcuchów z wielu komponentów. Podczas pracy z indeksami łańcuchów, należy uważać na przestrzeganie granic znaków UTF-8, aby uniknąć paniki w czasie wykonywania.


Dla bezpiecznego przetwarzania znak po znaku, ciągi zapewniają metody iteratora takie jak `chars()` dla wartości skalarnych Unicode i `bytes()` dla dostępu do surowych bajtów. Te iteratory poprawnie obsługują kodowanie UTF-8, zapewniając, że nie podzielisz przypadkowo znaków wielobajtowych. Takie podejście jest bezpieczniejsze i bardziej niezawodne niż ręczne indeksowanie, zwłaszcza podczas pracy z międzynarodowym tekstem, który może zawierać złożone znaki Unicode.



## Dwukategorialny system obsługi błędów Rust

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

Rust przyjmuje zasadniczo odmienne podejście do obsługi błędów w porównaniu do większości języków programowania. Podczas gdy wiele języków opiera się głównie na wyjątkach, Rust rozróżnia dwie różne kategorie błędów i zapewnia określone mechanizmy obsługi każdego typu. Niniejszy rozdział omawia kompleksowy system obsługi błędów Rust, obejmujący zarówno nieodwracalne błędy, które kończą wykonywanie programu, jak i możliwe do odzyskania błędy, które pozwalają programom kontynuować działanie z zachowaniem wdzięku.


### Nienaprawialne błędy i panika


Błędy nienaprawialne reprezentują sytuacje, w których program wszedł w niespójny lub nieoczekiwany stan, z którego nie może bezpiecznie wyjść. Obejmują one scenariusze, takie jak dostęp do tablicy poza granicami, próby operacji naruszających bezpieczeństwo pamięci lub napotkanie warunków wskazujących na podstawowe błędy logiczne programu. W przypadku wystąpienia takich błędów właściwą reakcją jest natychmiastowe zakończenie programu, zamiast ryzykować dalsze uszkodzenie lub niezdefiniowane zachowanie.


W Rust nieodwracalne błędy wywołują panikę, która powoduje awarię programu w kontrolowany sposób. Przed zakończeniem Rust wykonuje proces zwany rozwijaniem, w którym cofa się przez stos wywołań, aby zapewnić szczegółowy ślad stosu pokazujący dokładnie, gdzie wystąpiła panika. Proces ten pomaga programistom zidentyfikować źródło problemu podczas debugowania. W przypadku aplikacji o krytycznym znaczeniu dla wydajności lub systemów wbudowanych można wyłączyć rozwijanie i skonfigurować Rust tak, aby przerywał natychmiast po wystąpieniu paniki, choć poświęca to informacje debugowania na rzecz szybszego zakończenia.


Panikę można wywołać jawnie za pomocą makra `panic!` z niestandardowym komunikatem. Gdy wystąpi panika, zobaczysz dane wyjściowe wskazujące, który wątek wpadł w panikę i powiązany komunikat. Ustawienie zmiennej środowiskowej `RUST_BACKTRACE` zapewnia dodatkowe informacje debugowania, pokazując kompletny stos wywołań, który doprowadził do paniki. Na przykład, próba uzyskania dostępu do elementu 99 wektora zawierającego tylko trzy elementy spowoduje generate panikę z komunikatem "index out of bounds" wraz z backtrace pokazującym dokładną sekwencję wywołań funkcji, które doprowadziły do błędu.


### Możliwe do odzyskania błędy z wynikiem


Błędy odzyskiwalne reprezentują oczekiwane warunki awarii, które programy mogą obsłużyć z wdziękiem bez kończenia pracy. Przykłady obejmują próbę otwarcia pliku, który nie istnieje, awarie połączenia sieciowego lub nieprawidłowe dane wejściowe użytkownika. Dla takich sytuacji Rust udostępnia wyliczenie `Result`, które wyraźnie reprezentuje operacje, które mogą zakończyć się niepowodzeniem i zmusza programistów do obsługi zarówno przypadków powodzenia, jak i niepowodzenia.


Wyliczenie `Result` jest zdefiniowane z dwoma wariantami: `Ok(T)` dla udanych operacji zawierających wartość typu `T` i `Err(E)` dla niepowodzeń zawierających błąd typu `E`. Ten projekt wykorzystuje system typów Rust, aby zapewnić, że potencjalne awarie nie mogą zostać zignorowane. Funkcje, które mogą zawieść, zwracają `Result`, a kod wywołujący musi jawnie obsługiwać zarówno przypadki sukcesu, jak i błędu, zazwyczaj używając dopasowywania wzorców z wyrażeniami `match`.


Rozważmy funkcję `File::open`, która zwraca `Result<File, std::io::Error>`. Podczas otwierania pliku otrzymujemy albo obiekt `File`, jeśli operacja się powiedzie, albo `std::io::Error`, jeśli operacja się nie powiedzie. Możesz dopasować ten wynik, aby odpowiednio obsłużyć każdy przypadek. W przypadku sukcesu możesz kontynuować operacje na plikach, podczas gdy w przypadku błędu możesz spróbować utworzyć plik, wypróbować alternatywne podejście lub propagować błąd do kodu wywołującego. Ta wyraźna obsługa zapewnia, że program podejmuje świadome decyzje dotyczące odzyskiwania błędów, a nie niespodziewanie ulega awarii.


### Wzorce i skróty obsługi błędów


Podczas gdy jawne dopasowywanie wzorców zapewnia pełną kontrolę nad obsługą błędów, Rust oferuje kilka wygodnych metod dla typowych wzorców obsługi błędów. Metoda `unwrap` wyodrębnia wartość sukcesu z `Result`, ale panikuje, jeśli wystąpi błąd, co czyni ją przydatną do szybkiego prototypowania lub sytuacji, w których jesteś pewien, że operacja się powiedzie. Metoda `expect` działa podobnie, ale pozwala na dostarczenie niestandardowego komunikatu paniki, ułatwiając debugowanie, gdy coś pójdzie nie tak.


Aby zapewnić bardziej elastyczną obsługę błędów, metody takie jak `unwrap_or_else` pozwalają na dostarczenie zamknięcia, które wykonuje się, gdy wystąpi błąd, umożliwiając niestandardową logikę odzyskiwania. Operacje te można łączyć w łańcuchy, aby obsługiwać złożone scenariusze, takie jak próba otwarcia pliku i utworzenie go, jeśli nie istnieje, z różnymi strategiami obsługi błędów dla każdego kroku.


Operator znaku zapytania (`?`) zapewnia zwięzłą składnię propagacji błędów, która jest powszechna w programach Rust. Po dołączeniu `?` do `Result`, automatycznie rozpakowuje on pomyślne wartości i natychmiast zwraca błędy z bieżącej funkcji. Operator ten może być używany tylko w funkcjach zwracających typy `Result`, zapewniając, że błędy mogą być prawidłowo propagowane w górę stosu wywołań. Operator `?` sprawia, że kod obsługi błędów jest znacznie bardziej czytelny, eliminując rozwlekłe wyrażenia dopasowania, zachowując jednocześnie jawną semantykę propagacji błędów.


```rust
use std::fs::File;
use std::io::{self, Read};

// Custom error type for wallet operations
#[derive(Debug)]
enum WalletError {
FileNotFound,
InvalidFormat,
InsufficientFunds,
}

// Function returning Result for recoverable errors
fn load_wallet_balance(path: &str) -> Result<u64, WalletError> {
// Simulate reading from file
let balance_str = "150000"; // Would normally read from file
balance_str
.parse::<u64>()
.map_err(|_| WalletError::InvalidFormat)
}

// Using the ? operator for clean error propagation
fn send_payment(amount: u64) -> Result<String, WalletError> {
let balance = load_wallet_balance("wallet.dat")?; // Propagates error if it fails

if balance < amount {
return Err(WalletError::InsufficientFunds);
}

Ok(format!("Sent {} sats, remaining: {}", amount, balance - amount))
}

fn main() {
// Handle the Result explicitly
match send_payment(50_000) {
Ok(msg) => println!("Success: {}", msg),
Err(WalletError::InsufficientFunds) => println!("Error: Not enough funds"),
Err(WalletError::FileNotFound) => println!("Error: Wallet file not found"),
Err(WalletError::InvalidFormat) => println!("Error: Corrupted wallet file"),
}

// Or use unwrap_or_else for custom fallback
let result = send_payment(200_000)
.unwrap_or_else(|e| format!("Payment failed: {:?}", e));
println!("{}", result);
}
```


### Propagacja błędów i projektowanie funkcji


Propagacja błędów jest podstawową koncepcją w obsłudze błędów Rust, pozwalającą funkcjom na przekazywanie błędów w górę stosu wywołań zamiast obsługiwać je lokalnie. Podczas projektowania funkcji, które mogą zawieść, należy zwracać typy `Result`, aby zapewnić wywołującym elastyczność w decydowaniu o sposobie obsługi błędów. Takie podejście promuje kompozycyjną obsługę błędów, w której każda funkcja w łańcuchu wywołań może obsługiwać błędy lokalnie lub przekazywać je do kodu wyższego poziomu, który ma więcej kontekstu do podejmowania decyzji o odzyskiwaniu.


Operator znaku zapytania upraszcza propagację błędów. Zamiast pisać szczegółowe wyrażenia dopasowania dla każdej potencjalnie nieudanej operacji, można łączyć operacje w łańcuchy za pomocą operatorów `?`, tworząc czytelny kod, który obsługuje ścieżkę sukcesu, jednocześnie automatycznie propagując wszelkie występujące błędy. Ten wzorzec jest tak powszechny, że wiele funkcji Rust zostało zaprojektowanych specjalnie do pracy z operatorem `?`, umożliwiając płynną obsługę błędów w całej bazie kodu.


Podejmując decyzję między paniką a zwracaniem błędów, należy rozważyć, czy kod wywołujący może w rozsądny sposób odzyskać sprawność po awarii. Jeśli awaria reprezentuje błąd programistyczny lub niemożliwy do odzyskania stan systemu, panika jest odpowiednia. Jednakże, jeśli awaria jest oczekiwanym stanem, który kod wywołujący może obsłużyć inaczej w zależności od kontekstu, zwrócenie `Result` zapewnia lepszą elastyczność i możliwość komponowania.


### Najlepsze praktyki i kwestie projektowe


Skuteczna obsługa błędów w Rust wymaga przemyślanego rozważenia, kiedy należy panikować, a kiedy zwracać błędy. Paniki należy używać w sytuacjach, które reprezentują błędy programistyczne lub stany, które nigdy nie powinny wystąpić w poprawnych programach, takich jak dostęp do zakodowanych danych, o których wiadomo, że są prawidłowe. Na przykład, parsowanie zakodowanego ciągu adresu IP, który został zweryfikowany jako poprawny, może bezpiecznie używać `expect` z opisowym komunikatem wyjaśniającym, dlaczego operacja nigdy nie powinna się nie powieść.


W przypadku danych wejściowych kontrolowanych przez użytkownika lub interakcji z systemem zewnętrznym, zawsze preferuj zwracanie typów `Result` zamiast panikować. Użytkownicy popełniają błędy, pliki są usuwane, a połączenia sieciowe zawodzą - są to normalne warunki, które dobrze zaprojektowane programy powinny obsługiwać z wdziękiem. Zwracając błędy w takich sytuacjach, umożliwiasz kodowi wywołującemu wdrożenie odpowiednich strategii odzyskiwania, niezależnie od tego, czy jest to monitowanie użytkownika o inne dane wejściowe, powrót do wartości domyślnych, czy wyświetlanie pomocnych komunikatów o błędach.


Rozważ utworzenie niestandardowych typów, które wymuszają walidację w czasie budowy, aby zapobiec rozprzestrzenianiu się nieprawidłowych stanów w programie. Na przykład, jeśli program wymaga liczb w określonym zakresie, należy utworzyć typ opakowujący, który sprawdza poprawność danych wejściowych podczas konstruowania i nie zapewnia możliwości tworzenia nieprawidłowych instancji. Takie podejście wykorzystuje system typów Rust do wyeliminowania całych klas błędów poprzez uniemożliwienie reprezentacji nieprawidłowych stanów, zmniejszając potrzebę sprawdzania błędów w czasie wykonywania w całej bazie kodu.


## Funkcje programowania funkcjonalnego, domknięcia i inteligentne wskaźniki


<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Chociaż Rust nie jest czystym językiem programowania funkcyjnego, zawiera funkcje inspirowane paradygmatami programowania funkcyjnego. Funkcje te umożliwiają programistom pisanie zwięzłego kodu poprzez wykorzystanie koncepcji takich jak zamknięcia i iteratory. Rust zawiera te funkcjonalne elementy, aby zapewnić elastyczne narzędzia do przetwarzania danych i mechanizmy oddzwaniania.


Funkcje programowania funkcyjnego w Rust zachowują podstawowe zasady języka dotyczące bezpieczeństwa pamięci i abstrakcji o zerowych kosztach. Korzystając z domknięć i iteratorów, nie poświęcasz wydajności na rzecz ekspresyjności - kompilator Rust optymalizuje te konstrukcje, aby uzyskać wydajny kod maszynowy porównywalny z tradycyjnymi podejściami opartymi na pętlach.


### Zrozumienie zamknięć


Zamknięcia w Rust to anonimowe funkcje, które mogą przechwytywać zmienne z otaczającego je środowiska. W innych językach programowania są one często nazywane funkcjami lambda. Kluczową cechą domknięć jest ich zdolność do "zamykania" swojego środowiska, co oznacza, że mogą one uzyskiwać dostęp i używać zmiennych, które istnieją w zakresie, w którym zdefiniowane jest domknięcie.


Składnia domknięć używa znaków potoku (`|`) zamiast nawiasów do definiowania parametrów. Dla domknięcia bez parametrów, piszemy `||`, a dla domknięć z parametrami, wymieniamy je pomiędzy znakami potoku jak `|x, y|`. Jeśli ciało zamknięcia składa się z pojedynczego wyrażenia, można pominąć nawiasy klamrowe, dzięki czemu składnia jest bardzo zwięzła.


Rozważmy praktyczny przykład firmy produkującej koszulki, która rozdaje ekskluzywne koszulki w oparciu o preferencje klientów. Jeśli klient określił ulubiony kolor, otrzymuje ten kolor; w przeciwnym razie otrzymuje domyślnie najbardziej dostępny kolor. Używając domknięć, ta logika staje się: `user_preference.unwrap_or_else(|| self.most_stocked())`. Zamknięcie `|| self.most_stocked()` dostarcza domyślną wartość tylko wtedy, gdy jest to potrzebne i może uzyskać dostęp do `self` ze swojego środowiska.


### Wnioskowanie o typie zamknięcia i elastyczność


Jedną z najwygodniejszych funkcji Rust z domknięciami jest automatyczne wnioskowanie o typie. W przeciwieństwie do zwykłych funkcji, w których należy jawnie określić typy parametrów i typy zwracane, domknięcia często mogą wnioskować o tych typach z kontekstu. Kompilator analizuje sposób użycia domknięcia i automatycznie określa odpowiednie typy. Jednak po wywołaniu domknięcia z określonymi typami, typy te stają się stałe dla tej instancji domknięcia.


Zamknięcia można przechowywać w zmiennych, tak jak każdą inną wartość, co czyni je obywatelami pierwszej klasy w języku. Po przypisaniu domknięcia do zmiennej, można je później wywołać za pomocą nawiasów: `let my_closure = |x| x + 1; let result = my_closure(5);`. Ta elastyczność pozwala na przekazywanie domknięć jako argumentów do funkcji, zwracanie ich z funkcji i używanie ich w strukturach danych.


Jeśli kompilator nie może wnioskować o typach lub jeśli chcesz być jawny, możesz adnotować parametry zamknięcia i typy zwracane przy użyciu składni podobnej do funkcji: `|x: i32| -> i32 { x + 1 }`. Takie jawne typowanie jest czasami konieczne w złożonych scenariuszach, w których kompilator potrzebuje dodatkowych informacji do poprawnego określenia typów.


### Przechwytywanie zmiennych środowiskowych


Zamknięcia mogą przechwytywać zmienne ze swojego środowiska na trzy różne sposoby: przez niezmienne odniesienie, przez zmienne odniesienie lub przez przejęcie własności. Kompilator Rust automatycznie określa najbardziej restrykcyjną metodę przechwytywania, która spełnia potrzeby zamknięcia, zgodnie z zasadą najmniejszego przywileju.


Gdy zamknięcie musi tylko odczytać wartość, przechwytuje ją przez niezmienne odniesienie. Pozwala to oryginalnej zmiennej pozostać dostępną po zdefiniowaniu i wywołaniu zamknięcia. Na przykład, zamknięcie, które drukuje listę, pożyczy listę w sposób niezmienny, umożliwiając dalsze korzystanie z listy po wykonaniu zamknięcia.


Jeśli zamknięcie musi zmodyfikować przechwyconą zmienną, musi przechwycić ją przez mutowalne odniesienie. W takim przypadku zarówno przechwycona zmienna, jak i samo zamknięcie muszą być zadeklarowane jako zmienne. Zamknięcie może następnie modyfikować przechwyconą zmienną, ale nadal obowiązują zasady pożyczania - nie można mieć innych odniesień do tej zmiennej, gdy istnieje mutowalne zamknięcie.


Najbardziej restrykcyjną metodą przechwytywania jest przejęcie własności, które przenosi przechwycone zmienne do zamknięcia. Jest to konieczne, gdy zamknięcie może przekroczyć zakres, w którym zmienne zostały pierwotnie zdefiniowane, na przykład podczas odradzania wątków. Przechwytywanie własności można wymusić za pomocą słowa kluczowego `move` przed parametrami zamknięcia: `move |x| { /* closure body */ }`. Jest to niezbędne dla bezpieczeństwa wątków, ponieważ wątki nie mogą bezpiecznie pożyczać od innych wątków, które mogą zakończyć działanie i porzucić swoje zmienne.


### Cechy zamknięcia i typy funkcji


Rust reprezentuje domknięcia poprzez system cech z trzema kluczowymi cechami: `FnOnce`, `FnMut` i `Fn`. Cechy te tworzą hierarchię, która opisuje sposób, w jaki zamknięcia mogą być wywoływane i co mogą zrobić z przechwyconymi zmiennymi.


`FnOnce` jest najbardziej podstawową cechą, którą implementują wszystkie zamknięcia. Reprezentuje ona zamknięcia, które mogą być wywołane co najmniej raz. Niektóre zamknięcia, szczególnie te, które przenoszą przechwycone wartości lub wykorzystują je w jakiś sposób, mogą być wywołane tylko raz, ponieważ niszczą lub przenoszą przechwycone dane podczas wykonywania.


`FnMut` reprezentuje zamknięcia, które mogą być wywoływane wielokrotnie i mogą mutować swoje przechwycone środowisko. Zamknięcia te przechwytują zmienne przez mutowalne referencje i mogą je modyfikować podczas wielu wywołań. Reguły pożyczania zapewniają, że gdy zamknięcie `FnMut` jest aktywne, ma wyłączny mutowalny dostęp do swoich przechwyconych zmiennych.


`Fn` jest najbardziej restrykcyjną cechą, reprezentującą zamknięcia, które mogą być wywoływane wielokrotnie bez mutowania ich przechwyconego środowiska. Zamknięcia te przechwytują tylko przez niezmienne referencje i mogą być wywoływane współbieżnie bez naruszania gwarancji bezpieczeństwa Rust. Jeśli zamknięcie implementuje `Fn`, automatycznie implementuje także `FnMut` i `FnOnce`, ponieważ bycie wywoływanym wiele razy bez mutacji implikuje bycie wywoływanym z mutacją i bycie wywoływanym raz.


### Praca z iteratorami


Iteratory w Rust zapewniają sposób przetwarzania sekwencji danych. Są one leniwe, co oznacza, że nie wykonują żadnej pracy, dopóki nie zostaną wykorzystane przez wywołanie metod, które faktycznie wykonują iterację po danych. Ta leniwa ewaluacja pozwala na wydajne łączenie operacji bez tworzenia pośrednich kolekcji.


Cecha `Iterator` definiuje podstawową funkcjonalność z powiązanym typem `Item`, który reprezentuje to, co iterator zwraca oraz metodę `next`, która zwraca `Option<Self::Item>`. Gdy `next` zwraca `None`, iterator jest wyczerpany. Taka konstrukcja pozwala iteratorom bezpiecznie reprezentować zarówno skończone, jak i potencjalnie nieskończone sekwencje.


Możesz tworzyć iteratory z kolekcji używając metod takich jak `iter()` do pożyczania iteracji, `iter_mut()` do mutowalnego pożyczania iteracji i `into_iter()` do konsumowania iteracji. Wybór między tymi metodami zależy od tego, czy musisz modyfikować elementy i czy chcesz konsumować oryginalną kolekcję.


### Adaptery i odbiorniki iteratorów


Adaptery iteratorów to metody, które przekształcają jeden iterator w inny, pozwalając na łączenie operacji w łańcuchy. Popularne adaptery obejmują `map` do przekształcania każdego elementu, `filter` do wybierania elementów na podstawie predykatu i `enumerate` do dodawania indeksów. Adaptery te są leniwe - nie wykonują żadnej pracy, dopóki nie zostaną wykorzystane.


Metoda `map` stosuje zamknięcie do każdego elementu, przekształcając go w coś innego. Na przykład, `numbers.iter().map(|x| x * 2)` tworzy iterator, który podwaja każdą liczbę. Metoda `filter` zachowuje tylko elementy, dla których zamknięcie predykatu zwraca wartość true: `numbers.iter().filter(|&x| x > 10)` zachowuje tylko liczby większe niż dziesięć.


Metody konsumenckie faktycznie iterują przez dane i tworzą końcowy wynik. Metoda `collect` pobiera iterator i tworzy z niego kolekcję. Często trzeba określić typ kolekcji: `let vec: Vec<_> = iterator.collect()`. Inne konsumery obejmują `sum` do dodawania elementów numerycznych, `fold` do gromadzenia wartości za pomocą niestandardowej operacji i `for_each` do wykonywania efektów ubocznych na każdym elemencie.


### Zaawansowane wzorce iteratorów


Dodatkowe operacje iteratora obejmują `zip` do łączenia dwóch iteratorów element po elemencie, `chain` do łączenia iteratorów i `filter_map` do łączenia filtrowania i mapowania w jednej operacji. Metoda `zip` tworzy pary z odpowiadających sobie elementów dwóch iteratorów: `a.iter().zip(b.iter())` tworzy krotki `(a[0], b[0]), (a[1], b[1]), ...`.


Metoda `fold` jest przydatna do akumulowania wartości. Przyjmuje ona wartość początkową i zamknięcie, które łączy akumulator z każdym elementem: `numbers.iter().fold(0, |acc, x| acc + x)` sumuje wszystkie liczby. Ten wzorzec może implementować wiele innych operacji, takich jak znajdowanie wartości maksymalnych, budowanie ciągów lub tworzenie złożonych struktur danych.


Łańcuchy iteratorów mogą w zwięzły sposób wyrażać złożone transformacje danych. Na przykład, przetwarzanie danych audio może obejmować: `coefficients.iter().zip(buffer.iter()).map(|(c, b)| c * b).sum::<i32>() >> 12`. Powoduje to pomnożenie odpowiednich współczynników i wartości bufora, zsumowanie wyników i przesunięcie wartości końcowej, a wszystko to w jednym czytelnym wyrażeniu.


```rust
fn main() {
// Sample UTXOs: (txid_suffix, amount_sats)
let utxos = vec![
("a1b2", 50_000u64),
("c3d4", 15_000),
("e5f6", 100_000),
("g7h8", 3_000),
("i9j0", 75_000),
];

// Using closures and iterators to process UTXOs

// 1. Filter UTXOs above dust threshold (10,000 sats)
let spendable: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000)
.collect();
println!("Spendable UTXOs: {:?}", spendable);

// 2. Calculate total balance with fold
let total_balance: u64 = utxos
.iter()
.map(|(_, amount)| amount)
.fold(0, |acc, amount| acc + amount);
println!("Total balance: {} sats", total_balance);

// 3. Find UTXOs needed to cover a 120,000 sat payment
let target = 120_000u64;
let mut accumulated = 0u64;
let selected: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000) // Skip dust
.take_while(|(_, amount)| {
if accumulated >= target {
false
} else {
accumulated += amount;
true
}
})
.collect();
println!("Selected for payment: {:?}", selected);

// 4. Transform to display format using map and collect
let display_strings: Vec<String> = utxos
.iter()
.map(|(txid, amount)| format!("{}...:{} sats", txid, amount))
.collect();
println!("Display: {:?}", display_strings);
}
```


### Wprowadzenie do inteligentnych wskaźników


Inteligentne wskaźniki to struktury danych, które działają jak tradycyjne wskaźniki, ale zapewniają dodatkowe możliwości i automatyczne zarządzanie pamięcią. W przeciwieństwie do prostych referencji, inteligentne wskaźniki są właścicielami danych, na które wskazują i mogą implementować niestandardowe zachowanie w zakresie alokacji, dealokacji i wzorców dostępu do pamięci. Są one niezbędnymi narzędziami do zarządzania danymi przydzielonymi na stercie i wdrażania złożonych wzorców własności, które wykraczają poza podstawowy system własności Rust.


Aspekt "smart" wynika z ich zdolności do automatycznej obsługi zadań zarządzania pamięcią, które w przeciwnym razie wymagałyby ręcznej interwencji. Gdy inteligentny wskaźnik wychodzi poza zakres, może automatycznie zwolnić powiązaną pamięć, zmniejszyć liczbę odwołań lub wykonać inne operacje czyszczenia. Automatyzacja ta pomaga zapobiegać wyciekom pamięci i błędom use-after-free, zapewniając jednocześnie większą elastyczność niż alokacja oparta wyłącznie na stosie.


Inteligentne wskaźniki zazwyczaj implementują dwie kluczowe cechy: `Deref` i `Drop`. Cecha `Deref` pozwala na użycie inteligentnego wskaźnika tak, jakby był on odniesieniem do zawartych danych. Cecha `Drop` umożliwia niestandardową logikę czyszczenia, gdy inteligentny wskaźnik zostanie zniszczony. Razem, cechy te pozwalają inteligentnym wskaźnikom na automatyczne zarządzanie pamięcią.


### Inteligentny wskaźnik Box


`Box<T>` jest najprostszym inteligentnym wskaźnikiem, zapewniającym alokację sterty dla dowolnego typu `T`. Kiedy tworzysz `Box`, zawarta w nim wartość jest przechowywana na stercie, a nie na stosie, a sam `Box` (który jest tylko wskaźnikiem) jest przechowywany na stosie. To pośrednictwo jest użyteczne, gdy potrzebujesz przechowywać duże ilości danych bez przenoszenia ich, gdy potrzebujesz typu o nieznanym rozmiarze w czasie kompilacji lub gdy chcesz efektywnie przenieść własność danych sterty.


Tworzenie `Box` jest proste: `let boxed_value = Box::new(42);` alokuje liczbę całkowitą na stercie. `Box` automatycznie zarządza tą pamięcią - gdy `Box` wychodzi poza zakres, automatycznie dealokuje pamięć sterty. To automatyczne czyszczenie zapobiega wyciekom pamięci bez konieczności ręcznego zarządzania pamięcią.


Jednym z najważniejszych przypadków użycia `Box` jest umożliwienie rekurencyjnych struktur danych. Rozważmy połączoną listę, gdzie każdy węzeł zawiera wartość i wskaźnik do następnego węzła. Bez `Box` nie można zdefiniować takiej struktury, ponieważ kompilator nie może określić rozmiaru typu, który zawiera sam siebie. Używając `Box<Node>` dla następnego wskaźnika, łamiemy problem rekurencyjnego rozmiaru, ponieważ `Box` ma znany, stały rozmiar niezależnie od tego, co zawiera.


### Implementacja cechy Deref


Cecha `Deref` pozwala na dereferencję typu przy użyciu operatora `*`, dzięki czemu inteligentne wskaźniki zachowują się jak referencje do zawartych w nich danych. Kiedy zaimplementujesz `Deref` dla inteligentnego wskaźnika, włączysz automatyczne dereferencje, które sprawiają, że inteligentny wskaźnik jest przezroczysty w użyciu. Oznacza to, że można wywoływać metody na zawartym typie bezpośrednio przez inteligentny wskaźnik bez jawnego dereferencjonowania.


Cecha `Deref` definiuje powiązany typ `Target`, który określa jaki typ referencji powinna wygenerować operacja dereferencji. Cecha wymaga implementacji metody `deref`, która zwraca referencję do typu docelowego. Dla `Box<T>`, implementacja zwraca referencję do zawartej wartości `T`.


Rust wykonuje automatyczną koercję deref, co oznacza, że kompilator może automatycznie wstawiać wywołania `deref`, gdy jest to potrzebne do zapewnienia zgodności typów. To dlatego można przekazać `String` do funkcji oczekującej `&str` - kompilator automatycznie dereferencjonuje `String` by uzyskać wycinek łańcucha. Ta koercja może łączyć wiele poziomów, więc `Box<String>` może zostać automatycznie przekonwertowany na `&str` poprzez wiele operacji deref.


### Niestandardowa implementacja Drop


Cecha `Drop` pozwala określić niestandardowy kod czyszczący, który jest uruchamiany, gdy wartość wychodzi poza zakres. Jest to szczególnie ważne dla inteligentnych wskaźników, które zarządzają zasobami wykraczającymi poza zwykłą pamięć, takimi jak uchwyty plików, połączenia sieciowe lub liczniki referencji. Cecha `Drop` posiada pojedynczą metodę, `drop`, która pobiera zmienne odniesienie do `self` i wykonuje czyszczenie.


Większość typów nie potrzebuje niestandardowych implementacji `Drop`, ponieważ Rust automatycznie obsługuje upuszczanie ich pól. Jednak inteligentne wskaźniki często potrzebują niestandardowej logiki, aby prawidłowo wyczyścić zasoby, którymi zarządzają. Na przykład inteligentny wskaźnik zliczający referencje musi zmniejszyć liczbę referencji i potencjalnie usunąć współdzielone dane, gdy ostatnie odniesienie zostanie usunięte.


Można również jawnie porzucić wartość, zanim wyjdzie ona poza zakres, używając `std::mem::drop()`. Funkcja ta przejmuje własność wartości i natychmiast ją upuszcza, co może być przydatne do wczesnego zwalniania zasobów lub zapewnienia, że czyszczenie odbywa się w określonym punkcie programu. Jawna funkcja drop jest tylko funkcją tożsamości, która przejmuje własność - prawdziwa praca ma miejsce, gdy wartość jest usuwana na końcu funkcji.


Ten fundament domknięć, iteratorów i inteligentnych wskaźników daje programistom Rust narzędzia do pisania ekspresyjnego, bezpiecznego i wydajnego kodu. Funkcje te współpracują ze sobą, aby umożliwić wspólne wzorce programowania przy jednoczesnym zachowaniu podstawowych gwarancji bezpieczeństwa pamięci i wydajności Rust.



## Liczenie referencji i zmienność wnętrza

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### Zliczanie referencji za pomocą RC


Licznik referencyjny reprezentuje kolejny podstawowy typ inteligentnego wskaźnika w Rust, zaprojektowany specjalnie w celu umożliwienia wielu scenariuszy własności. W przeciwieństwie do Box, który jest zgodny z tradycyjnymi zasadami pojedynczej własności, gdzie jeden podmiot jest właścicielem danych, RC (Reference Counter) pozwala wielu częściom kodu na współdzielenie własności tych samych danych jednocześnie. Ten model współdzielonej własności działa poprzez mechanizm zliczania, który śledzi, ile odwołań istnieje do określonego fragmentu danych.


System zliczania referencji działa poprzez utrzymywanie wewnętrznego licznika, który zwiększa się za każdym razem, gdy klonujesz RC i zmniejsza się, gdy RC zostanie porzucony. Pamięć jest zwalniana tylko wtedy, gdy licznik osiągnie zero, zapewniając, że dane pozostają ważne tak długo, jak długo istnieje jakiekolwiek odniesienie. Takie podejście zapobiega przedwczesnej deallokacji, jednocześnie umożliwiając elastyczne wzorce udostępniania danych, które byłyby niemożliwe w przypadku prostej własności Box.


Praktyczny przykład, w którym RC jest przydatny, obejmuje tworzenie współdzielonych struktur danych, takich jak połączone listy, w których wiele list może odwoływać się do tego samego fragmentu ogona. Rozważmy próbę utworzenia dwóch oddzielnych list, które odwołują się do wspólnego podciągu. W przypadku własności Box staje się to niemożliwe, ponieważ przeniesienie współdzielonej części na pierwszą listę przenosi własność, uniemożliwiając jej użycie na drugiej liście. RC rozwiązuje ten problem, umożliwiając klonowanie referencji, a nie danych bazowych, dzięki czemu współdzielona struktura jest możliwa przy zachowaniu bezpieczeństwa pamięci.


Kiedy klonujesz RC, nie duplikujesz wewnętrznych danych, niezależnie od ich rozmiaru lub złożoności. Zamiast tego tworzone jest kolejne odwołanie do tej samej lokalizacji pamięci i inkrementowany jest licznik odwołań. Sprawia to, że klonowanie instancji RC jest wydajne nawet w przypadku dużych struktur danych, ponieważ kopiowane jest tylko samo odniesienie, podczas gdy dane bazowe pozostają na swoim miejscu.


### Zmienność wewnętrzna z RefCell


RefCell wprowadza wewnętrzną mutowalność, która pozwala na mutowanie danych, nawet jeśli masz do nich tylko niezmienne odniesienie. Możliwość ta zasadniczo zmienia sposób egzekwowania reguł pożyczania Rust poprzez przeniesienie kontroli z czasu kompilacji do czasu wykonywania. Podczas gdy normalne referencje polegają na kompilatorze w celu zweryfikowania bezpieczeństwa pożyczania, RefCell przeprowadza te kontrole podczas wykonywania programu, zapewniając większą elastyczność kosztem potencjalnej paniki w czasie wykonywania.


Podstawową zasadą RefCell jest utrzymywanie tych samych reguł pożyczania, które Rust normalnie egzekwuje w czasie kompilacji, ale sprawdzanie ich dynamicznie. W dowolnym momencie można mieć jedno zmienne odniesienie lub dowolną liczbę niezmiennych odniesień do danych wewnątrz RefCell. Jeśli kod będzie próbował naruszyć te zasady, tworząc jednocześnie sprzeczne zapożyczenia, program wpadnie w panikę, zamiast generować niezdefiniowane zachowanie.


To sprawdzanie w czasie wykonywania umożliwia pewne wzorce programowania, które kompilator może odrzucić, nawet jeśli są one w rzeczywistości bezpieczne. Analiza statyczna kompilatora nie zawsze jest w stanie udowodnić, że złożone wzorce zapożyczeń są poprawne, co skłania go do zachowania ostrożności. RefCell pozwala na pominięcie tych konserwatywnych ograniczeń, gdy jesteś pewien poprawności swojego kodu, ale ta pewność wiąże się z odpowiedzialnością za zapewnienie właściwego użycia, aby uniknąć awarii w czasie wykonywania.


Częstym przypadkiem użycia RefCell są obiekty mock w scenariuszach testowych. Podczas implementacji cechy, która zapewnia jedynie niezmienny dostęp do siebie, ale implementacja makiety musi wewnętrznie śledzić zmiany stanu, RefCell umożliwia ten wzorzec. Możesz zawinąć stan wewnętrzny w RefCell, pozwalając makiecie na mutowanie danych śledzenia nawet za pośrednictwem niezmiennego interfejsu.


### Połączenie RC i RefCell dla współdzielonego zmiennego stanu


Połączenie RC i RefCell tworzy wzorzec dla współdzielonego, zmiennego stanu, w którym wielu właścicieli może potencjalnie modyfikować te same dane. RC zapewnia możliwość współdzielenia własności, podczas gdy RefCell umożliwia mutację poprzez niezmienne referencje. Ta kombinacja jest przydatna w scenariuszach takich jak struktury grafów, pamięci podręczne lub w każdej sytuacji, w której wiele części programu potrzebuje zarówno odczytu, jak i zapisu do współdzielonych danych.


Zawijając RefCell wewnątrz RC, tworzysz strukturę, która może być klonowana i dystrybuowana w całym programie, a każdy klon zapewnia dostęp do tych samych podstawowych zmiennych danych. Wszyscy właściciele mogą potencjalnie modyfikować dane za pomocą metody borrow_mut RefCell, ale nadal muszą przestrzegać reguł pożyczania w czasie wykonywania. Ten wzorzec umożliwia tworzenie złożonych scenariuszy współdzielenia danych przy jednoczesnym zachowaniu gwarancji bezpieczeństwa Rust poprzez kontrole w czasie wykonywania.


Elastyczność ta wiąże się jednak z ważnymi zastrzeżeniami dotyczącymi wycieków pamięci i cykli referencyjnych. Podczas korzystania z RC z RefCell możliwe staje się przypadkowe utworzenie odwołań cyklicznych, w których struktury danych odwołują się do siebie bezpośrednio lub poprzez łańcuch odwołań. Cykle te uniemożliwiają osiągnięcie zera przez liczbę odwołań, powodując wycieki pamięci, ponieważ dane wydają się zawsze mieć aktywne odniesienia, nawet jeśli nie są już dostępne z reszty programu.


Rozwiązaniem dla cykli referencyjnych jest użycie słabych referencji, które nie przyczyniają się do liczby referencji wykorzystywanych do podejmowania decyzji dotyczących zarządzania pamięcią. Słabe referencje pozwalają utrzymywać połączenia między strukturami danych bez utrzymywania ich przy życiu, przerywając potencjalne cykle przy jednoczesnym zachowaniu możliwości dostępu do powiązanych danych, gdy nadal istnieją.


```rust
use std::rc::Rc;
use std::cell::RefCell;

// Simulating a channel state that multiple components need to access and modify
#[derive(Debug)]
struct ChannelState {
channel_id: String,
local_balance_msat: u64,
remote_balance_msat: u64,
is_active: bool,
}

fn main() {
// Rc<RefCell<T>> allows multiple owners with interior mutability
let channel = Rc::new(RefCell::new(ChannelState {
channel_id: "abc123".to_string(),
local_balance_msat: 1_000_000_000,  // 1M sats in msats
remote_balance_msat: 500_000_000,
is_active: true,
}));

// Clone Rc to share ownership (cheap - only increments counter)
let channel_for_ui = Rc::clone(&channel);
let channel_for_router = Rc::clone(&channel);

// Reference count is now 3
println!("Reference count: {}", Rc::strong_count(&channel));

// UI component reads the state (immutable borrow)
{
let state = channel_for_ui.borrow();
println!("UI shows balance: {} msats", state.local_balance_msat);
} // borrow ends here

// Router updates the state after a payment (mutable borrow)
{
let mut state = channel_for_router.borrow_mut();
state.local_balance_msat -= 100_000_000; // Sent 100k sats
state.remote_balance_msat += 100_000_000;
println!("Router updated balances");
} // mutable borrow ends here

// Original reference can still read the updated state
let state = channel.borrow();
println!("New local balance: {} msats", state.local_balance_msat);

// WARNING: This would panic at runtime!
// let borrow1 = channel.borrow();
// let borrow2 = channel.borrow_mut(); // PANIC: already borrowed
}
```


### Podstawy bezpieczeństwa wątków i współbieżności


Podejście Rust do współbieżności koncentruje się na zapobieganiu wyścigom danych i kwestiom bezpieczeństwa pamięci w czasie kompilacji. System typów wymusza bezpieczeństwo wątków poprzez cechy takie jak `Send` i `Sync`, które oznaczają typy jako bezpieczne dla transferu między wątkami lub bezpieczne dla współbieżnego dostępu. Ta weryfikacja w czasie kompilacji wyłapuje wiele błędów współbieżności, które w innych językach programowania systemowego pojawiłyby się dopiero w czasie wykonywania.


Tworzenie wątków w Rust odbywa się według prostego wzorca przy użyciu thread::spawn, który pobiera zamknięcie do wykonania w nowym wątku i zwraca uchwyt do zarządzania cyklem życia wątku. Odrodzony wątek działa współbieżnie z głównym wątkiem i można użyć metody join na uchwycie, aby poczekać na zakończenie. Bez wyraźnego dołączenia, wątki odrodzone mogą zostać zakończone, gdy główny wątek zakończy działanie, potencjalnie odcinając niekompletną pracę.


Słowo kluczowe move staje się kluczowe podczas pracy z wątkami, ponieważ zamknięcia przekazywane do odrodzonych wątków często muszą posiadać swoje dane, a nie je pożyczać. Ponieważ odrodzone wątki mogą przeżyć zakres, który je utworzył, pożyczanie danych z zakresu nadrzędnego powoduje potencjalne naruszenia czasu życia. Przeniesienie danych do zamknięcia wątku przenosi własność, zapewniając, że dane pozostaną ważne przez cały okres życia wątku, jednocześnie uniemożliwiając dostęp z pierwotnego zakresu.


Przekazywanie komunikatów stanowi alternatywę dla współbieżności stanu współdzielonego poprzez kanały, które umożliwiają wątkom komunikację poprzez wysyłanie danych, a nie współdzielenie pamięci. Standardowa biblioteka Rust udostępnia kanały Multiple Producer Single Consumer (MPSC), w których wiele wątków może wysyłać komunikaty do pojedynczego wątku odbierającego. Ten wzorzec eliminuje wiele problemów związanych z synchronizacją, całkowicie unikając współdzielenia zmiennego stanu, zamiast tego polegając na wymianie wiadomości w celu koordynacji.


### Współbieżność współdzielonego stanu z muteksem i Arc


Gdy przekazywanie komunikatów nie jest odpowiednie, Rust zapewnia tradycyjną współbieżność stanu współdzielonego poprzez Mutex (wzajemne wykluczanie) w połączeniu z Arc (Atomic Reference Counter). Mutex zapewnia, że tylko jeden wątek może uzyskać dostęp do chronionych danych w danym czasie, wymagając od wątków uzyskania blokady przed uzyskaniem dostępu do danych. Blokada jest automatycznie zwalniana, gdy obiekt strażnika zwrócony przez operację blokady wychodzi poza zakres, zapobiegając typowym scenariuszom zakleszczenia spowodowanym przez zapomniane odblokowania.


Arc służy jako bezpieczny dla wątków odpowiednik RC, wykorzystując operacje atomowe do bezpiecznego zarządzania liczbą referencji w wielu wątkach. Podczas gdy RC działa doskonale w scenariuszach jednowątkowych, jego nieatomowe zliczanie referencji tworzy warunki wyścigu, gdy dostęp jest uzyskiwany z wielu wątków. Liczniki atomowe Arc zapewniają, że modyfikacje liczby referencji odbywają się bezpiecznie nawet przy jednoczesnym dostępie, dzięki czemu nadaje się do udostępniania danych między wątkami.


Połączenie Arc i Mutex tworzy wzorzec dla współdzielonego mutowalnego stanu w programach współbieżnych. Zawijając muteks w łuk, można sklonować łuk, aby rozdzielić dostęp do tego samego muteksu na wiele wątków, przy czym każdy wątek może uzyskać blokadę i bezpiecznie modyfikować chronione dane. Ten wzorzec zapewnia elastyczność współdzielonego stanu przy jednoczesnym zachowaniu gwarancji bezpieczeństwa Rust poprzez weryfikację w czasie kompilacji i blokowanie w czasie wykonywania.


Cechy Send i Sync działają za kulisami, aby zapewnić bezpieczeństwo wątków w czasie kompilacji. Send wskazuje, że typ może być bezpiecznie przeniesiony do innego wątku, podczas gdy Sync wskazuje, że referencje do typu mogą być bezpiecznie współdzielone między wątkami. Większość typów automatycznie implementuje te cechy, gdy ich komponenty są bezpieczne dla wątków, ale niektóre typy, takie jak RC i RefCell, wyraźnie ich nie implementują, ponieważ nie są przeznaczone do współbieżnego dostępu. Ta automatyczna implementacja cech zapobiega przypadkowemu wprowadzeniu naruszeń bezpieczeństwa wątków, jednocześnie umożliwiając bezpiecznym typom płynną pracę w kontekstach współbieżnych.


## Zrozumienie makr Rust

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Wprowadzenie do makr w Rust


Makra w Rust są funkcją metaprogramowania, która pozwala programistom pisać kod, który generuje inny kod w czasie kompilacji. W przeciwieństwie do funkcji, które są wywoływane w czasie wykonywania, makra są rozszerzane na wczesnym etapie procesu kompilacji, przed sprawdzeniem typu i późniejszymi etapami. To fundamentalne rozróżnienie sprawia, że makra są szczególnie przydatne do zmniejszania powtarzalności kodu i tworzenia języków specyficznych dla domeny w programach Rust.


Najbardziej rozpoznawalnym wskaźnikiem wywołania makra jest wykrzyknik (!), który następuje po nazwie makra. Na przykład, używając `println!("Hello, world!")`, nie wywołujesz funkcji, ale makro. To makro rozwija się w bardziej złożony kod, który obsługuje formatowanie i operacje wyjściowe. Wykrzyknik służy jako wizualna wskazówka dla programistów, że ma miejsce generowanie kodu w czasie kompilacji, a nie standardowe wywołanie funkcji.


Rust oferuje trzy różne typy makr, z których każdy służy innym celom w ekosystemie języka:



- Makra funkcyjne**: Przypominają wywołania funkcji, ale działają w czasie kompilacji (np. `vec!`, `println!`)
- Makra pochodne**: Automatyczna implementacja cech dla typów (np. `#[derive(Debug, Clone)]`)
- Makra podobne do atrybutów**: Modyfikują zachowanie elementów kodu, do których są stosowane (np. `#[test]`, `#[tokio::main]`)


Zrozumienie tych różnych typów makr jest niezbędne do skutecznego programowania Rust, ponieważ każdy z nich odnosi się do określonych przypadków użycia i wzorców programowania.


### Rodzaje makr i ich zastosowania


Makra funkcyjne stanowią najczęściej spotykany typ makr w programowaniu Rust. Makra te używają składni podobnej do wywołań funkcji, ale wykonują dopasowywanie wzorców na swoich danych wejściowych do odpowiedniego kodu generate. Makro `vec!` jest powszechnym przykładem tej kategorii, pozwalając programistom na tworzenie i inicjowanie wektorów za pomocą zwięzłej składni. Gdy napiszesz `vec![1, 2, 3, 4]`, makro rozwinie to w kod, który tworzy nowy wektor, przesuwa każdy element indywidualnie i zwraca ukończony wektor.


Makra pochodne zapewniają automatyczne implementacje cech dla niestandardowych typów, znacznie redukując kod boilerplate. Dodając `#[derive(Debug)]` do definicji struct lub enum, instruujesz kompilator do generate kompletnej implementacji cechy Debug dla tego typu. Ta wygenerowana implementacja obsługuje logikę formatowania niezbędną do wyświetlenia zawartości typu w formacie czytelnym dla człowieka. Mechanizm derive obsługuje wiele standardowych cech bibliotecznych, w tym Clone, PartialEq, co czyni go powszechnie używanym narzędziem do redukcji boilerplate.


Makra atrybutowe modyfikują zachowanie elementów kodu, które adnotują, zapewniając sposób dodawania metadanych lub zmiany zachowania kompilacji. Makra te pojawiają się jako atrybuty umieszczone nad definicjami typów, funkcjami lub innymi konstrukcjami kodu. Na przykład, atrybut `#[non_exhaustive]` na wyliczeniu wskazuje, że dodatkowe warianty mogą zostać dodane w przyszłych wersjach, wymagając, by wyrażenia dopasowania zawierały domyślny przypadek. Mechanizm ten zapewnia kompatybilność w przyszłości, zapewniając jednocześnie jasną dokumentację potencjału ewolucji typu.


### Tworzenie niestandardowych makr przypominających funkcje


Pisanie niestandardowych makr funkcyjnych wymaga zrozumienia składni dopasowywania wzorców Rust dla definicji makr. Definicja makra wykorzystuje podejście deklaratywne, w którym określa się wzorce pasujące do różnych formularzy wejściowych i odpowiadających im szablonów generowania kodu. Każde makro może zawierać wiele rozgałęzień, umożliwiając obsługę różnych wzorców wejściowych i generowanie odpowiedniego kodu dla każdego przypadku.


Rozważmy utworzenie niestandardowego makra wektorowego, które demonstruje podstawowe zasady budowy makr. Definicja makra zaczyna się od `macro_rules!`, po którym następuje nazwa makra i seria gałęzi dopasowujących wzorce. Każda gałąź składa się z wzorca, który pasuje do określonej składni wejściowej i szablonu kodu, który generuje odpowiedni kod Rust. Na przykład, prosta gałąź może dopasować puste nawiasy `[]` i kod generate do utworzenia pustego wektora, podczas gdy inna gałąź dopasuje pojedyncze wyrażenie i wygeneruje kod do utworzenia wektora z jednym elementem.


Makra stają się szczególnie przydatne podczas implementacji wzorców zmiennych argumentów przy użyciu składni powtórzeń. Wzorzec `$($x:expr),*` dopasowuje zero lub więcej wyrażeń oddzielonych przecinkami, pozwalając makru na obsługę dowolnej liczby argumentów. Odpowiedni szablon generowania kodu używa `$(vec.push($x);)*` do iteracji po wszystkich dopasowanych wyrażeniach i generate indywidualnych instrukcji push dla każdego z nich. Ten mechanizm powtórzeń pozwala makrom na generate kodu, którego ręczne napisanie byłoby niemożliwe lub bardzo czasochłonne.


```rust
// A macro to create a HashMap with Bitcoin-related data
macro_rules! btc_map {
// Empty case
() => {
std::collections::HashMap::new()
};
// Key-value pairs case
($($key:expr => $value:expr),+ $(,)?) => {
{
let mut map = std::collections::HashMap::new();
$(
map.insert($key, $value);
)+
map
}
};
}

// A macro for logging with context (simulating a derive-like pattern)
macro_rules! log_payment {
($level:ident, $($arg:tt)*) => {
println!(
"[{}] [PAYMENT] {}",
stringify!($level).to_uppercase(),
format!($($arg)*)
)
};
}

fn main() {
// Using the btc_map! macro
let fee_rates = btc_map! {
"high_priority" => 50_u64,    // sats/vbyte
"medium" => 25_u64,
"low" => 10_u64,
};

println!("Fee rates: {:?}", fee_rates);

// Using the log_payment! macro
log_payment!(info, "Sending {} sats to {}", 100_000, "bc1q...");
log_payment!(warn, "Fee rate {} sats/vB is above average", 75);
log_payment!(error, "Payment failed: insufficient funds");

// Standard vec! macro usage comparison
let utxos = vec![50_000_u64, 30_000, 20_000];
let total: u64 = utxos.iter().sum();
println!("Total UTXOs: {} sats", total);
}
```


Proces kompilacji przekształca wywołania makr w rozszerzony kod przed sprawdzeniem typu i optymalizacją. Gdy kompilator napotka wywołanie makra, dopasowuje dane wejściowe do zdefiniowanych wzorców i zastępuje wywołanie makra wygenerowanym kodem. Rozszerzony kod jest następnie poddawany normalnym procesom kompilacji, w tym sprawdzaniu typów i optymalizacji. Narzędzia takie jak `cargo expand` pozwalają programistom na sprawdzenie wygenerowanego kodu, zapewniając cenne możliwości debugowania podczas tworzenia złożonych makr.


### Zaawansowane koncepcje makr i debugowanie


Tworzenie makr wymaga zrozumienia różnicy między wykonywaniem w czasie kompilacji i w czasie wykonywania. Makra wykonują się podczas kompilacji, generując kod, który zostanie uruchomiony w czasie wykonywania. Ta czasowa separacja oznacza, że logika makra nie może zależeć od wartości w czasie wykonywania, ale umożliwia także optymalizacje, w których złożone obliczenia mogą być wykonywane raz podczas kompilacji, a nie wielokrotnie podczas wykonywania.


System dopasowywania wzorców w makrach obsługuje różne specyfikatory fragmentów, które definiują, jakiego rodzaju elementy kodu mogą być dopasowywane. Specyfikator `expr` dopasowuje wyrażenia, `ty` dopasowuje typy, `ident` dopasowuje identyfikatory, a kilka innych zapewnia szczegółową kontrolę nad walidacją danych wejściowych. Specyfikatory te zapewniają, że makra otrzymują poprawne składniowo dane wejściowe i dostarczają jasnych komunikatów o błędach w przypadku napotkania nieprawidłowej składni.


Debugowanie makr stanowi wyjątkowe wyzwanie ze względu na ich naturę w czasie kompilacji. Komenda `cargo expand` jest przydatna do rozwijania makr, ponieważ wyświetla w pełni rozwinięty kod wygenerowany przez wywołania makr. Narzędzie to pozwala programistom zweryfikować, czy ich makra generate zawierają zamierzony kod i zidentyfikować problemy w logice rozszerzania. Gdy kod wygenerowany przez makro zawiera błędy, rozszerzone dane wyjściowe pomagają wskazać, czy problem leży w definicji makra, czy w strukturze wygenerowanego kodu.


Złożone makra mogą implementować wzorce rekurencyjne, w których makro wywołuje samo siebie ze zmodyfikowanymi argumentami w celu obsługi zagnieżdżonego lub iteracyjnego generowania kodu. Makra rekurencyjne wymagają jednak starannego zaprojektowania, aby uniknąć nieskończonej ekspansji i problemów z wydajnością kompilacji. Rozszerzanie makr w czasie kompilacji oznacza, że nawet nieefektywne implementacje makr wpływają jedynie na szybkość kompilacji, a nie na wydajność w czasie wykonywania, ale zbyt złożone makra mogą znacznie spowolnić proces kompilacji.



# Rust I Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Dlaczego Rust dla rozwoju Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


Wybór Rust dla rozwoju Bitcoin i Lightning nie jest przypadkowy. Rozwój Bitcoin wiąże się z wyjątkowymi obowiązkami, które odróżniają go od typowego rozwoju oprogramowania. Podczas pracy z Bitcoin programiści często obsługują fundusze użytkowników w środowisku, w którym błędy mogą być nieodwracalne. W przeciwieństwie do tradycyjnych systemów finansowych z zabezpieczeniami regulacyjnymi i mechanizmami obciążenia zwrotnego, zdecentralizowany charakter Bitcoin oznacza, że po nadaniu transakcji nie ma organu, do którego można by się odwołać w celu odzyskania środków. Ta rzeczywistość wymaga wyższego poziomu odpowiedzialności i precyzji w tworzeniu oprogramowania.


Filozofia "działaj szybko i psuj rzeczy", która sprawdza się w wielu sektorach technologicznych, po prostu nie ma zastosowania do rozwoju Bitcoin. Zamiast tego ekosystem wymaga języków i narzędzi, które pomagają programistom tworzyć solidne, bezpieczne oprogramowanie, w którym awarie są albo zapobiegane, albo obsługiwane z wdziękiem. Właśnie dlatego wiele znaczących projektów Bitcoin skłania się ku Rust, w tym Bitcoin Development Kit (BDK), Lightning Development Kit (LDK) i BreezSDK.


Rust oferuje trzy podstawowe właściwości, które sprawiają, że jest on szczególnie odpowiedni do rozwoju Bitcoin: statyczny silny system typów, bogate nowoczesne narzędzia i kompatybilność międzyplatformowa. Każda z tych cech przyczynia się do zdolności języka do pomagania programistom w pisaniu bezpieczniejszego, bardziej niezawodnego kodu do obsługi operacji kryptowalutowych.


### Statyczny system silnego typu Rust


System typów Rust zapewnia zarówno statyczną, jak i silną charakterystykę typowania, które współpracują ze sobą w celu wychwycenia błędów, zanim będą one mogły wpłynąć na użytkowników. Statyczna natura oznacza, że sprawdzanie typów odbywa się w czasie kompilacji, wymagając od programistów rozwiązywania niezgodności typów jeszcze przed utworzeniem programu. Kontrastuje to z dynamicznie typowanymi językami, w których błędy typu pojawiają się dopiero w czasie wykonywania, potencjalnie po wdrożeniu oprogramowania i obsłudze rzeczywistych funduszy użytkowników.


Siła systemu typów Rust odnosi się do jego ekspresywności i rygoru w modelowaniu problemów. W przeciwieństwie do języków o słabszych systemach typów, takich jak C, gdzie programiści są ograniczeni do podstawowych typów, takich jak liczby i struktury, Rust pozwala na bogate modelowanie typów, które może dokładnie reprezentować złożone koncepcje domeny. Można na przykład tworzyć typy, które rozróżniają różne rodzaje list lub wymuszają, że pewne operacje są wykonywane tylko na określonych typach obiektów.


To, co sprawia, że system typów Rust jest istotny dla rozwoju Bitcoin, to jego podejście do bezpieczeństwa pamięci. Ten sam system typów, który modeluje logikę biznesową, obsługuje również własność pamięci i współdzieloną kontrolę dostępu. Ta podwójna odpowiedzialność oznacza, że powszechne klasy luk w zabezpieczeniach, takie jak wycieki pamięci, błędy double-free i warunki wyścigu, są całkowicie eliminowane przez kompilator. System typów wymusza te gwarancje bezpieczeństwa poprzez koncepcje takie jak własność, pożyczanie i liczenie referencji, dzięki czemu niezwykle trudno jest wprowadzić błędy związane z pamięcią, które mogłyby zagrozić bezpieczeństwu lub stabilności.


```rust
// Example: Type-safe Bitcoin amount handling
// Using newtypes to prevent mixing up satoshis and other values

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Satoshis(u64);

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct FeeRate(u64); // sats per vbyte

impl Satoshis {
fn from_btc(btc: f64) -> Self {
Satoshis((btc * 100_000_000.0) as u64)
}

fn as_btc(&self) -> f64 {
self.0 as f64 / 100_000_000.0
}
}

// Calculate fee given tx size - type system ensures we can't mix up values
fn calculate_fee(tx_size_vbytes: u32, rate: FeeRate) -> Satoshis {
Satoshis(tx_size_vbytes as u64 * rate.0)
}

fn main() {
let payment = Satoshis::from_btc(0.001); // 100,000 sats
let fee_rate = FeeRate(25);              // 25 sats/vbyte
let tx_size = 250_u32;                   // vbytes

let fee = calculate_fee(tx_size, fee_rate);
println!("Payment: {:?} ({} BTC)", payment, payment.as_btc());
println!("Fee: {:?}", fee);

// This would NOT compile - type safety prevents mixing values:
// let bad_fee = calculate_fee(tx_size, payment); // ERROR: expected FeeRate, found Satoshis
}
```


### Nowoczesne narzędzia i obsługa wielu platform


Ekosystem narzędzi Rust zapewnia programistom narzędzia, które pomagają zwiększyć produktywność i jakość kodu. Sam kompilator Rust został zaprojektowany nie tylko do tłumaczenia kodu na postać binarną, ale także jako narzędzie edukacyjne, które pomaga programistom uczyć się i doskonalić. W przypadku wystąpienia błędów kompilacji, kompilator dostarcza szczegółowych wyjaśnień, co poszło nie tak i często sugeruje konkretne poprawki. Takie podejście jest szczególnie cenne dla programistów, którzy dopiero zaczynają pracę z Rust, ponieważ kompilator skutecznie uczy dobrych praktyk i pomaga zapobiegać typowym błędom.


Język zawiera Cargo, ujednolicony menedżer pakietów, który obsługuje zarządzanie zależnościami, budowanie, testowanie i generowanie dokumentacji. Ta standaryzacja eliminuje fragmentację widoczną w starszych językach, takich jak C++, gdzie wiele konkurujących ze sobą narzędzi powoduje niespójność między projektami. Cargo obsługuje również rozszerzenia takie jak rustfmt do formatowania kodu i Clippy do analizy statycznej, zapewniając, że kod jest zgodny z wytycznymi dotyczącymi stylu i wychwytuje potencjalne problemy, zanim staną się problemami.


Wieloplatformowe możliwości Rust wykraczają poza tradycyjne systemy operacyjne i obejmują platformy mobilne, takie jak Android i iOS, a także WebAssembly dla aplikacji opartych na przeglądarce. Ta wieloplatformowa obsługa jest przydatna dla aplikacji Bitcoin, które muszą działać w różnych środowiskach. Na przykład projekty takie jak Mutiny Wallet wykorzystują kompilację WebAssembly Rust do tworzenia portfeli Lightning, które działają bezpośrednio w przeglądarkach internetowych, co byłoby niepraktyczne w przypadku tradycyjnych technologii internetowych.


### Zrozumienie typów błędów i ich konsekwencji


Skuteczna obsługa błędów zaczyna się od zrozumienia różnych kategorii błędów, które mogą wystąpić podczas wykonywania programu. Rozważmy prostą aplikację routingu, która oblicza ścieżki między punktami geograficznymi. Ten przykład ilustruje trzy podstawowe typy błędów, które programiści muszą rozwiązać: nieprawidłowe błędy wejściowe, błędy zasobów uruchomieniowych i błędy logiczne.


Nieprawidłowe błędy wejściowe występują, gdy funkcja otrzymuje parametry, które nie spełniają jej wymagań. Na przykład, jeśli system współrzędnych geograficznych używa liczb całkowitych ze znakiem dla długości geograficznej, ale otrzymuje wartość ujemną, gdy prawidłowe są tylko wartości dodatnie, funkcja nie może kontynuować sensownie. Błędy te stanowią naruszenie umowy między wywołującym a funkcją, a odpowiednią reakcją jest zazwyczaj odrzucenie danych wejściowych i zwrócenie wskazania błędu.


Błędy zasobów środowiska uruchomieniowego występują, gdy zewnętrzne zależności są niedostępne lub niedostępne. Odczyt pliku mapy może się nie powieść, ponieważ plik nie istnieje, aplikacja nie ma odpowiednich uprawnień lub urządzenie pamięci masowej jest niedostępne. Błędy te są zewnętrzne w stosunku do logiki programu i często wymagają poprawek środowiskowych, a nie zmian w kodzie. Jednak solidne aplikacje muszą przewidywać i obsługiwać te scenariusze z wdziękiem.


Błędy logiczne reprezentują błędy w implementacji programu lub nieporozumienia dotyczące sposobu interakcji komponentów. Jeśli algorytm routingu zwraca pustą ścieżkę, gdy podano prawidłowe punkty początkowe i końcowe, oznacza to błąd logiczny, który należy poprawić w samym kodzie. W przeciwieństwie do innych typów błędów, błędy logiczne zazwyczaj wymagają debugowania i modyfikacji kodu.


### Strategie solidnego zarządzania błędami


Tworzenie niezawodnego oprogramowania wymaga proaktywnych strategii, które minimalizują możliwości wystąpienia błędów i sprawnie radzą sobie z nieuniknionymi błędami. Pierwsza strategia polega na ograniczaniu możliwych błędów poprzez staranne projektowanie typów. Wybierając typy, które mogą reprezentować tylko prawidłowe wartości, programiści mogą wyeliminować całe klasy nieprawidłowych błędów wejściowych. Na przykład użycie liczb całkowitych bez znaku dla wartości, które nie mogą być ujemne, zapobiega błędom wartości ujemnych w czasie kompilacji.


Asercje zapewniają kolejną warstwę ochrony poprzez wyraźne sprawdzanie, czy oczekiwane warunki są prawdziwe podczas wykonywania programu. Kontrole te służą wielu celom: wyłapują błędy podczas testowania, powodują wczesne awarie programów w przypadku wystąpienia problemów (ułatwiając debugowanie) i służą jako wykonywalna dokumentacja opisująca założenia programisty. Gdy asercja nie powiedzie się, oznacza to, że podstawowe założenie dotyczące stanu programu zostało naruszone, zazwyczaj wskazując na błąd logiczny, który wymaga zbadania.


Zasada warstwowych abstrakcji pomaga zarządzać złożonością poprzez zapewnienie, że błędy są obsługiwane na odpowiednich poziomach systemu. Wewnętrzne szczegóły implementacji, w tym określone typy błędów z bibliotek niższego poziomu, nie powinny rozprzestrzeniać się poza granice podsystemu. Zamiast tego każda warstwa powinna tłumaczyć błędy na terminy, które mają znaczenie na tym poziomie abstrakcji. Na przykład, aplikacja wallet używająca biblioteki Bitcoin powinna tłumaczyć niskopoziomowe błędy parsowania deskryptora na komunikaty wyższego poziomu, takie jak "nieprawidłowa konfiguracja wallet", które dostarczają użytecznych informacji użytkownikom lub kodowi wywołującemu.


Takie podejście do obsługi błędów, w połączeniu z systemem typów i narzędziami Rust, pomaga wychwycić potencjalne problemy na wczesnym etapie procesu rozwoju, zanim mogą one wpłynąć na użytkowników lub zagrozić bezpieczeństwu aplikacji Bitcoin.



## Model błędu

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

Rust zapewnia kompleksowe podejście do obsługi błędów, które równoważy bezpieczeństwo z praktycznością. Podczas gdy ogólne koncepcje modelu błędów mają zastosowanie we wszystkich językach programowania, Rust oferuje konkretne narzędzia i wzorce, które sprawiają, że obsługa błędów jest zarówno jawna, jak i łatwa w zarządzaniu. Zrozumienie tych mechanizmów ma kluczowe znaczenie dla pisania solidnych aplikacji Rust, które mogą z wdziękiem radzić sobie z nieoczekiwanymi sytuacjami, zachowując jednocześnie wydajność i bezpieczeństwo.


### Panika i jej właściwe zastosowanie


Mechanizm paniki Rust reprezentuje najbardziej bezpośredni sposób obsługi nienaprawialnych błędów. Po wywołaniu makra `panic!`, program natychmiast zatrzymuje wykonywanie, albo przerywa, albo rozwija się w zależności od konfiguracji. Makro panic akceptuje komunikat łańcuchowy, który opisuje, co poszło nie tak, zapewniając kontekst do debugowania. Dodatkowo, metody takie jak `unwrap()` i `expect()` na typach Result i Option służą jako skróty do paniki, gdy typy te zawierają odpowiednio wartości błędu lub None. Metoda `expect()` pozwala na dostarczenie niestandardowej wiadomości, czyniąc ją nieco bardziej informacyjną niż `unwrap()` podczas debugowania błędów.


Pomimo swojej prostoty, panika powinna być używana rozsądnie w kodzie produkcyjnym. Istnieje kilka scenariuszy, w których panika jest nie tylko akceptowalna, ale wręcz zalecana. Podczas pisania przykładów lub prototypów, panika zapewnia czysty sposób na skupienie się na podstawowej funkcjonalności bez zaśmiecania kodu kompleksową obsługą błędów. W środowiskach testowych panika jest często pożądanym zachowaniem, gdy asercje zawodzą, ponieważ wyraźnie wskazuje, że wystąpiło coś nieoczekiwanego. Społeczność Rust uznaje również sytuacje, w których programiści mają większą wiedzę niż kompilator, na przykład podczas analizowania zakodowanych na stałe adresów IP, o których wiadomo, że są prawidłowe.


Jednak pozorne bezpieczeństwo panik "zweryfikowanych przez kompilator" może być zwodnicze. Rozważmy scenariusz, w którym zakodowałeś na sztywno adres IP i użyłeś funkcji `expect()`, ponieważ wiesz, że jest poprawny. Z biegiem czasu, w miarę ewolucji kodu, ta zakodowana na stałe wartość może zostać przekształcona w stałą, a później ta stała może zostać zmieniona na coś w rodzaju "localhost" dla lepszego doświadczenia użytkownika. Nagle "bezpieczna" panika staje się awarią w czasie wykonywania. Ta ewolucja pokazuje, dlaczego generalnie lepiej jest unikać paniki w kodzie produkcyjnym i zamiast tego zwracać odpowiednie typy błędów, które mogą być obsługiwane z wdziękiem.


Jeden godny uwagi wyjątek od zasady "unikaj paniki" dotyczy operacji na muteksach. Kiedy wywołujesz `lock()` na muteksie, zwraca on Wynik, ponieważ blokada może się nie powieść, jeśli inny wątek spanikował podczas trzymania muteksu. Tworzy to mylącą sytuację, w której lokalny kod otrzymuje błąd za coś, co wydarzyło się w zupełnie innym kontekście. Ponieważ nie można rozsądnie obsłużyć błędu, który powstał w wyniku paniki innego wątku, wielu programistów uważa za dopuszczalne rozpakowywanie blokad muteksów, zwłaszcza jeśli utrzymujesz wolną od paniki bazę kodu w innym miejscu.


### Praca z typami wyników i opcji


Typ Result stanowi podstawę systemu obsługi błędów Rust. Jako wyliczenie, które może zawierać `Ok(wartość)` lub `Err(błąd)`, Result zmusza do wyraźnego potwierdzenia, że operacje mogą się nie powieść. Typ Option służy podobnemu celowi w przypadkach, gdy wartość może być po prostu nieobecna, zawierając `Some(value)` lub `None`. Chociaż Option nie dostarcza szczegółowych informacji o błędach, jest idealny w sytuacjach, w których brak wartości jest znaczący i oczekiwany.


Zarówno Result jak i Option udostępniają kilka metod, które czynią obsługę błędów bardziej ergonomiczną. Metoda `unwrap_or()` zwraca zawartą wartość, jeśli jest obecna, lub wartość domyślną, jeśli wystąpił błąd lub brak. Ten wzorzec jest szczególnie przydatny, gdy mamy rozsądne rozwiązanie awaryjne, takie jak parsowanie danych wejściowych użytkownika z rozsądną wartością domyślną, gdy parsowanie nie powiedzie się. Metoda `unwrap_or_default()` działa podobnie, ale używa domyślnej wartości typu zamiast wymagać jej określenia. Podczas gdy metody te technicznie nie obsługują błędów w tradycyjnym sensie, zapewniają one sposób na łagodne obniżenie funkcjonalności w przypadku wystąpienia problemów.


Operator znaku zapytania (`?`) jest zwięzłą składnią propagacji błędów. Po zastosowaniu do wyniku lub opcji, wyodrębnia on wartość sukcesu, jeśli jest obecna, lub natychmiast zwraca błąd z bieżącej funkcji, jeśli wystąpił problem. Operator ten eliminuje rozwlekłe wzorce sprawdzania błędów powszechne w językach takich jak Go, gdzie trzeba ręcznie sprawdzać i zwracać błędy na każdym kroku. Operator znaku zapytania zasadniczo zapewnia cukier syntaktyczny dla wczesnych zwrotów, umożliwiając pisanie czystego, liniowego kodu, który koncentruje się na szczęśliwej ścieżce, automatycznie obsługując propagację błędów.


### Zaawansowane wzorce obsługi błędów


Metoda `map()` na typach Result i Option umożliwia obsługę błędów w stylu funkcjonalnym, co może uczynić kod bardziej ekspresyjnym i łatwym do skomponowania. Kiedy wywołujesz `map()` na Result, dostarczona funkcja jest stosowana do wartości sukcesu, jeśli jest obecna, podczas gdy błędy są automatycznie propagowane bez modyfikacji. Ten wzorzec jest przydatny podczas łączenia operacji w łańcuchy, ponieważ można skupić się na przekształcaniu wartości bez wielokrotnej obsługi przypadków błędów. Metoda `map_err()` zapewnia odwrotną funkcjonalność, pozwalając na przekształcanie typów błędów, pozostawiając wartości sukcesu bez zmian.


Transformacja błędów staje się kluczowa podczas tworzenia aplikacji warstwowych, w których różne komponenty wymagają różnych typów błędów. Rozważmy funkcję, która analizuje dane wejściowe użytkownika i musi konwertować niskopoziomowe błędy parsowania na błędy specyficzne dla domeny. Używając `map_err()`, można łatwo przetłumaczyć ogólny błąd "nieprawidłowy format liczby" na bardziej kontekstowy błąd "nieprawidłowy wiek", który ma sens w domenie aplikacji. Ta transformacja odbywa się bezpośrednio w miejscu wystąpienia błędu, dzięki czemu kod jest bardziej czytelny i łatwiejszy w utrzymaniu niż tradycyjne bloki try-catch, w których obsługa błędów jest oddzielona od operacji, które mogą zakończyć się niepowodzeniem.


Połączenie operatora znaku zapytania z mapowaniem błędów tworzy zwięzłe wzorce obsługi błędów. Można łączyć operacje w łańcuchy, przekształcać błędy w razie potrzeby i propagować je w górę stosu wywołań przy minimalnej ilości szablonów. Takie podejście utrzymuje obsługę błędów blisko operacji, które mogą zakończyć się niepowodzeniem, zachowując jednocześnie czystą separację między ścieżkami sukcesu i błędów.


```rust
use std::fmt;

// Layered error types for a wallet application
#[derive(Debug)]
enum NetworkError {
ConnectionFailed(String),
Timeout,
}

#[derive(Debug)]
enum WalletError {
Network(NetworkError),
InvalidAddress(String),
InsufficientFunds { required: u64, available: u64 },
}

// Implement Display for user-friendly messages
impl fmt::Display for WalletError {
fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
match self {
WalletError::Network(e) => write!(f, "Network error: {:?}", e),
WalletError::InvalidAddress(addr) => write!(f, "Invalid address: {}", addr),
WalletError::InsufficientFunds { required, available } =>
write!(f, "Need {} sats but only have {} available", required, available),
}
}
}

// Convert from lower-level error to domain error
impl From<NetworkError> for WalletError {
fn from(err: NetworkError) -> Self {
WalletError::Network(err)
}
}

// Simulated network call
fn fetch_balance(address: &str) -> Result<u64, NetworkError> {
if address.starts_with("bc1") {
Ok(500_000) // 500k sats
} else {
Err(NetworkError::ConnectionFailed("Invalid endpoint".into()))
}
}

// Higher-level function using ? with automatic error conversion
fn send_payment(from: &str, amount: u64) -> Result<String, WalletError> {
let balance = fetch_balance(from)?; // NetworkError auto-converts to WalletError

if balance < amount {
return Err(WalletError::InsufficientFunds {
required: amount,
available: balance,
});
}

Ok(format!("Sent {} sats", amount))
}

fn main() {
match send_payment("bc1qtest...", 100_000) {
Ok(msg) => println!("Success: {}", msg),
Err(e) => println!("Failed: {}", e), // User-friendly message
}
}
```


### Biblioteki zewnętrzne i ekosystemy obsługi błędów


Ekosystem Rust zawiera kilka popularnych bibliotek, które rozszerzają możliwości obsługi błędów biblioteki standardowej. Biblioteka `anyhow` zapewnia uproszczone podejście do obsługi błędów, oferując uniwersalny typ błędu, który może automatycznie konwertować z dowolnego typu błędu, który implementuje standardową cechę Error. Ta automatyczna konwersja pozwala na użycie operatora znaku zapytania z różnymi typami błędów bez ręcznej konwersji, co czyni go szczególnie przydatnym w aplikacjach, w których nie trzeba programowo rozróżniać różnych typów błędów.


Podczas gdy `anyhow` doskonale upraszcza obsługę błędów w aplikacjach, w których błędy są głównie wyświetlane użytkownikom, ma on ograniczenia w tworzeniu bibliotek. Ponieważ `anyhow` zasadniczo konwertuje wszystkie błędy na komunikaty łańcuchowe, konsumenci biblioteki nie mogą łatwo programowo reagować na różne warunki błędu. To ograniczenie sprawia, że `anyhow` jest bardziej odpowiedni dla aplikacji użytkownika końcowego niż dla bibliotek, które muszą dostarczać ustrukturyzowane informacje o błędach swoim konsumentom.


Bardziej zaawansowane podejścia do obsługi błędów obejmują tworzenie niestandardowych typów błędów, które modelują określone tryby awarii aplikacji lub biblioteki. Dobrze zaprojektowany model błędów może rozróżniać nieprawidłowe dane wejściowe (które wywołujący może naprawić), błędy uruchomieniowe (które mogą być ponawiane) i trwałe awarie (które wskazują na błędy lub nienaprawialne warunki). Takie ustrukturyzowane podejście umożliwia konsumentom kodu podejmowanie inteligentnych decyzji dotyczących sposobu reagowania na różne rodzaje awarii, niezależnie od tego, czy oznacza to ponawianie operacji, monitowanie użytkowników o inne dane wejściowe, czy zgłaszanie błędów programistom.


## UniFFI, połączenie bibliotek Rust z wieloma językami


<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### Wprowadzenie do UniFFI i rozwoju międzyplatformowego


UniFFI to narzędzie do udostępniania bibliotek Rust w wielu językach programowania i na różnych platformach. Narzędzie to, opracowane przez Mozillę, stanowi odpowiedź na podstawowe wyzwanie związane z tworzeniem nowoczesnego oprogramowania: jak wykorzystać zalety Rust w zakresie wydajności i bezpieczeństwa przy jednoczesnym zachowaniu kompatybilności z różnymi ekosystemami programistycznymi. Narzędzie automatycznie generuje powiązania językowe dla bibliotek Rust, eliminując potrzebę ręcznego tworzenia przez programistów kodu interfejsu dla każdego języka docelowego.


Podstawowy problem rozwiązywany przez UniFFI wynika z natury Rust jako języka kompilowanego. Gdy kod Rust jest kompilowany, generuje on binarne dane wyjściowe z funkcją obcą Interface (FFI), która prezentuje niskopoziomowy interfejs, który może być trudny do użycia bezpośrednio z języków wyższego poziomu, takich jak Python, Swift lub Kotlin. Tradycyjnie, każdy programista biblioteki musiałby napisać niestandardowy kod wiążący dla każdego języka docelowego, tworząc znaczącą barierę dla adopcji międzyplatformowej. UniFFI eliminuje tę nadmiarowość, zapewniając znormalizowane podejście do automatycznego generowania tych powiązań.


Filozofia projektowania narzędzia koncentruje się na umożliwieniu programistom Rust skupienia się na podstawowej logice biznesowej, jednocześnie udostępniając swoje biblioteki programistom pracującym w innych językach. Na przykład programista iOS korzystający ze Swift może korzystać z biblioteki Rust za pośrednictwem powiązań wygenerowanych przez UniFFI, które prezentują całkowicie natywny interfejs Swift, bez wskazania, że podstawowa implementacja jest napisana w Rust. Ta płynna integracja pozwala zespołom wykorzystać zalety wydajności Rust bez konieczności uczenia się Rust przez wszystkich członków zespołu.


### Zrozumienie architektury i przepływu pracy UniFFI


UniFFI działa poprzez dobrze zdefiniowany przepływ pracy, który przekształca biblioteki Rust w pakiety kompatybilne z wieloma językami. Proces rozpoczyna się od utworzenia pliku Unified Definition Language (UDL), który służy jako specyfikacja interfejsu opisująca, które części biblioteki Rust powinny być dostępne dla innych języków. Ten plik UDL działa jako umowa między implementacją Rust a wygenerowanymi powiązaniami językowymi.


Architektura jest wyraźnie rozdzielona. Programiści utrzymują swoją bibliotekę Rust ze standardowymi idiomami i wzorcami Rust, a następnie tworzą oddzielny plik UDL, który mapuje interfejs publiczny do systemu typów UniFFI. Generator powiązań UniFFI przetwarza zarówno bibliotekę Rust, jak i specyfikację UDL, aby wygenerować powiązania w języku natywnym dla żądanych platform docelowych. Te wygenerowane wiązania obsługują wszystkie złożone operacje marshalingu i unmarshalingu danych między środowiskiem wykonawczym języka obcego a kodem Rust.


W czasie wykonywania architektura tworzy warstwowe podejście, w którym kod aplikacji napisany w języku docelowym (takim jak Kotlin dla Androida) współdziała z wygenerowanym kodem wiążącym, który wydaje się całkowicie natywny dla tego języka. Ta warstwa wiążąca obsługuje tłumaczenie między typami specyficznymi dla języka a typami Rust, bezpiecznie zarządza pamięcią ponad granicami językowymi i zapewnia obsługę błędów zgodną z konwencjami języka docelowego. Podstawowa logika biznesowa Rust pozostaje niezmieniona i nieświadoma wielu interfejsów językowych zbudowanych na niej.


### Praca z UDL: definicja i mapowanie typów Interface


Unified Definition Language służy jako kamień węgielny funkcjonalności UniFFI, zapewniając deklaratywny sposób określania, które części biblioteki Rust powinny być eksponowane i jak powinny być prezentowane w językach docelowych. Pliki UDL muszą zawierać co najmniej jedną przestrzeń nazw, która działa jako kontener dla funkcji, które mogą być wywoływane bezpośrednio bez konieczności tworzenia instancji obiektu. Te funkcje przestrzeni nazw zazwyczaj obsługują proste operacje, które przyjmują wartości jako parametry i zwracają wyniki.


UDL obsługuje kompleksowy zestaw wbudowanych typów, które w naturalny sposób mapują się na odpowiadające im typy Rust. Podstawowe typy obejmują standardowe prymitywy, takie jak boole, różne rozmiary liczb całkowitych (u8, u32 itp.), liczby zmiennoprzecinkowe i ciągi znaków. Bardziej złożone typy obejmują wektory, mapy hash i specyficzne dla Rust koncepcje, takie jak typy Option (reprezentowane za pomocą składni znaku zapytania) i typy Result do obsługi błędów. System typów obsługuje również wyliczenia, zarówno proste wyliczenia oparte na wartościach, jak i złożone wyliczenia, które zawierają powiązane dane, umożliwiając modelowanie danych, które przekłada się na granice językowe.


Struktury w Rust tłumaczą się na słowniki w UDL, zachowując zgodność prawie jeden do jednego, jednocześnie dostosowując się do konwencji składni UDL. Gdy struktury Rust mają powiązane metody, mogą być eksponowane jako interfejsy w UDL, które generate jako klasy z metodami w obiektowych językach docelowych, takich jak Kotlin lub Swift. Takie mapowanie zachowuje obiektowe wzorce projektowe, których programiści oczekują w tych językach, przy jednoczesnym zachowaniu struktury i zachowania bazowej implementacji Rust.


```
// Example UDL file for a Bitcoin wallet library (wallet.udl)
namespace wallet {
// Namespace functions - called directly without object
string generate_mnemonic();
Wallet create_wallet(string mnemonic);
};

// Dictionary (struct) - becomes data class in Kotlin, struct in Swift
dictionary Balance {
u64 confirmed_sats;
u64 pending_sats;
};

// Interface (class with methods) - becomes class with methods
interface Wallet {
// Constructor
constructor(string mnemonic);

// Methods
Balance get_balance();
string get_new_address();
string send_to_address(string address, u64 amount_sats);
};

// Enum with data - maps to sealed class (Kotlin) or enum with associated values (Swift)
[Enum]
interface TransactionStatus {
Pending(u32 confirmations_needed);
Confirmed(u32 block_height);
Failed(string reason);
};

// Error enum for Result types
[Error]
enum WalletError {
"InsufficientFunds",
"InvalidAddress",
"NetworkError",
};

// Function that can fail - throws in target language
interface Wallet {
[Throws=WalletError]
string send_to_address(string address, u64 amount_sats);
};
```


Odpowiednia implementacja Rust zdefiniuje te typy i zaimplementuje atrybut `uniffi::export` do wiązań generate dla Kotlin, Swift, Python i innych obsługiwanych języków.


### Obsługa błędów i funkcje zaawansowane


UniFFI zapewnia obsługę błędów, która zachowuje model błędów oparty na wynikach Rust, jednocześnie tłumacząc go odpowiednio dla języków docelowych. Funkcje zwracające typy Result w Rust mogą być oznaczone słowem kluczowym "throws" w UDL, określającym typy błędów, które mogą generować. Błędy te muszą być zdefiniowane jako wyliczenia błędów w pliku UDL i muszą implementować standardową cechę Error Rust w podstawowym kodzie Rust. Krata thiserror zapewnia wygodne makro do implementacji tej cechy, znacznie redukując kod boilerplate.


Tłumaczenie obsługi błędów demonstruje podejście UniFFI uwzględniające język. W Kotlinie funkcje oznaczone jako rzucające w metodach UDL generate, które rzucają wyjątki zgodnie z konwencjami Java/Kotlin. Wiązania Pythona podobnie używają modelu wyjątków Pythona. Tłumaczenie to zapewnia, że obsługa błędów jest naturalna i idiomatyczna w każdym języku docelowym, przy jednoczesnym zachowaniu semantycznego znaczenia oryginalnych typów błędów Rust.


Interfejsy wywołania zwrotnego reprezentują kolejną zaawansowaną funkcję, która umożliwia dwukierunkową komunikację między bibliotekami Rust a aplikacjami. Gdy biblioteka Rust musi oddzwonić do kodu aplikacji, programiści mogą zdefiniować cechy w Rust i oznaczyć je jako interfejsy wywołania zwrotnego w UDL. Aplikacja konsumująca implementuje te interfejsy w swoim rodzimym języku, a UniFFI obsługuje złożony marshaling wymagany do wywołania tych wywołań zwrotnych z kodu Rust. Ten wzorzec wymaga starannego rozważenia bezpieczeństwa wątków, ponieważ wywołania zwrotne mogą przekraczać granice wątków, wymagając granic wysyłania i synchronizacji po stronie Rust.


### Rzeczywiste zastosowania i obecne ograniczenia


UniFFI został przyjęty w społeczności programistów kryptowalut i blockchain, a główne projekty, takie jak BDK (Bitcoin Development Kit), LDK (Lightning Development Kit) i różne implementacje wallet, wykorzystują go do dostarczania mobilnych zestawów SDK. Projekty te demonstrują wykorzystanie UniFFI w środowiskach produkcyjnych.


Analiza rzeczywistych plików UDL z tych projektów ujawnia wzorce i najlepsze praktyki, które wyłoniły się z praktycznego zastosowania. Na przykład plik UDL BDK pokazuje, jak złożone modele domen z wieloma wyliczeniami, strukturami i interfejsami mogą być skutecznie mapowane w celu stworzenia kompleksowych mobilnych zestawów SDK. Spójność składni UDL w różnych projektach oznacza, że programiści zaznajomieni z jedną biblioteką obsługującą UniFFI mogą szybko zrozumieć i pracować z innymi, tworząc efekt sieci, który przynosi korzyści całemu ekosystemowi.


UniFFI ma jednak znaczące ograniczenia, które programiści muszą wziąć pod uwagę. Najważniejszym z nich jest brak obsługi interfejsów asynchronicznych. Wszystkie wygenerowane powiązania są synchroniczne, co wymaga od programistów obsługi operacji asynchronicznych w kodzie Rust i prezentowania synchronicznych interfejsów aplikacjom konsumującym. Dodatkowo, umieszczenie dokumentacji stanowi wyzwanie: dokumentacja napisana w kodzie Rust nie przenosi się do wygenerowanych wiązań, podczas gdy dokumentacja w plikach UDL nie jest dostępna dla bezpośrednich konsumentów biblioteki Rust. Chociaż trwają prace nad rozwiązaniem tych ograniczeń poprzez automatyczne analizowanie i generowanie, pozostają one kwestią do rozważenia dla obecnych implementacji. Wreszcie, UniFFI generuje powiązania językowe, ale nie obsługuje pakowania i dystrybucji specyficznej dla platformy, pozostawiając programistom zarządzanie końcowymi etapami tworzenia pakietów dystrybucyjnych dla każdej platformy docelowej.


# Rozwijanie LNP/BP za pomocą SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## Węzeł LN na SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### Zrozumienie architektury modułowej LDK


Lightning Development Kit (LDK) przyjmuje inne podejście do implementacji Lightning Network w porównaniu do tradycyjnego oprogramowania węzła, takiego jak CLightning lub LND. Podczas gdy konwencjonalne węzły Lightning działają jako kompletne aplikacje daemon działające w sposób ciągły na maszynie, LDK działa jako modułowa biblioteka Rust, która zapewnia prymitywne komponenty do tworzenia niestandardowych rozwiązań Lightning. To rozróżnienie architektoniczne sprawia, że LDK jest elastyczny, umożliwiając programistom łączenie funkcjonalności Lightning w sposób, który spełnia ich specyficzne wymagania projektowe.


Podstawową filozofią LDK jest modułowość i zdolność adaptacji. Zamiast dostarczać monolityczne rozwiązanie, LDK oferuje poszczególne komponenty, które można łączyć, dostosowywać lub całkowicie wymieniać. Każdy komponent zawiera domyślne implementacje, które działają po wyjęciu z pudełka, ale programiści zachowują swobodę zastępowania własnych implementacji w razie potrzeby. Przykładowo, LDK zawiera domyślne implementacje monitorowania blockchain, podpisywania transakcji i komunikacji sieciowej, ale każdy z nich można zastąpić niestandardowymi rozwiązaniami dostosowanymi do konkretnych przypadków użycia lub środowisk.


Ta modułowa konstrukcja umożliwia LDK działanie na różnych platformach i w scenariuszach, które byłyby wyzwaniem dla tradycyjnych węzłów Lightning. Aplikacje mobilne, przeglądarki internetowe, urządzenia wbudowane i specjalistyczny sprzęt mogą wykorzystywać komponenty LDK w sposób dostosowany do ich unikalnych ograniczeń i wymagań. Architektura biblioteki gwarantuje, że programiści mogą tworzyć aplikacje obsługujące Lightning bez konieczności stosowania z góry określonych wzorców operacyjnych lub zależności systemowych.


### Przypadki użycia LDK i elastyczność platformy


Elastyczność architektury LDK otwiera liczne przypadki użycia, które wykraczają daleko poza tradycyjne wdrożenia węzłów Lightning. Rozwój mobilnego wallet stanowi jedno z najbardziej atrakcyjnych zastosowań, w którym LDK umożliwia tworzenie portfeli Lightning bez nadzoru, podobnych do Phoenix wallet. Te mobilne implementacje mogą utrzymywać kontrolę użytkownika nad kluczami prywatnymi, jednocześnie synchronizując się z dostawcami usług Lightning (LSP) po wejściu w tryb online, umożliwiając płynne odbieranie płatności i zarządzanie kanałami nawet przy przerywanej łączności.


Integracja Hardware Security Module (HSM) pokazuje kolejny potężny przypadek użycia LDK. Wyodrębniając tylko komponenty podpisywania i weryfikacji transakcji, deweloperzy mogą tworzyć urządzenia podpisujące świadome Lightning, które rozumieją kontekst i konsekwencje transakcji Lightning. Możliwości te wykraczają poza zwykłe podpisywanie transakcji i obejmują inteligentną analizę przekazywania płatności, operacji kanałowych i decyzji o krytycznym znaczeniu dla bezpieczeństwa. HSM może ocenić, czy transakcja reprezentuje legalną płatność, operację routingu, czy potencjalnie złośliwą próbę, zapewniając użytkownikom znaczący wgląd w bezpieczeństwo.


Oparte na sieci Web aplikacje Lightning czerpią znaczne korzyści z filozofii projektowania LDK bez wywołań systemowych. Ponieważ środowiska WebAssembly nie mają bezpośredniego dostępu do zasobów systemowych, takich jak systemy plików, gniazda sieciowe lub źródła entropii, czyste podejście LDK pozwala na płynne działanie funkcji Lightning w środowiskach przeglądarek. Programiści mogą implementować niestandardowe warstwy sieciowe za pomocą WebSockets i zapewniać kompatybilne z przeglądarką źródła trwałości i losowości, zachowując pełną zgodność z protokołem Lightning.


### Podstawowe komponenty i architektura sterowana zdarzeniami


Wewnętrzna architektura LDK obraca się wokół kilku kluczowych komponentów, które współpracują ze sobą za pośrednictwem systemu sterowanego zdarzeniami. System zarządzania peerami obsługuje całą komunikację z innymi węzłami Lightning, implementując protokół szumu do szyfrowania i zarządzania strukturami wiadomości w celu zapewnienia zgodności z protokołem Lightning. Komponent ten działa niezależnie od podstawowego mechanizmu transportowego, umożliwiając programistom implementację sieci za pośrednictwem gniazd TCP, WebSockets, połączeń szeregowych USB lub dowolnego innego dwukierunkowego kanału komunikacyjnego.


Menedżer kanału służy jako centralny koordynator operacji kanału Lightning, ściśle współpracując z menedżerem równorzędnym w celu wykonywania operacji otwierania, zamykania i płatności kanału. Gdy deweloper inicjuje otwarcie kanału, channel manager tworzy niezbędne komunikaty protokołu i koordynuje z peer managerem obsługę wieloetapowego procesu negocjacji. Ta separacja problemów pozwala na czystą abstrakcję między logiką protokołu Lightning a szczegółami komunikacji sieciowej.


System zdarzeń LDK zapewnia asynchroniczne powiadomienia dla wszystkich istotnych operacji i zmian stanu. Zdarzenia obejmują pełne spektrum operacji Lightning, od połączeń i rozłączeń peer po sukcesy i porażki płatności, zmiany stanu kanału i potwierdzenia blockchain. To podejście oparte na zdarzeniach pozwala aplikacjom odpowiednio reagować na aktywność sieci Lightning, zachowując jednocześnie czystą separację między podstawową funkcjonalnością LDK a logiką specyficzną dla aplikacji. Programiści mogą implementować niestandardowe programy obsługi zdarzeń, które aktualizują interfejsy użytkownika, wyzwalają powiadomienia lub inicjują działania następcze w oparciu o zdarzenia sieci Lightning.


### Blockchain Integracja i zarządzanie danymi


Integracja danych Blockchain stanowi jedną z warstw abstrakcji LDK, zaprojektowaną tak, aby pomieścić wszystko, od pełnych węzłów Bitcoin po lekkich klientów mobilnych. LDK obsługuje dwa podstawowe tryby interakcji blockchain, z których każdy jest zoptymalizowany pod kątem różnych ograniczeń zasobów i wymagań operacyjnych. Tryb pełnego bloku umożliwia aplikacjom z dostępem do pełnych danych blockchain przekazywanie całych bloków do LDK, umożliwiając kompleksowe monitorowanie transakcji i natychmiastową reakcję na istotne zdarzenia blockchain.


W przypadku środowisk o ograniczonych zasobach LDK zapewnia podejście oparte na filtrowaniu, które zmniejsza wymagania dotyczące przepustowości i pamięci masowej. W tym trybie LDK komunikuje swoje zainteresowania monitorowaniem za pośrednictwem abstrakcyjnych interfejsów, żądając nadzoru określonych identyfikatorów transakcji, UTXO lub wzorców skryptów. Warstwa aplikacji może następnie wdrożyć to monitorowanie za pomocą serwerów Electrum, eksploratorów bloków lub innych lekkich źródeł danych blockchain. Takie podejście umożliwia portfelom mobilnym i aplikacjom internetowym utrzymanie funkcjonalności Lightning bez konieczności pełnej synchronizacji łańcucha bloków.


Warstwa trwałości w LDK jest zgodna z tymi samymi zasadami abstrakcji, zapewniając aplikacjom binarne bloki danych, które muszą być niezawodnie przechowywane i pobierane. LDK obsługuje całą złożoność serializacji i deserializacji stanów kanału Lightning, danych plotek sieciowych i innych krytycznych informacji. Aplikacje muszą po prostu wdrożyć niezawodne mechanizmy przechowywania, niezależnie od tego, czy korzystają z lokalnych systemów plików, usług przechowywania w chmurze czy wyspecjalizowanych systemów baz danych. Taka konstrukcja zapewnia, że zarządzanie stanem Lightning pozostaje solidne, jednocześnie umożliwiając aplikacjom wybór rozwiązań pamięci masowej, które odpowiadają ich wymaganiom operacyjnym i modelom bezpieczeństwa.


### Zaawansowane funkcje i wzorce integracji


Możliwości LDK obejmują funkcje Lightning Network, takie jak płatności wielościeżkowe, optymalizacja tras i zarządzanie plotkami sieciowymi. System routingu utrzymuje kompleksowy widok topologii Lightning Network poprzez uczestnictwo w protokole plotek, umożliwiając inteligentne wyszukiwanie ścieżek dla płatności. Aplikacje mogą wpływać na decyzje dotyczące routingu poprzez parametry konfiguracyjne, a nawet mogą implementować niestandardową logikę routingu dla wyspecjalizowanych przypadków użycia.


System powiązań językowych biblioteki umożliwia integrację LDK w wielu środowiskach programistycznych, obsługując Java, Kotlin, Swift, TypeScript, JavaScript i C++. Ta międzyplatformowa kompatybilność pozwala aplikacjom mobilnym napisanym w językach natywnych na włączenie funkcjonalności Lightning przy zachowaniu optymalnej charakterystyki wydajności. System wiążący zachowuje architekturę LDK opartą na zdarzeniach i modułową konstrukcję we wszystkich obsługiwanych językach, zapewniając spójne doświadczenia programistów niezależnie od platformy docelowej.


Szacowanie opłat i nadawanie transakcji to dodatkowe obszary, w których LDK zapewnia elastyczność. Aplikacje mogą wdrażać niestandardowe strategie szacowania opłat, które uwzględniają ich specyficzne wzorce operacyjne i wymagania użytkowników. Podobnie, rozgłaszanie transakcji można dostosować do pracy z różnymi interfejsami sieciowymi Bitcoin, od bezpośrednich połączeń full node po usługi rozgłaszania stron trzecich. Ta elastyczność zapewnia, że aplikacje oparte na LDK mogą zoptymalizować swoje interakcje blockchain pod kątem konkretnych przypadków użycia, zachowując jednocześnie zgodność z protokołem Lightning i standardami bezpieczeństwa.


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### Wyzwanie związane z rozwojem błyskawic


Tworzenie aplikacji integrujących płatności Lightning stanowi istotną barierę dla większości deweloperów. Aby stworzyć aplikację z funkcjonalnością płatności Lightning, deweloperzy muszą zasadniczo stać się ekspertami Lightning, rozumiejąc złożone koncepcje, takie jak zarządzanie kanałami, równoważenie płynności i topologia sieci. Ten wymóg wiedzy specjalistycznej stwarza podstawowy problem dla przyjęcia Lightning: podczas gdy sama sieć Lightning działa, a płatności są niezawodne, złożoność techniczna uniemożliwia powszechną integrację z codziennymi aplikacjami.


Głównym wyzwaniem jest rozdźwięk między potrzebami deweloperów a tym, co chcą oni dostarczyć. Programiści zazwyczaj pracują w napiętych terminach i preferują proste rozwiązania, które pozwalają im skupić się na podstawowej funkcjonalności aplikacji, a nie stać się ekspertami w dziedzinie infrastruktury płatności. Gdy integracja Lightning jest trudna, programiści naturalnie skłaniają się ku rozwiązaniom powierniczym, ponieważ oferują one ścieżkę najmniejszego oporu. Jednak ta tendencja do korzystania z usług powierniczych podważa podstawową wartość Bitcoin, jaką jest brak powierniczej suwerenności finansowej.


### Wizja Breez, błyskawice wszędzie


Breez wyłonił się z prostej, ale ambitnej wizji: aby każdy mógł połączyć się z siecią Lightning poprzez intuicyjne interfejsy do gospodarki Lightning. Podejście firmy uznaje, że chociaż sieć Lightning działa dobrze pod względem technicznym, rozpaczliwie potrzebuje przyjęcia przez użytkowników, aby osiągnąć swój pełny potencjał. Wyzwanie to wykracza poza indywidualnych użytkowników i obejmuje cały ekosystem aplikacji i usług, które mogą skorzystać z integracji Lightning.


Oryginalna aplikacja Breez zademonstrowała tę wizję, zapewniając użytkownikom bezobsługowy węzeł Lightning działający bezpośrednio na ich telefonach komórkowych. Aplikacja ta prezentowała możliwości Lightning, takie jak strumieniowe przesyłanie mikropłatności do podcasterów i funkcjonalność punktu sprzedaży. Jednak aplikacja Breez ujawniła również krytyczne ograniczenie architektoniczne: ekosystem aplikacji mobilnych nie ułatwia łatwej komunikacji między aplikacjami, zmuszając programistów do tworzenia wszystkich funkcji związanych z Lightning w jednej aplikacji, zamiast umożliwiać wyspecjalizowanym aplikacjom korzystanie ze wspólnej infrastruktury Lightning.


Wnioski wyciągnięte przez firmę z aplikacji Breez doprowadziły do kluczowego spostrzeżenia: przyszłość przyjęcia Lightning zależy od pozyskania deweloperów. Jeśli integracja Lightning bez nadzoru stanie się najłatwiejszą opcją dla programistów, stanie się domyślnym wyborem. Podejście to oferuje również korzyści regulacyjne, ponieważ oprogramowanie niebędące usługą powierniczą napotyka mniej przeszkód regulacyjnych niż usługi powiernicze, co ułatwia deweloperom dostarczanie aplikacji na całym świecie.


### Architektura Breez SDK


Breez SDK zapewnia alternatywne podejście do integracji funkcjonalności Lightning z aplikacjami. Zamiast wymagać od każdej aplikacji uruchamiania własnego węzła Lightning, SDK zapewnia architekturę, która zachowuje zasady braku odpowiedzialności, jednocześnie upraszczając doświadczenie programisty. Zasadniczo SDK zapewnia każdemu użytkownikowi końcowemu własny węzeł Lightning działający w infrastrukturze Greenlight, opartej na chmurze usłudze hostingu węzłów Lightning firmy Blockstream.


Architektura ta rozwiązuje kilka krytycznych problemów jednocześnie. Użytkownicy nie muszą martwić się o zarządzanie bazami danych, czas pracy serwerów lub utrzymanie infrastruktury - kwestie, które byłyby przytłaczające dla typowych konsumentów. Jednak w przeciwieństwie do tradycyjnych rozwiązań powierniczych, Greenlight nigdy nie ma dostępu do kluczy użytkowników. Węzeł Lightning w chmurze nie może wykonywać żadnych operacji bez aktywnie połączonej aplikacji, która może podpisywać transakcje i wiadomości. Ten projekt zachowuje korzyści bezpieczeństwa wynikające z samodzielnego przechowywania, jednocześnie eliminując złożoność operacyjną.


SDK obsługuje również interoperacyjność. Wiele aplikacji może łączyć się z węzłem Lightning tego samego użytkownika przy użyciu tej samej frazy seed, umożliwiając użytkownikom utrzymanie pojedynczego salda Lightning w różnych wyspecjalizowanych aplikacjach. Na przykład użytkownik może mieć zarówno ogólną aplikację Lightning wallet, jak i wyspecjalizowaną aplikację do podcastów, obie uzyskujące dostęp do tych samych funduszy i kanałów Lightning. Architektura ta umożliwia rozwój ukierunkowanych, wyspecjalizowanych aplikacji przy jednoczesnym zachowaniu ujednoliconej infrastruktury finansowej.


### Dostawcy usług błyskawicznych i płynność Just-in-Time


Kluczowym elementem Breez SDK jest jego integracja z dostawcami usług Lightning (LSP), którzy działają analogicznie do dostawców usług internetowych, ale dla sieci Lightning. LSP rozwiązują jedno z najbardziej złożonych wyzwań Lightning: zarządzanie płynnością. W kanałach Lightning fundusze mogą przepływać tylko w kierunkach, w których istnieje płynność, podobnie jak koraliki na liczydle, które mogą poruszać się tylko tam, gdzie jest miejsce.


SDK implementuje kanały "just-in-time" za pośrednictwem LSP, automatycznie zarządzając płynnością bez interwencji użytkownika. Gdy użytkownik musi otrzymać płatność, ale nie ma wystarczającej płynności przychodzącej, LSP automatycznie otwiera nowy kanał Lightning w momencie nadejścia płatności. Proces ten odbywa się płynnie w tle, zapewniając użytkownikom możliwość otrzymywania płatności bez konieczności rozumienia mechaniki kanału.


Ta integracja LSP wykracza poza proste zarządzanie płynnością. SDK zawiera kompleksową funkcjonalność Lightning od razu po wyjęciu z pudełka: wbudowane usługi watchtower dla bezpieczeństwa, interoperacyjność on-chain poprzez swapy podmorskie, fiat on-ramps poprzez usługi takie jak MoonPay oraz wsparcie dla protokołów LNURL. System zapewnia również płynne tworzenie kopii zapasowych i odzyskiwanie danych, dzięki czemu użytkownicy nigdy nie tracą dostępu do swoich środków, nawet jeśli dostawcy infrastruktury zmienią się lub staną się niedostępni.


### Wdrożenie i doświadczenie dewelopera


Breez SDK stawia na pierwszym miejscu doświadczenie dewelopera dzięki kompleksowemu podejściu obejmującemu baterie. SDK zapewnia powiązania dla wielu języków programowania, w tym Rust, Swift, Kotlin, Python, Go, React Native, Flutter i C#, umożliwiając programistom integrację płatności Lightning przy użyciu preferowanych narzędzi programistycznych. Architektura abstrahuje od złożoności Lightning poprzez interfejsy API, zachowując jednocześnie bezpieczeństwo sieci Lightning.


Kluczowe komponenty współpracują ze sobą, aby zapewnić to uproszczone doświadczenie. Parser wejściowy automatycznie obsługuje różne formaty płatności, określając, czy ciąg znaków reprezentuje fakturę, LNURL lub inną metodę płatności i kierując go do odpowiedniej funkcji obsługi. Zintegrowany podpisujący zarządza wszystkimi operacjami kryptograficznymi w tle, podczas gdy swapper obsługuje interakcje on-chain w sposób przejrzysty. Taka konstrukcja pozwala programistom skupić się na unikalnej propozycji wartości ich aplikacji, zamiast stawać się ekspertami od infrastruktury Lightning.


Architektura SDK zapewnia, że chociaż Greenlight może obserwować stany kanałów i informacje o routingu, nie może uzyskać dostępu do środków użytkownika ani wykonywać nieautoryzowanych operacji. Użytkownicy zachowują pełną kontrolę nad swoimi kluczami prywatnymi, które nigdy nie opuszczają ich urządzeń. Podejście to stanowi starannie przemyślany kompromis między prostotą operacyjną a prywatnością, zapewniając praktyczną ścieżkę do przyjęcia Lightning w głównym nurcie, przy jednoczesnym zachowaniu podstawowych zasad Bitcoin dotyczących suwerenności finansowej.


## LDK vs Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### Zrozumienie ograniczeń zestawu Lightning Development Kit (LDK)


Lightning Development Kit to zbiór bibliotek Rust zaprojektowanych w celu zapewnienia programistom elastyczności podczas tworzenia aplikacji Lightning Network. Elastyczność ta wiąże się jednak ze znacznymi wyzwaniami implementacyjnymi, które ujawniły się podczas rzeczywistego rozwoju w Lipa. Niskopoziomowy charakter LDK oznacza, że deweloperzy muszą obsługiwać wiele złożonych zadań niezależnie, od synchronizacji grafu sieciowego po optymalizację routingu płatności. Chociaż takie podejście zapewnia pełną kontrolę nad implementacją Lightning, wymaga znacznych zasobów programistycznych i głębokiej wiedzy technicznej, aby osiągnąć niezawodność gotową do produkcji.


Jedną z najbardziej krytycznych brakujących funkcji w LDK była obsługa LNURL, szeroko przyjętego standardu, który upraszcza interakcje Lightning Network dla użytkowników końcowych. Dodatkowo, brak wyjść kotwicy stanowił poważne wyzwanie operacyjne, szczególnie w środowiskach o wysokich opłatach. Wyjścia Anchor rozwiązują podstawowy problem związany z wymuszonym zamykaniem kanałów Lightning: gdy opłaty sieciowe gwałtownie rosną, kanały z predefiniowanymi opłatami mogą stać się niemożliwe do jednostronnego zamknięcia, ponieważ wstępnie ustawiona opłata staje się niewystarczająca do potwierdzenia transakcji. Ograniczenie to okazało się szczególnie problematyczne w przypadku mobilnych aplikacji wallet, w których użytkownicy mogą porzucić wallet bez skoordynowania wspólnych zamknięć kanałów, pozostawiając środki potencjalnie osierocone podczas skoków opłat.


Względna niedojrzałość LDK przejawiała się również w niewiarygodnym routingu płatności, co jest krytyczną kwestią dla każdej aplikacji Lightning. Pomimo tego, że LDK był technicznie solidną implementacją, jego szeroki zakres jako ogólnego rozwiązania utrudniał szybkie rozwiązywanie konkretnych problemów. Zespół programistów spędzał dużo czasu na rozwiązywaniu problemów z routingiem i wdrażaniu funkcji, które w idealnym przypadku powinny być obsługiwane na poziomie biblioteki, co ostatecznie wpływało na szybkość rozwoju i jakość doświadczenia użytkownika.


### Odkrywanie zalet Breez SDK i Greenlight


Przejście na Breez SDK stanowiło zmianę podejścia architektonicznego, polegającą na przejściu z samodzielnie zarządzanego węzła Lightning na rozwiązanie oparte na chmurze, obsługiwane przez usługę Greenlight firmy Blockstream. Zmiana ta natychmiast rozwiązała kilka krytycznych problemów związanych z implementacją LDK. Najbardziej znacząca poprawa nastąpiła w zakresie niezawodności płatności, głównie ze względu na zdolność Greenlight do utrzymywania zawsze aktualnego wykresu sieci. W przeciwieństwie do tradycyjnych mobilnych implementacji Lightning, które muszą synchronizować informacje o sieci po uruchomieniu aplikacji, węzły Greenlight działają nieprzerwanie w chmurze, utrzymując świadomość sieci w czasie rzeczywistym i natychmiast dostarczając kompletne dane wykresu, gdy użytkownicy się łączą.


Architektura ta wykorzystuje sprawdzoną w boju implementację Core Lightning (CLN), która od lat z powodzeniem routuje płatności jako jedna z oryginalnych implementacji Lightning Network. Zgromadzone doświadczenie i sprawdzona niezawodność CLN zapewniły natychmiastową poprawę stabilności w porównaniu z młodszym projektem LDK. Gdy użytkownicy aktywują swoje wallet zasilane przez Greenlight, natychmiast dziedziczą pełną wiedzę o sieci i możliwości routingu stale działającego węzła Lightning, eliminując opóźnienia synchronizacji i niepewność routingu, które nękały poprzednią implementację.


Opiniotwórcza filozofia projektowania Breez SDK była przydatna dla rozwoju wallet. Zamiast dostarczać ogólny zestaw narzędzi Lightning, Breez koncentruje się w szczególności na aplikacjach wallet dla użytkowników końcowych, umożliwiając zespołowi programistów skoncentrowanie wysiłków na tworzeniu kompleksowych rozwiązań dla tego konkretnego przypadku użycia. To ukierunkowane podejście umożliwiło Breez zintegrowanie podstawowych usług bezpośrednio z SDK, w tym funkcji Lightning Service Provider (LSP), która umożliwia użytkownikom otrzymywanie płatności natychmiast po instalacji wallet, bez konieczności ręcznego otwierania kanałów.


### Kompleksowe funkcje i ulepszenia doświadczenia użytkownika


Zintegrowane podejście Breez SDK wykracza poza podstawową funkcjonalność Lightning, obejmując funkcje, które zwiększają komfort użytkowania. Wbudowana integracja LSP eliminuje tradycyjną barierę wymagającą od użytkowników zrozumienia zarządzania kanałami, umożliwiając natychmiastowe otrzymywanie płatności dla nowych instalacji wallet. Ten proces wdrażania pomaga w przyjęciu do głównego nurtu, ponieważ użytkownicy mogą zacząć otrzymywać płatności Lightning bez wiedzy technicznej lub procedur konfiguracji.


Funkcja wymiany w łańcuchu zapewnia kolejną warstwę optymalizacji doświadczenia użytkownika, umożliwiając prezentację ujednoliconego salda użytkownikom. Zamiast zmuszać użytkowników do zrozumienia różnicy między Lightning i on-chain Bitcoin, usługa swap umożliwia automatyczną konwersję między tymi warstwami w razie potrzeby. Gdy użytkownicy muszą dokonać płatności on-chain, system może płynnie zamienić środki Lightning na on-chain Bitcoin za kulisami, utrzymując iluzję pojedynczego, płynnego salda, jednocześnie obsługując złożoność techniczną wewnętrznie.


Wsparcie SDK dla zerowych rezerw kanałowych jest odpowiedzią na istotne wyzwanie związane z doświadczeniem użytkownika w tradycyjnych implementacjach Lightning. Rezerwy kanałów zazwyczaj uniemożliwiają użytkownikom wydawanie pełnego wyświetlanego salda, powodując zamieszanie, gdy płatności nie powiodą się pomimo pozornie wystarczających środków. Eliminując te rezerwy, Breez umożliwia użytkownikom wydawanie pełnego wyświetlanego salda, choć wymaga to od LSP zaakceptowania dodatkowego ryzyka. Ten kompromis stanowi przykład podejścia Breez skoncentrowanego na użytkowniku, w którym złożoność techniczna i ryzyko są absorbowane przez dostawców usług w celu stworzenia intuicyjnych doświadczeń użytkownika.


Dodatkowe funkcje, takie jak obsługa LNURL, usługi kursowe i synchronizacja wielu urządzeń, dodatkowo demonstrują kompleksowe podejście SDK do rozwoju wallet. Architektura oparta na chmurze umożliwia użytkownikom dostęp do węzła Lightning z wielu urządzeń lub aplikacji, a Breez obsługuje synchronizację stanu między tymi różnymi punktami dostępu. Przyszłe pozycje na mapie drogowej obejmują funkcjonalność "spend-all" dla pełnego drenażu wallet, splicing dla dynamicznego zarządzania kanałami oraz rynek konkurencyjnych LSP w celu wprowadzenia zdrowej konkurencji w świadczeniu usług.


### Ocena kompromisów i obaw związanych z centralizacją


Przejście na Breez SDK i Greenlight wprowadza ważne kompromisy w zakresie centralizacji, które należy dokładnie rozważyć w kontekście zasad decentralizacji Bitcoin. Architektura oparta na chmurze oznacza, że węzły Lightning użytkowników działają w infrastrukturze Blockstream, tworząc zależności zarówno od ciągłego działania Greenlight, jak i ciągłego rozwoju Breez. Ta centralizacja wykracza poza zwykłą wygodę, potencjalnie wpływając na zdolność użytkowników do odzyskania środków, jeśli usługi staną się niedostępne lub wystąpi cenzura.


Scenariusze odzyskiwania stanowią szczególne wyzwanie w tej architekturze. Podczas gdy użytkownicy zachowują kontrolę nad swoimi kluczami prywatnymi, dostęp do funduszy bez infrastruktury Greenlight wymagałby wiedzy technicznej, aby uruchomić niezależne węzły Core Lightning i przywrócić stany kanałów. Dla indywidualnych użytkowników ten proces odzyskiwania prawdopodobnie okazałby się zbyt skomplikowany, a nawet dostawcy wallet stanęliby przed poważnymi wyzwaniami związanymi z migracją całych baz użytkowników do alternatywnej infrastruktury, gdyby usługi Greenlight zostały przerwane.


Wraz z tą zmianą architektoniczną zmieniają się również kwestie prywatności. Routing oparty na chmurze oznacza, że Greenlight potencjalnie zyskuje wgląd w miejsca docelowe płatności, podczas gdy poprzednie architektury oparte wyłącznie na LSP ograniczały wyciek informacji do kwot i terminów płatności. Generowanie Invoice w chmurze dodatkowo zwiększa potencjalną ekspozycję na informacje, ponieważ niewykorzystane faktury, które wcześniej pozostawały prywatne na urządzeniach użytkowników, przechodzą teraz przez infrastrukturę Blockstream.


Pomimo tych obaw związanych z centralizacją, praktyczne korzyści często przewyższają teoretyczne ryzyko dla wielu przypadków użycia. Zwiększona niezawodność, kompleksowy zestaw funkcji i doskonałe wrażenia użytkownika umożliwiają programistom wallet skupienie się na innowacjach w warstwie aplikacji, a nie na zarządzaniu infrastrukturą Lightning. Ten podział pracy odzwierciedla dojrzewający ekosystem, w którym wyspecjalizowani dostawcy usług radzą sobie ze złożonymi wyzwaniami technicznymi, pozwalając twórcom aplikacji skoncentrować się na doświadczeniach użytkowników i logice biznesowej. Kluczem jest jasne zrozumienie tych kompromisów i podejmowanie świadomych decyzji w oparciu o konkretne wymagania dotyczące przypadków użycia i poziomy tolerancji ryzyka.




# Sekcja końcowa

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Recenzje i oceny

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Wnioski

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>