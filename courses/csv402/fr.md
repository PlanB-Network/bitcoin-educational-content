---
name: Introduction à la programmation RGB
goal: Apprendre les bases de la pile de programmation RGB et construire vos premières applications RGB
objectives:
  - Comprendre RGB de manière théorique
  - Exécuter un nœud RGB
  - Construire sur RGB
---

# Un voyage dans RGB

Dans ce programme, nous plongerons profondément dans RGB, une solution révolutionnaire à plusieurs couches pour la scalabilité de Bitcoin. RGB utilise une validation côté client pour intégrer ses contrats intelligents dans Bitcoin, permettant des contrats hors chaîne et des cas d'utilisation évolutifs du protocole. De la DeFi aux NFT en passant par la création d'actifs, RGB est une technologie prometteuse qui peut permettre de nombreux nouveaux cas d'utilisation incensurables.

Dans ce cours, nous nous concentrerons d'abord sur les aspects théoriques, puis explorerons la partie programmation, et enfin, nous examinerons quelques exemples et exercices concrets de la vie réelle. Le cours est issu d'un séminaire en direct organisé par Fulgur'Ventures et enseigné par trois enseignants renommés et experts en RGB.

Profitez-en et bonne chance avec l'un des sujets les plus avancés de Bitcoin.

+++

# Introduction au cours RGB
<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Présentation du cours
<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Bonjour à tous et bienvenue dans cette formation dédiée à RGB, un système de contrats intelligents validés côté client, fonctionnant sur Bitcoin et le Lightning Network. La structure de cette formation est pensée pour permettre une exploration approfondie de ce sujet complexe. Voici comment la formation est organisée :

**Section 1 : Théorie**  

La première section est dédiée aux concepts théoriques nécessaires pour comprendre les principes fondamentaux de la validation côté client et de RGB. Ces notions dépassent en complexité celles de Bitcoin et de la blockchain, car elles impliquent une nature distribuée des données, contrairement à la centralisation des données sur une blockchain, donc nous allons prendre le temps d'étudier cela.

**Section 2 : Pratique**  

La deuxième section portera sur l'application des concepts théoriques vus dans la section 1. Nous apprendrons à créer et manipuler des contrats RGB, à programmer avec ces outils, et à explorer les développements futurs pour simplifier ce processus.

**Section 3 : Applications**  

La dernière section est animée par d'autres intervenants qui présentent des applications concrètes basées sur RGB, afin de mettre en lumière des cas d'utilisation réels.

---

