---
term: ANONSETS (ZESTAWY ANONIMOWOŚCI)
---

Anonsety służą jako wskaźniki do oceny poziomu prywatności danego UTXO. Mówiąc dokładniej, mierzą one liczbę nierozróżnialnych UTXO w zestawie zawierającym badaną monetę. Ponieważ wymagana jest grupa identycznych UTXO, anonsety są zazwyczaj obliczane w ramach cyklu coinjoinów. Pozwalają one, w stosownych przypadkach, ocenić jakość połączeń monet. Duży anonset oznacza zwiększony poziom anonimowości, ponieważ rozróżnienie konkretnego UTXO w zestawie staje się trudne. Istnieją dwa rodzaje anonsetów:


- Perspektywiczny zestaw anonimowości;
- Retrospektywny zestaw anonimowości.


Pierwszy z nich wskazuje wielkość grupy, wśród której ukryty jest badany UTXO, znając UTXO na wejściu. Wskaźnik ten pozwala zmierzyć odporność prywatności monety na analizę od przeszłości do teraźniejszości (od wejścia do wyjścia). W języku angielskim nazwa tego wskaźnika to "*forward anonset*" lub "*forward-looking metrics*"


![](../../dictionnaire/assets/39.webp)


Drugi wskazuje liczbę możliwych źródeł dla danej monety, znając UTXO na wyjściu. Wskaźnik ten pozwala zmierzyć odporność prywatności monety na analizę od teraźniejszości do przeszłości (od wyjścia do wejścia). W języku angielskim nazwa tego wskaźnika to "*backward anonset*" lub "*backward-looking metrics*"


![](../../dictionnaire/assets/40.webp)


> w języku francuskim ogólnie przyjęte jest używanie terminu "anonset" Można go jednak przetłumaczyć jako "ensemble d'anonymat" lub "potentiel d'anonymat" Zarówno w języku angielskim, jak i francuskim, termin "score" jest również czasami używany w odniesieniu do anonsetów (prospective score i retrospective score)