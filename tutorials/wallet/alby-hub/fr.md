---
name: Alby Hub
description: Comment lancer facilement son propre nœud Lightning ?
---
![cover](assets/cover.webp)

Alby Hub est le tout dernier logiciel proposé par Alby, l'entreprise qui produit la célèbre extension web Lightning. Alby Hub est essentiellement une interface permettant de gérer un nœud Lightning de manière facile.

Dans ce tutoriel, je vous propose de découvrir comment l'utiliser de différentes manières, et comment le connecter à Alby Go, l'application mobile d'Alby qui vous permettra de dépenser vos sats en déplacement tout en restant à 100% souverain sur vos fonds.

01

## C'est quoi Alby Hub ?

En 2024, Alby a annoncé prendre un tournant. Depuis plusieurs années, ils fournissent divers outils en lien avec Bitcoin et le Lightning Network, et notamment la célèbre extension Alby, qui permettait de disposer d'un portefeuille Lightning custodial ou non. Ce service de wallet custodial partagé sera prochainement arrêté car Alby souhaite passer sur des logiciel et service en self-custody. Alby Hub représente le nouvel outil central de la galaxy Alby, qui va vous permettre de gérer votre propre noeud Lighnting, pour lequel vous possédez les clés, mais de manière facile.

Alby Hub est un outil particulièrement intéressant, car il peut-être très utile pour tout le monde en fonction de la forme choisie. Pour les débutants, il permet de lancer un vrai nœud Lightning de manière simple sans avoir gérer toutes la complexité. Pour les utilisateurs intermédiaires et avancés, il fournit une interface pour gérer un nœud Lightning avec des options avancées.

En fonction de votre utilisation, votre Alby Hub pourra ainsi prendre différentes formes. Concrètement, il existe principalement 4 options pour utiliser Alby Hub :

- **Alby Hub Cloud :**
La première option, qui est plutôt destinée aux débutants, est celle du cloud d'Alby. Cette option vous permet de déployer un nouveau nœud Lightning directement sur un serveur géré par Alby, et de le gérer depuis votre interface Alby Hub. Avec cette option, vous n'avez pas besoin de gérer de serveur, puisque c'est Alby qui s'en occupe, mais vous restez tout de même souverain sur vos fonds, car Alby n'a pas directement accès à vos clés. Attention tout de même, cette option n'offre pas les mêmes garanties en termes de sécurité qu'une option self-hosted. En effet, vos clés sont chiffrées à l'aide d'un mot de passe (dont nous allons parler plus loin), mais pour que le nœud fonctionne, elles doivent être conservées déchiffrées en RAM sur le serveur. Cela signifie qu'en théorie, toute personne avec un accès physique au serveur pourrait potentiellement accéder à vos clés. Cette option est donc un compromis intéressant, mais il est tout même important d'exposer les risques.

Le gros avantage de cette option est qu'elle vous permet de disposer d'un vrai nœud Lightning disponible 24h/24 et 7j/7, sans avoir à héberger le noeud. La gestion est facilitée à distance grâce à l'outil Alby Hub. L'avantage de cette option est également que les sauvegardes de votre noeud Lightning sont facilitées par rapport aux options self-hosted, avec lesquelles vous devriez vous même gérer la sauvegarde de tous vos canaux Lightning.

