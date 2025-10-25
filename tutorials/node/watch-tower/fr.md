---
name: Lightning Watchtower
description: Comprendre et utiliser une Watchtower sur son nœud Lightning
---
![cover](assets/cover.webp)

## Comment fonctionnent les Watchtowers ?

Élément essentiel de l’écosystème du Lightning Network, les _Watchtowers_ offrent un degré de protection supplémentaire aux canaux Lightning des utilisateurs. Leur rôle principal est de surveiller l’état des canaux et d’intervenir si l’une des parties du canal tente de frauder l’autre.

Comment une Watchtower peut-elle déterminer si un canal a été compromis ? Elle reçoit du client (l’une des parties du canal) les informations nécessaires pour identifier correctement et traiter toute violation. Ces informations incluent les détails de la transaction la plus récente, l’état actuel du canal, ainsi que les éléments requis pour créer des transactions de pénalité. Avant de transmettre ces données à la Watchtower, le client peut les chiffrer afin de préserver sa confidentialité. Ainsi, même si la Watchtower reçoit les données, elle ne pourra pas les déchiffrer tant qu’une violation n’aura pas réellement eu lieu. Ce mécanisme de chiffrement protège la vie privée du client et empêche la Watchtower d’accéder à des informations sensibles sans autorisation.

Dans ce tutoriel, nous verrons 3 manières d’utiliser une **Watchtower** :
- d’abord la méthode classique et brute via LND,
- puis une autre approche avec Eye of Satoshi,
- et enfin, en dernière partie, la configuration simplifiée d’une Watchtower sur votre nœud Lightning hébergé avec Umbrel.

## 1 - Configurer une Watchtower ou un client via LND

