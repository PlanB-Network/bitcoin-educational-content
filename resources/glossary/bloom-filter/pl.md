---
term: FILTR BLOOM
---

Probabilistyczna struktura danych używana do sprawdzania, czy element jest częścią zbioru. Filtry Blooma pozwalają na szybkie sprawdzanie przynależności bez konieczności testowania całego zbioru danych. Są one szczególnie przydatne w kontekstach, w których przestrzeń i szybkość są krytyczne, ale niski i kontrolowany poziom błędu jest akceptowalny. Rzeczywiście, filtry Blooma nie generują fałszywych negatywów, ale generate pewną ilość fałszywych pozytywów. Gdy element jest dodawany do filtra, wiele funkcji Hash zajmuje pozycje generate w tablicy bitów. Aby sprawdzić przynależność, używane są te same funkcje Hash. Jeśli wszystkie odpowiednie bity są ustawione, element jest prawdopodobnie w zestawie, ale z ryzykiem fałszywych alarmów. Filtry Blooma są szeroko stosowane w bazach danych i sieciach. Wiadomo zwłaszcza, że Google używa ich w swoim skompresowanym systemie zarządzania bazami danych *BigTable*. W protokole Bitcoin są one wykorzystywane w szczególności do portfeli SPV zgodnie z BIP37.


> gdy mowa o wykorzystaniu filtrów Blooma w kontekście transakcji Bitcoin, czasami spotyka się termin "Transaction Bloom Filtering"