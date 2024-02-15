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

![carte extension stockage RPI4](assets/fr/1.png)

Pour stocker la blockchain Bitcoin, il vous faudra un SSD compatible avec la carte d'extension de stockage que vous avez choisie. Actuellement (février 2024), nous nous trouvons dans une phase de transition. Il est prévu que, dans quelques mois, les disques de 1 To ne suffiront plus pour contenir la taille croissante de la blockchain, surtout en considérant les diverses applications que vous prévoyez d'intégrer à votre nœud. Certains recommandent donc d'investir dans un SSD de 2 To pour être tranquille sur le long terme. Cependant, avec la tendance à la baisse des prix des SSD d'année en année, d'autres suggèrent de se contenter d'un disque de 1 To, qui devrait être suffisant pour un ou deux ans, argumentant qu'au moment où celui-ci deviendra obsolète, le coût des modèles de 2 To aura probablement diminué. Le choix dépend donc de vos préférences personnelles. Si vous envisagez de garder votre RoninDojo pour une durée significative et souhaitez éviter toute manipulation technique dans les années à venir, l'option d'un SSD de 2 To semble être la plus judicieuse, car elle vous offre une marge confortable pour l'avenir.

En complément, vous aurez besoin de divers petits composants :
- Un boîtier équipé d'un ventilateur pour accueillir votre Raspberry Pi et votre carte d'extension de stockage. Des kits incluant à la fois la carte d'extension pour le SSD et un boîtier compatible sont disponibles en ligne ;
- Un câble d'alimentation pour votre Raspberry Pi ;
- Une carte micro SD d'au moins 16 Go (bien que 8 Go puissent techniquement suffire, la différence de prix entre les cartes de 8 et 16 Go est souvent négligeable) ;
- Un câble Ethernet RJ45 pour la connexion réseau.

![matériel noeud](assets/fr/2.png)

## Comment monter le Raspberry Pi 4 ?
L'assemblage de votre nœud variera en fonction du matériel choisi, en particulier du type de boîtier. Toutefois, les grandes lignes des étapes à suivre restent généralement similaires dans le montage.

Commencez par installer votre SSD sur la carte d'extension de stockage, en prenant soin de fixer les deux vis de verrouillage à l'arrière.

![montage1](assets/fr/3.png)

Puis fixez votre Raspberry Pi sur la carte d'extension.

![montage2](assets/fr/4.png)

Fixez également le ventilateur sur le Raspberry Pi.

![montage3](assets/fr/5.png)

Connectez les différents éléments en prêtant attention à utiliser les bonnes broches, en vous référant à la notice d'instructions de votre boîtier. Les fabricants de boîtiers proposent souvent des tutoriels vidéo pour vous aider dans l'assemblage. Dans mon cas, je dispose d'une carte d'extension additionnelle équipée d'un bouton on/off. Cette dernière n'est pas indispensable pour faire un nœud Bitcoin. Je l'utilise principalement pour avoir un bouton de mise sous tension.

Si comme moi, vous avez une carte d'extension équipée d'un bouton marche/arrêt, n'oubliez pas d'installer le petit jumper « *Auto Power On* ». Cela permettra un démarrage automatique de votre nœud dès qu'il sera sous tension. Cette fonctionnalité s'avère particulièrement pratique en cas de coupure de courant, car elle permet à votre nœud de redémarrer de lui-même, sans intervention manuelle de votre part.

![montage4](assets/fr/6.png)

Avant d'insérer l'ensemble du matériel dans le boîtier, il est important de vérifier le bon fonctionnement de votre Raspberry Pi, de la carte d'extension de stockage et du ventilateur en les mettant sous tension.

![montage5](assets/fr/7.png)

