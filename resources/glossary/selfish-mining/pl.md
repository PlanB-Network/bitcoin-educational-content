---
term: SELFISH Mining
---

Strategia (lub atak) w Mining, w której Miner lub grupa górników celowo przetrzymuje bloki z ważnym Proof of Work bez natychmiastowego wypuszczania ich do sieci. Celem jest wyprzedzenie innych górników pod względem Proof of Work, potencjalnie umożliwiając im Miner kilka bloków z rzędu i opublikowanie ich wszystkich naraz, maksymalizując w ten sposób swoje zyski. Innymi słowy, atakująca grupa górników nie wydobywa ostatniego bloku zatwierdzonego przez całą sieć, ale raczej blok, który sami stworzyli, który różni się od tego zatwierdzonego przez sieć.


Proces ten generuje rodzaj tajnej gałęzi Blockchain, która pozostaje nieznana dla całej sieci, dopóki ten alternatywny łańcuch potencjalnie nie przekroczy uczciwego Blockchain. Gdy tajny łańcuch atakujących górników staje się dłuższy (tj. zawiera więcej zgromadzonej pracy) niż uczciwy, publiczny łańcuch, jest on następnie transmitowany do całej sieci. W tym momencie węzły w sieci podążające za najdłuższym łańcuchem (z największą ilością zgromadzonej pracy) zsynchronizują się z tym nowym łańcuchem. Następuje więc reorganizacja.


Samolubność Mining jest irytująca dla użytkowników, ponieważ zmniejsza bezpieczeństwo systemu poprzez marnowanie części mocy obliczeniowej sieci. Jeśli się powiedzie, prowadzi również do reorganizacji Blockchain, wpływając na niezawodność potwierdzeń transakcji dla użytkowników. Mimo to praktyka ta pozostaje ryzykowna dla atakującej grupy górników, ponieważ często bardziej opłacalne jest Miner zwykle powyżej ostatniego publicznie znanego bloku niż przydzielanie mocy obliczeniowej do tajnej gałęzi, która prawdopodobnie nigdy nie przekroczy uczciwego Blockchain. Im większa liczba bloków w reorganizacji, tym mniejsze prawdopodobieństwo udanego ataku.