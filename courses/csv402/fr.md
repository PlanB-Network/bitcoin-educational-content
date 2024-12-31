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

La dernière section est animée par d'autres intervenants qui présentent des applications concrètes basées sur RGB, afin de mettre en lumière des cas d’utilisation réels.

---

Cette formation est initialement issue d'un bootcamp de développement avancé de deux semaines à Viareggio, en Toscane, organisé par [Fulgur'Ventures](https://fulgur.ventures/). La première semaine, centrée sur Rust et les SDK, peut être retrouvée dans cet autre cours :

https://planb.network/courses/lnp402

Dans ce cours, nous nous concentrons sur la deuxième semaine du bootcamp, qui porte sur RGB.

**Semaine 1 - LNP402 :**

001

**Semaine 2 - Formation actuelle :**

002

Un grand merci à la personne qui a organisé ces cours en direct et aux 3 enseignants qui y ont participé :
- Maxim Orlovsky : *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, IA, robotique, transhumanisme. Créateur de RGB, Prime, Radiant et lnp_bp, mycitadel_io & cyphernet_io* ;
- Hunter Trujilo : *Développeur, Rust, Bitcoin, Bitcoin, Lightning, RGB* ;
- Federico Tenga : *Je fais ma part pour que le monde devienne une dystopie cypherpunk. Actuellement en train de travailler sur RGB chez Bitfinex*.



# RGB en théorie
<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Comprendre RGB
<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

![video](https://youtu.be/AF2XbifPGXM)


### Déroulé de la première section

Les deux premiers chapitres sont consacrés à la **validation côté client**, un paradigme fondamentalement différent de celui de la blockchain. Nous aborderons les points suivants :
- Les bases de la validation côté client dans le contexte du calcul distribué ;
- Les raisons de son importance et de sa nécessité ;
- Comment ce paradigme s’intègre avec la blockchain.

Les deux chapitres suivant se focaliseront sur les bases théoriques de RGB en tant que système de contrats intelligents. Nous aborderons notamment :
- **Le sharding** : un mécanisme clé pour atteindre l’évolutivité dans RGB.
- **Les scellés à usage unique (Single-Use Seals)** : une primitive cryptographique développée par Peter Todd, essentielle pour la validation côté client et distincte des autres formes d'engagements cryptographiques.

Nous allons débuter avec une introduction au calcul distribué et son rôle dans la validation côté client. Cette exploration restera centrée sur les aspects en lien avec Bitcoin.

### Introduction

Dans l’univers de la blockchain et de l’informatique distribuée, nous pouvons distinguer deux paradigmes fondamentaux : la _blockchain_ au sens traditionnel, et les _state channels_ (canaux d’état), dont le meilleur exemple en production est le _Lightning Network_. La _blockchain_ se définit comme un registre d’événements ordonnés chronologiquement, répliqué par consensus au sein d’un réseau ouvert et sans permission. Les _state channels_, eux, sont des canaux peer-to-peer qui permettent à deux (ou plusieurs) participants de maintenir un état mis à jour hors de la chaîne, ne recourant à la blockchain qu’au moment de l’ouverture et de la fermeture de ces canaux.

Dans le cadre de Bitcoin, vous connaissez sans doute les principes du minage, la décentralisation et la finalité des transactions sur la blockchain, ainsi que le fonctionnement des canaux de paiement. Nous allons introduire un nouveau paradigme appelé **client-side validation** (validation côté client), qui, contrairement à la blockchain ou à Lightning, consiste à conserver et à valider localement (côté client) l’état et les transitions d’état d’un contrat intelligent. Ceci se différencie aussi d’autres techniques de la "DeFi" (_rollups_, _plasma_, _ARK_, etc.), dans la mesure où la _client-side validation_ s’appuie sur la blockchain pour empêcher la double dépense et pour avoir un système d'horodatage, tout en conservant le registre des états et des transitions hors chaîne, uniquement chez les participants concernés.

Nous allons également plus tard introduire un terme important : la notion de "**stash**", qui désigne l’ensemble des données côté client nécessaires pour préserver l’état d’un contrat, ces données n’étant pas répliquées de façon globale sur le réseau. Enfin, nous aborderons la raison d’être de **RGB**, un protocole tirant parti de la _client-side validation_, et pourquoi il se révèle complémentaire aux approches existantes (blockchain et _state channels_).

003

### Les trilemmes en informatique distribuée

Pour comprendre en quoi _client-side validation_ et RGB répondent à des problématiques non résolues par la blockchain et Lightning, découvrons 3 "trilemmes" majeurs en informatique distribuée :

1. **Scalabilité, Décentralisation, Privacy**
2. **Théorème CAP** (Cohérence, Disponibilité, tolérance aux Partitions)
3. **Trilemme CIA** (Confidentialité, Intégrité, Disponibilité)

#### 1. Scalabilité, décentralisation et confidentialité

- **Blockchain (Bitcoin)**

La blockchain est très décentralisée, mais peu scalable. De plus, comme tout se trouve dans un registre global et public, la confidentialité est limitée. On peut tenter d’améliorer la confidentialité avec des technologies zero-knowledge (transactions confidentielles, schémas mimblewimble, etc.), mais la chaîne publique ne peut pas cacher le graphe des transactions.

- **Lightning/State channels**

Les canaux d’état (comme avec le Lightning Network) sont plus scalables et plus privés que la blockchain, car les transactions s’effectuent hors chaîne. Toutefois, l’obligation d’annoncer publiquement certains éléments (transactions de financement, topologie du réseau) et la surveillance du trafic réseau peuvent compromettre en partie la confidentialité. Aussi, la décentralisation en pâtit : le routage requiert une grande quantité de liquidité et les nœuds majeurs peuvent devenir des points de centralisation. C'est justement un phénomène que l'on peut commencer à observer actuellement sur Lightning.

- **Client-side validation (RGB)**

Ce nouveau paradigme est encore plus scalable et plus confidentiel, car non seulement on peut intégrer des techniques zero-knowledge, mais il n’y a pas de graphe global des transactions : personne ne détient la totalité du registre. En revanche, cela implique aussi un certain compromis sur la décentralisation : un _contract issuer_ (l’émetteur d’un contrat intelligent) peut avoir un rôle central (à l’instar d’un _contract deployer_ dans Ethereum). Néanmoins, contrairement à la blockchain, avec la _client-side validation_, vous ne stockez et ne validez que les contrats qui vous intéressent, ce qui améliore la scalabilité en évitant de télécharger et de vérifier tous les états existants.

004

#### 2. Théorème CAP (Consistency, Availability, Partition tolerance)

Le **théorème CAP** souligne qu’il est impossible pour un système distribué de satisfaire simultanément la cohérence (Consistency), la disponibilité (Availability) et la tolérance au partitionnement (Partition tolerance).

- **Blockchain**

La blockchain privilégie la cohérence et la disponibilité, mais s’accommode mal de la partition du réseau : si vous ne voyez pas un bloc, vous n’êtes pas en mesure d’agir et d’avoir la même vue que l’ensemble du réseau.

- **Lightning**

Un système de canaux d'états dispose de la disponibilité et de la tolérance au partitionnement (puisque deux nœuds peuvent rester connectés entre eux même si le réseau est fragmenté), mais la cohérence globale dépend de l’ouverture et de la fermeture des canaux sur la blockchain.

- **Client-side validation (RGB)**

Un système comme RGB offre la cohérence (chaque participant valide ses données localement, sans ambiguïté) et la tolérance au partitionnement (vous conservez vos données de manière autonome), mais ne garantit pas la disponibilité globale (chacun doit s’assurer d’avoir les morceaux d’historique pertinents, et certains participants peuvent ne rien publier ou cesser de partager certaines informations).

005

#### 3. Trilemme CIA (Confidentiality, Integrity, Availability)

Ce trilemme rappelle que la confidentialité, l’intégrité et la disponibilité ne peuvent être optimisées toutes les trois en même temps. Blockchain, Lightning et _client-side validation_ se répartissent différemment dans cet équilibre. L’idée est qu’aucun système unique ne peut tout fournir ; il faut combiner plusieurs approches (la time-stamping de la blockchain, l’approche synchrone de Lightning, et la validation locale avec RGB) pour obtenir un ensemble cohérent offrant de bonnes garanties dans chaque dimension.

006

### Le rôle de la blockchain et la notion de sharding

La blockchain (ici Bitcoin) sert surtout de mécanisme de _time-stamping_ et de protection contre la double dépense. Au lieu d’y insérer l’intégralité des données d’un smart contract ou d’un système décentralisé, on se contente d’y inclure des **engagements cryptographiques** (_commitments_) à des transactions (au sens de la _client-side validation_, que nous appellerons “transitions d’état”). Ainsi :
- On libère la blockchain d’une grande quantité de données et de logique.
- Chaque utilisateur ne stocke que l’historique nécessaire à sa propre portion du contrat (son “shard”), au lieu de répliquer l’état global.

Le _sharding_ est un concept né dans les bases de données distribuées (par exemple MySQL pour des réseaux sociaux comme Facebook ou Twitter). Pour résoudre le problème de volume de données et de latences de synchronisation, on segmente la base en _shards_ (États-Unis, Europe, Asie, etc.). Chaque segment est cohérent localement et ne se synchronise que partiellement avec les autres.

Pour les smart contracts de type RGB, on “sharde” selon les contrats eux-mêmes. Chaque contrat constitue un _shard_ indépendant. Par exemple, si vous ne détenez que des jetons USDT, vous n’avez pas à stocker ou valider tout l’historique d’un autre token comme l’USDC. Sur Bitcoin, la blockchain ne fait pas de _sharding_ : vous avez un ensemble d'UTXOs global. Avec la _client-side validation_, chaque participant conserve seulement les données des contrats qu’il détient ou utilise.

### Les couches : Blockchain, Lightning et RGB

On peut ainsi visualiser l’écosystème ainsi :
- **La blockchain (Bitcoin)** comme fondation qui assure la réplication complète d’un registre minimal et servant de couche d'horodatage.
- **Le lightning Network** pour des transactions rapides et confidentielles, qui repose toujours sur la sécurité et le règlement final de la blockchain Bitcoin.
- **RGB et la client-side validation** pour ajouter une logique plus complexe de smart contracts, sans encombrer la blockchain, ni perdre la confidentialité.

007

Ces trois éléments forment un ensemble triangulaire plus qu’un empilement linéaire de “layer 2”, “layer 3”, etc. Lightning peut se brancher directement sur Bitcoin, ou bien être associé à des transactions Bitcoin qui intègrent des données RGB. De même, un usage de la “BiFi” (finance sur Bitcoin) peut composer avec la blockchain, Lightning et RGB selon les besoins en confidentialité, scalabilité, ou logique de contrat.

008

### La notion de transitions d'état

Dans un système distribué, on modélise souvent l’évolution d’un contrat sous forme de “state machine” : un état initial, puis diverses transitions qui mènent à de nouveaux états.

009

Sur Bitcoin, l’état global est l’ensemble des UTXOs, et chaque bloc apporte un lot de transactions qui modifient une partie de cet ensemble. 

010

Tout le réseau doit valider et télécharger l’ensemble de ces mises à jour, ce qui nuit à la scalabilité et à la confidentialité (puisque les transactions sont publiques).

012

Avec la **client-side validation**, seules les personnes impliquées dans la transition d’état conservent et valident cette transition. On n’insère sur la blockchain qu’un engagement (via un arbre de Merkle, etc.) afin de profiter du time-stamping et de la protection face à la double dépense, mais on ne révèle jamais le contenu complet de la transition.

013

Concrètement :
- Vous préparez une nouvelle transition d’état (par exemple le transfert d’un jeton RGB).
- Vous générez un engagement cryptographique à cette transition et l’insérez dans une transaction Bitcoin (on appelle ces engagements des “anchors” dans le protocole RGB).
- La contrepartie (le destinataire) récupère l’historique _client-side_ associé à cet actif et valide la cohérence de bout en bout, depuis la genèse du smart contract jusqu’à la transition que vous lui transmettez.

014

Seuls les participants directement concernés par un contrat conservent les données historiques ; le réseau Bitcoin n’est pas alourdi par ces informations. Vous gagnez ainsi :
- **en scalabilité** : Pas de duplication globale de tout l’historique.
- **en confidentialité** : Personne ne voit l’intégralité du graphe des transferts de jetons.

L’élément central est donc la **décentralisation partielle** : chaque contrat constitue un shard indépendant, et chaque participant n’en stocke que la part d’historique qui le concerne.

015

### Le concept de stash

Un **stash** est l’ensemble de données côté client qu’un participant doit absolument conserver pour maintenir l’intégrité et l’historique d’un smart contract RGB. Contrairement à un canal Lightning, où l’on peut reconstruire certains états localement à partir d’informations partagées, le stash d’un contrat RGB n’est pas répliqué ailleurs : si vous le perdez, personne ne pourra vous le restaurer, car vous êtes responsable de votre part de l’historique. D’où l’intérêt de procédures de sauvegarde fiables dans RGB.

016

### Single use seal : origines et fonctionnement

Pour permettre cette validation locale, on s’appuie sur une invention de Peter Todd appelée **single use seal**. 

017

L’idée de base est de créer un engagement cryptographique que l’on ne puisse “fermer” qu’une seule fois, empêchant ainsi la duplication (double engagement).

018

Pour cela, on va combiner différentes techniques d'engagement qui à elles seules ne sont pas complètes :

- **Engagement cryptographique (hash)** : Avec une fonction de hachage, on peut s’engager sur une donnée (un nombre) en publiant son empreinte (hash). La donnée reste secrète tant qu’on ne révèle pas le préimage, mais on peut prouver qu’on la connaissait à l’avance.
- **Horodatage (blockchain)** : En insérant ce hash dans la blockchain, on prouve aussi qu’on le connaissait à un instant précis (celui de l’inclusion dans un bloc).
- **Single use seal** : Avec les sceaux à usage unique, on va plus loin en rendant l’engagement unique. Avec un simple hash, on peut créer plusieurs engagements contradictoires en parallèle (le problème du docteur qui annonce “C’est un garçon” à la famille et “C’est une fille” dans son journal personnel). Le single use seal élimine cette possibilité en connectant l’engagement à un support de preuve de publication, comme la blockchain Bitcoin, de sorte qu’une dépense d’UTXO scelle définitivement l’engagement. Une fois dépensé, on ne peut plus redépenser le même UTXO pour remplacer l’engagement.

|                                                                                  | Engagement simple (digest/hash) | Timestamps | Single-use-seals |
| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |
| La publication de l'engagement ne révèle pas le message                          | Oui                             | Oui        | Oui              |
| Preuve de la date de l'engagement / existence du message avant une certaine date | Impossible                      | Possible   | Possible         |
| Preuve qu’aucun autre engagement alternatif ne peut exister                      | Impossible                      | Impossible | Possible         |


019

Pour comprendre cela, faisons une analogie. Imaginez un journal (comme le _New York Times_) qui paraît chaque jour. Il est impossible de “republier” le même numéro sous deux versions différentes sans être détecté. On pourrait alors définir le coin supérieur droit de la dernière page comme un single use seal. Chaque jour (= chaque block Bitcoin), vous pouvez insérer un message dans cette zone. Ce message sert à prouver que vous avez publié quelque chose ce jour-là, en temps voulu et de manière irréfutable. Une fois ce journal imprimé et distribué, il devient impossible de revenir en arrière pour insérer un second message ou modifier le premier tout en prétendant que la version altérée est l’originale.

021

Sur la blockchain Bitcoin, le **single use seal** se définit de la même manière :

- Le _seal definition_ est l’UTXO que vous destinez à sceller un engagement futur.
- Le _seal closing_ survient quand vous dépensez cet UTXO, en créant une transaction qui contient l’engagement.
- Le _witness_ est la transaction elle-même, qui prouve que vous avez bien “fermé” le seal avec ce contenu.
- Vous ne pouvez pas prouver qu’un seal n’a pas été fermé (on ne peut pas être absolument sûr qu’un UTXO n’est pas déjà dépensé ou ne le sera pas dans un bloc qu’on n’a pas encore vu), mais on peut prouver qu’il a bel et bien été fermé de telle ou telle façon.

Cette unicité est importante pour la **client-side validation** : quand vous validez une transition d’état, vous vérifiez qu’elle correspond à un UTXO unique, non dépensé préalablement dans un engagement concurrent. C’est ce qui garantit l’absence de double spend dépense au niveau des smart contracts hors chaîne.

### Engagements multiples et ancrages

Un smart contract RGB peut avoir besoin de dépenser simultanément plusieurs single use seals (plusieurs UTXO). De plus, une seule transaction Bitcoin peut référencer plusieurs contrats distincts, chacun venant sceller sa propre transition d’état. Cela nécessite un mécanisme de **multi-commitments** permettant de prouver, de manière déterministe et unique, qu’aucun des engagements n’existe en double. C’est ici qu’intervient la notion d’**anchor** dans RGB : une structure spéciale reliant une transaction Bitcoin et un ou plusieurs engagements _client-side_ (transitions d’état), chacun relevant potentiellement d’un contrat différent.

023

Deux principaux dépôts GitHub du projet (sous l’organisation “LNPBP”) regroupent les implémentations de base :
- **client_side_validation** : Contient les primitives Rust pour la validation locale.
- **single_use_seals** : Implémente la logique pour définir et fermer ces seals de manière sécurisée.

020

Ces briques sont agnostiques par rapport à Bitcoin ; on pourrait, en théorie, les appliquer à tout autre support de preuve de publication (un autre registre, un journal, etc.). Dans la pratique, RGB repose sur Bitcoin pour sa robustesse et son large consensus.

021

### Questions du public

#### Vers un usage plus large des single use seals

Peter Todd a également créé le protocole _Open Timestamps_, et le concept de single use seal est un prolongement naturel de ces idées. Au-delà de RGB, on peut envisager d’autres cas d’utilisation, par exemple la construction de _sidechains_ sans recourir au _merge mining_ ni aux propositions liées aux drivechains comme le BIP300. Tout système nécessitant un engagement unique peut, en principe, exploiter cette primitive cryptographique. Aujourd’hui, RGB est la première grande mise en application concrète et complète.

#### Problèmes de disponibilité des données

Étant donné qu’en _client-side validation_, chaque utilisateur stocke sa partie de l’historique, la disponibilité des données n’est pas garantie globalement. Si un émetteur de contrat ne publie pas certaines informations ou les révoque, vous pourriez ignorer l’évolution réelle de l’offre. Dans certains cas (comme les stablecoins), on s’attend à ce que l’émetteur tienne à jour des données publiques pour prouver le volume en circulation, mais rien ne l’y contraint techniquement. Il est donc possible de concevoir des contrats volontairement opaques avec un stock illimité, ce qui pose des questions de confiance.

#### Sharding et isolement des contrats

Chaque contrat représente un _shard_ isolé : USDT et USDC, par exemple, n’ont pas à partager leur historique. Les swaps atomiques restent possibles, mais cela n’implique pas de fusionner leurs registres. Tout se fait par engagement cryptographique, sans divulguer l’ensemble du graphe d’historique à chaque participant.

### Conclusion

Nous avons vu où se situe le concept de _client-side validation_ par rapport à la blockchain et aux _state channels_, en quoi il répond à des trilemmes persistants de l’informatique distribuée, et comment il exploite la blockchain Bitcoin uniquement pour éviter la double dépense et pour l'horodatage (time-stamping). L’idée repose sur la notion de **single use seal**, permettant la création d’engagements uniques que vous ne pouvez pas redépenser à volonté. Ainsi, chaque participant ne télécharge que l’historique strictement nécessaire, ce qui accroît la scalabilité et la confidentialité des smart contracts tout en conservant la sécurité de Bitcoin en toile de fond.

La prochaine étape consistera à expliquer plus en détail **comment** on applique concrètement ce mécanisme de single use seal dans Bitcoin (via les UTXOs), comment on crée et on valide les **anchors**, puis comment on bâtit des _smart contracts_ complets dans RGB. Nous verrons notamment la question des engagements multiples, le défi technique de prouver qu’une transaction Bitcoin scelle simultanément plusieurs transitions d’état dans différents contrats, sans introduire de vulnérabilités ou de doubles engagements.

Avant de plonger dans les détails plus techniques du deuxième chapitre, n’hésitez pas à relire les définitions clés (client-side validation, single use seal, anchors, etc.) et à garder à l’esprit la logique globale : nous cherchons à concilier les atouts de la blockchain Bitcoin (sécurité, décentralisation, _time-stamping_) avec ceux des solutions hors chaîne (rapidité, confidentialité, scalabilité), et c’est précisément ce que RGB et la _client-side validation_ tentent de réaliser.





























## Validation côté client
<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

![video](https://youtu.be/FS6PDprWl5Q)

## Explication de l'état RGB
<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

![video](https://youtu.be/tmAVdyXGmj4)

## Logique métier RGB
<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

![video](https://youtu.be/lUTjeuM0oTA)

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
