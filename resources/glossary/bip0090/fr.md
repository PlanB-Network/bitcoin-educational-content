---
term: BIP0090
definition: Proposition simplifiant la vérification d'activation des anciens soft forks en utilisant la hauteur de bloc plutôt que la signalisation des mineurs.
---

Proposition pour simplifier le traitement de l'activation des soft forks antérieurs en remplaçant le mécanisme de signalisation par les mineurs via les numéros de version des blocs par de simples vérifications de la hauteur de bloc. Cette modification éliminerait la nécessité de vérifier les 1000 blocs précédents pour l'activation des règles de consensus, ce qui permettrait de réduire la dette technique associée à l'implémentation de ces soft fork.
