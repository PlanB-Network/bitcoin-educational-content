---
name: Zorin OS
description: Guide complet pour installer et utiliser Zorin OS comme alternative moderne à Windows
---

![cover](assets/cover.webp)

## Introduction

Un système d’exploitation (OS) est le logiciel fondamental qui permet à un ordinateur de fonctionner : il gère le matériel, les logiciels, la sécurité et l’interface utilisateur.
Zorin OS est une distribution Linux conçue spécifiquement pour faciliter la transition depuis Windows, tout en offrant les avantages du logiciel libre : sécurité, stabilité, respect de la vie privée et performances.

Basé sur Ubuntu LTS, Zorin OS combine une grande compatibilité logicielle avec une interface familière et personnalisable, ce qui en fait une alternative crédible et accessible à Windows.

## Pourquoi Zorin OS ?

- **Interface familière** : apparence proche de Windows (menu démarrer, barre des tâches)
- **Transition facilitée** : pensée pour les utilisateurs venant de Windows
- **Sécurité renforcée** : architecture Linux, moins exposée aux virus
- **Respect de la vie privée** : aucune collecte intrusive de données
- **Performances optimisées** : fonctionne correctement sur des machines modestes
- **Base Ubuntu LTS** : stabilité, mises à jour régulières et large compatibilité
- **Personnalisation avancée** : via l’outil Zorin Appearance.

## Installation et configuration

### 1. Prérequis

**Matériel nécessaire :**

- Une clé USB d’au moins **8 Go** (12 Go recommandés);
- Un ordinateur avec au moins **25 Go d’espace disque disponible**
- Une connexion Internet (recommandée).

### 2. Téléchargement de Zorin OS

