---
term: CODE DE PAIMENT RÉUTILISABLE
---

Dans le BIP47, un code de paiement réutilisable est un identifiant statique généré à partir d'un portefeuille Bitcoin permettant d'engager une transaction de notification et de dériver des adresses uniques. Cela permet de ne pas faire de réutilisation d'adresses, qui mènent à une perte de la confidentialité, sans pour autant devoir dériver et transmettre manuellement de nouvelles adresses vierges à chaque paiement. Dans le BIP47, les codes de paiement réutilisables sont construits de la manière suivante :
* L'octet 0 correspond à la version ;
* L'octet 1 est un champ de bits permettant d'ajouter des informations en cas d'utilisation spécifique ;
* L'octet 2 permet d'indiquer la parité du `y` de la clé publique ;
* De l'octet 3 à l'octet 34, on retrouvera la valeur `x` de la clé publique ;
* De l'octet 35 à l'octet 66, il y a le code de chaîne associé à la clé publique ;
* De l'octet 67 à l'octet 79, il y a du rembourrage de zéros.

On ajoute généralement un HRP au départ du code de paiement et une somme de contrôle à la fin, puis on l'encode en base58. La construction d'un code de paiement est donc assez proche de celle d'une clé étendue. Voici mon propre code de paiement BIP47 en base58 par exemple :

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

Dans l'implémentation PayNym du BIP47, les codes de paiement peuvent également être exprimés sous la forme d'identifiants associés à l'image d'un robot. Voici le mien par exemple : 

```text
+throbbingpond8B1
```

L'utilisation de codes de paiements avec l'implémentation PayNym est actuellement disponible sur Sparrow Wallet sur PC et sur Samourai Wallet sur mobile.

