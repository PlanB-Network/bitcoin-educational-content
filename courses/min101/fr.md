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

Une fonction de hachage est un outil qui prend un message en entrée et produit une sortie de taille fixe, qu'on appelle "empreinte" ou "hash". La fonction de hachage est intéressante dans des systèmes informatiques, car elle dispose de certaines propriétés :
* Si vous changez un seul bit de l’entrée, l’empreinte obtenue en sortie change totalement et de manière imprévisible ;
* Il est impossible de remonter de la sortie vers l’entrée : la fonction est irréversible ;
* Il est impossible de trouver deux messages différents qui donnent exactement la même empreinte.

La fonction de hachage utilisée dans Bitcoin pour le minage est `SHA256`, appliquée deux fois de suite. On parle de double SHA256, noté `SHA256d`. C’est cette double application qui produit l’empreinte du bloc.

```text
hash = SHA256(SHA256(message))
```

Dans notre cas, le `message` correspond en fait à l’entête du bloc, que vous avez vu au chapitre précédent. Pour rappel, l’entête est une petite structure qui résume tout ce qu'il y a dans le bloc.

### La preuve de travail : trouver une empreinte inférieure à une cible

La Proof-of-Work est souvent décrite comme le fait de "résoudre un problème complexe". En réalité, il ne s’agit pas vraiment d'un problème, mais plutôt d’une recherche par tâtonnement : le mineur doit trouver une version de l’entête dont l’empreinte (après passage dans la fonction `SHA256d`) respecte une condition simple : qu'elle soit inférieure à une certaines cible.

Cette condition se formule ainsi :
* on calcule l’empreinte de l’entête du bloc à l'aide de la fonction de hachage ;
* on interprète cette empreinte comme un nombre ;
* pour que le bloc soit valide, ce nombre doit être inférieur ou égal à une valeur appelée "cible de difficulté" ou "facteur de difficulté".

Autrement dit, un bloc est valide si :

```text
SHA256d(block_header) <= target
```

La cible est un nombre de 256 bits. Comme l’empreinte produite par `SHA256d` fait aussi 256 bits, on peut les comparer comme deux nombres. Plus la cible est basse, plus la condition à remplir est difficile, car il existe moins de résultats possibles en dessous de ce seuil. À l’inverse, plus la cible est élevée, plus la condition est facile à satisfaire, et plus le minage d’un bloc devient simple. Nous détaillerons dans les prochains chapitre comment cette cible est déterminée.

Dans ce système, la fonction de hachage est intéressante. Rappelez-vous qu’il est facile de calculer la sortie à partir de l’entrée, mais qu’il est impossible de retrouver une entrée en ne connaissant que la sortie. Dans le cadre du minage, on ne demande pas aux mineurs de trouver une empreinte précise, mais plutôt de trouver une empreinte inférieure à une valeur cible. Le seul moyen d’y parvenir consiste à effectuer un très grand nombre de tentatives, jusqu’à ce qu’une entête particulière de leur bloc candidat, une fois hachée, produise une empreinte inférieure à cette cible.

À partir du moment où la cible est suffisamment basse, ce processus devient coûteux. Le mineur calcule le hash de l’entête de son bloc candidat, vérifie le résultat, puis, si la condition n’est pas remplie, modifie l’entête et recommence le calcul. Cette boucle se répète jusqu’à ce qu’une entête valide soit trouvée. Lorsque le hash de l’entête satisfait enfin la condition, la preuve de travail est établie, le bloc est considéré comme valide et peut être diffusé sur le réseau Bitcoin afin que les nœuds l’ajoutent à leur blockchain. Le mineur gagnant reçoit alors la récompense associée (nous détaillerons sa composition plus tard), tandis que l’ensemble des mineurs repart immédiatement à la recherche d’une nouvelle entête valide pour le bloc suivant.

L’intérêt fondamental de ce mécanisme réside dans son asymétrie. Produire une preuve de travail est coûteux pour les mineurs, car cela nécessite un grand nombre de calculs de hachage. En revanche, pour les vérificateurs, c’est-à-dire les nœuds du réseau, la vérification est extrêmement simple : il suffit de hacher l’entête du bloc et de vérifier que l’empreinte obtenue est bien inférieure à la cible. Trouver une preuve demande donc beaucoup de travail et de ressources, tandis que vérifier sa validité est rapide et peu coûteux. C’est précisément cette propriété qui définit un système de preuve de travail efficace.

### Le nonce

Reste une question pratique : si l'entête du bloc candidat construit par le mineur ne donne pas une empreinte valide, comment le mineur peut-il réessayer ? Il lui faut modifier quelque chose dans l’entête afin d’obtenir une empreinte différente. C’est précisément le rôle du nonce.

Rappelez-vous la première propriété d’une fonction de hachage : modifier un seul bit de l’entrée suffit à produire une empreinte de sortie totalement différente et imprévisible. Chaque calcul de hash s’apparente donc à un tirage aléatoire. Pour tenter à nouveau sa chance, le mineur n’a pas besoin de modifier entièrement l’entête de son bloc candidat : il lui suffit d’en changer une infime partie, car le moindre bit différent entraînera une empreinte complètement nouvelle, et potentiellement valide si elle est inférieure à la cible.

C’est précisément pour cette raison que l’entête de bloc contient un nonce. Le nonce est une valeur de 32 bits, utilisée une seule fois, puis remplacée. Concrètement, pour un même bloc candidat, un mineur peut ainsi tester environ 4,29 milliards de valeurs possibles (de `0` à `2^32 - 1`). Chaque variation du nonce modifie l’entête du bloc et, par conséquent, change intégralement l’empreinte produite après l’application de la fonction de hachage `SHA256d`.

Le processus de minage est donc très simple :
- le mineur construit un bloc candidat (transactions + entête) ;
- il calcule l'empreinte `SHA256d(header)` ;
- si le résultat est supérieur à la cible, il change le nonce ;
- il recommence ;
- etc.

En réalité, le nonce n’est pas le seul champ que l’on peut modifier. Toute modification au sein des transactions d'un bloc entraîne un changement de la racine de l’arbre de Merkle, et donc une modification de l’entête de ce bloc. Avec la puissance de calcul moderne, parcourir les 4,29 milliards de valeurs possibles du nonce peut se faire relativement rapidement. C’est pourquoi il existe un autre champ, que l’on appelle généralement "extra-nonce", qui permet de démultiplier encore les possibilités de variation de l’entête. Nous reviendrons plus en détail sur ce mécanisme dans un prochain chapitre.

### Quel est l'intérêt de cette preuve de travail ?

On parle de "preuve" parce que le résultat est immédiatement vérifiable : une fois un bloc produit, n’importe quel nœud peut contrôler, en une fraction de seconde, que l’empreinte cryptographique de son en-tête est bien inférieure à la cible exigée. On parle de "travail" parce que parvenir à cette empreinte a requis une multitude d’essais, donc un coût réel en calcul et en énergie.

Dans le White Paper de Bitcoin, Satoshi Nakamoto met en avant deux intêrets à l'utilisation d'un système de preuve de travail dans Bitcoin :

- **Sceller l’historique économique :**

Une fois la charge de calcul dépensée, le bloc est figé : le modifier impliquerait de refaire la preuve de travail de ce bloc. Et comme les blocs sont enchaînés les uns avec les autres, altérer un bloc ancien obligerait aussi à recalculer tous les blocs suivants, puis à rattraper et dépasser le travail continu de la chaîne honnête. Autrement dit, la preuve de travail sert d’armature à un horodatage cumulatif qui rend la falsification du passé de plus en plus coûteuse à mesure que les blocs s’accumulent. Lorsqu’un nouveau bloc est miné, la sécurité fournie par la preuve de travail s’applique de manière simultanée et uniforme à l’ensemble des UTXOs existants. À chaque bloc ajouté, chaque UTXO accumule ainsi une quantité supplémentaire de sécurité issue de la Proof-of-Work.

- **Définir la règle de majorité (consensus) et neutraliser les Sybil :**

La preuve de travail permet à Bitcoin d’obtenir un consensus sans s’appuyer sur la règle de vote "un identifiant = une voix", facilement truqué par la création massive d’identités (IP, nœuds, clés...). Dans Bitcoin, la "majorité" n’est pas le plus grand nombre de participants, mais la **chaîne qui cumule le plus de travail** : comme l’écrit Satoshi, c’est un principe "une CPU = une voix", c’est-à-dire un vote pondéré par la puissance de calcul réellement dépensée pour produire des blocs valides. Ainsi, déployer des milliers de nœuds n’apporte aucun avantage en soi. Sans puissance de calcul supplémentaire, on n’accumule pas davantage de preuve de travail, et l’attaque Sybil devient inutile, tandis que la règle de décision reste objective et ne nécessite aucune identification des participants.

Les principes liés à l’utilité et aux pouvoirs des mineurs constituent un sujet très complexe que je ne détaillerai pas davantage dans cette formation. Nous y reviendrons cependant de manière approfondie dans la formation MIN 201.









## L'ajustement de la cible de difficulté






# La distribution des récompenses de minage

## La récompense de minage

- Comprendre la composition de la récompense de minage

## Le halving


- Comprendre le principe du halving
- Appréhender la fin de la subvention de bloc : il se passera quoi et quand ?
- Jamais 21m de BTC


## La transaction coinbase

- Comprendre la construction de la transaction coinbase








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