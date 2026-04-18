---
name: Wprowadzenie do Bitcoin mining
goal: Zrozumienie Bitcoin mining i proof-of-work od podstaw
objectives: 


  - Zrozumienie proof-of-work i jego roli w Bitcoin.
  - Przeanalizuj mechanizm regulacji trudności.
  - Dowiedz się, co tak naprawdę oznaczają terminy techniczne związane z mining.
  - Opisz kroki związane z budową bloku Bitcoin i jego komponentów.
  - Identyfikacja głównych wydarzeń w branży mining.


---

# Poznaj podstawy Bitcoin mining



Zrozumienie proof of work jest równoznaczne ze zrozumieniem działania Bitcoin. Bez tego wynalazku i jego genialnego zastosowania Bitcoin po prostu nie mógłby istnieć. Ten kurs zapewnia całą teorię mining potrzebną do podróży bitcoinowej.



MIN 101 jest skierowany przede wszystkim do początkujących, ponieważ wyjaśnia wszystkie koncepcje dokładnie od podstaw. Jeśli jednak masz już średniozaawansowaną wiedzę, ten kurs pozwoli ci skonsolidować swoje zrozumienie, skorygować niektóre przybliżone intuicje i zbadać szczegóły często pomijane w głównych wyjaśnieniach.



Pod koniec tego kursu będziesz w stanie wyjaśnić, jak działa proof-of-work w prosty i rygorystyczny sposób. MIN 101 jest również idealnym wprowadzeniem do wszystkich innych bardziej zaawansowanych kursów poświęconych Bitcoin mining na Plan ₿ Academy, zarówno teoretycznych, jak i praktycznych.



+++


# Wprowadzenie


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Przegląd kursu


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Witamy w kursie MIN 101, w którym poznasz podstawowe koncepcje teoretyczne mining i Proof-of-Work w systemie Bitcoin. Ten kurs jest pierwszym krokiem w podróży bitcoinera, aby zrozumieć, jak działa mining. Po jego ukończeniu będziesz mógł przejść do bardziej zaawansowanych kursów teoretycznych lub samemu zostać górnikiem bitcoinów!



W tym kursie MIN 101 nie będziemy wracać do podstawowych koncepcji Bitcoin, ponieważ przejdziemy od razu do sedna sprawy: mining. Jeśli nigdy nie słyszałeś o Bitcoin lub jeśli jego podstawy są dla ciebie nadal nieco niejasne, zdecydowanie zalecam rozpoczęcie od naszego wprowadzającego kursu BTC 101. Po zapoznaniu się z tymi podstawami, będziesz w stanie pewnie poradzić sobie z MIN 101:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Część 1 - Wprowadzenie



Rozpoczniemy ten kurs od opcjonalnego pierwszego rozdziału, w którym przedstawię bardzo uproszczone wyjaśnienie mining, aby dać ci jasny obraz mentalny przed przejściem do mechanizmów technicznych.



Celem nie jest tutaj podanie wszystkich szczegółów technicznych (pojawią się one w dalszej części kursu), ale zapewnienie wątku przewodniego. Po wprowadzeniu tych ram, każda bardziej zaawansowana koncepcja wprowadzona później będzie naturalnie pasować do tej struktury.



### Część 2 - Jak działa proof of work



Po wprowadzeniu, część 2 stanowi techniczną podstawę programu szkoleniowego. Jej celem jest wyjaśnienie, krok po kroku, w jaki sposób Bitcoin tworzy prawidłowe bloki. Zaczniemy od odkrycia struktury bloku, zanim przejdziemy do mechanizmu proof-of-work: roli celu, nonce i funkcji skrótu. Na koniec zobaczymy, w jaki sposób Bitcoin udaje się utrzymać stabilny wskaźnik produkcji bloków pomimo wahań mocy hashowania, dzięki mechanizmowi dostosowywania trudności. Pod koniec tej sekcji będziesz miał pełne zrozumienie podstawowych zasad Bitcoin proof-of-work.



### Część 3 - System motywacyjny Bitcoin mining



W trzeciej części przyjrzymy się, dlaczego górnicy są zachęcani do uczciwego udziału w mining. Wyszczególnimy zasadę nagrody blokowej, jej skład i metodę obliczania, jej ewolucję w czasie poprzez halvingi oraz szczególną rolę transakcji coinbase.



### Część 4 - Przemysł Bitcoin mining



Czwarta część umieszcza mining z powrotem w rzeczywistości operacyjnej. Śledzimy ewolucję maszyn mining, od początku Bitcoin do nowoczesnego ASIC, aby zrozumieć obecne ograniczenia sprzętowe. Przyglądamy się również podstawom puli mining, aby zrozumieć, w jaki sposób górnikom udaje się zmniejszyć zmienność ich dochodów.



### Część 5 - Sekcja końcowa



W końcowej części kursu możesz sprawdzić swoją wiedzę na temat mining, zdobywając dyplom.



Celem tego kursu MIN 101 jest zatem umożliwienie opuszczenia go z jasnym, ustrukturyzowanym i trwałym zrozumieniem Bitcoin mining, zarówno pod względem technicznym, jak i ekonomicznym.



Gotowy do odkrycia Bitcoin mining? Zaczynajmy!




