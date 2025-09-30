---
name: Wprowadzenie do Bitcoin Mining
goal: Zrozumienie funkcjonowania branży Mining poprzez praktyczne ćwiczenie ponownego wykorzystania układów ASIC.
objectives: 

  - Zrozumienie teorii stojącej za Mining
  - Zrozumieć branżę Mining
  - Przekształć S9 w grzejnik
  - Mój pierwszy Satoshi

---

# Pierwsze kroki w Mining!


W tym szkoleniu zagłębimy się w branżę Mining, aby zdemistyfikować ten złożony temat! Szkolenie jest dostępne dla każdego i nie wymaga żadnych początkowych inwestycji.


Pierwsza część będzie miała charakter teoretyczny, w której Ajelex i ja przeprowadzimy dogłębną dyskusję na różne tematy związane z Mining. Pomoże nam to lepiej zrozumieć tę branżę oraz związane z nią kwestie gospodarcze i geopolityczne.

W drugiej części zajmiemy się praktycznym przypadkiem. Rzeczywiście, dowiemy się, jak przekształcić używany S9 Miner w domowy system grzewczy! Za pomocą pisemnych przewodników i filmów pokażemy i wyjaśnimy wszystkie kroki, aby osiągnąć to w swoim domu :)


Dzięki temu filmowi mamy nadzieję pokazać, że branża Mining jest bardziej złożona, niż się wydaje, a jej badanie pomaga zniuansować związaną z nią debatę ekologiczną!

Jeśli potrzebujesz pomocy z konfiguracją, grupa Telegram została stworzona dla studentów, a wszystkie niezbędne komponenty można znaleźć na naszej platformie e-commerce!


+++

# Wprowadzenie


<partId>a99dc130-3650-563f-8d42-a0b5160af0ab</partId>


## Przegląd kursu


<chapterId>7ad1abeb-a190-5c85-8bff-44df71331e4d</chapterId>


Witamy w kursie MIN201: Wprowadzenie do Mining. Ajelex, Jim i Rogzy z przyjemnością poprowadzą Cię przez pierwsze kroki w tej branży. Mamy nadzieję, że spodoba ci się kurs i rozpoczniesz domową przygodę z Mining!


Szkolenie to przenosi w samo serce branży Bitcoin Mining, zapewniając zarówno wiedzę teoretyczną, jak i praktyczną. Niezależnie od tego, czy jesteś początkującym, czy już zaznajomionym z tematem, ten kurs pomoże Ci zrozumieć ekonomiczne i techniczne aspekty Mining, jednocześnie realizując praktyczny projekt zmiany przeznaczenia ASIC do ogrzewania domu.


**Sekcja 2: Wszystko o Mining**

W tej sekcji przedstawimy kompleksowe zrozumienie Bitcoin Mining. Omówimy techniczne funkcjonowanie Mining, jego rolę w protokole Bitcoin oraz jego implikacje gospodarcze i geopolityczne. Przeanalizujemy również złożony związek między ceną Bitcoin a Hashrate, a także kwestie związane z suwerennością i regulacjami w branży.


**Sekcja 3: Domowy Mining i ponowne wykorzystanie ciepła**

Następnie zajmiemy się praktycznym zastosowaniem koncepcji Attakai, która ma na celu demokratyzację domowego Mining poprzez przekształcenie używanych koparek S9 w domowe urządzenia grzewcze. Dowiesz się, jak kupić i zmodyfikować używany ASIC, przygotowując jednocześnie niezbędny sprzęt do modyfikacji sprzętu.


**Sekcja 4: Attakai - Modyfikowanie oprogramowania Antminer S9**

Tutaj dowiesz się, jak skonfigurować Antminer S9 do użytku domowego. Przeprowadzimy Cię przez konfigurację mostu Wi-Fi/Ethernet, resetowanie urządzenia, instalację BraiinsOS+ i optymalizację pod kątem Mining.


**Sekcja 5: Attakai - Modyfikacje wentylatorów**

Aby zoptymalizować Antminer S9 do użytku jako dodatkowy grzejnik, w tej sekcji dowiesz się, jak wymienić wentylatory Supply i wentylatory główne. Modyfikacje te są niezbędne do zmniejszenia hałasu i poprawy wydajności termicznej urządzenia.


**Sekcja 6: Attakai - Konfiguracja**

Na koniec dowiesz się, jak dołączyć do Mining pool i zoptymalizować wydajność Antminer S9. Dowiesz się, jak osiągnąć optymalną wydajność energetyczną i skutecznie wydobywać swoje pierwsze satoshi.


Gotowi na odkrycie świata Bitcoin Mining i podjęcie praktycznego wyzwania Attakai? Zaczynajmy!



# Wszystko, co musisz wiedzieć o Mining


<partId>aa99ef2c-da29-5317-a533-2ffa4f66f674</partId>


## Wyjaśnienie Mining


<chapterId>36a82de7-87ee-5e7a-b69e-48fc30030447</chapterId>


### Wyjaśnienie Mining: analogia do puzzli


Aby wyjaśnić koncepcję Mining w uproszczony sposób, można użyć odpowiedniej analogii: układanki. Podobnie jak puzzle, Mining jest złożonym zadaniem do wykonania, ale łatwym do zweryfikowania po jego zakończeniu. W kontekście Bitcoin Mining górnicy starają się szybko rozwiązać cyfrową łamigłówkę. Pierwszy Miner, który rozwiąże łamigłówkę, przedstawia swoje rozwiązanie całej sieci, która może następnie łatwo zweryfikować jego poprawność. Pomyślna weryfikacja umożliwia Miner zatwierdzenie nowego bloku i dodanie go do łańcucha Bitcoin Timechain. W uznaniu ich pracy, która wiąże się ze znacznymi kosztami, Miner jest nagradzany określoną liczbą bitcoinów. Nagroda ta służy jako zachęta finansowa dla górników do kontynuowania pracy polegającej na walidacji transakcji i zabezpieczaniu sieci Bitcoin.


![image](assets/en/001.webp)


Początkowo w sieci Bitcoin przyznawana nagroda wynosiła 50 bitcoinów co dziesięć minut, równolegle do odkrywania bloku średnio co dziesięć minut przez górników. Nagroda ta podlega Halving co 210 000 bloków, mniej więcej co cztery lata. Wynagrodzenie to służy jako silna zachęta do zachęcania górników do udziału w procesie Mining pomimo kosztów energii. Bez nagrody energochłonny Mining zostałby porzucony, zagrażając bezpieczeństwu i stabilności całej sieci Bitcoin.

Obecna nagroda Mining jest dwojaka. Z jednej strony obejmuje tworzenie nowych bitcoinów, które początkowo spadło z 50 bitcoinów co dziesięć minut do 6,25 bitcoinów dzisiaj (2023). Z drugiej strony obejmuje opłaty transakcyjne lub opłaty Mining od transakcji, które Miner zdecyduje się uwzględnić w swoim bloku. Kiedy dokonywana jest transakcja Bitcoin, uiszczane są opłaty transakcyjne. Opłaty te funkcjonują jako rodzaj aukcji, w której użytkownicy wskazują, ile są skłonni zapłacić, aby ich transakcja została uwzględniona w następnym bloku. Aby zmaksymalizować swoją nagrodę, górnicy, działając we własnym interesie, wybierają najbardziej dochodowe transakcje do uwzględnienia w swoim bloku, biorąc pod uwagę ograniczoną dostępną przestrzeń. W ten sposób nagroda Mining składa się zarówno z generowania nowych bitcoinów, jak i opłat transakcyjnych, zapewniając ciągłą zachętę dla górników i zapewniając długowieczność i bezpieczeństwo sieci Bitcoin.


### Górnicy i ich narzędzia: Mining


Proces Mining polega na znalezieniu prawidłowego Hash, który jest akceptowalny dla sieci Bitcoin. Raz obliczony i znaleziony Hash jest nieodwracalny, podobnie jak ziemniaki zamieniane w tłuczone ziemniaki. Weryfikuje on pewną funkcję bez możliwości powrotu. Górnicy, konkurując ze sobą, używają maszyn do obliczania tych hashy. Chociaż teoretycznie możliwe jest ręczne znalezienie tego Hash, złożoność operacji czyni tę opcję niewykonalną. Komputery, zdolne do szybkiego wykonywania tych obliczeń, są zatem używane, zużywając znaczną ilość energii elektrycznej.


Na początku dominowała era CPU, w której górnicy wykorzystywali swoje komputery osobiste do Bitcoin Mining. Odkrycie zalet GPU (kart graficznych) w tym zadaniu stanowiło punkt zwrotny, znacznie zwiększając Hashrate i zmniejszając zużycie energii. Postęp nie zatrzymał się na tym, wraz z późniejszym wprowadzeniem układów FPGA (programowalnych macierzy bramek). FPGA posłużyły jako platforma do rozwoju układów ASIC (układów scalonych specyficznych dla aplikacji).


![image](assets/en/002.webp)


Układy ASIC to układy porównywalne z układami CPU, jednak zostały one opracowane w celu wykonywania tylko jednego określonego typu obliczeń w możliwie najbardziej wydajny sposób. Innymi słowy, procesor jest w stanie wykonać wiele różnych typów obliczeń, nie będąc szczególnie zoptymalizowanym pod kątem jednego lub drugiego typu obliczeń, podczas gdy ASIC będzie w stanie wykonać tylko jeden typ obliczeń, ale bardzo wydajnie. W przypadku układów ASIC Bitcoin są one przeznaczone do obliczania algorytmu SHA256.

Obecnie górnicy używają wyłącznie układów ASIC dedykowanych tej operacji, zoptymalizowanych pod kątem testowania maksymalnej liczby kombinacji przy jak najmniejszym zużyciu energii i tak szybko, jak to możliwe. Komputery te, niezdolne do wykonywania zadań innych niż Bitcoin Mining, są namacalnym świadectwem ciągłej ewolucji i rosnącej specjalizacji branży Bitcoin Mining. Ta ciągła ewolucja odzwierciedla wewnętrzną dynamikę Bitcoin, gdzie dostosowanie trudności zapewnia produkcję bloku co dziesięć minut, pomimo wykładniczego wzrostu wydajności Mining.


Aby zilustrować intensywność tego procesu, rozważmy typowy Miner zdolny do osiągnięcia 14 TeraHash na sekundę lub 14 bilionów prób w każdej sekundzie, aby znaleźć prawidłowy Hash. W skali sieci Bitcoin osiągamy teraz około 300 ExaHash na sekundę, podkreślając zbiorową moc zmobilizowaną w Bitcoin Mining.


### Dostosowanie trudności


Regulacja trudności jest kluczowym mechanizmem w działaniu sieci Bitcoin, zapewniając, że bloki są wydobywane średnio co 10 minut. Czas ten jest średnią, ponieważ proces Mining jest w rzeczywistości grą prawdopodobieństwa, podobną do rzucania kośćmi w nadziei na uzyskanie liczby niższej niż liczba określona przez trudność. Co 2016 bloków sieć dostosowuje trudność Mining w oparciu o średni czas wymagany do wydobycia poprzednich bloków. Jeśli średni czas jest dłuższy niż 10 minut, trudność jest zmniejszana i odwrotnie, jeśli średni czas jest krótszy, trudność jest zwiększana. Ten mechanizm regulacji zapewnia, że czas Mining dla nowych bloków pozostaje stały w czasie, niezależnie od liczby górników lub ogólnej mocy obliczeniowej sieci. Właśnie dlatego Bitcoin Blockchain jest również nazywany Timechain.


![image](assets/en/003.webp)



- Przykład z Chin:

Przypadek Chin doskonale ilustruje ten trudny mechanizm dostosowawczy. Dzięki obfitej i taniej energii Chiny były głównym globalnym centrum Bitcoin Mining. W 2021 r. kraj ten nagle zakazał Bitcoin Mining na swoim terytorium, co spowodowało ogromny spadek Hashrate w globalnej sieci Bitcoin, o około 50%. Ten gwałtowny spadek mocy Mining mógł poważnie zakłócić działanie sieci Bitcoin poprzez wydłużenie średniego czasu bloku Mining. Jednak mechanizm dostosowania trudności zadziałał, zmniejszając trudność Mining, aby zapewnić, że częstotliwość bloków Mining pozostanie na średnim poziomie 10 minut. Ten przypadek pokazuje skuteczność i odporność mechanizmu dostosowywania trudności Bitcoin, który zapewnia stabilność i przewidywalność sieci, nawet w obliczu nagłych i znaczących zmian w globalnym krajobrazie Mining.


### Ewolucja maszyn Bitcoin Mining