- Rendez-vous sur le site officiel : [https://zorin.com/os](https://zorin.com/os)

![Page de téléchargement Balena Etcher](assets/fr/03.webp)

- Choisissez **Zorin OS Core** (version gratuite recommandée)

![Page de téléchargement Balena Etcher](assets/fr/04.webp)

- Téléchargez l’image ISO

 Zorin OS propose également :

- **Zorin OS Lite** (ordinateurs anciens)
- **Zorin OS Pro** (payant, avec dispositions avancées et support)

## Création d’une clé USB bootable

Vous pouvez utiliser plusieurs outils, par exemple Balena Etcher :

- Téléchargez [Balena Etcher](https://etcher.balena.io/) et installez-le.
- Ouvrez Balena Etcher, puis sélectionnez l'image ISO de Zorin.
- Sélectionnez la clé USB comme support de destination.
- Cliquez sur Flash et attendez la fin du processus.

![Utilisation de Balena Etcher](assets/fr/05.webp)

## Démarrage sur la clé et accès au BIOS

Éteignez l’ordinateur sur lequel vous souhaitez installer Zorin OS puis branchez la clé USB.
Au démarrage de votre ordinateur accédez au BIOS (`ESC`, `F9` ou `F11` selon les marques) et sélectionnez ensuite la clé USB comme périphérique de démarrage puis appuyez sur la touche `Entrée` pour lancer l’amorçage.

- Au démarrage, sélectionnez **Try or Install Zorin OS**.

![capture](assets/fr/08.webp)

- Si vous avez une carte graphique NVIDIA, sélectionnez **Try or Install Zorin OS (modern NVIDIA drivers)**.
- Patientez pendant la vérification des fichiers.

![capture](assets/fr/09.webp)

- Dans l’installeur de Zorin OS, sélectionnez la langue **Français** puis cliquez sur Installer **Zorin OS**.

![capture](assets/fr/10.webp)

- Sélectionnez la disposition du clavier.

![capture](assets/fr/11.webp)

- Cochez les cases **Télécharger les mises à jour pendant l’installation de Zorin OS** et **Installer un logiciel tiers pour le matériel graphique et Wi-Fi et des formats de média supplémentaires**.

![capture](assets/fr/12.webp)

- Pour installer Zorin OS sur le disque entier : sélectionnez **Effacer le disque et installer Zorin OS**.

![capture](assets/fr/14.webp)

Pour installer Zorin OS à côté de Windows (dual-boot) :

- Sélectionnez **Installer Zorin OS à côté de Windows Boot Manager**.

![capture](assets/fr/15.webp)

- Si vous n’avez pas partitionné votre disque, choisissez l’espace disque à allouer à Zorin OS puis cliquez sur **Installer maintenant**.

![capture](assets/fr/16.webp)

- Confirmez par deux fois les changements sur le disque.

![capture](assets/fr/16.webp)

![capture](assets/fr/17.webp)

- Sélectionnez la zone géographique **Paris**.

![capture](assets/fr/18.webp)

- Créez votre compte utilisateur et donnez un nom à votre ordinateur.

![capture](assets/fr/19.webp)

- Patientez pendant l’installation de Zorin OS.

![capture](assets/fr/20.webp)

- Une fois l’installation terminée, cliquez sur **Redémarrer maintenant**.

![capture](assets/fr/21.webp)

- Retirez la clé USB d’installation et appuyez sur Entrée.

![capture](assets/fr/22.webp)

## Découvrir et utiliser Zorin OS

### Premier démarrage

Au démarrage de l’ordinateur, vous arrivez sur GRUB – le gestionnaire de démarrage de Linux. Par défaut, **Zorin OS** est sélectionné ; au bout de 30 secondes, celui-ci démarre automatiquement.

![capture](assets/fr/23.webp)

Si vous avez installé Zorin OS en dual-boot avec Windows, vous pouvez démarrer sur Windows en sélectionnant **Windows Boot Manager**.

Connectez-vous avec votre compte utilisateur :

![capture](assets/fr/24.webp)

Au premier démarrage, l’application **Bienvenue dans Zorin OS** se lance et vous aide à découvrir votre nouveau système d’exploitation.

![capture](assets/fr/25.webp) 

![capture](assets/fr/26.webp)

![capture](assets/fr/27.webp)

![capture](assets/fr/28.webp)

![capture](assets/fr/29.webp)

![capture](assets/fr/30.webp)

![capture](assets/fr/31.webp)

![capture](assets/fr/32.webp)



### Mettre à jour le système

Rapidement, le Gestionnaire de mises à jour s’ouvrira pour vous signaler que des mises à jour sont disponibles. Installez-les en cliquant sur le bouton **Installer maintenant**.

![capture](assets/fr/33.webp)

Vous pouvez vérifier manuellement si des mises à jour sont disponibles dans l’application **Logiciels** > Mises à jour :

![capture](assets/fr/34.webp)

### Personnalisation

La première chose à faire dans Zorin OS est de choisir la **disposition de bureau** avec laquelle vous êtes le plus à l’aise. Vous y trouverez des dispositions ressemblant à celles que l’on trouve sur Windows (et encore plus avec la version Pro).

Pour cela, ouvrez **Zorin Appareance** > **Type** :

![capture](assets/fr/35.webp)  

Ouvrez ensuite les **Paramètres** pour personnaliser votre système :
**Son – Paramètres – Zorin OS**

![capture](assets/fr/36.webp)

**Comptes en ligne – Paramètres – Zorin OS**

![capture](assets/fr/37.webp)

### Applications

Pour installer des applications, vous avez plusieurs possibilités :

- **Logiciels**, le magasin d’applications de Zorin OS. Les applications proviennent de plusieurs sources : apt, Flatpak et Snap.  

![capture](assets/fr/38.webp)

![capture](assets/fr/39.webp)

- **apt** install (ligne de commande) :
  
```bash
sudo apt install gparted
```

![capture](assets/fr/40.webp)

Pour plus d’informations sur l’installation d’applications dans Zorin OS, consultez cette page : [Install Apps (zorin.com)](https://zorin.com/help/install-apps/).

### Applications Windows

Pour installer des applications Windows, commencez par installer le paquet **zorin-windows-app-support** via le Terminal :

```bash
sudo apt install zorin-windows-app-support
```

Pour connaître les applications Windows compatibles et leur niveau de compatibilité, consultez la page [Wine Application Database](https://appdb.winehq.org/). Vous y trouverez les badges suivants, qui correspondent au niveau de compatibilité (du meilleur au pire) : Platinum, Gold, Silver, Bronze et Garbage.

Pour installer une application .exe ou .msi Windows, vous avez deux possibilités :

- Ouvrez **PlayOnLinux** et cliquez sur le bouton **Install** pour parcourir les applications et jeux compatibles.  

![capture](assets/fr/41.webp)

- Double-cliquez sur le **fichier .exe ou .msi** de l’application et laissez-vous guider par le programme d’installation.  
  
![capture](assets/fr/42.webp)

![capture](assets/fr/43.webp)

## Conclusion et ressources complémentaires

Zorin OS constitue une alternative solide et accessible à Windows, combinant simplicité, sécurité et respect de la vie privée.

Il permet une transition en douceur vers Linux, sans sacrifier le confort ni la productivité.

Pour aller plus loin dans la protection de la vie numérique, il est recommandé d’utiliser des services respectueux de la vie privée, notamment pour la communication chiffrée :

https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
