---
name: BIP-85
description: Comment utiliser le BIP-85 pour générer plusieurs seedphrases à partir d'une seed principale ?
---
![cover](assets/cover.webp)

## 1. Comprendre le BIP-85

### 1.1 Qu’est-ce que le BIP-85 ?

Le BIP-85 est une fonction avancée qui permet de créer plusieurs **seed phrases secondaires** à partir d’une **seed phrase principale**.

Chaque seed phrase secondaire permet de créer un portefeuille Bitcoin totalement indépendant. Ces portefeuilles peuvent être utilisés pour différents besoins : un hot wallet sur mobile, un portefeuille pour un proche, un portefeuille d’épargne séparé, etc.

Toutes les seed phrases secondaires sont **dérivées mathématiquement**, mais il est **impossible de remonter à la seed phrase principale** depuis une secondaire. Cela garantit une séparation complète entre chaque portefeuille.

Tant que vous avez accès à votre seed phrase principale (et à la passphrase associée si vous en utilisez une), vous pouvez régénérer **à l’identique** n’importe quelle seed phrase secondaire, sans avoir besoin de la sauvegarder séparément.

### 1.2 Pourquoi utiliser BIP-85 ?

BIP-85 est utile si vous voulez :

- Créer plusieurs portefeuilles Bitcoin indépendants sans multiplier les sauvegardes
- Gérer vos fonds selon différents usages (épargne, dépenses, famille, projets)
- Être le garant de sauvegardes pour des proches (fonction "Uncle Jim")
- Supprimer un portefeuille sans perdre l’accès à ses fonds
- Simplifier votre sécurité : une seule seed phrase principale à protéger

### 1.3 Avantages par rapport à BIP-32

Avec BIP-32, une seule seed phrase permet de générer une hiérarchie complète de comptes et d’adresses Bitcoin grâce à des chemins de dérivation (par exemple : `m/44'/0'/0'/0/0`). Chaque chemin peut représenter un compte distinct, mais **tous restent liés à la même seed phrase**. Ainsi, si cette seed phrase est compromise, **l’ensemble des comptes dérivés devient accessible**.

Avec le BIP-85, à partir d’une seed phrase principale, on peut générer plusieurs seed phrases secondaires totalement indépendantes : **si l’une de ces seeds secondaires est compromise, l’attaquant ne pourra jamais remonter à la seed principale ni accéder aux autres portefeuilles**.
Cela permet une stratégie de compartimentation des risques :

- Vous pouvez utiliser une seed secondaire pour un hot wallet ou un usage temporaire, en acceptant une exposition plus élevée.
- Même si ce hot wallet est compromis, vos autres fonds, protégés par d’autres seeds secondaires ou conservés hors ligne, **restent en sécurité**.

En revanche, pour BIP-32 comme pour BIP-85, si la seed principale est compromise, **tous les fonds sont vulnérables**. Il est donc crucial de la protéger avec le plus haut niveau de sécurité.

![image](assets/fr/02.webp)
## 2. Cas d’usages pratiques de BIP-85

BIP-85 permet de créer plusieurs portefeuilles Bitcoin à partir d’une seule seed phrase principale, chacun avec sa propre seed phrase secondaire. Voici cinq cas d’usage pratiques pour organiser et sécuriser vos fonds Bitcoin. Chaque cas explique pourquoi utiliser BIP-85 est plus pratique que de gérer plusieurs comptes avec une seule seed phrase via BIP-32.

### 2.1 Limiter le risque d'un portefeuille moins sécurisé

- **Scénario** : Vous utilisez un portefeuille "hot wallet" (installé sur un appareil connecté à internet), pour des transactions quotidiennes.
- **Solution BIP-85** : Vous créez une seed phrase secondaire dédiée à ce portefeuille.
- **Avantage par rapport à BIP-32** : Vous évitez d’importer la seed phrase principale sur votre téléphone, réduisant le risque en cas de piratage. Seule la seed phrase secondaire est compromise, protégeant vos autres portefeuilles. Avec BIP-32, vous devez utiliser la seed phrase principale et un chemin de dérivation, exposant tous vos fonds.

### 2.2 Créer un portefeuille pour un membre de la famille

- **Scénario** : Vous configurez un portefeuille Bitcoin pour un proche (ex. : votre mère) tout en pouvant le récupérer s’il le perd.
- **Solution BIP-85** : Vous créez une seed phrase secondaire dédiée et partagez uniquement celle-ci.
- **Avantage par rapport à BIP-32** : Avec BIP-32, créer un compte pour un proche nécessite soit de partager votre seed phrase principale, risquant tous vos fonds et compliquant la gestion pour votre proche (gestion des chemins de dérivation), soit de créer une nouvelle seed phrase à sauvegarder en plus de votre seed phrase principale. 

