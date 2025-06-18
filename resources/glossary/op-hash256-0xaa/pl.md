---
term: OP_HASH256 (0XAA)
---

Pobiera górny element ze stosu i zastępuje go jego Hash poprzez dwukrotne użycie funkcji `SHA256`. Dane wejściowe są hashowane raz za pomocą `SHA256`, a następnie skrót jest hashowany drugi raz za pomocą `SHA256`. Ten dwuetapowy proces generuje 256-bitowy odcisk palca.