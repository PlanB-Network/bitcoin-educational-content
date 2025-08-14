---
name: Mettre en place son premier nœud Bitcoin
goal: Comprendre, installer, configurer et utiliser un nœud Bitcoin
objectives:
  - Comprendre le rôle et l’utilité d’un nœud Bitcoin.
  - Identifier les différentes solutions logicielles et matérielles disponibles.
  - Installer et configurer un nœud complet (Bitcoin Core).
  - Utiliser l’interface Umbrel et y ajouter des applications utiles.
  - Connecter un portefeuille personnel à son propre nœud.
  - Explorer les réglages avancés et les bonnes pratiques de sécurité.
---
# Devenez un bitcoiner souverain

Vous connaissez sans doute l’adage "*Pas tes clés, pas tes coins*", qui encourage la self-custody de vos bitcoins. Détenir ses propres clés constitue en effet une première étape indispensable, mais elle ne suffit pas. Pour obtenir une véritable souveraineté monétaire, il est également nécessaire d’installer et d’utiliser votre propre nœud Bitcoin. Ce cours a justement pour objectif de vous guider dans cette étape fondamentale de votre parcours de bitcoiner !

BTC 202 est une formation accessible et concrète, conçue pour vous apprendre à faire tourner votre propre nœud Bitcoin, même si vous n’êtes pas un expert technique. Nous commencerons par définir ce qu’est un nœud Bitcoin, à quoi il sert, et pourquoi il est absolument essentiel d’en faire tourner un par soi-même. Je vous guiderai ensuite pas à pas dans le choix de votre matériel, l’installation des logiciels nécessaires, la connexion de votre portefeuille et les premières optimisations possibles pour aller plus loin.

Cette formation s’adresse à tous les utilisateurs de Bitcoin qui ne disposent pas encore de nœud ou qui n’en perçoivent pas pleinement l’utilité. Que vous soyez débutant, simple curieux ou utilisateur expérimenté désireux de mieux appréhender cette composante essentielle du système imaginé par Satoshi Nakamoto, vous y trouverez des explications claires, des tutoriels pratiques et des conseils adaptés à votre niveau.

Faire tourner un nœud Bitcoin, ce n’est pas une option réservée aux experts. C’est un outil de résilience que chaque utilisateur doit comprendre et mettre en place. Ce cours est votre point de départ pour devenir un bitcoiner souverain !


+++




# Introduction
<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>


## Aperçu du cours
<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>

Présentation générale de la formation.













## Qu’est-ce qu’un nœud Bitcoin ?
<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>

Comme le décrit Satoshi Nakamoto, son créateur, Bitcoin se présente comme un système de cash électronique pair-à-pair. Cette simple phrase, qui est le titre du White Paper, recèle de nombreux éléments pour cerner la nature de Bitcoin :
- Tout d’abord, Satoshi qualifie Bitcoin de "système", autrement dit, un ensemble cohérent de composants matériels et logiciels qui interagissent pour fournir un service ou remplir une fonction précise ;
- Ensuite, il explique que ce système permet l’utilisation d’un cash électronique, c’est-à-dire une forme de monnaie immatérielle ;
- Enfin, il précise que ce système ne dépend d’aucune entité centrale : il est "pair-à-pair", ce qui signifie que ce sont les utilisateurs eux-mêmes qui font fonctionner le système.

Puisque Bitcoin est un système, il doit nécessairement être exécuté sur des ordinateurs. Et, du fait de son caractère pair-à-pair, ce sont les utilisateurs eux-mêmes qui assument la responsabilité de faire tourner ces machines.

Ce que l'on appelle un "nœud Bitcoin", c'est justement cet ordinateur sur lequel s’exécute un logiciel qui implémente le protocole Bitcoin (comme Bitcoin Core, mais nous y reviendrons plus tard). C’est ce qui permet à Bitcoin de fonctionner sans autorité centrale : la validation est assurée de manière distribuée, par des milliers de machines indépendantes appartenant à des milliers d'utilisateurs.

Ce sont précisément ces utilisateurs qui assurent la sécurité de Bitcoin. Comme l’expose Eric Voskuil dans son ouvrage *Cryptoeconomics*, la sécurité de Bitcoin ne repose ni sur la blockchain, ni sur la puissance de hachage, ni sur la validation, la décentralisation, la cryptographie, l’open-source ou la théorie des jeux. La sécurité de Bitcoin dépend avant tout des personnes qui acceptent de s’exposer à des risques personnels. La décentralisation permet de répartir cette prise de risque sur de nombreux individus et seule leur capacité à résister assure la robustesse du système.

Ce principe est facile à comprendre : si Bitcoin dépendait d’un unique nœud détenu par une seule personne, il suffirait d’emprisonner cette personne pour mettre fin au réseau, puisqu'elle assumerait seule tous les risques. Avec des dizaines de milliers de nœuds répartis dans le monde, le risque est disséminé : il faudrait neutraliser chacun de ces opérateurs pour éteindre Bitcoin.

On peut ainsi distinguer et nommer plusieurs concepts pour clarifier les choses pour la suite de ce cours :
- La monnaie bitcoin : l’unité de compte utilisée pour les transactions au sein de ce système ;
- Le réseau Bitcoin : l’ensemble constitué par tous les nœuds connectés ;
- Les nœuds Bitcoin : les machines exécutant une implémentation de Bitcoin ;
- Les implémentations de Bitcoin : les logiciels qui traduisent le protocole en instructions exécutables ;
- Le protocole Bitcoin : l’ensemble des règles qui régissent le fonctionnement du système ;
- Le système Bitcoin : la combinaison cohérente de l’ensemble de ces éléments.

### Le rôle du nœud Bitcoin

L'ensemble des nœuds Bitcoin représente donc ce que l'on appelle le réseau Bitcoin. Ce sont eux qui permettent à l’ensemble du système de fonctionner de manière autonome, sans recours à une autorité centrale ni à une hiérarchie de serveurs.

Dès l’origine, Bitcoin a été conçu pour que chaque utilisateur exécute un nœud personnel. C’est encore ce que propose le logiciel Bitcoin Core aujourd'hui, qui combine à la fois le rôle de portefeuille et le rôle de nœud. Mais de nos jours, cette fonction est souvent dissociée : beaucoup de portefeuilles Bitcoin modernes sont juste des portefeuilles qui se connectent à des nœuds externes (possédés par la même personne ou non).

#### Conserver la blockchain

La première mission d’un nœud consiste à conserver une copie locale de la blockchain. Pour empêcher la double dépense sur Bitcoin sans faire appel à une autorité centrale, chaque utilisateur doit vérifier la non existence d'une transaction dans le système. La seule manière d’en être certain est de connaître l’ensemble des transactions passées sur Bitcoin. C’est pourquoi toutes les transactions sont horodatées et regroupées dans des blocs, et chaque nœud stocke l’intégralité de la blockchain.

> Le seul moyen pour confirmer l’absence d’une transaction est d’être au courant de toutes les transactions.

Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://bitcoin.org/bitcoin.pdf

La blockchain est donc un registre évolutif : à chaque nouveau bloc publié par un mineur, le nœud en vérifie la validité avant de l’ajouter à sa propre copie locale de la chaîne. Aujourd’hui (juillet 2025), la blockchain complète dépasse les 675 Go, et cette taille continue d’augmenter, puisqu'un nouveau bloc est ajouté en moyenne toutes les 10 minutes.

Le nœud conserve également, en local, l’ensemble des UTXOs existants à un instant donné : il s’agit de ce que l’on appelle l’**UTXO set**. Cette base de données rassemble tous les fragments de bitcoins en attente d’être dépensés. Nous reviendrons en détail sur ce sujet dans la dernière partie de la formation.

#### Vérifier et diffuser les transactions

Le deuxième rôle d’un nœud est d’assurer la vérification et la propagation des transactions. Lorsqu’une nouvelle transaction parvient au nœud (soit via un logiciel de portefeuille, soit via un autre nœud), il va vérifier qu'elle respecte bien un ensemble de règles (règles de consensus et règles de relais). Par exemple :
- les bitcoins dépensés doivent exister dans son UTXO set (la base de données des sorties non dépensées) ;
- la signature doit être valide, et toutes les conditions de dépense doivent être respectées (script valide) ;
- le montant total des outputs ne doit pas dépasser celui des inputs, ce qui signifie que les frais ne peuvent être négatifs…

Après validation, la transaction est enregistrée dans la mempool du nœud, un espace mémoire temporaire réservé aux transactions non confirmées, puis relayée aux autres pairs du réseau auxquels il est connecté. Ce mécanisme de diffusion et de validation se poursuit de nœud en nœud. Ainsi, la transaction se propage sur le réseau Bitcoin, et chaque nœud la conserve en mempool jusqu’à son inclusion dans un bloc valide par un mineur, qui actera alors sa première confirmation.

#### Vérifier et diffuser les blocs

Le troisième rôle du nœud concerne la gestion des blocs minés. Lorsqu’un mineur découvre un nouveau bloc doté d’une preuve de travail valide, il le diffuse sur le réseau. Les nœuds le reçoivent, en vérifient la conformité avec l’ensemble des règles du protocole, puis l’intègrent à leur propre copie locale de la blockchain s’il est valide. Comme pour les transactions, les nouveaux blocs validés sont ensuite relayés à l’ensemble des pairs connectés au nœud. Ce processus se poursuit jusqu’à ce que tous les nœuds du réseau Bitcoin aient connaissance de ce nouveau bloc.

## Quelle est la différence entre un nœud et un portefeuille ?

Il convient de bien distinguer deux types de logiciels différents dans l’utilisation de Bitcoin : le nœud et le portefeuille.

Un nœud Bitcoin, comme nous l’avons évoqué précédemment, est un logiciel qui participe activement au réseau pair-à-pair. Il assure principalement trois missions :
- la sauvegarde de la blockchain,
- la validation et le relais des transactions,
- la validation et le relais des blocs.

Un portefeuille Bitcoin, quant à lui, est un logiciel dont la vocation première est de stocker et de gérer vos clés privées. Ces clés permettent de dépenser vos bitcoins en satisfaisant les scripts de verrouillage (généralement à l’aide d’une signature). Un portefeuille peut se connecter à un nœud (qu’il soit local ou distant) afin de consulter l’état de la blockchain et de diffuser les transactions qu’il construit, mais il n’est pas, en tant que tel, un participant du réseau.

Dans certains cas, ces deux fonctions coexistent au sein d’un même logiciel, comme c’est le cas de Bitcoin Core qui fait office à la fois de nœud complet et de portefeuille. Toutefois, beaucoup de logiciels de portefeuilles populaires (Sparrow, BlueWallet, etc.) doivent être connectés à un nœud externe (qu’il s’agisse du vôtre ou de celui d’un tiers) pour diffuser les transactions et connaitre le solde du portefeuille.

## Quelle est la différence entre un nœud et un mineur ?

Les notions de nœud et de mineur sont souvent confondues. Pourtant, ces deux éléments remplissent des fonctions radicalement différentes au sein du système.

Initialement, lorsque Bitcoin fut lancé par Satoshi Nakamoto en 2009, chaque utilisateur était censé participer au réseau dans sa globalité. Ainsi, le logiciel Bitcoin original combinait plusieurs fonctions à la fois : il faisait office de portefeuille, de nœud et également de mineur, capable de générer de nouveaux blocs. À cette période, la difficulté de minage était très basse. Il suffisait alors de faire fonctionner le logiciel Bitcoin sur son ordinateur pour trouver des blocs et recevoir des bitcoins en récompense.

Cependant, avec la popularisation progressive de Bitcoin et l'augmentation du nombre de mineurs, la concurrence dans le minage a radicalement changé la donne. Aujourd’hui, le minage est devenu une activité extrêmement compétitive, dominée par des acteurs industriels équipés d’infrastructures spécialisées. La puissance nécessaire pour miner un nouveau bloc est désormais si importante qu'il est pratiquement impossible pour un utilisateur particulier d'y parvenir en utilisant uniquement un ordinateur classique. Ainsi, le minage se fait désormais essentiellement à l'aide de machines spécialisées appelées ASIC (*Application Specific Integrated Circuits*). Ces puces sont optimisées exclusivement pour exécuter du double SHA-256, l'algorithme utilisé pour le minage sur Bitcoin.

Face à cette évolution, le rôle du nœud Bitcoin et celui du mineur se sont clairement distingués. Comme vu précédemment, le rôle du nœud Bitcoin est purement informationnel et validateur. Le rôle du mineur est différent :
- Il sélectionne les transactions en attente dans la mempool ;
- Il construit un bloc candidat intégrant ces transactions ;
- Il cherche par tâtonnement une preuve de travail valide ; 
- S'il trouve une preuve valide, il diffuse le bloc via son nœud aux autres nœuds.

Un mineur a en effet obligatoirement besoin d'un nœud Bitcoin afin d'interagir avec le réseau.

On différencie également parfois le rôle du mineur de celui du hacheur. Un hacheur est une machine qui a pour tâche de hacher des blocs templates fournis par le serveur d'une pool, en recherchant des hachages qui satisfont la cible de difficulté définie pour les shares, et non celle de Bitcoin. Le reste du processus de minage, qui inclut la construction effective des blocs, la sélection des transactions ou la recherche de la preuve de travail selon la difficulté propre à Bitcoin, ainsi que la diffusion, est effectué directement par les pools.

Enfin, il y a une différence fondamentale en termes d'incitation économique entre le mineur et le nœud. Faire tourner un nœud Bitcoin ne procure aucun avantage pécuniaire direct. En revanche, participer au minage permet de percevoir des récompenses (subvention et frais de transactions) à chaque bloc trouvé.

Dans la partie 2, nous explorerons plus en détail les bénéfices pratiques et personnels liés à l'installation et à l'utilisation d'un nœud Bitcoin, au-delà du simple intérêt financier.

## Bitcoin Core et les implémentations du protocole
<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>

Le protocole Bitcoin n’est pas un logiciel : c’est un ensemble de règles tacites partagées entre les utilisateurs du réseau. Il définit les conditions de validité d’une transaction, les mécanismes de création monétaire, le format des blocs, les conditions de preuve de travail et de nombreuses autres spécifications. Pour interagir avec ce protocole, les utilisateurs doivent faire tourner un logiciel qui implémente ces règles : c’est ce que l’on appelle une **implémentation** de Bitcoin.

