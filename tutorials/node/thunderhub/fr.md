---
name: ThunderHub
description: Interface web de gestion d'un nœud Lightning LND
---
![cover](assets/cover.webp)

## Introduction

ThunderHub est un **gestionnaire open-source pour nœuds Lightning (LND)**, offrant une interface intuitive accessible depuis tout appareil ou navigateur.

**Fonctionnalités principales :**
- **Surveillance** : Vue globale des soldes, canaux, transactions, statistiques de routage
- **Gestion** : Ouverture/fermeture de canaux, paiements entrants/sortants, équilibrage des canaux
- **Intégrations** : Support LNURL, swaps via Boltz, sauvegarde Amboss
- **Interface responsive** : Compatible mobile, tablette et desktop avec thèmes sombre/clair

ThunderHub s'intègre facilement à **Umbrel**, **Voltage**, **RaspiBlitz** et **MyNode**, simplifiant ainsi la gestion quotidienne de votre nœud.

**Cas d'usage :** ThunderHub convient particulièrement aux opérateurs recherchant une interface ergonomique pour gérer leurs canaux, piloter la liquidité (rebalancing), surveiller les transactions et intégrer des services tiers comme Amboss. La sécurité est assurée via une connexion locale ou Tor.

Si vous n'avez pas encore de nœud Lightning, nous vous recommandons de suivre notre tutoriel Umbrel LND :

https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installation

ThunderHub peut s'installer de différentes manières selon votre environnement d'hébergement du nœud Lightning. Que vous utilisiez une solution clef en main (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, etc.) ou une installation manuelle, ThunderHub est souvent disponible sans effort majeur. Nous décrivons ci-dessous deux approches courantes : via l'App Store d'Umbrel, et via une installation manuelle (applicable à un serveur ou à une distribution auto-hébergée).

### Installation via Umbrel

Umbrel intègre ThunderHub dans son **App Store**, ce qui rend son installation extrêmement simple. Aucun besoin de ligne de commande ou de configuration manuelle : tout se fait via l'interface Umbrel. Suivez ces étapes :

- **Ouvrir le dashboard Umbrel** : Connectez-vous à l'interface web de votre nœud Umbrel (par exemple `http://umbrel.local` sur votre réseau local, ou via son adresse `.onion` si vous utilisez Tor).
- **Accéder à l'App Store** : Dans le menu principal d'Umbrel, cliquez sur « App Store » (ou « App »). Recherchez **ThunderHub** dans la liste des applications disponibles.

![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)

- **Installer ThunderHub** : Cliquez sur l'application ThunderHub puis sur le bouton d'installation. Confirmez si nécessaire. Umbrel va télécharger et déployer automatiquement ThunderHub sur votre nœud.

- **Lancer l'application** : Une fois l'installation terminée (quelques dizaines de secondes), ThunderHub apparaît sur votre page d'accueil. Cliquez sur son icône pour l'ouvrir. ThunderHub se lance alors dans votre navigateur.

![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)

**Important :** Lors de la première ouverture, ThunderHub affiche automatiquement le **mot de passe par défaut** nécessaire pour la connexion. Une option "Don't show this again" vous permet de masquer cet affichage pour les prochaines connexions. **Il est fortement conseillé de :**
- **Sauvegarder immédiatement** ce mot de passe dans votre gestionnaire de mots de passe
- **Le copier** pour l'utiliser dans l'étape suivante
- Cocher "Don't show this again" une fois le mot de passe sauvegardé

![Page de connexion de ThunderHub](assets/fr/03.webp)

Vous arrivez ensuite sur la page de connexion où vous devez saisir ce mot de passe que vous avez copié à l'étape précédente pour déverrouiller l'interface.

![Interface de connexion complète à ThunderHub](assets/fr/04.webp)

