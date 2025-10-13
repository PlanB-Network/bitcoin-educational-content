---
name: Pears
description: Comment installer et utiliser des applications sur Pears ?
---

![cover](assets/cover.webp)

Dans ce tutoriel, nous allons apprendre à faire tourner des applications sur **Pears**, une technologie pair-à-pair (P2P) développée par **Holepunch** et soutenue par **Tether**. L’objectif est simple : rendre possible la diffusion et l’utilisation d’applications web sans dépendre d’aucune infrastructure centralisée (ni serveurs, ni hébergeurs, ni intermédiaires). En d’autres termes, même si un fournisseur de cloud ferme ou qu’un pays bloque un domaine, l’application continue de vivre entre les pairs du réseau.

## 1. Qu’est-ce que Pears ?

Pears est à la fois un environnement d’exécution, un outil de développement et une plateforme de déploiement pour des applications pair-à-pair. Cet outil open-source permet de construire, partager et exécuter des logiciels sans serveur et sans infrastructure, directement entre utilisateurs. Concrètement, cela signifie qu’au lieu d’héberger une application sur un serveur central, chaque utilisateur devient un nœud du réseau : il partage une partie de l’application et des données avec d’autres pairs. L’ensemble du système forme un réseau distribué où chaque instance coopère pour maintenir le service accessible.

![Image](assets/fr/01.webp)

Cette approche repose sur un ensemble de briques logicielles modulaires développées par Holepunch :
- **Hypercore** : un journal distribué qui garantit la cohérence et la sécurité des données sans base de données centrale.
- **Hyperbee** : un indexeur au-dessus d’Hypercore, qui permet d’organiser et de parcourir les données de façon efficace.
- **Hyperdrive** : un système de fichiers distribué qui est utilisé pour stocker et synchroniser les fichiers d’une application entre les pairs.
- **Hyperswarm** et **HyperDHT** : des couches réseau qui permettent la découverte et la connexion entre les pairs dans le monde entier, sans serveur central.
- **Secretstream** : un protocole de chiffrement E2E pour sécuriser les échanges entre deux pairs.

En combinant ces composants, Pears permet de créer des applications autonomes, chiffrées et distribuées, où chaque utilisateur participe activement au réseau. Cette architecture décentralisée élimine les coûts d’infrastructure, les risques de censure et les SPOF ("*Single Point of Failure*").

## 2. Origine et philosophie du projet

Pears est développé par Holepunch, une entreprise fondée par Mathias Buus et Paolo Ardoino (CEO de Tether et CTO de Bitfinex), avec la mission d’étendre la logique du pair-à-pair au-delà de Bitcoin. Leur ambition est de bâtir l’"*Internet des pairs*", où chaque application peut fonctionner sans autorisation, sans serveurs, et sans intermédiaire. Holepunch est déjà à l’origine de **Keet**, une application de visioconférence et de messagerie entièrement P2P.

## 3. Comment installer Pears sur Linux (Debian)

L’installation de Pears sur un Debian est relativement simple, mais nécessite quelques prérequis que nous allons détailler dans cette section.

*Si vous utilisez Windows, vous pouvez passer directement à l'étape 4.*

### 3.1. Mettre à jour le système

Avant toute chose, il est important de s’assurer que votre système est à jour.

```bash
sudo apt update && sudo apt upgrade -y
```

![Image](assets/fr/02.webp)

### 3.2. Installer les dépendances

Pears repose sur certaines bibliothèques système, notamment `libatomic1`, utilisée par le moteur d’exécution JavaScript Bare. Installez-la avec la commande suivante :

```bash
sudo apt install -y libatomic1 curl git
```

![Image](assets/fr/03.webp)

### 3.3. Installer Node.js et npm via NVM

