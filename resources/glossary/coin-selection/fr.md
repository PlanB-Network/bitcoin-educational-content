---
term: SÉLECTION DES PIÈCES
---

Processus par lequel un logiciel de portefeuille Bitcoin choisit quels UTXOs utiliser comme entrées pour satisfaire les sorties d'une transaction. La méthode de sélection des pièces est importante, car elle a des conséquences sur le coût d'une transaction et la confidentialité de l'utilisateur. Elle vise souvent à minimiser le nombre d'entrées utilisées, afin de réduire la taille de la transaction et les frais associés, tout en tentant de préserver la confidentialité en évitant de fusionner des pièces provenant de sources différentes (CIOH). Plusieurs méthodes existent pour la sélections de pièce, comme le *Knapsack Solver* ou le *Branch-and-Bound*. Lorsque la sélection des pièces est réalisée manuellement par l'utilisateur, on parle alors de « *Coin Control* ».

> ► *En anglais, on parle de « Coin Selection ».*