Jeśli chodzi o ewolucję maszyn Bitcoin Mining, należy zauważyć, że kontekst jest bardziej zorientowany na tradycyjny model biznesowy. Górnicy zarabiają na walidacji bloków, co jest zadaniem o stosunkowo niskim prawdopodobieństwie sukcesu. Obecnie używany model, Antminer S9, mimo że jest starszym modelem wprowadzonym na rynek około 2016 roku, nadal znajduje się w obiegu na rynku wtórnym, handlując za około 100-200 euro. Jednak cena maszyn Mining różni się w zależności od wartości Bitcoin, a nowszy model, Antminer S19, jest obecnie szacowany na około 3000 euro.


W obliczu ciągłego postępu technologicznego w dziedzinie Mining, profesjonaliści muszą zająć strategiczną pozycję. Branża Mining podlega ciągłym innowacjom, czego dowodem jest niedawna premiera wersji J modelu S19 i przewidywana premiera modelu S19 XP, oferującego znacznie wyższe możliwości Mining. Co więcej, ulepszenia nie są związane wyłącznie z surową wydajnością maszyn. Na przykład nowy model S19 XP wykorzystuje system chłodzenia Liquid, modyfikację techniczną, która pozwala na znaczną poprawę efektywności energetycznej. Chociaż innowacje pozostają niezmienne, przyszły wzrost wydajności będzie prawdopodobnie mniejszy w porównaniu do tych obserwowanych do tej pory, ze względu na osiągnięcie pewnego progu innowacji technologicznych.


![image](assets/en/004.webp)


Podsumowując, branża Bitcoin Mining nadal się dostosowuje i rozwija, a gracze branżowi muszą przewidywać malejący wzrost wydajności w przyszłości i odpowiednio dostosowywać swoje strategie. Przyszłe postępy technologiczne, choć nadal obecne, prawdopodobnie będą miały miejsce na mniejszą skalę, odzwierciedlając rosnącą dojrzałość sektora.


## Przemysł Mining


<chapterId>0896dfc1-c97e-5bec-9bf1-8c20b3388a2c</chapterId>


### Pule Mining


Obecnie Bitcoin Mining ewoluował w poważną i znaczącą branżę, z wieloma publicznie znanymi graczami i rosnącą liczbą znaczących górników. Ewolucja ta sprawiła, że Mining stał się prawie niedostępny dla małych graczy ze względu na wysokie koszty związane z zakupem nowych maszyn Mining. Rodzi to pytanie o dystrybucję Hashrate wśród różnych graczy rynkowych. Sytuacja jest złożona, ponieważ konieczne jest zbadanie zarówno dystrybucji Hashrate między różnymi firmami, jak i między różnymi pulami Mining.


![image](assets/en/005.webp)


Mining pool to grupa górników, którzy łączą swoje zasoby obliczeniowe, aby zwiększyć swoje szanse na Mining. Współpraca ta jest konieczna, ponieważ odizolowana mała maszyna Mining konkuruje z gigantami branży, zmniejszając swoje szanse na sukces do znikomego poziomu. Mining działa na zasadzie loterii, a szanse na wygranie bloku (a tym samym nagrody Bitcoin) co dziesięć minut są niezwykle niskie dla pojedynczego małego Miner. Łącząc się, górnicy mogą łączyć swoją moc obliczeniową, częściej znajdować bloki, a następnie rozdzielać nagrody proporcjonalnie do wkładu każdego Miner do puli.


Na przykład, jeśli pula znajdzie blok i wygra 6,25 bitcoinów, Miner wnoszący 1% całkowitej mocy obliczeniowej puli otrzyma 1% z 6,25 zarobionych bitcoinów. Należy jednak zauważyć, że pule Mining zazwyczaj pobierają niewielką prowizję (zwykle około 2%) na pokrycie kosztów operacyjnych spółdzielni.


### Oprogramowanie używane przez branżę


W kontekście Bitcoin Mining rola oprogramowania jest równie istotna jak sprzętu. Przykładem tego jest rola Bitmain, płodnego producenta, który opracował Antminer S9. Oprócz sprzętu Mining, branża w dużym stopniu opiera się na współpracujących pulach Mining, takich jak Brainspool, który kontroluje około 5% globalnej Hashrate sieci Bitcoin.

Podmioty w tej branży nieustannie dążą do zwiększenia wydajności poprzez sprzęt i oprogramowanie. Na przykład popularnym oprogramowaniem używanym w tym kontekście jest BrainsOS Plus. Oprogramowanie to zastępuje oryginalny system operacyjny maszyny Mining, umożliwiając bardziej wydajne wykonywanie tych samych operacji. Dzięki takiemu oprogramowaniu Miner może zwiększyć wydajność swojej maszyny o 25%. Oznacza to, że za równoważną ilość energii elektrycznej maszyna może wyprodukować dodatkowe 25% Hashrate, zwiększając w ten sposób nagrody otrzymywane przez Miner. Ta optymalizacja oprogramowania jest istotnym elementem konkurencyjności w Bitcoin Mining, pokazując znaczenie zintegrowanego podejścia, które łączy zarówno ulepszenia sprzętu, jak i oprogramowania, aby zmaksymalizować wydajność i zyski.


### Regulacja i taryfy energii elektrycznej


Jak zaobserwowano w Chinach i innych krajach, regulacje mają znaczący wpływ na Mining. Chociaż we Francji nie ma znaczących górników, regulacje i wysokie taryfy za energię elektryczną w Europie są głównymi przeszkodami. Górnicy nieustannie poszukują taniej energii elektrycznej, aby zmaksymalizować swoje zyski. Dlatego też wysokie koszty energii elektrycznej w Europie i Francji nie przyciągają górników do tych regionów.


Górnicy dążą do regionów o niskich taryfach energii elektrycznej, często w krajach wschodzących lub krajach z nadwyżkami energii. Na przykład, duża część globalnego Hashrate znajduje się w Teksasie w Stanach Zjednoczonych. Teksas ma niezależną sieć energetyczną, która nie dzieli swoich zasobów energetycznych z innymi stanami. Ta wyjątkowość często prowadzi do tego, że Teksas produkuje więcej energii elektrycznej niż jest to konieczne, aby uniknąć niedoborów, tworząc nadwyżkę. Górnicy Bitcoin wykorzystują tę nadprodukcję, zakładając działalność w Teksasie, gdzie mogą wydobywać bitcoiny po bardzo niskich stawkach za energię elektryczną w okresach nadwyżki energii. Sytuacja ta pokazuje znaczący wpływ przepisów i taryf energii elektrycznej na Bitcoin Mining, podkreślając znaczenie tych czynników w podejmowaniu przez górników decyzji dotyczących lokalizacji ich operacji Mining.


### Dokąd zmierzają górnicy i zarządzanie energią?


Podkreślając wpływ górników Bitcoin na świat energii, trajektoria jest jasna: podmioty te nieustannie poszukują źródeł taniej energii elektrycznej, często tych, które są marnowane lub niewykorzystane. Zjawisko to jest widoczne w regionach z nową infrastrukturą elektryczną, takich jak te wyposażone w najnowsze tamy hydroelektryczne.


Weźmy przykład. W kraju, który jest w trakcie budowy zapory wodnej, produkcja energii elektrycznej często rozpoczyna się przed pełnym uruchomieniem linii dystrybucyjnych. Ta luka czasowa może skutkować znacznymi kosztami i zniechęcać do inwestowania w takie projekty infrastrukturalne. Jednak górnicy Bitcoin mogą działać jako elastyczne źródło popytu, gotowe do zużycia tej "osieroconej" energii elektrycznej, pomagając w ten sposób zrównoważyć koszty infrastruktury. Wynika z tego, że nowe instalacje mogą być natychmiast opłacalne, promując tworzenie nowych źródeł energii elektrycznej. Zasada ta ma również zastosowanie na mniejszą skalę. Niezależnie od tego, czy jest to osoba fizyczna korzystająca z generatora hydroelektrycznego na małej rzece, czy gospodarstwo domowe wyposażone w panele słoneczne, nadwyżka wyprodukowanej energii elektrycznej może zostać wykorzystana do zasilania operacji Bitcoin Mining.


Na przykład we Francji nadwyżki energii elektrycznej z paneli słonecznych są wprowadzane z powrotem do sieci, a producenci otrzymują rekompensatę w postaci kredytu konsumpcyjnego od EDF. Podobnie, można sobie wyobrazić Miner działający na tej nadwyżce energii elektrycznej, wyłączający się, gdy lokalne zapotrzebowanie jest równe Supply. Chociaż może się to wydawać samolubne, przedkładając produkcję Bitcoin nad wspieranie lokalnej sieci energetycznej, przedstawia to inny aspekt: stabilizację sieci energetycznej. Złożone zarządzanie nadwyżkami energii elektrycznej, czasami nawet z powiązanymi kosztami utylizacji, można znacznie uprościć. Górnicy Bitcoin mogą wchłonąć te nadwyżki, działając jako elastyczny bufor, dostosowując popyt, a nie Supply. W świecie, w którym produkcja energii elektrycznej ze źródeł odnawialnych (niekontrolowanych) stale rośnie, górnicy mogą odgrywać kluczową rolę w zapewnianiu równowagi naszych sieci energetycznych, jednocześnie korzystając z taniej lub nadwyżki energii elektrycznej do zasilania swoich operacji Mining.


### Centralizacja Mining


Centralizacja Mining jest traktowana jako główne wyzwanie. Duzi gracze, tacy jak Foundry, dominują na rynku, co może potencjalnie prowadzić do cenzury transakcji. Ta centralizacja może również sprawić, że sieć będzie podatna na ataki, w tym atak 51%, w którym aktor lub grupa kontroluje ponad 50% mocy obliczeniowej sieci, co pozwala im kontrolować i manipulować siecią.


Podkreśla się, że gdyby kraj taki jak Stany Zjednoczone zdecydował się uregulować lub zakazać niektórych transakcji Bitcoin, mogłoby to mieć znaczący wpływ na sieć, zwłaszcza jeśli duża część mocy hashowania jest scentralizowana w tym kraju.


![image](assets/en/006.webp)


Aby zwalczyć tę centralizację, omawiane są różne strategie:



- Home Mining: Idea Home Mining opiera się na decentralizacji aktywności Mining. Zachęca ona osoby fizyczne do uczestnictwa w Mining ze swoich domów, rozpowszechniając w ten sposób Hashrate na szerszą skalę.
- Stratum V2: Protokół Stratum V2 oferuje inne podejście. W przeciwieństwie do swojego poprzednika, Stratum V2 pozwala górnikom wybrać, które transakcje mają być zawarte w wydobywanych przez nich blokach. Zdolność ta wzmacnia odporność na cenzurę i zmniejsza zdolność dużych pul Mining do zdominowania sieci. Dając większą władzę indywidualnym górnikom, protokół Stratum V2 może odegrać decydującą rolę w walce z centralizacją Hashrate.

Otwarte oprogramowanie Mining


- Otwarte oprogramowanie Mining: Jest to kolejna potencjalnie skuteczna strategia. Dzięki udostępnieniu oprogramowania Mining dla wszystkich, mali górnicy mieliby takie same możliwości jak duże firmy Mining, aby uczestniczyć w sieci Blockchain i wnosić do niej swój wkład. Takie podejście zachęciłoby do szerszej dystrybucji Hashrate, przyczyniając się tym samym do decentralizacji sieci.
- Dywersyfikacja podmiotów i geografii: Zachęcanie do udziału w kryptowalucie Mining różnych podmiotów z różnych regionów geograficznych może również okazać się skuteczne. Dywersyfikując Hashrate pod względem geograficznym, pojedynczemu podmiotowi lub krajowi trudniej jest wywierać nieproporcjonalną kontrolę lub wpływ na sieć. Takie podejście może pomóc chronić sieć przed potencjalnymi atakami i wzmocnić jej decentralizację.


Ogólny wniosek jest taki, że decentralizacja ma kluczowe znaczenie dla bezpieczeństwa i odporności sieci Bitcoin. Chociaż centralizacja może oferować korzyści w zakresie wydajności, naraża sieć na znaczne ryzyko, w tym cenzurę i ataki 51%. Inicjatywy takie jak Takai i przyjęcie nowych protokołów, takich jak Stratum V2, są ważnymi krokami w kierunku decentralizacji i ochrony sieci Bitcoin przed tymi zagrożeniami.


## Niuanse branży Mining


<chapterId>7b9ee427-316a-54e3-a2d4-4ea97839a31b</chapterId>


### Zasada Attakai


