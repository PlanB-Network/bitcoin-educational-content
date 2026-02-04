---
term: Płatność zwykła
definition: Model transakcji z 2 wyjściami, zazwyczaj płatnością i resztą.
---

Wzorzec transakcji (lub model) wykorzystywany w analizie łańcucha charakteryzujący się konsumpcją jednego lub więcej UTXO na wejściu i produkcją 2 UTXO na wyjściu. Model ten będzie zatem wyglądał następująco:





Ten prosty model płatności wskazuje, że prawdopodobnie mamy do czynienia z transakcją wysyłania lub płatności. Użytkownik zużył swój własny UTXO w wejściach, aby zaspokoić w wyjściach płatność UTXO i zmianę UTXO (zmiana zwrócona temu samemu użytkownikowi). Wiemy zatem, że obserwowany użytkownik prawdopodobnie nie jest już w posiadaniu jednego z dwóch UTXO na wyjściu (płatność), ale nadal jest w posiadaniu drugiego UTXO (zmiana).