---
name: CoinJoin - Dojo
description: Jak przeprowadzić CoinJoin we własnym Dojo?
---
![cover](assets/cover.webp)


***OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, narzędzie Whirlpool przestało działać, nawet dla osób, które mają własne Dojo lub używają Sparrow Wallet. Możliwe jednak, że narzędzie to zostanie przywrócone w nadchodzących tygodniach lub ponownie uruchomione w inny sposób. Co więcej, teoretyczna część tego artykułu pozostaje istotna dla zrozumienia zasad i celów coinjoinów w ogóle (nie tylko Whirlpool), a także zrozumienia skuteczności modelu Whirlpool.*


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

W tym samouczku dowiesz się, czym jest CoinJoin i jak go wykonać przy użyciu oprogramowania Samourai Wallet i implementacji Whirlpool, wykorzystując własne Dojo. Moim zdaniem ta metoda jest obecnie najlepsza do mieszania bitcoinów.


## Co to jest CoinJoin na Bitcoin?

**CoinJoin to technika, która łamie identyfikowalność bitcoinów na Blockchain**. Opiera się ona na transakcji współpracy o określonej strukturze o tej samej nazwie: transakcji CoinJoin.


Coinjoiny zwiększają prywatność użytkowników Bitcoin, komplikując analizę łańcucha zewnętrznym obserwatorom. Ich struktura umożliwia łączenie wielu monet od różnych użytkowników w jedną transakcję, zacierając w ten sposób ślady i utrudniając określenie powiązań między adresami wejściowymi i wyjściowymi.


Zasada CoinJoin opiera się na podejściu opartym na współpracy: kilku użytkowników, którzy chcą mieszać swoje bitcoiny, wpłaca identyczne kwoty jako dane wejściowe tej samej transakcji. Kwoty te są następnie redystrybuowane jako dane wyjściowe o równej wartości dla każdego użytkownika. Pod koniec transakcji niemożliwe staje się powiązanie konkretnego wyniku ze znanym użytkownikiem na wejściu. Nie istnieje bezpośrednie powiązanie między danymi wejściowymi i wyjściowymi, co zrywa związek między użytkownikami i ich UTXO, a także historią każdej monety.

![coinjoin](assets/notext/1.webp)


Przykład transakcji CoinJoin (nie ode mnie): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Aby wykonać CoinJoin przy jednoczesnym zapewnieniu, że każdy użytkownik zachowuje kontrolę nad swoimi środkami przez cały czas, proces rozpoczyna się od skonstruowania transakcji przez koordynatora, który następnie przesyła ją do uczestników. Następnie każdy użytkownik podpisuje transakcję po sprawdzeniu, czy mu odpowiada. Wszystkie zebrane podpisy są ostatecznie integrowane z transakcją. Jeśli użytkownik lub koordynator podejmie próbę przekierowania środków poprzez modyfikację danych wyjściowych transakcji CoinJoin, podpisy okażą się nieważne, co doprowadzi do odrzucenia transakcji przez węzły.


Istnieje kilka implementacji CoinJoin, takich jak Whirlpool, JoinMarket lub Wabisabi, z których każda ma na celu zarządzanie koordynacją między uczestnikami i zwiększenie wydajności transakcji CoinJoin.

W tym samouczku zagłębimy się w implementację **Whirlpool**, którą uważam za najbardziej wydajne rozwiązanie do wykonywania coinjoinów na Bitcoin. Chociaż jest on dostępny w kilku portfelach, w tym samouczku zbadamy wyłącznie jego użycie z aplikacją mobilną Samourai Wallet, bez Dojo.


## Po co wykonywać coinjoiny na Bitcoin?

Jednym z początkowych problemów każdego systemu płatności peer-to-peer jest podwójne wydawanie pieniędzy: jak zapobiec wielokrotnemu wydawaniu tych samych jednostek pieniężnych przez złośliwe osoby bez uciekania się do arbitrażu centralnego organu?


Satoshi Nakamoto zapewnił rozwiązanie tego dylematu poprzez protokół Bitcoin, elektroniczny system płatności peer-to-peer, który działa niezależnie od jakiegokolwiek organu centralnego. W swojej białej księdze podkreśla, że jedynym sposobem na potwierdzenie braku podwójnych wydatków jest zapewnienie widoczności wszystkich transakcji w systemie płatności.


Aby upewnić się, że każdy uczestnik jest świadomy transakcji, muszą one zostać ujawnione publicznie. W związku z tym działanie Bitcoin opiera się na przejrzystej i rozproszonej infrastrukturze, umożliwiającej każdemu operatorowi węzła weryfikację całości łańcuchów podpisów elektronicznych i historii każdej monety, od jej utworzenia przez Miner.


Przejrzysty i rozproszony charakter Bitcoin oznacza, że każdy użytkownik sieci może śledzić i analizować transakcje wszystkich innych uczestników. W rezultacie anonimowość na poziomie transakcji jest niemożliwa. Anonimowość jest jednak zachowana na poziomie indywidualnej identyfikacji. W przeciwieństwie do tradycyjnego systemu bankowego, w którym każde konto jest powiązane z osobistą tożsamością, w Bitcoin środki są powiązane z parami kluczy kryptograficznych, oferując w ten sposób użytkownikom formę pseudonimowości za identyfikatorami kryptograficznymi.


W ten sposób poufność Bitcoin jest zagrożona, gdy zewnętrzni obserwatorzy zdołają powiązać określone UTXO ze zidentyfikowanymi użytkownikami. Po ustaleniu tego powiązania możliwe staje się śledzenie ich transakcji i analizowanie historii ich bitcoinów. CoinJoin jest właśnie techniką opracowaną w celu przełamania identyfikowalności UTXO, oferując w ten sposób pewną Layer poufność użytkownikom Bitcoin na poziomie transakcji.


