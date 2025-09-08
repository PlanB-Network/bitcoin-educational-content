---
name: Blockstream App - Liquid
description: Comment configurer Blockstream App et utiliser le réseau Liquid
---
![cover](assets/cover.webp)
## 1. Introduction
### 1.1 Objectif du tutoriel

- Ce tutoriel explique comment utiliser l'application mobile **Blockstream App** pour gérer un portefeuille **Bitcoin Liquid**, c'est-à-dire des transactions directement enregistrées sur la side chain "Liquid" de Bitcoin.
- Il couvre les étapes d'installation, de configuration initiale, de création d'un portefeuille logiciel, et les opérations de réception et d'envoi de bitcoins sur Liquid.
- Note : D'autres tutoriels fournis en Annexes couvrent les fonctionnalités Onchain, Watch-Only, et la version desktop.

### 1.2 Public cible

- **Débutants** : Utilisateurs souhaitant gérer leurs bitcoins avec une application mobile intuitive, intégrant le réseau Liquid.
- **Utilisateurs intermédiaires** : Personnes cherchant à comprendre les fonctionnalités onchain et les options de confidentialité comme Tor ou SPV.

### 1.3 Présentation de Liquid

**Liquid** est une **sidechain** de Bitcoin, développée par **[Blockstream](https://blockstream.com/liquid/)**, conçue pour offrir des transactions plus rapides, plus confidentielles et des fonctionnalités avancées, tout en restant connectée à la blockchain Bitcoin principale.

Une sidechain est une blockchain indépendante qui fonctionne en parallèle de Bitcoin, utilisant un mécanisme appelé **two-way peg** (ancrage bilatéral). Ce système permet de verrouiller des bitcoins sur la blockchain principale pour créer des **Liquid-Bitcoins (L-BTC)**, des tokens qui circulent sur le réseau Liquid tout en conservant une parité de valeur avec les bitcoins d'origine. Les fonds peuvent être ramenés sur la blockchain Bitcoin à tout moment.

![image](assets/fr/17.webp)


- **(1) Peg-in** : Les bitcoins (BTC) sont verrouillés sur la blockchain principale par la fédération Liquid. En contrepartie, un montant équivalent de Liquid-Bitcoins (L-BTC), assurant la parité entre les deux chaînes, est émis sur la blockchain Liquid et envoyé à l'utilisateur.

- **(2) Transactions indépendantes** : Les transactions peuvent se dérouler simultanément et indépendamment sur la blockchain principale (BTC) et la sidechain Liquid (L-BTC), selon les besoins de l'utilisateur.

- **(3) Peg-out** : L'utilisateur renvoie des Liquid-Bitcoins (L-BTC) à la fédération Liquid. La fédération déverrouille alors un montant équivalent de bitcoins (BTC) sur la blockchain principale et les transfère à l'utilisateur.

Liquid repose sur une **fédération** de participants de confiance (exchanges, entreprises Bitcoin reconnues) qui gèrent la validation des blocs et l'ancrage bilatéral. Contrairement à la blockchain Bitcoin, qui est décentralisée et repose sur des mineurs, Liquid est un réseau **fédéré**, ce qui signifie que sa sécurité et sa gouvernance dépendent de ces participants. Bien que cela implique un compromis sur la décentralisation, cela permet des performances optimisées et des fonctionnalités avancées.

![image](assets/fr/18.webp)

##### Pourquoi utiliser Liquid ?

- **Vitesse** : Les transactions sur Liquid sont confirmées en environ **1 minute**, contre 10 minutes ou plus pour les transactions onchain, grâce à des blocs générés toutes les minutes par une fédération de validateurs.
- **Confidentialité renforcée** : Liquid utilise des **Confidential Transactions**, qui masquent le montant et le type d'actif transféré, rendant les transactions plus privées (bien que les adresses restent visibles).
- **Frais réduits** : Les transactions sur Liquid sont généralement moins coûteuses, ce qui les rend idéales pour les transferts fréquents ou de petits montants.
- **Actifs multiples** : En plus des L-BTC, Liquid prend en charge l'émission d'autres actifs numériques, comme des stablecoins ou des tokens, utilisables dans des applications spécifiques.
- **Cas d'usage** : Liquid est particulièrement adapté pour les échanges entre plateformes, les paiements rapides, ou les applications nécessitant des contrats intelligents, tout en restant lié à la sécurité de Bitcoin.

**Note** : Ce tutoriel se concentre sur l'utilisation de Liquid via Blockstream App. Vous trouverez des ressources en annexe pour une compréhension approfondie du réseau Liquid.

### 1.4. Rappels sur les hot wallets

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
- **Note** : Ce guide se concentre sur l'utilisation onchain. D'autres tutoriels fournis en Annexes couvrent les fonctionnalités Onchain, Watch-Only, et la version desktop.


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
- (3) **"Watch-Only"** : Importer un portefeuille existant en lecture seule, afin de consulter le solde (par exemple de votre cold wallet) sans exposer la phrase mnémonique. Voir en annexe le tutoriel "Watch Only".

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

### 4.3. Vérifier la seed phrase

Avant d'envoyer des fonds sur une adresse associée à cette seed phrase, vous devez impérativement tester la sauvegarde de vos 12 mots. 
Pour cela nous allons noter une référence, supprimer le wallet, le restaurer avec la sauvegarde, et vérifier que la référence est inchangée.

- Sur l'écran d'accueil du wallet, cliquez sur l'onglet "Paramètres", puis sur "Wallet Details", et copiez la zPub ([clé publique étendue](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)) :

![image](assets/fr/09.webp)

Nota : une adresse zpub peut être importée dans votre application Blockstream pour la fonction "Watch Only" (voir en Annexe).

- Supprimez l’application, puis restaurez le portefeuille via **"Restore from Backup"** en saisissant la phrase mnémonique, et vérifiez que la zpub est inchangée. Si oui, alors votre sauvegarde est correcte, et vous pouvez envoyer des fonds sur le wallet.

- Pour en savoir plus sur comment effectuer un test de récupération, voici un tutoriel dédié :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Sécuriser l'accès à l'application

Verrouillez l'accès à l'application par un code PIN robuste :
- Depuis l’écran d’accueil du wallet, allez dans **"Sécurité"** puis cliquez sur **"PIN"**
- Saisissez et confirmez **un code PIN à 6 chiffres aléatoires**.
   
**Option biométrique** : Disponible pour plus de commodité, mais moins sécurisée qu'un code PIN robuste (risque d’accès non autorisé, ex. : empreinte ou visage scanné pendant le sommeil).
 
**Note** : Le PIN sécurise l’appareil, mais seule la seed phrase permet de récupérer les fonds.



## 5. Utiliser le portefeuille Liquid

### 5.1. Recevoir des bitcoins "L-BTC"

Pour recevoir des Liquid-Bitcoins (L-BTC), plusieurs options sont disponibles. Vous pouvez demander à quelqu’un de vous en envoyer directement en partageant une adresse de réception Liquid, ce qui est détaillé ci-dessous.

Alternativement, échangez vos bitcoins onchain ou via le réseau Lightning contre des L-BTC en utilisant [un bridge tel que Boltz](https://boltz.exchange/) : entrez votre adresse de réception Liquid, effectuez le paiement selon votre préférence, et recevez vos L-BTC.

- Depuis l’écran d’accueil du portefeuille, cliquez sur '"**Transact**" puis **"Recevoir"**.

![image](assets/fr/19.webp)

- L’application affiche par défaut une **adresse de réception vierge, onchain** (format SegWit v0, commençant par `bc1q...`). Cliquez sur "Bitcoin" pour sélectionner des **Liquid bitcoin** :

![image](assets/fr/20.webp)

- **Options** :
	- (1) Cliquez sur les flèches pour choisir une autre nouvelle adresse liée à cette seed phrase. 
    - (2) Vous pouvez aussi choisir une adresse parmi celles déjà utilisées / affichées, en cliquant sur les trois points en haut à droite puis sur "List of Adresses"
    - (3) Pour demander un montant spécifique, cliquez sur les trois points en haut à droite, sélectionnez "Montant de la demande", et saisissez le montant souhaité. Le QR sera mis à jour, et l'adresse sera remplacée par un URI de paiement Bitcoin. 

![image](assets/fr/21.webp)

- Partagez l’adresse/l'URI en cliquant sur "**Partager**", en copiant le texte ou en scannant le QR code.
- **Vérification** : Vérifiez autant que possible l'adresse partagée au destinataire pour éviter les erreurs ou attaques (ex. : malwares modifiant le presse-papiers).

### 5.2. Envoyer des bitcoins

- Depuis l’écran d’accueil du portefeuille, cliquez sur "**Transact**" puis **"Envoyer"** :

![image](assets/fr/22.webp)

- **Saisir les détails** :
    - (1) Entrez l’**adresse du destinataire** en la collant ou en scannant un QR code.
    - (2) Vérifiez l'actif et le compte à partir duquel les fonds sont envoyés.
    - (3) Indiquez le **montant** à envoyer. Vous pouvez choisir l'unité : L-BTC, L-satoshis, USD, ...

![image](assets/fr/23.webp)

- **Vérification** :
    - Vérifiez l’adresse, le montant, et les frais sur l’écran de récapitulatif.
    - Une erreur d’adresse peut entraîner une perte irréversible des fonds. Méfiez-vous des malwares modifiant le presse-papiers.
    
![image](assets/fr/24.webp)

- **Confirmation** : Faites glisser le bouton "Envoyer" pour signer et diffuser la transaction.
- **Suivi** : Dans l'onglet "Transact" du wallet, la transaction apparaît comme "Non confirmée", puis "Confirmée", puis "Complétée" :

![image](assets/fr/25.webp)

- Le temps entre 2 blocks est de 1 minute sur Liquid, la transaction est donc être rapidement confirmée puis complétée.


## Annexes

### A1. Autres tutoriels Blockstream App

Utilisation du réseau Onchain

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Importer et suivre un wallet en "Watch Only"

https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Version Desktop (ordinateur)

https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Bonnes pratiques

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


### A3. Ressources supplémentaires

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


