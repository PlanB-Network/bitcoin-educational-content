---
name: Wprowadzenie do wydobywania Bitcoinów
goal: Zrozumienie funkcjonowania przemysłu wydobywczego poprzez praktyczne ćwiczenie z wykorzystaniem ASIC-ów.
objectives:
  - Zrozumienie teorii stojącej za wydobyciem
  - Zrozumienie przemysłu wydobywczego
  - Przekształcenie S9 w ogrzewacz
  - Wydobycie pierwszego satoshi
---

# Twoje pierwsze kroki w wydobyciu!

W tym szkoleniu zagłębimy się w przemysł wydobywczy, aby rozwiać tajemnice tego skomplikowanego tematu! Szkolenie jest dostępne dla wszystkich i nie wymaga początkowej inwestycji.

Pierwsza sekcja będzie teoretyczna, gdzie Ajelex i ja będziemy prowadzić dogłębną dyskusję na różne tematy związane z wydobyciem. Pomoże nam to lepiej zrozumieć ten przemysł oraz ekonomiczne i geopolityczne kwestie z nim związane.
W drugiej sekcji zajmiemy się praktycznym przypadkiem. Rzeczywiście, nauczymy się, jak przekształcić używanego koparkę S9 w system ogrzewania domowego! Poprzez przewodniki pisemne i filmy, pokażemy i wyjaśnimy wszystkie kroki, aby osiągnąć to w domu :)

Poprzez ten film, mamy nadzieję pokazać, że przemysł wydobywczy jest bardziej skomplikowany, niż się wydaje, i jego badanie pomaga nuansować ekologiczną debatę, która jest z nim związana!
Jeśli potrzebujesz pomocy przy swojej konfiguracji, dla studentów została utworzona grupa na Telegramie, a wszystkie niezbędne komponenty można znaleźć na naszej platformie e-commerce!

+++

# Wprowadzenie

## Witaj!

Witamy w MINING 201: wprowadzenie do wydobycia. Ajelex, Jim & Rogzy są podekscytowani, że mogą towarzyszyć Ci w Twoich pierwszych konkretnych krokach w tej nowej branży. Mamy nadzieję, że spodoba Ci się kurs i dołączysz do przygody domowego wydobycia!

### Przegląd kursu

W tej części kursu pierwsza sekcja skupi się na teorii wydobycia z Ajelex. Będziemy prowadzić dogłębne dyskusje na różne tematy związane z wydobyciem, co pomoże nam lepiej zrozumieć ten przemysł oraz ekonomiczne i geopolityczne kwestie z nim związane.

W drugiej sekcji zajmiemy się fascynującym przypadkiem praktycznym, ucząc się, jak przekształcić używaną koparkę S9 w system ogrzewania domowego. Poprzez przewodniki pisemne i filmy, wszystkie niezbędne kroki zostaną dokładnie wyjaśnione, zapewniając sukces w tym innowacyjnym projekcie.

Ta podróż edukacyjna pokaże Ci, że przemysł wydobywczy jest bardziej skomplikowany, niż się wydaje, oferując zrównoważoną perspektywę na ekologiczną debatę z nim związaną. Ciągła pomoc będzie dostępna poprzez dedykowaną grupę na Telegramie dla studentów, a wszystkie niezbędne komponenty będą łatwo dostępne na naszej platformie e-commerce.

### Program nauczania:

Sekcja teoretyczna:
* Wyjaśnienie wydobycia.
* Przemysł wydobywczy.
* Niuanse przemysłu wydobywczego.
* Wydobycie w protokole Bitcoin.
* Cena Bitcoina i Hashrate, korelacja? Suwerenność i regulacja
* Wywiad z profesjonalistą z branży wydobywczej

Sekcja praktyczna: Attakai
* Wprowadzenie do Attakai.
* Przewodnik zakupu.
* Modyfikacja oprogramowania koparki Antminer S9.
* Wymiana wentylatorów w celu zmniejszenia hałasu.
* Konfiguracja puli.
* Konfigurowanie Antminera S9 z Braiins OS+.

Gotowy, aby wyruszyć w tę fascynującą przygodę? Zanurzmy się razem w fascynujący świat domowego wydobycia!

# Wszystko, co musisz wiedzieć o wydobyciu

## Wyjaśnienie wydobycia

