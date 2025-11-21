---
term: RGB
---

Zdecentralizowany, poufny system Smart contract zaprojektowany do współpracy z Bitcoin i Lightning Network. RGB działa w oparciu o model Client-side Validation i oddziela przechowywanie Contract State od Blockchain, dzięki czemu przechowywane są na nim tylko zobowiązania kryptograficzne. W ten sposób pełna historia stanu jest przechowywana poza łańcuchem, umożliwiając większą skalowalność i poufność. RGB umożliwia zatem tworzenie złożonych kontraktów do przechowywania tokenów, NFT, zdecentralizowanych tożsamości lub rozwiązań DeFi, bezpośrednio na Bitcoin.


Na RGB odporność na Double-spending jest zapewniona przez użycie Single-Use Seal, mechanizmu kryptograficznego, który wykorzystuje fakt, że UTXO na Bitcoin mogą być użyte tylko raz. Jeśli chodzi o autentyczność tokena, jest ona gwarantowana przez weryfikację historii stanu po stronie klienta, od utworzenia Contract do jego ostatniego stanu.