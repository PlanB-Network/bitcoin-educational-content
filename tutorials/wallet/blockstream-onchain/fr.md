---
name: Blockstream Mobile - Onchain
description: Configurer Blockstream Mobile et gérer les transactions onchain
---
![cover](assets/cover.webp)
## 1. Introduction
### 1.1 Objectif du tutoriel

- Ce tutoriel explique comment utiliser l'application mobile **Blockstream App** pour gérer un portefeuille Bitcoin **onchain**, c'est-à-dire des transactions directement enregistrées sur la blockchain Bitcoin principale.
- Il couvre les étapes d'installation, de configuration initiale, de création d'un portefeuille logiciel, et les opérations de réception et d'envoi de bitcoins.
- Note : D'autres tutoriels fournis en Annexes couvrent les fonctionnalités Liquid, Watch-Only, XXXXXXXXXXX multisig, et la version desktop.
![image](assets/fr/01.webp)
### 1.2 Public cible

- **Débutants** : Utilisateurs souhaitant gérer leurs bitcoins avec une application mobile intuitive.
- **Utilisateurs intermédiaires** : Personnes cherchant à comprendre les fonctionnalités onchain et les options de confidentialité comme Tor ou SPV.

### 1.3. Rappels sur les hot wallet

- **Hot wallet**, **software wallet**, **wallet mobile**, **portefeuille logiciel** : autant d'appellations pour une application installée sur un smartphone, un ordinateur ou tout appareil connecté à Internet, permettant de gérer et sécuriser les clés privées d’un portefeuille Bitcoin.
- Contrairement aux **hardware wallets** appelés aussi **cold wallets**, qui isolent les clés hors ligne, les portefeuilles logiciels opèrent dans un environnement connecté, ce qui les expose davantage aux cyberattaques.

- **Utilisation recommandée** :
    - Idéal pour gérer des montants modérés de bitcoins, notamment pour les transactions quotidiennes.
    - Convient aux débutants ou aux utilisateurs avec un patrimoine limité, pour qui un hardware wallet peut sembler superflu.

- **Limites** : Moins sécurisés pour stocker des fonds importants ou une épargne à long terme. Dans ce cas, privilégiez un hardware wallet.


## 2. Présentation de Blockstream App