W obecnym kontekście Bitcoin Mining z modelem S9 może wydawać się skomplikowany, ale głębsza analiza otwiera drzwi do innowacyjnych alternatyw. Zasada Attakai opiera się na rozważeniu wykorzystania instalacji Mining w różnego rodzaju budynkach, takich jak szkoły czy szpitale. Główną ideą jest umieszczenie kilku maszyn Mining w różnych lokalizacjach, a tym samym ponowne wykorzystanie ciepła emitowanego przez te maszyny do ogrzewania placówek. Decydując się na bardziej wydajne modele, takie jak S19, możliwe byłoby rozproszenie działalności Mining, zwiększając w ten sposób ogólną wydajność, a jednocześnie wnosząc użyteczny wkład w społeczeństwo. Inicjatywa ta ma na celu konkurowanie z dużymi scentralizowanymi operacjami Mining poprzez wykorzystanie ciepła generowanego przez maszyny Mining w produktywny i wydajny sposób.


Inicjatywa Attakai wywodzi się z osobistego eksperymentu Mining przeprowadzonego przez dwóch przyjaciół, którzy chcieli aktywnie uczestniczyć w sieci Bitcoin. Napotkali oni poważne przeszkody, takie jak wysoki poziom hałasu sprzętu Mining, zaprojektowanego raczej do użytku przemysłowego niż domowego. Aby rozwiązać ten problem, dokonano modyfikacji sprzętowych w maszynach Mining. Bardziej wydajne i cichsze wentylatory zastąpiły oryginalny sprzęt, dzięki czemu domowy Mining stał się bardziej dostępny i mniej uciążliwy. Dodatkowo, włączenie adaptera Wi-Fi wyeliminowało potrzebę przewodowego połączenia Ethernet, jeszcze bardziej upraszczając proces domowego Mining. Zimą te zmodyfikowane koparki były używane jako źródło ogrzewania, zmieniając uciążliwość w korzyść.


Po zaprezentowaniu swojego projektu społeczności Bitcoin i zobaczeniu zainteresowania, jakie wzbudził, twórcy Attakai zdecydowali się opublikować szczegółowe przewodniki na platformie Découvre Bitcoin, umożliwiając każdemu odtworzenie ich domowego doświadczenia Mining. Teraz planują rozszerzyć tę koncepcję poza środowisko domowe. Celem jest zademonstrowanie, w jaki sposób zmodyfikowany Miner można przekształcić w cichy grzejnik pomocniczy przydatny zimą, oferując płynne przejście do drugiej części szkolenia, skoncentrowanej na praktycznym wdrożeniu tych modyfikacji, zilustrowanych filmami wyjaśniającymi. Pozostaje jednak pytanie, czy inicjatywa ta może zostać rozszerzona na większą skalę, oferując realistyczną i zrównoważoną alternatywę dla obecnych scentralizowanych struktur Mining.


![image](assets/en/007.webp)


### Ograniczenie tej decentralizacji?


Chociaż pomysł decentralizacji Mining poprzez produktywne wykorzystanie wytworzonego ciepła wydaje się obiecujący, ma pewne ograniczenia i pozostają pytania. Zakłady energochłonne, takie jak sauny i baseny, mogłyby skorzystać z tej koncepcji, wykorzystując ciepło wytwarzane przez górników do podgrzewania wody w swoich obiektach. Praktyka ta jest już wdrażana przez niektórych członków społeczności Bitcoin, którzy badają różne metody efektywnego wykorzystania ciepła generowanego przez urządzenia Mining. Na przykład, sala bankietowa może być teoretycznie ogrzewana przez trzy lub cztery górniki S19, z których każdy zużywa 3000 watów i wytwarza równoważną ilość ciepła.


Należy jednak zauważyć, że zużycie energii i produkcja ciepła są równoważne, niezależnie od tego, czy energia jest wykorzystywana przez grzejnik elektryczny czy Miner. Na każdy kilowat zużytej energii elektrycznej, ilość wyprodukowanego ciepła będzie taka sama w obu przypadkach. Różnica polega na tym, że Miner nie tylko zapewnia ciepło, ale także nagrodę Bitcoin, oferując w ten sposób ekonomiczną zachętę do korzystania z Miner zamiast zwykłego grzejnika elektrycznego. Ta dodatkowa nagroda może pomóc złagodzić obawy związane z wysokim zużyciem energii przez górników.


Kwestia długoterminowej wydajności i wykonalności wykorzystania górników Bitcoin do ogrzewania pozostaje otwarta. Bieżące innowacje w sprzęcie Mining i technologiach grzewczych mogą potencjalnie otworzyć nowe możliwości bardziej efektywnego wykorzystania ciepła generowanego przez Mining, przyczyniając się tym samym do opłacalności tego podejścia w przyszłości.


### Dlaczego warto mieć nagrody BTC?


Kwestia wynagradzania w Bitcoin, a nie w innej walucie, jest kluczowa w systemie przewidzianym przez Satoshi Nakamoto. Tworzenie Bitcoin charakteryzuje się stałym limitem 21 milionów jednostek. Celem było znalezienie sprawiedliwego sposobu dystrybucji tych nowo utworzonych jednostek. Górnicy, zapewniając swoją moc obliczeniową w celu zabezpieczenia sieci i uczynienia każdego ataku coraz bardziej kosztownym, skutecznie chronią sieć Bitcoin. W zamian za ten kluczowy wkład są oni nagradzani nowo utworzonymi bitcoinami, co ułatwia dystrybucję monet w ekosystemie.


Jest to system korzystny dla obu stron. Górnicy są nagradzani zarówno za zabezpieczanie sieci, jak i zatwierdzanie transakcji. Nowo utworzone bitcoiny stanowią zachętę do wzmocnienia bezpieczeństwa, a opłaty transakcyjne są dodatkowym dochodem za zatwierdzanie transakcji. Te dwa Elements łącznie składają się na całkowitą nagrodę za Mining. Pytanie o przyszłość Mining pojawia się ze względu na zaprogramowaną redukcję nagród Mining, Halving co cztery lata, wydarzenie znane jako "Halving". Do 2032 r. Block reward będzie mniejszy niż jeden Bitcoin, a do 2140 r. nie zostaną utworzone żadne nowe bitcoiny. W tym momencie górnicy będą polegać wyłącznie na opłatach transakcyjnych. Sieć Bitcoin będzie musiała obsługiwać dużą liczbę transakcji, z wystarczająco wysokimi opłatami, aby zapewnić rentowność Mining.


Wzrost popularności Lightning Network, który pozwala na szybkie i tanie transakcje poza głównym łańcuchem Bitcoin, rodzi pytania o przyszłość Mining. Lightning Network może potencjalnie znacznie obniżyć opłaty transakcyjne, wpływając tym samym na dochody górników. Będzie to jednak zależeć od przyjęcia i wykorzystania Lightning Network w porównaniu z główną siecią Bitcoin. W pesymistycznym scenariuszu górnikom może opłacać się wydobywać nawet ze stratą, jeśli zamortyzowali swoje koszty i mają dostęp do taniej energii elektrycznej. W bardziej optymistycznym scenariuszu opłaty transakcyjne w głównej sieci Bitcoin mogą pozostać wystarczająco wysokie, aby utrzymać rentowność Mining.


### Co powinien zawierać blok Bitcoin?


Jeśli chodzi o kwestię tego, co powinien zawierać blok Bitcoin, kluczowe znaczenie ma uwzględnienie komplementarnego charakteru różnych warstw sieci Bitcoin. Chociaż Lightning Network może umożliwić szybsze i tańsze transakcje, nadal opiera się na podstawowym Layer Bitcoin, często określanym jako "rozliczeniowy Layer", do otwierania i zamykania kanałów płatności.


Wraz z oczekiwanym rozwojem Lightning Network i wynikającym z tego wzrostem liczby otwarć i zamknięć kanałów, przestrzeń w blokach Bitcoin będzie coraz cenniejsza. Społeczność Bitcoin już teraz ceni sobie zachowanie tej przestrzeni, uznając jej nieodłączne ograniczenia. Świadomość ta doprowadziła do dyskusji na temat uzasadnionego wykorzystania przestrzeni blokowej, z obawami o "spam" na Blockchain z transakcji uznanych za nieistotne.


![image](assets/en/008.webp)


Spekuluje się na temat przyszłego wykorzystania przestrzeni blokowej, ale ogólnie przyjmuje się, że jest to rzadki zasób, który powinien być mądrze wykorzystywany. Nawet jeśli istnieje chęć jej zapełnienia, konieczne jest jej zachowanie, aby zapewnić długoterminową rentowność sieci Bitcoin, przewidując przyszły wzrost zapotrzebowania na przestrzeń blokową. Jak na każdym wolnym rynku, Supply i popyt będą regulować wykorzystanie przestrzeni blokowej. Przy ograniczonej ilości Supply interesariusze będą musieli dokonywać świadomych wyborów dotyczących wykorzystania tej cennej przestrzeni, aby zapewnić długoterminową wydajność i bezpieczeństwo sieci Bitcoin.


## Bitcoin Mining w protokole Bitcoin


<chapterId>879a66b0-c20a-56b5-aad0-8a21be61e338</chapterId>


Rola górników w sieci Bitcoin była przedmiotem intensywnej debaty podczas wojen o wielkość bloków. Chociaż górnicy są niezbędni dla bezpieczeństwa i funkcjonalności sieci, niekoniecznie posiadają ostateczną władzę w ekosystemie Bitcoin. Równowaga między górnikami, węzłami i użytkownikami końcowymi zapewnia integralność i dystrybucję sieci.


### Wojny o rozmiar bloku


Podczas wojen o wielkość bloków wielu górników sprzeciwiało się pewnym zmianom w sieci, podkreślając napięcie między różnymi podmiotami w ekosystemie. Pozostaje pytanie, jak zrównoważyć władzę wśród górników, węzłów i użytkowników, aby zapewnić długoterminowe bezpieczeństwo Bitcoin.


![image](assets/en/009.webp)


Dylemat bezpieczeństwa Bitcoin opiera się na delikatnej równowadze. Podczas gdy górnicy odgrywają kluczową rolę w walidacji i tworzeniu bloków, węzły utrzymują integralność poprzez weryfikację i walidację transakcji i bloków. Nieprawidłowy lub fałszywy blok zostanie odrzucony przez węzły, cenzurując w ten sposób Miner i zachowując bezpieczeństwo sieci. Władza jest również w posiadaniu węzłów i użytkowników sieci Bitcoin. Węzły mają moc weryfikacji i walidacji, podczas gdy użytkownicy mają moc wyboru Blockchain do użycia. Taki podział uprawnień zapewnia dystrybucję i integralność sieci Bitcoin.


Wojny o wielkość bloków ujawniły niepewność i napięcie związane z zarządzaniem siecią Bitcoin. Chociaż Bitcoin Core jest obecnie dominującą siecią, debata na temat zarządzania i zarządzania siecią trwa nadal.


Ostatecznie odpowiedzialność spoczywa na wszystkich uczestnikach sieci Bitcoin. Spadek liczby użytkowników, węzłów lub górników może osłabić sieć, zwiększając ryzyko centralizacji i podatności na ataki. Każdy podmiot przyczynia się do solidności i bezpieczeństwa sieci, wzmacniając znaczenie utrzymania równowagi władzy i odpowiedzialności.


### Siła górników


Elegancka teoria gier Satoshi Nakamoto stworzyła sytuację, w której każdy uczestnik sieci Bitcoin jest zachęcany do prawidłowego działania w celu ochrony zarówno własnych interesów, jak i interesów innych uczestników. Tworzy to równowagę, w której złe zachowanie może zostać upomniane, zwiększając w ten sposób bezpieczeństwo i stabilność całego systemu. Pomimo tej równowagi, państwa pozostają potencjalnym zagrożeniem. Jak wskazano w prezentacji Surfing Bitcoin 2022, państwa mogą próbować atakować branżę Mining, narażając sieć Bitcoin na ryzyko centralizacji i ataku. Hipotetyczne scenariusze, takie jak atak wojskowy na zakłady produkujące sprzęt Mining, podkreślają znaczenie dywersyfikacji geograficznej i przemysłowej dla odporności sieci Bitcoin.


![image](assets/en/010.webp)


