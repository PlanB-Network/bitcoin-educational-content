---
name: Ride The Lightning (RTL)
description: Utiliser Ride The Lightning (RTL) pour gérer son nœud Lightning
---
![cover](assets/cover.webp)
## 1. Introduction

**Ride The Lightning (RTL)** est une interface web complète pour gérer un nœud Lightning Network. Cette application web auto-hébergée offre un **"cockpit" Lightning** accessible depuis votre navigateur. RTL fonctionne avec les principales implémentations Lightning (LND, Core Lightning/CLN et Eclair) et donne un contrôle total sur votre nœud et vos canaux. Open-source (licence MIT) et gratuit, RTL est intégré par défaut dans de nombreuses solutions de nœuds clés en main (RaspiBlitz, MyNode, Umbrel, etc.).

**Pourquoi utiliser RTL ?** Sans interface graphique, la gestion d'un nœud Lightning se fait via des commandes CLI peu conviviales. RTL simplifie ces opérations avec une interface ergonomique. Voici les **cas d'usage principaux** :

* **Visualiser ses canaux et son nœud** – Le tableau de bord affiche le solde on-chain, la liquidité Lightning (locale/distante), l'état de synchronisation, l'alias du nœud, etc. Vous pouvez voir la liste de vos canaux, leur capacité, la répartition local/distante et leur état. RTL propose des tableaux de bord contextuels pour analyser l'activité selon différents angles.

* **Gérer les canaux Lightning** – Ouvrir/fermer des canaux se fait en quelques clics. RTL permet de se connecter à un pair et d'ouvrir un canal sans commande. Vous pouvez ajuster les frais de routage, visualiser le score d'équilibre, ou initier un rebalance circulaire pour rééquilibrer les fonds entre canaux.

* **Suivre et effectuer des paiements** – RTL gère les transactions Lightning : envoi de paiements via factures (invoices), génération de factures pour recevoir, suivi des transactions (paiements, routage) avec historique détaillé. L'interface analyse aussi le routage pour voir les paiements transitant par votre nœud.

* **Gestion du wallet on-chain et sauvegardes** – L'onglet on-chain permet de générer des adresses et d'envoyer des transactions. RTL facilite la sauvegarde des canaux en exportant le fichier SCB pour LND, avec mise à jour automatique à chaque modification de canal.

En résumé, RTL est un **tableau de bord puissant pour le Lightning Network**, offrant une interface pédagogique pour piloter son nœud au quotidien. Ce tutoriel vous guidera dans son installation et son utilisation pour gérer vos canaux et paiements.

## 2. Fonctionnement technique de RTL

![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)

Avant de passer à la pratique, il est utile de comprendre brièvement **comment RTL interagit avec votre nœud Lightning** sur le plan technique.

**Architecture générale :** RTL est une application web construite avec Node.js (backend) et Angular (frontend). Concrètement, RTL tourne comme un petit serveur web local (sur le port 3000 par défaut) qui dialogue avec votre implémentation Lightning via les API de celle-ci. Selon le type de nœud :

* Avec **LND**, RTL utilise l'API REST de LND (port 8080) pour exécuter les commandes Lightning. La connexion est sécurisée par TLS et nécessite le fichier **macaroon d'admin** de LND pour s'authentifier.

* Avec **Core Lightning (CLN)**, RTL utilise soit l'API REST fournie par *c-lightning-REST*, soit un **rune d'accès** via le plugin `commando`. Les solutions comme Umbrel configurent automatiquement ces éléments.

* Avec **Eclair**, RTL se connecte à l'API REST d'Eclair en utilisant le mot de passe d'authentification configuré.

**Configuration et sécurité :** RTL se configure via un fichier JSON (`RTL-Config.json`) où vous définissez le port web, le mot de passe d'accès, et les informations de connexion à votre nœud. L'interface web est protégée par un login/mot de passe (par défaut `password` à changer) et supporte la 2FA. Par défaut, RTL s'exécute en HTTP local (`http://localhost:3000`), mais pour un accès distant, utilisez toujours une connexion sécurisée (HTTPS via reverse-proxy, Tor, ou VPN).

