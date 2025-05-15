---
name: CoinJoin - Wróbel Wallet
description: Jak wykonać CoinJoin na Sparrow Wallet?
---
![cover](assets/cover.webp)


***OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, narzędzie Whirlpool przestało działać, nawet dla osób, które mają własne Dojo lub używają Sparrow Wallet. Możliwe jednak, że narzędzie to zostanie przywrócone w nadchodzących tygodniach lub ponownie uruchomione w inny sposób. Co więcej, teoretyczna część tego artykułu pozostaje istotna dla zrozumienia zasad i celów coinjoinów w ogóle (nie tylko Whirlpool), a także zrozumienia skuteczności modelu Whirlpool.*


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

W tym samouczku dowiesz się, czym jest CoinJoin i jak go wykonać przy użyciu oprogramowania Sparrow Wallet i implementacji Whirlpool.


## Co to jest CoinJoin na Bitcoin?

**CoinJoin to technika, która łamie identyfikowalność bitcoinów na Blockchain**. Opiera się ona na transakcji współpracy o określonej strukturze o tej samej nazwie: transakcji CoinJoin.


Coinjoiny zwiększają prywatność użytkowników Bitcoin, komplikując analizę łańcucha zewnętrznym obserwatorom. Ich struktura umożliwia łączenie wielu monet od różnych użytkowników w jedną transakcję, zacierając w ten sposób ślady i utrudniając określenie powiązań między adresami wejściowymi i wyjściowymi.


Zasada CoinJoin opiera się na podejściu opartym na współpracy: kilku użytkowników, którzy chcą mieszać swoje bitcoiny, wpłaca identyczne kwoty jako dane wejściowe tej samej transakcji. Kwoty te są następnie redystrybuowane jako dane wyjściowe o równej wartości dla każdego użytkownika. Pod koniec transakcji niemożliwe staje się powiązanie konkretnego wyniku ze znanym użytkownikiem na wejściu. Nie istnieje bezpośrednie powiązanie między wejściami i wyjściami, co zrywa związek między użytkownikami i ich UTXO, a także historią każdej monety.

![coinjoin](assets/notext/1.webp)


Przykład transakcji CoinJoin (nie ode mnie): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Aby wykonać CoinJoin przy jednoczesnym zapewnieniu, że każdy użytkownik zachowuje kontrolę nad swoimi środkami przez cały czas, proces rozpoczyna się od skonstruowania transakcji przez koordynatora, który następnie przesyła ją do każdego uczestnika. Następnie każdy użytkownik podpisuje transakcję po sprawdzeniu, czy mu odpowiada. Wszystkie zebrane podpisy są ostatecznie zintegrowane z transakcją. Jeśli użytkownik lub koordynator podejmie próbę przekierowania środków poprzez modyfikację danych wyjściowych transakcji CoinJoin, podpisy okażą się nieważne, co doprowadzi do odrzucenia transakcji przez węzły.


Istnieje kilka implementacji CoinJoin, takich jak Whirlpool, JoinMarket lub Wabisabi, z których każda ma na celu zarządzanie koordynacją między uczestnikami i zwiększenie wydajności transakcji CoinJoin.


W tym poradniku skupimy się na implementacji **Whirlpool**, którą uważam za najskuteczniejsze rozwiązanie do wykonywania coinjoinów na Bitcoin. Chociaż jest ona dostępna w kilku portfelach, niniejszy poradnik omawia wyłącznie jej użycie z oprogramowaniem Sparrow Wallet Desktop.

## Dlaczego warto wykonywać CoinJoins na Bitcoin?


Jednym z początkowych problemów każdego systemu płatności peer-to-peer jest Double-spending: jak uniemożliwić złośliwym osobom wielokrotne wydawanie tych samych jednostek pieniężnych bez odwoływania się do centralnego organu arbitrażowego?


Satoshi Nakamoto zapewnił rozwiązanie tego dylematu poprzez protokół Bitcoin, elektroniczny system płatności peer-to-peer, który działa niezależnie od jakiegokolwiek organu centralnego. W swojej białej księdze podkreśla, że jedynym sposobem na potwierdzenie braku Double-spending jest zapewnienie widoczności wszystkich transakcji w ramach systemu płatności.


Aby upewnić się, że każdy uczestnik jest świadomy transakcji, muszą one zostać ujawnione publicznie. W związku z tym działanie Bitcoin opiera się na przejrzystej i rozproszonej infrastrukturze, umożliwiającej każdemu operatorowi węzła weryfikację całości łańcuchów podpisów elektronicznych i historii każdej monety, od momentu jej utworzenia przez Miner.


Przejrzysty i rozproszony charakter Bitcoin oznacza, że każdy użytkownik sieci może śledzić i analizować transakcje wszystkich innych uczestników. W związku z tym anonimowość na poziomie transakcji jest niemożliwa. Anonimowość jest jednak zachowana na poziomie indywidualnej identyfikacji. W przeciwieństwie do tradycyjnego systemu bankowego, w którym każde konto jest powiązane z osobistą tożsamością, w Bitcoin środki są powiązane z parami kluczy kryptograficznych, oferując w ten sposób użytkownikom formę pseudonimowości za identyfikatorami kryptograficznymi.


Dlatego też poufność Bitcoin jest zagrożona, gdy zewnętrzni obserwatorzy zdołają powiązać określone UTXO ze zidentyfikowanymi użytkownikami. Po ustanowieniu takiego powiązania możliwe staje się śledzenie ich transakcji i analizowanie historii ich bitcoinów. CoinJoin jest właśnie techniką opracowaną w celu przełamania identyfikowalności UTXO, oferując w ten sposób pewną Layer poufność użytkownikom Bitcoin na poziomie transakcji.


