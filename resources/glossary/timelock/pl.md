---
term: TIMELOCK
---

Prymityw Smart contract, który umożliwia ustawienie warunku opartego na czasie, który musi zostać spełniony, aby transakcja została dodana do bloku. Istnieją dwa rodzaje blokad czasowych na Bitcoin:


- Absolutna blokada czasowa, która określa dokładny moment, przed którym transakcja nie może zostać włączona do bloku;
- Względna blokada czasowa, która ustawia opóźnienie od akceptacji poprzedniej transakcji.

Blokada czasowa może być zdefiniowana jako data wyrażona w czasie uniksowym lub jako numer bloku. Wreszcie, blokada czasowa może dotyczyć wyjścia transakcji poprzez użycie określonego kodu operacyjnego w skrypcie blokującym (`OP_CHECKLOCKTIMEVERIFY` lub `OP_CHECKSEQUENCEVERIFY`) lub całej transakcji poprzez użycie określonych pól transakcji (`nLockTime` lub `nSequence`).