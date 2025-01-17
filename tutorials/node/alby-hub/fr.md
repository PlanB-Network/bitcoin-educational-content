---
name: Alby Hub
description: Comment lancer facilement son propre nœud Lightning ?
---
![cover](assets/cover.webp)

Alby Hub est le dernier logiciel développé par Alby, la société à l'origine de la célèbre extension web Lightning. Alby Hub est une interface pour gérer facilement un nœud Lightning.

Dans ce tutoriel, nous allons découvrir différentes façons d'utiliser Alby Hub pour gérer son propre nœud Lightning et comment le connecter à Alby Go, l'application mobile d'Alby. Cela vous permettra de dépenser vos sats en déplacement tout en étant autonome sur la gestion de votre nœud.

![ALBY HUB](assets/fr/01.webp)

## C'est quoi Alby Hub ?

En 2024, Alby a marqué un virage stratégique. Depuis des années, ils offrent une variété d'outils associés à Bitcoin et au Lightning Network, dont l'emblématique extension Alby, qui permet d'exploiter un portefeuille Lightning, custodial ou non. Cependant, en 2025, ils prévoient d'arrêter leur service de wallet custodial partagé pour se concentrer désormais exclusivement sur des solutions en self-custody. Alby Hub s'annonce comme le nouvel outil phare de l'écosystème Alby. Ce logiciel offre la possibilité de gérer son propre nœud Lightning en toute simplicité, tout en conservant la propriété de ses clés (self-custody).

Alby Hub est un outil très adaptable. Il peut répondre aux besoins d'utilisateurs débutants comme avancés. Les novices l'utiliseront pour opérer facilement un vrai nœud Lightning en toute autonomie, sans se heurter à la complexité sous-jacente. Pour les utilisateurs plus expérimentés, Alby Hub peut être utilisé comme une interface complète pour la gestion avancée d'un nœud Lightning déjà existant.

Selon votre utilisation, Alby Hub peut se décliner en 4 configurations :

- **Alby Hub Cloud :**
Idéale pour les novices, cette première option est celle du cloud d'Alby. Elle vous permet de déployer un nœud Lightning directement sur un serveur géré par Alby, accessible via votre interface Alby Hub. Bien qu'Alby prenne en charge la gestion du serveur, vous conservez la souveraineté sur vos fonds car vos clés sont chiffrées à l'aide d'un mot de passe que vous êtes le seul à connaître. Toutefois, vos clés doivent rester déchiffrées en RAM pour le fonctionnement du nœud, ce qui les expose théoriquement à un risque si quelqu'un accède physiquement au serveur. C'est donc un compromis intéressant pour les débutants, mais il est important d'être conscient des risques.

Cette option présente l'avantage majeur de vous offrir un nœud Lightning opérationnel 24h/24, 7j/7, sans avoir à gérer vous-même l'hébergement. De plus, les sauvegardes de votre nœud Lightning sont simplifiées et automatisées par rapport aux options auto-hébergées où vous devez gérer vous-même la sauvegarde des canaux.

