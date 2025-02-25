---
name: Sparrow Wallet
description: Installer, configurer et utiliser Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet est un logiciel de gestion de portefeuille Bitcoin en self-custody développé par Craig Raw. Ce logiciel open-source est apprécié par les bitcoiners pour ses nombreuses fonctionnalités et son interface intuitive.

Il existe deux manières d'utiliser Sparrow :
- Comme un portefeuille chaud, où vos clés privées sont stockées sur votre PC.
- Comme un gestionnaire pour un portefeuille froid, où les clés privées sont conservées sur un hardware wallet. Dans ce mode, Sparrow manipule uniquement les informations publiques de votre portefeuille, trace les fonds, génère des adresses, et construit des transactions, mais la signature du hardware wallet est nécessaire pour rendre ces transactions valides. Il peut ainsi remplacer des applications comme Ledger Live ou Trezor Suite.

Sparrow supporte les portefeuilles à signature unique et multi-signatures, et permet une gestion fluide de plusieurs portefeuilles. Vous pouvez par exemple contrôler simultanément un portefeuille connecté à une Ledger, un autre à une Trezor, et avoir en plus un portefeuille chaud.

Le logiciel offre également des fonctionnalités avancées de contrôle des pièces (*coin control*), permettant de choisir précisément quels UTXO utiliser dans vos transactions pour optimiser votre confidentialité.

En termes de connexion, Sparrow vous permet de vous connecter à votre propre nœud Bitcoin, soit à distance via un Electrum Server, soit avec Bitcoin Core. Il est également possible d'utiliser un nœud public si vous ne disposez pas encore de votre propre nœud. Les connexions à distance se font via Tor.

## Installer Sparrow Wallet

Rendez-vous sur le site officiel de Sparrow Wallet [sur la page de téléchargement](https://sparrowwallet.com/download/), puis téléchargez le logiciel adapté à votre système.

01

Avant de l'installer, je vous conseille vivement de vérifier son authenticité et son intégrité. Si vous ne savez pas comment le faire, nous avons un tutoriel complet dédié :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Après avoir installé Sparrow, vous pouvez passer les premières explications pour arriver jusqu'à l'écran des connexions.

02

## Se connecter au réseau Bitcoin

Pour pouvoir disposer des informations de la blockchain Bitcoin et diffuser vos transactions, Sparrow doit pouvoir se connecter à un noeud Bitcoin. Il existe 3 manière différentes de le faire :
- 🟡 Avec une noeud "public", c'est à dire que vous vous connectez au noeud d'une autre personne ou d'une entité qui accepte ces connexions. Si vous n'avez pas votre propre noeud Bitocin, vous pouvez choisir cette option. Elle vous permet de commencer à utiliser Sparrow imémdiatement. Cependant, le noeud choisi verra passer toutes vos transactions, ce qui est un problème pour votre confidentialité. Être en self-custody, c'est bien, mais avoir son propre noeud Bitcoin, c'est mieux. Donc choisissez cette option uniquement si vous êtes débutant, et soyez conscient des risques que cela implique pour votre confidentialité ;
- 🟢 Avec un nœud Bitcoin Core. Si vous avez votre propre noeud Bitcoin Core, vous pouvez vous y connecter depuis Sparrow Wallet, soit en local si Bitcoin Core est sur la même machine, soit à distance.
- 🔵 Avec un serveur Electrum. Si votre noeud Bitcoin dispose de Electrs, par exemple si vous un node-in-box comme Umbrel ou Start9, vous pouvez vous y connecter à distance depuis Sparrow.

Vous l'aurez compris, il vaut mieux privilégier les connexions via Electrs ou via Bitocin Core sur votre propre noeud.

### Se connecter à un noeud public 🟡

Pour vous connecter à une noeud public c'est très simple. Cliquez sur l'onglet "Public Server".

03

Choisissez un noeud dans la liste déroulante.

04

Puis, cliquez sur le bouton "? Test Connection".

05

Sparrow Wallet est bien connecté. Si vous quittez cette fenêtre, vous verrez en bas à droite une coche jaune indiquant que vous êtes connecté à un nœud public.

06

### Se connecter à un Bitcoin Core 🟢

La deuxième solution pour communiquer avec un nœud Bitcoin est de connecter Sparrow à un Bitcoin Core qui se trouve soit sur la même machine, et dans ce cas on va utiliser le fichier cookie pour s'authentifier, ou bien à distance sur une autre machine, et dans ce cas le mot de passe configuré dans le fichier `bitcoin.conf`.






### Se connecter à un serveur Electrum 🔵





## Créer un portefeuille chaud




## Gérer un portefeuille froid




## Recevoir des bitcoins






## Envoyer des bitcoins




