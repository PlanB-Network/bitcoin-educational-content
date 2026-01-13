---
name: LNbits
description: Plateforme de comptabilité marchande
---
![presentation](assets/cover.webp)

## Système comptable

LNbits est doté de nombreux outils permettant de contrôler et de canaliser vos fonds entrants et sortants, de connecter votre boutique en ligne ou même des dispositifs tels qu'un portefeuille matériel ou un distributeur automatique de billets que vous avez construit vous-même. Les types d'utilisateurs sont les suivants :


- Les propriétaires de portefeuilles qui souhaitent utiliser LNbits comme interface pour la gestion de leurs fonds ainsi que ses fonctions supplémentaires.
- Les commerçants ou prestataires de services en ligne et hors ligne qui souhaitent accepter les paiements Bitcoin onchain et Lightning Network.
- Les développeurs qui souhaitent créer des applications pour le réseau Lightning.
- Les opérateurs de nœuds qui souhaitent intégrer leur nœud au système LNbits à des fins comptables.
- Tous ont des besoins différents. Nous construisons LNbits de manière modulaire afin que chaque utilisateur puisse utiliser nos fonctionnalités de la manière qui lui convient le mieux.

## Gestionnaire de portefeuille

LNbits est un système de comptabilité libre et gratuit - pas un gestionnaire de nœuds. La gestion des canaux est le domaine du nœud Lightning qui est connecté à LNbits en tant que source de financement comme LND ou c-lightning. Le superutilisateur ou les utilisateurs administrateurs du système LNbits sont responsables de la gestion de l'accessibilité globale et de la configuration des fonctions de comptabilité et des extensions internes.

LNbits sert d'interface entre l'utilisateur et le nœud Lightning, offrant un moyen simple et convivial de gérer et d'interagir avec le réseau de paiement.

Considérez LNbits comme un "cadre modulaire wordpress" pour votre nœud. Une plateforme facile à gérer, basée sur des extensions que vous pouvez combiner pour de nombreux cas d'utilisation.

Considérez LNbits comme votre propre logiciel de gestion financière bancaire. Votre nœud offre des canaux de paiement et LNbits étend votre nœud pour qu'il puisse gérer plus d'un portefeuille éclair (lightning wallet) fourni avec votre nœud. Ces portefeuilles ne doivent pas nécessairement vous appartenir. Supposons que vous, en tant que gestionnaire du nœud LN, disposiez déjà de suffisamment de liquidités et de fonds et que vous souhaitiez offrir des services bancaires en bitcoins à vos amis, à votre famille, à votre propre magasin ou à d'autres marchands réguliers.

Vous leur offrirez un moyen simple d'ouvrir un "compte bancaire" sur votre nœud sans avoir accès à d'autres portefeuilles sur votre nœud et à toutes les liquidités de votre nœud, mais seulement à leur part. Votre nœud (la banque) agit uniquement en tant que fournisseur de transport pour leurs paiements (entrée/sortie).

REMARQUE : tous les fonds que vos "clients" déposent sur leurs comptes bancaires LNbits sur votre nœud, iront directement dans les canaux LN de votre nœud. Cela signifie que VOUS êtes le véritable propriétaire de ces fonds. Vous aurez une grande responsabilité pour ces fonds. Ne soyez pas méchant et ne vous enfuyez pas avec les fonds, ne soyez pas méchant et ne facturez pas des frais élevés. Nous voulons baiser les banquiers fiduciaires, pas nous baiser les uns les autres (les utilisateurs de bitcoins).

## Plate-forme de démonstration

La démo se trouve à l'adresse [https://legend.lnbits.com](https://legend.lnbits.com). Elle est entièrement fonctionnelle et peut être utilisée pour découvrir le Lightning Network et les fonctionnalités de LNbits et de LNURL en général. Bien que nous ne puissions pas vous empêcher de l'utiliser, nous aimerions vous demander de ne pas l'utiliser pour votre installation de production. Non seulement nous travaillons souvent sur les serveurs pour tester de nouvelles fonctionnalités, mais nous aimerions également vous encourager à gérer votre propre nœud et LNbits de manière souveraine. Si vous pensez que gérer un nœud est trop demander pour le moment, vous pouvez connecter LNbits à un service de financement dans le nuage comme Opennode, Luna ou Votage ou au Lightning Tipbot sur Telegram pour n'en citer que quelques uns.

## Dépliant LNbits

