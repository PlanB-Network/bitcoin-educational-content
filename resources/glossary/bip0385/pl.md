---
term: BIP0385
definition: Funkcje addr() i raw() do opisu skryptów wyjściowych według adresu lub w formacie szesnastkowym w deskryptorach.
---

Wprowadza funkcje deskryptora `addr(ADDR)` i `raw(HEX)`. Funkcja `addr(ADDR)` umożliwia opisanie skryptu wyjściowego przy użyciu odbierającego Address, podczas gdy funkcja `raw(HEX)` umożliwia określenie skryptu wyjściowego przy użyciu surowej szesnastkowej reprezentacji tego skryptu. BIP385 został zaimplementowany wraz ze wszystkimi innymi BIPami związanymi z deskryptorami (z wyjątkiem BIP386) w wersji 0.17 Bitcoin Core.