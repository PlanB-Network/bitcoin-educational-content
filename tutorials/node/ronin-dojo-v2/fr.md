---
name: RoninDojo v2
description: Installer son nœud Bitcoin RoninDojo v2 sur un Raspberry Pi
---
![cover RoninDojo v2](assets/cover.jpeg)

> "*Use Bitcoin with privacy.*"

Dans [un précédent tutoriel](https://planb.network/tutorials/node/ronin-dojo), nous avions déjà expliqué la procédure d'installation et d'utilisation de RoninDojo v1. Cependant, au cours de l'année dernière, les équipes de RoninDojo ont lancé la version 2 de leur implémentation, qui a marquée un tournant significatif dans l'architecture du logiciel. En effet, ils ont délaissé la distribution Linux Manjaro au profit de Debian. Par conséquence, ils ne proposent plus d'image préconfigurée pour une installation automatique sur Raspberry Pi. Mais il existe tout de même une méthode pour procéder à une installation manuelle. C'est ce que j'ai utilisé pour mon propre nœud, et depuis, RoninDojo v2 fonctionne à merveille sur mon Raspberry Pi 4 depuis plusieurs mois. Je vous propose donc un nouveau tutoriel pour savoir comment installer manuellement RoninDojo v2 sur un Raspeberry Pi.


## Sommaire :
- Qu'est-ce que RoninDojo ?
- Quel matériel choisir pour installer RoninDojo v2 ?
- Comment monter le Raspberry Pi 4 ?
- Comment installer RoninDojo v2 sur un Raspberry Pi 4 ?
- Comment utiliser son nœud RoninDojo v2 ?



## Qu'est-ce que RoninDojo ? 
[Dojo](https://samouraiwallet.com/dojo) est initialement une implémentation de nœud complet Bitcoin, fondée sur Bitcoin Core, et mise au point par les équipes de Samourai Wallet. Cette solution peut être installée sur n'importe quel équipement. Contrairement à d'autres implémentations de Core, Dojo a été spécifiquement optimisé pour s'intégrer à l'environnement de l'application Android Samourai Wallet. Quant à RoninDojo, il s'agit d'un utilitaire conçu pour faciliter l'installation et la gestion de Dojo, ainsi que de divers autres outils complémentaires. En somme, RoninDojo enrichit l'implémentation de base de Dojo en y intégrant une multitude d'outils supplémentaires, tout en simplifiant son installation et sa gestion.

Ronin proposent [également une solution de node-in-box, dénommé le « *Tanto* »](https://ronindojo.io/en/products), un dispositif avec RoninDojo déjà installé sur un système assemblé par leur équipe. Le Tanto est une option payante, qui peut être intéressante pour ceux qui préfèrent éviter les complications techniques. Mais le code source de RoninDojo étant ouvert, il est aussi possible de le déployer sur son propre matériel. Cette alternative, plus économique, nécessite néanmoins quelques manipulations supplémentaires, que nous allons aborder dans ce tutoriel.

RoninDojo est un Dojo, il permet donc d'intégrer facilement Whirlpool CLI à votre nœud Bitcoin afin de disposer de la meilleure expérience possible de CoinJoin. Avec Whirlpool CLI, il devient possible de procéder au remixage de vos bitcoins de manière continue, 24 heures sur 24, 7 jours sur 7, sans nécessiter que votre ordinateur personnel reste allumé, tout en renforçant significativement votre confidentialité.

Au-delà de Whirlpool CLI, RoninDojo embarque une panoplie d'outils venant renforcer les fonctionnalités de votre Dojo. Parmi ceux-ci, le calculateur Boltzmann analyse le niveau de confidentialité de vos transactions, le serveur Electrum permet la connexion de vos portefeuilles Bitcoin à votre nœud, et le serveur Mempool vous permet de visualiser vos transactions en local, sans faire fuiter des informations.

En comparaison avec d'autres solutions de nœuds comme Umbrel, RoninDojo est clairement axé sur les solutions on-chain et les outils de confidentialité. Contrairement à Umbrel, RoninDojo ne supporte pas la mise en place d'un nœud Lightning ni l'intégration d'applications serveur plus généralistes. Bien que RoninDojo propose un nombre moins important d'outils polyvalents que Umbrel, il dispose de toutes les fonctionnalités essentielles pour gérer son activité on-chain.

Si vous n'avez pas besoin de fonctionnalités généralistes ou liées au Lightning Network comme proposées par Umbrel, et que vous recherchez un nœud simple, stable, avec des outils essentiels tels que Whirlpool ou Mempool, RoninDojo pourrait être la solution idéale. Tandis qu'Umbrel tend à devenir un mini-serveur multitâche orienté vers le Lightning Network et la polyvalence, RoninDojo, en accord avec la philosophie de Samourai Wallet, se concentre sur les outils fondamentaux pour la confidentialité de l'utilisateur.

Maintenant que nous avons pu dresser le portrait de RoninDojo, voyons ensemble comment mettre en place ce nœud.

## Quel matériel choisir pour installer RoninDojo v2 ?
RoninDojo propose une image permettant une installation automatique de son logiciel sur un [RockPro64](https://ronindojo.io/en/download). Cependant, notre tutoriel se concentre sur la procédure manuelle d'installation sur un Raspberry Pi 4. Bien que le Raspberry Pi 5 ait été récemment lancé, et que ce tutoriel devrait théoriquement être compatible avec ce nouveau modèle, je n'ai pas encore eu l'occasion de le tester personnellement, et je n'ai trouvé aucun retour d'expérience au sein de la communauté. Dès que j'aurai acquis le Pi 5 et les composants compatibles, je mettrai ce tutoriel à jour pour vous tenir informés. En attendant, je vous recommande de privilégier le Pi 4, car il fonctionne parfaitement pour mon nœud.

Pour ma part, je fais fonctionner RoninDojo sur un Raspberry Pi doté de 8 Go de RAM. Bien que certains membres de la communauté aient réussi à le faire fonctionner sur des appareils avec seulement 4 Go de RAM, je n'ai pas testé cette configuration moi-même. Étant donné la faible différence de prix, il me semble judicieux de choisir la version 8 Go de RAM. Cela pourrait également s'avérer utile si vous envisagez de réaffecter votre Raspberry Pi à d'autres usages dans le futur.

Il est important de noter que les équipes de RoninDojo ont signalé des problèmes fréquents liés au boîtier et à l'adaptateur SSD. J'ai moi-même été confronté à ces problèmes. **Il est donc fortement recommandé d'éviter les boîtiers équipés d'un câble USB pour le SSD de votre nœud.** Privilégiez à la place une carte d'extension de stockage conçue spécifiquement pour votre Raspberry Pi :

![carte extension stockage RPI4](assets/1.png)

Pour stocker la blockchain Bitcoin, il vous faudra un SSD compatible avec la carte d'extension de stockage que vous avez choisie. Actuellement (février 2024), nous nous trouvons dans une phase de transition. Il est prévu que, dans quelques mois, les disques de 1 To ne suffiront plus pour contenir la taille croissante de la blockchain, surtout en considérant les diverses applications que vous prévoyez d'intégrer à votre nœud. Certains recommandent donc d'investir dans un SSD de 2 To pour être tranquille sur le long terme. Cependant, avec la tendance à la baisse des prix des SSD d'année en année, d'autres suggèrent de se contenter d'un disque de 1 To, qui devrait être suffisant pour un ou deux ans, argumentant qu'au moment où celui-ci deviendra obsolète, le coût des modèles de 2 To aura probablement diminué. Le choix dépend donc de vos préférences personnelles. Si vous envisagez de garder votre RoninDojo pour une durée significative et souhaitez éviter toute manipulation technique dans les années à venir, l'option d'un SSD de 2 To semble être la plus judicieuse, car elle vous offre une marge confortable pour l'avenir.

En complément, vous aurez besoin de divers petits composants :
- Un boîtier équipé d'un ventilateur pour accueillir votre Raspberry Pi et votre carte d'extension de stockage. Des kits incluant à la fois la carte d'extension pour le SSD et un boîtier compatible sont disponibles en ligne ;
- Un câble d'alimentation pour votre Raspberry Pi ;
- Une carte micro SD d'au moins 16 Go (bien que 8 Go puissent techniquement suffire, la différence de prix entre les cartes de 8 et 16 Go est souvent négligeable) ;
- Un câble Ethernet RJ45 pour la connexion réseau.


## Comment monter le Raspberry Pi 4 ?





## Comment installer RoninDojo v2 sur un Raspberry Pi 4 ?

### Étape 1 : Préparer la micro SD bootable









## Comment utiliser son nœud RoninDojo v2 ?



### Connecter ses logiciels de portefeuilles à Electrs




### Connecter ses logiciels de portefeuilles à Samourai Dojo




### Utiliser son propre explorateur de blocs Mempool.space





### Utiliser Whirlpool pour mixer ses bitcoins





### Utiliser Whirlpool Stat Tool (WST)






### Utiliser le calculateur Boltzmann




### Les autres fonctionnalités de votre RoninDojo v2





**Ressources externes :**
- [https://samouraiwallet.com/dojo](https://samouraiwallet.com/dojo)
- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://code.samourai.io/ronindojo/RoninDojo](https://code.samourai.io/ronindojo/RoninDojo)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://oxt.me/](https://oxt.me/)
- [https://kycp.org/#/](https://kycp.org/#/)
