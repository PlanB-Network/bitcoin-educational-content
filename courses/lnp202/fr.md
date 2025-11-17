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

Il est aujourd’hui possible d'avoir une expérience utilisateur très proche de celle d’un portefeuille Lightning custodial, tout en restant en self-custody. L’objectif de ce chapitre est justement de vous aider à choisir la voie la plus adaptée à votre profil.

### Option 1 : ne pas utiliser Lightning directement

La première solution consiste tout simplement à ne pas utiliser Lightning de manière native, mais à passer par un portefeuille Bitcoin ou Liquid qui embarque des swaps atomiques. C’est par exemple le cas des applications Aqua ou Bull Bitcoin Wallet, qui permettent de payer des invoices Lightning sans exploiter vous-même un nœud Lightning, mais tout en restant en self-custody.

Le principe est le suivant : vos fonds restent en Bitcoin onchain ou sur Liquid, dans un portefeuille dont vous détenez les clés de manière classique. Lorsque vous scannez une invoice Lightning, le portefeuille envoie une transaction (onchain ou Liquid) vers un service de swap atomique. Ce service se charge ensuite de réaliser le paiement Lightning depuis son propre nœud, en échange de vos bitcoins reçus onchain ou via Liquid. En pratique, vous n’avez donc pas de canaux Lightning à gérer, mais vous pouvez tout de même régler des invoices Lightning.

13

L’avantage majeur de cette approche, par rapport à un portefeuille Lightning custodial classique, est que vous restez en possession de vos fonds à 100 % à chaque instant. Les bitcoins sont dans votre portefeuille onchain ou Liquid, avec votre propre phrase mnémonique. Même pendant le swap, vous restez en possession de vos fonds, car le swap est atomique. Il repose sur un mécanisme cryptographique qui garantit qu’il n’existe que deux issues possibles : soit le swap réussit entièrement, soit il échoue et le service ne peut pas s’approprier vos fonds.

