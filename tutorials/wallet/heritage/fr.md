---
name: Heritage
description: Un portefeuille Bitcoin avec mécanisme d'héritage intégré via scripts Taproot
---

![cover](assets/cover.webp)

La transmission de bitcoins en cas de décès ou d'incapacité représente un défi majeur pour tout détenteur de crypto-actifs. Sans plan d'héritage adapté, ces actifs deviennent irrécupérables pour vos proches.

Heritage apporte une réponse élégante en implémentant un mécanisme de dead-man switch directement sur la blockchain Bitcoin. Ce portefeuille open-source permet de configurer des conditions de succession on-chain : si le propriétaire n'effectue plus de transactions pendant une période définie, des clés alternatives prédésignées peuvent débloquer les fonds.

## Qu'est-ce que Heritage ?

Heritage est un portefeuille Bitcoin intégrant nativement un mécanisme d'héritage via les scripts Taproot. Développé sous licence MIT par Jérémie Rodon, ce logiciel open-source garantit transparence et pérennité.

Heritage fonctionne grâce à des scripts Taproot encodés dans les adresses Bitcoin. Chaque UTXO intègre deux types de conditions de dépense :

- **Chemin primaire** : Le propriétaire peut dépenser ses bitcoins à tout moment avec sa clé principale
- **Chemins alternatifs** : Pour chaque héritier désigné, un script combine sa clé publique avec un verrou temporel (timelock)

Chaque transaction du propriétaire repousse automatiquement la date d'activation des clauses d'héritage. En cas d'inactivité prolongée (décès, incapacité), les conditions s'enclenchent automatiquement.

## Le service Heritage (optionnel)

Heritage propose deux formules d'utilisation :

**Faites-le vous-même (gratuit)** : L'application open-source seule. Vous gérez tout en autonomie avec votre propre nœud. Cette option offre l'accès de secours intégré, l'héritage intégré et le contrôle exclusif de vos bitcoins. Cependant, vous devez créer vos propres alertes (calendrier, rappels) pour ne pas oublier de renouveler vos timelocks, et il n'y a pas de notification automatique pour vos héritiers.

**Utilisez le service (0,05% par an)** : Le service btc-heritage.com ajoute des fonctionnalités pour simplifier la gestion :
- Rappels automatiques avant l'expiration de vos délais
- Notifications automatiques aux héritiers pour les guider dans la récupération
- Support prioritaire
- Gestion simplifiée des descripteurs

Tarification : 0,05% du montant géré par an, minimum 0,5 mBTC/an. Première année gratuite.

Le service reste non-custodial : vos clés privées ne quittent jamais votre appareil. Heritage ne peut pas accéder à vos fonds.

## Heritage CLI

Pour les utilisateurs avancés préférant le terminal, Heritage propose un outil en ligne de commande (CLI) offrant un contrôle granulaire et permettant une utilisation sur machine air-gapped.

![Page Heritage CLI](assets/fr/03.webp)

