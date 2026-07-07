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

Vous avez déjà acquis vos premiers sats, sécurisé vos fonds en self-custody et déployé un nœud Bitcoin afin d’être souverain dans votre usage on-chain. L’étape suivante consiste à gagner la même autonomie sur Lightning : c’est précisément l’objectif de ce cours.

LNP 202 s’adresse aux utilisateurs intermédiaires et vous guide pas à pas dans le déploiement de votre premier nœud Lightning, sans compétences techniques avancées.

Vous apprendrez à installer LND sur Umbrel, ouvrir et gérer vos canaux, superviser votre nœud et connecter un portefeuille mobile, afin de profiter d’une expérience comparable à celle d’un portefeuille custodial, tout en conservant un contrôle total sur vos fonds.

+++


# Introduction
<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>

## Aperçu du cours
<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>

LNP 202 est un cours pratique, conçu pour vous rendre autonome sur Lightning en exploitant votre propre nœud. L’objectif est simple : partir d’un nœud Bitcoin déjà en place, déployer LND sur Umbrel, sécuriser correctement l’ensemble, ouvrir et gérer vos premiers canaux, puis utiliser votre nœud au quotidien depuis un portefeuille mobile. Ce cours suppose que vous avez déjà suivi le cours BTC 202, car je pars du principe que votre nœud Bitcoin sous Umbrel est en place et synchronisé. Nous ne reviendrons pas ici sur comment mettre en place un nœud Bitcoin.

https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Pour mieux comprendre la mécanique interne de Lightning, le cours LNP 201 est également vivement recommandé, même s’il n’est pas indispensable pour suivre ce cours :

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Dans la première partie de ce cours LNP 202, nous reviendrons sur ce qu’est réellement un nœud Lightning, ce que cela change par rapport à un simple portefeuille, et pourquoi l’exploitation d’un nœud personnel constitue la seule manière d’utiliser Lightning sans déléguer vos sats à un tiers de confiance. Cette partie se terminera par un choix stratégique : déterminer quelle solution correspond à votre usage, depuis les approches les plus simples jusqu’au nœud Lightning classique, celui que nous mettrons en place dans ce cours.

Dans la partie 2 du cours, vous installerez LND sur Umbrel, puis vous mettrez en place les éléments qui évitent les erreurs les plus coûteuses : une stratégie de sauvegarde réaliste et une protection contre la triche via une watchtower. Une fois ces bases en place, vous ouvrirez votre premier canal, afin de commencer à payer sur Lightning avec votre propre infrastructure.

Vous l’aurez donc compris : dans ce cours LNP 202, nous allons mettre en place un nœud Lightning en mode *plug-and-play* via Umbrel, et non de manière classique en ligne de commande, afin que cette approche soit adaptée à des utilisateurs intermédiaires. Si vous préférez une installation via les lignes de commande, je vous recommande plutôt de suivre le tutoriel ci-dessous. Par ailleurs, d’autres cours sur Lightning, plus avancés et orientés ligne de commande, sont également en préparation.

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

La partie 3 vous fera ensuite passer d’un nœud qui fonctionne à un nœud que vous saurez piloter. Vous commencerez par déterminer votre profil d’opérateur de nœud Lightning (consommateur, commerçant ou routeur), puis vous prendrez en main un logiciel gestionnaire complet, afin de suivre vos canaux et d’agir proprement sur votre topologie. Enfin, vous aborderez un point très important de Lightning : comment obtenir de la liquidité entrante, que ce soit via des solutions payantes ou coopératives.

La partie 4 portera sur l’usage quotidien. Vous mettrez en place une connexion entre votre nœud et un client mobile, pour payer et encaisser simplement depuis votre smartphone, sans renoncer à la self-custody. Nous verrons d’abord une approche réseau via *Tailscale*, puis une approche protocole via *Nostr Wallet Connect*, avec leurs avantages et leurs compromis respectifs. Le cours se conclura par un dernier chapitre qui vous donnera les bonnes habitudes pour pérenniser votre autonomie, à la fois sur le plan opérationnel et sur le plan pédagogique.

Si vous suivez ce cours LNP 202 dans l’ordre, vous disposerez à la fin d’une configuration complète pour votre nœud Lightning, fonctionnelle au quotidien, et surtout maîtrisée.


## Comprendre ce qu'est un nœud Lightning
<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>

