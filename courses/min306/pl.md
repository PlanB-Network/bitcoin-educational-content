---
name: Bitaxe Open Source Mining Mastery
goal: Opanuj cały ekosystem Bitaxe, od montażu sprzętu po zaawansowaną personalizację i optymalizację wydajności
objectives: 

  - Zrozumienie filozofii otwartego sprzętu Bitcoin mining
  - Zbuduj urządzenia Bitaxe mining od podstaw
  - Konfiguracja i optymalizacja oprogramowania mining, w tym AxeOS i Public Pool
  - Wdrożenie zaawansowanych optymalizacji wydajności, w tym podkręcania i testów porównawczych

---

# Przewodnik po Bitaxe Mining


Witamy w kompleksowym kursie Bitaxe, w którym opanujesz rewolucyjny sprzęt Bitcoin mining o otwartym kodzie źródłowym, który demokratyzuje dostęp do technologii mining. Kurs ten prowadzi od zrozumienia filozoficznych podstaw zdecentralizowanego mining do zaawansowanych technik dostosowywania sprzętu i optymalizacji wydajności.


Projekt Bitaxe reprezentuje zmianę paradygmatu w Bitcoin mining, przełamując monopol zastrzeżonych producentów ASIC poprzez dostarczanie w pełni otwartych projektów, oprogramowania układowego i oprogramowania. Dzięki tym praktycznym rozdziałom zdobędziesz praktyczne umiejętności w zakresie montażu sprzętu, konfiguracji oprogramowania, projektowania PCB i optymalizacji wydajności.


Nie jest wymagane żadne wcześniejsze doświadczenie w mining, choć przydatna będzie podstawowa wiedza z zakresu elektroniki i znajomość GitHub. Kurs przekształci cię z ciekawskiego obserwatora w zdolnego konstruktora i współtwórcę Bitaxe.


+++


# Wprowadzenie


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Przegląd kursu


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Witamy w kursie MIN 306 _**Bitaxe Open Source Mining Mastery**_, kompleksowej podróży do świata Bitaxe mining. Ten kurs jest przeznaczony dla tych, którzy chcą zrozumieć, zbudować i zoptymalizować własny sprzęt Bitaxe mining, jednocześnie badając filozoficzne i techniczne podstawy, które sprawiają, że ten projekt jest wyjątkowy w ekosystemie Bitcoin.


### Zrozumienie Bitaxe


Pierwsza sekcja stanowi podstawę: odkryjesz początki projektu Bitaxe, jego ewolucję oraz wartości decentralizacji i przejrzystości, które go definiują. Dowiesz się, czym właściwie jest Bitaxe, czym różni się od zastrzeżonych układów ASIC i gdzie znaleźć zasoby społeczności, aby pogłębić swoją wiedzę. Ta sekcja zapewnia kontekst potrzebny do zrozumienia, dlaczego Bitaxe stanowi punkt zwrotny w historii Bitcoin mining.


### Oprogramowanie i operacje


Druga sekcja skupia się na środowisku oprogramowania, ze szczegółową prezentacją *AxeOS*: systemu operacyjnego typu open-source zaprojektowanego specjalnie dla urządzeń Bitaxe. Poznasz jego główne funkcje oraz sposób konfiguracji i interakcji z urządzeniem, aby rozpocząć pierwszą operację mining.


### Społeczność i współpraca


Trzecia sekcja podkreśla aspekt współpracy w ramach projektu. Poznasz filozofię open-source zastosowaną zarówno do rozwoju sprzętu, jak i oprogramowania Bitaxe. Dzięki praktycznym ćwiczeniom dowiesz się, jak wnieść swój wkład bezpośrednio do kodu źródłowego, a także odkryjesz _Public Pool_, platformę społecznościową do łączenia mocy obliczeniowej. Dowiesz się również, jak zainstalować ją na węźle Umbrel w celu integracji lokalnej i suwerennej.


### Montaż sprzętu i rozwiązywanie problemów


W czwartej części zajmiemy się samym sprzętem. Dowiesz się, jak zidentyfikować narzędzia potrzebne do złożenia Bitaxe, naprawić problemy z lutowaniem i przeprowadzić pełną diagnostykę przy użyciu *AxeOS* i narzędzi USB. Ta sekcja kładzie nacisk na praktyczną praktykę i dogłębne zrozumienie interakcji między komponentami sprzętowymi i programowymi.


### Zaawansowane dostosowywanie


Piąta sekcja poświęcona jest personalizacji. Dowiesz się, jak zmodyfikować PCB (płytkę drukowaną), utworzyć plik fabryczny i korzystać z _Bitaxe Web Flasher_. Ta sekcja jest skierowana do tych, którzy chcą wyjść poza prosty montaż i naprawdę zaprojektować spersonalizowane wersje własnego urządzenia.


### Optymalizacja wydajności


Wreszcie, szósta sekcja obejmuje zaawansowane techniki optymalizacji. Dowiesz się, jak przeprowadzić benchmark Bitaxe, aby ocenić jego wydajność i jak efektywnie go podkręcać. Umiejętności te pomogą ci w pełni wykorzystać możliwości sprzętu przy jednoczesnym poszanowaniu jego fizycznych ograniczeń.


Podobnie jak w przypadku każdego kursu w Plan ₿ Academy, ostatnia sekcja zawiera ocenę mającą na celu ugruntowanie wiedzy.


Zanurz się w tej technicznej przygodzie - przyszłość Bitcoin mining jest w Twoich rękach!


# Zrozumienie Bitaxe

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## Historia

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

Projekt Bitaxe stanowi przełomową zmianę w rozwoju sprzętu Bitcoin mining, wprowadzając zasady open source do branży zdominowanej przez zastrzeżone rozwiązania. Ta seria edukacyjna bada kompleksową historię, innowacje techniczne i ewolucję Bitaxe napędzaną przez społeczność, zapewniając wgląd w to, jak wizja jednego inżyniera przekształciła się w kwitnący ekosystem zdecentralizowanego sprzętu mining. Badając początki projektu, wyzwania i osiągnięcia, zyskujemy cenne zrozumienie zarówno technicznych zawiłości rozwoju ASIC, jak i siły współpracy open source w przestrzeni Bitcoin.


### Historia powstania: Od odkrycia Jedwabnego Szlaku do wizji Solar Mining


Skot, założyciel Bitaxe, rozpoczął swoją podróż do Bitcoin na imprezie w college'u, gdzie po raz pierwszy dowiedział się o Bitcoin od kogoś, kto kupował przedmioty na Jedwabnym Szlaku. Ta początkowa ekspozycja na Bitcoin w cenie około 20 USD za monetę wywołała ciekawość, która później przekształciła się w rewolucyjny projekt mining. Techniczne podstawy jego przyszłej pracy powstały podczas studiów, gdzie miał dostęp do rozległych zasobów FPGA w warunkach laboratoryjnych. Współpracując ze swoim przełożonym, Skot zaczął eksperymentować z otwartymi strumieniami bitów FPGA dla Bitcoin mining, początkowo ze skromnym celem mining wystarczającym Bitcoin na zakup pizzy do ich biura.


Przejście od eksperymentów akademickich do poważnego rozwoju nastąpiło wiele lat później, gdy Skot pracował nad zasilanymi energią słoneczną bramkami do zdalnego gromadzenia danych w Afryce. To doświadczenie zawodowe z systemami zasilania energią słoneczną uświadomiło mu, że układy ASIC Bitcoin mining, będące zasadniczo urządzeniami niskonapięciowymi DC, doskonale współpracują z panelami słonecznymi. Koncepcja ta wydawała się naturalna i elegancka. Jednak kiedy Skot zaczął badać istniejące rozwiązania, odkrył znaczącą lukę na rynku: w przeciwieństwie do wczesnych dni Bitcoin mining, kiedy projekty FPGA były otwarcie dostępne, pojawienie się układów ASIC przesunęło branżę w kierunku całkowicie zastrzeżonych, zamkniętych rozwiązań.


Brak otwartego sprzętu mining stał się przyczyną frustracji Skota, szczególnie biorąc pod uwagę jego doświadczenie w tworzeniu oprogramowania open source i przekonanie, że otwarty charakter Bitcoin powinien rozciągać się na infrastrukturę mining. Ta filozoficzna zgodność z zasadami open source, w połączeniu z technicznym wyzwaniem inżynierii wstecznej zastrzeżonych projektów ASIC, przygotowała grunt pod projekt Bitaxe. Początkowa wizja była ambitna, ale praktyczna: stworzyć zasilaną energią słoneczną koparkę Bitcoin, która mogłaby działać niezależnie, nie wymagając oddzielnego komputera do sterowania, dzięki czemu nadawałaby się do wdrożenia w odległych lokalizacjach pod panelami słonecznymi.


### Wyzwania techniczne i przełomy w inżynierii odwrotnej


Rozwój Bitaxe wymagał pokonania znacznych przeszkód technicznych, głównie związanych z całkowitym brakiem dokumentacji chipów ASIC firmy Bitmain. Podejście Skota do tego wyzwania było przykładem determinacji i pomysłowości wymaganej do udanej inżynierii wstecznej. Bez dostępu do oficjalnych arkuszy danych lub specyfikacji technicznych, uciekał się do badania chipów pod mikroskopem, mierzenia rozstawu pinów za pomocą suwmiarki, a nawet skanowania chipów w celu określenia ich dokładnych wymagań dotyczących powierzchni. Ten żmudny proces zaowocował wieloma nieudanymi prototypami, a pierwsze dwie iteracje "day minera" nie działały poprawnie z powodu nieprawidłowych obliczeń zajmowanej powierzchni.


Przełom nastąpił wraz z trzecią iteracją w maju 2022 r., kiedy to Skot z powodzeniem stworzył działający dwuprocesorowy projekt wykorzystujący chipy BM1387 pozyskane z jednostek Antminer S9. Osiągnięcie to oznaczało narodziny nazwy Bitaxe, zainspirowanej koncepcją kilofa dla Bitcoin mining. Sukces tego projektu potwierdził słuszność podejścia inżynierii odwrotnej i pokazał, że niezależni deweloperzy mogą stworzyć funkcjonalny sprzęt mining bez wsparcia producenta. Wyzwania techniczne wykraczały jednak poza interfejs układu scalonego i obejmowały złożony projekt zasilania, ponieważ układy ASIC wymagały precyzyjnej regulacji napięcia przy wysokich prądach, często działając przy napięciu tak niskim jak 0,6 V przy jednoczesnym poborze znacznego natężenia prądu.


Rozwój oprogramowania układowego stanowił kolejną warstwę złożoności, ponieważ projekt wymagał stworzenia oprogramowania mining, które mogłoby działać bezpośrednio na mikrokontrolerze ESP32, zamiast polegać na zewnętrznych komputerach z oprogramowaniem takim jak CGMiner. Takie samodzielne podejście było niezbędne dla realizacji wizji Skota dotyczącej niezależnych jednostek mining. Połączenie inżynierii wstecznej sprzętu i rozwoju wbudowanego oprogramowania układowego stworzyło kompleksowe wyzwanie techniczne, które wymagało wiedzy specjalistycznej z wielu dziedzin, od inżynierii elektrycznej i projektowania płytek drukowanych po programowanie wbudowane i protokoły sieciowe.


### Tworzenie społeczności i współpraca open source


Przekształcenie Bitaxe z solowego projektu w dobrze prosperującą inicjatywę społecznościową stanowi jeden z najważniejszych aspektów jego sukcesu. Początkowo podejmowane przez Skota próby zainteresowania generate za pośrednictwem forów Bitcoin i mediów społecznościowych spotykały się z ograniczonym odzewem i okazjonalnym sceptycyzmem. Przełom nastąpił, gdy członkowie społeczności, tacy jak SirVapesAlot, dostrzegli potencjał mining open source i założyli serwer Discord Open Source Miners United (OSMU). Platforma ta zapewniła środowisko współpracy niezbędne do rozkwitu projektu, przyciągając współpracowników z różnych środowisk, których łączyło wspólne zainteresowanie demokratyzacją technologii Bitcoin mining.


Model rozwoju napędzany przez społeczność okazał się niezwykle skuteczny, a kluczowi współpracownicy, tacy jak johnny9 i Ben, pojawili się, aby stawić czoła konkretnym wyzwaniom technicznym. Doświadczenie Johnny'ego9 w rozwoju oprogramowania układowego rozwiązało krytyczne problemy związane z implementacją oprogramowania, podczas gdy umiejętności Bena w zakresie programowania front-end stworzyły intuicyjny pulpit nawigacyjny AxeOS, który uprościł konfigurację i monitorowanie urządzenia. Dodatkowy wkład Bena obejmował ustanowienie możliwości produkcyjnych i stworzenie Public Pool, puli mining o otwartym kodzie źródłowym zoptymalizowanej pod kątem urządzeń Bitaxe. To oparte na współpracy podejście pokazało, w jaki sposób zasady open source mogą przyspieszyć rozwój wykraczający poza to, co każdy indywidualny współpracownik mógłby osiągnąć w pojedynkę.


Społeczność OSMU wspierała również integracyjne środowisko, w którym nowicjusze mogli się uczyć i wnosić swój wkład niezależnie od ich początkowej wiedzy technicznej. Własna podróż Bena od nowicjusza lutowania do głównego producenta jest przykładem tego przyjaznego podejścia do rozwoju umiejętności. Zaangażowanie społeczności w edukację i wzajemne wsparcie stworzyło cnotliwy cykl, w którym doświadczeni członkowie mentorowali nowicjuszy, którzy następnie sami stali się współtwórcami. Model ten okazał się niezbędny do skalowania projektu poza jego pierwotny zakres i ustanowienia zrównoważonego ekosystemu dla ciągłych innowacji i rozwoju.


### Wizja zdecentralizowanego Mining i jego przyszłe oddziaływanie


Długoterminowa wizja Skota dla Bitaxe wykracza daleko poza stworzenie kolejnego urządzenia mining: jest to fundamentalna transformacja krajobrazu Bitcoin mining. Ambitny cel wyprodukowania miliona jednoterahashowych górników stworzyłby exahash rozproszonej mocy mining, stanowiąc znaczący krok w kierunku decentralizacji mining. Wizja ta odnosi się do krytycznych obaw związanych z centralizacją mining, gdzie duże pule i operacje przemysłowe mogą potencjalnie podlegać presji ze strony rządu lub regulacjom prawnym. Poprzez dystrybucję energii mining wśród niezliczonych górników domowych, sieć staje się bardziej odporna i zgodna ze zdecentralizowanymi zasadami Bitcoin.


Model ekonomiczny wspierający tę wizję opiera się na unikalnych cechach domowego mining, w którym koszty infrastruktury są zasadniczo zerowe, a górnicy mogą działać przy minimalnym nadzorze. W przeciwieństwie do przemysłowych operacji mining, które wymagają ogromnych inwestycji kapitałowych w obiekty, infrastrukturę energetyczną i systemy chłodzenia, domowi górnicy mogą po prostu podłączyć urządzenia do istniejących gniazdek elektrycznych i połączeń internetowych. Podejście to teoretycznie mogłoby przynieść znaczną szybkość hashowania online bez tradycyjnych barier wejścia, które charakteryzują operacje mining na dużą skalę.


Sukces projektu już zaczął wpływać na szerszy ekosystem Bitcoin mining, z potencjałem zainspirowania innych producentów do przyjęcia modeli rozwoju open source. Rentowność finansowa wykazana przez producentów Bitaxe dowodzi, że sprzęt open source może odnieść sukces komercyjny przy jednoczesnym zachowaniu przejrzystości i zaangażowania społeczności. Ponieważ projekt nadal ewoluuje wraz z nowymi integracjami chipów, ulepszonymi projektami i rozszerzonymi partnerstwami produkcyjnymi, służy on jako dowód koncepcji, w jaki sposób Bitcoin mining może powrócić do swoich zdecentralizowanych korzeni, jednocześnie wykorzystując nowoczesną technologię ASIC. Ostateczny cel wykracza poza zwykłą dystrybucję hash rate i obejmuje wpływ edukacyjny, zapewniając większej liczbie osób bezpośredni kontakt z fundamentalnym procesem Bitcoin mining i wspierając głębsze zrozumienie modelu bezpieczeństwa sieci.


## Czym jest Bitaxe?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Przegląd sprzętu i możliwości


Ekosystem Bitaxe obejmuje wiele iteracji sprzętu, z których każda została zaprojektowana w celu optymalizacji różnych aspektów doświadczenia mining przy jednoczesnym zachowaniu podstawowej filozofii dostępności open-source. Urządzenia te służą nie tylko jako funkcjonalny sprzęt mining, ale także jako narzędzia edukacyjne, które pozwalają użytkownikom zrozumieć zawiłe relacje między chipami ASIC, mikrokontrolerami i procesem Bitcoin mining. Zrozumienie filozofii projektowania i technicznej implementacji Bitaxe zapewnia cenny wgląd w to, jak działa nowoczesny sprzęt mining zarówno na poziomie komponentów, jak i systemu.



### Bitaxe Max, implementacja pierwszej generacji


Bitaxe Max stanowi fundamentalną implementację koncepcji Bitaxe, wykorzystując układ BM1397 ASIC pierwotnie opracowany przez Bitmain dla serii S17 mining. Ta integracja chipów pokazuje, w jaki sposób sprzęt open-source może zmienić przeznaczenie istniejącej technologii ASIC w celu stworzenia dostępnych rozwiązań mining. Bitaxe Max zapewnia szacunkową szybkość hashowania od 300 do 400 gigahashy na sekundę, pozycjonując go jako edukacyjną i eksperymentalną platformę mining, a nie rozwiązanie na skalę komercyjną.


Integracja układu BM1397 z Bitaxe Max wymagała starannego rozważenia zarządzania energią, kontroli termicznej i protokołów komunikacyjnych. Konstrukcja płyty uwzględnia specyficzne wymagania tego ASIC, zapewniając jednocześnie niezbędne obwody pomocnicze dla stabilnej pracy. Implementacja ta pokazuje, w jaki sposób rozwój sprzętu open-source może wykorzystać istniejącą technologię półprzewodnikową do tworzenia nowych aplikacji i możliwości uczenia się w ramach społeczności mining.


### Bitaxe Ultra, zaawansowana technologia chipów


Bitaxe Ultra reprezentuje ewolucję platformy Bitaxe, zawierając bardziej zaawansowany układ BM1366 ASIC z serii S19 firmy Bitmain. Ta nowsza technologia chipów zapewnia lepszą wydajność i charakterystykę wydajności platformy Bitaxe, zachowując tę samą podstawową filozofię projektowania. Aktualizacja do układu BM1366 demonstruje zdolność platformy do adaptacji i zaangażowanie społeczności we włączanie postępu technologicznego do rozwiązań mining typu open-source.


Przejście z układu BM1397 na BM1366 wymagało modyfikacji systemów zasilania płyty, zarządzania temperaturą i algorytmów sterowania. Zmiany te ilustrują iteracyjny charakter rozwoju sprzętu i znaczenie zachowania kompatybilności przy jednoczesnym zwiększaniu wydajności. Implementacja Bitaxe Ultra zapewnia użytkownikom dostęp do nowszej technologii ASIC, zachowując jednocześnie edukacyjny i eksperymentalny charakter platformy.


### Mikrokontroler i systemy komunikacyjne


Sercem każdego urządzenia Bitaxe jest mikrokontroler ESP, który służy jako główny interfejs między użytkownikiem a chipem ASIC. Mikrokontroler ten obsługuje specjalistyczne oprogramowanie opracowane przez społeczność Open Source Miners United (OSMU), umożliwiając precyzyjną kontrolę nad parametrami pracy ASIC. Komunikacja między mikrokontrolerem a ASIC odbywa się za pośrednictwem starannie zaprojektowanych szeregowych linii komunikacyjnych, które są wytrawione bezpośrednio na płytce drukowanej w postaci widocznych ścieżek.