La documentation complète du CLI est disponible sur [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Vous y trouverez toutes les instructions pour le téléchargement, la connexion au service, la création de wallets (avec Ledger ou clés locales), la gestion des héritiers et des transactions.

Ce tutoriel se concentre sur l'application Desktop, plus accessible pour la majorité des utilisateurs.

## Heritage Desktop

Heritage Desktop est l'application graphique offrant une interface intuitive qui guide l'utilisateur à travers chaque étape de configuration.

### Téléchargement

Rendez-vous sur [btc-heritage.com](https://btc-heritage.com) et cliquez sur "Télécharger l'application".

![Page d'accueil Heritage](assets/fr/01.webp)

Choisissez la version correspondant à votre système d'exploitation (Linux 64bits ou Windows 64bits). Les binaires ne sont pas signés numériquement, ce qui peut déclencher des avertissements de sécurité.

![Page de téléchargement](assets/fr/02.webp)

### Installation sur Linux

Sur Linux, l'application est distribuée au format AppImage. Avant de pouvoir l'exécuter, vous devez installer la dépendance `libfuse2` :

```bash
sudo apt install libfuse2
```

![Installation libfuse2](assets/fr/04.webp)

Ensuite, rendez le fichier exécutable et lancez-le :

```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```

### Premier lancement

Au premier lancement, l'assistant d'onboarding vous propose trois choix :

![Onboarding initial](assets/fr/05.webp)

- **Setup an Heritage Wallet** : Créer un nouveau wallet avec plan d'héritage
- **Inherit bitcoins** : Récupérer des bitcoins en tant qu'héritier
- **Explore by myself** : Explorer les fonctionnalités sans assistance

Sélectionnez "Setup an Heritage Wallet" pour créer votre premier wallet.

### Connexion au réseau Bitcoin

Choisissez comment vous connecter au réseau Bitcoin :

![Choix connexion](assets/fr/06.webp)

- **Using the Heritage Service** : Infrastructure gérée, plus simple pour les héritiers
- **Using my own node** : Connexion à votre propre nœud Bitcoin Core ou Electrum

Pour ce tutoriel, nous utilisons notre propre nœud.

### Gestion des clés privées

Sélectionnez comment gérer vos clés privées :

![Gestion des clés](assets/fr/07.webp)

- **With a Ledger Hardware Device** : Sécurité maximale avec hardware wallet (recommandé)
- **Local storage with password** : Clés stockées localement avec protection par mot de passe
- **Restore an existing wallet** : Restaurer depuis une seed existante

### Configuration du nœud

Si vous utilisez votre propre nœud, l'application vous guide pour le configurer. Assurez-vous que votre nœud Bitcoin ou Electrum est :
- Installé et en cours d'exécution
- Synchronisé avec le réseau Bitcoin
- Configuré pour accepter les connexions RPC (pour Bitcoin Core)

![Configuration nœud](assets/fr/08.webp)

Cliquez sur "My Bitcoin node is up and running" une fois votre nœud prêt.

### Panneau Status

Cliquez sur "Status" en haut à droite puis "Open Configuration" pour accéder aux paramètres de connexion.

![Panneau Status](assets/fr/09.webp)

Configurez l'URL de votre serveur Electrum (par exemple `umbrel.local:50001` si vous utilisez Umbrel).

![Configuration Electrum](assets/fr/10.webp)

### Création du wallet

Une fois la connexion établie, cliquez sur "Create Wallet" dans l'onglet WALLETS.

![Créer wallet](assets/fr/11.webp)

Un popup vous explique l'architecture split de Heritage :

![Architecture split](assets/fr/12.webp)

1. **Key Provider (Offline)** : Gère vos clés privées et signe les transactions. Peut être un Ledger ou un wallet logiciel.
2. **Online Wallet** : Gère la synchronisation avec le réseau Bitcoin, la création d'adresses et la diffusion des transactions.

Remplissez le formulaire de création :

![Formulaire création wallet](assets/fr/13.webp)

- **Wallet Name** : Un nom unique pour identifier votre wallet
- **Key Provider** : Choisissez Local Key Storage pour ce tutoriel
- **New/Restore** : Sélectionnez "New" pour générer une nouvelle seed
- **Word Count** : 24 mots recommandé pour la sécurité maximale

Entrez un mot de passe robuste et choisissez les options pour l'Online Wallet :

![Options Online Wallet](assets/fr/14.webp)

- **Local Node** : Utilise votre propre nœud Electrum ou Bitcoin Core
- **Heritage Service** : Utilise le service Heritage (recommandé pour les fonctionnalités de notification)

Cliquez sur "Create Wallet" pour finaliser la création.

### Interface du wallet

Votre wallet est maintenant créé. L'interface affiche :

![Interface wallet](assets/fr/15.webp)

- Le solde (Balance)
- Les boutons SEND et RECEIVE
- L'historique des transactions
- L'historique des configurations Heritage
- Les adresses du wallet

### Création des héritiers

Accédez à l'onglet "HEIRS" pour créer vos héritiers.

![Page Heirs](assets/fr/16.webp)

Le popup d'information vous explique :
- Les héritiers sont des clés publiques Bitcoin associées à des personnes
- Chaque héritier possède sa propre phrase mnémotechnique
- Le premier héritier devrait être un "Backup" pour vous-même (en cas de perte de votre wallet principal)

#### Création de l'héritier Backup

Cliquez sur "Create Heir" et nommez-le "Backup".

![Création héritier Backup](assets/fr/17.webp)

Le popup explique pourquoi une phrase de 12 mots sans passphrase est sécurisée pour les héritiers :
1. **Pas d'accès immédiat** : Les clés héritier ne peuvent pas accéder aux fonds tant que le timelock n'est pas expiré
2. **Détection de compromission** : Si quelqu'un accède à la phrase, vous pouvez mettre à jour la configuration Heritage
3. **Accessibilité long-terme** : Une passphrase pourrait être oubliée après des années

Configurez l'héritier :

![Configuration héritier](assets/fr/18.webp)

- **Key Provider** : Local Key Storage
- **New** : Générer une nouvelle seed
- **Word Count** : 12 mots

Finalisez la création :

![Finalisation héritier](assets/fr/19.webp)

- **Heir Type** : Extended Public Key
- **Export to Service** : Optionnel, permet les notifications automatiques aux héritiers

L'héritier Backup est maintenant créé :

![Héritier créé](assets/fr/20.webp)

#### Sauvegarde de la phrase mnémotechnique de l'héritier

Cliquez sur l'héritier Backup puis sur "Show Mnemonic" :

![Afficher mnemonic](assets/fr/21.webp)

**IMPORTANT** : Notez soigneusement ces 12 mots et conservez-les en lieu sûr. C'est la clé qui permettra de récupérer les fonds.

![Phrase mnémotechnique](assets/fr/22.webp)

#### Suppression de la seed de l'application

Une fois la phrase notée, accédez aux paramètres de l'héritier (icône roue dentée) :

![Paramètres héritier](assets/fr/23.webp)

Utilisez "Strip Heir Seed" pour supprimer la clé privée de l'application. Confirmez que vous avez bien sauvegardé la phrase.

![Strip Heir Seed](assets/fr/24.webp)

Ceci est une mesure de sécurité : seule la clé publique reste dans l'application, suffisante pour configurer l'héritage.

#### Création d'un second héritier

Répétez le processus pour créer un second héritier (par exemple "Satoshi"). Vous aurez maintenant deux héritiers :

![Deux héritiers](assets/fr/25.webp)

- **Backup** : Votre clé de secours personnelle
- **Satoshi** : Un héritier désigné

### Configuration Heritage

Retournez sur votre wallet et cliquez sur l'icône paramètres :

![Paramètres wallet](assets/fr/26.webp)

Dans la section "Heritage Configuration", cliquez sur "Create" :

![Heritage Configuration](assets/fr/27.webp)

Configurez les délais pour chaque héritier :

![Configuration délais](assets/fr/28.webp)

- **Backup** : 180 jours (6 mois) - Maturity Date : 2026-06-18
- **Satoshi** : 455 jours (15 mois) - Maturity Date : 2027-03-20

**Important** : Chaque héritier doit avoir un délai plus long que le précédent. Le premier héritier (Backup) aura accès aux fonds en premier.

Configurez également :

![Configuration finale](assets/fr/29.webp)

- **Reference Date** : Date de départ pour calculer les délais
- **Minimum Maturity Delay** : Délai minimum après une transaction (10 jours recommandé)

Cliquez sur "Create" pour valider la configuration.

La configuration Heritage est maintenant active :

![Configuration active](assets/fr/30.webp)

Elle affiche les deux héritiers avec leurs délais et dates d'expiration respectives.

### Sauvegarde des descripteurs

**Important** : Sauvegardez les descripteurs de votre wallet. Sans eux, même avec la phrase mnémotechnique, la récupération des fonds est impossible.

Cliquez sur "Backup Descriptors" :

![Bouton Backup](assets/fr/31.webp)

Sauvegardez le fichier JSON contenant vos descripteurs Bitcoin :

![Backup descripteurs](assets/fr/32.webp)

Ce fichier devra être transmis à vos héritiers avec leurs phrases mnémotechniques respectives.

### Recevoir des bitcoins

Cliquez sur "RECEIVE" pour générer une adresse de réception :

![Recevoir bitcoins](assets/fr/33.webp)

Félicitations ! Votre Heritage Wallet est prêt à recevoir des bitcoins. Chaque adresse générée intègre automatiquement vos conditions d'héritage.

Après réception d'une transaction, votre solde est mis à jour :

![Solde mis à jour](assets/fr/34.webp)

L'historique affiche la transaction et la configuration Heritage associée.

---

## Récupération par un héritier

Lorsque le délai configuré est écoulé, l'héritier peut récupérer les fonds.

### Prérequis

L'héritier a besoin de :
1. Sa phrase mnémotechnique de 12 mots
2. Le fichier de backup des descripteurs (JSON) du wallet original

### Création d'un Heir Wallet

Dans l'onglet "INHERITANCES", un popup rappelle ces prérequis :

![Page Heir Wallets](assets/fr/35.webp)

**Attention** : Sans le fichier de backup des descripteurs, l'accès aux fonds est IMPOSSIBLE, même avec la phrase mnémotechnique correcte.

Cliquez sur "Create Heir Wallet" :

![Créer Heir Wallet](assets/fr/36.webp)

Remplissez le formulaire :

![Formulaire Heir Wallet](assets/fr/37.webp)

- **Heir Wallet Name** : Un nom pour identifier ce wallet héritier
- **Key Provider** : Local Key Storage
- **Restore** : Sélectionnez cette option pour entrer une phrase existante

Entrez les 12 mots de la phrase mnémotechnique de l'héritier et configurez le Heritage Provider :

![Entrée mnemonic](assets/fr/38.webp)

- **Heritage Provider** : "Local" pour utiliser votre propre nœud avec le fichier de backup

Chargez le fichier de backup JSON et cliquez sur "Create Heir Wallet" :

![Chargement backup](assets/fr/39.webp)

### Interface Heir Wallet

Le Heir Wallet est créé. Initialement, si le timelock n'est pas encore expiré, aucun héritage n'est disponible :

![Pas d'héritage disponible](assets/fr/40.webp)

Une fois le délai écoulé et après synchronisation avec le réseau Bitcoin, les fonds apparaissent dans la liste des héritages :

![Héritage disponible](assets/fr/41.webp)

L'interface affiche :
- Le type de clé et son fingerprint
- Le total des fonds héritables
- Le montant actuellement dépensable (0 sat si le timelock n'est pas encore expiré)
- La date de maturité et l'expiration

Lorsque la date de maturité est atteinte, le bouton "Spend" permet de transférer les bitcoins vers un wallet personnel.

---

## Bonnes pratiques

### Sauvegarde des descripteurs

Les descripteurs du wallet sont essentiels pour reconstruire vos adresses Heritage. **Leur sauvegarde est encore plus importante que celle de la seed.** Sans les descripteurs, même avec votre phrase mnémotechnique, vous ne pourrez pas retrouver vos fonds.

### Sécurité des clés

- Utilisez un Ledger pour la clé principale si possible
- Ne stockez jamais les phrases des héritiers au même endroit que la vôtre
- Dispersez les informations entre plusieurs supports et localisations

### Documentation pour vos proches

Rédigez des instructions claires expliquant chaque étape de la récupération. Vos héritiers ne seront peut-être pas familiers avec Bitcoin au moment critique.

## Alternatives

D'autres solutions existent pour gérer la transmission de vos bitcoins, notamment Liana et Bitcoin Keeper. Vous trouverez nos tutoriels ci-après :

https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Conclusion

Heritage permet de planifier sa succession Bitcoin de manière souveraine via l'application Desktop. La mise en place requiert une réflexion sur les délais appropriés et la sécurisation des secrets. N'oubliez pas de transmettre à vos héritiers :
- Leur phrase mnémotechnique de 12 mots
- Le fichier de backup des descripteurs
- Les instructions de récupération

## Ressources

- [Site officiel Heritage](https://btc-heritage.com)
- [Documentation CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)
