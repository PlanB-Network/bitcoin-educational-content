---
term: BIP9
---

Méthode d'activation de soft forks sur Bitcoin proposée en 2015. Elle introduit un système où les mineurs signalent leur soutien à un soft fork en utilisant un bit spécifique dans le champ de version des blocs. Un soft fork proposé sous BIP9 est activé si 95 % des blocs sur une période de 2016 blocs (environ deux semaines, coïncidant avec chaque ajustement de difficulté) signalent leur approbation. Après ce verrouillage, un délai est accordé pour que les mineurs se préparent à la mise à jour avant son activation. En cas d'échec à atteindre le seuil de 95 % dans la durée maximale prévue, le soft fork est abandonné. Le BIP9 permet la signalisation de plusieurs soft forks simultanément, mais donne un pouvoir considérable aux mineurs, car si le seuil requis n'est pas atteint, le soft fork est simplement abandonné. Cette méthode était celle initialement utilisée pour SegWit, avant que le BIP148 qui suggère l'utilisation d'un UASF ne vienne rebattre les cartes et forcer le verrouillage via le BIP91.

