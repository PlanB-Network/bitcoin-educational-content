---
name: SwapMarket
description: Agrégateur de services de swaps Bitcoin et Lightning
---

![cover](assets/cover.webp)

Transférer des fonds entre Bitcoin on-chain et Lightning Network nécessite généralement soit l'ouverture manuelle de canaux Lightning (technique et coûteuse), soit le recours à des plateformes d'échange centralisées avec KYC. SwapMarket offre une alternative : des swaps atomiques trustless via des providers compétitifs, sans KYC.

L'innovation : bien que les providers soient des intermédiaires, les HTLC (*Hash Time Locked Contracts*) garantissent mathématiquement que vos fonds restent sous votre contrôle. L'agrégation de plusieurs providers (Boltz, ZEUS Swaps, Eldamar, Middle Way) crée une compétition tarifaire. Interface web open-source self-hostable.

## Qu'est-ce que SwapMarket ?

Agrégateur open-source lancé en 2024, SwapMarket fonctionne comme un comparateur de providers de swaps Bitcoin/Lightning. L'utilisateur compare instantanément les conditions (frais, liquidité, limites) et choisit le provider optimal.

### Architecture technique

**Frontend client-side** : Application 100% client-side (fork Boltz Web App) hébergée sur GitHub Pages. Le code s'exécute dans le navigateur sans serveur backend. Historique stocké en local (cookies/cache). Code source public et auditable.

**Découverte des providers** : Liste hardcodée dans `src/configs/mainnet.ts`. Nouveaux providers ajoutés via Pull Request ou email.

**Backends indépendants** : Chaque provider opère son propre backend Boltz. L'interface interroge les APIs en temps réel pour comparer les quotes instantanément.

**Swaps atomiques HTLC** : Hash Time Locked Contracts garantissent l'atomicité : soit le swap s'exécute, soit chaque partie récupère ses fonds. Risque de contrepartie mathématiquement éliminé.

### Philosophie

SwapMarket réduit la centralisation en créant une compétition entre providers pour les frais et la liquidité. Pas de KYC, code open-source self-hostable, multiplication des opérateurs indépendants pour éviter les points de défaillance unique.

## Fonctionnalités principales

### Marketplace de providers

L'interface affiche tous les fournisseurs actifs : nom du provider, frais appliqués (pourcentage et/ou fixe), montants minimum/maximum disponibles, et types de swaps supportés. L'application interroge directement les APIs de chaque provider référencé dans le fichier de configuration pour récupérer les quotes en temps réel. La compétition entre providers garantit des tarifs optimaux, généralement autour de 0,5% pour les swaps standards.

### Swaps bidirectionnels

**Swap-in (on-chain → Lightning)** : Convertir des BTC on-chain en satoshis Lightning. Cas d'usage : alimenter un wallet Lightning mobile, obtenir de la capacité entrante sur un nœud, ou disposer de liquidité instantanée.

**Swap-out (Lightning → on-chain)** : Convertir des satoshis Lightning en BTC on-chain. Cas d'usage : vider un wallet Lightning vers du cold storage ou rééquilibrer la liquidité entre couches.

### Sécurité et récupération

**Swaps atomiques trustless** : Les HTLC garantissent que soit l'échange se réalise complètement, soit chaque partie récupère sa mise. Le risque de contrepartie est mathématiquement éliminé.

**Mécanisme de remboursement** : Chaque swap possède un délai d'expiration (timelock). Si le swap échoue, les fonds sont automatiquement remboursables après expiration. L'utilisateur conserve toujours la possibilité de récupérer ses bitcoins.

**Clés de secours** : SwapMarket permet d'exporter des clés de récupération pour les swaps en cours. En cas de problème, ces clés permettent de finaliser ou annuler un swap depuis n'importe quel dispositif.

## Installation et accès

### Interface web

SwapMarket ne nécessite aucune installation. L'accès se fait via navigateur en visitant https://swapmarket.github.io. Pour une confidentialité maximale, privilégiez Brave, Firefox avec extensions anti-tracking, ou LibreWolf. Tor Browser est recommandé pour l'anonymat réseau.