Enfin, installez votre Raspberry Pi dans son boîtier. Attention, une étape ultérieure nécessitera l'ajout de la carte micro SD dans le port adapté sur le Raspberry. Si votre boîtier est équipé d'une ouverture permettant d'insérer la carte SD sans avoir à l'ouvrir (comme c'est le cas pour le mien illustré sur la photo), vous pouvez procéder à la fermeture du boîtier dès à présent. En revanche, si votre boîtier ne dispose pas d'un accès direct au port micro SD, il vous faudra attendre d'avoir préparé la carte micro SD pour l'insérer avant de finaliser l'assemblage.

![montage6](assets/fr/8.png)

## Comment installer RoninDojo v2 sur un Raspberry Pi 4 ?

### Étape 1 : Préparer la micro SD bootable

Après avoir assemblé votre matériel, l'étape suivante consiste à installer RoninDojo. Pour cela, nous allons préparer une carte micro SD bootable à partir de votre ordinateur, en y gravant l'image disque adéquat.

Il vous faudra utiliser le logiciel _**Raspberry Pi Imager**_, conçu pour faciliter le téléchargement, la configuration et l'écriture de systèmes d'exploitation sur une carte micro SD pour une utilisation avec un Raspberry Pi. Commencez par installer ce logiciel sur votre PC personnel :
- Pour Ubuntu/Debian : https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Pour Windows : https://downloads.raspberrypi.org/imager/imager_latest.exe 
- Pour Mac : https://downloads.raspberrypi.org/imager/imager_latest.dmg

Une fois le logiciel installé, ouvrez-le. À ce moment, insérez votre carte micro SD dans votre ordinateur personnel. Depuis l'interface de Raspberry Pi Imager, sélectionnez `CHOISIR L'OS` :

![choisir OS](assets/fr/9.png)

Ensuite, accédez au menu `Raspberry Pi OS (other)` :

![choisir OS autres](assets/fr/10.png)

Choisissez le système d'exploitation dénommé `Raspberry Pi OS (Legacy, 64-bits) Lite`, dont la taille est de `0.3 GB` :

![choisir OS Legacy Lite](assets/fr/11.png)

Après avoir sélectionné le système d'exploitation, vous serez redirigé vers le menu principal de Raspberry Pi Imager. Cliquez sur `CHOISIR LE STOCKAGE` :

![choisir stockage](assets/fr/12.png)

Sélectionnez votre carte micro SD :

![choisir micro sd](assets/fr/13.png)

Après avoir choisi le système d'exploitation et la carte micro SD, cliquez sur `SUIVANT` :

![choisir suivant](assets/fr/14.png)

Une nouvelle fenêtre apparaîtra. Sélectionnez `MODIFIER RÉGLAGES` :

![modifier réglages](assets/fr/15.png)

Dans cette fenêtre, accédez à l'onglet `GÉNÉRAL` et procédez aux réglages suivants (qui sont très importants pour que cela fonctionne) :
- Activez l'option et attribuez `RoninDojo` comme nom d'hôte ;
- Activez `Définir nom d'utilisateur et mot de passe`, saisissez `pi` comme nom d'utilisateur, choisissez un mot de passe et notez ces informations, car elles seront nécessaires ultérieurement. Ces identifiants sont temporaires et seront supprimés par la suite ;
- Désactivez `Configurer le Wi-Fi` ;
- Activez `Définir les réglages locaux` et sélectionnez votre fuseau horaire ainsi que le type de clavier correspondant à votre ordinateur ;

![réglages généraux](assets/fr/16.png)

Dans l'onglet SERVICES, cliquez sur la case `Activer SSH` et sélectionnez `Utiliser un mot de passe pour l'authentification` :

![réglages services](assets/fr/17.png)

Assurez vous également que dans l'onglet `OPTIONS`, la télémétrie est désactivée :

![réglages options](assets/fr/18.png)

Cliquez sur `ENREGISTRER` :

![réglages enregistrer](assets/fr/19.png)

Confirmez en cliquant sur `OUI` pour démarrer la création de la carte micro SD bootable :

![réglages oui](assets/fr/20.png)

Un message vous informera que toutes les données présentes sur la carte micro SD seront effacées. Confirmez en cliquant sur `OUI` pour lancer le processus :

![écraser micro SD](assets/fr/21.png)

Patientez jusqu'à ce que le logiciel termine de préparer votre carte micro SD :

![écriture micro SD](assets/fr/22.png)

Lorsque le message indiquant la fin du processus s'affiche, vous pouvez retirer la carte de votre ordinateur :

![écriture micro SD terminée](assets/fr/23.png)

### Étape 2 : Terminer le montage du nœud

Vous pouvez maintenant insérer la carte micro SD dans le port adapté de votre Raspberry Pi. 

![micro SD](assets/fr/24.png)

Connectez ensuite votre Raspberry Pi à votre box internet à l'aide du câble Ethernet. Pour finir, mettez votre nœud en marche en connectant le câble d'alimentation et en actionnant le bouton de mise sous tension (si votre configuration en est pourvue).

### Étape 3 : Établir une connexion SSH avec le nœud

Pour commencer, il est nécessaire de trouver l'adresse IP de votre nœud. Vous avez le choix entre utiliser un outil tel que _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ ou _[Angry IP Scanner](https://angryip.org/)_, ou consulter l'interface d'administration de votre routeur. L'adresse IP devrait se présenter sous la forme `192.168.1.??`. **Pour toutes les commandes qui suivent, remplacez `[IP]` par l'adresse IP réelle de votre nœud**, (en supprimant les crochets).

Lancez un terminal.

Pour éliminer une éventuelle clé déjà associée à l'adresse IP de votre nœud, exécutez la commande : `ssh-keygen -R [IP]`. Une erreur suite à cette commande n'est pas grave ; elle signifie simplement que la clé n'existe pas dans votre liste d'hôtes connus (ce qui est plutôt probable). Par exemple, si l'IP de votre nœud est `192.168.1.40`, la commande devient : `ssh-keygen -R 192.168.1.40`.

Ensuite, établissez une connexion SSH avec votre nœud en exécutant la commande : `ssh pi@[IP]`.

Un message s'affichera concernant l'authenticité de l'hôte : `The authenticity of host '[IP]' can't be established.`. Cela indique que l'authenticité de l'appareil auquel vous tentez de vous connecter ne peut être vérifiée faute de clé publique connue. Lors de la première connexion SSH à un nouvel hôte, ce message apparaît systématiquement. Vous devez répondre `yes` pour ajouter sa clé publique à votre répertoire local, ce qui empêchera l'affichage de ce message d'avertissement lors de connexions SSH futures à ce nœud. Saisissez donc `yes` et appuyez sur `entrer` pour valider.

Il vous sera ensuite demandé de saisir votre mot de passe, celui défini précédemment comme temporaire à l'étape 1. Validez avec `entrer`. Vous serez alors connecté à votre nœud via SSH.

En résumé, voici les commandes à exécuter :
- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `yes`
- Saisissez le mot de passe temporaire et validez.

### Étape 4 : Mise à jour et préparation

Vous êtes à présent connecté à votre nœud via une session SSH. Sur votre terminal, l'invite de commande devrait être : `pi@RoninDojo:~ $`. Pour commencer, mettez à jour la liste des paquets disponibles et installez les mises à jour des paquets existants avec la commande suivante :
`sudo apt update && sudo apt upgrade -y`

Une fois les mises à jour terminées, procédez à l'installation de *Git* et *Dialog* en utilisant la commande :
`sudo apt install git dialog -y` 

Ensuite, clonez la branche `master` du dépôt Git _RoninOS_ en exécutant :
`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`

Exécutez le script `customize-image.sh` avec la commande :
`cd /opt/RoninOS/ && sudo ./customize-image.sh`

**Il est important de laisser le script s'exécuter sans interruption et d'attendre patiemment la fin de son processus**, qui dure environ 10 minutes. Lorsque le message `Setup is complete` s'affiche, vous pouvez avancer vers l'étape suivante.

### Étape 5 : Lancement de RoninOS

Lancez RoninOS avec la commande :
`sudo systemctl start ronin-setup`

Affichez les lignes du fichier de log avec la commande :
`tail -f /home/ronindojo/.logs/setup.logs`

À cette étape, **il est important de laisser faire le lancement de RoninOS et d'attendre la fin** de son exécution. Cela prend environ 40 minutes. Lorsque `All RoninDojo feature installations complete!` apparaît, vous pouvez passer à l'étape 6.

### Étape 6 : Accéder à RoninUI et changer les identifiants

Après avoir finalisé l'installation, pour vous connecter à votre nœud via un navigateur, assurez-vous que votre ordinateur personnel soit connecté au même réseau local que votre nœud. Si vous utilisez un VPN sur votre machine, désactivez-le temporairement. Pour accéder à l'interface du nœud dans votre navigateur, saisissez dans la barre d'URL :
- Directement l'adresse IP de votre nœud, par exemple `192.168.1.??`.
- Ou bien tapez `ronindojo.local`.



.......





### Étape 7 : Supprimer les identifiants temporaires













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
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)