Rola mikrokontrolera wykracza poza proste sterowanie ASIC: obejmuje zarządzanie energią, monitorowanie temperatury i funkcje interfejsu użytkownika. Dzięki zintegrowanemu ekranowi użytkownicy mogą monitorować krytyczne parametry operacyjne, takie jak temperatura, szybkość mieszania, adres IP i inne istotne statystyki mining. Ten system informacji zwrotnej w czasie rzeczywistym zapewnia cenny wgląd w wydajność urządzenia i pomaga użytkownikom zoptymalizować działanie mining, jednocześnie ucząc się o zachowaniu sprzętu.


### Zarządzanie zasilaniem i kwestie bezpieczeństwa


Platforma Bitaxe działa w oparciu o ścisłe wymagania dotyczące zasilania 5 V, co sprawia, że właściwy dobór zasilania ma kluczowe znaczenie dla długowieczności i bezpieczeństwa urządzenia. System zarządzania energią na płytach Bitaxe zawiera zaawansowane obwody zaprojektowane do regulacji napięcia dostarczanego do układu ASIC, jednocześnie monitorując zużycie energii w różnych trybach pracy. Ta zdolność zarządzania energią pozwala urządzeniu działać wydajnie w całym zakresie wewnętrznych częstotliwości i napięć, zwykle zużywając od 5 do 25 watów w zależności od konfiguracji.


Zrozumienie wymagań dotyczących zasilania staje się kluczowe, gdy weźmie się pod uwagę, że nieprawidłowe zastosowanie napięcia może trwale uszkodzić urządzenie. Zależność między częstotliwością, napięciem, poborem mocy i szybkością mieszania pokazuje podstawowe zasady działania ASIC, które mają zastosowanie do całego sprzętu mining. Użytkownicy mogą eksperymentować z różnymi ustawieniami zasilania, aby zrozumieć kompromisy wydajności nieodłącznie związane z operacjami mining, zdobywając praktyczne doświadczenie z koncepcjami, które mają zastosowanie do implementacji mining na większą skalę.


### Solo Mining Koncentracja i uczestnictwo w sieci


Platforma Bitaxe jest w szczególności ukierunkowana na solowe aplikacje mining, w których indywidualni górnicy próbują rozwiązywać bloki Bitcoin niezależnie, zamiast uczestniczyć w dużych pulach mining. Chociaż wskaźnik hashowania urządzeń Bitaxe sprawia, że pomyślne odkrycie bloku jest statystycznie mało prawdopodobne, podejście to służy ważnym celom edukacyjnym i filozoficznym w społeczności Bitcoin. Solo mining z urządzeniami Bitaxe pomaga użytkownikom zrozumieć podstawową mechanikę systemu Bitcoin proof-of-work, jednocześnie przyczyniając się do decentralizacji sieci.


Nacisk na solo mining odzwierciedla zaangażowanie społeczności OSMU w zachęcanie do indywidualnego uczestnictwa w modelu bezpieczeństwa Bitcoin. Zapewniając dostępny sprzęt, który może działać niezależnie, platforma Bitaxe umożliwia użytkownikom uruchamianie własnych operacji mining bez polegania na infrastrukturze puli. Takie podejście sprzyja głębszemu zrozumieniu mechanizmu konsensusu Bitcoin, jednocześnie wspierając zdecentralizowany charakter sieci poprzez zwiększoną różnorodność górników.


### Ewolucja sprzętu i ulepszenia produkcji


Platforma Bitaxe stale ewoluuje dzięki opiniom społeczności i optymalizacji produkcji, a nowsze wersje zawierają ulepszenia, które poprawiają możliwości produkcyjne i wrażenia użytkownika. Aktualizacje wersji zazwyczaj koncentrują się na wydajności produkcji, a nie na fundamentalnych zmianach wydajności, zapewniając, że obecni użytkownicy nie staną w obliczu presji przestarzałości. Funkcje takie jak przejście ze złącza micro-USB na USB-C i ulepszone systemy połączeń zasilania odzwierciedlają uwagę społeczności na praktyczne ulepszenia użyteczności.


To ewolucyjne podejście pokazuje korzyści płynące z rozwoju sprzętu typu open source, gdzie wkład społeczności napędza stopniowe ulepszenia, które przynoszą korzyści wszystkim użytkownikom. Filozofia "jeśli hashuje, to hashuje" podkreśla skupienie platformy na funkcjonalności, a nie na ciągłych aktualizacjach, zachęcając użytkowników do utrzymywania i obsługi swoich urządzeń zamiast poszukiwania najnowszych wersji. Takie podejście wspiera zrównoważone praktyki sprzętowe przy jednoczesnym zachowaniu wartości edukacyjnej Bitaxe.


## Gdzie mogę dowiedzieć się więcej?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

Projekt Bitaxe reprezentuje kompleksową inicjatywę mining o otwartym kodzie źródłowym, która wykracza daleko poza pojedyncze urządzenie. Zrozumienie, gdzie znaleźć wiarygodne informacje, zasoby techniczne i wsparcie społeczności ma kluczowe znaczenie dla każdego, kto chce zaangażować się w ten ekosystem. Niniejszy rozdział zawiera kompletny przewodnik po najważniejszych platformach i zasobach, które stanowią podstawę społeczności Bitaxe i Open Source Miners United (OSMU).


### Bitaxe.org, centralne centrum


Witryna Bitaxe.org służy jako główna brama do wszystkich informacji i zasobów związanych z projektem. Ta scentralizowana platforma działa jako pierwszy punkt odniesienia za każdym razem, gdy chcesz dowiedzieć się więcej o urządzeniach Bitaxe lub poznać inne projekty w ramach społeczności OSMU. Projekt strony internetowej kładzie nacisk na dostępność i organizację, prezentując odwiedzającym starannie wyselekcjonowane linki, które łączą się z różnymi specjalistycznymi zasobami w całym ekosystemie.


Znaczenie tego centralnego ośrodka jest nie do przecenienia, ponieważ eliminuje on zamieszanie, które często towarzyszy zdecentralizowanym projektom open source. Zamiast przeszukiwać wiele platform lub polegać na potencjalnie nieaktualnych informacjach z nieoficjalnych źródeł, użytkownicy mogą zaufać Bitaxe.org, aby zapewnić aktualne, zweryfikowane linki do wszystkich niezbędnych zasobów. Takie podejście zapewnia, że zarówno nowicjusze, jak i doświadczeni członkowie społeczności mogą skutecznie zlokalizować konkretne informacje, których potrzebują do swoich projektów.


### Zasoby techniczne i materiały rozwojowe


Repozytorium plików projektowych sprzętu na GitHub stanowi jeden z najcenniejszych zasobów dla każdego zainteresowanego zrozumieniem lub budową urządzeń Bitaxe. To publiczne repozytorium zawiera kompleksową dokumentację, która obejmuje każdy aspekt procesu projektowania sprzętu, od wstępnych koncepcji po ostateczne specyfikacje produkcyjne. Repozytorium zawiera szczegółowe obrazy, cele projektu, opisy funkcji i objaśnienia wbudowanych komponentów, które zapewniają zarówno głębię techniczną, jak i praktyczne wskazówki.


Dla osób zainteresowanych produkcją własnych urządzeń, repozytorium zawiera określone pliki dokumentacji, takie jak building.md, który zawiera instrukcje krok po kroku dla całego procesu produkcyjnego. Dokumentacja ta obejmuje narzędzia programowe wymagane do projektowania PCB, procedury wysyłania plików do producentów oraz kroki związane z odbiorem i walidacją wyprodukowanych PCB. Ten poziom szczegółowości gwarantuje, że osoby indywidualne lub małe organizacje mogą z powodzeniem poruszać się po procesie produkcyjnym bez dużego wcześniejszego doświadczenia w produkcji sprzętu.


Repozytorium ESP-Miner służy jako centralna lokalizacja dla całego kodu i dokumentacji związanej z oprogramowaniem układowym. To repozytorium GitHub zawiera każdą linię kodu napisaną dla oprogramowania układowego Bitaxe, wraz z obszerną dokumentacją, która wyjaśnia wymagania systemowe, specyfikacje sprzętowe i opcje konfiguracji. Struktura repozytorium została zaprojektowana tak, aby pomieścić zarówno użytkowników, którzy preferują wstępnie skompilowane pliki binarne, jak i programistów, którzy chcą zbudować oprogramowanie układowe z kodu źródłowego.


Dokumentacja w tym repozytorium zawiera szczegółowe sekcje dotyczące wymagań sprzętowych, opcji wstępnej konfiguracji i zalecanych wartości dla różnych ustawień. Informacje te okazują się nieocenione dla użytkowników, którzy chcą dostosować swoje urządzenia lub rozwiązać określone problemy. Dodatkowo, repozytorium zawiera informacje o nowszych rozwiązaniach, takich jak integracja z Raspberry Pi, zapewniając, że dokumentacja pozostaje aktualna wraz z trwającą ewolucją projektu.


### Narzędzia do zarządzania i konserwacji urządzeń


Bitaxe web flasher to praktyczne rozwiązanie do konserwacji i aktualizacji urządzeń. To narzędzie internetowe pozwala użytkownikom na flashowanie oprogramowania sprzętowego do swoich urządzeń bez konieczności korzystania ze specjalistycznego oprogramowania lub skomplikowanych procedur wiersza poleceń. Flasher obsługuje wiele wariantów urządzeń, w tym Bitaxe Ultra z różnymi wersjami portów i starsze modele Bitaxe Max. Użytkownicy mogą wybrać pomiędzy aktualizacją istniejącego oprogramowania sprzętowego za pośrednictwem interfejsu internetowego lub wykonaniem pełnego resetu fabrycznego za pomocą połączeń USB.


Narzędzie to stanowi odpowiedź na jedno z najczęstszych wyzwań stojących przed entuzjastami sprzętu komputerowego: utrzymanie i aktualizację oprogramowania sprzętowego urządzeń. Zapewniając przyjazny dla użytkownika interfejs sieciowy, flasher eliminuje wiele barier technicznych, które w przeciwnym razie mogłyby uniemożliwić użytkownikom aktualizowanie urządzeń do najnowszych wersji oprogramowania układowego. Konstrukcja narzędzia stawia na prostotę przy jednoczesnym zachowaniu elastyczności potrzebnej do różnych konfiguracji urządzeń i scenariuszy aktualizacji.


### Platformy społecznościowe i kanały komunikacji


Serwer Discord stanowi serce interakcji i wsparcia społeczności w czasie rzeczywistym w ramach ekosystemu Bitaxe. Organizacja serwera odzwierciedla różnorodne zainteresowania i potrzeby członków społeczności, ze starannie zorganizowanymi kanałami, które ułatwiają ukierunkowane dyskusje na określone tematy. Nowi członkowie napotykają proces weryfikacji, który wymaga przeczytania i zaakceptowania zasad społeczności, zapewniając, że wszyscy uczestnicy rozumieją oczekiwania dotyczące pełnej szacunku i produktywnej interakcji.


Struktura kanałów serwera obejmuje ogólne obszary dyskusyjne obejmujące tematy takie jak integracja energii słonecznej, baseny mining i dyskusje związane z Bitcoin. Bardziej wyspecjalizowane sekcje koncentrują się na konkretnych urządzeniach, w tym na dedykowanych kanałach dla wariantów Bitaxe Ultra, Hex i Supra. Kanał poświęcony oprogramowaniu układowemu zapewnia przestrzeń do dyskusji technicznych na temat rozwoju oprogramowania i rozwiązywania problemów, podczas gdy oficjalny kanał poświęcony wydaniom zapewnia członkom społeczności otrzymywanie na czas powiadomień o nowych wydarzeniach.


Zawiera również obszar subskrypcji, który zapewnia dodatkowe korzyści członkom społeczności, którzy zdecydują się wesprzeć projekt finansowo. To wielopoziomowe podejście pozwala społeczności oferować ulepszone usługi przy jednoczesnym zachowaniu otwartego dostępu do podstawowych informacji i kanałów wsparcia. Kanał pomocy służy jako dedykowana przestrzeń do rozwiązywania problemów i pomocy technicznej, zapewniając użytkownikom szybkie wsparcie w przypadku napotkania trudności.



Open Source Miners United wiki (osmu.wiki) zapewnia kompleksową dokumentację, która uzupełnia dyskusje prowadzone w czasie rzeczywistym na Discordzie. W przeciwieństwie do platform opartych na czacie, wiki oferuje uporządkowaną, przeszukiwalną dokumentację, która obejmuje wszystkie aspekty projektu Bitaxe i powiązanych inicjatyw. Sposób organizacji odzwierciedla strukturę projektu, z dedykowanymi sekcjami dla różnych serii urządzeń i kompleksowymi przewodnikami konfiguracji.


Otwarty charakter wiki pozwala członkom społeczności na bezpośredni wkład w dokumentację. Użytkownicy mogą edytować strony, przesyłać poprawki i dodawać nowe informacje poprzez integrację z GitHub, zapewniając, że baza wiedzy pozostaje aktualna i przejrzysta. To podejście oparte na współpracy wykorzystuje zbiorową wiedzę społeczności, jednocześnie utrzymując kontrolę jakości poprzez proces przeglądu przesłanych zmian.


Wiki zawiera praktyczne zasoby, takie jak przewodniki konfiguracji PDF, które zawierają instrukcje krok po kroku dotyczące konfiguracji i użytkowania urządzenia. Przewodniki te służą jako cenne odniesienia zarówno dla nowych użytkowników, jak i doświadczonych członków społeczności, którzy potrzebują szybkiego dostępu do określonych procedur lub szczegółów konfiguracji.


### Informacje dotyczące zakupów i dostawców


Legalna lista Bitaxe jest odpowiedzią na krytyczną potrzebę społeczności sprzętu open-source: identyfikację godnych zaufania sprzedawców i unikanie nieuczciwych sprzedawców. Ta wyselekcjonowana lista zawiera zweryfikowanych sprzedawców i producentów, którzy spełniają określone kryteria legalności i wsparcia społeczności. Każda lista zawiera bezpośrednie linki do stron internetowych sprzedawców, informacje regionalne i opisy firm, które pomagają użytkownikom w podejmowaniu świadomych decyzji zakupowych.


Co ważne, lista wskazuje, czy każdy sprzedawca wnosi swój wkład w społeczność OSMU, zarówno finansowo, jak i poprzez inne formy wsparcia. Ta przejrzystość pomaga członkom społeczności zrozumieć, którzy sprzedawcy aktywnie wspierają rozwój i zrównoważony rozwój projektu. Lista służy również jako środek ochronny przed powszechnymi oszustwami, takimi jak nieautoryzowane zamówienia przedpremierowe na niewydane produkty, które w przeszłości powodowały problemy w społeczności.


Nacisk na linki niepowiązane pokazuje zaangażowanie społeczności w dostarczanie bezstronnych rekomendacji sprzedawców. Użytkownicy mogą ufać, że rekomendacje są oparte na legitymacji sprzedawcy i wkładzie społeczności, a nie na zachętach finansowych, zapewniając, że decyzje zakupowe wspierają zarówno indywidualne potrzeby, jak i zrównoważony rozwój społeczności.



# Oprogramowanie i operacje

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## Czym jest AxeOS?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS to oprogramowanie układowe i interfejs sieciowy dla urządzeń Bitaxe mining, zapewniający użytkownikom pełną kontrolę i możliwości monitorowania za pośrednictwem intuicyjnego pulpitu nawigacyjnego opartego na przeglądarce. System ten przekształca złożone zadanie zarządzania ASIC w przystępne doświadczenie, umożliwiając górnikom monitorowanie wydajności, dostosowywanie ustawień i zarządzanie wieloma urządzeniami z poziomu jednego interfejsu. Zrozumienie AxeOS jest niezbędne do zmaksymalizowania potencjału urządzenia Bitaxe i utrzymania optymalnych operacji mining.


### Przegląd pulpitu nawigacyjnego i podstawowe wskaźniki


Pulpit nawigacyjny AxeOS służy jako główne okno na wydajność urządzenia Bitaxe, prezentując krytyczne dane mining w zorganizowanym formacie w czasie rzeczywistym. Po przejściu do adresu IP urządzenia Bitaxe natychmiast wyświetlane są cztery kluczowe wskaźniki wydajności, które definiują bieżący stan operacji mining. Wskaźnik szybkości mieszania pokazuje rzeczywistą szybkość obliczeniową, jaką wytwarza układ ASIC podczas przetwarzania bieżącego szablonu bloku, zapewniając natychmiastową informację zwrotną na temat podstawowej funkcjonalności urządzenia.


Obok wskaźnika hashowania, licznik udziałów śledzi każde prawidłowe rozwiązanie, które urządzenie Bitaxe przesyła do puli mining, zwiększając się z każdym pomyślnym przesłaniem i służąc jako bezpośrednia miara wkładu urządzenia w wysiłki puli mining. Wskaźnik wydajności zapewnia kluczowy wgląd w wydajność energetyczną urządzenia, obliczając stosunek szybkości mieszania do zużycia energii, pomagając zoptymalizować rentowność operacji. Najlepszy wskaźnik trudności zachowuje rekord najwyższego poziomu trudności, jaki urządzenie kiedykolwiek znalazło, utrzymując to osiągnięcie nawet po ponownym uruchomieniu i aktualizacji, resetując się tylko po wykonaniu pełnego flashowania fabrycznego.


Rozszerzalny system menu pulpitu nawigacyjnego, kontrolowany za pomocą przycisku przełączania, zapewnia dostęp do wszystkich funkcji AxeOS przy zachowaniu przejrzystego interfejsu. Wykres szybkości mieszania na żywo stanowi jedną z najcenniejszych funkcji, wyświetlając dane o wydajności w czasie rzeczywistym, które stają się dokładniejsze i bardziej pouczające, im dłużej utrzymujesz sesję. Sekcje zasilania, ciepła i wydajności zapewniają kompleksowe monitorowanie stanu operacyjnego urządzenia, w tym ostrzeżenia o napięciu wejściowym, które ostrzegają o potencjalnych problemach z zasilaniem, zapewniając jednocześnie ciągłą pracę w bezpiecznych parametrach.


### Zaawansowane monitorowanie i informacje o systemie


Możliwości monitorowania AxeOS wykraczają daleko poza podstawowe śledzenie szybkości mieszania, zapewniając szczegółowy wgląd w każdy aspekt działania urządzenia Bitaxe. Sekcja zasilania wyświetla obliczone zużycie energii pochodzące z wbudowanych układów scalonych, pomiary napięcia wejściowego z połączenia zasilacza i żądane poziomy napięcia ASIC. Gdy wystąpią spadki napięcia, AxeOS natychmiast wyświetla powiadomienia ostrzegawcze, choć zazwyczaj nie mają one wpływu na działanie mining i po prostu wskazują potencjalne możliwości optymalizacji zasilania.


Monitorowanie temperatury koncentruje się na zarządzaniu temperaturą chipa ASIC, z odczytami pobieranymi ze strategicznych miejsc na urządzeniu, aby zapewnić dokładne dane termiczne z odpowiednimi przesunięciami dla dokładności na poziomie chipa. Wyświetlacze częstotliwości i napięcia oferują informacje zwrotne w czasie rzeczywistym na temat parametrów strojenia ASIC, przy czym zmierzone napięcie reprezentuje najdokładniejszy dostępny odczyt, pobrany bezpośrednio w lokalizacji chipa ASIC. Ta precyzja umożliwia precyzyjne dostrojenie parametrów wydajności przy zachowaniu bezpiecznych warunków pracy.


Sekcja stanu połączenia zapewnia natychmiastowy wgląd w konfigurację puli mining, wyświetlając bieżący adres URL warstwy, port i identyfikację użytkownika. W przypadku urządzeń podłączonych do publicznych pul AxeOS generuje wygodne szybkie łącza, które przenoszą użytkownika bezpośrednio do interfejsu internetowego puli, gdzie można uzyskać dostęp do szczegółowych statystyk, list urządzeń i historycznych danych dotyczących wydajności. Ta integracja usprawnia proces monitorowania, łącząc informacje na poziomie urządzenia i puli w płynnym przepływie pracy.