*Ce tutoriel est extrait [de la documentation officielle de LND](https://github.com/lightningnetwork/lnd/blob/master/docs/watchtower.md). Certaines modifications ont pu être apportées par rapport à la version originale.*

Depuis la v0.7.0, `lnd` prend en charge l’exécution d’une watchtower altruiste privée en tant que sous-système entièrement intégré à `lnd`. Les watchtowers constituent une seconde ligne de défense contre les scénarios de violation malveillante ou accidentelle lorsque le nœud du client est hors ligne ou incapable de répondre au moment de la violation, offrant ainsi un degré de sécurité accru pour les fonds des canaux.

À la différence d’une _reward watchtower_, qui exige une part des fonds du canal en contrepartie de son service, une _altruist watchtower_ restitue l’intégralité des fonds de la victime (moins les frais on-chain) sans prélever de commission. Les reward watchtowers seront activées dans une version ultérieure ; elles sont encore en phase de tests et d’améliorations.

Par ailleurs, `lnd` peut désormais être configuré pour fonctionner comme _client de watchtower_, en sauvegardant des transactions chiffrées de remédiation de violation (dites "transactions de justice") auprès d’autres watchtowers altruistes. La watchtower stocke des blobs chiffrés de taille fixe et ne peut déchiffrer et publier la transaction de justice qu’après que la partie fautive a diffusé un état de commitment révoqué. Les communications client ↔ watchtower sont chiffrées et authentifiées au moyen de paires de clés éphémères, ce qui limite la capacité de suivi de la watchtower sur ses clients via des identifiants de long terme.

Notez que nous avons choisi de déployer dans cette version un ensemble restreint de fonctionnalités fournissant déjà une sécurité significative aux utilisateurs de `lnd`. De nombreuses autres fonctions liées aux watchtowers sont proches d’aboutir ou bien avancées ; nous continuerons de les livrer au fil des tests et dès qu’elles seront jugées sûres.

_Remarque : pour l’instant, les watchtowers ne sauvegardent que les sorties `to_local` et `to_remote` des commitments révoqués ; la sauvegarde des sorties HTLC sera déployée dans une version ultérieure, le protocole pouvant être étendu pour inclure les données de signature supplémentaires dans les blobs chiffrés._

### Configurer une watchtower

Pour mettre en place une watchtower, les utilisateurs en ligne de commande doivent compiler le sous-serveur optionnel `watchtowerrpc`, qui permet d’interagir avec la watchtower via gRPC ou `lncli`. Les binaires publiés incluent par défaut le sous-serveur `watchtowerrpc`.

La configuration minimale pour activer la watchtower est `watchtower.active=1`.

Vous pouvez récupérer les informations de configuration de votre watchtower avec `lncli tower info` :

```shell
$  lncli tower info
{
        "pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
        "listeners": [
                "[::]:9911"
        ],
        "uris": [
        ],
}
```

L’ensemble complet des options de configuration de la watchtower est disponible via `lnd -h` :

```shell
$  lnd -h
...
watchtower:
      --watchtower.active                                     If the watchtower should be active or not
      --watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
      --watchtower.listen=                                    Add interfaces/ports to listen for peer connections
      --watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
      --watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
      --watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```

#### Interfaces d’écoute

Par défaut, la watchtower écoute sur `:9911`, ce qui correspond au port `9911` sur toutes les interfaces disponibles. Les utilisateurs peuvent définir leurs propres interfaces d’écoute via l’option `--watchtower.listen=`. Vous pouvez vérifier votre configuration dans le champ `"listeners"` de `lncli tower info`. En cas de difficulté à vous connecter à votre watchtower, assurez-vous que le `<port>` est ouvert ou que votre proxy est correctement configuré vers une interface d’écoute active.

#### Adresses IP externes

Les utilisateurs peuvent également spécifier l’adresse (ou les adresses) IP externe(s) de la watchtower avec `watchtower.externalip=`, ce qui expose les URI complètes de la watchtower (pubkey@hôte:port) via RPC ou `lncli tower info` :

```shell
$  lncli tower info
        ...
        "uris": [
                "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
        ]
```

Les URI de la watchtower peuvent être communiquées aux clients pour qu’ils s’y connectent et l’utilisent avec la commande suivante :

```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```

Si les clients de la watchtower doivent y accéder à distance, veillez à :
- Ouvrir le port 9911 (ou un port défini via `watchtower.listen`).
- Utiliser un proxy pour rediriger le trafic d’un port ouvert vers l’adresse d’écoute de la watchtower.

#### Services cachés Tor

Les watchtowers prennent en charge les services cachés Tor et peuvent en générer un automatiquement au démarrage avec les options suivantes :

```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```

L’adresse .onion apparaît ensuite dans le champ `"uris"` lors d’une requête `lncli tower info` :

```shell
$  lncli tower info
...
"uris": [
        "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```

_Remarque : la clé publique de la watchtower est distincte de la clé publique du nœud `lnd`. Pour l’instant, elle fait office de « liste blanche souple », car les clients doivent connaître la clé publique de la watchtower pour l’utiliser comme sauvegarde, en attendant des mécanismes de liste blanche plus avancés. Nous recommandons de NE PAS divulguer cette clé publique ouvertement, à moins d’être prêt à exposer votre watchtower à l’Internet entier._

#### Répertoire de la base de données de la watchtower

La base de données de la watchtower peut être déplacée à l’aide de l’option `watchtower.towerdir=`. Notez qu’un suffixe `/bitcoin/mainnet/watchtower.db` sera ajouté au chemin choisi afin d’isoler les bases de données selon les chaînes. Ainsi, définir `watchtower.towerdir=/path/to/towerdir` produira une base à `/path/to/towerdir/bitcoin/mainnet/watchtower.db`.

Sous Linux, par exemple, la base de données par défaut de la watchtower se trouve à :  
`/home/$USER/.lnd/data/watchtower/bitcoin/mainnet/watchtower.db`

### Configurer un client de watchtower

Pour configurer un client de watchtower, il vous faut deux éléments :

- Activer le client de watchtower avec l’option `--wtclient.active`.

```shell
$  lnd --wtclient.active
```

- L’URI d’une watchtower active.

```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```

Vous pouvez configurer plusieurs watchtowers de cette manière.

#### Taux de frais des transactions de justice

Les utilisateurs peuvent facultativement définir le taux de frais des transactions de justice via l’option `wtclient.sweep-fee-rate`, qui accepte des valeurs en sat/octet. La valeur par défaut est 10 sat/octet, mais il est possible de viser des taux plus élevés pour obtenir une priorité accrue lors des pics de frais. La modification de `sweep-fee-rate` s’applique à toutes les nouvelles mises à jour après redémarrage du démon.

#### Supervision

Avec la commande `lncli wtclient`, les utilisateurs peuvent désormais interagir directement avec le client de watchtower pour obtenir ou modifier des informations sur l’ensemble des watchtowers enregistrées.

Par exemple, avec `lncli wtclient tower`, vous pouvez connaître le nombre de sessions actuellement négociées avec la watchtower ajoutée ci-dessus et déterminer si elle est utilisée pour les sauvegardes grâce au champ `active_session_candidate`.

```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
	"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
	"addresses": [
		"1.2.3.4:9911"
	],
	"active_session_candidate": true,
	"num_sessions": 1,
	"sessions": []
}
```

Pour obtenir des informations sur les sessions de la watchtower, utilisez l’option `--include_sessions`.

```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
        "pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
        "addresses": [
                "1.2.3.4:9911"
        ],
        "active_session_candidate": true,
        "num_sessions": 1,
        "sessions": [
                {
                        "num_backups": 0,
                        "num_pending_backups": 0,
                        "max_backups": 1024,
                        "sweep_sat_per_vbyte": 10
                }
        ]
}
```

L’ensemble des options de configuration du client de watchtower est disponible via `lncli wtclient -h` :

```shell
$  lncli wtclient -h
NAME:
   lncli wtclient - Interact with the watchtower client.

USAGE:
   lncli wtclient command [command options] [arguments...]

COMMANDS:
     add     Register a watchtower to use for future sessions/backups.
     remove  Remove a watchtower to prevent its use for future sessions/backups.
     towers  Display information about all registered watchtowers.
     tower   Display information about a specific registered watchtower.
     stats   Display the session stats of the watchtower client.
     policy  Display the active watchtower client policy configuration.

OPTIONS:
   --help, -h  show help
```


## 2 - Installer votre propre Eye of Satoshi

*Ce tutoriel est en partie extrait d'un article du site [Summer of Bitcoin Blog](https://blog.summerofbitcoin.org/). Des modifications ont été apportées par rapport à la version originale.*

L’Eye of Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos)) est une watchtower Lightning non-dépositaire, conforme à [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Elle se compose de deux éléments principaux :

- **teos** : inclut une interface en ligne de commande (CLI) et les fonctionnalités serveur essentielles de la watchtower. Deux binaires — **teosd** et **teos-cli** — sont produits lors de la compilation de ce _crate_.

- **teos-common** : inclut des fonctionnalités partagées côté serveur et côté client (utile pour créer un client).

Pour exécuter la watchtower correctement, vous devez faire tourner **bitcoind** avant de lancer la watchtower avec la commande **teosd**. Avant d’exécuter ces deux commandes, vous devez configurer votre fichier **bitcoin.conf**. Voici les étapes à suivre :

- Installez Bitcoin Core depuis les sources ou téléchargez-le. Après le téléchargement, placez le fichier **bitcoin.conf** dans le répertoire utilisateur de Bitcoin Core. Consultez ce lien pour plus d’informations sur l’emplacement où placer le fichier, car cela dépend du système d’exploitation utilisé.

- Une fois l’emplacement identifié, ajoutez les options suivantes :

```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```

- **server** : pour les requêtes RPC

- **rpcuser** et **rpcpassword** : authentification des clients RPC auprès du serveur

- **regtest** : non requis, mais utile si vous prévoyez du développement.

Les valeurs de **rpcuser** et **rpcpassword** sont à choisir par vous-même. Elles doivent être écrites sans guillemets. Par exemple :

```shell
rpcuser=aniketh
rpcpassword=strongpassword
```

À présent, si vous lancez **bitcoind**, le nœud devrait démarrer.

- Pour la partie watchtower, vous devez d’abord installer **teos** depuis les sources. Suivez les instructions données dans ce lien.

- Après avoir installé **teos** avec succès sur votre système et exécuté les tests, vous pouvez passer à la dernière étape : configurer le fichier **teos.toml** dans le répertoire utilisateur de teos. Le fichier doit être placé dans un dossier nommé **.teos** (notez le point) sous votre répertoire personnel. Par exemple, **/home//.teos** sous Linux. Une fois l’emplacement trouvé, créez un fichier **teos.toml** et définissez ces options en cohérence avec les changements effectués sur **bitcoind** :

```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```

Notez qu’ici, le nom d’utilisateur et le mot de passe doivent être écrits **entre guillemets**. En reprenant l’exemple précédent :

```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```

Une fois cela fait, vous devriez être prêt à lancer la watchtower. Étant donné que nous tournons sur **regtest**, il est probable qu’aucun bloc n’ait été miné sur notre réseau de test Bitcoin lors de la première connexion de la watchtower (s’il y en a, quelque chose cloche). La watchtower construit un cache interne des 100 derniers blocs de **bitcoind** ; ainsi, lors du premier lancement, vous pourriez obtenir l’erreur suivante :

```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```

Comme nous utilisons **regtest**, nous pouvons miner des blocs en émettant une commande RPC, sans avoir à attendre le délai médian de 10 minutes que l’on observe sur d’autres réseaux (comme mainnet ou testnet). Consultez l’aide de **bitcoin-cli** pour savoir comment miner des blocs.

![Image](assets/fr/01.webp)

C’est tout : vous avez exécuté la watchtower avec succès. Félicitations. 🎉


## 3 - Configurer une Watchtower sur Umbrel

Sur Umbrel, se connecter à une Watchtower pour protéger votre nœud Lightning est extrêmement simple, car tout se fait via l’interface graphique. Après vous être connecté à distance à votre nœud, ouvrez l’application "**Lightning Node**".

![Image](assets/fr/02.webp)

Cliquez sur les trois petits points situés en haut à droite de l’interface, puis sélectionnez "**Advanced Settings**".  

![Image](assets/fr/03.webp)

Dans le menu "**Watchtower**", deux options sont disponibles :

- **Watchtower Service** : cette option permet d’exploiter une watchtower, c’est-à-dire un service surveillant les canaux d’autres nœuds afin de détecter toute tentative de fraude. En cas de violation, votre watchtower publie une transaction sur la blockchain pour permettre aux utilisateurs qui l’emploient de récupérer leurs fonds verrouillés. Une fois activée, l’URI de votre watchtower apparaît et peut être communiqué à d’autres nœuds pour qu’ils l’ajoutent à leur client watchtower ;

- **Watchtower Client** : cette option permet de se connecter à des watchtowers externes afin de protéger vos propres canaux. Une fois activée, vous pouvez ajouter des services de watchtower auxquels votre nœud transmettra les informations nécessaires sur ses canaux. Ces watchtowers surveilleront alors leur état et interviendront en cas de tentative de fraude.

La priorité pour vous est bien sûr d’activer le *Watchtower Client* afin de protéger votre nœud, mais je vous recommande également d’activer le *Watchtower Service* pour contribuer à la sécurité d’autres utilisateurs en retour.

![Image](assets/fr/04.webp)

Cliquez ensuite sur le bouton vert "**Save and Restart Node**". Votre LND redémarrera.  

Dans le même menu, vous trouverez ensuite l’URI de votre service Watchtower si vous l’avez activé. Vous pourrez surtout ajouter l’URI d’une Watchtower externe pour protéger vos canaux. Cliquez sur "**ADD**" pour confirmer.  

![Image](assets/fr/05.webp)

Il existe plusieurs Watchtowers disponibles en ligne. Par exemple, [LN+ et Voltage proposent une Watchtower altruiste](https://lightningnetwork.plus/watchtower) à laquelle vous pouvez vous connecter :

```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```

![Image](assets/fr/06.webp)

Une autre option consiste à échanger votre URI de Watchtower avec vos amis bitcoiners, afin que chacun protège le nœud de l’autre.

Je vous recommande également de configurer plusieurs Watchtowers pour réduire les risques en cas d’indisponibilité de l’une d’entre elles.

Enfin, vous pouvez ajuster le paramètre "**Watchtower Client Sweep Fee Rate**". Il définit le taux de frais maximum que vous êtes prêt à payer pour qu’une transaction de punition diffusée par la Watchtower soit incluse dans un bloc. Veillez à définir une valeur suffisamment élevée et adaptée aux montants verrouillés dans vos canaux.
