---
name: Blockstream App - Desktop
description: Comment utiliser son hardware wallet avec Blockstream App sur ordinateur ?
---
![cover](assets/cover.webp)

## 1. Introduction

### 1.1 Objectif du tutoriel

- Ce tutoriel explique comment utiliser le logiciel **Blockstream App** sur ordinateur pour gérer un portefeuille Bitcoin **onchain** avec un **hardware wallet**, permettant des transactions sécurisées enregistrées sur la blockchain Bitcoin principale.
- Il couvre les étapes d'installation, de configuration initiale, de connexion d’un hardware wallet, et les opérations de réception et d’envoi de bitcoins onchain.
- Note : D'autres tutoriels fournis en Annexes couvrent les fonctionnalités Liquid, Watch-Only, et l’application mobile.

### 1.2 Public cible

- **Débutants** : Utilisateurs souhaitant gérer leurs bitcoins avec un logiciel desktop sécurisé et un hardware wallet.
- **Utilisateurs intermédiaires** : Personnes cherchant à comprendre l’utilisation d’un hardware wallet pour les transactions onchain et les options de confidentialité comme Tor ou SPV.

### 1.3. Rappels sur les hardware wallets

- **Hardware wallet**, **cold wallet** : Un appareil physique qui stocke les clés privées hors ligne, offrant un niveau de sécurité élevé contre les cyberattaques, contrairement aux **hot wallets** (portefeuilles logiciels sur appareils connectés).
- **Utilisation recommandée** :
    - Idéal pour sécuriser des montants importants ou une épargne à long terme.
    - Convient aux utilisateurs prioritaires de la sécurité, souhaitant protéger leurs fonds contre les risques liés aux appareils connectés.
- **Limites** : Nécessite un logiciel comme Blockstream App pour consulter les soldes, générer des adresses, et diffuser des transactions signées par le hardware wallet.

## 2. Présentation de Blockstream App

- **Blockstream App** est une application mobile (iOS, Android) et desktop pour gérer des portefeuilles Bitcoin et des actifs sur le réseau Liquid. Acquise par Blockstream en 2016, elle s’appelait _GreenAddress_, a été renommée _Blockstream Green_ (2019), et s’appelle aujourd’hui _Blockstream app_ (2025).
- **Fonctionnalités principales** :
    - Transactions **onchain** sur la blockchain Bitcoin.
    - Transactions sur le réseau **Liquid** (sidechain pour des échanges rapides et confidentiels).
    - Portefeuilles **watch-only** pour surveiller des fonds sans accès aux clés.
    - Options de confidentialité : connexion via **Tor**, connexion à un **nœud personnel** via Electrum, ou vérification **SPV** pour réduire la dépendance aux nœuds tiers.
    - Fonctions **Replace-by-Fee (RBF)** pour accélérer les transactions non confirmées.
- **Compatibilité** : Intègre des hardware wallets comme **Blockstream Jade**.
- **Interface** : Intuitive pour les débutants, avec des options avancées pour les experts.
- **Note** : Ce guide se concentre sur l’utilisation onchain avec un hardware wallet sur la version desktop. D’autres tutoriels fournis en Annexes couvrent l'utilisation sur application mobile, pour les fonctionnalités onchain, Liquid, et Watch-Only.

## 3. Installer et paramétrer Blockstream App Desktop

### 3.1. Téléchargement

