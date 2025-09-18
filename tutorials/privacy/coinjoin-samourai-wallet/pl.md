---
name: Coinjoin - Samourai Wallet
description: Jak wykonać CoinJoin na Samourai Wallet?
---
![cover](assets/cover.webp)


***OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, narzędzie Whirlpool przestało działać, nawet dla osób, które mają własne Dojo lub używają Sparrow Wallet. Możliwe jednak, że narzędzie to zostanie przywrócone w nadchodzących tygodniach lub ponownie uruchomione w inny sposób. Co więcej, teoretyczna część tego artykułu pozostaje istotna dla zrozumienia zasad i celów coinjoinów w ogóle (nie tylko Whirlpool), a także zrozumienia skuteczności modelu Whirlpool.*


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

> *gW-6 Wallet dla ulic*

W tym samouczku dowiesz się, czym jest CoinJoin i jak go wykonać za pomocą oprogramowania Samourai Wallet i implementacji Whirlpool.


## Co to jest CoinJoin na Bitcoin?

**CoinJoin to technika, która łamie identyfikowalność bitcoinów na Blockchain**. Opiera się ona na wspólnej transakcji o określonej strukturze o tej samej nazwie: transakcji CoinJoin.


Coinjoiny zwiększają prywatność użytkowników Bitcoin, komplikując analizę łańcucha zewnętrznym obserwatorom. Ich struktura umożliwia łączenie wielu monet od różnych użytkowników w jedną transakcję, zaciemniając w ten sposób ślady i utrudniając określenie powiązań między adresami wejściowymi i wyjściowymi.


Zasada CoinJoin opiera się na podejściu opartym na współpracy: kilku użytkowników, którzy chcą mieszać swoje bitcoiny, wpłaca identyczne kwoty jako dane wejściowe tej samej transakcji. Kwoty te są następnie redystrybuowane jako dane wyjściowe o równej wartości dla każdego użytkownika. Pod koniec transakcji niemożliwe staje się powiązanie konkretnego wyniku ze znanym użytkownikiem na wejściu. Nie istnieje bezpośrednie powiązanie między danymi wejściowymi i wyjściowymi, zrywając powiązanie między użytkownikami i ich UTXO, a także historią każdej monety.

![coinjoin](assets/notext/1.webp)


Przykład transakcji CoinJoin (nie ode mnie): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Aby wykonać CoinJoin przy jednoczesnym zapewnieniu, że każdy użytkownik zachowuje kontrolę nad swoimi środkami przez cały czas, proces rozpoczyna się od skonstruowania transakcji przez koordynatora, który następnie przesyła ją do uczestników. Następnie każdy użytkownik podpisuje transakcję po sprawdzeniu, czy mu odpowiada. Wszystkie zebrane podpisy są ostatecznie integrowane z transakcją. Jeśli użytkownik lub koordynator podejmie próbę przekierowania środków, modyfikując dane wyjściowe transakcji CoinJoin, podpisy okażą się nieważne, co doprowadzi do odrzucenia transakcji przez węzły.


Istnieje kilka implementacji CoinJoin, takich jak Whirlpool, JoinMarket lub Wabisabi, z których każda ma na celu zarządzanie koordynacją między uczestnikami i zwiększenie wydajności transakcji CoinJoin.

W tym samouczku zagłębimy się w implementację **Whirlpool**, którą uważam za najbardziej wydajne rozwiązanie do wykonywania coinjoinów na Bitcoin. Chociaż jest on dostępny w kilku portfelach, w tym samouczku zbadamy jego użycie wyłącznie z aplikacją mobilną Samourai Wallet, bez Dojo.


## Dlaczego warto wykonywać coinjoiny na Bitcoin?

Jednym z początkowych problemów każdego systemu płatności peer-to-peer jest podwójne wydawanie pieniędzy: jak zapobiec wielokrotnemu wydawaniu tych samych jednostek pieniężnych przez złośliwe osoby bez uciekania się do arbitrażu centralnego organu?


Satoshi Nakamoto zapewnił rozwiązanie tego dylematu poprzez protokół Bitcoin, elektroniczny system płatności peer-to-peer, który działa niezależnie od jakiegokolwiek organu centralnego. W swojej białej księdze podkreśla, że jedynym sposobem na potwierdzenie braku podwójnych wydatków jest zapewnienie widoczności wszystkich transakcji w systemie płatności.


Aby zagwarantować, że każdy uczestnik jest świadomy transakcji, muszą one zostać ujawnione publicznie. W związku z tym działanie Bitcoin opiera się na przejrzystej i rozproszonej infrastrukturze, umożliwiającej każdemu operatorowi węzła weryfikację całości łańcuchów podpisów elektronicznych i historii każdej monety, od momentu jej utworzenia przez Miner.


Przejrzysty i rozproszony charakter Bitcoin oznacza, że każdy użytkownik sieci może śledzić i analizować transakcje wszystkich innych uczestników. W rezultacie anonimowość na poziomie transakcji jest niemożliwa. Anonimowość jest jednak zachowana na poziomie indywidualnej identyfikacji. W przeciwieństwie do tradycyjnego systemu bankowego, w którym każde konto jest powiązane z osobistą tożsamością, w Bitcoin środki są powiązane z parami kluczy kryptograficznych, oferując w ten sposób użytkownikom formę pseudonimowości za identyfikatorami kryptograficznymi.


W ten sposób poufność Bitcoin jest zagrożona, gdy zewnętrznym obserwatorom uda się powiązać określone UTXO ze zidentyfikowanymi użytkownikami. Po ustanowieniu takiego powiązania możliwe staje się śledzenie ich transakcji i analizowanie historii ich bitcoinów. CoinJoin jest właśnie techniką opracowaną w celu przełamania identyfikowalności UTXO, oferując w ten sposób pewną Layer poufność użytkownikom Bitcoin na poziomie transakcji.


## Jak działa Whirlpool?