Umbrel se charge en arrière-plan de fournir à ThunderHub les informations de connexion à LND (certificat TLS, macaroon d'administration, etc.), vous n'avez donc aucune configuration supplémentaire à faire. En quelques clics, vous disposez ainsi de ThunderHub fonctionnel sur votre nœud Umbrel.

### Installation manuelle (autohébergement hors Umbrel)

Pour les utilisateurs hors Umbrel (par exemple sur un serveur personnel, un Raspberry Pi avec RaspiBlitz ou une installation *stand-alone*), l'installation de ThunderHub nécessite quelques étapes supplémentaires. Nous décrivons ci-dessous l'installation depuis la source et la configuration, selon la [documentation officielle de ThunderHub](https://docs.thunderhub.io).

#### Installation

**Prérequis :** Assurez-vous que votre système répond aux exigences minimales selon la [documentation setup](https://docs.thunderhub.io/setup) :
- **Node.js** version 18 ou supérieure
- **npm** installé
- Accès aux fichiers d'authentification de LND :
  * Le certificat TLS de LND (`tls.cert`)
  * Le macaroon d'administration de LND (`admin.macaroon`)
  * L'adresse (hostname:port) du service gRPC de LND (par défaut `127.0.0.1:10009` en local)

**1. Récupérer le code ThunderHub :** Clonez le dépôt GitHub du projet comme indiqué dans la [documentation installation](https://docs.thunderhub.io/installation) :

```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```

**2. Installer les dépendances et construire l'application :**

```bash
npm install
npm run build
```

Ces commandes installent tous les modules requis puis compilent l'application (ThunderHub est écrit en TypeScript/React).

**3. Mise à jour ultérieure :** Pour les mises à jour futures, ThunderHub propose plusieurs méthodes :

```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```

#### Configuration (Setup)

**1. Fichier de configuration principal :** Créez un fichier `.env.local` à la racine du dossier ThunderHub pour personnaliser la configuration (cela évitera que vos réglages soient écrasés lors de mises à jour). Variables principales selon la [documentation setup](https://docs.thunderhub.io/setup) :

```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```

**2. Configuration des comptes (Server Accounts) :** Créez le fichier YAML spécifié dans `ACCOUNT_CONFIG_PATH` :

```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
  - name: 'Mon Nœud LND'
    serverUrl: '127.0.0.1:10009'
    macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
    certificatePath: '/home/user/.lnd/tls.cert'
    password: 'mot_de_passe_compte_specifique'
  # Optionnel : compte avec macaroon en hexadécimal
  - name: 'Nœud Distant'
    serverUrl: 'ip.distante:10009'
    macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
    certificate: '0202045c7365...' # Certificat en HEX ou Base64
```

**3. Accès distant (Remote Access) :** Pour se connecter à un nœud LND distant, ajoutez dans `lnd.conf` :

```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```

**4. Sécurité :** Au premier démarrage, ThunderHub **hache automatiquement** le `masterPassword` et tous les mots de passe des comptes dans le fichier YAML pour éviter d'avoir des mots de passe en clair sur le serveur.

**5. Démarrer ThunderHub :**

```bash
npm start
```

Par défaut, le serveur écoute sur le port 3000. Accédez à `http://localhost:3000` (ou `http://ip-serveur:3000` depuis le réseau local).

**6. Alternative Docker :** ThunderHub fournit des images Docker officielles :

```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```

La page de connexion ThunderHub apparaît. Sélectionnez le compte configuré et entrez le mot de passe défini pour accéder au tableau de bord.

**Installation sur autres distributions :** Les distributions de nœuds pré-packagées (RaspiBlitz, MyNode, Start9, etc.) proposent généralement une prise en charge native de ThunderHub via leurs interfaces d'administration respectives.

**Pour aller plus loin :** Consultez la documentation officielle complète :
- **Installation :** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Configuration :** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)

Ces ressources détaillent les options avancées comme les comptes SSO, les macaroons chiffrés, la configuration TOR, et bien plus encore.

Une fois ThunderHub installé et accessible, vous êtes prêt à exploiter toutes ses fonctionnalités. Dans la section suivante, nous allons passer en revue l'interface ThunderHub et ses différents onglets, afin de vous guider dans son utilisation.

## Présentation de l'interface

L'interface ThunderHub se structure autour d'un menu principal (généralement affiché en colonne latérale gauche) comprenant plusieurs sections clés. Chacune correspond à un aspect de la gestion de votre nœud Lightning. Nous allons les parcourir un à un :

* **Home** – Onglet d'accueil avec le tableau de bord général (vue d'ensemble de votre nœud et actions rapides).
* **Dashboard** – Tableau de bord personnalisable avec widgets et métriques avancées.
* **Peers** – Gestion des pairs Lightning (connexions aux autres nœuds).
* **Channels** – Gestion détaillée des canaux Lightning.
* **Rebalance** – Outil d'équilibrage des canaux (circular payments).
* **Transactions** – Historique des paiements Lightning (transactions LN).
* **Forwards** – Statistiques de routage (paiements relayés par votre nœud).
* **Chain** – Portefeuille on-chain du nœud (BTC on-chain : UTXOs, transactions).
* **Amboss** – Intégration avec Amboss (monitoring du nœud, backups, etc.).
* **Tools** – Outils divers (sauvegardes, messages signés, macaroons, rapports…).
* **Swap** – Fonctions de swap on-chain/Lightning via Boltz.
* **Stats** – Statistiques avancées et métriques de performance du nœud.

*(Note : Suivant la version de ThunderHub, certaines sections peuvent avoir des intitulés légèrement différents ou des fonctionnalités supplémentaires, mais les principes généraux restent les mêmes.)*

### Home (Tableau de bord général)

L'onglet **Home** de ThunderHub est la page d'accueil qui s'affiche après votre connexion. Il contient le **tableau de bord général** qui offre un **aperçu global** de l'état de votre nœud Lightning et propose des **actions rapides** pour les opérations courantes. Voici ce que vous y trouverez généralement :

![Tableau de bord principal de ThunderHub](assets/fr/05.webp)

* **Soldes et capacités :** En haut de la page, ThunderHub affiche vos soldes disponibles. Vous y verrez typiquement le solde on-chain (Bitcoin on-chain dans le wallet du nœud, symbolisé par une ancre ⚓) et le solde Lightning (capacités de vos canaux, symbolisé par un éclair ⚡). Cela vous donne une idée immédiate des fonds que vous avez en on-chain et en Lightning. Si vous avez plusieurs comptes ou réseaux, assurez-vous d'être sur le bon (par ex. mainnet vs testnet).

* **Statistiques clés :** Le tableau de bord peut présenter quelques métriques globales de votre nœud – par exemple le nombre de canaux ouverts, le nombre de pairs connectés, les frais de routage gagnés (si applicables), etc. C'est un résumé de l'activité récente et de la santé du nœud.

* **Quick Actions (actions rapides) :** Sur le dashboard figurent des boutons pour exécuter rapidement les tâches les plus communes, sans avoir à naviguer dans les menus. Parmi ces actions rapides on trouve notamment :

  * **Ghost** : Configuration d'une adresse Lightning personnalisée via Amboss.
  * **Donate** : Faire un don via Lightning.
  * **Login/Go To** : Permet de se connecter à votre compte Amboss (Quick Connect) et d'accéder directement à Amboss.space pour consulter les informations de votre nœud.
  * **Address** : Saisir une adresse Lightning pour effectuer un paiement.
  * **Open** : Ouvrir un nouveau canal Lightning. En cliquant, un formulaire s'ouvre pour saisir l'URI du nœud distant vers lequel ouvrir le canal, le montant et éventuellement les frais on-chain maximum à utiliser.
  * **Decode** : Décoder une facture Lightning ou un LNURL pour voir les détails avant paiement.
  * **LNURL** : Traiter des LNURL pour paiements ou retraits Lightning.
  * **LnMarkets Login** : Connexion à LnMarkets pour le trading.

Ces actions rapides permettent d'effectuer les opérations les plus fréquentes directement depuis la page d'accueil, sans avoir à naviguer dans les différents onglets de l'interface.

En résumé, le tableau de bord ThunderHub vous donne un **coup d'œil rapide** sur votre nœud et vous permet d'effectuer en un clic les opérations les plus fréquentes (envoyer/recevoir, ouvrir un canal). C'est le point de départ idéal pour l'administration quotidienne.

### Dashboard

La section **Dashboard** est distincte de l'onglet Home et offre un tableau de bord plus avancé et personnalisable. Cette section vous permet de créer une vue personnalisée avec des widgets spécifiques selon vos besoins d'opérateur de nœud.

* **Widgets personnalisables :** Contrairement à la page Home qui a une mise en page fixe, le Dashboard vous permet de choisir exactement quels éléments afficher et comment les organiser.

![Dashboard sans widgets activés](assets/fr/06.webp)

Si aucun widget n'est activé, vous verrez un message "No Widgets Enabled!" avec un bouton "Settings" pour accéder aux paramètres de personnalisation.

![Paramètres des widgets du Dashboard](assets/fr/07.webp)

Dans les paramètres, vous pouvez choisir parmi de nombreux widgets organisés en catégories : "Lightning - Info", "Lightning - Table", "Lightning - Graph", etc. Chaque widget peut être activé ou désactivé individuellement avec les boutons "Show/Hide".

![Bas de la page des paramètres](assets/fr/08.webp)

En bas des paramètres, vous trouverez les boutons "To Dashboard" pour revenir au tableau de bord et "Reset Widgets" pour réinitialiser l'affichage par défaut.

![Dashboard personnalisé avec widgets](assets/fr/09.webp)

Une fois configuré, votre dashboard peut afficher divers graphiques et métriques : graphiques des paiements Lightning, nombre de factures émises, statistiques de forwards, soldes détaillés, etc.

* **Métriques avancées :** Accédez à des statistiques plus détaillées sur les performances de votre nœud, avec des graphiques et des données en temps réel.

* **Vue d'ensemble configurable :** Adaptez l'affichage selon que vous soyez un utilisateur occasionnel ou un opérateur professionnel gérant plusieurs canaux de routage.

* **Interface modulaire :** Ajoutez ou supprimez des widgets selon vos besoins : graphiques de forwards, métriques de liquidité, alertes de santé du nœud, etc.

Cette section est particulièrement utile pour les utilisateurs avancés qui souhaitent surveiller des métriques spécifiques ou avoir un aperçu plus technique de leur nœud Lightning. Elle complète la section Home en offrant plus de flexibilité et de contrôle sur l'affichage des informations.

### Peers

La section **Peers** (pairs) liste tous les nœuds Lightning actuellement connectés au vôtre en tant que pairs. Un **peer** est une connexion directe de nœud à nœud sur le réseau Lightning. Votre nœud peut être connecté à des pairs même sans canal ouvert (par ex., juste pour échanger des informations de gossip sur le réseau), ou bien bien sûr chaque canal ouvert implique automatiquement un peer connecté.

![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)

Dans l'onglet Peers, vous verrez :

* **Colonnes d'information :** L'interface affiche des détails utiles comme le statut de synchronisation, le type de connexion (clearnet ou Tor), le ping, les satoshis reçus/envoyés et le volume de données échangées.
* **Ajouter un peer :** ThunderHub offre la possibilité de se connecter manuellement à un nouveau peer via le bouton **"Add"** en haut à droite. Vous devrez saisir l'URI du node (format `<public_key>@<socket>`). Une fois validé, ThunderHub envoie la commande `lncli connect` correspondante. Si le nœud est en ligne et accessible, il sera ajouté à votre liste de peers.

### Channels

L'onglet **Channels** est le cœur de la gestion des canaux Lightning. C'est probablement la section que vous consulterez le plus fréquemment. Elle présente **tous vos canaux Lightning** avec leurs détails, et permet de réaliser les actions de gestion sur ces canaux.

![Vue d'ensemble des channels ouverts](assets/fr/11.webp)

Voici ce que vous trouverez dans la page Channels :

* **Vue liste de canaux :** Chaque canal ouvert (ou en cours d'ouverture/fermeture) est listé, généralement avec l'alias du nœud distant, la capacité totale du canal, et une barre colorée illustrant la répartition de la liquidité local vs distante. ThunderHub utilise un code couleur (souvent bleu/vert) ou un pourcentage pour indiquer l'équilibre du canal : par exemple, du bleu pour votre part locale, du vert pour la part distante. Si un canal est parfaitement équilibré (50/50), la barre sera à moitié de chaque couleur. Cela permet d'identifier d'un coup d'œil quels canaux sont déséquilibrés (tout bleu = quasi tout en local, tout vert = quasi tout en distant).

* **Colonnes d'information :** L'interface affiche des colonnes détaillées incluant le Status (état du canal), les Actions disponibles, les Info du pair, le Channel ID, la Capacity, l'Activity, les Fees et la Balance avec visualisation graphique de la liquidité.

* **Configuration d'affichage :** Une roue dentée en haut à droite permet de personnaliser l'affichage des canaux selon vos préférences.

* **Statut :** Vous verrez aussi des indicateurs de statut – par ex. `Active` (le canal est ouvert et opérationnel), `Offline` (le peer est déconnecté, donc le canal est momentanément inutilisable), `Pending` (pour les ouvertures ou fermetures en attente de confirmation on-chain).

* **Actions sur un canal :** Pour chaque canal, ThunderHub fournit des boutons d'action (souvent sous forme d'icônes) :

![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)

  * **Modifier les frais (*Edit fees*) :** L'interface "Update Channel Policy" permet de régler tous les paramètres du canal : Base Fee, Fee Rate (en ppm), CLTV Delta, Max HTLC et Min HTLC. Vous pouvez ainsi ajuster vos politiques de frais individuellement par canal, dans le but d'attirer (ou décourager) du trafic de routage. *(Note : ThunderHub ne remplace pas un outil de gestion automatique de frais, mais pour du réglage manuel c'est très efficace.)*
  * **Fermer le canal (*Close*)** : L'interface "Close Channel" vous donne le choix entre une **fermeture coopérative** (par défaut) ou une **fermeture forcée** (*Force Close*) en définissant les frais (en sats/vByte). **Important :** privilégiez toujours la fermeture coopérative lorsque c'est possible, afin d'éviter des délais de règlement on-chain et des frais plus élevés. ThunderHub vous indiquera si le peer est en ligne (coopérative possible) ou non. En cas de force close, confirmez bien car c'est irréversible et cela déclenchera une transaction de sweeping avec un timelock (généralement 144 blocs soit ~1 jour sur Bitcoin mainnet).
  * **Ouvrir un nouveau canal :** Pour ouvrir un nouveau canal, cliquez sur la roue dentée en haut à droite de la page Channels, puis sélectionnez "Open". Vous pourrez alors initier un canal vers un nouveau peer ou un peer existant. L'avantage de passer par cette page est que vous avez sous les yeux la liste de vos canaux existants, ce qui peut aider à décider vers qui ouvrir un nouveau canal.

En bref, la section Channels vous donne une **maîtrise fine de chaque canal**. C'est ici que vous piloterez l'allocation de liquidité, que vous déciderez de quels canaux garder ou fermer, et que vous réglerez vos paramètres de routage par canal. ThunderHub offre une interface claire pour ces opérations cruciales de gestion de nœud.

### Rebalance

L'onglet **Rebalance** est dédié à l'**équilibrage des canaux**. L'équilibrage (ou *rebalance*) consiste à réajuster la répartition des fonds entre vos canaux sortants et entrants, en effectuant un **paiement circulaire** (circular payment) depuis un de vos canaux vers un autre de vos canaux, en passant par le réseau Lightning. Cela vous permet, sans apporter de nouveaux fonds, de déplacer de la liquidité d'un canal trop plein vers un canal trop vide, rendant ainsi vos canaux plus utiles (un canal équilibré peut à la fois envoyer et recevoir des paiements).

![Interface de rebalance des canaux](assets/fr/13.webp)

ThunderHub facilite grandement cette opération, qui serait fastidieuse en ligne de commande. Voici comment utiliser la section Rebalance :

* **Vue initiale des canaux :** En arrivant dans Rebalance, ThunderHub affiche la liste de vos canaux avec un indicateur de balance pour chacun (similaire à celui de la page Channels). Vous voyez d'emblée quels canaux sont déséquilibrés. ThunderHub peut classer les canaux par ordre de balance croissante, ce qui fait ressortir en haut de liste les canaux qui sont les plus déséquilibrés (0.0 signifiant entièrement côté local ou côté distant).

* **Sélection des pairs :** L'interface permet de sélectionner facilement les pairs sortants et entrants pour le rééquilibrage.

* **Configuration des paramètres :** Vous pouvez définir :
  - Les **frais maximum** (en sats et ppm) que vous êtes prêt à payer
  - Le **montant à rééquilibrer** avec option "Fixed" ou "Target"
  - Les **nœuds à éviter** lors du routage
  - Un **temps maximum d'essai** pour la recherche de route

* **Choisir le canal **source**** : Sélectionnez d'abord le **canal sortant (source)**, c'est-à-dire le canal depuis lequel vous avez trop de liquidité locale que vous souhaitez déplacer. En pratique, il s'agit d'un canal où votre part locale est importante (taux > 50%). Imaginons un canal A avec 1 000 000 sats dont 900 000 sats de local – c'est un bon candidat pour envoyer des sats ailleurs. En cliquant sur ce canal A comme "outgoing", ThunderHub le marque comme source.

* **Choisir le canal **cible**** : Ensuite, choisissez le **canal entrant (cible)** qui a besoin de recevoir de la liquidité. Typiquement, ce sera un canal où c'est l'inverse – la plupart des fonds sont côté distant (par exemple seulement 100 000 sats locaux sur 1 000 000). ThunderHub, une fois le canal source sélectionné, va trier les autres canaux dans l'ordre inverse (balance décroissante) pour aider à repérer les canaux les plus complémentaires. Sélectionnez un canal B qui a de la place côté local. ThunderHub affiche alors clairement quels sont les deux canaux choisis (source A et cible B).

* **Définir le montant et la tolérance de frais :** Un formulaire vous permet d'entrer :

  * Le **montant** à rééquilibrer (en sats). Souvent, on choisit un montant égal à ce qui permettrait d'équilibrer à \~50/50 les deux canaux. ThunderHub peut pré-remplir la moitié de la capacité excédentaire du canal source par exemple.
  * Le **frais maximum** que vous êtes prêt à payer pour cette opération (facultatif). Ce frais est exprimé en sats (frais totaux du routage circulaire). Si vous laissez vide, ThunderHub cherchera un chemin quel qu'en soit le coût, ce qui n'est généralement pas conseillé (il vaut mieux fixer une limite, ex: 10 sats pour un petit rebalance, ou un ppm maximal).

* **Rechercher un chemin (*Get Route*) :** Cliquez sur le bouton pour trouver une route. ThunderHub interroge LND pour calculer une route depuis votre canal source vers votre propre canal cible en passant par le réseau. S'il trouve un chemin possible respectant vos critères de frais, il l'affiche avec le détail des hops et le coût en frais. Par exemple, il peut indiquer qu'il a trouvé un chemin en 3 sauts avec un total de 2 sats de frais.

* **Lancer le rebalance :** Si la route proposée vous convient, cliquez sur **Balance Channel** (équilibrer). ThunderHub va alors initier le paiement circulaire via LND. Si le paiement aboutit, vous verrez une notification de succès et les canaux A et B verront leur balance modifiée en temps réel. ThunderHub mettra à jour l'indicateur de balance de ces canaux (idéalement ils seront plus verts qu'avant, signe d'un meilleur équilibre).

* **Ajustements et itérations :** Si aucune route n'est trouvée du premier coup (ou si elle est trop coûteuse), vous pouvez ajuster les paramètres :

  * Essayer un montant plus faible (parfois un rebalance partiel passe alors qu'un gros montant échoue).
  * Augmenter le frais max graduellement, mais en faisant attention à ne pas payer plus en fees que ce que ça vaut.
  * Utiliser le bouton **Get Another Route** si disponible, pour tenter une alternative.
  * Essayer une autre paire de canaux si vraiment ça coince.

ThunderHub rend le processus très **intuitif et visuel**. En 4 étapes (sélection du canal sortant, sélection du canal entrant, montant, valider), vous réalisez ce qui demandait autrefois des commandes manuelles complexes. L'outil est précieux pour maintenir un nœud bien équilibré, ce qui améliore vos performances de routage et votre expérience (plus de facilité à envoyer et recevoir des paiements sur l'ensemble de vos canaux).

Enfin, notez qu'un rebalance consomme des frais de routage (payés aux nœuds intermédiaires), il s'agit donc d'un **investissement** pour fluidifier votre node. Utilisez-le judicieusement, par exemple pour soutenir un canal vers un service que vous utilisez souvent (inbound liquidity) ou pour équilibrer un gros canal de routing. ThunderHub vous permet de le faire **simplement et efficacement**.

### Transactions

La section **Transactions** dans ThunderHub correspond à l'historique des transactions **Lightning** de votre nœud, c'est-à-dire les paiements et factures réglés ou reçus via les canaux. C'est en quelque sorte le relevé de compte de vos opérations LN.

![Historique des transactions Lightning](assets/fr/14.webp)

Dans cet onglet, vous trouverez :

* **Graphique des factures :** En haut à droite, un graphique montre l'évolution des factures reçues dans le temps, permettant de visualiser l'activité de votre nœud.

* La liste chronologique de toutes les transactions Lightning effectuées *depuis* ou *vers* votre nœud. Chaque entrée peut indiquer :

  * Le type d'opération : **paiement envoyé** (outgoing payment) ou **paiement reçu** (inbound, via une invoice payée).
  * Le montant en sats.
  * La date/heure.
  * L'ID de paiement (préimage hash ou RHash) ou le commentaire (si vous aviez ajouté une mémo à l'invoice).
  * Le statut : **complété**, ou éventuellement **en cours**/*échec* (par ex, un paiement en attente de résolution, mais généralement LND traite ça rapidement, donc peu de "pending" ici comparé aux transactions on-chain).

En bref, la section Transactions vous sert de **journal d'activité LN**. C'est très utile pour vérifier qu'un paiement est bien parti, combien de frais il a coûté, ou retracer l'historique de vos échanges Lightning. En conjonction avec la section Forwards (décrite ensuite), vous aurez une vue complète de l'argent ayant transité par votre nœud.

### Forwards

L'onglet **Forwards** est dédié à l'activité de **routage** de votre nœud, c'est-à-dire aux paiements qui **transitent** par vos canaux (lorsque vous agissez comme nœud intermédiaire sur le réseau Lightning). Si vous exploitez votre nœud comme nœud de routage (routing node), c'est une section importante pour suivre vos performances.

![Statistiques de routage Lightning](assets/fr/15.webp)

Dans Forwards, ThunderHub présente :

* **Filtres et options d'affichage :** En haut à droite, des filtres permettent de trier les données par jour/semaine/mois/année et de choisir entre un affichage graphique ou en tableau.

* **Message d'activité :** Si aucun routage n'a été effectué durant la période sélectionnée, l'interface affiche "No forwards for this period", comme illustré dans cet exemple.

* Une **table des forwards** récents : chaque entrée correspond à un paiement qui a été **acheminé** (forwarded) à travers votre nœud. Pour chaque forward, on voit généralement :

  * l'horodatage,
  * le montant routé (en sats),
  * le **frais gagné** sur ce forward (en sats, c'est la différence entre ce que vous avez reçu sur le canal entrant et envoyé sur le sortant),
  * le canal entrant et le canal sortant utilisés (souvent identifiés par l'alias du peer ou l'ID du canal).
  * le statut (normalement *completed*, ou échec si un forward a échoué en cours de route).

* Des **statistiques agrégées** : ThunderHub calcule et affiche en haut de page des totaux et statistiques sur une période donnée (ex : dernières 24h, ou 7 jours, etc., parfois paramétrable).

En résumé, la section Forwards offre un **aperçu en temps réel de l'activité de routage** de votre nœud Lightning. Couplé aux sections Channels et Rebalance, cela forme un ensemble complet pour optimiser votre node : Channels/Rebalance pour la liquidité, Forwards pour observer le résultat (flux et profits).

### Chain

La section **Chain** correspond à la gestion du portefeuille Bitcoin on-chain de votre nœud LND. Cette interface vous permet de visualiser et gérer les fonds Bitcoin qui servent notamment à ouvrir des canaux ou à recevoir des fonds de canaux fermés.

![Gestion du portefeuille on-chain](assets/fr/16.webp)

Dans Chain, vous trouverez :

* **Balance on-chain :** Affichage du solde total BTC disponible dans le wallet LND.

* **Liste des UTXOs :** Visualisation de toutes les sorties non dépensées (UTXO) avec le montant, les confirmations, l'adresse et le format pour chaque sortie.

* **Historique des transactions :** Tableau détaillé de toutes les transactions Bitcoin avec le type (entrée/sortie), la date, le montant, les frais, les confirmations, le bloc d'inclusion, les adresses et le TXID.

### Amboss

ThunderHub s'intègre avec la plateforme **Amboss** (amboss.space), qui offre des informations détaillées sur les nœuds Lightning, un marketplace de liquidité, et des fonctionnalités utiles comme la sauvegarde de canaux chiffrée et le monitoring de disponibilité.

![Intégration Amboss avec ses options](assets/fr/17.webp)

Dans ThunderHub, la section Amboss permet de **lier** votre nœud à votre compte Amboss :

* **Ghost Address :** Configuration d'une **adresse Lightning personnalisée** pour votre nœud, facilitant les paiements entrants.

* **Sauvegardes automatiques de canaux :** Fonctionnalité phare permettant de **sauvegarder vos canaux** (fichier SCB) sur Amboss de manière chiffrée. Activez **Amboss Auto Backup = Yes** dans les paramètres pour envoyer automatiquement les mises à jour du backup chiffré à chaque changement de canaux. En cas de panne, vous pourrez récupérer vos fonds grâce à ce backup externe.

* **Health Checks :** Activez **Amboss Healthcheck = Yes** pour que votre nœud envoie régulièrement des pings à Amboss. Vous recevrez des alertes si votre nœud semble hors-ligne.

* **Autres fonctionnalités :** Push automatique des soldes, intégration **Magma/Hydro** (marketplace de liquidité), et accès aux statistiques détaillées de performance.

L'intégration Amboss ajoute une **couche de sécurité** essentielle avec le backup externe automatique et le monitoring de disponibilité, accessible directement depuis ThunderHub.

### Tools

La section **Tools** regroupe divers outils avancés pour la gestion de votre nœud. Voici les principaux éléments :

![Interface des outils disponibles](assets/fr/18.webp)

* **Backups (Sauvegardes) :** Gérez manuellement vos sauvegardes de canaux (SCB). ThunderHub permet de **télécharger le fichier de backup** complet de vos canaux (option "Backup all channels -> Download"). Conservez ce fichier `channel-all.bak` en lieu sûr - il est essentiel pour récupérer vos fonds en cas de crash. Vous pouvez aussi **importer** un fichier de backup lors du redéploiement d'un nœud.

* **Accounting (Comptabilité) :** Outil d'export de rapports financiers incluant les frais gagnés/payés et volumes routés sur une période donnée.
* **Messages signés :** **Signez ou vérifiez des messages** avec votre nœud pour prouver la propriété de votre nœud Lightning via signature cryptographique.
* **Macaroons (section Bakery) :** Gérez les **macaroons LND** pour créer des accès personnalisés. L'interface "Bakery" permet de sélectionner précisément chaque permission : "Add or remove Peers", "Create Chain Addresses", "Create Invoices", "Create Macaroons", "Derive Keys", "Get Access Keys", "Get Chain Transactions", "Get Invoices", "Get Wallet Info", "Get Payments", "Get Peers", "Pay Invoices", "Revoke Access Ids", "Send to Chain Addresses", "Sign bytes", "Sign Messages", "Stop Daemon", "Verify bytes signature", "Verify messages", etc. Chaque permission peut être activée individuellement avec les boutons "Yes/No" pour créer un macaroon sur-mesure.
* **Informations système :** Affichage de la version du wallet et des RPCs activés.

En résumé, la section Tools rassemble les fonctions avancées d'administration : sauvegardes, comptabilité, sécurité et gestion des accès, dans une interface unifiée.

### Swap

L'onglet **Swap** de ThunderHub permet d'échanger des satoshis Lightning vers Bitcoin on-chain via le service Boltz. Cette fonctionnalité est utile pour "vider" un surplus de liquidité Lightning vers la chaîne sans fermer un canal.

![Interface de swap via Boltz](assets/fr/19.webp)

Le processus est simple :

* **Montant** : Définissez le montant à échanger
* **Adresse** : Indiquez l'adresse Bitcoin de réception
* **Exécution** : ThunderHub communique avec Boltz pour traiter automatiquement l'échange

**Avantages :**
* Service non-custodial (pas de garde de fonds)
* Préserve vos canaux existants
* Interface intégrée simple d'utilisation

Boltz facture une petite commission et vous payez les frais de transaction Bitcoin standard. ThunderHub affiche tous les coûts avant confirmation.

### Stats

La section **Stats** de ThunderHub offre des **statistiques avancées** sur votre nœud Lightning pour analyser ses performances et optimiser le routage.

![Statistiques du nœud via Amboss](assets/fr/20.webp)

Cette section est essentielle pour optimiser vos frais, identifier les canaux performants et planifier l'expansion de votre nœud.

## Conclusion

**ThunderHub** s'est imposé comme un outil incontournable pour administrer un nœud Lightning **LND** en toute simplicité. Cette interface moderne offre toutes les fonctions essentielles : gestion de canaux, paiements, monitoring, avec des fonctionnalités avancées comme le rebalance automatisé et l'intégration Amboss.

**Avantages clés :**
* Interface épurée et intuitive 
* Outils puissants (rebalance, swaps Boltz, sauvegardes automatiques)
* Compatible avec Umbrel, Voltage, RaspiBlitz et autres distributions

ThunderHub démocratise la gestion avancée d'un nœud Lightning, rendant accessible ce qui nécessitait auparavant des commandes techniques complexes. Que vous soyez débutant ou opérateur expérimenté, ThunderHub vous permet de gérer efficacement votre nœud Lightning via une interface moderne et complète.

## Ressources

**Liens officiels :**
* **Site officiel :** [thunderhub.io](https://thunderhub.io)
* **Documentation :** [docs.thunderhub.io](https://docs.thunderhub.io)
* **Code source GitHub :** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)