### Zarządzanie rojem i kontrola wielu urządzeń


Funkcjonalność Swarm stanowi rozwiązanie AxeOS dla złożoności zarządzania wieloma urządzeniami Bitaxe w sieci, eliminując potrzebę zapamiętywania i nawigowania do wielu adresów IP. Ten scentralizowany system zarządzania umożliwia dodawanie urządzeń poprzez proste wprowadzenie ich adresów IP, automatyczne wykrywanie aktywnych górników Bitaxe i włączanie ich do ujednoliconego pulpitu sterowania. Po skonfigurowaniu, Swarm zapewnia kompleksową kontrolę nad całą operacją mining z poziomu jednego interfejsu.


Za pomocą interfejsu Swarm można wykonywać krytyczne zadania zarządzania na wielu urządzeniach jednocześnie lub indywidualnie, w tym zmiany konfiguracji puli, ponowne uruchamianie urządzeń, dostosowywanie częstotliwości i monitorowanie wydajności. To scentralizowane podejście znacznie zmniejsza obciążenie administracyjne związane z zarządzaniem dużymi operacjami mining, zapewniając jednocześnie spójną konfigurację na wszystkich urządzeniach. System zachowuje indywidualną tożsamość urządzenia, zapewniając jednocześnie zbiorowe możliwości zarządzania, zapewniając optymalną równowagę między szczegółową kontrolą a wydajnością operacyjną.


Pulpit nawigacyjny Swarm przedstawia każde zarządzane urządzenie z jego aktualnym stanem, wskaźnikami wydajności i kontrolkami szybkiego dostępu, umożliwiając szybką reakcję na problemy z wydajnością lub zmiany konfiguracji. Funkcjonalność ta okazuje się szczególnie cenna dla górników obsługujących wiele urządzeń w różnych lokalizacjach lub tych, którzy często dostosowują parametry mining w oparciu o warunki rynkowe lub wydajność puli.


### Zarządzanie konfiguracją i ustawienia systemowe


Sekcja ustawień AxeOS zapewnia kompleksową kontrolę nad każdym konfigurowalnym aspektem urządzenia Bitaxe, od łączności sieciowej po parametry mining i optymalizację sprzętu. Konfiguracja sieci rozpoczyna się od konfiguracji Wi-Fi, w której należy określić nazwę sieci i hasło, przy czym AxeOS zaleca jednowyrazowe nazwy sieci bez spacji, aby zapewnić niezawodną łączność. System obsługuje cały proces konfiguracji sieci bezprzewodowej, umożliwiając zdalne zarządzanie i monitorowanie.


Konfiguracja Mining koncentruje się na ustawieniach warstwy, w których określa się adres URL wybranej puli mining bez prefiksów protokołów lub numerów portów, które są obsługiwane w oddzielnych polach. Pole użytkownika stratum uwzględnia różne wymagania puli, obsługując zarówno adresy Bitcoin dla solo mining, jak i systemy nazw użytkowników dla puli mining, z możliwością dołączania identyfikatorów urządzeń dla operacji na wielu urządzeniach. Niedawno dodana funkcja hasła warstwy obsługuje pule wymagające uwierzytelnienia, chociaż większość pul publicznych działa bez tego wymogu.


Optymalizacja sprzętowa poprzez regulację częstotliwości i napięcia rdzenia stanowi najpotężniejszą możliwość dostrajania wydajności AxeOS. W zależności od wersji urządzenia i przeglądarki, ustawienia te mogą być wyświetlane jako rozwijane menu ze wstępnie ustawionymi konfiguracjami lub jako otwarte pola umożliwiające wprowadzenie niestandardowych wartości. Domyślne ustawienia częstotliwości 485 MHz i napięcia rdzenia 1200 mV zapewniają stabilną pracę podczas wstępnych testów, podczas gdy zaawansowani użytkownicy mogą zoptymalizować te parametry pod kątem maksymalnej wydajności lub wydajności w oparciu o ich specyficzne wymagania i warunki pracy.


### Konserwacja systemu i funkcje zaawansowane


AxeOS zawiera zaawansowane funkcje konserwacji systemu zaprojektowane w celu utrzymania maksymalnej wydajności urządzenia Bitaxe, zapewniając jednocześnie informacje diagnostyczne do rozwiązywania problemów i optymalizacji. System aktualizacji usprawnia zarządzanie oprogramowaniem układowym, wyświetlając najnowszą dostępną wersję bezpośrednio w interfejsie i zapewniając bezpośrednie linki do pobrania oficjalnych plików oprogramowania układowego. Ta integracja eliminuje potrzebę ręcznego nawigowania po repozytoriach GitHub lub zarządzania pobieraniem plików, upraszczając proces aktualizacji do kilku kliknięć.


Interfejs aktualizacji akceptuje odpowiednio nazwane pliki oprogramowania układowego, w szczególności esp-miner.bin i www.bin, zapewniając kompatybilność i zapobiegając błędom instalacji. Dla użytkowników doświadczających trudności ze standardowym procesem aktualizacji, AxeOS zapewnia odniesienia do kompleksowych procedur fabrycznego flashowania, które mogą przywrócić urządzenia do pierwotnej funkcjonalności. To podwójne podejście uwzględnia zarówno rutynowe aktualizacje, jak i scenariusze odzyskiwania.


System rejestrowania zapewnia wgląd w czasie rzeczywistym w działanie urządzenia, wyświetlając szczegółowe informacje o modelach chipów ASIC, czasie pracy systemu, stanie łączności Wi-Fi, dostępnej pamięci, wersjach oprogramowania układowego i wersjach płyt. Dzienniki te są nieocenione dla programistów i zaawansowanych użytkowników, którzy chcą zrozumieć zachowanie urządzenia, zdiagnozować problemy lub zoptymalizować wydajność. Przeglądarka dziennika w czasie rzeczywistym prezentuje dane operacyjne na żywo, w tym przetwarzanie nonce, obliczenia trudności i parametry przesyłania mining, oferując bezprecedensowy wgląd w sam proces mining.


Dodatkowe funkcje systemu obejmują kontrolę orientacji ekranu dla urządzeń używanych w niestandardowych obudowach, odwrócenie polaryzacji wentylatora dla wyspecjalizowanych konfiguracji chłodzenia oraz automatyczne sterowanie wentylatorem, które dostosowuje chłodzenie w oparciu o temperaturę ASIC. Ręczna kontrola prędkości wentylatora zapewnia precyzyjne zarządzanie chłodzeniem, gdy systemy automatyczne nie spełniają określonych wymagań. Wszystkie zmiany konfiguracji wymagają zapisania i ponownego uruchomienia urządzenia, aby odniosły skutek, zapewniając stabilną pracę i zapobiegając częściowym stanom konfiguracji, które mogłyby wpłynąć na wydajność mining.



# Społeczność i współpraca

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Przegląd wkładu open source

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub i jego rola w rozwoju oprogramowania


GitHub stanowi fundamentalną zmianę w sposobie zarządzania projektami rozwoju oprogramowania i udostępniania ich globalnej społeczności programistów. Jako platforma oparta na chmurze, która obsługuje projekty rozwoju oprogramowania przy użyciu Git, rozproszonego systemu kontroli wersji, GitHub umożliwia programistom płynną współpracę nad projektami niezależnie od ich fizycznej lokalizacji. Platforma służy zarówno jako narzędzie techniczne, jak i sieć społecznościowa dla programistów, umożliwiając im śledzenie zmian, scalanie aktualizacji, utrzymywanie różnych wersji kodu i przyczynianie się do inicjatyw open source, takich jak projekt BitX z Open Source Miners United.


Siła GitHub leży w jego zdolności do upraszczania złożonego procesu wspólnego rozwoju. Gdy wielu deweloperów pracuje nad tym samym projektem, GitHub zapewnia infrastrukturę do zarządzania wkładami, przeglądania zmian, obsługi problemów projektowych i prowadzenia kompleksowej dokumentacji. To oparte na współpracy podejście sprawiło, że GitHub stał się istotnym elementem nowoczesnych przepływów pracy związanych z tworzeniem oprogramowania, zmieniając sposób, w jaki zarówno indywidualni programiści, jak i duże organizacje podchodzą do zarządzania projektami i udostępniania kodu.


### Poruszanie się po GitHub Interface i struktura repozytorium


Zrozumienie interfejsu GitHub zaczyna się od rozpoznania kluczowych elementów, które składają się na każdą stronę repozytorium. Górny pasek nawigacyjny zawiera kilka krytycznych sekcji, w tym Kod, Zgłoszenia, Wnioski o ściągnięcie, Dyskusje, Działania, Projekty, Bezpieczeństwo i Statystyki. Każda sekcja służy określonemu celowi w ekosystemie zarządzania projektami, przy czym sekcja Kod wyświetla rzeczywiste pliki i foldery składające się na projekt.


Sama struktura repozytorium odzwierciedla podejście organizacyjne opiekunów projektu. Niektóre repozytoria zawierają tylko jeden plik, być może prosty skrypt powłoki, podczas gdy inne, takie jak projekt sprzętowy BitX, zawierają wiele plików zorganizowanych w katalogi i podkatalogi. Nazwa repozytorium pojawia się w widocznym miejscu i służy zarówno jako identyfikator, jak i krótki opis celu projektu. Istotne elementy interaktywne obejmują przycisk Watch do otrzymywania powiadomień o aktualizacjach repozytorium, przycisk Fork do tworzenia osobistych kopii repozytorium oraz przycisk Star, który działa jako system poparcia społeczności podobny do funkcji "kciuka w górę".


Sekcja About zawiera kluczowe informacje o projekcie w skondensowanym formacie, w tym jednowierszowy opis, informacje licencyjne i kluczowe szczegóły projektu. W przypadku projektu BitX sekcja ta identyfikuje go jako "open source ASIC Bitcoin miner hardware" i określa licencję GPL 3.0. Zrozumienie zasad licencjonowania jest szczególnie ważne, ponieważ GitHub działa jako platforma open source, na której publiczne repozytoria są dostępne dla całej społeczności, ale zawartość może być wykorzystywana i rozpowszechniana wyłącznie zgodnie z zasadami zgodności każdej licencji.


### Praca z gałęziami i wersjami projektu


Koncepcja gałęzi stanowi jedną z najpotężniejszych funkcji GitHub do zarządzania różnymi wersjami i ścieżkami rozwoju w ramach jednego projektu. Gałąź zasadniczo tworzy kopię lub zmodyfikowaną wersję głównej bazy kodu, umożliwiając programistom pracę nad określonymi funkcjami, poprawkami błędów lub eksperymentalnymi zmianami bez wpływu na główną linię rozwoju. Gałąź główna zazwyczaj służy jako domyślna i najbardziej stabilna wersja projektu, podczas gdy dodatkowe gałęzie uwzględniają różne iteracje, fazy testowania lub zupełnie inne warianty produktu.


W projekcie sprzętowym BitX istnieje wiele gałęzi do zarządzania różnymi wersjami i konfiguracjami sprzętu. Na przykład gałąź Ultra v2 zawiera pliki specyficzne dla tej iteracji sprzętowej, podczas gdy gałąź Super 401 koncentruje się na implementacjach wykorzystujących układ S21 ASIC w celu zwiększenia wydajności. Każda gałąź może znajdować się kilka commitów przed lub za gałęzią master, wskazując zakres zmian i aktywności rozwojowej. Badając różne gałęzie, użytkownicy zauważą zupełnie inne struktury plików, dokumentację, a nawet reprezentacje wizualne, odzwierciedlające unikalne wymagania i specyfikacje każdego wariantu sprzętowego.


System gałęzi zapobiega dezorientacji wśród współtwórców i użytkowników poprzez wyraźne oddzielenie różnych ścieżek rozwoju. Zamiast mieszać funkcje eksperymentalne ze stabilnymi wydaniami lub łączyć różne wersje sprzętowe w jednym miejscu, gałęzie zapewniają czystą separację, zachowując jednocześnie możliwość scalania udanych zmian z powrotem do głównej linii rozwoju, gdy jest to właściwe. Takie podejście organizacyjne zapewnia, że użytkownicy mogą łatwo zlokalizować konkretną wersję, której potrzebują, podczas gdy programiści mogą pracować nad ulepszeniami bez zakłócania głównego projektu.


### Przyczynianie się poprzez problemy


Sekcja Problemy służy jako główny kanał komunikacji między użytkownikami a opiekunami projektu w celu zgłaszania problemów, sugerowania ulepszeń i dokumentowania błędów. Ważne jest jednak, aby zrozumieć, że sekcja Problemy jest specjalnie zaprojektowana dla uzasadnionych problemów technicznych, a nie ogólnych pytań lub próśb o wsparcie. Gdy użytkownicy napotkają rzeczywiste usterki, nieoczekiwane zachowanie lub zidentyfikują potencjalne ulepszenia, utworzenie dobrze udokumentowanego zgłoszenia pomaga całej społeczności, zwracając uwagę na problemy, które mogą mieć wpływ na wielu użytkowników.


Skuteczne zgłaszanie problemów wymaga szczegółowej dokumentacji problemu, w tym okoliczności, które do niego doprowadziły, kroków do odtworzenia problemu i wszelkich istotnych szczegółów technicznych. Projekt BitX demonstruje tę zasadę poprzez różne zamknięte problemy, które pokazują proces rozwiązywania, od początkowej identyfikacji problemu, poprzez dyskusję społeczności, aż po ostateczne rozwiązanie. Niektóre problemy skutkują ulepszeniami sprzętu, takimi jak dodanie otworów montażowych w celu zwiększenia opcji chłodzenia, podczas gdy inne mogą zostać rozwiązane poprzez edukację użytkowników lub aktualizacje oprogramowania.


Rozróżnienie między tematami i dyskusjami jest ważne dla utrzymania zorganizowanej interakcji społeczności. Podczas gdy Issues koncentrują się na konkretnych problemach technicznych, sekcja Discussions zapewnia środowisko podobne do forum dla pytań, pomysłów i ogólnego zaangażowania społeczności. Chociaż serwer Discord stał się głównym kanałem komunikacji dla społeczności BitX, sekcja GitHub Discussions pozostaje dostępna dla bardziej formalnych lub przeszukiwalnych rozmów, które korzystają ze stałej dokumentacji i łatwego odniesienia.


### Zrozumienie pull requestów


Żądania ściągnięcia stanowią mechanizm, za pomocą którego zewnętrzni współpracownicy proponują zmiany w repozytorium projektu. Gdy ktoś zidentyfikuje ulepszenie, poprawkę błędu lub nową funkcję, która przyniosłaby korzyści projektowi, może utworzyć żądanie ściągnięcia, aby przesłać swoje zmiany do przeglądu i potencjalnej integracji z główną bazą kodu. Proces ten zapewnia, że wszystkie modyfikacje przechodzą przegląd, zanim staną się częścią oficjalnego projektu, utrzymując jakość kodu i spójność projektu, jednocześnie umożliwiając wkład społeczności.


Przepływ pracy pull request zazwyczaj rozpoczyna się, gdy współautor rozwidla repozytorium, tworzy własną kopię, w której może wprowadzać zmiany, a następnie przesyła te zmiany z powrotem do oryginalnego projektu za pośrednictwem pull request. Opiekunowie projektu mogą następnie przejrzeć proponowane zmiany, omówić modyfikacje ze współautorem i ostatecznie zdecydować, czy scalić zmiany z głównym projektem. Ten wspólny proces przeglądu pomaga utrzymać standardy projektu, jednocześnie zachęcając społeczność do udziału i ulepszeń.


Zrozumienie tagów i wydań dodaje kolejną warstwę do zarządzania projektami i kontroli wersji. Tagi służą jako znaczniki na osi czasu rozwoju, identyfikując określone punkty, które reprezentują określone wersje lub kamienie milowe. W projektach sprzętowych, takich jak BitX, tagi często odpowiadają konkretnym numerom modeli lub wersjom sprzętu, zapewniając jasne punkty odniesienia dla użytkowników poszukujących określonych wersji. Wydania, częściej używane w projektach oprogramowania, reprezentują formalne dystrybucje ukończonych funkcji i poprawek błędów, którym często towarzyszą szczegółowe informacje o wydaniu i pakiety do pobrania.


Ekosystem GitHub tworzy kompleksowe środowisko współpracy open source, które wykracza daleko poza zwykłe udostępnianie plików. Dzięki zrozumieniu tych różnych komponentów i ich właściwego wykorzystania, współtwórcy mogą skutecznie uczestniczyć w projektach, pomagać w ulepszaniu projektów oprogramowania i sprzętu oraz korzystać ze zbiorowej wiedzy i wysiłków globalnej społeczności programistów. Niezależnie od tego, czy chodzi o zgłaszanie problemów, sugerowanie ulepszeń, czy dodawanie kodu, GitHub zapewnia narzędzia i strukturę niezbędną do znaczącej współpracy w świecie open source.


## Otwarte oprogramowanie w praktyce

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Opierając się na podstawach tworzenia zagadnień i eksploracji projektów open source, ten rozdział koncentruje się na praktycznych aspektach bezpośredniego wkładu poprzez pull requesty i zarządzanie repozytoriami. Zrozumienie sposobu fork repozytoriów, wprowadzania zmian i przesyłania pull requestów stanowi kluczowy zestaw umiejętności dla każdego programisty, który chce wnieść znaczący wkład w projekty open source, niezależnie od tego, czy dotyczą one tworzenia oprogramowania, czy projektowania sprzętu.


Proces wprowadzania zmian w kodzie odbywa się zgodnie ze standardowym przepływem pracy, który zapewnia integralność projektu, jednocześnie umożliwiając rozwój oparty na współpracy. Ten przepływ pracy obejmuje tworzenie własnej kopii repozytorium projektu, wprowadzanie modyfikacji w kontrolowanym środowisku, a następnie proponowanie tych zmian z powrotem do oryginalnego projektu w ramach formalnego procesu przeglądu. Chociaż przykłady w tym rozdziale koncentrują się głównie na wkładzie w oprogramowanie, te same zasady i procedury mają zastosowanie również do projektów sprzętowych obejmujących projekty PCB, schematy i inną dokumentację techniczną.


### Zrozumienie struktury widelców i repozytoriów


Podstawą współtworzenia dowolnego projektu open source jest utworzenie fork, który służy jako osobista kopia oryginalnego repozytorium. Po przejściu do repozytorium GitHub i kliknięciu przycisku "fork" tworzona jest niezależna kopia na własnym koncie GitHub, która zachowuje wyraźne połączenie z oryginalnym źródłem. To rozwidlone repozytorium pojawia się na koncie użytkownika z wyraźnym wskazaniem jego pochodzenia, wyświetlając tekst taki jak "rozwidlone z [oryginalny-właściciel]/[nazwa-repozytorium]" pod tytułem repozytorium.


Rozwidlone repozytorium działa niezależnie od oryginalnego, umożliwiając wprowadzanie zmian bez wpływu na główny projekt. Utrzymuje jednak świadomość aktualizacji oryginalnego repozytorium dzięki funkcjom synchronizacji GitHub. Gdy oryginalne repozytorium otrzymuje aktualizacje, których brakuje fork, GitHub wyświetla informacje o statusie, takie jak "Ta gałąź jest X commitów za" lub "X commitów przed", zapewniając jasny wgląd w relacje między fork a repozytorium upstream. Możesz zsynchronizować fork z oryginalnym repozytorium w dowolnym momencie, klikając przycisk "Synchronizuj fork", który pobiera najnowsze zmiany ze źródła upstream.


Relacja między fork a oryginalnym repozytorium staje się szczególnie ważna po rozpoczęciu wprowadzania zmian. W miarę wprowadzania modyfikacji i zatwierdzania ich w fork, GitHub śledzi te różnice i wyświetla je jako zatwierdzenia przed oryginalnym repozytorium. Ten system śledzenia umożliwia proces pull request, w którym można zaproponować zmiany do włączenia do głównego projektu, zachowując jednocześnie przejrzystą historię tego, co zostało zmodyfikowane.


