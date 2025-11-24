---
name: Kali
description: Installer Kali Linux sur VirtualBox, en clé USB bootable, ou en dual boot, étape par étape.
---

![cover-kali](assets/cover.webp)

## Introduction

### Pourquoi Kali Linux ?

**Kali Linux** est une distribution Linux spécialisée dans la sécurité informatique.
Voici pourquoi on utilise Kali Linux :

- Il est préconfiguré avec de nombreux outils de pentesting (tests de sécurité des systèmes et réseaux).
- Il est **open source et gratuit**, vous pouvez donc l’utiliser et le modifier librement.
- Il est **fiable et sécurisé**, idéal pour apprendre la cybersécurité.
- Il permet d’apprendre à utiliser Linux tout en ayant un environnement prêt pour les tests.
- Il peut être installé de différentes manières : **VirtualBox**, **clé USB bootable**, ou **dual boot**.

## Installation et configuration

### 1. Prérequis

**Matériel nécessaire :**

- **Processeur 64 bits** (Intel ou AMD).
- **8 Go de RAM minimum** (4 Go peuvent suffire pour une installation légère ou une VM).
- **50 Go d’espace disque libre** pour installer Kali Linux.
- **Connexion Internet** pour télécharger l’image ISO et les mises à jour.
- **Une clé USB de 8 Go minimum** pour créer un support bootable (si vous souhaitez installer Kali sur un PC ou tester en Live USB).

Il est important de sauvegarder vos données avant toute installation sur un PC existant.

### 2. Téléchargement