Whirlpool wyróżnia się na tle innych metod CoinJoin dzięki wykorzystaniu transakcji "_ZeroLink_", które zapewniają, że nie ma absolutnie żadnego technicznego powiązania między wszystkimi danymi wejściowymi i wszystkimi danymi wyjściowymi. To doskonałe połączenie osiąga się dzięki strukturze, w której każdy uczestnik wnosi identyczną kwotę wkładu (z wyjątkiem opłat Mining), generując w ten sposób produkty wyjściowe o idealnie równych kwotach.

To restrykcyjne podejście do danych wejściowych nadaje transakcjom Whirlpool CoinJoin wyjątkową cechę: całkowity brak deterministycznych powiązań między danymi wejściowymi i wyjściowymi. Innymi słowy, każde wyjście ma równe prawdopodobieństwo przypisania do dowolnego uczestnika, w porównaniu do wszystkich innych wyjść w transakcji.

Początkowo liczba uczestników każdego Whirlpool CoinJoin była ograniczona do 5, z 2 nowymi uczestnikami i 3 remikserami (wyjaśnimy te koncepcje w dalszej części). Jednak wzrost opłat transakcyjnych On-Chain zaobserwowany w 2023 r. skłonił zespoły Samourai do ponownego przemyślenia swojego modelu w celu poprawy prywatności przy jednoczesnym obniżeniu kosztów. Tak więc, biorąc pod uwagę sytuację rynkową opłat i liczbę uczestników, koordynator może teraz organizować coinjoiny obejmujące 6, 7 lub 8 uczestników. Te ulepszone sesje są określane jako "_Surge Cycles_". Ważne jest, aby pamiętać, że niezależnie od konfiguracji, w coinjoinach Whirlpool zawsze jest tylko 2 nowych uczestników.


Tak więc transakcje Whirlpool charakteryzują się identyczną liczbą wejść i wyjść, którymi mogą być:


- 5 wejść i 5 wyjść;

![coinjoin](assets/notext/2.webp)


- 6 wejść i 6 wyjść;

![coinjoin](assets/notext/3.webp)


- 7 wejść i 7 wyjść;

![coinjoin](assets/notext/4.webp)


- 8 wejść i 8 wyjść.

![coinjoin](assets/notext/5.webp)

Model proponowany przez Whirlpool opiera się zatem na małych transakcjach CoinJoin. W przeciwieństwie do Wasabi i JoinMarket, gdzie solidność anonsetów zależy od liczby uczestników w pojedynczym cyklu, Whirlpool stawia na łańcuch kilku małych cykli.


W tym modelu użytkownik uiszcza opłaty tylko przy pierwszym wejściu do puli, co pozwala mu uczestniczyć w wielu remiksach bez dodatkowych opłat. To nowi uczestnicy pokrywają opłaty Mining dla remikserów.


Z każdym dodatkowym CoinJoin, w którym moneta uczestniczy, wraz z jej rówieśnikami napotkanymi w przeszłości, anonsety będą rosły wykładniczo. Celem jest zatem skorzystanie z tych darmowych remiksów, które z każdym wystąpieniem przyczyniają się do zwiększenia gęstości anonsetów powiązanych z każdą mieszaną monetą.


Whirlpool został zaprojektowany z uwzględnieniem dwóch ważnych wymagań:


- Dostępność implementacji na urządzeniach mobilnych, biorąc pod uwagę, że Samourai Wallet jest przede wszystkim aplikacją na smartfony;
- Szybkość cykli remiksowania w celu promowania znacznego wzrostu liczby anonsów.

Te imperatywy kierowały twórcami Samourai Wallet przy projektowaniu Whirlpool, prowadząc ich do ograniczenia liczby uczestników na cykl. Zbyt mała liczba uczestników zagroziłaby wydajności CoinJoin, drastycznie zmniejszając liczbę anonsów generowanych w każdym cyklu, podczas gdy zbyt wielu uczestników stanowiłoby problemy z zarządzaniem aplikacjami mobilnymi i utrudniałoby przepływ cykli.

**Ostatecznie nie ma potrzeby posiadania dużej liczby uczestników na CoinJoin na Whirlpool, ponieważ anonsety są osiągane poprzez akumulację kilku cykli CoinJoin.**


-> Dowiedz się więcej o anonsach Whirlpool


### Baseny i opłaty CoinJoin

Aby te wielokrotne cykle skutecznie zwiększyły anonsety mieszanych monet, należy ustanowić pewne ramy w celu ograniczenia ilości używanego UTXO. Whirlpool definiuje zatem różne pule.


Pula reprezentuje grupę użytkowników, którzy chcą łączyć się ze sobą, którzy uzgadniają ilość UTXO do wykorzystania w celu optymalizacji procesu CoinJoin. Każda pula określa stałą ilość UTXO, której użytkownik musi przestrzegać, aby móc w niej uczestniczyć. Tak więc, aby wykonywać coinjoiny z Whirlpool, należy wybrać pulę. Obecnie dostępne są następujące pule:


- 0.5 bitcoinów;
- 0.05 Bitcoin;
- 0.01 Bitcoin;
- 0.001 Bitcoin (= 100.000 Sats).


Dołączając do puli ze swoimi bitcoinami, zostaną one podzielone na generate UTXO, które są idealnie jednorodne z tymi innych uczestników puli. Każda pula ma maksymalny limit; w związku z tym, w przypadku kwot przekraczających ten limit, będziesz zmuszony albo dokonać dwóch oddzielnych wpisów w ramach tej samej puli, albo skierować się do innej puli z wyższą kwotą:


| Pool (bitcoin) | Maximum amount per entry (bitcoin) |
|----------------|------------------------------------|
| 0.5            | 35                                 |
| 0.05           | 3.5                                |
| 0.01           | 0.7                                |
| 0.001          | 0.025                              |

Jak wspomniano wcześniej, UTXO jest uważany za należący do puli, gdy jest gotowy do zintegrowania z CoinJoin. Nie oznacza to jednak, że użytkownik traci nad nim kontrolę. **Poprzez różne cykle mieszania, użytkownik zachowuje pełną kontrolę nad swoimi kluczami, a co za tym idzie, bitcoinami.** To właśnie odróżnia technikę CoinJoin od innych scentralizowanych technik mieszania.