### Konfiguracja środowiska programistycznego


Stworzenie skutecznego środowiska programistycznego wymaga zwrócenia szczególnej uwagi zarówno na ogólne narzędzia programistyczne, jak i wymagania specyficzne dla projektu. Visual Studio Code służy jako doskonałe zintegrowane środowisko programistyczne (IDE) dla większości wkładów open source, zapewniając podstawowe funkcje edycji kodu, integracji kontroli wersji i zarządzania projektami. Pierwszym krytycznym elementem jest instalacja i konfiguracja rozszerzenia Git, które umożliwia płynną integrację z repozytoriami GitHub bezpośrednio ze środowiska programistycznego.


Nowoczesne wersje Visual Studio Code zazwyczaj domyślnie zawierają obsługę Git, ale aby włączyć pełną funkcjonalność, należy uwierzytelnić się za pomocą konta GitHub. Ten proces uwierzytelniania obejmuje logowanie do GitHub za pośrednictwem IDE, co następnie umożliwia klonowanie repozytoriów, zatwierdzanie zmian i wypychanie aktualizacji bezpośrednio ze środowiska programistycznego. Integracja z GitHub pojawia się jako ikona na lewym pasku bocznym, zapewniając dostęp do funkcji klonowania repozytoriów, zarządzania gałęziami i synchronizacji bez konieczności wykonywania operacji w wierszu poleceń.


W przypadku projektów obejmujących systemy wbudowane lub określone platformy sprzętowe, niezbędne stają się dodatkowe narzędzia. Rozszerzenie ESP-IDF stanowi kluczowy komponent dla projektów ukierunkowanych na mikrokontrolery ESP32, wymagając określonej zgodności wersji w celu zapewnienia prawidłowej funkcjonalności. Proces instalacji obejmuje wybór odpowiedniej wersji ESP-IDF, konfigurację ścieżek narzędzi i konfigurację środowiska kontenera programistycznego. Wersja 5.1.3 stanowi obecnie zalecaną konfigurację dla wielu projektów opartych na ESP32, choć wymagania te mogą ewoluować wraz z aktualizacją zależności i łańcuchów narzędzi.


### Wprowadzanie zmian i zarządzanie zatwierdzeniami


Po prawidłowym skonfigurowaniu środowiska programistycznego proces tworzenia znaczącego wkładu rozpoczyna się od pobrania lub sklonowania rozwidlonego repozytorium na komputer lokalny. Można to zrobić, pobierając plik ZIP z zawartością repozytorium lub korzystając ze zintegrowanej funkcji klonowania programu Visual Studio Code, która zapewnia bardziej usprawniony przepływ pracy dla bieżącego rozwoju. Proces klonowania tworzy lokalną kopię repozytorium, która pozostaje zsynchronizowana z GitHub fork, umożliwiając pracę w trybie offline przy zachowaniu możliwości kontroli wersji.


Podczas pracy z lokalnym repozytorium uzyskuje się dostęp do pełnej struktury projektu, w tym plików kodu źródłowego, plików konfiguracyjnych, dokumentacji i wszelkich plików projektu sprzętu. Większość projektów oprogramowania układowego wykorzystuje języki programowania, takie jak C dla podstawowych funkcji, z dodatkowymi komponentami napisanymi w języku TypeScript dla interfejsów użytkownika lub Java dla określonych narzędzi. Zrozumienie struktury projektu pomaga zidentyfikować odpowiednie pliki do modyfikacji i zapewnia, że zmiany są zgodne z wzorcami architektonicznymi projektu i standardami kodowania.


Proces zatwierdzania stanowi podstawowy aspekt kontroli wersji, który wymaga starannej dbałości zarówno o dokładność techniczną, jak i przejrzystość komunikacji. Przed wprowadzeniem jakichkolwiek zmian należy dokładnie zrozumieć istniejący kod i przetestować wszelkie modyfikacje w środowisku lokalnym. Kardynalna zasada wkładu open source podkreśla, że nigdy nie należy publikować nieprzetestowanego kodu, ponieważ może to wprowadzić błędy lub luki w zabezpieczeniach, które mają wpływ na całą społeczność projektu. Ponadto, nigdy nie należy udostępniać poufnych informacji, takich jak hasła, tokeny API lub osobiste dane uwierzytelniające w publicznych repozytoriach, ponieważ informacje te stają się trwale dostępne dla każdego, kto ma dostęp do repozytorium.


### Tworzenie i zarządzanie pull requestami


Zwieńczeniem wkładu użytkownika jest utworzenie pull requesta, który służy jako formalna propozycja scalenia wprowadzonych zmian z oryginalnym repozytorium projektu. Proces ten rozpoczyna się w GitHub fork, gdzie można przejrzeć różnice między swoim repozytorium a źródłem upstream. Interfejs GitHub wyraźnie wyświetla liczbę commitów przed lub za, zapewniając natychmiastowy wgląd w zakres proponowanych zmian. Przed utworzeniem żądania ściągnięcia należy upewnić się, że repozytorium fork jest zsynchronizowane z najnowszymi zmianami w źródle, aby zminimalizować potencjalne konflikty.


Stworzenie skutecznego pull requesta wymaga czegoś więcej niż tylko przesłania zmian w kodzie. Opis pull requesta służy jako okazja do przekazania opiekunom i społeczności projektu celu, zakresu i wpływu wprowadzonych modyfikacji. Dobrze napisany opis wyjaśnia, jakie problemy rozwiązują wprowadzone zmiany, w jaki sposób zaimplementowano rozwiązanie i jakie są potencjalne implikacje dla innych części projektu. Dokumentacja ta staje się szczególnie ważna w przypadku złożonych zmian, które mogą nie być od razu oczywiste po zbadaniu samych różnic w kodzie.


Proces recenzowania reprezentuje oparty na współpracy aspekt rozwoju open source, w którym opiekunowie projektu i doświadczeni współpracownicy oceniają proponowane zmiany. Możesz poprosić o konkretnych recenzentów, którzy mają doświadczenie w obszarach, na które wpływają twoje zmiany, zapewniając, że członkowie społeczności posiadający odpowiednią wiedzę zbadają twoją pracę. Proces recenzowania może obejmować wiele iteracji, w których recenzenci przekazują informacje zwrotne, żądają modyfikacji lub proszą o dodatkowe testy. Ten wspólny proces udoskonalania pomaga utrzymać jakość kodu, zapewniając jednocześnie cenne możliwości uczenia się dla współpracowników na wszystkich poziomach doświadczenia.


Zrozumienie, że nie wszystkie pull requesty otrzymują akceptację, pomaga ustalić odpowiednie oczekiwania względem procesu wnoszenia wkładu. Opiekunowie projektu mogą odrzucać pull requesty z różnych powodów, w tym z powodu niezgodności z celami projektu, niewystarczających testów lub istnienia alternatywnych rozwiązań, które są już opracowywane. Zamiast postrzegać odrzucenie jako porażkę, należy je traktować jako okazję do wyciągnięcia wniosków z informacji zwrotnych, udoskonalenia podejścia i potencjalnego wniesienia alternatywnych rozwiązań, które lepiej spełniają potrzeby projektu. Społeczność open source rozwija się dzięki temu iteracyjnemu procesowi propozycji, przeglądu i udoskonalania, który ostatecznie napędza projekty poprzez wspólny wysiłek i wspólną wiedzę.



## Co to jest Public-Pool?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool reprezentuje rewolucyjne podejście do Bitcoin mining, które rozwiązuje wiele obaw górników związanych z tradycyjnymi pulami mining. Jako w pełni otwarta pula solo Bitcoin mining, Public Pool zasadniczo zmienia model dystrybucji nagród, do którego przyzwyczaili się górnicy. W przeciwieństwie do konwencjonalnych pul mining, w których uczestnicy dzielą się nagrodami, gdy jakikolwiek górnik w puli znajdzie blok, Public Pool działa na zasadzie solo mining, w której indywidualni górnicy zatrzymują 100% swoich nagród za blok, gdy pomyślnie wydobędą blok.


Najbardziej atrakcyjną cechą Public Pool jest jego struktura bez opłat. Gdy górnicy pomyślnie znajdą blok za pomocą Public Pool, otrzymują pełną nagrodę za blok wraz ze wszystkimi powiązanymi opłatami transakcyjnymi, bez żadnych potrąceń z tytułu kosztów operacyjnych puli. Stoi to w wyraźnym kontraście z tradycyjnymi pulami mining, które zazwyczaj pobierają opłaty w wysokości od 1-3% nagród mining. Model zerowych opłat sprawia, że Public Pool jest szczególnie atrakcyjny dla górników, którzy chcą zmaksymalizować swoje potencjalne zyski, zachowując pełną kontrolę nad swoimi operacjami mining.


Aby zrozumieć wyjątkową pozycję Public Pool, ważne jest, aby zrozumieć fundamentalną różnicę między solo mining a pooled mining. Prawdziwe solo mining oznacza, że wydobywasz niezależnie i otrzymujesz pełną nagrodę za blok (obecnie 3,125 BTC + opłaty), jeśli znajdziesz blok, ale prawdopodobieństwo jest proporcjonalne do twojego wskaźnika hashowania w stosunku do całej sieci - tworząc ekstremalną zmienność, która może trwać miesiące lub lata między nagrodami. Tradycyjne pule łączą moc hashowania, aby częściej znajdować bloki, proporcjonalnie rozdzielając nagrody i zapewniając stały, przewidywalny dochód. Dla górników ze znacznym kapitałem zainwestowanym w sprzęt i koszty operacyjne, czysty solo mining jest zazwyczaj niepraktyczny, niezależnie od jego filozoficznych zalet - wariancja sprawia, że pokrycie kosztów energii elektrycznej i odzyskanie inwestycji jest prawie niemożliwe. Ta rzeczywistość ekonomiczna oznacza, że większość górników wybierze pooled mining z praktycznych powodów finansowych. Public Pool działa jako samodzielna pula mining, co oznacza, że nadal masz do czynienia z wariancją samodzielnego mining (otrzymujesz wynagrodzenie tylko wtedy, gdy osobiście znajdziesz blok), ale korzystasz z infrastruktury puli i przejrzystej, zerowej opłaty.


### Przewaga Open Source i techniczna implementacja


Zaangażowanie Public Pool w rozwój oprogramowania open-source zapewnia górnikom bezprecedensową przejrzystość i kontrolę nad ich operacjami mining. Cała baza kodu jest dostępna na GitHub, dzięki czemu górnicy mogą dokładnie sprawdzić, jak działa oprogramowanie, zmodyfikować je zgodnie ze swoimi potrzebami, a nawet przyczynić się do jego rozwoju. Ta przejrzystość jest odpowiedzią na poważne obawy społeczności mining dotyczące nieznanych konfiguracji i praktyk tradycyjnych pul mining.


Architektura oprogramowania obejmuje zarówno podstawową funkcjonalność puli mining, jak i oddzielne repozytorium interfejsu użytkownika, z których oba są swobodnie dostępne do pobrania i modyfikacji. Górnicy mogą uruchamiać Public Pool w różnych konfiguracjach, w tym w kontenerach Docker, dzięki czemu można go dostosować do różnych konfiguracji sprzętowych i preferencji technicznych. Kompleksowa dokumentacja udostępniona w repozytoriach GitHub oferuje szczegółowe przewodniki instalacji, opcje konfiguracji i instrukcje modyfikacji, dzięki czemu jest dostępna dla górników o różnym poziomie wiedzy technicznej.


Łączenie się z Public Pool wymaga minimalnej konfiguracji w porównaniu do tradycyjnych konfiguracji mining. Górnicy muszą po prostu skonfigurować swoje urządzenia mining ze szczegółami połączenia Stratum i podać swój adres Bitcoin jako nazwę użytkownika. Opcjonalna nazwa pracownika może zostać dodana po separatorze kropkowym w celach organizacyjnych.


### Cechy społeczności i model zrównoważonego rozwoju


Public Pool zawiera kilka innowacyjnych funkcji, które wzmacniają społeczność Bitcoin mining przy jednoczesnym utrzymaniu zerowych opłat. Platforma wyświetla kompleksowe statystyki, w tym całkowitą szybkość hashowania podłączonych górników, która zwykle wahała się od 1 do 2 PetaHash na sekundę w 2024 r. i około 40 PH / s w listopadzie 2025 r., A także zapewnia szczegółowe informacje o podłączonych urządzeniach mining. Na szczególną uwagę zasługuje nacisk platformy na sprzęt mining o otwartym kodzie źródłowym, z urządzeniami oznaczonymi gwiazdkami wskazującymi w pełni otwarte projekty, wraz z linkami do odpowiednich repozytoriów GitHub.


Trwałość operacji Public Pool bez opłat opiera się na kreatywnym partnerstwie programu partnerskiego z dostawcami sprzętu mining. Gdy górnicy kupują sprzęt od firm partnerskich przy użyciu kodu rabatowego "SOLO", pięćdziesiąt procent zarobków partnerskich wspiera koszty operacyjne Public Pool, podczas gdy pozostałe pięćdziesiąt procent jest rozdzielane jako nagrody dla górników, którzy osiągają najwyższe udziały trudności w każdym miesiącu. Model ten tworzy symbiotyczną relację, w której górnicy otrzymują zniżki na zakup sprzętu, sprzedawcy zyskują klientów, a Public Pool utrzymuje swoją działalność bez pobierania bezpośrednich opłat.


### Filozofia decentralizacji i najlepsze praktyki


Podczas gdy Public Pool oferuje doskonałą alternatywę dla tradycyjnych pul mining, ważne jest, aby zrozumieć jego rolę w szerszym kontekście decentralizacji Bitcoin. Platforma służy jako odskocznia w kierunku ostatecznego celu, jakim jest prowadzenie przez indywidualnych górników własnych pul mining. Prowadzenie własnej puli mining reprezentuje najwyższy poziom decentralizacji, ponieważ eliminuje zależność od jakiejkolwiek infrastruktury lub oprogramowania strony trzeciej, niezależnie od tego, jak przejrzysta lub mająca dobre intencje może być ta strona trzecia.


Otwarty charakter Public Pool sprawia, że jest to idealna platforma edukacyjna dla górników, którzy chcą zrozumieć działanie puli przed wdrożeniem własnych rozwiązań. Dostępność przewodników instalacji dla wielu systemów operacyjnych i kompleksowa dokumentacja zapewniają górnikom wiedzę potrzebną do przejścia od korzystania z Public Pool do obsługi własnej infrastruktury mining. Ten aspekt edukacyjny jest zgodny z podstawowymi zasadami Bitcoin dotyczącymi suwerenności i decentralizacji, umożliwiając poszczególnym górnikom przejęcie pełnej kontroli nad ich operacjami mining, jednocześnie przyczyniając się do ogólnego bezpieczeństwa i decentralizacji sieci Bitcoin.


Interfejs użytkownika platformy zapewnia górnikom szczegółowe możliwości monitorowania, w tym status pracowników, statystyki hash rate i wskaźniki wydajności. Funkcje te pomagają górnikom zoptymalizować swoje operacje, jednocześnie ucząc się o zasadach zarządzania pulą, które mogą później zastosować do własnych wdrożeń puli mining.


## Jak zainstalować Public-Pool na Umbrel

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Prowadzenie własnego basenu Bitcoin mining w domu staje się coraz bardziej dostępne dzięki nowoczesnemu sprzętowi i uproszczonym rozwiązaniom programowym. W tym rozdziale omówiono praktyczną implementację domowego basenu publicznego przy użyciu niedrogiego sprzętu mini PC i usprawnionego oprogramowania do zarządzania węzłami. Pod koniec tego przewodnika zrozumiesz wymagania sprzętowe, proces konfiguracji oprogramowania i podstawową konfigurację potrzebną do stworzenia własnej infrastruktury puli mining.


### Wymagania sprzętowe i konfiguracja


Podstawą każdej domowej konfiguracji basenu mining jest wybór odpowiedniego sprzętu, który równoważy wydajność, koszty i efektywność energetyczną. Mini PC stanowi idealne rozwiązanie dla tego zastosowania, oferując wystarczającą moc obliczeniową przy zachowaniu kompaktowych rozmiarów i rozsądnego zużycia energii. Zalecana konfiguracja obejmuje procesor Intel N100, który zapewnia odpowiednie zasoby obliczeniowe dla operacji puli, w połączeniu z co najmniej jednym terabajtem pamięci masowej NVMe, aby pomieścić blockchain Bitcoin i powiązane dane.


Wymóg pamięci masowej jest szczególnie krytyczny, ponieważ uruchomienie puli mining wymaga utrzymania w pełni zsynchronizowanego węzła Bitcoin. Dysk NVMe o pojemności jednego terabajta zapewnia szybkie operacje odczytu/zapisu niezbędne do synchronizacji łańcucha bloków i bieżącego przetwarzania transakcji. Dodatkowo, wystarczająca alokacja pamięci RAM wspiera płynne działanie zarówno bazowego systemu operacyjnego Linux, jak i oprogramowania do zarządzania węzłami, które będzie koordynować działania puli.


### Architektura oprogramowania i zarządzanie węzłami


Stos oprogramowania dla domowej puli mining opiera się na systemie Linux, zapewniając stabilność i bezpieczeństwo niezbędne do działania Bitcoin. Na szczycie tego systemu bazowego wyspecjalizowane oprogramowanie do zarządzania węzłami, takie jak Umbrel, tworzy intuicyjny interfejs do zarządzania infrastrukturą Bitcoin. Takie podejście abstrahuje od złożoności tradycyjnie związanej z uruchamianiem węzłów Bitcoin, dzięki czemu obsługa puli jest dostępna dla użytkowników bez rozległego zaplecza technicznego.


Umbrel służy jako kompleksowa platforma zarządzania węzłami, która obsługuje instalację, synchronizację i bieżącą konserwację Bitcoin Core za pośrednictwem interfejsu internetowego. Model sklepu z aplikacjami platformy pozwala na łatwą instalację dodatkowych usług, w tym oprogramowania puli mining, poprzez proste operacje typu "wskaż i kliknij". Taka architektura zapewnia, że użytkownicy mogą skupić się na obsłudze puli, a nie na administrowaniu systemem, zachowując pełną kontrolę nad swoją infrastrukturą Bitcoin.


### Instalacja i konfiguracja basenu publicznego


Instalacja oprogramowania puli publicznej za pośrednictwem platformy Umbrel demonstruje usprawniony charakter nowoczesnego wdrażania infrastruktury Bitcoin. Proces rozpoczyna się od uzyskania dostępu do sklepu z aplikacjami Umbrel za pośrednictwem interfejsu internetowego, gdzie proste wyszukiwanie "public pool" ujawnia dostępne oprogramowanie mining. Instalacja wymaga tylko kilku kliknięć: wyboru aplikacji, potwierdzenia instalacji i oczekiwania na zakończenie automatycznego procesu konfiguracji.


Proces instalacji automatycznie konfiguruje niezbędne połączenia między oprogramowaniem puli publicznej a bazowym węzłem Bitcoin. Integracja ta zapewnia, że pula może weryfikować transakcje, konstruować szablony bloków i dystrybuować pracę do podłączonych górników bez konieczności ręcznej konfiguracji złożonych parametrów sieciowych. Po zakończeniu instalacji interfejs puli staje się natychmiast dostępny za pośrednictwem sieci lokalnej, zapewniając możliwości monitorowania i zarządzania w czasie rzeczywistym.


### Łączenie górników i kwestie związane z siecią


Podłączenie sprzętu mining do nowo utworzonej puli wymaga skonfigurowania ustawień puli górnika tak, aby wskazywały na lokalną infrastrukturę. Obejmuje to zastąpienie domyślnego adresu puli lokalnym adresem IP i odpowiednim numerem portu przypisanym podczas instalacji puli publicznej. Zmiana konfiguracji przekierowuje wysiłki obliczeniowe sprzętu mining z zewnętrznych pul do infrastruktury domowej, umożliwiając zachowanie pełnej kontroli nad operacjami mining i potencjalnymi nagrodami.