Une implémentation est donc un logiciel de nœud : un programme capable de s’interfacer avec d’autres machines du réseau Bitcoin, de télécharger, vérifier, stocker et propager des blocs et des transactions, et de faire respecter localement les règles du consensus et des règles de relais. Chaque implémentation est une interprétation concrète du protocole, écrite dans un langage de programmation donné, avec des choix d’architecture, de performances et d’ergonomie propres. Chaque implémentation va aussi avoir sa propre organisation de développement, avec des répartitions de responsabilités.

Parmi ces implémentations, une domine très largement : **Bitcoin Core**.

### Une implémentation historique devenue référence

Bitcoin Core est le logiciel de référence du protocole Bitcoin. Il est issu du code original écrit par Satoshi Nakamoto en 2008-2009, et en constitue la continuité directe. Initialement connu sous le nom de "*Bitcoin*", puis "*Bitcoin QT*" (en raison de l’ajout d’une interface graphique via la bibliothèque Qt), il a été rebaptisé "*Bitcoin Core*" en 2014 pour bien différencier le logiciel du réseau. Depuis la version 0.5, il est distribué avec deux composants : `bitcoin-qt` (l’interface graphique) et `bitcoind` (l'interface en ligne de commande).

Bitcoin Core ne représente théoriquement pas le protocole Bitcoin, mais seulement une implémentation parmi d’autres. Il se distingue toutefois par son adoption massive, son ancienneté, la robustesse de son code, et la rigueur de son processus de développement. En conséquence, dans la pratique, les règles appliquées par Bitcoin Core sont de facto celles du protocole Bitcoin : les utilisateurs, développeurs, mineurs et services de l’écosystème s’y réfèrent presque exclusivement.

### Répartition actuelle des implémentations

Selon [les données collectées en juillet 2025 par Luke Dashjr](https://luke.dashjr.org/programs/bitcoin/files/charts/software.html) (développeur bien connu dans l’écosystème), la répartition des implémentations parmi les nœuds publics du réseau est la suivante :
- **Bitcoin Core** : 89 % des nœuds
- **Bitcoin Knots** : 10,5 %
- **Autres implémentations cumulées** : 0,5 % (btcsuite, Bcoin, BTCD...)

Autrement dit, environ 9 nœuds publics sur 10 font tourner Bitcoin Core. Le reste du réseau repose sur des clients plus marginaux (bien que la part de Knots ait fortement progressé ces derniers mois, notamment à la suite des débats concernant la limite de taille des OP_RETURN). Ils sont souvent maintenus par une seule personne ou une petite équipe.

**Note :** Ces chiffres demeurent néanmoins des estimations, car ils se fondent avant tout sur les *listening nodes*, c’est-à-dire les nœuds acceptant les connexions entrantes (avec le port 8333 ouvert). Les *non-listening nodes* sont beaucoup plus complexes à recenser, puisqu’il est impossible de s’y connecter directement : il faut attendre que l’initiative vienne d’eux, sous forme de connexion sortante. Le site de Luke Dashjr affirme tenter de comptabiliser également ces *non-listening nodes*, mais il demeure impossible d’obtenir des données parfaitement exactes à leur sujet, et la mise à jour de ces statistiques accuse forcément un certain retard par rapport à la réalité.

### Fonctionnement interne de Bitcoin Core

Bitcoin Core est un logiciel monolithique (tous les composants sont regroupés en un seul bloc indivisible) écrit en C++. C'est également un projet open-source sans véritable hiérarchie formelle. Il est maintenu par une communauté de développeurs bénévoles ou rémunérés par des entités diverses (souvent par des entreprises de l’écosystème qui ont intérêt à ce que le développement de Core se déroule favorablement). [Le code est hébergé sur GitHub](https://github.com/bitcoin/bitcoin), et le développement suit un modèle rigoureux :
- Les **contributeurs** soumettent des propositions sous forme de _pull requests_ (PR). En principe, n'importe qui peut proposer une modification, mais celle-ci doit être testée, documentée et passer par un processus de relecture par les pairs ;
- Les **mainteneurs** ont le droit d’approuver et de fusionner les PR. Ce sont eux qui garantissent la cohérence et la stabilité du projet. En juillet 2025, ils sont cinq : Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao et Ryan Ofsky ;
- Il n’existe plus de **mainteneur principal** depuis février 2023. Ce rôle avait été tenu naturellement par Satoshi Nakamoto au lancement de Bitcoin, puis par Gavin Andresen suite au départ de Nakamoto début 2011, et enfin par Wladimir J. Van Der Laan de 2014 à 2023.

Le développement de Bitcoin Core suit une logique de méritocratie : les nouveaux contributeurs sont encouragés à relire et tester le code avant d’en proposer eux-mêmes. Les décisions sont fondées sur le consensus technique, et les modifications importantes (notamment en matière de consensus) nécessitent des discussions en amont sur des canaux publics comme les mailing lists ou les clubs de revue de PR.

### Les autres implémentations de Bitcoin

Bien que marginales en termes d’adoption, d’autres clients existent. Le principal est Bitcoin Knots, développé par Luke Dashjr. Il s’agit d’un fork de Bitcoin Core qui intègre des options supplémentaires et une vision plus conservatrice du développement. Il propose notamment des restrictions renforcées en matière de format de transaction.

On peut aussi mentionner :
- **Libbitcoin** : une bibliothèque C++ modulaire développée par Amir Taaki et maintenue par Eric Voskuil ;
- **Bcoin** : une implémentation en JavaScript, qui n’est plus maintenue activement ;
- **BTCD/btcsuite** : une implémentation en Go.

Ces projets contribuent à la diversité de l’écosystème, mais leur adoption reste très limitée, ce qui rend difficile toute évolution indépendante de Bitcoin Core.

### Le pouvoir des développeurs de Core

On pourrait croire que les développeurs de Bitcoin Core ont un contrôle direct sur Bitcoin, mais ce n’est pas le cas. Ils ne peuvent pas imposer une modification du protocole. Leur rôle est de proposer du code. C’est chaque utilisateur, via son nœud, qui décide d'utiliser ce code ou non.

Cela signifie que si un changement dans Bitcoin Core ne fait pas consensus, il peut être ignoré par les nœuds, soit en ne mettant pas à jour Bitcoin Core, soit tout simplement en changeant d'implémentation. À l’inverse, si une fonctionnalité souhaitée par les utilisateurs est bloquée dans le processus de développement de Core, il est toujours possible de passer sur une autre implémentation ou de forker le projet.

Comme nous l’aborderons plus loin dans ce cours, ce sont les nœuds, en fonction de leur poids économique (c’est-à-dire les commerçants) qui confèrent son utilité à une version du protocole (et donc à la monnaie correspondante), en acceptant les unités qui respectent ses règles. Le véritable pouvoir de gouvernance sur Bitcoin appartient donc à ces commerçants, et non aux développeurs.


















# Devenir un bitcoiner souverain
<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>


## Pourquoi faire tourner son propre nœud ?
<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>

Il existe une idée reçue selon laquelle exploiter un nœud Bitcoin relèverait d’un acte purement altruiste, sans bénéfice personnel, simplement au service de la décentralisation du réseau. Certains considèrent ainsi que ce serait une forme de devoir pour les bitcoiners, dans le but de soutenir le système et de témoigner leur reconnaissance envers Bitcoin.

En effet, comme nous l’avons souligné dans les chapitres précédents, faire tourner un nœud ne procure pas de gain financier direct. On pourrait donc penser qu’il n’y a aucun intérêt personnel à le faire. Pourtant, exploiter son propre nœud apporte de nombreux avantages individuels. Pour vous en convaincre, je vais présenter dans ce chapitre l’ensemble des raisons, tant techniques que stratégiques, qui devraient vous inciter à installer et à utiliser votre propre nœud Bitcoin.

### Diffusion plus confidentielle de ses transactions

Lorsqu’un logiciel de portefeuille se connecte à un nœud externe, il transmet ses transactions à une infrastructure qui vous échappe. Cela engendre des risques évidents de surveillance : l’opérateur du nœud distant peut analyser les détails de vos transactions, les montants, la fréquence des opérations et, en recoupant certaines métadonnées (adresse IP, horaires, localisation…), potentiellement les associer à votre identité.

En effet, comme souligné dans un chapitre précédent, les portefeuilles ne communiquent pas avec le réseau Bitcoin par magie : ils doivent obligatoirement se connecter à un nœud pour consulter le solde ou diffuser des transactions. Si vous n’avez jamais configuré votre propre nœud, cela signifie que votre portefeuille dépend de l’infrastructure d’un tiers (le plus souvent celle de l’entreprise à l’origine du logiciel). Or, ce tiers, surtout s’il s’agit d’une entreprise, peut observer, exploiter ou même divulguer ces données : que ce soit dans une logique commerciale, sous contrainte légale, ou à la suite d’un piratage.

En faisant utilisant votre propre nœud, vous diffusez directement vos transactions dans le réseau, sans passer par un intermédiaire. À condition de sécuriser correctement votre nœud (ce que nous aborderons plus loin) ou de respecter certains standards, aucune information n’est alors exposée : ni votre adresse IP, ni les détails de vos transactions ne transitent par une entité que vous ne contrôlez pas. Il s’agit donc d’un prérequis de base pour préserver votre confidentialité sur Bitcoin.

https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Transactions non censurables

Pour les mêmes raisons que précédemment évoquées, un logiciel de portefeuille reposant sur un nœud tiers s’expose à un risque de censure : l’opérateur du nœud distant peut refuser de relayer certaines transactions pour diverses raisons. Il peut les considérer comme suspectes ou contraires à sa politique. La transaction peut également être bloquée si elle ne respecte pas les règles de relais du nœud. Enfin, l’opérateur pourrait cibler spécifiquement votre adresse IP afin de bloquer la diffusion de vos transactions.

À l’inverse, en utilisant votre propre nœud, vous assurez vous-même la propagation de vos transactions au sein du réseau pair-à-pair. Vous gardez ainsi le contrôle total sur la diffusion de vos transactions, sans dépendance à un intermédiaire. Tant que la transaction est conforme aux règles de consensus et de relais des nœuds connectés au vôtre, elle sera diffusée sur le réseau puis, à condition d’inclure des frais suffisants, intégrée dans un bloc par un mineur. Disposer de votre propre nœud vous garantit ainsi la confirmation neutre et sans permission de vos transactions.

### Vérification indépendante des données

Sans nœud personnel, vous demeurez tributaire d’un tiers pour accéder aux informations : solde de vos adresses, état de confirmation d’une transaction, validité d’un bloc… Cela implique une confiance implicite dans l’exactitude et l’intégrité du nœud externe.

Faire fonctionner un nœud complet permet de vérifier soi-même l’ensemble des règles du protocole, pour chaque transaction et chaque bloc. Ainsi, le solde affiché par votre portefeuille n’est pas une donnée reçue d’un serveur distant, mais un résultat calculé localement à partir d’une copie complète de la blockchain, validée bloc après bloc. Cette démarche donne tout son sens à la maxime des bitcoiners :

> Don’t trust, verify.

### Mieux répartir la sécurité du système

Chaque nœud qui rejoint le réseau renforce la redondance et la résilience de Bitcoin. Il facilite la diffusion des informations et permet à de nouveaux pairs de se connecter. Sans les nœuds, le système serait tout simplement inopérant.

Comme nous l’avons vu, la sécurité de Bitcoin ne tient pas à la décentralisation, au minage ou à la cryptographie : elle repose, comme pour tout système, sur les individus. Plus précisément, elle dépend de la capacité des opérateurs de nœuds à résister à la coercition.

Ce qui distingue les systèmes décentralisés comme Bitcoin, c’est la répartition des risques entre tous ceux qui participent à leur fonctionnement. Faire tourner votre propre nœud Bitcoin, c’est accepter une part de ce risque en assurant la sécurité de votre instance ; ce faisant, vous allégez d’autant le poids du risque pour les autres opérateurs de nœuds.

Ce n’est donc pas un avantage personnel direct : faire tourner un nœud vous rend en partie responsable de la sécurité du réseau. Il s’agit avant tout d’un bénéfice collectif, car votre implication permet de diffuser le risque. Par ricochet, vous accroissez votre propre capacité à utiliser Bitcoin de manière fiable.

### Approfondir sa compréhension du système

Installer un nœud complet n’est pas une opération anodine. Cela implique d’installer un logiciel, d’en comprendre le fonctionnement de base, de surveiller la synchronisation, d’examiner les journaux en cas de problème, voire d’utiliser le terminal. Cette démarche vous amènera nécessairement à approfondir votre compréhension du protocole. Il s’agit là d’un avantage indirect, mais non négligeable.

Acquérir cette connaissance renforce votre confiance dans l’outil et peut réduire les risques d’erreurs ou d’exposition à des arnaques. Faire tourner son propre nœud, c'est aussi apprendre.

### Choisir les règles que l’on applique

Un aspect fondamental, souvent mal compris, réside dans le fait qu’exploiter un nœud permet de choisir localement les règles que l’on applique. On distingue alors deux grands types de règles :

- **Les règles de consensus** :

Il s’agit des règles essentielles du protocole Bitcoin, garantes de l’intégrité du système, qui fixent les critères de validation des transactions et des blocs. Toute transaction qui ne respecte pas ces règles de consensus ne pourra jamais être intégrée dans un bloc valide. Par exemple, une transaction comportant une signature invalide sur l’une de ses entrées sera systématiquement exclue.

Modifier ces règles équivaut à changer de protocole, donc de monnaie (hard fork). Toutefois, même sans chercher à les modifier, le simple fait d’appliquer strictement les règles existantes confère un certains pouvoir : si un bloc viole les règles, le nœud le rejette aussitôt.

- **Les règles de relais** :

Il s’agit des règles propres à chaque nœud Bitcoin, qui viennent s’ajouter aux règles de consensus afin de définir la structure des transactions non confirmées acceptées dans la mempool et relayées aux pairs. Chaque nœud configure et applique ces règles localement, ce qui explique qu’elles puissent différer d’un nœud à l’autre. Elles ne concernent que les transactions non confirmées : une transaction jugée "non standard" par un nœud ne sera acceptée que si elle figure déjà dans un bloc valide. Modifier ces règles n’exclut donc pas le nœud du système Bitcoin.

Par exemple, une transaction sans frais est, selon les règles de consensus, parfaitement valide, mais elle sera rejetée par défaut selon la politique de relais de Bitcoin Core, car le paramètre `minRelayTxFee` est fixé à `0.00001` (en BTC/kB). Néanmoins, il est possible, sur votre propre nœud, d’abaisser ce seuil pour relayer des transactions avec moins de frais, ou, à l’inverse, d’augmenter la limite, par exemple à 2 sats/vB, pour ne pas relayer les transactions à faibles frais.

Faire tourner votre propre nœud, c’est donc affirmer : *"je valide ce que je choisis de valider, selon les règles que j’ai moi-même adoptées"*. Vous devenez ainsi un acteur de la gouvernance du système, capable de rejeter une évolution qui vous semble inacceptable, ou d’approuver une mise à jour selon vos propres critères.

On peut donc rapidement essayer de comprendre à quel point vous avez du pouvoir sur les règles grâce à votre nœud. Et la mesure de ce pouvoir va dépendre du type de règle.

#### Pour les règles de relais

Pour ce qui concerne les règles de relais, l’essentiel réside dans le simple fait de posséder un nœud, quelle que soit son activité économique. Ici, l’enjeu est l’acceptation ou non de relayer certains types de transactions.

Prenons l’exemple où vous estimez que les transactions dont les frais sont inférieurs à 1 sat/vB devraient être acceptées sur Bitcoin : vous pouvez alors ajuster cette règle sur votre nœud pour qu’il diffuse ces transactions, ce qui facilite ainsi leur propagation sur le réseau jusqu’à ce qu’un mineur les inclue éventuellement dans un bloc valide. Il s’agit donc essentiellement d’un pouvoir sur la diffusion des transactions : chaque nœud détient un pouvoir décisionnel, car accepter de relayer un type de transaction revient à en favoriser l’acceptation sur le réseau Bitcoin. Par conséquent, si vous exploitez plusieurs nœuds, vous bénéficiez d’une influence accrue sur la politique de relais, chaque nœud ayant ses propres connexions et zones d’impact sur le réseau.

En effet, posséder un ou plusieurs nœuds configurés avec des règles de relais spécifiques revient à déterminer quelle part du réseau accepte de propager un type donné de transaction. La diffusion d’un message dans un graphe pair-à-pair, comme c’est le cas pour les transactions sur Bitcoin, suit la logique de la théorie de la percolation. Imaginez chaque nœud comme un site qui peut être actif (`p` = il relaie) ou inactif (`1 – p`). Dès lors que la proportion `p` franchit un seuil critique (`p_c`), une composante géante émerge : la transaction parvient à traverser le réseau et a toutes les chances d’atteindre un mineur. Dans un réseau comme Bitcoin où chaque nœud entretient en moyenne 8 connexions sortantes, le seuil `p_c` s’établit généralement autour de quelques pourcents seulement, d’autant plus bas si certains nœuds disposent de connexions très nombreuses.

Le rapport de force autour des règles de relais ne relève donc pas d’un principe "un nœud = un vote", mais bien de la capacité à faire franchir au réseau ce seuil de percolation : tant que `p` demeure inférieur à `p_c`, une transaction reste confinée à des poches isolées et n’atteint pas un mineur ; dès que ce seuil est dépassé, elle se propage presque instantanément à l’ensemble du réseau.

In fine, ce sont toujours les mineurs qui décident d’inclure ou non une transaction dans un bloc. Toutefois, les nœuds interviennent en amont, en influençant la diffusion des transactions : ils déterminent si les mineurs auront connaissance ou non d’une transaction donnée. Si une transaction n’est pas relayée jusqu’aux mineurs, il leur est évidemment impossible de l’intégrer à un bloc.

Ajouter quelques nœuds supplémentaires n’aura donc qu’un impact marginal si le réseau est déjà en phase percolante pour un type de transaction donné, mais cela peut s’avérer décisif à l’approche du seuil de percolation. Détenir ou influencer plusieurs nœuds, en particulier s’ils sont bien connectés, permet ainsi d’augmenter ou de réduire la valeur de `p` et, par conséquent, d’orienter de facto les règles de relais qui détermineront les transactions vues et éventuellement acceptées par les mineurs.

#### Pour les règles de consensus

En ce qui concerne l’influence de votre nœud sur les règles de consensus, c’est avant tout son poids économique qui sera déterminant. Ce concept est très important : l’utilité d’une monnaie, quelle qu’elle soit, découle directement de sa capacité à faciliter les échanges. En effet, si un objet n’est accepté par personne en échange de biens ou de services, il n’a théoriquement aucune utilité monétaire. Par exemple, si aucun commerçant n’accepte les cailloux comme moyen de paiement, ces derniers n’ont aucune utilité en tant que monnaie. L’utilité reste bien sûr une notion subjective à l’échelle individuelle, mais, sur un territoire donné, plus le nombre de commerçants acceptant un objet comme moyen d’échange est élevé, plus il est probable que cet objet ait une utilité monétaire pour les personnes vivant sur ce territoire.

Prenons l’exemple d’un village où de nombreux commerçants acceptent l’or en échange de biens : il y a alors de fortes chances que l’or possède une utilité monétaire pour les habitants du village. On comprend ainsi que l’utilité d’une monnaie dépend directement de la décision des commerçants de l’accepter ou non.

Cette notion est fondamentale pour appréhender les rapports de force à l’œuvre dans le système Bitcoin. Satoshi le précise : Bitcoin est un système de cash électronique, autrement dit il rend le service de proposer une forme de monnaie, le bitcoin (ou BTC). Lorsque les règles du protocole sont modifiées de façon non rétrocompatible (hard fork), cela revient à créer un nouveau système et donc une nouvelle monnaie. Le succès ou l’échec de ce fork dépend alors de la taille de son économie, qui est elle-même déterminée par le nombre de commerçants acceptant cette nouvelle forme de monnaie.

Prenons un exemple : supposons que Bitcoin subisse un hard fork. Il existerait alors deux formes de monnaies distinctes : BTC-1 (la version originelle, inchangée) et BTC-2 (la nouvelle monnaie avec des règles de consensus différentes). Si l’ensemble des commerçants qui acceptaient BTC-1 continuent à le faire, mais refusent le BTC-2, alors ce dernier n’aura, en théorie, qu’une utilité monétaire très limitée. En tant qu’utilisateur, je n’aurais aucun intérêt à conserver et utiliser du BTC-2, sachant qu’aucun commerçant n’en voudra en échange de biens ou de services. À l’inverse, si 50 % des commerçants choisissent d’accepter exclusivement le BTC-2 et les 50 % restants ne prennent que le BTC-1, alors l'utilité du BTC-1 aura, en théorie, diminué de moitié. J’emploie le terme "en théorie", car l’utilité demeure subjective au niveau individuel, et dépend d’une multitude de facteurs (territoire, habitudes de consommation, etc.) difficiles à appréhender au cas par cas.

Sur Bitcoin, le rôle de "commerçant", entendu comme toute entité disposant d’un certain poids économique, englobe bien sûr les commerces (boutiques physiques, sites de vente en ligne, prestataires de services…), mais aussi les plateformes d’échange, puisqu’elles acceptent le bitcoin en contrepartie d’autres monnaies, ainsi que les mineurs, car ils acceptent le bitcoin via les frais en échange du service d’inclure une transaction dans un bloc.

Concernant les règles de consensus, votre nœud vous permet donc d’orienter votre activité économique vers telle ou telle monnaie. Par exemple, si vous possédez 10 nœuds complets chez vous, mais n’exercez aucune activité économique significative, votre influence lors d’un fork sera quasi nulle. À l’inverse, un seul nœud utilisé pour gérer une chaîne de 50 magasins qui acceptent le bitcoin confère un poids économique important.

Ce n’est donc pas le nombre de nœuds qui importe, mais l’importance de l’activité économique qu’ils soutiennent. Par ailleurs, si votre activité économique dépend d’un nœud que vous ne contrôlez pas, c’est son propriétaire qui décidera de la monnaie que vous utilisez, tant que vous resterez connecté à ce nœud. C’est pourquoi faire tourner et utiliser son propre nœud revêt une importance particulière dans le contexte de la gouvernance du système :

> Pas ton nœud, pas tes règles.












## Les différents types de nœuds Bitcoin
<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>

Présentation des diverses catégories de nœuds : nœud complet, nœud élagué, nœud SPV... Comparaison des usages et implications techniques de chacun.

## Panorama des solutions logicielles
<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>

Vue d’ensemble des principales solutions logicielles disponibles pour faire tourner un nœud Bitcoin (Core, Knot, + node-in-box Umbrel, MyNode, Raspiblitz...), avec leurs avantages et inconvénients.

## Panorama des solutions matérielles
<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>

Présentation des options matérielles adaptées : ordinateurs classiques, mini-PC (type Raspberry Pi) barbonne (type ThinkCentre), besoins minimaux, SSD, RAM, processeur... Conseils pratiques selon les profils + achat de matériel d'occasion + recyclage de vieux PC.

















# Installer un nœud Bitcoin facilement
<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>


## Umbrel : bien plus qu'un nœud Bitcoin
<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>

Introduction à Umbrel comme solution accessible et tout-en-un pour les débutants. Umbrel home + UmbrelOS. Cas d'usages.

## Installation d’un nœud complet avec Umbrel
<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>

Maintenant que nous disposons de toutes les informations nécessaires, il est temps de passer à la pratique. Dans ce tutoriel, nous allons découvrir comment installer un nœud complet Bitcoin à l’aide d’UmbrelOS.

### Matériel nécessaire

Dans ce tutoriel, nous allons utiliser l’image UmbrelOS x86, plus précisément la version x86_64. Vous pourrez donc suivre ce guide quelle que soit la machine choisie, à condition qu’elle ne soit pas équipée d’un processeur à architecture ARM (Apple Silicon, Raspberry Pi, etc.). Cela signifie que tout ordinateur doté d’un processeur Intel ou AMD 64 bits conviendra, sous réserve de répondre aux exigences minimales selon l’usage que vous envisagez pour votre instance Umbrel (au moins dual-core, quad-core recommandé).

Si vous avez opté pour un Raspberry Pi 5 (option que je déconseille, comme évoqué dans la partie précédente), l’installation diffère légèrement. Vous pouvez alors suivre ce tutoriel dédié et revenir à mon cours une fois sur l’interface web `http://umbrel.local` :

https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Pour ma part, j’ai choisi de réaliser ce tutoriel sur un petit PC reconditionné que j'ai trouvé à un prix intéressant : un Lenovo ThinkCentre M900 Tiny équipé d’un processeur Intel Core i7 et de 16 Go de RAM. C’est une configuration très confortable pour exécuter Umbrel, surtout pour un nœud Bitcoin. Mais j'ai choisi cette configuration, car par la suite, je souhaite installer un nœud Lightning et diverses applications plus exigeantes. J’ai également ajouté un SSD de 2 To à mon ThinkCentre pour conserver l’intégralité de la blockchain tout en disposant d’une marge confortable. Avec cette configuration, le coût total s’élève à 270 € tout compris.

001

J’apprécie particulièrement la gamme ThinkCentre Tiny de Lenovo, car il s’agit de machines compactes, silencieuses et très robustes. Ces ordinateurs sont très répandus dans les entreprises, et abondent donc sur le marché de l’occasion, ce qui permet de trouver des configurations intéressantes entre 70 € et 200 €.

Si, comme moi, vous avez opté pour un PC dépourvu d’écran, **vous devrez connecter un écran et un clavier** uniquement le temps de l’installation. Par la suite, il sera possible d’y accéder à distance depuis un autre ordinateur sur le même réseau (ou via d’autres méthodes que nous aborderons dans les prochains chapitres). Prévoyez également un câble Ethernet RJ45 pour connecter votre machine au réseau local, ainsi qu’une clé USB d’au moins 4 Go pour y graver l’image d’installation.

Pour récapituler, voici les besoins en matériel :
- Ordinateur avec processeur x86_64 (minimum Dual-core, recommandé Quad-core) ;
- Mémoire RAM (4 Go minimum, 8 Go recommandé ou encore plus si usage étendu) ;
- Un SSD (recommandé + 2 To) ;
- Clé USB (+ 4 Go) pour l'installation de l’image UmbrelOS ;
- Écran et clavier (utiles uniquement pour l'installation initiale si le PC n'en est pas équipé) ;
- Câble Ethernet RJ45.

### Étape 1 - Monter l'ordinateur

Selon le matériel que vous avez choisi, la première étape consiste à assembler les différents composants de votre ordinateur. Par exemple, dans mon cas, le SSD installé d’origine n’offrait qu’une capacité de 256 Go : je vais donc le recycler pour un autre usage et le remplacer par un SSD de 2 To. Si vous souhaitez également remplacer les barrettes de RAM, c’est le moment de le faire.

### Étape 2 : Préparer une clé USB bootable

Avant d’installer UmbrelOS sur votre machine, il vous faudra créer une clé USB bootable contenant le système d’exploitation. Toutes les manipulations de cette étape 2 doivent être effectuées sur votre ordinateur personnel (et non directement sur l’ordinateur destiné à devenir votre nœud).

- Commencez par télécharger la version la plus récente d’UmbrelOS au format USB :

Rendez-vous sur [le site officiel d’Umbrel pour télécharger l’image ISO](https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) destinée à l’installation via une clé USB. Assurez-vous de choisir la version compatible avec l’architecture x86_64 (fichier intitulé `umbrelos-amd64-usb-installer.iso`). Le téléchargement peut être relativement long, puisque l’image est volumineuse.

002

- Installez Balena Etcher :

Pour créer la clé USB bootable, vous allez utiliser un outil simple et multiplateforme appelé [Balena Etcher](https://www.balena.io/etcher/). Téléchargez-le et installez-le sur votre ordinateur.

003

- Insérez une clé USB vierge d’au moins 4 Go :

Branchez une clé USB dans votre ordinateur (celui sur lequel vous venez de télécharger l'image d'UmbrelOS et Balena Etcher). **Attention : toutes les données présentes sur la clé seront effacées**. Vérifiez donc qu’elle ne contient aucun fichier important.

- Gravez l’image ISO sur la clé USB avec Balena Etcher :

Lancez Balena Etcher et sélectionnez le fichier ISO `umbrelos-amd64-usb-installer.iso` que vous venez de télécharger en cliquant sur le bouton "*Flash from file*". Puis, sélectionnez la clé USB comme périphérique cible et cliquez sur "*Flash!*" pour lancer l’écriture.

004

Une fois l’opération terminée, vous disposerez d’une clé USB bootable contenant UmbrelOS, prête à être utilisée pour démarrer et installer Umbrel sur votre machine.

005

### Étape 3 : Démarrer l'ordinateur depuis la clé USB

Maintenant que votre clé USB bootable contenant UmbrelOS est prête, vous allez pouvoir démarrer votre ordinateur dessus pour lancer l’installation du système. Débranchez la clé USB de votre ordinateur principal et insérez-la dans l’appareil sur lequel vous souhaitez installer Umbrel et votre nœud Bitcoin.

Comme expliqué au début de ce chapitre, pour effectuer l’installation, vous aurez besoin d’un périphérique d'affichage et d’un périphérique d’entrée. Branchez un écran via HDMI (ou autre port en fonction de votre PC) et connectez un clavier en USB à votre machine. Ces périphériques ne sont requis que pour l’installation ; vous n’en aurez plus besoin par la suite, puisque l’accès à Umbrel se fera à distance depuis un autre ordinateur. Branchez donc ces deux périphériques à votre PC.

**Conseil :** Si vous ne disposez pas d'écran périphérique chez vous, vous pouvez utiliser votre téléviseur. Avec son entrée HDMI (ou autre), il peut parfaitement faire office d’écran temporaire le temps d'installer le système d’exploitation.

Umbrel nécessite évidemment une connexion internet. Branchez donc le câble Ethernet RJ45 entre votre appareil et votre routeur.

006

Allumez votre machine. Dans la majorité des cas, celle-ci devrait automatiquement détecter la clé USB et démarrer dessus. Vous verrez alors l’interface d’installation d’UmbrelOS apparaître à l’écran.

Si l’appareil démarre sur un autre système ou affiche un message d’erreur, cela signifie probablement qu’il ne boote pas automatiquement depuis la clé USB. Dans ce cas, redémarrez-le et entrez dans les paramètres du BIOS/UEFI (généralement en appuyant sur `DEL`, `F2`, `F12` ou `ESC` selon le fabricant de l'ordinateur), puis modifiez l’ordre de démarrage pour donner la priorité à la clé USB. Redémarrez ensuite l’appareil pour lancer UmbrelOS.

### Étape 4 : Installer UmbrelOS sur l'ordinateur

Une fois que l’appareil a démarré depuis la clé USB, vous allez être accueilli par l’interface d’installation d’UmbrelOS. Cette étape consiste à installer le système directement sur le disque interne de votre machine.

L’écran qui s’affiche liste tous les périphériques de stockage internes détectés par l’ordinateur. Chaque disque est accompagné d’un numéro, d’un nom et d’une capacité de stockage. Repérez le disque sur lequel vous souhaitez installer Umbrel. **Attention : tous les fichiers présents sur ce disque seront définitivement effacés.**

007

Une fois le bon disque identifié (généralement celui offrant la plus grande capacité, afin d’héberger la blockchain), notez le numéro qui lui est attribué. Par exemple, si le disque retenu apparaît sous le numéro `2`, il vous suffit de saisir `2`, puis d’appuyer sur la touche `Enter` du clavier.

008

Le programme va formater le disque sélectionné, y installer UmbrelOS et configurer automatiquement le système. Cette étape peut durer quelques minutes. Laissez le processus se dérouler sans interruption.

009

Lorsque l’installation est terminée, un message vous invite à éteindre l’appareil. Appuyez sur n’importe quelle touche pour arrêter l’ordinateur.

010

Vous pouvez à présent retirer la clé USB, le clavier et l’écran ; ils ne sont plus nécessaires pour l’utilisation de votre Umbrel. Votre nœud ne doit donc rester connecté qu’à l’alimentation électrique et au câble Ethernet RJ45.

011

Avant de redémarrer l’appareil, vérifiez les deux points suivants :

- **La clé USB est bien débranchée** : si elle reste connectée, le système pourrait redémarrer dessus au lieu du disque interne ;
- **Le câble Ethernet est branché** : l’appareil doit être connecté à votre routeur pour fonctionner.

Appuyez sur le bouton d’alimentation. Le système démarre automatiquement depuis le disque interne où UmbrelOS a été installé. Le premier démarrage peut prendre environ **5 minutes**. Pendant ce temps, Umbrel initialise ses services et son interface.

Depuis un autre ordinateur (votre PC du quotidien) connecté au **même réseau local**, ouvrez un navigateur web (firefox, chrome...) et rendez-vous sur :

```
http://umbrel.local
```

Cette adresse permet d’accéder à l’interface graphique d’Umbrel à distance pour commencer la configuration.

Si l’adresse `http://umbrel.local` ne fonctionne pas sur votre navigateur après avoir attendu au moins 5 minutes, essayez simplement :

```
http://umbrel
```

Si cela ne fonctionne toujours pas, saisissez directement l’adresse IP locale de votre Umbrel dans le navigateur. Par exemple : (remplacez `42` par le numéro de votre machine hébergeant Umbrel sur le réseau local) :

```
http://192.168.1.42
```

Pour identifier l’adresse IP de votre Umbrel, il y a plusieurs méthodes, de la plus simple à la plus avancée :

- Accédez à l’interface d’administration de votre routeur et recherchez l’adresse IP de l’appareil Umbrel sur le réseau local.

- Utilisez un logiciel de scan réseau tel qu’Angry IP Scanner pour détecter les appareils connectés et repérer l’adresse IP de votre Umbrel.

012

https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

- En dernier recours, rebranchez un écran et un clavier sur l’appareil, connectez-vous (identifiant par défaut : `umbrel`, mot de passe : `umbrel`), puis tapez la commande suivante :

```
hostname -I
```

Vous êtes maintenant prêt à utiliser Umbrel !

### Étape 5 : prise en main d'Umbrel

Pour commencer la configuration de votre Umbrel, cliquez sur le bouton "*Start*".

013

#### Créer un compte

Choisissez un pseudonyme ou indiquez votre nom, puis définissez un mot de passe fort. Soyez vigilant : ce mot de passe constitue la seule barrière protégeant l’accès à votre Umbrel depuis votre réseau (et donc, potentiellement, à vos bitcoins si vous faites tourner un nœud Lightning sur Umbrel). Il protège également l’accès à distance via Tor ou VPN, si ces services sont activés.

Sélectionnez donc un mot de passe fort, et, surtout, veillez à en conserver une ou plusieurs sauvegardes (gestionnaire de mots de passe recommandé).

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Un fois le mot de passe renseigné, cliquez sur le bouton "*Create*".

014

La configuration de votre Umbrel est terminée.

015

#### Découverte de l'interface

L’interface d’Umbrel est assez intuitive :

- Sur la page d’accueil, vous visualisez vos applications installées ainsi que vos widgets ;

016

- L’"*App Store*" permet d’installer de nouvelles applications ;

017

- Le menu "*Files*" centralise tous les documents stockés sur votre Umbrel ;

018

- Le menu "*Settings*" vous permet de modifier les paramètres de votre Umbrel et d’accéder à ses informations, notamment :
    - Mettre à jour, redémarrer ou arrêter votre machine ;
    - Consulter l’espace de stockage disponible, l’utilisation de la RAM ou encore la température du processeur ;
    - Changer le fond d’écran ;
    - Gérer l’accès à distance via Tor, activer le Wi-Fi ou le 2FA.

019

#### Paramètres de sécurité et de connexion

Avant toute chose, je vous recommande vivement d’activer le 2FA. Cette mesure ajoute une couche supplémentaire de sécurité à votre mot de passe. Elle s’avère quasi indispensable si vous envisagez d’utiliser votre Umbrel pour stocker des fichiers personnels, exécuter un nœud Lightning ou toute autre activité sensible.

https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Pour cela, cliquez sur la case correspondante dans les paramètres.

020

Scannez ensuite le QR code affiché à l’aide de votre application d’authentification. Saisissez enfin le code dynamique à 6 chiffres dans le champs prévu à cet effet sur votre Umbrel.

Désormais, chaque nouvelle connexion à votre Umbrel nécessitera à la fois le mot de passe et le code à 6 chiffres généré par votre application 2FA.

021

En ce qui concerne l’accès à distance via Tor, si vous n’en avez pas l’utilité, je vous recommande de laisser cette option désactivée afin de limiter la surface d’attaque de votre Umbrel. Par défaut, votre nœud n’est accessible que depuis une machine connectée au même réseau local. Activer l’accès via Tor vous permettra néanmoins de gérer votre Umbrel en déplacement.

Si vous activez cette fonctionnalité, il devient théoriquement possible pour toute machine dans le monde de tenter une connexion à votre nœud, à condition de connaître l’adresse Tor. Toutefois, la protection reste assurée par votre mot de passe et votre 2FA.

En cas d’activation de cette option, veillez à avoir le 2FA activé, un mot de passe fort, et à ne jamais divulguer l’adresse Tor de connexion.

Il vous suffira alors de saisir cette adresse Tor dans le navigateur Tor pour accéder à l’interface d’Umbrel depuis n’importe quel réseau.

026

Enfin, sur cette page de paramètres, vous avez également la possibilité d’activer la connexion Wi-Fi. Si votre machine hébergeant Umbrel dispose d’une carte réseau Wi-Fi ou d’un dongle Wi-Fi, cela permet d’accéder à Internet sans utiliser le câble RJ45. Toutefois, selon votre configuration, cette solution risque de ralentir la connexion, ce qui peut affecter la synchronisation initiale (IBD) et l’utilisation future du nœud (par exemple pour des transactions Lightning). À titre personnel, je ne recommande pas cette option, car un nœud n’a pas vocation à être utilisé en mobilité : on y accède toujours à distance, donc autant le laisser branché.

### Étape 6 : installer un nœud Bitcoin sur Umbrel

Maintenant qu’UmbrelOS est correctement installé et configuré sur votre machine, vous pouvez procéder à l’installation de votre nœud Bitcoin. Pour cela, rien de plus simple : rendez-vous dans l’App Store, ouvrez la catégorie "*Bitcoin*", puis sélectionnez l’application "*Bitcoin Node*" (il s’agit en réalité de Bitcoin Core).

022

Cliquez ensuite sur le bouton "*Install*".

023

Une fois l’installation achevée, votre nœud Bitcoin lancera son IBD (*Initial Block Download*) : il va télécharger et valider l’ensemble des transactions et des blocs depuis la création de Bitcoin en 2009.

024

Cette étape est particulièrement longue : sa durée dépend de plusieurs facteurs, notamment la quantité de RAM allouée au cache du nœud, la rapidité du disque, la vitesse de la connexion Internet et la puissance du processeur. La fourchette de durée est donc très large en fonction des configurations. Avec un PC très performant (SSD NVMe, +32 Go de RAM, processeur puissant et bonne connexion internet) l’IBD peut s’achever en une dizaine d’heures. À l’inverse, un vieux processeur, peu de RAM ou, encore pire, un disque dur mécanique (fortement déconseillé) peuvent allonger cette opération à plusieurs semaines.

Avec un PC de configuration normale (processeur correct, 8 à 16 Go de RAM, SSD), prévoyez environ 2 à 7 jours.

Pour accélérer légèrement l’IBD, vous pouvez augmenter la RAM allouée au cache du nœud (utilisé notamment pour l’UTXO set, mais nous y reviendrons plus loin dans la formation), via le paramètre `dbcache`. Sur Umbrel, cette modification s’effectue dans les paramètres de votre nœud, dans l'onglet "*Optimization*".

025

Par défaut, la valeur du paramètre `dbcache` dans Bitcoin Core est fixée à 450 MiB, soit environ 472 Mo. En augmentant cette valeur, vous pouvez accélérer légèrement l’IBD. Toutefois, je ne recommande pas forcément de pousser ce paramètre à des niveaux trop élevés : même en le réglant à 4 GiB, la synchronisation ne sera qu’environ 10 % plus rapide, et cela peut vous faire perdre du temps en cas d’interruption durant l’IBD.

Veillez aussi à ne pas allouer une valeur trop importante pour votre machine : si la RAM disponible pour UmbrelOS vient à manquer, votre nœud risque de s’arrêter brutalement, ce qui interromprait l’IBD et nécessiterait de la relancer manuellement, occasionnant une perte de temps considérable.

Pour approfondir l’impact du paramètre `dbcache` sur la synchronisation initiale, je vous recommande cette analyse de Jameson Lopp : [*Effects of DBcache Size on Bitcoin Node Sync Speed*](https://blog.lopp.net/effects-dbcache-size-bitcoin-node-sync-speed/) 

Une fois l’IBD de votre nœud terminée (synchronisation à 100 %), vous disposez désormais d’un nœud complet Bitcoin pleinement opérationnel. Félicitations, vous faites désormais partie intégrante du réseau Bitcoin !

027

Dans la prochaine partie, nous aborderons l’utilisation concrète de votre nouveau nœud : comment y connecter votre portefeuille et quelles applications installer pour devenir un bitcoiner souverain ?



# Connecter son portefeuille à son nœud
<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>

## Les indexeurs : rôle, fonctionnement et solutions
<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>

Si vous vous êtes déjà renseigné sur les nœuds Bitcoin avant de suivre cette formation, il est possible que vous ayez rencontré le terme "indexeur". Il s’agit d’outils comme Electrs ou Fulcrum, que l’on peut ajouter à un nœud Bitcoin Core. Mais quel est exactement le rôle de ces logiciels ? Comment fonctionnent-ils concrètement ? Et devez-vous en installer un sur votre nouveau nœud Bitcoin ? C’est ce que nous allons explorer dans ce chapitre.

### Qu'est-ce qu'un indexeur ?

De façon générale en informatique, un indexeur est un programme qui parcourt un ensemble de données brutes, en extrait des clés pertinentes (mots, identifiants, adresses…) et construit un fichier auxiliaire, appelé "index", où chaque clé renvoie à l’emplacement exact de la donnée dans le corpus. Cette phase de prétraitement mobilise du temps CPU et requiert un peu d’espace disque, mais elle évite par la suite de devoir parcourir tout le corpus à chaque requête sur la base de données : il suffit d’interroger l’index pour obtenir une réponse quasi immédiate.

Pour vulgariser, c’est le même principe qu’un index dans un livre : si vous cherchez une information précise, plutôt que de relire tout le livre, vous consultez l’index afin de trouver directement la page où figure l’information recherchée.

Dans un nœud Bitcoin comme Bitcoin Core, les données de la blockchain sont stockées sous une forme brute et chronologique. Chaque bloc contient des transactions, qui elles-mêmes contiennent des entrées et des sorties, sans aucun classement particulier par adresse, identifiant ou portefeuille. Cette organisation linéaire est optimisée pour la validation des blocs, mais très peu adaptée à des recherches ciblées. Par exemple, si vous souhaitez retrouver toutes les transactions liées à une adresse spécifique dans un nœud non indexé, vous devriez parcourir manuellement l’ensemble de la blockchain, bloc par bloc, transaction par transaction. C’est précisément là qu’intervient l'indexeur sur votre nœud Bitcoin.

Un indexeur est un logiciel spécialisé qui va analyser cette masse de données brutes (la blockchain, la mempool, l'UTXO set…) et en extraire des clés : identifiants de transaction, adresses, hauteurs de blocs... À partir de ces clés, il construit son index qui associe chaque clé à l’endroit exact où se trouve l’information dans le stockage du nœud.

L’indexation permet ainsi d’effectuer des recherches d’informations sur votre nœud de manière rapide, ciblée et efficace. Par exemple, lorsque vous connectez un portefeuille comme Sparrow à votre nœud, il peut afficher presque instantanément le solde d’une adresse. Concrètement, il interroge l’indexeur avec une requête du type : "_Quels UTXOs sont associés à ce script-hash ?_" L’indexeur répond presque aussitôt, sans avoir à relire l’ensemble de la blockchain, car cette donnée est déjà répertoriée dans sa base.

### Est-ce que Bitcoin Core dispose d'un indexeur ?

Sans ajout de logiciel supplémentaire, Bitcoin Core ne dispose pas, à proprement parler, d’un indexeur complet d'adresses comparable à ceux que l’on retrouve dans des logiciels comme Electrs ou Fulcrum. Néanmoins, il intègre plusieurs mécanismes d’indexation internes, ainsi que des options facultatives permettant d’étendre ses capacités d’interrogation. Pour bien comprendre la situation, il  faut faire un détour par l’histoire du projet.

Jusqu’à la version 0.8.0 de Bitcoin Core, la validation des transactions reposait sur un index global des transactions : le fameux `txindex`. Ce dernier référençait toutes les transactions de la blockchain ainsi que leurs sorties. Lorsqu’un nœud recevait une nouvelle transaction, il consultait cet index pour vérifier que les sorties consommées (en inputs) existaient bien, et qu’elles n’avaient pas déjà été dépensées. `txindex` était donc à l’époque indispensable à la validation des transactions.

Mais cette approche présentait des limites : lenteur, coût en terme de stockage, redondance d’informations. Pour y remédier, la version 0.8.0 introduit une refonte du modèle de validation appelée ***Ultraprune***. Ce changement inaugure notamment l’architecture actuelle : au lieu de tout stocker sous forme d'index de transactions, Bitcoin Core maintient une simple base de données dédiée aux seuls UTXOs, appelée `chainstate` (c'est que l'on appelle dans le langage courant "UTXO set"), et actualise au fur et à mesure sa liste en fonction des output consommés et créés.

Cette méthode est bien plus rapide, et elle permet de ne stocker que l’état actuel du registre, ce qui rend l'indexeur `txindex` inutile. Cependant, au lieu de supprimer le code de `txindex`, les développeurs ont choisi de conserver cette fonctionnalité derrière un simple paramètre (`txindex=1`). En activant cette option sur votre nœud, vous pouvez donc interroger n’importe quelle transaction à partir de son `txid`.

Contrairement à ce que l’on pourrait penser, Bitcoin Core ne propose pas d’indexation par adresse comme pourraient le faire Electrs ou Fulcrum. Plusieurs raisons expliquent ce choix :

- Le rôle de Bitcoin Core n’est pas de devenir un explorateur de blocs complet, ni de fournir une API taillée pour chaque usage. Intégrer un index par adresse impliquerait un engagement de maintenance à long terme, qui va au-delà du périmètre initial du logiciel ;

- La plupart des cas d’usage peuvent déjà être couverts autrement. Par exemple, pour estimer le solde d’une adresse, il est possible d’utiliser la commande `scantxoutset`, qui interroge directement l'UTXO set sans nécessiter d’index complet.

- Chaque logiciel a des exigences spécifiques sur le format ou le type de données à indexer (adresse, script-hash, tag propriétaire…). Il est plus souple et plus logique de laisser ces logiciels construire leurs propres index sur mesure plutôt que de figer une solution générique dans Bitcoin Core.

Bitcoin Core dispose bien en option d’un indexeur de transactions (`txindex`), vestige de son fonctionnement historique, mais il ne fournit aucun index par adresse, ni d’interface directe pour faire des recherches complexes. Il peut donc être utile dans certains cas d'ajouter un logiciel indexeur externe.

### Faut-il ajouter un indexeur d'adresses sur son nœud ?

Ajouter un indexeur d’adresses comme Electrs ou Fulcrum n’est en rien obligatoire ; tout dépend de vos besoins.

Si vous souhaitez simplement connecter un portefeuille comme Sparrow à votre nœud pour consulter le solde et diffuser des transactions, cela est tout à fait possible directement via l’interface RPC de Bitcoin Core, en local ou à distance via Tor.

En revanche, pour utiliser des logiciels plus avancés, comme faire tourner un explorateur de bloc mempool.space en local, l’installation d’un indexeur d’adresses devient indispensable.

L’indexeur nécessite un certain temps de synchronisation (inférieur à celui de l’IBD) et occupera un espace supplémentaire sur votre disque. Si votre SSD dispose encore d’assez d’espace libre une fois la blockchain téléchargée, vous pouvez sans problème ajouter un indexeur.

### Quel indexeur choisir ?

Deux logiciels sont couramment utilisés pour construire ce type d’index d’adresses et le rendre accessible : **Electrs** et **Fulcrum**. Ces outils indexent la blockchain selon les script-hash (adresses), puis proposent une interface standardisée (le protocole Electrum), à laquelle se connectent de nombreux portefeuilles tels qu’Electrum Wallet, Sparrow ou encore Phoenix.

Pour faire simple, Electrs est assez comapct : il indexe plus rapidement la blockchain et occupe moins d’espace disque, mais il est légèrement moins performant que Fulcrum lors des requêtes. À l’inverse, Fulcrum consomme davantage d’espace disque et requiert plus de temps pour l’indexation, mais il offre des performances supérieures lors des requêtes.

Pour un usage individuel, je recommande plutôt Electrs : il consomme moins d’espace, il est bien maintenu et, malgré une légère lenteur sur certaines requêtes par rapport à Fulcrum, il reste largement suffisant pour un usage courant. Si vous disposez de temps et d’espace disque, vous pouvez également tester Fulcrum, qui sera bien plus performant notamment sur les wallets avec de nombreuses adresses à vérifier.

Concrètement, en termes de besoins de stockage, en août 2025, Electrs requiert environ 56 Go, contre environ 178 Go pour Fulcrum. Le choix de votre indexeur dépend donc aussi de votre capacité de stockage :
- Si votre espace disque est très limité, contentez-vous de Bitcoin Core sans indexeur d’adresses externe ;
- Si vous souhaitez utiliser un indexeur, mais restez contraint par la capacité, optez pour Electrs ;
- Si vous disposez d’un espace disque confortable, Fulcrum peut s’avérer intéressant.

Pour la suite de cette formation BTC 202, j’utiliserai Electrs, mais vous pouvez sans difficulté suivre avec Fulcrum : la procédure d’installation est identique, tout comme l’interface de connexion aux logiciels de portefeuille, puisque les deux exposent un serveur Electrum.

### Comment installer un indexeur sur Umbrel ?

Pour installer Electrs (ou Fulcrum) sur votre Umbrel, la procédure est très simple : rendez-vous sur l’App Store, recherchez l’application concernée (elle figure dans l’onglet Bitcoin), puis cliquez sur le bouton "*Install*".

028

Une fois l’installation terminée, Electrs procédera à une phase de synchronisation (indexation), qui peut durer plusieurs heures.

029

Une fois la synchronisation terminée, vous pourrez connecter vos logiciels de portefeuille à votre serveur Electrum hébergé sur Umbrel.






























## Comment connecter son portefeuille à son nœud Bitcoin ?
<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>

Maintenant que vous disposez d’un nœud complet Bitcoin, il est temps de le mettre à profit ! Dans le prochain chapitre, nous aborderons d’autres usages possibles sur votre instance Umbrel, mais commençons par l’essentiel : connecter votre logiciel de portefeuille afin d'utiliser les informations de votre propre blockchain et de diffuser vos transactions via votre propre nœud.

Comme mentionné précédemment, il existe principalement deux interfaces de connexion :
- La connexion directe à Bitcoin Core via RPC ;
- Ou bien la connexion à un serveur Electrum (Electrs ou Fulcrum).

Dans ce tutoriel, nous nous concentrerons sur la connexion à votre nœud via Tor, car c'est une solution à la fois simple et sécurisée pour les débutants. Je vous déconseille fortement d’exposer le port RPC de votre nœud en clair : une mauvaise configuration représente un risque majeur pour la sécurité et la confidentialité de vos données. Le principal inconvénient des communications via Tor reste leur lenteur. Nous verrons donc, dans le chapitre suivant, une alternative rapide et sécurisée à Tor pour accéder à distance à votre nœud : le VPN.

Nous prendrons l’exemple de Sparrow dans ce chapitre, mais la procédure est identique pour tous les autres logiciels de gestion de portefeuille acceptant les connexions aux serveurs Electrum. Il vous suffira de repérer, dans les paramètres de votre application, l’emplacement du réglage correspondant (généralement dans "*Server*", "*Network*", "*Node*"...).

Sur Sparrow, ouvrez l’onglet "*File*" puis rendez-vous dans le menu "Settings".

030

Cliquez ensuite sur "*Server*" pour accéder aux paramètres de connexion.

031

Vous découvrirez alors trois options pour relier votre logiciel à un nœud Bitcoin :
- *Public Server* (jaune) : par défaut, si vous ne possédez pas de nœud Bitcoin, cette option vous connecte à un nœud public ne vous appartenant pas (généralement celui d'une entreprise). Cette option n’est pas pertinente ici, puisque vous avez votre propre nœud sur Umbrel ;
- *Bitcoin Core* (vert) : cette option correspond à la connexion via l’interface RPC, c’est-à-dire directement à Bitcoin Core ;
- *Private Electrum* (bleu) : cette option permet de se connecter via l’interface Electrum Server de votre indexeur (Electrs ou Fulcrum).

### Connexion à Bitcoin Core RPC

Si votre nœud Umbrel ne dispose pas d’un indexeur, cette option est celle que vous devez sélectionner. Sur Sparrow, cliquez sur "*Bitcoin Core*".

032

Vous devrez alors saisir plusieurs informations afin d’établir la connexion à votre nœud. Toutes ces données sont accessibles depuis l’application "*Bitcoin Node*" sur Umbrel, en cliquant sur le bouton "*Connect*" situé en haut à droite de l’interface.

033

L’onglet "*RPC Details*" présente l’ensemble des informations nécessaires à la connexion. Choisissez la connexion via l'adresse Tor (en `.onion`).

034

Renseignez ces éléments dans les champs correspondants sur Sparrow Wallet, puis cliquez sur le bouton "*Test Connection*".

035

Si la connexion s’établit correctement, une coche verte accompagnée d’un message de confirmation apparaîtra.

036

La coche située en bas à droite de l’interface Sparrow Wallet sera désormais verte (indiquant une connexion directe à Bitcoin Core).

**Remarque :** Pour que la connexion aboutisse, votre nœud doit impérativement être synchronisé à 100 %. Dans le cas contraire, patientez jusqu’à la fin de l’IBD.

### Connexion à Electrs

Si votre nœud dispose d'un indexeur, il est préférable de vous y connecter plutôt que d’utiliser directement Bitcoin Core, car vos requêtes seront traitées plus rapidement.

Sur Sparrow, rendez-vous dans l’onglet "*Private Electrum*".

037

Vous devrez alors saisir plusieurs informations afin d’établir la connexion avec votre indexeur. Vous trouverez ces données dans l’application "*Electrs*" (ou, le cas échéant, "*Fulcrum*") sur Umbrel.

Sélectionnez l’onglet "*Tor*" pour obtenir l’adresse de connexion en `.onion`. Si vous souhaitez connecter un logiciel de portefeuille sur mobile, vous pouvez également scanner directement le QR code.

038

Renseignez simplement l’adresse Tor de votre serveur Electrum dans le champ "*URL*", puis cliquez sur le bouton "*Test Connection*".

039

Si la connexion s’établit correctement, une coche et un message de confirmation s’afficheront.

040

La coche située en bas à droite de l’interface Sparrow Wallet deviendra bleue (couleur associée à la connexion à un serveur Electrum).

**Remarque :** Pour que la connexion fonctionne, votre indexeur doit être synchronisé à 100 %. Si ce n’est pas le cas, attendez la fin du processus d’indexation.

Vous savez désormais comment relier votre logiciel de gestion de portefeuille à votre nœud Bitcoin ! Dans le chapitre suivant, je vous présenterai plusieurs applications complémentaires disponibles sur Umbrel, que j’affectionne particulièrement et qui vous permettront d'améliorer votre usage de Bitcoin au quotidien grâce à votre nœud.


## Tour d’horizon des applications disponibles
<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>

Umbrel propose un vaste magasin d’applications. Comme vous pourrez le constater, on y trouve de nombreux outils liés à Bitcoin, mais également une grande variété d’applications dans des domaines très différents : solutions d’auto-hébergement de services et de fichiers, applications de productivité, outils financiers plus généraux, gestion de médias, sécurité et administration réseau, développement, intelligence artificielle, réseaux sociaux ou encore domotique.

Dans le cadre de cette formation BTC 202, nous nous concentrerons exclusivement sur les applications en rapport avec Bitcoin. Toutefois, n’hésitez pas à explorer le reste du catalogue pour y dénicher des outils pouvant vous être utiles.

Évidemment, il serait impossible de vous présenter ici toutes les applications Bitcoin tant elles sont nombreuses. Je vous propose donc, dans ce chapitre, de découvrir celles que je considère comme essentielles pour faciliter et enrichir votre utilisation quotidienne de Bitcoin.

### Mempool.space

Dans l’usage quotidien de Bitcoin, s’il est un outil véritablement incontournable, c’est bien l’explorateur de blocs. Qu’il soit accessible en ligne ou installé en local, il permet de transformer les données brutes de la blockchain en un format structuré, clair et facilement lisible. Il intègre également un moteur de recherche pour retrouver rapidement un bloc, une transaction ou une adresse spécifique.

Concrètement, l’explorateur vous permet d’estimer les frais nécessaires pour que votre transaction soit incluse dans un bloc, puis de suivre son évolution : savoir si elle est susceptible d’être intégrée prochainement en fonction du marché des frais, et enfin confirmer qu’elle a bien été incluse dans un bloc. Il offre aussi la possibilité d’analyser vos transactions passées et d’en consulter l’historique. En bref, c’est le véritable couteau suisse du bitcoiner.

Comme indiqué précédemment, un explorateur peut être hébergé en ligne sur un site web ou exécuté localement sur votre machine. L’inconvénient majeur d’un service en ligne est qu’il peut compromettre votre confidentialité. Sans VPN ni Tor, le serveur hébergeant l’explorateur peut relier votre adresse IP aux transactions que vous consultez, ce qui peut constituer un point d’entrée idéal pour une analyse de chaîne.

https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

De plus, votre fournisseur d’accès à Internet (ISP) peut savoir que vous consultez telle ou telle transaction via le site de l’explorateur de blocs. Cela soulève également une question de confiance : vous devez vous en remettre au service en ligne pour obtenir des informations exactes sur vos transactions, sans pouvoir en vérifier la véracité par vous-même.

C’est pourquoi il est toujours préférable d’utiliser son propre explorateur de blocs en local. De cette manière, aucune donnée liée à votre activité de recherche ne fuitera, puisque toutes les requêtes sont traitées directement sur une machine que vous contrôlez, sans passage par Internet. De plus, un explorateur local s’appuie sur les données de votre propre nœud Bitcoin, que vous avez validées vous-même, selon vos propres règles, et en lesquelles vous pouvez avoir confiance.

Sur Umbrel, plusieurs explorateurs de blocs sont disponibles :
- Mempool.space  
- Bitfeed  
- BTC RPC Explorer

Pour ma part, j’apprécie particulièrement Mempool.space, que j’ai donc installé sur mon nœud. Attention toutefois : pour utiliser la plupart des explorateurs de blocs sur Umbrel, un indexeur d’adresses est nécessaire. Vous devez donc disposer de l’application Bitcoin Node (ou Bitcoin Knots) avec une blockchain synchronisée à 100 %, ainsi que d’un indexeur tel qu’Electrs ou Fulcrum, également synchronisé à 100 %.

Une fois l’application installée, il vous suffit de l’ouvrir pour accéder à votre propre explorateur.

041

Pour approfondir l’utilisation de l'explorateur Mempool.space, je vous recommande de consulter ce tutoriel complet :

https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Nœud Lightning

Maintenant que vous possédez votre propre nœud Bitcoin, vous pouvez également mettre en place votre propre nœud Lightning afin d’effectuer des transactions off-chain, sans dépendre d’une infrastructure tierce.

Umbrel propose de nombreuses applications pour vous aider à faire fonctionner votre nœud Lightning. Vous pouvez déjà choisir entre deux principales implémentations :
- LND, via l’application *Lightning Node* ;
- Core Lightning.

https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Vous pouvez ensuite administrer votre nœud depuis l’interface principale, ou bien, pour bénéficier de davantage de fonctionnalités et d’options avancées, installer *Ride The Lightning* ou *ThunderHub*. Ces outils vous offriront une interface web de gestion bien plus complète pour votre nœud.

https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Enfin, je vous recommande l’application *Lightning Network+*, qui permet de trouver des pairs avec qui ouvrir des canaux, afin de disposer à la fois de liquidités sortantes et entrantes.

Grâce à Umbrel, la gestion d’un nœud Lightning personnel est grandement simplifiée, mais elle demeure malgré tout relativement complexe. C’est pourquoi nous aborderons ce sujet en profondeur dans un prochain cours entièrement consacré à cet usage.

### Tailscale

Une autre application que j'apprécie particulièrement sur Umbrel est Tailscale. C'est une application de VPN conçue pour simplifier la création de réseaux sécurisés entre plusieurs appareils, où qu’ils se trouvent dans le monde. Contrairement aux VPN traditionnels, qui reposent sur des serveurs centralisés, Tailscale s’appuie sur le protocole WireGuard pour établir des connexions chiffrées de bout en bout entre vos différentes machines. Cela vous permet de déployer un VPN fonctionnel en quelques minutes, sans manipulations réseau compliquées.

Sur Umbrel, l’installation de Tailscale permet de connecter votre nœud Bitcoin à votre propre réseau privé virtuel. Une fois configuré, votre nœud obtient une adresse IP privée Tailscale, accessible uniquement depuis vos autres appareils reliés au même réseau Tailscale (ordinateur, smartphone, tablette...). Cette connexion est chiffrée de bout en bout et ne transite pas par le réseau public non protégé, ce qui renforce considérablement la sécurité par rapport à une connexion en clair.

Concrètement, pour l'utilisation de votre Umbrel, Tailscale vous apporte plusieurs avantages :

- Vous pouvez administrer l’interface Umbrel ou accéder aux applications liées à votre nœud (comme Mempool, Ride The Lightning, ThunderHub...) depuis n’importe où, comme si vous étiez sur le même réseau local, sans exposer de ports sur Internet et sans passer par Tor qui est très lent ;

- Vous pouvez vous connecter à votre serveur Electrum (Electrs ou Fulcrum) ou directement à Bitcoin Core via votre VPN, sans passer par Tor. Cela vous offre une connexion sécurisée, comparable à l’utilisation de Tor, mais avec une vitesse bien plus élevée et une latence réduite. En résumé, vous conservez les avantages de Tor en matière de confidentialité et de sécurité, tout en bénéficiant de la rapidité d’une connexion en Clearnet. Pour un portefeuille on-chain, ce gain peut sembler marginal, mais si vous envisagez ultérieurement de mettre en place votre propre nœud Lightning, la différence est considérable. En effet, effectuer des paiements via votre nœud en déplacement sur Tor est extrêmement lent en raison des nombreux échanges requis, tandis qu’avec Tailscale, cela fonctionne parfaitement.

- Pas besoin de configurer des règles NAT, d’ouvrir des ports ou de mettre en place un serveur VPN classique. Une fois l’application installée sur Umbrel et vos appareils, le réseau est automatiquement établi.

Tailscale sur Umbrel est donc une solution très intéressante si vous souhaitez accéder à votre nœud depuis n’importe où dans le monde de manière sécurisée, performante et facile à configurer, sans sacrifier la confidentialité ou la sécurité.

Pour installer et configurer Tailscale sur votre Umbrel, consultez ce tutoriel, section 4 : "*Utilisation de Tailscale sur Umbrel*" :

https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr

Nostr, acronyme de "*Notes and Other Stuff Transmitted by Relays*", est un protocole ouvert et décentralisé conçu pour permettre la publication et l’échange de messages sur Internet sans dépendre d’une plateforme centralisée. Chaque utilisateur dispose d’une paire de clés cryptographiques : la clé publique (`npub`) qui sert d’identifiant, et la clé privée (`nsec`) qui permet de signer les messages et d’en garantir l’authenticité.

Les messages sont transmis à travers un réseau de relais indépendants. Cette architecture distribuée rend Nostr résistant à la censure : aucun serveur unique ne contrôle l’accès ou la diffusion, et un utilisateur peut se connecter à autant de relais qu’il le souhaite.

Ce protocole est très populaire au sein de la communauté Bitcoin, car, à l’instar de Bitcoin, Nostr répond à des enjeux de souveraineté numérique et de maîtrise des données. Son créateur, Fiatjaf, est un développeur qui était déjà reconnu dans l’écosystème pour ses nombreuses contributions.

Grâce à votre Umbrel, vous pouvez optimiser votre utilisaiton de Nostr. En installant l’application ***Nostr Relay***, vous pouvez héberger votre propre relais privé directement sur votre machine, ce qui garantit que toutes vos publications et interactions sur Nostr sont sauvegardées localement, et ne peuvent pas être perdues suite à une suppression par des relais publics.

Les clients Nostr ***noStrudel*** ou ***Snort*** sont également disponibles sur Umbrel. Grâce à ces applications, il est possible de publier, lire, rechercher des profils et interagir avec l’écosystème Nostr directement depuis l’interface web de son Umbrel.

Enfin, il y a l'application ***Nostr Wallet Connect*** sur Umbrel, qui permet de faire des paiements Lightning natifs dans Nostr. Concrètement, vous pouvez relier votre futur nœud Lightning à vos clients Nostr pour envoyer des micro-paiements, appelés "*zaps*", afin de récompenser un contenu ou interagir de manière monétisée, sans passer par un service tiers. Ces paiements partent directement de votre nœud personnel via vos canaux.

Pour savoir comment utiliser toutes ces applications, je vous conseille de découvrir ce tutoriel complet :

https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### BTCPay Server

BTCPay Server est un processeur de paiement libre et open-source permettant d’accepter des paiements via Bitcoin et le Lightning Network sans intermédiaire, en conservant la self-custody des fonds.

L’architecture de BTCPay Server repose sur un nœud Bitcoin et, pour Lightning, sur une implémentation compatible (LND, Core Lightning…), ce qui en fait une des seules solutions de PoS totalement non custodiales. C'est également le logiciel le plus complet pour le suivi et la comptabilité.

Si vous possédez un commerce et souhaitez accepter les paiements en bitcoins directement via votre nœud Umbrel, l’application BTCPay Server est idéale pour vous. Pour en savoir plus à ce sujet, je vous recommande de consulter les ressources suivantes :

- Le cours BIZ 101 sur l'utilisation de Bitcoin dans votre entreprise :

https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a

- Le cours POS 305 sur l'utilisation de BTCPay Server :

https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1

- Le tutoriel sur BTCPay Server :

https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Concepts avancés et bonnes pratiques
<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>


## Comprendre l’IBD et le processus de découverte des pairs
<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>

Votre nœud Bitcoin démarre sans aucune connaissance préalable de l’historique des transactions. Au départ, ce n’est qu’un ordinateur équipé d’un logiciel (Bitcoin Core ou autre). Pour devenir un nœud Bitcoin pleinement synchronisé et opérationnel, il doit reconstruire localement l’état du registre en vérifiant l’intégralité des blocs publiés depuis le bloc de Genèse (bloc 0, publié par Satoshi Nakamoto le 3 janvier 2009). Cette étape est appelée **IBD (_Initial Block Download_)**.

L’IBD consiste à télécharger et à vérifier un par un chaque bloc et chaque transaction, en appliquant les règles de consensus, pour construire sa propre version de la blockchain. L’objectif n’est pas simplement de récupérer une copie de données non vérifiées, mais bien d’aboutir, de façon totalement indépendante, à la même conclusion que la majorité honnête du réseau.

### Les grandes étapes de l’IBD

La synchronisation débute par l’étape _**headers-first**_. Votre nœud demande à plusieurs pairs la suite des en-têtes de blocs et, pour chacun d’eux, vérifie la preuve de travail, l’ajustement de la difficulté, la syntaxe, ainsi que les règles relatives aux horodatages et aux numéros de version. En résumé, il s’assure que chaque en-tête reçu respecte bien les règles de consensus.

Pour rappel, un bloc Bitcoin se compose d’un en-tête de 80 octets et d’une liste de transactions. L’empreinte du bloc est obtenue en appliquant un double hachage SHA-256 sur cet en-tête, lequel regroupe 6 champs :
- version
- hachage du bloc précédent
- racine de Merkle des transactions
- horodatage (supérieur au temps médian des 11 blocs précédents)
- cible de difficulté
- nonce

Les transactions sont en effet engagées au sein d’un arbre de Merkle. C'est une structure qui résume un grand ensemble de données (ici, toutes les transactions du bloc) en agrégeant leurs hachages progressivement deux à deux jusqu’à une seule "racine", ce qui permet de prouver qu’un élément appartient à l’ensemble (et de détecter toute modification). Ainsi, toute modification d'une transaction modifie également la racine de l'arbre de Merkle et donc l’empreinte de l’en-tête du bloc. SegWit a introduit un engagement supplémentaire distinct pour les témoins (signatures), placé dans la coinbase.

Cette étape _**headers-first**_ permet au nœud d’identifier la branche cumulant le plus de travail (indépendamment de son nombre de blocs), qui est la branche sur laquelle les nœuds Bitcoin se synchronisent. Une fois cette branche repérée, le nœud télécharge le contenu des blocs en parallèle depuis plusieurs connexions, puis valide chaque transaction : format, validité des scripts (sauf `assumevalid=1`), montants et absence de double dépense. À chaque vérification réussie, l’état courant des pièces non dépensées (UTXO set) est mis à jour dans la base de données `chainstate/` : les sorties dépensées sont retirées, tandis que les nouvelles sorties valides sont ajoutées.

La mempool, quant à elle, n’intervient qu’à l’approche de la pointe de la chaîne : tant que le nœud reste en retard, il n’a aucune transaction en attente à stocker.

Une fois l’IBD achevée, le nœud entre en phase normale : il valide les nouveaux blocs à mesure qu’ils sont publiés, maintient sa mempool avec les transactions en attente selon ses règles de relais, relaie transactions et blocs, et gère les éventuelles réorganisations de la chaîne.

### AssumeValid

Bitcoin Core intègre un mécanisme destiné à réduire le temps nécessaire avant qu’un nœud soit pleinement opérationnel, tout en conservant l’essentiel du principe de vérification autonome : AssumeValid.

Le paramètre `assumevalid` repose sur un bloc de référence passé, dont le hachage est intégré dans chaque version du logiciel. Durant l’IBD, si votre nœud constate que ce bloc se trouve bien sur la branche cumulant le plus de travail, il peut alors ignorer la vérification des scripts pour toutes les transactions antérieures à ce point.

Les autres règles (structure des blocs, preuve de travail, limites de taille, montants des transactions, UTXOs...) restent intégralement vérifiées. Seul le calcul des scripts antérieurs à ce bloc de référence est ignoré. Le gain en performance est important sur l'IBD, car la vérification des signatures représente une part importante de la charge CPU. Au-delà de ce bloc de référence, la vérification redevient complète et normale.

Vous pouvez forcer la validation intégrale de tous les scripts en désactivant ce mécanisme, au prix d’une IBD beaucoup plus longue, grâce au paramètre `assumevalid=0` dans le fichier `bitcoin.conf`.

### AssumeUTXO

`assumeutxo` est un autre paramètre existant, mais, contrairement à `assumevalid`, il n’est pas activé par défaut. Ce mécanisme permet au logiciel de charger un instantané de l’UTXO set, accompagné de ses métadonnées, et de le considérer provisoirement comme état de référence, après avoir vérifié que les en-têtes mènent bien à la blockchain avec le plus de travail.

Le nœud devient ainsi rapidement opérationnel pour des usages courants (RPC, connexion de portefeuilles, indexation externe...), tout en lançant, en arrière-plan, la reconstruction complète et vérifiée de son propre UTXO set. Une fois cette étape terminée, l’instantané initial est remplacé par l’état reconstitué localement. Cette approche dissocie la mise à disposition rapide du nœud et la vérification intégrale, sans pour autant sacrifier cette dernière.

### Découverte des pairs : comment votre nœud trouve-t-il le réseau Bitcoin ?

Lors de son premier démarrage, un nœud ne connaît encore aucun pair. Pourtant, il doit impérativement trouver d’autres nœuds Bitcoin sur internet pour leur demander les en-têtes, puis les blocs, et ainsi réaliser son IBD. Pour amorcer ces connexions, Bitcoin Core suit une logique avec un ordre de priorité.

Lorsque le nœud redémarre après avoir déjà été utilisé, Core commence par consulter son carnet d’adresses IP **`peers.dat`**, qui conserve la liste des pairs rencontrés précédemment, afin de pouvoir s’y reconnecter. Il s’agit simplement d’un fichier local, mis à jour et conservé par Core. En revanche, pour un nouveau nœud qui vient d'être lancé, ce fichier est vide, puisqu’il n’a encore jamais communiqué avec d’autres nœuds Bitcoin.

Dans ce cas, le logiciel interroge des _**DNS seeds**_. Il s’agit [de serveurs maintenus par des développeurs reconnus de l’écosystème](https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp), qui renvoient une liste d’adresses IP de nœuds présumés actifs. Ces adresses permettent au nouveau nœud d’initier ses premières connexions et de réclamer les données nécessaires à l’IBD. Voici la liste des *DNS seeds* actifs à ce jour (août 2025) :
- Pieter Wuille : `seed.bitcoin.sipa.be.`  
- Matt Corallo : `dnsseed.bluematt.me.`  
- Luke Dashjr : `dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us.`  
- Jonas Schnelli : `seed.bitcoin.jonasschnelli.ch.`  
- Peter Todd : `seed.btc.petertodd.net.`  
- Sjors Provoost : `seed.bitcoin.sprovoost.nl.`  
- Stephan Oeste : `dnsseed.emzy.de.`  
- Jason Maurice : `seed.bitcoin.wiz.biz.`  
- Ava Chow : `seed.mainnet.achownodes.xyz.`

Dans la grande majorité des cas, l’étape des *DNS seeds* suffit à établir les premières connexions avec d’autres nœuds. Si, exceptionnellement, ces serveurs ne répondent pas dans un délai de 60 secondes, le nœud passe à une autre méthode : [une liste statique de plus de 1 000 adresses](https://github.com/bitcoin/bitcoin/blob/master/src/chainparamsseeds.h) de _seed nodes_ est intégrée au code de Bitcoin Core et régulièrement mise à jour. Si les deux premières méthodes pour obtenir des adresses IP échouent, cette dernière solution permet d'établir une première connexion, à partir de laquelle le nœud pourra ensuite demander de nouvelles adresses IP.

En ultime recours, il est possible de fournir manuellement des adresses IP via le fichier `peers.dat` afin de forcer des connexions spécifiques.

Une fois l’amorçage effectué, le gestionnaire interne d’adresses veille à diversifier les sources (réseaux autonomes distincts, clearnet et Tor, zones géographiques variées...) pour réduire le risque d’isolement topologique. Le nœud établit ces connexions sortantes (connexions qu’il sélectionne lui-même, donc plus sûres).

Si votre nœud écoute sur un port ouvert (8333 par défaut), il accepte des connexions entrantes. Celles-ci renforcent la résilience globale du réseau en offrant un point de contact pour les nouveaux nœuds, sans apporter d’avantage particulier à votre propre IBD. Si votre nœud fonctionne sur Tor, la logique reste identique, mais les adresses utilisées sont alors des services `.onion`.


## Anatomie de votre nœud Bitcoin
<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>

Explication du modèle de données local d’un nœud : stockage des blocs (expliquer comment ça fonctionne concrètement, ou le trouver...), gestion de l'UTXO set et de la mempool.






Lorsque votre nœud a terminé sa synchronisation initiale, il conserve localement plusieurs ensembles de données complémentaires qui lui permettent de valider les blocs et transactions, de servir des pairs du réseau et de redémarrer rapidement en conservant son état. 3 briques principales sont essentielles sur un nœud :
- les **blocs** de la blockchain stockés sur disque,
- l’**UTXO set** maintenu en base de données clé-valeur,
- et la **mempool** conservée en mémoire vive et périodiquement sérialisée.

À cela s’ajoutent quelques fichiers auxiliaires (peers, estimations de frais, listes d’exclusion, portefeuilles...) qui complètent l’ensemble. Découvrons ensemble le rôle de tous ces fichiers.

### Où se trouvent concrètement les données du nœud ?

Par défaut, Bitcoin Core enregistre ses données dans un répertoire de travail spécifique. Sous GNU/Linux, il se trouve généralement dans `~/.bitcoin/`, sous Windows dans `%APPDATA%\Bitcoin\`, et sous macOS dans `~/Library/Application Support/Bitcoin/`. Si vous utilisez une solution packagée (par exemple au sein d’une distribution de nœud), ce répertoire peut être monté ailleurs mais sa structure reste la même. Les sous-dossiers et fichiers importants décrits ci-dessous s’y trouvent toujours.

### Les blocs

La blockchain est donc un ensemble de blocs. Un nœud complet conserve ces blocs sous forme de fichiers plats séquentiels et maintient en parallèle un index pour les retrouver rapidement. En cas de besoin (réorganisation, rescan de portefeuille, service aux pairs), ces données sont relues telles quelles.

**Note :** Une réorganisation ou resynchronisation, est un phénomène dans lequel la blockchain subit une modification de sa structure à cause de l'existence de blocs concurrents à une même hauteur. Cela survient lorsqu'une portion de la chaîne de blocs est remplacée par une autre chaîne ayant une quantité de travail accumulé plus importante. Ces resynchronisations font partie du fonctionnement naturel de Bitcoin, où différents mineurs peuvent trouver de nouveaux blocs presque simultanément, venant ainsi couper le réseau Bitcoin en deux. Dans de tels cas, le réseau peut se diviser temporairement en chaînes concurrentes. Finalement, lorsque l'une de ces chaînes accumule plus de travail, les autres chaînes sont abandonnées par les nœuds, et leurs blocs deviennent ce que l'on appelle des "blocs obsolètes" ou "blocs orphelins". Ce processus de remplacement d'une chaîne par une autre est la resynchronisation.

#### Fichiers blk*.dat (données brutes des blocs)

Les blocs reçus et validés sont écrits dans des conteneurs séquentiels nommés `blkNNNNN.dat`, stockés dans le dossier `blocks/`. Chaque fichier est rempli à la suite jusqu’à atteindre une taille maximale d’environ 128 Mio, puis Core ouvre le fichier suivant. À l’intérieur, chaque bloc est sérialisé en format réseau, précédé d’un identifiant magique et d’une longueur. Cette organisation permet une écriture rapide sur disque et facilite le service de blocs aux pairs qui se synchronisent.

En mode élagué, le nœud conserve uniquement une fenêtre récente de ces fichiers pour limiter l’empreinte disque. Il supprime les plus anciens conteneurs `blk*.dat` dès que l’objectif d’espace configuré est atteint, tout en conservant suffisamment d’historique pour rester cohérent avec la meilleure chaîne connue. L’index et l’UTXO set restent normaux, ce qui permet la validation des prochaines transactions et des prochains blocs.

#### Fichiers rev*.dat (données d’annulation)

Pour pouvoir revenir en arrière lors d’une réorganisation, Core enregistre, parallèlement à chaque fichier `blk`, un fichier `revNNNNN.dat` dans `blocks/`. Ce fichier contient les informations nécessaires pour défaire l’effet d’un bloc sur l’UTXO set : pour chaque sortie consommée par le bloc, on stocke l’état antérieur de l’UTXO correspondant (montant, script, hauteur...). En cas d’abandon de blocs, le nœud peut ainsi reconstituer l’état précédent rapidement sans rescanner toute la chaîne.

#### Index des blocs (blocks/index)

Rechercher un bloc directement dans les fichiers plats serait trop long. Core maintient donc une base de données LevelDB dans `blocks/index/` qui répertorie, pour chaque bloc connu, des métadonnées comme le hash, la hauteur, le statut de validation, le fichier `blk` et l’offset où il se trouve. Lorsqu’un pair demande un bloc, ou lorsqu’un composant interne doit accéder à un bloc précis, cet index permet un accès rapide. Sans cet index, cela demanderai bien trop d'opérations.

#### Index facultatifs (indexes/)

Certains index sont optionnels et désactivés par défaut, car ils augmentent l’empreinte disque :
- `indexes/txindex/`, dont nous avons déjà parlé, qui fournit une table de correspondance transaction → emplacement, permettant de retrouver n’importe quelle transaction confirmée sans connaître le bloc qui la contient. C'est utile pour des requêtes RPC de type `getrawtransaction` hors portefeuille, mais c'est assez coûteux.
- `indexes/blockfilter/` qui peut contenir des filtres compacts de blocs (BIP157/158) destinés aux clients légers. Ces structures accélèrent la vérification côté client au prix d’un stockage supplémentaire sur le nœud indexeur.

### L’UTXO set (chainstate)

Le modèle UTXO (*Unspent Transaction Output*) est la représentation comptable de Bitcoin : chaque sortie non dépensée est une "pièce" disponible qui pourra servir d’entrée à une future transaction. L’ensemble de toutes ces pièces à un instant T constitue l’UTXO set : une grosse liste de toutes les pièces disponibles maintenant. C’est cet état que le nœud consulte pour décider si une transaction dépense des unités légitimes et non déjà utilisées dans une transaction antérieure (pour éviter la double dépense).

L’UTXO set est conservé dans le dossier `chainstate/` sous la forme d’une base LevelDB compacte. Chaque pièce associe une clé dérivée du hash de la transaction et de l’index de sortie, à une valeur contenant : le montant, le `scriptPubKey` de verrouillage, la hauteur du bloc de création et un indicateur coinbase.

Le nœud maintient un cache mémoire au-dessus de LevelDB afin d’absorber les lectures/écritures fréquentes. Le paramètre `dbcache` permet de modifier la taille de ce cache : plus il est grand, plus l’IBD et la validation courante bénéficient d’accès mémoire, au prix d’une consommation RAM plus grande. Lorsqu'un nouveau bloc est trouvé par un mineur, le nœud supprime de l'UTXO set les sorties dépensées (consommées) par les transactions incluses dans le bloc et ajoute les sorties nouvellement créées.

Théoriquement, on pourrait valider une transaction en rescannant l’historique des blocs pour vérifier qu’une sortie n’a jamais été dépensée. Mais en pratique, ce serait beaucoup trop long, car il faudrait scanner toute la blockchain à chaque nouvelle transaction. L’UTXO set fournit ainsi la vue minimale suffisante pour prouver localement, et en temps raisonnable, l’absence de double dépense.

Notons que L'UTXO set est souvent au cœur d'inquiétudes sur la décentralisation de Bitcoin, car sa taille augmente naturellement très rapidement. Cette hausse s’explique notamment par l’augmentation du prix du bitcoin, qui encourage la fragmentation des pièces, ainsi que par l’adoption croissante du réseau : plus il y a d’utilisateurs, plus la demande en UTXOs est importante. La croissance de l'UTXO set découle également de la structure des transactions de paiement simples sur Bitcoin. En effet, lorsque vous effectuez un paiement, vous consommez un seul UTXO en entrée et créez en sortie 2 nouveaux UTXOs (l’un pour le paiement et l’autre pour le change). Enfin, une heuristique d’analyse de chaîne, appelée CIOH (*Common Input Ownership Heuristic*), est une incitation supplémentaire à éviter la consolidation de pièces.

https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Puisqu'il faut en conserver une partie en RAM pour pouvoir procéder à la vérification des transactions en temps raisonnable, il est possible que l'UTXO set rende progressivement l'opération d'un nœud complet trop couteuse. Pour résoudre ce problème, il existe déjà quelques propositions, notamment [Utreexo](https://planb.network/resources/glossary/utreexo).

### La mempool

La mempool est l’ensemble local des transactions valides reçues, mais pas encore confirmées. Pour rappel, une "transaction confirmée" est une transaction qui a été incluse dans un bloc valide. Chaque nœud maintient sa propre mempool, qui peut différer de celle des autres nœuds du réseau en fonction de :
- la taille allouée à la mempool via le paramètre `maxmempool` : un nœud disposant d’une mempool plus grande pourra contenir davantage de transactions qu’un nœud dont la mempool est plus limitée (sauf si cette dernière se vide) ;
- les règles de mempool : elles constituent un sous-ensemble des règles de relais du nœud et définissent les caractéristiques qu’une transaction non confirmée doit respecter pour être acceptée dans la mempool ;
- la percolation des transactions : en raison de divers facteurs, une transaction donnée peut avoir été diffusée à une partie du réseau, mais ne pas avoir encore atteint une autre partie.

Il est important de noter que les mempools des nœuds n’ont aucune valeur de consensus. Bitcoin fonctionne parfaitement même si chaque nœud possède une mempool différente. Au final, ce qui fait autorité reste toujours les blocs ajoutés à la blockchain. Par exemple, même si un nœud refuse initialement une transaction donnée dans sa mempool (valide selon les règles de consensus), il sera obligé de l’accepter si celle-ci est finalement incluse dans un bloc disposant d’une preuve de travail valide. S’il ne le faisait pas et rejetait ce bloc pourtant conforme aux règles de consensus, il provoquerait un hardfork, c’est-à-dire la création d’un nouveau Bitcoin distinct sur lequel il serait seul.

#### Politique et gestion de la mémoire

À la réception d’une transaction, Core donc applique une série de vérifications des règles de consensus (syntaxe, scripts valides, pas de double dépense...) et des règles de mempool, qui sont une politique locale (RBF, seuils de frais minimaux, limite de la data dans les `OP_RETURN`...). Si la transaction respecte ces règles, elle est insérée en mémoire.

La taille de la mempool est bornée par le paramètre `maxmempool` dans le fichier `bitcoin.conf` (nous en parlerons dans le prochain chapitre). Par défaut, la limite est de 300 Mo. Lorsqu’elle est pleine, le nœud relève dynamiquement son seuil de frais minimal et expulse en priorité les transactions les moins rémunératrices (c'est-à-dire les transactions qui devraient être minées en premières). Les transactions trop anciennes peuvent également expirer après un délai configuré.

#### Persistance de la mempool sur disque

Pour accélérer les redémarrages, Core sérialise périodiquement l’état de la mempool dans le fichier `mempool.dat` à l’arrêt du nœud. En plus de la mempool réelle qui reste donc en mémoire, Core conserve ce fichier `mempool.dat` sur le disque. Au lancement suivant, il recharge ce snapshot et élimine ce qui n’est plus valide vis-à-vis de la blockchain actuelle.

### Fichiers et bases auxiliaires

Plusieurs autres fichiers au même niveau que `blocks/`, `chainstate/` et `indexes/` participent au bon fonctionnement du nœud :
- `peers.dat` conserve un carnet d’adresses IP de pairs potentiels, alimenté par la découverte DNS initiale, les échanges réseau et les ajouts manuels. Lors de son démarrage, le nœud peut piocher dans ce fichier si besoin pour établir ses connexions sortantes ;
- `anchors.dat` enregistre, à l’extinction du nœud, les adresses de pairs sortants afin de tenter de les recontacter rapidement au prochain démarrage ;
- `banlist.json` contient les bannissements locaux décidés par l’opérateur ou par le nœud (comportements invalides répétés), afin d'empêcher le nœud de se reconnecter ou d'accepter des connexions de ces pairs spécifiques ;
- `fee_estimates.dat` stocke des statistiques d’horizon temporel sur les confirmations observées, utilisées par l’estimateur de frais pour proposer des taux de frais cohérents avec les objectifs de délai choisis lors de la création d'une transaction ;
- `bitcoin.conf` contient les paramètres de configuration de votre nœud. C’est notamment dans ce fichier que l’on peut ajuster les règles de relais. Je vous en parlerai plus en détail dans le prochain chapitre ;
- `settings.json` contient d'autres paramètres supplémentaires au `bitcoin.conf` ;
- `debug.log` est le journal texte de diagnostic, qui peut servir pour comprendre l’activité du nœud en cas de bug ;
- `bitcoind.pid` enregistre l’identifiant de processus pendant l’exécution, qui permet à d'autres applications ou scripts d'identifier facilement Bitcoind (*Bitcoin Daemon*) et d'interagir avec lui si nécessaire. Il est créé au démarrage du nœud et supprimé à l’arrêt ;
- `ip_asn.map` est une table de correspondance IP → ASN (système autonome) utilisée pour le bucketing et la diversification des pairs (option `-asmap`) ;
- `onion_v3_private_key` stocke la clé privée du service Tor v3 lorsque l’option `-listenonion` est activée, afin de conserver une adresse onion stable entre les redémarrages ;
- `i2p_private_key` stocke la clé privée I2P lorsque `-i2psam=` est utilisé, pour réaliser des connexion sortantes et éventuellement entrantes sur I2P ;
- `.cookie` contient un jeton d’authentification RPC éphémère (créé au démarrage, supprimé à l’arrêt) lorsque l’authentification par cookie est utilisée. Cela peut être utilisé par exemple pour connecter un logiciel de portefeuille ;
- `.lock` est le verrou du répertoire de données, qui empêche plusieurs instances d’écrire simultanément dans le même datadir ;
- `guisettings.ini.bak` est la sauvegarde automatique des paramètres de la GUI (*Bitcoin Qt*) lorsque l’option `-resetguisettings` est utilisée.

Comme nous l’avons vu dans les premières parties de ce cours BTC 202, Bitcoin Core est à la fois un logiciel de nœud Bitcoin et un logiciel de gestion de portefeuille. Cependant, ce n’est pas forcément la solution que je vous recommande pour gérer vos portefeuilles, car son interface reste sommaire et ses fonctionnalités limitées en comparaison de logiciels modernes comme Sparrow ou Liana. Core inclut donc également des fichiers destinés à gérer vos éventuels portefeuilles :

- `wallets/` est le répertoire par défaut qui héberge un ou plusieurs portefeuilles ;
- `wallets/<name>/wallet.dat` est la base SQLite du portefeuille (clés, descriptors, métadonnées de transactions...) ;
- `wallets/<nom>/wallet.dat-journal` est le journal de rollback SQLite.

Pour résumer, voici la structure de fichiers de Bitcoin Core :

```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```

### Le chemin de validation d'un nouveau bloc

À la réception d’un nouveau bloc, votre nœud vérifie la preuve de travail et, plus largement, le respect des règles de consensus. Si tout est bon, il applique transaction par transaction les modifications sur son UTXO set : il s’assure que chaque entrée dépense des UTXOs existant avec un script valide, supprime ces UTXOs et ajoute les nouvelles sorties. Si tout est valide les changements sont engagés dans `chainstate/`.

En parallèle, les données d’annulation sont écrites dans `rev*.dat` et les métadonnées dans l’index `blocks/index/`. Le bloc est ensuite sérialisé dans le bon fichier `blk*.dat`. En cas de réorganisation, le nœud lit `rev*.dat` à rebours pour déconnecter proprement les blocs abandonnés, restaurer l’UTXO set, puis connecter les blocs de la nouvelle meilleure chaîne.



## Comprendre le fichier bitcoin.conf
<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>

Le fichier `bitcoin.conf` est la principale interface de configuration de Bitcoin Core. Il permet d’ajuster le comportement et les paramètres de votre nœud sans avoir à recompiler son code source ou faire des modifications en lignes de commande. Concrètement, c'est un fichier texte brut structuré en paires clé-valeur, c'est-à-dire que chaque ligne du fichier référence un paramètre spécifique (la clé) et une valeur associée qui peut être modifiée pour ajuster ce paramètre.

On peut définir dans le `bitcoin.conf` des paramètres de réseau, de relais de transactions, de performances, d’indexation, de journalisation ou encore d’accès RPC. En revanche, ce fichier de configuration ne modifie jamais les règles de consensus du protocole : il fixe uniquement la politique locale du nœud (règles de relai), la manière dont il se connecte, indexe et expose des services.

### Emplacement et priorité

Par défaut, `bitcoin.conf` réside dans le répertoire de données de Bitcoin Core. C'est le fameux répertoire dont nous avons déjà parlé dans le chapitre précédant. En revanche, ce fichier n’est pas créé automatiquement par Bitcoin Core, sauf lorsqu’il est utilisé dans certains environnements comme Umbrel par exemple. S’il n’existe pas encore, vous devrez donc le générer vous-même en créant simplement un fichier nommé `bitcoin.conf`, puis en l’ouvrant dans un éditeur de texte pour y apporter vos modifications.

Les paramètres définis dans le `bitcoin.conf` peuvent être surchargés par 2 couches :
- `settings.json` (écrit dynamiquement par l’interface graphique ou certaines RPC),
- et les options modifiées via les lignes de commande.

Notons que toute modification du `bitcoin.conf` nécessite un redémarrage du nœud pour être prise en compte.

### Format et structure

Le format du `bitcoin.conf` est donc très simple : une ligne par option, sous la forme `option=valeur`. Les espaces inutiles et les lignes vides sont ignorés et les commentaires de code commencent par `#`.

La quasi-totalité des options booléennes peuvent être désactivées par un préfixe `no`. Par exemple `listen=0` et `nolisten=1` sont équivalents selon les versions.

Pour segmenter la configuration par réseau, on peut utiliser des sections : `[main]`, `[test]` (testnet3), `[testnet4]`, `[signet]`, `[regtest]`. Ou alors on peut préfixer le nom d’option : `regtest.maxmempool=100`.

### Ce que le bitcoin.conf peut et ne peut pas faire

Comment expliqué précédemment, les règles de consensus ne sont évidemment pas configurable dans le `bitcoin.conf`, puisque cela pourrait créer un hard fork. En revanche, beaucoup d’aspects non consensuels sont paramétrables. On distingue trois classes utiles à garder en tête :
- Les paramètres purement locaux. Ils n’affectent que votre nœud : taille du cache (`dbcache`), mode élagué (`prune`), index optionnels... Ils influencent les performances de votre machine, mais pas le réseau ;
- Les politiques de relais et de mempool. Elles décident de ce que votre nœud accepte, conserve et relaie avant confirmation : seuil minimal de frais (`minrelaytxfee`), taille et durée de rétention de la mempool (`maxmempool`, `mempoolexpiry`), remplacement des transactions (RBF)... Ces règles ne font pas partie du consensus, donc deux nœuds différents peuvent avoir des politiques différentes et rester pleinement compatibles. En revanche, ces paramètres vont avoir une influence sur le réseau Bitcoin (comme expliqué dans la première partie, notamment avec la théorie de la percolation) ;
- La connectivité réseau. Ce sont les options qui déterminent comment votre nœud trouve des pairs, écoute, traverse un NAT, utilise Tor ou un proxy, ou limite sa bande passante. Elles façonnent votre topologie, mais n’altèrent pas le relai des transactions.

Comprendre cette séparation est très important : si une transaction ne respecte pas les règles de consensus, votre nœud la rejettera dans tous les cas. Mais une politique locale plus stricte peut refuser de relayer une transaction pourtant valide au sens du consensus.

### Réseau et topologie

Tout d’abord, il est essentiel de distinguer clairement les 2 types de connexions qu’un nœud Bitcoin peut avoir :
- Les connexions sortantes, qui sont initiées par notre nœud vers un autre nœud ;
- Les connexions entrantes, qui sont initiées par un autre nœud vers le nôtre.

Ces deux types de connexions peuvent tout à fait échanger les mêmes données dans les deux sens ; il ne s’agit pas d’une limitation du sens du flux, mais uniquement d’une différence dans l’initiateur de la connexion. Du point de vue de notre nœud, les connexions sortantes sont généralement considérées comme plus sûres, car c’est nous qui en prenons l’initiative et choisissons précisément à quel nœud nous connecter, ce qui rend peu probable que cette connexion soit malveillante. Par défaut, Bitcoin Core maintient 10 connexions sortantes (8 "full-relay" + 2 "block-relay-only").

Un nœud complet apporte davantage de valeur au réseau lorsqu’il accepte des connexions entrantes. Le paramètre `listen=1` active l’écoute sur le port 8333 par défaut du réseau concerné, ce qui permet ainsi de recevoir ces connexions entrantes sur le clearnet. Pour que cela fonctionne, ce port doit également être ouvert sur votre routeur. S’il ne l’est pas, votre nœud continuera de fonctionner uniquement avec des connexions sortantes, ce qui n’aura aucun impact sur votre utilisation personnelle de Bitcoin. Le choix d’autoriser ou non les connexions entrantes vous appartient, il n'y a pas de "meilleur choix".

Si vous préférez ne pas ouvrir de port sur votre routeur tout en acceptant des connexions entrantes, vous pouvez activer le paramètre `listenonion=1`. Celui-ci permet d’obtenir le même résultat, mais en passant exclusivement par le réseau Tor plutôt que par le clearnet.

Niveau réseau, on a également :
- `addnode` : ajoute un pair ami à contacter en plus de la découverte habituelle (peut-être spécifié plusieurs fois) ;
- `connect` : restreint strictement les connexions à l'adresse fournie (peut-être spécifié plusieurs fois). Core ne se connectera à aucun autre nœud ;
- `seednode` : sert uniquement à remplir l’adresse-book en se connectant à un nœud, puis se déconnecte ;
- `maxconnections` : définit le plafond global de connexions entrantes + sortantes. Par défaut, ce paramètre est placé à 125, ce qui signifie que votre nœud n'acceptera jamais plus de 125 connexions ;
- `maxuploadtarget` : plafonne l’upload pour limiter la bande passante sur une fenêtre glissante de 24 h. Ce plafond ne sacrifie pas la propagation d’éléments récents indispensables ;
- `onlynet` : limite les connexions sortantes uniquement aux réseaux sélectionnés (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Par exemple, si vous souhaitez que votre nœud se connecte au réseau Bitcoin uniquement via Tor, vous pouvez activer le paramètre `onlynet=onion` et ne pas activer les connexions entrantes (ou bien uniquement via Tor également) ;
- `dnsseed` : autorise ou non la requête des _DNS seeds_ pour obtenir des pairs quand votre réserve locale d’adresses est faible (par défaut : `1`, sauf si `-connect` ou `-maxconnections=0`) ;
- `forcednsseed` : force la requête des _DNS seeds_ au démarrage, même si vous avez déjà des adresses en stock (par défaut : `0`) ;
- `fixedseeds` : Autorise l’usage des *seed nodes* (liste d'adresses hardcodées) si les _DNS seeds_ échouent ou sont désactivés (par défaut : `1`) ;
- `dns` : Autorise les résolutions DNS en général (par exemple pour `-addnode`/`-seednode`/`-connect`) ;

Par défaut, votre nœud communique sur le clearnet, Tor et I2P. Cela implique que les pairs avec lesquels il se connecte en clearnet peuvent voir votre adresse IP publique, et que votre ISP (fournisseur d’accès à Internet) pourra probablement détecter que vous exploitez un nœud Bitcoin (même si P2P Transport V2 complique l’écoute passive par un FAI).C e n’est pas nécessairement problématique, mais si vous souhaitez éviter toute fuite de ces informations, vous pouvez connecter votre nœud exclusivement via Tor.

Pour être entièrement sous Tor, vous devez forcer Bitcoin Core à utiliser uniquement ce réseau et à créer un service caché pour les connexions entrantes (si vous voulez les activez). Dans le `bitcoin.conf`, il faut ajouter cette configuration : 
- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- `bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.

Ainsi, toutes vos connexions P2P transitent par Tor, votre nœud obtient une adresse `.onion` pour les entrantes, aucun port n’a besoin d’être ouvert sur le routeur, votre FAI ne voit que du trafic Tor et vos pairs ne connaissent pas votre IP publique.

Si vous souhaitez éviter toute résolution DNS en clair, vous pouvez ajouter `dnsseed=0` et `dns=0`. Il faudra alors fournir manuellement des pairs `.onion` via `seednode=` ou `addnode=`, sans quoi la découverte de nouveaux nœuds sera difficile.

Évidemment, si vous êtes débutant, je vous conseille dans un premier temps de ne pas toucher à tous ces paramètres réseau. La configuration par défaut est souvent suffisante.





## Confidentialité et sécurité d’un nœud personnel
<chapterId>5e930262-9326-4edd-a128-9504df14eb18</chapterId>

Analyse des risques liés à l’exploitation d’un nœud sur son réseau local. Quelles données sont exposées ? Comment se protéger ? Utilisation de Tor, configuration réseau, pare-feu, gestion des ports ouverts, VPN...










Ouverture vers la prochaine formation : héberger un nœud Lightning LNP 202.







































# Partie finale
<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>



## Avis & Notes
<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>


<isCourseReview>true</isCourseReview>


## Examen final
<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>


<isCourseExam>true</isCourseExam>


## Conclusion
<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>


<isCourseConclusion>true</isCourseConclusion>

