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

Présentation de Bitcoin Core en tant qu’implémentation principale du protocole Bitcoin + chiffres actuels de répartition des nœud + leur poids et pouvoir dans la gouvernance du système. Explication de son architecture interne, de son fonctionnement, et courte histoire de son développement. Mention des autres implémentations existantes (notamment Knot).
















# Pourquoi devenir un bitcoiner souverain ?
<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>


## Pourquoi faire tourner son propre nœud ?
<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>

Analyse des raisons de faire tourner un nœud personnel : indépendance, validation des règles du protocole, confidentialité, résilience... (pas juste de l'altruisme : bénéfices perso).






Ce point mérite une attention particulière : l’utilité d’une monnaie, quelle qu’elle soit, découle directement de sa capacité à faciliter les échanges. En effet, si un objet n’est accepté par personne en échange de biens ou de services, il n’a théoriquement aucune utilité monétaire. Par exemple, si aucun commerçant n’accepte les cailloux comme moyen de paiement, ces derniers n’ont aucune utilité en tant que monnaie. L’utilité reste bien sûr une notion subjective à l’échelle individuelle, mais, sur un territoire donné, plus le nombre de commerçants acceptant un objet comme moyen d’échange est élevé, plus il est probable que cet objet ait une utilité monétaire pour les personnes vivant sur ce territoire.

Prenons l’exemple d’un village où de nombreux commerçants acceptent l’or en échange de biens : il y a alors de fortes chances que l’or possède une utilité monétaire pour les habitants du village. On comprend ainsi que l’utilité d’une monnaie dépend directement de la décision des commerçants de l’accepter ou non.

Cette notion est fondamentale pour appréhender les rapports de force à l’œuvre dans le système Bitcoin. Satoshi le précise : Bitcoin est un système de cash électronique, autrement dit il rend le service de proposer une forme de monnaie, le bitcoin (ou BTC). Lorsque les règles du protocole sont modifiées de façon non rétrocompatible (hard fork), cela revient à créer un nouveau système et donc une nouvelle monnaie. Le succès ou l’échec de ce fork dépend alors de la taille de son économie, qui est elle-même déterminée par le nombre de commerçants acceptant cette nouvelle forme de monnaie.

Prenons un exemple : supposons que Bitcoin subisse un hard fork. Il existerait alors deux formes de monnaies distinctes : BTC-1 (la version originelle, inchangée) et BTC-2 (la nouvelle monnaie avec des règles de consensus différentes). Si l’ensemble des commerçants qui acceptaient BTC-1 continuent à le faire, mais refusent le BTC-2, alors ce dernier n’aura, en théorie, qu’une utilité monétaire très limitée. En tant qu’utilisateur, je n’aurais aucun intérêt à conserver et utiliser du BTC-2, sachant qu’aucun commerçant n’en voudra en échange de biens ou de services. À l’inverse, si 50 % des commerçants choisissent d’accepter exclusivement le BTC-2 et les 50 % restants ne prennent que le BTC-1, alors l'utilité du BTC-1 aura, en théorie, diminué de moitié. J’emploie le terme "théoriquement", car l’utilité demeure subjective au niveau individuel, et dépend d’une multitude de facteurs (territoire, habitudes de consommation, etc.) difficiles à appréhender au cas par cas.

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


## Umbrel : un nœud Bitcoin plug-and-play
<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>

Introduction à Umbrel comme solution accessible et tout-en-un pour les débutants. Umbrel home + Umbrel OS. Cas d'usages.

## Installation d’un nœud complet avec Umbrel
<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>

Tutoriel pas à pas pour installer Umbrel sur un barbone. Téléchargement, configuration initiale + IBD.

## Tour d’horizon des applications disponibles
<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>

Présentation des principales applications qu’on peut ajouter à Umbrel dans le cadre de Bitcoin : Mempool, Lightning, Nostr, BTCPay, Tailscale... Introduction rapide à leurs fonctions + liens vers tutos. Ouverture sur les indexeurs.




















# Connecter son portefeuille à son nœud
<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>

## Les indexeurs : rôle, fonctionnement et solutions
<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>

Explication de la nécessité d’un indexeur pour les portefeuilles. Présentation de celui de base sur Core, d’Electrs et de Fulcrum : avantages et inconvénients.


## Comment connecter son portefeuille à son nœud Bitcoin ?
<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>

Tutoriel de connexion entre un portefeuille personnel (sûrement Sparrow) et son nœud, via plusieurs options : Core RPC, Tor Electrs et Tailscale.













# Concepts avancés et bonnes pratiques
<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>


## Comprendre l’IBD et le processus de découverte des pairs
<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>

Description du processus de synchronisation initiale (Initial Block Download), ses contraintes et les moyens de l’optimiser (assumevalid, assumeutxo...). Explication du mécanisme de découverte des pairs dans le réseau Bitcoin.

## Comprendre le stockage du nœud : blockchain, UTXO set et mempool
<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>

Explication du modèle de données local d’un nœud : stockage des blocs (expliquer comment ça fonctionne concrètement, ou le trouver...), gestion de l'UTXO set et de la mempool.

## Comprendre le fichier bitcoin.conf
<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>

Présentation du fichier `bitcoin.conf` : structure, rôle et options les plus utiles. Différenciation entre règles de consensus et règles de relais.

## Confidentialité et sécurité d’un nœud personnel
<chapterId>5e930262-9326-4edd-a128-9504df14eb18</chapterId>

Analyse des risques liés à l’exploitation d’un nœud sur son réseau local. Quelles données sont exposées ? Comment se protéger ? Utilisation de Tor, configuration réseau, pare-feu, gestion des ports ouverts, VPN...

## Premiers pas vers un nœud Lightning
<chapterId>040fe06c-01e9-453a-9834-353600ba9c2e</chapterId>

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