- **Blockstream App** est une application mobile (iOS, Android) et desktop pour gérer des portefeuilles Bitcoin et des actifs sur le réseau Liquid. Acquise par [Blockstream](https://blockstream.com/) en 2016, elle s'est précédemment appelée Green Adress puis Blockstream Green.
- **Fonctionnalités principales** :
    - Transactions **onchain** sur la blockchain Bitcoin.
    - Transactions sur le réseau **Liquid** (sidechain pour des échanges rapides et confidentiels).
    - Portefeuilles **watch-only** pour surveiller des fonds sans accès aux clés.
    - **2FA multisig** : XXXXXXXXXXX Portefeuille sécurisé par deux signatures avec un timelock pour récupérer les fonds sans Blockstream si nécessaire.
    - Options de confidentialité : connexion via **Tor**, connexion à un **nœud personnel** via Electrum, ou vérification **SPV** pour réduire la dépendance aux nœuds tiers.
    - Fonctions avancées : **Replace-by-Fee (RBF)**, étiquetage des transactions, et contrôle des pièces (UTXO).
- **Compatibilité** : Intègre des hardware wallets comme **Blockstream Jade**, **Ledger Nano S/X**, et **Trezor**.
- **Interface** : Intuitive pour les débutants, avec des options avancées pour les experts.
- **Note** : Ce guide se concentre sur l'utilisation onchain. D'autres tutoriels fournis en Annexes couvrent les fonctionnalités Liquid, Watch-Only, XXXXXXXXXXX multisig, et la version desktop.

## 3. Installer et paramétrer l'application Blockstream App

### 3.1. Téléchargement

- **Pour Android** :
    - Téléchargez [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) depuis le Google Play Store.
    - Alternative : Installez via le fichier APK disponible sur le [GitHub officiel de Blockstream](github.com/Blockstream/green_android).
- **Pour iOS** :
    - Téléchargez [Blockstream App](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590) depuis l'App Store.
- **Note** : Assurez-vous de télécharger depuis des sources officielles pour éviter les applications frauduleuses.

### 3.2. Configuration initiale

- **Écran d'accueil** : À la première ouverture, l'application affiche un écran sans portefeuille configuré. Les portefeuilles créés ou importés apparaîtront ici par la suite.
![image](assets/fr/02.webp)
- **Personnalisation des paramètres** : Cliquez sur "Paramètres de l'application", ajustez les options décrites ci-dessous selon vos besoins, cliquez sur "Sauvegarder", redémarrez l’application pour appliquer les changements, puis créez votre portefeuille.
![image](assets/fr/03.webp)
#### 3.2.1. Confidentialité renforcée (Android uniquement)

- **Fonction** : Désactive les captures d'écran, masque les aperçus d'application dans le gestionnaire de tâches, et verrouille l’accès dès que le téléphone est verrouillé.
- **Pourquoi ?** : Protège vos données contre les accès physiques non autorisés ou les malwares capturant l’écran.
#### 3.2.2. Connexion via Tor

- **Fonction** : Route le trafic réseau via **Tor**, un réseau anonyme qui chiffre vos connexions.
- **Pourquoi ?** : Masque votre adresse IP et protège votre vie privée, idéal si vous ne faites pas confiance à votre réseau (Wi-Fi public, par exemple).
- **Inconvénient** : Peut ralentir l’application en raison du chiffrement.
- **Recommandation** : Activez Tor si la confidentialité est une priorité, mais testez la vitesse de connexion.
#### 3.2.3. Connexion à un nœud personnel

- **Fonction** : Connecte l’application à votre propre **nœud Bitcoin complet** via un serveur **Electrum**.
- **Pourquoi ?** : Offre un contrôle total sur les données blockchain, éliminant la dépendance aux serveurs de Blockstream.
- **Prérequis** : Un nœud Bitcoin configuré.
- **Recommandation** : Utilisateurs avancés souhaitant une souveraineté maximale.

#### 3.2.4. Vérification SPV

- **Fonction** : Utilise la **Simplified Payment Verification (SPV)** pour vérifier directement certaines données blockchain sans télécharger l’intégralité de la chaîne.
- **Pourquoi ?** : Réduit la dépendance au nœud par défaut de Blockstream, tout en restant léger pour les appareils mobiles.
- **Inconvénient** : Moins sécurisé qu’un nœud complet, car il repose sur des nœuds tiers pour certaines informations.
- **Recommandation** : Activez SPV si vous ne pouvez pas utiliser un nœud personnel, mais préférez un nœud complet pour une sécurité optimale.



## 4. Créer un portefeuille Bitcoin onchain

### 4.1. Lancer la création

- **Note** : Configurez votre portefeuille dans un environnement privé, sans caméras ni observateurs.
- Depuis l’écran d’accueil, cliquez sur "Get Started" :
![image](assets/fr/04.webp)
- Si vous voulez non pas utiliser le hot wallet de Blockstream App, mais utiliser Blockstream App pour gérer votre cold wallet, cliquez sur "Connect Jade". Jade est le cold wallet développé par Blockstream, mais l'écran suivant vous permet de connecter d'autres cold wallets pourvu d'avoir le bluetooth : 
![image](assets/fr/05.webp)


- Vous arrivez à l'écran suivant : 
![image](assets/fr/06.webp)
	- (1) Pour créer un nouveau hot wallet, cliquez sur "Setup Mobile Wallet"
	- (2) Pour importer un compte existant à partir de votre seed phrase (phrase mnémonique de 12 ou 24 mots), cliquez sur "Restore from backup"
	  Nota : si vous avez un cold wallet, n'importez pas le compte en renseignant votre seed phrase, car elle serait alors stockée sur un appareil connecté à internet, annulant tout l'intérêt de votre cold wallet. A la place, connectez votre cold wallet à l'application comme indiqué à l'étape précédente.
	- (3) L'option "Watch-only" vous permet d'importer un compte existant, mais en lecture seule, sans pouvoir déplacer les fonds : ceci vous permet par exemple de consulter le solde de votre coldwallet sans que la seed phrase soit exposée. 

Dans ce tutoriel, nous nous concentrons sur la création d'un nouveau hot wallet (1).
En cliquant sur ""Setup Mobile Wallet", votre wallet est automatiquement créé et la page d'accueil du wallet, ici appelé "My Wallet 5", s'affiche : 
![image](assets/fr/07.webp)

! Blockstream a simplifié la création d'un wallet en supprimant l'affichage de votre phrase de récupération (seed phrase, phrase mnémonique) et l'étape de vérification : c'est plus simple, mais cela signifie aussi que l'utilisateur n'est plus invité à la sauvegarder précieusement !

Il faut donc absolument passer à cette étape avant d'envoyer des fonds sur ce wallet, sous risque de ne plus jamais y avoir accès. 


### 4.2. Sauvegarder la phrase mnémonique

- Sur l'écran d'accueil du wallet, cliquez sur l'onglet "Sécurité", puis sur l'invitation "Back Up" ou le menu "Phrase de récupération" : 
![image](assets/fr/08.webp)
La seed phrase sera affichée pour que vous la sauvegardiez.

- Notez votre phrase de récupération avec le plus grand soin. Inscrivez-la sur du papier ou du métal et conservez-la dans un endroit sûr (coffre-fort, lieu hors ligne). Cette phrase est votre seul moyen pour accéder à vos bitcoins en cas de perte de votre appareil ou suppression de l'application.
- Il est important de noter également que toute personne possédant cette phrase peut voler tous vos bitcoins. Ne la stockez jamais numériquement :
	- Pas de capture d’écran
	- Pas de sauvegarde dans le cloud, email ou messagerie
	- Pas de copier/coller (risque d’enregistrement dans le presse-papiers)

**! Ce point est critique**. Pour obtenir plus d'aide :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


**Cette phrase mnémonique donne un accès complet et non restreint à tous vos bitcoins.** N'importe qui en possession de cette phrase peut subtiliser vos fonds, même sans accès physique à votre téléphone.

Elle permet de restaurer l'accès à vos bitcoins en cas de perte, de vol ou de casse de votre téléphone. Il est donc très important de la sauvegarder soigneusement **sur un support physique (pas numérique)** et de la stocker dans un endroit sécurisé. Vous pouvez l'inscrire sur un bout de papier, ou bien pour plus de sécurité, si ce portefeuille est important, je vous recommande de la graver sur un support en acier inoxydable afin de la protéger contre les risques d'incendies, d'inondations ou d'écroulements (pour un portefeuille chaud destiné à sécuriser une petite quantité de bitcoins, une simple sauvegarde sur papier est probablement suffisante).

Cliquez sur "Afficher la phrase de récupération" pour voir les mots.
- **Avertissement** : Cette phrase donne un accès total à vos bitcoins. Ne la stockez jamais numériquement (pas de photos ni cloud) et ne la partagez pas.
- **Sauvegarde** : Inscrivez-la sur un support physique (papier ou acier inoxydable pour les portefeuilles importants).


### 4.4. Confirmer la phrase mnémonique

Avant d'envoyer des fonds sur une adresse associée à cette seed phrase, il faut absolument tester la sauvegarde de vos 12 mots que vous venez d'effectuer. Pour cela nous allons noter une référence, puis supprimer le wallet, le restaurer avec la sauvegarde, et vérifier que la référence est inchangée.

- Sur l'écran d'accueil du wallet, cliquez sur l'onglet "Paramètres", puis sur "Wallet Details", et copiez la zPub
![image](assets/fr/09.webp)
Nota : une adresse zpub peut être importée dans votre application Blockstream pour la fonction "Watch Only"

- Supprimez l’application, restaurez le portefeuille avec la phrase mnémonique, et vérifiez que la zpub est inchangée. Si oui, alors votre sauvegarde est correcte, et vous pouvez envoyer des fonds sur le wallet.


### 4.5. Sécuriser l'accès à l'application

Il est fortement conseillé de verrouiller l'accès à l'application par un code PIN robuste ou une authentification biométrique.
Bien que l'authentification biométrique soit pratique et rapide, il y a eu des cas où un Bitcoiner endormi a laissé quelqu'un scanner son visage / coller son empreinte pour accéder à son téléphone, et à ses fonds.

- Sur l'écran d'accueil du wallet, cliquez sur l'onglet "Sécurité", puis sur "Biometrics" ou "PIN".
- Choisissez un **code PIN à 6 chiffres** aléatoire pour sécuriser l’accès local.
- **Note** : Le PIN protège l’appareil, mais la phrase mnémonique est requise pour la récupération.
-