## Jak działa Whirlpool?


Whirlpool wyróżnia się na tle innych metod CoinJoin dzięki wykorzystaniu transakcji "_ZeroLink_", które zapewniają, że nie ma absolutnie żadnego technicznego powiązania między wszystkimi danymi wejściowymi i wszystkimi danymi wyjściowymi. To doskonałe połączenie osiąga się dzięki strukturze, w której każdy uczestnik wnosi identyczną kwotę wkładu (z wyjątkiem opłat Mining), generując w ten sposób produkty wyjściowe o idealnie równych kwotach.


To restrykcyjne podejście do danych wejściowych nadaje transakcjom Whirlpool CoinJoin wyjątkową cechę: całkowity brak deterministycznych powiązań między danymi wejściowymi i wyjściowymi. Innymi słowy, każde wyjście ma równe prawdopodobieństwo przypisania do dowolnego uczestnika, w porównaniu do wszystkich innych wyjść transakcji.

Początkowo liczba uczestników każdego Whirlpool CoinJoin była ograniczona do 5, z 2 nowymi uczestnikami i 3 remikserami (wyjaśnimy te koncepcje w dalszej części). Jednak wzrost opłat transakcyjnych On-Chain zaobserwowany w 2023 r. skłonił zespoły Samourai do ponownego przemyślenia swojego modelu w celu poprawy prywatności przy jednoczesnym obniżeniu kosztów. Tak więc, biorąc pod uwagę sytuację rynkową opłat i liczbę uczestników, koordynator może teraz organizować coinjoiny obejmujące 6, 7 lub 8 uczestników. Te ulepszone sesje są określane jako "_Surge Cycles_". Ważne jest, aby pamiętać, że niezależnie od konfiguracji, w coinjoinach Whirlpool zawsze jest tylko 2 nowych uczestników.


Dlatego transakcje Whirlpool charakteryzują się identyczną liczbą wejść i wyjść, którymi mogą być:


- 5 wejść i 5 wyjść;

![coinjoin](assets/notext/2.webp)


- 6 wejść i 6 wyjść;

![coinjoin](assets/notext/3.webp)


- 7 wejść i 7 wyjść;

![coinjoin](assets/notext/4.webp)


- 8 wejść i 8 wyjść.

![coinjoin](assets/notext/5.webp)

Model proponowany przez Whirlpool opiera się zatem na małych transakcjach CoinJoin. W przeciwieństwie do Wasabi i JoinMarket, gdzie solidność anonsetów zależy od liczby uczestników w pojedynczym cyklu, Whirlpool stawia na łańcuch kilku małych cykli.


W tym modelu użytkownik ponosi opłaty tylko przy pierwszym wejściu do puli, co pozwala mu uczestniczyć w wielu remiksach bez dodatkowych opłat. To nowi uczestnicy ponoszą opłaty Mining dla remikserów.


Z każdym dodatkowym CoinJoin, w którym moneta uczestniczy, wraz z jej wcześniej napotkanymi rówieśnikami, anonsety będą rosły wykładniczo. Celem jest zatem skorzystanie z tych darmowych remiksów, które przy każdym wystąpieniu przyczyniają się do zwiększenia gęstości anonsetów powiązanych z każdą mieszaną monetą.


Whirlpool został zaprojektowany z uwzględnieniem dwóch ważnych wymagań:


- Dostępność implementacji na urządzeniach mobilnych, biorąc pod uwagę, że Samourai Wallet jest przede wszystkim aplikacją na smartfony;
- Szybkość cykli remiksowania w celu promowania znacznego wzrostu liczby anonsów.


Te imperatywy kierowały wyborami twórców Samourai Wallet przy projektowaniu Whirlpool, prowadząc ich do ograniczenia liczby uczestników na cykl. Zbyt mała liczba uczestników wpłynęłaby negatywnie na skuteczność CoinJoin, drastycznie zmniejszając liczbę anonsów generowanych w każdym cyklu, podczas gdy zbyt duża liczba uczestników stanowiłaby problem w zarządzaniu aplikacjami mobilnymi i utrudniałaby przepływ cykli.


**Ostatecznie, nie ma potrzeby posiadania dużej liczby uczestników na CoinJoin na Whirlpool, ponieważ anonsety są dokonywane przez kumulację kilku cykli CoinJoin

[-> Dowiedz się więcej o anonsach Whirlpool](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### Pule i opłaty CoinJoin

Aby zapewnić, że wielokrotne cykle skutecznie zwiększają anonsety mieszanych monet, należy ustanowić pewne ramy w celu ograniczenia ilości używanych UTXO. Whirlpool definiuje w tym celu różne pule.


Pula reprezentuje grupę użytkowników, którzy chcą łączyć się ze sobą, którzy zgadzają się na ilość UTXO do wykorzystania w celu optymalizacji procesu CoinJoin. Każda pula określa stałą kwotę dla UTXO, której użytkownik musi przestrzegać, aby wziąć udział. Tak więc, aby wykonać coinjoiny z Whirlpool, należy wybrać pulę. Obecnie dostępne pule są następujące:


- 0.5 bitcoinów;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100.000 Sats).


Dołączając do puli ze swoimi bitcoinami, zostaną one podzielone na generate UTXO, które są idealnie jednorodne z tymi innych uczestników puli. Każda pula ma maksymalny limit; dlatego w przypadku kwot przekraczających ten limit będziesz zmuszony albo dokonać dwóch oddzielnych wpisów w ramach tej samej puli, albo przenieść się do innej puli z wyższą kwotą:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Jak wspomniano wcześniej, UTXO jest uważany za należący do puli, gdy jest gotowy do integracji z CoinJoin. Nie oznacza to jednak, że użytkownik traci nad nim kontrolę. **Podczas różnych cykli mieszania użytkownik zachowuje pełną kontrolę nad swoimi kluczami, a co za tym idzie, bitcoinami**. To właśnie odróżnia technikę CoinJoin od innych scentralizowanych technik mieszania.


