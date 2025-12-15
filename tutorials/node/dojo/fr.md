---
name: Dojo
description: Un nœud Bitcoin open-source orienté confidentialité et autonomie
---

![cover](assets/cover.webp)

*Ce tutoriel s’appuie sur [la documentation officielle d’Ashigaru](https://ashigaru.rs/docs/), que j’ai reprise et enrichie. J’ai réécrit toutes les sections pour en améliorer la clarté, ajouté des explications détaillées supplémentaires, ainsi que des illustrations pour les débutants, afin de rendre l’installation et l’utilisation plus faciles à comprendre.*

---

Dojo est un logiciel libre conçu pour servir de serveur backend à certains portefeuilles Bitcoin axés sur la confidentialité, en s'appuyant sur un nœud Bitcoin Core. Historiquement, il a été développé pour fonctionner avec Samourai Wallet, un portefeuille mobile qui proposait des fonctionnalités avancées de confidentialité comme Whirlpool (coinjoin), Ricochet, Stonewall, PayNym... Samourai Wallet est aujourd’hui à l’arrêt suite à l'arrestation de ses développeurs, mais son successeur communautaire, **Ashigaru Wallet**, a pris le relais et continue de s’appuyer sur Dojo pour offrir une expérience complète aux utilisateurs souhaitant garder le contrôle de leurs données lors de leur utilisation de Bitcoin.

![Image](assets/fr/01.webp)

Concrètement, Dojo agit comme une passerelle entre votre portefeuille et le réseau Bitcoin. Sans Dojo, un portefeuille mobile léger doit interroger des serveurs tiers pour obtenir l’état de vos UTXOs et votre historique ou pour diffuser vos transactions. Cela implique une dépendance et une fuite de données sensibles vers un serveur tiers (adresses utilisées, montants, fréquence des paiements...). Avec Dojo, vous hébergez vous-même ce serveur, directement connecté à votre propre nœud Bitcoin. Ainsi, toutes les requêtes de votre portefeuille passent par une infrastructure que vous contrôlez, sans intermédiaire, ce qui renforce votre confidentialité et votre souveraineté.

## Prérequis pour installer un Dojo

L’installation d’un serveur Dojo ne nécessite pas une machine ultra-puissante. Toute personne disposant d’un ordinateur d’entrée de gamme, d’une connexion Internet stable et capable de laisser cet appareil allumé en continu (24 heures sur 24 et 7 jours sur 7) peut mettre en place un Dojo fonctionnel.

### Choisir son type de machine

Vous pouvez utiliser :
- un ordinateur portable ;
- un ordinateur de bureau ;
- un mini-PC (par exemple un Intel NUC, Lenovo Thincentre Tiny...).

Chaque option présente des avantages et des inconvénients :
- Le prix : un mini-PC ou un ordinateur de bureau reconditionné sera souvent moins cher qu’un portable neuf.
- L’encombrement : un mini-PC prend moins de place.
- L’alimentation électrique : un portable a l’avantage d’avoir une batterie, ce qui lui évite de s’éteindre en cas de micro-coupure, contrairement à un mini-PC.
- Les possibilités d’évolution : les barbones permettent généralement d’ajouter de la mémoire ou de remplacer facilement un disque dur.

Pour plus d'information sur le choix de votre matériel, je vous conseille de suivre cette formation :

https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Matériel recommandé

Il n’est pas nécessaire d’acheter une machine neuve. Un ordinateur reconditionné avec les caractéristiques ci-dessous donnera de bien meilleures performances que les cartes électroniques monocartes (comme le Raspberry Pi).

**Spécifications minimales :**
- Architecture x86-64 (processeur 64 bits).
- Processeur double cœur 2 GHz ou plus rapide.
- 8 Go de RAM minimum.
- Disque SSD NVMe de 2 To ou plus (pour stocker la blockchain de Bitcoin et les index nécessaires).

**Système d’exploitation recommandé :**
- Une distribution basée sur Debian, comme Ubuntu 24.04 LTS.

**Matériel recommandé :**
- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- etc.

Il est tout à fait possible de faire tourner un serveur Dojo sur d’autres configurations matérielles. Cependant, pour obtenir les meilleures performances et limiter les problèmes, il est conseillé de respecter les recommandations ci-dessus.

Dans ce tutoriel, je vais utiliser un vieux ThinkCentre Tiny avec un processeur Intel Pentium Dual-Core G4400T, 8 Go de RAM et un SSD de 2 To.

## 1 - Installer Ubuntu

*Si vous souhaitez installer Dojo sur un appareil déjà configuré, vous pouvez ignorer cette étape et passer directement à l’étape 2.*

Après avoir préparé le matériel choisi, il faut maintenant y installer un système d’exploitation. Vous pouvez utiliser pratiquement n’importe quelle distribution Debian, mais je vous recommande d’opter pour une version LTS d’Ubuntu, car c'est parfaitement adapté à notre usage. Voici les étapes à suivre :  

### 1.1. Créer la clé USB amorçable

Depuis un ordinateur déjà fonctionnel (votre machine habituelle), téléchargez l’image ISO d’Ubuntu LTS [sur le site officiel](https://ubuntu.com/download/desktop) (`24.04` au moment de la rédaction de ce tutoriel, mais prenez la plus récente si une autre est disponible).

![Image](assets/fr/02.webp)

Insérez une clé USB d’au moins 8 Go dans cet ordinateur, puis créez une clé amorçable à l’aide d’un logiciel comme [Balena Etcher](https://etcher.balena.io/). Sélectionnez l’image ISO d’Ubuntu que vous venez de télécharger, choisissez la clé USB comme périphérique cible, puis lancez la création (ayez patience, cela peut prendre plusieurs minutes).

![Image](assets/fr/03.webp)

Insérez la clé USB amorçable dans l'ordinateur éteint (celui sur lequel vous voulez faire tourner Dojo). Démarrez ensuite la machine et appuyez immédiatement sur la touche **F12** ou **F10** de votre clavier (selon le modèle) pour accéder au menu de démarrage. Choisissez ensuite votre clé USB comme périphérique prioritaire dans l’ordre de boot de l’ordinateur.

![Image](assets/fr/04.webp)

### 1.2. Installer le système d'exploitation

L’écran d’accueil d’Ubuntu s’affiche. Sélectionnez "*Try or Install Ubuntu*".

![Image](assets/fr/05.webp)

Suivez ensuite le processus classique d’installation d’Ubuntu :
- Choisissez la langue.
- Sélectionnez le type de clavier.
- Si vous êtes connecté par câble RJ45, inutile de configurer le Wi-Fi.
- Cliquez sur "*Install Ubuntu*" et cochez l’option permettant l’installation des logiciels tiers (pilotes Wi-Fi, codecs multimédias...).
- Lorsque l’assistant vous demande le type d’installation, sélectionnez "*Erase disk and install Ubuntu*". **Attention** : cette opération effacera entièrement le contenu du disque. Vérifiez attentivement que le disque choisi correspond bien au SSD NVMe destiné à Dojo.
- Créez un nom d’utilisateur simple (par exemple "*loic*").
- Attribuez un nom à la machine (par exemple "*dojo-node*").
- Définissez un mot de passe robuste et conservez-le précieusement.
- Activez l’option "*Demander mon mot de passe pour ouvrir une session*" afin de renforcer la sécurité.
- Indiquez votre fuseau horaire, puis cliquez sur "*Install*".
- Patientez le temps de l’installation. Une fois terminée, le système redémarrera automatiquement.
- Retirez la clé USB d’installation lors du redémarrage de l’ordinateur.

Pour davantage de détails sur le processus d’installation d’Ubuntu, vous pouvez consulter notre tutoriel dédié :

https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. Mise à jour du système

Après le premier démarrage, ouvrez un terminal à l’aide de la combinaison de touches ***Ctrl + Alt + T*** et exécutez les commandes suivantes pour mettre à jour le système :

```bash
sudo apt update
sudo apt upgrade -y
```

![Image](assets/fr/06.webp)

## 2. Installation des dépendances

Pour que Dojo fonctionne correctement, certaines briques logicielles doivent être présentes sur votre système. Elles servent à gérer les dépôts logiciels, la communication, la décompression d’archives, ainsi que l’exécution de Dojo à l’intérieur de conteneurs Docker. Toutes ces opérations se réalisent dans le terminal.

### 2.1. Préparation

La commande suivante permet de revenir dans votre dossier personnel. C’est une bonne pratique avant d’exécuter une série d’installations.

```bash
cd ~/
```

Avant toute installation, il est nécessaire de s’assurer que la base de données des logiciels disponibles sur votre machine est à jour. Cela évite d’installer des versions obsolètes.

```bash
sudo apt-get update
```

![Image](assets/fr/07.webp)

### 2.2. Installer les utilitaires

Plusieurs outils doivent être ajoutés au système :
- `apt-transport-https` : permet de télécharger des paquets de manière sécurisée via HTTPS
- `ca-certificates` : gère les certificats nécessaires aux connexions chiffrées
- `curl` : pour récupérer des fichiers depuis Internet
- `gnupg-agent` : pour la gestion de clés GPG
- `software-properties-common` : fournit des utilitaires pour manipuler les dépôts APT
- `unzip` : permet de décompresser des fichiers au format ZIP

```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```

Lors de l’installation, le système peut vous demander une confirmation. Tapez alors sur la touche "*y*" puis appuyez sur "*Entrée*".

![Image](assets/fr/08.webp)

### 2.3. Installer Torsocks

Torsocks permet d’exécuter certaines commandes en passant par le réseau Tor, ce qui améliore la confidentialité des communications.

```bash
sudo apt install torsocks
```

![Image](assets/fr/09.webp)

### 2.4. Installer Docker et Docker Compose

Dojo s’exécute à l’intérieur de conteneurs Docker. Cela signifie que chaque service est isolé dans un environnement indépendant, ce qui simplifie la maintenance et la sécurité. Pour cela, il faut installer Docker et l’outil Docker Compose qui permet de gérer plusieurs conteneurs en même temps.

#### Ajout de la clé de signature Docker

Docker met à disposition sa propre clé de signature numérique. L’ajouter permet de vérifier l’authenticité des paquets téléchargés.

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

![Image](assets/fr/10.webp)

#### Ajout du dépôt officiel Docker

Il faut ensuite indiquer au système où trouver les paquets Docker officiels. Cette commande ajoute un nouveau dépôt à la configuration de votre gestionnaire de paquets.

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```

![Image](assets/fr/11.webp)

#### Installation de Docker et Docker Compose

Les composants principaux de Docker peuvent maintenant être installés.

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

![Image](assets/fr/12.webp)

#### Autorisation utilisateur

Par défaut, seules les commandes exécutées avec les droits administrateur peuvent lancer Docker. Pour plus de confort, je vous conseille d’ajouter votre utilisateur courant au groupe "*docker*". Cela permet d’utiliser Docker sans devoir taper systématiquement `sudo`.

```bash
sudo usermod -aG docker $USER
```

![Image](assets/fr/13.webp)

## 3. Création d’un utilisateur isolé (optionnel)

Si vous souhaitez améliorer la sécurité de votre système, je vous recommande de créer un utilisateur distinct exclusivement destiné à l’exécution de Dojo. Cette séparation limite les risques : si un problème de sécurité survient dans Dojo, il ne compromettra pas directement votre compte principal.

### 3.1. Création du compte utilisateur

La commande suivante crée un nouvel utilisateur nommé "*dojo*". Cet utilisateur disposera d’un répertoire personnel `/home/dojo` et de l’accès au terminal bash. Il sera également ajouté au groupe sudo pour permettre l’exécution de commandes admin.

```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```

### 3.2. Définition d’un mot de passe

Il est important d’attribuer un mot de passe fort à ce compte. L’idéal est d’utiliser un gestionnaire de mots de passe tel que Bitwarden afin de générer une combinaison longue et difficile à deviner.

```bash
sudo passwd dojo
```

Le système vous demandera alors de saisir le mot de passe choisi, puis de le confirmer une seconde fois.

https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Autoriser l'utilisateur à utiliser Docker

Pour que l’utilisateur "*dojo*" puisse lancer les conteneurs nécessaires au fonctionnement de Dojo, il doit être ajouté au groupe Docker. Cela évite d’avoir à précéder chaque commande de `sudo`.

```bash
sudo usermod -aG docker dojo
```

### 3.4. Redémarrage du système

Afin que les changements de groupe soient pris en compte, un redémarrage de la machine est nécessaire.

```bash
sudo reboot
```

### 3.5. Connexion avec le nouvel utilisateur

Lorsque le système redémarre, connectez-vous avec l’identifiant ***dojo*** et le mot de passe que vous avez défini précédemment. Toutes les étapes suivantes devront être réalisées depuis ce compte dédié.

## 4. Télécharger et vérifier Dojo

Avant d’installer Dojo, il est indispensable de s’assurer que les fichiers proviennent bien du développeur officiel et qu’ils n’ont pas été modifiés. Cette étape repose sur l’utilisation de PGP et des hachages pour vérifier l'authenticité et l'intégrité des fichiers.

### 4.1. Importer la clé PGP du développeur

Téléchargez la clé publique du développeur via Tor et importez-la dans votre trousseau local. Cette clé servira à vérifier les signatures associées aux fichiers de Dojo.

```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```

![Image](assets/fr/14.webp)

### 4.2. Télécharger la dernière version de Dojo

Récupérez l’archive compressée contenant le code source de Dojo. Dans cet exemple, la version la plus récente est la `1.27.0` : modifiez la commande en fonction de [la dernière version présente ici sur le dépôt GitHub officiel](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).

```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```

![Image](assets/fr/15.webp)

### 4.3. Télécharger les empreintes et leur signature

Les développeurs publient un fichier listant les empreintes numériques des archives, ainsi qu’un fichier signé par leur clé PGP. Téléchargez-les pour pouvoir comparer localement vos fichiers.

```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```

![Image](assets/fr/16.webp)

### 4.4. Vérifier la signature PGP

Vérifiez que le fichier des empreintes a bien été signé par la clé importée.

```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```

Un résultat correct affiche une signature valide avec la clé `E53AD419B242822F19E23C6D3033D463D6E544F6` et l’adresse associée `dojocoder@pm.me`. Un avertissement peut apparaître précisant que la clé n’est pas certifiée : vous pouvez l'ignorer.

Si en revanche la signature est invalide, arrêtez immédiatement le processus d'installation et recommencez depuis le début.

![Image](assets/fr/17.webp)

### 4.5. Vérifier l’intégrité de l’archive

Calculez l’empreinte SHA256 du fichier téléchargé puis ouvrez le fichier des empreintes pour comparer les deux valeurs.

```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```

Si les deux empreintes sont identiques, vous avez la garantie que l’archive n’a pas été modifiée. Si elles diffèrent, n’allez pas plus loin et supprimez les fichiers.

![Image](assets/fr/18.webp)

### 4.6. Extraire et organiser les fichiers

Une fois la vérification réussie, vous pouvez décompresser l’archive et préparer un dossier dédié à l’installation de Dojo.

```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```

![Image](assets/fr/19.webp)

### 4.7. Nettoyer les fichiers inutiles

Supprimez les fichiers temporaires et les archives devenues inutiles afin de garder votre environnement propre.

```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```

![Image](assets/fr/20.webp)

## 5. Configuration de Dojo

Dojo est un serveur backend qui regroupe plusieurs services pour interagir avec votre portefeuille et gérer votre nœud Bitcoin. Sa configuration peut être complexe, mais le projet propose une méthode simplifiée qui installe et configure automatiquement les composants suivants :
- Dojo (API principale)
- Bitcoin Core (nœud complet Bitcoin)
- BTC-RPC Explorer (explorateur de blocs web)
- Fulcrum Indexer (indexation rapide des blocs et des transactions)
- Fulcrum Electrum Server disponible sur le réseau Tor
- Fulcrum Electrum Server disponible sur le réseau local
- Identifiants d’administration

### 5.1. Identifiants d’administration

Pour sécuriser l’accès aux différents services, vous devez générer plusieurs identifiants uniques :
- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- `MYSQL_USER`
- `MYSQL_PASSWORD`
- `NODE_API_KEY`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SECRET`

Ces identifiants **doivent être uniques** (c'est très important, il ne faut pas utiliser le même mot de passe pour plusieurs services), composés uniquement de chiffres, de lettres majuscules et de lettres minuscules (alphanumériques), et comporter environ 40 caractères pour garantir un haut niveau de sécurité. Encore une fois, je vous conseille fortement d'utiliser un gestionnaire de mots de passe.

### 5.2. Accéder aux fichiers de configuration

Les fichiers de configuration de Dojo se trouvent dans le dossier `conf/`. Déplacez-vous dans ce répertoire :

```bash
cd ~/dojo-app/docker/my-dojo/conf/
```

![Image](assets/fr/21.webp)

### 5.3. Configuration de Bitcoin Core

Ouvrez le fichier de configuration de Bitcoin Core avec l’éditeur de texte nano :

```bash
nano docker-bitcoind.conf.tpl
```

![Image](assets/fr/22.webp)

Dans ce fichier, renseignez les identifiants générés :

```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```

⚠️ ***Remplacez `your-ID-here` et `your-password-here` par vos propres identifiants (avec un mot de passe fort).***

Ajustez également la taille de la mémoire cache utilisée par Bitcoin Core pour améliorer les performances (vous pouvez même mettre plus si vous avez beaucoup de RAM disponible) :

```
BITCOIND_DB_CACHE=2048
```

Pour enregistrer vos modifications et fermer l’éditeur :
- appuyez sur `Ctrl + X`
- tapez `y`
- puis appuyez sur "*Entrée*"

### 5.4. Configuration de MySQL

Ouvrez ensuite la configuration de la base de données MySQL :

```bash
nano docker-mysql.conf.tpl
```

Renseignez vos identifiants :

```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```

⚠️ ***Remplacez `your-ID-here` et `your-password-here` par vos propres identifiants (avec des mot de passe forts et uniques).***

Enregistrez de la même manière (`Ctrl + X`, `y`, "*Entrée*").

![Image](assets/fr/23.webp)

### 5.5. Configuration de l’indexeur Fulcrum

Ouvrez le fichier suivant :

```bash
nano docker-indexer.conf.tpl
```

Ajoutez les paramètres pour activer Fulcrum et l’intégrer correctement à Dojo :

```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```

![Image](assets/fr/24.webp)

Ensuite, il y a 2 possibilités en fonction de votre configuration. Si Dojo est installé sur une machine distincte de votre ordinateur de tous les jours (sur une machine dédiée, un serveur...), indiquez son adresse IP dans votre réseau local, par exemple :

```
INDEXER_EXTERNAL_IP=192.168.1.157
```

![Image](assets/fr/25.webp)

Pour connaître l’adresse IP locale de votre machine, ouvrez un autre terminal et saisissez la commande suivante :

```bash
hostname -I
```

Seconde possibilité : si Dojo est exécuté directement sur votre ordinateur personnel de tous les jours, conservez la valeur par défaut déjà présente dans le fichier de configuration :

```
INDEXER_EXTERNAL_IP=127.0.0.1
```

Enregistrez et quittez l’éditeur (`Ctrl + X`, `y`, "*Entrée*").

### 5.6. Configuration du service Node

Enfin, ouvrez la configuration du service principal Dojo :

```bash
nano docker-node.conf.tpl
```

Renseignez vos identifiants :

```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```

⚠️ ***Remplacez `your-password-here` par vos propres identifiants (avec des mot de passe forts et uniques).***

![Image](assets/fr/26.webp)

Activez ensuite l’indexeur local :

```
NODE_ACTIVE_INDEXER=local_indexer
```

Enregistrez et quittez l’éditeur (`Ctrl + X`, `y`, "*Entrée*").

### 5.7. Gestion des identifiants

Une fois la configuration terminée, il n’est pas nécessaire de conserver tous les identifiants générés. Le seul qui devra absolument être sauvegardé est :

```
NODE_ADMIN_KEY
```

Cet identifiant vous permettra de vous connecter plus tard à l’outil de maintenance de Dojo. Tous les autres identifiants peuvent être supprimés de votre gestionnaire de mots de passe ou de vos notes manuscrites. Ils restent accessibles depuis les fichiers de configuration de Dojo si vous deviez les retrouver dans le futur.

## 6. Installation de Dojo

À cette étape, Dojo va être installé et démarré sur votre machine. L’opération va lancer plusieurs services (Bitcoin Core, l’indexeur Fulcrum, le backend Dojo, etc.) et initier la synchronisation complète de la blockchain Bitcoin. Cette étape peut prendre plusieurs jours selon votre matériel et votre connexion Internet.

### 6.1. Vérifier le bon fonctionnement de Docker

Avant de démarrer l’installation, assurez-vous que Docker est opérationnel. Exécutez la commande suivante :

```bash
docker run hello-world
```

Cette commande télécharge et lance un petit conteneur de test. Si tout fonctionne correctement, vous devriez voir apparaître un message similaire à :

```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```

![Image](assets/fr/27.webp)

Si ce message ne s’affiche pas, commencez par redémarrer votre machine avec :

```bash
sudo reboot
```

Reconnectez-vous ensuite à votre compte **dojo** et exécutez de nouveau la commande de test. Si l’erreur persiste, cela indique que Docker n’a pas été installé correctement. Dans ce cas, retournez à l’étape `2.4.` consacrée à l’installation de Docker et vérifiez attentivement chaque commande.

### 6.2. Accéder au répertoire d’installation de Dojo

Les scripts nécessaires à l’installation se trouvent dans le dossier `my-dojo`. Déplacez-vous dans ce répertoire :

```bash
cd ~/dojo-app/docker/my-dojo
```

![Image](assets/fr/28.webp)

Vérifiez avec la commande `ls` que le fichier `dojo.sh` est bien présent. Il s’agit du script principal qui automatise l’installation de Dojo et le lancement de tous ses services.

![Image](assets/fr/29.webp)

### 6.3. Lancer l’installation

Démarrez l’installation en exécutant le script :

```bash
./dojo.sh install
```

Confirmez l'installation en tapant la touche `y` puis "*Entrée*".

![Image](assets/fr/30.webp)

Ce script va :
- télécharger et lancer les conteneurs Docker nécessaires,
- initialiser Bitcoin Core et commencer à synchroniser la blockchain,
- démarrer l’indexeur Fulcrum pour tracer les transactions et les adresses,
- activer le backend Dojo et ses API.

Vous allez voir défiler un flux continu de journaux contenant des mentions de couleur comme `bitcoind`, `soroban`, `nodejs` ou encore `fulcrum`. Ce défilement indique que Dojo fonctionne et commence à exécuter les différents services.

![Image](assets/fr/31.webp)

### 6.4. Quitter l’affichage des journaux

Les journaux apparaissent en temps réel dans votre terminal. Pour revenir à l’invite de commande tout en laissant Dojo tourner en arrière-plan, tapez :

```
Ctrl + C
```

Ne vous inquiétez pas : arrêter l’affichage des journaux ne stoppe pas les services. Docker continue à exécuter Dojo en arrière-plan (il ne faut évidemment pas arrêter l'ordinateur si vous voulez que l'IBD continue).

### 6.5. Comprendre l’*Initial Block Download* (IBD)

Dès le démarrage, Bitcoin Core doit télécharger et vérifier l’intégralité de la blockchain depuis 2009. Cette étape est appelée ***Initial Block Download* (IBD)**. Elle est indispensable, car elle permet à votre nœud Dojo de vérifier chaque bloc et transaction Bitcoin de manière indépendante.

La durée de cette synchronisation dépend de plusieurs facteurs :
- la puissance de votre processeur et la quantité de mémoire RAM disponible,
- la vitesse de votre disque,
- le nombre et la qualité des pairs auxquels votre nœud se connecte,
- la vitesse de votre connexion Internet.

En pratique, cette opération prend généralement entre **2 et 7 jours**. Pendant cette période, vous pouvez laisser votre machine tourner en continu. Plus la machine reste allumée, plus vite la synchronisation sera terminée. Je vous conseille de vérifier régulièrement l’état de la synchronisation en consultant les journaux de Bitcoin Core ou en utilisant l’outil de maintenance de Dojo une fois installé (partie suivante).

Pour approfondir vos connaissances sur l’IBD et, plus largement, sur le fonctionnement ainsi que le rôle de votre nœud Bitcoin, je vous recommande de consulter ce cours :

https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Suivi de la synchronisation

Lors de la première installation de Dojo, il faut attendre que deux opérations principales soient entièrement terminées : le téléchargement complet de la blockchain Bitcoin (*IBD*) et l’indexation de cette blockchain par Fulcrum. Selon votre connexion et la puissance de votre machine, cela peut prendre plusieurs jours. Pendant cette période, vous pouvez surveiller l’avancée du processus pour vous assurer que tout fonctionne correctement.

Deux méthodes existent pour suivre l’état de la synchronisation :
- l’utilisation de l’outil de maintenance de Dojo (ou DMT), qui est simple mais fournit peu de détails durant l’IBD ;
- la consultation directe des logs de Dojo sur votre machine, plus technique mais beaucoup plus précise.

### 7.1. Vérification via l’outil de maintenance de Dojo (DMT)

Le Dojo Maintenance Tool est une interface web sécurisée qui permet de surveiller l’état de votre installation, et de réaliser certaines opérations. C’est la méthode la plus simple et la plus accessible pour suivre l'avancement de l'IBD. Durant la phase initiale de synchronisation, les informations affichées peuvent être limitées. Par exemple, le DMT ne montre pas l’avancement détaillé de l’indexation de Fulcrum. En revanche, une fois la synchronisation terminée, le DMT affichera clairement :
- tous les voyants au vert ;
- le dernier bloc validé à jour pour chaque service (Node, Indexer, Dojo DB).

Pour y accéder, vous devez connaître l’URL de votre DMT et vous y connecter [via le navigateur Tor](https://www.torproject.org/download/). Pour cela, ouvrez un terminal et placez-vous dans le répertoire `/my-dojo` :

```bash
cd ~/dojo-app/docker/my-dojo
```

Puis exécutez la commande suivante :

```bash
./dojo.sh onion
```

![Image](assets/fr/32.webp)

Vous aurez alors accès à l’ensemble des informations relatives aux connexions à votre Dojo via Tor. Celle qui nous intéresse ici est l’URL suivante :

```
Dojo API and Maintenance Tool =
```

Pour accéder au DMT depuis n’importe quelle machine, quel que soit le réseau (même à distance), ouvrez Tor Browser et saisissez cette URL suivie de `/admin`. Par exemple, si votre URL est `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, vous devrez entrer dans la barre de [Tor Browser](https://www.torproject.org/download/) :

```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```

⚠️ **Attention : conservez cette adresse strictement confidentielle.**

Vous serez ensuite redirigé vers une page d’authentification. La connexion au DMT s’effectue à l’aide du mot de passe `NODE_ADMIN_KEY` que vous avez généré plus tôt.

![Image](assets/fr/33.webp)

Une fois connecté, vous accédez au *Dojo Maintenance Tool* ! Durant l'IBD, vous pouvez notamment voir l'information "*Latest Block*" dans le menu "*FULL NODE*", qui vous permet de savoir où en est votre noeud Bitcoin.

![Image](assets/fr/34.webp)

Pensez à ajouter cette adresse à vos favoris dans Tor Browser afin de la retrouver facilement par la suite.

Une fois votre Dojo entièrement synchronisé, vous devriez voir apparaître des green check ✅ sur l’ensemble des indicateurs de la page d’accueil du DMT.

### 7.2. Vérification via les logs de Dojo

La seconde méthode pour suivre l’avancement de votre IBD consiste à consulter directement les logs de votre machine. Cette approche offre un suivi bien plus précis et en temps réel. Vous pouvez ainsi observer la progression du téléchargement des blocs par Bitcoin Core ainsi que l’indexation réalisée par Fulcrum.

Connectez-vous à la machine qui héberge votre Dojo et ouvrez un terminal. Toutes les commandes doivent être exécutées depuis le répertoire `my-dojo`. Positionnez-vous dans ce dossier :

```bash
cd ~/dojo-app/docker/my-dojo
```

![Image](assets/fr/35.webp)

#### Logs de Bitcoin Core

Affichez les journaux liés à Bitcoin Core pour suivre la progression de l’IBD :

```bash
./dojo.sh logs bitcoind
```

Au début, vous verrez apparaître une phase de présynchronisation des en-têtes de blocs :

```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```

Lorsque ce chiffre atteint 100 %, Bitcoin Core entame alors le téléchargement complet de la blockchain. Vous verrez apparaître la progression de l’IBD. Pour connaître la hauteur de bloc en cours, consultez la valeur indiquée par `height=`. Vous pouvez également suivre la clé `progress=`, qui renseigne le pourcentage d’avancement de l’IBD.

![Image](assets/fr/36.webp)

Comme toujours, pour fermer les logs et revenir à l’invite de commande, utilisez la combinaison `Ctrl + C`.

#### Logs de Fulcrum

Une fois que Bitcoin Core a terminé la présynchronisation des en-têtes, Fulcrum commence à indexer la blockchain au fur et à mesure. Affichez ses journaux avec :

```bash
./dojo.sh logs fulcrum
```

Vous verrez alors s’afficher la hauteur du dernier bloc indexé, indiquée après `height:`, ainsi que le pourcentage de progression de l’indexation.

![Image](assets/fr/37.webp)

### 7.3. Corruption de la base de données de Fulcrum

Fulcrum est un indexeur particulièrement performant, mais son installation peut s’avérer complexe, notamment en raison de la gestion délicate de sa base de données. En cas de coupure de courant ou d’arrêt brutal de la machine durant la synchronisation initiale, la base de données de l’indexeur risque d’être corrompue. Vous pouvez le constater, par exemple, si vous avez les logs suivants :

```bash
fulcrum | The database has been corrupted etc... 
```

**Note :** Ce type d’erreur devrait être corrigé avec la sortie prochaine de Fulcrum 2.0.

Si cela vous arrive, aucun impact n’est à craindre sur bitcoind (votre nœud Bitcoin) : son IBD poursuivra sa progression indépendamment de Fulcrum. En revanche, il sera impossible d’utiliser Fulcrum tant que vous n’aurez pas supprimé ses données corrompues et relancé sa synchronisation depuis le début. Voici la marche à suivre :

Arrêtez Dojo :

```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```

Supprimez uniquement le conteneur et le volume de Fulcrum :

```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```

Normalement le nom est `my-dojo_data-fulcrum`, si ce n'est pas le cas pour vous, adaptez le nom renvoyé par la commande précédente.

Ensuite relancez Dojo et reconstruisez Fulcrum de zéro :

```bash
./dojo.sh upgrade
```

Vous pouvez ensuite vérifier le bon fonctionnement de Fulcrum en consultant les logs :

```bash
docker logs -f fulcrum
```


## 8. Utilisation du Dojo Maintenance Tool

Une fois votre nœud Bitcoin synchronisé sur la tête de chaîne présentant le plus de preuve de travail, et la blockchain indexée à 100 % par Fulcrum, vous pouvez commencer à utiliser votre Dojo.

Votre Dojo propose de nombreuses fonctionnalités, régulièrement enrichies à chaque nouvelle version. Selon moi, les 2 plus importantes sont :
- la possibilité de connecter votre portefeuille Ashigaru afin d’utiliser votre propre nœud pour consulter les données de la blockchain et diffuser vos transactions,
- et l’explorateur de blocs, qui offre un accès à des informations sur la blockchain Bitcoin sans exposer vos données à une instance extérieure que vous ne contrôlez pas.

Découvrons comment les utiliser.
### 8.1. Connecter Ashigaru à votre Dojo

Pour connecter votre portefeuille Ashigaru à votre Dojo, c’est très simple : une fois sur votre DMT, ouvrez le menu "*Pairing*". Un QR code s’affiche, que vous pouvez scanner directement avec l’application Ashigaru.

![Image](assets/fr/38.webp)

Dans l’application Ashigaru, au premier lancement après avoir créé ou restauré votre portefeuille, vous serez redirigé vers la page "*Configure your Dojo server*". Appuyez sur "*Scan QR*", puis scannez le QR code affiché sur votre DMT.

![Image](assets/fr/39.webp)

Cliquez ensuite sur le bouton "*Continue*".

![Image](assets/fr/40.webp)

Vous êtes désormais connecté à votre Dojo.

![Image](assets/fr/41.webp)

### 8.2. Utiliser l'explorateur de bloc

Dojo installe automatiquement un explorateur de blocs, [BTC-RPC Explorer](https://github.com/janoside/btc-rpc-explorer), qui s’appuie directement sur les données de votre propre nœud Bitcoin. Un explorateur vous permet d’accéder aux informations brutes de la blockchain et de votre mempool à travers une interface web facile à comprendre. Vous pouvez ainsi, par exemple, vérifier l’état d’une transaction en attente, consulter le solde d’une adresse ou encore examiner la composition d’un bloc facilement.

Pour y accéder, rien de plus simple : il suffit de récupérer l’adresse Tor de votre explorateur. Pour cela, exécutez la même commande que celle utilisée précédemment pour obtenir l’adresse de votre DMT :

```bash
./dojo.sh onion
```

![Image](assets/fr/42.webp)

Vous aurez accès à l’ensemble des informations relatives aux connexions à votre Dojo via Tor. Celle qui nous intéresse ici est l’URL suivante :

```
Block Explorer =
```

Si vous êtes déjà connecté à votre DMT, vous pouvez également retrouver cette adresse dans le menu "*Pairing*", à l’intérieur du JSON de connexion :

![Image](assets/fr/43.webp)

Pour accéder à votre explorateur depuis n’importe quelle machine, quel que soit le réseau (même à distance), ouvrez [Tor Browser](https://www.torproject.org/download/) et saisissez l’URL que vous venez de récupérer.

⚠️ **Attention : gardez cette adresse strictement confidentielle.**

Vous aurez alors accès à votre propre explorateur de blocs.

![Image](assets/fr/44.webp)

*Crédit image : https://ashigaru.rs/.*

Pour suivre une transaction, il vous suffit d’entrer son TXID dans la barre de recherche située en haut à droite.

![Image](assets/fr/45.webp)

*Crédit image : https://ashigaru.rs/.*

Pour vérifier les mouvements associés à une adresse, procédez de la même manière en saisissant l’adresse dans la barre de recherche.

![Image](assets/fr/46.webp)

*Crédit image : https://ashigaru.rs/.*

Vous pouvez également renseigner le hash d’un bloc ou sa hauteur dans la barre de recherche pour en afficher le détail.

![Image](assets/fr/47.webp)

*Crédit image : https://ashigaru.rs/.*

## 9. Maintenance de votre Dojo

### 9.1 Arrêter votre Dojo

Ne coupez jamais brutalement l’alimentation de votre Dojo, au risque de corrompre certaines bases de données, en particulier celle de l’indexeur Fulcrum. Si vous devez l’éteindre, procédez toujours à un arrêt propre de Dojo, puis, une fois toutes les procédures terminées, éteignez la machine à son tour :

```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```

### 9.2 Mettre à jour votre Dojo

Dojo évolue régulièrement et de nouvelles versions sont publiées pour corriger des bugs, améliorer la stabilité et ajouter des fonctionnalités. Il est donc important [de vérifier régulièrement si des mises à jour sont disponibles](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) et de mettre à jour votre Dojo. Le processus est proche de l’installation initiale, mais nécessite de remplacer certains fichiers par la dernière version disponible tout en conservant votre configuration. Voici les étapes détaillées à suivre pour effectuer une mise à jour propre et sécurisée :

Pour connaitre la version actuelle de votre Dojo, exécutez la commande : 

```bash
./dojo.sh version
```

Bien que cette étape soit optionnelle, je vous conseille de commencer par mettre à jour votre OS. Cela réduit les risques d’incompatibilités et assure que les dépendances utilisées par Dojo sont à jour :

```bash
sudo apt-get update
sudo apt-get upgrade
```

Placez-vous dans le répertoire de Dojo et arrêtez les services en cours :

```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```

Ensuite, redémarrez votre système pour repartir sur une base propre :

```bash
sudo reboot
```

Dojo est fourni avec des fichiers signés numériquement. Ces signatures PGP assurent que les fichiers proviennent bien du développeur et qu’ils n’ont subi aucune altération. Leur vérification est importante à chaque mise à jour, exactement comme lors de l’installation initiale. Commencez par télécharger la clé publique du développeur via Tor, puis importez-la :

```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```

Revenez dans votre répertoire personnel :

```bash
cd ~/
```

Téléchargez la dernière version de Dojo depuis GitHub via Tor. Dans cet exemple, il s’agit de la version `1.28.0` (qui n'existe pas encore au moment de la rédaction de ce tuto : c'est pour prendre un exemple). Pensez à remplacer le fichier et le lien [avec la version que vous souhaitez installer](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) :

```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```

Téléchargez également le fichier contenant les empreintes et la signature PGP (encore une fois, pensez à ajuster la version dans la commande) :

```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```

Vérifiez que le fichier d’empreintes téléchargé a bien été signé par la clé du développeur :

```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```

Un résultat correct doit afficher :

```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```

Un avertissement concernant l’absence de certification de la clé peut apparaître, mais il est sans importance. En revanche, si la signature est invalide ou correspond à une autre clé, n’allez pas plus loin et recommencez en vérifiant les liens.

Calculez ensuite l’empreinte SHA256 de l’archive et comparez-la avec celle du fichier d’empreintes officiel :

```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```

Si les deux empreintes correspondent parfaitement, l’archive est authentique et intacte. Si elles diffèrent, supprimez immédiatement les fichiers et ne continuez pas.

Décompressez l’archive dans votre répertoire personnel :

```bash
unzip samourai-dojo-1.28.0.zip -d .
```

Copiez ensuite le contenu vers le répertoire de Dojo, en écrasant les anciens fichiers :

```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```

Cette opération conserve vos fichiers de configuration situés dans `~/dojo-app/docker/my-dojo/conf`, mais remplace tous les autres fichiers par les versions mises à jour.

Pour garder un environnement propre, supprimez les fichiers inutiles :

```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```

Retournez dans le répertoire des scripts de Dojo et lancez la commande de mise à jour :

```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```

Cette commande demande à Docker de reconstruire les images avec les nouveaux fichiers, puis de relancer automatiquement tous les services. À la fin du processus, consultez les journaux pour vérifier que Bitcoin Core, Fulcrum et Dojo fonctionnent tous correctement :

```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```

Si les services démarrent sans erreur et que les journaux affichent des blocs en cours de traitement, cela signifie que votre Dojo est désormais à jour et opérationnel.
