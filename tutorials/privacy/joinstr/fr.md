---
name: Joinstr
description: CoinJoins décentralisés via le réseau Nostr pour une confidentialité Bitcoin souveraine
---

![cover](assets/cover.webp)

La transparence de la blockchain Bitcoin permet de tracer l'historique des transactions. Les CoinJoins brisent ces liens en mélangeant plusieurs transactions simultanées, restaurant un niveau de confidentialité comparable à l'argent liquide.

Cependant, les solutions traditionnelles dépendent d'un coordinateur central, point de défaillance unique. Wasabi et Samourai ont cessé leurs opérations en 2024 sous pression réglementaire.

**Joinstr** élimine ce point faible en utilisant le réseau décentralisé Nostr pour la coordination. Cette application open source permet des CoinJoins véritablement souverains, où aucune autorité centrale ne peut censurer, surveiller ou interrompre le service.

## Qu'est-ce que Joinstr ?

Joinstr est un outil open source qui révolutionne l'approche des CoinJoins en tirant parti du protocole Nostr comme infrastructure de coordination. Contrairement aux solutions centralisées nécessitant un serveur dédié, Joinstr s'appuie sur un réseau distribué de relais Nostr pour permettre aux participants de se coordonner directement entre pairs.

**Architecture décentralisée** : Le fonctionnement repose sur le remplacement du coordinateur central par le réseau Nostr. Les participants créent ou rejoignent des "pools" en publiant des annonces chiffrées via les relais Nostr. Ces informations (montants, participants, adresses) restent inintelligibles pour les relais, garantissant qu'aucune entité centrale ne peut surveiller, censurer ou filtrer les CoinJoins.

**Mécanisme SIGHASH_ALL|ANYONECANPAY** : Joinstr exploite ce flag de signature Bitcoin permettant à chaque participant de signer uniquement son entrée tout en validant toutes les sorties. Chaque utilisateur génère sa PSBT localement, la signe, puis la diffuse via Nostr. Vos bitcoins restent sous votre contrôle exclusif jusqu'à la signature finale.

**Philosophie** : Joinstr s'inscrit dans l'éthique cypherpunk de Bitcoin, visant trois objectifs : **résistance à la censure** (aucune autorité ne peut arrêter le service), **non-custodialité totale** (vous conservez vos clés privées), et **égalité de traitement** (aucune UTXO ne peut être discriminée).

### Fonctionnalités principales

**Pools flexibles** : Contrairement aux dénominations fixes, tout utilisateur peut créer un pool avec le montant exact souhaité et le nombre de participants cible, optimisant l'utilisation des UTXO sans fractionnement artificiel.

**Frais transparents** : Aucun frais de coordination. Seuls les frais de transaction Bitcoin sont répartis équitablement entre participants (quelques milliers de satoshis par personne).

**Éphémérité** : Aucune donnée utilisateur conservée. Les informations transitent via des messages Nostr éphémères chiffrés, immédiatement oubliés après la transaction.

### Plateformes disponibles

Ce tutoriel se concentre sur **l'application Android**, seule solution actuellement stable et recommandée. Un plugin Electrum existe mais rencontre des problèmes de compatibilité le rendant instable. Une interface web est en développement.

## Configuration Bitcoin Core

Joinstr Android nécessite une connexion à un nœud Bitcoin via RPC. Vous devez d'abord configurer Bitcoin Core sur votre ordinateur pour accepter les connexions depuis votre téléphone.

**Note** : Pour plus de détails sur la configuration complète de Bitcoin Core, consultez nos tutoriels dédiés : 

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Prérequis réseau

#### Localiser votre adresse IP locale

Votre téléphone Android doit pouvoir joindre votre nœud Bitcoin sur le réseau local. Trouvez l'adresse IP de votre ordinateur :

**Sur macOS** :

```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```

Alternative simple :

```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```

**Sur Linux** :

```bash
hostname -I | awk '{print $1}'
```

**Sur Windows** :

```cmd
ipconfig
```

Cherchez l'adresse IPv4 (format `192.168.x.x` ou `10.0.x.x`)

### Configuration RPC

#### Éditer bitcoin.conf

![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)

Localisez votre fichier `bitcoin.conf` :
- **Linux** : `~/.bitcoin/bitcoin.conf`
- **macOS** : `~/Library/Application Support/Bitcoin/bitcoin.conf`
- **Windows** : `%APPDATA%\Bitcoin\bitcoin.conf`

