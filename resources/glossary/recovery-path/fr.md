---
term: CHEMIN DE RÉCUPÉRATION
---

Dans un logiciel de portefeuille utilisant Miniscript, comme Liana par exemple, le ou les chemins de récupération désignent des ensembles de clés qui ne deviennent opérationnels qu'après une période d'inactivité définie dans le script qui bloque les bitcoins (timelock). Les chemins de récupération sont utilisables seulement une fois que les timelocks sont passés, et offrent ainsi une méthode de récupération des fonds lorsque le chemin primaire n'est pas disponible. Prenons l'exemple d'un script qui intègre 2 clés distinctes : la clé A, qui autorise la dépense immédiate des bitcoins, et la clé B, qui permet de les dépenser après un délai défini par un timelock de 52 560 blocs. Dans cet exemple, la clé A provient du chemin primaire, tandis que la clé B provient du chemin de récupération.