- Rendez-vous sur le [site officiel](https://blockstream.com/app/) et cliquez sur "_Download Now_". Téléchargez la version correspondant à votre système d’exploitation (Windows, macOS, Linux).
- **Note** : Assurez-vous de télécharger depuis la source officielle pour éviter les logiciels frauduleux.

### 3.2. Configuration initiale

- **Écran d'accueil** : À la première ouverture, l’application affiche un écran sans portefeuille configuré. Les portefeuilles créés ou importés apparaîtront ici par la suite.

![image](assets/fr/02.webp)

- **Personnalisation des paramètres** : Cliquez sur l’icône des paramètres en bas à gauche, ajustez les options ci-dessous, puis quittez l’interface pour poursuivre.

![image](assets/fr/03.webp)

#### 3.2.1. Paramètres généraux

- Dans le menu Paramètres, cliquez sur "**General**".
- **Fonction** : Modifiez la langue du logiciel et activez les fonctionnalités expérimentales si souhaité.

![image](assets/fr/04.webp)

#### 3.2.2. Connexion via Tor

- Dans le menu Paramètres, cliquez sur "**Network**".
- **Fonction** : Route le trafic réseau via **Tor**, un réseau anonyme qui chiffre vos connexions.
- **Pourquoi ?** : Masque votre adresse IP et protège votre vie privée, idéal si vous ne faites pas confiance à votre réseau (Wi-Fi public, par exemple).
- **Inconvénient** : Peut ralentir l’application en raison du chiffrement.
- **Recommandation** : Activez Tor si la confidentialité est une priorité, mais testez la vitesse de connexion.

![image](assets/fr/05.webp)

#### 3.2.3. Connexion à un nœud personnel

- Dans le menu Paramètres, cliquez sur "**Custom servers and validation**".
- **Fonction** : Connecte l’application à votre propre **nœud Bitcoin complet** via un serveur **Electrum**.
- **Pourquoi ?** : Offre un contrôle total sur les données blockchain, éliminant la dépendance aux serveurs de Blockstream.
- **Prérequis** : Un nœud Bitcoin configuré.
- **Recommandation** : Utilisateurs avancés souhaitant une souveraineté maximale.

![image](assets/fr/06.webp)

https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. Vérification SPV

- Dans le menu Paramètres, cliquez sur "**Custom servers and validation**".
- **Fonction** : Utilise la **Simplified Payment Verification (SPV)** qui télécharge les en-têtes de blocs et vérifie vos transactions par preuves d’inclusion (Merkle), sans stocker la blockchain complète.
- **Pourquoi ?** : Réduit la dépendance au nœud par défaut de Blockstream, tout en restant léger pour les appareils.
- **Inconvénient** : Moins sécurisé qu’un nœud complet, car il repose sur des nœuds tiers pour certaines informations.
- **Recommandation** : Activez SPV si vous ne pouvez pas utiliser un nœud personnel, mais préférez un nœud complet pour une sécurité optimale.

![image](assets/fr/07.webp)

## 4. Connecter un hardware wallet à Blockstream App

### 4.1. Considérations préalables

#### 4.1.1. Pour les utilisateurs de Ledger

- Blockstream Green ne prend en charge que l’application **Bitcoin Legacy** sur les appareils Ledger (Nano S, Nano X).
- Étapes à suivre dans **Ledger Live** avant de connecter votre appareil :
	1. Allez dans **"Paramètres"** → **"Fonctionnalités expérimentales"** et activez le **mode développeur**.
	2. Accédez à **"My Ledger"** → **"Catalogue d'apps"**, puis installez l’application **Bitcoin Legacy**
	3. Ouvrez l’application **Bitcoin Legacy** sur votre Ledger avant de lancer Blockstream Green pour établir la connexion.
- **Note** : Assurez-vous que votre Ledger est déverrouillé avec votre code PIN et que l’application Bitcoin Legacy est active lors de la connexion.

#### 4.1.2. Initialisation d’un hardware wallet

- Si votre hardware wallet (Ledger, Trezor, ou Blockstream Jade) n’a jamais été utilisé (ni avec Blockstream Green, ni avec un autre logiciel comme Ledger Live), vous devrez d’abord l’initialiser. Cette étape comprend, dans un environnement sécurisé, sans caméras ni observateurs :
	1. **Génération de la seed phrase / phrase mnémonique** (12, 18 ou 24 mots) : Notez-la soigneusement sur un papier.
	2. **Vérification de la seed phrase** : Testez l'importation du wallet à partir des mots notés, par exemple en vérifiant la clé publique étendue. À réaliser avant d'envoyer des fonds sur le wallet et de sécuriser définitivement la seed phrase.
	3. **Sécurisation de la seed phrase** : Stockez la phrase sur un support physique (papier ou métal) et dans un endroit sûr. Ne la conservez jamais numériquement (pas de capture d’écran, cloud, ou messagerie).
- **Important** : La seed phrase est votre seul moyen de récupérer vos fonds en cas de perte ou de dysfonctionnement de l’appareil. Toute personne y ayant accès peut voler vos bitcoins.
- **Ressources** pour la sauvegarde et la vérification de la seed phrase :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Configuration pour ce tutoriel :

- Nous considérerons que le hardware wallet a déjà été initialisé avec une seed phrase et un code PIN de verrouillage.
- Nous considérons que le hardware wallet n’a jamais été connecté à Blockstream App, ce qui nécessite la création d'un nouveau compte. Si le hardware wallet a déjà été utilisé avec Blockstream App, le compte apparaîtra automatiquement à l’ouverture de l’application.

### 4.2. Lancer la connexion

- Depuis l’écran d’accueil, cliquez sur "**Setup a New Wallet**", puis validez les conditions générales d'utilisation et cliquez sur "**Get Started**" :

![image](assets/fr/08.webp)

- Sélectionnez l’option "**On Hardware Wallet**" :

![image](assets/fr/09.webp)

- Si vous utilisez un **Blockstream Jade**, cliquez sur le bouton correspondant. Sinon, sélectionnez "**Connect a different Hardware Device**" :

![image](assets/fr/10.webp)

- Branchez votre hardware wallet à l’ordinateur via USB et sélectionnez-le dans Blockstream App :

![image](assets/fr/22.webp)

- Patientez pendant que Blockstream App importe les informations de votre portefeuille :

![image](assets/fr/23.webp)

### 4.3. Créer un compte

- Si votre hardware wallet a déjà été utilisé avec Blockstream App, votre compte apparaîtra automatiquement dans l’interface après l’importation. Sinon, créez un compte en cliquant sur "**Create Account**" :

![image](assets/fr/24.webp)

- Choisissez "**Standard**" pour configurer un portefeuille Bitcoin classique :

![image](assets/fr/25.webp)

- Une fois le compte créé, vous accédez à l’interface principale de votre portefeuille :

![image](assets/fr/26.webp)



## 5. Utiliser le portefeuille onchain avec un hardware wallet

### 5.1. Recevoir des bitcoins

- Depuis l’écran principal du portefeuille, cliquez sur "**Receive**" :

![image](assets/fr/27.webp)

- L’application affiche une **adresse de réception vierge**. Utiliser une nouvelle adresse pour chaque réception améliore votre confidentialité. Cliquez sur "**Copy address**" pour copier l’adresse ou laissez l'expéditeur scanner le QR code affiché :

![image](assets/fr/12.webp)

**Options** :
- (1) Cliquez sur les flèches pour générer une nouvelle adresse liée à votre portefeuille.
- (2) Pour demander un montant spécifique, cliquez sur "**More options**" puis sur "**Request Amount**". Le QR sera mis à jour, et l'adresse sera remplacée par un URI de paiement Bitcoin de type : `bitcoin:bc1q...?amount=0.00001`

![image](assets/fr/13.webp)

- (3) Pour réutiliser une adresse précédente, cliquez sur "**More options**" puis sur "**List of addresses**" :

![image](assets/fr/14.webp)

- **Vérification** : Vérifiez soigneusement l’adresse partagée pour éviter les erreurs ou attaques (ex. : malwares modifiant le presse-papiers).
- Une fois la transaction diffusée sur le réseau, elle apparaîtra dans votre portefeuille. Attendez 1 à 6 confirmations pour considérer la transaction comme immuable.

![image](assets/fr/28.webp)

### 5.2. Envoyer des bitcoins

- Depuis l’écran principal du portefeuille, cliquez sur "**Send**".

![image](assets/fr/29.webp)

- **Saisir les détails** :
    - (1) Vérifiez que l’actif sélectionné est **Bitcoin** (onchain).
    - (2) Entrez l’**adresse du destinataire** en la collant ou en scannant un QR code avec votre webcam.
    - (3) Indiquez le **montant** à envoyer (en BTC, satoshis, ou autre unité).


![image](assets/fr/16.webp)

- Sélectionnez les **frais de transaction** (optionnel) :
	- Choisissez parmi les options suggérées (rapide, moyen, lent) selon l’urgence, avec une estimation du temps de confirmation.
	- Pour des frais personnalisés, ajustez manuellement le nombre de satoshis par vbyte. Ils sont indiqués sur l'écran d'accueil. Vous pouvez aussi consulter [Mempool.space](https://mempool.space/).

![image](assets/fr/17.webp)

- **Sélection manuelle des UTXOs** (optionnel) : Cliquez sur "**Manual coin selection**" pour choisir les UTXOs spécifiques à utiliser dans la transaction.

![image](assets/fr/18.webp)

- **Vérification préliminaire** : Vérifiez l’adresse, le montant, et les frais sur l’écran de récapitulatif, puis cliquez sur "**Confirm transaction**". En réalité, la transaction ne sera pas diffusée au réseau tant que vous ne l'aurez pas signée avec votre hardware wallet, lui seul possédant les clés secrètes associées aux adresses sur lesquelles les UTXO (satoshis) vont être prélevés.

![image](assets/fr/19.webp)

- **Vérification finale et signature** : Assurez-vous que tous les paramètres de la transaction sont corrects **sur l'écran de votre hardware wallet**, puis signez la transaction à l'aide de celui-ci. Une erreur d’adresse peut entraîner une perte irréversible des fonds.

- **Diffusion** : Une fois signée, Blockstream App diffuse automatiquement la transaction sur le réseau Bitcoin. 

![image](assets/fr/20.webp)

- **Suivi** : 
	- La transaction apparaît dans l’écran d'accueil du wallet comme "en attente" jusqu’à confirmation.
	- Tant que la transaction n’est pas confirmée, la fonction **Replace-by-Fee (RBF)** peut être utilisée pour accélérer la confirmation en augmentant les frais (voir Annexe).

![image](assets/fr/21.webp)

## Annexes

### A1. Autres tutoriels Blockstream

- Utilisation du réseau Liquid :

https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

- Importer et suivre un portefeuille en "Watch-Only" :

https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

- Utilisation de Blockstream App sur mobile (hot wallet) :

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Explication de Replace-by-Fee (RBF)

- **Définition** : Replace-by-Fee (RBF) est une fonctionnalité du réseau Bitcoin qui permet à l’expéditeur d’accélérer la confirmation d’une transaction **onchain** en augmentant les frais.
- **Limites** :
    - RBF n’est pas disponible pour les transactions Liquid ou Lightning.
    - La transaction initiale doit être marquée comme RBF-compatible, ce que Blockstream App fait automatiquement.
- Pour plus d'informations, consultez [notre glossaire](https://planb.network/resources/glossary/rbf-replacebyfee).

### A3. Bonnes pratiques

- **Sécurisez votre phrase de récupération** :
    - Sauvegardez la phrase mnémonique de votre hardware wallet sur un support physique (papier, métal) dans un lieu sûr.
    - Ne la stockez jamais numériquement (cloud, email, capture d’écran).
    - Tutoriel : Sauvegarder sa phrase mnémonique :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

- **Protégez votre confidentialité** :
    
    - Générez une nouvelle adresse pour chaque réception onchain.
    - Activez **Tor** ou **SPV** pour limiter le traçage.
    - Connectez-vous à votre propre nœud Bitcoin via Electrum pour une souveraineté maximale.
- **Vérifiez toujours les adresses d’envoi** :
    
    - Vérifiez l’adresse sur l’écran de votre hardware wallet avant de signer.
    - Utilisez un copier/coller ou un QR code pour éviter les erreurs manuelles.
- **Optimisez les frais** :
    
    - Ajustez les frais en fonction de l’urgence et de la congestion du réseau (consultez [Mempool.space](https://mempool.space/)).
    - Utilisez Liquid ou Lightning pour des transactions rapides et économiques si elles ne nécessitent pas la sécurité onchain.
- **Mettez à jour le logiciel** :
    
    - Gardez Blockstream App et le firmware de votre hardware wallet à jour pour bénéficier des dernières fonctionnalités et correctifs de sécurité.

### A4. Ressources supplémentaires

- **Liens officiels** :
    - [Site officiel](https://blockstream.com/)
    - [Support pour Blockstream App](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/) : documentation et chat
    - [GitHub](https://github.com/Blockstream/green_qt)

- **Explorateurs de blocs** :
    - Onchain : [Mempool.space](https://mempool.space/)
    - Liquid : [Blockstream Info](https://blockstream.info/liquid)
    - Lightning : [1ML (Lightning Network)](https://1ml.com/)

- **Sécuriser sa phrase de récupération :**

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

- **Liquid Network** :

[Glossaire](https://planb.network/fr/resources/glossary/liquid-network)

https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727

- **Lightning Network** :

[Glossaire](https://planb.network/fr/resources/glossary/lightning-network)

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
