---
name: PearPass
description: Reprenez le contrôle de vos mots de passe grâce à un gestionnaire local, pair-à-pair et sans cloud
---

![cover](assets/cover.webp)

À l’heure où chaque individu gère des dizaines, voire des centaines de comptes en ligne, la sécurité des identifiants est devenue un enjeu central de la sécurité informatique. Réseaux sociaux, messageries, services professionnels, plateformes financières : chacun de ces accès repose sur un secret dont la compromission peut avoir des conséquences graves sur votre vie.

Pourtant, malgré la multiplication des attaques, les mauvaises pratiques restent largement répandues dans la population : mots de passe faibles, réutilisés, stockés en clair ou mémorisés approximativement. Pour résoudre ces problèmes sans se compliquer la vie au quotidien, la solution consiste à utiliser un gestionnaire de mots de passe.

Il existe déjà des dizaines de gestionnaires de mots de passe, et Plan ₿ Academy propose un tutoriel pour la plupart d’entre eux. Mais dans ce tutoriel, je vous propose d’en découvrir un qui se distingue clairement des autres par son fonctionnement : **PearPass**.

**PearPass est un gestionnaire de mots de passe pair-à-pair, local-first et open-source, pensé pour redonner à l’utilisateur un contrôle total sur ses données.**

![Image](assets/fr/01.webp)

## Pourquoi choisir PearPass ?

Un gestionnaire de mots de passe est un logiciel dont le rôle est de générer, stocker et organiser l’ensemble de vos identifiants de manière sécurisée. Plutôt que de mémoriser ou de réutiliser des mots de passe, vous n’avez plus qu’un seul secret à protéger : le mot de passe maître, qui chiffre l’intégralité de votre coffre-fort. Cette approche permet d’utiliser des mots de passe uniques, longs et aléatoires pour chaque service, ce qui réduit à la fois les risques d’oubli et de compromission, tout en limitant l’impact d’une éventuelle fuite. Aujourd’hui, il s’agit d’un outil de base en informatique que tout le monde devrait utiliser.

Il existe deux grandes catégories de gestionnaires de mots de passe. D’un côté, les logiciels fonctionnant uniquement en local, très sécurisés puisque les données ne sont jamais stockées sur un serveur central, mais peu pratiques, car ils ne permettent pas de synchroniser facilement vos identifiants entre plusieurs appareils (ordinateur, smartphone, tablette...). De l’autre, les gestionnaires de mots de passe fonctionnant dans le cloud, qui conservent vos identifiants sur leurs serveurs et les synchronisent sur l’ensemble de vos appareils. Leur principal avantage est la praticité, mais ils impliquent un compromis sur la sécurité, puisque vos mots de passe sont stockés sur des infrastructures que vous ne contrôlez pas.

PearPass rompt volontairement avec ces deux modèles. Il se positionne entre les gestionnaires locaux et les solutions cloud : il permet la synchronisation de vos mots de passe, tout en garantissant qu’ils ne sont jamais stockés sur des serveurs distants. Ainsi, l’ensemble de vos identifiants est conservé localement sur vos appareils, et la synchronisation entre plusieurs machines s’effectue exclusivement en pair-à-pair. Cette architecture élimine les points de défaillance uniques liés aux bases de données centralisées : il n’existe aucun serveur à compromettre, ni d’infrastructure tierce susceptible d’accéder à vos identifiants. Les communications entre vos appareils sont chiffrées de bout en bout, ce qui garantit que seules les clés que vous détenez permettent l’accès aux données.

![Image](assets/fr/02.webp)

Pour rendre cela possible, comme son nom l’indique, PearPass s’appuie sur **Pears**, un écosystème technologique pair-à-pair dédié à la création et à l’exécution d’applications sans serveur. Pears fournit l’environnement d’exécution, les mécanismes de distribution et les couches réseau nécessaires au fonctionnement d’applications entièrement décentralisées, capables de se synchroniser directement entre pairs, sans infrastructure centrale. Dans le cas de PearPass, Pears assure la découverte des appareils, l’établissement de connexions chiffrées et la synchronisation des coffres-forts de mots de passe entre vos machines. Cette approche garantit que PearPass reste fonctionnel, résilient et indépendant de toute autorité externe.

