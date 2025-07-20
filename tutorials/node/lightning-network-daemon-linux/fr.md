---
name: Lightning Network Daemon (Linux)
description: Installer et faire tourner Lightning Network Daemon sur Linux
---

![cover-lightning-network-daemon](assets/cover.webp)

Le réseau Lightning est une deuxième couche de Bitcoin qui permet à ce dernier de prendre des dimensions fulgurantes notamment grâce à la rapidité et aux faibles coûts de transactions proposées.

Dans ce tutoriel nous allons installer l'implémentation Lightning Network Daemon sur notre machine Linux (Distribution Ubuntu 24.04).  

## Qu'est-ce que c'est Lightning Network Daemon ?  

Lightning Network Daemon est une implémentation complète en Go du réseau Lightning. Il a été créé par la société Lightning Labs et vous permet de faire tourner une instance complète d'un nœud Lightning sur votre machine. 
Autrement dit, avec cette implémentation, vous pouvez : 

- **Interagir avec le réseau Lightning** : Grâce aux lignes de commandes, vous pouvez effectuer des processus de création d'un portefeuille Lightning, la gestion des canaux et des routes de paiements, vous avez une multitude de possibilités directement depuis le terminal de votre machine.  
- **Relier un nœud Bitcoin distant ou votre propre instance de Bitcoin Core** : LND vous permet de relier une instance de Bitcoin et de vous en servir comme backend pour votre utilisation, pour utiliser cette implémentation, vous n'aurez pas besoin de faire tourner obligatoirement une instance de Bitcoin Core sur votre machine.


https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Pourquoi avoir son propre nœud Lightning ?  
Lightning est une surcouche de Bitcoin qui vient optimiser le processus de transfert et réduire les frais de transaction. 

En faisant tourner votre nœud Lightning, vous gagnez en souveraineté et en autonomie. Vous êtes maître de vos fonds, gardez à l'esprit : 

"*Pas vos clés, pas vos bitcoins.*"

En ce sens, faire tourner un nœud Lightning augmente la sécurité et l'intégrité de vos données sur les points suivants: 

- **Contrôle total** : Gérez vos propres canaux de paiement, devenez votre propre banque et soyez maître de vos avoirs.
- **Confidentialité**: Effectuez des transactions sans dépendre de tiers afin de préserver votre confidentialité.
- **Apprentissage et autonomie** : Grâce aux commandes `lncli` vous pouvez comprendre mieux les processus sous-jacents de Lightning en vous appliquant depuis votre terminal.
- **Décentralisation** : Participez activement au renforcement et à la décentralisation du réseau Bitcoin / Lightning.  

https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Vous avez deux possibilités pour faire tourner une instance de l'implémentation LND sur notre machine. Nous pouvons configurer l'environnement sur notre machine même afin de pouvoir agir en local ou installer LND à partir d'un conteneur Docker. Ici, nous allons nous concentrer sur la première option, et nous verrons comment procéder avec Docker dans un prochain tutoriel.
## Installer LND à partir du code source

### Prérequis
LND étant écrit en Go, vous devez vous assurer d'avoir l'environnement GoLang et les dépendances nécessaires sur votre machine Linux.  

- **Prérequis Matériel :**
Pour une expérience fluide et sans accro, votre machine devra avoir la capacité nécessaire pour faire tourner votre nœud Lightning LND.  

Il vous faudra : 
1. **8 Go de RAM** pour une fluidité optimale, 
2. **Un processeur multi-core (quad-core ou plus)** pour gérer efficacement les actions de votre nœud, 
3. **Au moins 5 Go d'espace disque** pour un mode réduit (pruned node) et 1To pour faire tourner Bitcoin Core (facultatif si vous utilisez un nœud distant)

- **Installer les dépendances utiles :**
La commande ci-dessous vous permettra d'installer sur votre machine des outils nécessaires pour le bon fonctionnement de LND. Vous aurez entre autres besoin d'une installation de `Git`, un outil de versionning et de `make` qui pourra exécuter et construire l'implémentation LND à partir du code source.

```bash
sudo apt install -y build-essential git make
```

![installation-dependances](assets/fr/01.webp)

- **Installer GoLang sur votre machine Linux**

LND requiert à la date de ce tutoriel la ***version 1.23.6 de Go*** pour son installation. 

Si vous aviez une version antérieure déjà installée, procédez à une suppression de cette version pour la nouvelle installation de Go.
```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go 

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package 

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```

![go-install](assets/fr/02.webp)

- **Configuration de l'environnement Go** 
Dans votre fichier `~/.bashrc`, initialisez les variables d'environnement suivantes pour ajouter Go à votre système Linux.

```bash
# Configuration de l'environnement Go 
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin 

# Appliquer les modifications

source ~/.bashrc
```

- **Vérifier l'installation**
```bash
go version
```

