---
term: BIP0381
definition: Funkcje pk(), pkh() i sh() do opisu skryptów Legacy w deskryptorach.
---

Wprowadza funkcje dla deskryptorów, w szczególności `pk(KEY)` (Pay-to-PubKey), `pkh(KEY)` (Pay-to-PubKey-Hash) i `sh(SCRIPT)` (Pay-to-Script-Hash). Funkcje te standaryzują sposób opisywania typów skryptów Legacy w deskryptorach. BIP381 został zaimplementowany wraz ze wszystkimi innymi BIPami związanymi z deskryptorami (z wyjątkiem BIP386) w wersji 0.17 Bitcoin Core.