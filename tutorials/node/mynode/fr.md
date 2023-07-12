---
name: Mon Node
description: Configurez votre nœud Bitcoin MyNode
---

# Installer Bitcoin Core sur Mac ou Windows

![image](assets/0.jpeg)

https://mynodebtc.com/

La manière la plus simple et la plus puissante d'exécuter un nœud Bitcoin et Lightning ! Nous combinons les meilleurs logiciels open source avec notre interface, notre gestion et notre support afin que vous puissiez utiliser Bitcoin et Lightning facilement, en toute confidentialité et en toute sécurité.

> Le guide suivant a été offert par Parman (https://twitter.com/parman_the), vous pouvez lui donner des pourboires ici : dandysack84@walletofsatoshi.com Source originale : https://armantheparman.com/mynode-bitcoin-node-easy-setup-guide-raspberry-pi/

## Types de configurations de nœuds

Il existe différentes configurations de nœuds. MyNode est excellent. Il y a de nombreuses applications incluses, et encore plus si vous payez pour la version premium. Il est sinon très fastidieux de télécharger toutes ces applications vous-même. MyNode rend cela assez facile, comme vous le verrez.

Une autre option similaire est RaspiBlitz. L'interface graphique n'est pas aussi agréable et les applications se chevauchent beaucoup avec celles de MyNode, mais Raspiblitz est un logiciel open source gratuit (FOSS) tandis que MyNode ne l'est pas tout à fait. Une autre différence est que MyNode s'exécute dans un conteneur Docker. Je trouve Docker intimidant et difficile à dépanner. Cela ne pose problème que si vous rencontrez des erreurs ou des bugs. Le développeur propose de l'aide aux utilisateurs premium et il existe également un groupe de discussion Telegram.

Le RaspiBlitz est simplement un ensemble de programmes installés sur Linux, sans Docker. Le disque dur externe peut facilement être connecté à une autre machine Linux avec Bitcoin Core, et vous voilà prêt à partir, si besoin.

Une autre option consiste simplement à installer Bitcoin Core et une variété de serveur Electrum (il en existe plusieurs) sur un système d'exploitation. J'ai des guides pour Linux (Raspberry Pi), Mac et Windows.

## Liste de courses

- Raspberry Pi 4, 4 Go de mémoire ou 8 Go (4 Go suffisent)

- Alimentation officielle Raspberry Pi (Très important ! N'achetez pas de générique, sérieusement)

- Un boîtier pour le Pi. Le boîtier FLIRC est génial. Tout le boîtier est un dissipateur thermique et vous n'avez pas besoin d'un ventilateur, ce qui peut être bruyant.

- Carte microSD de 16 Go (vous en avez besoin, mais en avoir quelques-unes est pratique)

- Un lecteur de carte mémoire (la plupart des ordinateurs n'ont pas de fente pour carte microSD).

- Disque dur externe SSD 1 To.  
  Remarque : le SSD est crucial. N'utilisez pas de disque dur externe portable même s'il est moins cher.

- Un câble Ethernet (pour se connecter à votre routeur domestique)

- Vous n'avez pas besoin d'un écran

## Télécharger l'image MyNode

Accédez au site Web de MyNode Lien

![image](assets/1.jpeg)

Cliquez sur <Télécharger maintenant>

Téléchargez la version pour Raspberry Pi 4 :

![image](assets/2.jpeg)

C'est un gros fichier :

![image](assets/3.jpeg)

Téléchargez les hachages SHA 256

![image](assets/4.jpeg)

Ouvrez le terminal sur Mac ou Linux ou l'invite de commandes sur Windows. Tapez :

```
Mac/Linux : "shasum -a 256 NOMDUFICHIERTELECHARGE"
Windows : "certUtil -hashfile NOMDUFICHIERTELECHARGE SHA256"
```

L'ordinateur réfléchit pendant environ 20 secondes. Ensuite, vérifiez que le hachage de sortie correspond à celui téléchargé depuis le site Web à l'étape précédente. S'ils sont identiques, vous pouvez continuer.
Flashez la carte SD

## Télécharger et installer Balena Etcher. Lien

Je n'ai pas pu trouver la signature numérique pour cela. Si vous savez comment faire, veuillez me le faire savoir et je mettrai à jour cet article.
Etcher est facile à utiliser. Insérez votre carte micro SD et flasher le logiciel Raspberry Pi (.img file) sur la carte SD.

![image](assets/5.jpeg)
![image](assets/6.jpeg)
![image](assets/7.jpeg)
![image](assets/8.jpeg)
![image](assets/9.jpeg)
![image](assets/10.jpeg)
![image](assets/11.jpeg)

Une fois terminé, le lecteur n'est plus lisible. Vous pouvez recevoir une erreur du système d'exploitation et le lecteur devrait disparaître du bureau. Retirez la carte.

## Configurez le Pi et insérez la carte SD

Les pièces (le boîtier n'est pas montré) :

![image](assets/12.jpeg)
![image](assets/13.jpeg)

Connectez le câble Ethernet et le connecteur USB du disque dur (pas encore l'alimentation). Évitez de vous connecter aux ports USB de couleur bleue au centre. Ce sont des ports USB 3. MyNode vous recommande d'utiliser le port USB 2, même si le disque peut être compatible USB 3.

![image](assets/14.jpeg)

La carte micro SD va ici :

![image](assets/15.jpeg)

Enfin, connectez l'alimentation :

![image](assets/16.jpeg)

## Trouvez l'adresse IP du Pi

Vous n'avez jamais besoin d'un moniteur avec MyNode. Cependant, vous avez besoin d'un autre ordinateur sur le réseau domestique. Si votre Pi n'est pas connecté par Ethernet et que vous souhaitez utiliser le WiFi, trouver l'adresse IP nécessite des compétences informatiques avancées. Je ne peux pas vous aider, désolé. Vous avez besoin d'une connexion Ethernet. (Le problème vient du fait qu'il faut accéder à un moniteur et au système d'exploitation pour se connecter au WiFi et entrer un mot de passe).

Vérifiez votre routeur pour obtenir une liste de toutes les adresses IP des appareils connectés.

J'ai tapé 192.168.0.1 dans le navigateur (instructions fournies avec mon routeur), me suis connecté et j'ai pu voir un appareil "MyNode" avec l'adresse IP 192.168.0.18. Notez que ces adresses IP ne sont pas visibles sur Internet (elles passent d'abord par le routeur), ce sont simplement des identifiants pour les appareils de votre réseau domestique.

Trouver l'adresse IP est crucial.

> MISE À JOUR : vous pouvez utiliser le terminal sur un Mac ou une machine Linux pour trouver l'adresse IP de tous les appareils connectés par Ethernet sur le réseau domestique en utilisant la commande "arp -a". La sortie n'est pas aussi jolie que ce que le routeur affichera, mais toutes les informations dont vous avez besoin sont là. Si ce n'est pas évident quel est le Pi, procédez par essais et erreurs.

## SSH dans le Pi

Vous avez la possibilité de vous connecter à distance à l'appareil par la commande SSH, mais ce n'est pas obligatoire (c'est le cas pour RaspiBlitz Node). Je vais quand même vous montrer comment le faire, car c'est très pratique.

Ouvrez un ordinateur Mac ou Linux (pour Windows, téléchargez putty, un outil SSH) et tapez :

```
ssh admin@192.168.0.18
```

Utilisez votre propre adresse IP. Le nom d'utilisateur pour l'appareil MyNode est "admin" par défaut. Le mot de passe est "bolt" par défaut.

Si vous avez déjà utilisé votre Pi et avez interverti la carte micro SD, vous obtiendrez cette erreur :

![image](assets/17.jpeg)

Ce que vous devez faire, c'est accéder à l'endroit où se trouve le fichier "known_hosts" et le supprimer. C'est sans danger. Le message d'erreur vous montre le chemin. Pour moi, c'était /Users/MyUserName/.ssh/'
N'oubliez pas le "." avant ssh, cela indique qu'il s'agit d'un répertoire caché.
Ensuite, essayez à nouveau la commande ssh.

Cette fois, vous verrez cette sortie :

![image](assets/18.jpeg)

Le fichier que vous avez supprimé a été supprimé et vous ajoutez une nouvelle empreinte. Tapez oui et <enter>.

On vous demandera de saisir le mot de passe. C'est "bolt".

Vous avez maintenant accès au terminal du MyNode Pi, sans moniteur, et vous pouvez confirmer que tout s'est bien chargé.

![image](assets/19.jpeg)

## Accès via le navigateur Web

Ouvrez un navigateur. Il doit s'agir d'un ordinateur de votre réseau domestique, vous ne pouvez pas le faire depuis l'extérieur. Il y a un moyen, mais c'est difficile. Je ne l'ai pas testé.

Saisissez l'adresse IP dans la barre d'adresse du navigateur. Cela se produira :

![image](assets/20.jpeg)

Entrez le mot de passe "bolt" - changez-le plus tard.

Ensuite, cela se produira :

![image](assets/21.jpeg)

Choisissez "Format Drive"

![image](assets/22.jpeg)

Maintenant, nous attendons.

À un moment donné, on vous demandera si vous souhaitez entrer votre clé de produit ou utiliser la version gratuite "community edition" - je vais vous montrer la version Premium. Je recommande vivement de payer pour la version premium si vous en avez les moyens, cela en vaut vraiment la peine.

![image](assets/23.jpeg)

Vous verrez ensuite la progression des blocs téléchargés. Cela prend des jours :

![image](assets/24.jpeg)

Il est sûr d'éteindre la machine pendant le téléchargement si nécessaire. Allez dans les paramètres et trouvez le bouton pour éteindre la machine. Ne tirez pas simplement sur le cordon, vous pourriez corrompre l'installation ou le disque dur.

Assurez-vous, dès le début, d'aller dans "Paramètres" et de désactiver quicksync. Cela commencera le téléchargement initial des blocs depuis le début.

![image](assets/25.jpeg)

Je voulais continuer à créer le guide, donc voici un autre MyNode que j'ai préparé plus tôt. Voici à quoi ressemble la page lorsque la blockchain est synchronisée et que plusieurs "apps" ont été activées et synchronisées :

![image](assets/26.jpeg)

Notez que le serveur Electrum doit également se synchroniser, donc dès que la blockchain Bitcoin est synchronisée, cliquez sur le bouton pour démarrer ce processus - cela prend un jour ou deux. Tout le reste est activé en quelques minutes une fois que vous choisissez de l'activer. Vous pouvez cliquer sur des choses et explorer. Vous ne casserez rien. Si quelque chose se casse (cela m'est arrivé, mais je pense que c'est parce que j'avais des pièces bon marché), vous devrez re-flasher et recommencer le téléchargement. Le problème que j'ai avec MyNode, c'est que si vous devez "re-flasher", vous devez recommencer la synchronisation de la blockchain depuis le début. Il existe des moyens techniques de contourner cela, mais ce n'est pas facile.

Si vous souhaitez essayer un autre nœud également, par exemple un RaspiBlitz, vous avez besoin d'un disque dur externe SSD supplémentaire et d'une autre carte micro SD à flasher. Sinon, c'est le même équipement, vous ne pouvez tout simplement pas exécuter MyNode et RaspiBlitz simultanément, évidemment. Si vous voulez le faire, il est temps de chercher un autre Raspberry Pi.

Maintenant que vous avez un nœud en cours d'exécution, utilisez-le, ne le laissez pas simplement là à ne rien faire pour vous. Suivez mon article (et vidéo) sur la façon de connecter votre portefeuille de bureau Electrum à Electrum Server et Bitcoin Core ici.

> Le guide suivant a été offert par Parman (https://twitter.com/parman_the)'
> '> vous pouvez lui donner des pourboires ici; dandysack84@walletofsatoshi.com Source originale; https://armantheparman.com/mynode-bitcoin-node-easy-setup-guide-raspberry-pi/'
