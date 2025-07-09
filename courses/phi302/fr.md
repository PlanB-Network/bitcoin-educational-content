---
name: Philosophie de développement Bitcoin
goal: Développer une compréhension philosophique profonde des principes de conception de Bitcoin.
objectives: 

  - Analyser les compromis fondamentaux et les décisions architecturales de Bitcoin
  - Apprendre à évaluer les changements et innovations proposés pour le protocole Bitcoin
  - Synthèse de plus d'une décennie d'histoire du développement de Bitcoin et de débats au sein de la communauté
  - Appliquer des cadres de réflexion critique lors de l'évaluation de nouveaux PIF


---

# Plongée dans la philosophie du développement Bitcoin



La philosophie de développement du Bitcoin est un cours destiné aux développeurs Bitcoin qui comprennent déjà les bases des concepts et processus tels que le Proof-of-Work, la construction de blocs et le cycle de vie des transactions, et qui souhaitent passer à un niveau supérieur en acquérant une compréhension plus approfondie des compromis et de la philosophie de conception du Bitcoin.

Il devrait aider les nouveaux développeurs à assimiler les principales leçons tirées de plus d'une décennie de développement du Bitcoin et de débat public, tout en leur fournissant un contexte utile pour évaluer les nouvelles idées (les bonnes comme les mauvaises !).


### À quoi s'attendre ?


Comme indiqué ci-dessus, il s'agit d'un guide pratique destiné aux développeurs Bitcoin. Cependant, Bitcoin est un sujet vaste et complexe et nous ne pourrions pas en couvrir tous les aspects ici. Avec ce cours, nous espérons discuter des caractéristiques nécessaires pour démarrer votre activité de développement et vous permettre de l'explorer davantage par vous-même.


De nombreuses personnes sont impliquées dans le projet Bitcoin ; comme certaines d'entre elles ont des opinions opposées, vous pouvez trouver ici des ressources qui expriment des idées contradictoires. Cependant, nous nous efforçons toujours de rester dans le domaine des faits, où les opinions n'ont pas d'importance.


### Qui a écrit cela ?


Ce cours est adapté du livre éponyme dont l'auteur principal est Kalle Rosenbaum, et Linnéa Rosenbaum y a contribué en tant que co-auteur.

