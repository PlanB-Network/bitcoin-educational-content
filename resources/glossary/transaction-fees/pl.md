---
term: OPŁATY TRANSAKCYJNE
---

Opłaty transakcyjne stanowią sumę, która ma na celu zrekompensowanie górnikom ich udziału w mechanizmie Proof of Work. Opłaty te zachęcają górników do uwzględniania transakcji w tworzonych przez nich blokach. Wynikają one z różnicy między całkowitą ilością danych wejściowych a całkowitą ilością danych wyjściowych w transakcji:


```text
fees = inputs - outputs
```


Są one wyrażone w `Sats/vBytes`, co oznacza, że opłaty nie zależą od ilości wysłanych bitcoinów, ale od wagi transakcji. Są one swobodnie wybierane przez nadawcę transakcji i określają szybkość jej włączenia do bloku za pomocą mechanizmu aukcyjnego. Na przykład, załóżmy, że dokonuję transakcji o wartości wejściowej `100 000 Sats`, wartości wyjściowej `40 000 Sats` i kolejnej wartości wyjściowej `58 500 Sats`. Suma transakcji wyjściowych wynosi `98 500 Sats`. Opłaty przypisane do tej transakcji wynoszą `1 500 Sats`. Miner, który uwzględnia moją transakcję, może utworzyć `1 500 Sats` w swoim Coinbase Transaction w Exchange dla `1 500 Sats`, których nie odzyskałem w moich wyjściach.


Transakcje z wyższymi opłatami, w stosunku do ich wielkości, są traktowane priorytetowo przez górników, co może przyspieszyć proces potwierdzania. I odwrotnie, transakcje z niższymi opłatami mogą być opóźnione w okresach dużego zatłoczenia. Warto zauważyć, że opłaty transakcyjne Bitcoin różnią się od dotacji blokowej, która stanowi dodatkową zachętę dla górników. Block reward składa się z nowych bitcoinów tworzonych z każdym wydobytym blokiem (dotacja blokowa), a także zebranych opłat transakcyjnych. Podczas gdy dotacja blokowa zmniejsza się z czasem ze względu na całkowity limit bitcoinów Supply, opłaty transakcyjne będą nadal odgrywać kluczową rolę w zachęcaniu górników do uczestnictwa.


Na poziomie protokołu nic nie stoi na przeszkodzie, aby użytkownicy włączali do bloku transakcje bez żadnych opłat. W rzeczywistości ten rodzaj transakcji bez opłat jest wyjątkowy. Domyślnie węzły Bitcoin nie przekazują transakcji z opłatami niższymi niż `1 sat/vBytes`. Jeśli niektóre transakcje bez opłat przeszły, to dlatego, że zostały bezpośrednio zintegrowane przez zwycięski Miner, bez przechodzenia przez sieć węzłów. Na przykład poniższa transakcja nie zawiera żadnych opłat:


```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```


W tym konkretnym przykładzie była to transakcja zainicjowana przez dyrektora F2Pool Mining pool. Jako zwykły użytkownik, obecny dolny limit wynosi zatem `1 sat/vBytes`.

Konieczne jest również rozważenie limitów oczyszczania. W okresach dużego przeciążenia, mempoole węzłów oczyszczają swoje oczekujące transakcje poniżej pewnego progu, aby przestrzegać przydzielonego limitu pamięci RAM. Limit ten jest dowolnie wybierany przez użytkownika, ale wielu pozostawia domyślną wartość Bitcoin Core na poziomie 300 MB. Można go zmodyfikować w pliku `Bitcoin.conf` za pomocą parametru `maxmempool`.

> w języku angielskim określamy je jako "opłaty transakcyjne"