---
name: Construire avec les éléments et le réseau liquide
goal: Apprendre à utiliser et à développer avec la plateforme blockchain open-source Elements et ses principales caractéristiques
objectives: 

  - Comprendre les concepts fondamentaux de la plateforme blockchain Elements et des sidechains Liquid.
  - Apprenez à configurer et à faire fonctionner les nœuds Elements pour les configurations autonomes et les chaînes latérales.
  - Acquérir une expérience pratique de la signature de blocs fédérés et du Federated 2-Way Peg.
  - Mettre en place et gérer des environnements blockchain sécurisés et efficaces pour des cas d'utilisation réels.

---
# S'appuyer sur les liquides et les éléments

Découvrez les fonctionnalités avancées de Liquid et d'Elements, et apprenez à utiliser efficacement ces outils pour améliorer vos projets de développement. Cette formation fournit une base théorique et pratique complète, vous permettant de maîtriser des fonctionnalités telles que les transactions confidentielles, les actifs émis et la signature de blocs fédérés.

Liquid, basé sur le cadre Elements, est conçu pour améliorer la confidentialité, l'évolutivité et la fonctionnalité des solutions financières et techniques. Dans ce cours, vous acquerrez une expérience pratique de l'émission et de la gestion d'actifs, du Federated 2-Way Peg et de l'utilisation d'outils tels que elementsd et elements-cli, ce qui vous permettra de créer des solutions innovantes adaptées à vos besoins.

Ce cours est adapté aux développeurs de tous niveaux d'expérience. Les débutants et les utilisateurs intermédiaires trouveront des explications accessibles et des exemples pratiques, tandis que les utilisateurs avancés pourront approfondir les détails techniques et les fonctionnalités moins connues de Liquid et Elements.

Rejoignez-nous pour améliorer vos compétences, libérer le plein potentiel de Liquid et d'Elements, et créer des outils percutants pour l'avenir de l'innovation Liquid.

+++
# Introduction

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Introduction aux cours

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

