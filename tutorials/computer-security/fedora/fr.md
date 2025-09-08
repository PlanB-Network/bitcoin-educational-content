---
name: Fedora
description: La distribution Linux qui vous fournit un espace de travail libre, complet et sécurisé.
---


![cover](assets/cover.webp)

  

Fedora est un système d’exploitation libre et gratuit basé sur Linux initié en 2003, développé par la communauté **Fedora Project** et soutenu par **Red Hat Linux**. Il est reconnu pour sa stabilité, ses bonnes performances et sa facilité de prise en main, ce qui en fait un excellent choix, aussi bien pour les débutants que pour les utilisateurs plus avancés. Ce système fonctionne sur la plupart des architectures de processeurs modernes, ce qui permet de l’installer facilement sur quasiment tous les ordinateurs. Fedora est aussi disponible en plusieurs éditions préconfigurées, appelées "Fedora Spins" ou "Fedora Editions", conçues pour des besoins spécifiques (Jeux vidéos, Astronomies, Développement...).

## L'architecture de Fedora Linux

Comme vous l'avez lu plus haut, Fedora est un système d'exploitation libre qui se base sur le noyau Linux. Le noyau Linux est la partie du système d'exploitation qui communique avec le matériel de l'ordinateur et qui gère les ressources du système telles que la mémoire et la puissance de traitement.

Fedora Linux comprend une variété d'outils logiciels et d'applications qui sont nécessaires pour faire fonctionner le système d'exploitation au-dessus du noyau Linux. Fedora possède une architecture modulaire qui lui permet d'être principalement constitué d'une collection de composantes individuelles qui peuvent être facilement ajoutées, supprimées ou remplacées au besoin. Cela vous permet de façonner le système d'exploitation en utilisant que les ressources dont vous avez besoin.

Fedora comprend également un environnement de bureau, qui est l'interface par laquelle les utilisateurs effectuent des tâches et accèdent à des applications. L'environnement de bureau par défaut de Fedora est GNOME, un environnement de bureau convivial, facile à utiliser et hautement personnalisable.

## Pourquoi choisir Fedora ?

Parmi la multitude de distribution Linux disponible, Fedora se démarque notamment par :

- **Sa modularité** : Compatible avec différentes architectures de processeur, Fedora peut s’installer sur la majorité des ordinateurs, même peu puissants, s'adaptant parfaitement à vos besoins.

- **Une interface simple et intuitive** : Fedora combine une interface graphique moderne avec une interface en ligne de commande puissante, rendant son utilisation agréable pour tous les profils.

- **Stabilité du noyau** : Basé sur Red Hat, Fedora est réputée pour la fiabilité de ses mises à jour, notamment celles du noyau, qui se déroulent sans bugs majeurs grâce aux contributions libres d'une large communauté.

- **Installation rapide et facile** : avec une image d’environ 3 Go, l’installation est rapide et accessible, même sur des machines avec des ressources limitées.

## Les éditions de Fedora

Selon votre profil et votre utilisation, Fedora vous propose des éditions qui correspondent à vos besoins. Vous retrouverez principalement :

- **Fedora Workstation** : Idéale pour une utilisation personnelle et/ou professionnelle sur vos ordinateurs, cette édition s'installe avec des utilitaires génériques tels que les navigateurs, une suite bureautique (Éditeurs de textes), et des logiciels de lecture de médias.

- **Fedora Server** : Cette édition est dédiée à la gestion de serveurs. Fedora Serveur inclut des outils variés pour vous permettre de déployer et de gérer des serveurs à votre propre échelle.

- **Fedora CoreOS** : Vous souhaitez facilement faire tourner et déployer des applications cloud ? Fedora CoreOS est l'édition qui vous met à disposition des outils pour créer et gérer des images avec Docker et Kubernets par exemple.

Dans ce tutoriel, nous nous chargerons de prendre en main l'édition Fedora Workstation. Toutefois, les processus détaillés ci-dessous restent similairement les mêmes pour les autres éditions.

