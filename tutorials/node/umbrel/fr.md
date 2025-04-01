---
name: Umbrel
description: Découvrez et installez Umbrel - Votre noeud bitcoin et votre serveur domestique
---

![cover](assets/cover.webp)

## Introduction

### Qu'est-ce qu'un nœud Bitcoin ?

Un nœud Bitcoin est un ordinateur qui participe au réseau Bitcoin en exécutant le logiciel Bitcoin Core ou un client alternatif. Son rôle est essentiel pour le fonctionnement et la sécurité du réseau :

- **Stockage de la blockchain** : Il maintient une copie complète et à jour de la blockchain Bitcoin
- **Vérification des transactions** : Il valide chaque transaction et bloc selon les règles du protocole
- **Diffusion des informations** : Il partage les nouvelles transactions et blocs avec les autres nœuds
- **Participation au consensus** : Il contribue à l'application des règles du réseau

Exécuter votre propre nœud Bitcoin est une étape cruciale vers la souveraineté financière, offrant plusieurs avantages essentiels :

- **Confidentialité** : Diffusez vos transactions sans révéler vos informations à des tiers
- **Résistance à la censure** : Personne ne peut vous empêcher d'utiliser Bitcoin
- **Vérification indépendante** : Plus besoin de faire confiance aux nœuds des autres pour vérifier vos transactions
- **Participation au consensus** : Contribuez à l'application des règles du réseau Bitcoin
- **Soutien au réseau** : Devenez un participant actif dans la distribution et la décentralisation du réseau

### Umbrel : Une solution simple pour exécuter un nœud Bitcoin

Umbrel est un système d'exploitation open source qui simplifie l'installation et la gestion d'un nœud Bitcoin. Il transforme également votre ordinateur en un serveur domestique personnel et privé, permettant d'héberger facilement :

- Un nœud Bitcoin complet
- Des applications Bitcoin essentielles (Electrs, Mempool.space)
- D'autres services personnels (stockage cloud, streaming, VPN, etc.)

Avec son interface utilisateur élégante et intuitive, Umbrel rend accessible à tous l'auto-hébergement de services, tout en gardant le contrôle total de vos données.

## Options d'installation d'Umbrel

Umbrel propose deux façons principales d'utiliser leur solution : une option clé en main (Umbrel Home) et une version open source gratuite (UmbrelOS).

![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)

### Umbrel Home : La solution clé en main

Umbrel Home est un serveur domestique pré-configuré, spécialement conçu pour une expérience optimale. Cette solution matérielle tout-en-un comprend :

**Caractéristiques matérielles**
- Processeur performant optimisé pour le self-hosting
- Stockage SSD haute vitesse pré-installé
- Système de refroidissement silencieux
- Design compact et élégant
- Ports USB et Ethernet intégrés

**Avantages exclusifs**
- Installation plug-and-play : branchez et c'est parti
- Support premium avec assistance dédiée
- Mises à jour automatiques garanties
- Assistant de migration intégré
- Garantie matérielle complète
- Support complet de toutes les fonctionnalités

**Prix** : 399€ (prix susceptible de varier selon les périodes)

### UmbrelOS : La version open source

UmbrelOS est la version gratuite et open source du système d'exploitation Umbrel. Cette solution flexible vous permet d'utiliser votre propre matériel tout en bénéficiant des fonctionnalités essentielles d'Umbrel.

**Avantages**
- Totalement gratuit
- Code source ouvert et vérifiable
- Liberté de choix du matériel
- Possibilité de personnalisation avancée

**Plateformes supportées**
- Raspberry Pi 5 : Solution populaire et abordable
- Systèmes x86 : Pour PC ou serveur standard
- Machine virtuelle : Pour tester ou utiliser sur infrastructure existante

**Limitations**
- Support communautaire uniquement
- Certaines fonctionnalités avancées réservées à Umbrel Home
- Configuration initiale plus technique
- Performances dépendantes du matériel choisi

Cette version est idéale pour :
- Les utilisateurs techniques
- Ceux qui possèdent déjà du matériel compatible
- Les personnes souhaitant apprendre et expérimenter
- Les développeurs voulant contribuer au projet

Liens d'installation officiels :
- [Installation sur Raspberry Pi 5](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Installation sur système x86](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems) 
- [Installation sur machine virtuelle](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)

Dans ce tutoriel, nous nous concentrerons sur l'installation d'UmbrelOS sur un Raspberry Pi 5, mais les principes de base restent similaires pour d'autres plateformes.

## Installation d'Umbrel OS sur Raspberry Pi 5

