---
term: AJUSTEMENT DE LA DIFFICULTE
---

L'ajustement de la difficulté est un processus périodique qui redéfinit la cible de difficulté pour le mécanisme de la preuve de travail (le minage) sur Bitcoin. Cet évènement intervient tous les 2016 blocs (environ toutes les deux semaines). Il vient augmenter ou baisser le facteur de difficulté (également nommé la cible de difficulté), en fonction de la rapidité à laquelle les 2016 derniers blocs ont été trouvés. L’ajustement vise à conserver un taux de production de blocs stable et prévisible, à une fréquence d’un bloc toutes les 10 minutes, malgré les variations de la puissance de calcul déployée par les mineurs. La modification de la difficulté lors de l'ajustement est limitée à un facteur 4. La formule exécutée par les nœuds pour calculer la nouvelle cible est la suivante : 
$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$
&nbsp;
Où :
* $N$ : La nouvelle cible ;
* $A$ : L'ancienne cible des 2016 derniers blocs ;
* $T$ : Le temps total réel des 2016 derniers blocs en secondes ;
* $1,209,600$ : Le temps cible en secondes pour produire 2016 blocs avec un intervalle de 10 minutes entre chacun.

> ► *En français, on parle également parfois de « reciblage » pour évoquer l'ajustement. En anglais, on parle de « Difficulty Adjustment ».*