Aby przystąpić do puli CoinJoin, należy uiścić opłaty serwisowe oraz opłaty Mining. Opłaty serwisowe są ustalane dla każdej puli i mają na celu wynagrodzenie zespołów odpowiedzialnych za rozwój i utrzymanie Whirlpool. W przypadku użytkowników Sparrow Wallet opłaty te są przekazywane przez zespoły Samourai deweloperom Sparrow.


Opłaty za korzystanie z Whirlpool należy uiścić jednorazowo przy wejściu do puli. Po wykonaniu tego kroku użytkownik ma możliwość uczestniczenia w nieograniczonej liczbie remiksów bez dodatkowych opłat. Oto aktualne stałe opłaty dla każdej puli:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Opłaty te zasadniczo działają jak bilet wstępu do wybranej puli, niezależnie od kwoty wpłaconej w CoinJoin. Tak więc, niezależnie od tego, czy dołączysz do puli 0,01 z dokładnie 0,01 BTC, czy też wejdziesz z 0,5 BTC, opłaty pozostaną takie same w wartości bezwzględnej.


Przed przystąpieniem do coinjoins użytkownik ma zatem wybór między 2 strategiami:


- Wybierają mniejszą pulę, aby zminimalizować opłaty za usługi, wiedząc, że w zamian otrzymają kilka małych UTXO;
- Lub wolą większą pulę, zgadzając się płacić wyższe opłaty, aby uzyskać mniejszą liczbę UTXO o większej wartości.


Ogólnie rzecz biorąc, odradza się łączenie kilku mieszanych UTXO po cyklach CoinJoin, ponieważ może to zagrozić uzyskanej poufności, zwłaszcza ze względu na heurystykę Common-Input-Ownership (CIOH). W związku z tym rozsądne może być wybranie większej puli, nawet jeśli oznacza to wyższe koszty, aby uniknąć zbyt wielu UTXO o małej wartości jako danych wyjściowych. Użytkownik musi rozważyć te kompromisy, aby wybrać preferowaną pulę.


Oprócz opłat za usługi, należy również wziąć pod uwagę opłaty Mining związane z każdą transakcją Bitcoin. Jako użytkownik Whirlpool, będziesz musiał uiścić opłaty Mining za transakcję przygotowawczą (`Tx0`), jak również te za pierwszą CoinJoin. Wszystkie kolejne remiksy będą darmowe, dzięki modelowi Whirlpool, który opiera się na płatnościach nowych uczestników.


Rzeczywiście, w każdym Whirlpool CoinJoin dwóch użytkowników spośród wejść to nowi uczestnicy. Pozostałe dane wejściowe pochodzą od remikserów. W rezultacie opłaty Mining dla wszystkich uczestników transakcji są pokrywane przez tych dwóch nowych uczestników, którzy następnie również skorzystają z bezpłatnych remiksów:

![coinjoin](assets/en/6.webp)

Dzięki temu systemowi opłat, Whirlpool naprawdę odróżnia się od innych usług CoinJoin, ponieważ anonimowość UTXO nie jest proporcjonalna do ceny płaconej przez użytkownika. W ten sposób można osiągnąć znacznie wysoki poziom anonimowości, płacąc jedynie opłaty za wejście do puli i opłaty Mining za dwie transakcje (`Tx0` i początkowy miks).


Ważne jest, aby pamiętać, że użytkownik będzie musiał również pokryć opłaty Mining, aby wycofać swoje UTXO z puli po zakończeniu wielu coinjoinów, chyba że wybrał opcję `mix to`, którą omówimy w samouczku poniżej.


### Konta HD Wallet używane przez Whirlpool

Aby wykonać CoinJoin poprzez Whirlpool, Wallet musi generate kilka odrębnych kont. Konto, w kontekście HD (Hierarchical Deterministic) Wallet, stanowi sekcję, która jest całkowicie odizolowana od innych, ta separacja występuje na trzecim poziomie głębokości hierarchii Wallet, czyli na poziomie `xpub`.

HD Wallet może teoretycznie wyprowadzić do `2^(32/2)` różnych kont. Początkowe konto, używane domyślnie we wszystkich portfelach Bitcoin, odpowiada indeksowi `0`.


W przypadku portfeli dostosowanych do Whirlpool, takich jak Samourai lub Sparrow, używane są 4 konta, aby zaspokoić potrzeby procesu CoinJoin:


- Konto **depozytowe**, identyfikowane przez indeks `0`;
- Konto **złego banku** (lub doxxic change), identyfikowane przez indeks `2 147 483 644'`;
- Konto **premix**, identyfikowane przez indeks `2 147 483 645'`;
- Konto **postmix**, identyfikowane przez indeks `2 147 483 646'`.


Każde z tych kont spełnia określoną funkcję w ramach CoinJoin.


Wszystkie te konta są powiązane z pojedynczym seed, co pozwala użytkownikowi odzyskać dostęp do wszystkich swoich bitcoinów za pomocą frazy odzyskiwania i, w stosownych przypadkach, passphrase. Konieczne jest jednak określenie w oprogramowaniu, podczas tej operacji odzyskiwania, różnych indeksów kont, które zostały użyte.


Przyjrzyjmy się teraz różnym etapom Whirlpool CoinJoin w ramach tych kont.


### Różne etapy coinjoinów na Whirlpool

**Etap 1: Tx0**

