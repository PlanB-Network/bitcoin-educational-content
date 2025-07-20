---
term: SIGHASH_ALL (0X01)
---

Typ flagi SigHash używanej w podpisach transakcji Bitcoin w celu wskazania, że podpis dotyczy wszystkich składników transakcji. Używając `SIGHASH_ALL`, podpisujący obejmuje wszystkie wejścia i wszystkie wyjścia. Oznacza to, że ani wejścia, ani wyjścia nie mogą być modyfikowane po złożeniu podpisu bez jego unieważnienia. Ten typ SigHash Flag jest najbardziej powszechny w transakcjach Bitcoin, ponieważ zapewnia całkowitą finalność i integralność transakcji.