Aby przystąpić do puli CoinJoin, należy uiścić opłaty serwisowe oraz opłaty Mining. Opłaty serwisowe są ustalane dla każdej puli i mają na celu wynagrodzenie zespołów odpowiedzialnych za rozwój i utrzymanie Whirlpool.

Opłaty za korzystanie z Whirlpool należy uiścić tylko raz przy wejściu do puli. Po tym kroku użytkownik ma możliwość uczestniczenia w nieograniczonej liczbie remiksów bez żadnych dodatkowych opłat. Oto aktualne opłaty stałe dla każdej puli:


| Pool (bitcoin) | Entry Fee (bitcoin)        |
|----------------|---------------------------|
| 0.5            | 0.0175                    |
| 0.05           | 0.00175                   |
| 0.01           | 0.0005 (50,000 sats)      |
| 0.001          | 0.00005 (5,000 sats)      |


Opłaty te zasadniczo działają jak bilet wstępu do wybranej puli, niezależnie od kwoty, którą włożysz w CoinJoin. Tak więc, niezależnie od tego, czy dołączysz do puli 0,01 z dokładnie 0,01 BTC, czy wejdziesz do niej z 0,5 BTC, opłaty pozostaną takie same w wartości bezwzględnej.


Przed przejściem do coinjoins użytkownik ma zatem wybór między 2 strategiami:


- Wybierają mniejszą pulę, aby zminimalizować opłaty za usługi, wiedząc, że w zamian otrzymają kilka małych UTXO;
- Lub wolą większą pulę, zgadzając się na wyższe opłaty, aby uzyskać mniejszą liczbę UTXO o większej wartości.


Ogólnie rzecz biorąc, odradza się łączenie kilku mieszanych UTXO po cyklach CoinJoin, ponieważ może to zagrozić uzyskanej poufności, zwłaszcza ze względu na heurystykę Common-Input-Ownership (CIOH). W związku z tym rozsądne może być wybranie większej puli, nawet jeśli oznacza to wyższe koszty, aby uniknąć zbyt wielu UTXO o małej wartości jako danych wyjściowych. Użytkownik musi rozważyć te kompromisy, aby wybrać preferowaną pulę.


Oprócz opłat za usługę, należy również wziąć pod uwagę opłaty Mining związane z każdą transakcją Bitcoin. Jako użytkownik Whirlpool, będziesz musiał uiścić opłaty Mining za transakcję przygotowawczą (`Tx0`), jak również te za pierwszą CoinJoin. Wszystkie kolejne remiksy będą darmowe, dzięki modelowi Whirlpool, który opiera się na płatnościach nowych uczestników.


Rzeczywiście, w każdym Whirlpool CoinJoin dwóch użytkowników spośród wejść to nowi uczestnicy. Pozostałe dane wejściowe pochodzą od remikserów. W rezultacie opłaty Mining dla wszystkich uczestników transakcji są pokrywane przez tych dwóch nowych uczestników, którzy następnie również skorzystają z bezpłatnych remiksów:

![coinjoin](assets/en/6.webp)

Dzięki temu systemowi opłat Whirlpool naprawdę odróżnia się od innych usług CoinJoin, ponieważ anonimy UTXO nie są proporcjonalne do ceny płaconej przez użytkownika. W ten sposób można osiągnąć znacznie wysoki poziom anonimowości, płacąc jedynie opłatę za wejście do puli i opłaty Mining za dwie transakcje (`Tx0` i początkowy miks).

Ważne jest, aby pamiętać, że użytkownik będzie musiał również pokryć opłaty Mining, aby wycofać swoje UTXO z puli po zakończeniu wielu coinjoinów, chyba że wybrał opcję `mix to`, którą omówimy w samouczku poniżej.


### Konta HD Wallet używane przez Whirlpool

Aby wykonać CoinJoin poprzez Whirlpool, Wallet musi generate kilka odrębnych kont. Konto, w kontekście HD (*Hierarchical Deterministic*) Wallet, stanowi sekcję całkowicie odizolowaną od innych, ta separacja występuje na trzecim poziomie głębokości hierarchii Wallet, czyli na poziomie `xpub`.


HD Wallet może teoretycznie wyprowadzić do `2^(32/2)` różnych kont. Początkowe konto, używane domyślnie we wszystkich portfelach Bitcoin, odpowiada indeksowi `0`.


W przypadku portfeli dostosowanych do Whirlpool, takich jak Samourai lub Sparrow, używane są 4 konta, aby zaspokoić potrzeby procesu CoinJoin:


- Konto **depozytowe**, identyfikowane przez indeks `0`;
- Konto **złego banku** (lub doxxic change), identyfikowane przez indeks `2 147 483 644'`;
- Konto **premix**, identyfikowane przez indeks `2 147 483 645'`;
- Konto **postmix**, identyfikowane przez indeks `2 147 483 646'`.


Każde z tych kont spełnia określoną funkcję w ramach procesu CoinJoin.


Wszystkie te konta są powiązane z pojedynczym seed, co pozwala użytkownikowi odzyskać dostęp do wszystkich swoich bitcoinów przy użyciu frazy odzyskiwania i, w stosownych przypadkach, passphrase. Konieczne jest jednak określenie w oprogramowaniu, podczas tej operacji odzyskiwania, różnych indeksów kont, które zostały użyte.


Przyjrzyjmy się teraz różnym etapom Whirlpool CoinJoin w ramach tych kont.


### Różne etapy coinjoinów na Whirlpool

**Etap 1: Tx0**

Punktem wyjścia dla każdego Whirlpool CoinJoin jest **konto depozytowe**. To konto jest automatycznie używane podczas tworzenia nowego Bitcoin Wallet. To konto musi być zasilone bitcoinami, które chcemy wymieszać.

`Tx0` reprezentuje pierwszy krok w procesie mieszania Whirlpool. Ma on na celu przygotowanie i wyrównanie UTXO dla CoinJoin, poprzez podzielenie ich na jednostki odpowiadające ilości wybranej puli, aby zapewnić jednorodność mieszanki. Wyrównane UTXO są następnie wysyłane na konto **premix**. Jeśli chodzi o różnicę, która nie może wejść do puli, jest ona oddzielana na specjalnym koncie: **bad bank** (lub "doxxic change").