Centralizacja produkcji sprzętu Mining w Chinach stwarza kolejne ryzyko. Odmowa eksportu maszyn Mining lub nagromadzenie Hashrate na potrzeby potencjalnego ataku 51% przez Chiny podkreśla potrzebę dywersyfikacji produkcji sprzętu Mining. W odpowiedzi na te zagrożenia społeczność Bitcoin aktywnie poszukuje rozwiązań. Firmy takie jak Intel rozważają produkcję sprzętu Mining w Stanach Zjednoczonych, przyczyniając się do dystrybucji produkcji. Inne inicjatywy, takie jak open-source'owy Mining Development Kit (MDK) firmy Block, mają na celu zmniejszenie monopolu na projektowanie i produkcję sprzętu Mining, umożliwiając szerszą dystrybucję Hashrate. W samym sercu tych dyskusji leży podstawowa misja Bitcoin: bycie odporną na cenzurę wartościową siecią Exchange. Społeczność Bitcoin nieustannie dąży do wzmocnienia dystrybucji, odporności na cenzurę i niestabilności sieci, odrzucając propozycje takie jak przejście na proof of stake, które nie są zgodne z tymi podstawowymi zasadami.


### Fizyczne połączenie Proof of Work vs Proof of Stake


Proof of Work (PoW) jest niezbędny, ponieważ reprezentuje fizyczne połączenie między światem rzeczywistym a Bitcoin. Chociaż bitcoiny są niematerialne, ich produkcja wymaga namacalnej energii, ustanawiając w ten sposób bezpośrednie połączenie ze światem fizycznym i rzeczywistym. To połączenie zapewnia, że produkcja i walidacja bitcoinów i bloków ma rzeczywisty koszt energii, tym samym zakotwiczając sieć Bitcoin w rzeczywistości fizycznej i zapobiegając jej całkowitej dominacji przez potężne podmioty. PoW działa jako bastion przeciwko centralizacji, zapewniając, że uczestnictwo w sieci i walidacja transakcji wymagają inwestycji w zasoby materialne. Zapobiega to monopolizacji sieci przez podmioty, które w przeciwnym razie mogłyby przejąć kontrolę bez znaczącej bariery wejścia, zapewniając w ten sposób bardziej sprawiedliwy podział władzy i wpływów w sieci Bitcoin.


![image](assets/en/011.webp)


### Ograniczenia Proof of Stake


Z drugiej strony, Proof of Stake (PoS), choć pozwala na uczestnictwo na małą skalę, nie gwarantuje równoważnej ochrony przed centralizacją. W sieci PoS ci, którzy już posiadają dużą ilość waluty, mają nieproporcjonalną władzę, odzwierciedlając istniejące nierówności władzy w całym społeczeństwie. Ta dynamika może potencjalnie utrwalić centralizację i koncentrację władzy w rękach nielicznych, co jest sprzeczne z podstawowymi celami dystrybucyjnymi sieci Bitcoin. Argument, że każdy może uczestniczyć w PoS, nawet na małą skalę, dołączając do puli, niekoniecznie jest solidny. W sieci PoW nawet niewielki uczestnik, dysponujący skromnym sprzętem, może aktywnie uczestniczyć i przyczyniać się do bezpieczeństwa i dystrybucji sieci.


### Podsumowanie


Podsumowując, górnicy wzmacniają sieć Bitcoin przed cenzurą, wykorzystując energię elektryczną do obliczania Bitcoin z Proof of Work i są nagradzani nowymi bitcoinami i opłatami transakcyjnymi. Wraz z profesjonalizacją branży pojawiają się różni gracze, odgrywający różne role, od tworzenia chipów po zarządzanie farmami Mining. Dodatkowo, finanse również odgrywają rolę, sprawując kontrolę poprzez decydowanie o tym, kto przetrwa w różnych fazach rynku. Kwestia centralizacji utrzymuje się, a najbogatsze podmioty potencjalnie dominują na rynku. Opracowywane są jednak alternatywy zarówno na poziomie sprzętu, jak i oprogramowania. To od każdej osoby zależy, czy podejmie działania i przyczyni się do dystrybucji sieci. Bitcoin stanowi niezwykłą szansę nie tylko pod względem wolności, ale także niezależności energetycznej. Pomimo kontrowersji związanych ze zużyciem energii elektrycznej, Bitcoin oferuje ekonomiczną zachętę do przejścia na bardziej racjonalne i obfite wykorzystanie energii, realizując to, co wcześniej było ekologicznym ideałem.


## Cena Bitcoin i Hashrate, korelacja?


<chapterId>e6676214-007c-5181-968e-c27536231bd6</chapterId>


### Hashrate, cena i rentowność


Obecny kurs Hash, pomimo ceny Bitcoin na poziomie 30 000 USD w porównaniu do poprzedniego szczytu na poziomie 69 000 USD, podkreśla namacalny związek między Mining a światem rzeczywistym. Okresy hossy prowadzą do wysokiego popytu na Bitcoin Mining i wzrostu zamówień maszyn od producentów takich jak Avalon i Bitmain. Jednak produkcja i dostawa nie są natychmiastowe, co powoduje niedopasowanie między zwiększonym popytem a późniejszą dostępnością. Może to prowadzić do tego, że maszyny zamówione podczas hossy zostaną dostarczone podczas bessy, podkreślając znaczną asymetrię między niską ceną a wysokim wskaźnikiem Hash.


Sytuacja ta ilustruje również odporność Bitcoin, często ocenianą na podstawie jego ceny. Jednak głębsza analiza kondycji Bitcoin wymaga zbadania jego wskaźnika Hash, który mierzy obliczenia na sekundę w sieci Bitcoin. Podczas gdy cena Bitcoin ulega wahaniom, jego koszt, związany z energią elektryczną potrzebną do obsługi maszyn Mining, pozostaje kluczowy dla zrozumienia dynamiki rynku. Koncentrując się na kosztach, a nie na cenie, uzyskuje się bardziej spójną perspektywę stabilności i długoterminowej rentowności Bitcoin. Ogólnie rzecz biorąc, koszt Bitcoin jest proporcjonalny do jego ceny, zapewniając lepsze zrozumienie wahań cen i przyszłych perspektyw.


![image](assets/en/012.webp)


### Hash stawka i nagroda


Mining może ustanowić cenę minimalną dla Bitcoin, poniżej której górnicy sprzedawaliby ze stratą. Koszt Mining znacząco wpływa na cenę, co ilustruje zakaz Mining w Chinach, gdzie wskaźnik Hash i cena znacznie spadły, ale szybko wróciły do normy. Skupianie się wyłącznie na cenie może być mylące. Badanie kosztów za pomocą kalkulatorów rentowności oferuje bardziej zrównoważoną perspektywę. Rynek może jednak zachowywać się irracjonalnie, a górnicy mogą być zmuszeni do sprzedaży ze stratą, potencjalnie obniżając cenę poniżej kosztu Mining. Aby ocenić kondycję Bitcoin i jego decentralizację, można opracować równanie uwzględniające różne czynniki, takie jak liczba węzłów i cena. Takie podejście mogłoby zapewnić bardziej zniuansowaną analizę Bitcoin w porównaniu z dyskusjami opartymi wyłącznie na cenie.


### Mining dla zysku czy dla sieci?


Pytanie jest głębokie i obejmuje kilka wymiarów Bitcoin Mining. Równowaga między dążeniem do zysku a przyczynianiem się do bezpieczeństwa i dystrybucji sieci Bitcoin jest stałym dylematem dla górników. Debata trwa w społeczności Bitcoin, z silnymi argumentami po każdej ze stron.



- Mining dla zysku:



- Dla: Górników w naturalny sposób przyciągają potencjalne zarobki z Bitcoin Mining. Inwestowanie w drogi sprzęt Mining może zostać zrównoważone przez nagrody Mining i opłaty transakcyjne, zwłaszcza gdy cena Bitcoin jest wysoka.
- Przeciw: Pogoń za zyskiem może prowadzić do centralizacji mocy hashowania, jeśli tylko kilka dużych firm może sobie pozwolić na inwestowanie w wysokiej klasy sprzęt Mining. Ponadto Mining dla zysku może mieć znaczący wpływ na środowisko.



- Mining dla sieci:



- Dla: Mining przyczynienie się do bezpieczeństwa i decentralizacji sieci Bitcoin to szlachetna inicjatywa. Pomaga wzmocnić odporność sieci na cenzurę i ataki.
- Przeciw: Bez wystarczającej zachęty finansowej górnikom może być trudno kontynuować wspieranie sieci, zwłaszcza jeśli działają ze stratą.


Inicjatywa Attakai podkreśla znaczenie wkładu w sieć, oferując jednocześnie rozwiązania, dzięki którym Mining będzie bardziej dostępny i mniej szkodliwy. Możliwość Mining w domu, z bardziej przystępnym cenowo sprzętem i rozwiązaniami zmniejszającymi zanieczyszczenie hałasem, może pomóc w demokratyzacji Bitcoin Mining. Zachęca osoby zainteresowane Bitcoin nie tylko do inwestowania i posiadania bitcoinów, ale także do aktywnego udziału w zabezpieczaniu sieci. Dostarczając przetestowany sprzęt i przewodniki dotyczące montażu i instalacji, Attakai ułatwia wejście do świata Bitcoin Mining. Zachęca również do innowacji i ciągłych ulepszeń, zapraszając społeczność do wnoszenia wkładu i dzielenia się swoimi pomysłami i doświadczeniami w celu ulepszenia domowego Mining. Model Attakai jest odpowiedzią na pytanie Mining dla zysku czy dla sieci. Nie chodzi tylko o osiąganie zysków, ale także o wzmocnienie dystrybucji i bezpieczeństwa sieci Bitcoin, jednocześnie umożliwiając większej liczbie osób uczestnictwo w Mining, naukę i zrozumienie tej kluczowej branży. Wyzwanie związane z potencjalnym zakazem Mining w Europie pozostaje kwestią otwartą. Rodzi to obawy o przyszłość Bitcoin w regionie i potrzebę zrównoważonych regulacji, które uznają znaczenie Mining dla bezpieczeństwa i rentowności sieci Bitcoin przy jednoczesnym uwzględnieniu kwestii środowiskowych. Attakai i inne podobne inicjatywy mogą odegrać kluczową rolę w tej debacie, pokazując, że możliwe jest wydobycie w bardziej zrównoważony i odpowiedzialny sposób, przy jednoczesnym pozytywnym wpływie na sieć Bitcoin.


## Suwerenność i regulacja


<chapterId>9d9a5908-2acc-501e-906b-a6fce9ecfebd</chapterId>


### Suwerenność przed zyskiem?


Aby rozwiązać kluczową kwestię bogactwa poprzez Mining, ważne jest rozważenie różnych perspektyw i podejść. Pytania o rentowność Mining są powszechne, a zapytania dotyczą zakupu udziałów w spółkach takich jak Riot lub leasingu maszyn Mining w krajach o niskich kosztach energii, takich jak Islandia czy Rosja. Przed wejściem na rynek Mining, kluczową kwestią byłoby porównanie rentowności Mining z bezpośrednim zakupem Bitcoin. Jeśli koszt Mining dla Bitcoin przekracza koszt jego bezpośredniego zakupu, generalnie rozsądniej jest zakupić Bitcoin bezpośrednio. Pozwala to uniknąć wielu wyzwań i kosztów związanych z procesem Mining.


Mining oferuje jednak unikalne możliwości zaangażowania się w ekosystem Bitcoin. Na przykład, Mining Bitcoin zimą może być sprytnym sposobem na ogrzanie domu przy jednoczesnym generowaniu przychodów z Bitcoin. Inną opcją jest inwestowanie w firmy, które sprzedają sprzęt Mining i przechowują maszyny oraz zarządzają nimi w lokalizacjach o niskich kosztach energii, zapewniając w ten sposób dostęp do korzystnych stawek za energię elektryczną bez kłopotów związanych z zarządzaniem sprzętem.


Pomimo tych opcji, Mining stanowi poważne wyzwanie. Znane w świecie kryptowalut powiedzenie "Nie twoje klucze, nie twoje Bitcoiny" znajduje podobny oddźwięk w świecie Mining: "Nie twój Hashrate, nie twoja nagroda" Historie o rozczarowaniach i odłączonych maszynach są powszechne, a wielu graczy obiecuje wyjątkowe wyniki, ale ich nie osiąga. Problemy z energią elektryczną Supply i awarie maszyn mogą pozostawić inwestorów bezsilnymi, z drogim sprzętem, którego nie kontrolują. W tym kontekście ostrożność i dogłębne zrozumienie sektora Mining mają kluczowe znaczenie przed podjęciem w nim działalności. Chociaż istnieją możliwości osiągnięcia zysków, ryzyko jest znaczne, a świadome i przemyślane podejście jest niezbędne do poruszania się po tym złożonym i często nieprzewidywalnym obszarze. Dlatego ważne jest, aby przeprowadzić dokładne badania i starannie rozważyć zalety i wady przed zaangażowaniem się w Bitcoin Mining.


