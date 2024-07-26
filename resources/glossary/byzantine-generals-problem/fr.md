---
term: PROB. DES GÉNÉRAUX BYZANTINS
---

Problème formulé pour la première fois par Leslie Lamport, Robert Shostak et Marshall Pease dans le magazine spécialisé *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* [« The Byzantine Generals Problem »](https://lamport.azurewebsites.net/pubs/byz.pdf) en juillet 1982. Il est utilisé aujourd'hui pour illustrer les défis en termes de prise de décision quand un système distribué ne peut faire confiance à aucun acteur.

Dans cette métaphore, un groupe de généraux byzantins et leurs armées respectives sont campés autour d'une ville qu'ils souhaitent attaquer ou assiéger. Les généraux sont géographiquement séparés les uns des autres et doivent communiquer par messager pour coordonner leur stratégie. Qu'ils attaquent ou qu'ils battent en retraite n'a pas d'importance, du moment que tous les généraux parviennent à un consensus. 

Par conséquent, nous pouvons considérer les exigences suivantes :
* Chaque général doit prendre une décision : attaquer ou battre en retraite (oui ou non) ;
* Une fois la décision prise, elle ne peut plus être modifiée ;
* Tous les généraux doivent se mettre d'accord sur la même décision et l'exécuter de manière synchronisée.

De plus, un général ne peut communiquer avec un autre que par le biais de messages transmis par un coursier, pouvant être retardés, détruits, modifiés ou perdus. Et même si un message réussi à être délivré, un ou plusieurs généraux peuvent choisir (pour une raison quelconque) de trahir la confiance établie et d'envoyer un message frauduleux, et semer le chaos.

Si on applique le dilemme au contexte de la blockchain Bitcoin, chaque général représente un nœud du réseau, devant parvenir à un consensus sur l'état du système. En d'autres termes, La majorité des participants d'un réseau distribué doivent se mettre d'accord et exécuter la même action afin d'éviter une défaillance totale. Le seul moyen de parvenir à un consensus dans ce type de système distribué est d'avoir au moins 2/3 des nœuds de réseau fiables et honnêtes. Donc, si la majorité du réseau décide d'agir de manière malveillante, le système est vulnérable.

> ► *Ce dilemme est parfois également appelé « Problème de la diffusion cohérente ».*