Punktem wyjścia dla każdego Whirlpool CoinJoin jest **konto depozytowe**. To konto jest automatycznie używane podczas tworzenia nowego Bitcoin Wallet. To konto musi być zasilone bitcoinami, które chcesz wymieszać.


`Tx0` reprezentuje pierwszy etap procesu mieszania Whirlpool. Ma on na celu przygotowanie i wyrównanie UTXO dla CoinJoin, poprzez podzielenie ich na jednostki odpowiadające ilości wybranej puli, w celu zapewnienia jednorodności mieszania. Wyrównane UTXO są następnie wysyłane na konto **premix**. Jeśli chodzi o różnicę, która nie może wejść do puli, jest ona rozdzielana na specjalne konto: **bad bank** (lub "doxxic change").


Ta początkowa transakcja `Tx0` służy również do rozliczenia opłat za usługę należnych koordynatorowi mix. W przeciwieństwie do kolejnych etapów, ta transakcja nie jest oparta na współpracy; użytkownik musi zatem przyjąć pełne opłaty Mining:

![coinjoin](assets/en/7.webp)

W tym przykładzie transakcji `Tx0`, wejście w wysokości `372,000 Sats` z naszego **depozytowego** konta jest podzielone na kilka wychodzących UTXO, które są dystrybuowane w następujący sposób:


- Kwota `5.000 Sats` przeznaczona dla koordynatora na opłaty za usługi, odpowiadająca wejściu do puli `100.000 Sats`;
- Trzy UTXO przygotowane do mieszania, przekierowane na nasze konto **premix** i zarejestrowane u koordynatora. Te UTXO są wyrównane na poziomie `108,000 Sats` każdy, w celu pokrycia opłat Mining za ich przyszłe wstępne mieszanie;
- Nadwyżka, która nie może wejść do puli, ponieważ jest zbyt mała, jest uważana za toksyczną zmianę. Jest ona wysyłana na określone konto. W tym przypadku zmiana ta wynosi `40 000 Sats`;
- Wreszcie, istnieje `3,000 Sats`, które nie stanowią wyjścia, ale są opłatami Mining niezbędnymi do potwierdzenia `Tx0`.


Na przykład, oto prawdziwy Tx0 Whirlpool (który nie pochodzi ode mnie): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**Krok 2: Toksyczna zmiana**

Nadwyżka, której nie udało się zintegrować z pulą, tutaj odpowiadająca `40 000 Sats`, jest przekierowywana na konto **złego banku**, zwane również "toksyczną zmianą", aby zapewnić ścisłe oddzielenie od innych UTXO w Wallet.


Ten UTXO jest niebezpieczny dla prywatności użytkownika, ponieważ nie tylko jest zawsze powiązany z jego przeszłością, a zatem prawdopodobnie z tożsamością jego właściciela, ale dodatkowo jest odnotowany jako należący do użytkownika, który wykonał CoinJoin.


Jeśli ten UTXO zostanie połączony z mieszanymi wyjściami, ten ostatni straci całą prywatność uzyskaną podczas cykli CoinJoin, zwłaszcza z powodu CIOH (*Common-Input-Ownership-Heuristic*). Jeśli zostanie on połączony z innymi toksycznymi zmianami, użytkownik ryzykuje utratę prywatności, ponieważ połączy różne wpisy z cykli CoinJoin. Dlatego należy go traktować ostrożnie. Sposób zarządzania tym toksycznym UTXO zostanie szczegółowo opisany w ostatniej części tego artykułu, a przyszłe samouczki zagłębią się w te metody w sieci PlanB.


**Krok 3: Początkowa mieszanka**

Po zakończeniu `Tx0`, wyrównane UTXO są wysyłane do konta **premix** naszego Wallet, gotowe do wprowadzenia do pierwszego cyklu CoinJoin, zwanego również "początkowym miksem". Jeśli, jak w naszym przykładzie, `Tx0` generuje wiele UTXO przeznaczonych do mieszania, każdy z nich zostanie zintegrowany z oddzielnym początkowym CoinJoin.

Pod koniec tych początkowych miksów konto **premix** będzie puste, podczas gdy nasze monety, po uiszczeniu opłat Mining za ten pierwszy CoinJoin, zostaną dostosowane dokładnie do kwoty określonej przez wybraną pulę. W naszym przykładzie, nasze początkowe UTXO w wysokości `108 000 Sats` zostanie zredukowane do dokładnie `100 000 Sats`.

![coinjoin](assets/en/8.webp)

**Krok 4: Remiksy**

Po wstępnym zmiksowaniu UTXO są przenoszone na konto **postmix**. To konto gromadzi już zmiksowane UTXO i te, które czekają na ponowne zmiksowanie. Gdy klient Whirlpool jest aktywny, UTXO znajdujące się na koncie **postmix** są automatycznie dostępne do remiksowania i zostaną losowo wybrane do udziału w tych nowych cyklach.


Przypominamy, że remiksy są wtedy w 100% darmowe: nie są wymagane żadne dodatkowe opłaty za usługi ani opłaty Mining. Utrzymywanie UTXO na koncie **postmix** utrzymuje zatem ich wartość w stanie nienaruszonym, a jednocześnie poprawia ich anonsety. Dlatego ważne jest, aby umożliwić tym monetom udział w wielu cyklach CoinJoin. To nic nie kosztuje, a zwiększa ich poziom anonimowości.


Jeśli zdecydujesz się wydać zmiksowane UTXO, możesz to zrobić bezpośrednio z tego konta **postmix**. Zaleca się przechowywanie zmieszanych UTXO na tym koncie, aby skorzystać z darmowych remiksów i zapobiec opuszczeniu obwodu Whirlpool, co mogłoby zmniejszyć ich prywatność.