En résumé, RTL est un composant supplémentaire qui se connecte à votre nœud via des API sécurisées, nécessite des jetons d'accès appropriés, et propose sa propre couche de sécurité. Cette architecture modulaire permet même de gérer **plusieurs nœuds Lightning avec une seule instance RTL**.

## 3. Installation de RTL

RTL étant distribué en open-source, il existe plusieurs méthodes pour l'installer sur votre système. Dans cette section, nous couvrirons deux approches principales : l'installation manuelle et l'installation via Umbrel.

### Méthode manuelle

L'installation manuelle convient si vous aimez garder le contrôle fin ou si vous intégrez RTL dans une configuration personnalisée. Les étapes ci-dessous concernent un nœud LND tournant sous Linux (ex: Raspberry Pi ou VPS sous Ubuntu/Debian), mais sont similaires pour CLN/Eclair.

**Prérequis :** assurez-vous d'avoir un nœud Bitcoin **synchronisé** et un nœud Lightning fonctionnel (LND, CLN ou Eclair) sur la machine. RTL ne contient pas de nœud Lightning en soi, il se connecte à un nœud existant. Il vous faut également **Node.js** installé (version 14+ recommandée). Vous pouvez vérifier avec `node -v` ou installer Node depuis le site officiel (https://nodejs.org/en/download/) ou votre gestionnaire de paquets.

Les grandes étapes d'installation sont :

**Télécharger le code RTL** : Clonez le dépôt GitHub officiel de RTL dans le répertoire de votre choix. Par exemple :

   ```bash
   git clone https://github.com/Ride-The-Lightning/RTL.git
   cd RTL
   ```

**Installer les dépendances** : RTL est une application Node.js, il faut donc installer ses modules requis. Dans le dossier RTL, exécutez :

   ```bash
   npm install --omit=dev --legacy-peer-deps
   ```

   Cette commande installe les packages NPM nécessaires (en ignorant les dépendances de développement). L'option `--legacy-peer-deps` est recommandée pour éviter d'éventuels conflits de dépendances Node.

**Configurer RTL** : Une fois les dépendances en place, préparez le fichier de configuration. Copiez/renommez le fichier `Sample-RTL-Config.json` à la racine du projet en `RTL-Config.json`. Ouvrez-le dans votre éditeur :

   * **Mot de passe UI** : choisissez un mot de passe sécurisé et renseignez-le dans `multiPass` (à la place de `"password"` par défaut).
   * **Port** : par défaut `3000`. Vous pouvez le modifier si ce port est déjà pris sur votre machine.
   * **Nœud** : dans la section `nodes[0]`, ajustez les paramètres pour votre nœud :
     * `lnNode` : un nom descriptif de votre nœud (ex: `"LND Node Maison"`).
     * `lnImplementation` : `"LND"` (ou `"CLN"`/`"ECL"` selon le cas).
     * Sous `authentication`:
       * `macaroonPath` : indiquez le chemin complet du dossier qui contient le macaroon admin de LND.
       * `configPath` : chemin vers le fichier de config du nœud (`lnd.conf` pour LND).
     * Sous `settings`:
       * `fiatConversion` : mettre à `true` si vous voulez la conversion en devises fiat.
       * `unannouncedChannels` : mettre à `true` pour voir les canaux non-annoncés.
       * `themeColor` et `themeMode` : personnalisation de l'interface.
       * `channelBackupPath` : chemin pour les backups de canaux LND.
       * `lnServerUrl` : URL de votre nœud Lightning (ex: `https://127.0.0.1:8080`).

**Lancer le serveur RTL** : Dans le dossier RTL, exécutez :

   ```bash
   node rtl
   ```

   L'application démarre et est accessible à l'adresse `http://localhost:3000`.

**(Optionnel) Exécuter RTL en service** : Pour un démarrage automatique, créez un service systemd :

Pour cela :
- Ouvrez un terminal sur votre machine.
- Créez un nouveau fichier de service avec la commande suivante (remplacez `nano` par votre éditeur préféré) :
   ```bash
   sudo nano /etc/systemd/system/RTL.service
   ```
- Copiez-collez le contenu ci-dessous dans ce fichier :

```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```

