---
name: Mettre en place son premier nœud Lightning
goal: Comprendre, installer, configurer et utiliser un nœud Lightning
objectives:
  - Comprendre le rôle et l’utilité d’un nœud Lightning.
  - Identifier les différentes solutions logicielles disponibles.
  - Installer et configurer un nœud Lightning (LND).
  - Connecter un portefeuille de dépense.
  - Connaitre les risques liés à l'utilisation d'un nœud Lightning.
---

# Votre premier pas vers l’autonomie sur Lightning

Vous progressez dans votre parcours de bitcoiner : vous avez déjà acquis vos premiers sats, les avez sécurisés en self-custody, peut-être sur un hardware wallet, puis vous avez déployé votre premier nœud Bitcoin afin de devenir souverain dans votre utilisation onchain. L’étape suivante consiste à devenir également autonome dans votre utilisation de Lightning, et c’est précisément l’objectif de ce cours.

On vous a peut-être dit que Lightning était complexe, que les nœuds étaient réservés aux grandes entreprises, ou encore qu’il était acceptable d’utiliser un portefeuille custodial sur Lightning. Tout cela est faux, et c’est ce que je souhaite vous démontrer dans ce cours.

LNP 202 est une formation accessible aux utilisateurs intermédiaires, qui vous accompagnera dans le déploiement de votre premier nœud Lightning, sans exiger de compétences techniques avancées. Vous découvrirez ce qu’est un nœud Lightning, en quoi son utilisation renforce votre souveraineté, et comment l’installer simplement avec LND sur Umbrel. Vous apprendrez ensuite à ouvrir vos premiers canaux, gérer vos liquidités, utiliser des outils de supervision et connecter un portefeuille mobile, afin de bénéficier, au final, d’une expérience utilisateur comparable à celle d’un portefeuille Lightning custodial, mais en conservant une souveraineté totale.

+++




# Introduction



## Aperçu du cours


## Comprendre ce qu'est un nœud Lightning

Avant de lancer votre propre nœud LN, je vous propose de revoir brièvement dans ce chapitre le fonctionnement théorique de base du Lightning Network. Il est en effet important de comprendre les mécanismes en jeu, car cela vous permettra d’identifier les risques et d’adopter les bonnes pratiques pour les limiter. Je n’entrerai toutefois pas dans les détails ici, car ce n’est pas l’objectif principal de ce cours. Si vous souhaitez approfondir le sujet, je vous recommande vivement de consulter le cours LNP 201 de Fanis Michalakis, qui fait référence en la matière :

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### C'est quoi un nœud Lightning ?

Revenons aux fondamentaux : avant de définir ce qu’est un nœud, il faut comprendre ce qu’est le Lightning Network. Il s’agit d’un protocole de couche supérieure, construit au-dessus de Bitcoin, destiné à permettre des transactions en BTC offchain, rapides (à finalité quasi instantanée) et généralement peu coûteuses. "Offchain" signifie que les transactions effectuées sur Lightning ne sont pas destinées à apparaître sur la blockchain principale de Bitcoin. Lightning constitue également une réponse, certes partielle, à l’augmentation de l’usage de Bitcoin et aux phénomènes de congestion onchain, qui suscitent des inquiétudes quant à la scalabilité du système.

Pour fonctionner, Lightning repose sur l’ouverture de canaux de paiement entre les participants, au sein desquels les transactions peuvent être réalisées presque instantanément, avec des frais souvent minimes, sans qu’il soit nécessaire de les inscrire une par une sur la blockchain Bitcoin. Ces canaux peuvent rester ouverts très longtemps et ne requièrent des transactions onchain qu’au moment de leur ouverture et de leur fermeture.

Un nœud Lightning est justement un participant à ce réseau Lightning : il ouvre des canaux et réalise des paiements avec d’autres nœuds. Concrètement, un nœud Lightning est un logiciel exécuté sur un ordinateur et qui implémente le protocole Lightning Network. Il peut s’agir, par exemple, de LND, Core Lightning ou Eclair. Le rôle de ce logiciel va princiaplement être :
* de se connecter à un nœud Bitcoin pour obtenir les informations de la blockchain principale ;
* de créer et gèrer des canaux de paiement bidirectionnels avec d’autres nœuds ;
* d'échanger des messages avec l’ensemble du réseau Lightning.

001

### Nœud vs Wallet Lightning : une distinction importante

Sur Bitcoin (onchain), on parle de “wallet” pour désigner un logiciel qui gère vos clés privées, calcule votre solde à partir de vos UTXOs et construit vos transactions. Ce portefeuille peut s’appuyer sur votre propre nœud Bitcoin ou sur un nœud d'une autre personne, mais aujourd’hui, le rôle du nœud et celui du portefeuille onchain sont clairement distincts.