Konfiguracja sieci odgrywa kluczową rolę w dostępności i funkcjonalności puli. Konfiguracja sieci lokalnej zazwyczaj obejmuje standardowe adresowanie IP, ale użytkownicy mogą napotkać różnice w rozwiązywaniu DNS w zależności od konfiguracji routera. Niektóre routery zapewniają lokalne usługi DNS, które tworzą przyjazne nazwy dla usług lokalnych, podczas gdy inne wymagają bezpośredniego dostępu do adresu IP. Aby uzyskać szerszy dostęp poza siecią lokalną, konieczna może być konfiguracja przekierowania portów na routerze, choć wprowadza to dodatkowe kwestie bezpieczeństwa, które wymagają starannej oceny związanego z tym ryzyka i korzyści.


Pomyślne utworzenie domowej puli mining stanowi znaczący krok w kierunku zdecentralizowanej infrastruktury Bitcoin, zapewniając zarówno wartość edukacyjną, jak i praktyczne możliwości mining przy zachowaniu pełnej kontroli nad operacjami Bitcoin.


# Montaż sprzętu i rozwiązywanie problemów

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Jakich narzędzi używać?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

W świecie lutowania urządzeń do montażu powierzchniowego (SMD), szczególnie podczas pracy z projektami Bitaxe, posiadanie odpowiednich narzędzi stanowi różnicę między frustracją a sukcesem. Ten kompleksowy przewodnik obejmuje niezbędny sprzęt potrzebny do skutecznego radzenia sobie z projektami lutowania SMD, od podstawowych narzędzi ręcznych po specjalistyczny sprzęt, który zwiększy twoje możliwości lutownicze.


