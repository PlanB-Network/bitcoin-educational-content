---
name: Konfiguracja pierwszego węzła Bitcoin
goal: Zrozumienie, instalacja, konfiguracja i korzystanie z węzła Bitcoin
objectives: 


  - Zrozumienie roli i celu węzła Bitcoin.
  - Identyfikacja różnych dostępnych rozwiązań sprzętowych i programowych.
  - Zainstaluj i skonfiguruj Full node (Bitcoin core).
  - Użyj parasola Interface i dodaj przydatne aplikacje.
  - Podłącz osobisty Wallet do własnego węzła.
  - Poznaj zaawansowane ustawienia i najlepsze praktyki bezpieczeństwa.


---
# Zostań suwerennym bitcoinerem



Prawdopodobnie znasz powiedzenie "Nie twoje klucze, nie twoje monety", które zachęca do samodzielnego przechowywania bitcoinów. Posiadanie własnych kluczy jest rzeczywiście niezbędnym pierwszym krokiem, ale to nie wystarczy. Aby osiągnąć prawdziwą suwerenność monetarną, należy również zainstalować i używać własnego węzła Bitcoin. Ten kurs został zaprojektowany, aby poprowadzić Cię przez ten fundamentalny krok w Twojej podróży Bitcoin!



BTC 202 to przystępny kurs zaprojektowany, aby nauczyć Cię, jak wykonać własny węzeł Bitcoin, nawet jeśli nie jesteś ekspertem technicznym. Zaczniemy od zdefiniowania, czym jest węzeł Bitcoin, do czego służy i dlaczego absolutnie konieczne jest samodzielne wykonanie takiego węzła. Następnie poprowadzę cię krok po kroku przez wybór sprzętu, instalację niezbędnego oprogramowania, podłączenie Wallet i dokonanie pierwszych możliwych optymalizacji, aby pójść dalej.



Uruchomienie węzła Bitcoin to nie tylko opcja dla ekspertów; to konieczność. Jest to narzędzie odpornościowe, które każdy użytkownik musi zrozumieć i wdrożyć. Ten kurs jest punktem wyjścia do stania się suwerennym bitcoinerem!




+++




# Wprowadzenie


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Przegląd kursu


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Witamy w BTC 202, gdzie dowiesz się, jak łatwo i samodzielnie zainstalować, skonfigurować i używać węzła Bitcoin. Ale to nie wszystko: dowiesz się również więcej o miejscu i funkcji węzłów w systemie Bitcoin. Kurs przeplata wyjaśnienia teoretyczne z praktycznymi ćwiczeniami.



### Część 1 - Wprowadzenie



W tej pierwszej części kursu wyjaśnimy podstawowe pojęcia, a następnie przejdziemy do bardziej precyzyjnych definicji. Co to jest węzeł? Jakie są różnice między węzłem, Wallet i Miner? Następnie dowiesz się o Bitcoin core i implementacjach protokołu. Celem jest mówienie tym samym językiem, uniknięcie nieporozumień i ustanowienie solidnych podstaw teoretycznych.



### Część 2 - Stawanie się suwerennym bitcoinerem



W tej drugiej części zacznę od wyjaśnienia, dlaczego ważne jest uruchomienie własnego węzła Bitcoin. Następnie zbadamy różne typy węzłów, które istnieją (kompletne, pruned, SPV...), jak działają i jakie są ich implikacje techniczne.



Następnie przedstawimy przegląd oprogramowania dostępnego do uruchomienia węzła Bitcoin, w tym jego zalety i wady. Na koniec przedstawimy kilka bardzo praktycznych zaleceń dotyczących wyboru sprzętu odpowiedniego do potrzeb i budżetu.



Ta sekcja ilustruje zatem ścieżkę suwerennego bitcoinera: zrozumieć, dlaczego konieczne jest uruchomienie węzła, wybrać typ węzła, w oparciu o ten wybór, wybrać oprogramowanie i, w zależności od wybranego oprogramowania, określić odpowiedni sprzęt.



### Część 3 - Łatwa instalacja węzła Bitcoin



Po zakończeniu tych przygotowań nadszedł czas, aby przejść do części 3 poświęconej Umbrel: systemowi operacyjnemu chmury domowej, który upraszcza samodzielny hosting i instalację węzła Bitcoin i Lightning.



Po krótkim wprowadzeniu do Umbrel, przedstawimy szczegółowy samouczek, który poprowadzi Cię przez proces instalacji i konfiguracji na własnej maszynie DIY. Cel tej części jest jasny: posiadanie pierwszego w pełni funkcjonalnego i zsynchronizowanego węzła Bitcoin.



### Część 4 - Podłączanie Wallet do węzła



Po skonfigurowaniu węzła Bitcoin nadszedł czas, aby go użyć! W tej sekcji dowiesz się, jak podłączyć oprogramowanie zarządzające Wallet (takie jak Sparrow wallet) do własnego indeksera Address (Electrs lub Fulcrum) lub bezpośrednio do Bitcoin core, dzięki czemu nie będziesz już zależny od serwerów publicznych.



Przeanalizujemy również rolę indeksatorów i różne metody łączenia się z węzłem (LAN, Tor, Tailscale itp.). Wreszcie, w ostatnim rozdziale dokonamy przeglądu najbardziej przydatnych aplikacji dostępnych na Umbrel dla codziennego bitcoinera.



### Część 5 - Zaawansowane koncepcje i najlepsze praktyki



W tej ostatniej części BTC 202 celem jest pogłębienie wiedzy. Po pierwsze, przyjrzymy się najlepszym praktykom, które należy zastosować w nowym węźle Bitcoin i jak go utrzymać w dłuższej perspektywie.



Następnie zajmiemy się przeglądem niektórych teorii omówionych wcześniej w kursie, w tym szczegółowym zrozumieniem procesu IBD i wykrywania peerów, zbadaniem anatomii węzła i wreszcie nauczeniem się, jak korzystać z pliku `Bitcoin.conf` w celu dostrojenia ustawień.



### Część 6 - Sekcja końcowa



Podobnie jak w przypadku wszystkich kursów Plan ₿ Network, w sekcji końcowej znajduje się egzamin końcowy sprawdzający wiedzę na temat węzłów Bitcoin.



Czy jesteś gotowy, aby włączyć swój pierwszy węzeł Bitcoin? Wyznacz kurs na suwerenność!



## Co to jest węzeł Bitcoin?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Zgodnie z opisem jego twórcy, Satoshi Nakamoto, Bitcoin przedstawia się jako elektroniczny system gotówkowy peer-to-peer. To proste zdanie, będące tytułem Białej Księgi, zawiera wiele wskazówek dotyczących natury Bitcoin:




- Po pierwsze, Satoshi opisuje Bitcoin jako "system", innymi słowy, spójny zestaw komponentów sprzętowych i programowych, które współdziałają w celu świadczenia określonej usługi lub wykonywania określonej funkcji;
- Następnie wyjaśnia, że system ten umożliwia korzystanie z elektronicznej gotówki, tj. formy niematerialnej waluty;
- Wreszcie, podkreśla, że system ten nie jest zależny od żadnego centralnego podmiotu: jest to "peer-to-peer", co oznacza, że to sami użytkownicy obsługują system.



Ponieważ Bitcoin jest systemem, musi być koniecznie uruchamiany na komputerach. A ze względu na jego naturę peer-to-peer, to sami użytkownicy biorą odpowiedzialność za uruchomienie tych maszyn. To, co nazywamy "węzłem Bitcoin", jest dokładnie tym komputerem, na którym działa oprogramowanie implementujące protokół Bitcoin (podobnie jak Bitcoin core, ale do tego wrócimy później). To właśnie umożliwia Bitcoin działanie bez centralnego organu: walidacja jest przeprowadzana w sposób rozproszony, przez tysiące niezależnych maszyn należących do tysięcy użytkowników.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



To właśnie ci użytkownicy zapewniają bezpieczeństwo Bitcoin. Jak wyjaśnia Eric Voskuil w swojej książce *Cryptoeconomics*, bezpieczeństwo Bitcoin nie zależy ani od Blockchain, ani od mocy haszującej, ani od walidacji, decentralizacji, kryptografii, open source, ani teorii gier. Bezpieczeństwo Bitcoin zależy przede wszystkim od osób, które są skłonne narazić się na osobiste ryzyko. Decentralizacja pozwala na rozłożenie tego ryzyka na dużą liczbę osób i tylko ich zdolność do stawienia oporu zapewnia solidność systemu.



Zasada ta jest łatwa do zrozumienia: gdyby Bitcoin zależał od pojedynczego węzła należącego do jednej osoby, uwięzienie tej osoby wystarczyłoby do zamknięcia sieci, ponieważ tylko ona przejęłaby całe ryzyko. W przypadku dziesiątek tysięcy węzłów rozsianych po całym świecie ryzyko jest rozproszone: każdy z tych operatorów musiałby zostać zneutralizowany, aby wyłączyć Bitcoin.



![Image](assets/fr/048.webp)



Możemy zatem rozróżnić i nazwać kilka pojęć, aby wyjaśnić sprawy do końca tego kursu:




- Waluta Bitcoin: jednostka rozliczeniowa używana do transakcji w tym systemie;
- Sieć Bitcoin: zbiór wszystkich połączonych węzłów;
- Węzły Bitcoin: maszyny z uruchomioną implementacją Bitcoin;
- Implementacje Bitcoin: oprogramowanie, które tłumaczy protokół na instrukcje wykonywalne;
- Protokół Bitcoin: zestaw zasad regulujących działanie systemu;
- System Bitcoin: spójne połączenie wszystkich Elements.



### Rola węzła Bitcoin



Węzły Bitcoin tworzą razem tak zwaną sieć Bitcoin. Umożliwiają one działanie całego systemu w sposób autonomiczny, bez odwoływania się do centralnego organu lub hierarchii serwerów.



Od samego początku Bitcoin został zaprojektowany, aby umożliwić każdemu użytkownikowi uruchomienie osobistego węzła. Przypadek ten pozostaje aktualny w przypadku dzisiejszego oprogramowania Bitcoin core, które łączy role Wallet i węzła. Jednak obecnie funkcja ta jest często rozdzielana: wiele nowoczesnych portfeli Bitcoin to po prostu portfele, które łączą się z zewnętrznymi węzłami (należącymi do tej samej osoby lub nie).



### Zachowaj Blockchain



Pierwszym zadaniem węzła jest utrzymanie lokalnej kopii Blockchain. Aby zapobiec Double-spending na Bitcoin bez angażowania centralnego organu, każdy użytkownik musi sprawdzić, czy w systemie nie istnieje żadna transakcja. Jedynym sposobem, aby być tego pewnym, jest znajomość wszystkich transakcji dokonanych na Bitcoin. Z tego powodu wszystkie transakcje są znakowane czasem i grupowane w bloki, a każdy węzeł przechowuje cały Blockchain.



> Jedynym sposobem na potwierdzenie braku transakcji jest bycie świadomym wszystkich transakcji.

Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Blockchain jest zatem rejestrem ewoluującym: za każdym razem, gdy nowy blok jest publikowany przez Miner, węzeł sprawdza jego ważność przed dodaniem go do własnej lokalnej kopii łańcucha. Na dzień dzisiejszy (lipiec 2025 r.) kompletny Blockchain przekracza 675 GB, a rozmiar ten nadal rośnie, ponieważ nowy blok jest dodawany średnio co 10 minut.



![Image](assets/fr/049.webp)



Węzeł utrzymuje również lokalny zapis wszystkich UTXO istniejących w danym momencie, znany jako **zestaw UTXO**. Ta baza danych zawiera wszystkie niewydane fragmenty Bitcoin. Powrócimy do tego tematu w szczegółach w ostatniej części kursu.



### Weryfikacja i dystrybucja transakcji



Drugą rolą węzła jest zapewnienie weryfikacji i propagacji transakcji. Gdy nowa transakcja dociera do węzła (za pośrednictwem oprogramowania Wallet lub innego węzła), węzeł sprawdza, czy jest ona zgodna z zestawem reguł (reguły konsensusu i reguły przekazywania). Na przykład:




- wydane bitcoiny muszą istnieć w jego zestawie UTXO (baza danych niewydanych wyjść);
- podpis musi być ważny, a wszystkie warunki wydatków muszą być spełnione (ważny skrypt);
- całkowita kwota wyników nie może przekraczać całkowitej kwoty nakładów, co oznacza, że koszty nie mogą być ujemne.



![Image](assets/fr/050.webp)



Po zatwierdzeniu transakcja jest przechowywana w Mempool węzła, tymczasowej przestrzeni pamięci zarezerwowanej dla niepotwierdzonych transakcji, a następnie przekazywana do innych sieci równorzędnych, z którymi jest połączona. Ten mechanizm dystrybucji i walidacji jest kontynuowany od węzła do węzła. W ten sposób transakcja jest propagowana w całej sieci Bitcoin, a każdy węzeł przechowuje ją w Mempool, dopóki nie zostanie włączona do ważnego bloku przez Miner, który następnie działa na jej pierwsze potwierdzenie.



### Sprawdzanie i dystrybucja bloków



Trzecia rola węzła obejmuje zarządzanie wydobytymi blokami. Gdy Miner wykryje nowy blok z ważnym Proof of Work, jest on rozgłaszany w sieci. Węzły odbierają go, sprawdzają, czy jest zgodny ze wszystkimi zasadami protokołu, a następnie integrują go z własną lokalną kopią Blockchain, jeśli jest ważny. Podobnie jak w przypadku transakcji, nowo zweryfikowane bloki są następnie przekazywane do wszystkich węzłów równorzędnych podłączonych do węzła. Proces ten trwa do momentu, aż wszystkie węzły w sieci Bitcoin będą świadome nowego bloku.



![Image](assets/fr/051.webp)



## Jaka jest różnica między łukiem a Wallet?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



Podczas korzystania z Bitcoin należy rozróżnić dwa różne typy oprogramowania: węzeł i Wallet.



Węzeł Bitcoin, jak wspomniano powyżej, jest oprogramowaniem, które aktywnie uczestniczy w sieci peer-to-peer. Wykonuje on trzy główne zadania:




- kopia zapasowa Blockchain,
- walidacja i przekazywanie transakcji,
- walidacja bloku i przekaźnik.



Z drugiej strony Bitcoin Wallet to oprogramowanie zaprojektowane do przechowywania i zarządzania kluczami prywatnymi. Klucze te umożliwiają wydawanie bitcoinów poprzez spełnienie skryptów blokujących (zazwyczaj poprzez podpis). Wallet może połączyć się z węzłem (lokalnym lub zdalnym), aby sprawdzić status Blockchain i rozgłaszać transakcje, które tworzy, ale jako taki nie jest uczestnikiem sieci.



W niektórych przypadkach te dwie funkcje współistnieją w ramach tego samego oprogramowania, jak ma to miejsce w przypadku Bitcoin core, który służy zarówno jako Full node, jak i Wallet. Jednak wiele popularnych programów Wallet (Sparrow, BlueWallet itp.) wymaga połączenia z zewnętrznym węzłem (własnym lub strony trzeciej) w celu transmisji transakcji i określenia salda Wallet.



![Image](assets/fr/052.webp)



## Jaka jest różnica między węzłem a Miner?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Pojęcia węzła i Miner są często mylone. Jednak te dwa Elements pełnią radykalnie różne funkcje w systemie.



Początkowo, gdy Bitcoin został uruchomiony przez Satoshi Nakamoto w 2009 roku, każdy użytkownik miał uczestniczyć w sieci jako całości. W związku z tym oryginalne oprogramowanie Bitcoin łączyło kilka funkcji jednocześnie: działało jako Wallet, węzeł, a także jako Miner, zdolne do generowania nowych bloków. W tamtym czasie trudność Mining była bardzo niska. Wszystko, co trzeba było zrobić, to uruchomić oprogramowanie Bitcoin na swoim komputerze, aby znaleźć bloki i otrzymać w nagrodę bitcoiny.



Jednak wraz ze stopniową popularyzacją Bitcoin i wzrostem liczby górników, krajobraz konkurencyjny w Mining uległ radykalnej zmianie. Obecnie Mining stał się niezwykle konkurencyjną działalnością, zdominowaną przez graczy przemysłowych wyposażonych w wyspecjalizowaną infrastrukturę. Moc wymagana do wydobycia nowego bloku jest obecnie tak duża, że jest to praktycznie niemożliwe dla indywidualnego użytkownika przy użyciu tylko konwencjonalnego komputera. W rezultacie Mining jest obecnie przeprowadzany głównie przy użyciu wyspecjalizowanych maszyn zwanych ASIC (*Application-Specific Integrated Circuits*). Układy te są zoptymalizowane wyłącznie do uruchamiania podwójnego SHA-256, algorytmu używanego w Mining na Bitcoin.



![Image](assets/fr/053.webp)



W obliczu tej ewolucji role węzła Bitcoin i Miner stały się wyraźnie odrębne. Jak pokazano powyżej, rola węzła Bitcoin jest czysto informacyjna i oparta na walidacji. Rola Miner jest inna:




- Wybiera oczekujące transakcje w Mempool.
- Tworzy on blok kandydujący integrujący te transakcje.
- Szuka ważnego Proof of Work metodą prób i błędów.
- Jeśli znajdzie prawidłowy dowód, rozgłasza blok za pośrednictwem swojego węzła do innych węzłów.



Miner potrzebuje węzła Bitcoin do interakcji z siecią.



Rola Miner jest również czasami odróżniana od roli rozdrabniacza. Rozdrabniacz to maszyna, której zadaniem jest Hash szablonów bloków dostarczanych przez serwer puli, szukając hashy, które spełniają cel trudności zdefiniowany dla udziałów, a nie Bitcoin. Pozostała część procesu Mining, która obejmuje faktyczną budowę bloku, wybór transakcji lub wyszukiwanie Proof-of-Work zgodnie z trudnością Bitcoin, a także dystrybucję, jest przeprowadzana bezpośrednio przez pule.



![Image](assets/fr/054.webp)



Wreszcie, istnieje istotna różnica w zakresie zachęt ekonomicznych między Miner a węzłem. Prowadzenie węzła Bitcoin nie zapewnia bezpośrednich korzyści pieniężnych. Z drugiej strony, udział w Mining przynosi nagrody (dotacje i opłaty transakcyjne) za każdy znaleziony blok.



W części 2 zbadamy bardziej szczegółowo praktyczne i osobiste korzyści płynące z instalacji i korzystania z węzła Bitcoin, wykraczające poza kwestie czysto finansowe.



## Bitcoin core i implementacje protokołów


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Protokół Bitcoin nie jest oprogramowaniem: jest to zestaw milczących reguł współdzielonych przez użytkowników sieci. Definiuje on warunki ważności transakcji, mechanizmy tworzenia pieniędzy, format bloku, warunki Proof-of-Work i wiele innych specyfikacji. Aby wejść w interakcję z tym protokołem, użytkownicy muszą uruchomić oprogramowanie, które implementuje te zasady: jest to znane jako **implementacja** Bitcoin.



Implementacja jest zatem oprogramowaniem węzła: programem zdolnym do łączenia się z innymi maszynami w sieci Bitcoin, pobierania, weryfikowania, przechowywania i propagowania bloków i transakcji oraz lokalnego egzekwowania zasad konsensusu i przekazywania. Każda implementacja jest konkretną interpretacją protokołu, napisaną w danym języku programowania, z własną architekturą, wydajnością i ergonomią. Każda implementacja będzie miała również własną organizację rozwoju, z własnym podziałem obowiązków.



Wśród tych implementacji zdecydowanie dominuje jedna: **Bitcoin core**.



![Image](assets/fr/055.webp)



### Historyczne wdrożenie, które stało się punktem odniesienia



Bitcoin core jest oprogramowaniem referencyjnym dla protokołu Bitcoin. Wywodzi się z oryginalnego kodu napisanego przez Satoshi Nakamoto w latach 2008-2009 i jest jego bezpośrednią kontynuacją. Początkowo znany jako "*Bitcoin*", a następnie "*Bitcoin QT*" (ze względu na dodanie graficznego Interface za pośrednictwem biblioteki Qt), został przemianowany na "*Bitcoin core*" w 2014 roku, aby wyraźnie odróżnić oprogramowanie od sieci. Od wersji 0.5 jest dystrybuowany z dwoma komponentami: `Bitcoin-qt` (graficzny Interface) i `bitcoind` (wiersz poleceń Interface).



Teoretycznie Bitcoin core nie reprezentuje protokołu Bitcoin; jest to raczej jedna z wielu implementacji. Wyróżnia się jednak masowym przyjęciem, wiekiem, solidnością kodu i rygorem procesu rozwoju. W związku z tym w praktyce zasady stosowane przez Bitcoin core są de facto zasadami protokołu Bitcoin: użytkownicy, deweloperzy, górnicy i usługi ekosystemowe odnoszą się prawie wyłącznie do niego.



### Bieżąca dystrybucja implementacji