La plupart des portefeuilles qui proposent ce type de fonctionnalité s’appuient sur [Boltz](https://boltz.exchange/) pour la partie technique du swap.

Cette solution présente aussi des avantages intéressants en termes de confidentialité, surtout lorsqu’elle est couplée à Liquid. Pour un débutant, c’est également très simple à mettre en place et à sauvegarder : une phrase mnémonique classique, pas de canaux, pas de liquidité à équilibrer...

En revanche, cette approche a des limites. D’abord, elle n’est pas incensurable : vous dépendez de la disponibilité et de la bonne volonté du service de swap. Si celui-ci ne veut plus traiter votre compte, ou cesse d’opérer, vous ne pouvez plus payer d'invoices Lightning par son intermédiaire. Ensuite, il existe des frais non négligeables : vous payez à la fois les frais de transaction onchain ou Liquid, et la commission du service de swap. Aussi, en cas de forte augmentation des frais onchain, cela peut devenir très cher d'utiliser Lightning.

Donc pour un usage ponctuel, cela reste acceptable, mais pour un utilisateur très actif sur Lightning, il vaut mieux faire les choses comme il faut avec un vrai nœud Lightning.

### Option 2 : les nœuds Lightning embarqués

La deuxième catégorie de solutions repose sur les nœuds Lightning embarqués directement dans une application mobile. Phoenix Wallet a été le pionnier de ce modèle et reste une référence. Aujourd’hui, d’autres projets proposent des approches comparables, comme Zeus (en mode embedded) ou BitKit.

L’idée est simple : l’application exécute en réalité un nœud Lightning, mais toutes les opérations complexes sont gérées automatiquement en arrière-plan. Vous disposez d’une interface de "wallet Lightning" avec une phrase mnémonique pour la sauvegarde, vous voyez un solde et vous payez des invoices, mais vous ne gérez ni canaux, ni liquidité, ni la plupart des paramètres.

014

Ces solutions sont toujours self-custodial. Les clés qui contrôlent les fonds sont générées et stockées sur votre téléphone, et la sauvegarde passe par une seed ou un mécanisme équivalent. Vous n’êtes pas simplement titulaire d’un compte chez un prestataire, vous possédez réellement des bitcoins verrouillés dans des canaux qui vous appartiennent et ne peuvent pas vous être volés.

Les avantages des nœuds LN embarqués sont nombreux :
* installation et prise en main extrêmement simples ;
* expérience utilisateur proche d’un wallet Lightning custodial, mais tout en étant en self-custody ;
* pas de gestion manuelle des canaux ou de la liquidité ;
* sauvegarde relativement simple.

Mais ces portefeuilles embarqués ont aussi des limites importantes. D’abord, sur le plan de la confidentialité, l’opérateur du service (par exemple ACINQ dans le cas de Phoenix) dispose d’une vision assez fine des flux qui transitent par votre nœud : montants, fréquences, destinataires, même si c'est amené à s'améliorer, notamment avec l'adoption progressive des *Trampoline Nodes*. Ensuite, vous êtes fortement dépendant de cet opérateur comme pair Lightning principal. Si le nœud d’ACINQ devient indisponible (dans le cas de Phoenix), si l’entreprise subit des pressions réglementaires ou change son modèle économique, votre expérience utilisateur peut être fortement dégradée, voire compromise.

Enfin, cette simplicité a un prix. Les services de nœuds LN embarqués facturent généralement des frais spécifiques sur les dépôts, les retraits ou certaines opérations de gestion de canaux. Ce modèle reste cohérent au regard du service offert selon moi, mais pour un usage intensif, il peut se révéler beaucoup plus coûteux qu’un nœud Lightning classique bien géré.

### Option 3 : le nœud Lightning classique

La troisième solution, celle que nous allons approfondir dans ce cours LNP 202, consiste à exploiter un nœud Lightning classique sur un serveur ou un appareil dédié.

Par "classique" j'entends que vous installez et configurez vous-même une implémentation Lightning (par exemple LND) au-dessus de votre propre nœud Bitcoin. Vous choisissez vos pairs, vous ouvrez vos canaux, vous gérez votre liquidité entrante et sortante, et vous définissez vos politiques de frais de routage.

Sur le plan de la souveraineté, c’est la meilleure solution. Vous ne dépendez plus d’une entreprise spécifique pour vos canaux ou vos paiements : si un pair vous censure ou ferme un canal, vous pouvez en ouvrir un autre avec un nœud différent. Si un service disparaît, vos sats restent dans les canaux que vous contrôlez, et vous pouvez les rapatrier onchain. Vous avez également la possibilité d’optimiser vos coûts à long terme : une fois vos canaux correctement dimensionnés et gérés, le coût global des paiements peut devenir très faible.

En termes de confidentialité, vous êtes évidemment soumis aux limites du modèle de Lightning lui-même, mais vous ne livrez pas l’intégralité de votre activité à un opérateur unique.

En revanche, mettre en place un nœud Lightning classique est évidemment plus complexe : il faut installer, configurer, maintenir, surveiller les mises à jour, comprendre la logique des canaux et des politiques de frais, gérer les canaux et les liquidités, etc. Une mauvaise configuration, une sauvegarde négligée ou une gestion imprudente peuvent conduire plus facilement à la perte de sats. Le nœud doit également tourner en permanence.

C’est précisément ce chemin que je vous propose de suivre dans ce cours, en vous accompagnant dans chaque étape pour limiter les risques et structurer votre approche.

### Quelle solution pour quel profil d’utilisateur ?

Pour choisir la solution adaptée à votre profil d'utilisateur Lightning, il faut vous situer sur deux axes : votre fréquence d’utilisation de Lightning et votre appétence pour la gestion technique.

Vous réalisez peu de paiements Lightning, de manière ponctuelle, mais vous souhaitez tout de même pouvoir régler des invoices LN depuis votre téléphone de temps en temps, sans renoncer à la self-custody : un portefeuille Bitcoin ou Liquid avec fonctionnalité de swap est probablement la meilleure option. Vous restez propriétaire de vos fonds, vous ne gérez pas de nœud, et vous acceptez des frais un peu plus élevés en échange de la simplicité.

https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Vous utilisez Lightning assez régulièrement et vous souhaitez bénéficier des avantages d’un véritable nœud, sans pour autant passer du temps sur la gestion des canaux, des frais ou de l’infrastructure : un nœud Lightning embarqué sur mobile est une bonne solution. Vous conservez la garde de vos fonds, l’UX reste très accessible, et toute la complexité est cachée, au prix d’une dépendance marquée à un opérateur.

https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Vous êtes un utilisateur intermédiaire ou avancé, prêt à investir du temps pour comprendre et piloter votre infrastructure, et vous tenez à disposer d’un maximum de contrôle sur vos canaux, votre liquidité et vos frais : un nœud Lightning classique sur serveur est la meilleure voie. C’est la solution la plus exigeante, mais aussi la plus cohérente avec l’idée de souveraineté.


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