![go-version](assets/fr/03.webp)
### Cloner le dépôt GitHub de LND

Vous allez utiliser git pour avoir une copie du code source de LND en locale sur votre machine 
```bash
git clone https://github.com/lightningnetwork/lnd.git
```
![clone-lnd](assets/fr/04.webp)
### Construire et installer 

L'outil `make` préalablement installé vous permettra de construire un exécutable à partir du code source LND et pouvoir procéder à votre installation.  

```bash
# Acceder au repertoire clonné 
cd lnd 

# construire LND
make 
```

Installer LND sur votre machine 

```bash
# installer LND
make install
```

![make-lnd](assets/fr/06.webp)
- **Vérifier votre installation**

Pour vous assurer que tout s'est bien déroulé, en exécutant cette commande, vous devriez obtenir la version de LND que vous tournez actuellement. 

```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```
![lnd-version](assets/fr/05.webp) 
- **Maintenance et Mise à jour** 

```bash
cd lnd
git pull
make clean && make && make install
```
⚠️ **IMPORTANT** : Il se pourrait que les mises à jour de LND requièrent des versions plus récentes de Go, assurez-vous de mettre votre système à jour afin de ne pas rencontrer de problèmes de dépendances lors de votre installation. 
### Configurer Lightning Network Daemon 

La configuration d'un nœud Lightning LND est similaire à celle de Bitcoin, elle se fait dans un fichier de configuration contenant tous les paramètres de votre nœud. Pour cela, à la racine de votre machine vous pouvez créer un dossier caché `.lnd` puis créer votre fichier de configuration `lnd.conf` dans ce dossier.  

```bash
# Création du ficher 
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```



Dans le fichier de configuration vous pouvez paramétrer votre nœud LND.

```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```

## Comprendre votre configuration

Il est important pour vous de comprendre la configuration minimale que vous devez avoir pour une installation correcte et complète de votre nœud LND.  

En vous basant sur le contenu du fichier `~/.lnd/lnd.conf`, voici le détail des champs: 

- **noseedbackup** : Permet de choisir si vous souhaitez que LND effectue des sauvegardes automatiques de vos portefeuilles.  Définissez cette propriété à `0` vous permet de sauvegarder manuellement les informations de restauration dans un endroit sécurisé personnellement choisi.

- **debuglevel** : Permet de définir le niveau de détails des erreurs et des journaux en cas d'erreurs survenues lors d'une action.  

- **bitcoin.active** : Permet d'indiquer à LND de fonctionner en tant que nœud Bitcoin et d'interagir avec le réseau Bitcoin.

- **bitcoin.mainnet** : Spécifie à LND de se connecter au réseau principal de Bitcoin (mainnet), vous pouvez définir les valeurs `bitcoind.signet` et `bitcoind.regtest` respectivement pour les réseaux Bitcoin Signet et Bitcoin Regtest

- **bitcoin.node** : Spécifie à LND le type de nœud Bitcoin auquel il devra se connecter.

- **bitcoin.rpcuser**  et **bitcoin.rpcpassword** : Représentent.
respectivement les identifiants ( utilisateur , mot de passe)  pour se connecter à votre nœud Bitcoin 

- **bitcoind.zmqpubrawblock** et **bitcoind.zmqpubrawtx** : Définit respectivement les terminaisons ZeroMQ pour recevoir les notifications à propos de nouveaux blocs et des nouvelles transactions présentes sur le réseau Bitcoin.


## Vérifier son installation avec LND 

Vous souhaitez probablement vous assurer que le processus a bien été réussi et que vous vous synchronisez au réseau Lightning pour avoir les informations à jour sur votre nœud.  

Pour démarrer l'implémentation LND et avoir les informations sur votre nœud, rien de plus simple , dans votre terminal, tapez la commande : 
```bash
lnd getinfo
```
![lnd-getinfo](assets/fr/07.webp)
## Effectuer des actions sur LND

Une fois que votre installation terminée et vérifiée, vous pouvez commencer par l'utiliser. 
Retrouvez ci-dessous les commandes essentielles pour débuter.

### Créer un portefeuille 
Votre portefeuille Lightning est la première étape pour toute action pour gérer vos fonds.  

⚠️ **IMPORTANT** : Notez soigneusement votre **seed phrase** de 24 mots. Elle vous sera nécessaire pour récupérer vos fonds en cas de problèmes. 

Sauvegardez également le mot de passe de votre portefeuille afin de pouvoir le débloquer avec la commande `lncli unlock` lorsque vous relancerez votre nœud LND.

```bash
	lncli create
```
![créer-portefeuille](assets/fr/08.webp)
### Vérifier votre solde 

Consultez directement depuis votre terminal, vos comptes :

```bash
lncli walletbalance
```
![solde](assets/fr/09.webp)
### Informations sur votre nœud  

