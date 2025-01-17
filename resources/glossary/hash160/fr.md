---
term: HASH160
---

Fonction cryptographique utilisée sur Bitcoin notamment pour générer des adresses de réception Legacy et SegWit v0. Elle combine deux fonctions de hachage qui s'exécute successivement sur l'input : d'abord SHA256, puis RIPEMD160. La sortie de cette fonction est donc de 160 bits.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$