Ta początkowa transakcja `Tx0` służy również do rozliczenia opłat za usługę należnych koordynatorowi mix. W przeciwieństwie do kolejnych kroków, ta transakcja nie jest oparta na współpracy; użytkownik musi zatem przyjąć wszystkie opłaty Mining:

![coinjoin](assets/en/7.webp)


W tym przykładzie transakcji `Tx0`, wejście `372,000 Sats` z naszego **depozytowego** konta jest dzielone na kilka wyjściowych UTXO, które są rozdzielane w następujący sposób:


- Kwota `5,000 Sats` przeznaczona dla koordynatora na opłaty za usługi, odpowiadająca wejściu do puli `100,000 Sats`;
- Trzy UTXO przygotowane do mieszania, przekierowane na nasze konto **premix** i zarejestrowane u koordynatora. Te UTXO są wyrównane na `108,000 Sats` każdy, aby pokryć opłaty Mining za ich przyszłe wstępne mieszanie;
- Nadwyżka, która nie może wejść do puli, ponieważ jest zbyt mała, jest uważana za toksyczną zmianę. Jest ona wysyłana na określone konto. W tym przypadku zmiana ta wynosi `40 000 Sats`;
- Wreszcie, istnieje `3,000 Sats`, które nie stanowią wyjścia, ale są opłatami Mining niezbędnymi do potwierdzenia `Tx0`.


Na przykład, oto prawdziwy Whirlpool Tx0 (nie ode mnie): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://Mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)


**Krok 2: Zmiana doxxic**

Nadwyżka, która nie mogła zostać zintegrowana z pulą, tutaj odpowiadająca `40 000 Sats`, jest przekierowywana na konto **bad bank**, zwane również "doxxic change", aby zapewnić ścisłe oddzielenie od innych UTXO w Wallet.


Ten UTXO jest niebezpieczny dla prywatności użytkownika, ponieważ nie tylko jest nadal powiązany z jego przeszłością, a tym samym prawdopodobnie z tożsamością jego właściciela, ale dodatkowo jest odnotowany jako należący do użytkownika, który wykonał CoinJoin.

Jeśli ten UTXO zostanie połączony z mieszanymi danymi wyjściowymi, utracą one całą poufność uzyskaną podczas cykli CoinJoin, zwłaszcza z powodu algorytmu Common-Input-Ownership-Heuristic (CIOH). Jeśli zostanie on połączony z innymi zmianami doxxic, użytkownik ryzykuje utratę poufności, ponieważ połączy różne dane wejściowe cykli CoinJoin. Dlatego należy obchodzić się z nim ostrożnie. Sposób zarządzania tym toksycznym UTXO zostanie szczegółowo opisany w ostatniej części tego artykułu, a przyszłe samouczki będą bardziej szczegółowo omawiać te metody w PlanB Network.


**Krok 3: Początkowa mieszanka**

Po zakończeniu `Tx0`, wyrównane UTXO są wysyłane do konta **premix** naszego Wallet, gotowe do wprowadzenia do pierwszego cyklu CoinJoin, zwanego również "początkowym miksem". Jeśli, jak w naszym przykładzie, `Tx0` generuje wiele UTXO do mieszania, każdy z nich zostanie zintegrowany z oddzielnym początkowym CoinJoin.


Pod koniec tych pierwszych miksów konto **premix** będzie puste, podczas gdy nasze monety, po uiszczeniu opłat Mining za ten pierwszy CoinJoin, zostaną dostosowane dokładnie do kwoty określonej przez wybraną pulę. W naszym przykładzie, nasze początkowe UTXO w wysokości `108 000 Sats` zostanie zredukowane do dokładnie `100 000 Sats`.

![coinjoin](assets/en/8.webp)

**Krok 4: Remiksy**

Po wstępnym zmiksowaniu UTXO są przenoszone na konto **postmix**. To konto gromadzi już zmiksowane UTXO i te, które czekają na ponowne zmiksowanie. Gdy klient Whirlpool jest aktywny, UTXO na koncie **postmix** są automatycznie dostępne do ponownego miksowania i zostaną losowo wybrane do udziału w tych nowych cyklach.


Przypominamy, że remiksy są wtedy w 100% darmowe: nie są wymagane żadne dodatkowe opłaty za usługi ani opłaty Mining. Utrzymywanie UTXO na koncie **postmix** utrzymuje zatem ich wartość w stanie nienaruszonym i jednocześnie poprawia ich anonsety. Dlatego ważne jest, aby umożliwić tym monetom udział w wielu cyklach CoinJoin. To nic nie kosztuje, a zwiększa ich poziom anonimowości.


Jeśli zdecydujesz się wydać zmiksowane UTXO, możesz to zrobić bezpośrednio z tego konta **postmix**. Zaleca się przechowywanie zmieszanych UTXO na tym koncie, aby skorzystać z darmowych remiksów i uniknąć opuszczenia obwodu Whirlpool, co mogłoby zmniejszyć ich poufność.


Jak zobaczymy w poniższym samouczku, istnieje również opcja `mix to`, która oferuje możliwość automatycznego wysyłania zmieszanych monet do innego Wallet, takiego jak Cold Wallet, po określonej liczbie połączeń monet.

Po omówieniu teorii, przejdźmy do praktyki z samouczkiem na temat korzystania z Whirlpool za pośrednictwem aplikacji Samourai Wallet na Androida!


## Samouczek: CoinJoin Whirlpool na Samourai Wallet

Istnieje wiele opcji korzystania z Whirlpool. Ta, którą chcę tutaj przedstawić, to opcja Samourai Wallet (bez Dojo), aplikacja open-source do zarządzania Bitcoin Wallet na Androida.


Miksowanie na Samourai bez Dojo ma tę zaletę, że jest dość łatwe w obsłudze, szybkie w konfiguracji i nie wymaga żadnego innego urządzenia poza telefonem z Androidem i połączeniem internetowym.


Metoda ta ma jednak dwie istotne wady:


