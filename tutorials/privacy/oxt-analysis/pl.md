---
name: OXT - Analiza łańcucha
description: Opanuj podstawy analizy łańcucha na Bitcoin
---
![cover](assets/cover.webp)


***OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, **strona OXT.me jest obecnie niedostępna**. Istnieje jednak możliwość, że narzędzie to zostanie ponownie uruchomione w nadchodzących tygodniach. W międzyczasie nadal możesz skorzystać z tego samouczka, aby zrozumieć podstawy analizy łańcucha na Bitcoin. Wszystkie przedstawione tutaj heurystyki i wzorce mają zastosowanie do transakcji Bitcoin. Mimo że narzędzia te są mniej zoptymalizowane niż OXT, można tymczasowo użyć [Mempool.space](https://Mempool.space/) lub [Bitcoin Explorer](https://bitcoinexplorer.org/), aby zastosować teoretyczne koncepcje tego artykułu w praktyce


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

W tym artykule poznasz niezbędne podstawy teoretyczne potrzebne do rozpoczęcia podstawowych analiz łańcucha na Bitcoin, a co ważniejsze, do zrozumienia sposobu działania obserwujących cię osób. Chociaż ten artykuł nie jest praktycznym samouczkiem na temat narzędzia OXT (temat ten omówimy w przyszłym samouczku), zawiera on zestaw kluczowej wiedzy na temat jego użytkowania. Dla każdego przedstawionego modelu, metryki i wskaźnika podano link do przykładowej transakcji w OXT, co pozwoli ci lepiej zrozumieć jego użycie i ćwiczyć wraz z czytaniem.


## Wprowadzenie

Jedną z funkcji pieniądza jest rozwiązanie problemu podwójnej zbieżności potrzeb. W systemie opartym na barterze, ukończenie Exchange wymaga nie tylko znalezienia osoby oferującej dobro, które zaspokaja moje potrzeby, ale także dostarczenia jej dobra o równoważnej wartości, które zaspokaja jej własne potrzeby. Znalezienie tej równowagi okazuje się skomplikowane. Dlatego uciekamy się do pieniądza, który pozwala nam przenosić wartość zarówno w przestrzeni, jak i w czasie.


Aby pieniądze mogły rozwiązać ten problem, konieczne jest, aby strona dostarczająca towar lub usługę była przekonana o swojej zdolności do późniejszego wydania tej kwoty. W związku z tym każda racjonalna osoba, która chce zaakceptować kawałek pieniądza, czy to cyfrowego, czy fizycznego, upewni się, że spełnia on dwa podstawowe kryteria:


- Moneta musi być nienaruszona i autentyczna;
- i nie mogą być wydawane podwójnie.


Jeśli używamy fizycznych pieniędzy, jest to pierwsza cecha, która jest najbardziej złożona do potwierdzenia. W różnych okresach historii integralność metalowych monet była często naruszana przez praktyki takie jak obcinanie lub wiercenie. Na przykład w starożytnym Rzymie obywatele często zdrapywali krawędzie złotych monet, aby zebrać odrobinę cennego metalu, jednocześnie zachowując je do przyszłych transakcji. To właśnie dlatego na krawędziach monet wybijano później rowki. Autentyczność jest również trudną cechą do zweryfikowania na fizycznym nośniku monetarnym. Obecnie techniki walki z fałszerstwami są coraz bardziej złożone, co zmusza sprzedawców do inwestowania w drogie systemy weryfikacji.


Z drugiej strony, ze względu na swoją naturę, podwójne wydawanie nie stanowi problemu dla walut fizycznych. Jeśli dam ci banknot o nominale 10 euro, nieodwołalnie opuszcza on moje posiadanie i wchodzi w twoje, wykluczając tym samym możliwość wielokrotnego wydawania reprezentowanych przez niego jednostek pieniężnych.

W przypadku waluty cyfrowej wyzwanie jest inne. Zapewnienie autentyczności i integralności monety jest często prostsze, ale zapewnienie braku podwójnych wydatków jest bardziej złożone. Każde dobro cyfrowe jest zasadniczo informacją. W przeciwieństwie do dóbr fizycznych, informacje nie dzielą się podczas wymiany, ale rozprzestrzeniają się poprzez mnożenie. Na przykład, jeśli wyślę ci dokument e-mailem, zostanie on zduplikowany. Użytkownik nie może z całą pewnością zweryfikować, czy usunąłem oryginalny dokument.


Jedynym sposobem na uniknięcie powielania dóbr cyfrowych jest bycie świadomym wszystkich giełd w systemie. W ten sposób można wiedzieć, kto jest właścicielem czego i aktualizować konta wszystkich osób w oparciu o dokonane transakcje. Tak właśnie robi się na przykład z pieniędzmi skryptowymi. Kiedy płacisz 10 euro sprzedawcy kartą kredytową, bank odnotowuje ten Exchange i aktualizuje Ledger.


W Bitcoin zapobieganie podwójnemu wydawaniu odbywa się w ten sam sposób. Ma na celu potwierdzenie braku transakcji, która już wydała dane monety. Jeśli nigdy nie zostały one użyte, możemy być pewni, że nie dojdzie do podwójnego wydania. Jest to słynne zdanie Satoshi Nakamoto w Białej Księdze: "*Jedynym sposobem na potwierdzenie braku transakcji jest bycie świadomym wszystkich transakcji*"


W przeciwieństwie do modelu bankowego, w Bitcoin nie chcemy ufać centralnemu podmiotowi. Dlatego wszyscy użytkownicy muszą być w stanie potwierdzić brak podwójnych wydatków, bez polegania na stronie trzeciej. W związku z tym każdy musi być świadomy wszystkich transakcji Bitcoin.


To właśnie to publiczne rozpowszechnianie informacji komplikuje ochronę prywatności w Bitcoin. W tradycyjnym systemie bankowym teoretycznie tylko instytucja finansowa jest świadoma dokonywanych transakcji. Jednak w Bitcoin wszyscy użytkownicy są informowani o wszystkich transakcjach za pośrednictwem swoich węzłów.


Ze względu na to ograniczenie rozpowszechniania, model prywatności Bitcoin różni się od modelu systemu bankowego. W tym ostatnim transakcje są powiązane z tożsamością użytkownika, ale przepływ informacji jest odcięty między zaufaną stroną trzecią a opinią publiczną. Innymi słowy, twój bankier wie, że każdego ranka kupujesz bagietkę w lokalnej piekarni, ale twój sąsiad nie jest świadomy wszystkich tych transakcji. W przypadku Bitcoin, ponieważ przepływ informacji nie może zostać przerwany między transakcjami a domeną publiczną, model prywatności opiera się na oddzieleniu tożsamości użytkownika od samych transakcji.

![analysis](assets/en/1.webp)

*Schemat zainspirowany Satoshi Nakamoto w Białej Księdze: Bitcoin: A Peer-to-Peer Electronic Cash System, sekcja 10 "Prywatność "*

Ponieważ transakcje Bitcoin są upubliczniane, możliwe staje się ustalenie powiązań między nimi w celu uzyskania informacji o zaangażowanych stronach. Działalność ta stanowi nawet specjalizację samą w sobie, powszechnie nazywaną "analizą łańcucha". W tym artykule zapraszam do zapoznania się z podstawami analizy łańcucha, aby zrozumieć, w jaki sposób śledzone są twoje bitcoiny.


Większość firm specjalizujących się w analizie łańcuchów działa jako czarne skrzynki i nie ujawnia swoich metodologii. Dlatego trudno jest uzyskać informacje na temat tej praktyki. Pisząc ten artykuł, opierałem się głównie na kilku dostępnych otwartych zasobach:


- Większość mojego artykułu pochodzi z serii czterech artykułów zatytułowanych: [Understanding Bitcoin Privacy with OXT](https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), opracowanych przez Samourai Wallet w 2021 roku;
- Korzystałem również z różnych raportów [OXT Research] (https://medium.com/oxt-research), a także z ich bezpłatnego narzędzia do analizy łańcucha;
- Mówiąc szerzej, moja wiedza pochodzi z różnych tweetów i treści od [@LaurentMT](https://twitter.com/LaurentMT) i [@ErgoBTC](https://twitter.com/ErgoBTC);
- Zainspirował mnie również [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji), w którym brałem udział razem z [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___) i [@LaurentMT](https://twitter.com/LaurentMT).


Chciałbym podziękować ich autorom, deweloperom i producentom. Bez ich różnorodnej zawartości i oprogramowania ten artykuł by nie powstał. Dziękuję również recenzentom, którzy skrupulatnie poprawili ten tekst i zaszczycili mnie swoimi fachowymi radami:


- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).


*Dla Twojej informacji, na końcu artykułu dodałem minisłownik techniczny, aby zdefiniować niektóre terminy. Jeśli zobaczysz niezrozumiałe słowo z gwiazdką, jego definicja znajduje się na dole strony*


## Czym jest analiza łańcuchowa?

Analiza łańcuchowa to praktyka obejmująca wszystkie metody śledzenia przepływów Bitcoin na Blockchain. Ogólnie rzecz biorąc, analiza łańcuchowa opiera się na obserwacji cech w próbkach poprzednich transakcji. Następnie polega na zidentyfikowaniu tych samych cech w transakcji, którą chcemy przeanalizować i wydedukowaniu wiarygodnych interpretacji. Ta metoda rozwiązywania problemów, oparta na praktycznym podejściu do znalezienia wystarczająco dobrego rozwiązania, nazywana jest heurystyką.


Dla uproszczenia, analiza łańcucha odbywa się w dwóch głównych krokach:

1. Identyfikacja znanych cech;

2. Dedukcja hipotez.


Jednym z celów analizy łańcucha jest pogrupowanie różnych działań na Bitcoin w celu określenia unikalności użytkownika, który je wykonał. Następnie możliwe będzie podjęcie próby powiązania tej wiązki działań z rzeczywistą tożsamością.


Pamiętacie moje wprowadzenie. Wyjaśniłem, dlaczego model prywatności Bitcoin pierwotnie opierał się na oddzieleniu tożsamości użytkownika od jego transakcji. W związku z tym kuszące byłoby myślenie, że analiza łańcuchowa jest niepotrzebna, ponieważ nawet jeśli uda się pogrupować działania On-Chain, nie można ich powiązać z prawdziwą tożsamością. Teoretycznie stwierdzenie to jest prawdziwe. Pary kluczy kryptograficznych są używane do ustalania warunków dla UTXO. Zasadniczo te pary kluczy nie ujawniają żadnych informacji o tożsamości ich posiadaczy. Tak więc, nawet jeśli uda się pogrupować działania związane z różnymi parami kluczy, nie mówi nam to nic o podmiocie stojącym za tymi działaniami.


Praktyczna rzeczywistość jest jednak znacznie bardziej złożona. Istnieje wiele zachowań, które stwarzają ryzyko powiązania prawdziwej tożsamości z aktywnością On-Chain. W analizie nazywa się to punktem wejścia i jest ich wiele. Najczęstszym z nich jest oczywiście KYC (Know Your Customer). Jeśli wypłacasz swoje bitcoiny z regulowanej platformy na jeden z osobistych adresów odbiorczych, niektórzy ludzie są w stanie powiązać twoją tożsamość z tym Address. Mówiąc szerzej, punktem wejścia może być dowolna forma interakcji między prawdziwym życiem a transakcją Bitcoin. Na przykład, jeśli opublikujesz otrzymany Address w swoich sieciach społecznościowych, może to być punkt wejścia do analizy. Jeśli dokonasz płatności w bitcoinach swojemu piekarzowi, może on powiązać twoją twarz (która jest częścią twojej tożsamości) z Bitcoin Address.

Te punkty wejścia są niemal nieuniknione podczas korzystania z Bitcoin. Chociaż można starać się ograniczyć ich zakres, pozostaną one obecne. Dlatego tak ważne jest połączenie metod mających na celu ochronę prywatności. Podczas gdy utrzymanie akceptowalnego rozdziału między prawdziwą tożsamością a transakcjami jest godnym pochwały podejściem, pozostaje ono niewystarczające. Rzeczywiście, jeśli wszystkie działania On-Chain można zgrupować razem, to nawet najmniejszy punkt wejścia może zagrozić pojedynczemu Layer prywatności, który ustanowiłeś.


W związku z tym konieczne jest również zajęcie się analizą łańcucha w naszym korzystaniu z Bitcoin. W ten sposób możemy zminimalizować agregację naszych działań i ograniczyć wpływ punktu wejścia na naszą prywatność. Właśnie, aby lepiej przeciwdziałać analizie łańcuchowej, jakie jest lepsze podejście niż zapoznanie się z metodami stosowanymi w analizie łańcuchowej? Jeśli chcesz wiedzieć, jak poprawić swoją prywatność w Bitcoin, musisz zrozumieć te metody. Pozwoli ci to lepiej zrozumieć techniki takie jak [CoinJoin](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-samourai-Wallet-e566803d-ab3f-4d98-9136-5462009262ef) lub [PayJoin](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f) i ograniczyć błędy, które możesz popełnić.


W tym przypadku możemy wyciągnąć analogię z kryptografią i kryptoanalizą. Dobry kryptograf jest przede wszystkim dobrym kryptoanalitykiem. Aby wyobrazić sobie nowy algorytm szyfrowania, trzeba wiedzieć, z jakimi atakami będzie musiał się zmierzyć, a także zbadać, dlaczego poprzednie algorytmy zostały złamane. Ta sama zasada dotyczy prywatności w Bitcoin. Zrozumienie metod analizy łańcucha jest kluczem do ochrony przed nim. Dlatego oferuję ci ten artykuł.


Kluczowe jest zrozumienie, że analiza łańcucha nie jest nauką ścisłą. Opiera się na heurystyce pochodzącej z wcześniejszych obserwacji lub logicznych interpretacji. Zasady te pozwalają na uzyskanie dość wiarygodnych wyników, ale nigdy z absolutną precyzją. Innymi słowy, analiza łańcuchowa zawsze wiąże się z pewnym wymiarem prawdopodobieństwa w wyciąganych wnioskach. Możemy oszacować z mniejszą lub większą pewnością, że dwa adresy należą do tego samego podmiotu, ale całkowita pewność zawsze będzie poza zasięgiem.


Cały cel analizy łańcuchowej polega właśnie na agregacji różnych heurystyk w celu zminimalizowania ryzyka błędu. Jest to w pewnym sensie gromadzenie dowodów, które pozwalają nam zbliżyć się do rzeczywistości.


Te słynne heurystyki można podzielić na różne kategorie, które szczegółowo omówimy:


- Wzorce transakcji (lub modele transakcji);
- Wewnętrzna heurystyka transakcji;
- Zewnętrzna heurystyka transakcji.


Warto zauważyć, że pierwsze dwie heurystyki Bitcoin zostały sformułowane przez samego Satoshi Nakamoto. Omawia je w części 10 Białej Księgi. Jak zobaczymy później, interesujące jest zaobserwowanie, że te dwie heurystyki nadal utrzymują przewagę w analizie łańcucha. Są to:


- common Input Ownership Heuristic (CIOH);
- i ponowne wykorzystanie Address.


Przeanalizujmy razem obserwowalne cechy i interpretacje, które można wyciągnąć w celu przeprowadzenia analizy.


## Wzorce transakcji (lub modele transakcji)

Wzorzec transakcji to po prostu typowy model transakcji, który można znaleźć na Blockchain, którego interpretacja jest prawdopodobnie znana. Podczas badania wzorców skupimy się na pojedynczej transakcji, którą przeanalizujemy na wysokim poziomie. Innymi słowy, przyjrzymy się tylko liczbie wejść i wyjść, bez zagłębiania się w bardziej szczegółowe szczegóły lub środowisko. Na podstawie zaobserwowanego modelu będziemy w stanie zinterpretować charakter transakcji. Następnie poszukamy cech charakterystycznych dla jej struktury i wydedukujemy interpretację.


### Proste wysłanie (lub prosta płatność)

Model ten charakteryzuje się konsumpcją jednego lub więcej UTXO jako danych wejściowych i produkcją dwóch UTXO jako danych wyjściowych.


![analysis](assets/en/2.webp)


Interpretacja tego modelu jest taka, że mamy do czynienia z transakcją wysyłania lub płatności. Użytkownik wykorzystał własne UTXO jako dane wejściowe, aby zaspokoić płatność UTXO i zmianę UTXO (zmiana wraca do tego samego użytkownika). Wiemy zatem, że obserwowany użytkownik prawdopodobnie nie jest już w posiadaniu jednego z dwóch UTXO na wyjściu (płatność), ale nadal jest w posiadaniu drugiego UTXO (zmiana).


W tym momencie nie możemy określić, które dane wyjściowe reprezentują UTXO, ponieważ nie jest to celem tego modelu. Będziemy w stanie to zrobić, opierając się na heurystyce, którą przeanalizujemy w dalszej części. Na tym etapie nasz cel ogranicza się do zidentyfikowania charakteru danej transakcji, która w tym przypadku jest prostym wysłaniem.


Na przykład, oto transakcja Bitcoin, która przyjmuje prosty wzorzec wysyłania:

### Sweep ("zamiatać" w języku angielskim)

Model ten charakteryzuje się zużyciem pojedynczego UTXO jako wkładu i produkcją pojedynczego UTXO jako wyjścia.


![analysis](assets/en/3.webp)


Interpretacja tego modelu jest taka, że mamy do czynienia z autotransferem. Użytkownik przeniósł swoje bitcoiny do siebie, do innego Address, którego jest właścicielem. Rzeczywiście, ponieważ nie ma żadnej zmiany w transakcji, jest bardzo mało prawdopodobne, że mamy do czynienia z płatnością. Wiemy zatem, że obserwowany użytkownik prawdopodobnie nadal jest w posiadaniu tego UTXO.


Na przykład, oto transakcja Bitcoin, która przyjmuje wzór zamiatania:

[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://Mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)


Jednak ten rodzaj wzorca może również ujawnić samodzielny przelew na konto Exchange (platforma kryptowalutowa Exchange). Badanie znanych adresów i kontekstu transakcji pozwoli nam ustalić, czy jest to przelew na rachunek własny Wallet, czy wypłata na platformę.


### Konsolidacja

Model ten charakteryzuje się zużyciem kilku UTXO jako danych wejściowych i produkcją pojedynczego UTXO jako danych wyjściowych.


![analysis](assets/en/4.webp)


Interpretacja tego modelu jest taka, że mamy do czynienia z konsolidacją. Jest to powszechna praktyka wśród użytkowników Bitcoin, mająca na celu połączenie kilku UTXO w oczekiwaniu na możliwy wzrost opłat transakcyjnych. Wykonując tę operację w okresie, gdy opłaty są niskie, można zaoszczędzić na przyszłych opłatach.


Możemy wywnioskować, że użytkownik stojący za tą transakcją był prawdopodobnie w posiadaniu wszystkich UTXO na wejściu i nadal jest w posiadaniu UTXO na wyjściu. Dlatego jest to z pewnością transfer własny.


Podobnie jak w przypadku zamiatania, ten typ wzorca może również ujawnić samodzielny przelew na konto Exchange. Badanie znanych adresów i kontekstu transakcji pozwoli nam ustalić, czy jest to konsolidacja na własny rachunek Wallet, czy wypłata na platformę.


Na przykład, oto transakcja Bitcoin, która przyjmuje wzorzec konsolidacji:

[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://Mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)

### Model wydatków wsadowych

Model ten charakteryzuje się konsumpcją kilku UTXO jako danych wejściowych (często tylko jednego) i produkcją wielu UTXO jako danych wyjściowych.


![analysis](assets/en/5.webp)


Interpretacja tego modelu jest taka, że mamy do czynienia z wydatkami wsadowymi. Jest to praktyka, która prawdopodobnie ujawnia znaczącą działalność gospodarczą, taką jak na przykład Exchange. Wydatki wsadowe pozwalają tym podmiotom zaoszczędzić na opłatach, łącząc swoje wydatki w jedną transakcję.


Możemy wywnioskować, że dane wejściowe UTXO pochodzą od firmy prowadzącej znaczącą działalność gospodarczą i że dane wyjściowe UTXO będą rozproszone. Niektóre będą należeć do klientów firmy. Inne mogą trafić do firm partnerskich. Wreszcie, z pewnością nastąpi zmiana, która powróci do firmy emitującej.


Na przykład, oto transakcja Bitcoin, która przyjmuje wzorzec wydatków wsadowych:

[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://Mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)


### Transakcje specyficzne dla protokołu

Wśród wzorców transakcji możemy również zidentyfikować modele, które ujawniają użycie określonego protokołu. Na przykład coinjoiny Whirlpool będą miały łatwą do zidentyfikowania strukturę, która pozwoli je odróżnić od innych klasycznych transakcji.


![analysis](assets/en/6.webp)


Analiza tego wzorca sugeruje, że prawdopodobnie mamy do czynienia z transakcją opartą na współpracy. Możliwe jest również zaobserwowanie CoinJoin. Jeśli ta druga hipoteza okaże się trafna, to liczba wyjść może zapewnić nam przybliżone oszacowanie liczby uczestników.


Na przykład, oto transakcja Bitcoin, która przyjmuje wzór transakcji współpracy typu CoinJoin:

[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://Mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)


Istnieje wiele innych protokołów, które mają swoje własne specyficzne struktury. W ten sposób możemy wyróżnić na przykład transakcje typu Wabisabi lub Stamps.


## Heurystyka transakcji wewnętrznych

Wewnętrzna heurystyka to specyficzna cecha zidentyfikowana w samej transakcji, bez konieczności badania jej otoczenia, co pozwala nam na dokonywanie dedukcji. W przeciwieństwie do wzorców, które koncentrują się na ogólnej strukturze transakcji, heurystyka wewnętrzna opiera się na zestawie danych, które można wyodrębnić. Obejmuje to:


- Kwoty różnych UTXO zarówno przychodzących, jak i wychodzących;
- Wszystko związane ze skryptami: odbieranie adresów, wersjonowanie, locktimes...


Ogólnie rzecz biorąc, ten rodzaj heurystyki pozwala nam zidentyfikować zmianę w konkretnej transakcji. W ten sposób możemy kontynuować śledzenie podmiotu w wielu różnych transakcjach.


Jeszcze raz przypominam, że te heurystyki nie są absolutnie precyzyjne. Pojedynczo pozwalają nam jedynie zidentyfikować prawdopodobne scenariusze. Kumulacja kilku heurystyk przyczynia się do zmniejszenia niepewności, ale nigdy nie eliminuje jej całkowicie.


### Wewnętrzne podobieństwa

Ta heurystyka obejmuje badanie podobieństw między wejściami i wyjściami tej samej transakcji. Jeśli ta sama cecha jest obserwowana na wejściach i tylko na jednym z wyjść transakcji, to jest prawdopodobne, że to wyjście stanowi zmianę.


Najbardziej oczywistą cechą jest ponowne użycie Address w tej samej transakcji.


![analysis](assets/en/7.webp)


Ta heurystyka pozostawia niewiele miejsca na wątpliwości. O ile ich klucz prywatny nie został naruszony, ten sam odbierający Address nieuchronnie ujawnia aktywność pojedynczego użytkownika. Wynikająca z tego interpretacja jest taka, że zmiana transakcji jest wynikiem z tym samym Address co dane wejściowe. Pozwala nam to na dalsze śledzenie osoby na podstawie tej zmiany.


Na przykład, oto transakcja, w której można zastosować tę heurystykę:

[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://Mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)


Te podobieństwa między danymi wejściowymi i wyjściowymi nie kończą się na ponownym użyciu Address. Każde podobieństwo w użyciu skryptów może pozwolić na zastosowanie heurystyki. Na przykład czasami można zaobserwować to samo wersjonowanie między danymi wejściowymi a jednym z wyjść transakcji.


![analysis](assets/en/8.webp)

Na tym diagramie widzimy, że wejście numer 0 odblokowuje skrypt P2WPKH (SegWit V0 zaczynający się od "bc1q"). Wyjście numer 0 używa skryptu tego samego typu. Jednak wyjście numer 1 używa skryptu P2TR (SegWit V1 zaczynającego się od "bc1p"). Interpretacja tej cechy jest taka, że jest prawdopodobne, że Address z tym samym wersjonowaniem co dane wejściowe jest zmienionym Address. W związku z tym nadal należy do tego samego użytkownika.

Oto transakcja, w której można zastosować tę heurystykę:

[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://Mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)


W tej transakcji widzimy, że numer wejściowy 0 i numer wyjściowy 1 używają skryptów P2WPKH (SegWit V0), podczas gdy numer wyjściowy 0 używa innego typu skryptu, P2PKH (Legacy).


### Płatności w zaokrągleniu

Inną wewnętrzną heurystyką, która może pomóc nam zidentyfikować zmianę, jest okrągła liczba. Ogólnie rzecz biorąc, w obliczu prostego wzorca płatności (1 wejście i 2 wyjścia), jeśli jedno z wyjść wydaje okrągłą kwotę, to reprezentuje płatność.


![analysis](assets/en/9.webp)


W procesie eliminacji, jeśli jedno wyjście reprezentuje płatność, drugie reprezentuje zmianę. Dlatego możemy zinterpretować, że jest prawdopodobne, że użytkownik na wejściu nadal posiada dane wyjściowe zidentyfikowane jako zmiana.


Należy zauważyć, że ta heurystyka nie zawsze ma zastosowanie, ponieważ większość płatności jest nadal dokonywana w jednostkach waluty fiducjarnej. Rzeczywiście, gdy sprzedawca we Francji akceptuje Bitcoin, zazwyczaj nie wyświetla stabilnych cen w Sats. Woleliby raczej dokonać konwersji między ceną w euro a kwotą w bitcoinach do zapłaty. W związku z tym w wyniku transakcji nie powinna pojawić się okrągła liczba. Niemniej jednak analityk mógłby spróbować dokonać tej konwersji, biorąc pod uwagę kurs Exchange obowiązujący w momencie transmisji transakcji w sieci.


Jeśli pewnego dnia Bitcoin stanie się preferowaną jednostką rozliczeniową na naszych giełdach, ta heurystyka może stać się jeszcze bardziej przydatna do analizy.


Na przykład, oto transakcja, w której można zastosować tę heurystykę:

### Duże wydatki


Gdy w prostym modelu płatności wykryta zostanie wystarczająco duża różnica między dwoma wynikami transakcji, można oszacować, że większy wynik jest prawdopodobnie zmianą.


![analysis](assets/en/10.webp)


Ta heurystyka największej wydajności jest prawdopodobnie najbardziej nieprecyzyjna ze wszystkich. Jeśli zostanie zidentyfikowana samodzielnie, jest dość słaba. Cechę tę można jednak połączyć z innymi heurystykami, aby zmniejszyć niepewność naszej interpretacji.


Na przykład, jeśli badamy transakcję obejmującą produkcję o okrągłej kwocie i inną produkcję o większej kwocie, wspólne zastosowanie heurystyki płatności okrągłych i tej dotyczącej największej produkcji pozwala nam zmniejszyć nasz poziom niepewności.


Na przykład, oto transakcja, w której można zastosować tę heurystykę:

[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://Mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)


## Heurystyka zewnętrzna dla transakcji

Badanie heurystyki zewnętrznej polega na analizie podobieństw, wzorców i cech niektórych Elements, które nie są nieodłącznie związane z samą transakcją. Innymi słowy, jeśli wcześniej ograniczaliśmy się do wykorzystywania Elements nieodłącznie związanych z transakcją za pomocą heurystyki wewnętrznej, teraz rozszerzamy nasze pole analizy na środowisko transakcji dzięki heurystyce zewnętrznej.


### Ponowne użycie Address

Jest to jedna z najbardziej znanych heurystyk wśród Bitcoinerów. Ponowne użycie Address pozwala na ustanowienie powiązania między różnymi transakcjami i różnymi UTXO. Jest to obserwowane, gdy Bitcoin otrzymujący Address jest używany wielokrotnie.


Interpretacja ponownego użycia Address jest taka, że wszystkie UTXO zablokowane na tym Address należą (lub należały) do tego samego podmiotu. Ta heurystyka pozostawia niewiele miejsca na niepewność. Kiedy zostanie zidentyfikowana, interpretacja, która następuje, ma duże szanse na odpowiadanie rzeczywistości.

Jak wyjaśniono we wstępie, heurystyka ta została odkryta przez samego Satoshi Nakamoto. W Białej Księdze wyraźnie wspomina o rozwiązaniu, które ma uniemożliwić użytkownikom jej wytworzenie, czyli po prostu użycie nowego Address dla każdej nowej transakcji: "*Jako dodatkowy firewall, dla każdej transakcji można użyć nowej pary kluczy, aby nie były one powiązane ze wspólnym właścicielem."


Przykładem może być Address użyty ponownie w wielu transakcjach:

[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://Mempool.space/Address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)


### Podobieństwo skryptów i odcisków palców Wallet

Poza ponownym wykorzystaniem Address istnieje wiele innych heurystyk, które mogą łączyć akcje z tym samym Wallet lub klastrem adresów.


Po pierwsze, analityk może wykorzystać podobieństwa w użyciu skryptów. Na przykład niektóre skrypty mniejszościowe, takie jak Multisig, mogą być łatwiejsze do wykrycia niż skrypty SegWit V0. Im większa grupa, w której się ukrywamy, tym trudniej nas wykryć. To właśnie dlatego w protokole CoinJoin Whirlpool wszyscy uczestnicy używają dokładnie tego samego typu skryptu.


W szerszym ujęciu analityk może również skupić się na charakterystycznych odciskach palców Wallet. Są to specyficzne procesy użytkowania, które można próbować zidentyfikować w celu wykorzystania ich jako heurystyki śledzenia. Innymi słowy, jeśli zaobserwuje się nagromadzenie tych samych cech wewnętrznych w transakcjach przypisanych do śledzonego podmiotu, można spróbować zidentyfikować te same cechy w innych transakcjach.


Na przykład można zidentyfikować, że śledzony użytkownik systematycznie wysyła swoje zmiany na adresy P2TR* (bc1p...). Jeśli ten proces się powtarza, można go wykorzystać jako heurystykę do kontynuowania naszej analizy. Można również użyć innych odcisków palców, takich jak kolejność UTXO, umieszczenie zmiany w wyjściach, sygnalizacja RBF (Replace-by-fee), a nawet numer wersji i czas blokady.

Jak podaje [@LaurentMT](https://twitter.com/LaurentMT) w [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (podcast frankofoński), użyteczność odcisków palców Wallet w analizie łańcucha znacznie wzrasta w czasie. Rzeczywiście, rosnąca liczba typów skryptów i coraz bardziej stopniowe wdrażanie tych nowych funkcji przez oprogramowanie Wallet podkreślają różnice. Zdarza się nawet, że można dokładnie zidentyfikować oprogramowanie używane przez śledzony podmiot. Dlatego ważne jest, aby zrozumieć, że badanie odcisku palca Wallet jest szczególnie istotne dla ostatnich transakcji, bardziej niż dla tych zainicjowanych na początku 2010 roku.

Podsumowując, odcisk palca może być dowolną konkretną praktyką, wykonywaną automatycznie przez Wallet lub ręcznie przez użytkownika, którą można znaleźć w innych transakcjach, aby pomóc w naszej analizie.


### CIOH

CIOH, czyli "Common Input Ownership Heuristic", co można przetłumaczyć jako "heurystyka wspólnego Ownership danych wejściowych" lub "heurystyka wspólnego wydatkowania", to heurystyka stwierdzająca, że gdy transakcja ma wiele danych wejściowych, prawdopodobnie wszystkie pochodzą od jednego podmiotu. W związku z tym ich Ownership jest wspólny.


Aby zastosować CIOH, należy najpierw zaobserwować transakcję, która ma wiele wejść. Mogą to być zarówno dwa, jak i trzydzieści wejść. Po zauważeniu tej cechy należy sprawdzić, czy transakcja nie pasuje do znanego wzorca. Na przykład, jeśli ma 5 wejść z mniej więcej taką samą kwotą i 5 wyjść z dokładnie taką samą kwotą, wiemy, że jest to struktura CoinJoin Whirlpool. Dlatego nie można zastosować CIOH.


Jeśli jednak transakcja nie pasuje do żadnego znanego wzorca transakcji opartej na współpracy, można zinterpretować, że wszystkie dane wejściowe prawdopodobnie pochodzą od tego samego podmiotu. Może to być bardzo przydatne do rozszerzenia już znanego klastra lub do dalszego śledzenia.


![analysis](assets/en/11.webp)


CIOH został odkryty przez Satoshi Nakamoto. Omawia to w części 10 Białej Księgi: "*[...] powiązanie jest nieuniknione w przypadku transakcji z wieloma wejściami, które z konieczności ujawniają, że ich wejścia należały do tego samego właściciela. Ryzyko polega na tym, że jeśli właściciel klucza zostanie ujawniony, linki mogą ujawnić inne transakcje, które należały do tego samego właściciela *"

Szczególnie fascynujące jest to, że Satoshi Nakamoto, jeszcze przed oficjalnym uruchomieniem Bitcoin, zidentyfikował już dwie główne luki w prywatności użytkowników, a mianowicie CIOH i ponowne wykorzystanie Address. Taka dalekowzroczność jest dość niezwykła, ponieważ te dwie heurystyki pozostają, nawet dzisiaj, najbardziej przydatne w analizie łańcucha.


### Dane off-chain

Oczywiście analiza łańcucha nie ogranicza się do danych On-Chain. Wszelkie dane z poprzedniej analizy lub dostępne w Internecie mogą być również wykorzystane do udoskonalenia analizy.


Na przykład, jeśli zaobserwuje się, że śledzone transakcje są systematycznie nadawane z tego samego węzła Bitcoin i można zidentyfikować jego adres IP Address, może być możliwe wykrycie innych transakcji od tego samego podmiotu.


Analityk ma również możliwość polegania na analizach wcześniej udostępnionych jako open source lub na własnych wcześniejszych analizach. Być może można znaleźć dane wyjściowe, które wskazują na klaster adresów, które zostały już zidentyfikowane. Czasami można również polegać na danych wyjściowych wskazujących na Exchange, ponieważ adresy tych platform są ogólnie znane.


Podobnie można przeprowadzić analizę poprzez eliminację. Na przykład, jeśli podczas analizy transakcji z dwoma wyjściami, jedno z nich jest powiązane ze znanym, ale odrębnym klastrem adresów od śledzonej jednostki, wówczas można zinterpretować, że drugie wyjście prawdopodobnie reprezentuje zmianę.


Analiza łańcuchowa obejmuje również część OSINT (Open Source Intelligence), która jest nieco bardziej ogólna w przypadku wyszukiwania w Internecie. Dlatego odradza się publikowanie adresów odbiorczych bezpośrednio w mediach społecznościowych lub na stronie internetowej, niezależnie od tego, czy pod pseudonimem, czy nie.


### Modele czasowe

Może nie od razu się o tym myśli, ale pewne ludzkie zachowania są rozpoznawalne On-Chain. Najbardziej przydatny w badaniu jest wzorzec snu! Tak, kiedy śpisz, prawdopodobnie nie nadajesz transakcji Bitcoin. Ponieważ zazwyczaj śpimy mniej więcej w tych samych godzinach, w analizie On-Chain często stosuje się analizy czasowe. Polega ona po prostu na rejestrowaniu czasu, w którym transakcje danego podmiotu są transmitowane do sieci Bitcoin. Analiza tych wzorców czasowych pozwala nam wywnioskować wiele informacji.

Przede wszystkim analiza czasowa może czasami zidentyfikować charakter śledzonego podmiotu. Jeśli zaobserwujemy, że transakcje są transmitowane konsekwentnie przez 24 godziny, może to wskazywać na silną działalność gospodarczą. Podmiotem stojącym za tymi transakcjami jest prawdopodobnie firma, potencjalnie międzynarodowa i być może posiadająca zautomatyzowane procedury wewnętrzne.


Na przykład, rozpoznałem ten wzorzec kilka tygodni temu, analizując transakcję, która omyłkowo przydzieliła 19 bitcoinów w opłatach. Prosta analiza czasowa pozwoliła mi postawić hipotezę, że mamy do czynienia ze zautomatyzowaną usługą, a zatem prawdopodobnie dużym podmiotem, takim jak Exchange: https://twitter.com/Loic_Pandul/status/1701127409712452072


Rzeczywiście, kilka dni później odkryto, że środki należały do PayPal, za pośrednictwem Paxos Exchange.


I odwrotnie, jeśli widzimy, że wzorzec czasowy jest raczej rozłożony na 16 określonych godzin, to można oszacować, że mamy do czynienia z indywidualnym użytkownikiem lub być może lokalną firmą, w zależności od wymienianych wolumenów.


Oprócz charakteru obserwowanego podmiotu, wzorzec czasowy może również dać nam przybliżoną lokalizację użytkownika. W ten sposób możemy skorelować inne transakcje i wykorzystać Timestamp jako dodatkową heurystykę, którą można dodać do naszej analizy.


Dla przykładu, na wielokrotnie używanym Address, o którym wspomniałem wcześniej, można zaobserwować, że transakcje, zarówno przychodzące, jak i wychodzące, koncentrują się w przedziale 13 godzin.

![analysis](assets/notext/12.webp)

*Kredyt: OXT*


Przedział ten prawdopodobnie odpowiada Europie, Afryce lub Bliskiemu Wschodowi. Można zatem zinterpretować, że użytkownik stojący za tymi transakcjami mieszka właśnie tam.


W innym rejestrze jest to również analiza czasowa tego typu, która pozwoliła na postawienie hipotezy, że Satoshi Nakamoto nie działał z Japonii, ale faktycznie ze Stanów Zjednoczonych: [https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f)


### Analiza objętości

Inną zewnętrzną heurystyką, którą można wykorzystać, jest analiza wolumenów obrotu. W oparciu o kwoty obecne w każdej transakcji przypisanej do podmiotu, informacje te mogą być wykorzystane jako dodatkowa heurystyka dla pozostałej części analizy.

Ta heurystyka jest oczywiście dość słaba, ale może pomóc zmniejszyć niepewność, gdy zostanie dodana do innych heurystyk.


## Jak zabezpieczyć się przed analizą łańcucha?

Jako użytkownik Bitcoin masz prawo do ochrony swojej prywatności. Wynika to z naturalnych praw do posiadania i dysponowania sobą, które są nieodłączne dla każdej osoby, niezależnie od jakichkolwiek ograniczeń prawnych.


To naturalne prawo do ochrony prywatności zostało również przekształcone w prawo do roszczeń, zapisane w art. 12 Powszechnej Deklaracji Praw Człowieka, stanowiącym, że "*Nikt nie może być narażony na samowolną ingerencję w jego życie prywatne, rodzinne, domowe lub korespondencję, ani na zamachy na jego cześć i dobre imię. Każdy ma prawo do ochrony prawnej przed taką ingerencją lub atakami".


Jednak podstawowa działalność firm specjalizujących się w analizie łańcucha polega właśnie na ingerowaniu w sferę prywatną użytkownika, naruszając w ten sposób poufność jego korespondencji. Chociaż można by mieć nadzieję, że zgodnie z wyżej wymienionym prawem, państwa będą energicznie bronić naszej prywatności, nie tylko zaniedbują to, ale także w znacznym stopniu finansują te firmy analityczne. Próżno byłoby również liczyć na wsparcie ze strony stowarzyszeń branżowych, które wydają się skłonne do wszelkich ustępstw w obliczu ustawodawcy.


De facto prawo do prywatności w Bitcoin nie istnieje. W związku z tym to użytkownik powinien dochodzić swojego naturalnego prawa i chronić poufność swojej korespondencji. Wiąże się to z przyjęciem różnych technik i praktyk użytkowania, które pozwolą zapobiec lub oszukać heurystykę wykorzystywaną do analizy łańcucha.


### Unikanie popadania w heurystykę

Przede wszystkim, przed rozważeniem bardziej radykalnych metod, wskazane jest, aby w jak największym stopniu ograniczyć naszą ekspozycję na heurystykę wykorzystywaną do analizy łańcucha. Jak wspomniano wcześniej, dwie najpotężniejsze heurystyki to Address i CoinJoin.


Podstawową zasadą zapewnienia prywatności na Bitcoin jest użycie nowego, czystego Address dla każdej transakcji przychodzącej do Wallet. Ponowne użycie Address jest naprawdę głównym zagrożeniem dla poufności na Bitcoin.

Dla indywidualnego użytkownika wygenerowanie nowego Address dla każdej przychodzącej płatności jest bardzo proste. Nowoczesne portfele robią to automatycznie po kliknięciu przycisku "Odbierz". Jeśli więc przywiązujesz choćby najmniejszą wagę do prywatności swoich transakcji, korzystanie ze świeżych adresów stanowi absolutne minimum. Jeśli kiedykolwiek potrzebujesz statycznego punktu kontaktowego w Internecie, zamiast umieszczać odbierający Address, możesz skorzystać z rozwiązań [takich jak PayNym, które implementują BIP47] (https://planb.network/tutorials/privacy/On-Chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).

Następnie, jeśli chcesz przeciwdziałać analizie łańcucha, unikaj łączenia UTXO na wejściu transakcji. Co najmniej, jeśli naprawdę musisz scalić, preferuj UTXO, które mają to samo źródło. To zalecenie oznacza dobre zarządzanie swoimi UTXO. Kupując bitcoiny, preferuj przelewy obejmujące duże kwoty, aby zmaksymalizować liczbę płatności, których możesz dokonać bez konieczności łączenia. Radzę również oznaczać swoje UTXO w oprogramowaniu, aby zidentyfikować ich pochodzenie i uniknąć łączenia z różnych źródeł.


Mówiąc szerzej, w przypadku wszystkich innych heurystyk, trzeba je znać, aby starać się w nie nie popaść:


- Nie używaj skryptów mniejszości. Preferowane SegWit V0 lub ewentualnie SegWit V1;
- Nie dokonuj płatności w zaokrągleniu. Na przykład, jeśli chcesz wysłać 100 tys. Sats znajomemu, wyślij mu 114 486 Sats. W zamian postawi ci drinka;
- Staraj się, aby nie zawsze zmiana była znacznie większa niż wynik płatności;
- Nie publikuj adresów odbiorczych w mediach społecznościowych;
- Użyj własnego węzła pod Tor, aby transmitować swoje transakcje;
- Staraj się nie transmitować transakcji Bitcoin zawsze w tym samym czasie..


### Korzystanie z narzędzi ochrony prywatności

Można również skorzystać z metod, które sprawiają, że użycie Bitcoin jest niejednoznaczne w celu uniknięcia lub oszukania analizy łańcucha.


Najpopularniejszą techniką jest z pewnością CoinJoin, struktura transakcji współpracy, która mobilizuje kilka UTXO o tych samych kwotach. Celem jest tutaj zerwanie deterministycznych powiązań, zapobiegając w ten sposób analizom z teraźniejszości do przeszłości i z przeszłości do teraźniejszości. CoinJoin pozwala na wiarygodne zaprzeczenie, ukrywając monety w dużej grupie nierozróżnialnych monet. Jeśli chcesz dowiedzieć się więcej o CoinJoin, zarówno pod względem technicznym, jak i praktycznym, sugeruję przeczytanie innych artykułów i samouczków:


- [CoinJoin - SAMOURAI Wallet](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-samourai-Wallet-e566803d-ab3f-4d98-9136-5462009262ef);
- [CoinJoin - SPARROW Wallet](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-sparrow-Wallet-84def86d-faf5-4589-807a-83be60720c8b);
- [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).

![analysis](assets/en/13.webp)


CoinJoin jest doskonałym narzędziem do tworzenia wiarygodnego zaprzeczenia dla monet, ale nie jest zoptymalizowany pod kątem wszystkich potrzeb użytkowników w zakresie prywatności. W szczególności CoinJoin nie został zaprojektowany jako narzędzie płatnicze. Jest bardzo sztywny, jeśli chodzi o kwoty wymieniane w celu udoskonalenia produkcji wiarygodnej zaprzeczalności. Ponieważ nie można swobodnie wybierać kwoty transakcji, CoinJoin nie może być używany do dokonywania płatności w bitcoinach.


Dla przykładu, wyobraźmy sobie, że chcę zapłacić za moją bagietkę w bitcoinach, jednocześnie optymalizując swoją prywatność. Biorąc pod uwagę brak możliwości wyboru kwoty UTXO z CoinJoin, nie byłbym w stanie dostosować kwoty mojego wydatku do ceny ustalonej przez piekarza. Dlatego CoinJoin okazuje się nieodpowiedni do transakcji płatniczych.


Inne narzędzia zostały stworzone w celu zaspokojenia potrzeb prywatności w bardziej konkretnych przypadkach użycia. Na przykład mamy [PayJoin](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), rodzaj mini-CoinJoin, obejmujący tylko dwóch uczestników i oparty na strukturze umożliwiającej dokonywanie płatności.


Wyjątkowość PayJoin polega na jego zdolności do tworzenia transakcji, która wygląda zwyczajnie, podczas gdy w rzeczywistości jest to mini-CoinJoin między dwoma użytkownikami. W tej strukturze odbiorca transakcji uczestniczy wśród danych wejściowych obok faktycznego nadawcy. W ten sposób odbiorca wstawia płatność dla siebie w ramach transakcji, która ułatwia faktyczną płatność.


Na przykład, jeśli kupisz bagietkę od piekarza za 6 000 Sats z UTXO w wysokości 10 000 Sats i chcesz wykonać PayJoin, twój piekarz doda UTXO w wysokości 15 000 Sats, który należy do niego jako dane wejściowe do pierwotnej transakcji, którą w pełni odzyska jako dane wyjściowe, aby oszukać heurystykę:


![analysis](assets/en/14.webp)


Opłaty transakcyjne są pomijane, aby uprościć zrozumienie programu.


Cele PayJoin są dwojakie. Po pierwsze, ma on na celu oszukanie zewnętrznego obserwatora poprzez stworzenie wabika za pomocą COH. Rzeczywiście, gdy analityk obserwuje tę transakcję, pomyśli, że może zastosować COH, a tym samym założyć wspólny Ownership różnych danych wejściowych. W rzeczywistości założenie to jest błędne, ponieważ jedno wejście należy do nadawcy, podczas gdy drugie jest własnością odbiorcy. Dlatego PayJoin psuje analizę łańcucha, prowadząc analityka na złą ścieżkę.

Drugim celem PayJoin jest oszukanie analityka co do rzeczywistej kwoty transakcji, dzięki specyficznej strukturze jego danych wyjściowych. W ten sposób PayJoin wchodzi w zakres steganografii. Pozwala ukryć prawdziwą kwotę transakcji w ramach zwodniczej transakcji.


Rzeczywiście, jeśli wrócimy do naszego przykładu wykorzystania PayJoin do zakupu bagietki, zewnętrzny obserwator może pomyśleć, że mamy do czynienia z płatnością w wysokości 4 000 Sats lub 21 000 Sats. W rzeczywistości płatność za bagietkę wynosi 6 000 Sats: 21 000 - 15 000 = 6 000. Prawdziwa wartość płatności jest zatem ukryta w fałszywej płatności, która działa jako wabik do analizy łańcucha.


Oprócz PayJoin i CoinJoin istnieje wiele innych struktur transakcji Bitcoin, które albo blokują analizę łańcucha, albo ją oszukują. Wśród nich można wymienić transakcje [Stonewall](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) i [StonewallX2](https://planb.network/tutorials/privacy/On-Chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b), które pozwalają albo stworzyć elastyczny mini CoinJoin, albo imitować elastyczny mini CoinJoin. Istnieją również transakcje [Ricochet](https://planb.network/tutorials/privacy/On-Chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589), które symulują zmianę Ownership bitcoinów poprzez wykonanie wielu fałszywych przelewów do siebie.


Wszystkie te narzędzia są dostępne w Samourai Wallet na urządzenia mobilne i Sparrow Wallet na PC. Jeśli chcesz dowiedzieć się więcej o tych konkretnych strukturach transakcji, radzę zapoznać się z moimi samouczkami:


- [PayJoin](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f);
- [PayJoin - SAMOURAI Wallet](https://planb.network/tutorials/privacy/On-Chain/PayJoin-samourai-Wallet-48a5c711-ee3d-44db-b812-c55913080eab);
- [PayJoin - SPARROW Wallet](https://planb.network/tutorials/privacy/On-Chain/PayJoin-sparrow-Wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62);
- [STONEWALL](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4);
- [STONEWALL X2](https://planb.network/tutorials/privacy/On-Chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b);
- [RICOCHET](https://planb.network/tutorials/privacy/On-Chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).


## Wnioski

Analiza łańcuchowa to praktyka polegająca na próbie prześledzenia przepływu bitcoinów On-Chain. Aby to zrobić, analitycy szukają wzorców i cech charakterystycznych w celu wyciągnięcia mniej lub bardziej prawdopodobnych hipotez i interpretacji.


Dokładność tych heurystyk jest różna: niektóre zapewniają wyższy stopień pewności niż inne, ale żadna nie może twierdzić, że jest nieomylna. Jednak nagromadzenie kilku zbieżnych heurystyk może złagodzić tę nieodłączną wątpliwość, chociaż całkowite jej wyeliminowanie pozostaje niemożliwe.

Metody te można podzielić na trzy odrębne kategorie:


- Wzorce, koncentrujące się na ogólnej strukturze każdej transakcji;
- Wewnętrzna heurystyka, która pozwala na wyczerpujące zbadanie wszystkich szczegółów transakcji, bez rozszerzania jej kontekstu;
- Heurystyka zewnętrzna, która obejmuje analizę transakcji w jej środowisku, a także wszelkie dane zewnętrzne, które mogą zapewnić wgląd.


Jako użytkownik Bitcoin konieczne jest opanowanie podstawowych zasad analizy łańcucha, aby skutecznie mu przeciwdziałać, a tym samym chronić swoją prywatność.


## Minisłownik techniczny:

**P2PKH:** skrót od Pay to Public Key Hash. Jest to standardowy model skryptu używany do ustalania warunków wydawania na UTXO. Umożliwia blokowanie bitcoinów na Hash klucza publicznego, czyli na odbierającym Address. Skrypt ten jest powiązany ze standardem Legacy i został wprowadzony w pierwszych wersjach Bitcoin przez Satoshi Nakamoto. W przeciwieństwie do P2PK, gdzie klucz publiczny jest wyraźnie zawarty w skrypcie, P2PKH używa kryptograficznego odcisku klucza publicznego, z pewnymi metadanymi, zwanego również "odbierającym Address". Skrypt ten zawiera RIPEMD160 Hash SHA256 klucza publicznego i stanowi, że aby uzyskać dostęp do środków, odbiorca musi dostarczyć klucz publiczny pasujący do tego Hash, a także ważny podpis cyfrowy wygenerowany z powiązanego klucza prywatnego. Adresy P2PKH są kodowane przy użyciu formatu Base58Check, który zapewnia im odporność na błędy typograficzne dzięki zastosowaniu sumy kontrolnej. Adresy te zawsze zaczynają się od cyfry 1.

**P2TR:** skrót od Pay to Taproot ("zapłać do korzenia"). Jest to standardowy model skryptu używany do ustalania warunków wydatków na UTXO. P2TR został wprowadzony wraz z wdrożeniem Taproot w listopadzie 2021 roku. Wykorzystuje protokół Schnorra do agregacji kluczy kryptograficznych, a także drzewa Merkle'a dla alternatywnych skryptów, znanych jako MAST (Merkelized Alternative Script Tree). W przeciwieństwie do tradycyjnych transakcji, w których warunki wydatków są publicznie ujawniane (czasami przy odbiorze, czasami przy wydawaniu), P2TR pozwala na ukrywanie złożonych skryptów za jednym pozornym kluczem publicznym. Technicznie rzecz biorąc, skrypt P2TR blokuje bitcoiny na unikalnym kluczu publicznym Schnorra, oznaczonym jako K. Jednak ten klucz K jest w rzeczywistości agregatem klucza publicznego P i klucza publicznego M, przy czym ten ostatni jest obliczany na podstawie Merkle Root listy ScriptPubKeys. Agregacja kluczy jest wykonywana przy użyciu protokołu podpisu Schnorra. Bitcoiny zablokowane za pomocą skryptu P2TR można wydać na dwa różne sposoby: albo publikując podpis dla klucza publicznego P, albo spełniając jeden ze skryptów zawartych w Merkle Tree. Pierwsza opcja nazywana jest "ścieżką klucza", a druga "ścieżką skryptu" W ten sposób P2TR umożliwia użytkownikom wysyłanie bitcoinów albo do klucza publicznego, albo do wielu wybranych skryptów. Kolejną zaletą tego skryptu jest to, że chociaż istnieje wiele sposobów na wydanie wyniku P2TR, tylko ten, który jest używany, musi zostać ujawniony podczas wydawania, pozwalając niewykorzystanym alternatywom pozostać prywatnymi. Na przykład, dzięki agregacji kluczy Schnorra, klucz publiczny P może być kluczem zagregowanym, potencjalnie reprezentującym Multisig. P2TR jest wyjściem SegWit w wersji 1, co oznacza, że podpisy dla wejść P2TR są przechowywane w świadku transakcji, a nie w ScriptSig. Adresy P2TR używają kodowania Bech32m i zaczynają się od bc1p.

**P2WPKH:** Skrót od Pay to Witness Public Key Hash. Jest to standardowy model skryptu używany do ustalania warunków wydatków na UTXO. P2WPKH został wprowadzony wraz z wdrożeniem SegWit w sierpniu 2017 roku. Skrypt ten jest podobny do P2PKH (Pay to Public Key Hash), ponieważ również blokuje bitcoiny na podstawie Hash klucza publicznego, czyli otrzymanego Address. Różnica polega na tym, w jaki sposób podpisy i skrypty są uwzględniane w transakcji. W przypadku P2WPKH informacje o skrypcie podpisu (ScriptSig) są przenoszone z tradycyjnej struktury transakcji do oddzielnej sekcji o nazwie Witness. Przeniesienie to jest funkcją aktualizacji SegWit (Segregated Witness). Zaletą tej techniki jest zmniejszenie rozmiaru danych transakcji w głównej części, przy jednoczesnym zachowaniu niezbędnych informacji o skrypcie do walidacji w oddzielnej sekcji. W związku z tym transakcje P2WPKH są generalnie tańsze pod względem opłat w porównaniu z transakcjami Legacy. Adresy P2WPKH są zapisywane przy użyciu kodowania Bech32, co przyczynia się do bardziej zwięzłego i mniej podatnego na błędy zapisu dzięki sumie kontrolnej BCH. Adresy te zawsze zaczynają się od bc1q, dzięki czemu można je łatwo odróżnić od adresów odbiorczych Legacy. P2WPKH jest wersją 0 wyjścia SegWit.


**UTXO:** Skrót oznaczający niewydane środki z transakcji. UTXO to wynik transakcji, który nie został jeszcze wydany lub wykorzystany jako wkład do nowej transakcji. UTXO reprezentują ułamek bitcoinów, które użytkownik posiada i które są obecnie dostępne do wydania. Każdy UTXO jest powiązany z określonym skryptem wyjściowym, który określa warunki niezbędne do wydania bitcoinów. Transakcje w Bitcoin wykorzystują te UTXO jako dane wejściowe i tworzą nowe UTXO jako dane wyjściowe. Model UTXO ma fundamentalne znaczenie dla Bitcoin, ponieważ pozwala na łatwą weryfikację, czy transakcje nie próbują wydać bitcoinów, które nie istnieją lub zostały już wydane. Zasadniczo UTXO jest fragmentem Bitcoin.