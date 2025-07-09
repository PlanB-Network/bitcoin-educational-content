---
name: Filozofia rozwoju Bitcoin
goal: Rozwinąć głębokie filozoficzne zrozumienie zasad projektowania Bitcoin.
objectives: 

  - Analiza podstawowych kompromisów i decyzji architektonicznych w Bitcoin
  - Dowiedz się, jak oceniać proponowane zmiany i innowacje w protokole Bitcoin
  - Synteza ponad dekady historii rozwoju Bitcoin i debat społecznościowych
  - Stosowanie ram krytycznego myślenia podczas oceny nowych BIP


---

# Zanurz się głęboko w filozofię rozwoju Bitcoin



Filozofia rozwoju Bitcoin to kurs dla programistów Bitcoin, którzy rozumieją już podstawy koncepcji i procesów, takich jak Proof-of-Work, budowanie bloków i cykl życia transakcji, i którzy chcą awansować, zdobywając głębsze zrozumienie kompromisów i filozofii projektowania Bitcoin.

Powinien on pomóc nowym deweloperom w przyswojeniu najważniejszych wniosków z ponad dekady rozwoju Bitcoin i debaty publicznej, zapewniając im jednocześnie przydatny kontekst do oceny nowych pomysłów (dobrych i złych!).


### Czego się spodziewać?


Jak wspomniano powyżej, jest to praktyczny przewodnik dla programistów Bitcoin. Jednak Bitcoin jest szerokim i złożonym tematem i nie moglibyśmy tutaj omówić wszystkich jego aspektów. Mamy nadzieję, że w tym kursie omówimy funkcje niezbędne do rozpoczęcia działalności programistycznej, a także umożliwimy jej dalsze samodzielne odkrywanie.


Jest wiele osób zaangażowanych w Bitcoin; ponieważ niektóre z nich mają przeciwstawne opinie, tutaj możesz znaleźć zasoby, które wyrażają sprzeczne pomysły. Zawsze jednak staramy się trzymać domeny faktów, gdzie opinie nie mają znaczenia.


### Kto to napisał?


Kurs ten został zaadaptowany z książki o tym samym tytule, której głównym autorem jest Kalle Rosenbaum, a Linnéa Rosenbaum jest współautorką.

