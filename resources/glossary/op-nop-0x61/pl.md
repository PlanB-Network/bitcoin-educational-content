---
term: OP_NOP (0X61)
---

Nie ma żadnego wpływu na stos ani stan skryptu. Nie wykonuje żadnych ruchów, kontroli ani modyfikacji. Po prostu nic nie robi, chyba że postanowiono inaczej za pomocą Soft Fork. Rzeczywiście, od czasu ich modyfikacji przez Satoshi Nakamoto w 2010 roku, komendy `OP_NOP` (`OP_NOP1` (`0XB0`) do `OP_NOP10` (`0XB9`)) są używane do dodawania nowych kodów operacyjnych w formie Soft Fork.


Tak więc, `OP_NOP2` (`0XB1`) i `OP_NOP3` (`0XB2`) zostały już użyte do zaimplementowania odpowiednio `OP_CHECKLOCKTIMEVERIFY` i `OP_CHECKSEQUENCEVERIFY`. Są one używane w połączeniu z `OP_DROP` w celu usunięcia powiązanych wartości czasowych ze stosu, umożliwiając tym samym kontynuowanie wykonywania skryptu, niezależnie od tego, czy węzeł jest aktualny, czy nie. Komendy `OP_NOP` pozwalają zatem na wstawienie punktu przerwania w skrypcie w celu sprawdzenia dodatkowych warunków, które już istnieją lub mogą zostać dodane w przyszłych forkach Soft. Od czasu Tapscript, użycie `OP_NOP` zostało zastąpione przez bardziej wydajne `OP_SUCCESS`.