Jeśli chcesz zapoznać się z dokumentacją dotyczącą schematów, sprawdź to [repozytorium GitHub](https://github.com/skot/bitaxe-doc/tree/main).


### Podstawowe narzędzia ręczne i przyrządy precyzyjne


Podstawą każdego zestawu do lutowania SMD jest wysokiej jakości pęseta, która służy jako podstawowe narzędzie do umieszczania komponentów. Dwa rodzaje pęset okazują się najbardziej wartościowe w tej pracy: standardowe pęsety z prostą końcówką i te z lekko wygiętą końcówką. Odmiana z prostą końcówką radzi sobie z większością komponentów SMD znajdujących się w typowych zestawach Bitaxe, podczas gdy pęsety z wygiętą końcówką doskonale sprawdzają się podczas pracy z bardzo małymi komponentami, które wymagają precyzyjnego pozycjonowania. Narzędzia te są często dołączane do zestawów naprawczych, takich jak zestawy iFixit przeznaczone do naprawy telefonów, dzięki czemu są łatwo dostępne dla większości hobbystów.


Uzupełniając pęsetę, dobra para nożyczek staje się niezbędna do cięcia taśmy elektrycznej, która służy wielu celom w projektach elektronicznych. Taśma elektryczna zapewnia niezbędną izolację dla kabli i komponentów, a posiadanie łatwo dostępnej taśmy wysokiej jakości usprawnia proces lutowania. Te podstawowe materiały eksploatacyjne można nabyć w sklepach ze sprzętem lub u sprzedawców internetowych, bez konieczności korzystania z usług wyspecjalizowanych dostawców elektroniki.


### Aplikacja i zarządzanie pastą lutowniczą


Nakładanie pasty lutowniczej stanowi jeden z najbardziej krytycznych aspektów lutowania SMD, a odpowiednie narzędzia sprawiają, że proces ten jest zarówno dokładny, jak i przyjemny. Małe, nieostre strzykawki wypełnione pastą lutowniczą zapewniają wyjątkową kontrolę nad umieszczaniem pasty. Metoda ta pozwala na precyzyjne nakładanie dokładnej ilości pasty lutowniczej potrzebnej do każdego połączenia, a większość ludzi szybko rozwija właściwą technikę kontrolowania ciśnienia i natężenia przepływu poprzez praktyczną praktykę.


Wybór pasty lutowniczej ma znaczący wpływ na sukces lutowania. ChipQuik TS391SNL50 wyróżnia się jako wyjątkowa pasta lutownicza do projektów Bitaxe i ogólnych prac SMD. Pasta ta zachowuje odpowiednią konsystencję i charakterystykę topnienia, unikając problemów związanych z tańszymi alternatywami, które mają zbyt niskie temperatury topnienia. Pasty lutownicze niskiej jakości mogą powodować problemy, w których wcześniej lutowane połączenia stają się ponownie płynne podczas podgrzewania sąsiednich obszarów, co prowadzi do przemieszczania się komponentów i słabych połączeń. Podczas gdy wysokiej jakości pasta lutownicza stanowi wyższą inwestycję początkową, lepsze wyniki i mniejsza frustracja uzasadniają ten wydatek.


### Narzędzia do rozwiązywania problemów i czyszczenia


Nawet doświadczeni lutownicy napotykają na problemy, które wymagają korekty, co sprawia, że sprzęt do rozlutowywania jest niezbędny w każdym kompletnym zestawie narzędzi. Zestaw do rozlutowywania, czyli podgrzewane narzędzie próżniowe, usuwa nadmiar lutu i koryguje zmostkowane połączenia między pinami komponentów. Narzędzia te działają najskuteczniej w połączeniu z topnikiem, który poprawia przepływ lutu i pomaga w bardziej wydajnym procesie rozlutowywania.


Topnik występuje w różnych formach, w tym w postaci stałej i płynnej, i służy wielu celom poza pomocą w rozlutowywaniu. Gdy pasta lutownicza zaczyna tracić swoją skuteczność podczas długich sesji roboczych, zastosowanie dodatkowego topnika przywraca właściwą charakterystykę przepływu i zapewnia niezawodne połączenia. Małe narzędzie przypominające łyżkę, często spotykane w precyzyjnych zestawach naprawczych, ułatwia dokładne nakładanie topnika na określone obszary bez zanieczyszczania otaczających komponentów.


Czyszczenie deski jest ostatnim krokiem w profesjonalnej pracy, wymagającym alkoholu izopropanolowego i specjalnej szczotki do czyszczenia. Do tego celu doskonale nadaje się stara szczoteczka do zębów, a wyciskana butelka zawierająca izopropanol pozwala na kontrolowaną aplikację roztworu czyszczącego. Taka kombinacja usuwa pozostałości topnika i pasty, pozostawiając płytki o czystym, profesjonalnym wyglądzie, który ułatwia również kontrolę połączeń lutowniczych.


### Specjalistyczny sprzęt i zaawansowane narzędzia


W przypadku projektów obejmujących złożone układy scalone, zwłaszcza ASIC, szablony przekształcają proces lutowania z żmudnego ręcznego umieszczania w wydajne, dokładne nakładanie pasty. Te precyzyjnie wycięte szablony zapewniają stałą grubość i rozmieszczenie pasty, znacznie skracając czas wymagany dla złożonych komponentów przy jednoczesnej poprawie niezawodności. Inwestycja w wysokiej jakości szablony procentuje zarówno oszczędnością czasu, jak i lepszymi wynikami.


Zarządzanie ciepłem staje się kluczowe podczas pracy z komponentami zasilającymi, co sprawia, że pasta termiczna lub smar termiczny stają się niezbędnymi materiałami eksploatacyjnymi. Materiały te zapewniają prawidłowe przenoszenie ciepła między radiatorami i układami scalonymi, zapobiegając uszkodzeniom termicznym i zapewniając niezawodne działanie. Wysokiej jakości materiały termiczne stanowią niewielką inwestycję, która chroni znacznie droższe komponenty.


Sercem każdego zestawu do lutowania SMD jest stacja lutownicza na gorące powietrze, która zapewnia kontrolowane ciepło niezbędne do montażu powierzchniowego. Podczas gdy stacje budżetowe w przedziale 30-50 USD mogą działać odpowiednio, często brakuje im niezawodności i precyzji sprzętu wyższej klasy. Te podstawowe stacje zazwyczaj działają skutecznie w temperaturze 355°C i obejmują automatyczną redukcję temperatury po powrocie rękojeści do uchwytu. Jednak ich niezawodność może być niespójna, a niektóre jednostki ulegają przedwczesnej awarii. W przypadku poważnych prac, inwestycja w sprzęt wyższej jakości od wyspecjalizowanych dostawców elektroniki zapewnia lepszą długoterminową wartość dzięki zwiększonej niezawodności i bardziej precyzyjnej kontroli temperatury.


Połączenie tych narzędzi tworzy kompletne możliwości lutowania SMD, które wykraczają daleko poza projekty Bitaxe i obejmują ogólne prace elektroniczne. Zrozumienie roli każdego narzędzia i wybór wysokiej jakości sprzętu odpowiedniego do poziomu umiejętności i wymagań projektu zapewnia pomyślne wyniki i przyjemne doświadczenie lutowania.



## Napraw problemy z lutowaniem

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


Zestaw nadawczo-odbiorczy Bitaxe stawia wyjątkowe wyzwania podczas montażu, które wymagają zwrócenia szczególnej uwagi na orientację komponentów, zapobieganie mostkom lutowniczym i właściwe zarządzanie ciepłem. Zrozumienie tych powszechnych problemów i ich rozwiązań jest niezbędne do udanej konstrukcji zestawu i uniknięcia kosztownych uszkodzeń komponentów. Niniejszy rozdział analizuje najczęstsze problemy lutownicze napotykane podczas montażu Bitaxe i przedstawia praktyczne techniki ich identyfikacji i rozwiązywania.


### Orientacja i identyfikacja komponentów


Prawidłowa orientacja komponentów stanowi jeden z najważniejszych aspektów udanego montażu Bitaxe, szczególnie w przypadku tranzystorów MOSFET Q1 i Q2. Komponenty te posiadają charakterystyczne znaczniki orientacji, których należy dokładnie przestrzegać podczas instalacji. Każdy tranzystor MOSFET zawiera małe oznaczenie punktowe, które odpowiada określonym układom padów na płytce drukowanej. Kluczem do prawidłowej orientacji jest zrozumienie fizycznej struktury tych komponentów, które mają cztery piny ułożone z jednym dużym padem i trzema mniejszymi padami, które nie mają połączenia z dużym padem.


Podczas instalacji Q1 i Q2 należy dokładnie sprawdzić zarówno komponent, jak i płytkę drukowaną. Układ płytki wyraźnie pokazuje zamierzoną orientację poprzez konfigurację padów, z czterema pinami umieszczonymi tak, aby pasowały do struktury MOSFET. Przed przylutowaniem jakiegokolwiek dużego komponentu należy zawsze zweryfikować jego orientację, porównując fizyczne znaczniki komponentu z układem padów na płytce. Ten prosty krok weryfikacyjny zapobiega frustracji związanej z rozlutowywaniem i ponowną instalacją nieprawidłowo zorientowanych komponentów.


Konsekwencje nieprawidłowej orientacji wykraczają poza proste kwestie funkcjonalności. Nieprawidłowo zorientowane tranzystory MOSFET mogą powodować nieprawidłowe działanie obwodu, które jest trudne do zdiagnozowania i może wymagać całkowitej wymiany komponentów. Poświęcenie czasu na weryfikację orientacji przed zastosowaniem ciepła zapewnia prawidłowe działanie obwodu i zapobiega niepotrzebnemu rozwiązywaniu problemów na późniejszym etapie procesu montażu.


### Zarządzanie mostkami lutowniczymi i nadmiarem lutu


Mostki lutownicze stanowią kolejne powszechne wyzwanie w montażu Bitaxe, szczególnie wokół komponentów o drobnych odstępach, takich jak U10. Te niepożądane połączenia między sąsiednimi pinami mogą powodować nieprawidłowe działanie obwodu i wymagają starannych technik usuwania. Najskuteczniejszym podejściem jest użycie knota do rozlutowywania, miedzianego plecionego materiału, który pochłania nadmiar lutowia po podgrzaniu. Technika ta wymaga cierpliwości i odpowiedniego doboru narzędzi, aby uniknąć uszkodzenia delikatnych komponentów.


Podczas usuwania mostków lutowniczych na układach scalonych należy użyć uchwytu PCB lub zacisku przegubowego, aby bezpiecznie przytrzymać element podczas pracy. Zastosuj delikatne ciepło do dotkniętego obszaru i ostrożnie przeciągnij knot rozlutowujący przez zmostkowane połączenia. Miedziana plecionka w naturalny sposób wchłonie nadmiar lutowia, oddzielając niechciane połączenia. Proces ten może wymagać wielu prób, ale wytrwałość zapewnia czyste, prawidłowo oddzielone połączenia.


Zapobieganie pozostaje najlepszym podejściem do zarządzania mostkami lutowniczymi. Używanie odpowiednich ilości pasty lutowniczej i utrzymywanie stabilnej kontroli rąk podczas umieszczania komponentów znacznie ogranicza powstawanie mostków. Gdy mostki się pojawią, należy natychmiast się nimi zająć, zamiast mieć nadzieję, że nie wpłyną one na działanie obwodu. Nawet pozornie niewielkie mostki mogą powodować znaczące problemy z funkcjonalnością, które są trudne do zdiagnozowania po całkowitym zmontowaniu płytki.


### Krytyczne komponenty i kwestie specjalne


Konwerter buck U9 zasługuje na szczególną uwagę ze względu na jego krytyczną rolę w konwersji napięcia 5 V na 1,2 V dla układu ASIC. Ten komponent stanowi wyjątkowe wyzwanie ze względu na pięć małych połączeń i tendencję do awarii. Prawidłowa instalacja wymaga precyzyjnego nałożenia pasty lutowniczej i starannego zarządzania ciepłem. Niewystarczająca ilość pasty lutowniczej pod U9 może skutkować słabymi połączeniami, które uniemożliwiają prawidłową konwersję napięcia, podczas gdy nadmiar pasty może tworzyć mostki, które powodują nieprawidłowe działanie obwodu.


U9 wytwarza charakterystyczne sygnatury dźwiękowe, gdy występują problemy z mostkiem lutowniczym, generując szum o wysokiej częstotliwości, który różni się od normalnej pracy ASIC. Ta słuchowa technika diagnostyczna może pomóc w identyfikacji problemów, choć wymaga dobrego słuchu w zakresie wysokich częstotliwości. Gdy diagnostyka dźwiękowa nie jest możliwa, niezbędna staje się inspekcja wizualna. Należy dokładnie sprawdzić wszystkie połączenia, szukając mostków lub niewystarczającego pokrycia lutem.


Jeśli U9 nie generuje wymaganego napięcia 1,2 V, mimo że wydaje się prawidłowo przylutowany, prawdopodobną przyczyną jest niewystarczająca ilość pasty lutowniczej. Wyjmij komponent, nałóż niewielką ilość dodatkowej pasty lutowniczej i zainstaluj ponownie. W przypadkach, gdy poszczególne piny nie są odpowiednio pokryte lutowiem, ostrożnie nałóż niewielkie ilości pasty lutowniczej w określone miejsca za pomocą pęsety. Pasta lutownicza naturalnie przepłynie pod komponentem po podgrzaniu, tworząc odpowiednie połączenia poprzez działanie kapilarne.


### Zarządzanie ciepłem i ochrona podzespołów


Odpowiednie zarządzanie ciepłem chroni wrażliwe komponenty przed uszkodzeniami termicznymi, zapewniając jednocześnie niezawodne połączenia lutowane. Komponenty takie jak oscylator krystaliczny Y1 i U1 są szczególnie wrażliwe na długotrwałe działanie ciepła i wymagają starannej kontroli temperatury. Utrzymuj temperaturę lutownicy na poziomie 350 stopni Celsjusza, ale zminimalizuj czas aplikacji ciepła, aby zapobiec uszkodzeniu komponentów. Szybkie i wydajne techniki lutowania chronią te wrażliwe komponenty, zapewniając jednocześnie niezawodne połączenia.


Układ ASIC wymaga specjalnych technik obsługi ze względu na złożoną strukturę pinów i wrażliwość na naprężenia mechaniczne. Używając szablonów do nakładania pasty lutowniczej, należy zapewnić równomierne pokrycie wszystkich pinów, aby zapobiec nierównomiernemu osadzeniu komponentów. Jeśli nadmiar pasty lutowniczej powoduje nierównomierne osadzenie ASIC, przed wprowadzeniem poprawek należy odczekać, aż zespół całkowicie ostygnie. Aby uzyskać prawidłowe osadzenie, podczas ponownego podgrzewania należy delikatnie naciskać tylko na oznaczone krawędzie komponentu, nigdy na centralny obszar matrycy.


Komponent U8 stanowi wyjątkowe wyzwanie ze względu na liczne piny i możliwość wygięcia przewodów. Gdy piny ulegną wygięciu podczas przenoszenia, użyj uchwytu PCB lub zacisku przegubowego, aby zabezpieczyć komponent i ostrożnie wyprostuj uszkodzone piny. Pracuj powoli i cierpliwie, aby uniknąć złamania delikatnych przewodów. Zrozumienie, że niektóre grupy pinów na U8 są wewnętrznie połączone może uprościć rozwiązywanie problemów, ponieważ mostki między tymi konkretnymi pinami nie wpływają na działanie obwodu. Jednak mostki między innymi pinami wymagają ostrożnego usunięcia, aby zapewnić prawidłowe działanie.


## Jak debugować Bitaxe za pomocą AxeOS

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Podczas pracy z urządzeniami Bitaxe mining awarie sprzętu mogą objawiać się na różne sposoby, które mogą nie być od razu oczywiste. Zrozumienie, jak systematycznie diagnozować te problemy za pomocą systemu operacyjnego AxeOS, może zaoszczędzić znaczną ilość czasu i zapobiec niepotrzebnej wymianie komponentów. W tym rozdziale omówiono techniki diagnostyczne i metodologie rozwiązywania problemów, których doświadczeni technicy używają do identyfikowania określonych problemów sprzętowych poprzez analizę oprogramowania.


### Zrozumienie wskaźników zużycia energii


Pierwszym i najbardziej krytycznym wskaźnikiem diagnostycznym w AxeOS jest monitorowanie zużycia energii. Normalne urządzenia Bitaxe, w tym modele Bitaxe Ultra i Bitaxe Supra, zazwyczaj zużywają od 10 do 17 watów podczas standardowej pracy. Ten podstawowy pomiar służy jako główny wskaźnik kondycji całego systemu. Gdy pobór mocy spada znacznie poniżej tego zakresu, zwłaszcza poniżej 3 watów, sygnalizuje to podstawowy problem z chipem ASIC lub jego obwodem pomocniczym.


Scenariusze niskiego zużycia energii wymagają natychmiastowej uwagi, ponieważ wskazują, że układ mining jest albo całkowicie niefunkcjonalny, albo działa w stanie poważnej degradacji. Sam ten pomiar może pomóc w szybkim rozróżnieniu między problemami z wydajnością a całkowitymi awariami sprzętu. Odczyt mocy w AxeOS zapewnia informacje zwrotne w czasie rzeczywistym, które pozwalają monitorować skuteczność wszelkich prób naprawy urządzenia.


### Analiza pomiarów napięcia ASIC


Funkcja pomiaru napięcia ASIC w AxeOS dostarcza kluczowych informacji diagnostycznych, które pomagają dokładnie określić naturę problemów sprzętowych. Podczas sprawdzania odczytów napięcia należy zrozumieć związek między zmierzonym napięciem a żądanym napięciem, aby prawidłowo zdiagnozować problemy. System wyświetla zarówno napięcie dostarczane do układu ASIC, jak i napięcie, którego układ żąda od systemu zarządzania energią.


Jeśli zaobserwujesz pomiar napięcia ASIC wynoszący dokładnie 1,2 V w połączeniu z poborem mocy poniżej 3 W, ta konkretna kombinacja wskazuje albo na problem z lutowaniem chipa ASIC, albo na całkowicie uszkodzony ASIC. Ten odczyt napięcia sugeruje, że zasilanie dociera do lokalizacji chipa, ale sam chip nie działa prawidłowo. Fizyczna inspekcja matrycy ASIC może ujawnić pęknięcia lub inne widoczne uszkodzenia, które mogłyby wyjaśnić ten wzorzec zachowania.


Inny scenariusz diagnostyczny pojawia się w przypadku niskiego poboru mocy w połączeniu z bardzo niskimi odczytami żądanego napięcia, takimi jak 100 miliwoltów lub 0,5 wolta. Ten wzorzec wskazuje, że układ ASIC nie otrzymuje odpowiedniego napięcia zasilania, co zazwyczaj wskazuje na problemy z komponentem konwertera buck U9. Konwerter buck jest odpowiedzialny za zapewnienie precyzyjnej regulacji napięcia, której układy ASIC wymagają do prawidłowego działania.


### Interpretacja danych dziennika i komunikacja ASIC


System rejestrowania AxeOS zapewnia cenny wgląd w to, czy układ ASIC komunikuje się z systemem sterowania. Po uzyskaniu dostępu do dzienników za pomocą funkcji "show logs", obecność wpisów "ASIC results" potwierdza, że chip jest nie tylko zasilany, ale także aktywnie przetwarza pracę i zwraca wyniki. Ta komunikacja wskazuje, że ASIC jest prawidłowo przylutowany i utrzymuje połączenie z obwodem sterowania.


Brak wyników ASIC w logach, szczególnie w połączeniu z innymi objawami, pomaga zawęzić problem do konkretnych komponentów lub problemów z połączeniem. Takie podejście diagnostyczne pozwala odróżnić chipy, które całkowicie nie reagują, od tych, które mogą mieć przerywane problemy z połączeniem. Analiza dziennika staje się szczególnie cenna podczas rozwiązywania złożonych problemów, w których wiele objawów może sugerować różne przyczyny źródłowe.


### Systematyczne podejście do rozwiązywania problemów


Podczas diagnozowania problemów sprzętowych Bitaxe, stosowanie systematycznego podejścia zapobiega przeoczeniu krytycznych problemów i zapewnia wydajne procesy naprawcze. Rozpocznij od udokumentowania poboru mocy i odczytów napięcia, a następnie skoreluj te pomiary z danymi dziennika, aby uzyskać pełny obraz zachowania systemu. Takie metodyczne podejście pomaga zidentyfikować, czy problemy wynikają z samego układu ASIC, systemu zasilania, czy też ścieżek komunikacji między komponentami.


W przypadkach, w których problemem wydaje się być konwerter obniżający U9, konieczna może być fizyczna inspekcja i potencjalne ponowne lutowanie. Komponent U9 jest szczególnie podatny na problemy z lutowaniem, zwłaszcza przy pierwszym montażu. W przypadku podejrzenia problemów z regulacją napięcia, użycie multimetru w celu sprawdzenia, czy napięcie 1,2 V jest faktycznie obecne na stykach ASIC, zapewnia ostateczne potwierdzenie problemów z dostarczaniem zasilania. Jeśli napięcie jest obecne na stykach, ale ASIC nadal nie działa, a fizyczna inspekcja nie wykazuje żadnych uszkodzeń, wymiana układu ASIC staje się kolejnym logicznym krokiem. Jeśli problemy utrzymują się nawet po wymianie ASIC, komponent U2, który steruje układem ASIC, może wymagać uwagi jako ostatni element w sekwencji rozwiązywania problemów.


## Jak debugować za pomocą USB?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Podczas rozwiązywania problemów z urządzeniami Bitaxe mining, bezpośredni dostęp do wewnętrznego systemu rejestrowania urządzenia zapewnia nieoceniony wgląd, którego nie mogą zaoferować interfejsy internetowe. W tym rozdziale opisano, jak ustanowić bezpośrednie połączenie szeregowe USB z urządzeniem Bitaxe przy użyciu frameworka ESP-IDF, umożliwiając monitorowanie w czasie rzeczywistym dzienników systemowych, sekwencji rozruchowych i komunikatów o błędach. Takie podejście do debugowania jest szczególnie ważne w przypadku urządzeń, które często się restartują lub ulegają awariom sprzętowym, ponieważ przechwytuje wszystkie informacje diagnostyczne, które mogą zostać utracone podczas ponownego uruchomienia systemu.


Proces debugowania wymaga Visual Studio Code z rozszerzeniem ESP-IDF, choć można użyć dowolnego kompatybilnego IDE. Ta metoda działa ze wszystkimi wariantami Bitaxe, które zawierają port USB, w tym Bitaxe Ultra 204 i innymi modelami z tej serii. Bezpośrednie połączenie szeregowe omija potencjalne ograniczenia interfejsu internetowego i zapewnia niefiltrowany dostęp do wewnętrznych informacji o stanie urządzenia.


### Konfiguracja komunikacji szeregowej


Nawiązanie komunikacji z urządzeniem Bitaxe rozpoczyna się od podłączenia kabla USB i otwarcia terminala ESP-IDF w środowisku programistycznym. Polecenie `idf.py monitor` inicjuje proces połączenia, automatycznie skanując dostępne porty COM w celu nawiązania komunikacji UART z układem ESP32 w urządzeniu Bitaxe. System zazwyczaj przechodzi przez dostępne porty (COM3, COM4, COM16 itd.), aż znajdzie prawidłowe połączenie.


Po podłączeniu terminal wyświetla pełną sekwencję rozruchową i bieżące dzienniki operacyjne. Początkowy proces połączenia może potrwać kilka chwil, ponieważ system identyfikuje prawidłowy port komunikacyjny. Jeśli automatyczne wykrywanie portu nie powiedzie się, można ręcznie określić port COM za pomocą interfejsu wyboru portu IDE. Ten bezpośredni kanał komunikacyjny pozostaje aktywny przez cały czas działania urządzenia, zapewniając ciągły dostęp do diagnostyki systemu i wskaźników wydajności.


### Interpretacja sekwencji rozruchu i dzienników normalnego działania


Sekwencja rozruchowa dostarcza krytycznych informacji o konfiguracji sprzętowej i procesie inicjalizacji urządzenia Bitaxe. Normalne logi startowe rozpoczynają się od informacji o wersji ESP-IDF, po których następuje charakterystyczny komunikat "Welcome to the Bitaxe. Hack the planet", który potwierdza pomyślne załadowanie oprogramowania sprzętowego. Następnie system wyświetla konfigurację częstotliwości ASIC, identyfikację modelu urządzenia i szczegóły wersji płyty.


Prawidłowo działające urządzenie pokaże pomyślną inicjalizację I2C i regulację napięcia ASIC ustawioną na 1,2 V. Logi wyświetlają informacje o stanie GPIO i sekwencje inicjalizacji Wi-Fi, a następnie konfigurację serwera DHCP i przypisanie adresu IP. Jednym z najważniejszych wskaźników jest komunikat o wykryciu układu ASIC, który powinien informować o "wykryciu jednego układu ASIC" w przypadku urządzenia jednoukładowego. To potwierdzenie potwierdza, że sprzęt mining jest prawidłowo podłączony i komunikuje się z kontrolerem ESP32.


Dzienniki operacyjne ujawniają wiele jednoczesnych zadań uruchomionych na urządzeniu, w tym komunikację warstwy API, koordynację głównego zadania, zarządzanie zadaniami ASIC i przetwarzanie zadań warstwy. Te różne identyfikatory zadań pomagają wyizolować problemy z określonymi komponentami systemu. Normalne działanie obejmuje ustanowienie połączenia puli, komunikaty o dostosowaniu trudności, kolejkowanie i usuwanie zadań oraz raportowanie generowania nonce. Udane operacje mining wyświetlają wyniki ASIC z obliczeniami trudności, a mining przesyła potwierdzenia, gdy udziały osiągną wymagany próg.


### Identyfikacja awarii sprzętu i wzorców błędów


Awarie sprzętu objawiają się w dziennikach poprzez określone wzorce błędów, które wskazują, które komponenty działają nieprawidłowo. Najczęstszy tryb awarii obejmuje błędy komunikacji I2C z określonymi układami scalonymi na płycie Bitaxe. Na przykład, błędy komunikacji DS4432U pojawiają się jako komunikaty "ESP_ERROR_CHECK failed" ze wskaźnikami przekroczenia limitu czasu, wskazując na problemy z regulacją napięcia lub problemy lutownicze wpływające na komponent U10 odpowiedzialny za komunikację wyświetlacza.


Te komunikaty o błędach zawierają szczegółowe informacje debugowania, takie jak konkretny plik źródłowy (main_ds4432u.c), wywołanie funkcji, które nie powiodło się, oraz rdzeń procesora obsługujący zadanie. Informacje backtrace zapewniają dodatkowy kontekst dla zaawansowanego rozwiązywania problemów. Podobne wzorce błędów mogą wystąpić w przypadku układu sterowania temperaturą i wentylatorem EMC2101, z których każdy generuje charakterystyczne sygnatury dziennika, które pomagają zidentyfikować wadliwy komponent.


Fizyczne problemy sprzętowe często objawiają się powtarzającymi się cyklami błędów, po których następuje ponowne uruchomienie systemu. Jeśli urządzenie wytwarza słyszalny hałas podczas pracy, zazwyczaj wskazuje to na problemy z lutowaniem, takie jak mostki między pinami komponentów lub nieodpowiednie połączenia lutowane. Chociaż te problemy mechaniczne nie zawsze mogą powodować określone wpisy w dzienniku generate, tworzą one niestabilne warunki pracy, które objawiają się częstymi awariami i cyklami restartów w danych wyjściowych monitorowania.


### Zaawansowane strategie rozwiązywania problemów


Monitorowanie szeregowe zapewnia kilka korzyści w porównaniu z interfejsami debugowania opartymi na sieci Web, szczególnie w przypadku przerywanych awarii lub urządzeń doświadczających częstych restartów. Ciągłe przechwytywanie dziennika zapewnia, że żadne informacje diagnostyczne nie zostaną utracone podczas ponownego uruchamiania systemu, w przeciwieństwie do interfejsów internetowych, które mogą utracić dane podczas zdarzeń rozłączenia. Ta wszechstronna funkcja rejestrowania umożliwia identyfikację wzorców awarii i korelację określonych warunków błędu z czynnikami sprzętowymi lub środowiskowymi.


Analizując problematyczne urządzenia, należy skupić się na sekwencji zdarzeń prowadzących do awarii, a nie na pojedynczych komunikatach o błędach. Pomyślna komunikacja ASIC powinna wykazywać regularne przetwarzanie zadań, generowanie nonce i cykle przesyłania udziałów. Brak wyników ASIC w dziennikach wskazuje na awarie komunikacji między ESP32 a chipem mining, często spowodowane problemami z zasilaniem, uszkodzonymi śladami lub awariami komponentów.


W celu systematycznego rozwiązywania problemów należy udokumentować wzorce błędów i awarie poszczególnych komponentów przed zwróceniem się o pomoc do społeczności. Szczegółowe dzienniki błędów, w tym konkretne identyfikatory chipów i tryby awarii, umożliwiają doświadczonym użytkownikom zapewnienie ukierunkowanych wskazówek dotyczących naprawy, takich jak procedury wymiany komponentów lub poprawki lutownicze. Takie metodyczne podejście do debugowania sprzętu znacznie poprawia wskaźniki powodzenia napraw i skraca czas rozwiązywania złożonych problemów.


# Zaawansowane dostosowywanie

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Modyfikacja płytki drukowanej

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad to jedno z najpotężniejszych dostępnych narzędzi typu open-source do projektowania i trasowania obwodów drukowanych (PCB). To profesjonalne oprogramowanie umożliwia inżynierom i hobbystom tworzenie złożonych projektów elektronicznych poprzez umieszczanie komponentów na wirtualnych płytkach i trasowanie skomplikowanych ścieżek łączących te komponenty. To, co sprawia, że KiCad jest szczególnie cenny dla celów edukacyjnych i rozwojowych, to jego całkowicie otwarty charakter, umożliwiający użytkownikom modyfikowanie, dostosowywanie i uczenie się na podstawie istniejących projektów bez ograniczeń licencyjnych.


Projekt Bitaxe jest przykładem potęgi rozwoju sprzętu open-source, dostarczając kompletny projekt PCB, który użytkownicy mogą badać, modyfikować i dostosowywać do swoich konkretnych potrzeb. Ta dostępność tworzy doskonałe środowisko do nauki, w którym studenci i praktycy mogą badać rzeczywiste projekty PCB, jednocześnie rozwijając swoje zrozumienie systemów elektronicznych. Możliwość dostosowania elementów wizualnych, takich jak logo, zapewnia przystępny punkt wejścia dla użytkowników, którzy mogą być onieśmieleni techniczną złożonością projektowania elektronicznego.


### Konfiguracja środowiska KiCad


Przed rozpoczęciem jakichkolwiek prac dostosowawczych niezbędna jest odpowiednia konfiguracja środowiska programistycznego. Repozytorium Bitaxe musi zostać pobrane na komputer lokalny, zazwyczaj za pomocą funkcji pobierania ZIP w serwisie GitHub. Repozytorium to zawiera wszystkie niezbędne pliki projektu, w tym pliki projektu KiCad, biblioteki komponentów i dokumentację projektową wymaganą do pomyślnej modyfikacji.


Instalacja KiCad powinna zostać zakończona przy użyciu oficjalnej dystrybucji ze strony internetowej KiCad, zapewniając kompatybilność z plikami projektu i dostęp do najnowszych funkcji. Po prawidłowym zainstalowaniu zarówno repozytorium, jak i KiCad, otwarcie projektu wymaga przejścia do pliku projektu Bitaxe Ultra KiCad w pobranej strukturze repozytorium. Ten plik projektu służy jako centralne centrum, które łączy wszystkie powiązane pliki projektowe, biblioteki komponentów i ustawienia konfiguracyjne.


Początkowy widok złożonego projektu PCB może wydawać się przytłaczający, z licznymi komponentami, ścieżkami i warstwami tworzącymi gęsty wizualny krajobraz. Jednak funkcjonalność przeglądarki 3D KiCad zapewnia nieocenione narzędzie do zrozumienia fizycznego układu i relacji przestrzennych w projekcie. Ta trójwymiarowa perspektywa przekształca abstrakcyjny schemat w realistyczną wizualizację końcowego produktu, ułatwiając zrozumienie rozmieszczenia komponentów i ogólnej estetyki projektu.


### Proces dostosowywania logo


Dostosowywanie logo na projektach PCB jest jedną z najbardziej przystępnych modyfikacji dla nowych użytkowników KiCad, wymagającą minimalnej wiedzy technicznej i zapewniającą natychmiastowe efekty wizualne. Proces rozpoczyna się od narzędzia konwertera obrazów, które przekształca standardowe pliki obrazów w formaty footprintów kompatybilne z oprogramowaniem do projektowania PCB. Ten proces konwersji wymaga zwrócenia szczególnej uwagi na parametry rozmiaru, zwykle mierzone w milimetrach, aby zapewnić prawidłowe skalowanie na końcowej wyprodukowanej płytce.


Przepływ pracy konwertera obrazu obejmuje kilka krytycznych kroków, które określają ostateczny wygląd i rozmieszczenie niestandardowych logo. Wybór obrazu źródłowego powinien priorytetowo traktować projekty o wysokim kontraście, które będą dobrze przekładać się na proces sitodruku stosowany w produkcji PCB. Specyfikacja rozmiaru staje się kluczowa, ponieważ logo musi być wystarczająco duże, aby pozostało czytelne po wyprodukowaniu, a jednocześnie nie kolidowało z rozmieszczeniem komponentów lub funkcjonalnością. Wybór między przednią i tylną warstwą sitodruku wpływa zarówno na widoczność, jak i na kwestie produkcyjne.


Zarządzanie bibliotekami footprintów stanowi fundamentalny aspekt dostosowywania KiCad, wymagając od użytkowników zrozumienia, w jaki sposób oprogramowanie organizuje i uzyskuje dostęp do elementów projektu. Dodawanie niestandardowych logo obejmuje tworzenie nowych bibliotek footprintów lub modyfikowanie istniejących, a następnie prawidłowe łączenie tych bibliotek w strukturze projektu. Proces ten zapewnia, że niestandardowe elementy pozostają dostępne w różnych sesjach projektowych i mogą być łatwo udostępniane innym członkom zespołu lub współpracownikom.


### Zaawansowana eksploracja i zrozumienie projektu


Poza prostym dostosowywaniem logo, KiCad zapewnia potężne narzędzia do eksploracji i zrozumienia złożonych projektów PCB. System zarządzania warstwami pozwala użytkownikom na selektywne przeglądanie różnych aspektów projektu, od rozmieszczenia komponentów i trasowania po specyfikacje produkcyjne i informacje o montażu. To warstwowe podejście umożliwia szczegółową analizę konkretnych elementów projektu bez wizualnego bałaganu związanego z niepowiązanymi komponentami.


Analiza routingu ścieżek stanowi jeden z najbardziej edukacyjnych aspektów eksploracji PCB, ujawniając, w jaki sposób połączenia elektryczne przepływają między komponentami i podsystemami. Śledząc poszczególne ślady lub grupy powiązanych sygnałów, użytkownicy mogą zrozumieć funkcjonalność obwodu i decyzje projektowe. Na przykład, badanie sieci dystrybucji zasilania ujawnia, w jaki sposób komponenty regulacji napięcia i filtrowania współpracują ze sobą, aby zapewnić czystą, stabilną moc wrażliwym komponentom elektronicznym.


Zależność między projektem schematu a fizycznym układem staje się widoczna dzięki dokładnemu zbadaniu rozmieszczenia komponentów i decyzji dotyczących routingu. Zrozumienie, dlaczego określone komponenty są umieszczane w określonych lokalizacjach, w jaki sposób względy termiczne wpływają na decyzje dotyczące układu i w jaki sposób wymagania dotyczące integralności sygnału wpływają na wybór routingu, zapewnia cenny wgląd w profesjonalne praktyki projektowania PCB. Wiedza ta okazuje się nieoceniona dla użytkowników opracowujących własne projekty lub modyfikujących istniejące dla konkretnych zastosowań.


Kompleksowe narzędzia KiCad do sprawdzania i weryfikacji reguł projektowych zapewniają, że modyfikacje zachowują kompatybilność elektryczną i produkcyjną. Te zautomatyzowane systemy pomagają zapobiegać typowym błędom projektowym, jednocześnie edukując użytkowników w zakresie standardów branżowych i najlepszych praktyk. Integracja wizualizacji 3D z danymi projektu elektrycznego tworzy potężne środowisko do nauki, w którym koncepcje teoretyczne stają się namacalne dzięki wizualnej reprezentacji i interaktywnej eksploracji.


## Jak utworzyć plik fabryczny?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

Tworzenie niestandardowego oprogramowania układowego dla urządzeń mining opartych na ESP wymaga zwrócenia szczególnej uwagi na konfigurację, zależności i właściwy proces kompilacji. Ten kompleksowy przewodnik przeprowadza przez cały proces tworzenia zarówno standardowych plików binarnych oprogramowania układowego, jak i plików fabrycznych, które zawierają wstępnie skonfigurowane ustawienia, dzięki czemu wdrażanie jest bardziej wydajne i skraca czas konfiguracji dla użytkowników końcowych.


Należy pamiętać, że ten rozdział jest dość techniczny i można go po prostu przejrzeć, jeśli jesteś ciekawy.


### Konfiguracja środowiska programistycznego


Aby rozpocząć tworzenie oprogramowania układowego ESP-Miner, należy skonfigurować odpowiednie środowisko programistyczne w Visual Studio Code, najlepiej w dystrybucji Linuksa. Rozszerzenie ESP-IDF służy jako kamień węgielny tej konfiguracji, zapewniając niezbędne narzędzia i integrację frameworka do rozwoju ESP32. Podczas pierwszej instalacji rozszerzenia ESP-IDF użytkownicy napotykają przewodnik konfiguracji, który ułatwia proces konfiguracji.


Kluczową kwestią w procesie konfiguracji jest wybór odpowiedniej wersji ESP-IDF. Podczas gdy wersja 5.1.3 była wcześniej zalecana, praktyczne doświadczenie ujawniło, że ta wersja może powodować problemy z kompilacją, które komplikują proces rozwoju. Zalecane podejście obejmuje obecnie korzystanie z ESP-IDF w wersji 5.3 Beta 1, która okazała się rozwiązywać te komplikacje związane z budową i zapewnia prawidłowe działanie urządzeń Bitaxe. Proces instalacji wymaga wybrania opcji instalacji ekspresowej i wybrania wersji 5.3 Beta 1 z dostępnych opcji.


Konfiguracja środowiska programistycznego wykracza poza instalację ESP-IDF i obejmuje właściwą konfigurację terminala. Visual Studio Code zapewnia wiele metod dostępu do funkcjonalności ESP-IDF, w tym opcję palety poleceń, aby otworzyć terminal ESP-IDF lub za pomocą dedykowanej ikony terminala znajdującej się w interfejsie. To wyspecjalizowane środowisko terminalowe zapewnia, że wszystkie polecenia ESP-IDF działają poprawnie i zapewnia dostęp do pełnego zestawu narzędzi.


### Konfigurowanie ustawień ESP-Miner


Plik konfiguracyjny stanowi serce procesu dostosowywania ESP-Miner, zawierając wszystkie istotne parametry, które definiują sposób działania urządzenia w środowisku docelowym. Konfiguracja ta obejmuje ustawienia sieciowe, połączenia puli mining i parametry specyficzne dla sprzętu, które muszą być dostosowane do konkretnego scenariusza wdrożenia.


Konfiguracja sieci stanowi podstawowy element procesu konfiguracji, wymagający określenia poświadczeń Wi-Fi, w tym identyfikatora SSID i hasła. Zamiast używać wartości zastępczych, takich jak "test", konfiguracje produkcyjne powinny zawierać rzeczywiste poświadczenia sieciowe, których urządzenie będzie używać w swoim środowisku operacyjnym. Konfiguracja uwzględnia również różne konfiguracje puli mining, obsługując zarówno konfiguracje puli prywatnych z określonymi adresami IP, jak i pule publiczne, takie jak public-pool.io z odpowiednimi ustawieniami portów.


Parametry konfiguracyjne specyficzne dla Mining obejmują ustawienie użytkownika warstwy, które zazwyczaj odpowiada adresowi Bitcoin, na który powinny być kierowane nagrody mining. Dodatkowe parametry sprzętowe, takie jak ustawienia częstotliwości, konfiguracje napięcia i specyfikacje typu ASIC muszą być zgodne z docelową platformą sprzętową. Repozytorium GitHub zawiera wstępnie skonfigurowane przykłady dla różnych wariantów sprzętu, takie jak konfiguracja BM1368 przeznaczona dla urządzeń Super i ustawienia BM1366 dla wariantów Ultra. Specyfikacje wersji płyty, takie jak ustawienie wersji portu na 401 dla nowszych wersji sprzętu, zapewniają zgodność ze specyfiką urządzenia docelowego.


### Tworzenie sieciowego Interface i podstawowego oprogramowania układowego


Projekt ESP-Miner zawiera zaawansowany interfejs sieciowy, który wymaga oddzielnej kompilacji przed rozpoczęciem głównego procesu kompilacji oprogramowania układowego. Ten interfejs sieciowy, określany jako oprogramowanie układowe AxeOS, zapewnia użytkownikom kompleksowy interfejs zarządzania do monitorowania i sterowania urządzeniami mining.


Proces tworzenia interfejsu sieciowego rozpoczyna się od przejścia do katalogu serwera HTTP w głównej strukturze repozytorium, a konkretnie do podkatalogu AxeOS. Ta lokalizacja zawiera aplikację internetową opartą na Node.js, która wymaga instalacji zależności za pomocą polecenia npm install. System kompilacji zakłada, że Node.js jest poprawnie zainstalowany w systemie deweloperskim, ponieważ stanowi to podstawowy wymóg dla procesu kompilacji interfejsu internetowego.


Po instalacji zależności, polecenie npm run build kompiluje komponenty interfejsu sieciowego, tworząc niezbędne pliki, które zostaną osadzone w oprogramowaniu układowym ESP32. Ten proces kompilacji generuje zoptymalizowane zasoby sieciowe, które zapewniają funkcjonalność interfejsu użytkownika przy jednoczesnym zachowaniu efektywnego wykorzystania pamięci na ograniczonej platformie ESP32. Pomyślne ukończenie tego etapu kompilacji jest niezbędne przed przejściem do głównej kompilacji oprogramowania układowego, ponieważ oprogramowanie układowe ESP-Miner zawiera te komponenty interfejsu internetowego jako integralną funkcjonalność.


### Tworzenie plików fabrycznych z wbudowaną konfiguracją


Tworzenie plików fabrycznych stanowi zaawansowaną strategię wdrażania, która osadza ustawienia konfiguracyjne bezpośrednio w pliku binarnym oprogramowania układowego, eliminując potrzebę ręcznej konfiguracji podczas konfiguracji urządzenia. Takie podejście okazuje się szczególnie cenne w przypadku wdrożeń na dużą skalę lub sytuacji, w których niezbędna jest spójna konfiguracja na wielu urządzeniach.


Proces tworzenia pliku fabrycznego rozpoczyna się od wygenerowania konfiguracji binarnej z pliku konfiguracyjnego CSV przy użyciu narzędzia generatora partycji NVS ESP-IDF. Narzędzie to, znajdujące się w katalogu komponentów ESP-IDF pod nvs-flash/nvs-partition-generator, konwertuje konfigurację czytelną dla człowieka na format binarny odpowiedni do bezpośredniego przechowywania w pamięci flash. Skrypt nvs-partition-gen.py przetwarza plik config.csv i generuje plik config.binary, który jest przeznaczony dla przestrzeni adresowej pamięci 0x6000.


Ostateczny montaż plików fabrycznych wykorzystuje wyspecjalizowane skrypty scalające, które łączą podstawowe pliki binarne oprogramowania układowego z danymi konfiguracyjnymi. Repozytorium zapewnia wiele opcji scalania, w tym standardowy skrypt scalający dla podstawowych plików fabrycznych i skrypt scalający zawierający konfigurację dla kompleksowych plików fabrycznych. Skrypt merge-bin-with-config.sh tworzy pliki fabryczne, które zawierają zarówno funkcjonalność oprogramowania układowego, jak i wstępnie skonfigurowane ustawienia, co skutkuje kompletnym pakietem wdrożeniowym. Takie podejście umożliwia tworzenie plików fabrycznych specyficznych dla urządzenia, takich jak wersje dostosowane do urządzeń Bitaxe Ultra z określonymi wersjami płyt, przy jednoczesnym zachowaniu elastyczności ogólnych plików fabrycznych generate bez wbudowanych konfiguracji dla scenariuszy wymagających elastyczności ręcznej konfiguracji.


Ukończone pliki fabryczne zapewniają zespołom wdrożeniowym gotowe do flashowania pliki binarne, które zawierają wszystkie niezbędne komponenty oprogramowania układowego i ustawienia konfiguracyjne, usprawniając proces dostarczania urządzeń i zapewniając spójne parametry operacyjne we wdrożonych urządzeniach mining.


## Jak korzystać z Bitaxe Web Flasher?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

Bitaxe Web Installer reprezentuje usprawnione podejście do zarządzania oprogramowaniem sprzętowym dla urządzeń Bitaxe, zapewniając użytkownikom wiele opcji instalacji za pośrednictwem interfejsu internetowego. To kompleksowe narzędzie eliminuje złożoność tradycyjnie związaną z aktualizacjami oprogramowania układowego i nowymi instalacjami, dzięki czemu zarządzanie urządzeniami jest dostępne dla użytkowników niezależnie od ich wiedzy technicznej. Zrozumienie prawidłowego korzystania z tego instalatora ma kluczowe znaczenie dla utrzymania optymalnej wydajności urządzenia i uniknięcia typowych pułapek, które mogą tymczasowo uniemożliwić działanie urządzeń.


### Wymagania dotyczące dostępu i zgodności przeglądarki


Bitaxe Web Installer jest dostępny za pośrednictwem dedykowanego adresu URL [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) (ten przedstawiony w filmie jest obecnie przestarzały), służąc jako centralne centrum wszystkich działań związanych z instalacją oprogramowania układowego. Jednak pomyślne działanie tego narzędzia internetowego wymaga kompatybilności z przeglądarką, ponieważ instalator opiera się na określonych technologiach internetowych, które nie są powszechnie obsługiwane we wszystkich przeglądarkach. Chrome jest główną zalecaną przeglądarką dla instalatora, zapewniając pełną kompatybilność ze wszystkimi funkcjami. Podczas gdy inne przeglądarki oparte na Chromium mogą oferować podobną funkcjonalność, popularne alternatywy, takie jak Brave i Firefox, nie mają niezbędnej obsługi seriali internetowych API, co czyni je niekompatybilnymi z podstawowymi operacjami instalatora.


To ograniczenie przeglądarki wynika z zależności instalatora od bezpośredniej komunikacji szeregowej z urządzeniami Bitaxe za pośrednictwem interfejsu internetowego. Serial internetowy API, który umożliwia taką komunikację, pozostaje stosunkowo nowym standardem sieciowym, który nie został jeszcze powszechnie przyjęty w przeglądarkach. Użytkownicy próbujący uzyskać dostęp do instalatora za pośrednictwem nieobsługiwanych przeglądarek napotkają błędy połączenia i niemożność komunikacji ze swoimi urządzeniami, co wymaga przełączenia się na kompatybilną przeglądarkę przed przystąpieniem do jakichkolwiek czynności instalacyjnych.


### Wymagania dotyczące zasilania i przygotowanie urządzenia


Urządzenia Bitaxe wykazują różne wymagania dotyczące zasilania w zależności od konkretnego modelu i wersji, co sprawia, że właściwe zarządzanie energią jest niezbędne do pomyślnej instalacji oprogramowania układowego. Urządzenia działające w wersji 204 lub niższej mogą działać wyłącznie poprzez zasilanie USB, pobierając wystarczającą ilość prądu z podłączonego komputera, aby utrzymać działanie podczas procesu flashowania. Ten uproszczony układ zasilania sprawia, że te wcześniejsze wersje są szczególnie wygodne do aktualizacji oprogramowania układowego, ponieważ użytkownicy muszą podłączyć tylko jeden kabel USB, aby rozpocząć proces instalacji.


Jednak urządzenia z wersją 205 i nowszymi wymagają zewnętrznych źródeł zasilania oprócz połączenia USB, co odzwierciedla zmiany w zużyciu energii i konstrukcji obwodów w nowszych wersjach sprzętu. Urządzenia te nie mogą pobierać odpowiedniej mocy przez samo USB, co wymaga podłączenia do ich standardowych zasilaczy podczas instalacji oprogramowania układowego. Niezapewnienie odpowiedniego zasilania tym nowszym urządzeniom spowoduje niepowodzenie instalacji i potencjalne uszkodzenie procesu aktualizacji oprogramowania układowego.


Proces fizycznego połączenia wymaga określonego czasu i manipulacji przyciskami, aby zapewnić prawidłową komunikację między instalatorem a urządzeniem. Użytkownicy muszą nacisnąć i przytrzymać przycisk rozruchu na swoim urządzeniu Bitaxe przed podłączeniem kabla USB-C do komputera. Sekwencja ta przełącza urządzenie w tryb bootloadera, umożliwiając instalatorowi bezpośrednią komunikację z pamięcią firmware urządzenia. Podłączenie kabla USB przed naciśnięciem przycisku bootowania spowoduje normalne działanie urządzenia, a nie tryb bootloadera wymagany do instalacji oprogramowania układowego, uniemożliwiając instalatorowi ustanowienie niezbędnego kanału komunikacji.


### Opcje instalacji i ich zastosowania


Instalator Bitaxe Web Installer zapewnia cztery różne opcje instalacji, z których każda została zaprojektowana dla określonych przypadków użycia i konfiguracji urządzeń. Bitaxe Superboard w wersji 4.0.1 reprezentuje najbardziej aktualne oprogramowanie sprzętowe dla urządzeń Super model, z wersją 4.0.2 zaplanowaną do wydania w przyszłości. Opcja ta obejmuje zarówno warianty fabryczne, jak i aktualizacyjne, zapewniając elastyczność w podejściu do instalacji w oparciu o potrzeby użytkownika i stan urządzenia.


Instalacje fabryczne stanowią kompletną wymianę oprogramowania sprzętowego, która odzwierciedla oryginalny proces produkcyjny, w tym kompleksowe procedury autotestu, które weryfikują funkcjonalność urządzenia we wszystkich systemach. Gdy użytkownicy wybierają instalację fabryczną, instalator wykonuje całkowite usunięcie istniejącego oprogramowania układowego i danych konfiguracyjnych, zastępując je świeżą, czystą instalacją identyczną z tą, która zostałaby zastosowana podczas produkcji. Proces ten obejmuje zautomatyzowane autotesty, które weryfikują prawidłowe działanie sprzętu, wymagając od użytkowników ponownego uruchomienia urządzeń po zakończeniu przed wznowieniem normalnej pracy. Instalacje fabryczne okazują się szczególnie cenne, gdy urządzenia doświadczają trwałych problemów lub gdy użytkownicy chcą przywrócić swoje urządzenia do oryginalnych specyfikacji fabrycznych.


Instalacje aktualizacji zapewniają bardziej konserwatywne podejście, zachowując istniejące dane konfiguracyjne i aktualizując tylko podstawowe składniki oprogramowania układowego. Ta opcja jest idealna dla użytkowników, którzy dostosowali ustawienia urządzenia i chcą zachować swoje osobiste konfiguracje, jednocześnie korzystając z ulepszeń oprogramowania układowego i poprawek błędów. Proces aktualizacji dotyczy tylko tych komponentów oprogramowania układowego, które wymagają modyfikacji, pozostawiając ustawienia specyficzne dla użytkownika, dane uwierzytelniające WiFi i adresy Bitcoin nienaruszone podczas całego procesu instalacji.


### Krytyczne kwestie związane z instalacją i ochroną danych


Rozróżnienie między instalacją fabryczną a aktualizacją ma znaczący wpływ na konfigurację urządzenia i zachowanie danych użytkownika. Instalacje fabryczne wykonują całkowite wymazanie urządzenia, usuwając wszystkie ustawienia skonfigurowane przez użytkownika, w tym poświadczenia WiFi, adresy Bitcoin i wszelkie spersonalizowane parametry urządzenia. Po instalacji fabrycznej użytkownicy muszą ponownie połączyć się z domyślną siecią Wi-Fi urządzenia i ponownie skonfigurować wszystkie ustawienia osobiste od zera, zasadniczo traktując urządzenie tak, jakby było zupełnie nowe od producenta.


Instalacje aktualizacji wymagają zwrócenia szczególnej uwagi na opcję wymazywania urządzenia prezentowaną podczas procesu instalacji. Instalator wyświetli pytanie "Czy chcesz wymazać urządzenie przed zainstalowaniem Bitaxe Flasher?" wraz z ostrzeżeniem, że wszystkie dane na urządzeniu zostaną utracone. Użytkownicy wykonujący instalacje aktualizacji muszą odrzucić tę opcję, klikając "Dalej", zamiast potwierdzać operację wymazywania. Zaakceptowanie opcji wymazywania podczas instalacji aktualizacji spowoduje usunięcie pliku konfiguracyjnego urządzenia, potencjalnie czyniąc urządzenie niefunkcjonalnym do czasu przywrócenia prawidłowej konfiguracji. Chociaż sytuacja ta nie powoduje trwałego uszkodzenia urządzenia, powoduje niepotrzebne komplikacje i wymaga dodatkowych kroków konfiguracyjnych w celu przywrócenia normalnego działania.


Sam proces instalacji przebiega automatycznie, gdy użytkownicy dokonają wyboru i potwierdzą swoje wybory. Instalator obsługuje wszystkie techniczne aspekty transferu i weryfikacji oprogramowania sprzętowego, zapewniając wskaźniki postępu i aktualizacje stanu podczas całego procesu. To zautomatyzowane podejście eliminuje potrzebę zrozumienia przez użytkowników złożonych procedur instalacji oprogramowania układowego, zapewniając jednocześnie niezawodne i spójne wyniki dla różnych modeli urządzeń i wersji oprogramowania układowego.


## Jak stworzyć i zamówić PCB?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Ten rozdział skupia się na praktycznym procesie generowania plików produkcyjnych z projektów KiCad i zamawiania profesjonalnych PCB od producentów online. Używając projektu Bitaxe jako naszego przykładu, przejdziemy przez kompletny przepływ pracy od generowania pliku do złożenia zamówienia u producenta PCB.


### Zrozumienie procesu produkcji PCB


Podróż od ukończonego projektu KiCad do fizycznej płytki PCB obejmuje kilka krytycznych kroków, które wypełniają lukę między cyfrowym projektem a fizyczną produkcją. Podczas pracy ze złożonymi projektami, takimi jak Bitaxe, edytor PCB w KiCad zapewnia kompleksowy widok projektu, wyświetlając wszystkie komponenty i ich wzajemne połączenia za pomocą kolorowych ścieżek. Czerwone i niebieskie linie reprezentują połączenia elektryczne między różnymi układami scalonymi i komponentami na płytce. Funkcja podglądu 3D w KiCad pozwala na wizualizację ostatecznego wyglądu zmontowanej płytki, zapewniając cenny wgląd w rozmieszczenie komponentów i potencjalne konflikty mechaniczne.


Proces produkcyjny wymaga określonych formatów plików, które producenci PCB mogą interpretować i wykorzystywać do produkcji płytek. Pliki te zawierają dokładne informacje o warstwach miedzi, otworach, rozmieszczeniu komponentów i innych specyfikacjach produkcyjnych. Zrozumienie tego przepływu pracy jest niezbędne, niezależnie od tego, czy pracujesz ze standardowym projektem Bitaxe, czy też tworzysz modyfikacje, takie jak dodawanie niestandardowych logo, zmiana wartości komponentów lub dostosowywanie układu płytki, aby spełnić określone wymagania.


### Generowanie plików Gerber na potrzeby produkcji


Pliki Gerber służą jako standard branżowy do przekazywania producentom informacji o projekcie PCB. Pliki te zawierają wszystkie niezbędne dane do produkcji PCB, w tym wzory warstw miedzi, definicje masek lutowniczych i lokalizacje otworów. Aby generate te pliki w KiCad, przejdź do edytora PCB i uzyskaj dostęp do danych wyjściowych produkcji poprzez menu Pliki. Oprogramowanie automatycznie konfiguruje odpowiednie ustawienia dla standardowych procesów produkcyjnych, w tym właściwą strukturę katalogów wyjściowych, zwykle zorganizowaną jako "pliki produkcyjne/gerbers"


Proces generowania tworzy wiele plików Gerber, z których każdy reprezentuje różne aspekty projektu PCB. Pliki te współpracują ze sobą, aby zapewnić producentom kompletne instrukcje produkcji. Po wygenerowaniu pliki te muszą zostać skompresowane do archiwum ZIP, ponieważ jest to standardowy format oczekiwany przez większość producentów PCB. Plik ZIP zawiera wszystkie niezbędne dane produkcyjne i zapewnia, że żadne pliki nie zostaną utracone lub uszkodzone podczas procesu przesyłania na stronę internetową producenta.


Warto zauważyć, że wiele projektów open-source, w tym Bitaxe, często zawiera wstępnie wygenerowane pliki produkcyjne w swoich repozytoriach. Jednak zrozumienie, jak samodzielnie generate te pliki jest kluczowe podczas wprowadzania modyfikacji projektu lub pracy z różnymi wersjami płytek. Wiedza ta staje się szczególnie cenna podczas dostosowywania projektów lub rozwiązywania problemów produkcyjnych.


### Wybór producentów PCB i zrozumienie dostępnych opcji


Rynek produkcji obwodów drukowanych oferuje kilka renomowanych opcji, przy czym JLCPCB i PCBWay są jednymi z najpopularniejszych wyborów zarówno dla hobbystów, jak i profesjonalistów. Obaj producenci zapewniają podobne usługi w konkurencyjnych cenach i niezawodnej jakości, choć każdy z nich ma określone zalety w zależności od wymagań projektu. JLCPCB często przyciąga początkujących użytkowników promocyjnymi cenami i przyjaznymi dla użytkownika interfejsami, podczas gdy PCBWay może oferować różne opcje materiałowe lub specjalistyczne usługi.


Podczas przesyłania plików Gerber na stronę producenta, system automatycznie analizuje projekt i przedstawia różne opcje produkcji. Domyślne ustawienia zapewniane przez te platformy są zazwyczaj odpowiednie dla większości standardowych projektów i ogólnie zaleca się zachowanie tych ustawień, chyba że masz określone wymagania. Kluczowe parametry obejmują grubość PCB, masę miedzi, wykończenie powierzchni i minimalne ilości. Większość producentów wymaga minimalnych zamówień na poziomie pięciu płytek, co w rzeczywistości sprawdza się w przypadku projektów hobbystycznych, w których korzystne jest posiadanie zapasowych płytek lub dzielenie się nimi z przyjaciółmi.


Opcje kolorystyczne stanowią jeden z niewielu estetycznych wyborów dostępnych podczas procesu produkcyjnego. Podczas gdy zielony pozostaje tradycyjną i najbardziej opłacalną opcją, producenci zazwyczaj oferują alternatywy, w tym niebieski, czerwony, żółty, fioletowy i czarny. Wybór koloru jest czysto estetyczny i nie wpływa na wydajność elektryczną płytki PCB, chociaż niektóre kolory mogą mieć niewielki wpływ na koszty lub dłuższy czas produkcji.


### Zaawansowane aspekty produkcji i opcje montażu


Poza podstawową produkcją PCB, współcześni producenci oferują dodatkowe usługi, które mogą znacznie usprawnić realizację projektu. Szablony stanowią jedną z najcenniejszych usług dodatkowych, szczególnie w przypadku projektów z komponentami o drobnej podziałce, takimi jak chipy ASIC znalezione w projektach Bitcoin mining. Szablon jest zasadniczo precyzyjnie wyciętym aluminiowym szablonem z otworami, które dokładnie odpowiadają lokalizacjom pól lutowniczych na płytce drukowanej. Narzędzie to umożliwia spójne i dokładne nakładanie pasty lutowniczej, znacznie poprawiając jakość montażu i zmniejszając prawdopodobieństwo wystąpienia błędów lutowania.


Opcje szablonów zazwyczaj obejmują pojedyncze szablony z górnym i dolnym wzorem lub oddzielne szablony dla każdej strony płyty. W przypadku większości projektów, połączony szablon okazuje się wygodniejszy i bardziej opłacalny. Grubość szablonu jest dokładnie obliczana, aby nanieść odpowiednią ilość pasty lutowniczej dla określonych typów komponentów i rozmiarów padów. Korzystanie z szablonu przekształca to, co mogłoby być żmudnym i podatnym na błędy procesem ręcznym, w szybki i profesjonalny etap montażu.


Podczas gdy niektórzy producenci oferują częściowe lub kompletne usługi montażowe, opcje te wymagają starannego rozważenia w przypadku złożonych projektów, takich jak Bitaxe. Dostępność komponentów, implikacje kosztowe i wartość edukacyjna samodzielnego montażu mają wpływ na tę decyzję. Wiele specjalistycznych komponentów wymaganych w projektach Bitcoin mining może nie być łatwo dostępnych za pośrednictwem standardowych usług montażu PCB, co sprawia, że pozyskiwanie komponentów i ręczny montaż są bardziej praktycznym podejściem. Przyszłe odcinki tej serii obejmą strategie pozyskiwania komponentów i techniki montażu, które pomogą z powodzeniem ukończyć projekt Bitaxe od gołej płytki drukowanej do funkcjonalnego urządzenia.


Proces produkcji i montażu stanowi kluczowy pomost między cyfrowym projektem a fizycznym wdrożeniem. Zrozumienie tych przepływów pracy pozwala przejąć kontrolę nad projektami, obniżyć koszty i zdobyć cenne praktyczne doświadczenie w zakresie profesjonalnych procesów produkcyjnych. Niezależnie od tego, czy budujesz pojedynczy prototyp, czy planujesz małą serię produkcyjną, opanowanie tych umiejętności otwiera nowe możliwości ożywienia projektów elektronicznych.


# Optymalizacja wydajności

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Benchmark twojego Bitaxe

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

Dążenie do optymalnej wydajności mining wymaga systematycznego podejścia do konfiguracji sprzętowej, która równoważy hashrate, wydajność i zarządzanie temperaturą. Bitaxe oferuje wiele parametrów konfiguracyjnych, które mogą znacząco wpłynąć na wydajność, ale ręczne testowanie każdej kombinacji ustawień byłoby niepraktyczne i czasochłonne. W tym rozdziale zbadano, jak wykorzystać zautomatyzowane narzędzia do testów porównawczych, aby naukowo zoptymalizować wydajność Bitaxe przy zachowaniu bezpiecznych warunków pracy.


### Zrozumienie metryk wydajności Bitaxe i konfiguracji bazowej


Zanim zagłębimy się w techniki optymalizacji, ważne jest, aby zrozumieć kluczowe wskaźniki wydajności, które definiują wydajność operacyjną Bitaxe. Podstawowe wskaźniki obejmują hashrate mierzony w terahash na sekundę, wydajność energetyczną wyrażoną w dżulach na terahash, częstotliwość ASIC w megahercach i napięcie rdzenia w woltach. Dobrze skonfigurowany Bitaxe może osiągnąć około 1,1 terahasha z wydajnością około 17 dżuli na terahash, pracując z częstotliwością 550 megaherców przy zmierzonym napięciu ASIC wynoszącym 1,14 wolta. Te wartości bazowe stanowią punkt odniesienia dla zrozumienia potencjalnych ulepszeń dostępnych dzięki systematycznej optymalizacji.


Związek między tymi wskaźnikami jest złożony i współzależny. Wyższe częstotliwości zazwyczaj zwiększają hashrate, ale także zwiększają zużycie energii i wytwarzanie ciepła. Podobnie, regulacja napięcia wpływa zarówno na wydajność, jak i charakterystykę termiczną. Wyzwanie polega na znalezieniu optymalnej równowagi, która maksymalizuje hashrate lub wydajność przy jednoczesnym utrzymaniu stabilnej pracy w bezpiecznych granicach temperatur. Ten proces optymalizacji wymaga metodycznego testowania wielu kombinacji parametrów, dzięki czemu zautomatyzowane narzędzia są nieocenione w osiąganiu optymalnych wyników.


### Architektura narzędzia benchmarkowego Bitaxe Hashrate


Narzędzie [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) reprezentuje zaawansowane rozwiązanie oparte na języku Python, pierwotnie opracowane przez WhiteCookie, a następnie ulepszone przez mrv777. To narzędzie o otwartym kodzie źródłowym, rozpowszechniane na licencji GPLv3, automatyzuje złożony proces testowania wielu kombinacji konfiguracji w celu zidentyfikowania optymalnych ustawień dla konkretnego sprzętu. Główną siłą narzędzia jest jego systematyczne podejście do testowania parametrów, przyrostowe dostosowywanie ustawień częstotliwości i napięcia przy jednoczesnym ciągłym monitorowaniu wskaźników wydajności i warunków termicznych.


Proces analizy porównawczej wymaga zwykle od 30 do 40 minut, podczas których narzędzie metodycznie testuje różne kombinacje ustawień częstotliwości i napięcia ASIC. Narzędzie rozpoczyna od konserwatywnych ustawień bazowych, zwykle zaczynając od 1,15 V i 500 megaherców, a następnie stopniowo zwiększa te parametry, jednocześnie monitorując hashrate, temperaturę i stabilność. Co ważne, narzędzie priorytetowo traktuje bezpieczną pracę nad maksymalną wydajnością, automatycznie wycofując się z ustawień, które powodują nadmierne wytwarzanie ciepła lub niestabilność. To konserwatywne podejście gwarantuje, że proces optymalizacji nie wpłynie negatywnie na trwałość i niezawodność sprzętu.


### Wymagania dotyczące instalacji i konfiguracji


Wdrożenie narzędzia Bitaxe Hashrate Benchmark wymaga kilku niezbędnych komponentów oprogramowania na komputerze lokalnym. Podstawowe wymagania obejmują Python do wykonywania skryptów porównawczych, Git do zarządzania repozytorium i opcjonalnie Visual Studio Code dla rozszerzonych możliwości środowiska programistycznego. Chociaż narzędzie może być obsługiwane z poziomu interfejsu wiersza poleceń, korzystanie ze zintegrowanego środowiska programistycznego, takiego jak VS Code, zapewnia lepszy wgląd w proces analizy porównawczej i analizę wyników.


Proces instalacji przebiega zgodnie ze standardowymi praktykami programistycznymi Pythona, zaczynając od sklonowania repozytorium z GitHub na lokalny komputer. Po pobraniu repozytorium należy utworzyć środowisko wirtualne, aby odizolować zależności narzędzia od instalacji Pythona w systemie. Izolacja ta zapobiega potencjalnym konfliktom z innymi aplikacjami Python i zapewnia spójne działanie. Po aktywacji środowiska wirtualnego należy zainstalować wymagane zależności przy użyciu dostarczonego pliku wymagań, który automatycznie konfiguruje wszystkie niezbędne biblioteki i moduły do prawidłowego działania narzędzia.


### Wykonywanie testów porównawczych i interpretacja wyników


Uruchomienie testu porównawczego wymaga wykonania pojedynczego polecenia Python, które zawiera adres IP Bitaxe jako parametr. Narzędzie automatycznie łączy się z interfejsem sieciowym górnika i rozpoczyna systematyczny proces testowania. Podczas wykonywania, narzędzie zapewnia szczegółowe informacje z dziennika pokazujące bieżącą iterację testu, zastosowane ustawienia napięcia i częstotliwości, wynikowy hashrate, napięcie wejściowe, odczyty temperatury i dane termiczne z krytycznych komponentów, takich jak konwerter buck. Ta informacja zwrotna w czasie rzeczywistym pozwala monitorować postęp testów porównawczych i zrozumieć, w jaki sposób różne ustawienia wpływają na wydajność koparki.


Inteligentne zarządzanie temperaturą w narzędziu staje się widoczne, gdy temperatura zbliża się do bezpiecznego progu 66 stopni Celsjusza. Zamiast przekraczać bezpieczne limity operacyjne, benchmark automatycznie redukuje ustawienia, aby utrzymać stabilność termiczną. To konserwatywne podejście zapewnia, że proces optymalizacji priorytetowo traktuje długoterminową niezawodność sprzętu nad krótkoterminowym wzrostem wydajności. Po zakończeniu, narzędzie generuje kompleksowe wyniki w formacie JSON, klasyfikując pięć najlepszych konfiguracji zarówno pod względem maksymalnego hashrate, jak i optymalnej wydajności. Wyniki te zapewniają jasne wskazówki dotyczące wyboru konfiguracji, która najlepiej odpowiada priorytetom operacyjnym, niezależnie od tego, czy koncentruje się na maksymalnej mocy wyjściowej, czy na efektywności energetycznej.


Narzędzie do testów porównawczych oferuje również opcje dostosowywania dla zaawansowanych użytkowników, którzy chcą zmodyfikować parametry testowania. Argumenty wiersza poleceń pozwalają określić niestandardowe napięcia początkowe i częstotliwości, umożliwiając bardziej ukierunkowaną optymalizację dla określonych przypadków użycia. Na przykład, jeśli wiesz już, że twój sprzęt działa dobrze przy wyższych częstotliwościach, możesz uruchomić test porównawczy przy podwyższonych ustawieniach, zamiast zaczynać od konserwatywnych ustawień domyślnych. Ta elastyczność sprawia, że narzędzie jest cenne zarówno dla początkujących użytkowników poszukujących zautomatyzowanej optymalizacji, jak i doświadczonych górników, którzy chcą dostroić określoną charakterystykę wydajności.


## Podkręcanie Bitaxe

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

Podkręcanie urządzeń Bitaxe wymaga starannego rozważenia zarówno ograniczeń sprzętowych, jak i wymagań dotyczących chłodzenia. Podczas gdy wielu użytkowników woli podkręcać swoje urządzenia w celu zapewnienia cichszej pracy, zrozumienie właściwych technik podkręcania jest niezbędne dla tych, którzy szukają maksymalnej wydajności bez uszkadzania sprzętu. Proces ten obejmuje zwiększenie częstotliwości i potencjalne dostosowanie ustawień napięcia poza specyfikacje fabryczne, co z natury zwiększa wytwarzanie ciepła i obciążenie komponentów.


Podstawą udanego podkręcania jest odpowiednia infrastruktura chłodzenia. Przed przystąpieniem do modyfikacji częstotliwości, należy upewnić się, że płyta Bitaxe posiada odpowiednie możliwości rozpraszania ciepła. Bitaxe Gamma z wysokiej jakości radiatorem i wentylatorem zapewnia niezbędne zarządzanie termiczne dla bezpiecznego podkręcania. Urządzenia z małymi radiatorami i nieodpowiednimi wentylatorami nie powinny być podkręcane, ponieważ słaba wydajność chłodzenia doprowadzi do dławienia termicznego i potencjalnego uszkodzenia sprzętu. Zależność między ciepłem a żywotnością podzespołów ma kluczowe znaczenie - nadmierne ciepło powoduje stres, który z czasem degraduje podzespoły elektroniczne, znacznie skracając żywotność urządzenia.


### Strategiczne rozmieszczenie radiatora


Najbardziej krytycznym komponentem wymagającym dodatkowego chłodzenia jest konwerter buck, mały czarny komponent znajdujący się z tyłu Bitaxe w pobliżu dużej cewki. Urządzenie to konwertuje przychodzące zasilanie 5 V w dół do odpowiedniego napięcia dla układu ASIC, zwykle około 1,2 V. Konwerter buck, często określany jako TPS, generuje znaczne ciepło podczas pracy i stanowi wąskie gardło termiczne, które ogranicza potencjał podkręcania. Zainstalowanie małego samoprzylepnego radiatora na tym elemencie nie tylko umożliwia wyższy poziom podkręcania, ale także poprawia ogólną wydajność poprzez zmniejszenie strat termicznych.


Dodatkowe umiejscowienie radiatora może przynieść korzyści innym obszarom płytki o wysokim natężeniu prądu. Obwody regulacji napięcia doświadczają znacznego obciążenia elektrycznego, gdy moc przepływa z sekcji wejściowej w dół przez różne ścieżki płyty, aby zasilić układ ASIC. Wielu doświadczonych overclockerów instaluje radiatory z przodu Bitaxe w tych obszarach o wysokim natężeniu prądu, aby jeszcze bardziej poprawić rozpraszanie ciepła. Choć nie jest to absolutnie konieczne w przypadku umiarkowanego podkręcania, te dodatkowe środki chłodzenia stają się ważne przy zwiększaniu częstotliwości do ekstremalnych poziomów.


### Uwagi i ograniczenia dotyczące układu chłodzenia


Kontroler ESP32, widoczny jako srebrny element na płytce, zazwyczaj nie wymaga dodatkowego chłodzenia. Element ten samodzielnie generuje minimalną ilość ciepła i nagrzewa się tylko w wyniku transferu ciepła z otaczających go komponentów. Instalowanie radiatorów w pobliżu ESP32 może potencjalnie zakłócać sąsiednią antenę Wi-Fi, pogarszając łączność bezprzewodową i jakość sygnału. Skoncentruj wysiłki związane z chłodzeniem na komponentach regulacji mocy i obszarze ASIC, a nie na obwodach sterujących.


Konfiguracje z dwoma wentylatorami oferują zarówno możliwości, jak i ograniczenia. Podczas gdy dodanie drugiego wentylatora do nadmuchu powietrza z tyłu Bitaxe może poprawić wydajność chłodzenia, oprogramowanie układowe urządzenia może prawidłowo sterować tylko jednym wentylatorem. Bitaxe ma dwa nagłówki wentylatorów, ale tylko jeden kontroler wentylatorów, co oznacza, że podłączenie dwóch wentylatorów spowoduje dezorientację oprogramowania układowego, ponieważ otrzyma ono sprzeczne sygnały RPM. Taka konfiguracja będzie działać, ale może skutkować nieprzewidywalnym zachowaniem sterowania wentylatorem.


### Podstawowa ocena wydajności


Przed przystąpieniem do jakichkolwiek modyfikacji podkręcania, należy ustalić bazowe wskaźniki wydajności, uruchamiając Bitaxe przy ustawieniach fabrycznych na kilka godzin. Monitoruj temperaturę ASIC, temperaturę regulatora napięcia i procentową prędkość wentylatora za pośrednictwem interfejsu internetowego. Optymalna temperatura pracy powinna utrzymywać ASIC poniżej 60°C, a regulator napięcia poniżej 60°C w normalnych warunkach. Jeśli urządzenie działa już w temperaturze powyżej 65°C na ASIC lub 70-80°C na regulatorze napięcia przy ustawieniach fabrycznych, przed przystąpieniem do podkręcania konieczne jest zastosowanie dodatkowego chłodzenia.


Systematyczne podejście do zwiększania częstotliwości obejmuje stopniowe kroki przy użyciu predefiniowanych opcji częstotliwości w menu ustawień. Rozpocznij od wybrania następnego dostępnego kroku częstotliwości powyżej bieżącego ustawienia, zachowując domyślne napięcie rdzenia. To konserwatywne podejście pozwala ocenić wpływ na temperaturę i stabilność przed wprowadzeniem dodatkowych zmian. Pozwól urządzeniu działać przy każdym nowym ustawieniu częstotliwości przez co najmniej 30 minut do godziny, monitorując trendy temperatury i stabilność szybkości mieszania przez cały okres oceny.


### Zaawansowana konfiguracja niestandardowa


Dostęp do niestandardowych ustawień częstotliwości i napięcia wymaga włączenia zaawansowanego interfejsu przetaktowywania poprzez dołączenie "?OC" do adresu URL interfejsu internetowego urządzenia. Odblokowuje to pola ręcznego wprowadzania danych w celu precyzyjnej kontroli częstotliwości i napięcia, wraz z odpowiednimi ostrzeżeniami o ryzyku działania poza zaprojektowanymi parametrami. Niestandardowy interfejs umożliwia precyzyjne dostrojenie poza standardowymi krokami częstotliwości, pozwalając doświadczonym użytkownikom zoptymalizować wydajność dla konkretnych konfiguracji chłodzenia.


W przypadku korzystania z ustawień niestandardowych należy zachować konserwatywne przyrosty o wielkości 10-15 MHz na krok regulacji. Takie metodyczne podejście zapobiega nagłym skokom temperatury i pozwala na prawidłowe testowanie stabilności na każdym poziomie częstotliwości. Niektórzy zaawansowani użytkownicy osiągają częstotliwości około 700 MHz z napięciami rdzenia dostosowanymi do 1,175 V lub podobnych wartości, ale te ekstremalne ustawienia wymagają rozległych modyfikacji chłodzenia i uważnego monitorowania. Regulator napięcia może działać w temperaturach do 100°C bez natychmiastowego uszkodzenia, ale wyższe temperatury zmniejszają wydajność i długoterminową niezawodność. Skuteczne podkręcanie wymaga cierpliwości, systematycznego testowania i ciągłego monitorowania w celu osiągnięcia stabilnej poprawy wydajności przy jednoczesnym zachowaniu integralności sprzętu.


# Sekcja końcowa

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Oceń ten kurs

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Wnioski

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>