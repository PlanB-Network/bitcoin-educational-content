# Cours sur les Ordinals

*Ordinals* est un nouveau protocole construit sur Bitcoin qui apporte de nouvelles opportunités, de nouveaux risques et de belles promesses. 
C'est un protocole Open-Source qui peut changer beaucoup de choses sur Bitcoin. 
Pour ce faire je propose ci-dessous une base de cours la plus complète possible. Je ne pense pas être capable de rédiger la totalité de ce cours tout seul et propose à tous ceux qui sont intéressés par *Ordinals* de se joindre à moi pour tenter de présenter au mieux et au plus tôt ce cours.

Ce cours me semble essentiel dans l'écosystème Bitcoin, à l'heure de *RGB*, [RGB Protocol on Bitcoin, What is it? | Trust Machines](https://trustmachines.co/learn/what-is-the-rgb-protocol-on-bitcoin/#:~:text=The%20RGB%20network%20is%20a,assets%20on%20the%20Bitcoin%20blockchain.), des annonces de *Ark*, [Bitcoin Developer Introduces New Layer 2 Protocol Ark - Bitcoin Magazine - Bitcoin News, Articles and Expert Insights](https://bitcoinmagazine.com/technical/bitcoin-developer-introduces-new-layer-2-protocol-ark) et une marketcap d'Ordinals estimée à $55,393,093 [Bitcoin Ordinals Analysis](https://dune.com/dgtl_assets/bitcoin-ordinals-analysis).
Comprendre ce nouveau protocole et surtout les derniers développements basés sur ce protocole me semble capital !

Vous trouverez ci-dessous le sommaire, suivi d'un plan détaillé et des parties qui doivent être creusées.

Je me tiens à votre disposition pour toutes questions, critiques ou retour de votre part sur cette pull request ou par mail : galoisfield2718@gmail.com.


# Sommaire

## I/ Introduction
### 1) Premières traces du dossier sur Github & Workshop de Casey
####	a) Une première publication
####	b) La présentation by Casey
####	c) L'arrivée des degens et des techos
### 2) Des idées anciennes, remises au goût du jour
#### 	a) Les colored coins
#### 	b) Counterparty
#### 	c) Ethreum et les ABI
### 3) La core Team
####	a) Github
####	b) Twitter
####	c) Le passage du flambeau

## II) Théorie et implémentation
### 1) Compter les sats
#### 	a) La méthode
####	b) Les choix de Casey
####	c) A la recherche des sats rares
### 2) L'inscription
####	a) L'idée
####	b) La pratique
####	c) Le code
### 3) Le client
####	a) Bitcoin Core 
####	b) `ord`
####	c) Les commandes élémentaires 

## III) Utilisation et dernières avancées
### 1) Outils en lignes
####	a) Unisat 
####	b) Lookordinals
####	c) Xverse 
### 2) JSON et nouveaux protocoles
#### 	a) Début du `sns`
####	b) Arrivée de `brc-20`
#### 	c) Un Meta Protocol : BOSS
### 3) Les cursed inscriptions
####	a) L'issue git #2062
####	b) Le développement
####	c) L'intégration


## Conclusion
### Retour sur l'histoire
### Quel avenir ?
### Pour s'investir



## Annexe A : Utilisation offline du site iancoleman.com pour la génération d'adresse bech32.
## Annexe B : Rédaction de script avec `bitcoin-cli`

//
//


# Plan détaillé du cours

--------
Le but de ce cours est de s'adresser à tous les profils et dont les parties doivent pouvoir être lues indépendamment.

-----------


## I/ Introduction
Dans cette section le but est de s'intéresser à l'histoire de ce protocole et à l'humain qu'il y a derrière.
Le but n'est pas d'être technique mais de comprendre d'où ça vient, de qui et pour quelles motivations. 
Comprendre qui sont les participants et pouvoir permettre aux gens de se renseigner par eux-mêmes davantage sur ces développeurs.

### 1) Premières traces du dossier sur Github & Workshop de Casey
Le développeur phare de ce protocole est Casey Rodarmor ([Casey (@rodarmor) | Twitter](https://twitter.com/rodarmor/), [R O D A R M O R](https://rodarmor.com/), [casey (Casey Rodarmor) | Github](https://github.com/casey/)). 
En 2015, il travailla activement sur Bitcoin Core où il réalisa une série de batchs (mises-à-jours) et un remaniement d'une partie du code de Bitcoin Core ([Casey Rodarmor's Resume](https://rodarmor.com/resume/index.html)).

-> Taproot : en quelques mots, à partir de la réduction du poids des adresses et de l'augmentation de la taille de la *witness* (partie du block space laissant....)


En tant qu'important contributeurs on retrouve [raphjaph (raph)](https://github.com/raphjaph), un étudiant d'informatique à l'université de Munich et [veryordinally (ordinally)](https://github.com/veryordinally?tab=overview&from=2015-12-01&to=2015-12-31) dont le profil a été crée en 2015 mais actif seulement sur Ordinals.

	-> Sur Ordinally on a moins d'infos que sur les autres et ce profil parait assez étrange. Il serait intéressant de creuser d'avantage.

	-> Détailler les autres contributeurs : [Contributors to ordinals/ord](https://github.com/ordinals/ord/graphs/contributors)  

####	a) Une première publication
-> J'avais sauvegardé cette information qui maintenant n'est plus disponible 
[creation ord](./assets/Create_ord_casey.png)

On voit donc un travail pensé pendant presque un an par Casey avant la présentation de son idée en Octobre 2022, sur laquelle nous reviendrons.

-> [Casey Rodarmor: Why I Developed the Ordinals Bitcoin NFT Project](https://www.coindesk.com/consensus-magazine/2023/02/23/casey-rodarmor-why-i-developed-the-ordinals-bitcoin-nft-project-coindesk/)
 

####	b) La présentation by Casey
-> [Ordinals Workshop with Casey Rodarmor](https://www.youtube.com/watch?v=MC_haVa6N3I)

Ce workshop fut la première présentation live par Casey de ce nouveau protocole. Il a eu lieu à Austin au Texas le 27 Août 2022 [Ordinals Workshop with Rodamar, sam. 27 août 2022, 12:00 | Meetup](https://www.meetup.com/fr-FR/pleb-lab/events/287948415/). Il a présenté en live sa théorie, sur ce qu'est Ordinals et les ressources proposées.

-> Qu'est-ce qu'Ordinals ?


>What are Ordinals?
>A scheme for assigning ordinal numbers to satoshis and tracking them across transactions, and a command-line utility, `ord` for querying information about ordinals. 


-> Une présentation de ses motivations par l'art génératif et donner l'opportunité aux artistes d'inscrire leurs œuvres sur Bitcoin.

-> Une présentation assez difficile de ce qu'il entend par "compter les sats" ce sur quoi nous reviendrons plus en détail par la suite. Avec une live démo du site web [ordinals.com](https://ordinals.com), une description du dossier sur Github et enfin la présentation d'un algorithme Python permettant de montrer comment compter les satoshis.


####	c) L'arrivée des degens et des techos

Il fallu néanmoins attendre décembre 2022 pour avoir la première inscription [Inscription #0](https://ord.link/0) réalisée par **bc1qv8zhcjzpjw4m4tdyc5zn3dmax0z6rr6l78fevg** dont on peut voir qu'il ne l'a pas conservée puisque transférée immédiatement à une autre adresse [Activity for bc1qv8zhcjzpjw4m4tdyc5zn3dmax0z6rr6l78fevg | Ordiscan](https://ordiscan.com/address/bc1qv8zhcjzpjw4m4tdyc5zn3dmax0z6rr6l78fevg/activity). L'adresse finale qui possède l'inscription #0 est assez active [Activity for bc1pz4kvfpurqc2hwgrq0nwtfve2lfxvdpfcdpzc6ujchyr3ztj6gd9sfr6ayf | Ordiscan](https://ordiscan.com/address/bc1pz4kvfpurqc2hwgrq0nwtfve2lfxvdpfcdpzc6ujchyr3ztj6gd9sfr6ayf/activity).

Les Bitcoin rocks [Bitcoin Rocks | Ordiscan](https://ordiscan.com/collection/bitcoin-rocks) furent la première collection minté entre 71 et 247. Ils ont été la porte d'entrée des Degens 

### 2) Des idées anciennes, remises au goût du jour

-> Ici, il serait intéressant d'interviewer des gens l'ayant vécu pour avoir leur retour d'expérience. 

#### 	a) Counter Party (2012)

#### 	b) Les colored coins (2014)

#### 	c) Ethreum et les ABI (2015)

### 3) La core Team

Bien que Casey soit la tête de proue de ce projet, il n'est évidemment pas seul !

Seuls quelques uns ont participé très activement au code, mais de nombreuses personnes ont apportés des contributions sans lesquelles nous n'aurions pas un outil aussi complet que celui actuel.
Les différentes issues et discussion constitue également des contributions en soi mais ne malheureusement pas repertoriée dans les commits ^^.

A nous de chercher et d'indexer pour leur rendre hommage ;)

####	a) Github
[Contributors to ordinals/ord](https://github.com/ordinals/ord/graphs/contributors)

![core1](./assets/core_team1.png)
![core2](./assets/core_team2.png)
![core3](./assets/core_team3.png)


####	b) Twitter

Une liste Twitter regroupant les principaux core developpers [ordinals dev list](https://twitter.com/i/lists/1627776735210098708?s=20).

####	c) Le passage du flambeau
[Casey: "I haven't been able to give ord the attention it deserves, so I am pleased to announce that @raphjaph has agreed to step up as lead maintainer! Raph is an impoverished student, and his work on ord will be entirely funded by donations. If you can, please consider donating!…"](https://twitter.com/rodarmor/status/1662617512700420096)

## II) Théorie et implémentation

### 1) Compter les sats

>Every satoshi is serially numbered, starting at 0, in the order in which it is mined. These numbers are termed "ordinal numbers", or "ordinals", as they are ordinal numbers in the mathematical sense, giving the order of each satoshi in the totally supply. The word "ordinal" is nicely unambiguous, as it is not used elsewhere in the Bitcoin protocol.
>The ordinal numbers of transaction inputs are transferred to outputs in first-in-first-out order, according to the size and order of the transactions inputs and outputs.

>If a transaction is mined with the same transaction ID as outputs currently in the UTXO set, following the behavior of Bitcoin Core, the new transaction outputs displace the older UTXO set entries, destroying the ordinals contained in any unspent outputs of the first transaction. This rule is required to handle the two pairs of mainnet transactions with duplicate transaction IDs, namely the coinbase transactions of blocks 91812/91842, and 91722/91880, mined before BIP-34 made the creation of transactions with duplicate IDs impossible.

>For the purposes of the assignment algorithm, the coinbase transaction is considered to have an implicit input equal in size to the subsidy, followed by an input for every fee-paying transaction in the block, in the order that those transactions appear in the block. The implicit subsidy input carries the block's newly created ordinals. The implicit fee inputs carry the ordinals that were paid as fees in the block's transactions.

>Underpaying the subsidy does not change the ordinal numbers of satoshis mined in subsequent blocks. Ordinals depend only on how many satoshis could have been mined, not how many actually were.


#### 	a) La méthode

-> Détaillée longuement dans son workshop et présentée ci-dessus, il faut en faire une synthèse en français.

####	b) Les choix de Casey

-> Casey a choisit de nommer les sats en les numérotants.

-> Il a également ajouté des "steps" en plus du halving avec les cycles et autres pour créer de la rareté sur certains sats.

-> Il a créé un classement de sats rares. 

--> Néanmoins de nouvelles raretés sont apparus : *Retrouver le site qui permet de check ses sats et donne de nouvelles raretés*

####	c) A la recherche des sats rares

Outils online le plus facile. On donne son adresse et ils l'analysent.

-> Retrouver les outils online pour analyser les sats. 

Moyen de le faire par ligne de commande mais je ne sais toujours pas comment.

### 2) L'inscription

Maintenant qu'on sait compter les sats, on peut les manipuler. Ordinals propose d'inscrire sur ces derniers.

####	a) L'idée

Quand on fait une transaction, on peut stocker la data sur le premier sat de la tx. 

Techniquement il est utilisé une double tx de commit puis de reveal. Cela doit encore être détaillé sur pourquoi cette double tx. A priori c'est pour que le reveal connaisse l'output et puisses inscrire sur le bon sat. 
Mais il faut encore creuser un petit peu.


####	b) La pratique

-> Concrétement on n'a pas besoin de comprendre pourquoi ce fonctionnement pour l'utiliser. 

Néanmoins, suite à une inscription avec le client `ord` on obtient un json output de cette forme : 

```JSON
{
  "commit": "0bdbae349b685c0a59fa275f18d4ad14c3972fb5998d513399a478d87d805e00",
  "inscription": "d4ad4cd729fdd4dfaa5279aed4910e4afcfac6e3be25900ba40a2faebef28a9fi0",
  "reveal": "d4ad4cd729fdd4dfaa5279aed4910e4afcfac6e3be25900ba40a2faebef28a9f",
  "fees": 8440
}

```
Le commit et le reveal sont deux transactions qui permettent de réaliser l'inscritpion sur Bitcoin. Si vous souhaitez savoir pourquoi deux transactions je vous invite à consulter [Segregated Witness (SegWit) road to implementation](https://www.coingecko.com/learn/segregated-witness-road-to-implementation).

L'inscription est ce que l'on peut chercher sur les explorer.


####	c) Le code

--> [ordinals/ord/src/subcommand/wallet/inscribe.rs](https://github.com/ordinals/ord/tree/master/src/subcommand/wallet/inscribe.rs)

-> Le but n'est peut-être pas d'analyser TOUT le code mais détailler quelques fonction importantes comme `create_inscription_transactions` et `build_reveal_transaction`.

-> Pour les dev, ce fichier `inscribe.rs` doit pouvoir être modifié modéremment sans impacter le reste du programme client `ord`. Par exemple, les fees utilisés pour réaliser les transactions doivent pouvoir être modifié.
Une discussion approfondie avec des tests d'implémentation avancées pourrait être intéressante.

### 3) Le client
La référence pour cette partie est cette vidéo : [How To Setup A Bitcoin Node & Ord Wallet](https://www.youtube.com/watch?v=tdC8kmjn5N0&list=LL&index=1&t=0s)
Cette vidéo est faites sur Windows et étant sur Mac avec un node sur Disque dur externe je proposerai les commandes pour setup ceci sur Linux et Mac.

####	a) Bitcoin Core 

Note
-------
Cette partie a peut-être été réalisée ailleurs et pourrait simplement être référencée avec quelques ajouts ou copiée collée. A discuter de ce qui est le mieux.
-------

Requirements : 
- env. 700 Go de stockage, en SSD si possible.
- une bonne connexion internet.

Soit vous avez un vieil ordinateur et vous faites tourner le nœud Bitcoin sur celui-ci, soit je vous conseille de prendre un disque dur externe SSD de 1 To. Vous en trouver pour moins d'une centaine d'euros sur internet en général. 

[-> Lien pour Comparateur de prix et de marques.] 

[jonasnick/bitcoin-node: "How to Run a Bitcoin Node" handout](https://github.com/jonasnick/bitcoin-node)

**Step-by-Step installation Bitcoin Core**
1) Allez sur : [Download - Bitcoin](https://bitcoin.org/en/download) puis télécharger le version qui correspond à votre système d'exploitation ; 

2) Ouvrez le paquet qui doit ressembler à ceci : 
--> Mettre une image

3) Suivre les instructions

4) Configurer via `bitcoin.conf` pour que le lieu de stockage soit de la forme : 
*Sur Mac* : 
- `/Volumes/mon_disque/bitcoin`

*Sur Linux* : 
- `/media/mon_disque/bitcoin`

*Sur Windows* : 
- `C:/mon_disque`

5) Ligne de commande : 
*Sur Mac* : 
```
./bitcoin/bin/bitcoind --conf=/Volumes/mon_disque/bitcoin/bitcoin.conf --txindex=1
```
3) Suivre les instructions

4) Configurer via `bitcoin.conf` pour que le lieu de stockage soit de la forme : 
*Sur Mac* : 
- `/Volumes/mon_disque/bitcoin`

*Sur Linux* : 
- `/media/mon_disque/bitcoin`

*Sur Windows* : 
- `C:/mon_disque`

5) Ligne de commande : 
*Sur Mac* : 
```
./bitcoin/bin/bitcoind --conf=/Volumes/mon_disque/bitcoin/bitcoin.conf --txindex=1
```
Si cela ne suffit pas pour le forcer à télécharger la blockchain dans `mon_disque` alors ajouter les flags `--data-dir=/Volumes/mon_disque/bitcoin/Bitcoin --blocksdir=/Volumes/mon_disque/bitcoin/Bitcoin/blocks --settings=/Volumes/mon_disque/bitcoin/Bitcoin/settings.json --walletdir=/Volumes/mon_disque/bitcoin/Bitcoin/wallets --txindex=1`

*Sur Linux* : 


*Sur Windows* : 

####	b) `ord`
Une fois que le nœud est entièrement téléchargé on peut télécharger et lancer le client `ord`. On parle de client pour parler de la ligne de commande qui est utilisé pour intéragir avec le protocole ordinals.

Téléchargez `ord`: [Releases · ordinals/ord](https://github.com/ordinals/ord/releases)
en prenant la dernière mise à jour.

**Setup du wallet et inscription**

i) `ord wallet create` : Crée un portefeuille ordinals. 
```
USAGE:
    ord wallet create [OPTIONS]

OPTIONS:
    -h, --help                       Print help information
        --passphrase <PASSPHRASE>    Use <PASSPHRASE> to derive wallet seed. [default: ]
```

ii) `ord wallet receive` : Génère une adresse de réception Taproot. Envoyer des fonds sur celle-ci.
Vérifier l'arrivée des fonds avec `ord wallet balance`.

iii) Calculer le cout d'une inscription avec [instacal.com/56229](https://instacalc.com/56229)

iv) `ord wallet inscribe path/to/file --fee-rate=x` : Inscrit le fichier désigné dans le path avec x sats/vB. Les types gérés par le client `ord`sont: txt, json, webp, html,png, jpeg.

```
ord-wallet-inscribe 
Create inscription

USAGE:
    ord wallet inscribe [OPTIONS] --fee-rate <FEE_RATE> <FILE>

ARGS:
    <FILE>    Inscribe sat with contents of <FILE>

OPTIONS:
        --commit-fee-rate <COMMIT_FEE_RATE>
            Use <COMMIT_FEE_RATE> sats/vbyte for commit transaction.
            Defaults to <FEE_RATE> if unset.

        --destination <DESTINATION>
            Send inscription to <DESTINATION>.

        --dry-run
            Don't sign or broadcast transactions.

        --fee-rate <FEE_RATE>
            Use fee rate of <FEE_RATE> sats/vB

    -h, --help
            Print help information

        --no-backup
            Do not back up recovery key.

        --no-limit
            Do not check that transactions are equal to or below the MAX_STANDARD_TX_WEIGHT of
            400,000 weight units. Transactions over this limit are currently nonstandard and will
            not be relayed by bitcoind in its default configuration. Do not use this flag unless you
            understand the implications.

        --satpoint <SATPOINT>
            Inscribe <SATPOINT>
```

Le retour de cette commande doit être de la forme : 

```
{
  "commit": "ebcd883015295586d9db921e649fdc04a02476827591103aa28e85ec3d36d903",
  "inscription": "23aef7fa2df44a0192dde9ce14bee594ece7890c701820ed7c727485f154e4e0i0",
  "reveal": "23aef7fa2df44a0192dde9ce14bee594ece7890c701820ed7c727485f154e4e0",
  "fees": 311
}
```


v) `ord wallet inscritpions` : Cela permet de lister les inscriptions dans le wallet. 


----------------

Attention je n'ai pas encore trouver comment faire pour que l'indexing du client qui produit `index.redb` soit dans le disque dur et non pas sur l'ordinateur.
Néanmoins, il est beaucoup plus léger que la chain Bitcoin (~ 13 Go) donc c'est moins dérangeant. 

----------------


####	c) Les commandes élémentaires/utiles 

- `ord help` Liste toutes les commandes

- `ord wallet -help` Liste les sous-commandes de wallet

- `ord wallet create` Crée un nouveau wallet

- `ord wallet balance` Donne la balance du wallet ord actuel

- `ord server` Génère la page web [ordinals.com](https://ordinals.com) en local.

Ci-dessous on trouvera le retour de `ord help`.

Pour avoir plus de détail sur une commande on tapera : 
`ord <commande> --help`

```
ord 0.6.2

USAGE:
    ord [OPTIONS] <SUBCOMMAND>

OPTIONS:
        --bitcoin-data-dir <BITCOIN_DATA_DIR>
            Load Bitcoin Core data dir from <BITCOIN_DATA_DIR>.

        --bitcoin-rpc-pass <BITCOIN_RPC_PASS>
            Authenticate to Bitcoin Core RPC with <RPC_PASS>.

        --bitcoin-rpc-user <BITCOIN_RPC_USER>
            Authenticate to Bitcoin Core RPC as <RPC_USER>.

        --chain <CHAIN_ARGUMENT>
            Use <CHAIN>. [default: mainnet] [possible values: mainnet, testnet, signet, regtest]

        --config <CONFIG>
            Load configuration from <CONFIG>.

        --config-dir <CONFIG_DIR>
            Load configuration from <CONFIG_DIR>.

        --cookie-file <COOKIE_FILE>
            Load Bitcoin Core RPC cookie file from <COOKIE_FILE>.

        --data-dir <DATA_DIR>
            Store index in <DATA_DIR>.

        --first-inscription-height <FIRST_INSCRIPTION_HEIGHT>
            Don't look for inscriptions below <FIRST_INSCRIPTION_HEIGHT>.

    -h, --help
            Print help information

        --height-limit <HEIGHT_LIMIT>
            Limit index to <HEIGHT_LIMIT> blocks.

        --index <INDEX>
            Use index at <INDEX>.

        --index-sats
            Track location of all satoshis.

    -r, --regtest
            Use regtest. Equivalent to `--chain regtest`.

        --rpc-url <RPC_URL>
            Connect to Bitcoin Core RPC at <RPC_URL>.

    -s, --signet
            Use signet. Equivalent to `--chain signet`.

    -t, --testnet
            Use testnet. Equivalent to `--chain testnet`.

    -V, --version
            Print version information

        --wallet <WALLET>
            Use wallet named <WALLET>. [default: ord]

SUBCOMMANDS:
    epochs     List the first satoshis of each reward epoch
    find       Find a satoshi's current location
    help       Print this message or the help of the given subcommand(s)
    index      Update the index
    info       Display index statistics
    list       List the satoshis in an output
    parse      Parse a satoshi from ordinal notation
    preview    Run an explorer server populated with inscriptions
    server     Run the explorer server
    subsidy    Display information about a block's subsidy
    supply     Display Bitcoin supply information
    traits     Display satoshi traits
    wallet     Wallet commands

```

On sait maintenant inscrire en ligne de commandes. Beaucoup d'autres options sont disponibles et j'invite ceux qui le souhaitent à détailler ici des commandes standards ainsi que leur utilisation. 

## III) Utilisation et dernières avancées

Evidemment tout le monde ne va pas utiliser le client `ord` avec le full node Bitcoin.

Il faut donc des outils plus accessibles et online. 
Ces outils online présentent aussi parfois certains avantages, comme l'optimisation de frais, bien plus difficile via le client seul, des inscriptions spéciales via des templates pour certains protocoles (voir III.2), ou les cursed inscriptions (voir III.3).

Ils permettent donc une intégration simple et avancée des dernières fonctionnalités offertes par le protocole ordinals.

Plongeons alors dans ces outils avant de nous attaquer aux protocoles construits sur Ordinals puis aux Cursed Inscriptions.

### 1) Outils en lignes
Les outils en lignes apparaissent comme nécessaires pour le développement de l'écosystème et on va essayer de les traiter en profondeur. 

-> Des tutos sur chacun de ces outils serait le bienvenue ;)

Un outil très utilisé dans le groupe [Ordinals Francophone](https://t.me/OrdinalsFR) est [unisat.io](https://unisat.io), que l'on va détailler dans la partie suivante.

####	a) Unisat
Pour utiliser *Unisat* convenabelement il conviendra d'être sur un navigateur Chromium (Brave, google chrome, chromium,...). Firefox et Safari ne prennent pas en charge tous les outils d'Unisat.

Voici une liste d'étapes à suivre pour avoir accès aux fonctionnalités offertes par Unisat : 

1) Télécharger l'extension [Unisat Wallet](https://chrome.store/unisat-extension).

2) Créer un nouveau Wallet.

3) Cliquer sur "se connecter" sur le site [Unisat.io](https://unisat.io).

4) Vous avez accès à toutes les fonctionnalités du site.


Unisat est une application web qui permet : 

i) **D'inscrire** différents type de fichiers et des brc-20, sns et unisat name, en natif. L'inscription de brc-20 a fait sa popularité.

ii) **De visualiser** ce qui a été inscrits par Ordinals. Une de ses fonctionnalités principale est la gestion et les informations fournises pour les brc-20. Cela est géré et affiché en natif.
Quid des nouveaux standards ?
[@Lorenzonical](https://twitter.com/lorenzonical) Le fondateur d'unisat.

Un post très intéressant détaillant une interview du fondateur donnée à LeonidasNFT [Post de l'interview](https://twitter.com/unisat_wallet/status/1673936418748637184).
Avec son lien vers l'inscription de l'interview [Inscription interview de Lorenzocanical](https://t.co/ylMxRGk1Uj).

iii) D'accéder à une **Marketplace** pour acheter et revendre des ordinals. Certainement l'une des principales marketplace brc-20 en terme de volumes, elle a récemment intégrée et mise en avant des collections d'images et de vidéos. De nombreuses personnes travaillent à scraper (récupérer) les données de cette marketplace. Pour l'instant c'est toujours en développement.



####	b) [Lookordinals](https://lookordinals.com)

A la différence d'unisat cette plateforme sert uniquement à faire des inscriptions. 
Certainement le moins cher du marché actuellement, recommandée par [@0xGrug](https://t.me/OxGrug).

La force de Lookordinals ? Toutes ses options d'inscriptions : 

PRENDRE LE SCREEN
![screenshot lookordinals](assets/lookordinals.png)

Sa faiblesse ? Assez archaïque, on a l'impression de revenir sur le web des années 2000. Néanmoins, elle fait très bien le job et après tout c'est ce qu'on demande.

Régulièrement mise à jour, son code est également disponible sur Github pour ceux qui voudrait le fork [Github Lookordinals]()


####	c) Les moins utilisées

- ordinalswallet.com

- Gamma.io

- Xverse

 

### 2) JSON et nouveaux protocoles

Rapidement, le coût d'inscription d'image étant élevé des gens se sont tournés sur l'inscription de fichier textuel (moi le premier [galoisfield.btc](https://ord.link/187784)).
Néanmoins, avec de simple fichier texte comment se repérer ? Comment les retrouver ?
Comment les **INDEXER** ? 

Cette question de l'indexing est majeure sur ce protocole Ordinals et sur les protocoles construits sur Ordinals. 

Mais alors comment ça marche ?

Plongeons dans l'histoire !

#### 	a) Début du `sns`

Un acteur important de l'ecosystème ordinals est [@domodata](https://twitter.com/domodata).

Arrivé avec son full node le 24 février [domo: "Full node finally running. Will soon find out if the feeling of owning a wallet full of UTXOs, redolent with the scent of rare and exotic sats, is beyond compare."](https://twitter.com/domodata/status/1629134663842254848) il proposa rapidement de nouveaux standard.

Le premier qu'il a utilisé est `sns` pour Sats Name Service : 
![domo-sns](./assets/domo_sns.png)
[domo: "@sats-names"](https://twitter.com/domodata/status/1630948879737794561)

Etant le premier protocole construit sur Ordinals il a deux manière d'être utilisé.

1. La première très simple qui consiste simplement à inscrire un fichier texte avec `.sats`. Ce n'est pas celle qui nous intéressera ici.

2. Définir un fichier JSON contenant les specifications suivant : 
  a) Le nom du protocole via `"p" : "sns"`, ici le protocole utilisé est `sns`.
  b) L'opération voulu via `"op": "reg"`, ici `reg` signifie que l'on défninit un nouveau nom.
  c) Le nom choisit via : `"name" : "my_name.sats"`, on choisit `my_name.sats`.

3. On a aussi deux paramèters optionnels dans ce protocole : 
  a) L'association d'un sats name à une adresse btc via `"rev" : "bc1q...."`.
  b) L'association d'un sats name à une inscription via `"relay" : "...i0"`.