## Bitcoin mining w prosty sposób


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Zanim przejdę do szczegółowego i bardziej technicznego wyjaśnienia Bitcoin [mining](https://planb.academy/resources/glossary/mining), chciałbym dać ci przegląd zasady, która jest celowo prosta i schematyczna. Jeśli masz już podstawową wiedzę, możesz przejść od razu do sedna sprawy w następnym rozdziale, po udzieleniu odpowiedzi na pytania quizowe. Ten rozdział jest przeznaczony przede wszystkim dla początkujących, aby zapewnić ci łagodny start.



Wyobraź sobie Bitcoin jako duży publiczny notatnik, współdzielony przez wszystkich, w którym zapisujemy, kto wysłał bitcoiny do kogo. Ten notatnik nazywa się [blockchain](https://planb.academy/resources/glossary/blockchain). Nie może być przechowywany przez jedną osobę, w przeciwnym razie musiałby być zaufany. Zamiast tego Bitcoin działa zbiorowo: tysiące komputerów weryfikują i utrzymują tę samą wersję tego notatnika.



![Image](assets/fr/049.webp)



W Bitcoin podczas dokonywania płatności tworzona jest [transakcja](https://planb.academy/resources/glossary/transaction-tx). Transakcja ta nie jest natychmiast dodawana do notesu. Jest ona najpierw wysyłana do sieci, a następnie czeka na integrację z następnym pakietem transakcji. Pakiet ten nazywany jest [blokiem](https://planb.academy/resources/glossary/block).



![Image](assets/fr/050.webp)



Blok to po prostu zestaw transakcji zgrupowanych razem. Gdy blok jest gotowy, nie wystarczy go opublikować. Musisz udowodnić sieci, że blok jest wart dodania do puli. W tym miejscu pojawia się mining.



Mining to praca polegająca na walidacji bloku poprzez zużycie energii. Podmioty zwane [górnikami](https://planb.academy/resources/glossary/miner) używają wyspecjalizowanych komputerów. Maszyny te zużywają energię elektryczną do przeprowadzenia bardzo dużej liczby testów w pętli, aż znajdą dowód, który zostanie zaakceptowany przez sieć. Gdy górnik znajdzie taki dowód, jego blok jest uznawany za ważny.



Po zweryfikowaniu bloku jest on rozgłaszany w sieci. Pozostałe [węzły](https://planb.academy/resources/glossary/node) szybko sprawdzają, czy jest on zgodny z zasadami, a następnie dodają go do sekwencji poprzednich bloków. Właśnie dlatego nazywa się to "łańcuchem bloków": każdy nowy blok pojawia się po innych, w kolejności sekwencyjnej, a ten łańcuch rośnie stopniowo.



![Image](assets/fr/051.webp)



Podsumowując, najpierw tworzone są transakcje. Następnie są one grupowane w blok. Następnie górnik zatwierdza ten blok, zużywając energię elektryczną. Na koniec blok ten jest dodawany do łańcucha bloków, a zawarte w nim transakcje zostają [potwierdzone](https://planb.academy/resources/glossary/confirmation).



Jeśli górnicy zużywają energię elektryczną, to nie dlatego, że są wolontariuszami. Robią to, ponieważ jest za to nagroda. Kiedy górnik zatwierdza blok, otrzymuje dwa rodzaje dochodu. Z jednej strony otrzymuje nowo utworzone bitcoiny. Z drugiej strony pobiera [opłaty](https://planb.academy/resources/glossary/transaction-fees) uiszczane przez użytkowników za transakcje zawarte w bloku. Innymi słowy, górnik jest wynagradzany zarówno poprzez zaprogramowaną emisję pieniądza, jak i opłaty transakcyjne ustalane przez rynek.



Na tym etapie celowo przedstawiono bardzo prosty widok mining. Nie wyjaśnia on jeszcze szczegółowo, w jaki sposób blok jest zbudowany, ani jak dokładnie działa dowód, którego szukają górnicy, ani w jaki sposób Bitcoin utrzymuje stałe tempo, ani w jaki sposób nagroda jest dokładnie obliczana, ani w jaki sposób jest żądana. Nic nie szkodzi, to wszystko, co zobaczymy w dalszej części tego kursu MIN 101!



Celem tego rozdziału było po prostu przedstawienie jasnej struktury mentalnej: transakcje → bloki → mining → blockchain → nagroda. Należy pamiętać o tym łańcuchu pomysłów. W pozostałej części kursu każdy rozdział będzie dodawał warstwę szczegółów technicznych do jednego z tych elementów, aż zrozumiesz nie tylko, co się dzieje, ale także jak i dlaczego działa to niezawodnie, na dużą skalę, bez szefa i bez potrzeby zaufania.



# Jak działa proof of work


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## Ścieżka transakcji Bitcoin


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



Aby zrozumieć, na czym polega Bitcoin mining, musimy najpierw prześledzić ścieżkę typowej transakcji Bitcoin. To pokaże ci dokładnie, gdzie pojawia się blok i dlaczego jest on sercem systemu. To właśnie chciałbym odkryć w tym pierwszym rozdziale.



W Bitcoin transakcja jest strukturą danych, która przenosi własność bitcoinów z jednego użytkownika na drugiego. Mówiąc konkretnie, zużywa "[wyjścia](https://planb.academy/resources/glossary/output)" z poprzednich transakcji (tzw. [UTXO](https://planb.academy/resources/glossary/utxo)), odnosząc się do nich jako do "[wejść](https://planb.academy/resources/glossary/input)", a następnie tworzy nowe "wyjścia", które określają, do kogo te bitcoiny teraz należą i na jakich warunkach można je później wydać.



![Image](assets/fr/001.webp)



Ważną kwestią dotyczącą Bitcoin jest autoryzacja do wydawania. Bitcoin nie znajdują się na koncie, tak jak pieniądze w banku, ale są zablokowane przez warunki wydawania. Gdy [wallet](https://planb.academy/resources/glossary/wallet) chce użyć UTXO jako danych wejściowych, musi dostarczyć dowód kryptograficzny, że ma prawo do jego odblokowania. Dowód ten często przybiera formę [podpisu cyfrowego](https://planb.academy/resources/glossary/digital-signature) generated z [klucza prywatnego](https://planb.academy/resources/glossary/private-key). Właśnie dlatego bitcoinerzy nalegają na zabezpieczenie kluczy prywatnych: to one odblokowują dostęp do bitcoinów, a w konsekwencji umożliwiają ich wydawanie.



![Image](assets/fr/002.webp)



Podpis cyfrowy w Bitcoin odgrywa dwie ważne role:




- Autoryzuj wydatki: potwierdza, że użytkownik posiada klucz prywatny oczekiwany przez warunek wydatków UTXO;
- Ochrona integralności: łączy autoryzację z dokładnymi szczegółami transakcji (odbiorcy, kwoty, opłaty itp.). Jeśli ktoś później zmieni transakcję, podpis nie będzie już ważny.



Gdy transakcja zostanie poprawnie skonstruowana i podpisana przez Bitcoin wallet użytkownika, musi zostać rozgłaszana w sieci Bitcoin.



### Rola węzła Bitcoin w dystrybucji



Bitcoin jest siecią [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p): nie ma centralnego serwera, który odbiera i przetwarza wszystkie transakcje. Rolę tę pełnią wspólnie węzły. Węzeł Bitcoin to oprogramowanie (np. [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core)) połączone z innymi węzłami w sieci Bitcoin, którego głównym zadaniem jest weryfikacja, przechowywanie i przekazywanie transakcji i bloków.



Gdy wysyłasz transakcję z wallet, wallet przekazuje ją do węzła (własnego lub należącego do usługi). Węzeł ten najpierw sprawdzi, czy transakcja jest zgodna z różnymi regułami, takimi jak:




- podpisy są ważne;
- dane wejściowe odnoszą się do istniejących UTXO (tj. bitcoinów, które istnieją);
- gW-71 nie zostały jeszcze wydane gdzie indziej;
- ilość danych wyjściowych jest mniejsza lub równa ilości danych wejściowych (bitcoiny nie są tworzone z niczego);
- itp.



Jeśli transakcja przejdzie wszystkie te kontrole, węzeł propaguje ją do innych węzłów w sieci, z którymi jest połączony. Te z kolei sprawdzają ją i przekazują dalej, i tak dalej. W ciągu kilku sekund transakcja jest propagowana i staje się znana całej, a przynajmniej dużej części sieci Bitcoin.



![Image](assets/fr/003.webp)



### Mempool: poczekalnia transakcji



Pomiędzy momentem rozgłaszania transakcji a momentem jej potwierdzenia w bloku, musi ona czekać. Ten obszar oczekiwania nazywany jest **[mempool](https://planb.academy/resources/glossary/mempool)** (skrót od `memory` i `pool`). Mempool jest zatem tymczasową przestrzenią do przechowywania ważnych, ale wciąż niepotwierdzonych transakcji.



Ważna uwaga: nie ma czegoś takiego jak pojedynczy mempool, są tylko mempoole. Każdy węzeł utrzymuje swój własny mempool, z własnymi lokalnymi ograniczeniami. Oznacza to, że w dowolnym momencie dwa węzły mogą mieć nieco inną zawartość mempool (w zależności od tego, co otrzymały, co odrzuciły lub co usunęły).



![Image](assets/fr/004.webp)



Na tym etapie sieć wie o transakcji, zweryfikowała ją i przechowuje w pamięci do czasu jej potwierdzenia. Potwierdzenie tej transakcji nastąpi jednak dopiero wtedy, gdy górnik wstawi ją do bloku, a blok ten zostanie zaakceptowany przez sieć.



### Blockchain: publiczny rejestr znaczników czasu



Ponieważ bitcoin jest walutą niematerialną, musi rozwiązać jeden problem: zapobieganie [podwójnym wydatkom](https://planb.academy/resources/glossary/double-spending-attack) bez centralnego organu. Jeśli dwie transakcje próbują wydać ten sam UTXO, wszyscy muszą być w stanie zbiegać się w jednym, spójnym stanie. Satoshi Nakamoto podsumowuje tę kwestię tym słynnym zdaniem:



> Jedynym sposobem na potwierdzenie braku transakcji jest bycie świadomym wszystkich transakcji.

Innymi słowy, aby wiedzieć, że bitcoin nie został jeszcze wydany, potrzebny jest wspólny rejestr wcześniejszych wydatków.



Taką rolę pełni blockchain: publiczny rejestr zawierający historię transakcji. Zamiast jednak zapisywać każdą transakcję na bieżąco, Bitcoin grupuje je w bloki. Każdy blok działa jak strona historii, a system działa w ten sposób jak serwer znaczników czasu: porządkuje transakcje w czasie w weryfikowalny sposób.



Rejestr ten nie może zostać przepisany dzięki prostej zasadzie: każdy blok zawiera kryptograficzny odcisk palca ([hash](https://planb.academy/resources/glossary/hash-function)) poprzedniego bloku. W ten sposób bloki są ze sobą powiązane: jeśli zmodyfikujesz blok z przeszłości, jego hash ulegnie zmianie, co zerwie powiązanie z następnym blokiem, co zerwie powiązanie z kolejnym blokiem i tak dalej. To właśnie od tego łańcucha zależności pochodzi nazwa "*blockchain*".



![Image](assets/fr/005.webp)



Gdy już zrozumiemy te podstawowe zasady Bitcoin, możemy opisać cel górnika w bardziej konkretny sposób: zbudować nowy blok, który rozszerza istniejący łańcuch, poprzez wpisanie oczekujących transakcji, a następnie spróbować nadać mu ważność (jest to słynny "[proof of work](https://planb.academy/resources/glossary/proof-of-work)", który przeanalizujemy w późniejszym rozdziale). Najpierw jednak odkryjmy razem w następnym rozdziale, w jaki sposób budowany jest blok kandydujący.



## Budowa bloku Bitcoin


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Zrozumiałeś już, jak działa transakcja Bitcoin i jaka jest rola łańcucha bloków. Zanim jednak przyjrzymy się bardziej szczegółowo działaniu proof-of-work, pozostaje jeszcze jeden istotny krok, który musi wykonać górnik: budowa bloku kandydującego. Dowiedzmy się razem, czym jest [blok kandydujący](https://planb.academy/resources/glossary/candidate-block) i w jaki sposób górnik go konstruuje, zanim rozpoczniemy poszukiwanie ważnego dowodu.



### Blok kandydata



Miner muszą samodzielnie budować swoje bloki przed próbą ich wydobycia. Każdy górnik z kolei konstruuje tak zwany blok kandydujący z transakcji oczekujących w jego mempool. Tworzenie bloku kandydującego polega zatem na:




- wybrać, które transakcje mają zostać uwzględnione;
- zorganizować te transakcje w sposób zgodny z zasadami Bitcoin;
- tworzy metadane bloku, przechowywane w jego [nagłówku](https://planb.academy/resources/glossary/block-header).



Wybór transakcji wynika z prostej logiki ekonomicznej: blok ma pojemność ograniczoną przez protokół Bitcoin, więc górnik stara się zmaksymalizować to, co zarabia za tę przestrzeń. Jako priorytet wybiera transakcje oferujące najwyższe opłaty w stosunku do miejsca zajmowanego w bloku (jest to znane jako "stawka opłaty", wyrażona w sats/vB). Szczegóły dotyczące opłat zostaną omówione później; wystarczy zapamiętać ideę sortowania według efektywności przestrzeni.



Blok Bitcoin składa się zatem z dwóch głównych części:




- lista transakcji;
- nagłówek bloku, który służy w pewnym sensie jako dowód tożsamości bloku.



![Image](assets/fr/006.webp)



Nagłówek jest niezbędny, ponieważ jest używany jako podstawa proof-of-work: w Bitcoin nie wydobywasz bezpośrednio całego bloku; wydobywasz tylko nagłówek bloku, który podsumowuje informacje potrzebne do połączenia bloku z łańcuchem i zatwierdzenia jego zawartości. Aby umożliwić nagłówkowi reprezentowanie wszystkich transakcji, Bitcoin wykorzystuje narzędzie kryptograficzne: [drzewo Merkle](https://planb.academy/resources/glossary/merkle-tree).



### Drzewo Merkle: podsumowanie dużego zbioru transakcji



Wymienienie wszystkich transakcji w nagłówku byłoby niemożliwe: blok może zawierać tysiące transakcji, podczas gdy nagłówek ma stały rozmiar (80 bajtów). Rozwiązaniem jest zatem obliczenie unikalnego skrótu, który zależy od wszystkich transakcji w bloku: jest to [korzeń Merkle](https://planb.academy/resources/glossary/merkle-root).



Zasada jest następująca:




- obliczany jest kryptograficzny odcisk palca (hash) każdej transakcji;
- hasze te są parowane, łączone, a następnie ponownie haszowane w celu utworzenia nowej warstwy haszów;
- proces ten jest powtarzany, aż do uzyskania pojedynczego końcowego skrótu: korzenia Merkle.



![Image](assets/fr/007.webp)



Tak więc, jeśli pojedyncza transakcja ulegnie zmianie, nawet o jeden bit, wynikiem jest modyfikacja jej odcisku palca, która propaguje się do korzenia Merkle. Korzeń ten jest zawarty w nagłówku bloku. Tak więc modyfikacja przeszłej transakcji oznacza modyfikację nagłówka bloku, w którym jest zawarta, a tym samym śladu bloku, a następnie połączenia z kolejnymi blokami.



Od [SegWit](https://planb.academy/resources/glossary/segwit) oddzieliliśmy podpisy od reszty. Tak więc w rzeczywistości istnieją 2 drzewa Merkle zagnieżdżone w każdym bloku. Ta separacja ma konsekwencje dla sposobu, w jaki liczymy rozmiar bloku i dla niektórych zobowiązań kryptograficznych, ale podstawowa idea pozostaje taka sama: nagłówek musi zatwierdzać, w zwarty sposób, całą zawartość bloku.



### Nagłówek bloku



Nagłówek bloku ma długość 80 bajtów i zawiera dokładnie 6 pól. To właśnie te sześć elementów zostanie zaszyfrowanych podczas wyszukiwania proof of work (patrz następny rozdział):





- Wersja (`version`): Wskazuje, które zasady lub sygnały aktualizacji są przestrzegane przez blok. Służy jako mechanizm utrzymywania kompatybilności i ewolucji protokołu.




- Skrót poprzedniego bloku (`previousblockhash`): Jest to hash nagłówka poprzedniego bloku. To właśnie łączy bloki ze sobą. Bez tego pola mielibyśmy niezależne bloki. Dołączając hash nagłówka poprzedniego bloku, otrzymujemy łańcuch, w którym każdy nowy blok opiera się na poprzednim.





- Korzeń Merkle (`merkleroot`): Jest to odcisk palca wszystkich transakcji w bloku (poprzez drzewo Merkle). Łączy nagłówek z treścią: jeśli górnik zmodyfikuje wybór lub kolejność transakcji, korzeń ulegnie zmianie.





- [Znacznik czasu](https://planb.academy/resources/glossary/timestamp): Jest to znacznik czasu (czas uniksowy) wybrany przez górnika (z ograniczeniami ważności), który musi wskazywać, kiedy blok został wydobyty. Nie musi być idealnie dokładny co do sekundy, ale musi spełniać pewne warunki, aby pozostać akceptowalnym dla sieci.





- Zakodowany [cel trudności](https://planb.academy/resources/glossary/difficulty-target) (`nbits`): To pole koduje aktualny cel trudności. Omówimy to bardziej szczegółowo w rozdziale dotyczącym trudności, ale pamiętaj, że ten parametr jest częścią nagłówka.





- [Nonce](https://planb.academy/resources/glossary/nonce) (`nonce`): Jest to wartość, którą górnik może dowolnie modyfikować. Służy jako zmienna regulowana podczas proof-of-work. Wyjaśnię jej rolę bardziej szczegółowo w następnym rozdziale, ale ważne jest, aby zrozumieć, że nonce jest częścią nagłówka bloku i ma na celu umożliwienie kolejnych prób.



Aby ułatwić wizualizację, oto przykład nagłówka bloku w formacie szesnastkowym (80 bajtów):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



Oto podział na poszczególne pola:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Ten nagłówek bloku kandydującego, skonstruowany przez górnika, stanowi podstawę jego pracy. Podczas wyszukiwania ważnego proof-of-work, to nie cała lista transakcji jest bezpośrednio hashowana w pętli, ale raczej ten 80-bajtowy blok, który zawiera wszystko, co jest potrzebne do połączenia bloku z przeszłością i zatwierdzenia jego zawartości, a także zawiera parametry niezbędne dla mechanizmu mining, który omówimy w następnym rozdziale.



## Hash, cel i nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



W poprzednich rozdziałach prześledziliśmy ścieżkę transakcji Bitcoin: utworzonej i podpisanej przez wallet, przekazanej przez węzły, przechowywanej w mempoolach, a następnie potwierdzonej, gdy górnik włączy ją do bloku zaakceptowanego przez sieć. Nie widzieliśmy jednak jeszcze, w jaki sposób górnik może dodać swój blok do łańcucha bloków. Jaki proces kryje się za mining?



Zrozumienie procesu mining jest dość proste. Sprowadza się on do 3 pojęć, które idą ze sobą w parze: funkcja hashująca, wartość docelowa i zmienna, którą górnik może modyfikować. Przyjrzyjmy się, jak to wszystko działa.



### Funkcja skrótu



Funkcja skrótu to narzędzie, które pobiera wiadomość jako dane wejściowe i generuje dane wyjściowe o stałym rozmiarze, zwane "*fingerprint*" lub "*hash*".



![Image](assets/fr/010.webp)



Funkcja skrótu jest interesująca w systemach komputerowych, ponieważ ma pewne właściwości:





- Jeśli zmienisz pojedynczy bit na wejściu, wynikowy hash wyjściowy zmieni się całkowicie i nieprzewidywalnie;



![Image](assets/fr/011.webp)





- Niemożliwe jest przejście od wyjścia do wejścia: funkcja jest nieodwracalna;



![Image](assets/fr/012.webp)





- Niemożliwe jest znalezienie dwóch różnych wiadomości, które dają dokładnie taki sam hash.



![Image](assets/fr/013.webp)



Funkcja skrótu używana w Bitcoin dla mining to `SHA256`, zastosowana dwa razy z rzędu. Jest to znane jako podwójne [SHA256](https://planb.academy/resources/glossary/sha256) lub `SHA256d`. To właśnie to podwójne haszowanie tworzy odcisk palca bloku.



```text
hash = SHA256(SHA256(message))
```



W naszym przypadku `message` odpowiada w rzeczywistości nagłówkowi bloku, który widziałeś w poprzednim rozdziale. Dla przypomnienia, nagłówek jest małą strukturą, która podsumowuje wszystko w bloku.



![Image](assets/fr/014.webp)



### Dowód pracy: znalezienie hasha mniejszego niż docelowy



Proof-of-Work jest często opisywany jako rozwiązanie złożonego problemu. W rzeczywistości jest to nie tyle problem, co poszukiwanie metodą prób i błędów: górnik musi znaleźć wersję nagłówka, której hash (po przejściu przez funkcję hashującą `SHA256d`) spełnia prosty warunek: musi być mniejszy niż określony cel.



Warunek ten jest sformułowany w następujący sposób:




- skrót nagłówka bloku jest obliczany przy użyciu funkcji skrótu;
- interpretujemy ten hash jako liczbę;
- aby blok był ważny, liczba ta musi być mniejsza lub równa wartości zwanej "*cel trudności*".



Innymi słowy, blok jest ważny, jeśli



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



Celem jest 256-bitowa liczba. Ponieważ hash wygenerowany przez `SHA256d` ma również 256 bitów, można je porównać jako dwie liczby. Im niższa wartość docelowa, tym trudniejszy warunek, ponieważ istnieje mniej możliwych wyników poniżej tego progu. I odwrotnie, im wyższa wartość docelowa, tym łatwiej jest spełnić warunek i tym łatwiej jest wydobyć blok. W późniejszych rozdziałach przyjrzymy się bliżej sposobowi określania wartości docelowej.



W tym systemie interesująca jest funkcja skrótu. Należy pamiętać, że łatwo jest obliczyć wynik na podstawie danych wejściowych, ale niemożliwe jest znalezienie danych wejściowych, znając tylko wynik funkcji. W mining górnicy nie są proszeni o znalezienie dokładnego hasha, ale raczej o znalezienie hasha poniżej wartości docelowej. Jedynym sposobem na osiągnięcie tego celu jest wykonanie bardzo dużej liczby prób, aż określony nagłówek ich bloku kandydującego, po hashowaniu, da hash mniejszy niż ten docelowy.



Gdy cel jest wystarczająco niski, proces ten staje się kosztowny. Górnik oblicza hash nagłówka swojego bloku, sprawdza wynik i, jeśli warunek nie jest spełniony, modyfikuje nagłówek i powtarza obliczenia. Ta pętla jest powtarzana do momentu znalezienia prawidłowego nagłówka. Gdy hash nagłówka w końcu spełni warunek, proof of work zostaje ustanowiony, blok zostaje uznany za ważny i może zostać rozesłany w sieci Bitcoin do węzłów w celu dodania do ich łańcucha bloków. Zwycięski górnik otrzymuje następnie powiązaną nagrodę (szczegółowo omówimy jej skład później), podczas gdy wszyscy górnicy natychmiast wyruszają w poszukiwaniu nowego, ważnego nagłówka dla następnego bloku.



Podstawową zaletą tego mechanizmu jest jego asymetryczność. Wyprodukowanie proof of work jest kosztowne dla górników, ponieważ wymaga dużej liczby obliczeń hash. Z drugiej strony, dla weryfikatorów, tj. węzłów sieci, weryfikacja jest niezwykle prosta: wszystko, co muszą zrobić, to hashować nagłówek bloku dostarczony przez górnika i sprawdzić, czy wynikowy hash jest rzeczywiście niższy niż docelowy. Znalezienie dowodu wymaga zatem wiele pracy i zasobów, podczas gdy weryfikacja jego ważności jest szybka i niedroga. To właśnie ta właściwość definiuje wydajny system proof-of-work.



### Nonce



Pozostaje praktyczne pytanie: jeśli nagłówek bloku kandydata skonstruowany przez górnika nie daje prawidłowego skrótu, jak górnik może spróbować ponownie? Musi on zmodyfikować coś w nagłówku, aby uzyskać inny hash. To jest właśnie rola nonce.



Pamiętajmy o pierwszej właściwości funkcji hashującej: wystarczy zmienić pojedynczy bit na wejściu, by otrzymać zupełnie inny i nieprzewidywalny hash wyjściowy. Każde obliczenie skrótu jest zatem podobne do losowania.



![Image](assets/fr/016.webp)



Aby ponownie spróbować szczęścia, górnik nie musi modyfikować całego nagłówka swojego bloku kandydującego: wystarczy, że zmieni jego niewielką część, ponieważ nawet pojedynczy inny bit spowoduje powstanie zupełnie nowego hasha, potencjalnie ważnego, jeśli jest mniejszy niż docelowy.



Właśnie dlatego nagłówek bloku zawiera nonce. Nonce jest 32-bitową wartością, używaną raz, a następnie zastępowaną. W praktyce, dla tego samego bloku, górnik może przetestować około 4,29 miliarda możliwych wartości (od `0` do `2^32 - 1`). Każda odmiana nonce modyfikuje nagłówek bloku, a w konsekwencji całkowicie zmienia hash wygenerowany po zastosowaniu funkcji hashującej `SHA256d`.



Proces mining jest bardzo prosty:




- górnik tworzy blok kandydujący (transakcje + nagłówek);
- następnie oblicza hash dla `SHA256d(header)`;
- jeśli wynik jest większy niż wartość docelowa, zmienia nonce;
- zaczyna się od nowa;
- itp.



![Image](assets/fr/017.webp)



W rzeczywistości nonce nie jest jedynym polem, które może zostać zmodyfikowane. Każda modyfikacja w ramach transakcji bloku powoduje zmianę korzenia drzewa Merkle, a tym samym modyfikację nagłówka tego bloku. Dzięki nowoczesnej mocy obliczeniowej, przejście przez 4,29 miliarda możliwych wartości nonce można wykonać stosunkowo szybko. Dlatego też istnieje jeszcze jedno pole, ogólnie określane jako "*[extra-nonce](https://planb.academy/resources/glossary/extra-nonce)*", które dodatkowo zwielokrotnia możliwości zmiany nagłówka. Wrócimy do tego mechanizmu bardziej szczegółowo w późniejszym rozdziale.



### Jaki jest sens proof of work?



Nazywamy to "dowodem", ponieważ wynik jest natychmiast weryfikowalny: po wyprodukowaniu bloku każdy węzeł może w ułamku sekundy sprawdzić, czy kryptograficzny skrót jego nagłówka jest rzeczywiście poniżej wymaganego celu. Nazywamy to "pracą", ponieważ osiągnięcie tego skrótu wymaga wielu prób, a zatem rzeczywistego kosztu pod względem obliczeń i energii.



W [białej księdze](https://planb.academy/resources/glossary/white-paper) Bitcoin, Satoshi Nakamoto przedstawia dwie zalety korzystania z systemu proof-of-work w Bitcoin:





- Seal w historii gospodarczej:**



Po zużyciu obciążenia obliczeniowego blok zostaje zablokowany: jego modyfikacja wymagałaby ponownego wykonania proof of work tego bloku. A ponieważ bloki są połączone w łańcuchy, zmiana starego bloku oznaczałaby również ponowne obliczenie wszystkich kolejnych bloków, a następnie dogonienie i przekroczenie trwającej pracy uczciwego łańcucha.



Innymi słowy, proof-of-work służy jako kręgosłup systemu znakowania czasem, sprawiając, że fałszowanie przeszłości staje się coraz bardziej kosztowne w miarę gromadzenia bloków. Gdy wydobywany jest nowy blok, zabezpieczenie zapewniane przez proof of work jest stosowane jednocześnie i równomiernie do wszystkich istniejących UTXO. Z każdym dodanym blokiem, każdy UTXO gromadzi w ten sposób dodatkową ilość zabezpieczeń z Proof-of-Work.





- Zdefiniuj zasadę większości ([konsensus](https://planb.academy/resources/glossary/consensus)) i zneutralizuj Sybil:**



Proof-of-Work umożliwia również Bitcoin osiągnięcie konsensusu bez polegania na zasadzie głosowania "jeden identyfikator = jeden głos", która mogłaby zostać łatwo sfałszowana przez masowe tworzenie tożsamości (IP, węzłów, kluczy...).



W Bitcoin "*większość*" to nie największa liczba uczestników, ale **łańcuch, który zgromadzi najwięcej pracy**. Jak ujmuje to Satoshi, jest to zasada "jeden procesor = jeden głos", tj. głos ważony rzeczywistą mocą obliczeniową zużytą do wyprodukowania ważnych bloków. Tak więc wdrożenie tysięcy węzłów samo w sobie nie daje żadnej przewagi nad Bitcoin. Bez dodatkowej mocy obliczeniowej nie gromadzi się więcej dowodów pracy, a [atak Sybil](https://planb.academy/resources/glossary/sybil-attack) staje się bezużyteczny, podczas gdy reguła decyzyjna pozostaje obiektywna i nie wymaga identyfikacji uczestników.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System.*](https://bitcoin.org/bitcoin.pdf)



Zasady dotyczące przydatności i uprawnień małoletnich są bardzo złożonym tematem, którego nie będę szczegółowo omawiał w tym kursie. Powrócimy jednak do tego tematu w przyszłych kursach szkoleniowych MIN 201.



Na chwilę obecną można podsumować działanie mining w następujący sposób: górnicy budują blok kandydujący z transakcjami oczekującymi w mempoolach, a następnie szukają hasha jego nagłówka (poprzez `SHA256d`), który jest mniejszy lub równy celowi. Osiągają to poprzez testowanie nonces metodą prób i błędów.



W następnym rozdziale zajmiemy się krótką historią zasady proof-of-work, aby zrozumieć jej tło, a następnie przyjrzymy się, w jaki sposób system określa docelowy poziom trudności.



## Historia proof of work


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



Proof-of-work nie został wynaleziony dla Bitcoin. [Satoshi Nakamoto](https://planb.academy/resources/glossary/nakamoto-satoshi) wykorzystał i połączył kilka starszych pomysłów, które były już badane w różnych kontekstach.



### Hashcash



Pod koniec lat 90. problem spamu w wiadomościach e-mail stał się poważny. Rzeczywiście, jeśli wysłanie wiadomości e-mail prawie nic nie kosztuje, spamer może wysłać ich miliony. Ale jeśli każda wiadomość wymaga niewielkiego wysiłku obliczeniowego, wysłanie pojedynczej legalnej wiadomości pozostaje łatwe dla zwykłego użytkownika, podczas gdy wysyłanie milionów wiadomości staje się bardzo kosztowne.



Jest to cel [Hashcash](https://planb.academy/resources/glossary/hashcash), zaproponowany przez Adam Back w 1997 r., który jest uważany za wynalazek zasady proof-of-work. Zasada Hashcash jest bardzo podobna do mining: należy utworzyć hash, który spełnia pewien warunek (posiadanie określonej liczby zer na początku hasha). Dowód jest następnie dołączany do wiadomości i może być bardzo szybko zweryfikowany przez odbiorcę. Jeśli otrzymana wiadomość e-mail nie zawiera tego dowodu, może zostać natychmiast uznana za spam, a zatem odfiltrowana. Spamerzy są wtedy zmuszeni do poświęcenia znacznej ilości energii na wysłanie milionów wiadomości, co drastycznie zmniejsza (lub nawet całkowicie niweczy) opłacalność tego typu operacji, zarówno marketingowych, jak i oszukańczych.



Obecnie Hashcash nie jest wykorzystywany do wysyłania wiadomości e-mail. Filtrowanie spamu jest obecnie w dużej mierze oparte na scentralizowanych systemach. Przewaga Hashcash nad obecnymi rozwiązaniami polega na tym, że nie wymaga on scentralizowanego filtrowania: każdy może dostosować parametry według własnych kryteriów. Nie wymaga również identyfikacji, ponieważ wyszukiwanie hash może być wykonywane anonimowo. Przede wszystkim nie opiera się na systemie reputacji, który ma tendencję do wprowadzania subiektywnych form filtrowania.



W Hashcash nie chodziło o tworzenie pieniędzy. Jego celem było nałożenie kosztu krańcowego na łatwe do zautomatyzowania działanie cyfrowe.



![Image](assets/fr/008.webp)



### Bit Gold



Pod koniec lat 90. i na początku XXI wieku Nick Szabo badał ideę cyfrowego niedoboru opartego na proof of work. Jego koncepcyjny projekt, nazwany Bit Gold, przewiduje tworzenie jednostek wartości poprzez rozwiązanie kosztownego proof of work, a następnie zapisanie tych dowodów w rejestrze w celu ustanowienia formy własności.



Bit Gold nie zaowocował wdrożeniem systemu takiego jak Bitcoin, ale zawiera kilka ważnych spostrzeżeń: pomysł, że obliczenia mogą powodować niedobór oraz pomysł oznaczania elementów w czasie w celu stworzenia historii, którą trudno jest przepisać.



### RPOW



W 2004 roku Hal Finney zaproponował RPOW (*Reusable Proofs of Work*). Pomysł polegał na stworzeniu dowodów pracy, które mogłyby być następnie wymieniane, a nie tylko konsumowane. RPOW miał na celu stworzenie cyfrowych token opartych na proof of work, z systemem weryfikacji i transferu tych token bez ich powielania. RPOW ponownie nie rozwiązał w zadowalający sposób problemu całkowicie zdecentralizowanego rejestru, jak miało to miejsce później w przypadku Bitcoin, ale pozostaje jednym z największych prekursorów Bitcoin.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold i RPOW wykorzystują proof-of-work do nakładania kosztów i tworzenia formy niedoboru. Bitcoin wykorzystuje ten mechanizm, ale nadaje mu centralną i zbiorową rolę: proof-of-work jest wykorzystywany nie tylko do tworzenia czegoś, ale także do decydowania, kto ma prawo do napisania następnej strony rejestru (następnego bloku) oraz do uczynienia tego rejestru kosztownym do sfałszowania.



## Dostosowanie docelowego poziomu trudności


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



W poprzednich rozdziałach zobaczyłeś sedno proof-of-work: górnicy hashują nagłówek swojego bloku kandydata za pomocą `SHA256d`, a blok jest uznawany za ważny tylko wtedy, gdy wynikowy hash jest liczbowo mniejszy lub równy wartości referencyjnej zwanej celem. Pozostaje zatem pytanie: skąd pochodzi ten cel i w jaki sposób system zapewnia, że pozostaje on spójny w czasie?



Bitcoin dąży do osiągnięcia średniego tempa jednego znalezionego bloku co 10 minut. Oczywiście tempo to nie jest gwarantowane co do sekundy. W praktyce niektóre bloki są znajdowane kilka sekund po poprzednim, podczas gdy inne są znajdowane po ponad godzinie. Liczy się tutaj średnia z wystarczająco długiego okresu.



![Image](assets/fr/019.webp)



Zmienność ta wynika z probabilistycznej natury mining: każdy hash jest niezależną próbą, ze stałym prawdopodobieństwem (zakładając, że cel pozostaje niezmieniony) uzyskania wyniku poniżej celu. Można to zatem porównać do loterii z ciągłym losowaniem: im więcej haszy górnicy wykonują na sekundę, tym krótsze jest oczekiwane opóźnienie przed pojawieniem się ważnego bloku, ale nigdy nie eliminując losowości z jednego losowania do następnego.



### Dlaczego warto dążyć do 10-minutowych przerw między blokami?



Chociaż nie ma na to dowodów, Satoshi Nakamoto z pewnością wybrał 10 minut jako praktyczny kompromis między wydajnością a bezpieczeństwem. Krótszy interwał zapewniłby częstsze potwierdzenia, ale spowodowałby więcej tymczasowych podziałów sieci. Aby zrozumieć ten punkt, musimy wrócić do sposobu propagacji bloku.



Gdy górnik znajdzie ważny blok, natychmiast dystrybuuje go do swoich rówieśników. Węzły, które go otrzymują, sprawdzają jego ważność (transakcje, proof of work, zasady konsensusu itp.), a następnie przekazują go dalej. Ta propagacja zajmuje określoną ilość czasu, ograniczoną przez opóźnienia w Internecie, przepustowość i zdolność każdego węzła do weryfikacji bloku.



![Image](assets/fr/020.webp)



Jeśli podczas tego opóźnienia dyfuzji inny górnik również odkryje ważny blok na tej samej wysokości, sieć może zostać tymczasowo podzielona: jedna część węzłów i górników polega na bloku A, podczas gdy druga polega na bloku B. Jest to tymczasowy podział sieci.



![Image](assets/fr/021.webp)



Podziały te nie są katastrofalne. Konsensus Nakamoto przewiduje, że w dłuższej perspektywie zwycięży tylko jedna gałąź: ta, która zgromadzi najwięcej pracy. Rzeczywiście, gdy tylko nowy blok zostanie wydobyty na przykład na bloku A, cała sieć ponownie synchronizuje się z tą gałęzią i porzuca blok B, który następnie staje się "*[stale block](https://planb.academy/resources/glossary/stale-block)*", czasami błędnie nazywany "*orphan block*" w języku potocznym.



![Image](assets/fr/022.webp)



Z drugiej strony wiąże się to z kosztami: przez kilka minut ułamek górników pracuje nad gałęzią, która zostanie porzucona. Praca ta jest wówczas marnowana z punktu widzenia ogólnego bezpieczeństwa, ponieważ nie przyczyniła się do powstania końcowego łańcucha. Im krótszy odstęp czasu między poszczególnymi blokami, tym większe prawdopodobieństwo takich podziałów, ponieważ czas propagacji stanowi większą część czasu między każdym blokiem.



10-minutowy interwał generalnie zapewnia wystarczająco dużo czasu, aby zwycięski blok rozprzestrzenił się szeroko, zanim zostanie znaleziony konkurencyjny blok na tej samej wysokości. Jest to kompromis, który ogranicza podziały, zmniejsza marnowanie mocy obliczeniowej i pomaga sieci zachować synchronizację w skali globalnej.



### Zrozumienie hashrate



*"[Hashrate](https://planb.academy/resources/glossary/hashrate)*" odnosi się do ilości obliczeń hash wyprodukowanych na sekundę, czy to przez pojedynczego górnika, grupę górników, czy wszystkich górników w Bitcoin. Wyrażana jest w `H/s` (hashach na sekundę), z wielokrotnościami takimi jak `TH/s` (terahasze na sekundę) lub `EH/s` (eksahasze na sekundę). Reprezentuje to liczbę prób, które górnicy mogą podjąć w każdej sekundzie, aby uzyskać hash niższy niż docelowy.



Jeśli cel pozostaje stały, to:




- każda próba ma stałe prawdopodobieństwo powodzenia;
- wykonywanie większej liczby prób na sekundę zwiększa prawdopodobieństwo szybkiego pojawienia się zwycięskiej próby


Innymi słowy, jeśli jutrzejsza sieć Bitcoin podwoi swoją moc obliczeniową poprzez podłączenie dwa razy większej liczby maszyn mining, bez mechanizmu korygującego bloki będą znajdowane średnio dwa razy szybciej. Cel musi zatem zostać dostosowany, aby zrekompensować zmiany hashrate.



### Dostosowanie docelowego poziomu trudności



Bitcoin rozwiązuje ten problem za pomocą mechanizmu okresowej korekty celu, który dostosowuje trudność mining. Zasada jest następująca: co 2016 bloków (w przybliżeniu co 2 tygodnie) każdy węzeł ponownie oblicza docelowy poziom trudności, obserwując, ile czasu było faktycznie potrzebne do wyprodukowania tych 2016 bloków.



Celem tego mechanizmu jest skrócenie średniego czasu produkcji bloku do około 10 minut, podczas gdy ogólny hashrate sieci stale się zmienia, z powodu odłączania maszyn lub, przeciwnie, dodawania nowych maszyn.



![Image](assets/fr/023.webp)



Kalkulacja opiera się na obserwowanym czasie dla okresu, który upłynął:




- jeśli ostatnie bloki z 2016 r. zostały znalezione zbyt szybko, oznacza to, że hashrate wzrósł w tym okresie; Bitcoin utrudnia wtedy warunek, obniżając cel na następny okres;
- jeśli bloki 2016 zostały znalezione zbyt wolno, oznacza to, że hashrate zmniejszył się; Bitcoin łagodzi ten stan poprzez zwiększenie celu.



Formuła jest następująca:



```txt
Tn = To * (Ta / Tt)
```



Z:




- `tn`: nowy cel
- `to`: stary cel
- `Ta`: czas rzeczywisty, który upłynął dla ostatnich 2016 bloków
- `Tt`: czas docelowy (w sekundach)



Z docelowym czasem dwóch tygodni, tj. `Tt = 1 209 600` sekund:



```txt
Tn = To * (Ta / 1 209 600)
```



Aby zrozumieć, jak dostosować trudność Bitcoin mining, oto przykład z fikcyjnymi wartościami:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Z:



- `**To = 18,045,755,102**`: Stary cel, tj. wartość referencyjna przed korektą.
- `**ta = 1 000 000 sekund**`: Czas faktycznie spędzony na produkcji ostatnich 2016 bloków. Ponieważ czas ten jest krótszy niż czas docelowy, sieć wydobywała zbyt szybko.
- `**1 209 600 sekund**`: Docelowy czas odpowiadający 10 minutom na blok dla bloków z 2016 roku, używany jako odniesienie do korekty.
- `**tn = 14,918,779,020**`: Nowy cel obliczony po [dostosowaniu trudności](https://planb.academy/resources/glossary/difficulty-adjustment).



W tym przypadku nowy cel jest niższy niż stary, co oznacza, że mining staje się trudniejszy, aby spowolnić produkcję bloków w następnym okresie.


*Wartości docelowe w tym przykładzie są uproszczone i przeskalowane do celów dydaktycznych; rzeczywisty cel użyty w Bitcoin jest 256-bitową liczbą całkowitą o zupełnie innym rzędzie wielkości*



Obliczenia te są wykonywane lokalnie przez każdy węzeł, w oparciu o znaczniki czasu wprowadzone w blokach. Ponieważ wszystkie węzły stosują te same zasady, uzyskują ten sam wynik, a nowy cel staje się wspólnym odniesieniem dla następnych 2016 bloków.



Jest jeden ważny szczegół, na który należy zwrócić uwagę: **jest ona ograniczona**. Bitcoin ogranicza zmienność trudności na okres, aby uniknąć zbyt gwałtownych zmian, które mogłyby ją zablokować. W rzeczywistości rzeczywisty czas brany pod uwagę jest ograniczony do zakresu odpowiadającego współczynnikowi 4 (minimum jedna czwarta starego celu, maksymalnie czterokrotność starego celu). Zapobiega to ekstremalnemu retargetowaniu, jeśli znaczniki czasu są bardzo nietypowe lub manipulowane.



Zauważmy również, że w rzeczywistości dostosowanie trudności Bitcoina nie jest idealnie dokładne. Widzieliśmy bowiem, że trudność ma być przeliczana co 2016 bloków, poprzez porównanie rzeczywistego czasu, który upłynął, z czasem docelowym wynoszącym 14 dni (2016 × 10 minut). Jednak oryginalny kod Satoshi zawiera błąd zwany "*off-by-one*": zamiast mierzyć czas między ostatnimi blokami każdego okresu (czyli 2016 interwałów), mierzy czas między pierwszym a ostatnim blokiem, co daje tylko 2015 interwałów. W praktyce trudność jest obliczana tak, jakby okres składał się tylko z 2015 bloków zamiast 2016. Konsekwencją tego jest systematyczne, bardzo niewielkie przeszacowanie trudności, co sprawia, że bloki są wydobywane średnio nieco wolniej niż docelowe 10 minut (o około 0,05% wolniej). Ten błąd jest dobrze znany, ale nigdy nie został naprawiony, ponieważ jego zmiana wymagałaby hard forka, a jego wpływ pozostaje w praktyce zaniedbywalny, poza teoretycznym atakiem zwanym "*time warp*".

### Reprezentacja docelowa



W nagłówku bloku, cel nie pojawia się w swojej pełnej 256-bitowej formie, ponieważ zajęłoby to zbyt dużo miejsca. Zamiast tego, 32-bitowe pole `nBits` koduje cel w kompaktowym formacie, porównywalnym do notacji naukowej o podstawie 256: wykładnik (1 bajt) i współczynnik (3 bajty). Kompletny cel jest następnie rekonstruowany z tych dwóch wartości. Nie będziemy tutaj wchodzić w szczegóły, ponieważ temat jest stosunkowo złożony i nie wnosi nic do zrozumienia mining. Należy tylko pamiętać, że cel nie jest przechowywany w postaci nieprzetworzonej w nagłówku bloku, ale w postaci kompaktowej.



W tym ostatnim rozdziale części I omówiliśmy sposób działania proof-of-work w Bitcoin: górnik buduje blok kandydujący, wybierając transakcje ze swojego mempoolu, oblicza nagłówek bloku kandydującego, hashuje go, porównuje wynikowy hash z docelowym okresem, a następnie zaczyna od nowa, modyfikując nonce, aż do uzyskania prawidłowego hasha. Wreszcie, co 2016 bloków, sieć ponownie oblicza nowy cel, aby utrzymać średni czas około 10 minut na blok, pomimo ciągłych zmian w hashrate.




# System motywacyjny Bitcoin mining


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Jak można sobie wyobrazić, Bitcoin mining nie jest działalnością altruistyczną. Miner mają realne koszty: energię elektryczną do zasilania swoich komputerów mining, zakup specjalistycznego sprzętu, płace za konserwację, czasami pomieszczenia i systemy chłodzenia. Aby system Bitcoin działał, prywatne interesy górników muszą być zgodne ze zbiorowymi interesami sieci. Taka jest właśnie rola nagrody mining. Zachęca ona górników do inwestowania w proof of work, do zawierania ważnych transakcji i do przestrzegania zasad protokołu, zamiast próbować go zepsuć.



Logika ta opiera się na teorii gier: protokół czyni uczciwość racjonalną. Górnik zarabia pieniądze, gdy stworzy prawidłowy blok zaakceptowany przez węzły. I odwrotnie, jeśli spróbuje oszukiwać, jego blok zostanie odrzucony przez węzły, a on nic nie dostanie. Ponieważ wyprodukowanie bloku wiąże się z kosztami, odrzucony blok oznacza bezpośrednią stratę. W konkurencyjnym środowisku, w którym tysiące graczy jednocześnie szuka ważnego bloku, najbardziej opłacalną strategią jest zatem ścisłe przestrzeganie zasad i uczciwa maksymalizacja dochodów.



Aby to osiągnąć, protokół Bitcoin przewiduje, że górnik, który znajdzie ważny blok, wygrywa prawo do włączenia do niego określonej transakcji, za co górnik otrzymuje określoną sumę BTC. Jest to znane jako **[nagroda za blok](https://planb.academy/resources/glossary/block-reward)**. W pierwszym rozdziale tej sekcji celem jest zrozumienie, z czego się składa i jak jest określana. Później zobaczymy, jak część związana z tworzeniem pieniędzy ewoluuje w czasie (z halvingami) i jak jest faktycznie zbierana technicznie (poprzez transakcję coinbase).



### Z czego składa się nagroda blokowa?



W poprzednich rozdziałach widzieliśmy, jak górnikom udaje się znaleźć prawidłowy blok. Gdy górnik znajdzie nagłówek, którego hash jest mniejszy niż docelowy, jego kandydujący blok jest uznawany za prawidłowy. Może on następnie rozpowszechnić go w całej sieci Bitcoin. Blok jest dodawany do reszty łańcucha bloków, potwierdzając zawarte w nim transakcje.



To właśnie to wydarzenie (faktyczne dodanie bloku do łańcucha bloków) wyzwala przyznanie nagrody zwycięskiemu górnikowi. Nagroda ta składa się z dwóch różnych elementów, które są sumowane:




- [dotacja blokowa](https://planb.academy/resources/glossary/block-subsidy)**;
- opłaty transakcyjne**.



![Image](assets/fr/024.webp)



Przyjrzyjmy się, czemu odpowiadają te dwie części nagrody.



### Dotacja blokowa



Dotacja blokowa odpowiada pieniężnej części nagrody za utworzenie bloku. Gdy górnik utworzy prawidłowy blok, protokół upoważnia go do utworzenia określonej liczby nowych bitcoinów i przydzielenia ich sobie jako nagrody. Te bitcoiny są tworzone ex nihilo. Nie istniały wcześniej.



Ilość nowo utworzonych bitcoinów nie jest jednak dowolna. Jest ona ściśle określona przez zasady protokołu Bitcoin i jest identyczna dla wszystkich górników. Przyjrzymy się bliżej temu mechanizmowi w następnym rozdziale, ponieważ dotacja nie jest wartością stałą w nieskończoność: jest ona dzielona okresowo zgodnie z precyzyjnym harmonogramem. Na razie wystarczy to zapamiętać:




- subwencja blokowa jest jednym z dwóch składników nagrody blokowej;
- jest ona ograniczona i określona przez protokół, a nie przez górnika (nawet jeśli górnik może technicznie zażądać mniej niż maksymalna kwota);
- tworzy bitcoiny z powietrza.



Dotacja ta odgrywa dwie główne role w ramach protokołu Bitcoin. Pierwszą z nich jest zachęcanie graczy do udziału w mining. We wczesnych latach Bitcoin (a czasami nawet do dziś) opłaty transakcyjne były bardzo niskie. Subwencja gwarantowała zatem wystarczającą rekompensatę, aby przyciągnąć górników i utrzymać poziom bezpieczeństwa systemu.



Druga rola wiąże się z dystrybucją waluty. Każda nowa waluta staje przed pytaniem, jak sprawiedliwie dystrybuować jednostki monetarne wśród ludności. Subwencja blokowa stanowi odpowiedź na ten problem. Tworząc bitcoiny za pośrednictwem mining, umożliwia ich początkową dystrybucję w otwarty i neutralny sposób: każdy może je uzyskać, pod warunkiem, że uczestniczy w mining, bez konieczności wcześniejszej autoryzacji lub identyfikacji.



Z drugiej strony, ponieważ te bitcoiny są tworzone z niczego, ich wartość nie jest pozbawiona podstaw. Zwiększając ilość pieniędzy w obiegu, dotacja mechanicznie osłabia wartość istniejących bitcoinów. Wprowadza zatem formę inflacji monetarnej. W następnym rozdziale zobaczymy jednak, że dotacja ta ma stopniowo zanikać, a inflacja ostatecznie ustanie.



![Image](assets/fr/025.webp)



### Opłaty transakcyjne



Drugi składnik nagrody za blok jest związany z użytkowaniem systemu: kiedy użytkownik publikuje transakcję, chce, aby została ona potwierdzona. Przestrzeń blokowa jest jednak ograniczona, a bloki pojawiają się średnio co około 10 minut. Przestrzeń blokowa jest zatem zasobem deficytowym. Gdy popyt przewyższa podaż, cena rośnie: jest to rynek opłat transakcyjnych. Każdy górnik, któremu uda się stworzyć ważny blok, uzyskuje prawo do pobierania na własny rachunek pełnych opłat transakcyjnych związanych ze wszystkimi transakcjami, które zawarł w swoim bloku.



Można o tym myśleć jak o systemie aukcyjnym: każda transakcja proponuje kwotę opłaty, a górnicy priorytetowo traktują te, które maksymalizują ich dochód, przy ograniczeniach przestrzennych. Mechanizm ten w naturalny sposób wyrównuje interesy:




- użytkownicy, którym się spieszy, płacą więcej, aby zostać szybko uwzględnieni;
- górnicy są zachęcani do uwzględniania transakcji, które płacą najwyższe opłaty za przestrzeń blokową.
- sieć unika spamu, ponieważ publikacja transakcji wiąże się z kosztami.



#### Jak obliczane są opłaty transakcyjne?



Wbrew powszechnemu przekonaniu, opłaty nie są wynikiem transakcji Bitcoin. W rzeczywistości transakcja wydaje dane wejściowe i tworzy dane wyjściowe. Wejścia reprezentują źródło używanych bitcoinów, podczas gdy wyjścia reprezentują miejsce docelowe płatności. Opłaty transakcyjne to po prostu **różnica między całkowitymi nakładami a całkowitymi wynikami**.



Innymi słowy, nakłady bitcoinów użytkownika, które należą do niego, tworzą wyniki dla odbiorców, ale nie odtwarzają pełnej kwoty zużytej przez nakłady. Różnica między nimi stanowi opłaty transakcyjne, które może pobierać górnik.



Weźmy przykład. Transakcja zużywa dwa wejścia, jedno o wartości `100 000 sats` i drugie o wartości `150 000 sats`, i tworzy trzy wyjścia o wartościach `35 000 sats`, `42 000 sats` i `170 000 sats`.



![Image](assets/fr/027.webp)



Suma nakładów wynosi zatem `250 000 sats`, podczas gdy suma wyników wynosi `247 000 sats`. Oznacza to, że `3 000 sats` zostało zużytych w nakładach bez odtworzenia w nakładach: kwota ta odpowiada opłatom proponowanym przez tę transakcję.



![Image](assets/fr/028.webp)



Jeśli górnik włączy tę transakcję do ważnego bloku, będzie uprawniony do odzyskania tych `3 000 sats`, oprócz opłat za wszystkie inne transakcje zawarte w bloku. Nie ma jednak bezpośredniego powiązania on-chain między transakcją, która uiszcza opłatę, a sats faktycznie pobranym przez górnika. Technicznie rzecz biorąc, opłaty w wysokości `3 000 sats` są niszczone, a w zamian górnik uzyskuje prawo do odtworzenia tej samej kwoty dla siebie.



#### Współczynnik opłat



Blok nie jest ograniczony liczbą transakcji, ale jego całkowitą pojemnością (dziś, w praktyce, wagą bloku). Niektóre transakcje zajmują więcej miejsca niż inne: transakcja z wieloma wejściami i wyjściami będzie większa niż prosta transakcja z jednym wejściem i dwoma wyjściami. Użyte skrypty również będą miały wpływ na rozmiar.



![Image](assets/fr/026.webp)



Dwie transakcje mogą zatem płacić taką samą kwotę opłat w wartościach bezwzględnych, ale nie być ekonomicznie równoważne z punktu widzenia górnika. Jeśli jedna z nich jest dwa razy większa, kosztuje dwa razy więcej miejsca w bloku. Przestrzeń jest ograniczona, więc górnik stara się zmaksymalizować swój przychód na jednostkę przestrzeni.



Dlatego w praktyce wyrażamy konkurencyjność transakcji za pomocą współczynnika opłat, zwykle w `sats/vB` ([satoshis](https://planb.academy/resources/glossary/satoshi-sat) na wirtualny bajt). Obliczenie tego współczynnika jest proste:



```text
fee rate = fee / weight (in vB)
```



Na przykład, jeśli mamy transakcję o wadze `141 vB` i przydzielającą `1,974 sats` w opłatach, będzie ona miała stawkę opłaty `14 sats/vB`.



```text
1 974 / 141 ≈ 14 sats/vB
```



Współczynnik ten wyjaśnia wybory ekonomiczne dokonywane przez górników: przy stałej przepustowości, włączenie transakcji o wysokiej stawce maksymalizuje całkowite opłaty za blok, a tym samym wynagrodzenie górnika. Wyjaśnia to również, dlaczego tanie transakcje pozostają w kolejce w mempoolach przez długi czas: konkurują one z innymi transakcjami, które płacą więcej za jednostkę przestrzeni.



### Ochrona sieci przed spamem



Opłaty służą również bezpieczeństwu operacyjnemu: wprowadzają koszt do pomnażania transakcji. Gdyby publikowanie transakcji było darmowe, łatwo byłoby zalać sieć bezużytecznymi transakcjami i nasycić pule pamięci, zwiększając obciążenie węzłów.



W praktyce węzły stosują lokalne zasady przekazywania (reguły mempool) i często ustalają minimalny próg opłaty, poniżej którego nie będą przekazywać transakcji (domyślnie `0,1 sat/vB` w Bitcoin Core poprzez `minRelayTxFee`). Transakcja może być ważna w ścisłym znaczeniu zasad konsensusu, ale nie może zostać przekazana przez większość węzłów, jeśli jej opłaty są zbyt niskie. W rezultacie nie krąży, nie dociera do górników i ma bardzo małe szanse na potwierdzenie.



W tym momencie masz już sedno nagrody za blok: odpowiada ona rekompensacie dla zwycięskiego górnika i składa się z dwóch różnych elementów. Z jednej strony, dotacja blokowa, zdefiniowana przez zasady protokołu, która tworzy nowe bitcoiny ex nihilo. Z drugiej strony, opłaty za transakcje zawarte w wydobytym bloku.



W następnym rozdziale skupimy się bardziej szczegółowo na subwencji blokowej, aby dokładnie zrozumieć, w jaki sposób jest ona obliczana i jak zmienia się w czasie zgodnie z zasadami protokołu Bitcoin.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



W poprzednim rozdziale widzieliśmy, że górnicy, którzy tworzą ważny blok, otrzymują nagrodę składającą się z opłat za transakcje zawarte w bloku oraz subsydium blokowego. Nie wyjaśniliśmy jednak jeszcze, w jaki sposób ustalana jest wysokość tego subsydium. Mechanizm, który ustala i ewoluuje tę wartość, znany jest jako ***[halving](https://planb.academy/resources/glossary/halving)***.



### Co to jest zmniejszenie o połowę?



Halving to zdarzenie zaprogramowane w protokole Bitcoin, które zmniejsza o połowę dotację blokową, tj. maksymalną ilość nowych bitcoinów, które zwycięski górnik może utworzyć w każdym bloku. Nie ma to wpływu na opłaty transakcyjne: opłaty istnieją niezależnie i pozostają określane przez aktywność użytkowników i konkurencję o przestrzeń blokową.



Kiedy Bitcoin został uruchomiony w 2009 roku, dotacja blokowa została ustalona na 50 BTC za każdy wydobyty blok. Od tego czasu dotacja ta była kilkakrotnie zmniejszana o połowę.



![Image](assets/fr/029.webp)



Halving nie jest wyzwalany przez datę, ale przez wysokość bloku. Jest on wykonywany **co 210 000 bloków**. Ponieważ Bitcoin celuje w średni interwał około 10 minut na blok, 210 000 bloków odpowiada mniej więcej czterem latom.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Tak więc, jeśli odnotujemy `n` liczbę połówek, które już wystąpiły, dotację blokową w BTC można obliczyć w następujący sposób:



```text
subsidy(n) = 50 / 2^n
```



### Poprzednie połówki



Poniżej znajduje się tabela podsumowująca halvingi, które już miały miejsce, wraz z ich wysokością bloku, datą i nową dopłatą do bloku obowiązującą po tym wydarzeniu:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### Kiedy i jak kończy się dotacja?



Halving jest powtarzany tak długo, jak długo dotacja może być wyrażona w minimalnej jednostce systemu: satoshi.



```text
1 BTC = 100 000 000 sats
```



W miarę zmniejszania dotacji o połowę, ostatecznie osiągamy ułamki bitcoina tak małe, że stają się one mniejsze niż 1 satoshi. W tym momencie nie jest już możliwe stworzenie połowy jednostki satoshi. Tworzenie pieniędzy poprzez dotację blokową ustaje, a górnicy są wynagradzani wyłącznie na podstawie opłat transakcyjnych. Od tego momentu wszystkie bitcoiny będą w obiegu i nie będzie już możliwe wytwarzanie nowych jednostek.



Ostateczny koniec subsydiowania bloków nastąpi na poziomie 6 930 000 bloków, czyli przy 33. i ostatnim halvingu. Oczekuje się, że wydarzenie to będzie miało miejsce około 2140 roku, choć nie można podać dokładnej daty, ponieważ będzie to zależeć od faktycznego tempa znajdowania bloków do tego czasu.



Ponieważ dotacja blokowa podąża za sekwencją geometryczną ze stosunkiem 1/2 przy każdym halvingu, kreacja pieniądza była niezwykle wysoka we wczesnych dniach Bitcoin, a następnie bardzo szybko spadła. Do siódmego halvingu ponad 99% bitcoinów zostanie już wprowadzonych do obiegu. Oczekuje się, że próg 99% zostanie przekroczony między 2032 a 2036 rokiem. Oznacza to, że wydobycie ostatniego pozostałego 1% bitcoinów zajmie ponad 100 lat. Podczas gdy inflacja monetarna była bardzo wysoka w momencie uruchomienia Bitcoin, aby umożliwić powszechną dystrybucję waluty, obecnie jest ona bardzo niska i będzie nadal spadać, aż osiągnie poziom prawdziwej twardej waluty, której podaż w obiegu nie może już wzrosnąć.



![Image](assets/fr/030.webp)



### Dlaczego nigdy nie będzie 21 milionów BTC?



Maksymalna podaż monetarna Bitcoin jest często przedstawiana jako 21 milionów BTC. Jest to dobre przybliżenie dla zrozumienia jego polityki pieniężnej, ale ze ściśle technicznego punktu widzenia całkowita podaż nigdy nie osiągnie dokładnie 21 000 000 bitcoinów.



Główny powód jest mechaniczny. Poprzez kolejne halvingi, dotacja blokowa ostatecznie spada poniżej minimalnej wartości 1 sat, co kończy się emisją przed osiągnięciem dokładnej teoretycznej sumy. W wyniku tej minimalnej ziarnistości i zasad zaokrąglania, całkowita liczba bitcoinów utworzonych przez dotację wynosi nieco mniej niż 21 milionów.



Ponadto, marginalne odchylenia związane z protokołem również mogą się do tego przyczynić. Na przykład, w rzadkich przypadkach niektórzy górnicy mogli nie ubiegać się o pełną dotację, co ostatecznie zmniejsza ilość faktycznie wyemitowanych bitcoinów. Możemy również wspomnieć o [bloku genesis](https://planb.academy/resources/glossary/genesis-block), wyprodukowanym przez Satoshi 3 stycznia 2009 r., którego utworzone bitcoiny nie są częścią [UTXO set](https://planb.academy/resources/glossary/utxo-set), a także o niektórych wydarzeniach historycznych związanych z błędami, takimi jak zduplikowane identyfikatory transakcji coinbase.



Wreszcie, musimy również wziąć pod uwagę wszystkie bitcoiny, które zostały zniszczone lub zablokowane:




- bitcoiny zablokowane w nierozwiązywalnych skryptach;
- te celowo zniszczone przez skrypty `OP_RETURN`;
- lub utratę kluczy prywatnych na poziomie aplikacji.



Teoretycznie podaż Bitcoin jest zatem ograniczona do 21 milionów. W praktyce jednak nigdy nie będzie 21 milionów bitcoinów w obiegu.



## Transakcja coinbase


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



W poprzednich rozdziałach przedstawiliśmy dwa ważne punkty. Po pierwsze, górnik, któremu uda się wyprodukować i rozpowszechnić prawidłowy blok, otrzymuje nagrodę. Z drugiej strony widzieliśmy, że nagroda ta składa się z dwóch różnych elementów:




- subwencja blokowa (bitcoiny tworzone ex nihilo, których maksymalna ilość jest ustalana przez protokół i stopniowo zmniejszana poprzez halvingi);
- wszystkie opłaty transakcyjne uiszczone przez użytkowników, których transakcje zostały uwzględnione w bloku.



Pozostaje jednak jedno pytanie: za pomocą jakiego mechanizmu górnik pobiera tę nagrodę w Bitcoin? To jest właśnie rola konkretnej transakcji zwanej "coinbase".



### Jak działa transakcja coinbase



Jak widzieliśmy w pierwszej części kursu, każdy blok Bitcoin zawiera listę oczekujących transakcji, które zostaną potwierdzone. Pierwszą z nich jest zawsze [transakcja coinbase](https://planb.academy/resources/glossary/coinbase-transaction). To właśnie ona pozwala zwycięskiemu górnikowi otrzymać nagrodę.



![Image](assets/fr/031.webp)



Na pierwszy rzut oka wygląda jak klasyczna transakcja Bitcoin: ma [TXID](https://planb.academy/resources/glossary/txid-transaction-identifier), wyjścia i jest zawarta w drzewie Merkle bloku. Różni się jednak pod jednym ważnym względem: nie wydaje żadnych istniejących UTXO.



W klasycznej transakcji Bitcoin "wejścia" odnoszą się do poprzednich niewydanych wyjść (UTXO), które zapewniają wartość wejściową. Wyjścia następnie redystrybuują tę wartość do nowych UTXO, z nowymi warunkami wydawania. Innymi słowy, aby wysłać bitcoiny, musisz już je posiadać. Z drugiej strony transakcja coinbase nie zużywa bitcoinów na wejściu: tworzy bitcoiny na wyjściu bezpośrednio od zera.



To właśnie ten mechanizm umożliwia wprowadzanie nowych bitcoinów do obiegu za pośrednictwem dotacji blokowej i kredytuje górnika opłatami związanymi z transakcjami zawartymi w bloku. Transakcja coinbase nie może odnosić się do rzeczywistego istniejącego UTXO (w rzeczywistości odnosi się do fikcyjnego UTXO), ponieważ jej rolą jest właśnie stworzenie części wartości (dotacji) i odzyskanie drugiej części (opłat), bez otrzymywania ich z poprzedniej transakcji. Aby cały system pozostał spójny, część odpowiadająca opłatom musi być dokładnie równa sumie bitcoinów zużytych na wejściu, ale nie odtworzonych na wyjściu w innych transakcjach bloku.



![Image](assets/fr/032.webp)



Ta transakcja nie jest opcjonalna. Blok, który nie zawiera transakcji coinbase, jest nieważny i będzie systematycznie odrzucany przez węzły sieci.



⚠️ Uwaga: termin "*coinbase*" nie ma związku z platformą wymiany o tej samej nazwie. W Bitcoin "*coinbase*" historycznie odnosi się do transakcji, która tworzy nagrodę za blok. Firma po prostu przyjęła ten termin dla swojej nazwy.



Transakcja coinbase spełnia w rzeczywistości kilka ról jednocześnie:




- Pierwszym z nich jest ten, który właśnie opisaliśmy: przypisuje on górnikowi nagrodę, do której jest uprawniony za wyprodukowanie ważnego bloku.
- Jego drugą, bardziej techniczną rolą jest zakotwiczenie kryptograficznego zobowiązania do świadków (podpisów) transakcji SegWit zawartych w bloku.
- Trzecią rolą, tym razem niezwiązaną bezpośrednio z protokołem, ale powiązaną z nowoczesną industrializacją mining, jest to, że baza monet jest obecnie często wykorzystywana do zakotwiczenia dowolnych danych technicznych. Dane te są zazwyczaj związane z działaniem pul mining i ich wewnętrzną organizacją.



Aby pomóc ci zrozumieć te różne zastosowania, przyjrzymy się teraz bliżej strukturze transakcji coinbase.



### Podstawowa struktura transakcji coinbase



Transakcja coinbase musi zawierać dokładnie jedno wejście. Dla uproszczenia czasami mówimy, że nie ma danych wejściowych, ponieważ te dane wejściowe nie wydają żadnego rzeczywistego UTXO. W rzeczywistości istnieje wejście z odniesieniem do źródła, ale celowo wskazuje na nieistniejący UTXO.



Jak już widzieliśmy, każda transakcja Bitcoin musi wykorzystywać UTXO jako dane wejściowe w celu utworzenia prawidłowych danych wyjściowych. W transakcji Bitcoin zużycie to przybiera formę odniesienia do istniejącego UTXO jako danych wejściowych. Odniesienie to odbywa się po prostu poprzez wskazanie identyfikatora poprzedniej transakcji (tej, w której utworzono UTXO), a także jej indeksu wśród wyników tej transakcji. Konkretnie, UTXO jest definiowany przez hash (poprzedni TXID) i indeks.



Ale w przypadku transakcji coinbase, zamiast odwoływać się do prawdziwego istniejącego UTXO, dane wejściowe muszą koniecznie wskazywać na ten konkretny fałszywy UTXO, z TXID pełnym zer, który nie odpowiada żadnemu prawdziwemu TXID:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Bezpośrednio po nim następuje fałszywy indeks:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



W podstawowym protokole Bitcoin, jak opisano w Satoshi Nakamoto, to fałszywe wejście jest jedynym ograniczeniem nałożonym na transakcję coinbase.



Jak każdy UTXO przywoływany w danych wejściowych transakcji, jest on powiązany z polem `scriptSig`. W konwencjonalnej transakcji to pole `scriptSig` zawiera elementy potrzebne do spełnienia `scriptPubKey`, a tym samym odblokowania zużytego UTXO. Ale w konkretnym przypadku coinbase, ponieważ UTXO, do którego się odwołujemy, jest celowo fikcyjny, pole `scriptSig` jest całkowicie wolne. Miner mogą zatem wprowadzić dowolne dane. Później przyjrzymy się, jak ta swoboda jest wykorzystywana.


Oprócz tego fałszywego wejścia, istnieje jedno lub więcej całkowicie standardowych wyjść, które umożliwiają górnikowi zbieranie bitcoinów z nagrody na jednym z ich adresów Bitcoin. Te wyjścia to UTXO zablokowane przez `scriptPubKey` (np. skrypt wskazujący na adres kontrolowany przez górnika lub pulę). Jedyną osobliwością jest tutaj zasada obliczania ich wartości: całkowita suma wyjść coinbase nigdy nie może przekroczyć maksymalnej dozwolonej dotacji, do której dodawane są opłaty blokowe.



Historycznie rzecz biorąc, transakcja coinbase sprowadza się do tego prostego schematu: fałszywego wejścia odwołującego się do nieistniejącego UTXO i jednego lub więcej wyjść zaprojektowanych w celu dystrybucji nagrody za blok do zwycięskiego górnika. Dziś jednak coinbase nie ogranicza się już do tej roli dystrybucyjnej. Jego specjalna pozycja w bloku i duża elastyczność jego struktury doprowadziły do nowych zastosowań, zarówno w samym protokole, jak i w mechanizmach zarządzania pulą mining.



### Inne zastosowania coinbase



Z biegiem czasu transakcja coinbase stała się szczególnie wygodnym punktem wstawiania do integracji różnych informacji przydatnych dla mining i samej struktury bloków. Przyjrzyjmy się im, aby lepiej zrozumieć ogólną organizację coinbase.



#### BIP-34



[BIP-34](https://planb.academy/resources/glossary/bip0034) to [soft fork](https://planb.academy/resources/glossary/soft-fork) wdrożony w marcu 2013 roku, począwszy od bloku 227,930, który wprowadził wersję 2 bloków Bitcoin. Ta nowa wersja wymaga, aby każdy blok zawierał, w `scriptSig` transakcji coinbase, wysokość tworzonego bloku.



Z jednej strony ewolucja ta wyjaśnia sposób, w jaki sieć zgadza się na ewolucję struktury bloków i zasad konsensusu. Po drugie, zapewnia unikalność każdego bloku i transakcji coinbase.



Tak więc `scriptSig` coinbase nie jest całkowicie wolny. Od czasu aktywacji BIP-34 jest on po prostu ograniczony do rozpoczęcia od wysokości bloku, w którym zawarta jest ta transakcja coinbase.



![Image](assets/fr/035.webp)



#### Extra-nonce



Jak widzieliśmy w pierwszych rozdziałach tego kursu, górnik ma 32-bitowe pole nonce w nagłówku bloku, które modyfikuje metodą prób i błędów, aby znaleźć hash mniejszy lub równy celowi. Ta 32-bitowa przestrzeń pozwala już na zbadanie bardzo dużej liczby kombinacji, ale gdy trudność mining jest wysoka, zakres ten może zostać całkowicie wyczerpany w stosunkowo krótkim czasie, a tym samym może nie dać żadnej kombinacji, która tworzy prawidłowy hash. Jeśli wszystkie możliwe wartości `nonce` zostały przetestowane bez powodzenia, górnik musi następnie zmodyfikować inny element, aby zmienić nagłówek bloku i rozpocząć nową serię prób.



Ponieważ transakcja coinbase oferuje wolne pole poprzez `scriptSig` swojego wejścia, rozwiązaniem stosowanym do rozszerzenia przestrzeni nonce jest wykorzystanie części tego `scriptSig`. Jest to ogólnie określane jako extra-nonce. Modyfikując extra-nonce, górnik modyfikuje `scriptSig` coinbase, tj. identyfikator transakcji, następnie korzeń Merkle bloku, a na końcu sam nagłówek bloku. W ten sposób uzyskują nową przestrzeń wyszukiwania hashy do zbadania, bez konieczności modyfikowania innych składników bloku kandydującego.



![Image](assets/fr/036.webp)



#### Identyfikacja pul i górników



Obecnie bardzo duża część światowego wydobycia hashrate jest zorganizowana w pule mining. Struktury te łączą indywidualnych górników w celu połączenia ich pracy i zmniejszenia zmienności ich dochodów.



Ze względów operacyjnych pule mining wykorzystują również wolne pole `scriptSig` wejścia coinbase do wstawiania różnych informacji. Różnią się one w zależności od puli i protokołu sieciowego, ale zazwyczaj zawierają unikalny identyfikator (często dodatkowy nonce podzielony na kilka części) przypisany do każdego górnika, aby uniknąć powielania pracy w puli. Zazwyczaj dodawany jest znacznik identyfikacyjny puli, używany do publicznego przypisywania znalezionych bloków, statystyk mining i innych celów śledzenia.



![Image](assets/fr/037.webp)



#### Zaangażowanie SegWit



Odkąd SegWit soft fork został włączony w 2017 r., dane świadków (tj. generalnie podpisy) zostały oddzielone od głównych danych transakcji, w szczególności w celu skorygowania problemu [plastyczności transakcji Bitcoin](https://planb.academy/resources/glossary/malleability-transaction). Oddzielenie to wprowadza zatem nowy element, który ma zostać zatwierdzony w bloku.



Aby to zrobić, świadkowie są grupowani w innym dedykowanym drzewie Merkle, którego korzeń jest następnie zatwierdzany do transakcji coinbase za pośrednictwem wyjścia `OP_RETURN`.



![Image](assets/fr/038.webp)



Nie będę wchodził w szczegóły tego mechanizmu w tym kursie, ponieważ wykracza to poza zakres tego artykułu, ale wystarczy pamiętać, że od czasu wprowadzenia SegWit transakcja coinbase służy jako nośnik do zakotwiczenia w bloku odcisku palca podsumowującego wszystkich świadków SegWit. Świadkowie są umieszczani w niezależnym drzewie Merkle, korzeń tego drzewa jest zapisywany na wyjściu transakcji coinbase, a sama transakcja coinbase jest włączana do głównego drzewa Merkle wraz ze wszystkimi innymi transakcjami, których korzeń pojawia się w nagłówku bloku. W ten sposób świadkowie, przechowywani oddzielnie od głównych danych transakcji, są nadal zapisywani w nagłówku bloku.



![Image](assets/fr/039.webp)



#### Arbitralne komunikaty



Ponieważ `scriptSig` pozwala na swobodne wstawianie dowolnych informacji wybranych przez górnika, niektórzy skorzystali z okazji, aby dodać wiadomości o charakterze bardziej osobistym, a nie technicznym. Najbardziej znanym przypadkiem jest oczywiście Satoshi Nakamoto, z jego kultową już wiadomością:



> The Times 03/Jan/2009 Kanclerz na krawędzi drugiego pakietu ratunkowego dla banków

Ta wiadomość, obecna w bloku Genesis (pierwszy blok Bitcoin), jest w rzeczywistości zakodowana w systemie szesnastkowym w `scriptSig` transakcji coinbase:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### Okres zapadalności


Po wydobyciu i dystrybucji bloku, transakcja coinbase pojawia się w łańcuchu bloków jak każda inna transakcja. Tworzy UTXO dla zwycięskiego górnika, umożliwiając mu odebranie nagrody. Jednak te UTXO nie mogą być natychmiast wydane: podlegają one [okresowi zapadalności](https://planb.academy/resources/glossary/maturity-period). Okres ten jest ustalony na 100 bloków po bloku zawierającym coinbase. Mówiąc konkretnie, transakcja coinbase musi zatem uzyskać 101 potwierdzeń, aby jej wyniki mogły zostać wydane przez zwycięskiego górnika.


![Image](assets/fr/040.webp)


Celem tej reguły jest ograniczenie wpływu reorganizacji łańcucha na gospodarkę. Jak widzieliśmy w poprzednich rozdziałach, może się zdarzyć, że na tej samej wysokości dwa różne ważne bloki zostaną znalezione niemal jednocześnie przez różnych górników. Przez krótką chwilę sieć może się podzielić: niektóre węzły otrzymują najpierw blok A, podczas gdy inne widzą najpierw blok B. Następnie, w trakcie kolejnych bloków, jedna z dwóch gałęzi gromadzi więcej pracy i staje się gałęzią referencyjną. Druga gałąź zostaje porzucona, a jej bloki stają się nieaktualne. Transakcje, które zawierała, mogą następnie teoretycznie powrócić do mempooli oczekujących na potwierdzenie.



W praktyce rzadko się to zdarza, ponieważ rynek opłat często powoduje, że prawie te same transakcje pojawiają się w dwóch konkurencyjnych blokach na tej samej wysokości. Jest to jeden z powodów, dla których transakcja Bitcoin jest powszechnie uważana za niezmienną po sześciu potwierdzeniach: reorganizacje więcej niż sześciu bloków są tak mało prawdopodobne, że można je rozsądnie uznać za niemożliwe.



![Image](assets/fr/041.webp)



Problem z tymi reorganizacjami w przypadku transakcji coinbase polega na tym, że nie jest to zwykła transakcja. Wprowadza ona do obiegu zupełnie nowe bitcoiny. Gdyby nagroda za blok mogła zostać wydana natychmiast, mogłoby dojść do problematycznej sytuacji kaskadowej:




- górnik wydaje bitcoiny z bazy coinbase,
- te bitcoiny krążą w gospodarce,
- następnie oryginalny blok został ostatecznie porzucony podczas reorganizacji.



Bitcoiny w obiegu nigdy nie istniałyby w ostatecznym łańcuchu, a seria transakcji, które były ważne w momencie emisji, stałaby się nieważna a posteriori.



Okres zapadalności narzuca wystarczająco długie ramy czasowe, aby uczynić ten scenariusz nierealistycznym. Reorganizacja 101 bloków jest w praktyce uważana za niemożliwą (nawet jeśli istnieje nieskończenie małe prawdopodobieństwo). Nie wiemy dokładnie, dlaczego Satoshi wybrał tak wysoką wartość okresu zapadalności, ale jest prawdopodobne, że został on wybrany tak, aby mechanizm pozostał funkcjonalny, nawet w przypadku poważnych awarii sieci.



Zasada ta zapobiega sytuacji, w której nowo utworzone pieniądze z nagrody blokowej zaczynają krążyć, zanim blok, który je generated, zostanie bezpiecznie zakopany pod dużą ilością zgromadzonej pracy.



---

Doszliśmy teraz do końca naszego wyjaśnienia, jak działa Bitcoin mining. Powinieneś mieć teraz jasny obraz podstawowych mechanizmów.



W ostatniej części kursu powrócimy do bardziej konkretnych aspektów, aby pokazać, jak Bitcoin mining materializuje się w prawdziwym świecie: jego industrializacja, używane maszyny, grupowanie graczy i tak dalej. Celem będzie przedstawienie ogólnego spojrzenia na Bitcoin mining, zarówno z perspektywy teoretycznej i protokolarnej, którą właśnie widzieliśmy, jak i od strony praktycznej i operacyjnej.



# Przemysł Bitcoin mining


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## Ewolucja maszyn mining


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



We wczesnych dniach Bitcoin, mining nie był działalnością przemysłową. Była to część oprogramowania Bitcoin, uruchomiona na komputerze osobistym, często z ciekawości, czasami w celu wsparcia sieci, a po drugie w celu uzyskania bitcoinów, które wówczas nie miały praktycznie żadnej wartości rynkowej.



Z biegiem lat działalność ta przeszła transformację: zmieniły się maszyny, trudność eksplodowała, a mining stał się branżą samą w sobie. Przyjrzyjmy się aspektom operacyjnym Bitcoin mining.



### Pierwsze kroki: mining z procesorem



W 2009 roku i we wczesnych latach mining był realizowany głównie przy użyciu procesora konwencjonalnego komputera. Bitcoin był wtedy tylko prostym oprogramowaniem, służącym jako wallet, węzeł i górnik. Samo uruchomienie oprogramowania Satoshi Nakamoto na komputerze osobistym wystarczyło, aby wziąć udział w procesie mining i, w wielu przypadkach, znaleźć bloki.



Procesor może zrobić wszystko, ale nie jest do niczego zoptymalizowany. Wykonuje bardzo ogólne instrukcje ze złożoną logiką. W przypadku zadań takich jak powtarzalne hashowanie nagłówków bloków nie jest to idealne narzędzie, ale przy uruchamianiu sieci trudność jest tak niska, że jest więcej niż wystarczająca do znalezienia bloków.



Ten okres jest ważny, ponieważ przypomina nam o ważnej kwestii: proof of work nie zależy od konkretnej kategorii sprzętu. Liczy się zdolność do obliczania hashy szybciej niż inni, przy danym koszcie. Gdy tylko pojawia się przewaga techniczna, jest ona automatycznie przekształcana w przewagę ekonomiczną. Ale w wartościach bezwzględnych nadal można dziś próbować znaleźć bloki Bitcoin przy użyciu konwencjonalnego procesora. Takie podejście przyjął na przykład projekt NerdMiner. Szanse na znalezienie bloku są praktycznie zerowe, ale nadal istnieje nieskończenie małe prawdopodobieństwo.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Przejście na procesory graficzne



Wkrótce górnicy zdali sobie sprawę, że wąskim gardłem nie jest moc, ale zdolność do równoległego wykonywania ogromnej liczby podobnych operacji. Dokładnie to mogły zrobić procesory graficzne (GPU). Pierwotnie procesory graficzne zostały zaprojektowane do wykonywania tych samych operacji na dużych ilościach danych. Architektura ta doskonale nadawała się do zadań takich jak wielokrotne haszowanie: zamiast kilku wysoce wszechstronnych rdzeni, masz setki, a następnie tysiące jednostek zdolnych do jednoczesnego wykonywania tych samych instrukcji.



Przy porównywalnym zużyciu energii, GPU może produkować znacznie więcej hashy na sekundę niż CPU. W tym samym czasie bitcoin miał kurs wymiany w stosunku do dolara, jego wartość rosła i pojawiały się platformy wymiany. Od tego momentu charakter mining zaczął się zmieniać. Nie chodziło już tylko o uczestnictwo, ale o zarabianie pieniędzy. Pojawiły się dedykowane konfiguracje: maszyny zbudowane wokół kilku kart graficznych, czasem bez ekranów, z minimalnym systemem i specjalistycznym oprogramowaniem, których jedynym celem było kopanie.



W tym momencie trudność mining zaczęła eksplodować. Pomiędzy połową 2010 a połową 2011 roku wzrosła ona nawet 1000-krotnie. Mechanicznie rozpoczyna się specjalizacja, podobnie jak we wczesnych formach industrializacji, a zwykli użytkownicy - którzy są zadowoleni z uruchamiania oprogramowania Bitcoin na swoich komputerach osobistych - mają teraz bardzo małą szansę na znalezienie ważnego bloku.



![Image](assets/fr/044.webp)



*Źródło: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



Pomiędzy erą GPU a współczesną erą [ASIC](https://planb.academy/resources/glossary/asic) nastąpiła faza pośrednia: wykorzystanie układów FPGA. FPGA to reprogramowalny komponent: można go skonfigurować do bezpośredniej implementacji obwodu logicznego dedykowanego konkretnym obliczeniom, w tym przypadku `SHA256d`. Pomysł polegał na jeszcze większym odejściu od sprzętu ogólnego przeznaczenia (CPU/GPU) w celu zwiększenia efektywności energetycznej. Wkrótce jednak ulepszenia wprowadzone wirtualnie na układach FPGA zostaną fizycznie zastosowane w samych chipach: oto nadejście ASIC.



### Pojawienie się ASIC



Ostatnim etapem specjalizacji sprzętu mining było pojawienie się układów ASIC (*Application-Specific Integrated Circuits*). ASIC to układ zaprojektowany do pojedynczego zadania. W przypadku Bitcoin mining, zadaniem tym jest właśnie wykonanie `SHA256d` z maksymalną prędkością i optymalną wydajnością energetyczną. W przeciwieństwie do GPU, ASIC nie jest używany do uruchamiania gier, renderowania 3D lub sztucznej inteligencji. Służy do hashowania i to wszystko.



![Image](assets/fr/045.webp)



*ASIC S21 XP wyprodukowany przez Bitmain*



Ta specjalizacja ma dwie główne konsekwencje:




- Pierwszą z nich jest skok wydajności i efektywności. W przypadku urządzeń porównywalnej generacji, ASIC produkuje znacznie więcej hashy na sekundę niż GPU, zużywając przy tym mniej energii. Mining z GPU szybko stał się niekonkurencyjny: nawet jeśli działał technicznie, koszt energii elektrycznej znacznie przewyższał oczekiwane przychody w większości kontekstów;
- Drugim jest zmiana modelu: inwestycje przeniosły się głównie na sprzęt klasy przemysłowej. Mining wiąże się teraz z zakupem maszyn zaprojektowanych do tego celu, ich ciągłym zasilaniem, chłodzeniem, konserwacją i pochłanianiem ich przestarzałości. Ponieważ ASIC nie jest ekonomicznie wieczny: kiedy na rynku pojawia się nowa, bardziej wydajna generacja, stare maszyny stają się coraz mniej opłacalne, nawet jeśli pozostają funkcjonalne.



Od tego momentu nie mówimy już tylko o hobby. Mówimy o sektorze, w którym konkurencyjność zależy od równania:




- koszt energii elektrycznej;
- koszt sprzętu i amortyzacja;
- zdolność do chłodzenia i działania na dużą skalę;
- dostępność i niezawodność maszyn;
- szybkość komunikacji;
- itp.



### Farmy Mining



Odizolowana maszyna może wydobywać, ale grupując setki, a następnie tysiące ASIC w jednej lokalizacji, dzielimy koszty stałe, optymalizujemy logistykę i zbliżamy się do modelu wyspecjalizowanego centrum danych.



[Farma mining](https://planb.academy/resources/glossary/mining-farm), w swojej najprostszej formie, to budynek (lub zestaw kontenerów) wypełniony ASIC działającymi 24/7. Wyzwaniem jest teraz utrzymanie stabilnych warunków pracy:




- dostarczają duże ilości taniej, stabilnej energii elektrycznej;
- zarządzanie ciepłem w celu uniknięcia dławienia, ponieważ gęstość energii jest znaczna;
- filtrowanie kurzu, kontrola wilgotności, czyszczenie;
- monitorowanie wydajności urządzenia w czasie rzeczywistym (temperatury, błędy sprzętowe, spadki hashrate itp.).



![Image](assets/fr/043.webp)



*Jeden z siedmiu budynków poświęconych Bitcoin mining w siedzibie Riot Platforms w Rockdale, niedaleko Austin w Teksasie. Ten jest specjalnie poświęcony zanurzeniu mining*



Mining jest obecnie napędzany przez graczy przemysłowych, z których niektórzy są notowani na giełdzie, którzy budują i obsługują farmy na bardzo dużą skalę. Należą do nich MARA Holdings (Nasdaq: `MARA`) i Riot Platforms (Nasdaq: `RIOT`).



![Image](assets/fr/042.webp)



Nawet bez zagłębiania się w szczegóły modeli rentowności, ważne jest, aby zrozumieć, dlaczego mining przyjął taką formę. Proof-of-work jest mechanizmem konkurencyjnym: prawdopodobieństwo znalezienia bloku, a tym samym zarobienia pieniędzy, jest proporcjonalne do udziału hashrate, który wdrażasz. W rezultacie istnieje stała presja na zwiększenie mocy obliczeniowej, zmniejszenie kosztu jednostkowego obliczeń i ograniczenie strat. W rezultacie środowiska, które oferują tańszą energię elektryczną, klimat sprzyjający chłodzeniu lub bogatą infrastrukturę energetyczną, w naturalny sposób stają się bardziej atrakcyjne.



Mining Bitcoin ewoluował w ten sposób od aktywności dostępnej dla każdego na początku, do aktywności zdominowanej przez specjalistyczny sprzęt i profesjonalne operacje. Nie zmienia to jednak zasad protokołu. Teoretycznie każdy może kopać na dowolnej maszynie. Jednak w praktyce poziom trudności i wydajności ASIC sprawił, że krajowy mining stał się w dużej mierze niekonkurencyjny w większości kontekstów.



Oczywiście nadal istnieją sytuacje, w których domowy mining może być interesujący, na przykład jeśli korzystasz z bardzo taniej energii elektrycznej lub jeśli używasz ciepła generated przez swojego górnika do ogrzewania domu w zimie. Ale w każdym przypadku nadal będziesz musiał kupić maszynę wyposażoną w chip ASIC. Co więcej, ponieważ twoja moc mining pozostanie niezwykle mała w stosunku do sieci Bitcoin, będziesz musiał znaleźć sposób na zmniejszenie wariancji swoich dochodów: to jest właśnie rola pul mining, które omówimy w następnym rozdziale.



Jeśli chcesz poznać domowe rozwiązania mining z odzyskiem ciepła, mamy samouczki dotyczące różnych narzędzi, zarówno gotowych do użycia, jak i do samodzielnego montażu:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Grupowanie w pule mining


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Bitcoin wiąże się z bieżącymi i nieuniknionymi kosztami, z których najważniejszym jest zużycie energii przez maszynę. Wydatki te są ponoszone niezależnie od jakichkolwiek wyników, mimo że przychody z mining są z natury rzadkie i losowe. Odkrycie bloku zależy wyłącznie od udziału górnika w hashrate, co sprawia, że zyski są tym bardziej nieprzewidywalne, im mniejszy jest ten udział. To właśnie ten praktyczny problem szybko doprowadził do powszechnego wykorzystania [pul mining](https://planb.academy/resources/glossary/pool-mining). W tym ostatnim rozdziale kursu MIN 101 oferuję wprowadzenie do zasad i działania pul mining w Bitcoin.



### Co to jest basen mining?



Pula mining to organizacja (często usługa online), która agreguje moc obliczeniową wielu niezależnych górników w celu zwiększenia częstotliwości, z jaką ich grupa znajduje bloki. Gdy pula znajdzie blok, nagroda za blok jest następnie redystrybuowana między uczestnikami zgodnie z wewnętrznymi zasadami puli (które zostaną omówione w kursie MIN 201, ponieważ są one zbyt złożone dla MIN 101).



Uczestnicy puli mining są następnie często określani jako "[hashers](https://planb.academy/resources/glossary/hasher)", a nie jako "miners", ponieważ nie wykonują już całej pracy mining, ale po prostu hashują dane przesłane im przez pulę.



Należy uważać, aby nie pomylić puli mining z farmą mining. Są to dwie różne koncepcje. Jak widzieliśmy w poprzednim rozdziale, farma to fizyczna lokalizacja, w której pojedynczy podmiot obsługuje wiele maszyn mining. Z drugiej strony, pula to przede wszystkim wirtualne zgrupowanie: tysiące maszyn, często rozproszonych geograficznie, pracuje pod wspólną koordynacją. Jednak farma może i często uczestniczy w puli.



![Image](assets/fr/048.webp)



### Zmniejszenie wariancji dochodu



Po co więc dołączać do puli? Po prostu dlatego, że wynik aktywności mining jest probabilistyczny: przy każdej próbie hashowania istnieje bardzo mała szansa, że osiągnie ona docelowy poziom trudności, a tym samym wygeneruje prawidłowy blok.



W bardzo długim okresie średnie zarobki powinny być proporcjonalne do udziału w ogólnej liczbie hashrate. Zasada ta wynika bezpośrednio z praw prawdopodobieństwa: każde obliczenie hash stanowi niezależne losowanie, a zgodnie z prawem wielkich liczb częstotliwość, z jaką odkrywasz bloki, zbiega się matematycznie w kierunku twojego udziału w całkowitym hashrate sieci. Jednak w krótkim i średnim okresie rzeczywiste zarobki mogą być bardzo nieregularne. Tę rozbieżność między teoretyczną średnią a losową rzeczywistością nazywamy w matematyce **zmiennością**.



Oto prosty przykład ilustrujący tę zasadę:




- Sieć Bitcoin produkuje średnio 144 bloki dziennie (w przybliżeniu jeden blok co 10 minut);
- Jeśli masz `0,0001%` całkowitego hashrate, twoje oczekiwania to `144 × 0,000001`, czyli `0,000144` bloku/dzień;
- Innymi słowy, powinieneś znaleźć blok średnio co `1 / 0,000144` dni, czyli co 6 944 dni lub około 19 lat.



Wartość ta odpowiada jednak tylko matematycznemu oczekiwaniu: rozkład czasów odkrycia jest zgodny z prawem losowym, więc w praktyce jest całkowicie możliwe, że nigdy nie zostanie odkryty żaden blok, nawet w bardzo długim okresie. Można mieć pecha i nie znaleźć niczego przez bardzo długi czas, jednocześnie ponosząc powtarzające się koszty (energia elektryczna, konserwacja, amortyzacja sprzętu...).



Pula mining zmienia naturę tego problemu: łącząc hashrate, pula znajduje bloki częściej. Każdy uczestnik zgadza się otrzymywać tylko ułamek każdego znalezionego bloku, ale znacznie częściej. Jest to transformacja z wysoce niestabilnego, szeroko rozstawionego dochodu do bardziej regularnego, kosztem dzielenia się nagrodami i płacenia opłat za usługi.



### Dlaczego wariancja spada po zgrupowaniu?



Im wyższa moc obliczeniowa, tym wyższa oczekiwana częstotliwość znalezionych bloków. Co ważniejsze, im częstsze zdarzenia, tym obserwowane wyniki są bliższe średniej statystycznej w danym okresie.



W pojedynkę górnik działający na małą skalę może przez lata nie znaleźć ani jednego bloku, a następnie pewnego dnia otrzymać dużą wypłatę, a potem nic. W puli ta sama probabilistyczna rzeczywistość nadal ma zastosowanie, ale jest wygładzona w skali zbiorowej: pula częściej znajduje bloki, a redystrybucja przekształca te zdarzenia w bardziej regularne wypłaty dla każdego uczestnika. **Pula mining sprzedaje zatem przewidywalność aktywności mining**.



### Historyczne punkty orientacyjne



Jak widzieliśmy w poprzednim rozdziale, na samym początku mining można było wykonać solo na konwencjonalnym komputerze, ponieważ poziom trudności był bardzo niski. Jednak wraz z globalną eksplozją hashrate (GPU, a następnie ASIC), solo mining stało się bardzo czasochłonnym hazardem dla większości uczestników.



Pierwsze pule powstały właśnie w odpowiedzi na tę nową rzeczywistość. Braiins Pool (dawniej Slush Pool / Bitcoin.cz) to pierwsza pula Bitcoin mining: wydobyła swój pierwszy blok 16 grudnia 2010 roku. Sukces tej pierwszej puli mining był błyskawiczny, gdyż w ciągu zaledwie kilku dni zdobyła ona prawie 3,5% globalnej puli hashrate.



![Image](assets/fr/047.webp)



Od strony technicznej, pule zostały następnie zorganizowane wokół wyspecjalizowanych protokołów komunikacyjnych między pulą a górnikami (np. [Stratum](https://planb.academy/resources/glossary/stratum), a następnie Stratum V2), w celu efektywnej organizacji pracy rozproszonej. Przyjrzymy się bliżej tym koncepcjom w naszym szkoleniu MIN 201.



### Współczesna sytuacja



W chwili pisania tego tekstu (początek 2026 r.) globalny Bitcoin hashrate osiąga rząd wielkości zetta-hash na sekundę (= 1 000 EH/s = 1 000 000 000 000 000 000 haszy na sekundę), a prawie wszystkie znalezione bloki pochodzą z pul mining.



Oto dotychczasowy ranking głównych pul mining i ich udziału w hashrate. Ranking ten prawdopodobnie ulegnie zmianie do czasu przeczytania tego kursu. Aktualne dane można znaleźć na stronie [mempool.space](https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Źródło [mempool.space](https://mempool.space/graphs/mining/pools), dane z jednego miesiąca, od 16 grudnia 2025 r. do 16 stycznia 2025 r.*



W bardziej zaawansowanym kursie zagłębimy się w wewnętrzne funkcjonowanie puli (udziały, protokoły sieciowe, metody płatności...), ponieważ to właśnie tutaj pojawiają się szczegóły, które określają zarówno rentowność górnika, jak i potencjalne implikacje dla Bitcoin.



---

Doszliśmy do końca MIN 101. Dziękujemy za dotrwanie do końca. Jeśli chcesz ocenić umiejętności nabyte podczas kursu, w następnej sekcji czeka na Ciebie egzamin końcowy.



Z podstawową wiedzą, którą właśnie zdobyłeś, możesz teraz wziąć udział w bardziej zaawansowanych kursach mining na Plan ₿ Academy, czy to w teorii, jak ten, czy w bardziej praktycznych kursach, abyś i ty mógł zacząć uczestniczyć w Bitcoin mining!



# Część końcowa


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Recenzje i oceny


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Egzamin końcowy


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Wnioski


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>