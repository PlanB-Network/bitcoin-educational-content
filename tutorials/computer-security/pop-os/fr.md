---
name: Pop!_OS
description: Guide pour l'installation de Pop!_OS, une distribution Linux
---

![cover](assets/cover.webp)

## Introduction

Pop!OS est un système d’exploitation basé sur Linux, développé par **System76**, un constructeur américain spécialisé dans les machines dédiées aux développeurs, aux créateurs et aux utilisateurs avancés.

Conçu pour offrir un environnement moderne, stable et performant, Pop!OS se distingue par une expérience simple, des outils puissants et une forte orientation vers la productivité.

### Qui est System76 ?

System76 est une entreprise américaine fondée en 2005 et basée à Denver, spécialisée dans la fabrication d’ordinateurs portables, de PC de bureau et de serveurs conçus spécialement pour Linux.

Contrairement aux constructeurs traditionnels, System76 développe des machines pensées pour être ouvertes, réparables et tournées vers la liberté logicielle.

System76 ne se contente pas de fabriquer des ordinateurs.

L’entreprise développe également :
- **Pop!OS**, son propre système d’exploitation basé sur Linux ;
- **COSMIC**, l’environnement de bureau moderne et performant utilisé par Pop!OS ;
- **Open Firmware**, un firmware open-source basé sur Coreboot ;
- des outils destinés aux développeurs et aux créateurs.

L’objectif est d’offrir une intégration matérielle et logicielle de haute qualité, comparable à l’écosystème Apple, mais totalement ouverte et centrée sur Linux.

## Un système moderne, stable et accessible

Pop!OS reprend les fondations d’Ubuntu, ce qui lui confère une excellente stabilité, une compatibilité matérielle large et un accès à un écosystème logiciel immense.  
Il fournit une interface élégante, le bureau COSMIC, pensé pour être fluide, intuitif et personnalisable, même pour les nouveaux utilisateurs.

## Un choix idéal pour les développeurs, créateurs et utilisateurs exigeants

Pop!OS est particulièrement apprécié par :

- les développeurs (outils préinstallés, gestion avancée du tiling),
- les utilisateurs avec cartes graphiques Nvidia ou AMD,
- les étudiants et professionnels recherchant un système fiable,
- les personnes venant de Windows souhaitant une transition simple.

Il inclut une gestion automatique des fenêtres en mosaïque (“tiling”), un centre de logiciels clair, ainsi que des outils de productivité intégrés qui facilitent l’utilisation quotidienne.

## Points forts de Pop!OS

- **Performance optimisée** grâce à des mises à jour régulières.
- **Deux ISO disponibles** : version standard et version optimisée Nvidia.
- **Sécurité renforcée** (chiffrement LUKS disponible dès l’installation).
- **Interface COSMIC** ergonomique et moderne.
- **Grande compatibilité** avec les logiciels Ubuntu et Flatpak.

## Télécharger POP!OS de manière sûre

### 1. Prérequis

Avant de télécharger et d’installer POP!OS, quelques éléments sont nécessaires pour préparer correctement l’environnement d’installation.

### Matériel requis

- **Un ordinateur compatible** : processeur Intel ou AMD, GPU Intel / AMD / Nvidia.
- **Au moins 4 Go de RAM** (8 Go recommandés pour un usage confortable).
- **20 Go d’espace libre minimum** (40 Go ou plus recommandés).
- **Une clé USB de 4 Go minimum** pour créer le support d’installation.

### Connexion Internet

Une connexion stable est utile pour :

- télécharger l’image ISO,
- installer les mises à jour après l’installation.

Pop!OS peut fonctionner sans connexion, mais l’installation est plus fluide avec Internet.

### Sauvegarde des données

Si Pop!OS doit remplacer ou coexister avec un autre système (Windows, Ubuntu, etc.), il est conseillé de sauvegarder les fichiers importants avant de continuer.

### Vérifier la présence d’un GPU Nvidia (si applicable)

Pour les ordinateurs équipés d’une carte graphique Nvidia, il sera nécessaire de télécharger l’image ISO spéciale qui inclut les pilotes Nvidia.  
Cette vérification se fait simplement :

- en consultant les caractéristiques du PC,
- ou en regardant le modèle de carte graphique dans les paramètres système.