- Coinjoiny będą miały miejsce tylko wtedy, gdy Samourai działa w tle i jest podłączony. Oznacza to, że jeśli chcesz mieszać i remiksować swoje bitcoiny 24/7, musisz stale włączać Samourai;
- Jeśli używasz Whirlpool z Samourai Wallet bez dbania o podłączenie własnego Dojo, twoja aplikacja będzie musiała połączyć się z serwerem utrzymywanym przez zespoły Samourai, a ty ujawnisz im `xpub` twojego Wallet. Te anonimowe informacje są niezbędne, aby aplikacja mogła znaleźć transakcje.


Idealnym rozwiązaniem pozwalającym przezwyciężyć te ograniczenia jest obsługa własnego Dojo powiązanego z instancją Whirlpool CLI na osobistym węźle Bitcoin. W ten sposób unikniesz wycieku informacji i osiągniesz całkowitą niezależność. Chociaż przedstawiony poniżej samouczek jest przydatny dla niektórych celów lub dla początkujących, aby naprawdę zoptymalizować sesję CoinJoin, zaleca się korzystanie z własnego Dojo. Szczegółowy przewodnik dotyczący konfiguracji tego rozwiązania będzie wkrótce dostępny w PlanB Network.


### Instalacja Samourai Wallet

Aby rozpocząć, będziesz oczywiście potrzebować aplikacji Samourai Wallet. Można ją pobrać bezpośrednio z oficjalnej strony internetowej za pomocą APK, z ich GitLab lub ze sklepu Google Play.


### Tworzenie Software Wallet

Po zainstalowaniu oprogramowania należy przystąpić do tworzenia Bitcoin Wallet na Samourai. Jeśli już go posiadasz, możesz przejść bezpośrednio do następnego kroku.


Po otwarciu aplikacji naciśnij niebieski przycisk "Start". Następnie zostaniesz poproszony o wybranie lokalizacji w plikach telefonu, w której zostanie zapisana zaszyfrowana kopia zapasowa nowego Wallet.


![samourai](assets/notext/9.webp)

Aktywuj Tor, klikając odpowiednie wycięcie. Na tym etapie masz również możliwość wyboru konkretnego Dojo. Jednak w tym samouczku będziemy kontynuować z domyślnym Dojo; więc możesz pozostawić tę opcję wyłączoną. Gdy Tor jest podłączony, naciśnij przycisk "Utwórz nowy Wallet".

![samourai](assets/notext/10.webp)


Następnie Samourai Wallet wyświetli monit o ustawienie BIP39 passphrase. To dodatkowe hasło jest bardzo ważne, ponieważ bezpośrednio wpływa na wyprowadzanie kluczy prywatnych. Potencjalna utrata tego passphrase spowodowałaby niemożność uzyskania dostępu do bitcoinów, czyniąc je bezpowrotnie utraconymi. Aby przywrócić Samourai Wallet, konieczne jest posiadanie zarówno 12-wyrazowej frazy odzyskiwania, jak i passphrase.


Dlatego ważne jest, aby wybrać solidny passphrase i wykonać jedną lub więcej fizycznych kopii, na papierze lub na metalowym nośniku, aby zapewnić bezpieczeństwo swoich bitcoinów. Po wykonaniu tych zadań zaznacz pole `Jestem świadomy, że w przypadku utraty...`, a następnie naciśnij przycisk `NEXT`.


![samourai](assets/notext/11.webp)


Następnie należy zdefiniować kod PIN składający się z 5 do 8 cyfr. Kod ten zabezpieczy dostęp do Wallet w telefonie. Będzie on wymagany za każdym razem, gdy będziesz chciał otworzyć aplikację Samourai. Wybierz solidny kod PIN i zachowaj kopię zapasową. Następnie można nacisnąć przycisk `NEXT`.


![samourai](assets/notext/12.webp)


Samourai poprosi o ponowne wprowadzenie kodu PIN w celu potwierdzenia. Wprowadź go, a następnie naciśnij przycisk `FINALIZUJ`.


![samourai](assets/notext/13.webp)


Następnie uzyskasz dostęp do frazy odzyskiwania składającej się z 12 słów. Fraza ta umożliwia odzyskanie Wallet za pomocą wcześniej wprowadzonego passphrase. Zdecydowanie zaleca się wykonanie jednej lub więcej kopii tej frazy na nośniku fizycznym, takim jak papier lub materiał metaliczny, aby zapewnić bezpieczeństwo bitcoinów w przypadku wystąpienia problemu.


Po wykonaniu tych kopii zapasowych zostaniesz przekierowany do Interface nowego Samourai Wallet.


![samourai](assets/notext/14.webp)


Możesz otrzymać swojego bota PayNym. Możesz o to poprosić, jeśli chcesz, chociaż nie jest to konieczne dla naszego samouczka.


![samourai](assets/notext/15.webp)

Przed przystąpieniem do otrzymywania bitcoinów na nowym Wallet zdecydowanie zaleca się ponowne sprawdzenie ważności kopii zapasowych Wallet (passphrase i frazy odzyskiwania). Aby zweryfikować passphrase, możesz wybrać ikonę swojego bota PayNym znajdującą się w lewym górnym rogu ekranu, a następnie podążać ścieżką:

```plaintext
Settings > Troubleshooting > Passphrase/backup test
```


Wprowadź swój numer passphrase, aby przeprowadzić weryfikację.


![samourai](assets/notext/16.webp)


Samourai potwierdzi, czy jest on ważny.


![samourai](assets/notext/17.webp)


Aby zweryfikować kopię zapasową frazy odzyskiwania, przejdź do ikony swojego PayNym Bot, znajdującej się w lewym górnym rogu ekranu, i podążaj tą ścieżką:

```plaintext
Settings > Wallet > Show 12-word recovery phrase
```


Samourai wyświetli okno z frazą odzyskiwania. Upewnij się, że odpowiada ono dokładnie fizycznej kopii zapasowej.


Aby pójść dalej i wykonać pełny test odzyskiwania, zanotuj element świadka Wallet, taki jak jeden z `xpubs`, a następnie usuń Wallet (pod warunkiem, że nadal jest pusty). Celem jest próba przywrócenia tego pustego Wallet przy użyciu tylko fizycznych kopii zapasowych. Jeśli przywrócenie się powiedzie, oznacza to, że kopie zapasowe są prawidłowe i niezawodne.


