---
term: XOR
---

Sigle de l'opération « Exclusive or », en français « Ou exclusif ». C'est une fonction fondamentale de la logique booléenne. Cette opération prend deux opérandes booléens, chacun étant $vrai$ ou $faux$, et produit une sortie $vraie$ uniquement lorsque les deux opérandes diffèrent. Autrement dit, la sortie de l'opération XOR est $vraie$ si exactement un (mais pas les deux) des opérandes est $vrai$. Par exemple, l'opération XOR entre $1$ et $0$ donnera comme résultat $1$. Nous noterons :

$$
1 \oplus 0 = 1
$$

De même, l'opération XOR peut être effectuée sur des séquences plus longues de bits. Par exemple :

$$
10110 \oplus 01110 = 11000
$$

Chaque bit de la séquence est comparé à son homologue et l'opération XOR est appliquée. Voici la table de vérité de l'opération XOR :

<div align="center">

| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>

L'opération XOR est utilisée dans de nombreux domaines de l'informatique, notamment dans la cryptographie, pour ses attributs intéressants comme : 
* Sa commutativité : l'ordre des opérandes n'affecte pas le résultat. Pour deux variables $D$ et $E$ données : $D \oplus E = E \oplus D$ ;
* Son associativité : le regroupement des opérandes n'affecte pas le résultat. Pour trois variables $A$, $B$ et $C$ données : $(A \oplus B) \oplus C = A \oplus (B \oplus C)$ ;
* Il dispose d'un élément neutre $0$ : un opérande xorée à $0$ sera toujours égale à l'opérande. Pour une variable $A$ donnée : $A \oplus 0 = A$ ;
* Chaque élément est son propre inverse. Pour une variable $A$ donnée : $A \oplus A = 0$.

Dans le cadre de Bitcoin, on utilise évidemment l'opération XOR à de nombreux endroits. Par exemple, le XOR est massivement utilisé dans la fonction SHA256, elle-même largement utilisée dans le protocole Bitcoin. Certains protocoles comme le *SeedXOR* de Coldcard utilisent également cette primitive pour d'autres applications. On le retrouve aussi dans le BIP47 pour chiffrer le code de paiement réutilisable lors de sa transmission.

Dans le domaine plus général de la cryptographie, le XOR peut être utilisé tel quel comme un algorithme de chiffrement symétrique. On appelle cet algorithme le « *Masque Jetable* » ou le « *Chiffre Vernam* » du nom de son inventeur. Cet algorithme, bien qu'inutile en pratique du fait de la longueur de la clé, est un des seuls algorithmes de chiffrement reconnus comme inconditionnellement sûrs.