### Composants nécessaires

Pour cette installation, vous aurez besoin de :

- Un Raspberry Pi 5 (4 Go ou 8 Go de RAM)
- Une alimentation officielle Raspberry Pi (crucial pour la stabilité !)
- Une carte microSD (32 Go minimum)
- Un lecteur de carte microSD
- Un SSD externe pour le stockage des données
- Un câble Ethernet
- Un câble USB pour connecter le SSD

### Étapes d'installation

**Téléchargement d'UmbrelOS**

![Téléchargement UmbrelOS](assets/fr/01.webp)
- Rendez-vous sur le [site officiel](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Téléchargez la dernière version d'UmbrelOS pour Raspberry Pi 5

**Installation de Balena Etcher**

![Téléchargement Balena Etcher](assets/fr/02.webp)
- Téléchargez et installez [Balena Etcher](https://www.balena.io/etcher/) sur votre ordinateur

**Préparation de la carte microSD**

![Insertion carte microSD](assets/fr/03.webp)
- Insérez votre carte microSD dans le lecteur de votre ordinateur

**Flashage de l'image**

![Flashage UmbrelOS](assets/fr/04.webp)
- Lancez Balena Etcher
- Sélectionnez l'image UmbrelOS téléchargée
- Choisissez votre carte microSD comme destination
- Cliquez sur "Flash!" et attendez la fin du processus
- Éjectez la carte en toute sécurité

**Installation de la carte microSD**

![Installation microSD](assets/fr/05.webp)
- Insérez la carte microSD dans votre Raspberry Pi 5

**Connexion des périphériques**

![Connexion périphériques](assets/fr/06.webp)
- Connectez le SSD externe à un port USB disponible
- Branchez le câble Ethernet entre le Pi et votre routeur

**Mise sous tension**

![Démarrage du Pi](assets/fr/07.webp)
- Branchez l'alimentation officielle Raspberry Pi
- Attendez quelques minutes que le système démarre

**Premier accès**

![Accès interface web](assets/fr/08.webp)
- Sur un appareil connecté au même réseau, ouvrez votre navigateur
- Accédez à l'interface web d'Umbrel via : `http://umbrel.local`
  
   ![Page d'accueil Umbrel](assets/fr/09.webp)

Si `umbrel.local` ne fonctionne pas, vous devrez trouver l'adresse IP de votre Raspberry Pi sur votre réseau local. Vous pouvez :
- Consulter l'interface de votre routeur
- Utiliser un scanner de réseau comme nmap
- Utiliser la commande `arp -a` dans le terminal de votre ordinateur

## Premier pas sur Umbrel

Une fois votre Umbrel démarré et accessible via votre navigateur, suivez ces étapes pour commencer :

### Configuration initiale

**Création de votre compte**

![Création compte](assets/fr/10.webp)
- Choisissez un nom d'utilisateur
- Définissez un mot de passe sécurisé
- Ces identifiants seront nécessaires pour accéder à votre Umbrel

**Confirmation du compte**

![Confirmation compte](assets/fr/11.webp)
- Cliquez sur "Next" pour accéder à votre tableau de bord

**Découverte de l'interface**

![Interface Umbrel](assets/fr/12.webp)
- Vous accédez à l'App Store d'Umbrel
- Découvrez les nombreuses applications disponibles
- Commençons par installer les applications essentielles pour Bitcoin

### Installation des applications Bitcoin

**Bitcoin Node**

![Bitcoin Node](assets/fr/13.webp)
- Première application à installer
- Télécharge et vérifie l'intégralité de la blockchain Bitcoin

**Electrs**

![Installation Electrs](assets/fr/14.webp)
- Serveur Electrum permettant la connexion de wallets Bitcoin
- Se synchronise avec votre nœud Bitcoin

**Mempool**

![Installation Mempool](assets/fr/15.webp)
- Interface de visualisation de la blockchain
- Permet de suivre les transactions et les blocs en temps réel

## Suivre une transaction avec Mempool.space

Mempool.space est un explorateur de blockchain open source qui offre une visualisation en temps réel du réseau Bitcoin. Il vous permet de suivre vos transactions et de comprendre comment fonctionne la propagation des transactions sur le réseau.

### Comprendre le mempool et les confirmations

Le "mempool" (memory pool) est comme une salle d'attente virtuelle où toutes les transactions Bitcoin non confirmées sont stockées avant d'être incluses dans un bloc. Voici le parcours d'une transaction :

1. **Diffusion** : Lorsque vous envoyez une transaction, elle est d'abord diffusée sur le réseau Bitcoin
2. **Attente dans le mempool** : Elle attend d'être sélectionnée par un mineur en fonction de ses frais
3. **Première confirmation** : Un mineur l'inclut dans un bloc (1ère confirmation)
4. **Confirmations supplémentaires** : Chaque nouveau bloc miné après celui contenant votre transaction ajoute une confirmation

Le nombre de confirmations recommandé dépend du montant :
- Pour les petits montants : 1-2 confirmations peuvent suffire
- Pour les montants importants : 6 confirmations sont généralement considérées comme très sûres

### Explorer l'interface de Mempool.space

1. **La page d'accueil** vous présente une vue d'ensemble du réseau Bitcoin :
   - Les blocs récemment minés
   - Les estimations de frais pour différentes priorités
   - L'état actuel du mempool

![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)

2. **Recherche d'une transaction** : Pour suivre une transaction spécifique, collez son identifiant (TXID) dans la barre de recherche en haut de la page.

![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)

### Analyser les détails d'une transaction

Une fois votre transaction trouvée, Mempool.space vous présente une analyse complète :

1. **Informations essentielles** :
   - Statut (confirmée ou non)
   - Frais payés (en sats/vB)
   - Estimation du délai de confirmation

![Détails des frais et statut de la transaction](assets/fr/25.webp)

2. **Structure de la transaction** :
   - Représentation visuelle des entrées et sorties
   - Liste détaillée des adresses impliquées
   - Montants transférés

3. **Données techniques** :
   - Poids de la transaction
   - Taille virtuelle
   - Format et version utilisés
   - Autres métadonnées spécifiques

![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)

### Avantages d'utiliser Mempool.space sur Umbrel

1. **Confidentialité** : Vos requêtes passent par votre propre nœud
2. **Indépendance** : Pas besoin de faire confiance à un service tiers
3. **Fiabilité** : Accès aux données même en cas de panne des explorateurs publics

Grâce à cette application, vous pouvez surveiller efficacement vos transactions, comprendre comment les frais affectent la vitesse de confirmation, et obtenir une meilleure compréhension du fonctionnement du réseau Bitcoin.

## Connexion d'un wallet Bitcoin à votre nœud

### Configuration d'Electrs

**Connexion locale**

![Connexion locale](assets/fr/18.webp)
- Pour une utilisation sur votre réseau local
- Plus rapide et plus simple à configurer

**Connexion distante via Tor**

![Connexion Tor](assets/fr/19.webp)
- Pour accéder à votre nœud depuis n'importe où
- Plus sécurisé et privé

### Connexion avec Sparrow Wallet

**Accès aux paramètres**

![Paramètres Sparrow](assets/fr/20.webp)
- Ouvrez Sparrow Wallet
- Allez dans Préférences > Serveur
- Cliquez sur "Modifier la connexion existante"

**Choix du type de connexion**

Sparrow propose trois modes de connexion :

***Public Server***
- Connexion à des serveurs publics (ex: blockstream.info, mempool.space)
- Simple mais moins privé

***Bitcoin Core***
- Connexion directe à un nœud Bitcoin
- Privé mais plus lent

***Private Electrum***
- Connexion à votre serveur Electrs
- Combine confidentialité et performance

**Configuration d'Electrs**

Choisissez votre type de connexion en utilisant les informations affichées dans l'application Electrs que nous avons vue précédemment :

Dans les deux cas, laissez les options "Use SSL" et "Use proxy" décochées.

**Connexion locale**
   Hôte : umbrel.local
   Port : 50001

**Connexion distante (Tor)**
   Hôte : [votre-adresse-onion]
   Port : 50001
   
La connexion via Tor est nécessaire si vous souhaitez accéder à votre nœud en dehors de votre réseau local.

![Configuration connexion](assets/fr/21.webp)
Pour plus d'informations sur le logiciel Sparrow Wallet, nous avons un tutoriel complet : 
https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Conclusion

Votre Umbrel est maintenant prêt à être utilisé. Vous participez activement au réseau Bitcoin tout en gardant le contrôle total de vos données. N'hésitez pas à explorer les nombreuses autres applications disponibles dans l'App Store d'Umbrel pour étendre les capacités de votre serveur domestique.

## Ressources utiles

### Documentation officielle
- [Site officiel Umbrel](https://umbrel.com)
- [Documentation Umbrel](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)

### Applications Bitcoin
- [Bitcoin Core](https://bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://mempool.space)
- [Sparrow Wallet](https://sparrowwallet.com)

### Communauté
- [Forum Umbrel](https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Umbrel](https://twitter.com/umbrel)