### Otrzymywanie bitcoinów

Po utworzeniu Wallet zaczniesz od pojedynczego konta, oznaczonego indeksem `0`. Jest to konto **depozytowe**, o którym mówiliśmy w poprzednich częściach. To właśnie na to konto będziesz musiał przelać bitcoiny przeznaczone na coinjoiny.


Aby to zrobić, kliknij niebieski symbol `+` znajdujący się w prawym dolnym rogu ekranu.


![samourai](assets/notext/18.webp)


Następnie kliknij przycisk Green `Odbierz`.


![samourai](assets/notext/19.webp)


Samourai automatycznie generate nowy pusty Address do otrzymywania bitcoinów.


![samourai](assets/notext/20.webp)


Możesz tam wysłać bitcoiny do wymieszania.


![samourai](assets/notext/21.webp)


### Tworzenie Tx0

Po potwierdzeniu transakcji możemy rozpocząć proces łączenia monet. Aby to zrobić, kliknij niebieski przycisk `+` w prawym dolnym rogu ekranu.


![samourai](assets/notext/22.webp)


Następnie kliknij na `Whirlpool` na niebiesko.


![samourai](assets/notext/23.webp)


Poczekaj, aż Whirlpool zainicjuje się i Samourai utworzy niezbędne konta.


![samourai](assets/notext/24.webp)


Nastąpi przejście do strony głównej Whirlpool. Kliknij na `Start`.

![samourai](assets/notext/25.webp)

Wybierz UTXO z konta **depozytowego**, który chcesz wysłać w cyklach CoinJoin, a następnie kliknij `Next`.


![samourai](assets/notext/26.webp)


W następnym kroku należy wybrać poziom opłaty, który ma zostać przydzielony do `Tx0`, a także do pierwszego miksu. To ustawienie określi szybkość, z jaką twoje `Tx0` i twoje początkowe CoinJoin (lub początkowe coinjoiny) zostaną potwierdzone. Pamiętaj, że opłaty Mining za `Tx0` i początkowy miks są twoją odpowiedzialnością, ale nie będziesz musiał płacić opłat Mining za kolejne remiksy. Do wyboru są opcje `Low`, `Normal` lub `High`.


![samourai](assets/notext/27.webp)


W tym samym oknie masz możliwość wyboru puli, do której wejdziesz. Biorąc pod uwagę, że początkowo wybrałem UTXO w wysokości `454,258 Sats`, moim jedynym możliwym wyborem jest pula `100,000 Sats`. Ta strona przedstawia również opłaty za usługi puli, oprócz opłat Mining, co pozwala poznać całkowity koszt tego cyklu CoinJoin. Jeśli wszystko Ci odpowiada, wybierz odpowiednią pulę i kontynuuj, klikając niebieski przycisk "WERYFIKUJ SZCZEGÓŁY CYKLU".


![samourai](assets/notext/28.webp)


Następnie można wyświetlić wszystkie szczegóły cyklu CoinJoin:


- liczba UTXO, które wejdą do puli;
- różne poniesione opłaty;
- ilość zmian doxxic...


Zweryfikuj informacje, a następnie kliknij przycisk Green `START CYCLE`.


![samourai](assets/notext/29.webp)


Pojawi się okno z propozycją oznaczenia toksycznej zmiany wynikającej z wejścia do cyklu CoinJoin jako "nie do wydania". Wybierając `Tak`, ten UTXO nie będzie widoczny w Wallet i nie będzie można go wybrać do przyszłych transakcji. Pozostanie on jednak dostępny na liście UTXO w Wallet, gdzie można ręcznie zmienić jego status. Zaleca się wybranie tej opcji, aby uniknąć błędu obsługi, który mógłby później zagrozić prywatności użytkownika. Jeśli wybierzesz `NO`, toksyczna zmiana pozostanie dostępna do użycia w Wallet. Jeśli chcesz dowiedzieć się więcej o zarządzaniu i korzystaniu z tej toksycznej zmiany, radzę przeczytać ostatnią część tego samouczka.


![samourai](assets/notext/30.webp)


Następnie Samourai nada twój Tx0.


![samourai](assets/notext/31.webp)


### Wykonywanie coinjoinów

Gdy Tx0 zostanie nadany, można go znaleźć w zakładce `Transakcje` w menu Whirlpool.


![samourai](assets/notext/32.webp)

UTXO gotowe do mieszania znajdują się w zakładce `Mieszanie w toku...`, która odpowiada kontu **Premix**.

![samourai](assets/notext/33.webp)


Po potwierdzeniu `Tx0`, twoje UTXO zostaną automatycznie zarejestrowane w koordynatorze, a początkowe miksy rozpoczną się sukcesywnie w sposób automatyczny.


![samourai](assets/notext/34.webp)


Sprawdzając zakładkę `Remixing`, która odpowiada kontu **Postmix**, będziesz obserwować UTXO wynikające z początkowych miksów. Monety te pozostaną gotowe do późniejszego remiksowania, które nie będzie wiązało się z żadnymi dodatkowymi opłatami. Zalecam zapoznanie się z tym artykułem, aby dowiedzieć się więcej o procesie remiksowania i wydajności cyklu CoinJoin: [REMIX - Whirlpool](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)


![samourai](assets/notext/35.webp)


Możliwe jest tymczasowe zawieszenie remiksowania UTXO poprzez naciśnięcie przycisku pauzy znajdującego się po jego prawej stronie. Aby ponownie zakwalifikować się do remiksowania, wystarczy kliknąć ten sam przycisk po raz drugi. Ważne jest, aby pamiętać, że tylko jeden CoinJoin może być wykonywany na użytkownika i pulę jednocześnie. Tak więc, jeśli masz 6 UTXO z `100 000 Sats` gotowych do CoinJoin, tylko jeden z nich może zostać zmiksowany. Po zmieszaniu UTXO, Samourai Wallet losowo wybiera nowy UTXO z dostępnej puli, aby zdywersyfikować i zrównoważyć remiksowanie każdej monety.


![samourai](assets/notext/36.webp)