## Jak działa Whirlpool?

Whirlpool wyróżnia się na tle innych metod CoinJoin, wykorzystując transakcje "_ZeroLink_", które zapewniają, że nie ma absolutnie żadnego technicznego powiązania między wszystkimi danymi wejściowymi i wszystkimi danymi wyjściowymi. To doskonałe połączenie osiąga się dzięki strukturze, w której każdy uczestnik wnosi identyczną kwotę wkładu (z wyjątkiem opłat Mining), generując w ten sposób produkty wyjściowe o idealnie równych kwotach.

To restrykcyjne podejście do danych wejściowych nadaje transakcjom Whirlpool CoinJoin wyjątkową cechę: całkowity brak deterministycznych powiązań między danymi wejściowymi i wyjściowymi. Innymi słowy, każde wyjście ma równe prawdopodobieństwo przypisania do dowolnego uczestnika, w porównaniu do wszystkich innych wyjść w transakcji.

Początkowo liczba uczestników każdego Whirlpool CoinJoin była ograniczona do 5, z 2 nowymi uczestnikami i 3 remikserami (wyjaśnimy te koncepcje w dalszej części). Jednak wzrost opłat transakcyjnych On-Chain zaobserwowany w 2023 r. skłonił zespoły Samourai do ponownego przemyślenia swojego modelu w celu poprawy prywatności przy jednoczesnym obniżeniu kosztów. Tak więc, biorąc pod uwagę sytuację rynkową opłat i liczbę uczestników, koordynator może teraz organizować coinjoiny obejmujące 6, 7 lub 8 uczestników. Te ulepszone sesje są określane jako "_Surge Cycles_". Należy zauważyć, że niezależnie od konfiguracji, w coinjoinach Whirlpool zawsze biorą udział tylko 2 nowe osoby.


Tak więc transakcje Whirlpool charakteryzują się identyczną liczbą wejść i wyjść, którymi mogą być:


- 5 wejść i 5 wyjść;

![coinjoin](assets/notext/2.webp)


- 6 wejść i 6 wyjść;

![coinjoin](assets/notext/3.webp)


- 7 wejść i 7 wyjść;

![coinjoin](assets/notext/4.webp)


- 8 wejść i 8 wyjść.

![coinjoin](assets/notext/5.webp)

Model zaproponowany przez Whirlpool opiera się zatem na małych transakcjach CoinJoin. W przeciwieństwie do Wasabi i JoinMarket, gdzie solidność anonsetów opiera się na liczbie uczestników w pojedynczym cyklu, Whirlpool stawia na łańcuch wielu małych cykli.


W tym modelu użytkownik uiszcza opłaty tylko przy pierwszym wejściu do puli, co pozwala mu uczestniczyć w wielu remiksach bez dodatkowych opłat. To nowi uczestnicy pokrywają opłaty Mining dla remikserów.


Z każdym dodatkowym CoinJoin, w którym moneta uczestniczy, wraz z jej wcześniej napotkanymi rówieśnikami, anonsety będą rosły wykładniczo. Celem jest zatem skorzystanie z tych darmowych remiksów, które przy każdym wystąpieniu przyczyniają się do zwiększenia gęstości anonsetów powiązanych z każdą mieszaną monetą.


Whirlpool został zaprojektowany z uwzględnieniem dwóch ważnych wymagań:


- Dostępność implementacji na urządzeniach mobilnych, biorąc pod uwagę, że Samourai Wallet jest przede wszystkim aplikacją na smartfony;
- Szybkość cykli remiksowania w celu promowania znacznego wzrostu liczby anonsów.

Te imperatywy kierowały wyborami twórców Samourai Wallet przy projektowaniu Whirlpool, prowadząc ich do ograniczenia liczby uczestników na cykl. Zbyt mała liczba uczestników zagroziłaby wydajności CoinJoin, drastycznie zmniejszając liczbę anonsów generowanych w każdym cyklu, podczas gdy zbyt wielu uczestników stwarzałoby problemy z zarządzaniem aplikacjami mobilnymi i utrudniałoby przepływ cykli.

**Ostatecznie nie ma potrzeby posiadania dużej liczby uczestników na CoinJoin na Whirlpool, ponieważ anonsety są osiągane poprzez akumulację kilku cykli CoinJoin


[-> Dowiedz się więcej o anonsach Whirlpool.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


### Baseny i opłaty CoinJoin

Aby te wielokrotne cykle skutecznie zwiększyły anonsety mieszanych monet, należy ustanowić pewne ramy w celu ograniczenia ilości używanych UTXO. Whirlpool definiuje zatem różne pule.


Pula reprezentuje grupę użytkowników, którzy chcą mieszać się ze sobą, którzy zgadzają się na ilość UTXO do wykorzystania w celu optymalizacji procesu CoinJoin. Każda pula określa stałą ilość UTXO, której użytkownik musi przestrzegać, aby móc w niej uczestniczyć. Tak więc, aby wykonywać coinjoiny z Whirlpool, należy wybrać pulę. Obecnie dostępne są następujące pule:


- 0.5 bitcoinów;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100.000 Sats).


Dołączając do puli ze swoimi bitcoinami, zostaną one podzielone na generate UTXO, które są idealnie jednorodne z tymi innych uczestników puli. Każda pula ma maksymalny limit; w związku z tym, w przypadku kwot przekraczających ten limit, będziesz zmuszony albo dokonać dwóch oddzielnych wpisów w ramach tej samej puli, albo przenieść się do innej puli z wyższą kwotą:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Jak wspomniano wcześniej, UTXO jest uważany za należący do puli, gdy jest gotowy do integracji z CoinJoin. Nie oznacza to jednak, że użytkownik traci nad nim kontrolę. **Poprzez różne cykle mieszania, użytkownik zachowuje pełną kontrolę nad swoimi kluczami, a co za tym idzie, bitcoinami.** To właśnie odróżnia technikę CoinJoin od innych scentralizowanych technik mieszania.