### 2.3 Faciliter la gestion de portefeuilles distincts

- **Scénario** : Vous séparez vos bitcoins pour différents objectifs (ex. : épargne à long terme, fonds non-KYC).
- **Solution BIP-85** : Vous créez des seed phrases secondaires dédiées à chaque objectif.
- **Avantage par rapport à BIP-32** : Avec BIP-32, tous les comptes partagent la même seed phrase, ce qui complique la gestion dans des portefeuilles tiers en nécessitant de gérer des chemins de dérivation comme `m/44'/0'/0'`. De plus, il n’est pas possible d’attribuer un compte distinct par appareil (ex. : "épargne sur Coldcard", "quotidien sur mobile", "vacances sur Trezor"). BIP-85 attribue une seed phrase secondaire unique par objectif, facile à identifier et à importer séparément sur chaque appareil.

### 2.4 Utiliser un portefeuille temporaire pour des transactions

- **Scénario** : Vous avez besoin d’un portefeuille temporaire pour une transaction unique ou pour préserver la confidentialité (ex. : mixage de fonds, intéraction avec un exchange KYC, ..).
- **Solution BIP-85** : Vous créez une seed phrase secondaire, vous l'utilisez pour la transaction, puis vous la détruisez si nécessaire, sachant qu’elle peut être régénérée.
- **Avantage par rapport à BIP-32** : Avec BIP-32, un compte temporaire dépend de la seed phrase principale, exposant tous vos fonds si compromise.



## 3. Pré-requis avant de commencer

- **Matériel**
	- Coldcard Mk4 ou Q1
	- Carte MicroSD

- **Connaissances de base**
	- Comprendre les phrases mnémoniques (BIP-39) : liste de 12 à 24 mots pour sauvegarder un portefeuille.
	- Savoir ce qu’est un portefeuille Bitcoin : logiciel ou appareil pour gérer vos bitcoins, et comment le restaurer avec une phrase mnémonique.
	- Plus de ressources en Annexes.

- **Logiciels compatibles**
	- Sparrow Wallet (ordinateur, pour watch-only ou gestion avancée)
	- Nunchuck (mobile, pour multi-signatures)
	- BlueWallet (mobile)
	- ...

- **3.4 Configuration du Coldcard**
	- Initialiser une seed phrase de 24 mots sur le Coldcard.
	- Optionnel : Ajouter une passphrase pour sécuriser l’accès aux dérivations BIP-85.
	- Activer les options utiles : NFC (pour export), désactiver l’USB sur batterie (sécurité).


## 4. Tutoriel pas à pas

Suivez ces étapes pour créer, utiliser et récupérer une phrase mnémonique secondaire avec BIP-85 sur votre Coldcard. 

### 4.1 Générer une seed phrase secondaire

Vous allez créer une seed phrase secondaire à partir de votre seed phrase principale.
Allumez votre Coldcard, entrez votre code PIN.

- **1. Si vous avez appliqué une passphrase à votre seed principale :**
	- Depuis l'écran d'accueil, allez dans `Passphrase`.
    - Choisissez `Add Word` et entrez votre mot de passe.
    - Appuyez sur `Apply`.
    - Vérifiez l'identité du portefeuille :  Allez dans `Advanced > View Identity` pour noter l’empreinte (fingerprint) de ce portefeuille.

- **2. Aller au menu BIP-85**
	- Depuis l'écran d’accueil, allez dans `Advanced > Derive Seed B85` 
	- Lisez l’avertissement et confirmez.

La ColdCard vous informe que les seeds générées sont dérivées mathématiquement de votre seed principale, mais totalement indépendantes sur le plan cryptographique.
![image](assets/fr/03.webp)

- **3. Choisir un format**  
	Sélectionnez le format de la seed phrase secondaire : 12, 18 ou 24 mots. Vérifiez le nombre de mots acceptés par le wallet dans lequel vous voulez importer votre seed phrase secondaire.
![image](assets/fr/04.webp)

- **4. Sélectionner l'index**  
	- Entrez un index entre 0 et 9999.
	- Cet index est crucial pour pouvoir régénérer la seed secondaire plus tard. Conservez-le soigneusement avec un label du type : “Index 1 = wallet mobile”, "Index 2 = projet famille", "Index 4 = test mixage", ...
	- Si vous le perdez, vous ne perdez pas l'accès à vos fonds, mais il vous faudra tester les combinaisons de 0 à 9999 pour les retrouver.
