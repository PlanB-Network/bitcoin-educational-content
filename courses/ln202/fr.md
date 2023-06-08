---
name: Mise en place d’un nœud Bitcoin & Lightning
goal: Déployer un noeud Bitcoin et Lightning via Umbrel
objectives:
  - Installer un nœud Bitcoin
  - Gérer un nœud Bitcoin
  - Utiliser un nœud Lightning Network
---

# Un voyage vers le côté technique de Bitcoin

:[affiche du cours](Formation\courses\btc101\assets\affiche\BTC101_vignette-presentation-front.png)

Cette formation s'avère être plus technique et vous sera d'autant plus bénéfique si vous avez des bases sur Bitcoin, notamment la compréhension du fonctionnement des portefeuilles Bitcoin et le principe de transaction, de minage et de blockchain. Pas besoin de savoir coder, votre curiosité et votre volonté d'apprendre sont les seules compétences nécessaires. Rappelez-vous, chaque expert était autrefois un débutant. Alors, prenez une grande respiration, et sautez dans l'univers passionnant de Bitcoin. Vous êtes sur le point de débuter un voyage passionnant et enrichissant. Bon courage !

+++

# Devenir un Bitcoiner souverain

![Lancement de la formation](https://youtu.be/NF3SHhE1PFw?list=PLinTFKehfR4zoKvBcncHPr-ZTh1enuEhr)

Afin de prendre pleinement part à la philosophie du Bitcoin et d'incarner l'adage "Don't Trust, Verify", nous visons à devenir des utilisateurs souverains des nœuds Bitcoin. Dans cette démarche, nous allons nous appuyer sur l'interface de Umbrel pour mettre en place notre propre nœud. Les outils nécessaires à cette tâche incluent un Raspberry Pi, un disque dur externe, une carte SD, un ventilateur et une caisse, pour un investissement total estimé à environ 200€.

En adoptant Umbrel comme notre base opérationnelle, nous allons pouvoir intégrer le Lightning Network, explorer la mempool et découvrir des solutions de multisig. À l'issue de ce voyage, non seulement nous nous serons affirmés en tant que Bitcoiners souverains, mais nous aurons aussi la satisfaction d'avoir contribué activement au réseau Bitcoin.

# Qu’est-ce qu’un nœud Bitcoin ?

![qu'est ce qu'un noeud?](https://youtu.be/19YgL9vkHh4)

Un nœud Bitcoin est simplement un appareil faisant tourner le logiciel Bitcoin, la pierre angulaire de l'existence et de la communication du réseau. Ces nœuds constituent la fondation de la décentralisation de Bitcoin, en adoptant différentes formes et en assurant diverses responsabilités. Parmi elles, on compte la réception et la transmission des transactions, l'affichage des transactions sortantes et l'établissement de connexions avec d'autres nœuds.

Trois principaux rôles sont assignés à ces nœuds : établir le consensus Bitcoin, valider les transactions et interagir avec le réseau. Grâce à cette décentralisation, Bitcoin bénéficie d'une résilience accrue, avec une vie privée renforcée par le fait de ne pas dépendre d'un serveur tiers. Selon [Bitnodes](https://bitnodes.io/nodes/all/), environ 43 000 nœuds à travers le monde forment le réseau Bitcoin.

Explorons maintenant les fonctions spécifiques de ces nœuds au sein du réseau Bitcoin. Un nœud n'est pas seulement un logiciel ; c'est également une passerelle vers le consensus du réseau Bitcoin et l'accès à l'historique de la blockchain. Par exemple, les commerçants exploitent leur propre nœud pour valider les transactions entrantes et sortantes.

L'avantage de gérer son propre nœud réside dans l'amélioration de la vie privée et la réalisation de la souveraineté financière. En effet, exécuter son propre nœud renforce votre contribution au réseau et fait de vous votre propre banque. Cela vous permet de vérifier les transactions en temps réel, vous offrant une meilleure prise de décision sur vos finances.

En conclusion, faire fonctionner son propre nœud dans le réseau Bitcoin offre de nombreux avantages. Non seulement cela contribue à la décentralisation du réseau, renforçant ainsi la résilience du système, mais cela assure également une plus grande confidentialité et autonomie financière. En effectuant cette démarche, vous pourrez authentifier les transactions en temps réel, prendre des décisions financières éclairées et éviter la dépendance à un serveur tiers, garantissant ainsi votre vie privée. Au-delà de tout cela, exécuter son propre nœud est un moyen concret de contribuer à l'écosystème Bitcoin et d'incarner véritablement le rôle de sa propre banque.

# Tutoriel nœud Bitcoin via Umbrel

![Tuto umbrel](https://youtu.be/mr4iTzdTczI)

Au cours de ce chapitre, nous allons déployer nous-même un nœud Bitcoin, ouvrir des canaux lightning et essayer un portefeuille multi-signature.
Ceci a un coût matériel non négligeable pour certaines personnes. Sachez que la totalité de la formation peut être suivie SANS le matériel. Vous ne serez pas perdu si vous n’avez pas votre propre nœud.
Si vous avez envie de vous lancer, voici les produits (lien affiliation) :

- Carte SD 16Go – https://amzn.to/3Qi2Opm
- Raspberry Pi 4 – https://amzn.to/3qoSUYl
- SSD 1To – https://amzn.to/3jSvjLC​
- Boîtier Externe pour Disque Dur – https://amzn.to/3x5R02S
- RASPBERRY Alimentation – https://amzn.to/3D36zvM
- Raspberry Pi FLIRC Case – https://amzn.to/3TNllgi

Si vous êtes passé(e) par les liens d’affiliations, merci de votre soutien ! Vous permettez à ce projet de survivre et proposer toujours plus de formations et de contenus éducationnels.

Que faut-il pour faire tourner son nœud Bitcoin ?

- La blockchain est d’environ 500GB, il faut donc prévoir de l’espace
- La connexion internet doit être constante avec environ 5Gb de bande passante par mois
- Il faut de la RAM pour faire tourner BTC Core
- Il faut plus de RAM si l’on fait tourner Umbrel et un nœud LN (minimum 4 Go)

Vous pouvez donc faire tourner votre nœud Bitcoin directement sur votre ordinateur ou utiliser un système comme sur la vidéo avec un Raspberry Pi.

D’autres [solutions](https://thebitcoinmanual.com/behind-btc/nodes/buy-node/) déjà toute faite existent !

Suivez ces étapes pour créer un full node avec un Raspberry Pi et Umbrel. Avant de commencer, veuillez noter que vous aurez besoin d'environ 200 euros pour l'achat du matériel nécessaire, bien que le logiciel soit gratuit.

1. **Préparation des outils**: Rendez-vous sur [Umbrel](https://umbrel.com/), une solution open source réputée pour son excellente interface utilisateur et son bon service, pour télécharger le logiciel nécessaire. De plus, vous aurez besoin de Benella Itcher pour flasher la carte SD.
2. **Montage du Raspberry Pi**: Assemblez votre Raspberry Pi. Assurez-vous d'installer le ventilateur et les petits composants de refroidissement inclus dans le kit.
3. **Flashing de la carte SD**: Utilisez l'appareil fourni dans le kit pour flasher la carte SD. Si vous rencontrez des difficultés, essayez de reformater la carte ou de débrancher/rebrancher l'appareil.
4. **Connexion du matériel**: Une fois que la carte SD est flashée, connectez le SSD au Raspberry Pi via un port 3.0. Ensuite, connectez le Raspberry Pi à votre routeur et à une source d'alimentation électrique.
5. **Configuration d'Umbrel**: Après environ 5 minutes, vous pourrez accéder à l'interface d'Umbrel sur votre ordinateur. Il est recommandé d'utiliser un gestionnaire de mots de passe pour créer et enregistrer un mot de passe sécurisé pour l'accès à votre nœud Umbrel.
6. **Sécurisation de votre seed (phrase mnémonique)**: Votre seed est la clé privée qui vous donne accès à vos bitcoins. Veillez donc à la conserver en lieu sûr. Évitez de prendre des photos ou des captures d'écran de votre seed. Il est également recommandé d'enregistrer le lien TOR dans votre gestionnaire de mots de passe pour un accès facile ultérieur.
7. **Exploration du tableau de bord Umbrel**: Umbrel dispose d'un tableau de bord clair et d'un App Store innovant pour télécharger d'autres applications. Le tutoriel Umbrel est accessible à tous, il vous suffit d'acheter le matériel et de suivre les étapes.
8. **Prendre conscience de l'importance des nœuds**: Les nœuds sont essentiels pour transformer le système bancaire et remplacer les banques centrales. Avec votre propre nœud, vous partcipez à la vérification des transactions Bitcoin et du respect des règles du protocole. En faisant fonctionner votre propre nœud, vous n'avez plus besoin de faire confiance à un tiers de confiance, et pouvez vérifier les transactions vous-même. Les nœuds sont un pilier essentiel de votre souveraineté financière.

En suivant ces étapes, vous pourrez contribuer à la décentralisation du réseau Bitcoin, augmenter votre vie privée et autonomie financière et participer activement à l'évolution du système bancaire traditionnel. Alors, n'hésitez pas à vous lancer et à devenir un véritable Bitcoiner souverain.

# Overview de Umbrel

![umbrel overview](https://youtu.be/cwEa61BgemM)

Nous nous apprêtons à examiner de manière exhaustive cette interface qui facilite la gestion de votre portefeuille Bitcoin et Lightning Network.

Pour commencer, nous allons nous identifier sur le compte en utilisant un mot de passe sécurisé et un gestionnaire de mot de passe dédié. Puis, nous entreprendrons une exploration approfondie de l'interface, en nous familiarisant avec les caractéristiques distinctives du portefeuille Bitcoin et du Lightning Network.

Le nœud communiquera avec d'autres nœuds sur le réseau pair-à-pair de Bitcoin de façon aléatoire et sous pseudonyme. Cette caractéristique essentielle permet de télécharger l'intégralité de la blockchain (également appelée timechain) sans avoir à dépendre d'une entité centrale. Il faut cependant prendre en compte que le téléchargement initial de la timechain peut durer plusieurs jours, étant donné qu'il représente un volume de plus de 500 Go à réceptionner.

Nous entreprendrons ensuite des transactions au sein du portefeuille Bitcoin, y compris un transfert test vers un portefeuille multisig. Par la suite, nous nous attellerons à ouvrir des canaux Lightning Network et à utiliser des connexions actives dans le portefeuille Lightning Network. L'ouverture de canaux nécessite une certaine exploration visuelle.

Après avoir réalisé ces opérations, Bitcoin Core devient opérationnel. Vous êtes alors en mesure de connecter certains de vos portefeuilles à votre nœud pour vérifier l'état de vos comptes.

Il est envisageable de lier vos portefeuilles Bitcoin tels que [Green Wallet](https://blockstream.com/green/), [Samouraï](https://samouraiwallet.com/), [Spectre](https://specter.solutions/), [Sparrow](https://sparrowwallet.com/) à votre nœud Bitcoin via une interface dédiée. En connectant votre portefeuille à votre propre nœud, vous pouvez confirmer la réception des fonds sans avoir à faire confiance à un serveur externe, ce qui est particulièrement recommandé pour les commerçants.

Umbrel propose également un App Store regroupant des Explorers, de multiples autres services liés à Bitcoin, Lightning ou l'hébergement de vos propres données. De nouvelles applications sont régulièrement ajoutées à leur [appstore](https://apps.umbrel.com/).

Pour obtenir plus d'informations et de support, n'hésitez pas à consulter leur site internet, le chat Telegram, le Discord, le Github et le Reddit. En résumé, grâce à Umbrel, vous avez la possibilité de reprendre le contrôle de votre souveraineté financière grâce à Bitcoin, et devenir votre propre banque tout en contribuant au réseau. Nous vous encourageons vivement à approfondir et à apprendre cette technologie pour l'intégrer dans votre magasin, e-commerce, vie personnelle ou tout simplement par curiosité.

# Analyse de la MemPool

![mempool](https://youtu.be/0xS859IoMh8)

La Mempool, intrinsèquement, fonctionne comme un espace de transit pour les transactions Bitcoin qui attendent d'être validées dans la blockchain. Pour examiner la Mempool de manière efficace, Umbrel sert d'outil de choix. L'application [Mempool.space](https://mempool.space/), accessible via l'interface d'Umbrel, fournit une représentation claire des transactions en attente, des coûts associés et de diverses autres fonctionnalités pertinentes.

La blockchain Bitcoin est essentiellement une base de données qui incorpore des blocs de transactions à intervalles réguliers d'environ 10 minutes. Après chaque série de 2016 blocs, la difficulté de minage s'ajuste pour maintenir cet intervalle moyen. Si les mineurs décident de retirer leur énergie du réseau Bitcoin, le temps moyen nécessaire pour trouver de nouveaux blocs augmente, entraînant une baisse de la difficulté de minage et permettant à d'autres mineurs de redevenir compétitifs.

En plus de la difficulté de minage, le coût actuel d'une transaction Bitcoin est visible sur le tableau de bord, ainsi que la blockchain avec sa chaîne de blocs. Les frais pour une transaction Bitcoin sont actuellement de 40 sats/vbytes. Les frais de transaction sur Bitcoin sont basés sur la complexité de la transaction, qui est considérée proportionnelle au poids virtuel (le vbytes) de la transaction. Les vbytes, ou bytes virtuels, sont une unité de mesure utilisée dans Bitcoin pour évaluer la taille d'une transaction en tenant compte de la technologie SegWit. Ainsi, l'utilisation des vbytes permet une mesure plus précise de l'efficacité de l'espace dans un bloc.

Chaque utilisateur est libre de déterminer les frais associés à sa transaction, qui ont tendance à refléter l'urgence de la validation de la transaction : plus l'utilisateur souhaite que sa transaction soit validée rapidement, plus les frais augmentent. Ainsi, comme le volume d'un bloc est limité à 4 Mo (bien que la taille moyenne des blocs soit d'environ 1,5 Mo), lorsque la demande augmente, les frais pour augmenter la probabilité que notre transaction soit incluse dans le prochain bloc peuvent augmenter de manière significative.

Bitcoin comporte plusieurs couches : le Mainnet (la chaîne principale), le Testnet et le Signet (des chaînes dédiées à l'expérimentation et à la validation de nouvelles fonctionnalités), le Lightning Network (un réseau de paiement) et Liquid (une sidechain où les blocs sont validés toutes les minutes). Chacune de ces couches a sa propre utilité et ses cas d'usage spécifiques.

Les blocs qui contiennent les transactions sont construits par les pools de minage, et leur niveau de remplissage varie en fonction de la demande et du temps écoulé depuis le minage du dernier bloc. Des couches supérieures, comme le Lightning Network, permettent des transactions plus rapides et moins coûteuses que sur la blockchain principale, mais elles reposent toujours sur Bitcoin pour leur modèle de sécurité.

En conclusion, les explorateurs de blocs permettent de suivre les transactions en temps réel ou de les retracer dans le passé. Ces transactions peuvent présenter des niveaux de complexité variables. Mempool offre une solution efficace pour visualiser la blockchain, suivre les transactions et analyser les frais ainsi que la congestion du réseau.

# Block Explorer & Analyse Stats

![block explorer et analyse stat](https://youtu.be/Qe9VaUhUS0E)

Nous allons entamer un voyage d'exploration à travers la blockchain Bitcoin, en utilisant des outils puissants tels que les Block Explorers et l'application BTC Explorer sur le nœud Umbrel. Les Block Explorers nous donnent la capacité d'analyser en détail la blockchain Bitcoin. Avec BTC Explorer, une application sur Umbrel, vous pouvez vérifier toutes les informations relatives à la blockchain Bitcoin qui se trouve dans votre disque dur, ce qui vous permet de ne plus dépendre de la confiance d'un tiers.

Nous nous référons à une transaction spécifique, la même que celle examinée dans le cours précédent, pour démontrer les fonctionnalités et l'importance de ces outils. Nous illustrerons également les derniers blocs minés et détaillerons les informations sur leur contenu. Puis, nous ferons une comparaison approfondie entre deux blocs distincts, en analysant leur contenu et le temps qu'il a fallu pour les miner.

Le Block Explorer nous permet de visualiser les détails d'un bloc miné, tels que le hash, le sommaire, les outputs, les frais, le temps et les transactions. Quant à Bitcoin Explorer, il offre des outils plus sophistiqués pour l'analyse de la blockchain. Le premier outil permet par exemple d'examiner en détail son nœud (synchronisation, index, taille de la blockchain, BIP acceptés).

Les Bitcoin Improvement Proposals (BIP) sont des propositions d'amélioration du protocole Bitcoin. Nous pouvons observer l'activation de Segwit et le nombre de connexions réseau. De plus, les Blockstats fournissent des statistiques détaillées sur les frais, les transactions, les inputs et outputs.

L'analyse des données de Segwit offre une vue d'ensemble de l'évolution de Bitcoin au fil des années. Les statistiques des transactions, des volumes, des blocs, des UTXO et des timestamps sont disponibles gratuitement. L'interprétation de ces données est cruciale pour la recherche financière et pour vérifier l'adoption de Bitcoin.

Il est important de prendre en main sa souveraineté financière et d'aller chercher soi-même les données. L'analyse de blocs permet d'étudier les données d'un bloc spécifique, comme le premier bloc miné par Satoshi en 2009, où il a détruit volontairement ses 50 premiers bitcoins pour un lancement honnête.

Les données des transactions Bitcoin sont transparentes et consultables par tous, y compris les analystes et les professionnels du secteur. Ces informations sont vitales car elles fournissent des indications précieuses sur l'activité du réseau Bitcoin, la dynamique du marché et les tendances en cours, ce qui est essentiel pour une prise de décision éclairée et la mise en place de stratégies financières solides. De plus, ces données sont utilisées pour le suivi des transactions, permettant ainsi de garantir la traçabilité et la transparence du réseau Bitcoin.

Une transaction Bitcoin dite "lourde", comme par exemple une qui contient 673 inputs et 1 output, illustre le compromis entre le nombre d'UTXO (Unspent Transaction Outputs) et la quantité de Bitcoin dans une adresse. Les UTXO représentent les fonds non dépensés d'une transaction précédente, qui deviennent les inputs des transactions futures. L'augmentation du nombre d'UTXO dans une transaction la rend plus complexe et coûteuse. Par conséquent, il est essentiel de regrouper les UTXO pour minimiser les frais de transaction et optimiser l'utilisation de l'espace dans un bloc de la blockchain Bitcoin.

Le minage, pivot central du protocole Bitcoin, joue un rôle fondamental en sécurisant les transactions. Le processus est régulé par un ajustement de la difficulté tous les 2016 blocs pour conserver un intervalle moyen de 10 minutes entre les blocs. Parallèlement, le taux de hash, reflet de la puissance de calcul du réseau, est en augmentation constante.

Au sein du réseau, les mineurs se regroupend au sein de pools de minage. Ces entités n'ont pas le pouvoir de contrôler l'ensemble du réseau car les mineurs ont le privilège de pouvoir basculer entre les pools à leur convenance. Des technologies innovantes comme Stratum V2 donnent plus de pouvoir aux mineurs au sein des pools de minage. Par ailleurs, des solutions techniques telles que MimbleWimble et Dandelion se présentent comme des améliorations prometteuses pour les transactions.

Par ailleurs, la richesse historique de la blockchain réside dans le fait qu'elle archive toutes les transactions, depuis le bloc génésis jusqu'aux transactions les plus récentes. Elle comprend la première transaction Bitcoin effectuée par Satoshi à Hal Finney au bloc 170 et la fameuse transaction de 10 000 bitcoins contre deux pizzas au bloc 57043, événement à l'origine de la célébration annuelle du "Pizza Day" le 22 mai.

Pour renforcer votre souveraineté financière et éviter la dépendance à un tiers pour la réception et l'envoi de vos bitcoins, il est crucial de connecter vos portefeuilles à votre propre nœud Bitcoin. Les transactions sont d'abord validées par les nœuds du réseau lors de leur propagation, puis une seconde fois lorsqu'elles sont incorporées dans un bloc.
Pour conclure, partager et initier son entourage à Bitcoin est une démarche louable. En exploitant votre propre nœud et en contribuant au réseau, vous pouvez devenir votre propre banque. L'objectif ultime étant de devenir pleinement autonome.

# Connecter son portefeuille à son nœud

![connecter son portefeuille à son nœud](https://youtu.be/HOV3bVcram4)

Dans le monde numérique d'aujourd'hui, protéger ses crypto-monnaies et sa vie privée est primordial. C'est dans ce contexte que je vais vous guider dans la connexion de vos portefeuilles mobiles et de bureau à notre nœud Bitcoin. Cette procédure accroit significativement votre sécurité tout en augmentant votre contrôle sur vos actifs.

Il existe une multitude de portefeuilles disponibles : Bitbox App, Blue Wallet, Blockstream Green, Samouraï, Phoenix, Sparrow, Wasabi, Electrum et bien d'autres. Chacun possède ses spécificités, ses forces et ses faiblesses. Pour aujourd'hui, notre focus se portera sur Sparrow, une alternative intéressante à Ledger Live, réputée pour sa facilité de gestion et de création de portefeuilles.

En matière de sécurité et de confidentialité, une étape supplémentaire peut être franchie : l'utilisation d'un serveur privé plutôt qu'un serveur public. Cette démarche, bien que plus complexe, assure un niveau supérieur de contrôle et de protection. Vous trouverez les informations nécessaires à la connexion à un serveur privé sur Umbrel.

Rappelez-vous, maintenir vos portefeuilles à jour est un geste essentiel. Les mises à jour corrigent les bugs, combattent les vulnérabilités, améliorent le produit et ajoutent parfois de nouvelles fonctionnalités utiles. Umbrel, en particulier, assure la mise à jour automatique de toutes ses applications. Il est donc judicieux de garder votre Umbrel actualisé.

Pour conclure, connecter vos portefeuilles directement à notre nœud Bitcoin est une étape vers l'indépendance financière. Cela vous confère un niveau de confidentialité et de sécurité supérieur tout en vous permettant de garder un contrôle total sur vos actifs numériques. La souveraineté financière signifie avoir la pleine possession et le contrôle de son argent, sans intermédiaire. En diversifiant vos portefeuilles et en les maintenant à jour, vous faites un pas de plus vers cette autonomie.

# Les Portefeuilles multi-sig via Specter

![les portefeuille multi sig](https://youtu.be/mV1KS-Uwjew)

Nous vous proposons de franchir une nouvelle étape sur la voie de l'autonomie financière. Notre objectif : la mise en place d'un portefeuille multisig avec l'application Spectre, intégrée à Umbrel. Nous connecterons l'application Desktop à notre nœud, rendant ce tutoriel accessible à tous.

Le concept du multisig est simple : garantir un niveau de sécurité exceptionnel pour les montants importants. Pour cela, nous allons utiliser trois clés privées pour sécuriser notre nouveau portefeuille Bitcoin. Plusieurs niveaux de sécurité existent : portefeuille mobile, portefeuille physique, passphrase, multisig 2 sur 3, multisig 3 sur 5, ou même une combinaison de tous ces éléments avec open dimes. Pas besoin d'être un expert en technologie pour suivre ce tutoriel, mais une certaine familiarité avec le système de clés privées et publiques est requise.

Préparez-vous, car le tutoriel est rapide. Les appareils ayant déjà été initialisés, il devrait nous prendre environ 15 minutes. Pour suivre, vous aurez besoin de trois appareils initialisés, d'un nœud pour connecter l'application Spectre, ainsi qu'une clé USB et une imprimante. Nous utiliserons l'application Spectre pour notre solution multisig. Vous pouvez la télécharger via Umbrel ou directement depuis le site internet de Spectre Solutions. N'oubliez pas de vérifier la signature avant le téléchargement. Vous pouvez également faire votre multisig avec Sparrow ou Electrum. N'hésitez pas à faire vos recherches et à prendre le temps de vous familiariser avec ces outils avant de les utiliser pour gérer des montants importants.

Passons maintenant à la pratique. Ici, nous avons réalisons un 2 sur 3 avec une ledger et 2 trezor (blanc et noir) et Spectre Desktop qui est l'interface de portefeuille nous permettant d'interagir avec nos portefeuilles, et qui est connectée à Bitcoin Core via Umbrel.

Nous créerons d'abord un portefeuille simple pour interagir avec Ledger sans Ledger Live. Cela nous permettra de générer de nouvelles adresses et d'envoyer des Bitcoins. Nous ajouterons ensuite d'autres appareils (des trésors) pour créer le multisig. Commençons par choisir le deuxième appareil (le Trésor blanc) que nous connecterons via USB. Après avoir utilisé le PIN pour l'activer, nous extrairons les clés publiques et créerons un second portefeuille. Nous ajouterons ensuite un troisième appareil (le Trezor Noir) et l'utiliserons pour créer un portefeuille multisig. Nous créerons un portefeuille multisig en choisissant les trois appareils, en utilisant Signet pour tester et ne pas perdre de fond en cas de mauvaise manip (cependant la démarche et la même pour le mainnet)

Nous créerons ensuite le portefeuille en combinant les clés publiques. La sauvegarde d'un portefeuille multisig contient plusieurs éléments. En effet pour recréer le portefeuille nous aurons besoin des trois clés publiques et de deux clés privées pour dépenser l'argent. Il est donc crucial de stocker les clés publiques avec le backup de chacune des clés privées dans un endroit sûr.
Il est recommandé d'inscrire sur du papier ou sur du métal les phrases mnémoniques (liste de 24 mots) des 3 clés privées en plusieurs exemplaire (au moins 2). De plus, il est conseillé d'écrire des informations précises et détaillées qui permettent de récupérer votre argent en cas de problème ou pour un plan d'héritage. Ces instructions devont également stockées dans un endroit sûr.

Ainsi, vous aurez franchi un pas de plus sur le chemin de la souveraineté Bitcoin. En maîtrisant votre sécurité et en utilisant des outils tels que le multisig, vous renforcez votre autonomie financière et protégez vos actifs de manière optimale. N'oubliez pas, la prudence et l'apprentissage continus sont les clés de la réussite dans le monde de Bitcoin.
Si vous souhaitez vous entraîner avec des bitcoins du Testnet, vous pouvez vous en procurer via ce [faucet](https://bitcoinfaucet.uo1.net/).

# Ouverture de canaux Lightning

![ouverture de canaux](https://youtu.be/bAZJn0AH1yU)

Abordons maintenant la partie Lightning du nœud Umbrel. Nous allons utiliser ThunderHub, une application parmi plusieurs qui servent de gestionnaire de nœud Lightning, telles que Lightning Terminal et RideTheLightning (RTL). Ces applications nous donnent un aperçu précis de l'état de nos canaux, en nous servant d'interface entre nous et nos canaux Lightning Network (LN).

À ce stade, notre objectif principal est l'ouverture d'un nouveau canal. Lorsque vous téléchargez ThunderHub, un mot de passe par défaut est fourni, que vous pouvez trouver directement dans l'appstore. Il est essentiel de le changer et de conserver précieusement ce nouveau mot de passe dans un gestionnaire de mots de passe dédié.

Lorsque vous envisagez d'ouvrir un canal avec un autre nœud Lightning du réseau, certaines questions se posent. Par exemple, quelle quantité de liquidités souhaitez-vous allouer dans un canal? Avec quelles parties voulez-vous ouvrir un canal? Les réponses à ces questions sont cruciales pour optimiser vos transactions et pour éviter de potentiels problèmes.

Parlons de la taille des canaux. Il ne serait pas judicieux de commencer par ouvrir des canaux avec un montant faible, comme 20k, 50k ou 100k sats. Ce serait insuffisant et les frais d'ouverture et de fermeture du canal ne seraient pas couverts. Un canal de faible montant serait plus nuisible qu'utile pour vous et pour le reste du réseau. Par exemple, si vous avez un canal de 20k ouvert avec mon nœud, cela couvrirait à peine les frais d'ouverture et de fermeture (+ réserve). Il ne vous resterait que des miettes à dépenser.

C'est pourquoi il est conseillé d'ouvrir des canaux d'au moins 500k-1M sats. Cela offrirait un meilleur routage, bénéfique pour vous et pour tous les autres qui routeraient des transactions à travers votre nœud. Il est important de noter que l'idée de "plus c'est gros, mieux c'est" ne s'applique pas ici. Il serait préférable de disposer de 5 à 6 canaux sortants, chacun contenant entre 500k et 1M sats, et, selon vos besoins, de 4 à 5 canaux entrants d'une capacité similaire.

Maintenant que vous êtes familiarisé avec la taille des canaux, passons à leur gestion. En ce qui concerne la liquidité sortante (de votre côté), votre nœud LN vous permet de faire des paiements LN, d'acheter des choses, d'envoyer de l'argent à des amis, de payer des services, etc. Essayez d'ouvrir des canaux LN avec les marchands avec lesquels vous comptez échanger. En ce qui concerne la liquidité entrante (du côté de vos pairs), trouvez des pairs prêts à ouvrir des canaux vers votre nœud. Cette liquidité entrante est nécessaire pour recevoir des paiements sur le LN.

La question de savoir avec qui ouvrir des canaux est primordiale. Premièrement, avec les marchands chez qui vous comptez effectuer des transactions, vous pourrez profiter d'un routage direct et éviter les frais. Deuxièmement, pensez aux amis et aux utilisateurs expérimentés du LN que vous connaissez et qui peuvent créer un anneau de nœuds (ring of fire) avec une certaine quantité de sats pour ces canaux. Ceci est parfait pour équilibrer la liquidité tout en réduisant les frais entre les nœuds de l'anneau. Troisièmement, votre anneau de nœuds peut avoir des connexions ou des canaux "externes" avec d'autres bons nœuds, ce qui facilite et accélère le routage vers n'importe quel destinataire.

Pour établir ces connexions, vous devrez récupérer les adresses publiques des autres parties. Vous pouvez le faire en leur demandant directement ou via des sites comme [1ML](https://1ml.com/) ou [Amboss](https://amboss.space/). L'ouverture d'un canal implique des frais de transaction en chaîne, donc profitez des moments où la Mempool est vide pour ouvrir des canaux. Une fois un canal ouvert, la liquidité est bloquée d'un côté du canal. Pour la déplacer de l'autre côté, il faut effectuer des transactions pour des paiements, ou effectuer ce qu'on appelle un "submarine swap" (nous verrons cela dans la prochaine partie). Il est à noter que dans le Lightning Network, il y a des frais de routage. Si un canal se vide trop vite, à cause du routage, vous pouvez augmenter ces frais.

Avant de conclure, il est important de noter qu'il y a une autre décision cruciale à prendre lors de l'ouverture de canaux Lightning : choisir entre un canal public ou un canal privé. Chacun a ses avantages et inconvénients, en fonction de vos besoins et de vos préférences.

Un canal public est annoncé à l'ensemble du réseau Lightning et peut être utilisé pour le routage de paiements. C'est une excellente option si vous souhaitez participer activement au réseau et aider à faciliter les transactions d'autres utilisateurs. Cela peut également générer des revenus (très faibles) grâce aux frais de routage que vous pouvez percevoir. Cependant, gardez à l'esprit que puisqu'un canal public est visible par tout le monde, il ne convient pas si vous cherchez à maintenir un haut niveau de confidentialité.

D'un autre côté, un canal privé n'est pas annoncé au réseau et ne sera pas utilisé pour le routage de paiements. C'est une bonne option si vous privilégiez la confidentialité et si vous prévoyez d'utiliser le canal principalement pour vos propres transactions. Il convient de noter que même si un canal privé n'offre pas les mêmes opportunités de revenus de frais de routage qu'un canal public, il peut offrir une tranquillité d'esprit accrue en termes de sécurité et de confidentialité.

En fin de compte, le choix entre un canal public et un canal privé dépend de votre propre situation et de vos priorités. Évaluez soigneusement vos besoins et vos objectifs avant de prendre une décision.

En conclusion, l'ouverture de canaux dans le Lightning Network est une démarche technique essentielle pour optimiser vos transactions. Le choix de la taille de vos canaux, le choix entre un canal public ou privé, et la sélection judicieuse des parties avec lesquelles ouvrir des canaux sont des facteurs déterminants pour un routage efficace et économique. Dans notre prochaine partie, nous nous pencherons sur la gestion efficace de ces canaux. Alors, passez à la prochaine section pour plus de détails sur cette importante facette du Lightning Network.

# Gestion des canaux LN

![gestion des canaux LN](https://youtu.be/CgBnGQLar4o)

Maintenant que nous avons couvert l'ouverture des canaux du Lightning Network, tournons notre attention vers leur gestion. Une gestion efficace des canaux peut faire une grande différence dans l'optimisation de votre expérience Lightning Network.

Le premier élément essentiel de la gestion des canaux est l'équilibrage. Les canaux du Lightning Network ont ce qu'on appelle une "liquidité", qui est répartie entre les deux parties du canal. L'équilibrage de cette liquidité est crucial pour s'assurer que les transactions peuvent être acheminées efficacement par votre nœud. Trop de liquidité d'un côté ou de l'autre peut rendre le canal moins utile pour le routage. Heureusement, il existe plusieurs stratégies pour équilibrer les canaux, notamment en utilisant des services comme Lightning Loop de Lightning Labs, qui permet de déplacer la liquidité vers et hors du réseau Bitcoin.

Le deuxième élément à considérer est la surveillance de vos canaux. Il est important de vérifier régulièrement l'état de vos canaux et de surveiller les performances de votre nœud. Des outils comme ThunderHub et RTL offrent de grandes fonctionnalités pour aider à surveiller votre nœud et à gérer vos canaux. Ils vous fournissent des informations sur l'état de vos canaux, y compris leur liquidité, leurs frais et leur capacité. De plus, ils offrent des fonctionnalités pour fermer des canaux, ouvrir de nouveaux canaux et rééquilibrer la liquidité entre les canaux.

Troisièmement, il faut prendre en compte la fermeture des canaux. Parfois, vous pouvez vous retrouver avec un canal qui n'est plus utile ou qui n'est plus performant. Dans ce cas, vous voudrez fermer le canal. Cependant, il est important de noter que fermer un canal entraîne une transaction sur la blockchain de Bitcoin, ce qui peut entraîner des frais. Par conséquent, il est judicieux de fermer les canaux pendant les périodes de faible congestion sur la blockchain pour minimiser les frais.

En conclusion, la gestion des canaux du Lightning Network est un élément important pour maintenir un nœud Lightning performant et économique. Avec une bonne stratégie d'équilibrage, une surveillance régulière et une gestion intelligente de l'ouverture et de la fermeture des canaux, vous pouvez optimiser votre expérience avec le Lightning Network. Dans le prochain segment, nous aborderons un autre aspect crucial du Lightning Network : la sécurité.

# Renommer son nœud LN

![renommer son noeud LN](https://youtu.be/HnK1_TDYXsY)

Personnaliser l'alias de votre nœud Lightning Network est une excellente manière de vous distinguer sur le réseau. C'est non seulement pratique, mais c'est aussi une façon de personnaliser votre expérience. Pour changer l'alias de votre nœud, nous utiliserons l'interface de ligne de commande. Pour les moins familiers avec cette interface, ne vous inquiétez pas, ce guide vous aidera pas à pas.

Pour commencer, vous devez ouvrir le terminal de votre système. Le terminal est une interface de commande qui permet d'interagir directement avec votre système d'exploitation. Une fois le terminal ouvert, tapez la commande `ssh -t umbrel@umbrel.local` et appuyez sur Entrée. Cette commande va établir une connexion sécurisée avec votre Umbrel.

Ensuite, on vous demandera d'entrer le mot de passe de votre Umbrel. Notez bien que pour des raisons de sécurité, le mot de passe ne s'affiche pas à l'écran lors de la frappe. Après avoir entré votre mot de passe, vous allez accéder à l'interface de votre Umbrel.

Une fois connecté, entrez la commande `sudo nano umbrel/lnd/lnd.conf` dans le terminal et appuyez sur Entrée. Cela vous amène à un éditeur de texte appelé Nano où vous pouvez modifier le fichier de configuration de votre nœud Lightning.

Encore une fois, vous devrez taper votre mot de passe. Ensuite, naviguez dans le fichier jusqu'à la section intitulée "Application Options". Dans cette section, ajoutez la ligne `alias=SOMENAME`, en remplaçant "SOMENAME" par l'alias que vous souhaitez pour votre nœud. Notez que l'utilisation de la souris est inutile dans cette interface, donc utilisez plutôt les flèches pour naviguer.

Pour sauvegarder les modifications, appuyez sur `Ctrl-X`, puis sur `Y`, et enfin sur `Entrée`. Cela fermera l'éditeur et sauvegardera vos modifications. Pour que ces modifications prennent effet, vous devez redémarrer votre Umbrel. Pour ce faire, accédez au menu des paramètres de l'interface Umbrel et choisissez l'option de redémarrage.

Et voilà, vous avez réussi à changer l'alias de votre nœud Lightning Network ! Vous pouvez maintenant revendiquer votre nœud sur des sites comme 1ML ou Amboss. Dans la prochaine section, nous discuterons d'autres méthodes pour personnaliser et optimiser votre nœud Lightning Network.

### Soutiens-nous

Ce cours, ainsi que l'intégralité du contenu présent sur cette université, vous a été offert gratuitement par notre communauté. Pour nous soutenir, vous pouvez le partager autour de vous, devenir membre de l'université et même contribuer à son développement via GitHub. Au nom de toute l'équipe, merci !

### Note la formation

Un système de notation pour la formation sera bientôt intégré à cette nouvelle plateforme de E-learning ! En attendant, merci beaucoup d'avoir suivi le cours et si vous l'avez apprécié, pensez à le partager autour de vous.

# Utilisation ludique du LN

![utilisation du LN](https://youtu.be/6yekAvH13E0)

Maintenant que vous avez configuré votre nœud, il est temps de l'utiliser. Pour cette première utilisation, nous allons nous intéresser à [Satoshi's Place](https://satoshis.place/), un service fascinant qui vous permet de dépenser des satoshis, l'unité la plus petite du bitcoin, pour faire du pixel art sur une place publique en ligne. Chaque pixel change de couleur pour un satoshi. Libre à vous de laisser libre cours à votre créativité, pour ma part, j'ai créé une pokeball pour 166 satoshis ! Les paiements se font par l'intermédiaire de "factures" ou "invoices" sur le réseau Lightning. Ces factures peuvent être représentées sous forme de QR code, rendant le paiement facile et instantané.

Lorsqu'une transaction traverse plusieurs nœuds, des frais de routage sont généralement impliqués. Il est donc crucial d'être bien connecté au centre du réseau pour réduire ces coûts. Une alternative serait d'ouvrir un canal directement avec le commerçant. Cela présente plusieurs avantages, notamment des frais de transaction plus faibles et une vitesse de transaction plus rapide.

En guise d'exemple, nous allons créer un canal avec Satoshi's Place pour les futurs paiements. Après la création du canal, une attente d'environ 30 minutes est nécessaire pour que le canal devienne opérationnel. Une fois le canal créé, vous pouvez effectuer des paiements directs. Par exemple, vous pouvez envoyer un satoshi gratuitement via le réseau Lightning sans intermédiaire de confiance.

Le réseau Lightning présente plusieurs avantages, notamment son faible coût et la possibilité d'effectuer des paiements réguliers. Pour commencer, il est recommandé d'utiliser des portefeuilles tels que Wallet of Satoshi ou Alby. Ces portefeuilles permettent de payer des factures en utilisant le réseau Lightning. Pour en apprendre davantage pour pouvez lire cette [article](https://asi0.substack.com/p/comparatif-des-portefeuilles-ln) de Darthcoin.

En conclusion, le réseau Lightning prouve la capacité de Bitcoin à évoluer. Non seulement il permet des transactions à faible coût, mais il offre également une solution aux problèmes d'échelle que Bitcoin a connus dans le passé.

# Accepter Bitcoin avec BTCpay serveur

![accepter bticoin dans son commerce](https://youtu.be/zpCMlLfiRgg)

Au fil de ce dernier chapitre, nous explorerons les différentes façons d'accepter Bitcoin pour votre commerce. Nous passerons en revue trois options principales, à savoir BTCPay Server via votre nœud Umbrel, BTCPay via un nœud Luna externe et enfin via OpenNode. Il est essentiel de noter que chaque option a ses nuances, et il est crucial de choisir celle qui convient le mieux à vos besoins spécifiques.

Imaginons que vous êtes propriétaire d'un restaurant et que vous disposez d'un nœud Umbrel dans votre établissement. Dans ce cas, vous pouvez utiliser BTCpay directement sous Tor. C'est une solution idéale pour les opérations physiques où les clients paient en personne.

En revanche, pour un e-commerce, l'utilisation de BTCPay sous Tor de son nœud Umbrel n'est pas réalisable. Dans ce cas, l'utilisation d'un nœud externe en clearnet, comme Luna Node, est préférable. Ceci offre plus de flexibilité et permet une intégration plus fluide avec votre plateforme de commerce en ligne.

Pour ceux qui recherchent une solution tout-en-un et facile à gérer, OpenNode est une excellente option. Cependant, sa configuration et son utilisation peuvent être assez complexes. C'est pourquoi nous prévoyons de couvrir cette solution plus en détail dans une formation dédiée à part entière.

Vous trouverez ci-dessous les liens vers les différents services mentionnés :

- [OpenNode](https://www.opennode.com/)
- [BTCPay Server](https://btcpayserver.org/)
- [Luna Node](https://www.lunanode.com/) et le guide sur [BTCPay Server avec Luna Node](https://docs.btcpayserver.org/Deployment/LunaNode/)

En outre, j'ai eu l'occasion d'interviewer Nicolas Dorier, le créateur de BTCPay Server. Si cela vous intéresse, n'hésitez pas à visionner notre conversation en cliquant [ici](https://www.youtube.com/watch?v=XR6qB76hCL0&pp=ygUoaW50ZXJ2aWV3IG5pY29sYSBkb3JpZXIgZGVjb3V2cmUgYml0Y29pbg%3D%3D). Vous découvrirez de nombreuses informations intéressantes et des conseils précieux pour optimiser l'utilisation de BTCPay Server dans votre commerce.

En somme, l'acceptation de Bitcoin peut offrir une multitude d'avantages pour votre commerce. Que vous soyez un restaurant local ou un e-commerce mondial, il existe une solution adaptée à vos besoins. Prenez le temps d'examiner les différentes options, et n'hésitez pas à vous lancer dans cette nouvelle aventure Bitcoin.

# Résumé de la formation

![conclusion](https://youtu.be/QrKbagtUE1s)

Nous voici arrivés à la conclusion de notre exploration approfondie du réseau Lightning de Bitcoin. Nous avons parcouru un chemin complexe, peuplé d'innovations technologiques et de nouvelles perspectives sur la façon dont nous interagissons avec notre argent numérique. De l'exploration initiale d'Umbrel à l'ouverture et à la gestion des canaux Lightning, chaque étape a été un pas vers une meilleure compréhension et une plus grande maîtrise de cette technologie révolutionnaire.

Nous avons commencé par un survol d'Umbrel, nous familiarisant avec l'interface et les fonctionnalités clés. Nous avons ensuite plongé dans la Mempool, en apprenant à analyser les transactions en attente pour une vision plus approfondie du réseau Bitcoin. Ensuite, nous avons exploré les block explorers et les statistiques du réseau, des outils essentiels pour surveiller l'état du réseau.

Nous avons ensuite abordé l'aspect le plus personnel du réseau Bitcoin : le portefeuille. Nous avons appris à connecter notre portefeuille à notre nœud, puis nous avons découvert l'importance et la sécurité des portefeuilles multisig grâce à Specter.

Ensuite, nous avons plongé dans l'univers du réseau Lightning. Nous avons exploré l'ouverture des canaux Lightning et leur gestion, deux aspects cruciaux pour un fonctionnement optimal de notre nœud. Nous avons également appris à renommer notre nœud pour faciliter son identification sur le réseau.

Nous avons aussi eu un aperçu ludique de l'utilisation du Lightning Network grâce à Satoshi's Place, un exemple concret de la manière dont le LN peut être utilisé pour des micro-transactions à faible coût.

Enfin, nous avons abordé l'aspect commercial du Bitcoin. Nous avons exploré comment accepter Bitcoin dans son commerce via BTCpay server, en prenant en compte différentes configurations en fonction des besoins.

Cela étant dit, maîtriser le réseau Lightning n'est pas une tâche qui se fait en un jour. Il s'agit d'une technologie en constante évolution, complexe et nuancée. Il faudra du temps, de la pratique et une volonté d'apprendre pour vraiment maîtriser cet outil. Tout comme Bitcoin lui-même, le Lightning Network est une aventure, une exploration de ce qui est possible dans le domaine de la finance numérique. Mais avec patience, persévérance et une volonté d'apprendre, vous serez bientôt capable de naviguer dans le réseau Lightning avec aisance et confiance.

En somme, le voyage que nous avons entrepris ensemble à travers le réseau Lightning n'est que le début. La maîtrise de cette technologie offre de nombreuses opportunités et avantages. Alors continuez à explorer, à apprendre et à expérimenter avec le Lightning Network. Le futur de la finance est à portée de main.

Pour finir, il est important de souligner que cette formation, tout comme les autres que nous proposons, est entièrement gratuite. Nous croyons fermement à l'importance de partager la connaissance et de rendre l'accès à l'information aussi libre et ouvert que possible. C'est dans cet esprit que nous avons décidé de partager avec vous tout ce que nous avons appris sur le réseau Lightning.

Cependant, si vous avez trouvé de la valeur dans cette formation et que vous souhaitez nous soutenir, nous vous invitons à visiter notre site e-commerce à l'adresse suivante : https://thebitcoinrabbithole.myshopify.com/. En effectuant des achats sur notre site, vous contribuez non seulement à soutenir notre travail, mais vous nous aidez aussi à continuer à fournir des formations gratuites et de haute qualité.

Merci d'avoir pris le temps de suivre cette formation. Votre soutien et votre intérêt pour notre travail signifient beaucoup pour nous.

# Remerciements et continuez à creuser le terrier du lapin

Félicitations pour avoir terminé cette formation LN 202 ! J'espère de tout cœur qu'elle vous a plu et ouvert des portes. Votre découverte du bitcoin n'en est qu'à ses débuts et je vous invite à découvrir toutes les autres formations disponibles sur l'université.

- ECON 201 abordera l'économie autrichienne
- SECU 101 vous permettra de mettre à jour votre sécurité
- MINAGE 201 pour en savoir plus sur le minage
- (et bien d'autres)

Bisous et à bientôt !