![image](assets/en/013.webp)


### Bitcoiny Virgin


Dążenie do posiadania własnego Hashrate wydaje się obiecującą ścieżką w świecie Mining. Poruszanie się po tym złożonym ekosystemie wymaga jednak ostrożnego podejścia. Obszar Mining w chmurze charakteryzuje się dużą liczbą oszustw, napędzanych brakiem zrozumienia Mining przez wielu inwestorów. Atrakcyjne oferty, opakowane na różne sposoby, mogą łatwo wprowadzić w błąd tych, którzy nie są wystarczająco poinformowani. Z drugiej strony, posiadanie własnego sprzętu Mining oferuje znaczne korzyści. Oprócz osobistej satysfakcji z aktywnego przyczyniania się do bezpieczeństwa sieci Bitcoin i obserwowania, jak nagrody wpadają do Wallet, istnieje atrakcyjny aspekt "dziewiczych bitcoinów" Są to świeżo wydobyte bitcoiny, które nigdy nie zostały wydane i nie mają żadnej historii. Te bitcoiny są często uważane za bardziej wartościowe, ponieważ nigdy nie zostały "skażone", oferując pewną gwarancję przed odrzuceniem przez organy regulacyjne lub główne platformy Exchange.


Kolejną wartością dodaną jest możliwość pozyskiwania bitcoinów z Mining przy jednoczesnym unikaniu procedur Poznaj Swojego Klienta (KYC). Wiele pul Mining nie wymaga tożsamości górników, umożliwiając w ten sposób nabywanie bitcoinów bez przechodzenia żmudnych kontroli tożsamości. Dziewicze bitcoiny są postrzegane jako "czyste", bez historii i powiązań. Są one szczególnie poszukiwane przez dużych graczy instytucjonalnych, którzy mogą zagwarantować legalność swoich zasobów cyfrowych w obliczu organów regulacyjnych. Jednak pomimo tych zalet, kluczowe znaczenie ma uznanie, że branża Mining pozostaje niezwykle konkurencyjna i niestabilna, a nieprzewidziane incydenty mogą zakłócić operacje Mining.


W tym kontekście wybór autonomicznego i wyedukowanego podejścia do Mining wydaje się rozsądny. Nabycie własnego Hashrate i inwestowanie w osobisty sprzęt Mining, przy jednoczesnym zachowaniu świadomości ryzyka i wyzwań, może potencjalnie oferować bezpieczniejszą i bardziej satysfakcjonującą ścieżkę do pozyskiwania dziewiczych bitcoinów, zwiększając w ten sposób suwerenność finansową jednostki, jednocześnie wspierając ekosystem Bitcoin jako całość.


### Czy Mining jest zakazany w Europie?


W związku z potencjalnym zakazem stosowania Mining w Europie, dyskusje na temat regulacji stają się coraz bardziej istotne. Zmienny krajobraz regulacyjny może rzeczywiście znacząco wpłynąć na branżę Bitcoin Mining. Zakaz stosowania Mining w Europie jest możliwym scenariuszem, zwłaszcza biorąc pod uwagę precedensy w Chinach. Chociaż operacje Mining są kontynuowane w Chinach pomimo zakazu, Europa może podążać podobną ścieżką. Szersza dystrybucja Hashrate w różnych regionach może pomóc wzmocnić społeczność Mining w Europie, umożliwiając jej skuteczne przeciwdziałanie nieporozumieniom i błędnym przekonaniom na temat Mining, jego wpływu na środowisko i jego wpływu na sieć elektryczną.


![image](assets/en/014.webp)


W obliczu kampanii takich jak te prowadzone przez Greenpeace i często wprowadzających w błąd danych z niektórych badań, najlepszą bronią pozostaje prawdziwa informacja. Niezbędne jest informowanie opinii publicznej i decydentów o rzeczywistości Mining, jego złożoności i niuansach, zamiast pozwalać im polegać na stereotypach i niedokładnych informacjach. Im więcej osób jest poinformowanych i świadomych tego, czym naprawdę jest Mining, tym lepiej branża może bronić się przed potencjalnymi restrykcyjnymi regulacjami.


Podsumowując, pomimo ryzyka regulacyjnego i możliwości wprowadzenia zakazu stosowania Mining w Europie, najpotężniejszą bronią pozostaje edukacja i informacja. Jasne i precyzyjne zrozumienie Mining, jego działania i wpływu może pomóc w demistyfikacji branży i walce z dezinformacją, oferując tym samym lepszą odporność na potencjalnie szkodliwe regulacje. Inicjatywa mająca na celu szkolenie i informowanie ludzi o Mining, tak jak czyni to niniejsza dyskusja, jest krokiem we właściwym kierunku, aby zapewnić zrównoważony rozwój i wzrost Mining w Europie i na całym świecie. Ciągłe wysiłki na rzecz edukacji i informowania mają zasadnicze znaczenie dla zapewnienia bezpiecznej i pomyślnej przyszłości branży Bitcoin Mining.


# Strona główna Mining i ponowne wykorzystanie ciepła


<partId>78d22d06-2c4a-573f-86bb-1027115dad3a</partId>


## Attakai - uczynienie domowego Mining możliwym i dostępnym!


<chapterId>1f5d1b74-2f99-5f31-a088-a73d36491ebf</chapterId>


Attakai, co po japońsku oznacza "idealną temperaturę", to nazwa inicjatywy mającej na celu odkrycie Bitcoin Mining poprzez ponowne wykorzystanie ciepła, uruchomionej przez @ajelexBTC i @jimzap21 z Découvre Bitcoin.

Niniejszy przewodnik dotyczący modernizacji ASIC posłuży jako podstawa do zapoznania się z Mining, jego działaniem i podstawową ekonomią poprzez zademonstrowanie możliwości dostosowania Bitcoin Miner do użytku jako grzejniki w domach. Zapewnia to większy komfort i oszczędności, umożliwiając uczestnikom otrzymanie zwrotu gotówki za ogrzewanie elektryczne.


Bitcoin automatycznie dostosowuje trudność Mining i nagradza górników za ich udział. Koncentracja Hashrate może jednak stanowić zagrożenie dla neutralności sieci. Wykorzystanie mocy obliczeniowej Bitcoin do rozwiązań grzewczych przynosi bezpośrednie korzyści samej sieci poprzez zwiększenie dystrybucji mocy obliczeniowej.


### Po co ponownie wykorzystywać ciepło z ASIC?


Ważne jest, aby zrozumieć związek między energią a produkcją ciepła w układzie elektrycznym.


Przy inwestycji 1 kW energii elektrycznej, grzejnik elektryczny wytwarza 1 kW ciepła, nie więcej, nie mniej. Nowe grzejniki nie są bardziej wydajne od tradycyjnych. Ich zaletą jest zdolność do ciągłego i równomiernego rozprowadzania ciepła w pomieszczeniu, zapewniając większy komfort w porównaniu z tradycyjnymi grzejnikami, które na przemian mają wysoką moc grzewczą i nie nagrzewają się, generując regularne wahania temperatury i dyskomfort.


Komputer, lub szerzej płyta elektroniczna, nie zużywa energii do wykonywania obliczeń, po prostu potrzebuje energii do przepływu przez swoje komponenty, aby działać. Zużycie energii wynika z oporu elektrycznego komponentów, który powoduje straty i generuje ciepło, znane jako efekt Joule'a.


Niektóre firmy wpadły na pomysł połączenia zapotrzebowania na moc obliczeniową z potrzebami grzewczymi poprzez grzejniki/serwery. Pomysł polega na dystrybucji serwerów firmy do małych jednostek, które można umieścić w domach lub biurach. Pomysł ten napotyka jednak kilka problemów. Zapotrzebowanie na serwery nie jest związane z potrzebą ogrzewania, a firmy nie mogą elastycznie wykorzystywać możliwości obliczeniowych swoich serwerów. Istnieją również ograniczenia przepustowości, jaką mogą dysponować poszczególne osoby. Wszystkie te ograniczenia uniemożliwiają firmie uczynienie tych drogich instalacji opłacalnymi lub zapewnienie stabilnej oferty serwerów online bez centrów danych, które mogą przejąć kontrolę, gdy ogrzewanie nie jest potrzebne.


> Ciepło generowane przez komputer nie jest marnowane, jeśli trzeba ogrzać dom. Jeśli korzystasz z ogrzewania elektrycznego w miejscu zamieszkania, ciepło z komputera nie jest marnowane. Koszt generate tego ciepła z komputera jest taki sam. Jeśli masz tańszy system ogrzewania niż ogrzewanie elektryczne, marnotrawstwo polega tylko na różnicy w kosztach. Jeśli jest lato i używasz klimatyzacji, to jest to podwójne marnotrawstwo. Bitcoin Mining powinien mieć miejsce tam, gdzie jest taniej. Być może tam, gdzie klimat jest Cold i gdzie ogrzewanie jest elektryczne, Mining stanie się darmowy.
>

> Satoshi Nakamoto - 8 sierpnia 2010 r

Bitcoin i Proof of Work wyróżniają się tym, że automatycznie dostosowują trudność Mining w oparciu o ilość obliczeń wykonywanych przez całą sieć. Ilość ta nazywana jest Hashrate i wyrażana jest w hashach na sekundę. Obecnie szacuje się ją na 380 eksahashy na sekundę, czyli 380 miliardów miliardów haszy na sekundę. Hashrate reprezentuje pracę, a zatem ilość zużytej energii. Im wyższy Hashrate, tym wyższy poziom trudności i odwrotnie. Tak więc Bitcoin Miner może być aktywowany lub dezaktywowany w dowolnym momencie bez wpływu na sieć, w przeciwieństwie do grzejników/serwerów, które muszą pozostać stabilne, aby świadczyć swoje usługi. Miner jest nagradzany za swój udział w stosunku do innych, bez względu na to, jak mały może on być.


Podsumowując, grzejnik elektryczny i Bitcoin Miner wytwarzają 1 kW ciepła na 1 kW zużytej energii elektrycznej. Jednak Miner otrzymuje również bitcoiny jako nagrodę. Niezależnie od ceny energii elektrycznej, ceny Bitcoin lub konkurencji w zakresie aktywności Bitcoin Mining w sieci, ekonomicznie bardziej korzystne jest ogrzewanie za pomocą Miner niż grzejnika elektrycznego.


### Wartość dodana dla Bitcoin


Ważne jest, aby zrozumieć, w jaki sposób Mining przyczynia się do decentralizacji Bitcoin.

Kilka istniejących technologii zostało pomysłowo połączonych, aby ożywić konsensus Nakamoto. Konsensus ten ekonomicznie nagradza uczciwych uczestników za ich wkład w funkcjonowanie sieci Bitcoin, jednocześnie zniechęcając nieuczciwych uczestników. Jest to jeden z kluczowych punktów, który pozwala sieci istnieć w sposób zrównoważony.

Uczciwi gracze, ci, którzy wydobywają surowce zgodnie z zasadami, konkurują ze sobą, aby uzyskać jak największy udział w nagrodzie za produkcję nowych bloków. Ten bodziec ekonomiczny w naturalny sposób prowadzi do centralizacji, ponieważ firmy decydują się specjalizować w tej lukratywnej działalności, obniżając swoje koszty dzięki ekonomii skali. Te podmioty przemysłowe mają korzystną pozycję w zakresie zakupu i konserwacji maszyn, a także negocjowania hurtowych stawek za energię elektryczną.


> Początkowo większość użytkowników korzystałaby z węzłów sieciowych, ale w miarę jak sieć rozrastałaby się powyżej pewnego punktu, coraz częściej pozostawiano by ją specjalistom z farmami serwerów ze specjalistycznym sprzętem. Farma serwerów musiałaby mieć tylko jeden węzeł w sieci, a reszta sieci LAN łączyłaby się z tym węzłem.
>

> Satoshi Nakamoto - 2 listopada 2008 r

Niektóre podmioty posiadają znaczny procent całkowitej ilości Hashrate w dużych farmach Mining. Możemy zaobserwować niedawną falę Cold w Stanach Zjednoczonych, gdzie znaczna część Hashrate została wyłączona, aby przekierować energię do gospodarstw domowych o wyjątkowym zapotrzebowaniu na energię elektryczną. Przez kilka dni górnicy byli ekonomicznie zachęcani do wyłączania swoich farm, a tę wyjątkową pogodę można zaobserwować na krzywej Bitcoin Hashrate.


