---
name: POS OS
description: Installer POS OS
author: Bened45
---


# Kali Linux

![cover](assets/cover.webp)

## Introduction

Pop!OS est un système d’exploitation basé sur Linux, développé par *System76*, un constructeur américain spécialisé dans les machines dédiées aux développeurs, aux créateurs et aux utilisateurs avancés.
Conçu pour offrir un environnement moderne, stable et performant, Pop!_OS se distingue par une expérience simple, des outils puissants et une forte orientation vers la productivité

### Qui est System 76?

System76 est une entreprise américaine fondée en 2005 et basée à Denver, spécialisée dans la fabrication d’ordinateurs portables, de PC de bureau et de serveurs conçus spécialement pour Linux.  
Contrairement aux constructeurs traditionnels, System76 développe des machines pensées pour être ouvertes, réparables et tournées vers la liberté logicielle.
System76 ne se contente pas de fabriquer des ordinateurs.  
L’entreprise développe également :

- **Pop!_OS**, son propre système d’exploitation basé sur Linux ;
- **COSMIC**, l’environnement de bureau moderne et performant utilisé par Pop!_OS ;
- **Open Firmware**, un firmware open-source basé sur Coreboot ;
- des outils destinés aux développeurs et aux créateurs.

L’objectif est d’offrir une intégration matérielle et logicielle de haute qualité, comparable à l’écosystème Apple, mais totalement ouverte et centrée sur Linux.

## Un système moderne, stable et accessible

Pop!OS reprend les fondations d’Ubuntu, ce qui lui confère une excellente stabilité, une compatibilité matérielle large et un accès à un écosystème logiciel immense.  
Il fournit une interface élégante, le bureau COSMIC, pensé pour être fluide, intuitif et personnalisable, même pour les nouveaux utilisateurs.**

## Un choix idéal pour les développeurs, créateurs et utilisateurs exigeants

Pop!OS est particulièrement apprécié par :

- les développeurs (outils préinstallés, gestion avancée du tiling),
- les utilisateurs avec cartes graphiques Nvidia ou AMD,
- les étudiants et professionnels recherchant un système fiable,
- les personnes venant de Windows souhaitant une transition simple.

Il inclut une gestion automatique des fenêtres en mosaïque (“tiling”), un centre de logiciels clair, ainsi que des outils de productivité intégrés qui facilitent l’utilisation quotidienne.

## Points forts de Pop!_OS

- **Performance optimisée** grâce à des mises à jour régulières.
- **Deux ISO disponibles** : version standard et version optimisée Nvidia.
- **Sécurité renforcée** (chiffrement LUKS disponible dès l’installation).
- **Interface COSMIC** ergonomique et moderne.
- **Grande compatibilité** avec les logiciels Ubuntu et Flatpak.

## Télécharger Pop!_OS de manière sûre

### 1. Prérequis

Avant de télécharger et d’installer Pop!OS, quelques éléments sont nécessaires pour préparer correctement l’environnement d’installation.

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

