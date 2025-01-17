---
name: OXT - Chain Analysis
description: Maîtriser les bases de l’analyse de chaîne sur Bitcoin
---
![cover](assets/cover.webp)

***ATTENTION :** Suite à l'arrestation des fondateurs de Samourai Wallet et à la saisie de leurs serveurs le 24 avril dernier, **le site OXT.me n'est actuellement plus accessible**. Cependant, il reste possible que cet outil soit relancé dans les semaines à venir. En attendant, vous pouvez toujours profiter de ce tutoriel pour comprendre les bases de l'analyse de chaîne sur Bitcoin. Toutes les heuristiques et tous les patterns que je vous présente restent applicables aux transactions Bitcoin. Même si ces outils sont moins optimisés que OXT, vous pouvez utilisez provisoirement [Mempool.space](https://mempool.space/) ou bien [Bitcoin Explorer](https://bitcoinexplorer.org/) pour mettre en pratique les notions théoriques de cet article.*

_Nous suivons de près l'évolution de cette affaire ainsi que les développements concernant les outils associés. Soyez assuré que nous mettrons ce tutoriel à jour au fur et à mesure que de nouvelles informations seront disponibles._

_Ce tutoriel est fourni à des fins éducatives et informatives uniquement. Nous ne cautionnons ni n'encourageons l'utilisation de ces outils à des fins criminelles. Il est de la responsabilité de chaque utilisateur de respecter les lois en vigueur dans sa juridiction._

---

Dans cet article, vous allez apprendre les fondements théoriques essentiels à maîtriser pour vous lancer dans des analyses de chaîne basiques sur Bitcoin, et surtout, pour comprendre comment opèrent ceux qui vous observent. Bien que cet article ne constitue pas un tutoriel pratique sur l'outil OXT (sujet que nous aborderons dans un futur tuto), il compile un ensemble de connaissances cruciales pour son utilisation. Pour chaque modèle, métrique et indicateur présenté, un lien vers une transaction exemple sur OXT est fourni, ce qui vous permettra de mieux comprendre son utilisation et de pouvoir pratiquer en parallèle de votre lecture.

## Introduction
Une des fonctions de la monnaie est de résoudre le problème de la double coïncidence des besoins. Dans un système établi sur le troc, la réalisation d'un échange nécessite non seulement de trouver un individu cédant un bien correspondant à mon besoin, mais aussi de lui procurer un bien de valeur équivalente qui satisfait son propre besoin. Trouver cet équilibre s'avère complexe. C'est pourquoi nous recourons à la monnaie qui permet de déplacer la valeur à la fois dans l'espace et dans le temps.

Pour que la monnaie résolve ce problème, il est essentiel que la partie qui fournit un bien ou un service soit convaincue de sa capacité à dépenser cette somme ultérieurement. Ainsi, tout individu rationnel souhaitant accepter une pièce de monnaie, qu'elle soit numérique ou physique, s'assurera qu'elle remplit deux critères fondamentaux :
- La pièce doit être intègre et authentique ;
- et elle ne doit pas être double dépensée.

Si l’on utilise une monnaie physique, c’est la première caractéristique qui est la plus complexe à faire valoir. À différentes périodes de l’histoire, l’intégrité des pièces de métaux a souvent été affectée par des pratiques comme le rognage ou le perçage. Par exemple, durant la Rome antique, il était courant que les citoyens grattent les bords des pièces d’or pour en recueillir un peu de métal précieux, tout en les conservant pour des transactions futures. C’est notamment pour cette raison que l’on a plus tard frappé des cannelures sur la tranche des pièces. L’authenticité est également une caractéristique difficile à vérifier sur un support monétaire physique. De nos jours, les techniques pour lutter contre le faux monnayage sont de plus en plus complexes, obligeant les commerçants à investir dans des systèmes de vérification coûteux.

En revanche, en raison de leur nature, la double dépense n'est pas un problème pour les monnaies physiques. Si je vous cède un billet de 10 €, il quitte irrévocablement ma possession pour entrer dans la vôtre, excluant par là même toute possibilité de dépense multiple des unités monétaires qu’il incarne.

Pour la monnaie numérique, la difficulté est différente. S’assurer de l’authenticité et de l’intégrité d’une pièce est souvent plus simple, mais s’assurer de l'absence de double dépense est plus complexe. Tout bien numérique est en essence de l'information. Contrairement aux biens physiques, l'information ne se divise pas lors des échanges, mais se propage en se multipliant. Par exemple, si je vous transmets un document par courrier électronique, ce dernier se retrouve alors dupliqué. De votre côté, vous ne pouvez pas vérifier avec certitude que j'ai effacé le document original.

Le seul moyen d’éviter cette duplication d’un bien numérique est d’être au courant de l’intégralité des échanges sur le système. De cette manière, on peut savoir qui possède quoi et actualiser les comptes de chacun en fonction des transactions effectuées. C’est ce qui se fait, par exemple, pour la monnaie scripturale. Lorsque l’on paie 10 € à un commerçant par carte bancaire, la banque constate cet échange et actualise le livre des comptes.

Sur Bitcoin, la prévention de la double dépense se fait de la même manière. On va chercher à confirmer l'absence d'une transaction ayant déjà dépensé les pièces en question. Si ces dernières n'ont jamais été utilisées, alors nous pouvons être assurés qu'aucune double dépense n'aura lieu. C’est la fameuse phrase de Satoshi Nakamoto dans le White Paper (livre blanc) : « *Le seul moyen pour confirmer l’absence d’une transaction est d’être au courant de toutes les transactions.* »

Contrairement au modèle bancaire, on ne souhaite pas avoir à faire confiance à une entité centrale sur Bitcoin. Il faut alors que tous les utilisateurs soient en capacité de confirmer cette absence de double dépense, sans pour autant reposer sur un tiers. Ainsi, il faut que chacun soit au courant de toutes les transactions Bitcoin.

C'est précisément cette diffusion publique de l’information qui complique la protection de la vie privée sur Bitcoin. Dans le système bancaire traditionnel, en théorie, seule l'institution financière a connaissance des transactions effectuées. En revanche, sur Bitcoin, l'ensemble des utilisateurs est informé de toutes les transactions, via leurs nœuds respectifs.

À cause de cette contrainte de diffusion, le modèle de confidentialité de Bitcoin diffère de celui du système bancaire. Dans ce dernier, les transactions sont associées à l’identité de l’utilisateur, mais le flux d’information est coupé entre le tiers de confiance et le public. Autrement dit, votre banquier sait que vous achetez votre baguette tous les matins au boulanger du coin, mais votre voisin n’a pas connaissance de toutes ces transactions. Dans le cas de Bitcoin, puisque le flux d’information ne peut pas être cassé entre les transactions et le domaine public, le modèle de confidentialité repose sur la séparation entre l’identité de l’utilisateur et les transactions en elles-mêmes.
![analysis](assets/fr/1.webp)
*Schéma inspiré de celui de Satoshi Nakamoto dans le White Paper : Bitcoin: A Peer-to-Peer Electronic Cash System, partie 10 « Privacy ».*

