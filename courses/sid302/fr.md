---
name: Liquid Bootcamp Essentials
goal: Acquérir une compréhension globale des projets Liquid Network et Elements, et apprendre à mettre en œuvre des solutions avancées en matière de transactions confidentielles, de symbolisation et d'architecture de réseau décentralisé.
objectives: 

  - Comprendre les principes fondamentaux de l'architecture Liquid et sa relation avec Bitcoin.
  - Apprendre à configurer et à exploiter les nœuds Liquid à l'aide du logiciel Elements.
  - Étudier le recours aux transactions confidentielles et à l'émission d'actifs sur le Liquid Network.
  - Comprendre les aspects commerciaux et techniques du Liquid pour les applications sur les marchés des capitaux.

---

# Introduction au réseau Liquid


Embarquez pour un voyage éducatif conçu pour fournir une compréhension approfondie du projet Liquid Network et Elements. Ce bootcamp combine théorie et pratique pour vous enseigner les fondamentaux techniques, architecturaux et commerciaux nécessaires à la mise en œuvre et à l'exploitation des capacités du Liquid. Des transactions confidentielles à la conception de l'écosystème, ce cours est idéal pour ceux qui cherchent à étendre leurs connaissances des outils avancés au sein de l'écosystème Bitcoin.


Avec des présentations d'experts de l'industrie, le cours couvre des sujets tels que l'architecture Liquid, les applications de tokenisation, les concepts techniques de Elements, et des cas d'utilisation innovants comme le SDK Breez. Conçu pour être accessible aux débutants et aux utilisateurs intermédiaires, le cours offre également une valeur ajoutée aux développeurs expérimentés qui cherchent à maîtriser le Liquid en tant que plateforme pour optimiser leurs projets.

+++

# Introduction


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Aperçu du cours


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Bienvenue à l'atelier Liquid, une formation complète conçue pour vous doter des connaissances et des compétences nécessaires pour exploiter efficacement les projets Liquid Network et Elements. Ce cours offre une exploration complète des caractéristiques distinctives de Liquid, y compris Confidential Transactions, l'émission d'actifs, et son architecture de réseau fédéré, tout en introduisant également les concepts fondamentaux de Elements, le logiciel qui alimente Liquid.


Tout au long du camp d'entraînement, vous explorerez les applications pratiques du Liquid Network, de la mise en place et de l'exploitation des nœuds à la compréhension de son utilisation dans les marchés de capitaux et la tokenisation du Bitcoin. Grâce aux présentations d'experts du secteur, vous aurez également un aperçu des sujets avancés tels que les HTLC, le SDK Breez et le projet AMP de Blockstream.


