---
term: ENTROPIE (ANALYSE)
---

Dans le contexte spécifique de l'analyse de chaîne, l'entropie est également le nom d'un indicateur, dérivé de l'entropie de Shannon, inventé par LaurentMT. Cet indicateur permet de mesurer le manque de connaissance des analystes sur la configuration exacte d'une transaction Bitcoin. Autrement dit, plus l'entropie d'une transaction est élevée, plus la tâche d'identification des mouvements de bitcoins entre les entrées et les sorties devient difficile pour les analystes.

En pratique, l'entropie révèle si, du regard d'un observateur externe, une transaction présente de multiples interprétations possibles, basées uniquement sur les montants des entrées et sorties, sans prendre en compte d'autres paternes et heuristiques externes ou internes. Une grande entropie est alors synonyme d'une meilleure confidentialité pour la transaction.

L'entropie est définie comme le logarithme binaire du nombre de combinaisons possibles. Voici la formule utilisée avec $E$ l'entropie de la transaction et $C$ le nombre d'interprétations possibles :

$$
E = \log_2(C)
$$

En prenant en compte les valeurs des UTXOs impliqués dans la transaction, le nombre d'interprétations $C$ représente le nombre de manières dont les entrées peuvent être associées aux sorties. Autrement dit, il détermine le nombre d'interprétations qu'une transaction peut susciter du point de vue d'un observateur extérieur qui l'analyse.