L’image ISO de Pop!OS doit être téléchargée directement depuis la page officielle de System76 :
 [pop.system76](https://system76.com/pop/)

Cette page propose toujours la version la plus récente et la plus adaptée à votre matériel.

![capture](assets/fr/03.webp)

### **Choisir la version : Standard ou Nvidia, ou Raspberry Pi (ARM64)**

Pop!OS est disponible en trois variantes :

### **Version Standard**

Recommandée pour les ordinateurs utilisant :

- un processeur Intel ou AMD ;
- un GPU intégré Intel ou AMD ;
- une carte graphique AMD Radeon.

![Utilisation de Balena Etcher](assets/fr/04.webp)

### **• Version Nvidia**

Recommandée pour les ordinateurs équipés d’une carte graphique Nvidia.  
Cette image inclut déjà les pilotes Nvidia, ce qui facilite l’installation et réduit les problèmes graphiques.

![Utilisation de Balena Etcher](assets/fr/05.webp)

### **Version Raspberry Pi (ARM64)**

Pour Raspberry Pi 4 et 400 (processeur ARM).  
Adaptée à l’architecture ARM, c’est une version spécifique pour ces mini-ordinateurs.

![Utilisation de Balena Etcher](assets/fr/06.webp)

## Créer une clé USB bootable

Vous pouvez utiliser plusieurs outils, par exemple Balena Etcher :

- Téléchargez [Balena Etcher](https://etcher.balena.io/) et installez-le.

![Page de téléchargement Balena Etcher](assets/fr/07.webp)

![Installation de Balena Etcher](assets/fr/08.webp)

- Ouvrez Balena Etcher, puis sélectionnez l'image ISO de Pop!_OS.
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

Une fois votre clé USB bootable sélectionnée comme périphérique de démarrage, votre ordinateur démarrera dans un Pop live !_Environnement OS.

1. Sélectionnez votre langue.

![Capture](assets/fr/10.webp)

2. Sélectionnez un lieu.

![Capture](assets/fr/11.webp)

3. Sélectionnez une langue de saisie au clavier.

![Capture](assets/fr/12.webp)

4. Sélectionnez une disposition de clavier.

![Capture](assets/fr/13.webp)

5. Choisissez le `Clean Install` option pour une installation standard. C'est la meilleure option pour les nouveaux utilisateurs de Linux, mais sachez que cela effacera tout le contenu du lecteur cible. Alternativement, vous pouvez sélectionner `Try Demo Mode` pour continuer à tester Pop!OS dans l'environnement live.

![Capture](assets/fr/14.webp)

Sélectionner `Custom (Advanced)` pour accéder à GParted. Cet outil permet de configurer des fonctionnalités avancées telles que le double démarrage, la création d'un système distinct `/home` partition, ou en plaçant le `/tmp` partition sur un lecteur différent.

6. Cliquez `Erase and Install` pour installer Pop!OS sur votre disque sélectionné.

![Capture](assets/fr/15.webp)

### Configuration du compte utilisateur

La section suivante du programme d'installation vous guidera dans la création d'un compte utilisateur afin que vous puissiez vous connecter à votre nouveau Pop !_Installation du système d'exploitation.

Fournissez un nom complet (cela peut inclure n'importe quel texte de votre choix, majuscule ou minuscule), ainsi qu'un nom d'utilisateur (qui doit être en minuscules) :

![Capture](assets/fr/16.webp)

Une fois le compte créé, vous serez invité à définir un nouveau mot de passe.

![Capture](assets/fr/17.webp)

### Cryptage complet du disque

Le cryptage du disque système n'est pas nécessaire, mais il garantit la sécurité des données utilisateur dans le cas où quelqu'un obtiendrait un accès physique non autorisé à l'appareil.

Le lecteur peut être crypté à l'aide de votre mot de passe de connexion en vérifiant `Encryption password is the same as user account password`, ou vous pouvez décocher cette case et sélectionner `Set Password` en bas. Sélectionner `Don't Encrypt` pour ignorer le processus de cryptage du disque.

![Capture](assets/fr/18.webp)

Si vous avez choisi le `Set Password` bouton, vous verrez une invite supplémentaire pour définir votre mot de passe de cryptage. Cela sera demandé à chaque démarrage du système.

Passez à l’étape suivante dans le programme d’installation. Pop !OS va maintenant commencer l'installation sur le disque.

![Capture](assets/fr/19.webp)

Une fois l’installation terminée, redémarrez votre ordinateur et connectez-vous pour terminer le processus de configuration du compte utilisateur.

 Si vous avez modifié l'ordre de démarrage pour prioriser votre USB en direct au démarrage, arrêtez complètement l'ordinateur et supprimez l'USB d'installation. Si vous démarrez en double, appuyez sur les touches appropriées pour accéder à la configuration et sélectionnez le lecteur contenant le Pop !_Installation du système d'exploitation.

![Capture](assets/fr/20.webp)

### Graphiques NVIDIA

Si vous avez installé à partir de l'ISO Intel/AMD et que votre système dispose d'une carte graphique NVIDIA discrète ou si vous en avez ajouté une ultérieurement, vous devrez installer manuellement les pilotes de votre carte pour obtenir des performances optimales. Exécutez la commande suivante dans un terminal de commande pour installer le pilote :

```bash
sudo apt install system76-driver-nvidia
```

Vous pouvez également installer les pilotes graphiques NVIDIA depuis le Pop !_Boutique.

![Capture](assets/fr/20.webp)

## 7. Installer les outils essentiels

| Outil            | Description                              | Commande d'installation                         |
|------------------|----------------------------------------|------------------------------------------------|
| Firefox          | Navigateur web libre et populaire      | `sudo apt install firefox`                      |
| Brave            | Navigateur web axé sur la confidentialité | Installation via Pop!_Shop ou site officiel    |
| VS Code          | Éditeur de code pour développeurs      | `sudo snap install code --classic`              |
| Git              | Gestionnaire de versions                | `sudo apt install git`                          |
| Terminal GNOME   | Terminal de base intégré                 | Déjà installé par défaut                        |
| Flatpak          | Gestionnaire de paquets alternatif      | `sudo apt install flatpak`                      |
| VLC              | Lecteur multimédia polyvalent           | `sudo apt install vlc`                          |

## Conclusion

Pop!OS est une distribution Linux moderne, stable et adaptée aussi bien aux débutants qu’aux utilisateurs avancés.  
Grâce à son interface COSMIC intuitive et ses outils intégrés, elle offre une expérience fluide et productive, que ce soit pour le développement, la création ou l’usage quotidien.

Ce tutoriel a couvert les étapes clés : préparation, téléchargement, installation, premiers réglages et outils essentiels.  
N’hésitez pas à explorer davantage Pop!OS et à personnaliser votre environnement pour en tirer le meilleur.