Ce camp d'entraînement était à l'origine organisé en personne, selon un programme structuré (comme le montre l'image) conçu pour des sessions en direct. Cependant, pour cette adaptation du cours, le contenu a été réorganisé pour mieux convenir à un format en ligne et faciliter la compréhension des étudiants. Le nouvel ordre assure une progression logique des concepts fondamentaux vers des sujets plus avancés et techniques, maximisant ainsi l'expérience d'apprentissage.


Ce parcours est structuré de manière à accueillir des participants ayant des niveaux d'expertise variés, offrant un mélange de connaissances théoriques et d'expérience pratique. À la fin de ce camp d'entraînement, vous aurez une solide compréhension de l'architecture de Liquid, de son intégration avec Bitcoin et de la manière d'utiliser ses fonctionnalités innovantes pour construire et optimiser des solutions financières.


Plongez dans le monde de la sidechain Liquid et libérez tout son potentiel dès maintenant !

# Principes de base


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Architecture Liquid


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Architecture et modèle de consensus du Liquid Network


La Liquid Network est une chaîne latérale fédérée construite sur la base de code de la Elements, conçue pour étendre les capacités de la Bitcoin tout en s'appuyant sur sa sécurité fondamentale. Contrairement à la [Proof-of-Work](https://planb.academy/resources/glossary/proof-of-work) de la Bitcoin, la Liquid fonctionne selon un modèle de [consensus](https://planb.academy/resources/glossary/consensus) fédéré. Le réseau est géré par un groupe de membres répartis dans le monde entier, comprenant des bourses, des bureaux de négociation et des fournisseurs d'infrastructure. Parmi ces membres, quinze "fonctionnaires" sont sélectionnés pour agir en tant que signataires de [blocs](https://planb.academy/resources/glossary/block).


Ces fonctionnaires produisent des blocs selon une méthode déterministe de type round-robin, avec un nouveau bloc généré toutes les minutes. Ce calendrier précis contraste avec les intervalles probabilistes de dix minutes de la Bitcoin. Pour qu'un bloc soit valide, il doit être signé par au moins 11 des 15 fonctionnaires (seuil des deux tiers plus un). Ce mécanisme confère à la Liquid une "finalité à deux blocs", ce qui signifie qu'une fois qu'une [transaction](https://planb.academy/resources/glossary/transaction-tx) a reçu deux confirmations (environ deux minutes), il est mathématiquement impossible de réorganiser la chaîne. Cette rapidité et cette certitude sont essentielles pour l'arbitrage, le commerce automatisé et le règlement rapide entre les bourses.


La fédération est dynamique. Grâce au protocole Dynamic Federation (Dynafed), le réseau peut faire tourner les fonctionnaires ou mettre à jour les paramètres sans nécessiter de [fork](https://planb.academy/resources/glossary/fork). Cela permet au système d'évoluer et de remplacer le matériel ou les membres de manière transparente tout en maintenant un fonctionnement continu.


### Confidential Transactions et gestion des actifs


L'une des caractéristiques de la Liquid est sa prise en charge native de la Confidential Transactions (CT) et des actifs multiples. Sur la chaîne principale Bitcoin, tous les détails de la transaction - l'expéditeur, le destinataire et le montant - sont publics. Dans la Liquid, CT utilise des engagements cryptographiques pour cacher le type d'actif et le montant du grand livre public tout en permettant au réseau de vérifier que la transaction est valide (c'est-à-dire qu'il n'y a pas eu d'[inflation](https://planb.academy/resources/glossary/inflation)). Seuls les participants détenant les clés de masquage peuvent voir les valeurs spécifiques, ce qui offre un niveau de confidentialité commerciale essentiel pour les institutions qui déplacent des positions importantes.


Liquid traite tous les actifs comme des citoyens "natifs" de la [blockchain](https://planb.academy/resources/glossary/blockchain). Cela inclut le Liquid Bitcoin (LBTC), les stablecoins comme l'USDT et les security tokens. L'émission d'un actif ne nécessite pas de contrats intelligents complexes ; il s'agit d'une fonction de base du protocole.


#### Actifs réglementés et PGA

Pour les actifs nécessitant une conformité, tels que les jetons de sécurité, Liquid utilise la Blockstream Asset Management Platform (AMP). Celle-ci introduit une couche autorisée dans laquelle les transactions nécessitent une seconde signature de la part d'un serveur d'autorisation. Cela permet aux émetteurs d'appliquer des règles - telles que la liste blanche ou les exigences KYC - à un niveau granulaire, en combinant l'efficacité d'une blockchain avec les contrôles réglementaires de la finance traditionnelle.


### L'infrastructure bidirectionnelle de Peg et de sécurité


La connexion entre Liquid et Bitcoin est maintenue par une connexion bidirectionnelle. Pour se connecter, un utilisateur envoie Bitcoin à une adresse générée sur mainchain. Ces fonds sont bloqués pour 102 confirmations (environ 17 heures) afin d'éliminer les risques de réorganisation. Une fois confirmé, un montant équivalent de LBTC est frappé sur la chaîne latérale Liquid.


Le processus de "peg-out" permet aux utilisateurs d'échanger des LBTC contre des Bitcoin. Il faut pour cela brûler des LBTC et obtenir une autorisation cryptographique de la fédération. Pour éviter les vols, les peg-outs sont strictement contrôlés par des clés d'autorisation de peg-out (PAK) détenues par les membres de la fédération. En outre, les fonds peuvent être échangés instantanément par l'intermédiaire de fournisseurs tiers tels que SideSwap, ce qui permet de contourner le délai de règlement et d'obtenir une liquidité plus rapide.


#### Modules de sécurité matériels (HSM)

La sécurité est strictement assurée par le matériel. Les fonctionnaires ne conservent pas les [clés privées](https://planb.academy/resources/glossary/private-key) sur des serveurs standard ; ils utilisent des modules de sécurité matériels (HSM). Ces dispositifs sont isolés de la logique du serveur hôte et sont programmés avec des règles strictes. Par exemple, un HSM refusera de signer un bloc si sa hauteur n'est pas supérieure à celle du bloc précédent, empêchant ainsi les réécritures de l'historique. Ce modèle de sécurité "contradictoire" suppose que le serveur hôte peut être compromis, ce qui garantit que les clés restent sécurisées même si l'emplacement physique est violé.


## Principes de base de Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements : Les fondements de Liquid


Elements est une plateforme blockchain open-source dérivée de la base de code Bitcoin Core. Elle étend la fonctionnalité de Bitcoin en permettant des blockchains indépendantes des sidechains qui peuvent transférer des actifs vers et depuis Bitcoin. Alors que Bitcoin Core alimente le réseau Bitcoin, Elements est le moteur logiciel derrière Liquid Network et d'autres sidechains personnalisées.


La relation est simple : Liquid est une "instance" spécifique d'une chaîne latérale Elements, configurée pour une utilisation en production avec un modèle de consensus fédéré. Les développeurs familiers avec Bitcoin trouveront Elements intuitif, car il conserve la même interface RPC (Remote Procedure Call) et la même structure de ligne de commande (`elements-cli`, `elements-d`, `elements-qt`). La principale différence réside dans la configuration : le réglage de `chain=liquidv1` connecte un [noeud](https://planb.academy/resources/glossary/node) au réseau Liquid principal, tandis que `chain=elementsregtest` crée un environnement de test de régression local où les développeurs peuvent generate blocs instantanément et tester sans dépendances externes.


#### Émission d'actifs

L'une des particularités de Elements est l'émission native d'actifs. Contrairement à Ethereum, où les jetons sont des contrats intelligents complexes, les actifs de Elements sont des citoyens de première classe créés via une simple commande RPC (`issueasset`).


- Identifiants uniques:** Chaque bien reçoit un identifiant hexadécimal unique de 64 caractères.
- Jetons de réémission:** Les émetteurs peuvent optionnellement créer des jetons de réémission, qui accordent à leur détenteur le droit de frapper plus tard d'autres jetons (utile pour les stablecoins ou les jetons de sécurité).
- Registre des actifs:** Les identifiants hexadécimaux n'étant pas lisibles par l'homme, le registre des actifs de Blockstream les associe à des noms et à des codes (par exemple, "USDT"), à la manière d'un DNS pour les actifs.


### Vie privée via Confidential Transactions


Elements répond à l'une des principales limites des blockchains publiques : le manque de confidentialité commerciale. Sur la Bitcoin, chaque montant de transaction est visible par le monde entier. Elements introduit **Confidential Transactions (CT)**, qui masque cryptographiquement le montant et le type d'actif tout en permettant au réseau de vérifier la validité de la transaction.


Pour ce faire, on utilise les **engagements de Pedersen** et les **preuves de portée**.


- Les engagements Pedersen** remplacent le montant visible par un engagement cryptographique. Grâce au cryptage homomorphique, les validateurs peuvent vérifier que *Engagements d'entrée = Engagements de sortie + Frais* sans jamais voir les valeurs réelles.
- Les preuves de plage** empêchent un utilisateur de créer de l'argent à partir de rien (par exemple, en utilisant des nombres négatifs) en prouvant mathématiquement que la valeur cachée est un nombre entier positif compris dans une plage valide.


Pour un observateur extérieur, une transaction confidentielle présente des entrées et des sorties valides, mais ne permet pas de savoir *ce qui* est envoyé et *qui* est envoyé. Seuls l'expéditeur et le destinataire (qui possèdent les clés d'anonymat) peuvent voir les données en clair.


### Développement et flux de travail RPC


L'interaction avec un nœud Elements se fait principalement par l'intermédiaire de son interface JSON-RPC. Cela permet aux applications écrites en Python, JavaScript ou Go de communiquer avec la blockchain.



- Configuration:** Un développeur démarre généralement en mode `regtest`. Cela permet la génération instantanée de blocs (`generateblock`) pour confirmer les transactions immédiatement, en contournant le temps de bloc d'une minute du réseau réel.
- Commandes:** Les commandes standard de Bitcoin comme `getblockchaininfo` sont disponibles, ainsi que les commandes spécifiques à Elements comme `dumpblindingkey` (pour auditer les CTs) ou `pegin` (pour déplacer des BTC dans la sidechain).
- Alias:** Pour gérer plusieurs noeuds (par exemple, un "émetteur" et un "récepteur" pour les tests), les développeurs utilisent souvent des alias shell comme `e1-cli` et `e2-cli` pointant vers différents répertoires de données, simulant ainsi un réseau [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) sur une seule machine.


Cette architecture permet aux développeurs de créer des applications financières sophistiquées, telles que des plateformes de titres ou des passerelles de paiement privées, en utilisant les outils robustes et familiers de l'écosystème Bitcoin.


## Connexion des couches Bitcoin


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Infrastructure Cross-Layer et HTLCs


L'écosystème Bitcoin a évolué vers une architecture multicouche, avec la Mainchain fournissant le règlement, Lightning offrant la vitesse, et Liquid permettant des capacités d'actifs avancées. Le déplacement de la valeur entre ces couches sans intermédiaires centralisés nécessite une primitive cryptographique sans confiance : le Hash Time Locked Contract ([HTLC](https://planb.academy/resources/glossary/htlc)).


Un HTLC crée un [canal de paiement](https://planb.academy/resources/glossary/payment-channel) conditionnel qui relie des systèmes indépendants de manière atomique. Il fonctionne grâce à deux contraintes principales : un **serrure de [hachage](https://planb.academy/resources/glossary/hash-function)** et un **serrure de temps**.


- La serrure Hash:** Les fonds peuvent être dépensés immédiatement si le destinataire révèle une "préimage" secrète qui correspond à un hachage cryptographique spécifique.
- Le verrouillage temporel:** Si le destinataire ne révèle pas le secret dans un délai donné (hauteur du bloc), l'expéditeur initial peut récupérer les fonds.


Cette structure à double voie garantit la sécurité. Dans un échange entre couches, le même verrou de hachage est utilisé sur les deux réseaux. Lorsque le destinataire révèle le secret pour réclamer des fonds sur une couche (par exemple, Liquid), ce secret devient visible pour l'expéditeur, qui peut alors l'utiliser pour réclamer les fonds réciproques sur l'autre couche (par exemple, Lightning). Cette liaison cryptographique garantit que le swap se termine avec succès pour les deux parties ou échoue pour les deux, éliminant ainsi le risque qu'une partie perde des fonds alors que l'autre en gagne.


### La mise à niveau du Taproot et du MuSig2


Les anciens HTLC ([SegWit](https://planb.academy/resources/glossary/segwit) v0) fonctionnaient bien mais souffraient d'inconvénients en termes de confidentialité et d'efficacité. Ils nécessitaient la publication de l'ensemble de la logique du [script](https://planb.academy/resources/glossary/script) on-chain, ce qui rendait les transactions de swap facilement identifiables par les analystes de la blockchain et plus coûteuses en raison de la taille de leurs données. L'introduction de [Taproot](https://planb.academy/resources/glossary/taproot) (SegWit v1) et du protocole MuSig2 a révolutionné cette architecture.


Taproot permet l'agrégation de **clés** via MuSig2. Au lieu de révéler un script complexe avec plusieurs [clés publiques](https://planb.academy/resources/glossary/public-key), MuSig2 permet aux participants à l'échange de combiner leurs clés en une seule clé publique agrégée.


- Le "chemin de la clé" coopératif:** Si les deux parties acceptent l'échange (le "chemin heureux"), elles cosignent la transaction. Pour le réseau, cette transaction est identique à un paiement standard à signature unique. Elle consomme un espace de bloc minimal et ne révèle absolument aucune information sur les conditions de l'échange.
- Si l'une des parties ne répond plus ou devient malveillante, le script sous-jacent (contenant les verrous de hachage et de temps) n'est révélé qu'à ce moment-là. Celui-ci est organisé en [arbre de Merkle](https://planb.academy/resources/glossary/merkle-tree), ce qui permet à la partie honnête de ne dévoiler que la branche spécifique nécessaire au recouvrement des fonds, le reste de la logique du contrat restant caché.


### Mise en œuvre pratique : Liquid - Échanges de foudre


Dans la pratique, ces protocoles permettent un échange transparent entre les couches du Bitcoin. Un échange typique entre Liquid et Lightning commence par une demande d'échange de la part d'un client auprès d'un fournisseur de services. Le client fournit une [facture Lightning](https://planb.academy/resources/glossary/invoice-lightning) et le fournisseur verrouille l'équivalent Liquid Bitcoin (L-BTC) dans une adresse HTLC compatible Taproot.


L'atomicité est appliquée lorsque le paiement est réglé. Pour réclamer le L-BTC, le prestataire de services doit avoir la préimage. Il n'obtient cette préimage que lorsqu'il paie avec succès la facture Lightning du client. Dès que le paiement Lightning est finalisé, la préimage est révélée, ce qui permet au prestataire de débloquer les fonds Liquid.


#### Abstraction Wallet et gestion UTXO

Pour les utilisateurs finaux, cette complexité est entièrement abstraite. Les [portefeuilles](https://planb.academy/resources/glossary/wallet) modernes tels que Aqua gèrent la génération des clés, la création des factures et les processus de signature en arrière-plan. L'utilisateur "paie" simplement une facture Lightning en utilisant son solde Liquid. En coulisses, le service gère la consolidation [UTXO](https://planb.academy/resources/glossary/utxo), balayant périodiquement les petites sorties non réclamées ou remboursées pour maintenir l'efficacité wallet et minimiser l'impact des frais pendant les périodes de forte affluence.


## Liquid Network Vue d'ensemble


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Architecture et consensus


Le Liquid Network fonctionne comme une chaîne latérale fédérée construite sur la base de code **Elements**. Alors que Elements - un fork du Bitcoin Core - fournit la base logicielle, Liquid est l'implémentation du réseau de production. Contrairement à la Proof-of-Work de la Bitcoin, qui s'appuie sur la [mining](https://planb.academy/resources/glossary/mining) concurrentielle, la Liquid utilise un modèle de **consensus fédéré**.


Le réseau est entretenu par quinze "fonctionnaires" répartis dans le monde entier Ces entités exploitent des serveurs spécialisés qui jouent deux rôles essentiels :

1.  **Production de blocs:** Les fonctionnaires se relaient pour créer des blocs selon un programme déterministe de type round-robin, générant un nouveau bloc toutes les minutes.

2.  **Pour qu'un bloc soit valide, il doit être signé par au moins 11 des 15 fonctionnaires.


Ce seuil de 11 sur 15 garantit que le réseau peut tolérer la défaillance d'un maximum de quatre nœuds sans s'arrêter. Le principal avantage de ce compromis est la **finalité déterministe**. Alors que Bitcoin traite des probabilités, Liquid atteint la certitude de règlement après deux blocs (environ deux minutes). Une fois qu'un bloc a reçu une confirmation unique, la chaîne ne peut plus être réorganisée, ce qui la rend très efficace pour l'arbitrage et le règlement rapide.


### Confidential Transactions et les biens autochtones


La caractéristique principale du Liquid est l'utilisation par défaut du **Confidential Transactions (CT)**. Sur le Bitcoin mainchain, l'expéditeur, le destinataire et le montant sont publics. La Liquid améliore cette situation en masquant cryptographiquement le montant et le type d'actif, tout en laissant les adresses de l'expéditeur et du destinataire visibles à des fins de vérification.


Pour s'assurer qu'un utilisateur ne peut pas imprimer de l'argent (par exemple, en envoyant des montants négatifs), Liquid utilise les **Engagements de Pedersen** et les **Preuves d'étendue**. Ces primitives cryptographiques permettent au réseau de vérifier que *Intrants = Sorties + Frais* et que toutes les valeurs sont des nombres entiers positifs, sans jamais révéler les nombres spécifiques dans le registre public. Seuls les participants détenant les clés d'aveuglement peuvent voir les données décryptées.


#### Émission d'actifs

Liquid traite tous les actifs comme "natifs" Qu'il s'agisse du Liquid Bitcoin (L-BTC), d'un stablecoin comme l'USDT ou d'un titre token, ils partagent tous la même architecture. L'émission d'un actif ne nécessite pas de contrat intelligent, mais un simple appel RPC.


- Actifs non réglementés:** Peuvent être émis sans autorisation par n'importe qui.
- Actifs réglementés :** En utilisant la plateforme de gestion des actifs Blockstream (AMP), les émetteurs peuvent appliquer les règles de conformité (comme KYC/AML) en exigeant une deuxième signature d'un serveur d'autorisation avant qu'un actif ne puisse être déplacé.


### La cheville à double sens et la fédération dynamique


Le pont entre Bitcoin et Liquid est le **Two-Way Peg**. Il permet aux utilisateurs de déplacer des BTC vers la sidechain (Peg-in) et de revenir vers le mainchain (Peg-out).


**Le processus d'entrée en fonction:**

Il s'agit d'un système sans autorisation. Un utilisateur envoie des BTC à une adresse contrôlée par la fédération. Pour se protéger contre les réorganisations de la blockchain Bitcoin, ces fonds doivent attendre **102 confirmations** (environ 17 heures) avant que l'équivalent en L-BTC ne soit frappé sur la sidechain.


**Le processus de sortie de crise:**

Pour revenir au Bitcoin, le L-BTC est brûlé. Cependant, pour éviter le vol des réserves Bitcoin sous-jacentes, les peg-outs ne sont pas entièrement automatisés. Ils nécessitent l'autorisation d'un membre détenant une **clé d'autorisation de peg-out (PAK)**. Les fonds Bitcoin eux-mêmes sont sécurisés dans un wallet multi-signature de 11 sur 15, avec des clés détenues dans des modules de sécurité matériels (HSM) qui sont placés dans un air-gapped à partir des serveurs principaux des fonctionnaires.


**Fédération dynamique (Dynafed):**

Pour assurer sa longévité, Liquid utilise Dynafed, un protocole qui permet au réseau d'assurer la rotation des fonctionnaires ou de mettre à jour les paramètres sans qu'une fork soit nécessaire. Lorsqu'un fonctionnaire doit être remplacé, le réseau émet une transaction de transition. Après une période de chevauchement de deux semaines, la nouvelle configuration prend le relais, ce qui permet à la fédération d'évoluer de manière transparente tout en maintenant un temps de fonctionnement continu.


## Écosystème et marchés des capitaux


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network : Stratégie commerciale et écosystème


Liquid est plus qu'une sidechain technique ; il s'agit d'une couche d'infrastructure axée sur les affaires, conçue pour gérer les exigences complexes des marchés de capitaux que Bitcoin mainchain ne peut pas prendre en charge efficacement. Alors que la [Lightning Network](https://planb.academy/resources/glossary/lightning-network) est optimisée pour les paiements à haute fréquence et de faible valeur, la Liquid vise les transferts de grande valeur, l'émission d'actifs et le règlement interchange.


L'écosystème est piloté par la **Liquid Federation**, un consortium d'environ 73 entreprises comprenant des bourses, des bureaux de négociation et des fournisseurs d'infrastructure. Ce modèle de collaboration reflète les chambres de compensation financières traditionnelles, mais fonctionne avec une plus grande transparence et des délais de règlement considérablement réduits (2 minutes au lieu de T+2 jours).


### La tokenisation des actifs du monde réel (RWA)


Le principal argument commercial en faveur de Liquid est la "tokenisation", c'est-à-dire la représentation de la valeur du monde réel (actions, obligations, contrats mining) sous forme de jetons numériques sur la blockchain. Cela présente trois avantages principaux :

1.  **Marchés mondiaux 24 heures sur 24 et 7 jours sur 7 : suppression des heures d'ouverture des banques et des restrictions géographiques.

2.  **Efficacité opérationnelle:** Élimination des erreurs de réconciliation grâce à un grand livre partagé et immuable.

3.  **Règlement atomique:** Réduit le risque de contrepartie en garantissant que la livraison a lieu en même temps que le paiement.


#### Actifs réglementés et PGA

La plupart des actifs institutionnels ne peuvent pas être échangés sans permission en raison d'exigences légales. La **Plateforme de gestion des actifs (PGA)** est la norme technique qui permet de faire respecter ces règles.


- Liste blanche:** Les émetteurs peuvent limiter la détention et la négociation aux adresses vérifiées par KYC.
- Multisig Control:** Les actions de conformité (comme le gel des fonds volés ou la réémission des jetons perdus) sont gérées par le biais d'une autorisation multi-signature, ce qui garantit qu'aucun employé ne peut agir unilatéralement.


Cette infrastructure est opérationnelle dès aujourd'hui. Des plateformes comme **Stalker** fournissent des services de tokenisation de bout en bout en Europe, tandis que **Sideswap** agit en tant qu'échange décentralisé et wallet non dépositaire, permettant l'échange de pair à pair d'actifs tels que le **Blockstream Mining Note (BMN)** et les actions MicroStrategy tokenisées (CMSTR).


### Une réussite dans le monde réel : L'étude de cas Mayfell


La preuve la plus convaincante de l'utilité du Liquid nous vient de **Mayfell** au Mexique. Sur un marché où le financement traditionnel repose sur des billets à ordre en papier - qui sont sujets à la perte, à la fraude et à la lenteur du traitement - Mayfell a transféré l'ensemble de son infrastructure au Liquid.



- Plus de 25 000 billets à ordre ont été émis, représentant une valeur de plus de 1,5 milliard de dollars.
- Confidentialité:** En utilisant le Liquid's Confidential Transactions, les montants des prêts ne sont visibles que par le prêteur et l'emprunteur, ce qui préserve la confidentialité commerciale tout en permettant aux auditeurs de vérifier l'intégrité du grand livre.
- Impact:** En connectant les prêteurs non bancaires aux marchés de capitaux mondiaux via la blockchain, Mayfell a réduit les coûts et élargi l'accès au crédit pour les PME mexicaines, démontrant que la proposition de valeur de Liquid va bien au-delà du commerce spéculatif.


### Positionnement stratégique par rapport aux autres chaînes


Liquid est en concurrence sur un marché encombré de plateformes de tokenisation (Ethereum, Solana, etc.), mais elle possède des avantages stratégiques distincts :


- Clarté réglementaire:** Liquid utilise Bitcoin (L-BTC) comme actif natif. Elle n'a pas de token pré-miné ni d'ICO, évitant ainsi les risques de "titres non enregistrés" qui affectent d'autres blockchains L1.
- Stabilité:** Contrairement au modèle de compte d'Ethereum où les transactions ratées brûlent encore des frais de gaz, le modèle Liquid est déterministe et fiable pour les données financières critiques.
- Confidentialité:** La confidentialité par défaut est une exigence de la plupart des institutions financières, une fonction que Liquid offre de manière native et que les chaînes publiques peinent à mettre en œuvre sans ajouts complexes.


Pour les développeurs, cet écosystème offre une opportunité claire : créer les outils (tableaux de bord, portefeuilles, intégrations de conformité) qui font le lien entre la finance traditionnelle et la couche de règlement sécurisée de Bitcoin.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP : Contrôle des biens autorisés sur Liquid


Blockstream AMP (Asset Management Platform) sert de couche d'infrastructure critique sur le Liquid Network, conçu spécifiquement pour les émetteurs de titres numériques réglementés et de stablecoins. Alors que la Liquid fournit une couche de base sans permission avec l'émission d'actifs natifs, les entités réglementées ont souvent besoin d'une surveillance stricte et de capacités de conformité. AMP comble cette lacune en introduisant une couche de contrôle avec permission sur des actifs spécifiques sans sacrifier les avantages de confidentialité de la Confidential Transactions de la Liquid.


La proposition de valeur centrale de la plateforme repose sur deux capacités principales : la visibilité complète de l'émetteur et l'autorisation de la transaction. Contrairement aux actifs Liquid standard, dont les montants et les types sont blinded accessibles à tous sauf aux participants, les actifs AMP permettent à l'émetteur de maintenir une piste d'audit unblinded complète. Cette transparence est essentielle pour les rapports réglementaires et les audits internes. En outre, AMP applique un modèle d'autorisation strict par le biais d'un mécanisme de cosignature. Chaque transfert d'un actif AMP nécessite une signature du serveur AMP. Cela permet aux émetteurs d'appliquer des règles off-chain complexes, telles que le gel des comptes, l'inscription sur liste blanche des investisseurs accrédités ou l'imposition de limites de transfert, agissant ainsi comme un gardien centralisé au sein d'un réseau décentralisé.


#### Compromis opérationnels

Cette architecture introduit des compromis spécifiques. Le système repose sur la disponibilité du serveur AMP ; si le serveur joue le rôle de cosignataire et qu'il est hors ligne, la liquidité des actifs s'interrompt. En outre, bien que la confidentialité entre utilisateurs soit maintenue, les investisseurs doivent accepter que l'émetteur ait une visibilité totale sur leurs avoirs. Ce modèle est idéal pour les jetons de sécurité conformes, mais ne convient pas aux [crypto-monnaies](https://planb.academy/resources/glossary/cryptocurrency) résistantes à la censure.


### Évolution de l'architecture et voies d'intégration


L'écosystème AMP est actuellement en train de passer de sa première itération à une architecture "Version 2" plus flexible et interopérable. L'ancien système exigeait des émetteurs qu'ils maintiennent des nœuds Elements entièrement synchronisés et obligeait les développeurs à s'appuyer fortement sur le SDK monolithique Green. Bien que fonctionnel, ce système créait des barrières techniques élevées à l'entrée et limitait les choix en matière de wallet.


L'architecture de nouvelle génération simplifie fondamentalement ces exigences en déplaçant la complexité vers le serveur. Dans ce nouveau modèle, le serveur AMP se charge de la construction de la transaction, de la sélection de la UTXO et du calcul des frais. Il présente à l'émetteur une transaction Elements partiellement signée (PSET) qui nécessite simplement une signature. Cette approche "serveur intelligent, wallet muet" évite aux émetteurs d'avoir à exécuter des nœuds complets et permet d'utiliser des portefeuilles matériels et des configurations multi-signatures standard pour la gestion de la trésorerie.


Pour les développeurs, cette évolution signifie qu'il faut abandonner les SDK propriétaires au profit de descripteurs standard et de flux de travail PSET. Les portefeuilles peuvent désormais enregistrer des descripteurs multi-signatures auprès du serveur AMP afin d'établir des droits d'autorisation. Cela permet d'aligner le développement AMP sur les normes Bitcoin wallet plus larges, rendant l'intégration accessible à toute application capable de traiter les formats PSBT/PSET. Les développeurs qui construisent aujourd'hui sont encouragés à utiliser des outils tels que le kit Liquid Wallet (LWK), qui prend en charge ces architectures modernes basées sur des descripteurs, garantissant ainsi que leurs applications sont à l'épreuve du temps pour les nouvelles normes AMP.


### L'écosystème Liquid Wallet et la confidentialité


Construire des applications sur Liquid nécessite de naviguer dans une pile plus complexe que le développement Bitcoin standard en raison de caractéristiques telles que les actifs natifs et Confidential Transactions. L'écosystème est soutenu par une architecture en couches : des bibliothèques de bas niveau comme `secp256k1-zkp` gèrent les primitives cryptographiques, tandis que des boîtes à outils de plus haut niveau gèrent la logique wallet.


Historiquement, le kit de développement Green (GDK) fournissait une solution complète mais rigide. L'alternative moderne est le kit Liquid Wallet (LWK), qui offre une approche modulaire. Le LWK sépare les problèmes en plusieurs catégories distinctes - les descripteurs, la signature et la communication matérielle sont traités indépendamment - ce qui donne aux développeurs la souplesse nécessaire pour élaborer des solutions personnalisées sans avoir à supporter les frais généraux d'une bibliothèque monolithique.


#### Manipulation Confidential Transactions

Le défi le plus important dans cet écosystème est la gestion du cycle de vie de l'aveuglement. Dans Liquid, les résultats des transactions sont cryptés à l'aide d'un échange de clés ECDH (Elliptic Curve Diffie-Hellman). Un expéditeur utilise la clé publique d'aveuglement du destinataire pour chiffrer les montants et les types d'actifs, générant ainsi une preuve de portée qui vérifie la validité de la transaction sans révéler les valeurs.


Pour qu'une wallet fonctionne, elle doit réussir à inverser ce processus. Lorsqu'une wallet détecte une transaction entrante, elle tente de déverrouiller la sortie à l'aide de sa clé privée de déverrouillage. Si le secret partagé correspond, la wallet peut décrypter la valeur et l'ajouter au solde de l'utilisateur. Ce processus est intensif en termes de calcul et nécessite une gestion précise des facteurs d'aveuglement pour garantir que les transactions sont mathématiquement équilibrées, une complexité que des outils tels que LWK visent à abstraire pour le développeur.


# Technique


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Breez SDK - Sans objet


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Introduction au SDK Breez Liquid


Le SDK Breez Liquid est un kit d'outils open-source et autonome conçu pour combler le fossé entre le Liquid Network et l'écosystème plus large du Bitcoin. Sa mission première est d'abstraire les complexités de la gestion des nœuds Lightning Network et des swaps atomiques, permettant aux développeurs de créer des applications financières sans friction.


Construite avec une philosophie "mobile-first", la logique de base est écrite en Rust pour la performance et la sécurité, mais elle utilise UniFFI (Unified Foreign Function Interface) pour fournir des liaisons natives pour Kotlin, Swift, Python, C#, Dart, et Flutter. Cela garantit que les développeurs peuvent intégrer la fonctionnalité Bitcoin dans leur environnement préféré sans avoir à gérer des opérations cryptographiques de bas niveau.


**Types de transactions pris en charge:**

Le SDK fonctionne avec Liquid comme "base" Il excelle dans trois opérations spécifiques :

1.  **Liquid-to-Liquid:** Transferts directs on-chain.

2.  **Liquid-to-Lightning:** Paiement des factures Lightning à l'aide des fonds Liquid.

3.  **Liquid-to-Bitcoin:** Transfert de fonds directement vers le Bitcoin mainchain.


*Remarque : le SDK ne prend pas en charge les transactions directes de Lightning à Lightning ou de Bitcoin à Bitcoin. Il s'agit d'un outil strictement centré sur le Liquid


### Architectures de paiement : Swaps sous-marins


Pour assurer l'interopérabilité entre Liquid, Lightning et Bitcoin sans dépositaires centralisés, Breez s'appuie sur les **Submarine Swaps**. Il s'agit d'opérations atomiques au cours desquelles une transaction se termine avec succès sur les deux réseaux ou échoue sur les deux, ce qui garantit que les fonds ne sont jamais perdus en cours de route.


#### Envoi d'éclairs (échange de sous-marins)

Lorsqu'un utilisateur paie une facture Lightning, le SDK diffuse une transaction de "blocage" sur le Liquid Network. Cette transaction met effectivement les fonds sous séquestre. Le fournisseur de swap (Boltz) le détecte, paie la facture Lightning, puis utilise la préimage de paiement (le reçu cryptographique) pour réclamer les fonds bloqués de la Liquid.


#### Réception de la foudre (échange inversé de sous-marins)

La réception du Lightning est le processus inverse. L'utilisateur génère une facture et le fournisseur de swap bloque les fonds sur le Lightning Network. Le SDK surveille ce processus par l'intermédiaire de WebSockets. Une fois le blocage confirmé, le SDK exécute automatiquement une transaction de réclamation pour transférer les fonds équivalents dans la Liquid wallet de l'utilisateur.


#### Chaîne croisée Bitcoin

Pour les transferts Liquid vers Bitcoin, l'architecture utilise un mécanisme de "double permutation". Les transactions de blocage ont lieu simultanément sur les deux chaînes. L'expéditeur réclame des fonds sur la Bitcoin, tandis que le destinataire réclame des fonds sur la Liquid. Cela permet un rapprochement sans confiance sans dépendre des federated peg-outs ou des échanges centralisés.


### Développeur Interface et gestion automatisée


Le SDK Breez simplifie l'expérience du développeur en condensant les flux financiers complexes en un processus normalisé en trois étapes : **Connecter, Préparer et Exécuter**.


1.  **Connect:** Initialise le wallet, se synchronise avec la blockchain en utilisant le kit Liquid Wallet (LWK), et établit des connexions WebSocket pour la surveillance en temps réel.

2.  **Prepare:** Avant d'engager des fonds, cette étape calcule et renvoie tous les frais de réseau et de swap associés, ce qui permet à l'interface utilisateur de présenter un total clair à l'utilisateur.

3.  **Cette étape consiste à construire la transaction, à la diffuser et à initier l'échange.


#### Mécanismes de sécurité automatisés

L'une des fonctions les plus importantes du SDK est la **gestion automatisée des remboursements**. En cas de défaillance du réseau ou d'une contrepartie non coopérative, les fonds peuvent théoriquement rester bloqués dans un contrat à durée déterminée. Le SDK fait abstraction de la logique de récupération. Il surveille l'état de chaque swap ; si un swap échoue ou se termine, le SDK construit et diffuse automatiquement la transaction de remboursement pour renvoyer les fonds vers la wallet de l'utilisateur.


En outre, le SDK gère la **résolution des métadonnées**. Il fusionne les données d'échange off-chain (fournies par l'échangeur Boltz) avec l'historique des transactions on-chain. Cela garantit que l'historique des transactions de l'utilisateur est lisible par l'homme, affichant les détails de la facture et le contexte du paiement plutôt que de simples hachages hexadécimaux bruts des transactions.


# Section finale


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Critiques et évaluations


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Examen final


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusion


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>