## Installer et Configurer Fedora Workstation

Installer Fedora Workstation vous demandera la configuration matérielle suivante :
- Une clé USB d’au moins **8 Go** pour booter le système d'exploitation.
- Au minimum **40 Go d’espace libre** sur le disque dur de votre ordinateur.
- **4 Go de RAM** pour une expérience fluide.

### Télécharger Fedora Workstation

Vous pouvez télécharger l'édition [Fedora Workstation](https://fedoraproject.org/fr/workstation/download) sur le site officiel du projet Fedora. Sélectionnez ensuite la version correspondante à l'architecture de votre processeur (32 bits - 64 bits) puis cliquez sur l'icône **Télécharger**.

![download](assets/fr/01.webp)

![telecharger](assets/fr/02.webp)
### Créer une clé USB bootable

Pour installer Fedora, il est nécessaire de créer une clé USB bootable à l’aide d’un logiciel comme [Balena Etcher](https://etcher.balena.io/).

![flashOs](assets/fr/03.webp)

![flash](assets/fr/04.webp)

Une fois l'installation de Balena Etcher finie, ouvrez l'application puis sélectionnez l'image ISO de Fedora Workspace téléchargée. Sélectionnez votre clé USB comme support de destination et cliquez sur le bouton **Flash** pour lancer la création de la clé bootable.

![boot](assets/fr/05.webp)
### Faire une installation de Fedora

A la fin de l'opération de boot de votre clé USB, éteignez votre ordinateur.
Allumez votre ordinateur puis accédez au BIOS lors du démarrage en cliquant sur la touche `F2`,  `F12` ou `ESC` selon votre ordinateur.

Dans les options de démarrage, sélectionnez votre clé USB comme périphérique de démarrage principal. En validant ce choix, votre ordinateur redémarrera et lancera automatiquement **l’installateur Fedora** présent sur la clé USB.

Une fois votre ordinateur démarré sur la clé USB, l’**écran de GRUB** s’affiche.  

À cette étape, vous avez les options suivante :
- **Tester le support** : Cette option permet de vérifier l’intégrité de la clé USB et s’assurer que toutes les dépendances requises pour une installation correcte sont réunies. Il s'agit d'une étape facultative, mais recommandée si vous avez un doute sur la clé USB.

![install](assets/fr/06.webp)

![testing](assets/fr/07.webp)

- **Démarrer Fedora** : Cela lance Fedora en mode "live", sans installation.

Sur le bureau de Fedora (mode live), cliquez sur **Installer Fedora** (ou Installer sur le disque dur) pour démarrer le processus d’installation. Vous pouvez choisir d'installer plus tard et de tester Fedora sans avoir besoin de l'installer.

![install-live](assets/fr/08.webp)

La première étape consiste à sélectionner la **langue d’installation** de Fedora ainsi que la **disposition du clavier**

![language](assets/fr/10.webp)

- Sélection du disque d’installation :

Choisissez le disque dur sur lequel vous souhaitez installer Fedora.  

Si le disque est vide, Fedora utilisera automatiquement tout l’espace disponible. Autrement, vous pourrez personnaliser la répartition (partitionnement manuel ou automatique).

![disk](assets/fr/11.webp)

- Le chiffrement :

À cette étape, Fedora propose de chiffrer votre disque afin d’ajouter une couche de sécurité supplémentaire. Cela garantit que vos données ne seront lisibles que par votre système Fedora.

![chiffrement](assets/fr/12.webp)

Avant de lancer l’installation, Fedora vous affiche un récapitulatif de vos choix. Confirmez puis cliquez sur le bouton installer pour démarrer l'installation de Fedora.

![resume](assets/fr/13.webp)

Pendant l’installation, Fedora copie les fichiers et configure le système. Une fois terminé, l’ordinateur redémarre automatiquement.

![installation](assets/fr/14.webp)

### Configuration de base
À la première utilisation, vous devrez finaliser quelques réglages :
- Changez la langue du système si nécessaire.

![language](assets/fr/15.webp)

- Sélectionnez une disposition de clavier adaptée à vos préférences.

![keyboard](assets/fr/16.webp)

- Choisissez le fuseau horaire en tapant le nom de votre ville dans la barre de recherche, puis cliquez sur la suggestion correspondante.

![timezone](assets/fr/17.webp)

 - Activez ou non l’accès à votre position pour les applications qui en ont besoin, ainsi que l’envoi automatique des rapports de bugs.
 
![location](assets/fr/18.webp)

- Décidez si vous souhaitez activer les dépôts de logiciels tiers.  

![logs](assets/fr/19.webp)

- Saisissez votre nom complet et définissez un nom d’utilisateur pour votre compte.

![name](assets/fr/20.webp)

- Créez un mot de passe sécurisé pour votre session : le plus long possible (minimum 20 caractères), le plus aléatoire possible et avec une diversité de caractères (minuscules, majuscules, chiffres et symboles). Pensez à faire une sauvegarde de votre mot de passe.

![mdp](assets/fr/21.webp)

 Une fois toutes ces étapes terminées, lancez Fedora et commencez à l’utiliser immédiatement, sans redémarrage supplémentaire.

![welcome](assets/fr/22.webp)

![start](assets/fr/23.webp)

Une fois votre installation achevée, vous pouvez consulter votre interface d'accueil avec quelques utilitaires préinstallés.

![install-now](assets/fr/09.webp)

## Découvrez les tâches de base

### Naviguer sur Internet
Le navigateur par défaut de Fedora est **Firefox**. Il est simple d’utilisation et adapté à la majorité des besoins.
Si vous préférez un autre navigateur, vous pouvez l’installer depuis le **gestionnaire de logiciels** ou via le **terminal**.
### Traitement de texte
Fedora inclut par défaut la suite bureautique **LibreOffice**, qui propose plusieurs outils utiles :
- **Writer** pour le traitement de texte.
- **Calc** pour les feuilles de calcul.
- **Impress** pour créer des présentations.
## Installer des applications
Pour installer de nouvelles applications, vous pouvez utiliser le **gestionnaire de logiciels** de Fedora (nommé _Logiciels_), qui permet une installation facile et visuelle.  Cependant, passer par le **terminal** est souvent plus rapide et plus précis.

Avant d’installer un logiciel, pensez toujours à mettre à jour les **dépôts** pour être sûr d’avoir accès aux dernières versions disponibles.  

Utilisez ensuite la commande suivante pour lancer l’installation de l’application souhaitée :
`sudo dnf install nom_du_logiciel`
## Mise à jour de votre système d’exploitation
Après l’installation, il est important de mettre à jour Fedora pour bénéficier des derniers correctifs de sécurité et des mises à jour logicielles disponibles.
### Option 1 : Via l’interface graphique
- Ouvrez les **paramètres** de Fedora, puis allez dans la section **Système**.
- Cliquez sur **Mise à jour logicielle**.
- Lancez le téléchargement des mises à jour et patientez jusqu’à la fin du processus.

Un **redémarrage** peut être nécessaire une fois les mises à jour installées.
### Option 2 : Via le terminal
- Ouvrez un terminal et commencez par mettre à jour les **dépôts** pour vous assurer de disposer des dernières versions des paquets :

```shell
sudo dnf check-update
```

- Ensuite, lancez la mise à jour de tous les logiciels installés avec la commande suivante :

```shell
sudo dnf upgrade
```

Voilà, votre système Fedora est à jour et prêt à être utilisé pour toutes vos tâches du quotidien. Découvrez notre tutoriel sur Linux Mint, une autre distribution Linux et comment mettre en place un environnement sain et sécurisé pour effectuer vos transactions Bitcoin.

https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5
