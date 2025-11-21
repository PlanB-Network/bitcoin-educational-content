---
term: ANALIZA ŁAŃCUCHÓW
---

Praktyka obejmująca wszystkie metody wykorzystywane do śledzenia przepływu bitcoinów na Blockchain. Ogólnie rzecz biorąc, analiza łańcucha opiera się na obserwacji cech charakterystycznych w próbkach poprzednich transakcji. Następnie polega na zidentyfikowaniu tych samych cech w transakcji, którą chcemy przeanalizować, i wydedukowaniu wiarygodnych interpretacji. Ta metoda rozwiązywania problemów, oparta na praktycznym podejściu do znalezienia wystarczająco dobrego rozwiązania, znana jest jako heurystyka. Dla uproszczenia, analiza łańcucha odbywa się w dwóch głównych krokach:


- Identyfikacja znanych cech;
- Odejmowanie hipotez.


Jednym z celów analizy łańcucha jest pogrupowanie różnych działań na Bitcoin w celu określenia unikalności użytkownika, który je wykonał. Następnie możliwe będzie podjęcie próby powiązania tej wiązki działań z rzeczywistą tożsamością poprzez punkt wejścia. Ważne jest, aby zrozumieć, że analiza łańcucha nie jest nauką ścisłą. Opiera się na heurystyce pochodzącej z wcześniejszych obserwacji lub logicznych interpretacji. Zasady te pozwalają na uzyskanie dość wiarygodnych wyników, ale nigdy z absolutną precyzją. Innymi słowy, analiza łańcuchowa zawsze obejmuje wymiar prawdopodobieństwa w wyciągniętych wnioskach. Na przykład, można oszacować z większą lub mniejszą pewnością, że dwa adresy należą do tego samego podmiotu, ale całkowita pewność zawsze będzie poza zasięgiem. Cały cel analizy łańcuchowej polega właśnie na agregacji różnych heurystyk w celu zminimalizowania ryzyka błędu. Jest to w pewnym sensie kumulacja dowodów, która pozwala nam zbliżyć się do rzeczywistości. Te słynne heurystyki można podzielić na różne kategorie:


- Wzorce transakcji (lub modele transakcji);
- Heurystyka wewnętrzna dla transakcji;
- Heurystyka zewnętrzna w stosunku do transakcji.


Warto zauważyć, że pierwsze dwie heurystyki Bitcoin zostały sformułowane przez samego Nakamoto. Przedstawił je w części 10 Białej Księgi. Warto zauważyć, że te dwie heurystyki nadal utrzymują przewagę w analizie łańcucha. Są to Common Input Ownership Heuristic (CIOH) i Address reuse.