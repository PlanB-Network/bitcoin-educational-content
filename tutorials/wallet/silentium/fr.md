---
name: Silentium
description: Portefeuille web progressif avec support des Silent Payments (BIP-352)
---

![cover](assets/cover.webp)

La réutilisation d'adresses Bitcoin constitue l'une des menaces les plus directes pour la confidentialité des utilisateurs. Lorsqu'un destinataire partage une adresse unique pour recevoir plusieurs paiements, n'importe quel observateur peut retracer l'ensemble des transactions associées et reconstituer son historique financier. Ce problème affecte particulièrement les créateurs de contenu, les associations caritatives ou les activistes qui souhaitent afficher publiquement une adresse de donation sans compromettre leur vie privée.

Silentium répond à cette problématique en proposant une solution élégante accessible directement depuis votre navigateur. Cette application web progressive (PWA) open-source, lancée en mai 2024 par Louis Singer, implémente les Silent Payments (BIP-352) : une adresse statique réutilisable où chaque paiement aboutit sur une adresse blockchain distincte, sans interaction préalable ni lien observable entre les transactions.

**Avertissement important** : Silentium est un projet expérimental servant de *proof-of-concept* pour les wallets légers Silent Payments. Il ne doit pas être utilisé comme wallet quotidien ni pour stocker des montants significatifs. Les développeurs précisent explicitement : 

> Use at your own risk.

A noter qu'il est possible d'utiliser ce wallet en testnet ou bien regtest. 

## Qu'est-ce que Silentium ?

### Philosophie et objectifs

Silentium sert de démonstration technique pour implémenter les Silent Payments dans un wallet navigateur léger. Bien qu'il supporte aussi les adresses Bitcoin classiques, l'accent est mis sur les Silent Payments pour permettre aux utilisateurs d'expérimenter cette technologie de confidentialité simplement.

### Comment fonctionnent les Silent Payments ?

Les Silent Payments (BIP-352) utilisent l'échange de clés Diffie-Hellman sur courbe elliptique (ECDH). Le destinataire génère une adresse statique (`sp1...` sur mainnet, `tsp1...` sur testnet) composée de deux clés publiques : une clé de scan pour détecter les paiements, et une clé de dépense pour les utiliser.

L'expéditeur combine ses clés privées d'inputs avec la clé de scan du destinataire pour calculer un secret partagé générant un "tweak" cryptographique. Ce tweak, ajouté à la clé de dépense, crée une adresse Taproot unique pour chaque transaction. Le destinataire reproduit ce calcul avec sa clé privée de scan pour détecter et dépenser les fonds sans interaction préalable.

Avantages : confidentialité renforcée pour l'émetteur et le destinataire, aucun serveur tiers nécessaire, transactions indiscernables des paiements Taproot classiques. Inconvénient principal : scan intensif de la blockchain pour détecter les paiements.

Pour approfondir le fonctionnement théorique des Silent Payments, consultez la dernière partie du cours BTC,204 sur Plan ₿ Academy :

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Plateformes supportées

Silentium est une Progressive Web App (PWA) accessible depuis n'importe quel navigateur moderne (mobile ou desktop). Utilisez-la directement sur `app.silentium.dev`, installez-la comme application native via votre navigateur, ou déployez-la localement. L'installation se fait directement depuis le navigateur, sans passer par les stores officiels.

## Utilisation via la Web App

### Accès et installation