Książka została zamówiona i sfinansowana przez [Chaincode Labs](https://learning.chaincode.com/), centrum rozwoju, które prowadzi programy edukacyjne dla programistów, którzy chcą dowiedzieć się więcej o rozwoju Bitcoin.


+++



# Wprowadzenie

<partId>58c48e9b-e285-4dc6-8952-6cc5140b1313</partId>


## Przegląd kursu

<chapterId>28b7256b-9cb0-463e-a82d-d732be86c98c</chapterId>


Witamy w kursie PHI 301 na temat filozofii rozwoju Bitcoin.


Bitcoin to coś więcej niż tylko kryptowaluta, to ucieleśnienie filozoficznej wizji decentralizacji, prywatności, braku zaufania i odporności. Kurs ten został zaprojektowany specjalnie dla programistów zaznajomionych już z technicznymi podstawami Bitcoin, którzy chcą teraz pogłębić swoje zrozumienie zasad leżących u podstaw projektu i zarządzania Bitcoin.


W trakcie tego kursu zyskasz jasność co do podstawowych wartości i strategii, które kierowały ewolucją Bitcoin przez ponad dekadę. Poprzez dogłębne zbadanie tych tematów, rozwiniesz krytyczną perspektywę potrzebną do oceny i przyczynienia się do przyszłego rozwoju z pewnością siebie.


### Główne wartości Bitcoin


Co sprawia, że Bitcoin jest wyjątkowy? Ta sekcja ujawnia podstawowe wartości leżące u podstaw projektu Bitcoin. Poznasz **decentralizację**, kamień węgielny zapewniający, że żaden pojedynczy podmiot nie kontroluje sieci; **niezaufanie**, klucz do wyeliminowania zależności od stron trzecich; **prywatność**, niezbędną zarówno dla wolności jednostki, jak i integralności systemu; oraz **nieskończony Supply**, zakodowaną gwarancję niedoboru, która kształtuje tożsamość ekonomiczną Bitcoin. Opanowanie tych pojęć pozwoli ci w pełni zrozumieć mocne i słabe strony Bitcoin.


### Bitcoin Zarządzanie


Poruszanie się po złożonym krajobrazie zarządzania Bitcoin wymaga nie tylko wiedzy technicznej, ale także zrozumienia unikalnego podejścia Bitcoin do konsensusu i podejmowania decyzji. W tej sekcji poznasz mechanizmy i filozofie kryjące się za krytycznymi procesami, takimi jak aktualizacje protokołów, konieczność przeciwstawnego myślenia, siłę współpracy open source, ciągłe wyzwania związane ze skalowaniem oraz zniuansowane strategie wymagane, gdy sprawy nieuchronnie idą źle. Wyposażony w tę wiedzę, będziesz przygotowany nie tylko do uczestnictwa, ale także do skutecznego i odpowiedzialnego kształtowania przyszłości Bitcoin.


Gotowy na kolejny krok w swojej podróży Bitcoin? Zaczynajmy!


***UWAGA: Jeśli podczas kursu napotkasz nieznane terminy związane z Bitcoin, zapoznaj się z [glosariuszem] (https://planb.network/resources/glossary), aby znaleźć definicje*




# Wartości centralne Bitcoin

<partId>2d6c683b-54c8-5465-b2ca-4e96a6828834</partId>


## Decentralizacja

<chapterId>9397c84b-0038-5d0e-88d5-11767ce8182d</chapterId>




Analizujemy, czym jest decentralizacja i dlaczego jest ona niezbędna do funkcjonowania Bitcoin. Rozróżniamy między

decentralizacji górników i pełnych węzłów oraz omówić, co wnoszą one do odporności na cenzurę, jednej z najważniejszych właściwości Bitcoin.


Następnie dyskusja przenosi się na zrozumienie neutralności - lub braku uprawnień wobec użytkowników, górników i deweloperów - która jest niezbędną właściwością każdego zdecentralizowanego systemu. Na koniec poruszamy kwestię tego, jak Hard może być w stanie zrozumieć zdecentralizowany system, taki jak Bitcoin, i przedstawiamy kilka modeli mentalnych, które mogą pomóc w jego zrozumieniu.


System bez centralnego punktu kontroli jest określany jako *zdecentralizowany*. Bitcoin ma na celu uniknięcie centralnego punktu kontroli, a dokładniej *centralnego punktu cenzury*.


Decentralizacja jest środkiem do osiągnięcia *odporności na cenzurę*.


Istnieją dwa główne aspekty decentralizacji w Bitcoin: Decentralizacja Miner i decentralizacja Full node.


Decentralizacja Miner odnosi się do faktu, że przetwarzanie transakcji nie jest wykonywane ani koordynowane przez żaden centralny podmiot. Decentralizacja Full node odnosi się do faktu, że walidacja bloków, tj. danych wydobywanych przez górników, odbywa się na brzegu sieci, ostatecznie przez jej użytkowników, a nie przez kilka zaufanych organów.


![](assets/decentralization-banner.webp)


### Decentralizacja Miner



Przed Bitcoin podejmowano próby stworzenia walut cyfrowych, ale większość z nich zakończyła się niepowodzeniem z powodu braku decentralizacji zarządzania i oporu przed cenzurą.


Decentralizacja Miner w Bitcoin oznacza, że *zamawianie transakcji* nie jest przeprowadzane przez żaden pojedynczy podmiot lub ustalony zestaw podmiotów. Jest ono przeprowadzane zbiorowo przez wszystkie podmioty, które chcą w nim uczestniczyć; ten kolektyw górników jest dynamicznym zbiorem użytkowników. Każdy może do niego dołączyć lub go opuścić. Ta właściwość sprawia, że Bitcoin jest odporny na cenzurę.


Gdyby Bitcoin był scentralizowany, byłby podatny na tych, którzy chcieliby go cenzurować, takich jak rządy. Spotkałby go ten sam los, co wcześniejsze próby stworzenia cyfrowego pieniądza. We wstępie do [artykułu](https://www.blockstream.com/sidechains.pdf) zatytułowanego "Enabling Blockchain Innovations with Pegged Sidechains", autorzy wyjaśniają, w jaki sposób wczesne wersje cyfrowego pieniądza nie były przystosowane do przeciwstawnego środowiska (patrz także rozdział "Adversarial Thinking" w następnej części).


David Chaum wprowadził cyfrową gotówkę jako temat badań w 1983 roku, w środowisku z centralnym serwerem, który jest zaufany, aby zapobiec Double-spending. Aby zmniejszyć ryzyko prywatności dla osób fizycznych ze strony tej centralnej zaufanej strony i wymusić zamienność, Chaum wprowadził ślepy podpis, który wykorzystał do zapewnienia kryptograficznych środków zapobiegających łączeniu podpisów centralnego serwera (które reprezentują monety), jednocześnie umożliwiając centralnemu serwerowi zapobieganie podwójnym wydatkom.

Wymóg centralnego serwera stał się piętą achillesową cyfrowej gotówki[Gri99]. Chociaż możliwe jest rozproszenie tego pojedynczego punktu awarii poprzez zastąpienie podpisu centralnego serwera podpisem progowym kilku sygnatariuszy, dla możliwości audytu ważne jest, aby sygnatariusze byli odrębni i identyfikowalni. To nadal pozostawia system podatny na awarie, ponieważ każdy podpisujący może zawieść lub zostać zmuszony do awarii, jeden po drugim.


Stało się jasne, że korzystanie z centralnego serwera do zamawiania transakcji nie jest realną opcją ze względu na wysokie ryzyko cenzury. Nawet gdyby zastąpić centralny serwer federacją ustalonego zestawu n serwerów, z których co najmniej m musi zatwierdzić zamówienie, nadal istniałyby trudności. Problem rzeczywiście zmieniłby się na taki, w którym użytkownicy musieliby zgodzić się na ten zestaw n serwerów, a także na to, jak zastąpić złośliwe serwery dobrymi bez polegania na centralnym organie.


Zastanówmy się, co mogłoby się stać, gdyby Bitcoin można było cenzurować. Cenzor mógłby naciskać na użytkowników, aby identyfikowali się, deklarowali, skąd pochodzą ich pieniądze lub co za nie kupują, zanim pozwolą swoim transakcjom wejść do Blockchain.


Ponadto brak oporu cenzury pozwoliłby cenzorowi zmusić użytkowników do przyjęcia nowych zasad systemu. Na przykład, mogliby narzucić zmianę, która pozwoliłaby im zawyżyć pieniądze Supply, wzbogacając się w ten sposób. W takim przypadku użytkownik weryfikujący bloki miałby trzy opcje radzenia sobie z nowymi zasadami:



- Przyjęcie: Zaakceptuj zmiany i wprowadź je do Full node.
- Odrzuć: Odmowa przyjęcia zmian; pozostawia to użytkownika z systemem, który nie przetwarza już transakcji, ponieważ bloki cenzora są teraz uznawane za nieważne przez Full node użytkownika.
- Przeniesienie: Wyznaczenie nowego centralnego punktu kontroli; wszyscy użytkownicy muszą dowiedzieć się, jak koordynować, a następnie uzgodnić nowy centralny punkt kontroli.


Jeśli im się uda, te same problemy najprawdopodobniej powrócą w przyszłości, biorąc pod uwagę, że system pozostał tak samo cenzurowany jak wcześniej.


Żadna z tych opcji nie jest korzystna dla użytkownika.


Odporność na cenzurę poprzez decentralizację jest tym, co odróżnia Bitcoin od innych systemów pieniężnych, ale nie jest to łatwe do osiągnięcia ze względu na *problem Double-spending*. Jest to problem polegający na upewnieniu się, że nikt nie może wydać tej samej monety dwa razy, co wiele osób uważało za niemożliwe do rozwiązania w sposób zdecentralizowany. Satoshi Nakamoto pisze w swoim [Bitcoin whitepaper](https://planb.network/Bitcoin.pdf) o tym, jak rozwiązać problem Double-spending:


> W niniejszym artykule proponujemy rozwiązanie problemu Double-spending przy użyciu rozproszonego serwera Timestamp typu peer-to-peer do generate obliczeniowego dowodu chronologicznej kolejności transakcji.


Używa on tutaj osobliwie brzmiącego wyrażenia "rozproszony serwer Timestamp peer-to-peer". Słowem kluczowym jest tutaj *rozproszony*, co w tym kontekście oznacza, że nie ma centralnego punktu kontroli. Następnie Nakamoto wyjaśnia, w jaki sposób Proof-of-Work jest rozwiązaniem.

Nikt jednak nie wyjaśnił tego lepiej niż

[Gregory Maxwell na Reddit](https://www.reddit.com/r/Bitcoin/comments/ddddfl/question_on_the_vulnerability_of_bitcoin/f2g9e7b/), gdzie odpowiada komuś, kto proponuje ograniczenie mocy Hash górników, aby uniknąć potencjalnych ataków 51%:


> Zdecentralizowany system, taki jak Bitcoin, wykorzystuje wybory publiczne. Ale w zdecentralizowanym systemie nie można po prostu głosować na "ludzi", ponieważ wymagałoby to scentralizowanej strony upoważniającej ludzi do głosowania. Zamiast tego Bitcoin wykorzystuje głosowanie mocą obliczeniową, ponieważ możliwe jest zweryfikowanie mocy obliczeniowej bez pomocy jakiejkolwiek scentralizowanej instytucji
strona trzecia.


W poście wyjaśniono, w jaki sposób zdecentralizowana sieć Bitcoin może dojść do porozumienia w sprawie zamawiania transakcji za pomocą Proof-of-Work.


Następnie podsumowuje, mówiąc, że atak 51% nie jest szczególnie niepokojący w porównaniu z ludźmi, którzy nie dbają lub nie rozumieją właściwości decentralizacji Bitcoin:


> Znacznie większym ryzykiem dla Bitcoin jest to, że społeczeństwo korzystające z niego nie zrozumie, nie będzie dbać i nie będzie chronić właściwości decentralizacji, które sprawiają, że jest on cenniejszy niż scentralizowane alternatywy.

Wniosek jest ważny. Jeśli ludzie nie będą chronić decentralizacji Bitcoin, która jest proxy dla jego odporności na cenzurę, Bitcoin może paść ofiarą scentralizowanych mocy, aż stanie się tak scentralizowany, że cenzura stanie się rzeczą. Wtedy większość, jeśli nie całość, jego propozycji wartości zniknie. To prowadzi nas do następnej sekcji dotyczącej decentralizacji Full node.


### Decentralizacja Full node



W powyższych akapitach rozmawialiśmy głównie o decentralizacji Miner i o tym, jak centralizacja górników może pozwolić na cenzurę. Ale jest też inny aspekt decentralizacji, a mianowicie *decentralizacja Full node*.


Znaczenie decentralizacji Full node jest związane z brakiem zaufania. Załóżmy, że użytkownik przestaje uruchamiać własny Full node z powodu, na przykład, zaporowego wzrostu kosztów eksploatacji. W takim przypadku musi on wejść w interakcję z siecią Bitcoin w inny sposób, być może za pomocą portfeli internetowych lub lekkich portfeli, co wymaga pewnego poziomu zaufania do dostawców tych usług.


Użytkownik przechodzi od bezpośredniego egzekwowania zasad konsensusu sieciowego do zaufania, że zrobi to ktoś inny. Załóżmy teraz, że większość użytkowników deleguje egzekwowanie konsensusu do zaufanego podmiotu. W takim przypadku sieć może szybko popaść w centralizację, a zasady sieci mogą zostać zmienione przez spiskujących złośliwych aktorów.


W [a

Artykuł w Bitcoin Magazine](https://bitcoinmagazine.com/technical/decentralist-perspective-Bitcoin-might-need-small-blocks-1442090446), Aaron van Wirdum przeprowadza wywiad z deweloperami Bitcoin na temat ich poglądów na temat decentralizacji i ryzyka związanego ze zwiększeniem maksymalnego rozmiaru bloku Bitcoin. Dyskusja ta była tematem Hot w latach 2014-2017, kiedy wiele osób spierało się o zwiększenie limitu wielkości bloku, aby umożliwić większą przepustowość transakcji.


Potężnym argumentem przeciwko zwiększaniu rozmiaru bloku jest to, że zwiększa to koszt weryfikacji Jeśli koszt weryfikacji wzrośnie, zmusi to niektórych użytkowników do zaprzestania uruchamiania pełnych węzłów. To z kolei doprowadzi do tego, że więcej osób nie będzie w stanie korzystać z systemu w sposób Trustless.


Pieter Wuille jest cytowany w artykule, w którym wyjaśnia ryzyko centralizacji Full node:


> Jeśli wiele firm korzysta z Full node, oznacza to, że wszystkie muszą zostać przekonane do wdrożenia innego zestawu reguł. Innymi słowy: decentralizacja walidacji bloków jest tym, co nadaje regułom konsensusu ich wagę.
> Ale jeśli liczba Full node spadnie bardzo nisko, na przykład dlatego, że wszyscy używają tych samych portfeli internetowych, giełd i SPV lub portfeli mobilnych, regulacja może stać się rzeczywistością. A jeśli władze mogą regulować zasady konsensusu, oznacza to, że mogą zmienić wszystko, co czyni Bitcoin Bitcoin. Nawet limit 21 milionów Bitcoin.

Proszę bardzo. Użytkownicy Bitcoin powinni uruchomić własne pełne węzły, aby powstrzymać organy regulacyjne i duże korporacje przed próbami zmiany zasad konsensusu.


### Neutralność



Bitcoin jest neutralny, lub bez pozwolenia, jak ludzie lubią go nazywać. Oznacza to, że Bitcoin nie dba o to, kim jesteś i do czego go używasz.


Bitcoin jest neutralny, co jest dobrą rzeczą i jedynym sposobem, w jaki może działać. Gdyby był kontrolowany przez organizację, byłby po prostu kolejnym typem wirtualnego obiektu i nie byłbym nim zainteresowany


Tak długo, jak grasz zgodnie z zasadami, możesz go używać, jak chcesz, bez pytania nikogo o pozwolenie. Obejmuje to *Mining*, *transakcje* i *budowanie protokołów i usług* na Bitcoin:



- Gdyby *Mining* był procesem wymagającym zezwolenia, potrzebowalibyśmy centralnego organu, który wybierałby, kto może wydobywać. Najprawdopodobniej doprowadziłoby to do tego, że górnicy musieliby podpisywać umowy prawne, w których zgadzaliby się na

do cenzurowania transakcji zgodnie z kaprysami władz centralnych, co przede wszystkim zaprzecza celowi Mining.



- Gdyby osoby *transakcjonujące* w Bitcoin musiały podać dane osobowe, zadeklarować cel swoich transakcji lub w inny sposób udowodnić, że są godne dokonywania transakcji, potrzebowalibyśmy również centralnego punktu władzy do zatwierdzania użytkowników lub transakcji. Ponownie, doprowadziłoby to do cenzury i wykluczenia.



- Gdyby deweloperzy musieli prosić o pozwolenie na *budowanie protokołów* na bazie Bitcoin, rozwijane byłyby tylko protokoły dozwolone przez centralny komitet przyznający uprawnienia deweloperom. To, ze względu na interwencję rządu, nieuchronnie wykluczyłoby wszystkie protokoły chroniące prywatność i wszelkie próby poprawy decentralizacji.


Na wszystkich poziomach próba nałożenia ograniczeń na to, kto może używać Bitcoin do czego, zaszkodzi Bitcoin do tego stopnia, że przestanie on spełniać swoją propozycję wartości.


Pieter Wuille https://Bitcoin.stackexchange.com/a/92055/69518[odpowiada na pytanie dotyczące stosu Exchange] o tym, jak Blockchain odnosi się do zwykłych baz danych. Wyjaśnia, w jaki sposób można osiągnąć brak uprawnień poprzez wykorzystanie Proof-of-Work w połączeniu z zachętami ekonomicznymi.


Podsumowuje:


> Korzystanie z algorytmów konsensusu Trustless, takich jak PoW, dodaje coś, czego nie daje żadna inna konstrukcja (uczestnictwo bez pozwolenia, co oznacza, że nie ma określonej grupy uczestników, którzy mogą cenzurować twoje zmiany), Korzystanie z algorytmów konsensusu Trustless, takich jak PoW, dodaje coś nie, ale wiąże się z wysokimi kosztami, a jego założenia ekonomiczne sprawiają, że jest on praktycznie użyteczny tylko dla systemów, które definiują własną kryptowalutę.
> Prawdopodobnie jest tylko jedno miejsce na świecie dla jednego lub kilku faktycznie używanych egzemplarzy.

Wyjaśnia on, że aby osiągnąć brak uprawnień, system najprawdopodobniej potrzebuje własnej waluty, tym samym "ograniczając przypadki użycia do efektywnie tylko kryptowalut". Wynika to z faktu, że uczestnictwo bez zezwoleń lub Mining wymaga zachęt ekonomicznych wbudowanych w sam system.


### Rozwijanie decentralizacji



Istotnym aspektem Bitcoin jest to, że nikt go nie kontroluje. W Bitcoin nie ma komitetów ani kierownictwa. Gregory Maxwell, ponownie [na subreddicie Bitcoin] (https://www.reddit.com/r/Bitcoin/comments/s82t2n/comment/htdte7w/?utm_source=share&utm_medium=web2x&context=3), porównuje to do języka angielskiego w intrygujący sposób:


> Wielu ludzi ma Hard czas na zrozumienie autonomicznych systemów, w ich życiu jest wiele rzeczy, takich jak język angielski - ale ludzie po prostu biorą je za pewnik i nawet nie myślą o nich jako o systemach. Tkwią w scentralizowanym sposobie myślenia, w którym wszystko, co uważają za "rzecz", ma władzę, która to kontroluje.
>

> Bitcoin nie skupia się na niczym. Różne osoby, które przyjęły Bitcoin, z własnej woli zdecydowały się go promować, a sposób, w jaki to robią, to ich własna sprawa. Ludzie zafiksowani na punkcie władzy mogą widzieć te działania i wierzyć, że są one jakąś operacją władz Bitcoin, ale taka władza nie istnieje.


Sposób, w jaki Bitcoin działa poprzez decentralizację, przypomina niezwykłą zbiorową inteligencję występującą wśród wielu gatunków w przyrodzie. Informatyk Radhika Nagpal mówi w [Ted talk](https://www.ted.com/talks/radhika_nagpal_what_intelligent_machines_can_learn_from_a_school_of_fish) o zbiorowym zachowaniu ławic ryb i o tym, jak naukowcy próbują je naśladować za pomocą robotów.


> Po drugie, co nadal uważam za najbardziej niezwykłe, wiemy, że nie ma liderów nadzorujących tę ławicę ryb. Zamiast tego, to niesamowite zachowanie zbiorowego umysłu wyłania się wyłącznie z interakcji jednej ryby z drugą.
> W jakiś sposób istnieją interakcje lub zasady zaangażowania między sąsiadującymi rybami, które sprawiają, że wszystko się udaje.

Zwraca uwagę, że wiele systemów, zarówno naturalnych, jak i sztucznych, może działać i działa bez liderów, i są one potężne i odporne. Każda jednostka wchodzi w interakcję tylko ze swoim bezpośrednim otoczeniem, ale razem tworzą coś ogromnego.


![](assets/fishschool.webp)

*Ławice ryb nie mają liderów*


Bez względu na to, co myślisz o Bitcoin, jego zdecentralizowana natura sprawia, że trudno go kontrolować. Bitcoin istnieje i nic nie można na to poradzić. Jest to coś, co należy badać, a nie dyskutować.


### Wnioski dotyczące decentralizacji


Rozróżniamy decentralizację Full node i decentralizację Mining. Decentralizacja Mining jest środkiem do osiągnięcia odporności na cenzurę, podczas gdy decentralizacja Full node jest tym, co utrzymuje zasady konsensusu sieci Hard do zmiany bez szerokiego poparcia wśród użytkowników.


Zdecentralizowany charakter Bitcoin pozwala na neutralność wobec deweloperów, użytkowników i górników. Każdy może w nim uczestniczyć bez pytania o pozwolenie.


Zdecentralizowane systemy mogą być Hard, ale istnieją pewne modele mentalne, które mogą pomóc, na przykład język angielski lub ławice ryb.


## Nieufność

<chapterId>0506ba61-16a3-543c-95fa-3f3e2dd64121</chapterId>



![](assets/trustlessness-banner.webp)


W tym rozdziale przeanalizowano koncepcję braku zaufania, co to oznacza z punktu widzenia informatyki i dlaczego Bitcoin musi być Trustless, aby zachować swoją propozycję wartości.

Następnie porozmawiamy o tym, co to znaczy używać Bitcoin w sposób Trustless i jakie gwarancje może dać Full node, a jakich nie.

W ostatniej sekcji przyjrzymy się rzeczywistej interakcji między Bitcoin a rzeczywistym oprogramowaniem lub użytkownikami oraz potrzebie kompromisów między wygodą a brakiem zaufania, aby w ogóle cokolwiek zrobić.


Ludzie często mówią takie rzeczy jak "Bitcoin jest świetny, ponieważ jest Trustless".


Co oznaczają słowa Trustless? Pieter Wuille wyjaśnia ten powszechnie używany termin na stronie [Stack Exchange](https://Bitcoin.stackexchange.com/a/45674/69518):


> Zaufanie, o którym mówimy w "Trustless", jest abstrakcyjnym terminem technicznym. System rozproszony jest nazywany Trustless, gdy nie wymaga żadnych zaufanych stron do prawidłowego działania.

Krótko mówiąc, słowo *Trustless* odnosi się do właściwości protokołu Bitcoin, dzięki której może on logicznie funkcjonować bez "żadnych zaufanych stron". Różni się to od zaufania, które nieuchronnie trzeba pokładać w uruchamianym oprogramowaniu lub sprzęcie. Więcej na temat tego drugiego aspektu zaufania zostanie omówione w dalszej części tego rozdziału.


W scentralizowanych systemach polegamy na reputacji centralnego aktora, aby upewnić się, że zadba on o bezpieczeństwo lub wycofa się w przypadku problemów, a także na systemie prawnym, który sankcjonuje wszelkie naruszenia. Te wymagania dotyczące zaufania są problematyczne w pseudonimowych systemach zdecentralizowanych - nie ma możliwości odwołania się, więc tak naprawdę nie może być żadnego zaufania. We wstępie do [Bitcoin whitepaper](https://Bitcoin.org/Bitcoin.pdf), Satoshi Nakamoto opisuje ten problem:


> Handel w Internecie opiera się niemal wyłącznie na instytucjach finansowych służących jako zaufane strony trzecie do przetwarzania płatności elektronicznych.
> Chociaż system działa wystarczająco dobrze w przypadku większości transakcji, nadal cierpi z powodu nieodłącznych słabości modelu opartego na zaufaniu.  Całkowicie nieodwracalne transakcje nie są tak naprawdę możliwe, ponieważ instytucje finansowe nie mogą uniknąć mediacji w sporach. Koszt mediacji zwiększa koszty transakcji, ograniczając minimalny praktyczny rozmiar transakcji i odcinając możliwość dokonywania niewielkich transakcji dorywczych, a także wiąże się z szerszym kosztem utraty możliwości dokonywania nieodwracalnych płatności za nieodwracalne usługi.
> Wraz z możliwością odwrócenia, rośnie potrzeba zaufania. Sprzedawcy muszą uważać na swoich klientów, żądając od nich więcej informacji, niż by potrzebowali.  Pewien odsetek oszustw jest akceptowany jako nieunikniony. Tych kosztów i niepewności związanych z płatnościami można uniknąć osobiście, korzystając z fizycznej waluty, ale nie istnieje żaden mechanizm umożliwiający dokonywanie płatności za pośrednictwem kanału komunikacyjnego bez zaufanej strony

Wydaje się, że nie możemy mieć zdecentralizowanego systemu opartego na zaufaniu i dlatego brak zaufania jest ważny w Bitcoin.


Aby korzystać z Bitcoin w sposób Trustless, należy uruchomić w pełni walidujący węzeł Bitcoin. Tylko wtedy będziesz w stanie zweryfikować, czy bloki, które otrzymujesz od innych, są zgodne z zasadami konsensusu; na przykład, czy harmonogram emisji monet jest przestrzegany i czy nie występują podwójne wydatki na Blockchain. Jeśli nie uruchamiasz Full node, zlecasz weryfikację bloków Bitcoin komuś innemu i ufasz, że powie ci prawdę, co oznacza, że nie korzystasz z Bitcoin bez zaufania.


David Harding jest autorem [artykułu na stronie Bitcoin.org] (https://Bitcoin.org/en/Bitcoin-core/features/validation) wyjaśniającego, w jaki sposób prowadzenie Full node - lub korzystanie z Bitcoin bez zaufania - faktycznie pomaga:


> Waluta Bitcoin działa tylko wtedy, gdy ludzie akceptują bitcoiny w Exchange w zamian za inne wartościowe rzeczy. Oznacza to, że to ludzie akceptujący bitcoiny nadają im wartość i decydują o tym, jak ma działać Bitcoin.
>

> Akceptując bitcoiny, masz prawo do egzekwowania zasad Bitcoin, takich jak zapobieganie konfiskacie bitcoinów dowolnej osoby bez dostępu do jej kluczy prywatnych.
>

> Niestety, wielu użytkowników outsourcuje swoją moc egzekwowania prawa. Pozostawia to decentralizację Bitcoin w osłabionym stanie, w którym garstka górników może zmówić się z garstką banków i bezpłatnych usług, aby zmienić zasady Bitcoin dla wszystkich niezweryfikujących użytkowników, którzy przekazali swoją moc na zewnątrz.
>

> W przeciwieństwie do innych portfeli, Bitcoin Core egzekwuje zasady - więc jeśli górnicy i banki zmienią zasady dla swoich niezweryfikowanych użytkowników, użytkownicy ci nie będą mogli płacić w pełni zweryfikowanym użytkownikom Bitcoin Core, takim jak Ty.


Twierdzi on, że uruchomienie Full node pomoże ci zweryfikować każdy aspekt Blockchain bez ufania komukolwiek innemu, aby upewnić się, że monety, które otrzymujesz od innych, są autentyczne. To świetnie, ale jest jedna ważna rzecz, w której Full node nie może ci pomóc: nie może zapobiec podwójnym wydatkom poprzez przepisywanie łańcucha:


> Należy pamiętać, że chociaż wszystkie programy - w tym Bitcoin Core - są podatne na przepisywanie łańcucha, Bitcoin zapewnia mechanizm obronny: im więcej potwierdzeń mają twoje transakcje, tym jesteś bezpieczniejszy. Nie ma znanej zdecentralizowanej obrony lepszej niż ta.

Bez względu na to, jak zaawansowane jest twoje oprogramowanie, nadal musisz ufać, że bloki zawierające twoje monety nie zostaną przepisane. Jednak, jak wskazał Harding, można poczekać na pewną liczbę potwierdzeń, po których prawdopodobieństwo przepisania łańcucha jest na tyle małe, że można je zaakceptować.


Zachęty do korzystania z Bitcoin w sposób Trustless są zgodne z potrzebą decentralizacji systemu Full node. Im więcej osób korzysta z własnych pełnych węzłów, tym większa decentralizacja Full node, a tym samym silniejsza ochrona Bitcoin przed złośliwymi zmianami w protokole. Niestety, jak wyjaśniono w sekcji dotyczącej decentralizacji Full node, użytkownicy często wybierają zaufane usługi w wyniku nieuniknionego kompromisu między brakiem zaufania a wygodą.


Brak zaufania Bitcoin jest absolutnie niezbędny z perspektywy systemu. W 2018 r. Matt Corallo [mówił o braku zaufania] (https://btctranscripts.com/baltic-honeybadger/2018/trustlessness-scalability-and-directions-in-security-models/) na konferencji Baltic Honeybadger w Rydze.


![video](https://youtu.be/66ZoGUAnY9s?t=4019)


Istotą tego wykładu jest to, że nie można budować systemów Trustless na zaufanym systemie, ale można budować zaufane systemy - na przykład Wallet - na zaufanym systemie Trustless.



![width=50%](assets/trust.webp)


Podstawa Trustless Layer pozwala na różne kompromisy na wyższych poziomach


Ten model bezpieczeństwa pozwala projektantowi systemu wybrać kompromisy

które mają dla nich sens, bez wymuszania tych kompromisów na innych.


### Nie ufaj, weryfikuj



Bitcoin działa bezawaryjnie, ale nadal musisz w pewnym stopniu ufać swojemu oprogramowaniu i sprzętowi. Dzieje się tak dlatego, że oprogramowanie lub sprzęt mogą nie być zaprogramowane do robienia tego, co podano na pudełku. Na przykład:



- Procesor może być złośliwie zaprojektowany do wykrywania operacji kryptograficznych klucza prywatnego i wycieku danych klucza prywatnego.
- Generator liczb losowych systemu operacyjnego może nie być tak losowy, jak twierdzi.
- Bitcoin Core mógł przemycić kod, który wyśle twoje klucze prywatne do jakiegoś złego aktora.


Tak więc, oprócz uruchomienia Full node, musisz również upewnić się, że uruchamiasz to, co zamierzasz. Użytkownik Reddit brianddk [napisał artykuł](https://www.reddit.com/r/Bitcoin/comments/smj1ep/bitcoin_v220_and_guix_stronger_defense_against/) o różnych poziomach zaufania, które można wybrać podczas weryfikacji oprogramowania. W sekcji "Zaufanie do budowniczych" mówi o odtwarzalnych kompilacjach:


> Odtwarzalne kompilacje to sposób na zaprojektowanie oprogramowania w taki sposób, aby wielu deweloperów społeczności mogło zbudować oprogramowanie i upewnić się, że ostateczny zbudowany instalator jest identyczny z tym, co produkują inni deweloperzy. W przypadku bardzo publicznego, odtwarzalnego projektu, takiego jak Bitcoin, żaden pojedynczy deweloper nie musi być całkowicie zaufany. Wielu deweloperów może wykonać kompilację i potwierdzić, że stworzyli ten sam plik, który został podpisany cyfrowo przez pierwotnego twórcę.

Artykuł definiuje 5 poziomów zaufania: zaufanie do witryny, twórców, kompilatora, jądra i sprzętu.


Aby jeszcze bardziej pogłębić temat odtwarzalnych kompilacji, Carl Dong [przedstawił prezentację na temat Guix](https://btctranscripts.com/breaking-Bitcoin/2019/Bitcoin-build-system/) wyjaśniając, dlaczego ufanie systemowi operacyjnemu, bibliotekom i kompilatorom może być problematyczne i jak to naprawić za pomocą systemu o nazwie Guix, który jest obecnie używany przez Bitcoin Core.


> Co więc możemy zrobić z faktem, że nasz toolchain może mieć kilka zaufanych plików binarnych, które mogą być odtwarzalnie złośliwe? Musimy być nie tylko odtwarzalni. Musimy być bootrapowalni. Nie możemy mieć tak wielu narzędzi binarnych, które musimy pobierać i którym musimy ufać z zewnętrznych serwerów kontrolowanych przez inne organizacje.
>

> Powinniśmy wiedzieć, w jaki sposób te narzędzia są budowane i dokładnie, jak możemy przejść przez proces ich ponownego budowania, najlepiej ze znacznie mniejszego zestawu zaufanych plików binarnych. Musimy zminimalizować nasz zaufany zestaw plików binarnych tak bardzo, jak to możliwe, i mieć łatwą do skontrolowania ścieżkę od tych łańcuchów narzędzi do tego, czego używamy do budowy Bitcoin. Pozwoli nam to zmaksymalizować weryfikację i zminimalizować zaufanie.

Następnie wyjaśnia, w jaki sposób Guix pozwala nam zaufać tylko minimalnemu plikowi binarnemu o rozmiarze 357 bajtów, który można zweryfikować i w pełni zrozumieć, jeśli wiesz, jak interpretować instrukcje. Jest to dość niezwykłe: jeden weryfikuje, czy 357-bajtowy plik binarny robi to, co powinien, a następnie używa go do zbudowania pełnego systemu kompilacji z kodu źródłowego i kończy z plikiem binarnym Bitcoin Core, który powinien być dokładną kopią kompilacji każdego innego.


Istnieje mantra, którą podpisuje się wielu bitcoinerów, a która dobrze oddaje większość z powyższych:


> Nie ufaj, weryfikuj.

Nawiązuje to do frazy "[ufaj, ale weryfikuj](https://en.wikipedia.org/wiki/Trust,_but_verify)", której były prezydent USA Ronald Reagan użył w kontekście rozbrojenia nuklearnego. [Bitcoiners](https://twitter.com/Truthcoin/status/1491415722123153408?s=20&t=ZyROxZxlBppdRpuuzsiF5w) zamienili je, aby podkreślić odrzucenie zaufania i znaczenie uruchomienia Full node.


To użytkownicy decydują, w jakim stopniu chcą zweryfikować oprogramowanie, którego używają i dane Blockchain, które otrzymują. Podobnie jak w przypadku wielu innych rzeczy w Bitcoin, istnieje kompromis między wygodą a brakiem zaufania. Prawie zawsze wygodniej jest korzystać z Wallet w porównaniu do uruchamiania Bitcoin Core na własnym sprzęcie. Ponieważ jednak oprogramowanie Bitcoin dojrzewa, a interfejsy użytkownika są ulepszane, z czasem powinno lepiej wspierać użytkowników, którzy chcą pracować nad brakiem zaufania. Ponadto, w miarę zdobywania przez użytkowników coraz większej wiedzy, powinni oni być w stanie stopniowo usuwać zaufanie z równania.


Niektórzy użytkownicy myślą kontradyktoryjnie i weryfikują większość aspektów uruchamianego oprogramowania. W rezultacie ograniczają potrzebę zaufania do absolutnego minimum, ponieważ muszą ufać tylko swojemu sprzętowi komputerowemu i systemowi operacyjnemu. W ten sposób pomagają również ludziom, którzy nie weryfikują swojego sprzętu tak dokładnie, podnosząc publicznie głos, aby ostrzec o wszelkich problemach, które mogą znaleźć. Dobrym tego przykładem jest [zdarzenie, które miało miejsce w 2018 r.] (https://bitcoincore.org/en/2018/09/20/notice/), kiedy ktoś odkrył błąd, który pozwalał górnikom na dwukrotne wydanie wyniku w tej samej transakcji:


> CVE-2018-17144, którego poprawka została wydana 18 września w Bitcoin Core w wersjach 0.16.3 i 0.17.0rc4, zawiera zarówno komponent Denial of Service, jak i krytyczną podatność na inflację. Pierwotnie został on zgłoszony kilku deweloperom pracującym nad Bitcoin Core, a także projektami obsługującymi inne kryptowaluty, w tym ABC i Unlimited, 17 września jako błąd związany wyłącznie z odmową usługi, jednak szybko ustaliliśmy, że błąd ten był również podatnością na inflację z tą samą przyczyną źródłową i poprawką.

W tym przypadku anonimowa osoba zgłosiła błąd, który okazał się znacznie gorszy, niż zgłaszający zdawał sobie sprawę. Podkreśla to fakt, że osoby weryfikujące kod często zgłaszają luki w zabezpieczeniach zamiast je wykorzystywać. Jest to korzystne dla tych, którzy nie są w stanie zweryfikować wszystkiego samodzielnie.


Jednak użytkownicy nie powinni ufać innym, że zapewnią im bezpieczeństwo, ale raczej powinni sami sprawdzać, kiedy tylko i cokolwiek mogą; w ten sposób pozostaje się tak suwerennym, jak to tylko możliwe i jak Bitcoin prosperuje. Im więcej oczu na oprogramowanie, tym mniejsze prawdopodobieństwo przedostania się złośliwego kodu i luk w zabezpieczeniach.


### Wnioski dotyczące nieufności



Protokół Bitcoin jest protokołem Trustless, ponieważ pozwala użytkownikom na interakcję z nim bez ufania stronie trzeciej. W praktyce jednak większość ludzi nie jest w stanie zweryfikować całego stosu oprogramowania i sprzętu, na którym uruchamiają Bitcoin. Wykwalifikowane osoby, które weryfikują oprogramowanie lub sprzęt, są w stanie ostrzec inne, mniej wykwalifikowane osoby, gdy znajdą złośliwy kod lub błędy.


Bez braku zaufania nie możemy mieć decentralizacji, ponieważ zaufanie nieuchronnie wiąże się z jakimś centralnym punktem władzy. Można zbudować zaufany system na systemie Trustless, ale nie można zbudować systemu Trustless na zaufanym systemie.


## Prywatność

<chapterId>1b960afe-0008-589b-b2f4-007d60d264c6</chapterId>



![](assets/privacy-banner.webp)


Ten rozdział dotyczy tego, jak zachować prywatne informacje finansowe dla siebie. Wyjaśnia, co oznacza prywatność w kontekście Bitcoin, dlaczego jest ważna i co oznacza stwierdzenie, że Bitcoin jest pseudonimowy. Analizuje również, w jaki sposób prywatne dane mogą wyciekać, zarówno On-Chain, jak i off-chain.


Następnie omówiono fakt, że bitcoiny powinny być zamienne, co oznacza, że można je wymieniać na dowolne inne bitcoiny, oraz w jaki sposób zamienność i prywatność idą w parze. Wreszcie, rozdział wprowadza pewne środki, które można podjąć, aby poprawić prywatność swoją i innych.


Bitcoin można opisać jako system pseudonimowy, w którym użytkownicy mają wiele pseudonimów w postaci kluczy publicznych. Na pierwszy rzut oka wygląda to na całkiem dobry sposób ochrony użytkowników przed identyfikacją, ale w rzeczywistości bardzo łatwo jest nieumyślnie ujawnić prywatne informacje finansowe.


### Co oznacza prywatność?



Prywatność może oznaczać różne rzeczy w różnych kontekstach. W Bitcoin ogólnie oznacza to, że użytkownicy nie muszą ujawniać swoich informacji finansowych innym osobom, chyba że zrobią to dobrowolnie.


Istnieje wiele sposobów, w jakie można ujawnić swoje prywatne informacje innym osobom, wiedząc o tym lub nie. Dane mogą wyciec z publicznego Blockchain lub w inny sposób, na przykład gdy złośliwi aktorzy przechwytują Twoją komunikację internetową.


### Dlaczego prywatność jest ważna?


Może wydawać się oczywiste, dlaczego prywatność jest ważna w Bitcoin, ale są pewne aspekty, o których można nie pomyśleć od razu. [Na forum Bitcoin Talk](https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908), Gregory Maxwell przedstawia nam wiele powodów, dla których uważa, że prywatność ma znaczenie. Wśród nich są wolny rynek, bezpieczeństwo i ludzka godność:


> Prywatność finansowa jest podstawowym kryterium skutecznego funkcjonowania wolnego rynku: jeśli prowadzisz firmę, nie możesz skutecznie ustalać cen, jeśli twoi dostawcy i klienci mogą zobaczyć wszystkie twoje transakcje wbrew twojej woli.
> Nie można skutecznie konkurować, jeśli konkurencja śledzi sprzedaż.  Jeśli nie masz prywatności nad swoimi kontami, tracisz możliwość korzystania z informacji w prywatnych transakcjach: jeśli płacisz swojemu wynajmującemu w Bitcoin bez wystarczającej prywatności, Twój wynajmujący zobaczy, kiedy otrzymałeś podwyżkę i będzie mógł zażądać od Ciebie wyższego czynszu.
>

> Prywatność finansowa jest niezbędna dla bezpieczeństwa osobistego: jeśli złodzieje widzą Twoje wydatki, dochody i stan posiadania, mogą wykorzystać te informacje, aby Cię namierzyć i wykorzystać. Bez prywatności złośliwe strony mają większe możliwości kradzieży tożsamości, podkradania dużych zakupów lub podszywania się pod firmy, z którymi przeprowadzasz transakcje... mogą dokładnie określić, na jaką kwotę próbują cię oszukać.
>

> Prywatność finansowa jest niezbędna dla ludzkiej godności: nikt nie chce, aby zasmarkany barista w kawiarni lub wścibscy sąsiedzi komentowali jego dochody lub nawyki związane z wydatkami. Nikt nie chce, by jego oszalali na punkcie dzieci teściowie pytali, dlaczego kupuje antykoncepcję (lub zabawki erotyczne). Twój pracodawca nie powinien wiedzieć, na jaki kościół przekazujesz datki. Tylko w doskonale oświeconym, wolnym od dyskryminacji świecie, w którym nikt nie ma nadmiernej władzy nad nikim innym, możemy zachować naszą godność i swobodnie dokonywać legalnych transakcji bez autocenzury, jeśli nie mamy prywatności.

Maxwell porusza również kwestię zamienności, która zostanie omówiona w dalszej części tego rozdziału, a także tego, w jaki sposób prywatność i egzekwowanie prawa nie są ze sobą sprzeczne.


### Pseudonimowość


Wspomnieliśmy powyżej, że Bitcoin jest pseudonimowy, a pseudonimy są kluczami publicznymi. W mediach często słyszy się, że Bitcoin jest anonimowy, co nie jest prawdą. Istnieje rozróżnienie między anonimowością a pseudonimowością.


Andrew Poelstra [wyjaśnia w poście Bitcoin Stack Exchange](https://Bitcoin.stackexchange.com/a/29473/69518), jak wyglądałaby anonimowość w transakcjach:


> Całkowita anonimowość, w tym sensie, że kiedy wydajesz pieniądze, nie ma śladu, skąd pochodzą ani dokąd zmierzają, jest teoretycznie możliwa dzięki zastosowaniu kryptograficznej techniki dowodów zerowej wiedzy.

Różnica wydaje się polegać na tym, że w pseudonimowej formie pieniądza można śledzić płatności między pseudonimami, podczas gdy w anonimowej formie pieniądza nie można. Ponieważ płatności Bitcoin można śledzić między pseudonimami, nie jest to system anonimowy.


Powiedzieliśmy również, że pseudonimy są kluczami publicznymi, ale w rzeczywistości są to adresy pochodzące z kluczy publicznych. Dlaczego używamy adresów jako pseudonimów, a nie czegoś innego, na przykład nazw opisowych, takich jak "watchme1984"? Zostało to [dobrze wyjaśnione](https://Bitcoin.stackexchange.com/a/25175/69518) przez użytkownika Tim S., również na Bitcoin Stack Exchange:


> Aby pomysł Bitcoin zadziałał, musisz mieć monety, które mogą być wydawane tylko przez właściciela danego klucza prywatnego. Oznacza to, że cokolwiek wysyłasz, musi być w jakiś sposób powiązane z kluczem publicznym.
>

> Używanie arbitralnych pseudonimów (np. nazw użytkowników) oznaczałoby, że musiałbyś w jakiś sposób powiązać pseudonim z kluczem publicznym, aby umożliwić kryptografię klucza publicznego/prywatnego. Usunęłoby to możliwość bezpiecznego tworzenia adresów/pseudonimów offline (np. zanim ktoś mógłby wysłać pieniądze na nazwę użytkownika "tdumidu", musiałbyś ogłosić w Blockchain, że "tdumidu" jest własnością klucza publicznego "a1c..." i dołączyć opłatę, aby inni mieli powód, by to ogłosić), zmniejszyłoby anonimowość (zachęcając do ponownego użycia pseudonimów) i niepotrzebnie zwiększyłoby rozmiar Blockchain. Stworzyłoby to również fałszywe poczucie bezpieczeństwa, że wysyłasz pieniądze do tego, kim myślisz, że jesteś (jeśli przyjmę nazwę "Linus Torvalds", zanim on to zrobi, to jest ona moja i ludzie mogą wysyłać pieniądze, myśląc, że płacą twórcy Linuksa, a nie mnie).

Używając adresów lub kluczy publicznych, osiągamy ważne cele, takie jak wyeliminowanie potrzeby wcześniejszej rejestracji pseudonimu, zmniejszenie zachęt do ponownego użycia pseudonimu, uniknięcie rozdęcia Blockchain i utrudnienie podszywania się pod inne osoby.


### Blockchain prywatność



Prywatność Blockchain odnosi się do informacji ujawnianych przez użytkownika podczas dokonywania transakcji na Blockchain. Dotyczy to wszystkich transakcji, zarówno tych wysyłanych, jak i otrzymywanych.


Satoshi Nakamoto zastanawia się nad prywatnością On-Chain w sekcji 7 swojego [Bitcoin whitepaper](https://Bitcoin.org/Bitcoin.pdf):


> Jako dodatkowa zapora ogniowa, dla każdej transakcji powinna być używana nowa para kluczy, aby zapobiec powiązaniu ich ze wspólnym właścicielem. Pewne powiązania są nadal nieuniknione w przypadku transakcji z wieloma wejściami, które z konieczności ujawniają, że ich wejścia należały do tego samego właściciela. Ryzyko polega na tym, że jeśli właściciel klucza zostanie ujawniony, powiązanie może ujawnić inne transakcje, które należały do tego samego właściciela.

Artykuł podsumowuje główne problemy prywatności Blockchain, a mianowicie ponowne wykorzystanie Address i grupowanie Address. Pierwszy z nich jest oczywisty, a drugi odnosi się do możliwości podjęcia decyzji, z pewnym poziomem pewności, że zestaw różnych adresów należy do tego samego użytkownika.


![](assets/address-reuse-clustering.webp)


Typowe wycieki prywatności na Blockchain


Chris Belcher [napisał bardzo szczegółowo](https://en.Bitcoin.it/Privacy#Blockchain_attacks_on_privacy) o różnych rodzajach wycieków prywatności, które mogą się zdarzyć na Bitcoin Blockchain. Zalecamy przeczytanie przynajmniej kilku pierwszych podrozdziałów w sekcji "Ataki Blockchain na prywatność"


Wniosek jest taki, że prywatność w Bitcoin nie jest idealna. Prywatne transakcje wymagają znacznego nakładu pracy. Większość ludzi nie jest gotowa posunąć się tak daleko dla prywatności. Wydaje się, że istnieje wyraźny kompromis między prywatnością a użytecznością.


Innym ważnym aspektem prywatności jest to, że środki podejmowane w celu ochrony własnej prywatności wpływają również na innych użytkowników. Jeśli jesteś niedbały o własną prywatność, inni ludzie również mogą doświadczyć ograniczenia prywatności. Gregory Maxwell wyjaśnia to bardzo jasno w tej samej dyskusji Bitcoin Talk [do której link zamieściliśmy powyżej] (https://bitcointalk.org/index.php?topic=334316.msg3589252#msg3589252) i kończy przykładem:


> Działa to również w praktyce... Miły haker whitehat na IRC bawił się łamaniem brainwalletów i trafił na frazę z ~250 BTC w środku.  Byliśmy w stanie zidentyfikować właściciela na podstawie samego Address, ponieważ został opłacony przez usługę Bitcoin, która ponownie wykorzystywała adresy, a on był w stanie namówić ich do podania danych kontaktowych użytkowników. Użytkownik był zszokowany i zdezorientowany, ale wdzięczny, że nie stracił swoich pieniędzy.  Szczęśliwe zakończenie. (Nie jest to jedyny taki przykład, ale jeden z bardziej zabawnych).

W tym przypadku wszystko poszło dobrze dzięki filantropijnie nastawionemu hakerowi, ale nie licz na to następnym razem.


### Prywatność inna niż Blockchain


Podczas gdy Blockchain okazuje się być znanym źródłem wycieków prywatności, istnieje wiele innych wycieków, które nie wykorzystują Blockchain, niektóre bardziej podstępne niż inne. Obejmują one od rejestratorów kluczy po analizę ruchu sieciowego. Aby zapoznać się z niektórymi z tych metod, należy ponownie zapoznać się z artykułem [Chrisa Belchera] (https://en.Bitcoin.it/Privacy#Non-blockchain_attacks_on_privacy), a konkretnie z sekcją "Ataki na prywatność inne niż Blockchain".


Wśród wielu ataków Belcher wymienia możliwość szpiegowania przez kogoś połączenia internetowego, na przykład przez dostawcę usług internetowych:


> Jeśli przeciwnik zobaczy transakcję lub blok wychodzący z węzła, który wcześniej nie został wprowadzony, może wiedzieć z niemal całkowitą pewnością, że transakcja została dokonana przez użytkownika lub blok został wydobyty przez użytkownika. Ponieważ w grę wchodzą połączenia internetowe, przeciwnik będzie w stanie połączyć adres IP Address z odkrytymi informacjami Bitcoin.

Jednak jednym z najbardziej oczywistych wycieków prywatności są giełdy. Ze względu na przepisy, zwykle określane jako KYC (Know Your Customer) i AML (Anti-Money Laundering), które obowiązują w jurysdykcjach, w których działają, giełdy i powiązane z nimi firmy często muszą gromadzić dane osobowe swoich użytkowników, tworząc duże bazy danych o tym, którzy użytkownicy posiadają jakie bitcoiny. Te bazy danych są świetnymi honeypotami dla złych rządów i przestępców, którzy zawsze szukają nowych ofiar. Istnieją rzeczywiste rynki dla tego rodzaju danych, na których hakerzy

sprzedać dane oferentowi, który zaoferuje najwyższą cenę.


Co gorsza, firmy zarządzające tymi bazami danych często mają niewielkie doświadczenie w ochronie danych finansowych, w rzeczywistości wiele z nich to młode start-upy i wiemy na pewno, że doszło już do kilku wycieków. Kilka przykładów to

[MobiQwik z siedzibą w Indiach](https://bitcoinmagazine.com/business/probably-the-largest-kyc-data-leak-in-history-demonstrates-the-importance-of-Bitcoin-privacy) i [HubSpot](https://bitcoinmagazine.com/business/hubspot-security-breach-leaks-Bitcoin-users-data).


Ponownie, ochrona danych przed tak szerokim zakresem ataków to Hard i jest prawdopodobne, że nie będziesz w stanie tego w pełni zrobić. Będziesz musiał wybrać kompromis między wygodą a prywatnością, który będzie dla Ciebie najlepszy.


### Grzybiczość


Zamienność, w kontekście walut, oznacza, że jedna moneta jest wymienna na każdą inną monetę tej samej waluty. To zabawne

słowo to zostało pokrótce omówione wcześniej w tym rozdziale.


W omawianym tam artykule Gregory Maxwell [stwierdził] (https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908):


> Prywatność finansowa jest istotnym elementem zamienności w Bitcoin: jeśli można w znaczący sposób odróżnić jedną monetę od drugiej, to ich zamienność jest słaba. Jeśli nasza zamienność jest zbyt słaba w praktyce, nie możemy być zdecentralizowani: jeśli ktoś ważny ogłosi listę skradzionych monet, z których nie będzie akceptował monet pochodnych, musisz dokładnie sprawdzić monety, które akceptujesz, w odniesieniu do tej listy i zwrócić te, które zawiodą.  Wszyscy utknęli w sprawdzaniu czarnych list wydanych przez różne władze, ponieważ w tym świecie wszyscy nie chcielibyśmy utknąć ze złymi monetami. Zwiększa to tarcie i koszty transakcyjne oraz sprawia, że Bitcoin jest mniej wartościowy jako pieniądz.

Tutaj mówi o zagrożeniach wynikających z braku zamienności. Załóżmy, że masz UTXO. Historię tego UTXO można zwykle prześledzić kilka razy wstecz, rozchodząc się do wielu poprzednich wyjść. Jeśli którekolwiek z tych wyjść było zaangażowane w jakąkolwiek nielegalną, niechcianą lub podejrzaną działalność, niektórzy potencjalni odbiorcy Twojej monety mogą ją odrzucić. Jeśli uważasz, że twoi odbiorcy zweryfikują twoje monety na jakiejś scentralizowanej białej lub czarnej liście, możesz zacząć sprawdzać monety, które otrzymujesz, aby być po bezpiecznej stronie. W rezultacie zła zamienność wzmocni jeszcze gorszą zamienność.


Adam Back i Matt Corallo [przedstawili prezentację na temat zamienności](https://btctranscripts.com/scalingbitcoin/milan-2016/fungibility-overview/) podczas Scaling Bitcoin w Mediolanie w 2016 roku. Myśleli w ten sam sposób:


> Do funkcjonowania Bitcoin potrzebna jest zamienność. Jeśli otrzymujesz monety i nie możesz ich wydać, zaczynasz wątpić, czy możesz je wydać. Jeśli pojawią się wątpliwości co do otrzymanych monet, ludzie będą odwiedzać serwisy taint i sprawdzać, czy "te monety są błogosławione", a następnie odmówią handlu. Powoduje to przejście Bitcoin ze zdecentralizowanego systemu bez zezwoleń do scentralizowanego systemu z zezwoleniami, w którym masz "IOU" od dostawców czarnej listy.

Wydaje się, że prywatność i zamienność idą w parze. Zamienialność osłabnie, jeśli prywatność będzie słaba, na przykład monety od niechcianych osób mogą trafić na czarną listę. W ten sam sposób prywatność osłabnie, jeśli zamienność będzie słaba: jeśli istnieje czarna lista, będziesz musiał zapytać dostawców czarnej listy o to, które monety zaakceptować, tym samym prawdopodobnie ujawniając swój adres IP Address, e-mail Address i inne poufne informacje. Te dwie cechy są ze sobą tak powiązane, że Hard nie może mówić o żadnej z nich w oderwaniu od siebie.


### Środki ochrony prywatności



Opracowano kilka technik, które mają pomóc ludziom chronić się przed wyciekami prywatności. Wśród najbardziej oczywistych jest, jak zauważył wcześniej Nakamoto, używanie unikalnych

adresów dla każdej transakcji, ale istnieje kilka innych. Nie zamierzamy uczyć Cię, jak zostać ninja prywatności. Jednak Bitcoin Q+A zawiera [szybkie podsumowanie technologii zwiększających prywatność] (https://bitcoiner.guide/privacytips/), nieco uporządkowane według tego, jak należy je wdrożyć w Hard. Kiedy go przeczytasz, zauważysz, że prywatność Bitcoin często ma związek z rzeczami spoza Bitcoin. Na przykład, nie powinieneś chwalić się swoimi bitcoinami i powinieneś używać Tora i VPN.


W poście wymieniono również niektóre środki bezpośrednio związane z Bitcoin:


- Full node: Jeśli nie korzystasz z własnego Full node, wycieknie wiele informacji o twoim Wallet do serwerów w Internecie. Uruchomienie Full node to świetny pierwszy krok.
- Lightning Network: Istnieje kilka protokołów opartych na Bitcoin, na przykład Lightning Network i Liquid Sidechain firmy Blockstream.
- CoinJoin: Sposób na łączenie transakcji wielu osób w jedną, co utrudnia analizę łańcucha.


W [wystąpieniu](https://btctranscripts.com/breaking-Bitcoin/2019/breaking-Bitcoin-privacy/) na konferencji Breaking Bitcoin Chris Belcher podał interesujący praktyczny przykład tego, jak poprawiono prywatność:


> Było to kasyno Bitcoin. Hazard online nie jest dozwolony w USA. Wszyscy klienci Coinbase, którzy dokonali wpłaty bezpośrednio do Bustabit, mieliby zamknięte konta, ponieważ Coinbase monitorował to. Bustabit zrobił kilka rzeczy. Zrobili coś, co nazywa się unikaniem zmiany, gdzie przechodzisz i sprawdzasz, czy możesz skonstruować transakcję, która nie ma wyjścia zmiany. Oszczędza to opłaty Miner, a także utrudnia analizę.
>

> Ponadto zaimportowali swoje często używane adresy depozytowe do joinmarket. W tym momencie klienci coinbase.com nigdy nie zostali zbanowani. Wygląda na to, że usługa nadzoru Coinbase nie była w stanie przeprowadzić analizy po tym, więc możliwe jest złamanie tych algorytmów.

Wspomniał również o tym przykładzie, między innymi, na [stronie prywatności](https://en.Bitcoin.it/Privacy) na wiki Bitcoin.


Zwróć uwagę, jak lepszą prywatność można osiągnąć, budując systemy na Bitcoin, tak jak ma to miejsce w przypadku Lightning Network:


![image](assets/privacy.webp)


Warstwy na wierzchu Bitcoin mogą zwiększyć prywatność


Zauważyliśmy w ostatnim artykule, że potrzeba zaufania może wzrosnąć tylko z warstwami na wierzchu, ale nie wydaje się, aby dotyczyło to prywatności, którą można poprawić lub pogorszyć arbitralnie w warstwach na wierzchu. Dlaczego tak jest? Każdy Layer na Bitcoin, jak wyjaśniono w akapicie Skalowanie warstwowe w przyszłym rozdziale Skalowanie, musi od czasu do czasu korzystać z transakcji On-Chain, w przeciwnym razie nie byłby "na Bitcoin". Warstwy zwiększające prywatność zazwyczaj starają się używać podstawowego Layer w jak najmniejszym stopniu, aby zminimalizować ilość ujawnianych informacji.


Powyższe są nieco technicznymi sposobami na poprawę prywatności. Istnieją jednak inne sposoby. Na początku tego rozdziału powiedzieliśmy, że Bitcoin jest systemem pseudonimowym. Oznacza to, że użytkownicy Bitcoin nie są znani z prawdziwych nazwisk lub innych danych osobowych, ale z kluczy publicznych. Klucz publiczny jest pseudonimem użytkownika, a użytkownik może mieć wiele pseudonimów. W idealnym świecie tożsamość osobista jest oddzielona od pseudonimów Bitcoin. Niestety, ze względu na problemy z prywatnością opisane w tym rozdziale, to oddzielenie zwykle z czasem ulega pogorszeniu.


Aby zminimalizować ryzyko ujawnienia danych osobowych, nie należy ich podawać ani przekazywać scentralizowanym usługom, które tworzą duże bazy danych, które mogą wyciekać. Artykuł Bitcoin Q+A [wyjaśnia KYC](https://bitcoiner.guide/nokyconly/) i wynikające z niego zagrożenia. Sugeruje również pewne kroki, które można podjąć, aby poprawić swoją sytuację:


> Na szczęście istnieją pewne opcje zakupu Bitcoin za pośrednictwem źródeł bez KYC. Są to wszystkie giełdy P2P (peer to peer), na których handlujesz bezpośrednio z inną osobą, a nie ze scentralizowaną stroną trzecią. Niestety, niektóre z nich sprzedają inne monety, a także Bitcoin, dlatego zalecamy ostrożność.

Artykuł sugeruje, aby unikać korzystania z giełd, które wymagają KYC/AML i zamiast tego handlować prywatnie lub korzystać ze zdecentralizowanych giełd, takich jak [bisq](https://bisq.network/).


https://planb.network/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04

Więcej informacji na temat środków zaradczych można znaleźć we wcześniej wspomnianym [artykule wiki na temat prywatności] (https://en.Bitcoin.it/wiki/Privacy#Methods_for_improving_privacy_.28non-Blockchain.29), zaczynając od "Metod poprawy prywatności (nie-Blockchain)".


### Wnioski dotyczące prywatności



Prywatność jest bardzo ważna, ale Hard do osiągnięcia. Nie ma srebrnej kuli prywatności.


Aby uzyskać przyzwoitą prywatność w Bitcoin, trzeba podjąć aktywne działania, z których niektóre są kosztowne i czasochłonne.


## Finite Supply

<chapterId>af125ba2-ef98-5905-8895-41a538fe5ea5</chapterId>



![](assets/finitesupply-banner.webp)


W tym rozdziale przyjrzymy się limitowi Bitcoin Supply wynoszącemu 21 milionów BTC, czyli ile tak naprawdę wynosi? Mówimy o tym, jak ten limit jest egzekwowany i co można zrobić, aby sprawdzić, czy jest on przestrzegany. Ponadto zaglądamy do kryształowej kuli i omawiamy dynamikę, która wejdzie w grę, gdy Block reward zmieni się z opartego na dotacjach na oparty na opłatach.


Dobrze znany skończony Supply w wysokości 21 milionów BTC jest uważany za fundamentalną właściwość Bitcoin. Ale czy naprawdę jest ona ustalona?


Zacznijmy od przyjrzenia się temu, co obecne zasady konsensusu mówią o Supply z Bitcoin i ile z nich będzie faktycznie użytecznych. Pieter Wuille napisał o tym artykuł [na stosie Exchange] (https://Bitcoin.stackexchange.com/a/38998/69518), w którym policzył, ile bitcoinów będzie dostępnych po wydobyciu wszystkich monet:


> Po zsumowaniu wszystkich tych liczb otrzymujemy 20999999.9769 BTC.

Jednak z wielu powodów - takich jak wczesne problemy z transakcjami coinbase, górnicy, którzy nieumyślnie pobierają mniej niż dozwolone, oraz utrata kluczy prywatnych - ten górny limit nigdy nie zostanie osiągnięty. Wuille podsumowuje:


> To pozostawia nam 20999817.31308491 BTC (biorąc pod uwagę wszystko do bloku 528333)

Jednak różne portfele zostały zgubione lub skradzione, transakcje zostały wysłane do niewłaściwego Address, ludzie zapomnieli, że posiadają Bitcoin. Suma tych strat może sięgać milionów. Ludzie próbowali podliczyć znane straty [tutaj] (https://bitcointalk.org/index.php?topic=7253.0).


To pozostawia nas z: ??? BTC.


Możemy więc być pewni, że Bitcoin Supply będzie co najwyżej 20999817.31308491 BTC. Wszelkie utracone lub nieweryfikowalnie spalone monety sprawią, że liczba ta będzie niższa, ale nie wiemy o ile. Interesujące jest to, że tak naprawdę nie ma to znaczenia, a nawet więcej, ma to znaczenie w pozytywny sposób dla posiadaczy Bitcoin,

[jak wyjaśniono](https://bitcointalk.org/index.php?topic=198.msg1647#msg1647) przez Satoshi Nakamoto:


> Utracone monety tylko nieznacznie zwiększają wartość monet innych graczy.  Potraktuj to jako darowiznę dla wszystkich.

Skończona Supply będzie się kurczyć, co powinno, przynajmniej teoretycznie, spowodować deflację cen.


Ważniejszy od dokładnej liczby monet w obiegu jest sposób, w jaki limit Supply jest egzekwowany bez żadnego centralnego organu. Alias chytrik dobrze to ujął na [Stack Exchange] (https://Bitcoin.stackexchange.com/a/106830/69518):


> Odpowiedź jest więc taka, że nie musisz ufać komuś, że nie zwiększy Supply. Wystarczy uruchomić kod, który sprawdzi, czy tego nie zrobił.

Nawet jeśli niektóre pełne węzły przejdą na ciemną stronę i zdecydują się zaakceptować bloki z transakcjami coinbase o wyższej wartości, wszystkie pozostałe pełne węzły po prostu je zignorują i będą kontynuować działalność jak zwykle. Niektóre pełne węzły mogą, celowo lub nieumyślnie, uruchamiać złe oprogramowanie, ale kolektyw będzie solidnie zabezpieczał Blockchain. Podsumowując, możesz zaufać systemowi bez konieczności ufania komukolwiek.


### Subwencja blokowa i opłaty transakcyjne



Block reward składa się z dotacji blokowej oraz opłat transakcyjnych. Block reward musi pokryć koszty bezpieczeństwa Bitcoin. Możemy z całą pewnością stwierdzić, że w dzisiejszych warunkach w odniesieniu do dotacji blokowej, opłat transakcyjnych, ceny Bitcoin, wielkości Mempool, mocy Hash, stopnia decentralizacji itp. zachęty dla każdego gracza do gry zgodnie z zasadami są wystarczająco wysokie, aby zachować bezpieczny system monetarny.


Co się dzieje, gdy subsydium blokowe zbliża się do zera? Aby zachować prostotę, załóżmy, że faktycznie wynosi ona zero. W tym momencie koszt bezpieczeństwa systemu jest pokrywany wyłącznie z opłat transakcyjnych. Nie możemy wiedzieć, co przyniesie nam przyszłość, gdy tak się stanie. Czynniki niepewności są liczne i jesteśmy zdani na spekulacje. Na przykład wkład Paula Sztorca w ten temat [na jego blogu Truthcoin] (https://www.truthcoin.info/blog/security-budget/) to głównie spekulacje, ale ma on co najmniej jeden solidny punkt (należy pamiętać, że M2, o którym mówi Sztorc, jest miarą pieniądza fiducjarnego Supply):


> Podczas gdy oba są mieszane w tym samym "budżecie bezpieczeństwa", dotacja blokowa i opłaty txn są całkowicie i całkowicie różne. Różnią się od siebie tak bardzo, jak "całkowite zyski VISA w 2017 r." różnią się od "całkowitego wzrostu M2 w 2017 r.".

Dziś to posiadacze płacą za bezpieczeństwo (poprzez inflację monetarną). Jutro przyjdzie kolej na wydawców, którzy w jakiś sposób wezmą na siebie ten ciężar, jak pokazano poniżej.


![image](assets/finitesupply.webp)


W miarę upływu czasu ponoszenie kosztów bezpieczeństwa przesunie się z posiadaczy na wydawców


Gdy opłaty transakcyjne są główną motywacją dla Mining, zachęty ulegają zmianie. W szczególności, jeśli Mempool Miner nie zawiera wystarczającej ilości opłat transakcyjnych, może stać się bardziej opłacalne dla tego Miner, aby przepisać historię Bitcoin zamiast ją rozszerzać. Bitcoin Optech ma specjalną [sekcję na temat tego zachowania] (https://bitcoinops.org/en/topics/fee-sniping/), zwaną *fee sniping*, napisaną przez Davida Hardinga:


> Fee sniping to problem, który może się pojawić, gdy dotacja Bitcoin będzie się zmniejszać, a opłaty transakcyjne zaczną dominować w nagrodach za bloki Bitcoin. Jeśli opłaty transakcyjne są wszystkim, co ma znaczenie, to Miner z `x` procentem stawki Hash ma `x` procent szans na Mining w następnym bloku, więc oczekiwana wartość dla nich uczciwego Mining wynosi `x` procent [najlepszego zestawu transakcji] (https://bitcoinops.org/en/newsletters/2021/06/02/#candidate-set-based-csb-block-template-construction) w ich Mempool.
>

> Alternatywnie, Miner może nieuczciwie próbować ponownie wydobyć poprzedni blok plus całkowicie nowy blok, aby przedłużyć łańcuch. Takie zachowanie jest określane jako fee sniping, a szansa na sukces nieuczciwego Miner, jeśli każdy inny Miner jest uczciwy, wynosi `(x/(1-x))^2`. Pomimo tego, że fee sniping ma ogólnie niższe prawdopodobieństwo sukcesu niż uczciwy Mining, próba nieuczciwego Mining może być bardziej opłacalnym wyborem, jeśli transakcje w poprzednim bloku zapłaciły znacznie wyższe stawki niż transakcje obecnie w Mempool - mała szansa na dużą kwotę może być warta więcej niż duża szansa na małą kwotę.

Naszą nadzieję na przyszłość przekreśla fakt, że jeśli górnicy zaczną snajperować, zachęci to innych do robienia tego samego, pozostawiając jeszcze mniej uczciwych górników. Może to poważnie pogorszyć ogólne bezpieczeństwo Bitcoin. Harding wymienia kilka środków zaradczych, które można podjąć, takich jak poleganie na blokadach czasu transakcji w celu ograniczenia miejsca, w którym w Blockchain może pojawić się transakcja.


Tak więc, biorąc pod uwagę, że konsensus w sprawie skończonego Supply pozostaje, dotacja blokowa - dzięki [BIP42](https://github.com/Bitcoin/bips/blob/master/bip-0042.mediawiki), który naprawił bardzo długoterminowy błąd inflacji - osiągnie zero około roku 2140. Czy opłaty transakcyjne będą wystarczające, aby zabezpieczyć sieć?


Nie da się tego stwierdzić, ale wiemy kilka rzeczy:


- Stulecie to *długi* czas z perspektywy Bitcoin. Jeśli nadal istnieje, prawdopodobnie przeszedł ogromną ewolucję.
- Jeśli przytłaczająca większość ekonomiczna uzna za konieczne zmienić zasady i wprowadzić na przykład wieczną roczną inflację monetarną w wysokości 0,1% lub 1%, Supply z Bitcoin nie będzie już skończony.
- Przy zerowej dotacji blokowej i pustym lub prawie pustym Mempool sytuacja może stać się chwiejna z powodu snipowania opłat.


Ponieważ przejście do Block reward opartego wyłącznie na opłatach jest tak odległą przyszłością, rozsądnie byłoby nie wyciągać pochopnych wniosków i spróbować naprawić potencjalne problemy, póki jeszcze możemy. Na przykład Peter Todd uważa, że istnieje rzeczywiste ryzyko, że budżet bezpieczeństwa Bitcoin nie będzie wystarczający w przyszłości, a co za tym idzie, opowiada się za niewielką wieczną inflacją w Bitcoin. Jednak uważa on również, że nie jest dobrym pomysłem omawianie takiej kwestii w tej chwili, jak [powiedział w podcaście What Bitcoin Did] (https://www.whatbitcoindid.com/podcast/peter-todd-on-the-essence-of-Bitcoin):


> Jest to jednak ryzyko sięgające 10, 20 lat w przyszłość. To bardzo długi okres. A do tego czasu, kto do cholery wie, jakie jest ryzyko?

Być może moglibyśmy myśleć o Bitcoin jak o czymś organicznym. Wyobraźmy sobie mały, powoli rosnący dąb. Wyobraź sobie również, że nigdy w życiu nie widziałeś w pełni rozwiniętego drzewa. Czy nie byłoby mądrze ograniczyć kontrolę zamiast ustalać z góry wszystkie zasady dotyczące tego, jak ta roślina powinna ewoluować i rosnąć?


### Wnioski dotyczące Supply



Czy Bitcoin Supply wzrośnie powyżej 21 milionów, nie możemy dziś powiedzieć, a to prawdopodobnie nie jest takie złe. Zapewnienie, że budżet bezpieczeństwa pozostanie wystarczająco wysoki, jest kluczowe, ale nie pilne. Porozmawiajmy o tym za 10-50 lat, kiedy będziemy wiedzieć więcej. Jeśli nadal będzie to istotne.


# Bitcoin Gouvernance

<partId>411bf53f-af4b-50f1-b71b-e40fe3ff64b7</partId>


## Aktualizacja

<chapterId>3ffa84d1-adfa-5fbc-9b13-384ea783fcdd</chapterId>



![](assets/upgrading-banner.webp)


Bezpieczna aktualizacja Bitcoin może być niezwykle trudna. Wprowadzenie niektórych zmian zajmuje kilka lat. W tym rozdziale zapoznamy się z powszechnym słownictwem dotyczącym aktualizacji Bitcoin i przeanalizujemy kilka przykładów historycznych aktualizacji jego protokołu, a także spostrzeżenia, które z nich uzyskaliśmy. Na koniec omawiamy podziały łańcucha oraz związane z nimi ryzyko i koszty.


Aby dobrze przygotować się do tego rozdziału, należy przeczytać [artykuł Davida Hardinga na temat harmonii i dysonansu] (https://bitcointalk.org/dec/p1.html):


> Eksperci Bitcoin często mówią o konsensusie, którego znaczenie jest abstrakcyjne i Hard trudne do ustalenia. Ale słowo konsensus wyewoluowało z łacińskiego słowa concentus, "śpiewająca razem harmonia", więc nie mówmy o Bitcoin konsensusie, ale o Bitcoin harmonii.
>

> Harmonia jest tym, co sprawia, że Bitcoin działa. Tysiące pełnych węzłów pracują niezależnie, aby zweryfikować poprawność otrzymywanych transakcji, tworząc harmonijne porozumienie co do stanu Bitcoin Ledger, bez konieczności ufania komukolwiek innemu przez operatora węzła. Przypomina to chór, w którym każdy członek śpiewa tę samą piosenkę w tym samym czasie, tworząc coś o wiele piękniejszego, niż każdy z nich mógłby stworzyć sam.
>

> Rezultatem harmonii Bitcoin jest system, w którym bitcoiny są bezpieczne nie tylko przed drobnymi złodziejami (pod warunkiem, że trzymasz klucze w bezpiecznym miejscu), ale także przed niekończącą się inflacją, masową lub ukierunkowaną konfiskatą lub po prostu biurokratycznym gąszczem, jakim jest dotychczasowy system finansowy.

W tym rozdziale omówiono, w jaki sposób można zaktualizować Bitcoin bez wywoływania niezgody. Zachowanie harmonii, tj. utrzymanie konsensusu, jest rzeczywiście jednym z największych wyzwań w rozwoju Bitcoin. Istnieje wiele niuansów w mechanizmach aktualizacji, które można najlepiej zrozumieć, studiując rzeczywiste przypadki poprzednich aktualizacji. Z tego powodu rozdział ten kładzie duży nacisk na przykłady historyczne i rozpoczyna się od wprowadzenia przydatnego słownictwa.


### Słownictwo



Według Wikipedii [kompatybilność w przód] (https://en.wikipedia.org/wiki/Forward_compatibility) odnosi się do stanu, w którym stare oprogramowanie może przetwarzać dane utworzone przez nowsze oprogramowanie, ignorując części, których nie rozumie:


Standard wspiera kompatybilność w przód, jeśli produkt zgodny z wcześniejszymi wersjami może "z wdziękiem" przetwarzać dane wejściowe zaprojektowane dla późniejszych wersji standardu, ignorując nowe części, których nie rozumie.


I odwrotnie, [kompatybilność wsteczna] (https://en.wikipedia.org/wiki/Backward_compatibility) odnosi się do sytuacji, gdy dane ze starego oprogramowania można wykorzystać w nowszym oprogramowaniu. Mówi się, że zmiana jest w pełni kompatybilna, jeśli jest kompatybilna zarówno do przodu, jak i wstecz.


Zmiana zasad konsensusu Bitcoin jest określana jako * Soft Fork*, jeśli jest w pełni kompatybilna. Jest to najczęstszy sposób aktualizacji Bitcoin z wielu powodów, które omówimy w dalszej części tego rozdziału. Jeśli zmiana reguł konsensusu Bitcoin jest kompatybilna wstecz, ale nie jest kompatybilna do przodu, nazywana jest * Hard Fork*.


Aby zapoznać się z technicznym przeglądem forków Soft i Hard, przeczytaj [rozdział 11 Grokking Bitcoin] (https://rosenbaum.se/book/grokking-Bitcoin-11.html). Wyjaśnia on te terminy, a także zagłębia się w mechanizmy aktualizacji. Zaleca się, choć nie jest to absolutnie konieczne, zapoznanie się z tym przed kontynuowaniem czytania.


### Historyczne aktualizacje



Bitcoin nie jest dziś taki sam, jak w momencie tworzenia bloku Genesis. Na przestrzeni lat dokonano kilku aktualizacji. W 2018 r. Eric Lombrozo [przemawiał na konferencji Breaking Bitcoin] (https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) o różnych mechanizmach aktualizacji Bitcoin, wskazując, jak bardzo ewoluowały one w czasie. Wyjaśnił nawet, w jaki sposób Satoshi Nakamoto zaktualizował Bitcoin poprzez Hard Fork:


> W rzeczywistości było Hard-Fork w Bitcoin, które Satoshi zrobiło, że nigdy nie zrobilibyśmy tego w ten sposób - to dość zły sposób na zrobienie tego. Jeśli spojrzysz na opis commitu git tutaj [[757f076](https://github.com/Bitcoin/Bitcoin/commit/757f0769d8360ea043f469f3a35f6ec204740446)], on mówi coś o przywróconym makefile.unix wx-config w wersji 0.3.6. Racja. To wszystko, co mówi. Nic nie wskazuje na to, że w ogóle wprowadzono przełomową zmianę. Zasadniczo ukrył ją tam. Napisał również [post na bitcointalk](https://bitcointalk.org/index.php?topic=626.msg6451#msg6451) i powiedział, że prosimy o jak najszybszą aktualizację do wersji 0.3.6. Naprawiliśmy błąd w implementacji, przez który fałszywe transakcje mogą być wyświetlane jako zaakceptowane. Nie akceptuj płatności Bitcoin do czasu aktualizacji do wersji 0.3.6. Jeśli nie możesz dokonać aktualizacji od razu, najlepiej będzie wyłączyć węzeł Bitcoin do czasu aktualizacji. A na dodatek, nie wiem dlaczego zdecydował się to zrobić, postanowił dodać kilka optymalizacji w tym samym kodzie. Naprawić błąd i dodać kilka optymalizacji.

Zwraca on uwagę, że czy to celowo, czy nie, ten Hard Fork stworzył możliwości dla przyszłych forków Soft, a mianowicie operatorów skryptowych (opcodes) OP_NOP1-OP_NOP10. Przyjrzymy się bliżej tej zmianie kodu w cve-2010-5141. Te kody operacyjne były dotychczas używane w dwóch forkach Soft:


- [BIP65](https://github.com/Bitcoin/bips/blob/master/bip-0065.mediawiki) (OP_CHECKLOCKTIMEVERIFY)
- [BIP113](https://github.com/Bitcoin/bips/blob/master/bip-0112.mediawiki) (OP_SEQUENCEVERIFY).


Lombrozo przedstawia również przegląd sposobu, w jaki mechanizmy aktualizacji ewoluowały na przestrzeni lat, aż do 2017 roku. Od tego czasu wdrożono tylko jedną dużą aktualizację, Taproot. Długi i nieco chaotyczny proces, który doprowadził do jego aktywacji, pomógł nam uzyskać dalszy wgląd w mechanizmy aktualizacji Bitcoin.


#### Aktualizacja SegWit



Podczas gdy wszystkie aktualizacje poprzedzające SegWit były mniej lub bardziej bezbolesne, ta była inna. Kiedy kod aktywacyjny SegWit został wydany w październiku 2016 r., wydawało się, że użytkownicy Bitcoin mają dla niego ogromne poparcie, ale z jakiegoś powodu górnicy nie zasygnalizowali wsparcia dla tej aktualizacji, co opóźniło aktywację bez widocznego rozwiązania.


Aaron van Wirdum opisuje tę krętą drogę w swoim artykule w Bitcoin Magazine [The Long Road To SegWit] (https://bitcoinmagazine.com/technical/the-long-road-to-SegWit-how-bitcoins-biggest-protocol-upgrade-became-reality). Zaczyna od wyjaśnienia, czym jest SegWit i w jaki sposób nawiązuje do debaty na temat rozmiaru bloku. Następnie Van Wirdum nakreśla przebieg wydarzeń, które doprowadziły do jego ostatecznej aktywacji. W centrum tego procesu znajdował się mechanizm aktualizacji o nazwie *user activated Soft Fork*, w skrócie UASF, który został zaproponowany przez użytkownika Shaolinfry:


> Shaolinfry zaproponował alternatywę: aktywowany przez użytkownika Soft Fork (UASF). Zamiast aktywacji mocy Hash, aktywowany przez użytkownika Soft Fork miałby "aktywację dnia flagi", w której węzły rozpoczynałyby egzekwowanie w określonym czasie w przyszłości" Dopóki taka UASF jest egzekwowana przez większość ekonomiczną, powinno to zmusić większość górników do przestrzegania (lub aktywacji) Soft Fork.

Cytuje on między innymi e-mail Shaolinfry'ego do listy mailingowej Bitcoin-dev. Przy tej okazji Shaolinfry [argumentował przeciwko forkom Miner aktywowanym Soft](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-February/013643.html), wymieniając szereg problemów z nimi związanych:


> Po pierwsze, wymaga to zaufania, że moc Hash zostanie zatwierdzona po aktywacji.  BIP66 Soft Fork był przypadkiem, w którym 95% Hashrate sygnalizowało gotowość, ale w rzeczywistości około połowa nie walidowała zaktualizowanych reguł i przez pomyłkę wydobywała nieważny blok.
>

> Po drugie, sygnalizacja Miner ma naturalne weto, które pozwala niewielkiemu procentowi Hashrate zawetować aktywację węzła aktualizacji dla wszystkich. Do tej pory forki Soft wykorzystywały względnie scentralizowany krajobraz Mining, w którym istnieje stosunkowo niewiele pul Mining budujących ważne bloki; w miarę jak zmierzamy w kierunku większej decentralizacji Hashrate, jest prawdopodobne, że będziemy coraz bardziej cierpieć z powodu "bezwładności aktualizacji", która zawetuje większość aktualizacji.

Shaolinfry zwrócił również uwagę na powszechną błędną interpretację sygnalizacji Miner: ludzie ogólnie uważali, że jest to środek, za pomocą którego górnicy mogą decydować o aktualizacjach protokołu, a nie działanie, które pomaga koordynować aktualizacje. Z powodu tego nieporozumienia górnicy mogli również czuć się zobowiązani do publicznego głoszenia swoich poglądów na temat określonego Soft Fork, tak jakby nadawało to wagę propozycji.


Propozycja UASF to, w skrócie, "dzień flagi", w którym węzły zaczynają egzekwować określone nowe zasady. W ten sposób górnicy nie muszą podejmować wspólnych wysiłków w celu skoordynowania aktualizacji, ale *mogą* uruchomić aktywację wcześniej niż w dniu flagi, jeśli wystarczająca liczba bloków zasygnalizuje wsparcie:


> Moja sugestia jest taka, aby uzyskać to, co najlepsze z obu światów. Ponieważ aktywowany przez użytkownika Soft Fork wymaga stosunkowo długiego czasu realizacji przed aktywacją, możemy połączyć z BIP9, aby dać możliwość szybszej aktywacji skoordynowanej z mocą Hash lub aktywacji w dniu flagi, w zależności od tego, co nastąpi wcześniej.
> W obu przypadkach możemy wykorzystać systemy ostrzegania w BIP9. Zmiana jest stosunkowo prosta, dodając parametr czasu aktywacji, który spowoduje przejście stanu BIP9 do LOCKED_IN przed końcem limitu czasu wdrożenia BIP9.

Pomysł ten spotkał się z dużym zainteresowaniem, ale nie uzyskał jednomyślnego poparcia, co spowodowało obawy o potencjalny podział łańcucha. Artykuł Aarona van Wirduma wyjaśnia, jak ostatecznie rozwiązano tę kwestię dzięki [BIP91](https://github.com/Bitcoin/bips/blob/master/bip-0091.mediawiki), którego autorem jest James Hilliard:


> Hilliard zaproponował nieco skomplikowane, ale sprytne rozwiązanie, które sprawiłoby, że wszystko byłoby kompatybilne: Segregowana aktywacja świadka, zaproponowana przez zespół ds. rozwoju Bitcoin Core, BIP148 UASF i mechanizm aktywacji New York Agreement. Jego BIP91 mógłby utrzymać Bitcoin w całości - przynajmniej podczas aktywacji SegWit.

Wiązało się to z kilkoma bardziej skomplikowanymi czynnikami (np. tak zwanym "porozumieniem nowojorskim"), które ten BIP musiał wziąć pod uwagę. Zachęcamy do przeczytania całego artykułu Van Wirduma, aby poznać wiele interesujących szczegółów tej historii.


#### Dyskusja po SegWit


Po wdrożeniu SegWit pojawiła się dyskusja na temat mechanizmów wdrażania. Jak zauważył Eric Lombrozo w [swoim wystąpieniu na konferencji Breaking Bitcoin](https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) i Shaolinfry, Miner aktywowany Soft Fork nie jest idealnym mechanizmem aktualizacji:


> W pewnym momencie prawdopodobnie będziemy chcieli dodać więcej funkcji do protokołu Bitcoin. To wielkie filozoficzne pytanie, które sobie zadajemy. Czy zrobimy UASF dla następnego? A co z podejściem hybrydowym? Miner aktywowany samodzielnie został wykluczony. bip9 nie będziemy używać ponownie.

W styczniu 2020 roku Matt Corallo [wysłał wiadomość e-mail](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2020-January/017547.html) na listę mailingową Bitcoin-dev, która rozpoczęła dyskusję na temat przyszłych mechanizmów wdrażania Soft Fork. Wymienił pięć celów, które jego zdaniem były niezbędne w aktualizacji. David Harding [podsumował je w biuletynie Bitcoin Optech](https://bitcoinops.org/en/newsletters/2020/01/15/#discussion-of-Soft-Fork-activation-mechanisms) jako:


> Możliwość przerwania w przypadku napotkania poważnego sprzeciwu wobec proponowanych zmian zasad konsensusu. Przydzielenie wystarczającej ilości czasu po wydaniu zaktualizowanego oprogramowania, aby zapewnić, że większość węzłów ekonomicznych zostanie zaktualizowana w celu egzekwowania tych zasad. Oczekiwanie, że wskaźnik Hash sieci będzie mniej więcej taki sam przed i po zmianie, a także w okresie przejściowym. Zapobieganie, w miarę możliwości, tworzeniu bloków, które są nieważne zgodnie z nowymi zasadami, co mogłoby prowadzić do fałszywych potwierdzeń w niezaktualizowanych węzłach i klientach SPV. Zapewnienie, że mechanizmy przerywania nie mogą być nadużywane przez żałobników lub partyzantów w celu wstrzymania powszechnie pożądanej aktualizacji bez znanych problemów

To, co proponuje Corallo, to połączenie Miner aktywowanego Soft Fork i Soft Fork aktywowanego przez użytkownika:


> Tak więc, jako coś bardziej konkretnego, myślę, że metoda aktywacji, która ustanawia właściwy precedens i odpowiednio uwzględnia powyższe cele, byłaby:
>

> 1) standardowe wdrożenie BIP 9 z rocznym horyzontem czasowym dla
aktywacja z 95% gotowością Miner, +

> 2) w przypadku braku aktywacji w ciągu roku, okres sześciu miesięcy
okres wyciszenia, podczas którego społeczność może analizować i dyskutować

powody braku aktywacji i, +

> 3) w przypadku, gdy ma to sens, prosty parametr wiersza poleceń/Bitcoin.conf, który był obsługiwany od pierwotnej wersji wdrożenia, umożliwiłby użytkownikom wybranie wdrożenia BIP 8 z 24-miesięcznym horyzontem czasowym dla aktywacji flagi dnia (a także nowej wersji Bitcoin Core umożliwiającej powszechne stosowanie flagi).
>

> Zapewnia to bardzo długi horyzont czasowy dla bardziej standardowej aktywacji, jednocześnie zapewniając osiągnięcie celów określonych w punkcie #5, nawet jeśli w takich przypadkach horyzont czasowy musi zostać znacznie wydłużony, aby osiągnąć cele określone w punkcie #3. Rozwój Bitcoin to nie wyścig. Jeśli musimy, odczekanie 42 miesięcy gwarantuje, że nie ustanowimy negatywnego precedensu, którego będziemy żałować w miarę dalszego rozwoju Bitcoin.

#### Aktualizacja Taproot - przyspieszony proces



Kiedy Taproot był gotowy do wdrożenia w październiku 2020 r., co oznaczało, że wszystkie szczegóły techniczne dotyczące jego zasad konsensusu zostały wdrożone i uzyskały szerokie poparcie w społeczności, dyskusje na temat tego, jak faktycznie go wdrożyć, zaczęły się rozgrzewać. Do tego momentu dyskusje te były dość powściągliwe.


Pojawiło się wiele propozycji mechanizmów aktywacji, a David Harding

[podsumował je na Bitcoin Wiki](https://en.Bitcoin.it/wiki/Taproot_activation_proposals). W swoim artykule wyjaśnił niektóre właściwości BIP8, który w tym czasie miał kilka ostatnich zmian wprowadzonych w celu uczynienia go bardziej elastycznym.


> W chwili pisania tego dokumentu [BIP8](https://github.com/Bitcoin/bips/blob/master/bip-0008.mediawiki) został opracowany na podstawie doświadczeń zdobytych w 2017 roku. Jedną z godnych uwagi zmian po BIP 9+148 jest to, że wymuszona aktywacja jest teraz oparta na wysokości bloku, a nie na medianie czasu przeszłego; drugą godną uwagi zmianą jest to, że wymuszona aktywacja jest parametrem logicznym wybieranym, gdy parametry aktywacji Soft Fork są ustawiane albo dla początkowego wdrożenia, albo aktualizowane w późniejszym wdrożeniu.

BIP8 bez wymuszonej aktywacji jest bardzo podobny do [BIP9](https://github.com/Bitcoin/bips/blob/master/bip-0009.mediawiki) wersji bitów z limitem czasu i opóźnieniem, z jedyną znaczącą różnicą polegającą na użyciu przez BIP8 wysokości bloków w porównaniu do użycia przez BIP9 mediany czasu przeszłego. To ustawienie pozwala na niepowodzenie próby (ale można ją ponowić później).


BIP8 z wymuszoną aktywacją kończy się obowiązkowym okresem sygnalizacji, w którym wszystkie bloki wyprodukowane zgodnie z jego zasadami muszą sygnalizować gotowość do Soft Fork w sposób, który spowoduje aktywację we wcześniejszym wdrożeniu tego samego Soft Fork z nieobowiązkową aktywacją. Innymi słowy, jeśli wersja x węzła zostanie wydana bez wymuszonej aktywacji, a później zostanie wydana wersja y, która z powodzeniem zmusi górników do rozpoczęcia sygnalizowania gotowości w tym samym okresie, obie wersje zaczną egzekwować nowe zasady konsensusu w tym samym czasie.


Ta elastyczność zmienionej propozycji BIP8 umożliwia wyrażenie niektórych innych pomysłów w kategoriach tego, jak wyglądałyby one przy użyciu BIP8. Zapewnia to wspólny czynnik do wykorzystania przy kategoryzacji wielu różnych propozycji.


Od tego momentu dyskusje stały się bardzo gorące, zwłaszcza wokół tego, czy `lockinontimeout` powinno być `true` (jak w aktywowanym przez użytkownika Soft Fork, określanym przez Hardinga jako "BIP8 z wymuszoną aktywacją") czy `false` (jak w aktywowanym przez Miner Soft Fork, określanym przez Hardinga jako "BIP8 bez wymuszonej aktywacji").


Wśród wymienionych propozycji jedna z nich nosiła tytuł "Zobaczmy, co się stanie". Z jakiegoś powodu propozycja ta zyskała na popularności dopiero siedem miesięcy później.


W ciągu tych siedmiu miesięcy dyskusja trwała i wydawało się, że nie ma sposobu na osiągnięcie szerokiego konsensusu co do tego, jakiego mechanizmu wdrażania użyć. Istniały głównie dwa obozy: jeden, który preferował `lockinontimeout=true` (tłum UASF) i drugi, który preferował `lockinontimeout=false` (tłum "spróbuj, a jeśli się nie powiedzie, przemyśl ponownie"). Ponieważ nie było przytłaczającego poparcia dla żadnej z tych opcji, debata toczyła się w kółko, pozornie bez żadnej drogi naprzód. Niektóre z tych dyskusji odbywały się na IRC, na kanale o nazwie ##Taproot-activation, ale [5 marca 2021 r.] (https://gnusha.org/Taproot-activation/2021-03-05.log) coś się zmieniło:


```
06:42 < harding> roconnor: is somebody proposing BIP8(3m, false)?  I mentioned that the other day but I didn't see any responses.
[...]
06:43 < willcl_ark_> Amusingly, I was just thinking to myself that, vs this, the SegWit activation was actually pretty straightforward: simply a LOT=false and if it fails a UASF.
06:43 < maybehuman> it's funny, "let's see what happens" (i.e. false, 3m) was a poular choice right at the beginning of this channel iirc
06:44 < roconnor> harding: I think I am.  I don't know how much that is worth.  Mostly I think it would be a widely acceptable configuration based on my understanding of everyone's concerns.
06:44 < willcl_ark_> maybehuman: becuase everybody actually wants this, even miners reckoned they could upgrade in about two weeks (or at least f2pool said that)
06:44 < roconnor> harding: BIP8(3m,false) with an extended lockin-period.
06:45 < harding> roconnor: oh, good.  It's been my favorite option since I first summarized the options on the wiki like seven months ago.
06:45 <@michaelfolkson> UASF wouldn't release (true,3m) but yeah Core could release (false, 3m)
06:45 < willcl_ark_> harding: It certainly seems like a good approach to me. _if_ that fails, then you can try an understand why, without wasting too much time
```


Podejście "zobaczmy, co się stanie" w końcu zdawało się trafiać do umysłów ludzi. Proces ten został później nazwany "Speedy Trial" ze względu na jego krótki okres sygnalizacyjny. David Harding wyjaśnia ten pomysł szerszej społeczności w artykule

[email na listę dyskusyjną Bitcoin-dev](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-March/018583.html):

> Wcześniejsza wersja tej propozycji została udokumentowana ponad 200 dni temu, a kod bazowy Taproot został scalony z Bitcoin Core ponad 140 dni temu. Gdybyśmy rozpoczęli Speedy Trial w momencie, gdy Taproot został scalony (co jest nieco nierealne), to albo bylibyśmy mniej niż dwa miesiące od Taproot, albo przeszlibyśmy do kolejnej próby aktywacji ponad miesiąc temu.
>

> Zamiast tego długo debatowaliśmy i nie wydaje się, abyśmy byli bliżej tego, co moim zdaniem jest powszechnie akceptowalnym rozwiązaniem, niż kiedy lista dyskusyjna zaczęła omawiać schematy aktywacji po SegWit ponad rok temu. Myślę, że Speedy Trial jest sposobem na szybki postęp generate, który albo zakończy debatę (na razie, jeśli aktywacja się powiedzie), albo da nam rzeczywiste dane, na których będziemy mogli oprzeć przyszłe propozycje aktywacji Taproot.

Ten mechanizm wdrażania został dopracowany w ciągu dwóch miesięcy, a następnie wydany w [Bitcoin Core wersja 0.21.1](https://github.com/Bitcoin/Bitcoin/blob/master/doc/release-notes/release-notes-0.21.1.md#Taproot-Soft-Fork). Górnicy szybko zaczęli sygnalizować tę aktualizację, przenosząc stan wdrożenia do `LOCKED_IN`, a po okresie karencji reguły Taproot zostały aktywowane w połowie listopada 2021 r. w bloku [709632] (https://Mempool.space/block/0000000000000000000687bca986194dc2c1f949318629b44bb54ec0a94d8244).


#### Przyszłe mechanizmy wdrażania


Biorąc pod uwagę problemy z ostatnimi forkami Soft, SegWit i Taproot, nie jest jasne, w jaki sposób zostanie wdrożona kolejna aktualizacja. Speedy Trial został użyty do wdrożenia Taproot, ale został on wykorzystany do zmniejszenia przepaści między UASF i MASF, a nie dlatego, że stał się najlepszym znanym mechanizmem wdrażania.


### Ryzyko


Podczas aktywacji dowolnego Fork, czy to Hard, czy Soft, Miner aktywowanego lub aktywowanego przez użytkownika, istnieje ryzyko długotrwałego podziału łańcucha. Podział, który utrzymuje się dłużej niż kilka bloków, może spowodować poważne szkody dla nastrojów wokół Bitcoin, a także dla jego ceny. Ale przede wszystkim spowodowałoby to ogromne zamieszanie co do tego, czym jest Bitcoin. Czy Bitcoin to ten czy tamten łańcuch?


Ryzyko związane z aktywowanym przez użytkownika Soft Fork polega na tym, że nowe zasady zostaną aktywowane, nawet jeśli większość mocy Hash ich nie obsługuje. Taki scenariusz skutkowałby długotrwałym rozłamem łańcucha, który utrzymywałby się do czasu, aż większość mocy Hash przyjęłaby nowe zasady. Szczególnie Hard może zachęcać górników do przejścia na nowy łańcuch, jeśli już wydobywali bloki po podziale na starym łańcuchu, ponieważ zmieniając gałąź, porzuciliby własne nagrody za bloki. Warto jednak wspomnieć o niezwykłym epizodzie: w marcu 2013 r. doszło do długotrwałego podziału z powodu niezamierzonego Hard Fork i, w przeciwieństwie do tej zachęty, dwie główne pule Mining podjęły decyzję o porzuceniu swojej gałęzi podziału w celu przywrócenia konsensusu.


Z drugiej strony, ryzyko związane z Miner aktywowanym Soft Fork wynika z faktu, że górnicy mogą angażować się w fałszywe sygnały, co oznacza, że rzeczywisty udział mocy Hash, który popiera zmianę, może być mniejszy niż się wydaje. Jeśli rzeczywiste wsparcie nie stanowi większości mocy Hash, prawdopodobnie zobaczymy długotrwały podział łańcucha podobny do tego opisanego w poprzednim akapicie. Ten lub przynajmniej podobny problem miał miejsce w rzeczywistości, gdy BIP66 został wdrożony, ale został rozwiązany w ciągu około 6 bloków.


#### Koszty podziału



Jimmy Song [mówił o kosztach związanych z widełkami Hard](https://btctranscripts.com/breaking-Bitcoin/2017/socialized-costs-of-Hard-forks/) podczas Breaking Bitcoin w Paryżu, ale wiele z tego, co powiedział, dotyczy również rozerwania łańcucha z powodu nieudanego Soft Fork. Mówił o *negatywnych efektach zewnętrznych* i zdefiniował je jako cenę, którą ktoś inny musi zapłacić za twoje własne działania:


> Klasycznym przykładem negatywnych efektów zewnętrznych jest fabryka. Może produkuje ona - może jest to rafineria ropy naftowej - dobro, które jest dobre dla gospodarki, ale wytwarza również coś, co jest negatywnym efektem zewnętrznym, takim jak zanieczyszczenie. To nie tylko coś, za co wszyscy muszą płacić, sprzątać lub cierpieć. Ale są to również efekty drugiego i trzeciego rzędu, takie jak większy ruch w kierunku fabryki w wyniku większej liczby pracowników, którzy muszą tam dotrzeć. Może też dojść do zagrożenia dla dzikiej przyrody. Nie chodzi o to, że wszyscy muszą płacić za negatywne efekty zewnętrzne, mogą to być konkretni ludzie, na przykład ludzie, którzy wcześniej korzystali z tej drogi lub zwierzęta, które znajdowały się w pobliżu tej fabryki, i oni również płacą za koszty tej fabryki.

W kontekście Bitcoin ilustruje negatywne efekty zewnętrzne za pomocą Bitcoin Cash (bcash), który jest Hard Fork Bitcoin stworzonym na krótko przed konferencją w 2017 roku. Kategoryzuje on negatywne efekty zewnętrzne Hard Fork na koszty jednorazowe i koszty stałe.


Wśród wielu przykładów jednorazowych kosztów wymienia te ponoszone przez giełdy:


> Mamy więc kilka giełd, które musiały ponieść wiele jednorazowych kosztów. Pierwszą rzeczą, która się wydarzyła, było to, że wpłaty i wypłaty musiały zostać wstrzymane na dzień lub dwa dla tych giełd, ponieważ nie wiedziały, co się stanie. Wiele z tych giełd musiało sięgnąć do magazynu Cold, ponieważ ich użytkownicy domagali się bcash. To część ich obowiązku powierniczego, muszą to zrobić. Należy również przeprowadzić audyt nowego oprogramowania. To jest coś, co musieliśmy zrobić w itbit. Chcemy wydawać gotówkę - jak to zrobić? Musimy pobrać elektroniczną gotówkę? Czy ma złośliwe oprogramowanie? Musimy przejść audyt. Mieliśmy około 10 dni, aby dowiedzieć się, czy to jest w porządku, czy nie. A potem musisz zdecydować, czy pozwolimy tylko na jednorazową wypłatę, czy też zamierzamy umieścić tę nową monetę na liście? Dla Exchange, aby wymienić tę nową monetę, nie jest to łatwe - istnieje wiele nowych procedur dotyczących przechowywania Cold, podpisywania, wpłat, wypłat. Możesz też po prostu zorganizować jednorazowe wydarzenie, w którym w pewnym momencie dasz im ich bcash, a potem nigdy więcej o tym nie pomyślisz. Ale to też ma swoje problemy. Wreszcie, niezależnie od sposobu, w jaki to zrobisz, wypłaty lub notowania - będziesz potrzebować nowej infrastruktury do pracy z token w jakiś sposób, nawet jeśli jest to jednorazowa wypłata. Potrzebujesz jakiegoś sposobu na przekazanie tych tokenów swoim użytkownikom. Ponownie, krótkie powiadomienie. Prawda? Nie ma na to czasu, trzeba to zrobić szybko.

Wymienia również jednorazowe koszty ponoszone przez sprzedawców, podmioty przetwarzające płatności, portfele, górników i użytkowników, a także niektóre koszty stałe, na przykład utratę prywatności i wyższe ryzyko reorganizacji.


Rzeczywiście, gdy dojdzie do podziału, a łańcuch z najbardziej ogólnymi zasadami stanie się silniejszy niż łańcuch z bardziej rygorystycznymi zasadami, nastąpi reorganizacja. Będzie to miało poważny wpływ na wszystkie transakcje przeprowadzane w wymazanej gałęzi. Z tych powodów naprawdę ważne jest, aby zawsze starać się unikać podziałów łańcucha.


### Wnioski dotyczące aktualizacji


Bitcoin rozwija się i ewoluuje wraz z upływem czasu. Przez lata stosowano różne mechanizmy aktualizacji, a krzywa uczenia się jest stroma. W miarę jak dowiadujemy się więcej o tym, jak reaguje sieć, wymyślane są coraz bardziej wyrafinowane i niezawodne metody.


Aby utrzymać Bitcoin w harmonii, forki Soft okazały się być drogą naprzód, ale wielkie pytanie wciąż nie ma pełnej odpowiedzi: jak bezpiecznie wdrożyć forki Soft bez wywoływania niezgody?


## Myślenie kontradyktoryjne

<chapterId>d4982f3d-4694-51cc-99be-28f54b03a2a2</chapterId>


![](assets/adversarialthinking-banner.webp)


Ten rozdział dotyczy *myślenia kontradyktoryjnego*, sposobu myślenia, który koncentruje się na tym, co może pójść źle i jak mogą działać przeciwnicy. Zaczynamy od omówienia założeń bezpieczeństwa i modelu bezpieczeństwa Bitcoin, po czym wyjaśniamy, w jaki sposób zwykli użytkownicy mogą poprawić swoją niezależność i decentralizację Bitcoin Full node poprzez myślenie kontradyktoryjne. Następnie przyjrzymy się niektórym rzeczywistym zagrożeniom dla Bitcoin, a także umysłowi przeciwnika. Na koniec mówimy o *aksjomacie oporu*, który może pomóc zrozumieć, dlaczego ludzie w ogóle pracują nad Bitcoin.


Omawiając bezpieczeństwo w różnych systemach, ważne jest, aby zrozumieć, jakie są założenia bezpieczeństwa. Typowym założeniem bezpieczeństwa w Bitcoin jest "problem logarytmu dyskretnego jest Hard do rozwiązania", co, mówiąc najprościej, oznacza, że praktycznie niemożliwe jest znalezienie klucza prywatnego, który odpowiada konkretnemu kluczowi publicznemu. Innym dość mocnym założeniem dotyczącym bezpieczeństwa jest to, że większość mocy obliczeniowej sieci jest uczciwa, co oznacza, że grają zgodnie z zasadami. Jeśli te założenia okażą się błędne, Bitcoin będzie w tarapatach.


W 2015 roku Andrew Poelstra [wygłosił wykład](https://btctranscripts.com/scalingbitcoin/hong-kong-2015/security-assumptions/) na konferencji Scaling Bitcoin w Hong Kongu, podczas którego przeanalizował założenia bezpieczeństwa Bitcoin. Rozpoczął od zauważenia, że wiele systemów w pewnym stopniu lekceważy przeciwników; na przykład ochrona budynku przed wszystkimi rodzajami zdarzeń jest naprawdę Hard. Zamiast tego zazwyczaj akceptujemy możliwość, że ktoś może spalić budynek i do pewnego stopnia zapobiegamy temu i innym wrogim zachowaniom poprzez egzekwowanie prawa itp.


Zobacz analogię budynku autorstwa Grega Maxwella:


![](https://youtu.be/Gs9lJTRZCDc?t=2799)


Ale w sieci jest inaczej:


> Jednak w sieci tego nie ma. Mamy pseudonimowe i anonimowe zachowanie, każdy może połączyć się z każdym i zaszkodzić systemowi. Jeśli możliwe jest niekorzystne działanie na szkodę systemu, zrobią to. Nie możemy zakładać, że będą widoczni i że zostaną złapani.

Konsekwencją jest to, że wszystkie znane słabości Bitcoin muszą być w jakiś sposób wyeliminowane, w przeciwnym razie zostaną wykorzystane. W końcu Bitcoin to największy garnek miodu na świecie.


Poelstra wspomina dalej, że Bitcoin jest nowym rodzajem systemu; jest bardziej mglisty niż na przykład protokół podpisywania, który ma bardzo jasne założenia dotyczące bezpieczeństwa.


Na swoim osobistym blogu, inżynier oprogramowania Jameson Lopp, [zagłębia się w ten temat](https://blog.lopp.net/bitcoins-security-model-a-deep-dive/):


> W rzeczywistości protokół Bitcoin był i jest budowany bez formalnie zdefiniowanej specyfikacji lub modelu bezpieczeństwa. Najlepsze, co możemy zrobić, to zbadać motywacje i zachowanie aktorów w systemie, aby lepiej go zrozumieć i spróbować opisać.

Mamy więc system, który wydaje się działać w praktyce, ale nie możemy formalnie udowodnić, że jest bezpieczny. Dowód jest prawdopodobnie niemożliwy ze względu na

złożoność samego systemu.


### Nie tylko dla ekspertów Bitcoin



Znaczenie przeciwstawnego myślenia rozciąga się również w pewnym stopniu na codziennych użytkowników Bitcoin, nie tylko na hardkorowych deweloperów i ekspertów Bitcoin. Ragnar Lifthasir wspomina w [burzy tweetów](https://bitcoinwords.github.io/tweetstorm-on-adversarial-thinking), jak uproszczone narracje wokół Bitcoin - na przykład "tylko HODL" - mogą być poniżające dla samego Bitcoin, i kończy stwierdzeniem


> Aby wzmocnić Bitcoin i nas samych, musimy myśleć jak inżynierowie oprogramowania, którzy współtworzą Bitcoin. Dokonują oni wzajemnej weryfikacji, bezlitośnie szukając wad. Na swoich wydarzeniach technicznych rozmawiają o każdym sposobie, w jaki propozycja może zawieść. Myślą kontradyktoryjnie. Są konserwatywni

Odnosi się do tych uproszczonych narracji jako monomanii. Poprzez tę definicję mówi, że skupiając się na jednej rzeczy - na przykład "tylko HODL" - ryzykujesz przeoczenie prawdopodobnie ważniejszych rzeczy, takich jak utrzymywanie bezpieczeństwa Bitcoin lub robienie wszystkiego, co w twojej mocy, aby używać Bitcoin w sposób Trustless.


### Zagrożenia



Istnieje wiele znanych słabości Bitcoin, a wiele z nich jest aktywnie wykorzystywanych. Aby się o tym przekonać, warto zajrzeć na stronę [Weaknesses page](https://en.Bitcoin.it/wiki/Weaknesses) na wiki Bitcoin. Wymieniono tam wiele różnych problemów, takich jak

Wallet kradzież i ataki typu denial-of-service:


> Jeśli atakujący spróbuje wypełnić sieć kontrolowanymi przez siebie klientami, bardzo prawdopodobne jest, że połączysz się tylko z węzłami atakującego. Chociaż Bitcoin nigdy nie używa do niczego liczby węzłów, całkowite odizolowanie węzła od uczciwej sieci może być pomocne w przeprowadzaniu innych ataków.

Ten rodzaj ataku nazywany jest *atakiem Sybil* i występuje zawsze, gdy pojedynczy podmiot kontroluje wiele węzłów w sieci i wykorzystuje je do wyświetlania się jako wiele podmiotów.


Jak również wspomniano w cytacie, atak Sybil nie jest skuteczny w sieci Bitcoin, ponieważ nie ma głosowania za pośrednictwem węzłów lub innych numerowalnych jednostek, ale raczej za pomocą mocy obliczeniowej. Niemniej jednak ta płaska struktura sprawia, że system jest podatny na inne ataki. Strona wiki Bitcoin przedstawia również inne możliwe ataki, takie jak ukrywanie informacji (często określane jako *atak zaćmienia*) oraz sposób, w jaki Bitcoin Core implementuje pewne heurystyczne środki zaradcze przeciwko takim atakom.


Powyższe to przykłady realnych zagrożeń, którymi należy się zająć.


### Pole prostego sabotażu


![](assets/sabotage-manual.webp)


Fragment podręcznika Simple Sabotage Field Manual


Aby lepiej zrozumieć umysł przeciwnika, pomocne może być zapoznanie się z jego sposobem działania. Amerykański organ rządowy o nazwie Office of Strategic Services, który działał podczas II wojny światowej i miał na celu prowadzenie szpiegostwa, sabotażu i szerzenia propagandy, opracował [podręcznik](https://www.gutenberg.org/ebooks/26184) dla swojego personelu na temat tego, jak prawidłowo sabotować wroga. Jego tytuł brzmiał "Simple Sabotage Field Manual" i zawierał konkretne wskazówki dotyczące infiltracji wroga, aby uczynić jego życie Hard. Wskazówki obejmowały zarówno podpalanie magazynów, jak i powodowanie zniszczeń na ćwiczeniach w celu zmniejszenia liczebności wroga

wydajność.


Na przykład, istnieje sekcja o tym, jak infiltrator może zakłócić działanie organizacji. Nie jest Hard jasne, w jaki sposób taka taktyka mogłaby zostać wykorzystana do ataku na proces rozwoju Bitcoin, w którym każdy może uczestniczyć. Dedykowany atakujący może powstrzymywać postępy poprzez niekończące się obawy o nieistotne kwestie, targować się o precyzyjne sformułowania i próbować powtórzyć dyskusje, które zostały już kompleksowo omówione. Atakujący może również zatrudnić armię trolli, aby zwielokrotnić swoją skuteczność; możemy to nazwać społecznym atakiem Sybil. Używając ataku Social Sybil, mogą sprawić, że będzie wyglądało na to, że opór przeciwko proponowanej zmianie jest większy niż w rzeczywistości.


Podkreśla to, jak zdeterminowane państwo może i zrobi wszystko, co w jego mocy, aby zniszczyć wroga, w tym rozbić go od wewnątrz. Ponieważ Bitcoin jest formą pieniądza, która konkuruje z uznanymi walutami fiducjarnymi, istnieje prawdopodobieństwo, że państwa będą postrzegać Bitcoin jako wroga.


### Aksjomat oporu


Eric Voskuil [pisze na swojej stronie wiki Cryptoeconomics](https://github.com/libbitcoin/libbitcoin-system/wiki/Axiom-of-Resistance) o tym, co nazywa "aksjomatem oporu":


> Innymi słowy, istnieje założenie, że system może oprzeć się kontroli państwa. Nie jest to akceptowane jako fakt, ale uważane za rozsądne założenie, ze względu na empiryczne badania zachowania podobnych systemów, na których można oprzeć system.
>

> Ten, kto nie akceptuje aksjomatu oporu, rozważa zupełnie inny system niż Bitcoin. Jeśli założymy, że nie jest możliwe, aby system oparł się kontroli państwa, wnioski nie mają sensu w kontekście Bitcoin - tak jak wnioski z geometrii sferycznej są sprzeczne z euklidesową. W jaki sposób Bitcoin może być wolny od przyzwolenia lub odporny na cenzurę bez aksjomatu? Sprzeczność prowadzi do popełniania oczywistych błędów w próbie racjonalizacji konfliktu.


Zasadniczo mówi on, że tylko wtedy, gdy zakłada się, że możliwe jest stworzenie systemu, którego państwa nie mogą kontrolować, warto próbować.


Oznacza to, że aby pracować nad Bitcoin, należy zaakceptować aksjomat oporu, w przeciwnym razie lepiej poświęcić swój czas na inne projekty. Uznanie tego aksjomatu pomaga skoncentrować wysiłki programistyczne na prawdziwych problemach: kodowaniu wokół przeciwników na poziomie państwowym. Innymi słowy, myśl przeciwstawnie.


### Wnioski dotyczące myślenia kontradyktoryjnego



Zdecentralizowany system nie może mieć odpowiedzialności poza samym systemem, dlatego Bitcoin musi zapobiegać złośliwym zachowaniom bardziej rygorystycznie niż tradycyjne systemy. W takim systemie konieczne jest myślenie adwersarskie.


Aby zapewnić bezpieczeństwo Bitcoin, trzeba znać jego wrogów i ich motywacje. Większość zagrożeń wydaje się sprowadzać do państw narodowych, które mają ogromną władzę gospodarczą dzięki opodatkowaniu i drukowaniu pieniędzy. Prawdopodobnie nie zrezygnują one łatwo ze swoich przywilejów drukowania pieniędzy.


## Open Source

<chapterId>427a160c-f893-5b2c-afba-7b24e71ba899</chapterId>



![](assets/opensource-banner.webp)


Bitcoin jest zbudowany przy użyciu oprogramowania open source. W tym rozdziale przeanalizujemy, co to oznacza, jak działa konserwacja oprogramowania i jak otwarte oprogramowanie w Bitcoin pozwala na rozwój bez zezwoleń. Zanurzamy nasze palce w *kryptografii selekcyjnej*, która zajmuje się wyborem i wykorzystaniem bibliotek w systemach kryptograficznych. Rozdział zawiera sekcję o procesie recenzowania Bitcoin, a następnie kolejną o sposobach finansowania deweloperów Bitcoin. Ostatnia sekcja mówi o tym, jak kultura open source Bitcoin może wyglądać naprawdę dziwnie z zewnątrz i dlaczego ta postrzegana dziwność jest tak naprawdę oznaką dobrego zdrowia.


Większość oprogramowania Bitcoin, a w szczególności Bitcoin Core, jest oprogramowaniem typu open source. Oznacza to, że kod źródłowy oprogramowania jest udostępniany ogółowi społeczeństwa do wglądu, majsterkowania, modyfikacji i redystrybucji. Definicja otwartego oprogramowania na stronie [](https://opensource.org/osd) zawiera, między innymi, następujące ważne punkty:


> Swobodna redystrybucja: Licencja nie będzie ograniczać żadnej ze stron w sprzedaży lub rozdawaniu oprogramowania jako składnika zbiorczej dystrybucji oprogramowania zawierającej programy z kilku różnych źródeł. Licencja nie będzie wymagać opłat licencyjnych ani innych opłat za taką sprzedaż.
>

> Kod źródłowy: Program musi zawierać kod źródłowy i musi umożliwiać dystrybucję zarówno w postaci kodu źródłowego, jak i w postaci skompilowanej. Jeśli jakaś forma produktu nie jest dystrybuowana z kodem źródłowym, musi istnieć dobrze nagłośniony sposób uzyskania kodu źródłowego za cenę nie wyższą niż rozsądny koszt reprodukcji, najlepiej pobieranie przez Internet bez opłat. Kod źródłowy musi być preferowaną formą, w jakiej programista zmodyfikowałby program. Celowo zaciemniony kod źródłowy jest niedozwolony. Formy pośrednie, takie jak dane wyjściowe preprocesora lub translatora, są niedozwolone.
>

> Dzieła pochodne: Licencja musi zezwalać na modyfikacje i prace pochodne oraz umożliwiać ich dystrybucję na tych samych warunkach, co licencja oryginalnego oprogramowania.

Bitcoin Core jest zgodny z tą definicją, ponieważ jest rozpowszechniany na licencji [MIT License](https://github.com/Bitcoin/Bitcoin/blob/master/COPYING):


```
The MIT License (MIT)

Copyright (c) 2009-2022 The Bitcoin Core developers
Copyright (c) 2009-2022 Bitcoin Developers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```


Jak wspomniano w rozdziale "Nie ufaj, weryfikuj", ważne jest, aby użytkownicy mogli zweryfikować, czy oprogramowanie Bitcoin, które uruchamiają, "działa zgodnie z reklamą". Aby to zrobić, muszą mieć nieograniczony dostęp do kodu źródłowego oprogramowania, które chcą zweryfikować.


W kolejnych sekcjach zagłębimy się w inne interesujące aspekty oprogramowania open source w Bitcoin.


### Konserwacja oprogramowania



Kod źródłowy Bitcoin Core jest przechowywany w repozytorium Git hostowanym na [GitHub](https://github.com/Bitcoin/Bitcoin). Każdy może sklonować to repozytorium bez pytania o pozwolenie, a następnie sprawdzić, zbudować lub wprowadzić zmiany lokalnie. Oznacza to, że istnieje wiele tysięcy kopii repozytorium rozsianych po całym świecie. Są to kopie tego samego repozytorium, więc co sprawia, że to konkretne repozytorium GitHub Bitcoin Core jest tak wyjątkowe? Technicznie nie jest ono wcale wyjątkowe, ale społecznie stało się centralnym punktem rozwoju Bitcoin.


Bitcoin i ekspert ds. bezpieczeństwa Jameson Lopp wyjaśnia to bardzo dobrze w [wpisie na blogu](https://blog.lopp.net/who-controls-Bitcoin-core-/) zatytułowanym "Kto kontroluje Bitcoin Core?":


> Bitcoin Core jest centralnym punktem rozwoju protokołu Bitcoin, a nie punktem dowodzenia i kontroli. Gdyby przestał istnieć z jakiegokolwiek powodu, pojawiłby się nowy punkt centralny - platforma komunikacji technicznej, na której jest oparta (obecnie repozytorium GitHub), jest raczej kwestią wygody niż definicji / integralności projektu. W rzeczywistości widzieliśmy już, jak główny punkt rozwoju Bitcoin zmieniał platformy, a nawet nazwy!

Następnie wyjaśnia, w jaki sposób oprogramowanie Bitcoin Core jest utrzymywane i zabezpieczone przed złośliwymi zmianami kodu. Ogólne wnioski z tego pełnego artykułu podsumowano na samym końcu:


> Nikt nie kontroluje Bitcoin.
>

> Nikt nie kontroluje centralnego punktu rozwoju Bitcoin.

Deweloper Bitcoin Core, Eric Lombrozo, mówi więcej o procesie rozwoju w swoim poście [Medium] (https://medium.com/@elombrozo/the-Bitcoin-core-merge-process-74687a09d81d) zatytułowanym "The Bitcoin Core Merge Process":


> Każdy może Fork repozytorium bazy kodu i wprowadzać dowolne zmiany we własnym repozytorium. Może zbudować klienta z własnego repozytorium i uruchomić go, jeśli chce. Może również tworzyć kompilacje binarne do uruchamiania przez inne osoby.
>

> Jeśli ktoś chce scalić zmianę wprowadzoną we własnym repozytorium do Bitcoin Core, może przesłać pull request. Po jego przesłaniu każdy może przejrzeć zmiany i skomentować je, niezależnie od tego, czy ma dostęp do zatwierdzenia w samym Bitcoin Core.

Należy zauważyć, że pull requesty mogą trwać bardzo długo, zanim zostaną scalone z repozytorium przez opiekunów, a to zwykle z powodu braku recenzji, co często wynika z braku *recenzentów*.


Lombrozo mówi również o procesie, który otacza zmiany konsensusu, ale wykracza to nieco poza zakres tego rozdziału. Więcej informacji na temat aktualizacji protokołu Bitcoin można znaleźć w poprzednim rozdziale "Aktualizacja".


### Rozwój bez zezwoleń



Ustaliliśmy, że każdy może napisać kod dla Bitcoin Core bez pytania o pozwolenie, ale niekoniecznie musi on zostać scalony z głównym repozytorium Git. Ma to wpływ na wszelkie modyfikacje, od zmiany schematów kolorów graficznego Interface użytkownika, po sposób formatowania wiadomości peer-to-peer, a nawet zasady konsensusu, tj. zestaw reguł definiujących prawidłowy Blockchain.


Prawdopodobnie równie ważne jest to, że użytkownicy mogą swobodnie rozwijać systemy na bazie Bitcoin, bez pytania o pozwolenie. Widzieliśmy niezliczone udane projekty oprogramowania, które zostały zbudowane na Bitcoin, takie jak:



- Lightning Network: Sieć płatności, która pozwala na szybkie płatności bardzo małych kwot. Wymaga bardzo niewielu On-Chain Bitcoin transakcji. Istnieją różne interoperacyjne implementacje, takie jak [Core Lightning](https://github.com/ElementsProject/lightning), [LND](https://github.com/lightningnetwork/LND), [Eclair](https://github.com/ACINQ/eclair) i [Lightning Dev Kit](https://github.com/lightningdevkit).
- CoinJoin: Wiele stron współpracuje w celu połączenia swoich płatności w jedną transakcję, aby utrudnić klastrowanie Address. Istnieją różne implementacje.
- Łańcuchy boczne: System ten może zablokować monetę na Bitcoin w Blockchain w celu odblokowania jej na innym Blockchain. Pozwala to na przeniesienie bitcoinów do innego Blockchain, a mianowicie Sidechain, aby korzystać z funkcji dostępnych na tym Sidechain. Przykłady obejmują [Blockstream's Elements](https://github.com/ElementsProject/Elements).
- OpenTimestamps: Pozwala na [Timestamp dokumentu](https://opentimestamps.org/) na Bitcoin Blockchain w sposób prywatny. Następnie można użyć tego Timestamp, aby udowodnić, że dokument musiał istnieć przed określonym czasem.


Bez rozwoju bez zezwoleń wiele z tych projektów nie byłoby możliwych. Jak wspomniano w rozdziale poświęconym neutralności, gdyby deweloperzy musieli prosić o pozwolenie na tworzenie protokołów na Bitcoin, rozwijane byłyby tylko protokoły dozwolone przez centralny komitet przyznający uprawnienia deweloperom.


Powszechne jest, że systemy takie jak te wymienione powyżej są licencjonowane jako oprogramowanie open source, co z kolei pozwala ludziom na wnoszenie wkładu, ponowne wykorzystanie lub przeglądanie ich kodu bez pytania o pozwolenie. Otwarte oprogramowanie stało się złotym standardem licencjonowania oprogramowania Bitcoin.


### Pseudonimowy rozwój



Brak konieczności proszenia o pozwolenie na rozwijanie oprogramowania Bitcoin daje interesującą i ważną opcję: możesz pisać i publikować kod w Bitcoin Core lub innym projekcie open source bez ujawniania swojej tożsamości.


Wielu deweloperów wybiera tę opcję, działając pod pseudonimem i starając się oddzielić go od swojej prawdziwej tożsamości. Powody takiego działania mogą się różnić w zależności od dewelopera. Jednym z pseudonimowych użytkowników jest ZmnSCPxj. Wśród innych projektów ma on swój wkład w Bitcoin Core i Core Lightning, jedną z kilku implementacji Lightning Network. [Pisze on](https://zmnscpxj.github.io/about.html) na swojej stronie internetowej:


> Jestem ZmnSCPxj, losowo wygenerowana osoba internetowa. Moje zaimki to on/ona/jego/jej.
>

> Rozumiem, że ludzie instynktownie pragną poznać moją tożsamość. Uważam jednak, że moja tożsamość jest w dużej mierze niematerialna i wolę być oceniany na podstawie mojej pracy.
>

> Jeśli zastanawiasz się, czy przekazać darowiznę, czy nie, i zastanawiasz się, jakie są moje koszty utrzymania lub moje dochody, zrozum, że właściwie rzecz biorąc, powinieneś przekazać mi darowiznę w oparciu o użyteczność, którą uważasz za moją
artykuły i moja praca nad Bitcoin i Lightning Network.


W jego przypadku powód używania pseudonimu należy oceniać na podstawie jego zasług, a nie tego, kim jest osoba lub osoby kryjące się za pseudonimem. Co ciekawe, ujawnił on w [artykule na CoinDesk](https://www.coindesk.com/markets/2020/06/29/many-Bitcoin-developers-are-choosing-to-use-pseudonyms-for-good-reason/), że pseudonim został stworzony z innego powodu.


> Moim początkowym powodem [używania pseudonimu] było po prostu to, że martwiłem się [o] popełnienie ogromnego błędu; dlatego ZmnSCPxj miał być pierwotnie jednorazowym pseudonimem, który można by porzucić w takim przypadku. Wydaje się jednak, że zyskał on w większości pozytywną reputację, więc go zachowałem

Używanie pseudonimu rzeczywiście pozwala ci mówić swobodniej bez narażania swojej osobistej reputacji na ryzyko, gdybyś powiedział coś głupiego lub popełnił jakiś duży błąd. Jak się okazało, jego pseudonim zyskał bardzo dobrą reputację, a w 2019 roku [otrzymał nawet dotację na rozwój] (https://twitter.com/spiralbtc/status/1204815615678177280), co samo w sobie jest świadectwem bezwarunkowej natury Bitcoin.


Prawdopodobnie najbardziej znanym pseudonimem w Bitcoin jest Satoshi Nakamoto. Nie jest jasne, dlaczego zdecydował się na pseudonim, ale z perspektywy czasu była to prawdopodobnie dobra decyzja z wielu powodów:


- Ponieważ wiele osób spekuluje, że Nakamoto posiada wiele Bitcoin, dla jego bezpieczeństwa finansowego i osobistego konieczne jest, aby jego tożsamość pozostała nieznana.
- Ponieważ jego tożsamość jest nieznana, nie ma możliwości ścigania kogokolwiek, co daje różnym organom rządowym czas Hard.
- Nie ma autorytatywnej osoby, na której można by się wzorować, dzięki czemu Bitcoin jest bardziej merytokratyczny i odporny na szantaż.


Zauważ, że te punkty nie dotyczą tylko Satoshi Nakamoto, ale każdego, kto pracuje w Bitcoin lub posiada znaczne ilości waluty, w różnym stopniu.


### Kryptografia selekcji


Programiści open source często korzystają z bibliotek open source opracowanych przez inne osoby. Jest to naturalna i wspaniała część każdego zdrowego ekosystemu. Jednak oprogramowanie Bitcoin ma do czynienia z prawdziwymi pieniędzmi i w związku z tym programiści muszą zachować szczególną ostrożność przy wyborze bibliotek stron trzecich, na których powinni polegać.


W filozoficznej [rozmowie o kryptografii] (https://btctranscripts.com/greg-maxwell/2015-04-29-gmaxwell-Bitcoin-selection-cryptography/) Gregory Maxwell chce przedefiniować termin "kryptografia", który jego zdaniem jest zbyt wąski. Wyjaśnia, że zasadniczo *informacja chce być wolna* i na tym opiera swoją definicję kryptografii:


> Kryptografia to sztuka i nauka, której używamy do walki z fundamentalną naturą informacji, do naginania jej do naszej politycznej i moralnej woli oraz do kierowania jej do ludzkich celów wbrew wszelkim szansom i wysiłkom, by się jej przeciwstawić.

Następnie wprowadza termin *kryptografia selekcyjna*, określany jako sztuka wyboru narzędzi kryptograficznych, i wyjaśnia, dlaczego jest to ważna część kryptografii. Obraca się wokół tego, jak wybrać biblioteki kryptograficzne, narzędzia i praktyki, lub jak mówi "kryptosystem wyboru kryptosystemów".


Używając konkretnych przykładów, pokazuje, jak kryptografia selekcji może łatwo pójść okropnie źle, a także proponuje listę pytań, które można sobie zadać podczas jej praktykowania. Poniżej znajduje się skrócona wersja tej listy:


- Czy oprogramowanie jest przeznaczone do Twoich celów?
- Czy kwestie kryptograficzne są traktowane poważnie?
- Jak wygląda proces weryfikacji? Czy istnieje taki proces?
- Jakie jest doświadczenie autorów?
- Czy oprogramowanie jest udokumentowane?
- Czy oprogramowanie jest przenośne?
- Czy oprogramowanie zostało przetestowane?
- Czy oprogramowanie stosuje najlepsze praktyki?


Chociaż nie jest to ostateczny przewodnik po sukcesie, przejście przez te punkty może być bardzo pomocne podczas wykonywania kryptografii selekcji.


Ze względu na kwestie wspomniane powyżej przez Maxwella, Bitcoin Core naprawdę stara się Hard [zminimalizować swoją ekspozycję na biblioteki stron trzecich] (https://github.com/Bitcoin/Bitcoin/blob/master/doc/dependencies.md). Oczywiście, nie da się wyeliminować wszystkich zewnętrznych zależności, w przeciwnym razie musiałbyś napisać wszystko sam, od renderowania czcionek po implementację wywołań systemowych.


### Recenzja



Ta sekcja nosi nazwę "Przegląd", a nie "Przegląd kodu", ponieważ bezpieczeństwo Bitcoin opiera się w dużej mierze na przeglądzie na wielu poziomach, a nie tylko na kodzie źródłowym. Co więcej, różne pomysły wymagają przeglądu na różnych poziomach: zmiana reguły konsensusu wymagałaby głębszego przeglądu na większej liczbie poziomów w porównaniu ze zmianą schematu kolorów lub poprawką literówki.


W drodze do ostatecznego przyjęcia, pomysł zazwyczaj przechodzi przez kilka faz dyskusji i przeglądu. Niektóre z tych faz wymieniono poniżej:



- Pomysł został opublikowany na liście mailingowej Bitcoin-dev
- Pomysł ten został sformalizowany w postaci propozycji ulepszenia Bitcoin (BIP)
- BIP jest zaimplementowany w pull request (PR) do Bitcoin Core
- Omówiono mechanizmy wdrażania
- Niektóre konkurencyjne mechanizmy wdrażania zostały zaimplementowane w pull requestach do Bitcoin Core
- Żądania ściągnięcia są scalane z gałęzią główną
- Użytkownicy decydują, czy chcą korzystać z oprogramowania, czy nie


Na każdym z tych etapów ludzie o różnych punktach widzenia i pochodzeniu przeglądają dostępne informacje, czy to kod źródłowy, BIP, czy tylko luźno opisany pomysł. Fazy zwykle nie są wykonywane w żaden ściśle odgórny sposób, w rzeczywistości wiele faz może odbywać się jednocześnie, a czasami przechodzisz między nimi. Różne osoby mogą również przekazywać informacje zwrotne na różnych etapach.


Jednym z najbardziej płodnych recenzentów kodu w Bitcoin Core jest Jon Atack. Napisał on [wpis na blogu](https://jonatack.github.io/articles/how-to-review-pull-requests-in-Bitcoin-core) o tym, jak przeglądać pull requesty w Bitcoin Core. Podkreśla on, że dobry recenzent kodu skupia się na tym, jak najlepiej dodać wartość.


> Jako nowicjusz, celem jest próba dodania wartości, z życzliwością i pokorą, jednocześnie ucząc się jak najwięcej.
>

> Dobrym podejściem jest sprawienie, by nie chodziło o ciebie, ale raczej "Jak mogę najlepiej służyć?"

Podkreśla on fakt, że recenzja jest naprawdę ograniczającym czynnikiem w Bitcoin Core. Wiele dobrych pomysłów utknęło w zawieszeniu, w którym nie ma recenzji. Zauważ, że recenzowanie jest nie tylko korzystne dla Bitcoin, ale także świetnym sposobem na poznanie oprogramowania i jednoczesne dostarczanie mu wartości. Zasadą Atacka jest przejrzenie 5-15 PR przed dokonaniem własnego PR. Ponownie, należy skupić się na tym, jak najlepiej służyć społeczności, a nie na tym, jak scalić własny kod. Podkreśla on również, jak ważne jest dokonywanie przeglądu na odpowiednim poziomie: czy jest to czas na gnidy i literówki, czy też deweloper potrzebuje bardziej zorientowanego na koncepcję przeglądu? Jon Attack dodaje:


> Przydatnym pierwszym pytaniem przy rozpoczynaniu przeglądu może być: "Co jest najbardziej potrzebne w tym momencie?" Odpowiedź na to pytanie wymaga doświadczenia i zgromadzonego kontekstu, ale jest to przydatne pytanie przy podejmowaniu decyzji, w jaki sposób można wnieść największą wartość w jak najkrótszym czasie.

Druga połowa postu zawiera przydatne praktyczne wskazówki techniczne dotyczące faktycznego przeprowadzania przeglądu i zawiera linki do ważnej dokumentacji do dalszej lektury.


Gloria Zhao, programistka Bitcoin Core i recenzentka kodu, napisała [artykuł](https://github.com/glozow/Bitcoin-notes/blob/master/review-checklist.md) zawierający pytania, które zwykle zadaje sobie podczas recenzji. Określiła również, co uważa za dobrą recenzję:


> Osobiście uważam, że dobra recenzja to taka, w której zadałem sobie wiele konkretnych pytań na temat PR i byłem zadowolony z odpowiedzi
do nich. [...] Oczywiście zaczynam od pytań koncepcyjnych, następnie pytań związanych z podejściem, a następnie pytań dotyczących implementacji. Ogólnie rzecz biorąc, osobiście uważam, że bezużyteczne jest pozostawianie komentarzy związanych ze składnią C++ w wersji roboczej PR i czułbym się niegrzecznie wracając do "czy to ma sens" po tym, jak autor odniósł się do ponad 20 moich sugestii dotyczących organizacji kodu.


Jej pomysł, że dobra recenzja powinna skupiać się na tym, co jest najbardziej potrzebne w danym momencie, jest zgodny z radą Jona Atacka. Ona

proponuje listę pytań, które można sobie zadać na różnych poziomach procesu recenzowania, ale podkreśla, że lista ta nie jest w żaden sposób wyczerpująca ani nie stanowi bezpośredniego przepisu. Lista jest zilustrowana rzeczywistymi przykładami z GitHub.


### Finansowanie



Wiele osób pracuje nad rozwojem Bitcoin open source, zarówno dla Bitcoin Core, jak i dla innych projektów. Wielu robi to w wolnym czasie, nie otrzymując żadnego wynagrodzenia, ale niektórzy deweloperzy również otrzymują za to wynagrodzenie.


Firmy, osoby prywatne i organizacje, które są zainteresowane dalszym sukcesem Bitcoin, mogą przekazywać fundusze deweloperom, bezpośrednio lub za pośrednictwem organizacji, które z kolei dystrybuują fundusze do poszczególnych deweloperów. Istnieje również wiele firm skupionych na Bitcoin, które zatrudniają wykwalifikowanych deweloperów, pozwalając im pracować nad Bitcoin w pełnym wymiarze godzin.


### Szok kulturowy



Ludzie czasami odnoszą wrażenie, że wśród deweloperów Bitcoin jest wiele walk i niekończących się gorących debat, a oni sami są niezdolni do podejmowania decyzji.


Na przykład mechanizm wdrażania Taproot był dyskutowany przez długi czas, podczas którego utworzyły się dwa "obozy". Jeden z nich chciał "zawalić" aktualizację, jeśli górnicy nie zagłosowaliby w przeważającej większości za nowymi zasadami po pewnym czasie, podczas gdy drugi chciał egzekwować zasady po tym momencie bez względu na wszystko. Michael Folkson podsumował argumenty obu obozów w wiadomości [email](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-February/018380.html) wysłanej na listę mailingową Bitcoin-dev.


Debata trwała pozornie w nieskończoność i naprawdę Hard nie widział, by w najbliższym czasie doszło do jakiegokolwiek konsensusu w tej sprawie. To doprowadziło ludzi do frustracji, a w rezultacie temperatura wzrosła. Gregory Maxwell (jako użytkownik nullc) martwił się [na Reddit](https://www.reddit.com/r/Bitcoin/comments/hrlpnc/technical_taproot_why_activate/fyqbn8s/?utm_source=share&utm_medium=web2x&context=3), że długie dyskusje sprawią, że aktualizacja będzie mniej bezpieczna:


> W tym momencie dodatkowe oczekiwanie nie dodaje więcej recenzji i pewności. Zamiast tego, dodatkowe opóźnienie osłabia inercję i potencjalnie zwiększa ryzyko, ponieważ ludzie zaczynają zapominać o szczegółach, opóźniając prace nad dalszym wykorzystaniem (np. wsparcie Wallet) i nie inwestując tyle dodatkowego wysiłku w przegląd, ile zainwestowaliby, gdyby mieli pewność co do ram czasowych aktywacji.

Ostatecznie spór ten został rozwiązany dzięki nowej propozycji Davida Hardinga i Russela O'Connora o nazwie Speedy Trial, która zakładała stosunkowo krótszy okres sygnalizacji dla górników, aby zablokować aktywację Taproot lub szybko zawieść. Jeśli aktywowali go w tym czasie, Taproot zostanie wdrożony około 6 miesięcy później.


Ktoś, kto nie jest przyzwyczajony do procesu rozwoju Bitcoin, prawdopodobnie pomyślałby, że te gorące debaty wyglądają okropnie źle, a nawet toksycznie. Istnieją co najmniej dwa czynniki, które sprawiają, że w oczach niektórych wyglądają one źle:



- W porównaniu do firm o zamkniętym kodzie źródłowym, wszystkie debaty odbywają się na otwartej przestrzeni, bez edycji. Firma programistyczna, taka jak Google, nigdy nie pozwoliłaby swoim pracownikom na otwartą debatę na temat proponowanych funkcji, co najwyżej opublikowałaby oświadczenie o stanowisku firmy w tej sprawie. To sprawia, że firmy wyglądają bardziej harmonijnie w porównaniu do Bitcoin.
- Ponieważ Bitcoin nie wymaga zezwoleń, każdy może wyrażać swoje opinie. Różni się to zasadniczo od zamkniętej firmy, która ma garstkę ludzi z opinią, zwykle podobnie myślących. Mnogość opinii wyrażanych w Bitcoin jest po prostu oszałamiająca w porównaniu do, na przykład, PayPal.


Większość deweloperów Bitcoin twierdzi, że ta otwartość zapewnia dobre i zdrowe środowisko, a nawet, że jest niezbędna do osiągnięcia najlepszych wyników.


Jak wskazano w rozdziale Zagrożenie, drugi z powyższych punktów może być bardzo korzystny, ale ma też wadę. Atakujący może stosować taktyki przeciągania, takie jak te opisane w [Simple Sabotage Field Manual] (https://www.gutenberg.org/ebooks/26184), aby zakłócić proces podejmowania decyzji i rozwoju.


Kolejną rzeczą wartą wspomnienia jest to, że ponieważ Bitcoin to pieniądze, a Bitcoin Core zabezpiecza niezgłębione ilości pieniędzy, bezpieczeństwo w tym kontekście nie jest traktowane lekko. Właśnie dlatego doświadczony Bitcoin Core

deweloperzy mogą wydawać się bardzo Hard-headed, co zazwyczaj jest uzasadnione. Rzeczywiście, funkcja ze słabym uzasadnieniem nie zostanie zaakceptowana. To samo stałoby się, gdyby złamała ona

odtwarzalne kompilacje, dodano nowe zależności lub kod nie był zgodny z [najlepszymi praktykami] Bitcoin (https://github.com/Bitcoin/Bitcoin/blob/master/doc/developer-notes.md).


Nowi (i starzy) deweloperzy mogą być tym sfrustrowani. Ale, jak to zwykle bywa w oprogramowaniu open source, zawsze możesz Fork repozytorium, scalić co chcesz do własnego Fork i zbudować i uruchomić własną binarkę.


### Wnioski dotyczące Open Source


Bitcoin Core i większość innego oprogramowania Bitcoin jest oprogramowaniem typu open source, co oznacza, że każdy może swobodnie rozpowszechniać, modyfikować i wykorzystywać oprogramowanie w dowolny sposób. Repozytorium Bitcoin Core na GitHub jest obecnie centralnym punktem rozwoju Bitcoin, ale status ten może ulec zmianie, jeśli ludzie zaczną nie ufać jego opiekunom lub samej witrynie.


Otwarte oprogramowanie pozwala na rozwój bez zezwoleń w Bitcoin i na jego szczycie. Niezależnie od tego, czy piszesz kod, przeglądasz kod czy protokoły; open source jest tym, co pozwala ci to robić, pseudonomicznie lub nie.


Proces rozwoju wokół Bitcoin jest radykalnie otwarty, co może sprawiać, że Bitcoin wygląda jak toksyczne i nieefektywne miejsce, ale to właśnie sprawia, że Bitcoin jest odporny na złośliwe podmioty.


## Skalowanie

<chapterId>bb3f3924-202c-5cdd-b2e9-e0c1cab0e48e</chapterId>



![](assets/scaling-banner.webp)



W tym rozdziale zbadamy, w jaki sposób Bitcoin skaluje się i nie skaluje. Zaczynamy od przyjrzenia się temu, jak ludzie rozumowali o skalowaniu w przeszłości. Następnie większa część tego rozdziału wyjaśnia różne podejścia do skalowania Bitcoin, w szczególności skalowanie pionowe, poziome, wewnętrzne i warstwowe. Po każdym opisie następują rozważania na temat tego, czy dane podejście koliduje z propozycją wartości Bitcoin.


W przestrzeni Bitcoin różne osoby przypisują różne definicje słowu "skala". Niektórzy rozumieją je jako zwiększenie pojemności transakcyjnej Blockchain, inni uważają, że jest to równoznaczne z bardziej wydajnym wykorzystaniem Blockchain, a jeszcze inni postrzegają je jako rozwój systemów na szczycie Bitcoin.


W kontekście Bitcoin i dla celów tej książki definiujemy skalowanie jako *zwiększanie możliwości Bitcoin bez narażania jego odporności na cenzurę*. Definicja ta obejmuje kilka aspektów

rodzaje zmian, na przykład:


- Sprawianie, by dane wejściowe transakcji zużywały mniej bajtów
- Poprawa wydajności weryfikacji podpisu
- Zmniejszenie wykorzystania przepustowości przez sieć peer-to-peer
- Grupowanie transakcji
- Architektura warstwowa


Wkrótce zagłębimy się w różne podejścia do skalowania, ale zacznijmy od krótkiego przeglądu historii Bitcoin w kontekście skalowania.


### Historia skalowania



Skalowanie było głównym punktem dyskusji od Genesis z Bitcoin. Pierwsze zdanie [bardzo pierwszego e-maila](https://www.metzdowd.com/pipermail/cryptography/2008-November/014814.html) w odpowiedzi na ogłoszenie Satoshi o białej księdze Bitcoin na liście mailingowej Cryptography rzeczywiście dotyczyło skalowania:


> Satoshi Nakamoto napisał:
>

> "Pracowałem nad nowym elektronicznym systemem gotówkowym, który jest w pełni peer-to-peer, bez zaufanej strony trzeciej.  Artykuł jest dostępny na stronie http://www.Bitcoin.org/Bitcoin.pdf"
>

> Bardzo, bardzo potrzebujemy takiego systemu, ale sposób, w jaki rozumiem twoją propozycję, nie wydaje się skalować do wymaganego rozmiaru.

Rozmowa sama w sobie nie jest może zbyt interesująca ani dokładna, ale pokazuje, że skalowanie było problemem od samego początku.


Dyskusje na temat skalowania osiągnęły szczyt zainteresowania w latach 2015-2017, kiedy krążyło wiele różnych pomysłów na temat tego, czy i jak zwiększyć maksymalny limit rozmiaru bloku. Była to raczej nieciekawa dyskusja na temat zmiany parametru w kodzie źródłowym, zmiany, która zasadniczo niczego nie rozwiązywała, ale odsuwała problem skalowania dalej w przyszłość, budując dług techniczny.


W 2015 r. w Montrealu odbyła się konferencja pod nazwą [Scaling Bitcoin](https://scalingbitcoin.org/), a sześć miesięcy później w Hongkongu, a następnie w wielu innych miejscach na całym świecie. Skupiono się dokładnie na tym, jak skalować Address. Wielu deweloperów Bitcoin i innych entuzjastów zebrało się na tych konferencjach, aby omówić różne kwestie i propozycje dotyczące skalowania. Większość tych dyskusji nie koncentrowała się na zwiększaniu rozmiaru bloku, ale na bardziej długoterminowych rozwiązaniach.


Po konferencji w Hong Kongu w grudniu 2015 r. Gregory Maxwell [podsumował swój pogląd](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-December/011865.html) na wiele kwestii, które były przedmiotem debaty, zaczynając od ogólnej filozofii skalowania:


> Przy dostępnej technologii istnieją fundamentalne kompromisy między skalą a decentralizacją. Jeśli system jest zbyt kosztowny, ludzie będą zmuszeni zaufać stronom trzecim, zamiast niezależnie egzekwować zasady systemu. Jeśli wykorzystanie zasobów Bitcoin Blockchain w stosunku do dostępnej technologii jest zbyt duże, Bitcoin traci swoją przewagę konkurencyjną w porównaniu do starszych systemów, ponieważ walidacja będzie zbyt kosztowna (wyceniając wielu użytkowników), zmuszając zaufanie z powrotem do systemu.  Jeśli przepustowość jest zbyt niska, a nasze metody zawierania transakcji zbyt nieefektywne, dostęp do łańcucha w celu rozstrzygania sporów będzie zbyt kosztowny, ponownie wypychając zaufanie z powrotem do systemu.

Mówi o kompromisie między przepustowością a decentralizacją. Jeśli zezwolisz na większe bloki, wypchniesz niektórych ludzi z sieci, ponieważ nie będą już mieli zasobów do walidacji bloków. Ale z drugiej strony, jeśli dostęp do przestrzeni blokowej stanie się droższy, mniej osób będzie mogło sobie pozwolić na wykorzystanie jej jako mechanizmu rozstrzygania sporów. W obu przypadkach użytkownicy są popychani w kierunku zaufanych usług.


Kontynuuje, podsumowując wiele podejść do skalowania przedstawionych na konferencji. Wśród nich są bardziej wydajne obliczeniowo weryfikacje podpisów, *segregowany świadek*, w tym zmiana limitu rozmiaru bloku, bardziej wydajny przestrzennie mechanizm propagacji bloków oraz budowanie protokołów na szczycie Bitcoin w warstwach. Wiele z tych

podejścia zostały wdrożone.


### Podejścia do skalowania



Jak wskazano powyżej, skalowanie Bitcoin niekoniecznie musi polegać na zwiększaniu limitu rozmiaru bloku lub innych limitów. Przejdziemy teraz przez kilka ogólnych podejść do skalowania, z których niektóre nie cierpią z powodu kompromisu między przepustowością a decentralizacją wspomnianego w poprzedniej sekcji.


#### Skalowanie pionowe



Skalowanie pionowe to proces zwiększania zasobów obliczeniowych maszyn przetwarzających dane. W kontekście Bitcoin byłyby to pełne węzły, a mianowicie maszyny, które weryfikują Blockchain w imieniu swoich użytkowników.


Najczęściej omawianą techniką skalowania pionowego w Bitcoin jest zwiększenie limitu rozmiaru bloku. Wymagałoby to od niektórych pełnych węzłów modernizacji sprzętu, aby nadążyć za rosnącymi wymaganiami obliczeniowymi. Wadą jest to, że odbywa się to kosztem centralizacji.


Oprócz negatywnego wpływu na decentralizację Full node, skalowanie pionowe może również negatywnie wpływać na decentralizację Bitcoin i bezpieczeństwo Mining w mniej oczywisty sposób. Przyjrzyjmy się, jak "powinni" działać górnicy. Załóżmy, że Miner wydobywa blok na wysokości 7 i publikuje go w sieci Bitcoin. Minie trochę czasu, zanim ten blok osiągnie szeroką akceptację, co wynika głównie z dwóch czynników:


- Przesłanie bloku między urządzeniami równorzędnymi wymaga czasu ze względu na ograniczenia przepustowości.
- Walidacja bloku wymaga czasu.


Podczas gdy blok 7 jest propagowany przez sieć, wielu górników nadal Mining na szczycie bloku 6, ponieważ nie otrzymali jeszcze i nie zatwierdzili bloku 7. W tym czasie, jeśli którykolwiek z tych górników znajdzie nowy blok na wysokości 7, będą istniały dwa konkurujące ze sobą bloki na tej wysokości. Na wysokości 7 (lub dowolnej innej wysokości) może znajdować się tylko jeden blok, co oznacza, że jeden z dwóch kandydatów musi stać się nieaktualny.


Krótko mówiąc, nieaktualne bloki zdarzają się, ponieważ propagacja każdego bloku zajmuje trochę czasu, a im dłużej trwa propagacja, tym większe prawdopodobieństwo wystąpienia nieaktualnych bloków.


Załóżmy, że limit rozmiaru bloku zostanie zniesiony, a średni rozmiar bloku znacznie wzrośnie. Bloki rozprzestrzeniałyby się wówczas wolniej w sieci ze względu na ograniczenia przepustowości i czas weryfikacji. Wydłużenie czasu propagacji zwiększy również szanse na pojawienie się nieaktualnych bloków.


Górnicy nie lubią, gdy ich bloki są przeciągane, ponieważ stracą Block reward, więc zrobią wszystko, co w ich mocy, aby tego uniknąć

scenariusz. Środki, które mogą podjąć, obejmują:



- Odroczenie walidacji przychodzącego bloku, znane również jako *bezwalidacyjny Mining*. Górnicy mogą po prostu sprawdzić Proof-of-Work nagłówka bloku i wydobywać na jego podstawie, podczas gdy w międzyczasie pobierają pełny blok i walidują go.
- Podłączenie do Mining pool z większą przepustowością i łącznością.


Mining bez walidacji dodatkowo osłabia decentralizację Full node, ponieważ Miner ucieka się do ufania przychodzącym blokom, przynajmniej tymczasowo. W pewnym stopniu szkodzi to również bezpieczeństwu, ponieważ część mocy obliczeniowej sieci potencjalnie opiera się na nieprawidłowym Blockchain, zamiast na najsilniejszym i prawidłowym łańcuchu.


Drugi punkt ma negatywny wpływ na decentralizację Miner, ponieważ zazwyczaj pule o najlepszej łączności sieciowej i przepustowości są również największe, co powoduje, że górnicy grawitują w kierunku kilku dużych pul.


#### Skalowanie poziome



Skalowanie poziome odnosi się do technik, które dzielą obciążenie na wiele maszyn. Chociaż jest to powszechne podejście do skalowania wśród popularnych witryn internetowych i baz danych, nie jest to łatwe do wykonania w Bitcoin.


Wiele osób określa to podejście do skalowania Bitcoin jako *sharding*. Zasadniczo polega to na tym, że każdy Full node weryfikuje tylko część Blockchain. Peter Todd poświęcił wiele uwagi koncepcji shardingu. Napisał [wpis na blogu](https://petertodd.org/2015/why-scaling-Bitcoin-with-sharding-is-very-Hard) wyjaśniający sharding w ogólnych warunkach, a także przedstawiający własny pomysł o nazwie *treechains*. Artykuł jest trudny do przeczytania, ale Todd przedstawia kilka punktów, które są całkiem strawne:


> W systemach sharded "obrona Full node" nie działa, przynajmniej bezpośrednio. Chodzi o to, że nie każdy ma wszystkie dane, więc musisz zdecydować, co się stanie, gdy nie będą one dostępne.

Następnie przedstawia różne pomysły na to, jak poradzić sobie z shardingiem lub skalowaniem poziomym. Pod koniec postu podsumowuje:


> Jest jednak duży problem: święty !@#$ jest to skomplikowane w porównaniu do Bitcoin! Nawet "dziecinna" wersja shardingu - mój schemat linearyzacji zamiast zk-SNARKS - jest prawdopodobnie o jeden lub dwa rzędy wielkości bardziej złożona niż korzystanie z protokołu Bitcoin w tej chwili, ale w tej chwili wydaje się, że ogromny procent firm w tej przestrzeni rzucił ręce w górę i zamiast tego skorzystał ze scentralizowanych dostawców API. Faktyczne wdrożenie powyższego i przekazanie go w ręce użytkowników końcowych nie będzie łatwe.
>

> Z drugiej strony, decentralizacja nie jest tania: korzystanie z PayPal jest o jeden lub dwa rzędy wielkości prostsze niż protokół Bitcoin.

Wniosek jest taki, że sharding *mógłby* być technicznie możliwy, ale kosztem ogromnej złożoności. Biorąc pod uwagę, że wielu użytkowników już uważa Bitcoin za zbyt skomplikowane i zamiast tego woli korzystać ze scentralizowanych usług, przekonanie ich do korzystania z czegoś jeszcze bardziej złożonego będzie Hard.


#### Skalowanie wewnętrzne



Podczas gdy skalowanie poziome i pionowe historycznie sprawdzało się dobrze w scentralizowanych systemach, takich jak bazy danych i serwery internetowe, nie wydają się one odpowiednie dla zdecentralizowanej sieci, takiej jak Bitcoin, ze względu na ich centralizujące efekty.


Podejściem, które jest zbyt mało doceniane, jest to, co możemy nazwać *skalowaniem wewnętrznym*, co tłumaczy się jako "rób więcej za mniej". Odnosi się to do ciągłej pracy wykonywanej przez wielu programistów w celu optymalizacji już istniejących algorytmów, tak abyśmy mogli zrobić więcej w ramach istniejących ograniczeń systemu.


Ulepszenia, które zostały osiągnięte dzięki skalowaniu do wewnątrz, są co najmniej imponujące. Aby dać ci ogólne wyobrażenie o ulepszeniach na przestrzeni lat, Jameson Lopp [przeprowadził testy porównawcze](https://blog.lopp.net/Bitcoin-core-performance-evolution/) synchronizacji Blockchain, porównując wiele różnych wersji Bitcoin Core, począwszy od wersji 0.8.


![](assets/Bitcoin-Core-Sync-Performance-1.webp)


Początkowa wydajność pobierania bloków dla różnych wersji Bitcoin Core. Na osi Y znajduje się zsynchronizowana wysokość bloku, a na osi X czas potrzebny na synchronizację do tej wysokości


Poszczególne linie reprezentują różne wersje Bitcoin Core. Najbardziej wysunięta na lewo linia to najnowsza, tj. wersja 0.22, która została wydana we wrześniu 2021 r., a jej pełna synchronizacja zajęła 396 minut. Najbardziej wysunięta na prawo to wersja 0.8 z listopada 2013 r., której pełna synchronizacja zajęła 3452 minuty. Cała ta - około 10-krotna - poprawa wynika z wewnętrznego skalowania.


Usprawnienia te można sklasyfikować jako oszczędność miejsca (pamięci RAM, dysku, przepustowości itp.) lub oszczędność mocy obliczeniowej. Obie kategorie przyczyniają się do ulepszeń na powyższym diagramie.


Dobry przykład poprawy wydajności obliczeniowej można znaleźć w bibliotece [libsecp256k1](https://github.com/Bitcoin-core/secp256k1), która między innymi implementuje prymitywy kryptograficzne potrzebne do tworzenia i weryfikacji podpisów cyfrowych. Pieter Wuille jest jednym ze współautorów tej biblioteki i napisał [wątek na Twitterze](https://twitter.com/pwuille/status/1450471673321381896) prezentujący poprawę wydajności osiągniętą dzięki różnym pull requestom.


![](assets/libsecp256k1speedups.webp)


Wydajność weryfikacji podpisów w czasie, z zaznaczonymi na osi czasu istotnymi pull requestami


Wykres przedstawia trend dla dwóch różnych 64-bitowych typów procesorów, a mianowicie ARM i x86. Różnica w wydajności wynika z bardziej wyspecjalizowanych instrukcji dostępnych w architekturze x86 w porównaniu do architektury ARM, która ma mniej i bardziej ogólne instrukcje. Ogólny trend jest jednak taki sam dla obu architektur. Należy zauważyć, że oś Y jest logarytmiczna, co sprawia, że ulepszenia wyglądają mniej imponująco niż w rzeczywistości.


Istnieje również kilka dobrych przykładów ulepszeń oszczędzających miejsce, które przyczyniły się do zwiększenia wydajności. W

[Medium blog post](https://murchandamus.medium.com/2-of-3-Multisig-inputs-using-Pay-to-Taproot-d5faf2312ba3) o wkładzie Taproot w oszczędzanie miejsca, użytkownik Murch porównuje, ile miejsca w blokach wymagałaby sygnatura progowa 2 na 3, używając Taproot na różne sposoby, a także nie używając go wcale.


![](assets/murch-taproot.webp)


Oszczędność miejsca dla różnych typów wydatków, Taproot i starszych wersji.


Multisig 2 na 3 wykorzystujący natywny SegWit wymagałby łącznie 104,5+43 vB = 147,5 vB, podczas gdy najbardziej oszczędne wykorzystanie Taproot wymagałoby tylko 57,5+43 vB = 100,5 vB w standardowym przypadku użycia. W najgorszym przypadku i w rzadkich przypadkach, na przykład gdy standardowy sygnatariusz nie jest dostępny z jakiegoś powodu, Taproot używałby 107,5 + 43 vB = 150,5 vB. Nie musisz rozumieć wszystkich szczegółów, ale powinno to dać ci wyobrażenie o tym, jak programiści myślą o oszczędzaniu miejsca - liczy się każdy mały bajt.


Oprócz wewnętrznego skalowania w oprogramowaniu Bitcoin, istnieją pewne sposoby, w jakie użytkownicy mogą również przyczynić się do wewnętrznego skalowania. Mogą oni dokonywać swoich transakcji w sposób bardziej inteligentny, aby zaoszczędzić na opłatach transakcyjnych, jednocześnie zmniejszając swój ślad na wymaganiach Full node. Dwie powszechnie stosowane techniki zmierzające do osiągnięcia tego celu nazywane są grupowaniem transakcji i konsolidacją danych wyjściowych.


Idea grupowania transakcji polega na łączeniu wielu płatności w jedną transakcję, zamiast dokonywania jednej transakcji na płatność. Może to zaoszczędzić wiele opłat, a jednocześnie zmniejszyć obciążenie przestrzeni blokowej.


![](assets/tx-batching.webp)


Grupowanie transakcji łączy wiele płatności w jedną transakcję, aby zaoszczędzić na opłatach.


Konsolidacja wyjść odnosi się do korzystania z okresów niskiego zapotrzebowania na przestrzeń blokową w celu połączenia wielu wyjść w jedno wyjście. Może to obniżyć koszty opłat w późniejszym czasie, gdy trzeba będzie dokonać płatności, gdy zapotrzebowanie na przestrzeń blokową jest wysokie.


![](assets/utxo-consolidation.webp)


Konsolidacja wyjścia: Połącz swoje monety w jedną dużą monetę, gdy opłaty są niskie, aby zaoszczędzić na opłatach później.


Może nie być oczywiste, w jaki sposób konsolidacja danych wyjściowych przyczynia się do skalowania do wewnątrz. W końcu całkowita ilość danych Blockchain jest nawet nieznacznie zwiększona dzięki tej metodzie. Niemniej jednak zestaw UTXO, tj. baza danych, która śledzi, kto jest właścicielem których monet, kurczy się, ponieważ wydajesz więcej UTXO niż tworzysz. Odciąża to pełne węzły w utrzymywaniu ich zestawów UTXO.


Niestety, te dwie techniki *zarządzania UTXO* mogą być szkodliwe dla prywatności użytkownika lub jego odbiorców. W przypadku grupowania, każdy odbiorca będzie wiedział, że wszystkie grupowane dane wyjściowe pochodzą od Ciebie do innych odbiorców (z wyjątkiem ewentualnej zmiany). W przypadku konsolidacji UTXO ujawnisz, że wyjścia, które konsolidujesz, należą do tego samego Wallet. Konieczne może być więc dokonanie kompromisu między efektywnością kosztową a prywatnością.


#### Skalowanie warstwowe



Najbardziej wpływowym podejściem do skalowania jest prawdopodobnie warstwowanie. Ogólna idea stojąca za warstwowaniem polega na tym, że protokół może rozliczać płatności między użytkownikami bez dodawania transakcji do Blockchain.


Protokół warstwowy rozpoczyna się od uzgodnienia przez dwie lub więcej osób transakcji początkowej, która jest umieszczana na Blockchain, jak pokazano na poniższym rysunku.


![](assets/scaling-layer.webp)

Typowy protokół Layer 2 na Bitcoin, Layer 1.


Sposób tworzenia transakcji początkowej różni się w zależności od protokołu, ale wspólnym tematem jest to, że uczestnicy tworzą niepodpisaną transakcję początkową i szereg wstępnie podpisanych transakcji karnych, które wydają dane wyjściowe transakcji początkowej na różne sposoby. Następnie transakcja początkowa jest w pełni podpisywana i publikowana w Blockchain, a transakcje karne mogą być w pełni podpisane i opublikowane w celu ukarania niewłaściwie zachowującej się strony. Zachęca to uczestników do dotrzymywania obietnic, aby protokół mógł działać w sposób Trustless.


Po rozpoczęciu transakcji na Blockchain protokół może robić to, co powinien. Na przykład może wykonywać superszybkie płatności między uczestnikami, wdrażać pewne techniki zwiększające prywatność lub wykonywać bardziej zaawansowane skrypty, które nie byłyby obsługiwane przez Bitcoin Blockchain.


Nie będziemy szczegółowo opisywać działania poszczególnych protokołów, ale jak widać na poprzednim rysunku, Blockchain jest rzadko używany podczas cyklu życia protokołu. Cała soczysta akcja dzieje się *off-chain*. Widzieliśmy, jak może to być korzystne dla prywatności, jeśli zostanie wykonane prawidłowo, ale może być również korzystne dla skalowalności.


W poście [Reddit](https://www.reddit.com/r/Bitcoin/comments/438hx0/a_trip_to_the_moon_requires_a_rocket_with/) zatytułowanym "Podróż na Księżyc wymaga rakiety z wieloma stopniami, w przeciwnym razie równanie rakiety zje twój lunch... pakowanie wszystkich w stylu klauna-samochodu do trebusza i liczenie na sukces jest nie na miejscu.", Gregory Maxwell wyjaśnia, dlaczego nakładanie warstw jest naszą najlepszą szansą na skalowanie Bitcoin o rzędy wielkości.


Zaczyna od podkreślenia błędności postrzegania Visa lub Mastercard jako głównych konkurentów Bitcoin i podkreślenia, że zwiększenie maksymalnego rozmiaru bloku jest złym podejściem do sprostania tej konkurencji. Następnie mówi o tym, jak zrobić prawdziwą różnicę, używając warstw:


> Czy to oznacza, że Bitcoin nie może być wielkim zwycięzcą jako technologia płatności? Nie. Ale aby osiągnąć wydajność wymaganą do zaspokojenia potrzeb płatniczych świata, musimy pracować bardziej inteligentnie.
>

> Od samego początku Bitcoin był projektowany tak, aby zawierał warstwy w bezpieczny sposób dzięki możliwości inteligentnego kontraktowania (co, myślisz, że zostało to po prostu umieszczone, aby ludzie mogli filozofować na temat bezsensownych "DAO"?). W efekcie będziemy używać systemu Bitcoin jako wysoce dostępnego i całkowicie godnego zaufania zrobotyzowanego sędziego i prowadzić większość naszych interesów poza salą sądową - ale dokonywać transakcji w taki sposób, że jeśli coś pójdzie nie tak, mamy wszystkie dowody i ustalone umowy, więc możemy być pewni, że zrobotyzowany sąd to naprawi. (Geek sidebar: Jeśli wydaje się to niemożliwe, przeczytaj ten stary post na temat przecięcia transakcji)
>

> Jest to możliwe właśnie ze względu na podstawowe właściwości Bitcoin. Cenzurowalny lub odwracalny system bazowy nie nadaje się zbytnio do budowania potężnego górnego przetwarzania transakcji Layer... a jeśli aktywa bazowe nie są solidne, nie ma sensu w ogóle dokonywać z nimi transakcji.

Analogia z sędzią dobrze ilustruje sposób działania warstw: ten sędzia musi być nieprzekupny i nigdy nie zmieniać zdania, w przeciwnym razie warstwy powyżej Bitcoin Layer nie będą działać niezawodnie.


Kontynuuje, zwracając uwagę na scentralizowane usługi. Zwykle nie ma problemu z zaufaniem centralnemu serwerowi z trywialnymi ilościami Bitcoin, aby wykonać zadania: to także skalowanie warstwowe.


Minęło wiele lat od czasu, gdy Maxwell napisał powyższy artykuł, a jego słowa wciąż są aktualne. Sukces Lightning Network dowodzi, że nakładanie warstw jest rzeczywiście sposobem na zwiększenie użyteczności Bitcoin.



### Wnioski dotyczące skalowania



Omówiliśmy różne sposoby, za pomocą których można skalować Bitcoin, zwiększając jego wydajność. Skalowanie było problemem w Bitcoin od samego początku jego istnienia.


Dziś wiemy, że Bitcoin nie skaluje się dobrze w pionie ("kupuj większy sprzęt") ani w poziomie ("weryfikuj tylko części danych"), ale raczej do wewnątrz ("rób więcej za mniej") i warstwowo ("buduj protokoły na Bitcoin").


## Kiedy gówno uderza w wentylator

<chapterId>fe39c13c-310f-51fd-84ff-6b92dd01c9e7</chapterId>



![](assets/shtf-banner.webp)

Bitcoin jest tworzony przez ludzi. Ludzie piszą oprogramowanie, a następnie je uruchamiają. Kiedy odkrywana jest luka w zabezpieczeniach lub poważny błąd - czy naprawdę istnieje między nimi rozróżnienie? - zawsze odkrywają je ludzie, z krwi i kości. Ten rozdział rozważa, co ludzie robią, powinni i czego nie powinni robić, gdy gówno uderzy w wentylator. Pierwsza sekcja wyjaśnia termin *odpowiedzialne ujawnienie*, który odnosi się do tego, w jaki sposób ktoś, kto odkryje podatność, może działać odpowiedzialnie, aby zminimalizować szkody. Pozostała część rozdziału to wycieczka po niektórych z najpoważniejszych luk w zabezpieczeniach wykrytych na przestrzeni lat oraz sposobie, w jaki radzili sobie z nimi programiści, górnicy i użytkownicy. We wczesnym dzieciństwie Bitcoin sytuacja nie była tak rygorystyczna jak obecnie.


### Odpowiedzialne ujawnianie informacji



Wyobraź sobie, że odkrywasz błąd w Bitcoin Core, który pozwala każdemu na zdalne wyłączenie węzła Bitcoin Core za pomocą specjalnie spreparowanych wiadomości sieciowych. Wyobraź sobie również, że nie jesteś złośliwy i chciałbyś, aby ten błąd pozostał niewykorzystany. Co wtedy zrobisz? Jeśli będziesz milczeć na ten temat, ktoś inny prawdopodobnie odkryje błąd, a nie możesz być pewien, że ta osoba nie będzie złośliwa.


W przypadku wykrycia błędu w zabezpieczeniach, osoba odkrywająca taki błąd powinna zastosować termin _responsible disclosure_, który jest często używany wśród deweloperów Bitcoin. Termin ten jest [wyjaśniony w Wikipedii] (https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure):


> Twórcy sprzętu i oprogramowania często potrzebują czasu i zasobów, aby naprawić swoje błędy. Często to etyczni hakerzy znajdują te błędy
podatności. Hakerzy i naukowcy zajmujący się bezpieczeństwem komputerowym uważają, że ich społecznym obowiązkiem jest uświadamianie opinii publicznej o lukach w zabezpieczeniach. Ukrywanie problemów może powodować poczucie fałszywego bezpieczeństwa. Aby tego uniknąć, zaangażowane strony koordynują i negocjują rozsądny okres czasu na naprawę podatności. W zależności od potencjalnego wpływu podatności, oczekiwanego czasu potrzebnego na opracowanie i zastosowanie awaryjnej poprawki lub obejścia oraz innych czynników, okres ten może wynosić od kilku dni do kilku miesięcy.


Oznacza to, że jeśli znajdziesz błąd bezpieczeństwa, powinieneś zgłosić go zespołowi odpowiedzialnemu za system. Ale co to oznacza w kontekście Bitcoin? Nikt nie kontroluje Bitcoin, ale obecnie istnieje centralny punkt rozwoju Bitcoin, a mianowicie repozytorium [Bitcoin Core Github](https://github.com/Bitcoin/Bitcoin). Opiekunowie wspomnianego repozytorium są odpowiedzialni za kod w nim zawarty, ale nie są odpowiedzialni za system jako całość - nikt nie jest. Niemniej jednak najlepszą praktyką jest wysłanie wiadomości e-mail na adres security@bitcoincore.org.


W wiadomości [email thread](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/015002.html) zatytułowanej "Responsible disclosure of bugs" z 2017 roku, Anthony Towns próbował podsumować to, co uważał za obecne najlepsze praktyki. Zebrał on informacje z kilku źródeł i od różnych osób, aby przedstawić swój pogląd na ten temat.




- Luki w zabezpieczeniach należy zgłaszać za pośrednictwem strony security.bitcoincore.org
- Problem krytyczny (który może zostać natychmiast wykorzystany lub jest już wykorzystywany, powodując duże szkody) zostanie rozwiązany przez:
  - wydana łatka JAK NAJSZYBCIEJ
  - szerokie powiadomienie o potrzebie aktualizacji (lub wyłączenia dotkniętych systemów)
  - minimalne ujawnienie rzeczywistego problemu, aby opóźnić ataki
- Luka niekrytyczna (ponieważ jej wykorzystanie jest trudne lub kosztowne) będzie obsługiwana przez:
  - poprawki i przeglądy podejmowane w ramach zwykłego procesu rozwoju
  - backport poprawki lub obejścia z wersji master do aktualnie wydanej wersji
- Deweloperzy będą starali się zapewnić, że publikacja poprawki nie ujawni natury luki, dostarczając proponowaną poprawkę doświadczonym deweloperom, którzy nie zostali poinformowani o luce, mówiąc im, że naprawia ona lukę i prosząc ich o zidentyfikowanie luki.
- Deweloperzy mogą zalecić innym implementacjom Bitcoin przyjęcie poprawek luk w zabezpieczeniach przed wydaniem i szerokim wdrożeniem poprawki, jeśli mogą to zrobić bez ujawniania luki; np. jeśli poprawka ma znaczące korzyści w zakresie wydajności, które uzasadniałyby jej włączenie.
- Zanim luka zostanie upubliczniona, deweloperzy zazwyczaj zalecają zaprzyjaźnionym deweloperom Altcoin, aby nadrobili zaległości w poprawkach. Dzieje się tak jednak dopiero po szerokim wdrożeniu poprawek w sieci Bitcoin.
- Deweloperzy zazwyczaj nie powiadamiają deweloperów Altcoin, którzy zachowują się w sposób wrogi (np. wykorzystują luki w zabezpieczeniach do atakowania innych lub naruszają embargo).
- Twórcy Bitcoin nie ujawnią szczegółów podatności, dopóki >80% węzłów Bitcoin nie wdroży poprawek. Osoby odkrywające podatności są zachęcane i proszone o przestrzeganie tej samej polityki. [1] [6]


Ta lista pokazuje, jak ostrożnym trzeba być podczas publikowania łatek dla Bitcoin, ponieważ sama łatka może zdradzić lukę. Czwarty punkt jest szczególnie interesujący, ponieważ wyjaśnia, jak sprawdzić, czy łatka została wystarczająco dobrze ukryta. Rzeczywiście, jeśli kilku naprawdę doświadczonych programistów nie jest w stanie wykryć luki, nawet wiedząc, że łatka ją naprawia, to prawdopodobnie inni odkryją ją dopiero po Hard.


W wątku, który doprowadził do wysłania tego e-maila, dyskutowano o tym, czy, kiedy i jak ujawniać luki w zabezpieczeniach altcoinów i innych implementacji Bitcoin. Nie ma tu jednoznacznej odpowiedzi. "Pomaganie dobrym ludziom" wydaje się rozsądną rzeczą do zrobienia, ale kto decyduje, kim oni są i gdzie należy wyznaczyć granicę? Bryan Bishop [argumentował](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014983.html), że pomaganie altcoinom, a nawet scamcoinom w obronie przed exploitami bezpieczeństwa jest moralnym obowiązkiem:


> Nie wystarczy bronić Bitcoin i jego użytkowników przed aktywnymi zagrożeniami, istnieje bardziej ogólna odpowiedzialność za ochronę wszystkich rodzajów użytkowników i różnego oprogramowania przed wieloma rodzajami zagrożeń w dowolnej formie, nawet jeśli ludzie używają głupiego i niezabezpieczonego oprogramowania, którego osobiście nie utrzymujesz, nie współtworzysz ani nie popierasz. Postępowanie z wiedzą o lukach w zabezpieczeniach to delikatna sprawa i może się zdarzyć, że otrzymasz wiedzę o poważniejszym bezpośrednim lub pośrednim wpływie niż pierwotnie opisano.

Do powyższego e-maila Town doprowadził również [post](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014977.html) Gregory'ego Maxwella, w którym argumentował, że luki w zabezpieczeniach mogą być poważniejsze, niż się wydaje:


> Wielokrotnie widziałem, jak problem z Hard do wykorzystania okazywał się trywialny, gdy znalazłeś odpowiednią sztuczkę, lub drobny problem z dosami okazał się znacznie poważniejszy.
>

> Proste błędy wydajnościowe, fachowo wdrożone, mogą być potencjalnie wykorzystane do podzielenia sieci --- Miner A i Exchange B trafiają do jednej partycji, wszyscy inni do drugiej... i podwójnego podziału.
>

> I tak dalej.  Tak więc, chociaż absolutnie zgadzam się, że różne rzeczy powinny i mogą być traktowane w różny sposób, nie zawsze jest to tak jednoznaczne. Rozsądnie jest traktować rzeczy jako poważniejsze, niż się o nich wie.

Tak więc, nawet jeśli luka wydaje się Hard do wykorzystania, najlepiej jest założyć, że jest ona łatwa do wykorzystania, a ty po prostu jeszcze nie wiesz, jak to zrobić.


Wspomina również, że "nazywanie tego wątku czymkolwiek związanym z ujawnianiem informacji jest nieco niepoprawne, ten wątek nie dotyczy ujawniania informacji. Ujawnienie jest wtedy, gdy mówisz sprzedawcy.  Ten wątek dotyczy publikacji i ma zupełnie inne implikacje. Publikacja ma miejsce wtedy, gdy jesteś pewien, że powiedziałeś potencjalnym atakującym". To ostatnie spostrzeżenie dotyczące rozróżnienia między ujawnieniem a publikacją jest bardzo ważne. Łatwa część to odpowiedzialne ujawnianie; część Hard to rozsądne publikowanie.


### Traumatyczne dzieciństwo Bitcoin



Bitcoin rozpoczął się jako jednoosobowy (przynajmniej tak sugeruje pseudonim jego twórcy) projekt, a Bitcoin początkowo miał niewielką lub żadną wartość. W związku z tym luki i poprawki błędów nie były tak rygorystycznie obsługiwane jak obecnie.


Wiki Bitcoin zawiera [listę powszechnych luk i zagrożeń](https://en.Bitcoin.it/wiki/Common_Vulnerabilities_and_Exposures) (CVE), przez które przeszedł Bitcoin. Ta sekcja stanowi małe exposé niektórych kwestii bezpieczeństwa i incydentów z wczesnych lat Bitcoin. Nie omówimy ich wszystkich, ale wybraliśmy kilka, które uważamy za szczególnie interesujące.


#### 2010-07-28: Wydać czyjeś monety (CVE-2010-5141)



W dniu 28 lipca 2010 r. osoba o pseudonimie ArtForz odkryła błąd w wersji 0.3.4, który pozwalał każdemu zabrać monety komukolwiek innemu. ArtForz *odpowiedzialnie* zgłosił to Satoshi Nakamoto i innemu deweloperowi Bitcoin o imieniu Gavin Andresen.


Problem polegał na tym, że operator skryptu `OP_RETURN` po prostu kończył wykonywanie programu, więc jeśli scriptPubKey był `<pubkey> OP_CHECKSIG` i scriptSig był `OP_1 OP_RETURN`, część programu w scriptPubKey nigdy by się nie wykonała. Jedyną rzeczą, która by się wydarzyła, byłoby umieszczenie `1` na stosie, a następnie `OP_RETURN` spowodowałoby wyjście z programu. Jakakolwiek niezerowa wartość na szczycie stosu po wykonaniu programu oznacza, że warunek wydania został spełniony. Ponieważ górny element stosu `1` jest niezerowy, wydawanie będzie OK.


Był to kod do obsługi `OP_RETURN`:


```
case OP_RETURN:
{
pc = pend;
}
break;
```

Efektem `pc = pend;` było pominięcie reszty programu, co oznaczało, że każdy skrypt blokujący w scriptPubKey byłby ignorowany. Poprawka polegała na zmianie znaczenia `OP_RETURN` tak, by zamiast tego natychmiast się nie powiodło.


```
case OP_RETURN:
{
return false;
}
break;
```


Satoshi dokonał tej zmiany lokalnie i zbudował z niej wykonywalny plik binarny z wersją 0.3.5. Następnie opublikował na forum Bitcointalk `\\*** ALERT \*** Uaktualnij do 0.3.5 ASAP`, zachęcając użytkowników do zainstalowania tej jego wersji binarnej, bez przedstawiania jej kodu źródłowego:


> Prosimy o jak najszybszą aktualizację do wersji 0.3.5!  Naprawiliśmy błąd implementacji, który umożliwiał akceptację fałszywych transakcji.  Nie akceptuj transakcji Bitcoin jako płatności do czasu aktualizacji do wersji 0.3.5!

Oryginalna wiadomość została później edytowana i nie jest już dostępna w pełnej formie. Powyższy fragment pochodzi z [cytowania odpowiedzi](https://bitcointalk.org/index.php?topic=626.msg6458#msg6458). Niektórzy użytkownicy wypróbowali plik binarny Satoshi, ale napotkali na problemy. Wkrótce potem [Satoshi napisał](https://bitcointalk.org/index.php?topic=626.msg6469#msg6469):


> Nie miałem jeszcze czasu na aktualizację SVN.  Poczekaj na 0.3.6, właśnie go buduję.  W międzyczasie możesz wyłączyć węzeł.

A 35 minut później [napisał](https://bitcointalk.org/index.php?topic=626.msg6480#msg6480):


> SVN został zaktualizowany do wersji 0.3.6.
>

> Przesyłam teraz kompilację 0.3.6 dla Windows na Sourceforge, a następnie przebuduję wersję linuksową.

W tym momencie wydawało się również, że zaktualizował oryginalny post, aby wspomnieć o wersji 0.3.6 zamiast 0.3.5:


> Prosimy o jak najszybszą aktualizację do wersji 0.3.6!  Naprawiliśmy błąd implementacji, w wyniku którego fałszywe transakcje mogły być wyświetlane jako zaakceptowane.  Nie akceptuj transakcji Bitcoin jako płatności do czasu aktualizacji do wersji 0.3.6!
>

> Jeśli nie możesz od razu zaktualizować do wersji 0.3.6, najlepiej wyłączyć węzeł Bitcoin do czasu aktualizacji.
>

> Również w 0.3.6, szybsze hashowanie:
> - optymalizacja pamięci podręcznej midstate dzięki tcatm
> - Crypto++ ASM SHA-256 dzięki BlackEye
> Całkowite przyspieszenie generowania 2,4x szybsze.
>

> Pobierz:
>

> http://sourceforge.net/projects/Bitcoin/files/Bitcoin/Bitcoin-0.3.6/
>

> Użytkownicy systemów Windows i Linux: jeśli masz wersję 0.3.5, nadal musisz zaktualizować ją do wersji 0.3.6.

Zwróć uwagę na różnicę w opisie problemu w stosunku do pierwszej wiadomości: "może być wyświetlany jako zaakceptowany" vs "może być zaakceptowany". Być może Satoshi zbagatelizował wagę błędu w swoim komunikacie, aby nie zwracać zbytniej uwagi na rzeczywisty problem. W każdym razie ludzie zaktualizowali do wersji 0.3.6 i wszystko działało zgodnie z oczekiwaniami. Ten konkretny problem został rozwiązany, o dziwo, bez strat Bitcoin.


Wiadomość Satoshi opisywała również pewną optymalizację wydajności dla Mining. Nie jest jasne, dlaczego zostało to uwzględnione w krytycznej poprawce bezpieczeństwa, możliwe, że celem było zatajenie prawdziwego problemu. Wydaje się jednak bardziej prawdopodobne, że po prostu wydał to, co znajdowało się na czele gałęzi rozwojowej repozytorium Subversion, z dodaną poprawką bezpieczeństwa.


W tamtym czasie nie było tak wielu użytkowników jak obecnie, a wartość Bitcoin była bliska zeru. Gdyby ta reakcja na błąd miała miejsce dzisiaj, zostałaby uznana za kompletne gówno z wielu powodów:



- Satoshi udostępnił binarne wydanie 0.3.5 zawierające poprawkę. Nie dostarczono żadnej łatki ani kodu, być może w celu ukrycia problemu.
- 0.3.5 [nawet nie działało](https://bitcointalk.org/index.php?topic=626.msg6455#msg6455).
- Poprawka w 0.3.6 była w rzeczywistości Hard Fork.


Inną dyskusyjną kwestią jest to, czy to dobrze, czy źle, że użytkownicy zostali poproszeni o wyłączenie swoich węzłów. Dziś nie byłoby to możliwe, ale w tamtym czasie wielu użytkowników aktywnie śledziło fora w poszukiwaniu aktualizacji i zwykle było na bieżąco. Biorąc pod uwagę, że było to możliwe, mogło to być rozsądne posunięcie.


#### 2010-08-15 Przepełnienie połączonego wyjścia (CVE-2010-5139)



W połowie sierpnia 2010 r. użytkownik forum Bitcointalk jgarzik, alias Jeff Garzik,

[odkryto, że](https://bitcointalk.org/index.php?topic=822.msg9474#msg9474) pewna transakcja na wysokości bloku 74638 miała dwa wyjścia o niezwykle wysokiej wartości:


```
"out" : [
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0xB7A73EB128D7EA3D388DB12418302A1CBAD5E890 OP_EQUALVERIFY OP_CHECKSIG"
},
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0x151275508C66F89DEC2C5F43B6F9CBE0B5C4722C OP_EQUALVERIFY OP_CHECKSIG"
}
]
```


> "Wartość out" w tym bloku #74638 jest dość dziwna:
>

> 92233720368.54277039 BTC?  Zastanawiam się, czy to UINT64_MAX?

Prawdopodobnie wystąpił błąd powodujący przepełnienie sumy dwóch wyjść int64 (nie uint64, jak przypuszczał Garzik) do wartości ujemnej -0.00997538 BTC. Niezależnie od sumy danych wejściowych, "suma" danych wyjściowych byłaby mniejsza, co sprawiłoby, że ta transakcja byłaby OK zgodnie z ówczesnym kodem.


W tym przypadku błąd został ujawniony i opublikowany poprzez rzeczywisty exploit. Niefortunnym skutkiem tego było utworzenie około 2x92 miliardów Bitcoin, co poważnie osłabiło pieniądze Supply w wysokości około 3,7 miliona monet, które istniały w tym czasie.


W powiązanym wątku [Satoshi napisał](https://bitcointalk.org/index.php?topic=823.msg9531#msg9531), że byłby wdzięczny, gdyby ludzie przestali Mining (lub *generować*, jak to wtedy nazywali):


> Pomogłoby, gdyby ludzie przestali generować.  Prawdopodobnie będziemy musieli ponownie stworzyć gałąź wokół obecnej, a im mniej generate, tym szybciej to nastąpi.
>

> Pierwsza łatka pojawi się w SVN rev 132.  Nie została jeszcze przesłana.  Najpierw usuwam kilka innych drobnych zmian, a potem wgram łatkę do tego.

Jego plan polegał na stworzeniu Soft Fork, aby unieważnić transakcje takie jak ta omawiana tutaj, a tym samym unieważnić bloki (zwłaszcza blok 74638), które zawierały takie transakcje. Niecałą godzinę później opublikował [poprawkę w rewizji 132](https://sourceforge.net/p/Bitcoin/code/132/) repozytorium Subversion i [post na forum](https://bitcointalk.org/index.php?topic=823.msg9548#msg9548) opisujący, co jego zdaniem powinni zrobić użytkownicy:


> Patch został przesłany do SVN rev 132!
>

> Na razie zalecane kroki:
> 1) Wyłączenie.
> 2) Pobierz pliki blk knightmb.  (zastąp pliki blk0001.dat i blkindex.dat)
> 3) Aktualizacja.
> 4) Powinien zacząć od mniej niż 74000 bloków. Pozwól mu ponownie pobrać resztę.
>

> Jeśli nie chcesz używać plików knightmb, możesz po prostu usunąć pliki blk*.dat, ale będzie to duże obciążenie dla sieci, jeśli wszyscy będą pobierać cały indeks bloków naraz.
>

> Wkrótce utworzę wydania.

Chciał, aby ludzie pobierali dane blokowe od konkretnego użytkownika, a mianowicie knightmb, który opublikował swoje Blockchain w takiej postaci, w jakiej pojawiły się na jego dysku, pliki blkXXXX.dat i blkindex.dat. Powodem pobierania danych Blockchain w ten sposób, w przeciwieństwie do synchronizacji od zera, było zmniejszenie wąskich gardeł przepustowości sieci.


Wiązało się z tym duże zastrzeżenie: dane pobierane przez użytkowników od knightmb [nie były weryfikowane przez oprogramowanie Bitcoin](https://Bitcoin.stackexchange.com/a/113682/69518) podczas uruchamiania. Plik blkindex.dat zawierał zestaw UTXO, a oprogramowanie akceptowało wszelkie zawarte w nim dane tak, jakby już je zweryfikowało. knightmb mógł manipulować danymi, aby dać sobie lub komukolwiek innemu trochę bitcoinów.


Ponownie, ludzie zdawali się na to zgadzać, a odwrócenie nieważnego bloku i jego następców zakończyło się sukcesem. Górnicy rozpoczęli pracę nad nowym następcą bloku [74637](https://Mempool.space/block/0000000000606865e679308edf079991764d88e8122ca9250aef5386962b6e84) i, zgodnie z Timestamp bloku, następca pojawił się o 23:53 UTC, około 6 godzin po wykryciu problemu. O godzinie 08:10 następnego dnia, 16 sierpnia, około bloku 74689, nowy łańcuch wyprzedził stary łańcuch, dlatego wszystkie niezaktualizowane węzły zostały zreorgowane, aby podążać za nowym łańcuchem. Jest to najgłębszy reorg - 52 bloki - w historii Bitcoin.


W porównaniu do sprawy OP_RETURN, ta kwestia została rozwiązana w nieco czystszy sposób:


- Brak wydania łatki tylko dla wersji binarnej
- Wydane oprogramowanie działało zgodnie z przeznaczeniem
- Nie Hard Fork


Użytkownicy zostali również poproszeni o zatrzymanie Mining podczas tego wydania. Możemy dyskutować, czy jest to dobry pomysł, czy nie, ale wyobraź sobie, że jesteś Miner i jesteś przekonany, że wszystkie bloki na szczycie złego bloku zostaną ostatecznie wymazane w głębokim reorg: dlaczego miałbyś marnować zasoby na skazane na zagładę bloki Mining?


Możesz również pomyśleć, że to trochę podejrzane, aby zrobić to, co sugeruje Nakamoto i pobrać Blockchain, w tym zestaw UTXO, z dysku Hard przypadkowego kolesia. Jeśli tak, to masz rację: to podejrzane. Ale biorąc pod uwagę okoliczności, ta awaryjna reakcja była rozsądna.


Istnieje istotna różnica między tym przypadkiem a poprzednim przypadkiem OP_RETURN: ten błąd był wykorzystywany na wolności, a zatem poprawka mogła być prostsza. W przypadku OP_RETURN musieli oni zaciemnić poprawkę i wydać publiczne oświadczenia, które nie ujawniały bezpośrednio, na czym polegał błąd.


#### 2013-03-11 Problem z blokadami DB w wersjach 0.7.2 - 0.8.0 (CVE-2013-3220)



Bardzo interesująca i wartościowa edukacyjnie kwestia pojawiła się w marcu 2013 roku. Okazało się, że Blockchain rozdzielił się (choć w poniższym cytacie użyto słowa "Fork") po bloku 225429. Szczegóły tego incydentu zostały [opisane w BIP50](https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki). W podsumowaniu napisano:


> Wydobyto i rozesłano blok, który miał większą liczbę całkowitych wejść transakcyjnych niż poprzednio. Węzły Bitcoin 0.8 były w stanie go obsłużyć, ale niektóre węzły Bitcoin sprzed 0.8 odrzuciły go, powodując nieoczekiwany Fork Blockchain. Niezgodny łańcuch pre-0.8 (od tego momentu łańcuch 0.8) miał w tym momencie około 60% mocy Mining Hash, dzięki czemu podział nie został automatycznie rozwiązany (co miałoby miejsce, gdyby łańcuch pre-0.8 przewyższył łańcuch 0.8 pod względem całkowitej pracy, zmuszając węzły 0.8 do reorganizacji do łańcucha pre-0.8).
>

> Aby jak najszybciej przywrócić kanoniczny łańcuch, BTCGuild i Slush obniżyły swoje węzły Bitcoin 0.8 do 0.7, aby ich pule również odrzuciły większy blok. Spowodowało to umieszczenie większości hashpower w łańcuchu bez większego bloku, co ostatecznie spowodowało reorganizację węzłów 0,8 do łańcucha sprzed 0,8.

Szybkie działania podjęte przez pule Mining BTCGuild i Slush były niezbędne w tej sytuacji. Były one w stanie przenieść większość mocy Hash na gałąź podziału sprzed wersji 0.8, a tym samym pomóc w przywróceniu konsensusu. Dało to deweloperom czas na opracowanie trwałej poprawki.


Bardzo interesujące w tej sprawie jest również to, że wersja 0.7.2 była niekompatybilna z samą sobą, podobnie jak w przypadku wcześniejszych wersji. Zostało to wyjaśnione w sekcji [Root cause section of BIP50](https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki#root-cause):


> Przy niewystarczająco wysokiej konfiguracji blokady BDB, stała się ona niejawnie regułą konsensusu sieciowego określającą ważność bloku (aczkolwiek
niespójna i niebezpieczna reguła, ponieważ użycie blokady może się różnić w zależności od węzła).


Krótko mówiąc, problem polega na tym, że liczba blokad bazy danych, których oprogramowanie Bitcoin Core potrzebuje do weryfikacji bloku, nie jest deterministyczna. Jeden węzeł może potrzebować X blokad, podczas gdy inny węzeł może potrzebować X+1 blokad. Węzły mają również limit liczby blokad, które może przyjąć Bitcoin. Jeśli liczba potrzebnych blokad przekroczy limit, blok zostanie uznany za nieważny. Jeśli więc X+1 przekroczy limit, ale nie X, wówczas dwa węzły podzielą Blockchain i nie zgodzą się, która gałąź jest ważna.


Wybranym rozwiązaniem, oprócz natychmiastowych działań podjętych przez oba baseny w celu przywrócenia konsensusu, było



- ograniczenie bloków zarówno pod względem rozmiaru, jak i wymaganych blokad w wersji 0.8.1
- popraw stare wersje (0.7.2 i niektóre starsze) z tymi samymi nowymi zasadami i zwiększ globalny limit blokady.


Z wyjątkiem zwiększonego limitu globalnej blokady w drugim punkcie, zasady te zostały wdrożone tymczasowo na określony czas. Plan zakładał usunięcie tych limitów po uaktualnieniu większości węzłów.


Ten Soft Fork znacznie zmniejszył ryzyko niepowodzenia konsensusu, a kilka miesięcy później, 15 maja, tymczasowe zasady zostały zgodnie dezaktywowane w całej sieci. Należy zauważyć, że ta dezaktywacja była w rzeczywistości Hard Fork, ale nie była kontrowersyjna. Co więcej, została ona wydana wraz z poprzedzającym ją Soft Fork, więc osoby korzystające z oprogramowania Soft-forked doskonale zdawały sobie sprawę, że po niej nastąpi Hard Fork. Dlatego też zdecydowana większość węzłów pozostała w konsensusie, gdy Hard Fork został aktywowany. Niestety, kilka węzłów, które nie dokonały aktualizacji, zostało utraconych w tym procesie.


Można się zastanawiać, czy dziś byłoby to wykonalne. Krajobraz Mining jest dziś bardziej złożony i, w zależności od siły Hash po obu stronach podziału, wprowadzenie łatki takiej jak ta w BIP50 może być Hard wystarczająco szybkie. Prawdopodobnie Hard będzie musiał przekonać górników z "niewłaściwej" gałęzi, aby zrezygnowali ze swoich nagród za bloki.


#### BIP66



BIP66 jest interesujący, ponieważ podkreśla znaczenie:



- dobry wybór kryptografii
- odpowiedzialne ujawnianie informacji
- wdrożenie bez ujawniania podatności
- Mining na szczycie zweryfikowanych bloków


BIP66 był propozycją zaostrzenia zasad kodowania podpisów w Bitcoin Script. Motywacją](https://github.com/Bitcoin/bips/blob/master/bip-0066.mediawiki#motivation) było umożliwienie analizowania podpisów za pomocą oprogramowania lub bibliotek innych niż OpenSSL, a nawet ostatnich wersji OpenSSL. OpenSSL jest biblioteką kryptograficzną ogólnego przeznaczenia, z której w tamtym czasie korzystał Bitcoin Core.


BIP został aktywowany 4 lipca 2015 roku. Jednakże, choć powyższe jest prawdą, BIP66 naprawia również znacznie poważniejszy problem, o którym nie wspomniano w BIP.


##### Podatność



Pełne ujawnienie tej kwestii zostało opublikowane 28 lipca 2015 r. przez Pietera Wuille'a w artykule pt

[email na listę mailingową Bitcoin-dev](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-July/009697.html):


> Witam wszystkich,
>

> Chciałbym ujawnić lukę, którą odkryłem we wrześniu 2014 r., a która stała się nie do wykorzystania po osiągnięciu 95% progu BIP66 na początku tego miesiąca.
>

> Krótki opis:
>

> Specjalnie spreparowana transakcja mogła spowodować rozwidlenie Blockchain między węzłami:
>

> - korzystanie z OpenSSL w systemach 32-bitowych i 64-bitowych systemach Windows
> - korzystanie z OpenSSL w 64-bitowych systemach innych niż Windows (Linux, OSX, ...)
> - używanie niektórych baz kodu innych niż OpenSSL do analizowania podpisów

E-mail zawiera dalsze szczegóły dotyczące tego, w jaki sposób problem został wykryty, a dokładniej, co go spowodowało. Na koniec przedstawia oś czasu wydarzeń, a my powtórzymy tutaj niektóre z najważniejszych. Niektóre z nich, jak pokazuje powyższy rysunek, zostały już opisane.


![](assets/bip66-timeline-1.webp)


Oś czasu wydarzeń związanych z BIP66. Elementy zaznaczone na czarno zostały wyjaśnione powyżej.


##### Przed odkryciem



Gdyby nikt nie wiedział o tym problemie, mógłby on zostać rozwiązany przez obecnie wycofany BIP62, który był propozycją ograniczenia możliwości manipulowania transakcjami. Wśród proponowanych zmian w BIP62 było zaostrzenie zasad konsensusu dotyczących kodowania podpisów lub "ścisłe kodowanie DER". Pieter Wuille zaproponował pewne poprawki do BIP w lipcu 2014 roku, które rozwiązałyby ten problem:


> 2014-Jul-18: Aby zasady kodowania podpisów Bitcoin nie zależały od specyficznego parsera OpenSSL, zmodyfikowałem propozycję BIP62, aby jej ścisły wymóg podpisów DER miał również zastosowanie do transakcji w wersji 1. W tamtym czasie nie wydobywano już żadnych podpisów innych niż DER w blokach, więc założono, że nie będzie to miało żadnego wpływu. Zob. https://github.com/Bitcoin/bips/pull/90 i http://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2014-July/006299.html. Nieznane w tamtym czasie, ale gdyby zostało wdrożone, rozwiązałoby to lukę.

Ze względu na szeroki zakres tego BIP, który obejmował znacznie więcej niż tylko "ścisłe kodowanie DER", był on stale zmieniany i nigdy nie był bliski wdrożenia. BIP został później wycofany, ponieważ Segregated Witness, BIP141, rozwiązał problem zmienności transakcji w inny i bardziej kompletny sposób.


##### Po odkryciu



OpenSSL wydało nowe wersje swojego oprogramowania z łatkami, które, gdyby były używane w Bitcoin od samego początku, rozwiązałyby problem. Jednak użycie jakiejkolwiek nowej wersji OpenSSL tylko w nowym wydaniu Bitcoin Core pogorszyłoby sprawę. Gregory Maxwell wyjaśnił to w innym [email thread](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-January/007097.html) w styczniu 2015 roku:


> Podczas gdy w przypadku większości aplikacji ogólnie akceptowalne jest ochocze odrzucanie niektórych podpisów, Bitcoin jest systemem konsensusu, w którym wszyscy uczestnicy muszą zasadniczo zgodzić się co do dokładnej ważności lub nieważności danych wejściowych.  W pewnym sensie spójność jest ważniejsza niż "poprawność".
> [...]
> Powyższe poprawki naprawiają jednak tylko jeden z symptomów ogólnego problemu: poleganie na oprogramowaniu, które nie zostało zaprojektowane lub rozpowszechnione do użytku w ramach konsensusu (w szczególności OpenSSL) w celu zachowania zgodnego z normami konsensusu.  Dlatego też, jako stopniowe ulepszenie, proponuję ukierunkowane Soft-Fork, aby wkrótce wymusić ścisłą zgodność z DER, wykorzystując podzbiór BIP62.

Zwraca uwagę, że używanie kodu, który nie jest przeznaczony do użytku w systemach konsensusu, stwarza poważne ryzyko i proponuje, aby Bitcoin implementował ścisłe kodowanie DER. Jest to bardzo wyraźny przykład znaczenia dobrej kryptografii selekcyjnej.


Te wydarzenia mogą sprawiać wrażenie, że Gregory Maxwell wiedział o luce, którą później opublikował Pieter Wuille, ale chciał pomóc w przemyceniu poprawki w przebraniu środka ostrożności, bez zwracania zbytniej uwagi na rzeczywisty problem. Być może tak było, ale to tylko spekulacje.


Następnie, zgodnie z propozycją Maxwella, utworzono BIP66 jako podzbiór BIP62, który określał tylko ścisłe kodowanie DER. Ten BIP został najwyraźniej szeroko zaakceptowany i wdrożony w lipcu, aczkolwiek dwa podziały Blockchain ironicznie wystąpiły z powodu *bezwalidacyjnego Mining*. Podziały te zostały omówione w następnej sekcji.


![](assets/bip66-timeline-2.webp)


Kluczowym wnioskiem z tego jest to, że BIP powinny być mniej lub bardziej *atomowe*, co oznacza, że powinny być wystarczająco kompletne, aby zapewnić coś użytecznego lub rozwiązać konkretny problem, ale wystarczająco małe, aby umożliwić szerokie wsparcie wśród użytkowników. Im więcej rzeczy umieścisz w BIP, tym mniejsza szansa na akceptację.


##### Podziały z powodu braku walidacji Mining



Niestety, historia BIP66 na tym się nie skończyła. Kiedy BIP66 został aktywowany, okazało się, że jest to dość chaotyczne, ponieważ niektórzy górnicy nie zweryfikowali bloków, które próbowali rozszerzyć. Nazywa się to Mining bez walidacji lub SPV-Mining (jak w uproszczonej weryfikacji płatności). Wiadomość ostrzegawcza została wysłana do węzłów Bitcoin z linkiem do [strony internetowej opisującej problem] (https://Bitcoin.org/en/alert/2015-07-04-spv-Mining):


> Wczesnym rankiem 4 lipca 2015 r. osiągnięto próg 950/1000 (95%). Wkrótce potem mały Miner (część niezaktualizowanych 5%) wydobył nieprawidłowy blok - co było spodziewanym zjawiskiem. Niestety, okazało się, że około połowa sieci Hash była Mining bez pełnej walidacji bloków (zwana SPV Mining) i zbudowała nowe bloki na szczycie tego nieważnego bloku.

Strona z ostrzeżeniem instruowała ludzi, aby czekali na 30 dodatkowych potwierdzeń niż normalnie, w przypadku korzystania ze starszych wersji Bitcoin Core.


Wspomniany powyżej podział nastąpił w dniu 2015-07-04 o godzinie 02:10 UTC po wysokości bloku [363730](https://Mempool.space/block/000000000000000006a320d752b46b532ec0f3f815c5dae467aff5715a6e579e). Problem ten został rozwiązany o 03:50 tego samego dnia, po wydobyciu 6 nieprawidłowych bloków. Niestety, ten sam problem powtórzył się następnego dnia, tj. 2015-07-05 o 21:50, ale tym razem nieprawidłowa gałąź trwała tylko 3 bloki.


![](assets/bip66-timeline-3.webp)

Wydarzenia, które doprowadziły do BIP66, jego wdrożenia i następstw, stanowią bardzo dobre studium przypadku dla tego, jak ostrożni muszą być deweloperzy Bitcoin. Kilka kluczowych wniosków z BIP66:



- Równowaga między otwartością a niepublikowaniem słabych punktów jest delikatna.
- Wdrażanie poprawek dla niepublikowanych luk w zabezpieczeniach to trudna gra.
- Konsensusem jest Hard.
- Oprogramowanie nieprzeznaczone dla systemów konsensusu jest generalnie ryzykowne.
- BIPy powinny być w pewnym stopniu atomowe.


### Wnioski na temat When Shit Hits The Fan



Bitcoin zawiera błędy. Osoby odkrywające błędy są zachęcane do odpowiedzialnego ujawniania ich deweloperom Bitcoin, aby mogli naprawić błąd bez ujawniania go publicznie. Najlepiej byłoby, gdyby poprawka błędu mogła być ukryta jako poprawa wydajności lub inna zasłona dymna.


Przyjrzeliśmy się niektórym z poważniejszych problemów, które pojawiły się na przestrzeni lat, i temu, jak sobie z nimi poradzono. Niektóre z nich zostały odkryte publicznie za pomocą exploitów, podczas gdy inne zostały odpowiedzialnie ujawnione i mogły zostać naprawione, zanim złośliwi aktorzy mieli szansę je wykorzystać.


## Pytania do dyskusji

<chapterId>91462ca7-f09c-55da-a5b9-3e211de31da5</chapterId>


Te pytania do dyskusji nie są tylko podsumowaniem treści zawartych w "Filozofii rozwoju Bitcoin", ale mają na celu zachęcenie cię do dalszych badań, więc pamiętaj, aby wyjść i zbadać.


Możesz sprawdzić głębię swojego zrozumienia, pisząc [mini-esej](https://www.youtube.com/watch?v=N4YjXJVzoZY) o długości 100-300 słów, wybierając temat z tej puli pytań. Jeśli chcesz uzyskać opinię na temat swojej pracy, możesz wysłać ją na adres mini-essay@planb.network, a my z przyjemnością ją przeanalizujemy.


#### Decentralizacja



- Decentralizacja to Hard. Dlaczego zadajemy sobie tyle trudu, by to zadziałało? Czy możemy zdecydować się na podejście hybrydowe, w którym niektóre części są scentralizowane, a inne nie?
- Czy decentralizacja wprowadza problem podwójnych wydatków, czy też problem podwójnych wydatków wymaga decentralizacji? Jak Satoshi rozwiązał problem podwójnych wydatków?
- W jakich aspektach Bitcoin jest nadal najbardziej podatny na cenzurę i dlaczego cenzura jest taka zła? Czy są jakieś argumenty przemawiające za cenzurą?
- Stwierdzono, że Bitcoin nie wymaga zezwolenia. Czy są jakieś inne metody płatności, które można uznać za bezzezwoleniowe?



#### Nieufność




- Nieufność jest często spektrum, a nie zjawiskiem binarnym. Które aspekty Bitcoin są raczej Trustless, a które zazwyczaj wiążą się z wyższym poziomem zaufania? Czy można je złagodzić?
- Chcesz uruchomić Full node, aby móc w pełni zweryfikować wszystkie transakcje. Pobierasz Bitcoin Core z https://Bitcoin.org/en/download. Gdzie zaufałeś, a gdzie jesteś w pełni Trustless?
- Czy można zbudować system Trustless na bazie zaufanego systemu?



#### Prywatność




- Jakie są ważne korzyści dla użytkownika, który zachowuje prywatność podczas interakcji z Bitcoin? Jakie są altruistyczne korzyści dla sieci?
- Jak ponowne wykorzystanie adresów wpływa na prywatność użytkownika?
- Bitcoin wykorzystuje model UTXO, podczas gdy niektóre alternatywne kryptowaluty wykorzystują model konta. Jakie są konsekwencje tego wyboru dla prywatności?



#### Finite Supply




- Jaki jest związek między Bitcoin z Supply a emisją monet przez Coinbase Transaction? Jaki jest związek między emisją monet a budżetem bezpieczeństwa i w jaki sposób są one sprzeczne?
- Jakie parametry mógł zmienić Satoshi, aby zmienić limit Bitcoin dla Supply? Co by się zmieniło, gdyby zdecydował się ograniczyć Supply do 1 miliona? A co z 1 bilionem?
- Dlaczego niektórzy opowiadają się za zwiększeniem Bitcoin Supply? Czy uważasz, że tak się stanie?


#### Aktualizacja



- Czym jest Speedy Trial i dlaczego konieczne było aktywowanie Taproot?
- Dlaczego potrzebujemy tak wysokiego odsetka górników do aktualizacji w softforku? Dlaczego próg nie wynosi tylko 51%?



#### Myślenie kontradyktoryjne




- Czym jest atak sybilli i co sprawia, że zdecentralizowana sieć jest na niego podatna?
- Dlaczego ważne jest, aby wszyscy gracze w sieci Bitcoin - a nie tylko deweloperzy - myśleli przeciwstawnie?



#### Otwarte źródło




- Tylko garstka opiekunów ma niezbędne uprawnienia GitHub do scalania kodu w repozytorium [Bitcoin Core](https://github.com/Bitcoin/Bitcoin). Czy nie jest to sprzeczne z siecią bez uprawnień?
- Czy proces rozwoju oprogramowania open source jest podatny na ataki sybilli? Jeśli tak, to jak można temu przeciwdziałać?
- Jakie są zalety i wady polegania na bibliotekach open source innych firm i jakie jest podejście przyjęte w Bitcoin Core?
- W jaki sposób potrzebujemy przeglądu wykraczającego poza zwykły przegląd kodu? Jak określić, ile recenzji wystarczy?
- W jaki sposób możemy zapewnić, że zawsze będzie wystarczająco dużo osób z wiedzą specjalistyczną pracujących nad Bitcoin? Co się dzieje, gdy ich nie ma i jak oceniamy ich uczciwość i intencje?



#### Skalowanie




- Argumentuje się, że sharding oferuje korzyści skalowania kosztem złożoności. Dlaczego powinniśmy lub nie powinniśmy przyjmować ulepszeń technologicznych, ponieważ są one trudne do zrozumienia, nawet jeśli wydają się technologicznie uzasadnione?
- Jakie są przykłady metod skalowania do wewnątrz wprowadzonych w Bitcoin?
- Dlaczego skalowanie pionowe jest znacznie trudniejsze w systemie zdecentralizowanym? A co ze skalowaniem poziomym?
- Wygląda na to, że nigdzie nie osiągnęliśmy konsensusu co do tego, w jaki sposób moglibyśmy przenieść cały świat na Bitcoin. Czy Satoshi nie powinien przynajmniej pomyśleć o ścieżce dotarcia tam, przed Mining, pierwszym blokiem w 2009 roku?
- Jak sklasyfikowałbyś (pionowo, poziomo, do wewnątrz lub nie jako technikę skalowania) każdą z następujących technik: sharding, zwiększenie rozmiaru bloku, SegWit, węzły SPV, scentralizowane giełdy, Lightning Network, zmniejszenie interwału bloków, Taproot, łańcuchy boczne?



# Sekcja końcowa


<partId>4b6ff4ef-b9ea-4c48-b05f-62d41a38fbbb</partId>


## Recenzje i oceny


<chapterId>d334a837-df46-4989-9cad-8d8779147dbe</chapterId>


<isCourseReview>true</isCourseReview>

## Wnioski


<chapterId>b77ed55c-b13a-430b-a212-37aab527b9e7</chapterId>


<isCourseConclusion>true</isCourseConclusion>