Pears est distribué via *npm*, le gestionnaire de paquets *Node.js*. Même si Pears ne dépend pas directement de *Node.js* pour fonctionner, celui-ci est nécessaire à l’installation. La méthode recommandée pour installer *Node.js* sur Linux est *NVM* (*Node Version Manager*), qui permet de gérer plusieurs versions de Node en parallèle.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```

![Image](assets/fr/04.webp)

Ensuite, rechargez votre terminal pour activer *NVM* :

```bash
source ~/.bashrc
```

![Image](assets/fr/05.webp)

Vérifiez que *NVM* est bien installé :

```bash
nvm --version
```

![Image](assets/fr/06.webp)

Installez ensuite une version stable de *Node.js* (par exemple la LTS actuelle) :

```bash
nvm install --lts
```

![Image](assets/fr/07.webp)

Vérifiez les installations de *Node.js* et *npm* :

```bash
node -v
npm -v
```

![Image](assets/fr/08.webp)

### 3.4. Installer Pears avec npm

Une fois *npm* disponible, vous pouvez installer Pears CLI globalement sur votre système. Cela vous permettra d’exécuter la commande `pear` depuis n’importe quel répertoire.

```bash
npm install -g pear
```

![Image](assets/fr/09.webp)

### 3.5. Initialiser Pears

Après l’installation, lancez simplement la commande suivante dans votre terminal :

```bash
pear
```

Lors du premier démarrage, Pears va se connecter au réseau pair-à-pair pour télécharger les composants nécessaires. Ce processus ne nécessite aucun serveur central : les fichiers sont obtenus directement depuis d’autres pairs.  

![Image](assets/fr/10.webp)

Une fois le téléchargement terminé, relancez la commande pour vérifier que tout fonctionne :

```bash
pear
```

![Image](assets/fr/11.webp)

Si tout est correctement installé, l’aide de Pears s’affichera avec la liste des commandes disponibles.

### 3.6. Tester Pears avec Keet

Pour vérifier que Pears est pleinement opérationnel, vous pouvez lancer une application P2P déjà disponible sur le réseau, comme Keet, le logiciel de messagerie et visioconférence open-source de Holepunch.

```bash
pear run pear://keet
```

Cette commande charge l’application Keet directement depuis le réseau Pears, sans passer par un serveur central. Si Keet se lance correctement, cela signifie que votre installation de Pears est pleinement fonctionnelle.

![Image](assets/fr/12.webp)

Votre système Linux est désormais prêt à exécuter et héberger des applications pair-à-pair avec Pears.

## 4. Comment installer Pears sur Windows

L’installation de Pears sur Windows est tout aussi simple que sur Linux, mais nécessite quelques outils spécifiques.

*Si vous utilisez Linux, vous pouvez passer directement à l'étape 5.*

### 4.1. Ouvrir PowerShell en mode administrateur

Avant toute chose, lancez PowerShell avec les droits administrateur :
- Cliquez sur le menu Démarrer ;
- Tapez PowerShell ;
- Faites un clic droit sur "*Windows PowerShell*" ;
- Sélectionnez "*Exécuter en tant qu’administrateur*".

![Image](assets/fr/15.webp)

### 4.2. Télécharger NVS

Pears s’installe via *npm*, le gestionnaire de paquets de *Node.js*. Sur Windows, la méthode recommandée par Holepunch consiste à utiliser *NVS* (*Node Version Switcher*), plus stable que *NVM* sur ce système.

Dans PowerShell, exécutez la commande suivante pour installer la dernière version de *NVS* :

```PowerShell
winget install jasongin.nvs
```

![Image](assets/fr/16.webp)

### 4.3. Installer Node.js

Après l’installation, redémarrez PowerShell, puis saisissez la commande suivante :

```powershell
nvs
```

Vous devriez voir apparaître la liste des versions de *Node.js* disponibles. Sélectionnez la première en appuyant sur la touche `a` de votre clavier.

![Image](assets/fr/17.webp)

*Node.js* est bien installé.

![Image](assets/fr/18.webp)

### 4.4. Vérifier les installations

Assurez-vous que *Node.js* et *npm* sont accessibles :

```powershell
node -v
npm -v
```

Les deux commandes doivent renvoyer un numéro de version.

![Image](assets/fr/19.webp)

### 4.5. Installer Pears avec npm

Une fois *Node.js* et *npm* disponibles, installez **Pears CLI** globalement sur votre système :

```powershell
npm install -g pear
```

Cela installera le binaire `pear` dans votre répertoire *npm* global.

![Image](assets/fr/20.webp)

### 4.6. Vérifier et initialiser Pears

Une fois l’installation terminée, exécutez :

```powershell
pear
```

Lors du premier lancement, Pears téléchargera automatiquement les composants nécessaires depuis le réseau pair-à-pair. Ce processus peut durer quelques instants.

![Image](assets/fr/21.webp)

Si tout s’est bien déroulé, vous devriez voir apparaître l’aide du CLI Pears avec la liste des sous-commandes disponibles (run, seed, info...).

### 4.7. Tester Pears avec Keet

Pour vérifier que Pears est pleinement opérationnel, vous pouvez lancer une application P2P déjà disponible sur le réseau, comme Keet, le logiciel de messagerie et visioconférence open-source de Holepunch.

```bash
pear run pear://keet
```

Cette commande charge l’application Keet directement depuis le réseau Pears, sans passer par un serveur central. Si Keet se lance correctement, cela signifie que votre installation de Pears est pleinement fonctionnelle.

![Image](assets/fr/22.webp)

Votre système Windows est désormais prêt à exécuter et héberger des applications pair-à-pair avec Pears.

## 5. Comment utiliser une application sur Pears ?

Une fois Pears installé et fonctionnel, vous pouvez directement exécuter l'application de votre choix grâce à la commande suivante :

```bash
pear run pear://[KEY]
```

Remplacez simplement `[KEY]` par la clé de l’application que vous souhaitez utiliser.

![Image](assets/fr/13.webp)

Pour apprendre à exécuter notre plateforme Plan ₿ Academy sur Pears, consultez ce tutoriel complet :

https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

Et pour découvrir comment utiliser l’application de messagerie Keet que vous venez de lancer sur Pears, consultez ce tutoriel :

https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b