Aby przystąpić do puli CoinJoin, należy uiścić opłaty serwisowe oraz opłaty Mining. Opłaty serwisowe są ustalane dla każdej puli i mają na celu wynagrodzenie zespołów odpowiedzialnych za rozwój i utrzymanie Whirlpool.

Opłaty za korzystanie z Whirlpool należy uiścić tylko raz przy wejściu do puli. Po tym kroku użytkownik ma możliwość uczestniczenia w nieograniczonej liczbie remiksów bez żadnych dodatkowych opłat. Oto aktualne opłaty stałe dla każdej puli:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Opłaty te zasadniczo funkcjonują jako bilet wstępu do wybranej puli, niezależnie od kwoty wpłaconej do CoinJoin. Tak więc, niezależnie od tego, czy dołączysz do puli 0,01 z dokładnie 0,01 BTC, czy wejdziesz do niej z 0,5 BTC, opłaty pozostaną takie same pod względem wartości bezwzględnej.


Przed przejściem do coinjoins użytkownik ma zatem wybór między 2 strategiami:


- Wybierają mniejszą pulę, aby zminimalizować opłaty za usługi, wiedząc, że w zamian otrzymają kilka małych UTXO;
- Lub wolą większą pulę, zgadzając się płacić wyższe opłaty, aby uzyskać mniejszą liczbę UTXO o większej wartości.


Ogólnie rzecz biorąc, odradza się łączenie kilku mieszanych UTXO po cyklach CoinJoin, ponieważ może to zagrozić uzyskanej poufności, zwłaszcza ze względu na heurystykę Common-Input-Ownership (CIOH). W związku z tym rozsądne może być wybranie większej puli, nawet jeśli oznacza to wyższe koszty, aby uniknąć zbyt wielu UTXO o małej wartości na wyjściu. Użytkownik musi rozważyć te kompromisy, aby wybrać preferowaną pulę.


Oprócz opłat za usługi, należy również wziąć pod uwagę opłaty Mining związane z każdą transakcją Bitcoin. Jako użytkownik Whirlpool, będziesz musiał uiścić opłaty Mining za transakcję przygotowawczą (`Tx0`), jak również te za pierwszy CoinJoin. Wszystkie kolejne remiksy będą darmowe, dzięki modelowi Whirlpool, który opiera się na płatnościach nowych uczestników.


Rzeczywiście, w każdym Whirlpool CoinJoin dwóch użytkowników wśród wejść to nowi uczestnicy. Pozostałe dane wejściowe pochodzą od remikserów. W rezultacie opłaty za Mining dla wszystkich uczestników transakcji są pokrywane przez tych dwóch nowych uczestników, którzy następnie również skorzystają z bezpłatnych remiksów:

![coinjoin](assets/en/6.webp)

Dzięki temu systemowi opłat Whirlpool naprawdę odróżnia się od innych usług CoinJoin, ponieważ anonimowość UTXO nie jest proporcjonalna do ceny płaconej przez użytkownika. W ten sposób można osiągnąć znacznie wysoki poziom anonimowości, płacąc jedynie opłatę za wejście do puli i opłaty Mining za dwie transakcje (`Tx0` i początkowy mix).

Ważne jest, aby pamiętać, że użytkownik będzie musiał również pokryć opłaty Mining, aby wycofać swoje UTXO z puli po zakończeniu wielu coinjoinów, chyba że wybrał opcję `mix to`, którą omówimy w samouczku poniżej.


### Konta HD Wallet używane przez Whirlpool

Aby wykonać CoinJoin poprzez Whirlpool, Wallet musi generate kilka odrębnych kont. Konto, w kontekście HD (*Hierarchical Deterministic*) Wallet, stanowi sekcję całkowicie odizolowaną od innych, ta separacja występuje na trzecim poziomie głębokości hierarchii Wallet, czyli na poziomie `xpub`.


HD Wallet może teoretycznie wyprowadzić do `2^(32/2)` różnych kont. Początkowe konto, używane domyślnie we wszystkich portfelach Bitcoin, odpowiada indeksowi `0'`.


W przypadku portfeli dostosowanych do Whirlpool, takich jak Samourai lub Sparrow, używane są 4 konta, aby zaspokoić potrzeby procesu CoinJoin:


- Konto **depozytowe**, identyfikowane przez indeks `0`;
- Konto **złego banku** (lub doxxic change), identyfikowane przez indeks `2 147 483 644'`;
- Konto **premix**, identyfikowane przez indeks `2 147 483 645'`;
- Konto **postmix**, identyfikowane przez indeks `2 147 483 646'`.


Każde z tych kont spełnia określoną funkcję w ramach CoinJoin.


Wszystkie te konta są powiązane z pojedynczym seed, co pozwala użytkownikowi odzyskać dostęp do wszystkich swoich bitcoinów za pomocą frazy odzyskiwania i, w razie potrzeby, passphrase. Konieczne jest jednak określenie w oprogramowaniu, podczas tej operacji odzyskiwania, różnych indeksów kont, które zostały użyte.


Przyjrzyjmy się teraz różnym etapom Whirlpool CoinJoin w ramach tych kont.


### Różne etapy coinjoinów na Whirlpool

**Etap 1: Tx0**

