---
term: RÉORGANISATION
---

Se réfère à un phénomène dans lequel la blockchain subit une modification de sa structure à cause de l'existence de blocs concurrents à une même hauteur. Cela survient lorsqu'une portion de la chaîne de blocs est remplacée par une autre chaîne ayant une quantité de travail accumulé plus importante.

Ces réorganisations font partie du fonctionnement naturel de Bitcoin, où différents mineurs peuvent trouver de nouveaux blocs presque simultanément, venant ainsi couper le réseau Bitcoin en deux. Dans de tels cas, le réseau peut se diviser temporairement en chaînes concurrentes. Finalement, lorsque l'une de ces chaînes accumule plus de travail, les autres chaînes sont abandonnées par les nœuds, et leurs blocs deviennent ce que l'on appelle des « blocs obsolètes » ou « blocs orphelins ». Ce processus de remplacement d'une chaîne par une autre est la réorganisation.

![](../../dictionnaire/assets/9.webp)

Les réorganisations peuvent avoir diverses conséquences. Tout d'abord, si un utilisateur avait une transaction confirmée dans un bloc qui s'avère être abandonné, mais que celle-ci ne se retrouve pas dans la chaîne finalement valide, alors sa transaction redevient non confirmée. C'est pour cette raison que l'on vous conseille de toujours attendre au moins 6 confirmations pour considérer une transaction comme réellement immuable. Passé 6 blocs de profondeur, les réorganisations sont tellement improbables que la chance qu'il y en ait une peut être considérée comme nulle.

Ensuite, au niveau du système global, les réorganisations impliquent un gaspillage de la puissance de calcul des mineurs. En effet, lorsqu'une division intervient, une partie des mineurs seront sur la chaîne `A`, et une autre partie sur la chaîne `B`. Si la chaîne `B` est finalement abandonnée lors d'une réorganisation, alors toute la puissance de calcul déployée par les mineurs sur cette chaîne est par définition gaspillée. S'il y a trop de réorganisations sur le réseau Bitcoin, la sécurité globale de celui-ci est donc réduite. C'est notamment pour cette raison, en partie, que l'augmentation de la taille des blocs ou la réduction de l'intervalle entre chaque bloc (10 minutes) peuvent être dangereuses.

> ► *Certains bitcoiners préfèrent parler de « bloc orphelin » pour désigner un bloc périmé. Aussi, dans le langage courant, on parle d'une « réorg » pour désigner une « réorganisation ». Le terme de « réorganisation » est un anglicisme. Pour être plus juste, on pourrait parler d'une « resynchronisation ».*

