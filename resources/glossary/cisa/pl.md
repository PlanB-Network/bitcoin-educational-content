---
term: CISA
---

Skrót od "Cross-Input Signature Aggregation". Jest to propozycja techniczna mająca na celu optymalizację rozmiaru transakcji Bitcoin poprzez zmniejszenie liczby podpisów wymaganych do ich walidacji.


Obecnie na Bitcoin każde wejście w transakcji musi mieć indywidualny podpis, zanim będzie mogło zostać wykorzystane. Dowodzi to, że właściciel danego UTXO autoryzował transakcję. Celem CISA jest połączenie podpisów wszystkich danych wejściowych do pojedynczej transakcji w jeden podpis obejmujący wszystkie dane wejściowe. Umożliwiłoby to zmniejszenie rozmiaru transakcji z wieloma danymi wejściowymi, a tym samym zmniejszenie ich kosztów. Byłoby to szczególnie przydatne dla tych, którzy przeprowadzają coinjoiny lub konsolidacje, jednocześnie umożliwiając potwierdzenie większej liczby transakcji na Bitcoin bez zmiany rozmiarów bloków lub interwałów. CISA opiera się na protokole Schnorra, który umożliwia liniową agregację podpisów. Oznacza to, że pojedynczy podpis może potwierdzać posiadanie kilku niezależnych kluczy.


Wdrożenie CISA na Bitcoin jest jednak bardzo złożone, ponieważ wymaga głębokich zmian w sposobie działania skryptów. Obecnie weryfikacja skryptów na Bitcoin odbywa się wejście po wejściu. Przejście do modelu, w którym cała transakcja jest sprawdzana jednocześnie, jak proponuje CISA, jest dalekie od trywialnej zmiany.