---
name: Remix - Whirlpool
description: Ile remiksów należy wykonać na Whirlpool?
---
![cover remix- wp](assets/cover.webp)


**OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, narzędzie Whirlpool Stats Tool nie jest już dostępne do pobrania, ponieważ było hostowane na Gitlab Samourai. Nawet jeśli wcześniej pobrałeś to narzędzie lokalnie na swój komputer lub zostało ono zainstalowane na węźle RoninDojo, WST nie będzie teraz działać. Jego działanie opierało się na danych dostarczonych przez OXT.me, a strona ta nie jest już dostępna. Obecnie WST nie jest szczególnie przydatny, ponieważ protokół Whirlpool jest nieaktywny. Istnieje jednak możliwość, że oprogramowanie to zostanie przywrócone w nadchodzących tygodniach. Co więcej, teoretyczna część tego artykułu pozostaje istotna dla zrozumienia zasad i celów coinjoinów w ogóle (nie tylko Whirlpool), a także zrozumienia skuteczności modelu Whirlpool. Można również dowiedzieć się, jak ilościowo określić pr


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

> *Przerwij połączenie, które pozostawiają po sobie monety*

Jest to pytanie, które jest mi często zadawane. **Podczas wykonywania coinjoinów z Whirlpool, ile remiksów należy wykonać, aby osiągnąć zadowalające wyniki?**


Celem CoinJoin jest zaoferowanie wiarygodnego zaprzeczenia poprzez zmieszanie monety z grupą nieodróżnialnych monet. Celem tego działania jest zerwanie powiązań identyfikowalności, zarówno z przeszłości do teraźniejszości, jak i z teraźniejszości do przeszłości. Innymi słowy, analityk, który zna początkową transakcję na wejściu cykli CoinJoin, nie powinien być w stanie ostatecznie zidentyfikować UTXO na wyjściu cykli remiksowania (analiza od cykli wejścia do cykli wyjścia).

![past-present links diagram](assets/en/1.webp)


I odwrotnie, analityk, który zna twój UTXO na wyjściu z cykli CoinJoin, nie powinien być w stanie określić pierwotnej transakcji na wejściu do cykli (analiza od cykli wyjściowych do cykli wejściowych).

![present-past links diagram](assets/en/2.webp)

Jednak liczba remiksów nie jest wiarygodnym kryterium oceny trudności, jakie analityk napotkałby w ustaleniu powiązań między przeszłością a teraźniejszością lub odwrotnie. Bardziej odpowiednim wskaźnikiem byłby rozmiar grup, w których ukrywa się moneta. Wskaźniki te są określane jako "anonsety". W przypadku Whirlpool istnieją dwa rodzaje anonsetów.


Po pierwsze, możemy określić rozmiar grupy, w której ukryty jest UTXO na wyjściu z cykli CoinJoin, tj. liczbę nierozróżnialnych monet obecnych w tej grupie.

![probable UTXOs at exit](assets/en/3.webp)

Wskaźnik ten, zwany "prospective anonset" w języku francuskim, "forward anonset" w języku angielskim lub "forward-looking metrics", pozwala nam ocenić odporność monety na analizy śledzące jej ścieżkę od wejścia do wyjścia z cykli CoinJoin. Ta metryka szacuje stopień, w jakim twoja UTXO jest chroniona przed próbami odtworzenia jej historii od punktu wejścia do punktu wyjścia w procesie CoinJoin. Na przykład, jeśli twoja transakcja uczestniczyła w pierwszym cyklu CoinJoin i wykonano dwa dodatkowe cykle, potencjalny anonset twojej monety wynosiłby `13`:

![forward anonset](assets/en/4.webp)

Po drugie, można obliczyć inny wskaźnik, aby ocenić odporność twojego utworu na analizę od teraźniejszości do przeszłości. Znając swój UTXO na koniec cykli, wskaźnik ten określa liczbę potencjalnych transakcji Tx0, które mogły stanowić twój wkład w cyklach CoinJoin (analiza od końca do początku cykli). Wskaźnik ten mierzy, jak trudno jest analitykowi prześledzić pochodzenie twojego elementu po tym, jak przeszedł on przez coinjoiny.![Prawdopodobne źródła na wejściu](assets/en/5.webp)

Nazwa tego wskaźnika to "backward anonset" lub "backward-looking metrics". Po francusku lubię go nazywać "anonset rétrospectif". Na poniższym wykresie odpowiada to wszystkim pomarańczowym bąbelkom Tx0:

![backward anonset](assets/en/6.webp)

Aby dowiedzieć się więcej o metodzie obliczania tych wskaźników, polecam przeczytanie [mojego wątku na Twitterze](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) na ten temat. Przygotowujemy również bardziej obszerny artykuł na temat PlanB Network.


Zdaję sobie sprawę, że udzielona odpowiedź może wydawać się niezadowalająca, ponieważ liczyłeś na konkretną liczbę remiksów i kieruję Cię do dokumentacji. Powodem jest to, że liczba remiksów jest niewiarygodnym wskaźnikiem do oceny anonimowości uzyskanej w cyklach CoinJoin. Dlatego nie jest możliwe zdefiniowanie stałej liczby remiksów jako bezwzględnego i uniwersalnego progu bezpieczeństwa.


