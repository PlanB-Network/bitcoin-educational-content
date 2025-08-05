---
name: Blockstream App - Onchain
description: Configurer Blockstream App sur mobile et gérer les transactions onchain
---
![cover](assets/cover.webp)
## 1. Introduction
### 1.1 Objectif du tutoriel

- Ce tutoriel explique comment utiliser l'application mobile **Blockstream App** pour gérer un portefeuille Bitcoin **onchain**, c'est-à-dire des transactions directement enregistrées sur la blockchain Bitcoin principale.
- Il couvre les étapes d'installation, de configuration initiale, de création d'un portefeuille logiciel, et les opérations de réception et d'envoi de bitcoins.
- Note : D'autres tutoriels fournis en Annexes couvrent les fonctionnalités Liquid, Watch-Only, et la version desktop.

![image](assets/fr/01.webp)

### 1.2 Public cible

- **Débutants** : Utilisateurs souhaitant gérer leurs bitcoins avec une application mobile intuitive.
- **Utilisateurs intermédiaires** : Personnes cherchant à comprendre les fonctionnalités onchain et les options de confidentialité comme Tor ou SPV.

### 1.3. Rappels sur les hot wallets

- **Hot wallet**, **software wallet**, **wallet mobile**, **portefeuille logiciel** : autant d'appellations pour une application installée sur un smartphone, un ordinateur ou tout appareil connecté à Internet, permettant de gérer et sécuriser les clés privées d’un portefeuille Bitcoin.
- Contrairement aux **hardware wallets** appelés aussi **cold wallets**, qui isolent les clés hors ligne, les portefeuilles logiciels opèrent dans un environnement connecté, ce qui les expose davantage aux cyberattaques.

- **Utilisation recommandée** :
    - Idéal pour gérer des montants modérés de bitcoins, notamment pour les transactions quotidiennes.
    - Convient aux débutants ou aux utilisateurs avec un patrimoine limité, pour qui un hardware wallet peut sembler superflu.

- **Limites** : Moins sécurisés pour stocker des fonds importants ou une épargne à long terme. Dans ce cas, privilégiez un hardware wallet.


## 2. Présentation de Blockstream App