Sur Lightning, il est plus difficile de réutiliser ce vocabulaire sans créer de confusion. Parler d’un “wallet Lightning” est assez vague, car en réalité il n’existe pas de portefeuille Lightning véritablement self-custodial sans qu’il repose sur un nœud. Seulement deux situations sont donc possibles :

- Avoir un véritable nœud Lightning (donc non-custodial) : le logiciel que vous utilisez (par exemple une app mobile comme Phoenix ou une instance LND sur Umbrel) exécute réellement un nœud, et vous détenez effectivement les clés permettant de récupérer vos bitcoins. Dans ce cas, votre “wallet Lightning” n’est en réalité qu’une interface utilisateur au-dessus d’un nœud Lightning, qu’il soit embarqué ou distant.

- Utiliser un service custodial : vous utilisez une application qui vous affiche un solde en sats sur Lightning, mais en arrière-plan, les fonds se trouvent sur le nœud d’un prestataire (par exemple : Wallet of Satoshi). Vous ne possédez ni les clés, ni le contrôle des canaux. Votre solde n’est qu’une écriture comptable dans la base de données de l'entreprise ; en somme, c’est comparable au fait de laisser ses bitcoins sur une plateforme d’échange, avec tous les risques associés. Dans ce cas, votre “wallet Lightning” n’est qu’un accès à un compte géré par un opérateur qui, lui, exploite un vrai nœud Lightning.

Il n’existe donc aucun entre-deux sur Lightning : soit vous avez un nœud (même embarqué) et vous êtes en self-custody, soit vous n’en avez pas, et une entreprise détient vos sats. Mais comme nous le verrons dans les chapitres suivants, ces deux usages peuvent parfois être difficiles à distinguer. Par exemple, Phoenix est une application mobile qui embarque un véritable nœud Lightning, mais l’utilisateur n’en a pas forcément conscience, car toute la complexité de son fonctionnement est presque entièrement cachée.

### Rappels sur le fonctionnement du Lightning Network

Dans cette section, je vous propose un rappel rapide du fonctionnement de Lightning. Une nouvelle fois, si vous souhaitez une présentation plus approfondie des concepts théoriques, je vous invite à consulter le cours dédié LNP 201.

#### Canaux de paiement : ouvrir, mettre à jour et fermer

Le cœur du réseau Lightning repose sur les canaux de paiement bidirectionnels. Un canal peut être ouvert (c’est-à-dire créé), mis à jour au fil des transactions Lightning, puis finalement fermé. Du point de vue onchain, un canal n’est rien d’autre qu’une sortie multisignature 2/2.

002

Du point de vue Lightning, il s’agit d’un canal de paiement disposant de liquidités réparties entre les deux participants.

003

- **Ouverture d’un canal :**

Deux nœuds décident d’ouvrir un canal. L’un d’eux engage des bitcoins dans une transaction onchain appelée "transaction de funding". Cette transaction crée une sortie reposant sur un script multisignature 2-of-2, ce qui signifie que dépenser ces fonds sur Bitcoin nécessite la signature des deux nœuds du canal. Avant de diffuser cette transaction, la partie qui apporte les fonds demande à l’autre de signer une "transaction de retrait", non publiée onchain, mais qui lui permet de récupérer ses fonds en cas de problème.

004

- **Transactions d’engagement :**

L’état du canal (c’est-à-dire la répartition des sats entre A et B) est représenté par une "transaction d’engagement", connue des deux nœuds mais non diffusée immédiatement sur la blockchain. Cette transaction décrit comment redistribuer onchain les fonds du canal en fonction des paiements réalisés sur Lightning.

À chaque paiement Lightning, les deux nœuds signent un nouvel état qui remplace le précédent. L’ancien est révoqué grâce à un mécanisme de clés de révocation : si l’un des participants tente de diffuser un ancien état, l’autre peut récupérer l’intégralité des fonds en guise de pénalité.

L’idée importante ici est qu’il existe en permanence une transaction Bitcoin signée, non diffusée onchain, conservée par les nœuds, et qui permet de redistribuer les sats de chacun selon les paiements opérées sur le Lightning Network.

005

- **Fermeture de canal :**

Un canal peut être fermé proprement via une fermeture coopérative, lorsque les deux parties s’accordent sur l’état final du canal, ou de manière unilatérale (une fermeture forcée) si l’un des participants cesse de coopérer ou devient injoignable. Dans tous les cas, la fermeture prend la forme d’une transaction onchain qui dépense la sortie 2/2 et répartit les fonds entre les participants selon le dernier état valide du canal.