[Rendez-vous sur `https://app.silentium.dev/` depuis votre navigateur](https://app.silentium.dev/). L'application se charge instantanément et affiche l'écran d'accueil.

Pour l'installer comme application native sur iOS, appuyez sur le bouton de partage (carré avec flèche vers le haut) puis sélectionnez "Sur l'écran d'accueil". Sur Android, le navigateur propose généralement une notification "Ajouter à l'écran d'accueil" directement. Une fois installée, Silentium apparaît avec son icône dédiée et fonctionne comme une application native, mais nécessite une connexion internet pour synchroniser les transactions.

![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)

### Création du portefeuille

Au premier lancement, choisissez "Create Wallet" pour générer un nouveau portefeuille, ou "Restore Wallet" pour restaurer depuis une phrase de récupération existante.

Sélectionnez "Create Wallet". L'application génère une phrase de 12 mots que vous devez noter soigneusement. Cette phrase est l'unique moyen de récupérer vos fonds. Même sur testnet, adoptez les bonnes pratiques de sauvegarde. Appuyez sur "Continue" après avoir sauvegardé votre phrase.

L'application vous demande ensuite de définir un mot de passe pour sécuriser l'accès au wallet. Choisissez un mot de passe fort et confirmez-le.

![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)

Une fois la phrase confirmée et le mot de passe défini, vous accédez à l'interface principale.

### Interface principale et paramètres

L'interface principale affiche votre solde en satoshis (initialement 0 sats), avec trois boutons en bas :
- **Sync** : synchronise le wallet avec la blockchain
- **Receive** : pour recevoir des fonds
- **Send** : pour envoyer des bitcoins

Accédez aux paramètres via l'icône en haut à droite (trois barres horizontales). Le menu Settings propose plusieurs options :

- **About** : informations sur l'application
- **Backup** : sauvegarde de la phrase de récupération
- **Explorer** : choix de l'explorateur blockchain (Mempool par défaut) et du serveur Silentiumd
- **Network** : sélection du réseau (mainnet/testnet)
- **Password** : modification du mot de passe
- **Reload** : rechargement du wallet
- **Reset** : réinitialisation complète
- **Theme** : changement de thème

![Interface principale et paramètres avec Explorer](assets/fr/03.webp)

La section **Explorer** est particulièrement importante : elle vous permet de choisir l'explorateur blockchain utilisé (Mempool par défaut) et affiche également l'URL du serveur Silentiumd (`https://bitcoin.silentium.dev/v1` pour mainnet). Si vous hébergez votre propre serveur Silentiumd ou souhaitez utiliser le testnet, c'est ici que vous configurerez ces paramètres.

### Recevoir des fonds

Depuis l'interface principale, appuyez sur le bouton "Receive". Par défaut, Silentium affiche une adresse Silent Payment avec son QR code. L'adresse commence par `sp1...` sur mainnet ou `tsp1...` sur testnet.

Vous pouvez basculer entre adresse Silent Payment et adresse Bitcoin classique en utilisant le bouton "Switch to classic address" / "Switch to silent address" en bas de l'écran.

![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)


Une fois la transaction diffusée, patientez quelques minutes. Pour les paiements Silent Payments, Silentium scanne automatiquement la blockchain pour détecter les transactions qui vous sont destinées. Les transactions apparaissent avec le statut "Unconfirmed" avant de se confirmer progressivement.

### Envoyer un paiement

Depuis l'interface principale, appuyez sur le bouton "Send". L'écran d'envoi vous demande :

1. **Address** : collez une adresse Silent Payment (`sp1...` ou `tsp1...`) ou une adresse Bitcoin classique. Vous pouvez utiliser l'icône de scan QR pour scanner une adresse.
2. **Amount** : saisissez le montant en satoshis à envoyer. Un clavier numérique s'affiche pour faciliter la saisie. Votre solde disponible est affiché en haut pour référence.

![Envoi de fonds depuis Silentium](assets/fr/05.webp)

Une fois l'adresse et le montant saisis, appuyez sur "Proceed" pour continuer. L'application vous demandera de sélectionner le niveau de frais souhaité avant de confirmer la transaction.

## Self-hosting du wallet

### Pourquoi self-host ?

L'hébergement local de Silentium offre souveraineté totale, vérification du code, environnement de développement et résilience face aux pannes du site officiel.

### Prérequis

Node.js (version 14+), npm ou yarn, Git, et environ 500 Mo d'espace disque.

### Installation locale

Clonez le dépôt et installez les dépendances :

```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```

### Lancement et utilisation

Démarrez l'application en mode développement :

```bash
yarn start
```

Accédez à `http://localhost:3000` dans votre navigateur. Pour une version optimisée en production :

```bash
yarn build
```

Les fichiers générés dans `build/` peuvent être servis avec nginx, Apache ou tout serveur web. Par défaut, Silentium se connecte au serveur public `bitcoin.silentium.dev`. Modifiez cette configuration dans les paramètres pour utiliser testnet ou votre propre serveur.

## Le serveur Silentiumd

### Rôle et fonctionnement

Silentium utilise un serveur d'indexation **Silentiumd** pour optimiser la détection des paiements. Scanner toutes les transactions Taproot serait trop lourd pour un navigateur ou mobile.

Silentiumd pré-calcule les données intermédiaires (tweaks) pour chaque transaction Taproot. Votre wallet télécharge ces tweaks (quelques octets par transaction) et effectue le calcul final localement pour vérifier l'appartenance du paiement. Le serveur ne connaît jamais vos clés ni ne peut identifier vos transactions, contrairement aux serveurs Electrum classiques.

Les filtres compacts BIP158 permettent à votre wallet de déterminer quels blocs scanner sans révéler vos adresses, préservant ainsi votre confidentialité.

### Serveur public

Le serveur public `bitcoin.silentium.dev` (mainnet), sponsorisé par Vulpem Ventures, offre une expérience simple et immédiate. Bien que la confidentialité soit préservée, cette approche implique une confiance relative dans l'infrastructure tierce.

### Héberger son propre serveur Silentiumd

Pour une souveraineté totale, hébergez votre propre serveur Silentiumd. Prérequis : nœud Bitcoin Core non-élagué avec `txindex=1` et `blockfilterindex=1`, Go 1.21+, 10-20 Go d'espace disque, compétences en administration système.

**Installation :**

```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```

Configurez via variables d'environnement (consultez `config.md` du dépôt pour les détails). Le serveur indexe la blockchain et expose une API interrogeable par votre wallet.

Aucune solution packagée pour Umbrel ou Start9 n'existe actuellement, limitant l'accessibilité aux utilisateurs non techniques.

## Avantages et limitations

### Points forts

- **Accessibilité maximale** : utilisable depuis n'importe quel navigateur, aucune installation lourde requise
- **Multi-plateforme** : fonctionne sur mobile (Android/iOS) et desktop grâce à la technologie PWA
- **Self-hosting simple** : installation locale possible avec quelques commandes
- **Open-source** : code entièrement auditable sur GitHub
- **Privacy-focused** : aucun tracking, aucune analytics, calculs cryptographiques locaux
- **Architecture séparée** : séparation claire entre wallet (client) et serveur d'indexation
- **Sans compte** : aucune inscription ni donnée personnelle requise

### Contraintes à considérer

- **Projet expérimental** : preuve de concept uniquement, non destiné à un usage quotidien ou production
- **Aucune garantie** : risque de bugs, vulnérabilités, perte de fonds possible
- **Support limité** : peu de documentation utilisateur, communauté restreinte, pas de support officiel
- **Dépendance serveur** : nécessite un serveur Silentiumd fonctionnel (public ou self-hosted)
- **Scan intensif** : la détection des paiements Silent Payments consomme de la bande passante
- **Fonctionnalités réduites** : pas de coin control, pas de Lightning, pas de multi-signatures

## Bonnes pratiques

### Sécurité de la seed

Même sur testnet, traitez votre phrase de récupération avec sérieux. Notez-la sur papier et conservez-la en lieu sûr. Maintenez des wallets séparés pour testnet et mainnet : n'utilisez jamais une seed de test sur un wallet destiné à des fonds réels.

### Vérification du code source

L'un des avantages du self-hosting est la possibilité de vérifier le code source avant de l'exécuter. Si vous envisagez d'utiliser Silentium avec des fonds réels, prenez le temps d'auditer le code ou faites appel à un développeur de confiance pour le faire. Comparez également le hash du code déployé sur `app.silentium.dev` avec celui du dépôt GitHub pour vous assurer de l'authenticité.

### Sauvegarde et restauration

La récupération de fonds Silent Payments nécessite un portefeuille compatible avec le protocole BIP-352. Un wallet standard ne peut pas scanner la blockchain pour retrouver vos UTXO Silent Payments. Conservez Silentium installé ou assurez-vous d'avoir accès à un autre wallet compatible (comme Cake Wallet ou d'autres implémentations futures) pour restaurer vos fonds si nécessaire.

## Conclusion

Silentium offre un terrain d'expérimentation accessible pour comprendre les Silent Payments sans friction technique. En tant que preuve de concept, il démontre comment cette technologie de confidentialité peut être intégrée dans un wallet navigateur tout en préservant l'auto-custody. Expérimentez sur testnet pour découvrir cette avancée prometteuse pour la confidentialité on-chain.

## Ressources

### Documentation officielle
- Dépôt GitHub Silentium (wallet) : https://github.com/louisinger/silentium
- Dépôt GitHub Silentiumd (serveur) : https://github.com/louisinger/silentiumd
- Application web : https://app.silentium.dev/
- Site communautaire Silent Payments : https://silentpayments.xyz
- Spécification BIP-352 : https://bips.dev/352

### Articles et ressources
- Annonce officielle (Twitter) : https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin : https://www.nobsbitcoin.com/silentium-silent-payments/
- Bitcoin Optech - Silent Payments : https://bitcoinops.org/en/topics/silent-payments/

### Outils testnet
- Testnet faucet : https://testnet-faucet.com/
- Explorateur testnet Mempool : https://mempool.space/testnet