Jak zobaczymy w poniższym samouczku, istnieje również opcja `mix to`, która oferuje możliwość automatycznego wysyłania zmieszanych monet do innego Wallet, takiego jak Cold Wallet, po określonej liczbie połączeń monet.


Po omówieniu teorii, przejdźmy do praktyki z samouczkiem na temat korzystania z Whirlpool za pośrednictwem oprogramowania komputerowego Sparrow Wallet!


## Samouczek: CoinJoin Whirlpool na Sparrow Wallet

Istnieje wiele opcji korzystania z Whirlpool. Pierwszą z nich jest opcja Sparrow Wallet, oprogramowanie do zarządzania Bitcoin Wallet o otwartym kodzie źródłowym dla komputerów PC.

Korzystanie ze Sparrow ma tę zaletę, że jest dość łatwe do rozpoczęcia, szybkie w konfiguracji i nie wymaga żadnego sprzętu poza komputerem i połączeniem internetowym. Istnieje jednak znacząca wada: coinjoiny będą miały miejsce tylko wtedy, gdy Sparrow jest uruchomiony i podłączony. Oznacza to, że jeśli chcesz mieszać i remiksować swoje bitcoiny 24/7, będziesz musiał stale mieć włączony komputer.


### Zainstaluj Sparrow Wallet