Punktem wyjścia dla każdego Whirlpool CoinJoin jest konto **depozytowe**. To konto jest automatycznie używane podczas tworzenia nowego Bitcoin Wallet. To konto musi być zasilone bitcoinami, które chcemy wymieszać.

`Tx0` reprezentuje pierwszy krok w procesie mieszania Whirlpool. Ma on na celu przygotowanie i wyrównanie UTXO dla CoinJoin, poprzez podzielenie ich na jednostki odpowiadające ilości wybranej puli, aby zapewnić jednorodność mieszania. Wyrównane UTXO są następnie wysyłane na konto **premix**. Jeśli chodzi o różnicę, która nie może wejść do puli, jest ona oddzielana na specjalnym koncie: **bad bank** (lub "doxxic change").

Ta początkowa transakcja `Tx0` służy również do rozliczenia opłat za usługę należnych koordynatorowi mix. W przeciwieństwie do kolejnych kroków, ta transakcja nie jest oparta na współpracy; użytkownik musi zatem ponieść wszystkie opłaty Mining:

![coinjoin](assets/en/7.webp)


W tym przykładzie transakcji `Tx0`, wejście `372,000 Sats` z naszego **depozytowego** konta jest dzielone na kilka wyjściowych UTXO, które są rozdzielane w następujący sposób:


- Kwota `5.000 Sats` przeznaczona dla koordynatora na opłaty za usługi, odpowiadająca wejściu do puli `100.000 Sats`;
- Trzy UTXO przygotowane do mieszania, przekierowane na nasze konto **premix** i zarejestrowane u koordynatora. Te UTXO są wyrównane na `108,000 Sats` każdy, aby pokryć opłaty Mining za ich przyszłe wstępne mieszanie;
- Nadwyżka, która nie może wejść do puli, ponieważ jest zbyt mała, jest uważana za toksyczną zmianę. Jest ona wysyłana na określone konto. W tym przypadku zmiana ta wynosi `40 000 Sats`;
- Wreszcie, istnieje `3,000 Sats`, które nie stanowią wyjścia, ale są opłatami Mining niezbędnymi do potwierdzenia `Tx0`.


Na przykład, oto prawdziwy Whirlpool Tx0 (nie ode mnie): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**Krok 2: Zmiana doxxic**

Nadwyżka, która nie mogła zostać zintegrowana z pulą, tutaj odpowiadająca `40 000 Sats`, jest przekierowywana na konto **bad bank**, określane również jako "doxxic change", aby zapewnić ścisłe oddzielenie od innych UTXO w Wallet.


Ten UTXO jest niebezpieczny dla prywatności użytkownika, ponieważ nie tylko jest nadal powiązany z jego przeszłością, a zatem prawdopodobnie z tożsamością jego właściciela, ale dodatkowo jest odnotowany jako należący do użytkownika, który wykonał CoinJoin.

Jeśli ten UTXO zostanie połączony z mieszanymi danymi wyjściowymi, utracą one całą poufność uzyskaną podczas cykli CoinJoin, zwłaszcza z powodu algorytmu Common-Input-Ownership-Heuristic (CIOH). Jeśli zostanie połączony z innymi zmianami doxxic, użytkownik ryzykuje utratę poufności, ponieważ połączy różne dane wejściowe cykli CoinJoin. Dlatego należy obchodzić się z nim ostrożnie. Sposób zarządzania tym toksycznym UTXO zostanie szczegółowo opisany w ostatniej części tego artykułu, a przyszłe samouczki omówią te metody bardziej szczegółowo w PlanB Network.


**Krok 3: Początkowa mieszanka**

Po zakończeniu `Tx0`, wyrównane UTXO są wysyłane do konta **premix** naszego Wallet, gotowe do wprowadzenia do ich pierwszego cyklu CoinJoin, zwanego również "początkowym miksem". Jeśli, jak w naszym przykładzie, `Tx0` generuje kilka UTXO przeznaczonych do mieszania, każdy z nich zostanie zintegrowany z oddzielnym początkowym CoinJoin.


Pod koniec tych pierwszych miksów konto **premix** będzie puste, podczas gdy nasze monety, po uiszczeniu opłat Mining za ten pierwszy CoinJoin, zostaną dostosowane dokładnie do kwoty określonej przez wybraną pulę. W naszym przykładzie, nasze początkowe UTXO w wysokości `108 000 Sats` zostanie zredukowane do dokładnie `100 000 Sats`.

![coinjoin](assets/en/8.webp)

**Krok 4: Remiksy**

Po wstępnym zmiksowaniu UTXO są przenoszone na konto **postmix**. To konto gromadzi już zmiksowane UTXO i te, które czekają na ponowne zmiksowanie. Gdy klient Whirlpool jest aktywny, UTXO znajdujące się na koncie **postmix** są automatycznie dostępne do remiksowania i zostaną losowo wybrane do udziału w tych nowych cyklach.


Przypominamy, że remiksy są wtedy w 100% darmowe: nie są wymagane żadne dodatkowe opłaty za usługi ani opłaty Mining. Utrzymywanie UTXO na koncie **postmix** utrzymuje zatem ich wartość w stanie nienaruszonym i jednocześnie poprawia ich anonsety. Dlatego ważne jest, aby umożliwić tym monetom udział w wielu cyklach CoinJoin. To nic nie kosztuje, a zwiększa ich poziom anonimowości.


Jeśli zdecydujesz się wydać zmiksowane UTXO, możesz to zrobić bezpośrednio z tego konta **postmix**. Zaleca się przechowywanie zmiksowanych UTXO na tym koncie, aby skorzystać z darmowych remiksów i uniknąć opuszczenia obwodu Whirlpool, co mogłoby zmniejszyć ich poufność.