- Remplacez `/chemin/vers/RTL/rtl` par le chemin réel vers le fichier `rtl` sur votre machine, et `<votre_user>` par votre nom d'utilisateur Linux.
- Enregistrez et fermez le fichier.
- Rechargez la configuration systemd :
   ```bash
   sudo systemctl daemon-reload
   ```
- Activez et démarrez le service RTL :
   ```bash
   sudo systemctl enable RTL
   sudo systemctl start RTL
   ```

RTL démarrera désormais automatiquement à chaque redémarrage de la machine. Vous pouvez vérifier son statut avec :
```bash
sudo systemctl status RTL
```

### Installation via Umbrel

Si vous utilisez [Umbrel](https://getumbrel.com), l'installation de RTL est beaucoup plus simple :

- Accédez à l'interface Umbrel (généralement via `http://umbrel.local`)
- Allez dans l'**App Store**
- Recherchez "Ride The Lightning"

**Remarque importante : il existe deux applications distinctes RTL dans l'App Store Umbrel :**
- **Ride The Lightning** (pour LND) : à utiliser si vous exploitez le nœud Lightning par défaut d'Umbrel (LND).
- **Ride The Lightning (Core Lightning)** : à utiliser uniquement si vous avez installé l'application *Core Lightning* sur Umbrel et souhaitez gérer ce nœud avec RTL.

*Chaque version de RTL est préconfigurée pour dialoguer avec l'implémentation correspondante (LND ou Core Lightning). Si vous n'avez pas changé de nœud Lightning, choisissez simplement la version LND classique.*

![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)

- Cliquez sur **Installer**

![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)

**Important :** Après l'installation, RTL affiche un écran avec le mot de passe par défaut. **Copiez et sauvegardez ce mot de passe** - il vous sera nécessaire pour vous connecter à l'interface RTL. Ce mot de passe s'affichera à chaque démarrage de RTL jusqu'à ce que vous cochiez l'option "Don't show it again". 

Umbrel s'occupe automatiquement de :
* Télécharger et configurer RTL
* Configurer les accès au nœud Lightning
* Gérer les mises à jour
* Sécuriser l'accès à l'interface

Une fois installée, l'application apparaît dans votre menu *Apps* sur Umbrel. Cliquez sur **Ride The Lightning** pour la lancer.

![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)

Sur l'écran de connexion, entrez le mot de passe que vous avez copié précédemment. Une fois connecté, l'interface web RTL sera accessible directement depuis le dashboard Umbrel, sans configuration supplémentaire nécessaire!

## 4. Présentation et utilisation de l'interface RTL

Maintenant que RTL est installé et fonctionnel, explorons son interface web et ses principales fonctionnalités. Nous allons parcourir les différentes sections de l'application pour vous donner une vue d'ensemble complète.

### Le tableau de bord principal

![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)

Dès votre connexion, vous accédez au **tableau de bord principal** qui offre une vue d'ensemble de votre nœud Lightning. Cette page centralise les informations essentielles :
- Votre solde Lightning total
- Le solde on-chain disponible
- La répartition de votre liquidité (entrante/sortante)
- Un accès rapide pour envoyer ou recevoir des sats via votre nœud Lightning

### Gestion des fonds on-chain

![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)

L'onglet **On-chain** vous permet de gérer vos bitcoins directement sur la chaîne principale :
- Affichage du solde en différentes unités (sats, BTC, USD)
- Liste complète des transactions
- Génération d'adresses Taproot (P2TR), P2SH (NP2WKH) ou Bech32 (P2WKH)
- Gestion des UTXO, réception et envoi de bitcoins

### Lightning : présentation détaillée des sous-menus

L'interface RTL propose un menu latéral dédié au Lightning Network, regroupant toutes les fonctionnalités essentielles pour gérer votre nœud. Voici le détail de chaque sous-menu, dans l'ordre de la capture d'écran :

#### 1. Peers/Channels

![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)

Ce sous-menu permet de :
- Visualiser la liste de vos pairs connectés et de vos canaux Lightning ouverts ou en attente.
- Ajouter un nouveau pair (connexion à un autre nœud Lightning).
- Ouvrir, fermer ou gérer les canaux existants.
- Consulter les détails de chaque canal : capacité, soldes locaux/distants, état, historique des échanges, score d'équilibre, etc.

#### 2. Transactions

![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)

Dans ce sous-menu, vous pouvez :
- Envoyer des paiements Lightning (via une invoice).
- Générer et gérer vos factures (invoices) pour recevoir des paiements.
- Consulter l'historique complet des paiements envoyés et reçus, avec détails (montant, date, statut, frais, nombre de sauts, etc.).

#### 3. Routing

Ce sous-menu affiche :
- Les paiements routés par votre nœud pour d'autres utilisateurs du réseau Lightning.
- Les statistiques de routage : nombre de transactions relayées, frais gagnés, erreurs rencontrées.
- Un historique exportable pour analyse avancée.

#### 4. Reports

Ce sous-menu propose :
- Des rapports détaillés sur l'activité de votre nœud Lightning.
- Des graphiques et tableaux sur les canaux, les paiements, les frais, la capacité, etc.
- Des outils pour mieux comprendre la performance de votre nœud.

#### 5. Graph Lookup

Ce sous-menu permet :
- D'explorer la topologie du réseau Lightning.
- De rechercher des nœuds ou des canaux spécifiques.
- D'obtenir des informations sur la connectivité et la capacité globale du réseau.

#### 6. Sign/Verify

Ce sous-menu offre :
- La possibilité de signer un message avec la clé de votre nœud (preuve de propriété).
- La vérification de signatures pour authentifier des messages provenant d'autres nœuds.

#### 7. Backup

Ce sous-menu est dédié à la sauvegarde :
- Export du fichier de backup des canaux (SCB pour LND).
- Restauration de la configuration ou des canaux en cas de besoin.
- Conseils pour sécuriser vos sauvegardes.

#### 8. Node/Network

![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)

Dans ce sous-menu, vous trouverez :
- Un résumé complet de l'état de votre nœud Lightning : alias, version, couleur, état de synchronisation.
- Les statistiques sur les canaux (actifs, en attente, fermés), la capacité totale, la connectivité.
- Des informations sur le réseau Lightning global et la position de votre nœud dans ce réseau.

### Services : Boltz Swaps

![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)

Boltz est un service d'échange respectueux de la vie privée, non custodial, qui permet de convertir des bitcoins entre le réseau Lightning et la blockchain Bitcoin (on-chain). Il propose deux types d'opérations : le Reverse Submarine Swap (**Swap Out**) et le Submarine Swap (**Swap In**).

#### Swap Out (Reverse Submarine Swap)

Le Swap Out permet de convertir des sats disponibles sur le réseau Lightning en bitcoins on-chain. Ce mécanisme est utile lorsqu'un nœud manque de capacité entrante ou lorsqu'on souhaite récupérer ses fonds sur une adresse on-chain. Le processus fonctionne ainsi :
- L'utilisateur choisit un montant à échanger
- Le nœud envoie un paiement Lightning à Boltz
- En échange, Boltz bloque un montant équivalent en bitcoins on-chain
- Une fois la transaction confirmée, l'utilisateur peut réclamer les fonds en révélant un secret utilisé dans le swap

Ce processus se fait de manière non custodiale, Boltz ne détenant jamais les fonds de l'utilisateur.
![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)

#### Swap In (Submarine Swap)

À l'inverse, le Swap In permet de réinjecter des fonds on-chain dans le réseau Lightning. C'est particulièrement utile pour restaurer une capacité de sortie sur ses canaux. Le déroulement est le suivant :
- L'utilisateur envoie des bitcoins à une adresse spécifique générée par Boltz
- Ces fonds ne peuvent être débloqués par Boltz que s'il règle une facture Lightning générée par le nœud de l'utilisateur
- Une fois la facture payée, les fonds sont disponibles sur le canal Lightning, augmentant la capacité de sortie du nœud

![Configuration d'un swap-in](assets/fr/12.webp)

Ces deux mécanismes permettent de gérer efficacement la liquidité des canaux Lightning tout en maintenant la souveraineté de l'utilisateur sur ses fonds.

### Configuration et personnalisation

![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)

L'onglet **Node Config** permet de personnaliser votre expérience :
- Activation des canaux non annoncés
- Personnalisation de l'affichage des soldes
- Configuration de l'explorateur de blocs
- Ajustement de l'interface

### Documentation et aide

![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)

Enfin, la section **Help** offre une documentation complète sur :
- Configuration initiale
- Gestion des pairs et canaux
- Paiements et transactions
- Sauvegardes et restaurations
- Rapports et statistiques
- Signatures et vérifications
- Paramètres du nœud et de l'application

Cette interface complète vous permet de gérer efficacement votre nœud Lightning, des opérations basiques aux fonctionnalités avancées, le tout dans une interface intuitive et bien organisée.

## 5. Cas d'usage avancés & sécurité

Dans cette partie, voici l'essentiel à retenir pour aller plus loin avec RTL et sécuriser votre nœud Lightning :

### Monitoring et dépannage

Pour surveiller votre nœud, vous pouvez exporter les données de RTL (logs, CSV) et les visualiser dans des outils comme Grafana. En cas de problème (paiement bloqué, canal inactif), consultez les logs de LND/CLN et utilisez les commandes de diagnostic (`lncli listchannels`, `lncli pendingchannels`, etc.). RTL propose aussi une interface de logs pour suivre les événements de routage.

### Accès distant sécurisé

N'exposez jamais RTL directement sur Internet. Privilégiez :
- **VPN** (ex : Tailscale) pour un accès privé et chiffré
- **Tor** pour un accès anonyme et sécurisé
- **Reverse proxy HTTPS** (Nginx/Caddy) uniquement si vous maîtrisez la configuration

https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Bonnes pratiques de sécurité

- **Protégez vos accès** : ne partagez jamais le fichier admin.macaroon ni votre mot de passe RTL. Limitez les permissions des fichiers sensibles.
- **Sauvegardes régulières** : exportez le fichier de backup des canaux (SCB) après chaque modification et stockez-le hors du nœud.
- **Mises à jour** : gardez RTL, votre nœud et Umbrel à jour pour bénéficier des dernières corrections de sécurité.
- **Confidentialité** : anonymisez les logs et captures d'écran avant de les partager. Ne diffusez jamais vos soldes ou la liste de vos pairs publiquement.
- **Accès unique** : RTL n'est pas multi-utilisateur. Ne partagez pas l'accès admin. Pour un accès en lecture seule, utilisez un macaroon dédié si besoin.

En appliquant ces principes, vous limitez fortement les risques et gardez le contrôle sur votre nœud Lightning.

## 7. Conclusion

**Ride The Lightning** est un outil incontournable pour gérer efficacement un nœud Bitcoin/Lightning, que vous soyez débutant ou utilisateur avancé. Il offre une interface claire pour piloter vos canaux, paiements et la santé de votre nœud, tout en permettant d'approfondir votre compréhension du Lightning Network.

RTL se distingue par sa compatibilité multi-implémentation, ses fonctions avancées (rebalancing, swaps, rapports) et sa pédagogie. Pour des besoins simples, l'interface Umbrel ou un wallet mobile suffisent, mais RTL prend tout son sens pour une gestion active et optimisée de votre nœud.

Pour aller plus loin :
- Site officiel RTL : https://www.ridethelightning.info/
- GitHub RTL : https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork** : [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Discussions techniques, annonces de projets, retours d'expérience et ressources pédagogiques
- **Umbrel Community Forum** : [community.getumbrel.com](https://community.getumbrel.com) - Forum officiel avec section dédiée Bitcoin/Lightning, guides et solutions aux problèmes courants
- **Lightning Network Developers** : [github.com/lightning](https://github.com/lightning) - Dépôt GitHub officiel pour suivre le développement et contribuer au code source
- **Stack Exchange Bitcoin** : [bitcoin.stackexchange.com](https://bitcoin.stackexchange.com) - Questions-réponses techniques avec des développeurs et utilisateurs avancés

En résumé, RTL vous donne le contrôle total sur votre nœud Lightning, dans une interface moderne et complète.

**Sources :** RTL official website; RTL GitHub; Umbrel App Store; Umbrel Community; Plan B Network resources.

Pour approfondir votre compréhension du fonctionnement du Lightning Network, je vous recommande également de suivre ce cours gratuit :

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb