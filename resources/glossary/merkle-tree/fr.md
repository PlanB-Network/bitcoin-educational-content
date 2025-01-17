---
term: ARBRE DE MERKLE
---

Un Arbre de Merkle est un accumulateur cryptographique. C’est une méthode pour justifier l’appartenance d’une information donnée à un ensemble plus grand. C'est une structure de données qui facilite la vérification d’informations dans un format compact. Dans le système Bitcoin, les arbres de Merkle sont utilisés pour regrouper et condenser les transactions d'un bloc en un unique hachage, appelé la racine de Merkle (ou « *Root Hash* »). Chaque transaction est hachée, puis les hachages adjacents sont hachés ensemble de façon hiérarchique jusqu'à ce que la racine de Merkle soit obtenue.

![](../../dictionnaire/assets/1.webp)

Cette structure permet de vérifier rapidement si une transaction spécifique est incluse dans un bloc donné sans avoir à analyser l'ensemble des transactions. Par exemple, si je dispose seulement de la racine de Merkle et que je souhaite vérifier que la `TX 7` fait bien partie de l'arbre, j'aurai uniquement besoin des preuves suivantes :
* `TX 7` ;
* `HASH 8` ;
* `HASH 5-6` ;
* `HASH 1-2-3-4`.
Grâce à ces quelques informations, je suis en capacité de calculer les nœuds intermédiaires jusqu'à la racine de Merkle.

![](../../dictionnaire/assets/2.webp)

Les arbres de Merkle sont notamment utilisés pour les nœuds légers (dits « SPV ») qui ne conservent que les entêtes de blocs, mais pas les transactions. On retrouve également cette structure dans le protocole UTREEXO, un protocole permettant de condenser l'UTXO set des nœuds, et dans le MAST Taproot.

> ► *L'arbre de Merkle porte le nom de Ralph Merkle, un cryptographe qui a conçu cette structure en 1979. Un arbre de Merkle peut également être nommé « arbre de hachage ». En anglais, on dit « Merkle Tree » ou « Hash Tree ».*