![image](assets/fr/05.webp)

- **5. Noter ou exporter la seed phrase secondaire**  
	La ColdCard affiche maintenant une nouvelle seed phrase secondaire. Vous pouvez :
	- La **noter manuellement**.
	- Appuyer sur :
	    - `1` pour l’enregistrer sur la carte SD
	    - `2` pour **passer en mode "utiliser cette seed"** sur la ColdCard (utile pour l’export ou la signer une transaction)
	    - `3` pour afficher un **QR code** (à scanner avec une application mobile comme BlueWallet ou Nunchuck)
	    - `4` pour l’envoyer par **NFC**

💡 À ce stade, vous avez une seed phrase indépendante, utilisable dans n’importe quel wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck…).
![image](assets/fr/06.webp)
![image](assets/fr/07.webp)
### 4.2 Utilisation de la seed secondaire

Vous pouvez maintenant utiliser cette seed dérivée pour créer un nouveau portefeuille dans :    
- une app mobile
- un autre hardware wallet
- un portefeuille multisig

### 4.3 Récupérer une seed phrase secondaire perdue

À tout moment, pour retrouver une seed secondaire, recommencez le process :
1. Redémarrez votre ColdCard
2. Entrez votre PIN
3. Entrez votre passphrase, si définie
4. Allez dans `Advanced > Derive Seed B85`
5. Choisissez le format (12/18/24 mots)
6. Entrez le même index (ex : `1`)
7. Vous obtiendrez exactement la même seed secondaire


## 5. Limites, risques et bonnes pratiques

### 5.1 Dépendance à la seed phrase principale + passphrase

L'utilisation de BIP85 repose entièrement sur la seed phrase principale de 24 mots, ainsi que sur la passphrase si vous en avez appliqué une. 
- A partir de ces deux éléments, toutes les seed phrases secondaires peuvent être régénérées.
- Sans un seul de ces 2 éléments, vous perdez l'accès à l'ensemble des portefeuilles dérivés. 

### 5.2 Risques en configuration multi-signature

Il est fortement déconseillé d'utiliser dans une configuration multi-sig des seed phrase secondaires générés à partir de la même seed phrase principales : en cas de compromission de l’appareil ou de la seed phrase principale, toutes les clés de la multi-sig pourraient être régénérées par un attaquant. 

### 5.3 Compatibilité logicielle

Toutes les applications ne supportent pas directement la dérivation BIP85. Toutefois, les seeds générées via BIP85 sont des seeds standards BIP39 (12, 18 ou 24 mots), et peuvent donc être utilisées dans n’importe quel portefeuille compatible BIP39.

### 5.4 Registre des comptes BIP85

Il est recommandé de tenir à jour un registre personnel des seed phrases secondaires. 
- Il permet de retrouver rapidement quel index BIP85 correspond à quel portefeuille, sans avoir besoin de conserver les seed phrases secondaires.
- Ce registre doit rester minimaliste, sans mention explicite de Bitcoin, et doit rester stocké séparément de la graine principale. Pensez à en faire mention dans votre plan d'héritage.

Le registre peut contenir :
- l’index BIP85 utilisé (nombre de 0 à 9999)
- un usage ou un nom de référence (ex : hot wallet, épargne perso, wallet de Maman)
- éventuellement l’empreinte "fingerprint" du portefeuille pour vérification dans ColdCard

### 5.5 Sauvegarde

Les sauvegardes doivent inclure :
- la graine principale
- la passphrase (si utilisée)

Ne jamais stocker ensemble :
- la graine principale et la passphrase
- la graine principale et le registre des comptes BIP85

Plus de ressources en Annexes.


## ANNEXES

## A.1 Glossaire

- [BIP](https://planb.network/resources/glossary/bip)
- [BIP-32](https://planb.network/resources/glossary/bip0032)
- [BIP-39](https://planb.network/resources/glossary/bip0039)
- [BIP-85](https://planb.network/resources/glossary/bip0085)
- [Seed phrase](https://planb.network/resources/glossary/recovery-phrase)
- [Passphrase](https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig](https://planb.network/resources/glossary/multisig)


### A.2 Sauvegarder sa phrase de récupération

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Comprendre la Passphrase BIP39

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Les rouages des portefeuilles Bitcoin

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