![Video](https://youtu.be/gkQfnwYLyI0?si=H6cIPhgZaSAwHaHI)

L'objectif de l'Académie Elements est de présenter et d'expliquer les concepts clés d'Elements, la plateforme open-source sur laquelle Liquid est construit. À la fin du cours, vous devriez avoir une bonne compréhension des principales caractéristiques d'Elements, telles que les transactions confidentielles et les actifs émis, ainsi que des processus impliqués dans le fonctionnement d'Elements Core.

Chaque section comprend des leçons avec un texte explicatif et une vidéo qui se termine par un quiz. Le nombre de questions dépend de la taille du sujet précédent. La section 10 résumera le contenu du cours et se terminera par un quiz plus important.

Toute question, demande d'information complémentaire ou interrogation sur les réponses du quiz peut être adressée à votre professeur James Dorfman.

## Aperçu des éléments

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

![Video](https://youtu.be/ns-JLGdkNig?si=fmWye_boRSvVF1Bt)

Elements est une plateforme blockchain open source, compatible avec la sidechain, qui donne accès à de puissantes fonctionnalités développées par les membres de la communauté, telles que les transactions confidentielles et les actifs émis.

Elements est, à la base, un protocole qui permet de former un consensus autour de l'historique des transactions et des règles qui régissent le transfert et la création d'actifs stockés dans un grand livre distribué de la blockchain.

De plus amples informations sur Elements sont disponibles sur le site web du projet Elements (https://elementsproject.org/), sur le blog officiel de Liquid (https://blog.liquid.net/) et sur le portail des développeurs (https://liquid.net/devs).

### Éléments

Lancé en 2015, Elements réduit les coûts de développement et de recherche internes et exploite la toute dernière technologie blockchain, ouvrant de nombreux nouveaux cas d'utilisation pour la mise en œuvre. Une blockchain basée sur Elements peut fonctionner comme une blockchain autonome ou être rattachée à une autre et fonctionner comme une Sidechain. L'exécution d'Elements en tant que Sidechain permet de transférer des actifs de manière vérifiable entre différentes blockchains.

Construit sur la base du code Bitcoin et l'étendant, il permet aux développeurs familiarisés avec l'API Bitcoind de créer rapidement et à moindre coût des blockchains fonctionnelles et de tester des projets de validation de concept. Le fait d'être construit sur la base du code Bitcoin permet également à Elements de fonctionner comme un banc d'essai pour les changements apportés au protocole Bitcoin lui-même.

Quelques-unes des principales caractéristiques d'Elements sont énumérées ci-dessous.

#### Transactions confidentielles

Par défaut, toutes les adresses d'Elements sont masquées à l'aide des transactions confidentielles. L'aveuglement est le processus par lequel le montant et le type d'actif transféré sont cryptographiquement cachés à tout le monde, sauf aux participants et à ceux à qui ils choisissent de révéler la clé d'aveuglement.

#### Actifs émis

Les actifs émis sur les éléments permettent d'émettre et de transférer plusieurs types d'actifs entre les participants au réseau. Un actif émis bénéficie également de transactions confidentielles et peut être réémis ou détruit par toute personne détenant le jeton de réémission correspondant.

#### Piquet à 2 voies fédéré

Elements est une plateforme blockchain à usage général qui peut également être "rattachée" à une blockchain existante (telle que Bitcoin) afin de permettre le transfert bidirectionnel d'actifs d'une chaîne à l'autre. La mise en œuvre d'Elements en tant que sidechain vous permet de contourner certaines des propriétés inhérentes à la chaîne principale, tout en conservant un bon niveau de sécurité fourni par les actifs sécurisés sur la chaîne principale.

#### Blocs signés

Elements utilise une fédération forte de signataires, appelés signataires de blocs, qui signent et créent des blocs de manière fiable et opportune. Cela supprime la latence de transaction du processus minier PoW, qui est sujet à une grande variance de temps de bloc en raison de sa distribution aléatoire de poisson. Le processus de signature de blocs fédérés permet de créer des blocs fiables sans qu'il soit nécessaire de recourir à la confiance d'un tiers ou à l'exploitation minière basée sur un algorithme de calcul.

Elements ajoute toutes ces fonctionnalités à la base de code Bitcoin Core, étendant la capacité du protocole de la chaîne principale et permettant de nouveaux cas d'utilisation commerciale lorsqu'ils sont déployés en tant que chaîne latérale ou en tant que solution de chaîne de blocs autonome.

# Élément

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Fonctionnement d'Elements

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

![Video](https://youtu.be/v0lzmfH81AY?si=V-xDWfmDLKyBcdPs)

Elements apporte une solution technique aux problèmes auxquels les utilisateurs de la blockchain sont confrontés quotidiennement : latence des transactions, manque de confidentialité et risque de fongibilité.

Elements surmonte ces problèmes grâce à l'utilisation de la signature par blocs fédérés et des transactions confidentielles.

Contrairement au réseau Bitcoin, le processus de signature des blocs au sein d'Elements ne repose pas sur les signatures multipartites à adhésion dynamique (DMMS) et la preuve de travail (PoW). Au lieu de cela, Elements utilise une Fédération forte de signataires, appelés signataires de blocs, qui peuvent signer et créer des blocs de manière fiable et opportune. Cela permet d'éliminer la latence de transaction du processus d'extraction de la preuve de travail, qui est sujet à une grande variance de temps de bloc en raison de sa distribution aléatoire de poisson. Le processus de signature de blocs fédérés permet de créer des blocs fiables sans qu'il soit nécessaire de faire confiance à une tierce partie.

Elements peut fonctionner en tant que sidechain d'une autre blockchain, telle que Bitcoin, ou en tant que blockchain autonome ne dépendant pas d'autres réseaux.

Lorsqu'elle est utilisée comme sidechain, la Strong Federation contient également des membres qui permettent le transfert sécurisé et contrôlé d'actifs entre une chaîne principale et une sidechain Elements. Le transfert contrôlé d'actifs est appelé Federated 2-Way Peg et les membres qui jouent le rôle de transfert d'actifs sont appelés Watchmen.

Les processus impliqués dans le fonctionnement d'un réseau Éléments et les rôles des participants au réseau sont importants pour comprendre le fonctionnement d'Éléments.

Qu'il soit implémenté en tant que sidechain ou blockchain autonome, Elements utilise des fédérations fortes de signataires de blocs pour produire des blocs.

### Des fédérations fortes

Elements utilise un modèle de consensus proposé pour la première fois par Blockstream, appelé Strong Federations. Une fédération forte n'a pas besoin de preuve de travail (PoW) et s'appuie plutôt sur les actions collectives d'un groupe de participants qui se méfient les uns des autres, appelés fonctionnaires.

Les rôles qu'un fonctionnaire peut remplir au sein d'une Fédération forte sont les suivants : Les signataires de blocs et les gardiens. Les signataires de blocs sont nécessaires si vous exécutez les éléments en mode sidechain ou blockchain autonome, tandis que les gardiens ne sont nécessaires que dans une configuration sidechain.

Les actions qu'un membre d'une fédération forte peut effectuer sont réparties entre deux rôles distincts afin de renforcer la sécurité et de limiter les dommages qu'un attaquant peut causer.

Combinés, les rôles de ces participants permettent à Elements d'offrir à la fois une création rapide de blocs (confirmation plus rapide et définitive des transactions) et des actifs garantis et transférables (actifs rattachés directement liés à une autre blockchain).

Vous pouvez lire le livre blanc sur les fédérations fortes ici : https://blockstream.com/strong-federations.pdf

### Signataires en bloc

Une blockchain comme celle de Bitcoin est étendue lorsque toute personne faisant partie d'un groupe dynamique de signataires de blocs étend la chaîne en apportant la preuve du travail effectué. La nature dynamique de l'ensemble introduit les problèmes de latence inhérents à ces systèmes.

En utilisant un ensemble fixe de signataires, un modèle fédéré remplace l'ensemble dynamique par un ensemble connu, un schéma multi-signature. La réduction du nombre de participants nécessaires pour étendre la blockchain augmente la vitesse et l'évolutivité du système, tandis que la validation par toutes les parties garantit l'intégrité de l'historique des transactions.

La signature fédérée de blocs se compose de plusieurs phases :


- Étape 1 - Les signataires de blocs proposent des blocs candidats à tous les autres signataires de blocs participants.
- Étape 2 - Chaque signataire de bloc signale son intention en s'engageant à signer le bloc candidat donné.
- Étape 3 - Si le seuil d'engagement préalable est atteint, chaque signataire de bloc signe le bloc.
- Étape 4 - Si le seuil de signature (qui peut être différent de celui de l'étape 3) est atteint, le bloc est accepté et envoyé au réseau. La Fédération forte est parvenue à un consensus sur le dernier bloc de transactions.
- Étape 5 - Le bloc suivant est alors proposé par le signataire de bloc suivant dans la ronde et le processus se répète.

Étant donné que la génération de blocs d'une fédération forte n'est pas probabiliste et qu'elle est basée sur un ensemble fixe de signataires, elle ne sera jamais sujette à des réorganisations multi-blocs. Cela permet de réduire considérablement le temps d'attente associé à la confirmation des transactions. Il supprime également l'incitation à miner pour le profit (c'est-à-dire les récompenses de bloc) et la remplace par une incitation à participer de manière productive à un réseau où tous les participants ont le même objectif commun : veiller à ce que le réseau continue à fonctionner d'une manière qui soit bénéfique pour tous. Cela se fait sans introduire de point de défaillance unique ni d'exigences plus élevées en matière de confiance.

### Elements as a Sidechain - Watchmen et le Peg à deux voies fédéré

Lorsqu'ils sont gérés comme une sidechain, certains membres de la Strong Federation ont un rôle supplémentaire à remplir, celui des Watchmen. Les Watchmen sont responsables du transfert des actifs dans et hors d'une Elements sidechain, processus connus sous le nom de `Peg-In` et `Peg-Out`.

Pour qu'une sidechain fonctionne de manière fiable, elle doit permettre aux participants de vérifier que l'offre d'actifs est contrôlée et vérifiable. Une blockchain Elements utilise un Peg fédéré à deux voies pour permettre le transfert bidirectionnel d'actifs à l'intérieur et à l'extérieur d'une blockchain Elements. Cela répond aux exigences d'émission prouvable et de transferts inter-chaînes.

La fonction Federated 2-way Peg permet à un actif d'être interopérable avec d'autres blockchains et d'être représentatif de l'actif natif d'une autre blockchain. En associant votre blockchain à une autre, vous pouvez étendre les capacités de la chaîne principale et surmonter certaines de ses limites inhérentes.

À un niveau élevé, les transferts dans la sidechain se produisent lorsque quelqu'un envoie des actifs de la chaîne principale à une adresse contrôlée par un portefeuille Watchmen à signatures multiples. Cela a pour effet de geler les actifs sur la chaîne principale. Watchmen valide alors la transaction et libère le même montant de l'actif associé dans la sidechain. Les actifs libérés sont envoyés à un portefeuille de la sidechain qui peut prouver qu'il revendique les actifs originaux de la mainchain. Ce processus permet de déplacer les actifs de la chaîne principale vers la chaîne secondaire.

Afin de transférer des actifs vers la chaîne principale, un utilisateur effectue une transaction spéciale de retrait sur la chaîne secondaire. Cette transaction est vérifiée par les Watchmen, qui signent ensuite une dépense de transaction à partir du portefeuille multi-signature qu'ils contrôlent sur la chaîne principale. Un nombre seuil de participants à la fédération doit signer pour que la transaction sur la chaîne principale devienne valide. Lorsque les Watchmen renvoient un actif sur la chaîne principale, ils détruisent également le montant correspondant sur la chaîne secondaire, transférant ainsi efficacement les actifs entre les chaînes de blocs.

## Mise en place et fonctionnement des éléments

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

![Video](https://youtu.be/Frr_OjTEPAM?si=iq5XonJyQk8S5OAu)

Comme Elements est basé sur la base de code de Bitcoin, les éléments qui constituent un réseau fonctionnel sont très similaires.

Le logiciel du nœud Elements lui-même s'appelle `elementsd` et fonctionne comme un démon sur la machine de l'utilisateur. Un démon (ou service dans Windows) est un programme qui fonctionne en arrière-plan sans nécessiter le contrôle direct d'un utilisateur connecté.

Note : Dans ce document, nous ferons toujours référence à elementsd comme étant la version démon, mais tout peut être fait avec elements-qt, à condition que l'option serveur soit activée.

Le démon Elements se connecte à d'autres nœuds du réseau afin d'échanger des données sur les transactions et les blocs, de valider et d'étendre sa copie locale de la chaîne de blocs du réseau.

Le logiciel Elements comprend également un programme client appelé `elements-cli` qui vous permet d'envoyer des commandes RPC (Remote Procedure Call) à elementsd à partir de la ligne de commande. Cela peut être utilisé pour demander le solde d'un portefeuille, voir les données de transaction ou de bloc ou diffuser une transaction par exemple. Cette configuration devrait être familière à tous ceux qui ont utilisé les équivalents Bitcoin : bitcoind et bitcoin-cli.

Comme un nœud Elements peut être configuré en passant des paramètres au démarrage ou via un fichier de configuration, il est possible d'avoir plus d'une instance fonctionnant sur la même machine. Chaque nœud Elements possède sa propre copie des données de la blockchain, gère son propre pool de transactions valides non confirmées et écoute les requêtes RPC sur différents ports.

### Le dépôt de code des éléments et la communauté

Elements est un projet open-source dont le code source est disponible dans le dépôt GitHub Elements à l'adresse https://github.com/ElementsProject/elements. Ce dépôt contient les sources des programmes elementsd et elements-cli, ainsi que des outils d'installation et de construction, une suite de tests et une documentation didactique.

Pour compléter le dépôt de code, il y a aussi le site web https://elementsproject.org, une ressource axée sur la communauté qui contient des explications sur ce qu'est Elements, comment il fonctionne et une section de tutoriel complète. Le tutoriel se concentre sur l'apprentissage d'Elements en suivant des exemples en ligne de commande et vous montre comment construire des applications web et de bureau simples à partir d'Elements. Le site répertorie également les forums de discussion populaires de la communauté Elements et est lui-même hébergé sur GitHub, ce qui permet à la communauté de contribuer au contenu du site.

Afin d'exécuter Elements sur votre machine, vous devrez d'abord cloner (télécharger une copie) le code source, installer toutes les dépendances du code et enfin construire les exécutables démon et client. Le logiciel Elements est alors prêt à être configuré et exécuté.

## Configuration des nœuds et du réseau

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

Les paramètres de configuration peuvent être transmis à un nœud d'éléments au démarrage afin de modifier la façon dont il fonctionne, valide les données, se connecte à d'autres nœuds et initialise ses données de blockchain.

Les paramètres sont soit chargés à partir du fichier `elements.conf` désigné, soit passés en tant que paramètres via la ligne de commande.

Certains éléments peuvent être modifiés à l'aide de ces paramètres :


- Le nom de l'actif par défaut utilisé dans les implémentations d'une blockchain autonome.
- Le numéro de l'actif initial créé.
- L'actif à utiliser pour payer les frais de transaction sur le réseau.
- L'emplacement de stockage des fichiers de données de la blockchain.
- Les informations d'identification RPC utilisées pour se connecter à un nœud Bitcoin.
- Le seuil `n de m` à respecter et les clés publiques valides qui peuvent signer les blocs.
- Le script qui doit être satisfait afin de transférer des actifs dans et hors d'une sidechain.
- Connexion ou non à un nœud Bitcoin en tant que sidechain.

Beaucoup d'entre eux font partie des règles de consensus du réseau, il est donc important qu'ils soient appliqués à tous les nœuds au démarrage. Certains peuvent être modifiés après l'initialisation d'une chaîne, mais d'autres doivent être corrigés après avoir été utilisés pour initialiser une chaîne.

L'utilisation des paramètres sera abordée plus loin dans le cours, au fur et à mesure qu'ils se rapportent à chaque section.

### Opérations de base à l'aide de la ligne de commande

Ce cours montre des exemples qui utilisent le programme `elements-cli` pour faire des appels RPC à un ou plusieurs noeuds Elements. Cela se fait à partir d'une session de terminal et afin de rendre les commandes plus brèves, un `alias` sera utilisé. Par cette convention, lorsque vous verrez quelque chose comme les commandes suivantes :

```bash
e1-dae
e1-cli getnewaddress
```

Les `e1-dae` et `e1-cli` sont en fait un raccourci typographique qui utilise la fonction `alias` du terminal. Les `e1-dae` et `e1-cli` seront en fait remplacés lors de l'exécution de la commande et la commande qui s'exécutera sera similaire à :

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

Ce que nous voyons ci-dessus est un appel au démarrage du démon Elements et un appel aux programmes elements-cli situés dans le répertoire `$HOME/elements/src` et une valeur pour le paramètre `datadir`. Le paramètre `datadir` nous permet d'indiquer aux instances du démon et du client où se trouvent leurs fichiers de configuration et, dans le cas du démon, où stocker sa copie de la blockchain. Comme ils partagent un fichier de configuration, le client pourra faire des appels RPC au démon.

En exécutant à nouveau la commande ci-dessus, mais avec une valeur `datadir` différente, nous pouvons démarrer plus d'une instance d'Elements, chacune avec sa propre copie de la blockchain et des paramètres de configuration. Par cette convention, nous utiliserons les alias `e2-dae` et `e2-cli` dans le cours pour faire référence à un répertoire datadir différent de celui de e1. Donc l'exemple ci-dessus pour notre seconde instance `e2` serait :

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

Cela nous permettra d'effectuer toutes sortes d'opérations telles que la transaction d'actifs entre les nœuds, l'émission d'actifs et la vérification de l'utilisation de l'aveuglement dans les transactions confidentielles entre les différents nœuds d'un même réseau.

# Utilisation de l'élément Cas d'utilisation pratique

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Transactions confidentielles

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

![Video](https://youtu.be/-by2xBtXQeE?si=7bLo_geGn3qh7MXN)

Dans cette section, vous apprendrez à utiliser la fonction Transactions confidentielles d'Elements.

Toutes les adresses d'Elements sont, par défaut, masquées à l'aide de transactions confidentielles, qui rendent le montant et le type d'actifs transférés visibles uniquement aux participants à la transaction (et à ceux à qui ils choisissent de révéler la clé de masquage), tout en garantissant cryptographiquement qu'il n'est pas possible de dépenser plus de pièces qu'il n'y en a de disponibles.

### Adresses et transactions confidentielles

Par défaut, lorsque vous créez une nouvelle adresse dans Elements à l'aide de la commande `getnewaddress`, elle est créée en tant qu'adresse confidentielle.

Afin de démontrer la nature confidentielle des transactions, nous allons demander à e2 de s'envoyer des fonds, puis d'essayer de voir la transaction depuis e1. Cela démontrera la nature confidentielle des transactions dans Elements.

Chaque nouvelle adresse générée par un nœud d'éléments est confidentielle par défaut. Nous pouvons le démontrer en demandant à e2 de générer une nouvelle adresse.

```
e2-cli getnewaddress
```

Notez que l'adresse commence par e1. Il s'agit donc d'une adresse confidentielle. Un examen plus approfondi de l'adresse à l'aide de la commande getaddressinfo permet d'obtenir plus de détails sur l'adresse.

```
e2-cli getaddressinfo <address>
```

Vous pouvez voir qu'il existe une propriété confidential_key qui nous indique qu'il s'agit d'une adresse confidentielle.

La clé confidentielle est la clé publique aveuglante, qui est ajoutée à l'adresse confidentielle elle-même. C'est la raison pour laquelle une adresse confidentielle est si longue.

Une adresse non confidentielle lui est également associée. Si vous souhaitez utiliser des transactions régulières et non confidentielles au sein d'Elements, les actifs doivent être envoyés à cette adresse plutôt qu'à celle portant le préfixe lq1.

Nous pouvons maintenant demander à e2 d'envoyer des fonds à l'adresse qu'il a générée. Cela montrera plus tard que e1, n'étant pas l'une des parties à la transaction, ne sera pas en mesure de voir les détails de la transaction.

```
e2-cli sendtoaddress <address>
```

Notez l'identifiant de la transaction. Confirmez la transaction.

```
e2-cli -generate 101
```

L'examen de la transaction par laquelle e2 s'est envoyé des fonds à lui-même se fait du point de vue de e2 lui-même.

```
e2-cli gettransaction <txid>
```

En faisant défiler les détails de la transaction, vous pouvez voir que e2 peut afficher les montants envoyés et reçus ainsi que l'actif transigé. Vous pouvez également voir les propriétés amountblinder et assetblinder, qui sont utilisées pour masquer les détails aux autres nœuds non impliqués dans la transaction.

Pour vérifier les détails de la même transaction à partir de e1, nous devons d'abord obtenir les détails bruts de la transaction.

```
e1-cli getrawtransaction <txid>
```

Cela renvoie les détails de la transaction brute. Si vous regardez dans la section vout, vous pouvez voir qu'il y a trois instances. Les deux premières instances sont les montants de réception et de modification, et la troisième est la commission de transaction. De ces trois montants, les frais sont les seuls pour lesquels vous pouvez voir une valeur, étant donné que les frais eux-mêmes sont toujours non masqués dans Elements.

### Clés aveuglantes

Les deux premières sections de la vout sont des "fourchettes aveugles" des montants en valeur et des données d'engagement qui servent de preuve du montant et du type d'actif réellement échangé.

Même si nous importions la clé privée de e2 dans le portefeuille de e1, ce dernier ne serait toujours pas en mesure de voir les montants et le type d'actifs échangés, car il n'a toujours pas connaissance de la clé d'aveuglement utilisée par e2. Nous allons le prouver en important la clé privée utilisée par le portefeuille de e2 dans celui de e1. Tout d'abord, nous devons exporter la clé de e2

```
e2-cli dumpprivkey <address>
```

Puis l'importer dans e1.

```
e1-cli importprivkey <privkey>
```

Nous pouvons maintenant prouver que e1 ne peut toujours pas voir les valeurs.

```
e1-cli gettransaction <txid>
```

En effet, il affiche 0 comme quantité de tx alors qu'il s'agit en fait de 1.

Pour pouvoir voir la valeur réelle, non lissée, nous avons besoin de la clé d'aveuglement. Pour ce faire, nous devons d'abord exporter la clé d'aveuglement de e2.

```
e2-cli dumpblindingkey <address>
```

Puis l'importer dans e1.

```
e1-cli importblindingkey <address> <blinding key>
```

Maintenant, lorsque nous obtenons les détails de la transaction de e1.

```
e1-cli gettransaction <txid>
```

Cela montre qu'avec l'importation de la clé aveugle, nous pouvons maintenant voir la valeur réelle de 1 dans la transaction.

Dans cette section, nous avons vu que l'utilisation d'une clé de blocage permet de masquer le montant et le type d'actifs d'une transaction et qu'en important la bonne clé de blocage, il est possible de révéler ces valeurs. Dans la pratique, une clé de masquage peut, par exemple, être remise à un auditeur, s'il est nécessaire de vérifier les montants et les types d'actifs détenus par une partie. La fonction "transactions confidentielles" d'Elements permet également d'effectuer des "preuves de fourchette". Ces preuves permettent de prouver qu'un montant d'actif est détenu dans une fourchette donnée, sans qu'il soit nécessaire d'exposer le montant réel lui-même.

Nous avons également vu que les transactions confidentielles sont facultatives, mais qu'elles sont activées par défaut lorsqu'une nouvelle adresse est générée.

C'est tout pour cette leçon ; bonne chance pour le quiz et à la prochaine !

## Actifs émis

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

![Video](https://youtu.be/XnY4WZUNSs4?si=dG8I5OoSh_0EBdvL)

Dans cette section, vous apprendrez à utiliser la fonction "Issued Assets" d'Elements.

Les actifs émis permettent d'émettre et de transférer plusieurs types d'actifs entre les participants au réseau Elements. Tout nœud du réseau peut émettre ses propres actifs. Les émissions peuvent représenter la propriété fongible de n'importe quel actif, y compris des bons, des coupons, des devises, des dépôts, des obligations, des actions, etc. Issued Assets ouvre la voie à la construction d'échanges sans confiance, d'options et d'autres contrats intelligents avancés impliquant des actifs auto-émis.

Un actif émis bénéficie également de transactions confidentielles et peut être réémis par toute personne détenant le jeton associé.

La première étape consiste à accéder à deux nœuds Elements, que nous appellerons e1 et e2. Les blockchains de ces nœuds ont été réinitialisées et l'actif par défaut a été réparti entre eux.

Les deux nœuds se trouvent sur le même réseau local et sont connectés l'un à l'autre. Ils partagent donc les mêmes transactions dans leur mempool de transactions et des blockchains identiques. Bien qu'ils fonctionnent sur la même machine, il convient de noter qu'ils ne partagent pas les mêmes fichiers de blockchain. Chaque nœud gère sa propre copie locale de la blockchain, qui contient le même historique de transactions parce qu'ils sont en consensus et adhèrent aux mêmes règles de protocole les uns que les autres.

Commençons par vérifier la vision qu'a chaque nœud des émissions d'actifs existantes sur le réseau.

Cette opération s'effectue à l'aide de la commande listissuances.

```
e1-cli listissuances
e2-cli listissuances
```

Comme vous pouvez le constater, les deux nœuds présentent le même historique d'émission. Ils affichent tous deux un actif, l'émission initiale de 21 millions de bitcoins qui ont été créés lors de l'initialisation de la chaîne. Vous pouvez voir l'identifiant hexadécimal de l'actif dans les résultats de l'exécution de la commande ci-dessus, ainsi que l'étiquette attribuée à l'actif, qui est "bitcoin".

Il est intéressant de noter que l'élément par défaut reçoit toujours une étiquette lors de l'initialisation de la chaîne. Lorsque vous créez vos propres ressources, vous pouvez leur attribuer des étiquettes, ce que nous allons faire dans quelques instants. Avant de pouvoir le faire, nous devons créer notre propre ressource.

Nous allons demander à e1 d'émettre le nouveau bien. Cela se fait à l'aide de la commande issueasset.

```
e1-cli issueasset 100 1 false
```

`issueasset` accepte 3 paramètres.

Le montant du nouvel actif à émettre, nous avons choisi 100. La quantité de jetons à créer (les jetons sont utilisés pour réémettre des quantités d'un actif), nous avons choisi 1. Le dernier paramètre indique à Elements de créer l'émission d'actifs en aveugle ou non. Nous utiliserons unblinded car nous voulons voir les montants d'émission de e2 dans une minute, nous entrerons donc false.

L'exécution de la commande renvoie des données sur l'émission. Il s'agit notamment de l'identifiant de la transaction, dont vous pouvez faire une copie pour une utilisation ultérieure, de la valeur hexagonale unique de l'actif et de la valeur hexagonale unique du jeton de l'actif.

Générer un bloc pour confirmer la transaction d'émission.

```
e1-cli -generate 1
```

Exécutez à nouveau la commande `listissuances` sur e1.

```
e1-cli listissuances
```

Cela nous montre que e1 est maintenant au courant de 2 émissions, l'émission initiale de Bitcoin et notre nouvel actif émis, dont nous pouvons voir 100 exemplaires. Notez la valeur hexadécimale du nouvel actif et le fait qu'il n'y a pas d'étiquette d'actif associée, comme c'est le cas pour l'émission de bitcoins.

Vérifiez à nouveau la liste des émissions connues de l'e2.

```
e2-cli listissuances
```

Cela nous montre que e2 n'est pas au courant de l'émission d'actifs effectuée par e1. Il ne peut voir que l'émission initiale de bitcoins qu'il pouvait déjà voir.

En effet, e2 ignore et ne surveille pas l'adresse à laquelle le nouveau bien a été envoyé lorsqu'il a été émis par e1.

Il convient de noter que même si e2 ne peut pas voir l'émission elle-même, e1 peut toujours envoyer à e2 une partie de l'actif. Le nouvel actif apparaîtrait alors comme un solde disponible dans le portefeuille de e2, même s'il n'est pas au courant de l'émission initiale.

Pour permettre à e2 de voir la délivrance effective (et donc le montant délivré), nous devons ajouter l'adresse à e2 en tant qu'adresse surveillée.

Pour ce faire, nous devons trouver l'adresse à laquelle l'actif a été envoyé. Pour cela, nous utiliserons l'identifiant de la transaction que nous avons copié plus tôt et nous demanderons à e1 de récupérer les détails de cette transaction afin que nous puissions trouver l'adresse correcte à ajouter à la liste de surveillance du portefeuille de e2.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

En faisant défiler l'hexagone des données de la transaction, vous verrez l'adresse qui a reçu 100 de notre nouvel actif, identifiée par sa valeur hexagonale.

Prenez l'adresse et copiez-la pour que nous puissions l'importer dans e2.

Importons maintenant cette adresse dans e2. Pour ce faire, nous utilisons la commande importaddress.

```
e2-cli importaddress <the-issued-to-address>
```

Vérifions maintenant la liste des émissions de e2.

```
e2-cli listissuances
```

Vous pouvez voir que notre actif nouvellement émis est maintenant inclus dans la liste. Le nœud e2 est également en mesure de déterminer le montant de l'actif qui a été émis, ainsi que le montant du jeton associé, car l'émission était une émission non masquée. Pour activer l'utilisation de la correspondance entre l'ID de l'actif et le nom dans Elements, arrêtez d'abord Elements.

```
e1-cli stop
```

Redémarrez-le ensuite avec un paramètre supplémentaire qui associe l'hexagone d'un bien à l'étiquette fournie. Cela permet au nœud d'afficher des données sur l'actif dans un format plus lisible par l'homme. Vous pouvez ajouter ce paramètre à la fin de elements.conf si vous préférez, vous n'aurez alors pas besoin d'ajouter l'argument au démon à chaque fois que vous le démarrez. Par exemple :

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

Mais nous utiliserons ici la méthode de l'argument.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Interroger à nouveau le nœud pour obtenir une liste d'émissions.

```
e1-cli listissuances
```

Cela nous montre que la correspondance entre la valeur hexadécimale de l'actif et son étiquette fonctionne. Nous vérifions à nouveau la liste des émissions du nœud e2.

```
e2-cli listissuances
```

Vous pouvez voir que le nœud e2 n'a pas accès à cette étiquette, car les étiquettes ne sont disponibles que pour le nœud qui les a définies. En effet, nous pouvons attribuer un label différent au même hexagone d'actif sur e2 que nous l'avons fait sur e1. Arrêtez d'abord le noeud e2.

```
e2-cli stop
```

Redémarrer avec une étiquette différente attribuée à l'hexagone de notre nouvel actif.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Liste des émissions de l'e2.

```
e2-cli listissuances
```

Les étiquettes des biens sont locales à chaque nœud, seul l'hexagone du bien est reconnu par les autres nœuds du réseau.

La correspondance entre l'étiquette et l'hexagone de l'actif est utile lors de l'exécution d'actions telles que les transactions et les requêtes sur le solde du portefeuille, car elle permet de faire référence à un actif de manière abrégée. Par exemple, si nous voulions envoyer une partie de notre nouvel actif (un montant de 10) de e1 à e2 sans utiliser le label.

Nous devons d'abord obtenir une adresse à laquelle envoyer l'actif.

```
e2-cli getnewaddress
```

Utilisez ensuite la commande sendtoaddress.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Confirmer la transaction en générant un bloc.

```
generate 1
```

Vérification de la réception de l'actif sur e2.

```
e2-cli getwalletinfo
```

Nous pouvons constater que l'actif a bien été reçu.

Notez que l'application e2 associe l'hexagone du poste reçu et l'affiche à l'aide de son propre libellé. Un moyen plus simple de faire la même chose serait d'utiliser l'étiquette du poste e1 lors de l'envoi.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

En coulisses, Elements fait correspondre les étiquettes locales à des valeurs hexagonales afin de simplifier l'utilisation des ressources émises.

Dans cette section, nous avons vu comment émettre et étiqueter des actifs. Dans la section suivante, nous verrons comment réémettre et détruire des quantités d'un actif émis.

## Réémission d'actifs

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

![Video](https://youtu.be/5em79YHtYk0?si=rhponm6Hw9AB6RJp)

Dans cette section, vous apprendrez comment émettre davantage d'un actif déjà émis et comment détruire une quantité donnée d'un actif émis.

La nécessité de réémettre (créer plus) un actif ou de détruire un montant de l'actif est susceptible de se produire lorsque l'actif représente quelque chose qui n'a pas d'approvisionnement fixe. Cela peut s'appliquer à des actifs représentant de l'or détenu dans un coffre-fort par exemple ; lorsque des unités d'or entrent et sortent du coffre-fort, l'actif représentant l'offre du coffre-fort doit être ajusté à la hausse ou à la baisse en conséquence.

La réémission d'une quantité d'un actif nécessite la possession du jeton associé qui a été créé en même temps que l'actif lors de son émission initiale.

Lors de la création de nouvelles quantités d'un actif, le nœud qui a émis l'actif en premier lieu n'a pas d'importance, tant que le nœud qui réémet une quantité d'un actif est en possession de ce qui est communément appelé le jeton de réémission de l'actif. Nous verrons comment créer initialement le jeton de réémission, comment l'utiliser pour réémettre un montant d'actif et comment transférer le jeton de réémission à d'autres nœuds, afin qu'ils aient également la permission de réémettre l'actif.

Nous aurons besoin d'accéder à deux nœuds Elements, que nous appellerons e1 et e2. Les blockchains de ces nœuds ont été réinitialisées et l'actif par défaut a été réparti entre eux.

Nous allons demander à e1 d'émettre un montant de 100 d'un nouvel actif et de créer 1 jeton de réémission pour ce même actif. Pour simplifier l'exemple, nous allons créer l'émission à l'aveugle. Nous allons donc procéder à l'émission de l'actif et du jeton de réémission qui lui est associé.

```
e1-cli issueasset 100 1 false
```

Notez l'identifiant de l'actif et celui du jeton (de réémission).

Comme nous réémettrons plus tard d'autres actifs à partir d'e2, nous devrons prendre note de l'ID de la transaction dans laquelle l'actif a été émis et l'utiliser pour importer l'adresse à laquelle l'actif a été envoyé.

Confirmer la transaction.

```
e1-cli -generate 1
```

Nous allons maintenant vérifier les détails de la transaction à l'aide de la commande gettransaction :

```
e1-cli gettransaction <txid>
```

En faisant défiler l'hexagone des données de la transaction, vous verrez que, dans la transaction, e1 a reçu 1 jeton de réémission et 100 de l'actif associé.

Faites une copie de l'adresse pour que nous puissions l'importer dans e2.

Et maintenant, importation de l'adresse dans le portefeuille de e2.

```
e2-cli importaddress <address>
```

Nous pouvons maintenant constater que e1 et e2 sont tous deux au courant de l'émission d'actifs.

```
e1-cli listissuances
e2-cli listissuances
```

Actuellement, e1 détient un montant de l'actif et le jeton de réémission 1, mais pas e2.

```
e1-cli getwalletinfo
```

Notez également que e1 possède moins d'actifs par défaut qu'auparavant, car il a payé un petit montant pour couvrir les frais de transaction. Ce montant doit être perçu par e1 lorsque le bloc créé arrive à maturité à plus de 100 blocs de profondeur.

```
e2-cli getwalletinfo
```

Comme e1 détient le jeton de réémission, il peut en réémettre d'autres. Pour ce faire, il utilise la commande reissueasset. Demandons à e1 de réémettre 100 autres exemplaires de l'actif.

```
e1-cli reissueasset <asset-id> 100
```

La vérification de la réémission a fonctionné.

```
e1-cli getwalletinfo
```

Vous pouvez voir que e1 détient maintenant 200 de l'actif, comme prévu.

Comme e2 ne détient pas de jeton de réémission, ils recevront une erreur s'ils essaient de réémettre l'actif.

```
e2-cli reissueasset <asset-id> 100
```

Notez le message d'erreur.

Nous pouvons voir les détails de la réémission de e1 en utilisant la commande listissuances.

```
e1-cli listissuances
```

Notez l'indicateur `is_reissuance`.

Si nous envoyons maintenant à e2 une quantité de jetons de réémission, ils pourront réémettre eux-mêmes une quantité de l'actif. Nous avons d'abord besoin d'une adresse pour l'envoyer. Il convient de noter que le jeton de réémission est traité de la même manière que tout autre actif au sein d'elements lors de l'envoi et de l'affichage des soldes et qu'il peut également être décomposé en plus petites dénominations comme tout autre actif, de sorte qu'il n'est pas nécessaire d'envoyer le jeton de réémission à e2 pour qu'il puisse réémettre l'actif. N'importe quelle dénomination suffira. Générer une adresse pour e2 afin qu'il reçoive le jeton de réémission.

```
e2-cli getnewaddress
```

Envoyez ensuite une fraction du RIT de e1 à e2.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confirmer la transaction.

```
e1-cli -generate 1
```

Nous pouvons maintenant voir que e2 détient les 0,1 qui lui ont été envoyés.

```
e2-cli getwalletinfo
```

Cela signifie que e2 peut maintenant réémettre une plus grande quantité de l'actif associé au RIT qu'il détient dans son portefeuille. Nous allons demander à e2 de réémettre 500 de l'actif.

```
e2-cli reissueasset <asset-id> 500
```

Vérifier le résultat de la réémission.

```
e2-cli getwalletinfo
```

Vous pouvez voir que e2 détient maintenant le montant réémis dans le solde de son portefeuille et que le RIT lui-même n'est pas consommé dans le processus de réémission de l'actif.

La destruction d'une quantité d'un actif est quelque chose que toute personne détenant au moins la quantité détruite peut faire, elle n'est pas régie par le jeton de réémission.

```
e2-cli destroyamount <asset-id>
e2-cli getwalletinfo
```

Dans cette section, nous avons vu comment émettre un actif et comment utiliser le jeton de réémission qui est optionnellement créé dans le cadre de l'émission d'un actif. Nous avons également vu que le transfert d'un jeton de réémission est aussi simple que le transfert de n'importe quel autre actif, et que la détention d'un jeton de réémission, quelle qu'en soit la quantité, confère à son détenteur le droit d'émettre davantage d'actifs associés. Il est donc très important de contrôler qui a accès aux jetons de réémission dans votre réseau. Nous avons également vu comment détruire une quantité d'un actif et que ce processus n'est pas contrôlé par la possession du jeton de réémission.

# Fédération des éléments

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Signature en bloc

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

![Video](https://youtu.be/kxWX91fCnus?si=KItm_Am3_RrBcLBN)

Elements prend en charge un modèle de signature fédérée qui vous permet de spécifier le nombre de membres de la fédération forte qui doivent signer un bloc proposé afin de produire un bloc valide.

Auparavant, et pour faciliter l'exemple, nous avons créé des blocs à l'aide de la commande `generate`, qui n'avait pas besoin de satisfaire à une exigence de multi-signature pour que les blocs créés soient acceptés par le réseau comme étant valides.

Nous allons configurer nos nœuds pour qu'ils exigent la création de blocs multisignes 2 sur 2. Cette configuration se fera à l'aide du paramètre signblockscript, qui peut être ajouté au fichier de configuration ou transmis au nœud lors de son démarrage. Afin d'initialiser une chaîne avec ce paramètre, nous devons d'abord construire le script qui la compose.

Nous allons le faire en utilisant certains nœuds existants, en sauvegardant les données qu'ils produisent, puis en effaçant la chaîne afin de pouvoir la redémarrer à l'aide de notre paramètre signblockscript. Ce paramètre est nécessaire car le script fait partie des règles de consensus du réseau et doit être défini lors de l'initialisation de la chaîne. Il ne peut pas être ajouté ultérieurement à une chaîne déjà existante.

Nous aurons besoin d'accéder à deux nœuds Elements, que nous appellerons e1 et e2. Les blockchains de ces nœuds ont été réinitialisées et l'actif par défaut a été réparti entre eux.

Assurez-vous que le paramètre con_max_block_sig_size est fixé à une valeur élevée dans votre fichier elements.conf, faute de quoi la signature en bloc échouera dans la suite de cette section. Nous avons défini con_max_block_sig_size=2000 pour ce tutoriel.

Comme nous allons réinitialiser notre blockchain et effacer les portefeuilles associés à e1 et e2, nous devrons prendre une copie des adresses, des clés publiques et des clés privées que nous utilisons pour générer le script de signature de bloc afin de pouvoir les utiliser plus tard.

Tout d'abord, chacun des nœuds de signature des blocs doit générer une nouvelle adresse, dont vous devez faire une copie.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Nous devons ensuite extraire les clés publiques des adresses et les noter en vue d'une utilisation ultérieure.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Nous extrayons ensuite les clés privées, que nous réimporterons plus tard afin que les nœuds puissent signer les blocs après avoir réinitialisé notre blockchain et les données du portefeuille.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Nous devons maintenant générer un script de rédemption avec une exigence de multi-signature 2 sur 2. Pour ce faire, nous utilisons la commande createmultisig, nous passons le premier paramètre à 2 et nous fournissons deux clés publiques. Ce sont ces clés que la propriété doit prouver plus tard lorsque le bloc est créé.

L'un ou l'autre des nœuds, e1 ou e2, peut générer le multisig.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

Nous obtenons ainsi notre redeemscript, que vous pouvez copier pour l'utiliser ultérieurement.

Nous devons maintenant effacer les données existantes de la blockchain et du portefeuille afin de pouvoir recommencer avec le nouveau script signblockscript dans le cadre des règles de consensus de la chaîne. C'est pourquoi nous avons dû faire une copie de certaines données plus tôt, comme les clés privées qui seront utilisées dans la nouvelle chaîne pour signer les blocs. Vous devez le faire avant de continuer.

Avec notre portefeuille existant et les données de la chaîne supprimées, nous pouvons maintenant démarrer nos nœuds et leur demander d'initialiser une nouvelle chaîne en utilisant le paramètre signblockscript. Passons -evbparams=dynafed:0:: : pour désactiver l'activation de dynafed, car nous n'avons pas besoin de cette fonctionnalité avancée pour cet exemple.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Nous devons maintenant importer les clés privées que nous avons enregistrées précédemment afin que nos nœuds puissent signer et aider à compléter les blocs proposés.

```
e1-cli importprivkey <e1-priv-key>
e2-cli importprivkey <e2-priv-key>
```

L'utilisation de la commande generate devrait maintenant provoquer une erreur, car elle ne respecte pas les règles de signature de bloc désormais appliquées par nos nœuds.

```
e1-cli -generate 1
```

Pour proposer un nouveau bloc, chaque nœud peut appeler la commande getnewblockhex. Cette commande renvoie l'hexagone d'un nouveau bloc qui devra être signé avant d'être accepté par les nœuds du réseau.

```
e1-cli getnewblockhex
```

Rappelez-vous que la commande ne fait que créer un bloc proposé, elle n'en génère pas.

Pour confirmer cela, nous pouvons voir qu'il n'y a actuellement aucun bloc dans notre blockchain.

```
e1-cli getblockcount
```

Si nous essayons de soumettre le bloc hexagonal sans le signer au préalable.

```
e1-cli submitblock <block-hex>
```

Nous recevons un message nous indiquant que la preuve de bloc n'est pas valide. Cela est dû au fait qu'elle n'a pas encore été signée par deux des deux parties requises.

Nous allons donc demander à e1 de signer le bloc proposé.

```
e1-cli signblock <block-hex>
```

Faire signer l'hexagone par e2.

```
e2-cli signblock <block-hex>
```

Remarquez que e2 ne signe pas la sortie créée par e1 qui signe le bloc proposé. Les deux signent l'hexagone du bloc proposé indépendamment des résultats de l'un et de l'autre.

Nous devons maintenant combiner les signatures de bloc de e1 et e2. L'un ou l'autre nœud peut le faire, tout ce dont il a besoin est l'hexagone de bloc signé de l'autre nœud.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

Vous pouvez voir que la commande combineblocksigs produit l'hexagone du bloc signé ainsi qu'un état complet, indiquant que l'hexagone du bloc est prêt à être soumis.

Maintenant, n'importe quel nœud peut soumettre l'hexagone de bloc complété. Nous allons demander à e1 de le faire.

```
e1-cli submitblock <combined-signed-hex>
```

Vérification de la validité de la soumission.

```
e1-cli getblockcount
e2-cli getblockcount
```

Vous pouvez voir que e1 et e2 ont tous deux accepté le bloc comme valide et l'ont ajouté à l'extrémité de leurs copies locales de la blockchain.

Pour résumer le processus. Dans cette section, nous avons :


- Proposition d'un bloc.
- Il l'a fait signer par chaque nœud.
- Combiner les signatures.
- Vérification que les signatures sont valides et respectent le seuil de redémarrage de la chaîne.
- Soumis le bloc.

Chaque nœud du réseau valide le bloc et l'ajoute à sa copie locale de la blockchain.

### Blocage de l'information

Bien que le processus semble complexe au départ, la séquence de signature des blocs dans Elements est toujours la même et la configuration initiale ne doit être effectuée qu'une seule fois :

1. Configuration initiale (effectuée une fois)

2. Une adresse multi-signature est créée, appelée `signblockscript`, en utilisant les clés publiques des Federated Block Signers.

3. Le script de rachat est utilisé pour démarrer une nouvelle blockchain.

4. Production de blocs (en cours)

5. Les blocs proposés sont générés et échangés pour signature.

Une fois qu'un nombre seuil de signataires a signé le bloc proposé, celui-ci est combiné et soumis au réseau. S'il répond aux critères du `signblockscript` de la chaîne, les nœuds l'acceptent en tant que bloc valide.

## Élément en tant que chaîne latérale

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

![Video](https://youtu.be/egYzj4N8CB8?si=v7_-IXsjHPE-ARDe)

Elements est une plateforme blockchain open-source à usage général qui peut également être "rattachée" à une blockchain existante, telle que Bitcoin. Lorsqu'il est rattaché à une autre blockchain, on dit qu'Elements fonctionne comme une "sidechain". Les sidechains permettent le transfert bidirectionnel d'actifs d'une chaîne à l'autre. La mise en œuvre d'Elements en tant que sidechain vous permet de contourner certaines des limites inhérentes à la chaîne principale, tout en conservant un bon niveau de sécurité fourni par les actifs sécurisés sur la chaîne principale.

Alors qu'une sidechain a connaissance de la mainchain et de l'historique de ses transactions, la mainchain n'a aucune connaissance de la sidechain et aucune n'est nécessaire à son fonctionnement. Cela permet aux sidechains d'innover sans restrictions ni délais associés aux propositions d'amélioration du protocole de la mainchain. Plutôt que d'essayer de le modifier directement, l'extension du protocole principal permet à la chaîne principale elle-même de rester sécurisée et spécialisée, ce qui sous-tend le bon fonctionnement de la chaîne secondaire.

En étendant les fonctionnalités de Bitcoin et en tirant parti de sa sécurité sous-jacente, une sidechain basée sur Elements est en mesure d'offrir de nouvelles fonctionnalités qui n'étaient pas disponibles auparavant pour les utilisateurs de la mainchain. Liquid Network est un exemple de sidechain basée sur Elements et utilisée en production.

Afin d'initialiser une blockchain Elements en tant que sidechain, nous devons utiliser le paramètre de script federated peg. Ce paramètre peut être défini dans le fichier de configuration d'un nœud ou transmis au démarrage.

Le script du peg fédéré définit quels membres de la fédération forte peuvent effectuer des fonctions de peg-in et de peg-out. Ces fonctionnaires sont appelés "veilleurs", car ils surveillent la chaîne principale et la chaîne secondaire à la recherche de transactions valides de peg-in et de peg-out, et les exécutent si elles sont valides. Le terme "peg-out" signifie que l'on fait sortir des actifs de la sidechain vers la mainchain et le terme "peg-in" signifie que l'on fait entrer des actifs dans la sidechain à partir de la mainchain. Lorsque nous disons "move into the sidechain", nous voulons dire que les fonds sont bloqués dans une adresse multi-signature sur la mainchain et qu'un montant correspondant de l'actif est créé sur la sidechain Elements. Lorsque nous disons "sortir de la sidechain", nous voulons dire que les actifs sont détruits sur la sidechain d'Elements et que le montant correspondant est libéré des fonds bloqués détenus sur la mainchain. L'autorisation d'exécuter les fonctions de peg-in et de peg-out exige que les fonctionnaires prouvent qu'ils possèdent les clés publiques utilisées dans le script de peg fédéré. Cela se fait par l'utilisation des clés privées correspondantes.

Pour créer un script de chevilles fédérées, nous devons donc d'abord faire en sorte que chacun de nos nœuds génère une clé publique. Nous devons également stocker les clés privées associées pour une utilisation ultérieure, car nous devrons effacer toutes les données de la chaîne existante et initialiser une nouvelle chaîne à l'aide du script federated peg. En effet, le script federated peg fait partie des règles de consensus d'une sidechain, et il ne peut pas être appliqué à une blockchain existante, non pegée, à une date ultérieure.

Générons donc une adresse avec chacun de nos nœuds, stockons les données pertinentes pour une utilisation ultérieure et générons le script federated peg que nous utiliserons pour initialiser notre sidechain plus tard.

Tout d'abord, chacun de nos nœuds, qui joueront le rôle de gardien dans notre réseau, doit générer une nouvelle adresse.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Nous validons ensuite l'adresse pour obtenir les clés publiques.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Il récupère ensuite les clés privées associées à chaque adresse.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Stocker les clés privée et publique pour une utilisation ultérieure.

Nous devons maintenant effacer la blockchain existante et les données du portefeuille car nous allons initialiser une nouvelle chaîne à l'aide d'un script de peg fédéré. Vous pouvez le faire maintenant. N'oubliez pas de démarrer le démon Bitcoin, dont nous aurons besoin pour le peg-in.

Nous pouvons maintenant initialiser une nouvelle chaîne avec un script de peg fédéré créé à l'aide des clés publiques que nous avons stockées plus tôt. Les nombres que nous entrons et qui entourent nos clés publiques définissent et délimitent le nombre de clés utilisées, et la propriété de la clé qui doit être prouvée afin d'entrer et de sortir de notre sidechain.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Nous allons maintenant importer les clés privées que nous avons sauvegardées précédemment, afin que nos nœuds puissent ensuite signer et compléter le transfert d'actifs entre les chaînes et satisfaire aux exigences du script du peg fédéré.

```
e1-cli importprivkey <priv-key-1>
e2-cli importprivkey <priv-key-1>
```

Nous devons maintenant faire mûrir certains blocs sur les deux chaînes. La maturité des blocs est une exigence du processus de rattachement, car elle protège contre les réorganisations de blocs sur la chaîne principale conduisant à une inflation de l'offre d'actifs rattachés dans la chaîne secondaire.

Pour que cette section reste centrée sur le peg fédéré, nous allons générer des blocs sans utiliser le modèle de signature des blocs que nous avons étudié dans la dernière section, et revenir à l'utilisation de la commande "generate" pour créer de nouveaux blocs.

```
b-cli generate 101
e1-cli generate 1
```

Nous n'avons pas nécessairement besoin de générer des blocs maintenant pour les éléments. Mais générons-en tout de même un. C'est une bonne pratique pour éviter les incohérences potentielles.

Notre chaîne est maintenant prête à être connectée. Pour ce faire, nous devons générer une adresse spéciale à l'aide de la commande getpeginaddress. Notez que la durée entre la génération d'une adresse de rattachement avec getpeginaddress et sa revendication avec claimpegin doit être aussi courte que possible. Les adresses de rattachement ne sont pas durables à long terme et ne doivent pas être réutilisées.

```
e1-cli getpeginaddress
```

Vous pouvez voir que la commande crée une nouvelle adresse mainchain, ainsi qu'un nouveau script qui devra être satisfait afin de réclamer les fonds peg-in. L'adresse de la chaîne principale est une adresse `pay to script hash` qui sera utilisée par les fonctionnaires jouant le rôle de Watchmen au sein du réseau Elements.

Comme getnewaddress, getpeginaddress ajoute un nouveau secret au portefeuille du nœud appelant. Il est donc important de prévoir une sauvegarde du fichier du portefeuille dans votre processus de gestion des nœuds.

Nous allons maintenant envoyer quelques bitcoins de la mainchain vers la sidechain. Notre portefeuille de test de régression de la chaîne principale contient déjà des fonds.

```
b-cli getwalletinfo
```

Nous pouvons voir que le portefeuille contient 50 bitcoins. Nous allons envoyer un bitcoin de la chaîne principale à la chaîne secondaire. Nous devons envoyer des fonds à l'adresse de la chaîne principale que notre nœud a générée plus tôt.

```
b-cli sendtoaddress <e1-pegin-address>
```

Nous devons conserver l'identifiant de cette transaction, car nous en aurons besoin ultérieurement pour prouver le financement.

Nous pouvons maintenant voir que le solde du portefeuille de la chaîne principale a diminué du montant que nous avons envoyé, plus un petit montant supplémentaire pour couvrir les frais de transaction.

```
b-cli getwalletinfo
```

Nous devons à nouveau faire mûrir la transaction.

```
b-cli generate 101
```

Pour que notre nœud Elements puisse réclamer les fonds de peg-in, nous devons obtenir la "preuve" que la transaction de peg-in a été effectuée. La preuve cryptographique utilise l'identifiant de la transaction de financement pour calculer le chemin de Merkel et prouve que la transaction est présente dans un bloc confirmé.

```
b-cli gettxoutproof '["<tx-id>"]'
```

Nous avons également besoin des données brutes des transactions.

```
b-cli getrawtransaction <tx-id>
```

Avec la preuve et les données brutes de la transaction de rattachement, notre nœud d'éléments peut maintenant réclamer le rattachement à l'aide de la transaction brute et de la preuve de la transaction.

```
e1-cli claimpegin <raw> <proof>
```

Notez qu'il existe un troisième argument optionnel que nous aurions pu fournir à claimpegin. Ce troisième paramètre peut être utilisé pour spécifier l'adresse de la sidechain à laquelle envoyer les fonds réclamés. Cela n'était pas nécessaire dans notre exemple car nous avons appelé la commande depuis le même nœud que celui qui possède l'adresse à laquelle les fonds réclamés sont envoyés.

Vérification du solde de e1.

```
e1-cli getwalletinfo
```

Générer un bloc pour confirmer la demande.

```
e1-cli generate 1
```

Vérification du solde de e1.

```
e1-cli getwalletinfo
```

Nous constatons que la demande d'insertion a été acceptée.

Pour le peg-out, le processus est similaire. Une adresse est générée, des fonds lui sont envoyés et les fonds sont libérés si la transaction est valide. Nous ne couvrirons pas l'ensemble du processus de peg-out car il implique un travail sur la chaîne principale qui dépasse le cadre de ce cours. Les étapes en termes d'événements Elements sont les suivantes : une adresse est générée sur la chaîne principale.

```
b-cli getnewaddress
```

Les fonds sont envoyés à l'adresse de la chaîne principale à partir d'un nœud d'éléments à l'aide de la commande sendtomainchain.

```
e1-cli sendtomainchain <new-address> 1
```

Génération d'un bloc pour confirmer la transaction.

```
e1-cli generate 1
```

Vérifier le solde du portefeuille du nœud.

```
e1-cli getwalletinfo
```

Et voyez que le solde a diminué.

Dans cette section, nous avons vu comment


- Générer un script de peg fédéré.
- Initialiser une nouvelle chaîne qui utilise le script comme règle de paramètre de consensus du réseau.
- Envoyer des fonds de la mainchain vers la sidechain.
- Réclamer les fonds dans la sidechain Elements.
- Comprendre comment l'envoi de fonds à la chaîne principale est lancé.

### FederatedPegScript

Afin de permettre à Elements de fonctionner comme une sidechain, le bloc genesis dans sa blockchain doit être créé avec un `fedpegscript` en place. Cela se fait en passant le paramètre `fedpegscript` au démarrage du nœud. Le script fera alors partie des règles de consensus de la blockchain Elements et permettra aux demandes de peg-in et de peg-out d'être validées et prises en compte.

Le `fedpegscript` est composé de clés publiques contrôlées par les personnes autorisées à effectuer les actions du peg. L'exemple suivant montre le format d'un fedpegscript multisignature 2 sur 2 :

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Note : Les caractères à l'extérieur des clés publiques sont des délimiteurs qui indiquent les exigences en matière de clé publique et de "n de m". Par exemple, le modèle pour un fedpegscript 1 de 1 serait '5121<clé publique 1>51ae'.

### Piquetage

Avant qu'un peg-in puisse être accepté par une sidechain Elements, il doit avoir suffisamment de confirmations sur la mainchain. Cela est nécessaire pour éviter une inflation de l'offre de l'actif rattaché sur la sidechain Elements, qui pourrait être causée par une réorganisation de la mainchain.

De brèves réorganisations de la pointe de la blockchain Bitcoin sont attendues dans le cadre du fonctionnement normal du mécanisme de consensus de la preuve de travail (PoW). Ainsi, Elements n'accepte un peg-in comme valide que lorsqu'il a une profondeur suffisante dans la blockchain Bitcoin. Cela permet d'éviter qu'Elements n'accepte le même peg-in plus d'une fois.

### Sortie de secours

Un peg-out se produit lorsqu'un nœud Elements appelle la commande `sendtomainchain`, qui prend en entrée une adresse mainchain (la destination du peg-out) ainsi que le montant de l'actif rattaché qui doit être "retiré". Cela crée une transaction de peg-out sur la sidechain. Une fois que les Fonctionnaires qui agissent en tant que Watchmen détectent que la transaction de peg-out a été confirmée sur la sidechain, ils s'occupent de libérer l'actif sur la mainchain vers la destination de peg-out, comme nous l'avons appris dans les sections précédentes du cours.

## Les éléments en tant que blockchain autonome

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

![Video](https://youtu.be/u-3rV7DGtD0?si=G1__H0Uelf4sTUDM)

Jusqu'à présent, nous avons vu comment faire fonctionner Elements en tant que sidechain. Cependant, il peut également fonctionner comme une solution blockchain autonome avec son propre actif natif par défaut. Dans cette configuration, une blockchain Elements conserve toutes les caractéristiques d'une implémentation sidechain, telles que les transactions confidentielles et les actifs émis, mais n'a pas besoin de peg-in ou peg-out pour ajouter ou supprimer des montants d'actifs par défaut de la circulation.

Dans cette section, nous allons

Initialiser une nouvelle blockchain Elements avec un actif par défaut nommé `newasset`.

Spécifiez 1 000 000 `newasset` à créer ainsi que 2 tokens de réémission pour celui-ci.

Réclamez toutes les pièces "newasset" que vous pouvez dépenser.

Réclamer tous les jetons de réémission "tout le monde peut dépenser" pour "newasset".

Envoyer le bien et son jeton de réémission au portefeuille d'un autre nœud.

Réémettre plus de "newasset" à partir des deux nœuds.

Afin d'initialiser un réseau Elements pour qu'il fonctionne comme une blockchain autonome, chaque nœud doit être démarré avec certains paramètres de base. Ils sont utilisés pour indiquer au nœud de ne pas essayer de valider les peg-ins d'une autre blockchain, le nom de l'actif par défaut du réseau et le montant de l'actif par défaut et du jeton de réémission associé à créer.

Nous allons démarrer une nouvelle chaîne en utilisant ces paramètres sur nos deux nœuds Elements connectés. Nous nommerons l'actif par défaut `newasset` et émettrons un million d'entre eux ainsi que deux jetons de réémission `newasset`.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Notez que les montants utilisés ici correspondent à la plus petite dénomination que le réseau peut accepter, de sorte que les deux cents millions de jetons de réémission correspondent en fait à deux jetons entiers. Il en va de même pour la dénomination des pièces gratuites initiales.

Vérifier les soldes actuels des portefeuilles de nos nœuds.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Nous constatons que l'initialisation s'est déroulée correctement.

Lorsque l'émission initiale d'actifs est créée en tant que "tout le monde peut dépenser", nous demanderons à e1 de les réclamer tous afin de supprimer l'accès d'e2 à ces actifs.

```
e1-cli getnewaddress
e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Notez qu'il n'est pas nécessaire de spécifier "newasset" comme actif à envoyer puisqu'il s'agit déjà de l'actif par défaut, et donc également de l'actif par défaut utilisé pour payer les frais de réseau.

Dans Elements, vous pouvez envoyer plusieurs types d'actifs à la même adresse. Nous pouvons donc réutiliser l'adresse que nous venons de générer pour recevoir l'actif par défaut et l'utiliser comme adresse de destination pour les jetons de réémission.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confirmer les transactions.

```
e1-cli generate 101
```

Nous allons vérifier que e1 est le seul détenteur de l'actif et de son jeton de réémission.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Ce qui, nous le constatons, est effectivement le cas.

Nous allons maintenant envoyer une partie du "newasset" à e2, qui détient actuellement un solde de zéro.

```
e2-cli getnewaddress
e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Notez que nous n'avons pas eu à spécifier le type d'actif à envoyer, car `newasset` a été créé en tant qu'actif par défaut du réseau

Envoyons également quelques tokens de réémission pour `newasset` à e2.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confirmer les transactions.

```
e1-cli generate 101
```

Nous pouvons vérifier que les portefeuilles ont été mis à jour en conséquence.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Nous allons maintenant réémettre certains des actifs par défaut de e1. Notez que la possibilité de faire cela est activée par le paramètre de démarrage initialreissuancetokens. S'il est omis ou fixé à zéro, il en résultera un actif par défaut qui ne pourra pas être réémis à une date ultérieure.

```
e1-cli reissueasset newasset 100
```

Nous avons pu utiliser le label `newasset` au lieu d'avoir à fournir la valeur hexadécimale parce qu'une chaîne d'éléments étiquette toujours son asset par défaut.

Vérification du fonctionnement de la réémission de l'actif par défaut :

```
e1-cli generate 101
e1-cli getwalletinfo
```

Nous allons maintenant prouver que parce que e2 détient certains des jetons de réémission `newasset`, il peut également réémettre l'actif par défaut.

```
e2-cli reissueasset newasset 100
```

Vérification que la réémission de l'actif par défaut par e2 a fonctionné.

```
e2-cli generate 101
e2-cli getwalletinfo
```

Dans cette section, nous avons mis en place Elements en tant que blockchain autonome et vérifié que les fonctionnalités de base fonctionnent comme prévu.

Nous avons utilisé les paramètres de démarrage pour :

Initialiser une nouvelle blockchain Elements avec un actif par défaut nommé "newasset".

Indiquer le montant de l'actif par défaut à créer lors de l'initialisation de la chaîne.

Créer des jetons de réémission pour l'actif par défaut et réémettre d'autres jetons de l'actif par défaut à partir des deux nœuds.

Sur notre réseau autonome de blockchain Elements, toutes les autres opérations transactionnelles fonctionneront de la même manière que les exemples couverts dans les sections principales du cours, mais utiliseront "newasset" au lieu de "bitcoin" comme actif par défaut et payant.

### Paramètres de démarrage du nœud et d'initialisation de la chaîne

Pour qu'un nœud Elements fonctionne comme une blockchain autonome, quelques paramètres doivent être utilisés conjointement. Nous allons examiner chacun d'entre eux et découvrir ce qu'ils font.

#### `validatepegin=0`

Comme une blockchain autonome n'a pas besoin de valider les transactions peg-in ou peg-out, nous devons désactiver ces vérifications. Avec ce paramètre, vous n'avez pas besoin d'exécuter le logiciel client Bitcoin ni de stocker une copie de la blockchain Bitcoin, car le réseau Elements fonctionnera de manière indépendante.

#### `defaultpeggedassetname` (nom de l'actif par défaut)

Cela vous permet de spécifier le nom de l'actif par défaut créé lors de l'initialisation de la blockchain.

#### `initialfreecoins`

Le nombre (équivalent à l'unité Satoshi de Bitcoin) de l'actif par défaut à créer.

#### jetons d'émission initiale

Le nombre (équivalent à l'unité Satoshi de Bitcoin) de jetons de réémission pour l'actif par défaut à créer. Sans cette valeur, il serait impossible de créer d'autres actifs par défaut. Si vous ne souhaitez pas qu'il soit possible de créer d'autres actifs par défaut, cette valeur peut être fixée à zéro ou omise.

En utilisant ces paramètres, la procédure commune de démarrage d'un nœud ressemblerait à ce qui suit :

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Opérations de base

Le paramètre `defaultpeggedassetname` applique un label à l'actif par défaut. Sans ce paramètre, l'actif par défaut sera automatiquement nommé `bitcoin`. Dans les sections précédentes, lorsque nous envoyons des assets que nous avons émis nous-mêmes à un autre noeud, nous devons spécifier soit l'hexagone de l'asset, soit le label de l'asset appliqué localement pour indiquer à Elements quel asset nous envoyons. Comme `defaultpeggedassetname` s'applique à tous les noeuds, nous n'avons pas besoin de le nommer lorsque nous l'envoyons, même si son nom n'est pas `bitcoin`. Chaque fonction qui aurait envoyé `bitcoin` auparavant par défaut enverra maintenant ce que vous avez choisi de nommer l'actif par défaut.

Il suffit donc d'envoyer 10 exemplaires du nouvel actif par défaut à une adresse donnée :

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

Si vous avez également fourni au nœud une valeur de `initialreissuancetokens` supérieure à zéro, vous serez également en mesure de réémettre plus d'actifs par défaut, ce qui n'est pas possible si vous exécutez Elements en tant que sidechain.

Pour ce faire, tout nœud détenant un montant de jeton associé à l'actif par défaut doit simplement émettre une commande sous la forme :

```
e1-cli reissueasset <default asset name> <amount>
```

En utilisant les paramètres ci-dessus, vous pouvez faire fonctionner Elements comme une blockchain autonome avec son propre actif par défaut, découplée de Bitcoin et d'autres blockchains.

## Conclusion

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

![Video](https://youtu.be/CTMdamTZBBM?si=16LBcXvN4pBfC7lr)

Dans ce cours, nous avons appris qu'Elements est un protocole de réseau open-source qui peut être mis en œuvre en tant que sidechain d'une autre blockchain, ou en tant que solution blockchain autonome.

Nous avons vu que le code source et le site web d'Elements (https://github.com/ElementsProject/elements) sont hébergés sur GitHub et qu'il existe des forums de discussion communautaires, tels que Build On L2 (https://community.liquid.net/c/developers/) ou Liquid Developers Telegram (https://t.me/liquid_devel), qui peuvent être utilisés pour en savoir plus sur le déploiement et le développement d'applications sur Elements et Liquid. Des fonctionnalités clés telles que les transactions confidentielles et les actifs émis ont été abordées, ainsi que la manière dont les membres d'une fédération forte permettent la signature fédérée des blocs et le mécanisme 2-Way Peg.

La prochaine étape consiste à vous lancer un défi en répondant à un questionnaire cumulatif qui couvre toutes les sections précédentes, puis à entamer votre parcours dans le domaine des éléments... bonne chance !

# Conclusion

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Critiques et évaluations

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusion

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

Félicitations pour avoir suivi ce cours !

Nous sommes ravis que vous ayez franchi avec succès cette étape de votre parcours d'apprentissage. Grâce à votre dévouement et à votre engagement, vous avez acquis des connaissances et des compétences précieuses qui vous seront utiles dans votre développement professionnel.