---
term: Anonsets (anonymity sets)
definition: Wskaźniki mierzące stopień prywatności UTXO poprzez liczenie nierozróżnialnych UTXO w zbiorze, zwykle po coinjoinie.
---
Anonsety służą jako wskaźniki do oceny poziomu prywatności danego UTXO. Dokładniej mierzą one liczbę nierozróżnialnych UTXO w zbiorze, który obejmuje analizowaną monetę. Ponieważ konieczne jest posiadanie grupy identycznych UTXO, anonsety są zazwyczaj obliczane w ramach cyklu coinjoinów. Umożliwiają one w razie potrzeby ocenę jakości coinjoinów. Duży anonset oznacza wyższy poziom anonimowości, ponieważ trudno jest wyróżnić konkretny UTXO w obrębie zbioru.

Istnieją dwa rodzaje anonsetów: forward anonset (forward-looking metrics); oraz backward anonset (backward-looking metrics). Termin "*score*" bywa również używany do określania anonsetów.

Pierwszy wskazuje wielkość grupy, w której ukrywa się analizowany UTXO wyjściowy, przy znanym UTXO wejściowym. Wskaźnik ten pozwala mierzyć odporność prywatności monety na analizę od przeszłości do teraźniejszości (od wejścia do wyjścia). Drugi wskazuje liczbę możliwych źródeł dla danej monety, przy znanym UTXO wyjściowym. Wskaźnik ten pozwala mierzyć odporność prywatności monety na analizę od teraźniejszości do przeszłości (od wyjścia do wejścia).
