### Télécharger depuis le site officiel

L’image ISO de Pop!OS doit être téléchargée directement depuis la page officielle de System76 : [system76.com/pop](https://system76.com/pop/).

Cette page propose toujours la version la plus récente et la plus adaptée à votre matériel.

![capture](assets/fr/03.webp)

### Choisir la version : Standard ou Nvidia, ou Raspberry Pi (ARM64)

Pop!OS est disponible en trois variantes :

### Version Standard

Recommandée pour les ordinateurs utilisant :

- un processeur Intel ou AMD ;
- un GPU intégré Intel ou AMD ;
- une carte graphique AMD Radeon.

![Utilisation de Balena Etcher](assets/fr/04.webp)

### Version Nvidia

Recommandée pour les ordinateurs équipés d’une carte graphique Nvidia.  
Cette image inclut déjà les pilotes Nvidia, ce qui facilite l’installation et réduit les problèmes graphiques.

![Utilisation de Balena Etcher](assets/fr/05.webp)

### Version Raspberry Pi (ARM64)

Pour Raspberry Pi 4 et 400 (processeur ARM).  
Adaptée à l’architecture ARM, c’est une version spécifique pour ces mini-ordinateurs.

![Utilisation de Balena Etcher](assets/fr/06.webp)

## Créer une clé USB bootable

Vous pouvez utiliser plusieurs outils, par exemple Balena Etcher :

- Téléchargez [Balena Etcher](https://etcher.balena.io/) et installez-le.

![Page de téléchargement Balena Etcher](assets/fr/07.webp)

![Installation de Balena Etcher](assets/fr/08.webp)

- Ouvrez Balena Etcher, puis sélectionnez l'image ISO de Pop!OS.
- Sélectionnez la clé USB comme support de destination.
- Cliquez sur Flash et attendez la fin du processus.

![Utilisation de Balena Etcher](assets/fr/09.webp)

## Installer et sécuriser Pop!OS

### Démarrage sur la clé USB

- Éteignez l'ordinateur.
- Branchez la clé USB (contenant Pop!OS).
- Allumez l'ordinateur. Sur les PC récents, le système devrait reconnaître automatiquement la clé USB de démarrage. Si ce n'est pas le cas, redémarrez en maintenant la touche d'accès au BIOS/UEFI (généralement F2, F12 ou Delete, selon la marque).
  - Dans le menu du BIOS/UEFI, sélectionnez votre clé USB comme périphérique de démarrage (Boot).
  - Sauvegardez (Save) et redémarrez.

### Lancement de l'installation

Une fois votre clé USB bootable sélectionnée comme périphérique de démarrage, votre ordinateur démarrera dans un environnement Pop!OS Live.

 Sélectionnez votre langue.

![Capture](assets/fr/10.webp)

 Sélectionnez un lieu.

![Capture](assets/fr/11.webp)

 Sélectionnez une langue de saisie au clavier.

![Capture](assets/fr/12.webp)

 Sélectionnez une disposition de clavier.

![Capture](assets/fr/13.webp)

Choisissez l'option `Clean Install` pour une installation standard. C'est la meilleure option pour les nouveaux utilisateurs de Linux, mais sachez que cela effacera tout le contenu du lecteur cible. Alternativement, vous pouvez sélectionner `Try Demo Mode` pour continuer à tester Pop!OS dans l'environnement live.

![Capture](assets/fr/14.webp)

Sélectionnez `Custom (Advanced)` pour accéder à GParted. Cet outil permet de configurer des fonctionnalités avancées telles que le double démarrage, la création d'une partition `/home` distincte, ou le placement de la partition `/tmp` sur un lecteur différent.

Cliquez sur `Erase and Install` pour installer Pop!OS sur le disque sélectionné.

![Capture](assets/fr/15.webp)

### Configuration du compte utilisateur

La section suivante du programme d'installation vous guidera dans la création d'un compte utilisateur afin que vous puissiez vous connecter à votre nouveau  système d'exploitation.

Fournissez un nom complet (cela peut inclure n'importe quel texte de votre choix, majuscule ou minuscule), ainsi qu'un nom d'utilisateur (qui doit être en minuscules) :

![Capture](assets/fr/16.webp)

Une fois le compte créé, vous serez invité à définir un nouveau mot de passe.

![Capture](assets/fr/17.webp)

### Cryptage complet du disque

Le cryptage du disque système n'est pas nécessaire, mais il garantit la sécurité des données utilisateur dans le cas où quelqu'un obtiendrait un accès physique non autorisé à l'appareil.

Le lecteur peut être chiffré à l'aide de votre mot de passe de connexion en cochant `Encryption password is the same as user account password`. Vous pouvez également décocher cette case et sélectionner `Set Password` en bas. Sélectionnez `Don't Encrypt` pour ignorer le processus de chiffrement du disque.

![Capture](assets/fr/18.webp)

Si vous avez choisi le bouton `Set Password`, vous verrez une invite supplémentaire pour définir votre mot de passe de chiffrement.

Passez à l’étape suivante dans le programme d’installation. Pop!OS va maintenant commencer l'installation sur le disque.

![Capture](assets/fr/19.webp)

Une fois l’installation terminée, redémarrez votre ordinateur et connectez-vous pour terminer le processus de configuration du compte utilisateur.

Si vous avez modifié l'ordre de démarrage pour prioriser votre clé USB Live au démarrage, éteignez complètement l'ordinateur et retirez la clé USB d'installation. Si vous êtes en dual-boot (double démarrage), appuyez sur les touches appropriées pour accéder à la configuration et sélectionnez le lecteur contenant l'installation de Pop!OS.

![Capture](assets/fr/20.webp)

### Graphiques NVIDIA

Si vous avez installé à partir de l'ISO Intel/AMD et que votre système dispose d'une carte graphique NVIDIA discrète ou si vous en avez ajouté une ultérieurement, vous devrez installer manuellement les pilotes de votre carte pour obtenir des performances optimales. Exécutez la commande suivante dans un terminal de commande pour installer le pilote :

```bash
sudo apt install system76-driver-nvidia
```

Vous pouvez également installer les pilotes graphiques NVIDIA depuis le Pop!_Shop.

![Capture](assets/fr/20.webp)

## Installation des outils essentiels

Pop!OS propose une large gamme de logiciels via sa boutique Pop!Shop, mais beaucoup d’outils essentiels sont également installables via le terminal avec `apt` ou `flatpak`. Voici comment installer les outils clés pour un environnement de travail complet.

### Installation via le terminal

| Outil                        | Description                                | Commande d’installation                         |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox                      | Navigateur web libre et populaire          | `sudo apt install firefox`                      |
| Brave                        | Navigateur web axé sur la confidentialité  | Installation via Pop!_Shop ou site officiel     |
| Visual Studio Code (VS Code) | Éditeur de code puissant pour développeurs | `flatpak install flathub com.visualstudio.code` |
| Git                          | Gestionnaire de versions                   | `sudo apt install git`                          |
| Flatpak                      | Gestionnaire de paquets alternatif         | `sudo apt install flatpak`                      |
| VLC                          | Lecteur multimédia polyvalent              | `sudo apt install vlc`                          |
| GNOME Terminal               | Terminal par défaut                        | Préinstallé sur Pop!OS                          |
| Curl                         | Outil de transfert de données en ligne     | `sudo apt install curl`                         |
| Wget                         | Téléchargement de fichiers via HTTP/FTP    | `sudo apt install wget`                         |
| Docker                       | Conteneurisation d’applications            | Installation via script officiel ou `apt`       |
| Node.js                      | Environnement JavaScript côté serveur      | Installation via `apt` ou NodeSource            |
| Python3                      | Langage de programmation                   | `sudo apt install python3 python3-pip`          |
| GIMP                         | Éditeur d’image avancé                     | `sudo apt install gimp`                         |
| Thunderbird                  | Client mail                                | `sudo apt install thunderbird`                  |
| Transmission                 | Client BitTorrent léger                    | `sudo apt install transmission-gtk`             |
| Htop                         | Moniteur de système interactif             | `sudo apt install htop`                         |

### Installation via Pop! Shop (interface graphique)

- Ouvrez **Pop!_Shop** depuis le menu principal.
- Utilisez la barre de recherche pour trouver les applications souhaitées (par exemple, “Brave”).
- Cliquez sur **Installer** pour chaque application.
- Pop!_Shop gère automatiquement les dépendances et mises à jour.

## Mise à jour du système

### Option 1 : Via l’interface graphique (GUI)

Pop!OS propose un gestionnaire de mises à jour graphique simple et intuitif.

1. Cliquez sur le **menu principal** (icône en bas à gauche).
2. Ouvrez **“Pop!_Shop”**.
3. Dans la Pop!_Shop, cliquez sur l’onglet **“Updates”** ou **“Mises à jour”**.
4. Le système va vérifier automatiquement les mises à jour disponibles.
5. Cliquez sur **“Mettre à jour tout”** pour lancer l’installation des mises à jour.
6. Entrez votre mot de passe si demandé.
7. Laissez le processus se terminer, puis redémarrez si nécessaire.

### Option 2 : Via le terminal

Ouvrez un terminal et tapez :

```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```

### Gestion des utilisateurs

Il est recommandé d’utiliser un compte utilisateur standard avec droits sudo pour les opérations quotidiennes.

Pour créer un nouvel utilisateur :

```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```

Déconnectez-vous, puis reconnectez-vous avec ce nouvel utilisateur.

### Gestion des pilotes graphiques

- Pour les cartes Nvidia, vérifiez que les pilotes propriétaires sont bien installés :

```bash
sudo apt install system76-driver-nvidia
```

- Pour AMD/Intel, les pilotes sont généralement inclus par défaut.

### Activer le pare-feu (UFW)

Pop!OS ne bloque pas le trafic réseau par défaut. Activez UFW pour renforcer la sécurité :

```bash
sudo ufw enable && sudo ufw status verbose
```

### Configurer les mises à jour automatiques

Pour garder le système à jour sans intervention manuelle :

```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```

### Personnaliser l’apparence et le comportement

- Ouvrez les **Paramètres système** → **Apparence** pour choisir un thème clair ou sombre.
- Configurez les coins actifs, animations et extensions via le gestionnaire COSMIC.
- Ajustez la disposition du bureau pour optimiser votre workflow.

### Configurer la sauvegarde automatique

Pop!OS intègre des outils comme Deja Dup pour la sauvegarde :

- Lancez **Sauvegardes** depuis le menu.
- Choisissez un disque externe ou un emplacement réseau.
- Programmez des sauvegardes régulières.

### Installer des extensions GNOME/COSMIC utiles

Voici quelques extensions recommandées pour améliorer l’expérience utilisateur :

- **Dash to Dock** : barre d’applications toujours visible.
- **GSConnect** : synchronisation avec Android.
- **Clipboard Indicator** : gestion du presse-papiers avancée.

Installez-les via :

```bash
sudo apt install gnome-shell-extensions
```

Puis activez-les dans les paramètres.

### Optimiser la gestion de la mémoire et du swap

Vérifiez l’état de votre swap :

```bash
swapon --show
```

Si nécessaire, augmentez la taille du swap ou configurez un fichier swap :

```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

Ajoutez-le au fichier `/etc/fstab` pour un montage automatique.

## Gestion des paquets et dépôts

### Comprendre les sources de paquets

Pop!OS, basé sur Ubuntu, utilise principalement :

- **Les dépôts officiels Ubuntu** : pour la majorité des logiciels stables.
- **Les dépôts System76** : pour les pilotes, firmware et outils spécifiques.
- **Flatpak** : pour accéder à un large choix d’applications sandboxées.
- **Snap** (optionnel) : autre format de paquets universels.

---

### Ajouter et gérer des dépôts PPA

Pour installer des logiciels souvent mis à jour, certains PPA (Personal Package Archives) peuvent être ajoutés :

```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```

## Conclusion

Pop!OS est une distribution Linux moderne, stable et adaptée aussi bien aux débutants qu’aux utilisateurs avancés.

Grâce à son interface COSMIC intuitive et ses outils intégrés, elle offre une expérience fluide et productive, que ce soit pour le développement, la création ou l’usage quotidien.

Ce tutoriel a couvert les étapes clés : préparation, téléchargement, installation, premiers réglages et outils essentiels.

N’hésitez pas à explorer davantage Pop!OS et à personnaliser votre environnement pour en tirer le meilleur.
