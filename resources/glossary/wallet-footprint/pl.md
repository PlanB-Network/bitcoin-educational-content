---
term: Wallet FOOTPRINT
---

Zestaw charakterystycznych cech obserwowalnych w transakcjach dokonywanych przez ten sam Bitcoin Wallet. Cechy te mogą obejmować podobieństwa w użyciu typów skryptów, ponowne użycie adresów, kolejność UTXO, umieszczenie wyjść zmian, sygnalizację RBF (*Replace-by-fee*), numer wersji, pole `nSequence` i pole `nLockTime`.


Ślady Wallet są wykorzystywane przez analityków do śledzenia działań określonego podmiotu na Blockchain poprzez identyfikację powtarzających się wzorców w jego transakcjach. Na przykład użytkownik, który systematycznie wysyła swoje zmiany na adresy P2TR (`bc1p...`), tworzy charakterystyczny ślad, który można wykorzystać do śledzenia jego przyszłych transakcji.


Jak wyjaśnia LaurentMT w Space Kek #19 (francuskojęzyczny podcast), użyteczność śladów Wallet w analizie łańcucha znacznie wzrasta wraz z upływem czasu. Rzeczywiście, rosnąca liczba typów skryptów i coraz bardziej stopniowe wdrażanie tych nowych funkcji przez oprogramowanie Wallet uwydatniają różnice. Możliwe jest nawet dokładne zidentyfikowanie oprogramowania używanego przez śledzony podmiot. Dlatego ważne jest, aby zrozumieć, że badanie śladu Wallet jest szczególnie istotne dla ostatnich transakcji, bardziej niż dla tych zainicjowanych na początku 2010 roku.