Alby propose ce service de gestion de serveur pour 21 000 sats par mois (prix relevé en décembre 2024, a peut-être évolué depuis, [vérifier sur leur page de prix](https://albyhub.com/#pricing)). Votre abonnement est automatiquement prélevé directement sur votre noeud via une invoice Lightning émise par Alby. Ce prélèvement automatique est rendu possible par une connexion NWC, qui, pour faire simple, dit à votre nœud qu'il doit automatiquement payer les invoice d'Alby correspondant à l'abonnement.

- **Alby Hub avec un nœud déjà existant :**
Si vous disposez déjà d'un nœud Lightning hébergé par exemple sur un node-in-box Umbrel ou Start9, vous pouvez utiliser Alby Hub comme une interface de gestion de votre noeud. Si vous souhaitez disposer d'options plus avancées que l'interface de base de votre noeud Lightning, Alby Hub est une excellente option. Elle vous permettra de gérer facilement votre noeud, de connecter différentes app en lien avec Bitcoin, ou encore de disposer d'une adresse Lightning.

- **Alby Hub en local :**
Il est également possible d'installer directement Alby Hub sur votre PC en local. Dans ce cas, votre noeud Lightning sera sur votre PC, ce qui signifie que vous devrez le laisser allumer en continue si vous souhaitez y accéder à distance et utiliser votre noeud. C'est pour cette raison que cette option est selon moi moins pertinente que les deux précédentes, mais en fonction de votre situation personelle, elle peut vous intéresser.

- **Alby Hub avec un serveur personnel :**
Enfin, si vous êtes un utilisateur avancé, vous pouvez déployer facilement Alby Hub sur votre propre serveur avec une simple commande. Nous n'allons pas en parler dans ce tutoriel, mais vous pouvez retrouver toutes les instructions spécifique à votre type de serveur [sur le GitHub d'Alby](https://github.com/getAlby/hub?tab=readme-ov-file#docker).

Dans ce tutoriel, nous allons principalement nous intéresser à l'utilisation de l'interface, donc vous pouvez le suivre quelle que soit l'option choisie ci-dessus. Je vais vous montrer comment créer votre compte et choisir l'option cloud payante. Pour la version sur Umbrel ou Start9, il suffit d'installer l'application depuis le store, puis vous pourrez suivre le tutoriel de la même façon.

02

Pour la version locale sur un ordinateur, [il suffit de télécharger et d'installer le logiciel en fonction de votre système d'exploitation](https://github.com/getAlby/hub/releases), puis vous pourrez également suivre le reste du tutoriel de la même manière.

03

## Créer un compte Alby

La première étape est de créer un compte Alby. Ce n'est pas obligatoire pour utiliser Alby Hub, mais ça vous permet de bénéficier d'un maximum d'options, notamment la possibilité d'avoir une adresse Lightning.

Rendez-vous sur [le site officiel d'Alby](https://getalby.com/), puis cliquez sur le bouton "Create Account".

04

Renseignez un pseudo et une adresse email, puis cliquez sur "Sign up". Cette adresse email sera utilisée pour vous connecter à votre compte par la suite.

05

Renseignez le code de vérification reçu par email.

06

Une fois connecté sur votre compte en ligne, cliquez sur le bouton "Continue".

07

Cliquez une nouvelle fois sur "Continue".

08

## L'option d'hébergement cloud

Vous devrez ensuite choisir entre une option self-hosted, c'est à dire avec un noeud Lightning hébergé sur une machine que vous maîtrisez, ou bien l'option payante avec le cloud d'Alby. Je vais d'abbord vous expliquer comment faire avec l'option Cloud (attention, cette option est payante, voir la partie précédente).

Cliquez sur le bouton "Upgrade".

09

Validez en cliquant sur le bouton "Subscribe Now".

10

Cliquez sur le bouton "Launch Alby Hub"

11

Patientez quel instants le temps de création de votre noeud.

12

Et voilà, votre Alby Hub a bien été créé. Dans la paortie suivante, je vais expliquer comment l'installer sur un noued déjà existant. Vous pouvez sauter cette partie et passer directement à la suivante pour configurer votre noeud.

13

## L'option d'auto-hébergement

Si vous préférez utiliser Alby Hub comme une interface pour votre noeud Lighnting déjà existant, vous pouvez l'installer sur un serveur, en local sur votre ordinateur ou bien avec un node-in-box (Umbrel ou Start9). Dans ce cas, l'utilisation d'Alby Hub est gratuite. C'est cette dernière option du node-in-box que nous allons voir ensemble, car je trouve moins intéressant l'option de déploiement sur serveur qui, si vous n'avez pas acès physiquement au serveur, présente les mêmes risques que la version cloud, et pour la version locale sur PC, je trouve que c'est inadapté dans la plupart des cas. Voyons ensemble comment configurer cela sur Umbrel (sur Start9 les étapes sont exactement les mêmes). Avant de commencer, vous aurez évidemment besoin d'avoir un noeud LND déjà configuré.

Connectez-vous sur votre interface Umbrel et rendez-vous dasn le magasin d'applications.

14

Rechezchez l'application "Alby Hub".

15

Installez-la sur votre noeud.

16

Et voilà, votre interface Alby Hub est prête. Vous pouvez suivre le reste du tutoriel de la même manière qu'avec l'interface cloud, à la différence près que vous n'aurez pas accès aux options qui dépendent de la version payante. Aussi, vos clés ne sont pas conservées sur les serveurs d'Alby contrairement à la version cloud, mais en local sur votre noeud.

17

## Lancer Alby Hub

Cliquez sur le bouton "Get Started".

18

Alby Hub vous demande ensuite de choisir un mot de passe. Attention, ce mot de passe est d'une grande importance ! Il sera utiliser pour chiffrer votre portefeuille. En effet, avec la version cloud payante, vos clés sont conservées sur le serveur d'Alby. Elles sont chiffrées à l'aide de ce mot de passe que vous êtes le seul à connaitre, puis déchiffrées et conservées uniquement en RAM pour signer lorsque nécessaire.

Vous devez donc absolument choisir un mot de passe fort. Quiconque en possession de ce mot de passe peut potentiellement accéder à votre nœud. Vous devez également veiller à en faire une ou plusieurs sauvegardes physiques sur un morceau de papier (ou un morceau de métal pour plus de sécurité). En effet, si jamais vous perdez accès à ce mot de passe, il sera impossible de retrouver l'accès à vos bitcoins. Alby n'a pas de connaissance de ce mot de passe et ne peut pas le réinitialiser. Donc si vous le perdez, vous perdez vos bitcoins.

Une fois le mot de passe fort entré et sauvegardé soigneusement, cliquez sur le bouton "Create Password"

19

Vous avez maintenant accès à votre nœud Lightning.

20

Avant toute chose, il faut aller chercher sa phrase de récupération pour en faire une sauvegarde. C'est à partir de cette phrase que vos clés sont dérivées. Elle vous permet donc de récupérer l'accès à votre wallet onchain, et, en plus du dernier état de vos canaux, de retrouver l'accès avec vos sats sur Lightning. Pour ce faire, cliquez sur "Settings".

21

Puis allez dans l'onglet "Backup".

22

Entrez votre mot de passe pour y accéder.

23

Vous aurez ensuite accès à votre phrase de récupération de 12 mots. Faites en une ou plusieurs sauvegardes physiques sur un bout de papier ou un bout de métal et stockez là en lieu sûr.

24

Ensuite, vous pouvez cocher la case pour confirmer que vous avez bien sauvergardé la phrase et cliquer sur le bouton "Continue".

25

## Comment récupérer l'accès à ses bitcoins ?

Avant d'envoyer des fonds sur votre nœud, il est toujours important de savoir précisément comment les récupérer en cas de problème, et quelles informations sont nécessaires. Le processus de récupération varie en fonction de ce que vous souhaitez récupérer et en fonction de la manière dont vous hébergez votre nœud.

Pour les utilisateurs du cloud payant, pour récupérer l'accès à l'intégralité de vos bitcoins, vous aurez besoin de trois choses :
- Votre phrase de récupération ;
- Votre mot de passe (celui du nœud) ;
- Un accès à votre compte Alby sur lequel vous pouvez récupérer le dernier état de vos canaux Lightning.

Ces trois informations sont essentielles. Si l'une d'elle venait à manquer, vous ne pourriez pas retrouver l'accès à vos bitcoins.

Pour les utilisateurs qui hébergent leurs noeuds eux-mêmes, le processus de récuépration est le même que pour n'importe quel noeud Lightning, ilvous faudra :
- Votre phrase de récupération ;
- Le dernier état de vos canaux Lightning. Pour cette information, vous avez d'ailleurs [une option sur Umbrel](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) pour la chiffrer puis la sauvegarder de manière dynamique et anonyme via Tor.

## Acheter son premier canal Lightning

Vous pouvez ensuite simplement suivre les indications d'Alby Hub. Cliquez sur le bouton pour ouvrir votre premier canal et disposer de liquidités entrantes.

26

Cliquez sur "Open Channel". Si vous n'en avez pas réellement besoin et si vous ne souhaitez pas être un nœud de routage, je vous conseille de faire uniquement des canaux privés.

27

Alby Hub génère une invoice que vous devez payer. Cela permet de régler les frais de transaction nécessaires à l'ouverture de votre canal, en plus des frais de service du LSP (*Lightning Service Provider*) qui va ouvrir un canal vers votre nœud pour vous permettre de revoir immédiatement des paiements.

28

Une fois l'invoice réglée, vous disposez dorénavant d'un premier canal foncitonnel.

29

En allant dans l'onglet "Node", vous pouvez voir que vous disposez de liquidités entrantes, ce qui vous permet déjà de recevoir des paiements sur Lightning.

30

Pour ce faire, vous pouvez cliquer sur l'onglet "Wallet" puis sur le bouton "Receive".

31

Précisez un montant et ajoutez une description si vous le souhaitez, puis cliquez sur le bouton "Create Invoice".

32

On peut voir que j'ai bien reçu mon premier paiement pour 120 000 sats.

33

En retournant dans l'onglet "Wallet", vous pourrez voir le solde de votre portefeuille. Attention, lors du premier paiement, Alby Hub mettra automatiquement en réserve 354 sats. Par la suite, pour chaque canal Lightning que vous ouvrirez, vous devrez constituer une réserve égale à 1% des capacités du canal. Cette réserve est un mécanisme de sécurité qui permet à votre nœud de pouvoir récupérer les fonds du canal en cas de tentative de triche de la part de votre pair. C'est pour cela que dans mon exemple j'ai envoyé 120 000 sats, mais il n'y a d'affiché sur mon solde que 119 646 sats.

34

## Déposer des bitcoins onchain

Pour disposer de liquidités sortantes qui vous permettront d'effectuer des paiements, vous pouvez également ouvrir vous-même un canal. Pour ce faire, vous allez avoir besoin de bitcoins onchain sur votre portefeuille.

Pour recevoir des bitcoins onchain, depuis l'onglet "Node", cliquez sur le bouton "Deposit".

35

Envoyez une somme de bitcoins à l'adresse affichée. Cette adresse est dérivée depuis votre phrase récupération que vous avez sauvegardée tout à l'heure.

36

J'y ai envoyé 72 000 sats. On peut voir qu'ils apparaissent désormais dans mon solde "Savings Balance", qui désigne tous les fond que je possède onchain, et non pas sur Lightning.

37

## Ouvrir un canal Lightning

Maintenant que vous avez des fonds onchain, vous allez pouvoir ouvrir un nouveau canal Lightning. Je vous conseille d'en ouvrir quelques uns, avec des sommes pas trop petites, afin d'être sur de toujours pouvoir faire des paiements sans être bloqué. La plupart des LSP qui vous sont proposés demandent au minimum 150 000 sats pour ouvrir un canal avec vous.

Dans l'onglet "Node" cliquez sur le bouton "Open Channel".

38

Choisissez la taille de votre canal.

39

Dans le menu "Advanced Options", vous pouvez choisir avec quel ISP vous allez ouvrir votre canal, ou bien vous pouvez également renseigner un autre nœud Lightning librement.

40

Puis cliquez sur le bouton "Open Channel".

41

Patientez le temps que l'ouverture de votre canal soit confirmé onchain.

42

Vous pouvez maintenant voir votre nouveau canal dans l'onglet "Node".

## Connecter une application de dépense

Maintenant que vous disposez d'un nœud Lightning fonctionnel, vous pouvez l'utiliser pour recevoir et dépenser des sats au quotidien. Si l'interface web d'Alby Hub est pratique pour gérer son nœud, elle n'est pas forcément adaptée pour réaliser des transactions rapidement en déplacement. Pour ce faire, nous allons utiliser une application d'interface de wallet Lightning installée sur notre smartphone.

Dans ce tutoriel, je vous propose d'utiliser Alby Go qui est très simple à utiliser, mais vous pouvez également connecter d'autres applications comme Zeus par exemple.

43

Rendez-vous sur votre store d'applications :
- [Pour Android](https://play.google.com/store/apps/details?id=com.getalby.mobile) ;
- [Pour Apple](https://apps.apple.com/us/app/alby-go/id6471335774).

44

Pour les utilisateurs Android, vous avez aussi la possibilité d'installer l'application via le fichier `.apk` [disponible sur le GitHub d'Alby](https://github.com/getAlby/go/releases).

45







Et voilà, vous savez maintenant comment utiliser Lightning avec votre propre nœud à l'aide de l'outil Alby Hub.

Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de mettre un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci beaucoup !

Pour comprendre en détail tous les mécanismes de Lightning que nous avons manipulés dans ce tutoriel, je vous conseille vivement de découvrir notre formation gratuite sur le sujet :

https://planb.network/courses/lnp201