Kwestia ta może stać się problematyczna i stanowi poważne zagrożenie dla neutralności sieci. Podmiot posiadający ponad 51% udziałów w Hashrate mógłby łatwiej cenzurować transakcje. Dlatego ważne jest, aby rozdzielić Hashrate między wiele podmiotów, a nie scentralizowanych podmiotów, które mogłyby być łatwiej przejęte przez rząd.


**Jeśli górnicy są rozproszeni w tysiącach, a nawet milionach gospodarstw domowych na całym świecie, państwu bardzo trudno jest przejąć nad nimi kontrolę**


Kiedy Miner wychodzi z fabryki, nie nadaje się do użytku jako grzejnik w domu, ze względu na dwa główne problemy: nadmierny hałas i brak regulacji. Problemy te można jednak łatwo rozwiązać za pomocą modyfikacji sprzętu i oprogramowania, co pozwala na uzyskanie znacznie cichszego Miner, który można skonfigurować i zautomatyzować jak nowoczesne grzejniki elektryczne.


**Attakaï to inicjatywa edukacyjna, która uczy, jak zmodernizować Antminer S9 w najbardziej opłacalny sposób**


Jest to doskonała okazja, aby uczyć się poprzez praktykę, a jednocześnie być nagradzanym za udział w satoshis bez KYC.


## Przewodnik zakupu używanego ASIC


<chapterId>3b0b3bf0-859b-57f2-b92f-843ac70b7e68</chapterId>


W tej sekcji omówimy najlepsze praktyki dotyczące zakupu używanego Bitmain Antminer S9, maszyny, na której oparty będzie ten samouczek dotyczący modernizacji chłodnicy. Niniejszy przewodnik dotyczy również innych modeli układów ASIC, ponieważ jest to ogólny przewodnik zakupu używanego sprzętu Mining.


Antminer S9 to urządzenie oferowane przez Bitmain od maja 2016 roku. Pobiera 1400 W energii elektrycznej i wytwarza 13,5 TH/s. Chociaż jest uważany za stary, pozostaje doskonałą opcją do uruchomienia Mining. Ponieważ został wyprodukowany w dużych ilościach, łatwo jest znaleźć części zamienne w wielu regionach świata. Zasadniczo można go nabyć peer-to-peer na stronach takich jak eBay lub LeBonCoin, ponieważ profesjonalni sprzedawcy nie oferują go już ze względu na jego niższą konkurencyjność w porównaniu z nowszymi maszynami. Jest mniej wydajny niż układy ASIC, takie jak Antminer S19, oferowane od marca 2020 r., ale to sprawia, że jest to niedrogi używany sprzęt i bardziej odpowiedni do modyfikacji, które wprowadzimy.


Antminer S9 występuje w kilku wariantach (i, j), które wprowadzają drobne modyfikacje do sprzętu pierwszej generacji. Uważamy, że nie powinno to wpływać na decyzję o zakupie, a niniejszy przewodnik działa dla wszystkich tych wariantów.


Cena układów ASIC różni się w zależności od wielu czynników, takich jak cena Bitcoin, trudność sieci, wydajność maszyny i koszt energii elektrycznej. W związku z tym trudno jest podać dokładne szacunki dotyczące zakupu używanej maszyny. W lutym 2023 r. oczekiwana cena we Francji wynosiła od 100 do 200 euro, ale ceny te mogą szybko ulec zmianie.


![image](assets/en/015.webp)


Antminer S9 składa się z następujących części:



- 3 hashboardy, które zawierają chipy generujące moc mieszania.


![image](assets/en/016.webp)



- Płyta sterująca, która zawiera gniazdo na kartę SD, port Ethernet oraz złącza dla hashboardów i wentylatorów. To jest mózg twojego ASIC.


![image](assets/en/017.webp)



- 3 kable danych łączące tablice mieszające z płytą sterowania.


![image](assets/en/018.webp)



- Moc Supply, która działa na 220V i może być podłączona jak zwykłe urządzenie gospodarstwa domowego.


![image](assets/en/019.webp)



- 2 wentylatory 120 mm.


![image](assets/en/020.webp)



- Męski kabel C13.


![image](assets/en/021.webp)


Przy zakupie używanej maszyny ważne jest sprawdzenie, czy wszystkie części są dołączone i sprawne. Podczas Exchange należy poprosić sprzedawcę o włączenie maszyny, aby sprawdzić jej prawidłowe działanie. Ważne jest, aby sprawdzić, czy urządzenie włącza się prawidłowo, a następnie sprawdzić łączność z Internetem, podłączając kabel Ethernet i uzyskując dostęp do loginu Bitmain Interface za pośrednictwem przeglądarki internetowej w tej samej sieci lokalnej. IP Address można znaleźć, łącząc się z routerem internetowym Interface i szukając podłączonych urządzeń. Ten Address powinien mieć następujący format: 192.168.x.x


![image](assets/en/022.webp)


Sprawdź również, czy działają domyślne poświadczenia (nazwa użytkownika: root, hasło: root). Jeśli domyślne poświadczenia nie działają, konieczne będzie zresetowanie urządzenia.


![image](assets/en/023.webp)


Po podłączeniu powinieneś być w stanie zobaczyć status każdej tablicy hashboard na pulpicie nawigacyjnym. Jeśli Miner jest podłączony do puli, powinieneś zobaczyć wszystkie działające hashboardy. Ważne jest, aby pamiętać, że górnicy wytwarzają dużo hałasu, co jest normalne. Należy również upewnić się, że wentylatory działają prawidłowo.


Następnie można usunąć Mining pool poprzedniego właściciela, aby później skonfigurować własny. Jeśli chcesz, możesz również sprawdzić hashboardy, demontując maszynę. Ten krok jest jednak bardziej skomplikowany i wymaga więcej czasu i narzędzi. Jeśli chcesz kontynuować ten demontaż, możesz zapoznać się z następną częścią tego samouczka, w której szczegółowo opisano, jak to zrobić. Ważne jest, aby pamiętać, że górnicy zbierają dużo Dust i wymagają regularnej konserwacji. Możesz obserwować gromadzenie się Dust i jakość konserwacji, demontując maszynę.

Po zapoznaniu się z tymi wszystkimi punktami, możesz kupić swoją maszynę z dużym stopniem pewności. W razie wątpliwości należy skonsultować się ze społecznością.


Podsumowując ten przewodnik w jednym zdaniu: **"Nie ufaj, weryfikuj"**


[Można również zwrócić się do profesjonalistów w dziedzinie regeneracji maszyn Mining, takich jak nasz partner 21energy. Oferują oni przetestowane maszyny S9, wyczyszczone i z zainstalowanym oprogramowaniem BraiiinOS+. Z kodem partnerskim "decouvre" otrzymasz 10% zniżki na zakup S9, wspierając jednocześnie projekt Attakai](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)


## Przewodnik dotyczący zakupu modyfikacji sprzętowych dla S9


<chapterId>fa5f5eca-bcbf-5a83-9b03-98ecbadbabd6</chapterId>


Właściciel Antminera S9 zapewne wie, jak głośny i nieporęczny potrafi być ten sprzęt. Możliwe jest jednak przekształcenie go w cichy i podłączony grzejnik, wykonując kilka prostych kroków. W tej sekcji przedstawimy niezbędny sprzęt do wykonania modyfikacji.


Jeśli jesteś doświadczonym majsterkowiczem i chcesz przekształcić Miner w grzejnik, ten poradnik jest dla Ciebie. Ostrzegamy, że modyfikacje urządzenia elektronicznego mogą stwarzać zagrożenie elektryczne. Dlatego ważne jest, aby podjąć wszelkie niezbędne środki ostrożności, aby uniknąć uszkodzeń lub obrażeń.


1. Wymiana wentylatorów


Oryginalne wentylatory Antminer S9 są zbyt głośne, aby używać Antminera jako grzałki. Rozwiązaniem jest zastąpienie ich cichszymi wentylatorami. Nasz zespół przetestował kilka modeli marki Noctua i wybrał Noctua NF-A14 iPPC-2000 PWM jako najlepszy kompromis. Pamiętaj, aby wybrać wersję 12V wentylatorów. Ten 140-milimetrowy wentylator może wytworzyć do 1200 W ciepła przy zachowaniu teoretycznego poziomu hałasu 31 dB. Aby zainstalować te wentylatory 140 mm, należy użyć adaptera 140 mm na 120 mm, który można znaleźć w sklepie DécouvreBitcoin. Dodamy również 140-milimetrowe kratki ochronne.


![image](assets/en/024.webp)

![image](assets/en/025.webp)

![image](assets/en/026.webp)


Wentylator Supply jest również dość głośny i wymaga wymiany. Zalecamy wentylator Noctua NF-A6x25 PWM. Należy pamiętać, że złącza wentylatorów Noctua nie są takie same jak oryginalne, więc do ich podłączenia potrzebny będzie adapter. Dwa będą wystarczające. Ponownie, upewnij się, że wybrałeś wersję 12V wentylatora.


![image](assets/en/027.webp)

![image](assets/en/028.webp)


2. Dodanie mostka WIFI/Ethernet


Zamiast używać kabla Ethernet, można podłączyć Antminer przez WIFI, dodając mostek WIFI/Ethernet. Wybraliśmy vonets vap11g-300, ponieważ umożliwia on łatwe pobieranie sygnału WIFI ze skrzynki internetowej i przesyłanie go do Antminera przez Ethernet bez tworzenia podsieci. Jeśli masz umiejętności elektryczne, możesz zasilać go bezpośrednio z zasilacza Antminer Supply bez konieczności dodawania ładowarki USB. W tym celu potrzebny będzie żeński wtyk jack 5,5 mm x 2,1 mm.


![image](assets/en/029.webp)

![image](assets/en/030.webp)


3. Opcjonalnie: dodaj inteligentną wtyczkę


Jeśli chcesz włączać/wyłączać Antminera ze smartfona i monitorować zużycie energii, możesz dodać inteligentną wtyczkę. Przetestowaliśmy wtyczkę ANTELA w wersji 16A, kompatybilną z aplikacją smartlife. Ta inteligentna wtyczka umożliwia przeglądanie dziennego i miesięcznego zużycia energii i łączy się bezpośrednio z routerem internetowym przez WiFi.


![image](assets/en/031.webp)


Lista sprzętu i linki



- 2X adapter 3D 140 mm na 120 mm



- [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW)



