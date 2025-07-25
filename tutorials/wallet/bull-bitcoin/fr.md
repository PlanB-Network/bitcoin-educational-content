---
name: Bull Bitcoin Wallet
description: Découvrez comment utiliser le wallet Bull Bitcoin
---

![cover](assets/cover.webp)

Ce guide vous accompagne dans l’installation, la configuration, et l’utilisation de Bull Bitcoin Mobile. Vous apprendrez à recevoir et envoyer des fonds sur les trois réseaux : onchain, Liquid et Lightning et à transférer vos Bitcoin d’un réseau à l’autre. Des annexes fournissent les ressources et contacts, apportent du contexte, et expliquent succinctement les concepts techniques.

## Introduction

**Bull Bitcoin Mobile**, développé par **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([créer son compte](https://app.bullbitcoin.com/registration/orangepeel)), est un portefeuille Bitcoin **self-custodial**, ce qui signifie que vous contrôlez entièrement vos clés privées et donc vos fonds, sans dépendre d’un tiers. Open-source et ancré dans une philosophie cypherpunk, ce wallet combine simplicité, confidentialité, et fonctionnalités avancées comme les swaps entre réseaux et le support de Payjoin. Il permet de gérer vos bitcoins sur trois réseaux : **Bitcoin onchain**, **Liquid** et **Lightning**, chacun adapté à des usages spécifiques.

### Contexte du développement

Le wallet répond à un défi majeur : les frais du réseau Bitcoin sont inadaptés aux petits paiements, ou à l’ouverture de petits canaux Lightning auto-hébergés. Le wallet Bull Bitcoin Mobile propose une solution self-custodial tout en se reposant sur les 3 réseaux majeurs de Bitcoin :

* **Réseau Bitcoin (onchain)** : Idéal pour la conservation d'UTXOs à moyen ou long terme et les transactions de montants élevés, où les frais sont proportionnellement négligeables.
* **Réseau Liquid** : Conçu pour des transactions rapides (~2 minutes), plus confidentielles (montants masqués), et à faible coût, parfait pour accumuler de petits montants ou protéger sa vie privée.
* **Réseau Lightning** : Optimisé pour des paiements instantanés et à faible coût, adapté aux transactions quotidiennes de petite ou moyenne valeur.  

Ainsi avec Bull Bitcoin Mobile, vous pouvez par exemple accumuler de petits montants sur les portefeuilles **Liquid** ou **Lightning** puis, une fois un montant significatif atteint, vous pouvez :

* Transférer vers le réseau onchain pour une conservation sécurisée à moyen ou long terme, en ayant amélioré la confidentialité grâce à Liquid et/ou Lightning en amont, et avec des frais onchain pour une seule transaction

### Évolution continue

Le wallet évolue constamment, donc ne soyez pas surpris si vous constatez des écarts entre ce tutoriel et votre application à jour.
- Par exemple, au 19/07/2025, les boutons **"Buy / Sell / Pay"** sont visibles mais grisés dans l’application, car ces options, disponibles sur l'exchange [bullbitcoin.com](https://app.bullbitcoin.com/registration/orangepeel), seront bientôt intégrées pour une expérience unifiée. Leur utilisation restera entièrement optionnelle. Beaucoup d’autres évolutions sont en cours ou planifiées : gestion multi wallets, passphrase, compatibilité avec les hardware wallets...
- Vous pouvez consulter sur le [GitHub de BullBitcoin](https://github.com/orgs/SatoshiPortal/projects/49) les sujets en cours et les prochaines évolutions. Le projet étant 100% open-source et "built in public", vous pouvez également faire remonter vos suggestions et éventuels bugs rencontrés.


## 1. Prérequis

Avant de commencer à utiliser **Bull Bitcoin Mobile**, assurez-vous de disposer des éléments suivants :

* **Smartphone compatible** : Un appareil **iOS** (iPhone ou iPad) ou **Android**
* **Connexion internet**
* **Support sécurisé pour la sauvegarde** : Notez votre **phrase de récupération** (12 mots) sur un papier ou du métal et stockez-la dans un endroit sûr.
* **Connaissances de base** : Une compréhension minimale des concepts Bitcoin (adresses, transactions, frais) est utile, bien que ce tutoriel explique chaque étape pour les débutants.

## 2. Installation

- **Téléchargez l’application** :
	- **[Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)** Téléchargez depuis le magasin d'application pour les appareils Android
	- **[GitHub](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Téléchargez directement l'APK pour les appareils Android
	- **[iOS](https://testflight.apple.com/join/FJbE4JPN)** Téléchargez via TestFlight pour les appareils Apple
	- Vérifiez le nom du développeur (Bull Bitcoin) pour éviter les applications frauduleuses.
	- Assurez-vous que la version téléchargée correspond à la dernière version stable indiquée sur GitHub.
	- Bull Bitcoin Mobile est **open-source**. Pour consulter le code : [GitHub de BullBitcoin](https://github.com/orgs/SatoshiPortal/projects/49) 

- **Installez l’application**


## 3. Configuration initiale

### 3.1 Lancer l’application :

L’application utilise une **phrase de récupération** (12 mots) unique pour les deux portefeuilles :
 - **‘Secure Bitcoin’ Wallet** : Pour les transactions sur le réseau Bitcoin (onchain)
 - **‘Instant Payments’ Wallet** : Pour les transactions instantanées sur les réseaux Liquid et Lightning

 A l'ouverture, vous êtes donc invité à importer une phrase de récupération existante, ou à créer un nouveau wallet :
 
![image](assets/fr/02.webp)

### 3.2 Phrase de récupération :

Si vous souhaitez ré-utiliser un wallet existant, cliquez sur “**Recover Wallet**” et renseignez les 12 mots de votre phrase de récupération.

Sinon, cliquez sur “**Create New Wallet**” :
- Notez votre phrase de récupération avec le plus grand soin. Inscrivez-la sur du papier ou du métal et conservez-la dans un endroit sûr (coffre-fort, lieu hors ligne). Cette phrase est votre seul moyen pour accéder à vos bitcoins en cas de perte de votre appareil ou suppression de l'application.
- Il est important de noter également que toute personne possédant cette phrase peut voler tous vos bitcoins. Ne la stockez jamais numériquement :
	- Pas de capture d’écran
	- Pas de sauvegarde dans le cloud, email ou messagerie
	- Pas de copier/coller (risque d’enregistrement dans le presse-papiers)

**! Ce point est critique**. Pour obtenir plus d'aide :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Sécurisation de l’accès :

* Accéder aux paramètres puis cliquez sur **PIN Code**.
* Configurez un **code PIN** robuste pour protéger l’accès à l’application.
* Cette étape est facultative mais fortement recommandée pour empêcher quiconque ayant l'accès à votre téléphone de pouvoir accéder à votre wallet.

![image](assets/fr/03.webp)
  
### 3.4 Connexion à un nœud personnel (optionnel):

Le wallet BullBitcoin se connecte à des serveurs Electrum par défaut : le premier géré par Bull Bitcoin et un serveur secondaire de Blockstream, tous deux considérés comme ne conservant pas de logs, ce qui réduit les risques de suivi.

Pour plus de confidentialité, vous pouvez connecter l’application à votre propre nœud Bitcoin via un serveur Electrum (instructions disponibles sur le [GitHub de BullBitcoin](https://github.com/orgs/SatoshiPortal/projects/49) ).
  

## 4. Recevoir des fonds

 Recevoir des fonds avec **Bull Bitcoin Mobile** est simple et adapté à vos besoins, que vous utilisiez :
  - le réseau **Bitcoin (onchain)** pour la conservation à long terme,
  - le réseau **Liquid** pour des transactions rapides et plus confidentielles,
  - le réseau **Lightning** pour des paiements instantanés de faibles montants.  

L’application génère automatiquement des adresses de reception ou factures Lightning selon le réseau choisi. Voici comment procéder pour chaque réseau.

### 4.1. Onchain (réseau Bitcoin)

Sur l’écran d’accueil, vous pouvez :
* soit sélectionner le **Secure Bitcoin Wallet** puis cliquer sur “**Receive”** :

![image](assets/fr/04.webp)

* soit cliquer sur “**Receive”**, et ensuite choisir le réseau **Bitcoin** :

![image](assets/fr/05.webp)

#### 4.1.1. Option "Copy or scan address only" désactivée (par défaut)

![image](assets/fr/06.webp)

- Ceci donne accès à des paramètres avancés, optionnels. Vous pouvez préciser :
	- Un **montant** en BTC, en sats ou en fiat.
	- Une **note personnelle** qui sera intégrée dans la copie de l'URI / dans le QR Code.
	* L’activation de **Payjoin** (voir Annexe 3 pour détails), qui améliore la confidentialité en combinant les entrées de l’expéditeur et du destinataire.

- **Exemple d’URI** automatiquement généré :

```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```

- **Utilisation** : Copiez l’URI pour le partager à l'expéditeur, ou laissez-le scannez le QR code.

#### 4.1.2. Option "Copy or scan address only" activée

![image](assets/fr/07.webp)

- Avec l’option **"Copy or scan address only"** activée, l’application génère une adresse Bitcoin simple au format SegWit (bech32).

- Exemple :

```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```

Même si vous saisissez un montant ou une note, ils ne seront pas intégrés au QR Code ou dans la copie de l'adresse

- **Utilisation** : Copiez l’adresse pour la partager à l'expéditeur, ou laissez-le scannez le QR code.

#### 4.1.3. Génération d’une nouvelle adresse

- Pourquoi utiliser une nouvelle adresse pour chaque transaction ? Cela **protège votre vie privée** en empêchant de relier plusieurs paiements à une même adresse, et limite les possibilités de traçage sur la blockchain.
	- **Par défaut, Bull Bitcoin génère automatiquement une adresse non utilisée.**
	- Vous pouvez forcer la création d’une nouvelle adresse en cliquant sur **“New Address”** en bas de l'écran.
	- Toutes vos adresses sont liées à votre seed phrase : quel que soit le nombre d’adresses utilisées, votre portefeuille affichera un solde unique et pourra regrouper automatiquement les fonds lors d’un envoi.

- **Conseil : Utilisez systématiquement la nouvelle adresse** fournie par Bull Bitcoin, sauf en cas de besoin spécifique (ex. : adresse publique pour recevoir des dons).

### 4.2. Liquid

Sur l’écran d’accueil, vous pouvez :
* soit sélectionner le **Instant payments Wallet** puis cliquer sur **"Receive”** puis **"Liquid"** :

![image](assets/fr/08.webp)

* soit cliquer sur “**Receive”**, et ensuite choisir le réseau **Liquid** :

![image](assets/fr/09.webp)
  
Une fois que vous êtes sur l'écran **"Receive"**, copier une adresse Liquid :

- Sans montant ni note. Exemple :

```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```

* Ou en précisant un **montant** (en BTC, en sats ou en fiat) et/ou une **note personnelle** qui sera intégrée dans la copie de l'URI / dans le QR Code. Exemple :

```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```

**Utilisation** : Copiez l’adresse/URI pour la partager à l'expéditeur, ou laissez-le scannez le QR code.

### 4.3. Lightning

Sur l’écran d’accueil, vous pouvez :
* soit sélectionner le **Instant payments Wallet** puis cliquer sur “**Receive”** :

![image](assets/fr/10.webp)

* soit cliquer sur “**Receive”**, et ensuite choisir le réseau **Lightning** :

![image](assets/fr/11.webp)

#### 4.3.1. Fonctionnement, limites et avantages

- **Mécanisme** : Bull Bitcoin Wallet est un portefeuille qui permet d'effectuer et de recevoir des paiements via Lightning. Les fonds reçus via Lightning sont stockés sur le réseau **Liquid** (dans le Instant Payments Wallet) grâce à un swap automatique via **Boltz**. Ce qui permet d'avoir les capacités d'interagir avec Lightning sans avoir à gérer de canaux de liquidités, tout en restant en self-custody.

- **Limites :**
	- **Un montant minimal** de 100 satoshis (au 19/07/2025) lorsque vous générez la facture.
	* **Des frais à votre charge** qui seront soustraits du montant envoyé par l'expéditeur, contrairement à une réception avec wallet Lightning native, où seul l’expéditeur paie les frais de transfert en plus du montant envoyé. Au 19/07/2025, 47 sats sont déduits du montant envoyé.

- **Avantages** :
	* **Self-custodial** : Vos fonds restent sous votre contrôle, stockés sur le réseau Liquid.
	* **Pas de frais onchain élevés** : Le stockage sur Liquid évite les dépôts onchain coûteux pour ouvrir votre canal Lightning ou ajouter des liquidités. Ces opérations peuvent se faire plus tard, lorsque le montant accumulé sur Liquid justifie les frais.

- **Astuce :** Si l’expéditeur possède le Wallet Bull Bitcoin, utilisez directement le réseau Liquid pour éviter les frais de swap

#### 4.3.2. Générer une facture

- Renseignez un **montant** (en BTC, sats ou fiat)

- Ajoutez une **note personnelle** qui sera intégrée dans la facture. Si l'expéditeur règle la facture, elle sera aussi reprise par votre wallet dans les détails de la transaction.

- **Validité de la facture :** La facture Lightning est valide pendant **12 heures**. Après ce délai, elle expire et ne peut plus être payée, une nouvelle facture doit être générée.

- **Utilisation** : Copiez la facture pour la partager à l'expéditeur, ou laissez-le scannez le QR code.
 

## 5. Envoyer des fonds

### 5.1. Principe de base

Soit à partir de la page d'accueil, soit à partir des wallets :

![image](assets/fr/12.webp)

vous accédez à l'écran d'envoi :

![image](assets/fr/13.webp)

**Bull Bitcoin Mobile** facilite l’envoi de fonds en détectant automatiquement le réseau (Bitcoin, Liquid, ou Lightning) à partir de l’adresse ou de la facture saisie (copiée ou scannée via QR code).
  
### 5.2. Envoi onchain (réseau Bitcoin)

#### 5.2.1. Ecran d'envoi

**Action** : Entrez ou scannez une adresse Bitcoin onchain

* Si le montant n'a pas été défini, par exemple :

```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```

- Alors vous pourrez choisir sur l'écran d'envoi : 
	* Le montant en BTC, en sat ou en fiat. Montant minimal : 546 satoshis au 22/07/2025.
	* Une note optionnelle pour identifier la transaction. Uniquement visible par vous, dans les détails de la transaction. 
  
![image](assets/fr/14.webp)

* Si le montant a déjà été défini, par exemple :

```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```

Alors, vous arrivez directement à l'écran de confirmation ci-après.  

#### 5.2.2 Ecran de confirmation

Prenez bien le temps de vérifier tous les paramètres, particulièrement le montant, l'adresse de destination et les frais.
Puis vous pouvez ajuster des paramètres :

![image](assets/fr/15.webp)
- **Frais** : Vous pouvez choisir :
	 - **Soit la vitesse d’exécution** de votre transaction, et les frais associés seront estimés
	 - **Soit les frais**, en mode Absolute fees (frais totaux en satoshis) ou Relative fees (frais par byte), et la vitesse d’exécution de votre transaction sera estimée

- **Paramètres avancés** :

	 - **Replace-by-Fee (RBF)** : Activé par défaut, cette fonction permet d'accélérer la transaction en payant des frais plus élevés (voir Annexe 4 pour détails).
	 - **Sélection manuelle des UTXO** : Si vos fonds sont stockés sur plusieurs adresses différentes de ton wallet, vous pouvez choisir les adresses à partir desquelles envoyer les fonds. Pourquoi ? Avec l’adoption croissante de Bitcoin, les frais de transfert augmentent. Envoyer depuis plusieurs adresses avec de petits montants est plus coûteux qu’un envoi depuis une adresse unique, mais le faire maintenant évite de devoir le faire plus tard, lorsque les frais seront encore plus élevés. On parle de **consolidation d’UTXO.**

![image](assets/fr/16.webp)

- **Envoi avec Payjoin** : Si la fonction a été activée par le destinataire qui a fourni l'URI, par exemple :

```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```

Alors, Bull Bitcoin Mobile va configurer l'envoi en combinant en entrée vos UTXO avec des UTXO du destinataire, améliorant la confidentialité (voir Annexe 3 pour détails).

### 5.3. Envoi sur Liquid

#### 5.3.1 Ecran d'envoi

Le réseau **Liquid** permet des transactions rapides (~2 minutes grâce à un bloc par minute), plus confidentielles (montants masqués) que sur le réseau onchain, et avec des frais très faibles. Les fonds sont prélevés du **Instant Payments Wallet**. 

 **Action** : Entrez ou scannez une adresse Liquid

* Si le montant n'a pas été défini, par exemple :

```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```

Alors, vous pourrez choisir sur l'écran d'envoi : 
- Le montant en BTC, en sat ou en fiat. Pas de minimum, 1 satoshi possible ;
- Une note optionnelle pour identifier la transaction. Uniquement visible par vous, dans les détails de la transaction. 
  
![image](assets/fr/17.webp)

* Si le montant a déjà été défini, par exemple :

```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```

Alors, vous arrivez directement à l'écran de confirmation ci-après.  

#### 5.3.2 Ecran de confirmation

Prenez bien le temps de vérifier tous les paramètres, particulièrement le montant et l'adresse de destination.

![image](assets/fr/18.webp)

* **Frais** : Proportionnels à la complexité de la transaction, généralement sur une base 0.1 sat/vB, soit 20-40 satoshis pour une transaction simple (33 sats au 22/07/2025).
  
### 5.4. Envoi sur Lightning

#### 5.4.1 Ecran d'envoi

Le réseau **Lightning** permet des paiements instantanés à faible coût pour les transactions de faibles montants, idéaux pour les petites transactions quotidiennes. 

**Action** : Entrez ou scannez une facture Lightning

* Si vous scannez une adresse LN-URL qui vous laisse définir le montant
  Exemple : `orangepeel@walletofsatoshi.com`.
  alors vous pourrez choisir sur l'écran d'envoi : 
	* Le montant en BTC, en sat ou en fiat. Montant minimal de 1000 satoshis au 23/07/2025
	* Une note optionnelle pour identifier la transaction. Elle sera transmise au destinataire.
  
![image](assets/fr/19.webp)

* Si vous scannez une facture Lightning qui contient un montant défini
  Exemple :

```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```

Alors, vous arrivez directement à l'écran de confirmation ci-après. 

Nota : le montant doit être supérieur à 21 sats au 23/07/2025

#### 5.4.2 Fonctionnement, limites et avantages

* **Mécanisme** : Les fonds sont prélevés du **Instant Payments Wallet** (Liquid) et convertis via un swap **Liquid → Lightning** avec **Boltz**. 

* **Limites :**
	* **Un montant minimal** supérieur à un wallet Lightning native (voir ci-avant)
	* **Frais** augmentés du swap Liquid → Lightning via Boltz

* **Avantages** :
	* **Self-custodial** : Vos fonds restent sous votre contrôle, stockés sur le réseau Liquid, et transférables via Lightning si besoin
	* **Pas de frais onchain élevés** : Le stockage sur Liquid vous a évité des dépôts onchain coûteux pour ouvrir votre canal Lightning ou ajouter des liquidités. Ces opérations peuvent se faire plus tard, lorsque le montant accumulé sur Liquid justifie les frais.

* **Astuce :** si le destinataire possède le Wallet Bull Bitcoin, utilisez directement le réseau Liquid pour vous éviter les frais de swap

#### 5.3.3 Ecran de confirmation

Prenez bien le temps de vérifier tous les paramètres, particulièrement le montant et l'adresse de destination.

![image](assets/fr/20.webp)


## 6. Consultation de l’historique
  
**Bull Bitcoin Mobile** permet de suivre facilement vos transactions sur les réseaux **Bitcoin (onchain)**, **Liquid**, et **Lightning**. L’historique est accessible de deux manières et affiche des informations détaillées pour chaque type de transaction. Vous pouvez également vérifier vos transactions à l’aide d’explorateurs de blocs externes.

### 6.1. Accéder à l’historique  

* **Via l’écran d’accueil** :
	* Cliquez sur le **Secure Bitcoin Wallet** pour voir les transactions **onchain**, ou sur l’**Instant Payments Wallet** pour les transactions **Liquid** et **Lightning**.
	* L’historique s’affiche directement sous le montant total du portefeuille, filtré selon le type de wallet sélectionné.

![image](assets/fr/21.webp)

* **Via la page dédiée** :
	* Sur l’écran d’accueil, cliquez sur le **symbole de l’historique** (icône d’horloge ou similaire).
	* Accédez à une page listant toutes les transactions, avec des filtres par type d’action : **Send**, **Receive**, **Swap**, **Payjoin**, **Sell**, **Buy** (note : Sell et Buy sont en cours de développement et non disponibles à ce jour, 20 juillet 2025).

![image](assets/fr/22.webp)

### 6.2. Détails des transactions

Chaque transaction affiche des informations spécifiques selon le réseau et le type d’action (envoi ou réception). Voici les détails disponibles pour une **transaction onchain** :

![image](assets/fr/23.webp)
  
### 6.3. Vérification via explorateurs de blocs

La liste des explorateurs pour les réseaux **Bitcoin onchain**, **Liquid** et **Lightning** sont en Annexe 4.

Pour **Lightning**, les transactions ne sont pas visibles sur des explorateurs publics. Vérifiez les détails (y compris Swap ID pour Boltz) dans l’application.


## 7. Settings

La page "Settings" est accessible directement depuis la page d'accueil de l'application Bull Bitcoin et permet de configurer et gérer divers aspects du portefeuille et de l'expérience utilisateur.

![image](assets/fr/24.webp)

* **Wallet Backup** : Affiche la phrase de récupération du portefeuille pour permettre une sauvegarde sécurisée. Consultez la section 3. sur la création du portefeuille pour les bonnes pratiques liées à la gestion et au stockage de la phrase de récupération.

* **Wallet Details** :
	* **Pubkey** : Clé publique associée au portefeuille, utilisée pour générer des adresses de réception Bitcoin.
	* **Derivation Path** : Chemin de dérivation utilisé pour générer les adresses du portefeuille à partir de la clé privée.

* **Electrum Server (Bitcoin Node)** : Permet de configurer une connexion à un nœud Bitcoin personnalisé pour les transactions onchain. 

* **PIN Code** : Activation et/ou modification du code de sécurité pour protéger l'accès à l'application et aux fonctionnalités du portefeuille.

* **Currency** : Permet de choisir l'affichage des montants en BTC ou en sats, ainsi que la monnaie fiat par défaut (dollar, euro, etc.).

* **Auto Swap Settings** : La fonction _Auto Swap_ permet d’automatiser le transfert de vos BTC depuis le **Instant Payments Wallet (Liquid)** vers votre portefeuille **Bitcoin on-chain**, dès que le montant atteint un seuil que vous jugez suffisamment élevé pour justifier les frais de transaction.

* **Logs** : Journaux d'activité consultables, pouvant être partagés avec le support technique pour faciliter le dépannage.

* **Accès au Telegram pour support** : Lien direct vers le canal Telegram officiel pour une assistance utilisateur.

* **Accès au Github** : Lien vers le [dépôt Github de Bull Bitcoin](https://github.com/SatoshiPortal) pour consulter le code open-source ou signaler des problèmes.
 

## ANNEXES

### A1. Explication de Payjoin (P2EP)

![image](assets/fr/25.webp)

**Définition** : 
- Payjoin, ou **Pay-to-EndPoint (P2EP)**, est une technique de transaction Bitcoin qui améliore la confidentialité sur le réseau **onchain**. Elle combine les entrées de l’expéditeur et du destinataire dans une seule transaction, rendant les montants et les adresses plus difficiles à tracer.
  
**Fonctionnement :**
- Dans une transaction Payjoin, l’expéditeur et le destinataire collaborent via un serveur Payjoin compatible pour générer une transaction conjointe.
- Au lieu que seul l’expéditeur fournisse des entrées (UTXO), le destinataire contribue également avec un de ses propres UTXO. Cela brouille les informations visibles sur la blockchain : au lieu d’une seule entrée correspondant au montant réel, il y a désormais deux entrées, et les sorties ne reflètent pas directement le montant échangé.
- La transaction finale ressemble à une transaction Bitcoin standard (multi-entrées/multi-sorties), mais elle masque le montant réel envoyé et les liens entre les adresses grâce à une structure stéganographique.

**Utilisation dans Bull Bitcoin Mobile**
- **Réception** (fourniture d’une adresse) : Payjoin est activé par défaut. 
- **Envoi** : Le wallet détecte automatiquement un URI Payjoin et configure la transaction en conséquence, par exemple :

```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```

 
**Avantages**
- **Confidentialité renforcée** : Payjoin invalide l'hypothèse qui suppose que toutes les entrées d’une transaction appartiennent à une seule entité. Avec Payjoin, les entrées proviennent de l’expéditeur et du destinataire, brisant cette assomption.
- **Masquage du montant** : Le montant réel échangé n’apparaît pas directement dans les sorties. Il est calculé comme la différence entre l’UTXO du destinataire en entrée et en sortie, rendant l’analyse trompeuse.

**Limites**
- Payjoin nécessite que l’expéditeur et le destinataire utilisent des portefeuilles compatibles, Sinon, une transaction onchain standard est utilisée.
- La transaction est légèrement plus complexe (plus d’entrées et de sorties), ce qui entraîne des frais légèrement plus élevés.
- Bien que conçue pour ressembler à une transaction standard, des heuristiques avancées (ex. : sorties ambiguës, serveurs Payjoin connus) peuvent faire suspecter son utilisation, bien que sans certitude absolue.

**Plus d'info :**
- [Glossaire](https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions Payjoin](https://planb.network/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-transactions-payjoin-c1e90b95-f709-4574-837b-2ec26b11286f)


### A2. Explication de Replace-by-Fee (RBF)

**Définition** : Replace-by-Fee (RBF) est une fonctionnalité du réseau Bitcoin qui permet à l'expéditeur d'accélérer la confirmation d'une transaction **onchain** en acceptant de payer des frais plus élevés.

**Limites** :
- RBF n’est pas disponible pour les transactions Liquid ou Lightning.
* La transaction initiale doit être marquée comme RBF-compatible lors de sa création, ce que Bull Bitcoin Mobile fait automatiquement sauf si désactivé.

**Plus d'info :** 
- [Glossaire](https://planb.network/fr/resources/glossary/rbf-replacebyfee)


### A3. Bonnes pratiques

Pour utiliser **Bull Bitcoin Mobile** de manière sécurisée et efficace, suivez ces recommandations. Elles vous aideront à protéger vos fonds, optimiser vos transactions, et préserver votre confidentialité sur les réseaux **Bitcoin (onchain)**, **Liquid**, et **Lightning**.

* **Sécurisez votre phrase de récupération** :
	* Tutoriel : [Sauvegarder sa phrase mnémonique](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) 
	* Cours [La phrase mnémonique](https://planb.network/fr/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/la-phrase-mnemonique-8f9340c1-e6dc-5557-a2f2-26c9669987d5)  

* **Utilisez l’authentification sécurisée** : 
	* Activez un **code PIN robuste** ou l’**authentification biométrique** (empreinte digitale ou reconnaissance faciale) pour protéger l’accès à l’application.
	* Ne partagez jamais votre PIN ou vos données biométriques.

- **Protégez votre confidentialité** : 
	- Générez une nouvelle adresse pour chaque réception onchain ou Liquid afin de limiter le traçage sur la blockchain.
	- Utilisez Payjoin lorsque disponible pour augmenter la confidentialité quant au montant envoyé onchain
	- Pour une confidentialité maximale, connectez votre wallet à votre propre nœud Bitcoin via un serveur Electrum au lieu d’utiliser le nœud public 

* **Choisissez le réseau adapté à vos besoins** : 
	* **Onchain** : Privilégiez pour la conservation à long terme ou les transactions de montants élevés (frais négligeables par rapport au montant).
	* **Liquid** : Utilisez pour des transferts rapides, à faible coût et avec une confidentialité renforcée.
	* **Lightning** : Optez pour des transferts instantanés et très économiques pour de faibles montants. Si vous êtes deux utilisateurs du wallet Bull Bitcoin, privilégiez Liquid pour éviter les frais de swap Lightning <> Liquid via Boltz. 

* **Vérifiez toujours les adresses d'envoi** :
	* Avant d’envoyer des fonds, vérifiez soigneusement l’adresse. Les fonds envoyés à une mauvaise adresse sont perdus à jamais. Utilisez un copier/coller ou le scan de QR code, ne recopiez / modifiez jamais une adresse à la main. 

* **Optimisez les frais** :
	* Pour les transactions onchain, choisissez des frais adaptés (lente, moyenne, rapide) en fonction de l’urgence et de la congestion du réseau.
	* Utilisez Liquid, ou Lightning pour les petits montants.
	* Activez Replace-by-Fee (RBF) (voir Annexe 4) pour les envois onchain si vous anticipez un besoin d’accélérer la confirmation. 

* **Tenez l'application à jour**


### A4. Ressources supplémentaires

* **Liens officiels et support :** 
	* **[staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : email du support
	* **[Site officiel de Bull Bitcoin](https://bullbitcoin.com/) :** Informations sur les services Bull Bitcoin, création de compte, accès à l'application
	- **[GitHub Bull Bitcoin Mobile](https://github.com/SatoshiPortal/bullbitcoin-mobile) :** Consulter le code, les évolution et la roadmap, contribuer au développement...
	- **[Compte X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)**
	- **Groupe Telegram** pour le wallet mobile : chat collectif avec support, voir la page “Settings”.

* **Explorateurs de blocs :**
	* On chain : **[Mempool.space](https://mempool.space/)**
	* Liquid : **[Blockstream Info](https://blockstream.info/liquid)**
	* Lightning : **[1ML (Lightning Network)](https://1ml.com/)** 

* **Apprentissage et tutoriels :** **[Plan ₿ Network](https://planb.network/)** : 
	* **Sécuriser sa phrase de récupération**

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/


    * **Liquid Network** : 
	    * **[Glossaire](https://planb.network/fr/resources/glossary/liquid-network)**

https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727


    * **Lightning Network** :
	    * **[Glossaire](https://planb.network/fr/resources/glossary/lightning-network)**

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Bull Bitcoin

#### Aperçu de l'entreprise

 **[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, est la plus ancienne plateforme d'échange non dépositaire dédiée exclusivement au Bitcoin, fondée en 2013 à l'Ambassade Bitcoin de Montréal, Canada. Dirigée par Francis Pouliot, un pionnier reconnu dans l'écosystème Bitcoin, l'entreprise se positionne comme un acteur clé dans la promotion de la souveraineté financière et de l'autonomie des utilisateurs. Sa mission est de permettre aux individus de reprendre le contrôle de leur argent en utilisant Bitcoin comme outil de liberté et de paiement, tout en rejetant les monnaies fiat et les cryptomonnaies autres que Bitcoin.
 
![image](assets/fr/26.webp)

[Créer votre compte](https://app.bullbitcoin.com/registration/orangepeel) avec de 0,25 % de réduction sur vos achats et ventes de Bitcoin.

#### Valeurs et philosophie

Bull Bitcoin se distingue par son engagement envers les principes cypherpunk et l'éthique Bitcoin :

* **Focus exclusif sur Bitcoin** : La plateforme est fidèle à la vision d'une monnaie décentralisée et résistante à la censure.

* **Non-dépositaire** : Les utilisateurs conservent le contrôle total de leurs Bitcoin via l’envoi des fonds vers leurs propres portefeuilles.

* **Confidentialité** : Minimisation de la collecte de données personnelles, avec des options d'achat sans KYC pour des transactions inférieures à 999 USD. Les données sont protégées conformément aux réglementations (FINTRAC au Canada, AMF en France).

* **Transparence** : Pas de frais cachés, les coûts sont intégrés dans le spread (écart entre prix d'achat et de vente).

* **Souveraineté financière** : Bull Bitcoin promeut l'indépendance vis-à-vis des systèmes bancaires traditionnels et des institutions centralisées.  

#### Services principaux

* **Dépôt de fiat** : Les utilisateurs peuvent approvisionner leur compte Bull Bitcoin en devises fiat (CAD, EUR, etc.) via des virements bancaires ou en espèces/carte de débit dans certains bureaux de poste canadiens.

* **Achat de Bitcoin** : Les utilisateurs peuvent acheter du Bitcoin qui est envoyé directement à leur portefeuille non dépositaire, garantissant un contrôle total de leurs fonds.

* **Achat de Bitcoin programmé** : Bull Bitcoin propose un service d'achat récurrent automatisé (DCA - Dollar Cost Averaging) à intervalles réguliers, qui puise dans votre solde disponible, avec transfert direct des Bitcoins vers un portefeuille contrôlé par l'utilisateur, réduisant l'impact de la volatilité des prix.

Il est à noter qu'une option appelée "AutoBuy" permet de convertir vos fiats dès lors qu'ils touchent votre solde Bull Bitcoin et d'envoyer vos Bitcoins sur votre propre portefeuille. Cette option peut elle aussi être combinée à un virement bancaire récurrent programmé chez votre banque pour réaliser un DCA. Cette option permet d'automatiser votre accumulation de Bitcoin sans jamais avoir besoin d'ouvrir l'application.


* **Achat de Bitcoin à un prix fixé ‘Limit Order’** : Permet d'acheter du Bitcoin à un prix spécifié à l’avance par l’utilisateur, qui est automatiquement exécuté lorsque le prix de l'indice Bull Bitcoin atteint ou tombe en dessous de la limite fixée.

* **Vente de Bitcoin** : Les utilisateurs peuvent vendre leurs Bitcoins et recevoir les fonds en devise fiat directement sur leur compte bancaire via virement bancaire ou SEPA.

* **Paiements de tiers** : Bull Bitcoin permet à l’utilisateur d'envoyer de l'argent fiat à des comptes bancaires à partir de ses Bitcoin, de façon entièrement transparente pour le destinataire.

* **Bull Bitcoin Prime** : Bull Bitcoin Prime est un service premium destiné aux clients à haut patrimoine et aux entreprises, offrant des solutions personnalisées et un accompagnement premium. Cela inclut l'accès à des frais réduits, un gestionnaire de compte dédié, et des services sur mesure pour les entreprises. Ce service s'adresse aux institutions, aux traders professionnels et aux entreprises cherchant une expertise approfondie et un traitement prioritaire.

* **Portefeuille mobile** : Bull Bitcoin propose un portefeuille mobile open-source et self-custodial, disponible sur Android et iOS, qui prend en charge les transactions onchain, Liquid et Lightning Network.

* **Support éducatif** : Guides gratuits et accompagnement personnalisé pour aider les utilisateurs à créer, sécuriser et gérer leurs portefeuilles Bitcoin, renforçant l'autonomie financière.

#### Conformité et sécurité

* **Réglementation** : Enregistrée auprès de FINTRAC (Canada) et de l'AMF (France), Bull Bitcoin respecte les exigences KYC/AML.

* **Sécurité** : Utilisation de portefeuilles sécurisés et recommandations de stockage hors ligne. Les données personnelles sont hébergées sur l'infrastructure de Bull Bitcoin qui est 100% auto-hébergée et ne repose sur aucun tiers.
