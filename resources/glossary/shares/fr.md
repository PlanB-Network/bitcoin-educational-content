---
term: SHARES
---

Dans le cadre des pools de minage, une share est un indicateur utilisé pour quantifier la contribution d'un mineur individuel au sein de la pool. Cette mesure sert de base pour le calcul de la récompense que la pool redistribue à chaque mineur. Chaque share correspond à un hash qui satisfait une cible de difficulté moins élevée que celle du réseau Bitcoin.

Pour expliquer avec une analogie, considérons un dé à 20 faces. Sur Bitcoin, supposons que la preuve de travail exige de faire un lancé inférieur à 3 pour valider un bloc (c'est-à-dire, obtenir un résultat de 1 ou 2). Maintenant, imaginons qu'au sein d'une pool de minage, la cible de difficulté pour une share est fixée à 10. Ainsi, pour un mineur individuel dans la pool, chaque lancer de dés qui donne un résultat inférieur à 10 compte comme une share valide. Ces shares sont ensuite transmises à la pool par le mineur, afin de réclamer sa rémunération, même si elles ne correspondent pas à un résultat valide pour un bloc sur Bitcoin.

Pour chaque hash calculé, un mineur individuel dans une pool peut rencontrer trois scénarios différents :
* Si la valeur du hash est supérieure ou égale à la cible de difficulté fixée par la pool pour une share, alors ce hash n'est d'aucune utilité. Le mineur modifie alors son nonce pour tenter un nouveau hash : `hash > share > bloc`.
* Si le hash est inférieur à la cible de difficulté de la share, mais supérieur ou égal à la cible de difficulté de Bitcoin, alors ce hash constitue une share valide qui n'est cependant pas suffisante pour valider un bloc. Le mineur peut envoyer ce hash à sa pool pour réclamer la récompense associée à la share : `share > hash > bloc`.
* Si le hash est inférieur à la cible de difficulté du réseau Bitcoin, il est considéré à la fois comme une share valide et comme un bloc valide. Le mineur transmet ce hash à sa pool, qui s'empresse de le diffuser sur le réseau Bitcoin. Ce hash est également comptabilisé comme une share valide pour le mineur : `share > bloc > hash`.

![](../../dictionnaire/assets/32.webp)

Ce système de shares est utilisé pour estimer le travail réalisé par chaque mineur individuel au sein d'une pool, sans devoir recalculer individuellement tous les hash générés par un mineur, ce qui serait complètement inefficace pour la pool.

Les pools de minage ajustent la difficulté des shares pour équilibrer la charge de vérification et s'assurer que chaque mineur, qu'il soit petit ou grand, soumet des shares environ toutes les quelques secondes. Cela permet de calculer avec précision le hashrate de chaque mineur et de distribuer les récompenses selon la méthode de calcul de la rémunération choisie (PPS, PPLNS, TIDES...).

> ► *En français, on peut traduire « shares » par « part ».*