Ce livre a été commandé et financé par [Chaincode Labs] (https://learning.chaincode.com/), un centre de développement qui organise des programmes éducatifs à l'intention des développeurs désireux de se familiariser avec le développement de Bitcoin.


+++



# Introduction

<partId>58c48e9b-e285-4dc6-8952-6cc5140b1313</partId>


## Aperçu du cours

<chapterId>28b7256b-9cb0-463e-a82d-d732be86c98c</chapterId>


Bienvenue dans ce cours PHI 301 sur la philosophie de développement de Bitcoin.


Le Bitcoin est plus qu'une simple crypto-monnaie, il incarne une vision philosophique de la décentralisation, de la vie privée, de l'absence de confiance et de la résilience. Ce cours est conçu spécifiquement pour les développeurs qui connaissent déjà les fondements techniques du Bitcoin et qui cherchent maintenant à approfondir leur compréhension des principes qui sous-tendent la conception et la gouvernance du Bitcoin.


Tout au long de ce cours, vous comprendrez mieux les valeurs et les stratégies essentielles qui ont guidé l'évolution du Bitcoin depuis plus d'une décennie. En explorant ces thèmes en profondeur, vous développerez la perspective critique nécessaire pour évaluer les développements futurs et y contribuer en toute confiance.


### Les valeurs centrales du Bitcoin


Qu'est-ce qui rend Bitcoin unique ? Cette section révèle les valeurs fondamentales qui sont au cœur de la conception de Bitcoin. Vous découvrirez la **décentralisation**, la pierre angulaire qui garantit qu'aucune entité ne contrôle le réseau ; l'**absence de confiance**, la clé qui élimine la dépendance à l'égard des tiers ; la **confidentialité**, essentielle à la fois à la liberté individuelle et à l'intégrité du système ; et la **finite Supply**, la garantie codée de la rareté qui façonne l'identité économique de la Bitcoin. La maîtrise de ces concepts vous permettra d'appréhender pleinement les forces et les faiblesses de Bitcoin.


### Bitcoin Gouvernance


Naviguer dans le paysage complexe de la gouvernance du Bitcoin exige plus qu'une expertise technique, il faut comprendre l'approche unique du Bitcoin en matière de consensus et de prise de décision. Dans cette section, vous découvrirez les mécanismes et les philosophies qui sous-tendent les processus critiques tels que les mises à jour de protocole, la nécessité de la pensée contradictoire, la force de la collaboration open-source, les défis permanents de la mise à l'échelle et les stratégies nuancées requises lorsque les choses tournent inévitablement mal. Fort de ces connaissances, vous serez prêt non seulement à participer, mais aussi à façonner l'avenir de Bitcoin de manière efficace et responsable.


Prêt à franchir la prochaine étape de votre parcours Bitcoin ? Commençons !


***N.B.** : Si vous rencontrez des termes inconnus liés à Bitcoin pendant le cours, veuillez vous référer au [glossaire] (https://planb.network/resources/glossary) pour trouver les définitions.*




# Bitcoin Valeurs centrales

<partId>2d6c683b-54c8-5465-b2ca-4e96a6828834</partId>


## Décentralisation

<chapterId>9397c84b-0038-5d0e-88d5-11767ce8182d</chapterId>




Ce document analyse ce qu'est la décentralisation et pourquoi elle est essentielle au fonctionnement de Bitcoin. Nous faisons la distinction entre la

et la décentralisation des mineurs et celle des nœuds complets, et discuter de ce qu'ils apportent à la résistance à la censure, l'une des propriétés les plus importantes du Bitcoin.


La discussion s'oriente ensuite vers la compréhension de la neutralité - ou l'absence de permission envers les utilisateurs, les mineurs et les développeurs - qui est une propriété nécessaire de tout système décentralisé. Enfin, nous abordons la question de savoir à quel point il peut être difficile de comprendre un système décentralisé tel que le Bitcoin, et nous présentons quelques modèles mentaux qui pourraient vous aider à le comprendre.


Un système sans point de contrôle central est dit *décentralisé*. Bitcoin est conçu pour éviter d'avoir un point central de contrôle, ou plus précisément un *point central de censure*.


La décentralisation est un moyen de parvenir à une *résistance à la censure*.


Il y a deux aspects majeurs de la décentralisation dans le Bitcoin : La décentralisation de la Miner et la décentralisation de la Full node.


La décentralisation Miner fait référence au fait que le traitement des transactions n'est ni effectué ni coordonné par une entité centrale. La décentralisation Full node fait référence au fait que la validation des blocs, c'est-à-dire les données produites par les mineurs, est effectuée à la périphérie du réseau, en fin de compte par ses utilisateurs, et non par quelques autorités de confiance.


![](assets/decentralization-banner.webp)


### Miner décentralisation



Il y a eu des tentatives de création de monnaies numériques avant le Bitcoin, mais la plupart d'entre elles ont échoué en raison d'un manque de décentralisation de la gouvernance et d'une résistance à la censure.


La décentralisation de Miner dans Bitcoin signifie que l'"ordre des transactions" n'est pas effectué par une seule entité ou un ensemble fixe d'entités. Il est effectué collectivement par tous les acteurs qui veulent y participer ; ce collectif de mineurs est un ensemble dynamique d'utilisateurs. Chacun peut s'y joindre ou le quitter à sa guise. Cette propriété rend Bitcoin résistant à la censure.


Si le Bitcoin était centralisé, il serait vulnérable à ceux qui voudraient le censurer, comme les gouvernements. Il connaîtrait le même sort que les précédentes tentatives de création de monnaie numérique. Dans l'introduction d'un [document] (https://www.blockstream.com/sidechains.pdf) intitulé "Enabling Blockchain Innovations with Pegged Sidechains", les auteurs expliquent que les premières versions de la monnaie numérique n'étaient pas équipées pour un environnement contradictoire (voir également le chapitre sur la pensée contradictoire dans la partie suivante).


David Chaum a présenté l'argent numérique comme un sujet de recherche en 1983, dans un contexte où un serveur central est chargé d'empêcher le Double-spending. Afin d'atténuer le risque de violation de la vie privée par cette partie centrale de confiance et d'assurer la fongibilité, Chaum a introduit la signature aveugle, qu'il a utilisée pour fournir un moyen cryptographique d'empêcher la liaison des signatures du serveur central (qui représentent des pièces de monnaie), tout en permettant au serveur central d'empêcher les doubles dépenses.

La nécessité d'un serveur central est devenue le talon d'Achille de l'argent liquide numérique [Gri99]. Bien qu'il soit possible de répartir ce point de défaillance unique en remplaçant la signature du serveur central par une signature de seuil de plusieurs signataires, il est important pour l'auditabilité que les signataires soient distincts et identifiables. Le système reste donc vulnérable aux pannes, puisque chaque signataire peut tomber en panne, ou être mis en panne, un par un.


Il est apparu clairement que l'utilisation d'un serveur central pour ordonner les transactions n'était pas une option viable en raison du risque élevé de censure. Même si l'on remplaçait le serveur central par une fédération d'un ensemble fixe de n serveurs, dont au moins m doivent approuver une commande, des difficultés subsisteraient. Le problème se déplacerait en effet vers une situation où les utilisateurs devraient se mettre d'accord sur cet ensemble de n serveurs ainsi que sur la manière de remplacer les serveurs malveillants par de bons serveurs sans dépendre d'une autorité centrale.


Imaginons ce qui pourrait se passer si la Bitcoin était censurable. Le censeur pourrait obliger les utilisateurs à s'identifier, à déclarer d'où vient leur argent ou ce qu'ils achètent avec avant d'autoriser leurs transactions à entrer dans la Blockchain.


De plus, l'absence de résistance à la censure permettrait au censeur de contraindre les utilisateurs à adopter de nouvelles règles du système. Par exemple, il pourrait imposer un changement qui lui permettrait de gonfler le montant de l'argent Supply, s'enrichissant ainsi lui-même. Dans ce cas, un utilisateur vérifiant les blocs aurait trois options pour gérer les nouvelles règles :



- Adopter : Accepter les modifications et les intégrer dans leur Full node.
- Rejeter : Refuser d'adopter les modifications ; l'utilisateur se retrouve alors avec un système qui ne traite plus les transactions, car les blocages du censeur sont désormais considérés comme non valables par le Full node de l'utilisateur.
- Déplacement : désigner un nouveau point central de contrôle ; tous les utilisateurs doivent déterminer comment se coordonner et se mettre d'accord sur le nouveau point central de contrôle.


S'ils y parviennent, les mêmes problèmes referont probablement surface à l'avenir, étant donné que le système est resté tout aussi censurable qu'auparavant.


Aucune de ces options n'est bénéfique pour l'utilisateur.


La résistance à la censure grâce à la décentralisation est ce qui différencie le Bitcoin des autres systèmes monétaires, mais ce n'est pas une chose facile à accomplir en raison du *problème du Double-spending*. Il s'agit de s'assurer que personne ne peut dépenser deux fois la même pièce, un problème que de nombreuses personnes pensaient impossible à résoudre de manière décentralisée. Satoshi Nakamoto écrit dans son [Bitcoin whitepaper] (https://planb.network/Bitcoin.pdf) comment résoudre le problème Double-spending :


> Dans cet article, nous proposons une solution au problème Double-spending en utilisant un serveur distribué peer-to-peer Timestamp pour generate la preuve informatique de l'ordre chronologique des transactions.


Il utilise ici l'expression étrange de "serveur Timestamp distribué de pair à pair". Le mot clé est ici *distribué*, ce qui, dans ce contexte, signifie qu'il n'y a pas de point de contrôle central. Nakamoto explique ensuite comment le Proof-of-Work est la solution.

Pourtant, personne ne l'explique mieux que

[Gregory Maxwell sur Reddit] (https://www.reddit.com/r/Bitcoin/comments/ddddfl/question_on_the_vulnerability_of_bitcoin/f2g9e7b/), où il répond à quelqu'un qui propose de limiter la puissance Hash des mineurs pour éviter les attaques potentielles de 51 % :


> Un système décentralisé comme Bitcoin utilise une élection publique. Mais on ne peut pas se contenter d'un vote des "gens" dans un système décentralisé, car il faudrait alors qu'une partie centralisée autorise les gens à voter. Bitcoin utilise plutôt un vote de puissance informatique, car il est possible de vérifier la puissance informatique sans l'aide d'un système centralisé
tiers.


Le billet explique comment le réseau décentralisé Bitcoin peut parvenir à un accord sur l'ordre des transactions grâce à l'utilisation de Proof-of-Work.


Il conclut en disant que l'attaque des 51% n'est pas particulièrement inquiétante, comparée au fait que les gens ne se soucient pas des propriétés de décentralisation de Bitcoin ou ne les comprennent pas :


> Le risque le plus important pour Bitcoin est que le public qui l'utilise ne comprenne pas, ne se préoccupe pas et ne protège pas les propriétés de décentralisation qui lui confèrent sa valeur par rapport aux alternatives centralisées.

La conclusion est importante. Si les gens ne protègent pas la décentralisation de Bitcoin, qui est une approximation de sa résistance à la censure, Bitcoin pourrait être victime de pouvoirs centralisateurs, jusqu'à ce qu'il soit tellement centralisé que la censure devienne une réalité. Dans ce cas, la plupart, sinon la totalité, de sa proposition de valeur disparaît. Ceci nous amène à la section suivante sur la décentralisation de Full node.


### Full node décentralisation



Dans les paragraphes ci-dessus, nous avons surtout parlé de la décentralisation Miner et de la façon dont la centralisation des mineurs peut permettre la censure. Mais il existe également un autre aspect de la décentralisation, à savoir la *décentralisation Full node*.


L'importance de la décentralisation de la Full node est liée à l'absence de confiance. Supposons qu'un utilisateur cesse d'exploiter sa propre Full node en raison, par exemple, d'une augmentation prohibitive du coût d'exploitation. Dans ce cas, il doit interagir avec le réseau Bitcoin d'une autre manière, éventuellement en utilisant des portefeuilles web ou des portefeuilles légers, ce qui nécessite un certain niveau de confiance dans les fournisseurs de ces services.


L'utilisateur passe de l'application directe des règles de consensus du réseau à la confiance en quelqu'un d'autre. Supposons maintenant que la plupart des utilisateurs délèguent l'application du consensus à une entité de confiance. Dans ce cas, le réseau peut rapidement tomber dans la spirale de la centralisation et les règles du réseau peuvent être modifiées par des acteurs malveillants conspirateurs.


Dans [a

Bitcoin Magazine article] (https://bitcoinmagazine.com/technical/decentralist-perspective-Bitcoin-might-need-small-blocks-1442090446), Aaron van Wirdum interroge les développeurs de Bitcoin sur leur point de vue concernant la décentralisation et les risques liés à l'augmentation de la taille maximale des blocs de Bitcoin. Cette discussion a été un sujet de Hot pendant la période 2014-2017, lorsque de nombreuses personnes se sont opposées à l'augmentation de la limite de la taille des blocs pour permettre un plus grand débit de transactions.


Un argument de poids contre l'augmentation de la taille des blocs est qu'elle augmente le coût de la vérification. Si le coût de la vérification augmente, cela poussera certains utilisateurs à cesser d'exploiter leurs nœuds complets. De ce fait, davantage de personnes ne seront pas en mesure d'utiliser le système d'une manière conforme à la norme Trustless.


Pieter Wuille est cité dans l'article, où il explique les risques de la centralisation Full node :


> Si de nombreuses entreprises gèrent une Full node, cela signifie qu'elles doivent toutes être convaincues de mettre en œuvre un ensemble de règles différent. En d'autres termes, la décentralisation de la validation des blocs est ce qui donne du poids aux règles de consensus.
> Mais si le nombre de Full node tombe très bas, par exemple parce que tout le monde utilise les mêmes portefeuilles web, bourses et SPV ou portefeuilles mobiles, la réglementation pourrait devenir une réalité. Et si les autorités peuvent réglementer les règles de consensus, cela signifie qu'elles peuvent changer tout ce qui fait de Bitcoin Bitcoin. Même la limite de 21 millions de Bitcoin.

Nous y voilà. Les utilisateurs de Bitcoin devraient gérer leurs propres nœuds complets afin de dissuader les régulateurs et les grandes entreprises d'essayer de changer les règles du consensus.


### Neutralité



Bitcoin est neutre, ou sans permission, comme on aime à l'appeler. Cela signifie que Bitcoin ne se soucie pas de qui vous êtes ni de l'usage que vous en faites.


Bitcoin est neutre, ce qui est une bonne chose, et c'est la seule façon dont il peut fonctionner. S'il était contrôlé par une organisation, il ne serait qu'un autre type d'objet virtuel et ne m'intéresserait pas du tout


Tant que vous respectez les règles, vous êtes libre de l'utiliser comme bon vous semble, sans demander la permission à qui que ce soit. Cela inclut *Mining*, *transiger* dans, et *construire des protocoles et des services* au-dessus de Bitcoin :



- Si le *Mining* était un processus soumis à autorisation, il faudrait qu'une autorité centrale sélectionne les personnes autorisées à exploiter les mines. Cela conduirait très probablement les mineurs à devoir signer des contrats légaux dans lesquels ils accepteraient de

de censurer les transactions en fonction des caprices de l'autorité centrale, ce qui va à l'encontre de l'objectif premier du Mining.



- Si les personnes *transigeant* dans Bitcoin devaient fournir des informations personnelles, déclarer l'objet de leurs transactions, ou prouver qu'elles sont dignes de transiger, nous aurions également besoin d'un point central d'autorité pour approuver les utilisateurs ou les transactions. Encore une fois, cela conduirait à la censure et à l'exclusion.



- Si les développeurs devaient demander l'autorisation de *construire des protocoles* sur la base de Bitcoin, seuls les protocoles autorisés par le comité central de subvention des développeurs seraient développés. En raison de l'intervention du gouvernement, cela exclurait inévitablement tous les protocoles préservant la vie privée et toutes les tentatives d'amélioration de la décentralisation.


À tous les niveaux, essayer d'imposer des restrictions sur qui peut utiliser Bitcoin pour quoi que ce soit nuira à Bitcoin au point qu'il ne sera plus à la hauteur de sa proposition de valeur.


Pieter Wuille https://Bitcoin.stackexchange.com/a/92055/69518 [répond à une question sur la pile Exchange] sur la façon dont la Blockchain est liée aux bases de données normales. Il explique comment l'absence de permission est possible grâce à l'utilisation de la Proof-of-Work en combinaison avec des incitations économiques.


Il conclut :


> 
> Il n'y a probablement qu'un seul endroit au monde où l'on peut trouver un ou quelques exemplaires d'occasion.

Il explique que, pour parvenir à l'absence de permission, le système a très probablement besoin de sa propre monnaie, ce qui "limite les cas d'utilisation aux seules crypto-monnaies". En effet, la participation sans permission, ou Mining, nécessite des incitations économiques intégrées au système lui-même.


### La décentralisation en marche



L'un des aspects convaincants de la Bitcoin est qu'il est facile de comprendre que personne ne la contrôle. Il n'y a pas de comités ou d'exécutifs dans Bitcoin. Gregory Maxwell, toujours [sur le subreddit Bitcoin] (https://www.reddit.com/r/Bitcoin/comments/s82t2n/comment/htdte7w/?utm_source=share&utm_medium=web2x&context=3), compare cela à la langue anglaise d'une manière intrigante :


> Beaucoup de gens ont du mal à comprendre les systèmes autonomes, il y en a beaucoup dans leur vie, des choses comme la langue anglaise, mais les gens les prennent pour acquis et ne les considèrent même pas comme des systèmes. Ils sont coincés dans un mode de pensée centralisé où tout ce qu'ils considèrent comme une "chose" est contrôlé par une autorité.
>

> Bitcoin ne se concentre sur rien. Les diverses personnes qui ont adopté Bitcoin ont choisi de leur plein gré d'en faire la promotion, et la façon dont elles choisissent de le faire ne regarde qu'elles. Les personnes obsédées par l'autorité peuvent voir ces activités et croire qu'il s'agit d'une opération de l'autorité Bitcoin, mais une telle autorité n'existe pas.


La façon dont Bitcoin fonctionne grâce à la décentralisation ressemble à l'extraordinaire intelligence collective que l'on trouve chez de nombreuses espèces dans la nature. L'informaticienne Radhika Nagpal parle dans un [Ted talk] (https://www.ted.com/talks/radhika_nagpal_what_intelligent_machines_can_learn_from_a_school_of_fish) du comportement collectif des bancs de poissons et de la manière dont les scientifiques tentent de l'imiter à l'aide de robots.


> Deuxièmement, et c'est ce que je trouve toujours le plus remarquable, nous savons qu'il n'y a pas de chef pour superviser ce banc de poissons. Au contraire, cet incroyable comportement collectif émerge purement des interactions d'un poisson avec un autre.
> D'une manière ou d'une autre, il existe des interactions ou des règles d'engagement entre les poissons voisins qui font que tout se passe bien.

Elle souligne que de nombreux systèmes, qu'ils soient naturels ou artificiels, peuvent fonctionner sans chef et le font, et qu'ils sont puissants et résistants. Chaque individu n'interagit qu'avec son environnement immédiat, mais ensemble, ils forment quelque chose de formidable.


![](assets/fishschool.webp)

*Les bancs de poissons n'ont pas de leader*


Quelle que soit votre opinion sur le Bitcoin, sa nature décentralisée le rend difficile à contrôler. Le Bitcoin existe, et vous ne pouvez rien y faire. C'est un sujet à étudier, pas à débattre.


### Conclusion sur la décentralisation


Nous faisons la distinction entre la décentralisation Full node et la décentralisation Mining. La décentralisation Mining est un moyen de résister à la censure, tandis que la décentralisation Full node est ce qui empêche les règles consensuelles du réseau Hard d'être modifiées sans un large soutien de la part des utilisateurs.


La nature décentralisée du Bitcoin permet une neutralité vis-à-vis des développeurs, des utilisateurs et des mineurs. Tout le monde est libre de participer sans demander la permission.


Les systèmes décentralisés peuvent être difficiles à comprendre, mais il existe des modèles mentaux qui peuvent aider, par exemple la langue anglaise ou les bancs de poissons.


## L'absence de confiance

<chapterId>0506ba61-16a3-543c-95fa-3f3e2dd64121</chapterId>



![](assets/trustlessness-banner.webp)


Ce chapitre analyse le concept d'absence de confiance, ce qu'il signifie du point de vue de l'informatique et pourquoi Bitcoin doit être Trustless pour conserver sa proposition de valeur.

Nous discuterons ensuite de ce que signifie utiliser Bitcoin d'une manière Trustless, et du type de garanties qu'une Full node peut ou ne peut pas vous donner.

Dans la dernière section, nous examinons l'interaction réelle entre Bitcoin et les logiciels ou les utilisateurs réels, ainsi que la nécessité de faire des compromis entre la commodité et l'absence de confiance pour obtenir quoi que ce soit.


Les gens disent souvent des choses comme "Bitcoin est génial parce que c'est Trustless".


Qu'entend-on par Trustless ? Pieter Wuille explique ce terme très répandu sur [Stack Exchange] (https://Bitcoin.stackexchange.com/a/45674/69518) :


> La confiance dont nous parlons dans "Trustless" est un terme technique abstrait. Un système distribué est appelé Trustless lorsqu'il ne nécessite aucune partie de confiance pour fonctionner correctement.

En bref, le terme *Trustless* fait référence à une propriété du protocole Bitcoin qui lui permet de fonctionner logiquement sans "aucune partie de confiance". Cela diffère de la confiance que vous devez inévitablement accorder au logiciel ou au matériel que vous utilisez. Ce dernier aspect de la confiance sera abordé plus loin dans ce chapitre.


Dans les systèmes centralisés, nous nous appuyons sur la réputation d'un acteur central pour nous assurer qu'il veillera à la sécurité ou qu'il fera marche arrière en cas de problème, ainsi que sur le système juridique pour sanctionner toute violation. Ces exigences de confiance sont problématiques dans les systèmes décentralisés pseudonymes - il n'y a pas de possibilité de recours et il ne peut donc pas y avoir de confiance. Dans l'introduction du [livre blanc Bitcoin] (https://Bitcoin.org/Bitcoin.pdf), Satoshi Nakamoto décrit ce problème :


> Le commerce sur Internet repose presque exclusivement sur les institutions financières qui servent de tiers de confiance pour le traitement des paiements électroniques.
> Bien que le système fonctionne assez bien pour la plupart des transactions, il souffre toujours des faiblesses inhérentes au modèle basé sur la confiance.  Les transactions totalement irréversibles ne sont pas vraiment possibles, car les institutions financières ne peuvent pas éviter la médiation des litiges. Le coût de la médiation augmente les coûts de transaction, en limitant la taille minimale pratique de la transaction et en supprimant la possibilité d'effectuer de petites transactions occasionnelles, et il y a un coût plus large dans la perte de la capacité d'effectuer des paiements non réversibles pour des services non réversibles.
> Avec la possibilité d'un retournement, le besoin de confiance s'accroît. Les commerçants doivent se méfier de leurs clients et leur demander plus d'informations qu'ils n'en auraient besoin.  Un certain pourcentage de fraude est considéré comme inévitable. Ces coûts et incertitudes de paiement peuvent être évités en personne en utilisant de la monnaie physique, mais il n'existe aucun mécanisme permettant d'effectuer des paiements sur un canal de communication sans une partie de confiance

Il semble que nous ne puissions pas avoir un système décentralisé basé sur la confiance, et c'est pourquoi l'absence de confiance est importante dans Bitcoin.


Pour utiliser la Bitcoin à la manière de la Trustless, vous devez faire fonctionner un nœud Bitcoin à validation complète. Ce n'est qu'alors que vous pourrez vérifier que les blocs que vous recevez des autres suivent les règles du consensus ; par exemple, que le calendrier d'émission des pièces est respecté et qu'il n'y a pas de double dépense sur la Blockchain. Si vous ne gérez pas de Full node, vous confiez la vérification des blocs Bitcoin à quelqu'un d'autre et vous lui faites confiance pour vous dire la vérité, ce qui signifie que vous n'utilisez pas la Bitcoin sans confiance.


David Harding a rédigé [un article sur le site web Bitcoin.org] (https://Bitcoin.org/en/Bitcoin-core/features/validation) expliquant comment la gestion d'une Full node - ou l'utilisation sans confiance de la Bitcoin - vous aide réellement :


> La monnaie Bitcoin ne fonctionne que lorsque les gens acceptent des bitcoins en Exchange contre d'autres choses de valeur. En d'autres termes, ce sont les personnes qui acceptent des bitcoins qui lui donnent de la valeur et qui décident du fonctionnement de la Bitcoin.
>

> Lorsque vous acceptez des bitcoins, vous avez le pouvoir d'appliquer les règles de Bitcoin, telles que l'interdiction de confisquer les bitcoins d'une personne sans avoir accès aux clés privées de cette personne.
>

> Malheureusement, de nombreux utilisateurs externalisent leur pouvoir d'application. Cela laisse la décentralisation de Bitcoin dans un état affaibli où une poignée de mineurs peut s'entendre avec une poignée de banques et de services gratuits pour changer les règles de Bitcoin pour tous les utilisateurs non vérificateurs qui ont externalisé leur pouvoir.
>

> Contrairement à d'autres portefeuilles, Bitcoin Core applique les règles - ainsi, si les mineurs et les banques changent les règles pour leurs utilisateurs qui ne vérifient pas, ces utilisateurs ne pourront pas payer les utilisateurs de Bitcoin Core qui ont une validation complète, comme vous.


Il affirme que l'utilisation d'une Full node vous aidera à vérifier tous les aspects de la Blockchain sans faire confiance à personne d'autre, afin de garantir que les pièces que vous recevez des autres sont authentiques. C'est très bien, mais il y a une chose importante qu'une Full node ne peut pas faire : elle ne peut pas empêcher la double dépense par la réécriture de la chaîne :


> Notez que bien que tous les programmes - y compris le Bitcoin Core - soient vulnérables aux réécritures de chaîne, le Bitcoin fournit un mécanisme de défense : plus vos transactions ont de confirmations, plus vous êtes en sécurité. Il n'y a pas de meilleure défense décentralisée connue que celle-là.

Quel que soit le degré d'avancement de votre logiciel, vous devez toujours être certain que les blocs contenant vos pièces ne seront pas réécrits. Toutefois, comme le souligne Harding, vous pouvez attendre un certain nombre de confirmations, après quoi vous considérez que la probabilité d'une réécriture de la chaîne est suffisamment faible pour être acceptable.


Les incitations à utiliser Bitcoin d'une manière Trustless s'alignent sur le besoin de décentralisation Full node du système. Plus il y a de personnes qui utilisent leurs propres nœuds complets, plus la décentralisation Full node est importante, et donc plus la Bitcoin est résistante aux modifications malveillantes du protocole. Malheureusement, comme nous l'avons expliqué dans la section sur la décentralisation Full node, les utilisateurs optent souvent pour des services de confiance en raison de l'inévitable compromis entre l'absence de confiance et la commodité.


L'absence de confiance de Bitcoin est absolument impérative du point de vue du système. En 2018, Matt Corallo a [parlé de l'absence de confiance] (https://btctranscripts.com/baltic-honeybadger/2018/trustlessness-scalability-and-directions-in-security-models/) lors de la conférence Baltic Honeybadger à Riga.


![video](https://youtu.be/66ZoGUAnY9s?t=4019)


L'essentiel de cet exposé est qu'il n'est pas possible de construire des systèmes Trustless au-dessus d'un système de confiance, mais qu'il est possible de construire des systèmes de confiance - par exemple, un système Wallet de garde - au-dessus d'un système Trustless.



![width=50%](assets/trust.webp)


Une Trustless de base Layer permet de faire des compromis à des niveaux plus élevés


Ce modèle de sécurité permet au concepteur du système de faire des compromis

qui ont un sens pour eux, sans imposer ces compromis aux autres.


### Ne faites pas confiance, vérifiez



Bitcoin fonctionne en toute confiance, mais vous devez toujours faire confiance à votre logiciel et à votre matériel dans une certaine mesure. En effet, il se peut que votre logiciel ou votre matériel ne soit pas programmé pour faire ce qui est indiqué sur la boîte. Par exemple, il se peut que votre logiciel ou matériel ne soit pas programmé pour faire ce qui est indiqué sur la boîte :



- L'unité centrale peut être conçue de manière malveillante pour détecter les opérations cryptographiques de la clé privée et faire fuir les données de la clé privée.
- Le générateur de nombres aléatoires du système d'exploitation n'est peut-être pas aussi aléatoire qu'il le prétend.
- Bitcoin Core pourrait avoir inséré un code qui enverra vos clés privées à un acteur malveillant.


Donc, en plus d'utiliser un Full node, vous devez également vous assurer que vous utilisez ce que vous avez l'intention d'utiliser. L'utilisateur de Reddit brianddk [a écrit un article](https://www.reddit.com/r/Bitcoin/comments/smj1ep/bitcoin_v220_and_guix_stronger_defense_against/) sur les différents niveaux de confiance que vous pouvez choisir lors de la vérification de votre logiciel. Dans la section "Trusting the builders", il parle des constructions reproductibles :


> Les versions reproductibles sont un moyen de concevoir un logiciel de façon à ce que de nombreux développeurs de la communauté puissent chacun construire le logiciel et s'assurer que l'installateur final construit est identique à ce que les autres développeurs produisent. Dans le cas d'un projet très public et reproductible comme Bitcoin, il n'est pas nécessaire de faire entièrement confiance à un seul développeur. De nombreux développeurs peuvent tous effectuer la construction et attester qu'ils ont produit le même fichier que celui signé numériquement par le développeur d'origine.

L'article définit cinq niveaux de confiance : confiance dans le site, dans les constructeurs, dans le compilateur, dans le noyau et dans le matériel.


Pour approfondir le sujet des constructions reproductibles, Carl Dong [a fait une présentation sur Guix] (https://btctranscripts.com/breaking-Bitcoin/2019/Bitcoin-build-system/) expliquant pourquoi faire confiance au système d'exploitation, aux bibliothèques et aux compilateurs peut être problématique, et comment résoudre ce problème avec un système appelé Guix, qui est utilisé par le Bitcoin Core aujourd'hui.


> Que pouvons-nous donc faire pour éviter que notre chaîne d'outils ne contienne un certain nombre de binaires de confiance qui peuvent être reproduits de manière malveillante ? Nous devons être plus que reproductibles. Nous devons être amorçables. Nous ne pouvons pas avoir autant d'outils binaires que nous devons télécharger et auxquels nous devons faire confiance à partir de serveurs externes contrôlés par d'autres organisations.
>

> Nous devrions savoir comment ces outils sont construits et comment nous pouvons les reconstruire, de préférence à partir d'un ensemble beaucoup plus restreint de binaires de confiance. Nous devons réduire autant que possible notre ensemble de binaires de confiance et disposer d'un chemin facilement vérifiable entre ces chaînes d'outils et ce que nous utilisons pour construire Bitcoin. Cela nous permet de maximiser la vérification et de minimiser la confiance.

Il explique ensuite comment Guix nous permet de ne faire confiance qu'à un binaire minimal de 357 octets qui peut être vérifié et entièrement compris si vous savez comment interpréter les instructions. C'est assez remarquable : on vérifie que le binaire de 357 octets fait ce qu'il doit faire, puis on l'utilise pour construire le système de construction complet à partir du code source, et on se retrouve avec un binaire Bitcoin Core qui devrait être une copie exacte de la construction de n'importe qui d'autre.


Il existe un mantra auquel souscrivent de nombreux bitcoiners et qui résume bien ce qui précède :


> Ne faites pas confiance, vérifiez.

Cela fait référence à la phrase "[trust, but verify](https://en.wikipedia.org/wiki/Trust,_but_verify)" que l'ancien président américain Ronald Reagan a utilisée dans le contexte du désarmement nucléaire. les [Bitcoiners](https://twitter.com/Truthcoin/status/1491415722123153408?s=20&t=ZyROxZxlBppdRpuuzsiF5w) l'ont inversée pour souligner le rejet de la confiance et l'importance d'exécuter une Full node.


Il appartient aux utilisateurs de décider dans quelle mesure ils souhaitent vérifier le logiciel qu'ils utilisent et les données Blockchain qu'ils reçoivent. Comme pour beaucoup d'autres choses dans le Bitcoin, il y a un compromis entre la commodité et la confiance. Il est presque toujours plus pratique d'utiliser un Wallet dont on a la garde que d'exécuter le Bitcoin Core sur son propre matériel. Cependant, comme le logiciel Bitcoin mûrit et que les interfaces utilisateur s'améliorent, il devrait, avec le temps, mieux supporter les utilisateurs désireux de travailler sans confiance. En outre, au fur et à mesure que les utilisateurs acquièrent des connaissances, ils devraient être en mesure d'éliminer progressivement la confiance de l'équation.


Certains utilisateurs pensent de manière contradictoire et vérifient la plupart des aspects du logiciel qu'ils utilisent. En conséquence, ils réduisent le besoin de confiance au strict minimum, puisqu'ils ne doivent faire confiance qu'à leur matériel informatique et à leur système d'exploitation. Ce faisant, ils aident également les personnes qui ne vérifient pas leur matériel de manière aussi approfondie en faisant entendre leur voix en public pour les avertir de tout problème qu'ils pourraient trouver. Un bon exemple de cela est un [événement survenu en 2018] (https://bitcoincore.org/en/2018/09/20/notice/), lorsque quelqu'un a découvert un bug qui permettait aux mineurs de dépenser une sortie deux fois dans la même transaction :


> CVE-2018-17144, dont un correctif a été publié le 18 septembre dans les versions 0.16.3 et 0.17.0rc4 de Bitcoin Core, comprend à la fois un composant de déni de service et une vulnérabilité critique d'inflation. Il a été initialement signalé à plusieurs développeurs travaillant sur Bitcoin Core, ainsi que sur des projets supportant d'autres crypto-monnaies, y compris ABC et Unlimited le 17 septembre comme un bug de déni de service uniquement, mais nous avons rapidement déterminé que le problème était également une vulnérabilité d'inflation avec la même cause racine et le même correctif.

Dans ce cas, une personne anonyme a signalé un problème qui s'est avéré bien pire que ce qu'elle avait imaginé. Cela montre que les personnes qui vérifient le code signalent souvent les failles de sécurité au lieu de les exploiter. Cela est bénéfique pour ceux qui ne sont pas en mesure de tout vérifier eux-mêmes.


Cependant, les utilisateurs ne devraient pas faire confiance à d'autres pour assurer leur sécurité, mais plutôt vérifier par eux-mêmes chaque fois qu'ils le peuvent ; c'est ainsi que l'on reste aussi souverain que possible, et que Bitcoin prospère. Plus il y a d'yeux sur le logiciel, moins il y a de chances que des codes malveillants et des failles de sécurité se glissent dans le logiciel.


### Conclusion sur l'absence de confiance



Le protocole Bitcoin est Trustless parce qu'il permet aux utilisateurs d'interagir avec lui sans faire confiance à un tiers. Dans la pratique, cependant, la plupart des gens ne sont pas en mesure de vérifier l'ensemble des logiciels et du matériel sur lesquels ils exécutent le protocole Bitcoin. Les personnes qualifiées qui vérifient les logiciels ou le matériel sont en mesure d'avertir d'autres personnes moins qualifiées lorsqu'elles trouvent des codes malveillants ou des bogues.


Sans confiance, il ne peut y avoir de décentralisation, car la confiance implique inévitablement un point d'autorité central. On peut construire un système de confiance au-dessus d'un système Trustless, mais on ne peut pas construire un système Trustless au-dessus d'un système de confiance.


## Vie privée

<chapterId>1b960afe-0008-589b-b2f4-007d60d264c6</chapterId>



![](assets/privacy-banner.webp)


Ce chapitre traite de la manière de garder pour soi ses informations financières privées. Il explique ce qu'est la vie privée dans le contexte de Bitcoin, pourquoi elle est importante et ce que signifie le fait que Bitcoin soit pseudonyme. Il examine également la manière dont les données privées peuvent fuir, tant en On-Chain qu'en off-chain.


Il aborde ensuite le fait que les bitcoins doivent être fongibles, c'est-à-dire interchangeables avec d'autres bitcoins, et explique comment la fongibilité et la protection de la vie privée vont de pair. Enfin, le chapitre présente quelques mesures que vous pouvez prendre pour améliorer votre vie privée et celle des autres.


Bitcoin peut être décrit comme un système pseudonyme, dans lequel les utilisateurs ont plusieurs pseudonymes sous la forme de clés publiques. À première vue, cela semble être un bon moyen de protéger les utilisateurs contre l'identification, mais il est en fait très facile de divulguer involontairement des informations financières privées.


### Qu'est-ce que le respect de la vie privée ?



La notion de vie privée peut revêtir des significations différentes selon les contextes. Dans Bitcoin, cela signifie généralement que les utilisateurs n'ont pas à révéler leurs informations financières à d'autres personnes, à moins qu'ils ne le fassent volontairement.


Il existe de nombreuses façons de divulguer des informations privées à d'autres personnes, que ce soit à leur insu ou non. Les données peuvent être divulguées sur le réseau public Blockchain ou par d'autres moyens, par exemple lorsque des acteurs malveillants interceptent vos communications sur internet.


### Pourquoi la vie privée est-elle importante ?


L'importance de la protection de la vie privée dans le cadre de Bitcoin peut sembler évidente, mais il y a des aspects auxquels on ne pense pas forcément tout de suite. [Sur le forum Bitcoin Talk] (https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908), Gregory Maxwell nous présente un grand nombre de bonnes raisons pour lesquelles il pense que la vie privée est importante. Parmi elles, le libre marché, la sécurité et la dignité humaine :


> La confidentialité financière est un critère essentiel pour le fonctionnement efficace d'un marché libre : si vous dirigez une entreprise, vous ne pouvez pas fixer efficacement vos prix si vos fournisseurs et vos clients peuvent voir toutes vos transactions contre votre volonté.
> Vous ne pouvez pas être compétitif si vos concurrents suivent vos ventes.  Si vous payez votre propriétaire en Bitcoin sans disposer d'une confidentialité suffisante, votre propriétaire verra que vous avez reçu une augmentation de salaire et pourra vous réclamer un loyer plus élevé.
>

> La protection de la vie privée est essentielle pour la sécurité personnelle : si les voleurs peuvent voir vos dépenses, vos revenus et vos avoirs, ils peuvent utiliser ces informations pour vous cibler et vous exploiter. Sans protection de la vie privée, les personnes malveillantes sont plus à même d'usurper votre identité, de vous dérober vos achats importants ou de se faire passer pour des entreprises avec lesquelles vous effectuez des transactions... elles peuvent savoir exactement combien elles essaieront de vous escroquer.
>

> La protection de la vie privée est essentielle à la dignité humaine : personne ne veut que la serveuse snobinarde du café ou ses voisins indiscrets commentent ses revenus ou ses habitudes de consommation. Personne ne veut que sa belle-famille, folle de bébés, lui demande pourquoi elle achète des contraceptifs (ou des sex toys). Votre employeur n'a pas à savoir à quelle église vous faites des dons. Ce n'est que dans un monde parfaitement éclairé et exempt de discrimination, où personne n'a d'autorité indue sur autrui, que nous pourrions conserver notre dignité et effectuer nos transactions légales librement, sans autocensure, si nous ne disposons pas d'une vie privée.

Maxwell aborde également la question de la fongibilité, qui sera examinée plus loin dans ce chapitre, ainsi que la question de savoir si le respect de la vie privée et l'application de la loi ne sont pas contradictoires.


### Pseudonymat


Nous avons mentionné plus haut que Bitcoin est pseudonyme et que les pseudonymes sont des clés publiques. Dans les médias, on entend souvent dire que Bitcoin est anonyme, ce qui n'est pas exact. Il existe une distinction entre l'anonymat et le pseudonymat.


Andrew Poelstra [explique dans un billet Bitcoin Stack Exchange] (https://Bitcoin.stackexchange.com/a/29473/69518) à quoi ressemblerait l'anonymat dans les transactions :


> L'anonymat total, c'est-à-dire le fait que lorsque vous dépensez de l'argent, il n'y a aucune trace de son origine ou de sa destination, est théoriquement possible en utilisant la technique cryptographique des preuves à connaissance nulle.

La différence semble être que dans une forme pseudonyme de monnaie, il est possible de retracer les paiements entre les pseudonymes, alors que dans une forme anonyme de monnaie, ce n'est pas le cas. Étant donné que les paiements effectués dans le cadre de Bitcoin sont traçables entre les pseudonymes, il ne s'agit pas d'un système anonyme.


Nous avons également dit que les pseudonymes étaient des clés publiques, mais il s'agit en fait d'adresses dérivées de clés publiques. Pourquoi utilisons-nous des adresses comme pseudonymes et pas autre chose, par exemple des noms descriptifs, comme "watchme1984" ? Cette question a été [bien expliquée] (https://Bitcoin.stackexchange.com/a/25175/69518) par l'utilisateur Tim S., également sur Bitcoin Stack Exchange :


> Pour que l'idée de Bitcoin fonctionne, vous devez avoir des pièces qui ne peuvent être dépensées que par le propriétaire d'une clé privée donnée. Cela signifie que ce que vous envoyez doit être lié, d'une manière ou d'une autre, à une clé publique.
>

> L'utilisation de pseudonymes arbitraires (par exemple, des noms d'utilisateur) signifierait qu'il faudrait ensuite lier d'une manière ou d'une autre le pseudonyme à une clé publique afin d'activer la cryptographie à clé publique/privée. Cela supprimerait la possibilité de créer des adresses/pseudonymes hors ligne en toute sécurité (par exemple, avant que quelqu'un puisse envoyer de l'argent au nom d'utilisateur "tdumidu", il faudrait annoncer dans la Blockchain que "tdumidu" est détenu par la clé publique "a1c...", et inclure une redevance pour que les autres aient une raison de l'annoncer), réduirait l'anonymat (en vous encourageant à réutiliser les pseudonymes), et augmenterait inutilement la taille de la Blockchain. Cela créerait également un faux sentiment de sécurité quant au fait que vous envoyez de l'argent à la personne que vous pensez être (si je prends le nom "Linus Torvalds" avant lui, alors c'est le mien et les gens pourraient envoyer de l'argent en pensant qu'ils paient le créateur de Linux, et non moi).

L'utilisation d'adresses ou de clés publiques permet d'atteindre des objectifs importants, tels que la suppression de la nécessité d'enregistrer préalablement un pseudonyme d'une manière ou d'une autre, la réduction des incitations à la réutilisation des pseudonymes, l'évitement du gonflement de Blockchain et la difficulté d'usurper l'identité d'autres personnes.


### Blockchain vie privée



La protection de la vie privée sur le site Blockchain concerne les informations que vous divulguez en effectuant des transactions sur le site Blockchain. Elle s'applique à toutes les transactions, celles que vous envoyez comme celles que vous recevez.


Satoshi Nakamoto réfléchit à la confidentialité On-Chain dans la section 7 de son [Bitcoin whitepaper] (https://Bitcoin.org/Bitcoin.pdf) :


> En guise de pare-feu supplémentaire, une nouvelle paire de clés doit être utilisée pour chaque transaction afin d'éviter qu'elles ne soient liées à un propriétaire commun. L'établissement de liens est toujours inévitable dans le cas des transactions à entrées multiples, qui révèlent nécessairement que leurs entrées appartiennent au même propriétaire. Le risque est que si le propriétaire d'une clé est révélé, l'établissement d'un lien pourrait révéler d'autres transactions appartenant au même propriétaire.

Le document résume les principaux problèmes de confidentialité Blockchain, à savoir la réutilisation Address et le regroupement Address. Le premier s'explique de lui-même, le second fait référence à la capacité de décider, avec un certain niveau de certitude, qu'un ensemble d'adresses différentes appartient au même utilisateur.


![](assets/address-reuse-clustering.webp)


Fuites de données typiques sur le Blockchain


Chris Belcher [a écrit en détail] (https://en.Bitcoin.it/Privacy#Blockchain_attacks_on_privacy) sur les différents types de fuites de la vie privée qui peuvent se produire sur le Bitcoin Blockchain. Nous vous recommandons de lire au moins les premiers paragraphes de la rubrique "Blockchain attacks on privacy"


Il en ressort que la protection de la vie privée dans Bitcoin n'est pas parfaite. Les transactions privées exigent une quantité de travail non négligeable. La plupart des gens ne sont pas prêts à aller aussi loin pour la protection de la vie privée. Il semble qu'il y ait un compromis clair entre la protection de la vie privée et la facilité d'utilisation.


Un autre aspect important de la protection de la vie privée est que les mesures que vous prenez pour protéger votre propre vie privée affectent également les autres utilisateurs. Si vous négligez votre propre vie privée, d'autres personnes risquent également de voir leur vie privée réduite. Gregory Maxwell l'explique très clairement dans le cadre de la discussion Bitcoin Talk [dont le lien figure ci-dessus] (https://bitcointalk.org/index.php?topic=334316.msg3589252#msg3589252), et conclut par un exemple :


> Cela fonctionne également dans la pratique... Un hacker blanc sympa sur IRC s'amusait à craquer des brainwallets et a trouvé une phrase avec ~250 BTC à l'intérieur.  Nous avons pu identifier le propriétaire rien qu'avec la Address, parce qu'il avait été payé par un service Bitcoin qui réutilisait les adresses, et il a pu le convaincre de donner les coordonnées de l'utilisateur. Il a réussi à les convaincre de lui donner les coordonnées de l'utilisateur. Il a réussi à joindre l'utilisateur par téléphone, qui était choqué et confus, mais reconnaissant de ne pas avoir perdu son argent.  C'est une fin heureuse. (Ce n'est pas le seul exemple, loin de là, mais c'est l'un des plus amusants).

Dans ce cas, tout s'est bien passé grâce à un hacker à l'esprit philanthropique, mais ne comptez pas sur lui la prochaine fois.


### Protection de la vie privée hors Blockchain


Si le Blockchain s'avère être une source notoire de fuites de données privées, il existe de nombreuses autres fuites qui n'utilisent pas le Blockchain, certaines plus sournoises que d'autres. Elles vont des enregistreurs de frappe à l'analyse du trafic réseau. Pour en savoir plus sur certaines de ces méthodes, reportez-vous à [l'article de Chris Belcher] (https://en.Bitcoin.it/Privacy#Non-blockchain_attacks_on_privacy), et plus particulièrement à la section "Non-Blockchain attacks on privacy" (attaques contre la vie privée sans Blockchain).


Parmi une pléthore d'attaques, Belcher mentionne la possibilité pour quelqu'un d'espionner votre connexion internet, par exemple votre fournisseur d'accès :


> Si l'adversaire voit sortir de votre nœud une transaction ou un bloc qui n'y est pas entré auparavant, il peut savoir avec une quasi-certitude que la transaction a été effectuée par vous ou que le bloc a été miné par vous. Comme il s'agit de connexions internet, l'adversaire sera en mesure de relier l'IP Address aux informations découvertes sur la Bitcoin.

Toutefois, ce sont les bourses d'échange qui présentent les fuites les plus évidentes en matière de protection de la vie privée. En raison des lois, généralement appelées KYC (Know Your Customer) et AML (Anti-Money Laundering), en vigueur dans les juridictions où elles opèrent, les bourses et les entreprises connexes doivent souvent collecter des données personnelles sur leurs utilisateurs, constituant ainsi de grandes bases de données sur les utilisateurs et les bitcoins qu'ils possèdent. Ces bases de données constituent de formidables pots de miel pour les gouvernements et les criminels malveillants qui sont toujours à la recherche de nouvelles victimes. Il existe de véritables marchés pour ce type de données, où les pirates informatiques

vendre des données au plus offrant.


Pour ne rien arranger, les entreprises qui gèrent ces bases de données ont souvent peu d'expérience en matière de protection des données financières ; en fait, beaucoup d'entre elles sont de jeunes start-ups, et nous savons pertinemment que plusieurs fuites ont déjà eu lieu. En voici quelques exemples

[MobiQwik] (https://bitcoinmagazine.com/business/probably-the-largest-kyc-data-leak-in-history-demonstrates-the-importance-of-Bitcoin-privacy) et HubSpot] (https://bitcoinmagazine.com/business/hubspot-security-breach-leaks-Bitcoin-users-data).


Encore une fois, la protection des données contre ce large éventail d'attaques est Hard, et il est probable que vous n'y parviendrez pas totalement. Vous devrez opter pour le compromis entre commodité et protection de la vie privée qui vous convient le mieux.


### Fongibilité


La fongibilité, dans le contexte des monnaies, signifie qu'une pièce est interchangeable avec toute autre pièce de la même monnaie. Cette drôle de

a été brièvement évoquée plus haut dans le chapitre.


Dans l'article dont il est question ici, Gregory Maxwell [déclare] (https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908) :


> La confidentialité financière est un élément essentiel de la fongibilité dans Bitcoin : si vous pouvez distinguer de manière significative une pièce d'une autre, alors leur fongibilité est faible. Si notre fongibilité est trop faible dans la pratique, alors nous ne pouvons pas être décentralisés : si quelqu'un d'important annonce une liste de pièces volées dont il n'acceptera pas les pièces dérivées, vous devez soigneusement vérifier les pièces que vous acceptez par rapport à cette liste et renvoyer celles qui échouent.  Tout le monde est obligé de vérifier les listes noires émises par diverses autorités car, dans ce monde, nous n'aimerions pas nous retrouver avec de mauvaises pièces. Cela ajoute des frictions et des coûts de transaction et rend le Bitcoin moins valable en tant que monnaie.

Il parle ici des dangers liés à l'absence de fongibilité. Supposons que vous ayez une UTXO. L'histoire de cette UTXO peut normalement être retracée sur plusieurs sauts, en s'étendant sur des multitudes de sorties précédentes. Si l'une de ces sorties a été impliquée dans une activité illégale, indésirable ou suspecte, certains destinataires potentiels de votre pièce pourraient la rejeter. Si vous pensez que vos bénéficiaires vérifieront vos pièces par rapport à un service centralisé de liste blanche ou noire, vous commencerez peut-être à vérifier les pièces que vous recevez également, par mesure de sécurité. Il en résulte qu'une mauvaise fongibilité renforcera une fongibilité encore plus mauvaise.


Adam Back et Matt Corallo [ont fait une présentation sur la fongibilité] (https://btctranscripts.com/scalingbitcoin/milan-2016/fungibility-overview/) à Scaling Bitcoin à Milan en 2016. Ils réfléchissaient dans le même sens :


> La fongibilité est nécessaire au fonctionnement de Bitcoin. Si vous recevez des pièces et que vous ne pouvez pas les dépenser, vous commencez à douter de la possibilité de les dépenser. S'il y a des doutes sur les pièces que vous recevez, les gens vont aller voir les services d'altération et vérifier si "ces pièces sont bénies" et ils vont refuser d'échanger. Cela fait passer Bitcoin d'un système décentralisé sans permission à un système centralisé avec permission où vous avez une "reconnaissance de dette" de la part des fournisseurs de listes noires.

Il semble que la protection de la vie privée et la fongibilité aillent de pair. La fongibilité diminuera si le respect de la vie privée est faible, par exemple parce que les pièces provenant de personnes non désirées peuvent être mises sur liste noire. De la même manière, la vie privée sera affaiblie si la fongibilité est faible : s'il existe une liste noire, vous devrez demander aux fournisseurs de la liste noire quelles pièces accepter, révélant ainsi éventuellement votre adresse IP Address, votre adresse électronique Address et d'autres informations sensibles. Ces deux caractéristiques sont si étroitement liées qu'il est impossible de parler de l'une ou l'autre d'entre elles de manière isolée.


### Mesures de protection de la vie privée



Plusieurs techniques ont été mises au point pour aider les gens à se protéger contre les fuites de données personnelles. L'une des plus évidentes est, comme l'a fait remarquer Nakamoto, l'utilisation d'un numéro d'identification unique

pour chaque transaction, mais il en existe plusieurs autres. Nous n'allons pas vous apprendre à devenir un ninja de la protection de la vie privée. Cependant, Bitcoin Q+A propose un [résumé rapide des technologies de protection de la vie privée] (https://bitcoiner.guide/privacytips/), classé en fonction de la façon dont elles doivent être mises en œuvre dans Hard. En le lisant, vous remarquerez que la protection de la vie privée en Bitcoin a souvent à voir avec des choses en dehors de Bitcoin. Par exemple, vous ne devriez pas vous vanter de vos bitcoins, et vous devriez utiliser Tor et VPN.


L'article énumère également certaines mesures directement liées à Bitcoin :


- Full node : Si vous n'utilisez pas votre propre Full node, vous ferez fuir beaucoup d'informations sur votre Wallet vers des serveurs sur Internet. L'utilisation d'un Full node est une excellente première étape.
- Lightning Network : Plusieurs protocoles existent au-dessus du Bitcoin, par exemple le Lightning Network et le Liquid de Blockstream Sidechain.
- CoinJoin : Un moyen pour plusieurs personnes de fusionner leurs transactions en une seule, ce qui rend plus difficile l'analyse en chaîne.


Lors d'un [exposé] (https://btctranscripts.com/breaking-Bitcoin/2019/breaking-Bitcoin-privacy/) à la conférence Breaking Bitcoin, Chris Belcher a donné un exemple pratique intéressant de la manière dont la protection de la vie privée a été améliorée :


> Il s'agissait d'un casino Bitcoin. Les jeux d'argent en ligne ne sont pas autorisés aux États-Unis. Tous les clients de Coinbase qui ont déposé directement sur Bustabit ont vu leurs comptes fermés parce que Coinbase surveillait cette situation. Bustabit a fait plusieurs choses. Il a mis en place un système appelé "change avoidance" (évitement de la monnaie), qui consiste à vérifier si l'on peut construire une transaction qui n'entraîne aucune sortie de monnaie. Cela permet d'économiser les frais Miner et de gêner l'analyse.
>

> Ils ont également importé leurs adresses de dépôt réutilisées, très utilisées, dans joinmarket. À ce stade, les clients de coinbase.com n'ont jamais été bannis. Il semble que le service de surveillance de Coinbase n'ait pas été en mesure d'effectuer l'analyse après cela, de sorte qu'il est possible de casser ces algorithmes.

Il a également mentionné cet exemple, parmi d'autres, sur la [page Vie privée] (https://en.Bitcoin.it/Privacy) du wiki Bitcoin.


Notez qu'il est possible d'améliorer la protection de la vie privée en construisant des systèmes au-dessus de Bitcoin, comme c'est le cas avec Lightning Network :


![image](assets/privacy.webp)


La superposition de couches de Bitcoin peut renforcer la protection de la vie privée


Nous avons noté dans le dernier chapitre que le besoin de confiance ne peut qu'augmenter avec les couches superposées, mais cela ne semble pas être le cas pour la vie privée, qui peut être améliorée ou détériorée arbitrairement dans les couches superposées. Comment cela se fait-il ? Toute Layer placée au-dessus de la Bitcoin, comme l'explique le paragraphe sur l'échelonnement en couches du futur chapitre sur l'échelonnement, doit utiliser occasionnellement les transactions de la On-Chain, sinon elle ne serait pas "placée au-dessus de la Bitcoin". Les couches qui renforcent la confidentialité essaient généralement d'utiliser le moins possible la Layer de base pour minimiser la quantité d'informations révélées.


Il s'agit là de moyens quelque peu techniques d'améliorer votre vie privée. Mais il existe d'autres moyens. Au début de ce chapitre, nous avons dit que Bitcoin est un système pseudonyme. Cela signifie que les utilisateurs de Bitcoin ne sont pas connus par leurs noms réels ou d'autres données personnelles, mais par leurs clés publiques. Une clé publique est un pseudonyme pour un utilisateur, et un utilisateur peut avoir plusieurs pseudonymes. Dans un monde idéal, votre identité personnelle est découplée de vos pseudonymes Bitcoin. Malheureusement, en raison des problèmes de confidentialité décrits dans ce chapitre, ce découplage se dégrade généralement avec le temps.


Pour limiter les risques de divulgation de vos données personnelles, il convient de ne pas les communiquer en premier lieu et de ne pas les confier à des services centralisés, qui constituent de grandes bases de données susceptibles de fuir. Un article de Bitcoin Q+A [explique KYC] (https://bitcoiner.guide/nokyconly/) et les dangers qui en découlent. Il suggère également quelques mesures à prendre pour améliorer votre situation :


> Heureusement, il existe quelques options pour acheter du Bitcoin via des sources sans KYC. Il s'agit d'échanges P2P (peer to peer) où vous négociez directement avec un autre individu et non avec une tierce partie centralisée. Malheureusement, certains vendent d'autres pièces que le Bitcoin, nous vous recommandons donc d'être prudent.

L'article suggère d'éviter d'utiliser les bourses qui exigent un KYC/AML et d'effectuer plutôt des transactions en privé, ou d'utiliser des bourses décentralisées comme [bisq] (https://bisq.network/).


https://planb.network/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04

Pour une lecture plus approfondie des contre-mesures, reportez-vous à l'[article wiki sur la vie privée] (https://en.Bitcoin.it/wiki/Privacy#Methods_for_improving_privacy_.28non-Blockchain.29), à partir de "Méthodes d'amélioration de la vie privée (non-Blockchain)".


### Conclusion sur la protection de la vie privée



La protection de la vie privée est très importante mais Hard à réaliser. Il n'existe pas de solution miracle en matière de protection de la vie privée.


Pour obtenir une protection décente de la vie privée dans Bitcoin, vous devez prendre des mesures actives, dont certaines sont coûteuses et prennent du temps.


## Fini Supply

<chapterId>af125ba2-ef98-5905-8895-41a538fe5ea5</chapterId>



![](assets/finitesupply-banner.webp)


Ce chapitre examine la limite Bitcoin Supply de 21 millions de BTC, ou combien est-elle en réalité ? Nous expliquons comment cette limite est appliquée et ce que l'on peut faire pour vérifier qu'elle est respectée. En outre, nous jetons un coup d'œil dans la boule de cristal et discutons de la dynamique qui entrera en jeu lorsque la Block reward passera d'un système de subventions à un système de redevances.


La fameuse Supply finie de 21 millions de BTC est considérée comme une propriété fondamentale de la Bitcoin. Mais est-elle vraiment gravée dans le marbre ?


Commençons par examiner ce que les règles de consensus actuelles disent à propos de la Supply de la Bitcoin, et combien de celle-ci sera réellement utilisable. Pieter Wuille a écrit un article à ce sujet [sur la pile Exchange] (https://Bitcoin.stackexchange.com/a/38998/69518), dans lequel il a compté le nombre de bitcoins qu'il y aurait une fois que toutes les pièces auraient été extraites :


> Si vous additionnez tous ces chiffres, vous obtenez 20999999.9769 BTC.

Mais pour un certain nombre de raisons, telles que les premiers problèmes liés aux transactions Coinbase, les mineurs qui réclament involontairement moins que ce qui est autorisé, et la perte de clés privées, cette limite supérieure ne sera jamais atteinte. Wuille conclut :


> Il nous reste donc 20999817.31308491 BTC (en tenant compte de tout ce qui a été fait jusqu'au bloc 528333)

Cependant, plusieurs portefeuilles ont été perdus ou volés, des transactions ont été envoyées au mauvais Address, des personnes ont oublié qu'elles possédaient un Bitcoin. Le total de ces pertes pourrait bien se chiffrer en millions. Des personnes ont essayé de comptabiliser les pertes connues [ici] (https://bitcointalk.org/index.php?topic=7253.0).


Ce qui nous laisse avec : ? ?? BTC.


Nous pouvons donc être sûrs que le Bitcoin Supply sera 20999817.31308491 BTC au maximum. Toute pièce perdue ou brûlée de manière non vérifiable fera baisser ce chiffre, mais nous ne savons pas de combien. Ce qui est intéressant, c'est que cela n'a pas vraiment d'importance, ou mieux encore, que cela a une importance positive pour les détenteurs de Bitcoin,

[tel qu'expliqué] (https://bitcointalk.org/index.php?topic=198.msg1647#msg1647) par Satoshi Nakamoto :


> Les pièces perdues ne font qu'augmenter la valeur des pièces des autres.  Considérez cela comme un don à tout le monde.

Les réserves limitées de Supply vont se réduire, ce qui devrait, du moins en théorie, entraîner une déflation des prix.


Plus que le nombre exact de pièces en circulation, c'est la façon dont la limite Supply est appliquée sans aucune autorité centrale qui est importante. Alias chytrik le dit bien sur [Stack Exchange] (https://Bitcoin.stackexchange.com/a/106830/69518) :


> La réponse est donc que vous n'avez pas à faire confiance à quelqu'un pour ne pas augmenter la Supply. Il suffit d'exécuter un code qui vérifiera qu'il ne l'a pas fait.

Même si certains nœuds complets passent du côté obscur et décident d'accepter des blocs contenant des transactions coinbase de plus grande valeur, tous les nœuds complets restants les négligeront simplement et continueront à faire des affaires comme d'habitude. Certains nœuds complets peuvent, intentionnellement ou non, exécuter des logiciels malveillants, mais le collectif sécurisera solidement le Blockchain. En conclusion, vous pouvez choisir de faire confiance au système sans avoir à faire confiance à qui que ce soit.


### Subvention de bloc et frais de transaction



La Block reward se compose de la subvention de bloc et des frais de transaction. La Block reward doit couvrir les coûts de sécurité de la Bitcoin. Nous pouvons affirmer avec certitude que dans les conditions actuelles, en ce qui concerne la subvention des blocs, les frais de transaction, le prix de la Bitcoin, la taille de la Mempool, la puissance de la Hash, le degré de décentralisation, etc., les incitations pour chaque acteur à respecter les règles sont suffisamment élevées pour préserver un système monétaire sûr.


Que se passe-t-il lorsque la subvention globale s'approche de zéro ? Pour simplifier les choses, supposons qu'elle soit effectivement égale à zéro. À ce stade, le coût de la sécurité du système est couvert uniquement par les frais de transaction. Nous ne pouvons pas savoir ce que l'avenir nous réserve à ce moment-là. Les facteurs d'incertitude sont nombreux et nous en sommes réduits à des spéculations. Par exemple, la contribution de Paul Sztorc à ce sujet [dans son blog Truthcoin] (https://www.truthcoin.info/blog/security-budget/) est principalement constituée de spéculations, mais il a au moins un point solide (veuillez noter que M2, tel que mentionné par Sztorc, est une mesure d'une monnaie fiduciaire Supply) :


> Alors que les deux sont mélangés dans le même "budget de sécurité", la subvention globale et les frais fiscaux sont totalement et complètement différents. Elles sont aussi différentes l'une de l'autre que "les bénéfices totaux de VISA en 2017" le sont de "l'augmentation totale de M2 en 2017".

Aujourd'hui, ce sont les détenteurs qui paient pour la sécurité (via l'inflation monétaire). Demain, ce sera au tour des dépensiers d'assumer en quelque sorte ce fardeau, comme illustré ci-dessous.


![image](assets/finitesupply.webp)


Au fil du temps, la prise en charge des coûts de sécurité se déplacera des détenteurs vers les dépensiers


Lorsque les frais de transaction sont la principale motivation de la Mining, les incitations changent. Notamment, si la Mempool d'une Miner ne contient pas assez de frais de transaction, il peut devenir plus rentable pour cette Miner de réécrire l'histoire de la Bitcoin plutôt que de la prolonger. Bitcoin Optech a une [section sur ce comportement] (https://bitcoinops.org/en/topics/fee-sniping/), appelée *fee sniping*, écrite par David Harding :


> Le "fee sniping" est un problème qui peut survenir lorsque la subvention de Bitcoin continue à diminuer et que les frais de transaction commencent à dominer les récompenses des blocs de Bitcoin. Si les frais de transaction sont tout ce qui compte, alors une Miner avec `x` pour cent du taux de Hash a `x` pour cent de chance de Mining le bloc suivant, donc la valeur attendue pour eux de Mining honnêtement est `x` pour cent de la [meilleure série de transactions] (https://bitcoinops.org/en/newsletters/2021/06/02/#candidate-set-based-csb-block-template-construction) dans leur Mempool.
>

> Alternativement, une Miner pourrait tenter malhonnêtement de re-mine le bloc précédent plus un tout nouveau bloc pour étendre la chaîne. Ce comportement est connu sous le nom de fee sniping, et la probabilité que la Miner malhonnête y parvienne si toutes les autres Miner sont honnêtes est de `(x/(1-x))^2`. Même si le fee sniping a une probabilité de succès globalement plus faible que l'honnête Mining, tenter la Mining malhonnête pourrait être le choix le plus rentable si les transactions du bloc précédent ont payé des taux significativement plus élevés que les transactions actuellement dans la Mempool - une petite chance pour un gros montant peut valoir plus qu'une grande chance pour un petit montant.

Si les mineurs commencent à pratiquer le sniping, cela incitera d'autres mineurs à faire de même, ce qui réduira encore le nombre de mineurs honnêtes. Cela pourrait gravement nuire à la sécurité globale de Bitcoin. Harding poursuit en énumérant quelques contre-mesures qui peuvent être prises, comme le fait de s'appuyer sur des verrous de temps de transaction pour limiter l'endroit où la transaction peut apparaître dans la Blockchain.


Ainsi, étant donné que le consensus sur la Supply finie demeure, la subvention des blocs - grâce à [BIP42](https://github.com/Bitcoin/bips/blob/master/bip-0042.mediawiki) qui a corrigé un bug d'inflation à très long terme - atteindra zéro aux alentours de l'année 2140. Les frais de transaction seront-ils alors suffisants pour sécuriser le réseau ?


Il est impossible de le dire, mais nous savons certaines choses :


- Un siècle est une période *longue* du point de vue de Bitcoin. S'il existe toujours, il aura probablement énormément évolué.
- Si une majorité économique écrasante juge nécessaire de changer les règles et d'introduire, par exemple, une inflation monétaire annuelle perpétuelle de 0,1 % ou 1 %, la Supply de la Bitcoin ne sera plus finie.
- Avec une subvention de bloc nulle et une Mempool vide ou presque vide, la situation peut devenir précaire en raison des pressions exercées sur les tarifs.


Étant donné que la transition vers une Block reward payante est si lointaine, il serait peut-être sage de ne pas tirer de conclusions hâtives et d'essayer de résoudre les problèmes potentiels pendant que nous le pouvons. Par exemple, Peter Todd pense qu'il existe un risque réel que le budget de sécurité de la Bitcoin ne soit pas suffisant à l'avenir, et plaide donc en faveur d'une légère inflation perpétuelle dans la Bitcoin. Cependant, il pense également que ce n'est pas une bonne idée de discuter d'un tel problème à l'heure actuelle, comme [il l'a dit sur le podcast What Bitcoin Did] (https://www.whatbitcoindid.com/podcast/peter-todd-on-the-essence-of-Bitcoin) :


> Mais c'est un risque qui se situe dans 10 ou 20 ans. C'est très long. Et d'ici là, qui peut bien savoir quels sont les risques ?

Nous pourrions peut-être considérer Bitcoin comme quelque chose d'organique. Imaginez un petit chêne à croissance lente. Imaginez également que vous n'avez jamais vu un arbre adulte de votre vie. Ne serait-il pas judicieux de limiter vos problèmes de contrôle au lieu d'établir à l'avance toutes les règles sur la façon dont cette plante devrait être autorisée à évoluer et à grandir ?


### Conclusion sur la Supply finie



Nous ne pouvons pas dire aujourd'hui si la Bitcoin Supply dépassera les 21 millions d'habitants, et ce n'est probablement pas si mal. Il est crucial, mais pas urgent, de veiller à ce que le budget de la sécurité reste suffisamment élevé. Reprenons cette discussion dans 10 à 50 ans, lorsque nous en saurons plus. Si c'est toujours d'actualité.


# Bitcoin Gouvernance

<partId>411bf53f-af4b-50f1-b71b-e40fe3ff64b7</partId>


## Mise à niveau

<chapterId>3ffa84d1-adfa-5fbc-9b13-384ea783fcdd</chapterId>



![](assets/upgrading-banner.webp)


Il peut être extrêmement difficile de mettre à jour Bitcoin en toute sécurité. Certains changements prennent plusieurs années à se mettre en place. Dans ce chapitre, nous abordons le vocabulaire commun relatif à la mise à niveau de la Bitcoin et explorons quelques exemples de mises à niveau historiques de son protocole, ainsi que les enseignements que nous en avons tirés. Enfin, nous aborderons la question du fractionnement des chaînes, ainsi que les risques et les coûts qui y sont liés.


Pour vous mettre au diapason de ce chapitre, nous vous conseillons de lire [l'article de David Harding sur l'harmonie et la discorde] (https://bitcointalk.org/dec/p1.html) :


> Les experts Bitcoin parlent souvent de consensus, dont le sens est abstrait et Hard difficile à cerner. Mais le mot consensus vient du mot latin concentus, "une harmonie chantée ensemble", alors ne parlons pas de Bitcoin consensus mais de Bitcoin harmonie.
>

> C'est l'harmonie qui permet à Bitcoin de fonctionner. Des milliers de nœuds complets travaillent chacun indépendamment pour vérifier que les transactions qu'ils reçoivent sont valides, produisant un accord harmonieux sur l'état de la Bitcoin Ledger sans qu'aucun opérateur de nœud n'ait besoin de faire confiance à quelqu'un d'autre. C'est un peu comme un chœur où chaque membre chante la même chanson en même temps pour produire quelque chose de bien plus beau que ce que chacun d'entre eux pourrait produire seul.
>

> Le résultat de l'harmonie Bitcoin est un système dans lequel les bitcoins sont à l'abri non seulement des petits voleurs (à condition que vous gardiez vos clés en sécurité), mais aussi d'une inflation sans fin, d'une confiscation massive ou ciblée, ou tout simplement du marasme bureaucratique qu'est le système financier existant.

Ce chapitre traite de la manière dont Bitcoin peut être mis à niveau sans provoquer de discorde. Rester en harmonie, c'est-à-dire maintenir le consensus, est en effet l'un des plus grands défis du développement de Bitcoin. Les mécanismes de mise à niveau comportent de nombreuses nuances, que l'on peut mieux comprendre en étudiant des cas concrets de mises à niveau antérieures. C'est pourquoi ce chapitre met l'accent sur des exemples historiques et commence par préparer le terrain avec un vocabulaire utile.


### Vocabulaire



Selon Wikipédia, la [compatibilité ascendante] (https://en.wikipedia.org/wiki/Forward_compatibility) désigne la situation dans laquelle un ancien logiciel peut traiter des données créées par des logiciels plus récents, en ignorant les parties qu'il ne comprend pas :


Une norme assure la compatibilité ascendante si un produit conforme aux versions antérieures peut traiter "gracieusement" des données conçues pour des versions ultérieures de la norme, en ignorant les nouvelles parties qu'il ne comprend pas.


À l'inverse, la [compatibilité ascendante] (https://en.wikipedia.org/wiki/Backward_compatibility) désigne le fait que les données d'un ancien logiciel sont utilisables avec des logiciels plus récents. On dit d'une modification qu'elle est pleinement compatible si elle est à la fois compatible en amont et en aval.


Une modification des règles de consensus de Bitcoin est dite *Soft Fork* si elle est entièrement compatible. C'est la façon la plus courante de mettre à jour Bitcoin, pour un certain nombre de raisons que nous aborderons plus loin dans ce chapitre. Si une modification des règles de consensus Bitcoin est compatible avec le passé mais pas avec l'avenir, elle est appelée *Hard Fork*.


Pour un aperçu technique des fourches Soft et Hard, veuillez lire le [chapitre 11 de Grokking Bitcoin] (https://rosenbaum.se/book/grokking-Bitcoin-11.html). Il explique ces termes et aborde également les mécanismes de mise à niveau. Il est recommandé, mais pas strictement nécessaire, de se familiariser avec ces notions avant de poursuivre la lecture.


### Améliorations historiques



Le bloc Bitcoin n'est plus le même aujourd'hui qu'au moment de la création du bloc Genesis. Plusieurs améliorations ont été apportées au fil des ans. En 2018, Eric Lombrozo [s'est exprimé lors de la conférence Breaking Bitcoin] (https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) sur les différents mécanismes de mise à niveau de Bitcoin, soulignant à quel point ils ont évolué au fil du temps. Il a même expliqué comment Satoshi Nakamoto a une fois mis à niveau Bitcoin par le biais d'un Hard Fork :


> Il y avait en fait un Hard-Fork dans Bitcoin que Satoshi a fait et que nous ne ferions jamais de cette façon - c'est une assez mauvaise façon de le faire. Si vous regardez la description du commit git ici [[757f076](https://github.com/Bitcoin/Bitcoin/commit/757f0769d8360ea043f469f3a35f6ec204740446)], il dit quelque chose à propos de makefile.unix wx-config version 0.3.6. C'est exact. C'est tout ce qu'il dit. Il n'y a aucune indication qu'il y a un changement de rupture. Il l'a en fait caché là-dedans. Il a également [posté sur bitcointalk](https://bitcointalk.org/index.php?topic=626.msg6451#msg6451) et a dit, s'il vous plaît mettez à jour vers 0.3.6 ASAP. Nous avons corrigé un bug d'implémentation où il est possible que de fausses transactions soient affichées comme acceptées. N'acceptez pas de paiements Bitcoin tant que vous n'êtes pas passé à la version 0.3.6. Si vous ne pouvez pas mettre à jour tout de suite, il serait préférable d'arrêter votre nœud Bitcoin jusqu'à ce que vous le fassiez. Et en plus de cela, je ne sais pas pourquoi il a décidé de faire cela, il a décidé d'ajouter des optimisations dans le même code. Corriger un bug et ajouter des optimisations.

Il souligne que, intentionnellement ou non, cette Hard Fork a créé des opportunités pour de futurs forks Soft, à savoir les opérateurs de script (opcodes) OP_NOP1-OP_NOP10. Nous examinerons plus en détail ce changement de code dans le document cve-2010-5141. Ces opcodes ont été utilisés pour deux forks Soft jusqu'à présent :


- [BIP65](https://github.com/Bitcoin/bips/blob/master/bip-0065.mediawiki) (OP_CHECKLOCKTIMEVERIFY)
- [BIP113](https://github.com/Bitcoin/bips/blob/master/bip-0112.mediawiki) (OP_SEQUENCEVERIFY).


M. Lombrozo donne également un aperçu de l'évolution des mécanismes de mise à niveau au fil des ans, jusqu'en 2017. Depuis lors, seule une autre mise à niveau majeure, la Taproot, a été déployée. Le processus long et quelque peu chaotique qui a conduit à son activation nous a permis de mieux comprendre les mécanismes d'amélioration du Bitcoin.


#### Mise à niveau du SegWit



Alors que toutes les mises à niveau précédant SegWit avaient été plus ou moins indolores, celle-ci était différente. Lorsque le code d'activation de la SegWit a été publié, en octobre 2016, les utilisateurs de la Bitcoin semblaient la soutenir massivement, mais pour une raison quelconque, les mineurs n'ont pas signalé leur soutien à cette mise à niveau, ce qui a bloqué l'activation sans qu'aucune solution ne soit en vue.


Aaron van Wirdum décrit ce chemin sinueux dans son article du magazine Bitcoin [The Long Road To SegWit] (https://bitcoinmagazine.com/technical/the-long-road-to-SegWit-how-bitcoins-biggest-protocol-upgrade-became-reality). Il commence par expliquer ce qu'est la SegWit et comment elle s'inscrit dans le débat sur la taille des blocs. M. Van Wirdum décrit ensuite la tournure des événements qui ont conduit à son activation finale. Au centre de ce processus se trouvait un mécanisme de mise à niveau appelé *user activated Soft Fork*, ou UASF en abrégé, proposé par l'utilisateur Shaolinfry :


> Shaolinfry a proposé une alternative : une Soft Fork activée par l'utilisateur (UASF). Au lieu de l'activation de la Hash, une Soft Fork activée par l'utilisateur aurait une "activation du jour du drapeau" où les nœuds commencent à appliquer la loi à un moment prédéterminé dans le futur Tant qu'un tel UASF est appliqué par une majorité économique, il devrait contraindre une majorité de mineurs à suivre (ou à activer) la Soft Fork.

Entre autres choses, il cite le courriel de Shaolinfry à la liste de diffusion Bitcoin-dev. À cette occasion, Shaolinfry [s'est prononcé contre les forks Miner et Soft activés] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-February/013643.html), en énumérant un certain nombre de problèmes qu'ils posent :


> Tout d'abord, il faut faire confiance à la puissance de la Hash pour qu'elle soit validée après l'activation.  Dans le cas du BIP66 Soft Fork, 95 % de la Hashrate signalait qu'elle était prête, mais en réalité, environ la moitié ne validait pas les règles mises à jour et exploitait par erreur un bloc non valide.
>

> Deuxièmement, la signalisation Miner a un veto naturel qui permet à un petit pourcentage de Hashrate d'empêcher l'activation du nœud de la mise à niveau pour tout le monde. Jusqu'à présent, les forks Soft ont profité du paysage relativement centralisé de Mining où il y a relativement peu de pools Mining qui construisent des blocs valides ; au fur et à mesure que nous nous dirigeons vers une plus grande décentralisation de Hashrate, il est probable que nous souffrirons de plus en plus de " l'inertie des mises à niveau " qui mettra son veto à la plupart des mises à niveau.

Shaolinfry a également attiré l'attention sur une mauvaise interprétation courante de la signalisation Miner : les gens pensaient généralement qu'il s'agissait d'un moyen par lequel les mineurs pouvaient décider des mises à niveau du protocole, plutôt que d'une action qui aidait à coordonner les mises à niveau. En raison de ce malentendu, les mineurs ont pu se sentir obligés de proclamer publiquement leur opinion sur une certaine Soft Fork, comme si cela donnait du poids à la proposition.


La proposition de l'UASF consiste, en résumé, en un "jour du drapeau" au cours duquel les nœuds commencent à appliquer de nouvelles règles spécifiques. De cette façon, les mineurs n'ont pas besoin de faire un effort collectif pour coordonner la mise à niveau, mais *peuvent* déclencher l'activation avant le jour du drapeau si suffisamment de blocs signalent leur soutien :


> Ma suggestion est d'avoir le meilleur des deux mondes. Étant donné qu'une Soft Fork activée par l'utilisateur nécessite un délai relativement long avant l'activation, nous pouvons la combiner avec le BIP9 pour offrir l'option d'une activation plus rapide Hash coordonnée par le pouvoir ou d'une activation par le jour du drapeau, selon ce qui est le plus tôt.
> Dans les deux cas, nous pouvons exploiter les systèmes d'alerte du BIP9. La modification est relativement simple : il s'agit d'ajouter un paramètre de temps d'activation qui fera passer l'état BIP9 à LOCKED_IN avant la fin du délai de déploiement du BIP9.

Cette idée a suscité beaucoup d'intérêt, mais n'a pas semblé faire l'unanimité, ce qui a fait craindre une rupture potentielle de la chaîne. L'article d'Aaron van Wirdum explique comment ce problème a finalement été résolu grâce à [BIP91] (https://github.com/Bitcoin/bips/blob/master/bip-0091.mediawiki), dont l'auteur est James Hilliard :


> Hilliard a proposé une solution un peu complexe mais intelligente qui rendrait tout compatible : L'activation séparée des témoins, telle que proposée par l'équipe de développement du Bitcoin Core, le BIP148 UASF et le mécanisme d'activation de l'Accord de New York. Son BIP91 pourrait permettre à la Bitcoin de rester entière - au moins jusqu'à l'activation de la SegWit.

Le BIP a dû prendre en considération d'autres facteurs de complication (par exemple, l'accord dit "de New York"). Nous vous encourageons à lire l'article de Van Wirdum dans son intégralité pour découvrir les nombreux détails intéressants de cette histoire.


#### Discussion post-SegWit


Après le déploiement de SegWit, une discussion sur les mécanismes de déploiement a émergé. Comme l'ont noté Eric Lombrozo dans [son exposé à la conférence Breaking Bitcoin] (https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) et Shaolinfry, une Miner activée Soft Fork n'est pas le mécanisme de mise à niveau idéal :


> À un moment donné, nous voudrons probablement ajouter d'autres fonctionnalités au protocole Bitcoin. C'est une grande question philosophique que nous nous posons. Faisons-nous un UASF pour le prochain ? Pourquoi pas une approche hybride ? La Miner activée en tant que telle a été exclue. Nous n'utiliserons plus le bip9.

En janvier 2020, Matt Corallo [a envoyé un courriel](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2020-January/017547.html) à la liste de diffusion Bitcoin-dev qui a lancé une discussion sur les futurs mécanismes de déploiement Soft Fork. Il a énuméré cinq objectifs qu'il jugeait essentiels dans une mise à niveau. David Harding [les résume dans un bulletin d'information d'Optech sur le Bitcoin](https://bitcoinops.org/en/newsletters/2020/01/15/#discussion-of-Soft-Fork-activation-mechanisms) comme suit :


> La possibilité d'interrompre le processus en cas d'objection sérieuse aux modifications des règles consensuelles proposées . L'allocation d'un délai suffisant après la publication du logiciel mis à jour pour s'assurer que la plupart des nœuds économiques sont mis à niveau pour appliquer ces règles . L'espoir que le taux de Hash du réseau sera à peu près le même avant et après le changement, ainsi que pendant toute transition . La prévention, dans la mesure du possible, de la création de blocs qui ne sont pas valides en vertu des nouvelles règles, ce qui pourrait entraîner de fausses confirmations dans les nœuds non mis à niveau et les clients SPV . L'assurance que les mécanismes d'annulation ne peuvent pas être utilisés à mauvais escient par des "griefers" ou des partisans pour empêcher une mise à niveau largement souhaitée et sans problème connu

Ce que Corallo propose est une combinaison d'une Miner activée Soft Fork et d'une Soft Fork activée par l'utilisateur :


> Ainsi, pour être un peu plus concret, je pense qu'une méthode d'activation qui créerait un bon précédent et prendrait en compte de manière appropriée les objectifs susmentionnés serait la suivante :
>

> 1) un déploiement standard du BIP 9 avec un horizon temporel d'un an pour
activation avec 95% de préparation Miner, +

> 2) si aucune activation n'a lieu dans un délai d'un an, un délai de six mois est accordé pour la mise en œuvre de l'accord
période de calme pendant laquelle la communauté peut analyser et discuter

les raisons de l'absence d'activation et, +

> 3) dans le cas où cela se justifie, un simple paramètre de ligne de commande/Bitcoin.conf pris en charge depuis la version initiale du déploiement permettrait aux utilisateurs d'opter pour un déploiement BIP 8 avec un horizon temporel de 24 mois pour l'activation du jour du drapeau (ainsi que pour une nouvelle version de Bitcoin Core activant le drapeau de manière universelle).
>

> Cela permet de disposer d'un horizon temporel très long pour une activation plus standard, tout en garantissant que les objectifs du point 5 sont atteints, même si, dans ces cas, l'horizon temporel doit être considérablement prolongé pour atteindre les objectifs du point 3. Le développement du Bitcoin n'est pas une course. S'il le faut, attendre 42 mois permet de ne pas créer un précédent négatif que nous regretterons au fur et à mesure que Bitcoin se développera.

#### Taproot upgrade - Procès accéléré



Lorsque Taproot a été prêt à être déployé en octobre 2020, c'est-à-dire lorsque tous les détails techniques relatifs aux règles de consensus ont été mis en œuvre et ont été largement approuvés par la communauté, les discussions sur la manière de le déployer ont commencé à s'intensifier. Jusqu'alors, ces discussions étaient restées assez discrètes.


De nombreuses propositions de mécanismes d'activation ont commencé à circuler, et David Harding

(résumé sur le wiki Bitcoin) (https://en.Bitcoin.it/wiki/Taproot_activation_proposals). Dans son article, il explique certaines propriétés du BIP8 qui, à l'époque, avait fait l'objet de modifications récentes visant à le rendre plus flexible.


> Au moment de la rédaction du présent document, [BIP8] (https://github.com/Bitcoin/bips/blob/master/bip-0008.mediawiki) a été rédigé sur la base des enseignements tirés en 2017. Un changement notable suite aux BIP 9+148 est que l'activation forcée est désormais basée sur la hauteur du bloc plutôt que sur le temps médian passé ; un second changement notable est que l'activation forcée est un paramètre booléen choisi lorsque les paramètres d'activation d'un Soft Fork sont définis soit pour le déploiement initial, soit mis à jour lors d'un déploiement ultérieur.

Le BIP8 sans activation forcée est très similaire aux bits de la version [BIP9](https://github.com/Bitcoin/bips/blob/master/bip-0009.mediawiki) avec délai d'attente et retard, la seule différence significative étant l'utilisation par le BIP8 des hauteurs de blocs par rapport à l'utilisation par le BIP9 du temps médian écoulé. Ce paramètre permet à la tentative d'échouer (mais elle peut être réessayée plus tard).


Le BIP8 avec activation forcée se termine par une période de signalisation obligatoire au cours de laquelle tous les blocs produits conformément à ses règles doivent signaler qu'ils sont prêts pour la Soft Fork d'une manière qui déclenchera l'activation dans un déploiement antérieur de la même Soft Fork avec une activation non obligatoire. En d'autres termes, si la version x du nœud est publiée sans activation forcée et que, plus tard, la version y est publiée et oblige les mineurs à commencer à signaler qu'ils sont prêts dans le même délai, les deux versions commenceront à appliquer les nouvelles règles de consensus en même temps.


Cette flexibilité de la proposition révisée du BIP8 permet d'exprimer d'autres idées en termes de ce à quoi elles ressembleraient en utilisant le BIP8. Cela permet de disposer d'un facteur commun à utiliser pour classer de nombreuses propositions différentes.


À partir de là, les discussions sont devenues très animées, notamment sur la question de savoir si `lockinontimeout` devait être `true` (comme dans un Soft Fork activé par l'utilisateur, appelé "BIP8 avec activation forcée" par Harding) ou `false` (comme dans un Miner activé Soft Fork, appelé "BIP8 sans activation forcée" par Harding).


Parmi les propositions énumérées, l'une d'entre elles était intitulée "Voyons ce qui se passe". Pour une raison ou une autre, cette proposition n'a pas eu beaucoup d'écho jusqu'à sept mois plus tard.


Pendant ces sept mois, la discussion s'est poursuivie et il semblait qu'il n'y avait aucun moyen de parvenir à un large consensus sur le mécanisme de déploiement à utiliser. Il y avait principalement deux camps : l'un qui préférait `lockinontimeout=true` (les partisans de l'UASF) et l'autre qui préférait `lockinontimeout=false` (les partisans du "essayez et si ça ne marche pas, repensez-y"). Comme il n'y avait pas de soutien massif pour l'une ou l'autre de ces options, le débat tournait en rond sans qu'il y ait apparemment de solution. Certaines de ces discussions ont eu lieu sur IRC, dans un canal appelé ##Taproot-activation, mais [le 5 mars 2021] (https://gnusha.org/Taproot-activation/2021-03-05.log), quelque chose a changé :


```
06:42 < harding> roconnor: is somebody proposing BIP8(3m, false)?  I mentioned that the other day but I didn't see any responses.
[...]
06:43 < willcl_ark_> Amusingly, I was just thinking to myself that, vs this, the SegWit activation was actually pretty straightforward: simply a LOT=false and if it fails a UASF.
06:43 < maybehuman> it's funny, "let's see what happens" (i.e. false, 3m) was a poular choice right at the beginning of this channel iirc
06:44 < roconnor> harding: I think I am.  I don't know how much that is worth.  Mostly I think it would be a widely acceptable configuration based on my understanding of everyone's concerns.
06:44 < willcl_ark_> maybehuman: becuase everybody actually wants this, even miners reckoned they could upgrade in about two weeks (or at least f2pool said that)
06:44 < roconnor> harding: BIP8(3m,false) with an extended lockin-period.
06:45 < harding> roconnor: oh, good.  It's been my favorite option since I first summarized the options on the wiki like seven months ago.
06:45 <@michaelfolkson> UASF wouldn't release (true,3m) but yeah Core could release (false, 3m)
06:45 < willcl_ark_> harding: It certainly seems like a good approach to me. _if_ that fails, then you can try an understand why, without wasting too much time
```


L'approche "voyons ce qui se passe" a finalement semblé s'imposer dans l'esprit des gens. Ce processus sera plus tard qualifié de "procès rapide" en raison de la brièveté de la période de signalisation. David Harding explique cette idée à l'ensemble de la communauté dans un

[email à la liste de diffusion Bitcoin-dev] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-March/018583.html) :

> La version précédente de cette proposition a été documentée il y a plus de 200 jours et le code sous-jacent de Taproot a été fusionné dans Bitcoin Core il y a plus de 140 jours. Si nous avions démarré Speedy Trial au moment où Taproot a été fusionné (ce qui est un peu irréaliste), nous serions à moins de deux mois de Taproot ou nous serions passés à la tentative d'activation suivante il y a plus d'un mois.
>

> Au lieu de cela, nous avons longuement débattu et ne semblons pas plus proches de ce que je pense être une solution largement acceptable que lorsque la liste de diffusion a commencé à discuter des schémas d'activation post-SegWit il y a plus d'un an. Je pense que Speedy Trial est un moyen de generate progresser rapidement qui mettra fin au débat (pour l'instant, si l'activation est réussie) ou nous donnera des données réelles sur lesquelles baser les futures propositions d'activation de Taproot.

Ce mécanisme de déploiement a été affiné pendant deux mois, puis publié dans [Bitcoin Core version 0.21.1] (https://github.com/Bitcoin/Bitcoin/blob/master/doc/release-notes/release-notes-0.21.1.md#Taproot-Soft-Fork). Les mineurs ont rapidement commencé à signaler cette mise à niveau en faisant passer l'état de déploiement à `LOCKED_IN`, et après une période de grâce, les règles Taproot ont été activées à la mi-novembre 2021 dans le bloc [709632] (https://Mempool.space/block/0000000000000000000687bca986194dc2c1f949318629b44bb54ec0a94d8244).


#### Mécanismes de déploiement futurs


Etant donné les problèmes rencontrés avec les récents forks Soft, SegWit et Taproot, il n'est pas évident de savoir comment la prochaine mise à jour sera déployée. Speedy Trial a été utilisé pour déployer Taproot, mais il a été utilisé pour combler le fossé entre les foules de l'UASF et de la MASF, et non parce qu'il s'est imposé comme le mécanisme de déploiement le plus connu.


### Risques


Lors de l'activation d'une Fork, qu'il s'agisse d'une Hard ou d'une Soft, d'une Miner activée ou d'une activation par l'utilisateur, il existe un risque de rupture durable de la chaîne. Une scission qui dure plus de quelques blocs peut causer de graves dommages au sentiment autour de la Bitcoin ainsi qu'à son prix. Mais surtout, il en résulterait une grande confusion sur ce qu'est la Bitcoin. La Bitcoin est-elle cette chaîne ou cette chaîne ?


Le risque d'une Soft Fork activée par l'utilisateur est que les nouvelles règles soient activées même si la majorité du pouvoir Hash ne les soutient pas. Ce scénario entraînerait une rupture durable de la chaîne, qui persisterait jusqu'à ce que la majorité de la puissance Hash adopte les nouvelles règles. Il pourrait être particulièrement intéressant pour la Hard d'inciter les mineurs à passer à la nouvelle chaîne s'ils ont déjà extrait des blocs après la scission sur l'ancienne chaîne, car en changeant de branche, ils abandonneraient les récompenses de leurs propres blocs. Toutefois, il convient de mentionner un épisode remarquable : en mars 2013, une scission de longue durée s'est produite en raison d'une Hard Fork involontaire et, contrairement à cette incitation, deux grands pools Mining ont pris la décision d'abandonner leur branche de la scission afin de rétablir le consensus.


D'autre part, le risque d'une Miner activée Soft Fork est dû au fait que les mineurs peuvent émettre de faux signaux, ce qui signifie que la part réelle de la puissance Hash qui soutient le changement pourrait être plus petite qu'il n'y paraît. Si le soutien réel ne représente pas une majorité de la puissance de la Hash, nous assisterons probablement à une scission en chaîne durable similaire à celle décrite dans le paragraphe précédent. Ce problème, ou du moins un problème similaire, s'est déjà produit dans la réalité lorsque le BIP66 a été déployé, mais il a été résolu en l'espace de 6 blocs environ.


#### Coûts d'une scission



Jimmy Song [a parlé des coûts associés aux fourches Hard] (https://btctranscripts.com/breaking-Bitcoin/2017/socialized-costs-of-Hard-forks/) lors du Breaking Bitcoin à Paris, mais une grande partie de ce qu'il a dit s'applique également à une rupture de chaîne due à une Soft Fork défaillante. Il a parlé des *externalités négatives* et les a définies comme le prix que quelqu'un d'autre doit payer pour vos propres actions :


> L'exemple classique d'une externalité négative est celui d'une usine. Il s'agit peut-être d'une raffinerie de pétrole qui produit un bien qui est bon pour l'économie, mais qui produit également quelque chose qui constitue une externalité négative, comme la pollution. Ce n'est pas seulement quelque chose que tout le monde doit payer, nettoyer ou subir. Mais il y a aussi des effets de deuxième et troisième ordre, comme l'augmentation de la circulation vers l'usine en raison de l'augmentation du nombre de travailleurs qui doivent s'y rendre. Il se peut aussi que vous mettiez en danger la faune et la flore des environs. Ce n'est pas tout le monde qui doit payer pour les externalités négatives, il peut s'agir de personnes spécifiques, comme les personnes qui utilisaient auparavant cette route ou les animaux qui se trouvaient à proximité de l'usine, et qui paient également pour le coût de l'usine.

Dans le contexte de la Bitcoin, il illustre les externalités négatives en utilisant Bitcoin Cash (bcash), qui est une Hard Fork de la Bitcoin créée peu avant cette conférence en 2017. Il classe les externalités négatives d'une Hard Fork en coûts ponctuels et en coûts permanents.


Parmi les nombreux exemples de coûts non récurrents, il cite ceux encourus par les échanges :


> Nous avons donc un certain nombre d'échanges et ils ont dû faire face à de nombreux coûts ponctuels. La première chose qui s'est produite, c'est que les dépôts et les retraits ont dû être interrompus pendant un jour ou deux pour ces bourses parce qu'elles ne savaient pas ce qui allait se passer. Nombre de ces bourses ont dû puiser dans les réserves de Cold parce que leurs utilisateurs demandaient de la bcash. Cela fait partie de leurs obligations fiduciaires. Il faut également auditer le nouveau logiciel. C'est quelque chose que nous avons dû faire chez itbit. Nous voulons dépenser de l'argent liquide - comment faire ? Nous devons télécharger electron cash ? Y a-t-il des logiciels malveillants ? Nous devons procéder à un audit. Nous avons eu environ 10 jours pour déterminer si c'était bon ou pas. Ensuite, il faut décider si l'on va se contenter d'autoriser un retrait unique ou si l'on va inscrire cette nouvelle pièce sur la liste Il n'est pas facile pour une Exchange d'inscrire une nouvelle pièce, il y a toutes sortes de nouvelles procédures pour le stockage, la signature, les dépôts et les retraits de la Cold. On peut aussi se contenter d'un événement ponctuel où l'on donne la monnaie à un moment donné et où l'on n'y pense plus. Mais cela pose aussi des problèmes. Enfin, quelle que soit la façon dont vous procédez, retrait ou inscription, vous aurez besoin d'une nouvelle infrastructure pour travailler avec cette token, même s'il s'agit d'un retrait unique. Vous avez besoin d'un moyen de donner ces jetons à vos utilisateurs. Encore une fois, le préavis est court. C'est ça ? Pas le temps de faire ça, il faut faire vite.

Il énumère également les coûts ponctuels supportés par les commerçants, les processeurs de paiement, les portefeuilles, les mineurs et les utilisateurs, ainsi que certains coûts permanents, tels que la perte de confidentialité et le risque accru de refonte.


En effet, lorsqu'une scission se produit et que la chaîne qui applique les règles les plus générales devient plus forte que la chaîne qui applique les règles les plus strictes, une réorganisation se produit. Cela aura un impact sévère sur toutes les transactions effectuées dans la branche effacée. C'est pourquoi il est très important d'essayer d'éviter les scissions de chaînes à tout moment.


### Conclusion sur la mise à niveau


Bitcoin grandit et évolue avec le temps. Différents mécanismes de mise à niveau ont été utilisés au fil des ans et la courbe d'apprentissage est raide. Des méthodes de plus en plus sophistiquées et robustes sont inventées au fur et à mesure que nous en apprenons davantage sur la façon dont le réseau réagit.


Pour préserver l'harmonie de Bitcoin, les fourches Soft se sont avérées être la voie à suivre, mais la grande question n'a pas encore trouvé de réponse : comment déployer en toute sécurité les fourches Soft sans provoquer de discorde ?


## Pensée contradictoire

<chapterId>d4982f3d-4694-51cc-99be-28f54b03a2a2</chapterId>


![](assets/adversarialthinking-banner.webp)


Ce chapitre traite de la *pensée contradictoire*, un état d'esprit qui se concentre sur ce qui pourrait mal tourner et sur la façon dont les adversaires pourraient agir. Nous commençons par discuter des hypothèses et du modèle de sécurité de Bitcoin, après quoi nous expliquons comment les utilisateurs ordinaires peuvent améliorer leur souveraineté personnelle et la décentralisation Full node de Bitcoin en pensant de manière contradictoire. Ensuite, nous examinons quelques menaces réelles pour Bitcoin ainsi que l'esprit de l'adversaire. Enfin, nous parlerons de l'"axiome de résistance" qui peut vous aider à comprendre pourquoi les gens travaillent sur Bitcoin en premier lieu.


Lorsque l'on discute de la sécurité dans différents systèmes, il est important de comprendre quelles sont les hypothèses de sécurité. Une hypothèse de sécurité typique dans Bitcoin est que "le problème du logarithme discret est Hard à résoudre", ce qui, en termes simples, signifie qu'il est pratiquement impossible de trouver une clé privée qui corresponde à une clé publique particulière. Une autre hypothèse de sécurité assez forte est qu'une majorité de la puissance du réseau est honnête, ce qui signifie qu'elle respecte les règles. Si ces hypothèses s'avèrent fausses, Bitcoin est en difficulté.


En 2015, Andrew Poelstra [a donné une conférence] (https://btctranscripts.com/scalingbitcoin/hong-kong-2015/security-assumptions/) lors de la conférence Scaling Bitcoin à Hong Kong, au cours de laquelle il a analysé les hypothèses de sécurité de Bitcoin. Il commence par remarquer que de nombreux systèmes ne tiennent pas compte des adversaires dans une certaine mesure ; par exemple, il est vraiment Hard de protéger un bâtiment contre tous les types d'événements adverses. Au lieu de cela, nous acceptons généralement la possibilité que quelqu'un mette le feu au bâtiment et, dans une certaine mesure, nous prévenons cette éventualité et d'autres comportements adverses par le biais de l'application de la loi, etc.


Voir l'analogie du bâtiment de Greg Maxwell :


![](https://youtu.be/Gs9lJTRZCDc?t=2799)


Mais en ligne, les choses sont différentes :


> Cependant, en ligne, ce n'est pas le cas. Nous avons des comportements pseudonymes et anonymes, n'importe qui peut se connecter à n'importe qui et nuire au système. S'il est possible de nuire au système de manière contradictoire, ils le feront. Nous ne pouvons pas supposer qu'ils seront visibles et qu'ils se feront prendre.

La conséquence est que toutes les faiblesses connues de la Bitcoin doivent être corrigées d'une manière ou d'une autre, sinon elles seront exploitées. Après tout, Bitcoin est le plus grand pot de miel du monde.


M. Poelstra poursuit en indiquant que le Bitcoin est un nouveau type de système ; il est plus nébuleux que, par exemple, un protocole de signature qui repose sur des hypothèses de sécurité très claires.


Sur son blog personnel, l'ingénieur en logiciel Jameson Lopp [se penche sur la question] (https://blog.lopp.net/bitcoins-security-model-a-deep-dive/) :


> En réalité, le protocole Bitcoin a été et continue d'être construit sans spécification ni modèle de sécurité formellement définis. Le mieux que nous puissions faire est d'étudier les motivations et le comportement des acteurs au sein du système afin de mieux le comprendre et de tenter de le décrire.

Nous avons donc un système qui semble fonctionner dans la pratique, mais dont nous ne pouvons pas prouver formellement qu'il est sûr. Une preuve n'est probablement pas possible pour les raisons suivantes

la complexité du système lui-même.


### Pas seulement pour les experts Bitcoin



L'importance de la pensée contradictoire s'étend également aux utilisateurs quotidiens de Bitcoin dans une certaine mesure, et pas seulement aux développeurs et experts hardcore de Bitcoin. Ragnar Lifthasir mentionne dans un [tweetstorm] (https://bitcoinwords.github.io/tweetstorm-on-adversarial-thinking) comment les récits simplistes autour de Bitcoin - par exemple, "juste HODL" - peuvent être dégradants pour Bitcoin lui-même, et conclut en disant


> Pour rendre Bitcoin et nous-mêmes plus forts, nous devons penser comme les ingénieurs logiciels qui contribuent à Bitcoin. Ils procèdent à une évaluation par les pairs, cherchant impitoyablement les failles. Lors de leurs événements techniques, ils parlent de toutes les façons dont une proposition peut échouer. Ils pensent de manière contradictoire. Ils sont conservateurs

Il qualifie ces récits simplistes de monomanies. Par cette définition, il veut dire qu'en se concentrant sur une seule chose - par exemple, "juste HODL" - on risque de négliger des choses sans doute plus importantes, comme de garder sa Bitcoin en sécurité ou de faire de son mieux pour utiliser la Bitcoin d'une manière qui soit conforme à la Trustless.


### Menaces



Il y a beaucoup de faiblesses connues dans Bitcoin, et beaucoup d'entre elles sont activement exploitées. Pour s'en rendre compte, il suffit de consulter la [page des faiblesses] (https://en.Bitcoin.it/wiki/Weaknesses) sur le wiki Bitcoin. Il y est fait mention d'une grande variété de problèmes, tels que

Wallet vol et attaques par déni de service :


> Si un attaquant tente de remplir le réseau avec des clients qu'il contrôle, il est fort probable que vous ne vous connectiez qu'aux nœuds de l'attaquant. Bien que Bitcoin n'utilise jamais un nombre de nœuds pour quoi que ce soit, isoler complètement un nœud du réseau honnête peut être utile pour l'exécution d'autres attaques.

Ce type d'attaque est appelé *attaque Sybil* et se produit lorsqu'une seule entité contrôle plusieurs nœuds dans un réseau et les utilise pour se faire passer pour plusieurs entités.


Comme le mentionne également la citation, l'attaque Sybil n'est pas efficace sur le réseau Bitcoin parce qu'il n'y a pas de vote par nœuds ou autres entités numériques, mais plutôt par puissance de calcul. Néanmoins, cette structure plate rend le système vulnérable à d'autres attaques. La page wiki Bitcoin décrit également d'autres attaques possibles, telles que la dissimulation d'informations (souvent appelée *attaque par éclipse*), et la façon dont le Bitcoin Core met en œuvre des contre-mesures heuristiques contre de telles attaques.


Les exemples ci-dessus sont des menaces réelles auxquelles il faut faire face.


### Champ de sabotage simple


![](assets/sabotage-manual.webp)


Extrait du Simple Sabotage Field Manual (Manuel de terrain du sabotage simple)


Pour mieux comprendre l'esprit de l'adversaire, il peut être utile d'avoir un aperçu de son mode de fonctionnement. Un organisme gouvernemental américain appelé Office of Strategic Services, qui opérait pendant la Seconde Guerre mondiale et dont l'un des objectifs était de mener des activités d'espionnage, de sabotage et de propagande, a publié un [manuel] (https://www.gutenberg.org/ebooks/26184) à l'intention de son personnel sur la manière de saboter correctement l'ennemi. Intitulé "Simple Sabotage Field Manual", il contient des conseils concrets pour infiltrer l'ennemi et lui rendre la vie impossible (Hard). Les conseils vont de l'incendie d'entrepôts à l'usure d'exercices afin de réduire la résistance de l'ennemi

l'efficacité.


Par exemple, une section traite de la manière dont un infiltré peut perturber les organisations. Il n'est pas difficile de voir comment de telles tactiques pourraient être utilisées pour cibler le processus de développement Bitcoin, auquel tout le monde peut participer. Un attaquant dévoué peut continuer à bloquer les progrès par des préoccupations interminables sur des questions non pertinentes, des marchandages sur des formulations précises et des tentatives de réitérer des discussions qui ont déjà été abordées de manière exhaustive. L'attaquant peut également engager une armée de trolls pour multiplier sa propre efficacité ; c'est ce que l'on appelle une attaque par Sybille sociale. Grâce à cette attaque, il peut faire croire que la résistance à un changement proposé est plus forte qu'elle ne l'est en réalité.


Cela montre qu'un État déterminé peut faire et fera tout ce qui est en son pouvoir pour détruire l'ennemi, y compris le briser de l'intérieur. Étant donné que la Bitcoin est une forme de monnaie qui entre en concurrence avec les monnaies fiduciaires établies, il y a de fortes chances que les États considèrent la Bitcoin comme un ennemi.


### Axiome de la résistance


Eric Voskuil [écrit sur sa page wiki Cryptoeconomics] (https://github.com/libbitcoin/libbitcoin-system/wiki/Axiom-of-Resistance) sur ce qu'il appelle "l'axiome de résistance" :


> En d'autres termes, on suppose qu'il est possible pour un système de résister au contrôle de l'État. Cette hypothèse n'est pas acceptée comme un fait, mais est considérée comme une hypothèse raisonnable, en raison de l'étude empirique du comportement de systèmes similaires, sur laquelle le système est basé.
>

> Celui qui n'accepte pas l'axiome de la résistance envisage un système entièrement différent de Bitcoin. Si l'on suppose qu'il n'est pas possible pour un système de résister aux contrôles de l'État, les conclusions n'ont pas de sens dans le contexte de Bitcoin - tout comme les conclusions de la géométrie sphérique contredisent celles de la géométrie euclidienne. Comment Bitcoin peut-il être sans permission ou résistant à la censure sans l'axiome ? La contradiction conduit à commettre des erreurs évidentes pour tenter de rationaliser le conflit.


Ce qu'il dit essentiellement, c'est que ce n'est que lorsqu'on suppose qu'il est possible de créer un système que les États ne peuvent pas contrôler qu'il est utile d'essayer.


Cela signifie que pour travailler sur Bitcoin, vous devez accepter l'axiome de la résistance, sinon vous feriez mieux de consacrer votre temps à d'autres projets. Reconnaître cet axiome vous permet de concentrer vos efforts de développement sur les vrais problèmes qui se posent : coder autour d'adversaires au niveau de l'État. En d'autres termes, pensez de manière contradictoire.


### Conclusion sur la pensée contradictoire



Un système décentralisé ne peut avoir de responsabilité en dehors du système lui-même, c'est pourquoi Bitcoin doit prévenir les comportements malveillants de manière plus rigoureuse que les systèmes traditionnels. La pensée adverse est impérative dans un tel système.


Pour assurer la sécurité de Bitcoin, il faut connaître ses ennemis et leurs motivations. La plupart des menaces semblent se résumer aux États-nations, qui disposent d'un énorme pouvoir économique, grâce à la fiscalité et à l'impression monétaire. Ils ne renonceront probablement pas facilement à leurs privilèges en matière d'impression monétaire.


## Source ouverte

<chapterId>427a160c-f893-5b2c-afba-7b24e71ba899</chapterId>



![](assets/opensource-banner.webp)


Bitcoin est construit à l'aide de logiciels libres. Dans ce chapitre, nous analysons ce que cela signifie, comment fonctionne la maintenance du logiciel, et comment le logiciel libre de Bitcoin permet un développement sans permission. Nous nous plongeons dans la *cryptographie de sélection*, qui traite de la sélection et de l'utilisation des bibliothèques dans les systèmes cryptographiques. Le chapitre comprend une section sur le processus de révision de Bitcoin, suivie d'une autre sur la façon dont les développeurs de Bitcoin sont financés. La dernière section explique comment la culture open source de Bitcoin peut sembler vraiment bizarre de l'extérieur, et pourquoi cette bizarrerie perçue est en fait un signe de bonne santé.


La plupart des logiciels Bitcoin, et en particulier Bitcoin Core, sont des logiciels libres. Cela signifie que le code source du logiciel est mis à la disposition du grand public pour examen, bricolage, modification et redistribution. La définition de l'open source à [] (https://opensource.org/osd) comprend, entre autres, les points importants suivants :


> Redistribution gratuite : La licence n'empêche pas une partie de vendre ou de donner le logiciel en tant que composant d'une distribution globale de logiciels contenant des programmes provenant de plusieurs sources différentes. La licence n'exige pas de redevance ou d'autres droits pour une telle vente.
>

> Code source : Le programme doit inclure le code source et doit permettre la distribution du code source et de la version compilée. Lorsqu'une forme de produit n'est pas distribuée avec le code source, il doit exister un moyen bien connu d'obtenir le code source pour un coût de reproduction raisonnable, de préférence en le téléchargeant gratuitement sur l'internet. Le code source doit être la forme préférée sous laquelle un programmeur modifierait le programme. Le code source délibérément obscurci n'est pas autorisé. Les formes intermédiaires telles que la sortie d'un préprocesseur ou d'un traducteur ne sont pas autorisées.
>

> Travaux dérivés : La licence doit autoriser les modifications et les travaux dérivés, et doit permettre leur distribution dans les mêmes conditions que la licence du logiciel original.

Bitcoin Core respecte cette définition en étant distribué sous la [MIT License] (https://github.com/Bitcoin/Bitcoin/blob/master/COPYING) :


```
The MIT License (MIT)

Copyright (c) 2009-2022 The Bitcoin Core developers
Copyright (c) 2009-2022 Bitcoin Developers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```


Comme indiqué au chapitre "Ne faites pas confiance, vérifiez", il est important que les utilisateurs puissent vérifier que le logiciel Bitcoin qu'ils utilisent "fonctionne comme annoncé". Pour ce faire, ils doivent avoir un accès illimité au code source du logiciel qu'ils souhaitent vérifier.


Dans les prochaines sections, nous nous pencherons sur d'autres aspects intéressants des logiciels libres dans Bitcoin.


### Maintenance des logiciels



Le code source de Bitcoin Core est maintenu dans un dépôt Git hébergé sur [GitHub] (https://github.com/Bitcoin/Bitcoin). N'importe qui peut cloner ce même dépôt sans demander aucune permission, puis l'inspecter, le construire ou y apporter des modifications localement. Cela signifie qu'il existe plusieurs milliers de copies du référentiel réparties dans le monde entier. Ce sont toutes des copies du même dépôt, alors qu'est-ce qui rend ce dépôt GitHub Bitcoin Core si spécial ? Techniquement, il n'est pas spécial du tout, mais socialement, il est devenu le point central du développement de Bitcoin.


Jameson Lopp, expert en Bitcoin et en sécurité, l'explique très bien dans un [billet de blog] (https://blog.lopp.net/who-controls-Bitcoin-core-/) intitulé "Who Controls Bitcoin Core ?" (Qui contrôle le noyau Bitcoin ?):


> Bitcoin Core est un point focal pour le développement du protocole Bitcoin plutôt qu'un point de commande et de contrôle. S'il cessait d'exister pour quelque raison que ce soit, un nouveau point focal émergerait - la plateforme de communication technique sur laquelle il est basé (actuellement le dépôt GitHub) est une question de commodité plutôt qu'une question de définition / intégrité du projet. En fait, nous avons déjà vu le point focal de Bitcoin pour le développement changer de plateforme et même de nom !

Il explique ensuite comment le logiciel de Bitcoin Core est maintenu et protégé contre les modifications de code malveillantes. La conclusion générale de cet article complet est résumée à la toute fin :


> Personne ne contrôle Bitcoin.
>

> Personne ne contrôle le point central du développement de Bitcoin.

Le développeur de Bitcoin Core, Eric Lombrozo, parle plus en détail du processus de développement dans son [Medium post] (https://medium.com/@elombrozo/the-Bitcoin-core-merge-process-74687a09d81d) intitulé "The Bitcoin Core Merge Process" (Le processus de fusion de Bitcoin Core) :


> N'importe qui peut Fork le dépôt de la base de code et faire des changements arbitraires à leur propre dépôt. Il peut construire un client à partir de son propre dépôt et l'exécuter à la place s'il le souhaite. Il peut également créer des versions binaires pour que d'autres personnes les exécutent.
>

> Si quelqu'un veut fusionner un changement qu'il a fait dans son propre dépôt dans Bitcoin Core, il peut soumettre une demande d'extraction. Une fois la demande soumise, n'importe qui peut examiner les changements et les commenter, qu'il ait ou non accès à Bitcoin Core lui-même.

Il faut noter que les pull requests peuvent prendre beaucoup de temps avant d'être fusionnées dans le dépôt par les mainteneurs, et cela est généralement dû à un manque de révision, qui est souvent dû à un manque de *réviseurs*.


Lombrozo parle également du processus qui entoure les changements de consensus, mais cela dépasse un peu le cadre de ce chapitre. Voir le chapitre précédent "Mise à jour" pour plus d'informations sur la façon dont le protocole Bitcoin est mis à jour.


### Développement sans autorisation



Nous avons établi que n'importe qui peut écrire du code pour Bitcoin Core sans demander de permission, mais pas nécessairement le faire fusionner dans le dépôt Git principal. Ceci affecte toute modification, depuis le changement des couleurs de l'utilisateur graphique Interface, jusqu'à la façon dont les messages peer-to-peer sont formatés, et même les règles de consensus, c'est-à-dire l'ensemble des règles qui définissent un Blockchain valide.


Il est probablement tout aussi important que les utilisateurs soient libres de développer des systèmes à partir de Bitcoin, sans demander aucune permission. Nous avons vu d'innombrables projets logiciels réussis qui ont été construits sur la base de Bitcoin, tels que :



- Lightning Network : Un réseau de paiement qui permet le paiement rapide de très petits montants. Il nécessite très peu de On-Chain Bitcoin transactions. Il existe plusieurs implémentations interopérables, telles que [Core Lightning](https://github.com/ElementsProject/lightning), [LND](https://github.com/lightningnetwork/LND), [Eclair](https://github.com/ACINQ/eclair) et [Lightning Dev Kit](https://github.com/lightningdevkit).
- CoinJoin : Plusieurs parties collaborent pour combiner leurs paiements en une seule transaction afin de rendre le Address clustering plus difficile. Il existe plusieurs implémentations.
- Chaînes latérales : Ce système peut verrouiller une pièce sur la Blockchain de la Bitcoin afin de la déverrouiller sur une autre Blockchain. Cela permet de déplacer des bitcoins vers une autre Blockchain, à savoir une Sidechain, afin d'utiliser les fonctionnalités disponibles sur cette Sidechain. Parmi les exemples, on peut citer [la Elements de Blockstream] (https://github.com/ElementsProject/Elements).
- OpenTimestamps : il vous permet de [Timestamp un document] (https://opentimestamps.org/) sur la Blockchain de Bitcoin de manière privée. Vous pouvez ensuite utiliser cette Timestamp pour prouver qu'un document a dû exister avant une certaine date.


Sans le développement sans permission, beaucoup de ces projets n'auraient pas été possibles. Comme indiqué dans le chapitre sur la neutralité, si les développeurs devaient demander l'autorisation de créer des protocoles sur la base de Bitcoin, seuls les protocoles autorisés par le comité central d'octroi de licences aux développeurs seraient développés.


Il est courant que des systèmes tels que ceux énumérés ci-dessus soient eux-mêmes sous licence de logiciel libre, ce qui permet aux gens de contribuer, de réutiliser ou de réviser leur code sans demander d'autorisation. L'open source est devenu l'étalon-or des licences de logiciels Bitcoin.


### Développement du pseudonyme



Le fait de ne pas avoir à demander l'autorisation de développer le logiciel Bitcoin offre une option intéressante et importante : vous pouvez écrire et publier du code, dans Bitcoin Core ou dans tout autre projet open source, sans révéler votre identité.


De nombreux développeurs choisissent cette option en opérant sous un pseudonyme et en essayant de le dissocier de leur véritable identité. Les raisons de ce choix peuvent varier d'un développeur à l'autre. ZmnSCPxj est un utilisateur sous pseudonyme. Parmi d'autres projets, il contribue à Bitcoin Core et Core Lightning, l'une des nombreuses implémentations de Lightning Network. [Il écrit](https://zmnscpxj.github.io/about.html) sur sa page web :


> Je suis ZmnSCPxj, un internaute généré aléatoirement. Mes pronoms sont he/him/his.
>

> Je comprends que les humains désirent instinctivement connaître mon identité. Cependant, je pense que mon identité est largement immatérielle et je préfère être jugé sur mon travail.
>

> Si vous vous demandez si vous devez faire un don ou non, et si vous vous interrogez sur mon coût de la vie ou mes revenus, sachez qu'à proprement parler, vous devez me faire un don en fonction de l'utilité que vous trouvez à mon travail
et mon travail sur le Bitcoin et le Lightning Network.


Dans son cas, la raison de l'utilisation d'un pseudonyme doit être jugée sur ses mérites et non sur l'identité de la personne ou des personnes qui se cachent derrière le pseudonyme. Il est intéressant de noter qu'il a révélé dans un [article sur CoinDesk] (https://www.coindesk.com/markets/2020/06/29/many-Bitcoin-developers-are-choosing-to-use-pseudonyms-for-good-reason/) que le pseudonyme a été créé pour une raison différente.


> La raison initiale [de l'utilisation d'un pseudonyme] était simplement que je craignais de commettre une grave erreur ; ainsi, ZmnSCPxj était initialement destiné à être un pseudonyme jetable qui pourrait être abandonné dans un tel cas. Cependant, comme il semble avoir acquis une réputation plutôt positive, je l'ai conservé

L'utilisation d'un pseudonyme vous permet en effet de parler plus librement sans mettre votre réputation personnelle en danger si vous dites quelque chose de stupide ou si vous faites une grosse erreur. Il s'est avéré que son pseudonyme a acquis une très bonne réputation et qu'en 2019 [il a même obtenu une subvention de développement] (https://twitter.com/spiralbtc/status/1204815615678177280), ce qui est en soi un témoignage de la nature sans permission de Bitcoin.


Le pseudonyme le plus connu de Bitcoin est sans doute Satoshi Nakamoto. Les raisons pour lesquelles il a choisi ce pseudonyme ne sont pas claires, mais avec le recul, il s'agit probablement d'une bonne décision pour de multiples raisons :


- Comme de nombreuses personnes pensent que Nakamoto possède beaucoup de Bitcoin, il est impératif pour sa sécurité financière et personnelle de ne pas dévoiler son identité.
- Son identité étant inconnue, il n'est pas possible de poursuivre qui que ce soit, ce qui donne aux différentes autorités gouvernementales un délai Hard.
- Il n'y a pas de personne autoritaire sur laquelle s'appuyer, ce qui rend la Bitcoin plus méritocratique et plus résistante au chantage.


Notez que ces points ne s'appliquent pas seulement à Satoshi Nakamoto, mais à toute personne travaillant dans Bitcoin ou détenant des quantités significatives de la monnaie, à des degrés divers.


### Cryptographie de sélection


Les développeurs open source utilisent souvent des bibliothèques open source développées par d'autres personnes. Il s'agit là d'un élément naturel et formidable de tout écosystème sain. Mais les logiciels Bitcoin traitent de l'argent réel et, à la lumière de cela, les développeurs doivent être très prudents lorsqu'ils choisissent les bibliothèques tierces dont ils doivent dépendre.


Dans un [exposé philosophique sur la cryptographie] (https://btctranscripts.com/greg-maxwell/2015-04-29-gmaxwell-Bitcoin-selection-cryptography/), Gregory Maxwell souhaite redéfinir le terme "cryptographie" qu'il juge trop étroit. Il explique que, fondamentalement, *l'information veut être libre* et fonde sa définition de la cryptographie sur ce principe :


> La cryptographie est l'art et la science que nous utilisons pour lutter contre la nature fondamentale de l'information, pour la plier à notre volonté politique et morale, et pour l'orienter vers des fins humaines contre toute chance et tout effort de s'y opposer.

Il présente ensuite le terme "cryptographie de sélection", qui désigne l'art de sélectionner les outils cryptographiques, et explique pourquoi il s'agit d'une partie importante de la cryptographie. Elle porte sur la manière de sélectionner les bibliothèques, les outils et les pratiques cryptographiques ou, comme il le dit, "le cryptosystème de sélection des cryptosystèmes".


À l'aide d'exemples concrets, il montre comment la cryptographie de sélection peut facilement tourner mal, et propose également une liste de questions que vous pouvez vous poser lorsque vous la pratiquez. Vous trouverez ci-dessous une version condensée de cette liste :


- Le logiciel est-il destiné à votre usage ?
- Les considérations cryptographiques sont-elles prises au sérieux ?
- Quelle est la procédure d'examen ? Y en a-t-il une ?
- Quelle est l'expérience des auteurs ?
- Le logiciel est-il documenté ?
- Le logiciel est-il portable ?
- Le logiciel est-il testé ?
- Le logiciel adopte-t-il les meilleures pratiques ?


Bien qu'il ne s'agisse pas d'un guide ultime pour réussir, il peut être très utile de passer en revue ces points lorsque l'on fait de la cryptographie de sélection.


En raison des problèmes mentionnés ci-dessus par Maxwell, Bitcoin Core essaie vraiment Hard de [minimiser son exposition aux bibliothèques tierces] (https://github.com/Bitcoin/Bitcoin/blob/master/doc/dependencies.md). Bien sûr, vous ne pouvez pas éradiquer toutes les dépendances externes, sinon vous devriez tout écrire vous-même, du rendu des polices à l'implémentation des appels système.


### Révision



Cette section est nommée "Révision", plutôt que "Révision du code", parce que la sécurité de Bitcoin repose fortement sur une révision à plusieurs niveaux, et pas seulement au niveau du code source. De plus, différentes idées nécessitent une révision à différents niveaux : un changement de règle consensuelle nécessiterait une révision plus profonde à plusieurs niveaux par rapport à un changement de schéma de couleur ou une correction de coquille.


Sur le chemin de l'adoption finale, une idée passe généralement par plusieurs phases de discussion et d'examen. Certaines de ces phases sont énumérées ci-dessous :



- Une idée est postée sur la liste de diffusion Bitcoin-dev
- L'idée est formalisée dans une proposition d'amélioration de la Bitcoin (BIP)
- Le BIP est mis en œuvre dans une demande d'extension (pull request, PR) à Bitcoin Core
- Les mécanismes de déploiement sont examinés
- Certains mécanismes de déploiement concurrents sont mis en œuvre dans des demandes d'extension de Bitcoin Core
- Les pull requests sont fusionnées avec la branche master
- Les utilisateurs choisissent d'utiliser ou non le logiciel


À chacune de ces phases, des personnes ayant des points de vue et des antécédents différents examinent les informations disponibles, qu'il s'agisse du code source, d'un BIP ou simplement d'une idée vaguement décrite. En effet, plusieurs phases peuvent se dérouler simultanément et il arrive que l'on passe de l'une à l'autre. Différentes personnes peuvent également fournir un retour d'information au cours des différentes phases.


L'un des réviseurs de code les plus prolifiques sur Bitcoin Core est Jon Atack. Il a écrit [un billet de blog] (https://jonatack.github.io/articles/how-to-review-pull-requests-in-Bitcoin-core) sur la façon de réviser les demandes de modification dans Bitcoin Core. Il insiste sur le fait qu'un bon réviseur de code se concentre sur la meilleure façon d'apporter de la valeur ajoutée.


> En tant que nouvel arrivant, l'objectif est d'essayer d'apporter une valeur ajoutée, avec amabilité et humilité, tout en apprenant autant que possible.
>

> Une bonne approche consiste à ne pas se préoccuper de soi, mais plutôt de se demander "Comment puis-je servir au mieux ?"

Il souligne le fait que la révision est un facteur réellement limitant dans Bitcoin Core. Beaucoup de bonnes idées restent bloquées dans les limbes où aucune révision n'a lieu, en attente. Notez que la révision n'est pas seulement bénéfique pour Bitcoin, mais aussi un excellent moyen d'apprendre sur le logiciel tout en lui apportant de la valeur, en même temps. La règle empirique d'Atack est d'examiner 5 à 15 RP avant de faire le vôtre. Encore une fois, vous devez vous concentrer sur la façon de servir au mieux la communauté, et non sur la façon de faire fusionner votre propre code. En outre, il insiste sur l'importance d'effectuer la relecture au bon niveau : est-ce le moment de se pencher sur les points faibles et les coquilles, ou le développeur a-t-il besoin d'une relecture plus orientée sur les concepts ? Jon Attack ajoute :


> Une première question utile au début d'un examen peut être : "Qu'est-ce qui est le plus nécessaire ici en ce moment ?" Répondre à cette question requiert de l'expérience et un contexte accumulé, mais c'est une question utile pour décider de la manière dont vous pouvez apporter le plus de valeur ajoutée en un minimum de temps.

La seconde moitié du billet consiste en des conseils techniques pratiques utiles sur la manière de procéder à l'examen, et fournit des liens vers des documents importants pour une lecture plus approfondie.


Gloria Zhao, développeuse Bitcoin Core et examinatrice de code, a écrit [un article] (https://github.com/glozow/Bitcoin-notes/blob/master/review-checklist.md) contenant les questions qu'elle se pose habituellement lors d'un examen. Elle indique également ce qu'elle considère comme une bonne évaluation :


> Personnellement, je pense qu'une bonne évaluation est une évaluation dans laquelle je me suis posé un grand nombre de questions précises sur le PR et où j'ai été satisfait des réponses
à ces questions. [Naturellement, je commence par des questions conceptuelles, puis des questions relatives à l'approche et enfin des questions relatives à la mise en œuvre. En général, je pense personnellement qu'il est inutile de laisser des commentaires relatifs à la syntaxe du C++ sur un projet de PR, et je me sentirais mal à l'aise de revenir à "est-ce que cela a du sens" après que l'auteur a répondu à plus de 20 de mes suggestions sur l'organisation du code.


Son idée qu'un bon examen doit se concentrer sur ce qui est le plus nécessaire à un moment donné s'aligne bien sur les conseils de Jon Atack. Elle

propose une liste de questions que vous pouvez vous poser à différents niveaux du processus de révision, mais insiste sur le fait que cette liste n'est en aucun cas exhaustive ni ne constitue une recette pure et simple. La liste est illustrée par des exemples concrets tirés de GitHub.


### Financement



De nombreuses personnes travaillent au développement de Bitcoin Open Source, que ce soit pour Bitcoin Core ou pour d'autres projets. Beaucoup le font pendant leur temps libre sans aucune compensation, mais certains développeurs sont également payés pour le faire.


Les entreprises, les individus et les organisations qui ont un intérêt dans le succès continu de Bitcoin peuvent donner des fonds aux développeurs, soit directement, soit par l'intermédiaire d'organisations qui à leur tour distribuent les fonds aux développeurs individuels. Il existe également un certain nombre d'entreprises axées sur Bitcoin qui embauchent des développeurs qualifiés pour leur permettre de travailler à plein temps sur Bitcoin.


### Choc culturel



Les gens ont parfois l'impression que les développeurs de Bitcoin se livrent à des querelles intestines et à des débats passionnés sans fin, et qu'ils sont incapables de prendre des décisions.


Par exemple, le mécanisme de déploiement du Taproot a fait l'objet de longues discussions au cours desquelles deux "camps" se sont formés. L'un voulait faire "échouer" la mise à jour si les mineurs n'avaient pas voté massivement pour les nouvelles règles après un certain moment, tandis que l'autre voulait appliquer les règles après ce moment, quoi qu'il arrive. Michael Folkson résume les arguments des deux camps dans un [email](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-February/018380.html) envoyé à la liste de diffusion Bitcoin-dev.


Le débat a duré apparemment indéfiniment, et il était vraiment Hard impossible de voir un consensus se former à ce sujet dans un avenir proche. Les gens se sont donc sentis frustrés et le débat s'est intensifié. Gregory Maxwell (en tant qu'utilisateur nullc) s'est inquiété [sur Reddit] (https://www.reddit.com/r/Bitcoin/comments/hrlpnc/technical_taproot_why_activate/fyqbn8s/?utm_source=share&utm_medium=web2x&context=3) que les longues discussions rendent la mise à jour moins sûre :


> À ce stade, une attente supplémentaire n'apporte pas plus d'examen et de certitude. Au contraire, un délai supplémentaire sape l'inertie et augmente potentiellement le risque, car les gens commencent à oublier des détails, à retarder le travail sur l'utilisation en aval (comme la prise en charge du Wallet) et à ne pas investir autant d'efforts de révision supplémentaires qu'ils le feraient s'ils avaient confiance dans le délai d'activation.

Finalement, ce différend a été résolu grâce à une nouvelle proposition de David Harding et Russel O'Connor appelée Speedy Trial, qui impliquait une période de signalisation comparativement plus courte pour les mineurs afin de verrouiller l'activation du Taproot, ou fail fast. S'ils l'activent pendant cette période, le Taproot sera déployé environ 6 mois plus tard.


Quelqu'un qui n'est pas habitué au processus de développement de Bitcoin penserait probablement que ces débats houleux ont l'air terriblement mauvais, voire toxiques. Il y a au moins deux facteurs qui les rendent mauvais, aux yeux de certaines personnes :



- Par rapport aux entreprises à source fermée, tous les débats se déroulent au grand jour, sans aucune censure. Un éditeur de logiciels comme Google ne laisserait jamais ses employés débattre ouvertement des fonctionnalités proposées ; il publierait tout au plus une déclaration sur la position de l'entreprise à ce sujet. Les entreprises paraissent ainsi plus harmonieuses que Bitcoin.
- Étant donné que Bitcoin n'exige aucune permission, tout le monde peut exprimer son opinion. C'est fondamentalement différent d'une entreprise à source fermée qui ne compte qu'une poignée de personnes ayant une opinion, généralement des personnes partageant les mêmes idées. La pléthore d'opinions exprimées au sein de Bitcoin est tout simplement stupéfiante par rapport à PayPal, par exemple.


La plupart des développeurs de Bitcoin soutiendraient que cette ouverture crée un environnement bon et sain, et même qu'elle est nécessaire pour produire le meilleur résultat.


Comme indiqué dans le chapitre Menace, le deuxième point ci-dessus peut être très bénéfique, mais il comporte un inconvénient. Un attaquant pourrait utiliser des tactiques dilatoires, comme celles décrites dans le [Simple Sabotage Field Manual] (https://www.gutenberg.org/ebooks/26184), pour fausser le processus de prise de décision et de développement.


Une autre chose qui mérite d'être mentionnée est que, puisque le Bitcoin est de l'argent et que le Bitcoin Core sécurise des quantités insondables d'argent, la sécurité dans ce contexte n'est pas prise à la légère. C'est la raison pour laquelle le Bitcoin Core

les développeurs peuvent paraître très "Hard-headed", ce qui est généralement justifié. En effet, une fonctionnalité dont la justification est faible ne sera pas acceptée. Il en irait de même si elle rompait le

reproductibles, ajoutait de nouvelles dépendances, ou si le code ne suivait pas les [meilleures pratiques] de Bitcoin (https://github.com/Bitcoin/Bitcoin/blob/master/doc/developer-notes.md).


Les nouveaux (et anciens) développeurs peuvent être frustrés par cela. Mais, comme il est d'usage dans les logiciels libres, vous pouvez toujours Fork consulter le dépôt, fusionner ce que vous voulez dans votre propre Fork, et construire et exécuter votre propre binaire.


### Conclusion sur l'Open Source


Bitcoin Core et la plupart des autres logiciels Bitcoin sont open source, ce qui signifie que chacun est libre de distribuer, de modifier et d'utiliser le logiciel comme il l'entend. Le dépôt Bitcoin Core sur GitHub est actuellement le point central du développement de Bitcoin, mais ce statut peut changer si les gens commencent à se méfier de ses mainteneurs, ou du site web lui-même.


L'open source permet un développement sans permission dans et au-dessus de Bitcoin. Que vous écriviez du code, que vous révisiez du code ou des protocoles, l'open source est ce qui vous permet de le faire, de manière pseudonome ou non.


Le processus de développement de Bitcoin est radicalement ouvert, ce qui peut donner l'impression que Bitcoin est un lieu toxique et inefficace, mais c'est ce qui permet à Bitcoin de résister aux acteurs malveillants.


## Mise à l'échelle

<chapterId>bb3f3924-202c-5cdd-b2e9-e0c1cab0e48e</chapterId>



![](assets/scaling-banner.webp)



Dans ce chapitre, nous examinons comment Bitcoin peut ou ne peut pas être mis à l'échelle. Nous commençons par examiner comment les gens ont raisonné sur la mise à l'échelle dans le passé. Ensuite, la majeure partie de ce chapitre explique diverses approches de la mise à l'échelle de Bitcoin, en particulier la mise à l'échelle verticale, horizontale, vers l'intérieur et en couches. Chaque description est suivie de considérations sur la question de savoir si l'approche interfère avec la proposition de valeur de Bitcoin.


Dans l'espace Bitcoin, les définitions du mot "échelle" varient d'une personne à l'autre. Certains le conçoivent comme l'augmentation de la capacité de transaction du Blockchain, d'autres pensent qu'il équivaut à une utilisation plus efficace du Blockchain, et d'autres encore le voient comme le développement de systèmes au-dessus du Bitcoin.


Dans le contexte de Bitcoin, et pour les besoins de cet ouvrage, nous définissons la mise à l'échelle comme *l'augmentation de la capacité d'utilisation de Bitcoin sans compromettre sa résistance à la censure*. Cette définition englobe plusieurs

les changements peuvent être de plusieurs ordres, par exemple :


- Réduire le nombre d'octets utilisés pour les entrées de transaction
- Améliorer les performances de la vérification des signatures
- Faire en sorte que le réseau peer-to-peer utilise moins de bande passante
- Mise en lots des transactions
- Architecture en couches


Nous nous pencherons bientôt sur les différentes approches de la mise à l'échelle, mais commençons par un bref aperçu de l'histoire de Bitcoin dans le contexte de la mise à l'échelle.


### Histoire de la mise à l'échelle



La mise à l'échelle a été un point central de discussion depuis la Genesis de la Bitcoin. La toute première phrase du [tout premier courriel] (https://www.metzdowd.com/pipermail/cryptography/2008-November/014814.html) en réponse à l'annonce par Satoshi du livre blanc Bitcoin sur la liste de diffusion Cryptographie concernait en effet la mise à l'échelle :


> Satoshi Nakamoto a écrit :
>

> "J'ai travaillé sur un nouveau système de monnaie électronique qui est entièrement peer-to-peer, sans tiers de confiance.  Le document est disponible à l'adresse suivante : http://www.Bitcoin.org/Bitcoin.pdf"
>

> Nous avons vraiment besoin d'un tel système, mais d'après ce que je comprends de votre proposition, il ne semble pas pouvoir s'adapter à la taille requise.

La conversation en elle-même n'est peut-être pas très intéressante ni exacte, mais elle montre que la mise à l'échelle a été une préoccupation dès le début.


Les discussions sur la mise à l'échelle ont atteint leur pic d'intérêt vers 2015-2017, lorsque de nombreuses idées différentes circulaient sur la question de savoir s'il fallait augmenter la limite maximale de la taille des blocs et comment. Il s'agissait d'une discussion plutôt inintéressante sur la modification d'un paramètre dans le code source, une modification qui ne résolvait rien fondamentalement mais qui repoussait le problème de la mise à l'échelle plus loin dans le futur, créant ainsi une dette technique.


En 2015, une conférence intitulée [Scaling Bitcoin] (https://scalingbitcoin.org/) s'est tenue à Montréal, avec une conférence de suivi six mois plus tard à Hong Kong et, par la suite, dans un certain nombre d'autres endroits dans le monde. L'accent a été mis précisément sur la manière de mettre à l'échelle Address. De nombreux développeurs Bitcoin et d'autres enthousiastes se sont réunis lors de ces conférences pour discuter de diverses questions et propositions relatives à la mise à l'échelle. La plupart de ces discussions ne portaient pas sur l'augmentation de la taille des blocs, mais sur des solutions à plus long terme.


Après la conférence de Hong Kong en décembre 2015, Gregory Maxwell [a résumé son point de vue] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-December/011865.html) sur de nombreuses questions qui ont été débattues, en commençant par une philosophie générale de la mise à l'échelle :


> Avec la technologie disponible, il existe des compromis fondamentaux entre l'échelle et la décentralisation. Si le système est trop coûteux, les gens seront obligés de faire confiance à des tiers plutôt que d'appliquer les règles du système de manière indépendante. Si l'utilisation des ressources du Bitcoin Blockchain, par rapport à la technologie disponible, est trop importante, le Bitcoin perd ses avantages concurrentiels par rapport aux anciens systèmes parce que la validation sera trop coûteuse (excluant de nombreux utilisateurs), ce qui obligera à rétablir la confiance dans le système.  Si la capacité est trop faible et nos méthodes de transaction trop inefficaces, l'accès à la chaîne pour la résolution des litiges sera trop coûteux, ce qui ramènera à nouveau la confiance dans le système.

Il parle du compromis entre le débit et la décentralisation. Si vous autorisez des blocs plus grands, vous pousserez certaines personnes hors du réseau parce qu'elles n'auront plus les ressources nécessaires pour valider les blocs. Mais d'un autre côté, si l'accès à l'espace des blocs devient plus cher, moins de personnes pourront se permettre de l'utiliser comme mécanisme de résolution des conflits. Dans les deux cas, les utilisateurs sont poussés vers des services de confiance.


Il poursuit en résumant les nombreuses approches de la mise à l'échelle présentées lors de la conférence. Parmi celles-ci figurent des vérifications de signatures plus efficaces en termes de calcul, des *témoins séparés*, y compris une modification de la taille limite des blocs, un mécanisme de propagation des blocs plus efficace en termes d'espace, et la construction de protocoles en couches au-dessus du Bitcoin. Bon nombre de ces

ont été mises en œuvre depuis.


### Méthodes de mise à l'échelle



Comme nous l'avons suggéré plus haut, la mise à l'échelle de Bitcoin ne doit pas nécessairement consister à augmenter la taille limite des blocs ou d'autres limites. Nous allons maintenant passer en revue quelques approches générales de la mise à l'échelle, dont certaines ne souffrent pas du compromis débit-décentralisation mentionné dans la section précédente.


#### Mise à l'échelle verticale



La mise à l'échelle verticale est le processus d'augmentation des ressources informatiques des machines qui traitent les données. Dans le contexte de la Bitcoin, ces dernières seraient les nœuds complets, à savoir les machines qui valident la Blockchain pour le compte de leurs utilisateurs.


La technique la plus couramment évoquée pour la mise à l'échelle verticale dans le Bitcoin est l'augmentation de la taille limite des blocs. Cela nécessiterait que certains nœuds complets mettent à niveau leur matériel pour répondre à l'augmentation des demandes de calcul. L'inconvénient est que cela se fait au détriment de la centralisation.


Outre les effets négatifs sur la décentralisation Full node, la mise à l'échelle verticale pourrait également avoir un impact négatif sur la décentralisation et la sécurité Mining de Bitcoin de manière moins évidente. Voyons comment les mineurs "devraient" fonctionner. Supposons qu'un Miner mine un bloc à la hauteur 7 et publie ce bloc sur le réseau Bitcoin. Il faudra un certain temps pour que ce bloc soit largement accepté, ce qui est principalement dû à deux facteurs :


- Le transfert du bloc entre les pairs prend du temps en raison des limitations de la bande passante.
- La validation du bloc prend du temps.


Pendant que le bloc 7 se propage dans le réseau, de nombreux mineurs sont encore en train de fabriquer des Mining sur le bloc 6 parce qu'ils n'ont pas encore reçu et validé le bloc 7. Pendant ce temps, si l'un de ces mineurs trouve un nouveau bloc à la hauteur 7, il y aura deux blocs concurrents à cette hauteur. Il ne peut y avoir qu'un seul bloc à la hauteur 7 (ou à toute autre hauteur), ce qui signifie que l'un des deux candidats doit devenir périmé.


En bref, les blocs périmés se produisent parce qu'il faut du temps pour que chaque bloc se propage, et plus la propagation est longue, plus la probabilité de blocs périmés est élevée.


Supposons que la limite de taille des blocs soit levée et que la taille moyenne des blocs augmente considérablement. Les blocs se propageraient alors plus lentement sur le réseau en raison des limitations de la bande passante et du temps de vérification. L'augmentation du temps de propagation accroît également les risques de blocs périmés.


Les mineurs n'aiment pas que leurs blocs soient bloqués parce qu'ils perdent leur Block reward, et ils font donc tout ce qu'ils peuvent pour éviter cela

scénario. Les mesures qu'ils peuvent prendre sont les suivantes :



- Report de la validation d'un bloc entrant, également connu sous le nom de *validationless Mining*. Les mineurs peuvent simplement vérifier la Proof-of-Work de l'en-tête du bloc et miner par-dessus, tout en téléchargeant le bloc complet et en le validant.
- Connexion à un Mining pool avec une plus grande largeur de bande et une meilleure connectivité.


La Mining sans validation affaiblit encore la décentralisation de la Full node, car la Miner se contente de faire confiance aux blocs entrants, au moins temporairement. Elle nuit également à la sécurité dans une certaine mesure, car une partie de la puissance de calcul du réseau est potentiellement construite sur une Blockchain invalide, au lieu de construire sur la chaîne la plus forte et la plus valide.


Le deuxième point a un effet négatif sur la décentralisation de Miner, car les pools disposant de la meilleure connectivité réseau et de la meilleure bande passante sont aussi les plus grands, ce qui incite les mineurs à graviter autour de quelques grands pools.


#### Mise à l'échelle horizontale



La mise à l'échelle horizontale fait référence aux techniques qui divisent la charge de travail entre plusieurs machines. Bien qu'il s'agisse d'une approche de mise à l'échelle très répandue sur les sites web et les bases de données populaires, elle n'est pas facile à mettre en œuvre dans Bitcoin.


De nombreuses personnes appellent cette approche de mise à l'échelle du Bitcoin *sharding*. Fondamentalement, elle consiste à laisser chaque Full node vérifier une partie seulement de la Blockchain. Peter Todd a beaucoup réfléchi au concept de sharding. Il a écrit un [billet de blog] (https://petertodd.org/2015/why-scaling-Bitcoin-with-sharding-is-very-Hard) expliquant le sharding en termes généraux, et présentant également sa propre idée appelée *treechains*. L'article est difficile à lire, mais Todd soulève des points qui sont tout à fait digestes :


> Dans les systèmes partagés, la "défense Full node" ne fonctionne pas, du moins directement. L'idée est que tout le monde ne dispose pas de toutes les données, et qu'il faut donc décider de ce qui se passe lorsqu'elles ne sont pas disponibles.

Il présente ensuite plusieurs idées sur la manière d'aborder le sharding, ou la mise à l'échelle horizontale. Vers la fin de son billet, il conclut :


> Mais il y a un gros problème : ce qui précède est sacrément complexe par rapport à Bitcoin ! Même la version "enfant" du sharding - mon schéma de linéarisation plutôt que zk-SNARKS - est probablement un ou deux ordres de grandeur plus complexe que l'utilisation du protocole Bitcoin à l'heure actuelle, et pourtant un énorme % des entreprises dans cet espace semblent avoir jeté leurs mains en l'air et utilisé des fournisseurs d'API centralisés à la place. Il ne sera pas facile de mettre en œuvre ce qui précède et de le mettre entre les mains des utilisateurs finaux.
>

> D'autre part, la décentralisation n'est pas bon marché : l'utilisation de PayPal est un ou deux ordres de grandeur plus simple que le protocole Bitcoin.

La conclusion qu'il en tire est que le sharding *pourrait* être techniquement possible, mais au prix d'une énorme complexité. Étant donné que de nombreux utilisateurs trouvent déjà Bitcoin trop complexe et préfèrent utiliser des services centralisés, il faudra Hard pour les convaincre d'utiliser quelque chose d'encore plus complexe.


#### Mise à l'échelle vers l'intérieur



Alors que les échelles horizontale et verticale ont toujours bien fonctionné dans les systèmes centralisés tels que les bases de données et les serveurs web, elles ne semblent pas convenir à un réseau décentralisé tel que Bitcoin en raison de leurs effets centralisateurs.


Une approche qui n'est pas assez appréciée est ce que l'on peut appeler *inward scaling*, qui se traduit par "faire plus avec moins". Il s'agit du travail permanent effectué par de nombreux développeurs pour optimiser les algorithmes déjà en place, afin que nous puissions faire plus dans les limites existantes du système.


Les améliorations obtenues grâce à l'échelonnement vers l'intérieur sont impressionnantes, c'est le moins que l'on puisse dire. Pour vous donner une idée générale des améliorations apportées au fil des ans, Jameson Lopp [a effectué des tests de référence] (https://blog.lopp.net/Bitcoin-core-performance-evolution/) sur la synchronisation Blockchain, en comparant de nombreuses versions différentes de Bitcoin Core en remontant jusqu'à la version 0.8.


![](assets/Bitcoin-Core-Sync-Performance-1.webp)


Performances de téléchargement des blocs initiaux de différentes versions de Bitcoin Core. L'axe des ordonnées indique la hauteur du bloc synchronisé et l'axe des abscisses indique le temps qu'il a fallu pour synchroniser à cette hauteur


Les différentes lignes représentent les différentes versions de Bitcoin Core. La ligne la plus à gauche est la plus récente, c'est-à-dire la version 0.22, qui a été publiée en septembre 2021 et a pris 396 minutes pour se synchroniser complètement. La ligne la plus à droite est la version 0.8 de novembre 2013, qui a pris 3452 minutes. Toute cette amélioration - environ 10x - est due à une mise à l'échelle vers l'intérieur.


Les améliorations peuvent être classées comme suit : économie d'espace (RAM, disque, bande passante, etc.) ou économie de puissance de calcul. Ces deux catégories contribuent aux améliorations présentées dans le diagramme ci-dessus.


Un bon exemple d'amélioration du calcul se trouve dans la bibliothèque [libsecp256k1](https://github.com/Bitcoin-core/secp256k1), qui, entre autres, implémente les primitives cryptographiques nécessaires à la création et à la vérification des signatures numériques. Pieter Wuille est l'un des contributeurs de cette bibliothèque, et il a écrit un [fil Twitter](https://twitter.com/pwuille/status/1450471673321381896) présentant les améliorations de performance obtenues grâce à diverses demandes d'extraction.


![](assets/libsecp256k1speedups.webp)


Performance de la vérification des signatures au fil du temps, avec les demandes de retrait significatives marquées sur la ligne du temps


Le graphique montre la tendance pour deux types de CPU 64 bits différents, à savoir ARM et x86. La différence de performance est due aux instructions plus spécialisées disponibles sur x86 par rapport à l'architecture ARM, qui dispose d'instructions moins nombreuses et plus génériques. Cependant, la tendance générale est la même pour les deux architectures. Notez que l'axe des ordonnées est logarithmique, ce qui rend les améliorations moins impressionnantes qu'elles ne le sont en réalité.


Il existe également plusieurs bons exemples d'améliorations permettant d'économiser de l'espace et contribuant à l'amélioration des performances. Dans un

[Medium blog post](https://murchandamus.medium.com/2-of-3-Multisig-inputs-using-Pay-to-Taproot-d5faf2312ba3) sur la contribution de Taproot à l'économie d'espace, l'utilisateur Murch compare l'espace de bloc nécessaire à une signature à seuil 2 sur 3, en utilisant Taproot de différentes manières et en ne l'utilisant pas du tout.


![](assets/murch-taproot.webp)


Gain de place pour les différents types de dépenses, Taproot et anciennes versions.


Une Multisig 2 sur 3 utilisant la SegWit native nécessiterait un total de 104,5+43 vB = 147,5 vB, alors que l'utilisation la plus prudente de la Taproot ne nécessiterait que 57,5+43 vB = 100,5 vB dans le cas d'utilisation standard. Dans le pire des cas et dans des cas rares, comme lorsqu'un signataire standard n'est pas disponible pour une raison quelconque, Taproot utiliserait 107,5+43 vB = 150,5 vB. Il n'est pas nécessaire de comprendre tous les détails, mais cela devrait vous donner une idée de la façon dont les développeurs pensent à économiser de l'espace - chaque petit octet compte.


Outre l'élargissement vers l'intérieur du logiciel Bitcoin, les utilisateurs peuvent également contribuer à l'élargissement vers l'intérieur de certaines manières. Ils peuvent effectuer leurs transactions de manière plus intelligente afin d'économiser les frais de transaction tout en réduisant leur empreinte sur les exigences de la Full node. Deux techniques couramment utilisées pour atteindre cet objectif sont la mise en lots des transactions et la consolidation des sorties.


L'idée de la mise en lot des transactions est de combiner plusieurs paiements en une seule transaction, au lieu d'effectuer une transaction par paiement. Cela peut vous permettre d'économiser beaucoup de frais, tout en réduisant la charge de l'espace de bloc.


![](assets/tx-batching.webp)


La mise en lot des transactions permet de regrouper plusieurs paiements en une seule transaction afin d'économiser des frais.


La consolidation des sorties consiste à profiter des périodes de faible demande d'espace de stockage pour combiner plusieurs sorties en une seule. Cela peut réduire le coût de la redevance plus tard, lorsque vous devrez effectuer un paiement alors que la demande d'espace de stockage est élevée.


![](assets/utxo-consolidation.webp)


Consolidation des sorties : Faites fondre vos pièces en une seule lorsque les frais sont peu élevés afin d'économiser des frais par la suite.


Il n'est peut-être pas évident de comprendre comment la consolidation des sorties contribue à la mise à l'échelle vers l'intérieur. Après tout, la quantité totale de données Blockchain est même légèrement augmentée avec cette méthode. Néanmoins, l'ensemble UTXO, c'est-à-dire la base de données qui permet de savoir qui possède quelles pièces, diminue car vous dépensez plus d'UTXO que vous n'en créez. Cela allège le fardeau des nœuds complets qui doivent maintenir leurs ensembles UTXO.


Malheureusement, ces deux techniques de gestion *UTXO* peuvent être néfastes pour votre vie privée ou celle de vos bénéficiaires. Dans le cas de la mise en lots, chaque bénéficiaire saura que toutes les sorties mises en lots proviennent de vous et sont destinées à d'autres bénéficiaires (à l'exception, éventuellement, de la modification). Dans le cas de la consolidation de la UTXO, vous révélerez que les sorties que vous consolidez appartiennent à la même Wallet. Il se peut donc que vous deviez faire un compromis entre la rentabilité et le respect de la vie privée.


#### Mise à l'échelle en couches



L'approche la plus efficace de la mise à l'échelle est probablement la superposition. L'idée générale de la superposition est qu'un protocole peut régler les paiements entre les utilisateurs sans ajouter de transactions au Blockchain.


Un protocole à plusieurs niveaux commence par l'accord de deux personnes ou plus sur une transaction de départ qui est placée sur le Blockchain, comme illustré dans la figure ci-dessous.


![](assets/scaling-layer.webp)

Un protocole Layer 2 typique au-dessus de Bitcoin, Layer 1.


La manière dont cette transaction de démarrage est créée varie d'un protocole à l'autre, mais un thème commun est que les participants créent une transaction de démarrage non signée et un certain nombre de transactions de punition pré-signées, qui dépensent la sortie de la transaction de démarrage de diverses manières. Par la suite, la transaction de départ est entièrement signée et publiée sur le Blockchain, et les transactions de punition peuvent être entièrement signées et publiées pour punir une partie qui s'est mal comportée. Cela incite les participants à tenir leurs promesses afin que le protocole puisse fonctionner de manière Trustless.


Une fois que la transaction de départ est sur le Blockchain, le protocole peut faire ce qu'il est censé faire. Par exemple, il peut effectuer des paiements ultra-rapides entre les participants, mettre en œuvre des techniques d'amélioration de la confidentialité ou utiliser des scripts plus avancés qui ne seraient pas pris en charge par le Bitcoin Blockchain.


Nous ne détaillerons pas le fonctionnement des protocoles spécifiques, mais comme vous pouvez le voir dans la figure précédente, le Blockchain est rarement utilisé pendant le cycle de vie du protocole. Toute l'action juteuse se déroule *off-chain*. Nous avons vu comment cela peut être une victoire pour la vie privée si c'est bien fait, mais cela peut aussi être un avantage pour l'évolutivité.


Dans un [post Reddit] (https://www.reddit.com/r/Bitcoin/comments/438hx0/a_trip_to_the_moon_requires_a_rocket_with/) intitulé "Un voyage sur la lune nécessite une fusée à plusieurs étages, sinon l'équation de la fusée vous mangera le déjeuner... entasser tout le monde dans une voiture de clown dans un trébuchet et espérer le succès est à proscrire", Gregory Maxwell explique pourquoi la superposition est notre meilleure chance de faire évoluer Bitcoin de plusieurs ordres de grandeur.


Il commence par souligner qu'il est faux de considérer Visa ou Mastercard comme les principaux concurrents du Bitcoin et que l'augmentation de la taille maximale des blocs est une mauvaise approche pour faire face à cette concurrence. Il explique ensuite comment faire une réelle différence en utilisant des couches :


> Cela signifie-t-il que le Bitcoin ne peut pas être une technologie de paiement gagnante ? Non. Mais pour atteindre le niveau de capacité requis pour répondre aux besoins du monde en matière de paiements, nous devons travailler plus intelligemment.
>

> Dès le début, Bitcoin a été conçu pour incorporer des couches de manière sécurisée grâce à sa capacité de contrats intelligents (Quoi, vous pensez que cela a été mis là juste pour que les gens puissent faire de la philosophie sur des "DAO" sans signification ?) En fait, nous utiliserons le système Bitcoin comme un juge robotique très accessible et parfaitement digne de confiance, et nous mènerons la plupart de nos affaires en dehors de la salle d'audience - mais nous ferons des transactions de telle sorte que si quelque chose tourne mal, nous aurons toutes les preuves et tous les accords établis, de sorte que nous pourrons être sûrs que le tribunal robotique fera ce qu'il faut pour régler le problème. (Aparté geek : si cela vous semble impossible, lisez cet ancien article sur la transparence des transactions)
>

> Cela est possible précisément en raison des propriétés fondamentales du Bitcoin. Un système de base censurable ou réversible n'est pas très approprié pour construire un puissant traitement de transaction Layer supérieur... et si l'actif sous-jacent n'est pas sain, il n'y a pas vraiment d'intérêt à effectuer des transactions avec lui.

L'analogie avec le juge illustre bien le fonctionnement de la stratification : ce juge doit être incorruptible et ne jamais changer d'avis, sinon les couches au-dessus de la base Bitcoin Layer ne fonctionneront pas de manière fiable.


Il poursuit en évoquant les services centralisés. Il n'y a généralement aucun problème à faire confiance à un serveur central doté de quantités triviales de Bitcoin pour accomplir les tâches : il s'agit également d'une mise à l'échelle en couches.


De nombreuses années se sont écoulées depuis que Maxwell a écrit l'article ci-dessus, et ses propos sont toujours d'actualité. Le succès du Lightning Network prouve que la superposition est en effet un moyen d'accroître l'utilité du Bitcoin.



### Conclusion sur la mise à l'échelle



Nous avons discuté des différentes façons de faire évoluer Bitcoin, d'augmenter la capacité d'utilisation de Bitcoin. La mise à l'échelle a été une préoccupation de Bitcoin depuis ses tout premiers jours.


Nous savons aujourd'hui que Bitcoin ne s'adapte pas bien verticalement ("acheter du matériel plus grand") ou horizontalement ("ne vérifier que certaines parties des données"), mais plutôt vers l'intérieur ("faire plus avec moins") et en couches ("construire des protocoles au-dessus de Bitcoin").


## Quand la merde s'abat sur le ventilateur

<chapterId>fe39c13c-310f-51fd-84ff-6b92dd01c9e7</chapterId>



![](assets/shtf-banner.webp)

Bitcoin est construit par des personnes. Ce sont eux qui écrivent le logiciel, et ce sont eux qui l'exécutent. Lorsqu'une faille de sécurité ou un bogue grave est découvert - y a-t-il vraiment une distinction entre les deux ? - ce sont toujours des personnes, en chair et en os, qui les découvrent. Ce chapitre examine ce que les gens font, devraient faire et ne devraient pas faire quand la merde frappe le ventilateur. La première section explique le terme "divulgation responsable", qui fait référence à la façon dont une personne qui découvre une vulnérabilité peut agir de manière responsable pour aider à minimiser les dommages causés par cette vulnérabilité. Le reste du chapitre vous emmène à la découverte de quelques-unes des vulnérabilités les plus graves découvertes au fil des ans, et de la manière dont elles ont été traitées par les développeurs, les mineurs et les utilisateurs. Les choses n'étaient pas aussi rigoureuses dans la petite enfance de Bitcoin qu'elles le sont aujourd'hui.


### Divulgation responsable



Imaginez que vous découvriez un bogue dans Bitcoin Core, un bogue qui permet à n'importe qui d'arrêter à distance un nœud Bitcoin Core en utilisant des messages réseau spécialement conçus. Imaginez également que vous n'êtes pas malveillant et que vous aimeriez que ce problème ne soit pas exploité. Que feriez-vous ? Si vous restez silencieux, quelqu'un d'autre découvrira probablement le problème, et vous ne pouvez pas être sûr que cette personne ne sera pas malveillante.


Lorsqu'un problème de sécurité est découvert, la personne qui le découvre doit recourir à la _divulgation responsable_, un terme souvent utilisé par les développeurs de Bitcoin. Ce terme est [expliqué sur Wikipedia] (https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure) :


> Les développeurs de matériel et de logiciels ont souvent besoin de temps et de ressources pour réparer leurs erreurs. Souvent, ce sont des pirates éthiques qui trouvent ces
les vulnérabilités. Les pirates informatiques et les spécialistes de la sécurité informatique estiment qu'il est de leur responsabilité sociale de sensibiliser le public aux vulnérabilités. Le fait de cacher les problèmes pourrait créer un sentiment de fausse sécurité. Pour éviter cela, les parties concernées se coordonnent et négocient un délai raisonnable pour réparer la vulnérabilité. En fonction de l'impact potentiel de la vulnérabilité, du temps nécessaire à la mise au point et à l'application d'un correctif d'urgence ou d'une solution de contournement et d'autres facteurs, ce délai peut varier de quelques jours à plusieurs mois.


Cela signifie que si vous trouvez un problème de sécurité, vous devez le signaler à l'équipe responsable du système. Mais qu'est-ce que cela signifie dans le contexte de Bitcoin ? Personne ne contrôle Bitcoin, mais il y a actuellement un point central pour le développement de Bitcoin, à savoir le [Bitcoin Core Github repository] (https://github.com/Bitcoin/Bitcoin). Les mainteneurs de ce dépôt sont responsables du code qu'il contient, mais ils ne sont pas responsables du système dans son ensemble - personne ne l'est. Néanmoins, la meilleure pratique générale est d'envoyer un courriel à security@bitcoincore.org.


Dans un [fil de discussion] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/015002.html) intitulé "Responsible disclosure of bugs" datant de 2017, Anthony Towns a tenté de résumer ce qu'il percevait comme étant les meilleures pratiques actuelles. Il avait recueilli des informations auprès de plusieurs sources et de différentes personnes pour éclairer son point de vue sur le sujet.




- Les vulnérabilités doivent être signalées via security at bitcoincore.org
- Un problème critique (qui peut être exploité immédiatement ou qui l'est déjà et qui cause un préjudice important) sera traité de la manière suivante :
  - un correctif publié le plus rapidement possible
  - une large notification de la nécessité de mettre à niveau (ou de désactiver les systèmes concernés)
  - la divulgation minimale du problème réel, afin de retarder les attaques
- Une vulnérabilité non critique (parce qu'elle est difficile ou coûteuse à exploiter) sera traitée de la manière suivante :
  - la correction et l'examen entrepris dans le cours normal du développement
  - rétroportage d'un correctif ou d'une solution de contournement du master vers la version publiée actuelle
- Les développeurs tenteront de s'assurer que la publication du correctif ne révèle pas la nature de la vulnérabilité en fournissant le correctif proposé aux développeurs expérimentés qui n'ont pas été informés de la vulnérabilité, en leur disant qu'il corrige une vulnérabilité et en leur demandant d'identifier la vulnérabilité.
- Les développeurs peuvent recommander à d'autres implémentations de Bitcoin d'adopter des corrections de vulnérabilité avant que la correction ne soit publiée et largement déployée, s'ils peuvent le faire sans révéler la vulnérabilité ; par exemple, si la correction présente des avantages significatifs en termes de performances qui justifieraient son inclusion.
- Avant qu'une vulnérabilité ne soit rendue publique, les développeurs recommandent généralement aux développeurs Altcoin amis de rattraper les corrections. Mais ce n'est qu'après que les correctifs aient été largement déployés dans le réseau Bitcoin.
- Les développeurs ne notifieront généralement pas les développeurs Altcoin qui se sont comportés de manière hostile (par exemple, en utilisant des vulnérabilités pour attaquer d'autres personnes, ou en violant des embargos).
- Les développeurs de Bitcoin ne divulgueront pas les détails des vulnérabilités jusqu'à ce que >80% des nœuds Bitcoin aient déployé les correctifs. Les découvreurs de vulnérabilités sont encouragés et priés de suivre la même politique. [1] [6]


Cette liste montre à quel point il faut être prudent lorsqu'on publie des correctifs pour Bitcoin, car le correctif lui-même peut révéler la vulnérabilité. Le quatrième point est particulièrement intéressant car il explique comment tester si un correctif a été suffisamment bien déguisé. En effet, si quelques développeurs vraiment expérimentés ne peuvent pas repérer la vulnérabilité même en sachant que le correctif en corrige une, il sera probablement vraiment Hard difficile pour les autres de la découvrir.


Le fil de discussion qui a conduit à ce courriel portait sur la question de savoir si, quand et comment divulguer les vulnérabilités des altcoins et d'autres implémentations de Bitcoin. Il n'y a pas de réponse claire à ce sujet. "Aider les gentils semble être la chose à faire, mais qui décide de qui ils sont et où se situe la limite ? Bryan Bishop [a soutenu] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014983.html) qu'aider les altcoins et même les scamcoins à se défendre contre les exploits de sécurité était un devoir moral :


> Il ne suffit pas de défendre Bitcoin et ses utilisateurs contre les menaces actives, il y a une responsabilité plus générale de défendre toutes sortes d'utilisateurs et de logiciels différents contre toutes sortes de menaces sous toutes leurs formes, même si les gens utilisent des logiciels stupides et peu sûrs que vous ne maintenez pas personnellement, auxquels vous ne contribuez pas ou pour lesquels vous ne plaidez pas. La gestion de la connaissance d'une vulnérabilité est une question délicate et il se peut que vous receviez des informations ayant un impact direct ou indirect plus grave que celui décrit à l'origine.

Un [post] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014977.html) de Gregory Maxwell, dans lequel il affirme que les failles de sécurité peuvent être plus graves qu'il n'y paraît, a également conduit à l'envoi de l'e-mail de M. Town ci-dessus :


> J'ai vu à plusieurs reprises un problème Hard à exploiter se révéler trivial lorsque l'on trouve la bonne astuce, ou un problème de dos mineur se révéler bien plus grave.
>

> De simples bogues de performance, déployés de manière experte, peuvent potentiellement être utilisés pour découper le réseau - Miner A et Exchange B vont dans une partition, tous les autres dans une autre... et doublependent.
>

> Et ainsi de suite.  Ainsi, bien que je sois tout à fait d'accord sur le fait que différentes choses devraient et peuvent être traitées différemment, ce n'est pas toujours aussi clair. Il est prudent de considérer les choses comme plus graves que ce que l'on sait.

Ainsi, même si une vulnérabilité semble Hard à exploiter, il est préférable de supposer qu'elle est facilement exploitable et que vous n'avez pas encore trouvé comment.


Il mentionne également qu'"il est quelque peu erroné d'appeler ce fil de discussion un sujet relatif à la divulgation, ce fil de discussion ne concerne pas la divulgation. La divulgation consiste à informer le vendeur.  Ce fil traite de la publication et cela a des implications très différentes. La publication est le moment où l'on est sûr d'avoir informé les attaquants potentiels". Cette dernière observation concernant la distinction entre divulgation et publication est importante. La partie facile est la divulgation responsable ; la partie Hard est la publication raisonnable.


### L'enfance traumatisante de Bitcoin



Bitcoin a débuté comme un projet individuel (c'est du moins ce que suggère le pseudonyme de son créateur), et Bitcoin n'avait au départ que peu ou pas de valeur. Les vulnérabilités et les corrections de bogues n'étaient donc pas gérées de manière aussi rigoureuse qu'aujourd'hui.


Le wiki Bitcoin contient une [liste des vulnérabilités et expositions communes] (https://en.Bitcoin.it/wiki/Common_Vulnerabilities_and_Exposures) (CVE) que Bitcoin a traversées. Cette section constitue un petit exposé de certains problèmes et incidents de sécurité des premières années de Bitcoin. Nous ne les aborderons pas tous, mais nous en avons sélectionné quelques-uns que nous trouvons particulièrement intéressants.


#### 2010-07-28 : Dépenser les pièces de n'importe qui (CVE-2010-5141)



Le 28 juillet 2010, un pseudonyme du nom d'ArtForz a découvert un bug dans la version 0.3.4 qui permettait à n'importe qui de prendre les pièces de n'importe qui d'autre. ArtForz l'a signalé de manière responsable à Satoshi Nakamoto et à un autre développeur de Bitcoin, Gavin Andresen.


Le problème était que l'opérateur de script `OP_RETURN` quittait simplement l'exécution du programme, donc si la clé de scriptPubKey était `<pubkey> OP_CHECKSIG` et que scriptSig était `OP_1 OP_RETURN`, la partie du programme dans la clé de scriptPubKey ne s'exécuterait jamais. La seule chose qui se produirait serait que `1` soit placé sur la pile et que `OP_RETURN` entraîne la sortie du programme. Toute valeur non nulle au sommet de la pile après l'exécution du programme signifie que la condition de dépense est remplie. Puisque l'élément `1` du haut de la pile est non nul, la dépense est correcte.


Il s'agit du code pour le traitement de `OP_RETURN` :


```
case OP_RETURN:
{
pc = pend;
}
break;
```

L'effet de `pc = pend;` était que le reste du programme était ignoré, ce qui signifiait que tout script de verrouillage dans scriptPubKey serait ignoré. La correction consistait à changer la signification de `OP_RETURN` pour qu'il échoue immédiatement.


```
case OP_RETURN:
{
return false;
}
break;
```


Satoshi a effectué ce changement localement et a construit un binaire exécutable avec la version 0.3.5 à partir de celui-ci. Il a ensuite posté sur le forum Bitcointalk un message intitulé "ALERTE ALERTE ALERTE ALERTE ALERTE ALERTE ALERTE ALERTE ALERTE ALERTE", invitant les utilisateurs à installer cette version binaire, sans présenter le code source de cette version :


> Veuillez passer à la version 0.3.5 dès que possible !  Nous avons corrigé un bug d'implémentation qui permettait d'accepter de fausses transactions.  N'acceptez pas de transactions Bitcoin comme moyen de paiement tant que vous n'êtes pas passé à la version 0.3.5 !

Le message original a été modifié par la suite et n'est plus disponible dans sa forme complète. L'extrait ci-dessus provient d'une [réponse de citation] (https://bitcointalk.org/index.php?topic=626.msg6458#msg6458). Certains utilisateurs ont essayé le binaire de Satoshi, mais ont rencontré des problèmes. Peu après, [Satoshi a écrit](https://bitcointalk.org/index.php?topic=626.msg6469#msg6469) :


> Je n'ai pas encore eu le temps de mettre à jour le SVN.  Attendez la 0.3.6, je suis en train de la construire.  Vous pouvez éteindre votre nœud en attendant.

Et 35 minutes plus tard, [il écrit] (https://bitcointalk.org/index.php?topic=626.msg6480#msg6480) :


> Le SVN est mis à jour avec la version 0.3.6.
>

> Je télécharge la version Windows de la 0.3.6 sur Sourceforge, puis je reconstruirai la version linux.

À ce stade, il semble également avoir mis à jour le message original pour mentionner la version 0.3.6 au lieu de la version 0.3.5 :


> Veuillez passer à la version 0.3.6 dès que possible !  Nous avons corrigé un bug d'implémentation où il était possible que de fausses transactions soient affichées comme acceptées.  N'acceptez pas de transactions Bitcoin en tant que paiement avant d'avoir effectué la mise à jour vers la version 0.3.6 !
>

> Si vous ne pouvez pas mettre à jour vers la version 0.3.6 immédiatement, il est préférable d'éteindre votre nœud Bitcoin jusqu'à ce que vous le fassiez.
>

> Également dans la version 0.3.6, hachage plus rapide :
> - optimisation du cache midstate grâce à tcatm
> - Crypto++ ASM SHA-256 grâce à BlackEye
> Vitesse totale de génération 2,4 fois plus rapide.
>

> Télécharger :
>

> http://sourceforge.net/projects/Bitcoin/files/Bitcoin/Bitcoin-0.3.6/
>

> Utilisateurs de Windows et de Linux : si vous avez obtenu la version 0.3.5, vous devez encore mettre à jour vers la version 0.3.6.

Notez la différence dans la caractérisation du problème par rapport au premier message : "pourrait être affiché comme accepté" vs "pourrait être accepté". Peut-être que Satoshi a minimisé la gravité du bogue dans sa communication afin de ne pas attirer trop d'attention sur le problème réel. Quoi qu'il en soit, les gens sont passés à la version 0.3.6 et cela a fonctionné comme prévu. Ce problème particulier a été résolu, étonnamment, sans aucune perte pour Bitcoin.


Le message de Satoshi décrivait également une optimisation des performances pour Mining. La raison pour laquelle cela a été inclus dans un correctif de sécurité critique n'est pas claire, il est possible que le but était d'obscurcir le vrai problème. Cependant, il semble plus probable qu'il ait simplement publié ce qui se trouvait en tête de la branche de développement du dépôt Subversion, avec le correctif de sécurité ajouté.


À l'époque, il n'y avait pas autant d'utilisateurs qu'aujourd'hui, et la valeur de Bitcoin était proche de zéro. Si cette réponse au bug avait lieu aujourd'hui, elle serait considérée comme un véritable spectacle de merde pour de multiples raisons :



- Satoshi a fait une version binaire de la 0.3.5 contenant le correctif. Aucun correctif ou code n'a été fourni, peut-être dans le but d'obscurcir le problème.
- 0.3.5 [n'a même pas fonctionné] (https://bitcointalk.org/index.php?topic=626.msg6455#msg6455).
- Le correctif de la 0.3.6 était en fait un Hard Fork.


Un autre point discutable est de savoir s'il est bon ou mauvais que les utilisateurs aient été invités à éteindre leurs nœuds. Cela ne serait pas possible aujourd'hui, mais à l'époque, de nombreux utilisateurs suivaient activement les forums pour obtenir des mises à jour et étaient généralement au courant de la situation. Étant donné qu'il était possible de le faire, il aurait été judicieux de le faire.


#### 2010-08-15 Débordement de la sortie combinée (CVE-2010-5139)



À la mi-août 2010, l'utilisateur du forum Bitcointalk jgarzik, alias Jeff Garzik,

[découvert que](https://bitcointalk.org/index.php?topic=822.msg9474#msg9474) une certaine transaction à la hauteur du bloc 74638 avait deux sorties d'une valeur anormalement élevée :


```
"out" : [
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0xB7A73EB128D7EA3D388DB12418302A1CBAD5E890 OP_EQUALVERIFY OP_CHECKSIG"
},
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0x151275508C66F89DEC2C5F43B6F9CBE0B5C4722C OP_EQUALVERIFY OP_CHECKSIG"
}
]
```


> La "valeur de sortie" dans ce bloc #74638 est assez étrange :
>

> 92233720368.54277039 BTC ?  Est-ce que c'est UINT64_MAX, je me le demande ?

Il y avait vraisemblablement un bogue qui faisait que la somme des sorties de deux int64 (et non uint64, comme Garzik l'a supposé) débordait pour atteindre une valeur négative de -0,00997538 BTC. Quelle que soit la somme des entrées, la "somme" des sorties serait plus petite, ce qui rendrait cette transaction acceptable selon le code de l'époque.


Dans ce cas, le bogue avait été divulgué et publié par le biais d'un exploit réel. Malheureusement, environ 2 x 92 milliards de Bitcoin ont été créés, ce qui a fortement dilué la monnaie Supply d'environ 3,7 millions de pièces qui existait à l'époque.


Dans un fil de discussion connexe, [Satoshi a posté](https://bitcointalk.org/index.php?topic=823.msg9531#msg9531) qu'il apprécierait que les gens arrêtent Mining (ou *generating*, comme ils l'appelaient à l'époque) :


> Il serait utile que les gens arrêtent de générer.  Nous devrons probablement refaire une branche autour de la branche actuelle, et moins il y aura de generate, plus ce sera rapide.
>

> Un premier patch sera dans le SVN rev 132.  Il n'est pas encore téléchargé.  Je pousse d'abord d'autres changements divers, puis je mettrai en ligne le correctif pour ceci.

Son plan consistait à créer un Soft Fork pour invalider les transactions comme celle dont il est question ici, invalidant ainsi les blocs (en particulier le bloc 74638) qui contenaient de telles transactions. Moins d'une heure plus tard, il a déposé un [patch dans la révision 132](https://sourceforge.net/p/Bitcoin/code/132/) du dépôt Subversion et [posté sur le forum](https://bitcointalk.org/index.php?topic=823.msg9548#msg9548) décrivant ce qu'il pensait que les utilisateurs devaient faire :


> Le correctif est téléchargé dans le SVN rev 132 !
>

> Pour l'instant, les mesures recommandées :
> 1) Arrêter.
> 2) Téléchargez les fichiers blk de knightmb.  (remplacez vos fichiers blk0001.dat et blkindex.dat)
> 3) Mise à niveau.
> 4) Il devrait commencer avec moins de 74000 blocs. Laissez-le retélécharger le reste.
>

> Si vous ne voulez pas utiliser les fichiers de knightmb, vous pouvez simplement supprimer vos fichiers blk*.dat, mais le réseau sera très sollicité si tout le monde télécharge l'index des blocs en une seule fois.
>

> Je construirai des versions sous peu.

Il voulait que les gens téléchargent les données en bloc d'un utilisateur spécifique, à savoir knightmb, qui avait publié son Blockchain tel qu'il apparaissait sur son disque, les fichiers blkXXXX.dat et blkindex.dat. La raison du téléchargement des données Blockchain de cette manière, par opposition à une synchronisation à partir de zéro, était de réduire les goulets d'étranglement de la bande passante du réseau.


Il y avait un gros problème : les données que les utilisateurs téléchargeaient de knightmb [n'étaient pas vérifiées par le logiciel Bitcoin] (https://Bitcoin.stackexchange.com/a/113682/69518) au démarrage. Le fichier blkindex.dat contenait l'ensemble UTXO, et le logiciel acceptait toutes les données qu'il contenait comme s'il les avait déjà vérifiées. knightmb aurait pu manipuler les données pour se donner ou donner à quelqu'un d'autre quelques bitcoins.


Une fois de plus, les gens ont semblé être d'accord, et l'inversion du bloc invalide et de ses successeurs a été couronnée de succès. Les mineurs ont commencé à travailler sur un nouveau successeur au bloc [74637](https://Mempool.space/block/0000000000606865e679308edf079991764d88e8122ca9250aef5386962b6e84) et, selon le Timestamp du bloc, un successeur est apparu à 23:53 UTC, environ 6 heures après la découverte du problème. À 8 h 10 le lendemain, le 16 août, autour du bloc 74689, la nouvelle chaîne avait dépassé l'ancienne, et tous les nœuds non mis à niveau se sont donc réorganisés pour suivre la nouvelle chaîne. Il s'agit de la réorganisation la plus profonde - 52 blocs - de l'histoire de Bitcoin.


Comparé au problème de la OP_RETURN, ce problème a été traité d'une manière un peu plus propre :


- Pas de version binaire du correctif
- Le logiciel publié a fonctionné comme prévu
- Non Hard Fork


Il a également été demandé aux utilisateurs d'arrêter les Mining pendant cette période. Nous pouvons débattre de la question de savoir si c'est une bonne idée ou non, mais imaginez que vous êtes un Miner et que vous êtes convaincu que tous les blocs situés au-dessus du mauvais bloc seront finalement effacés lors d'une profonde réorganisation : pourquoi gaspilleriez-vous des ressources sur des blocs Mining condamnés ?


Vous pourriez également penser qu'il est un peu louche de faire ce que suggère Nakamoto et de télécharger le Blockchain, y compris l'ensemble UTXO, à partir du disque Hard d'un inconnu. Si c'est le cas, vous avez raison : c'est louche. Mais, compte tenu des circonstances, cette réaction d'urgence était judicieuse.


Il existe une différence importante entre ce cas et le cas précédent OP_RETURN : ce problème a été exploité dans la nature, et la correction a donc pu être faite plus simplement. Dans le cas de OP_RETURN, il a fallu obscurcir la correction et faire des déclarations publiques qui ne révélaient pas directement la nature du problème.


#### 2013-03-11 Problème de verrouillage de la base de données 0.7.2 - 0.8.0 (CVE-2013-3220)



Un problème très intéressant et très instructif est apparu en mars 2013. Il est apparu que le Blockchain s'était divisé (bien que le mot "Fork" soit utilisé dans la citation ci-dessous) après le bloc 225429. Les détails de cet incident ont été [rapportés dans le BIP50] (https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki). Le résumé dit :


> Un bloc contenant un plus grand nombre d'entrées de transactions que précédemment a été miné et diffusé. Les nœuds Bitcoin 0.8 ont pu le gérer, mais certains nœuds Bitcoin pré-0.8 l'ont rejeté, provoquant une Fork inattendue de la Blockchain. La chaîne incompatible pré-0.8 (ci-après, la chaîne 0.8) disposait alors d'environ 60 % de la puissance Mining Hash, ce qui a permis de ne pas résoudre automatiquement la scission (comme cela aurait été le cas si la chaîne pré-0.8 avait dépassé la chaîne 0.8 en termes de travail total, obligeant les nœuds 0.8 à se réorganiser en faveur de la chaîne pré-0.8).
>

> Afin de rétablir une chaîne canonique le plus rapidement possible, BTCGuild et Slush ont rétrogradé leurs nœuds Bitcoin 0.8 en 0.7 afin que leurs pools rejettent également le bloc le plus important. Cela a placé la majorité de la puissance de hachage sur la chaîne sans le bloc plus grand, ce qui a finalement conduit les nœuds 0.8 à se réorganiser vers la chaîne pré-0.8.

L'action rapide des pools Mining BTCGuild et Slush a été impérative dans cette situation d'urgence. Ils ont été capables de faire basculer la majorité de la puissance du Hash vers la branche pré-0.8 du split, et ainsi aider à restaurer le consensus. Cela a donné aux développeurs le temps de trouver une solution durable.


Ce qui est également très intéressant dans ce problème, c'est que la version 0.7.2 était incompatible avec elle-même, comme c'était le cas pour les versions précédentes. Ceci est expliqué dans la [section Cause première du BIP50] (https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki#root-cause) :


> Avec la configuration de verrouillage BDB insuffisamment élevée, il était implicitement devenu une règle de consensus du réseau déterminant la validité du bloc (bien qu'une règle de consensus de la BDB)
règle incohérente et peu sûre, puisque l'utilisation du verrou peut varier d'un nœud à l'autre).


En bref, le problème est que le nombre de verrous de base de données dont le logiciel Bitcoin Core a besoin pour vérifier un bloc n'est pas déterministe. Un nœud peut avoir besoin de X verrous tandis qu'un autre nœud peut avoir besoin de X+1 verrous. Les nœuds ont également une limite sur le nombre de verrous que Bitcoin peut prendre. Si le nombre de verrous nécessaires dépasse la limite, le bloc sera considéré comme invalide. Ainsi, si X+1 dépasse la limite mais pas X, les deux nœuds diviseront le Blockchain et ne seront pas d'accord sur la branche qui est valide.


La solution retenue, outre les mesures immédiates prises par les deux pools pour rétablir le consensus, a été la suivante



- limiter les blocs en termes de taille et de verrous nécessaires sur la version 0.8.1
- corriger les anciennes versions (0.7.2 et quelques autres plus anciennes) avec les mêmes nouvelles règles, et augmenter la limite globale de verrouillage.


À l'exception de l'augmentation de la limite de verrouillage global mentionnée au deuxième point, ces règles ont été mises en œuvre temporairement pour une durée prédéterminée. Il était prévu de supprimer ces limites une fois que la plupart des nœuds auraient été mis à niveau.


Cette Soft Fork a considérablement réduit le risque d'échec du consensus et, quelques mois plus tard, le 15 mai, les règles temporaires ont été désactivées de concert sur l'ensemble du réseau. Il convient de noter que cette désactivation était en fait une Hard Fork, mais qu'elle n'était pas litigieuse. En outre, elle a été publiée en même temps que la Soft Fork précédente, de sorte que les personnes utilisant le logiciel Soft-forked savaient parfaitement qu'une Hard Fork suivrait. Par conséquent, la grande majorité des nœuds sont restés dans le consensus lorsque la Hard Fork a été activée. Malheureusement, quelques nœuds qui n'ont pas été mis à niveau ont été perdus dans le processus.


On peut se demander si cela serait possible aujourd'hui. Le paysage Mining est plus complexe aujourd'hui et, en fonction de la puissance Hash de chaque côté de la scission, il pourrait être Hard de déployer assez rapidement un correctif tel que celui du BIP50. Il serait probablement Hard de convaincre les mineurs de la "mauvaise" branche de renoncer à leurs récompenses de bloc.


#### BIP66



Le BIP66 est intéressant parce qu'il souligne l'importance de :



- bonne sélection cryptographie
- divulgation responsable
- déploiement sans révéler la vulnérabilité
- Mining au sommet des blocs vérifiés


BIP66 était une proposition visant à renforcer les règles relatives aux encodages de signature dans le script Bitcoin. La [motivation] (https://github.com/Bitcoin/bips/blob/master/bip-0066.mediawiki#motivation) était de pouvoir analyser les signatures avec des logiciels ou des bibliothèques autres qu'OpenSSL et même des versions récentes d'OpenSSL. OpenSSL est une bibliothèque de cryptographie générale que Bitcoin Core utilisait à l'époque.


Le BIP a été activé le 4 juillet 2015. Toutefois, si ce qui précède est vrai, le BIP66 corrige également un problème beaucoup plus grave qui n'est pas mentionné dans le BIP.


##### La vulnérabilité



La divulgation complète de cette question a été publiée le 28 juillet 2015 par Pieter Wuille dans un article de

[email à la liste de diffusion Bitcoin-dev] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-July/009697.html) :


> Bonjour à tous,
>

> J'aimerais divulguer une vulnérabilité que j'ai découverte en septembre 2014 et qui est devenue inexploitable lorsque le seuil de 95 % de BIP66 a été atteint au début de ce mois.
>

> Description succincte :
>

> Une transaction spécialement conçue aurait pu faire bifurquer le Blockchain entre les nœuds :
>

> - l'utilisation d'OpenSSL sur les systèmes 32 bits et sur les systèmes Windows 64 bits
> - utiliser OpenSSL sur des systèmes non Windows 64 bits (Linux, OSX, ...)
> - utilisation de bases de code non OpenSSL pour l'analyse des signatures

Le courriel explique en détail comment le problème a été découvert et, plus précisément, ce qui l'a provoqué. À la fin, il soumet une chronologie des événements, dont nous reprendrons ici les plus importants. Certains d'entre eux ont déjà été décrits, comme l'illustre la figure ci-dessus.


![](assets/bip66-timeline-1.webp)


Chronologie des événements entourant le BIP66. Les éléments en noir ont été expliqués ci-dessus.


##### Avant la découverte



Sans que personne ne soit au courant de ce problème, il aurait pu être résolu par la BIP62, qui était une proposition visant à réduire les possibilités de malléabilité des transactions. Parmi les changements proposés dans le BIP62 figurait le renforcement des règles de consensus pour l'encodage des signatures, ou "encodage DER strict". Pieter Wuille a proposé quelques modifications au BIP en juillet 2014, qui auraient permis de résoudre le problème :


> 2014-Jul-18 : Afin que les règles d'encodage de signature de Bitcoin ne dépendent pas de l'analyseur spécifique d'OpenSSL, j'ai modifié la proposition BIP62 pour que son exigence stricte de signatures DER s'applique également aux transactions de la version 1. À l'époque, plus aucune signature non DER n'était extraite des blocs, de sorte que l'on a supposé que cela n'aurait aucun impact. Voir https://github.com/Bitcoin/bips/pull/90 et http://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2014-July/006299.html. Inconnu à l'époque, mais s'il avait été déployé, il aurait permis de résoudre la vulnérabilité.

En raison de l'ampleur de ce BIP, qui couvrait bien plus que le simple "codage DER strict", il a été constamment modifié et n'a jamais pu être déployé. Le BIP a été retiré par la suite, car le Segregated Witness, BIP141, a résolu la malléabilité des transactions d'une manière différente et plus complète.


##### Après la découverte



OpenSSL a publié de nouvelles versions de son logiciel avec des correctifs qui, s'ils avaient été utilisés dans Bitcoin depuis le début, auraient résolu le problème. Cependant, l'utilisation de toute nouvelle version d'OpenSSL uniquement dans une nouvelle version de Bitcoin Core ne ferait qu'empirer les choses. Gregory Maxwell explique cela dans un autre [email thread] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-January/007097.html) en janvier 2015 :


> Alors que pour la plupart des applications, il est généralement acceptable de rejeter avec empressement certaines signatures, Bitcoin est un système consensuel dans lequel tous les participants doivent être d'accord sur la validité ou l'invalidité exacte des données d'entrée.  Dans un sens, la cohérence est plus importante que la "justesse".
> [...]
> Les correctifs ci-dessus ne corrigent toutefois qu'un symptôme du problème général : le recours à des logiciels non conçus ou distribués pour une utilisation consensuelle (en particulier OpenSSL) pour un comportement conforme aux normes consensuelles.  Par conséquent, en tant qu'amélioration progressive, je propose un Soft-Fork ciblé pour appliquer bientôt une stricte conformité DER, en utilisant un sous-ensemble de BIP62.

Il souligne que l'utilisation d'un code qui n'est pas destiné à être utilisé dans les systèmes de consensus présente de sérieux risques, et propose que le Bitcoin mette en œuvre un codage DER strict. Il s'agit là d'un exemple très clair de l'importance d'une bonne cryptographie de sélection.


Ces événements pourraient vous donner l'impression que Gregory Maxwell connaissait la vulnérabilité que Pieter Wuille a publiée plus tard, mais qu'il a voulu aider à introduire en douce un correctif déguisé en mesure de précaution, sans trop attirer l'attention sur le problème réel. C'est peut-être le cas, mais il s'agit d'une pure spéculation.


Ensuite, comme l'a proposé Maxwell, le BIP66 a été créé comme un sous-ensemble du BIP62 qui ne spécifiait que l'encodage DER strict. Ce BIP a apparemment été largement accepté et déployé en juillet, bien que deux scissions de Blockchain se soient ironiquement produites en raison de *Mining sans validation*. Ces scissions sont discutées dans la section suivante.


![](assets/bip66-timeline-2.webp)


Il en ressort que les BIP doivent être plus ou moins *atomiques*, c'est-à-dire qu'ils doivent être suffisamment complets pour fournir quelque chose d'utile ou résoudre un problème spécifique, mais suffisamment petits pour permettre un large soutien de la part des utilisateurs. Plus vous mettez de choses dans un BIP, plus les chances qu'il soit accepté sont faibles.


##### Séparations dues à la validation sans validation Mining



Malheureusement, l'histoire du BIP66 ne s'est pas arrêtée là. Lorsque le BIP66 a été activé, il s'est avéré assez désordonné parce que certains mineurs n'ont pas vérifié les blocs qu'ils essayaient d'étendre. C'est ce qu'on appelle la Mining sans validation, ou SPV-Mining (Simplified Payment Verification). Un message d'alerte a été envoyé aux nœuds Bitcoin avec un lien vers [une page web décrivant le problème] (https://Bitcoin.org/en/alert/2015-07-04-spv-Mining) :


> Tôt dans la matinée du 4 juillet 2015, le seuil de 950/1000 (95 %) a été atteint. Peu de temps après, un petit Miner (faisant partie des 5 % non améliorés) a miné un bloc invalide - ce qui était prévisible. Malheureusement, il s'est avéré qu'environ la moitié du taux Hash du réseau était Mining sans validation complète des blocs (appelé SPV Mining), et a construit de nouveaux blocs au-dessus de ce bloc invalide.

La page d'alerte demandait aux utilisateurs d'attendre 30 confirmations supplémentaires au cas où ils utiliseraient des versions plus anciennes de Bitcoin Core.


La scission mentionnée ci-dessus s'est produite le 2015-07-04 à 02:10 UTC après la hauteur du bloc [363730](https://Mempool.space/block/000000000000000006a320d752b46b532ec0f3f815c5dae467aff5715a6e579e). Ce problème a été résolu à 03:50 le même jour, après que 6 blocs invalides aient été minés. Malheureusement, le même problème s'est reproduit le lendemain, c'est-à-dire le 2015-07-05 à 21:50, mais cette fois la branche invalide n'a duré que 3 blocs.


![](assets/bip66-timeline-3.webp)

Les événements qui ont conduit à BIP66, son déploiement et ses conséquences constituent une très bonne étude de cas qui montre à quel point les développeurs de Bitcoin doivent être prudents. Quelques éléments clés à retenir de BIP66 :



- L'équilibre entre l'ouverture et le fait de ne pas publier une vulnérabilité est délicat à trouver.
- Le déploiement de correctifs pour les vulnérabilités non publiées est un jeu délicat.
- Le consensus de maintien est le Hard.
- Les logiciels qui ne sont pas destinés aux systèmes consensuels sont généralement risqués.
- Les BIP devraient être quelque peu atomiques.


### Conclusion à propos de When Shit Hits The Fan



Bitcoin a des bugs. Les personnes qui découvrent des bogues sont encouragées à les divulguer de manière responsable aux développeurs de Bitcoin, afin qu'ils puissent corriger le bogue sans le révéler publiquement. Idéalement, la correction du bogue peut être déguisée en amélioration des performances, ou en un autre écran de fumée.


Nous avons examiné certains des problèmes les plus graves qui sont apparus au fil des ans et la manière dont ils ont été traités. Certains ont été découverts publiquement grâce à des exploits, tandis que d'autres ont été divulgués de manière responsable et ont pu être corrigés avant que des acteurs malveillants n'aient la possibilité de les exploiter.


## Questions de discussion

<chapterId>91462ca7-f09c-55da-a5b9-3e211de31da5</chapterId>


Ces questions de discussion ne sont pas seulement un récapitulatif du contenu de "Bitcoin development philosophy", elles ont pour but de vous encourager à faire des recherches plus approfondies, alors n'hésitez pas à sortir et à explorer.


Vous pouvez tester la profondeur de votre compréhension en rédigeant un [mini-essai] (https://www.youtube.com/watch?v=N4YjXJVzoZY) de 100 à 300 mots en choisissant un sujet dans cette liste de questions. Si vous souhaitez obtenir un retour sur votre travail, vous pouvez l'envoyer à mini-essay@planb.network, nous serons ravis de l'examiner.


#### Décentralisation



- La décentralisation est Hard. Pourquoi se donner tant de mal pour la faire fonctionner ? Pourrions-nous opter pour une approche hybride, où certaines parties sont centralisées et d'autres non ?
- La décentralisation introduit-elle le problème de la double dépense ou le problème de la double dépense nécessite-t-il la décentralisation ? Comment Satoshi a-t-il résolu le problème de la double dépense ?
- Dans quels domaines Bitcoin est-il encore le plus sujet à la censure, et pourquoi la censure est-elle une si mauvaise chose ? Existe-t-il des arguments en faveur de la censure ?
- Il est indiqué que le Bitcoin n'est pas autorisé. Existe-t-il d'autres méthodes de paiement que l'on pourrait considérer comme sans autorisation ?



#### L'absence de confiance




- L'absence de confiance est souvent un spectre, et non une brique. Quels sont les aspects de Bitcoin qui sont plutôt Trustless, et quels sont ceux qui impliquent généralement un niveau de confiance plus élevé ? Peut-on les atténuer ?
- Vous souhaitez exécuter un Full node pour pouvoir valider entièrement toutes les transactions. Vous téléchargez Bitcoin Core à partir de https://Bitcoin.org/en/download. Où avez-vous placé votre confiance et où en êtes-vous avec Trustless ?
- Est-il possible de construire un système Trustless au-dessus d'un système de confiance ?



#### Vie privée




- Quels sont les principaux avantages qu'un utilisateur retire du respect de sa vie privée lorsqu'il interagit avec Bitcoin ? Quels sont les avantages altruistes pour le réseau ?
- Comment la réutilisation des adresses affecte-t-elle votre vie privée ?
- La Bitcoin utilise un modèle UTXO, alors que certaines crypto-monnaies alternatives utilisent un modèle de compte. Quelles sont les implications de ce choix sur la protection de la vie privée ?



#### Fini Supply




- Quelle est la relation entre la Bitcoin finie et la Supply et son émission de pièces par le biais de la Coinbase Transaction ? Quelle est la relation entre l'émission de pièces et le budget de sécurité, et comment s'opposent-ils ?
- Quels paramètres Satoshi aurait-il pu modifier pour changer le plafond Bitcoin de la Supply ? Qu'est-ce qui changerait s'il avait décidé de plafonner la Supply à 1 million ? Qu'en serait-il d'un trillion ?
- Pourquoi certaines personnes préconisent-elles une augmentation de Bitcoin Supply ? Pensez-vous que cela se produira ?


#### Mise à niveau



- Qu'est-ce que le procès rapide et pourquoi était-il nécessaire d'activer Taproot ?
- Pourquoi avons-nous besoin d'un pourcentage aussi élevé de mineurs pour procéder à une mise à niveau dans le cadre d'un softfork ? Pourquoi le seuil n'est-il pas simplement de 51 % ?



#### Pensée contradictoire




- Qu'est-ce qu'une attaque de type "sybil" et pourquoi un réseau décentralisé y est-il si vulnérable ?
- Pourquoi est-il important que tous les acteurs du réseau Bitcoin - et pas seulement les développeurs - pensent de manière contradictoire ?



#### Source ouverte




- Seule une poignée de mainteneurs ont les permissions GitHub nécessaires pour fusionner le code dans le dépôt [Bitcoin Core](https://github.com/Bitcoin/Bitcoin). Cela ne va-t-il pas à l'encontre d'un réseau sans permission ?
- Le processus de développement des logiciels libres est-il susceptible de faire l'objet d'une attaque de type "sybil" ? Dans l'affirmative, comment y remédier ?
- Quels sont les avantages et les inconvénients de s'appuyer sur des bibliothèques open source tierces, et quelle est l'approche adoptée avec Bitcoin Core ?
- De quelle manière avons-nous besoin d'un examen plus approfondi que l'examen du code ? Comment déterminer quelle quantité de révision est suffisante ?
- Comment s'assurer qu'il y aura toujours suffisamment de personnes compétentes pour travailler sur Bitcoin ? Que se passe-t-il lorsqu'il n'y en a pas, et comment évaluer leur intégrité et leurs intentions ?



#### Mise à l'échelle




- L'argument avancé est que le sharding offre des avantages en termes d'échelle au prix de la complexité. Pourquoi devrions-nous ou ne devrions-nous pas adopter des améliorations technologiques parce qu'elles sont difficiles à comprendre, même si elles semblent technologiquement valables ?
- Quels sont les exemples de méthodes d'échelonnement vers l'intérieur introduites dans Bitcoin ?
- Pourquoi l'extension verticale est-elle beaucoup plus difficile dans un système décentralisé ? Qu'en est-il de la mise à l'échelle horizontale ?
- Il semble que nous ne soyons pas près de parvenir à un consensus sur la manière dont nous pourrions embarquer le monde entier sur Bitcoin. Satoshi n'aurait-elle pas dû au moins réfléchir à un moyen d'y parvenir, avant Mining, le premier bloc de 2009 ?
- Comment classeriez-vous (verticalement, horizontalement, vers l'intérieur ou pas une technique de mise à l'échelle) chacun des éléments suivants : sharding, augmentation de la taille des blocs, SegWit, nœuds SPV, échanges centralisés, Lightning Network, diminution de l'intervalle entre les blocs, Taproot, sidechains



# Section finale


<partId>4b6ff4ef-b9ea-4c48-b05f-62d41a38fbbb</partId>


## Critiques et évaluations


<chapterId>d334a837-df46-4989-9cad-8d8779147dbe</chapterId>


<isCourseReview>true</isCourseReview>

## Conclusion


<chapterId>b77ed55c-b13a-430b-a212-37aab527b9e7</chapterId>


<isCourseConclusion>true</isCourseConclusion>