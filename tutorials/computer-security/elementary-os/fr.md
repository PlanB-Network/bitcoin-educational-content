---
name: Elementary OS
description: Le remplaçant idéal pour Windows et MacOS
---

![cover](assets/cover.webp)

Elementary OS est un système d’exploitation basé sur Ubuntu, conçu pour être simple, rapide et stable dans de nombreux usages quotidiens. Il représente une alternative Linux équilibrée à MacOS et Windows. Son interface graphique fluide, intuitive et épurée rend la prise en main facile, même pour les débutants. Il met également l’accent sur l’ergonomie, la sécurité et la performance.

https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

## Pourquoi choisir Elementary OS

- **Simplicité et facilité d’utilisation** : L’interface graphique d’Elementary OS est à mi-chemin entre celles de MacOs et Windows. Cette familiarité facilite son adoption, même par des utilisateurs peu expérimentés.

- **Sécurité** : Comme la majorité des distributions Linux, Elementary OS bénéficie d’un haut niveau de sécurité. Les mises à jour régulières, la gestion des droits et l’absence de virus courants en font un système fiable.

- **Rapidité** : Elementary OS est une distribution légère. Elle nécessite peu de ressources, ce qui la rend rapide et adaptée aux ordinateurs avec des configurations modestes.

- **Gratuité** : Le système est entièrement gratuit. Cependant, lors du téléchargement, vous pouvez faire un don pour soutenir les développeurs.

- **Communauté active** : La communauté autour d’Elementary OS est diversifiée et réactive. En cas de difficulté, vous pouvez facilement trouver de l’aide sur les forums ou réseaux sociaux.

## Installation et Configuration 
### Prérequis Matériels

Avant de commencer l’installation, assurez-vous de disposer du matériel suivant :

- Une **clé USB** d’au moins 12 Go
- Une **mémoire RAM** de 4 Go minimum
- Un **disque dur de 20 Go** ou plus pour un usage confortable

## Téléchargement de l’image ISO

Accédez au site officiel du système d'exploitation [elementary](https://elementary.io/) puis choisissez un montant à verser pour soutenir le projet. Cette étape est facultative.
Si vous souhaitez télécharger l’ISO gratuitement, entrez 0 dans le champ **« Autre »** et lancez le téléchargement de l’image ISO du système.

![0_01](assets/fr/01.webp)

## Création d’une clé USB bootable

Après avoir téléchargé l’image ISO, il est nécessaire de la rendre amorçable sur une clé USB pour procéder à l’installation.

