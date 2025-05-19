---
term: PayJoin
---

Specyficzna struktura transakcji Bitcoin, która zwiększa prywatność użytkownika podczas wydawania pieniędzy poprzez współpracę z odbiorcą płatności. Wyjątkowość PayJoin polega na jego zdolności do generate transakcji, która na pierwszy rzut oka wygląda zwyczajnie, ale w rzeczywistości jest mini CoinJoin między dwiema stronami. W tym celu struktura transakcji obejmuje odbiorcę płatności w danych wejściowych obok faktycznego nadawcy. W ten sposób odbiorca zawiera płatność dla siebie w środku transakcji, która pozwala mu otrzymać zapłatę. Na przykład, jeśli kupisz bagietkę za `6,000 Sats` przy użyciu UTXO w wysokości `10,000 Sats` i zdecydujesz się na PayJoin, twój piekarz doda UTXO w wysokości `15,000 Sats` należący do niego jako wkład, który odzyska w całości jako wynik, oprócz twoich `6,000 Sats`.


Transakcja PayJoin spełnia dwa cele. Po pierwsze, ma na celu zmylenie zewnętrznego obserwatora poprzez stworzenie wabika w analizie łańcucha na podstawie heurystyki Common Input Ownership (CIOH). Zwykle, gdy transakcja na Blockchain ma wiele wejść, zakłada się, że wszystkie te wejścia prawdopodobnie należą do tego samego podmiotu. Tak więc, gdy analityk bada transakcję PayJoin, jest przekonany, że wszystkie dane wejściowe pochodzą od tej samej osoby. Takie przekonanie jest jednak błędne, ponieważ odbiorca płatności również przyczynia się do danych wejściowych obok faktycznego płatnika. Po drugie, PayJoin wprowadza również w błąd zewnętrznego obserwatora co do rzeczywistej kwoty dokonanej płatności. Badając strukturę transakcji, analityk może sądzić, że płatność jest równoważna kwocie jednego z wyjść. W rzeczywistości kwota płatności nie odpowiada żadnemu z wyników. W rzeczywistości jest to różnica między UTXO odbiorcy na wyjściu a UTXO odbiorcy na wejściu. W ten sposób transakcja PayJoin wchodzi w zakres steganografii. Pozwala ona ukryć rzeczywistą kwotę transakcji w fałszywej transakcji, która działa jak wabik.


![](../../dictionnaire/assets/14.webp)


> *PayJoin jest również czasami nazywana "P2EP (Pay-to-End-Point)", "Stowaway" lub "transakcją steganograficzną"