Cette formation est initialement issue d'un bootcamp de développement avancé de deux semaines à Viareggio, en Toscane, organisé par [Fulgur'Ventures](https://fulgur.ventures/). La première semaine, centrée sur Rust et les SDK, peut être retrouvée dans cet autre cours :

https://planb.network/courses/lnp402

Dans ce cours, nous nous concentrons sur la deuxième semaine du bootcamp, qui porte sur RGB.

**Semaine 1 - LNP402 :**

![RGB-Bitcoin](assets/fr/001.webp)

**Semaine 2 - Formation actuelle :**

![RGB-Bitcoin](assets/fr/002.webp)

Un grand merci à la personne qui a organisé ces cours en direct et aux 3 enseignants qui y ont participé :
- Maxim Orlovsky : *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, IA, robotique, transhumanisme. Créateur de RGB, Prime, Radiant et lnp_bp, mycitadel_io & cyphernet_io* ;
- Hunter Trujilo : *Développeur, Rust, Bitcoin, Bitcoin, Lightning, RGB* ;
- Federico Tenga : *Je fais ma part pour que le monde devienne une dystopie cypherpunk. Actuellement en train de travailler sur RGB chez Bitfinex*.

La version écrite de cette formation a été rédigée en s'appuyant sur 2 ressources principales :
- Les vidéos du séminaire de Maxim Orlovsky lors du Lightning Bootcamp ;
- La documentation de RGB, dont la production a été sponsorisée par [Bitfinex](https://www.bitfinex.com/).

# RGB en théorie
<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Introduction aux concepts de l'informatique distribuée
<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

![video](https://youtu.be/AF2XbifPGXM)


**RGB** est un protocole conçu pour appliquer et faire respecter des droits numériques (sous forme de contrats et d’actifs) de manière évolutive et confidentielle, en s’appuyant sur les règles de consensus et les opérations de la blockchain Bitcoin. L’objectif de ce premier chapitre est de présenter les concepts et la terminologie de base autour du protocole RGB, en soulignant notamment ses liens étroits avec des concepts de base de l’informatique distribuée tels que la _Client-side Validation_ et les _Single-use Seals_.

Dans ce chapitre, nous explorerons les fondements des **systèmes de consensus distribué** et nous verrons comment **RGB** s’intègre dans cette famille de technologies. Nous introduirons également les grands principes qui permettent de comprendre pourquoi RGB se veut, d’une part, extensible, et d’autre part, indépendant du mécanisme de consensus propre à Bitcoin, tout en s’appuyant sur lui lorsqu’il le faut.

### Introduction

L’**informatique distribuée** (_Distributed Computing_), une branche spécifique de l’informatique, étudie les protocoles permettant de faire circuler et de traiter des informations sur un réseau de nœuds. L’ensemble de ces nœuds et des règles du protocole constitue ce qu’on appelle un **système distribué**. Parmi les propriétés essentielles qui caractérisent un tel système, on retrouve :
- La **capacité de vérification et de validation indépendante** de certaines données par chaque nœud ;
- La possibilité pour les nœuds de construire (selon le protocole) une vue complète ou partielle de l’information. Ces vues sont les **états** du système distribué ;
- L’**ordre chronologique** des opérations, afin que les données soient horodatées de manière fiable et qu’il existe un consensus sur la séquence d’événements (séquence d’états).

En particulier, la notion de **consensus** dans un système distribué recouvre deux aspects :
- La **reconnaissance de la validité** des changements d’état (selon les règles du protocole) ;
- L’**accord sur l’ordre** de ces changements d’état, ce qui rend impossible la réécriture ou l’inversion a posteriori des opérations validées (c’est ce que l'on appelle également dans le cadre de Bitcoin, la **protection contre la double-dépense**).

La première implémentation permissionless et fonctionnelle d’un mécanisme de consensus distribué a été introduite par Satoshi Nakamoto avec Bitcoin, grâce à l’utilisation conjointe d’une structure de données en _blockchain_ et d’un algorithme de **Proof-of-Work (PoW)**. Dans ce système, la crédibilité de l’historique des blocs dépend de la puissance de calcul que les nœuds (mineurs) y consacrent. Bitcoin est donc un exemple historique et majeur de **systèmes de consensus distribué** ouvert à tous (permissionless).

Dans l'univers de la blockchain et de l'informatique distribuée, nous pouvons distinguer deux paradigmes fondamentaux : la _blockchain_ au sens traditionnel, et les _state channels_ (canaux d'état), dont le meilleur exemple en production est le _Lightning Network_. La _blockchain_ se définit comme un registre d'événements ordonnés chronologiquement, répliqué par consensus au sein d'un réseau ouvert et sans permission. Les _state channels_, eux, sont des canaux peer-to-peer qui permettent à deux (ou plusieurs) participants de maintenir un état mis à jour hors de la chaîne, ne recourant à la blockchain qu'au moment de l'ouverture et de la fermeture de ces canaux.

Dans le cadre de Bitcoin, vous connaissez sans doute les principes du minage, la décentralisation et la finalité des transactions sur la blockchain, ainsi que le fonctionnement des canaux de paiement. Nous allons introduire un nouveau paradigme appelé **client-side validation** (validation côté client), qui, contrairement à la blockchain ou à Lightning, consiste à conserver et à valider localement (côté client) les transitions d'état d'un contrat intelligent. Ceci se différencie aussi d'autres techniques de la "DeFi" (_rollups_, _plasma_, _ARK_, etc.), dans la mesure où la _client-side validation_ s'appuie sur la blockchain pour empêcher la double dépense et pour avoir un système d'horodatage, tout en conservant le registre des états et des transitions hors chaîne, uniquement chez les participants concernés.

Nous allons également plus tard introduire un terme important : la notion de "**stash**", qui désigne l'ensemble des données côté client nécessaires pour préserver l'état d'un contrat, ces données n'étant pas répliquées de façon globale sur le réseau. Enfin, nous aborderons la raison d'être de **RGB**, un protocole tirant parti de la _client-side validation_, et pourquoi il se révèle complémentaire aux approches existantes (blockchain et _state channels_).

![RGB-Bitcoin](assets/fr/003.webp)

### Les trilemmes en informatique distribuée

Pour comprendre en quoi la _client-side validation_ et RGB répondent à des problématiques non résolues par la blockchain et Lightning, découvrons 3 "trilemmes" majeurs en informatique distribuée :

1. **Scalabilité, Décentralisation, Privacy**
2. **Théorème CAP** (Cohérence, Disponibilité, tolérance aux Partitions)
3. **Trilemme CIA** (Confidentialité, Intégrité, Disponibilité)

#### 1. Scalabilité, décentralisation et confidentialité

- **Blockchain (Bitcoin)**

La blockchain est très décentralisée, mais peu scalable. De plus, comme tout se trouve dans un registre global et public, la confidentialité est limitée. On peut tenter d'améliorer la confidentialité avec des technologies zero-knowledge (transactions confidentielles, schémas mimblewimble, etc.), mais la chaîne publique ne peut pas cacher le graphe des transactions.

- **Lightning/State channels**

Les canaux d'état (comme avec le Lightning Network) sont plus scalables et plus privés que la blockchain, car les transactions s'effectuent hors chaîne. Toutefois, l'obligation d'annoncer publiquement certains éléments (transactions de financement, topologie du réseau) et la surveillance du trafic réseau peuvent compromettre en partie la confidentialité. Aussi, la décentralisation en pâtit : le routage requiert une grande quantité de liquidités et les nœuds majeurs peuvent devenir des points de centralisation. C'est justement un phénomène que l'on peut commencer à observer actuellement sur Lightning.

- **Client-side validation (RGB)**

Ce nouveau paradigme est encore plus scalable et plus confidentiel, car non seulement on peut intégrer des techniques zero-knowledge, mais il n'y a pas de graphe global des transactions : personne ne détient la totalité du registre. En revanche, cela implique aussi un certain compromis sur la décentralisation : un _contract issuer_ (l'émetteur d'un contrat intelligent) peut avoir un rôle central (à l'instar d'un _contract deployer_ dans Ethereum). Néanmoins, contrairement à la blockchain, avec la _client-side validation_, vous ne stockez et ne validez que les contrats qui vous intéressent, ce qui améliore la scalabilité en évitant de télécharger et de vérifier tous les états existants.

![RGB-Bitcoin](assets/fr/004.webp)

#### 2. Théorème CAP (Consistency, Availability, Partition tolerance)

Le **théorème CAP** souligne qu'il est impossible pour un système distribué de satisfaire simultanément la cohérence (Consistency), la disponibilité (Availability) et la tolérance au partitionnement (Partition tolerance).

- **Blockchain**

La blockchain privilégie la cohérence et la disponibilité, mais s'accommode mal de la partition du réseau : si vous ne voyez pas un bloc, vous n'êtes pas en mesure d'agir et d'avoir la même vue que l'ensemble du réseau.

- **Lightning**

Un système de canaux d'états dispose de la disponibilité et de la tolérance au partitionnement (puisque deux nœuds peuvent rester connectés entre eux même si le réseau est fragmenté), mais la cohérence globale dépend de l'ouverture et de la fermeture des canaux sur la blockchain.

- **Client-side validation (RGB)**

Un système comme RGB offre la cohérence (chaque participant valide ses données localement, sans ambiguïté) et la tolérance au partitionnement (vous conservez vos données de manière autonome), mais ne garantit pas la disponibilité globale (chacun doit s'assurer d'avoir les morceaux d'historique pertinents, et certains participants peuvent ne rien publier ou cesser de partager certaines informations).

![RGB-Bitcoin](assets/fr/005.webp)

#### 3. Trilemme CIA (Confidentiality, Integrity, Availability)

Ce trilemme rappelle que la confidentialité, l'intégrité et la disponibilité ne peuvent être optimisées toutes les trois en même temps. Blockchain, Lightning et _client-side validation_ se répartissent différemment dans cet équilibre. L'idée est qu'aucun système unique ne peut tout fournir ; il faut combiner plusieurs approches (la time-stamping de la blockchain, l'approche synchrone de Lightning, et la validation locale avec RGB) pour obtenir un ensemble cohérent offrant de bonnes garanties dans chaque dimension.

![RGB-Bitcoin](assets/fr/006.webp)

### Le rôle de la blockchain et la notion de sharding

La blockchain (ici Bitcoin) sert surtout de mécanisme de _time-stamping_ et de protection contre la double dépense. Au lieu d'y insérer l'intégralité des données d'un smart contract ou d'un système décentralisé, on se contente d'y inclure des **engagements cryptographiques** (_commitments_) à des transactions (au sens de la _client-side validation_, que nous appellerons "transitions d'état"). Ainsi :
- On libère la blockchain d'une grande quantité de données et de logique.
- Chaque utilisateur ne stocke que l'historique nécessaire à sa propre portion du contrat (son "shard"), au lieu de répliquer l'état global.

Le _sharding_ est un concept né dans les bases de données distribuées (par exemple MySQL pour des réseaux sociaux comme Facebook ou Twitter). Pour résoudre le problème de volume de données et de latences de synchronisation, on segmente la base en _shards_ (États-Unis, Europe, Asie, etc.). Chaque segment est cohérent localement et ne se synchronise que partiellement avec les autres.

Pour les smart contracts de type RGB, on "sharde" selon les contrats eux-mêmes. Chaque contrat constitue un _shard_ indépendant. Par exemple, si vous ne détenez que des jetons USDT, vous n'avez pas à stocker ou valider tout l'historique d'un autre token comme l'USDC. Sur Bitcoin, la blockchain ne fait pas de _sharding_ : vous avez un ensemble d'UTXOs global. Avec la _client-side validation_, chaque participant conserve seulement les données des contrats qu'il détient ou utilise.

On peut donc imaginer l'écosystème ainsi :
- **La blockchain (Bitcoin)** comme fondation qui assure la réplication complète d'un registre minimal et sert de couche d'horodatage ;
- **Le Lightning Network** pour des transactions rapides et confidentielles, qui repose toujours sur la sécurité et le règlement final de la blockchain Bitcoin ;
- **RGB et la client-side validation** pour ajouter une logique plus complexe de smart contracts, sans encombrer la blockchain, ni perdre en confidentialité.

![RGB-Bitcoin](assets/fr/007.webp)

Ces trois éléments forment un ensemble triangulaire plus qu'un empilement linéaire de "layer 2", "layer 3", etc. Lightning peut se brancher directement sur Bitcoin, ou bien être associé à des transactions Bitcoin qui intègrent des données RGB. De même, un usage de la "BiFi" (finance sur Bitcoin) peut composer avec la blockchain, Lightning et RGB selon les besoins en confidentialité, scalabilité, ou logique de contrat.

![RGB-Bitcoin](assets/fr/008.webp)

### La notion de transitions d'état

Dans tout système distribué, l’objectif du mécanisme de validation est de pouvoir **déterminer la validité et l’ordre chronologique des changements d’état**. Il s’agit de vérifier que les règles du protocole sont bien respectées et de prouver que ces changements d’état se succèdent dans un ordre définitif et inattaquable.

Pour comprendre comment se présente cette validation dans le cadre de **Bitcoin** et, plus généralement, pour saisir la philosophie derrière la *Client-side Validation*, revenons d’abord sur les mécanismes de la blockchain Bitcoin, avant de voir comment la validation côté client s’en démarque et quelles optimisations elle rend possibles.

![RGB-Bitcoin](assets/fr/009.webp)

Dans le cas de la blockchain Bitcoin, la validation des transactions repose sur une règle simple :
- Tous les nœuds du réseau téléchargent chaque bloc et chaque transaction ;
- Ils **valident** ces transactions pour vérifier la bonne évolution de l'**UTXO set** (ensemble des sorties non dépensées) ;
- Ils **stockent** ces données (sous forme de blocs) de manière à pouvoir rejouer l’historique si nécessaire.

![RGB-Bitcoin](assets/fr/010.webp)

Ce modèle présente toutefois deux inconvénients majeurs :
- **Scalabilité** : puisque chaque nœud doit traiter, vérifier et archiver toutes les transactions de tout le monde, il existe une limite évidente à la capacité de transaction, liée notamment à la taille maximale des blocs (1 Mo en moyenne sur 10 minutes pour Bitcoin, hors witness) ;
- **Vie privée** : tout est diffusé et stocké publiquement (montants, adresses de destination, etc.), ce qui limite la confidentialité des échanges.

![RGB-Bitcoin](assets/fr/012.webp)

En pratique, ce modèle fonctionne pour Bitcoin en tant que couche de base (Layer 1), mais peut devenir insuffisant pour des usages plus complexes qui exigent simultanément un haut débit de transactions et un certain degré de confidentialité.

La *Client-side Validation* repose sur l’idée inverse : plutôt que d’exiger que tout le réseau valide et stocke toutes les transactions, chaque participant (client) va valider uniquement la partie de l’historique qui le concerne.

- Lorsqu’une personne reçoit un actif (ou toute autre propriété numérique), elle n’a besoin de connaître et de vérifier que la chaîne d’opérations (les transitions d'état) qui aboutit à cet actif et qui lui en prouve la légitimité.
- Cette suite d’opérations, du **genesis** (émission initiale) jusqu’à la transaction la plus récente, forme un graphe orienté acyclique (DAG) ou un **shard**, c’est-à-dire une fraction du grand historique global.

![RGB-Bitcoin](assets/fr/013.webp)

Parallèlement, pour que le reste du réseau (ou plus exactement la couche sous-jacente, telle que Bitcoin) puisse **verrouiller** l’état final sans pour autant voir le détail de ces données, la *Client-side Validation* s’appuie sur la notion de **commitment**.

Un commitment est un engagement cryptographique, typiquement un _hash_ (SHA-256 par exemple) inséré dans une transaction Bitcoin, qui prouve qu’on a englobé des données privées, sans révéler ces données.

Grâce à ces _commitments_, on peut prouver :
- L’existence d’une information (puisqu’elle est engagée dans un hash) ;
- L’antériorité de cette information (car elle est ancrée et horodatée dans la blockchain, avec une date et un ordre des blocs).

En revanche, le contenu exact n’est pas révélé, ce qui préserve la confidentialité.

Concrètement :
- Vous préparez une nouvelle transition d'état (par exemple le transfert d'un jeton RGB).
- Vous générez un engagement cryptographique à cette transition et l'insérez dans une transaction Bitcoin (on appelle ces engagements des "anchors" dans le protocole RGB).
- La contrepartie (le destinataire) récupère l'historique _client-side_ associé à cet actif et valide la cohérence de bout en bout, depuis la Genèse du smart contract jusqu'à la transition que vous lui transmettez.

![RGB-Bitcoin](assets/fr/014.webp)

La *Client-side Validation* présente ainsi deux bénéfices majeurs :

- **La scalabilité :**  
Les engagements (*commitments*) inclus dans la blockchain ont une taille réduite (de l’ordre de quelques dizaines d’octets). Cela permet de ne pas saturer l’espace dans les blocs, car seul le hash doit être inclus, et cela permet également de faire évoluer le protocole off-chain, car chaque utilisateur n’a à stocker que son fragment d’historique (son _stash_).

- **La privacy :**  
Les transactions en elles-mêmes (c’est-à-dire leur contenu détaillé) ne sont pas publiées on-chain. Seules leurs empreintes (*hash*) le sont. Ainsi, les montants, les adresses et la logique du contrat restent privés, et le receveur peut vérifier, en local, la validité de son shard en inspectant toutes les transitions antérieures. Il n’a aucune raison de diffuser ces données publiquement, sauf en cas de litige ou de preuve nécessaire.

Dans un système comme RGB, plusieurs transitions d'état de différents contrats (ou différents actifs) peuvent être agrégées dans une même transaction Bitcoin via un seul _commitment_, parfois appelé **Anchor**. Ce mécanisme :
- Établit un lien déterministe et horodaté entre la transaction on-chain et les données off-chain (les transitions validées côté client) ;
- Permet d’enregistrer simultanément plusieurs shards dans un même point d’ancrage, ce qui réduit encore plus le coût et l’empreinte on-chain.

En pratique, lorsque cette transaction Bitcoin est validée, elle "verrouille" définitivement l’état des contrats sous-jacents, puisqu’il devient impossible de modifier le hash déjà inscrit dans la blockchain.

![RGB-Bitcoin](assets/fr/015.webp)

### Le concept de stash

Un **stash** est l'ensemble de données côté client qu'un participant doit absolument conserver pour maintenir l'intégrité et l'historique d'un smart contract RGB. Contrairement à un canal Lightning, où l'on peut reconstruire certains états localement à partir d'informations partagées, le stash d'un contrat RGB n'est pas répliqué ailleurs : si vous le perdez, personne ne pourra vous le restaurer, car vous êtes responsable de votre part de l'historique. D'où l'intérêt de procédures de sauvegarde fiables dans RGB.

![RGB-Bitcoin](assets/fr/016.webp)


### Single use seal : origines et fonctionnement

Lors de l'acceptation d'un actif comme par exemple une monnaie, deux garanties sont essentielles :
- L'authenticité du jeton reçu ;
- L'unicité du jeton, afin d'éviter les doubles dépenses.

Pour les actifs physiques, comme un billet de banque, la présence physique suffit à prouver qu'il n'est pas dupliqué. Cependant, dans le monde numérique, où les actifs sont purement informationnels, cette vérification est plus complexe, car l'information peut facilement se multiplier et être dupliquée.

Comme nous l'avons vu précédemment, la révélation par l'envoyeur de l'historique des transitions d'état permet de s'assurer de l'authenticité d'un jeton RGB. En ayant accès à toutes les transactions depuis la transaction génésique, on peut confirmer l'authenticité du jeton. Ce principe est similaire à celui de Bitcoin où l'on peut suivre l'historique des pièces jusqu'à la transaction coinbase originelle pour vérifier leur validité. Toutefois, contrairement à Bitcoin, cet historique des transitions d'état dans RGB est privé et conservé côté client.

Pour prévenir la double dépense des jetons RGB, nous utilisons un mécanisme appelé "*Single-use Seal*". Ce système assure que chaque jeton, une fois utilisé, ne peut être réutilisé frauduleusement.

Les **Single-use Seals** sont des primitives cryptographiques, proposées en 2016 par Peter Todd, qui s’apparentent au concept de scellés physiques : une fois qu’on a placé un sceau sur un conteneur, il devient impossible de l’ouvrir ou de le modifier sans briser le sceau de manière irréversible.

![RGB-Bitcoin](assets/fr/018.webp)

Cette approche, transposée à l’univers numérique, permet de prouver qu’une séquence d’événements a bel et bien eu lieu et qu’elle ne peut plus être altérée a posteriori. Les Single-use Seals dépassent donc la simple logique de `hash + timestamp` en y ajoutant la notion d’un _sceau_ fermable **une seule et unique fois**.

![RGB-Bitcoin](assets/fr/017.webp)

Pour que les Single-use Seals fonctionnent, il faut un ***Proof-of-Publication Medium*** : un support capable de prouver l’existence ou l’absence d’une publication et difficile (voire impossible) à falsifier une fois l’information diffusée. Une **blockchain** (comme Bitcoin) peut tenir ce rôle, tout comme un journal papier au tirage public. L’idée est la suivante :
- On veut prouver qu’un certain engagement sur un message `h(m)` a été publié à une audience sans révéler le contenu du message `m` ;
- On veut prouver qu’aucun autre engagement de message `h(m')` concurrent n’a été publié à la place de `h(m)` ;
- On veut également pouvoir vérifier que le message `m` existe avant une certaine date.

Une **blockchain** se prête idéalement à ce rôle : dès qu’une transaction est incluse dans un bloc, tout le réseau possède la même preuve infalsifiable de son existence et de son contenu (du moins en partie, puisque le _commitment_ peut masquer les détails tout en prouvant l’authenticité du message).

On peut donc voir un Single-use Seal comme une promesse formelle de publier un message (encore inconnu à ce stade) une et une seule fois, de manière vérifiable par toutes les parties intéressées.

Contrairement aux simples _commitments_ (hash) ou aux timestamps qui attestent d’une date d’existence, un Single-use Seal offre la garantie supplémentaire qu’**aucun engagement alternatif** ne peut coexister : on ne peut pas fermer deux fois le même sceau ou tenter de remplacer le message scellé.

La comparaison suivante aide à comprendre :
- **Engagement cryptographique (hash)** : Avec une fonction de hachage, on peut s'engager sur une donnée (un nombre) en publiant son empreinte (hash). La donnée reste secrète tant qu'on ne révèle pas le préimage, mais on peut prouver qu'on la connaissait à l'avance.
- **Horodatage (blockchain)** : En insérant ce hash dans la blockchain, on prouve aussi qu'on le connaissait à un instant précis (celui de l'inclusion dans un bloc).
- **Single-use seal** : Avec les sceaux à usage unique, on va plus loin en rendant l'engagement unique. Avec un simple hash, on peut créer plusieurs engagements contradictoires en parallèle (le problème du docteur qui annonce "*C'est un garçon*" à la famille et "*C'est une fille*" dans son journal personnel). Le single-use seal élimine cette possibilité en connectant l'engagement à un support de preuve de publication, comme la blockchain Bitcoin, de sorte qu'une dépense d'UTXO scelle définitivement l'engagement. Une fois dépensé, on ne peut plus redépenser le même UTXO pour remplacer l'engagement.

|                                                                                  | Engagement simple (digest/hash) | Timestamps | Single-use seals |
| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |
| La publication de l'engagement ne révèle pas le message                          | Oui                             | Oui        | Oui              |
| Preuve de la date de l'engagement / existence du message avant une certaine date | Impossible                      | Possible   | Possible         |
| Preuve qu'aucun autre engagement alternatif ne peut exister                      | Impossible                      | Impossible | Possible         |

Le fonctionnement des Single-use Seals s’articule autour de trois grandes étapes :

**Seal Definition :**
- Alice définit à l’avance les règles de publication du sceau (quand, où et comment le message sera publié) ;
- Bob accepte ou constate ces conditions.

![RGB-Bitcoin](assets/fr/021.webp)

**Seal Closing :**
- Au moment de l’exécution, Alice ferme le sceau en publiant le message effectif (généralement sous forme de _commitment_, par exemple un hash) ;
- Elle fournit aussi un **witness** (preuve cryptographique) prouvant que le sceau est bel et bien fermé et irrévocable.

![RGB-Bitcoin](assets/fr/019.webp)

**Seal Verification :**
- Une fois le sceau fermé, Bob ne peut plus l’ouvrir : il peut simplement vérifier qu’il a bien été clos ;
- Bob récupère le sceau, le **witness** et le message (ou son engagement) pour s’assurer que tout concorde et qu’il n’existe pas de sceau concurrent ou de version différente.

On peut résumer le processus :

```txt
# Défini par Alice, validé ou accepté par Bob

seal <- Define()

# Fermeture du sceau par Alice avec le message

witness <- Close(seal, message)

# Vérification par Bob

bool <- Verify(seal, witness, message)
```


Dans le cadre de la **Client-side Validation**, il faut toutefois aller plus loin : si la définition d’un sceau reste elle-même hors de la blockchain, il est possible (en théorie) que quelqu’un conteste l’existence ou la légitimité du sceau en question. Pour pallier ce problème, on recourt à une **chaîne de Single-use Seals**, imbriqués les uns dans les autres :
- Chaque sceau fermé renferme la définition du sceau suivant ;
- On inscrit ces fermetures (avec leurs _commitments_) au sein de la **blockchain** (par exemple, dans une transaction Bitcoin) ;
- Ainsi, toute tentative de modifier un sceau antérieur se retrouverait en contradiction avec l’historique ancré sur Bitcoin.

C’est précisément ce que fait le système **RGB** :
- Les messages publiés sont les _commitments_ vers des données validées côté client ;
- La définition du sceau est associée à un UTXO Bitcoin ;
- Le sceau se ferme lorsque l’on dépense cet UTXO ou qu’on crédite une nouvelle sortie liée au même engagement ;
- La chaîne de transactions qui dépense ces UTXOs correspond à la **Proof-of-Publication** : chaque transition ou changement d’état sur RGB s’ancre ainsi dans Bitcoin.

Pour résumer :
- Le _seal definition_ est l'UTXO que vous destinez à sceller un engagement futur ;
- Le _seal closing_ survient quand vous dépensez cet UTXO, en créant une transaction qui contient l'engagement ;
- Le _witness_ est la transaction elle-même, qui prouve que vous avez bien fermé le sceau avec ce contenu ;
- Vous ne pouvez pas prouver qu'un seal n'a pas été fermé (on ne peut pas être absolument sûr qu'un UTXO n'est pas déjà dépensé ou ne le sera pas dans un bloc qu'on n'a pas encore vu), mais on peut prouver qu'il a bel et bien été fermé de telle ou telle façon.

Cette unicité est importante pour la Client-side Validation : quand vous validez une transition d'état, vous vérifiez qu'elle correspond à un UTXO unique, non dépensé préalablement dans un engagement concurrent. C'est ce qui garantit l'absence de double dépense au niveau des smart contracts off-chain.

### Engagements multiples et ancrages

Un smart contract RGB peut avoir besoin de dépenser simultanément plusieurs single use seals (plusieurs UTXOs). De plus, une seule transaction Bitcoin peut référencer plusieurs contrats distincts, chacun venant sceller sa propre transition d'état. Cela nécessite un mécanisme de **multi-commitments** permettant de prouver, de manière déterministe et unique, qu'aucun des engagements n'existe en double. C'est ici qu'intervient la notion d'**anchor** dans RGB : une structure spéciale reliant une transaction Bitcoin et un ou plusieurs engagements _client-side_ (transitions d'état), chacun relevant potentiellement d'un contrat différent. Nous allons justement détailler ce concept dans le chapitre suivant.

![RGB-Bitcoin](assets/fr/023.webp)

Deux principaux dépôts GitHub du projet (sous l'organisation "LNPBP") regroupent les implémentations de base de ces concepts étudiés dans le premier chapitre :
- **client_side_validation** : Contient les primitives Rust pour la validation locale.
- **single_use_seals** : Implémente la logique pour définir et fermer ces seals de manière sécurisée.

![RGB-Bitcoin](assets/fr/020.webp)

Ces briques sont agnostiques par rapport à Bitcoin ; on pourrait, en théorie, les appliquer à tout autre support de preuve de publication (un autre registre, un journal, etc.). Dans la pratique, RGB repose sur Bitcoin pour sa robustesse et son large consensus.

![RGB-Bitcoin](assets/fr/021.webp)

### Questions du public

#### Vers un usage plus large des single use seals

Peter Todd a également créé le protocole _Open Timestamps_, et le concept de single use seal est un prolongement naturel de ces idées. Au-delà de RGB, on peut envisager d'autres cas d'utilisation, par exemple la construction de _sidechains_ sans recourir au _merge mining_ ni aux propositions liées aux drivechains comme le BIP300. Tout système nécessitant un engagement unique peut, en principe, exploiter cette primitive cryptographique. Aujourd'hui, RGB est la première grande mise en application concrète et complète.

#### Problèmes de disponibilité des données

Étant donné qu'en _client-side validation_, chaque utilisateur stocke sa partie de l'historique, la disponibilité des données n'est pas garantie globalement. Si un émetteur de contrat ne publie pas certaines informations ou les révoque, vous pourriez ignorer l'évolution réelle de l'offre. Dans certains cas (comme les stablecoins), on s'attend à ce que l'émetteur tienne à jour des données publiques pour prouver le volume en circulation, mais rien ne l'y contraint techniquement. Il est donc possible de concevoir des contrats volontairement opaques avec un stock illimité, ce qui pose des questions de confiance.

#### Sharding et isolement des contrats

Chaque contrat représente un _shard_ isolé : USDT et USDC, par exemple, n'ont pas à partager leur historique. Les swaps atomiques restent possibles, mais cela n'implique pas de fusionner leurs registres. Tout se fait par engagement cryptographique, sans divulguer l'ensemble du graphe d'historique à chaque participant.

### Conclusion

Nous avons vu où se situe le concept de _client-side validation_ par rapport à la blockchain et aux _state channels_, en quoi il répond à des trilemmes persistants de l'informatique distribuée, et comment il exploite la blockchain Bitcoin uniquement pour éviter la double dépense et pour l'horodatage (time-stamping). L'idée repose sur la notion de **single use seal**, permettant la création d'engagements uniques que vous ne pouvez pas redépenser à volonté. Ainsi, chaque participant ne télécharge que l'historique strictement nécessaire, ce qui accroît la scalabilité et la confidentialité des smart contracts tout en conservant la sécurité de Bitcoin en toile de fond.

La prochaine étape consistera à expliquer plus en détail comment on applique concrètement ce mécanisme de single use seal dans Bitcoin (via les UTXOs), comment on crée et on valide les **anchors**, puis comment on bâtit des _smart contracts_ complets dans RGB. Nous verrons notamment la question des engagements multiples, le défi technique de prouver qu'une transaction Bitcoin scelle simultanément plusieurs transitions d'état dans différents contrats, sans introduire de vulnérabilités ou de doubles engagements.

Avant de plonger dans les détails plus techniques du deuxième chapitre, n'hésitez pas à relire les définitions clés (client-side validation, single use seal, anchors, etc.) et à garder à l'esprit la logique globale : nous cherchons à concilier les atouts de la blockchain Bitcoin (sécurité, décentralisation, _time-stamping_) avec ceux des solutions hors chaîne (rapidité, confidentialité, scalabilité), et c'est précisément ce que RGB et la _client-side validation_ tentent de réaliser.




## Validation côté client
<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

![video](https://youtu.be/FS6PDprWl5Q)

Nous allons désormais appliquer tout ce que nous avons vu dans le premier chapitre au cas spécifique de Bitcoin et de RGB. Nous allons revenir sur la notion de _single-use seals_ (scellés à usage unique), cette fois-ci directement par-dessus les transactions Bitcoin. Ensuite, nous parlerons de deux points importants qui n’ont pas encore été traités en détail :

- Les _deterministic Bitcoin commitments_
- Les _multi-protocol commitments_

C’est la combinaison de ces concepts qui nous permet de superposer plusieurs systèmes ou contrats au-dessus d’un même _UTXO_ et donc d’une même blockchain.

### Les single-use seals sur Bitcoin

Avant d’entrer dans le vif du sujet, il y a souvent une plaisanterie autour de l’orthographe du terme _single-use seals_, qui peut sembler ambigu en anglais. Si quelqu’un a une façon arrêtée de l’écrire, avec des tirets ou autre, il est libre d’avoir son opinion. Mais l’important est moins l’orthographe que la notion technique derrière.

Comme vu dans le premier chapitre de la formation, les _single-use seals_ sont un concept général : on fait une promesse d’inclure un engagement (un _commitment_) dans un emplacement précis d’une transaction, cet emplacement agit comme un scellé que l’on ferme sur un message. Toutefois, sur la blockchain Bitcoin, plusieurs options existent pour choisir où placer ce _commitment_.

Pour comprendre la logique, rappelons le principe de base : pour fermer un _single-use seal_, on dépense l’endroit scellé en y insérant le _commitment_ sur un message donné. Dans Bitcoin, cela peut se faire de différentes manières :

- **Utiliser une clé publique ou une adresse**  

On peut décider qu’une clé publique ou une adresse spécifique est le _single-use seal_. Dès que cette clé ou cette adresse apparaît on-chain dans une transaction, cela signifie que le scellé est fermé avec un certain message.

- **Utiliser un output de transaction Bitcoin**  

Cela signifie que l’on définit un _single-use seal_ comme un _outpoint_ précis (un couple `TXID + numéro d’output`). Dès que cet _outpoint_ est dépensé, il s’agit de l’acte de fermeture du scellé.

Bien sûr, selon la méthode retenue, le _commitment_ (c’est-à-dire la donnée prouvant le message) peut être placé soit dans l’output de la transaction, soit dans l’input qui dépense l’UTXO concerné.

En travaillant sur RGB, nous avons identifié au moins 4 manières différentes d’implémenter ces scellés sur Bitcoin :
- Définir le scellé via une clé publique, et le fermer dans un _output_
- Définir le scellé via un _outpoint_, et le fermer dans un _output_
- Définir le scellé via la valeur d'une clé publique, et le fermer dans un _input_
- Définir le scellé via un _outpoint_, et le fermer dans un _input_

| Nom du schéma | Définition du scellé      | Fermeture du scellé   | Exigences supplémentaires                                         | Application principale       | Schémas d'engagement possibles |
| ------------- | ------------------------- | --------------------- | ----------------------------------------------------------------- | ---------------------------- | ------------------------------ |
| Pk0           | Valeur de la clé publique | Sortie de transaction | P2(W)PKH                                                          | Aucune pour le moment        | Keytweak, taptweak, opret      |
| Tx02          | Sortie de transaction     | Sortie de transaction | Nécessite des engagements déterministes sur Bitcoin               | RGBv1 (universel)            | Keytweak, taptweak, opret      |
| PkI           | Valeur de la clé publique | Entrée de transaction | Uniquement Taproot & non compatible avec les portefeuilles Legacy | Identités basées sur Bitcoin | Sigtweak, witweak              |
| Tx01          | Sortie de transaction     | Entrée de transaction | Uniquement Taproot & non compatible avec les portefeuilles Legacy | Aucune pour le moment        | Sigtweak, witweak              |

Nous ne détaillerons pas chacune de ces configurations, car dans RGB, nous avons choisi d’utiliser **un _outpoint_ comme définition du scellé**, et de placer le _commitment_ dans l’output de la transaction dépensant cet _outpoint_. On peut donc introduire les concepts suivants pour la suite :
- **"Seal definition"** : Un _outpoint_ donné (identifié par `TXID + N° de sortie`).
- **"Seal closing"** : La transaction qui dépense cet _outpoint_, dans laquelle on ajoute un _commitment_ à un message.

Ce schéma a été sélectionné pour sa compatibilité avec l’architecture RGB, mais d’autres configurations pourraient être utiles pour des usages différents (par exemple pour la gestion d’identités sur Bitcoin).

### Le fonctionnement du single-use seal basé sur un outpoint

Pour rappel, définir un _single-use seal_ ne nécessite pas nécessairement de publier une transaction on-chain. Il suffit qu’Alice, par exemple, possède déjà un UTXO non dépensé. Elle peut décider : "Cet _outpoint_ (déjà existant) est désormais mon scellé". Elle le note localement (_client-side_), et tant que cet UTXO n’est pas dépensé, le scellé est considéré comme ouvert.

![RGB-Bitcoin](assets/fr/024.webp)

#### Fermeture du scellé

Le jour où elle veut fermer le scellé (pour signaler un événement, ou pour ancrer un message particulier), elle dépense cet UTXO dans une nouvelle transaction (on appelle souvent cette transaction la _witness transaction_, sans rapport avec _segwit_, c’est juste le terme qu’on lui donne). Cette nouvelle transaction contiendra le _commitment_ au message.

![RGB-Bitcoin](assets/fr/025.webp)

- **Personne d’autre que Bob** (ou les personnes à qui Alice choisit de révéler la preuve complète) ne saura qu’un certain message est caché dans cette transaction.
- Tout le monde peut constater que l'_outpoint_ a été dépensé, mais seul Bob détient la preuve que le message est bien ancré dans la transaction.

#### Exemple : révocation de clé PGP

Pour illustrer, on peut utiliser un _single-use seal_ comme mécanisme de révocation d’une clé PGP. Au lieu de publier un certificat de révocation sur des serveurs, Alice peut dire : "Cette sortie Bitcoin, si elle est dépensée, signifie que ma clé PGP est révoquée."

![RGB-Bitcoin](assets/fr/026.webp)

Au moment où Alice dépense cet UTXO, elle referme le scellé sur un message qui indique sa nouvelle clé, ou simplement la révocation de l’ancienne. Ainsi, toute personne surveillant on-chain verra que l’UTXO est dépensé, mais seule celle qui dispose de la preuve complète saura qu’il s’agit précisément de la révocation de la clé PGP.

![RGB-Bitcoin](assets/fr/027.webp)

#### Ancrage et preuve

Pour que Bob ou toute autre personne concernée puisse vérifier le message caché, Alice doit lui fournir des informations off-chain.

![RGB-Bitcoin](assets/fr/028.webp)

Alice doit donc fournir à Bob :
- Le message lui-même (par exemple, la nouvelle clé PGP).
- La preuve cryptographique attestant que ce message a été engagé dans la transaction (ce qu’on appelle l’_extra transaction proof_ ou _anchor_).

![RGB-Bitcoin](assets/fr/029.webp)

Les tiers n’ont pas cette information. Ils voient seulement qu’un UTXO a été dépensé. La confidentialité est donc assurée.

Pour bien clarifier la structure, récapitulons le cheminement en deux transactions :

- **Transaction 1** : Elle contient la _seal definition_, c’est-à-dire l'_outpoint_ qui servira de scellé.

![RGB-Bitcoin](assets/fr/031.webp)

- **Transaction 2** : Elle dépense cet _outpoint_. De ce fait, le scellé est fermé et, dans cette même transaction, on insère le _commitment_ sur le message.

![RGB-Bitcoin](assets/fr/033.webp)

Nous appelons donc la seconde transaction la "_witness transaction_". 

Pour illustrer cela sous un autre angle, on peut représenter deux couches :

- **La couche supérieure (blockchain, publique)** : tout le monde voit la transaction et sait qu’il y a un _outpoint_ dépensé.
- **La couche inférieure (client-side, privée)** : seule Alice (ou la personne intéressée) sait que cette dépense correspond à tel message, via la preuve cryptographique et le message qu’elle conserve en local.

![RGB-Bitcoin](assets/fr/034.webp)

Mais lors de cette fermeture du scellé, on peut se poser la question suivante : concrètement, où devons-nous insérer le _commitment_ ?

### Deterministic Bitcoin Commitments

Nous avons brièvement mentionné, dans la partie précédente, comment le modèle _client-side validation_ peut s’appliquer à RGB ou à d’autres systèmes. Ici, nous abordons la partie concernant les **deterministic Bitcoin commitments** et la façon de les intégrer dans une transaction. L’idée est de comprendre pourquoi on cherche à insérer un unique engagement dans la _witness transaction_, et surtout comment s’assurer qu’il ne puisse y avoir d’autres engagements concurrents non dévoilés.

#### L’importance d’un unique engagement dans la witness transaction

Lorsque vous transmettez à quelqu’un la preuve qu’un certain message est ancré dans une transaction, vous devez pouvoir garantir qu’il n’existe pas, dans cette même transaction, une autre forme d’engagement (un second message caché) qui ne vous aurait pas été révélé. Pour que la validation _côté client_ reste robuste, il faut donc un mécanisme **déterministe** permettant de placer un unique _commitment_ dans la transaction qui ferme le _single-use seal_.

La _witness transaction_ dépense le fameux UTXO (ou _seal definition_) et cette dépense correspond à la fermeture du scellé. Au niveau technique, on sait que chaque outpoint ne peut être dépensé qu’une seule fois. C’est justement ce qui sert de base à la résistance à la double dépense sur Bitcoin. Mais la transaction de dépense peut avoir plusieurs _inputs_, plusieurs _outputs_, ou être composée de façon complexe (coinjoins, cannaux Lightning, etc.). Il faut donc définir clairement où insérer le _commitment_ dans cette structure, sans ambiguïté et de manière uniforme.

#### Où mettre le commitment dans la transaction ?

- **Dans l’input ?**  

Potentiellement, on peut utiliser la partie _scriptSig_ ou _witness_ de l’input qui dépense le scellé. Par exemple, la signature ECDSA ou Schnorr contient une composante “aléatoire” (nonce) que l’on pourrait _tweaker_ pour y glisser un engagement.

- **Dans l’output ?**  

On peut également choisir d’insérer le _commitment_ dans le _scriptPubKey_ d’une sortie. C’est ce que font certains schémas d’engagement (op-return, pay-to-contract, taproot script tree, etc.).

![RGB-Bitcoin](assets/fr/035.webp)

Le problème est de s’assurer qu’aucune autre partie de la transaction ne porte un second engagement non déclaré, et qu’on sache exactement lequel des inputs ou outputs véhicule le commitment. Plusieurs approches ont été tentées pour définir un champ déterministe dans lequel glisser la donnée :

![RGB-Bitcoin](assets/fr/038.webp)

***Sig tweak (sign-to-contract) :***

Un schéma anciennement proposé consistait à exploiter la partie aléatoire d’une signature (ECDSA ou Schnorr) pour y intégrer le _commitment_ : c’est la technique appelée "**sign to contract**". Vous remplacez le nonce généré au hasard par un hash contenant la donnée. Ainsi, la signature révèle implicitement votre engagement, sans espace additionnel dans la transaction. Cette approche présente des avantages :
- Pas de surcharge on-chain (vous utilisez la même place que le nonce de base).
- En théorie, cela peut être assez discret, car le nonce est initialement une donnée aléatoire.

Cependant, 2 inconvénients majeurs ont émergé :
- Les multisig avant Taproot : quand vous avez plusieurs signataires, il faut décider quelle signature porte le _commitment_. Les signatures peuvent être ordonnées différemment, et si un signataire refuse, vous perdez le contrôle sur l’aboutissement du _commitment_.
- MuSig et le nonce partagé : avec les multisig Schnorr (*MuSig*), la génération du nonce est un algorithme multipartite, et il devient pratiquement impossible de tweaker le nonce individuellement.

En pratique, **sig tweak** est donc peu compatible avec le matériel (hardware wallets) et les formats existants (Lightning, etc.). Cette belle idée est difficile à mettre en place concrètement.

***Key tweak (pay-to-contract) :***

Le **key tweak** reprend le concept historique de _pay-to-contract_. On prend la clé publique `X` et on la tweak en lui ajoutant la valeur `H(message)`. Concrètement, si `X = x * G` et `h = H(message)`, alors la nouvelle clé sera `X' = X + h * G`. Cette clé tweakée dissimule l’engagement sur le `message`. Le détenteur de la clé privée d’origine peut, en ajoutant `h` à sa clé privée `x`, prouver qu’il possède la clé permettant de dépenser la sortie. En théorie, c’est élégant, car :
- Le _commitment_ s’inscrit sans ajouter de champs supplémentaires.
- Vous ne stockez pas de données on-chain additionnelles.

Néanmoins, dans la pratique, on se heurte aux difficultés suivantes :
- Les wallets ne reconnaissent plus la clé publique standard, puisqu’elle a été “tweakée” ; ils ne peuvent donc pas facilement associer l’UTXO à votre clé habituelle.
- Les hardware wallets ne sont pas conçus pour signer avec une clé qui n’est pas issue de leur dérivation standard.
- Vous devez adapter vos scripts, descriptors, etc.

Dans le cadre de RGB, cette piste a été envisagée jusqu’en 2021, mais il s’est avéré trop compliqué de la faire fonctionner avec les standards et l’infrastructure actuelle.

***Witness tweak :***

Une autre idée, que certains protocoles comme les _inscriptions Ordinals_ ont concrétisée, est de placer les données directement dans la section `witness` de la transaction (d’où l’expression **"witness tweak"**). Cependant, cette méthode :
- Rend l’engagement immédiatement visible (vous collez littéralement des données brutes dans le witness).
- Peut être sujette à la censure (des mineurs ou nœuds peuvent refuser de relayer si c’est trop volumineux ou arbitraire).
- Consomme de l’espace dans les blocs, ce qui est contraire à l’objectif de discrétion et de légèreté de RGB.

En plus, le witness est conçu pour être prunable dans certains contextes, ce qui peut rendre plus compliqué le fait d'avoir des preuves robustes.

***Op-return (opret) :***

Historique et simple, un `OP_RETURN` permet de stocker un hash ou un message dans un champ spécial de la transaction. Mais c’est immédiatement détectable : tout le monde voit qu’il y a un _commitment_ dans la transaction, et cela peut être censuré ou écarté, en plus d’ajouter un output supplémentaire. Cela augmente également la transparence et la taille. C’est donc considéré comme moins satisfaisant dans l’optique d’une solution de _client-side validation_.

***Taproot (tapret) :***

La dernière option est l’utilisation de **Taproot** (introduit avec le BIP341), qui offre la possibilité de dissimuler un script (contenant le fameux _commitment_) dans l’arbre de Merkle d’une sortie Taproot. L’idée est que la clé interne est tweakée par la racine de Merkle globale de tous les scripts. Vous pouvez alors :
- Ajouter un petit script _op-return_ masqué dans l’arbre.
- Prouver off-chain qu’il existe réellement cette feuille (et qu’aucune autre ne contient un engagement concurrent), sans devoir révéler l’arbre entier.

![RGB-Bitcoin](assets/fr/036.webp)

C’est ce qui a été retenu pour RGB à partir de 2021, lorsque l’équipe est passée du _pay-to-contract_ classique au **Taproot commitment**. Il reste néanmoins un défi : prouver que cette insertion est unique dans l’arbre (pas de double engagement dans une autre feuille). On veut également éviter d’exposer à jamais toute la structure du script (politique de dépense, etc.).

Quatre algorithmes ont été testés pour gérer ce positionnement du _commitment_ dans l’arbre. Certains étaient trop complexes ou trop risqués pour être implémentés et audités sereinement. Un compromis plus simple a finalement été privilégié, qui reste “analysable” et fonctionnel.

RGB insère ainsi un script additionnel contenant un `OP_RETURN <commitment>` au sommet de l’arbre. Cependant, pour prouver que ce script est unique, on impose des règles quant à l’emplacement du *commitment* :
- Dans Taproot, l’emplacement _gauche_ ou _droite_ d’une branche est déterminé par l’ordre lexicographique des _hash_ de nœuds (BIP-341).
- Si le script du _commitment_ se retrouve du côté _gauche_, on peut prouver qu’il n’y a pas de script à droite en montrant un _hash_ vide ou un _hash_ aléatoire, etc.
- Si le script _commitment_ se place à droite, on doit révéler l’autre branche ou d’autres _hash_ frères pour montrer que ce n’est pas un second _commitment_.
- Pour limiter le risque d’être « forcé » du côté droit, on peut utiliser un petit _nonce_ (8 bits) pour rejouer le calcul et trouver un placement plus favorable.

![RGB-Bitcoin](assets/fr/037.webp)

Cela reste plus complexe qu’un simple “on place le hash dans l’arbre”. Mais c’est la seule façon d’empêcher que la dépense ultérieure d’un script BIP341 n’expose toute la structure d’origine ou ne permette un second engagement secret. Au final, l’équipe a trouvé un compromis gérable entre performance, discrétion, et auditabilité.

![RGB-Bitcoin](assets/fr/039.webp)

### Analyses et choix pratiques dans RGB

Quand nous avons démarré RGB, nous avons passé en revue toutes ces méthodes pour déterminer où et comment placer un _commitment_ dans une transaction de manière déterministe. Nous avons défini des critères :
- Compatibilité avec différents scénarios (par exemple, usages de multisig, de Lightning, de hardware wallets, etc.) ;
- Impact sur la place nécessaire on-chain ;
- Difficulté d’implémentation et de maintenance ;
- Confidentialité et résistance à la censure.


| Méthode                                             | Trace et taille on-chain | Taille côté client | Intégration des portefeuilles | Compatibilité matérielle | Compatibilité Lightning | Compatibilité Taproot |
| --------------------------------------------------- | ------------------------ | ------------------ | ----------------------------- | ------------------------ | ----------------------- | --------------------- |
| Keytweak (P2C déterministe)                         | 🟢                       | 🟡                 | 🔴                            | 🟠                       | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🟢 MuSig  |
| Sigtweak (S2C déterministe)                         | 🟢                       | 🟢                 | 🟠                            | 🔴                       | 🔴 BOLT, 🔴 Bifrost     | 🟠 Taproot, 🔴 MuSig  |
| Opret (OP_RETURN)                                   | 🔴                       | 🟢                 | 🟢                            | 🟠                       | 🔴 BOLT, 🟠 Bifrost     | -                     |
| Algorithme Tapret : noeud haut-gauche               | 🟠                       | 🔴                 | 🟠                            | 🟢                       | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |
| Algorithme Tapret #4 : n'importe quel nœud + preuve | 🟢                       | 🟠                 | 🟠                            | 🟢                       | 🔴 BOLT, 🟢 Bifrost     | 🟢 Taproot, 🟢 MuSig  |


| Schéma d’engagement déterministe                              | Standard       | Coût on-chain                                                                                                           | Taille de la preuve côté client                                                                                    |
| ------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Keytweak (P2C déterministe)                                   | LNPBP-1, 2     | 0 bytes                                                                                                                 | 33 bytes (clé non tweakée)                                                                                         |
| Sigtweak (S2C déterministe)                                   | WIP (LNPBP-39) | 0 bytes                                                                                                                 | 0 bytes                                                                                                            |
| Opret (OP_RETURN)                                             | -              | 36 (v)bytes (TxOut additionnel)                                                                                         | 0 bytes                                                                                                            |
| Algorithme Tapret : nœud haut-gauche                          | LNPBP-6        | 32 bytes dans le témoin (8 vbytes) sur n’importe quel multisig n-of-m et dépenses par chemin de script                  | 0 bytes sur les scriptless scripts taproot ~270 bytes dans un cas de script unique, ~128 bytes si plus d’un script |
| Algorithme Tapret #4 : n’importe quel nœud + preuve d’unicité | LNPBP-6        | 32 bytes dans le témoin (8 vbytes) pour les cas de script unique, 0 bytes dans le témoin dans la plupart des autres cas | 0 bytes sur les scriptless scripts taproot, 65 bytes jusqu’à ce que le Taptree ait une douzaine de scripts         |


| Layer                          | Coût on-chain (bytes/vbytes) | Coût on-chain (bytes/vbytes) | Coût on-chain (bytes/vbytes) | Coût on-chain (bytes/vbytes) | Coût on-chain (bytes/vbytes) | Coût côté client (bytes) | Coût côté client (bytes) | Coût côté client (bytes) | Coût côté client (bytes) | Coût côté client (bytes) |
| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| **Type**                       | **Tapret**                   | **Tapret #4**                | **Keytweak**                 | **Sigtweak**                 | **Opret**                    | **Tapret**               | **Tapret #4**            | **Keytweak**             | **Sigtweak**             | **Opret**                |
| Single-sig                     | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | 0?                       | 0                        |
| MuSig (n-of-n)                 | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | ? > 0                    | 0                        |
| Multi-sig 2-of-3               | 32/8                         | 32/8 ou 0                    | 0                            | n/a                          | 32                           | ~270                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 3-of-5               | 32/8                         | 32/8 ou 0                    | 0                            | n/a                          | 32                           | ~340                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 2-of-3 with timeouts | 32/8                         | 0                            | 0                            | n/a                          | 32                           | 64                       | 65                       | 32                       | n/a                      | 0                        |


| Layer                            | Coût on-chain (vbytes) | Coût on-chain (vbytes) | Coût on-chain (vbytes) | Coût côté client (bytes) | Coût côté client (bytes) |
| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |
| **Type**                         | **Base**               | **Tapret #2**          | **Tapret #4**          | **Tapret #2**            | **Tapret #4**            |
| MuSig (n-of-n)                   | 16.5                   | 0                      | 0                      | 0                        | 0                        |
| FROST (n-of-m)                   | ?                      | 0                      | 0                      | 0                        | 0                        |
| Multi_a (n-of-m)                 | 1+16n+8m               | 8                      | 8                      | 33 * m                   | 65                       |
| Branche MuSig / Multi_a (n-of-m) | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |
| Avec timeouts (n-of-m)           | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |

| Méthode                                   | Confidentialité et évolutivité | Interopérabilité | Compatibilité | Portabilité | Complexité |
| ----------------------------------------- | ------------------------------ | ---------------- | ------------- | ----------- | ---------- |
| Keytweak (P2C déterministe)               | 🟢                             | 🔴               | 🔴            | 🟡          | 🟡         |
| Sigtweak (S2C déterministe)               | 🟢                             | 🔴               | 🔴            | 🟢          | 🔴         |
| Opret (OP_RETURN)                         | 🔴                             | 🟠               | 🔴            | 🟢          | 🟢         |
| Algo Tapret : nœud haut-gauche            | 🟠                             | 🟢               | 🟢            | 🔴          | 🟠         |
| Algo Tapret #4 : Nœud quelconque + preuve | 🟢                             | 🟢               | 🟢            | 🟠          | 🔴         |


### Compatibilité avec Lightning et problèmes restants

Au fil de l’étude, il est apparu qu’aucun des schémas de commitments n’était pleinement compatible avec le standard LN actuel (qui n’emploie pas Taproot, ni _muSig2_, ni la prise en compte d’un _commitment_ supplémentaire). Des efforts sont en cours pour modifier la construction de canaux LN (*BiFrost*) et permettre d’insérer les engagements RGB. C’est un autre chantier où l’on doit revoir la structure de la transaction, les clés, et la façon dont sont signées les mises à jour de canaux.

L’analyse a montré qu’en effet, d’autres méthodes (key tweak, sig tweak, witness tweak, etc.) présentaient d’autres formes de complication :
- Soit on a un gros volume on-chain ;
- Soit on a une incompatibilité radicale avec le code existant des wallets. ;
- Soit la solution n’est pas viable en multisig non coopératif.

En fin de compte, **Taproot** demeure la plus prometteuse, même si elle réclame une mise à jour considérable de l’écosystème pour être prise en charge dans toutes les situations (Lightning, hardware wallets, etc.).

### Sharding appliqué aux contrats et rôle de l'Anchor

Nous avions déjà discuté du besoin de sharding dans le premier chapitre de la formation. L’idée est qu’un _anchor_ doit parfois contenir des engagements relatifs à plusieurs smart contracts différents. Comment construire un arbre de Merkle pour deux, cinq, ou deux cent mille contrats, tout en permettant à chacun de prouver uniquement l’engagement qui le concerne ?

![RGB-Bitcoin](assets/fr/041.webp)

#### Construire un arbre de Merkle pour plusieurs contrats

Je vous propose un exemple avec un seul contrat, ayant un _contract ID_ de 256 bits (un hash de la _genesis_). On sélectionne une profondeur minimale de l’arbre, mettons `8`, ce qui procure 2^8 = 256 feuilles. On place l’engagement dans la feuille correspondant à `contract_id mod 256`. Dès lors :
- Le détenteur du contrat peut produire un _Merkle path_ menant à cette position.
- Le validateur sait que le contract ID ne peut être associé qu’à cette unique feuille, vu que la profondeur est fixée et que la division modulaire impose un placement déterministe.

Pour plusieurs contrats (ex. USDT, USDC, NFT), vous calculez cette position pour chacun, vérifiez qu’il n’y a pas collision, et construisez l’arbre en conséquence. S’il existe une collision, vous pouvez augmenter la largeur (ou ajuster un cofacteur, un _nonce_) pour obtenir un placement adéquat. Ceci reste hors consensus : vous êtes libre de la largeur d’arbre tant que la preuve finale est cohérente.

#### Preuve côté client et structure MPC

Sur le client, on ne stocke jamais l’ensemble du Merkle tree. On se contente de générer, à l’instant T, un _Merkle path_ pour chaque contrat concerné, à transmettre au destinataire (qui pourra ainsi valider l’engagement). Dans certains cas, vous possédez plusieurs actifs passés par le même UTXO. Vous pouvez alors fusionner plusieurs _Merkle paths_ dans ce qu’on appelle un _multi-protocol commitment block_, afin d'éviter de dupliquer trop de données.

![RGB-Bitcoin](assets/fr/042.webp)

Dans la base de code (répertoire _client-side validation_, module `commit-verify::mpc`), on retrouve notamment :
- Des structures d'arbres de Merkle paramétrables (profondeur `depth`, entropie, cofacteur, etc.).
- Un type de **Merkle proof** qui stocke la position ciblée dans l’arbre et la suite de hachages frères menant à la racine.

![RGB-Bitcoin](assets/fr/044.webp)

Chaque _Merkle proof_ est donc légère, d’autant plus que la profondeur de l’arbre n’excédera pas 32 dans RGB. Il existe également une notion de **Merkle block**, conservant plus d’informations (la cross-section, l’entropie, etc.), utile pour combiner ou séparer plusieurs branches.

Voilà pourquoi la finalisation de RGB a demandé du temps. On avait la vision globale dès 2019 : tout mettre en client-side, faire circuler les tokens hors chaîne. Mais des détails comme le sharding pour plusieurs contrats, la structure Merkle, la manière de gérer les collisions et la fusion de preuves… tout cela a exigé des itérations.

### Les anchors : un assemblage global

Il reste un dernier élément fondamental : **les anchors**, qui combinent d’une part les _deterministic Bitcoin commitments_ (inclus dans la transaction) et d’autre part les _multi-protocol commitments_ (Merkle tree) :
- L’**anchor** comporte l’ID de la transaction de dépense (witness transaction), car retrouver on-chain la transaction exacte dépensant un outpoint peut être coûteux.
- Il inclut la preuve _multi-protocol commitment_ (un _Merkle path_ vers la bonne feuille).
- Il inclut aussi la preuve _deterministic Bitcoin commitment_ (comme par exemple : Tapret, key tweak, op-return, etc.), afin de montrer précisément où se situe l’engagement dans la transaction Bitcoin et comment vérifier l’absence d’engagement concurrent.

Ainsi, côté client, vous avez tous les éléments pour reconstruire la logique : "J’ai dépensé tel outpoint, ancré mon état dans tel script Taproot, la racine Merkle englobant plusieurs contrats, et la feuille correspondant à mon contrat s’obtient via tel chemin."

On a ainsi deux modes dans RGB :
- Soit on emploie `OpRet` (op-return) pour la compatibilité avec l’historique (mais ce n’est pas recommandé),
- Soit on utilise la version **Tapret** qui est plus complexe.

L’anchor Tapret requiert notamment :
- La clé publique interne (pour prouver comment la racine de Merkle tweak la clé)
- Un **nonce** si nécessaire (pour tenter de forcer le script sur la gauche de l’arbre)
- Les informations prouvant que le nœud adjacent n’est pas un autre engagement, mais seulement un script ou un hash quelconque inoffensif.

![RGB-Bitcoin](assets/fr/045.webp)

### Conclusion

Nous avons couvert :
- Comment appliquer le concept de _single-use seals_ dans Bitcoin (en particulier via un _outpoint_).
- Les différentes méthodes pour insérer de façon déterministe un _commitment_ dans une transaction (Sig tweak, Key tweak, witness tweak, op_return, Taproot/Tapret).
- Les raisons pour lesquelles RGB se concentre sur les engagements Taproot.
- La gestion multi-contrat via des _multi-protocol commitments_, indispensable pour ne pas exposer l’intégralité d’un état ou d’autres contrats lorsqu’on veut prouver un point précis.

Nous avons aussi vu l’importance des _anchors_, qui rassemblent tout (le _TXID_ de la transaction, la preuve de l’arbre de Merkle, la preuve Taproot...) dans un même ensemble.

En pratique, la mise en œuvre technique est répartie entre plusieurs _crates_ Rust dédiés (dans _client_side_validation_, _commit-verify_, _bp_core_, etc.). Les notions fondamentales sont là :

![RGB-Bitcoin](assets/fr/046.webp)

Dans les chapitres suivants, nous approfondirons la manière dont on bâtit concrètement un smart contract RGB en assemblant ces briques : comment on encode la logique du contrat, comment on transfère des jetons ou des droits, et comment on tire parti de la modularité offerte par Taproot et les multi-productal commitments pour faire coexister de nombreux contrats ou fonctionnalités au sein d’une seule transaction Bitcoin. Nous verrons aussi les problématiques spécifiques liées à Lightning, et la proposition **Bifrost** pour rendre compatibles les canaux LN avec le protocole RGB et son mécanisme d’ancrage avancé.


## Explication de l'état RGB
<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

![video](https://youtu.be/tmAVdyXGmj4)

## Logique métier RGB
<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

![video](https://youtu.be/lUTjeuM0oTA)


## Glossaire RGB
<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

En cas de besoin dans la formation, vous pouvez revenir sur ce petit glossaire des termes techniques importants employés dans l'univers RGB (classés par ordre alphabétique).

#### Anchor

Un **Anchor** représente un ensemble de données côté client (client-side data) permettant de prouver l’inclusion d’un _commitment_ unique dans une transaction. Dans le protocole RGB, un Anchor est constitué des éléments suivants :

- L’identifiant de la transaction Bitcoin (le **Transaction ID** ou _txid_) de la **witness transaction**.
- Le **Multi Protocol Commitment (MPC)**.
- Le **Deterministic Bitcoin Commitment (DBC)**.
- L’**Extra Transaction Proof (ETP)** si l’on emploie le mécanisme de commitment **Tapret** (voir la section dédiée à ce schéma).

Un Anchor sert donc à établir un lien vérifiable entre une transaction Bitcoin précise et des données privées validées par le protocole RGB. Il garantit que ces données sont bel et bien incluses (committed) dans la blockchain, sans pour autant que leur contenu exact soit exposé publiquement.

#### AluVM

L’abréviation **AluVM** désigne "_Algorithmic logic unit Virtual Machine_", une machine virtuelle à registres, conçue pour la validation de smart contracts et le calcul distribué. Elle est utilisée (sans y être exclusivement réservée) dans le cadre de la validation des contrats RGB. Les scripts ou les opérations inscrites dans un contrat RGB peuvent ainsi être exécutés dans l’environnement AluVM.  
Pour plus d’informations : [Site officiel d’AluVM](https://www.aluvm.org/)

### Assignment

Dans la logique d’RGB, un **Assignment** est l’équivalent d’une “sortie de transaction” (output) qui modifie, met à jour ou crée certaines propriétés au sein de l’état d’un **contract**. Un Assignment comporte deux éléments :

1. Une **Seal Definition** (la référence à un UTXO précis).
2. Un **Owned State** (les données décrivant l’état associé à ce nouveau détenteur).

Un Assignment indique donc qu’une portion de l’état (ex. un actif) est désormais allouée à un détenteur particulier, identifié via un _seal_ lié à un UTXO.

### Business Logic

La **Business Logic** regroupe l’ensemble des règles et opérations internes d’un contrat, décrites par son **Schema** (c’est-à-dire la structure même du contrat). Elle dicte la manière dont l’état du contrat peut évoluer et sous quelles conditions. Dans RGB, cette logique spécifie quels types de transitions (State Transitions) sont autorisés, comment elles doivent être validées et quels droits sont conférés à chaque participant.

### Client-side Validation

La **Client-side Validation** renvoie au processus par lequel chaque partie (client) vérifie un ensemble de données échangées en privé, selon les règles d’un protocole. Dans le cas d’RGB, ces données échangées sont regroupées dans ce qu’on appelle des **consignments**. Contrairement au protocole Bitcoin qui exige que toutes les transactions soient publiées on-chain, RGB permet de ne stocker en public que des _commitments_ (ancrés dans Bitcoin), tandis que l’essentiel des informations de contrat (transitions, attestations, preuves) reste off-chain, partagées seulement entre les utilisateurs concernés.

### Commitment

Un **Commitment** (au sens cryptographique) est un objet mathématique, noté CC, dérivé de façon déterministe à partir d’une opération sur une donnée structurée mm (le message) et d’une valeur aléatoire rr. On écrit souvent C=commit(m,r)C = \text{commit}(m, r).  
Ce mécanisme comprend deux opérations principales :

1. **Commit** : on applique une fonction cryptographique à un message mm et à un aléa rr pour produire CC.
2. **Verify** : on utilise CC, le message mm et la valeur rr pour vérifier que ce commitment est correct. La fonction renvoie Vrai ou Faux (True/False).

Un commitment doit respecter deux propriétés :

- **Binding** : il doit être impossible (ou computativement infaisable) de trouver deux messages différents (m,r)(m, r) et (m′,r′)(m', r') produisant le même CC.
- **Hiding** : la connaissance de CC ne doit pas révéler le contenu de mm.

Dans le protocole RGB, un commitment est souvent inclus dans une transaction Bitcoin afin de prouver l’existence d’une certaine information à un instant donné, sans dévoiler cette information elle-même.

### Consignment

Un **Consignment** regroupe les données échangées entre les parties, soumises à la Client-side Validation dans RGB. Il existe deux grandes catégories de consignments :

- **Contract Consignment** : fourni par l’**issuer** (émetteur du contrat), il comprend les informations d’initialisation telles que le **Schema**, la **Genesis**, l’**Interface** et l’**Interface Implementation**.
- **Transfer Consignment** : fourni par la partie qui paie (payer). Il contient tout l’historique de transitions d’état aboutissant au **terminal consignment** (c’est-à-dire l’état final reçu par le payeur).

Ces consignments ne sont pas enregistrés publiquement dans la blockchain ; ils sont échangés directement, ou via un mécanisme privé, entre les parties concernées.

### Contract

Un **Contract** désigne un ensemble de **droits** (Contract Rights) exécutés numériquement entre plusieurs acteurs via le protocole RGB. Il possède un état actif (Active State) et une logique d’affaires (Business Logic), définie par un **Schema**, qui précise quelles opérations sont autorisées (transferts, extensions, etc.).  
L’état d’un contrat, ainsi que les règles de validité, s’expriment dans le **Schema**. À tout moment, le contrat n’évolue que conformément à ce qui est permis par ce Schema et par les scripts de validation (exécutés, par exemple, dans AluVM).

### Contract Operation

Une **Contract Operation** est une mise à jour de l’état du contrat effectuée selon les règles du **Schema**. Les opérations suivantes existent dans RGB :

- **State Transition**
- **Genesis**
- **State Extension**

Chaque opération modifie l’état en y ajoutant ou en y remplaçant certaines données (Global State, Owned State…).

### Contract Participant

Un **Contract Participant** est un acteur prenant part aux opérations relatives au contrat. Dans RGB, on distingue :

- L’**issuer** du contrat, qui crée la **Genesis** (l’origine du contrat).
- Les **contract parties**, c’est-à-dire les détenteurs de droits (Ownership rights) sur l’état du contrat.
- Les **public parties**, acteurs pouvant construire des **State Extensions** si le contrat propose des _Valencies_ accessibles au public.

### Contract Rights

Les **Contract Rights** désignent les différents droits que peuvent exercer les acteurs d’un contrat RGB. Ils se classent en plusieurs catégories :

- Les **ownership rights**, associés à la détention d’un UTXO particulier (via un _Seal Definition_).
- Les **executive rights**, c’est-à-dire la capacité de construire une ou plusieurs transitions (State Transitions) conformes au **Schema**.
- Les **public rights**, lorsque le Schema autorise certains usages publics, par exemple la création d’une **State Extension** via la rédemption d’une Valency.

### Contract State

Le **Contract State** correspond à l’état courant d’un contrat à un instant donné. Il peut être constitué de données à la fois publiques et privées, reflétant la situation du contrat. Dans RGB, on distingue :

- Le **Global State**, qui comprend les propriétés publiques du contrat (mises en place dès la Genesis ou ajoutées via des mises à jour autorisées).
- Les **Owned States**, qui appartiennent à des détenteurs précis, identifiés par leurs UTXOs.

### Deterministic Bitcoin Commitment - DBC

Le **Deterministic Bitcoin Commitment (DBC)** est l’ensemble de règles permettant d’inscrire de manière prouvable et unique un _commitment_ dans une transaction Bitcoin. Dans le protocole RGB, il existe deux formes principales de DBC :

- **Opret**
- **Tapret**

Ces mécanismes définissent précisément comment le _commitment_ est encodé dans les sorties ou dans la structure d’une transaction Bitcoin, afin de s’assurer que cet engagement est repérable et vérifiable de façon déterministe.

### Directed Acyclic Graph - DAG

Un **DAG** (ou Graphe Orienté Acyclique) est un graphe sans cycle, permettant un ordonnancement topologique. Les blockchains, tout comme les _shards_ de contrats RGB, peuvent être représentés par des DAGs.  
(Plus d’informations : [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph))

### Engraving

Un **Engraving** est une chaîne de données optionnelle que les détenteurs successifs d’un contrat peuvent inscrire dans l’historique du contrat. Cette fonctionnalité existe, par exemple, dans l’interface **RGB21** et permet d’ajouter des informations “commémoratives” ou descriptives dans l’historique du contrat.

### Extra Transaction Proof - ETP

L’**ETP** (Extra Transaction Proof) est la partie de l’**Anchor** qui renferme les données supplémentaires nécessaires à la validation d’un commitment de type **Tapret** (dans un contexte _taproot_). Elle comprend, entre autres, la clé publique interne du script taproot (_internal PubKey_) et les informations spécifiques au _Script Path Spend_.

### Genesis

La **Genesis** désigne l’ensemble des données, régies par un **Schema**, qui forment l’état initial de tout contrat dans RGB. On peut la rapprocher du concept de _Genesis Block_ (le bloc originel) en Bitcoin, mais ici au niveau _client-side_.  
(Plus d’informations : [Genesis dans la documentation RGB](https://chatgpt.com/rgb-state-and-operations/state-transitions.md#genesis))

### Interface

L’**Interface** est l’ensemble des instructions qui permettent de décoder les données binaires compilées dans un **Schema** ou dans des opérations de contrat (Contract Operations) et leurs états, afin de les rendre lisibles pour l’utilisateur ou son wallet. Elle agit comme une couche d’interprétation.

### Interface Implementation

L’**Interface Implementation** est l’ensemble de déclarations qui relient une **Interface** à un **Schema**. Elle rend possible la “traduction” sémantique opérée par l’Interface elle-même, afin que les données brutes d’un contrat soient compréhensibles par l’utilisateur ou les logiciels impliqués.

### Invoice

Une **Invoice** prend la forme d’une URL encodée en [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), qui embarque les données nécessaires à la construction d’une **State Transition** (par le payeur). En d’autres termes, c’est une facture permettant à la contrepartie (payer) de créer la transition correspondante pour transférer l’actif ou mettre à jour l’état du contrat.

### Global State

Le **Global State** est l’ensemble des propriétés publiques contenues dans l’état d’un contrat (Contract State). Il est défini lors de la **Genesis** et peut être, selon les règles du contrat, mis à jour par des transitions autorisées. Contrairement aux Owned States, le Global State n’appartient pas à une entité particulière ; il est plus proche d’un registre public dans le cadre du contrat.

### Lightning Network

Le **Lightning Network** est un réseau décentralisé de _payment channels_ (ou _state channels_) Bitcoin, constitué de portefeuilles multi-signatures 2-of-2. Il autorise des transactions _off-chain_ rapides et peu coûteuses, tout en s’appuyant sur la couche 1 de Bitcoin pour l’arbitrage (ou la fermeture) lorsque nécessaire.  
(Plus d’informations : [Lightning Network](https://lightning.network/))

### Multi Protocol Commitment - MPC

Le **Multi Protocol Commitment (MPC)** désigne la structure de Merkle Tree utilisée dans RGB pour inclure, au sein d’une unique transaction Bitcoin, plusieurs **Transition Bundles** issus de contrats différents. L’idée est de regrouper plusieurs engagements (correspondant potentiellement à différents contrats ou différents actifs) dans un seul point d’ancrage afin d’optimiser l’occupation de l’espace de bloc.  
(Plus d’informations : [MPC](https://chatgpt.com/c/commitment-layer/multi-protocol-commitments-mpc.md))

### Owned State

Un **Owned State** est la partie de l’état d’un contrat (Contract State) qui est enfermée dans un **Assignment** et associée à un détenteur particulier (via un _seal_ pointant vers un UTXO). Cela représente, par exemple, un actif numérique ou un droit contractuel spécifique attribué à cette personne.

### Ownership

Le terme **Ownership** renvoie à la capacité de contrôler et de “dépenser” un UTXO référencé par une **Seal Definition**. Lorsqu’un Owned State est lié à un UTXO, le propriétaire de cet UTXO a le droit, potentiellement, de transférer ou de faire évoluer l’état associé, selon les règles du contrat.

### Partially Signed Bitcoin Transaction - PSBT

Une **PSBT** (_Partially Signed Bitcoin Transaction_) est une transaction Bitcoin qui n’est pas encore complètement signée. Elle peut être partagée entre plusieurs entités, chacune pouvant y ajouter ou y vérifier certains éléments (signatures, scripts…), jusqu’à ce que la transaction soit jugée prête pour la diffusion on-chain.  
(Plus d’informations : [BIP-0174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki))

### Pedersen commitment

Un **Pedersen commitment** est un type de _commitment_ cryptographique présentant la propriété d’être **homomorphique** vis-à-vis de l’opération d’addition. Cela signifie qu’il est possible de valider la somme de deux engagements sans dévoiler les valeurs individuelles. Formellement, si

$$
C1=commit(m1,r1)etC2=commit(m2,r2),C_1 = \text{commit}(m_1, r_1) \quad \text{et} \quad C_2 = \text{commit}(m_2, r_2)
$$

alors

$$
C3=C1⋅C2=commit(m1+m2, r1+r2).C_3 = C_1 \cdot C_2 = \text{commit}(m_1 + m_2, \, r_1 + r_2)
$$

Cette propriété devient utile, par exemple, pour dissimuler les montants de tokens échangés tout en pouvant vérifier les totaux.  
(Plus d’informations : [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9))

### Redeem

Dans une **State Extension**, un **Redeem** fait référence à l’action de récupérer (ou d’exploiter) une **Valency** précédemment déclarée. Une Valency étant un droit public, le Redeem permet à un participant autorisé de “réclamer” une extension spécifique de l’état du contrat.

### Schema

Un **Schema** dans RGB est un morceau de code déclaratif décrivant l’ensemble des variables, règles et logiques d’affaires (Business Logic) qui régissent le fonctionnement d’un contrat. Le Schema définit la structure de l’état, les types de transitions autorisées et les conditions de validation.

### Seal Definition

La **Seal Definition** est la partie d’un **Assignment** qui associe le _commitment_ à un UTXO possédé par le nouveau détenteur. Elle indique, en d’autres termes, “où” se trouve l’état (dans quel UTXO) et permet d’établir la propriété d’un actif ou d’un droit.  
(Plus d’informations : [Seal Definition](https://chatgpt.com/rgb-state-and-operations/components-of-a-contract-operation.md#seal-definition))

### Shard

Un **Shard** représente une branche dans le DAG de l’historique des **State Transitions** d’un contrat RGB. Autrement dit, c’est un sous-ensemble cohérent de l’historique global du contrat, correspondant par exemple à la séquence de transitions nécessaires pour prouver la validité d’un actif donné depuis la _Genesis_.

### Single-Use Seal

Un **Single-Use Seal** est une promesse de _commit_ (engagement cryptographique) sur un message encore inconnu, qui sera révélé une seule fois à l’avenir et qui doit être connu de tous les membres d’une audience spécifique. L’objectif est d’empêcher la création de multiples engagements concurrents pour le même sceau.  
(Plus d’informations : [Single-Use Seal](https://chatgpt.com/distributed-computing-concepts/single-use-seals.md))

### Stash

Le **Stash** est l’ensemble des données côté client (client-side data) qu’un utilisateur stocke pour un ou plusieurs contrats RGB, afin de procéder à la validation (Client-side Validation). Cela inclut l’historique des transitions, les consignments, les preuves de validité, etc. Chaque détenteur ne conserve que les parties de l’historique dont il a besoin (shards).

### State Extension

Une **State Extension** est une opération de contrat permettant de redéclencher des mises à jour de l’état via la rédemption de **Valencies** préalablement déclarées. Pour être effective, une State Extension doit ensuite être refermée par une **State Transition** (qui actualise l’état final du contrat).  
(Plus d’informations : [State Extensions](https://chatgpt.com/rgb-state-and-operations/state-transitions.md#state-extensions))

### State Transition

La **State Transition** est l’opération centrale qui fait évoluer l’état d’un contrat RGB vers un nouvel état. Elle peut modifier les données du **Global State** et/ou les **Owned States**. Dans la pratique, chaque transition est vérifiée par les règles du **Schema** et ancrée dans la blockchain Bitcoin via un _commitment_.  
(Plus d’informations : [State Transitions](https://chatgpt.com/rgb-state-and-operations/state-transitions.md#state-transitions-and-their-mechanics))

### Taproot

Le terme **Taproot** fait référence au format de transactions Segwit v1 de Bitcoin, introduit par [BIP341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) et [BIP342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot permet d’améliorer la confidentialité et la flexibilité des scripts, notamment en rendant les transactions plus compactes et plus difficiles à distinguer les unes des autres.

### Terminal Consignment - Consignment Endpoint

Le **Terminal Consignment** (ou _Consignment Endpoint_) est un **transfer consignment** comprenant l’état final du contrat qui intègre la **State Transition** créée à partir de l’**Invoice** du destinataire (payee). Il s’agit donc du point d’aboutissement d’un transfert, avec les données nécessaires pour prouver que la propriété ou l’état a bien été transmis.

### Transition Bundle

Un **Transition Bundle** est un ensemble de **State Transitions** RGB (appartenant au même contrat) qui sont tous engagés dans la même **witness transaction** Bitcoin. Cela permet de regrouper plusieurs mises à jour ou transferts en un seul ancrage on-chain.  
(Plus d’informations : [Transition Bundle](https://chatgpt.com/rgb-state-and-operations/state-transitions.md#transition-bundle))

### UTXO

Un **UTXO** (Unspent Transaction Output) Bitcoin est défini par le hachage d’une transaction et l’index de la sortie (vout). On l’appelle aussi parfois un _outpoint_. Dans le protocole RGB, la référence à un UTXO (via une Seal Definition) permet de localiser l’Owned State, c’est-à-dire la propriété détenue sur la blockchain.

### Valency

Une **Valency** est un droit public ne nécessitant pas de stockage d’état en tant que tel, mais qui peut être racheté (Redeem) via une **State Extension**. Il s’agit donc d’une forme de possibilité ouverte à tous (ou à certains acteurs), déclarée dans la logique du contrat, afin d’effectuer ultérieurement une extension particulière.

### Witness Transaction

La **Witness Transaction** est la transaction Bitcoin qui ferme le _seal_ autour d’un message contenant un **Multi Protocol Commitment (MPC)**. Cette transaction dépense un UTXO ou en crée un, de façon à sceller (close) l’engagement lié au protocole RGB. Elle fait office de preuve on-chain que l’état a été “fixé” à un instant précis.


# Programmation sur RGB
<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## Bases de la programmation RGB
<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

![video](https://youtu.be/Uo1UoxiImsI)

## Programmation RGB Partie 2
<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

![video](https://youtu.be/sVoKIi-1XbY)

## Rédaction de contrats intelligents
<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

![video](https://youtu.be/GRwS-NvWF3I)

## Sujets avancés RGB et discussions futures
<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

![video](https://youtu.be/mqCupTlDbA0)

# Construire sur RGB
<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## Bitmask
<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

![video](https://youtu.be/nbUtV8GOR_U)

## Noeud RGB partie 1 
<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

![vidéo](https://youtu.be/5iAhsgCSL3U)

## Noeud RGB partie 2
<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

![vidéo](https://youtu.be/piQQH4Q2nr0)


# Conclusion 
<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>



## Évaluez ce cours
<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>
<isCourseReview>true</isCourseReview>

## Mot de clôture
<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

Merci d'avoir participé aux cours RGB proposés par Plan ₿ Network en collaboration avec Fulgur'Ventures. Nous exprimons notre gratitude à nos enseignants pour leur soutien. Si vous êtes intéressé à poursuivre votre travail avec RGB, voici une liste utile de ressources à explorer :

- https://rgb.tech/
- https://www.rgbfaq.com/
- https://rgb.tech/docs/
- https://www.youtube.com/LNP-BP
- https://twitter.com/lnp_bp

Merci et bonne chance pour vos études chez Plan ₿ Network.
