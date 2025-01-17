---
term: BIP113
---

A introduit une modification dans le calcul de toutes les opérations de timelock (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` et `OP_CHECKSEQUENCEVERIFY`). Il spécifie que pour évaluer la validité des timelocks, il faut désormais les comparer au MTP (*Median Time Past*), c'est-à-dire la médiane des horodatages des 11 derniers blocs. Auparavant, on utilisait seulement l'horodatage du bloc précédent. Cette méthode rend le système plus prévisible et évite la manipulation du référentiel de temps par les mineurs. Le BIP113 a été introduit via un soft fork le 4 juillet 2016 en même temps que le BIP68 et le BIP112, activé pour la première fois grâce à la méthode du BIP9.