Aby zapewnić ciągłą dostępność UTXO do remiksowania, konieczne jest utrzymywanie aplikacji Samourai aktywnej w tle. Powinieneś zobaczyć powiadomienie na swoim telefonie potwierdzające, że Whirlpool jest uruchomiony. Zamknięcie aplikacji lub wyłączenie telefonu spowoduje wstrzymanie łączenia monet.


### Uzupełnianie coinjoinów

Aby wydać zmieszane bitcoiny, przejdź do konta **Postmix** oznaczonego jako `Remixing` w zakładkach menu Whirlpool.


![samourai](assets/notext/37.webp)


Kliknij niebieskie logo Whirlpool znajdujące się w prawym dolnym rogu.


![samourai](assets/notext/38.webp)


Następnie kliknij `Spend Mixed UTXOs`.


![samourai](assets/notext/39.webp)


Następnie można wprowadzić Address odbiorcy i kwotę do wysłania, w taki sam sposób, jak w przypadku każdej innej transakcji dokonanej za pomocą Samourai Wallet. Niebieskie tło wskazuje, że środki są wydawane z konta Whirlpool, a nie z konta **depozytowego**.


![samourai](assets/notext/40.webp)


Klikając 3 małe kropki w prawym górnym rogu, można wybrać określone UTXO.

![samourai](assets/notext/41.webp)

Klikając biały kwadrat w prawym górnym rogu okna, można zeskanować kod QR odbieranego Address za pomocą aparatu.


![samourai](assets/notext/42.webp)


Wprowadź niezbędne informacje dotyczące transakcji wydatków, a następnie kliknij niebieski przycisk "WERYFIKUJ TRANSAKCJĘ".


![samourai](assets/notext/43.webp)


W następnym kroku możesz zmodyfikować stawkę opłaty powiązaną z transakcją. Możesz również włączyć opcję Stonewall, zaznaczając odpowiednie pole. Jeśli opcja Stonewall nie jest dostępna, oznacza to, że konto **Postmix** nie zawiera UTXO o rozmiarze wystarczającym do obsługi tej konkretnej struktury transakcji.