![CONTENU BITCOIN.CONF](assets/fr/02.webp)

Ouvrez le fichier avec votre éditeur de texte préféré et ajoutez cette configuration pour activer le serveur RPC.

**Configuration recommandée pour débuter (signet)** :

```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```

**Configuration mainnet** (pour usage en production) :

```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```

**Important** :
- **Signet est fortement recommandé** pour vos premiers tests : l'application est encore en développement (beta), des bugs peuvent subsister. Signet permet de tester gratuitement sans risquer de fonds réels
- Remplacez `192.168.1.0/24` par votre subnet réseau (ex: si votre IP est `192.168.68.57`, utilisez `192.168.68.0/24`)

**Sécurité** : Générez un mot de passe fort :

```bash
openssl rand -base64 32
```

### Initialisation

#### Redémarrage et vérification

1. Arrêtez Bitcoin Core complètement
2. Redémarrez-le pour appliquer la configuration


![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)

Lors du premier démarrage sur signet, Bitcoin Core va télécharger et synchroniser la blockchain signet. Cette opération est beaucoup plus rapide que sur mainnet (quelques minutes seulement). Patientez jusqu'à ce que la synchronisation soit complète avant de continuer.

![CRÉATION DE WALLET](assets/fr/04.webp)

Une fois synchronisé, créez un nouveau portefeuille en cliquant sur "Create a new wallet". Donnez-lui un nom explicite comme `tuto_joinstr_signet`.

![WALLET CRÉÉ](assets/fr/05.webp)

Votre wallet est maintenant créé et prêt à recevoir des bitcoins signet pour vos tests.

#### Obtenir des bitcoins signet (test)

Pour tester Joinstr sur signet, vous avez besoin de bitcoins de test gratuits :

![SIGNET FAUCET](assets/fr/06.webp)

Utilisez un faucet signet public comme :
- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [signet257.bublina.eu.org](https://signet257.bublina.eu.org)

Dans Bitcoin Core, générez une nouvelle adresse de réception (onglet "Receive"), copiez-la, puis collez-la dans le formulaire du faucet. Résolvez le captcha si nécessaire. Vous recevrez des bitcoins signet gratuits en quelques secondes.

## Application Android

### Installation

![APPLICATION ANDROID](assets/fr/07.webp)

Rendez-vous sur [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) pour télécharger la dernière version APK. Sur votre navigateur Android, téléchargez le fichier puis ouvrez-le pour lancer l'installation. Vous devrez autoriser l'installation depuis des sources inconnues dans les paramètres de sécurité de votre téléphone si nécessaire.

### Configuration de l'application

![PERMISSIONS VPN](assets/fr/08.webp)

Au premier lancement, l'application Joinstr demandera des autorisations pour contrôler le VPN intégré. Acceptez les deux demandes de permission : le contrôle OpenVPN et la connexion VPN. Ces autorisations sont nécessaires pour l'intégration du VPN qui protège votre confidentialité réseau.

![INTERFACE APPLICATION](assets/fr/09.webp)

L'application Joinstr est organisée en trois onglets principaux :
- **Home** : Écran d'accueil
- **Pools** : Création et gestion des pools CoinJoin
- **Settings** : Configuration de l'application

![CONFIGURATION SETTINGS](assets/fr/13.webp)

Configurez les paramètres dans l'onglet "Settings" :

**1. Nostr Relay** : Adresse du relais Nostr pour la coordination des pools
- Exemple : `wss://relay.damus.io`
- Autres relais recommandés : `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Important** : Tous les participants doivent utiliser le **même relais Nostr** pour voir et rejoindre les mêmes pools. Si vous utilisez un relais différent, vous ne verrez pas les pools créés sur d'autres relais

**2. Node URL** : Adresse IP de votre nœud Bitcoin (sans le port)
- Format : `http://VOTRE_IP_LOCALE`
- Exemple : `http://192.168.68.57`

**3. RPC Username** : Le nom d'utilisateur configuré dans `rpcuser=` de votre bitcoin.conf
- Exemple : `satoshi`

**4. RPC Password** : Le mot de passe configuré dans `rpcpassword=` de votre bitcoin.conf

**5. RPC Port** : Le port RPC selon le réseau
- **Mainnet** : `8332`
- **Signet** : `38332`

**6. Wallet** : Sélectionnez le portefeuille Bitcoin Core contenant les UTXO à mixer
- Exemple : `tuto_joinstr_signet`

**7. VPN Gateway** : Sélectionnez un serveur VPN Riseup
- Exemple : `(Paris) vpn07-par.riseup.net`
- Autres disponibles : Amsterdam, Seattle, etc.
- ⚠️ **Important** : Tous les participants d'un même pool doivent utiliser le **même VPN Gateway** pour participer au CoinJoin. Pendant le round de mixing, tous les participants doivent apparaître avec la même adresse IP de sortie pour empêcher l'analyse réseau de corréler les participants

L'application Joinstr **intègre nativement** le VPN Riseup, ce qui simplifie la coordination entre participants.

**Important** :
- Assurez-vous que votre téléphone et votre ordinateur sont sur le même réseau WiFi local
- La connexion VPN s'activera automatiquement lors de la participation à un pool
- Cliquez sur **"Save"** après avoir configuré tous les paramètres

## Utilisation pratique

### Créer ou rejoindre un pool

![CRÉATION POOL ANDROID](assets/fr/10.webp)

Vous avez deux options pour participer à un CoinJoin :

**Option 1 : Créer un nouveau pool**

Appuyez sur "Create New Pool" dans l'onglet "Pools". Spécifiez la dénomination en BTC (par exemple 0.002 BTC) et le nombre de participants souhaité (minimum 2, recommandé 3-5 pour plus d'anonymat). L'application attend ensuite que d'autres utilisateurs rejoignent votre pool. Une fois le nombre requis atteint, le processus d'enregistrement des sorties commence automatiquement, et vous devrez sélectionner votre UTXO à mixer et cliquer sur "Register".