![Co to jest wydobycie Bitcoinów?](https://www.youtube.com/watch?v=neEQzEQzmPQ)

### Wydobycie wyjaśnione: Analogia łamigłówki
Aby w prosty sposób wyjaśnić koncepcję wydobywania (mining), można użyć odpowiedniej analogii: układanki. Podobnie jak układanka, mining jest złożonym zadaniem do wykonania, ale łatwym do zweryfikowania po zakończeniu. W kontekście wydobywania Bitcoinów, górnicy starają się szybko rozwiązać cyfrową łamigłówkę. Pierwszy górnik, który rozwiąże zagadkę, prezentuje swoje rozwiązanie całej sieci, która może łatwo zweryfikować jego ważność. Ta udana weryfikacja pozwala górnikowi na zatwierdzenie nowego bloku i dodanie go do Łańcucha Czasu Bitcoin. W uznaniu ich pracy, która wiąże się z istotnymi kosztami, górnik jest nagradzany pewną liczbą bitcoinów. Ta nagroda służy jako finansowa zachęta dla górników do kontynuowania pracy nad weryfikacją transakcji i zabezpieczaniem sieci Bitcoin.
![image](assets/overview/puzzle.png)

Początkowo w sieci Bitcoin nagroda wynosiła 50 bitcoinów co dziesięć minut, równolegle do odkrywania bloku co dziesięć minut średnio przez górników. Ta nagroda ulega zmniejszeniu o połowę co 210 000 bloków, co około cztery lata. Ta rekompensata służy jako potężna zachęta, aby zachęcić górników do uczestnictwa w procesie wydobywczym pomimo jego kosztów energetycznych. Bez nagrody, energochłonne wydobywanie zostałoby porzucone, co zagrażałoby bezpieczeństwu i stabilności całej sieci Bitcoin.
Obecna nagroda za wydobycie ma dwie formy. Z jednej strony obejmuje tworzenie nowych bitcoinów, które zmniejszyło się z 50 bitcoinów co dziesięć minut na początku do 6,25 bitcoinów dzisiaj (2023). Z drugiej strony obejmuje opłaty transakcyjne, czyli opłaty za wydobycie, z transakcji, które górnik decyduje się uwzględnić w swoim bloku. Gdy dokonywana jest transakcja bitcoinowa, płaci się opłaty transakcyjne. Te opłaty działają jak rodzaj aukcji, gdzie użytkownicy wskazują, ile są skłonni zapłacić, aby ich transakcja została uwzględniona w następnym bloku. Aby zwiększyć swoją nagrodę, górnicy, działając w swoim własnym interesie, wybierają najbardziej opłacalne transakcje do uwzględnienia w swoim bloku, biorąc pod uwagę ograniczoną dostępną przestrzeń. W ten sposób nagroda za wydobycie składa się zarówno z generowania nowych bitcoinów, jak i opłat transakcyjnych, zapewniając ciągłą zachętę dla górników i zapewniając długowieczność i bezpieczeństwo sieci Bitcoin.

### Górnicy i ich narzędzia: Mining

Proces wydobywania polega na znalezieniu ważnego hasha, który jest akceptowalny przez sieć Bitcoin. Po obliczeniu i znalezieniu, ten hash jest nieodwracalny, podobnie jak ziemniaki zamienione w puree ziemniaczane. Weryfikuje on pewną funkcję bez możliwości cofnięcia się. Górnicy, w konkurencji, używają maszyn do obliczania tych hashy. Chociaż teoretycznie możliwe jest znalezienie tego hasha ręcznie, złożoność operacji sprawia, że opcja ta jest niewykonalna. Komputery, zdolne do szybkiego wykonywania tych obliczeń, są więc używane, zużywając znaczną ilość energii elektrycznej.

Na początku dominowała era CPU, gdzie górnicy używali swoich komputerów osobistych do wydobywania Bitcoinów. Odkrycie zalet GPU (kart graficznych) dla tego zadania oznaczało punkt zwrotny, znacznie zwiększając hashrate i redukując zużycie energii. Postęp nie zatrzymał się na tym, z kolejnym wprowadzeniem FPGA (programowalnych macierzy bramek). FPGA służyły jako platforma do rozwoju ASIC (układów scalonych o specjalnym przeznaczeniu).

![image](assets/overview/chip.png)

ASIC to chipy, porównywalne do chipa CPU, jednak są one rozwijane do wykonywania tylko jednego konkretnego typu obliczeń w możliwie najbardziej efektywny sposób. Innymi słowy, CPU jest zdolne do wykonywania wielu różnych typów obliczeń bez bycia szczególnie zoptymalizowanym pod kątem jednego typu obliczeń czy innego, podczas gdy ASIC będzie w stanie wykonywać tylko jeden typ obliczeń, ale bardzo efektywnie. W przypadku ASIC Bitcoin, są one zaprojektowane do obliczania algorytmu SHA256.
Obecnie górnicy wykorzystują wyłącznie dedykowane ASIC do tej operacji, zoptymalizowane do testowania maksymalnej liczby kombinacji przy jak najmniejszym zużyciu energii i jak najszybciej. Te komputery, niezdolne do wykonywania zadań innych niż wydobycie Bitcoinów, są namacalnym świadectwem ciągłej ewolucji i rosnącej specjalizacji w branży wydobycia Bitcoinów. Ta ciągła ewolucja odzwierciedla wewnętrzną dynamikę Bitcoina, gdzie dostosowanie trudności zapewnia produkcję bloku co dziesięć minut, pomimo wykładniczego wzrostu zdolności wydobywczych.

Aby zilustrować intensywność tego procesu, rozważmy typowego górnika zdolnego do osiągnięcia 14 TeraHash na sekundę, czyli 14 bilionów prób znalezienia odpowiedniego hasha co sekundę. Na skalę sieci Bitcoin, osiągamy obecnie około 300 HexaHash na sekundę, co podkreśla zbiorową moc mobilizowaną w wydobyciu Bitcoinów.

### Dostosowanie Trudności:

Dostosowanie trudności to kluczowy mechanizm w działaniu sieci Bitcoin, zapewniający, że bloki są wydobywane średnio co 10 minut. Czas ten jest średnią, ponieważ proces wydobycia jest w rzeczywistości grą prawdopodobieństwa, podobną do rzucania kośćmi w nadziei na uzyskanie liczby mniejszej niż liczba określona przez trudność. Co 2016 bloków, sieć dostosowuje trudność wydobycia na podstawie średniego czasu wymaganego do wydobycia poprzednich bloków. Jeśli średni czas jest większy niż 10 minut, trudność jest zmniejszana, a w przeciwnym razie, jeśli średni czas jest niższy, trudność jest zwiększana. Ten mechanizm dostosowania zapewnia, że czas wydobycia nowych bloków pozostaje stały w czasie, niezależnie od liczby górników czy ogólnej mocy obliczeniowej sieci. Dlatego Blockchain Bitcoin jest również nazywany Timechain.

![image](assets/overview/chinaban.png)

* Przykład z Chin:
Przypadek Chin doskonale ilustruje ten mechanizm dostosowania trudności. Dzięki obfitej i taniej energii, Chiny były głównym globalnym centrum wydobycia Bitcoinów. W 2021 roku kraj ten nagle zakazał wydobycia Bitcoinów na swoim terytorium, co spowodowało masowy spadek hashrate globalnej sieci Bitcoin, około 50%. Ta szybka redukcja mocy wydobywczej mogła poważnie zakłócić sieć Bitcoin, zwiększając średni czas wydobycia bloków. Jednak mechanizm dostosowania trudności wszedł w życie, redukując trudność wydobycia, aby zapewnić, że częstotliwość wydobycia bloków pozostaje na średnim poziomie 10 minut. Ten przypadek demonstruje efektywność i odporność mechanizmu dostosowania trudności Bitcoina, który zapewnia stabilność i przewidywalność sieci, nawet w obliczu nagłych i znaczących zmian w globalnym krajobrazie wydobycia.

### Ewolucja maszyn do wydobycia Bitcoinów

W kontekście ewolucji maszyn do wydobycia Bitcoinów ważne jest zauważenie, że kontekst jest bardziej zorientowany na tradycyjny model biznesowy. Górnicy zarabiają na walidacji bloków, zadaniu o stosunkowo niskim prawdopodobieństwie sukcesu. Obecny model w użyciu, Antminer S9, choć jest starszym modelem wprowadzonym około 2016 roku, nadal jest obecny na rynku wtórnym, handlując za około 100 do 200 euro. Jednak cena maszyn do wydobycia waha się w zależności od wartości Bitcoina, a nowszy model, Antminer S19, jest obecnie wyceniany na około 3000 euro.

W obliczu ciągłych postępów technologicznych w dziedzinie wydobycia, profesjonaliści muszą strategicznie się pozycjonować. Branża wydobywcza podlega ciągłym innowacjom, jak pokazuje niedawne wprowadzenie na rynek wersji J modelu S19 i oczekiwane wprowadzenie modelu S19 XP, oferujące znacznie wyższe możliwości wydobywcze. Ponadto, ulepszenia nie dotyczą tylko surowej wydajności maszyn. Na przykład nowy model S19 XP wykorzystuje system chłodzenia cieczą, techniczną modyfikację, która pozwala na znaczną poprawę efektywności energetycznej. Chociaż innowacja pozostaje stała, przyszłe zyski w efektywności będą prawdopodobnie mniejsze w porównaniu do tych obserwowanych do tej pory, ze względu na osiągnięcie pewnego progu innowacji technologicznych.
![obraz](assets/overview/chipevolution.png)Podsumowując, przemysł wydobywczy Bitcoin ciągle się adaptuje i rozwija, a uczestnicy rynku muszą przewidywać zmniejszające się zyski z efektywności w przyszłości i odpowiednio dostosowywać swoje strategie. Przyszłe postępy technologiczne, choć nadal obecne, prawdopodobnie będą miały miejsce w mniejszej skali, co odzwierciedla rosnącą dojrzałość sektora.
## Przemysł wydobywczy

![Czy wydobycie Bitcoin jest zbyt scentralizowane? Ryzyka i rozwiązania](https://www.youtube.com/watch?v=xkiY8DgkcLQ)

### Baseny wydobywcze

Obecnie wydobycie Bitcoin przekształciło się w poważny i znaczący przemysł, z wieloma graczami, którzy są teraz publicznie znani i rosnącą liczbą znaczących górników. Ta ewolucja sprawiła, że wydobycie stało się prawie niedostępne dla małych graczy z powodu wysokich kosztów związanych z nabyciem nowych maszyn wydobywczych. Rodzi to pytanie o dystrybucję hashrate wśród różnych graczy rynkowych. Sytuacja jest skomplikowana, ponieważ istotne jest zbadanie zarówno dystrybucji hashrate wśród różnych firm, jak i wśród różnych basenów wydobywczych.

![obraz](assets/overview/pool.png)

Basen wydobywczy to grupa górników, którzy łączą swoje zasoby obliczeniowe, aby zwiększyć swoje szanse na wydobycie. Ta współpraca jest konieczna, ponieważ izolowana mała maszyna wydobywcza konkuruję z gigantami branży, redukując swoje szanse na sukces do poziomu znikomego. Wydobycie działa na zasadzie loterii, a szanse na wygranie bloku (a więc nagrody w Bitcoinach) co dziesięć minut są niezwykle niskie dla indywidualnego małego górnika. Łącząc się, górnicy mogą połączyć swoją moc obliczeniową, znaleźć bloki częściej, a następnie rozdzielić nagrody proporcjonalnie do wkładu każdego górnika do basenu.

Na przykład, jeśli basen znajdzie blok i wygra 6,25 bitcoina, górnik przyczyniający się 1% całkowitej mocy obliczeniowej basenu otrzyma 1% z zarobionych 6,25 bitcoina. Należy jednak zauważyć, że baseny wydobywcze zazwyczaj pobierają małą prowizję (zwykle około 2%), aby pokryć koszty operacyjne spółdzielni.

### Oprogramowanie używane przez przemysł

W kontekście wydobycia Bitcoin, rola oprogramowania jest równie kluczowa co sprzęt. Przykładem tego jest rola Bitmain, płodnego producenta, który opracował Antminer S9. Oprócz sprzętu do wydobycia, przemysł ten w dużej mierze polega na współpracujących basenach wydobywczych, takich jak Brainspool, który kontroluje około 5% globalnego hashrate sieci Bitcoin.
Aktorzy w tym przemyśle ciągle dążą do zwiększenia efektywności poprzez sprzęt i oprogramowanie. Na przykład, popularnym oprogramowaniem używanym w tym kontekście jest BrainsOS Plus. To oprogramowanie zastępuje oryginalny system operacyjny maszyny wydobywczej, pozwalając na wykonywanie tych samych operacji bardziej efektywnie. Dzięki takiemu oprogramowaniu, górnik może zwiększyć efektywność swojej maszyny o 25%. Oznacza to, że przy równoważnej ilości energii elektrycznej, maszyna może wyprodukować dodatkowe 25% hashrate, zwiększając tym samym nagrody otrzymywane przez górnika. Optymalizacja oprogramowania jest kluczowym elementem konkurencyjności w wydobyciu Bitcoin, demonstrując znaczenie zintegrowanego podejścia, które łączy ulepszenia sprzętu i oprogramowania, aby maksymalizować efektywność i zwroty.

### Regulacje i taryfy elektryczne

Jak zaobserwowano w Chinach i innych miejscach, regulacje mają znaczący wpływ na wydobycie. Chociaż we Francji nie ma znaczących górników, regulacje i wysokie taryfy elektryczne w Europie są głównymi przeszkodami. Górnicy ciągle szukają taniej elektryczności, aby maksymalizować swoje zyski. Dlatego wysokie koszty energii elektrycznej w Europie i Francji nie przyciągają górników do tych regionów.
Górnicy często skłaniają się ku regionom z niskimi taryfami za energię elektryczną, często w krajach rozwijających się lub krajach z nadwyżkami energetycznymi. Na przykład, duża część globalnej mocy obliczeniowej (hashrate) znajduje się w Teksasie, w Stanach Zjednoczonych. Teksas posiada niezależną sieć energetyczną, która nie dzieli swoich zasobów energetycznych z innymi stanami. Ta unikalność często prowadzi do tego, że Teksas produkuje więcej energii elektrycznej niż jest to konieczne, aby uniknąć niedoborów, tworząc nadwyżkę. Górnicy Bitcoin korzystają z tej nadprodukcji, zakładając operacje w Teksasie, gdzie mogą wydobywać bitcoiny przy bardzo niskich stawkach za energię elektryczną w okresach nadwyżki energetycznej. Ta sytuacja demonstruje znaczący wpływ regulacji i taryf energetycznych na wydobycie Bitcoin, podkreślając znaczenie tych czynników w procesie decyzyjnym górników dotyczącym lokalizacji ich operacji wydobywczych.

### Dokąd zmierzają górnicy i zarządzanie energią?

Podkreślając wpływ górników Bitcoin na świat energii, trajektoria jest jasna: ci aktorzy nieustannie poszukują źródeł taniej energii elektrycznej, często takich, które są marnowane lub niezagospodarowane. To zjawisko jest widoczne w regionach z nową infrastrukturą elektryczną, takich jak te wyposażone w niedawno zbudowane tamy hydroelektryczne.
Weźmy przykład. W kraju, który jest w trakcie budowy tamy, produkcja energii elektrycznej często rozpoczyna się zanim linie dystrybucyjne będą w pełni operacyjne. Ta luka czasowa może prowadzić do znaczących kosztów i zniechęcać do inwestycji w takie projekty infrastrukturalne. Jednakże, górnicy Bitcoin mogą działać jako elastyczne źródło popytu, gotowe do konsumpcji tej "osieroconej" energii elektrycznej, tym samym pomagając zrównoważyć koszty infrastruktury. Implikacja tutaj jest taka, że nowe instalacje mogą być natychmiast rentowne, promując tworzenie nowych źródeł energii elektrycznej. Zasada ta stosuje się również w mniejszej skali. Czy to pojedyncza osoba używająca generatora hydroelektrycznego na małej rzece, czy gospodarstwo domowe wyposażone w panele słoneczne, nadmiar wyprodukowanej energii elektrycznej może być wykorzystany do zasilania operacji wydobywczych Bitcoin.

We Francji, na przykład, nadwyżka energii elektrycznej z paneli słonecznych jest wtłaczana z powrotem do sieci, a producenci są rekompensowani kredytem konsumenckim od EDF. Podobnie, można sobie wyobrazić górnika działającego na tej nadwyżce energii elektrycznej, wyłączającego się, gdy lokalny popyt równa się podaży. Chociaż może to wydawać się samolubne, priorytetyzując produkcję bitcoinów nad wsparciem lokalnej sieci energetycznej, przedstawia to inny kąt: stabilizowanie sieci energetycznej. Złożone zarządzanie nadwyżkami energii elektrycznej, czasami nawet związane z kosztami jej utylizacji, może być znacznie uproszczone. Górnicy Bitcoin mogą absorbować te nadwyżki, działając jako elastyczny bufor, dostosowując popyt zamiast podaży. W świecie, w którym produkcja energii elektrycznej z odnawialnych źródeł (niekontrolowalnych) stale rośnie, górnicy mogą odgrywać kluczową rolę w zapewnieniu równowagi naszych sieci energetycznych, jednocześnie korzystając z taniej lub nadwyżkowej energii elektrycznej do zasilania swoich operacji wydobywczych.

### Centralizacja wydobycia

Centralizacja wydobycia jest traktowana jako główne wyzwanie. Dużymi graczami, takimi jak Foundry, dominuje rynek, co potencjalnie może prowadzić do cenzurowania transakcji. Ta centralizacja może również uczynić sieć podatną na ataki, w tym atak 51%, gdzie aktor lub grupa kontroluje więcej niż 50% mocy obliczeniowej sieci, pozwalając im kontrolować i manipulować siecią.
Ryzyko regulacji Podkreśla się, że jeśli kraj taki jak Stany Zjednoczone zdecydowałby się regulować lub zakazać pewnych transakcji Bitcoin, mogłoby to mieć znaczący wpływ na sieć, szczególnie jeśli duża część mocy obliczeniowej jest skoncentrowana w tym kraju.

![image](assets/overview/foundry.png)

Aby zwalczać tę centralizację, omawiane są różne strategie:
* Wydobycie domowe: Idea Wydobycia domowego opiera się na decentralizacji działalności wydobywczej. Zachęca się osoby indywidualne do uczestnictwa w wydobyciu z ich domów, tym samym rozprowadzając moc obliczeniową szerzej.
* Stratum V2: Protokół Stratum V2 oferuje inne podejście. W przeciwieństwie do swojego poprzednika, Stratum V2 pozwala górnikom na wybór, które transakcje mają zostać uwzględnione w wydobywanych przez nich blokach. Ta zdolność wzmacnia odporność na cenzurę i zmniejsza możliwość dominacji dużych pul miningowych w sieci. Dając więcej mocy indywidualnym górnikom, protokół Stratum V2 może odgrywać decydującą rolę w walce z centralizacją hashrate.
* Otwarte oprogramowanie do wydobywania: To kolejna potencjalnie skuteczna strategia. Udostępniając oprogramowanie do wydobywania dla wszystkich, mali górnicy mieliby takie same możliwości jak duże firmy górnicze do uczestnictwa i przyczyniania się do sieci blockchain. To podejście zachęcałoby do szerszego rozpowszechnienia hashrate, przyczyniając się tym samym do decentralizacji sieci.
* Dywersyfikacja aktorów i geografii: Zachęcanie do udziału różnorodnych aktorów z różnych regionów geograficznych w wydobyciu kryptowalut również może okazać się skuteczne. Dzięki geograficznej dywersyfikacji hashrate, trudniej jest pojedynczemu aktorowi lub krajowi wywierać nieproporcjonalną kontrolę lub wpływ na sieć. To podejście może pomóc chronić sieć przed potencjalnymi atakami i wzmacniać jej decentralizację.

Ogólny wniosek jest taki, że decentralizacja jest kluczowa dla bezpieczeństwa i odporności sieci Bitcoin. Chociaż centralizacja może oferować korzyści efektywnościowe, naraża sieć na znaczące ryzyka, w tym cenzurę i ataki 51%. Inicjatywy takie jak Takai i przyjęcie nowych protokołów jak Stratum V2 są ważnymi krokami w kierunku decentralizacji i ochrony sieci Bitcoin przed tymi zagrożeniami.

## Niuanse branży wydobywczej

![Ogrzewanie domu przez wydobycie bitcoinów?](https://www.youtube.com/watch?v=SQaK4_8M0kA)

### Zasada Attakai
Limit tej decentralizacji?
Pomimo że pomysł decentralizacji wydobycia poprzez produktywne wykorzystanie generowanego ciepła wydaje się obiecujący, ma pewne ograniczenia i pozostają pytania. Obiekty o intensywnym zużyciu energii, takie jak sauny i baseny, mogłyby skorzystać z tego koncepcji, wykorzystując ciepło produkowane przez górników do ogrzewania wody w swoich obiektach. Praktyka ta jest już wdrażana przez niektórych członków społeczności Bitcoin, którzy eksplorują różne metody efektywnego wykorzystania ciepła generowanego przez sprzęt do wydobycia. Na przykład sala bankietowa teoretycznie mogłaby być ogrzewana przez trzy lub cztery koparki S19, każda zużywająca 3000 watów i produkująca równoważną ilość ciepła.

Jednak należy zauważyć, że zużycie energii i produkcja ciepła są równoważne, niezależnie od tego, czy energia jest wykorzystywana przez grzejnik elektryczny, czy górnika. Na każdy kilowat zużytej energii elektrycznej, ilość produkowanego ciepła będzie taka sama w obu przypadkach. Różnica polega na tym, że górnik nie tylko dostarcza ciepło, ale także nagrodę w bitcoinach, oferując tym samym ekonomiczną zachętę do używania koparki zamiast prostego grzejnika elektrycznego. Ta dodatkowa nagroda mogłaby pomóc złagodzić obawy dotyczące wysokiego zużycia energii przez górników.

Pytanie o długoterminową efektywność i wykonalność wykorzystania koparek bitcoinowych do ogrzewania pozostaje otwarte. Trwające innowacje w sprzęcie do wydobycia i technologiach grzewczych mogą potencjalnie otworzyć nowe możliwości dla bardziej efektywnego wykorzystania ciepła generowanego przez wydobycie, przyczyniając się tym samym do wykonalności tego podejścia w przyszłości.

### Dlaczego nagrody w BTC?

Pytanie o nagradzanie w bitcoinach, a nie innej walucie, jest kluczowe w systemie zaprojektowanym przez Satoshi Nakamoto. Tworzenie Bitcoina charakteryzuje się stałym limitem 21 milionów jednostek. Celem było znalezienie sprawiedliwego sposobu dystrybucji tych nowo utworzonych jednostek. Górnicy, dostarczając swoją moc obliczeniową do zabezpieczenia sieci i czyniąc każdy atak coraz kosztowniejszym, skutecznie chronią sieć Bitcoin. W zamian za ten kluczowy wkład, są nagradzani nowo utworzonymi bitcoinami, ułatwiając dystrybucję monet w ekosystemie.
Jest to system korzystny dla obu stron. Górnicy są nagradzani zarówno za zabezpieczanie sieci, jak i zatwierdzanie transakcji. Nowo utworzone bitcoiny są dawane jako zachęta do wzmocnienia bezpieczeństwa, a opłaty transakcyjne stanowią dodatkowy dochód za zatwierdzanie transakcji. Te dwa elementy razem stanowią całkowitą nagrodę za wydobycie. Pytanie o przyszłość wydobycia pojawia się z powodu zaprogramowanego zmniejszenia nagród za wydobycie, które zmniejsza się o połowę co cztery lata, zdarzenie znane jako "halving". Do 2032 roku nagroda za blok będzie mniejsza niż jeden bitcoin, a do 2140 roku nie będą tworzone nowe bitcoiny. W tym momencie górnicy będą polegać wyłącznie na opłatach transakcyjnych za wynagrodzenie. Sieć Bitcoin będzie musiała obsługiwać dużą liczbę transakcji, z wystarczająco wysokimi opłatami, aby zapewnić rentowność wydobycia. Pojawienie się Lightning Network, które umożliwia szybkie i tanie transakcje poza głównym łańcuchem Bitcoin, rodzi pytania o przyszłość wydobycia. Lightning Network ma potencjał znacznego zmniejszenia opłat transakcyjnych, wpływając tym samym na dochody górników. Jednak będzie to zależeć od adopcji i użytkowania Lightning Network w porównaniu z główną siecią Bitcoin. W pesymistycznym scenariuszu górnicy mogą uznać wydobycie za opłacalne nawet przy stratach, jeśli zdołali już zamortyzować swoje koszty i mają dostęp do taniej energii elektrycznej. W bardziej optymistycznym scenariuszu opłaty transakcyjne w głównej sieci Bitcoin mogą pozostać na wystarczająco wysokim poziomie, aby utrzymać rentowność wydobycia.

### Co powinno być zawarte w bloku Bitcoin?

W kwestii tego, co powinno być zawarte w bloku Bitcoin, kluczowe jest rozważenie komplementarnej natury różnych warstw sieci Bitcoin. Chociaż Lightning Network może umożliwić szybsze i tańsze transakcje, nadal polega na bazowej warstwie Bitcoin, często określanej jako "warstwa rozliczeniowa", do otwierania i zamykania kanałów płatności.

Wraz z oczekiwanym wzrostem Lightning Network i wynikającym z tego wzrostem otwierania i zamykania kanałów, przestrzeń w blokach Bitcoin stanie się coraz bardziej cenna. Społeczność Bitcoin już ma tendencję do cenić zachowanie tej przestrzeni, rozpoznając jej wrodzone ograniczenie. Ta świadomość doprowadziła do dyskusji na temat legalnego użytkowania przestrzeni blokowej, z obawami o "spam" na blockchainie z transakcji uznawanych za nieistotne.

![image](assets/overview/block.png)
Spekulacje otaczają przyszłe wykorzystanie przestrzeni blokowej, ale ogólnie przyjmuje się, że jest to zasób ograniczony, który powinien być mądrze wykorzystywany. Chociaż istnieje chęć wypełnienia go, istotne jest, aby zachować go w celu zapewnienia długoterminowej żywotności sieci Bitcoin, przewidując przyszły wzrost zapotrzebowania na przestrzeń blokową. Jak w każdym wolnym rynku, podaż i popyt będą regulować wykorzystanie przestrzeni blokowej. Przy ograniczonej podaży, interesariusze będą musieli dokonywać świadomych wyborów dotyczących wykorzystania tej cennej przestrzeni, aby zapewnić długoterminową efektywność i bezpieczeństwo sieci Bitcoin.

## Wydobycie w protokole Bitcoin

![Kto ma moc? Bitcoin, energia i producenci](https://www.youtube.com/watch?v=4wywK6BfDw8)

Rola górników w sieci Bitcoin była przedmiotem intensywnej debaty podczas wojen o rozmiar bloku. Chociaż są niezbędni dla bezpieczeństwa i funkcjonalności sieci, górnicy niekoniecznie posiadają ostateczną moc w ekosystemie Bitcoin. Równowaga między górnikami, węzłami i użytkownikami końcowymi zapewnia integralność i dystrybucję sieci.

### Wojny o rozmiar bloku

Podczas wojen o rozmiar bloku wielu górników sprzeciwiało się pewnym rozwojom sieci, podkreślając napięcie między różnymi aktorami w ekosystemie. Pytanie pozostaje, jak zrównoważyć moc między górnikami, węzłami i użytkownikami, aby zapewnić długoterminowe bezpieczeństwo Bitcoin.

Bezpieczeństwo i równowaga sił

![image](assets/overview/blocksize-wars--BTC-vs-BCH-.webp)
Dylemat bezpieczeństwa Bitcoina opiera się na delikatnej równowadze. Chociaż górnicy odgrywają kluczową rolę w walidacji i tworzeniu bloków, węzły utrzymują integralność poprzez weryfikację i walidację transakcji oraz bloków. Nieprawidłowy lub fałszywy blok zostanie odrzucony przez węzły, cenzurując górnika i zachowując bezpieczeństwo sieci. Moc jest również w rękach węzłów i użytkowników sieci Bitcoin. Węzły mają moc weryfikacji i walidacji, podczas gdy użytkownicy mają moc wyboru, której blockchain użyć. Ta dystrybucja mocy zapewnia dystrybucję i integralność sieci Bitcoin.
Wojny blokowe ujawniły wrodzoną niepewność i napięcie w zarządzaniu siecią Bitcoin. Chociaż Bitcoin Core jest obecnie dominującym łańcuchem, debata nad zarządzaniem i zarządzaniem siecią trwa.
Ostatecznie odpowiedzialność jest współdzielona przez wszystkich aktorów w sieci Bitcoin. Spadek liczby użytkowników, węzłów lub górników może osłabić sieć, zwiększając ryzyko centralizacji i podatności na ataki. Każdy aktor przyczynia się do solidności i bezpieczeństwa sieci, wzmacniając znaczenie utrzymania równowagi mocy i odpowiedzialności.
### Moc górników

Elegancka teoria gier Satoshi Nakamoto stworzyła sytuację, w której każdy aktor w sieci Bitcoin jest zmotywowany do prawidłowego działania, aby chronić zarówno własne interesy, jak i interesy innych uczestników. Tworzy to równowagę, gdzie złe zachowanie może być karane, wzmacniając tym samym bezpieczeństwo i stabilność całego systemu. Pomimo tej równowagi, państwa pozostają potencjalnym zagrożeniem. Jak wskazano na prezentacji na Surfing Bitcoin 2022, państwa mogą próbować zaatakować przemysł wydobywczy, narażając sieć Bitcoin na ryzyko centralizacji i ataku. Hipotetyczne scenariusze, takie jak atak wojskowy na obiekty produkcyjne sprzętu do wydobycia, podkreślają znaczenie geograficznej i przemysłowej dywersyfikacji dla odporności sieci Bitcoin.

![image](assets/overview/miner.png)

Centralizacja produkcji sprzętu wydobywczego w Chinach stanowi kolejne ryzyko. Odmowa eksportu maszyn do wydobycia lub akumulacja hashrate na potrzeby potencjalnego ataku 51% przez Chiny podkreśla potrzebę zdywersyfikowanej produkcji sprzętu wydobywczego. W obliczu tych ryzyk, społeczność Bitcoin aktywnie szuka rozwiązań. Firmy takie jak Intel rozważają produkcję sprzętu do wydobycia w Stanach Zjednoczonych, przyczyniając się do dystrybucji produkcji. Inne inicjatywy, takie jak otwarty zestaw narzędzi do wydobycia (MDK) firmy Block, mają na celu zmniejszenie monopolu na projektowanie i produkcję sprzętu wydobywczego, umożliwiając szerszą dystrybucję hashrate. W centrum tych dyskusji jest fundamentalna misja Bitcoina: być siecią wymiany wartości odporną na cenzurę. Społeczność Bitcoin nieustannie dąży do wzmocnienia dystrybucji, odporności na cenzurę i antykruchości sieci, odrzucając propozycje takie jak przejście na proof of stake, które nie są zgodne z tymi zasadniczymi zasadami.

### Fizyczne powiązanie proof of work vs proof of stake
Proof of Work (PoW) jest kluczowe, ponieważ stanowi fizyczne powiązanie między rzeczywistym światem a Bitcoinem. Chociaż bitcoiny są niematerialne, ich produkcja wymaga namacalnej energii, ustanawiając bezpośrednie powiązanie z fizycznym i rzeczywistym światem. To połączenie zapewnia, że produkcja i walidacja bitcoinów oraz bloków mają rzeczywisty koszt energetyczny, zakotwiczając sieć Bitcoin w fizycznej rzeczywistości i zapobiegając jej całkowitej dominacji przez potężne podmioty. PoW działa jako bariera przed centralizacją, zapewniając, że uczestnictwo w sieci i walidacja transakcji wymagają inwestycji w namacalne zasoby. Zapobiega to monopolizacji sieci przez podmioty, które w przeciwnym razie mogłyby przejąć kontrolę bez żadnych znaczących barier wejścia, zapewniając bardziej sprawiedliwy podział mocy i wpływów w sieci Bitcoin.
![image](assets/overview/POWPOS.png)

### Ograniczenia Proof of Stake
Z drugiej strony, Proof of Stake (PoS), choć pozwala na udział w małej skali, nie gwarantuje równoważnej ochrony przed centralizacją. W sieci PoS, ci, którzy już posiadają dużą ilość waluty, mają nieproporcjonalnie dużą moc, odzwierciedlając istniejące nierówności władzy w społeczeństwie ogólnie. Ta dynamika może potencjalnie utrwalać centralizację i koncentrację władzy w rękach nielicznych, wbrew fundamentalnym celom dystrybucji sieci Bitcoin. Argument, że każdy może uczestniczyć w PoS, nawet na małą skalę, dołączając do pul, nie jest koniecznie silny. W sieci PoW, nawet mały uczestnik, z skromnym sprzętem, może aktywnie uczestniczyć i przyczyniać się do bezpieczeństwa i dystrybucji sieci.

### Podsumowanie

Podsumowując, górnicy wzmacniają sieć Bitcoin przed cenzurą, używając elektryczności do obliczania proof of work dla Bitcoina, i są nagradzani nowymi bitcoinami oraz opłatami transakcyjnymi. Z profesjonalizacją branży pojawiają się różni aktorzy, pełniący różne role, od tworzenia chipów po zarządzanie farmami górniczymi. Dodatkowo, finanse również interweniują, wywierając kontrolę poprzez decydowanie, kto przetrwa różne fazy rynkowe. Problem centralizacji trwa, z najbogatszymi podmiotami potencjalnie dominującymi na rynku. Jednakże, rozwijane są alternatywy na poziomie sprzętu i oprogramowania. To od każdego zależy, czy podejmie działania i przyczyni się do dystrybucji sieci. Bitcoin reprezentuje bezprecedensową okazję nie tylko pod względem wolności, ale także niezależności energetycznej. Pomimo kontrowersji dotyczących jego zużycia energii elektrycznej, Bitcoin oferuje ekonomiczną zachętę do przejścia na bardziej racjonalne i obfite wykorzystanie energii, materializując to, co wcześniej było ekologicznym ideałem.

## Cena Bitcoina a hashrate, czy istnieje korelacja?
Kopanie dla zysku czy dla sieci?

Aktualny hashrate, mimo że cena Bitcoina wynosi 30 000 dolarów w porównaniu do jego poprzedniego szczytu 69 000 dolarów, podkreśla namacalny związek między kopaniem a rzeczywistym światem. Okresy wzrostu cen (rynek byka) prowadzą do wysokiego popytu na kopanie Bitcoina i wzrostu zamówień na maszyny od producentów takich jak Avalon i Bitmain. Jednak produkcja i dostawa nie są natychmiastowe, co tworzy rozbieżność między zwiększonym popytem a późniejszą dostępnością. Może to prowadzić do dostarczenia maszyn zamówionych podczas rynku byka w spadającym rynku, podkreślając znaczącą asymetrię między niską ceną a wysokim hashrate.

Ta sytuacja ilustruje również odporność Bitcoina, często ocenianego na podstawie jego ceny. Jednak głębsza analiza zdrowia Bitcoina wymaga zbadania jego hashrate, który mierzy obliczenia na sekundę w sieci Bitcoin. Podczas gdy cena Bitcoina fluktuuje, jego koszt, związany z potrzebną energią elektryczną do obsługi maszyn górniczych, pozostaje istotny dla zrozumienia dynamiki rynku. Skupiając się na koszcie zamiast na cenie, uzyskuje się bardziej spójną perspektywę na stabilność i długoterminową żywotność Bitcoina. Ogólnie, koszt Bitcoina jest proporcjonalny do jego ceny, co pozwala lepiej zrozumieć wahania cen i przyszłe perspektywy.

Hashrate i nagroda

Kopanie ustanawia cenę minimalną dla Bitcoina, poniżej której górnicy sprzedawaliby ze stratą. Koszt kopania znacząco wpływa na cenę, jak pokazuje zakaz kopania w Chinach, gdzie hashrate i cena spadły znacząco, ale szybko się odbiły. Skupianie się wyłącznie na cenie może być mylące. Studiowanie kosztów, za pomocą kalkulatorów rentowności, oferuje bardziej zrównoważoną perspektywę. Jednak rynek może zachowywać się irracjonalnie, z górnikami zmuszonymi do sprzedaży ze stratą, potencjalnie obniżając cenę poniżej kosztów kopania. Aby ocenić zdrowie Bitcoina i jego decentralizację, można by opracować równanie uwzględniające różne czynniki, takie jak liczba węzłów i cena. Takie podejście mogłoby zapewnić bardziej zniuansowaną analizę Bitcoina w porównaniu do dyskusji opartych wyłącznie na cenie.

Kopanie dla zysku czy dla sieci?
Pytanie jest głębokie i obejmuje kilka wymiarów wydobycia Bitcoinów. Równowaga między dążeniem do zysku a przyczynianiem się do bezpieczeństwa i dystrybucji sieci Bitcoin jest ciągłym dylematem dla górników. Debata trwa w społeczności Bitcoin, z mocnymi argumentami po obu stronach.

* Wydobycie dla zysku:
  - Za: Górnicy są naturalnie przyciągani przez potencjał zysku, jaki oferuje wydobycie Bitcoinów. Inwestycja w drogie sprzęty do wydobycia może być opłacalna dzięki nagrodom za wydobycie i opłatom transakcyjnym, szczególnie gdy cena Bitcoina jest wysoka.
  - Przeciw: Dążenie do zysku może prowadzić do centralizacji mocy obliczeniowej, jeśli tylko kilka dużych firm stać na inwestycję w zaawansowany sprzęt do wydobycia. Ponadto, konsumpcja energii przez wydobycie dla zysku może mieć znaczący wpływ na środowisko.

* Wydobycie dla sieci:
  - Za: Wydobycie w celu przyczynienia się do bezpieczeństwa i decentralizacji sieci Bitcoin jest szlachetną inicjatywą. Pomaga to wzmocnić odporność sieci na cenzurę i ataki.
  - Przeciw: Bez wystarczających zachęt finansowych może być trudno dla górników kontynuować wsparcie dla sieci, szczególnie jeśli działają na stratę.

Inicjatywa Attakai podkreśla znaczenie przyczyniania się do sieci, oferując jednocześnie rozwiązania, które czynią wydobycie bardziej dostępnym i mniej szkodliwym. Możliwość wydobycia w domu, z bardziej przystępnym cenowo sprzętem i rozwiązaniami zmniejszającymi zanieczyszczenie hałasem, może pomóc zdemokratyzować wydobycie Bitcoinów. Zachęca to osoby zainteresowane Bitcoinem nie tylko do inwestowania i trzymania bitcoinów, ale także do aktywnego uczestnictwa w zabezpieczaniu sieci. Dostarczając przetestowany sprzęt oraz przewodniki do montażu i instalacji, Attakai ułatwia wejście w świat wydobycia Bitcoinów. Zachęca również do innowacji i ciągłych ulepszeń, zapraszając społeczność do przyczyniania się i dzielenia się swoimi pomysłami i doświadczeniami w celu ulepszenia wydobycia domowego. Model Attakai jest odpowiedzią na pytanie o wydobycie dla zysku czy dla sieci. To nie tylko o osiąganiu zysków, ale także o wzmacnianiu dystrybucji i bezpieczeństwa sieci Bitcoin, umożliwiając większej liczbie osób uczestnictwo w wydobyciu, naukę i zrozumienie tej kluczowej branży. Wyzwanie potencjalnego zakazu wydobycia w Europie pozostaje otwartym pytaniem. Budzi to obawy dotyczące przyszłości wydobycia Bitcoinów w regionie i potrzeby zrównoważonej regulacji, która uznaje znaczenie wydobycia dla bezpieczeństwa i żywotności sieci Bitcoin, jednocześnie adresując kwestie środowiskowe. Attakai i inne podobne inicjatywy mogą odgrywać kluczową rolę w tej debacie, pokazując, że możliwe jest wydobycie w bardziej zrównoważony i odpowiedzialny sposób, jednocześnie pozytywnie przyczyniając się do sieci Bitcoin.

## Suwerenność i regulacja
### Suwerenność przed zyskiem?
Aby zająć się kluczowym pytaniem bogactwa przez wydobycie, ważne jest rozważenie różnych perspektyw i podejść. Pytania o rentowność wydobycia są powszechne, z obawami dotyczącymi zakupu akcji w firmach takich jak Riot czy wynajmu maszyn do wydobycia w krajach o niskich kosztach energii, takich jak Islandia czy Rosja. Przed rozpoczęciem wydobycia istotne byłoby porównanie rentowności wydobycia z bezpośrednim zakupem Bitcoina. Jeśli koszt wydobycia jednego Bitcoina przewyższa koszt bezpośredniego zakupu, ogólnie mądrzejszym wyborem jest bezpośredni zakup Bitcoina. Pozwala to uniknąć wielu wyzwań i kosztów związanych z procesem wydobycia.

Jednak wydobycie oferuje unikalne sposoby zaangażowania się w ekosystem Bitcoina. Na przykład, wydobycie Bitcoina w zimie może być sprytnym sposobem na ogrzewanie domu, jednocześnie generując dochód w Bitcoinach. Inną opcją jest inwestowanie w firmy, które sprzedają sprzęt do wydobycia i przechowują oraz zarządzają maszynami w lokalizacjach o niskich kosztach energii, zapewniając tym samym dostęp do korzystnych stawek za energię elektryczną bez kłopotów z zarządzaniem sprzętem.
Pomimo tych opcji, wydobycie kryptowalut przedstawia znaczące wyzwania. Znane powiedzenie w świecie kryptowalut, "Nie twoje klucze, nie twoje Bitcoiny," znajduje podobne odzwierciedlenie w świecie wydobycia: "Nie twój hashrate, nie twoja nagroda." Historie rozczarowań i odłączonych maszyn są powszechne, przy czym wielu aktorów obiecuje wyjątkowe wyniki, ale ich nie dostarcza. Problemy z dostawą energii i awarie maszyn mogą pozostawić inwestorów bezsilnymi, z drogim sprzętem, nad którym nie mają kontroli. W tym kontekście ostrożność i głębokie zrozumienie sektora wydobycia są kluczowe przed podjęciem się tego przedsięwzięcia. Chociaż istnieją możliwości zysku, ryzyka są znaczące, a świadome i przemyślane podejście jest niezbędne do nawigacji po tym skomplikowanym i często nieprzewidywalnym polu. Dlatego dokładne badania i staranne rozważenie zalet i wad są niezbędne przed zaangażowaniem się w wydobycie Bitcoinów.
![image](assets/overview/self.png)

### Virgin Bitcoins
Wydobycie zabronione w Europie?

Tłumaczenie:
Dążenie do posiadania własnego hashrate przedstawia się jako obiecująca ścieżka w świecie wydobycia. Jednak nawigacja po tym złożonym ekosystemie wymaga ostrożnego podejścia. Branża cloud mining jest naznaczona dużą liczbą oszustw, napędzanych brakiem zrozumienia wydobycia przez wielu inwestorów. Kuszące oferty, pakowane na różne sposoby, mogą łatwo wprowadzić w błąd tych, którzy nie są dobrze poinformowani. Z drugiej strony, posiadanie własnego sprzętu do wydobycia oferuje znaczne zalety. Oprócz osobistej satysfakcji z aktywnego przyczyniania się do bezpieczeństwa sieci Bitcoin i obserwowania spadających nagród do własnego portfela, istnieje atrakcyjny aspekt "virgin bitcoins". Są to świeżo wydobyte bitcoiny, które nigdy nie zostały wydane i nie mają do nich przypisanej żadnej historii. Te bitcoiny są często uważane za bardziej wartościowe, ponieważ nigdy nie zostały "zanieczyszczone", co zapewnia pewną gwarancję przed odrzuceniem przez regulatorów lub główne platformy wymiany.
Możliwość wydobycia virgin bitcoins, unikając procedur know-your-customer (KYC), jest kolejną dodaną wartością. Wiele basenów wydobywczych nie wymaga od górników podawania swojej tożsamości, co pozwala im nabywać bitcoiny bez przechodzenia przez żmudne procesy weryfikacji tożsamości. Virgin bitcoins są postrzegane jako "czyste", bez żadnej przeszłości czy stowarzyszenia. Są one szczególnie poszukiwane przez dużych instytucjonalnych graczy, którzy mogą zagwarantować legalność swoich aktywów cyfrowych wobec organów regulacyjnych. Jednak pomimo tych zalet, kluczowe jest uświadomienie sobie, że branża wydobycia pozostaje niezwykle konkurencyjna i zmienna, a nieprzewidziane incydenty mogą zakłócić operacje wydobywcze.

W tym kontekście, wybór autonomicznego i świadomego podejścia do wydobycia wydaje się mądry. Nabycie własnego hashrate i inwestycja w osobisty sprzęt do wydobycia, przy jednoczesnej świadomości ryzyka i wyzwań, może potencjalnie zaoferować bezpieczniejszą i bardziej satysfakcjonującą ścieżkę do zdobycia virgin bitcoins, wzmacniając indywidualną suwerenność finansową przy jednoczesnym wsparciu dla ekosystemu Bitcoin jako całości.

### Wydobycie zabronione w Europie?
W kontekście potencjalnego zakazu wydobycia w Europie, dyskusje na temat regulacji stają się coraz bardziej istotne. Fluktuujący krajobraz regulacyjny może rzeczywiście mieć znaczący wpływ na branżę wydobycia Bitcoinów. Zakaz wydobycia w Europie jest wyobrażalnym scenariuszem, szczególnie biorąc pod uwagę precedensy w Chinach. Chociaż operacje wydobywcze kontynuują w Chinach pomimo zakazu, Europa mogłaby podążyć podobną ścieżką. Szerzej rozłożony hashrate w różnych regionach mógłby pomóc wzmocnić społeczność wydobywczą w Europie, umożliwiając im skuteczne przeciwdziałanie nieporozumieniom i błędnym wyobrażeniom na temat wydobycia, jego wpływu na środowisko i śladu w sieci energetycznej.
![image](assets/overview/regulation.jpg)
W obliczu kampanii takich jak te prowadzone przez Greenpeace oraz często wprowadzających w błąd danych z niektórych badań, najlepszą bronią pozostaje dokładna informacja. Istotne jest, aby informować ogół społeczeństwa i decydentów o rzeczywistości związanej z górnictwem, jego złożoności i niuansach, zamiast pozwalać im polegać na stereotypach i nieprecyzyjnych informacjach. Im więcej osób będzie świadomych, czym naprawdę jest górnictwo, tym lepiej branża może bronić się przed potencjalnie restrykcyjnymi regulacjami.
Podsumowując, pomimo ryzyka regulacyjnego i możliwości zakazu górnictwa w Europie, najpotężniejszą bronią pozostaje edukacja i informacja. Jasne i precyzyjne zrozumienie górnictwa, jego funkcjonowania i wpływu może pomóc rozwiać mity na temat branży i zwalczać dezinformację, oferując tym samym lepszy opór wobec potencjalnie szkodliwych regulacji. Inicjatywa edukowania i informowania ludzi o górnictwie, tak jak ta dyskusja, jest krokiem we właściwym kierunku, aby zapewnić zrównoważony rozwój i wzrost górnictwa w Europie i na całym świecie. Kontynuowane wysiłki w celu edukacji i informowania są niezbędne, aby zapewnić bezpieczną i prosperującą przyszłość dla branży wydobywczej Bitcoin.

## Wywiad z profesjonalistą z branży górniczej

### Za kulisami górnictwa przemysłowego - Sebastien Gouspillou

![Za kulisami górnictwa przemysłowego - Sebastien Gouspillou](https://www.youtube.com/watch?v=vYaQRLSDr5E&t=69s)

# Górnictwo domowe i ponowne wykorzystanie ciepła

## Attakai - umożliwiające i ułatwiające górnictwo domowe!

![Przedstawiamy Attakaï!](https://www.youtube.com/watch?v=gKoh44UCSnE&t=3s)

Attakai, co w japońskim oznacza "idealną temperaturę", to nazwa inicjatywy mającej na celu odkrywanie górnictwa bitcoin poprzez ponowne wykorzystanie ciepła, uruchomionej przez @ajelexBTC i @jimzap21 z Découvre Bitcoin.
Ten przewodnik po modernizacji ASIC posłuży jako podstawa do nauki więcej o górnictwie, jego działaniu i leżącej u jego podstaw ekonomii, demonstrując możliwość adaptacji koparki Bitcoin do użytku jako grzejników w domach. Oferuje to większy komfort i oszczędności, pozwalając uczestnikom otrzymywać zwrot gotówkowy non-KYC BTC na rachunku za ogrzewanie elektryczne.

Bitcoin automatycznie dostosowuje trudność wydobycia i nagradza górników za ich udział. Jednak koncentracja hashrate może stanowić ryzyko dla neutralności sieci. Wykorzystanie mocy obliczeniowej Bitcoina do rozwiązań grzewczych bezpośrednio korzysta na sieci, zwiększając dystrybucję mocy obliczeniowej.

### Dlaczego warto ponownie wykorzystać ciepło z ASIC?

Ważne jest, aby zrozumieć związek między energią a produkcją ciepła w systemie elektrycznym.

Dla inwestycji 1 kW energii elektrycznej, elektryczny grzejnik produkuje 1 kW ciepła, nie więcej, nie mniej. Nowe grzejniki nie są bardziej wydajne niż tradycyjne grzejniki. Ich zaletą jest zdolność do ciągłego i równomiernego rozprowadzania ciepła w pomieszczeniu, zapewniając większy komfort w porównaniu z tradycyjnymi grzejnikami, które zmieniają moc grzewczą i nie grzeją, generując regularne zmiany temperatury i dyskomfort.

Komputer, czy szerzej płyta elektroniczna, nie zużywa energii do wykonywania obliczeń, po prostu potrzebuje energii do przepływu przez swoje komponenty, aby funkcjonować. Zużycie energii wynika z elektrycznego oporu komponentów, co powoduje straty i generuje ciepło, znane jako efekt Joule'a.
Niektóre firmy wpadły na pomysł połączenia potrzeb obliczeniowych z potrzebami ogrzewania poprzez radiatory/serwery. Pomysł polega na rozdzielaniu serwerów firmy na małe jednostki, które mogłyby być umieszczane w domach lub biurach. Jednak ten pomysł napotyka na kilka problemów. Potrzeba serwerów nie jest związana z potrzebą ogrzewania, a firmy nie mogą elastycznie wykorzystywać możliwości obliczeniowych swoich serwerów. Istnieją również ograniczenia przepustowości, jaką mogą mieć poszczególni użytkownicy. Wszystkie te ograniczenia uniemożliwiają firmie uczynienie tych kosztownych instalacji zyskownymi lub zapewnienie stabilnej oferty serwerów online bez centrów danych, które mogą przejąć obowiązki, gdy ogrzewanie nie jest potrzebne. "Ciepło generowane przez twój komputer nie jest marnowane, jeśli potrzebujesz ogrzać swój dom. Jeśli używasz ogrzewania elektrycznego tam, gdzie mieszkasz, to ciepło z twojego komputera nie jest marnowane. Koszt wytworzenia tego ciepła za pomocą komputera jest taki sam. Jeśli masz tańszy system ogrzewania niż ogrzewanie elektryczne, to strata polega tylko na różnicy kosztów. Jeśli jest lato i używasz klimatyzacji, to jest to podwójna strata. Kopanie bitcoinów powinno odbywać się tam, gdzie jest to tańsze. Może to być tam, gdzie klimat jest zimny i gdzie ogrzewanie jest elektryczne, gdzie kopanie stanie się darmowe."
> Satoshi Nakamoto - 8 sierpnia 2010

Bitcoin i jego dowód pracy wyróżniają się tym, że automatycznie dostosowują trudność kopania w oparciu o ilość obliczeń wykonywanych przez całą sieć. Ta ilość nazywana jest hashrate i jest wyrażana w hashach na sekundę. Dzisiaj szacuje się ją na 380 eksahashy na sekundę, co stanowi 380 miliardów miliardów hashy na sekundę. Ten hashrate reprezentuje pracę, a więc ilość zużytej energii. Im wyższy hashrate, tym wyższa trudność, i odwrotnie. W ten sposób górnik Bitcoin może być aktywowany lub dezaktywowany w dowolnym momencie bez wpływu na sieć, w przeciwieństwie do radiatorów/serwerów, które muszą pozostać stabilne, aby świadczyć swoje usługi. Górnik jest nagradzany za swoją uczestnictwo, względem innych, niezależnie od tego, jak małe może być.

Podsumowując, elektryczny radiator i górnik Bitcoin oba produkują 1 kW ciepła na 1 kW zużytej energii elektrycznej. Jednak górnik otrzymuje również bitcoiny jako nagrodę. Niezależnie od ceny energii elektrycznej, ceny bitcoina, czy konkurencji w działalności kopania Bitcoin na sieci, jest to ekonomicznie bardziej korzystne, aby ogrzewać się za pomocą górnika niż elektrycznego radiatora.

### Dodana wartość dla Bitcoina

Ważne jest zrozumienie, jak kopanie przyczynia się do decentralizacji Bitcoina.
Kilka istniejących technologii zostało pomysłowo połączonych, aby ożywić konsensus Nakamoto. Ten konsensus ekonomicznie nagradza uczciwych uczestników za ich wkład w działanie sieci Bitcoin, jednocześnie zniechęcając nieuczciwych uczestników. Jest to jeden z kluczowych punktów, które pozwalają sieci istnieć w sposób zrównoważony.
Uczciwi aktorzy, ci, którzy kopią zgodnie z zasadami, konkurują ze sobą o jak największy udział w nagrodzie za produkcję nowych bloków. Ten ekonomiczny bodziec naturalnie prowadzi do pewnej formy centralizacji, ponieważ firmy decydują się specjalizować w tej lukratywnej działalności, redukując swoje koszty poprzez ekonomię skali. Ci przemysłowi aktorzy mają korzystną pozycję do zakupu i utrzymania maszyn, jak również negocjowania hurtowych stawek za energię elektryczną.

> "Na początku większość użytkowników prowadziłaby węzły sieciowe, ale w miarę jak sieć rośnie poza pewien punkt, coraz więcej zostawiano by specjalistom z farmami serwerów specjalistycznego sprzętu. Farma serwerowa potrzebowałaby tylko mieć jeden węzeł w sieci, a reszta LAN łączyłaby się z tym węzłem."
>
> - Satoshi Nakamoto - 2 listopada 2008
Niektóre podmioty posiadają znaczący procent całkowitej mocy obliczeniowej (hashrate) w dużych farmach wydobywczych. Możemy zaobserwować niedawne zimno w Stanach Zjednoczonych, gdzie znacząca część mocy obliczeniowej została wyłączona, aby przekierować energię do gospodarstw domowych z wyjątkowym zapotrzebowaniem na elektryczność. Przez kilka dni, górnicy byli ekonomicznie zachęcani do wyłączenia swoich farm, a ta wyjątkowa pogoda może być zauważona na krzywej mocy obliczeniowej Bitcoina.
Ta kwestia może stać się problematyczna i stanowi znaczące ryzyko dla neutralności sieci. Podmiot dysponujący więcej niż 51% mocy obliczeniowej mógłby łatwiej cenzurować transakcje, jeśli by tego chciał. Dlatego ważne jest, aby rozprowadzić moc obliczeniową wśród wielu podmiotów, a nie centralizowanych jednostek, które mogłyby być łatwiej przejęte przez rząd, na przykład.

**Jeśli górnicy są rozproszeni w tysiącach, a nawet milionach gospodarstw domowych na całym świecie, staje się bardzo trudno dla państwa przejąć nad nimi kontrolę.**

Kiedy miner wychodzi z fabryki, nie nadaje się do użytku jako grzejnik w domu, z powodu dwóch głównych problemów: nadmiernego hałasu i braku regulacji. Jednak te problemy można łatwo rozwiązać poprzez modyfikacje sprzętowe i programowe, umożliwiając uzyskanie znacznie cichszego minera, który może być konfigurowany i automatyzowany jak nowoczesne grzejniki elektryczne.

**Attakaï to inicjatywa edukacyjna, która uczy, jak w najbardziej opłacalny sposób przerobić Antminera S9.**

To doskonała okazja, aby uczyć się poprzez praktykę, będąc nagradzanym za udział KYC-free satoshis.

## Przewodnik zakupu używanego ASIC

![Wprowadzenie do Attakaï: Ogrzewanie za pomocą Bitcoina](https://www.youtube.com/watch?v=U_PLo59lp-g)
W tej sekcji omówimy najlepsze praktyki zakupu używanego Bitmain Antminera S9, maszyny, na której będzie oparty ten poradnik przeróbki na grzejnik. Przewodnik ten dotyczy również innych modeli ASIC, ponieważ jest to ogólny przewodnik zakupu używanego sprzętu wydobywczego.

Antminer S9 to urządzenie oferowane przez Bitmain od maja 2016 roku. Zużywa 1400W energii elektrycznej i produkuje 13,5 TH/s. Mimo że jest uważany za stary, pozostaje doskonałą opcją na rozpoczęcie wydobycia. Ponieważ został wyprodukowany w dużych ilościach, łatwo jest znaleźć części zamienne w wielu regionach świata. Ogólnie można go nabyć międzyosobowo na stronach takich jak eBay czy LeBonCoin, ponieważ profesjonalni sprzedawcy już go nie oferują ze względu na jego niższą konkurencyjność w porównaniu z nowszymi maszynami. Jest mniej wydajny niż ASIC takie jak Antminer S19, oferowany od marca 2020 roku, ale to czyni go przystępnym cenowo używanym sprzętem i bardziej odpowiednim do modyfikacji, które wykonamy.

Antminer S9 występuje w kilku wariantach (i, j), które wprowadzają drobne modyfikacje do sprzętu pierwszej generacji. Nie uważamy, aby miało to wpływać na decyzję o zakupie, i ten przewodnik działa dla wszystkich tych wariantów.

Cena ASIC zależy od wielu czynników, takich jak cena bitcoina, trudność sieci, wydajność maszyny i koszt energii elektrycznej. Dlatego trudno jest podać dokładną szacunkową cenę zakupu używanej maszyny. W lutym 2023 roku, oczekiwana cena we Francji ogólnie waha się od 100 do 200 euro, ale te ceny mogą szybko się zmieniać.

![obraz](assets/guide-achat/1.jpeg)

Antminer S9 składa się z następujących części:

- 3 płyty hashujące, które zawierają chipy produkujące moc obliczeniową.

![obraz](assets/guide-achat/2.jpeg)

- Płyta kontrolna, która zawiera slot na kartę SD, port Ethernet oraz złącza do płyt hashujących i wentylatorów. To jest mózg twojego ASIC.
![obraz](assets/guide-achat/3.jpeg)
- 3 kable danych łączące płyty hashujące z płytą sterującą.

![obraz](assets/guide-achat/4.jpeg)

- Zasilacz, który działa na 220V i może być podłączony jak zwykłe urządzenie domowe.

![obraz](assets/guide-achat/5.jpeg)

- 2 wentylatory 120mm.

![obraz](assets/guide-achat/6.jpeg)

- Męski kabel C13.

![obraz](assets/guide-achat/7.jpeg)
Przy zakupie używanej maszyny ważne jest, aby sprawdzić, czy wszystkie części są dołączone i sprawne. Podczas wymiany należy poprosić sprzedającego o włączenie maszyny, aby sprawdzić jej prawidłowe działanie. Ważne jest, aby zweryfikować, czy urządzenie włącza się poprawnie, a następnie sprawdzić łączność z internetem, podłączając kabel Ethernet i uzyskując dostęp do interfejsu logowania Bitmain za pomocą przeglądarki internetowej w tej samej lokalnej sieci. Adres IP można znaleźć, łącząc się z interfejsem routera internetowego i szukając podłączonych urządzeń. Adres ten powinien mieć następujący format: 192.168.x.x
![obraz](assets/guide-achat/8.gif)

Sprawdź także, czy domyślne dane logowania działają (nazwa użytkownika: root, hasło: root). Jeśli domyślne dane logowania nie działają, będziesz musiał zresetować maszynę.

![obraz](assets/guide-achat/9.jpeg)

Po połączeniu powinieneś być w stanie zobaczyć status każdej płyty hashującej na pulpicie nawigacyjnym. Jeśli koparka jest podłączona do puli, powinieneś zobaczyć wszystkie płyty hashujące w działaniu. Ważne jest, aby zauważyć, że koparki generują dużo hałasu, co jest normalne. Upewnij się także, że wentylatory działają prawidłowo.

Następnie możesz usunąć pulę wydobywczą poprzedniego właściciela, aby później ustawić własną. Jeśli chcesz, możesz również zbadać płyty hashujące, rozbierając maszynę. Jednak ten krok jest bardziej skomplikowany i wymaga więcej czasu oraz niektórych narzędzi. Jeśli chcesz przeprowadzić tę demontaż, możesz odnieść się do następnej części tego poradnika, która szczegółowo opisuje, jak to zrobić. Ważne jest, aby zauważyć, że koparki zbierają dużo kurzu i wymagają regularnej konserwacji. Możesz zaobserwować tę akumulację kurzu i jakość konserwacji, rozbierając maszynę.
Po przeanalizowaniu wszystkich tych punktów, możesz kupić swoją maszynę z dużym stopniem pewności. W razie wątpliwości skonsultuj się ze społecznością.

Podsumowując ten przewodnik w jednym zdaniu: **"Nie ufaj, weryfikuj."**

[Możesz również zwrócić się do profesjonalistów zajmujących się renowacją maszyn do wydobywania, takich jak nasz partner 21energy. Oferują oni przetestowane maszyny S9, oczyszczone i z już zainstalowanym oprogramowaniem BraiiinOS+. Z kodem partnerskim "decouvre" otrzymasz 10% zniżki na zakup S9, wspierając jednocześnie projekt Attakai.](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)

## Przewodnik po zakupie modyfikacji sprzętowych dla S9

![Wprowadzenie do Attakaï: ogrzewanie za pomocą Bitcoina](https://www.youtube.com/watch?v=U_PLo59lp-g)
Jako właściciel Antminera S9, prawdopodobnie wiesz, jak głośne i masywne może być to urządzenie. Jednak możliwe jest przekształcenie go w ciche i połączone ogrzewanie, wykonując kilka prostych kroków. W tej sekcji przedstawimy niezbędny sprzęt do dokonania modyfikacji.

Jeśli jesteś zręcznym majsterkowiczem i chcesz przekształcić koparkę w ogrzewanie, ten poradnik jest dla Ciebie. Chcemy Cię ostrzec, że modyfikacje dokonane na urządzeniu elektronicznym mogą stanowić ryzyko elektryczne. Dlatego niezbędne jest podjęcie wszystkich niezbędnych środków ostrożności, aby uniknąć wszelkich uszkodzeń lub obrażeń.
1. Wymień wentylatory
Oryginalne wentylatory Antminera S9 są zbyt głośne, aby używać twojego Antminera jako grzejnika. Rozwiązaniem jest wymiana ich na cichsze wentylatory. Nasz zespół przetestował kilka modeli marki Noctua i wybrał Noctua NF-A14 iPPC-2000 PWM jako najlepszy kompromis. Upewnij się, że wybierasz wersję wentylatorów 12V. Ten 140mm wentylator może wytworzyć do 1200W ciepła, utrzymując teoretyczny poziom hałasu na poziomie 31 dB. Aby zainstalować te 140mm wentylatory, będziesz potrzebować adaptera z 140mm na 120mm, który możesz znaleźć w sklepie DécouvreBitcoin. Dodamy również 140mm osłony ochronne.

![image](assets/piece/1.jpeg)
![image](assets/piece/2.jpeg)
![image](assets/piece/3.jpeg)

Wentylator zasilacza jest również dość głośny i wymaga wymiany. Polecamy Noctua NF-A6x25 PWM. Zauważ, że złącza wentylatorów Noctua nie są takie same jak oryginalne, więc będziesz potrzebować adaptera złącza, aby je podłączyć. Dwa wystarczą. Ponownie, upewnij się, że wybierasz wersję wentylatora 12V.

![image](assets/piece/4.jpeg)
![image](assets/piece/5.jpeg)

2. Dodaj mostek WIFI/Ethernet

Zamiast używać kabla Ethernet, możesz połączyć swój Antminer przez WIFI, dodając mostek WIFI/Ethernet. Wybraliśmy vonets vap11g-300, ponieważ łatwo pozwala na odebranie sygnału WIFI z twojego routera internetowego i przesłanie go do twojego Antminera przez Ethernet bez tworzenia podsieci. Jeśli posiadasz umiejętności elektryczne, możesz zasilić go bezpośrednio z zasilacza Antminera, bez potrzeby dodawania ładowarki USB. W tym celu będziesz potrzebować żeńskiego gniazda jack 5,5mmx2,1mm.

![image](assets/piece/6.jpeg)
![image](assets/piece/7.jpeg)

3. Opcjonalnie: dodaj inteligentne gniazdko
Jeśli chcesz włączać/wyłączać swojego Antminera ze swojego smartfona i monitorować jego zużycie energii, możesz dodać inteligentne gniazdko. Testowaliśmy gniazdko ANTELA w wersji 16A, kompatybilne z aplikacją smartlife. To inteligentne gniazdko pozwala na przeglądanie dziennego i miesięcznego zużycia energii i łączy się bezpośrednio z twoim routerem internetowym przez WiFi.
![image](assets/piece/8.jpeg)

Lista sprzętu i linków

* 2X Adapter 3D z 140mm na 120mm

* [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)

* [2X Osłony wentylatorów 140mm](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
* [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)
* [Cukier elektryka 2.5mm2](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
* [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
* [Opcjonalne inteligentne gniazdo ANTELA](https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1)

# Attakai - Modyfikacja oprogramowania Antminera S9

## Konfiguracja mostu WIFI/Ethernet Vonet

![Podłącz Antminera S9 do swojej sieci Wifi](https://www.youtube.com/watch?v=y4oYURBaPqg)

Aby połączyć ASIC przez WIFI, potrzebujesz urządzenia zwane mostem. Urządzenie to pozwala na odebranie sygnału WIFI z routera i przesłanie go do innego urządzenia za pomocą Ethernetu.

Wiele urządzeń może pełnić tę funkcję, ale polecamy mostek/repeater WIFI VONETS ze względu na jego wygodę.

Zasil mostek, łącząc go przez USB.

Z komputera połącz się z siecią WIFI VONETS_******, używając hasła 12345678.

![obraz](assets/software/vonet1.png)

Zaloguj się, używając nazwy użytkownika "admin" i hasła "admin".

![obraz](assets/software/vonet2.png)

Wybierz opcję Wizard.

![obraz](assets/software/vonet3.png)

Wybierz sieć WIFI, do której chcesz podłączyć swój koparkę, a następnie kliknij Next.

UWAGA: Mostek Vonet działa tylko na częstotliwości 2.4GHz. Obecnie routery zazwyczaj oferują dwie sieci WIFI, jedną na 2.4GHz i jedną na 5GHz.
![obraz](assets/software/vonet4.png)
Wpisz hasło do swojej sieci WIFI w polu "Source WIFI hotspot password". Jeśli nie chcesz używać mostka Vonet do rozszerzenia swojej sieci WIFI, zaznacz pole "Disable Hotspot". W przeciwnym razie, pozostaw je niezaznaczone.

Następnie możesz kliknąć Zastosuj.

Na koniec kliknij na reboot, aby zrestartować mostek. Potrzebuje on kilku minut na ponowne uruchomienie.

Mostek powinien połączyć się z twoim routerem i pojawić się pod nazwą "[VONETS.COM](http://vonets.com/)". Jeśli nadal nie łączy się po kilku minutach, może być konieczne odłączenie i ponowne podłączenie mostka.

Po połączeniu mostka, podłącz kabel Ethernet z mostka do twojego ASIC, a następnie podłącz ASIC do gniazdka zasilania. Następnie możesz uzyskać dostęp do interfejsu ASIC w taki sam sposób, jak gdyby był bezpośrednio połączony z routerem za pomocą Ethernetu.

## Resetowanie Antminera S9

Przed instalacją BraiinOS+, może być konieczne zresetowanie twojego S9 do ustawień fabrycznych.
Ta metoda może być stosowana między 2 minutami a 10 minutami po uruchomieniu koparki.
2 minuty po włączeniu koparki, naciśnij przycisk "Reset" na 5 sekund, a następnie go zwolnij. Koparka zostanie przywrócona do ustawień fabrycznych w ciągu 4 minut i automatycznie zrestartuje się (nie ma potrzeby jej wyłączania).

![obraz](assets/software/1.jpeg)

## Instalacja BraiinsOS+ na Antminerze S9

![Instalacja Braiins OS+ na twoim Antminerze S9](https://www.youtube.com/watch?v=luqwlvzGsO4)

Oryginalne oprogramowanie instalowane przez Antminera na ich maszynach do kopania jest ograniczone w funkcjonalności. Dlatego w tym przewodniku zainstalujemy inne oprogramowanie o nazwie BraiinsOS+. Jest to oprogramowanie stron trzecich opracowane przez pierwszy basen wydobywczy Bitcoin, które posiada więcej funkcji i pozwala na przykład modyfikować moc maszyny.

Istnieje kilka sposobów na instalację Braiins OS+ na ASIC. Możesz odnieść się do tego przewodnika, jak również do [oficjalnej dokumentacji Braiins](https://academy.braiins.com/en/braiins-os/about/).

Tutaj zobaczymy, jak łatwo zainstalować Braiins OS+ bezpośrednio na pamięci twojego Antminera za pomocą oprogramowania BOS toolbox, zastępując oryginalny system operacyjny, poprzez szczegółowe kroki poniżej.

1. Włącz swój Antminer i połącz go z twoim internetowym boxem.
2. Pobierz BOS toolbox dla Windows / Linux.
3. Rozpakuj pobrany plik i otwórz plik bos-toolbox.bat. Wybierz język, a po kilku chwilach zobaczysz to okno:

![obraz](assets/software/5.jpeg)

4. BOS toolbox pozwoli ci łatwo znaleźć adres IP twojego Antminera i zainstalować BraiinsOS+. Jeśli już znasz adres IP swojej maszyny, możesz przejść do kroku 8. W przeciwnym razie przejdź do zakładki skanowania.

![obraz](assets/software/6.jpeg)

5. Zazwyczaj, w domowych sieciach, zakres adresów IP to między 192.168.1.1 a 192.168.1.255, więc wprowadź "192.168.1.0/24" w polu zakresu IP. Jeśli twoja sieć jest inna, zmień te adresy odpowiednio. Następnie kliknij na "Start".

6. Uwaga, jeśli Antminer ma hasło, wykrycie nie zadziała. W takim przypadku najprostszym rozwiązaniem jest wykonanie resetu.

7. Powinieneś zobaczyć wszystkie Antminery w twojej sieci, które się tutaj pojawią, a adres IP to 192.168.1.37.
8. Kliknij "Wstecz", a następnie na zakładkę "Instaluj", wprowadź wcześniej znaleziony adres IP i kliknij "Start".

> Jeśli instalacja nie powiedzie się, może być konieczne wykonanie resetu i ponowna próba (patrz poprzednia sekcja).

9. Po kilku chwilach Twój Antminer uruchomi się ponownie i będziesz mógł uzyskać dostęp do interfejsu Braiins OS+ pod określonym adresem IP, tutaj 192.168.1.37, bezpośrednio w pasku adresu przeglądarki. Domyślna nazwa użytkownika to "root", a domyślne hasło nie istnieje.

## Konfiguracja BraiinsOS+

![Konfiguruj swój Antminer S9 z Braiins OS+](https://www.youtube.com/watch?v=dK0t8M8kLYg)

Będziesz musiał połączyć się z ASIC za pomocą lokalnego adresu IP urządzenia w Twojej sieci przez przeglądarkę.

Adres IP swojej maszyny możesz znaleźć za pomocą narzędzia BOS toolbox lub bezpośrednio na stronie internetowej Twojego routera.

Dane uwierzytelniające są takie same jak w oryginalnym systemie operacyjnym.

- nazwa użytkownika: root
- hasło: (brak)

Następnie zostaniesz przywitany przez pulpit nawigacyjny Braiins OS+.

### Pulpit nawigacyjny

Na tej pierwszej stronie możesz obserwować rzeczywistą wydajność swojej maszyny.

- Trzy wykresy w czasie rzeczywistym pokazujące temperaturę, hashrate i ogólny status maszyny.
- Po prawej stronie rzeczywisty hashrate, średnia temperatura chipów, szacowana efektywność w W/THs i zużycie energii.
- Poniżej prędkość wentylatora jako procent maksymalnej prędkości i liczba obrotów na minutę.

- Niżej znajdziesz szczegółowy widok każdej płyty hashującej. Średnia temperatura płyty i chipów, które zawiera, oraz napięcie i częstotliwość.
- Szczegóły dotyczące aktywnych pul miningowych w Pools.
- Status autotuningu w Tuner Status.
- Po prawej szczegóły dotyczące danych przesyłanych do puli.

### Konfiguracja

### System

### Szybkie akcje

# Attakai - Modyfikacja wentylatora

## Wymiana wentylatora zasilacza

![Wymień wentylatory, aby zmniejszyć hałas](https://www.youtube.com/watch?v=2CNGKZiveuc)

> UWAGA: Istotne jest, aby wcześniej zainstalować Braiins OS+ na swoim kopiarce lub jakiekolwiek inne oprogramowanie, które może zmniejszyć wydajność maszyny. Ten krok jest kluczowy, ponieważ w celu zmniejszenia hałasu zainstalujemy mniej wydajne wentylatory, które mogą rozpraszać mniej ciepła.

### Materiały potrzebne

- 1 wentylator Noctua NF-A6x25 PWM
- 2,5mm2 cukier elektryka

> UWAGA: Przede wszystkim, zanim zaczniesz, upewnij się, że odłączyłeś swojego kopiarza, aby uniknąć ryzyka porażenia prądem.

Najpierw usuń 6 śrub po boku obudowy, które trzymają ją zamkniętą. Po usunięciu śrub ostrożnie otwórz obudowę, aby usunąć plastikową ochronę pokrywającą komponenty.
Następnie nadszedł czas, aby usunąć oryginalny wentylator, starając się nie uszkodzić pozostałych komponentów. Aby to zrobić, należy usunąć śruby, które go utrzymują na miejscu i delikatnie odkleić białą klejową substancję otaczającą złącze. Ważne jest, aby postępować ostrożnie, aby nie uszkodzić przewodów ani złącz.
![image](assets/hardware/4.jpeg)

Po usunięciu oryginalnego wentylatora zauważysz, że złącza nowego wentylatora Noctua nie pasują do tych w oryginalnym wentylatorze. Rzeczywiście, nowy wentylator ma 3 przewody, w tym żółty przewód, który umożliwia kontrolę prędkości. Jednak w tym konkretnym przypadku ten przewód nie będzie używany. Aby podłączyć nowy wentylator, zaleca się więc użycie specjalnego adaptera. Ważne jest jednak zauważenie, że czasami ten adapter może być trudny do znalezienia.

![image](assets/hardware/5.jpeg)

Jeśli nie masz tego adaptera, nadal możesz kontynuować podłączanie nowego wentylatora, używając kostki elektrycznej. Aby to zrobić, będziesz musiał przeciąć kable starego i nowego wentylatora.

![image](assets/hardware/6.jpeg)
![image](assets/hardware/7.jpeg)

Na nowym wentylatorze użyj noża i ostrożnie przetnij kontury głównej osłony na 1cm, nie przecinając osłon przewodów pod spodem.

![image](assets/hardware/8.jpeg)

Następnie, ciągnąc główną osłonę w dół, przetnij osłony czerwonego i czarnego kabla w ten sam sposób co wcześniej. I przetnij żółty kabel równo z osłoną.

![image](assets/hardware/9.jpeg)

Na starym wentylatorze delikatniejsze jest przecięcie głównej osłony bez uszkodzenia osłon czerwonego i czarnego przewodu. W tym celu użyliśmy igły, którą wsunęliśmy między główną osłonę a czerwone i czarne przewody.

![image](assets/hardware/10.jpeg)
![image](assets/hardware/11.jpeg)

Po odsłonięciu czerwonych i czarnych przewodów, ostrożnie przetnij osłony, aby nie uszkodzić przewodów elektrycznych.

![image](assets/hardware/12.jpeg)

Następnie połącz przewody za pomocą kostki, czarny z czarnym, a czerwony z czerwonym. Możesz także dodać taśmę izolacyjną.

![image](assets/hardware/13.jpeg)
![image](assets/hardware/14.jpeg)
Po wykonaniu połączenia nadszedł czas, aby zainstalować nowy wentylator Noctua z kratką i starymi śrubami. Nowe śruby w pudełku zostaną wykorzystane później. Upewnij się, że umieszczasz go we właściwej orientacji. Zauważysz strzałkę po jednej stronie wentylatora, wskazującą kierunek przepływu powietrza. Ważne jest, aby umieścić wentylator tak, aby ta strzałka wskazywała do wewnątrz obudowy. Następnie ponownie podłącz wentylator.
![image](assets/hardware/15.jpeg)
![image](assets/hardware/16.jpeg)

> Opcjonalnie: Jeśli znasz się na elektryce, możesz bezpośrednio dodać żeńskie złącze jack 5,5mm do wyjścia zasilania 12V, które bezpośrednio zasili mostek Wi-Fi Vonet. Jednakże, jeśli nie jesteś pewien swoich umiejętności elektrycznych, najlepiej jest użyć złącza USB z ładowarką typu smartfon, aby uniknąć ryzyka zwarcia lub uszkodzenia elektrycznego.

![image](assets/hardware/17.jpeg)

Po wykonaniu połączeń umieść plastikową osłonę na zewnątrz obudowy plastikowej, a nie wewnątrz.

![image](assets/hardware/18.jpeg)

Na koniec umieść z powrotem pokrywę obudowy i przykręć 6 śrub po bokach, aby wszystko było na miejscu. I oto masz, twoja obudowa zasilacza jest teraz wyposażona w nowy wentylator.

## Wymiana głównych wentylatorów
![Zamień wentylatory, aby zmniejszyć hałas](https://www.youtube.com/watch?v=2CNGKZiveuc)
> UWAGA: Konieczne jest wcześniejsze zainstalowanie Braiins OS+ na twoim kopiarce, lub innego oprogramowania zdolnego do zmniejszenia wydajności maszyny. Ten krok jest kluczowy, ponieważ w celu zmniejszenia hałasu zainstalujemy mniej mocne wentylatory, które będą rozpraszać mniej ciepła.

![obraz](assets/hardware/cover.jpeg)

### Wymagane materiały

- 2 sztuki adaptera 3D 140mm na 120mm
- 2 wentylatory Noctua NF-A14 iPPC-2000 PWM
- 2 kratki wentylatora 140mm

> UWAGA: Przede wszystkim, przed rozpoczęciem, upewnij się, że odłączyłeś swojego kopiarza, aby uniknąć ryzyka porażenia prądem.

1. Najpierw odłącz wentylatory i odkręć je.

![obraz](assets/hardware/19.jpeg)

2. Złącza nowych wentylatorów Noctua nie pasują do oryginalnych, ale nie martw się! Weź swój nóż i ostrożnie przetnij małe plastikowe zaczepy, aby złącza idealnie pasowały do twojego kopiarza.

![obraz](assets/hardware/20.jpeg)
![obraz](assets/hardware/21.jpeg)
3. Czas zainstalować części 3D!
Przymocuj je po obu stronach kopiarza, używając śrub, które wyjąłeś z wentylatorów. Wkręć je, aż główka śruby będzie równa z częścią 3D i będzie solidnie na miejscu. Uważaj, aby nie dokręcić zbyt mocno, ponieważ możesz zdeformować część, a jedna ze śrub może dotknąć kondensatora!

![obraz](assets/hardware/22.jpeg)

4. Teraz przejdźmy do wentylatorów.

Przymocuj je do części 3D, używając śrub dostarczonych w pudełku. Zwróć uwagę na kierunek przepływu powietrza, strzałki na bokach wentylatorów wskażą kierunek do śledzenia. Idź od strony portu Ethernet do drugiej strony. Zobacz zdjęcie poniżej.

![obraz](assets/hardware/23.jpeg)
![obraz](assets/hardware/24.jpeg)
![obraz](assets/hardware/25.jpeg)

5. Ostatni krok: podłącz wentylatory i przymocuj kratki na górze, używając śrub, które nie były używane w pudełku wentylatora zasilacza. Masz tylko 4 z nich, ale 2 na kratkę w przeciwnych rogach będą wystarczające. Możesz również poszukać podobnych śrub w sklepie z narzędziami, jeśli jest to konieczne.

![obraz](assets/hardware/26.jpeg)
![obraz](assets/hardware/27.jpeg)

Czekając, aż będziemy mogli zaoferować bardziej stylową obudowę dla twojego nowego ogrzewacza, możesz przymocować obudowę i zasilacz za pomocą opasek kablowych elektryka.

![obraz](assets/hardware/28.jpeg)

I na koniec, podłącz mostek Vonet do portu Ethernet i jego zasilanie.

![obraz](assets/hardware/29.jpeg)

I to wszystko, gratulacje! Właśnie wymieniłeś całą mechaniczną część swojego kopiarza. Teraz powinieneś słyszeć znacznie mniej hałasu.

# Attakai - Konfiguracja

## Dołączanie do puli wydobywczej

![Dołączanie do puli wydobywczej z Antminerem S9](https://www.youtube.com/watch?v=wM-dRog6mls&t=166s)
Można sobie wyobrazić basen wydobywczy jako kooperatywę rolniczą. Rolnicy łączą swoją produkcję, aby zmniejszyć zmienność podaży i popytu, a tym samym uzyskać bardziej stabilny dochód dla swojej działalności. Basen wydobywczy działa w ten sam sposób, przy czym wspólnym zasobem są hashe. Rzeczywiście, odkrycie pojedynczego ważnego hasha pozwala na stworzenie bloku i wygranie nagrody początkowej (coinbase) czyli obecnie 6,25 BTC plus opłaty transakcyjne zawarte w bloku. Jeśli kopiemy samodzielnie, nagroda przysługuje nam tylko wtedy, gdy znajdziemy blok. Konkurując z wszystkimi innymi górnikami na planecie, miałbyś bardzo małe szanse na wygranie tej loterii i nadal musiałbyś płacić opłaty związane z używaniem twojego koparki bez żadnej gwarancji sukcesu. Baseny wydobywcze rozwiązują ten problem, łącząc moc obliczeniową wielu (tysięcy) górników i dzieląc ich nagrody na podstawie procentowego udziału w hashrate basenu, gdy zostanie znaleziony blok. Aby zobrazować swoje szanse na samodzielne wydobycie bloku, możesz użyć tego narzędzia. Wprowadzając informacje dla Antminera S9, możemy zobaczyć, że szanse na znalezienie hasha, który pozwala na stworzenie bloku, wynoszą 1 na 24,777,849 dla każdego bloku lub 1 na 172,068 na dzień. Średnio (przy stałym hashrate i trudności), znalezienie bloku zajęłoby 471 lat.

Jednakże, ponieważ wszystko w Bitcoinie opiera się na prawdopodobieństwie, czasami zdarza się, że samotni górnicy są nagradzani za podjęcie tego ryzyka: Solo Bitcoin Miner Solves Block With Hash Rate of Just 10 TH/s, Beating Extremely Unlikely Odds – Decrypt

Jeśli lubisz ryzyko, możesz spróbować, ale nasz przewodnik nie będzie skupiał się w tym kierunku. Zamiast tego, skoncentrujemy się na basenie wydobywczym, który najlepiej odpowiada naszym potrzebom tworzenia systemu ogrzewania.
Rozważania przy wyborze basenu wydobywczego dotyczą działania systemu nagród basenu, które może się różnić, jak również minimalnej kwoty przed możliwością wypłaty nagród na adres. Na przykład, Braiins, który oferuje oprogramowanie, o którym tutaj mówimy, oferuje również basen. Ten basen ma system nagród zwany "Score", który zachęca górników do długotrwałego kopania. Udział obejmuje czynnik czasu pracy wyrażony jako "scoring hashrate". W naszym przypadku, gdzie chcemy system ogrzewania, który może być włączony tylko przez kilka minut, to nie jest idealny system nagród. Preferujemy system nagród, który daje nam równą nagrodę za każdy udział. Dodatkowo, minimalna kwota wypłaty dla Braiins Pool wynosi 100 000 sats i On-Chain. Więc tracimy kilka sats na opłatach transakcyjnych i część naszej nagrody może być zablokowana, jeśli nie wydobędziemy wystarczająco dużo podczas zimy.

Model nagród, który nas interesuje, to PPS, co oznacza "płatność za udział". Oznacza to, że górnik otrzyma nagrodę za każdy ważny udział. Istnieje również wariant tego systemu, FPPS (Full Pay Per Share), który nie tylko dzieli nagrodę początkową, ale także opłaty transakcyjne zawarte w bloku. Baseny wydobywcze, które polecamy do połączenia z twoim systemem wydobywczym/ogrzewaniem to Linecoin Pool (FPPS) i Nicehash (PPS).

- Nicehash: Zaletą Nicehash jest to, że wypłata może być dokonana za pomocą Lightning z minimalnymi opłatami. Dodatkowo, minimalna kwota wypłaty to 2000 sats. Wadą jest to, że Nicehash używa swojego hashrate dla najbardziej opłacalnego blockchaina, nie dając naprawdę kontroli użytkownikowi, więc może niekoniecznie przyczyniać się do hashrate Bitcoin.
- Linecoin: Przewagą Linecoin jest liczba oferowanych funkcji, takich jak szczegółowy pulpit nawigacyjny, możliwość dokonywania wypłat za pomocą Paynym (BIP 47) dla lepszej ochrony prywatności, oraz integracja bota Telegram oraz bezpośrednio konfigurowalnych automatyzacji w aplikacji mobilnej. Ten pool kopie tylko bloki Bitcoin, ale minimalna kwota do wypłaty pozostaje wysoka - 100 000 satoshi. Przyjrzymy się interfejsowi jednego z tych pooli bardziej szczegółowo w przyszłym artykule.
Aby skonfigurować pool w Braiins OS+, musisz utworzyć konto w jednym z wybranych przez siebie pooli. Tutaj weźmiemy przykład Linecoin:

![obraz](assets/software/19.jpeg)

Po utworzeniu konta kliknij na Connect To Pool

Następnie skopiuj adres Stratum i swoją nazwę użytkownika:

![obraz](assets/software/20.jpeg)

Teraz możesz wrócić do interfejsu Braiins OS+, aby wprowadzić te dane. W przypadku hasła, możesz zostawić pole puste.

![obraz](assets/software/21.jpeg)
## Optymalizacja wydajności Twojego Antminer S9
![Optymalizacja wydajności Twojego Antminer S9 z auto-tuningiem](https://www.youtube.com/watch?v=yh8U9Ay1i-E&t=277s)

Zarówno podkręcanie (overclocking), jak i auto-tuning polegają na dostosowywaniu częstotliwości na płytach haszujących, aby poprawić wydajność ASIC. Różnica między nimi polega na złożoności tych ustawień częstotliwości.

Podkręcanie to prosta regulacja, która polega na zwiększeniu częstotliwości na płytach haszujących, aby zwiększyć szybkość haszowania maszyny. Z kolei underclocking polega na obniżeniu częstotliwości zegara układu scalonego poniżej jego nominalnej częstotliwości. Poprzez obniżenie częstotliwości zegara ASIC przez underclocking, redukowana jest również generowana przez sprzęt ciepło. Pozwala to na zmniejszenie prędkości wentylatorów wymaganych do chłodzenia ASIC, ponieważ nie muszą one pracować tak ciężko, aby utrzymać odpowiednią temperaturę. Obniżając prędkość wentylatorów, redukowany jest również hałas generowany przez ASIC. Może to być szczególnie przydatne dla użytkowników, którzy używają ASIC w domu i chcą zminimalizować zakłócenia hałasem spowodowane przez sprzęt do kopania.

Braiins OS+ wspiera podkręcanie, underclocking ASICów oraz auto-tuning. Pozwala użytkownikom elastycznie dostosować częstotliwość zegara ich sprzętu, aby maksymalizować wydajność lub oszczędzać energię zgodnie z ich preferencjami.

### Optymalizacja wydajności Twojego Antminer S9 z auto-tuningiem

Przed 2018 rokiem, górnicy mieli dwie drogi do uzyskania przewagi w swojej działalności: znalezienie elektryczności w rozsądnej cenie i kupowanie bardziej wydajnego sprzętu. Jednak w 2018 roku odkryto nowy postęp w dziedzinie oprogramowania i firmware do kopania, zwany AsicBoost. Ta technika pozwala górnikom na obniżenie kosztów o około 13% poprzez modyfikację firmware działającego na ich urządzeniach.
Dziś istnieje nowy postęp w sektorze oprogramowania i firmware do kopania nazywany auto-tuningiem, który oferuje jeszcze większą przewagę niż AsicBoost. ASIC składają się z wielu małych chipów komputerowych, które wykonują haszowanie. Te chipy są wykonane z krzemu, tego samego elementu szeroko używanego w półprzewodnikach i innych komponentach mikroelektronicznych. Kluczowe jest zrozumienie, że nie wszystkie chipy krzemowe są identyczne, każdy może nieznacznie różnić się swoimi właściwościami elektrycznymi. Producenci sprzętu są tego świadomi i publikują specyfikacje wydajności swoich maszyn do kopania na podstawie dolnej granicy ich tolerancji. Innymi słowy, producenci znają częstotliwość, która najlepiej działa dla przeciętnych chipów i używają tej częstotliwości jednolicie dla wszystkich chipów w maszynie.
To ustanawia górną granicę dla szybkości hashowania, jaką może osiągnąć maszyna. Autotuning to proces, w którym algorytmy oceniają optymalne częstotliwości dla hashowania chip po chipie, zamiast traktować całą maszynę jako pojedynczą jednostkę. Oznacza to, że chip o wyższej jakości, który może wykonać więcej hashy na sekundę, otrzyma wyższą częstotliwość, a chip o niższej jakości, który może wykonać stosunkowo mniej hashy, otrzyma niższą częstotliwość. Autotuning na poziomie chipa to w zasadzie sposób na optymalizację wydajności ASIC za pomocą oprogramowania i firmware'u działającego na nim.

Końcowym rezultatem jest wyższa szybkość hashowania na wat energii elektrycznej, co oznacza większe marże zysku dla górników. Powodem, dla którego maszyny nie są dystrybuowane z tego typu oprogramowaniem, jest to, że zróżnicowanie maszyn jest niepożądane, ponieważ klienci chcą dokładnie wiedzieć, co otrzymują, więc sprzedaż produktu, który nie ma spójnej i przewidywalnej wydajności z jednej maszyny na drugą, jest złym pomysłem dla producentów. Ponadto, autotuning na poziomie chipa wymaga znacznych zasobów rozwojowych, ponieważ jest skomplikowany w implementacji. Producenci już wydają dużo zasobów na rozwijanie własnych firmware'ów. Istnieją rozwiązania programowe, które pozwalają na autotuning, takie jak Braiins OS+. Oprócz poprawy wydajności ASIC nawet o 20%.

## Kontrolowanie Antminera S9 ze smartfona

### Tworzenie skrótów w iOS

![Kontrolowanie Antminera S9 za pomocą smartfona](https://www.youtube.com/watch?v=OsKmdB2iw88&t=60s)