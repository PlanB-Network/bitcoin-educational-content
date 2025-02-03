---
name: Le protocole RGB, de la théorie à la pratique
goal: Acquérir les compétences nécessaires pour comprendre et utiliser RGB
objectives:
  - Comprendre les concepts fondamentaux du protocole RGB
  - Maîtriser les principes de la validation côté client et des engagements sur Bitcoin
  - Apprendre à créer, gérer et transférer des contrats RGB
  - Savoir opérer un noeud Lightning compatible avec RGB
---

# À la découverte du protocole RGB

Plongez dans l’univers de RGB, un protocole conçu pour appliquer et faire respecter des droits numériques, sous forme de contrats et d’actifs, en s’appuyant sur les règles de consensus et les opérations de la blockchain Bitcoin. Cette formation complète vous guide à travers les fondations techniques et pratiques de RGB, depuis les concepts de la "Client-side Validation" et des "Single-use Seals", jusqu'à l'implémentation de contrats intelligents avancés.

À travers un programme structuré et progressif, vous découvrirez les mécanismes de la validation côté client, les engagements déterministes sur Bitcoin et les schémas d’interaction entre les utilisateurs. Apprenez à créer, gérer et transférer des tokens RGB sur Bitcoin ou bien sur le Lightning Network.

Que vous soyez développeur, passionné de Bitcoin, ou simplement curieux d’en apprendre davantage sur cette technologie, cette formation vous fournira les outils et les connaissances nécessaires pour maîtriser RGB et construire des solutions innovantes sur Bitcoin.

Le cours est issu d'un séminaire en direct organisé par Fulgur'Ventures et enseigné par trois enseignants renommés et experts de RGB.

+++

# Introduction
<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Présentation du cours
<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Bonjour à tous et bienvenue dans cette formation dédiée à RGB, un système de contrats intelligents validés côté client, fonctionnant sur Bitcoin et le Lightning Network. La structure de cette formation est pensée pour permettre une exploration approfondie de ce sujet complexe. Voici comment la formation est organisée :

**Section 1 : Théorie**  

La première section est dédiée aux concepts théoriques nécessaires pour comprendre les principes fondamentaux de la validation côté client et de RGB. Comme vous le découvrirez dans cette formation, RGB introduit une multitude de concepts techniques que l'on n'a pas l'habitude de voir sur Bitcoin. Vous trouverez donc également dans cette section un glossaire fournissant des définitions pour tous les termes spécifiques au protocole RGB.

**Section 2 : Pratique**  

La deuxième section portera sur l'application des concepts théoriques vus dans la section 1. Nous apprendrons à créer et manipuler des contrats RGB. Nous allons également voir comment programmer avec ces outils. Ces deux premières sections sont présentées par Maxim Orlovsky.

**Section 3 : Applications**  

La dernière section est animée par d'autres intervenants qui présentent des applications concrètes basées sur RGB, afin de mettre en lumière des cas d'utilisation réels.

---

