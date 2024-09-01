---
name: Les Inscriptions sur Bitcoin au travers d'Ordinals
goal: Comprendre le fonctionnement technique et effectif d'Ordinals
objectives:
  - Définir les notions théoriques d'Ordinals
  - Savoir comment les données sont inscrites sur Bitcoin 
  - Utiliser des outils pour explorer les inscriptions.
  - Comprendre les projets qui utilisent Ordinals
---


# 0/ Précautions
⚠️ ATTENTION
Nous n'avons pas de certitudes sur la continuité d'Ordinals. Il se peut que ce protocole devienne obsolète à long terme. 
Ceci reste une expérimentation en version beta (au 01/09/24) encore en alpha jusqu'au 25/96/24 et peut subir des modifications majeures. 

La version actuelle est : `ord 0.19.1`. 

Au vue de l'arrivée récente du protocole il n'y a pas encore de personne formée à ce sujet. J'ai découvert Ordinals en février 2023 et je ne suis qu'un explorateur de ce protocole.

Ce qui est partagé ici est une synthèse de mes connaissances et de mes expériences, et peut être amené à évoluer. Comme dans le cas de Bitcoin il est important de se tenir à jour des évolutions du/des protocole(s).

## 1. Préambule

J'ai adopté un discours et des explications qui ne suivent pas l'ordre utilisé en général comme dans [What is Ordinals and runes protocol?](https://youtu.be/g1jsHW-MX7A?si=5G3yOW0nVDIWR-38). 

J'ai pris le parti de mettre en avant l'enveloppe qui constitue selon moi le cœur de cette nouveauté et de passer les sats et l'*ordinal theory* ensuite. 
Les projets discutés et présentés ont pour but de sensibiliser et d'expliquer l'histoire en train de se faire. Bien d'autres projets sont en train de se faire et ce cours reste une introduction générale aux Ordinals. Des cours plus avancés seront disponibles et l'histoire pourra éventuellement être traitée dans des pages dédiées. 

# I/ Introduction

Ordinals a été proposé par Casey Rodarmor[^1].

<!--Transcript depuis [Casey Rodarmor - From Ordinals to Runes: Meet Bitcoin’s Most Controversial Dev](https://www.youtube.com/watch?v=sqfCarDdXPM) :-->

Casey a quitté l'école à 15 ans pour aller travailler dans des petits boulots. A 21 ans il découvre la programmation et veut en faire son métier. Il rattrape ses dernières années dans un [collège communautaire](https://fr.wikipedia.org/wiki/Coll%C3%A8ge_communautaire) avant d'intégrer Berkeley en Sciences de l'Informatique (Computer sciences). Il poursuit chez Google comme Ingénieur Fiabilité sur site ([Site Reliability Engineering](https://fr.wikipedia.org/wiki/Site_Reliability_Engineering)) puis rejoint l'équipe de [Chaincode Labs](https://chaincode.com/) en 2015. Chez Chaincode Labs il a maintenu Bitcoin core en réalisant des petites missions: nettoyage de certains PRs (Pull Requests), remaniement d'une partie des tests, et d'autres taches de maintenance. 

En 2019, il découvre [Art Blocks | Generative digital art](https://www.artblocks.io/), qui publie et promeut l'art géneratif. Fasciné par cet algorithmisation de l'art, il veut en faire. En se lancant dans *"les NFTs"* il voit les défaillances voir le non-sens informatique de devoir déployer un contrat pour écrire une URL renvoyant vers un lien IPFS (ou autres) stockant le JPEG. Il lui semble évident qu'il faut l'écrire *on-chain*. En tant que Bitcoin maximaliste[^2], il développe alors un outil qui permettrait de faire ceci : écrire **concrétement** l'image sur Bitcoin. 

C'est alors que né **Ordinals**. 

Pour plus de détails sur la vie de Casey (et son avis) vous pouvez consulter: 
[Casey Rodarmor's Resume](https://rodarmor.com/resume/index.html).
[Casey Rodarmor - From Ordinals to Runes: Meet Bitcoin’s Most Controversial Dev](https://www.youtube.com/watch?v=sqfCarDdXPM)
Vous pouvez écouter son podcast en anglais: [Hell Money](https://hell.money/) co-host par [Realizing Erin](https://www.youtube.com/realizingerin).  

Le protocole Oridnals a connu sa première inscription le 14 décembre 2022 [Inscription #0](https://ordiscan.com/inscription/0).

Ordinals est un protocole qui permet d'inscrire facilement des données sur Bitcoin et de les retrouver. 

Dans *L'élégance de Bitcoin* (Les contrats autonomes, l'inscription de données arbitraires et métaprotocoles pp.332-340), **Ludovic Lars** retrouve des trésors cachés dans Bitcoin comme l'hommage à Len Sassaman en art ASCII ![hommage_len](./assets/hommage_len.jpg) [source image](https://hellotoken.io/dordinals/) et bien d'autres[^3]. 

On voit ici que l'on sait inscrire des données sur Bitcoin depuis longtemps, mais qu'il nous est difficile de les retrouver. On dit alors que ces éléments ne sont pas indexés nativement[^4].
Ordinals est entre-autre une réponse à ceci en permettant de facilement retrouver tout ce qui est inscrit par cette méthode en utilisant un indexer[^5] permettant la créationd'[explorer](https://ordinals.com).

Ordinals est un protocole qui permet l'écriture de larges données sur Bitcoin et d'en tracer la possession. 
On parle d'**enveloppe**, d'**index** (ou d'indexer[^5]) et de **satoshis** (les unités de Bitcoin) pour tracer la propriété.

Nous allons donc voir comment cela fonctionne, comment on peut utiliser ce protocole et présenter quelques projets important de l'écosystem Ordinals.

Avant cela on peut se demander si Ordinals est unique.

## Ordinals est-il unique ?
Il existe d'autres protocoles à enveloppe sur Bitcoin (comme Atomicals) ou sur d'autres blockchain (comme Dogecoin).

### Atomicals

Ce protocole fut proposé fin 2023 sous forme de ligne de commande construite en javascript [atomicals-js](https://github.com/atomicals/atomicals-js). Comme pour Ordinals étant un protocole il doit être indexé. Pour ce faire ils ont proposés un indexer basé sur ElectrumX : [Electrumx Atomicals Indexer Server](https://github.com/atomicals/atomicals-electrumx).

Ce protocole utilise des messages plus compact qu'Ordinals avec une enveloppe plus élémentaire. De plus, au lieu d'écrire les données uniquement en hexadecimal sur Bitcoin il les transcrit d'abord en CBOR (Concise Binary Object Representation) puis en hexadécimal.
Atomicals a également la possibilité de faire des tokens, des nfts et des noms de domaine (appelés *realms*) nativement. 

<!--La différence majeure entre Atomicals et Ordinals est que Atomicals est un protocole de type *stateful* alors qu'Ordinals est un protocole de type *stateless*.-->

Une des attentes actuelles concernant Atomicals est l'Atomicals Virtual Machine (AVM) qui permettrait de faire des contrats autonomes sur Bitcoin.

A l'heure actuelle l'AVM n'est pas encore sortie.

Ce protocole est également très intéressant et permet de faire de nombreuses choses sur Bitcoin. Cela fera l'objet de cours futurs. 
Nous pouvons noter que la communauté Atomicals est bien moindre que la communauté Ordinals. Ce protocole peine à se faire connaître et à être utilisé.

Pour vous plonger dans ce protocole je vous invite à consulter [la documentation faites par la communauté](https://atomicals-community.github.io/atomicals-guide/).

### Doginals

Doginals est une copie du protocole Ordinals qui utilise exactement la même enveloppe mais sur la blockchain Dogecoin[^9]. 
On y retrouve alors l'univers Ordinals avec souvent quelques mois de retard. 
Un avantage d'avoir Ordinals sur Dogecoin (via Doginals) est le coût indéniablement moindre des inscriptions ainsi que la rapidité des transactions.
De plus, on y trouve une culture un peu différente de celle d'Ordinals, plus tourné autour de la culture Dogecoin elle-même. Les volumes sont dérisoires comparé à ceux d'Ordinals mais il y a tout de même un peu de trafic.
Doginals souffre néanmoins de mauvais indexers et d'outils encore peu développés aussi bien pour inscrire que pour interagir avec le protocole.

L'intégration annoncée des Doginals dans [mydoge wallet](https://www.mydoge.com/) peut être une étape vers une utilisation plus simple et plus répandue de ce protocole.  

Les principaux sites web autour de doginals pour l'achat et la vente d'inscriptions sont : [doggy.market](https://doggy.market) et [drc-20.org](https://drc-20.org/)[^6]. 

Les protocoles de type inscriptions sont encore balbutiants et peuvent être à la manière d'Atomicals assez différents d'Ordinals. Néanmoins, ce travail d'apprentissage sur Ordinals sera toujours bénéfique pour comprendre les évolutions futures. 

# II/ Le cœur d'Ordinals
**Ici nous regardons les détails de l'enveloppe et des tags du protocole.**

Dans une transaction Bitcoin on peut mettre un message. Ce message doit respecter une certaine structure et utiliser des "fonctions" du protocole Bitcoin.
Ces "fonctions" sont appelées des <u>opérations</u> et sont nommées `OP_CODE` (on utilise la notation `OP_OPERATION` par exemple `OP_ADD` pour l'opération d'addition). 
Ces opérations sont envoyées au *réseau Bitcoin*[^7] dans des transactions.

Via des `OP_CODEs` on peut réaliser des opérations algorithmique sur le réseau Bitcoin, on appelle cela un `script`. Pour plus de détail : [Opcodes used in Bitcoin Script - Bitcoin Wiki](https://wiki.bitcoinsv.io/index.php/Opcodes_used_in_Bitcoin_Script)

Ordinals peut alors être vu comme une proposition de standardisation de script Bitcoin pour permettre l'écriture de larges données sur Bitcoin et en tracer la possession. On voit ici apparaître le lien fort entre le script Bitcoin et les protocoles de type inscription sur Bitcoin. 
Les protocoles seront appelés de type Inscription lorsqu'ils utilisent la forme de script suivant :
```
OP_FALSE
OP_IF
    OP_PUSHDATA <ID_DU_PROTOCOLE>
    OP_PUSHDATA <REGLE_APPLIQUEE>
    ...
    OP_PUSHDATA <DONNEES>
OP_ENDIF
```
Evidemment, la forme exacte varie d'un protocole à l'autre, mais les protocoles à inscription sont tous, actuellement, basés sur cette structure.
On appelle alors ce script une **enveloppe**, servant à envelopper les données sur Bitcoin.

Comme ce cours concerne Ordinals nous nous bornerons à l'enveloppe Ordinals mais vous pourrez aisément trouver l'enveloppe d'Atomicals dans la documentation fournie par la communauté Atomicals.

## 1. L'enveloppe

Basiquement on pousse les informations suivantes via l'enveloppe : 
```
"ord"

"Type" (MIME format) 

"Données"
```

Autrement dit on envoie le script suivant sur Bitcoin : 
```
OP_FALSE
OP_IF
    OP_PUSHDATA "ord"
    OP_PUSH 1
    OP_PUSHDATA <TYPE MIME>
    OP_PUSH 0
    OP_PUSHDATA <DONNEES>
OP_ENDIF
```
Les opérations `OP_PUSH 1` et `OP_PUSH 0` sont des opérations qui permettent de séparer les champs de l'enveloppe. On appelle cela les **tags** et nous détailleront cela par la suite. 

La question qui peut se poser est : qu'est-ce que le format [MIME](https://developer.mozilla.org/fr/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) ?

Le format MIME est un standard d'Internet initialement prévu pour détailler le type de fichier envoyé dans un courrier électronique. Il permet d'indiquer le type de contenu d'un message[^10].

La plupart des extensions de fichier (`.jpg`, `.pdf`, `.mp3`, ...) ont un type MIME associé (voir: [RFC 2046](https://datatracker.ietf.org/doc/html/rfc2046)). 
Pour Ordinals en fonction du fichier que l'on souhaite inscrire le type MIME est sélectionné puis écrit en conséquence. 

Cela a deux fonctions :
- Permettre de retrouver les données inscrites en fonction de leur type.
- Afficher correctement les données contenues dans l'enveloppe. Cela vaut surtout pour les explorers qui pourront afficher le contenu convenablement. 

Pouvant mettre n'importe quel format MIME, on peut aisément stocker du HTML, du CSS, du javascript ou encore de l'audio ou de la vidéo sur Bitcoin.

Quelques exemples sont disponibles dans l'article [{In-On}-Chain](https://6120.eu/posts/in-on-chain/).
Un exemple plutôt sympa est l'inscription 466 : [Yet Another Doom Clone](https://ordinals.com/content/521f8eccffa4c41a3a7728dd012ea5a4a02feed81f41159231251ecf1e5c79dai0). Publiée assez rapidement et codée entièrement en HTML, cette inscription fait que DOOM sera toujours disponible, on aura simplement à récupérer les données sur Bitcoin pour y jouer. Vous pouvez consulter le code source via [Inscription #466 | Ordiscan](https://ordiscan.com/inscription/466) en cliquant sur **view source code** en haut de la fenêtre d'affichage. 

Vous pouvez avoir un détail du nombre d'inscriptions par type MIME sur [ordinals.com/status](https://ordinals.com/status).

### Activité
Trouver des inscriptions de type MIME `text/html;charset=utf-8`, `image/jpeg`, `image/webp`, `video/mp4`, `image/gif` et `text/javascript`.

Pour cela trouver un explorer Ordinals qui vous permet de filtrer les inscriptions pour obtenir ces types MIME.
<!--Explorer possible : ord.io-->

### Activité avancée
Créer le script de création d'une transaction depuis `createrawtransaction` avec une librairie ou langage quelconque. (Sympa en bitcoin-cli, mais pas de copier-coller du Rust de [./src/subcommand/wallet/inscribe.rs](https://github.com/ordinals/ord))

### Détails sur les inscriptions brc-20
Comme on l'a vu pour faire une inscription simple on a juste besoin de spécifier le type de notre fichier et de l'envoyer sur Bitcoin.

En mars 2023 [domodata](https://domo-2.gitbook.io/brc-20-experiment) a proposé un standard permettant de créer et échanger des tokens sur Bitcoin via l'enveloppe Ordinals. On appelle ce standard **brc-20** et nous allons voir quel est-il et comment fonctionne-t-il. 

Le nom du standard est une référence au standard ERC-20 d'Ethereum. Le but de ce standard est d'être facile et de fonctionner. Il s'agit en effet de la première expérimentation dans cette direction. Loin d'être parfait et optimisé il a le mérite de fonctionner. 

**Mais, comment ?**
 
Pour créer un token brc-20 il suffit de créer une inscription avec le type MIME `application/json` et de respecter la structure suivante pour le fichier inscrit : 
```json
{
    "p": "brc-20",
    "op": "deploy",
    "tick": "TICK",
    "supply": "xx",
    "lim": 1000000
}
```
- `p` est le protocole utilisé, ici brc-20.
- `op` est l'opération à réaliser, ici deploy pour déployer un token.
- `tick` est le ticker du token, il doit faire 4 caractères pour être indexé.
- `supply` est la quantité totale de token possible.
- `lim` est le nombre maximum de token pouvant être minté par opération *mint*.

On voit ici qu'on est une fois de plus face à un protocole. Ce protocole possède 3 opérations : *deploy* (détaillé ci-dessus), *mint* (pour créer des tokens) et *transfer* (pour échanger des tokens).
Chaque opération prend des paramètres particuliers et doit respecter la structure attendue pour être indexée.

Comme pour Ordinals il faut un indexer, qui à l'instar d'Ordinals fait un peu plus que simplement permettre de retrouver les tokens. 
L'indexer brc-20, permet non seulement de tenir à jour les tokens existants mais tiens également une balance pour chaque wallet ayant minté ou transféré des tokens. On dit que le protocole est *stateful*, il prend en compte l'état du système[^15]. 

Le *mint* est assez simple, il suffit d'inscrire le fichier suivant : 
```json
{
    "p": "brc-20",
    "op": "mint",
    "tick": "TICK",
    "amt": "xx"
}
```
Si le montant (amount : `amt`) est supérieur à la limite (`lim`) définie dans l'inscription de `deploy` alors l'opération est refusée et les tokens ne sont pas ajoutés à l'adresse ayant effectué l'opération. Si le montant est inférieur ou égal à la limite alors l'adresse est créditée d'autant de token. 

Le *transfer* est un peu plus complexe, il faut inscrire le fichier suivant puis transférer ce fichier fraîchement inscrit à l'adresse de destination.

```json
{
    "p": "brc-20",
    "op": "transfer",
    "tick": "TICK",
    "amt": "xx"
}
```

On voit donc qu'avec des fichiers JSON simples on peut créer des tokens en utilisant l'enveloppe Ordinals moyennant un indexer du protocole brc-20.

D'autres expérimentations plus poussées sont en cours du côté de [Trac ecosystem](https://trac.network/).
**Trac** se définit comme un ecosystème avec plusieurs protocoles permettant de créer des tokens, réalisés des swaps, du staking ou encore des tokens d'authentification. Le développement est en cours et si vous voulez en savoir plus en français je vous invite à écouter l'[OP_SPACE 006: Tap Protocol -> TOUT !](https://x.com/i/spaces/1lPJqbbnzwmxb). 
Une autre expérimentation était : [`cbrc-20`](https://www.ord.io/preview/130c79034450163f36fcde8e27f96904dc42e535f28aacd5af3b9a18d0b1c7f9i0?type=text/html&raw=true) pour un standard de token plus avancé que brc-20 et plus natif à Ordinals dans sa définition. On verra par la suite quel est l'outil principal d'Ordinals utilisé par cbrc-20. 

## 2. Les *tags*
Les *tags* ou étiquettes en français permettent une spécification des messages protocolaires. Cela permet d'ajouter du contexte à l'inscription brute vue en partie 1.

Ci-dessous un détail des *tags* possibles :
```
content_type, avec le tag 1, sa valeur est le type MIME du corps.
pointer, avec le tag 2, [pointer docs](https://docs.ordinals.com/inscriptions/pointer.html).
parent, avec le tag 3, [provenance](https://docs.ordinals.com/inscriptions/provenance.html).
metadata, avec le tag 5, [metadata](https://docs.ordinals.com/inscriptions/metadata.html).
metaprotocol, avec le tag 7, dont la valeur est l'identifiant du metaprotocol.
content_encoding, avec le tag 9, dont la valeur est l'encodage utilisé pour le corps.
delegate, avec le tag 11, [delegate](https://docs.ordinals.com/inscriptions/delegate.html).
```
Le tag 1 a été longuement détaillé dans la partie précédente. 

Les autres tags permettent de donner des informations supplémentaires sur l'inscription. Regardons quelques tags importants dans l'écosystème actuel. 

- Le tag 2 est utilisé pour donner un pointeur vers une autre inscription. Cela permet de lier des inscriptions entre elles. Plus précisément, si vous voulez que votre inscription envoie l'image d'une autre inscription par exemple celle-ci: [SKULL 1187713](https://ordinals.com/inscription/24bb1fb29bc075ac00c33638a893b9cbf583d6a8b286c70eef290697b212de50i0), il vous faudra mettre ce tag suivi de l'identifiant de cette inscription. 
- Le tag 3 est utilisé pour créer ce que l'on appelle des *parent/enfant*. Cela permet de tracer la provenance d'une inscription et de créer des "arbres d'inscriptions". En effet, dans le cadre d'une collection d'art par exemple il peut être intéressant d'inscrire l'image représentative de la collection puis d'inscrire chaque oeuvre de la collection en tant qu'enfant de l'inscription de la collection. Ex : [Manifesto parent](https://ordinals.com/inscription/2914e780bb7272612b97517af3dfe8fc604b6f8661645eedad226eef181df06bi0), les enfants sont appelés *children* dans l'interface d'[ordinals.com](https://ordinals.com).
- Le tag 5 est utilisé pour donner des informations supplémentaires sur l'inscription. Cela peut être des informations sur l'auteur, la date de création, le lieu de création, etc.
- Le tag 7 est utilisé pour donner l'identifiant du metaprotocol. Cela permet de spécifier quel protocole est utilisé pour l'inscription. Dans l'exemple donné pour le tag 3 le metaprotocol est `OP_SPACE`. 
- Le tag 9 est utilisé pour donner l'encodage du corps. Cela permet de savoir comment lire les données inscrites.
- Le tag 11 est utilisé pour donner un délégué. Cela permet de donner des droits à une autre adresse sur l'inscription.

### Activité possible
Chercher "à la main" des inscriptions exemples pour chacun des tags.
Attention : cet exercice peut être très difficile compte tenu de la mauvaise gestion des explorers actuels des filtres par *tags*. Un fork de [ord](https://github.com/ordinals/ord) a été proposé pour permettre de filtrer par tag metaprotocol : [xord](https://github.com/cyb-ord/xord) mais repose sur une ancienne version d'`ord`.

### Activité avancée

Proposer un script permettant de filtrer les inscriptions par leur tag. 
Cela pourra être publier et donner lieu à du soutient par la communauté Ordinals. 

On voit ici que les tags apportent de nouveaux cas d'usage d'Ordinals. Un exemple de l'utilisation avancée des tags est le protocole [cbrc-20](https://ordinals.com/preview/130c79034450163f36fcde8e27f96904dc42e535f28aacd5af3b9a18d0b1c7f9i0) aujourd'hui en cours d'abandon. Ce protocole utilisait le champ metaprotocol et metadata pour créer, minter et transférer des tokens. 

De nombreux uses-cases sont encore à explorer avec tout ceci.

### Activité
Trouver un ou deux projets utilisant certains tags avancées et expliquer comment ils les utilisent.

<!--Un exemple de très grosse transaction : [Creation des Quantum Cats](https://mempool.space/tx/4b31771df21656d2a77e6fa18720a6dd94b04510b9065a7c67250d5c89ad2079).-->
<!--Cette inscription contient par exemple un module javascript recursif : [cat0001](https://ordiscan.com/inscription/53785861).-->
<!--La collection Blob : [ex : blob01](https://ordiscan.com/inscription/67285792)-->
<!--La collection Bitcoin Puppet : [ex : puppet #6060](https://ordinals.com/inscription/e4520773d3d7a182ed4bd8875626419db5db3ec73fcacd4cc48ad060afb02a30i0).-->

Par exemple, [`cbrc-20`](https://www.ord.io/preview/130c79034450163f36fcde8e27f96904dc42e535f28aacd5af3b9a18d0b1c7f9i0?type=text/html&raw=true) avait proposé un standard de token utilisant le tag `metaprotocol` ainsi qu'une syntaxe avancée (vrn) permettant des utilisations plus poussées que brc-20 comme le transfer en un message (xmail), le swap ou encore le staking.  


### Récursivité

Pour aller plus loin on peut également parler de récursivité. Comme on l'a vu précédemment on peut inscrire des fichiers javascript ou html. 
Un tel fichier peut alors accéder à la mémoire interne de son lieu de stockage. Mais... Où est-il stocké ? 
Sur Bitcoin ! Il a donc accès à des éléments propre à Bitcoin. Cela se fait via l'accès à ce que l'on appelle des *endpoints* décrit dans la [documentation officielle](https://docs.ordinals.com/inscriptions/recursion.html). 

Les chemins sont de la forme : `/r/<OPTION>/<ID>` où `OPTION` est le nom d'une catégorie à laquelle on souhaite accéder et `ID` est l'identifiant de l'inscription. Une description complète est donnée dans le lien ci-dessus. 

Cela nous permet d'écrire du code qui utilise d'autres inscriptions. Par exemple, le code exact de React@18.2.0 est [on-chain](https://ordinals.com/content/7f403153b6484f7d24f50a51e1cdf8187219a3baf103ef0df5ea2437fb9de874i0). 
Ainsi, on peut créer un site web React utilisant cette librairie entièrement on-chain : [Psyop website](https://ordiscan.com/inscription/25949479).

La récursivité est aujourd'hui très utilisée dans Ordinals. 

Ici vous trouverez une liste assez complète de packages js déployé sur ordinals : [jokie88/ordinalpublicgoods: A list of resources inscribed on bitcoin](https://github.com/jokie88/ordinalpublicgoods?tab=readme-ov-file#ordinal-public-goods).

### Activité 

Trouver une collection importante utilisant la recursivité. 

<!--Ex : [RSIC METAPROTOCOL](https://www.ord.io/56718386)-->

## 3. L'interprétation des satoshis et l'`index` pour la propriété ?

Le protocole Ordinals a été proposé par Casey avec une théorie de la propriété. Cette théorie appelée Théorie des Ordinals (*Ordinal Theory*) définie une numérotation de chaque satoshi (sat) produit par le réseau Bitcoin.

Une fois la numérotation effectuée (qui continue à mesure que de nouveaux blocs sont minés) il a déclaré que l'inscription se faisait sur un sat: le premier de l'UTXO.
Ainsi, on peut tracer la propriété d'une inscription par la propriété du sat qui la contient.

> Cela se fait par l'information de la localisation *location* donnée par l'indexer à propos du sat.  

L'accès à ces informations peuvent se faire de plusieurs manières en fonction des usages et des besoins. 
De l'interface web [ordinals.com](https://ordinals.com) à la manipulation directe via le fichier `index.redb`.

De plus, une fois la numérotation effectuée, il y a des sats qui sont considérés comme rares. Par exemple, le premier sat miné par Satoshi est légendaire, le premier sat miné lors de chaque halving est rare ou encore le premier sat de chaque bloc est considéré comme *uncommon* (pas commun). 
Ces sats tout comme la numismatic (étude des pièces de monnaie) sont des éléments de collection et peuvent être échangés. De nouveaux niveaux de raretés sont créés par les utilisateurs d'Ordinals. Par exemple, les sats ayant servi à payer la Pizza (du Bitcoin pizza day) sont identifiés comme les *pizza sats*.

### Activité 
En prenant connaissance des [points d'accès](https://docs.ordinals.com/guides/explorer.html) donné dans la documentation et des explorers trouvés précédemment donner des sats rares et/ou vérifier la rareté de certains sats. 
![API Endpoints](./assets/endpoints_ordinals.png)

Trouver une collection ayant été entièrement inscrite sur des sats particuliers. 
<!--Pizza Ninja-->

Un bon thread au sujet de la rareté réalisé par [@Besbtc](https://x.com/Besbtc) : [Sat rarity](https://x.com/Besbtc/status/1739987968922632240). 
<!--Proposer à Besbtc de faire un tuto sats rares.-->

#### Pour aller plus loin

La ligne de commande `ord` permet également d'étudier les sats. Pour cela il faut avoir l'index qui est convenanblement configuré. 
> Donner la configuration pour chasser les sats.

> Discuter du format redb. 

<!--Proposer à Crypto9ine de faire un tuto sur la chasse aux sats en cli.-->

# III/ L'utilisation & les projets

On a passé du temps pour bien comprendre ce qu'il se passe on-chain et quelles sont les idées derrière Ordinals. Maintenant on va voir comment on peut utiliser tout cela et quels sont les projets qui ont construit sur Ordinals.

## 1. Les outils

Pour utiliser Ordinals il faut des outils. 
Si vous êtes un développeur ou familier des lignes de commandes vous pouvez utiliser directement la ligne de commande [`ord`](https://github.com/ordinals/ord) pour inscrire et indexer Ordinals. Pour cela il vous faudra ~1To de disponible pour avoir un full node Bitcoin avec l'option `txindex=1` activée.
Pour l'installation de `ord` vous pouvez suivre la très bonne vidéo [@pazNGMI: How To Setup A Bitcoin Node & Ord Wallet](https://www.youtube.com/watch?v=tdC8kmjn5N0). Pour la partie node Bitcoin je vous invite à consulter directement PlanB Network [Tutoriels nodes](https://planb.network/fr/tutorials/node).

Pour un usage plus user friendly voici quelques outils que j'utilise ou dont j'ai entendu parler[^8]:

- Explorers : [ordinals.com](https://ordinals.com), [ordiscan.com](https://ordiscan.com), [ordpool.space](https://ordpool.space), [ord.io](https://ord.io), ...

- Quelques wallets : [Unisat](https://unisat.io), [Xverse](https://xverse.app), [Magic Eden](https://wallet.magiceden.io/), ...

- Outils d'inscriptions : [Unisat](https://unisat.io), [ordinals bot](https://ordinalsbot.com), [looksordinals.com](https://looksordinals.com), [Chisel](https://chisel.xyz) [Cool pour faire des inscriptions parent/enfants], ...

## 2. Les Projets

La propriété issues d'ordinals est définit consensuellement comme étant le premier à écrire un fichier (vu comme "message" au sein du protocole). 
Idée importante dans la définition de sous-protocoles pour créer le consensus. Autrement dit, si vous êtes le premier à inscrire une image ou un message (comme nous le verrons ci-dessous) vous en êtes le propriétaire ; les suivants ne le seront pas (bien que posssédant une version de l'image ou du message). 

Comme discuté précédemment brc-20, cbrc-20,… applique le principe du : premier arrivé premier servi. On reverra cela avec Bitmap.

<!--Faire une ref à la ss-section Bitmap-->

Mais cela vient aussi de quelque chose de marrant et communautaire. On retrouve assez vite : [Un guide pour coder tetris | Sur page noire](https://ordiscan.com/inscription/145), [Zork Game](https://ordiscan.com/inscription/146)->[wiki](https://fr.wikipedia.org/wiki/Zork), [Un tweet de Luke DashJr qui veut arrêter Ordinals](https://ordiscan.com/inscrption/128) ou encore [le caractère Bitcoin en utf-8](https://ordiscan.com/inscription/110).

### a. Premières collections

L'histoire !
![inscription0](https://ordinals.com/content/6fb976ab49dcec017f1e201e84395983204ae1a7c2abf7ced0a85d692e442799i0)

*Si vous souhaitez visualiser les premières inscriptions réalisées je vous invite à consulter [Inscriptions | Ordiscan](https://ordiscan.com/inscriptions?types=image&sort=oldest).*

La première collection revendiquée sur Ordinals sont les [**Bitcoin Schrooms** | @BitcoinShrooms](https://x.com/BitcoinShrooms) *224 inscriptions*:
![Shroom 0](https://ordinals.com/content/9163af650dcdeeeb9a7e1f47f693b51921dce3bdf2475e69360ec83d9956f5d7i0)
`inscription_id:9163af650dcdeeeb9a7e1f47f693b51921dce3bdf2475e69360ec83d9956f5d7i0`

Le compte de la communauté est celui-ci : [@bitcoinshroom](https://x.com/bitcoinshroom). 

On voit bien ici une collection d'art génératif (créé algorithmiquement) reprenant les codes d'internet, des memes et de Bitcoin. Vous pouvez vous balader sur [bitcoinshrooms/com](https://bitcoinshrooms.com) pour y voir des références à l'Orange Pill, Bitcoin Magazine, à l'euro et l'union européenne, BTCServer ou encore à d'autres collections (certainement le plus ironique). 
La collection ne s'est pas inscrite en une seule fois et permet de mettre en lumière la jeunesse de l'écosystème Ordinals. En effet, la collection est mal indexée sur certains sites comme [gamma.io](https://gamma.io/ordinals/collections/bitcoinshrooms) ou [ordiscan](https://ordiscan.com/collection/bitcoin-shrooms?sort=oldest) qui n'ont pas les mêmes.
Par exemple, le fichier de définition de la collection ne contient pas le shroom ci-dessus [inscriptions.json](https://github.com/ordinals-wallet/ordinals-collections/blob/main/collections/bitcoin-shrooms/inscriptions.json), pourtant bien dans la collection d'après [le site officiel](https://bitcoinshrooms.com).
Les inscriptions de cette collection se sont échangés pour plusieurs BTC chacunes et s'échange pour les moins chers autour de 1,9 BTC actuellement (Août 24)[^11]. 

Cela nous montre et rappelle que l'écosystème est encore imature et il ne faut pas y aller aveuglément. 


La collection suivante qui est la première collection inscrite en une seule fois et indexée entièrement on-chain sont les [**Bitcoin Rocks** | @ordrocks](https://x.com/ordrocks), *100 inscriptions*: 
![Rock 0](https://ordinals.com/content/e8ce0fcb238b377b3a6b9921333e26fbec5c5724c5bf6e783c3dcc1129794508i0)
`inscription_id:e8ce0fcb238b377b3a6b9921333e26fbec5c5724c5bf6e783c3dcc1129794508i0`

La liste exhaustive de toutes les Bitcoin rocks sont listées sur l'[inscription #191](https://ordiscan.com/inscription/191). 
Certains mystères demeurent comme : comment ont-ils réalisés ces inscriptions ? Mon hypothèse est qu'ils l'ont réalisés avec l'aide d'un mineur pour n'avoir que ces transactions ordinals-ci dans le bloc. Est-ce un premier test pour le premier bloc le plus lourd de l'histoire Bitcoin via des inscriptions ?  
Bien que peu liquide le floor sur [Magic Eden](https://magiceden.io/ordinals/marketplace/bitcoinrocks) est à 4 BTC.


Finalement on pourra citer [**Bitcoin Wizard** | @bitcoinwizardry](https://x.com/bitcoinwizardry) (Sorcier Bitcoin)*1 300 inscriptions*:
![r/bitcoin](https://ordinals.com/content/b1c5baa2593b256068635bbc475e0cc439d66c2dcf12e9de6f3aaeaf96ff818bi0)
`inscription_id:b1c5baa2593b256068635bbc475e0cc439d66c2dcf12e9de6f3aaeaf96ff818bi0`

Une collection qui provient tout droit de [Reddit r/BitcoinWizard](https://www.reddit.com/r/BitcoinWizard/) dessiné par [u/mavensbot](https://reddit.com/u/mavensbot). 
> "En février 2013, une campagne de marketing pour Bitcoin a été lancée sur Reddit, mettant en vedette le désormais emblématique Sorcier Bitcoin [Bitcoin Wizard]. Depuis, cette mascotte adorée est devenue synonyme de Bitcoin et est reconnue comme le symbole le plus connu de la cryptomonnaie."
Cela a donné : "Magic internet money" ; comme Bitcoin était considéré à ce moment là. Le meme (message) qui en ressort en fait une collection assez emblématique et elle a été l'un des premiers mints public.

Nous parlerons des **Taproot Wizards** qui se sont basés sur ce meme pour construire leur empire. On pourra également noter les [**Bitcoin Punks**](https://bitcoinpunks.com/) *10k inscriptions*, inscrits assez rapidement, faisant référence aux *cryptopunks*.
![punk inscription#420](https://ordinals.com/content/5a55780e69b923d418ac6212151540c4c4462088e3e6d52522a466d36c006cdai0) 
`inscription_id:5a55780e69b923d418ac6212151540c4c4462088e3e6d52522a466d36c006cdai0`

### b. Bitmap

Dans cette idée de propriété on a : 
[Bitmap](https://bitmap.community/) -> consensus produisant une propriété sur les blocs Bitcoin. Crée l’idée d’un metaverse Bitcoin dont les biens de propriétés sont les blocs. 
Le premier à inscrire : NumeroDeBloc.bitmap possède alors le bloc NumeroDeBloc au regard du protocole Bitmap.

Fondé *possiblement* par [TheBlockRunner](https://www.youtube.com/@TheBlockRunner), ils ont une assez grosse communautés de gens qui aiment et soutiennent le projet.
On y trouve un détail sur la rareté des blocs: [Blocktributes](https://8bit-1.gitbook.io/blocktributes), faites par la communauté ainsi qu'un détail des blocs [trait-definitions](https://docs.bitmap.community/bitmap.community/trait-definitions). 
Cela est intéressant car il met en avant une étude minutieuse du bloc avant son achat ou de sa vente. En effet, la rareté et les attributs que vous allez obtenir sur le bloc dépendent des caractéristiques de ce bloc: ses fees, sa récompense, son nombres de transactions,... ; ainsi que des caractéristique de rareté posés par la communauté comme les blocs minés via le [Patoshi](https://bitcoin.fr/satoshi-etait-il-un-mineur-cupide/), les blocs contenant moins 100 transactions, moins de 1000 ou encore moins de 100k transactions ont un trait spécial, certain blocs ayant fait l'objet d'une mise-à-jour majeure par exemple valent plus chers. Cela est intéressant car il oblige ses holders et ses investisseurs à apprendre et relever cela ; de même que les développeurs sur Bitmap. 

Actuellement, tout cela reste uniquement pour l'échange et possiblement la spéculation mais le projet a apparemment de grandes ambitions de métaverse et avait proposé un premier jeu un peu comme [Minecraft](https://www.minecraft.net/fr-fr) où l'on extrayait des ressources issues des transactions contenues dans le bloc. 

Pour plus d'information sur ce projet vous pouvez suivre leur X (anc. Twitter). 

### c. Taproot Wizard

Un projet important à mentionner est : 
[**Taproot Wizard** 🧙 |  Manifesto](https://taprootwizards.com/manifesto) *2 108 inscriptions*[^12].
![taproot wizard](https://ordinals.com/content/0301e0480b374b32851a9462db29dc19fe830a7f7d7a88b81612b9d42099c0aei0)

Projet arrivé tôt dans Ordinals porté par : [Udi Weirthemeier | @udiWertheimer](https://x.com/udiwertheimer), [Eric Wall | @ercwl](https://x.com/ercwl) et dessiné par [0xFar | @0xfar](https://x.om/0xfar). Vous reconnaitrez certainement *l'inspiration* de Bitcoin Wizards. 

Tout d'abord, ce fut la première collection à inscrire un bloc Bitcoin le plus lourd de l'histoire [Block 774628](https://mempool.space/block/0000000000000000000515e202c8ae73c8155fc472422d7593af87aa74f2cf3d?showDetails=true) (aujourd'hui dépassé par [**Runestone**](https://www.ord.io/collection/runestone)[^13]). 
Pour ce faire ils ont réalisés un partenariat avec la pool [Luxor Technology | @luxor](https://x.com/luxor). Cela rappelle que les mineurs choisissent les transactions qu'ils mettent dans le bloc, et des partenariats sont possibles pour faciliter le passage de certaines transactions[^14].
Cette inscription a fait du bruit et lancé la machine Taproot Wizards. Ces inscriptions n'ont pas étés vendues sur le marché secondaire ni données à tout le monde gratuitement. Il fallait tweeter la *txid* (hash de la transaction) de l'image ci-dessus pour avoir une chance d'en obtenir au début. On ne connait pas la répartition exacte qui a été faites, mais certaines personnes auraient leur Taproot Wizards comme [Jameson Lopp | @lopp](https://x.com/lopp), [@root13maxi](https://x.com/root13maxi) ou [@hash_bender](https://x.com/hash_bender) dont je ne connais pas personnellement leur wallet pour l'assurer. 

Cela était la première étape, s'en est suivi la publication de leur manifesto où ils promeuvent un Wizard Village, puis une école de Sorcier. Leur volonté est clairement la constitution d'une communauté très forte de plusieurs manières. Par la qualité de ses membres dont certains sont des OGs Bitcoin ou Ordinals, par la niveau de connaissance on retrouve un public écaliré sur la technologie Ordinals ainsi que par l'engagement de ses membres au travers des nombreuses missions demandées. 
En effet, si vous n'avez pas eu de Taproot Wizards au lancement alors il va falloir donner Beaucoup ! Ils offrent à quelques rares personnes des Whitelist, ce qu'il signifie que ça donne la possibilité de payer afin d'en obtenir un. 
Je n'ai aucune information sur les prix pratiqués ni sur comment les possesseurs de ces oeuvres peuvent gagner ou récupérer de l'argent. C'est certainement un des clubs privés les plus importants dans Ordinals. 

Néanmoins, ce n'est pas uniquement un club. Avec cette *école* et cette culture, de plus en plus de gens veulent en faire partie. Et ça tombe bien ils ont besoin d'engagement ! 

**Pourquoi faire ?**
Evidemment, nous ne sommes pas eux et je n'ai aucun lien avec les fondateurs. Mais nous pouvons essayer des corrélations. 
Cela n'est que mon interprétation et j'essaye de relater les faits de manière la plus objective possible. 

Un terme a été réintroduit récemment dans le monde de Bitcoin : les [*covenants*](https://fr.wikipedia.org/wiki/Covenant). Mot anglais emprunté au français, il désigne la conventions. Principalements utilisé au pluriel dans le cadre de Bitcoin. 
Une idée générale des covenants est d'appliquer des règles (on-chain/protocolaires) sur des adresses Bitcoin. 
> "Les covenants sont une catégorie de modifications proposées aux règles de consensus de Bitcoin qui permettraient à un script d'empêcher un utilisateur autorisé de transférer des fonds vers certains autres scripts." [Covenants | Bitcoin Optech](https://bitcoinops.org/en/topics/covenants/)

Par exemple, contraindre une adresse à ne pouvoir retirer des fonds que vers une autre adresse spécifique, ou encore borner le montant possible. Pour plus de détail pratique veuillez consulter:  [#covenants | Grand angle crypto](https://www.youtube.com/watch?v=JCtnsXCUrzs) où des cas sont explicités. 
Ce terme est employé sur Bitcoin Talk dès 2013 : [CoinCovenants using SCIP signatures, an amusingly bad idea.](https://bitcointalk.org/index.php?topic=278122.0) pour le critiquer (bienvenu sur Bitcoin...). Il sera employé dans un article scientifique dès 2016 dans :  [Bitcoin Covenants | SpringerLink](https://link.springer.com/chapter/10.1007/978-3-662-53357-4_9). Peu d'échanges à ce sujet hormis le premier thread de critique jusqu'à 2021 où on en trouve une première allusion restée sans réponse : [OP_MERKLE | Bitcoin Talk ](https://bitcointalk.org/index.php?topic=5377956.0).
 
Comme évoqué dans l'article Bitcoin Covenants, et mis en lumière dans les deux références suivantes, il y a plusieurs manières de faire des covenants. Principalement, en ajoutant de nouveaux `OP_CODE` (`OP_CHECKTEMPLATEVERIFY`, `OP_CHECKSIGFROMSTACK`, `OP_VAULT`,...).  
Celui qui va nous intéresser est `OP_CAT`, discuté dans [Bitcoin OPTECH #200](https://bitcoinops.org/en/newsletters/2022/05/18/#when-would-enabling-op-cat-allow-recursive-covenants) en 2022 suite aux échanges sur Bitcoin-dev digest avec [ZmnSCPxj (ZmnSCPxj, ZmnSCPxj jxPCSmnZ)](https://github.com/ZmnSCPxj).

L'opération `OP_CAT` est farouchement défendue par Udi Wertheimer. Au moins d'octobre 2023 ils lancèrent les Quantum Cats, qui ont fait grand bruit dans la communauté et dont le premier s'est vendu sur [Sothebyse]() pour x BTC. Ils ont alors lancés les quêtes `OP_CAT`. 
**Le but ?**
Faire promouvoir par la communauté ce qu'est `OP_CAT` et que peut-il apporter de *magique* à Bitcoin. Dessins, Threads, déguisement, missions exentriques, ... pour : peut-être avoir la chance d'obtenir une whitelist Taproot Wizards et/ou un Quantum Cat. 

Les Quantum Cats se vendent sur le marché secondaire pour 0.25 BTC (Août 24) et sont également un ticket d'entrée pour le club des Wizards. 

On voit donc que cette école de Sorciers doublée d'un club très privé est là pour servir des intérêts dont certains peuvent être de faire évoluer Bitcoin et son code. 

Cela permet néanmoins de sensibiliser de nombreuses personnes au code Bitcoin et de s'en saisir. L'image et les relations d'Udi en font un personnage sulfureux mais qui peut nouer des liens avec des gens très influent dans l'univers de Bitcoin. 

[Covenants, OP_CAT et OP_CTV : Tout savoir sur la prochaine mise à jour de Bitcoin](https://cryptoast.fr/covenants-opcat-opctv-tout-savoir-prochaine-mise-a-jour-bitcoin/)

[^1]: ([Casey (@rodarmor) | Twitter](https://twitter.com/rodarmor/), [R O D A R M O R](https://rodarmor.com/), [casey (Casey Rodarmor) | Github](https://github.com/casey/))

[^2]: Bitcoin maximaliste se dit des personnes mettant en avant le fait que Seul Bitcoin a une véritable valeur monétaire. Les autres cryptos sont en général désignées par *Shitcoin* de la part des maximalistes. Il existe plusieurs courant du maximalisme allant du minimalisme au toxic maximalisme. Les détails dépassent largement le cadre de cet introduction à Ordinals.  

[^3]: Pour un peu d'histoire cypherpunk : [Len Sassaman and Satoshi: a Cypherpunk history | Medium](https://evanhatch.medium.com/len-sassaman-and-satoshi-e483c85c2b10).

[^4]: En effet, il est possible de retrouver ces données sur Internet par exemple mais très difficile on-chain (depuis Bitcoin).

[^5]: En français on prononce indexeUr et non indexé, comme explorer (exploreUr et non exploré).

[^6]: Standard basé sur brc-20 pour Doginals. Nous détaillerons plus tard ce qu'est le standard brc-20.

[^7]: On appelle <u>réseau Bitcoin</u>, l'ensemble des machines exécutant le protocole Bitcoin. On trouvera un détail des clients utilisés pour accéder au réseau Bitcoin sur [Coin Dance | Bitcoin Nodes Summary](https://coin.dance/nodes/share).

[^8]: Attention, ces outils peuvent être obsolètes ou ne pas être sécurisés. Il est important de bien se renseigner avant d'utiliser un outil et de ne pas mettre tout son argent dans un seul outil !

[^9]: Techniquement il y a des différences assez importantes dû au code de Dogecoin qui n'est pas à jour par rapport à Bitcoin. Taproot n'est pas implémenté. 

[^10]: [RFC 2045 | Format of Internet Message Bodies](https://datatracker.ietf.org/doc/html/rfc2045), [RFC 2046 | Media Types](https://datatracker.ietf.org/doc/html/rfc2046).

[^11]: Les chiffres historique à ce sujet manque mais vous pouvez chercher sur [OpenOrdex](https://openordex.org/collection?slug=bitcoin-shrooms) si cela vous intéresse. 

[^12]: 

[^13]: Plus gros airdrop Bitcoin jamais réalisé ayant occasioné le minage du bloc: [Block 832849](https://mempool.space/block/00000000000000000000e37d10aa5a5ece8dba4a20f011280ae3d1880414ff7e). Un *airdrop* est un envoi gratuit d'inscription(s) ou de jeton(s). 

[^14]: En ce moment, mempool.space propose un service d'accéleration de transaction basé sur ce principe d'accord (off-chain, pris entre le mineur et l'utilisateur par l'intermédiaire de mempool). Est-ce que ces accords successifs avec TaprootWizards et Runestone ont joués pour quelque chose ?


[^15]: Pour un exemple de protocole *stateless* on peut penser à Bitcoin qui ne stocke que les UTXO et non pas les états des adresses (nativement) en opposition à Ethereum qui stocke les états de chaque adresses au cours du temps. Ethereum est un exemple de protocole *stateful*. 







































