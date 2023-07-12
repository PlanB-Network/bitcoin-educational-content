---
name: RGB
description: Introduction et création d'actifs sur RGB
---

# Une brève introduction aux protocoles RGB

Francisco Calderón publié le
08 novembre 2021
https://grunch.dev/blog/brief-intro-rgb/
grunch@getalby.com

![RGB vs Ethereum](assets/0.png)

## Introduction

Le 3 janvier 2009, Satoshi Nakamoto a lancé le premier nœud Bitcoin, à partir de ce moment-là, de nouveaux nœuds ont rejoint et Bitcoin a commencé à se comporter comme s'il s'agissait d'une nouvelle forme de vie, une forme de vie qui n'a cessé d'évoluer, petit à petit, il est devenu le réseau le plus sûr au monde grâce à sa conception unique, très bien pensée par Satoshi, car, grâce à des incitations économiques, il attire des utilisateurs communément appelés mineurs à investir dans l'énergie et la puissance de calcul, ce qui contribue à la sécurité du réseau.

Alors que Bitcoin continue sa croissance et son adoption, il fait face à des problèmes de scalabilité. Le réseau Bitcoin permet à un nouveau bloc avec des transactions d'être miné en environ 10 minutes. En supposant que nous ayons 144 blocs par jour avec des valeurs maximales de 2700 transactions par bloc, Bitcoin n'aurait permis que 4,5 transactions par seconde. Satoshi était conscient de cette limitation, nous pouvons le voir dans un e-mail1 envoyé à Mike Hearn en mars 2011 où il explique comment ce que nous connaissons aujourd'hui sous le nom de canal de paiement fonctionne. micropaiements rapidement et en toute sécurité sans attendre de confirmations. C'est là que les protocoles hors chaîne entrent en jeu.

Selon Christian Decker2, les protocoles hors chaîne sont généralement des systèmes dans lesquels les utilisateurs utilisent des données d'une blockchain et les gèrent sans toucher à la blockchain elle-même jusqu'à la dernière minute. Sur la base de ce concept, le Lightning Network est né, un réseau qui utilise des protocoles hors chaîne pour permettre des paiements Bitcoin presque instantanés et, comme toutes ces opérations ne sont pas écrites sur la chaîne de blocs, il permet des milliers de transactions par seconde et met à l'échelle Bitcoin.

La recherche et le développement dans le domaine des protocoles hors chaîne sur Bitcoin ont ouvert une boîte de Pandore, aujourd'hui nous savons que nous pouvons réaliser beaucoup plus que le transfert de valeur de manière décentralisée, l'association à but non lucratif LNP/BP Standards se concentre sur le développement de protocoles de couche 2 et 3 sur Bitcoin et le Lightning Network, parmi ces projets, RGB se distingue.

## Qu'est-ce que RGB ?

RGB est apparu à partir des recherches de Peter Todd3 sur les scellés à usage unique et la validation côté client, qui a été formulé en 2016-2019 par Giacomo Zucco et la communauté en un meilleur protocole d'actifs pour Bitcoin et le réseau Lightning. L'évolution ultérieure de ces idées a conduit au développement de RGB en un système de contrats intelligents à part entière par Maxim Orlovsky, qui en assure la mise en œuvre depuis 2019 avec la participation de la communauté.

Nous pouvons définir RGB comme un ensemble de protocoles open source qui nous permet d'exécuter des contrats intelligents complexes de manière évolutive et confidentielle. Ce n'est pas un réseau particulier (comme Bitcoin ou Lightning) ; chaque contrat intelligent est simplement un ensemble de participants au contrat qui peuvent interagir en utilisant différents canaux de communication (par défaut, le réseau Lightning). RGB utilise la blockchain Bitcoin comme couche d'engagement de l'état et conserve le code du contrat intelligent et les données hors chaîne, ce qui le rend évolutif, en exploitant les transactions Bitcoin (et Script) comme système de contrôle de propriété pour les contrats intelligents ; tandis que l'évolution du contrat intelligent est définie par un schéma hors chaîne, il est enfin important de noter que tout est validé côté client.

En termes simples, RGB est un système qui permet à l'utilisateur d'auditer un contrat intelligent, de l'exécuter et de le vérifier individuellement à tout moment sans coût supplémentaire, car il n'utilise pas une blockchain comme le font les systèmes "traditionnels". Les systèmes de contrats intelligents complexes ont été pionnés par Ethereum, mais en raison de la nécessité pour l'utilisateur de dépenser des quantités importantes de gaz pour chaque opération, ils n'ont jamais atteint la scalabilité promise, ce qui en fait jamais une option pour les utilisateurs exclus du système financier actuel.