Vous trouverez la documentation à l'adresse suivante [Mint names - Sats Names](https://docs.sats.id/sats-names/sns-spec/mint-names)

L'idée du protocole `sns` qui sera celle qui nous suivra tout au long de ces sur-protocoles est l'utilisation d'un JSON vérifiant toujours plus ou moins cette structure. 

En voici un exemple :  
```JSON
{
 "p" : "sns",
 "op" : "reg",
 "name" : "galoisfield.sats",
 "rev" : "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
}
```

On a donc ici construit un protocole dont les éléments sont facilement reprérables parmi toutes les inscritpions et permettant à n'importe qui d'*indexer* ces éléments et de les utiliser dans n'importe quelles applications. 

-> Pour les developpeurs chevronnés vous pouvez essayer de développer ou d'intégrer ce protocole à une application pour permettre le login des utilisateurs ou la vérification d'achievements dans votre app. 


####	b) Arrivée de `brc-20`

Maintenant que l'on a compris le fonctionnement du protocole `sns` il nous sera très facile d'appréhender d'autre protocole comme par exemple `brc-20`.

Posé pour la première fois par *@domodata* [domo: "Using inspiration from @sats_names and @redphonecrypto, I wondered if the concept could be expanded to fungible tokens. This is what I came up with: 2/x https://t.co/h6fksQ1WpM"](https://twitter.com/domodata/status/1633658976931037184).

L'idée est simple : répliquer le concept de protocole comme `sns` pour créer des tokens sur Bitcoin. 

On garde : le protocole, l'opération, on remplace `name` par `tick`, on ajoute `amt` pour le montant de jetons considérés et on distingue les opérations de déploiement, de mint et de transfer. 

L'opération la plus *tricky* est celle de transfer sur laquelle nous reviendrons un peu plus tard. 

Une contrainte posé par Domo est que le ticker d'un brc-20 ne doit comporter que 4 caractères. 

-> Trouver une ref de pourquoi 4 caractères.

Pour un détail en vidéo de ces explications vous pouvez consulter [The Only BRC-20 Guide You Will Need](https://www.youtube.com/watch?v=XftBkRZ9jqk).

Faisons le schéma complet d'un token `DBTC` pour DécouvreBitcoin (le token existe déjà et n'y est pas relié, ceci est simplement à titre indicatif et ne constitue en aucun cas une invitation à le mint, l'acheter ou autre) : 

1. Le déploiement

On a notre ticker maintenant il faut décider d'un montant. Pour être cohérent avec celui déjà déployé prenons 21 000.
```JSON
{ 
 "p": "brc-20",
 "op": "deploy",
 "tick": "DBTC",
 "amt" : "21000",
 "lim" : "1"
}
```

L'instruction `lim` détermine combien de token pourront être minté en une fois. 

Si `lim = 1` mais que vous en mintez 2 alors vous n'aurez aucun token car votre instruction ne sera pas valide au regard du protocole. 
Faites bien attention à ceci quand vous mintez !

![DBTC](./assets/DBTC.png)
  

2. Le mint

Une fois notre token déployé on peut le mint. Pour cela il faut inscrire le JSON suivant : 

```JSON
{
 "p" : "brc-20",
 "op": "mint",
 "tick": "DBTC",
 "amt": "1"
}
```

Une fois l'inscription minée dans un block vous aurez 1 DBTC associé à votre addresse de mint.


3. Le transfer

Maintenant que vous avez mint le token `DBTC` vous pouvez le transférer (à votre meilleur ami, votre compagne ou compagnon ou quelqu'un qui souhaiterais vous l'acheter).

Pour ce faire il vous faudra suivre deux étapes : 

A. L'inscription de l'opération `transfer` 

```JSON
{
 "p": "brc-20",
 "op": "transfer",
 "tick": "DBTC",
 "amt": "1"
}
```

Ici vous avez maintenant 1 DBTC transférable au regard du protocole `brc-20`.

Vous pouvez alors le transférer.

B. Le transfer du token

Il vous faut maintenant faire une tansaction Bitcoin. 
Vous devez envoyer l'inscription de transfer à la personne souhaitée. 

Via les wallets online cela se fait en cliquant simplement sur `Transfer` ou `Envoie`.

Via le client ord il vous faudra :
- lister vos inscriptions par la commande `ord wallet inscriptions` ; 
- selectionner celle qui vous intéresse ; 
- entrer la commande `ord --cookie-file=/Volumes/mon_disque/bitcoin/.cookie wallet send --fee-rate 3 bc1pxsa6d95jrwald4jjsu0kwu4pyaztmjvh6rdjyrztfv0yx2gakk9qse5sjf acddd636c4ab0fb45c9f70ce2598cffa205c88594de916832a5789e3e58ca688i0`.

Si vous connaissez déjà l'inscription de transfer entrez directement la dernière commande (adaptée à vos système d'exploitation, ici MacOs).


On a donc ici couvert toutes les opérations réalisables avec `brc-20`. 
A ce stade vous devez mieux voir comment fonctionne ces protocoles construits sur Ordinals. 

Il y aurait beaucoup à dire des discussions qui ont animés les différents discord et telegram en lien avec `brc-20` et cela pourra faire l'objet d'articles annexes.


#### 	c) Un Meta Protocol : BOSS

Maintenant que nous avons compris comment fonctionne ces deux protocoles nous pouvons nous attaquer à un très gros morceau qui est pour l'instant toujours en développement le Meta Procole **BOSS** (Bitcoin Operationnal Standard System).

BOSS propose un avenir florissant avec l'idée de Meta Protocols. Créant un standard sur tous ces protocoles sauvages ainsi qu'une machine virtuelle on peut s'attendre à ce que beaucoup de solutions de demain soit construites sur BOSS.
En tout cas, BOSS va être un terrain d'expérimentation assez fou sur Bitcoin.


De nouvelles choses sont régulièrement proposés. Des interfaces améliorées, du code à clarifier, des articles à écrire, des tutos à réaliser, les choses qui arrivent ne manque pas et nous devons nous tenir informés pour être là où les choses se développent.



### 3) Les cursed inscriptions

Les inscriptions "maudites". Ces inscriptions ont fait leur apparitions quelques mois après le lancement d'Ordinals.
Une cursed inscription est basiquement une inscritpion non valide a priori pour le protocole Ordinals.

####	a) L'issue git #2062

Dans l'issue git [Inscription numbers off by one, or the curious case of transaction `c1e0db6368a43...d9e4117151` · Issue #2062 · ordinals/ord](https://github.com/ordinals/ord/issues/2062) quelque chose d'étrange a été trouvé. 
Une inscription avec 0 satoshi attachée !

Enfer et damnation ! Nous avons dit qu'il fallait inscrire sur des satoshis. Comment est-ce possible ?

Est-ce la seule forme d'inscription non valide ?

NON ! 

De nombreuses inscriptions non valides au regard du protocole Ordinals ont pu être inscrite dont on peut avoir un détail avec l'issue ouverte par Casey [Cursed Inscription Tracking Issue · Issue #2045 · ordinals/ord](https://github.com/ordinals/ord/issues/2045). 

Des inscriptions multiples, des inscriptions avec d'autres `OP_CODE` par exemple l'`op_code`, `OP_66` qui n'est pas indexé par `ord`, ... .

Afin d'intégrer les cursed inscriptions sur le marché et sur l'indexer il a été décidé dans un premier temps de les indexer par un nombre négatif avant de les considérer comme valides et positives dans la nouvelle mise à jour [Leonidas.og: "Version 0.6.0 of the Ordinals Protocol just went live! Here is everything you need to know about this major update"](https://twitter.com/LeonidasNFT/status/1665437076450336768).

On n'en est encore qu'au début et beaucoup de choses vont être amenée à changer. Les cursed inscriptions seront quelque chose d'historique pour l'écosystème. Même s'il n'est pas nécessaire de se plonger à corps perdu dans ce type d'inscription il est important de voir que cela a été un pas important dans l'intégration de nouvelles formes d'inscriptions sur Ordinals. 
Ordinals est un protcole très jeune et en constante évolution. Suivre ce genre d'événement permet de mieux comprendre ce peut arriver par la suite et savoir gérer des nouveautés dans les inscriptions.



Pour plus de détail sur les `OP_CODE` de Bitcoin on pourra consulter [Opcodes used in Bitcoin Script - Bitcoin Wiki](https://wiki.bitcoinsv.io/index.php/Opcodes_used_in_Bitcoin_Script).

-> Références supplémentaires sur les cursed inscritptions
[Bitcoin Ordinals and the mystery of the 'cursed Inscriptions' - AMBCrypto](https://ambcrypto.com/bitcoin-ordinals-and-the-mystery-of-the-cursed-inscriptions/)
[Inscriptions in Reverse: The Quirky Journey of Cursed Ordinals - Influencive](https://www.influencive.com/inscriptions-in-reverse-the-quirky-journey-of-cursed-ordinals/)
[Bitcoin Ordinals rolls out upgrade to rectify 'Cursed Inscriptions' issue](https://cointelegraph.com/news/bitcoin-ordinals-upgrade-rectify-cursed-inscriptions-issue)


####	b) Le développement

La mise à jour d'ordinals pour prendre en compte les cursed inscriptions dans la version (0.6.0) publiée le 4 juin 2023.

[raph: "Just released a new version of ord (0.6.0), which implements the first steps in recognizing more types of inscriptions (cursed inscriptions). Additionally you can now pass in RPC credentials through command-line flags, environmental vars or a config file. https://t.co/Xi6C92cC6z"](https://twitter.com/raphjaph/status/1665367103342362625)

L'acceptation de ces cursed inscriptions permet maintenant de manipuler "légalement" les inscriptions multiples dans une même transaction et sur un même satoshi. 

-> Il faudrait préparer un TP sur ce sujet !

# Conclusion

Une des choses les plus puissantes offertes par Ordinals est certainement BOSS. Actuellement en développement, les promesses de BOSS sont assez folles. 
Il faudrait dédier un papier entier aux fonctionnalités qu'annonce BOSS et une étude approfondie du lightpaper.

Un workshop coordoné avec un développeur JS ayant étudié les propositions techniques de la BVM (Bitcoin Virtual Machine) proposée par BOSS et un "théoricien" mettant en lumière l'architecture du projet pourrait être très intéressant pour mieux appréhender BOSS.

Evidemment il n'y a pas que BOSS. Beaucoup de choses sont encore à découvrir et créer ! 
Ce cours bien qu'autant exhaustif que possible est loin de tout couvrir et nécessite encore beaucoup de travail d'approfondissement et de recherche individuelle comme académique pour pouvoir être complet.



### Pour s'investir

-> Participer à la rédaction de ce cours.

-> Tuto Youtube, Live, contenus, accompagnement de gens intéressés.

-> Développement par fork d'unisat ou de lookordinals.

-> Développement de nouvelles idées via des inscriptions HTML ou interprétation de code au format txt via un nouvel indexer peut être essayé.

-> Prise en main de BOSS dès que le code sera disponible. Pour un tech JS, se coordoner pour organiser le workshop discuté précedemment. 