Jak zobaczymy w poniższym samouczku, istnieje również opcja `mix to`, która oferuje możliwość automatycznego wysyłania zmieszanych monet do innego Wallet, takiego jak Cold Wallet, po określonej liczbie połączeń monet.

Po omówieniu teorii, przejdźmy do praktyki z samouczkiem na temat korzystania z Whirlpool za pośrednictwem aplikacji Samourai Wallet na Androida, zsynchronizowanej z Whirlpool CLI i GUI na własnym Dojo!

## Samouczek: CoinJoin Whirlpool z własnym Dojo

Istnieje wiele opcji korzystania z Whirlpool. Tą, którą chcę tutaj przedstawić, jest opcja Samourai Wallet, aplikacja open-source do zarządzania Bitcoin Wallet na Androida, ale tym razem **z własnym Dojo**.


Wykonywanie coinjoinów za pośrednictwem Samourai Wallet przy użyciu własnego Dojo jest moim zdaniem najskuteczniejszą jak dotąd strategią przeprowadzania coinjoinów na Bitcoin. Podejście to wymaga pewnych początkowych inwestycji w zakresie konfiguracji, ale po wdrożeniu oferuje możliwość mieszania i remiksowania bitcoinów w sposób ciągły, 24 godziny na dobę, 7 dni w tygodniu, bez konieczności utrzymywania aktywnej aplikacji Samourai przez cały czas. Rzeczywiście, dzięki Whirlpool CLI działającemu na węźle Bitcoin, jesteś zawsze gotowy do udziału w coinjoinach. Aplikacja Samourai daje wtedy możliwość wydawania mieszanych środków w dowolnym momencie, gdziekolwiek jesteś, bezpośrednio ze smartfona. Co więcej, ta metoda ma tę zaletę, że nigdy nie łączy cię z serwerami zarządzanymi przez zespoły Samourai, chroniąc w ten sposób twój `xpub` przed jakąkolwiek ekspozycją zewnętrzną.


Technika ta jest zatem idealna dla osób poszukujących maksymalnej prywatności i najwyższej jakości cykli CoinJoin. Wymaga jednak posiadania do dyspozycji węzła Bitcoin i, jak zobaczymy później, wymaga pewnej konfiguracji. Jest więc bardziej odpowiedni dla średnio zaawansowanych i zaawansowanych użytkowników. Początkującym polecam zapoznanie się z CoinJoin za pomocą tych dwóch innych samouczków, które pokazują, jak to zrobić z Sparrow Wallet lub Samourai Wallet (bez Dojo):


- [Sparrow Wallet CoinJoin tutorial](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b)**;
- [Samourai Wallet CoinJoin tutorial (without Dojo)](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)**.


### Zrozumienie konfiguracji

Aby rozpocząć, będziesz potrzebował Dojo! Dojo to implementacja węzła Bitcoin oparta na Bitcoin Core, opracowana przez zespoły Samourai.


Aby uruchomić własne Dojo, masz możliwość zainstalowania węzła Dojo autonomicznie lub skorzystania z Dojo na innym rozwiązaniu węzła Bitcoin "node-in-box". Obecnie dostępne opcje to:


