---
term: NLOCKTIME
---

Wbudowane pole w transakcjach, które ustawia warunek czasowy, przed którym transakcja nie może zostać dodana do ważnego bloku. Parametr ten umożliwia określenie dokładnego czasu (Unix Timestamp) lub określonej liczby bloków jako warunku uznania transakcji za ważną. Jest to więc absolutna blokada czasowa (nie względna). `nLockTime` wpływa na całą transakcję i efektywnie umożliwia weryfikację czasu, podczas gdy opcode `OP_CHECKLOCKTIMEVERIFY` pozwala jedynie na porównanie górnej wartości stosu z wartością `nLockTime`.