**⏱️ Important** : Les pools expirent après **10 minutes** d'inactivité. Si le nombre requis de participants n'est pas atteint, le pool sera automatiquement fermé.

**Option 2 : Rejoindre un pool existant**

Dans l'onglet "View Other Pools", parcourez les pools disponibles créés par d'autres utilisateurs. Sélectionnez un pool correspondant à votre montant et rejoignez-le. Assurez-vous d'avoir configuré le même relais Nostr et le même VPN Gateway que les autres participants (voir section Configuration).

**Règle de sélection des UTXO** : Votre UTXO doit être légèrement supérieur à la dénomination du pool (entre +500 et +5000 sats de surplus).

**Exemple** : Pour un pool de 0.002 BTC (200 000 sats), utilisez un UTXO entre 200 500 et 205 000 sats.

![PROCESSUS COINJOIN](assets/fr/11.webp)

Le processus est ensuite **entièrement automatique** : après l'enregistrement de votre input, l'application attend que tous les participants enregistrent leurs inputs. Une fois tous les inputs enregistrés, la PSBT est créée, signée automatiquement avec vos clés, puis combinée avec les signatures des autres participants. Enfin, la transaction complète est diffusée sur le réseau Bitcoin. Vous recevez le TXID (identifiant de transaction) une fois la diffusion effectuée. Aucune manipulation manuelle de PSBT n'est requise sur Android.

### Vérification on-chain

![TRANSACTION MEMPOOL](assets/fr/12.webp)

Une fois la transaction diffusée, vous recevez le TXID (identifiant de transaction). Consultez-le sur [mempool.space](https://mempool.space) ou votre explorateur préféré. Pour tester sur signet, utilisez [mempool.space/signet](https://mempool.space/signet).

Vous pourrez observer :

- **N entrées** : Une par participant (dans notre exemple, 2 entrées)
- **N sorties identiques** : Montant exact de la dénomination (ici, 2 sorties de 0.00199800 BTC chacune)
- **Diagramme de flux** : mempool.space affiche visuellement le mixage des entrées vers les sorties
- **Caractéristiques** : La transaction peut être identifiée comme SegWit, Taproot, RBF, etc.

Toutes les sorties principales ayant le même montant, il est **impossible de déterminer laquelle appartient à qui**. C'est le principe fondamental du CoinJoin : l'indistinguabilité des outputs.

**Exemple de transaction signet** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)

**Attention** : Si vos UTXO étaient plus grandes que la dénomination du pool, vous aurez des sorties de change (surplus). Ces UTXO de change restent traçables et doivent être gérées séparément de vos outputs anonymisés. Ne les combinez jamais avec vos outputs mixés.

## Qualité du CoinJoin et ensembles d'anonymat

L'efficacité d'un CoinJoin se mesure par son **ensemble d'anonymat** (anonset) : le nombre de sorties de valeur identique produites par la transaction. Plus ce nombre est élevé, plus il est difficile de déterminer quelle entrée correspond à quelle sortie.

