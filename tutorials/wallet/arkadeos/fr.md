---
name: ArkadeOS
description: Guide complet sur le portefeuille Arkade et le protocole Ark
---

![cover](assets/cover.webp)

Le réseau Bitcoin fait face à un défi majeur : sa scalabilité. Si la couche principale (layer 1) offre une sécurité et une décentralisation inégalées, elle ne peut traiter qu'un nombre limité de transactions par seconde. Le Lightning Network a émergé comme une solution de seconde couche (layer 2) prometteuse, permettant des paiements rapides et peu coûteux. Cependant, Lightning impose ses propres contraintes : la gestion de canaux, la nécessité de liquidité entrante et une complexité technique qui peut rebuter les nouveaux utilisateurs.

C'est dans ce contexte qu'apparaît **Ark**, un nouveau protocole de layer 2 conçu pour offrir une expérience utilisateur simplifiée sans sacrifier la souveraineté. **ArkadeOS** (ou Arkade) est la première implémentation majeure de ce protocole, proposant un portefeuille Bitcoin de nouvelle génération.

Ce tutoriel vous guidera à travers l'univers d'Arkade. Nous explorerons le fonctionnement du protocole Ark, comment installer et configurer le portefeuille Arkade, et comment l'utiliser pour envoyer et recevoir des bitcoins instantanément, de manière confidentielle et sans les frictions habituelles du Lightning Network.

## Comprendre le protocole Ark

Avant de plonger dans l'utilisation d'Arkade, il est essentiel de saisir les concepts clés du protocole Ark qui l'anime. Ark n'est pas une blockchain séparée, mais un mécanisme de coordination intelligent au-dessus de Bitcoin.

### Le concept de VTXO
Au cœur d'Ark se trouve le **VTXO** (Virtual UTXO). Un VTXO est un UTXO qui n'est pas encore publié sur la blockchain Bitcoin : il existe hors de la chaîne principale (off-chain) mais est garanti par des transactions pré-signées sur la blockchain.

Contrairement à un solde sur un échange centralisé, un VTXO vous appartient réellement. Vous détenez une preuve cryptographique qui vous permet, à tout moment, de réclamer les vrais bitcoins correspondants sur la blockchain, même si le serveur Ark disparaît. Les VTXOs permettent de transférer de la valeur instantanément entre utilisateurs sans attendre les confirmations de bloc.

### Le rôle de l'ASP (Ark Service Provider)
Le protocole Ark fonctionne sur un modèle client-serveur. Le serveur est appelé **ASP** (Ark Service Provider). L'ASP joue le rôle de chef d'orchestre :
*   Il fournit la liquidité nécessaire au réseau.
*   Il coordonne les transactions entre utilisateurs.
*   Il organise les "rounds" (tours) de règlement sur la blockchain.

Il est crucial de noter que l'ASP est **non-custodial** (non-dépositaire). Il ne détient jamais vos clés privées et ne peut pas voler vos fonds. Son rôle est purement technique et logistique. Si un ASP censure vos transactions ou tombe en panne, vous pouvez toujours récupérer vos fonds via une procédure de sortie unilatérale.

### Les Rounds et la confidentialité
Les transactions sur Ark sont finalisées par lots appelés **Rounds**. Périodiquement (par exemple toutes les quelques secondes), l'ASP rassemble toutes les transactions en attente et les ancre sur la blockchain Bitcoin en une seule transaction optimisée.
Ce mécanisme offre deux avantages majeurs :
- **Scalabilité** : Une seule transaction on-chain peut valider des milliers de paiements off-chain, réduisant drastiquement les frais pour les utilisateurs.
- **Confidentialité** : Chaque round agit comme un **CoinJoin**. Les fonds de tous les participants sont mélangés dans un pool commun avant d'être redistribués sous forme de nouveaux VTXOs. Cela brise le lien entre l'expéditeur et le destinataire, rendant le traçage des paiements extrêmement difficile, voire impossible pour un observateur externe.

## Présentation d'ArkadeOS

ArkadeOS est l'application concrète qui rend le protocole Ark utilisable pour le grand public. Développé par Ark Labs, c'est un écosystème complet comprenant un portefeuille (Wallet), un serveur (Operator) et des outils pour développeurs.

Pour l'utilisateur final, Arkade se présente sous la forme d'un portefeuille web (PWA - Progressive Web App) élégant et intuitif. Il masque la complexité cryptographique des VTXOs et des rounds derrière une interface familière. Avec Arkade, vous disposez d'une adresse pour recevoir, d'un bouton pour envoyer, et d'un historique de transactions, tout comme un wallet classique, mais avec la puissance de l'instantanéité et de la confidentialité d'Ark.

## Installation et Configuration

Arkade étant une Progressive Web App, son installation est particulièrement simple et ne passe pas nécessairement par les magasins d'applications traditionnels.

### Accès et Installation
Vous pouvez accéder à Arkade directement depuis n'importe quel navigateur web moderne (Chrome, Safari, Brave) sur ordinateur ou mobile.

- Rendez-vous sur le site officiel de l'application : **[arkade.money](https://arkade.money)**.

![arkade homepage](assets/fr/01.webp)

Vous serez accueilli par une série d'écrans d'introduction qui vous présenteront les concepts clés d'Arkade : un nouvel écosystème pour Bitcoin, l'importance du self-custody et les avantages des transactions par lots.

![arkade onboarding](assets/fr/02.webp)

- **Sur Android (Chrome/Brave)** : Appuyez sur le menu du navigateur (trois points) et sélectionnez "Installer l'application" ou "Ajouter à l'écran d'accueil".
- **Sur iOS (Safari)** : Appuyez sur le bouton de partage (carré avec une flèche vers le haut) et choisissez "Sur l'écran d'accueil".

Une fois installée, Arkade se lance comme une application native, en plein écran et sans barre d'adresse.

### Création du portefeuille
Au premier lancement, vous serez invité à configurer votre portefeuille.

- Cliquez sur **"Create New Wallet"** (Créer un nouveau portefeuille).

![create wallet](assets/fr/03.webp)

- Le portefeuille est créé instantanément. Contrairement aux wallets Bitcoin traditionnels, **Arkade n'utilise pas de phrase de récupération de 12 ou 24 mots**. À la place, Arkade génère automatiquement une **clé privée** au format Nostr (nsec) qui servira à sauvegarder et restaurer votre portefeuille. Pensez à sauvegarder cette clé immédiatement (voir la section suivante).

- Vous verrez l'écran "Your new wallet is live!" confirmant que votre portefeuille est prêt à être utilisé. Cliquez sur **"GO TO WALLET"** pour accéder à l'interface principale.

Une fois dans votre portefeuille, vous accédez à l'interface principale d'Arkade. Vous y trouverez votre solde, les boutons pour envoyer et recevoir des fonds, ainsi qu'un onglet "Apps" qui donne accès à des applications intégrées comme Boltz (échange Lightning), LendaSat et LendaSwap (services de prêt), ou encore Fuji Money (actifs synthétiques).

![wallet interface](assets/fr/04.webp)

### Connexion à l'ASP
Par défaut, le portefeuille est automatiquement configuré pour se connecter à l'ASP officiel d'Arkade Labs. Vous pouvez vérifier à quel serveur vous êtes connecté en allant dans **Settings** > **About** où vous verrez l'adresse du serveur (actuellement `https://arkade.computer`).

Dans la version actuelle d'Arkade (Beta), il n'est pas possible de modifier manuellement le serveur ASP. L'application se connecte automatiquement à l'ASP officiel d'Arkade Labs. À l'avenir, il est envisageable que les utilisateurs puissent choisir entre différents ASP selon leurs préférences, mais cette fonctionnalité n'est pas encore disponible.

### Sauvegarde de votre clé privée
**Cette étape est essentielle et doit être effectuée immédiatement après la création de votre portefeuille.** Arkade utilise une clé privée au format Nostr (nsec) comme méthode de sauvegarde et de récupération. Pour sauvegarder votre clé privée :

- Rendez-vous dans **Settings** (Paramètres) depuis l'écran principal.
- Sélectionnez **"Backup and privacy"** (Sauvegarde et confidentialité).
- Vous verrez votre **clé privée** affichée au format `nsec...`. Cette longue chaîne de caractères est votre unique moyen de restaurer votre portefeuille.
- Appuyez sur **"COPY NSEC TO CLIPBOARD"** pour copier votre clé privée.
- **Conservez cette clé en lieu sûr** : notez-la sur papier, stockez-la dans un gestionnaire de mots de passe sécurisé, ou utilisez toute autre méthode de sauvegarde qui vous convient.
- Arkade propose également l'option **"Enable Nostr backups"**. Cette fonctionnalité utilise le protocole Nostr (un réseau décentralisé) pour sauvegarder automatiquement certaines données de votre wallet de manière chiffrée sur des relais Nostr. Cela facilite la synchronisation entre plusieurs appareils et offre une récupération plus simple de l'état de votre wallet.

**Important** : Les backups Nostr sont une fonctionnalité de **confort** uniquement. Ils ne remplacent en aucun cas la sauvegarde de votre clé nsec. Les relais Nostr ne garantissent pas un stockage permanent des données. Votre clé privée nsec reste votre unique moyen garanti de récupérer vos fonds.

![backup private key](assets/fr/05.webp)


## Utilisation d'Arkade

Une fois votre portefeuille configuré, vous êtes prêt à explorer les capacités d'Arkade. L'interface est conçue pour unifier les différents types de paiements Bitcoin (On-chain, Lightning, Ark) de manière transparente.

### Recevoir des fonds

Pour alimenter votre portefeuille, appuyez sur **"Receive"**. Arkade propose trois méthodes de réception :

- **Paiement Ark** : Si l'expéditeur utilise également Arkade, partagez votre adresse Ark pour un transfert instantané, confidentiel et quasi-gratuit.
- **Dépôt On-chain (Boarding)** : Utilisez l'adresse Bitcoin (`bc1p...`) pour recevoir depuis un wallet classique ou un exchange. Comptez une confirmation (~10 min) avant que les fonds soient convertis en VTXOs.
- **Swap Lightning** : Générez une facture Lightning et payez-la depuis un wallet Lightning externe. Les fonds arrivent instantanément via un swap automatique.

![receive amount](assets/fr/06.webp)

L'écran de réception affiche toutes les options disponibles : QR code, adresse Ark, adresse Bitcoin (BIP21) et facture Lightning. Pour les paiements Lightning, gardez l'application ouverte pendant la transaction.

![receive confirmation](assets/fr/07.webp)

### Envoyer des fonds

Pour envoyer des fonds, appuyez sur **"Send"** et collez l'adresse ou scannez le QR code du destinataire. Arkade détecte automatiquement le type de paiement requis :

- **Paiement Ark** : Vers une adresse Ark, le transfert est instantané, privé et quasi-gratuit (0 SATS de frais). Le destinataire n'a pas besoin d'être en ligne.
- **Paiement Lightning** : Scannez une facture Lightning (`lnbc...`) et Arkade effectue automatiquement un swap. L'ASP paie la facture pour vous et débite votre solde Ark.
- **Paiement On-chain** : Vers une adresse Bitcoin classique (`bc1q...` ou `bc1p...`), Arkade initie une "Sortie collaborative" qui sera incluse dans le prochain round on-chain.

Vérifiez les détails sur l'écran "Sign transaction", puis validez avec **"TAP TO SIGN"**.

![send payment](assets/fr/08.webp)

**Limitation actuelle (Beta)** : Les VTXOs créés il y a moins de 24 heures ne peuvent pas être utilisés pour les sorties on-chain. Si vous rencontrez une erreur, attendez que vos VTXOs soient "matures".

**Confidentialité des sorties on-chain** : L'exemple ci-dessous montre une [transaction de sortie Ark sur mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). On observe une entrée distribuée vers 4 sorties différentes, comme un CoinJoin. Pour un observateur externe, il est impossible de déterminer quel montant appartient à quel utilisateur.

![transaction ark mempool](assets/fr/11.webp)

## Fonctionnalités Avancées

### Gestion de l'expiration des VTXOs
Une particularité technique du protocole Ark est que les VTXOs ont une **durée de vie limitée**. Cette contrainte temporelle est inhérente à la conception du protocole. La durée d'expiration est configurable par chaque serveur ASP ; sur l'ASP officiel d'Arkade Labs, cette période est d'environ **4 semaines (≈30 jours)**.

**Pourquoi cette expiration ?** Cette limitation permet au serveur Ark de gérer efficacement la liquidité et de nettoyer les VTXOs des utilisateurs inactifs. Après l'expiration, le serveur Ark peut techniquement réclamer les fonds restants dans l'arbre de VTXOs.

**Comment fonctionne le rafraîchissement ?** Pour maintenir vos VTXOs actifs, ils doivent être "rafraîchis" avant leur expiration. Le rafraîchissement consiste à participer à un nouveau "round" où vos VTXOs proches de l'expiration sont échangés contre de nouveaux VTXOs avec une nouvelle période de validité complète (≈30 jours sur l'ASP d'Arkade Labs).