- [RoninDojo](https://ronindojo.io/), który jest Dojo wzbogaconym o dodatkowe narzędzia, w tym asystenta instalacji i asystenta administracyjnego. Szczegółową procedurę konfiguracji i korzystania z RoninDojo opisałem w tym poradniku: [RONINDOJO V2](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8);
- [Umbrel](https://umbrel.com/) z aplikacją "Samourai Server";
- [MyNode](https://mynodebtc.com/) z aplikacją "Dojo";
- [Nodl](https://www.nodl.eu/) z aplikacją "Dojo";
- [Cytadela](https://runcitadel.space/) z aplikacją "Samourai".

![coinjoin](assets/notext/9.webp)

W naszej konfiguracji będziemy wchodzić w interakcje z trzema różnymi interfejsami:


- Samourai Wallet**, który będzie hostował nasze Bitcoin Wallet dedykowane coinjoinom. Dostępna za darmo na Androida, ta aplikacja FOSS pozwala kontrolować miksowanie Wallet, szczególnie w przypadku wydawania postmixów ze smartfona;
- Whirlpool CLI** (_Command Line Interface_), który będzie działał na węźle hostującym Dojo. Oprogramowanie to będzie miało dostęp do kluczy Samourai Wallet. Jest ono odpowiedzialne za komunikację z koordynatorem i ciągłe zarządzanie coinjoinami. Działa jako kopia Samourai Wallet na węźle, gotowa do udziału w coinjoinach w dowolnym momencie;
- Whirlpool GUI** (_Graphical User Interface_), graficzny interfejs użytkownika Interface, którego będziemy używać do monitorowania aktywności Whirlpool CLI i zdalnego inicjowania mieszania. Whirlpool GUI zapewnia wizualną reprezentację operacji wykonywanych przez Whirlpool CLI. Oprogramowanie to musi być zainstalowane na komputerze oddzielnym od Dojo. Dla użytkowników Umbrel, MyNode, Nodl i Citadel, Whirlpool GUI jest obowiązkowy. Jednakże, z RoninDojo, Whirlpool GUI Interface jest już zintegrowany z Interface web węzła poprzez aplikację `Whirlpool`. Dlatego nie trzeba instalować go na oddzielnym komputerze.


Moim zdaniem korzystanie z RoninDojo stanowi najlepsze rozwiązanie do wykonywania coinjoinów z Dojo. Ponieważ to oprogramowanie node-in-box jest w bezpośredniej współpracy z zespołami Samourai, RoninDojo jest znacznie bardziej zoptymalizowany do tego celu. Co więcej, integracja Whirlpool GUI z Interface znacznie upraszcza proces konfiguracji. W tym samouczku wyjaśnię jeszcze, jak to zrobić z innymi rozwiązaniami integrującymi Dojo (Umbrel, Nodl, MyNode i Citadel).


### Przygotowanie Dojo

Aby rozpocząć, musisz zainstalować Dojo i uzyskać kod QR lub link, który pozwoli ci połączyć się z nim zdalnie. Ten link to Tor Address kończący się na `.onion`. Jeśli korzystasz z RoninDojo, po prostu przejdź do menu `Pairing`, aby uzyskać dostęp do tych informacji.

![coinjoin](assets/notext/10.webp)


Poniżej `Samourai Dojo`, kliknij na przycisk `Paruj teraz`.


![coinjoin](assets/notext/11.webp)


Wyświetlony zostanie kod QR połączenia i odpowiedni link.


![coinjoin](assets/notext/12.webp)


Jeśli korzystasz z Umbrel, przejdź do App Store i wyszukaj aplikację `Samourai Server`. Znajduje się ona w zakładce `Bitcoin`.


![coinjoin](assets/notext/13.webp)


Zainstaluj aplikację.


![coinjoin](assets/notext/14.webp)


Po otwarciu aplikacji uzyskasz dostęp do kodu QR umożliwiającego połączenie z Dojo.


![coinjoin](assets/notext/15.webp)


Jeśli korzystasz z innego oprogramowania typu node-in-box, takiego jak MyNode, Citadel lub Nodl, proces jest podobny do tego z Umbrel. Musisz zainstalować aplikację Samourai lub Dojo, aby uzyskać niezbędne informacje do połączenia się z Dojo.


![coinjoin](assets/notext/16.webp)


### Przygotowanie Samourai Wallet

Po pobraniu informacji o połączeniu z Dojo, nadszedł czas, aby skonfigurować Wallet do coinjoinów. Istnieją dwa scenariusze: jeśli nie masz jeszcze Samourai Wallet na swoim smartfonie, proces jest prosty, wystarczy utworzyć nowy.


Z drugiej strony, jeśli posiadasz już Samourai Wallet, będziesz musiał ponownie zainstalować aplikację, aby powiązać ją z nowym Dojo. Ten krok jest konieczny, ponieważ połączenie z Dojo można nawiązać tylko przy pierwszym uruchomieniu aplikacji. Jednak dzięki automatycznie generowanemu przez Samourai zaszyfrowanemu plikowi kopii zapasowej na telefonie procedura ta jest prosta i szybka.


*Jeśli nigdy nie korzystałeś z Samourai, możesz pominąć te wstępne kroki i przejść bezpośrednio do instalacji aplikacji*


Przede wszystkim należy upewnić się, że aplikacja Samourai Wallet jest aktualna. Aby to zrobić, sprawdź Sklep Google Play lub porównaj wersję aplikacji w `Ustawienia > Inne` z wersją dostępną na stronie Samourai.


![coinjoin](assets/notext/17.webp)


Upewnij się, że masz frazę odzyskiwania Samourai Wallet i że jest ona czytelna. Następnie przeprowadź test BIP39 passphrase, przechodząc do `Ustawienia > Rozwiązywanie problemów > passphrase/Test kopii zapasowej`, aby potwierdzić jego dokładność.


![coinjoin](assets/notext/18.webp)

Wprowadź swój passphrase, a następnie sprawdź, czy Samourai potwierdza jego ważność.

![coinjoin](assets/notext/19.webp)


Jeśli twój passphrase jest nieważny lub jeśli nie masz frazy odzyskiwania, konieczne jest natychmiastowe przerwanie procedury! **W takim przypadku zaleca się przeniesienie środków do innego Wallet i rozpoczęcie od nowego pustego Samourai Wallet. Poniższe kroki należy wykonać tylko wtedy, gdy masz pewność, że masz wszystkie niezbędne informacje zapasowe i że twój passphrase jest ważny.


Następnie utwórz zaszyfrowaną kopię zapasową Wallet i skopiuj ją do schowka. Aby wykonać tę operację, kliknij trzy małe kropki znajdujące się w prawym górnym rogu ekranu, a następnie wybierz `Export Wallet backup`.


![coinjoin](assets/notext/20.webp)


**Od tego momentu nie kopiuj niczego innego do schowka!** Zachowanie skopiowanej kopii zapasowej jest absolutnie konieczne.


Jeśli poprawnie wykonałeś poprzednie kroki, możesz teraz bezpiecznie usunąć Samourai Wallet. Aby to zrobić, przejdź do: `Ustawienia > Wallet > Bezpieczne kasowanie Wallet`.


![coinjoin](assets/notext/21.webp)


![coinjoin](assets/notext/22.webp)


*Jeśli nigdy nie korzystałeś z Samourai i instalujesz aplikację od zera, możesz wznowić samouczek na tym etapie


Aplikacja Samourai została zresetowana. Otwórz aplikację i wykonaj kroki konfiguracji tak, jakbyś używał jej po raz pierwszy.


![coinjoin](assets/notext/23.webp)


W następnym kroku uzyskasz dostęp do strony poświęconej konfiguracji Dojo. Wybierz opcję `Dojo`, a następnie wprowadź dane logowania do Dojo. Aby to zrobić, możesz zeskanować informacje, naciskając `Scan QR`.


![coinjoin](assets/notext/24.webp)


*W przypadku nowych użytkowników Samourai konieczne będzie utworzenie Wallet od podstaw. Jeśli potrzebujesz pomocy, możesz zapoznać się z instrukcjami konfiguracji nowego Samourai Wallet [w tym samouczku, w szczególności w sekcji "Tworzenie Software Wallet"](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)*


Jeśli kontynuujesz przywracanie już istniejącego Samourai Wallet, wybierz `Przywróć istniejący Wallet`, a następnie wybierz `Mam plik kopii zapasowej Samourai`.


![coinjoin](assets/notext/25.webp)

Zwykle plik odzyskiwania powinien zawsze znajdować się w schowku. Następnie kliknij `PASTE`, aby wstawić plik do wyznaczonej lokalizacji. Aby go odszyfrować, konieczne będzie również wprowadzenie BIP39 passphrase twojego Wallet w odpowiednim polu, znajdującym się tuż poniżej. Aby zakończyć, kliknij `FINISH`.

![coinjoin](assets/notext/26.webp)


Następnie zostaniesz przekierowany do swojego Samourai Wallet, który tym razem będzie połączony z twoim własnym Dojo.


![coinjoin](assets/notext/27.webp)


### Instalacja Whirlpool GUI

Nadszedł czas, aby zainstalować Whirlpool GUI, graficznego użytkownika Interface, który pozwoli ci zarządzać cyklami CoinJoin z poziomu zwykłego komputera. Dla użytkowników RoninDojo ten krok nie jest konieczny, ponieważ zarządzanie coinjoinami może odbywać się bezpośrednio przez Interface w `Apps > Whirlpool`. Jeśli jednak korzystasz z innego rozwiązania Bitcoin "node-in-box", koniecznie wykonaj tę instalację.

![coinjoin](assets/notext/28.webp)

Przejdź do komputera osobistego i pobierz oprogramowanie Whirlpool z oficjalnej strony internetowej Samourai Wallet, wybierając wersję odpowiadającą Twojemu systemowi operacyjnemu.


![coinjoin](assets/notext/29.webp)


Przed uruchomieniem Whirlpool GUI, konieczne jest zainstalowanie JAVA 8 lub wyższej wersji na komputerze. W tym celu [można zainstalować OpenJDK](https://adoptium.net/).

![coinjoin](assets/notext/30.webp)

Konieczne jest również, aby Tor daemon lub Tor Browser działały w tle na komputerze. Upewnij się, że uruchamiasz Tora przed każdą sesją Whirlpool GUI. Jeśli Tor nie jest jeszcze zainstalowany na twoim komputerze, [możesz go pobrać i zainstalować z oficjalnej strony projektu](https://www.torproject.org/download/), upewnij się, że uruchomiłeś go w tle.


![coinjoin](assets/notext/31.webp)


Po zainstalowaniu JDK w systemie i uruchomieniu Tora w tle, można uruchomić Whirlpool GUI.


![coinjoin](assets/notext/32.webp)


W GUI Whirlpool kliknij `Zaawansowane: Remote CLI`, aby podłączyć Whirlpool CLI, który znajduje się w Dojo. Będziesz potrzebował Tor Address swojego Whirlpool CLI.


![coinjoin](assets/notext/33.webp)


Aby zlokalizować Tor Address na Umbrel i innych rozwiązaniach "node-in-box", wystarczy uruchomić serwer Samourai lub aplikację Dojo (nazwa może się różnić w zależności od używanego oprogramowania). Tor Address będzie bezpośrednio widoczny na stronie aplikacji.

![coinjoin](assets/notext/34.webp)

W Whirlpool GUI wprowadź uzyskany wcześniej Tor Address w polu `CLI Address`. Zachowaj prefiks `http://`, ale nie dodawaj portu `:8899` na końcu. Wklej tylko Address w takiej postaci, w jakiej został ci dostarczony.

![coinjoin](assets/notext/35.webp)


W polu Tor Proxy wpisz `socks5://127.0.0.1:9050`, jeśli używasz Tor daemon, lub `socks5://127.0.0.1:9150`, jeśli jest to Tor Browser. Podczas pierwszego połączenia z Whirlpool CLI za pośrednictwem Whirlpool GUI, możliwe jest pozostawienie pustego pola klucza API. Jeśli nie jest to pierwsze połączenie, wprowadź klucz API w dedykowanym miejscu. Klucz ten znajduje się na tej samej stronie co klucz Tor Address.


![coinjoin](assets/notext/36.webp)


Po wypełnieniu wszystkich pól kliknij przycisk "Połącz". Poczekaj, połączenie może potrwać kilka minut.


![coinjoin](assets/notext/37.webp)


### Parowanie Samourai Wallet z Whirlpool GUI

*Użytkownicy RoninDojo mogą wznowić samouczek tutaj


Teraz sparujemy Samourai Wallet, który skonfigurowaliśmy wcześniej z oprogramowaniem Whirlpool GUI lub bezpośrednio z RoninDojo dla tych, którzy używają tego oprogramowania. Niezależnie od tego, czy korzystasz z Whirlpool GUI, czy RoninDojo, zostaniesz poproszony o wklejenie lub zeskanowanie informacji o parowaniu Samourai Wallet.


![coinjoin](assets/notext/38.webp)


Aby znaleźć te informacje, przejdź do ustawień Wallet.


![coinjoin](assets/notext/39.webp)


Kliknij `Transakcje`, a następnie `Paruj z Whirlpool GUI`.


![coinjoin](assets/notext/40.webp)


Następnie Samourai przekaże informacje niezbędne do nawiązania połączenia. Bądź ostrożny, te dane są wrażliwe! Można je przesłać do komputera, kopiując je bezpośrednio lub skanując wyświetlony kod QR za pomocą kamery internetowej komputera po kliknięciu symbolu kodu QR.


![coinjoin](assets/notext/41.webp)


Po wykonaniu tej operacji, w Whirlpool GUI, wybierz `Initialize GUI`. Poczekaj, ponieważ ten krok może chwilę potrwać.


![coinjoin](assets/notext/42.webp)


Niezależnie od tego, czy używasz Whirlpool GUI czy RoninDojo, zostaniesz poproszony o wprowadzenie passphrase twojego Samourai Wallet. Wprowadź go w dedykowanym polu, a następnie naciśnij przycisk `Login`, aby kontynuować.


![coinjoin](assets/notext/43.webp)


Zostaniesz przeniesiony na stronę główną Whirlpool CLI


![coinjoin](assets/notext/44.webp)


### Inicjowanie koincydencji z poziomu Whirlpool GUI

*Dla użytkowników RoninDojo proces jest identyczny. Aplikacja Whirlpool Interface zintegrowana z RoninDojo oferuje te same opcje i funkcje, co oprogramowanie Whirlpool GUI na komputerze. Dlatego można postępować zgodnie z tymi instrukcjami w ten sam sposób

Teraz, gdy wszystko jest już skonfigurowane, możesz zacząć mieszać swoje bitcoiny. Aby to zrobić, przelej bitcoiny, które chcesz wymieszać, na konto **Deposit** swojego Samourai Wallet. Operację tę można przeprowadzić bezpośrednio za pomocą aplikacji Samourai Wallet lub interfejsu graficznego Whirlpool. Na stronie głównej kliknij przycisk `+ Depozyt` znajdujący się w lewym górnym rogu.


![coinjoin](assets/notext/45.webp)


Whirlpool GUI będzie generate odbierającym Address. Wyświetli również minimalną kwotę wymaganą do uczestnictwa w każdej puli CoinJoin. Kwota ta różni się w zależności od rynku opłat. Zaleca się zdeponowanie kwoty nieco wyższej niż wymagane minimum, ponieważ jeśli opłaty Mining nie spadną, UTXO może nie zostać zaakceptowany w żądanej puli. Dlatego też należy wysłać swoje bitcoiny na podany Address. Aby otrzymać nowy Address, wystarczy kliknąć przycisk "Odnów Address".


![coinjoin](assets/notext/46.webp)


Po potwierdzeniu wpłaty będzie ona widoczna na koncie **Depozyt** w Whirlpool GUI.


![coinjoin](assets/notext/47.webp)


Aby uruchomić cykle CoinJoin, wybierz UTXO, które chcesz wymieszać i naciśnij przycisk `Premix`. Uważaj: jeśli wybierzesz kilka różnych UTXO w tym samym czasie, zostaną one połączone podczas transakcji przygotowawczej `TX0`. To połączenie może prowadzić do zmniejszenia prywatności, zwłaszcza jeśli UTXO pochodzą z różnych źródeł, ze względu na algorytm CIOH (Common Input Ownership Heuristic).


![coinjoin](assets/notext/48.webp)


Otworzy się strona konfiguracji Whirlpool. Możesz wybrać pulę, do której chcesz wejść. Należy również wybrać opłaty Mining dedykowane dla `TX0` i pierwszych coinjoinów. Na dole tej strony znajduje się podsumowanie przedstawiające kwotę zmiany doxxic, a także kwotę i liczbę UTXO, które zostaną wyrównane i uwzględnione w cyklach CoinJoin. Jeśli jesteś zadowolony z tej konfiguracji, naciśnij przycisk `Premix`, aby rozpocząć cykle CoinJoin.

![coinjoin](assets/notext/49.webp)


Po utworzeniu `TX0` będziesz mógł zobaczyć swoje wyrównane UTXO na koncie **Premix**, czekając na potwierdzenie. Aby umożliwić automatyczne remiksowanie monet 24 godziny na dobę, 7 dni w tygodniu, zalecam aktywowanie opcji `Automatycznie mieszaj premiks i postmiks`. Funkcję tę można znaleźć w zakładce `Konfiguracja`, znajdującej się po lewej stronie okna GUI Whirlpool.

![coinjoin](assets/notext/50.webp)

Po rozpoczęciu coinjoinów, możesz opuścić GUI Whirlpool, jak również Samourai Wallet. Tylko twój węzeł musi pozostać podłączony, aby móc uczestniczyć w ciągłych coinjoinach. Zaleca się jednak okresowe sprawdzanie postępu cykli CoinJoin. Jeśli zauważysz, że twoje UTXO nie są już wybierane do CoinJoin przez jakiś czas, może to oznaczać błąd. W takim przypadku przejdź do Whirlpool CLI i wybierz `Start`, aby ponownie uruchomić dostępność dla coinjoinów.


![coinjoin](assets/notext/51.webp)


Twoje mieszane UTXO są widoczne z konta **Postmix** na Whirlpool GUI. Dodatkowo masz możliwość przeglądania i wydawania ich bezpośrednio przez Whirlpool Interface na Samourai Wallet. Aby uzyskać dostęp do tego menu, kliknij niebieski `+` na dole ekranu, a następnie wybierz `Whirlpool`.


![coinjoin](assets/notext/52.webp)


Konta Whirlpool są łatwo rozpoznawalne na Samourai Wallet dzięki niebieskiemu kolorowi. Pozwala to na wydawanie mieszanych UTXO z dowolnego miejsca i w dowolnym czasie, bezpośrednio ze smartfona.


![coinjoin](assets/notext/53.webp)


Aby śledzić automatyczne coinjoiny, zalecam również skonfigurowanie Watch-only wallet za pośrednictwem aplikacji Sentinel. Dodaj ZPUB swojego konta **Postmix** i monitoruj postęp swoich cykli CoinJoin w czasie rzeczywistym. Jeśli chcesz zrozumieć, jak korzystać z Sentinel, polecam zapoznać się z tym innym samouczkiem na PlanB Network: [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)