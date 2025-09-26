---
name: Dojo
description: Un nœud Bitcoin open-source orienté confidentialité et autonomie
---

![cover](assets/cover.webp)

*Ce tutoriel s’appuie sur [la documentation officielle d’Ashigaru](https://ashigaru.rs/docs/), que j’ai reprise et enrichie. J’ai réécrit toutes les sections pour en améliorer la clarté, ajouté des explications détaillées supplémentaires, ainsi que des illustrations pour les débutants, afin de rendre l’installation et l’utilisation plus faciles à comprendre.*

---

Dojo est un logiciel libre conçu pour servir de serveur backend à certains portefeuilles Bitcoin axés sur la confidentialité, en s'appuyant sur un nœud Bitcoin Core. Historiquement, il a été développé pour fonctionner avec Samourai Wallet, un portefeuille mobile qui proposait des fonctionnalités avancées de confidentialité comme Whirlpool (coinjoin), Ricochet, Stonewall, PayNym... Samourai Wallet est aujourd’hui à l’arrêt suite à l'arrestation de ses développeurs, mais son successeur communautaire, **Ashigaru Wallet**, a pris le relais et continue de s’appuyer sur Dojo pour offrir une expérience complète aux utilisateurs souhaitant garder le contrôle de leurs données lors de leur utilisation de Bitcoin.

01

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

https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

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

Il est tout à fait possible de faire tourner un serveur Dojo sur d’autres configurations matérielles. Cependant, pour obtenir les meilleures performances et limiter les problèmes, il est conseillé de respecter les recommandations ci-dessus.

Dans ce tutoriel, je vais utiliser un ThinkCentre Tiny.

## 1 - Installer Ubuntu

*Si vous souhaitez installer Dojo sur un appareil déjà configuré, vous pouvez ignorer cette étape et passer directement à l’étape 2.*

Après avoir préparé le matériel choisi, il faut maintenant y installer un système d’exploitation. Vous pouvez utiliser pratiquement n’importe quelle distribution Debian, mais je vous recommande d’opter pour une version LTS d’Ubuntu, car c'est parfaitement adapté à notre usage. Voici les étapes à suivre :  

### 1.1. Créer la clé USB amorçable

Depuis un ordinateur déjà fonctionnel (votre machine habituelle), téléchargez l’image ISO d’Ubuntu LTS [sur le site officiel](https://ubuntu.com/download/desktop) (`24.04` au moment de la rédaction de ce tutoriel, mais prenez la plus récente si une autre est disponible).

02

Insérez une clé USB d’au moins 8 Go dans cet ordinateur, puis créez une clé amorçable à l’aide d’un logiciel comme [Balena Etcher](https://etcher.balena.io/). Sélectionnez l’image ISO d’Ubuntu que vous venez de télécharger, choisissez la clé USB comme périphérique cible, puis lancez la création (ayez patience, cela peut prendre plusieurs minutes).

03

Insérez la clé USB amorçable dans le ThinkCentre éteint. Allumez la machine et appuyez immédiatement sur la touche **F12** ou **F10** de votre clavier (cela dépent du modèle) afin d’accéder au menu de démarrage. Sélectionnez votre clé usb comme priorité sur le boot de l'ordinateur.

04

### 1.2. Installer le système d'exploitation

L’écran d’accueil d’Ubuntu apparaît. Choisissez "Try or Install Ubuntu".

05

Puis suivez le processus classique d'installation d'Ubuntu :
- Sélectionnez la langue.
- Indiquez le type de clavier.
- Si vous utilisez un cable RJ45, pas besoin de connecter le Wi-Fi.
- Optez pour "Install Ubuntu" et cochez la case permettant l’installation des logiciels tiers (pilotes Wi-Fi, codecs multimédias).
- Lorsque le programme demande le type d’installation, choisissez "Erase disk and install Ubuntu". **Attention** : cette action effacera intégralement le contenu du disque. Vérifiez que le disque sélectionné correspond bien au SSD NVMe destiné à Dojo.
- Définissez un nom d’utilisateur simple (par exemple "loic").
- Attribuez un nom à la machine (par exemple "dojo-node").
- Choisissez un mot de passe fort et conservez-le précieusement.
- Activez l’option "Demander mon mot de passe pour ouvrir une session" afin de renforcer la sécurité.
- Choisissez votre timezone, puis cliquez sur le bouton "Install".
- Patientez le temps de l'instalation. Une fois terminé, le système redémarre automatiquement.
- Retirez la clé USB amorçale d’installation lorsque l’ordinateur redémarre.

Pour plus de précisions sur le rpocessus d'instaltion d'Ubuntu, vous pouvez consulter notre tutoriel dédié : 

https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. Mise à jour du système

Après le premier démarrage, ouvrez un terminal à l’aide de la combinaison de touches **Ctrl + Alt + T** et exécutez les commandes suivantes :

```bash
sudo apt update
sudo apt upgrade -y
```

06

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

07

### 2.2. Installer les utilitaires indispensables

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

Lors de l’installation, le système peut vous demander une confirmation. Tapez alors sur la touche "y" puis appuyez sur "Entrée".

08

### 2.3. Installer Torsocks

Torsocks permet d’exécuter certaines commandes en passant par le réseau Tor, ce qui améliore la confidentialité des communications.

```bash
sudo apt install torsocks
```

09

### 2.4. Installation de Docker et Docker Compose

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

10

#### Ajout du dépôt officiel Docker

Il faut ensuite indiquer au système où trouver les paquets Docker officiels. Cette commande ajoute un nouveau dépôt à la configuration de votre gestionnaire de paquets.

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```

11

#### Installation de Docker et Docker Compose

Les composants principaux de Docker peuvent maintenant être installés.

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

12

#### Autorisation de l’utilisateur

Par défaut, seules les commandes exécutées avec les droits administrateur peuvent lancer Docker. Pour plus de confort, je vous conseille d’ajouter votre utilisateur courant au groupe "docker". Cela permet d’utiliser Docker sans devoir taper systématiquement `sudo`.

```bash
sudo usermod -aG docker $USER
```

13

## 3. Création d’un utilisateur isolé (optionnel)

Si vous souhaitez améliorer la sécurité de votre système, je vous recommande de créer un utilisateur distinct exclusivement destiné à l’exécution de Dojo. Cette séparation limite les risques : si un problème de sécurité survient dans Dojo, il ne compromettra pas directement votre compte principal, et inversement.

### 3.1. Création du compte utilisateur

La commande suivante crée un nouvel utilisateur nommé "dojo". Cet utilisateur disposera d’un répertoire personnel `/home/dojo` et de l’accès au terminal bash. Il sera également ajouté au groupe sudo pour permettre l’exécution de commandes admin.

```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```

### 3.2. Définition d’un mot de passe robuste

Il est important d’attribuer un mot de passe fort à ce compte. L’idéal est d’utiliser un gestionnaire de mots de passe tel que Bitwarden afin de générer une combinaison longue et difficile à deviner. Si le serveur Dojo est installé sur une machine locale (non accessible à distance), vous pouvez aussi noter ce mot de passe dans un carnet pour ne pas le perdre.

```bash
sudo passwd dojo
```

Le système vous demandera alors de saisir le mot de passe choisi, puis de le confirmer une seconde fois.

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Autorisation de l’utilisateur à utiliser Docker

Pour que l’utilisateur "dojo" puisse lancer les conteneurs nécessaires au fonctionnement de Dojo, il doit être ajouté au groupe Docker. Cela évite d’avoir à précéder chaque commande de `sudo`.

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

Avant d’installer Dojo, il est indispensable de s’assurer que les fichiers proviennent bien du développeur officiel et qu’ils n’ont pas été modifiés. Cette étape repose sur l’utilisation de Tor pour télécharger les fichiers et de PGP pour vérifier leur authenticité.

### 4.1. Importer la clé PGP du développeur

Téléchargez la clé publique du développeur via Tor et importez-la dans votre trousseau local. Cette clé servira à vérifier les signatures associées aux fichiers de Dojo.

```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```

14

### 4.2. Télécharger la dernière version de Dojo

Récupérez l’archive compressée contenant le code source de Dojo. Dans cet exemple, la version la plus récente est la `1.27.0` : modifiez la commande en fonction de [la dernière version présente ici sur le dépôt GitHub officiel](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).

```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```

15

### 4.3. Télécharger les empreintes et leur signature

Les développeurs publient un fichier listant les empreintes numériques des archives, ainsi qu’un fichier signé par leur clé PGP. Téléchargez-les pour pouvoir comparer localement vos fichiers.

```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```

16

### 4.4. Vérifier la signature PGP

Vérifiez que le fichier des empreintes a bien été signé par la clé importée.

```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```

Un résultat correct affiche une signature valide avec la clé `E53AD419B242822F19E23C6D3033D463D6E544F6` et l’adresse associée `dojocoder@pm.me`. Un avertissement peut apparaître précisant que la clé n’est pas certifiée : vous pouvez l'ignorer.

Si en revanche la signature est invalide, arrêtez immédiatement le processus d'installation et recommencez depuis le début.

17

### 4.5. Vérifier l’intégrité de l’archive

Calculez l’empreinte SHA256 du fichier téléchargé puis ouvrez le fichier des empreintes pour comparer les deux valeurs.

```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```

Si les deux empreintes sont identiques, vous avez la garantie que l’archive n’a pas été modifiée. Si elles diffèrent, n’allez pas plus loin et supprimez les fichiers.

18

### 4.6. Extraire et organiser les fichiers

Une fois la vérification réussie, vous pouvez décompresser l’archive et préparer un dossier dédié à l’installation de Dojo.

```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```

19

### 4.7. Nettoyer les fichiers inutiles

Supprimez les fichiers temporaires et les archives devenues inutiles afin de garder votre environnement propre.

```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```

20

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

Ces identifiants doivent être uniques (c'est très important, il ne faut pas utiliser le même mot de passe pour plusieurs services), composés uniquement de chiffres, de lettres majuscules et de lettres minuscules (alphanumériques), et comporter environ 40 caractères pour garantir un haut niveau de sécurité.

### 5.2. Accéder aux fichiers de configuration

Les fichiers de configuration de Dojo se trouvent dans le dossier `conf`. Déplacez-vous dans ce répertoire :

```bash
cd ~/dojo-app/docker/my-dojo/conf/
```

21

### 5.3. Configuration de Bitcoin Core

Ouvrez le fichier de configuration de Bitcoin Core avec l’éditeur de texte nano :

```bash
nano docker-bitcoind.conf.tpl
```

22

Dans ce fichier, renseignez les identifiants générés :

```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```

⚠️ ***Remplacez `your-ID-here` et `your-password-here` par vos propres identifiants (avec un mot de passe fort).***

Ajustez également la taille de la mémoire cache utilisée par Bitcoin Core pour améliorer les performances :

```
BITCOIND_DB_CACHE=2048
```

Pour enregistrer vos modifications et fermer l’éditeur :
- appuyez sur `Ctrl + X`
- tapez `y`
- puis appuyez sur "Entrée"

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

Enregistrez de la même manière (`Ctrl + X`, `y`, "Entrée").

23

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

24

Ensuite, il y a 2 possibilités en fonction de votre configuration. Si Dojo est installé sur une machine distincte de votre ordinateur de tous les jours (sur une machine dédiée, un serveur...), indiquez son adresse IP dans votre réseau local, par exemple :

```
INDEXER_EXTERNAL_IP=192.168.1.157
```

25

Pour connaitre l'adresse IP lcoale de votre machine, dna sun autre terminal, tapez la commande : 

```shell
hostname -I
```

Seconde possibilité : si Dojo est exécuté directement sur votre ordinateur personnel de tous les jours, conservez la valeur par défaut déjà présente dans le fichier de configuration :

```
INDEXER_EXTERNAL_IP=127.0.0.1
```

Enregistrez et quittez l’éditeur (`Ctrl + X`, `y`, "Entrée").

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

26

Activez ensuite l’indexeur local :

```
NODE_ACTIVE_INDEXER=local_indexer
```

Enregistrez et quittez l’éditeur (`Ctrl + X`, `y`, "Entrée").

### 5.7. Gestion des identifiants

Une fois la configuration terminée, il n’est pas nécessaire de conserver tous les identifiants générés. Le seul qui devra absolument être sauvegardé est :

```
NODE_ADMIN_KEY
```

Cet identifiant vous permettra de vous connecter plus tard à l’outil de maintenance de Dojo. Tous les autres identifiants peuvent être supprimés de votre gestionnaire de mots de passe ou de vos notes manuscrites. Ils restent accessibles depuis les fichiers de configuration de Dojo si vous deviez les retrouver dans le futur.

## 6. Installation de Dojo

À cette étape, Dojo va être installé et démarré sur votre machine. L’opération va lancer plusieurs services critiques (Bitcoin Core, l’indexeur Fulcrum, le backend Dojo, etc.) et initier la synchronisation complète de la blockchain Bitcoin. Cette étape peut prendre plusieurs jours selon votre matériel et votre connexion Internet.

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

27

Si ce message ne s’affiche pas, commencez par redémarrer votre machine avec :

```bash
sudo reboot
```

Reconnectez-vous ensuite à votre compte **dojo**, puis relancez la commande de test. Si le problème persiste, cela signifie que Docker n’est pas installé correctement. Dans ce cas, il faudra revenir à l’étape `2.4.` d’installation de Docker et vérifier chaque commande.

### 6.2. Accéder au répertoire d’installation de Dojo

Les scripts nécessaires à l’installation se trouvent dans le dossier `my-dojo`. Déplacez-vous dans ce répertoire :

```bash
cd ~/dojo-app/docker/my-dojo
```

28

Vérifiez avec la commande `ls` que le fichier `dojo.sh` est bien présent. Il s’agit du script principal qui automatise l’installation de Dojo et le lancement de tous ses services.

29

### 6.3. Lancer l’installation

Démarrez l’installation en exécutant le script :

```bash
./dojo.sh install
```

Confirmez l'installation en tapant la touche `y` puis "Entrée".

30

Ce script va :
- télécharger et lancer les conteneurs Docker nécessaires,
- initialiser Bitcoin Core et commencer à synchroniser la blockchain,
- démarrer l’indexeur Fulcrum pour gérer les transactions et les adresses,
- activer le backend Dojo et ses API.

Vous allez voir défiler un flux continu de journaux contenant des mentions de couleur comme `bitcoind`, `soroban`, `nodejs` ou encore `fulcrum`. Ce défilement indique que Dojo fonctionne et commence à exécuter les différents services.

31

### 6.4. Quitter l’affichage des journaux

Les journaux apparaissent en temps réel dans votre terminal. Pour revenir à l’invite de commande tout en laissant Dojo tourner en arrière-plan, tapez :

```
Ctrl + C
```

Ne vous inquiétez pas : arrêter l’affichage des journaux ne stoppe pas les services. Docker continue à exécuter Dojo en arrière-plan (il ne faut évidemment pas arrêter l'ordinateur si vous voulez que l'IBD continue).

### 6.5. Comprendre l’Initial Block Download (IBD)

Dès le démarrage, Bitcoin Core doit télécharger et vérifier l’intégralité de la blockchain depuis 2009. Cette étape est appelée ***Initial Block Download* (IBD)**. Elle est indispensable, car elle permet à votre nœud Dojo de vérifier chaque bloc et transaction Bitcoin de manière indépendante.

La durée de cette synchronisation dépend de plusieurs facteurs :
- la puissance de votre processeur et la quantité de mémoire RAM disponible,
- la vitesse de votre disque,
- le nombre et la qualité des pairs auxquels votre nœud se connecte,
- la vitesse de votre connexion Internet.

En pratique, cette opération prend généralement entre **2 et 7 jours**. Pendant cette période, vous pouvez laisser votre machine tourner en continu. Plus la machine reste allumée, plus vite la synchronisation sera terminée. Je vous conseille de vérifier régulièrement l’état de la synchronisation en consultant les journaux de Bitcoin Core ou en utilisant l’outil de maintenance de Dojo une fois installé (partie suivante).

Pour en savoir plus sur l'IBD, et plus généralement, sur le foncitonnement et le rôle de votre noeud Bitcoin, je vous consielle de consulter ce cours :

https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426
