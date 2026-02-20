---
name: Blitz Wallet
description: Le portefeuille Bitcoin le plus simple.
---

![cover](assets/cover.webp)

L'expérience utilisateur est l'un des facteurs décisifs lorsqu'on choisit un portefeuille Bitcoin. Dans ce tutoriel, nous vous présentons Blitz Wallet, un portefeuille qui place la simplicité au centre de son approche : grâce à l'intégration du protocole **Spark**, Blitz vous offre l'un des portefeuilles Bitcoin les plus simples et les plus complets du marché, avec des paiements instantanés et sans gestion technique.

## Qu'est-ce que Blitz Wallet ?

Blitz Wallet est un portefeuille Bitcoin **self-custodial** et **open source**, qui mise sur votre souveraineté et une expérience utilisateur fluide et intuitive.

[Blitz Wallet](https://blitz-wallet.com/) est une application mobile disponible sur Android (Play Store) et iOS (App Store).

Contrairement aux portefeuilles Lightning traditionnels qui nécessitent de gérer des canaux de paiement et de la liquidité entrante, Blitz Wallet s'appuie sur le **protocole Spark** pour éliminer ces complexités techniques. Résultat : des paiements instantanés dès le premier satoshi reçu, sans aucune configuration préalable. L'objectif de Blitz est de rendre les paiements en bitcoin aussi simples qu'une application de paiement classique, sans jamais compromettre la self-custody de vos fonds.

Blitz Wallet supporte également les **adresses lisibles** au format `utilisateur@domaine.com` (via LNURL), ce qui permet d'envoyer des bitcoins aussi facilement qu'un e-mail, sans avoir à manipuler de longues invoices ou de QR codes à chaque transaction.

## Comprendre le protocole Spark

Avant de passer à la pratique, il est utile de comprendre la technologie qui fait fonctionner Blitz Wallet sous le capot : le **protocole Spark**.

### Qu'est-ce que Spark ?

Spark est un protocole de surcouche open source construit sur Bitcoin, développé par l'équipe de Lightspark. Il permet d'effectuer des transactions instantanées et à faible coût, tout en préservant la self-custody de vos bitcoins.

Contrairement au Lightning Network qui repose sur des **canaux de paiement** entre deux parties, Spark utilise une technologie appelée **statechain** (chaîne d'état). Le principe fondamental est le suivant : au lieu de déplacer les bitcoins sur la blockchain à chaque transaction, Spark transfère le **droit de dépense** d'un utilisateur à un autre, sans mouvement on-chain.

### Comment ça fonctionne ?

Pour comprendre Spark de manière intuitive, imaginons que dépenser un bitcoin sur Spark nécessite de compléter un puzzle à deux pièces :
- Une pièce est détenue par l'utilisateur (par exemple, Alice).
- L'autre pièce est détenue par un groupe d'opérateurs appelé la **Spark Entity (SE)**.

Seule la combinaison des deux pièces correspondantes permet de dépenser les bitcoins.

Lorsqu'Alice veut envoyer ses bitcoins à Bob, voici ce qui se passe : un nouveau puzzle est créé conjointement entre Bob et le SE. Le puzzle garde la même forme, mais les pièces qui le composent changent. Désormais, c'est la pièce de Bob qui correspond à celle du SE. L'ancienne pièce d'Alice devient inutilisable, car le SE a détruit sa pièce correspondante. La propriété des bitcoins a changé de mains, **sans aucune transaction sur la blockchain**.

Bob peut ensuite répéter le même processus pour envoyer ces bitcoins à Carol, et ainsi de suite. Chaque transfert fonctionne par remplacement des pièces du puzzle, pas par un mouvement de fonds on-chain.

### Pourquoi c'est sécurisé ?

Une question légitime se pose : que se passe-t-il si le SE ne détruit pas réellement son ancienne pièce ?

Le Spark Entity n'est pas une entité unique : c'est un groupe d'opérateurs indépendants. La pièce du SE n'est jamais détenue par un seul opérateur. Le remplacement du puzzle nécessite la coopération de plusieurs opérateurs. Il suffit qu'**un seul opérateur soit honnête** lors d'un transfert pour empêcher la réactivation d'un ancien puzzle. Aucun opérateur isolé ne peut secrètement conserver un ancien puzzle actif ou le recréer ultérieurement.

De plus, Spark intègre un mécanisme de sortie unilatérale : vous pouvez toujours récupérer vos bitcoins on-chain sans la coopération du SE. Ce mécanisme de secours fait partie intégrante de l'architecture de Spark, et garantie que vous n'êtes jamais dépendant du réseau pour accéder à vos fonds.

### Spark vs Lightning Network

Spark et Lightning ne sont pas en concurrence : ils sont **complémentaires**. Blitz Wallet intègre les deux, ce qui vous permet de bénéficier des avantages de chacun.

|                               | **Spark**                    | **Lightning Network** |
| ----------------------------- | ---------------------------- | --------------------- |
| **Technologie**               | Statechains (chaînes d'état) | Canaux de paiement    |
| **Gestion de canaux**         | Non requise                  | Requise               |
| **Liquidité entrante**        | Non requise                  | Requise               |
| **Transactions instantanées** | Oui                          | Oui                   |
| **Self-custody**              | Oui                          | Oui                   |
| **Compatibilité Lightning**   | Oui (via atomic swaps)       | Natif                 |

Le Lightning Network reste un excellent protocole pour les paiements instantanés, mais il impose des contraintes techniques (gestion de canaux, liquidité entrante, nœud en ligne...) qui peuvent freiner les débutants. Spark supprime ces contraintes tout en restant compatible avec Lightning.

## Installation et configuration

Dans ce tutoriel, nous nous basons sur la version Android de Blitz Wallet, mais tous les processus présentés ci-dessous sont également valables sur iOS.

![installation](assets/fr/01.webp)

Blitz Wallet étant un portefeuille en self-custody, vous avez le choix entre **créer un nouveau portefeuille** ou **importer une phrase de récupération** (12 ou 24 mots) d'un portefeuille existant.

Ici, nous partons sur la création d'un nouveau portefeuille. Retrouvez ci-dessous nos recommandations sur la sauvegarde de votre phrase de récupération :

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **IMPORTANT** : Ces 12 ou 24 mots de récupération sont **la seule clé d'accès à vos bitcoins**. Blitz est un portefeuille self-custodial : ni Blitz ni Spark n'ont accès à votre phrase de récupération ni à vos fonds. Si vous perdez ces mots, vous perdrez définitivement l'accès à vos bitcoins. Ne les partagez avec personne : quiconque les possède peut dépenser vos bitcoins.

Créez ensuite un **code PIN** pour sécuriser l'accès à votre portefeuille.

![setup-wallet](assets/fr/02.webp)

## Débuter avec Blitz

Effectuer des transactions avec Blitz est plus intuitif que dans la plupart des autres portefeuilles Bitcoin. L'interface est minimaliste et centrée sur trois actions principales : envoyer, scanner et recevoir.

### Recevoir des bitcoins

Pour recevoir des bitcoins sur votre portefeuille Blitz, cliquez sur l'icône **"Flèche bas"** (↓), saisissez le montant en satoshis que vous souhaitez recevoir, ajoutez une description optionnelle, puis le portefeuille générera une facture (invoice) que vous pourrez partager à votre expéditeur.

⚠️ **NOTE** : Le satoshi (ou "sat") est la plus petite unité de bitcoin : **1 bitcoin = 100 000 000 satoshis**.

L'une des particularités de Blitz Wallet est qu'il supporte plusieurs réseaux et protocoles de l'écosystème Bitcoin :

- **Lightning Network** : L'une des surcouches de Bitcoin qui permet d'effectuer des micropaiements instantanément avec des frais très faibles. Idéal pour les petits montants du quotidien.

- **Bitcoin (on-chain)** : La blockchain principale du protocole Bitcoin, adaptée pour les transactions de montants plus importants où la sécurité maximale et la finalité sont prioritaires.

- **Liquid Network** : Une sidechain (chaîne parallèle) de Bitcoin développée par Blockstream, qui permet des transactions rapides et confidentielles en utilisant des Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Par défaut, Blitz génère une facture Lightning, mais vous pouvez choisir le réseau sur lequel vous souhaitez recevoir vos satoshis en cliquant sur le bouton **"Choose format"** (Choisir le format).

![receive-sats](assets/fr/03.webp)

### Créer des contacts

Blitz Wallet simplifie l'envoi récurrent de bitcoins grâce à son système de contacts.

Dans le menu **Contacts**, vous pouvez enregistrer des noms d'utilisateurs Blitz ou des adresses Lightning (LNURL) avec lesquelles vous interagissez fréquemment.

Vous pourrez ainsi envoyer des satoshis à ces adresses en quelques clics, sans avoir à scanner un QR code ou saisir manuellement une adresse à chaque fois.

### Envoyer des bitcoins

Outre les méthodes classiques d'envoi de bitcoin (scan de QR code, saisie manuelle d'adresse), Blitz propose plusieurs options pratiques :

- **Depuis une image** (*From Image*) : Importez un QR code depuis votre galerie photo.
- **Depuis le presse-papiers** (*From Clipboard*) : Collez une adresse ou une facture copiée précédemment.
- **Saisie manuelle** (*Manual Input*) : Entrez directement une adresse Bitcoin, une facture Lightning ou une adresse lisible (par exemple `utilisateur@walletofsatoshi.com`).
- **Depuis vos contacts** : Sélectionnez un destinataire pré-enregistré pour envoyer en quelques clics.

Dans le menu **Wallet**, cliquez sur le bouton **"Flèche haut"** (↑), choisissez votre méthode d'envoi, saisissez le montant à envoyer, ajoutez une description et confirmez la transaction.

Le montant minimal pour effectuer un envoi est actuellement de **1 000 satoshis**.

![send-bitcoin](assets/fr/05.webp)

## Le magasin Blitz

Au-delà des opérations de transfert de bitcoins, Blitz Wallet intègre un magasin dans lequel vous pouvez dépenser vos bitcoins pour acheter des services numériques directement depuis l'application.

Depuis le menu principal, cliquez sur l'onglet **Store** pour accéder au magasin. Vous y trouverez également un accès à la plateforme **Bitrefill** qui permet d'acheter des cartes cadeaux auprès de milliers de commerçants dans le monde entier, directement en bitcoin.

- **Intelligence artificielle** : Accédez aux derniers modèles d'IA générative (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) et payez vos crédits directement en satoshis. Plusieurs forfaits sont disponibles selon vos besoins (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **SMS anonymes** : Envoyez et recevez des SMS partout dans le monde sans révéler votre numéro de téléphone personnel. Le service est facturé en satoshis pour chaque message envoyé.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard** : Protégez votre vie privée en ligne en souscrivant à un abonnement VPN WireGuard (hebdomadaire, mensuel ou trimestriel), payable en bitcoin directement depuis le magasin Blitz. Il vous suffira de télécharger l'application client WireGuard sur votre appareil pour en profiter.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet en coulisses : aller plus loin

Derrière la simplicité d'utilisation de Blitz Wallet se cache une architecture technique bien pensée qui combine plusieurs couches de l'écosystème Bitcoin.

### La répartition de votre solde

Blitz Wallet gère votre solde de manière transparente en répartissant vos fonds entre les différents protocoles en fonction des besoins. Lorsque votre solde est inférieur à 500 000 satoshis, Blitz utilise le **Liquid Network** et des échanges atomiques (*atomic swaps*) pour vous offrir une expérience fluide et permettre des transactions sur le Lightning Network même avec de petits montants.

Cette approche garantit une prise en main simple pour les nouveaux utilisateurs, sans qu'ils aient besoin de comprendre les mécanismes sous-jacents. Vous pouvez consulter la répartition de votre solde entre les différentes couches dans le menu **Paramètres > Balance Info**.

![balance](assets/fr/09.webp)

### Le mode Lightning (optionnel)

Par défaut, Blitz Wallet utilise le Liquid Network et le protocole Spark pour vous offrir une expérience fluide sans configuration technique. Cependant, Blitz vous donne la possibilité d'activer le **mode Lightning** qui ouvrira automatiquement un canal de paiement lorsque vous atteindrez un solde de **500 000 satoshis** (0,005 BTC).

Pour activer le mode Lightning, rendez-vous dans les **Paramètres**, puis dans la section **Paramètres Techniques**, cliquez sur l'option **Node Info**.

![enable-lightning](assets/fr/10.webp)

Grâce au protocole Spark, cette activation est **optionnelle** : Spark permet déjà d'effectuer des paiements compatibles Lightning sans avoir besoin d'ouvrir de canal ni de gérer de liquidité entrante. Le mode Lightning natif reste utile pour les utilisateurs avancés qui souhaitent disposer de leur propre noeud Lightning intégré au sein de l'application.

### Point de vente (PoS)

Blitz Wallet intègre une fonctionnalité de **point de vente** qui permet aux commerçants d'accepter les paiements en bitcoin directement depuis l'application.

Dans le menu **Paramètres > Point-of-sale**, vous pouvez configurer :

- L'identifiant unique de votre magasin
- La devise fiduciaire locale dans laquelle afficher les prix
- Les instructions pour vos employés
- L'option de pourboire pour vos clients

Vos clients n'ont qu'à scanner le QR code généré pour effectuer leur paiement en bitcoin, de manière instantanée.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Ressources utilisées pour rédiger ce tutoriel :
- Blog de [Breez](https://breez.technology/) Technology : [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).