---
term: BIP0383
---

Wprowadza funkcje `multi(NUM, KEY, ..., KEY)` i `sortedmulti(NUM, KEY, ..., KEY)` dla deskryptorów. Funkcje te pozwalają na opisanie skryptów z wieloma podpisami w deskryptorach, przy czym `sortedmulti` sortuje klucze publiczne w porządku leksykograficznym, aby zapewnić kompatybilność podczas importu. BIP383 został zaimplementowany wraz ze wszystkimi innymi BIP-ami związanymi z deskryptorami (z wyjątkiem BIP386) w wersji 0.17 Bitcoin Core.