- [2 kratki wentylatora 140 mm] (https://www.amazon.fr/dp/B06XD4FTSQ)
- [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4)



- [Cukier elektryczny 2,5 mm²](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS)
- [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W)
- [Opcjonalna inteligentna wtyczka ANTELA](https://www.amazon.fr/dp/B09YYMVXJZ)


# Attakai - Modyfikowanie oprogramowania Antminer S9


<partId>afc9c29a-84aa-5f1d-82e2-5fd9ff2e1805</partId>


## Konfiguracja Vonet WIFI/Ethernet Bridge


<chapterId>3cf487a4-21ef-5b24-83d5-789b811f740f</chapterId>


Aby podłączyć ASIC przez WIFI, potrzebne będzie urządzenie zwane mostkiem. Urządzenie to umożliwia pobieranie sygnału WIFI z routera i przesyłanie go do innego urządzenia za pośrednictwem sieci Ethernet.


Wiele urządzeń może pełnić tę funkcję, ale polecamy VONETS WiFi Bridge/Repeater ze względu na jego wygodę.


Zasil mostek, podłączając go przez USB.


Z komputera połącz się z siecią WIFI VONETS\_**\*\*** za pomocą hasła 12345678.


![image](assets/en/032.webp)


Zaloguj się przy użyciu nazwy użytkownika "admin" i hasła "admin".


![image](assets/en/033.webp)


Wybierz Kreator.


![image](assets/en/034.webp)


Wybierz sieć WIFI, do której chcesz podłączyć Miner, a następnie kliknij Next.


UWAGA: Mostek Vonet działa tylko na częstotliwości 2,4 GHz. Obecnie routery zwykle oferują dwie sieci WIFI, jedną na częstotliwości 2,4 GHz i jedną na częstotliwości 5 GHz.


![image](assets/en/035.webp)


Wprowadź hasło do sieci WIFI w polu "Source WIFI hotspot password". Jeśli nie chcesz używać mostka Vonet do rozszerzenia sieci WIFI, zaznacz pole "Disable Hotspot". W przeciwnym razie pozostaw to pole niezaznaczone.


Następnie możesz kliknąć przycisk Zastosuj.


Na koniec kliknij restart, aby ponownie uruchomić most. Ponowne uruchomienie zajmie kilka minut.


Most powinien połączyć się z routerem i pojawić się pod nazwą "[VONETS.COM](http://vonets.com/)". Jeśli po kilku minutach nadal nie będzie połączenia, konieczne może być odłączenie/podłączenie mostka.


Po podłączeniu mostu, podłącz kabel Ethernet z mostu do ASIC, a następnie podłącz ASIC do gniazda zasilania. Następnie można uzyskać dostęp do ASIC Interface w taki sam sposób, jakby był bezpośrednio podłączony do routera przez Ethernet.


## Resetowanie urządzenia Antminer S9


<chapterId>b518b6bd-9dae-5136-ae3c-1fafb1cb2592</chapterId>


Przed instalacją systemu BraiinOS+ może być konieczne przywrócenie ustawień fabrycznych telefonu S9.

Metoda ta może być stosowana od 2 do 10 minut po uruchomieniu Miner.

2 minuty po włączeniu Miner naciśnij przycisk "Reset" przez 5 sekund, a następnie zwolnij go. Miner zostanie przywrócony do ustawień fabrycznych w ciągu 4 minut i uruchomi się ponownie automatycznie (nie trzeba go wyłączać).


![image](assets/en/036.webp)


## Instalacja systemu BraiinsOS+ na urządzeniu Antminer S9


<chapterId>38e8b1a8-8b1d-51ed-8b92-59d4ddb15184</chapterId>


Oryginalne oprogramowanie zainstalowane przez Antminer na ich maszynach Mining ma ograniczoną funkcjonalność. Dlatego w tym przewodniku zainstalujemy inne oprogramowanie o nazwie BraiinsOS+. Jest to oprogramowanie innej firmy opracowane przez pierwszego Bitcoin Mining pool, które ma więcej funkcji i pozwala na przykład modyfikować moc maszyny.


Istnieje kilka sposobów instalacji Braiins OS+ na ASIC. Można zapoznać się z niniejszym przewodnikiem, a także z [oficjalną dokumentacją Braiins] (https://academy.braiins.com/en/braiins-os/about/).


Tutaj zobaczymy, jak łatwo zainstalować Braiins OS+ bezpośrednio w pamięci Antminera za pomocą oprogramowania BOS toolbox, zastępując oryginalny system operacyjny, wykonując szczegółowe kroki opisane poniżej.


1. Włącz Antminer i podłącz go do skrzynki internetowej.

2. Pobierz BOS toolbox dla Windows / Linux.

3. Rozpakuj pobrany plik i otwórz plik bos-toolbox.bat. Wybierz język, a po kilku chwilach zobaczysz to okno:


![image](assets/en/037.webp)


4. Bos toolbox pozwoli ci łatwo znaleźć IP Address twojego Antminera i zainstalować BraiinsOS+. Jeśli znasz już adres IP Address swojego urządzenia, możesz przejść do kroku 8. W przeciwnym razie przejdź do zakładki skanowania.


![image](assets/en/038.webp)


5. Zazwyczaj w sieciach domowych zakres adresów IP Address wynosi od 192.168.1.1 do 192.168.1.255, dlatego w polu zakresu adresów IP należy wpisać "192.168.1.0/24". Jeśli sieć jest inna, należy odpowiednio zmienić te adresy. Następnie kliknij "Start".


6. Uwaga, jeśli Antminer ma hasło, wykrywanie nie będzie działać. W takim przypadku najprostszym rozwiązaniem jest wykonanie resetu.


7. W tym miejscu powinny pojawić się wszystkie Antminery w sieci, a adres IP Address to 192.168.1.37.


![image](assets/en/039.webp)


8. Kliknij "Wstecz", a następnie zakładkę "Zainstaluj", wprowadź wcześniej znaleziony adres IP Address i kliknij "Start".


> Jeśli instalacja nie powiedzie się, konieczne może być wykonanie resetu i ponowna próba (patrz poprzednia sekcja).

![image](assets/en/040.webp)


9. Po kilku chwilach Antminer uruchomi się ponownie i będzie można uzyskać dostęp do Braiins OS+ Interface pod określonym adresem IP Address, tutaj 192.168.1.37, bezpośrednio w pasku Address przeglądarki. Domyślna nazwa użytkownika to "root" i nie ma domyślnego hasła.


## Konfiguracja systemu BraiinsOS+


<chapterId>36e432f2-85bc-52d0-a62a-009fc4c69338</chapterId>


Będziesz musiał połączyć się z ASIC przy użyciu lokalnego adresu IP Address urządzenia w sieci za pośrednictwem przeglądarki.


Adres IP Address urządzenia można znaleźć za pomocą narzędzia BOS Toolbox lub bezpośrednio na stronie internetowej routera.


Domyślne poświadczenia są takie same jak w oryginalnym systemie operacyjnym.



- nazwa użytkownika: root
- hasło: (brak)


Następnie zostaniesz powitany przez pulpit nawigacyjny Brains OS+.


### Pulpit nawigacyjny


![image](assets/en/041.webp)


Na tej pierwszej stronie można obserwować wydajność urządzenia w czasie rzeczywistym.



- Trzy wykresy w czasie rzeczywistym, które pokazują temperaturę, Hashrate i ogólny stan urządzenia.
- Po prawej, rzeczywisty Hashrate, średnia temperatura chipa, szacowana wydajność w W/THs i pobór mocy.
- Poniżej prędkość wentylatora jako procent prędkości maksymalnej i liczba obrotów na minutę.


![image](assets/en/042.webp)



- W dalszej części znajduje się szczegółowy widok każdej płyty głównej. Średnia temperatura płyty i zawartych w niej chipów, a także napięcie i częstotliwość.
- Szczegółowe informacje na temat aktywnych pul Mining w sekcji Pule.
- Stan automatycznego dostrajania w Status tunera.
- Po prawej stronie znajdują się szczegóły dotyczące danych przesyłanych do puli.


### Konfiguracja


![image](assets/en/043.webp)


### System


![image](assets/en/044.webp)


### Szybkie działania


![image](assets/en/045.webp)


# Attakai - Modyfikacja wentylatora


<partId>98266a8f-3745-58a0-9f6b-26a9734e1427</partId>


## Wymiana wentylatora zasilania Supply


<chapterId>0c6befa7-f3ef-5bcf-ae8d-0ad5e5d41d70</chapterId>


> OSTRZEŻENIE: Niezbędne jest wcześniejsze zainstalowanie systemu Braiins OS+ na Miner lub jakiegokolwiek innego oprogramowania, które może zmniejszyć wydajność urządzenia. Środek ten ma kluczowe znaczenie, ponieważ w celu zmniejszenia hałasu zainstalujemy wentylatory o mniejszej mocy, które mogą rozpraszać mniej ciepła.

![image](assets/en/046.webp)


### Wymagane materiały



- 1 wentylator Noctua NF-A6x25 PWM
- 2.cukier elektryczny 5mm2


> OSTRZEŻENIE: Przede wszystkim przed uruchomieniem upewnij się, że odłączyłeś Miner od zasilania, aby uniknąć ryzyka porażenia prądem.

![image](assets/en/047.webp)


Najpierw należy odkręcić 6 śrub z boku obudowy, które utrzymują ją zamkniętą. Po usunięciu śrub ostrożnie otwórz obudowę, aby usunąć plastikową osłonę zakrywającą komponenty.


![image](assets/en/048.webp)

![image](assets/en/049.webp)


Następnie nadszedł czas, aby usunąć oryginalny wentylator, uważając, aby nie uszkodzić innych komponentów. W tym celu należy odkręcić śruby, które utrzymują go na miejscu i delikatnie odkleić biały klej otaczający złącze. Ważne jest, aby postępować ostrożnie, aby uniknąć uszkodzenia przewodów lub złączy.


![image](assets/en/050.webp)


Po usunięciu oryginalnego wentylatora można zauważyć, że złącza nowego wentylatora Noctua nie pasują do złączy oryginalnego wentylatora. Rzeczywiście, nowy wentylator ma 3 przewody, w tym żółty przewód, który umożliwia sterowanie prędkością. Jednak ten przewód nie będzie używany w tym konkretnym przypadku. Aby podłączyć nowy wentylator, zaleca się zatem użycie specjalnego adaptera. Należy jednak pamiętać, że adapter ten może być czasami trudny do znalezienia.


![image](assets/en/051.webp)


Jeśli nie posiadasz tego adaptera, nadal możesz podłączyć nowy wentylator za pomocą cukru elektrycznego. W tym celu należy przeciąć kable starego i nowego wentylatora.


![image](assets/en/052.webp)

![image](assets/en/053.webp)


W przypadku nowego wentylatora należy użyć noża i ostrożnie przeciąć kontury głównej osłony w odległości 1 cm bez przecinania osłon kabli znajdujących się pod spodem.


![image](assets/en/054.webp)


Następnie, ciągnąc główną osłonę w dół, przetnij osłony czerwonego i czarnego kabla w taki sam sposób jak poprzednio. Odetnij również żółty kabel.


![image](assets/en/055.webp)


W przypadku starego wentylatora przecięcie głównej osłony bez uszkodzenia osłon czerwonego i czarnego przewodu jest bardziej delikatne. W tym celu użyliśmy igły, którą wsunęliśmy między główną osłonę a czerwony i czarny przewód.


![image](assets/en/056.webp)

![image](assets/en/057.webp)


Po odsłonięciu czerwonego i czarnego przewodu należy ostrożnie przeciąć osłony, aby uniknąć uszkodzenia przewodów elektrycznych.


![image](assets/en/058.webp)


Następnie połącz kable za pomocą cukru, czarny przewód z czarnym, a czerwony z czerwonym. Można również dodać taśmę izolacyjną.


![image](assets/en/059.webp)

![image](assets/en/060.webp)


Po wykonaniu połączenia nadszedł czas, aby zainstalować nowy wentylator Noctua z kratką i starymi śrubami. Nowe śruby w pudełku zostaną ponownie użyte później. Upewnij się, że umieściłeś go we właściwej orientacji. Po jednej stronie wentylatora znajduje się strzałka wskazująca kierunek przepływu powietrza. Ważne jest, aby ustawić wentylator tak, aby strzałka była skierowana do wnętrza obudowy. Następnie ponownie podłącz wentylator.


![image](assets/en/061.webp)

![image](assets/en/062.webp)


> Opcjonalnie: Jeśli masz wiedzę na temat elektryczności, możesz bezpośrednio dodać żeńskie złącze jack 5,5 mm do wyjścia zasilania 12 V, które będzie bezpośrednio zasilać mostek Wi-Fi Vonet. Jeśli jednak nie masz pewności co do swoich umiejętności elektrycznych, najlepiej jest użyć złącza USB z ładowarką typu smartfon, aby uniknąć ryzyka zwarcia lub uszkodzenia elektrycznego.

![image](assets/en/063.webp)


Po wykonaniu połączeń umieść plastikową osłonę na plastikowej obudowie, a nie wewnątrz.


![image](assets/en/064.webp)


Na koniec umieść pokrywę obudowy z powrotem na miejscu i przykręć 6 śrub po bokach, aby utrzymać wszystko na miejscu. I gotowe, obudowa Supply jest teraz wyposażona w nowy wentylator.


## Wymiana wentylatorów głównych


<chapterId>a29f60f1-3fa3-57fc-a630-9c97cec30e56</chapterId>


> OSTRZEŻENIE: Niezbędne jest wcześniejsze zainstalowanie systemu Braiins OS+ na Miner lub jakiegokolwiek innego oprogramowania, które może zmniejszyć wydajność urządzenia. Środek ten ma kluczowe znaczenie, ponieważ w celu zmniejszenia hałasu zainstalujemy wentylatory o mniejszej mocy, które będą rozpraszać mniej ciepła.

![image](assets/en/046.webp)


### Wymagane materiały



- 2 sztuki adaptera 3D 140 mm na 120 mm
- 2 wentylatory Noctua NF-A14 iPPC-2000 PWM
- 2 kratki wentylatora 140 mm


> OSTRZEŻENIE: Przede wszystkim przed uruchomieniem należy odłączyć Miner, aby uniknąć ryzyka porażenia prądem.

1. Najpierw odłącz wentylatory i odkręć je.


![image](assets/en/065.webp)


2. Złącza nowych wentylatorów Noctua nie pasują do oryginalnych, ale nie martw się! Wyjmij nożyk i ostrożnie wytnij małe plastikowe wypustki, aby złącza idealnie pasowały do Miner.


![image](assets/en/066.webp)

![image](assets/en/067.webp)


3. Czas zainstalować części 3D!

Przymocuj je po obu stronach Miner za pomocą śrub usuniętych z wentylatorów. Przykręć je, aż łeb śruby zrówna się z częścią 3D i będzie bezpiecznie na miejscu. Uważaj, aby nie dokręcić zbyt mocno, ponieważ możesz zdeformować część, a jedna ze śrub może dotknąć kondensatora!


![image](assets/en/068.webp)


4. Przejdźmy teraz do fanów.


Przymocuj je do części 3D za pomocą śrub dostarczonych w pudełku. Zwróć uwagę na kierunek przepływu powietrza, strzałki po bokach wentylatorów wskażą kierunek, w którym należy podążać. Przejdź od strony portu Ethernet na drugą stronę. Patrz zdjęcie poniżej.


![image](assets/en/069.webp)

![image](assets/en/070.webp)

![image](assets/en/071.webp)


5. Ostatni krok: podłącz wentylatory i przymocuj kratki na górze za pomocą śrub, które nie były używane w obudowie wentylatora Supply. Masz ich tylko 4, ale wystarczą 2 na kratkę w przeciwległych rogach. W razie potrzeby można również poszukać podobnych śrub w sklepie z narzędziami.


![image](assets/en/072.webp)

![image](assets/en/073.webp)


W oczekiwaniu na możliwość zaoferowania bardziej stylowej obudowy dla nowego grzejnika, można przymocować obudowę i zasilanie Supply za pomocą opasek kablowych dla elektryków.


![image](assets/en/074.webp)


Na koniec należy podłączyć mostek Vonet do portu Ethernet i zasilania Supply.


![image](assets/en/075.webp)


No i proszę, gratulacje! Właśnie wymieniłeś całą część mechaniczną Miner. Teraz powinieneś słyszeć znacznie mniej hałasu.


# Attakai - Konfiguracja


<partId>9c3918a8-d9a3-5a1f-bb9a-70314f7ac175</partId>


## Łączenie Mining pool


<chapterId>b57a6105-0a53-5fe9-bad1-d6d9daf97c0d</chapterId>


Można sobie wyobrazić Mining pool jako spółdzielnię rolniczą. Rolnicy łączą swoją produkcję, aby zmniejszyć zmienność Supply i popytu, a tym samym uzyskać bardziej stabilny dochód dla swojej działalności. Mining pool działa w ten sam sposób, przy czym współdzielonym zasobem są hashe. Rzeczywiście, odkrycie pojedynczego ważnego Hash pozwala na utworzenie bloku i wygranie coinbase lub nagrody, obecnie 6,25 BTC plus opłaty transakcyjne zawarte w bloku.


Jeśli wydobywasz sam, zostaniesz nagrodzony tylko wtedy, gdy znajdziesz blok. Konkurując ze wszystkimi innymi górnikami na świecie, miałbyś bardzo małe szanse na wygranie tej loterii i nadal musiałbyś płacić opłaty związane z korzystaniem z Miner bez żadnej gwarancji sukcesu. Mining łączy Address tę kwestię, łącząc moc obliczeniową kilku (tysięcy) górników i dzieląc ich nagrody w oparciu o procentowy udział w Hashrate puli po znalezieniu bloku. Aby zwizualizować swoje szanse na samodzielne Mining bloku, możesz użyć tego narzędzia. Wprowadzając informacje dla Antminera S9, możemy zobaczyć, że szanse na znalezienie Hash, który pozwala na utworzenie bloku, wynoszą 1 na 24 777 849 dla każdego bloku lub 1 na 172 068 dziennie. Średnio (przy stałym Hashrate i poziomie trudności) znalezienie bloku zajęłoby co najmniej 471 lat (wraz ze wzrostem poziomu trudności).


Ponieważ jednak wszystko w Bitcoin opiera się na prawdopodobieństwie, czasami zdarza się, że górnicy solo są nagradzani za podjęcie tego ryzyka: Solo Bitcoin Miner rozwiązuje blok z Hash z szybkością zaledwie 10 TH/s, pokonując niezwykle mało prawdopodobne szanse - Decrypt


Jeśli lubisz hazard, możesz spróbować, ale nasz przewodnik nie będzie koncentrował się w tym kierunku. Zamiast tego skoncentrujemy się na Mining pool, który najlepiej odpowiada naszym potrzebom w zakresie tworzenia systemu grzewczego.


Przy wyborze Mining pool należy wziąć pod uwagę działanie nagród w puli, które mogą się różnić, a także minimalną kwotę, zanim będzie można wypłacić nagrody do Address. Na przykład Braiins, który oferuje oprogramowanie, o którym tutaj mówimy, oferuje również pulę. Pula ta ma system nagród o nazwie "Score", który zachęca górników do wydobywania przez długi czas. Uczestnictwo obejmuje współczynnik dyspozycyjności wyrażony jako "punktacja Hashrate". W naszym przypadku, gdy chcemy mieć system grzewczy, który można włączyć tylko na kilka minut, nie jest to idealny system nagradzania. Wolimy system nagród, który daje nam równą nagrodę za każdy udział. Dodatkowo, minimalna kwota wypłaty dla Braiins Pool wynosi 100 000 Sats i On-Chain. Tracimy więc trochę Sats w opłatach transakcyjnych, a część naszej nagrody może zostać zablokowana, jeśli nie wydobędziemy wystarczająco dużo w zimie.


Model wynagradzania, który nas interesuje, to PPS, co oznacza "pay-per-share". Oznacza to, że Miner otrzyma nagrodę za każdą ważną akcję. Istnieje również wariant tego systemu, FPPS (Full Pay Per Share), który nie tylko dzieli nagrodę coinbase, ale także opłaty transakcyjne zawarte w bloku. Pule Mining, które zalecamy do podłączenia Mining/ogrzewania, to Linecoin Pool (FPPS) i Nicehash (PPS).



- Nicehash: Zaletą Nicehash jest to, że wypłaty można dokonać za pomocą Lightning przy minimalnych opłatach. Dodatkowo minimalna kwota wypłaty wynosi 2000 Sats. Wadą jest to, że Nicehash wykorzystuje swoje Hashrate do najbardziej dochodowych Blockchain, nie dając tak naprawdę kontroli użytkownikowi, więc niekoniecznie może przyczynić się do Bitcoin Hashrate.



- Linecoin: Zaletą Linecoin jest liczba oferowanych funkcji, takich jak szczegółowy pulpit nawigacyjny, możliwość dokonywania wypłat za pomocą Paynym (BIP 47) dla lepszej ochrony prywatności oraz integracja bota Telegram, a także bezpośrednio konfigurowalne automatyzacje w aplikacji mobilnej. Ta pula wydobywa tylko bloki Bitcoin, ale minimalna kwota do wypłaty pozostaje wysoka i wynosi 100 000 Sats. Przeanalizujemy Interface jednej z tych pul bardziej szczegółowo w przyszłym artykule.


Aby skonfigurować pulę w Braiins OS+, należy utworzyć konto w jednej z wybranych pul. Tutaj weźmiemy przykład Linecoin:


![image](assets/en/076.webp)


Po utworzeniu konta kliknij przycisk Połącz z pulą


Następnie skopiuj Stratum Address i swoją nazwę użytkownika:


![image](assets/en/077.webp)


Możesz teraz wrócić do Braiins OS+ Interface, aby wprowadzić te dane uwierzytelniające. W przypadku hasła pole można pozostawić puste.


![image](assets/en/078.webp)


## Optymalizacja wydajności urządzenia Antminer S9


<chapterId>25380972-31c7-540d-80d8-17a06b171ca0</chapterId>


Zarówno overclocking, jak i autotuning obejmują regulację częstotliwości na płytach hashujących w celu poprawy wydajności ASIC. Różnica między nimi polega na złożoności tych ustawień częstotliwości.


Overclocking to prosta regulacja, która polega na zwiększeniu częstotliwości na płytach hashujących w celu zwiększenia szybkości Hash maszyny. Z drugiej strony, podkręcanie polega na zmniejszeniu częstotliwości taktowania układu scalonego poniżej jego częstotliwości nominalnej. Zmniejszając częstotliwość zegara ASIC poprzez podkręcanie, zmniejsza się również ciepło generowane przez sprzęt. Pozwala to na zmniejszenie prędkości wentylatorów wymaganych do chłodzenia ASIC, ponieważ nie muszą one pracować tak jak Hard, aby utrzymać odpowiednią temperaturę. Zmniejszając prędkość wentylatora, zmniejsza się również hałas generowany przez ASIC. Może to być szczególnie przydatne dla użytkowników, którzy używają układów ASIC w domu i chcą zminimalizować hałas powodowany przez sprzęt Mining.


Braiins OS+ obsługuje overclocking, underclocking układów ASIC oraz autotuning. Pozwala to użytkownikom na elastyczne dostosowywanie częstotliwości taktowania sprzętu w celu maksymalizacji wydajności lub oszczędzania energii zgodnie z ich preferencjami.


### Optymalizacja wydajności Antminer S9 za pomocą automatycznego dostrajania


Przed 2018 r. górnicy mieli dwa sposoby na uzyskanie przewagi w swojej działalności: znalezienie energii elektrycznej po rozsądnych kosztach i zakup bardziej wydajnego sprzętu. Jednak w 2018 r. odkryto nowe osiągnięcie w dziedzinie oprogramowania i oprogramowania układowego Mining, zwane AsicBoost. Technika ta pozwala górnikom obniżyć koszty o około 13% poprzez modyfikację oprogramowania układowego działającego na ich urządzeniach.


Obecnie w sektorze oprogramowania i oprogramowania układowego Mining pojawiło się nowe rozwiązanie o nazwie autotuning, które oferuje jeszcze większą przewagę niż AsicBoost. Układy ASIC składają się z wielu małych chipów komputerowych, które wykonują haszowanie. Chipy te są wykonane z krzemu, tego samego pierwiastka, który jest szeroko stosowany w półprzewodnikach i innych komponentach mikroelektronicznych. Kluczowe jest tutaj zrozumienie, że nie wszystkie chipy krzemowe są identyczne, a każdy z nich może nieznacznie różnić się właściwościami elektrycznymi. Producenci sprzętu są tego świadomi i publikują specyfikacje wydajności swoich urządzeń Mining w oparciu o dolną granicę tolerancji. Innymi słowy, producenci znają częstotliwość, która działa najlepiej dla przeciętnych chipów i używają tej częstotliwości jednolicie dla wszystkich chipów w maszynie.


Nakłada to górny limit na szybkość Hash, jaką może mieć maszyna. Autotuning to proces, w którym algorytmy oceniają optymalne częstotliwości dla hashowania chip-by-chip, zamiast traktować całą maszynę jako pojedynczą jednostkę. Oznacza to, że chip wyższej jakości, który może wykonać więcej skrótów na sekundę, otrzyma wyższą częstotliwość, a chip niższej jakości, który może wykonać stosunkowo mniej skrótów, otrzyma niższą częstotliwość. Autotuning na poziomie chipa jest zasadniczo sposobem na optymalizację wydajności ASIC poprzez oprogramowanie i oprogramowanie układowe działające na nim.


Efektem końcowym jest wyższy wskaźnik Hash na wat energii elektrycznej, co oznacza większe marże zysku dla górników. Powodem, dla którego maszyny nie są dystrybuowane z tego typu oprogramowaniem, jest to, że zmienność maszyn jest niepożądana, ponieważ klienci chcą dokładnie wiedzieć, co otrzymują, więc jest to zły pomysł dla producentów, aby sprzedawać produkt, który nie ma spójnej i przewidywalnej wydajności z jednej maszyny na drugą. Dodatkowo, autotuning na poziomie układu scalonego wymaga znacznych zasobów rozwojowych, ponieważ jego implementacja jest złożona. Producenci już teraz poświęcają wiele zasobów na rozwój własnego oprogramowania układowego. Istnieją rozwiązania programowe umożliwiające autotuning, takie jak Braiins OS+. Oprócz poprawy wydajności ASIC nawet o 20%.


# Sekcja końcowa


<partId>fa42ec0b-b1fd-47f6-8268-6eab684c1d2b</partId>


## Recenzje i oceny


<chapterId>6af13742-df68-5cf4-b7aa-93dc0c2eaae9</chapterId>

<isCourseReview>true</isCourseReview>

## Egzamin końcowy


<chapterId>f51a7c88-3b7e-48df-b45f-22bb10fe619f</chapterId>

<isCourseExam>true</isCourseExam>

## Wnioski


<chapterId>2941f29a-d6ce-4a3c-b61b-6e399f5395b1</chapterId>

<isCourseConclusion>true</isCourseConclusion>