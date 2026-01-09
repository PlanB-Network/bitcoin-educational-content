---
name: Introduction au minage de Bitcoin
goal: Tout comprendre du minage de Bitcoin et de la preuve de travail, en partant de zéro
objectives:
  - Comprendre la preuve de travail et son rôle dans le fonctionnement de Bitcoin.
  - Analyser le mécanisme d’ajustement de la difficulté et ses effets sur le rythme des blocs.
  - Savoir ce qu'évoquent concrètement les termes techniques liés au minage.
  - Décrire les étapes de construction d’un bloc Bitcoin et les éléments qui le composent.
  - Identifier les grandes évolutions de l’industrie du minage.
---


# Découvrez les fondamentaux du minage de Bitcoin

Comprendre la preuve de travail, c’est comprendre le fonctionnement même de Bitcoin. Sans cette invention et son usage ingénieux, Bitcoin n’aurait tout simplement pas pu exister. Ce cours MIN 101 vous donne toutes les bases théoriques qui manquent souvent aux débutants et qui feront toute la différence dans votre parcours de bitcoiner.

Pensé pour partir de zéro, ce cours s’adresse aux débutants tout en conservant un haut niveau de rigueur technique et de précision. Vous y découvrirez comment le minage de Bitcoin fonctionne concrètement. Et si vous avez déjà un niveau intermédiaire, il vous permettra de consolider votre compréhension, de corriger certaines intuitions approximatives et d’explorer des détails souvent absents des explications grand public.

À l’issue de ce cours, vous ne vous contenterez plus de reprendre des raccourcis : vous serez capable d’expliquer le fonctionnement de la preuve de travail de façon simple, rigoureuse et concrète, afin de mieux juger les débats, comprendre l’évolution de Bitcoin et prendre des décisions plus éclairées dans votre utilisation. MIN 101 constitue également une porte d’entrée idéale avant d’aborder l’ensemble des autres cours plus avancés consacrés au minage de Bitcoin sur Plan ₿ Academy, qu’ils soient théoriques ou pratiques.

+++


# Introduction

## Aperçu du cours

Bienvenue dans le cours MIN 101, dans lequel vous allez découvrir les concepts théoriques fondamentaux du minage et de la Proof-of-Work au sein du système Bitcoin. Ce cours constitue la première étape de votre parcours de bitcoiner pour comprendre le fonctionnement du mining. À l’issue de celui-ci, vous pourrez poursuivre vers des cours théoriques plus avancés ou bien passer à la pratique et devenir vous-même mineur de bitcoins !

Dans ce cours MIN 101, nous ne reviendrons pas sur les concepts de base de Bitcoin, car nous allons entrer directement au cœur du sujet : le minage. Si vous n’avez jamais entendu parler de Bitcoin, ou si ses fondements vous semblent encore flous, je vous recommande vivement de commencer par notre cours d’introduction BTC 101. Une fois ces bases acquises, vous pourrez aborder sereinement MIN 101 :

https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966



# Le fonctionnement de la preuve de travail

## La construction d'un bloc Bitcoin

Avant de comprendre ce qu'est le minage de Bitcoin, il faut d’abord suivre le trajet d’une transaction typique sur Bitcoin. Cela permet de voir où intervient exactement le bloc, et pourquoi il est au cœur du système. C'est ce que je vous propose de découvrir dans ce premier chapitre.

### Le parcours de la transaction Bitcoin

Sur Bitcoin, une transaction est une structure de données qui transfère la propriété de bitcoins d'un utilisateur à un autre. Concrètement, elle consomme des `outputs` de transactions passées (ce qu'on appelle des UTXO) en les référant comme `inputs`, puis elle crée de nouveaux `outputs` qui définissent à qui appartiennent désormais ces bitcoins et sous quelles conditions ils pourront être dépensés plus tard.

001

Un point important sur Bitcoin est l’autorisation de dépenser. Les bitcoins ne sont pas dans un comptes, comme le pourraient être votre argent à la banque, mais ils sont verrouillés par des conditions de dépense. Lorsqu’un portefeuille veut utiliser un UTXO comme `inputs`, il doit fournir une preuve cryptographique qui prouve qu'il a bien le droit de le déverrouiller. Dans la pratique, cette preuve prend souvent la forme d’une signature numérique produite à partir d’une clé privée. C’est pour cette raison que les bitcoiners insistent sur la nécessité de sécuriser vos clés privées : ce sont elles qui permettent de déverrouiller l’accès à vos bitcoins et, par conséquent, de les dépenser.

002

La signature numérique dans Bitcoin joue ainsi deux rôles importants :
- Autoriser la dépense : elle prouve que l’utilisateur possède la clé privée attendue par la condition de dépense de l’UTXO ;
- Protéger l’intégrité : elle lie l’autorisation aux détails précis de la transaction (destinataires, montants, frais...). Si quelqu’un modifie la transaction après coup, la signature ne correspond plus.

Une fois la transaction correctement construite et signée par le portefeuille Bitcoin de l'utilisateur, elle doit être diffusée sur le réseau Bitcoin.

### Le rôle du nœud Bitcoin dans la diffusion

Bitcoin est un réseau pair-à-pair : il n’existe pas de serveur central qui reçoit et traite toutes les transactions. Ce rôle est joué collectivement par les nœuds. Un nœud Bitcoin est un logiciel (par exemple Bitcoin Core) connecté à d’autres nœuds du réseau Bitcoin, dont la mission principale est de vérifier, stocker et relayer les transactions et les blocs.

Quand vous envoyez une transaction depuis un portefeuille, celui-ci la transmet à un nœud (votre propre nœud, ou celui d’un service). Ce nœud va d’abord vérifier que la transaction respecte différentes règles, par exemple :
* les signatures sont valides ;
* les inputs référencent bien des UTXO existants (c'est-à-dire des bitcoins qui existent) ;
* ces UTXO n’ont pas déjà été dépensés ailleurs ;
* le montant des outputs est inférieur ou égal à celui des inputs (on ne crée pas de bitcoins à partir de rien) ;
* etc.

Si la transaction passe tous ces contrôles, le nœud la propage aux autres nœuds du réseau avec lesquels il est connecté. Eux-mêmes la vérifient à leur tour et la relaient, et ainsi de suite. En quelques secondes, la transaction est propagée et devient connue de l’ensemble, ou du moins d’une large partie, du réseau Bitcoin.

003

### La mempool : la salle d’attente des transactions

Entre le moment où une transaction est diffusée et le moment où elle est confirmée dans un bloc, elle doit attendre. Cette zone d’attente s’appelle **la mempool** (contraction de `memory` et `pool`). Une mempool est donc un espace de stockage temporaire de transactions valides, mais encore non confirmées.

Point important : il n’existe pas une mempool unique, mais des mempools. En effet, chaque nœud maintient la sienne, avec ses propres contraintes locales. Cela implique qu’à un instant donné, deux nœuds peuvent avoir des contenus de mempool légèrement différents (selon ce qu’ils ont reçu, ce qu’ils ont rejeté, ou ce qu’ils ont purgé).

004

À ce stade, on a donc un réseau qui connaît la transaction, l’a vérifiée, et la garde en mémoire en attendant qu’elle soit confirmée. Mais la confirmation de cette transaction n'arrivera que lorsqu'un mineur l’insère dans un bloc, et que ce bloc est accepté par le réseau.

### La blockchain : un registre public d’horodatage

Le bitcoin étant une monnaie immatérielle, elle doit répondre à un problème : empêcher la double dépense sans autorité centrale. Si deux transactions tentent de dépenser le même UTXO, il faut que tout le monde puisse converger vers un seul état cohérent. Satoshi Nakamoto résume cet enjeu avec cette phrase célèbre :

> Le seul moyen pour confirmer l’absence d’une transaction est d’être au courant de toutes les transactions.

Autrement dit, pour savoir qu’un bitcoin n’a pas déjà été dépensé, il faut disposer d’un registre commun des dépenses passées.

C’est le rôle de la blockchain : un registre public qui contient l’historique des transactions. Mais plutôt que d’écrire chaque transaction au fil de l’eau, Bitcoin les regroupe dans des blocs. Chaque bloc agit comme une page d’historique, et le système fonctionne ainsi comme un serveur d’horodatage : il ordonne les transactions dans le temps, de manière vérifiable.

Ce registre ne peut pas être réécrit grâce à un principe simple : chaque bloc inclut l’empreinte cryptographique (le hash) du bloc précédent. Ainsi, les blocs s’enchaînent : si vous modifiez un bloc du passé, son empreinte change, ce qui casse le lien avec le bloc suivant, ce qui casse le lien avec le bloc d’après, etc. C’est cette chaîne de dépendances qui donne son nom à la "blockchain".

005

Une fois que l'on a compris ces principes de base de Bitcoin, on peut décrire l’objectif d’un mineur de manière plus concrète : construire un nouveau bloc qui prolonge la chaîne existante, en y inscrivant des transactions en attente, puis tenter de le rendre valide (c'est la fameuse "preuve de travail" que l'on étudiera dans le chapitre suivant). Ici, on se concentre sur la construction du bloc candidat.

### Le bloc candidat

Les mineurs ne trouvent pas des blocs qui existeraient déjà quelque part : il doivent le fabriquer avant d'essayer de le miner. Chaque mineur, de son côté, construit ce que l'on appelle un bloc candidat à partir des transactions en attente dans sa mempool. Construire un bloc candidat consiste donc à :
- choisir quelles transactions inclure ;
- organiser ces transactions de manière compatible avec les règles de Bitcoin ;
- produire les métadonnées du bloc, contenues dans son entête.

Le choix des transactions répond à une logique économique simple : un bloc a une capacité limitée par le protocole Bitcoin, donc le mineur cherche à maximiser ce qu’il gagne pour cet espace. Il sélectionne en priorité les transactions offrant les frais les plus élevés relativement à la place qu’elles occupent dans le bloc (on parle ainsi de "taux de frais", par exemple en `sats/vB`). Les détails des frais seront traités plus tard ; retenez ici l’idée de tri par rentabilité de l’espace.

Un bloc Bitcoin se compose donc de deux grandes parties :
* une liste de transactions ;
* une entête de bloc, qui sert, en quelque sorte, de carte d’identité du bloc.

006

L’entête est essentielle, car c’est elle qui est utilisée comme base pour la preuve de travail : dans Bitcoin, on ne mine pas directement un bloc entier ; on mine uniquement l’entête d'un bloc, qui résume les informations nécessaires pour lier le bloc à la chaîne et engager son contenu. Pour que l’entête puisse représenter l’ensemble des transactions, Bitcoin utilise un outil cryptographique : l’arbre de Merkle.

### L’arbre de Merkle : résumer un grand ensemble de transactions

Lister toutes les transactions dans l’entête serait impossible : un bloc peut contenir des milliers de transactions, alors que l’entête a une taille fixe (80 octets). La solution consiste donc à calculer un hash unique qui dépend de toutes les transactions du bloc : c'est la racine de Merkle.

Le principe est le suivant :
* on calcule l’empreinte cryptographique de chaque transaction ;
* on regroupe ces empreintes deux par deux, on les met bout-à-bout, puis on les hache de nouveau pour obtenir une nouvelle couche d’empreintes ;
* on répète cette opération jusqu’à obtenir une seule empreinte finale : la racine de Merkle.

007

Ainsi, si une seule transaction change, même d’un seul bit, cela entraîne une modification de son empreinte, laquelle se propage jusqu'à la racine de Merkle. Or cette racine est incluse dans l’entête du bloc. Donc modifier une transaction passée revient à modifier l’entête du bloc dans lequel elle est incluse, et donc l’empreinte du bloc, puis le lien avec les blocs suivants.

Depuis SegWit, on sépare ce qui relève des signatures (témoins) du reste. Il y a donc en réalité 2 arbres de Merkle imbriqués dans chaque bloc. Cette séparation a des conséquences sur la manière de compter la taille d’un bloc et sur certains engagements cryptographiques, mais l’idée de base reste la même : l’entête doit engager, de manière compacte, tout le contenu du bloc.

### L’entête de bloc : ce que le mineur prépare réellement

L’entête de bloc fait 80 octets et contient exactement 6 champs. Ce sont ces six éléments qui seront hachés lors de la recherche d'une preuve de travail (voir chapitre suivant) :

- La version (`version`) : Elle indique quelles règles ou quels signaux de mise à jour le bloc utilise. C’est un mécanisme de compatibilité et d’évolution du protocole.

- L’empreinte du bloc précédent (`previousblockhash`) : C’est le hash de l’entête du bloc précédent. C’est lui qui enchaîne les blocs entre eux. Sans ce champ, on aurait des blocs indépendants. En incluant le hash de l'entête du bloc précédent, on obtient une chaîne, où chaque nouveau bloc s’appuie sur le précédent.

- La racine de Merkle (`merkleroot`) : C’est l'empreinte de toutes les transactions du bloc (via l’arbre de Merkle). Elle lie l’entête au contenu : si le mineur modifie la sélection ou l’ordre des transactions, la racine change.

- L’horodatage (`time`) : C’est un timestamp (temps Unix) choisi par le mineur (avec des contraintes de validité), qui doit indiquer quand le bloc a été miné. Il n’a pas besoin d’être parfaitement exact à la seconde près, mais il doit respecter certaines conditions pour rester acceptable par le réseau.

- La cible de difficulté encodée (`bits`) : Ce champ encode la cible de difficulté en vigueur. Nous détaillerons ce point dans le chapitre sur la difficulté, mais retenez ici que ce paramètre fait partie intégrante de l’entête.

- Le nonce (`nonce`) : C’est une valeur que le mineur peut modifier librement. Elle sert de variable d’ajustement durant la preuve de travail. Je vous expliquerai son rôle plus précisément dans le prochain chapitre, mais il est important de comprendre que le nonce fait partie de l’entête du bloc et qu’il est prévu précisément pour permettre des essais successifs.

Pour rendre cela plus facile à visualiser, voici un exemple d’entête de bloc au format hexadécimal (80 octets) :

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Et voici sa décomposition champ par champ :

```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
bits: b2e00517
nonce: 43f09a40
```

Cette entête du bloc candidat construit par le mineur constitut sa base de travail. Lors de la recherche d'une preuve de travail valide, ce n’est pas la liste entière des transactions qui est directement hachée en boucle, mais bien ce bloc de 80 octets, qui contient tout ce qu’il faut pour lier le bloc au passé et engager son contenu, tout en embarquant les paramètres nécessaires au mécanisme de minage, que nous allons justement découvrir dans le chapitre suivant.

## Le hachage, la cible et le nonce

Dans le chapitre précédent, vous avez suivi le chemin d’une transaction Bitcoin : créée et signée par un portefeuille, relayée par les nœuds, stockée dans les mempools, puis confirmée lorsqu’un mineur l’inclut dans un bloc accepté par le réseau. Mais nous n'avons pas encore vu comment un mineur peut ajouter son bloc à la blockchain. Autrement dit, quel est le processus concret derrière le minage ?

Comprendre le processus du minage, c'est assez simple. Cela tient en 3 notions qui vont ensemble : une fonction de hachage, une valeur cible et une variable que le mineur peut modifier. Voyons ensemble comment tout cela fonctionne.

### La fonction de hachage

Une fonction de hachage est un outil qui prend un message en entrée et produit une sortie de taille fixe, qu'on appelle "empreinte" ou "hash".

010

La fonction de hachage est intéressante dans des systèmes informatiques, car elle dispose de certaines propriétés :

* Si vous changez un seul bit de l’entrée, l’empreinte obtenue en sortie change totalement et de manière imprévisible ;

011

* Il est impossible de remonter de la sortie vers l’entrée : la fonction est irréversible ;

012

* Il est impossible de trouver deux messages différents qui donnent exactement la même empreinte.

013

La fonction de hachage utilisée dans Bitcoin pour le minage est `SHA256`, appliquée deux fois de suite. On parle de double SHA256, noté `SHA256d`. C’est cette double application qui produit l’empreinte du bloc.

```text
hash = SHA256(SHA256(message))
```

Dans notre cas, le `message` correspond en fait à l’entête du bloc, que vous avez vu au chapitre précédent. Pour rappel, l’entête est une petite structure qui résume tout ce qu'il y a dans le bloc.

014

### La preuve de travail : trouver une empreinte inférieure à une cible

La Proof-of-Work est souvent décrite comme le fait de résoudre un problème complexe. En réalité, il ne s’agit pas vraiment d'un problème, mais plutôt d’une recherche par tâtonnement : le mineur doit trouver une version de l’entête dont l’empreinte (après passage dans la fonction de hachage `SHA256d`) respecte une condition simple : qu'elle soit inférieure à une certaines cible.

Cette condition se formule ainsi :
* on calcule l’empreinte de l’entête du bloc à l'aide de la fonction de hachage ;
* on interprète cette empreinte comme un nombre ;
* pour que le bloc soit valide, ce nombre doit être inférieur ou égal à une valeur appelée "cible de difficulté" ou "facteur de difficulté".

Autrement dit, un bloc est valide si :

```text
SHA256d(block_header) <= target
```

015

La cible est un nombre de 256 bits. Comme l’empreinte produite par `SHA256d` fait aussi 256 bits, on peut les comparer comme deux nombres. Plus la cible est basse, plus la condition à remplir est difficile, car il existe moins de résultats possibles en dessous de ce seuil. À l’inverse, plus la cible est élevée, plus la condition est facile à satisfaire, et plus le minage d’un bloc devient simple. Nous détaillerons dans les prochains chapitre comment cette cible est déterminée.

Dans ce système, la fonction de hachage est intéressante. Rappelez-vous qu’il est facile de calculer la sortie à partir de l’entrée, mais qu’il est impossible de retrouver une entrée en ne connaissant que la sortie. Dans le cadre du minage, on ne demande pas aux mineurs de trouver une empreinte précise, mais plutôt de trouver une empreinte inférieure à une valeur cible. Le seul moyen d’y parvenir consiste à effectuer un très grand nombre de tentatives, jusqu’à ce qu’une entête particulière de leur bloc candidat, une fois hachée, produise une empreinte inférieure à cette cible.

À partir du moment où la cible est suffisamment basse, ce processus devient coûteux. Le mineur calcule le hash de l’entête de son bloc candidat, vérifie le résultat, puis, si la condition n’est pas remplie, modifie l’entête et recommence le calcul. Cette boucle se répète jusqu’à ce qu’une entête valide soit trouvée. Lorsque le hash de l’entête satisfait enfin la condition, la preuve de travail est établie, le bloc est considéré comme valide et peut être diffusé sur le réseau Bitcoin afin que les nœuds l’ajoutent à leur blockchain. Le mineur gagnant reçoit alors la récompense associée (nous détaillerons sa composition plus tard), tandis que l’ensemble des mineurs repart immédiatement à la recherche d’une nouvelle entête valide pour le bloc suivant.

L’intérêt fondamental de ce mécanisme réside dans son asymétrie. Produire une preuve de travail est coûteux pour les mineurs, car cela nécessite un grand nombre de calculs de hachage. En revanche, pour les vérificateurs, c’est-à-dire les nœuds du réseau, la vérification est extrêmement simple : il suffit de hacher l’entête du bloc et de vérifier que l’empreinte obtenue est bien inférieure à la cible. Trouver une preuve demande donc beaucoup de travail et de ressources, tandis que vérifier sa validité est rapide et peu coûteux. C’est précisément cette propriété qui définit un système de preuve de travail efficace.

### Le nonce

Reste une question pratique : si l'entête du bloc candidat construit par le mineur ne donne pas une empreinte valide, comment le mineur peut-il réessayer ? Il lui faut modifier quelque chose dans l’entête afin d’obtenir une empreinte différente. C’est précisément le rôle du nonce.

Rappelez-vous la première propriété d’une fonction de hachage : modifier un seul bit de l’entrée suffit à produire une empreinte de sortie totalement différente et imprévisible. Chaque calcul de hash s’apparente donc à un tirage aléatoire.

016

Pour tenter à nouveau sa chance, le mineur n’a pas besoin de modifier entièrement l’entête de son bloc candidat : il lui suffit d’en changer une infime partie, car le moindre bit différent entraînera une empreinte complètement nouvelle, et potentiellement valide si elle est inférieure à la cible.

C’est précisément pour cette raison que l’entête de bloc contient un nonce. Le nonce est une valeur de 32 bits, utilisée une seule fois, puis remplacée. Concrètement, pour un même bloc candidat, un mineur peut ainsi tester environ 4,29 milliards de valeurs possibles (de `0` à `2^32 - 1`). Chaque variation du nonce modifie l’entête du bloc et, par conséquent, change intégralement l’empreinte produite après l’application de la fonction de hachage `SHA256d`.

Le processus de minage est donc très simple :
- le mineur construit un bloc candidat (transactions + entête) ;
- il calcule l'empreinte `SHA256d(header)` ;
- si le résultat est supérieur à la cible, il change le nonce ;
- il recommence ;
- etc.

017

En réalité, le nonce n’est pas le seul champ que l’on peut modifier. Toute modification au sein des transactions d'un bloc entraîne un changement de la racine de l’arbre de Merkle, et donc une modification de l’entête de ce bloc. Avec la puissance de calcul moderne, parcourir les 4,29 milliards de valeurs possibles du nonce peut se faire relativement rapidement. C’est pourquoi il existe un autre champ, que l’on appelle généralement "extra-nonce", qui permet de démultiplier encore les possibilités de variation de l’entête. Nous reviendrons plus en détail sur ce mécanisme dans un prochain chapitre.

### Quel est l'intérêt de cette preuve de travail ?

On parle de "preuve" parce que le résultat est immédiatement vérifiable : une fois un bloc produit, n’importe quel nœud peut contrôler, en une fraction de seconde, que l’empreinte cryptographique de son en-tête est bien inférieure à la cible exigée. On parle de "travail" parce que parvenir à cette empreinte a requis une multitude d’essais, donc un coût réel en calcul et en énergie.

Dans le White Paper de Bitcoin, Satoshi Nakamoto met en avant deux intêrets à l'utilisation d'un système de preuve de travail dans Bitcoin :

- **Sceller l’historique économique :**

Une fois la charge de calcul dépensée, le bloc est figé : le modifier impliquerait de refaire la preuve de travail de ce bloc. Et comme les blocs sont enchaînés les uns avec les autres, altérer un bloc ancien obligerait aussi à recalculer tous les blocs suivants, puis à rattraper et dépasser le travail continu de la chaîne honnête. Autrement dit, la preuve de travail sert d’armature à un horodatage cumulatif qui rend la falsification du passé de plus en plus coûteuse à mesure que les blocs s’accumulent. Lorsqu’un nouveau bloc est miné, la sécurité fournie par la preuve de travail s’applique de manière simultanée et uniforme à l’ensemble des UTXOs existants. À chaque bloc ajouté, chaque UTXO accumule ainsi une quantité supplémentaire de sécurité issue de la Proof-of-Work.

- **Définir la règle de majorité (consensus) et neutraliser les Sybil :**

La preuve de travail permet à Bitcoin d’obtenir un consensus sans s’appuyer sur la règle de vote "un identifiant = une voix", facilement truqué par la création massive d’identités (IP, nœuds, clés...). Dans Bitcoin, la "majorité" n’est pas le plus grand nombre de participants, mais la **chaîne qui cumule le plus de travail** : comme l’écrit Satoshi, c’est un principe "une CPU = une voix", c’est-à-dire un vote pondéré par la puissance de calcul réellement dépensée pour produire des blocs valides. Ainsi, déployer des milliers de nœuds n’apporte aucun avantage en soi. Sans puissance de calcul supplémentaire, on n’accumule pas davantage de preuve de travail, et l’attaque Sybil devient inutile, tandis que la règle de décision reste objective et ne nécessite aucune identification des participants.

018

[Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System.*](https://bitcoin.org/bitcoin.pdf)

Les principes liés à l’utilité et aux pouvoirs des mineurs constituent un sujet très complexe que je ne détaillerai pas davantage dans cette formation. Nous y reviendrons cependant de manière approfondie dans la formation MIN 201.

### D’où vient l’idée de la preuve de travail ?

La preuve de travail n’a pas été inventée pour Bitcoin. Satoshi Nakamoto a repris et assemblé plusieurs idées plus anciennes, déjà explorées dans des contextes différents.

#### Hashcash

À la fin des années 1990, le problème du spam des e-mails devient important. Une idée simple apparaît : si envoyer un e-mail coûte presque zéro, un spammeur peut en envoyer des millions. Mais si chaque message exige un petit effort de calcul, envoyer un message reste facile pour un utilisateur normal, tandis qu’envoyer des millions de messages devient très cher.

C’est l’objectif de Hashcash, proposé par Adam Back en 1997, que l'on considère comme l'invention du principe de preuve de travail. Le principe de Hashcash ressemble fortement au minage : produire un hash qui respecte une condition (par exemple avoir un certain nombre de zéros en début d’empreinte). La preuve accompagne ensuite le message et peut être vérifiée très rapidement par le destinataire. En cas de réception d’un e-mail ne contenant pas cette preuve, celui-ci peut être immédiatement considéré comme du spam. Les spammeurs sont alors contraints de dépenser une quantité d’énergie considérable pour envoyer des millions de messages, ce qui réduit drastiquement (voire annule complètement) la rentabilité de ce type d’opérations, qu’elles soient marketing ou frauduleuses.

Hashcash ne cherchait pas à créer de la monnaie. Il cherchait à imposer un coût marginal à une action numérique facilement automatisable.

008

#### Bit Gold

Nick Szabo, à la fin des années 1990 et au début des années 2000, explore l’idée d’une rareté numérique basée sur la preuve de travail. Son projet conceptuel, appelé Bit Gold, imagine la création d’unités de valeur en résolvant une preuve de travail coûteuse, puis en enregistrant ces preuves dans un registre afin d’établir une forme de propriété.

Bit Gold n’a pas abouti à un système déployé comme Bitcoin, mais il contient plusieurs intuitions importantes : l’idée que du calcul peut produire une rareté, et l’idée d'horodater des éléments dans le temps pour créer un historique difficile à réécrire.

#### RPOW

Hal Finney propose en 2004 RPOW (*Reusable Proofs of Work*). L’idée est de produire des preuves de travail qui pourraient ensuite être échangées, plutôt que d’être simplement consommées. RPOW visait à créer des jetons numériques basés sur la preuve de travail, avec un système permettant de vérifier et de transférer ces jetons sans les dupliquer. RPOW, là encore, ne résout pas de façon satisfaisante le problème d’un registre totalement décentralisé comme Bitcoin le fera plus tard, mais il reste l'un des grands précurseurs de Bitcoin.

009

Hashcash, Bit Gold et RPOW utilisent la preuve de travail pour imposer un coût, créer de la rareté, ou construire des objets échangeables. Bitcoin reprend ce mécanisme, mais lui donne un rôle central et collectif : la preuve de travail ne sert pas seulement à créer quelque chose, elle sert à départager qui a le droit d’écrire la prochaine page du registre (le prochain bloc), et à rendre ce registre coûteux à falsifier.

Pour l’instant, vous pouvez résumer le fonctionnement du minage ainsi : les mineurs construisent un bloc candidat avec les transactions en attente dans les mempools, puis cherchent une empreinte de son entête (via `SHA256d`) qui soit inférieure ou égale à une cible. Ils y parviennent en testant des nonces par tâtonnement. Dans le chapitre suivant, nous allons découvrir comment cette cible de difficulté est déterminée par le système.

## L'ajustement de la cible de difficulté

Dans le chapitre précédent, vous avez vu le cœur de la preuve de travail : les mineurs hachent l’entête de leur bloc candidat avec `SHA256d`, et le bloc n’est considéré valide que si l’empreinte obtenue est numériquement inférieure ou égale à une valeur de référence appelée la cible. Il reste alors une question : d’où vient cette cible, et comment le système s’assure qu’elle reste cohérente au fil du temps ?

Bitcoin vise un rythme moyen d’un bloc trouvé toutes les 10 minutes. Ce rythme n’est évidemment pas une promesse à la seconde près. En pratique, certains blocs sont trouvés quelques secondes après le précédent, quand d’autres le sont après plus d'une heure. Ce qui importe ici, c’est la moyenne sur une période suffisamment longue.

019

Cette variabilité découle du caractère probabiliste du minage : chaque hachage est un essai indépendant, avec une probabilité constante (à cible inchangée) de produire un résultat inférieur à la cible. On peut donc le comparer à une loterie au tirage continu : plus les mineurs effectuent de hachages par seconde, plus le délai attendu avant l’apparition d’un bloc valide diminue, mais sans jamais supprimer l’aléa d’un tirage à l’autre.

### Pourquoi viser 10 minutes entre les blocs ?

Même si l'on n'a aucune preuve de cela, Satoshi Nakamoto a sûrement choisi 10 minutes comme un compromis pratique entre efficacité et sécurité. Un intervalle plus court donnerait des confirmations plus fréquentes, mais provoquerait davantage de divisions temporaires du réseau. Pour comprendre ce point, il faut revenir à la manière dont un bloc se propage.

Lorsqu’un mineur trouve un bloc valide, il le diffuse immédiatement à ses pairs. Les nœuds qui le reçoivent vérifient sa validité (transactions, preuve de travail, règles de consensus...), puis le relaient à leur tour. Cette propagation prend un certain temps, limité par la latence d'Internet, la bande passante, et la capacité de chaque nœud à vérifier le bloc.

020

Si, durant ce délai de diffusion, un autre mineur découvre lui aussi un bloc valide à la même hauteur, le réseau peut se retrouver temporairement scindé : une partie des nœuds et des mineurs se base sur le bloc A, tandis que l’autre se base sur le bloc B. C'est une division temporaire du réseau.

021

Ces divisions ne sont pas catastrophiques. Le consensus de Nakamoto prévoit qu’à terme, une seule branche l’emportera : celle qui accumule le plus de travail. En effet, dès qu’un nouveau bloc est miné par-dessus le bloc A par exemple, l’ensemble du réseau se resynchronise sur cette branche et abandonne le bloc B, qui devient alors un "stale block", parfois appelé à tort un "bloc orphelin" dans le langage courant.

022

En revanche, elles ont un coût : pendant quelques minutes, une fraction des mineurs travaille sur une branche qui sera abandonnée. Ce travail est alors gaspillé du point de vue de la sécurité globale, car il n’a pas contribué à la chaîne finale. Plus l'intervalle entre chaque bloc est rapide, plus la probabilité de ces divisions augmente, puisque le temps de propagation représente une part plus importante du temps entre chaque bloc.

L’intervalle de 10 minutes laisse généralement suffisamment de temps pour que le bloc gagnant se propage largement avant qu'un éventuel bloc à la même hauteur soit trouvé. C’est un compromis qui limite les divisions, réduit le gaspillage de la puissance de calcul, et aide le réseau à rester synchronisé à l’échelle mondiale.

### Comprendre la notion de hashrate

Le "hashrate" désigne la quantité de calcul de hachage produite par seconde, que ce soit par un seul mineur, par un groupe de mineur, ou bien par l'ensemble des mineurs sur Bitcoin. On l’exprime en `H/s` (hashs par seconde), avec des multiples comme `TH/s` (térahashs par seconde) ou `EH/s` (exahashs par seconde). Cela représente donc le nombre d’essais que les mineurs peuvent faire chaque seconde pour tenter d’obtenir un hash inférieur à la cible.

Si la cible reste fixe, alors :
* chaque essai a une probabilité fixe de réussite ;
* faire plus d’essais par seconde augmente la probabilité qu’un essai gagnant apparaisse rapidement.

Autrement dit, si demain le réseau Bitcoin double sa puissance de calcul en branchant deux fois plus de machines de minage, sans mécanisme correcteur, les blocs seraient trouvés en moyenne deux fois plus vite. Il faut donc ajuster la cible pour compenser les variations de hashrate.

### L'ajustement

Bitcoin résout ce problème avec un mécanisme d’ajustement périodique de la cible, qui vient donc ajuster la difficulté du minage. Le principe est le suivant : tous les 2016 blocs (environ toutes les 2 semaines), chaque nœud recalcule la cible de difficulté en observant combien de temps a réellement été nécessaire pour produire ces 2016 blocs.

L’objectif de ce mécanisme est de ramener le temps moyen de production d’un bloc autour de 10 minutes, alors que le hashrate global du réseau varie en permanence, en raison de machines qui se débranchent ou, au contraire, de nouvelles machines qui sont ajoutées.

023

Le calcul se fait à partir du temps observé pour la période écoulée :
* si les 2016 derniers blocs ont été trouvés trop vite, cela signifie que le hashrate a augmenté pendant cette période ; Bitcoin rend alors la condition plus difficile en abaissant la cible pour la prochaine période ;
* si les 2016 blocs ont été trouvés trop lentement, cela signifie que le hashrate a diminué ; Bitcoin facilite la condition en augmentant la cible.

La formule est donc celle-ci :

```txt
Tn = To * (Ta / Tt)
```

Avec :
* `Tn` : nouvelle cible
* `To` : ancienne cible
* `Ta` : temps réel écoulé pour les 2016 derniers blocs
* `Tt` : temps cible (en secondes)

Avec un temps cible de deux semaines, soit `Tt = 1 209 600` secondes :

```txt
Tn = To * (Ta / 1 209 600)
```

Pour bien comprendre l'ajustement de la difficulté du minage de Bitcoin, voici un exemple avec des valeurs réelles :

```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```

Avec :
* **`To = 18 045 755 102`** : Ancienne cible, c’est-à-dire la valeur de référence avant l’ajustement.
* **`Ta = 1 000 000` secondes** : Temps réellement passé pour produire les 2016 derniers blocs. Ce temps étant inférieur au temps cible, le réseau a miné trop rapidement.
* **`1 209 600` secondes** : Temps cible correspondant à deux semaines, utilisé comme référence pour l’ajustement.
* **`Tn = 14 918 779 020`** : Nouvelle cible calculée après l’ajustement de difficulté.

La nouvelle cible est ici plus basse que l’ancienne, ce qui implique une augmentation de la difficulté de minage afin de ralentir la production des blocs lors de la période suivante.

*Les valeurs des cibles dans cet exemple sont simplifiées et mises à l’échelle à des fins pédagogiques ; la cible réelle utilisée sur Bitcoin est un entier sur 256 bits d’un tout autre ordre de grandeur.*

Ce calcul est exécuté localement par chaque nœud, à partir des horodatages inscrits dans les blocs. Comme tous les nœuds appliquent les mêmes règles, ils aboutissent au même résultat, et la nouvelle cible devient la référence commune pour les 2016 blocs suivants.

Il y a un détail important à noter sur cet ajustement : **il est borné**. Bitcoin limite la variation de difficulté par période afin d’éviter des changements trop brutaux qui pourraient le bloquer. En effet, le temps réel pris en compte est contraint à rester dans une fourchette équivalente à un facteur 4 (au minimum un quart de deux semaines, au maximum quatre fois deux semaines). Cela empêche un reciblage extrême si les horodatages étaient très atypiques ou manipulés.

### La représentation de la cible

Dans l’entête de bloc, la cible n’apparaît pas sous sa forme complète de 256 bits, car cela prendrait trop de place. À la place, le champ `nBits` (de 32 bits) encode la cible dans un format compact, comparable à une notation scientifique en base 256 : un exposant (1 octet) et un coefficient (3 octets). La cible complète est ensuite reconstruite à partir de ces deux valeurs. Nous n’allons pas entrer dans le détail ici, car le sujet est relativement complexe et n’apporte rien à la compréhension du minage. Retenez simplement que la cible n’est pas stockée de manière brute dans l’entête du bloc, mais sous une forme compacte et normalisée.

Avec ce dernier chapitre, nous avons fait le tour du fonctionnement de la preuve de travail sur Bitcoin : le mineur construit un bloc candidat en sélectionnant des transactions dans sa mempool, calcule l’entête du bloc candidat, la hache, compare l’empreinte obtenue à la cible de la période, puis recommence en modifiant le nonce jusqu’à obtenir une empreinte valide. Enfin, tous les 2016 blocs, le réseau recalcule une nouvelle cible afin de maintenir un temps moyen d’environ 10 minutes par bloc, malgré les variations permanentes du hashrate.


# Le système d’incitations du minage de Bitcoin

## La récompense de bloc

Vous vous en doutez sûrement : miner sur Bitcoin n’est pas une activité altruiste. Les mineurs ont des coûts bien réels : l’électricité pour faire tourner leurs ordinateurs qui minent, l'achat de matériel spécialisé, la masse salariale pour la maintenance, parfois des locaux et des systèmes de refroidissement. Pour que le système Bitcoin fonctionne, il faut donc aligner l’intérêt privé des mineurs avec l’intérêt collectif du réseau. C’est exactement le rôle de la récompense de minage. Elle incite les mineurs à investir dans la preuve de travail, à inclure des transactions valides, et à respecter les règles du protocole plutôt que de tenter de le corrompre.

Cette logique relève de la théorie des jeux : le protocole rend l’honnêteté rationnelle. Un mineur gagne de l’argent lorsqu’il produit un bloc valide accepté par les nœuds. À l’inverse, s'il essaie de tricher, son bloc sera rejeté par les nœuds, et il n’obtiendra rien. Comme produire un bloc a un coût, un bloc rejeté représente une perte sèche. Dans un environnement concurrentiel où des milliers d’acteurs cherchent simultanément un bloc valide, la stratégie la plus rentable, la plupart du temps, consiste donc à suivre strictement les règles et à maximiser son revenu de manière honnête.

Pour ce faire, le protocole Bitcoin prévoit que le mineur qui trouve un bloc valide remporte le droit d’y inclure une transaction particulière qui lui attribue une certaine somme de BTC. C'est ce que l'on appelle **la récompense de bloc**. Dans ce premier chapitre, l’objectif est de comprendre de quoi elle est composée et comment elle est déterminée. Nous verrons plus tard comment la partie création monétaire évolue au fil du temps (avec les halvings) et comment elle est effectivement récupérée techniquement (via la transaction coinbase).

### De quoi se compose la récompense de bloc ?

Dans les chapitres précédents, nous avons vu comment les mineurs parviennent à trouver un bloc valide. Une fois qu’un mineur a trouvé une entête dont le hash est inférieur à la cible, son bloc candidat est considéré comme valide. Il peut alors le diffuser à l’ensemble du réseau Bitcoin. Le bloc est ajouté à la suite de la blockchain et permet de confirmer les transactions qu’il contient. C’est précisément cet événement (l’ajout effectif du bloc à la blockchain) qui déclenche l’attribution d’une récompense au mineur gagnant. Cette récompense se compose de deux éléments distincts que l'on additionne :
- **la subvention de bloc** ;
- **les frais de transaction**.

024

Voyons ensemble à quoi correspondent ces deux parties de la récompense.

### La subvention de bloc

La subvention de bloc correspond à la partie création monétaire de la récompense. Lorsqu’un mineur produit un bloc valide, le protocole l’autorise à créer un certain nombre de nouveaux bitcoins et à se les attribuer comme rémunération. Ces bitcoins sont créés ex nihilo. Ils n’existaient pas auparavant.

Toutefois, la quantité de bitcoins nouvellement créés n’est absolument pas arbitraire. Elle est strictement définie par les règles du protocole Bitcoin et identique pour tous les mineurs. Nous détaillerons ce mécanisme dans le chapitre suivant, car la subvention n’est pas une valeur fixe indéfiniment : elle est divisée périodiquement selon un calendrier précis. Pour l’instant, retenez simplement que :
- la subvention de bloc constitue une des deux composantes de la récompense de bloc ;
- elle est plafonnée et déterminée par le protocole, et non par le mineur (même si le mineur peut techniquement demander moins que le montant prévu) ;
- elle crée des bitcoins à partir de rien.

Cette subvention joue principalement deux rôles au sein du protocole Bitcoin. Le premier est d’inciter les acteurs à participer au minage. Durant les premières années de Bitcoin (et c’est encore parfois le cas aujourd’hui) les frais de transaction étaient très faibles. La subvention garantissait donc une rémunération suffisante pour attirer des mineurs et maintenir un niveau de sécurité pour le système.

Le second rôle est lié à la distribution de la monnaie. Toute nouvelle monnaie fait face à une question : comment distribuer les unités monétaires de manière juste ? La subvention de bloc apporte une réponse juste à ce problème. En créant des bitcoins via le minage, elle permet leur distribution initiale de façon ouverte et neutre : n’importe qui peut en obtenir, à condition de participer au minage, sans autorisation préalable ni identité requise.

En revanche, puisque ces bitcoins sont créés à partir de rien, leur valeur ne provient pas de nulle part. En augmentant la quantité de monnaie en circulation, la subvention dilue mécaniquement la valeur des bitcoins déjà existants. Elle introduit donc une forme d’inflation monétaire. Nous verrons toutefois dans le prochain chapitre que cette subvention est destinée à disparaître progressivement, et qu’à terme, cette inflation cessera.

025

### Les frais de transaction

La seconde composante de la récompense de bloc est liée à l’usage du système : lorsqu’un utilisateur diffuse une transaction, il veut qu’elle soit confirmée. Or, l’espace dans les blocs est limité et un bloc n’apparaît en moyenne qu’environ toutes les 10 minutes. L’espace de bloc est donc une ressource rare. Quand la demande dépasse l’offre, le prix monte : c’est le marché des frais de transaction. Chaque mineur qui parvient à produire un bloc valide obtient le droit de percevoir, pour son propre compte, l’intégralité des frais de transaction associés à toutes les transactions qu’il a incluses dans son bloc.

Vous pouvez le voir comme un système d’enchères : chaque transaction propose un montant de frais, et les mineurs sélectionnent en priorité celles qui maximisent leur revenu, sous contrainte de place. Ce mécanisme aligne naturellement les intérêts :
* les utilisateurs pressés paient davantage pour être inclus rapidement ;
* les mineurs sont incités à inclure les transactions qui rémunèrent le mieux l’espace du bloc ;
* le réseau évite le spam, car publier une transaction a un coût.

#### Comment sont calculés les frais d’une transaction ?

Contrairement à une idée reçue, les frais ne sont pas un output dans une transaction Bitcoin. En effet, une transaction dépense des inputs et crée des outputs. Les inputs représentent la source des bitcoins utilisés, tandis que les outputs représentent la destination des paiements. Les frais de transaction correspondent simplement à **la différence entre le total des inputs et le total des outputs**.

Autrement dit, l’utilisateur engage en inputs des bitcoins qui lui appartiennent, crée des outputs pour les destinataires, mais ne recrée pas en outputs la totalité du montant consommé en inputs. La différence entre les deux constitue les frais de transaction que le mineur peut récupérer.

Prenons un exemple. Une transaction consomme deux inputs, l’un de `100 000 sats` et l’autre de `150 000 sats`, et crée trois outputs de `35 000 sats`, `42 000 sats` et `170 000 sats`.

027

La somme des inputs est donc de `250 000 sats`, tandis que la somme des outputs est de `247 000 sats`. Cela signifie que `3 000 sats` ont été consommés en inputs sans être recréés en outputs : ce montant correspond aux frais proposés par cette transaction.

028

Si un mineur inclut cette transaction dans un bloc valide, il aura le droit de récupérer ces `3 000 sats`, en plus des frais de toutes les autres transactions incluses dans le bloc. En revanche, il n’existe aucun lien direct on-chain entre la transaction qui paie les frais et les sats effectivement perçus par le mineur. Techniquement, les `3 000 sats` de frais sont détruits, et, en contrepartie, le mineur obtient le droit de les recréer pour lui-même.

#### Le ratio de frais

Un bloc n’est pas limité par le nombre de transactions, mais par sa capacité totale (aujourd’hui, en pratique, par le poids du bloc). Certaines transactions prennent plus de place que d’autres : une transaction avec de nombreux inputs et outputs sera plus volumineuse qu’une transaction simple avec un seul input et deux outputs. Les scripts utilisés vont aussi influencer la taille.

026

Deux transactions peuvent donc payer le même montant de frais en valeur absolue, mais ne pas être équivalentes économiquement du point de vue du mineur. Si l’une est deux fois plus grosse, elle coûte deux fois plus d’espace dans le bloc. Or l’espace est rare : le mineur cherche donc à maximiser ses revenus par unité d’espace.

C’est la raison pour laquelle, dans la pratique, on exprime la compétitivité d’une transaction avec un taux de frais, généralement en `sats/vB` (satoshis par octet virtuel). Le calcul de ce ratio est très simple :

```text
fee rate = fee / weight (in vB)
```

Par exemple, si l'on a une transaction qui pèse `141 vB` et qui alloue `1 974 sats` de frais, elle va avoir un taux de frais de `14 sats/vB`.

```text
1 974 / 141 ≈ 14 sats/vB
```

Ce ratio explique la stratégie des mineurs : à capacité fixe, inclure des transactions à taux élevé maximise les frais totaux du bloc, donc la rémunération du mineur. C’est aussi ce qui explique les périodes où les transactions à bas frais restent longtemps en attente dans les mempools : elles sont en concurrence avec d’autres transactions qui payent davantage par unité d’espace.

### La protection du réseau contre le spam

Les frais ont également une utilité de sécurité opérationnelle : ils introduisent un coût à la multiplication de transactions. Si publier une transaction était gratuit, il serait facile d’inonder le réseau de transactions inutiles et de saturer les mempools, augmentant la charge sur les nœuds.

Dans la pratique, les nœuds appliquent des politiques locales de relais (règles de mempool) et fixent souvent un seuil minimal de frais en dessous duquel ils ne relaient pas une transaction (par défaut, `0.1 sat/vB` sur Bitcoin Core via `minRelayTxFee`). Une transaction peut être valide au sens strict des règles de consensus tout en étant non relayée par la plupart des nœuds si ses frais sont trop bas. Résultat : elle ne circule pas, n’atteint pas les mineurs, et a très peu de chances d’être confirmée.

À ce stade, vous avez compris l’essentiel de la récompense de bloc : elle correspond à la rémunération du mineur gagnant et se compose de deux éléments distincts. D’une part, une subvention de bloc, définie par les règles du protocole, qui crée de nouveaux bitcoins ex nihilo. D’autre part, les frais des transactions incluses dans le bloc miné. Dans le chapitre suivant, nous allons nous concentrer plus en détail sur la subvention de bloc, afin de comprendre précisément comment elle est calculée et comment elle évolue au fil du temps selon les règles du protocole Bitcoin.

## Le halving

Dans le chapitre précédent, nous avons vu que les mineurs qui produisent un bloc valide reçoivent une récompense composée des frais des transactions incluses dans le bloc, ainsi que d’une subvention de bloc. En revanche, nous n’avons pas encore expliqué comment le montant de cette subvention est déterminé. Le mécanisme qui fixe et fait évoluer cette valeur est ce que l’on appelle le ***halving***.

### En quoi consiste le halving ?

Le halving est un événement programmé dans le protocole Bitcoin qui réduit de moitié la subvention de bloc, c’est-à-dire la quantité maximale de nouveaux bitcoins que le mineur gagnant est autorisé à créer à chaque bloc. Il ne concerne pas les frais de transaction : les frais existent indépendamment et restent déterminés par l’activité des utilisateurs et la concurrence pour l’espace de bloc.

Lors du lancement de Bitcoin en 2009, la subvention de bloc était fixée à 50 BTC pour chaque bloc miné. Depuis, cette subvention a été divisée par deux à plusieurs reprises, lors de chaque halving.

029

Le halving n’est pas déclenché par une date, mais par la hauteur de bloc. Il est exécuté **tous les 210 000 blocs**. Comme Bitcoin vise un intervalle moyen d’environ 10 minutes par bloc, 210 000 blocs correspondent à peu près à quatre ans.

```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
    int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
    // Force block reward to zero when right shift is undefined.
    if (halvings >= 64)
        return 0;

    CAmount nSubsidy = 50 * COIN;
    // Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
    nSubsidy >>= halvings;
    return nSubsidy;
}
```

Ainsi, si l’on note `n` le nombre de halvings déjà survenus, la subvention de bloc en BTC peut être calculée de cette manière :

```text
subsidy(n) = 50 / 2^n
```

### Les halvings passés

Voici un tableau récapitulatif des halvings déjà survenus, avec leur hauteur de bloc, la date et la nouvelle subvention de bloc applicable après l’événement :

| Événement           |   Hauteur | Date                        | Subvention |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 juillet 2016              |   12,5 BTC |
| Halving 3           |   630 000 | 11 mai 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 avril 2024               |  3,125 BTC |
| Halving 5 (à venir) | 1 050 000 | Printemps 2028 (estimation) | 1,5625 BTC |

### Quand et comment la subvention s’arrête ?

Le halving se répète tant que la subvention reste exprimable dans l’unité minimale du système : le satoshi.

```text
1 BTC = 100 000 000 sats
```

À mesure que la subvention est divisée par deux, on finit par atteindre des fractions de bitcoin si petites qu’elles deviennent inférieures à 1 sat. À partir de ce moment, il n’est plus possible de créer une demi-unité de satoshi. La création monétaire via la subvention de bloc s’arrête, et la rémunération des mineurs repose alors uniquement sur les frais de transaction. À partir de ce moment-là, tous les bitcoins seront en circulation et il ne sera plus possible de produire de nouvelles unités.

L’arrêt définitif de la subvention de bloc interviendra à la hauteur de bloc 6 930 000, soit lors du 33ème et dernier halving. Cet événement est attendu aux alentours de l’année 2140. Il est toutefois impossible de donner une date exacte, car celle-ci dépendra de la vitesse réelle à laquelle les blocs seront trouvés d’ici là.

En revanche, comme la subvention de bloc suit une suite géométrique de raison 1/2 à chaque halving, la création monétaire a été extrêmement élevée aux débuts de Bitcoin, puis décroît très rapidement. Dès le 7ème halving, plus de 99 % des bitcoins auront déjà été mis en circulation. Le franchissement de ce seuil des 99 % devrait avoir lieu entre 2032 et 2036. Cela veut dire qu'il faudra ensuite plus de 100 ans pour miner le dernier 1 % des bitcoins restants. Si l’inflation monétaire était donc très forte au lancement de Bitcoin afin de permettre une distribution large de la monnaie, elle est aujourd’hui très faible et continuera de décroître, jusqu’à atteindre une véritable monnaie dure, dont l’offre en circulation ne pourra plus augmenter.

030

### Pourquoi il n’y aura jamais 21 millions de BTC ?

On présente souvent l’offre monétaire maximale de Bitcoin comme étant de 21 millions de BTC. C’est une bonne approximation pour comprendre sa politique monétaire, mais d’un point de vue strictement technique, l’offre totale n’atteindra en réalité jamais exactement 21 000 000 de bitcoins.

La raison principale est mécanique. À force de halvings successifs, la subvention de bloc finit par passer sous la valeur minimale de 1 sat, ce qui met fin à l’émission avant d’atteindre précisément la somme théorique. En raison de cette granularité minimale et des règles d’arrondi, le total des bitcoins créés par la subvention est donc légèrement inférieur à 21 millions.

À cela peuvent s’ajouter des écarts marginaux d’origine protocolaire. Il est par exemple arrivé, de manière très rare, que certains mineurs n’aient pas réclamé la totalité de leur subvention, ce qui réduit encore définitivement la quantité de bitcoins effectivement émise. On peut également mentionner le bloc de genèse, produit par Satoshi le 3 janvier 2009, dont les bitcoins créés ne font pas partie de l’UTXO set, ainsi que certains événements historiques liés à des bugs, comme celui des identifiants de transactions coinbase dupliqués.

Enfin, il faut aussi prendre en compte tous les bitcoins qui ont été détruits ou bloqués :
- les bitcoins verrouillés dans des scripts insolubles ;
- ceux volontairement détruits via des scripts `OP_RETURN` ;
- ou encore les pertes de clés privées au niveau applicatif.

En théorie, l’offre de Bitcoin est donc bornée à 21 millions. En pratique, cependant, il n’y aura jamais réellement 21 millions de bitcoins en circulation.

## La transaction coinbase






# L'industrie du minage de Bitcoin

## L'évolution des machines de minage


## Le regroupement en pools de minage






















# Partie finale

## Avis & Notes
<isCourseReview>true</isCourseReview>

## Examen final
<isCourseExam>true</isCourseExam>

## Conclusion
<isCourseConclusion>true</isCourseConclusion>