- **Blockstream App** est une application mobile (iOS, Android) et desktop pour gérer des portefeuilles Bitcoin et des actifs sur le réseau Liquid. Acquise par [Blockstream](https://blockstream.com/) en 2016, elle était auparavant nommée *Green Address* puis *Blockstream Green*.
- **Fonctionnalités principales** :
    - Transactions **onchain** sur la blockchain Bitcoin.
    - Transactions sur le réseau **Liquid** (sidechain pour des échanges rapides et confidentiels).
    - Portefeuilles **watch-only** pour surveiller des fonds sans accès aux clés.
    - Options de confidentialité : connexion via **Tor**, connexion à un **nœud personnel** via Electrum, ou vérification **SPV** pour réduire la dépendance aux nœuds tiers.
    - Fonctions **Replace-by-Fee (RBF)** pour accélérer les transactions non confirmées.
- **Compatibilité** : Intègre des hardware wallets comme **Blockstream Jade**.
- **Interface** : Intuitive pour les débutants, avec des options avancées pour les experts.
- **Note** : Ce guide se concentre sur l'utilisation onchain. D'autres tutoriels fournis en Annexes couvrent les fonctionnalités Liquid, Watch-Only, et la version desktop.

## 3. Installer et paramétrer l'application Blockstream App

### 3.1. Téléchargement

- **Pour Android** :
    - Téléchargez [Blockstream App](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) depuis le Google Play Store.
    - Alternative : Installez via le fichier APK disponible sur le [GitHub officiel de Blockstream](https://github.com/Blockstream/green_android).
- **Pour iOS** :
    - Téléchargez [Blockstream App](https://apps.apple.com/us/app/green-bitcoin-wallet/id1402243590) depuis l'App Store.
- **Note** : Assurez-vous de télécharger depuis des sources officielles pour éviter les applications frauduleuses.

### 3.2. Configuration initiale

- **Écran d'accueil** : À la première ouverture, l'application affiche un écran sans portefeuille configuré. Les portefeuilles créés ou importés apparaîtront ici par la suite.

![image](assets/fr/02.webp)

- **Personnalisation des paramètres** : Cliquez sur "Paramètres de l'application", ajustez les options ci-dessous, cliquez sur "Sauvegarder", redémarrez l’application puis créez votre portefeuille.

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

- **Précaution** : Configurez votre portefeuille dans un environnement privé, sans caméras ni observateurs.
- Depuis l’écran d’accueil, cliquez sur "Get Started" :

![image](assets/fr/04.webp)

- Si vous voulez gérer un **cold wallet** (portefeuille hors ligne) : cliquez sur **"Connect Jade"** pour utiliser le hardware wallet Blockstream Jade ou d’autres cold wallets compatibles.

![image](assets/fr/05.webp)

- Vous arrivez à l'écran suivant : 

![image](assets/fr/06.webp)

- (1) **"Setup Mobile Wallet"** : Créer un nouveau portefeuille chaud (hot wallet).
- (2) **"Restore from Backup"** : Importer un portefeuille existant via une phrase mnémonique (12 ou 24 mots). Attention : N’importez pas la phrase d’un cold wallet, car elle serait exposée sur un appareil connecté, annulant sa sécurité.
- (3) **"Watch-Only"** : Importer un portefeuille existant en lecture seule, afin de consulter le solde (par exemple de votre cold wallet) sans exposer la phrase mnémonique. Voir en annexe le tutoriel Watch Only.

**Dans ce tutoriel** : Cliquez sur **"Setup Mobile Wallet"** pour créer un hot wallet. 
Votre wallet est automatiquement créé et la page d'accueil du wallet, ici appelé "My Wallet 5", s'affiche :

![image](assets/fr/07.webp)

**Important** : Blockstream App a simplifié la création d'un wallet en n’affichant pas automatiquement la seed phrase de 12 mots. *Même si le portefeuille est désormais créé en un clic, vous risquez de perdre l'accès à vos fonds si vous ne sauvegardez pas votre seed phrase*.

### 4.2. Sauvegarder la seed phrase

- Sur l'écran d'accueil du wallet, cliquez sur l'onglet "Sécurité", puis sur l'invitation "Back Up" ou le menu "Phrase de récupération" :

![image](assets/fr/08.webp)

La seed phrase de 12 mots sera affichée pour que vous la sauvegardiez.

- Notez votre phrase de récupération avec le plus grand soin. Inscrivez-la sur du papier ou du métal et conservez-la dans un endroit sûr (coffre-fort, lieu hors ligne). Cette phrase est votre seul moyen pour accéder à vos bitcoins en cas de perte de votre appareil ou suppression de l'application.
- Il est important de noter également que toute personne possédant cette phrase peut voler tous vos bitcoins. Ne la stockez jamais numériquement :
	- Pas de capture d’écran
	- Pas de sauvegarde dans le cloud, email ou messagerie
	- Pas de copier/coller (risque d’enregistrement dans le presse-papiers)

**! Ce point est critique**. Pour plus d’informations sur la sauvegarde :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Confirmer la seed phrase

Avant d'envoyer des fonds sur une adresse associée à cette seed phrase, vous devez impérativement tester la sauvegarde de vos 12 mots.

Pour cela nous allons noter une référence, supprimer le wallet, le restaurer avec la sauvegarde, et vérifier que la référence est inchangée.

- Sur l'écran d'accueil du wallet, cliquez sur l'onglet "Paramètres", puis sur "Wallet Details", et copiez la zPub ([clé publique étendue](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602)) :

![image](assets/fr/09.webp)

Nota : une adresse zpub peut être importée dans votre application Blockstream pour la fonction "Watch Only" (voir en Annexe).

- Supprimez l’application, puis restaurez le portefeuille via **"Restore from Backup"** en saisissant la phrase mnémonique, et vérifiez que la zpub est inchangée. Si oui, alors votre sauvegarde est correcte, et vous pouvez envoyer des fonds sur le wallet.

- Pour en savoir plus sur comment effectuer un test de récupération, voici un tutoriel dédié :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5. Sécuriser l'accès à l'application

Verrouillez l'accès à l'application par un code PIN robuste :
- Depuis l’écran d’accueil du wallet, allez dans **"Sécurité"** puis cliquez sur **"PIN"**
- Saisissez et confirmez **un code PIN à 6 chiffres aléatoires**.
   
**Option biométrique** : Disponible pour plus de commodité, mais moins sécurisée qu'un code PIN robuste (risque d’accès non autorisé, ex. : empreinte ou visage scanné pendant le sommeil).
 
**Note** : Le PIN sécurise l’appareil, mais seule la seed phrase permet de récupérer les fonds.



## 5. Utiliser le portefeuille onchain

### 5.1. Recevoir des bitcoins

- Depuis l’écran d’accueil du portefeuille, cliquez sur '"**Transact**" puis **"Recevoir"**.

![image](assets/fr/10.webp)

- L’application affiche une **adresse de réception vierge** (format SegWit v0, commençant par `bc1q...`). Utiliser une nouvelle adresse pour chaque réception de Bitcoin améliore votre confidentialité.

- **Options** :
    - (1) "Bitcoin" : cliquez pour sélectionner un envoi onchain ou via Liquid, et choisir l'actif.
    - (2) Cliquez sur les flèches pour choisir une autre nouvelle adresse liée à cette seed phrase. 
    - (3) Vous pouvez aussi choisir une adresse parmi celles déjà utilisées / affichées, en cliquant sur les trois points en haut à droite puis sur "List of Adresses"
    - (4) Pour demander un montant spécifique, cliquez sur les trois points en haut à droite, sélectionnez "Montant de la demande", et saisissez le montant souhaité. Le QR sera mis à jour, et l'adresse sera remplacée par un URI de paiement Bitcoin.


![image](assets/fr/11.webp)

- Partagez l’adresse/l'URI en cliquant sur "**Partager**", en copiant le texte ou en scannant le QR code.
- **Vérification** : Vérifiez autant que possible l'adresse partagée au destinataire pour éviter les erreurs ou attaques (ex. : malwares modifiant le presse-papiers).

### 5.2. Envoyer des bitcoins

- Depuis l’écran d’accueil du portefeuille, cliquez sur "**Transact**" puis **"Envoyer"** :

![image](assets/fr/12.webp)

- **Saisir les détails** :
    - (1) Entrez l’**adresse du destinataire** en la collant ou en scannant un QR code.
    - (2) Vérifiez l'actif et le compte à partir duquel les fonds sont envoyés.
    - (3) Indiquez le **montant** à envoyer. Vous pouvez choisir l'unité : BTC, satoshis, USD, ...
      Le montant minimal (dush limit) au 03/08/2025 est 546 sats.
    - (4) Sélectionnez les **frais de transaction** :
        - Choisissez parmi les options suggérées (ex. : rapide, moyen, lent) selon l’urgence, une durée de transfert approximative sera affichée.
        - Pour des frais personnalisés, ajustez manuellement le nombre de satoshi par vbytes (consultez [Mempool.space](https://mempool.space/) pour les taux du marché).


![image](assets/fr/13.webp)

- **Vérification** :
    - Vérifiez l’adresse, le montant, et les frais sur l’écran de récapitulatif.
    - Une erreur d’adresse peut entraîner une perte irréversible des fonds. Méfiez-vous des malwares modifiant le presse-papiers.

![image](assets/fr/14.webp)

- **Confirmation** : Faites glisser le bouton "Envoyer" pour signer et diffuser la transaction.
- **Suivi** : Dans l'onglet "Transact" du wallet, la transaction apparaît comme "en attente" jusqu’à confirmation (1 à 6 confirmations) :

![image](assets/fr/15.webp)

- Tant que la transaction n'est pas confirmée, la fonction "Replace by fee" (voir Annexe) vous permet d'accélérer sa prise en charge en augmentant les fees de transaction :

![image](assets/fr/16.webp)


## Annexes

### A1. Autres tutoriels Blockstream

- Utilisation du réseau Liquid

*En cours de révision*

- Importer et suivre un wallet en "Watch Only"

*En cours de révision*

- Version ordinateur

*En cours de révision*


### A2. Explication de Replace-by-Fee (RBF)

**Définition** : Replace-by-Fee (RBF) est une fonctionnalité du réseau Bitcoin qui permet à l'expéditeur d'accélérer la confirmation d'une transaction **onchain** en acceptant de payer des frais plus élevés.

**Limites** :
- RBF n’est pas disponible pour les transactions Liquid ou Lightning.
* La transaction initiale doit être marquée comme RBF-compatible lors de sa création, ce que Blockstream App fait automatiquement.

**Plus d'info :** 
- [Glossaire](https://planb.network/fr/resources/glossary/rbf-replacebyfee)


### A3. Bonnes pratiques

Pour utiliser **Blockstream App** de manière sécurisée et efficace, suivez ces recommandations. Elles vous aideront à protéger vos fonds, optimiser vos transactions, et préserver votre confidentialité sur les réseaux **Bitcoin (onchain)**, **Liquid**, et **Lightning**.

* **Sécurisez votre phrase de récupération** :
	* Tutoriel : Sauvegarder sa phrase mnémonique

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


* **Utilisez l’authentification sécurisée** : 
	* Activez un **code PIN robuste** ou l’**authentification biométrique** (empreinte digitale ou reconnaissance faciale) pour protéger l’accès à l’application.
	* Ne partagez jamais votre PIN ou vos données biométriques.

- **Protégez votre confidentialité** : 
	- Générez une nouvelle adresse pour chaque réception onchain ou Liquid afin de limiter le traçage sur la blockchain.
	- Activez les fonctions "Confidentialité renforcée", "Tor", et "SPV".
	- Pour une confidentialité maximale, connectez votre wallet à votre propre nœud Bitcoin via un serveur Electrum au lieu d’utiliser le nœud public 

* **Choisissez le réseau adapté à vos besoins** : 
	* **Onchain** : Privilégiez pour la conservation à long terme ou les transactions de montants élevés (frais négligeables par rapport au montant).
	* **Liquid** : Utilisez pour des transferts rapides, à faible coût et avec une confidentialité renforcée.
	* **Lightning** : Optez pour des transferts instantanés et très économiques pour de faibles montants. 
  
* **Vérifiez toujours les adresses d'envoi** :
	* Avant d’envoyer des fonds, vérifiez soigneusement l’adresse. Les fonds envoyés à une mauvaise adresse sont perdus à jamais. Utilisez un copier/coller ou le scan de QR code, ne recopiez / modifiez jamais une adresse à la main. 

* **Optimisez les frais** :
	* Pour les transactions onchain, choisissez des frais adaptés (lente, moyenne, rapide) en fonction de l’urgence et de la congestion du réseau.
	* Utilisez Liquid, ou Lightning pour les petits montants.

* **Tenez l'application à jour**


### A4. Ressources supplémentaires

* **Liens officiels :** 
	* **[Site officiel](https://blockstream.com/)**
	* **[Support pour l'application mobile](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : documentation et tchat
	- **[GitHub](https://github.com/Blockstream/green_android)**

* **Explorateurs de blocs :**
	* On chain : **[Mempool.space](https://mempool.space/)**
	* Liquid : **[Blockstream Info](https://blockstream.info/liquid)**
	* Lightning : **[1ML (Lightning Network)](https://1ml.com/)** 

* **Apprentissage et tutoriels :** **[Plan ₿ Network](https://planb.network/)** : 
	* **Sécuriser sa phrase de récupération**

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


- **Liquid Network** :
	- **[Glossaire](https://planb.network/fr/resources/glossary/liquid-network)**

https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727


- **Lightning Network** :
	- **[Glossaire](https://planb.network/fr/resources/glossary/lightning-network)**

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

