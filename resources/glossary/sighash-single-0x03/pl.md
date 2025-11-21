---
term: SIGHASH_SINGLE (0X03)
---

Typ flagi SigHash używanej w podpisach transakcji Bitcoin do wskazania, że podpis dotyczy wszystkich wejść transakcji i tylko jednego wyjścia, odpowiadającego indeksowi tego samego podpisanego wejścia. W ten sposób każde wejście podpisane za pomocą `SIGHASH_SINGLE` jest konkretnie powiązane z konkretnym wyjściem. Pozostałe wyjścia nie są powiązane z podpisem i mogą być modyfikowane później. Ten typ podpisu jest przydatny w złożonych transakcjach, w których uczestnicy chcą powiązać określone wejścia z określonymi wyjściami, pozostawiając elastyczność dla innych wyjść transakcji.