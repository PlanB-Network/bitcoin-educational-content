---
term: PSEUDO-RANDOM
---

Przymiotnik ten jest używany do opisania sekwencji liczb, która, choć jest wynikiem deterministycznego procesu, wykazuje cechy zbliżone do idealnej, prawdziwie losowej sekwencji. Pojęcie idealnej losowości oznacza całkowity brak przewidywalności i korelacji między kolejnymi Elements. Liczba pseudolosowa jest generowana przez deterministyczny algorytm i dlatego teoretycznie jest całkowicie przewidywalna, jeśli znamy początkowy stan generatora.


Generator liczb pseudolosowych (PRNG) to algorytm używany do generowania takich liczb. Zasadniczo zaczyna się od wartości początkowej lub "seed", a następnie stosuje serię przekształceń matematycznych w celu wytworzenia sekwencji liczb. Ze względu na tę determinowalność, dla bezpieczeństwa kryptograficznego ważne jest, aby początkowy seed pozostawał tajny. Sekwencje pseudolosowe są szeroko stosowane w różnych dziedzinach, w tym w kryptografii, ponieważ wykazują pozornie losowe zachowanie, które wystarcza do wielu zastosowań. Ocena jakości PRNG opiera się na stopniu, w jakim jego wynik zbliża się do prawdziwej losowości pod względem rozkładu, korelacji i innych właściwości statystycznych. W kontekście Bitcoin, liczby pseudolosowe są wykorzystywane do tworzenia kluczy prywatnych lub do generate i seed dla deterministycznych i hierarchicznych portfeli.