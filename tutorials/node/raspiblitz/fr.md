---
name: RaspiBlitz
description: Guide pour configurer votre RaspiBlitz
---

![image](assets/0.jpeg)

# RaspiBlitz

Le RaspiBlitz est un nœud Lightning (LND et/ou Core Lightning) à faire soi-même, fonctionnant avec un Bitcoin-Fullnode sur un RaspberryPi (1TB SSD) et un bel écran pour une configuration et une surveillance faciles.

Le RaspiBlitz est principalement destiné à apprendre comment exécuter votre propre nœud décentralisé depuis chez vous - car : Pas votre nœud, pas vos règles. Découvrez et développez l'écosystème croissant du Lightning Network en en devenant un membre à part entière. Construisez-le lors d'un atelier ou en tant que projet de week-end.

![video](https://youtu.be/DTHlSPMz3ns)
RASPIBLITZ - Comment exécuter un nœud Lightning et Bitcoin Full Node par BTC session

# Guide d'installation de Raspiblitz de Parman

> Le guide suivant a été offert par Parman (https://twitter.com/parman_the), vous pouvez lui donner des pourboires ici : dandysack84@walletofsatoshi.com Source originale : https://armantheparman.com/raspiblitz/

Le Raspiblitz est un excellent système pour exécuter un nœud Bitcoin et des applications associées. Je recommande cela et le nœud My Node à la plupart des utilisateurs (idéalement, avoir deux nœuds pour la redondance). Un avantage majeur est que le nœud Raspiblitz est un "logiciel libre et open source", contrairement à MyNode ou Umbrel. Pourquoi est-ce important ? Vlad Costa explique. Vous pouvez également exécuter le RaspbiBlitz avec une connexion WiFi plutôt qu'Ethernet - voici un guide supplémentaire à ce sujet (je n'ai pas trouvé de moyen de le faire avec MyNode).

Vous pouvez acheter un nœud préfabriqué avec un écran miniaturisé intégré, ou vous pouvez le construire vous-même (vous n'avez pas besoin d'un écran).

Le guide sur la page GitHub est excellent, mais peut-être trop détaillé pour un utilisateur moyennement expérimenté. Mes instructions seront plus succinctes et, espérons-le, plus faciles à suivre.

Essentiellement, le processus est très similaire au processus de configuration d'un nœud MyNode avec un Raspberry Pi 4. Le guide Raspiblitz suggère d'acheter un moniteur, mais vous n'en avez vraiment pas besoin, et je ne le recommanderais pas. Vous n'avez même pas besoin d'un clavier ou d'une souris supplémentaires. Accédez simplement au menu terminal de l'appareil via un ordinateur connecté au même réseau domestique et utilisez la commande ssh dans le terminal. Cela est possible avec Linux/Mac (facile) et un peu plus difficile avec Windows.

## Étape 1 : Achetez le matériel.

Vous avez besoin exactement du même matériel que pour exécuter un nœud MyNode. Vous pouvez essayer l'un ou l'autre, la seule différence est les données sur la carte micro SD.

- Raspberry Pi 4, 4 Go de mémoire ou 8 Go (4 Go suffisent)
- Alimentation officielle Raspberry Pi (Très important ! N'achetez pas de générique, sérieusement)
- Un boîtier pour le Pi (le boîtier FLIRC est génial. Tout le boîtier est un dissipateur thermique et vous n'avez pas besoin d'un ventilateur, qui peut être bruyant)
- Carte microSD de 32 Go (vous en avez besoin d'une, mais quelques-unes sont pratiques)
- Un lecteur de carte mémoire (la plupart des ordinateurs n'ont pas de fente pour une carte microSD).
- Disque dur externe SSD 1 To.
- Un câble Ethernet (pour se connecter à votre routeur domestique).

Vous n'avez pas besoin d'un moniteur (ou d'un clavier ou d'une souris).
Note: Ceci est le mauvais disque dur: il s'agit d'un disque dur externe portable. Ce n'est pas un SSD. Le SSD est crucial. C'est pourquoi il est bon marché (Prix en AUD)

![image](assets/1.png)

Voici le bon type à obtenir:

![image](assets/2.png)

C'est plus rapide, mais inutilement cher:

![image](assets/3.png)

## Étape 2: Télécharger l'image Raspiblitz

Accédez au site web de Raspiblitz sur Github et trouvez le lien "télécharger l'image":

![image](assets/4.png)

Le hash sha-256 du fichier téléchargé est fourni sur le site web. Il changera à chaque mise à jour. Si vous ne comprenez pas de quoi il s'agit, vous devriez le faire, alors j'ai écrit un guide que vous pouvez lire ici.

![image](assets/5.png)

## Étape 3: Vérifier l'image

Avant de continuer, si vous ne connaissez pas le système de fichiers en ligne de commande, il est facile d'apprendre et vous devriez le faire.

Voici une vidéo utile pour Linux, mais qui s'applique également à Mac.

Pour Windows, voici un tutoriel simple.
Mac/Linux

Attendez que le téléchargement du fichier soit terminé (important!), puis ouvrez le terminal, accédez à l'endroit où vous avez téléchargé le fichier et tapez la commande suivante...

```
shasum -a 256 xxxxxxxxxxxxxx
```

où xxxxxxxxxxxxxx est le nom du fichier que vous venez de télécharger. Si vous n'êtes pas dans le répertoire où se trouve ce fichier, vous devez taper le chemin complet.

L'ordinateur réfléchit pendant environ 20 secondes. Vérifiez que le hash du fichier de sortie correspond à celui téléchargé depuis le site web à l'étape précédente. S'ils sont identiques, vous pouvez continuer.
Windows

Ouvrez l'invite de commandes et accédez à l'endroit où le fichier est téléchargé, puis tapez cette commande:

```
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```

où xxxxxxxxxxxxxx est le nom du fichier que vous venez de télécharger. Si vous n'êtes pas dans le répertoire où se trouve ce fichier, vous devez taper le chemin complet.

L'ordinateur réfléchit pendant environ 20 secondes. Vérifiez que le hash du fichier de sortie correspond à celui téléchargé depuis le site web à l'étape précédente. S'ils sont identiques, vous pouvez continuer.

## Étape 4: Flasher la carte SD

Vous pouvez utiliser Balena Etcher pour cela. Téléchargez-le ici.

Etcher est facile à utiliser. Insérez votre carte micro SD et flashez le logiciel Raspiblitz (.img) sur la carte SD.

![image](assets/6.png)

![image](assets/7.png)

![image](assets/8.png)

![image](assets/9.png)

Une fois terminé, le lecteur n'est plus lisible. Vous pouvez recevoir une erreur du système d'exploitation et le lecteur devrait disparaître du bureau. Retirez la carte.

## Étape 5: Configurer le Pi et insérer la carte SD

Les pièces (le boîtier n'est pas montré):

![image](assets/10.png)

![image](assets/11.png)

Connectez le câble Ethernet et le connecteur USB du disque dur (pas encore l'alimentation). Évitez de vous connecter aux ports USB de couleur bleue au centre. Ce sont des ports USB 3. Utilisez le port USB 2, même si le disque peut être compatible USB 3 (plus fiable).

![image](assets/12.png)

La carte micro SD va ici:

![image](assets/13.png)

Enfin, connectez l'alimentation:

![image](assets/14.png)

## Étape 6: Trouver l'adresse IP du Pi

Vous n'avez jamais besoin d'un moniteur avec le Raspiblitz. Cependant, vous avez besoin d'un autre ordinateur sur le réseau domestique. Si votre Pi n'est pas connecté par Ethernet et que vous souhaitez utiliser le WiFi, trouver l'adresse IP nécessite certaines compétences en informatique. Je ne peux pas vous aider, désolé. Vous avez besoin d'une connexion Ethernet. (Le problème vient du fait qu'il faut accéder à un moniteur et au système d'exploitation pour connecter le WiFi et entrer un mot de passe.)
Vérifiez votre routeur pour obtenir une liste de toutes les adresses IP des appareils connectés.

J'ai tapé 192.168.0.1 dans le navigateur (instructions fournies avec mon routeur), me suis connecté et j'ai pu voir mon appareil avec l'adresse IP 192.168.0.191. Notez que ces adresses IP ne sont pas visibles sur Internet (elles passent d'abord par le routeur), ce sont simplement des identifiants pour les appareils de votre réseau domestique.

Trouver l'adresse IP est crucial.

> MISE À JOUR : vous pouvez utiliser le terminal d'un Mac ou d'une machine Linux pour trouver l'adresse IP de tous les appareils connectés par Ethernet sur le réseau domestique en utilisant la commande "arp -a". La sortie n'est pas aussi jolie que ce que le routeur affichera, mais toutes les informations dont vous avez besoin sont là. Si ce n'est pas évident quel est le Pi, procédez par essais et erreurs.

## Étape 7 : SSH dans le Pi

N'oubliez pas d'insérer la carte SD dans le Pi avant de l'allumer. Attendez quelques minutes, puis sur un autre ordinateur Linux/Mac, ouvrez le terminal.

Pour Mac/Linux, dans le terminal, tapez :

```
ssh admin@adresse_IP_de_votre_Pi
```

Pour Windows, vous devrez installer putty pour vous connecter en SSH au Pi. Tapez la même commande que ci-dessus.

La première fois que vous le faites, ou chaque fois que vous changez le système d'exploitation du Pi en changeant la carte SD, vous pouvez obtenir cette erreur ou non...

![image](assets/15.png)

La façon de la résoudre est de vous rendre à l'endroit où se trouve le fichier "known_hosts" (cela vous est indiqué dans le message d'erreur) et de le supprimer. La commande est "rm known_hosts".

Ensuite, répétez la commande ssh pour vous connecter. Cela se produira...

![image](assets/16.png)

Tapez "yes" (en toutes lettres) pour continuer.

Si vous réussissez, on vous demandera un mot de passe. Ce n'est pas pour votre ordinateur, mais pour le raspiblitz. Le mot de passe générique est "raspiblitz" et vous le changerez plus tard. La fenêtre du terminal deviendra bleue et vous aurez des options de menu comme les anciens menus DOS. Naviguez avec les touches fléchées ou la souris.

![image](assets/17.png)

Suivez les invites, définissez vos mots de passe, puis il détectera votre disque dur et vous proposera de le formater si nécessaire.

Ensuite, on vous demandera si vous souhaitez copier les données de la blockchain à partir d'une autre source ou les télécharger à nouveau. La copie est un processus d'apprentissage et les instructions sont assez bonnes, et bonnes à garder à portée de main...

![image](assets/18.png)

La façon simple mais plus lente est de télécharger toute la chaîne à partir de zéro...

![image](assets/19.png)

Beaucoup de texte défilera à l'écran du terminal. Vous pourriez le confondre avec le processus de téléchargement de la blockchain, mais il me semble que cela génère une clé privée pour la communication.

Ensuite, les options Lightning apparaissent.

![image](assets/20.png)

Créez un nouveau mot de passe pour verrouiller votre portefeuille Lightning, puis un nouveau portefeuille sera créé et vous recevrez 24 mots à noter...

![image](assets/21.png)
Assurez-vous de le noter et de le garder en sécurité. J'ai entendu parler d'une personne qui ne l'a pas fait parce qu'il ne prévoyait pas d'utiliser Lightning, mais qui a décidé un an plus tard de l'utiliser et d'ouvrir des canaux. Puis, se rendant compte que ses mots n'étaient pas sauvegardés, et je me souviens qu'il n'était pas possible d'extraire à nouveau les mots du dispositif, il a dû fermer tous ses canaux et recommencer. Il s'en est sorti, mais d'autres pourraient ne pas être aussi chanceux.
Suite à cela, quelques minutes de texte défilent dans la fenêtre du terminal. Ensuite...

![image](assets/22.png)

Vous serez déconnecté de la session ssh. Connectez-vous à nouveau, cette fois avec votre nouveau mot de passe, mot de passe A. Une fois connecté, on vous demandera le mot de passe C pour déverrouiller votre portefeuille Lightning.

Maintenant, nous attendons. Rendez-vous dans 2 semaines. Vous pouvez fermer le terminal, cela n'affecte pas le Pi, c'est juste une fenêtre de communication.

![image](assets/23.png)

Si, pour une raison quelconque, vous souhaitez éteindre le Pi avant que la blockchain ait fini de se télécharger, c'est possible tant que vous le faites correctement. La blockchain continuera de se télécharger là où elle s'était arrêtée une fois que vous vous reconnecterez.

Appuyez sur CTRL+c pour quitter l'écran bleu. Vous accéderez au terminal Linux du Pi. Ici, vous pouvez taper "menu" pour charger l'écran suivant, et à partir de là, vous pouvez éteindre le Pi.

![image](assets/24.png)

FIN du guide

> Le guide suivant a été offert par Parman (https://twitter.com/parman_the)
> vous pouvez lui faire un don ici : dandysack84@walletofsatoshi.com Source originale : https://armantheparman.com/raspiblitz/

Maintenant, votre nœud est prêt à fonctionner. Si vous avez encore besoin d'aide pour naviguer dans d'autres options, consultez le github pour plus de tutoriels et de guides https://github.com/raspiblitz/raspiblitz#feature-documentation
