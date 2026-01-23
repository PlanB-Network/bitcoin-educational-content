---
term: BIP0383
definition: Fonctions multi() et sortedmulti() pour décrire les scripts multisig dans les descriptors.
---

Introduit les fonctions `multi(NUM, KEY, ..., KEY)` et `sortedmulti(NUM, KEY, ..., KEY)` pour les descriptors. Ces fonctions permettent de décrire les scripts multisignatures dans les descriptors, avec `sortedmulti` qui trie les clés publiques par ordre lexicographique pour assurer la compatibilité lors de l'import. Le BIP383 a été implémenté avec tous les autres BIP liés aux descriptors (sauf le BIP386) dans la version 0.17 de Bitcoin Core.