Puisque les transactions Bitcoin sont rendues publiques, il devient possible d'établir des liens entre elles pour en déduire des renseignements sur les parties impliquées. Cette activité constitue même une spécialité en soi, communément appelée « analyse de chaîne ». Dans cet article, je vous invite à explorer les fondamentaux de l'analyse de chaîne afin de comprendre comment vos bitcoins sont tracés.

La majorité des entreprises spécialisées dans l'analyse de chaîne opèrent comme des boîtes noires, et ne divulguent pas leurs méthodologies. Il est donc difficile d'obtenir des informations sur cette pratique. Pour la rédaction de cet article, je me suis principalement appuyé sur les rares ressources ouvertes disponibles :
- Le plus gros de mon article est extrait de la série de quatre articles nommée : [Understanding Bitcoin Privacy with OXT](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), produite par Samourai Wallet en 2021 ;
- Je me suis également servi des différents rapports d’[OXT Research](https://medium.com/oxt-research), ainsi que de leur outil gratuit d’analyse de chaîne ;
- Plus largement, mes connaissances proviennent des différents tweets et contenus de [@LaurentMT](https://twitter.com/LaurentMT) et de [@ErgoBTC](https://twitter.com/ErgoBTC) ;
- Je me suis aussi inspiré du [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) auquel j’ai participé en compagnie de [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___) et [@LaurentMT](https://twitter.com/LaurentMT).

Je tiens à remercier leurs auteurs, développeurs et producteurs. Sans leurs différents contenus et logiciels, cet article n’existerait pas. Je remercie également les relecteurs qui ont méticuleusement corrigé ce texte et m'ont gratifié de leurs conseils d’experts :
- [Gilles Cadignan](https://twitter.com/gillesCadignan) ;
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).

*Pour information, j’ai ajouté un miniglossaire technique à la fin de l’article pour définir certains termes. Si vous voyez un mot que vous ne comprenez pas avec une étoile, sa définition se trouve en bas de la page.*


## C’est quoi l’analyse de chaîne ?

L’analyse de chaîne est une pratique qui regroupe toutes les méthodes permettant de tracer les flux de bitcoins sur la blockchain. De façon générale, l’analyse de chaîne s’appuie sur l’observation de caractéristiques sur des échantillons de transactions antérieures. Elle consiste ensuite à repérer ces mêmes caractéristiques sur une transaction que l’on souhaite analyser, et à en déduire des interprétations vraisemblables. Cette méthode de résolution de problème à partir d’une approche pratique, pour trouver une solution suffisamment bonne, c’est ce que l’on appelle une heuristique.

Pour vulgariser, l’analyse de chaîne se fait en deux grandes étapes :
1. Le repérage de caractéristiques connues ;
2. La déduction d’hypothèses.

Un des objectifs de l’analyse de chaîne consiste à regrouper diverses activités sur Bitcoin en vue de déterminer l'unicité de l'utilisateur les ayant effectuées. Par la suite, il sera possible de tenter de rattacher ce faisceau d'activités à une identité réelle.

Rappelez-vous de mon introduction. Je vous ai expliqué pourquoi le modèle de confidentialité de Bitcoin reposait originellement sur la séparation entre l’identité de l’utilisateur et ses transactions. Il serait donc tentant de penser que l'analyse de chaîne s'avère inutile, puisque même si l'on parvient à regrouper des activités on-chain, on ne peut pas les associer à une identité réelle. Théoriquement, cette affirmation est exacte. On emploie des paires de clés cryptographiques pour établir des conditions sur les UTXO. Par essence, ces paires de clés ne divulguent aucune information sur l’identité de leurs détenteurs. Ainsi, même si l'on réussit à regrouper les activités associées à différentes paires de clés, cela ne nous renseigne en rien sur l'entité à l'origine de ces activités.

Cependant, la réalité pratique est bien plus complexe. Il existe une multitude de comportements qui risquent de lier une identité réelle à une activité on-chain. En analyse, on appelle cela un point d’entrée, et il en existe une multitude. Le plus courant, c’est évidemment le KYC. Si vous retirez vos bitcoins d’une plateforme régulée vers une de vos adresses de réception personnelles, alors certaines personnes sont en capacité de lier votre identité à cette adresse. Plus largement, un point d’entrée peut être toute forme d’interaction entre votre vie réelle et une transaction Bitcoin. Par exemple, si vous publiez une adresse de réception sur vos réseaux sociaux, cela peut constituer un point d’entrée pour une analyse. Si vous réalisez un paiement en bitcoins à votre boulanger, ce dernier pourra associer votre face (qui fait partie de votre identité) à une adresse Bitcoin.

Ces points d'entrée sont quasiment inévitables dans l'usage de Bitcoin. Bien que l'on puisse chercher à en restreindre la portée, ils demeureront présents. C'est pourquoi il est crucial de combiner les méthodes visant à préserver votre vie privée. Si maintenir une séparation acceptable entre votre identité réelle et vos transactions est une démarche louable, elle demeure insuffisante. En effet, si l'ensemble de vos activités on-chain peut être regroupé, alors le moindre petit point d'entrée est susceptible de compromettre l'unique couche de confidentialité que vous aviez instaurée.

Ainsi, il faut également pouvoir faire face à l’analyse de chaîne dans notre utilisation de Bitcoin. En procédant de la sorte, nous pouvons minimiser l'agrégation de nos activités et limiter l’impact d’un point d’entrée sur notre vie privée. Justement, pour mieux contrecarrer l'analyse de chaîne, quelle meilleure approche que de s'initier aux méthodes employées dans l’analyse de chaîne ? Si vous souhaitez savoir comment améliorer votre confidentialité sur Bitcoin, vous devez comprendre ces méthodes. Cela vous permettra de mieux appréhender les techniques comme [le Coinjoin](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef) ou [le Payjoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), et de réduire les erreurs que vous pourriez faire.

En ça, nous pouvons faire une analogie avec la cryptographie et la cryptanalyse. Un bon cryptographe est avant tout un bon cryptanalyste. Pour imaginer un nouvel algorithme de chiffrement, il faut savoir quelles sont les attaques auxquelles il devra faire face, et également étudier pourquoi les algorithmes précédents ont été cassés. Le même principe s'applique à la confidentialité sur Bitcoin. Comprendre les méthodes de l'analyse de chaîne est la clé pour s'en prémunir. C’est pour cette raison que je vous propose cet article.

Il est primordial de comprendre que l'analyse de chaîne n'est pas une science exacte. Elle repose sur des heuristiques dérivées d'observations antérieures ou d’interprétations logiques. Ces règles permettent d'obtenir des résultats assez fiables, mais jamais d'une précision absolue. En d'autres termes, l'analyse de chaîne implique toujours une dimension de probabilité dans les conclusions émises. On pourra estimer avec plus ou moins de certitude que deux adresses appartiennent à une même entité, mais une certitude totale sera toujours hors de portée.

Tout l’objectif de l'analyse de chaîne réside précisément dans l'agrégation de diverses heuristiques en vue de minimiser le risque d'erreur. Il s'agit en quelque sorte d'une accumulation de preuves qui nous permet de nous approcher davantage de la réalité.

Ces fameuses heuristiques peuvent être regroupées en différentes catégories que nous allons détailler ensemble :
- Les patterns de transaction (ou modèles de transaction) ;
- Les heuristiques internes à la transaction ;
- Les heuristiques externes à la transaction.

Notons que les deux premières heuristiques sur Bitcoin ont été formulées par Satoshi Nakamoto lui-même. Il les expose dans la partie 10 du White Paper (livre blanc). Comme nous le verrons plus loin, il est intéressant d’observer que ces deux heuristiques conservent toujours une prééminence dans l’analyse de chaîne aujourd’hui. Ce sont :
- la CIOH (Common Input Ownership Heuristic) ;
- et la réutilisation d’adresse.

Étudions ensemble les différentes caractéristiques observables et les interprétations que l’on peut en tirer pour réaliser une analyse.

## Les patterns de transactions (ou modèles de transactions)
Un pattern de transaction est simplement un modèle de transaction typique, que l’on peut retrouver sur la blockchain, dont on connaît l’interprétation vraisemblable. Lorsque l’on étudie les patterns, on va s’attarder sur une seule transaction que l’on va analyser à un niveau élevé. En d’autres termes, on va uniquement regarder le nombre d’entrées et le nombre de sorties, sans nous attarder sur ses détails plus spécifiques ou son environnement. À partir du modèle observé, nous pourrons interpréter la nature de la transaction. On va alors rechercher des caractéristiques sur sa structure et en déduire une interprétation.

### L’envoi simple (ou le paiement simple)
Ce modèle se caractérise par la consommation d’un ou plusieurs UTXOs en entrée et la production de deux UTXOs en sortie.

![analysis](assets/fr/2.webp)

L’interprétation de ce modèle est que nous sommes en présence d’une transaction d’envoi ou de paiement. L’utilisateur a consommé ses propres UTXOs en entrée pour satisfaire en sortie un UTXO de paiement et un UTXO de change (rendu de monnaie qui revient vers le même utilisateur). Nous savons donc que l’utilisateur observé n’est vraisemblablement plus en possession d’un des deux UTXOs en sortie (celui du paiement), mais qu’il est toujours en possession de l’autre UTXO (celui de change).

Pour l'instant, il nous est impossible de préciser quelle sortie représente quel UTXO, puisque ce n'est pas l'objectif de ce modèle. Nous y parviendrons en nous appuyant sur les heuristiques que nous étudierons dans la partie suivante. À ce stade, notre objectif se limite à identifier la nature de la transaction en question, qui est, en l'occurrence, un envoi simple.

Par exemple, voici une transaction Bitcoin qui adopte le pattern de l’envoi simple :
[b6cc79f45fd2d7669ff94db5cb14c45f1f879ea0ba4c6e3d16ad53a18c34b769](https://mempool.space/tx/b6cc79f45fd2d7669ff94db5cb14c45f1f879ea0ba4c6e3d16ad53a18c34b769)

### Le balayage (« sweep » en anglais)
Ce modèle se caractérise par la consommation d’un seul UTXO en entrée et la production d’un seul UTXO en sortie.

![analysis](assets/fr/3.webp)

L’interprétation de ce modèle est que nous sommes en présence d’un auto-transfert. L’utilisateur s’est transféré ses bitcoins à lui-même, sur une autre adresse lui appartenant. En effet, puisqu’aucun change n'existe sur la transaction, il est très peu plausible que l’on soit en présence d’un paiement. Nous savons alors que l’utilisateur observé est vraisemblablement encore en possession de cet UTXO.

Par exemple, voici une transaction Bitcoin qui adopte le pattern du balayage :
[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)

Attention, ce type de pattern peut également révéler un auto-transfert sur le compte d’un exchange (plateforme d’échange de cryptomonnaies). Ce seront l’étude des adresses connues et le contexte de la transaction qui nous permettront de savoir si c’est un balayage vers un portefeuille en self-custody (conservation autonome) ou un retrait vers une plateforme.

### La consolidation
Ce modèle se caractérise par la consommation de plusieurs UTXOs en entrée et la production d’un seul UTXO en sortie.

![analysis](assets/fr/4.webp)

L’interprétation de ce modèle est que nous sommes en présence d’une consolidation. C’est une pratique courante chez les utilisateurs de Bitcoin, visant à fusionner plusieurs UTXOs en anticipation d'une éventuelle augmentation des frais de transaction. En effectuant cette opération durant une période où les frais sont bas, il est possible de réaliser des économies sur les frais futurs.

Nous pouvons en déduire que l’utilisateur derrière cette transaction était vraisemblablement en possession de l’intégralité des UTXOs en entrée et qu’il est toujours en possession de l’UTXO en sortie. C’est donc sûrement un auto-transfert.

Tout comme le balayage, ce type de pattern peut également révéler un auto-transfert sur le compte d’un exchange. Ce seront l’étude des adresses connues et le contexte de la transaction qui nous permettront de savoir si c’est une consolidation vers un portefeuille en self-custody ou un retrait vers une plateforme.

Par exemple, voici une transaction Bitcoin qui adopte le pattern de la consolidation :
[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)

### La dépense groupée
Ce modèle se caractérise par la consommation de quelques UTXO en entrée (souvent un seul) et la production de nombreux UTXOs en sortie.

![analysis](assets/fr/5.webp)

L’interprétation de ce modèle est que nous sommes en présence d’une dépense groupée. C’est une pratique qui révèle vraisemblablement une grosse activité économique, comme un exchange par exemple. La dépense groupée permet à ces entités d’économiser des frais en réunissant leurs dépenses dans une seule transaction.

Nous pouvons en déduire que l’UTXO en entrée provient d’une société avec une grosse activité économique et que les UTXOs en sorties vont se disperser. Certains appartiendront à des clients de la société. D’autres iront peut-être vers des sociétés partenaires. Enfin, il y aura certainement un change qui reviendra à la société émettrice.

Par exemple, voici une transaction Bitcoin qui adopte le pattern de la dépense groupée :
[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)

### Les transactions propres à un protocole
Parmi les patterns de transactions, nous pouvons également identifier des modèles qui révèlent l’utilisation d’un protocole spécifique. Par exemple, les coinjoins Whirlpool vont avoir une structure facilement identifiable qui permet de les différencier d'autres transactions classiques.

![analysis](assets/fr/6.webp)

L'analyse de ce pattern suggère que nous sommes vraisemblablement en présence d'une transaction collaborative. Il est aussi possible d'y observer un coinjoin. Si cette dernière hypothèse se révèle exacte, alors le nombre de sorties pourrait nous fournir une estimation approximative du nombre de participants.

Par exemple, voici une transaction Bitcoin qui adopte le pattern de la transaction collaborative de type coinjoin :
[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)

Il existe de nombreux autres protocoles qui disposent de leurs propres structures spécifiques. Ainsi, nous pourrions distinguer des transactions de type Wabisabi ou bien des transactions Stamps par exemple.

## Les heuristiques internes à la transaction
Une heuristique interne est une caractéristique spécifique que l'on identifie au sein même d'une transaction, sans nécessiter l'examen de son environnement, et qui nous permet de réaliser des déductions. Contrairement aux patterns qui se focalisent sur la structure globale de la transaction, les heuristiques internes se fondent sur l'ensemble des données extractibles. Cela inclut :
- Les montants des différents UTXOs en entrée comme en sortie ;
- Tout ce qui touche aux scripts : les adresses de réception, les versionnages, les locktimes…

Généralement, ce type d’heuristique va nous permettre d’identifier le change dans une transaction spécifique. Ce faisant, nous pourrons ensuite perpétuer le traçage d’une entité sur plusieurs transactions différentes.

Une nouvelle fois, je vous rappelle que ces heuristiques ne sont pas d’une précision absolue. Prises individuellement, elles nous permettent uniquement d’identifier des scénarios vraisemblables. C’est l’accumulation de plusieurs heuristiques qui contribue à atténuer l'incertitude, sans toutefois jamais parvenir à l'éliminer totalement.

### Les similitudes internes
Cette heuristique regroupe l’étude des similitudes entre les entrées et les sorties d’une même transaction. Si l’on observe une même caractéristique sur les entrées et sur une seule des sorties de la transaction, alors il est vraisemblable que cette sortie constitue le change.

La caractéristique la plus flagrante est la réutilisation d’une adresse de réception dans une même transaction.

![analysis](assets/fr/7.webp)

Cette heuristique laisse peu de place au doute. À moins qu’il se soit fait pirater sa clé privée, une même adresse de réception révèle forcément l’activité d’un unique utilisateur. L’interprétation qui en découle est que le change de la transaction est la sortie avec la même adresse que l’entrée. On pourra ainsi continuer de tracer l’individu à partir de ce change.

Par exemple, voici une transaction sur laquelle on peut vraisemblablement appliquer cette heuristique :
[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)

Ces similitudes entre les entrées et les sorties ne s’arrêtent pas à la réutilisation d’adresse. Toute ressemblance dans l’utilisation des scripts peut permettre l’application d’une heuristique. Par exemple, on va parfois pouvoir observer le même versionnage entre l’entrée et une des sorties de la transaction.

![analysis](assets/fr/8.webp)

Sur ce schéma, on peut voir que l’input (entrée) n° 0 débloque un script P2WPKH* (SegWit V0 commençant par « bc1q »). L’output (sortie) n° 0 utilise le même type de script. En revanche, l’output n° 1 utilise un script P2TR* (SegWit V1 commençant par « bc1p »). L’interprétation de cette caractéristique est qu’il est vraisemblable que l’adresse avec le même versionnage que l’entrée soit l’adresse de change. Elle appartiendrait donc toujours au même utilisateur.

Voici une transaction sur laquelle on peut vraisemblablement appliquer cette heuristique :
[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)

Sur cette dernière, on peut voir que l’input n° 0 et l’output n° 1 utilisent des scripts P2WPKH* (SegWit V0), alors que l’output n° 0 utilise un script différent de type P2PKH* (Legacy).

### Les paiements par nombres ronds
Une autre heuristique interne qui peut nous permettre d’identifier le change est celle du nombre rond. De manière générale, lorsque l’on se retrouve face à un pattern de paiement simple (1 entrée et 2 sorties), si une des sorties dépense un montant rond, alors celle-ci représente le paiement.

![analysis](assets/fr/9.webp)

Par élimination, si une sortie représente le paiement, l’autre représente le change. On peut donc interpréter qu’il est vraisemblable que l’utilisateur en entrée soit toujours en possession de la sortie identifiée comme étant le change.

Il convient de souligner que cette heuristique n'est pas toujours applicable, puisque la majorité des paiements s'effectuent encore en unités de compte fiduciaires. En effet, lorsqu'un commerçant en France accepte le bitcoin, en général, il n’affiche pas des prix stables en sats. Il optera plutôt pour une conversion entre le prix en euros et le montant en bitcoins à régler. Il ne devrait donc pas y avoir de nombre rond en sortie de la transaction. Néanmoins, un analyste pourrait tenter de réaliser cette conversion en tenant compte du taux de change en vigueur lorsque la transaction a été diffusée sur le réseau.

Si un jour, le bitcoin devient l’unité de compte préférée dans nos échanges, cette heuristique pourrait devenir encore plus utile pour les analyses.

Par exemple, voici une transaction sur laquelle on peut vraisemblablement appliquer cette heuristique :
[2bcb42fab7fba17ac1b176060e7d7d7730a7b807d470815f5034d52e96d2828a](https://mempool.space/tx/2bcb42fab7fba17ac1b176060e7d7d7730a7b807d470815f5034d52e96d2828a)

### La grande sortie
Lorsque l’on repère un écart suffisamment large entre 2 sorties de transactions sur un modèle de paiement simple, on peut estimer que la sortie la plus grande est vraisemblablement le change.

![analysis](assets/fr/10.webp)

Cette heuristique du plus gros output (sortie) est sûrement la plus imprécise de toutes. Si on l’identifie seule, elle est assez faible. Toutefois, cette caractéristique peut être additionnée avec d’autres heuristiques afin de réduire l’incertitude de notre interprétation.

Par exemple, si nous examinons une transaction présentant une sortie avec un montant rond et une autre sortie avec un montant plus important, l'application conjointe de l'heuristique des paiements ronds et de celle concernant la plus grande sortie nous permet de réduire notre niveau d'incertitude.

Par exemple, voici une transaction sur laquelle on peut vraisemblablement appliquer cette heuristique :
[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)

## Les heuristiques externes à la transaction
L’étude des heuristiques externes, c’est l’analyse des similitudes, des patterns et des caractéristiques de certains éléments qui ne sont pas propres à la transaction en elle-même. Autrement dit, si précédemment, nous nous limitions à l'exploitation d'éléments intrinsèques à la transaction avec les heuristiques internes, nous élargissons désormais notre champ d’analyse à l'environnement de la transaction grâce aux heuristiques externes.

### La réutilisation d’adresse
C’est une des heuristiques les plus connues des bitcoiners. La réutilisation d’adresse permet d’établir un lien entre différentes transactions et différents UTXOs. Elle s’observe lorsqu’une adresse de réception Bitcoin est utilisée plusieurs fois.

L’interprétation de la réutilisation d’une adresse est que tous les UTXOs bloqués sur cette adresse appartiennent (ou ont appartenu) à une même entité. Cette heuristique laisse peu de place à l'incertitude. Lorsque l'on parvient à l'identifier, l'interprétation qui en découle a de fortes chances de correspondre à la réalité.

Comme expliqué en introduction, cette heuristique fut découverte par Satoshi Nakamoto lui-même. Dans le White Paper, il évoque justement une solution pour que les utilisateurs évitent de la produire, qui est tout simplement d’utiliser une adresse vierge pour chaque nouvelle transaction : « *En guise de pare-feu additionnel, une nouvelle paire de clés pourrait être utilisée pour chaque transaction afin de les garder non liées à un propriétaire commun.* »

Par exemple, voici une adresse réutilisée sur plusieurs transactions :
[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://mempool.space/address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)

### La similitude des scripts et les empreintes de portefeuilles
Au-delà de la réutilisation d’adresse, il existe de nombreuses autres heuristiques qui permettent de rattacher des actions à un même portefeuille ou à un cluster d’adresses.

Tout d’abord, un analyste peut s’aider des similitudes dans l’utilisation des scripts. Par exemple, certains scripts minoritaires comme du multisig peuvent être plus facilement repérables que des scripts SegWit V0. Au plus le groupe dans lequel nous nous cachons est grand, au plus il est difficile de nous repérer. C’est notamment pour cette raison que sur le protocole de Coinjoin Whirlpool, l’ensemble des participants utilisent exactement le même type de script.

De manière plus globale, un analyste peut également se focaliser sur les empreintes caractéristiques d'un portefeuille. Il s'agit de procédés spécifiques à une utilisation que l'on peut chercher à identifier dans le but de les exploiter comme heuristiques de traçage. Autrement dit, si l’on observe une accumulation des mêmes caractéristiques internes sur des transactions attribuées à l’entité tracée, on peut tenter d’identifier ces mêmes caractéristiques sur d’autres transactions.

Par exemple, on va pouvoir identifier que l’utilisateur tracé envoie systématiquement son change sur des adresses P2TR* (bc1p…). Si ce processus se répète, on pourra l’utiliser comme une heuristique pour la suite de notre analyse. On peut aussi utiliser d’autres empreintes, comme l’ordre des UTXOs, la place du change dans les sorties, la signalisation de RBF (Replace-by-Fee), ou encore, le numéro de version et le locktime.

Comme le précise [@LaurentMT](https://twitter.com/LaurentMT) dans le [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (un podcast francophone), l'utilité des empreintes de portefeuille dans l'analyse de chaîne s'accroît de manière significative avec le temps. En effet, le nombre croissant de types de scripts et le déploiement de plus en plus progressif de ces nouvelles fonctionnalités par les logiciels de portefeuille accentuent les différences. Il arrive même que l'on puisse identifier avec exactitude le logiciel employé par l'entité tracée. Il faut donc comprendre que l’étude de l’empreinte d'un portefeuille s'avère particulièrement pertinente pour les transactions récentes, davantage que pour celles initiées au début des années 2010.

Pour résumer, une empreinte peut être n’importe quelle pratique spécifique, réalisée automatiquement par le portefeuille ou manuellement par l’utilisateur, que l’on pourra retrouver sur d’autres transactions pour nous aider dans notre analyse.

### La CIOH
La CIOH, pour « Common Input Ownership Heuristic », que l'on pourrait traduire en français par « heuristique de propriété commune des entrées » ou « heuristique de co-dépense », est une heuristique stipulant que lorsqu'une transaction comporte plusieurs entrées, ces dernières émanent vraisemblablement toutes d'une entité unique. En conséquence, leur propriété est commune.

Pour appliquer la CIOH, on va d’abord observer une transaction qui dispose de plusieurs entrées. Cela peut être deux entrées, comme 30 entrées. Une fois que cette caractéristique est repérée, on va vérifier si la transaction ne rentre pas dans un pattern connu. Par exemple, si elle comporte 5 entrées avec à peu près le même montant et 5 sorties avec exactement le même montant, on saura que c’est la structure d’un Coinjoin Whirlpool. On ne pourra donc pas appliquer la CIOH.

En revanche, si la transaction ne rentre dans aucun pattern connu de transaction collaborative, alors on peut interpréter que toutes les entrées proviennent vraisemblablement de la même entité. Cela peut être très utile pour élargir un cluster déjà connu ou pour perpétuer un traçage.

![analysis](assets/fr/11.webp)

La CIOH a été découverte par Satoshi Nakamoto. Il en parle dans la partie 10 du White Paper (livre blanc) : « *[...] le lien est inévitable avec les transactions à plusieurs entrées, qui révèlent nécessairement que leurs entrées étaient détenues par un même propriétaire. Le risque est que si le propriétaire d'une clé est révélé, les liens peuvent révéler d'autres transactions qui ont appartenu au même propriétaire.* »

Il est particulièrement fascinant de constater que Satoshi Nakamoto, avant même le lancement officiel de Bitcoin, avait déjà identifié les deux principales vulnérabilités en matière de confidentialité pour les utilisateurs, à savoir la CIOH et la réutilisation d'adresse. Une telle clairvoyance est assez remarquable, car ces deux heuristiques demeurent, encore aujourd’hui, les plus utiles dans l'analyse de chaîne.

### Les données off-chain
Évidemment, l’analyse de chaîne ne se limite pas à des données on-chain. Toute donnée issue d'une analyse antérieure ou accessible sur Internet peut également être utilisée pour affiner une analyse.

Par exemple, si l'on observe que les transactions tracées sont systématiquement diffusées depuis le même nœud Bitcoin et que l'on parvient à identifier son adresse IP, il est possible que l'on puisse repérer d'autres transactions de la même entité.

L'analyste a aussi la possibilité de s’appuyer sur des analyses préalablement rendues open-source, ou bien sur ses propres analyses antérieures. Peut-être que l’on va pouvoir trouver une sortie qui pointe vers un cluster d’adresses que l’on avait déjà identifiées. Parfois, il est aussi possible de s'appuyer sur des sorties qui pointent vers un exchange, les adresses de ces plateformes étant généralement connues.

De la même manière, on peut réaliser une analyse par élimination. Par exemple, si lors de l'analyse d'une transaction comportant deux sorties, l'une d'elles se rattache à un cluster d'adresses déjà connu, mais distinct de l'entité que l'on trace, alors on peut interpréter que l'autre sortie représente vraisemblablement le change.

L’analyse de chaîne inclut aussi une partie d’OSINT (Open Source Intelligence) un peu plus généraliste avec des recherches sur internet. C’est pour cette raison que l’on déconseille de publier des adresses de réception directement sur les réseaux sociaux ou sur un site web, que ce soit sous pseudo ou non.

### Les modèles temporels
On y pense moins, mais certains comportements humains sont reconnaissables on-chain. Celui qui est le plus utile dans une étude, c’est votre rythme de sommeil ! Et oui, lorsque vous dormez, à priori, vous ne diffusez pas de transactions Bitcoin. Or, vous dormez généralement à peu près aux mêmes horaires. Il est donc courant d’utiliser des analyses temporelles dans l’analyse on-chain. Il s'agit tout simplement du recensement des heures auxquelles les transactions d'une entité donnée sont diffusées au réseau Bitcoin. L’analyse de ces patterns temporels nous permet de déduire de nombreuses informations.

Tout d’abord, une analyse temporelle permet parfois d’identifier la nature de l’entité tracée. Si l’on observe que les transactions sont diffusées de manière constante sur 24 heures, alors cela va trahir une forte activité économique. L’entité derrière ces transactions est vraisemblablement une entreprise, potentiellement internationale et peut-être avec des procédures automatisées en interne.

Par exemple, j’avais reconnu ce pattern il y a quelques semaines en analysant la transaction qui avait par erreur alloué 19 bitcoins de frais. Une simple analyse temporelle m’avait permis d'émettre l’hypothèse que l’on avait affaire à un service automatisé, et donc vraisemblablement à une grosse entité de type exchange : https://twitter.com/Loic_Pandul/status/1701127409712452072

Effectivement, quelques jours plus tard, on a découvert que les fonds appartenaient à PayPal, via l’exchange Paxos.

Au contraire, si l’on voit que le pattern temporel est plutôt réparti sur 16 heures bien spécifiques, alors on peut estimer que l’on a affaire à un utilisateur individuel, ou peut-être à une entreprise locale en fonction des volumes échangés.

Au-delà de la nature de l’entité observée, le pattern temporel peut également nous indiquer approximativement la localisation de l’utilisateur. On pourra ainsi rapprocher d’autres transactions, et utiliser l’horodatage de celles-ci comme une heuristique supplémentaire pouvant s’ajouter à notre analyse.

Par exemple, sur l'adresse réutilisée plusieurs fois dont je vous ai préalablement parlé, on peut observer que les transactions, qu'elles soient entrantes ou sortantes, se concentrent sur un intervalle de 13 heures.
![analysis](assets/notext/12.webp)
*Crédit : OXT*

Cet intervalle correspond vraisemblablement à l’Europe, à l’Afrique ou au Moyen-Orient. On peut donc interpréter que l’utilisateur derrière ces transactions habite par là.

Dans un registre différent, c'est également une analyse temporelle de ce type qui a permis de formuler l'hypothèse selon laquelle Satoshi Nakamoto n’opérait pas depuis le Japon, mais bien depuis les États-Unis : [https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f)

### L’analyse des volumes
Une autre heuristique externe qui peut être utilisée est l’analyse des volumes échangés. En fonction des montants présents dans chaque transaction attribuée à une entité, on va pouvoir utiliser cette information comme une heuristique supplémentaire pour le reste de l’analyse.

Cette heuristique est évidemment assez faible, mais elle peut permettre de réduire l’incertitude en l’additionnant à d’autres heuristiques.

## Comment se protéger face à l’analyse de chaîne ?
En tant qu'utilisateur de Bitcoin, vous avez le droit de protéger votre vie privée. Cela découle de vos droits naturels de posséder et de disposer de vous-même, qui sont inhérents à chaque individu, indépendamment de toute contrainte législative.

Ce droit naturel de protéger sa vie privée est d'ailleurs détourné dans un droit-créance, consacré par l'article 12 de la Déclaration universelle des droits de l'homme, stipulant que « *Nul ne sera l'objet d'immixtions arbitraires dans sa vie privée, sa famille, son domicile ou sa correspondance, ni d'atteintes à son honneur et à sa réputation. Toute personne a droit à la protection de la loi contre de telles immixtions ou de telles atteintes.* ».

Or, le cœur de métier des entreprises spécialisées en analyse de chaîne consiste précisément à s'ingérer dans votre sphère privée, compromettant ainsi la confidentialité de votre correspondance. Alors qu'on pourrait espérer que, conformément au droit-créance susmentionné, les États défendent avec vigueur notre vie privée, non seulement ils négligent de le faire, mais ils alimentent même substantiellement le financement de ces entreprises d'analyse. Il serait également vain d'espérer l’appui de la part des associations du secteur, qui semblent disposées à toutes les concessions face au législateur.

De facto, ce droit-créance à la vie privée sur Bitcoin n’existe pas. Il vous revient donc à vous, utilisateur, de faire valoir votre droit naturel et de protéger la confidentialité de votre correspondance. Cela implique l'adoption de diverses techniques et pratiques d'utilisation, qui vous permettront d’empêcher ou de tromper les heuristiques utilisées pour l’analyse de chaîne.

### Éviter de rentrer dans les heuristiques
Tout d’abord, avant d’envisager des méthodes plus radicales, il convient de limiter au maximum notre exposition aux heuristiques utilisées pour l’analyse de chaîne. Nous l’avons dit précédemment, les deux heuristiques les plus puissantes sont la réutilisation d’adresse et la CIOH.

Le principe de base pour garantir votre vie privée sur Bitcoin réside dans l'utilisation d'une nouvelle adresse vierge pour chaque transaction entrante en direction de votre portefeuille. La réutilisation d'adresse constitue véritablement la menace principale à la confidentialité sur Bitcoin.

Pour un utilisateur individuel, générer une nouvelle adresse pour chaque paiement entrant s'avère être très simple. Les bons portefeuilles modernes le font automatiquement dès lors que vous cliquez sur « Recevoir ». Alors, si vous accordez ne serait-ce qu'une infime importance à la confidentialité de vos transactions, l'utilisation d'adresses vierges représente le strict minimum. Si jamais vous avez besoin d’un point de contact statique sur internet, au lieu de mettre une adresse de réception, vous pouvez utiliser des solutions [comme PayNym qui implémentent le BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).

Ensuite, si vous souhaitez agir face à la CIOH, évitez de fusionner des UTXOs en entrée de transaction. Au minimum, si vous devez vraiment fusionner, privilégiez des UTXOs qui ont la même source. Cette recommandation implique d’avoir une bonne gestion de ses UTXOs. Lors de l’achat de vos bitcoins, privilégiez des transferts impliquant de gros montants pour maximiser le nombre de paiements que vous pourrez effectuer sans avoir à fusionner. Je vous conseille également d'étiqueter vos UTXOs dans votre logiciel afin d'en identifier la provenance et d'éviter la fusion de sources distinctes.

Plus largement, pour toutes les autres heuristiques, il faut les connaître pour essayer de ne pas tomber dedans :
- N’utilisez pas de scripts minoritaires. Préférez du SegWit V0 ou éventuellement du SegWit V1 ;
- Ne faites pas des paiements par nombre rond. Par exemple, si vous devez envoyer 100k sats à un ami, envoyez-lui 114 486 sats. Il vous paiera à boire en échange ;
- Essayez de ne pas toujours avoir un change qui soit bien plus gros que la sortie de paiement ;
- Ne publiez pas vos adresses de réception sur les réseaux sociaux ;
- Utilisez votre propre nœud sous Tor pour diffuser vos transactions ;
- Essayez de ne pas toujours diffuser vos transactions Bitcoin à la même heure…

### Utiliser des outils de confidentialité
Vous pouvez également vous tourner vers des méthodes qui permettent de rendre ambigüe votre utilisation de Bitcoin afin d’empêcher ou de tromper l’analyse de chaîne.

La technique la plus populaire est sûrement le Coinjoin, une structure de transaction collaborative qui mobilise plusieurs UTXOs de mêmes montants. L’objectif ici est de rompre les liens déterministes, empêchant ainsi les analyses du présent vers le passé et du passé vers le présent. Le Coinjoin permet de produire du déni plausible en cachant vos pièces au sein d’un grand groupe de pièces indifférenciables. Si vous souhaitez en savoir plus sur le Coinjoin, tant sur le plan technique que pratique, je vous suggère de lire ces autres articles et tutoriels :
- [COINJOIN - SAMOURAI WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef) ;
- [COINJOIN - SPARROW WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b) ;
- [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).

![analysis](assets/fr/13.webp)

Le CoinJoin est un excellent outil pour produire du déni plausible sur des pièces, mais il n’est pas optimisé pour tous les besoins de l’utilisateur en termes de confidentialité. Typiquement, le CoinJoin n’a pas été pensé pour devenir un outil de paiement. Il est très rigide sur les montants échangés afin de perfectionner la production de déni plausible. Puisque l’on ne peut pas choisir librement le montant des sorties de transaction, alors on ne peut pas utiliser le CoinJoin pour payer en bitcoins.

Par exemple, imaginons que je souhaite payer ma baguette en bitcoins tout en optimisant ma confidentialité. Étant donné l'impossibilité de sélectionner le montant de l'UTXO résultant du CoinJoin, je me trouverais dans l'incapacité d'ajuster le montant de ma dépense au tarif fixé par le boulanger. De ce fait, le CoinJoin se révèle inadéquat pour des transactions de paiement.

D’autres outils ont ainsi été imaginés pour répondre à des besoins de confidentialité dans des cas d’utilisation plus spécifiques. Par exemple, nous avons le [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), une sorte de mini-CoinJoin, impliquant uniquement deux participants et reposant sur une structure qui permet un paiement.

La particularité du PayJoin réside dans sa capacité à produire une transaction qui semble ordinaire, alors qu'elle constitue en réalité un mini-CoinJoin entre deux utilisateurs. Dans cette structure, le destinataire de la transaction intervient parmi les entrées aux côtés de l'expéditeur réel. Ainsi, le destinataire insère un paiement vers lui-même au sein de la transaction qui permet le paiement réel.

Par exemple, si vous achetez une baguette à votre boulanger pour 6 000 sats à partir d’un UTXO de 10 000 sats, et que vous souhaitez faire un PayJoin, votre boulanger va ajouter en entrée de votre transaction originelle un UTXO de 15 000 sats qui lui appartient, qu’il va récupérer en intégralité en sortie, afin de tromper les heuristiques :

![analysis](assets/fr/14.webp)

Les frais de transaction sont négligés afin de faciliter la compréhension du schéma.

Les objectifs du PayJoin sont doubles. Tout d'abord, il vise à tromper un observateur extérieur en produisant un leurre grâce à la CIOH. En effet, lorsqu'un analyste observe cette transaction, il va penser qu’il peut appliquer la CIOH, et ainsi présumer une propriété commune des différentes entrées. En réalité, cette supposition est erronée, car une entrée appartient à l'émetteur, tandis que l'autre est la propriété du destinataire. Le PayJoin a donc pour effet de corrompre l'analyse de chaîne, en orientant l'analyste sur un chemin qui se révèle être le mauvais.

Le second objectif du PayJoin est de tromper l'analyste sur le montant réel de la transaction, grâce à la structure spécifique de ses sorties. Le PayJoin s'inscrit ainsi dans le champ de la stéganographie. Il permet de dissimuler le montant réel de la transaction au sein d'une transaction trompeuse.

Effectivement, si l’on reprend notre exemple du PayJoin pour acheter une baguette, un observateur extérieur va penser que l’on a affaire à un paiement de 4 000 sats ou de 21 000 sats. En réalité, le paiement pour la baguette est de 6 000 sats : 21 000 - 15 000 = 6 000. La valeur réelle du paiement est donc cachée au sein d’un faux paiement qui agit comme un leurre pour l’analyse de chaîne.

Au-delà du PayJoin et du CoinJoin, il existe de nombreuses autres structures de transactions Bitcoin qui permettent soit de bloquer l’analyse de chaîne, soit de la tromper. Parmi celles-ci, je pourrais citer les transactions [Stonewall](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) et [StonewallX2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b), qui permettent soit de faire un mini Coinjoin flexible, soit d’imiter un mini Coinjoin flexible. Il y a également les transactions [Ricochet](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589) qui permettent de simuler un changement de propriétaire des bitcoins en réalisant une multitude de faux transferts vers soi-même.

Tous ces outils sont disponibles sur les portefeuilles Samourai Wallet sur mobile, et Sparrow Wallet sur PC. Si vous souhaitez en savoir plus sur ces structures de transaction spécifiques, je vous conseille de découvrir mes tutoriels :
- [PAYJOIN](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f) ;
- [PAYJOIN - SAMOURAI WALLET](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab) ;
- [PAYJOIN - SPARROW WALLET](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62) ;
- [STONEWALL](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) ;
- [STONEWALL X2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b) ;
- [RICOCHET](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

## Conclusion
L’analyse de chaîne est une pratique qui consiste à essayer de tracer les flux de bitcoins on-chain. Pour ce faire, les analystes cherchent des patterns et des caractéristiques afin de conclure des hypothèses et des interprétations plus ou moins vraisemblables.

L'exactitude de ces heuristiques varie : certaines procurent un degré de certitude plus élevé que d'autres, mais aucune ne saurait prétendre à l'infaillibilité. L’accumulation de plusieurs heuristiques convergentes peut toutefois atténuer ce doute inhérent, bien qu'il demeure impossible de l'annihiler.

Nous pouvons regrouper ces méthodes en trois grandes catégories distinctes :
- Les patterns, axés sur la structure globale de chaque transaction ;
- Les heuristiques internes, qui permettent l'examen exhaustif de tous les détails d'une transaction, sans toutefois s'étendre à son contexte ;
- Les heuristiques externes, qui englobent l'analyse de la transaction dans son environnement, ainsi que toute donnée externe susceptible d'apporter un éclairage.

En tant qu'utilisateur de Bitcoin, il est indispensable de s'approprier les principes fondamentaux de l'analyse de chaîne pour être en mesure de la contrer efficacement, et ainsi de protéger sa vie privée.

## Miniglossaire technique :
**P2PKH :** sigle pour Pay to Public Key Hash (« payer au hachage d’une clé publique »). C’est un modèle de script standard utilisé pour établir des conditions de dépenses sur un UTXO. Il permet de bloquer des bitcoins sur un hachage d’une clé publique, c’est-à-dire sur une adresse de réception. Ce script est associé au standard Legacy, et a été introduit dès les premières versions de Bitcoin par Satoshi Nakamoto. À la différence du P2PK, où la clé publique est explicitement incluse dans le script, le P2PKH utilise une empreinte cryptographique de la clé publique, avec quelques métadonnées, également nommée « adresse de réception ». Ce script inclut le hachage RIPEMD160 du SHA256 de la clé publique et stipule que, pour accéder aux fonds, le destinataire doit fournir une clé publique correspondant à ce hachage, ainsi qu'une signature numérique valide générée à partir de la clé privée associée. Les adresses P2PKH sont encodées en utilisant le format Base58Check, qui leur confère une résistance face aux erreurs typographiques grâce à l'utilisation d'une somme de contrôle. Ces adresses débutent systématiquement par le chiffre 1.

**P2TR :** sigle pour Pay to Taproot (« payer à la racine »). C’est un modèle de script standard utilisé pour établir des conditions de dépenses sur un UTXO. P2TR a été introduit avec l'implémentation de Taproot en novembre 2021. Il utilise le protocole de Schnorr pour agréger des clés cryptographiques, ainsi que des arbres de Merkle pour des scripts alternatifs, connus sous le nom de MAST (Merkelized Alternative Script Tree). Contrairement aux transactions traditionnelles où les conditions de dépense sont exposées publiquement (parfois à la réception, parfois à la dépense), P2TR permet de masquer des scripts complexes derrière une seule clé publique apparente. Techniquement, un script P2TR verrouille des bitcoins sur une clé publique Schnorr unique, dénommée K. Cependant, cette clé K est en réalité un agrégat d'une clé publique P et d'une clé publique M, cette dernière étant calculée à partir de la racine de Merkle d'une liste de ScriptPubKeys. L'agrégation de clés est réalisée à l'aide du protocole de signature de Schnorr. Les bitcoins verrouillés avec un script P2TR peuvent être dépensés de deux manières distinctes : soit en publiant une signature pour la clé publique P, soit en satisfaisant l'un des scripts contenus dans l'arbre de Merkle. La première option est appelée « key path » (chemin de clé) et la seconde « script path » (chemin de script). Ainsi, P2TR permet aux utilisateurs d'envoyer des bitcoins soit à une clé publique, soit à plusieurs scripts de leur choix. Un autre avantage de ce script est que, bien qu'il y ait de multiples façons de dépenser une sortie P2TR, seule celle qui est utilisée doit être révélée à la dépense, permettant ainsi aux alternatives inutilisées de rester privées. Par exemple, grâce à l'agrégation des clés Schnorr, la clé publique P peut elle-même être une clé agrégée, représentant éventuellement un multisig. P2TR est une sortie SegWit de version 1, ce qui signifie que les signatures pour les entrées P2TR sont stockées dans le témoin d'une transaction, et non dans le ScriptSig. Les adresses P2TR utilisent un encodage Bech32m et commencent par bc1p.

**P2WPKH :** sigle pour Pay to Witness Public Key Hash (« payer au témoin du hachage de la clé publique »). C’est un modèle de script standard utilisé pour établir des conditions de dépenses sur un UTXO. P2WPKH a été introduit avec l'implémentation de SegWit en août 2017. Ce script est similaire à P2PKH (Pay to Public Key Hash), en ce sens qu'il verrouille également des bitcoins sur la base du hachage d'une clé publique, c’est-à-dire d’une adresse de réception. La différence réside dans la manière dont les signatures et les scripts sont inclus dans la transaction. Dans le cadre de P2WPKH, les informations du script de signature (ScriptSig) sont déplacées de la structure traditionnelle de la transaction vers une section distincte appelée Witness (témoin). Ce déplacement est une caractéristique de la mise à jour SegWit (Segragated Witness). Cette technique présente l'avantage de réduire la taille des données de transaction dans le corps principal, tout en conservant les informations de script nécessaires à la validation dans une section séparée. Par conséquent, les transactions P2WPKH sont généralement moins coûteuses en termes de frais par rapport aux transactions Legacy. Les adresses P2WPKH sont écrites en utilisant l'encodage Bech32, ce qui contribue à une écriture plus concise et moins sujette aux erreurs typographiques grâce à la somme de contrôle sous forme de code BCH. Ces adresses commencent toujours par bc1q, ce qui permet de les distinguer facilement des adresses de réception Legacy. P2WPKH est une sortie SegWit de version 0.

**UTXO :** Sigle de Unspent Transaction Output. Un UTXO est une sortie de transaction qui n'a pas encore été dépensée ou utilisée comme entrée pour une nouvelle transaction. Les UTXOs représentent la fraction de bitcoins que possède un utilisateur et qui sont actuellement disponibles pour être dépensés. Chaque UTXO est associé à un script de sortie spécifique, qui définit les conditions nécessaires pour dépenser les bitcoins. Les transactions dans Bitcoin consomment ces UTXOs en entrées (inputs) et créent de nouveaux UTXOs en sorties (outputs). Le modèle d'UTXO est fondamental sur Bitcoin, car il permet de vérifier facilement que les transactions n'essaient pas de dépenser des bitcoins qui n'existent pas ou qui ont déjà été dépensés. En gros, un UTXO c’est un morceau de Bitcoin.