- Rendez-vous sur [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Choisissez l’image ISO correspondant à votre usage :
  - **Installer Image** : pour installation sur PC.
  - **Virtual Image** : pour installer Kali sur VirtualBox ou VMware.
- Téléchargez l’image ISO.

![Page de téléchargement Kali](assets/fr/01.webp)

![Sélection de la version Kali](assets/fr/02.webp)

### 3. Créer une clé USB bootable

Vous pouvez utiliser plusieurs outils, par exemple Balena Etcher :

- Téléchargez [Balena Etcher](https://etcher.balena.io/) et installez-le.

![Page de téléchargement Balena Etcher](assets/fr/03.webp)

![Installation de Balena Etcher](assets/fr/04.webp)

- Ouvrez Balena Etcher, puis sélectionnez l'image ISO de Kali.
- Sélectionnez la clé USB comme support de destination.
- Cliquez sur Flash et attendez la fin du processus.

![Utilisation de Balena Etcher](assets/fr/05.webp)

### 4. Installer et sécuriser Kali Linux

#### 4.1 Démarrage sur la clé USB

- Éteignez l'ordinateur.
- Branchez la clé USB (contenant Kali Linux).
- Allumez l'ordinateur. Sur les PC récents, le système devrait reconnaître automatiquement la clé USB de démarrage. Si ce n'est pas le cas, redémarrez en maintenant la touche d'accès au BIOS/UEFI (généralement F2, F12 ou Delete, selon la marque).
  - Dans le menu du BIOS/UEFI, sélectionnez votre clé USB comme périphérique de démarrage (Boot).
  - Sauvegardez (Save) et redémarrez.

#### 4.2 Lancement de l'installation

##### Écran de démarrage

Lors du démarrage sur la clé USB, l'écran de démarrage de Kali Linux devrait s'afficher. Choisissez entre **l'installation graphique** et **l'installation** en mode texte. Dans cet exemple, nous avons opté pour l'installation graphique.

![capture](assets/fr/06.webp)

Si vous utilisez l'image **Live**, vous verrez un autre mode, **Live**, qui est également l'option de démarrage par défaut.

![Mode Live](assets/fr/07.webp)

##### Choix de la langue

Choisissez votre langue préférée pour l'installation et le système.

![Sélection de la langue](assets/fr/08.webp)

Veuillez préciser votre situation géographique.

![Options d'accessibilité](assets/fr/09.webp)

##### Configuration du clavier

Sélectionnez la disposition de votre clavier. Un champ de test est disponible pour vérifier que les touches correspondent bien à votre configuration.

![Configuration du clavier](assets/fr/10.webp)

##### Connexion réseau

L'installation va maintenant analyser vos interfaces réseau, rechercher un service DHCP, puis vous inviter à saisir un nom d'hôte pour votre système. Dans l'exemple ci-dessous, nous avons saisi **« kali »** comme nom d'hôte.

![Configuration réseau](assets/fr/11.webp)

Vous pouvez éventuellement fournir un nom de domaine par défaut que ce système utilisera (les valeurs peuvent être récupérées à partir du DHCP ou s'il existe un système d'exploitation préexistant).

![Choix du type d'installation](assets/fr/12.webp)

##### Comptes utilisateurs

Ensuite, créez le compte utilisateur pour le système (nom complet, nom d'utilisateur et un mot de passe fort).

![Création d'un utilisateur](assets/fr/13.webp)

![Mode d'installation](assets/fr/14.webp)

![Sélection des applications](assets/fr/15.webp)

##### Fuseau horaire

Sélectionnez votre zone géographique pour configurer l'heure système.

![Sélection du fuseau horaire](assets/fr/16.webp)

##### Type de partitionnement

Le programme d’installation analyse ensuite vos disques et affiche plusieurs options selon votre configuration.

Dans ce guide, nous partons d’un **disque vierge**, ce qui fait apparaître **quatre choix possibles**.
Nous allons sélectionner **Guidé - utiliser tout le disque**, car nous effectuons ici une installation unique de Kali Linux (mono-amorçage). Cela signifie qu’aucun autre système d’exploitation ne sera conservé, et que le disque peut être entièrement effacé.

Si votre disque contient déjà des données, une option supplémentaire **Guidé – utiliser le plus grand espace libre contigu** peut s’afficher.

Cette alternative permet d’installer Kali Linux sans supprimer les données existantes, pratique pour un double démarrage (dual boot) avec un autre système.

Dans notre cas, le disque est vide, donc cette option n’apparaît pas.

![Choix du partitionnement](assets/fr/17.webp)

Sélectionnez le disque à partitionner.

![capture](assets/fr/18.webp)

Selon vos besoins, vous pouvez choisir de conserver tous vos fichiers dans une seule partition (comportement par défaut) ou d'avoir des partitions séparées pour un ou plusieurs répertoires de premier niveau.

Si vous n'êtes pas sûr de ce que vous voulez, prenez l'option **Tous les fichiers dans une seule partition**.

![capture](assets/fr/19.webp)

![capture](assets/fr/20.webp)

Vous aurez ensuite une dernière occasion de vérifier la configuration de votre disque avant que le programme d'installation n'effectue des modifications irréversibles. Après avoir cliqué sur _Continuer_, le programme d'installation se lancera et l'installation sera presque terminée.

![capture](assets/fr/21.webp)

##### LVM chiffré

Si cette option a été activée à l'étape précédente, Kali Linux va maintenant procéder à un effacement sécurisé du disque dur avant de vous demander un mot de passe LVM.

Veuillez utiliser un mot de passe fort, sinon un avertissement concernant une phrase de passe faible s'affichera.

##### Informations sur les proxys

Kali Linux utilise des dépôts pour distribuer les applications. Vous devrez saisir les informations de proxy nécessaires si votre environnement en utilise.

Si vous n’êtes **pas certain** d’utiliser un proxy, **laissez vide**. Saisir de fausses informations empêchera la connexion aux dépôts.

![capture](assets/fr/22.webp)

##### Métapaquets

Si l'accès réseau n'a pas été configuré, vous devrez **poursuivre la configuration** lorsque vous y serez invité.

Si vous utilisez l'image **Live**, l'étape suivante ne s'affichera pas.

Vous pouvez ensuite sélectionner les [métapaquets](https://www.kali.org/docs/general-use/metapackages/) que vous souhaitez installer. Les options par défaut installeront un système Kali Linux standard ; vous n'aurez donc rien à modifier.

![capture](assets/fr/23.webp)

#### Informations de démarrage

Confirmez ensuite l'installation du chargeur de démarrage GRUB.

![capture](assets/fr/24.webp)

##### Redémarrage

Enfin, cliquez sur Continuer pour redémarrer sur votre nouvelle installation de Kali Linux.

![capture](assets/fr/25.webp)

#### 4.3 Mise à jour et configuration de Kali Linux après installation

La mise à jour du système est une étape importante après une nouvelle installation. Vous avez deux options :

##### Option 1 : Via l'interface graphique (GUI)

Kali, comme Debian/Ubuntu, propose un gestionnaire de mises à jour graphique intégré.

1. Cliquez sur le **menu principal** (en haut à gauche ou en bas selon le bureau).
2. Ouvrez **"Software Updater"** ou **"Mises à jour logicielles"**.
3. L’outil va :
    - Vérifier les paquets à mettre à jour.
    - Vous afficher une liste (avec les tailles et versions).
    - Vous permettre de lancer la mise à jour en un clic.
4. Entrez votre mot de passe administrateur (`sudo`) quand demandé.
5. Laissez-le installer et redémarrez si nécessaire.

##### Option 2 : Via le terminal

Ouvrez un terminal et exécutez :

```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```

Il n'est pas conseillé d'utiliser le compte **root** pour le travail au quotidien ; créez plutôt un utilisateur non-root.

Dans votre terminal, tapez ces commandes :

```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```

Déconnectez-vous puis reconnectez-vous avec le nouvel utilisateur.

Résumons maintenant dans un tableau quelques tâches de base sous Kali Linux.

### Les tâches de base sous Kali Linux

| **Catégorie**              | **Tâche de base**                      | **Description / Objectif**                                 | **Méthode principale**                                       |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Navigation système**     | Ouvrir le terminal                     | Accéder à la ligne de commande principale de Kali          | Cliquez sur l’icône du terminal ou utilisez `Ctrl + Alt + T` |
|                            | Parcourir les dossiers                 | Se déplacer dans l’arborescence du système                 | `cd /chemin/du/dossier`, `ls` pour lister les fichiers       |
|                            | Créer / supprimer un dossier           | Organiser les fichiers                                     | `mkdir nom_dossier`, `rm -r nom_dossier`                     |
| **Gestion des fichiers**   | Copier / déplacer un fichier           | Manipuler des fichiers dans le terminal                    | `cp fichier destination`, `mv fichier destination`           |
|                            | Supprimer un fichier                   | Libérer de l’espace disque                                 | `rm nom_du_fichier`                                          |
|                            | Afficher le contenu d’un fichier texte | Lire rapidement un fichier                                 | `cat fichier.txt`, `less fichier.txt`                        |
| **Gestion du système**     | Mettre à jour Kali Linux               | Installer les dernières versions et correctifs de sécurité | `sudo apt update && sudo apt full-upgrade -y`                |
|                            | Installer un logiciel                  | Ajouter un nouvel outil ou utilitaire                      | `sudo apt install nom_du_paquet`                             |
|                            | Supprimer un logiciel                  | Nettoyer le système                                        | `sudo apt remove nom_du_paquet`                              |
|                            | Nettoyer les dépendances inutiles      | Gagner de l’espace disque                                  | `sudo apt autoremove`                                        |
| **Réseau et Internet**     | Vérifier la connexion réseau           | Tester l’accès à Internet                                  | `ping google.com`                                            |
|                            | Identifier l’adresse IP                | Connaître sa configuration réseau                          | `ip a` ou `ifconfig`                                         |
|                            | Changer de réseau Wi-Fi                | Se connecter à un autre point d’accès                      | Icône réseau → Sélectionner le Wi-Fi voulu                   |
| **Comptes et permissions** | Exécuter une commande administrateur   | Obtenir les droits root temporairement                     | `sudo commande`                                              |
|                            | Créer un nouvel utilisateur            | Ajouter un compte local                                    | `sudo adduser nom_utilisateur`                               |
|                            | Modifier un mot de passe               | Sécuriser un compte                                        | `passwd`                                                     |
| **Apparence et confort**   | Changer le fond d’écran                | Personnaliser le bureau                                    | Clic droit sur le bureau → **Paramètres du bureau**          |
|                            | Modifier le thème / icônes             | Améliorer la lisibilité et l’esthétique                    | Paramètres → Apparence / Thèmes                              |
| **Outils Kali**            | Ouvrir le menu des outils              | Explorer les outils de test et de sécurité                 | Menu **Applications → Kali Linux**                           |
|                            | Lancer un outil (ex : nmap, wireshark) | Découverte pratique des utilitaires de sécurité            | `sudo nmap`, `wireshark`, etc.                               |
| **Aide et documentation**  | Obtenir de l’aide sur une commande     | Comprendre une commande avant de l’utiliser                | `man commande` ou `commande --help`                          |

## Conclusion

L’installation de Kali Linux n’est qu’une première étape dans la découverte de cet environnement puissant dédié à la cybersécurité. En maîtrisant les tâches de base et la gestion du système, chacun peut commencer à explorer les outils intégrés et à comprendre le fonctionnement interne d’un système Linux. Kali offre une excellente plateforme d’apprentissage, autant pour renforcer ses compétences techniques que pour développer une véritable culture de la sécurité informatique.