Téléchargez un logiciel tel que [Balena Etcher](https://etcher.balena.io/) ou un outil similaire puis lancez le logiciel.
Sélectionnez l’image ISO d’**Elementary OS** précédemment téléchargée et définissez votre clé USB comme cible.

Cliquez sur le bouton **flash** pour lancer le processus et patientez jusqu’à la fin du processus avant de retirer la clé USB.

![0_02](assets/fr/02.webp)

## Démarrage sur la clé et accès au BIOS

Éteignez l’ordinateur sur lequel vous souhaitez installer Elementary OS puis branchez la clé USB.
Au démarrage de votre ordinateur accédez au BIOS (`ESC`, `F9` ou `F11` selon les marques) et sélectionnez ensuite la clé USB comme périphérique de démarrage puis appuyez sur la touche `Entrée` pour lancer l’amorçage.

## Installation de Elementary OS

L’installation commence automatiquement si la clé USB est correctement configurée.

### Choix de la langue

Sélectionnez la langue dans laquelle vous souhaitez installer le système. Vous pouvez également choisir une variante régionale.

![0_03](assets/fr/03.webp)

![0_04](assets/fr/04.webp)

### Disposition du clavier

Choisissez la disposition correspondante à votre clavier. Un champ est prévu pour vérifier que les touches produisent les bons caractères.

![0_05](assets/fr/05.webp)

![0_06](assets/fr/06.webp)

### Mode d’essai

Elementary OS vous propose de tester le système avant de procéder à l’installation. Ce mode vous permet d’explorer l’interface sans rien modifier sur votre disque dur.

### Lancement de l’installation

- Cliquez sur **« Erase disk and install »** pour une installation directe sur l’ensemble du disque.
- Cliquez sur **« Custom install »** si vous souhaitez gérer manuellement les partitions.

![0_07](assets/fr/07.webp)

### Choix du disque

Sélectionnez le disque sur lequel Elementary OS doit être installé, puis cliquez sur le bouton continuer.

![0_08](assets/fr/08.webp)

### Chiffrement du disque

Une option permet de chiffrer le disque pour **sécuriser vos données**. Il vous faudra définir un mot de passe robuste pour activer cette protection. Néanmoins elle est optionnelle.

![0_09](assets/fr/09.webp)

![0_10](assets/fr/10.webp)

### Lancement de l’installation

Avant de lancer l'installation vous pouvez autoriser l’installation automatique de pilotes matériels additionnels, selon la compatibilité de votre machine.

- Cliquez sur « Erase and install » pour commencer l’installation.
- Patientez jusqu’à la fin du processus.

![0_11](assets/fr/11.webp)

![0_12](assets/fr/12.webp)

### Redémarrage 

 Une fois terminé, cliquez sur le bouton **entré** pour redémarrer puis retirez la clé USB au moment opportun, afin d’éviter de relancer l’installation.

![0_13](assets/fr/13.webp)

## Configuration après installation

Après le redémarrage, quelques étapes supplémentaires sont nécessaires.

![0_14](assets/fr/14.webp)

### Choix de la langue

Confirmez ou modifiez la langue du système à l’ouverture de session.

![0_15](assets/fr/15.webp)

### Disposition du clavier

Assurez-vous que la disposition du clavier est bien celle souhaitée.

![0_16](assets/fr/05.webp)

### Création d’un compte utilisateur

Associez un compte utilisateur à votre système d'exploitation en définissant un nom d'utilisateur puis en sécurisant l'accès à vos données avec un mot de passe alphanumérique d'au moins 20 caractères et symboles.

![0_17](assets/fr/17.webp)

### Première connexion

Lors de votre première connexion, Elementary OS vous propose de personnaliser votre environnement via quelques paramètres de base.

![0_18](assets/fr/18.webp)

![0_19](assets/fr/19.webp)

## Mise à jour du système

Avant toute utilisation prolongée, il est important de mettre à jour le système pour bénéficier des derniers correctifs.
### Option 1 : Mise à jour via l’interface graphique

Entrez dans l'**AppCenter** et cliquez sur l’icône de mise à jour en haut à droite. Attendez que les mises à jour soient listées puis cliquez sur **« Tout mettre à jour »** pour lancer l’installation.

![0_20](assets/fr/20.webp)

![0_21](assets/fr/21.webp)

### Option 2 : Mise à jour via le terminal

Vous pouvez aussi effectuer la mise à jour en ligne de commande via votre terminal : une option recommandée pour sa précision.

```shell
sudo apt update
```

```shell
sudo apt full-upgrade
```

Pour vos premières mises à jour, le système d'exploitation requiert votre mot de passe utilisateur puis une confirmation afin de mettre à jour les paquets des logiciels, ce même dans le noyau de Elementary. 

## Configuration de l’environnement de travail

Elementary OS n’inclut que les outils essentiels. Pour adapter votre environnement à vos besoins, en particulier si vous souhaitez faire du développement, il est conseillé d’installer des outils supplémentaires.

- Vous pouvez ajouter des dépendances utiles avec la commande suivante (à adapter selon votre usage) :  

```shell
sudo apt update && sudo apt install -y git python3 python3-pip build-essential wget curl zsh make snapd && sudo snap install code --classic
```

Cette commande permet d'installer **Git**, **Python 3**, **pip**, **outils de compilation**, **wget**, **curl**, **zsh**, **make**, **snapd** ainsi que **vscode** pour préparer un environnement basique pour le développement. 

Elementary OS est maintenant opérationnel sur votre machine. Sa philosophie orientée vers la simplicité, la légèreté et l’élégance en fait un excellent choix, aussi bien pour une utilisation personnelle que professionnelle. Vous disposez d’un système stable, fluide et épuré, prêt à être personnalisé selon vos préférences. Que ce soit pour le développement, la bureautique ou la navigation quotidienne, tout est en place pour bâtir un environnement de travail efficace, intuitif et agréable. Découvrez également le tutoriel sur Fedora, une distribution Linux toute aussi simple, robuste, modulable.

https://planb.academy/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0