006

Lightning fonctionne ainsi comme une couche secondaire ancrée sur Bitcoin : seuls certains événements (l’ouverture et la fermeture des canaux) apparaissent sur la blockchain principale. Les paiements intermédiaires restent offchain.

Avant de continuer, voici deux notions essentielles pour comprendre la gestion d’un canal Lightning :
- La "liquidité" : c'est quantité de sats disponibles d’un côté du canal ;
- La "capacité" : c'est le montant total verrouillé dans l’output multisig 2/2, c’est-à-dire la somme des liquidités des deux côtés du canal.

#### Un réseau de canaux et de liquidité

Un canal ne sert pas uniquement aux paiements entre deux nœuds : il s’inscrit dans un réseau global de canaux interconnectés. Votre nœud peut ainsi router des paiements pour d’autres utilisateurs à travers ses propres canaux, et vous pouvez envoyer des sats à un nœud Lightning avec lequel vous n’avez aucun canal direct, tant qu’un chemin valide peut être trouvé entre vos deux nœuds.

Chaque nœud connaît, via le protocole de gossip, une carte de ce réseau : quels canaux existent, quels nœuds sont connectés par un canal bidirectionnel, et quelles capacités sont publiées. Pour envoyer un paiement à un destinataire sans canal direct, votre nœud calcule un itinéraire composé de plusieurs sauts : votre nœud → nœud X → nœud Y → nœud destinataire. À chaque saut, le paiement transite dans un canal qui doit disposer de suffisamment de liquidité dans le sens du paiement.

007

La liquidité d’un canal n’est donc pas symétrique : un côté peut être très chargé tandis que l’autre est presque vide. La gestion de cette liquidité, c'est-à-dire savoir où se trouvent les sats et dans quel sens ils peuvent circuler, constitue l’un des aspects les plus importants de l’exploitation d’un nœud Lightning. Nous aborderons cela en détail dans les chapitres pratiques à venir.

#### HTLC : acheminer un paiement sans se faire voler

Pour permettre aux paiements de transiter par des nœuds intermédiaires sans nécessiter de confiance, Lightning utilise des contrats intelligents appelés "HTLC" (*Hashed Time-Locked Contracts*). Pour faire simple, un HTLC conditionne le transfert de fonds à la révélation d’un secret et intègre une contrainte temporelle permettant de protéger l’expéditeur en cas d’échec de la transaction. Chaque paiement est donc soumis à la présentation d’une préimage (un secret dont le hachage correspond à une valeur convenue). Si le destinataire final fournit cette préimage, il peut réclamer les fonds, ce qui permet en cascade à chaque nœud intermédiaire de récupérer les siens.

008

Je vous épargne les détails techniques du fonctionnement des HTLCs, car ils ne sont pas indispensables dans le cadre de ce cours. Vous en trouverez une explication approfondie dans la formation théorique LNP 201. Retenez simplement que les HTLCs permettent d’effectuer des échanges atomiques : soit le transfert aboutit entièrement et personne n’est lésé dans le routage, soit il échoue et chaque participant récupère ses fonds initiaux. Il n’existe pas d’entre-deux possible.

### Les principales implémentations de nœuds Lightning

Tout comme pour Bitcoin, il existe plusieurs implémentations du protocole Lightning. Plusieurs équipes indépendantes développent leurs propres versions, toutes interopérables puisqu’elles respectent les mêmes spécifications (les BOLT). Voici les principales implémentations utilisées aujourd’hui.

#### LND (*Lightning Network Daemon*)

LND est une implémentation complète du protocole Lightning, écrite en Go et développée par Lightning Labs.

009

#### Core Lightning (*CLN*)

Core Lightning (anciennement "C-Lightning") est l’implémentation développée par Blockstream. Elle est écrite en C, avec certains composants en Rust.

010

#### Eclair

Eclair est une implémentation écrite en Scala et développée par l’entreprise française ACINQ. ACINQ exploite l’un des plus importants nœuds de routage du réseau Lightning avec Eclair, et utilise cette implémentation comme base logicielle pour ses propres produits, comme l’application Phoenix.

011

#### LDK (*Lightning Development Kit*)

LDK (*Lightning Development Kit*) est un kit de développement en Rust, maintenu par Spiral (Block, ex-Square). Ce n’est pas un daemon prêt à l’emploi comme LND ou CLN, mais une bibliothèque destinée aux développeurs souhaitant intégrer Lightning directement dans leurs applications.

012