Actuellement, l'industrie de la blockchain promeut que le code des contrats intelligents et les données doivent être stockés dans la blockchain et exécutés par chaque nœud du réseau, indépendamment de l'augmentation excessive de la taille ou de l'utilisation abusive des ressources informatiques. Le schéma proposé par RGB est beaucoup plus intelligent et efficace car il rompt avec le paradigme de la blockchain en séparant les contrats intelligents et les données de la blockchain, évitant ainsi la saturation du réseau observée sur d'autres plateformes. De plus, il ne force pas chaque nœud à exécuter chaque contrat, mais plutôt les parties impliquées, ce qui ajoute une confidentialité à un niveau jamais vu auparavant.

![RGB vs Ethereum](assets/1.png)

## Contrats intelligents dans RGB

Dans RGB, le développeur de contrats intelligents définit un schéma spécifiant les règles selon lesquelles le contrat évolue dans le temps. Le schéma est la norme pour la construction de contrats intelligents dans RGB, et à la fois un émetteur lors de la définition d'un contrat pour l'émission et un portefeuille ou une bourse doivent adhérer à un schéma particulier contre lequel ils doivent valider le contrat. Seulement si la validation est correcte, chaque partie peut accepter les demandes et travailler avec l'actif.

Un contrat intelligent dans RGB est un graphe acyclique dirigé (DAG) de changements d'état, où seule une partie du graphe est toujours connue et il n'y a pas d'accès au reste. Le schéma RGB est un ensemble de règles de base pour l'évolution de ce graphe avec lequel le contrat intelligent démarre. Chaque participant au contrat peut ajouter à ces règles (si cela est autorisé par le schéma) et le graphe résultant est construit à partir de l'application itérative de ces règles.

## Actifs fongibles

Les actifs fongibles dans RGB suivent la spécification LNPBP RGB-20, lorsque RGB-20 est défini, les données d'actif connues sous le nom de "données de genèse" sont distribuées via le réseau Lightning, ce qui contient ce qui est nécessaire pour utiliser l'actif. La forme la plus basique des actifs n'autorise pas l'émission secondaire, la destruction de jetons, la renomination ou le remplacement.

Parfois, l'émetteur aura besoin d'émettre plus de jetons à l'avenir, par exemple des stablecoins tels que USDT, qui maintiennent la valeur de chaque jeton liée à la valeur d'une monnaie inflationniste telle que le dollar américain. Pour cela, des schémas RGB-20 plus complexes existent, et en plus des données de genèse, ils exigent de l'émetteur de produire des envois, qui circuleront également dans le réseau Lightning ; avec ces informations, nous pouvons connaître l'offre totale en circulation de l'actif. Il en va de même pour les actifs brûlants ou pour le changement de leur nom.

Les informations relatives à l'actif peuvent être publiques ou privées : si l'émetteur exige la confidentialité, il peut choisir de ne pas partager d'informations sur le jeton et effectuer des opérations en toute confidentialité absolue, mais nous avons également le cas inverse où l'émetteur et les détenteurs ont besoin que tout le processus soit transparent. Cela est réalisé en partageant les données du jeton.

## Procédures RGB-20

La procédure de destruction désactive les jetons, les jetons brûlés ne peuvent plus être utilisés.

La procédure de remplacement se produit lorsque des jetons sont brûlés et qu'une nouvelle quantité du même jeton est créée. Cela permet de réduire la taille des données historiques de l'actif, ce qui est important pour maintenir la rapidité de l'actif.

Pour prendre en charge le cas d'utilisation où il est possible de brûler des actifs sans avoir à les remplacer, un sous-schéma de RGB-20 est utilisé qui permet uniquement de brûler des actifs.

## Actifs non fongibles

Les actifs non fongibles (NFT) dans RGB suivent la spécification LNPBP RGB-21, lorsque nous travaillons avec des NFT, nous avons également un schéma principal et un sous-schéma. Ces schémas ont une procédure de gravure, qui nous permet d'attacher des données personnalisées par le propriétaire du jeton, l'exemple le plus courant que nous voyons aujourd'hui dans les NFT est l'art numérique lié au jeton. L'émetteur du jeton peut interdire cette gravure de données en utilisant le sous-schéma RGB-21. Contrairement à d'autres systèmes de blockchain NFT, RGB permet de distribuer des données de jeton multimédia de grande taille de manière décentralisée et résistante à la censure, en utilisant une extension du réseau P2P Lightning appelée Bifrost, qui est également utilisée pour construire de nombreuses autres fonctionnalités de contrat intelligent spécifiques à RGB.