Aby rozpocząć, będziesz oczywiście potrzebował oprogramowania Sparrow Wallet. Można je pobrać bezpośrednio z [oficjalnej strony](https://sparrowwallet.com/download/) lub z [ich GitHub](https://github.com/sparrowwallet/sparrow/releases).


Przed instalacją oprogramowania ważne będzie zweryfikowanie podpisu i integralności właśnie pobranego pliku wykonywalnego. Jeśli chcesz uzyskać więcej szczegółów na temat procesu instalacji i weryfikacji oprogramowania Sparrow, radzę przeczytać ten inny samouczek: *[The Sparrow Wallet Guides](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)*


### Utwórz Software Wallet

Po zainstalowaniu oprogramowania należy przystąpić do tworzenia Bitcoin Wallet. Ważne jest, aby pamiętać, że do udziału w coinjoinach niezbędne jest użycie Software Wallet (zwanego również "Hot Wallet"). Dlatego **nie będzie możliwe wykonywanie coinjoinów z Wallet zabezpieczonym przez Hardware Wallet**.


Chociaż nie jest to konieczne, w przypadku planowania mieszania znacznych ilości, zdecydowanie zaleca się wybranie silnego BIP39 passphrase dla tego Wallet.


Aby utworzyć nowy Wallet, otwórz aplikację Sparrow, a następnie kliknij zakładkę `File` i `New Wallet`.


![sparrow](assets/notext/9.webp)


Wybierz nazwę dla tego Wallet, na przykład: "CoinJoin Wallet". Kliknij przycisk `Twórz Wallet`.


![sparrow](assets/notext/10.webp)


Pozostaw ustawienia domyślne, a następnie kliknij przycisk `Nowy lub zaimportowany Software Wallet`.


![sparrow](assets/notext/11.webp)


Po uzyskaniu dostępu do okna tworzenia Wallet zalecam wybranie sekwencji 12 słów, ponieważ jest ona wystarczająca. Wybierz `generate New`, aby utworzyć nową frazę odzyskiwania generate i kliknij `Use passphrase`, jeśli chcesz dodać BIP39 passphrase. Ważne jest, aby wykonać fizyczną kopię zapasową informacji o odzyskiwaniu, czy to na papierze, czy na metalowym wsporniku, aby zapewnić bezpieczeństwo swoich bitcoinów.


![sparrow](assets/notext/12.webp)

Upewnij się, że kopia zapasowa frazy odzyskiwania jest prawidłowa, zanim klikniesz `Potwierdź kopię zapasową...`. Sparrow poprosi o ponowne wprowadzenie frazy, aby zweryfikować jej poprawność. Po zakończeniu tego kroku kontynuuj, klikając `Create Keystore`.

![sparrow](assets/notext/13.webp)


Pozostaw sugerowaną ścieżkę derywacji jako domyślną i naciśnij `Import Keystore`. W moim przykładzie ścieżka derywacji różni się nieznacznie, ponieważ używam Testnet w tym samouczku. Ścieżka derywacji, która powinna się pojawić, jest następująca:

```plaintext
m/84'/0'/0'
```


![sparrow](assets/notext/14.webp)


Następnie Sparrow wyświetli szczegóły derywacji nowego Wallet. W przypadku ustawienia passphrase, wysoce zalecane jest zanotowanie "głównego odcisku palca". Chociaż ten odcisk palca klucza głównego nie jest danymi wrażliwymi, będzie przydatny do późniejszego sprawdzenia, czy rzeczywiście uzyskujesz dostęp do prawidłowego Wallet i potwierdzenia braku błędów podczas wprowadzania passphrase.


Kliknij przycisk "Zastosuj".


![sparrow](assets/notext/15.webp)


Firma Sparrow zachęca do utworzenia hasła do urządzenia Wallet. Hasło to będzie wymagane, aby uzyskać dostęp do urządzenia za pośrednictwem oprogramowania Sparrow Wallet. Wybierz silne hasło, utwórz jego kopię zapasową, a następnie kliknij przycisk `Set Password`.


![sparrow](assets/notext/16.webp)


### Otrzymywanie bitcoinów

Po utworzeniu Wallet początkowo będziesz mieć jedno konto z indeksem `0`. Jest to konto **depozytowe**, o którym mówiliśmy w poprzednich częściach. Jest to konto, na które będziesz musiał wysłać bitcoiny, aby je wymieszać.


Aby to zrobić, wybierz zakładkę `Receive` po lewej stronie okna. Sparrow automatycznie generate nowy pusty Address do odbierania bitcoinów.


![sparrow](assets/notext/17.webp)


Możesz wprowadzić etykietę dla tego Address, a następnie wysłać do niego bitcoiny, które mają zostać zmieszane.


![sparrow](assets/notext/18.webp)


### Tworzenie Tx0

Po potwierdzeniu transakcji możesz przejść do zakładki `UTXOs`.


![sparrow](assets/notext/19.webp)


Następnie wybierz UTXO, które chcesz przesłać do cykli CoinJoin. Aby wybrać wiele UTXO jednocześnie, przytrzymaj klawisz `Ctrl`, klikając wybrane UTXO.


![sparrow](assets/notext/20.webp)


Następnie kliknij przycisk `Mix Selected` w dolnej części okna. Jeśli ten przycisk nie pojawia się na Interface, oznacza to, że korzystasz z Wallet zabezpieczonego Hardware Wallet. Musisz użyć Software Wallet, aby wykonać coinjoins ze Sparrow.

![sparrow](assets/notext/21.webp)

Otworzy się okno wyjaśniające działanie Whirlpool. Jest to uproszczenie tego, co wyjaśniłem w poprzednich częściach. Kliknij `Next`, aby kontynuować.


![sparrow](assets/notext/22.webp)


Na następnej stronie możesz wprowadzić "SCODE", jeśli go posiadasz. SCODE to kod promocyjny, który oferuje zniżkę na opłaty serwisowe basenu. Samourai Wallet od czasu do czasu udostępnia takie kody swoim użytkownikom podczas specjalnych wydarzeń. Radzę [śledzićSamourai Wallet](https://twitter.com/SamouraiWallet) w mediach społecznościowych, aby nie przegapić przyszłych SCODES.


Na tej samej stronie należy również ustawić stawkę opłaty dla `Tx0` i początkowego miksu. Wybór ten wpłynie na szybkość potwierdzenia transakcji przygotowawczej i pierwszego CoinJoin. Pamiętaj, że jesteś odpowiedzialny za opłaty Mining za `Tx0` i początkowy miks, ale nie będziesz winien opłat Mining za kolejne remiksy. Dostosuj suwak `Premix Priority` zgodnie ze swoimi preferencjami, a następnie kliknij `Next`.


![sparrow](assets/notext/23.webp)


W tym nowym oknie będziesz mieć możliwość wyboru puli, którą chcesz wprowadzić, korzystając z listy rozwijanej. W moim przypadku, po początkowym wybraniu UTXO w wysokości `456 214 Sats`, moim jedynym możliwym wyborem jest pula `100 000 Sats`. Ten Interface informuje również o opłatach za usługi, które należy uiścić, a także o liczbie UTXO, które zostaną włączone do puli. Jeśli warunki wydają ci się satysfakcjonujące, kontynuuj klikając na `Preview Premix`.


![sparrow](assets/notext/24.webp)


Po tym kroku Sparrow poprosi o wprowadzenie hasła do Wallet, które zostało ustalone podczas tworzenia go w oprogramowaniu. Po wprowadzeniu hasła uzyskasz dostęp do podglądu swojego `Tx0`. Po lewej stronie okna zobaczysz, że Sparrow wygenerował różne konta niezbędne do korzystania z Whirlpool (`Deposit`, `Premix`, `Postmix` i `Badbank`). Będziesz miał również możliwość przeglądania struktury swojego `Tx0`, z różnymi wyjściami:


- Opłaty za usługi;
- Wyrównane UTXO miały wejść do puli;
- Toksyczna zmiana (Doxxic Change).


![sparrow](assets/notext/25.webp)


Jeśli transakcja ci odpowiada, kliknij `Broadcast Transaction`, aby rozgłosić twój `Tx0`. W przeciwnym razie możesz dostosować parametry tego `Tx0`, wybierając `Clear`, aby usunąć wprowadzone dane i rozpocząć proces tworzenia od początku.


### Wykonywanie Coinjoins

Po nadaniu Tx0, na koncie `Premix` znajdziesz UTXO gotowe do zmiksowania.

![sparrow](assets/notext/26.webp)


Po potwierdzeniu `Tx0`, twoje UTXO zostaną zarejestrowane w koordynatorze, a początkowe miksy rozpoczną się automatycznie.


![sparrow](assets/notext/27.webp)


Sprawdzając konto `Postmix`, będziesz obserwować UTXO wynikające z początkowych miksów. Monety te pozostaną gotowe do późniejszego remiksowania, które nie będzie wiązało się z żadnymi dodatkowymi opłatami.


![sparrow](assets/notext/28.webp)


W kolumnie `Mixes` można zobaczyć liczbę coinjoinów wykonanych przez każdą z monet. Jak zobaczymy w kolejnych sekcjach, to co naprawdę ma znaczenie, to nie tyle liczba remiksów jako takich, ale raczej powiązane z nimi anonsety, chociaż te dwa wskaźniki są częściowo powiązane.


![sparrow](assets/notext/29.webp)


Aby tymczasowo zatrzymać łączenie monet, wystarczy kliknąć przycisk `Stop Mixing`. Będziesz mieć możliwość wznowienia operacji w dowolnym momencie, wybierając `Start Mixing`.


![sparrow](assets/notext/30.webp)


Aby zapewnić ciągłą dostępność UTXO do remiksowania, konieczne jest utrzymanie aktywnego oprogramowania Sparrow. Zamknięcie oprogramowania lub wyłączenie komputera spowoduje wstrzymanie coinjoinów. Rozwiązaniem pozwalającym obejść ten problem jest wyłączenie funkcji uśpienia w ustawieniach systemu operacyjnego. Dodatkowo, Sparrow oferuje opcję zapobiegania automatycznemu usypianiu komputera, którą można znaleźć w zakładce `Tools` zatytułowanej `Prevent Computer Sleep`.


![sparrow](assets/notext/31.webp)


### Uzupełnianie coinjoinów

Aby wydać zmieszane bitcoiny, masz kilka opcji. Najbardziej bezpośrednią metodą jest dostęp do konta `Postmix` i wybranie zakładki `Wyślij`.


![sparrow](assets/notext/32.webp)


W tej sekcji będziesz mieć możliwość wprowadzenia miejsca docelowego Address, kwoty do wysłania i opłat transakcyjnych, w taki sam sposób, jak w przypadku każdej innej transakcji dokonanej za pomocą Sparrow Wallet. Jeśli chcesz, możesz również skorzystać z zaawansowanych funkcji prywatności, takich jak Stonewall, klikając przycisk `Prywatność`.


![sparrow](assets/notext/33.webp)


[-> Dowiedz się więcej o transakcjach Stonewall](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


Jeśli chcesz dokonać bardziej precyzyjnego wyboru monet do wydania, przejdź do zakładki `UTXOs`. Wybierz UTXO, które chcesz wykorzystać, a następnie naciśnij przycisk "Wyślij wybrane", aby zainicjować transakcję.


![sparrow](assets/notext/34.webp)

Wreszcie, opcja `Mix to...` dostępna w Sparrow pozwala na automatyczne usunięcie wybranego UTXO z cykli CoinJoin, bez ponoszenia dodatkowych opłat. Ta funkcja umożliwia określenie liczby remiksów, po których UTXO nie zostanie ponownie zintegrowany z kontem `Postmix`, ale zamiast tego zostanie przeniesiony bezpośrednio do innego Wallet. Ta opcja jest często używana do automatycznego wysyłania zmieszanych bitcoinów do Cold Wallet.

Aby skorzystać z tej opcji, zacznij od otwarcia odbiorcy Wallet obok CoinJoin Wallet w oprogramowaniu Sparrow.


![sparrow](assets/notext/35.webp)


Następnie przejdź do zakładki `UTXOs`, a następnie kliknij przycisk `Mix to...` w dolnej części okna.


![sparrow](assets/notext/36.webp)


Otworzy się okno, w którym należy wybrać docelowy Wallet z listy rozwijanej.


![sparrow](assets/notext/37.webp)


Wybierz próg CoinJoin, po przekroczeniu którego wypłata zostanie dokonana automatycznie. Nie mogę podać dokładnej liczby remiksów do wykonania, ponieważ zależy to od osobistej sytuacji i celów związanych z prywatnością, ale unikaj wybierania zbyt niskiego progu. Zalecam zapoznanie się z tym artykułem, aby dowiedzieć się więcej o procesie remiksowania: [REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


Opcję `Index range` można pozostawić na domyślnej wartości `Full`. Ta funkcja pozwala na jednoczesne miksowanie z różnych klientów, ale nie to chcemy zrobić w tym samouczku. Aby zakończyć i aktywować opcję `Mix to...`, naciśnij `Restart Whirlpool`.


![sparrow](assets/notext/38.webp)


Należy jednak zachować ostrożność podczas korzystania z opcji `Mix to`, ponieważ usunięcie mieszanych monet z konta `Postmix` może znacznie zwiększyć ryzyko naruszenia prywatności. Powody tego potencjału są szczegółowo opisane w poniższych sekcjach.


## Jak poznać jakość naszych cykli CoinJoin?

Aby CoinJoin był naprawdę skuteczny, ważne jest, aby prezentował dobrą jednorodność między kwotami wejść i wyjść. Ta jednorodność zwiększa liczbę możliwych interpretacji w oczach zewnętrznego obserwatora, zwiększając tym samym niepewność wokół transakcji. Aby określić niepewność generowaną przez CoinJoin, można uciec się do obliczenia entropii transakcji. W celu dogłębnego zbadania tych wskaźników odsyłam do samouczka: [KALKULATOR BOLTZMANNA](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe). Model Whirlpool jest uznawany za ten, który zapewnia największą jednorodność w coinjoinach.

Następnie wydajność kilku cykli CoinJoin jest oceniana na podstawie wielkości grup, w których moneta jest ukryta. Rozmiar tych grup definiuje to, co nazywa się anonsets. Istnieją dwa rodzaje anonsetów: pierwszy ocenia prywatność uzyskaną w wyniku analizy retrospektywnej (od teraźniejszości do przeszłości), a drugi w wyniku analizy prospektywnej (od przeszłości do teraźniejszości). Aby uzyskać szczegółowe wyjaśnienie tych dwóch wskaźników, zapraszam do zapoznania się z samouczkiem: [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


## Jak zarządzać postmixem?

Po wykonaniu cykli CoinJoin najlepszą strategią jest przechowywanie UTXO na koncie **postmix**, czekając na ich przyszłe wykorzystanie. Zaleca się nawet pozostawienie ich na koncie remix na czas nieokreślony, dopóki nie będzie trzeba ich wydać.


Niektórzy użytkownicy mogą rozważyć przeniesienie swoich mieszanych bitcoinów do Wallet zabezpieczonego przez Hardware Wallet. Jest to możliwe, ale ważne jest, aby skrupulatnie przestrzegać zaleceń Samourai Wallet, aby nie naruszyć nabytej poufności.


Łączenie UTXO jest najczęściej popełnianym błędem. Konieczne jest unikanie łączenia mieszanych UTXO z niemieszanymi UTXO w tej samej transakcji, aby uniknąć CIOH (*Common-Input-Ownership-Heuristic*). Wymaga to starannego zarządzania UTXO w ramach Wallet, zwłaszcza w zakresie etykietowania. Poza CoinJoin, łączenie UTXO jest ogólnie złą praktyką, która często prowadzi do utraty prywatności, jeśli nie jest odpowiednio zarządzana.


Ważne jest również, aby zachować ostrożność przy konsolidowaniu ze sobą mieszanych UTXO. Umiarkowane konsolidacje są możliwe, jeśli mieszane UTXO mają znaczące anonsety, ale nieuchronnie zmniejszy to poufność monet. Upewnij się, że konsolidacje nie są zbyt duże ani przeprowadzane po niewystarczającej liczbie remiksów, ponieważ grozi to ustanowieniem możliwych do wywnioskowania powiązań między UTXO przed i po cyklach CoinJoin. W przypadku wątpliwości co do tych manipulacji, najlepszą praktyką jest nie konsolidowanie UTXO po mieszaniu i przenoszenie ich pojedynczo do Hardware Wallet, generując za każdym razem nowy pusty Address. Ponownie należy pamiętać o prawidłowym oznaczeniu każdego otrzymanego UTXO.

Odradza się również przenoszenie postmix UTXO do Wallet przy użyciu nietypowych skryptów. Na przykład, jeśli wejdziesz do Whirlpool z Multisig Wallet za pomocą skryptów `P2WSH`, istnieje niewielka szansa, że zostaniesz zmieszany z innymi użytkownikami, którzy pierwotnie mają ten sam typ Wallet. Jeśli wycofasz swój postmix do tego samego Multisig Wallet, poziom prywatności twoich mieszanych bitcoinów zostanie znacznie zmniejszony. Poza skryptami istnieje wiele innych odcisków palców Wallet, które mogą cię oszukać.

Podobnie jak w przypadku każdej transakcji Bitcoin, ważne jest, aby nie używać ponownie adresów odbiorczych. Każda nowa transakcja powinna być odbierana na nowym, pustym Address.


Najprostszym i najbezpieczniejszym rozwiązaniem jest pozostawienie mieszanych UTXO na koncie **postmix**, pozwalając im na remiksowanie i dotykanie ich tylko w celu wydania. Portfele Samourai i Sparrow mają dodatkowe zabezpieczenia przed wszystkimi zagrożeniami związanymi z analizą łańcucha. Zabezpieczenia te pomagają uniknąć błędów.


## Jak zarządzać zmianą doxxic?

Następnie należy zachować ostrożność w zarządzaniu doksyczną zmianą, zmianą, która nie mogła wejść do puli CoinJoin. Te toksyczne UTXO, wynikające z użycia Whirlpool, stanowią zagrożenie dla prywatności użytkownika, ponieważ tworzą powiązanie między użytkownikiem a użyciem CoinJoin. Dlatego konieczne jest ostrożne obchodzenie się z nimi i nie łączenie ich z innymi UTXO, zwłaszcza mieszanymi UTXO. Oto różne strategie, które należy rozważyć podczas korzystania z nich:


- Wymieszaj je w mniejszych basenach:** Jeśli toksyczność UTXO jest wystarczająco duża, aby dostać się do mniejszego basenu, rozważ jego wymieszanie. Często jest to najlepsza opcja. Jednak ważne jest, aby nie łączyć kilku toksycznych UTXO, aby uzyskać dostęp do puli, ponieważ może to połączyć różne wpisy;
- Oznacz je jako "niewydawalne":** Innym podejściem jest nieużywanie ich, oznaczenie ich jako "niewydawalnych" na dedykowanym koncie i po prostu HODL. Gwarantuje to, że nie zostaną one przypadkowo wydane. Jeśli wartość Bitcoin wzrośnie, mogą pojawić się nowe pule bardziej odpowiednie dla toksycznych UTXO;
- Darowizny:** Rozważ przekazanie darowizny, nawet skromnej, deweloperom pracującym nad Bitcoin i powiązanym oprogramowaniem. Możesz również przekazać darowiznę organizacjom akceptującym BTC. Jeśli zarządzanie toksycznymi UTXO wydaje się zbyt skomplikowane, możesz się ich po prostu pozbyć, przekazując darowiznę;
- Kupowanie kart podarunkowych:** Platformy takie jak [Bitrefill](https://www.bitrefill.com/) umożliwiają wymianę bitcoinów Exchange na karty podarunkowe, które można wykorzystać u różnych sprzedawców. Może to być sposób na pozbycie się toksycznych UTXO bez utraty związanej z nimi wartości.
- Skonsoliduj je na Monero:** Samourai Wallet oferuje teraz usługę atomic swap pomiędzy BTC i XMR. Jest to idealne rozwiązanie do zarządzania toksycznymi UTXO poprzez konsolidację ich na Monero, bez narażania prywatności za pośrednictwem CIOH, przed wysłaniem ich z powrotem do Bitcoin. Opcja ta może być jednak kosztowna pod względem opłat Mining i premii ze względu na ograniczenia płynności.
- Przesłanie ich do Lightning Network:** Przeniesienie tych UTXO do Lightning Network w celu skorzystania z obniżonych opłat transakcyjnych jest opcją, która może być interesująca. Jednak ta metoda może ujawnić pewne informacje w zależności od sposobu korzystania z Lightning i dlatego należy ją stosować ostrożnie.


Szczegółowe samouczki dotyczące wdrażania tych różnych technik zostaną wkrótce udostępnione w PlanB Network.


**Dodatkowe zasoby:**

[Samouczek wideo Sparrow Wallet](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

[Samourai Wallet Video Tutorial](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)


- [Dokumentacja Samourai Wallet - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts);
- [Wątek na Twitterze dotyczący CoinJoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Wpis na blogu CoinJoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).