[-> Dowiedz się więcej o transakcjach Stonewall](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


Jeśli wszystko jest w porządku, kliknij przycisk Green `WYŚLIJ ... BTC`.


![samourai](assets/notext/44.webp)


Następnie Samourai przystąpi do podpisania transakcji przed rozgłaszaniem jej w sieci. Musisz tylko poczekać, aż zostanie ona dodana do bloku przez Miner.


![samourai](assets/notext/45.webp)


### Używanie SCODE

Czasami zespoły Samourai Wallet oferują "SCODE". SCODE to kod promocyjny, który zapewnia zniżkę na opłaty za usługi puli. Samourai Wallet od czasu do czasu oferuje takie kody swoim użytkownikom podczas specjalnych wydarzeń. Radzę [śledzić Samourai Wallet](https://twitter.com/SamouraiWallet) w mediach społecznościowych, aby nie przegapić przyszłych SCODE.


Aby zastosować SCODE na Samourai, przed rozpoczęciem nowego cyklu CoinJoin, przejdź do menu Whirlpool i wybierz trzy małe kropki znajdujące się w prawym górnym rogu ekranu.


![samourai](assets/notext/46.webp)


Kliknij `SCODE (kod promocyjny) Whirlpool`.


![samourai](assets/notext/47.webp)


Wprowadź SCODE w otwartym oknie, a następnie zatwierdź klikając `OK`.


![samourai](assets/notext/48.webp)


Whirlpool zamknie się automatycznie. Poczekaj, aż Samourai zakończy ładowanie, a następnie ponownie otwórz menu Whirlpool.


![samourai](assets/notext/49.webp)


Upewnij się, że SCODE został poprawnie zarejestrowany, klikając ponownie trzy małe kropki, a następnie wybierając `SCODE (kod promocyjny) Whirlpool`. Jeśli wszystko jest w porządku, możesz rozpocząć nowy cykl Whirlpool ze zniżką na opłaty za usługę. Ważne jest, aby pamiętać, że te SCODE są tymczasowe: pozostają ważne przez kilka dni, zanim staną się nieaktualne.


## Jak poznać jakość naszych cykli CoinJoin?

Aby CoinJoin był naprawdę skuteczny, ważne jest, aby wykazywał dobrą jednorodność między kwotami wejść i wyjść. Ta jednorodność zwiększa liczbę możliwych interpretacji w oczach zewnętrznego obserwatora, zwiększając tym samym niepewność związaną z transakcją. Aby określić niepewność generowaną przez CoinJoin, można uciec się do obliczenia entropii transakcji.


W celu dogłębnego zbadania tych wskaźników (model Whirlpool jest uznawany za ten, który zapewnia największą jednorodność coinjoinów), odsyłam do samouczka: [KALKULATOR BOLTZMANNA](https://planb.network/tutorials/privacy/analysis/boltzmann-entropy-738e45af-18a6-4ce6-af1a-1bf58e15f1fe)


Następnie wydajność kilku cykli CoinJoin jest oceniana na podstawie zakresu grup, w których moneta jest ukryta. Rozmiar tych grup definiuje tak zwane anonsety. Istnieją dwa rodzaje anonsetów: pierwszy ocenia prywatność uzyskaną na podstawie analizy retrospektywnej (od teraźniejszości do przeszłości), a drugi na podstawie analizy prospektywnej (od przeszłości do teraźniejszości). Aby uzyskać szczegółowe wyjaśnienie tych dwóch wskaźników, zapraszam do zapoznania się z samouczkiem: Whirlpool STATS TOOLS - ANONSETS


## Jak zarządzać postmixem?

Po wykonaniu cykli CoinJoin najlepszą strategią jest przechowywanie UTXO na koncie **postmix**, czekając na ich przyszłe wykorzystanie. Zaleca się nawet pozostawienie ich na koncie remix na czas nieokreślony, dopóki nie będzie trzeba ich wydać.


Niektórzy użytkownicy mogą rozważyć przeniesienie swoich mieszanych bitcoinów do Wallet zabezpieczonego przez Hardware Wallet. Jest to możliwe, ale ważne jest, aby skrupulatnie przestrzegać zaleceń Samourai Wallet, aby nie naruszyć nabytej poufności.


Łączenie UTXO jest najczęściej popełnianym błędem. Konieczne jest unikanie łączenia mieszanych UTXO z niemieszanymi UTXO w tej samej transakcji, aby uniknąć CIOH (*Common-Input-Ownership-Heuristic*). Wymaga to starannego zarządzania UTXO w ramach Wallet, szczególnie w zakresie etykietowania. Poza CoinJoin, łączenie UTXO jest ogólnie złą praktyką, która często prowadzi do utraty poufności, jeśli nie jest odpowiednio zarządzana.

Należy również uważać na konsolidację mieszanych UTXO ze sobą. Umiarkowane konsolidacje są możliwe, jeśli mieszane UTXO mają znaczące anonsety, ale nieuchronnie zmniejszy to prywatność monet. Upewnij się, że konsolidacje nie są zbyt duże ani przeprowadzane po niewystarczającej liczbie remiksów, ponieważ grozi to ustanowieniem możliwych do wywnioskowania powiązań między UTXO przed i po cyklach CoinJoin. W przypadku wątpliwości co do tych operacji, najlepszą praktyką jest nie konsolidowanie UTXO po mieszaniu i przenoszenie ich pojedynczo do Hardware Wallet, generując za każdym razem nowy pusty Address. Ponownie należy pamiętać o prawidłowym oznaczeniu każdego otrzymanego UTXO.


Odradza się również przenoszenie postmix UTXO do Wallet przy użyciu nietypowych skryptów. Na przykład, jeśli wejdziesz do Whirlpool z Multisig Wallet za pomocą skryptów `P2WSH`, istnieje niewielka szansa, że zostaniesz zmieszany z innymi użytkownikami posiadającymi pierwotnie ten sam typ Wallet. Jeśli wyjdziesz z postmix do tego samego Multisig Wallet, poziom prywatności twoich mieszanych bitcoinów zostanie znacznie zmniejszony. Poza skryptami istnieje wiele innych odcisków palców Wallet, które mogą cię oszukać.


Podobnie jak w przypadku każdej transakcji Bitcoin, nie należy ponownie wykorzystywać adresów odbiorczych. Każda nowa transakcja musi zostać odebrana na nowym pustym Address.


Najprostszym i najbezpieczniejszym rozwiązaniem jest pozostawienie zmieszanych UTXO na koncie **postmix**, pozwalając im na remiksowanie i dotykanie ich tylko w celu wydania. Portfele Samourai i Sparrow mają dodatkowe zabezpieczenia przed wszystkimi tymi zagrożeniami związanymi z analizą łańcucha. Zabezpieczenia te pomagają uniknąć popełniania błędów.


## Jak zarządzać zmianą doxxic?

Następnie należy zachować ostrożność w zarządzaniu doksyczną zmianą, zmianą, która nie mogła wejść do puli CoinJoin. Te toksyczne UTXO, wynikające z użycia Whirlpool, stanowią zagrożenie dla prywatności użytkownika, ponieważ tworzą powiązanie między użytkownikiem a użyciem CoinJoin. Dlatego konieczne jest ostrożne obchodzenie się z nimi i nie łączenie ich z innymi UTXO, zwłaszcza mieszanymi UTXO. Oto różne strategie, które należy rozważyć przy ich użyciu:


- Wymieszaj je w mniejszych basenach: Jeśli toksyczny UTXO jest wystarczająco duży, aby samodzielnie dostać się do mniejszego basenu, rozważ jego wymieszanie. Jest to często najlepsza opcja. Jednak ważne jest, aby nie łączyć kilku toksycznych UTXO, aby uzyskać dostęp do puli, ponieważ może to połączyć różne wpisy.
- Oznacz je jako **"niewydawalne"**: Innym podejściem jest zaprzestanie ich używania, oznaczenie ich jako "niewydawalnych" na dedykowanym koncie i po prostu HODL. Gwarantuje to, że nie zostaną one przypadkowo wydane. Jeśli wartość Bitcoin wzrośnie, mogą pojawić się nowe pule bardziej odpowiednie dla toksycznych UTXO;
- **Darowizny:** Rozważ przekazanie darowizny, nawet skromnej, deweloperom pracującym nad Bitcoin i powiązanym oprogramowaniem. Możesz również przekazać darowiznę organizacjom, które akceptują BTC. Jeśli zarządzanie toksycznymi UTXO wydaje się zbyt skomplikowane, możesz się ich po prostu pozbyć, przekazując darowiznę;
- **Kupowanie kart podarunkowych:** Platformy takie jak [Bitrefill](https://www.bitrefill.com/) pozwalają na Exchange bitcoinów na karty podarunkowe, które można wykorzystać u różnych sprzedawców. Może to być sposób na pozbycie się toksycznych UTXO bez utraty związanej z nimi wartości;
- Skonsoliduj je na **Monero:** Samourai Wallet oferuje teraz usługę atomic swap pomiędzy BTC i XMR. Jest to idealne rozwiązanie do zarządzania toksycznymi UTXO poprzez konsolidację ich na Monero, bez narażania prywatności poprzez KYC, przed odesłaniem ich z powrotem do Bitcoin. Opcja ta może być jednak kosztowna pod względem opłat Mining i premii ze względu na ograniczenia płynności;
- Przesłanie ich do Lightning Network: Przeniesienie tych UTXO do Lightning Network w celu skorzystania z obniżonych opłat transakcyjnych jest opcją, która może być interesująca. Ta metoda może jednak ujawniać pewne informacje w zależności od sposobu korzystania z Lightning i dlatego należy ją stosować ostrożnie.


Szczegółowe samouczki dotyczące wdrażania tych różnych technik zostaną wkrótce udostępnione w PlanB Network.


**Dodatkowe zasoby:**

[Samourai Wallet video tutorial]()


- [Dokumentacja Samourai Wallet - Whirlpool](https://docs.samourai.io/Whirlpool/basic-concepts);
- [Wątek na Twitterze dotyczący coinjoinów](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Wpis na blogu na temat coinjoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).