Pas d'inscription, ni email, ni vérification d'identité requis.

### Self-hosting (optionnel)

Pour les utilisateurs techniques souhaitant éliminer toute dépendance au domaine GitHub Pages officiel, SwapMarket peut être exécuté localement :

**Via npm** :
```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```

**Via Docker** :
```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```

L'application sera accessible sur `http://localhost:3000`. Le self-hosting garantit un contrôle total sur l'interface, élimine le risque de censure du domaine officiel, et permet d'auditer le code source avant exécution.

### Configuration initiale

**Wallet Lightning** : Assurez-vous d'avoir un wallet Lightning opérationnel (Phoenix, Zeus, BlueWallet, etc.). Pour les swap-in, vous générerez une facture Lightning. Pour les swap-out, vous paierez une facture Lightning.

**Wallet on-chain** : Pour les swap-in, vous aurez besoin d'un wallet Bitcoin on-chain pour envoyer des fonds. Pour les swap-out, préparez une adresse de réception Bitcoin.

**Configuration optionnelle** : SwapMarket stocke l'historique des swaps et les préférences dans les cookies du navigateur. Aucune création de compte n'est nécessaire.

## Accès aux paramètres et Rescue Key

Avant de réaliser vos premiers swaps, il est fortement recommandé de télécharger votre **Rescue Key** (clé de récupération). Cette clé de secours permet de récupérer vos fonds en cas de problème technique ou de perte d'accès à votre appareil.

### Accéder aux paramètres

Depuis la page principale de SwapMarket, cliquez sur l'icône d'engrenage (⚙️) située en haut à droite de l'interface, à côté du formulaire de swap.

![Accès aux paramètres](assets/fr/01.webp)

### Page Settings

La page Settings s'ouvre et affiche plusieurs options de configuration :

- **Denomination** : Choix entre BTC ou sats
- **Decimal Separator** : Séparateur décimal (, ou .)
- **Audio/Browser Notifications** : Notifications sonores et navigateur
- **Rescue Key** : Téléchargement de la clé de récupération
- **Logs** : Consultation, téléchargement ou suppression des logs

![Page Settings](assets/fr/02.webp)

### Télécharger la Rescue Key

Cliquez sur le bouton **Download** (icône de téléchargement) à côté de "Rescue Key".

**Points importants** :
- La Rescue Key est une **clé de secours unique** qui fonctionne pour tous vos swaps futurs
- Conservez cette clé dans un endroit **sécurisé et permanent** (gestionnaire de mots de passe, coffre-fort numérique)
- En cas de problème avec un swap (timeout, échec technique), cette clé permet de récupérer vos fonds

## Réaliser un swap pas à pas

### Swap-out : Lightning → Bitcoin

Ce premier exemple montre comment convertir des satoshis Lightning en bitcoins on-chain.

**Étape 1 : Configuration du swap**

Depuis la page principale, sélectionnez dans le formulaire de swap :
- **LIGHTNING** (champ supérieur) : Saisissez le montant que vous souhaitez envoyer en sats Lightning (exemple : 30 000 sats)
- **BITCOIN** (champ inférieur) : Le montant que vous recevrez s'affiche automatiquement après déduction des frais (exemple : 29 320 sats)

Dans le champ du bas, collez votre **adresse Bitcoin de réception** où vous souhaitez recevoir les fonds. Vérifiez méticuleusement cette adresse.