Joinstr génère actuellement des pools de **2 à 5 participants** en moyenne. Ces chiffres sont inférieurs aux coordinateurs centralisés traditionnels comme Wasabi (50-100 participants) ou Whirlpool (5-10 participants), mais c'est le prix de la décentralisation.

💡 **Pour comprendre en détail les ensembles d'anonymat et leur calcul**, consultez notre cours complet : [Les ensembles d'anonymat](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).

### Joinstr vs autres CoinJoins

| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

💡 **Autres solutions CoinJoin actives** :
- **Ashigaru** : Implémentation open source du protocole Whirlpool avec coordinateur centralisé mais déployable de manière décentralisée. Continue de fonctionner après la saisie de Samourai Wallet en 2024.
- **JoinMarket** : Solution P2P décentralisée sans coordinateur central, basée sur un modèle économique maker/taker où les "makers" fournissent de la liquidité et sont rémunérés par les "takers".

https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Le trade-off fondamental** : Joinstr et JoinMarket sont les deux seules solutions sans coordinateur central. JoinMarket utilise un modèle économique P2P avec incitations financières, tandis que Joinstr utilise Nostr pour la coordination sans frais. Joinstr sacrifie les grands ensembles d'anonymat immédiats au profit de la simplicité (pas de gestion maker/taker) et de l'absence totale de frais de coordination.

**Recommandation pratique** : Pour compenser les pools plus petits, effectuez plusieurs rounds de CoinJoin successifs avec des participants différents. Espacez vos rounds et changez de relais Nostr entre chaque round pour maximiser votre confidentialité.

N'hésitez pas à consulter notre cours complet sur la confidentialité sur bitcoin pour plus d'information sur ce sujet :

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Avantages et limitations

### Points forts

**Confidentialité renforcée** : La combinaison du chiffrement des communications Nostr, du VPN partagé entre participants, et de l'utilisation recommandée de Tor crée une protection multicouche difficile à contourner.

**Frais transparents et minimaux** : Absence de frais de coordination, seuls les frais miniers sont partagés équitablement entre participants. Aucun pourcentage prélevé par un opérateur.

### Contraintes à considérer

- **Liquidité variable** : Pools plus petits, attente possible pour réunir les participants
- **Projet en évolution** : Application en beta, bugs possibles. Testez d'abord avec petits montants sur signet
- **Attaques Sybil** : Possibilité qu'un adversaire contrôle plusieurs participants du pool

## Bonnes pratiques

**Isolation des UTXO** : Ne combinez jamais une UTXO mixée avec une non-mixée. Utilisez un portefeuille séparé pour vos outputs anonymisés.

**Rounds multiples essentiels** : Effectuez minimum 3 rounds successifs avec des participants différents. Variez montants et timings pour éviter les patterns. Espacez les rounds de plusieurs heures.

**Protection réseau** : Utilisez systématiquement Tor en plus du VPN intégré. Générez des clés Nostr éphémères pour chaque session importante.

**Progression prudente** : Commencez sur signet avec de petits montants.

## Conclusion

Joinstr représente une solution de confidentialité Bitcoin véritablement décentralisée. En utilisant Nostr pour la coordination, elle élimine la dépendance aux coordinateurs centraux tout en préservant la souveraineté des utilisateurs.

**Pour qui ?** Utilisateurs valorisant la résistance à la censure et prêts à effectuer plusieurs rounds de CoinJoin pour compenser les pools plus petits.

Dans un contexte de surveillance financière croissante, disposer d'outils décentralisés pour protéger sa vie privée devient essentiel.

## Ressources

### Documentation officielle
- [Site officiel Joinstr](https://joinstr.xyz)
- [Documentation utilisateur](https://docs.joinstr.xyz/users/using-joinstr)
- [Documentation technique](https://docs.joinstr.xyz/overview/how-does-it-work)
- [Code source GitLab](https://gitlab.com/invincible-privacy/joinstr)
- [Application Android](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)

### Tutoriels
- [Tutoriel Electrum plugin](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Guide complet par Uncensored Tech

### Communauté et support
- [Groupe Telegram Joinstr](https://t.me/joinstr) - Support communautaire et obtention de coins signet
- [Discussion technique sur DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)

### Outils complémentaires
- [Signet Faucet](https://signetfaucet.com) - Bitcoins de test gratuits
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Faucet alternatif
- [Mempool.space](https://mempool.space) - Explorateur de blocs avec analyse de confidentialité