En plus des actifs fongibles et des NFT, RGB et Bifrost peuvent être utilisés pour produire d'autres formes de contrats intelligents, y compris des DEX, des pools de liquidité, des stablecoins algorithmiques, etc., que nous aborderons dans des articles futurs.

## NFT de RGB vs NFT d'autres plateformes

- Pas besoin de stockage coûteux sur la blockchain
- Pas besoin d'IPFS, une extension du réseau Lightning (appelée Bifrost) est utilisée à la place (et elle est entièrement chiffrée de bout en bout)
- Pas besoin d'une solution de gestion de données spéciale - encore une fois, Bifrost prend ce rôle
- Pas besoin de faire confiance aux sites web pour maintenir les données des jetons NFT ou des actifs / ABI de contrat
- Cryptage DRM intégré et gestion de la propriété
- Infrastructure de sauvegarde utilisant le réseau Lightning (Bifrost)
- Moyens de monétiser le contenu (non seulement la vente du NFT lui-même, mais aussi l'accès au contenu, plusieurs fois)

## Conclusions

Depuis le lancement de Bitcoin, il y a près de 13 ans, il y a eu beaucoup de recherches et d'expérimentations dans ce domaine, les succès et les erreurs nous ont permis de comprendre un peu mieux le comportement des systèmes décentralisés dans la pratique, ce qui les rend vraiment décentralisés et quelles actions tendent à les mener vers la centralisation. Tout cela nous a conduit à conclure que la véritable décentralisation est un phénomène rare et difficile à atteindre, la véritable décentralisation n'a été réalisée que par Bitcoin et c'est pour cette raison que nous concentrons nos efforts pour construire dessus.

RGB a son propre terrier dans le terrier du lapin Bitcoin, pendant que je tombe à travers eux, je posterai ce que j'ai appris, dans le prochain article, nous aurons une introduction aux nœuds LNP et RGB et comment les utiliser.

- 1 https://plan99.net/~mike/satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md

- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md

# Tutoriel RGB-node

## Introduction

Dans ce tutoriel, nous expliquons comment utiliser RGB-node pour créer un jeton fongible et comment le transférer. Ce document est basé sur la démo RGB-node et diffère en ce sens que ce tutoriel utilise de vraies données de testnet et pour cela, nous devons construire notre propre transaction Bitcoin partiellement signée (PSBT), psbt à partir de maintenant.

Francisco Calderón publié le
1er mars 2022
https://grunch.dev/blog/rgbnode-tutorial/

## Exigences

L'utilisation d'une distribution Linux est recommandée, ce tutoriel a été écrit en utilisant Pop!/\_OS, qui est basé sur Ubuntu et vous aurez besoin de :

- cargo
- Bitcoin core
- git

Note : Ce tutoriel montre l'exécution de commandes dans un terminal Linux, pour différencier ce que l'utilisateur écrit et la réponse qu'il obtient dans le terminal, nous incluons le symbole $ symbolisant l'invite de commande bash.

Vous devrez installer certaines dépendances :

```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```

Compilation et exécution

RGB-node est en cours de développement (WIP), c'est pourquoi nous devons nous positionner sur un commit spécifique (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) pour pouvoir le compiler et l'utiliser correctement, pour cela nous exécutons les commandes suivantes.

```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```

Maintenant nous le compilons, n'oubliez pas d'utiliser le drapeau --locked car il y a un changement majeur introduit dans une version de clap.

```
$ cargo install --path . --all-features --locked

....
....
    Finished release [optimized] target(s) in 2m 14s
  Installing /home/user/.cargo/bin/fungibled
  Installing /home/user/.cargo/bin/rgb-cli
  Installing /home/user/.cargo/bin/rgbd
  Installing /home/user/.cargo/bin/stashd
   Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```

Comme le compilateur Rust nous l'indique, les binaires ont été copiés dans le répertoire $HOME/.cargo/bin, si votre compilateur les a copiés ailleurs, vous devez vous assurer que ce répertoire est inclus dans $PATH.

Parmi les binaires installés, nous pouvons voir trois démons ou services (les fichiers se terminant par d) et une interface en ligne de commande (cli), le cli nous permet d'interagir avec le démon principal rgbd. Comme dans ce tutoriel nous allons exécuter deux nœuds, nous aurons également besoin de deux clients, chacun doit se connecter à son propre nœud, pour cela nous créons deux alias.

```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```

Nous pouvons simplement exécuter les alias ou les ajouter à la fin du fichier $HOME/.bashrc et exécuter source $HOME/.bashrc.
Prémisse

RGB-node ne gère aucune fonctionnalité liée au portefeuille, il effectue simplement des tâches spécifiques à RGB sur les données qui seront fournies par un portefeuille externe tel que bitcoin core. En particulier, pour démontrer un flux de travail de base avec l'émission et le transfert, nous aurons besoin de :

- Un issuance_utxo auquel rgb-node-0 liera l'actif nouvellement émis
- Un receive_utxo où rgb-node-1 reçoit l'actif
- Un change_utxo où rgb-node-0 reçoit le changement d'actif
- Une transaction bitcoin partiellement signée (tx.psbt), dont la clé publique de sortie sera ajustée pour inclure un engagement de transfert.
  Nous utiliserons le bitcoin core cli, nous devons avoir le démon bitcoind en cours d'exécution sur testnet, cela nous donnera une interopérabilité et à la fin nous pourrons envoyer nos propres actifs à d'autres utilisateurs RGB qui ont suivi ce tutoriel.
  Pour simplifier, nous ajouterons cet alias à la fin de notre fichier ~/.bashrc.

```
alias bcli="bitcoin-cli -testnet"
```

Listons nos transactions de sortie non dépensées et en sélectionnons deux, l'une sera l'issuance_utxo et l'autre change_utxo, peu importe lequel est lequel, l'important est que l'émetteur ait le contrôle de ces deux UTXO.

```
$ bcli listunspent
[
  {
    "txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
    "vout": 1,
    "address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
    "label": "",
    "scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
    "amount": 0.01703963,
    "confirmations": 62432,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
    "safe": true
  },
  {
    "txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
    "vout": 1,
    "address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
    "scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
    "amount": 0.02877504,
    "confirmations": 189184,
    "spendable": true,
    "solvable": true,
    "desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
    "safe": true
  }
]
```

Avant d'aller plus loin, nous devons parler des outpoints, une seule transaction peut inclure plusieurs sorties, l'outpoint comprend à la fois un TXID de 32 octets et un numéro d'index de sortie de 4 octets (vout) pour faire référence à une sortie spécifique séparée par un deux-points :. Dans notre sortie de listunspent, nous pouvons trouver deux UTXOs, sur chacun nous pouvons voir txid et vout, ce sont les outpoints issuance_utxo et change_utxo.
'receive_utxo' est un UTXO contrôlé par le destinataire, dans ce cas, nous utiliserons e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 qui est un outpoint d'un autre portefeuille.

- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Nous allons maintenant créer une transaction partiellement signée (tx.psbt) dont la sortie sera ajustée pour inclure un engagement de transfert, n'oubliez pas de remplacer le txid et le vout par les vôtres, l'adresse de destination n'a pas vraiment d'importance, elle peut être la vôtre ou celle d'une autre personne, peu importe où vont ces sats, ce qui importe, c'est que nous utilisions issuance_utxo.

```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
  "psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
  "fee": 0.00000280,
  "changepos": 0'
```

L'extrait nous a donné un psbt encodé en base64 que nous utiliserons pour créer tx.psbt.

```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```

Créons un nouveau répertoire appelé rgbdata dans lequel les répertoires de données de chaque nœud sont stockés.

```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```

Déjà situé dans $HOME/rgbdata, nous démarrons chaque nœud dans des terminaux différents, où ~/.cargo/bin est le répertoire où cargo a copié tous les binaires après l'installation de rgb-node.

```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```

## Émission

Pour émettre un actif, nous exécutons rgb0-cli avec les sous-commandes d'émission fongible, puis les arguments, le ticker USDT, le nom "USD Tether" et dans l'allocation, nous utiliserons le montant d'émission et l'issuance_utxo comme indiqué ci-dessous :

```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```

Actif émis avec succès. Utilisez ces informations pour le partage :
Informations sur l'actif :

```
'genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
  - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    amount: 1000
    origin: ~
knownInflation: {}
knownAllocations:
  - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    index: 0
    outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
    revealedAmount:
      value: 1000
      blinding: "0000000000000000000000000000000000000000000000000000000000000001"'
```

Nous obtenons l'assetId, nous en avons besoin pour transférer l'actif.

```
$ rgb0-cli fungible list

- name: USD Tether
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```

## Générer une UTXO aveuglée

Afin de recevoir les nouveaux USDT, rgb-node-1 doit générer une UTXO aveuglée correspondant à receive_utxo pour contenir l'actif.

```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Outpoint aveuglé : utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Secret d'aveuglement de l'outpoint : 1679197189805229975
```

Pour pouvoir accepter les transferts liés à cette UTXO, nous aurons besoin de la receive_utxo originale et du blinding_factor.

## Transfert

Pour transférer une certaine quantité de l'actif à rgb-node-1, nous devons l'envoyer à l'UTXO aveuglée, rgb-node-0 doit créer un envoi et une divulgation, et le valider dans une transaction bitcoin. Ensuite, nous aurons besoin d'un psbt que nous modifierons pour inclure l'engagement. De plus, les options -i et -a nous permettent de fournir un outpoint d'entrée qui serait l'origine de l'actif et une allocation où nous recevrons la monnaie rendue, nous devons l'indiquer de la manière suivante @<change_utxo>.

```
'$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
Le transfert a réussi, les envois et les divulgations sont écrits dans "consignment.rgb" et "disclosure.rgb", la transaction de témoin partiellement signée dans "witness.psbt"'
Données de consignation à partager : consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e'
```

Cela écrira trois nouveaux fichiers, consignment, disclosure et le psbt incluant le tweak, ce psbt est appelé transaction témoin, la consignment est envoyée à rgb-node-1.

## Témoin

La transaction témoin doit être signée et diffusée, pour cela nous devons l'encoder en base64.

```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```

Signez-le avec la sous-commande walletprocesspsbt.

```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="{'
'"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",  "complete": true
}
```

Maintenant finalisez-le et obtenez l'hexadécimal.

```
'$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="{
  "hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
  "complete": true
}
```

## Diffuser

Diffusez-le en utilisant la sous-commande sendrawtransaction pour le faire confirmer dans la blockchain.

```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```

## Accepter

Pour accepter un transfert entrant, rgb-node-1 doit avoir reçu le fichier de consignation de rgb-node-0, avoir le receive_utxo et le blinding_factor correspondant généré lors de la génération de l'UTXO de brouillage.

```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Transfert d'actif accepté avec succès.
```

Nous pouvons maintenant voir (dans le champ knownAllocations) la nouvelle allocation de 100 unités d'actif dans <receive_utxo> en exécutant :

```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT'
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
  amount: 1000
  origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
  index: 0
  outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
  revealedAmount:
    value: 1000
    blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
  index: 1
  outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
  revealedAmount:
    value: 100
    blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0

Since receive_utxo was blinded when the transfer was made, the payer rgb-node-0 has no information about where the 100 USDT was sent, so the location is not shown in knownAllocations.

$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0'
'id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6  ticker: USDT
  name: USD Tether
  description: ~
  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```

Mais comme vous pouvez le voir, rgb-node-0 ne peut pas voir le changement d'actif de 900 que nous avons fourni à la commande de transfert avec l'argument -a. Pour enregistrer le changement, rgb-node-0 doit accepter la divulgation.

```
$ rgb0-cli fungible enclose disclosure.rgb

Données de divulgation correctement incluses.
```

Si rgb-node-0 a réussi, vous pouvez voir le changement en listant l'actif.

```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
  name: USD Tether'
'description: ~  knownCirculating: 1000
  isIssuedKnown: ~
  issueLimit: 0
  chain: testnet
  decimalPrecision: 0
  date: "2022-02-23T20:53:26"
  knownIssues:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      amount: 1000
      origin: ~
  knownInflation: {}
  knownAllocations:
    - nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      index: 0
      outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      revealedAmount:
        value: 1000
        blinding: "0000000000000000000000000000000000000000000000000000000000000001"
    - nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      index: 0
      outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
      revealedAmount:
        value: 900
        blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```

## Conclusions

Nous avons pu créer un actif fongible et le déplacer d'une transaction à une autre de manière privée. Si nous vérifions la transaction confirmée dans un explorateur de blocs, nous ne trouverions rien de différent d'une transaction normale, cela est dû au fait que RGB utilise des scellés à usage unique pour ajuster les transactions. Dans cet article, je présente une introduction à la façon dont RGB fonctionne.

Cet article peut contenir des bugs, si vous en trouvez, veuillez me le faire savoir pour améliorer ce guide. Les suggestions et les critiques sont également les bienvenues, joyeux piratage ! 🖖

> Guide proposé par Franscisco : grunch@getalby.com
> https://twitter.com/negrunch
> https://grunch.dev/blog/rgbnode-tutorial/'
