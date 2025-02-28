---
term: SILENT PAYMENTS
---

Méthode pour utiliser des adresses Bitcoin statiques afin de recevoir des paiements sans pour autant produire de réutilisation d'adresse, sans interaction et sans lien visible on-chain entre les différents paiements et l'adresse statique. Cette technique élimine le besoin de générer de nouvelles adresses de réception vierges pour chaque transaction, ce qui permet d'éviter les interactions habituelles dans Bitcoin où le destinataire doit fournir une nouvelle adresse au payeur.

Avec les Silent Payments, le payeur utilise les clés publiques du destinataire (clé publique de dépense et clé publique de scan) et la somme de ses clés privées personnelles en input pour générer une adresse vierge pour chaque paiement. Seul le destinataire, grâce à ses clés privées, peut calculer la clé privée correspondant à cette adresse de paiement. On utilise ECDH (*Elliptic-Curve Diffie-Hellman*), un algorithme cryptographique d'échange de clés, pour établir un secret partagé qui sert ensuite à dériver l'adresse de réception et la clé privée (uniquement du côté du destinataire). Pour identifier les Silent Payments qui leur sont destinés, les destinataires doivent scanner la blockchain et examiner chaque transaction correspondant aux critères du protocole. Contrairement au BIP47, qui utilise une transaction de notification pour établir le canal de paiement, les Silent Payments suppriment cette étape, ce qui permet d'économiser une transaction. Toutefois, le compromis est que le destinataire doit scanner l'ensemble des transactions potentielles pour déterminer, en appliquant ECDH, si elles lui sont adressées.

Par exemple, l'adresse statique de Bob $B$ représente la concaténation de sa clé publique de scan et de sa clé publique de dépense :

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Ces clés sont simplement dérivées à partir du chemin suivant :

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Cette adresse statique est publiée par Bob. Alice la récupère pour faire un Silent Payment vers Bob. Elle calcule l'adresse de paiement $P_0$ appartenant à Bob de cette façon :

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Où :

$$  \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A)  $$

Avec :
* $B_{\text{scan}}$ : La clé publique de scan de Bob (adresse statique) ;
* $B_{\text{spend}}$ : La clé publique de dépense de Bob (adresse statique) ;
* $A$ : La somme des clés publiques en input (tweak) ;
* $a$ : La clé privée du tweak, c'est-à-dire la somme de toutes les paires de clés utilisées dans les `scriptPubKey` des UTXOs consommés en inputs de la transaction d'Alice ;
* $\text{outpoint}_L$ : Le plus petit UTXO (lexicographiquement) utilisé en input de la transaction d'Alice ;
* $\text{ ‖ }$ : La concaténation (opération qui consiste à mettre bout-à-bout les opérandes) ;
* $G$ : Le point générateur de la courbe elliptique `secp256k1` ;
* $\text{hash}$ : La fonction de hachage SHA256 taguée avec `BIP0352/SharedSecret` ;
* $P_0$ : La première clé publique / adresse unique pour le paiement vers Bob ;
* $0$ : Un entier permettant de générer plusieurs adresses de paiement uniques.

Bob scanne la blockchain pour trouver son Silent Payment de cette manière :

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

Avec :
* $b_{\text{scan}}$ : La clé privée de scan de Bob.

S'il trouve $P_0$ comme une adresse qui contient un Silent Payment lui étant adressé, il calcule $p_0$, la clé privée permettant de dépenser les fonds envoyés par Alice sur $P_0$ :

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

Avec :
* $b_{\text{spend}}$ : La clé privée de dépense de Bob ;
* $n$ : l'ordre de la courbe elliptique `secp256k1`.

En plus de cette version de base, on peut également utiliser des labels qui permettent de générer plusieurs adresses statiques différentes à partir d'une même adresse statique de base, dans le but de séparer plusieurs utilisations, sans pour autant multiplier irraisonnablement le travail requis lors du scanning.