Dans ce cours LNP 202, nous nous concentrerons principalement sur LND, car il s’agit de l’implémentation la plus utilisée dans les solutions clé en main destinées aux particuliers, comme Umbrel.

Voilà pour ce bref rappel sur le fonctionnement de Lightning. Une nouvelle fois, si certains concepts vous échappent ou si vous souhaitez les approfondir avant de passer à la pratique, le cours de Fanis Michalakis est la référence incontournable sur le sujet :

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Pourquoi exploiter son propre nœud Lightning ?

Répondre à cette question est assez simple, puisqu’elle est rhétorique : sans son propre nœud, on n’utilise plus réellement Lightning, mais seulement l’illusion de Lightning au travers de l’infrastructure d’une entreprise.

Utiliser un portefeuille Lightning custodial signifie que les bitcoins appartiennent techniquement à l’entreprise qui opère le nœud. Vous ne détenez pas les clés privées et vous ne contrôlez pas les canaux. Votre solde de portefeuille n’est qu’une ligne dans la base de données d’un prestataire. C’est certes très pratique pour les débutants, l’expérience utilisateur est souvent fluide, mais la question de fond est la suivante : quel est l’intérêt de se donner la peine d’utiliser Bitcoin et Lightning si l’on renonce précisément à ce qui les distingue des monnaies étatiques et des banques ?

Les deux principales propositions de valeur de Bitcoin sont la souveraineté monétaire (ne plus dépendre d’une autorité centrale pour l’émission et la détention) et la résistance à la censure (impossibilité pour un tiers d’empêcher ou de filtrer des paiements légitimes). Un système custodial sur Lightning va frontalement à l’encontre de ces deux objectifs : vous ne pouvez pas vérifier l’offre monétaire interne de la plateforme, et par définition, un opérateur qui détient tous les fonds et tous les canaux peut censurer, retarder, prioriser ou bloquer vos paiements. Dans ces conditions, on peut légitimement se demander, **à quoi bon utiliser le bitcoin via Lightning si c’est pour reproduire les mêmes modèles de confiance et de dépendance qu’avec les systèmes de monnaie étatique traditionnels**.

> What is needed is an electronic payment system based on cryptographic proof instead of trust, allowing any two willing parties to transact directly with each other without the need for a trusted third party.

*Satoshi Nakamoto, Bitcoin White Paper.*

Au-delà de la philosophie, les inconvénients plus concrets pour vous sont les suivants. D’abord, vous n’avez aucun moyen de vérifier que l’entreprise détient réellement les bitcoins correspondant aux soldes affichés. Elle peut fonctionner en réserve fractionnaire, être victime d’un piratage, faire faillite ou disparaître purement et simplement. Vous êtes alors un créancier parmi d’autres, sans garantie effective de récupération de vos fonds.

Ensuite, l’entreprise est soumise à des risques réglementaires : injonctions, gel de fonds, demandes de blocage d’utilisateurs ou de transactions, surveillance renforcée, voire interdiction pure et simple d’activité dans certaines juridictions. Chaque contrainte qui pèse sur le prestataire se répercute mécaniquement sur vous.

Sur le plan de la confidentialité, la situation n’est pas meilleure. Un opérateur custodial voit l’ensemble de vos flux : montants, fréquences, destinataires, soldes, habitudes de dépenses. Combinées à des informations données pas l'application et éventuellement à l’analyse de chaîne sous-jacente sur Bitcoin, ces informations peuvent permettre de dresser un profil très précis de votre activité financière. Là encore, on s’éloigne totalement de l’objectif de réduction de la surveillance financière que permet Bitcoin.

La bonne nouvelle, c’est qu’aujourd’hui, exploiter son propre nœud Lightning n’est plus réservé à des experts techniques, comme ça pouvait être le cas à la fin des années 2010. Il existe des solutions relativement simples à mettre en place pour les particuliers que nous allons détailler dans le prochain chapitre.


## Choisir la solution adaptée à son usage








# Créer son premier nœud Lightning

## Installer LND avec Umbrel



## Ouvrir son premier canal Lightning



## Fermer un canal Lightning



# Gérer les liquidités de son nœud Lightning



## Utiliser un gestionnaire de nœud Lightning

(ThunderHub / RTL) + Alby Hub ?

## Obtenir de la liquidité entrante

LN+ / LSP




# Protéger son nœud Lightning

## Watchtower : rôle et mise en place



## Sauvegarder son nœud et protéger ses sats





# Libérer le potentiel de votre nœud Lightning




## Connecter un portefeuille mobile





## Gérer les frais et le routage


## Naviguer dans le réseau Lightning


### Visualiser sa position (LNVisualizer)