Vous souhaitez donner quelques informations de base à un commerçant ou à un ami bâtisseur ? Nous sommes très heureux d'annoncer notre premier flyer à l'usage de tous. Le format est celui d'un flyer typique avec 6 pages (2 plis) et une largeur de 3508 et une hauteur de 2480px.

LNbits pour les commerçants : [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbits pour les constructeurs : [EN](/assets/lnbits-builders-fr.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

## Quelques notions de base

LNbits fonctionne sur la base du protocole LNURL, ce qui signifie que les demandes sont valables sous deux formes : soit en tant que lien https://clearnet (aucun certificat auto-signé n'est autorisé), soit en tant que lien http://v2/v3 onion. Pour offrir des services LNbits tels que les codes QR LNURLp/w ou les cartes NFC, qui peuvent être utilisés dans la nature, vous devrez ouvrir LNbits à clearnet (https).

Avant d'installer LNbits, assurez-vous d'avoir lu et compris les guides généraux suivants sur ce qu'est LNbits et sur les possibilités qu'il vous offre.


- [Guide du LND](https://docs.lightning.engineering/) | Installation du LND
- [Exemple de configuration LND](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | Paramètres LND
- [Guide CLN](https://docs.corelightning.org/docs/installation) | Installation de CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Diriger une tour de guet](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | Très important !

Des guides plus détaillés sur l'utilisation des LNbits dans des scénarios d'utilisation spécifiques sont disponibles ici :


- [Premiers pas avec LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Guide de la sous-paquette
- [ToDos pour votre sécurité avec LNbits](https://youtu.be/i5FQf96e6zg) | Vidéo Youtube
- [Banques privées sur le Lightning Network](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | Guide de la sous-pile
- [Portefeuilles de garde pour vos amis et votre famille](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Guide Substack
- [LNbits pour un petit restaurant / hôtel](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Guide Substack
- [Utilisation du copilote LNbits Streamer](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Guide de l'utilisation de Substack
- [Démarrez votre marché NOSTR avec LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Guide de la sous-pile
- [Utilisation des LNbits dans le cadre de projets scolaires ou de festivals](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Guide d'accompagnement

## Installer LNbits

### Guide d'installation de base

LNbits peut être installé sur n'importe quelle machine sous Linux. Il n'a pas besoin d'une machine ou d'un serveur puissant, mais seulement de suffisamment de mémoire RAM et d'un peu d'espace disque pour la base de données. Il peut être exécuté séparément d'un nœud BTC/LN (PC local ou VPS distant) ou ensemble sur la même machine que le nœud ou déjà installé dans une machine logicielle de nœud groupé.

Vous pouvez choisir entre les gestionnaires de paquets les plus courants comme poetry et nix. Par défaut, LNbits utilise SQLite comme base de données. Vous pouvez également utiliser PostgreSQL qui est recommandé pour les applications à forte charge. [Voici un guide d'installation de base utilisant poetry ou nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).

Pour les novices, vous trouverez des guides détaillés, étape par étape, pour faire fonctionner vos LNbits dans des environnements spécifiques :


- [LNbits sur clearnet](https://ereignishorizont.xyz/lnbits-server/en/) par Axel
- [LNbits sur un VPS](https://github.com/TrezorHannes/vps-lnbits) par Hannes
- [LNbits on cloudflare](https://www.nodeacademy.org/lnbits) par Leo

Vous pouvez également trouver une vidéo sur [l'installation dockerisée sur un VPS avec PostgreSQ, LightningTipBot comme source de financement en utilisant nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).

[Plus de scénarios d'installation ici](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).

Pour les nœuds logiciels groupés, veuillez vous référer à leur documentation spécifique sur les LNbits : [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

### LNbits SaaS

Si vous n'êtes pas intéressés par les aspects techniques et que vous ne souhaitez pas héberger vous-même votre source de financement ou vos LNbits, il existe une [version LNbits SaaS](https://saas.lnbits.com) (Software-as-a-service) que vous pouvez utiliser. C'est en fait comme LNbits dans un nuage mais vous pouvez définir la source de financement (par exemple votre Node, un portefeuille LNbits, le LNtipbot, le faux portefeuille, etc) et les variables d'environnement vous-même - ce qui n'est généralement pas le cas sur d'autres solutions de nuage.

[Voici un guide détaillé sur l'utilisation de LNbits SaaS pour des cas d'utilisation spécifiques](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).

### Sources de financement

LNbits n'est pas un logiciel de gestion de nœuds, mais un système de comptabilité axé sur les LN, qui s'ajoute à une source de financement LND ou CLN. Après la première installation, vous pouvez visiter votre LNbits à l'adresse http://localhost:5000/.

Pour modifier la source de financement, allez sur l'URL de votre super-utilisateur et sélectionnez une source de financement dans "Manage Server" ou éditez le fichier .env en modifiant `LNBITS_BACKEND_WALLET_CLASS` en fonction de la source dont vous avez besoin si vous avez mis `adminUI=TRUE` dans le fichier `.env`.

Vous trouverez le fichier .env dans votre dossier lnbits/ ou lnbits/apps/data en étendant la commande pour lister les fichiers de votre répertoire par `ls -a`.

Il se peut que vous deviez également installer d'autres paquets ou effectuer d'autres étapes d'installation, en sélectionnant la source de financement souhaitée. Après un redémarrage, votre nouvelle configuration sera active.

Quelles sources de financement puis-je utiliser pour LNbits ?

LNbits peut fonctionner avec de nombreuses sources de financement du réseau Lightning. Il prend actuellement en charge CoreLightning, LND, LNbits, LNPay, OpenNode, et d'autres sont ajoutés régulièrement.

Il est important de choisir une source qui dispose d'une bonne liquidité et de bons pairs connectés. Si vous utilisez les LNbits pour des services publics, les paiements de vos utilisateurs ne peuvent que circuler dans les deux sens.

Un portefeuille backend (source de financement) peut être configuré en utilisant les variables d'environnement LNbits suivantes dans le fichier `.env` ou dans votre compte superutilisateur dans la section Manage-Server.

Si vous souhaitez utiliser la version .env, vous trouverez les paramètres ici :

#### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS` : **CoreLightningWallet**
  - `CORELIGHTNING_RPC` : /file/path/lightning-rpc
- Etincelle (c-lightning)
  - `LNBITS_BACKEND_WALLET_CLASS` : **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - `SPARK_TOKEN` : secret_access_key

#### Daemon du réseau Lightning


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS` : **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT` : /file/path/tls.cert
  - `LND_REST_MACAROON` : /file/path/admin.macaroon ou Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED` : eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS` : **LndWallet**
  - `LND_GRPC_ENDPOINT` : ip_address
  - `LND_GRPC_PORT` : port
  - `LND_GRPC_CERT` : /file/path/tls.cert
  - `LND_GRPC_MACAROON` : /file/path/admin.macaroon ou Bech64/Hex

Vous pouvez également utiliser un macaron crypté AES (plus d'informations) à la place en utilisant


  - `LND_GRPC_MACAROON_ENCRYPTED` : eNcRyPtEdMaCaRoOn

Pour chiffrer votre macaron, lancez `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.

#### LNbits (une autre instance de LNbits)


- Instance LNbits hébergée sur un serveur en nuage ou sur votre propre serveur domestique
  - `LNBITS_BACKEND_WALLET_CLASS` : **LNbitsWallet**
  - `LNBITS_ENDPOINT` : https://lnbits.mydomain.com
  - `LNBITS_KEY` : my-lnbits-AdminKey
- LNbits Legend Demo Server ( !! N'utilisez PAS celui-ci à des fins de production / commerciales, uniquement pour des tests ! !!)
  - `LNBITS_BACKEND_WALLET_CLASS` : **LNbitsWallet**
  - `LNBITS_ENDPOINT` : https://legend.lnbits.com
  - `LNBITS_KEY` : legend-lnbits-AdminKey

#### Lightning TipBot

Pour connecter votre [Lightning Tipbot](https://t.me/LightningTipBot) à partir de Telegram, vous devez définir les paramètres suivants :


  - `LNBITS_BACKEND_WALLET_CLASS` : **LnTipsWallet**
  - `LNBITS_ENDPOINT` : https://ln.tips
  - `LNBITS_KEY` : Pour obtenir la clé, vous devrez exécuter /api dans un chat privé avec le LightningTipbot sur Telegram une fois.

Voir aussi ce tutoriel pour installer [LNbits avec LightningTipBot via vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)

#### IBEX HUB

Enregistrez-vous [ici](https://ibexpay.ibexmercado.com/onboard) puis obtenez vos clés/tokens à partir de là, le point d'arrivée est https://ibexpay-api.ibexmercado.com.

Pour plus d'informations, voir [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

#### LNPay

Pour que l'écoute des factures fonctionne, vous devez avoir une URL accessible au public dans votre LNbits et mettre en place un [LNPay webhook](https://dashboard.lnpay.co/webhook/) pointant vers `<votre hôte LNbits>/wallet/webhook` avec l'événement "Wallet Receive" et aucun secret donné. Le paramètre `https://mylnbits/wallet/webhook` sera l'url du point de terminaison qui sera notifié de tout paiement.


  - `LNBITS_BACKEND_WALLET_CLASS` : **LNPayWallet**
  - `LNPAY_API_ENDPOINT` : https://api.lnpay.co/v1/
  - `LNPAY_API_KEY` : sak_apiKey
  - `LNPAY_WALLET_KEY` : waka_apiKey

#### OpenNode

Pour que la facture fonctionne, vous devez avoir une URL accessible au public dans votre LNbits. Le paramétrage du webhook est facultatif.


  - `LNBITS_BACKEND_WALLET_CLASS` : **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT` : https://api.opennode.com/
  - `OPENNODE_KEY` : opennodeAdminApiKey

#### Alby

Alby est une extension de navigateur avec des fonctionnalités de portefeuille LN et un compte LNDHUB qui peut être utilisé comme source de financement pour les LNbits. [Plus de détails ici](https://getalby.com/).

Pour que la facture fonctionne, vous devez avoir une URL accessible au public dans votre LNbits. Aucun paramétrage manuel du webhook n'est nécessaire. Vous pouvez générer un jeton d'accès Alby ici : https://getalby.com/developer/access_tokens/new


- `LNBITS_BACKEND_WALLET_CLASS` : AlbyWallet
- `ALBY_API_ENDPOINT` : https://api.getalby.com/
- `ALBY_ACCESS_TOKEN` : AlbyAccessToken

### Guides supplémentaires / de dépannage

Voici quelques instructions supplémentaires au cas où vous en auriez besoin. Cliquez sur la flèche pour développer la description.

#### The Killswitch 🚨

Il y a eu tellement de bogues dangereux ces derniers temps, non seulement dans l'ensemble de l'espace mais aussi dans LNbits, que nous avons décidé de faire quelque chose à ce sujet. Vous pouvez désormais choisir de recevoir des avertissements et/ou de prendre des mesures directes lorsqu'une vulnérabilité ou un bogue susceptible d'entraîner une perte de fonds se produit à nouveau.

![killswitchn](assets/lnbits-killswitch.webp)

Si vous passez à void-wallet, tous les types d'utilisateurs de l'instance verront une bannière jaune à l'endroit où se trouve normalement l'avis "LNbits is in Beta" à côté de la zone thème/langue à droite - et c'est l'indice le plus évident qu'il s'est passé quelque chose. Jetez un oeil à votre nouvel onglet serveur surligné en vert dans la partie gauche de la fenêtre.

Comment cela fonctionne-t-il ? Lorsque le killswitch est activé, un dépôt github secret accessible uniquement à l'équipe centrale de LNbits sera vérifié à un intervalle de X minutes (qui peut être spécifié). Si un bug vulnérable est publié dans ce dépôt, il sert de signal qui déclenche le killswitch sur toutes les installations qui se sont abonnées et qui transforment votre instance LNbits pour utiliser le void wallet. Si les nuages se sont dissipés et que vous avez installé la mise à jour de sécurité, vous pouvez régler votre source de financement sur votre nœud, votre porte-monnaie ou tout ce que vous utilisez à nouveau, également via la section Gérer le serveur. Ce wiki contient une section sur le changement de source de financement si vous ne savez pas quoi configurer.

#### Différence entre administrateur et superutilisateur

L'interface d'administration de LNbits vous permet de modifier les paramètres de LNbits via le frontend de LNbits. Elle est désactivée par défaut et la première fois que vous définissez la variable d'environnement `LNBITS_ADMIN_UI=true` dans le fichier `.env`, les paramètres sont initialisés et seront utilisés. A partir de là, ce sont les paramètres de la base de données qui sont utilisés à la place de ceux du fichier .env.

#### Super utilisateur

Avec l'interface d'administration, nous avons introduit le super utilisateur qui a accès au serveur et peut donc modifier des paramètres qui pourraient faire planter le serveur ou le rendre insensible via le frontend et l'API, comme par exemple changer la source de financement. Le super utilisateur est uniquement stocké dans la table des paramètres de la base de données. Après la "réinitialisation des paramètres par défaut" et le redémarrage, un nouveau super-utilisateur est créé. Nous avons également ajouté un décorateur pour les routes de l'API afin de vérifier l'existence d'un super utilisateur. Son ID n'est jamais envoyé via l'API et le frontend et ne reçoit qu'un bool (oui/non) si vous êtes un super utilisateur ou non.

Seul le super utilisateur est autorisé à transférer des satoshis vers différents portefeuilles via la section "Top Up".

Vous pouvez également envoyer le super utilisateur via un webhook à un autre service lorsqu'il est créé. Plus d'informations ici https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`

Dans le frontend, vous trouverez également la possibilité de changer l'image de la boutique qui est affichée sur la page "créer un portefeuille" en ouvrant la section Gérer le serveur et en choisissant Thème -> Logo personnalisé.

#### Utilisateurs administratifs

Variable d'environnement : `LNBITS_ADMIN_USERS`, liste d'identifiants d'utilisateurs séparés par des virgules. Les utilisateurs Admin peuvent changer les paramètres dans l'interface d'administration - à l'exception des paramètres de source de financement, car cela nécessiterait un redémarrage du serveur et pourrait potentiellement rendre le serveur inaccessible. Ils ont également accès à toutes les extensions qui leur sont dédiées dans `LNBITS_ADMIN_EXTENSIONS`.

#### Utilisateurs autorisés

Variable d'environnement : `LNBITS_ALLOWED_USERS`, liste d'ID d'utilisateurs séparés par des virgules. En définissant ces utilisateurs, LNbits ne sera plus utilisable par le public. Seuls les utilisateurs définis et les administrateurs peuvent alors accéder au frontend de LNbits.

##### Mise à jour des LNbits

Une mise à jour normale de votre instance locale de LNbits se fait simplement en copiant-collant les commandes CLI suivantes :

```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```

Si vous utilisez Raspiblitz ou MyNode, vous pouvez également avoir besoin d'un fichier

```
sudo systemctl restart lnbits
```

à la fin, parce qu'il utilise LNbits comme un service.

Sur Umbrel/Citadel, les commandes seraient les suivantes

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

##### Migration de SQLite vers PostgreSQL

Si LNbits est déjà installé et fonctionne sur une base de données SQLite, nous vous recommandons vivement de migrer vers postgres si vous envisagez de faire fonctionner LNbits à grande échelle.

Il y a un script inclus qui peut faire la migration facilement. Vous devez avoir Postgres déjà installé et il doit y avoir un mot de passe pour l'utilisateur (voir le guide d'installation de Postgres ci-dessus). De plus, votre instance LNbits doit s'exécuter une fois sur Postgres pour implémenter le schéma de la base de données avant que la migration ne puisse fonctionner :

```
# STOP LNbits
# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit
# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Avec un peu de chance, tout fonctionne et est migré... Lancez à nouveau LNbits et vérifiez que tout fonctionne correctement.

##### Sauvegarde et restauration de la base de données

Veuillez consulter [ce guide très détaillé sur la procédure de sauvegarde et de restauration](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).

##### Le financement de mon portefeuille LNbits à partir de mon nœud ne fonctionne pas

Si vous souhaitez envoyer des satellites à partir du même nœud que celui qui est la source de financement de vos LNbits, vous devrez modifier le fichier lnd.conf.

Les paramètres à inclure sont les suivants : `allow-circular-route=1`

Veuillez le faire dans la section Application options de votre lnd.conf. Dans le cas contraire, le démarrage du LND pourrait échouer sur certains nœuds du bundle.

NOTE : Il est recommandé d'utiliser la nouvelle extension adminUI avec l'option "TopUp" pour ajouter des fonds à un compte LNbits.

##### Erreur 426

J'ai obtenu l'erreur suivante : "lnurl needs to be delivered over publically accessible https domain or tor. 426 upgrade required"</summary>

Cette erreur est généralement due au fait que votre LNbits derrière un tunnel ngnix ne transmet pas correctement l'adresse LNURL. Arrêtez votre LNbits et éditez le fichier .env en ajoutant cette ligne :

`FORWARDED_ALLOW_IPS=*`

De plus, si vous utilisez une configuration ngnix, assurez-vous d'avoir ces en-têtes dans la configuration ngnix :

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

##### Erreur de réseau

J'ai obtenu "https error", "network error" ou autres lorsque j'ai scanné un QR</summary>

Mauvaise nouvelle, il s'agit d'une erreur de routage qui peut avoir de nombreuses raisons. Vérifiez d'abord le LNURL du QR avec le [Lightning Decoder](https://lightningdecoder.com/) si vous y trouvez quelque chose d'étrange. Essayons quelques-uns des problèmes les plus courants et leurs solutions.

LNbits fonctionne uniquement via Tor, vous ne pouvez pas l'ouvrir sur un domaine public comme lnbits.yourdomain.com


- Étant donné que vous voulez que votre configuration reste ainsi, ouvrez votre portefeuille LNbits en utilisant l'URI .onion et créez-le à nouveau. De cette manière, le QR est généré pour être accessible via cette URI .onion, donc via tor uniquement. Ne générez pas cette QR à partir d'une URI .local, car elle ne sera pas accessible via l'internet, mais uniquement à partir de votre réseau local domestique.
- Ouvrez l'application du portefeuille LN que vous avez utilisée pour scanner la QR et cette fois-ci en utilisant tor (voir les paramètres de l'application du portefeuille). Si l'application ne propose pas tor, vous pouvez utiliser Orbot (Android) à la place. Voir la section d'installation pour des instructions détaillées sur la façon d'ouvrir vos LNbits pour clearnet/https.

##### Empêcher les autres de générer des portefeuilles sur mes LNbits

Lorsque vous gérez vos LNbits dans Clearnet, tout le monde peut générer un portefeuille. Puisque les fonds de votre nœud sont liés à ces portefeuilles, vous voudrez peut-être empêcher cela. Il y a deux façons de le faire :

Configurez les utilisateurs autorisés et les extensions dans le fichier `.env` ([voir l'exemple d'env ici](https://github.com/lnbits/lnbits/blob/main/.env.example)). Cela ne fonctionne que si vous utilisez le paramètre `adminUI=FALSE` dans le fichier .env, sinon vous devez le faire dans la section Gérer le serveur -> Utilisateurs -> Utilisateurs autorisés. Tous les autres ne seront pas autorisés par la suite.

##### Personnaliser le délai d'expiration de la facture

Vous pouvez désormais générer des factures avec une date d'expiration personnalisée. Compatible avec les backends : LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet jusqu'à présent !

Vous pouvez définir `LIGHTNING_INVOICE_EXPIRY` dans votre fichier .env ou utiliser l'AdminUI pour changer la valeur par défaut pour toutes les factures. Il y a aussi un nouveau champ dans le endpoint /api/v1/payments où vous pouvez définir l'expiration dans les données JSON.

### Wallet-URL supprimé

#### Portefeuille sur le serveur de démonstration legend.lnbits

Sauvegardez toujours une copie de votre wallet-URL, Export2phone-QR ou LNDhub pour vos propres portefeuilles dans un endroit sûr. LNbits ne peut pas vous aider à les récupérer en cas de perte.

#### Portefeuille sur votre propre source/noyau de financement

Sauvegardez toujours une copie de votre wallet-URL, Export2phone-QR ou LNDhub pour vos propres portefeuilles dans un endroit sûr. Vous pouvez trouver tous les utilisateurs de LNbits et les identifiants de portefeuilles dans votre extension de gestion des utilisateurs de LNbits ou dans votre base de données sqlite. Pour éditer ou lire la base de données LNbits, allez dans le dossier LNbits /data et cherchez le fichier appelé sqlite.db. Vous pouvez l'ouvrir et le modifier avec Excel ou avec un éditeur SQL dédié comme [SQLite browser](https://sqlitebrowser.org/).

Vous pouvez également vidanger les portefeuilles via cli et visualiser tous les portefeuilles de votre base de données.

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

Le résultat ressemblera à ceci

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

et vous voulez mettre ces valeurs dans une url comme ceci

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

Vous remplacez f8a43fc363ea428db5c53b3559935f1f par la valeur qui précède le nom (dans notre exemple f8a43fc363ea428db5c53b3559935f1f) et 1280ff5910a9c485a782a2376f338b6c est votre utilisateur et doit devenir la valeur affichée après le nom. Pour quitter sqlite3, tapez

```
.quit
```

##### LNURL pour une adresse éclair et vice versa

Essayez ce [codeur](https://lnurl-codec.netlify.app/) de fiatjaf ou [celui-ci](https://lightningdecoder.com/). Pour payer ou vérifier un LNURLp, vous pouvez également utiliser [LNurlpay](https://wwww.lnurlpay.com/). Il doit être indiqué HTTPS et non HTTP.

##### Configurer un commentaire que les gens voient lorsqu'ils paient à mon LNURLp QR

Lorsque vous créez un LNURL-p, la zone de commentaire n'est pas remplie par défaut. Cela signifie que les commentaires ne peuvent pas être joints aux paiements.

Afin d'autoriser les commentaires, ajoutez la longueur des caractères de la boîte, de 1 à 250. Une fois que vous aurez ajouté un nombre, la boîte de commentaires s'affichera lors du processus de paiement. Vous pouvez également modifier une LNURL-p déjà créée et ajouter ce nombre.

![lnbits comments](assets/lnbits-comments.webp)

##### Dépôt de BTC onchain sur LNbits

Il y a deux façons d'échanger des sats de BTC onchain en LN BTC (resp. en LNbits).

###### Par l'intermédiaire d'un service d'échange externe.

Les autres utilisateurs qui n'ont pas accès à votre LNb its peuvent utiliser un service d'échange comme [Boltz](https://boltz.exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) ou [ZigZag](https://zigzag.io/). Ceci est utile si vous ne fournissez que des factures LNURL/LN à partir de votre instance LNbits, mais qu'un payeur n'a que des sats onchain, il devra donc d'abord échanger ces sats de son côté. La procédure est simple : l'utilisateur envoie des btc onchain au service d'échange et fournit la facture LNURL / LN de LNbits comme destination de l'échange.

###### Utilisation de l'extension Onchain et Boltz LNbits.

Gardez à l'esprit qu'il s'agit d'un portefeuille séparé, et non de celui des btc LN qui est représenté par LNbits comme "votre portefeuille" sur votre source de financement LN. Ce portefeuille onchain peut également être utilisé pour échanger des LN btc contre (par exemple, votre hardwarewallet) en utilisant l'extension LNbits Boltz ou Deezy. Si vous gérez une boutique en ligne qui est liée à votre LNbits pour les paiements en LN, il est très pratique de drainer régulièrement tous les sats de LN vers onchain. Cela permet d'avoir plus d'espace dans vos canaux LN pour pouvoir recevoir de nouveaux sats frais.

Procédure pour ceux qui n'ont pas de portefeuille matériel bitcoin :


- Utilisez Electrum ou Sparrow wallet pour créer un nouveau portefeuille onchain et enregistrez la graine de sauvegarde dans un endroit sûr.
- Allez dans les informations du portefeuille et copiez le fichier xpub.
- Allez sur LNbits - Onchain extension et créez un nouveau watch-only wallet avec ce xpub.
- Allez sur LNbits - Tipjar extension et créez un nouveau Tipjar. Sélectionnez également l'option onchain en plus du portefeuille LN.
- Optionnel - Allez sur LNbits - SatsPay extension et créez une nouvelle charge pour onchain btc. Vous pouvez choisir entre onchain et LN ou les deux. Une facture sera alors créée et pourra être partagée.
- Optionnel - Si vous utilisez vos LNbits liés à une page Wordpress + Woocommerce, une fois que vous avez créé/lié un porte-monnaie de montre uniquement à votre porte-monnaie de boutique en btc LN, le client aura les deux options de paiement sur le même écran.

Lorsque vous recevez un paiement dans LNbits, le journal des transactions n'affiche qu'un type de reprise de la transaction.

![lnbits payment details](assets/lnbits-payment-details.webp)

Dans l'aperçu de votre transaction, vous trouverez une petite flèche verte pour les fonds reçus et une flèche rouge pour les fonds envoyés.

Si vous cliquez sur ces flèches, une fenêtre contextuelle détaillée affiche les messages joints ainsi que le nom de l'expéditeur, le cas échéant.

Configurer un nom pour qu'il apparaisse dans les paiements, dans LNbits ce n'est actuellement pas possible de le faire - mais de le recevoir. Cela n'est possible que si le portefeuille LN de l'expéditeur prend en charge [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) comme [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).

Vous verrez alors un alias/pseudonyme dans la section des détails de vos transactions LNbits (cliquez sur les flèches). Notez que vous pouvez donner n'importe quel nom et qu'il peut ne pas être lié au nom de l'expéditeur réel si vous en recevez un.

![lnbits namedesc](assets/lnbits-namedesc.webp)

Pour importer votre compte LNbits dans une application de portefeuille, ouvrez votre LNbits avec le compte / portefeuille que vous souhaitez utiliser, allez dans "gérer les extensions" et activez l'extension LNDHUB. Ouvrez l'extension LNDHUB, choisissez le portefeuille que vous souhaitez utiliser et scannez le QR "admin" ou "invoice only", en fonction du niveau de sécurité que vous souhaitez pour ce portefeuille.

Vous pouvez utiliser [Zeus](https://zeusln.app/) ou [Bluewallet](https://bluewallet.io/) en tant qu'applications de portefeuille pour un compte lndhub, BW prenant en charge plusieurs portefeuilles de ce type.

Lors de cette opération, nous vous recommandons également de définir l'URI du réseau LN comme étant celui de votre propre nœud. Si votre instance LNbits est uniquement Tor, vous devez également utiliser ces applications avec Tor activé. Dans ce cas également, vous devez ouvrir la page LNbits via votre adresse Tor .onion.

Si vous avez une erreur "unsupported hash type" lorsque vous utilisez un ypub dans l'extension On-chain, vérifiez si votre instance de LNbits utilise python 3.10, il pourrait être affecté par [ce problème](https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python). Editez le fichier openssl.cnf comme décrit dans la réponse de stackoverflow et redémarrez votre LNbits.

### Outillage et construction avec LNbits

LNbits dispose de toutes sortes d'[API ouvertes](https://legend.lnbits.com/docs) et d'outils permettant de programmer et de se connecter à un grand nombre d'appareils différents pour un grand nombre de cas d'utilisation.

Si vous êtes novice en matière de construction, commencez par cette [présentation MakerBits](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) de Ben Arc sur la construction de gadgets basés sur les LNbits.

#### IMPORTANT :


- LNbits fonctionne sur la base du protocole LNURL dont les requêtes sont valables sous deux formes : soit en tant que https://clearnet link (pas de certificats auto-signés autorisés) soit en tant que http://v2/v3 onion link. Pour offrir des services LNbits tels que les codes QR LNURLp/w ou les cartes NFC, qui peuvent être utilisés dans la nature, vous devrez ouvrir LNbits à clearnet (https).
- N'utilisez que des câbles DATA pour alimenter votre esp32. Tous les câbles ne supportent pas les données en plus de l'alimentation de l'esp. Vous ne seriez pas le premier si le câble fourni avec l'esp est un câble d'alimentation uniquement
- Veillez à ne pas utiliser un hub USB avec d'autres appareils connectés. Cela peut entraîner des effets bizarres difficiles à déboguer (par exemple, le fait de ne pas démarrer ou de ne pas s'arrêter).
- Pour réaliser des projets esp avec un MacOS, vous aurez besoin d'un pilote de pont UART. Si vous avez des problèmes avec le pilote sur les systèmes Mac ou Linux, vous pouvez les trouver ici ou, si un écran TTGO est impliqué, celui-ci. Si vous êtes sous Windows et que vous avez des problèmes de connexion, assurez-vous de télécharger l'ANCIENNE version 11.1.0 car la plus récente ne fonctionne pas ! Vous pouvez également trouver un terminal série ici pour vérifier votre connexion - réglé sur une vitesse de transmission de 115200.
- Bien qu'il soit beaucoup plus confortable d'utiliser Platform.io (par exemple, les dépendances sont installées automatiquement), nous recommandons l'utilisation d'Arduino à tous ceux qui débutent dans la construction.
- TT-Go Display S3 : La couleur de la languette du film de protection de l'écran vous indique quel contrôleur exactement (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ...) a été utilisé pour le construire. Gardez-le pour pouvoir déboguer si vous vous programmez et que l'écran n'affiche pas les graphiques correctement, par exemple des couleurs erronées, des images en miroir ou des pixels parasites sur les bords. Si jamais vous devez le faire, il existe un guide épique sur l'adaptation aux différents écrans
- Utilisez toujours la minuscule lnurl239xx au lieu de LNURLl239xx
- L'ajout de lightning:lnurl1234xyz créera un QR qui demandera d'ouvrir le portefeuille de l'utilisateur pour cette facture lors du scan (dernière installation de l'application lightning sur iOS, réglage sur Android)
- Si vous flashez un esp32 via le web, cela ne fonctionnera qu'avec ces navigateurs (TL:DR Chrome, Edge & Opera).
- Veuillez noter cette référence de PIN-OUT pour l'esp
- Lorsque vous utilisez des logiciels FOSS ou des guides FOS, veuillez toujours indiquer le nom de l'auteur. Tout le monde aime voir son bébé grandir et cela initie également une chaîne de construction qui est tout à fait impressionnante à regarder :)

Venez sur le [Makerbits Telegram Group](https://t.me/makerbits) si vous avez besoin d'aide pour un projet - nous sommes là pour vous !

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

Voici quelques catégories de projets que vous pouvez réaliser avec LNbits :


- [Nostr Signing Device](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Lampe Zap Nostr](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [Distributeur automatique](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora et le maillage](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [AIDES ET RESSOURCES](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Plus d'exemples de projets "Powered by LNbits" ici](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Cas d'utilisation des LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)