La commande ci-dessous vous permet de connaître les canaux actifs sur votre nœud.

 ```bash
 lncli listchannels
```

Vous pouvez également obtenir la liste des nœuds auquel vous êtes connectés.

```bash
lncli listpeers
```

### Gestion des canaux 

Un canal Lightning vous permet d'avoir une **connexion directe et paire-à-paire avec un autre nœud sur le réseau Lightning**. Dans ce canal, vous pouvez librement échanger des Satoshi à la hauteur de la capacité de ce canal. 

### Se connecter à un nœud 

La connexion à d'autres nœuds Lightning est une action fondamentale si vous voulez participer activement et profiter de la puissance de Lightning.  

Pour vous connecter à un pair (nœud Lightning), vous aurez besoin de trois informations: 
- **La clé publique du nœud** : Elle représente l'identifiant unique de ce nœud dans le réseau Bitcoin ;
- **IP** : L'IP de la machine sur laquelle le nœud est installé ;
- **PORT** :  Le port ouvert sur la machine qui permet la communication avec ce nœud. 

Vous pouvez trouver des nœuds auxquels vous connecter sur [amboss](https://amboss.space/), une plateforme qui recense les informations sur les nœuds Lightning.

```bash 
 # Se connecter à un noeud
 lncli connect <ID_PUBKEY>@<IP>:<PORT>

	 # Un exemple  : Connexion au noeud de Wallet of Satoshi 
 lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```


Assurez-vous de vous connecter à des **nœuds fiables** afin de préserver l'intégrité de votre propre système. Voici quelques recommandations pour une bon choix de vos connexions. 

- **Diversification géographique** : Connectez-vous à des nœuds dans différentes régions.

- **Réputation** : Privilégiez les nœuds avec une bonne disponibilité.

- **Capacité** : Choisissez des nœuds avec une bonne liquidité.

- **Frais** : Vérifiez les frais de routage pratiqués.
### Ouvrir un canal de paiement 
Pour ouvrir un canal de paiement assurez vous de la **connexion avec le nœud** pair puis définir la **capacité** (le montant de satoshis) que vous souhaitez bloquer dans ce canal.  

```bash 
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```
### Créer une facture Lightning  

Une facture Lightning représente une chaine de caractères exprimant votre désir de recevoir des satoshis dans votre portefeuille Lightning. 
Créer des factures Lightning avec votre propre nœud vous permet de protéger vos données (géographiques et personnelles) et vous donne la possibilité d'être 100% autonome sur la gestion de vos fonds. 

```bash 
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```

### Payer une facture Lightning 

```bash 
lncli payinvoice <FACTURE>
```
### Fermer un canal 

Vous avez deux possibilités pour fermer un canal actif sur votre nœud actuellement.  

- **La fermeture coopérative** : Elle signale le souhait de votre nœud de se retirer du canal de paiement et permet de s'assurer de la finition des tâches en cours et de procéder à une sauvegarde des données afin d'éviter des pertes de fonds. 
```
lncli closechannel <ID_CANAL>
```
- **La fermeture forcée** : ⚠️ À éviter si possible, cette action interrompt les processus en cours dans votre canal de paiement et augmente le risque de perte de fonds.
```
lncli closechannel --force <ID_CANAL>
```
## Bonnes pratiques et sécurité de votre nœud LND. 
La sécurité est primordiale lors de l'utilisation d'un nœud Bitcoin/ Lightning. Voici quelques points pour renforcer la sécurité de votre installation : 

- Conservez votre `seed phrase` dans un endroit sécurisé et hors ligne.  

- Faites des sauvegardes régulières du fichier `~/.lnd/channel.backup` : Ce fichier sauvegarde les états de vos canaux chaque fois qu'un nouveau canal est ouvert (ou un ancien canal est fermé) sur votre nœud.
   ⚠️ Il vous permet restaurer les canaux et de récupérer les fonds que vous avez bloqués dans les canaux de paiement en cas de perte de données ou de défaillance de votre nœud  
   
Vous pouvez procéder à la restauration de vos fonds avec la commande ci dessous en spécifiant le chemin de sauvegarde de ce fichier :  
```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```
- Assurez-vous d'avoir bien sauvegardé les mots de restauration et le mot de passe de votre portefeuille Lightning.
- Gardez votre système à jour. 

## Dépannage Courant
### Problèmes fréquents
- **Erreur de connexion à bitcoind** : Vérifiez vos identifiants RPC
- **Synchronisation bloquée** : Vérifiez votre connexion internet
- **Erreur de permission** : Vérifiez les droits du dossier `~/.lnd`


Vous êtes donc à la fin de ce tutoriel, si vous désirez en apprendre plus sur Lightning, nous vous proposons ce cours introductif pour vous permettre de comprendre mieux les concepts et les pratiques sur le réseau Lightning. 


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb




