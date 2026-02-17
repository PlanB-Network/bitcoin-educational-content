---
name: Introduction au minage de Bitcoin
goal: Tout comprendre du minage de Bitcoin et de la preuve de travail, en partant de zéro
objectives:
  - Comprendre la preuve de travail et son rôle dans le fonctionnement de Bitcoin.
  - Analyser le mécanisme d’ajustement de la difficulté.
  - Savoir ce qu'évoquent concrètement les termes techniques liés au minage.
  - Décrire les étapes de construction d’un bloc Bitcoin et les éléments qui le composent.
  - Identifier les grandes évolutions de l’industrie du minage.
---

# Découvrez les fondamentaux du minage de Bitcoin

Comprendre la preuve de travail, c’est comprendre le fonctionnement même de Bitcoin. Sans cette invention et son usage ingénieux, Bitcoin n’aurait tout simplement pas pu exister. Ce cours vous fournit l’ensemble des bases théoriques sur le minage nécessaires dans votre parcours de bitcoiner.

MIN 101 s’adresse avant tout aux débutants, puisque l’ensemble des notions y est expliqué précisément depuis zéro. Toutefois, si vous disposez déjà d’un niveau intermédiaire, ce cours vous permettra de consolider votre compréhension, de corriger certaines intuitions approximatives et d’explorer des détails souvent absents des explications grand public.

À l’issue de ce cours, vous serez capable d’expliquer le fonctionnement de la preuve de travail de façon simple et rigoureuse. MIN 101 constitue également une porte d’entrée idéale avant d’aborder l’ensemble des autres cours plus avancés consacrés au minage de Bitcoin sur Plan ₿ Academy, qu’ils soient théoriques ou pratiques.

+++


# Introduction
<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>

## Aperçu du cours
<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>

Bienvenue dans le cours MIN 101, dans lequel vous allez découvrir les concepts théoriques fondamentaux du minage et de la Proof-of-Work au sein du système Bitcoin. Ce cours constitue la première étape de votre parcours de bitcoiner pour comprendre le fonctionnement du mining. À l’issue de celui-ci, vous pourrez poursuivre vers des cours théoriques plus avancés ou bien passer à la pratique et devenir vous-même mineur de bitcoins !

Dans ce cours MIN 101, nous ne reviendrons pas sur les concepts de base de Bitcoin, car nous allons entrer directement au cœur du sujet : le minage. Si vous n’avez jamais entendu parler de Bitcoin, ou si ses fondements vous semblent encore flous, je vous recommande vivement de commencer par notre cours d’introduction BTC 101. Une fois ces bases acquises, vous pourrez aborder sereinement MIN 101 :

https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Partie 1 – Introduction

Nous allons commencer ce cours par un premier chapitre optionnel, dans lequel je vous propose une explication très simplifiée du minage, afin de poser une image mentale claire avant d’entrer dans les mécanismes techniques.

L’objectif ici n’est pas de vous donner tous les détails techniques (ils viendront plus loin dans la formation), mais de vous donner le fil conducteur. Une fois ce cadre en place, chaque notion plus avancée abordée ensuite viendra naturellement se rattacher à cette structure.

### Partie 2 – Le fonctionnement de la preuve de travail

Après l'introduction, la partie 2 est le socle technique de la formation. Son but est de vous expliquer, pas à pas, comment Bitcoin produit des blocs valides. Nous commencerons par découvrir la structure d’un bloc, avant d’entrer dans le mécanisme de la preuve de travail : le rôle de la cible, du nonce et de la fonction de hachage. Enfin, nous verrons comment Bitcoin parvient à maintenir un rythme de production des blocs stable malgré les variations de la puissance de hachage, grâce au mécanisme d’ajustement de la difficulté. À l’issue de cette partie, vous comprendrez l’ensemble des rouages et des principes fondamentaux de la preuve de travail sur Bitcoin.

### Partie 3 – Le système d’incitations du minage de Bitcoin

Dans la troisième partie, nous verrons pourquoi les mineurs sont incités à participer honnêtement au minage. Nous détaillerons le principe de la récompense de bloc, sa composition et son mode de calcul, son évolution dans le temps à travers les halvings, ainsi que le rôle spécifique de la transaction coinbase.

### Partie 4 – L’industrie du minage de Bitcoin

La quatrième partie replace le minage dans sa réalité opérationnelle. Elle retrace l’évolution des machines de minage, du début de Bitcoin jusqu'aux ASIC modernes, afin de comprendre les contraintes matérielles actuelles. Nous étudierons également les bases du fonctionnement des pools de minage, afin de comprendre comment les mineurs parviennent à réduire la variance de leurs revenus.

### Partie 5 – Partie finale

Dans la partie finale du cours, vous pourrez évaluer vos connaissances sur le minage en passant votre diplôme.

L’objectif de ce cours MIN 101 est donc de vous permettre de repartir avec une compréhension claire, structurée et durable du minage de Bitcoin, aussi bien sur le plan technique qu’économique.

Prêt à découvrir le minage de Bitcoin ? C’est parti !


## Le minage de Bitcoin expliqué simplement
<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>

Avant de passer à l’explication détaillée et plus technique du minage de Bitcoin, je vous propose une vue d’ensemble de son principe, volontairement simple et schématique. Si vous disposez déjà de ces quelques connaissances de base, vous pouvez passer directement au vif du sujet dans le chapitre suivant, après avoir répondu aux questions du quiz. Ce chapitre s’adresse avant tout aux débutants, afin de commencer en douceur.

Imaginez Bitcoin comme un grand cahier public, partagé par tout le monde, où l’on écrit qui a envoyé des bitcoins à qui. Ce cahier s’appelle la blockchain. Il ne peut pas être tenu par une seule personne, sinon il faudrait lui faire confiance. À la place, Bitcoin fonctionne de façon collective : des milliers d’ordinateurs vérifient et conservent la même version de ce cahier.

![Image](assets/fr/049.webp)

Dans Bitcoin, quand vous faites un paiement, vous créez une transaction. Cette transaction n’est pas ajoutée instantanément dans le cahier. Elle est d’abord envoyée au réseau, puis elle attend d’être intégrée au prochain paquet de transactions. Ce paquet s’appelle un bloc.

![Image](assets/fr/050.webp)

Un bloc, c’est donc simplement un ensemble de transactions regroupées. Quand un bloc est prêt, il ne suffit pas de le publier. Il faut prouver au réseau que ce bloc mérite d’être ajouté au cahier commun. C’est là qu’intervient le minage.

Le minage, c’est le travail qui consiste à valider un bloc en dépensant de l’énergie. Des acteurs appelés mineurs utilisent des ordinateurs spécialisées. Ces machines consomment de l’électricité pour effectuer un très grand nombre d'essais, en boucle, jusqu’à trouver une preuve que le réseau accepte. Quand un mineur trouve cette preuve, son bloc est considéré comme valide.

Une fois le bloc validé, il est diffusé au réseau. Les autres nœuds vérifient rapidement qu’il respecte bien les règles, puis ils l’ajoutent à la suite des blocs précédents. C’est pour cela qu’on parle de "blockchain" : chaque nouveau bloc vient se placer après les autres, dans un ordre séquentiel, et cette chaine grandit petit à petit.

![Image](assets/fr/051.webp)

Pour résumer, on a donc d’abord des transactions qui sont créées. Ensuite, elles sont regroupées dans un bloc. Ensuite, un mineur valide ce bloc en dépensant de l’électricité. Enfin, ce bloc est ajouté à la blockchain, et les transactions qu’il contient deviennent confirmées.

Si des mineurs consomment de l’électricité, ce n’est pas par bénévolat. Ils le font parce qu’il y a une récompense. Quand un mineur valide un bloc, il reçoit deux types de revenus. D’un côté, il reçoit des bitcoins nouvellement créés. De l’autre, il récupère les frais payés par les utilisateurs dans les transactions incluses dans le bloc. Autrement dit, le mineur est rémunéré à la fois par une création monétaire programmée, et par un marché de frais.

À ce stade, vous avez volontairement une vision très simple du minage. Elle n’explique pas encore comment le bloc est construit en détail, ni comment fonctionne exactement la preuve que les mineurs cherchent, ni comment Bitcoin garde un rythme régulier, ni comment la récompense est calculée précisément, ni comment elle est encaissée. C’est normal, c'est tout ce que nous allons voir dans la suite de ce cours MIN 101 !

L’objectif de ce chapitre était simplement de vous donner une structure mentale claire : transactions → blocs → minage → blockchain → récompense. Gardez cette chaîne d’idées en tête. Dans la suite du cours, chaque chapitre viendra ajouter une couche de précision technique sur l’un de ces éléments, jusqu’à ce que vous compreniez non seulement ce qui se passe, mais aussi comment et pourquoi cela fonctionne de manière fiable, à grande échelle, sans chef, et sans besoin confiance.

# Le fonctionnement de la preuve de travail
<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>

## Le parcours de la transaction Bitcoin
<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>

Avant de comprendre ce qu'est le minage de Bitcoin, il faut d’abord suivre le trajet d’une transaction typique sur Bitcoin. Cela permet de voir où intervient exactement le bloc, et pourquoi il est au cœur du système. C'est ce que je vous propose de découvrir dans ce premier chapitre.

Sur Bitcoin, une transaction est une structure de données qui transfère la propriété de bitcoins d'un utilisateur à un autre. Concrètement, elle consomme des `outputs` de transactions passées (ce qu'on appelle des UTXO) en les référant comme `inputs`, puis elle crée de nouveaux `outputs` qui définissent à qui appartiennent désormais ces bitcoins et sous quelles conditions ils pourront être dépensés plus tard.

![Image](assets/fr/001.webp)

Un point important sur Bitcoin est l’autorisation de dépenser. Les bitcoins ne sont pas dans un comptes, comme le pourraient être votre argent à la banque, mais ils sont verrouillés par des conditions de dépense. Lorsqu’un portefeuille veut utiliser un UTXO comme `input`, il doit fournir une preuve cryptographique qui atteste qu'il a bien le droit de le déverrouiller. Cette preuve prend souvent la forme d’une signature numérique produite à partir d’une clé privée. C’est pour cette raison que les bitcoiners insistent sur la nécessité de sécuriser vos clés privées : ce sont elles qui permettent de déverrouiller l’accès à vos bitcoins et, par conséquent, de les dépenser.

![Image](assets/fr/002.webp)

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

![Image](assets/fr/003.webp)

### La mempool : la salle d’attente des transactions

Entre le moment où une transaction est diffusée et le moment où elle est confirmée dans un bloc, elle doit attendre. Cette zone d’attente s’appelle **la mempool** (contraction de `memory` et `pool`). Une mempool est donc un espace de stockage temporaire de transactions valides, mais encore non confirmées.

Point important : il n’existe pas une mempool unique, mais des mempools. En effet, chaque nœud maintient la sienne, avec ses propres contraintes locales. Cela implique qu’à un instant donné, deux nœuds peuvent avoir des contenus de mempool légèrement différents (selon ce qu’ils ont reçu, ce qu’ils ont rejeté, ou ce qu’ils ont purgé).

![Image](assets/fr/004.webp)

À ce stade, on a donc un réseau qui connaît la transaction, l’a vérifiée, et la garde en mémoire en attendant qu’elle soit confirmée. Mais la confirmation de cette transaction n'arrivera que lorsqu'un mineur l’insère dans un bloc, et que ce bloc est accepté par le réseau.

### La blockchain : un registre public d’horodatage

Le bitcoin étant une monnaie immatérielle, elle doit répondre à un problème : empêcher la double dépense sans autorité centrale. Si deux transactions tentent de dépenser le même UTXO, il faut que tout le monde puisse converger vers un seul état cohérent. Satoshi Nakamoto résume cet enjeu avec cette phrase célèbre :

> Le seul moyen pour confirmer l’absence d’une transaction est d’être au courant de toutes les transactions.

Autrement dit, pour savoir qu’un bitcoin n’a pas déjà été dépensé, il faut disposer d’un registre commun des dépenses passées.

C’est le rôle de la blockchain : un registre public qui contient l’historique des transactions. Mais plutôt que d’écrire chaque transaction au fil de l’eau, Bitcoin les regroupe dans des blocs. Chaque bloc agit comme une page d’historique, et le système fonctionne ainsi comme un serveur d’horodatage : il ordonne les transactions dans le temps, de manière vérifiable.

Ce registre ne peut pas être réécrit grâce à un principe simple : chaque bloc inclut l’empreinte cryptographique (le hash) du bloc précédent. Ainsi, les blocs s’enchaînent : si vous modifiez un bloc du passé, son empreinte change, ce qui casse le lien avec le bloc suivant, ce qui casse le lien avec le bloc d’après, etc. C’est cette chaîne de dépendances qui donne son nom à la "*blockchain*".

![Image](assets/fr/005.webp)

Une fois que l'on a compris ces principes de base de Bitcoin, on peut décrire l’objectif d’un mineur de manière plus concrète : construire un nouveau bloc qui prolonge la chaîne existante, en y inscrivant des transactions en attente, puis tenter de le rendre valide (c'est la fameuse "*preuve de travail*" que l'on étudiera dans un prochain chapitre). Mais d'abord, découvrons ensemble dans le prochain chapitre comment est construit un bloc candidat.

## La construction d'un bloc Bitcoin
<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>

Vous avez maintenant compris le parcours d’une transaction sur Bitcoin ainsi que le rôle de la blockchain. Avant d’étudier plus en détail le fonctionnement de la preuve de travail, il reste toutefois une étape essentielle que le mineur doit réaliser : la construction d’un bloc candidat. Découvrons ensemble ce qu’est un bloc candidat et comment le mineur le construit, avant de se lancer dans la recherche d’une preuve valide.

### Le bloc candidat

Les mineurs doivent fabriquer leur bloc eux-même avant d'essayer de le miner. Chaque mineur, de son côté, construit ce que l'on appelle un bloc candidat à partir des transactions en attente dans sa mempool. Construire un bloc candidat consiste donc à :
- choisir quelles transactions inclure ;
- organiser ces transactions de manière compatible avec les règles de Bitcoin ;
- produire les métadonnées du bloc, contenues dans son entête.

Le choix des transactions répond à une logique économique simple : un bloc a une capacité limitée par le protocole Bitcoin, donc le mineur cherche à maximiser ce qu’il gagne pour cet espace. Il sélectionne en priorité les transactions offrant les frais les plus élevés relativement à la place qu’elles occupent dans le bloc (on parle ainsi de "*taux de frais*", exprimé en `sats/vB`). Les détails des frais seront traités plus tard ; retenez ici simplement l’idée de tri par rentabilité de l’espace.

Un bloc Bitcoin se compose donc de deux grandes parties :
* une liste de transactions ;
* une entête de bloc, qui sert, en quelque sorte, de carte d’identité du bloc.

![Image](assets/fr/006.webp)

L’entête est essentielle, car c’est elle qui est utilisée comme base pour la preuve de travail : dans Bitcoin, on ne mine pas directement un bloc entier ; on mine uniquement l’entête d'un bloc, qui résume les informations nécessaires pour lier le bloc à la chaîne et engager son contenu. Pour que l’entête puisse représenter l’ensemble des transactions, Bitcoin utilise un outil cryptographique : l’arbre de Merkle.

### L’arbre de Merkle : résumer un grand ensemble de transactions

Lister toutes les transactions dans l’entête serait impossible : un bloc peut contenir des milliers de transactions, alors que l’entête a une taille fixe (80 octets). La solution consiste donc à calculer un hachage unique qui dépend de toutes les transactions du bloc : c'est la racine de Merkle.

Le principe est le suivant :
* on calcule l’empreinte cryptographique de chaque transaction ;
* on regroupe ces empreintes deux par deux, on les met bout-à-bout, puis on les hache de nouveau pour obtenir une nouvelle couche d’empreintes ;
* on répète cette opération jusqu’à obtenir une seule empreinte finale : la racine de Merkle.

![Image](assets/fr/007.webp)

Ainsi, si une seule transaction change, même d’un seul bit, cela entraîne une modification de son empreinte, laquelle se propage jusqu'à la racine de Merkle. Or cette racine est incluse dans l’entête du bloc. Donc modifier une transaction passée revient à modifier l’entête du bloc dans lequel elle est incluse, et donc l’empreinte du bloc, puis le lien avec les blocs suivants.

Depuis SegWit, on sépare ce qui relève des signatures (témoins) du reste. Il y a donc en réalité 2 arbres de Merkle imbriqués dans chaque bloc. Cette séparation a des conséquences sur la manière de compter la taille d’un bloc et sur certains engagements cryptographiques, mais l’idée de base reste la même : l’entête doit engager, de manière compacte, tout le contenu du bloc.

### L’entête de bloc

L’entête de bloc fait 80 octets et contient exactement 6 champs. Ce sont ces six éléments qui seront hachés lors de la recherche d'une preuve de travail (voir chapitre suivant) :

- La version (`version`) : Elle indique quelles règles ou quels signaux de mise à jour le bloc utilise. C’est un mécanisme de compatibilité et d’évolution du protocole.

- L’empreinte du bloc précédent (`previousblockhash`) : C’est le hash de l’entête du bloc précédent. C’est lui qui enchaîne les blocs entre eux. Sans ce champ, on aurait des blocs indépendants. En incluant le hash de l'entête du bloc précédent, on obtient une chaîne, où chaque nouveau bloc s’appuie sur le précédent.

- La racine de Merkle (`merkleroot`) : C’est l'empreinte de toutes les transactions du bloc (via l’arbre de Merkle). Elle lie l’entête au contenu : si le mineur modifie la sélection ou l’ordre des transactions, la racine change.

- L’horodatage (`time`) : C’est un timestamp (temps Unix) choisi par le mineur (avec des contraintes de validité), qui doit indiquer quand le bloc a été miné. Il n’a pas besoin d’être parfaitement exact à la seconde près, mais il doit respecter certaines conditions pour rester acceptable par le réseau.

- La cible de difficulté encodée (`nbits`) : Ce champ encode la cible de difficulté en vigueur. Nous détaillerons ce point dans le chapitre sur la difficulté, mais retenez ici que ce paramètre fait partie de l’entête.

- Le nonce (`nonce`) : C’est une valeur que le mineur peut modifier librement. Elle sert de variable d’ajustement durant la preuve de travail. Je vous expliquerai son rôle plus précisément dans le prochain chapitre, mais il est important de comprendre que le nonce fait partie de l’entête du bloc et qu’il est prévu pour permettre des essais successifs.

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
nbits: b2e00517
nonce: 43f09a40
```

Cette entête du bloc candidat construit par le mineur constitut sa base de travail. Lors de la recherche d'une preuve de travail valide, ce n’est pas la liste entière des transactions qui est directement hachée en boucle, mais bien ce bloc de 80 octets, qui contient tout ce qu’il faut pour lier le bloc au passé et engager son contenu, tout en embarquant les paramètres nécessaires au mécanisme de minage, que nous allons justement découvrir dans le chapitre suivant.

## Le hachage, la cible et le nonce
<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>

Dans les chapitres précédents, vous avez suivi le chemin d’une transaction Bitcoin : créée et signée par un portefeuille, relayée par les nœuds, stockée dans les mempools, puis confirmée lorsqu’un mineur l’inclut dans un bloc accepté par le réseau. Mais nous n'avons pas encore vu comment un mineur peut ajouter son bloc à la blockchain. Quel est le processus derrière le minage ?

Comprendre le processus du minage, c'est assez simple. Cela tient en 3 notions qui vont ensemble : une fonction de hachage, une valeur cible et une variable que le mineur peut modifier. Voyons ensemble comment tout cela fonctionne.

### La fonction de hachage

Une fonction de hachage est un outil qui prend un message en entrée et produit une sortie de taille fixe, qu'on appelle "*empreinte*" ou "*hash*".

![Image](assets/fr/010.webp)

La fonction de hachage est intéressante dans des systèmes informatiques, car elle dispose de certaines propriétés :

* Si vous changez un seul bit de l’entrée, l’empreinte obtenue en sortie change totalement et de manière imprévisible ;

![Image](assets/fr/011.webp)

* Il est impossible de remonter de la sortie vers l’entrée : la fonction est irréversible ;

![Image](assets/fr/012.webp)

* Il est impossible de trouver deux messages différents qui donnent exactement la même empreinte.

![Image](assets/fr/013.webp)

La fonction de hachage utilisée dans Bitcoin pour le minage est `SHA256`, appliquée deux fois de suite. On parle de double SHA256, noté `SHA256d`. C’est cette double application qui produit l’empreinte du bloc.

```text
hash = SHA256(SHA256(message))
```

Dans notre cas, le `message` correspond en fait à l’entête du bloc, que vous avez vu au chapitre précédent. Pour rappel, l’entête est une petite structure qui résume tout ce qu'il y a dans le bloc.

![Image](assets/fr/014.webp)

### La preuve de travail : trouver une empreinte inférieure à une cible

La Proof-of-Work est souvent décrite comme le fait de résoudre un problème complexe. En réalité, il ne s’agit pas vraiment d'un problème, mais plutôt d’une recherche par tâtonnement : le mineur doit trouver une version de l’entête dont l’empreinte (après passage dans la fonction de hachage `SHA256d`) respecte une condition simple : qu'elle soit inférieure à une certaines cible.

Cette condition se formule ainsi :
* on calcule l’empreinte de l’entête du bloc à l'aide de la fonction de hachage ;
* on interprète cette empreinte comme un nombre ;
* pour que le bloc soit valide, ce nombre doit être inférieur ou égal à une valeur appelée "*cible de difficulté*" ou "*facteur de difficulté*".

Autrement dit, un bloc est valide si :

```text
SHA256d(block_header) <= target
```

![Image](assets/fr/015.webp)

La cible est un nombre de 256 bits. Comme l’empreinte produite par `SHA256d` fait aussi 256 bits, on peut les comparer comme deux nombres. Plus la cible est basse, plus la condition à remplir est difficile, car il existe moins de résultats possibles en dessous de ce seuil. À l’inverse, plus la cible est élevée, plus la condition est facile à satisfaire, et plus le minage d’un bloc devient simple. Nous détaillerons dans les prochains chapitre comment cette cible est déterminée.

Dans ce système, la fonction de hachage est intéressante. Rappelez-vous qu’il est facile de calculer la sortie à partir de l’entrée, mais qu’il est impossible de retrouver une entrée en ne connaissant que la sortie de la fonction. Dans le cadre du minage, on ne demande pas aux mineurs de trouver une empreinte précise, mais plutôt de trouver une empreinte inférieure à une valeur cible. Le seul moyen d’y parvenir consiste à effectuer un très grand nombre de tentatives, jusqu’à ce qu’une entête particulière de leur bloc candidat, une fois hachée, produise une empreinte inférieure à cette cible.

À partir du moment où la cible est suffisamment basse, ce processus devient coûteux. Le mineur calcule le hash de l’entête de son bloc candidat, vérifie le résultat, puis, si la condition n’est pas remplie, modifie l’entête et recommence le calcul. Cette boucle se répète jusqu’à ce qu’une entête valide soit trouvée. Lorsque le hash de l’entête satisfait enfin la condition, la preuve de travail est établie, le bloc est considéré comme valide et peut être diffusé sur le réseau Bitcoin afin que les nœuds l’ajoutent à leur blockchain. Le mineur gagnant reçoit alors la récompense associée (nous détaillerons sa composition plus tard), tandis que l’ensemble des mineurs repart immédiatement à la recherche d’une nouvelle entête valide pour le bloc suivant.

L’intérêt fondamental de ce mécanisme réside dans son asymétrie. Produire une preuve de travail est coûteux pour les mineurs, car cela nécessite un grand nombre de calculs de hachage. En revanche, pour les vérificateurs, c’est-à-dire les nœuds du réseau, la vérification est extrêmement simple : il suffit de hacher l’entête du bloc fournie par le mineur et de vérifier que l’empreinte obtenue est bien inférieure à la cible. Trouver une preuve demande donc beaucoup de travail et de ressources, tandis que vérifier sa validité est rapide et peu coûteux. C’est précisément cette propriété qui définit un système de preuve de travail efficace.

### Le nonce

Reste une question pratique : si l'entête du bloc candidat construit par le mineur ne donne pas une empreinte valide, comment le mineur peut-il réessayer ? Il lui faut modifier quelque chose dans l’entête afin d’obtenir une empreinte différente. C’est précisément le rôle du nonce.

Rappelez-vous la première propriété d’une fonction de hachage : modifier un seul bit de l’entrée suffit à produire une empreinte de sortie totalement différente et imprévisible. Chaque calcul de hash s’apparente donc à un tirage aléatoire.

![Image](assets/fr/016.webp)

Pour tenter à nouveau sa chance, le mineur n’a pas besoin de modifier entièrement l’entête de son bloc candidat : il lui suffit d’en changer une infime partie, car le moindre bit différent entraînera une empreinte complètement nouvelle, et potentiellement valide si elle est inférieure à la cible.

C’est précisément pour cette raison que l’entête de bloc contient un nonce. Le nonce est une valeur de 32 bits, utilisée une seule fois, puis remplacée. Concrètement, pour un même bloc candidat, un mineur peut ainsi tester environ 4,29 milliards de valeurs possibles (de `0` à `2^32 - 1`). Chaque variation du nonce modifie l’entête du bloc et, par conséquent, change intégralement l’empreinte produite après l’application de la fonction de hachage `SHA256d`.

Le processus de minage est donc très simple :
- le mineur construit un bloc candidat (transactions + entête) ;
- il calcule l'empreinte de l'entête `SHA256d(header)` ;
- si le résultat est supérieur à la cible, il change le nonce ;
- il recommence ;
- etc.

![Image](assets/fr/017.webp)

En réalité, le nonce n’est pas le seul champ que l’on peut modifier. Toute modification au sein des transactions d'un bloc entraîne un changement de la racine de l’arbre de Merkle, et donc une modification de l’entête de ce bloc. Avec la puissance de calcul moderne, parcourir les 4,29 milliards de valeurs possibles du nonce peut se faire relativement rapidement. C’est pourquoi il existe un autre champ, que l’on appelle généralement "*extra-nonce*", qui permet de démultiplier encore les possibilités de variation de l’entête. Nous reviendrons plus en détail sur ce mécanisme dans un prochain chapitre.

### Quel est l'intérêt de la preuve de travail ?

On parle de "*preuve*" parce que le résultat est immédiatement vérifiable : une fois un bloc produit, n’importe quel nœud peut contrôler, en une fraction de seconde, que l’empreinte cryptographique de son entête est bien inférieure à la cible exigée. On parle de "*travail*" parce que parvenir à cette empreinte a requis une multitude d’essais, donc un coût réel en calcul et en énergie.

Dans le White Paper de Bitcoin, Satoshi Nakamoto met en avant deux intérêts à l'utilisation d'un système de preuve de travail dans Bitcoin :

- **Sceller l’historique économique :**

Une fois la charge de calcul dépensée, le bloc est figé : le modifier impliquerait de refaire la preuve de travail de ce bloc. Et comme les blocs sont enchaînés les uns avec les autres, altérer un bloc ancien obligerait aussi à recalculer tous les blocs suivants, puis à rattraper et dépasser le travail continu de la chaîne honnête.

Autrement dit, la preuve de travail sert d’armature à l'horodatage qui rend la falsification du passé de plus en plus coûteuse à mesure que les blocs s’accumulent. Lorsqu’un nouveau bloc est miné, la sécurité fournie par la preuve de travail s’applique de manière simultanée et uniforme à l’ensemble des UTXOs existants. À chaque bloc ajouté, chaque UTXO accumule ainsi une quantité supplémentaire de sécurité issue de la Proof-of-Work.

- **Définir la règle de majorité (consensus) et neutraliser les Sybil :**

La preuve de travail permet également à Bitcoin d’obtenir un consensus sans s’appuyer sur la règle de vote "*un identifiant = une voix*", qui pourrait être facilement truqué par la création massive d’identités (IP, nœuds, clés...).

Dans Bitcoin, la "*majorité*" n’est pas le plus grand nombre de participants, mais la **chaîne qui cumule le plus de travail**. Comme l’écrit Satoshi, c’est un principe "*un CPU = une voix*", c’est-à-dire un vote pondéré par la puissance de calcul réellement dépensée pour produire des blocs valides. Ainsi, déployer des milliers de nœuds n’apporte aucun avantage en soi sur Bitcoin. Sans puissance de calcul supplémentaire, on n’accumule pas davantage de preuve de travail, et l’attaque Sybil devient inutile, tandis que la règle de décision reste objective et ne nécessite aucune identification des participants.

![Image](assets/fr/018.webp)

[Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System.*](https://bitcoin.org/bitcoin.pdf)

Les principes liés à l’utilité et aux pouvoirs des mineurs constituent un sujet très complexe que je ne détaillerai pas davantage dans cette formation. Nous y reviendrons cependant de manière approfondie dans la future formation MIN 201.

Pour l’instant, vous pouvez résumer le fonctionnement du minage ainsi : les mineurs construisent un bloc candidat avec les transactions en attente dans les mempools, puis cherchent une empreinte de son entête (via `SHA256d`) qui soit inférieure ou égale à une cible. Ils y parviennent en testant des nonces par tâtonnement.

Dans le chapitre suivant, nous ferons un bref détour historique sur le principe de la preuve de travail afin d’en comprendre le contexte, puis nous verrons ensuite comment la cible de difficulté est déterminée par le système.

## L'histoire de la preuve de travail
<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>

La preuve de travail n’a pas été inventée pour Bitcoin. Satoshi Nakamoto a repris et assemblé plusieurs idées plus anciennes, déjà explorées dans des contextes différents.

### Hashcash

À la fin des années 1990, le problème du spam des e-mails devient important. En effet, si envoyer un e-mail coûte presque zéro, un spammeur peut en envoyer des millions. Mais si chaque message exige un petit effort de calcul, envoyer un seul message légitime reste facile pour un utilisateur normal, tandis qu’envoyer des millions de messages devient très cher.

C’est l’objectif de Hashcash, proposé par Adam Back en 1997, que l'on considère comme l'invention du principe de preuve de travail. Le principe de Hashcash ressemble fortement au minage : produire un hash qui respecte une condition (avoir un certain nombre de zéros en début d’empreinte). La preuve accompagne ensuite le message et peut être vérifiée très rapidement par le destinataire. En cas de réception d’un e-mail ne contenant pas cette preuve, celui-ci peut être immédiatement considéré comme du spam, et donc filtré. Les spammeurs sont alors contraints de dépenser une quantité d’énergie considérable pour envoyer des millions de messages, ce qui réduit drastiquement (voire annule complètement) la rentabilité de ce type d’opérations, qu’elles soient marketing ou frauduleuses.

De nos jours, Hashcash n’est pas utilisé pour les e-mails. Le filtrage du spam repose désormais en grande partie sur des systèmes centralisés. L’intérêt de Hashcash par rapport aux solutions actuelles réside dans le fait qu’il ne nécessite aucune centralisation du filtrage : chacun pourrait en ajuster les paramètres selon ses propres critères. Il ne requiert pas non plus d’identification, puisque la recherche d’un hash peut être effectuée de manière anonyme, et surtout, il ne s’appuie pas sur un système de réputation, lequel tend rapidement à introduire des formes de filtrage subjectives.

Hashcash ne cherchait pas à créer de la monnaie. Il cherchait à imposer un coût marginal à une action numérique facilement automatisable.

![Image](assets/fr/008.webp)

### Bit Gold

Nick Szabo, à la fin des années 1990 et au début des années 2000, explore l’idée d’une rareté numérique basée sur la preuve de travail. Son projet conceptuel, appelé Bit Gold, imagine la création d’unités de valeur en résolvant une preuve de travail coûteuse, puis en enregistrant ces preuves dans un registre afin d’établir une forme de propriété.

Bit Gold n’a pas abouti à un système déployé comme Bitcoin, mais il contient plusieurs intuitions importantes : l’idée que du calcul peut produire une rareté, et l’idée d'horodater des éléments dans le temps pour créer un historique difficile à réécrire.

### RPOW

Hal Finney propose en 2004 RPOW (*Reusable Proofs of Work*). L’idée est de produire des preuves de travail qui pourraient ensuite être échangées, plutôt que d’être simplement consommées. RPOW visait à créer des jetons numériques basés sur la preuve de travail, avec un système permettant de vérifier et de transférer ces jetons sans les dupliquer. RPOW, là encore, ne résout pas de façon satisfaisante le problème d’un registre totalement décentralisé comme Bitcoin le fera plus tard, mais il reste l'un des grands précurseurs de Bitcoin.

![Image](assets/fr/009.webp)

Hashcash, Bit Gold et RPOW utilisent la preuve de travail pour imposer un coût et créer une forme de rareté. Bitcoin reprend ce mécanisme, mais lui donne un rôle central et collectif : la preuve de travail ne sert pas seulement à créer quelque chose, elle sert à départager qui a le droit d’écrire la prochaine page du registre (le prochain bloc), et à rendre ce registre coûteux à falsifier.

## L'ajustement de la cible de difficulté
<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>

Dans les chapitres précédents, vous avez vu le cœur de la preuve de travail : les mineurs hachent l’entête de leur bloc candidat avec `SHA256d`, et le bloc n’est considéré valide que si l’empreinte obtenue est numériquement inférieure ou égale à une valeur de référence appelée la cible. Il reste alors une question : d’où vient cette cible, et comment le système s’assure qu’elle reste cohérente au fil du temps ?

Bitcoin vise un rythme moyen d’un bloc trouvé toutes les 10 minutes. Ce rythme n’est évidemment pas une promesse à la seconde près. En pratique, certains blocs sont trouvés quelques secondes après le précédent, quand d’autres le sont après plus d'une heure. Ce qui importe ici, c’est la moyenne sur une période suffisamment longue.

![Image](assets/fr/019.webp)

Cette variabilité découle du caractère probabiliste du minage : chaque hachage est un essai indépendant, avec une probabilité constante (à cible inchangée) de produire un résultat inférieur à la cible. On peut donc le comparer à une loterie au tirage continu : plus les mineurs effectuent de hachages par seconde, plus le délai attendu avant l’apparition d’un bloc valide diminue, mais sans jamais supprimer l’aléa d’un tirage à l’autre.

### Pourquoi viser 10 minutes entre les blocs ?

Même si l'on n'a aucune preuve de cela, Satoshi Nakamoto a sûrement choisi 10 minutes comme un compromis pratique entre efficacité et sécurité. Un intervalle plus court donnerait des confirmations plus fréquentes, mais provoquerait davantage de divisions temporaires du réseau. Pour comprendre ce point, il faut revenir à la manière dont un bloc se propage.

Lorsqu’un mineur trouve un bloc valide, il le diffuse immédiatement à ses pairs. Les nœuds qui le reçoivent vérifient sa validité (transactions, preuve de travail, règles de consensus...), puis le relaient à leur tour. Cette propagation prend un certain temps, limité par la latence d'Internet, la bande passante, et la capacité de chaque nœud à vérifier le bloc.

![Image](assets/fr/020.webp)

Si, durant ce délai de diffusion, un autre mineur découvre lui aussi un bloc valide à la même hauteur, le réseau peut se retrouver temporairement scindé : une partie des nœuds et des mineurs se base sur le bloc A, tandis que l’autre se base sur le bloc B. C'est une division temporaire du réseau.

![Image](assets/fr/021.webp)

Ces divisions ne sont pas catastrophiques. Le consensus de Nakamoto prévoit qu’à terme, une seule branche l’emportera : celle qui accumule le plus de travail. En effet, dès qu’un nouveau bloc est miné par-dessus le bloc A par exemple, l’ensemble du réseau se resynchronise sur cette branche et abandonne le bloc B, qui devient alors un "*stale block*", parfois appelé à tort un "*bloc orphelin*" dans le langage courant.

![Image](assets/fr/022.webp)

En revanche, elles ont un coût : pendant quelques minutes, une fraction des mineurs travaille sur une branche qui sera abandonnée. Ce travail est alors gaspillé du point de vue de la sécurité globale, car il n’a pas contribué à la chaîne finale. Plus l'intervalle entre chaque bloc est rapide, plus la probabilité de ces divisions augmente, puisque le temps de propagation représente une part plus importante du temps entre chaque bloc.

L’intervalle de 10 minutes laisse généralement suffisamment de temps pour que le bloc gagnant se propage largement avant qu'un éventuel bloc à la même hauteur soit trouvé. C’est un compromis qui limite les divisions, réduit le gaspillage de la puissance de calcul, et aide le réseau à rester synchronisé à l’échelle mondiale.

### Comprendre la notion de hashrate

Le "*hashrate*" désigne la quantité de calcul de hachage produite par seconde, que ce soit par un seul mineur, par un groupe de mineur, ou bien par l'ensemble des mineurs sur Bitcoin. On l’exprime en `H/s` (hachages par seconde), avec des multiples comme `TH/s` (térahashs par seconde) ou `EH/s` (exahashs par seconde). Cela représente donc le nombre d’essais que les mineurs peuvent faire chaque seconde pour tenter d’obtenir un hash inférieur à la cible.

Si la cible reste fixe, alors :
* chaque essai a une probabilité fixe de réussite ;
* faire plus d’essais par seconde augmente la probabilité qu’un essai gagnant apparaisse rapidement.

Autrement dit, si demain le réseau Bitcoin double sa puissance de calcul en branchant deux fois plus de machines de minage, sans mécanisme correcteur, les blocs seraient trouvés en moyenne deux fois plus vite. Il faut donc ajuster la cible pour compenser les variations de hashrate.

### L'ajustement de la cible de difficulté

Bitcoin résout ce problème avec un mécanisme d’ajustement périodique de la cible, qui vient donc ajuster la difficulté du minage. Le principe est le suivant : tous les 2016 blocs (environ toutes les 2 semaines), chaque nœud recalcule la cible de difficulté en observant combien de temps a réellement été nécessaire pour produire ces 2016 blocs.

L’objectif de ce mécanisme est de ramener le temps moyen de production d’un bloc autour de 10 minutes, alors que le hashrate global du réseau varie en permanence, en raison de machines qui se débranchent ou, au contraire, de nouvelles machines qui sont ajoutées.

![Image](assets/fr/023.webp)

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

Pour bien comprendre l'ajustement de la difficulté du minage de Bitcoin, voici un exemple avec des valeurs fictives :

```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```

Avec :
* **`To = 18 045 755 102`** : Ancienne cible, c’est-à-dire la valeur de référence avant l’ajustement.
* **`Ta = 1 000 000` secondes** : Temps réellement passé pour produire les 2016 derniers blocs. Ce temps étant inférieur au temps cible, le réseau a miné trop rapidement.
* **`1 209 600` secondes** : Temps cible correspondant à 10 minutes par bloc pour 2016 blocs, utilisé comme référence pour l’ajustement.
* **`Tn = 14 918 779 020`** : Nouvelle cible calculée après l’ajustement de difficulté.

La nouvelle cible est ici plus basse que l’ancienne, ce qui implique une augmentation de la difficulté de minage afin de ralentir la production des blocs lors de la période suivante.

*Les valeurs des cibles dans cet exemple sont simplifiées et mises à l’échelle à des fins pédagogiques ; la cible réelle utilisée sur Bitcoin est un entier sur 256 bits d’un tout autre ordre de grandeur.*

Ce calcul est exécuté localement par chaque nœud, à partir des horodatages inscrits dans les blocs. Comme tous les nœuds appliquent les mêmes règles, ils aboutissent au même résultat, et la nouvelle cible devient la référence commune pour les 2016 blocs suivants.

Il y a un détail important à noter sur cet ajustement : **il est borné**. Bitcoin limite la variation de difficulté par période afin d’éviter des changements trop brutaux qui pourraient le bloquer. En effet, le temps réel pris en compte est contraint à rester dans une fourchette équivalente à un facteur 4 (au minimum un quart de l'ancienne cible, au maximum quatre fois l'ancienne cible). Cela empêche un reciblage extrême si les horodatages étaient très atypiques ou manipulés.

### La représentation de la cible

Dans l’entête de bloc, la cible n’apparaît pas sous sa forme complète de 256 bits, car cela prendrait trop de place. À la place, le champ `nBits` (de 32 bits) encode la cible dans un format compact, comparable à une notation scientifique en base 256 : un exposant (1 octet) et un coefficient (3 octets). La cible complète est ensuite reconstruite à partir de ces deux valeurs. Nous n’allons pas entrer dans le détail ici, car le sujet est relativement complexe et n’apporte rien à la compréhension du minage. Retenez simplement que la cible n’est pas stockée de manière brute dans l’entête du bloc, mais sous une forme compacte.

Avec ce dernier chapitre de la première partie, nous avons fait le tour du fonctionnement de la preuve de travail sur Bitcoin : le mineur construit un bloc candidat en sélectionnant des transactions dans sa mempool, calcule l’entête du bloc candidat, la hache, compare l’empreinte obtenue à la cible de la période, puis recommence en modifiant le nonce jusqu’à obtenir une empreinte valide. Enfin, tous les 2016 blocs, le réseau recalcule une nouvelle cible afin de maintenir un temps moyen d’environ 10 minutes par bloc, malgré les variations permanentes du hashrate.


# Le système d’incitations du minage de Bitcoin
<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>

## La récompense de bloc
<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>

Vous vous en doutez sûrement : miner sur Bitcoin n’est pas une activité altruiste. Les mineurs ont des coûts bien réels : l’électricité pour faire tourner leurs ordinateurs qui minent, l'achat de matériel spécialisé, la masse salariale pour la maintenance, parfois des locaux et des systèmes de refroidissement. Pour que le système Bitcoin fonctionne, il faut donc aligner l’intérêt privé des mineurs avec l’intérêt collectif du réseau. C’est exactement le rôle de la récompense de minage. Elle incite les mineurs à investir dans la preuve de travail, à inclure des transactions valides, et à respecter les règles du protocole plutôt que de tenter de le corrompre.

Cette logique relève de la théorie des jeux : le protocole rend l’honnêteté rationnelle. Un mineur gagne de l’argent lorsqu’il produit un bloc valide accepté par les nœuds. À l’inverse, s'il essaie de tricher, son bloc sera rejeté par les nœuds, et il n’obtiendra rien. Comme produire un bloc a un coût, un bloc rejeté représente une perte sèche. Dans un environnement concurrentiel où des milliers d’acteurs cherchent simultanément un bloc valide, la stratégie la plus rentable, la plupart du temps, consiste donc à suivre strictement les règles et à maximiser son revenu de manière honnête.

Pour ce faire, le protocole Bitcoin prévoit que le mineur qui trouve un bloc valide remporte le droit d’y inclure une transaction particulière qui lui attribue une certaine somme de BTC. C'est ce que l'on appelle **la récompense de bloc**. Dans ce premier chapitre de cette partie, l’objectif est de comprendre de quoi elle est composée et comment elle est déterminée. Nous verrons plus tard comment la partie création monétaire évolue au fil du temps (avec les halvings) et comment elle est effectivement récupérée techniquement (via la transaction coinbase).

### De quoi se compose la récompense de bloc ?

Dans les chapitres précédents, nous avons vu comment les mineurs parviennent à trouver un bloc valide. Une fois qu’un mineur a trouvé une entête dont le hash est inférieur à la cible, son bloc candidat est considéré comme valide. Il peut alors le diffuser à l’ensemble du réseau Bitcoin. Le bloc est ajouté à la suite de la blockchain et permet de confirmer les transactions qu’il contient. 

C’est précisément cet événement (l’ajout effectif du bloc à la blockchain) qui déclenche l’attribution d’une récompense au mineur gagnant. Cette récompense se compose de deux éléments distincts que l'on additionne :
- **la subvention de bloc** ;
- **les frais de transaction**.

![Image](assets/fr/024.webp)

Voyons ensemble à quoi correspondent ces deux parties de la récompense.

### La subvention de bloc

La subvention de bloc correspond à la partie création monétaire de la récompense. Lorsqu’un mineur produit un bloc valide, le protocole l’autorise à créer un certain nombre de nouveaux bitcoins et à se les attribuer comme rémunération. Ces bitcoins sont créés ex nihilo. Ils n’existaient pas auparavant.

Toutefois, la quantité de bitcoins nouvellement créés n’est absolument pas arbitraire. Elle est strictement définie par les règles du protocole Bitcoin et identique pour tous les mineurs. Nous détaillerons ce mécanisme dans le chapitre suivant, car la subvention n’est pas une valeur fixe indéfiniment : elle est divisée périodiquement selon un calendrier précis. Pour l’instant, retenez simplement que :
- la subvention de bloc constitue une des deux composantes de la récompense de bloc ;
- elle est plafonnée et déterminée par le protocole, et non par le mineur (même si le mineur peut techniquement demander moins que le montant maximal prévu) ;
- elle crée des bitcoins à partir de rien.

Cette subvention joue principalement deux rôles au sein du protocole Bitcoin. Le premier est d’inciter les acteurs à participer au minage. Durant les premières années de Bitcoin (et c’est encore parfois le cas aujourd’hui) les frais de transaction étaient très faibles. La subvention garantissait donc une rémunération suffisante pour attirer des mineurs et maintenir un niveau de sécurité pour le système.

Le second rôle est lié à la distribution de la monnaie. Toute nouvelle monnaie fait face à une question : comment distribuer les unités monétaires de manière juste à la population ? La subvention de bloc apporte une réponse à ce problème. En créant des bitcoins via le minage, elle permet leur distribution initiale de façon ouverte et neutre : n’importe qui peut en obtenir, à condition de participer au minage, sans autorisation préalable ni identification requise.

En revanche, puisque ces bitcoins sont créés à partir de rien, leur valeur ne provient pas de nulle part. En augmentant la quantité de monnaie en circulation, la subvention dilue mécaniquement la valeur des bitcoins déjà existants. Elle introduit donc une forme d’inflation monétaire. Nous verrons toutefois dans le prochain chapitre que cette subvention est destinée à disparaître progressivement, et qu’à terme, cette inflation cessera.

![Image](assets/fr/025.webp)

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

![Image](assets/fr/027.webp)

La somme des inputs est donc de `250 000 sats`, tandis que la somme des outputs est de `247 000 sats`. Cela signifie que `3 000 sats` ont été consommés en inputs sans être recréés en outputs : ce montant correspond aux frais proposés par cette transaction.

![Image](assets/fr/028.webp)

Si un mineur inclut cette transaction dans un bloc valide, il aura le droit de récupérer ces `3 000 sats`, en plus des frais de toutes les autres transactions incluses dans le bloc. En revanche, il n’existe aucun lien direct on-chain entre la transaction qui paie les frais et les sats effectivement perçus par le mineur. Techniquement, les `3 000 sats` de frais sont détruits, et, en contrepartie, le mineur obtient le droit de recréer la même somme pour lui-même.

#### Le ratio de frais

Un bloc n’est pas limité par le nombre de transactions, mais par sa capacité totale (aujourd’hui, en pratique, par le poids du bloc). Certaines transactions prennent plus de place que d’autres : une transaction avec de nombreux inputs et outputs sera plus volumineuse qu’une transaction simple avec un seul input et deux outputs. Les scripts utilisés vont aussi influencer la taille.

![Image](assets/fr/026.webp)

Deux transactions peuvent donc payer le même montant de frais en valeur absolue, mais ne pas être équivalentes économiquement du point de vue du mineur. Si l’une est deux fois plus grosse, elle coûte deux fois plus d’espace dans le bloc. Or l’espace est rare : le mineur cherche donc à maximiser ses revenus par unité d’espace.

C’est la raison pour laquelle, dans la pratique, on exprime la compétitivité d’une transaction avec un taux de frais, généralement en `sats/vB` (satoshis par octet virtuel). Le calcul de ce ratio est très simple :

```text
fee rate = fee / weight (in vB)
```

Par exemple, si l'on a une transaction qui pèse `141 vB` et qui alloue `1 974 sats` de frais, elle va avoir un taux de frais de `14 sats/vB`.

```text
1 974 / 141 ≈ 14 sats/vB
```

Ce ratio explique les choix économiques des mineurs : à capacité fixe, inclure des transactions à taux élevé maximise les frais totaux du bloc, donc la rémunération du mineur. C’est aussi ce qui explique les périodes où les transactions à bas frais restent longtemps en attente dans les mempools : elles sont en concurrence avec d’autres transactions qui payent davantage par unité d’espace.

### La protection du réseau contre le spam

Les frais ont également une utilité de sécurité opérationnelle : ils introduisent un coût à la multiplication de transactions. Si publier une transaction était gratuit, il serait facile d’inonder le réseau de transactions inutiles et de saturer les mempools, augmentant la charge sur les nœuds.

Dans la pratique, les nœuds appliquent des politiques locales de relais (règles de mempool) et fixent souvent un seuil minimal de frais en dessous duquel ils ne relaient pas une transaction (par défaut, `0.1 sat/vB` sur Bitcoin Core via `minRelayTxFee`). Une transaction peut être valide au sens strict des règles de consensus tout en étant non relayée par la plupart des nœuds si ses frais sont trop bas. Résultat : elle ne circule pas, n’atteint pas les mineurs, et a très peu de chances d’être confirmée.

À ce stade, vous avez compris l’essentiel de la récompense de bloc : elle correspond à la rémunération du mineur gagnant et se compose de deux éléments distincts. D’une part, une subvention de bloc, définie par les règles du protocole, qui crée de nouveaux bitcoins ex nihilo. D’autre part, les frais des transactions incluses dans le bloc miné.

Dans le chapitre suivant, nous allons nous concentrer plus en détail sur la subvention de bloc, afin de comprendre précisément comment elle est calculée et comment elle évolue au fil du temps selon les règles du protocole Bitcoin.

## Le halving
<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>

Dans le chapitre précédent, nous avons vu que les mineurs qui produisent un bloc valide reçoivent une récompense composée des frais des transactions incluses dans le bloc, ainsi que d’une subvention de bloc. En revanche, nous n’avons pas encore expliqué comment le montant de cette subvention est déterminé. Le mécanisme qui fixe et fait évoluer cette valeur est ce que l’on appelle le ***halving***.

### En quoi consiste le halving ?

Le halving est un événement programmé dans le protocole Bitcoin qui réduit de moitié la subvention de bloc, c’est-à-dire la quantité maximale de nouveaux bitcoins que le mineur gagnant est autorisé à créer à chaque bloc. Il ne concerne pas les frais de transaction : les frais existent indépendamment et restent déterminés par l’activité des utilisateurs et la concurrence pour l’espace de bloc.

Lors du lancement de Bitcoin en 2009, la subvention de bloc était fixée à 50 BTC pour chaque bloc miné. Depuis, cette subvention a été divisée par deux à plusieurs reprises, lors de chaque halving.

![Image](assets/fr/029.webp)

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

Comme la subvention de bloc suit une suite géométrique de raison 1/2 à chaque halving, la création monétaire a été extrêmement élevée aux débuts de Bitcoin, puis décroît très rapidement. Dès le 7ème halving, plus de 99 % des bitcoins auront déjà été mis en circulation. Le franchissement de ce seuil des 99 % devrait avoir lieu entre 2032 et 2036. Cela veut dire qu'il faudra ensuite plus de 100 ans pour miner le dernier 1 % des bitcoins restants. Si l’inflation monétaire était donc très forte au lancement de Bitcoin afin de permettre une distribution large de la monnaie, elle est aujourd’hui très faible et continuera de décroître, jusqu’à atteindre une véritable monnaie dure, dont l’offre en circulation ne pourra plus augmenter.

![Image](assets/fr/030.webp)

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
<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>

Dans les chapitres précédents, nous avons présenté deux points importants. D’une part, le mineur qui parvient à produire et diffuser un bloc valide reçoit une récompense. D’autre part, nous avons vu que cette récompense est composée de deux éléments distincts :
- une subvention de bloc (des bitcoins créés ex nihilo, dont le montant maximal est fixé par le protocole et diminue progressivement via les halvings) ;
- l’ensemble des frais de transaction payés par les utilisateurs dont les transactions ont été incluses dans le bloc.

Il reste toutefois une question : par quel mécanisme le mineur perçoit-il cette récompense sur Bitcoin ? C’est précisément le rôle d’une transaction particulière appelée "*coinbase*".

### Le fonctionnement de la transaction coinbase

Nous l’avons vu dans la première partie du cours : chaque bloc Bitcoin contient une liste de transactions en attente qu’il va venir confirmer. La toute première d’entre elles est toujours la transaction coinbase. C’est elle qui permet au mineur gagnant de percevoir sa récompense.

![Image](assets/fr/031.webp)

À première vue, elle ressemble à une transaction Bitcoin classique : elle possède un TXID, des outputs, et elle est incluse dans l’arbre de Merkle du bloc. Toutefois, elle se distingue par un point important : elle ne dépense aucun véritable UTXO existant.

Dans une transaction Bitcoin classique, les `inputs` référencent des outputs non dépensés antérieurs (UTXOs), qui apportent la valeur en entrée. Les `outputs` redistribuent ensuite cette valeur vers de nouveaux UTXOs, avec de nouvelles conditions de dépense. Autrement dit, pour envoyer des bitcoins, il faut déjà les posséder. La transaction coinbase, elle, ne consomme aucun bitcoin en input : elle crée directement des bitcoins en outputs à partir de rien.

C’est précisément ce mécanisme qui permet à la fois d’introduire de nouveaux bitcoins en circulation via la subvention de bloc, et de créditer le mineur des frais associés aux transactions incluses dans le bloc. La transaction coinbase ne peut pas référencer de véritable UTXO existant (en réalité, elle référence un UTXO fictif), puisque son rôle est justement de créer une partie de la valeur (la subvention) et de récupérer l’autre partie (les frais), sans les recevoir d’une transaction précédente. Pour que l’ensemble reste cohérent, la part correspondant aux frais doit exactement égaler la somme des bitcoins consommés en inputs mais non recréés en outputs dans les autres transactions du bloc.

![Image](assets/fr/032.webp)

Cette transaction n’est pas optionnelle. Un bloc qui ne contient pas de transaction coinbase est invalide et sera systématiquement rejeté par les nœuds du réseau.

⚠️ Précision utile : le terme "*coinbase*" n’a ici aucun lien avec la plateforme d’échange du même nom. Sur Bitcoin, "*coinbase*" désigne historiquement la transaction qui crée la récompense de bloc. L’entreprise a simplement repris ce terme pour son nom.

La transaction coinbase remplit en réalité plusieurs rôles simultanés :
- Le premier est celui que nous venons de détailler : elle attribue au mineur la récompense à laquelle il a droit pour avoir produit un bloc valide.
- Son second rôle, plus technique, est qu’elle sert de point d’ancrage à l’engagement cryptographique portant sur les témoins (les signatures) des transactions SegWit incluses dans le bloc.
- Un troisième rôle, cette fois-ci non directement protocolaire mais lié à l’industrialisation moderne du minage, est que la coinbase est aujourd’hui fréquemment utilisée pour ancrer des données arbitraires techniques. Ces données sont généralement liées au fonctionnement des pools de minage et à leur organisation interne.

Pour bien comprendre ces différents usages, nous allons maintenant détailler ces éléments en étudiant plus précisément la structure de la transaction coinbase.

### La structure de base de la transaction coinbase

Une transaction coinbase doit contenir exactement un seul input. On dit parfois, par simplification, qu’elle n’a pas d’input, car cet input ne dépense aucun UTXO réel. En réalité, il existe bien un input avec une source référencée, mais celle-ci pointe volontairement vers un UTXO inexistant.

En effet, comme nous l’avons déjà vu, toute transaction Bitcoin doit consommer des UTXOs en input afin de pouvoir créer des outputs valides. Cette consommation se matérialise, dans la transaction Bitcoin, par le référencement en input d’un UTXO existant. Ce référencement se fait simplement en indiquant l’identifiant de la transaction précédente (celle dans laquelle l’UTXO a été créé), ainsi que son index parmi les outputs de cette transaction. De manière très concrète, un UTXO est donc défini par un hash (le TXID précédent) et un index.

Mais dans le cas de la transaction coinbase, au lieu de référencer un véritable UTXO existant, l’input doit obligatoirement pointer vers ce faux UTXO particulier, avec un TXID plein de zéros, qui ne correspond à aucun TXID réel :

```text
0000000000000000000000000000000000000000000000000000000000000000
```

Directement suivi du faux index :

```text
0xffffffff
```

![Image](assets/fr/033.webp)

Dans le protocole Bitcoin de base, tel que décrit par Satoshi Nakamoto, ce faux input constitue la seule contrainte imposée à la transaction coinbase.

Comme tout UTXO référencé en input d'une transaction, il est associé à un champ `scriptSig`. Dans une transaction classique, ce champ `scriptSig` contient les éléments nécessaires pour satisfaire le `scriptPubKey` et ainsi déverrouiller l’UTXO dépensé. Mais dans le cas particulier de la coinbase, puisque l’UTXO référencé est volontairement fictif, le champ `scriptSig` est entièrement libre. Le mineur peut donc y inscrire n’importe quelle donnée. Nous verrons plus loin quels usages sont faits de cette liberté.

À ce faux input s’ajoutent ensuite, de manière tout à fait classique, un ou plusieurs outputs parfaitement standards, qui permettent au mineur de percevoir les bitcoins issus de la récompense sur l’une de ses adresses Bitcoin. Ces outputs sont des UTXOs verrouillés par un `scriptPubKey` (par exemple un script pointant vers une adresse contrôlée par le mineur ou par la pool). La seule particularité réside ici dans la règle de calcul de leur valeur : la somme totale des outputs de la coinbase ne doit jamais excéder la subvention maximale autorisée, à laquelle s’ajoutent les frais du bloc.

Historiquement, la transaction coinbase se résume donc à ce schéma simple : un faux input référençant un UTXO inexistant, et un ou plusieurs outputs destinés à distribuer la récompense de bloc au mineur gagnant. Toutefois, aujourd’hui, la coinbase ne se limite plus à ce rôle de distribution. Sa position particulière dans le bloc et la grande flexibilité de sa structure ont conduit à de nouveaux usages, à la fois au niveau du protocole lui-même et dans les mécanismes de gestion des pools de minage.

### Les autres usages de la coinbase

Au fil du temps, la transaction coinbase est devenue un point d’insertion particulièrement pratique pour intégrer diverses informations utiles au minage et à la structure même des blocs. Examinons-les afin de mieux comprendre l’organisation globale de la coinbase.

#### Le BIP-34

Le BIP-34 est un soft fork déployé en mars 2013, à partir du bloc 227 930, qui a introduit la version 2 des blocs Bitcoin. Cette nouvelle version impose que chaque bloc inclue, dans le `scriptSig` de la transaction coinbase, la hauteur du bloc en cours de création.

Cette évolution permet, d’une part, de clarifier la manière dont le réseau s’accorde pour faire évoluer la structure des blocs et les règles de consensus. D’autre part, elle force l’unicité de chaque bloc ainsi que de chaque transaction coinbase.

Ainsi, le `scriptSig` de la coinbase n’est pas totalement libre. Depuis l’activation du BIP-34, il est simplement contraint de commencer par la hauteur du bloc dans lequel cette transaction coinbase est incluse.

![Image](assets/fr/035.webp)

#### L’extra-nonce

Nous l’avons vu dans les premiers chapitres de ce cours : dans l’entête de bloc, le mineur dispose d’un champ `nonce` de 32 bits qu’il modifie par tâtonnement afin de trouver un hachage inférieur ou égal à la cible. Cet espace de 32 bits permet déjà d’explorer un très grand nombre de combinaisons, mais lorsque la difficulté de minage est élevée, cette plage peut être parcourue intégralement en un temps relativement court, et donc ne permettre aucune combinaison donnant un hash valide. Si toutes les valeurs possibles du `nonce` ont été testées sans succès, le mineur doit alors modifier un autre élément afin de faire varier l’entête du bloc et relancer une nouvelle série d’essais.

Comme la transaction coinbase offre un champ libre via le `scriptSig` de son input, la solution utilisée pour étendre l’espace du nonce consiste à exploiter une partie de ce `scriptSig`. C’est ce que l’on appelle généralement l’extra-nonce. En modifiant l’extra-nonce, le mineur modifie le `scriptSig` de la coinbase, donc l’identifiant de cette transaction, puis la racine de Merkle du bloc, et enfin l’entête du bloc lui-même. Il obtient ainsi un nouvel espace de recherche de hachages à explorer, sans avoir à toucher aux autres composantes de son bloc candidat.

![Image](assets/fr/036.webp)

#### L’identification des pools et des mineurs

Aujourd’hui, une part très importante du hashrate mondial est organisée au sein de pools de minage. Ces structures regroupent des hacheurs individuels afin de mutualiser le travail et de réduire la variance de leurs revenus.

Pour des raisons opérationnelles, les pools de minage exploitent également le champ libre du `scriptSig` de l’input de la coinbase pour y insérer différentes informations. Celles-ci varient selon les pools et selon le protocole réseau utilisé, mais on y retrouve généralement un identifiant unique (souvent un extra-nonce structuré en plusieurs sous-parties) attribué à chaque hacheur afin d’éviter la duplication du travail au sein de la pool. On y ajoute généralement un tag d’identification de la pool, utilisé pour l’attribution publique des blocs trouvés, les statistiques de minage, et d’autres besoins de suivi.

![Image](assets/fr/037.webp)

#### L’engagement de SegWit

Depuis le soft fork SegWit activé en 2017, les données de témoins (c’est-à-dire généralement les signatures) sont séparées des données de base des transactions, notamment afin de corriger le problème de malléabilité des transactions Bitcoin. Cette séparation introduit donc un nouvel élément à engager dans le bloc.

Pour cela, les témoins sont regroupés au sein d’un autre arbre de Merkle dédié, dont la racine est ensuite engagée dans la transaction coinbase via un output `OP_RETURN`.

![Image](assets/fr/038.webp)

Je ne détaillerai pas davantage ce mécanisme dans ce cours, car il sort de son périmètre, mais retenez simplement que depuis l’introduction de SegWit, la transaction coinbase sert de support pour ancrer dans le bloc une empreinte résumant l’ensemble des témoins SegWit. Les témoins sont placés dans un arbre de Merkle indépendant, la racine de cet arbre est inscrite dans un output de la transaction coinbase, et cette transaction coinbase est elle-même incluse dans l’arbre de Merkle principal avec toutes les autres transactions, dont la racine figure dans l’entête du bloc. C'est de cette manière qu'on engage les témoins, pourtant séparés, dans l'entête.

![Image](assets/fr/039.webp)

#### Les messages arbitraires

Puisque le `scriptSig` permet d’insérer librement des informations au choix du mineur, certains en ont profité pour y ajouter des messages non pas techniques, mais d’ordre plus personnel. Le cas le plus célèbre est évidemment celui de Satoshi Nakamoto, avec son message devenu emblématique :

> The Times 03/Jan/2009 Chancellor on brink of second bailout for banks

Ce message, présent dans le bloc de Genèse (le tout premier bloc de Bitcoin) est en réalité encodé en hexadécimal dans le `scriptSig` de la transaction coinbase :

```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```

![Image](assets/fr/034.webp)

### La période de maturité

Une fois le bloc miné et diffusé, la transaction coinbase apparaît dans la blockchain comme n’importe quelle autre transaction. Elle crée des UTXOs au bénéfice du mineur gagnant, lui permettant de récupérer sa récompense. Toutefois, ces UTXOs ne sont pas immédiatement dépensables : ils sont soumis à une période de maturité. Cette maturité est fixée à 100 blocs après le bloc qui contient la coinbase. Concrètement, la transaction coinbase doit donc totaliser 101 confirmations pour que ses outputs deviennent dépensables par le mineur gagnant.

![Image](assets/fr/040.webp)

L’objectif de cette règle est de limiter l’impact des réorganisations de chaîne sur l’économie. Comme nous l’avons vu dans les chapitres précédents, il arrive qu’à une même hauteur, deux blocs valides distincts soient trouvés presque simultanément par des mineurs différents. Pendant un court instant, le réseau peut alors se scinder : certains nœuds reçoivent d’abord le bloc A, tandis que d’autres voient d’abord le bloc B. Puis, au fil des blocs suivants, l’une des deux branches accumule davantage de travail et devient la branche de référence. L’autre branche est abandonnée et ses blocs deviennent obsolètes. Les transactions qu’elle contenait peuvent alors, en théorie, retourner dans les mempools en attente de confirmation.

Dans la pratique, cela arrive rarement, car le marché des frais conduit souvent à retrouver quasiment les mêmes transactions dans deux blocs concurrents à une même hauteur. C’est notamment pour cette raison qu’il est courant de considérer qu’une transaction Bitcoin devient immuable après six confirmations : les réorganisations de plus de six blocs sont si peu probables qu’on peut raisonnablement les considérer comme impossibles.

![Image](assets/fr/041.webp)

Le problème posé par ces réorganisations dans le cas de la transaction coinbase est qu’il ne s’agit pas d’une transaction ordinaire. Elle introduit des bitcoins tous neufs en circulation. Si la récompense de bloc pouvait être dépensée immédiatement, une situation problématique en cascade pourrait apparaître :
- un mineur dépense des bitcoins issus d’une coinbase,
- ces bitcoins circulent dans l’économie,
- puis le bloc d’origine est finalement abandonné lors d’une réorganisation.

Les bitcoins ayant circulé n’auraient alors jamais existé dans la chaîne finale, et une série de transactions pourtant valides au moment de leur émission deviendraient invalides a posteriori.

La période de maturité impose donc un délai suffisamment long pour rendre ce scénario irréaliste. Une réorganisation de 101 blocs est considérée, en pratique, comme impossible (même s’il subsiste toujours une probabilité infinitésimale). On ne sait pas précisément pourquoi Satoshi a choisi une valeur aussi élevée pour la maturité, mais il est probable qu’elle ait été retenue afin que le mécanisme reste fonctionnel, même en cas de gros dysfonctionnements au niveau du réseau.

Cette règle évite donc que la monnaie nouvellement créée via la récompense de bloc ne commence à circuler avant que le bloc qui l’a engendrée ne soit extrêmement solidement ancré sous une grande quantité de travail accumulé.

---

Nous arrivons désormais à la fin de cette explication consacrée au fonctionnement du minage de Bitcoin. Vous devriez à présent avoir une vision claire des mécanismes fondamentaux en jeu.

Dans la dernière partie de la formation, nous allons revenir à des aspects plus concrets, afin de vous montrer comment le minage de Bitcoin se matérialise dans le monde réel : son industrialisation, les machines utilisées, le regroupement des acteurs, etc. L’objectif sera d’aboutir à une vision d’ensemble du minage de Bitcoin, à la fois sous l’angle théorique et protocolaire que nous venons de voir, mais aussi dans sa dimension pratique et opérationnelle.

# L'industrie du minage de Bitcoin
<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>

## L'évolution des machines de minage
<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>

Au début de Bitcoin, miner n’avait rien d’une activité industrielle. Cela faisait partie du logiciel Bitcoin, lancé sur un ordinateur personnel, souvent par curiosité, parfois pour soutenir le réseau, et accessoirement pour récupérer des bitcoins qui n’avaient alors quasiment aucune valeur marchande.

Au fil des années, cette activité a connu une transformation : les machines ont changé, la difficulté a explosé, et le minage est devenu une industrie à part entière. Découvrons ensemble ces aspects opérationnels du minage de Bitcoin.

### Les débuts : miner avec un CPU

En 2009 et dans les premières années, le minage se faisait principalement avec le processeur (CPU) d’un ordinateur classique. Bitcoin est alors un simple logiciel, qui endosse le rôle de wallet, de nœud et de mineur. Le simple fait de lancer le logiciel de Satoshi Nakamoto sur son ordinateur personnel suffisait alors pour participer au minage et, bien souvent, pour trouver des blocs.

Un CPU sait tout faire, mais il n’est optimisé pour rien. Il exécute des instructions très générales, avec une logique complexe. Pour une tâche comme le hachage répétitif des entêtes de bloc, ce n’est pas l’outil idéal, mais au démarrage du réseau, la difficulté est si faible que cela suffit largement pour trouver des blocs.

Cette période est importante, car elle nous rappelle un point important : la preuve de travail ne dépend pas d’une catégorie de matériel en particulier. Ce qui compte, c’est la capacité à calculer des hachages plus vite que les autres, à coût donné. Dès qu’un avantage technique apparaît, il se transforme mécaniquement en avantage économique. Mais dans l’absolu, il est toujours possible aujourd’hui de tenter de trouver des blocs Bitcoin à l’aide d’un CPU classique. C’est d’ailleurs l’approche adoptée par le projet NerdMiner par exemple. Les chances de découvrir un bloc sont quasiment nulles, mais il subsiste néanmoins une probabilité infinitésimale.

https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Le basculement vers les GPU

Assez vite, des mineurs ont compris que le goulot d’étranglement n’était pas la puissance, mais la capacité à effectuer énormément d’opérations similaires en parallèle. C’est exactement ce que savent faire les cartes graphiques (GPU). À l’origine, un GPU est conçu pour exécuter les mêmes opérations sur de grandes quantités de données. Cette architecture se prête très bien à une tâche comme le hachage répété : au lieu d’avoir quelques cœurs très polyvalents, on dispose de centaines, puis de milliers d’unités capables d’exécuter les mêmes instructions simultanément.

À consommation électrique comparable, un GPU peut produire bien plus de hachages par seconde qu’un CPU. En parallèle, le bitcoin dispose désormais d’un taux de change face au dollar, sa valeur augmente, et des plateformes d’échange font leur apparition. À partir de là, le minage commence à changer de nature. Il ne s’agit plus seulement de participer, mais de chercher à gagner de l'argent. On voit apparaître des configurations dédiées : des machines montées autour de plusieurs cartes graphiques, parfois sans écran, avec un système minimal et des logiciels spécialisés, dont le seul objectif est de miner.

C’est à ce moment-là que la difficulté de minage commence à exploser. Entre mi-2010 et mi-2011, elle est même multipliée par 1 000. Mécaniquement, la spécialisation s’amorce, tout comme les premières formes d’industrialisation, et les utilisateurs normaux, qui se contentent de faire tourner le logiciel Bitcoin sur leur ordinateur personnel, n’ont désormais plus qu’une probabilité très faible de trouver un bloc valide.

![Image](assets/fr/044.webp)

*Source: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*

Entre l’ère GPU et l’ère moderne des ASIC, on observe une phase intermédiaire : l’utilisation de FPGA. Un FPGA est un composant reprogrammable : il peut être configuré pour implémenter directement un circuit logique dédié à un calcul particulier, ici `SHA256d`. L’intérêt est de s’éloigner encore davantage du matériel généraliste (CPU/GPU) pour gagner en efficacité énergétique. Mais rapidement, les améliorations réalisées virtuellement sur les FPGA seront appliquées physiquement aux puces elles-mêmes : c'est l'arrivée des ASIC.

### L’arrivée des ASIC

L’étape finale de la spécialisation du matériel de minage est l’apparition des ASIC (*Application-Specific Integrated Circuits*). Un ASIC est une puce conçue pour une tâche unique. Dans le cas du minage Bitcoin, cette tâche est précisément l’exécution de `SHA256d` à une vitesse maximale et avec une efficacité énergétique optimale. Contrairement à un GPU, un ASIC ne sert pas à faire tourner des jeux, du rendu 3D ou de l’IA. Il sert à hacher, et c'est tout.

![Image](assets/fr/045.webp)

*ASIC S21 XP fabriqué par l'entreprise Bitmain.*

Cette spécialisation a deux conséquences majeures :
- La première est un saut de performance et d’efficacité. À génération équivalente, un ASIC produit un nombre de hachages par seconde très supérieur à un GPU, pour une consommation plus maîtrisée. Rapidement, miner avec un GPU devient non compétitif : même si cela fonctionne techniquement, le coût électrique dépasse largement les revenus espérés dans la plupart des contextes ;
- La seconde est un changement de modèle : l’investissement devient principalement du matériel industriel. Miner implique désormais d’acheter des machines conçues pour cela, de les alimenter en continu, de les refroidir, de les maintenir, et d’absorber leur obsolescence. Car un ASIC n’est pas éternel économiquement : lorsqu’une nouvelle génération plus efficace arrive sur le marché, les anciennes machines deviennent progressivement moins rentables, même si elles restent fonctionnelles.

À partir de là, on ne parle plus seulement d’un hobby. On parle d’un secteur où la compétitivité dépend d’une équation :
* coût de l’électricité ;
* coût du matériel et de son amortissement ;
* capacité à refroidir et opérer à grande échelle ;
* disponibilité et fiabilité des machines ;
* rapidité des communications ;
* etc.

### Les fermes de minage

Une machine isolée peut miner, mais en regroupant des centaines, puis des milliers d’ASIC dans un même lieu, on mutualise les coûts fixes, on optimise la logistique, et on se rapproche d’un modèle de data center spécialisé.

Une ferme de minage, dans sa forme la plus simple, c’est un bâtiment (ou un ensemble de conteneurs) rempli d'ASIC qui tournent 24/7. Le défi est dorénavant de maintenir des conditions d’exploitation stables :
* fournir une puissance électrique importante, à bas coût et stable ;
* gérer la chaleur afin d’éviter le throttle, car la densité énergétique est considérable ;
* filtrer la poussière, contrôler l’humidité, nettoyer ;
* surveiller en temps réel la performance des machines (températures, erreurs matérielles, baisse de hashrate...).

![Image](assets/fr/043.webp)

*L’un des sept bâtiments dédiés au minage de Bitcoin sur le site de Rockdale de Riot Platforms, à proximité d’Austin, au Texas. Celui-ci est spécifiquement dédié au minage par immersion.*

Le minage est désormais porté par des acteurs industriels, parfois cotés en bourse, qui construisent et exploitent des fermes à très grande échelle. On peut notamment citer MARA Holdings (Nasdaq: `MARA`) ou Riot Platforms (Nasdaq: `RIOT`).

![Image](assets/fr/042.webp)

Même sans entrer dans les détails des modèles de rentabilité, il est important de comprendre pourquoi le minage a pris cette forme. La preuve de travail est un mécanisme compétitif : la probabilité de trouver un bloc, et donc de gagner de l'argent, est proportionnelle à la part de hashrate que l’on déploie. Par conséquent, la pression est permanente pour augmenter la puissance de calcul, réduire le coût par unité de calcul et limiter les pertes. Dès lors, les environnements qui offrent de l’électricité moins chère, un climat favorable au refroidissement, ou une infrastructure énergétique abondante, deviennent naturellement plus attractifs.

Miner du Bitcoin est donc passé d’une activité accessible à n’importe qui à ses débuts, à une activité dominée par du matériel spécialisé et des opérations professionnelles. Cela ne change pas les règles du protocole. N’importe qui peut en théorie miner avec n'importe quelle machine. Mais en pratique, le niveau de difficulté et l’efficacité des ASIC ont rendu le minage domestique largement non compétitif dans la plupart des contextes.

Il subsiste évidemment des situations dans lesquelles le minage domestique peut présenter un intérêt, par exemple si vous bénéficiez d’une électricité très peu chère, ou si vous valorisez la chaleur dégagée par votre mineur, par exemple pour chauffer un logement en hiver. Mais dans tous les cas, vous devrez néanmoins acquérir une machine équipée d’une puce ASIC. De plus, puisque votre puissance de minage restera extrêmement limitée à l’échelle du réseau Bitcoin, il vous faudra trouver un moyen de réduire la variance de vos revenus : c’est précisément le rôle des pools de minage dont nous allons parler dans le prochaine chapitre.

Si vous souhaitez explorer des solutions de minage domestique avec valorisation de la chaleur, nous avons des tutoriels sur différents outils, à la fois prêts à l’emploi et en DIY :

https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Le regroupement en pools de minage
<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>

Le minage de Bitcoin implique des coûts continus et incompressibles, au premier rang desquels figure la consommation électrique des machines. Ces dépenses sont engagées indépendamment de tout résultat, alors même que les revenus issus du minage sont, par nature, rares et aléatoires. La découverte d’un bloc dépend exclusivement de la part de hashrate détenue par le mineur, ce qui rend les gains d’autant plus imprévisibles que cette part est faible. C’est précisément ce problème pratique qui a rapidement conduit à la généralisation des pools de minage. Je vous propose, dans ce dernier chapitre du cours MIN 101, une introduction aux principes et au fonctionnement des pools de minage sur Bitcoin.

### C’est quoi une pool de minage ?

Une pool de minage est une organisation (souvent un service en ligne) qui agrège la puissance de calcul de nombreux mineurs indépendants, afin d’augmenter la fréquence à laquelle leur groupe trouve des blocs. Quand la pool trouve un bloc, la récompense de bloc est ensuite redistribuée entre les participants selon des règles internes à la pool (qui seront abordées dans le cours MIN 201, car trop complexes pour MIN 101).

Les participants à une pool de minage sont alors souvent désignés comme des "*hacheurs*", et non plus comme des "*mineurs*", car ils n’effectuent plus l’ensemble du travail de minage, mais se contentent de hacher les données qui leur sont transmises par la pool.

Attention de ne pas confondre la pool de minage avec la ferme de minage. Ce sont deux concepts différents. Comme nous l'avons vu dans le chapitre précédent, une ferme est un site physique où une même entité opère de nombreuses machines de minage. Une pool, elle, est avant tout un regroupement virtuel : des milliers de machines, souvent dispersées géographiquement, travaillent sous une coordination commune. Une ferme peut toutefois participer à une pool, et c’est même souvent le cas.

![Image](assets/fr/048.webp)

### Réduire la variance des revenus

Mais alors pourquoi se regrouper en pool ? Tout simplement car le résultat de l'activité de minage est probabiliste : à chaque tentative de hachage, vous avez une chance infime de tomber sous la cible de difficulté et donc de produire un bloc valide.

Sur le très long terme, vos gains moyens devraient être proportionnels à votre part du hashrate global. Ce principe découle directement des lois de la probabilité : chaque calcul de hachage constitue un tirage aléatoire indépendant, et, par la loi des grands nombres, la fréquence à laquelle vous découvrez des blocs converge mathématiquement vers votre fraction du hashrate total du réseau. En revanche, à court et moyen terme, vos gains réels peuvent être extrêmement irréguliers. C’est ce décalage entre moyenne théorique et réalité aléatoire que l’on appelle **la variance** en mathématiques.

Voici un exemple très simple pour comprendre ce principe :
* Le réseau Bitcoin produit en moyenne 144 blocs par jour (environ un bloc toutes les 10 minutes) ;
* Si vous disposez de `0.0001 %` du hashrate total, votre espérance est de `144 × 0.000001`, soit `0.000144` bloc/jour ;
* Autrement dit, vous devriez trouver un bloc en moyenne tous les `1 / 0,000144` jours, c'est-à-dire tous les 6 944 jours, soit environ 19 ans.

Mais cette valeur correspond uniquement à une espérance mathématique : la distribution des temps de découverte suit une loi aléatoire, et il est donc parfaitement possible, en pratique, de ne jamais découvrir le moindre bloc, même sur une durée très longue. Vous pouvez être malchanceux et ne rien trouver pendant très longtemps, tout en payant des coûts récurrents (électricité, maintenance, amortissement du matériel...).

La pool de minage change la nature de ce problème : en mutualisant les hashrates, la pool trouve des blocs plus souvent. Chaque participant accepte alors de ne toucher qu’une fraction de chaque bloc trouvé, mais beaucoup plus fréquemment. C’est une transformation d’un revenu très volatil et très espacé en un revenu plus régulier, au prix d’un partage et de frais de service.

### Pourquoi la variance baisse quand on se regroupe ?

Plus votre puissance de calcul est élevée, plus votre fréquence attendue de blocs trouvés est élevée. Mais surtout, plus les événements deviennent fréquents, plus les résultats observés se rapprochent de la moyenne statistique sur une période donnée.

En solo, un petit mineur peut passer des années sans aucun bloc, puis toucher un gros gain un jour, puis plus rien. Dans une pool, la même réalité probabiliste existe, mais elle est lissée à l’échelle du collectif : la pool trouve des blocs plus souvent, et la redistribution transforme ces événements en paiements plus réguliers pour chaque participant. **La pool de minage vend donc de la prévisibilité sur l'activité de minage**.

### Repères historiques

Nous l'avons vu dans le chapitre précédent, au tout début, le minage pouvait se faire en solo avec un ordinateur classique, car la difficulté était très faible. Mais à mesure que le hashrate global a explosé (GPU, puis ASIC), le minage solo est devenu un pari très long pour la majorité des participants.

Les premières pools apparaissent précisément pour répondre à cette nouvelle réalité. Braiins Pool (anciennement Slush Pool / Bitcoin.cz) est la première pool de minage de Bitcoin : elle a miné son premier bloc le 16 décembre 2010. Le succès de cette première pool de minage est rapide, puisqu'en quelques jours seulement, elle obtient près de 3,5% du hashrate global.

![Image](assets/fr/047.webp)

Côté technique, les pools se sont ensuite structurées autour de protocoles de communication spécialisés entre la pool et les mineurs (par exemple Stratum, puis Stratum V2), afin d’orchestrer efficacement le travail distribué. Nous évoquerons plus précisément tous ces concepts dans la formation MIN 201.

### La situation moderne

À la date de rédaction de cette formation (début 2026), le hashrate global de Bitcoin se situe à un ordre de grandeur de l’ordre du zetta-hash par seconde (= 1 000 EH/s = 1 000 000 000 000 000 000 000 de hachages par seconde), et la quasi-totalité des blocs trouvés proviennent de pools de minage.

Voici un classement, à date, des principales pools de minage et de leur part respective du hashrate. Ce classement est susceptible d’évoluer au moment où vous lirez ce cours. Pour consulter des données actualisées, vous pouvez vous rendre sur le site de [mempool.space](https://mempool.space/graphs/mining/pools).

![Image](assets/fr/046.webp)

| Classement | Pool           | Blocs trouvés | Part du hashrate |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Source [mempool.space](https://mempool.space/graphs/mining/pools), données sur un mois, du 16 décembre 2025 au 16 janvier 2026.*

Dans un cours plus avancé, on ira plus loin sur le fonctionnement interne des pools (shares, protocoles réseaux, méthodes de paiement...), car c’est là que se jouent les détails qui déterminent à la fois la rentabilité pour le mineur, et les implications possibles sur Bitcoin.

---

Nous arrivons maintenant à la fin de ce cours MIN 101. Merci de l’avoir suivi jusqu’au bout. Si vous souhaitez évaluer les compétences acquises au fil de ce cours, un examen final vous attend dans la partie suivante.

Avec les connaissances de base que vous venez d’acquérir, vous pouvez désormais suivre des cours plus avancés sur le minage sur Plan ₿ Academy, qu’il s’agisse de formations théoriques, comme celle-ci, ou de cours plus pratiques, afin de commencer, vous aussi, à participer au minage sur Bitcoin !

# Partie finale
<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>

## Avis & Notes
<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>
<isCourseReview>true</isCourseReview>

## Examen final
<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusion
<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>
<isCourseConclusion>true</isCourseConclusion>