Prawdą jest, że każdy dodatkowy remiks utworu zwiększa jego anonimowość. Ważne jest jednak, aby zrozumieć, że to przede wszystkim remiksy wykonywane przez rówieśników przyczyniają się do wzrostu potencjalnego anonsetu. W modelu Whirlpool transakcja może osiągnąć znaczny poziom potencjalnego anonsetu w zaledwie dwóch lub trzech cyklach CoinJoin, wyłącznie dzięki aktywności rówieśników zaangażowanych w poprzednie coinjoiny.


Z drugiej strony, anonset retrospektywny nie jest problemem w naszym przypadku. W rzeczywistości, od początkowego CoinJoin, korzystasz z dziedziczenia poprzednich transakcji puli, natychmiast dając swojemu utworowi wysoki anonset wsteczny, z marginalnym wzrostem w każdym kolejnym cyklu.

Ważne jest również, aby zrozumieć, że tworzenie wiarygodnego zaprzeczenia nigdy nie jest kompletne. Polega ono na prawdopodobieństwie namierzenia monety. Prawdopodobieństwo to maleje wraz ze wzrostem wielkości ukrywających się grup. Dlatego powinieneś dostosować swoje cele w zakresie anonimowości do swoich osobistych oczekiwań. Zadaj sobie pytanie o powody, które skłaniają cię do korzystania z coinjoinów i poziomy anonimowości niezbędne do osiągnięcia tych celów. Na przykład, jeśli korzystanie z coinjoinów ma na celu po prostu zachowanie prywatności Wallet podczas wysyłania kilku Sats swojemu chrześniakowi na urodziny, bardzo wysoki poziom anonimowości nie jest konieczny. Twój chrześniak prawdopodobnie nie jest w stanie przeprowadzić dogłębnej analizy łańcucha, a nawet gdyby był, reperkusje dla twojego życia nie byłyby katastrofalne. Jeśli jednak jesteś celem autorytarnego reżimu, w którym najmniejsza informacja może skutkować więzieniem, twoje działania będą musiały być kierowane znacznie surowszymi kryteriami.


Aby określić te słynne wskaźniki anonset, można użyć narzędzia Python o nazwie **WST** (Whirlpool Stats Tool).


Nie zawsze jednak konieczne jest obliczanie anonsetów każdej z połączonych monet. Sam projekt Whirlpool zapewnia już gwarancje. Jak wspomniano wcześniej, anonset retrospektywny rzadko jest problemem. Z początkowego miksu uzyskujesz już szczególnie wysoki wynik retrospektywny. Jeśli chodzi o anonset prospektywny, wystarczy trzymać monetę na koncie post-mix przez wystarczająco długi okres czasu. Na przykład, oto wyniki anonset jednej z moich monet `100,000 Sats` po spędzeniu dwóch miesięcy w puli CoinJoin:

![WST anonsets](assets/en/7.webp)

Wyświetla wynik retrospektywny `34,593` i wynik prospektywny `45,202`. Konkretnie oznacza to dwie rzeczy:


- Jeśli analityk zna moją monetę na końcu cykli i spróbuje prześledzić jej pochodzenie, napotka `34 593` potencjalnych źródeł, z których każde ma równe prawdopodobieństwo bycia moją monetą.
- Jeśli analityk zna moją monetę na początku cykli i próbuje określić jej odpowiednik na końcu, będzie miał do czynienia z `45 202` możliwymi UTXO, z których każdy ma takie samo prawdopodobieństwo bycia moją monetą.

Dlatego uważam, że wykorzystanie Whirlpool jest szczególnie istotne w strategii `HODL -> Mix -> Spend -> Replace`. Moim zdaniem najbardziej logicznym podejściem jest utrzymywanie większości swoich oszczędności w bitcoinach w Cold Wallet, przy jednoczesnym stałym utrzymywaniu pewnej liczby monet w CoinJoin na Samourai w celu pokrycia codziennych wydatków. Gdy bitcoiny z coinjoinów zostaną wydane, są one zastępowane nowymi, aby powrócić do określonego progu mieszanych monet. Ta metoda pozwala nam uwolnić się od obaw związanych z anonsetami naszych UTXO, jednocześnie sprawiając, że czas wymagany do skutecznego coinjoina jest znacznie mniej restrykcyjny.


Mam nadzieję, że ta odpowiedź rzuciła nieco światła na model Whirlpool. Jeśli chcesz dowiedzieć się więcej o tym, jak coinjoiny działają w Bitcoin, polecam przeczytać mój obszerny artykuł na ten temat:




**Zasoby zewnętrzne:**


- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://estudiobitcoin.com/como-instalar-y-utilizar-Whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/
- https://medium.com/samourai-Wallet/diving-head-first-into-Whirlpool-anonymity-sets-4156a54b0bc7.