Le provider affiché par défaut est généralement Boltz Exchange. Les frais du réseau (Network Fee) et les frais du provider (Provider's Fee) sont affichés clairement.

![Configuration swap-out](assets/fr/03.webp)

**Étape 2 : Sélection du provider**

Cliquez sur le menu déroulant du provider (par défaut "Boltz Exchange") pour afficher tous les fournisseurs de liquidité disponibles.

Une fenêtre modale s'ouvre affichant un tableau comparatif :
- **Status** : Indicateur vert si le provider est actif
- **Alias** : Nom du provider (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- **Fee** : Frais appliqués par le provider (généralement entre 0,49% et 0,5%)
- **Max Swap** : Montant maximum accepté pour un swap

Comparez les frais et montants maximum, puis sélectionnez le provider de votre choix.

**À noter** : L'interface de sélection des providers n'affiche pas les **montants minimums** pour chaque provider. Ces informations apparaissent uniquement dans l'interface de création du swap, après avoir sélectionné un provider. Les minimums et maximums peuvent varier selon les providers et évoluer dans le temps. **Vérifiez toujours ces limites au moment de votre swap** : si le montant que vous souhaitez échanger est en dehors des limites d'un provider, vous pouvez en sélectionner un autre plus adapté à votre transaction.

![Sélection du provider](assets/fr/04.webp)

**Étape 3 : Création du swap et paiement Lightning**

Cliquez sur le bouton jaune **"CREATE ATOMIC SWAP"**. SwapMarket génère une **facture Lightning** (BOLT11) que vous devez payer depuis votre wallet Lightning.

La page affiche :
- **Swap ID** : Identifiant unique du swap (exemple : J4ymFIMVR6Hm)
- **Status** : "swap.created" (swap créé, en attente de paiement)
- **QR code** : Scannez-le avec votre wallet Lightning
- **Facture Lightning** : Chaîne de caractères commençant par "lnbc" (exemple : lnbc300u1p50whiv...gn5dk2szgqkvfkzc)

Payez cette facture depuis votre wallet Lightning (Phoenix, Zeus, BlueWallet, etc.). Le montant exact à payer est affiché (exemple : 30 000 sats).

![Paiement Lightning](assets/fr/05.webp)

**Étape 4 : Confirmation et réception**

Une fois le paiement Lightning confirmé, SwapMarket reçoit instantanément votre paiement et le provider diffuse la transaction Bitcoin vers votre adresse.

Le statut passe à **"invoice.settled"** (facture payée), et un message de confirmation s'affiche.

Vos bitcoins on-chain seront disponibles dès la confirmation de la transaction (généralement quelques minutes à quelques heures selon les frais de minage choisis par le provider).

![Confirmation swap-out](assets/fr/06.webp)

Vous pouvez cliquer sur **"OPEN CLAIM TRANSACTION"** pour voir la transaction Bitcoin sur un explorateur de blockchain.

### Swap-in : Bitcoin → Lightning

Ce second exemple montre comment convertir des bitcoins on-chain en satoshis Lightning.

**Étape 1 : Configuration du swap**

Depuis la page principale, sélectionnez dans le formulaire de swap :
- **BITCOIN** (champ supérieur) : Saisissez le montant que vous souhaitez envoyer en sats Bitcoin (exemple : 63 400 sats)
- **LIGHTNING** (champ inférieur) : Le montant que vous recevrez s'affiche automatiquement après déduction des frais (exemple : 62 884 sats)

Dans le champ du bas, collez une **facture Lightning** (BOLT11) générée depuis votre wallet Lightning, ou utilisez votre adresse LNURL si votre wallet la supporte.

![Configuration swap-in](assets/fr/07.webp)

**Étape 2 : Vérification de la Rescue Key**

Après avoir cliqué sur **"CREATE ATOMIC SWAP"**, une fenêtre modale apparaît vous demandant de vérifier votre Rescue Key.

![Modal Rescue Key](assets/fr/08.webp)

**Boltz Rescue Key** : Comme vous avez déjà téléchargé votre clé de récupération lors de la configuration initiale (voir section précédente), cliquez sur le bouton **"VERIFY EXISTING KEY"** pour importer la clé que vous avez sauvegardée.

Sélectionnez le fichier de la Rescue Key téléchargée précédemment. Une fois la vérification réussie, l'interface bascule automatiquement sur l'étape suivante.

**Étape 3 : Adresse de dépôt Bitcoin**

SwapMarket génère maintenant une **adresse Bitcoin unique** contenant le contrat HTLC lié à votre facture Lightning.

La page affiche :
- **Swap ID** : Identifiant unique (exemple : 1kGmB6JyGqU4)
- **Status** : "invoice.set" (facture définie, en attente de paiement Bitcoin)
- **QR code** : Adresse Bitcoin de dépôt
- **Adresse Bitcoin** : Commençant généralement par "bc1p..." (exemple : bc1p5mvtwxapjkds...9d4n9f)
- **Warning en jaune** : "Make sure your transaction confirms within ~24 hours after creation of this swap!"

Ce délai de ~24 heures est le **timeout** du contrat HTLC. Si votre transaction Bitcoin n'est pas confirmée dans ce délai, le swap échouera et vous devrez utiliser votre Rescue Key pour récupérer vos fonds.

![Adresse de dépôt Bitcoin](assets/fr/09.webp)

Vous pouvez copier l'adresse en cliquant sur le bouton **"ADDRESS"** ou scanner le QR code directement depuis votre wallet on-chain.

**Étape 4 : Envoi des bitcoins**

Depuis votre wallet Bitcoin on-chain, envoyez **exactement** le montant indiqué (exemple : 63 400 sats) vers l'adresse générée.

**Important** : Utilisez des frais de minage appropriés pour garantir une confirmation rapide. Si les frais sont trop bas et que la transaction reste en mempool au-delà du timeout (~24h), le swap échouera.

Une fois la transaction envoyée, SwapMarket détecte qu'elle est dans la mempool et affiche :
- **Status** : "transaction.mempool"
- **Message** : "Transaction is in mempool - Waiting for confirmation to complete the swap"

![Transaction en mempool](assets/fr/10.webp)

**Étape 5 : Confirmation et réception Lightning**

Dès que la transaction Bitcoin obtient sa première confirmation, le provider paie automatiquement votre facture Lightning. Vous recevez instantanément les satoshis sur votre wallet Lightning.

Le statut passe à **"transaction.claim.pending"**, puis un message de confirmation s'affiche :

![Confirmation swap-in](assets/fr/11.webp)

Vos satoshis Lightning sont immédiatement disponibles dans votre wallet.

## Avantages et limitations

### Avantages

**Compétition tarifaire** : L'agrégation de providers crée une compétition naturelle tirant les frais vers le bas (0,49% à 0,5%).

**Confidentialité** : Absence de KYC, interface 100% client-side (pas de transmission de données personnelles), compatible Tor Browser.

**Non-custodial** : HTLC garantissent mathématiquement le contrôle exclusif de vos fonds. Soit le swap aboutit, soit vous récupérez vos bitcoins.

**Open-source self-hostable** : Code public auditable, déployable localement pour résistance maximale à la censure.

### Limitations

**Liquidité limitée** : Nombre restreint de providers actifs (Boltz, Eldamar, MiddleWay selon périodes). Les montants maximum peuvent être limités.

**Délais d'expiration** : Timeout de 24h à 48h. Si la transaction on-chain n'est pas confirmée avant expiration, récupération manuelle nécessaire.

**Centralisation de l'interface** : Bien que self-hostable, l'interface officielle est hébergée sur GitHub Pages. Si GitHub censure le repo, l'accès via swapmarket.github.io sera bloqué (solution : self-hosting).

**Traces on-chain** : Les scripts HTLC sont potentiellement identifiables par analyse blockchain avancée.

## Bonnes pratiques

### Configuration sécurisée

**Téléchargez votre Rescue Key** : Avant vos premiers swaps, téléchargez votre clé de récupération depuis les paramètres (voir section dédiée ci-dessus). Cette clé unique fonctionne pour tous vos swaps futurs et permet de récupérer vos fonds en cas de problème.

**Utilisez Tor Browser** : Pour une confidentialité maximale, accédez à SwapMarket via Tor Browser afin de masquer votre adresse IP.

**Considérez le self-hosting** : Pour les utilisateurs techniques, exécuter sa propre instance SwapMarket élimine la dépendance au domaine GitHub Pages officiel.

### Optimisation des swaps

**Surveillez la mempool** : Consultez mempool.space avant un swap-in. Privilégiez les moments de faible activité pour minimiser les frais de minage.

**Vérifiez les adresses** : Pour les swap-out, vérifiez méticuleusement votre adresse de réception. Utilisez le copier-coller et vérifiez les 5 premiers et 5 derniers caractères.

**Testez avec petits montants** : Commencez avec le minimum autorisé (25 000 à 50 000 sats). Augmentez progressivement une fois le processus maîtrisé.

**Documentez vos swaps** : Notez l'ID de chaque swap, l'adresse de remboursement, et le délai d'expiration. Ces informations facilitent le suivi et la récupération en cas de problème technique.

### Stratégie d'usage

**Équilibrez vos liquidités** : Utilisez SwapMarket pour ajuster votre répartition entre on-chain (épargne, sécurité à long terme) et Lightning (dépenses quotidiennes, paiements instantanés) selon vos besoins réels.

**Calculez la rentabilité** : Pour des besoins permanents de liquidité Lightning, comparez le coût cumulé de swaps répétés versus l'ouverture directe d'un canal Lightning. SwapMarket excelle pour les ajustements ponctuels, pas nécessairement pour des flux réguliers importants.

## SwapMarket vs Boltz : Quelle différence ?

### Boltz : Technologie vs Service

**Boltz est la technologie open-source** (`boltz-backend` sur GitHub) qui implémente les swaps atomiques via HTLC entre Bitcoin, Lightning et Liquid.

**Point critique** : Tous les providers sur SwapMarket (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) déploient leur propre instance du backend Boltz. La technologie sous-jacente est donc identique. Une vulnérabilité dans le backend Boltz affecterait potentiellement tous les providers, mais le caractère open-source permet l'audit communautaire.

**Boltz Exchange** est un service unique opéré par l'équipe Boltz, tandis que **SwapMarket** agrège plusieurs providers utilisant tous la technologie Boltz, créant ainsi une compétition tarifaire.

N'hésitez pas à consulter nos tutoriels sur Boltz ou encore Zeus Swap pour plus de précisions : 

https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.network/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Différences clés

| Aspect        | Boltz Exchange           | SwapMarket                                 |
| ------------- | ------------------------ | ------------------------------------------ |
| Nature        | Service unique           | Agrégateur multi-providers                 |
| Providers     | Boltz uniquement         | Boltz, ZEUS, Eldamar, Middle Way           |
| Compétition   | Tarifs fixes             | Compétition libre                          |
| Interface     | boltz.exchange           | swapmarket.github.io (self-hostable)       |
| Sécurité      | Non-custodial (HTLC)     | Non-custodial (HTLC)                       |

**Avantages SwapMarket** : Compétition tarifaire, diversification des instances backend, comparaison en temps réel.

**Alternatives technologiques** (non compatibles SwapMarket) : Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Ces solutions utilisent leurs propres implémentations de submarine swaps.

**Recommandation** : Utilisez Boltz Exchange pour la simplicité ou SwapMarket pour optimiser les coûts via la compétition. Les deux sont équivalents en sécurité (HTLC non-custodial).

## Conclusion

SwapMarket facilite les échanges Bitcoin/Lightning en agrégeant plusieurs providers dans une interface unique. L'architecture HTLC garantit le caractère non-custodial des swaps, l'absence de KYC préserve la confidentialité, et le code open-source self-hostable renforce la résistance à la censure.

La compétition entre providers améliore les tarifs et multiplie les sources de liquidité. Pour optimiser sa gestion bicouche (épargne on-chain, dépenses Lightning), SwapMarket constitue un outil pratique préservant souveraineté financière et confidentialité.

## Ressources

### Documentation officielle
- [SwapMarket - Application web](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Documentation technique](https://docs.boltz.exchange/)
- [Guide self-hosting](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)

### Projets connexes
- [Boltz Exchange](https://boltz.exchange) - Service de swaps atomiques originel
- [ZEUS Swaps](https://zeusln.com) - Provider de swaps Lightning
