---
term: HEURYSTYKA ANALIZY
---

Analiza heurystyczna dla łańcucha Bitcoin to rodzina metod empirycznych wykorzystywanych do śledzenia przepływu bitcoinów na Blockchain w oparciu o cechy zaobserwowane w transakcjach. Heurystyka jest praktycznym podejściem do rozwiązywania problemów, często za pomocą przybliżonych metod, ale reprezentuje wystarczająco dobre rozwiązanie, aby osiągnąć dany cel. Te heurystyki dają dość wiarygodne wyniki, ale nigdy z absolutną precyzją. Innymi słowy, analiza łańcuchowa zawsze wiąże się z pewnym stopniem prawdopodobieństwa wyciągniętych wniosków. Na przykład, można oszacować z większą lub mniejszą pewnością, że dwa adresy należą do tego samego podmiotu, ale całkowita pewność jest zawsze poza zasięgiem. Cały cel analizy łańcuchowej polega właśnie na agregacji różnych heurystyk w celu zminimalizowania ryzyka błędu. Jest to w pewnym sensie gromadzenie dowodów, które pozwalają nam zbliżyć się do rzeczywistości. W tym kontekście rozróżnia się heurystyki wewnętrzne i zewnętrzne.


Wewnętrzne heurystyki koncentrują się na cechach specyficznych dla poszczególnych transakcji. Obejmują one w swojej analizie Elements, takie jak kwoty UTXO, użyte skrypty, wersje lub czasy blokady. Na przykład heurystyka płatności zaokrąglonej pozwala zidentyfikować wynik transakcji jako prawdopodobnie będący płatnością, jeśli jego kwota jest liczbą zaokrągloną. Te heurystyki często umożliwiają identyfikację zmiany (pieniądze zwrócone temu samemu użytkownikowi), a tym samym kontynuowanie śledzenia.


Z drugiej strony heurystyki zewnętrzne analizują podobieństwa i cechy wykraczające poza samą transakcję. Obejmują one całe środowisko transakcji. Na przykład ponowne wykorzystanie Address w wielu transakcjach jest heurystyką zewnętrzną. CIOH jest również jedną z nich.