Alby propose ce service pour 21 000 sats par mois (tarif de décembre 2024, susceptible de changer, [consultez leur tarification](https://albyhub.com/#pricing)). Les frais sont automatiquement déduits de votre nœud via une facture Lightning émise par Alby. Cette opération est réalisée par une connexion NWC qui configure votre nœud pour régler automatiquement les factures d'Alby liées à votre abonnement.

- **Alby Hub avec un nœud existant :**
Si vous possédez déjà un nœud hébergé, par exemple sur Umbrel ou Start9, Alby Hub peut être utilisé comme une interface de gestion avancée, de la même manière que ThunderHub ou RTL.

- **Alby Hub en local :**
Il est également possible d'installer Alby Hub et votre nœud directement sur votre PC, bien que cette option soit moins pratique, car votre PC doit rester actif en permanence pour accéder à distance au nœud Lightning. Cette alternative peut néanmoins convenir en fonction de vos besoins spécifiques.

- **Alby Hub sur un serveur personnel :**
Pour les utilisateurs avancés, Alby Hub peut être déployé sur un serveur personnel avec une simple commande. Cette option n'est pas couverte dans ce tutoriel, mais vous pouvez trouver les instructions dédiées [sur le GitHub d'Alby](https://github.com/getAlby/hub?tab=readme-ov-file#docker).

Ce tutoriel se concentre principalement sur l'interface, qui sera la même quelle que soit l'option choisie. Nous allons également voir comment déployer Alby Hub avec l'option du cloud payant, puis avec l'option du node-in-box (Umbrel ou Start9).

![ALBY HUB](assets/fr/02.webp)

Pour une installation locale sur votre PC, [téléchargez et installez le logiciel selon votre système d'exploitation](https://github.com/getAlby/hub/releases), puis suivez les mêmes instructions au niveau de l'interface.

![ALBY HUB](assets/fr/03.webp)

## Créer un compte Alby

La première étape consiste à créer un compte Alby. Bien que ce ne soit pas indispensable pour utiliser Alby Hub, cela vous permet de profiter pleinement des options disponibles, notamment la possibilité d'obtenir une adresse Lightning.

Rendez-vous sur [le site officiel d'Alby](https://getalby.com/) et cliquez sur le bouton "*Create Account*".

![ALBY HUB](assets/fr/04.webp)

Saisissez un pseudonyme et une adresse email, puis cliquez sur "*Sign up*". Cette adresse email servira à vous connecter à votre compte par la suite.

![ALBY HUB](assets/fr/05.webp)

Entrez le code de vérification que vous avez reçu par email.

![ALBY HUB](assets/fr/06.webp)

Une fois connecté à votre compte en ligne, cliquez sur le bouton "*Continue*".

![ALBY HUB](assets/fr/07.webp)

Cliquez de nouveau sur "*Continue*".

![ALBY HUB](assets/fr/08.webp)

## L'option d'hébergement cloud

Vous devrez ensuite choisir entre une option self-hosted, où vous hébergez un nœud Lightning sur votre propre matériel, ou l'option payante utilisant le cloud d'Alby. Je vais d'abord vous expliquer comment procéder avec l'option Cloud (notez que cette option est payante, voir les détails dans la partie précédente).

Cliquez sur "*Upgrade*".

![ALBY HUB](assets/fr/09.webp)

Confirmez en cliquant sur "*Subscribe Now*".

![ALBY HUB](assets/fr/10.webp)

Cliquez sur "*Launch Alby Hub*".

![ALBY HUB](assets/fr/11.webp)

Patientez quelques instants le temps que votre nœud soit créé.

![ALBY HUB](assets/fr/12.webp)

Et voilà, votre Alby Hub est désormais configuré. Dans la partie suivante, je vous montrerai comment installer Alby Hub sur un nœud déjà existant. Si vous n'en avez pas besoin, vous pouvez passer directement à la section suivante pour configurer votre nœud.

![ALBY HUB](assets/fr/13.webp)

## L'option d'auto-hébergement

Si vous préférez utiliser Alby Hub comme interface pour votre nœud Lightning existant, vous avez plusieurs options : l'installer sur un serveur, en local sur votre ordinateur, ou via un node-in-box (Umbrel ou Start9). L'utilisation d'Alby Hub dans ces configurations est gratuite. Nous allons nous concentrer sur l'option node-in-box, car je trouve que l'option serveur, sans accès physique, présente des risques similaires à la version cloud, et l'installation locale sur PC est souvent inadaptée.

Pour configurer cela sur Umbrel (les étapes pour Start9 sont identiques), vous devez d'abord avoir un nœud LND déjà configuré.

Connectez-vous à votre interface Umbrel et allez dans le magasin d'applications.

![ALBY HUB](assets/fr/14.webp)

Recherchez l'application "*Alby Hub*".

![ALBY HUB](assets/fr/15.webp)

Installez-la sur votre nœud.

![ALBY HUB](assets/fr/16.webp)

Votre interface Alby Hub est maintenant prête. Vous pouvez suivre le reste du tutoriel comme si vous utilisiez l'interface cloud, mais sans les options de la version payante. De plus, contrairement à la version cloud, vos clés sont conservées localement sur votre nœud et non sur les serveurs d'Alby.

![ALBY HUB](assets/fr/17.webp)

## Lancer Alby Hub

Cliquez sur le bouton "*Get Started*".

![ALBY HUB](assets/fr/18.webp)

Alby Hub vous invitera ensuite à choisir un mot de passe. Ce mot de passe est très important, car il sera utilisé pour chiffrer votre portefeuille. Dans la version cloud payante, vos clés sont conservées sur le serveur d'Alby, chiffrées avec ce mot de passe que vous êtes le seul à connaître, puis déchiffrées et stockées uniquement en RAM pour signer les transactions quand nécessaire.

Il est donc essentiel de choisir un mot de passe robuste. Toute personne possédant ce mot de passe pourrait potentiellement accéder à votre nœud. Assurez-vous également de réaliser une ou plusieurs sauvegardes physiques de ce mot de passe sur un morceau de papier, ou mieux, sur un morceau de métal pour plus de sécurité. **Si vous perdez ce mot de passe, il vous sera impossible de récupérer l'accès à vos bitcoins**, car Alby n'a aucun moyen de le réinitialiser. La perte de ce mot de passe signifie donc la perte de vos bitcoins.

Après avoir soigneusement choisi et sauvegardé votre mot de passe, cliquez sur "*Create Password*".

![ALBY HUB](assets/fr/19.webp)

Vous avez maintenant accès à votre nœud Lightning.

![ALBY HUB](assets/fr/20.webp)

La première action à faire est de sauvegarder votre phrase de récupération, à partir de laquelle vos clés sont dérivées. Cette phrase vous permet de récupérer l'accès à votre wallet onchain et, avec le dernier état de vos canaux, vos sats sur Lightning. Pour cela, cliquez sur "*Settings*".

![ALBY HUB](assets/fr/21.webp)

Rendez-vous ensuite dans l'onglet "*Backup*". Entrez votre mot de passe pour y accéder.

![ALBY HUB](assets/fr/22.webp)

Vous aurez alors accès à votre phrase de récupération de 12 mots. Réalisez une ou plusieurs sauvegardes physiques de cette phrase sur du papier ou du métal et conservez-la en lieu sûr.

![ALBY HUB](assets/fr/23.webp)

Après avoir sauvegardé la phrase, cochez la case confirmant que vous l'avez bien sauvegardée et cliquez sur "*Continue*".

![ALBY HUB](assets/fr/24.webp)

## Comment récupérer l'accès à ses bitcoins ?

Avant d'envoyer des fonds sur votre nœud, il est important de comprendre comment les récupérer en cas de problème, ainsi que de savoir quelles sont les informations nécessaires à cette récupération. Le processus varie selon la nature des fonds à récupérer et le mode d'hébergement de votre nœud.

Pour les utilisateurs du cloud payant, la récupération complète de vos bitcoins nécessite trois éléments essentiels :
- Votre phrase de récupération ;
- Votre mot de passe (celui utilisé pour votre nœud) ;
- Un accès à votre compte Alby, afin de récupérer le dernier état de vos canaux Lightning.

L'absence de l'une de ces 3 informations rendrait impossible la récupération complète de vos bitcoins.

Pour ceux qui hébergent leur propre nœud, le processus de récupération est identique à celui de n'importe quel nœud Lightning. Vous aurez besoin de :
- Votre phrase de récupération ;
- Le dernier état de vos canaux Lightning. Pour sécuriser cette dernière information, Umbrel offre [une option](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) pour la chiffrer et la sauvegarder de manière dynamique et anonyme via Tor.

## Acheter son premier canal Lightning

Vous pouvez maintenant suivre les instructions fournies par Alby Hub. Cliquez sur le bouton pour ouvrir votre premier canal et ainsi disposer de liquidités entrantes.

![ALBY HUB](assets/fr/25.webp)

Sélectionnez "*Open Channel*". Si vous n'avez pas l'intention de devenir un nœud de routage et que vous n'en avez pas spécifiquement besoin, je vous recommande d'opter pour des canaux privés.

![ALBY HUB](assets/fr/26.webp)

Alby Hub va générer une invoice que vous devrez payer. Ce paiement couvre les frais de transaction nécessaires pour ouvrir votre canal, ainsi que les frais de service du LSP (*Lightning Service Provider*) qui ouvrira un canal vers votre nœud, ce qui vous permet de recevoir immédiatement des paiements.

![ALBY HUB](assets/fr/27.webp)

Une fois l'invoice payée et la transaction confirmée, votre premier canal Lightning est établi.

![ALBY HUB](assets/fr/28.webp)

Dans l'onglet "*Node*", vous pouvez constater que vous disposez désormais de liquidités entrantes, ce qui vous permet de recevoir des paiements via Lightning.

![ALBY HUB](assets/fr/29.webp)

Pour recevoir un paiement, cliquez sur l'onglet "*Wallet*" puis sur "*Receive*".

![ALBY HUB](assets/fr/30.webp)

Indiquez un montant et ajoutez une description si nécessaire, puis cliquez sur "*Create Invoice*".

![ALBY HUB](assets/fr/31.webp)

J'ai reçu mon premier paiement de 120 000 sats.

![ALBY HUB](assets/fr/32.webp)

En retournant dans l'onglet "*Wallet*", vous pouvez vérifier le solde de votre portefeuille. Notez qu'Alby Hub met automatiquement en réserve 354 sats lors du premier paiement. Pour chaque canal Lightning que vous ouvrez par la suite, Alby Hub constituera automatiquement une réserve équivalente à 1% des capacités du canal. Cette réserve est une mesure de sécurité qui permet à votre nœud de récupérer les fonds du canal en cas de tentative de fraude par votre pair. C'est pourquoi, bien que j'aie envoyé 120 000 sats, seul 119 646 sats sont affichés sur mon solde.

![ALBY HUB](assets/fr/33.webp)

## Déposer des bitcoins onchain

Pour avoir des liquidités sortantes qui vous permettront d'effectuer des paiements, vous pouvez également ouvrir un canal vous-même. Pour cela, vous aurez besoin de bitcoins onchain dans votre portefeuille.

Depuis l'onglet "*Node*", cliquez sur "*Deposit*".

![ALBY HUB](assets/fr/34.webp)

Envoyez des bitcoins à l'adresse qui s'affiche. Cette adresse est dérivée de votre phrase de récupération que vous avez sauvegardée précédemment.

![ALBY HUB](assets/fr/35.webp)

J'ai envoyé 72 000 sats. Ils sont maintenant visibles dans "*Savings Balance*", qui regroupe tous les fonds que je possède onchain, et non sur Lightning.

![ALBY HUB](assets/fr/36.webp)

## Ouvrir un canal Lightning

Maintenant que vous disposez de fonds onchain, vous pouvez ouvrir un nouveau canal Lightning. Il est conseillé d'ouvrir plusieurs canaux, avec des montants suffisants pour assurer que vous puissiez toujours effectuer des paiements sans contrainte. La plupart des LSP (*Lightning Service Providers*) demandent un minimum de 150 000 sats pour ouvrir un canal avec vous.

Dans l'onglet "*Node*", cliquez sur "*Open Channel*".

![ALBY HUB](assets/fr/37.webp)

Sélectionnez la taille de votre canal. Je vous recommande de ne pas ouvrir de canaux trop petits, tout en gardant à l'esprit que c'est un nœud Lightning et que la machine hébergeant vos clés n'offre pas le même niveau de sécurité qu'un hardware wallet. Soyez donc prudents avec les montants que vous choisissez de bloquer.

![ALBY HUB](assets/fr/38.webp)

Dans le menu "*Advanced Options*", vous avez la possibilité de choisir avec quel LSP ouvrir votre canal, ou d'entrer manuellement un autre nœud Lightning.

![ALBY HUB](assets/fr/39.webp)

Cliquez ensuite sur "*Open Channel*".

![ALBY HUB](assets/fr/40.webp)

Patientez pendant que l'ouverture de votre canal est confirmée onchain.

![ALBY HUB](assets/fr/41.webp)

Votre nouveau canal apparaîtra désormais dans l'onglet "*Node*".

![ALBY HUB](assets/fr/42.webp)

## Connecter une application de dépense

Maintenant que vous disposez d'un nœud Lightning fonctionnel, vous pouvez l'utiliser pour recevoir et dépenser des sats au quotidien. Bien que l'interface web d'Alby Hub soit pratique pour gérer votre nœud, elle n'est pas idéale pour effectuer rapidement des transactions en déplacement. Pour cela, nous allons utiliser une application de wallet Lightning installée sur notre smartphone.

Dans ce tutoriel, je vous recommande d'opter pour Alby Go, qui est très simple d'utilisation, mais vous pouvez également utiliser d'autres applications compatibles comme Zeus.

![ALBY HUB](assets/fr/43.webp)

Pour installer Alby Go, rendez-vous sur le magasin d'applications de votre appareil :
- [Pour Android](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Pour Apple](https://apps.apple.com/us/app/alby-go/id6471335774).

![ALBY HUB](assets/fr/44.webp)

Les utilisateurs Android peuvent aussi installer l'application via le fichier `.apk` [disponible sur le GitHub d'Alby](https://github.com/getAlby/go/releases).

![ALBY HUB](assets/fr/45.webp)

Au lancement de l'application, cliquez sur "*Connect Wallet*".

![ALBY HUB](assets/fr/46.webp)

Dans votre Alby Hub, sous l'onglet "*Connections*", cliquez sur "*Add Connection*".

![ALBY HUB](assets/fr/47.webp)

Nommez cette connexion pour l'identifier facilement dans votre Hub, et sélectionnez les permissions que vous souhaitez accorder à l'application. Dans mon cas, je choisis "*Full Access*" pour avoir un accès total aux fonds de mon nœud Lightning depuis mon smartphone, mais vous pouvez également limiter l'accès par un budget maximal, sélectionner les fonctionnalités autorisées, ou fixer une date d'expiration pour ces permissions. Une fois la configuration terminée, cliquez sur "*Next*".

![ALBY HUB](assets/fr/48.webp)

Alby Hub générera alors un secret pour établir la connexion.

![ALBY HUB](assets/fr/49.webp)

Retournez sur l'application Alby Go, scannez le QR code ou collez le secret.

![ALBY HUB](assets/fr/50.webp)

Cliquez sur "*Finish*".

![ALBY HUB](assets/fr/51.webp)

Vous avez maintenant accès à distance à votre nœud Lightning depuis votre smartphone, ce qui facilite les dépenses et les réceptions de sats en déplacement au quotidien.

![ALBY HUB](assets/fr/52.webp)

Si nécessaire, vous pouvez gérer les autorisations de cette connexion directement sur Alby Hub en cliquant dessus.

![ALBY HUB](assets/fr/53.webp)

Pour recevoir des sats, cliquez simplement sur "*Receive*".

![ALBY HUB](assets/fr/54.webp)

Modifiez le montant et la description de l'invoice en cliquant sur "*Invoice*".

![ALBY HUB](assets/fr/55.webp)

Faites-vous payer l'invoice pour recevoir des sats.

![ALBY HUB](assets/fr/56.webp)

Pour envoyer des sats, cliquez sur "*Send*".

![ALBY HUB](assets/fr/57.webp)

Scannez l'invoice que vous souhaitez payer.

![ALBY HUB](assets/fr/58.webp)

Cliquez ensuite sur "*Pay*".

![ALBY HUB](assets/fr/59.webp)

Votre transaction est confirmée.

![ALBY HUB](assets/fr/60.webp)

En cliquant sur la petite flèche, vous pouvez accéder à votre historique de transactions.

![ALBY HUB](assets/fr/61.webp)

Ces transactions sont également visibles sur votre Alby Hub.

![ALBY HUB](assets/fr/62.webp)

## Personnaliser son adresse Lightning

Alby vous offre la possibilité de disposer d'une adresse Lightning. Elle vous permet de recevoir des paiements sur votre nœud sans devoir générer manuellement une invoice à chaque fois. Par défaut, Alby vous attribue une adresse Lightning, mais vous pouvez la personnaliser. Connectez-vous à votre compte Alby en ligne, cliquez sur votre nom en haut à droite, puis sélectionnez "*Settings*".

![ALBY HUB](assets/fr/63.webp)

Naviguez jusqu'au menu "*Lightning Address*".

![ALBY HUB](assets/fr/64.webp)

Modifiez votre adresse, puis confirmez en cliquant sur "*Update your lightning address*".

![ALBY HUB](assets/fr/65.webp)

Attention, une fois modifiée, votre ancienne adresse ne vous appartient plus. Assurez-vous donc de ne plus y faire envoyer des sats.

Et voilà, vous savez maintenant comment utiliser Lightning avec votre propre nœud à l'aide de l'outil Alby Hub. Si vous avez trouvé ce tutoriel utile, je vous serais très reconnaissant de mettre un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci beaucoup !

Pour comprendre en détail tous les mécanismes de Lightning que nous avons manipulés dans ce tutoriel, je vous conseille vivement de découvrir notre formation gratuite sur le sujet :

https://planb.network/courses/lnp201