Le portefeuille Arkade gère ce processus automatiquement : l'application surveille en permanence l'état de vos VTXOs et les rafraîchit automatiquement quelques jours avant leur expiration. Tant que vous ouvrez votre application régulièrement (au moins une fois par semaine), vos VTXOs seront automatiquement maintenus actifs.

**Que se passe-t-il en cas d'expiration ?** Si vous n'ouvrez pas votre portefeuille pendant plus de 4 semaines, vos VTXOs expireront. Cependant, vous ne perdez pas vos fonds : vous conservez la possibilité de les récupérer via une **sortie unilatérale** (voir section suivante). Cette procédure est plus coûteuse en frais et plus lente, mais elle garantit que vos fonds restent récupérables.

La nécessité d'ouvrir régulièrement l'application fait d'Arkade un **"Hot Wallet"** conçu pour les dépenses courantes, et non un coffre-fort pour l'épargne à long terme. Pour stocker des bitcoins sans les utiliser pendant de longues périodes, privilégiez un cold wallet hardware.

**Vérifier l'état de vos VTXOs** : Vous pouvez surveiller l'état de vos VTXOs dans **Settings** > **Advanced**. Consultez "Next Renewal" pour voir quand aura lieu le prochain renouvellement automatique, et "Virtual Coins" pour voir la liste détaillée de tous vos VTXOs avec leur date d'expiration.

![vtxo management](assets/fr/09.webp)

### Sortie Unilatérale (Unilateral Exit)

La sortie unilatérale est une **garantie cryptographique fondamentale** du protocole Ark qui vous assure la récupération de vos fonds, même si l'ASP disparaît, censure vos transactions ou refuse de coopérer. Techniquement, vos VTXOs sont des **transactions Bitcoin pré-signées** que vous possédez. En cas d'urgence absolue, vous pouvez diffuser ces transactions sur la blockchain Bitcoin pour récupérer vos fonds sans l'autorisation de personne.

**Comment ça fonctionne ?** Le processus se déroule en deux étapes. D'abord l'**Unrolling** (déroulement) : vous diffusez séquentiellement les transactions pré-signées qui composent vos VTXOs dans l'arbre de transactions. Ensuite la **Finalisation** : une fois les timelocks expirés (généralement 24 heures), vous récupérez vos bitcoins sur une adresse classique.

**État actuel dans Arkade** : Dans la version Beta, il n'existe pas encore de bouton ou d'interface utilisateur simple pour effectuer une sortie unilatérale. Cette fonctionnalité nécessite actuellement l'utilisation du SDK Arkade et des connaissances techniques en programmation TypeScript.

**Pourquoi c'est malgré tout important ?** Même si la procédure n'est pas accessible via un simple bouton, la garantie cryptographique existe. Vos VTXOs contiennent les transactions pré-signées qui vous appartiennent légitimement. C'est cette garantie technique qui fait d'Ark un protocole **non-custodial** : même dans le pire des scénarios, vos fonds restent techniquement récupérables. Une interface simplifiée sera probablement ajoutée dans les futures versions d'Arkade.

## Avantages et Limitations

Pour bien situer Arkade, résumons ses forces et ses faiblesses actuelles.

### Points Forts
*   **Expérience Utilisateur (UX)** : Pas de gestion de canaux, de capacité entrante ou de backups complexes de canaux comme sur Lightning. On installe et on utilise.
*   **Confidentialité** : L'architecture CoinJoin par défaut offre un niveau d'anonymat bien supérieur aux transactions on-chain ou Lightning standard.
*   **Interopérabilité** : Payez n'importe quel QR code Bitcoin (On-chain ou Lightning) depuis une seule interface.

### Contraintes
*   **Jeunesse du protocole** : Ark est une technologie très récente. Des bugs peuvent exister. Il est prudent de ne pas y stocker des sommes dont la perte serait critique.
*   **Dépendance à l'ASP** : Bien que non-custodial, le système repose sur la disponibilité de l'ASP pour la fluidité. Si l'ASP est hors ligne, vous ne pouvez plus transacter instantanément (seulement sortir vos fonds on-chain).
*   **Hot Wallet uniquement** : La nécessité d'ouvrir l'application régulièrement pour rafraîchir les VTXOs ne convient pas au stockage froid (Cold Storage).

## Comparaison : Arkade vs Lightning vs Cashu

Pour mieux comprendre le positionnement d'Arkade, comparons-le aux deux autres solutions majeures de scalabilité.