Avant de lancer votre propre nœud, je vous propose de revoir brièvement dans ce chapitre le fonctionnement théorique de base du [Lightning Network](https://planb.academy/resources/glossary/lightning-network). Il est en effet important de comprendre les mécanismes en jeu, car cela vous permettra d’identifier les risques et d’adopter les bonnes pratiques pour les limiter. Je n’entrerai toutefois pas dans les détails ici, car ce n’est pas l’objectif principal de ce cours. Si vous souhaitez approfondir le sujet, je vous recommande vivement de consulter le cours LNP 201 de Fanis Michalakis, qui fait référence en la matière :

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### C'est quoi un nœud Lightning ?

Revenons aux fondamentaux : avant de définir ce qu’est un nœud, il faut comprendre ce qu’est le Lightning Network. Il s’agit d’un protocole de couche supérieure, construit au-dessus de Bitcoin, destiné à permettre des transactions en BTC [off-chain](https://planb.academy/resources/glossary/offchain), rapides (à finalité quasi instantanée) et généralement peu coûteuses. "*Off-chain*" signifie que les transactions effectuées sur Lightning ne sont pas destinées à apparaître sur la [blockchain](https://planb.academy/resources/glossary/blockchain) principale de Bitcoin. Lightning constitue également une réponse, certes partielle, à l’augmentation de l’usage de Bitcoin et aux phénomènes de congestion [on-chain](https://planb.academy/resources/glossary/onchain), qui suscitent des inquiétudes quant à la [scalabilité](https://planb.academy/resources/glossary/scalability) du système.

Pour fonctionner, Lightning repose sur l’ouverture de [canaux de paiement](https://planb.academy/resources/glossary/payment-channel) entre les participants, au sein desquels les transactions peuvent être réalisées presque instantanément, avec des frais souvent minimes, sans qu’il soit nécessaire de les inscrire une par une sur la blockchain Bitcoin. Ces canaux peuvent rester ouverts très longtemps et ne requièrent des transactions on-chain qu’au moment de leur ouverture et de leur fermeture.

Un [nœud Lightning](https://planb.academy/resources/glossary/lightning-node) est justement un participant à ce réseau Lightning : il ouvre des canaux et réalise des paiements avec d’autres nœuds. Concrètement, un nœud Lightning est un logiciel exécuté sur un ordinateur et qui implémente le protocole Lightning Network. Il peut s’agir, par exemple, de LND, Core Lightning ou Eclair. Le rôle de ce logiciel va principalement être :
* de se connecter à un [nœud Bitcoin](https://planb.academy/resources/glossary/full-node) pour obtenir les informations de la blockchain principale ;
* de créer et gérer des canaux de paiement bidirectionnels avec d’autres nœuds ;
* d'échanger des messages avec l’ensemble du réseau Lightning.

![Image](assets/fr/001.webp)

### Nœud vs. Wallet Lightning : une distinction importante

Sur Bitcoin (on-chain), on parle de "*wallet*" pour désigner un logiciel qui gère vos [clés privées](https://planb.academy/resources/glossary/private-key), calcule votre solde à partir de vos [UTXOs](https://planb.academy/resources/glossary/utxo) et construit vos transactions. Ce [portefeuille](https://planb.academy/resources/glossary/wallet) peut s’appuyer sur votre propre nœud Bitcoin ou sur un nœud d'une autre personne, mais aujourd’hui, le rôle du nœud et celui du portefeuille on-chain sont clairement distincts.

Sur Lightning, il est plus difficile de réutiliser ce vocabulaire sans créer de confusion. Parler d’un "*wallet Lightning*" est assez vague, car en réalité il n’existe pas de portefeuille Lightning véritablement self-custodial sans qu’il repose sur un nœud. Seulement deux situations sont donc possibles :

- Avoir un véritable nœud Lightning (donc non-custodial) : le logiciel que vous utilisez (par exemple une app mobile comme Phoenix ou une instance LND sur Umbrel) exécute réellement un nœud, et vous détenez effectivement les clés permettant de récupérer vos bitcoins. Dans ce cas, votre "*wallet Lightning*" n’est en réalité qu’une interface utilisateur au-dessus d’un nœud Lightning, qu’il soit embarqué ou distant.

- Utiliser un service custodial : vous utilisez une application qui vous affiche un solde en [sats](https://planb.academy/resources/glossary/satoshi-sat) sur Lightning, mais en arrière-plan, les fonds se trouvent sur le nœud d’un prestataire (par exemple : Wallet of Satoshi). Vous ne possédez ni les clés, ni le contrôle des canaux. Votre solde n’est qu’une écriture comptable dans la base de données de l'entreprise. C’est comparable au fait de laisser ses bitcoins sur une plateforme d’échange, avec tous les risques associés. Dans ce cas, votre "*wallet Lightning*" n’est qu’un accès à un compte géré par un opérateur qui, lui, exploite un vrai nœud Lightning.

Il n’existe donc aucun entre-deux sur Lightning : soit vous avez un nœud (même embarqué) et vous êtes en self-custody, soit vous n’en avez pas, et une entreprise détient vos sats. Mais comme nous le verrons dans les chapitres suivants, ces deux usages peuvent parfois être difficiles à distinguer. Par exemple, Phoenix est une application mobile qui embarque un véritable nœud Lightning, mais l’utilisateur n’en a pas forcément conscience, car toute la complexité de son fonctionnement est presque entièrement cachée.

### Rappels sur le fonctionnement du Lightning Network

Dans cette section, je vous propose un rappel rapide du fonctionnement de Lightning. Une nouvelle fois, si vous souhaitez une présentation plus approfondie des concepts théoriques, je vous invite à consulter le cours dédié LNP 201.

#### Canaux de paiement : ouvrir, mettre à jour et fermer

Le cœur du réseau Lightning repose sur les canaux de paiement bidirectionnels. Un canal peut être ouvert (c’est-à-dire créé), mis à jour au fil des transactions Lightning, puis finalement fermé. Du point de vue on-chain, un canal n’est rien d’autre qu’une [sortie](https://planb.academy/resources/glossary/output) [multisignature](https://planb.academy/resources/glossary/multisig) 2/2.

![Image](assets/fr/002.webp)

Du point de vue de Lightning, il s’agit d’un canal de paiement disposant de [liquidités](https://planb.academy/resources/glossary/liquidity-lightning) réparties entre les deux participants.

![Image](assets/fr/003.webp)

- **Ouverture d’un canal :**

Deux nœuds décident d’ouvrir un canal. L’un d’eux engage des bitcoins dans une transaction on-chain appelée *transaction de funding*. Cette transaction crée une sortie reposant sur un [script](https://planb.academy/resources/glossary/script) multisignature 2-of-2, ce qui signifie que dépenser ces fonds sur Bitcoin nécessite la [signature](https://planb.academy/resources/glossary/digital-signature) des deux nœuds du canal. Avant de diffuser cette transaction, la partie qui apporte les fonds demande à l’autre de signer une *transaction de retrait*, non publiée on-chain, mais qui lui permet de récupérer ses fonds en cas de problème.

![Image](assets/fr/004.webp)

- **Transactions d’engagement :**

L’état du canal (c’est-à-dire la répartition des sats entre A et B) est représenté par une *[transaction d’engagement](https://planb.academy/resources/glossary/commitment-transaction)*, connue des deux nœuds mais non diffusée immédiatement sur la blockchain. Cette transaction décrit comment redistribuer on-chain les fonds du canal en fonction des paiements réalisés sur Lightning.

À chaque paiement Lightning, les deux nœuds signent un nouvel état qui remplace le précédent. L’ancien est révoqué grâce à un mécanisme de clés de révocation : si l’un des participants tente de diffuser un ancien état, l’autre peut récupérer l’intégralité des fonds en guise de pénalité.

L’idée importante ici est qu’il existe en permanence une transaction Bitcoin signée, non diffusée on-chain, conservée par les nœuds, et qui permet de redistribuer les sats de chacun selon les paiements opérés sur le Lightning Network.

![Image](assets/fr/005.webp)

- **Fermeture de canal :**

Un canal peut être fermé proprement via une fermeture coopérative, lorsque les deux parties s’accordent sur l’état final du canal, ou de manière unilatérale (une fermeture forcée) si l’un des participants cesse de coopérer ou devient injoignable. Dans tous les cas, la fermeture prend la forme d’une transaction on-chain qui dépense la sortie 2/2 et répartit les fonds entre les participants selon le dernier état valide du canal.

![Image](assets/fr/006.webp)

Lightning fonctionne ainsi comme une couche secondaire ancrée sur Bitcoin : seuls certains événements (l’ouverture et la fermeture des canaux) apparaissent sur la blockchain principale. Les paiements intermédiaires restent off-chain.

Avant de continuer, voici deux notions essentielles pour comprendre la gestion d’un canal Lightning :
- La *liquidité* : c'est la quantité de sats disponibles d’un côté du canal ;
- La *[capacité](https://planb.academy/resources/glossary/lightning-channel-capacity)* : c'est le montant total verrouillé dans l’output multisig 2/2, c’est-à-dire la somme des liquidités des deux côtés du canal.

#### Un réseau de canaux et de liquidité

Un canal ne sert pas uniquement aux paiements entre deux nœuds : il s’inscrit dans un réseau global de canaux interconnectés. Votre nœud peut ainsi router des paiements pour d’autres utilisateurs à travers ses propres canaux, et vous pouvez envoyer des sats à un nœud Lightning avec lequel vous n’avez aucun canal direct, tant qu’un chemin valide peut être trouvé entre vos deux nœuds.

Chaque nœud connaît, via le protocole de [gossip](https://planb.academy/resources/glossary/gossip), une carte de ce réseau : quels canaux existent, quels nœuds sont connectés par un canal bidirectionnel, et quelles capacités sont publiées. Pour envoyer un paiement à un destinataire sans canal direct, votre nœud calcule un itinéraire composé de plusieurs sauts : votre nœud → nœud X → nœud Y → nœud destinataire. À chaque saut, le paiement transite dans un canal qui doit disposer de suffisamment de liquidité dans le sens du paiement.

![Image](assets/fr/007.webp)

La liquidité d’un canal n’est donc pas symétrique : un côté peut être très chargé tandis que l’autre est presque vide. La gestion de cette liquidité, c'est-à-dire savoir où se trouvent les sats et dans quel sens ils peuvent circuler, constitue l’un des aspects les plus importants de l’exploitation d’un nœud Lightning. Nous aborderons cela en détail dans les chapitres pratiques à venir.

#### HTLC : acheminer un paiement sans se faire voler

Pour permettre aux paiements de transiter par des nœuds intermédiaires sans nécessiter de confiance, Lightning utilise des [contrats intelligents](https://planb.academy/resources/glossary/smart-contract) appelés *[HTLC](https://planb.academy/resources/glossary/htlc)* (*Hashed Time-Locked Contracts*). Pour faire simple, un HTLC conditionne le transfert de fonds à la révélation d’un secret et intègre une contrainte temporelle permettant de protéger l’expéditeur en cas d’échec de la transaction. Chaque paiement est donc soumis à la présentation d’une préimage (un secret dont le [hachage](https://planb.academy/resources/glossary/hash-function) correspond à une valeur convenue). Si le destinataire final fournit cette préimage, il peut réclamer les fonds, ce qui permet en cascade à chaque nœud intermédiaire de récupérer les siens.

![Image](assets/fr/008.webp)

Je vous épargne les détails techniques du fonctionnement des HTLCs, car ils ne sont pas indispensables dans le cadre de ce cours. Vous en trouverez une explication approfondie dans la formation théorique LNP 201. Retenez simplement que les HTLCs permettent d’effectuer des échanges atomiques (*atomic swaps*) : soit le transfert aboutit entièrement et personne n’est lésé dans le routage, soit il échoue et chaque participant récupère ses fonds initiaux. Il n’existe pas d’entre-deux possible.

### Les principales implémentations de nœuds Lightning

Tout comme pour Bitcoin, il existe plusieurs implémentations du protocole Lightning. Plusieurs équipes indépendantes développent leurs propres versions, toutes interopérables puisqu’elles respectent les mêmes spécifications (les [BOLT](https://planb.academy/resources/glossary/bolt)). Voici les principales implémentations utilisées aujourd’hui.

#### LND (*Lightning Network Daemon*)

LND est une implémentation complète du protocole Lightning, écrite en Go et développée par Lightning Labs.

![Image](assets/fr/009.webp)

#### Core Lightning (*CLN*)

Core Lightning (anciennement *C-Lightning*) est l’implémentation développée par Blockstream. Elle est écrite en C, avec certains composants en Rust.

![Image](assets/fr/010.webp)

#### Eclair

Eclair est une implémentation écrite en Scala et développée par l’entreprise française ACINQ. ACINQ exploite l’un des plus importants nœuds de routage du réseau Lightning avec Eclair, et utilise cette implémentation comme base logicielle pour ses propres produits, comme l’application Phoenix.

![Image](assets/fr/011.webp)

#### LDK (*Lightning Development Kit*)

LDK (*Lightning Development Kit*) est un kit de développement en Rust, maintenu par Spiral (Block, ex-Square). Ce n’est pas un daemon prêt à l’emploi comme LND ou CLN, mais une bibliothèque destinée aux développeurs souhaitant intégrer Lightning directement dans leurs applications.

![Image](assets/fr/012.webp)

Dans ce cours LNP 202, nous nous concentrerons principalement sur LND, car il s’agit de l’implémentation la plus utilisée dans les solutions clé en main destinées aux particuliers, comme Umbrel.

Voilà pour ce bref rappel sur le fonctionnement de Lightning. Une nouvelle fois, si certains concepts vous échappent ou si vous souhaitez les approfondir avant de passer à la pratique, le cours de Fanis Michalakis est la référence incontournable sur le sujet :

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Pourquoi exploiter son propre nœud Lightning ?
<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>

Répondre à cette question est assez simple, puisqu’elle est rhétorique : sans son propre nœud, on n’utilise plus réellement Lightning, mais seulement l’illusion de Lightning au travers de l’infrastructure d’une entreprise.

Utiliser un portefeuille Lightning custodial signifie que les bitcoins appartiennent techniquement à l’entreprise qui opère le nœud. Vous ne détenez pas les clés privées et vous ne contrôlez pas les canaux. Votre solde de portefeuille n’est qu’une ligne dans la base de données d’un prestataire. C’est certes très pratique pour les débutants, l’expérience utilisateur est souvent fluide, mais la question de fond est la suivante : quel est l’intérêt de se donner la peine d’utiliser Bitcoin et Lightning si l’on renonce précisément à ce qui les distingue des monnaies étatiques et des banques ?

Les deux principales propositions de valeur de Bitcoin sont la souveraineté monétaire (ne plus dépendre d’une autorité centrale pour l’émission et la détention) et la résistance à la censure (impossibilité pour un tiers d’empêcher ou de filtrer des paiements). Un système custodial sur Lightning va frontalement à l’encontre de ces deux objectifs : vous ne pouvez pas vérifier l’offre monétaire interne de la plateforme, et par définition, un opérateur qui détient tous les fonds et tous les canaux peut censurer, retarder, prioriser ou bloquer vos paiements. Dans ces conditions, on peut légitimement se demander, **à quoi bon utiliser le bitcoin via Lightning si c’est pour reproduire les mêmes modèles de confiance et de dépendance qu’avec les systèmes de monnaie étatique traditionnels**.

> What is needed is an electronic payment system based on cryptographic proof instead of trust, allowing any two willing parties to transact directly with each other without the need for a trusted third party.

*Satoshi Nakamoto, Bitcoin White Paper.*

Au-delà de la philosophie, les inconvénients plus concrets pour vous sont les suivants. D’abord, vous n’avez aucun moyen de vérifier que l’entreprise détient réellement les bitcoins correspondant aux soldes affichés. Elle peut fonctionner en réserve fractionnaire, être victime d’un piratage, faire faillite ou disparaître purement et simplement. Vous êtes alors un créancier parmi d’autres, sans garantie effective de récupération de vos fonds.

Ensuite, l’entreprise est soumise à des risques réglementaires : injonctions, gel de fonds, demandes de blocage d’utilisateurs ou de transactions, surveillance renforcée, voire interdiction pure et simple d’activité dans certaines juridictions. Chaque contrainte qui pèse sur le prestataire se répercute mécaniquement sur vous.

Sur le plan de la confidentialité, la situation n’est pas meilleure. Un opérateur custodial voit l’ensemble de vos flux : montants, fréquences, destinataires, soldes, habitudes de dépenses. Combinées à des informations données par l'application et éventuellement à l’analyse de chaîne sous-jacente sur Bitcoin, ces informations peuvent permettre de dresser un profil très précis de votre activité financière. Là encore, on s’éloigne totalement de l’objectif de réduction de la surveillance financière que permet Bitcoin.

La bonne nouvelle, c’est qu’aujourd’hui, exploiter son propre nœud Lightning n’est plus réservé à des experts techniques, comme ça pouvait être le cas à la fin des années 2010. Il existe des solutions relativement simples à mettre en place pour les particuliers que nous allons détailler dans le prochain chapitre.


## Choisir la solution adaptée à son usage
<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>

Il est aujourd’hui possible d'avoir une expérience utilisateur très proche de celle d’un portefeuille Lightning custodial, tout en restant en self-custody. L’objectif de ce chapitre est justement de vous aider à choisir la voie la plus adaptée à votre profil.

### Option 1 : ne pas utiliser Lightning directement

La première solution consiste tout simplement à ne pas utiliser Lightning de manière native, mais à passer par un portefeuille Bitcoin ou [Liquid](https://planb.academy/resources/glossary/liquid-network) qui embarque des [atomic swaps](https://planb.academy/resources/glossary/atomic-swap). C’est par exemple le cas des applications Aqua ou BULL Wallet, qui permettent de payer des [invoices](https://planb.academy/resources/glossary/invoice-lightning) Lightning sans exploiter vous-même un nœud Lightning, mais tout en restant en self-custody.

Le principe est le suivant : vos fonds restent en Bitcoin on-chain ou sur Liquid, dans un portefeuille dont vous détenez les clés de manière classique. Lorsque vous scannez une invoice Lightning, le portefeuille envoie une transaction (on-chain ou Liquid) vers un service d'atomic swap. Ce service se charge ensuite de réaliser le paiement Lightning depuis son propre nœud, en échange de vos bitcoins reçus on-chain ou via Liquid. En pratique, vous n’avez donc pas de canaux Lightning à gérer, mais vous pouvez tout de même régler des invoices Lightning.

![Image](assets/fr/013.webp)

L’avantage majeur de cette approche, par rapport à un portefeuille Lightning custodial classique, est que vous restez en possession de vos fonds à 100 % à chaque instant. Les bitcoins sont dans votre portefeuille on-chain ou Liquid, avec votre propre [phrase mnémonique](https://planb.academy/resources/glossary/seed). Même pendant le swap, vous restez en possession de vos fonds, car le swap est atomique. Il repose sur un mécanisme cryptographique qui garantit qu’il n’existe que deux issues possibles : soit le swap réussit entièrement, soit il échoue et le service ne peut pas s’approprier vos fonds.

La plupart des portefeuilles qui proposent ce type de fonctionnalité s’appuient sur [Boltz](https://boltz.exchange/) pour la partie technique du swap.

Cette solution présente aussi des avantages intéressants en termes de confidentialité, surtout lorsqu’elle est couplée à Liquid. Pour un débutant, c’est également très simple à mettre en place et à sauvegarder : une phrase mnémonique classique, pas de canaux, pas de liquidité à équilibrer...

En revanche, cette approche a des limites. D’abord, elle n’est pas incensurable : vous dépendez de la disponibilité et de la bonne volonté du service de swap. Si celui-ci ne veut plus traiter votre compte, ou cesse d’opérer, vous ne pouvez plus payer d'invoices Lightning par son intermédiaire. Ensuite, il existe des frais non négligeables : vous payez à la fois les [frais de transaction](https://planb.academy/resources/glossary/transaction-fees) on-chain ou Liquid, et la commission du service de swap. Aussi, en cas de forte augmentation des frais on-chain, cela peut devenir très cher d'utiliser Lightning.

Donc pour un usage ponctuel, cela reste acceptable, mais pour un utilisateur très actif sur Lightning, il vaut mieux faire les choses comme il faut avec un vrai nœud Lightning.

### Option 2 : les nœuds Lightning embarqués

La deuxième catégorie de solutions repose sur les nœuds Lightning embarqués directement dans une application mobile. Phoenix Wallet a été le pionnier de ce modèle et reste une référence. Aujourd’hui, d’autres projets proposent des approches comparables, comme Zeus (en mode embedded) ou BitKit.

L’idée est simple : l’application exécute en réalité un nœud Lightning, mais toutes les opérations complexes sont gérées automatiquement en arrière-plan. Vous disposez d’une interface de "*wallet Lightning*" avec une phrase mnémonique pour la sauvegarde, vous voyez un solde et vous payez des invoices, mais vous ne gérez ni canaux, ni liquidité, ni la plupart des paramètres.

![Image](assets/fr/014.webp)

Ces solutions sont toujours self-custodiales. Les clés qui contrôlent les fonds sont générées et stockées sur votre téléphone, et la sauvegarde passe par une seed ou un mécanisme équivalent. Vous n’êtes pas simplement titulaire d’un compte chez un prestataire, vous possédez réellement des bitcoins verrouillés dans des canaux qui vous appartiennent et ne peuvent pas vous être volés.

Les avantages des nœuds LN embarqués sont nombreux :
* installation et prise en main extrêmement simples ;
* expérience utilisateur proche d’un wallet Lightning custodial, mais tout en étant en self-custody ;
* pas de gestion manuelle des canaux ou de la liquidité ;
* sauvegarde relativement simple.

Mais ces portefeuilles embarqués ont aussi des limites importantes. D’abord, sur le plan de la confidentialité, l’opérateur du service (par exemple ACINQ dans le cas de Phoenix) dispose d’une vision assez fine des flux qui transitent par votre nœud : montants, fréquences, destinataires, même si c'est amené à s'améliorer, notamment avec l'adoption progressive des *Trampoline Nodes*. Ensuite, vous êtes fortement dépendant de cet opérateur comme pair Lightning principal. Si le nœud d’ACINQ devient indisponible (dans le cas de Phoenix), si l’entreprise subit des pressions réglementaires ou change son modèle économique, votre expérience utilisateur peut être fortement dégradée, voire compromise.

Enfin, cette simplicité a un prix. Les services de nœuds LN embarqués facturent généralement des frais spécifiques sur les dépôts, les retraits ou certaines opérations de gestion de canaux. Ce modèle reste cohérent au regard du service offert selon moi, mais pour un usage intensif, il peut se révéler beaucoup plus coûteux qu’un nœud Lightning classique bien géré.

### Option 3 : le nœud Lightning classique

La troisième solution, celle que nous allons approfondir dans ce cours LNP 202, consiste à exploiter un nœud Lightning classique sur un serveur ou un appareil dédié.

Par "*classique*", j'entends que vous installez et configurez vous-même une implémentation Lightning (par exemple LND) au-dessus de votre propre nœud Bitcoin. Vous choisissez vos pairs, vous ouvrez vos canaux, vous gérez votre [liquidité entrante](https://planb.academy/resources/glossary/inbound-capacity) et sortante, et vous définissez vos politiques de frais de routage.

Sur le plan de la souveraineté, c’est la meilleure solution. Vous ne dépendez plus d’une entreprise spécifique pour vos canaux ou vos paiements : si un pair vous censure ou ferme un canal, vous pouvez en ouvrir un autre avec un nœud différent. Si un service disparaît, vos sats restent dans les canaux que vous contrôlez, et vous pouvez les rapatrier on-chain. Vous avez également la possibilité d’optimiser vos coûts à long terme : une fois vos canaux correctement dimensionnés et gérés, le coût global des paiements peut devenir très faible.

En termes de confidentialité, vous êtes évidemment soumis aux limites du modèle de Lightning lui-même, mais vous ne livrez pas l’intégralité de votre activité à un opérateur unique.

En revanche, mettre en place un nœud Lightning classique est évidemment plus complexe : il faut installer, configurer, maintenir, surveiller les mises à jour, comprendre la logique des canaux et des politiques de frais, gérer les canaux et les liquidités, etc. Une mauvaise configuration, une sauvegarde négligée ou une gestion imprudente peuvent conduire plus facilement à la perte de sats. Le nœud doit également tourner en permanence.

C’est précisément ce chemin que je vous propose de suivre dans ce cours, en vous accompagnant dans chaque étape pour limiter les risques et structurer votre approche.

### Quelle solution pour quel profil d’utilisateur ?

Pour choisir la solution adaptée à votre profil d'utilisateur Lightning, il faut vous situer sur deux axes : votre fréquence d’utilisation de Lightning et votre appétence pour la gestion technique.

Vous réalisez peu de paiements Lightning, de manière ponctuelle, mais vous souhaitez tout de même pouvoir régler des invoices LN depuis votre téléphone de temps en temps, sans renoncer à la self-custody : un portefeuille Bitcoin ou Liquid avec fonctionnalité de swap est probablement la meilleure option. Vous restez propriétaire de vos fonds, vous ne gérez pas de nœud, mais vous acceptez des frais un peu plus élevés en échange de la simplicité.

https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Vous utilisez Lightning assez régulièrement et vous souhaitez bénéficier des avantages d’un véritable nœud, sans pour autant passer du temps sur la gestion des canaux, des frais ou de l’infrastructure : un nœud Lightning embarqué sur mobile est une bonne solution. Vous conservez la garde de vos fonds, l’UX reste très accessible, et toute la complexité est cachée, au prix d’une dépendance marquée à un opérateur.

https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Vous êtes un utilisateur intermédiaire ou avancé, prêt à investir du temps pour comprendre et piloter votre infrastructure, et vous tenez à disposer d’un maximum de contrôle sur vos canaux, votre liquidité et vos frais : un nœud Lightning classique sur serveur est la meilleure voie. C’est la solution la plus exigeante, mais aussi la plus cohérente avec l’idée de souveraineté de Bitcoin.


# Créer son premier nœud Lightning
<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>

## Installer LND avec Umbrel
<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>

Maintenant que nous avons revu les bases de Lightning et les solutions disponibles, il est temps de passer à la pratique. Pour suivre ce cours, vous aurez besoin d’un nœud Bitcoin synchronisé sur Umbrel. Cette formation LNP 202 est la continuité de BTC 202 ; si vous n’avez pas encore de nœud Bitcoin, je vous invite à suivre cette autre formation avant de revenir ici une fois votre nœud synchronisé. Je vous recommande vivement de la consulter, car je ne reviendrai pas en détail sur son fonctionnement, sa configuration, ni sur les mesures de sécurité à appliquer.

https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Dans ce premier chapitre, nous allons voir comment installer LND sur votre Umbrel. Le fonctionnement d’Umbrel rend cette étape très simple, puisqu’il suffit d’installer une application.

Depuis la page d’accueil, ouvrez l’`App Store` situé en bas de l’interface.

![Image](assets/fr/015.webp)

Dans la barre de recherche, saisissez `Lightning Node`, puis cliquez sur l’application.

![Image](assets/fr/016.webp)

Cliquez ensuite sur le bouton `Install` pour lancer l’installation.

![Image](assets/fr/017.webp)

Depuis la page d’accueil, cliquez sur l’application pour l’ouvrir, puis sélectionnez `Setup a new node`.

![Image](assets/fr/018.webp)

Une phrase mnémonique de 24 mots vous est donnée. Conservez-la précieusement dans un endroit sûr. Nous verrons plus en détail dans le prochain chapitre comment récupérer l’accès à votre nœud Lightning (c'est un processus beaucoup plus complexe que pour un simple portefeuille Bitcoin) mais retenez pour le moment que cette phrase joue un rôle crucial et doit être sauvegardée avec le plus grand soin.

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Sauvegardez cette phrase de la même manière qu’une phrase mnémonique classique : sur un support physique (papier ou métal) stocké dans un endroit sécurisé, puis cliquez sur le bouton `NEXT`.

![Image](assets/fr/019.webp)

Saisissez ensuite les mots de votre phrase afin de vérifier que vous les avez correctement notés.

![Image](assets/fr/020.webp)

Un message d’avertissement vous rappellera que l’application est en version bêta et que le Lightning Network demeure une technologie expérimentale. Évidemment, n’engagez jamais sur votre nœud Lightning des montants que vous n’êtes pas prêt à perdre.

Vous arriverez ensuite sur l’interface principale de votre nœud Lightning. Sur la gauche, vous trouverez votre portefeuille Bitcoin on-chain hébergé sur votre nœud. C'est celui qui a été généré à partir de la phrase de 24 mots que vous venez de sauvegarder.

Au centre, vous trouverez votre portefeuille Lightning. Il correspond en réalité à vos [liquidités sortantes](https://planb.academy/resources/glossary/outbound-capacity), c’est-à-dire les bitcoins qui vous appartiennent au sein de vos canaux Lightning.

Sur la droite, vous verrez plusieurs informations importantes concernant votre nœud :
- Le nombre de connexions et de canaux ouverts ;
- Le total de vos liquidités sortantes, c’est-à-dire ce que vous pouvez théoriquement dépenser sur Lightning ;
- Le total de vos liquidités entrantes, c’est-à-dire ce que vous pouvez théoriquement recevoir sur Lightning.

![Image](assets/fr/021.webp)

Nous allons commencer par personnaliser notre nœud. Cliquez sur les trois petits points en haut à droite de l’interface, puis sur `Advanced Settings`. Dans le sous-menu `Personalization`, vous pouvez définir un nom public pour votre nœud (évitez d’utiliser votre véritable nom) et choisir sa couleur.

![Image](assets/fr/046.webp)

Cliquez ensuite sur le bouton vert `SAVE AND RESTART` afin de redémarrer votre nœud et appliquer ces modifications.

Votre nœud Lightning est désormais prêt à ouvrir ses premiers canaux pour effectuer des paiements. Mais avant cela, voyons comment protéger vos sats !

## Sauvegarder son nœud Lightning
<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>

Avant d’envoyer vos premiers sats sur votre nœud, il est important de comprendre comment fonctionne sa sauvegarde et quels sont les risques associés. Contrairement à un simple portefeuille Bitcoin on-chain, la sauvegarde d’un nœud Lightning est assez complexe : une mauvaise stratégie peut mener à la perte définitive de vos fonds. Dans ce chapitre, nous allons voir ce qu’il faut réellement sauvegarder, puis comment Umbrel gère ce processus avec LND.

Dans cette formation, nous utilisons l'implémentation LND (*Lightning Network Daemon*). Bien que les principes soient similaires sur les autres implémentations, les fichiers et procédures de récupération dont je vais parler sont spécifiques à LND.

### Que faut-il sauvegarder sur un nœud Lightning ?

Sur un nœud Lightning, il ne suffit pas de sauvegarder la seed et d’espérer que tout reviendra à la normale. Plusieurs éléments jouent des rôles différents, et il est donc important de bien les distinguer.

#### La seed (*aezeed*)

Lorsque vous initialisez LND, vous recevez une seed de 24 mots. Il s’agit d’un format spécifique à LND appelé "*aezeed*". Ce n’est pas une seed BIP39 classique, même si elle lui ressemble beaucoup. À partir de cette seed, LND dérive les clés privées de votre portefeuille on-chain associé au nœud Lightning, c’est-à-dire les adresses dans lesquelles vous pouvez recevoir ou vers lesquelles vous pouvez rapatrier des bitcoins suite à des fermetures de canaux.

![Image](assets/fr/019.webp)

Cette seed permet donc de recréer le portefeuille on-chain associé à votre nœud et de retrouver les fonds qui ont déjà été rapatriés on-chain (par exemple après une fermeture de canal). En revanche, la seed seule ne suffit pas à restaurer vos canaux Lightning encore ouverts, car elle ne contient pas les informations nécessaires sur l'état de vos canaux.

#### La base de données de canaux (`channel.db`)

LND conserve l’état détaillé de vos canaux dans une base de données nommée `channel.db`. Cette base contient notamment :
* la liste de vos canaux ouverts ;
* vos pairs et leurs identifiants ;
* les dernières transactions d’engagement pour chaque canal (les états successifs qui définissent qui possède quoi dans le canal et permettent de récupérer les fonds on-chain en cas de problème) ;
* les informations nécessaires pour punir un pair qui tenterait de diffuser un ancien état.

Le problème de cette base de données, c'est qu'elle change en permanence : chaque paiement, chaque routage, chaque ouverture ou fermeture de canal modifie son contenu. C’est pour cela qu’une sauvegarde classique (par exemple une copie périodique de votre `channel.db`) est dangereuse. Si vous restaurez une version trop ancienne de `channel.db` et que vous remontez le nœud avec cet état obsolète, vos pairs peuvent considérer que vous êtes en train de diffuser un ancien état de canal. Dans ce cas, le protocole prévoit une pénalité : votre pair peut récupérer l’intégralité des fonds du canal, comme si vous aviez tenté de tricher.

En pratique, `channel.db` n’est donc pas un support de sauvegarde à proprement parler. C’est l’état vivant de votre nœud. La seule situation où il est raisonnable de s’en servir pour restaurer votre nœud, c’est lorsque vous récupérez cette base directement depuis une machine qui vient de tomber en panne (par exemple un disque encore lisible). Dans ce cas, vous récupérez l’état le plus récent et vous pouvez redémarrer LND sur une autre machine en vous appuyant sur cette base, en ayant la certitude que cet état est bien le plus à jour possible puisque l’ancienne machine ne fonctionne plus. Une autre situation où cette méthode peut servir de sauvegarde pertinente est celle d’une configuration à deux disques durs, avec une copie dynamique et permanente de l’un vers l’autre. Toutefois, ce type de mise en place est plus complexe à réaliser.

Mais faire des copies périodiques de `channel.db` et les stocker comme des backups à restaurer plus tard est une très mauvaise idée : le jour où vous les utilisez, vous prenez le risque de vous pénaliser vous-même et de perdre tous vos sats.

#### Le Static Channel Backup (SCB)

Pour rendre la récupération possible en cas de catastrophe, LND a introduit le mécanisme de *Static Channel Backup* (SCB). Il s’agit d’un fichier spécial, souvent nommé `channel.backup`, qui contient des informations statiques sur vos canaux : quels sont vos pairs, comment les contacter et quels sont vos canaux.

Ce fichier ne contient pas l’état détaillé du canal ni l’historique des mises à jour. Il ne permet pas de rouvrir les canaux dans l’état exact où ils étaient, ni de continuer à opérer ce nœud Lightning. Son rôle est plutôt de servir de point d’ancrage pour demander à vos pairs de vous aider à fermer proprement tous vos canaux, et donc recevoir vos sats on-chain, sur des clés que vous pouvez récupérer grâce à la seed. Ainsi, contrairement au fichier `channel.db`, qui est modifié à chaque paiement ou routage, le fichier SCB n’est mis à jour que lors de l’ouverture ou de la fermeture d’un canal.

Lors d’une récupération via SCB, le processus est le suivant :
- Vous restaurez votre seed (*aezeed*), ce qui recrée votre portefeuille on-chain associé au nœud Lightning ;
- Vous fournissez à LND votre SCB le plus récent ;
- LND utilise le SCB pour retrouver la liste de vos pairs et les canaux que vous aviez avec eux ;
- Il contacte chaque pair, lui indique que vous avez subi une perte de données et lui demande de "*force-close*" votre canal avec lui, afin que vous puissiez récupérer votre part on-chain.

L’idée est donc que vos pairs, en constatant que vous déclarez une perte de données, vont diffuser leur dernière transaction d’engagement et fermer le canal de force. Une fois ces transactions confirmées, vos fonds réapparaissent dans votre portefeuille on-chain (lié à la seed).

Ce mécanisme de récupération n’est toutefois pas parfait. D’abord, il ne permet pas à proprement parler de restaurer votre nœud Lightning, puisque tous les canaux seront fermés. Il faudra donc ensuite refaire un nouveau nœud Lightning de zéro. Ensuite, il ne garantit pas de récupérer 100 % des fonds, même s’il augmente considérablement les chances de retrouver vos soldes on-chain en cas de problème. En effet, ce protocole de récupération dépend de la coopération et de la disponibilité de vos pairs : si l’un d’eux est hors ligne, a perdu ses propres données ou refuse de coopérer, vos fonds peuvent rester bloqués, voire être définitivement perdus. C’est pourquoi il est important de ne pas conserver sur votre nœud Lightning, en temps normal, des canaux ouverts avec des pairs injoignables sur une longue durée. Si vous subissez une perte de données à ce moment-là et que le pair demeure injoignable, la récupération via le SCB sera impossible, et vos fonds resteront perdus tant que ce pair ne reviendra pas en ligne (peut-être pour toujours).

Pour résumer une bonne stratégie de sauvegarde Lightning sur LND repose sur trois piliers :
* Votre seed (*aezeed*), pour la couche on-chain ;
* Une sauvegarde automatique fiable du SCB ;
* Une bonne gestion des canaux en choisissant des pairs fiables et en fermant préventivement ceux qui sont souvent injoignables.

### Comment Umbrel gère la sauvegarde de votre nœud LND ?

Umbrel propose une mécanique de sauvegarde simplifiée pour le nœud LND, basée précisément sur le SCB. L’idée est de vous éviter de manipuler vous-même ce fichier, d'en faire une sauvegarde et d'automatiser au maximum le processus.

Lors de la création de votre nœud sur Umbrel, vous recevez une seed qui joue un double rôle :
* elle permet de dériver votre portefeuille Bitcoin on-chain associé à votre nœud Lightning ;
* elle sert à dériver un identifiant de sauvegarde et une clé de chiffrement utilisés pour les backups distants du SCB.

Grâce à ce mécanisme, Umbrel réalise automatiquement une sauvegarde chiffrée de votre SCB et la stocke sur ses serveurs via Tor. Le SCB est stocké chiffré grâce à une clé dérivée de votre seed. Ainsi, en cas de perte de données, il vous suffit de recréer un nœud Bitcoin et Lightning sur Umbrel, sur la même machine ou une autre, puis de saisir votre seed. Vous pourrez alors récupérer le dernier état de votre SCB depuis les serveurs d’Umbrel, le déchiffrer et lancer la procédure de récupération de vos fonds.

Ces sauvegardes sont chiffrées localement par votre nœud avant d’être envoyées, ce qui garantit la confidentialité de vos données : Umbrel ne peut pas lire le contenu du SCB. La transmission s’effectue via Tor, ce qui évite de faire fuiter votre adresse IP. De plus, votre Umbrel ajoute du bruit au trafic (padding aléatoire et faux backups envoyés à intervalles irréguliers) afin d’empêcher le serveur de déduire précisément quand vous ouvrez ou fermez un canal.

Le principal avantage de cette méthode est qu’elle simplifie considérablement la sauvegarde de votre nœud Lightning : vous n’avez qu’à sauvegarder votre seed une seule fois lors de l’initialisation du nœud. Cela comporte certes des risques, puisqu’il s’agit uniquement d’un backup du SCB, mais pour des montants raisonnables, c’est un compromis acceptable.

### Les bonnes pratiques pour limiter les risques de perte

Même avec la sauvegarde Umbrel, quelques bonnes pratiques simples permettent de réduire fortement le risque de perdre des sats :

- Surveiller la disponibilité de vos pairs :

Si un canal important est fréquemment associé à un pair injoignable ou instable, il est plus prudent de le fermer proprement tant que votre nœud fonctionne encore. Une fermeture coopérative ou forcée préventive élimine une source potentielle de problème en cas de récupération par SCB.

- Éviter de concentrer trop de liquidité sur des pairs inconnus :

Plus un pair a avec vous un canal de grande capacité, plus il est important qu’il soit fiable. Privilégiez des nœuds sérieux, bien connectés et actifs, afin qu’une éventuelle récupération future via le SCB puisse se dérouler correctement.

- Compléter Umbrel par des sauvegardes locales :

En plus de la sauvegarde automatique d'Umbrel, vous pouvez également conserver une copie chiffrée de votre fichier SCB (`channel.backup`) sur un support externe et mettre cette sauvegarde à jour de manière périodique. L’idéal est de la renouveler à chaque ouverture ou fermeture de canal. Cela vous donne une solution de secours si, pour une raison quelconque, le service de sauvegarde automatique d’Umbrel devenait indisponible.

- Gérer sa seed de la bonne manière :

Votre seed Umbrel permet non seulement de restaurer votre portefeuille on-chain, mais aussi de dériver la clé de chiffrement des sauvegardes. Un attaquant qui y aurait accès pourrait donc lancer une récupération et transférer vos fonds vers son propre portefeuille, sans même avoir accès physiquement à votre nœud.

Aussi, si vous devez restaurer votre nœud mais que vous n’avez plus votre seed, vous ne pourrez rien récupérer : tous vos sats seront perdus. Il est donc très important de sauvegarder cette seed avec le plus grand soin, uniquement sur un support physique (papier ou métal), et de la conserver dans un lieu sécurisé. Pour plus d'informations sur la gestion d’une seed, je vous invite à consulter ce tutoriel :

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Comment sauvegarder son nœud Lightning sur Umbrel ?

Maintenant que vous avez compris le fonctionnement théorique, passons à la pratique. Depuis votre application `Lightning Node` (qui correspond en réalité à LND), cliquez en haut à droite sur les trois petits points.

![Image](assets/fr/022.webp)

Trois éléments nous intéressent ici pour la sauvegarde :
- Vérifiez que l’option `Automatic backups` est bien activée. C’est elle qui permet d’envoyer automatiquement votre SCB chiffré aux serveurs d’Umbrel.
- Vous pouvez ensuite choisir si l’envoi doit s’effectuer via Tor ou en clearnet grâce à l’option `Backup over Tor`. Comme expliqué dans les sections précédentes, je vous recommande vivement d’utiliser Tor pour préserver votre confidentialité.
- Enfin, vous disposez d’un bouton `Download channel backup file`, qui vous permet de télécharger sur votre ordinateur un fichier `channel.backup`, c’est-à-dire un instantané chiffré de votre SCB. Cela vous donne la possibilité de réaliser ponctuellement des sauvegardes locales supplémentaires, en complément de celles automatiquement envoyées aux serveurs d’Umbrel.

Vous savez désormais comment protéger les sats de votre nœud Lightning face aux pertes de données. Dans le prochain chapitre, nous verrons comment sécuriser votre nœud contre les tentatives de triche.


## Watchtower : rôle et mise en place
<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>

Sur Lightning, chaque canal repose sur une suite d’états successifs, représentés par des transactions d’engagement non publiées. À chaque paiement ou routage Lightning, les 2 participants du canal construisent un nouveau couple de transactions d’engagement qui reflète la répartition actuelle des fonds dans le canal. Les anciennes transactions d’engagement deviennent alors obsolètes.

Si l’une des parties publie un état obsolète, l’autre a le droit de la sanctionner et de récupérer l’intégralité des fonds du canal. Dans ce chapitre, nous allons voir brièvement comment fonctionne ce mécanisme, puis nous expliquerons comment mettre en place une ***watchtower*** : un système permettant de protéger votre nœud Lightning contre d’éventuelles tentatives de triche.

### Comprendre le fonctionnement des watchtowers

À un instant donné, chaque partie du canal possède une transaction d’engagement qui lui permettrait, si elle la publiait, de fermer le canal et de récupérer sa part des fonds. C'est ce que l'on appelle une fermeture forcée. Mais si elle tentait de publier une transaction d’engagement plus ancienne, correspondant à un état antérieur du canal où elle détenait davantage de sats, alors cette transaction serait considérée comme une tentative de triche. Dans ce cas, la contrepartie peut utiliser la clé de révocation associée à cet ancien état pour récupérer l’intégralité des fonds du canal, tandis que le tricheur est temporairement bloqué par le timelock.

Ce système fait que publier un ancien état, c'est-à-dire tenter de tricher, est très risqué : si l’autre partie voit passer cette transaction dans les mempools ou sur la blockchain avant l’expiration du timelock, elle peut utiliser la clé de révocation et récupérer l’intégralité des fonds. **La sécurité de votre canal Lightning repose donc sur votre capacité à détecter une tentative de triche dans la fenêtre de temps imposée par le timelock**.

#### Pourquoi les watchtowers sont nécessaires ?

Le mécanisme de pénalité ne fonctionne que si la partie lésée est en mesure :
* de surveiller chaque nouveau bloc Bitcoin pour voir si une transaction d’engagement concernant le canal a été publiée ;
* de déterminer si cette transaction correspond au dernier état valide ou à un état révoqué ;
* en cas d’état révoqué, de diffuser à temps la transaction de justice qui utilise la clé de révocation pour récupérer l’intégralité des fonds avant l’expiration du timelock.

![Image](assets/fr/023.webp)

Dans un scénario idéal, votre nœud Lightning est en ligne 24/7, synchronisé, et surveille la blockchain en continu. Il peut alors, à lui seul, détecter une tentative de triche et réagir. Mais en pratique, un nœud Lightning personnel peut s’éteindre, notamment en cas de coupure prolongée d’électricité ou de connexion internet.

C’est précisément pendant ces périodes d’indisponibilité que le risque devient réel : si un pair malhonnête publie un ancien état pendant que votre nœud est hors ligne, et que le timelock s’écoule sans réaction de votre part, la tricherie devient effective. Vous perdez alors une partie ou la totalité de vos fonds présents dans le canal.

Les watchtowers ont justement été introduites pour réduire ce risque. Une watchtower est un service externe qui, à votre place, surveille la blockchain pour détecter une éventuelle publication d’un ancien état sur l’un de vos canaux, et qui diffuse automatiquement la transaction de pénalité en votre nom si nécessaire. Ainsi, même si votre nœud Lightning reste hors ligne pendant une longue période, tant que la watchtower que vous utilisez est opérationnelle, elle pourra protéger vos fonds en surveillant toute tentative de triche et en appliquant la pénalité correspondante dès qu’elle en détecte une.

#### Le fonctionnement d’une watchtower

Le fonctionnement d’une watchtower est conçu pour minimiser les informations qu’elle apprend sur vos canaux, tout en lui donnant les moyens d’agir en cas de problème :
- À chaque nouvel état de canal avec un pair, votre nœud prépare à l’avance une transaction de pénalité potentielle. Cette transaction permettrait, en cas de triche de ce pair, de récupérer l’intégralité des fonds du canal ;
- Votre nœud chiffre ensuite cette transaction de pénalité à l’aide du TXID de la transaction d’engagement correspondante (celle qui serait utilisée en cas de triche par le tricheur). Tant qu’aucune fermeture n’a lieu, la watchtower ne peut pas déchiffrer cette transaction, car elle ne connaît pas entièrement le TXID de la transaction de triche ;
- Votre nœud envoie à la watchtower un paquet contenant la transaction de pénalité chiffrée ainsi que la moitié du TXID de la potentielle transaction de triche.

Comme le TXID transmis à la watchtower est incomplet, celle-ci ne peut pas déchiffrer la transaction de justice. En revanche, elle peut surveiller la blockchain à la recherche d’un TXID qui correspond à la partie qu’elle possède. Si elle détecte une telle transaction, elle tente alors d’utiliser le TXID complet de cette transaction pour déchiffrer votre transaction de pénalité. Si le déchiffrement réussit, elle sait qu’il s’agit d’une tentative de triche et publie immédiatement, à votre place, la transaction de justice.

![Image](assets/fr/024.webp)

La watchtower n’a donc aucune visibilité sur les détails de vos canaux : ni l’identité de vos pairs, ni les soldes, ni la structure des transactions. Elle ne voit que des paquets chiffrés. La seule information qu’elle peut déduire est le rythme de mise à jour de vos canaux, puisqu’elle reçoit un paquet à chaque nouvel état, mais sans pouvoir en connaître le contenu. En cas de triche, elle découvrira certes les informations du canal en déchiffrant la transaction de pénalité, mais au moins, vos sats seront sauvés.

Ce mécanisme repose ainsi sur un compromis : vous déléguez à la watchtower la capacité de publier une transaction de pénalité pré-signée, mais cette transaction reste totalement opaque pour elle tant qu’aucune triche n’a lieu. La watchtower ne peut ni modifier les destinataires, ni détourner les fonds, puisqu’elle ne possède qu’une transaction déjà signée, dont les sorties sont figées en votre faveur. Elle ne peut pas non plus connaître les détails d’un canal lors d’une fermeture forcée légitime ou d’une fermeture coopérative, car les TXID ne correspondent pas. En revanche, la watchtower reste un tiers de confiance minimal : vous devez compter sur elle pour être en ligne et pour diffuser correctement votre transaction de justice au moment où vous en avez besoin.

#### Devenir une watchtower

En théorie, n’importe quel nœud Lightning peut agir comme watchtower pour d’autres nœuds (s'ils utilisent la même implémentation, par exemple LND), tout en étant lui-même protégé par d’autres nœuds jouant ce rôle pour lui. Je vous montrerai dans les sections pratiques suivantes comment configurer simplement ce mécanisme sur votre LND sous Umbrel.

Une stratégie intéressante pourrait donc être de vous accorder avec des amis bitcoiners de confiance pour jouer mutuellement le rôle de watchtower. Vous surveillez leurs canaux, et ils surveillent les vôtres.

### Trouver une watchtower altruiste

Si vous ne connaissez personne capable de vous fournir un service de watchtower dans votre entourage il existe des watchtowers publiques dites altruistes sur lesquelles vous pouvez vous connecter. Par exemple, dans ce cours LNP 202, je vous propose de vous connecter au service de watchtower proposé conjointement par LN+ et Voltage. Il s’agit d’une watchtower pour LND.

Pour s'y connecter, voici les identifiants :

- Via Tor :

```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```

- Via clearnet :

```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Pour les remercier de fournir ce service gratuit de watchtower, [vous pouvez leur faire un don via Lightning](https://lightningnetwork.plus/donation). 

Maintenant que nous disposons d’un service de watchtower altruiste, voyons comment le configurer concrètement sur notre nœud LND sous Umbrel.

### Configurer une watchtower

Depuis l’application `Lightning Node`, cliquez sur les trois points en haut à droite de l’interface, puis sélectionnez `Advanced Settings`.

![Image](assets/fr/025.webp)

Rendez-vous ensuite dans le menu `Watchtower`.

![Image](assets/fr/026.webp)

Activez l’option `Watchtower Client`, puis cliquez sur le bouton `SAVE AND RESTART NODE`. Patientez le temps que LND redémarre.

![Image](assets/fr/027.webp)

Une fois le redémarrage terminé, retournez dans le même menu et renseignez l’identifiant de la watchtower altruiste de votre choix dans le champ prévu à cet effet. Cliquez ensuite sur le bouton `ADD` pour confirmer. Vous pouvez également ajuster le paramètre `Watchtower Client Sweep Fee Rate` : il s’agit du taux de frais que vous êtes prêt à payer pour une éventuelle transaction de justice diffusée par la watchtower. Inutile de choisir un taux excessivement élevé, mais évitez aussi un taux trop bas, au risque que la transaction de justice ne soit pas confirmée à temps.

Redémarrez votre nœud à l’aide du bouton `SAVE AND RESTART NODE` afin d’appliquer ces modifications.

![Image](assets/fr/028.webp)

Si vous revenez dans ce même menu, vous pourrez constater que votre nœud Lightning est désormais protégé par la watchtower que vous venez d’ajouter.

![Image](assets/fr/029.webp)

Une watchtower altruiste est généralement suffisante, surtout si vous ne placez pas de montants trop importants sur votre nœud Lightning et si vous avez une bonne gestion de votre nœud (ne pas le laisser off trop longtemps). Pour renforcer encore votre sécurité, vous pouvez également en ajouter plusieurs en répétant ce même processus.

## Ouvrir son premier canal Lightning
<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>

Si vous êtes arrivé jusqu’ici, vous savez déjà qu’un nœud Lightning sans canal est un peu comme un wallet vide : il existe, mais il ne sert à rien. Pour pouvoir envoyer ou recevoir des paiements, votre nœud doit être relié à au moins un autre nœud du réseau Lightning via un canal. Par la suite, il sera fortement recommandé d’ouvrir plusieurs canaux, pour des raisons de résilience et d’efficacité de routage. Nous verrons également dans les chapitres suivants comment gérer vos liquidités, optimiser votre topologie de canaux et utiliser des outils plus avancés que l’interface de base de LND sur Umbrel.

Mais dans ce chapitre d’introduction, l’objectif est simplement de comprendre comment choisir un bon pair Lightning, où trouver l’information nécessaire pour sélectionner ses pairs, et enfin comment ouvrir son premier canal via l'interface de base de LND.

### Comment choisir un bon pair Lightning ?

Lorsque vous ouvrez un canal, vous devez choisir un pair : c'est un autre nœud Lightning auquel votre nœud sera directement connecté via un canal. Ce choix du pair est important, car il aura un impact direct sur :
* la facilité avec laquelle vos paiements trouveront une route ;
* la fiabilité de vos canaux dans le temps ;
* vos frais de routage.

Il n’existe pas de pair parfait valable pour tout le monde, mais plusieurs critères concrets permettent de repérer de bons candidats.

#### 1. La connectivité du nœud

Un bon pair est un nœud bien connecté au réseau Lightning. Cela ne signifie pas seulement disposer d’un grand nombre de canaux (même si cela peut constituer un indicateur) mais surtout être relié à d’autres nœuds fiables et occuper une position suffisamment centrale dans le graphe du réseau.

Un nœud bien connecté augmente vos chances de trouver une route efficace vers la plupart des destinations pour vos paiements. Il réduit également le nombre de nœuds intermédiaires nécessaires, ce qui limite les frais.

À l’inverse, ouvrir votre premier canal vers un nœud isolé ou faiblement connecté risque de restreindre vos possibilités : vous pourrez payer ce pair, mais beaucoup plus difficilement le reste du réseau.

#### 2. La capitalisation et la capacité des canaux

Un bon pair est aussi un nœud suffisamment capitalisé. Cela se voit à travers la capacité totale de ses canaux (la somme des sats engagés sur l’ensemble de ses canaux) et la capacité moyenne de ses canaux (il vaut souvent mieux avoir seulement quelques canaux bien capitalisés que beaucoup de petits canaux).

Un nœud avec une capacité ridicule, ou dont tous les canaux sont minuscules, ne pourra pas router des paiements avec de gros montants, ce qui se traduira par des échecs de routage pour vous.

#### 3. Les politiques de frais

Chaque nœud fixe ses propres frais de routage (`base fee` et `fee rate`). Un bon pair ne pratique pas de frais exorbitants sur des canaux stratégiques. Pour un premier canal il est préférable de privilégier un nœud avec des frais plutôt modérés, afin de ne pas handicaper vos propres paiements.

Rappelez-vous que vos propres frais de routage influencent aussi la perception que les autres auront de vous comme pair : un nœud qui change sans cesse ses frais ou qui impose des coûts absurdes est rarement apprécié.

#### 4. La stabilité et l'ancienneté

La stabilité d’un pair est un critère très important. Un bon nœud affiche un uptime élevé (il est très rarement hors ligne), il conserve ses canaux ouverts longtemps et il ne joue pas en permanence à ouvrir/fermer des canaux sans raison.

Des canaux anciens et encore actifs sont un bon signal : ils suggèrent que la relation est profitable pour le pair, que le nœud sait gérer son capital et qu’il ne ferme pas n’importe quand, ce qui vous évite de payer sans cesse des frais on-chain de fermeture et de réouverture.

À l’inverse, un pair souvent hors ligne ou qui ferme rapidement ses canaux peut être source de problèmes pour vous et de frais supplémentaires pour l'ouverture de nouveaux canaux.

Même avec ces critères, vous ne ferez pas des choix parfaits du premier coup. C’est normal : la qualité réelle d’un pair se révèle surtout à l’usage. Il est donc important de :
* surveiller l’activité de vos canaux (volumes routés, disponibilité...) ;
* fermer les canaux qui ne servent à rien ou dont le pair est trop souvent hors ligne ;
* réallouer votre capital vers de meilleurs pairs au fil du temps.

L’idée n’est pas d’ouvrir et fermer des canaux tous les jours (ce qui serait coûteux en frais on-chain), mais de faire évoluer progressivement votre topologie pour converger vers un ensemble de pairs fiables, bien connectés et compatibles avec vos besoins.

### Comment trouver un pair ?

Pour appliquer ces critères, vous aurez besoin d’outils qui donnent de la visibilité sur le réseau Lightning. Il existe plusieurs explorateurs et services qui permettent de faire cela. Parmi les explorateurs Lightning les plus connus, il y a [1ML](https://1ml.com/) et [Amboss](https://amboss.space/).

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

Ici, je vous propose toutefois d’utiliser [l’outil Lightning Terminal de Lightning Labs](https://terminal.lightning.engineering/), qui fournit un classement (certes basé sur des critères en partie subjectifs) des nœuds Lightning jugés les plus pertinents pour ouvrir un canal.

![Image](assets/fr/030.webp)

Le problème avec les très gros nœuds Lightning que l’on retrouve en tête de ce classement est que la plupart n’acceptent pas l’ouverture de canaux en dessous de montants très élevés. Beaucoup appliquent également des politiques strictes de gestion des pairs, ce qui peut conduire à la fermeture de votre canal. Par ailleurs, ces nœuds n’ont généralement aucun besoin de liquidité entrante au vu de leur nombre de connexions.

Je vous conseille donc plutôt de descendre dans ce classement afin de trouver un nœud bien connecté, fiable et suffisamment central dans le graphe du réseau, sans être excessivement gros. Par exemple, j’ai ici identifié le nœud Lightning du site stacker.news, qui est très bien connecté, dispose de capacités importantes et occupe une position centrale dans le graphe du réseau.

![Image](assets/fr/031.webp)

Une autre approche intéressante consiste à ouvrir un canal vers un nœud ayant besoin de liquidité entrante, comme un commerçant que vous connaissez, une association ou une communauté. Cette stratégie présente trois avantages :
- L’entité choisie ayant besoin de liquidité entrante, elle sera logiquement moins incitée à fermer votre canal sans raison ;
- Son activité économique augmente les chances de routage sur ce canal, et donc de percevoir quelques frais ;
- Vous rendez service à l’écosystème et contribuez utilement à d’autres bitcoiners.

Une fois un nœud pertinent identifié, vous pouvez récupérer son Node ID. Celui-ci correspond simplement à la concaténation de la clé publique du nœud, d'un `@` de séparation, de son adresse IP ou Tor, ainsi que du port utilisé. Cet identifiant est facilement accessible depuis le profil du nœud sur n’importe quel explorateur Lightning.

### Ouvrir son premier canal via LND

Maintenant que nous avons identifié le nœud avec lequel ouvrir notre premier canal, il nous faut disposer de sats à y bloquer. Pour cela, vous devez alimenter le portefeuille Bitcoin on-chain associé à votre LND.

Depuis l’interface principale de LND, repérez votre `Bitcoin Wallet`, puis cliquez sur le bouton `Deposit`. Une adresse de réception on-chain est alors générée : envoyez-y des sats. Le montant à transférer dépend de la capacité que vous souhaitez allouer à votre premier canal, mais gardez en tête qu’il faut envoyer légèrement plus que la capacité visée. Par exemple, si vous souhaitez ouvrir un canal de 500 000 sats, n’envoyez pas exactement 500 000 sats, mais un montant supérieur.

![Image](assets/fr/032.webp)

Une fois la transaction diffusée, elle apparaît dans l’interface. Attendez qu’elle soit confirmée avant de procéder à l’ouverture du canal. Vous verrez une flèche vert à côté de celle-ci lorsque ce sera le cas.

![Image](assets/fr/033.webp)

Descendez sur l'interface principale, puis cliquez sur `+ OPEN CHANNEL`.

![Image](assets/fr/034.webp)

Renseignez le `Node ID` du nœud avec lequel vous souhaitez ouvrir un canal, indiquez le montant que vous voulez y bloquer, puis ajustez les frais de la transaction d’ouverture en fonction de l’état du marché des frais on-chain. Évidemment, assurez-vous de disposer, au préalable, d’un solde suffisant dans votre portefeuille on-chain LND.

Une fois tous les paramètres complétés, cliquez sur le bouton `OPEN CHANNEL`.

![Image](assets/fr/035.webp)

Patientez ensuite le temps que la transaction d’ouverture soit confirmée on-chain. Votre premier canal sera alors officiellement opérationnel : félicitations !

On peut constater que, pour le moment, la liquidité du canal est à 100 % de mon côté : c’est normal, puisque c’est moi qui ai ouvert le canal. Au fil des paiements et du routage, cette répartition va évoluer, mais la capacité totale du canal restera toujours identique.

![Image](assets/fr/036.webp)

Maintenant que vous disposez d’un canal, vous pouvez effectuer vos premiers paiements sur Lightning, à condition que le nœud choisi soit correctement connecté au réseau. Nous verrons bien sûr, dans les chapitres suivants, comment mettre en place une méthode plus pratique pour payer des invoices Lightning depuis votre mobile. Mais pour l’instant, essayons d’effectuer un premier paiement directement depuis LND sur Umbrel.

Pour cela, dans la section `Lightning Wallet`, cliquez sur le bouton `SEND`, puis collez l’invoice à régler.

![Image](assets/fr/037.webp)

Le montant de l’invoice s’affiche. Validez le paiement en cliquant sur le bouton `SEND`.

![Image](assets/fr/038.webp)

Si une route valide est trouvée, votre premier paiement Lightning devrait aboutir.

![Image](assets/fr/039.webp)

Si l’on observe ensuite la répartition des liquidités dans le canal, on voit que mon pair dispose désormais de 5 002 sats de son côté. Cela correspond aux 5 000 sats du paiement que je viens d’effectuer et qu’il a routé vers le nœud du destinataire. Les 2 sats supplémentaires représentent les frais de routage que j’ai payés, puisque le destinataire a bien reçu exactement 5 000 sats.

![Image](assets/fr/040.webp)

Pour améliorer la fiabilité de nos paiements, il sera évidemment nécessaire d’ouvrir d’autres canaux. En fonction de nos objectifs, nous devrons également trouver un moyen de disposer de liquidité entrante afin de pouvoir recevoir des paiements sur Lightning. Ce sera précisément le sujet de la prochaine partie.

# Gérer son nœud Lightning
<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>

## Définir son profil d'opérateur de nœud
<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>

Maintenant que votre nœud Lightning est opérationnel, l’étape suivante consiste à définir votre profil d’opérateur. Ce choix est important, car il conditionne votre stratégie d’ouverture de canaux, le type de pairs à privilégier, ainsi que votre manière de gérer la liquidité.

Sur Lightning, pour que ça fonctionne, il faut avoir de la liquidité dans le bon sens. La liquidité sortante correspond à votre capacité à payer (des sats disponibles de votre côté des canaux). La liquidité entrante correspond à votre capacité à recevoir (des sats disponibles du côté de vos pairs). Autrement dit, votre profil se résume à une question simple : la majorité du temps, vos sats sortent-ils de votre nœud, ou y entrent-ils ?

### Le consommateur

C’est le profil de la grande majorité des utilisateurs. Vous exploitez votre nœud pour effectuer des paiements Lightning : acheter des biens et des services, régler des factures, envoyer des pourboires, bref, utiliser Lightning comme un moyen de paiement rapide. En revanche, vous recevez peu sur Lightning, ou seulement de manière marginale, par exemple quelques dons, des remboursements entre amis ou quelques micro-paiements.

Ce profil est le plus simple à gérer, car votre besoin principal est d’être capable de payer. Concrètement, cela signifie que vous devez disposer de liquidité sortante. Une fois que vous avez ouvert un ou plusieurs canaux correctement dimensionnés vers des nœuds stables et bien connectés, vos paiements sortants déplaceront mécaniquement la liquidité vers l’autre côté de vos canaux. C’est justement ce mouvement qui finit par créer naturellement une quantité raisonnable de liquidité entrante. Résultat : même si vous ne cherchez pas à recevoir régulièrement, vous serez tout de même capable de recevoir de temps en temps sans mettre en place une stratégie complexe. Vous n'avez donc pas besoin de vous soucier de vos liquidités entrantes.

Dans ce cours LNP 202, nous allons nous concentrer sur ce profil "*consommateur*" d'opérateur de nœud, car c’est celui qui correspond à la quasi-totalité des utilisateurs de Bitcoin sur Lightning.

### Le commerçant

Le commerçant est, en quelque sorte, l'inverse du consommateur. Ici, l’objectif principal n’est pas de payer, mais d’encaisser. Un commerce, un prestataire de services, une boutique en ligne ou un point de vente qui accepte Lightning recevra beaucoup de paiements entrants, et effectuera relativement peu de paiements sortants depuis ce nœud.

Ce profil est plus exigeant, car un paiement refusé sur Lightning représente potentiellement une vente perdue. La priorité devient donc la liquidité entrante. Si votre nœud ne dispose pas d’assez d’inbound, vos clients verront leurs paiements échouer, même s’ils ont les fonds, simplement parce qu’aucune route ne peut acheminer la liquidité vers vous dans le bon sens.

Le défi majeur du commerçant vient aussi de l’évolution naturelle des canaux. Si vous ne faites que recevoir, vos canaux vont progressivement se remplir de votre côté. Il faut donc prévoir des mécanismes pour maintenir et renouveler votre liquidité entrante.

Il existe toutefois un cas plus simple : le profil mixte consommateur et commerçant. Si vous encaissez sur Lightning, mais dépensez aussi sur Lightning (dépenses professionnelles, paiements à des fournisseurs, ou même dépenses personnelles), alors vos paiements sortants recréent naturellement de l’inbound. La gestion devient plus fluide, car les flux se compensent, et vous avez moins besoin de recourir à des mécanismes artificiels uniquement destinés à regagner de la liquidité entrante.

### Le routeur

Le routeur est un profil spécifique. Il n’exploite pas son nœud Lightning pour payer ou encaisser, mais pour router les paiements des autres et percevoir des frais. L’objectif devient donc d’être une route utile, fiable et économiquement compétitive au sein du graphe Lightning.

Pour être honnête avec vous, être routeur sur Lightning est une activité plus complexe qu’elle n’en a l’air, et la rentabilité est difficile à atteindre. D’abord, ouvrir et fermer des canaux coûte cher en frais on-chain. Or, pour router efficacement, vous devez souvent ajuster votre topologie, tester, fermer des canaux peu performants, en ouvrir d’autres, et rééquilibrer régulièrement votre liquidité. Ensuite, la concurrence est rude : de gros nœuds déjà établis captent naturellement une grande partie du trafic, et il est difficile de se faire une place sans immobiliser des capitaux importants dans des canaux bien dimensionnés.

S’ajoute aussi une exigence opérationnelle élevée. Un nœud de routage doit être extrêmement stable, surveillé, correctement sauvegardé, et géré avec rigueur. Il faut suivre la performance des canaux, adapter sa politique de frais, maintenir une liquidité équilibrée, gérer les pairs, et résoudre rapidement les problèmes techniques. Ce niveau d’implication peut être intéressant comme hobby technique ou comme contribution à l’infrastructure, mais si votre objectif est simplement d’utiliser Lightning de manière souveraine, se lancer dans le routage pour gagner de l’argent est rarement pertinent. C’est pour cette raison que ce cours LNP 202 ne traite pas ce profil en profondeur.

### Se situer clairement avant d’aller plus loin

Si vous vous reconnaissez dans le profil consommateur, votre priorité sera de pouvoir payer de manière fiable avec une gestion simple. Si vous êtes commerçant, votre priorité sera d’encaisser sans échec, ce qui implique une stratégie d'acquisition de liquidité entrante. Si vous envisagez le routage, il faut l’aborder comme une activité exigeante, incertaine économiquement et très chronophage.

Définir ce profil dès maintenant vous évitera un piège classique : appliquer une stratégie de canaux conçue pour un commerçant ou un routeur, alors que vous êtes simplement un utilisateur qui veut payer.

## Utiliser un gestionnaire de nœud Lightning
<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>

Dans la partie précédente de cette formation LNP 202, nous avons utilisé l’interface de base de l’application `Lightning Node` sur Umbrel. Cette interface est suffisante pour les opérations essentielles (consulter le solde, visualiser la répartition des liquidités, ouvrir et fermer un canal) mais elle est volontairement très simplifiée. Cette simplicité limite les options disponibles et ne donne pas accès à de nombreuses fonctionnalités avancées de votre nœud LND. C’est pour cette raison que nous allons maintenant utiliser un autre logiciel de gestion de nœud Lightning, plus complet.

Ce logiciel supplémentaire ne sera qu’une interface de gestion complémentaire pour votre nœud. Cela signifie que vous pourrez continuer à utiliser l’interface `Lightning Node` en parallèle, et même en utiliser plusieurs différentes si vous le souhaitez. Il s’agit simplement de différentes manières d’interagir avec le même nœud Lightning.

Parmi les logiciels les plus connus, on retrouve :
- [Alby Hub](https://albyhub.com/) ;
- [Ride The Lightning](https://www.ridethelightning.info/) ;
- [ThunderHub](https://thunderhub.io/).

Ces trois outils sont de bonnes solutions. Vous pouvez, si vous le souhaitez, les tester tous les trois avec votre nœud avant de choisir celui qui vous convient le mieux. Pour ma part, j’utilise ThunderHub par habitude et parce qu’il me semble plus complet que les autres. C’est donc cet outil que je vous présenterai dans cette formation, mais vous pouvez tout à fait opter pour l’une des deux autres alternatives. Nous disposons d’ailleurs d’un tutoriel dédié pour chacun de ces logiciels sur Plan ₿ Academy.

https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Installer ThunderHub

Ces logiciels peuvent tous être installés très facilement depuis l’App Store d’Umbrel. Comme je vous l’indiquais, nous allons utiliser ThunderHub ici, mais si vous souhaitez en tester un autre par la suite, la procédure sera similaire.

![Image](assets/fr/041.webp)

Umbrel vous fournit un mot de passe par défaut pour accéder à ThunderHub. Copiez-le : vous en aurez besoin juste après. Pensez également à l’enregistrer dans votre gestionnaire de mots de passe, car il vous sera demandé à chaque ouverture du logiciel.

![Image](assets/fr/042.webp)

Cliquez sur `Login`, puis collez le mot de passe fourni par Umbrel afin de vous connecter.

![Image](assets/fr/043.webp)

Vous arrivez ensuite sur la page d’accueil de ThunderHub, qui affiche les principales informations relatives à votre nœud Lightning.

![Image](assets/fr/044.webp)

Pour commencer, je vous recommande d’activer l'authentification à deux facteurs (2FA). Dans les paramètres, cliquez simplement sur `Enable` à côté de `Enable 2FA`, puis suivez le processus classique.

![Image](assets/fr/045.webp)

### Utiliser ThunderHub

ThunderHub est relativement simple à prendre en main. Tous les menus sont accessibles depuis la colonne de gauche de l’interface. Voici, pour résumer, le rôle de chacun :
- `Home` : vue d’ensemble du nœud, soldes et actions rapides ;
- `Dashboard` : tableau de bord personnalisable avec widgets et métriques ;
- `Peers` : visualisation et gestion des connexions avec les autres nœuds Lightning ;
- `Channels` : gestion complète des canaux (liquidité, frais, fermeture...) ;
- `Rebalance` : outil de rééquilibrage des canaux via des paiements circulaires ;
- `Transactions` : historique des paiements Lightning envoyés et reçus ;
- `Forwards` : statistiques de routage et frais générés par votre nœud ;
- `Chain` : portefeuille Bitcoin on-chain (UTXOs et transactions) ;
- `Amboss` : intégration Amboss pour le monitoring et les sauvegardes ;
- `Tools` : outils avancés (backups, rapports, génération de macaroons, signatures…) ;
- `Swap` : swaps Lightning/on-chain via Boltz ;
- `Stats` : statistiques globales et performances de votre nœud Lightning.

Avec cet ensemble de fonctionnalités, vous disposez de tous les outils nécessaires pour gérer efficacement votre nœud Lightning. Il n’est pas indispensable de maîtriser chaque option dans le détail dès maintenant : nous les découvrirons progressivement tout au long de ce cours. Si vous souhaitez toutefois approfondir l'utilisation de ce logiciel, je vous invite à consulter notre tutoriel dédié à ThunderHub :

https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Le menu qui nous intéressera le plus ici est `Channels`. Il offre une vue détaillée de l’ensemble des canaux de votre nœud, avec leur répartition de liquidités. Vous pouvez notamment consulter les canaux ouverts dans `Open`, ceux en attente d’ouverture ou de fermeture dans `Pending`, et les canaux déjà fermés dans `Closed`.

![Image](assets/fr/047.webp)

Pour un canal donné, vous pouvez cliquer sur le nom du pair ou sur l’identifiant du canal afin d’ouvrir sa page Amboss et obtenir plus d’informations. Vous pouvez également cliquer sur l’icône en forme de crayon pour modifier les paramètres du canal, notamment la politique de frais appliquée à ce canal si votre nœud route des paiements vers celui de votre pair.

![Image](assets/fr/048.webp)

Si vous utilisez votre nœud Lightning principalement comme "*consommateur*", il n’est pas nécessaire de modifier ces frais : vous pouvez conserver les valeurs par défaut. En revanche, si vous souhaitez mieux comprendre le fonctionnement des frais de routage sur Lightning, je vous recommande la formation LNP 201, et en particulier le chapitre 4.1 :

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

En cliquant sur la petite croix à côté d’un pair, vous pouvez initier la fermeture d’un canal. Si vous constatez, par exemple, qu’un pair est régulièrement inactif, il peut être pertinent de fermer ce canal afin de réallouer votre capital vers un pair plus fiable.

Deux options s’offrent alors à vous. La première, toujours préférable, est la fermeture coopérative. En confirmant cette action, votre nœud demande à votre pair de fermer le canal de manière conjointe. S’il accepte, vous pouvez diffuser la transaction de fermeture on-chain et récupérer votre part des fonds. Les avantages de cette méthode sont que vous choisissez les frais on-chain de la transaction, ce qui évite ainsi des coûts inutiles, et que les fonds sont récupérés plus rapidement, sans aucun timelock.

![Image](assets/fr/049.webp)

La seconde option est la fermeture forcée. Dans ce cas, vous ne sollicitez pas l’accord du pair et diffusez directement la dernière transaction d’engagement en votre possession. Je vous déconseille cette méthode sauf en dernier recours, par exemple si le pair refuse systématiquement les fermetures coopératives ou ne répond plus. La fermeture forcée présente deux inconvénients majeurs : des frais souvent très élevés, car ils ont été définis à l’avance pour anticiper une hausse des frais on-chain, et un délai de récupération des fonds, puisqu'ils sont bloqués par un timelock. Ce timelock permet de laisser le temps à votre pair de réagir en cas de tentative de triche (ce n'est évidemment pas le cas ici, mais il faut tout de même attendre).

![Image](assets/fr/050.webp)

Enfin, pour ouvrir un nouveau canal, rendez-vous dans le menu `Home` et cliquez sur `Open a Channel` dans la section `Liquidity`. Vous pourrez alors renseigner l’identifiant du nœud choisi, la capacité du canal, les frais de routage Lightning souhaités, ainsi que les frais on-chain pour la transaction d’ouverture.

![Image](assets/fr/051.webp)

Voilà pour les principales actions dont vous aurez besoin sur ThunderHub. Nous découvrirons d’autres fonctionnalités au fil des besoins dans ce cours LNP 202.

## Obtenir de la liquidité entrante
<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>

Vous l’aurez compris : disposer de liquidité sortante pour effectuer des paiements sur Lightning n’est pas particulièrement complexe. Il suffit d’ouvrir des canaux de votre propre initiative vers d’autres nœuds pour commencer à envoyer des sats. En revanche, disposer de liquidité entrante, pour recevoir des paiements sur Lightning, est plus compliqué, puisqu’il faut soit que d’autres nœuds ouvrent des canaux vers vous, soit que vous déplaciez vous-même la liquidité en effectuant des paiements.

Si vous adoptez un profil de "*consommateur*", il n’y a généralement pas lieu de s’inquiéter de la liquidité entrante. Votre usage du nœud Lightning sera majoritairement orienté vers les paiements plutôt que vers les encaissements. En effectuant simplement quelques paiements Lightning, vous créerez naturellement de la liquidité entrante au fil du temps.

En revanche, si vous êtes dans un profil de "*commerçant*", la situation est inversée : vous allez principalement encaisser des paiements et en effectuer peu. Vous ne pouvez donc pas compter uniquement sur vos propres paiements pour disposer de liquidité entrante. Il devient alors nécessaire que d’autres nœuds Lightning ouvrent des canaux vers le vôtre. Mais comment y parvenir ? Comment inciter d’autres opérateurs à immobiliser du capital pour vous ? C’est précisément ce que nous allons explorer dans ce chapitre.

### Acheter de la liquidité entrante

Comme vous vous en doutez, la manière la plus efficace d’inciter quelqu’un à agir reste de le rémunérer. Pour la liquidité entrante de votre nœud Lightning, le principe est exactement le même. La solution la plus simple pour obtenir l’ouverture de canaux vers votre nœud consiste à payer pour ce service et pour l’immobilisation de capital qu’il implique.

Si vous êtes une entreprise ou un commerçant, cette approche permet d’obtenir rapidement des canaux fiables afin d’encaisser les paiements de vos clients sans friction.

Il existe de nombreuses méthodes pour acheter de la liquidité entrante. Celle que j’utilise personnellement et que je vous recommande est la plateforme [Magma](https://magma.amboss.tech/) d’Amboss. Son utilisation est très simple, l’ouverture de canal est rapide et les tarifs sont généralement raisonnables. Magma fonctionne comme une place de marché avec des makers et des takers, mais sa version 2 a grandement simplifié l’expérience : il suffit de créer une demande, de payer le prix via Lightning, et Magma se charge automatiquement de la faire correspondre avec la meilleure offre disponible. Après six confirmations on-chain, votre canal avec liquidité entrante est opérationnel. Voici comment procéder :

Rendez-vous sur [le site de Magma](https://magma.amboss.tech/buy), dans la section `Buy Channels`.

![Image](assets/fr/052.webp)

Si vous le souhaitez, vous pouvez créer un compte afin de suivre vos différents achats, mais ce n’est pas obligatoire. Si vous ne créez pas de compte, Magma vous fournira simplement un identifiant de session, qui vous permettra de retrouver vos achats ultérieurement.

Une fois sur le site, renseignez les informations nécessaires à l’achat de liquidité. Sélectionnez `One Time` pour un achat ponctuel, puis indiquez le montant que vous êtes prêt à payer pour obtenir de la liquidité entrante. Plus le montant payé est élevé, plus le canal ouvert vers votre nœud aura une grande capacité. Une estimation de la capacité du canal apparaît en dessous : il s’agit d’une approximation, car le montant final dépendra de la meilleure offre trouvée par Magma, qui est parfois supérieure, parfois inférieure.

![Image](assets/fr/053.webp)

Renseignez ensuite l’identifiant de votre nœud. Vous pouvez le retrouver par exemple dans le menu `Node ID` de l’application `Lightning Node` sur Umbrel.

![Image](assets/fr/054.webp)

Une fois toutes les informations complétées, cliquez sur le bouton `Review & open order`.

![Image](assets/fr/055.webp)

Si vous n’avez pas créé de compte, Magma vous fournit une clé de session ainsi qu’un fichier de sauvegarde. Conservez soigneusement ces deux éléments, car ils vous permettront de retrouver cette commande ultérieurement ou de suivre son état en cas de problème. Une fois la sauvegarde effectuée, cliquez sur le bouton `Pay with Lightning`.

![Image](assets/fr/056.webp)

Magma génère alors une invoice Lightning correspondant au montant que vous avez choisi. Vous devez la payer. Si vous disposez déjà de canaux sur votre nœud Lightning, vous pouvez la payer directement depuis celui-ci, ou utiliser un autre portefeuille Lightning externe.

![Image](assets/fr/057.webp)

Une fois le paiement effectué, la transaction apparaît comme en cours de traitement dans l’interface Magma.

![Image](assets/fr/058.webp)

Après quelques minutes, la demande est traitée : un canal avec des sats est en cours d’ouverture vers votre nœud Lightning. Une fois la transaction d’ouverture confirmée on-chain, vous disposerez de la liquidité entrante correspondante.

![Image](assets/fr/059.webp)

Magma est également intégré directement dans ThunderHub. Dans l’onglet `Home`, descendez jusqu’à la section `Liquidity` et cliquez sur `Buy Inbound Liquidity`. Il vous suffira alors d’indiquer le montant souhaité et de confirmer. Aucune invoice n’est à payer manuellement, car ThunderHub se charge automatiquement du paiement depuis votre nœud.

![Image](assets/fr/060.webp)

Si vous êtes commerçant, ce type de service est particulièrement adapté, car il permet d’obtenir rapidement une quantité importante de liquidité entrante depuis des nœuds fiables, ce qui garantit que vos clients pourront vous payer sans difficulté. En revanche, si vous êtes un particulier ou si vous ne souhaitez pas payer pour disposer de liquidité entrante, il existe également des solutions gratuites. Voyons cela ensemble.

### Obtenir de la liquidité entrante par coopération

Si vous n’êtes pas commerçant mais que vous avez malgré tout besoin de disposer d’un peu de liquidité entrante (par exemple pour amorcer votre nœud au démarrage, en attendant d’avoir effectué quelques paiements) vous n’êtes pas forcément obligé de payer pour l’obtenir. L’une des solutions que je préfère consiste à coopérer avec d’autres opérateurs de nœuds qui, eux aussi, ont besoin de liquidité entrante, afin d’ouvrir mutuellement des canaux Lightning. De cette façon, l’ouverture d’un canal vous apporte de la liquidité sortante, tout en vous procurant en parallèle de la liquidité entrante, et ce gratuitement (modulo les frais on-chain pour l'ouverture).

Pour cela, vous pouvez bien sûr vous organiser directement avec des amis bitcoiners. Il existe toutefois une plateforme dédiée à ce type de mise en relation pour réaliser des ouvertures circulaires : [Lightning Network +](https://lightningnetwork.plus/). Le principe n’est pas d’ouvrir deux canaux entre les mêmes personnes, mais de mettre en place des ouvertures circulaires impliquant au minimum trois participants, voire davantage.

Prenons un exemple pour bien comprendre le fonctionnement de Lightning Network + :
- Un opérateur de nœud, nommé `A`, publie une annonce indiquant qu’il souhaite ouvrir un canal de 1 million de sats avec deux autres personnes ;
- L’annonce reste active jusqu’à ce que d’autres participants se manifestent ;
- Plus tard, deux opérateurs, `B` et `C`, rejoignent l’annonce du nœud `A`. Le triangle est alors constitué et la phase d’ouverture peut commencer.
- Le nœud `A` ouvre un canal vers le nœud `B` ;
- Le nœud `B` ouvre un canal vers le nœud `C` ;
- Le nœud `C` ouvre un canal vers le nœud `A`.

À l’issue de l’opération, chaque nœud dispose de 1 million de sats de liquidité sortante et de 1 million de sats de liquidité entrante. Ce schéma peut être étendu à quatre ou cinq participants.

Bien entendu, il n’existe aucun mécanisme technique garantissant qu’un participant ouvrira effectivement le canal qu’il s’est engagé à créer. C’est pourquoi la plateforme a mis en place un système de réputation, basé sur des avis positifs lorsque les opérateurs respectent leurs engagements. Et dans le pire des cas, si vous tombez sur une personne qui ne coopère pas, vous n’aurez pas perdu d’argent : vous aurez simplement manqué une opportunité d'avoir de la liquidité entrante.

Cette solution est particulièrement adaptée à un profil de "*consommateur*", car elle permet d’obtenir gratuitement de la liquidité entrante, tout en connectant son nœud à d’autres petits opérateurs. En revanche, si vous êtes commerçant, cette approche n’est généralement pas pertinente : chaque sat de liquidité entrante nécessite de bloquer un sat de liquidité sortante, et vos besoins importants en liquidité entrante impliqueraient alors une immobilisation de capital trop élevée.

Pour utiliser Lightning Network +, deux options s’offrent à vous : soit passer par l’application intégrée à Umbrel, soit utiliser le site web classique et créer un compte en vous connectant depuis votre nœud. Je vous recommande cette seconde solution, car l’application intégrée ne propose pas l’ensemble des fonctionnalités disponibles.

Rendez-vous sur le site de [Lightning Network +](https://lightningnetwork.plus/) et cliquez sur le bouton `Login` en haut à droite de l’interface.

![Image](assets/fr/061.webp)

Pour vous authentifier, vous devez signer le message fourni à l’aide de la clé privée de votre nœud Lightning. Avec ThunderHub, cette opération est très simple. Commencez par copier le message affiché par LN+.

![Image](assets/fr/062.webp)

Dans ThunderHub, allez dans l’onglet `Tools`, puis cliquez sur le bouton `Sign` dans la section `Messages`.

![Image](assets/fr/063.webp)

Collez le message d’authentification fourni par LN+, puis cliquez sur `Sign`.

![Image](assets/fr/064.webp)

ThunderHub signe alors ce message à l’aide de la clé privée de votre nœud. Copiez la signature générée.

![Image](assets/fr/065.webp)

Collez cette signature dans le champ correspondant sur le site LN+, puis cliquez sur `Sign in`.

![Image](assets/fr/066.webp)

Vous êtes maintenant connecté à LN+ avec votre nœud Lightning. Ce processus permet à LN+ de vérifier que vous êtes bien le propriétaire légitime du nœud que vous revendiquez sur leur plateforme.

![Image](assets/fr/067.webp)

Si vous le souhaitez, vous pouvez personnaliser votre profil LN+, par exemple en ajoutant une courte biographie.

Pour participer à votre première ouverture de canaux circulaires, rendez-vous dans le menu `Swaps` en haut de l’interface. Vous y trouverez l’ensemble des swaps actuellement disponibles en fonction des caractéristiques de votre nœud.

![Image](assets/fr/068.webp)

Pour rejoindre une offre de swap existante, il suffit de cliquer dessus puis de s’inscrire. Toutefois, sur LN+, le créateur d’un swap peut imposer certaines conditions aux participants, notamment un nombre minimal de canaux ou une capacité totale minimale du nœud. Il est donc possible, surtout au début, que peu d’offres soient accessibles à votre nœud. Dans mon cas, malgré quelques canaux déjà ouverts, aucune offre n’était disponible pour mon nœud. J’ai donc créé mon propre swap, et vous pouvez faire de même si vous êtes dans la même situation.

Cliquez sur `Start Liquidity Swap`, puis renseignez les paramètres de votre offre :
- Choisissez le nombre total de participants (3, 4 ou 5) ;
- Indiquez le montant des canaux à ouvrir (assurez-vous de disposer au minimum de cette somme sur votre portefeuille on-chain) ;
- Définissez la durée d’ouverture des canaux. Cela correspond à la période durant laquelle les participants s’engagent à ne pas les fermer ;
- Sur la droite, vous pouvez fixer des restrictions pour les participants : nombre minimal de canaux, capacité totale minimale et type de connexion acceptée.

Une fois tous les paramètres définis, cliquez sur le bouton `Start Liquidity Swap`.

![Image](assets/fr/069.webp)

Votre offre de swap est maintenant créée. Il ne reste plus qu’à attendre que d’autres opérateurs de nœuds s’y inscrivent. Si vos conditions ne sont pas trop restrictives, cela ne devrait pas prendre trop de temps. Pensez à surveiller l’état de votre swap dans les heures ou les jours suivants.

![Image](assets/fr/070.webp)

Toutes les places du swap ont été prises : nous passons désormais à la phase d’ouverture des canaux. Chaque participant peut voir, depuis son interface LN+, vers quel nœud il doit ouvrir un canal Lightning.

![Image](assets/fr/084.webp)

De votre côté, ouvrez le canal en utilisant le Node ID fourni par LN+ et en respectant le montant indiqué. Comme nous l’avons vu dans les chapitres précédents, vous pouvez effectuer cette ouverture soit via ThunderHub, soit avec un autre gestionnaire de nœud Lightning, soit directement depuis l’interface de base de l’application `Lightning Node`.

![Image](assets/fr/085.webp)

Une fois l’ouverture lancée, vous pouvez la voir apparaître dans la section des canaux en attente. Dans mon cas, il s’agit du canal avec le nœud `Plebian_fr`.

![Image](assets/fr/086.webp)

Vous pouvez ensuite retourner sur LN+ afin de confirmer que vous avez bien initié l’ouverture du canal. Cliquez simplement sur le bouton `Channel Opening Started`.

![Image](assets/fr/087.webp)

Lorsque tous les autres participants ont également ouvert le canal auquel ils s’étaient engagés, pensez à leur laisser un avis positif.

![Image](assets/fr/088.webp)

En cas de difficulté ou de retard, vous pouvez contacter vos pairs directement via la section commentaires située en bas de la page.

![Image](assets/fr/089.webp)

Il arrive que certains participants souhaitent rééquilibrer les canaux circulaires dès le départ, en effectuant un paiement vers eux-mêmes. Cela permet d’obtenir une répartition équilibrée des liquidités dans chaque canal. Si vous êtes dans un profil de "*consommateur*", ce n’est pas indispensable, mais vous pouvez soit effectuer ce rééquilibrage vous-même si vous le souhaitez, soit fixer temporairement les frais de vos canaux à zéro afin de faciliter l’opération pour le pair qui souhaite s’en charger. Parfois personne ne souhaite le faire.

![Image](assets/fr/090.webp)


# Libérer le potentiel de son nœud Lightning
<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>

## Connecter un portefeuille mobile via Tailscale
<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>

Ça y est, vous disposez désormais d’un nœud Lightning bien connecté, avec à la fois de la liquidité entrante et sortante. Tout est donc prêt pour utiliser votre nœud Lightning dans la vie réelle. Jusqu’ici, nous avons toujours utilisé directement des interfaces sur Umbrel, que ce soit celle de l’application `Lightning Node` ou l’interface `ThunderHub`. Ces outils fonctionnent pour envoyer et recevoir des paiements, mais ils ne sont clairement pas optimisés pour des paiements Lightning du quotidien. L’interface est pensée pour un usage sur ordinateur, peu pratique sur smartphone, et nécessite en plus d’être connecté au même réseau pour fonctionner correctement (même s’il est techniquement possible de s’y connecter à distance via Tor).

Dans la pratique, ce que nous recherchons en tant que bitcoiner, c’est une interface de wallet Lightning classique sur smartphone : la possibilité de scanner des invoices via QR code, et une interface simple pour payer et encaisser des sats. C’est précisément ce que nous allons mettre en place dans ce chapitre et le suivant. L’idée générale est d’avoir sur votre smartphone une application de wallet Lightning mobile, utilisable depuis n’importe où (pas uniquement depuis votre réseau local) mais qui, en arrière-plan, s’appuie sur votre propre nœud Lightning pour envoyer et recevoir des paiements.

### Quelles sont les solutions pour connecter un client mobile ?

Aujourd’hui, il existe plusieurs manières de procéder, tant du côté de l’application mobile que du type de connexion entre votre nœud et cette application. Les trois principaux modes de connexion sont :
- via ***Tor*** ;
- via un VPN ***Tailscale*** ;
- via ***Nostr Wallet Connect***.

Il y a quelques années, j’utilisais une connexion via ***Tor***, mais j’ai rapidement arrêté : le nombre d’échecs et les délais de communication étaient beaucoup trop importants. En théorie, cela fonctionne, mais en pratique, l’expérience utilisateur était catastrophique. Je vous déconseille donc cette approche.

L’alternative que j’ai ensuite adoptée consiste à utiliser un VPN ***Tailscale*** pour assurer la communication entre l’application mobile et le nœud. Cette solution fonctionne très bien : même sur des réseaux mobiles avec peu de débit, mes paiements sont toujours passés sans difficulté. C’est donc cette méthode que je vais vous présenter en premier dans ce chapitre, avec l’application Zeus.

Dans le chapitre suivant, nous verrons une autre solution plus récente, qui fonctionne elle aussi très bien : ***Nostr Wallet Connect***. Nous utiliserons cette fois l’application Alby Go afin de vous présenter une alternative, même si Zeus est également compatible avec NWC si vous le souhaitez.

### Installer et configurer Tailscale

Pour cette première méthode, nous allons avoir besoin de Tailscale. Il s’agit d’une solution de VPN basée sur WireGuard, qui permet de relier de manière sécurisée des appareils répartis sur Internet, tout en gérant automatiquement le chiffrement, l’authentification et la traversée des NAT. Pour faire simple, c’est comme si tous vos appareils étaient connectés au même réseau local que votre routeur, alors qu’ils peuvent se trouver n’importe où sur Internet.

Pour l’utiliser, vous devez commencer par créer un compte. Rendez-vous sur le site de Tailscale, puis cliquez sur le bouton `Get Started`.

![Image](assets/fr/071.webp)

Choisissez ensuite un fournisseur d’identité pour votre compte Tailscale. Personnellement, j’ai utilisé l’un de mes comptes GitHub pour me connecter.

![Image](assets/fr/072.webp)

Une fois connecté, quelques questions vous seront posées concernant votre usage. Répondez-y brièvement afin de poursuivre.

![Image](assets/fr/073.webp)

Tailscale vous propose ensuite d’installer un client sur votre machine. Pour l’instant, ce n’est pas ce qui nous intéresse : rendez-vous directement sur Umbrel et installez l’application Tailscale depuis l’App Store.

![Image](assets/fr/074.webp)

À l’ouverture de l’application, cliquez sur `Log In`, puis suivez le processus d’authentification en utilisant la même méthode que lors de la création de votre compte.

![Image](assets/fr/075.webp)

Cliquez sur `Connect` pour confirmer. Votre Umbrel est maintenant connecté à votre réseau VPN.

![Image](assets/fr/076.webp)

Téléchargez ensuite l’application Tailscale sur votre smartphone et connectez-vous de la même manière, avec le même compte. Attention : sur Android, il n’est pas possible d’utiliser deux VPN simultanément. Pour que Tailscale fonctionne, vous devrez donc désactiver tout autre VPN actif. De plus, chaque fois que vous souhaiterez utiliser votre nœud Lightning via Zeus, il faudra impérativement que le VPN Tailscale soit activé, sans quoi la connexion ne pourra pas s’établir.

![Image](assets/fr/077.webp)

Sur le site de Tailscale, maintenant qu’au moins deux clients sont connectés, vous pouvez accéder à la console d’administration avec la liste de tous vos appareils connectés au réseau et leurs adresses IP Tailscale.

![Image](assets/fr/078.webp)

### Connecter Zeus

Installez l’application Zeus sur votre téléphone. À l’ouverture, sélectionnez `Advanced Setup`, puis `Create or connect a wallet`.

![Image](assets/fr/079.webp)

Dans la section `Wallet interface`, choisissez `LND (REST)`. Renseignez ensuite l’adresse Tailscale de votre Umbrel, que vous pouvez retrouver depuis votre tableau de bord Tailscale ou directement dans l’application Tailscale sur Umbrel. Pour le port, indiquez `8080`.

![Image](assets/fr/080.webp)

Zeus vous demande ensuite de fournir un `Macaroon`. Il s’agit d’un jeton d’autorisation permettant de définir précisément les droits accordés à une application (en l’occurrence Zeus) pour interagir avec votre nœud Lightning. Il est possible de générer un macaroon depuis ThunderHub, dans le menu `Tools`, sous-menu `Bakery`, mais pour cet usage, le plus simple est de le récupérer directement depuis l’application `Lightning Node`.

Cliquez sur les trois petits points en haut à droite de l’interface, puis sur `Connect Wallet`. Choisissez `REST (Local Network)`. Vous pourrez alors copier un macaroon disposant des droits appropriés.

![Image](assets/fr/081.webp)

Collez-le dans le champ correspondant dans Zeus, puis cliquez sur le bouton `SAVE WALLET CONFIG`.

![Image](assets/fr/082.webp)

Vous avez maintenant accès à votre nœud Lightning depuis l’application Zeus. Vous pouvez ainsi générer des invoices pour recevoir des paiements directement sur votre nœud Lightning depuis votre smartphone, et également régler des invoices Lightning, où que vous soyez.

![Image](assets/fr/083.webp)

Astuce : Tailscale ne se limite pas à l’utilisation de votre nœud Lightning à distance. Il vous permet d’accéder à l’ensemble des outils de votre Umbrel depuis d’autres logiciels, même à distance. Par exemple, vous pouvez utiliser l’adresse IP Tailscale de votre Umbrel pour connecter votre nœud Bitcoin (via Electrs ou Fulcrum) à Sparrow Wallet, sans passer par Tor. Cela permet d’éviter, une fois de plus, les lenteurs inhérentes à Tor. Il suffit pour cela d'installer le client Tailscale sur votre ordinateur et de le connecter à votre réseau.

https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

Dans le prochain chapitre, nous découvrirons une autre méthode, tout aussi efficace, pour connecter un client mobile à votre nœud Lightning : Nostr Wallet Connect. Nous utiliserons alors une autre application que Zeus (même si Zeus est également compatible avec NWC) à savoir Alby Go.

## Connecter un portefeuille mobile via NWC
<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>

Si la connexion via Tailscale ne vous a pas convaincus, ou si la gestion d’un double VPN vous semble contraignante, je vous propose dans ce chapitre une autre méthode pour utiliser un client mobile à distance afin de payer et recevoir des sats via votre nœud Lightning : ***Nostr Wallet Connect***.

Pour l’exemple, nous utiliserons l’application mobile Alby Go, qui est très bien conçue et particulièrement simple à prendre en main. Cela dit, vous pouvez tout à fait utiliser Zeus ou n’importe quelle autre application mobile compatible avec NWC. Vous trouverez la liste des applications compatibles sur [le dépôt GitHub `awesome-nwc`](https://github.com/getAlby/awesome-nwc).

### Comment fonctionne Nostr Wallet Connect ?

Nostr Wallet Connect est un protocole standardisé qui permet à une application ou un site web de déclencher des actions sur un nœud Lightning distant, sans établir de connexion réseau directe vers ce nœud (pas d’API LND exposée, pas de VPN, pas de service `.onion`...). NWC définit la manière dont une application formule une intention (par exemple `pay_invoice`) et reçoit le résultat.

Son fonctionnement est assez simple. Vous initialisez une session en scannant un QR code ou via un deeplink `nostr+walletconnect:`. Cette chaîne contient les paramètres de session et un secret d’autorisation. Ensuite, lorsque l’application veut payer, elle sérialise la requête, la chiffre, puis la publie sous forme d’événement sur un relais Nostr. Le nœud lit l’événement sur le relais, le déchiffre, vérifie que l’auteur est autorisé pour cette session, exécute le paiement, puis renvoie une réponse chiffrée (succès avec préimage, ou erreur). Le relais ne sert que d’intermédiaire de transport : il ne peut pas lire le contenu, mais il peut éventuellement observer le moment et la fréquence des requêtes.

Par rapport à une connexion via Tailscale ou Tor, l’intérêt principal de NWC est d’éviter toute joignabilité directe de votre nœud depuis l’extérieur. Cela simplifie énormément l’usage en mobilité : votre nœud n’a pas besoin d’accepter des connexions entrantes, il lui suffit de pouvoir communiquer avec un relais. En contrepartie, vous introduisez une dépendance fonctionnelle à des relais Nostr : s’ils sont indisponibles, l’expérience se dégrade. Aussi, même si les messages sont chiffrés, le relais peut observer un certain niveau de métadonnées d’activité.

La différence de modèle de sécurité est également importante. Avec Tailscale ou Tor, vous exposez un accès direct à votre nœud (via l’API de LND) protégé par des secrets très sensibles. C’est puissant, car vous pouvez tout administrer, mais c’est aussi une surface d’attaque plus basse couche. Avec NWC, l’accès est plus applicatif : vous déléguez un jeton de session qui autorise seulement certaines actions.

### Installer Alby Hub sur votre nœud Lightning

Auparavant, il existait une application spécifiquement dédiée aux connexions NWC dans l’App Store d’Umbrel, mais elle n’est malheureusement plus disponible aujourd’hui. Il faut donc désormais passer par Alby Hub pour établir ce type de connexion. Pour cela, commencez par installer l’application Alby Hub directement depuis le store.

![Image](assets/fr/091.webp)

À l’ouverture, passez les écrans d’introduction, puis cliquez sur le bouton `Get Started (LND)`. Il est important de vérifier qu’il est bien indiqué `LND`, et non `LDK`, entre parenthèses. Si `LND` apparaît, cela signifie qu’Alby Hub a correctement détecté votre nœud Lightning existant et va se configurer comme interface pour celui-ci. En revanche, si `LDK` est affiché, cela indique qu’Alby Hub n’a pas détecté votre nœud et s’apprête à en créer un nouveau, ce qui n’est pas l’objectif ici.

![Image](assets/fr/092.webp)

Il vous est ensuite proposé de connecter un compte Alby. Pour un usage limité à NWC, ce n’est pas nécessaire, mais vous pouvez le faire si vous souhaitez profiter des services spécifiques d’Alby. Si ce n’est pas le cas, cliquez sur `Maybe later` pour continuer.

![Image](assets/fr/093.webp)

Choisissez ensuite un mot de passe fort et unique. Celui-ci protège l’accès à Alby Hub sur votre nœud. Pensez à l’enregistrer dans votre gestionnaire de mots de passe.

![Image](assets/fr/094.webp)

Vous arrivez alors sur l’interface d’Alby Hub. Il n’est pas nécessaire de procéder à l’ensemble de la configuration, sauf si vous souhaitez l’utiliser comme gestionnaire principal de votre nœud Lightning. Comme vu précédemment, Alby Hub peut en effet remplacer l’usage de ThunderHub pour l’administration de votre nœud. Si vous souhaitez en savoir plus sur les options d'Alby Hub, consultez notre tutoriel dédié :

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Rendez-vous dans le menu `Connections`.

![Image](assets/fr/095.webp)

Vous pouvez y voir toutes les applications pouvant se connecter à votre nœud Lightning via NWC. Parmi elles figure notamment Zeus, déjà évoquée dans le chapitre précédent. Ici, nous allons utiliser Alby Go. Cliquez donc sur Alby Go, puis sur le bouton `Connect to Alby Go` afin de lancer le processus de connexion.

![Image](assets/fr/096.webp)

### Installer et connecter Alby Go

Sur votre smartphone, installez l’application Alby Go :
- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile) ;
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774) ;
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).

Dans Alby Hub, configurez ensuite les droits que vous souhaitez accorder à l’application Alby Go sur votre nœud Lightning. Vous pouvez par exemple définir des limites de dépenses par période, une date d’expiration pour le lien NWC ou bien laisser un contrôle total. Une fois les paramètres définis, cliquez sur le bouton `Next`.

![Image](assets/fr/097.webp)

Alby Hub génère alors un QR code permettant d’établir la connexion NWC entre votre nœud Lightning et Alby Go.

![Image](assets/fr/098.webp)

Sur l’application Alby Go, lors de la première ouverture, cliquez sur `Connect Wallet`, puis scannez le QR code fourni par Alby Hub.

![Image](assets/fr/099.webp)

Choisissez un nom pour identifier ce wallet. Vous avez désormais accès à votre nœud Lightning à distance via Alby Go. Vous pouvez générer des invoices pour recevoir des sats sur votre nœud, ou régler des invoices Lightning directement avec celui-ci.

![Image](assets/fr/100.webp)

Par exemple, j’ai envoyé 1543 sats depuis l’interface d’Alby Go.

![Image](assets/fr/101.webp)

Si je me rends sur l’interface de base de mon nœud Lightning sur Umbrel, je peux constater que ce paiement a bien été effectué par mon nœud.

![Image](assets/fr/102.webp)

Vous savez dorénavant comment utiliser facilement votre nœud Lightning depuis n'importe quel endroit.

## Pérenniser son autonomie sur Lightning
<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>

Nous arrivons maintenant à la fin de ce cours pratique LNP 202. Vous disposez désormais des bases nécessaires pour utiliser le Lightning Network de manière souveraine : vous comprenez le rôle réel d’un nœud, les compromis des différentes approches, et vous avez mis en place une instance LND sur Umbrel avec une stratégie de sauvegarde et de protection cohérente. Vous avez également ouvert vos premiers canaux, appris à gérer les liquidités, afin de rendre vos paiements fiables au quotidien.

Pour la suite sur le plan opérationnel, votre nœud doit désormais entrer dans un rythme de maintenance. L’essentiel consiste à le surveiller (uptime, synchronisation, état des canaux, échecs de paiements...), à appliquer les mises à jour proposées par Umbrel lorsque des versions stables sont disponibles, et à vérifier périodiquement que vos sauvegardes et votre configuration de watchtower sont toujours actives.

Côté canaux, gardez une approche pragmatique : conservez ceux qui vous rendent service, fermez ceux qui sont durablement inactifs ou associés à des pairs instables, et réallouez progressivement votre capital vers une topologie plus robuste.

**Attention toutefois :** l’un des pièges les plus courants à ce stade consiste à vouloir allouer trop de capital à son nœud Lightning. Gardez à l’esprit que votre nœud Lightning est beaucoup moins sécurisé qu'un hardware wallet, et que la disponibilité des fonds engagés dans vos canaux repose sur des mécanismes de sauvegarde qui restent imparfaits. Il est donc très important de rester sur des montants raisonnables, que vous pouvez vous permettre de perdre en cas de problème, et de toujours conserver la majorité de vos sats avec un hardware wallet on-chain.

Concernant les outils, je vous recommande de rester curieux et attentif aux évolutions et aux nouveautés. Dans cette formation, nous en avons découvert plusieurs, que ce soit pour la gestion de votre nœud, sa connectivité ou l’usage à distance pour effectuer des paiements. Cependant, Lightning est un domaine particulièrement dynamique. Chaque année, de nouveaux outils pertinents voient le jour, et de nombreuses applications apparaissent également sur Umbrel. Se tenir informé de ces nouveautés peut vous permettre de découvrir des solutions plus performantes ou plus pratiques que celles présentées dans ce cours.

Sur le plan pédagogique, si ce n’est pas encore fait, je vous conseille vivement de suivre le cours théorique LNP 201 de Fanis Michalakis, dédié au fonctionnement du Lightning Network. Il vous aidera à mieux comprendre les manipulations réalisées dans ce cours LNP 202 et vous apportera davantage de confiance dans la gestion quotidienne de votre nœud.

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Dans un registre différent, mais tout aussi essentiel dans votre parcours de bitcoiner, je vous recommande également l’excellent cours de Ludovic Lars consacré à l’histoire de la création de Bitcoin.

https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Mais avant de passer à autre chose, vous pouvez donner votre avis sur ce cours LNP 202 et, bien entendu, passer le diplôme afin de valider que vous avez bien assimilé l’ensemble de son contenu.

# Partie finale
<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>

## Avis & Notes
<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>

<isCourseReview>true</isCourseReview>

## Examen final
<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusion
<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
