---
term: ENTROPIA (ANALIZA)
---

W konkretnym kontekście analizy łańcucha, entropia jest również nazwą wskaźnika, wywodzącego się z entropii Shannona, wynalezionego przez LaurentMT. Wskaźnik ten pozwala zmierzyć brak wiedzy analityków na temat dokładnej konfiguracji transakcji Bitcoin. Innymi słowy, im wyższa entropia transakcji, tym trudniej jest analitykom zidentyfikować ruchy bitcoinów między wejściami i wyjściami.


W praktyce entropia ujawnia, czy z perspektywy zewnętrznego obserwatora transakcja przedstawia wiele możliwych interpretacji, opartych wyłącznie na ilości danych wejściowych i wyjściowych, bez uwzględnienia innych zewnętrznych lub wewnętrznych wzorców i heurystyk. Wysoka entropia jest wtedy synonimem lepszej poufności transakcji.


Entropia jest definiowana jako logarytm binarny liczby możliwych kombinacji. Oto wzór, w którym $E$ reprezentuje entropię transakcji, a $C$ liczbę możliwych interpretacji:


$$
E = \log_2(C)
$$


Biorąc pod uwagę wartości UTXO zaangażowanych w transakcję, liczba interpretacji $C$ reprezentuje liczbę sposobów, w jakie dane wejściowe mogą być powiązane z danymi wyjściowymi. Innymi słowy, określa ona liczbę interpretacji, jakie transakcja może wywołać z punktu widzenia analizującego ją zewnętrznego obserwatora.