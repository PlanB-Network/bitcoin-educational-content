---
term: BIP8
---

Élaboré suite aux débats sur SegWit, qui utilisait le BIP9 pour son activation, le BIP8 est une méthode d'activation de soft forks qui incorpore nativement un mécanisme d'UASF (*User-Activated Soft Fork*) automatique. Comme le BIP9, le BIP8 utilise la signalisation des mineurs, mais ajoute le paramètre `LOT` (*Lock-in On Time out*). Si `LOT` est réglé sur `vrai`, à l'expiration de la période de signalisation sans atteindre le seuil requis, un UASF est automatiquement déclenché, forçant l'activation du soft fork. Cette approche contraint les mineurs à être coopératifs ou risquer un UASF imposé par les utilisateurs. De plus, contrairement au BIP9, le BIP8 définit la période de signalisation établie sur la hauteur des blocs, éliminant les manipulations potentielles via le taux de hachage par les mineurs. Le BIP8 permet également de fixer un seuil de vote variable et introduit un paramètre pour une hauteur de bloc minimale pour l'activation, donnant aux mineurs le temps de se préparer et de signaler leur accord en avance sans forcément être prêts. Lorsqu'un soft fork est activé via le BIP8 avec le paramètre `LOT=vrai`, on utilise ici une méthode très agressive contre les mineurs qui sont immédiatement mis sous la pression d'un éventuel UASF. En effet, ça leur laisse seulement 2 choix :
* Être coopératifs, et ainsi faciliter le processus d'activation ;
* Être non coopératifs, auquel cas les utilisateurs font un UASF automatiquement pour imposer le soft fork.