| Critère | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modèle** | UTXO partagé coordonné par serveur (ASP) | Réseau P2P de canaux de paiement | Jetons aveugles émis par une banque (Mint) |
| **Custodie** | **Non-custodial** (vous avez les clés) | **Non-custodial** (vous avez les clés) | **Custodial** (le Mint a les fonds) |
| **Confidentialité** | **Élevée** (CoinJoin natif, aveugle pour le public) | **Moyenne** (Routage en oignon, mais canaux visibles) | **Très Élevée** (Aveugle même pour le Mint) |
| **Scalabilité** | Excellente (Batching massif on-chain) | Excellente (Transactions infinies off-chain) | Excellente (Simples signatures serveur) |
| **Expérience** | Simple (proche d'un wallet on-chain) | Complexe (gestion de canaux, liquidité) | Très simple (comme du cash numérique) |
| **Risque principal** | Disponibilité de l'ASP & Expiration | Gestion des canaux & Backups | Confiance dans le Mint (risque de vol) |

**Arkade** se positionne comme le compromis idéal : la simplicité et la confidentialité de Cashu, mais avec la souveraineté (non-custodial) de Lightning.

## Support et Assistance

Si vous rencontrez des problèmes ou avez des questions lors de votre utilisation d'Arkade, l'application propose plusieurs options d'assistance :

- Accédez à **Settings** > **Support**.
- Vous trouverez plusieurs options :
  - **Customer support** : Obtenez de l'aide pour votre portefeuille, signalez des bugs ou posez des questions.
  - **Secure Chat** : Vos conversations sont sécurisées et privées, l'historique étant maintenu entre les sessions.
  - **Bug Reports** : Signalez tout problème rencontré en incluant les étapes pour le reproduire.
  - **Track Progress** : Suivez vos tickets de support et conversations à tout moment.

![support](assets/fr/10.webp)

L'équipe d'Arkade est également active sur Telegram via le canal @arkade_os pour le support et les opportunités d'intégration.

## Note importante : Application en Beta

**⚠️ Arkade est actuellement en version Beta publique sur le mainnet Bitcoin**. Bien que l'application soit fonctionnelle avec de vrais bitcoins, il est important de prendre certaines précautions.

### Recommandations d'utilisation
- **Utilisez de petits montants** : Évitez de stocker des sommes importantes sur Arkade. Privilégiez ce portefeuille pour vos dépenses courantes et gardez vos économies sur un cold wallet hardware.
- **Bugs et limitations possibles** : Comme toute application en développement actif, Arkade peut présenter des bugs ou des comportements inattendus. Signalez tout problème via le support intégré.
- **Évolution rapide** : L'application et le protocole sont en constante amélioration. Certaines fonctionnalités peuvent changer ou être ajoutées dans les prochaines versions.

### Limitations actuelles connues
- **Délai de 24h sur les VTXOs** : Les VTXOs récemment créés ne peuvent pas être utilisés immédiatement pour les sorties on-chain.
- **ASP unique** : Il n'est pas encore possible de changer de serveur ASP dans l'application.
- **Sortie unilatérale technique** : Pas encore d'interface simplifiée pour la sortie unilatérale (nécessite le SDK).

L'équipe d'Arkade Labs travaille activement à assouplir ces limitations dans les futures versions.

## Conclusion

ArkadeOS représente une avancée majeure dans l'écosystème Bitcoin. En implémentant le protocole Ark, il prouve qu'il est possible de concilier la simplicité d'utilisation avec les principes fondamentaux de Bitcoin : ne pas faire confiance, vérifier.

Bien qu'encore jeune, Arkade offre un aperçu fascinant de ce que pourrait être l'avenir des paiements Bitcoin : instantanés, privés et accessibles à tous sans prérequis technique. C'est un outil parfait pour vos dépenses quotidiennes, complémentaire à votre solution d'épargne sécurisée (Cold Wallet).

Nous vous encourageons à tester Arkade avec de petits montants pour découvrir ce nouveau protocole par vous-même. L'écosystème évolue vite, et Arkade est aux avant-postes de cette innovation.

## Ressources

Pour aller plus loin, consultez les ressources officielles :

*   **Site Web Arkade** : [arkadeos.com](https://arkadeos.com)
*   **Documentation** : [docs.arkadeos.com](https://docs.arkadeos.com)
*   **Protocole Ark** : [ark-protocol.org](https://ark-protocol.org)
*   **Code Source** : [GitHub Arkade](https://github.com/arkade-os)