https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Au-delà de cette architecture novatrice, PearPass est entièrement open-source et l’ensemble de ses fonctionnalités est gratuit. Le logiciel a également fait l’objet d’un audit indépendant par Secfault Security. En plus de son architecture spécifique, PearPass propose évidemment toutes les fonctionnalités classiques attendues d’un bon gestionnaire de mots de passe, que nous allons découvrir tout au long de ce tutoriel.

Pour résumer, là où les gestionnaires de mots de passe traditionnels vous demandent de faire confiance à une entreprise et à ses serveurs, PearPass adopte une logique de souveraineté : pas de cloud, pas de comptes centralisés, pas d’intermédiaires. Vous conservez un contrôle exclusif sur vos identifiants, tout en bénéficiant de la synchronisation entre vos appareils.

## Comment installer PearPass ?

PearPass est disponible sur l’ensemble des plateformes : Windows, Linux, macOS, Android, iOS et extension de navigateur. Il n’est pas nécessaire d’installer Pears sur votre machine : PearPass fonctionne de manière autonome.

### Installation sur Windows

Sur Windows, PearPass est fourni sous la forme d’un installateur classique. Rendez-vous [sur la page officielle de téléchargement](https://pass.pears.com/download), puis cliquez sur le bouton `Download Windows installer`.

Une fois le fichier téléchargé, ouvrez l’installateur et suivez les étapes indiquées par l’assistant. L’application est ensuite accessible depuis le `Start Menu` ou via un raccourci sur le bureau.

![Image](assets/fr/03.webp)

### Installation sur macOS

Sur macOS, PearPass est distribué sous la forme d’une image disque (`.dmg`). Rendez-vous [sur la page officielle de téléchargement](https://pass.pears.com/download) et choisissez la version correspondant à l’architecture de votre Mac (Intel ou Apple Silicon). Après téléchargement, ouvrez le fichier `.dmg` et lancez l’application depuis le dossier `Applications`.

Lors du premier démarrage, macOS affichera un message de sécurité indiquant que l’application provient d’Internet : il suffit de confirmer pour poursuivre.

### Installation sur Linux

Sur Linux, PearPass est proposé au format `.AppImage`, ce qui garantit une compatibilité large avec la majorité des distributions sans dépendances spécifiques. Téléchargez le fichier `.AppImage` depuis [la page officielle de téléchargement](https://pass.pears.com/download), puis lancez-le directement par un double-clic.

Selon votre environnement, il peut être nécessaire de rendre le fichier exécutable via les propriétés du fichier (clique droit) ou avec la commande `chmod +x`. Une fois autorisé, PearPass se lance comme une application autonome.

### Installation de l’extension navigateur

PearPass propose une extension pour navigateur permettant le remplissage automatique des identifiants et un accès rapide à votre coffre-fort lors de la navigation web. L’extension est actuellement disponible pour Google Chrome et les navigateurs compatibles. Pour l’installer, rendez-vous [sur la page de téléchargement officielle](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).

![Image](assets/fr/04.webp)

Une fois ajoutée, vous pouvez l'épingler dans la barre d’outils pour un accès rapide. L’activation de l’extension nécessite ensuite une liaison avec l’application PearPass installée localement sur votre ordinateur (nous y reviendrons plus loin dans le tutoriel).

### Installation sur iOS et Android

Sur iPhone et Android, vous pouvez simplement télécharger l’application depuis votre store d’applications :
- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass) ;
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).

![Image](assets/fr/05.webp)

En plus de ces méthodes d’installation classiques, il est également possible de télécharger directement le logiciel depuis les dépôts GitHub, pour chaque plateforme :
- [Desktop](https://github.com/tetherto/pearpass-app-desktop) ;
- [Mobile](https://github.com/tetherto/pearpass-app-mobile) ;
- [Extension de navigateur](https://github.com/tetherto/pearpass-app-browser-extension).

Une fois PearPass installé sur une ou plusieurs plateformes, vous pouvez passer à la configuration initiale. Dans ce tutoriel, nous commencerons par configurer le logiciel sur desktop, puis nous le synchroniserons avec l’extension de navigateur et l’application mobile.

## Comment créer un coffre-fort sur PearPass ?

Lors du premier lancement de PearPass sur ordinateur, l’application vous guide à travers deux étapes : la définition de votre mot de passe maître, puis la création de votre premier coffre-fort.

### Définir le mot de passe maître

Au premier démarrage de l’application sur desktop, cliquez sur le bouton `Skip` puis `Continue` afin de parcourir l’écran d’introduction et d’atteindre l’étape de configuration du mot de passe maître.

![Image](assets/fr/06.webp)

Vient ensuite l'étape importante du choix de votre mot de passe maître. Comme nous l'avons vu dans l'introduction, ce mot de passe est très important, car il vous donne accès à tous vos autres mots de passe sauvegardés sur le gestionnaire. Techniquement, il sert à dériver les clés cryptographiques utilisées pour chiffrer vos données.

Le mot de passe maître comporte deux risques principaux : la perte et la compromission. Si vous perdez l’accès à ce mot de passe, vous ne pourrez plus accéder à vos identifiants. En effet, PearPass ne conserve jamais votre mot de passe maître : **s’il est perdu, vos identifiants le sont définitivement**. Il n’existe aucun mécanisme de récupération. À l’inverse, si ce mot de passe est compromis et qu’un attaquant obtient l’accès à l’un de vos appareils, il pourra accéder à l’intégralité de vos comptes.

Pour limiter le risque de perte, vous pouvez effectuer une sauvegarde physique de votre mot de passe maître, par exemple sur papier, et la conserver dans un lieu sécurisé. Idéalement, scellez cette sauvegarde dans une enveloppe afin de pouvoir vérifier périodiquement qu’elle n’a pas été consultée. En revanche, ne réalisez jamais de sauvegarde numérique de ce mot de passe.

Pour réduire le risque de compromission, votre mot de passe maître doit être fort. Il doit être le plus long possible, inclure une grande diversité de caractères et être choisi de manière réellement aléatoire. En 2025, les recommandations minimales évoquent au moins 13 caractères comprenant des lettres minuscules et majuscules, des chiffres et des symboles, à condition que le mot de passe soit aléatoire. Toutefois, je vous recommande plutôt un mot de passe d’au moins 20 caractères, voire davantage, avec tous les types de caractères, afin d’assurer un niveau de sécurité plus durable.

Saisissez votre mot de passe maître dans le champ prévu, confirmez-le une seconde fois, puis cliquez sur le bouton `Continue`.

![Image](assets/fr/07.webp)

Vous êtes alors redirigé vers l’écran de connexion : saisissez votre mot de passe maître pour vérifier que tout fonctionne correctement.

![Image](assets/fr/08.webp)

### Créer votre premier coffre-fort

Une fois connecté, PearPass vous propose de créer votre premier coffre-fort. Un coffre-fort est un conteneur chiffré dans lequel sont stockés vos mots de passe, identifiants, notes sécurisées et autres informations. Chaque coffre-fort est isolé et peut être identifié par un nom distinct, ce qui permet d’organiser vos données selon vos usages (personnel, professionnel, projets spécifiques...).

Cliquez sur le bouton `Create a new vault`.

![Image](assets/fr/09.webp)

Choisissez un nom pour ce coffre-fort, puis cliquez de nouveau sur `Create a new vault` pour finaliser la création.

![Image](assets/fr/10.webp)

Votre coffre-fort est immédiatement prêt à l’emploi. Vous pouvez dès à présent commencer à y ajouter des mots de passe, des identifiants ou des notes sécurisées.

![Image](assets/fr/11.webp)

## Comment ajouter un identifiant sur PearPass ?

Une fois votre coffre-fort créé, vous pouvez commencer à y enregistrer vos éléments. PearPass prend en charge l’enregistrement de nombreux types d’éléments :
- identifiant de connexion à un site ou à un service ;
- identité : vos informations personnelles pour remplir rapidement des formulaires, mais aussi stocker des documents d’identité directement dans PearPass ;
- carte bancaire : vos numéros de carte pour payer plus rapidement lors de vos achats en ligne ;
- Wi-Fi : les mots de passe de vos réseaux Wi-Fi ;
- PassPhrase : phrase secrète composée de plusieurs mots (attention : je vous déconseille fortement de l’utiliser pour des phrases mnémoniques de wallet Bitcoin) ;
- note : création de notes sécurisées ;
- custom : cette fonctionnalité permet de créer un type d’élément personnalisé, adapté à vos besoins spécifiques.

Commencez par ouvrir PearPass et connectez-vous à l’aide de votre mot de passe maître.

![Image](assets/fr/12.webp)

Sélectionnez le coffre-fort dans lequel vous souhaitez enregistrer cet identifiant.

![Image](assets/fr/13.webp)

Sur la page d’accueil, cliquez ensuite sur le bouton permettant d’ajouter un nouvel élément, en fonction du type d’information que vous souhaitez enregistrer. Dans mon cas, je veux ajouter un identifiant pour mon compte sur le site web de Plan ₿ Academy : je clique donc sur le bouton `Create a Login`.

![Image](assets/fr/14.webp)

Après avoir sélectionné le type d’élément à ajouter, un formulaire s’affiche et vous permet de renseigner les informations associées au service concerné. Selon vos besoins, vous pouvez indiquer le nom du service, l’identifiant de connexion, le mot de passe et, si besoin, l’adresse du site web et des notes complémentaires.

PearPass intègre également un générateur de mots de passe, qui permet de créer un mot de passe fort directement depuis le formulaire. Pour l’utiliser, cliquez sur l’icône représentant trois petits points dans le champ `Password`, choisissez la longueur souhaitée, puis cliquez sur `Insert password`.

Une fois l’ensemble des champs renseignés, cliquez sur le bouton `Save` afin d’enregistrer l’identifiant dans le coffre-fort.

![Image](assets/fr/15.webp)

L’identifiant est désormais enregistré. Il apparaît dans la liste des éléments du coffre-fort sélectionné et peut être consulté en cliquant dessus.

![Image](assets/fr/16.webp)

Vous pouvez facilement modifier un élément en cliquant dessus, puis sur le bouton `Edit`. Il est également possible de le supprimer en cliquant sur les trois petits points en haut à droite de l’interface, puis sur `Delete element`.

![Image](assets/fr/22.webp)

Sur mobile, la logique reste la même, bien que l’interface soit adaptée. Après vous être connecté, sélectionnez le coffre-fort souhaité, tapez sur le bouton `+`, choisissez le type d’élément à créer, puis renseignez les informations nécessaires.

![Image](assets/fr/17.webp)

## Comment organiser PearPass ?

Nous l’avons vu dans les sections précédentes, PearPass permet de créer plusieurs vaults distincts. Cela permet de séparer différents usages et constitue un premier niveau d’organisation de votre gestionnaire de mots de passe. Depuis la page d’accueil, vous pouvez passer facilement d’un vault à un autre en cliquant sur la flèche située en haut à gauche de l’interface.

![Image](assets/fr/18.webp)

Une autre façon d’organiser vos mots de passe, à l’intérieur même d’un vault, consiste à créer des dossiers. Pour cela, dans la colonne de gauche de l’interface, cliquez sur le symbole `+` à côté de `All Folders`, puis indiquez le nom du dossier que vous souhaitez créer.

![Image](assets/fr/19.webp)

Vous pouvez ensuite y ranger les identifiants de votre choix, soit directement lors de la création d’un élément, soit ultérieurement en cliquant sur `Edit`. Il vous suffit alors de sélectionner, en haut à gauche du formulaire, le dossier souhaité.

![Image](assets/fr/20.webp)

Après avoir ouvert un élément, comme un identifiant, vous pouvez cliquer sur l’icône en forme d’étoile en haut à droite de l’interface afin de l’ajouter à vos favoris. Les favoris peuvent être retrouvés rapidement dans un dossier dédié, en plus de leur dossier de base.

![Image](assets/fr/21.webp)

Enfin, il y a une barre de recherche, située en haut de l’interface, qui vous permet de retrouver rapidement l’élément que vous recherchez, même si votre vault contient de nombreux identifiants.

## Comment synchroniser PearPass sur mobile ?

Maintenant que vous disposez d’un vault fonctionnel avec des éléments enregistrés sur votre ordinateur, vous allez probablement vouloir accéder à vos mots de passe depuis votre smartphone ou un autre appareil. PearPass permet de synchroniser votre gestionnaire sur plusieurs machines de manière sécurisée grâce à Pears. Voyons comment procéder.

Pour commencer, sur la machine source (votre ordinateur par exemple), connectez-vous à votre vault à l’aide de votre mot de passe maître. Une fois sur la page d’accueil, cliquez sur le bouton `Add a Device`, situé en bas à droite de l’interface.

![Image](assets/fr/23.webp)

PearPass génère alors un lien d’invitation, également disponible sous forme de QR code, afin de synchroniser le vault sélectionné sur l’appareil de votre choix.

![Image](assets/fr/24.webp)

Si vous souhaitez effectuer cette synchronisation sur votre appareil mobile, commencez par installer l’application, puis lancez-la. Il vous sera demandé de créer un mot de passe maître pour votre gestionnaire sur mobile. Vous pouvez choisir d’utiliser le même que sur votre ordinateur ou un mot de passe différent. Dans tous les cas, suivez les mêmes recommandations : mot de passe fort, aléatoire et sauvegardé sur un support physique.

![Image](assets/fr/25.webp)

Vous pouvez ensuite activer l’authentification biométrique si vous le souhaitez, afin d’éviter d'avoir à saisir manuellement votre mot de passe maître à chaque déverrouillage sur mobile.

![Image](assets/fr/26.webp)

Renseignez à nouveau votre mot de passe maître, puis cliquez sur le bouton `Continue`.

![Image](assets/fr/27.webp)

Sélectionnez l’option `Load a vault`, puis cliquez sur `Scan QR Code` et scannez le QR code d’invitation affiché par PearPass sur votre machine source (l’ordinateur).

![Image](assets/fr/28.webp)

Vos vaults présents sur votre ordinateur et sur votre mobile sont désormais synchronisés. Chaque identifiant ajouté sur l’un des appareils sera enregistré de manière sécurisée et répliqué sur l’autre.

![Image](assets/fr/29.webp)

Sur mobile, vous pouvez également activer, si vous le souhaitez, le remplissage automatique des champs. Pour cela, rendez-vous dans `Settings > Advanced`, puis cliquez sur le bouton `Set as Default` dans la section `Autofill`.

![Image](assets/fr/30.webp)

## Comment synchroniser PearPass sur l'extension de navigateur ?

Disposer d’un gestionnaire de mots de passe synchronisé entre son ordinateur et son smartphone est déjà très pratique, mais l’intégrer directement à son navigateur l’est encore davantage. Pour cela, commencez par [ajouter l’extension officielle PearPass à votre navigateur](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).

![Image](assets/fr/31.webp)

Depuis le logiciel PearPass installé sur votre machine en local, rendez-vous dans `Settings > Advanced`, puis activez l’option `Activate browser extension`.

![Image](assets/fr/32.webp)

PearPass génère alors un token d’appairage. Copiez-le.

![Image](assets/fr/33.webp)

Ouvrez ensuite l’extension PearPass dans votre navigateur, collez le token d’appairage, puis cliquez sur le bouton `Verify`, suivi de `Complete`.

![Image](assets/fr/34.webp)

Votre gestionnaire de mots de passe est désormais synchronisé avec l’extension de navigateur.

![Image](assets/fr/35.webp)

Vous pouvez maintenant l’utiliser pour vous connecter facilement à vos différents comptes sur le web.

![Image](assets/fr/36.webp)

Vous savez désormais comment utiliser le gestionnaire de mots de passe PearPass. Au-delà de cet outil, la sécurité numérique au quotidien repose sur le bon usage de solutions adaptées. Si vous souhaitez apprendre à mettre en place un environnement numérique personnel sécurisé, stable et efficace, je vous invite à découvrir notre formation dédiée à ce sujet :

https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