Cette formation est initialement issue d'un bootcamp de développement avancé de deux semaines à Viareggio, en Toscane, organisé par [Fulgur'Ventures](https://fulgur.ventures/). La première semaine, centrée sur Rust et les SDK, peut être retrouvée dans cet autre cours :

https://planb.network/courses/lnp402

Dans ce cours, nous nous concentrons sur la deuxième semaine du bootcamp, qui porte sur RGB.

**Semaine 1 - LNP402 :**

![RGB-Bitcoin](assets/fr/001.webp)

**Semaine 2 - Formation actuelle CSV402 :**

![RGB-Bitcoin](assets/fr/002.webp)

Un grand merci aux organisateurs de ces cours en direct et aux 3 enseignants qui y ont participé :
- Maxim Orlovsky : *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, IA, robotique, transhumanisme. Créateur de RGB, Prime, Radiant et lnp_bp, mycitadel_io & cyphernet_io* ;
- Hunter Trujilo : *Développeur, Rust, Bitcoin, Lightning, RGB* ;
- Federico Tenga : *Je fais ma part pour que le monde devienne une dystopie cypherpunk. Actuellement en train de travailler sur RGB chez Bitfinex*.

La version écrite de cette formation a été rédigée en s'appuyant sur 2 ressources principales :
- Les vidéos du séminaire de Maxim Orlovsky, Hunter Trujilo et Frederico Tenga lors du Lightning Bootcamp ;
- La documentation de RGB, dont la production a été sponsorisée par [Bitfinex](https://www.bitfinex.com/).

# RGB en théorie
<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Introduction aux concepts de l'informatique distribuée
<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

![video](https://youtu.be/AF2XbifPGXM)


RGB est un protocole conçu pour appliquer et faire respecter des droits numériques (sous forme de contrats et d’actifs) de manière évolutive et confidentielle, en s’appuyant sur les règles de consensus et les opérations de la blockchain Bitcoin. L’objectif de ce premier chapitre est de présenter les concepts et la terminologie de base autour du protocole RGB, en soulignant notamment ses liens étroits avec des concepts de base de l’informatique distribuée tels que la Client-side Validation et les Single-use Seals.

Dans ce chapitre, nous explorons les fondements des **systèmes de consensus distribué** et nous verrons comment RGB s’intègre dans cette famille de technologies. Nous introduirons également les grands principes qui permettent de comprendre pourquoi RGB se veut, d’une part, extensible, et d’autre part, indépendant du mécanisme de consensus propre à Bitcoin, tout en s’appuyant sur lui lorsqu’il le faut.

### Introduction

L’informatique distribuée (_Distributed Computing_), une branche spécifique de l’informatique, étudie les protocoles permettant de faire circuler et de traiter des informations sur un réseau de nœuds. L’ensemble de ces nœuds et des règles du protocole constitue ce qu’on appelle un système distribué. Parmi les propriétés essentielles qui caractérisent un tel système, on retrouve :
- La **capacité de vérification et de validation indépendante** de certaines données par chaque nœud ;
- La possibilité pour les nœuds de construire (selon le protocole) une vue complète ou partielle de l’information. Ces vues sont les **états** du système distribué ;
- L’**ordre chronologique** des opérations, afin que les données soient horodatées de manière fiable et qu’il existe un consensus sur la séquence d’événements (séquence d’états).

En particulier, la notion de **consensus** dans un système distribué recouvre deux aspects :
- La **reconnaissance de la validité** des changements d’état (selon les règles du protocole) ;
- L’**accord sur l’ordre** de ces changements d’état, ce qui rend impossible la réécriture ou l’inversion a posteriori des opérations validées (c’est ce que l'on appelle également dans le cadre de Bitcoin, la "protection contre la double-dépense").

La première implémentation sans permission et fonctionnelle d’un mécanisme de consensus distribué a été introduite par Satoshi Nakamoto avec Bitcoin, grâce à l’utilisation conjointe d’une structure de données en blockchain et d’un algorithme de Proof-of-Work (PoW). Dans ce système, la crédibilité de l’historique des blocs dépend de la puissance de calcul que les nœuds (mineurs) y consacrent. Bitcoin est donc un exemple historique et majeur de système de consensus distribué ouvert à tous (*permissionless*).

Dans l'univers de la blockchain et de l'informatique distribuée, nous pouvons distinguer deux paradigmes fondamentaux : la ***blockchain*** au sens traditionnel, et les ***state channels*** (canaux d'état), dont le meilleur exemple en production est le Lightning Network. La blockchain se définit comme un registre d'événements ordonnés chronologiquement, répliqué par consensus au sein d'un réseau ouvert et sans permission. Les state channels, eux, sont des canaux en pair-à-pair qui permettent à deux (ou plusieurs) participants de maintenir un état mis à jour off-chain, ne recourant à la blockchain qu'au moment de l'ouverture et de la fermeture de ces canaux.

Dans le cadre de Bitcoin, vous connaissez sans doute les principes du minage, de la décentralisation et de la finalité des transactions sur la blockchain, ainsi que le fonctionnement des canaux de paiement. Avec RGB, nous allons introduire un nouveau paradigme appelé **Client-side Validation** (validation côté client), qui, contrairement à la blockchain ou à Lightning, consiste à conserver et à valider localement (côté client) les transitions d'état d'un contrat intelligent. Ceci se différencie aussi d'autres techniques de la "DeFi" (_rollups_, _plasma_, _ARK_, etc.), dans la mesure où la Client-side Validation s'appuie sur la blockchain pour empêcher la double dépense et pour avoir un système d'horodatage, tout en conservant le registre des états et des transitions off-chain, uniquement chez les participants concernés.

![RGB-Bitcoin](assets/fr/003.webp)

Nous allons également plus tard introduire un terme important : la notion de "**stash**", qui désigne l'ensemble des données côté client nécessaires pour préserver l'état d'un contrat, ces données n'étant pas répliquées de façon globale sur le réseau. Enfin, nous aborderons la raison d'être de RGB, un protocole qui tire parti de la Client-side Validation, et pourquoi il se révèle complémentaire aux approches existantes (blockchain et state channels).

### Les trilemmes en informatique distribuée

Pour comprendre en quoi la Client-side Validation et RGB répondent à des problématiques non résolues par la blockchain et Lightning, découvrons 3 "trilemmes" majeurs en informatique distribuée :

- **Scalabilité, Décentralisation, Privacy** ;
- **Théorème CAP** (Cohérence, Disponibilité, tolérance aux Partitions) ;
- **Trilemme CIA** (Confidentialité, Intégrité, Disponibilité).

#### 1. Scalabilité, décentralisation et confidentialité

- **Blockchain (Bitcoin)**

La blockchain est très décentralisée, mais peu scalable. De plus, comme tout se trouve dans un registre global et public, la confidentialité est limitée. On peut tenter d'améliorer la confidentialité avec des technologies zero-knowledge (transactions confidentielles, schémas mimblewimble, etc.), mais la chaîne publique ne peut pas cacher le graphe des transactions.

- **Lightning/State channels**

Les canaux d'état (comme avec le Lightning Network) sont plus scalables et plus privés que la blockchain, car les transactions s'effectuent off-chain. Toutefois, l'obligation d'annoncer publiquement certains éléments (transactions de financement, topologie du réseau) et la surveillance du trafic réseau peuvent compromettre en partie la confidentialité. Aussi, la décentralisation en pâtit : le routage requiert une grande quantité de liquidités et les nœuds majeurs peuvent devenir des points de centralisation. C'est justement un phénomène que l'on peut commencer à observer actuellement sur Lightning.

- **Client-side Validation (RGB)**

Ce nouveau paradigme est encore plus scalable et plus confidentiel, car non seulement on peut intégrer des techniques de preuves à divulgation nulle de connaissance, mais il n'y a pas de graphe global des transactions, puisque personne ne détient la totalité du registre. En revanche, cela implique aussi un certain compromis sur la décentralisation : l'émetteur d'un contrat intelligent peut avoir un rôle central (à l'instar d'un "*contract deployer*" dans Ethereum). Néanmoins, contrairement à la blockchain, avec la Client-side Validation, vous ne stockez et ne validez que les contrats qui vous intéressent, ce qui améliore la scalabilité en évitant de télécharger et de vérifier tous les états existants.

![RGB-Bitcoin](assets/fr/004.webp)

#### 2. Théorème CAP (Consistency, Availability, Partition tolerance)

Le théorème CAP souligne qu'il est impossible pour un système distribué de satisfaire simultanément la cohérence (*Consistency*), la disponibilité (*Availability*) et la tolérance au partitionnement (*Partition tolerance*).

- **Blockchain**

La blockchain privilégie la cohérence et la disponibilité, mais s'accommode mal de la partition du réseau : si vous ne voyez pas un bloc, vous n'êtes pas en mesure d'agir et d'avoir la même vue que l'ensemble du réseau.

- **Lightning**

Un système de canaux d'états dispose de la disponibilité et de la tolérance au partitionnement (puisque deux nœuds peuvent rester connectés entre eux même si le réseau est fragmenté), mais la cohérence globale dépend de l'ouverture et de la fermeture des canaux sur la blockchain.

- **Client-side Validation (RGB)**

Un système comme RGB offre la cohérence (chaque participant valide ses données localement, sans ambiguïté) et la tolérance au partitionnement (vous conservez vos données de manière autonome), mais ne garantit pas la disponibilité globale (chacun doit s'assurer d'avoir les morceaux d'historique pertinents, et certains participants peuvent ne rien publier ou cesser de partager certaines informations).

![RGB-Bitcoin](assets/fr/005.webp)

#### 3. Trilemme CIA (Confidentiality, Integrity, Availability)

Ce trilemme rappelle que la confidentialité, l'intégrité et la disponibilité ne peuvent être optimisées toutes les trois en même temps. Blockchain, Lightning et Client-side Validation se répartissent différemment dans cet équilibre. L'idée est qu'aucun système unique ne peut tout fournir ; il faut combiner plusieurs approches (l'horodatage de la blockchain, l'approche synchrone de Lightning, et la validation locale avec RGB) pour obtenir un ensemble cohérent offrant de bonnes garanties dans chaque dimension.

![RGB-Bitcoin](assets/fr/006.webp)

### Le rôle de la blockchain et la notion de sharding

La blockchain (ici Bitcoin) sert surtout de mécanisme de _time-stamping_ et de protection contre la double dépense. Au lieu d'y insérer l'intégralité des données d'un smart contract ou d'un système décentralisé, on se contente d'y inclure des **engagements cryptographiques** (_commitments_) à des transactions (au sens de la Client-side Validation, que nous appellerons "transitions d'état"). Ainsi :
- On libère la blockchain d'une grande quantité de données et de logique ;
- Chaque utilisateur ne stocke que l'historique nécessaire à sa propre portion du contrat (son "*shard*"), au lieu de répliquer l'état global.

Le _sharding_ est un concept né dans les bases de données distribuées (par exemple MySQL pour des réseaux sociaux comme Facebook ou Twitter). Pour résoudre le problème de volume de données et de latences de synchronisation, on segmente la base en _shards_ (États-Unis, Europe, Asie, etc.). Chaque segment est cohérent localement et ne se synchronise que partiellement avec les autres.

Pour les smart contracts de type RGB, on sharde selon les contrats eux-mêmes. Chaque contrat constitue un _shard_ indépendant. Par exemple, si vous ne détenez que des jetons USDT, vous n'avez pas à stocker ou valider tout l'historique d'un autre token comme l'USDC. Sur Bitcoin, la blockchain ne fait pas de _sharding_ : vous avez un ensemble d'UTXOs global. Avec la Client-side Validation, chaque participant conserve seulement les données des contrats qu'il détient ou utilise.

On peut donc imaginer l'écosystème ainsi :
- **La blockchain (Bitcoin)** comme fondation qui assure la réplication complète d'un registre minimal et sert de couche d'horodatage ;
- **Le Lightning Network** pour des transactions rapides et confidentielles, qui repose toujours sur la sécurité et le règlement final de la blockchain Bitcoin ;
- **RGB et la Client-side Validation** pour ajouter une logique plus complexe de smart contracts, sans encombrer la blockchain, ni perdre en confidentialité.

![RGB-Bitcoin](assets/fr/007.webp)

Ces trois éléments forment un ensemble triangulaire plus qu'un empilement linéaire de "layer 2", "layer 3", etc. Lightning peut se brancher directement sur Bitcoin, ou bien être associé à des transactions Bitcoin qui intègrent des données RGB. De même, un usage de la "BiFi" (finance sur Bitcoin) peut composer avec la blockchain, avec Lightning et avec RGB selon les besoins en confidentialité, scalabilité, ou logique de contrat.

![RGB-Bitcoin](assets/fr/008.webp)

### La notion de transitions d'état

Dans tout système distribué, l’objectif du mécanisme de validation est de pouvoir **déterminer la validité et l’ordre chronologique des changements d’état**. Il s’agit de vérifier que les règles du protocole sont bien respectées et de prouver que ces changements d’état se succèdent dans un ordre définitif et inattaquable.

Pour comprendre comment se présente cette validation dans le cadre de **Bitcoin** et, plus généralement, pour saisir la philosophie derrière la Client-side Validation, revenons d’abord sur les mécanismes de la blockchain Bitcoin, avant de voir comment la validation côté client s’en démarque et quelles optimisations elle rend possibles.

![RGB-Bitcoin](assets/fr/009.webp)

Dans le cas de la blockchain Bitcoin, la validation des transactions repose sur une règle simple :
- Tous les nœuds du réseau téléchargent chaque bloc et chaque transaction ;
- Ils valident ces transactions pour vérifier la bonne évolution de l'UTXO set (ensemble des sorties non dépensées) ;
- Ils stockent ces données (sous forme de blocs) de manière à pouvoir rejouer l’historique si nécessaire.

![RGB-Bitcoin](assets/fr/010.webp)

Ce modèle présente toutefois deux inconvénients majeurs :
- **Scalabilité** : puisque chaque nœud doit traiter, vérifier et archiver toutes les transactions de tout le monde, il existe une limite évidente à la capacité de transaction, liée notamment à la taille maximale des blocs (1 Mo en moyenne sur 10 minutes pour Bitcoin, hors témoin) ;
- **Vie privée** : tout est diffusé et stocké publiquement (montants, adresses de destination, etc.), ce qui limite la confidentialité des échanges.

![RGB-Bitcoin](assets/fr/012.webp)

En pratique, ce modèle fonctionne pour Bitcoin en tant que couche de base (Layer 1), mais peut devenir insuffisant pour des usages plus complexes qui exigent simultanément un haut débit de transactions et un certain degré de confidentialité.

La Client-side Validation repose sur l’idée inverse : plutôt que d’exiger que tout le réseau valide et stocke toutes les transactions, chaque participant (client) va valider uniquement la partie de l’historique qui le concerne :
- Lorsqu’une personne reçoit un actif (ou toute autre propriété numérique), elle n’a besoin de connaître et de vérifier que la chaîne d’opérations (les transitions d'état) qui aboutit à cet actif et qui lui en prouve la légitimité ;
- Cette suite d’opérations, de la ***Genesis*** (émission initiale) jusqu’à la transaction la plus récente, forme un graphe orienté acyclique (DAG) ou un shard, c’est-à-dire une fraction du grand historique global.

![RGB-Bitcoin](assets/fr/013.webp)

Parallèlement, pour que le reste du réseau (ou plus exactement la couche sous-jacente, telle que Bitcoin) puisse verrouiller l’état final sans pour autant voir le détail de ces données, la Client-side Validation s’appuie sur la notion de ***commitment***.

Un *commitment* est un engagement cryptographique, typiquement un _hash_ (SHA-256 par exemple) inséré dans une transaction Bitcoin, qui prouve qu’on a englobé des données privées, sans révéler ces données.

Grâce à ces _commitments_, on peut prouver :
- L’existence d’une information (puisqu’elle est engagée dans un hash) ;
- L’antériorité de cette information (car elle est ancrée et horodatée dans la blockchain, avec une date et un ordre des blocs).

En revanche, le contenu exact n’est pas révélé, ce qui préserve sa confidentialité.

Concrètement, voici le déroulé d'une transition d'état sur RGB :
- Vous préparez une nouvelle transition d'état (par exemple le transfert d'un jeton RGB) ;
- Vous générez un engagement cryptographique à cette transition et l'insérez dans une transaction Bitcoin (on appelle ces engagements des "*anchors*" dans le protocole RGB) ;
- La contrepartie (le destinataire) récupère l'historique Client-side associé à cet actif et valide la cohérence de bout en bout, depuis la Genèse du smart contract jusqu'à la transition que vous lui transmettez.

![RGB-Bitcoin](assets/fr/014.webp)

La Client-side Validation présente ainsi deux bénéfices majeurs :

- **La scalabilité :**  
Les engagements (*commitments*) inclus dans la blockchain ont une taille réduite (de l’ordre de quelques dizaines d’octets). Cela permet de ne pas saturer l’espace dans les blocs, car seul le hash doit être inclus. Cela permet également de faire évoluer le protocole off-chain, car chaque utilisateur n’a à stocker que son fragment d’historique (son _stash_).

- **La privacy :**  
Les transactions en elles-mêmes (c’est-à-dire leur contenu détaillé) ne sont pas publiées on-chain. Seules leurs empreintes (*hash*) le sont. Ainsi, les montants, les adresses et la logique du contrat restent privés, et le receveur peut vérifier, en local, la validité de son shard en inspectant toutes les transitions antérieures. Il n’a aucune raison de diffuser ces données publiquement, sauf en cas de litige ou de preuve nécessaire.

Dans un système comme RGB, plusieurs transitions d'état de différents contrats (ou différents actifs) peuvent être agrégées dans une même transaction Bitcoin via un seul _commitment_. Ce mécanisme établit un lien déterministe et horodaté entre la transaction on-chain et les données off-chain (les transitions validées côté client), et permet d’enregistrer simultanément plusieurs shards dans un même point d’ancrage, ce qui réduit encore plus le coût et l’empreinte on-chain.

En pratique, lorsque cette transaction Bitcoin est validée, elle "verrouille" définitivement l’état des contrats sous-jacents, puisqu’il devient impossible de modifier le hash déjà inscrit dans la blockchain.

![RGB-Bitcoin](assets/fr/015.webp)

### Le concept de stash

Un **stash** est l'ensemble de données côté client qu'un participant doit absolument conserver pour maintenir l'intégrité et l'historique d'un smart contract RGB. Contrairement à un canal Lightning, où l'on peut reconstruire certains états localement à partir d'informations partagées, le stash d'un contrat RGB n'est pas répliqué ailleurs : si vous le perdez, personne ne pourra vous le restaurer, car vous êtes responsable de votre part de l'historique. C'est pourquoi il faut adopter un système avec des procédures de sauvegarde fiables dans RGB.

![RGB-Bitcoin](assets/fr/016.webp)

### Single-use Seal : origines et fonctionnement

Lors de l'acceptation d'un actif comme par exemple une monnaie, deux garanties sont essentielles :
- L'authenticité de la chose reçue ;
- L'unicité de la chose reçue, afin d'éviter les doubles dépenses.

Pour les actifs physiques, comme un billet de banque, la présence physique suffit à prouver qu'il n'est pas dupliqué. Cependant, dans le monde numérique, où les actifs sont purement informationnels, cette vérification est plus complexe, car l'information peut facilement se multiplier et être dupliquée.

Comme nous l'avons vu précédemment, la révélation par l'envoyeur de l'historique des transitions d'état permet de s'assurer de l'authenticité d'un jeton RGB. En ayant accès à toutes les transactions depuis la transaction génésique, on peut confirmer l'authenticité du jeton. Ce principe est similaire à celui de Bitcoin où l'on peut suivre l'historique des pièces jusqu'à la transaction coinbase originelle pour vérifier leur validité. Toutefois, contrairement à Bitcoin, cet historique des transitions d'état dans RGB est privé et conservé côté client.

Pour prévenir la double dépense des jetons RGB, nous utilisons un mécanisme appelé "**Single-use Seal**". Ce système assure que chaque jeton, une fois utilisé, ne peut être réutilisé une seconde fois frauduleusement.

Les Single-use Seals sont des primitives cryptographiques, proposées en 2016 par Peter Todd, qui s’apparentent au concept de scellés physiques : une fois qu’on a placé un sceau sur un conteneur, il devient impossible de l’ouvrir ou de le modifier sans briser le sceau de manière irréversible.

![RGB-Bitcoin](assets/fr/018.webp)

Cette approche, transposée à l’univers numérique, permet de prouver qu’une séquence d’événements a bel et bien eu lieu et qu’elle ne peut plus être altérée a posteriori. Les Single-use Seals dépassent donc la simple logique de `hash + timestamp` en y ajoutant la notion d’un "sceau" fermable **une seule et unique fois**.

![RGB-Bitcoin](assets/fr/017.webp)

Pour que les Single-use Seals fonctionnent, il faut un support de preuve de publication capable de prouver l’existence ou l’absence d’une publication et difficile (voire impossible) à falsifier une fois l’information diffusée. Une **blockchain** (comme Bitcoin) peut tenir ce rôle, tout comme un journal papier au tirage public par exemple. L’idée est la suivante :
- On veut prouver qu’un certain engagement sur un message `h(m)` a été publié à une audience sans révéler le contenu du message `m` ;
- On veut prouver qu’aucun autre engagement de message `h(m')` concurrent n’a été publié à la place de `h(m)` ;
- On veut également pouvoir vérifier que le message `m` existe avant une certaine date.

Une blockchain se prête idéalement à ce rôle : dès qu’une transaction est incluse dans un bloc, tout le réseau possède la même preuve infalsifiable de son existence et de son contenu (du moins en partie, puisque le _commitment_ peut masquer les détails tout en prouvant l’authenticité du message).

On peut donc voir un Single-use Seal comme une promesse formelle de publier un message (encore inconnu à ce stade) une et une seule fois, de manière vérifiable par toutes les parties intéressées.

Contrairement aux simples _commitments_ (hash) ou aux horodatages qui attestent d’une date d’existence, un Single-use Seal offre la garantie supplémentaire qu’**aucun engagement alternatif** ne peut coexister : on ne peut pas fermer deux fois le même sceau ou tenter de remplacer le message scellé.

La comparaison suivante aide à comprendre ce principe :
- **Engagement cryptographique (hash)** : Avec une fonction de hachage, on peut s'engager sur une donnée (un nombre) en publiant son empreinte (hash). La donnée reste secrète tant qu'on ne révèle pas la préimage, mais on peut prouver qu'on la connaissait à l'avance ;
- **Horodatage (blockchain)** : En insérant ce hash dans la blockchain, on prouve aussi qu'on le connaissait à un instant précis (celui de l'inclusion dans un bloc) ;
- **Single-use Seal** : Avec les sceaux à usage unique, on va plus loin en rendant l'engagement unique. Avec un simple hash, on peut créer plusieurs engagements contradictoires en parallèle (le problème du docteur qui annonce "*C'est un garçon*" à la famille et "*C'est une fille*" dans son journal personnel). Le Single-use Seal élimine cette possibilité en connectant l'engagement à un support de preuve de publication, comme la blockchain Bitcoin, de sorte qu'une dépense d'UTXO scelle définitivement l'engagement. Une fois dépensé, on ne peut plus redépenser le même UTXO pour remplacer l'engagement.

|                                                                                  | Engagement simple (digest/hash) | Timestamps | Single-use Seals |
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

Dans le cadre de la Client-side Validation, il faut toutefois aller plus loin : si la définition d’un sceau reste elle-même hors de la blockchain, il est possible (en théorie) que quelqu’un conteste l’existence ou la légitimité du sceau en question. Pour pallier ce problème, on recourt à une chaîne de Single-use Seals, imbriqués les uns dans les autres :
- Chaque sceau fermé renferme la définition du sceau suivant ;
- On inscrit ces fermetures (avec leurs _commitments_) au sein de la blockchain (dans une transaction Bitcoin) ;
- Ainsi, toute tentative de modifier un sceau antérieur se retrouverait en contradiction avec l’historique ancré sur Bitcoin.

C’est précisément ce que fait le système RGB :
- Les messages publiés sont les _commitments_ vers des données validées côté client ;
- La définition du sceau est associée à un UTXO Bitcoin ;
- Le sceau se ferme lorsque l’on dépense cet UTXO ou qu’on crédite une nouvelle sortie liée au même engagement ;
- La chaîne de transactions qui dépense ces UTXOs correspond à la preuve de publication : chaque transition ou changement d’état sur RGB s’ancre ainsi dans Bitcoin.

Pour résumer :
- Le _seal definition_ est l'UTXO que vous destinez à sceller un engagement futur ;
- Le _seal closing_ survient quand vous dépensez cet UTXO, en créant une transaction qui contient l'engagement ;
- Le _witness_ est la transaction elle-même, qui prouve que vous avez bien fermé le sceau avec ce contenu ;
- Vous ne pouvez pas prouver qu'un sceau n'a pas été fermé (on ne peut pas être absolument sûr qu'un UTXO n'est pas déjà dépensé ou ne le sera pas dans un bloc qu'on n'a pas encore vu), mais on peut prouver qu'il a bel et bien été fermé.

Cette unicité est importante pour la Client-side Validation : quand vous validez une transition d'état, vous vérifiez qu'elle correspond à un UTXO unique, non dépensé préalablement dans un engagement concurrent. C'est ce qui garantit l'absence de double dépense au niveau des smart contracts off-chain.

### Engagements multiples et ancrages

Un smart contract RGB peut avoir besoin de dépenser simultanément plusieurs Single-use Seals (plusieurs UTXOs). De plus, une seule transaction Bitcoin peut référencer plusieurs contrats distincts, chacun venant sceller sa propre transition d'état. Cela nécessite un mécanisme de **multi-commitments** permettant de prouver, de manière déterministe et unique, qu'aucun des engagements n'existe en double. C'est ici qu'intervient la notion d'**anchor** dans RGB : une structure spéciale reliant une transaction Bitcoin et un ou plusieurs engagements client-side (transitions d'état), chacun relevant potentiellement d'un contrat différent. Nous allons justement détailler ce concept dans le chapitre suivant.

![RGB-Bitcoin](assets/fr/023.webp)

Deux principaux dépôts GitHub du projet (sous l'organisation LNPBP) regroupent les implémentations de base de ces concepts étudiés dans le premier chapitre :
- **client_side_validation** : Contient les primitives Rust pour la validation locale ;
- **single_use_seals** : Implémente la logique pour définir et fermer ces sceaux de manière sécurisée.

![RGB-Bitcoin](assets/fr/020.webp)

Notons que ces briques logicielles sont agnostiques par rapport à Bitcoin ; on pourrait, en théorie, les appliquer à tout autre support de preuve de publication (un autre registre, un journal, etc.). Dans la pratique, RGB repose sur Bitcoin pour sa robustesse et son large consensus.

![RGB-Bitcoin](assets/fr/021.webp)

### Questions du public

#### Vers un usage plus large des Single-use Seals

Peter Todd a également créé le protocole _Open Timestamps_, et le concept de Single-use Seal est un prolongement naturel de ces idées. Au-delà de RGB, on peut envisager d'autres cas d'utilisation, par exemple la construction de _sidechains_ sans recourir au _merge mining_ ni aux propositions liées aux drivechains comme le BIP300. Tout système nécessitant un engagement unique peut, en principe, exploiter cette primitive cryptographique. Aujourd'hui, RGB est la première grande mise en application concrète et complète.

#### Problèmes de disponibilité des données

Étant donné qu'en Client-side Validation, chaque utilisateur stocke sa partie de l'historique, la disponibilité des données n'est pas garantie globalement. Si un émetteur de contrat ne publie pas certaines informations ou les révoque, vous pourriez ignorer l'évolution réelle de l'offre. Dans certains cas (comme les stablecoins), on s'attend à ce que l'émetteur tienne à jour des données publiques pour prouver le volume en circulation, mais rien ne l'y contraint techniquement. Il est donc possible de concevoir des contrats volontairement opaques avec un stock illimité, ce qui pose des questions de confiance.

#### Sharding et isolement des contrats

Chaque contrat représente un _shard_ isolé : USDT et USDC, par exemple, n'ont pas à partager leur historique. Les swaps atomiques restent possibles, mais cela n'implique pas de fusionner leurs registres. Tout se fait par engagement cryptographique, sans divulguer l'ensemble du graphe d'historique à chaque participant.

### Conclusion

Nous avons vu où se situe le concept de Client-side Validation par rapport à la blockchain et aux _state channels_, en quoi il répond à des trilemmes de l'informatique distribuée, et comment il exploite la blockchain Bitcoin uniquement pour éviter la double dépense et pour l'horodatage (*time-stamping*). L'idée repose sur la notion de **Single-use Seal**, permettant la création d'engagements uniques que vous ne pouvez pas redépenser à volonté. Ainsi, chaque participant ne télécharge que l'historique strictement nécessaire, ce qui accroît la scalabilité et la confidentialité des smart contracts tout en conservant la sécurité de Bitcoin en toile de fond.

La prochaine étape consistera à expliquer plus en détail comment on applique concrètement ce mécanisme de Single-use Seal dans Bitcoin (via les UTXOs), comment on crée et on valide les anchors, puis comment on construit des smart contracts complets dans RGB. Nous verrons notamment la question des engagements multiples, le défi technique de prouver qu'une transaction Bitcoin scelle simultanément plusieurs transitions d'état dans différents contrats, sans introduire de vulnérabilités ou de doubles engagements.

Avant de plonger dans les détails plus techniques du deuxième chapitre, n'hésitez pas à relire les définitions clés (Client-side Validation, Single-use Seal, anchors, etc.) et à garder à l'esprit la logique globale : nous cherchons à concilier les atouts de la blockchain Bitcoin (sécurité, décentralisation, time-stamping) avec ceux des solutions off-chain (rapidité, confidentialité, scalabilité), et c'est précisément ce que RGB et la Client-side Validation tentent de réaliser.

## La couche d'engagement
<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

![video](https://youtu.be/FS6PDprWl5Q)


Dans ce chapitre, nous allons étudier la mise en application de la Client-side Validation et des Single-use Seals au sein de la blockchain Bitcoin. Nous allons présenter les principes majeurs de la **couche d'engagement** (layer 1) de RGB, en nous intéressant plus particulièrement au schémas **TxO2**, retenu par RGB pour définir et fermer un sceau dans le cadre d’une transaction Bitcoin. Ensuite, nous parlerons de deux points importants qui n’ont pas encore été traités en détail :
- Les _deterministic Bitcoin commitments_ ;
- Les _multi-protocol commitments_.

C’est la combinaison de ces concepts qui nous permet de superposer plusieurs systèmes ou contrats au-dessus d’un même UTXO et donc d’une même blockchain.

Il convient de rappeler que les opérations cryptographiques décrites peuvent s’appliquer, dans l’absolu, à d’autres blockchains ou médias de publication, mais les caractéristiques de Bitcoin (en matière de décentralisation, de résistance à la censure et d’ouverture à tous) en fait le socle idéal pour développer de la programmabilité avancée comme celle requise par **RGB**.

### Les schémas d'engagement dans Bitcoin et leur utilisation par RGB

Comme vu dans le premier chapitre de la formation, les Single-use Seals sont un concept général : on fait une promesse d’inclure un engagement (_commitment_) dans un emplacement précis d’une transaction, cet emplacement agit comme un scellé que l’on ferme sur un message. Toutefois, sur la blockchain Bitcoin, plusieurs options existent pour choisir où placer ce _commitment_.

Pour comprendre la logique, rappelons le principe de base : pour fermer un _single-use seal_, on dépense l’endroit scellé en y insérant le _commitment_ sur un message donné. Dans Bitcoin, cela peut se faire de différentes manières :

- **Utiliser une clé publique ou une adresse**  

On peut décider qu’une clé publique ou une adresse spécifique est le _single-use seal_. Dès que cette clé ou cette adresse apparaît on-chain dans une transaction, cela signifie que le scellé est fermé avec un certain message.

- **Utiliser un output de transaction Bitcoin**  

Cela signifie que l’on définit un _single-use seal_ comme un _outpoint_ précis (un couple TXID + numéro d’output). Dès que cet _outpoint_ est dépensé, il s’agit de l’acte de fermeture du scellé.

En travaillant sur RGB, nous avons identifié au moins 4 manières différentes d’implémenter ces scellés sur Bitcoin :
- Définir le scellé via une clé publique, et le fermer dans un _output_ ;
- Définir le scellé via un _outpoint_, et le fermer dans un _output_ ;
- Définir le scellé via la valeur d'une clé publique, et le fermer dans un _input_ ;
- Définir le scellé via un _outpoint_, et le fermer dans un _input_.

| Nom du schéma | Définition du scellé      | Fermeture du scellé   | Exigences supplémentaires                                         | Application principale       | Schémas d'engagement possibles |
| ------------- | ------------------------- | --------------------- | ----------------------------------------------------------------- | ---------------------------- | ------------------------------ |
| PkO           | Valeur de la clé publique | Sortie de transaction | P2(W)PKH                                                          | Aucune pour le moment        | Keytweak, taptweak, opret      |
| TxO2          | Sortie de transaction     | Sortie de transaction | Nécessite des engagements déterministes sur Bitcoin               | RGBv1 (universel)            | Keytweak, tapret, opret        |
| PkI           | Valeur de la clé publique | Entrée de transaction | Uniquement Taproot & non compatible avec les portefeuilles Legacy | Identités basées sur Bitcoin | Sigtweak, witweak              |
| TxO1          | Sortie de transaction     | Entrée de transaction | Uniquement Taproot & non compatible avec les portefeuilles Legacy | Aucune pour le moment        | Sigtweak, witweak              |

Nous ne détaillerons pas chacune de ces configurations, car dans RGB, nous avons choisi d’utiliser **un _outpoint_ comme définition du scellé**, et de placer le _commitment_ dans l’output de la transaction dépensant cet _outpoint_. On peut donc introduire les concepts suivants pour la suite :
- **"Seal definition"** : Un _outpoint_ donné (identifié par TXID + N° de sortie) ;
- **"Seal closing"** : La transaction qui dépense cet _outpoint_, dans laquelle on ajoute un _commitment_ à un message.

Ce schéma a été sélectionné pour sa compatibilité avec l’architecture RGB, mais d’autres configurations pourraient être utiles pour des usages différents.

La mention "O2" dans "TxO2" rappelle que la définition et la fermeture reposent toutes deux sur la dépense (ou la création) d’une sortie de transaction.

### Exemple d'utilisation du schéma TxO2

Pour rappel, définir un _single-use seal_ ne nécessite pas nécessairement de publier une transaction on-chain. Il suffit qu’Alice, par exemple, possède déjà un UTXO non dépensé. Elle peut décider : "Cet _outpoint_ (déjà existant) est désormais mon scellé". Elle le note localement (_client-side_), et tant que cet UTXO n’est pas dépensé, le scellé est considéré comme ouvert.

![RGB-Bitcoin](assets/fr/024.webp)

Le jour où elle veut fermer le scellé (pour signaler un événement, ou pour ancrer un message particulier), elle dépense cet UTXO dans une nouvelle transaction (on appelle souvent cette transaction la "_witness transaction_" (sans rapport avec _segwit_, c’est juste le terme qu’on lui donne). Cette nouvelle transaction contiendra le _commitment_ au message.

![RGB-Bitcoin](assets/fr/025.webp)

Notons que dans cet exemple :
- Personne d’autre que Bob (ou les personnes à qui Alice choisit de révéler la preuve complète) ne saura qu’un certain message est caché dans cette transaction ;
- Tout le monde peut constater que l'_outpoint_ a été dépensé, mais seul Bob détient la preuve que le message est bien ancré dans la transaction.

Pour illustrer ce schéma TxO2, on peut utiliser un _single-use seal_ comme mécanisme de révocation d’une clé PGP. Au lieu de publier un certificat de révocation sur des serveurs, Alice peut dire : "Cette sortie Bitcoin, si elle est dépensée, signifie que ma clé PGP est révoquée".

Alice dispose donc d’un UTXO spécifique, auquel est associé localement (côté client) un certain état ou des données (connues d’elle seule).

Alice informe Bob qu’en cas de dépense de cet UTXO, un événement particulier sera réputé s’être produit. De l’extérieur, on ne voit qu’une transaction Bitcoin ; mais Bob, lui, sait que cette dépense a une signification cachée.

![RGB-Bitcoin](assets/fr/026.webp)

Au moment où Alice dépense cet UTXO, elle referme le scellé sur un message qui indique sa nouvelle clé, ou simplement la révocation de l’ancienne. Ainsi, toute personne surveillant on-chain verra que l’UTXO est dépensé, mais seule celle qui dispose de la preuve complète saura qu’il s’agit précisément de la révocation de la clé PGP.

![RGB-Bitcoin](assets/fr/027.webp)

Pour que Bob ou toute autre personne concernée puisse vérifier le message caché, Alice doit lui fournir des informations off-chain.

![RGB-Bitcoin](assets/fr/028.webp)

Alice doit donc fournir à Bob :
- Le message lui-même (par exemple, la nouvelle clé PGP) ;
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
- **La couche supérieure (blockchain, publique)** : tout le monde voit la transaction et sait qu’il y a un _outpoint_ dépensé ;
- **La couche inférieure (client-side, privée)** : seule Alice (ou la personne intéressée) sait que cette dépense correspond à tel message, via la preuve cryptographique et le message qu’elle conserve en local.

![RGB-Bitcoin](assets/fr/034.webp)

Mais lors de cette fermeture du scellé, on peut se poser la question suivante : concrètement, où devons-nous insérer le _commitment_ ?

Nous avons brièvement mentionné, dans la partie précédente, comment le modèle Client-side Validation peut s’appliquer à RGB ou à d’autres systèmes. Ici, nous abordons la partie concernant les **deterministic Bitcoin commitments** et la façon de les intégrer dans une transaction. L’idée est de comprendre pourquoi on cherche à insérer un unique engagement dans la _witness transaction_, et surtout comment s’assurer qu’il ne puisse y avoir d’autres engagements concurrents non dévoilés.

### Les emplacements du commitment dans une transaction

Lorsque vous transmettez à quelqu’un la preuve qu’un certain message est ancré dans une transaction, vous devez pouvoir garantir qu’il n’existe pas, dans cette même transaction, une autre forme d’engagement (un second message caché) qui ne vous aurait pas été révélé. Pour que la validation côté client reste robuste, il faut donc un mécanisme **déterministe** permettant de placer un unique _commitment_ dans la transaction qui ferme le _single-use seal_.

La _witness transaction_ dépense le fameux UTXO (ou _seal definition_) et cette dépense correspond à la fermeture du scellé. Au niveau technique, on sait que chaque outpoint ne peut être dépensé qu’une seule fois. C’est justement ce qui sert de base à la résistance à la double dépense sur Bitcoin. Mais la transaction de dépense peut avoir plusieurs _inputs_, plusieurs _outputs_, ou être composée de façon complexe (coinjoins, cannaux Lightning, etc.). Il faut donc définir clairement où insérer le _commitment_ dans cette structure, sans ambiguïté et de manière uniforme.

Quelle que soit la méthode (PkO, TxO2, etc.), le _commitment_ peut être inséré :
- **Dans un Input** via :
    - **Sigtweak** (on modifie le composant `r` de la signature ECDSA, ce qui s’apparente au principe de "Sign-to-contract") ;
    - **Witweak** (on modifie les données _segregated witness_ de la transaction).

- **Dans un Output** via :
    - **Keytweak** (on "tweake" la clé publique destinataire avec le message) ;
    - **Opret** (on place le message dans une sortie `OP_RETURN`, non dépensable) ;
    - **Tapret** (ou _Taptweak_), qui s’appuie sur taproot pour insérer l’engagement dans la partie script d’une clé taproot, ce qui vient modifier la clé publique de manière déterministe.

![RGB-Bitcoin](assets/fr/035.webp)

Voici le détail de chaque méthode :

![RGB-Bitcoin](assets/fr/038.webp)

***Sig tweak (sign-to-contract) :***

Un schéma anciennement proposé consistait à exploiter la partie aléatoire d’une signature (ECDSA ou Schnorr) pour y intégrer le _commitment_ : c’est la technique appelée "**Sign-to-contract**". Vous remplacez le nonce généré au hasard par un hash contenant la donnée. Ainsi, la signature révèle implicitement votre engagement, sans espace additionnel dans la transaction. Cette approche présente des avantages :
- Pas de surcharge on-chain (vous utilisez la même place que le nonce de base) ;
- En théorie, cela peut être assez discret, car le nonce est initialement une donnée aléatoire.

Cependant, 2 inconvénients majeurs ont émergé :
- Les multisig avant Taproot : quand vous avez plusieurs signataires, il faut décider quelle signature porte le _commitment_. Les signatures peuvent être ordonnées différemment, et si un signataire refuse, vous perdez le contrôle sur l’aboutissement du _commitment_ ;
- MuSig et le nonce partagé : avec les multisig Schnorr (*MuSig*), la génération du nonce est un algorithme multipartite, et il devient pratiquement impossible de tweaker le nonce individuellement.

En pratique, **sig tweak** est également peu compatible avec le matériel (hardware wallets) et les formats existants (Lightning, etc.). Cette belle idée est donc difficile à mettre en place concrètement.

***Key tweak (pay-to-contract) :***

Le **key tweak** reprend le concept historique de _pay-to-contract_. On prend la clé publique `X` et on la tweak en lui ajoutant la valeur `H(message)`. Concrètement, si `X = x * G` et `h = H(message)`, alors la nouvelle clé sera `X' = X + h * G`. Cette clé tweakée dissimule l’engagement sur le `message`. Le détenteur de la clé privée d’origine peut, en ajoutant `h` à sa clé privée `x`, prouver qu’il possède la clé permettant de dépenser la sortie. En théorie, c’est élégant, car :
- Le _commitment_ s’inscrit sans ajouter de champs supplémentaires ;
- Vous ne stockez pas de données on-chain additionnelles.

Néanmoins, dans la pratique, on se heurte aux difficultés suivantes :
- Les wallets ne reconnaissent plus la clé publique standard, puisqu’elle a été “tweakée” ; ils ne peuvent donc pas facilement associer l’UTXO à votre clé habituelle ;
- Les hardware wallets ne sont pas conçus pour signer avec une clé qui n’est pas issue de leur dérivation standard ;
- Vous devez adapter vos scripts, descriptors, etc.

Dans le cadre de RGB, cette piste a été envisagée jusqu’en 2021, mais il s’est avéré trop compliqué de la faire fonctionner avec les standards et l’infrastructure actuelle.

***Witness tweak :***

Une autre idée, que certains protocoles comme les _inscriptions Ordinals_ ont concrétisée, est de placer les données directement dans la section `witness` de la transaction (d’où l’expression "witness tweak"). Cependant, cette méthode :
- Rend l’engagement immédiatement visible (vous collez littéralement des données brutes dans le witness) ;
- Peut être sujette à la censure (des mineurs ou nœuds peuvent refuser de relayer si c’est trop volumineux ou toute autre caractéristique arbitraire) ;
- Consomme de l’espace dans les blocs, ce qui est contraire à l’objectif de discrétion et de légèreté de RGB.

En plus, le witness est conçu pour être prunable dans certains contextes, ce qui peut rendre plus compliqué le fait d'avoir des preuves robustes.

***Op-return (opret) :***

Très simple dans son fonctionnement, un `OP_RETURN` permet de stocker un hash ou un message dans un champ spécial de la transaction. Mais c’est immédiatement détectable : tout le monde voit qu’il y a un _commitment_ dans la transaction, et cela peut être censuré ou écarté, en plus d’ajouter un output supplémentaire. Puisque cela augmente la transparence et la taille, c’est donc considéré comme moins satisfaisant dans l’optique d’une solution de Client-side Validation.

```txt
34-byte_Opret_Commitment =
 OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
  1-byte       1-byte         32 bytes                      
```

### Tapret

La dernière option est l’utilisation de **Taproot** (introduit avec le BIP341) avec le schéma *Tapret*. *Tapret* est une forme plus complexe d'engagement déterministe, qui apporte des améliorations en termes d’empreinte sur la blockchain et de confidentialité pour les opérations de contrat. L’idée directrice est de cacher le commitment dans la partie `Script Path Spend` d’une [transaction taproot](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki).

![RGB-Bitcoin](assets/fr/036.webp)

Avant de décrire comment l’engagement est inséré dans une transaction taproot, examinons la **forme exacte** de l’engagement, qui doit **impérativement** correspondre à une chaîne de 64 octets [construite](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) de la manière suivante :

```txt
64-byte_Tapret_Commitment =

 OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
 OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
        TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```

- Les 29 octets `OP_RESERVED`, suivis de `OP_RETURN`, puis de `OP_PUSHBYTE_33`, forment la partie _prefix_ de 31 octets ;
- Vient ensuite un _commitment_ de 32 octets (généralement la racine de Merkle issue du **MPC**), auquel on ajoute 1 octet de **Nonce** (soit 33 octets au total pour cette seconde partie).

Ainsi, la méthode `Tapret` de 64 octets ressemble à un `Opret` auquel on a préfixé 29 octets de `OP_RESERVED` et auquel on ajoute un octet supplémentaire en guise de Nonce.

Pour conserver une grande flexibilité d’implémentation, de confidentialité et de passage à l’échelle, le schéma Tapret prend en compte divers cas d’usage, selon les besoins :
- Incorporation unique d’un commitment Tapret dans une transaction taproot sans structure de Script Path préexistante ;
- Intégration d’un commitment Tapret dans une transaction taproot déjà dotée d’un Script Path.

Détaillons ensemble chacun de ces deux scénarios.

#### Incorporation Tapret sans Script Path existant

Dans ce premier cas, on part d’une sortie taproot (*Taproot Output Key*) `Q` qui ne comporte que la clé publique interne `P` *(Internal Key*), sans chemin de script associé (*Script Path*) :

![RGB-Bitcoin](assets/fr/047.webp)

- `P` : la clé publique interne pour le _Key Path Spend_.
- `G` : le point générateur de la courbe elliptique [secp256k1](https://en.bitcoin.it/wiki/Secp256k1).
- `t = tH_TWEAK(P)` est le facteur de tweak, calculé via un _tagged hash_ (par exemple `SHA-256(SHA-256(TapTweak) || P)`), conformément au [BIP86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki#address-derivation). Cela prouve qu’il n’y a pas de script caché.

Pour inclure un commitment **Tapret**, il faut alors ajouter une **Script Path Spend** avec un **unique script**, selon le schéma suivant :

![RGB-Bitcoin](assets/fr/048.webp)

- `t = tH_TWEAK(P || Script_root)` devient alors le nouveau facteur de tweak, incluant le **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` représente la racine de ce **script**, laquelle est simplement un hash de type `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.

La preuve d’inclusion et d’unicité dans l’arbre taproot se résume ici à la seule clé publique interne `P`.

#### Intégration Tapret dans un Script Path préexistant

Le second scénario concerne une **sortie taproot** `Q` plus complexe, qui comporte déjà plusieurs scripts. Par exemple, on dispose d’un arbre de 3 scripts :

![RGB-Bitcoin](assets/fr/049.webp)

- `tH_LEAF(x)` désigne la fonction de hachage (tagged hash) normalisée d’un script leaf.
- `A, B, C` représentent les scripts déjà inclus dans la structure taproot.

Pour ajouter le commitment Tapret, on doit insérer un script "inconsommable" (*unspendable script*) au premier niveau de l’arbre, en décalant les scripts déjà existants un niveau plus bas. Visuellement, l’arbre devient :

![RGB-Bitcoin](assets/fr/050.webp)

- `tHABC` représente le hash (tagged) du niveau supérieur regroupant `A, B, C`.
- `tHT` représente le hash du script correspondant au `Tapret` de 64 octets.

Selon les règles de taproot, chaque branche/feuille doit être combinée en respectant un ordre lexicographique des hachages. Deux cas se présentent alors :
- `tHT` > `tHABC` : le commitment Tapret se place à droite dans l’arbre. La preuve d’unicité n’a besoin que de `tHABC` et `P` ;
- **`tHT` < `tHABC`** : le commitment Tapret se place à gauche. Pour prouver qu’il n’y a pas d’autre commitment Tapret dans la partie droite, il faut révéler `tHAB` et `tHC` afin de démontrer l’absence de tout autre script de ce type.

Exemple visuel pour le premier cas (`tHABC < tHT`) :

![RGB-Bitcoin](assets/fr/051.webp)

Exemple pour le second cas (`tHABC > tHT`) :

![RGB-Bitcoin](assets/fr/052.webp)

#### Optimisation avec le nonce

Pour améliorer la confidentialité, on peut "miner" (un terme plus juste serait "bruteforcer") la valeur du `<Nonce>` (le dernier octet du `Tapret` de 64 octets) pour tenter d’obtenir un hash `tHT` tel que `tHABC < tHT`. Dans ce cas, le commitment se place à droite, ce qui évite ainsi à l’utilisateur de devoir divulguer tout le contenu des scripts existants pour prouver l’unicité du Tapret.

En résumé, le `Tapret` offre un moyen discret et déterministe d’incorporer un engagement dans une transaction taproot, tout en respectant l’exigence d’unicité et de non-ambiguïté essentielle à la logique de Client-side Validation et des Single-use Seal de RGB.

#### Les sorties valides

Pour les opérations de commitment dans le cadre de RGB, l’exigence principale pour qu’un schéma de commitment Bitcoin soit valide est la suivante : La transaction (*witness transaction*) doit de manière prouvable contenir un seul commitment. Grâce à cette exigence, il devient impossible de construire, au sein d’une même transaction, une histoire alternative pour les données validées côté client. Ainsi, le message autour duquel se ferme le _single-use seal_ est unique.

Pour satisfaire ce principe, et ce quel que soit le nombre de sorties d’une transaction, on impose qu’**une seule et unique sortie** puisse contenir un engagement (*commitment*). Pour chacun des schémas utilisés (*Opret* ou *Tapret*), les seules sorties valides pouvant contenir un _commitment_ RGB sont :
- La première sortie `OP_RETURN` (si présente) pour le schéma *Opret* ;
- La première sortie taproot (si présente) pour le schéma *Tapret*.

Notez qu’il est tout à fait possible qu’une transaction contienne simultanément un unique commitment `Opret` et un unique commitment `Tapret` dans deux sorties distinctes. Grâce à la nature déterministe de la Seal Definition, ces deux engagements correspondent alors à deux données distinctes validées côté client.

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

Au fil de l’étude, il est apparu qu’aucun des schémas de commitments n’était pleinement compatible avec le standard Lightning actuel (qui n’emploie pas Taproot, ni _muSig2_, ni la prise en compte d’un _commitment_ supplémentaire). Des efforts sont en cours pour modifier la construction de canaux Lightning (*BiFrost*) et permettre d’insérer les engagements RGB. C’est un autre chantier où l’on doit revoir la structure de la transaction, les clés, et la façon dont sont signées les mises à jour de canaux.

L’analyse a montré qu’en effet, d’autres méthodes (key tweak, sig tweak, witness tweak, etc.) présentaient d’autres formes de complication :
- Soit on a un gros volume on-chain ;
- Soit on a une incompatibilité radicale avec le code existant des wallets ;
- Soit la solution n’est pas viable en multisig non coopératif.

Ainsi, pour RGB, deux des méthodes sortent particulièrement du lot : ***Opret*** et ***Tapret***, toutes deux classées en “Transaction Output”, et compatibles avec le mode TxO2 utilisé par le protocole.

### Multi Protocol Commitments - MPC

Dans cette section, nous abordons la manière dont **RGB** gère l’agrégation de plusieurs contrats (ou plus précisément leurs _transition bundles_) au sein d’un unique engagement (*commitment*) enregistré dans une transaction Bitcoin via un schéma déterministe (selon `Opret` ou `Tapret`). Pour y parvenir, l'ordre de Merkelisation des différents contrats s’opère dans une structure nommée **MPC Tree** (_Multi Protocol Commitment Tree_). Dans cette section, nous allons étudier la construction de ce MPC Tree, l’obtention de sa racine, ainsi que la façon dont plusieurs contrats peuvent ainsi partager la même transaction en toute confidentialité et sans ambiguïté.

Le Multi Protocol Commitment (MPC) vise à répondre à deux besoins :
- La construction du hash `mpc::Commitment` : celui-ci sera inclus dans la blockchain Bitcoin selon un schéma `Opret` ou `Tapret`, et doit refléter l’ensemble des états changés (state changes) à valider ;
- Le stockage simultané de plusieurs contrats dans un seul _commitment_, permettant de gérer en une seule transaction Bitcoin des mises à jour distinctes, portant sur plusieurs assets ou contrats RGB.

Concrètement, chacun des _transition bundles_ appartient à un contrat particulier. Toutes ces informations sont insérées dans un **MPC Tree** dont la racine (`mpc::Root`) est ensuite hachée de nouveau pour donner le `mpc::Commitment`. C’est ce dernier hash qui est placé dans la transaction Bitcoin (_witness transaction_), selon la méthode déterministe choisie.

![RGB-Bitcoin](assets/fr/042.webp)

#### MPC Root Hash

La valeur effectivement inscrite on-chain (dans `Opret` ou `Tapret`) se nomme `mpc::Commitment`. Celle-ci est calculée en suivant la forme du [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki), selon la formule :

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

où :
- `mpc_tag` est une étiquette : `urn:ubideco:mpc:commitment#2024-01-31`, choisie selon les [conventions RGB de tagging](https://github.com/RGB-WG/rgb-core/blob/master/doc/Commitments.md) ;
- `depth` (1 octet) indique la profondeur du *MPC Tree* ;
- `cofactor` (16 bits, en Little Endian) est un paramètre permettant de favoriser l’unicité des positions assignées à chaque contrat dans l’arbre ;
- `mpc::Root` est la racine de *MPC Tree*, calculée selon le processus décrit dans la section suivante.

![RGB-Bitcoin](assets/fr/044.webp)

#### Construction du MPC Tree

Pour construire ce MPC Tree, il faut assurer qu’à chaque contrat corresponde une position de feuille unique. Supposons qu’on ait :
- `C` contrats à inclure, indexés par `i` dans `i = {0,1,..,C-1}` ;
- Pour chaque contrat `c_i`​, on dispose d’un identifiant `ContractId(i) = c_i`.

On va alors construire un arbre de largeur `w` et de profondeur `d` telle que `2^d = w`, avec `w > C`, de sorte que chaque contrat puisse être placé dans une _leaf_ distincte. La position `pos(c_i)` de chaque contrat dans l’arbre est déterminée par :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

où `cofactor` est un entier qui augmente les probabilités d’obtenir des positions distinctes pour chaque contrat. Dans la pratique, la construction suit un processus itératif :
- On part d’une profondeur minimale (`d=3` par convention pour masquer le nombre exact de contrats) ;
- On tente différents `cofactor` (jusqu’à `w/2`, ou un maximum de 500 pour des raisons de performance) ;
- Si on ne parvient pas à positionner tous les contrats sans collision, on incrémente `d` et on recommence.

Le but est d’éviter les arbres trop grands tout en maintenant un risque de collision minimal. Notons que le phénomène de collisions suit une logique de distribution aléatoire, liée au [Paradoxe des anniversaires](https://en.wikipedia.org/wiki/Birthday_problem).

#### Les feuilles habitées

Une fois `C` positions distinctes `pos(c_i)` obtenues pour les contrats `i = {0,1,..,C-1}`, on renseigne chaque feuille via une fonction de hachage (*tagged hash*) :

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

où :
- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, est toujours choisi selon les conventions Merkle de RGB ;
- `0x10` identifie un _contract leaf_ ;
- `c_i` est l’identifiant de 32 octets du contrat (issu du hash de sa Genesis) ;
- `BundleId(c_i)` est un hash de 32 octets décrivant l’ensemble des `State Transitions` relatives à `c_i` (réunies en une *Transition Bundle*).

#### Les feuilles inhabitées

Les feuilles restantes, non affectées à un contrat (c’est-à-dire `w - C` feuilles), sont remplies par une valeur dite "dummy" (_entropy leaf_) :

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

où :
- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, est toujours choisi selon les conventions Merkle de RGB ;
- `0x11` désigne une _entropy leaf_ ;
- `entropy` est une valeur aléatoire de 64 octets, choisie par la personne qui construit l’arbre ;
- `j` est la position (en 32 bits Little Endian) de cette feuille dans l’arbre.

#### Les nœuds MPC

Après avoir généré les `w` feuilles (habitées ou non), on procède à la merkelisation. Tout nœud interne est haché comme suit :

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

où :

- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, est toujours choisi selon les conventions Merkle de RGB ;
- `b` est la _branching factor_ (8 bits). Le plus souvent, `b=0x02` car l’arbre est binaire et complet ;
- `d` est la profondeur du nœud dans l’arbre ;
- `w` est la largeur de l’arbre (en binaire 256 bits Little Endian) ;
- `tH1` et `tH2` sont les hachages des nœuds enfants (ou feuilles), déjà calculés comme indiqués ci-dessus.

En progressant ainsi, on obtient la racine `mpc::Root`. On peut ensuite calculer `mpc::Commitment` (comme expliqué précédemment) et l’insérer on-chain.

Pour illustrer cela, imaginons un exemple où `C=3` (trois contrats). On suppose que leurs positions sont `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. Les autres feuilles (positions 0, 1, 3, 5, 6) sont des _entropy leaves_. Le schéma ci-dessous montre comment s’enchaînent les hachages jusqu’à la racine avec :
- `BUNDLE_i` qui représente `BundleId(c_i)` ;
- `tH_MPC_LEAF(A)` et ainsi de suite, qui représentent les feuilles (certaines pour les contrats, d’autres pour l’entropie) ;
- Chaque branche `tH_MPC_BRANCH(...)` qui combine les hachages de ses deux fils.

Le résultat final est le **mpc::Root**, puis le `mpc::Commitment`.

![RGB-Bitcoin](assets/fr/053.webp)

#### Vérification de l'arbre MPC

Lorsqu’un vérificateur souhaite s’assurer qu’un contrat `c_i`​ (et son `BundleId`) est bien inclus dans l’engagement final `mpc::Commitment`, il reçoit simplement une preuve de Merkle. Cette preuve indique les nœuds nécessaires pour remonter des feuilles (ici, la _contract leaf_ de `c_i`​) jusqu’à la racine. Inutile de divulguer l’intégralité du *MPC Tree* : cela protège la confidentialité des autres contrats.

Dans l’exemple, un vérificateur de `c_2` n’a besoin que d'un hachage intermédiaire (`tH_MPC_LEAF(D)`), de deux `tH_MPC_BRANCH(...)`, de la preuve de la position `pos(c_2)` et de la valeur `cofactor`. Il peut alors reconstruire localement la racine, puis recalculer le `mpc::Commitment` et le comparer à celui inscrit dans la transaction Bitcoin (au sein d’`Opret` ou de `Tapret`).

![RGB-Bitcoin](assets/fr/054.webp)

Ce mécanisme garantit ainsi que :
- L’état relatif à `c_2` est bien inclus dans le bloc d’information agrégé (client-side) ;
- Personne ne peut construire une histoire alternative avec la même transaction, car le _commitment_ on-chain pointe vers une unique racine MPC.

#### Résumé de la structure MPC

Le *Multi Protocol Commitment* (MPC) est donc le principe qui permet à RGB d’agréger plusieurs contrats dans une seule transaction Bitcoin, tout en maintenant l’unicité des engagements et la confidentialité vis-à-vis des autres participants. Grâce à la construction déterministe de l’arbre, chaque contrat se voit attribuer une position unique, et la présence de feuilles “dummy” (*Entropy Leaves*) masque partiellement le nombre total de contrats participant à l’opération.

Sur le client, on ne stocke jamais l’ensemble de l'arbre de Merkle. On se contente de générer, à l’instant T, un _Merkle path_ pour chaque contrat concerné, à transmettre au destinataire (qui pourra ainsi valider l’engagement). Dans certains cas, vous possédez plusieurs actifs passés par le même UTXO. Vous pouvez alors fusionner plusieurs _Merkle paths_ dans ce qu’on appelle un _multi-protocol commitment block_, afin d'éviter de dupliquer trop de données.

Chaque _Merkle proof_ est donc légère, d’autant plus que la profondeur de l’arbre n’excédera pas 32 dans RGB. Il existe également une notion de "Merkle block", qui conserve plus d’informations (la cross-section, l’entropie, etc.), utile pour combiner ou séparer plusieurs branches.

Voilà pourquoi la finalisation de RGB a demandé du temps. On avait la vision globale dès 2019 : tout mettre en client-side, faire circuler les tokens off-chain. Mais pour les détails comme le sharding pour plusieurs contrats, la structure de l'arbre de Merkle, la manière de gérer les collisions et la fusion de preuves… tout cela a exigé des itérations.

### Les anchors : un assemblage global

Dans la continuité de la construction de nos engagements (`Opret` ou `Tapret`) et de notre MPC (*Multi Protocol Commitment*), nous devons aborder la notion d’**Anchor** dans le protocole RGB. Un Anchor est une structure validée côté client qui rassemble les éléments nécessaires pour vérifier qu’un engagement Bitcoin renferme bien une information contractuelle précise. Autrement dit, un Anchor résume toutes les données utiles à la validation des _commitments_ décrits précédemment.

Un Anchor se compose de trois champs ordonnés :
- `Txid`
- `MPC Proof`
- `Extra Transaction Proof - ETP`

Chacun de ces champs intervient dans la procédure de validation, qu’il s’agisse de reconstituer la transaction Bitcoin sous-jacente ou de prouver l’existence d’un engagement caché (notamment dans le cas de `Tapret`).

#### TxId

Le champ `Txid` correspond à l’identifiant de 32 octets de la transaction Bitcoin qui contient l’engagement `Opret` ou `Tapret`.  

En théorie, il serait envisageable de retrouver ce `Txid` en retraçant la chaîne de transitions d'états qui pointent elles-mêmes vers chaque witness transaction, en suivant la logique des Single-use Seals. Cependant, pour faciliter et accélérer la vérification, ce `Txid` est tout simplement inclus dans l’Anchor, ce qui évite ainsi au validateur d’avoir à remonter tout l’historique off-chain.

#### MPC Proof

Le second champ, la `MPC Proof`, se rapporte à la preuve que ce contrat précis (par exemple `c_i`) est bien inclus dans le _Multi Protocol Commitment_. Il s’agit d’une combinaison de :
- `pos_i`, la position de ce contrat dans l’arbre du MPC ;
- `cofactor`, la valeur définie pour résoudre les collisions de positions ;
- la `Merkle Proof`, c’est-à-dire l’ensemble des nœuds et hachages permettant de reconstruire la racine du MPC et de vérifier que l’identifiant de contrat et son `Transition Bundle` sont bien engagés dans la racine.

Ce mécanisme a été décrit dans la section précédente consacrée à la construction du *MPC Tree*, où chaque contrat obtient une feuille unique grâce à l’opération :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

Puis, on utilise un schéma de merkelisation déterministe pour agréger toutes les feuilles (contrats + entropie). La `MPC Proof` permet, au final, de reconstituer localement la racine et de la comparer au `mpc::Commitment` inclus on-chain.

#### Extra Transaction Proof – ETP

Le troisième champ, l’**ETP**, dépend du type d’engagement utilisé. Si l’engagement est de type `Opret`, aucune preuve supplémentaire n’est requise. Le validateur inspecte la première sortie `OP_RETURN` de la transaction et y retrouve directement le `mpc::Commitment`.

**Si l’engagement est de type `Tapret`**, il faut fournir une preuve additionnelle appelée *Extra Transaction Proof – ETP*. Elle contient :
- La clé publique interne (`P`) de la sortie taproot dans laquelle est incrusté le *commitment* ;
- Les nœuds partenaires du `Script Path Spend` (lorsque le *commitment* Tapret est inséré dans un script), afin de prouver l’emplacement exact de ce script dans l’arbre taproot :
	- Si le *commitment* `Tapret` se trouve sur la branche de droite, on révèle le nœud de gauche (par exemple `tHABC`),
	- Si le *commitment* `Tapret` est sur la gauche, il faut divulguer 2 nœuds (par exemple `tHAB` et `tHC`) pour prouver qu’aucun autre *commitment* n’est présent sur la partie de droite.
- Le `nonce` éventuellement utilisé pour "miner" la meilleure configuration, permettant de placer le *commitment* à droite de l’arbre (optimisation de la preuve).

Cette preuve supplémentaire est indispensable, car, contrairement à `Opret`, l’engagement `Tapret` s’intègre dans la structure d’un script taproot, ce qui exige de révéler une partie de l’arbre taproot afin de valider correctement l’emplacement du *commitment*.

![RGB-Bitcoin](assets/fr/045.webp)

Les **Anchors** encapsulent donc l’ensemble des informations nécessaires pour valider un engagement Bitcoin dans le contexte de RGB. Ils indiquent à la fois la transaction pertinente (`Txid`) et les preuves de positionnement du contrat (`MPC Proof`), tout en gérant la preuve supplémentaire (`ETP`) dans le cas de `Tapret`. Ainsi, un Anchor protège l’intégrité et l’unicité de l’état off-chain en assurant qu’une même transaction ne puisse être réinterprétée pour d’autres données contractuelles.

### Conclusion

Dans ce chapitre, nous avons couvert :
- Comment appliquer le concept de Single-use Seals dans Bitcoin (en particulier via un _outpoint_) ;
- Les différentes méthodes pour insérer de façon déterministe un _commitment_ dans une transaction (Sig tweak, Key tweak, witness tweak, op_return, Taproot/Tapret) ;
- Les raisons pour lesquelles RGB se concentre sur les engagements Tapret ;
- La gestion multi-contrat via des _multi-protocol commitments_, indispensable pour ne pas exposer l’intégralité d’un état ou d’autres contrats lorsqu’on veut prouver un point précis ;
- Nous avons aussi vu le rôle des _Anchors_, qui rassemblent tout (le TXID de la transaction, la preuve de l’arbre de Merkle et la preuve Taproot) dans un même ensemble.

En pratique, la mise en œuvre technique est répartie entre plusieurs _crates_ Rust dédiés (dans _client_side_validation_, _commit-verify_, _bp_core_, etc.). Les notions fondamentales sont là :

![RGB-Bitcoin](assets/fr/046.webp)

Dans le chapitre suivant, nous étudierons la composante purement off-chain de RGB, à savoir la logique des contrats. Nous verrons comment les contrats RGB, organisés sous forme de _finite state machine_ partiellement répliquée, atteignent une expressivité bien plus élevée que celle autorisée par les scripts Bitcoin, tout en préservant la confidentialité de leurs données.

## Introduction aux contrats intelligents et à leurs états
<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

![video](https://youtu.be/tmAVdyXGmj4)

Dans ce chapitre et le prochain, nous allons aborder la notion de **smart contract** au sein de l’environnement RGB et nous allons étudier les différentes manières dont ces contrats peuvent définir et faire évoluer leur état (*state*). Nous verrons pourquoi l’architecture RGB, en utilisant la séquence ordonnée de Single-use Seals, permet d’exécuter divers types de ***Contract Operations*** de manière scalable et sans passer par un registre centralisé. Nous verrons également le rôle fondamental de la ***Business Logic*** pour encadrer l’évolution de l’état contractuel.

### Contrats intelligents et droits au porteur numériques

L’objectif de RGB est de proposer une infrastructure où l’on peut mettre en œuvre des smart contracts sur Bitcoin. Par "smart contract", on entend un accord entre plusieurs parties qui est automatiquement et informatiquement appliqué, sans intervention humaine pour faire respecter les clauses. En d’autres termes, la loi du contrat est exécutée par le logiciel, et non par un tiers de confiance.

Cette automatisation soulève la question de la décentralisation : comment s’affranchir d’un registre centralisé (par exemple une plateforme ou une base de données centrale) pour gérer la propriété et l’exécution des contrats ? L’idée d’origine, reprise par RGB, consiste à renouer avec un mode de possession dit **"au porteur"** (*bearer instruments*). Dans la tradition historique, certains titres (obligations, actions, etc.) étaient émis au porteur, permettant à quiconque possédait physiquement le document de faire valoir ses droits.  

![RGB-Bitcoin](assets/fr/055.webp)

RGB applique ce concept au monde numérique : les droits (et obligations) sont enfermés dans des données manipulées off-chain, et l’état de ces données est validé par les participants eux-mêmes. Cela permet, à priori, un degré de confidentialité et d’indépendance beaucoup plus grand que celui qu’offrent d’autres approches basées sur des registres publics.

### Introduction à l’État d’un Smart Contract RGB

Un smart contract dans RGB peut être vu comme une machine à états, définie par :
- Un **State** (état), c’est-à-dire l’ensemble d’informations reflétant la configuration actuelle du contrat ;
- Une **Business Logic** (ensemble de règles), qui décrit sous quelles conditions et par qui l’état peut être modifié.

![RGB-Bitcoin](assets/fr/056.webp)

Il est important de comprendre que ces contrats ne sont pas limités aux simples transferts de tokens. Ils peuvent incarner une grande variété d’applications : des actifs traditionnels (jetons, actions, obligations) jusqu’à des mécaniques plus complexes (droits d’usage, conditions commerciales, etc.). Contrairement à d’autres blockchains où le code du contrat est accessible et exécutable par tous, l’approche de RGB cloisonne l’accès et la connaissance du contrat aux participants ("***contract participants***"). Il existe ainsi plusieurs rôles :
- **L’issuer** ou créateur du contrat, qui définit la Genèse du contrat et ses variables initiales ;
- **Les parties détentrices** de droits (*ownership*) ou d’autres capacités d’exécution ;
- Des **observateurs**, potentiellement limités à voir certaines informations, mais qui ne peuvent pas déclencher des modifications.

Cette séparation des rôles contribue à la résistance à la censure, en permettant que seules les personnes autorisées puissent interagir avec l’état contractuel. Cela confère également à RGB la capacité de s’étendre de manière horizontale : la majorité des validations a lieu en dehors de la blockchain, et seules des ancrages cryptographiques (les *commitments*) sont inscrits sur Bitcoin.

### État et Business Logic dans RGB

D’un point de vue pratique, la **Business Logic** du contrat se présente sous forme de règles et de scripts, définis dans ce que RGB appelle un **Schema**. Le Schema encode :
- La structure de l’État (quels champs sont publics ? Quels champs sont détenus par telle ou telle partie ?) ;
- Les conditions de validité (qu’est-ce qui doit être vérifié avant d’autoriser une mise à jour de l’État ?) ;
- Les autorisations (qui peut initier une *State Transition* ? Qui peut seulement observer ?).

En parallèle, l’**État** (_Contract State_) se décompose souvent en deux volets :
- Un **Global State** : partie publique, potentiellement observable par tous (selon la configuration) ;
- Des **Owned States** : parties privées, attribuées spécifiquement à des détenteurs (*owners*) via des UTXOs référencés dans la logique du contrat.

Comme nous le verrons dans les chapitres suivants, toute mise à jour d’état (*Contract Operation*) doit s’arrimer à un _commitment_ Bitcoin (via `Opret` ou `Tapret`) et se conformer aux scripts de la *Business Logic* pour être considérée comme valide.

### Contract Operations : création et évolution de l’État

Dans l’univers RGB, on appelle ***Contract Operation*** tout événement qui fait passer le contrat d’un **ancien état** (_old state_) à un **nouvel état** (_new state_). Ces opérations suivent la logique suivante :
- On prend connaissance de l’État actuel du contrat ;
- On applique la règle ou l’opération (une ***State Transition***, une ***Genesis*** si c’est le tout premier état, ou encore une ***State Extension*** s’il y a une *valency* publique à redéclencher) ;
- On ancre la modification via un nouveau _commitment_ sur la blockchain, en fermant un _single-use seal_ et en en créant un autre ;
- Les détenteurs de droits concernés valident localement (*client-side*) que la transition est conforme au *Schema* et que la transaction Bitcoin associée est inscrite on-chain.

![RGB-Bitcoin](assets/fr/057.webp)

Le résultat final est un contrat mis à jour, dont l’État est désormais différent. Cette transition ne nécessite pas que l’ensemble du réseau Bitcoin s’intéresse aux détails, puisque seule une petite empreinte cryptographique (le _commitment_) est enregistrée dans la blockchain. La séquence des Single-use Seals prévient toute double-dépense ou double-utilisation de l’État.

### Chaîne d’opérations : de la Genesis au Terminal State

Pour remettre en perspective, un smart contract RGB démarre par une **Genesis**, le tout premier état. Par la suite, diverses Contract Operations se succèdent, formant un DAG (*Directed Acyclic Graph*) d’opérations :
- Chaque transition s’appuie sur un état précédent (ou plusieurs, en cas de transitions convergentes) ;
- L’ordre chronologique est garanti par l’inclusion de chaque transition dans un ancrage Bitcoin, horodaté et inaltérable grâce au consensus par Proof-of-Work ;
- Lorsque plus aucune opération n’est en cours, on atteint un **Terminal State** : la situation la plus récente et complète du contrat.

![RGB-Bitcoin](assets/fr/012.webp)

Cette topologie en DAG (au lieu d’une simple chaîne linéaire) reflète la possibilité que différentes parties du contrat puissent évoluer en parallèle, tant qu’elles ne se contredisent pas. RGB se charge alors d’éviter toute incohérence via la vérification *client-side* de chaque participant concerné.

### Synthèse

Les smart contracts dans RGB introduisent un modèle d’instruments au porteur numériques, décentralisés, mais ancrés dans Bitcoin pour l’horodatage et la garantie de l’ordre des opérations. L’exécution automatisée de ces contrats repose sur :
- Un **État** (*Contract State*), indiquant la configuration actuelle du contrat (droits, soldes, variables…) ;
- Une **Business Logic** (*Schema*), définissant quelles transitions sont autorisées et comment elles doivent être validées ;
- Des **Contract Operations**, qui mettent à jour cet État étape par étape, grâce à des engagements ancrés dans des transactions Bitcoin.

Dans le chapitre suivant, nous entrerons plus en détail dans la représentation concrète de ces ***states*** et des ***state transitions*** au niveau off-chain, ainsi que dans la manière dont ils se lient aux UTXOs et aux Single-use Seals ancrés dans Bitcoin. Ce sera l’occasion de voir comment la mécanique interne de RGB, fondée sur une validation client-side, parvient à maintenir la cohérence des smart contracts tout en préservant la confidentialité des données.


## Opérations des contrats RGB
<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

![video](https://youtu.be/lUTjeuM0oTA)

Dans ce chapitre, nous allons étudier le fonctionnement des opérations dans les contrats intelligents et des transitions d'état, toujours au sein du protocole RGB. Le but sera également de comprendre comment plusieurs participants coopèrent pour transférer la propriété d’un actif.

### Les transitions d'état et leurs mécaniques

Le principe général est toujours celui de la Client-side Validation, où les données de l’état sont conservées chez le propriétaire et validées par le destinataire. Toutefois, la spécificité ici avec RGB réside dans le fait que Bob, en tant que destinataire, demande à Alice d’incorporer certaines informations dans les données du contrat afin d’avoir un véritable contrôle sur l’actif reçu, via une référence cachée à l’un de ses UTXOs.

Pour illustrer le processus d’une *State Transition* (qui est l’une des ***Contract Operations*** fondamentales dans RGB), suivons pas à pas l’exemple d’un transfert d’actif entre Alice et Bob :

**Situation initiale :**
Alice dispose d’un ***stash RGB*** de données validées en local (*client-side*). Ce stash fait référence à l’un de ses UTXOs sur Bitcoin. Cela signifie qu’une définition de sceau (_seal definition_) pointe, dans ces données, vers un UTXO qui appartient à Alice. L’idée est de lui permettre de transférer à Bob certains droits numériques liés à un actif (par exemple des jetons RGB).

![RGB-Bitcoin](assets/fr/058.webp)

**Bob possède également des UTXOs :**
Bob, de son côté, détient au moins un UTXO qui lui est propre, sans lien direct avec celui d’Alice. Dans le cas où Bob ne posséderait pas d'UTXO, il reste tout de même envisageable de procéder au transfert à son bénéfice en utilisant la transaction témoin (*witness transaction*) elle-même : l’output de cette transaction inclura alors l’engagement (_commitment_) et associera implicitement la propriété du nouveau contrat à Bob.

![RGB-Bitcoin](assets/fr/059.webp)

**Construction de la nouvelle propriété (*New State*) :**
Bob envoie à Alice des informations encodées sous forme d’***invoice*** (nous détaillerons dans les prochains chapitres la construction de l'invoice) lui demandant de créer un nouvel état conforme aux règles du contrat. Cet état inclura une nouvelle *seal definition* pointant vers l’un des UTXOs de Bob. Ainsi, Bob se voit attribuer la propriété sur les actifs définis dans ce nouvel état, par exemple un certain montant de jetons RGB.

![RGB-Bitcoin](assets/fr/060.webp)

**Préparation de la transaction témoin :**
Alice crée ensuite une transaction Bitcoin dépensant l'UTXO référencé dans le sceau précédent (celui qui la légitimait comme détentrice). Dans la sortie de cette transaction, un *commitment* (via `Opret` ou `Tapret`) est inséré pour ancrer le nouvel état RGB. Les engagements `Opret` ou `Tapret` sont dérivés d’un *MPC tree* (comme vu dans les chapitres précédents), qui peut agréger plusieurs transitions de différents contrats.

**Transmission du *Consignment* à Bob :**
Avant de diffuser la transaction, Alice envoie à Bob un ***Consignment*** contenant l’intégralité des données *client-side* nécessaires (son *stash*) ainsi que les informations du nouvel état en faveur de Bob. À ce stade, Bob applique les règles de consensus RGB :
- Il valide toutes les données RGB contenues dans le *Consignment*, y compris le nouvel état qui lui octroie la propriété de l’actif ;
- En s’appuyant sur les *Anchors* inclus dans le *Consignment*, il vérifie la chronologie des transactions témoins (depuis la Genesis jusqu’à la transition la plus récente) et valide les engagements correspondants dans la blockchain.

**Finalisation de la transition :**
Si Bob est satisfait, il peut éventuellement donner son approbation (par exemple en signant le *consignment*). Alice peut alors diffuser la transaction témoin préparée. Une fois confirmée, celle-ci clos le sceau précédemment détenu par Alice et officialise la propriété par Bob. La sécurité anti double-dépense se base alors sur le même mécanisme que dans Bitcoin : l’UTXO est dépensé, ce qui prouve qu’Alice ne peut plus le réutiliser.

![RGB-Bitcoin](assets/fr/061.webp)
Le nouvel état référence désormais l'UTXO de Bob, ce qui confère à celui-ci la propriété que détenait précédemment Alice. La sortie Bitcoin où sont ancrées les données RGB devient la preuve irrévocable du transfert de propriété.

Un exemple de DAG (*Directed Acyclic Graph*) minimal comprenant deux opérations de contrat (une **Genesis** puis un ***State Transition***) peut illustrer comment l’état RGB (couche *client-side*, en rouge) se relie à la blockchain Bitcoin (couche *Commitment*, en orange).  

![RGB-Bitcoin](assets/fr/062.webp)

On y voit qu’une Genesis définit un sceau (*seal definition*), puis qu’une *State Transition* vient clore ce sceau pour en créer un nouveau dans un autre UTXO.

Dans ce contexte, voici quelques rappels de terminologie :
- Une ***Assignment*** associe :
    - Une ***Seal Definition*** (qui pointe vers un UTXO) ;
    - Des **Owned States**, c’est-à-dire des données liées à la propriété (par exemple, la quantité de tokens transférés).
- Un **Global State** rassemble des propriétés générales du contrat, visibles par tous, et assurant la cohérence globale des évolutions.

Les **State Transitions**, décrites dans le chapitre précédent, constituent la forme principale d’opérations de contrat. Elles se réfèrent à un ou plusieurs états antérieurs (issus de la Genesis ou d’une autre State Transition) et les mettent à jour vers un nouvel état.

![RGB-Bitcoin](assets/fr/063.webp)

Ce schéma montre comment, dans une *State Transition Bundle*, on peut clore plusieurs sceaux en une seule transaction témoin, en ouvrant simultanément de nouveaux sceaux. En effet, une caractéristique intéressante du protocole RGB est sa possibilité de passage à l'échelle : plusieurs transitions peuvent être agrégées dans un Transition Bundle, chaque agrégation étant associée à une feuille distincte du *MPC tree* (un identifiant de bundle unique). Grâce au mécanisme de *Deterministic Bitcoin Commitment* (DBC), l’ensemble du message est inséré dans une sortie `Tapret` ou `Opret`, tout en fermant les sceaux précédents et en définissant éventuellement de nouveaux sceaux. L’*Anchor* sert de lien direct entre l’engagement stocké dans la blockchain et la structure de validation côté client (*client-side*).

Nous étudierons dans les chapitre suivants tous les composants et les processus liés à la construction et à la validation d’une State Transition. La plupart de ces éléments relèvent du consensus RGB, implémenté dans la "**RGB Core Library**".

### Transition Bundle

Sur RGB, il est possible de regrouper différentes State Transitions appartenant au même contrat (c’est-à-dire partageant le même **ContractId**, dérivé du **OpId** de la Genesis). Dans le cas le plus simple, comme entre Alice et Bob dans l’exemple ci-dessus, un **Transition Bundle** ne contient qu’une seule transition. Mais la prise en charge des opérations multi-payer (comme par exemple des coinjoins, des ouvertures de canaux Lightning, etc.) permet à plusieurs utilisateurs de combiner leurs State Transitions en un seul bundle.

Une fois rassemblées, ces transitions sont ancrées (par le mécanisme MPC + DBC) dans une unique transaction Bitcoin :
- Chaque State Transition est hashée et regroupée en une Transition Bundle ;
- La Transition Bundle est elle-même hachée et insérée dans la feuille du MPC tree correspondant à ce contrat (un BundleId) ;
- Le MPC tree est finalement engagé via `Opret` ou `Tapret` dans la transaction témoin, qui ferme ainsi les sceaux consommés et définit les nouveaux sceaux.

Sur le plan technique, le **BundleId** inséré dans la feuille MPC est obtenu à partir d’un tagged hash appliqué à la sérialisation stricte du champ *InputMap* du bundle :

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

Dans lequel `bundle_tag = urn:lnp-bp:rgb:bundle#2024-02-03` par exemple.

L’*InputMap* est une structure de données qui répertorie, pour chaque entrée `i` de la transaction témoin, la référence à l’*OpId* de la State Transition correspondante. Par exemple :

```txt
InputMap =
         N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)    
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
 16-bit Little Endian   32-bit LE   32-byte hash                                         
                       |_________________________| |_________________________|  ...  |___________________________|
                               MapElement1                MapElement2                       MapElementN 
```

- `N` est le nombre total d’entrées de la transaction qui se réfèrent à un `OpId`;
- `OpId(input_j)` est l’identifiant d’opération d’une des State Transitions présentes dans le bundle.

En référençant chaque entrée une seule fois et de manière ordonnée, on empêche la double-dépense d’un même sceau dans deux State Transitions simultanées.

### State Generation et Active State

Les State Transitions permettent donc de transférer la propriété d’un actif d’une personne à une autre. Cependant, ce ne sont pas les seules opérations possibles dans le protocole RGB. Le protocole définit trois **Contract Operations** :
- **State Transition** ;
- **Genesis** ;
- **State Extension**.

Parmi celles-ci, **Genesis** et **State Extension** sont parfois appelées "*State Generation operations*", car elles créent de nouveaux états sans pour autant en refermer immédiatement. C’est d'ailleurs un point très important : **Genesis** et **State Extension** n’impliquent pas la fermeture d’un sceau. Elles définissent plutôt un nouveau sceau, qui devra ensuite être dépensé par une **State Transition** ultérieure pour être réellement validé dans l’historique de la blockchain.

![RGB-Bitcoin](assets/fr/064.webp)

On définit souvent l’**Active State** d’un contrat comme l’ensemble des derniers états résultant de l’historique (le DAG) des opérations, en commençant par la Genesis et en suivant tous les ancrages dans la blockchain Bitcoin. Tous les anciens états déjà obsolètes (c’est-à-dire attachés à des UTXOs dépensés) ne sont plus considérés comme actifs, mais restent indispensables pour vérifier la cohérence de l’historique.

### Genesis

La Genesis est le point de départ de tout contrat RGB. Elle est créée par l’émetteur du contrat et définit les paramètres initiaux, conformément au **Schema**. Dans le cas d’un token RGB, la Genesis peut spécifier, par exemple :
- La quantité de jetons créée à l’origine et leurs propriétaires ;
- Le plafond total d’émission possible ;
- Les éventuelles règles de réémission, et quels participants peuvent y prétendre.

Étant la première opération du contrat, la Genesis ne référence aucun état antérieur, ni ne ferme aucun sceau. Toutefois, pour apparaître dans l’historique et être validée, la Genesis doit être **consommée** (refermée) par une première State Transition (souvent une transaction de balayage / auto-spend vers l’émetteur lui-même ou bien la distribution initiale aux utilisateurs).

### State Extension

Les **State Extensions** offrent une fonctionnalité originale pour des smart contracts. Elles permettent de racheter certains droits numériques (*Valencies*) prévus dans la définition du contrat, sans fermer immédiatement le sceau. Le plus souvent, cela concerne :
- Des émissions distribuées de tokens ;
- Des mécanismes de swap entre actifs ;
- Des réémissions conditionnelles (pouvant inclure la destruction d’autres actifs, etc.).

Sur le plan technique, une State Extension référence un *Redeem* (un type particulier d’input RGB) qui correspond à une *Valency* définie précédemment (par exemple dans la Genesis ou dans une autre State Transition). Elle définit un nouveau sceau, à la disposition de la personne ou de la condition qui en bénéficie. Pour que ce sceau soit rendu effectif, il faudra qu’une State Transition ultérieure vienne le dépenser.

![RGB-Bitcoin](assets/fr/065.webp)

Par exemple : la Genesis crée un droit d’émission (*Valency*). Celui-ci peut être exercé par un acteur autorisé, qui construit alors une State Extension :
- Elle référence la Valency (redeem) ;
- Elle crée un nouvel *assignement* (nouvelles données *Owned State*) pointant vers un UTXO ;
- Une State Transition future, émise par le propriétaire de ce nouvel UTXO, viendra réellement transférer ou répartir les jetons nouvellement émis.

### Composants d’une Contract Operation

Maintenant, je vous propose d'examiner de manière détaillée chacun des éléments constitutifs d’une **Contract Operation** dans RGB. Une Contract Operation est l’action qui permet de modifier l’état d’un contrat, et dont la validation se fait côté client, de manière déterministe, par le destinataire légitime. Nous allons notamment voir comment la Contract Operation prend en compte, d’un côté, l’**ancien état** (*Old State*) du contrat, et de l’autre côté, la définition d’un **nouvel état** (*New State*).

```txt
               +---------------------------------------------------------------------------------------------------------------------+
               |  Contract Operation                                                                                                 |
               |                                                                                                                     |
               |  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |                             
               |  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |                               
               |  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |     
               |                                                                                                                     |
               |  +-----------------------------------------------+  +------------------------------------------------------------+  |
               |  | Metadata                                      |  | Global State                                               |  |
               |  |                                               |  | +----------------------------------+                       |  |
               |  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
               |  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
               |  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
               |  |                                               |  | +----------------------------------+                       |  |
               |  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
               |                                                                                                                     +---------> OpId |
               |  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
               |  | Inputs                                        |  | Assignments                                                |  |
               |  |                                               |  |                                                            |  |
               |  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
               |  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
               |  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |         
               |  |                                               |  |                                                            |  |         
               |  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |         
               |  | | Input #2                                  | |  | | Assignment #2                                          | |  |         
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
               |  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
               |  |                                               |  |                                                            |  |
               |  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
               |  |                                               |  |                                                            |  |
               |  +-----------------------------------------------+  +------------------------------------------------------------+  |
               |                                                                                                                     |
               |  +-----------------------------------------------+  +------------------------------------------------------------+  |
               |  | Redeems                                       |  | Valencies                                                  |  |
               |  |                                               |  |                                                            |  |            
               |  | +------------------------------+              |  |                                                            |  |   
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |            
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |    
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |    
               |  | +------------------------------+              |  |                                                            |  |   
               |  |                                               |  |                                                            |  |      
               |  +-----------------------------------------------+  +------------------------------------------------------------+  |    
               |                                                                                                                     |    
               +---------------------------------------------------------------------------------------------------------------------+
```

En observant le schéma ci-dessus, on note qu’une Contract Operation comporte des éléments se rapportant au **New State** et d’autres qui font référence à l’**Old State** mis à jour.

Les éléments du **New State** sont :
- Les **Assignments**, dans lesquels sont définis :
	- La **Seal Definition** ;
	- Les **Owned State**.
- Le **Global State**, qui peut être modifié ou enrichi ;
- Les **Valencies**, éventuellement définies dans une State Transition ou une Genesis.

L’**Old State** est référencé via :
- Les **Inputs**, qui pointent vers des *Assignments* de transitions d’état précédentes (pas présents dans la Genesis) ;
- Les **Redeems**, qui font référence à des Valencies antérieurement définies (uniquement dans les State Extensions).

Par ailleurs, une Contract Operation inclut des champs plus généraux, propres à l’opération :
- `Ffv` (*Fast-forward version*) : entier de 2 octets indiquant la version du contrat ;
- `TransitionType` ou `ExtensionType` : entier 16 bits spécifiant le type de Transition ou d’Extension, selon la logique métier ;
- `ContractId` : nombre de 32 octets renvoyant à l’*OpId* de la Genesis du contrat. Inclus dans les Transitions et Extensions, mais pas dans la Genesis ;
- `SchemaId` : présent uniquement dans la Genesis, c’est le hash de 32 octets représentant la structure (*Schema*) du contrat ;
- `Testnet` : booléen indiquant si l’on est sur le réseau Testnet ou Mainnet. Seulement dans la Genesis ;
- `Altlayers1` : variable identifiant la couche alternative (sidechain ou autre) utilisée pour ancrer les données en plus de Bitcoin. Présente uniquement dans la Genesis ;
- `Metadata` : champ pouvant stocker des informations temporaires, utiles à la validation d’un contrat complexe, mais qui ne doivent pas être enregistrées dans l’historique d’état final.

Enfin, tous ces champs sont condensés par un procédé de hachage personnalisé, afin de produire une empreinte unique, l’`OpId`. Cet `OpId` est ensuite intégré au Transition Bundle, ce qui permettra de l’authentifier et de le valider au sein du protocole.

Chaque *Contract Operation* est donc identifiée par un hash de 32 octets nommé `OpId`. Ce hash est calculé par un hachage SHA256 de l’ensemble des éléments composant l’opération. Autrement dit, chaque *Contract Operation* dispose de son propre engagement cryptographique, qui inclut toutes les données permettant de vérifier l’authenticité et la cohérence de l’opération.

Un contrat RGB est ensuite identifié par un `ContractId`, dérivé de l’`OpId` de la Genesis (puisqu’il n’y a pas d’opération antérieure à la Genesis). Concrètement, on prend l’`OpId` de la Genesis, on en inverse l’ordre des octets et on applique un encodage Base58. Cet encodage rend le `ContractId` plus facilement manipulable et reconnaissable.

### Méthodes et règles de mise à jour de l’état

Le **Contract State** représente l’ensemble des informations que le protocole RGB doit suivre pour un contrat donné. Il se compose :
- **D’un seul Global State** : c’est la partie publique et globale du contrat, visible par tous ;
- **D’un ou plusieurs Owned State** : chaque Owned State est associé à un sceau unique (et donc à un UTXO sur Bitcoin). On distingue :
    - Les Owned States **publics**,
    - Les Owned States **privés**.

![RGB-Bitcoin](assets/fr/066.webp)

Le *Global State* est directement inclus dans la *Contract Operation* sous la forme d’un bloc unique. Les *Owned States* sont, eux, définis dans chaque *Assignment*, à côté de la *Seal Definition*.

Une particularité majeure de RGB est la manière dont on modifie le Global State et les Owned States. On distingue généralement deux comportements :
- **Mutable** : lorsqu’un élément d’état est décrit comme mutable, chaque nouvelle opération remplace l’état précédent par un nouvel état. L’ancienne donnée est alors considérée comme obsolète ;
- **Accumulating** : lorsqu’un élément d’état est défini comme cumulatif, chaque nouvelle opération vient ajouter une information supplémentaire à l’état précédent, sans l’écraser. On obtient ainsi une sorte d’historique accumulé.

Si, dans le contrat, un élément d’état n’est pas défini comme mutable ou cumulatif, cet élément restera vide pour les opérations ultérieures (autrement dit, il n’y a aucune nouvelle version pour ce champ). C'est le Schema du contrat (c’est-à-dire la logique métier codée) qui détermine si un état (Global ou Owned) est mutable, cumulatif ou fixe. Une fois la Genesis définie, ces propriétés ne peuvent être modifiées que si le contrat lui-même l’autorise, par exemple via une State Extension spécifique.

Le tableau ci-dessous illustre comment chaque type de Contract Operation peut manipuler (ou non) le Global State et l’Owned State :

|                              | Genesis | State Extension | State Transition |
| ---------------------------- | :-----: | :-------------: | :--------------: |
| **Ajout de Global State**    |    +    |        -        |        +         |
| **Mutation de Global State** |   n/a   |        -        |        +         |
| **Ajout de Owned State**     |    +    |        -        |        +         |
| **Mutation de Owned State**  |   n/a   |       Non       |        +         |
| **Ajout de Valencies**       |    +    |        +        |        +         |

**`+`** : action possible si le Schema du contrat le permet.
**`-`** : l’opération doit être confirmée par une State Transition ultérieure (la State Extension, seule, ne ferme pas le Single-use Seal).

Par ailleurs, on peut distinguer la portée temporelle et les droits de mise à jour de chaque type de données dans le tableau suivant :

|                                 | Metadata                                 | Global State                                   | Owned State                                                                                                  |
| ------------------------------- | ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Portée**                      | Défini pour une seule Contract Operation | Défini globalement pour le contrat             | Défini pour chaque sceau (*Assignment*)                                                                      |
| **Qui peut le mettre à jour ?** | Non réactualisable (données éphémères)   | Opération émise par les acteurs (issuer, etc.) | Dépend du détenteur légitime qui possède le sceau (celui qui peut le dépenser dans une transaction suivante) |
| **Portée temporelle**           | Juste pour l’opération en cours          | L’état est établi à l’issue de l’opération     | L’état est défini avant l’opération (par la *Seal Definition* de l’opération précédente)                     |

### Global State

Le Global State se décrit souvent par la formule : "*personne ne possède, tout le monde sait*". Il contient des informations générales sur le contrat, visibles publiquement. Par exemple, dans un contrat d’émission de jetons, on y retrouve potentiellement :
- Le ticker (abréviation symbolique du jeton) : `ticker` ;
- Le nom complet du jeton : `name` ;
- La précision (nombre de décimales) : `precision` ;
- L’offre initiale (et/ou la limite maximale de tokens) : `issuedSupply` ;
- La date d’émission : `created` ;
- Des données légales ou tout autre information publique : `data`.

Ce Global State peut être placé sur des ressources publiques (sites web, IPFS, Nostr, Torrent, etc.) et diffusé auprès de la communauté. Aussi, l’incitation économique (le besoin de détenir et de transférer ces tokens, etc.) pousse naturellement les utilisateurs du contrat à maintenir eux-mêmes et à propager ces données.

### Assignments

L’*Assignment* est la structure de base permettant de définir :
- Le sceau (*Seal Definition*), qui pointe vers un UTXO spécifique ;
- L'*Owned State*, c’est-à-dire la propriété ou les données associées à ce sceau.

On peut voir un *Assignment* comme l’analogue d’une sortie de transaction Bitcoin, mais avec plus de flexibilité. C’est ici que réside la logique de transfert de propriété : l’*Assignment* associe un type particulier d’actif ou de droit (`AssignmentType`) à un sceau. Quiconque possède la clé privée de l’UTXO lié à ce sceau (ou qui peut dépenser cet UTXO) est considéré comme le propriétaire de cet *Owned State*.

Une des grandes forces de RGB réside dans la possibilité de révéler (*reveal*) ou de cacher (*conceal*) à volonté les champs du *Seal Definition* et de l’*Owned State*. Cela offre une combinaison poussée de confidentialité et de sélectivité. Par exemple, on peut prouver qu’une transition est valide sans divulguer la totalité des données, dès lors qu’on fournit la version révélée à celui qui doit la valider, tandis que les tiers ne voient que la version cachée (un hash). Dans la pratique, l’`OpId` d’une transition est toujours calculé à partir des données cachées (*concealed*).

![RGB-Bitcoin](assets/fr/067.webp)

#### Seal Definition

La *Seal Definition*, dans sa forme révélée, comporte quatre champs de base : `txptr`, `vout`, `blinding` et `method` :
- **txptr** : c'est une référence à un UTXO sur Bitcoin :
    - Dans le cas d’un **Genesis seal**, on pointe directement vers un UTXO existant (celui associé à la Genesis) ;
    - Dans le cas d’un **Graph seal**, on peut avoir :
        - Un simple `txid`, si on pointe vers un UTXO précis,
        - Ou un `WitnessTx`, qui désigne une auto-référence : le sceau pointe vers la transaction elle-même. Cela sert notamment quand aucun UTXO externe n’est disponible, par exemple dans des transactions d’ouverture de canal Lightning ou si le destinataire ne possède pas d’UTXO.
- **vout** : le numéro de sortie de la transaction indiquée par `txptr`. Présent uniquement pour un Graph seal standard (pas pour le `WitnessTx`) ;
- **blinding** : un nombre aléatoire de 8 octets, qui permet de renforcer la confidentialité pour éviter les tentatives de brute force sur l’identité de l’UTXO ;
- **method** : indique la méthode d’ancrage utilisée (`Tapret` ou `Opret`).

La forme cachée (*concealed*) de la Seal Definition est un hash SHA256 (tagged) de la concaténation de ces 4 champs, avec un tag spécifique à RGB.

![RGB-Bitcoin](assets/fr/068.webp)

#### Owned States

Le second composant de l’*Assignment* est l’Owned State. Contrairement au Global State, il peut exister sous forme publique ou privée :
- **Public Owned State** : tout le monde connaît la donnée associée au sceau. Par exemple, une image publique ;
- **Private Owned State** : la donnée est cachée, seul le propriétaire (et potentiellement le validateur si nécessaire) la connaît. Par exemple, la quantité de jetons détenue.

RGB définit quatre types d’état (*StateTypes*) possibles pour un Owned State :
- **Declarative** : ne contient aucune donnée numérique, c’est juste un droit déclaratif (par exemple un droit de vote). La forme cachée et la forme révélée sont identiques ;
- **Fungible** : représente une quantité fongible (comme des jetons). En forme révélée, on a `amount` et `blinding`. En forme cachée, on a un unique *Pedersen commitment* qui dissimule le montant et le blinding ;
- **Structured** : permet de stocker des données structurées (jusqu’à 64 Kio). En forme révélée, c’est le blob de données. En forme cachée, c’est un hash tagué de ce blob :

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

Avec par exemple :

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```

- **Attachments** : permet de relier un fichier (audio, image, binaire, etc.) à l’Owned State, en stockant le hash du fichier `file_hash`, le type MIME `media type` et un sel cryptographique `salt`. Le fichier lui-même est hébergé ailleurs. En forme cachée, c’est un hash tagué des trois données précédentes :

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

Avec par exemple :

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

Pour résumer, voici les 4 types d'états possibles dans la forme publique et cachée :

```txt
  State                      Concealed form                              Revealed form

+---------------------------------------------------------------------------------------------------------

                     +--------------------------------------------------------------------------------+
                     |                                                                                |
  Declarative        |                              < void >                                          |
                     |                                                                                |
                     +--------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------

                     +--------------------------+             +---------------------------------------+
                     | +----------------------+ |             |         +--------+ +----------+       |
  Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
                     | +----------------------+ |             |         +--------+ +----------+       |
                     +--------------------------+             +---------------------------------------+

+---------------------------------------------------------------------------------------------------------

                     +--------------------------+             +---------------------------------------+
                     | +----------------------+ |             |         +--------------------+        |
  Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
                     | +----------------------+ |             |         +--------------------+        |
                     +--------------------------+             +---------------------------------------+

+---------------------------------------------------------------------------------------------------------

                     +--------------------------+             +---------------------------------------+
                     | +----------------------+ |             | +-----------+ +------------+ +------+ |
  Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
                     | +----------------------+ |             | +-----------+ +------------+ +------+ |
                     +--------------------------+             +---------------------------------------+

```

| **Élément**           | **Déclaratif** | **Fongible**                         | **Structuré**                 | **Pièces jointes**           |
| --------------------- | -------------- | ------------------------------------ | ----------------------------- | ---------------------------- |
| **Données**           | Aucune         | Entier signé ou non signé de 64 bits | Tout type de données strictes | Tout fichier                 |
| **Type d'info**       | Aucune         | Signé ou non signé                   | Types stricts                 | Type MIME                    |
| **Confidentialité**   | Non requise    | Pedersen commitment                  | Hachage avec blinding         | Identifiant de fichier haché |
| **Limites de taille** | N/A            | 256 octets                           | Jusqu’à 64 Ko                 | Jusqu’à ~500 Go              |

### Inputs

Les Inputs d’une *Contract Operation* font référence aux *Assignments* qui sont en train d’être dépensés dans cette nouvelle opération. Un Input indique :
- `PrevOpId` : l’identifiant (`OpId`) de l’opération précédente où se trouvait l’*Assignment* ;
- `AssignmentType` : le type d’*Assignment* (par exemple, `assetOwner` pour un token) ;
- `Index` : l’index de l’*Assignment* dans la liste associée à l’`OpId` précédent, déterminé après un tri lexicographique des sceaux cachés.

Les Inputs n’apparaissent jamais dans la Genesis, puisqu’il n’y a pas d’Assignments antérieurs. Ils n’apparaissent pas non plus dans les State Extensions (car ces dernières ne ferment pas de sceau ; elles redéfinissent plutôt de nouveaux sceaux en se basant sur des Valencies).

Lorsqu’on a des Owned States de type `Fungible`, la logique de validation (via l’AluVM script prévu dans le Schema) vérifie la cohérence des sommes : la somme de jetons entrants (*Inputs*) doit être égale à la somme de jetons sortants (dans les nouveaux *Assignments*).

### Metadata

Le champ **Metadata** peut aller jusqu’à 64 KiB et sert à inclure des données temporaires utiles à la validation, mais sans être intégrées dans l’état permanent du contrat. Par exemple, on peut y stocker des variables de calcul intermédiaires pour des scripts complexes. Cet espace n’est pas destiné à être conservé dans l’historique global, ce qui explique pourquoi il se trouve hors du périmètre des Owned States ou du Global State.

### Valencies

Les **Valencies** sont un mécanisme original du protocole RGB. On peut les rencontrer dans la Genesis, les State Transitions ou les State Extensions. Elles représentent des droits numériques activables par une State Extension (via des *Redeems*), puis finalisés par une Transition ultérieure. Chaque Valency est identifiée par un `ValencyType` (16 bits). Sa sémantique (droit de réémission, swap de jetons, droit de burn, etc.) est définie dans le Schema.

Concrètement, on peut imaginer qu’une Genesis définisse une valency "droit de réémission". Une State Extension viendra la consommer (*Redeem*) si certaines conditions sont remplies, afin d’introduire une nouvelle quantité de jetons. Puis, une State Transition émanant du détenteur du sceau ainsi créé pourra transférer ces nouveaux jetons.

### Redeems

Les Redeems sont l’équivalent, pour les Valencies, de ce que sont les Inputs pour les Assignments. Ils n’apparaissent que dans les State Extensions, car c’est là qu’on active une Valency préalablement définie. Un Redeem comporte deux champs :
- `PrevOpId` : l’`OpId` de l’opération où la Valency a été spécifiée ;
- `ValencyType` : le type de Valency que l’on souhaite activer (chaque `ValencyType` ne peut être consommé qu’une seule fois par State Extension).

Exemple : un Redeem peut correspondre à une exécution de CoinSwap, suivant ce qui était codé dans la Valency.

### Caractéristiques de l'état RGB

Nous allons maintenant étudier plusieurs caractéristiques fondamentales de l’état dans RGB. Nous allons notamment voir ce que sont :
- Le **Strict Type System**, qui impose une organisation précise et typée des données ;
- L’importance de la séparation entre **validation** et **propriété** ;
- Le système d’**évolution du consensus** dans RGB, qui inclut les notions de *fast-forward* et de *push-back*.

Comme à chaque fois, gardez à l’esprit que tout ce qui concerne l’état du contrat est validé côté client selon des règles de consensus énoncées dans le protocole, et dont l’ultime référence cryptographique est ancrée dans des transactions Bitcoin.

#### Strict Type System

RGB utilise un *Strict Type System* et un mode de sérialisation déterministe (*Strict Encoding*). Cette organisation est conçue pour garantir une reproductibilité et une précision parfaite dans la définition, la manipulation et la validation des données du contrat.

Dans de nombreux environnements de programmation (JSON, YAML…), la structure des données peut être flexible, voire trop permissive. Dans RGB, au contraire, la Structure et les Types de chaque champ sont définis avec des contraintes explicites. Ainsi :
- Chaque variable possède un type précis (par exemple un entier non signé sur 8 bits `u8`, ou un entier signé sur 16 bits, etc.) ;
- Les types peuvent se composer (types imbriqués). On peut ainsi définir un type basé sur d’autres types (exemple : un type agrégé qui contient un champ `u8`, un champ `bool`, etc.) ;
- On peut également spécifier des collections : listes (*list*), ensembles (*set*) ou dictionnaires (*map*), avec un ordre de parcours déterministe ;
- Chaque champ est borné (*lower bound* / *upper bound*). On impose également des bornes au nombre d’éléments dans les collections (confinement) ;
- Les données sont alignées sur l’octet et la sérialisation se fait de manière strictement définie, sans ambiguïté.

Grâce à ce protocole d’encodage strict :
- L’ordre des champs est toujours le même, indépendamment de l’implémentation ou du langage de programmation utilisé ;
- Les hash calculés sur un même ensemble de données sont donc reproductibles et identiques (*commitments* strictement déterministes) ;
- Les bornes évitent la croissance incontrôlée de la taille des données (ex. nombre de champs trop élevé) ;
- Cette forme d’encodage facilite la vérification cryptographique, car chaque participant sait exactement comment sérialiser et hacher les données.

En pratique, la structure (*Schema*) et le code qui en découle (*Interface* et logique associée) sont compilés. Il existe un langage descriptif qui précise la définition du contrat (types, champs, règles) et génère un format binaire strict. À la compilation, on obtient :
- Un *Memory Layout* (la disposition en mémoire de chaque champ) ;
- Des identifiants sémantiques (qui indiquent si le changement d’un nom de variable a un impact sur la logique, même si la structure mémoire reste la même).

Le système de types stricts permet aussi de faire un suivi précis des évolutions : toute modification de la structure (même un changement de nom de champ) est détectable et peut entraîner un changement de l’empreinte globale.

Enfin, chaque compilation produit une empreinte, un identifiant cryptographique qui atteste de la version exacte du code (données, règles, validation). Par exemple un identifiant de la forme :

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

Cela permet de gérer les mises à jour de consensus ou d’implémentation, tout en assurant une traçabilité fine des versions employées dans le réseau.

Pour éviter que l’état d’un contrat RGB ne devienne trop lourd à valider côté client, une règle de consensus impose une taille maximale de `2^16` octets (64 Kio) pour toute donnée impliquée dans les calculs de validation. Cela concerne chaque variable ou structure : pas plus de 65536 octets, ou l’équivalent en nombres (32768 entiers de 16 bits, etc.). Cela concerne également les collections (listes, sets, maps), qui ne peuvent dépasser `2^16` éléments.

Cette limite garantit :
- Un contrôle sur la taille maximale des données à manipuler lors d’une transition d’état ;
- Une compatibilité avec la machine virtuelle (*AluVM*) utilisée pour exécuter les scripts de validation.

#### Le paradigme Validation != Ownership

L’une des innovations majeures de RGB est la séparation stricte entre deux concepts :
- La **validation** : le fait de vérifier qu’une transition d’état respecte les règles du contrat (logique métier, historique, etc.) ;
- L’**ownership** (la propriété, ou le contrôle) : le fait de posséder l’UTXO Bitcoin qui permet de dépenser (ou fermer) le Single-use Seal et donc de réaliser la transition d’état.

La **Validation** se fait au niveau de la pile logicielle RGB (les bibliothèques, le protocole de *commitments*, etc.). Son rôle est de s’assurer que les règles internes au contrat (montants, permissions, etc.) sont bien respectées. Les observateurs ou les autres participants peuvent aussi valider l’historique des données.

L’**Ownership**, elle, repose totalement sur la sécurité de Bitcoin. Posséder la clé privée d’un UTXO, c’est contrôler la capacité de lancer une nouvelle transition (fermer le Single-use Seal). Ainsi, même si quelqu’un peut voir ou valider les données, il ne peut pas modifier l’état s’il ne détient pas l’UTXO concerné.

![RGB-Bitcoin](assets/fr/069.webp)

Cette approche limite les vulnérabilités classiques rencontrées dans les blockchains plus complexes (où tout le code d’un smart contract est public et modifiable par n’importe qui, ce qui a parfois mené à des hacks). Sur RGB, un attaquant ne peut pas simplement interagir avec l’état on-chain, car le droit d’agir sur l’état (*ownership*) est protégé par la couche Bitcoin.

De plus, ce découplage permet à RGB de s’intégrer naturellement avec le Lightning Network. Les canaux Lightning peuvent servir à engager et à déplacer les actifs RGB sans engager à chaque fois les *commitments* on-chain. Nous étudierons plus précisément cette intégration de RGB sur Lightning dans les prochains chapitres de la formation.

#### Évolutions de consensus dans RGB

Outre le versioning sémantique du code, RGB inclut un système permettant de faire évoluer ou de mettre à jour les règles de consensus d’un contrat au fil du temps. On distingue deux grandes formes d’évolution :
- **Fast-forward**
- **Push-back**

Un fast-forward survient lorsqu’une règle auparavant non valide devient valide. Par exemple, si le contrat évolue pour autoriser un nouveau type d’`AssignmentType` ou un nouveau champ :
- On ne peut pas comparer cela à un hardfork de blockchain classique, car RGB fonctionne en validation côté client et n’affecte pas la compatibilité globale de la blockchain ;
- Sur le plan pratique, ce type de changement est indiqué par le champ `Ffv` (*fast-forward version*) dans l’opération du contrat ;
- Les détenteurs actuels ne sont pas lésés : leur état reste valide ;
- Les nouveaux bénéficiaires (ou nouveaux utilisateurs) doivent en revanche mettre à jour leur logiciel (leur wallet) afin de reconnaître les nouvelles règles.

Un push-back signifie qu’une règle jusque-là valide devient invalide. C'est donc un "durcissement" des règles, mais ce n’est pas à proprement parler un softfork :
- Les détenteurs existants peuvent être impactés (ils pourraient se retrouver avec des actifs rendus obsolètes ou invalides dans la nouvelle version) ;
- On peut considérer qu’on crée en fait un nouveau protocole : celui qui adopte la nouvelle règle s’écarte de l’ancien ;
- L’issuer peut décider de réémettre les actifs dans ce nouveau protocole, obligeant les utilisateurs à tenir deux wallets distincts (l’un pour l’ancien protocole, l’autre pour le nouveau), s’ils veulent gérer les deux versions.

Dans ce chapitre consacré aux opérations des contrats RGB, nous avons exploré les principes fondamentaux qui sous-tendent ce protocole. Comme vous l'avez remarqué, la complexité inhérente du protocole RGB implique l'usage de nombreux termes techniques. Ainsi, dans le prochain chapitre, je vous propose un glossaire qui récapitulera tous les concepts abordés dans cette première partie théorique, avec les définitions de tous les termes techniques relatifs à RGB. Ensuite, dans la partie suivante, nous aborderons de manière pratique la définition et l'implémentation des contrats RGB.


## Glossaire RGB
<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

En cas de besoin dans la formation, vous pouvez revenir sur ce petit glossaire des termes techniques importants employés dans l'univers RGB (classés par ordre alphabétique). Ce chapitre n'est donc pas indispensable si vous avez déjà bien compris tout ce que nous avons vu dans la première section.

#### AluVM

L’abréviation AluVM désigne "_Algorithmic logic unit Virtual Machine_", une machine virtuelle à registres, conçue pour la validation de smart contracts et le calcul distribué. Elle est utilisée (sans y être exclusivement réservée) dans le cadre de la validation des contrats RGB. Les scripts ou les opérations inscrites dans un contrat RGB peuvent ainsi être exécutés dans l’environnement AluVM.  
Pour plus d’informations : [Site officiel d’AluVM](https://www.aluvm.org/)

#### Anchor

Un Anchor représente un ensemble de données côté client permettant de prouver l’inclusion d’un _commitment_ unique dans une transaction. Dans le protocole RGB, un Anchor est constitué des éléments suivants :
- L’identifiant de la transaction Bitcoin (TXID) de la **witness transaction** ;
- Le **Multi Protocol Commitment (MPC)** ;
- Le **Deterministic Bitcoin Commitment (DBC)** ;
- L’**Extra Transaction Proof (ETP)** si l’on emploie le mécanisme de commitment **Tapret** (voir la section dédiée à ce modèle).

Un Anchor sert donc à établir un lien vérifiable entre une transaction Bitcoin précise et des données privées validées par le protocole RGB. Il garantit que ces données sont bel et bien incluses dans la blockchain, sans pour autant que leur contenu exact soit exposé publiquement.

#### Assignment

Dans la logique de RGB, un Assignment est l’équivalent d’une sortie de transaction (output) qui modifie, met à jour ou crée certaines propriétés au sein de l’état d’un contract. Un Assignment comporte deux éléments :
- Une **Seal Definition** (la référence à un UTXO précis) ;
- Un **Owned State** (les données décrivant l’état associé à ce nouveau détenteur).

Un Assignment indique donc qu’une portion de l’état (par exemple, un actif) est désormais allouée à un détenteur particulier, identifié via un Single-use Seal lié à un UTXO.

#### Business Logic

La Business Logic regroupe l’ensemble des règles et des opérations internes d’un contrat, décrites par son **schéma** (c’est-à-dire la structure même du contrat). Elle dicte la manière dont l’état du contrat peut évoluer et sous quelles conditions.

#### Client-side Validation

La Client-side Validation renvoie au processus par lequel chaque partie (client) vérifie un ensemble de données échangées en privé, selon les règles d’un protocole. Dans le cas de RGB, ces données échangées sont regroupées dans ce qu’on appelle des **consignments**. Contrairement au protocole Bitcoin qui exige que toutes les transactions soient publiées on-chain, RGB permet de ne stocker en public que des _commitments_ (ancrés dans Bitcoin), tandis que l’essentiel des informations de contrat (transitions, attestations, preuves) reste off-chain, partagé seulement entre les utilisateurs concernés.

#### Commitment

Un Commitment (au sens cryptographique) est un objet mathématique, noté `C`, dérivé de façon déterministe à partir d’une opération sur une donnée structurée `m` (le message) et d’une valeur aléatoire `r`. On écrit :
$$
C = \text{commit}(m, r)
$$

Ce mécanisme comprend deux opérations principales :
- **Commit** : on applique une fonction cryptographique à un message `m` et à un aléa `r` pour produire `C` ;
- **Verify** : on utilise `C`, le message `m` et la valeur `r` pour vérifier que ce commitment est correct. La fonction renvoie `Vrai` ou `Faux`.

Un commitment doit respecter deux propriétés :
- **Binding** : il doit être impossible de trouver deux messages différents produisant le même `C` :
$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad 
$$
Tels que :
$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$

- **Hiding** : la connaissance de `C` ne doit pas révéler le contenu de `m`.

Dans le protocole RGB, un commitment est inclus dans une transaction Bitcoin afin de prouver l’existence d’une certaine information à un instant donné, sans dévoiler cette information elle-même.

#### Consignment

Un **Consignment** regroupe les données échangées entre les parties, soumises à la Client-side Validation dans RGB. Il existe deux grandes catégories de consignments :
- **Contract Consignment** : fourni par l’*issuer* (émetteur du contrat), il comprend les informations d’initialisation telles que le Schema, la Genesis, l’Interface et l’Implementation de l'Interface.
- **Transfer Consignment** : fourni par la partie qui paie (*payer*). Il contient tout l’historique de transitions d’état aboutissant au terminal consignment (c’est-à-dire l’état final reçu par le payeur).

Ces consignments ne sont pas enregistrés publiquement dans la blockchain ; ils sont échangés directement entre les parties concernées sur le canal de communication de leur choix.

#### Contract

Un Contract désigne un ensemble de droits exécutés numériquement entre plusieurs acteurs via le protocole RGB. Il possède un état actif et une logique d’affaires, définie par un Schema, qui précise quelles opérations sont autorisées (transferts, extensions, etc.). L’état d’un contrat, ainsi que les règles de validité, s’expriment dans le Schema. À tout moment, le contrat n’évolue que conformément à ce qui est permis par ce Schema et par les scripts de validation (exécutés, par exemple, dans AluVM).

#### Contract Operation

Une Contract Operation est une mise à jour de l’état du contrat effectuée selon les règles du Schema. Les opérations suivantes existent dans RGB :
- **State Transition** ;
- **Genesis** ;
- **State Extension**.

Chaque opération modifie l’état en y ajoutant ou en y remplaçant certaines données (Global State, Owned State…).

#### Contract Participant

Un Contract Participant est un acteur prenant part aux opérations relatives au contrat. Dans RGB, on distingue :
- L’issuer du contrat, qui crée la Genesis (l’origine du contrat) ;
- Les contract parties, c’est-à-dire les détenteurs de droits sur l’état du contrat ;
- Les public parties, acteurs pouvant construire des State Extensions si le contrat propose des Valencies accessibles au public.

#### Contract Rights

Les Contract Rights désignent les différents droits que peuvent exercer les acteurs d’un contrat RGB. Ils se classent en plusieurs catégories :
- Les **ownership rights**, associés à la détention d’un UTXO particulier (via un _Seal Definition_) ;
- Les **executive rights**, c’est-à-dire la capacité de construire une ou plusieurs transitions (State Transitions) conformes au Schema ;
- Les **public rights**, lorsque le Schema autorise certains usages publics, par exemple la création d’une State Extension via la rédemption d’une Valency.

#### Contract State

Le Contract State correspond à l’état courant d’un contrat à un instant donné. Il peut être constitué de données à la fois publiques et privées, qui reflète la situation du contrat. Dans RGB, on distingue :
- Le **Global State**, qui comprend les propriétés publiques du contrat (mises en place dès la Genesis ou ajoutées via des mises à jour autorisées) ;
- Les **Owned States**, qui appartiennent à des détenteurs précis, identifiés par leurs UTXOs.

#### Deterministic Bitcoin Commitment - DBC

Le Deterministic Bitcoin Commitment (DBC) est l’ensemble de règles permettant d’inscrire de manière prouvable et unique un _commitment_ dans une transaction Bitcoin. Dans le protocole RGB, il existe deux formes principales de DBC :
- **Opret**
- **Tapret**

Ces mécanismes définissent précisément comment le _commitment_ est encodé dans les sorties ou dans la structure d’une transaction Bitcoin, afin de s’assurer que cet engagement est repérable et vérifiable de façon déterministe.

#### Directed Acyclic Graph - DAG

Un DAG (ou *Graphe Orienté Acyclique*) est un graphe sans cycle, permettant un ordonnancement topologique. Les blockchains, tout comme les _shards_ de contrats RGB, peuvent être représentés par des DAGs.

Pour plus d’informations : [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### Engraving

Un Engraving est une chaîne de données optionnelle que les détenteurs successifs d’un contrat peuvent inscrire dans l’historique du contrat. Cette fonctionnalité existe, par exemple, dans l’interface **RGB21** et permet d’ajouter des informations commémoratives ou descriptives dans l’historique du contrat.

#### Extra Transaction Proof - ETP

L’ETP (*Extra Transaction Proof*) est la partie de l’Anchor qui renferme les données supplémentaires nécessaires à la validation d’un *commitment* de type **Tapret** (dans le contexte de _taproot_). Elle comprend, entre autres, la clé publique interne du script taproot (_internal PubKey_) et les informations spécifiques au _Script Path Spend_.

#### Genesis

La Genesis désigne l’ensemble des données, régies par un Schema, qui forment l’état initial de tout contrat dans RGB. On peut la rapprocher du concept de _Genesis Block_ (le bloc originel) sur Bitcoin, ou bien au concept de transaction Coinbase, mais ici au niveau _client-side_ et des jetons RGB.

#### Global State

Le Global State est l’ensemble des propriétés publiques contenues dans l’état d’un contrat (Contract State). Il est défini lors de la Genesis et peut être, selon les règles du contrat, mis à jour par des transitions autorisées. Contrairement aux Owned States, le Global State n’appartient pas à une entité particulière ; il est plus proche d’un registre public dans le cadre du contrat.

#### Interface

L’Interface est l’ensemble des instructions qui permettent de décoder les données binaires compilées dans un Schema ou dans des opérations de contrat et leurs états, afin de les rendre lisibles pour l’utilisateur ou son wallet. Elle agit comme une couche d’interprétation.

#### Interface Implementation

L’Interface Implementation est l’ensemble des déclarations qui relient une **Interface** à un **Schema**. Elle rend possible la traduction sémantique opérée par l’Interface elle-même, afin que les données brutes d’un contrat soient compréhensibles par l’utilisateur ou les logiciels impliqués (les wallets).

#### Invoice

Une Invoice prend la forme d’une URL encodée en [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), qui embarque les données nécessaires à la construction d’une **State Transition** (par le payeur). En d’autres termes, c’est une facture permettant à la contrepartie (*payer*) de créer la transition correspondante pour transférer l’actif ou mettre à jour l’état du contrat.

#### Lightning Network

Le Lightning Network est un réseau décentralisé de canaux de paiements (ou _state channels_) sur Bitcoin, constitué de portefeuilles multi-signatures 2/2. Il permet de faire des transactions _off-chain_ rapides et peu coûteuses, tout en s’appuyant sur la couche 1 de Bitcoin pour l’arbitrage (ou la fermeture) lorsque nécessaire.

Pour plus d’informations sur le fonctionnement de Lightning, je vous conseille de suivre cette autre formation :

https://planb.network/courses/lnp201

#### Multi Protocol Commitment - MPC

Le Multi Protocol Commitment (MPC) désigne la structure d'arbre de Merkle utilisée dans RGB pour inclure, au sein d’une unique transaction Bitcoin, plusieurs **Transition Bundles** issus de contrats différents. L’idée est de regrouper plusieurs engagements (correspondant potentiellement à différents contrats ou différents actifs) dans un seul point d’ancrage afin d’optimiser l’occupation de l’espace de bloc.

#### Owned State

Un Owned State est la partie de l’état d’un contrat (Contract State) qui est enfermée dans un Assignment et associée à un détenteur particulier (via un Single-use Seal pointant vers un UTXO). Cela représente, par exemple, un actif numérique ou un droit contractuel spécifique attribué à cette personne.

#### Ownership

Le terme Ownership renvoie à la capacité de contrôler et de dépenser un UTXO référencé par une Seal Definition. Lorsqu’un Owned State est lié à un UTXO, le propriétaire de cet UTXO a le droit, potentiellement, de transférer ou de faire évoluer l’état associé, selon les règles du contrat.

#### Partially Signed Bitcoin Transaction - PSBT

Une PSBT (_Partially Signed Bitcoin Transaction_) est une transaction Bitcoin qui n’est pas encore complètement signée. Elle peut être partagée entre plusieurs entités, chacune pouvant y ajouter ou y vérifier certains éléments (signatures, scripts…), jusqu’à ce que la transaction soit jugée prête pour la diffusion on-chain.  

Pour plus d’informations : [BIP-0174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Pedersen commitment

Un Pedersen commitment est un type d'engagement cryptographique présentant la propriété d’être **homomorphique** vis-à-vis de l’opération d’addition. Cela signifie qu’il est possible de valider la somme de deux engagements sans dévoiler les valeurs individuelles.

Formellement, si :

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

alors :

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

Cette propriété devient utile, par exemple, pour dissimuler les montants de tokens échangés tout en pouvant vérifier les totaux.

Pour plus d’informations : [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

#### Redeem

Dans une State Extension, un Redeem fait référence à l’action de récupérer (ou d’exploiter) une **Valency** précédemment déclarée. Une Valency étant un droit public, le Redeem permet à un participant autorisé de réclamer une extension spécifique de l’état du contrat.

#### Schema

Un Schema dans RGB est un morceau de code déclaratif décrivant l’ensemble des variables, règles et logiques d’affaires (*Business Logic*) qui régissent le fonctionnement d’un contrat. Le Schema définit la structure de l’état, les types de transitions autorisées et les conditions de validation.

#### Seal Definition

La Seal Definition est la partie d’un Assignment qui associe le _commitment_ à un UTXO possédé par le nouveau détenteur. Elle indique, en d’autres termes, où se trouve l’état (dans quel UTXO) et permet d’établir la propriété d’un actif ou d’un droit.

#### Shard

Un Shard représente une branche dans le DAG de l’historique des State Transitions d’un contrat RGB. Autrement dit, c’est un sous-ensemble cohérent de l’historique global du contrat, correspondant par exemple à la séquence de transitions nécessaires pour prouver la validité d’un actif donné depuis la _Genesis_.

#### Single-use Seal

Un Single-use Seal est une promesse d'engagement cryptographique sur un message encore inconnu, qui sera révélé une seule fois à l’avenir et qui doit être connu de tous les membres d’une audience spécifique. L’objectif est d’empêcher la création de multiples engagements concurrents pour le même sceau.

#### Stash

Le Stash est l’ensemble des données côté client qu’un utilisateur stocke pour un ou plusieurs contrats RGB, afin de procéder à la validation (*Client-side Validation*). Cela inclut l’historique des transitions, les consignments, les preuves de validité, etc. Chaque détenteur ne conserve que les parties de l’historique dont il a besoin (*shards*).

#### State Extension

Une State Extension est une opération de contrat permettant de redéclencher des mises à jour de l’état via la rédemption de **Valencies** préalablement déclarées. Pour être effective, une State Extension doit ensuite être refermée par une State Transition (qui actualise l’état final du contrat).  

#### State Transition

La State Transition est l’opération qui fait évoluer l’état d’un contrat RGB vers un nouvel état. Elle peut modifier les données du Global State et/ou des Owned States. Dans la pratique, chaque transition est vérifiée par les règles du Schema et ancrée dans la blockchain Bitcoin via un _commitment_.

#### Taproot

Fait référence au format de transactions Segwit v1 de Bitcoin, introduit par le [BIP341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) et le [BIP342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot permet d’améliorer la confidentialité et la flexibilité des scripts, notamment en rendant les transactions plus compactes et plus difficiles à distinguer les unes des autres.

#### Terminal Consignment - Consignment Endpoint

Le Terminal Consignment (ou _Consignment Endpoint_) est un *transfer consignment* comprenant l’état final du contrat qui intègre la State Transition créée à partir de l’Invoice du destinataire (*payee*). Il s’agit donc du point d’aboutissement d’un transfert, avec les données nécessaires pour prouver que la propriété ou l’état a bien été transmis.

#### Transition Bundle

Un Transition Bundle est un ensemble de State Transitions RGB (appartenant au même contrat) qui sont tous engagés dans la même ***witness transaction*** Bitcoin. Cela permet de regrouper plusieurs mises à jour ou transferts en un seul ancrage on-chain.

#### UTXO

Un UTXO (*Unspent Transaction Output*) Bitcoin est défini par le hachage d’une transaction et l’index de la sortie (*vout*). On l’appelle aussi parfois un _outpoint_. Dans le protocole RGB, la référence à un UTXO (via une **Seal Definition**) permet de localiser l’**Owned State**, c’est-à-dire la propriété détenue sur la blockchain.

#### Valency

Une Valency est un droit public ne nécessitant pas de stockage d’état en tant que tel, mais qui peut être racheté via une **State Extension**. Il s’agit donc d’une forme de possibilité ouverte à tous (ou à certains acteurs), déclarée dans la logique du contrat, afin d’effectuer ultérieurement une extension particulière.

#### Witness Transaction

La Witness Transaction est la transaction Bitcoin qui ferme le Single-use Seal autour d’un message contenant un Multi Protocol Commitment (MPC). Cette transaction dépense un UTXO ou en crée un, de façon à sceller l’engagement lié au protocole RGB. Elle fait office de preuve on-chain que l’état a été fixé à un instant précis.

# Programmation sur RGB
<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## Implémentation des contrats RGB
<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

![video](https://youtu.be/Uo1UoxiImsI)

Dans ce chapitre, nous allons aborder concrètement la manière dont un contrat RGB est défini et mis en place. Nous allons voir quels sont les composants d'un contrat RGB, quels sont leurs rôles et comment ils sont construits.

### Les composants d'un contrat RGB

Jusqu’ici, nous avons déjà discuté de la **Genesis**, qui représente le point de départ d’un contrat, et nous avons vu comment elle s’inscrit dans la logique d’une *Contract Operation* et de l’état du protocole. La définition complète d’un contrat RGB ne se limite cependant pas à la seule Genesis : elle implique trois composants complémentaires qui, ensemble, forment le cœur de l’implémentation.

Le premier composant est appelé le **Schema**. Il s’agit d’un fichier décrivant la structure fondamentale et la logique métier (*business logic*) du contrat. En son sein, on précise les types de données utilisés, les règles de validation, les opérations permises (par exemple : l'émission initiale de tokens, le transferts, des conditions particulières...), bref, l’ossature générale qui dicte le fonctionnement du contrat.

Le deuxième composant est l'**Interface**. Il se focalise sur la manière dont les utilisateurs (et par extension, les logiciels de portefeuilles) vont interagir avec ce contrat. On y décrit la sémantique, c’est-à-dire la représentation lisible des différents champs et actions. Ainsi, alors que le Schema définit comment le contrat fonctionne techniquement, l’Interface définit comment présenter et exposer ces fonctionnalités : noms des méthodes, affichage des données, etc.

Le troisième composant est l'**Interface Implementation**, qui vient compléter les deux précédents en étant une sorte de pont entre le Schema et l’Interface. Autrement dit, il associe la sémantique énoncée par l’Interface aux règles sous-jacentes définies dans le Schema. C’est cette implémentation qui va gérer, par exemple, la conversion entre un paramètre saisi dans le wallet et la structure binaire imposée par le protocole, ou encore la compilation des règles de validation en langage machine.

Cette modularité est une caractéristique intéressante dans RGB, car elle permet à différents groupes de développeurs de travailler séparément sur ces aspects (*Schema*, *Interface*, *Implementation*), tant qu’ils suivent les règles de consensus du protocole.

Pour résumer, chaque contrat se compose donc de :
- **Genesis**, qui est l’état initial du contrat (et qu’on peut assimiler à une transaction spéciale définissant la première propriété d’un actif, d'un droit, ou de toute autre donnée paramétrable) ;
- **Schema**, qui décrit la logique métier du contrat (types de données, règles de validation, etc.) ;
- **Interface**, qui apporte une couche sémantique, destinée aux wallets et aux utilisateurs humains, afin de clarifier la lecture et l’exécution des opérations ;
- **Interface Implementation**, qui fait le lien entre la logique métier et la présentation, afin d'assurer que la définition du contrat est cohérente avec l’expérience utilisateur.

![RGB-Bitcoin](assets/fr/070.webp)

Il est important de noter que pour qu’un portefeuille puisse gérer un actif RGB (que ce soit un jeton fongible ou un droit quelconque), il doit disposer de tous ces éléments compilés : *Schema*, *Interface*, *Interface Implementation* et *Genesis*. Cela se transmet via un ***contract consignment***, c’est-à-dire un paquet de données contenant tout le nécessaire pour valider le contrat côté client.

Afin de mieux clarifier ces notions, voici un tableau récapitulatif comparant les composants d’un contrat RGB à des concepts déjà connus soit en programmation orientée objet (OOP), soit dans l’écosystème Ethereum :

| Composant de contrat RGB     | Signification                           | Équivalent OOP                                     | Équivalent Ethereum                |
| ---------------------------- | --------------------------------------- | -------------------------------------------------- | ---------------------------------- |
| **Genesis**                  | État initial du contrat                 | Class constructor                                  | Contract constructor               |
| **Schema**                   | Logique métier du contrat               | Class                                              | Contract                           |
| **Interface**                | Sémantique du contrat                   | Interface (Java) / trait (Rust) / protocol (Swift) | ERC Standard                       |
| **Interface Implementation** | Mapping de la sémantique et  la logique | Impl (Rust) / Implements (Java)                    | Application Binary Interface (ABI) |

Dans la colonne de gauche, on retrouve les éléments propres au protocole RGB. Dans la colonne du milieu, on voit la fonction concrète de chaque composant. Puis, dans la colonne "Équivalent OOP", on trouve le terme équivalent dans la programmation orientée objet :
- La **Genesis** joue un rôle similaire à un *Class constructor* : c’est là qu’on initialise l’état du contrat ;
- Le **Schema** correspond à la description d’une classe, c’est-à-dire la définition des propriétés, des méthodes, et de la logique sous-jacente ;
- L’**Interface** correspond aux *interfaces* (Java), aux *traits* (Rust) ou encore aux *protocols* (Swift) : ce sont les définitions publiques des fonctions, événements, champs... ;
- L’**Interface Implementation** correspond à *Impl* en Rust ou *Implements* en Java, où l’on précise comment le code va réellement exécuter les méthodes annoncées dans l’interface.

Dans le cadre d’Ethereum, la Genesis se rapproche du *contract constructor*, le Schema de la définition du contrat, l’Interface d’un standard type ERC-20 ou ERC-721, et l’Interface Implementation de l’ABI (*Application Binary Interface*), qui  spécifie le format des interactions avec le contrat.

L’avantage de la modularité de RGB tient aussi au fait que des parties prenantes différentes peuvent écrire, par exemple, leur propre Interface Implementation, tant qu’elles respectent la logique du *Schema* et la sémantique de l’*Interface*. Ainsi, un émetteur pourrait développer un nouveau front-end (Interface) plus convivial, sans modifier la logique du contrat, ou inversement, on pourrait étendre le Schema pour ajouter une fonctionnalité, et fournir une nouvelle version de l’Interface Implementation adaptée, tandis que les anciennes implémentations resteraient valables pour les fonctionnalités de base.

Lorsqu’on compile un nouveau contrat, on génère une Genesis (première étape d’émission ou de distribution de l’actif), ainsi que ses composants (Schema, Interface, Interface Implementation). Après cela, le contrat est pleinement opérationnel et peut être propagé aux wallets et aux utilisateurs. Cette méthode, où la Genesis se combine à ces trois composants, garantit à la fois un haut degré de personnalisation (chaque contrat peut avoir sa propre logique), de décentralisation (chacun peut contribuer à un composant donné), et de sécurité (la validation demeure strictement définie par le protocole, sans dépendre d’un code arbitraire on-chain comme c’est souvent le cas sur d’autres blockchains).

Maintenant, je vous propose de découvrir plus en détail chacun de ces composants : le **Schema**, l’**Interface** et l’**Interface Implementation**.

### Schema

Dans la section précédente, nous avons vu que dans l’écosystème RGB, un contrat est composé de plusieurs éléments : la Genesis, qui instaure l’état initial, et plusieurs autres composants complémentaires. Le but du Schema est de décrire de manière déclarative toute la logique métier (*business logic*) du contrat, c’est-à-dire la structure des données, les types utilisés, les opérations permises et leurs conditions. C'est donc un élément très important pour rendre un contrat opérationnel côté client, puisque chaque participant (un wallet, par exemple) doit vérifier que les transitions d’état qu’il reçoit sont conformes à la logique définie dans le Schema.

Le Schema peut être assimilé à une "classe" dans la programmation orientée objet (OOP). De manière générale, il sert de modèle définissant les composants d’un contrat, tels que :
- Les différents types de Owned States et les Assignments ;
- Les Valencies, c’est-à-dire les droits spéciaux pouvant être déclenchés (*redeemed*) dans le cadre de certaines opérations ;
- Les champs du Global State, qui décrivent des propriétés globales, publiques et partagées du contrat ;
- La structure de la Genesis (la toute première opération qui active le contrat) ;
- Les formes autorisées de State Transitions et de State Extensions, et la manière dont ces opérations peuvent modifier l’état ;
- Des éventuelles Metadata associées à chaque opération, permettant de stocker des informations temporaires ou supplémentaires ;
- Les règles qui déterminent comment les données internes du contrat peuvent évoluer (par exemple, si un champ est mutable ou cumulatif) ;
- Les séquences d’opérations considérées comme valides : par exemple, un ordre de transitions à respecter ou un ensemble de conditions logiques à satisfaire.

![RGB-Bitcoin](assets/fr/071.webp)

Lorsque l’*issuer* d’un actif sur RGB publie un contrat, il fournit la Genesis et le Schema qui lui est associé. Les utilisateurs ou wallets qui souhaitent interagir avec l’actif récupèrent ce Schema pour comprendre la logique qui sous-tend le contrat et pouvoir vérifier par la suite que les transitions auxquelles ils participeront sont légitimes.

La première étape, pour quiconque reçoit des informations sur un actif RGB (par exemple un transfert de tokens), est de valider ces informations par rapport au Schema. Cela implique d’utiliser la compilation du Schema pour :
- Vérifier que les Owned States, Assignments et autres éléments sont correctement définis et qu’ils respectent bien les types imposés (ce qu’on appelle le *strict type system*) ;
- Vérifier que les règles de transitions (scripts de validation) sont satisfaites. Ces scripts peuvent être exécutés via AluVM, présent côté client et chargé de valider la cohérence de la logique métier (montant d’un transfert, conditions particulières, etc.).

Dans la pratique, le Schema n’est pas un code exécutable comme on peut le voir dans des blockchains qui stockent le code on-chain (EVM sur Ethereum). Au contraire, RGB sépare la logique métier (déclarative) du code d’exécution sur la blockchain (qui se limite à des ancrages cryptographiques). Ainsi, le Schema détermine les règles, mais l’application de ces règles se fait hors de la blockchain, chez chaque participant, selon le principe de la Client-side Validation.

Un Schema doit être compilé pour être utilisable par les applications RGB. Cette compilation produit un fichier binaire (par exemple `.rgb`) ou binaire chiffré (`.rgba`). Lorsque le wallet importe ce fichier, il sait alors :
- À quoi ressemble chaque type de donnée (entiers, structures, tableaux…) grâce au strict type system ;
- De quelle façon la Genesis doit être structurée (afin de comprendre l’initialisation de l’actif) ;
- Les différents types d’opérations (State Transitions, State Extensions) et la manière dont elles peuvent modifier l’état ;
- Les règles de script (introduites dans le Schema) que le moteur AluVM appliquera pour vérifier la validité des opérations.

Comme expliqué dans les chapitres précédents, le *strict type system* nous donne un format d’encodage stable et déterministe : toutes les variables, qu’il s’agisse d'Owned States, de Global State ou de Valencies, sont décrites avec précision (taille, borne inférieure et supérieure si nécessaire, type signé ou non signé, etc.). Il est également possible de définir des structures imbriquées, par exemple pour prendre en charge des cas d’usage complexes.

En option, le Schema peut référencer un `SchemaId` racine qui facilite la réutilisation d’une structure de base existante (un template). On peut ainsi faire évoluer un contrat ou créer des variations (par exemple un nouveau type de token) à partir d’un canevas déjà éprouvé. Cette modularité vise à éviter la recréation de contrats entiers et encourage la standardisation des bonnes pratiques.

Un autre point important est que la logique d’évolution de l’état (transferts, mises à jour, etc.) se trouve décrite dans le Schema sous forme de scripts, de règles et de conditions. Ainsi, si le concepteur du contrat souhaite autoriser une réémission ou imposer un mécanisme de burn (destruction de tokens), il peut spécifier les scripts correspondants pour AluVM dans la partie validation du Schema.

#### Différence avec les blockchains programmables on-chain

Contrairement à des systèmes comme Ethereum, où le code du smart contract (exécutable) est inscrit dans la blockchain elle-même, RGB stocke le contrat (sa logique) off-chain, sous forme de document déclaratif compilé. Cela implique que :
- Il n’y a pas de VM Turing-complète qui tourne dans chaque nœud du réseau Bitcoin. Les règles d’un contrat RGB ne sont pas exécutées sur la blockchain, mais bien chez chaque utilisateur qui souhaite valider un état ;
- Les données du contrat ne polluent pas la blockchain : seules des preuves cryptographiques (*commitments*) sont ancrées dans les transactions Bitcoin (via `Tapret` ou `Opret`) ;
- Le Schema peut être mis à jour ou décliner des versions (*fast-forward*, *push-back*, etc.), sans nécessiter de fork sur la blockchain Bitcoin. Les wallets doivent simplement importer le nouveau Schema et s’adapter aux changements de consensus.

#### Utilisation par l’émetteur et par les utilisateurs

Lorsqu’un *issuer* crée un actif (par exemple un jeton fongible non inflationniste), il prépare :
- Un Schema décrivant les règles d’émission, de transfert, etc. ;
- Une Genesis adaptée à ce Schema (avec le nombre total de jetons émis, l’identité de l’owner initial, éventuellement des Valencies spéciales pour la réémission, etc.).

Ensuite, il met à disposition des utilisateurs le Schema compilé (un fichier `.rgb`), afin que toute personne recevant un transfert de ce token puisse vérifier localement la cohérence de l’opération. Sans ce Schema, un utilisateur ne saurait pas interpréter les données d’état ou vérifier qu’elles respectent les règles du contrat.

Aussi, lorsqu’un nouveau wallet souhaite prendre en charge un actif, il lui suffit d’intégrer le Schema pertinent. Ce mécanisme permet d’ajouter la compatibilité à de nouveaux types d’actifs RGB, sans changer la base logicielle du wallet de manière invasive : il suffit d’importer le binaire du Schema et de comprendre sa structure.

Le Schema définit donc la logique métier dans RGB. Il liste les règles d’évolution d’un contrat, la structure de ses données (Owned States, Global State, Valencies) et les scripts de validation associés (exécutables par AluVM). Grâce à ce document déclaratif, on sépare clairement la définition d’un contrat (fichier compilé) de l’exécution même des règles (côté client). Ce découplage confère une grande souplesse à RGB, en permettant une large gamme de cas d’usage (jetons fongibles, NFT, contrats plus sophistiqués) tout en évitant la complexité et les failles typiques des blockchains programmables on-chain.

#### Exemple de Schema

Examinons ensemble un exemple concret de Schema pour un contrat RGB. Il s’agit d’un extrait en Rust issu du fichier `nia.rs` (initiales de "*Non-Inflatable Assets*"), qui définit un modèle de jetons fongibles ne pouvant pas être réémis au-delà de leur supply initiale (un actif non inflationniste). On peut considérer ce type de jeton comme l’équivalent, dans l’univers RGB, des ERC20 sur Ethereum, c’est-à-dire des tokens fongibles qui respectent certaines règles de base (par exemple sur les transferts, l’initialisation de la supply, etc.).

Avant de plonger dans le code, il est utile de rappeler la structure générale d’un Schema RGB. On y trouve une série de déclarations encadrant :
- Un éventuel `SchemaId` qui indique l'utilisation d'un autre Schema de base comme template ;
- Les **Global States** et **Owned States** (avec leurs types stricts) ;
- Les **Valencies** (s’il y en a) ;
- Les **Operations** (Genesis, State Transitions, State Extensions) qui peuvent référencer ces états et valencies ;
- Le **Strict Type System** utilisé pour décrire et valider les données ;
- Les **scripts de validation** (exécutés via AluVM).

![RGB-Bitcoin](assets/fr/072.webp)

Le code ci-dessous montre la définition complète du Schema Rust. Nous allons le commenter partie par partie, en suivant les annotations (1) à (9) ci-dessous :

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
    
    // definitions of libraries and variables

    // ===== PART 2: General Properties (ffv, subset_of, type_system) =====
    Schema {
        ffv: zero!(),
        subset_of: None,
        type_system: types.type_system(),

        // ===== PART 3: Global States =====
        global_types: tiny_bmap! {
            GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
            GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
            GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
            GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
        },

        // ===== PART 4: Owned Types =====
        owned_types: tiny_bmap! {
            OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
        },

        // ===== PART 5: Valencies =====
        valency_types: none!(),

        // ===== PART 6: Genesis: Initial Operations =====
        genesis: GenesisSchema {
            metadata: Ty::<SemId>::UNIT.id(None),
            globals: tiny_bmap! {
                GS_NOMINAL => Occurrences::Once,
                GS_DATA => Occurrences::Once,
                GS_TIMESTAMP => Occurrences::Once,
                GS_ISSUED_SUPPLY => Occurrences::Once,
            },
            assignments: tiny_bmap! {
                OS_ASSET => Occurrences::OnceOrMore,
            },
            valencies: none!(),
        },

        // ===== PART 7: Extensions =====
        extensions: none!(),

        // ===== PART 8: Transitions: TS_TRANSFER =====
        transitions: tiny_bmap! {
            TS_TRANSFER => TransitionSchema {
                metadata: Ty::<SemId>::UNIT.id(None),
                globals: none!(),
                inputs: tiny_bmap! {
                    OS_ASSET => Occurrences::OnceOrMore,
                },
                assignments: tiny_bmap! {
                    OS_ASSET => Occurrences::OnceOrMore,
                },
                valencies: none!(),
            }
        },

        // ===== PART 9: Script AluVM and Entry Points =====
        script: Script::AluVM(AluScript {
            libs: confined_bmap! { alu_id => alu_lib },
            entry_points: confined_bmap! {
                EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
                EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
            },
        }),
    }
}
```

- **(1) – En-tête de la fonction et SubSchema**

La fonction `nia_schema()` renvoie un `SubSchema`, ce qui indique que ce Schema peut hériter partiellement d’un schéma plus générique. Dans l’écosystème RGB, cette souplesse permet de réutiliser certains éléments standard d’un schema master, puis de définir des règles spécifiques au contrat en question. Ici, on choisit de ne pas activer d’héritage puisque `subset_of` sera `None`.

- **(2) – Propriétés générales : ffv, subset_of, type_system**

La propriété `ffv` correspond à la version *fast-forward* du contrat. Une valeur `zero!()` indique ici qu’on est à la version 0 ou initiale de ce schéma. Si plus tard on souhaite ajouter de nouvelles fonctionnalités (nouveau type d’opération, etc.), on peut incrémenter cette version pour indiquer un changement de consensus.

La propriété `subset_of: None` confirme l’absence d’héritage. Le champ `type_system` fait référence au strict type system déjà défini dans la bibliothèque `types`. Grâce à cette ligne, on indique que toutes les données employées par le contrat utilisent l’implémentation de sérialisation stricte fournie par la librairie mentionnée.

- **(3) – Global States**

Dans le bloc `global_types`, on déclare quatre éléments. On utilise la clé, comme `GS_NOMINAL` ou `GS_ISSUED_SUPPLY`, pour les référencer par la suite :
- `GS_NOMINAL` fait référence à un type `DivisibleAssetSpec`, qui décrit divers champs du jeton créé (nom complet, ticker, precision…) ;
- `GS_DATA` représente des données générales, par exemple un disclaimer, des métadonnées, ou tout autre texte ;
- `GS_TIMESTAMP` fait référence à une date d’émission ;
- `GS_ISSUED_SUPPLY` établit la supply totale, c’est-à-dire le nombre maximal de jetons qu’il est permis de créer.

Le mot-clé `once(...)` signifie que chacun de ces champs ne peut apparaître qu’une seule fois.

- **(4) – Owned Types**

Dans `owned_types`, on déclare `OS_ASSET`, qui décrit un état fongible. On utilise `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, indiquant que la quantité d’actifs (tokens) est stockée en tant qu’entier non signé de 64 bits. Ainsi, toute transaction enverra un certain montant d’unités de ce jeton, qui sera validé selon cette structure numérique strictement typée.

- **(5) – Valencies**

On indique `valency_types: none!()`, ce qui signifie qu’il n’y a pas de Valencies dans ce schéma, autrement dit aucun droit spécial ou extra (comme la réémission, un burn conditionnel, etc.). Si un schéma en prévoyait, on les déclarerait dans cette section.

- **(6) – Genesis : premières opérations**

On entre ici dans la partie qui déclare les Contract Operations. La Genesis est décrite par :
- L’absence de `metadata` (champ `metadata: Ty::<SemId>::UNIT.id(None)`) ;
- Les Global States qui doivent être présents une fois chacun (`Once`) ;
- Une Assignments list où `OS_ASSET` doit apparaître `OnceOrMore`. Cela signifie qu’à la Genesis, il faut au moins un Assignments `OS_ASSET` (un détenteur initial) ;
- Aucune Valency : `valencies: none!()`.

C’est ainsi qu’on limite la définition d’émission initiale du jeton : on doit déclarer la supply émise (`GS_ISSUED_SUPPLY`), plus au moins un détenteur (une Owned State de type `OS_ASSET`).

- **(7) – Extensions**

Le champ `extensions: none!()` indique qu’aucune State Extension n’est prévue dans ce contrat. Cela signifie qu’il n’y a pas d’opération servant à racheter un droit numérique (Valency) ou à effectuer une extension de l’état avant une Transition. Tout se fait via la Genesis ou les State Transitions.

- **(8) – Transitions : TS_TRANSFER**

Dans `transitions`, on définit le type d’opération `TS_TRANSFER`. On explique que :
- Il n’a pas de `metadata` ;
- Il ne modifie pas le Global State (celui-ci étant déjà défini dans la Genesis) ;
- Il prend en entrée (`inputs`) un ou plusieurs `OS_ASSET`. Cela signifie qu’il doit dépenser des Owned States existants ;
- Il crée (`assignments`) au moins un nouveau `OS_ASSET` (autrement dit, le ou les destinataires reçoivent des jetons) ;
- Il ne génère aucune nouvelle Valency.

Cela modélise le comportement d’un transfert basique, qui consomme des tokens sur un UTXO, puis crée de nouveaux Owned States en faveur des destinataires, et donc conserve l’égalité du montant total entre les inputs et les outputs.

- **(9) – Script AluVM et Entry Points**

Enfin, on déclare un script AluVM (`Script::AluVM(AluScript { ... })`). Ce script contient :
- Une ou plusieurs bibliothèques externes (`libs`) à utiliser durant la validation ;
- Des `entry_points` qui pointent vers des offsets de fonctions dans le code AluVM, correspondant à la validation de la Genesis (`ValidateGenesis`) et de chaque Transition déclarée (`ValidateTransition(TS_TRANSFER)`).

Ce code de validation est responsable d’appliquer la logique métier. Par exemple, il vérifiera :
- Que la `GS_ISSUED_SUPPLY` n’est pas dépassée lors de la Genesis ;
- Que la somme des `inputs` (tokens dépensés) égale la somme des `assignments` (tokens reçus) pour `TS_TRANSFER`.

En cas de non-respect de ces règles, la transition sera considérée comme invalide.

Cet exemple de Schema de "*Non Inflatable Fungible Asset*" nous permet de mieux comprendre la structure d’un contrat de token fongible simple sous RGB. On voit clairement la séparation entre la description des données (Global et Owned States), la déclaration des opérations (Genesis, Transitions, Extensions) et l’implémentation de la validation (scripts AluVM). Grâce à ce modèle, un token se comporte comme un jeton fongible classique, mais reste validé côté client et ne dépend pas de l’infrastructure on-chain pour exécuter son code. Seuls des engagements cryptographiques sont ancrés dans la blockchain Bitcoin.

### Interface

L'interface est la couche destinée à rendre un contrat lisible et manipulable, tant par des utilisateurs (lecture humaine) que par les portefeuilles (lecture logicielle). L’Interface joue donc un rôle comparable à celui d’une interface dans un langage de programmation orientée objet (Java, Rust trait, etc.), en ce sens qu’elle expose et clarifie la structure fonctionnelle d’un contrat, sans nécessairement dévoiler les détails internes de la logique métier.

Contrairement au Schema, qui est purement déclaratif et compilé en un fichier binaire difficilement exploitable tel quel, l’Interface fournit les clés de lecture nécessaires pour :
- Lister et décrire les Global States et Owned States présents dans le contrat ;
- Accéder aux noms et aux valeurs de chaque champ, afin de pouvoir les afficher (par exemple pour un jeton, connaître son ticker, son montant maximal, etc.) ;
- Interpréter et construire les Contract Operations (Genesis, State Transition, ou State Extension) en associant les données à des noms compréhensibles (par exemple réaliser un transfert en spécifiant clairement "amount" plutôt qu’un identifiant binaire).

![RGB-Bitcoin](assets/fr/073.webp)

Grâce à l’Interface, on peut par exemple écrire un code dans un wallet qui, au lieu de manipuler des champs, manipule directement des libellés comme "nombre de tokens", "nom de l’actif", etc. De cette manière, la gestion d’un contrat devient plus intuitive.

#### Fonctionnement général

Cette méthode dispose de nombreux avantages :

- **Standardisation :**  

Un même type de contrat peut être pris en charge par une Interface standard, partagée entre plusieurs implémentations de wallets. Cela facilite la compatibilité et la réutilisation du code.

- **Séparation claire entre le Schema et l’Interface :**  

Dans la conception de RGB, le Schema (logique métier) et l’Interface (présentation et manipulation) sont deux entités indépendantes. Les développeurs qui écrivent la logique du contrat peuvent se concentrer sur le Schema, sans se soucier de l’ergonomie ou de la représentation des données, tandis qu’une autre équipe (ou la même, mais sur un autre temps) peut développer l’Interface.

- **Évolution flexible :**  

L’Interface peut être modifiée ou complétée après l’émission de l’actif, sans avoir à changer le contrat lui-même. C’est une différence majeure avec certains systèmes de smart contracts on-chain où l’Interface (souvent mêlée au code d’exécution) est figée dans la blockchain.

- **Possibilité de multi-interface**  

Un même contrat pourrait être exposé par différentes Interfaces adaptées à des besoins distincts : une Interface simple pour l’utilisateur final, une autre plus avancée pour l’issuer qui doit gérer des opérations complexes de configuration. Le wallet pourra alors choisir quelle Interface importer, selon son usage.

![RGB-Bitcoin](assets/fr/074.webp)

En pratique, lorsque le wallet récupère un contrat RGB (via un fichier `.rgb` ou `.rgba`), il importe également l’Interface associée, elle aussi compilée. À l’exécution, le wallet peut par exemple :
- Parcourir la liste des states et lire leurs noms, afin d’afficher sur l’interface utilisateur Ticker, Montant initial, Date d’émission, etc. plutôt qu’un identifiant numérique illisible ;
- Construire une opération (comme un transfert) en utilisant des noms de paramètres explicites : au lieu d’écrire `assignments { OS_ASSET => 1 }`, il peut proposer à l’utilisateur un champ "Amount" dans un formulaire, et traduire cette information en champs strictement typés attendus par le contrat.

#### Différence avec Ethereum et les autres systèmes

Sur Ethereum, l’Interface (décrite via l’ABI, *Application Binary Interface*) est généralement dérivée d’un code stocké on-chain (le smart contract). Il peut être coûteux ou compliqué de modifier une partie spécifique de l’interface sans toucher au contrat lui-même. Or, RGB repose sur une logique entièrement off-chain, avec des données ancrées en *commitments* sur Bitcoin. Cette conception rend possible la modification de l’Interface (ou de son implémentation) sans impact sur la sécurité fondamentale du contrat, car la validation des règles métier reste dans le Schema et le code AluVM référencé.

#### Compilation de l’Interface

Comme pour le Schema, l’Interface est définie dans un code source (souvent en Rust) et compilée en un fichier `.rgb` ou `.rgba`. Ce fichier binaire regroupe toutes les informations nécessaires au wallet pour :
- Identifier les champs par leurs noms ;
- Faire le lien entre chaque champ (et sa valeur) et le strict type system défini dans le contrat ;
- Connaître les différentes opérations autorisées et la façon de les construire.

Une fois l’Interface importée, le wallet peut donc afficher correctement le contrat et proposer des interactions à l'utilisateur.


### Interfaces standardisées par l'association LNP/BP

Dans l’écosystème RGB, une Interface sert donc à donner un sens lisible et manipulable aux données et opérations d’un contrat. L’Interface est ainsi un complément du Schema, qui décrit plutôt la logique métier en interne (types stricts, scripts de validation, etc.). Dans cette section, nous allons découvrir les Interfaces standards développées par l'association LNP/BP pour des types de contrats fréquents (tokens fongibles, NFT...).

Pour rappel, l’idée est que chaque Interface décrit la façon d’afficher et de manipuler un contrat du côté du wallet, en nommant clairement les champs (comme `spec`, `ticker`, `issuedSupply`...) et en définissant les opérations possibles (comme `Transfer`, `Burn`, `Rename`...). Plusieurs Interfaces sont déjà opérationnelles, mais il y en aura de plus en plus à l'avenir.

#### Quelques interface prêtes à l'emploi

**RGB20** est l’Interface destinée aux actifs fongibles, que l’on peut comparer au standard ERC20 d’Ethereum. Elle va cependant plus loin en offrant des fonctionnalités plus étendues :
- Par exemple, la possibilité de renommer l’actif (changement de *ticker* ou de nom complet) après son émission, ou bien d’ajuster sa précision (*stock splits*) ;
- Elle peut aussi décrire des mécanismes de réémission secondaire (limitée ou illimitée) et de burn puis de remplacement, afin d'autoriser l’issuer à détruire puis recréer des actifs sous certaines conditions ;

À titre d’exemple, on peut lier l’Interface RGB20 au **Schema Non-Inflatable Asset (NIA)**, qui impose une supply initiale non inflationniste, ou à d’autres schémas plus évolués selon les besoins.

**RGB21** concerne les contrats de type NFT ou plus largement, tout contenu numérique unique, comme la représentation de médias numériques (images, musiques, etc.). En plus de décrire l’émission et le transfert d’un actif unique, elle inclut des fonctionnalités comme :
- Le support intégré pour l’inclusion directe d’un fichier (jusqu’à 16 Mo) dans le contrat (pour le récupérer côté client) ;
- La possibilité pour le propriétaire d’inscrire un marquage, ou "*engraving*", dans l’historique, afin de prouver sa détention passée d’un NFT.

**RGB25** est un standard hybride combinant des aspects fongibles et non-fongibles. Il est destiné aux actifs partiellement fongibles, par exemple de la tokenisation immobilière, où l’on veut fractionner une propriété tout en conservant un lien avec un actif racine unique (autrement dit, on a des morceaux de maison fongibles, liés à une maison qui, elle, n'est pas fongible). Techniquement, on peut relier cette interface au **Schema *Collectible Fungible Asset* (CFA)**, qui prend en compte la notion de fractionnement tout en traçant l’actif original.

#### Interfaces en cours de développement

D’autres Interfaces sont envisagées pour des usages plus spécialisés, mais ne sont pas encore disponibles à l’heure actuelle :
- **RGB22**, orientée identités numériques, pour gérer des identifiants ou des profils on-chain dans l’écosystème RGB ;
- **RGB23**, pour des horodatages avancés, reprenant certaines idées d’*Opentimestamps*, mais avec des fonctionnalités de traçabilité ;
- **RGB24**, qui vise l’équivalent d’un système de noms de domaines décentralisés (DNS) similaire à l’*Ethereum Name Service* ;
- **RGB26**, destinée à la gestion de DAOs (*Decentralized Autonomous Organization*) dans un format plus complexe (gouvernance, votes, etc.) ;
- **RGB30**, très similaire à RGB20 mais avec la particularité de prendre en compte une émission initiale décentralisée et d’utiliser des State Extensions. Cela servirait à des actifs dont la réémission est gérée par plusieurs entités, ou soumise à des conditions plus fines.

Évidemment, selon la date à laquelle vous consultez cette formation, il est possible que ces interfaces soient déjà opérationnelles et accessibles.

#### Exemple d'Interface

Dans cet extrait de code Rust, on peut voir une Interface [RGB20](https://github.com/RGB-WG/rgb-std/blob/master/src/interface/rgb20.rs) (actif fongible). Ce code est tiré du fichier `rgb20.rs` dans la bibliothèque standard RGB. Nous allons l’examiner pour comprendre la structure d’une Interface et la façon dont elle fournit un pont entre, d’un côté, la logique métier (définie dans le Schema) et de l’autre, les fonctionnalités exposées aux wallets et aux utilisateurs.

```rust
// ...
fn rgb20() -> Iface {
    let types = StandardTypes::with(rgb20_stl());

    Iface {
        version: VerNo::V1,
        name: tn!("RGB20"),
        global_state: tiny_bmap! {
            fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
            fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
            fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
            fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
            fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
            fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
        },
        assignments: tiny_bmap! {
            fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
            fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
            fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
            fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
            fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
        },
        valencies: none!(),
        genesis: GenesisIface {
            metadata: Some(types.get("RGBContract.IssueMeta")),
            global: tiny_bmap! {
                fname!("spec") => ArgSpec::required(),
                fname!("data") => ArgSpec::required(),
                fname!("created") => ArgSpec::required(),
                fname!("issuedSupply") => ArgSpec::required(),
            },
            assignments: tiny_bmap! {
                fname!("assetOwner") => ArgSpec::many(),
                fname!("inflationAllowance") => ArgSpec::many(),
                fname!("updateRight") => ArgSpec::optional(),
                fname!("burnEpoch") => ArgSpec::optional(),
            },
            valencies: none!(),
            errors: tiny_bset! {
                SUPPLY_MISMATCH,
                INVALID_PROOF,
                INSUFFICIENT_RESERVES
            },
        },
        transitions: tiny_bmap! {
            tn!("Transfer") => TransitionIface {
                optional: false,
                metadata: None,
                globals: none!(),
                inputs: tiny_bmap! {
                    fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
                },
                assignments: tiny_bmap! {
                    fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
                },
                valencies: none!(),
                errors: tiny_bset! {
                    NON_EQUAL_AMOUNTS
                },
                default_assignment: Some(fname!("beneficiary")),
            },
            tn!("Issue") => TransitionIface {
                optional: true,
                metadata: Some(types.get("RGBContract.IssueMeta")),
                globals: tiny_bmap! {
                    fname!("issuedSupply") => ArgSpec::required(),
                },
                inputs: tiny_bmap! {
                    fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
                },
                assignments: tiny_bmap! {
                    fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
                    fname!("future") => ArgSpec::from_many("inflationAllowance"),
                },
                valencies: none!(),
                errors: tiny_bset! {
                    SUPPLY_MISMATCH,
                    INVALID_PROOF,
                    ISSUE_EXCEEDS_ALLOWANCE,
                    INSUFFICIENT_RESERVES
                },
                default_assignment: Some(fname!("beneficiary")),
            },
            tn!("OpenEpoch") => TransitionIface {
                optional: true,
                metadata: None,
                globals: none!(),
                inputs: tiny_bmap! {
                    fname!("used") => ArgSpec::from_required("burnEpoch"),
                },
                assignments: tiny_bmap! {
                    fname!("next") => ArgSpec::from_optional("burnEpoch"),
                    fname!("burnRight") => ArgSpec::required()
                },
                valencies: none!(),
                errors: none!(),
                default_assignment: Some(fname!("burnRight")),
            },
            tn!("Burn") => TransitionIface {
                optional: true,
                metadata: Some(types.get("RGBContract.BurnMeta")),
                globals: tiny_bmap! {
                    fname!("burnedSupply") => ArgSpec::required(),
                },
                inputs: tiny_bmap! {
                    fname!("used") => ArgSpec::from_required("burnRight"),
                },
                assignments: tiny_bmap! {
                    fname!("future") => ArgSpec::from_optional("burnRight"),
                },
                valencies: none!(),
                errors: tiny_bset! {
                    SUPPLY_MISMATCH,
                    INVALID_PROOF,
                    INSUFFICIENT_COVERAGE
                },
                default_assignment: None,
            },
            tn!("Replace") => TransitionIface {
                optional: true,
                metadata: Some(types.get("RGBContract.BurnMeta")),
                globals: tiny_bmap! {
                    fname!("replacedSupply") => ArgSpec::required(),
                },
                inputs: tiny_bmap! {
                    fname!("used") => ArgSpec::from_required("burnRight"),
                },
                assignments: tiny_bmap! {
                    fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
                    fname!("future") => ArgSpec::from_optional("burnRight"),
                },
                valencies: none!(),
                errors: tiny_bset! {
                    NON_EQUAL_AMOUNTS,
                    SUPPLY_MISMATCH,
                    INVALID_PROOF,
                    INSUFFICIENT_COVERAGE
                },
                default_assignment: Some(fname!("beneficiary")),
            },
            tn!("Rename") => TransitionIface {
                optional: true,
                metadata: None,
                globals: tiny_bmap! {
                    fname!("new") => ArgSpec::from_required("spec"),
                },
                inputs: tiny_bmap! {
                    fname!("used") => ArgSpec::from_required("updateRight"),
                },
                assignments: tiny_bmap! {
                    fname!("future") => ArgSpec::from_optional("updateRight"),
                },
                valencies: none!(),
                errors: none!(),
                default_assignment: Some(fname!("future")),
            },
        },
        extensions: none!(),
        error_type: types.get("RGB20.Error"),
        default_operation: Some(tn!("Transfer")),
        type_system: types.type_system(),
    }
}
```

Dans cette interface, on remarque des similarités avec la structure du Schema : on retrouve une déclaration de Global State, de Owned States, de Contract Operations (Genesis et Transitions), ainsi que de la gestion d’erreurs. Mais l’Interface se concentre sur la présentation et la manipulation de ces éléments pour un wallet ou toute autre application.

La différence avec le Schema réside dans la nature des types. Dans le Schema, on utilise des types stricts (comme `FungibleType::Unsigned64Bit`) et des identifiants plus techniques. Dans l’Interface, on utilise plutôt des noms de champs, des macros (`fname!()`, `tn!()`), et des références à des classes d’arguments (`ArgSpec`, `OwnedIface::Rights`...). Il s’agit ici de faciliter la compréhension fonctionnelle et l’organisation des éléments pour le wallet.

De plus, l’Interface peut introduire des fonctionnalités supplémentaires par rapport au schéma de base (par exemple, la gestion d’un droit de `burnEpoch`), tant que celles-ci restent cohérentes avec la logique finale validée côté client. La section "script" AluVM dans le Schema assurera la validité cryptographique, tandis que l’Interface décrit comment l’utilisateur (ou le wallet) interagit avec ces états et transitions.

#### Global State et Assignments

Dans la section `global_state`, on retrouve des champs tels que `spec` (description de l’actif), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Ce sont des champs que le wallet peut lire et présenter. Par exemple :
- `spec` permettra d’afficher la configuration du jeton ;
- `issuedSupply` ou `burnedSupply` nous donnent sur le nombre total de tokens émis ou brûlés, etc.

Dans la section `assignments`, on définit différents rôles ou droits. Par exemple :
- `assetOwner` correspond à la détention de tokens (c’est le *Owned State* fongible) ;
- `burnRight` correspond à la capacité de brûler des tokens ;
- `updateRight` correspond au droit de renommer l’actif.

Le mot-clé `public` ou `private` (par exemple `AssignIface::public(...)`) indique si ces états sont visibles (`public`) ou confidentiels (`private`). Quant à `Req::NoneOrMore`, `Req::Optional`, ils indiquent l’occurrence attendue.

#### Genesis et transitions

La partie `genesis` décrit la manière dont est initialisé l’actif :
- Les champs `spec`, `data`, `created`, `issuedSupply` sont obligatoires (`ArgSpec::required()`) ;
- Les `assignments` comme `assetOwner` peuvent être présents en plusieurs exemplaires (`ArgSpec::many()`), ce qui permet de distribuer des tokens à plusieurs détenteurs initiaux ;
- On peut éventuellement prévoir (ou non) des champs comme `inflationAllowance` ou `burnEpoch` dans la Genesis.

Ensuite, pour chaque Transition (`Transfer`, `Issue`, `Burn`…), l’Interface définit quels champs l’opération attend en entrée, quels champs l’opération va produire en sortie, et les éventuelles erreurs qui peuvent survenir. Par exemple :

**Transition `Transfer` :**
- Inputs : `previous` → doit être un `assetOwner` ;
- Assignments : `beneficiary` → sera un nouvel `assetOwner` ;
- Erreur : `NON_EQUAL_AMOUNTS` (le wallet saura ainsi gérer les cas où la somme en entrée ne correspond pas à celle en sortie).

**Transition `Issue` :**
- Optionnelle (`optional: true`), car l’émission supplémentaire n’est pas forcément activée ;
- Inputs : `used` → un `inflationAllowance`, c’est-à-dire la permission d’ajouter plus de tokens ;
- Assignments : `beneficiary` (nouveaux tokens reçus) et `future` (`inflationAllowance` restant) ;
- Erreurs possibles : `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, etc.

**Transition `Burn` :**
- Inputs : `used` → un `burnRight` ;
- Globals : `burnedSupply` obligatoire ;
- Assignments : `future` → une éventuelle poursuite du `burnRight` si on n’a pas tout brûlé ;
- Erreurs : `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.

Chaque opération est donc décrite d’une façon lisible pour un wallet. Cela permet d’afficher une interface graphique où l’utilisateur voit clairement : "*Vous avez un droit de burn. Souhaitez-vous brûler un certain montant ?*". Le code sait qu’il faut renseigner un champ `burnedSupply` et vérifier que le `burnRight` est valide.

Pour résumer, il faut garder à l’esprit qu’une Interface, aussi complète soit-elle, ne définit pas à elle seule la logique interne du contrat. Le cœur du travail est fait par le **Schema**, qui comprend les types stricts, la structure de la Genesis, les transitions, etc. L’Interface se contente en quelque sorte d’exposer ces éléments de manière plus intuitive et nommée, pour un usage dans une application.

Grâce à la modularité de RGB, on peut ainsi faire évoluer l’Interface (par exemple, ajouter une transition `Rename`, corriger l’affichage d’un champ...) sans devoir réécrire tout le contrat. Les utilisateurs de cette Interface peuvent alors bénéficier immédiatement de ces améliorations, dès qu’ils mettent à jour le fichier `.rgb` ou `.rgba`.

Mais après avoir déclaré une Interface, il faut la relier au Schema correspondant. Cette correspondance s’effectue via l’***Interface Implementation***, qui indique comment mapper chaque champ nommé (comme par exemple `fname!("assetOwner")`) à l’ID strict (comme par exemple `OS_ASSET`) défini dans le Schema. Cela permet par exemple de s’assurer que, lorsqu’un wallet manipule un champ `burnRight`, il s’agit bien de l’état qui, dans le Schema, décrit la capacité de brûler des tokens.

### Interface Implementation

Dans l’architecture RGB, nous avons vu que chaque composant (Schema, Interface, etc.) peut être développé et compilé indépendamment. Il reste toutefois un élément indispensable pour relier ces différentes briques : l’***Interface Implementation***. C’est elle qui fait le mappage explicite entre les identifiants ou les champs définis dans le Schema (côté logique métier) et les noms déclarés dans l’Interface (côté présentation et interaction utilisateur). Ainsi, lorsqu’un wallet charge un contrat, il peut comprendre précisément quel champ correspond à quoi, et comment une opération nommée dans l’Interface se rattache à la logique du Schema.

Un point important est que l’Interface Implementation n’a pas forcément vocation à exposer toutes les fonctionnalités d’un Schema, ni tous les champs d’une Interface : elle peut se limiter à un sous-ensemble. En pratique, cela permet de brider ou filtrer certains aspects du Schema. Par exemple, on pourrait avoir un Schema avec quatre types d’opérations, mais une Interface Implementation qui n’en mappe que deux dans un contexte donné. Inversement, si une Interface propose des endpoints supplémentaires, on peut choisir de ne pas les implémenter ici.

Voici un exemple classique d’Interface Implementation, où l’on associe un Schema *Non-Inflatable Asset* (NIA) à l’Interface RGB20 :

```rust
fn nia_rgb20() -> IfaceImpl {
    let schema = nia_schema();
    let iface = Rgb20::iface();

    IfaceImpl {
        version: VerNo::V1,
        schema_id: schema.schema_id(),
        iface_id: iface.iface_id(),
        script: none!(),
        global_state: tiny_bset! {
            NamedField::with(GS_NOMINAL, fname!("spec")),
            NamedField::with(GS_DATA, fname!("data")),
            NamedField::with(GS_TIMESTAMP, fname!("created")),
            NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
        },
        assignments: tiny_bset! {
            NamedField::with(OS_ASSET, fname!("assetOwner")),
        },
        valencies: none!(),
        transitions: tiny_bset! {
            NamedType::with(TS_TRANSFER, tn!("Transfer")),
        },
        extensions: none!(),
    }
}
```

Dans cette Interface Implementation :
- On référence explicitement le Schema, via `nia_schema()`, et l’Interface, via `Rgb20::iface()`. Les appels `schema.schema_id()` et `iface.iface_id()` servent à ancrer l’Interface Implementation du côté de la compilation (cela associe les identifiants cryptographiques de ces deux composants) ;
- On établit un mappage entre les éléments du Schema et ceux de l’Interface. Par exemple, le champ `GS_NOMINAL` dans le Schema est lié à la chaîne `"spec"` côté Interface (`NamedField::with(GS_NOMINAL, fname!("spec"))`). On fait de même pour les opérations, comme `TS_TRANSFER`, qu’on rattache à `"Transfer"` dans l’Interface... ;
- On peut observer qu’il n’y a pas de valencies (`valencies: none!()`) ni d’extensions (`extensions: none!()`), ce qui reflète le fait que ce contrat NIA n’utilise pas ces fonctionnalités.

Le résultat après compilation est un fichier `.rgb` ou `.rgba` séparé, destiné à être importé dans le wallet en complément du Schema et de l’Interface. Ainsi, le logiciel sait comment connecter concrètement ce contrat NIA (dont la logique est décrite par son Schema) à l’Interface "RGB20" (qui fournit des noms humains et un mode d’interaction pour des jetons fongibles), en appliquant cette Interface Implementation comme passerelle entre les deux.

#### Pourquoi séparer l’Interface Implementation ?

La séparation renforce la flexibilité. Un même Schema pourrait avoir plusieurs Interface Implementations distinctes, chacune mappant un ensemble différent de fonctionnalités. Par ailleurs, l’Interface Implementation elle-même peut évoluer ou être réécrite sans nécessiter un changement dans le Schema ni dans l’Interface. On garde donc le principe de modularité de RGB : chaque composant (Schema, Interface, Interface Implementation) peut être versionné et mis à jour de manière indépendante, tant qu’on respecte les règles de compatibilité imposées par le protocole (mêmes identifiants, cohérence des types, etc.).

Dans le cadre d’une utilisation concrète, lorsque le wallet charge un contrat, il doit :
- Charger le **Schema** compilé (pour connaître la structure de la logique métier) ;
- Charger l’**Interface** compilée (pour comprendre les noms et les opérations côté utilisateur) ;
- Charger l’**Interface Implementation** compilée (pour relier la logique du Schema aux noms de l’Interface, opération par opération, champ par champ).

Cette architecture modulaire rend possible des scénarios d’usage tels que :
- Limiter certaines opérations pour certains utilisateurs : proposer une Interface Implementation partielle qui ne donne accès qu’aux transferts de base, sans offrir la fonction de burn ou d’update, par exemple ;
- Changer la présentation : concevoir une Interface Implementation qui renomme un champ dans l’Interface ou le mappe différemment, sans altérer la base du contrat ;
- Supporter plusieurs schémas : un wallet peut charger plusieurs Interface Implementations pour le même type d’Interface, afin de gérer différents schémas (différentes logiques de jetons), pourvu que leur structure soit compatible.

Dans le chapitre suivant, nous allons étudier comment fonctionne le transfert d'un contrat, et comment sont générées les invoices RGB.

## Les transferts de contrat
<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

![video](https://youtu.be/sVoKIi-1XbY)


Dans ce chapitre, nous allons analyser le déroulement d'un transfert de contrat dans l’écosystème RGB. Pour l’illustrer, nous retrouvons Alice et Bob, nos protagonistes habituels, qui désirent échanger un actif RGB. Nous allons également montrer des extraits de commandes issus de l’outil en ligne de commande `rgb`, afin de voir comment cela fonctionne en pratique.

### Comprendre le transfert de contrat RGB

Prenons donc un exemple de transfert entre Alice et Bob. Dans cet exemple, on suppose que Bob commence tout juste à utiliser RGB, tandis qu’Alice détient déjà des actifs RGB dans son wallet. Nous verrons comment Bob installe son environnement, importe le contrat concerné, puis demande à Alice un transfert, et enfin comment Alice réalise la transaction effective sur la blockchain Bitcoin.

#### 1) Installation du wallet RGB

Avant toute chose, Bob doit installer un wallet RGB, c’est-à-dire un logiciel compatible avec le protocole. Celui-ci ne contient au départ aucun contrat. Bob aura également besoin :
- D’un wallet Bitcoin pour gérer ses UTXOs ;
- D’une connexion à un nœud Bitcoin (ou à un serveur Electrum), afin de pouvoir identifier ses UTXOs et propager ses transactions sur le réseau.

Pour rappel, **les Owned States** dans RGB font référence à des UTXOs Bitcoin. On doit donc toujours être en mesure de gérer et de dépenser des UTXOs dans une transaction Bitcoin qui intègre les engagements cryptographiques (`Tapret` ou `Opret`) pointant vers les données RGB.

#### 2) Acquisition des informations sur le contrat

Bob doit ensuite récupérer les données du contrat qui l’intéresse. Ces données peuvent circuler par n’importe quel canal : site web, e-mail, application de messagerie... En pratique, elles sont groupées dans un ***consignment***, c’est-à-dire un petit paquet de données contenant :
- La **Genesis**, qui définit l’état initial du contrat ;
- Le **Schema**, qui décrit la logique métier (types stricts, scripts de validation, etc.) ;
- L’**Interface**, qui définit la couche de présentation (noms des champs, opérations accessibles) ;
- L’**Interface Implementation**, qui relie concrètement le Schema à l’Interface.

![RGB-Bitcoin](assets/fr/075.webp)

La taille totale est souvent de l’ordre de quelques kilo-octets, car chaque composant pèse généralement moins de 200 octets. Il peut également être possible de diffuser ce consignment en Base58, via des canaux résistants à la censure (comme Nostr ou via le Lightning Network par exemple), ou sous forme de QR code.

#### 3) Import du contrat et validation

Une fois que Bob a reçu le consignment, il l’importe dans son wallet RGB. Celui-ci va alors :
- Vérifier que la Genesis et le Schema sont valides ;
- Charger l’Interface et l’Interface Implementation ;
- Mettre à jour son stash de données côté client.

Bob peut maintenant voir l’actif dans son wallet (même s’il n’en détient pas encore) et comprendre quels sont les champs disponibles, les opérations possibles... Il doit ensuite contacter une personne qui possède effectivement l’actif à transférer. Dans notre exemple, c’est Alice.

Le processus de découverte de qui détient un certain actif RGB s’apparente à la découverte d’un payeur en bitcoins. Les détails de cette mise en relation dépendent des usages (places de marché, canaux de discussion privés, facturation, vente de biens et services, salaire...).

#### 4) Émission d'une invoice

Pour lancer le transfert d’un actif RGB, Bob doit commencer par émettre une invoice. Cette invoice sert à :
- Indiquer à Alice le type d’opération à réaliser (par exemple un `Transfer` issu d’une interface RGB20) ;
- Fournir à Alice la *seal definition* de Bob (c’est-à-dire l’UTXO où il souhaite recevoir l’actif) ;
- Préciser la quantité d’actif souhaitée (par exemple 100 unités).

Bob utilise l’outil `rgb` en ligne de commande. Supposons qu’il souhaite 100 unités d’un jeton dont le `ContractId` est connu, qu’il veut s’appuyer sur `Tapret`, et qu’il spécifie son UTXO (`456e3..dfe1:0`) :

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

Nous étudierons plus précisément la structure des invoices RGB à la fin de ce chapitre.

#### 5) Transmission de l’invoice

L’invoice générée (par exemple sous forme d'URL : `rgb:2WBcas9.../RGB20/100+utxob:...`) contient toutes les informations nécessaires pour qu’Alice puisse préparer le transfert. Comme pour le consignment, elle peut être encodée de manière compacte (Base58 ou un autre format) et envoyée via une application de messagerie, e-mail, Nostr...

![RGB-Bitcoin](assets/fr/076.webp)

#### 6) Préparation de la transaction côté Alice

Alice reçoit l’invoice de Bob. Elle dispose dans son wallet RGB d’un stash où figure l’actif à transférer. Pour dépenser l’UTXO où se situe l’actif, elle doit commencer par générer une PSBT (*Partially Signed Bitcoin Transaction*), c’est-à-dire une transaction Bitcoin incomplète, utilisant l’UTXO qu’elle possède :

```bash
alice$ wallet construct tx.psbt
```

Cette transaction de base (non signée pour le moment) servira de support pour ancrer l’engagement cryptographique lié au transfert vers Bob. L’UTXO d’Alice sera ainsi dépensé, et dans la sortie, on placera le commitment `Tapret` ou `Opret` pour Bob.

#### 7) Génération du consignment de transfert

Ensuite, Alice construit le ***terminal consignment*** (parfois appelé "consignment de transfert") via la commande :

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

Ce nouveau fichier `consignment.rgb` contient :
- L’historique complet des State Transitions nécessaires pour valider l’actif jusqu’à l’instant présent (depuis la Genesis) ;
- La nouvelle State Transition qui transfère l’actif d’Alice vers Bob, selon l’invoice que Bob a émise ;
- La transaction Bitcoin (*witness transaction*) incomplète (`tx.psbt`), qui dépense le Single-use Seal d'Alice, modifiée pour inclure l’engagement cryptographique en faveur de Bob.

À ce stade, la transaction n’est pas encore diffusée sur le réseau Bitcoin. Le consignment est plus volumineux qu’un consignment de base, car il inclut tout l’historique (*proof chain*) pour prouver la légitimité de l’actif.

#### 8) Bob vérifie et accepte le consignment

Alice transmet ce **terminal consignment** à Bob. Bob va alors :
- Vérifier la validité de la State Transition (s’assurer que l’historique est cohérent, que les règles du contrat sont respectées, etc.) ;
- L’ajouter à son stash en local ;
- Générer éventuellement une signature (`sig:...`) sur le consignment, pour prouver qu’il l’a examiné et qu’il donne son accord (on l’appelle parfois un "*payslip*").

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/fr/077.webp)

#### 9) Option : Bob renvoie une confirmation à Alice (*payslip*)

Si Bob le souhaite, il peut renvoyer cette signature à Alice. Cela indique :
- Qu’il reconnaît la transition comme valide ;
- Qu’il est d’accord pour que la transaction Bitcoin soit diffusée.

Ce n’est pas obligatoire, mais cela peut constituer une assurance pour Alice qu’il n’y aura pas de litige par la suite sur ce transfert.

#### 10) Alice signe et publie la transaction

Alice peut alors :
- Vérifier la signature éventuelle de Bob (`rgb check <sig>`) ;
- Signer la *witness transaction* qui est encore une PSBT (`wallet sign`) ;
- Publier la witness transaction sur le réseau Bitcoin (`—publish`).

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/fr/078.webp)

Une fois confirmée, cette transaction marque la conclusion du transfert. Bob devient le nouveau détenteur de l’actif : il possède désormais un Owned State pointant vers l’UTXO qu’il contrôle, prouvé par la présence de l’engagement dans la transaction.

Pour résumer, voici le processus de transfert complet : 

![RGB-Bitcoin](assets/fr/079.webp)

### Avantages des transferts RGB

- **Confidentialité** : 

Seuls Alice et Bob possèdent la totalité des données de la State Transition. Ils échangent ces informations en dehors de la blockchain, via des consignments. Les engagements cryptographiques dans la transaction Bitcoin ne révèlent pas le type d’actif ni le montant, ce qui garantie une confidentialité bien supérieure à celle des autres systèmes de tokens on-chain.

- **Validation côté client** :

Bob peut vérifier seul la cohérence du transfert en confrontant le *consignment* aux *anchors* dans la blockchain Bitcoin. Il n’a pas besoin d’une validation par un tiers. Alice n’a pas à publier l’historique complet sur la blockchain, ce qui allège la charge sur protocole de base et améliore la confidentialité.

- **Atomicité simplifiée** : 

Les échanges complexes (atomic swaps entre BTC et un actif RGB, par exemple) peuvent être réalisés au sein d’une même transaction, ce qui évite l’utilisation de scripts HTLC ou PTLC. Si l’accord n’est pas diffusé, chacun peut réutiliser ses UTXOs autrement.

### Schéma récapitulatif d'un transfert

Avant d'étudier plus en détail les invoices, voici un schéma récapitulatif de flux global d’un transfert RGB :
- Bob installe un wallet RGB et obtient le consignment initial du contrat ;
- Bob émet une invoice mentionnant l’UTXO où recevoir l’actif ;
- Alice reçoit l’invoice, construit la PSBT et génère le terminal consignment ;
- Bob l’accepte, vérifie, ajoute les données à son stash, et éventuellement signe (*payslip*) ;
- Alice publie la transaction sur le réseau Bitcoin ;
- La confirmation de la transaction officialise le transfert.

![RGB-Bitcoin](assets/fr/080.webp)
Le transfert illustre toute la puissance et la souplesse du protocole RGB : un échange privé, validé côté client, ancré de façon minimale et discrète sur la blockchain Bitcoin, et conservant le meilleur de la sécurité du protocole (pas de risque de double dépense). C’est ce qui fait de RGB un écosystème prometteur pour des transferts de valeur plus confidentiels et plus modulables que sur des blockchains programmables on-chain.

### Invoices RGB

Dans cette section, nous allons expliquer en détail la façon dont les **invoices** fonctionnent dans l’écosystème RGB et comment elles permettent de réaliser des opérations (en particulier des transferts) avec un contrat. Nous allons aborder d’abord la question des identifiants utilisés, puis la manière dont ils sont encodés, et enfin la structure d’une invoice exprimée sous forme d’URL (un format assez pratique pour un usage dans les wallets).

#### Identifiants et encodage

Pour chacun des éléments suivants, on définit un identifiant unique :
- Un contrat RGB ;
- Son Schema (logique métier) ;
- Son Interface et son Interface Implementation ;
- Ses actifs (tokens, NFT, etc.),

Cette unicité est très importante, car chaque composant du système doit pouvoir être distingué. Par exemple, un contrat X ne doit pas être confondu avec un autre contrat Y, et deux interfaces différentes (RGB20 vs. RGB21 par exemple) doivent avoir des identifiants distincts.

Pour que ces identifiants soient à la fois efficaces (peu volumineux) et lisibles, on utilise :
- Un encodage en base58, qui évite l’emploi de caractères pouvant créer des confusions (par ex. le `0` et la lettre `O`) et qui fournit des chaînes de caractères relativement courtes ;
- Un préfixe indiquant la nature de l’identifiant, généralement sous forme de `rgb:` ou d’une URN similaire.

Par exemple, un `ContractId` pourra être représenté par quelque chose du type :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Le préfixe `rgb:` confirme qu’il s’agit d’un identifiant RGB, et non pas d’un lien HTTP ou d’un autre protocole. Grâce à ce préfixe, les wallets savent interpréter correctement la chaîne.

#### Segmentation de l'identifiant

Les identifiants RGB sont souvent assez longs, car la sécurité sous-jacente (cryptographique) peut nécessiter des champs de 256 bits ou plus. Pour faciliter la lecture et la vérification humaine, on segmente (*chunk*) ces chaînes en plusieurs blocs séparés par un tiret (`-`). Ainsi, au lieu d’avoir une longue suite ininterrompue de caractères, on la divise en blocs plus courts. Cette pratique est courante pour les numéros de cartes bancaires ou de téléphones, et elle s’applique également ici pour la facilité de vérification. Ainsi, on peut par exemple annoncer à un utilisateur ou un partenaire : "*Vérifie s’il te plaît que le troisième bloc est `9GEgnyMj7`*", plutôt que de devoir comparer la totalité d’un seul coup. Le dernier bloc sert souvent de **checksum**, afin d'avoir un système de détection d’erreurs ou de typos.

À titre d’exemple, un `ContractId` en base58 encodé et segmenté pourrait être :

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Chacun des tirets vient couper la chaîne en sections. Cela n’affecte pas la sémantique du code, seulement sa présentation.

#### Utilisation des URLs pour les Invoices

Une invoice RGB se présente comme une URL. Cela signifie qu’elle peut être cliquée ou scannée (sous forme de QR code), et qu’un wallet pourra directement l’interpréter pour effectuer une opération. Cette simplicité d’interaction diffère de certains autres systèmes où l’on doit copier-coller divers morceaux de données dans différents champs du logiciel.

Une invoice pour un token fongible (par exemple un jeton RGB20) peut ressembler à ceci :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Analysons cette URL :
- **`rgb:`** (préfixe) : indique qu’il s’agit d’un lien invoquant le protocole RGB (analogue à `http:` ou `bitcoin:` dans d’autres contextes) ;
- **`2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`** : représente le `ContractId` du jeton que l’on veut manipuler ;
- **`/RGB20/100`** : indique qu’on utilise l’interface `RGB20` et qu’on demande 100 unités de l’actif. La syntaxe est donc : `/Interface/amount` ;
- **`+utxob:`** : spécifie qu’on ajoute l’information sur l’UTXO destinataire (ou plus exactement la définition du Single-use Seal) ;
- **`egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`** : c’est le *blinded* UTXO (ou seal definition). Autrement dit, Bob a masqué son UTXO exact, donc l’expéditeur (Alice) ne sait pas quelle est l’adresse exacte. Elle sait seulement qu’il y a un sceau valide se référant à un UTXO contrôlé par Bob.

Le fait que tout tienne dans une seule URL facilite la vie de l’utilisateur : un simple clic ou un scan dans le wallet, et l’opération est prête à être exécutée.

On pourrait imaginer des systèmes où l’on emploie un simple ticker (ex. `USDT`) à la place du `ContractId`. Cela poserait néanmoins de gros problèmes de confiance et de sécurité : un ticker n’est pas une référence unique (plusieurs contrats peuvent prétendre s’appeler "USDT"). Sur RGB, on veut un identifiant cryptographique unique, sans ambiguïté. D’où l’adoption de la chaîne de 256 bits, encodée en base58 et segmentée. L’utilisateur sait qu’il manipule précisément le contrat dont l’ID est `2WBcas9-yjz...` et pas un autre.

#### Paramètres supplémentaires dans l’URL

On peut également ajouter des paramètres supplémentaires à l’URL, de la même façon qu’avec HTTP, comme par exemple :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```

- `?sig=...` : représente par exemple une signature associée à l’invoice, que certains wallets peuvent vérifier ;
- Si un wallet ne gère pas cette signature, il ignore simplement ce paramètre.

Prenons maintenant le cas d’un NFT via l’interface RGB21. On pourrait par exemple avoir :

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Ici, on voit :
- **`rgb:`** : préfixe de l’URL ;
- **`7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`** : ID du contrat (NFT) ;
- **`RGB21`** : interface pour les actifs non fongibles (NFT) ;
- **`DbwzvSu-4BZU81jEp-...`** : une référence explicite à la partie unique du NFT, par exemple un hash du blob de données (média, métadonnées…) ;
- **`+utxob:egXsFnw-...`** : la seal definition.

L’idée est la même : transmettre un lien unique que le wallet sait interpréter, en identifiant clairement l’actif unique à transférer.

#### Autres opérations via URL

Les URLs RGB ne servent pas uniquement à demander un transfert. Elles peuvent aussi encoder des opérations plus avancées, comme l’émission de nouveaux tokens (*issuance*). Par exemple :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Ici, on retrouve :
- `rgb:` : protocole ;
- `2WBcas9-...` : ID du contrat ;
- `/RGB20/issue/100000` : indique qu’on veut invoquer la transition "*Issue*" pour créer 100000 jetons supplémentaires ;
- `+utxob:` : la seal definition.

Ainsi, le wallet pourra comprendre : "*On me demande d’effectuer une opération `issue` depuis l’interface `RGB20`, sur tel contrat, pour 100000 unités, au profit de tel Single-use Seal.*"

Maintenant que nous avons étudié les principaux éléments liés à la programmation sur RGB, je vous propose, dans le chapitre suivant, de rédiger un contrat RGB.

## Rédaction de contrats intelligents
<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

![video](https://youtu.be/GRwS-NvWF3I)

Dans ce chapitre, nous allons suivre pas à pas la rédaction d'un contrat, en utilisant l’outil en ligne de commande `rgb`. L’objectif est de montrer comment installer et manipuler la CLI, compiler un **Schema**, importer l’**Interface** et l’**Interface Implementation**, puis émettre (*issue*) un actif. Nous verrons également la logique sous-jacente, avec la compilation et la validation de l’état. À l’issue de ce chapitre, vous devriez être en mesure de reproduire la démarche et de créer vos propres contrats RGB.

Pour rappel, la logique interne de RGB repose sur des bibliothèques Rust que vous, en tant que développeurs, pouvez importer dans vos projets pour gérer la partie Client-side Validation. En complément, l’équipe de l'Association LNP/BP travaille à proposer des bindings pour d’autres langages, mais ce n’est pas encore finalisé. Par ailleurs, d’autres entités comme Bitfinex développent leurs propres stacks d’intégration (nous en parlerons dans les 2 derniers chapitres de la formation). La CLI `rgb` constitue donc pour l’instant la référence officielle, même si elle reste relativement brute de décoffrage.

### Installation et présentation de l’outil rgb

La commande principale se nomme simplement `rgb`. Elle est conçue de façon à rappeler l’usage de `git`, avec un ensemble de sous-commandes pour manipuler les contrats, les invoquer, émettre des assets, etc. Actuellement, la partie Bitcoin Wallet n’y est pas intégrée, mais va l’être dans une version imminente (0.11). Cette prochaine version permettra de créer et gérer ses wallets (via des descriptors) directement depuis `rgb`, y compris la génération de PSBT, la compatibilité avec du matériel externe (par exemple un hardware wallet) pour la signature, ou encore l’interopérabilité avec des logiciels comme Sparrow. Le scénario complet d’émission et de transfert d’actif deviendra ainsi plus simple.

#### Installation via Cargo

On installe l’outil en Rust avec :

```bash
cargo install rgb-contracts --all-features
```

(Remarque : le crate s’appelle `rgb-contracts`, et la commande installée sera nommée `rgb`. S’il existait déjà un crate nommé `rgb`, il aurait pu y avoir collision, d’où cette dénomination.)

L’installation compile un grand nombre de dépendances (par exemple le parsing de la commande, l’intégration avec Electrum, la gestion des zero-knowledge proofs, etc.).

Une fois l’installation terminée, on dispose de la commande :

```bash
rgb
```

L’exécution de `rgb` (sans argument) affiche la liste des sous-commandes disponibles, comme `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer`, etc. Il est possible de modifier le répertoire de stockage local (un stash qui conserve les consignments, schémas et implémentations), de choisir le réseau (testnet, mainnet) ou de configurer son Electrum server.

![RGB-Bitcoin](assets/fr/081.webp)

#### Premier aperçu des commandes

Lorsqu’on exécute la commande suivante, on voit qu’une interface `RGB20` est déjà intégrée par défaut :

```bash
rgb interfaces
```

Si jamais cette interface n'est pas intégrée, clonez le dépôt des interfaces :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Compilez-le :

```bash
cargo run
```

Puis importez l'interface de votre choix :

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/fr/082.webp)

En revanche, on nous indique qu’aucun schema n’est encore importé dans le logiciel. Il n’y a pas non plus de contrat dans le stash. Pour le voir, exécutez la commande :

```bash
rgb schemata
```

Vous pouvez alors cloner le dépôt pour récupérer certains schémas :

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/fr/083.webp)

Ce dépôt contient, dans son répertoire `src/`, plusieurs fichiers Rust (par exemple `nia.rs`) qui définissent des schémas (NIA pour "*Non Inflatable Asset*", UDA pour "*Unique Digital Asset*", etc.). On peut alors exécuter pour compiler :

```bash
cd rgb-schemata
cargo run
```

Cela génère plusieurs fichiers `.rgb` et `.rgba` qui correspondent aux schémas compilés. Par exemple, on peut y trouver `NonInflatableAsset.rgb`.

#### Import du Schema et de l’Interface Implementation

Vous pouvez maintenant importer le schéma dans `rgb` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/fr/084.webp)

Cela permet de l'ajouter dans le stash local. Si on exécute la commande suivante, on constate que le schéma apparaît désormais :

```bash
rgb schemata
```

### Création d’un contrat (issuing)

Pour créer un nouvel actif, il y a deux approches :
- Soit on utilise un script ou code en Rust qui construit un Contract en alimentant les champs du schéma (global state, Owned States, etc.) et produit un fichier `.rgb` ou `.rgba` ;
- Soit on utilise directement la sous-commande `issue`, avec un fichier YAML (ou TOML) décrivant les propriétés du token.

Vous pouvez retrouver des exemples en Rust dans le dossier `examples` qui illustrent comment on construit un `ContractBuilder`, on renseigne le `global state` (nom de l’actif, ticker, supply, date, etc.), on définit l’Owned State (à quel UTXO il est assigné), puis on compile tout cela en un *contract consignment* qu’on peut exporter, valider et importer dans un stash.

L'autre manière est donc d'éditer manuellement un fichier YAML pour personnaliser le `ticker`, le `name`, la `supply`, etc. Supposons que le fichier s’appelle `RGB20-demo.yaml`. On peut y spécifier :
- `spec` : ticker, nom, precision ;
- `terms` : un champ de mentions légales ;
- `issuedSupply` : le montant de token émis ;
- `assignments` : indique le Single-use Seal (*seal definition*) et la quantité débloquée.

Voici un exemple de fichier YAML à créer :

```yaml
interface: RGB20Fixed

globals:
  spec:
    ticker: PBN
    name: Plan B Network
    details: "Pay attention: the asset has no value"
    precision: 2
  terms:
    text: >
      SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
    media: ~
  issuedSupply: 100000000

assignments:
  assetOwner:
    seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
    amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/fr/085.webp)

Ensuite, il suffit d'exécuter la commande :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/fr/086.webp)

Dans mon cas, l'identifiant unique du schéma (à mettre entre guillemets simples) est `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` et je n'ai mis aucun issuer. Ma commande est donc :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Si vous ne connaissez pas l'ID du schéma, exécutez la commande :

```bash
rgb schemata
```

La CLI répond qu’un nouveau contrat a été émis et ajouté au stash. Si on tape la commande suivante, on voit qu’il y a désormais un contrat supplémentaire, correspondant à celui qu’on vient d’émettre :

```bash
rgb contracts
```

![RGB-Bitcoin](assets/fr/087.webp)

 Puis, la commande suivante permet d'afficher les global states (le nom, le ticker, la supply...) et la liste des Owned States, c’est-à-dire les allocations (par exemple, 1 million de token `PBN` définis dans l'UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/fr/088.webp)

### Export, import et validation

Pour partager ce contrat avec d’autres utilisateurs, on peut l’exporter depuis le stash vers un fichier :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/fr/089.webp)

Le fichier `myContractPBN.rgb` peut être transmis à un autre utilisateur, lequel pourra l’ajouter dans son stash avec la commande  :

```bash
rgb import myContractPBN.rgb
```

À l’import, si c’est un simple *contract consignment*, on aura un message "`Importing consignment rgb`". S’il s’agit d’un *state transition consignment* plus volumineux, la commande sera différente (`rgb accept`).

Pour s’assurer de la validité, on peut aussi utiliser la fonctionnalité de validation en local. On pourrait exécuter par exemple :

```bash
rgb validate myContract.rgb
```

#### Utilisation du stash, vérification et affichage

Pour rappel, le stash est un inventaire en local qui conserve à la fois les schémas, les interfaces, les implémentations et les contrats (Genesis + transitions). Chaque fois qu’on exécute "`import`", on ajoute un élément au stash. On peut visualiser ce stash en détail avec la commande :

```bash
rgb dump
```

![RGB-Bitcoin](assets/fr/090.webp)

Cela va générer un dossier avec le détail de tout le stash.

### Transfert et PSBT

Pour réaliser un transfert, il va falloir manipuler un wallet Bitcoin en local pour gérer les engagements `Tapret` ou `Opret`.

#### Générer une invoice

Dans la plupart des cas, l’interaction entre les participants d’un contrat (par exemple Alice et Bob) se fait via la génération d’une invoice. Si Alice souhaite que Bob exécute quelque chose (un transfert de tokens, une réémission, une action dans une DAO, etc.), Alice crée une invoice qui détaille ses instructions à Bob. On a donc :
- **Alice** (l'émettrice de l’invoice) ;
- **Bob** (qui reçoit et exécute l’invoice).

Contrairement à d’autres écosystèmes, une invoice RGB ne se limite pas à la notion de paiement. Elle peut embarquer n’importe quelle requête liée au contrat : révoquer une clé, voter, créer une gravure (*engraving*) sur un NFT, etc. L’opération correspondante peut être décrite dans l’interface du contrat.

La commande suivante vous permet de générer une invoice RGB :

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Avec :
- `$CONTRACT` : l’identifiant du contrat (*ContractId*) ;
- `$INTERFACE` : l’interface à utiliser (par exemple `RGB20`) ;
- `$ACTION` : le nom de l’opération prévue dans l’interface (pour un simple transfert de token fongible, cela peut être "Transfer"). Si l'interface prévoit déjà une action par défaut, vous n'avez pas besoin de la renseigner de nouveau ici ;
- `$STATE` : la donnée d’état à transférer (par exemple un montant de tokens si on fait un transfert de token fongible) ;
- `$SEAL` : le Single-use Seal du bénéficiaire (Alice), c'est-à-dire une référence explicite à un UTXO. Bob utilisera cette info pour construire la witness transaction, et l’output correspondant appartiendra ensuite à Alice (sous forme *blinded UTXO* ou en clair).

Par exemple, avec les commandes suivantes :

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'

alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1

alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

La CLI va générer une invoice du style :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Elle peut être transmise à Bob par n’importe quel canal (texte, QR code, etc.).

#### Effectuer un transfert

Pour réaliser un transfert à partir de cette invoice :
- Bob (qui détient les tokens dans son stash) dispose d’un wallet Bitcoin. Il doit préparer une transaction Bitcoin (sous forme de PSBT, par ex. `tx.psbt`) qui dépense les UTXOs où se trouvent les tokens RGB nécessaires, plus un UTXO pour la monnaie (change) ;
- Bob exécute la commande suivante :

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```

- Cela génère un fichier `consignment.rgb`  qui contient :
	- L’historique des transitions prouvant à Alice que les tokens sont authentiques ;
	- La nouvelle transition qui transfère les tokens vers le Single-use Seal d’Alice ;
	- Une witness transaction (non signée).

- Bob envoie ce fichier `consignment.rgb` à Alice (par e-mail, un serveur de partage ou un protocole RGB-RPC, Storm, etc.) ;
- Alice reçoit `consignment.rgb` et l’accepte dans son propre stash :

```bash
alice$ rgb accept consignment.rgb
```

- La CLI vérifie la validité de la transition et l’ajoute au stash d’Alice. Si c’est invalide, la commande échoue avec des messages d’erreur détaillés. Sinon, elle réussit, et signale que la transaction témoin n’est pas encore diffusée sur le réseau Bitcoin (Bob attend le feu vert d’Alice) ;
- En guise de confirmation, la commande `accept` renvoie une signature (*payslip*) qu’Alice peut envoyer à Bob pour lui montrer qu’elle a bien validé le *consignment* ;
- Bob peut alors signer et publier (`--publish`) sa transaction Bitcoin :

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```

- Dès que cette transaction est confirmée on-chain, la propriété de l’actif est considérée comme transférée à Alice. Le wallet d’Alice, en surveillant le minage de la transaction, voit apparaître la nouvelle Owned State dans son stash.

Dans le prochain chapitre, nous aborderons plus en détail l'intégration de RGB au Lightning Network.

## RGB sur le Lightning Network
<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

![video](https://youtu.be/mqCupTlDbA0)

Dans ce chapitre, je vous propose d'examiner comment RGB peut être utilisé au sein du Lightning Network, afin d’intégrer et de déplacer des actifs RGB (tokens, NFT, etc.) via des canaux de paiement off-chain.

L’idée fondamentale est que la transition d’état RGB (*State Transition*) peut être engagée dans une transaction Bitcoin qui, elle-même, peut rester off-chain tant que le canal Lightning n’est pas fermé. Ainsi, à chaque mise à jour de canal, on peut incorporer une nouvelle transition d’état RGB dans la nouvelle transaction d'engagement, qui invalide alors l’ancienne transition. De cette façon, des canaux Lightning peuvent servir à transférer des actifs RGB, et on peut les router comme on le ferait pour des paiements Lightning classiques.

### Création d'un canal et funding

Pour créer un canal Lightning qui transporte des actifs RGB, on a besoin de deux éléments :
- Un funding en bitcoins afin de créer le multisig 2/2 du canal (l’UTXO de base pour le canal) ;
- Un funding RGB, qui envoie les actifs sur ce même multisig.

Sur le plan de Bitcoin, la transaction de funding doit exister pour définir l’UTXO de référence, même si elle ne contient qu’une petite quantité de sats (il faut simplement que chaque sortie dans les futures transactions d'engagement restent au-dessus du dust limit tout de même). Par exemple, Alice peut décider de fournir 10k sats et 500 USDT (émis sous forme d’un actif RGB). Sur la transaction de funding, on ajoute un engagement (`Opret` ou `Tapret`) qui ancre la transition d’état RGB.

![RGB-Bitcoin](assets/fr/091.webp)

Une fois la transaction de funding préparée (mais pas encore diffusée), on crée les transactions d'engagement pour que chaque partie puisse, à tout moment, fermer le canal unilatéralement. Ces transactions ressemblent aux transactions d'engagement classiques de Lightning, à la différence qu’on y ajoute une sortie supplémentaire contenant l’ancre RGB (OP_RETURN ou Taproot) liée à la nouvelle transition d’état.

La transition d’état RGB déplace alors les actifs depuis le multisig 2/2 du funding vers les sorties de la transaction d'engagement. L’avantage ce ce processus est que la sécurité de l’état RGB se cale exactement sur la mécanique punitive de Lightning : si Bob diffuse un ancien état du canal, Alice peut le punir et dépenser la sortie, afin de récupérer à la fois les sats et les tokens RGB. L’incitation est donc plus forte encore que dans un canal Lightning sans actif RGB, puisqu’un attaquant peut perdre non seulement des sats, mais aussi les actifs RGB du canal.

Une transaction d'engagement signée par Alice et envoyée à Bob ressemblera donc à cela :

![RGB-Bitcoin](assets/fr/092.webp)

Et la transaction d'engagement qui va de paire, signée par Bob et envoyée à Alice ressemblera à cela :

![RGB-Bitcoin](assets/fr/093.webp)

### Mise à jour du canal

Lorsqu’un paiement se produit entre deux participants du canal (ou qu’ils souhaitent modifier la répartition des actifs), ils créent une nouvelle paire de transactions d'engagement. Le montant en sats sur chaque sortie peut rester inchangé ou non, selon l’implémentation, car son rôle principal est de permettre la construction d’UTXOs valides. En revanche, la sortie OP_RETURN (ou Taproot) doit être modifiée pour contenir le nouvel ancrage RGB, représentant la nouvelle répartition des actifs dans le canal.

Par exemple, si Alice transfère 30 USDT à Bob dans le canal, la nouvelle transition d’état va refléter un solde de 400 USDT pour Alice et 100 USDT pour Bob. La transaction d'engagement se voit ajouter (ou modifier) l’ancrage OP_RETURN/Taproot pour inclure cette transition. À noter que, du point de vue de RGB, l’input dans la transition reste le multisig initial (où sont réellement alloués les assets on-chain jusqu’à la fermeture du canal). Seules les sorties RGB (allocations) changent, selon la redistribution décidée.

La transaction d'engagement signée par Alice, prête à être diffusée par Bob :

![RGB-Bitcoin](assets/fr/094.webp)

La transaction d'engagement signée par Bob, prête à être diffusée par Alice :

![RGB-Bitcoin](assets/fr/095.webp)

### Gestion des HTLCs

Dans la réalité, le Lightning Network permet le routage de paiements via des canaux multiples, en utilisant des HTLCs (*Hashed Time-Locked Contracts*). C’est identique avec RGB : pour tout paiement en transit dans le canal, on ajoute une sortie HTLC à la transaction d'engagement et une allocation RGB liée à cet HTLC. Ainsi, celui qui dépense la sortie HTLC (grâce au secret ou après expiration du timelock) récupère à la fois les sats et les actifs RGB associés. En revanche, il faut évidemment avoir sur la route suffisamment de liquidités à la fois en sats et en actif RGB.

![RGB-Bitcoin](assets/fr/096.webp)

Le fonctionnement de RGB sur Lightning doit donc être considéré en parallèle avec celui du Lightning Network lui-même. Si vous désirez approfondir ce sujet, je vous recommande vivement de consulter cette autre formation complète :

https://planb.network/courses/lnp201


### Plan du code de RGB

Pour terminer et avant de passer à la section suivante, je voudrais vous faire un récapitulatif du code utilisé sur RGB. Le protocole repose sur un ensemble de librairies Rust et de spécifications open source. Voici un panorama des principaux dépôts et crates :

![RGB-Bitcoin](assets/fr/097.webp)

#### Client-side Validation

- **Repository** : [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- **Crates** : [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)

Gestion de la validation off-chain et de la logique des Single-use Seals.

#### Deterministic Bitcoin Commitments (DBC)

- **Repository** : [bp-core](https://github.com/BP-WG/bp-core)
- **Crate** : [bp-dbc](https://crates.io/crates/bp-dbc)

Gestion de l’ancrage déterministe dans les transactions Bitcoin (Tapret, OP_RETURN, etc.).

#### Multi Protocol Commitment (MPC)

- **Repository** : [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- **Crate** : [commit_verify](https://crates.io/crates/commit_verify)

Combinaisons d’engagements multiples et intégration avec différents protocoles.

#### Strict Types & Strict Encoding

- **Spécifications** : [site web strict-types.org](https://www.strict-types.org/)
- **Repositories** : [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- **Crates** : [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

Le système de typage strict et la sérialisation déterministe utilisés pour la validation côté client.

#### RGB Core

- **Repository** : [rgb-core](https://github.com/RGB-WG/rgb-core)
- **Crate** : [rgb-core](https://crates.io/crates/rgb-core)

Cœur du protocole, qui englobe la logique principale de la validation RGB.

#### RGB Standard Library & Wallet

- **Repository** : [rgb-std](https://github.com/RGB-WG/rgb-std)
- **Crate** : [rgb-std](https://crates.io/crates/rgb-std)

Implémentations standard, gestion du stash et wallet.

#### RGB CLI

- **Repository** : [rgb](https://github.com/RGB-WG/rgb)
- **Crates** : [rgb-cli](https://crates.io/crates/rgb-cli), [rgb-wallet](https://crates.io/crates/rgb-wallet)

La CLI `rgb` et le crate wallet, qui permettent de manipuler les contrats en ligne de commande.

#### RGB Schema

- **Repository** : [rgb-schemata](https://github.com/RGB-WG/rgb-schemata/)

Contient des exemples de schémas (NIA, UDA, etc.) et leurs implémentations.

#### ALuVM

- **Info** : [aluvm.org](https://www.aluvm.org/)
- **Repositories** : [aluvm-spec](https://github.com/AluVM/aluvm-spec), [alure](https://github.com/AluVM/alure)
- **Crates** : [aluvm](https://crates.io/crates/aluvm), [aluasm](https://crates.io/crates/aluasm)

Machine virtuelle registry-based utilisée pour exécuter les scripts de validation.

#### Bitcoin Protocol - BP

- **Repositories** : [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-wallet](https://github.com/BP-WG/bp-wallet)

Compléments pour la prise en charge du protocole Bitcoin (transactions, dérivations, etc.).

#### Ubiquitous Deterministic Computing - UBIDECO

- **Repository** : [UBIDECO](https://github.com/UBIDECO)

Écosystème lié aux développements déterministes open-source.


# Construire sur RGB
<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA et le projet Bitmask
<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

![video](https://youtu.be/nbUtV8GOR_U)

Cette dernière section de la formation provient de présentations effectuées par différents intervenants lors du bootcamp sur RGB. Elle comprend des témoignages et des réflexions concernant RGB et son écosystème, ainsi que des présentations d'outils et de projets basés sur le protocole. Ce premier chapitre est animé par Hunter Beast et les deux suivants le seront par Frederico Tenga.

### De JavaScript à Rust, et l’entrée dans l’écosystème Bitcoin

Au début, Hunter Beast travaillait principalement en JavaScript. Puis il a découvert **Rust**, dont la syntaxe lui semblait peu attrayante et frustrante au départ. Cependant, il en est venu à apprécier la puissance offerte par ce langage, le contrôle sur la mémoire (*heap* et *stack*), ainsi que la sécurité et les performances qui en découlent. Il souligne que Rust constitue une excellente formation pour comprendre en profondeur comment fonctionne un ordinateur.

Hunter Beast raconte son passé dans divers projets de l’écosystème des *altcoins*, comme Ethereum (avec du Solidity, du TypeScript, etc.), et plus tard Filecoin. Il explique avoir été d’abord impressionné par certains protocoles, mais avoir fini par se sentir désillusionné par la plupart, notamment à cause de leur tokenomics. Il dénonce les incitations financières douteuses, la création inflationniste des tokens qui dilue les investisseurs, et l’aspect possiblement exploitative de ces projets. Il finit donc par adopter une posture de **Bitcoin maximaliste**, notamment parce que certaines personnes lui ont ouvert les yeux sur les mécanismes économiques plus sains de Bitcoin, et sur la robustesse de ce système.

### L’attrait pour RGB et la construction sur des layers

Ce qui l’a définitivement convaincu de la pertinence de Bitcoin, selon ses dires, est la découverte de RGB et du concept de layers. Il considère que les fonctionnalités existantes sur d’autres blockchains pourrait être reproduites sur des couches supérieures, au-dessus de Bitcoin, sans altérer le protocole de base.

En février 2022, il rejoint **DIBA** pour travailler précisément sur RGB, et en particulier sur le wallet **Bitmask**. À l’époque, Bitmask en était encore à la version 0.01 et exploitait RGB en version 0.4, uniquement pour la gestion de tokens simples. Il note que c’était moins tourné vers la self-custody qu’aujourd’hui, car la logique reposait en partie sur un serveur. Depuis, l’architecture a évolué vers ce modèle apprécié par les bitcoiners.

### Les fondements du protocole RGB

Le protocole **RGB** est la concrétisation la plus récente et la plus poussée du concept de _colored coins_, déjà exploré vers 2012-2013. À l’époque, plusieurs équipes cherchaient à associer de la valeur différente du bitcoin sur des UTXOs, ce qui a mené à de multiples implémentations dispersées. Ce manque de standardisation et la faible demande de l’époque ont empêché ces solutions de s’imposer durablement.

RGB se distingue aujourd’hui par sa solidité conceptuelle et ses spécifications unifiées via l’association LNP/BP. Le principe repose sur une validation en dehors de la blockchain (Client-side Validation). La blockchain Bitcoin ne stocke que des engagements cryptographiques (_commitments_, via Taproot ou OP_RETURN), tandis que la majorité des données (définition des contrats, historiques de transferts, etc.) se conserve chez les utilisateurs concernés. Ainsi, la charge de stockage est répartie et la confidentialité des échanges est renforcée, sans alourdir la blockchain. Cette approche permet la création d’actifs fongibles (standard **RGB20**) ou d’actifs uniques (standard **RGB21**), dans un cadre modulaire et évolutif.

### La fonction de tokens (RGB20) et d’actifs uniques (RGB21)

Avec **RGB20**, on définit un jeton fongible sur Bitcoin. L’émetteur choisit un _supply_, une _precision_, et crée un _contrat_ dans lequel il peut ensuite effectuer des transferts. Chaque transfert fait référence à un UTXO Bitcoin, qui agit comme un *Single-use Seal*. Cette logique garantit que l’utilisateur ne pourra pas dépenser le même actif deux fois, puisque seule la personne capable de dépenser l’UTXO détient effectivement la clé permettant d’actualiser l’état du contrat côté client.

**RGB21** cible quant à lui les actifs uniques (ou "NFT"). L’actif a une supply de 1, et on peut y associer des métadonnées (fichier image, audio, etc.) décrites via un champ spécifique. Contrairement aux NFT sur des blockchains publiques, les données et leurs identifiants MIME peuvent rester privées, diffusées de pair à pair selon la volonté du propriétaire.

### La solution Bitmask : un wallet pour RGB

Pour exploiter concrètement les capacités de RGB, le projet **DIBA** a conçu un wallet baptisé [Bitmask](https://bitmask.app/). L’idée est de fournir un outil non custodial, basé sur Taproot, accessible comme une application web ou une extension de navigateur. Bitmask gère à la fois des actifs RGB20 et RGB21, et intègre divers mécanismes de sécurisation :
- Le code central est écrit en Rust, puis compilé en WebAssembly pour s’exécuter dans un environnement JavaScript (React) ;
- Les clés sont générées localement, puis stockées chiffrées en local ;
- Les données relatives à l’état (stash) sont maintenues dans un stock en mémoire, sérialisées et chiffrées via la bibliothèque **Carbonado**, qui effectue compression, correction d’erreurs, chiffrement et vérification du flux en utilisant Blake3.

Grâce à cette architecture, toutes les opérations sur les actifs se font côté client. La transaction Bitcoin n’est, de l’extérieur, qu’une transaction de dépense Taproot classique, dont personne ne peut soupçonner qu’elle véhicule aussi un transfert de tokens fongibles ou de NFT. L’absence de surcharge on-chain (pas de métadonnées stockées publiquement) garantit une certaine discrétion et permet de mieux résister aux éventuelles tentatives de censure.

### Sécurité et architecture distribuée

Dans la mesure où le protocole RGB exige que chaque participant conserve son historique de transactions (pour prouver la validité des transferts qu’il reçoit), la question du stockage se pose. Bitmask propose de sérialiser ce stash localement, puis de l’envoyer vers plusieurs serveurs ou clouds (optionnellement). Les données restent chiffrées par l’utilisateur via **Carbonado** ; ainsi, un serveur ne peut pas lire ces informations. En cas de corruption partielle, la couche de correction d’erreurs peut reconstituer le contenu.

L’usage du CRDT (_Conflict-free replicated data type_) permet de fusionner différentes versions du stash si jamais elles divergent. Chacun est libre d’héberger ces données où il le souhaite, car aucun full node unique ne porte la totalité des informations liées à l’actif. Cela reflète exactement la philosophie *Client-side Validation*, où chaque propriétaire est responsable du stockage des preuves de la validité de son actif RGB.

### Vers un écosystème plus large : marketplace, interopérabilité et nouvelles fonctionnalités

La société derrière Bitmask ne se limite pas au simple développement d'un wallet. DIBA entend développer :
- Une **marketplace** pour échanger les tokens, notamment sous forme **RGB21** ;
- Une compatibilité avec d’autres wallets (comme *Iris Wallet*) ;
- Des techniques de **transfer batching**, c’est-à-dire la possibilité d’inclure plusieurs transferts RGB successifs dans une seule transaction.

En parallèle, certains développements portent sur **WebBTC** ou **WebLN** (des standards permettant à des sites web de demander au wallet de signer des opérations Bitcoin ou Lightning), ainsi que sur la capacité de "télébrûler" des inscriptions Ordinals (si on veut rapatrier l’Ordinals vers un format RGB plus discret et plus flexible).

### Conclusion

L’ensemble de cette démarche montre comment l’écosystème RGB peut être déployé et rendu accessible à des utilisateurs finaux grâce à des solutions techniques robustes. La transition d’une perspective altcoin vers une vision plus centrée sur Bitcoin, couplée à la découverte de la *Client-side Validation*, illustre un cheminement assez logique : on comprend qu’il est possible d’implémenter des fonctionnalités variées (tokens fongibles, NFT, smart contracts…) sans forker la blockchain, simplement en profitant d’engagements cryptographiques sur des transactions Taproot ou des OP_RETURN.

Le wallet **Bitmask** s'inscrit dans cette démarche : côté blockchain, on ne voit qu’une transaction Bitcoin banale ; côté utilisateur, on manipule une interface web où l’on crée, échange, et stocke toutes sortes d’actifs off-chain. Ce modèle dissocie clairement l’infrastructure monétaire (Bitcoin) de la logique d’émission et de transferts (RGB), tout en assurant une grande confidentialité et un meilleur passage à l’échelle.

## Les travaux de Bitfinex sur RGB
<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

![vidéo](https://youtu.be/5iAhsgCSL3U)

Dans ce chapitre établi sur la présentation de Frederico Tenga, nous étudions un ensemble d’outils et de projets créés par l'équipe de Bitfinex dédiée à RGB, dans l’optique de favoriser l’émergence d’un écosystème riche et diversifié autour de ce protocole. L’équipe n’a pas, au départ, l’objectif de sortir un produit commercial précis ; elle s’emploie plutôt à mettre à disposition des briques logicielles, à contribuer au protocole RGB lui-même, et à proposer des références de mise en œuvre concrètes comme un wallet mobile (*Iris Wallet*) ou un nœud Lightning compatible RGB.

### Contexte et objectifs

Depuis environ 2022, l’équipe Bitfinex spécialisée dans RGB se concentre sur le développement de la pile technologique permettant d’exploiter et de tester efficacement RGB. Plusieurs contributions ont été réalisées :
- Participation au code source et aux spécifications du protocole, notamment la rédaction de propositions d’amélioration, la correction de bugs, etc ;
- Mise à disposition d’outils à destination des développeurs pour simplifier l’intégration de RGB dans leurs applications ;
- Conception d’un wallet mobile nommé [Iris](https://iriswallet.com/) pour expérimenter et illustrer les bonnes pratiques d’utilisation de RGB ;
- Réalisation d’un nœud Lightning personnalisé, apte à gérer des canaux avec des actifs RGB ;
- Accompagnement d’autres équipes qui bâtissent des solutions sur RGB, afin d’encourager la diversité et la solidité de l’écosystème.

Cette approche vise à couvrir toute la chaîne de besoins : de la librairie de bas niveau (*[RGBlib](https://github.com/RGB-Tools/rgb-lib)*), permettant l’implémentation d’un wallet, jusqu’à l’aspect mise en production (un nœud Lightning, un wallet pour Android, etc.).

### La librairie RGBlib : simplifier le développement d’applications RGB

Un point important pour démocratiser la création de wallets et d’applications RGB réside dans la mise à disposition d’une abstraction suffisamment simple pour que les développeurs n’aient pas à tout apprendre de la logique interne du protocole. C’est précisément l’objectif de **RGBlib**, écrite en Rust.

RGBlib joue le rôle de passerelle entre les exigences très flexibles (mais parfois complexes) de RGB que nous avons pu étudier dans les chapitres précédents, et les besoins concrets d’un développeur d’application. En d’autres termes, un wallet (ou un service) qui souhaite gérer des transferts de tokens, des émissions d’assets, des vérifications, etc., peut s’appuyer sur RGBlib sans connaître chaque détail cryptographique ou chaque paramètre customisable de RGB.

La librairie propose :
- Des fonctions clé en main pour l’émission (_issuance_) d’actifs (fongibles ou non) ;
- La possibilité de transférer (envoyer/réceptionner) des assets en manipulant des objets simples (adresses, montants, UTXOs, etc.) ;
- Un mécanisme pour stocker et charger les informations d’état (*consignments*) indispensables à la Client-side Validation.

RGBlib repose donc sur des notions complexes propres à RGB (Client-side Validation, ancrages Tapret/Opret), mais les encapsule pour que l’application finale n’ait pas à tout reprogrammer ni à prendre de décisions hasardeuses. De plus, RGBlib est déjà bindée dans plusieurs langages (Kotlin et Python), ce qui ouvre la porte à des usages plus larges qu’un simple univers en Rust.

### Iris Wallet : un exemple de wallet RGB sur Android

Pour prouver l’efficacité de RGBlib, l’équipe de Bitfinex a développé **Iris Wallet**, exclusivement sur Android à ce stade. Il s’agit d’un wallet mobile permettant d’illustrer un parcours utilisateur proche d’un wallet Bitcoin ordinaire : on peut y émettre un asset, l’envoyer, le recevoir, et voir son historique, tout en restant sur un modèle de self-custody.

Iris dispose de certaines caractéristiques intéressantes :

**Utilisation d’un serveur Electrum :**

Comme tout wallet, Iris doit connaître les confirmations de transactions sur la blockchain. Plutôt que d’embarquer un nœud complet, Iris s’appuie par défaut sur un serveur Electrum maintenu par l’équipe de Bitfinex. L’utilisateur, s’il le souhaite, peut cependant configurer son propre serveur ou un autre service tiers. Ainsi, la validation des transactions Bitcoin et la récupération d’informations (indexation) se fait de façon modulable.

**Le serveur proxy RGB :**

Contrairement à Bitcoin, RGB exige l’échange de métadonnées off-chain (*consignments*) entre l’expéditeur et le receveur. Pour simplifier ce procesus, Iris propose une solution où la communication s’effectue via un serveur proxy. Le wallet destinataire génère une *invoice* mentionnant notamment où l’expéditeur doit envoyer les données *client-side*. Par défaut, l’URL pointe vers un proxy hébergé par l’équipe de Bitfinex, mais il demeure possible de changer ce proxy (ou d’en héberger un soi-même). L’idée est de retrouver une expérience utilisateur familière où le destinataire affiche un QR code, et l’expéditeur scanne ce code pour la transaction, sans manipulations supplémentaires complexes.

**Sauvegarde en continu :**

Dans un contexte strictement Bitcoin, sauvegarder sa seed suffit généralement (même si de nos jours on conseille plutôt de sauvegarder la seed et les descriptors). Avec RGB, c’est insuffisant : on doit aussi conserver l’historique local (les *consignments*) prouvant qu’on possède vraiment un actif RGB. À chaque réception, l’appareil stocke de nouvelles données indispensables à la dépense ultérieure. Iris gère automatiquement un backup chiffré dans le Google Drive de l’utilisateur. Cela n’exige aucune confiance particulière en Google, car la sauvegarde est chiffrée et il est prévu, dans l’avenir, des options plus robustes (comme un serveur personnel) pour éviter tout risque de censure ou de suppression par un opérateur tiers.

**Autres fonctionnalités :**

- Possibilité de créer un faucet pour tester ou distribuer rapidement des tokens à des fins d’expérimentation ou de promotion ;
- Un système de certification (pour l’instant centralisé) afin de distinguer un token légitime d’un faux jeton copiant un ticker célèbre. Dans l’avenir, cette certification pourra devenir plus décentralisée (via DNS ou d'autres mécanismes).

Au final, Iris affiche donc une expérience utilisateur proche d’un wallet Bitcoin classique, en masquant la complexité supplémentaire (gestion du stash, historique de *consignments*, etc.) grâce à RGBlib et l'utilisation d'un serveur proxy.

### Serveur proxy et expérience utilisateur

Le serveur proxy introduit ci-dessus mérite d’être détaillé, car il constitue la clef d’une expérience fluide pour l'utilisateur. Au lieu que l’expéditeur doive manuellement transmettre les *consignments* au destinataire, la transaction RGB s’effectue en arrière-plan via un schéma de requêtes :
- Le destinataire génère une *invoice* (contenant, entre autres, l’adresse du proxy) ;
- L’expéditeur envoie (via une requête HTTP) un projet de transition (le *consignment*) au proxy ;
- Le destinataire récupère ce projet, exécute localement la validation *client-side* ;
- Le destinataire publie ensuite, via le proxy, l’acceptation (ou éventuellement le refus) de la transition d'état ;
- L’expéditeur peut consulter l’état de validation, et, si c’est accepté, diffuser la transaction Bitcoin finalisant le transfert.

Ainsi, le wallet se comporte presque comme un wallet normal. L’utilisateur n’a pas conscience de toutes les étapes intermédiaires. Certes, le proxy actuel n’est pas chiffré ni authentifié (ce qui laisse des inquiétudes quant à la confidentialité et l’intégrité), mais ces améliorations sont possibles dans des versions ultérieures. Le concept de proxy demeure extrêmement utile pour recréer l’expérience : "*j’envoie un QR code, tu scannes pour payer*".

### Intégration de RGB sur le Lightning Network

Un autre axe essentiel du travail mené par l’équipe de Bitfinex consiste à rendre le Lightning Network compatible avec des assets RGB. L’objectif est de permettre des canaux Lightning en USDT (ou tout autre jeton), et de bénéficier des mêmes avantages que pour le bitcoin sur Lightning (transactions quasi instantanées, routage, etc.). Concrètement, il s’agit de créer un nœud Lightning modifié pour :
- Ouvrir un canal en plaçant non seulement des satoshis, mais aussi un ou plusieurs assets RGB dans l’UTXO multisig de funding ;
- Générer les transactions d'engagement Lightning (côté Bitcoin) accompagnées de transitions d’état RGB correspondantes. À chaque mise à jour du canal, une transition RGB redéfinit la répartition de l’asset dans les sorties Lightning ;
- Permettre la fermeture unilatérale, où l’on récupère l’asset dans un UTXO exclusif, conformément aux règles du Lightning Network (HTLC, timelock, punition...).

Cette solution, baptisée "**RGB Lightning Node**", utilise notamment LDK (*Lightning Dev Kit*) comme base et ajoute les mécanismes nécessaires pour injecter des tokens RGB dans les canaux. Les engagements Lightning conservent la structure classique (sorties punissables, timelock...), et en plus on y ancre une transition d'état RGB (via `Opret` ou `Tapret`). Pour l’utilisateur, cela ouvre la voie à des canaux Lightning en stablecoins ou en tout autre actif émis via RGB.

### Potentiel DEX et impacts sur Bitcoin

Une fois plusieurs actifs gérés via Lightning, il devient possible d’imaginer un **échange atomique** sur un unique chemin de routage Lightning, en utilisant la même logique de secrets et timelocks. Par exemple, un utilisateur A détient du bitcoin sur un canal Lightning, et un utilisateur B détient de l’USDT RGB sur un autre canal Lightning. Ils peuvent construire un chemin reliant leurs deux canaux et échanger simultanément BTC contre USDT, sans besoin de confiance. Ce n’est rien d’autre qu’un **atomic swap** se déroulant en plusieurs sauts, rendant les participants extérieurs quasi inconscients du fait qu’ils réalisent un trade, pas juste un routage. Cette approche offre :
- Une latence très faible, car tout reste off-chain sur Lightning.
- Une **privacy** supérieure : personne ne sait que c’est un trade, et pas un routage normal ;
- L’évitement du "frontrunning", un problème récurrent des DEX on-chain ;
- Des frais réduits (on ne paie pas de blockspace, mais juste des frais de routage Lightning).

On peut alors imaginer un écosystème où des nœuds Lightning proposent des prix de swap (en fournissant de la liquidité). Chaque nœud, s’il le souhaite, peut jouer ce rôle de _market maker_, en achetant et en vendant divers actifs sur Lightning. Cette perspective d’un DEX _layer-2_ renforce l’idée qu’il n’est pas nécessaire de fork ou d’utiliser des blockchains tierces pour obtenir des échanges d’actifs décentralisés.

L’impact pour Bitcoin peut être positif : l’infrastructure de Lightning (nœuds, canaux et services) serait davantage utilisée grâce aux volumes générés par ces *stablecoins*, dérivés et autres tokens. Les commerçants intéressés par les paiements en USDT sur Lightning, découvriraient mécaniquement les paiements en BTC sur Lightning (gérés par la même stack). L’entretien et le financement de l’infrastructure du Lightning Network pourraient aussi profiter de la multiplication de ces flux non-BTC, ce qui, indirectement, profiterait aux utilisateurs de Bitcoin.

### Conclusion et ressources

L’équipe de Bitfinex dédiée à RGB illustre, via ses travaux, la diversité de ce qu’on peut faire au-dessus du protocole. D’un côté, on a RGBlib, une librairie qui facilite la conception de wallets et d’applications. D’un autre côté, on a Iris Wallet, une démonstration pratique sur Android d’une interface soignée pour l’utilisateur final. Enfin, l’intégration de RGB à Lightning montre que des canaux en stablecoin sont rendus possibles, et ouvre la voie à un potentiel DEX décentralisé sur Lightning.

Cette démarche reste largement expérimentale et continue d’évoluer : la librairie RGBlib se peaufine au fur et à mesure, Iris Wallet reçoit des améliorations régulières et le nœud Lightning dédié n’est pas encore un client Lightning mainstream.

Pour ceux qui souhaitent en savoir plus ou contribuer, plusieurs ressources sont disponibles, notamment :
- [Les dépôts GitHub RGB Tools](https://github.com/RGB-Tools) ;
- [Un site d’information dédié à Iris Wallet](https://iriswallet.com/) pour tester le wallet sur Android.

Dans le prochain chapitre, nous allons voir concrètement commet on peut lancer un nœud RGB Lightning.

## RLN - RGB Lightning Node
<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

![vidéo](https://youtu.be/piQQH4Q2nr0)

Dans ce dernier chapitre, Frederico Tenga vous guide étape par étape dans la mise en place d'un nœud Lightning RGB sur un environnement en Regtest, et vous montre comment y créer des tokens RGB. En lançant deux nœuds séparés, vous découvrirez également comment ouvrir un canal Lightning entre eux et y échanger des actifs RGB.

Cette vidéo sert de tutoriel, similaire à ce que nous avons abordé dans un chapitre précédent, mais spécifiquement axée sur Lightning cette fois-ci !

La principale ressource de cette vidéo est le dépôt Github [RGB Lightning Node](https://github.com/RGB-Tools/rgb-lightning-node), qui vous facilite le lancement de cette configuration en Regtest.

### Déploiement d’un nœud Lightning compatible RGB

Le processus reprend et met en pratique toutes les notions abordées dans les chapitres précédents :
- L’idée que l’**UTXO** bloqué sur un multisig 2/2 d’un canal Lightning peut recevoir non seulement des bitcoins, mais également être un Single-use Seal d'actif RGB (fongibles ou non) ;
- L’ajout, dans chaque transaction d'engagement Lightning d’une sortie (`Tapret` ou `Opret`) dédiée à l’ancrage de la transition d’état RGB ;
- L’infrastructure associée (bitcoind/indexer/proxy) pour valider les transactions Bitcoin et échanger les données *client-side*.

### Présentation de rgb-lightning-node

Le projet **`rgb-lightning-node`** est un daemon en Rust qui s’appuie sur un fork de `rust-lightning` (LDK) modifié pour prendre en compte l’existence d’assets RGB dans un canal. Lors de l’ouverture d’un canal, on peut ainsi préciser la présence d’assets, et lors de chaque mise à jour de l’état du canal, une transition RGB est créée, qui reflète la répartition de l’asset dans les outputs Lightning. Cela permet :
- D’ouvrir des canaux Lightning en USDT par exemple ;
- D’acheminer ces tokens à travers le réseau, à condition que les chemins de routage disposent de suffisamment de liquidités ;
- D’exploiter la logique de punition et de timelock Lightning sans modification : on ancre simplement la transition RGB dans une sortie supplémentaire de la transaction d'engagement.

Le code est encore à un stade alpha : il est conseillé de l’utiliser en **regtest** ou sur le **testnet** uniquement.

### Installation du nœud

Pour compiler et installer le binaire `rgb-lightning-node`, on commence par cloner le dépôt et ses sous-modules, puis on va lancer la compilation :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/fr/098.webp)

- L’option `--recurse-submodules` permet de cloner également les sous-dépôts nécessaires (dont la version modifiée de `rust-lightning`) ;
- L’option `--shallow-submodules` restreint la profondeur du clone pour accélérer le téléchargement, tout en ayant accès aux commits indispensables.

Depuis la racine du projet, exécutez la commande suivante pour compiler et installer le binaire :

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/fr/099.webp)

- `--locked` assure que la version des dépendances est strictement respectée ;
- `--debug` n’est pas obligatoire, mais peut faciliter la mise au point (vous pouvez utiliser `--release` si vous préférez) ;
- `--path .` indique à `cargo install` d’installer depuis le répertoire courant.

Au terme de cette commande, un exécutable `rgb-lightning-node` sera disponible dans votre `$CARGO_HOME/bin/`. Assurez-vous que ce chemin est dans votre `$PATH` pour pouvoir invoquer la commande depuis n’importe quel répertoire.

### Prérequis d’exécution

Pour fonctionner, le daemon `rgb-lightning-node` requiert la présence et la configuration de :

- **Un nœud `bitcoind`**  

Chaque instance RLN aura besoin de communiquer avec `bitcoind` pour diffuser et surveiller ses transactions on-chain. L’authentification (login/password) et l’URL (host/port) devront être fournis au daemon.

- **Un indexeur** (Electrum ou Esplora)  

Le daemon doit pouvoir lister et explorer les transactions on-chain, en particulier pour retrouver l’UTXO sur lequel un asset a été ancré. Vous devrez préciser l’URL de votre Electrum server ou Esplora.

- **Un proxy RGB**  

Comme vu dans les chapitres précédents, le **serveur proxy** est un composant (optionnel, mais fortement recommandé) permettant de simplifier l’échange de *consignments* entre pairs Lightning. Là encore, une URL doit être spécifiée.

Les identifiants et URL sont renseignés au moment où l’on _unlock_ le daemon via l’API. Cela sera détaillé plus loin.

### Lancement en Regtest

Pour un usage simple, il y a un script `regtest.sh` qui démarre automatiquement, via Docker, un ensemble de services : `bitcoind`, `electrs` (indexer), `rgb-proxy-server`. 

![RGB-Bitcoin](assets/fr/100.webp)

Cela permet de lancer un environnement local, isolé et déjà configuré. Il crée et détruit les conteneurs ainsi que les répertoires de données à chaque redémarrage. Nous allons commencer par démarrer l'environnement :

```bash
./regtest.sh start
```

Ce script va :
- Créer un répertoire `docker/` pour stocker les données ;
- Lancer `bitcoind` en regtest, ainsi que l’indexer `electrs` et le `rgb-proxy-server` ;
- Attendre que tout soit prêt à l’emploi.

![RGB-Bitcoin](assets/fr/101.webp)

Puis, nous allons lancer plusieurs nœuds RLN. Dans des shells distincts, exécutez par exemple (pour lancer 3 nœuds RLN) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
    --ldk-peer-listening-port 9735 --network regtest

# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
    --ldk-peer-listening-port 9736 --network regtest

# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
    --ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/fr/102.webp)

- Le paramètre `--network regtest` indique l’usage de la configuration regtest ;
- `--daemon-listening-port` indique sur quel port REST le nœud Lightning écoutera pour les appels API (JSON) ;
- `--ldk-peer-listening-port` spécifie sur quel port Lightning p2p écouter ;
- `dataldk0/`, `dataldk1/` sont les chemins vers les répertoires de stockage (chaque nœud stocke ses infos séparément).

Vous pouvez également exécuter des commandes sur vos nœuds RLN depuis votre navigateur :

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Pour qu’un nœud puisse ouvrir un canal, il doit d'abord posséder des bitcoins sur une adresse générée avec la commande suivante (pour le nœud n°1 par exemple) :

```bash
curl -X POST http://localhost:3001/address
```

La réponse vous fournira une adresse.

![RGB-Bitcoin](assets/fr/103.webp)

Sur le `bitcoind` Regtest, on va miner quelques bitcoins. Exécutez :

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/fr/104.webp)

Envoyez des fonds à l'adresse du nœud générée précédemment :

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/fr/105.webp)

Puis minez un bloc pour confirmer la transaction :

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/fr/106.webp)

### Lancement en Testnet (sans Docker)

Si vous souhaitez tester un scénario plus réaliste, vous pouvez lancer 3 nœuds RLN sur le Testnet plutôt qu'en Regtest, pointant vers des services publics :

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
    --ldk-peer-listening-port 9735 --network testnet

rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
    --ldk-peer-listening-port 9736 --network testnet

rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
    --ldk-peer-listening-port 9737 --network testnet
```

Par défaut, s’il ne trouve pas de configuration, le daemon tentera d’utiliser les services :
- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- `indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Avec les identifiants :
- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

Vous pouvez aussi personnaliser ces éléments via l’API `init`/`unlock`.

### Émission d'un token RGB

Pour émettre un token on va commencer par créer des UTXOs "colorables" :

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
        "up_to": false,
        "num": 4,
        "size": 2000000,
        "fee_rate": 4.2,
        "skip_sync": false
      }' \
  http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/fr/107.webp)

Vous pouvez évidemment adapter la commande. Pour confirmer la transaction, on mine un bloc :

```bash
./regtest.sh mine 1
```

On peut maintenant créer un asset RGB. La commande va dépendre du type d'asset que vous souhaitez créer et de ses paramètres. Ici je crée un token NIA (*Non Inflatable Asset*) nommé "PBN" avec une supply de 1000 unités. La `precision` permet de définir la divisibilité des unités.

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
        "amounts": [
          1000
        ],
        "ticker": "PBN",
        "name": "Plan B Network",
        "precision": 0
      }' \
  http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/fr/108.webp)

La réponse inclue l’identifiant de l’asset nouvellement créé. Pensez à noter cet identifiant. Dans mon cas, c'est :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/fr/109.webp)

Vous pourrez ensuite effectuer des transferts on-chain, ou bien l’allouer dans un canal Lightning. C'est justement ce que nous allons faire dans la prochaine section.

### Ouverture de canal et transfert d’un actif RGB

Vous devez d'abord connecter votre nœud à un pair du réseau Lightning en utilisant la commande `/connectpeer`. Dans mon exemple, je contrôle les deux nœuds. Je vais donc récupérer la clé publique de mon second nœud Lightning avec cette commande :

```bash
curl -X 'GET' \
  'http://localhost:3002/nodeinfo' \
  -H 'accept: application/json'
```

La commande me renvoie la clé publique de mon nœud n°2 :

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/fr/110.webp)

Ensuite, nous allons ouvrir le canal en spécifiant l'asset concerné (`PBN`). La commande `/openchannel` vous permet de définir la taille du canal en satoshis et d'opter pour l'inclusion de l'asset RGB. Cela dépend de ce que vous souhaitez créer, mais dans mon cas, la commande est :

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
        "peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
        "capacity_sat": 1000000,
        "push_msat": 10000000,
        "asset_amount": 500,
        "asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
        "public": true,
        "with_anchors": true,
        "fee_base_msat": 1000,
        "fee_proportional_millionths": 0,
        "temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
      }' \
  http://localhost:3001/openchannel

```

Dans le détail ici :
- `peer_pubkey_and_opt_addr` : Identifiant du pair auquel on souhaite se connecter (la clé publique que nous avons trouvée précédemment) ;
- `capacity_sat` : Capacité totale du canal en satoshis ;
- `push_msat` : Montant en millisatoshis initialement transféré au pair lors de l'ouverture du canal (ici je lui transfère immédiatement 10 000 sats pour qu'il puisse faire un transfert RGB par la suite) ;
- `asset_amount` : Quantité d'actifs RGB à engager dans le canal ;
- `asset_id` : Identifiant unique de l'actif RGB engagé dans le canal ;
- `public` : Indique si le canal doit être rendu public pour le routage sur le réseau.

![RGB-Bitcoin](assets/fr/111.webp)

Pour confirmer la transaction, on mine 6 blocs :

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/fr/112.webp)

Le canal Lightning est désormais ouvert et contient également 500 tokens `PBN` du côté du nœud n°1. Si le nœud n°2 souhaite recevoir des tokens `PBN`, il devra générer une invoice. Voici comment procéder :

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
        "amt_msat": 3000000,
        "expiry_sec": 420,
        "asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
        "asset_amount": 100
      }' \
  http://localhost:3002/lninvoice
```

Avec :
- `amt_msat` : Montant de l'invoice en millisatoshis (minimum 3000 sats) ;
- `expiry_sec` : Délai d'expiration de l'invoice en secondes ;
- `asset_id` : Identifiant de l'actif RGB associé à l'invoice ;
- `asset_amount` : Quantité de l'actif RGB à transférer avec cette invoice.

En réponse, vous obtiendrez une invoice RGB (comme décris dans les chapitres précédents) :

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/fr/113.webp)

Nous allons maintenant payer cette invoice depuis le premier nœud, qui détient les liquidités nécessaires avec le token `PBN` :

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
        "invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
      }' \
  http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/fr/114.webp)

Le paiement a bien été effectué. On peut le vérifier en exécutant sur un des deux nœuds la commande :

```bash
curl -X 'GET' \
  'http://localhost:3001/listpayments' \
  -H 'accept: application/json'
```

![RGB-Bitcoin](assets/fr/115.webp)

Voici donc comment déployer un nœud Lightning modifié pour transporter des assets RGB. Cette démonstration se base sur :
- Un environnement regtest (via `./regtest.sh`) ou testnet ;
- Un nœud Lightning (`rgb-lightning-node`) s’appuyant sur un `bitcoind`, un indexer et un `rgb-proxy-server` ;
- Une série d’APIs JSON REST pour ouvrir/fermer des canaux, émettre des tokens, transférer des assets via Lightning, etc.

Grâce à ce processus :
- Les transactions d'engagement Lightning embarquent une sortie supplémentaire (OP_RETURN ou Taproot) avec l’ancrage d’une transition RGB ;
- Les transferts s’effectuent exactement comme des paiements Lightning traditionnels, mais en transportant un token RGB en plus ;
- On peut relier plusieurs nœuds RLN pour router et expérimenter des paiements sur plusieurs nœuds, à condition d'avoir suffisamment de liquidités à la fois en bitcoins et en asset RGB sur le chemin.

Le projet demeure à un stade alpha. Il est donc fortement recommandé de se limiter à des environnements test (regtest, testnet).

Les opportunités ouvertes par cette compatibilité LN-RGB sont considérables : stablecoins sur Lightning, DEX layer-2, transferts de tokens fongibles ou de NFT à très faible coût… Les chapitres précédents ont exposé l’architecture conceptuelle et la logique de validation. Désormais, vous possédez une vue pratique de la mise en route d’un tel nœud, pour vos futurs développements ou tests.

# Conclusion 
<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>


## Avis & Notes
<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>
<isCourseReview>true</isCourseReview>

## Conclusion 
<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>
<isCourseConclusion>true</isCourseConclusion>