Według [danych zebranych w sierpniu 2025 r. przez Luke'a Dashjra](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (znanego dewelopera w ekosystemie), rozkład wdrożeń wśród publicznych węzłów sieci wygląda następująco:




- Bitcoin core**: 87.3% węzłów
- Bitcoin Knots**: 12.5
- Inne skumulowane wdrożenia**: 0.2% (btcsuite, Bcoin, BTCD...)



![Image](assets/fr/056.webp)



Innymi słowy, około 9 na 10 węzłów publicznych korzysta z Bitcoin core. Reszta sieci opiera się na bardziej marginalnych klientach (chociaż udział Knots gwałtownie wzrósł w ostatnich miesiącach, zwłaszcza w następstwie debat nad limitem rozmiaru `OP_RETURN`). Te alternatywne implementacje są często utrzymywane przez jedną osobę lub mały zespół.



**Uwaga:** Liczby te są jednak nadal szacunkowe, ponieważ opierają się głównie na *węzłach nasłuchujących*, tj. węzłach akceptujących połączenia przychodzące (z otwartym portem 8333). Węzły niesłuchające* są znacznie bardziej skomplikowane do policzenia, ponieważ nie można się z nimi połączyć bezpośrednio: trzeba czekać na inicjatywę z ich strony, w postaci połączenia wychodzącego. Witryna Luke'a Dashjra twierdzi, że próbuje policzyć również te *węzły niesłuchające*, ale nadal niemożliwe jest uzyskanie idealnie dokładnych danych na ich temat, a aktualizacja tych statystyk nieuchronnie pozostaje w tyle za rzeczywistością.



### Wewnętrzne działanie Bitcoin core



Bitcoin core jest napisany w języku C++. Jest to również projekt open source, który jest utrzymywany przez społeczność programistów, którzy są wolontariuszami lub są opłacani przez różne podmioty (często przez firmy w ekosystemie, które mają żywotny interes w rozwoju Core). [Kod jest hostowany na GitHub](https://github.com/Bitcoin/Bitcoin), a rozwój odbywa się w rygorystyczny sposób:




- Współtwórcy** przesyłają propozycje w formie _pull requests_ (PR). Zasadniczo każdy może zaproponować zmianę, ale musi ona zostać przetestowana, udokumentowana i przejść przez proces wzajemnej weryfikacji.
- **Opiekunowie** mają prawo do zatwierdzania i łączenia PR-ów. To oni gwarantują spójność i stabilność projektu. W lipcu 2025 roku jest ich pięciu: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao i Ryan Ofsky.
- Od lutego 2023 r. nie było **głównego opiekuna**. Rolę tę początkowo pełnił Satoshi Nakamoto w momencie uruchomienia Bitcoin, następnie Gavin Andresen po odejściu Nakamoto na początku 2011 roku, a ostatecznie Wladimir J. Van Der Laan od 2014 do 2023 roku.



![Image](assets/fr/057.webp)



Rozwój Bitcoin core przebiega zgodnie z logiką merytokratyczną: nowi współtwórcy są zachęcani do przeglądania i testowania kodu przed samodzielnym zaproponowaniem jakichkolwiek zmian. Decyzje opierają się na konsensusie technicznym, a większe modyfikacje (szczególnie w obszarach konsensusu) wymagają dyskusji na publicznych kanałach, takich jak listy mailingowe lub kluby recenzentów PR.



### Inne implementacje Bitcoin



Choć marginalne pod względem adopcji, istnieją inne klienty. Głównym z nich jest Bitcoin Knots, opracowany przez Luke'a Dashjra, Fork Bitcoin core, który zawiera dodatkowe opcje i bardziej konserwatywne podejście do rozwoju. Obejmują one ściślejsze ograniczenia dotyczące formatów transakcji.



![Image](assets/fr/058.webp)



Możemy również wspomnieć:




- Libbitcoin**: modułowa biblioteka C++ opracowana przez Amira Taaki i utrzymywana przez Erica Voskuila;
- Bcoin**: implementacja JavaScript, która nie jest już aktywnie utrzymywana;
- BTCD/btcsuit**e: implementacja w Go.



Projekty te przyczyniają się do różnorodności ekosystemu, ale ich przyjęcie pozostaje bardzo ograniczone, co utrudnia niezależną ewolucję Bitcoin core.



### Potęga deweloperów Core



Można by pomyśleć, że twórcy Bitcoin core mają bezpośrednią kontrolę nad Bitcoin, ale tak nie jest. Nie mogą narzucić zmiany protokołu. Ich rolą jest zaproponowanie kodu. To każdy użytkownik, za pośrednictwem swojego węzła, decyduje, czy użyć tego kodu.



Oznacza to, że jeśli zmiana w Bitcoin core nie spotka się z konsensusem, może zostać zignorowana przez węzły, poprzez brak aktualizacji Bitcoin core lub po prostu zmianę implementacji. I odwrotnie, jeśli funkcja pożądana przez użytkowników zostanie zablokowana w procesie rozwoju Core, zawsze można przełączyć się na inną implementację lub Fork projekt.



Jak omówimy w dalszej części tego kursu, to węzły, zgodnie z ich wagą ekonomiczną (tj. kupcy), nadają użyteczność wersji protokołu (a zatem odpowiedniej walucie), akceptując jednostki, które przestrzegają jego zasad. Prawdziwa władza nad Bitcoin leży zatem w gestii kupców, a nie deweloperów.




# Zostań suwerennym bitcoinerem


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Po co skręcać własny węzeł?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



Istnieje powszechne przekonanie, że obsługa węzła Bitcoin jest działaniem czysto altruistycznym, bez osobistych korzyści, wyłącznie w służbie decentralizacji sieci. Niektórzy uważają, że jest to forma obowiązku dla bitcoinerów, aby wspierać system i okazywać wdzięczność Bitcoin.



Rzeczywiście, jak wskazaliśmy w poprzednich rozdziałach, nie ma bezpośrednich korzyści finansowych ze splatania węzła. Można by zatem pomyśleć, że nie ma w tym żadnego osobistego interesu. Jednak prowadzenie własnego węzła przynosi wiele indywidualnych korzyści. Aby cię o tym przekonać, przedstawię w tym rozdziale wszystkie powody, zarówno techniczne, jak i strategiczne, dla których powinieneś zainstalować i używać własnego węzła Bitcoin.



### Bardziej poufne rozpowszechnianie transakcji



Gdy oprogramowanie Wallet łączy się z zewnętrznym węzłem, przesyła swoje transakcje do infrastruktury, która nie znajduje się pod kontrolą użytkownika. Generuje to oczywiste ryzyko inwigilacji: operator zdalnego węzła może analizować szczegóły transakcji, w tym kwoty i częstotliwość, a także, sprawdzając krzyżowo określone metadane (takie jak adresy IP, godziny i lokalizacje), potencjalnie powiązać je z tożsamością użytkownika.



Rzeczywiście, jak wskazano w poprzednim rozdziale, portfele nie komunikują się z siecią Bitcoin za pomocą magii; muszą połączyć się z węzłem, aby sprawdzić salda lub transmitować transakcje. Jeśli nigdy nie skonfigurowałeś własnego węzła, oznacza to, że twój Wallet zależy od infrastruktury strony trzeciej (zwykle firmy stojącej za oprogramowaniem). Ta strona trzecia, zwłaszcza jeśli jest to firma, może obserwować, wykorzystywać, a nawet ujawniać te dane: czy to z powodów komercyjnych, pod przymusem prawnym, czy w wyniku piractwa.



![Image](assets/fr/059.webp)



Korzystając z własnego węzła, transmitujesz swoje transakcje bezpośrednio do sieci, omijając pośredników. Pod warunkiem, że odpowiednio zabezpieczysz swój węzeł (co omówimy później) lub będziesz przestrzegać pewnych standardów, żadne informacje nie zostaną ujawnione: ani twoje IP Address, ani szczegóły twoich transakcji nie przechodzą przez podmiot, którego nie kontrolujesz. Jest to podstawowy warunek zachowania poufności na Bitcoin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Transakcje niepodlegające cenzurze



Z tych samych powodów, o których wspomniano powyżej, oprogramowanie Wallet oparte na węźle strony trzeciej jest podatne na ryzyko cenzury: operator zdalnego węzła może odmówić przekazania pewnych transakcji z różnych powodów. Może uznać je za podejrzane lub sprzeczne z jego polityką. Transakcja może również zostać zablokowana, jeśli nie jest zgodna z zasadami przekazywania węzła. Wreszcie, operator może specjalnie wybrać adres IP Address użytkownika, aby zablokować transmisję jego transakcji.



Z drugiej strony, korzystając z własnego węzła, zapewniasz propagację swoich transakcji w sieci peer-to-peer. Oznacza to, że zachowujesz całkowitą kontrolę nad dystrybucją swoich transakcji, bez zależności od pośrednika. Tak długo, jak transakcja jest zgodna z konsensusem i zasadami przekazywania węzłów połączonych z twoim, będzie ona transmitowana w sieci, a następnie, pod warunkiem uwzględnienia wystarczających opłat, zintegrowana z blokiem przez Miner. Posiadanie własnego węzła gwarantuje neutralne, wolne od uprawnień potwierdzenie transakcji.



### Niezależna weryfikacja danych



Bez osobistego węzła użytkownik pozostaje zależny od strony trzeciej w zakresie dostępu do informacji, takich jak saldo Address, status potwierdzenia transakcji i ważność bloku. Wiąże się to z domniemanym zaufaniem do dokładności i integralności węzła zewnętrznego.



![Image](assets/fr/060.webp)



Uruchomienie Full node oznacza możliwość samodzielnego sprawdzenia wszystkich reguł protokołu dla każdej transakcji i każdego bloku. W rezultacie saldo wyświetlane przez Wallet nie jest danymi otrzymanymi ze zdalnego serwera, ale wynikiem obliczonym lokalnie na podstawie pełnej kopii Blockchain, zatwierdzonej blok po bloku. Takie podejście nadaje pełne znaczenie maksymie bitcoinerów:



> Nie ufaj, weryfikuj.

### Lepsza dystrybucja zabezpieczeń systemu



Każdy węzeł, który dołącza do sieci, wzmacnia redundancję i odporność Bitcoin. Ułatwia on rozpowszechnianie informacji i umożliwia nowym użytkownikom łączenie się ze sobą. Bez węzłów system po prostu nie działałby.



Jak widzieliśmy, bezpieczeństwo Bitcoin nie opiera się na decentralizacji, Mining ani kryptografii: jak w przypadku każdego systemu, opiera się na jednostkach. Dokładniej mówiąc, zależy to od zdolności operatorów węzłów do opierania się przymusowi.



Tym, co wyróżnia zdecentralizowane systemy, takie jak Bitcoin, jest rozkład ryzyka na wszystkie osoby zaangażowane w ich działanie. Prowadzenie własnego węzła Bitcoin oznacza zaakceptowanie części tego ryzyka poprzez zapewnienie bezpieczeństwa swojej instancji; w ten sposób zmniejszasz również ciężar ryzyka dla innych operatorów węzłów.



Nie jest to więc bezpośrednia korzyść osobista: prowadzenie węzła czyni cię częściowo odpowiedzialnym za bezpieczeństwo sieci. Przede wszystkim jest to korzyść zbiorowa, ponieważ zaangażowanie pomaga rozłożyć ryzyko. Z kolei ty zwiększasz swoją własną zdolność do niezawodnego korzystania z Bitcoin.



### Głębsze zrozumienie systemu



Instalacja Full node nie jest trywialną operacją. Obejmuje instalację oprogramowania, zrozumienie podstawowej obsługi, monitorowanie synchronizacji, sprawdzanie dzienników w przypadku problemów, a nawet korzystanie z terminala. To z pewnością doprowadzi do pogłębienia zrozumienia protokołu. Jest to pośrednia, ale nie bez znaczenia zaleta.



Zdobycie tej wiedzy wzmacnia zaufanie do narzędzia i może zmniejszyć ryzyko błędu lub narażenia na oszustwa. Tworzenie własnego węzła jest również formą nauki.



### Wybór reguł do zastosowania



Ważnym aspektem, często źle rozumianym, jest to, że obsługa węzła pozwala wybrać reguły stosowane lokalnie. Istnieją dwa główne rodzaje reguł:





- Zasady konsensusu**:



Są to podstawowe zasady protokołu Bitcoin, zapewniające integralność systemu i ustanawiające kryteria walidacji transakcji i bloków. Każda transakcja, która nie jest zgodna z tymi zasadami konsensusu, nigdy nie może zostać włączona do ważnego bloku. Na przykład transakcja z nieprawidłowym podpisem na jednym z jej wpisów będzie systematycznie wykluczana.



Zmiana tych zasad jest równoznaczna ze zmianą protokołu, a tym samym waluty (Hard Fork). Jednak nawet bez próby ich modyfikacji, prosty fakt ścisłego stosowania istniejących zasad nadaje pewną moc: jeśli blok narusza zasady, węzeł natychmiast go odrzuca.





- Zasady sztafety**:



Są to reguły specyficzne dla każdego węzła Bitcoin, które są dodawane do reguł konsensusu w celu zdefiniowania struktury niepotwierdzonych transakcji akceptowanych w Mempool i przekazywanych do węzłów równorzędnych. Każdy węzeł konfiguruje i stosuje te reguły lokalnie, co wyjaśnia, dlaczego mogą się one różnić w zależności od węzła. Mają one zastosowanie tylko do niepotwierdzonych transakcji: transakcja uznana przez węzeł za "niestandardową" zostanie zaakceptowana tylko wtedy, gdy pojawi się już w ważnym bloku. Zmiana tych zasad nie wyklucza węzła z systemu Bitcoin.



Na przykład transakcja bez opłat jest, zgodnie z zasadami konsensusu, całkowicie ważna, ale zostanie domyślnie odrzucona zgodnie z polityką przekazywania Bitcoin core, ponieważ parametr `minRelayTxFee` jest ustawiony na `0,00001` (w BTC/kB). Możliwe jest jednak obniżenie tego progu na własnym węźle, aby przekazywać transakcje o niższych opłatach, lub odwrotnie, zwiększenie limitu, na przykład do 2 Sats/vB, aby uniknąć przekazywania transakcji o niskich opłatach.



Kręcenie własnym węzłem oznacza stwierdzenie: "Zatwierdzam to, co zdecyduję się zatwierdzić, zgodnie z zasadami, które sam przyjąłem "*. W ten sposób stajesz się aktorem w zarządzaniu systemem, zdolnym do odrzucenia ewolucji, która wydaje ci się nie do przyjęcia, lub do zatwierdzenia aktualizacji zgodnie z własnymi kryteriami.



Możemy więc szybko spróbować zrozumieć, jak dużą władzę masz nad regułami dzięki swojemu węzłowi. Zakres tej władzy zależy od rodzaju reguły.



#### Zasady dotyczące przekaźników



Jeśli chodzi o zasady przekazywania, najważniejszą rzeczą jest po prostu posiadanie węzła, niezależnie od jego działalności gospodarczej. Stawką jest to, czy zgadzasz się na przekazywanie określonych rodzajów transakcji.



Jeśli na przykład uważasz, że transakcje z opłatami mniejszymi niż 1 sat/vB powinny być akceptowane na Bitcoin, możesz dostosować tę regułę na swoim węźle tak, aby rozgłaszał te transakcje, ułatwiając w ten sposób ich propagację w sieci, aż Miner ostatecznie włączy je do ważnego bloku. Zasadniczo jest to więc kwestia władzy nad rozpowszechnianiem transakcji: każdy węzeł ma moc decyzyjną, ponieważ zgoda na przekazanie pewnego rodzaju transakcji jest równoznaczna z promowaniem jej akceptacji w sieci Bitcoin. W rezultacie, jeśli obsługujesz kilka węzłów, masz większy wpływ na politykę przekazywania, ponieważ każdy węzeł ma własne połączenia i obszary wpływu na sieć.



Rzeczywiście, posiadanie jednego lub więcej węzłów skonfigurowanych z określonymi regułami przekazywania oznacza określenie, która część sieci akceptuje propagację danego rodzaju transakcji. Rozprzestrzenianie wiadomości w grafie peer-to-peer, jak ma to miejsce w przypadku transakcji Bitcoin, jest zgodne z logiką teorii perkolacji. Wyobraźmy sobie każdy węzeł jako miejsce, które może być aktywne (`p` = przekazuje) lub nieaktywne (`1-p`). Gdy tylko proporcja `p` przekroczy próg krytyczny (`p_c`), pojawia się gigantyczny komponent: transakcja udaje się przemierzyć sieć i ma wszelkie szanse na dotarcie do Miner. W sieci takiej jak Bitcoin, gdzie każdy węzeł utrzymuje średnio 8 połączeń wychodzących, próg `p_c` jest zwykle ustawiony na zaledwie kilka procent, a nawet niżej, jeśli niektóre węzły mają bardzo dużą liczbę połączeń.



![Image](assets/fr/061.webp)



Dopóki `p` pozostaje poniżej `p_c`, transakcja pozostaje ograniczona do odizolowanych kieszeni i nie dociera do Miner. Gdy tylko próg ten zostanie przekroczony, rozprzestrzenia się niemal natychmiast w całej sieci.



Ostatecznie to górnicy zawsze decydują o tym, czy transakcja zostanie włączona do bloku. Węzły interweniują jednak wcześniej, wpływając na dystrybucję transakcji: określają, czy górnicy będą świadomi danej transakcji. Jeśli transakcja nie zostanie przekazana górnikom, nie jest oczywiście możliwe, aby włączyli ją do bloku.



Dodanie kilku dodatkowych węzłów będzie miało zatem jedynie marginalny wpływ, jeśli sieć jest już w fazie perkolacji dla danego rodzaju transakcji, ale może okazać się decydujące, gdy zbliża się próg perkolacji. Posiadanie lub wpływanie na kilka węzłów, zwłaszcza jeśli są one dobrze połączone, może zwiększyć lub zmniejszyć wartość `p`, a w konsekwencji pośrednio kierować zasadami przekazywania, które określają, które transakcje są widoczne i ostatecznie akceptowane przez górników.



#### Dla zasad konsensusu



Jeśli chodzi o wpływ węzła na zasady konsensusu, decydująca będzie przede wszystkim jego waga ekonomiczna. Jest to kluczowa koncepcja: wartość każdej waluty jest bezpośrednio związana z jej zdolnością do ułatwienia Exchange. Rzeczywiście, jeśli przedmiot nie jest akceptowany przez nikogo w Exchange za towary lub usługi, teoretycznie nie ma on użyteczności pieniężnej. Na przykład, jeśli żaden kupiec nie akceptuje kamyków jako środka płatniczego, nie mają one zastosowania jako pieniądz. Oczywiście użyteczność pozostaje pojęciem subiektywnym w skali indywidualnej, ale na danym terytorium, im większa liczba kupców akceptujących dany przedmiot jako środek Exchange, tym bardziej prawdopodobne jest, że przedmiot ten ma użyteczność pieniężną dla ludzi żyjących na tym terytorium.



Weźmy przykład wioski, w której wielu kupców akceptuje złoto w Exchange za towary: istnieje prawdopodobieństwo, że złoto ma użyteczność pieniężną dla mieszkańców wioski. Wskazuje to, że użyteczność waluty zależy bezpośrednio od decyzji kupców o jej przyjęciu lub odrzuceniu.



Koncepcja ta ma kluczowe znaczenie dla zrozumienia dynamiki władzy w systemie Bitcoin. Satoshi stawia sprawę jasno: Bitcoin jest elektronicznym systemem gotówkowym; innymi słowy, zapewnia usługę, która oferuje formę waluty, Bitcoin (lub BTC). Gdy zasady protokołu są modyfikowane w sposób, który nie jest kompatybilny wstecz (Hard Fork), jest to równoznaczne z utworzeniem nowego systemu, a tym samym nowej waluty. Sukces lub porażka Fork zależy od wielkości jego gospodarki, która z kolei zależy od liczby sprzedawców akceptujących tę nową formę waluty.



![Image](assets/fr/062.webp)



Weźmy przykład: załóżmy, że Bitcoin cierpi z powodu Hard Fork. Istniałyby wówczas 2 różne formy waluty: BTC-1 (oryginalna, niezmieniona wersja) i BTC-2 (nowa waluta z innymi zasadami konsensusu). Jeśli wszyscy sprzedawcy, którzy zaakceptowali BTC-1, nadal będą to robić, ale odrzucą BTC-2, to ta ostatnia będzie teoretycznie miała bardzo ograniczoną użyteczność pieniężną. Jako użytkownik nie byłbym zainteresowany przechowywaniem i używaniem BTC-2, wiedząc, że żaden sprzedawca nie chciałby go w Exchange za towary lub usługi. I odwrotnie, jeśli 50% sprzedawców zdecyduje się akceptować wyłącznie BTC-2, a pozostałe 50% przyjmie tylko BTC-1, wówczas użyteczność BTC-1 teoretycznie zmniejszy się o połowę. Używam terminu "teoretycznie", ponieważ użyteczność pozostaje subiektywna na poziomie indywidualnym i zależy od wielu czynników (takich jak terytorium i nawyki konsumpcyjne), które są trudne do zrozumienia w poszczególnych przypadkach.



W Bitcoin rola "sprzedawcy", rozumianego jako dowolny podmiot o określonej wadze ekonomicznej, obejmuje oczywiście przedsiębiorstwa (sklepy fizyczne, witryny sprzedaży online, usługodawców itp.), ale także platformy Exchange, ponieważ akceptują Bitcoin w Exchange dla innych walut, oraz górników, ponieważ akceptują Bitcoin za pośrednictwem opłat w Exchange za usługę włączenia transakcji do bloku.



Jeśli chodzi o zasady konsensusu, węzeł pozwala skierować aktywność gospodarczą na jedną lub drugą walutę. Na przykład, jeśli masz 10 pełnych węzłów w domu, ale nie prowadzisz żadnej znaczącej działalności gospodarczej, twój wpływ podczas Fork będzie prawie zerowy. I odwrotnie, pojedynczy węzeł używany do zarządzania siecią 200 sklepów akceptujących Bitcoin nadaje znaczną wagę ekonomiczną.



Nie liczy się więc liczba węzłów, ale znaczenie działalności gospodarczej, którą wspierają. Co więcej, jeśli twoja działalność gospodarcza zależy od węzła, którego nie kontrolujesz, jego właściciel zdecyduje, jakiej waluty używasz, o ile pozostaniesz połączony z tym węzłem. Właśnie dlatego prowadzenie i używanie własnego węzła jest szczególnie ważne w kontekście zarządzania systemem:



> Nie twój węzeł, nie twoje zasady.


## Różne typy węzłów Bitcoin


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



Węzeł Bitcoin jest zatem maszyną z uruchomioną implementacją protokołu Bitcoin. Za tą wspólną definicją węzłów kryje się kilka możliwych konfiguracji, z których nie wszystkie oferują ten sam poziom autonomii, zużycia zasobów i użyteczności dla sieci. W tym rozdziale postaramy się zrozumieć te różnice, aby pomóc ci wybrać architekturę węzła, która pasuje do twojego zastosowania i ograniczeń sprzętowych.



### Kompletny węzeł



Full node to po prostu węzeł Bitcoin, który pobiera cały Blockchain z bloku Genesis, weryfikuje każdy blok niezależnie i przechowuje historię całego Blockchain lokalnie. Jest to "normalna" forma węzła Bitcoin, wyobrażona przez Satoshi Nakamoto.



![Image](assets/fr/063.webp)



Full node nie musi nikomu ufać, ponieważ weryfikuje i zna wszystkie informacje w systemie. Jest to typ węzła, który daje największe gwarancje: wiesz, bez polegania na stronie trzeciej, czy płatność jest ważna, czy blok jest ważny, czy reorganizacja jest legalna i tak dalej.



W praktyce Full node wymaga nietrywialnych zasobów, w tym kilkuset gigabajtów na pliki blokowe, procesora zdolnego do sprawdzania poprawności skryptów, pamięci RAM dla Mempool i pamięci podręcznych oraz stabilnej przepustowości. Pierwsza synchronizacja (*IBD*) odczytuje i weryfikuje całą historię: jest intensywna, ale odbywa się tylko raz. Full node aktywnie uczestniczy w sieci, przekazując bloki i transakcje, i może akceptować połączenia przychodzące, aby pomagać innym peerom.



W zależności od potrzeb można dodać indeksator do Full node. Bitcoin core oferuje indeksowanie transakcji jako opcjonalną funkcję (domyślnie wyłączoną), która może być przydatna do określonych celów. Nie zawiera jednak indeksatora Address, który jest często najbardziej poszukiwaną funkcją dla użytkowników indywidualnych. Aby temu zaradzić, można zainstalować dedykowane oprogramowanie na węźle, takie jak Electrs lub Fulcrum, aby przyspieszyć zapytania weryfikujące saldo Address z powiązanych UTXO. Wrócimy do roli indeksatora bardziej szczegółowo w osobnym rozdziale.



### Węzeł pruned



Węzeł pruned waliduje wszystko jako Full node, od bloku Genesis do głowy łańcucha z największą ilością pracy, ale **zachowuje tylko najnowszą część plików bloków**. Po sprawdzeniu starych bloków stopniowo usuwa je, aby pozostać poniżej limitu miejsca, który można ustawić. Ta konfiguracja jest idealna, jeśli masz ograniczenia miejsca na dysku: zachowujesz niezależność walidacji bloków, bez przechowywania pełnego archiwum historii Blockchain. Ta opcja jest szczególnie przydatna, jeśli chcesz po prostu zainstalować Bitcoin core na swoim komputerze osobistym, bez korzystania z dedykowanej maszyny.



![Image](assets/fr/064.webp)



Techniczne implikacje tej opcji są dość proste: węzeł pruned jest doskonale zdolny do rozgłaszania transakcji, uczestniczenia w przekaźniku, weryfikacji bloków i transakcji oraz śledzenia łańcucha. Z drugiej strony, nie może służyć jako źródło danych historycznych poza swoimi ograniczeniami dla innych aplikacji (np. pełnych eksploratorów, indeksatorów, portfeli). Funkcje wymagające archiwum (lub globalnego indeksu) nie będą zatem dostępne.



W praktyce można użyć węzła pruned do podłączenia oprogramowania do zarządzania Wallet, takiego jak Sparrow wallet. Nie będzie jednak możliwe skanowanie transakcji na Wallet, które poprzedzają limit przycinania. Na przykład, jeśli masz transakcję zarejestrowaną w bloku 901 458, ale twój węzeł przechowuje tylko bloki od 905 402 w górę (ponieważ najstarsze były pruned), nie będziesz w stanie zeskanować tej transakcji. Z drugiej strony, jeśli już ją zeskanowałeś, gdy twój węzeł nadal miał tę wysokość bloku, oprogramowanie zarządzające Wallet zapisze informacje i poprawnie wyświetli saldo odpowiednich UTXO.



Krótko mówiąc, śledzenie Wallet działa bezproblemowo na węźle pruned, jeśli utworzysz nowy Wallet, gdy oprogramowanie jest już podłączone do tego węzła. Z drugiej strony możesz napotkać trudności, jeśli przywrócisz stary Wallet, ponieważ przeszłe transakcje, które nie są już przechowywane przez węzeł, nie będą oczywiście możliwe do odzyskania.



### Węzeł świetlny / SPV



Węzeł SPV (*Simplified Payment Verification*), czyli węzeł lekki, zachowuje tylko nagłówki bloków, a nie szczegóły transakcji, i polega na innych pełnych węzłach w celu uzyskania dowodu, że transakcja znajduje się w bloku (dowody Merkle'a za pośrednictwem drzew), dla którego posiada nagłówek. Koncepcja uproszczonej weryfikacji płatności nie jest nowa, została zaproponowana przez samego Satoshi Nakamoto w części 8 Białej Księgi.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Ten typ węzła jest oczywiście znacznie lżejszy pod względem pamięci masowej i wykorzystania procesora niż węzeł Full node lub nawet pruned. Węzeł SPV jest zatem dobrze dostosowany do mniejszych urządzeń i przerywanych połączeń. W rzeczywistości jest on często zintegrowany bezpośrednio z Wallet, zwłaszcza z oprogramowaniem mobilnym, takim jak aplikacja Blockstream.



Kompromisem jest zaufanie i poufność: klient SPV sam nie sprawdza skryptów ani zasad walidacji; zakłada, że łańcuch z największą ilością pracy jest ważny i zależy od jednego lub więcej pełnych węzłów w celu uzyskania odpowiedzi. Korzystanie z tego typu węzła jest zatem lepszą opcją niż łączenie się z węzłem innej firmy; jednak nadal jest mniej korzystne niż posiadanie węzła Full node lub nawet pruned.



![Image](assets/fr/065.webp)



### Który węzeł do jakich potrzeb?





- Użytkownik mobilny / początkujący



Dla początkującego użytkownika posiadającego tylko Wallet w aplikacji mobilnej, korzystanie z węzła SPV jest z pewnością najlepszym sposobem na rozpoczęcie pracy. Instalacja jest szybka, wymaga niewielu zasobów, a doświadczenie jest proste i płynne. Oznacza to, że można samodzielnie zweryfikować pewne informacje, a tym samym w mniejszym stopniu polegać na węzłach stron trzecich, jednocześnie będąc bardziej niezależnym, jeśli chodzi o nadawanie transakcji.





- PC / użytkownik średniozaawansowany



Średnio zaawansowany użytkownik z komputerem PC może zainstalować węzeł pruned, aby korzystać z prawie wszystkich zalet Full node, bez przeciążania swojego komputera na co dzień: pełna walidacja, umiarkowane wykorzystanie dysku i prosta konserwacja. Jest to idealne rozwiązanie do łączenia portfeli stacjonarnych i zachowania niezależności w dystrybucji transakcji, bez inwestowania w dedykowaną maszynę lub przeciążania przestrzeni dyskowej.





- Suwerenny Bitcoiner / zaawansowany



Full node pozostaje najlepszym rozwiązaniem, jeśli chcesz być całkowicie niezależny w korzystaniu z Bitcoin i nie ograniczać się później do zaawansowanych zastosowań, takich jak indeksator, węzeł Lightning, a nawet Block explorer. Dokładnie to zamierzamy zbadać w tym kursie!



## Przegląd rozwiązań programowych


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



Po stronie oprogramowania istnieją 2 główne sposoby uruchomienia węzła Bitcoin:




- bezpośrednio zainstalować implementację protokołu, taką jak Bitcoin core (zalecane) lub Bitcoin Knots,
- lub skorzystać z gotowej dystrybucji (często nazywanej "_node-in-a-box_"), która integruje implementację Bitcoin w ten sam sposób, ale zawiera również system administracyjny Interface, sklep z aplikacjami i gotowe do użycia narzędzia (Lightning, przeglądarki, serwery indeksowe, a nawet aplikacje do samodzielnego hostowania zewnętrzne w stosunku do Bitcoin...).



Oba podejścia prowadzą do tego samego celu: posiadania własnego węzła, ale różnią się pod względem instalacji i użytkowania Interface, konserwacji, możliwości rozbudowy i kosztów. To właśnie zbadamy w tym rozdziale.



### Surowe implementacje węzłów Bitcoin



Instalacja surowej implementacji oznacza bezpośrednie korzystanie z oprogramowania implementacji protokołu Bitcoin (takiego jak Core), bez dodatkowego oprogramowania Layer. Użytkownik samodzielnie zarządza konfiguracją, aktualizacjami i powiązanymi usługami (indeksowanie, API, Lightning, kopie zapasowe itp.) zgodnie z własnymi potrzebami.



Jest to najbardziej suwerenne i elastyczne podejście: wiesz dokładnie, co jest uruchomione, gdzie znajdują się dane i jak wszystko działa. Z drugiej strony, staje się ono bardziej złożone, gdy tylko chcesz wyjść poza proste działanie węzła Bitcoin. Jeśli celem jest tylko posiadanie węzła, złożoność jest porównywalna z węzłem w pudełku, a nawet mniejsza, ponieważ jest to po prostu kwestia instalacji oprogramowania.



#### Bitcoin core (klient ultra-większościowy)



[Bitcoin core jest ultra-większościowym klientem sieci](https://bitcoincore.org/). Pobiera, weryfikuje i utrzymuje Blockchain, zapewnia interfejsy API RPC/REST i może zintegrować Wallet. Jeśli wolisz standardowe narzędzia i czujesz się komfortowo, dodając usługi samodzielnie (takie jak serwer Electrum, eksplorator i LND), lepiej będzie, jeśli użyjesz Core w obecnej formie.



**Korzyści:** Maksymalna stabilność, przewidywalne zachowanie, surowe doświadczenie, łatwa instalacja i konfiguracja.



**Wady:** Musisz ręcznie zbudować resztę stosu, aby utworzyć kompletne środowisko aplikacji, a nie tylko węzeł Bitcoin.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (główny klient alternatywny)



[Bitcoin Knots jest Fork z Bitcoin core](https://bitcoinknots.org/), utrzymywany przez Luke'a Dashjr. Jest to główny klient alternatywny dla Core do implementacji protokołu Bitcoin. W pełni kompatybilny z resztą sieci (w żadnym wypadku nie jest Hard Fork jak Bitcoin Cash), oferuje jednak dodatkowe funkcje, w tym opcje polityki przekazywania, które są nieobecne w Core lub stosowane bardziej rygorystycznie domyślnie w celu ograniczenia tego, co niektórzy uważają za spam.



Istnieją 2 możliwe powody, dla których warto wybrać Knots zamiast Core:




- Techniki**: Różne opcje od Core, szczególnie w zakresie zarządzania przekaźnikami, poprzez określenie, które transakcje są akceptowane i transmitowane przez węzeł.
- Polityka**: Niektórzy ludzie wolą używać alternatywnych klientów, takich jak Knots, z powodów nietechnicznych, zwłaszcza w celu wspierania alternatywy dla Core, a tym samym zmniejszenia jego monopolu. Jeśli Core zostałby kiedykolwiek skompromitowany, przydatne byłoby nie tylko posiadanie solidnych, dobrze utrzymanych alternatywnych klientów, ale także wiedza, jak skutecznie z nich korzystać. Inni używają Knots w celach protestacyjnych, ponieważ stracili zaufanie do programistów Core lub nie akceptują większości kierownictwa klienta.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Osobiście polecam wybrać Core, głównie po to, by szybciej korzystać z łatek bezpieczeństwa. Rzeczywiście, niektóre luki wykryte w Knots są poprawiane z opóźnieniem. Ogólnie rzecz biorąc, proces rozwoju Core jest solidnie zorganizowany i wspierany przez dużą liczbę współpracowników, podczas gdy Knots jest utrzymywany przez jedną osobę i ma znacznie mniejszą społeczność. Z drugiej strony, reguły przekaźnikowe mają tendencję do tracenia swojej użyteczności, zwłaszcza gdy są stosowane tylko przez niewielką część sieci (zgodnie z teorią perkolacji).



### Dystrybucje Node-in-a-box



Węzeł _node-in-a-box_ łączy Bitcoin core (lub Knots) ze wstępnie skonfigurowanym systemem operacyjnym, Interface Web i App Store z usługami samodzielnego hostingu (Lightning, explorers, serwer Electrum, Mempool, serwer BTCPay, Nextcloud itp.) Wystarczy jedno kliknięcie, aby zainstalować, zaktualizować i połączyć te różne moduły.



Jest to znacznie prostsze rozwiązanie do uruchamiania i zarządzania wieloma aplikacjami pomocniczymi na co dzień. Wadą jest to, że gdy wystąpi problem (np. konflikt obrazów Docker, błędna aktualizacja, uszkodzona baza danych), debugowanie może stać się bardzo skomplikowane, ponieważ polegasz na własnej integracji dystrybucji. Co więcej, wsparcie społeczności lub oficjalne jest często skomplikowane.



Tak więc node-in-a-box jest niezwykle łatwy w użyciu, o ile wszystko działa poprawnie, ale w przypadku błędu musisz być przygotowany na długie poszukiwania, czekanie na pomoc i brudzenie sobie rąk.



Większość z tych rozwiązań jest dostępna w dwóch formatach:




- Wstępnie zmontowane urządzenie: kompletny komputer z zainstalowanym systemem operacyjnym. Te maszyny typu pay-as-you-go muszą być po prostu podłączone do sieci i podłączone do Internetu, aby mogły działać. Jeśli pozwala na to budżet, ta opcja ma tę zaletę, że jest bardzo prosta w konfiguracji, często oferuje priorytetowe wsparcie i przyczynia się do finansowania rozwoju, ponieważ model biznesowy tych firm opiera się zazwyczaj na sprzedaży sprzętu.
- Zrób to sam: zainstaluj dystrybucję systemu operacyjnego na własnym komputerze (starym PC, NUC, Raspberry Pi, domowym serwerze...). Jest to najbardziej ekonomiczne rozwiązanie, ponieważ możesz poddać recyklingowi starą maszynę lub wybrać sprzęt, który dokładnie odpowiada Twoim potrzebom i budżetowi. Jest to również najbardziej elastyczna opcja i najbardziej satysfakcjonująca w konfiguracji. To właśnie tym podejściem zajmiemy się w praktycznej części kursu.



Oto przegląd głównych dostępnych rozwiązań node-in-a-box (w 2025 r.):



### Umbrel (umbrelOS i Umbrel Home)



[Dziś Umbrel jest liderem rozwiązań typu node-in-a-box (https://umbrel.com/). Swój sukces zawdzięcza w dużej mierze prostocie instalacji (gdy został uruchomiony na prostym Raspberry Pi), eleganckiemu i intuicyjnemu Interface oraz ekosystemowi aplikacji, który szybko się rozrósł i jest obecnie niezwykle rozbudowany.



![Image](assets/fr/067.webp)



Uruchomiony w 2020 roku jako prosty węzeł Bitcoin wraz z kilkoma aplikacjami pomocniczymi, Umbrel stopniowo ewoluował w w pełni funkcjonalną, nowoczesną chmurę domową.



Nie będę się tutaj zagłębiał w szczegóły dotyczące jego działania i konkretnych funkcji, ponieważ przeanalizujemy je bardziej szczegółowo w pierwszym rozdziale następnej części. Rzeczywiście, na potrzeby tego kursu BTC 202 zdecydowałem się użyć UmbrelOS, który moim zdaniem jest najlepszym obecnie rozwiązaniem typu node-in-a-box dla początkujących i średnio zaawansowanych użytkowników.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9 oferuje StartOS (https://start9.com/), system zaprojektowany z myślą o "suwerennym przetwarzaniu": celem jest, aby każdy posiadał i zarządzał własnym prywatnym serwerem, wzbogaconym o rynek samodzielnie hostowanych aplikacji. Użytkownik może zakupić serwer Start9 (Server One w cenie 619 USD, Server Pure w cenie 899 USD) lub złożyć własny w trybie DIY na własnej maszynie.



Po stronie Bitcoin, StartOS pozwala zainstalować Full node, węzeł Lightning, serwer BTCPay, Electrs i wiele innych usług. Jednak atrakcyjność Start9 wykracza poza to: oferuje możliwość odkrywania, konfigurowania i eksponowania różnego oprogramowania (chmura plików, przesyłanie wiadomości, monitorowanie) w ujednolicony sposób, z pełną kontrolą. Projekt jest zatem skierowany do użytkowników, którzy chcą solidnej platformy do samodzielnego hostowania, a nie tylko prostego węzła Bitcoin. Jest to prawdopodobnie najbardziej kompletny ekosystem po Umbrel.



![Image](assets/fr/068.webp)



Główna różnica w stosunku do Umbrel leży w Interface. Umbrel opiera się na wysoce dopracowanym UX, podczas gdy Start9 oferuje prostszy, bardziej funkcjonalny Interface. Ekosystem aplikacji Start9 jest mniej bogaty niż Umbrel, ale rekompensuje to kilkoma zaletami technicznymi: dostęp do zaawansowanych ustawień aplikacji jest uproszczony, podczas gdy Umbrel szybko staje się restrykcyjny, jeśli żądana opcja nie jest dostarczana przez Interface. Start9 wyróżnia się również w zarządzaniu kopiami zapasowymi: oprócz wydajnego rozwiązania Umbrel dla LND, nie ma ujednoliconego mechanizmu, w przeciwieństwie do Start9. Co więcej, oferuje bardziej dostępne narzędzia do monitorowania i szyfrowane połączenie zdalne (`https`), podczas gdy lokalny dostęp do Umbrel odbywa się przez `http`.



Krótko mówiąc, jeśli po prostu potrzebujesz podstawowych aplikacji dla Bitcoin, bez szczególnego zainteresowania bardzo bogatym ekosystemem Umbrel, a użytkownik Interface nie jest priorytetem, to Start9 jest lepszą opcją. W przeciwnym razie, Umbrel jest lepszym wyborem.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MyNode



[MyNode to dystrybucja skoncentrowana wyłącznie na Bitcoin i Lightning](https://mynodebtc.com/), oferująca Interface, rynek aplikacji i aktualizacje jednym kliknięciem. Można kupić gotowy do użycia sprzęt (*Model Two* dostępny w cenie 549 USD) lub zainstalować MyNode bezpłatnie na własnej maszynie. Projekt oferuje również wersję *Premium* oprogramowania (94 USD), która obejmuje priorytetowe wsparcie i zaawansowane funkcje.



![Image](assets/fr/069.webp)



W praktyce MyNode łączy w sobie wszystkie podstawowe elementy potrzebne do obsługi Full node, a także aplikacje niezbędne dla użytkowników Bitcoin. Dlatego jest to odpowiednie rozwiązanie, jeśli nie potrzebujesz aplikacji spoza ekosystemu Bitcoin, takich jak aplikacje hostowane samodzielnie w systemach Start9 i Umbrel.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz to projekt w 100% open source](https://docs.raspiblitz.org/) (licencja MIT) do montażu węzła Bitcoin i węzła Lightning na Raspberry Pi. Wystarczy pobrać obraz, uruchomić komputer, a następnie postępować zgodnie z instrukcjami kreatora, aby uzyskać działający węzeł w pudełku na Raspberry Pi. Wstępnie zmontowane zestawy są również dostępne od stron trzecich, zwykle w cenie od 300 do 400 USD, w zależności od sprzętu. RaspiBlitz oferuje również szereg dodatkowych, łatwych do zainstalowania aplikacji.



![Image](assets/fr/070.webp)



Jeśli posiadasz Raspberry Pi, jest to doskonała opcja, ponieważ bardziej kompletne systemy, takie jak Umbrel, stają się coraz cięższe dla tego typu mini-PC.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo to skoncentrowany na prywatności node-in-a-box](https://wiki.ronindojo.io/en/home), który automatyzuje wdrażanie Samurai Dojo i Whirlpool, z dedykowanym Interface i wtyczkami zaprojektowanymi specjalnie dla ekosystemu Samurai.



Zasada jest prosta: jeśli korzystasz z Ashigaru Wallet (następcy Fork Samurai Wallet, po aresztowaniu jego twórców) lub jeśli chcesz skorzystać z zaawansowanych narzędzi ochrony prywatności, RoninDojo jest dla Ciebie.



![Image](assets/fr/071.webp)



Projekt oferował wcześniej wstępnie skonfigurowaną maszynę o nazwie Tanto, ale jest ona obecnie niedostępna. Może ona powrócić w późniejszym terminie. W międzyczasie można łatwo zainstalować RoninDojo na Rock5B+ lub Rockpro64, a nawet pośrednio na Raspberry Pi.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



Innym rozwiązaniem [node-in-a-box jest Nodl](https://www.nodl.eu/). Podobnie jak w przypadku poprzednich projektów, można kupić wstępnie skonfigurowany sprzęt (od 599 do 799 euro, w zależności od modelu) lub zainstalować go samodzielnie w trybie DIY.



Po stronie oprogramowania, Nodl integruje Bitcoin core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL, a także BTC RPC Explorer, wszystkie ze zintegrowanym łańcuchem aktualizacji i otwartym kodem źródłowym na licencji MIT.



![Image](assets/fr/072.webp)



Po zapoznaniu się z różnymi rozwiązaniami programowymi, nadszedł czas, aby wybrać maszynę, która będzie hostować węzeł!




## Przegląd rozwiązań sprzętowych


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Teraz, gdy zbadaliśmy już wszystkie możliwości oprogramowania, skupmy się na sprzęcie wymaganym dla węzła. Przedstawię kilka konkretnych porad dotyczących wyboru komponentów, wraz z konfiguracjami dostosowanymi do różnych budżetów. Oczywiście jest to moja osobista opinia i opinia: z pewnością istnieją inne istotne alternatywy oprócz tych przedstawionych tutaj. Co więcej, nie będę powracał do wstępnie zmontowanych maszyn oferowanych przez projekty node-in-a-box, które omówiliśmy już w poprzednim rozdziale. Tutaj skupimy się wyłącznie na rozwiązaniach DIY.



### Czy naprawdę potrzebujesz dedykowanej maszyny?



W ciągu ostatnich kilku lat bitcoinowcy stawali się coraz bardziej świadomi powszechnego błędnego przekonania, szczególnie wraz z popularyzacją node-in-a-box na początku lat 2020: węzeł Bitcoin powinien koniecznie działać na maszynie przeznaczonej wyłącznie do tego celu. Nie jest to jednak prawdą. Do uruchomienia węzła Bitcoin niekoniecznie potrzebny jest dedykowany komputer: Bitcoin core może być uruchomiony na komputerze PC. Jeśli masz wystarczającą ilość miejsca na dysku dla Blockchain lub włączysz przycinanie, możesz zatwierdzić łańcuch, podłączyć Wallet, a nawet zamknąć program, gdy skończysz go używać. Zaleta tego podejścia jest znacząca: zerowa inwestycja początkowa i minimalna złożoność.



![Image](assets/fr/074.webp)



Niemniej jednak, korzystanie z dedykowanej maszyny jest często wygodniejsze. Może działać nieprzerwanie (24/7), być zdalnie dostępny przez cały czas, nie monopolizować zasobów głównego komputera, a przede wszystkim izolować zastosowania (dobra praktyka bezpieczeństwa: jeśli twój osobisty komputer napotka problem, twój węzeł nadal działa i odwrotnie). Pytanie nie brzmi więc "Czy muszę dedykować maszynę?", ale raczej "Czy potrzebuję węzła, który jest stale online, dostępny dla innych urządzeń i zdolny do ewolucji?" (Lightning, indeksatory, dodatkowe aplikacje...). Jeśli odpowiedź jest twierdząca, wybór oddzielnej maszyny znacznie uprości sprawę.



### 3 metody pozyskiwania: recykling, używane i nowe



#### Recykling starego komputera



To najbardziej ekonomiczne rozwiązanie. Większość z nas ma w domu lub u przyjaciół i rodziny stary komputer zbierający Dust: to idealna okazja, aby przywrócić go do użytku! Aby dostosować go do użytku jako węzeł Bitcoin, wystarczy dodać dysk SSD o pojemności 2 TB i, w zależności od potrzeb, wymienić lub dodać paski pamięci RAM w celu zwiększenia pamięci RAM. Za w pełni funkcjonalną maszynę należy zapłacić od 100 do 200 euro.



Przed zakupem jakiegokolwiek sprzętu należy sprawdzić liczbę dostępnych slotów na dyski, typ połączenia (M.2 lub SATA), format pamięci RAM (SODIMM lub DIMM) i jej generację (DDR4 itp.). Powinieneś również skorzystać z okazji, aby wyczyścić maszynę, zwłaszcza wentylator, aby zapewnić optymalną wydajność.



Uważaj jednak, jeśli korzystasz z laptopa: bateria może z czasem stać się problemem (więcej na ten temat w dalszej części rozdziału).



#### Regenerowane lub używane



Rynek jest pełen odnowionych biznesowych mini-PC, takich jak *Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini* lub *Dell OptiPlex Micro*. Maszyny te są solidne, kompaktowe, ciche i energooszczędne. Ich cena jest znacznie niższa od nowych, a łatwo jest znaleźć modele wyposażone w procesory i5/i7 od 6 do 10 generacji i od 8 do 16 GB pamięci RAM, a wszystko to w bardzo atrakcyjnych cenach, zazwyczaj od 70 do 200 euro, w zależności od konfiguracji. Moim zdaniem jest to prawdopodobnie najlepsza opcja, jeśli szukasz dedykowanej maszyny dla swojego węzła Bitcoin.



![Image](assets/fr/075.webp)



Możliwe jest również znalezienie używanych komputerów PC i laptopów sprzed kilku lat, z ciekawymi konfiguracjami i doskonałym stosunkiem jakości do ceny.



**Uwaga: *Urządzenia z flot korporacyjnych, takie jak *ThinkCentre Tiny*, są często wyposażone tylko w port *DisplayPort* (DP) dla ekranu, bez wyjścia HDMI. Nie zapomnij więc zabrać ze sobą adaptera lub kabla DP-HDMI, jeśli go potrzebujesz.



#### Zakup nowego



Jeśli pozwala na to budżet, można również zdecydować się na nową maszynę. Jest to dobra opcja, jeśli chcesz mieć najnowszy sprzęt o dobrej wydajności, zwłaszcza jeśli planujesz używać Umbrel lub Start9 z dodatkowymi aplikacjami spoza ekosystemu Bitcoin do samodzielnego hostingu.



### Jaki typ urządzenia powinienem wybrać?



#### Mini-PC "NUC" / barebone



Mini-PC, moim zdaniem, oferują najlepszy kompromis do hostowania węzła Bitcoin w domu. Oszczędzają miejsce, łatwo mieszczą się na półce, zużywają minimalną ilość energii i nadają się do łatwych modyfikacji sprzętu, takich jak dodanie pamięci RAM lub wymiana dysku SSD.



Osobiście preferuję *Lenovo ThinkCentre Tiny*, który jest bardzo rozpowszechniony na rynku używanym (z flot korporacyjnych); są one szczególnie wytrzymałe i łatwe do modyfikacji. Istnieje oczywiście wiele odpowiedników od innych producentów: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*....



![Image](assets/fr/001.webp)



**Zalety:** niewielkie rozmiary, umiarkowane zużycie energii, niski poziom hałasu, skalowalność (w zależności od modelu) i niezawodność.



**Wady:** nieco droższy niż SBC typu Raspberry Pi, brak wbudowanego ekranu (dostęp zdalny lub przez zewnętrzny monitor), brak baterii (nagłe wyłączenie w przypadku przerwy w dostawie prądu).



#### Dedykowany laptop



Jest to doskonała tania alternatywa dla mini-PC: dziś można znaleźć używane lub nawet nowe laptopy w niskich cenach, wyposażone w przyzwoite procesory, liczne porty, a także zintegrowany ekran i klawiaturę (bardzo praktyczne przy pierwszej instalacji). Przede wszystkim bateria działa jak naturalny UPS: w przypadku przerwy w dostawie prądu węzeł nie wyłącza się nagle, a nawet może działać przez kilka godzin.



![Image](assets/fr/076.webp)



**Najważniejsze cechy:** Rozwiązanie typu "wszystko w jednym", bateria działająca jako UPS (brak przerw w dostawie prądu), uproszczona instalacja dzięki zintegrowanemu wyświetlaczowi i klawiaturze, zintegrowana karta Wi-Fi oraz szeroki wybór używanych i nowych rynków (co często oznacza możliwość negocjacji cen).



**Słabe strony:** nieco wyższe zużycie energii niż w przypadku zwykłego mini-PC, stopniowe zużywanie się baterii podczas pracy 24/7 i utrata pojemności, rzadkie, ale realne ryzyko puchnięcia baterii lub ucieczki termicznej wraz z wiekiem. To głównie ten aspekt sprawia, że uważam mini-PC za lepszą opcję niż laptop: stopniowa degradacja baterii i związane z tym ryzyko.



Jeśli zdecydujesz się na to rozwiązanie, zalecam uważne obserwowanie stanu baterii, aby zapobiec wszelkim niebezpieczeństwom. Zwróć uwagę na nadmierne ciepło, nietypowe zapachy, niestabilność lub zdeformowaną powłokę. W przypadku alarmu należy natychmiast wyłączyć i odłączyć komputer, a następnie zutylizować baterię w wyspecjalizowanym punkcie recyklingu.



**Wskazówka:** Jeśli BIOS/UEFI lub narzędzie producenta na to pozwala, ustaw limit obciążenia (np. 60% lub 80%), aby wydłużyć żywotność baterii.



#### Raspberry Pi i inne SBC: błędny pomysł



Na początku lat 2020-tych, wraz z rozwojem oprogramowania typu node-in-a-box, pojawił się również szał na Raspberry Pi jako sposób na uruchomienie węzła Bitcoin. Pomysł wydawał się atrakcyjny: niedrogi, kompaktowy i dostępny.



![Image](assets/fr/073.webp)



W praktyce, jeśli celem jest wyłącznie uruchomienie węzła Bitcoin bez dodatkowych aplikacji, Raspberry Pi może być wystarczające. Ale gdy tylko zechcesz użyć Umbrel, Start9 lub bogatszego ekosystemu (Block explorer, indeksator Address, węzeł Lightning, aplikacje do samodzielnego hostowania...), maszyna szybko osiągnie swoje granice.



Raspberry Pi ma szereg wad:




- procesory, które są zbyt smukłe, z architekturą ARM, która czasami jest niekompatybilna z niektórym oprogramowaniem lub wymaga większej obsługi;
- Przylutowana pamięć RAM, niemożliwa do rozbudowy, z ograniczonymi konfiguracjami (często maksymalnie 8 GB);
- zewnętrzne pudełka na dyski SSD połączone kablem, częste źródła błędów, wymagające zakupu specjalnej karty dla stabilnego dysku SSD;
- tendencja do szybkiego nagrzewania się i trudności w zapewnieniu prawidłowego chłodzenia;
- konieczność zakupu dodatkowego sprzętu (obudowa, wentylator, karta SSD itp.);
- bardzo ograniczona łączność.



W przeszłości wielką zaletą komputerów SBC, takich jak Raspberry Pi, była ich cena: za kilkadziesiąt euro można było dostać dedykowaną maszynę. Jednak obecnie ceny gwałtownie wzrosły, a po dodaniu całego niezbędnego dodatkowego sprzętu koszt zbliża się do kosztów pierwszych używanych lub odnowionych mini-PC x86, które moim zdaniem oferują znacznie więcej korzyści. Z tego powodu nie polecam decydowania się na SBC.



### Wybór komponentów



#### Pamięć dyskowa: Dysk SSD obowiązkowy, minimum 2 TB



Technicznie możliwe jest uruchomienie węzła Bitcoin na dysku HDD. Problem polega na tym, że wszystko znacznie zwolni, zwłaszcza IBD, który stanie się niezwykle długi ze względu na intensywne wykorzystanie dysku przez Bitcoin core jako pamięci podręcznej (szczególnie w przypadku zestawu UTXO). Dlatego też zdecydowanie odradzam korzystanie z dysku twardego: tworzy to prawdziwe wąskie gardło, poważnie ogranicza przyszłą ewolucję (np. dla węzła Lightning), a nawet może prowadzić do niedopasowania synchronizacji z głowicą Blockchain. Co więcej, ciągłe obciążenie dysku mechanicznego zwiększa ryzyko jego przedwczesnego zużycia.



Dyski SSD radykalnie zmieniają wrażenia użytkownika: wszystko staje się szybsze i płynniejsze, przy znacznie większej niezawodności. Korzystanie z dysków SSD jest zatem (prawie) obowiązkowe dla węzła i nie będziesz tego żałować, zwłaszcza że modele o dużej pojemności są teraz stosunkowo przystępne cenowo.



![Image](assets/fr/077.webp)



Jeśli chodzi o pojemność, 2 TB stopniowo staje się nowym rozsądnym minimum. Latem 2025 r. Blockchain zbliża się już do 700 GB, a jeśli dodamy Umbrel, indekser Address i kilka aplikacji, dysk SSD o pojemności 1 TB szybko się nasyci. Dzięki 2 TB masz wygodny margines na nadchodzące lata (w szerokim szacunku od 5 do 15 lat). Możesz również zdecydować się na 4 TB, jeśli planujesz używać wielu aplikacji na Umbrel, przechowywać duże pliki w hostingu własnym lub jeśli chcesz w dużym stopniu przewidzieć swoje potrzeby w zakresie przestrzeni dyskowej.



![Image](assets/fr/078.webp)



Jeśli chodzi o format, będzie to zależeć od portów dostępnych w komputerze; jednak jeśli to możliwe, zalecam użycie dysku SSD NVMe M.2.



#### Pamięć (RAM): 8 do 16 GB



W przypadku samego Bitcoin core (bez nakładki Umbrel) zalecenia dewelopera wskazują na minimum 256 MB pamięci RAM przy ustawieniach dostosowanych do najniższego ustawienia, 512 MB przy ustawieniach domyślnych i 1 GB do normalnego użytkowania.



Z drugiej strony, jeśli korzystasz z systemu node-in-a-box, takiego jak Umbrel lub Start9, wymagania dotyczące pamięci RAM są znacznie wyższe. Deweloperzy Umbrel zalecają minimum 4 GB pamięci RAM. Może to wystarczyć do uruchomienia tylko Core, ale wkrótce będziesz ograniczony. Dlatego zalecają 8 GB, co również uważam za minimum dla podstawowej konfiguracji wokół Bitcoin (Core, LND, indeksator i kilka aplikacji). Z mojego doświadczenia, z Umbrel i kilkoma dodatkowymi usługami, 8 GB to wciąż trochę mało. Aby czuć się naprawdę komfortowo i mieć pewien margines, zalecałbym 16 GB RAM.



#### Procesor (CPU)



W przypadku węzła Umbrel minimalnym wymaganiem jest dwurdzeniowy 64-bitowy procesor Intel lub AMD. Jeśli chcesz korzystać z kilku aplikacji oprócz Bitcoin core, czterordzeniowy (lub wyższy) procesor zrobi prawdziwą różnicę pod względem płynności. Na przykład procesory i5/i7 od 6. do 10. generacji są doskonałymi opcjami na rynku używanym.



### Przykłady konkretnych konfiguracji



Poniżej proponuję trzy konkretne konfiguracje, dostosowane do różnych budżetów i potrzeb, wraz z dokładnymi modelami do ich obsługi. Wybory te zostały przedstawione jako przykłady w celu zilustrowania informacji zawartych w tym rozdziale; nie masz obowiązku wybierania dokładnie tych modeli. Ponieważ uważam Mini-PC za najlepszą opcję w dłuższej perspektywie, będę polegał na tym formacie dla trzech proponowanych konfiguracji.



*Poniższe ceny mają charakter orientacyjny i mogą różnić się w zależności od regionu, dostawcy i okresu*



Przede wszystkim potrzebujesz dysku SSD, który jest wystarczająco duży, aby pomieścić Blockchain, pozostawiając jednocześnie pole do manewru. Dyski SSD mają ograniczoną żywotność pod względem cykli zapisu i całkowitej ilości zapisanych danych. Jednak węzeł Bitcoin znacznie obciąża dysk podczas zapisu. Dlatego nie polecam modeli klasy podstawowej; zamiast tego sugeruję dysk SSD NVMe, który oferuje znacznie lepszą wydajność.



Jako przykład, na potrzeby tego kursu wybrałem następujący model: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, dostępny za około 120 euro na Amazon. Można również zdecydować się na inne znane marki, takie jak Crucial, Western Digital lub Kingston.



![Image](assets/fr/046.webp)



#### Konfiguracja niskobudżetowa



Oczywiście, jeśli twój budżet jest bardzo ograniczony (poniżej 200 euro), radziłbym nie inwestować w dedykowaną maszynę, ale raczej zainstalować Bitcoin core bezpośrednio na twoim codziennym komputerze (w trybie pruned, jeśli brakuje ci miejsca na dysku).



W przeciwnym razie, dla podstawowego budżetu, polecam *HP EliteDesk 800 G2 Mini*. Na Amazonie znalazłem odnowiony model za 96 euro, wyposażony w procesor Intel Core i5 6. generacji i 8 GB pamięci RAM. Jest to szczególnie interesująca opcja dla początkujących: ten procesor i ta ilość pamięci są więcej niż wystarczające do uruchomienia Core na Umbrel, a także kilku aplikacji jednocześnie, takich jak indeksator Electrs, węzeł Lightning i instancja Mempool, pod warunkiem, że nie przydzielisz zbyt dużej ilości pamięci podręcznej do Core. Co więcej, ten typ mini-PC ułatwia zwiększenie pamięci RAM do 16 GB, na przykład, jeśli zajdzie taka potrzeba (spodziewaj się dopłaty około 30-40 euro za jeden lub dwa wysokiej jakości pendrive'y).



![Image](assets/fr/045.webp)



Następnie wystarczy dodać dysk SSD do budżetu. Zaczynając od dysku Samsung 2TB za 120 euro, otrzymujemy całkowity koszt 216 euro za kompletną, funkcjonalną maszynę.



#### Konfiguracja średniobudżetowa



Jeśli dysponujesz średnim budżetem w wysokości około 300 euro na maszynę, która będzie hostować twój węzeł, polecam na przykład *Lenovo ThinkCentre Tiny*, wyposażony w wydajny procesor i wystarczającą ilość pamięci RAM. Na Amazonie znalazłem odnowiony model za 180 euro, wyposażony w procesor Intel Core i7 6. generacji i 16 GB pamięci RAM. Po dodaniu dysku SSD o pojemności 2 TB w cenie 120 EUR, całkowity koszt wynosi 300 EUR.



![Image](assets/fr/044.webp)



Dzięki tej maszynie masz wygodną konfigurację: szybki IBD i możliwość uruchamiania wielu aplikacji na Umbrel lub Start9 bez trudności. Właśnie takiej konfiguracji używam w tym kursie BTC 202.



#### Wysokiej klasy konfiguracja



Przy większym budżecie możliwości stają się znacznie szersze. Można wybrać konfigurację DIY, a nawet zdecydować się na wstępnie zmontowaną maszynę oferowaną bezpośrednio przez projekt node-in-a-box.



Na przykład *ASUS NUC 14 Pro* jest dostępny jako nowy w Amazon za 540 euro. Za tę cenę otrzymujemy procesor Intel Core Ultra 5 (najnowszy i szczególnie wydajny), któremu towarzyszy 16 GB pamięci RAM DDR5. Dzięki takiej konfiguracji będziesz w stanie ukończyć IBD w rekordowym czasie i bez trudu zainstalować wymagające aplikacje.



Jest to niezwykle wygodna konfiguracja, a nawet przesada, jeśli początkowym celem jest po prostu uruchomienie węzła Bitcoin. Z drugiej strony, jeśli chcesz w pełni wykorzystać wszystkie aplikacje self-hosting dostępne na Umbrel i Start9, ten poziom mocy jest właśnie dla Ciebie.



![Image](assets/fr/043.webp)



W zależności od zamierzonego zastosowania, można zdecydować się na dysk SSD o pojemności 2 TB, tak jak w innych konfiguracjach, lub bezpośrednio na dysk SSD o pojemności 4 TB w cenie 260 euro, jeśli chcesz również przechowywać pliki osobiste i rozszerzyć możliwości samodzielnego hostingu. W przypadku dysku SSD o pojemności 2 TB całkowity koszt konfiguracji wynosi 660 euro, a w przypadku dysku SSD o pojemności 4 TB - 800 euro.



### Kilka dodatkowych wskazówek





- Jeśli chcesz kupić używany sprzęt i zapłacić bitcoinami, przyjdź na spotkanie w pobliżu! Rozmawiając z innymi uczestnikami, z pewnością znajdziesz odpowiedni sprzęt w dobrej cenie, jednocześnie pomagając utrzymać przy życiu gospodarkę o obiegu zamkniętym wokół Bitcoin. Jest to również okazja do skorzystania z rzetelnych porad społeczności.





- Do połączenia z Internetem potrzebny będzie oczywiście kabel Ethernet RJ45, przynajmniej na czas instalacji systemu.





- Niektóre środowiska, takie jak Umbrel, pozwalają na korzystanie z Wi-Fi, ale wydajność będzie generalnie gorsza (zwłaszcza jeśli chcesz zdalnie korzystać z węzła Lightning, ponieważ może to mieć wpływ). Jeśli wybierzesz Wi-Fi, upewnij się, że twoje urządzenie ma wbudowaną kartę lub dodaj kompatybilny klucz sprzętowy.





- Należy zawsze używać oryginalnego zasilacza Supply producenta urządzenia. Ma to kluczowe znaczenie dla zapobiegania uszkodzeniom sprzętu i ryzyku wzniecenia pożaru.





- Jeśli urządzenie nie ma wbudowanego akumulatora, warto zainwestować w falownik, aby uniknąć nagłych wyłączeń.





- W zależności od wartości sprzętu i położenia geograficznego, odpowiedni może być również system odgromowy, bezpośrednio w rozdzielnicy lub na używanej listwie zasilającej.





- Wreszcie, pamiętaj o optymalizacji chłodzenia swojego komputera: regularnie go czyść i zainstaluj w chłodnym, dobrze wentylowanym, niezatłoczonym miejscu, aby uniknąć przegrzania, które może prowadzić do throttlingu (dobrowolnego ograniczenia prędkości procesora).



# Łatwa instalacja węzła Bitcoin


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: znacznie więcej niż węzeł Bitcoin


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel jest osobistym serwerowym systemem operacyjnym zaprojektowanym by uczynić self-hosting dostępnym: instalujesz Umbrel, otwierasz przeglądarkę na `umbrel.local` i zarządzasz wszystkim poprzez prosty zdalny Interface.



Projekt najpierw spopularyzował ideę Bitcoin i węzła Lightning za jednym kliknięciem, a następnie rozwinął się w prawdziwą "domową chmurę": przechowywanie plików i zdjęć, strumieniowanie multimediów, narzędzia sieciowe, automatykę domową, lokalną sztuczną inteligencję i setki aplikacji instalowanych ze zintegrowanego sklepu App Store.



W Umbrel każda aplikacja działa w kontenerze Docker (izolacja, atomowe aktualizacje, niezależny start/stop). Interface centralizuje dostęp do wszystkich tych aplikacji, oferując pojedyncze logowanie (z opcjonalnym 2FA), aktualizacje systemu operacyjnego i aplikacji jednym kliknięciem, monitorowanie maszyny na żywo (procesor, pamięć RAM, temperatura, pamięć masowa), zarządzanie uprawnieniami między aplikacjami i przegląd ich zużycia.



Celem Umbrel jest zatem przywrócenie kontroli i poufności danych, bez polegania na usługach w chmurze, poza zwykłą obsługą węzła Bitcoin.



### Umbrel Home vs umbrelOS



Umbrel oferuje dwa różne podejścia:





- [**Umbrel Home**](https://umbrel.com/umbrel-home): jest to gotowy do użycia mini-serwer, specjalnie zaprojektowany i zoptymalizowany pod kątem umbrelOS. Kompaktowy, cichy, podłączony do sieci Ethernet, jest wyposażony w dysk SSD NVMe (opcjonalnie do 4 TB), 16 GB pamięci RAM i czterordzeniowy procesor. Zamawiasz go, podłączasz i wchodzisz na stronę `umbrel.local`. Możesz mieć działający Umbrel w ciągu kilku minut. To jest opcja plug-and-play.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): jest to system operacyjny, który można zainstalować na własnym sprzęcie (mini-PC, NUC, tower, dedykowany laptop...). Masz ten sam Interface i ten sam App Store, co na Umbrel Home.



![Image](assets/fr/080.webp)



W obu przypadkach doświadczenie użytkownika jest identyczne po stronie oprogramowania: administracja oparta na przeglądarce, aktualizacje jednym kliknięciem, instalacja aplikacji na żądanie... Rozwiązanie DIY jest często bardziej ekonomiczne niż zakup Umbrel Home (w zależności od używanej maszyny). Jednak niekoniecznie zalecałbym, aby zawsze wybierać opcję DIY, ponieważ **zakup Umbrel Home przyczynia się bezpośrednio do finansowania rozwoju projektu**, ponieważ jego model biznesowy opiera się na sprzedaży sprzętu. I szczerze mówiąc, przy 389 euro za 2 TB pamięci masowej, cena pozostaje bardzo rozsądna, biorąc pod uwagę jakość oferowanego urządzenia.



![Image](assets/fr/079.webp)



W następnym rozdziale zbadamy, jak zainstalować umbrelOS DIY na własnej maszynie. Możesz jednak śledzić ten kurs BTC 202 w ten sam sposób, jeśli zdecydowałeś się na Umbrel Home.



### Przypadek użycia: z węzła Bitcoin do chmury domowej



Umbrel może pozostać bardzo minimalistyczny i skupiać się wyłącznie na Bitcoin lub ewoluować w prawdziwy wielofunkcyjny serwer osobisty, w zależności od potrzeb. Oto główne zastosowania Umbrel:





- Prosty węzeł Bitcoin**: jest to podstawowe zastosowanie, na którym Umbrel opierał się od samego początku. Możesz uruchomić Bitcoin core (lub Knots), podłączyć portfele bezpośrednio do węzła, wystawić serwer Electrum, hostować Mempool Block explorer, aby wyświetlić Blockchain i oszacować opłaty... To właśnie na tych zastosowaniach skupimy się w tym kursie.



![Image](assets/fr/082.webp)





- Lightning Network**: Umbrel umożliwia również wdrożenie LND lub Core Lightning, dwóch implementacji Lightning Network, do zarządzania własnym węzłem Lightning. Będziesz mógł otwierać kanały, zarządzać płynnością, dokonywać płatności, automatyzować bilansowanie, oferować usługi, łączyć zdalny Wallet lub korzystać z zaawansowanego zarządzania Interface dzięki wielu dostępnym aplikacjom. Przyjrzymy się temu konkretnemu przypadkowi użycia w naszym następnym kursie LNP 202.



![Image](assets/fr/083.webp)





- Ogólny self-hosting**: z Nextcloud, Immich, Jellyfin/Plex, blokerami reklam w całym DNS (Pi-hole/AdGuard), VPN (WireGuard, Tailscale), automatyką domową (Home Assistant), kopiami zapasowymi, zarządzaniem notatkami, narzędziami biurowymi, lokalną AI (Ollama + Open WebUI)... Umbrel może stać się Twoim osobistym serwerem, pozwalając Ci odzyskać kontrolę nad Twoimi danymi. Sam hostujesz usługi, z których korzystasz na co dzień, z dopracowanym doświadczeniem użytkownika, które bardzo przypomina rozwiązania zewnętrzne, zachowując pełną kontrolę nad swoimi danymi i prywatnością.



Wdrażając aplikacje w kontenerach, możesz dowolnie kształtować Umbrel: zacznij od prostego węzła Bitcoin i kilku aplikacji powiązanych z jego ekosystemem, a następnie zainstaluj węzeł Lightning obok węzła Bitcoin i stopniowo wzbogacaj swoją instancję o potrzebne aplikacje do samodzielnego hostowania.



### Społeczność i wzajemna pomoc



Jedną z kluczowych przewag Umbrel nad konkurencją jest ogromna i bardzo aktywna społeczność użytkowników. Można się z nimi skontaktować głównie poprzez [ich Discord](https://discord.gg/efNtFzqtdx) i [ich forum internetowe](https://community.umbrel.com/). Znajdziesz tam nie tylko praktyczne porady, ale przede wszystkim rozwiązania problemów i błędy. To świetne miejsce, by zacząć, rozwijać się i w końcu pomagać innym użytkownikom, dzięki czemu nie zostaniesz sam ze swoim Coin.



![Image](assets/fr/084.webp)



### Licencja UmbrelOS



Kod Umbrel jest publicznie dostępny (można go przeglądać, Fork i modyfikować), ale nie jest objęty prawdziwą licencją open-source. W rzeczywistości umbrelOS jest rozpowszechniany na licencji [*PolyForm Noncommercial 1.0*] (https://polyformproject.org/licenses/noncommercial/1.0.0/), chociaż niektóre powiązane narzędzia programistyczne są dostępne na licencji MIT.



W praktyce z systemem umbrelOS można robić praktycznie wszystko, co się chce, o ile jest to do użytku osobistego, niekomercyjnego: modyfikacja, redystrybucja w celach niekomercyjnych, tworzenie pochodnych dla siebie lub dla organizacji non-profit, pod warunkiem przestrzegania informacji prawnych.



Zabronione jest jednak sprzedawanie Umbrel lub jego pochodnych (na przykład wstępnie zmontowanej maszyny z zainstalowanym systemem umbrelOS), oferowanie usług związanych z Umbrel w celach komercyjnych lub integrowanie jego kodu z produktem w celu osiągnięcia zysku.



Z technicznego punktu widzenia licencja ta nie ogranicza instalacji, audytu ani adaptacji Umbrel do użytku osobistego. Z prawnego punktu widzenia chroni ona projekt przed nieautoryzowaną odsprzedażą lub komercyjnym hostingiem, w szczególności przez dostawców usług w chmurze. Umbrel nie jest zatem open source, choć jego kod pozostaje publicznie dostępny.



Jednak każda aplikacja w sklepie zachowuje własną licencję, często open source.




## Instalacja Full node z parasolem


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Teraz, gdy mamy już wszystkie niezbędne informacje, nadszedł czas, aby zagłębić się w szczegóły. W tym samouczku pokażemy, jak zainstalować kompletny węzeł Bitcoin przy użyciu UmbrelOS.



### Wymagane materiały



Tutaj będziemy używać obrazu UmbrelOS x86 (a dokładniej wersji x86_64). Będziesz mógł postępować zgodnie z tym przewodnikiem na dowolnej maszynie, o ile nie jest ona wyposażona w procesor architektury ARM (nie Apple Silicon, Raspberry Pi itp.). Oznacza to, że każdy komputer z 64-bitowym procesorem Intel lub AMD będzie wystarczający, o ile spełnia minimalne wymagania, w zależności od tego, jak zamierzasz używać Umbrel (zalecany jest co najmniej dwurdzeniowy procesor).



Jeśli zdecydowałeś się na Raspberry Pi 5 (opcja, której nie polecam, jak wspomniano w poprzedniej sekcji), instalacja jest nieco inna. Możesz wtedy postępować zgodnie z tym dedykowanym samouczkiem i powrócić do mojego kursu na stronie Interface `http://umbrel.local`:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Jak wspomniałem w poprzedniej sekcji, zdecydowałem się uruchomić ten samouczek na małym odnowionym komputerze, który znalazłem w dobrej cenie: *Lenovo ThinkCentre M900 Tiny* wyposażonym w procesor Intel Core i7 i 16 GB pamięci RAM. Jest to bardzo wygodna konfiguracja do uruchomienia Umbrela, zwłaszcza dla węzła Bitcoin. Wybrałem jednak tę konfigurację, ponieważ chcę później zainstalować węzeł Lightning i inne bardziej wymagające aplikacje. Dodałem również dysk SSD o pojemności 2 TB do mojego ThinkCentre, aby zachować pełny Blockchain i nadal mieć wygodny margines. W tej konfiguracji całkowity koszt wynosi 270 euro, wliczając wszystkie wydatki.



![Image](assets/fr/001.webp)



Szczególnie lubię serię ThinkCentre Tiny od Lenovo, ponieważ są to kompaktowe, ciche i bardzo wytrzymałe maszyny. Komputery te są bardzo popularne wśród firm i dlatego jest ich dużo na rynku używanych, gdzie można znaleźć ciekawe konfiguracje w cenie od 70 do 200 euro.



Jeśli, tak jak ja, wybrałeś komputer bez monitora, **będziesz musiał podłączyć monitor i klawiaturę** tylko na czas instalacji. Później będziesz mógł uzyskać do niego zdalny dostęp z innego komputera w tej samej sieci (lub za pomocą innych metod, które omówimy w późniejszych rozdziałach). Będziesz także potrzebował kabla Ethernet RJ45 do podłączenia komputera do sieci lokalnej oraz klucza USB o pojemności co najmniej 4 GB do przechowywania obrazu instalacyjnego.



Podsumowując, oto wymagania sprzętowe:




- Komputer z procesorem x86_64 (minimum dwurdzeniowy, zalecany czterordzeniowy);
- Pamięć RAM (minimum 4 GB, zalecane 8 GB lub więcej przy dłuższym użytkowaniu);
- Dysk SSD (zalecany + 2 TB);
- Klucz USB (+ 4 GB) do instalacji obrazu UmbrelOS;
- Monitor i klawiatura (przydatne tylko do początkowej instalacji, jeśli komputer nie jest w nie wyposażony);
- Kabel Ethernet RJ45.



### Krok 1 - Montaż komputera



W zależności od wybranego sprzętu, pierwszym krokiem jest złożenie różnych komponentów komputera. Na przykład w moim przypadku oryginalny dysk SSD miał pojemność tylko 256 GB, więc poddam go recyklingowi do innego użytku i zastąpię go dyskiem SSD o pojemności 2 TB. Jeśli chcesz również wymienić moduły pamięci RAM, nadszedł czas, aby to zrobić.



### Krok 2: Przygotowanie bootowalnego klucza USB



Przed zainstalowaniem systemu UmbrelOS na komputerze należy utworzyć bootowalny klucz USB zawierający system operacyjny. Wszystkie czynności opisane w kroku 2 należy wykonać na komputerze osobistym (a nie bezpośrednio na komputerze, który ma stać się węzłem).





- Zacznij od pobrania najnowszej wersji systemu UmbrelOS w formacie USB:



Przejdź do [oficjalnej strony Umbrel, aby pobrać obraz ISO](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) do instalacji za pomocą klucza USB. Upewnij się, że wybrałeś wersję zgodną z architekturą x86_64 (plik o nazwie `umbrelos-amd64-usb-installer.iso`). Pobieranie może zająć trochę czasu, ponieważ obraz jest dość duży.



![Image](assets/fr/002.webp)





- Zainstalować Balena Etcher:



Aby utworzyć bootowalną pamięć USB, użyj prostego, wieloplatformowego narzędzia o nazwie [Balena Etcher](https://www.balena.io/etcher/). Pobierz i zainstaluj je na swoim komputerze.



![Image](assets/fr/003.webp)





- Włóż pusty klucz USB o pojemności co najmniej 4 GB:



Podłącz klucz USB do komputera (tego, na który właśnie pobrałeś obraz UmbrelOS i Balena Etcher). **Ostrzeżenie: wszystkie dane na kluczu zostaną usunięte**. Upewnij się, że nie zawiera on żadnych ważnych plików.





- Nagraj obraz ISO na pamięć USB za pomocą programu Balena Etcher:



Uruchom Balena Etcher i wybierz pobrany plik ISO `umbrelos-amd64-usb-installer.iso`, klikając przycisk "*Flash from file*". Następnie wybierz klucz USB jako urządzenie docelowe i kliknij "*Flash!*", aby rozpocząć zapis.



![Image](assets/fr/004.webp)



Po zakończeniu operacji otrzymasz bootowalny klucz USB zawierający UmbrelOS, gotowy do uruchomienia i zainstalowania Umbrel na twoim komputerze.



![Image](assets/fr/005.webp)



### Krok 3: Uruchamianie komputera z klucza USB



Teraz, gdy bootowalna pamięć USB zawierająca system UmbrelOS jest gotowa, można uruchomić z niej komputer, aby rozpocząć instalację systemu. Odłącz klucz USB od głównego komputera i włóż go do urządzenia, na którym chcesz zainstalować Umbrel i węzeł Bitcoin.



Jak wyjaśniono na początku tego rozdziału, do ukończenia instalacji potrzebne będzie urządzenie wyświetlające i urządzenie wejściowe. Podłącz wyświetlacz przez HDMI (lub inny port, w zależności od komputera) i podłącz klawiaturę przez USB do komputera. Urządzenia te są wymagane tylko do instalacji; nie będą potrzebne później, ponieważ Umbrel będzie dostępny zdalnie z innego komputera. Podłącz te dwa urządzenia do komputera.



**Wskazówka:** Jeśli nie masz w domu ekranu peryferyjnego, możesz użyć telewizora. Dzięki wejściu HDMI (lub innemu) może on służyć jako tymczasowy ekran podczas instalacji systemu operacyjnego.



Umbrel wymaga oczywiście połączenia z Internetem. Podłącz kabel Ethernet RJ45 między urządzeniem a routerem.



![Image](assets/fr/006.webp)



Włącz urządzenie. W większości przypadków urządzenie powinno automatycznie wykryć klucz USB i uruchomić się z niego. Następnie pojawi się ekran instalacji UmbrelOS Interface.



Jeśli urządzenie uruchamia się w innym systemie lub wyświetla komunikat o błędzie, prawdopodobnie oznacza to, że nie uruchamia się automatycznie z klucza USB. W takim przypadku należy zrestartować komputer i wejść do ustawień BIOS/UEFI (zwykle dostępnych po naciśnięciu `DEL`, `F2`, `F12` lub `ESC`, w zależności od producenta komputera). Następnie zmień kolejność uruchamiania, aby nadać priorytet kluczowi USB. Następnie uruchom ponownie urządzenie, aby uruchomić UmbrelOS.



### Krok 4: Instalacja systemu UmbrelOS na komputerze



Po uruchomieniu urządzenia z pamięci USB, zostaniesz powitany przez instalację Interface UmbrelOS. Ten krok obejmuje instalację systemu bezpośrednio na wewnętrznym dysku Hard.



Na wyświetlonym ekranie wyświetlona zostanie lista wszystkich wewnętrznych urządzeń pamięci masowej wykrytych przez komputer. Każdemu dyskowi towarzyszy numer, nazwa i pojemność. Zlokalizuj dysk, na którym chcesz zainstalować Umbrel. **Ostrzeżenie: wszystkie pliki na tym dysku zostaną trwale usunięte



![Image](assets/fr/007.webp)



Po zidentyfikowaniu właściwego dysku (zwykle tego o największej pojemności, aby pomieścić Blockchain), zanotuj przypisany do niego numer. Na przykład, jeśli wybrany dysk pojawia się pod numerem `2`, wystarczy wpisać `2`, a następnie nacisnąć klawisz `Enter` na klawiaturze.



![Image](assets/fr/008.webp)



Program sformatuje wybrany dysk, zainstaluje UmbrelOS i automatycznie skonfiguruje system. Może to potrwać kilka minut. Proces powinien przebiegać bez zakłóceń.



![Image](assets/fr/009.webp)



Po zakończeniu instalacji zostanie wyświetlony monit o wyłączenie urządzenia. Naciśnij dowolny klawisz, aby wyłączyć komputer.



![Image](assets/fr/010.webp)



Możesz teraz usunąć klucz USB, klawiaturę i ekran, które nie są już potrzebne dla Umbrel. Wszystko, co pozostało z węzła, to zasilanie Supply i kabel Ethernet RJ45.



![Image](assets/fr/011.webp)



Przed ponownym uruchomieniem urządzenia należy sprawdzić następujące dwa punkty:





- Klucz USB jest odłączony**: jeśli pozostanie podłączony, system może uruchomić się ponownie na nim zamiast na dysku wewnętrznym;
- Kabel Ethernet jest podłączony**: urządzenie musi być podłączone do routera, aby działać.



Naciśnij przycisk zasilania. System uruchomi się automatycznie z dysku wewnętrznego, na którym zainstalowano system UmbrelOS. Pierwsze uruchomienie może potrwać około **5 minut**. W tym czasie Umbrel inicjalizuje swoje usługi i Interface.



Z innego komputera (codziennego PC) podłączonego do **tej samej sieci lokalnej**, otwórz przeglądarkę internetową (Firefox, Chrome...) i przejdź do:



```
http://umbrel.local
```



Ten Address służy do zdalnego dostępu do graficznego Interface użytkownika Umbrel Interface i rozpoczęcia konfiguracji.



Jeśli Address `http://umbrel.local` nie działa w przeglądarce po odczekaniu co najmniej 5 minut, po prostu spróbuj:



```
http://umbrel
```



Jeśli to nadal nie działa, wpisz lokalny adres IP Address Umbrel bezpośrednio w przeglądarce. Na przykład (zastąp `42` numerem komputera hostującego Umbrel w sieci lokalnej):



```
http://192.168.1.42
```



Aby zidentyfikować Umbrel's IP Address, istnieje kilka metod, od najprostszych do najbardziej zaawansowanych:





- Uzyskaj dostęp do administracji routera Interface i znajdź adres IP Address urządzenia Umbrel w sieci lokalnej.





- Użyj oprogramowania do skanowania sieci, takiego jak Angry IP Scanner, aby wykryć podłączone urządzenia i zlokalizować IP Umbrel Address.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- W ostateczności podłącz ponownie monitor i klawiaturę do urządzenia, zaloguj się (domyślny login: `umbrel`, hasło: `umbrel`), a następnie wpisz następujące polecenie:



```
hostname -I
```



Teraz możesz korzystać z Umbrel!



### Krok 5: Rozpoczęcie pracy z Umbrel



Aby rozpocząć konfigurację Umbrel, kliknij przycisk "*Start*".



![Image](assets/fr/013.webp)



#### Utwórz konto



Wybierz pseudonim lub wprowadź swoje imię i nazwisko, a następnie ustaw silne hasło. Bądź ostrożny: to hasło jest jedyną barierą chroniącą dostęp do Umbrel z twojej sieci (a zatem potencjalnie do twoich bitcoinów, jeśli uruchomisz węzeł Lightning na Umbrel). Chroni również zdalny dostęp przez Tor lub VPN, jeśli te usługi są włączone.



Wybierz silne hasło i upewnij się, że przechowujesz co najmniej jedną kopię zapasową (zalecany jest menedżer haseł).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Po wprowadzeniu hasła kliknij przycisk "*Twórz*".



![Image](assets/fr/014.webp)



Konfiguracja Umbrel została zakończona.



![Image](assets/fr/015.webp)



#### Odkrycie Interface



Umbrel Interface jest dość intuicyjny:





- Na stronie głównej można wyświetlić zainstalowane aplikacje i widżety.



![Image](assets/fr/016.webp)





- "*App Store*" umożliwia instalowanie nowych aplikacji,



![Image](assets/fr/017.webp)





- Menu "*Files*" centralizuje wszystkie dokumenty przechowywane na Umbrel.



![Image](assets/fr/018.webp)





- Menu "*Ustawienia*" pozwala modyfikować ustawienia Umbrela i uzyskiwać dostęp do jego informacji, w tym:
    - Aktualizacja, ponowne uruchomienie lub zatrzymanie urządzenia;
    - Sprawdź dostępną przestrzeń dyskową, wykorzystanie pamięci RAM i temperaturę procesora;
    - Zmiana tapety;
    - Zarządzaj zdalnym dostępem przez Tor, aktywuj Wi-Fi lub 2FA.



![Image](assets/fr/019.webp)



#### Ustawienia zabezpieczeń i połączeń



Przede wszystkim zdecydowanie zalecam włączenie uwierzytelniania dwuskładnikowego (2FA). Dodaje to dodatkowe zabezpieczenie Layer do hasła. Jest to prawie niezbędne, jeśli planujesz używać Umbrel do przechowywania osobistych plików, uruchamiania węzła Lightning lub wykonywania innych wrażliwych czynności.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Aby to zrobić, kliknij odpowiednie pole w ustawieniach.



![Image](assets/fr/020.webp)



Następnie zeskanuj wyświetlony kod QR za pomocą aplikacji uwierzytelniającej. Następnie wprowadź 6-cyfrowy kod dynamiczny w polu dostępnym w aplikacji Umbrel.



Od teraz każde nowe połączenie z Umbrel będzie wymagało zarówno hasła, jak i 6-cyfrowego kodu wygenerowanego przez aplikację do uwierzytelniania dwuskładnikowego (2FA).



![Image](assets/fr/021.webp)



Jeśli chodzi o zdalny dostęp przez Tor, jeśli nie jest on potrzebny, zalecam pozostawienie tej opcji wyłączonej, aby ograniczyć powierzchnię ataku Umbrel. Domyślnie dostęp do węzła można uzyskać tylko z komputera podłączonego do tej samej sieci lokalnej. Włączenie dostępu przez Tor pozwoli jednak na zarządzanie Umbrelem w ruchu.



Po włączeniu tej funkcji teoretycznie każda maszyna na świecie może próbować nawiązać połączenie z węzłem, pod warunkiem, że zna Tor Address. Jednak hasło i 2FA nadal będą cię chronić.



Jeśli aktywujesz tę opcję, upewnij się, że masz włączone uwierzytelnianie dwuskładnikowe (2FA), silne hasło i nigdy nie ujawniaj swojego połączenia Tor Address.



Wystarczy wpisać ten Tor Address w przeglądarce Tor, aby uzyskać dostęp do Interface Umbrel z dowolnej sieci.



![Image](assets/fr/026.webp)



Wreszcie, na tej stronie ustawień można również aktywować połączenie Wi-Fi. Jeśli urządzenie hostujące Umbrel ma kartę sieciową Wi-Fi lub klucz Wi-Fi, umożliwia to dostęp do Internetu bez użycia kabla RJ45. Jednak w zależności od konfiguracji, rozwiązanie to może spowolnić połączenie, co może wpłynąć na początkową synchronizację (IBD) i przyszłe wykorzystanie węzła (np. do transakcji Lightning). Osobiście nie polecam tej opcji, ponieważ węzeł nie jest przeznaczony do użytku mobilnego: zawsze jest dostępny zdalnie, więc równie dobrze można pozostawić go podłączonego.



### Krok 6: Zainstalowanie węzła Bitcoin na Umbrel



Teraz, gdy UmbrelOS jest poprawnie zainstalowany i skonfigurowany na twoim komputerze, możesz przystąpić do instalacji węzła Bitcoin. Nic prostszego: przejdź do App Store, otwórz kategorię "*Bitcoin*", a następnie wybierz aplikację "*Bitcoin Node*" (w rzeczywistości jest to Bitcoin core).



![Image](assets/fr/022.webp)



Następnie kliknij przycisk "*Install*".



![Image](assets/fr/023.webp)



Po zakończeniu instalacji węzeł Bitcoin uruchomi IBD (*Initial Block Download*): pobierze i zweryfikuje wszystkie transakcje i bloki od momentu utworzenia Bitcoin w 2009 roku.



![Image](assets/fr/024.webp)



Ten etap jest szczególnie czasochłonny, ponieważ jego czas trwania zależy od kilku czynników, w tym ilości pamięci RAM przydzielonej do pamięci podręcznej węzła, szybkości dysku, szybkości połączenia internetowego i mocy procesora. Zakres czasu trwania jest zatem bardzo szeroki, w zależności od konfiguracji. W przypadku wydajnego komputera (dysk SSD NVMe, +32 GB pamięci RAM, mocny procesor i dobre połączenie internetowe), IBD można ukończyć w około dziesięć godzin. Z drugiej strony, stary procesor, mało pamięci RAM lub, co gorsza, mechaniczny dysk Hard (zdecydowanie odradzany) może wydłużyć tę operację do kilku tygodni.



W przypadku komputera o normalnej konfiguracji (przyzwoity procesor, od 8 do 16 GB pamięci RAM i dysk SSD) pozwala to na około 2 do 7 dni.



Aby nieco przyspieszyć IBD, można zwiększyć pamięć RAM przydzieloną do pamięci podręcznej węzła (używanej głównie dla zestawu UTXO, do którego wrócimy w dalszej części kursu) za pomocą parametru `dbcache`. W Umbrel ta modyfikacja jest dokonywana w parametrach węzła, w zakładce "*Optimization*".



![Image](assets/fr/025.webp)



Domyślnie wartość parametru `dbcache` w Bitcoin core jest ustawiona na 450 MiB, czyli około 472 MB. Zwiększając tę wartość, można nieco przyspieszyć IBD. Jednak niekoniecznie zalecałbym przesuwanie tego parametru zbyt wysoko: nawet ustawienie go na 4 GiB przyspieszy synchronizację tylko o około 10% i może spowodować utratę czasu w przypadku przerwy podczas IBD.



Należy uważać, aby nie przydzielić wartości, która jest zbyt duża dla komputera. Jeśli pamięć RAM dostępna dla UmbrelOS wyczerpie się, węzeł może zostać nagle zatrzymany, przerywając IBD i wymagając ręcznego ponownego uruchomienia, co spowoduje znaczną stratę czasu.



Aby dowiedzieć się więcej o wpływie parametru `dbcache` na początkową synchronizację, polecam tę analizę Jamesona Loppa: [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Po zakończeniu IBD węzła (100% synchronizacji), masz teraz w pełni operacyjny węzeł Bitcoin. Gratulacje, jesteś teraz integralną częścią sieci Bitcoin!



![Image](assets/fr/027.webp)



W następnej części zbadamy praktyczne wykorzystanie nowego węzła: jak podłączyć do niego Wallet i jakie aplikacje należy zainstalować, aby stać się suwerennym Bitcoinerem.





# Podłączanie Wallet do węzła


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indeksatory: rola, działanie i rozwiązania


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Jeśli poznałeś już węzły Bitcoin przed wzięciem udziału w tym kursie, być może spotkałeś się z terminem "indeksator". Są to narzędzia takie jak Electrs lub Fulcrum, które można dodać do węzła Bitcoin core. Ale jaka dokładnie jest ich rola? Jak działają w praktyce? I czy powinieneś zainstalować jeden z nich na swoim nowym węźle Bitcoin? To właśnie zamierzamy zbadać w tym rozdziale.



### Co to jest indeksator?



Ogólnie rzecz biorąc, indeksator to program, który skanuje zestaw nieprzetworzonych danych, wyodrębnia odpowiednie klucze (takie jak słowa, identyfikatory i adresy) i tworzy plik pomocniczy, zwany "indeksem", w którym każdy klucz odnosi się do dokładnej lokalizacji danych w korpusie. Ta faza wstępnego przetwarzania wykorzystuje czas procesora i wymaga trochę miejsca na dysku, ale eliminuje potrzebę przetwarzania całego korpusu za każdym razem, gdy baza danych jest odpytywana; po prostu przesłuchanie indeksu daje niemal natychmiastową odpowiedź.



Mówiąc prościej, jest to ta sama zasada, co indeks w książce: jeśli szukasz konkretnej informacji, zamiast ponownie czytać całą książkę, sprawdzasz indeks, aby bezpośrednio znaleźć stronę, na której pojawia się poszukiwana informacja.



W węźle Bitcoin, takim jak Bitcoin core, dane Blockchain są przechowywane w surowej, chronologicznej formie. Każdy blok zawiera transakcje, które z kolei zawierają wejścia i wyjścia, bez żadnej szczególnej klasyfikacji według Address, identyfikatora lub Wallet. Ta liniowa organizacja jest zoptymalizowana pod kątem walidacji bloków, ale nie nadaje się do ukierunkowanego wyszukiwania. Na przykład, jeśli chcesz znaleźć wszystkie transakcje powiązane z określonym Address w nieindeksowanym węźle, musisz ręcznie przejrzeć cały Blockchain, blok po bloku i transakcja po transakcji. Właśnie w tym miejscu pojawia się indeksator w węźle Bitcoin.



![Image](assets/fr/085.webp)



Indeksator to wyspecjalizowany program, który analizuje masę nieprzetworzonych danych (zestaw Blockchain, Mempool, UTXO) i wyodrębnia klucze, takie jak identyfikatory transakcji, adresy i wysokości bloków. Na podstawie tych kluczy buduje indeks, kojarząc każdy klucz z dokładną lokalizacją informacji w pamięci węzła.



![Image](assets/fr/086.webp)



Indeksowanie umożliwia szybkie, dokładne i wydajne wyszukiwanie informacji w węźle. Na przykład, po podłączeniu Wallet lub Sparrow do węzła, może on niemal natychmiast wyświetlić saldo Address. Mówiąc konkretnie, wysyła zapytanie do indeksatora z żądaniem takim jak: "_Which UTXOs are associated with this script-Hash?_" Indeksator odpowiada niemal natychmiast, bez konieczności ponownego odczytywania całego Blockchain, ponieważ dane te są już wymienione w jego bazie danych.



### Czy Bitcoin core posiada indeksator?



Bez potrzeby dodatkowego oprogramowania, Bitcoin core nie oferuje, ściśle mówiąc, kompletnego indeksatora Address porównywalnego do tych, które można znaleźć w oprogramowaniu takim jak Electrs lub Fulcrum. Niemniej jednak, zawiera on kilka wewnętrznych mechanizmów indeksowania, jak również opcjonalne opcje rozszerzające jego możliwości zapytań. Aby w pełni zrozumieć tę sytuację, musimy zagłębić się w historię projektu.



Do wersji 0.8.0 Bitcoin core, walidacja transakcji była oparta na globalnym indeksie transakcji, znanym jako `txindex`. Indeks ten odnosił się do wszystkich transakcji Blockchain i ich wyników. Gdy węzeł otrzymywał nową transakcję, sprawdzał ten indeks, aby zweryfikować, czy zużyte wyjścia (w wejściach) faktycznie istnieją i nie zostały już wydane. `txindex` był zatem niezbędny do walidacji transakcji w tamtym czasie.



Podejście to miało jednak swoje ograniczenia: było powolne, kosztowne pod względem przechowywania i nadmiarowe pod względem informacji. Aby temu zaradzić, wersja 0.8.0 wprowadza przegląd modelu walidacji o nazwie ***Ultraprune***. Zamiast przechowywać wszystko w formie indeksów transakcji, Bitcoin core utrzymuje prostą bazę danych dedykowaną wyłącznie UTXO, zwaną `chainstate` (w języku potocznym jest to znane jako "UTXO set") i aktualizuje swoją listę w miarę zużywania i tworzenia wyjść.



Ta metoda jest znacznie szybsza i przechowuje tylko aktualny stan rejestru, czyniąc indeksator `txindex` niepotrzebnym. Zamiast jednak usuwać kod `txindex`, deweloperzy zdecydowali się zachować tę funkcjonalność za prostym parametrem (`txindex=1`). Włączając tę opcję na swoim węźle, możesz zapytać o dowolną transakcję z jego `txid`.



Wbrew powszechnemu przekonaniu, Bitcoin core nie oferuje indeksowania opartego na Address, jak Electrs czy Fulcrum. Istnieje kilka powodów takiego wyboru:





- Rolą Bitcoin core nie jest stanie się kompletnym Block explorer, ani zapewnienie API dostosowanego do każdego zastosowania. Integracja indeksu opartego na Address oznaczałaby długoterminową konserwację Commitment, która wykracza poza początkowy zakres oprogramowania.





- Większość przypadków użycia może być już pokryta w inny sposób. Na przykład, aby oszacować saldo Address, można użyć polecenia `scantxoutset`, które bezpośrednio odpytuje zestaw UTXO bez konieczności posiadania pełnego indeksu.





- Każdy program ma określone wymagania dotyczące formatu lub typu danych, które mają być indeksowane (Address, skrypt Hash, własny znacznik itp.). Bardziej elastyczne i logiczne jest umożliwienie tym programom tworzenia własnych, dostosowanych indeksów niż ustalanie ogólnego rozwiązania w Bitcoin core.



Bitcoin core posiada opcjonalny indeksator transakcji (`txindex`), będący pozostałością po jego historycznym działaniu, ale nie zapewnia on indeksu Address, ani bezpośredniego Interface dla złożonych wyszukiwań. Dlatego w niektórych przypadkach może być przydatne dodanie zewnętrznego indeksatora.



### Czy należy dodać indeksator Address do węzła?



Dodanie indeksatora Address, takiego jak Electrs lub Fulcrum, nie jest obowiązkowe; zależy to od konkretnych potrzeb.



Jeśli chcesz po prostu podłączyć Wallet, taki jak Sparrow, do swojego węzła, aby przeglądać salda i nadawać transakcje, jest to całkowicie możliwe bezpośrednio przez Bitcoin core Interface RPC, lokalnie lub zdalnie przez Tor.



Z drugiej strony, aby korzystać z bardziej zaawansowanego oprogramowania, takiego jak uruchomienie Mempool.lokalnie, instalacja indeksera Address staje się niezbędna dla przestrzeni Block explorer.



Indekser wymaga pewnej ilości czasu synchronizacji (mniej niż IBD) i będzie zajmował dodatkowe miejsce na dysku. Jeśli po pobraniu Blockchain na dysku SSD nadal jest wystarczająco dużo wolnego miejsca, można łatwo dodać indeksator.



### Który indeksator wybrać?



Dwa programy są powszechnie używane do tworzenia tego typu indeksu Address i udostępniania go: **Electrs** i **Fulcrum**. Narzędzia te indeksują Blockchain zgodnie ze skryptem Hash (adresy), a następnie proponują ustandaryzowany Interface (protokół Electrum), z którym łączą się liczne portfele, takie jak Electrum Wallet, Sparrow lub Phoenix.



![Image](assets/fr/087.webp)



Mówiąc prościej, Electrs jest dość kompaktowy: indeksuje Blockchain szybciej i zajmuje mniej miejsca na dysku, ale działa nieco gorzej niż Fulcrum w zapytaniach. Z kolei Fulcrum zużywa więcej miejsca na dysku i dłużej indeksuje, ale oferuje lepszą wydajność zapytań.



Do użytku indywidualnego polecam Electrs: zajmuje mniej miejsca, jest dobrze utrzymany i chociaż jest nieco wolniejszy w niektórych żądaniach niż Fulcrum, nadal jest więcej niż wystarczający do codziennego użytku. Jeśli masz czas i miejsce na dysku, możesz również wypróbować Fulcrum, który będzie działał znacznie lepiej, szczególnie w przypadku portfeli z wieloma adresami do weryfikacji.



Mówiąc konkretnie, w sierpniu 2025 r. Electrs będzie potrzebował około 56 GB pamięci masowej, w porównaniu do około 178 GB w przypadku Fulcrum. Wybór indeksatora zależy zatem również od pojemności pamięci masowej:




- Jeśli ilość miejsca na dysku jest bardzo ograniczona, będziesz musiał zadowolić się Bitcoin core bez zewnętrznego indeksera Address.
- Jeśli chcesz korzystać z indeksatora, ale nadal jesteś ograniczony pojemnością, wybierz Electrs.
- Jeśli dysponujesz odpowiednią ilością miejsca na dysku, Fulcrum może być właśnie tym, czego szukasz.



W pozostałej części tego kursu BTC 202 będę używał Electrs, ale możesz z łatwością podążać za Fulcrum: procedura instalacji jest identyczna, podobnie jak połączenie Interface z Wallet, ponieważ oba udostępniają serwer Electrum.



### Jak zainstalować indeksator na Umbrel?



Aby zainstalować Electrs (lub Fulcrum) na swoim Umbrelu, procedura jest prosta: przejdź do App Store, wyszukaj odpowiednią aplikację (znajdującą się w zakładce Bitcoin), a następnie kliknij przycisk "*Install*".



![Image](assets/fr/028.webp)



Po zakończeniu instalacji Electrs przejdzie do fazy synchronizacji (indeksowania), która może potrwać kilka godzin.



![Image](assets/fr/029.webp)



Po zakończeniu synchronizacji można połączyć oprogramowanie Wallet z serwerem Electrum, który jest hostowany na Umbrel.



## Jak podłączyć Wallet do węzła Bitcoin?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Teraz, gdy masz już kompletny węzeł Bitcoin, nadszedł czas, aby go dobrze wykorzystać! W następnym rozdziale zbadamy inne potencjalne zastosowania instancji Umbrel. Zacznijmy jednak od podstaw: podłączenia oprogramowania Wallet w celu wykorzystania informacji z własnego Blockchain i dystrybucji transakcji za pośrednictwem własnego węzła.



Jak wspomniano powyżej, istnieją dwa główne interfejsy połączeń:




- Bezpośrednie połączenie z Bitcoin core przez RPC;
- Lub połączyć się z serwerem Electrum (Electrs lub Fulcrum).



W tym samouczku skoncentrujemy się na łączeniu się z węzłem za pośrednictwem sieci Tor, ponieważ jest to zarówno proste, jak i bezpieczne rozwiązanie dla początkujących. Zdecydowanie odradzam wystawianie portu RPC węzła na światło dzienne, ponieważ błędna konfiguracja stanowi poważne zagrożenie dla bezpieczeństwa i poufności danych. Główną wadą komunikacji za pośrednictwem sieci Tor jest jej powolność. W następnym rozdziale zbadamy szybką i bezpieczną alternatywę dla Tora do zdalnego dostępu do węzła: VPN.



W tym rozdziale użyjemy Sparrow jako przykładu, ale procedura jest taka sama dla wszystkich innych programów zarządzających Wallet akceptujących połączenia z serwerami Electrum. Wystarczy znaleźć odpowiednie ustawienie w parametrach aplikacji (zwykle w "*Server*", "*Network*", "*Node*"...).



W Sparrow otwórz zakładkę "*Plik*" i przejdź do menu "Ustawienia".



![Image](assets/fr/030.webp)



Następnie kliknij "*Server*", aby uzyskać dostęp do parametrów połączenia.



![Image](assets/fr/031.webp)



Następnie odkryjesz trzy opcje łączenia oprogramowania z węzłem Bitcoin:




- Serwer publiczny* (żółty): domyślnie, jeśli nie posiadasz węzła Bitcoin, ta opcja łączy cię z węzłem publicznym, którego nie posiadasz (zwykle firmy). Ta opcja nie jest tutaj istotna, ponieważ masz własny węzeł na Umbrel.
- Bitcoin core* (Green): ta opcja odpowiada połączeniu przez Interface RPC, tj. bezpośrednio z Bitcoin core.
- Private Electrum* (niebieski): ta opcja umożliwia połączenie za pośrednictwem serwera Electrum Interface indeksera (Electrs lub Fulcrum).



### Połączenie z Bitcoin core RPC



Jeśli węzeł Umbrel nie ma indeksatora, jest to opcja, którą należy wybrać. W Sparrow kliknij na "*Bitcoin core*".



![Image](assets/fr/032.webp)



Następnie należy wprowadzić kilka informacji, aby ustanowić połączenie z węzłem. Dostęp do wszystkich tych danych można uzyskać z aplikacji "*Bitcoin Node*" na Umbrel, klikając przycisk "*Connect*" w prawym górnym rogu Interface.



![Image](assets/fr/033.webp)



Zakładka "*RPC Details*" wyświetla wszystkie informacje niezbędne do połączenia. Wybierz połączenie przez Tor Address (w `.onion`).



![Image](assets/fr/034.webp)



Wprowadź te dane w odpowiednich polach na Sparrow wallet, a następnie kliknij przycisk "*Testuj połączenie*".



![Image](assets/fr/035.webp)



Jeśli połączenie się powiedzie, pojawi się symbol zaznaczenia Green i komunikat potwierdzający.



![Image](assets/fr/036.webp)



Znacznik w prawym dolnym rogu Interface Sparrow wallet będzie teraz Green (wskazując bezpośrednie połączenie z Bitcoin core).



**Uwaga:** Aby połączenie się powiodło, węzeł musi być w 100% zsynchronizowany. Jeśli tak nie jest, należy poczekać do końca IBD.



### Połączenie z Electrs



Jeśli węzeł ma indeksator, lepiej jest połączyć się z nim, niż korzystać bezpośrednio z Bitcoin core, ponieważ zapytania będą przetwarzane szybciej.



W Sparrow przejdź do zakładki "*Private Electrum*".



![Image](assets/fr/037.webp)



Następnie należy wprowadzić kilka informacji, aby ustanowić połączenie z indeksatorem. Dane te można znaleźć w aplikacji "*Electrs*" (lub, w stosownych przypadkach, "*Fulcrum*") na Umbrel.



Wybierz zakładkę "*Tor*", aby uzyskać połączenie `.onion` Address. Jeśli chcesz podłączyć mobilne oprogramowanie Wallet, możesz również bezpośrednio zeskanować kod QR.



![Image](assets/fr/038.webp)



Wystarczy wpisać adres Tor Address serwera Electrum w polu "*URL*", a następnie kliknąć przycisk "*Testuj połączenie*".



![Image](assets/fr/039.webp)



Jeśli połączenie się powiedzie, zostanie wyświetlony znacznik wyboru i komunikat potwierdzający.



![Image](assets/fr/040.webp)



Zaznaczenie w prawym dolnym rogu Interface Sparrow wallet zmieni kolor na niebieski (kolor związany z połączeniem z serwerem Electrum).



**Uwaga:** Aby połączenie działało, indeksator musi być w 100% zsynchronizowany. Jeśli tak nie jest, należy poczekać na zakończenie procesu indeksowania.



Teraz już wiesz, jak podłączyć Wallet do węzła Bitcoin! W następnym rozdziale przedstawię kilka dodatkowych aplikacji dostępnych na Umbrel, które szczególnie lubię i które pozwolą ci usprawnić codzienne korzystanie z Bitcoin za pośrednictwem węzła.




## Przegląd dostępnych aplikacji


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel oferuje obszerny sklep z aplikacjami. Jak można się przekonać, znajduje się w nim wiele narzędzi związanych z Bitcoin, ale także szeroka gama aplikacji z bardzo różnych dziedzin: rozwiązania do samodzielnego hostowania usług i plików, aplikacje zwiększające produktywność, bardziej ogólne narzędzia finansowe, zarządzanie mediami, bezpieczeństwo sieci i administracja, rozwój, sztuczna inteligencja, sieci społecznościowe, a nawet automatyka domowa.



W tym kursie BTC 202 skupimy się wyłącznie na aplikacjach związanych z Bitcoin. Zachęcamy jednak do zapoznania się z resztą katalogu w poszukiwaniu narzędzi, które mogą być przydatne.



Oczywiście nie sposób wymienić tutaj wszystkich zastosowań Bitcoin. W tym rozdziale chciałbym przedstawić podstawowe narzędzia, które ułatwią i wzbogacą codzienne korzystanie z Bitcoin.



### Mempool.space



W codziennym użytkowaniu Bitcoin, jeśli istnieje jedno narzędzie, które jest naprawdę niezbędne, to jest nim Block explorer. Niezależnie od tego, czy jest dostępny online, czy zainstalowany lokalnie, przekształca surowe dane Blockchain w uporządkowany, przejrzysty i łatwy do odczytania format. Posiada również wyszukiwarkę, która pozwala użytkownikom szybko zlokalizować określony blok, transakcję lub Address.



Mówiąc konkretnie, eksplorator pozwala oszacować opłaty wymagane do uwzględnienia transakcji w bloku, a następnie śledzić jej postępy: dowiedzieć się, czy jest prawdopodobne, że zostanie ona uwzględniona w najbliższej przyszłości, w zależności od rynku opłat, a na koniec potwierdzić, że rzeczywiście została ona uwzględniona w bloku. Oferuje również możliwość analizowania wcześniejszych transakcji i sprawdzania ich historii. Krótko mówiąc, jest to szwajcarski scyzoryk bitcoinera.



Jak wspomniano wcześniej, eksplorator może być hostowany online na stronie internetowej lub uruchamiany lokalnie na komputerze. Główną wadą usług online jest to, że mogą one naruszać prywatność użytkownika. Bez VPN lub Tor serwer hostujący eksplorator może połączyć twój adres IP Address z przeglądanymi transakcjami, co może stanowić idealny punkt wejścia do analizy łańcucha.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Co więcej, Twój dostawca usług internetowych (ISP) może wiedzieć, że przeglądasz konkretną transakcję za pośrednictwem strony Block explorer. Wiąże się to również z kwestią zaufania: musisz polegać na usłudze online, aby zapewnić sobie dokładne informacje o swoich transakcjach, bez możliwości samodzielnego zweryfikowania ich prawdziwości.



Dlatego zawsze najlepiej jest korzystać z własnego lokalnego Block explorer. W ten sposób żadne dane związane z aktywnością wyszukiwania nie wyciekną, ponieważ wszystkie zapytania są przetwarzane bezpośrednio na maszynie, którą kontrolujesz, bez przechodzenia przez Internet. Co więcej, lokalny eksplorator opiera się na danych z własnego węzła Bitcoin, które zostały zweryfikowane przez użytkownika zgodnie z jego własnymi zasadami i którym można zaufać.



Umbrel oferuje kilka eksploratorów bloków:




- Mempool.Space
- Bitfeed
- BTC RPC Explorer



Szczególnie podoba mi się Mempool.Space, który zainstalowałem na moim węźle. Uwaga: aby korzystać z większości eksploratorów bloków na Umbrel, wymagany jest indeksator Address. Potrzebna jest zatem aplikacja Bitcoin Node (lub Bitcoin Knots), która ma w 100% zsynchronizowany Blockchain, a także indeksator, taki jak Electrs lub Fulcrum, który jest również w 100% zsynchronizowany.



Po zainstalowaniu aplikacji wystarczy ją otworzyć, aby uzyskać dostęp do własnego eksploratora.



![Image](assets/fr/041.webp)



Aby dowiedzieć się więcej na temat korzystania z eksploratora Mempool.Space, polecam ten obszerny samouczek:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Węzeł Lightning



Teraz, gdy masz własny węzeł Bitcoin, możesz również skonfigurować własny węzeł Lightning do przeprowadzania transakcji off-chain, bez polegania na infrastrukturze strony trzeciej.



Umbrel oferuje szereg aplikacji, które pomagają w uruchomieniu węzła Lightning. Do wyboru są dwie główne implementacje:




- LND, za pośrednictwem aplikacji *Lightning Node*;
- Core Lightning.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Następnie można zarządzać węzłem z poziomu głównego Interface lub, w celu uzyskania jeszcze większej funkcjonalności i zaawansowanych opcji, zainstalować *Ride The Lightning* lub *ThunderHub*. Narzędzia te zapewniają znacznie bardziej wszechstronny internetowy system zarządzania Interface dla węzła.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Na koniec polecam aplikację *Lightning Network+*, która pozwala znaleźć partnerów, z którymi można otworzyć kanały, umożliwiając zarówno wychodzące, jak i przychodzące transakcje gotówkowe.



![Image](assets/fr/089.webp)



Dzięki Umbrel zarządzanie osobistym węzłem Lightning zostało znacznie uproszczone, ale nadal jest stosunkowo złożone. Z tego powodu przyjrzymy się bliżej temu tematowi w przyszłym kursie poświęconym w całości temu zastosowaniu.



### Skala ogonowa



Inną aplikacją, którą szczególnie lubię w Umbrel, jest Tailscale. Jest to aplikacja VPN zaprojektowana w celu uproszczenia tworzenia bezpiecznych sieci między wieloma urządzeniami, niezależnie od tego, gdzie się znajdują. W przeciwieństwie do tradycyjnych sieci VPN, które opierają się na scentralizowanych serwerach, Tailscale wykorzystuje protokół WireGuard do ustanawiania szyfrowanych połączeń typu end-to-end między różnymi urządzeniami. Oznacza to, że można wdrożyć działającą sieć VPN w ciągu zaledwie kilku minut, bez konieczności skomplikowanej konfiguracji sieci.



W Umbrel instalacja Tailscale łączy węzeł Bitcoin z własną wirtualną siecią prywatną. Po skonfigurowaniu węzeł uzyskuje prywatny adres IP Tailscale Address, dostępny tylko z innych urządzeń podłączonych do tej samej sieci Tailscale (takich jak komputery, smartfony i tablety). To połączenie jest szyfrowane od końca do końca i nie przechodzi przez niezabezpieczoną sieć publiczną, co znacznie zwiększa bezpieczeństwo w porównaniu z nieszyfrowanym połączeniem.



![Image](assets/fr/090.webp)



Mówiąc konkretnie, Tailscale oferuje kilka korzyści podczas korzystania z Umbrel:





- Możesz administrować Interface Umbrel lub uzyskać dostęp do aplikacji połączonych z węzłem (takich jak Mempool, Ride The Lightning, ThunderHub...) z dowolnego miejsca, tak jakbyś był w tej samej sieci lokalnej, bez ujawniania portów w Internecie i bez przechodzenia przez Tor, który jest bardzo powolny;





- Możesz połączyć się z serwerem Electrum (Electrs lub Fulcrum) lub bezpośrednio z Bitcoin core przez VPN, omijając Tor. Zapewnia to bezpieczne połączenie, porównywalne do korzystania z Tora, ale ze znacznie większą prędkością i mniejszymi opóźnieniami. Krótko mówiąc, zachowujesz prywatność i bezpieczeństwo Tor, jednocześnie ciesząc się szybkością połączenia Clearnet. W przypadku On-Chain Wallet zysk ten może wydawać się marginalny, ale jeśli planujesz skonfigurować własny węzeł Lightning w późniejszym terminie, różnica jest znacząca. Rzeczywiście, dokonywanie płatności za pośrednictwem węzła w ruchu na Torze jest niezwykle powolne ze względu na liczne wymagane wymiany, podczas gdy w Tailscale działa to doskonale.





- Nie ma potrzeby konfigurowania reguł NAT, otwierania portów ani konfigurowania konwencjonalnego serwera VPN. Po zainstalowaniu aplikacji na Umbrel i urządzeniach, sieć jest tworzona automatycznie.



Tailscale na Umbrel jest zatem bardzo interesującym rozwiązaniem, jeśli chcesz uzyskać dostęp do swojego węzła z dowolnego miejsca na świecie w bezpieczny, wydajny i łatwy w konfiguracji sposób, bez poświęcania prywatności lub bezpieczeństwa.



Aby zainstalować i skonfigurować Tailscale na Umbrel, zapoznaj się z tym samouczkiem, sekcja 4: "*Używanie Tailscale na Umbrel*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, skrót od "*Notes and Other Stuff Transmitted by Relays*", jest otwartym, zdecentralizowanym protokołem zaprojektowanym w celu umożliwienia publikowania i wymiany wiadomości w Internecie bez zależności od scentralizowanej platformy. Każdy użytkownik posiada parę kluczy kryptograficznych: klucz publiczny (`npub`), który służy jako identyfikator, oraz klucz prywatny (`nsec`), który służy do podpisywania wiadomości i gwarantowania ich autentyczności.



Wiadomości są przesyłane za pośrednictwem sieci niezależnych przekaźników. Ta rozproszona architektura sprawia, że Nostr jest odporny na cenzurę: żaden pojedynczy serwer nie kontroluje dostępu ani dystrybucji, a użytkownik może połączyć się z dowolną liczbą przekaźników.



Protokół ten jest bardzo popularny w społeczności Bitcoin, ponieważ podobnie jak Bitcoin, Nostr zajmuje się kwestiami suwerenności cyfrowej i kontroli danych. Jego twórca, Fiatjaf, jest deweloperem już uznanym w ekosystemie za swój liczny wkład.



Dzięki Umbrel możesz zoptymalizować korzystanie z Nostr. Instalując aplikację ***Nostr Relay***, możesz hostować swój prywatny przekaźnik bezpośrednio na swoim komputerze, zapewniając, że wszystkie twoje posty i interakcje na Nostr są zapisywane lokalnie i nie mogą zostać utracone przez usunięcie przez publiczne przekaźniki.



Klienci Nostr ***noStrudel*** lub ***Snort*** są również dostępni na Umbrel. Dzięki tym aplikacjom można publikować, czytać, wyszukiwać profile i wchodzić w interakcje z ekosystemem Nostr bezpośrednio z sieci Interface na Umbrel.



Wreszcie, istnieje aplikacja ***Nostr Wallet Connect*** na Umbrel, która umożliwia natywne płatności Lightning w Nostr. Mówiąc konkretnie, możesz połączyć swój przyszły węzeł Lightning z klientami Nostr, aby wysyłać mikropłatności, zwane "*zaps*", w celu nagradzania treści lub interakcji w sposób monetyzowany, bez konieczności korzystania z usługi strony trzeciej. Płatności te są wysyłane bezpośrednio z węzła osobistego za pośrednictwem kanałów użytkownika.



Aby dowiedzieć się, jak korzystać ze wszystkich tych aplikacji, polecam zapoznać się z tym kompletnym samouczkiem:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### Serwer BTCPay



BTCPay Server to darmowy procesor płatności typu open-source, który umożliwia przyjmowanie płatności za pośrednictwem Bitcoin i Lightning Network bez pośredników, przy jednoczesnym zachowaniu własnego przechowywania środków.



Architektura BTCPay Server opiera się na węźle Bitcoin, a w przypadku Lightning na kompatybilnej implementacji (LND, Core Lightning...), co czyni go jednym z niewielu całkowicie bezobsługowych rozwiązań PoS. Jest to również najbardziej wszechstronne oprogramowanie do śledzenia i księgowania.



![Image](assets/fr/091.webp)



Jeśli jesteś właścicielem firmy i chciałbyś akceptować płatności Bitcoin bezpośrednio za pośrednictwem węzła Umbrel, aplikacja BTCPay Server jest dla Ciebie idealna. Aby dowiedzieć się więcej na ten temat, polecam zapoznać się z następującymi zasobami:





- Kurs BIZ 101 na temat korzystania z Bitcoin w swojej firmie:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- Kurs POS 305 dotyczący korzystania z serwera BTCPay:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- Samouczek dotyczący serwera BTCPay:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Zaawansowane koncepcje i najlepsze praktyki


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Konserwacja węzła Umbrel


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Aby rozpocząć tę ostatnią sekcję i przed przejściem do bardziej zaawansowanej teorii, chciałbym przeanalizować najlepsze praktyki i konkretne działania, które można podjąć po zainstalowaniu, zsynchronizowaniu i prawidłowym skonfigurowaniu węzła Umbrel w tym krótkim rozdziale. Jak utrzymywać go na co dzień?



### Utrzymanie sprzętu w dobrym stanie



Niezawodny węzeł zaczyna się od stabilnego sprzętu. Upewnij się, że urządzenie, w którym znajduje się węzeł, jest odpowiednio wentylowane, wolne od Dust i zainstalowane w suchym środowisku, z dala od źródeł ciepła i wilgoci. Unikaj upychania go w ograniczonej przestrzeni i wybierz dobrze wentylowaną lokalizację.



W przypadku Raspberry Pi i mini-PC, Dust ostatecznie zatyka radiatory, podnosząc temperaturę i prowadząc do throttlingu (dobrowolnego ograniczenia wykorzystania zasobów), co z kolei skutkuje spadkiem wydajności węzła. Dlatego zalecam okresowe czyszczenie wlotu powietrza i wentylatora, najlepiej co kilka miesięcy.



Upewnij się, że używasz wysokiej jakości zasilacza Supply, ponieważ niestabilne napięcie może prowadzić do uszkodzenia systemu, a nawet stanowić zagrożenie pożarowe. Najlepiej używać oryginalnego zasilacza Supply dostarczonego przez producenta urządzenia. Należy również uważać na przegrzanie spowodowane efektem Joule'a na listwach zasilających: zawsze należy przestrzegać maksymalnej dopuszczalnej mocy i nigdy nie podłączać kilku listew zasilających kaskadowo.



Zalecam również zainwestowanie w zasilacz UPS. Chroni to węzeł przed nagłymi wyłączeniami, umożliwia czyste wyłączenie Umbrel w przypadku awarii i zapewnia ciągłość działania podczas mikroprzerw lub krótkotrwałych awarii.



Po stronie pamięci masowej należy śledzić postępy: jeśli dysk zbliża się do nasycenia, należy rozważyć zwolnienie miejsca (odinstalowanie nieużywanych aplikacji, dostosowanie ustawień indeksera) lub migrację na większy dysk SSD. Wadą pełnego węzła Bitcoin jest to, że jego wymagania dotyczące pamięci masowej stale rosną, ponieważ nowy blok jest generowany co 10 minut, a starych bloków nie można usunąć (chyba że węzeł to pruned). Dlatego radzę zaplanować wystarczająco dużą pojemność przy zakupie sprzętu (minimum 2 TB).



### Aktualizacja



Aktualizacje węzłów są ważne z trzech głównych powodów: po pierwsze, bezpieczeństwo (poprawki luk w zabezpieczeniach, wzmocnienie sieci i ochrona przed atakami DoS); po drugie, kompatybilność (zmiany zasad przekazywania, zmiany formatu i aktualizacje protokołów); i po trzecie, niezawodność i wydajność (poprawki błędów, zużycie zasobów i inne ulepszenia). Należy więc okresowo sprawdzać, czy system UmbrelOS i aplikacje są aktualne:





- Aby zaktualizować system: Otwórz menu ustawień, a następnie kliknij przycisk "*Check for Update*" obok parametru "*UmbrelOS*".



![Image](assets/fr/042.webp)





- Aby zaktualizować aplikacje: Przejdź do App Store. Jeśli którakolwiek z aplikacji wymaga aktualizacji, w prawym górnym rogu Interface pojawi się przycisk z czerwonym dymkiem. Wystarczy go kliknąć, a następnie zaktualizować każdą aplikację.



Wykonuj tę operację regularnie, aby zapewnić aktualność systemu operacyjnego i aplikacji.



### Kopie zapasowe



Jeśli używasz węzła Bitcoin tylko do walidacji i dystrybucji transakcji, ale Twoje portfele są zarządzane poza Umbrel (np. za pomocą Hardware Wallet i Sparrow wallet), nie ma nic do tworzenia kopii zapasowych bezpośrednio w Umbrel. W takim przypadku podstawową kopią zapasową pozostaje fraza odzyskiwania i Descriptor zewnętrznego Wallet, i ma to zastosowanie niezależnie od tego, czy używasz własnego węzła, czy nie. Tak więc nic się nie zmienia w stosunku do poprzedniej konfiguracji.



Z drugiej strony, w zależności od dodatkowych aplikacji używanych na Umbrel, mogą być wymagane dalsze kopie zapasowe. Jest to szczególnie ważne w przypadku korzystania z węzła Lightning na Umbrel. W takim przypadku absolutnie konieczne jest wykonanie kopii zapasowej seed dostarczonego podczas instalacji węzła Lightning. Oprócz seed potrzebna jest aktualna ***Static Channel Backup (SCB)***, aby móc przywrócić węzeł Lightning w przypadku wystąpienia problemu. SCB umożliwia odzyskanie środków poprzez wymuszone zamknięcie kanałów. Brak seed lub SCB uniemożliwia przywrócenie węzła Lightning.



Umbrel oferuje również opcję automatycznego i dynamicznego tworzenia kopii zapasowych tego SCB na swoich serwerach, za pośrednictwem Tora, aby zapewnić, że aktualny plik jest zawsze dostępny. W takim przypadku do przywrócenia węzła potrzebny jest tylko seed.



Powrócimy do tych aspektów szczegółowo w następnym kursie LNP202.



### Codzienne bezpieczeństwo operacyjne



Jeśli chodzi o bezpieczeństwo, używaj długiego, unikalnego i losowego hasła do Interface Umbrel i pamiętaj o włączeniu uwierzytelniania dwuskładnikowego (2FA). W przypadku aplikacji, które oferują zarówno ochronę hasłem, jak i 2FA, zawsze aktywuj oba i zmień domyślne hasła.



Nigdy nie udostępniaj pulpitu nawigacyjnego w Internecie bez korzystania z bezpiecznej bramy (takiej jak VPN, Tor lub tylko dostęp lokalny). Ogranicz liczbę instalowanych aplikacji i regularnie usuwaj te, których już nie potrzebujesz, aby zmniejszyć powierzchnię ataku.



Aby pogłębić swoją ogólną wiedzę na temat bezpieczeństwa komputerowego, gorąco polecam zapoznanie się z tym innym bezpłatnym kursem:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnoza i samopomoc



W przypadku wystąpienia błędu w Umbrel, najpierw generate pakiet diagnostyczny za pośrednictwem sekcji rozwiązywania problemów UmbrelOS lub danej aplikacji, a następnie czysto uruchom ponownie aplikację. Jeśli to konieczne, spróbuj również pełnego restartu systemu.



Jeśli problem nadal występuje, zalecam [dołączenie do społeczności użytkowników Umbrel na ich Discordzie](https://discord.gg/efNtFzqtdx). Zacznij od wyszukania, czy ktoś już napotkał tę samą trudność i znalazł rozwiązanie. Jeśli nie, możesz opublikować wiadomość na kanale `general-support`. Możesz również skorzystać z [forum Umbrel](https://community.umbrel.com/).



Obszary te umożliwiają nie tylko śledzenie ogłoszeń i aktualizacji dotyczących bezpieczeństwa, ale także zadawanie pytań i ostatecznie pomaganie innym użytkownikom. To właśnie w takich wymianach często odkrywane są najlepsze praktyki.



Dzięki tym prostym nawykom węzeł Umbrel pozostanie stabilny, bezpieczny i użyteczny, zarówno dla Ciebie, jak i dla sieci Bitcoin.




## Zrozumienie IBD i procesu wzajemnego odkrywania


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Węzeł Bitcoin uruchamia się bez wcześniejszej wiedzy o historii transakcji. Początkowo jest to tylko komputer z uruchomionym oprogramowaniem (Bitcoin core lub podobnym). Aby stać się w pełni zsynchronizowanym i działającym węzłem Bitcoin, musi on lokalnie zrekonstruować stan Ledger poprzez sprawdzenie wszystkich bloków opublikowanych od bloku Genesis (blok 0, opublikowany przez Satoshi Nakamoto 3 stycznia 2009 r.). Krok ten nazywany jest **IBD (_Initial Block Download_)**.



IBD polega na pobieraniu i weryfikowaniu każdego bloku i transakcji indywidualnie, stosując zasady konsensusu, aby zbudować własną wersję Blockchain. Celem nie jest po prostu pobranie kopii niezweryfikowanych danych, ale dojście do tego samego wniosku całkowicie niezależnie, jak uczciwa większość sieci.



![Image](assets/fr/092.webp)



### Kamienie milowe IBD



Synchronizacja rozpoczyna się od kroku _**headers-first**_. Węzeł żąda sekwencji nagłówków bloków od kilku elementów równorzędnych i dla każdego z nich weryfikuje Proof of Work, dostosowanie trudności, składnię, a także Timestamp i reguły numeru wersji. Krótko mówiąc, upewnia się, że każdy otrzymany nagłówek jest zgodny z regułami konsensusu.



![Image](assets/fr/093.webp)



Dla przypomnienia, blok Bitcoin składa się z 80-bajtowego nagłówka i listy transakcji. Odcisk palca bloku uzyskuje się poprzez zastosowanie podwójnego SHA-256 Hash do tego nagłówka, który zawiera 6 pól:




- wersja
- Hash z poprzedniego bloku
- Merkle Root transakcji
- Timestamp (dłuższy niż mediana czasu poprzednich 11 bloków)
- docelowy poziom trudności
- Nonce



![Image](assets/fr/094.webp)



Transakcje są zapisywane w Merkle Tree. Jest to struktura, która podsumowuje duży zestaw danych (w tym przypadku wszystkie transakcje w bloku), agregując ich skróty stopniowo dwa po dwa do pojedynczego "korzenia", udowadniając w ten sposób, że element należy do zestawu (i wykrywając wszelkie modyfikacje). W ten sposób każda modyfikacja transakcji modyfikuje również korzeń Merkle Tree, a tym samym odcisk palca nagłówka bloku. SegWit wprowadził oddzielny dodatkowy Commitment dla plików cookie (podpisów), umieszczony w bazie monet.



![Image](assets/fr/095.webp)



Ten krok _**headers-first**_ pozwala węzłowi zidentyfikować gałąź z największą ilością pracy (niezależnie od liczby bloków), która jest gałęzią, na której synchronizują się węzły Bitcoin. Po zidentyfikowaniu tej gałęzi węzeł pobiera zawartość bloków równolegle z kilku połączeń, a następnie sprawdza poprawność każdej transakcji: format, ważność skryptów (z wyjątkiem `assumevalid=1`), kwoty i brak podwójnych wydatków. Z każdym pomyślnym sprawdzeniem, aktualny stan niewydanych monet (zestaw UTXO) jest aktualizowany w bazie danych `chainstate/`: zużyte wyjścia są usuwane, podczas gdy nowe ważne wyjścia są dodawane.



Z drugiej strony Mempool wchodzi w grę tylko wtedy, gdy zbliża się do końca łańcucha: tak długo, jak węzeł pozostaje spóźniony, nie ma oczekujących transakcji do przechowywania.



Po zakończeniu IBD węzeł wchodzi w normalną fazę: weryfikuje nowe bloki, gdy są publikowane, utrzymuje Mempool z oczekującymi transakcjami zgodnie z zasadami przekazywania, przekazuje transakcje i bloki oraz zarządza wszelkimi reorganizacjami łańcucha.



### AssumeValid



Bitcoin core zawiera mechanizm zaprojektowany w celu skrócenia czasu potrzebnego do pełnego uruchomienia węzła, przy jednoczesnym zachowaniu istoty zasady autonomicznej weryfikacji: AssumeValid.



Parametr `assumevalid` jest oparty na przeszłym bloku referencyjnym, którego Hash jest zintegrowany z każdą wersją oprogramowania. Podczas IBD, jeśli węzeł stwierdzi, że ten blok rzeczywiście znajduje się w gałęzi z największą ilością pracy, może zignorować weryfikację skryptu dla wszystkich transakcji przed tym punktem.



Wszystkie inne zasady (struktura bloku, Proof of Work, limity rozmiaru, kwoty transakcji, UTXO itp.) pozostają w pełni zweryfikowane. Tylko obliczenia skryptów przed tym blokiem referencyjnym są ignorowane. Wzrost wydajności jest znaczący w IBD, ponieważ weryfikacja podpisu stanowi główną część obciążenia procesora. Poza tym blokiem referencyjnym weryfikacja powraca do normalnego stanu.



Można wymusić pełną walidację wszystkich skryptów poprzez wyłączenie tego mechanizmu, kosztem znacznie dłuższego IBD, używając parametru `assumevalid=0` w pliku `Bitcoin.conf`.



### ZałóżUTXO



`assumeutxo` to kolejny istniejący parametr, ale w przeciwieństwie do `assumevalid`, nie jest on domyślnie aktywowany. Mechanizm ten umożliwia oprogramowaniu załadowanie migawki zestawu UTXO wraz z jego metadanymi i tymczasowe uznanie go za stan odniesienia, po sprawdzeniu, czy nagłówki rzeczywiście prowadzą do Blockchain z największą ilością pracy.



W ten sposób węzeł szybko staje się operacyjny dla typowych zastosowań (RPC, łączenie portfeli itp.), jednocześnie uruchamiając pełną, zweryfikowaną rekonstrukcję własnego zestawu UTXO w tle. Po zakończeniu tego etapu początkowa migawka jest zastępowana lokalnie zrekonstruowanym stanem. Takie podejście oddziela szybkie dostarczanie węzłów od pełnej weryfikacji, bez uszczerbku dla tej ostatniej.



### Wykrywanie urządzeń równorzędnych: W jaki sposób węzeł znajduje sieć Bitcoin?



Gdy węzeł uruchamia się po raz pierwszy, nie zna jeszcze żadnych urządzeń równorzędnych. Musi jednak znaleźć inne węzły Bitcoin w Internecie, aby zażądać nagłówków, a następnie bloków, aby ukończyć IBD. Aby zainicjować te połączenia, Bitcoin core stosuje logikę priorytetową.



![Image](assets/fr/096.webp)



Gdy węzeł uruchamia się ponownie po tym, jak był już używany, Core najpierw próbuje ponownie połączyć się z wychodzącymi peerami zarejestrowanymi przed wyłączeniem, informacje przechowywane w pliku `anchors.dat`. Następnie konsultuje się ze swoją księgą IP Address **`peers.dat`**, która przechowuje listę wcześniej napotkanych peerów, aby ponownie się z nimi połączyć. Jest to po prostu plik lokalny, aktualizowany i przechowywany przez Core. Z drugiej strony, dla nowego węzła, który właśnie został uruchomiony, te 2 pliki są puste, ponieważ nigdy jeszcze nie komunikował się z innymi węzłami Bitcoin.



W tym przypadku oprogramowanie wysyła zapytanie do _**DNS seeds**_. Są to [serwery utrzymywane przez uznanych twórców ekosystemu](https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), które zwracają listę adresów IP przypuszczalnie aktywnych węzłów. Adresy te umożliwiają nowemu węzłowi zainicjowanie pierwszych połączeń i zażądanie niezbędnych danych z IBD. Oto lista *DNS seeds* aktywnych do tej pory (sierpień 2025):




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.`
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: `seed.Mainnet.achownodes.xyz.`



W zdecydowanej większości przypadków krok *DNS seeds* jest wystarczający do nawiązania pierwszych połączeń z innymi węzłami. Jeśli wyjątkowo serwery te nie odpowiedzą w ciągu 60 sekund, węzeł przełącza się na inną metodę: [statyczna lista ponad 1000 adresów](https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) _węzłów nasiennych_ jest wbudowana w kod Bitcoin core i regularnie aktualizowana. Jeśli dwie pierwsze metody uzyskiwania adresów IP zawiodą, to ostatnie rozwiązanie ustanawia początkowe połączenie, z którego węzeł może następnie zażądać nowych adresów IP.



![Image](assets/fr/097.webp)



W ostateczności można ręcznie użyć adresów IP Supply za pośrednictwem pliku `peers.dat`, aby wymusić określone połączenia.



Po uruchomieniu wewnętrzny menedżer Address dywersyfikuje źródła (oddzielne sieci autonomiczne, Clearnet i Tor, a także różne obszary geograficzne), aby zmniejszyć ryzyko izolacji topologicznej. Węzeł ustanawia te połączenia wychodzące (połączenia, które sam wybiera, a zatem są bezpieczniejsze).



Jeśli węzeł nasłuchuje na otwartym porcie (domyślnie 8333), akceptuje połączenia przychodzące. Wzmacniają one ogólną odporność sieci, zapewniając punkt kontaktowy dla nowych węzłów, nie przynosząc żadnych szczególnych korzyści dla własnego IBD. Jeśli węzeł działa na Torze, logika pozostaje taka sama, ale używane adresy to usługi `.onion`.




## Anatomia węzła Bitcoin


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Po zakończeniu początkowej synchronizacji węzeł przechowuje lokalnie kilka uzupełniających się zestawów danych, umożliwiając mu sprawdzanie poprawności bloków i transakcji, obsługę sieci równorzędnych i szybkie ponowne uruchamianie przy zachowaniu swojego stanu. węzeł składa się z 3 głównych elementów:




- gW-402 **bloki** przechowywane na dysku,
- **Zestaw UTXO** przechowywany w bazie danych klucz-wartość,
- a **Mempool** jest przechowywany w pamięci RAM i okresowo serializowany.



Dodatkowo, kilka plików pomocniczych (rówieśnicy, szacunki opłat, listy wykluczeń, portfele itp.) uzupełniają obraz. Odkryjmy rolę wszystkich tych plików.



### Gdzie faktycznie znajdują się dane węzła?



Domyślnie Bitcoin core zapisuje swoje dane w określonym katalogu roboczym. Pod GNU/Linux jest to zazwyczaj `~/.Bitcoin/`, pod Windows w `%APPDATA%\Bitcoin/`, a pod macOS w `~/Library/Application Support/Bitcoin/`. Jeśli używasz spakowanego rozwiązania (np. w ramach dystrybucji węzła), katalog ten może być zamontowany w innym miejscu, ale jego struktura pozostaje taka sama. Ważne podfoldery i pliki opisane poniżej nadal znajdują się tutaj.



![Image](assets/fr/098.webp)



### Bloki



Blockchain jest zatem zbiorem bloków. Full node przechowuje te bloki jako sekwencyjne pliki płaskie i utrzymuje indeks równoległy w celu szybkiego wyszukiwania. W razie potrzeby (reorganizacja, ponowne skanowanie Wallet, usługa równorzędna) dane te są ponownie odczytywane w niezmienionej postaci.



**Uwaga:** Reorganizacja lub resynchronizacja to zjawisko, w którym Blockchain ulega modyfikacji swojej struktury z powodu istnienia konkurencyjnych bloków na tej samej wysokości. Dzieje się tak, gdy część Blockchain zostaje zastąpiona innym łańcuchem z większą ilością zgromadzonej pracy. Te resynchronizacje są naturalną częścią działania Bitcoin, gdzie różni górnicy mogą znaleźć nowe bloki niemal jednocześnie, dzieląc w ten sposób sieć Bitcoin na dwie części. W takich przypadkach sieć może tymczasowo podzielić się na konkurujące ze sobą łańcuchy. Ostatecznie, gdy jeden z tych łańcuchów gromadzi więcej pracy, pozostałe łańcuchy są porzucane przez węzły, a ich bloki stają się znane jako "przestarzałe bloki" lub "bloki osierocone" Ten proces zastępowania jednego łańcucha innym nazywany jest resynchronizacją.



#### Pliki Blk*.dat (nieprzetworzone dane blokowe)



Odebrane i zatwierdzone bloki są zapisywane do sekwencyjnych kontenerów o nazwie `blkNNNNN.dat`, przechowywanych w folderze `blocks/`. Każdy plik jest wypełniany sekwencyjnie, aż osiągnie maksymalny rozmiar 128 MB, po czym Core otwiera następny plik. Wewnątrz, każdy blok jest serializowany w formacie sieciowym, poprzedzony magicznym identyfikatorem i długością. Taka organizacja umożliwia szybki zapis na dysk i ułatwia usługę blokową w celu synchronizacji peerów.



![Image](assets/fr/099.webp)



W trybie pruned węzeł zachowuje tylko ostatnie okno tych plików, aby ograniczyć ślad dyskowy. Usuwa najstarsze kontenery `blk*.dat`, gdy tylko zostanie osiągnięty skonfigurowany cel przestrzeni, zachowując wystarczającą historię, aby zachować spójność z najbardziej znanym łańcuchem. Indeks i zestaw UTXO pozostają normalne, umożliwiając walidację kolejnych transakcji i bloków.



#### Pliki Rev*.dat (dane anulowania)



Aby móc cofnąć się w czasie podczas reorganizacji, Core zapisuje, równolegle z każdym plikiem `blk`, plik `revNNNNN.dat` w `blocks/`. Plik ten zawiera informacje potrzebne do cofnięcia wpływu bloku na zestaw UTXO: dla każdego wyjścia zużytego przez blok, przechowywany jest poprzedni stan odpowiedniego UTXO (ilość, skrypt, wysokość...). W przypadku przerwania bloku węzeł może szybko odtworzyć poprzedni stan bez konieczności ponownego skanowania całego łańcucha.



![Image](assets/fr/100.webp)



#### Indeks bloków (bloki/indeks)



Wyszukiwanie bloku bezpośrednio w płaskich plikach byłoby zbyt czasochłonne. Dlatego też Core utrzymuje bazę danych LevelDB w `blocks/index/`, która wymienia, dla każdego znanego bloku, metadane takie jak Hash, wysokość, status walidacji, plik `blk` i offset, w którym się znajduje. Gdy peer żąda bloku lub gdy wewnętrzny komponent musi uzyskać dostęp do określonego bloku, indeks ten zapewnia szybki dostęp. Bez tego indeksu wymagana byłaby zbyt duża liczba operacji.



![Image](assets/fr/101.webp)



#### Opcjonalne indeksy (indexes/)



Niektóre indeksy są opcjonalne i domyślnie wyłączone, ponieważ zwiększają ilość zajmowanego miejsca na dysku:




- `indexes/txindex/`, o którym już wspominaliśmy, zapewnia tabelę mapowania transakcja → lokalizacja, umożliwiając pobranie dowolnej potwierdzonej transakcji bez znajomości bloku, który ją zawiera. Jest to przydatne dla zapytań typu Wallet `getrawtransaction`, ale jest dość kosztowne.
- indexes/blockfilter/`, które mogą zawierać kompaktowe filtry blokowe (BIP157/158) dla cienkich klientów. Struktury te przyspieszają weryfikację po stronie klienta kosztem dodatkowej pamięci na węźle indeksującym.



### Zestaw UTXO (stan łańcucha)



Model UTXO (*Niewydane Transakcje Wyjściowe*) jest księgową reprezentacją Bitcoin: każde niewydane wyjście jest dostępnym "Coin", który może być użyty jako dane wejściowe dla przyszłej transakcji.



![Image](assets/fr/102.webp)



Całość wszystkich tych części w danym momencie T stanowi zestaw UTXO: dużą listę wszystkich dostępnych obecnie części. To właśnie ten stan jest konsultowany przez węzeł, aby zdecydować, czy transakcja wydaje legalne jednostki, które nie zostały już wykorzystane w poprzedniej transakcji (aby uniknąć Double-spending).



![Image](assets/fr/103.webp)



Zestaw UTXO jest przechowywany w folderze `chainstate/` jako kompaktowa baza danych LevelDB. Każda część kojarzy klucz pochodzący z Hash transakcji i indeksu wyjściowego z wartością zawierającą: kwotę, blokadę `scriptPubKey`, wysokość utworzonego bloku i wskaźnik coinbase.



![Image](assets/fr/104.webp)



Węzeł utrzymuje pamięć podręczną powyżej LevelDB, aby absorbować częste operacje odczytu i zapisu. Parametr `dbcache` może być użyty do modyfikacji rozmiaru tej pamięci podręcznej: im jest ona większa, tym więcej dostępu do pamięci korzysta IBD i bieżąca walidacja, kosztem wyższego zużycia pamięci RAM. Gdy nowy blok zostanie znaleziony przez Miner, węzeł usuwa z zestawu UTXO wyjścia wydane (lub zużyte) przez transakcje zawarte w bloku i dodaje nowo utworzone wyjścia.



Teoretycznie moglibyśmy zweryfikować transakcję, ponownie skanując historię bloków, aby sprawdzić, czy dane wyjście nigdy nie zostało wydane. W praktyce byłoby to jednak zbyt czasochłonne, ponieważ cały Blockchain musiałby być skanowany dla każdej nowej transakcji. Zestaw UTXO zapewnia zatem minimalny widok wymagany do udowodnienia lokalnie i w rozsądnym czasie braku Double-spending.



Należy zauważyć, że zestaw UTXO jest często w centrum obaw o decentralizację Bitcoin, ponieważ jego rozmiar naturalnie szybko rośnie. Wynika to częściowo z rosnącej ceny Bitcoin, która zachęca do fragmentacji części, a częściowo z rosnącej popularności systemu: im więcej użytkowników, tym większe zapotrzebowanie na UTXO.



![Image](assets/fr/105.webp)



Wzrost zestawu UTXO wynika również ze struktury prostych transakcji płatniczych na Bitcoin. Rzeczywiście, kiedy dokonujesz płatności, zużywasz pojedynczy UTXO jako dane wejściowe i tworzysz 2 nowe UTXO jako dane wyjściowe (jeden dla płatności, a drugi dla Exchange). Wreszcie, heurystyka analizy łańcucha, zwana CIOH (*Common Input Ownership Heuristic*), stanowi dodatkową zachętę do unikania konsolidacji Coin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Ponieważ jego część musi być przechowywana w pamięci RAM, aby zweryfikować transakcje w rozsądnym czasie, zestaw UTXO może stopniowo uczynić działanie Full node zbyt kosztownym. Aby rozwiązać ten problem, istnieje już kilka propozycji, w szczególności [Utreexo](https://planb.network/resources/glossary/utreexo).



### Mempool



Mempool to lokalny zestaw ważnych transakcji, które zostały odebrane, ale nie zostały jeszcze potwierdzone. Dla przypomnienia, "potwierdzona transakcja" to taka, która została zawarta w ważnym bloku. Każdy węzeł utrzymuje swój własny Mempool, który może różnić się od Mempool innych węzłów w sieci w zależności od:




- rozmiar przydzielony do Mempool za pomocą parametru `maxmempool`: węzeł z większym Mempool będzie w stanie pomieścić więcej transakcji niż węzeł z mniejszym Mempool (chyba że ten ostatni stanie się pusty);
- reguły gW-433: są podzbiorem reguł przekaźnika węzła i definiują cechy, które musi spełniać niepotwierdzona transakcja, aby mogła zostać zaakceptowana w Mempool;
- perkolacja transakcji: z powodu różnych czynników dana transakcja mogła zostać rozesłana do jednej części sieci, ale nie dotarła jeszcze do innej.



Należy zauważyć, że mempoole węzłów nie mają wartości konsensusu. Bitcoin działa doskonale, nawet jeśli każdy węzeł ma inny Mempool. Ostatecznie autorytatywne bloki to zawsze te dodane do Blockchain. Na przykład, nawet jeśli węzeł początkowo odrzuci daną transakcję w swoim Mempool (ważnym zgodnie z zasadami konsensusu), będzie zobowiązany do jej zaakceptowania, jeśli zostanie ostatecznie uwzględniona w bloku z ważnym Proof of Work. Gdyby tego nie zrobił i odrzucił ten blok, mimo że był zgodny z zasadami konsensusu, uruchomiłby Hard Fork, tj. utworzenie nowego, oddzielnego Bitcoin, na którym byłby sam.



#### Polityka i zarządzanie pamięcią



Gdy transakcja zostanie odebrana, Core stosuje serię sprawdzeń pod kątem reguł konsensusu (składnia, prawidłowe skrypty, brak podwójnych wydatków itp.) oraz reguł Mempool, które są lokalną polityką (RBF, minimalne progi opłat, limit danych w `OP_RETURN` itp.). Jeśli transakcja jest zgodna z tymi zasadami, jest przechowywana w pamięci.



Rozmiar Mempool jest ograniczony przez parametr `maxmempool` w pliku `Bitcoin.conf` (więcej na ten temat w następnym rozdziale). Domyślnie limit ten wynosi 300 MB. Gdy jest pełny, węzeł dynamicznie podnosi próg minimalnego obciążenia i najpierw usuwa najmniej opłacalne transakcje (tj. zatrzymuje transakcje, które powinny być wydobywane w pierwszej kolejności). Transakcje, które są zbyt stare, mogą również wygasnąć po skonfigurowanym opóźnieniu.



#### Mempool trwałość na dysku



Aby przyspieszyć ponowne uruchomienie, Core okresowo serializuje stan Mempool w pliku `Mempool.dat`, gdy węzeł jest wyłączony. Oprócz rzeczywistego Mempool, który pozostaje w pamięci, Core przechowuje ten plik `Mempool.dat` na dysku. Następnym razem, gdy węzeł zostanie uruchomiony, ponownie załaduje tę migawkę i usunie wszystko, co nie jest już ważne dla bieżącego Blockchain.



### Pliki pomocnicze i bazy danych



Kilka innych plików na tym samym poziomie co `blocks/`, `chainstate/` i `indexes/` bierze udział w prawidłowym funkcjonowaniu:




- `peers.dat` przechowuje księgę IP Address potencjalnych peerów, zasilaną przez początkowe wykrywanie DNS, wymianę sieci i ręczne dodawanie. Kiedy węzeł się uruchamia, może korzystać z tego pliku w celu ustanowienia połączeń wychodzących.
- Gdy węzeł jest wyłączony, `anchors.dat` zapisuje adresy wychodzących peerów, dzięki czemu można szybko spróbować skontaktować się z nimi ponownie przy następnym uruchomieniu.
- `banlist.json` zawiera lokalne bany ustalone przez operatora lub przez węzeł (powtarzające się nieprawidłowe zachowanie), aby uniemożliwić węzłowi ponowne łączenie się lub akceptowanie połączeń od tych konkretnych peerów.
- `fee_estimates.dat` przechowuje statystyki horyzontu czasowego obserwowanych potwierdzeń, wykorzystywane przez estymator opłat do proponowania stawek opłat zgodnych z celami opóźnień wybranymi podczas tworzenia transakcji.
- gW-446.conf` zawiera parametry konfiguracyjne węzła. To tutaj można dostosować reguły przekaźnika. Więcej na ten temat opowiem w następnym rozdziale.
- `settings.json` zawiera dodatkowe parametry do `Bitcoin.conf`.
- `debug.log` jest diagnostycznym dziennikiem tekstowym, który może być użyty do zrozumienia aktywności węzła w przypadku wystąpienia błędu.
- gW-448.pid` przechowuje identyfikator procesu w czasie wykonywania, umożliwiając innym aplikacjom lub skryptom łatwą identyfikację bitcoind (*Bitcoin daemon*) i interakcję z nim w razie potrzeby. Jest on tworzony podczas uruchamiania węzła i usuwany podczas jego zamykania.
- `ip_asn.map` to tabela mapowania IP → ASN (system autonomiczny) używana do bucketingu i dywersyfikacji peerów (opcja `-asmap`).
- `onion_v3_private_key` przechowuje klucz prywatny usługi Tor v3, gdy włączona jest opcja `-listenonion`, w celu utrzymania stabilnego onion Address pomiędzy restartami.
- `i2p_private_key` przechowuje klucz prywatny I2P, gdy używany jest `-i2psam=`, do nawiązywania połączeń wychodzących i ewentualnie przychodzących na I2P.
- `.cookie` zawiera efemeryczny RPC uwierzytelniający token (tworzony przy uruchamianiu, usuwany przy zamykaniu), gdy używane jest uwierzytelnianie cookie. Może to być wykorzystane na przykład do podłączenia oprogramowania Wallet.
- `.lock` to blokada katalogu danych, która uniemożliwia wielu instancjom jednoczesny zapis do tego samego katalogu danych.
- `guisettings.ini.bak` jest automatycznym zapisem ustawień GUI (*Bitcoin Qt*), gdy używana jest opcja `-resetguisettings`.



Jak widzieliśmy w pierwszych częściach tego kursu BTC 202, Bitcoin core jest zarówno oprogramowaniem węzła Bitcoin, jak i Wallet. Jednak niekoniecznie jest to rozwiązanie, które poleciłbym do zarządzania portfelami, ponieważ jego Interface pozostaje podstawowy, a jego funkcje są ograniczone w porównaniu z nowoczesnym oprogramowaniem, takim jak Sparrow lub Liana. Core zawiera również pliki do zarządzania portfelami:





- `wallets/` jest domyślnym katalogiem, w którym znajduje się jeden lub więcej portfeli;
- `wallets/<nazwa>/Wallet.dat` to baza danych SQLite Wallet (klucze, deskryptory, metadane transakcji itp.);
- wallets/<nazwa>/Wallet.dat-journal` jest dziennikiem wycofania SQLite.



Podsumowując, oto struktura pliku Bitcoin core:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Ścieżka walidacji dla nowego bloku



Po otrzymaniu nowego bloku węzeł sprawdza Proof of Work i, bardziej ogólnie, zgodność z zasadami konsensusu. Jeśli wszystko jest w porządku, stosuje zmiany transakcja po transakcji do swojego zestawu UTXO: sprawdza, czy każdy wpis wydaje istniejące UTXO z ważnym skryptem, usuwa te UTXO i dodaje nowe wyjścia. Jeśli wszystko jest prawidłowe, zmiany są zatwierdzane do `chainstate/`.



Równolegle, dane cofnięcia są zapisywane do pliku `rev*.dat`, a metadane do indeksu `blocks/index/`. Blok jest następnie serializowany do właściwego pliku `blk*.dat`. W przypadku reorganizacji, węzeł odczytuje `rev*.dat` w odwrotnej kolejności, aby czysto odłączyć porzucone bloki, przywrócić zestaw UTXO, a następnie połączyć bloki nowego najlepszego łańcucha.





## Zrozumienie Bitcoin.conf


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Plik `Bitcoin.conf` jest głównym plikiem konfiguracyjnym Interface dla Bitcoin core. Umożliwia on dostosowanie zachowania i parametrów węzła bez konieczności ponownej kompilacji jego kodu źródłowego lub wprowadzania modyfikacji w wierszu poleceń. Mówiąc konkretnie, jest to zwykły plik tekstowy o strukturze par klucz-wartość, co oznacza, że każda linia pliku odwołuje się do określonego parametru (klucza) i powiązanej z nim wartości, którą można zmodyfikować w celu dostosowania tego parametru.



Parametry sieci, przekazywania transakcji, wydajności, indeksowania, logowania i dostępu do RPC można zdefiniować w pliku `Bitcoin.conf`. Jednak ten plik konfiguracyjny nigdy nie modyfikuje zasad konsensusu protokołu: ustawia jedynie lokalną politykę węzła (zasady przekazywania), sposób, w jaki łączy się, indeksuje i udostępnia usługi.



### Lokalizacja i priorytet



Domyślnie `Bitcoin.conf` znajduje się w katalogu danych Bitcoin core. Jest to słynny katalog, o którym wspomnieliśmy w poprzednim rozdziale. Plik ten nie jest jednak automatycznie tworzony przez Bitcoin core, z wyjątkiem niektórych środowisk, takich jak Umbrel. Jeśli jeszcze nie istnieje, będziesz musiał sam go utworzyć, po prostu tworząc plik o nazwie `Bitcoin.conf`, a następnie otwierając go w edytorze tekstu, aby dokonać modyfikacji.



Parametry zdefiniowane w pliku `Bitcoin.conf` mogą zostać zastąpione przez 2 warstwy:




- `settings.json` (napisany dynamicznie przez grafikę Interface lub niektóre RPC),
- i opcje modyfikowane za pomocą linii poleceń.



Należy pamiętać, że każda modyfikacja pliku `Bitcoin.conf` wymaga restartu węzła.



### Format i struktura



Format pliku `Bitcoin.conf` jest więc bardzo prosty: jedna linia na opcję, w formie `option=value`. Niepotrzebne spacje i puste linie są ignorowane, a komentarze do kodu zaczynają się od `#`.



Prawie wszystkie opcje logiczne mogą być wyłączone z prefiksem `no`. Na przykład, `listen=0` i `nolisten=1` są równoważne w zależności od wersji.



Aby podzielić konfigurację według sieci, można użyć sekcji: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Alternatywnie, można poprzedzić nazwę opcji prefiksem `regtest.maxmempool=100`.



### Co Bitcoin.conf może, a czego nie może zrobić



Jak wyjaśniono powyżej, reguły konsensusu nie są oczywiście konfigurowalne w pliku `Bitcoin.conf`, ponieważ mogłoby to spowodować utworzenie Hard Fork. Z drugiej strony, wiele innych aspektów jest konfigurowalnych. Istnieją 3 przydatne klasy, o których należy pamiętać:




- Parametry czysto lokalne. Wpływają one tylko na węzeł: rozmiar pamięci podręcznej (`dbcache`), tryb pruned (`prune`), opcjonalne indeksy.... Wpływają one na wydajność komputera, ale nie na sieć.
- Zasady dotyczące przekaźników i Mempool. Decydują one o tym, co węzeł akceptuje, zachowuje i przekazuje przed potwierdzeniem: minimalny próg opłaty (`minrelaytxfee`), rozmiar Mempool i czas przechowywania (`maxmempool`, `mempoolexpiry`), wymiana transakcji (RBF).... Reguły te nie są częścią konsensusu, więc dwa różne węzły mogą mieć różne polityki i nadal być w pełni kompatybilne. Z drugiej strony, parametry te będą miały wpływ na sieć Bitcoin (jak wyjaśniono w pierwszej części, zwłaszcza w teorii perkolacji).
- Łączność sieciowa. Opcje te określają, w jaki sposób węzeł znajduje rówieśników, nasłuchuje, przechodzi przez NAT, używa Tora lub proxy lub ogranicza przepustowość. Kształtują one topologię, ale nie zmieniają przekazywania transakcji.



Zrozumienie tej separacji jest kluczowe: jeśli transakcja nie jest zgodna z zasadami konsensusu, węzeł i tak ją odrzuci. Jednak bardziej rygorystyczna polityka lokalna może odmówić przekazania transakcji, która jest ważna w sensie konsensusu.



### Sieć i topologia



Przede wszystkim ważne jest wyraźne rozróżnienie między 2 typami połączeń, jakie może mieć węzeł Bitcoin:




- Połączenia wychodzące, które są inicjowane przez nasz węzeł do innego węzła;



![Image](assets/fr/106.webp)





- Połączenia przychodzące, zainicjowane przez inny węzeł do naszego.



![Image](assets/fr/107.webp)



Te dwa typy połączeń są całkowicie zdolne do wymiany tych samych danych w obu kierunkach; nie jest to kwestia ograniczenia kierunku przepływu, a jedynie różnicy w inicjatorze połączenia. Z punktu widzenia naszego węzła, połączenia wychodzące są ogólnie uważane za bezpieczniejsze, ponieważ inicjujemy je i wybieramy dokładnie, z którym węzłem się połączyć, dzięki czemu jest mało prawdopodobne, że połączenie jest złośliwe. Domyślnie Bitcoin core utrzymuje 10 połączeń wychodzących (8 "*full-relay*" + 2 "*block-relay-only*").



Full node dodaje więcej wartości do sieci poprzez akceptowanie połączeń przychodzących. Parametr `listen=1` włącza nasłuchiwanie na domyślnym porcie 8333 danej sieci, umożliwiając odbieranie połączeń przychodzących przez clearnet. Aby to zadziałało, port ten musi być również otwarty na routerze. Jeśli tak nie jest, węzeł będzie nadal działał tylko z połączeniami wychodzącymi, co nie będzie miało wpływu na osobiste korzystanie z Bitcoin. Wybór, czy zezwolić na połączenia przychodzące, należy do użytkownika; nie ma "najlepszego wyboru"



Jeśli wolisz nie otwierać portu na routerze, ale nadal akceptować połączenia przychodzące, możesz aktywować parametr `listenonion=1`. Pozwoli to osiągnąć ten sam rezultat, ale tylko poprzez sieć Tor, a nie clearnet.



Na poziomie sieci mamy również:




- `addnode`: dodaje przyjaznego peera do kontaktu oprócz zwykłego wykrywania (może być określony kilka razy).
- connect`: ściśle ogranicza połączenia do dostarczonego Address (można podać kilka razy). Core nie połączy się z żadnym innym węzłem.
- `seednode`: jest używany tylko do wypełnienia księgi Address podczas łączenia się z węzłem, a następnie rozłącza się.
- `maxconnections`: definiuje globalny limit połączeń przychodzących i wychodzących. Domyślnie parametr ten jest ustawiony na 125, co oznacza, że węzeł nigdy nie zaakceptuje więcej niż 125 połączeń.
- maxuploadtarget`: ogranicza przesyłanie danych w celu ograniczenia przepustowości w 24-godzinnym oknie. Ograniczenie to nie poświęca propagacji istotnych ostatnich Elements.
- `onlynet`: ogranicza połączenia wychodzące tylko do wybranych sieci (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Na przykład, jeśli chcesz, aby twój węzeł łączył się z siecią Bitcoin tylko przez Tor, możesz włączyć parametr `onlynet=onion` i wyłączyć połączenia przychodzące (lub zezwolić na połączenia tylko przez Tor).
- `dnsseed`: zezwala lub nie zezwala _DNS seeds_ na żądanie peerów, gdy lokalna pula Address jest niska (domyślnie: `1`, chyba że `-connect` lub `-maxconnections=0`).
- `forcednsseed`: wymusza żądanie _DNS seeds_ przy starcie, nawet jeśli masz już adresy w magazynie (domyślnie: `0`).
- `fixedseeds`: Zezwól na użycie węzłów *seed* (zakodowana lista Address), jeśli _DNS seeds_ zawiodą lub są wyłączone (domyślnie: `1`).
- `dns`: Autoryzuje rozdzielczość DNS w ogóle (np. dla `-addnode`/`-seednode`/`-connect`).



Domyślnie węzeł komunikuje się przez clearnet, Tor i I2P. Oznacza to, że peery, z którymi łączy się w clearnecie, mogą zobaczyć twój publiczny adres IP Address, a twój dostawca usług internetowych prawdopodobnie będzie w stanie wykryć, że używasz węzła Bitcoin (chociaż P2P Transport V2 utrudnia podsłuchiwanie przez dostawcę usług internetowych). Nie jest to koniecznie problem, ale jeśli chcesz uniknąć wycieku tych informacji, możesz połączyć swój węzeł wyłącznie za pośrednictwem sieci Tor.



Aby w pełni włączyć obsługę Tora, należy zmusić Bitcoin core do korzystania tylko z tej sieci i utworzenia ukrytej usługi dla połączeń przychodzących (jeśli chcesz je włączyć). W pliku `Bitcoin.conf` należy dodać tę konfigurację:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Wszystkie połączenia P2P przechodzą przez Tor. Węzeł otrzymuje adres `.onion` Address dla połączeń przychodzących, więc nie ma potrzeby otwierania portów na routerze. Twój dostawca usług internetowych widzi tylko ruch Tor, a Twoi rówieśnicy nie są świadomi Twojego rzeczywistego publicznego adresu IP Address.



Aby uniknąć rozpoznawania DNS, można dodać `dnsseed=0` i `dns=0` do konfiguracji. Będziesz wtedy musiał ręcznie dostarczyć peery `.onion` poprzez `seednode=` lub `addnode=`, ponieważ w przeciwnym razie wykrywanie nowych węzłów będzie trudne.



Oczywiście, jeśli jesteś początkującym użytkownikiem, radziłbym na razie pozostawić wszystkie te ustawienia sieciowe w spokoju. Domyślna konfiguracja jest często wystarczająca.



### Mempool i polityka przekazywania



#### Podstawowe parametry



Oto podstawowe parametry, które można modyfikować w pliku `Bitcoin.conf` dotyczące zarządzania Mempool i przekazywania niepotwierdzonych transakcji:





- `maxmempool=<n>`: Ogranicza maksymalny rozmiar lokalnego Mempool do `<n>` megabajtów (domyślnie: `300`). Po osiągnięciu limitu węzeł dynamicznie podnosi efektywny próg opłaty i nadaje priorytet najmniej opłacalnym transakcjom (w oparciu o stawkę opłaty, a nie wartość bezwzględną), aby pozostać poniżej limitu. Ustawienie to można pozostawić jako domyślne. Zwiększenie tej wartości może być przydatne, jeśli korzystasz z Mining solo lub jeśli chcesz uzyskać dokładniejszy obraz przeciążenia Mempool i poprawić szacowanie opłat. I odwrotnie, zmniejszenie go pozwoli zaoszczędzić pamięć RAM i, w mniejszym stopniu, inne zasoby systemowe.





- `mempoolexpiry=<n>`: Maksymalny czas retencji dla niepotwierdzonych transakcji w Mempool (w godzinach, domyślnie: `336`). Po tym czasie transakcje są usuwane, nawet jeśli pozostało wolne miejsce.





- `persistmempool=1`: Zapisuje migawkę Mempool w stanie spoczynku i ładuje ją przy ponownym uruchomieniu (domyślnie: `1`). Przyspiesza to odzyskiwanie po ponownym uruchomieniu, unikając konieczności ponownego uczenia się stanu przez sieć.





- `maxorphantx=<n>`: Maksymalna liczba zachowanych transakcji osieroconych (zależne wejścia z UTXO jeszcze nie widziane w zestawie UTXO, domyślnie: `100`). Po przekroczeniu tego progu najstarsze transakcje są usuwane, aby uniknąć niekontrolowanego wzrostu pamięci podręcznej.





- blocksonly=1`: Wyłącza akceptację i retransmisję niepotwierdzonych transakcji otrzymanych od peerów (chyba że przyznano specjalne uprawnienia). Węzeł teraz tylko przesyła i reklamuje bloki. Transakcje utworzone lokalnie mogą być nadal transmitowane (aby używać węzła z oprogramowaniem Wallet). To znacznie zmniejsza zapotrzebowanie na przepustowość i pamięć RAM, aczkolwiek kosztem zmniejszonej użyteczności dla przekaźnika i całkowitej nieznajomości Mempool.





- `minrelaytxfee=<n>`: Minimalna stawka opłaty (w BTC/kvB), poniżej której transakcje nie są akceptowane w Mempool węzła i nie są przekazywane do peerów (domyślnie: `0.00001` = 1 sat/vB). Im wyższa wartość, tym bardziej agresywnie węzeł filtruje tanie transakcje.





- `mempoolfullrbf=1`: Akceptuj transakcje RBF nawet bez wyraźnej sygnalizacji RBF w zastępowanej transakcji. Dzięki tej polityce "*full-RBF*" transakcja oferująca wyższą stawkę opłaty może zastąpić inną w Mempool, jeśli spełnione są inne warunki zastąpienia.



Dla przypomnienia, RBF to mechanizm transakcyjny, który umożliwia nadawcy zastąpienie transakcji transakcją o wyższej opłacie w celu przyspieszenia potwierdzenia. Jeśli transakcja ze zbyt niską opłatą pozostaje zablokowana, nadawca może użyć *Replace-by-fee*, aby zwiększyć opłatę i nadać priorytet transakcji zastępczej w mempoolach i u górników.



#### Ustawienia zaawansowane i szczegółowe



Poniżej znajdują się zaawansowane ustawienia dla Mempool i polityki przekaźników. Jeśli jesteś początkującym użytkownikiem, nie powinieneś modyfikować tych ustawień:





- datacarrier=1`: Pozwala na przekazywanie i (jeśli Mining przez węzeł) włączanie transakcji niosących dane niefinansowe przez wyjście `OP_RETURN` (domyślnie: `1`). Wyłączenie tego parametru nieznacznie zmniejsza powierzchnię spamu danych niefinansowych, kosztem zmniejszonej kompatybilności z niektórymi zastosowaniami. We wszystkich przypadkach należy zaakceptować wydobywane `OP_RETURN`.





- `datacarrierize=<n>`: Maksymalny rozmiar (w bajtach) `OP_RETURN`, który węzeł przekazuje (domyślnie: `83`). Obniżenie tej wartości ogranicza ładunki transportowane przez `OP_RETURN`. Należy pamiętać, że limit ten zostanie domyślnie usunięty w przyszłej wersji Bitcoin core.





- `bytespersigop=<n>`: Parametr, który konwertuje transakcje podpisu na równoważne bajty do oceny limitu przekaźnika (domyślnie: `20`). Wpłynie to na akceptację transakcji bogatych w `sigops` zgodnie z lokalnymi zasadami polityki.





- `permitbaremultisig=1`: Zezwala na przekazywanie *bare-Multisig* transakcji P2MS (domyślnie: `1`). Jest to najstarszy szablon skryptu do ustanawiania warunków wielopodpisu na UTXO (wynaleziony w 2011 roku przez Gavina Andresena).





- `whitelistrelay=1`: Automatycznie przyznaje uprawnienia przekaźnika dla peerów przychodzących z białej listy (domyślnie: `1`). Te peery mają swoje transakcje akceptowane przez przekaźnik, nawet jeśli węzeł nie jest w ogólnym trybie przekaźnika.





- `whitelistforcerelay=1`: Przypisuje uprawnienie "*forcerelay*" do peerów na białej liście z domyślnymi uprawnieniami (domyślnie: `0`). Węzeł następnie przekazuje ich transakcje, nawet jeśli są już obecne w Mempool, omijając w ten sposób mechanizmy zapobiegające redundancji.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Wiąże zakres Interface lub Address i przypisuje drobnoziarniste uprawnienia do odpowiednich urządzeń równorzędnych: `relay`, `forcerelay`, `Mempool` (żądanie zawartości Mempool), `noban`, `download`, `addr`, `bloomfilter`. Może to być przydatne do przyznawania uprzywilejowanego traktowania zaufanym partnerom (takim jak bramy, sieci LAN i usługi wewnętrzne).





- peerbloomfilters=1`: Włącz obsługę filtrów Blooma (BIP37), aby serwować przefiltrowane bloki/transakcje do cienkich klientów (domyślnie: `0`). Ostrzeżenie: zwiększa to obciążenie zasobów.





- peerblockfilters=1`: Serwuje kompaktowe filtry BIP157 (*Neutrino*) do peerów (domyślnie: `0`).





- `blockreconstructionextratxn=<n>`: Dodatkowa liczba transakcji zachowanych w pamięci w celu odbudowania zwartych bloków (domyślnie: `100`). Poprawia powodzenie rekonstrukcji podczas kompaktowych synchronizacji, kosztem niewielkiej ilości pamięci.



Przypominamy, że wszystkie te zasady przekaźnika nie mają wpływu na ważność transakcji zawartych w ważnym bloku. Służą one do dostosowania wkładu użytkownika w przekaźnik, ochrony zasobów i uczynienia węzła przewidywalnym w ograniczonych środowiskach, ale nigdy nie pozwalają na odrzucenie bloków, które są zgodne z zasadami konsensusu.



### Portfele



Można również dostosować sposób zarządzania portfelami w pliku `Bitcoin.conf`. Jeśli nie używasz Wallet bezpośrednio w Core, ale raczej zewnętrznego oprogramowania zarządzającego, takiego jak Sparrow lub Liana, parametry te nie będą miały większego znaczenia:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Określa format adresów generowanych przez Wallet do odbioru.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Wymusza format Exchange Address (pozostała część wejścia na pojedynczej płatności).





- `Wallet=<ścieżka>`: Ładuje istniejący Wallet podczas uruchamiania (można powtórzyć, aby załadować wiele portfeli).





- `walletdir=<dir>`: Katalog zawierający portfele (domyślnie: `<datadir>/wallets` jeśli istnieje, w przeciwnym razie `<datadir>`). Może to być przydatne, jeśli chcesz przechowywać portfele na dedykowanym lub zaszyfrowanym woluminie.





- `walletbroadcast=1`: Automatycznie rozgłasza transakcje utworzone przez załadowane portfele (domyślnie: `1`). Ustaw na `0`, jeśli chcesz zarządzać rozgłaszaniem za pośrednictwem innego kanału.





- `walletrbf=1`: Włącza opcję RBF opt-in, aby sygnalizować RBF na wszystkich transakcjach (domyślnie: `1`). Umożliwia późniejsze zwiększenie opłat w przypadku zablokowania transakcji.





- `txconfirmtarget=<n>`: Cel potwierdzenia transakcji (w liczbie bloków, domyślnie: `6`). Wallet automatycznie ustawi opłatę za transakcję, która ma zostać potwierdzona w ciągu tej liczby bloków.





- `paytxfee=<amt>`: Stała stawka opłaty (BTC/kvB) stosowana do transakcji Wallet. Unikaj ogólnie: użyj szacowania adaptacyjnego za pomocą `txconfirmtarget`.





- fallbackfee=<amt>`: Stawka awaryjna (BTC/kvB) używana, gdy estymatorowi zabraknie danych (domyślnie: `0.00`). Ustawienie wartości 0 całkowicie wyłącza funkcję awaryjną.





- `mintxfee=<amt>`: Minimalny próg (BTC/kvB) dla Wallet do tworzenia transakcji (domyślnie: `0.00001`). Wallet odmówi utworzenia transakcji poniżej tego progu.





- `maxtxfee=<amt>`: Bezwzględny limit całkowitych opłat za transakcję Wallet (domyślnie: `0,10` BTC). Chroni przed nienormalnie wysokimi opłatami, które niepotrzebnie niszczyłyby bitcoiny.





- `avoidpartialspends=1`: Wybiera UTXO według klastrów Address, aby uniknąć częściowych wydatków.





- `spendzeroconfchange=1`: Zezwala na ponowne użycie niepotwierdzonego UTXO Exchange jako wpisu w nowej transakcji (domyślnie: `1`).





- `consolidatefeerate=<amt>`: Maksymalna stawka (BTC/kvB), po przekroczeniu której Wallet unika dodawania większej ilości danych wejściowych niż jest to konieczne do konsolidacji. Pozwala to na oportunistyczne konsolidacje przy niskich cenach i zmniejsza koszty, gdy koszty są wysokie.





- `maxapsfee=<n>`: Budżet na dodatkowe opłaty (BTC, wartość bezwzględna), które Wallet zgadza się zapłacić, aby aktywować opcję "*avoid partial spends*".





- `discardfee=<amt>`: Stawka (BTC/kvB) wskazująca tolerancję na odrzucenie Exchange poprzez dodanie go do opłaty. Wyjścia, które kosztowałyby więcej niż jedną trzecią ich wartości przy tej stawce, są odrzucane.





- `keypool=<n>`: Rozmiar wstępnie wygenerowanej puli Address (domyślnie: `1000`). Zbyt małe wartości zwiększają ryzyko niekompletnego przywracania.





- `disablewallet=1`: Uruchamia Bitcoin core bez podsystemu Wallet i wyłącza powiązane RPC. Zmniejsza powierzchnię ataku i ślad, jeśli węzeł jest używany tylko do walidacji / wydania.



### Przechowywanie, indeksowanie i wydajność



Plik konfiguracyjny umożliwia również dostosowanie parametrów związanych z urządzeniem. Może to być szczególnie istotne, jeśli masz ograniczone zasoby lub, przeciwnie, dużą ilość dostępnej przepustowości:





- `datadir=<dir>`: Ustawia główny katalog danych Bitcoin core.





- `blocksdir=<dir>`: Oddziela lokalizację plików bloków (`blocks/blk*.dat` i `blocks/rev*.dat`) od `datadir`. Może to być przydatne do umieszczenia archiwum bloków na innym woluminie, zachowując bazę stanu (`chainstate/`) na przykład na szybszym nośniku.





- `dbcache=<n>`: Przydziela `<n>` MiB do pamięci podręcznej bazy danych (*LevelDB*) używanej przez indeks bloków i `chainstate` (domyślnie: `450`). Im wyższa wartość, tym szybsze IBD i bieżąca walidacja, kosztem wyższego zużycia pamięci RAM.





- `prune=<n>`: Włącza przycinanie plików blokowych i ustawia docelową przestrzeń dyskową w MiB (domyślnie: `0` = wyłączone; `1` = ręczne przycinanie przez RPC; `>=550` = automatyczne przycinanie poniżej celu). Niekompatybilne z `txindex=1`. Węzeł pozostaje w pełni walidującym węzłem, ale nie może już dostarczać starej historii. Opcja ta jest szczególnie przydatna, jeśli miejsce na dysku jest ograniczone, na przykład podczas instalowania węzła na komputerze domowym.





- txindex=1`: Tworzy i utrzymuje globalny indeks potwierdzonych transakcji. Niezbędny dla niektórych zapytań (`getrawtransaction` nie-Wallet) i do celów eksploracyjnych, ale znacznie zwiększa obciążenie dysku. Niekompatybilne z trybem pruned.





- `assumevalid=<hex>`: Wskazuje blok, który jest uważany za prawidłowy, umożliwiając pominięcie sprawdzania skryptów dla jego przodków (ustaw `0`, aby sprawdzić wszystko). Więcej informacji można znaleźć w poprzednim rozdziale.





- `reindex=1`: Rekonstruuje indeksy bloków i stan (`chainstate`) z plików `blk*.dat` na dysku. Odbudowuje również opcjonalne aktywne indeksy. Jest to czasochłonna operacja używana do naprawy uszkodzonej bazy danych lub czystej aktywacji/dezaktywacji ciężkich indeksów.





- `reindex-chainstate=1`: Odbudowuje tylko `chainstate` z bieżącego indeksu bloków. Preferowane, gdy pliki bloków są zdrowe.





- `blockfilterindex=<typ>`: Utrzymuje indeksy kompaktowych filtrów blokowych (np. `basic`) używanych przez cienkich klientów (BIP157/158) i niektóre RPC. Domyślnie wyłączone (`0`). Zużywa dodatkowe miejsce na dysku i czas indeksowania.





- `coinstatsindex=1`: Utrzymuje indeks statystyk zestawu UTXO obsługiwany przez wywołanie `gettxoutsetinfo`. Przydatne dla audytów i metryk, eliminując potrzebę kosztownego przeliczania. Domyślnie wyłączone.





- `loadblock=<plik>`: Importuje bloki podczas uruchamiania z zewnętrznego pliku `blk*.dat`. Służy do wstępnego ładowania historii ze źródła offline (kopia lokalna, nośnik zewnętrzny) w celu przyspieszenia inicjalizacji.





- `par=<n>`: Ustawia liczbę wątków weryfikacji skryptu (od `-10` do `15`, `0` = auto, `<0` = pozostawia tę liczbę rdzeni wolną). Umożliwia dostosowanie równoległości procesora podczas walidacji. Tryb automatyczny jest odpowiedni w większości przypadków.





- `debuglogfile=<plik>`: Określa lokalizację dziennika `debug.log`.





- `shrinkdebugfile=1`: Zmniejsza rozmiar pliku `debug.log` podczas uruchamiania (domyślnie: `1`, gdy `-debug` nie jest aktywny).





- `settings=<plik>`: Ścieżka do pliku ustawień dynamicznych `settings.json`.



### Dostęp i bezpieczeństwo operacyjne RPC



Wreszcie, plik `Bitcoin.conf` pozwala również skonfigurować parametry dostępu dla węzła. Zachowaj ostrożność z tymi ustawieniami, zwłaszcza jeśli dopiero zaczynasz: unikaj ich zmiany bez dokładnego zrozumienia konsekwencji, ponieważ może to wprowadzić luki w zabezpieczeniach.





- `server=1`: Aktywuje serwer JSON-RPC. Niezbędne, jeśli używasz `bitcoind` przez `bitcoin-cli` lub aplikację innej firmy. Wyłącz (`0`) na węźle czysto walidującym, który nie ujawnia żadnego API lub już używa serwera Electrum.





- `rpcbind=<addr>[:port]`: Serwer RPC nasłuchujący Address/port. Domyślnie nasłuchiwanie odbywa się tylko lokalnie (`127.0.0.1` i `::1`). Ten parametr jest ignorowany, jeśli `rpcallowip` nie jest również zdefiniowany. Użyj go, aby wyraźnie ograniczyć Interface.





- `rpcport=<port>`: Port RPC (domyślnie: `8332` na Mainnet, `18332` na Testnet, `38332` na bookmark, `18443` na regtest).





- `rpcallowip=<ip|cidr>`: Zezwala klientom RPC z danego IP lub podsieci (może się powtarzać). Użyj w połączeniu z `rpcbind`, aby udostępnić API tylko zaufanemu segmentowi (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Zalecana metoda uwierzytelniania RPC (zaszyfrowane hasło). Umożliwia wiele wpisów i pozwala uniknąć przechowywania tajnego hasła w postaci zwykłego tekstu.





- `rpccookiefile=<path>`: Ścieżka do pliku cookie uwierzytelniania (domyślnie: plik `.cookie` pod `datadir/`). Jest to używane do lokalnego dostępu przez tego samego użytkownika bez zarządzania trwałymi hasłami. Na przykład, można go użyć do połączenia Liana Wallet z Bitcoin core na tym samym komputerze.





- `rpcuser=<user>` / `rpcpassword=<pw>`: Klasyczne uwierzytelnianie RPC z hasłem w postaci zwykłego tekstu. Unikaj używania tego na korzyść `rpcauth` lub cookie.





- `rpcthreads=<n>`: Liczba wątków do obsługi wywołań RPC (domyślnie: `4`). Zwiększ ją, jeśli masz wysokie szczyty wywołań po stronie monitorowania/narzędzia zewnętrznego.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Biała lista autoryzowanych interfejsów API. Zmniejsza powierzchnię ataku poprzez ograniczenie dostępnych metod.





- `rpcwhitelistdefault=1|0`: Domyślne zachowanie białej listy: jeśli jest włączone i używana jest biała lista, połączenia niewymienione na liście są odrzucane. Może to również wymusić domyślny pusty zestaw (brak dozwolonych połączeń), o ile nic nie jest wyraźnie wymienione.





- `rest=1`: Włącz publiczne API REST (domyślnie wyłączone). Udostępniane tylko w zaufanej sieci (taka sama ostrożność jak w przypadku JSON-RPC).





- `conf=<plik>`: Określa, tylko w wierszu poleceń, plik konfiguracyjny tylko do odczytu. Przydatne do zamrożenia profilu wykonania (niezmiennego) po stronie operacyjnej.





- `includeconf=<plik>`: Ładuje dodatkowy plik konfiguracyjny (ścieżka względem `datadir/`). Umożliwia rozdzielenie ról: wspólna baza + wrażliwe lokalne przeciążenie.





- `daemon=1` / `daemonwait=1`: Uruchamia `bitcoind` w tle i, z `daemonwait`, czeka na zakończenie inicjalizacji przed przekazaniem. Ułatwia to integrację z nadzorcami (systemd, runit).





- `pid=<plik>`: Lokalizacja pliku PID.





- `sandbox=<log-and-abort|abort>`: Włącza eksperymentalny sandboxing wywołań syscalls: dozwolone są tylko oczekiwane wywołania syscalls.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Wykonuje polecenie podczas uruchamiania lub zamykania systemu.





- `alertnotify=<cmd>`: Uruchamia polecenie po otrzymaniu alertu.





- `blocknotify=<cmd>`: Wykonuje polecenie dla każdego nowego bloku.





- `debug=<kategoria>|1` / `debugexclude=<kategoria>`: Włącza/wyłącza szczegółowe kategorie logów (np. `net`, `Mempool`, `RPC`, `validation`...).





- `logips=1`: Rejestruje adresy IP.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Dodaje odpowiednio lokalizacje źródłowe, nazwy wątków i dokładne znaczniki czasu do dzienników.





- `printtoconsole=1`: Wysyła ślady/debugi do konsoli (*stdout*).





- `help-debug=1`: Wyświetla pomoc opcji debugowania i kończy działanie.





- `uacomment=<cmt>`: Dodaje komentarz do User-Agent P2P.



Zakończyliśmy teraz wypisywanie większości parametrów konfiguracyjnych. Plik `Bitcoin.conf` stanowi zatem prawdziwy pulpit nawigacyjny węzła: definiuje konfigurację sieci, zarządzanie Mempool, użycie dysku i pamięci, indeksowanie i ogólną administrację. Jeśli chciałbyś dowiedzieć się więcej na temat tego pliku i stworzyć plik dostosowany do swoich potrzeb, polecam skorzystanie z [generatora Jamesona Loppa](https://jlopp.github.io/Bitcoin-core-config-generator/).



Dotarliśmy do końca tego kursu BTC 202, który umożliwił ci nie tylko zrozumienie podstaw działania węzłów i ich interakcji w systemie, ale także skonfigurowanie własnego. Jesteś teraz suwerennym Bitcoinerem, z własnym Wallet, transmitującym swoje transakcje za pośrednictwem własnego węzła. Gratulacje!



Możesz teraz przejść do ostatniej części kursu, w której będziesz mógł ocenić BTC 202, a następnie uzyskać dyplom, aby sprawdzić, czy opanowałeś wszystkie omówione koncepcje.



Dostępnych jest teraz kilka opcji. Następnym logicznym krokiem jest skonfigurowanie własnego węzła Lightning, co pozwoli ci być w pełni niezależnym od transakcji off-chain. Będzie to przedmiotem nadchodzącego kursu, który zostanie opublikowany jesienią 2025 r. na Plan ₿ Network.



W międzyczasie zapraszam do zapoznania się ze szkoleniem BTC 204, które pozwoli Ci zrozumieć i opanować zasady ochrony prywatności podczas korzystania z Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Część końcowa


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Recenzje i oceny


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Egzamin końcowy


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Wnioski


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>