---
term: Commitment
---

Commitment (w sensie kryptograficznym) jest obiektem matematycznym, oznaczanym $C$, otrzymanym deterministycznie z operacji na danych strukturalnych $m$ (wiadomość) i wartości losowej $r$. Piszemy :


$$
C = \text{commit}(m, r)
$$


Mechanizm ten obejmuje dwie główne operacje:




- Zobowiązanie: stosujemy funkcję kryptograficzną do wiadomości $m$ i losowej wartości $r$, aby uzyskać $C$;
- Verify: używamy $C$, wiadomości $m$ i wartości $r$, aby sprawdzić, czy Commitment jest poprawny. Funkcja zwraca `True` lub `False`.


Commitment musi respektować dwie właściwości:




- Wiązanie: musi być niemożliwe znalezienie dwóch różnych wiadomości generujących to samo $C$ :


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Takich jak :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Ukrywanie: znajomość $C$ nie może ujawniać zawartości $m$.


W przypadku protokołu RGB, Commitment jest zawarty w transakcji Bitcoin w celu udowodnienia istnienia określonej informacji w danym czasie, bez ujawniania samej informacji.