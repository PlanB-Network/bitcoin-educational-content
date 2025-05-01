---
term: PŁATNOŚĆ OKRĄGŁA
---

Wewnętrzna heurystyka do analizy łańcucha w Bitcoin, która pozwala na postawienie hipotezy o naturze wyjść transakcji w oparciu o okrągłe kwoty. Ogólnie rzecz biorąc, w obliczu prostego wzorca płatności (1 wejście i 2 wyjścia), jeśli jedno z wyjść wydaje okrągłą kwotę, to reprezentuje płatność. W drodze eliminacji, jeśli jedno wyjście reprezentuje płatność, drugie reprezentuje zmianę. Można zatem zinterpretować, że jest prawdopodobne, że użytkownik wprowadzający transakcję nadal posiada wyjście zidentyfikowane jako zmiana.


Należy zauważyć, że ta heurystyka nie zawsze ma zastosowanie, ponieważ większość płatności jest nadal dokonywana w jednostkach waluty fiducjarnej. Rzeczywiście, gdy sprzedawca we Francji akceptuje Bitcoin, zazwyczaj nie wyświetla stabilnych cen w Sats. Woleliby raczej dokonać konwersji między ceną w euro a kwotą w bitcoinach, która ma zostać zapłacona za pośrednictwem ich POS (na przykład serwera BTCPay). W związku z tym w danych wyjściowych transakcji nie powinna występować okrągła liczba. Niemniej jednak analityk mógłby spróbować dokonać tej konwersji, biorąc pod uwagę kurs Exchange obowiązujący w momencie transmisji transakcji w sieci. Jeśli pewnego dnia Bitcoin stanie się preferowaną jednostką rozliczeniową na naszych giełdach, ta heurystyka może stać się jeszcze bardziej przydatna w analizach.


![](../../dictionnaire/assets/11.webp)