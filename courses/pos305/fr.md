---
name: Maîtriser BTC Pay Server
goal: Configurer une instance BTC Pay Server pour une entreprise locale
objectives:
- Comprendre les fondamentaux du rôle de BTCPay Server dans le traitement des paiements
- Maîtriser le fonctionnement interne du processus de configuration de BTCPay Server
- Déployer BTCPay Server sur des environnements cloud et basés sur des nœuds
- Devenir opérateur de BTC Pay Server
---
# Voyage vers la Souveraineté Financière

La confiance est fragile, surtout lorsqu'il s'agit d'argent. Ce cours d'introduction vous guide à travers BTCPay Server, un outil puissant qui vous permet d'accepter des paiements Bitcoin sans dépendre de tiers. Vous apprendrez les fondamentaux pour devenir un opérateur BTCPay Server

Créé par Alekos et Bas, et adapté par melontwist et asi0, ce cours révèle comment les individus et les entreprises construisent des alternatives aux systèmes de paiement traditionnels. Que vous soyez curieux à propos du Bitcoin ou prêt à gérer des infrastructures de paiement pour des entreprises, vous découvrirez des compétences pratiques qui remettent en question le statu quo. Prêt à explorer ce à quoi ressemble réellement l'indépendance financière ?
+++
# Introduction


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Aperçu du cours


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


Bienvenue au cours POS 305 sur le serveur BTCPay !


L'objectif de cette formation est de vous apprendre à installer, configurer et utiliser BTCPay Server au sein de votre entreprise ou organisation. BTCPay Server est une solution open-source qui vous permet de traiter les paiements Bitcoin de manière autonome, sécurisée et rentable. Ce cours est principalement destiné aux utilisateurs avancés qui souhaitent maîtriser l'auto-hébergement de BTCPay Server pour une intégration complète dans leurs opérations quotidiennes.


**Section 1 : Introduction au serveur BTCPay

Nous commencerons par une présentation générale de BTCPay Server, y compris l'écran de connexion, la gestion des comptes utilisateurs et la création d'une nouvelle boutique. Cette introduction vous aidera à comprendre le Interface de BTCPay Server et à saisir les fonctionnalités de base nécessaires pour commencer à utiliser cet outil.


**Section 2 : Introduction à la sécurisation des clés Bitcoin**

La sécurité de vos fonds Bitcoin est très importante. Dans cette section, nous explorerons la génération de clés cryptographiques, l'utilisation de portefeuilles matériels pour sécuriser ces clés, et comment interagir avec vos clés via le serveur BTCPay. Vous apprendrez également comment configurer un serveur BTCPay Lightning Wallet pour optimiser vos transactions.


**Section 3 : Serveur BTCPay Interface**

Cette partie vous guidera à travers l'utilisateur de BTCPay Server Interface. Vous apprendrez à naviguer dans le tableau de bord, à configurer les paramètres de la boutique et du serveur, à gérer les paiements et à profiter des plugins intégrés. L'objectif est de vous fournir les outils nécessaires pour personnaliser votre installation en fonction de vos besoins spécifiques.


**Section 4 : Configurer le serveur BTCPay**

Enfin, nous nous concentrerons sur l'installation pratique de BTCPay Server dans différents environnements. Que vous utilisiez LunaNode, Voltage ou un nœud Umbrel, vous apprendrez les étapes essentielles pour déployer et configurer votre serveur BTCPay, en tenant compte des spécificités de chaque environnement.


Prêt à maîtriser le serveur BTCPay et à développer votre activité ? Allons-y !


## Acclamation critique pour le serveur Bitcoin et BTCPay de l'auteur


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


Commençons par comprendre ce qu'est le serveur BTCPay et ses origines. Nous accordons de l'importance à la transparence et à certaines normes pour instaurer la confiance dans l'espace Bitcoin.

Un projet dans l'espace a brisé ces valeurs. Le développeur principal de BTCPay Server, Nicolas Dorier, l'a pris personnellement et a fait la promesse de les rendre obsolètes. Nous voici, bien des années plus tard, en train de travailler chaque jour à ce futur, entièrement open-source.


> C'est un mensonge, ma confiance en vous est rompue, je vous rendrai obsolète.
> Nicolas Dorier

Après les mots prononcés par Nicolas, il était temps de commencer à construire. Une quantité importante de travail a été consacrée à ce que nous appelons aujourd'hui BTCPay Server. De plus en plus de personnes ont voulu contribuer à cet effort. Les plus connus sont r0ckstardev, MrKukks, Pavlenex, et le premier marchand à utiliser le logiciel, astupidmoose.


Qu'entend-on par "open source" et qu'est-ce qui entre dans la composition d'un tel projet ?


FOSS est l'acronyme de Free & Open-Source Software (logiciel libre et gratuit). Le premier terme fait référence aux conditions qui permettent à quiconque de copier, modifier et même distribuer des versions (même à des fins lucratives) du logiciel. Le second fait référence au partage ouvert du code source, encourageant le public à y contribuer et à l'améliorer.

Cela attire des utilisateurs expérimentés qui sont enthousiastes à l'idée de contribuer au logiciel qu'ils utilisent déjà et dont ils tirent de la valeur, ce qui s'avère en fin de compte plus efficace en termes d'adoption que les logiciels propriétaires. Elle est conforme à l'éthique de Bitcoin selon laquelle "l'information aspire à être libre" Il rassemble des personnes passionnées qui forment une communauté et il est tout simplement plus amusant. Comme Bitcoin, le logiciel libre est inévitable.


### Avant de commencer


Ce cours se compose de plusieurs parties. Plusieurs seront prises en charge par votre enseignant, les environnements de démonstration auxquels vous aurez accès, un serveur hébergé pour vous, et éventuellement un nom de domaine. Si vous suivez ce cours de manière indépendante, sachez que les environnements étiquetés comme DEMO ne vous seront pas accessibles.

NB. Si vous suivez ce cours dans une salle de classe, les noms des serveurs peuvent varier en fonction de la configuration de la salle de classe. Les variables dans les noms de serveurs peuvent être différentes pour cette raison.


### Structure du cours


Chaque chapitre comporte des objectifs et des évaluations des connaissances. Dans ce cours, nous couvrirons chacun de ces éléments et fournirons un résumé des caractéristiques clés à la fin de chaque bloc de leçons (c.-à-d. chapitre). Des illustrations sont utilisées pour fournir un retour d'information visuel et renforcer les concepts clés d'un point de vue visuel. Des objectifs sont fixés au début de chaque bloc de leçons. Ces objectifs vont au-delà d'une liste de contrôle. Ils vous guident vers un nouvel ensemble de compétences. Les évaluations des connaissances sont progressivement plus difficiles, à mesure que la configuration de votre serveur BTCPay est terminée.


### Qu'est-ce que les étudiants reçoivent avec le cours ?


Avec le cours sur le serveur BTCPay, un étudiant peut comprendre les principes de base, techniques et non techniques, de Bitcoin. La formation approfondie à l'utilisation de Bitcoin par le biais de BTCPay Server permettra aux étudiants d'exploiter leur propre infrastructure Bitcoin.


### Adresses web importantes ou possibilités de contact


La Fondation BTCPay Server, qui a permis à Alekos et Bas de rédiger ce cours, se trouve à Tokyo, au Japon. La fondation BTCPay Server peut être contactée via le site web indiqué.



- https://foundation.btcpayserver.org
- Rejoignez les canaux de discussion officiels : https://chat.btcpayserver.org


## Introduction à Bitcoin


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Comprendre Bitcoin grâce à un exercice en classe


Il s'agit d'un exercice en classe, donc si vous suivez ce cours vous-même, vous ne pouvez pas le réaliser, mais vous pouvez quand même faire cet exercice. Pour réaliser cette tâche, un minimum de 9 à 11 personnes est nécessaire.


L'exercice commence après le visionnage de l'introduction "How Bitcoin and the Blockchain works" de la BBC.


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


Cet exercice requiert un minimum de neuf participants. Cet exercice vise à fournir une compréhension physique du fonctionnement de Bitcoin. En jouant chaque rôle dans le réseau, vous apprendrez de manière interactive et ludique. Cet exercice n'implique pas Lightning Network.


### Exemple : Besoin de 9 / 11 personnes


Les rôles sont les suivants :



- 1 Client
- 1 Marchand
- 7 à 9 nœuds Bitcoin


**La configuration est la suivante:**


Les clients achètent un produit dans le magasin avec Bitcoin.


**Scénario 1 - Système bancaire traditionnel**



- Mise en place :
  - Voir les diagrammes/explications dans le Figjam - [Schéma de l'activité](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0) ci-joint.
  - Demandez à trois élèves volontaires de jouer les rôles du client (Alice), du commerçant (Bob) et de la banque.
- Jouez la séquence des événements :
  - Client - il parcourt le magasin en ligne et trouve un article à 25 $, qu'il désire, et informe le commerçant qu'il souhaite l'acheter
  - Marchand - demande le paiement.
  - Le client envoie les informations relatives à sa carte au commerçant
  - Le commerçant transmet des informations à la Banque (identifiant à la fois sa propre identité et l'identité/information), demandant le paiement de
  - La banque recueille des informations sur le client et le commerçant (Alice et Bob) et vérifie que le solde du client est suffisant.
  - Déduit 25 $ du compte de Alice, ajoute 24 $ au compte de Bob, prend 1 $ pour le service
  - Le commerçant reçoit le feu vert de la banque et expédie l'article au client.
- Commentaires :
  - Bob et Alice doivent avoir une relation avec une banque.
  - La banque recueille des informations d'identification sur Bob et Alice.
  - Bank subit une coupure.
  - Il faut faire confiance à la banque pour qu'elle conserve à tout moment l'argent de chaque participant.


**Scénario 2 - Système Bitcoin**



- Mise en place :
  - Voir les diagrammes/explications dans le Figjam - [Schéma de l'activité](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0) ci-joint.
  - Remplacer la banque par neuf élèves qui joueront le rôle d'un ordinateur (Bitcoin nœuds/mineurs) dans un réseau destiné à remplacer la banque.
- Chacun des neuf ordinateurs dispose d'un historique complet de toutes les transactions passées (ce qui permet d'obtenir des soldes exacts sans falsification), ainsi que d'un ensemble de règles :
  - Vérifier que la transaction est correctement signée (thekeyfitsthelock)
  - Diffuser et recevoir des transactions valides aux pairs du réseau, rejeter les transactions non valides (y compris celles qui tentent de dépenser deux fois les mêmes fonds)
- Mise à jour/ajout périodique des enregistrements avec les nouvelles transactions reçues de l'ordinateur "aléatoire", à condition que tous les contenus soient valides (remarque : nous ignorons, pour l'instant, la composante Proof of Work de tout ceci, pour des raisons de simplicité), sinon nous les rejetons et continuons comme avant jusqu'à ce que le prochain ordinateur "aléatoire" envoie une mise à jour
  - Le montant approprié était récompensé si le contenu était valide.
- Jouez la séquence des événements :
  - Client - il parcourt le magasin en ligne et trouve un article à 25 $ qu'il veut, et informe le commerçant qu'il souhaite l'acheter
  - Le marchand demande le paiement en envoyant au client une Invoice/Address à partir de sa Wallet.
  - Le client effectue une transaction (envoi de 25 $ de BTC à un Address fourni par le marchand) et la diffuse sur le réseau Bitcoin.
- Ordinateurs - reçoivent la transaction et la vérifient :
  - Il y a au moins 25 $ de BTC dans le Address envoyé de
  - La transaction est signée correctement ("déverrouillée" par le client)
  - Si ce n'est pas le cas, la transaction ne sera pas propagée dans le réseau, et si c'est le cas, elle se propagera et sera mise en attente.
  - Les commerçants peuvent vérifier que la transaction est en attente.
- Un ordinateur est choisi "au hasard" pour proposer de finaliser la transaction proposée en diffusant "un bloc" la contenant ; si elle est vérifiée, il recevra une récompense en BTC.
  - OPTIONNEL/AMÉLIORÉ - au lieu de sélectionner un ordinateur au hasard, simuler Mining en demandant aux ordinateurs de lancer des dés jusqu'à ce qu'un résultat prédéterminé se produise (par exemple, le premier à obtenir un double six est sélectionné)
  - Il peut également reproduire ce qui se passerait si deux ordinateurs gagnaient à peu près simultanément, ce qui entraînerait une scission en chaîne.
  - Les ordinateurs vérifient la validité, mettent à jour/ajoutent des enregistrements à leurs grands livres si les règles sont respectées et diffusent le bloc de transactions à leurs homologues.
  - L'ordinateur choisi au hasard reçoit une récompense pour avoir proposé un bloc valide.
  - La transaction des chèques du commerçant a été finalisée ; les fonds ont donc été reçus et l'article a été envoyé au client.
- Commentaires :
  - Notez qu'il n'était pas nécessaire d'avoir une relation bancaire préexistante.
  - Aucune tierce partie n'est nécessaire pour faciliter les choses ; le code et les mesures d'incitation les remplacent.
  - Aucune collecte de données par quiconque en dehors de la Exchange directe, et seule la quantité nécessaire doit être échangée entre les participants (par exemple, l'expédition de la Address).
  - Aucune confiance n'est requise entre les personnes (autres que le marchand qui envoie l'objet), comme pour un achat en espèces à bien des égards.
  - L'argent appartient directement aux individus.
  - Le Bitcoin Ledger est représenté en dollars pour plus de simplicité, mais en réalité, il s'agit de BTC.
  - Nous simulons la diffusion d'une seule transaction, mais en réalité, plusieurs transactions sont en attente dans le réseau, et les blocs comprennent des milliers de transactions à la fois. Les nœuds vérifient également qu'aucune transaction à double dépense n'est en attente (dans ce cas, j'écarterais toutes les transactions sauf une).
- Scénarios de tricherie :
  - Que se passe-t-il si le client ne dispose pas de 25 BTC ?
    - Ils ne pourraient pas créer la transaction car "déverrouiller" et "Ownership" sont la même chose, et les ordinateurs vérifient que la transaction est correctement signée ; dans le cas contraire, ils la rejettent
  - Que se passe-t-il si l'ordinateur choisi au hasard tente de "changer le Ledger" ?
    - Le bloc serait rejeté, car tous les autres ordinateurs disposent d'un historique complet et remarqueraient le changement, violant ainsi l'une de leurs règles.
    - L'ordinateur aléatoire ne recevrait pas de récompense et aucune transaction de son bloc ne serait finalisée.


## Évaluation des connaissances


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### KA Discussion en classe


Discutez des simplifications excessives faites lors de l'exercice en classe dans le cadre du deuxième scénario et décrivez plus en détail ce que fait le système Bitcoin.


### KA Révision du vocabulaire


Définir les termes clés suivants introduits dans la section précédente :



- Nœud
- Mempool
- Difficulté Cible
- Bloc


**Discuter en groupe de la signification de certains termes supplémentaires:**


Blockchain, transaction, double dépense, problème byzantin des généraux, Mining, Proof of Work (PoW), Hash fonction, Block reward, Blockchain, chaîne la plus longue, attaque à 51 %, sortie, verrouillage de la sortie, changement, satoshis, clé publique/privée, Address, cryptographie à clé publique, signature numérique, Wallet


# Présentation du serveur BTCPay


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## Comprendre l'écran de connexion de BTCPay Server


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### Travailler avec le serveur BTCPay


L'objectif de ce bloc de cours est d'acquérir une compréhension générale du logiciel BTCPay Server. Dans un environnement partagé, il est recommandé de suivre la démonstration de l'instructeur et de se référer au manuel de cours de BTCPay Server pour suivre le professeur. Vous apprendrez à créer une Wallet à l'aide de plusieurs méthodes. Les exemples incluent des configurations Hot Wallet et des portefeuilles matériels connectés via BTCPay Server Vault. Ces objectifs se déroulent dans l'environnement de démonstration, affiché et accessible par votre instructeur de cours.


Si vous suivez ce cours par vous-même, vous pouvez trouver une liste d'hôtes tiers à des fins de démonstration à l'adresse https://directory.btcpayserver.org/filter/hosts. Nous déconseillons fortement d'utiliser ces options tierces comme environnements de production ; cependant, elles servent à introduire l'utilisation de Bitcoin et de BTCPay Server.


En tant que stagiaire de BTCPay Server rockstar, vous avez peut-être déjà eu l'occasion de configurer un nœud Bitcoin. Ce cours est spécifiquement adapté à la pile logicielle de BTCPay Server.


De nombreuses options de BTCPay Server existent sous une forme ou une autre dans d'autres logiciels liés à Bitcoin Wallet.


### Ecran de connexion au serveur BTCPay


Lorsque vous êtes accueilli dans l'environnement de démonstration, il vous est demandé de vous "connecter" ou de "créer votre compte" Les administrateurs du serveur peuvent désactiver la fonction de création de nouveaux comptes pour des raisons de sécurité. Les logos et les couleurs des boutons de BTCPay Server peuvent être modifiés car BTCPay Server est un logiciel Open Source. Un hébergeur tiers peut mettre le logiciel en marque blanche et en modifier l'apparence complète.


![image](assets/en/001.webp)


### Fenêtre Créer un compte


La création de comptes sur le serveur BTCPay nécessite des chaînes Address valides pour l'email ; example@email.com serait une chaîne valide pour l'email.


Le mot de passe doit comporter au moins 8 caractères, y compris des lettres, des chiffres et des caractères. Après avoir défini le mot de passe une fois, vous devrez vérifier que le mot de passe est le même que celui qui a été saisi dans le premier champ de mot de passe.


Lorsque les champs Email et Mot de passe sont correctement remplis, cliquez sur le bouton "Créer un compte". L'adresse électronique et le mot de passe seront enregistrés sur l'instance du serveur BTCPay de l'instructeur.


![image](assets/en/002.webp)


**!Note!**


Si vous suivez ce cours de manière indépendante, la création de ce compte sera probablement effectuée sur un hôte tiers ; par conséquent, nous insistons à nouveau sur le fait que ces environnements ne doivent pas être utilisés comme des environnements de production, mais uniquement à des fins de formation.


### Création de compte par l'administrateur du serveur BTCPay


L'administrateur de l'instance de BTCPay Server peut également créer des comptes pour BTCPay Server. L'Administrateur de l'instance de BTCPay Server peut cliquer sur 'Paramètres du serveur' (1), cliquer sur l'onglet 'Utilisateurs' (2), et cliquer sur le bouton "+ Ajouter un utilisateur" (3) en haut à droite de l'onglet Utilisateurs. Dans l'Objectif (4.3), vous en apprendrez davantage sur le contrôle des comptes par l'administrateur.


![image](assets/en/003.webp)


En tant qu'administrateur, vous aurez besoin de l'adresse électronique de l'utilisateur Address et vous définirez un mot de passe standard. Il est recommandé à l'administrateur d'informer l'utilisateur qu'il doit changer ce mot de passe avant d'utiliser le compte pour des raisons de sécurité. Si l'administrateur ne définit pas de mot de passe et que le protocole SMTP a été configuré sur le serveur, l'utilisateur recevra un courriel contenant un lien d'invitation à créer son compte et à définir lui-même un mot de passe.


### Exemple


Si vous suivez le cours avec un instructeur, suivez le lien fourni par l'instructeur et créez votre compte dans l'environnement de démonstration. Assurez-vous que votre email Address et votre mot de passe sont sauvegardés en toute sécurité ; vous aurez besoin de ces identifiants de connexion pour le reste des objectifs de démonstration de ce cours.


Il se peut que votre instructeur ait recueilli l'email Address à l'avance et envoyé un lien d'invitation avant cet exercice. Si c'est le cas, vérifiez votre courrier électronique.


Si vous suivez le cours sans instructeur, créez votre compte en utilisant l'environnement de démonstration de BTCPay Server


https://Mainnet.demo.btcpayserver.org/login.


Ce compte ne doit être utilisé qu'à des fins de démonstration/formation et jamais à des fins professionnelles.


### Résumé des compétences


Dans cette section, vous avez appris ce qui suit :



- Comment créer un compte sur un serveur hébergé via le Interface.
- Comment un administrateur de serveur peut ajouter manuellement des utilisateurs dans les paramètres du serveur.


### Évaluation des connaissances


#### Examen conceptuel de l'AC


Donnez les raisons pour lesquelles l'utilisation d'un serveur de démonstration n'est pas une bonne idée pour la production.


## Gestion des comptes d'utilisateurs


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### Gestion des comptes sur le serveur de BTCPay


Une fois que le propriétaire d'une boutique a créé son compte, il peut le gérer dans le coin inférieur gauche de l'interface utilisateur de BTCPay Server. Sous le bouton Compte, il y a plusieurs paramètres de niveau supérieur.



- Mode sombre/clair.
- Masquer les informations sensibles.
- Gérer le compte.


![image](assets/en/004.webp)


### Mode sombre et mode clair


Les utilisateurs de BTCPay Server peuvent choisir entre une version de l'interface utilisateur en mode clair ou foncé. Les pages destinées aux clients ne changeront pas. Elles utilisent les paramètres préférés du client en ce qui concerne le mode sombre ou clair.


### Hide Sensitive Info Toggle (masquer les informations sensibles)


Le bouton Hide Sensitive Info offre une sécurité Layer simple et rapide. Lorsque vous devez utiliser votre serveur BTCPay, mais qu'il peut y avoir des gens qui regardent par-dessus votre épaule dans un espace public, activez le bouton Cacher les informations sensibles, et toutes les valeurs de BTCPay Server seront cachées. Il se peut que quelqu'un puisse regarder par-dessus votre épaule, mais il ne pourra plus voir les valeurs que vous traitez.


### Gérer le compte


Une fois le compte utilisateur créé, c'est ici que l'on peut gérer les mots de passe, le 2FA ou les clés API.


### Gérer le compte - Compte


En option, mettez à jour votre compte avec un email Address différent. Pour s'assurer que votre email Address est correct, le serveur BTCPay vous permet d'envoyer un email de vérification. Cliquez sur enregistrer si l'utilisateur définit un nouvel email Address et confirme que la vérification a fonctionné. Le nom d'utilisateur reste le même que l'email précédent.


Un utilisateur peut décider de supprimer l'ensemble de son compte. Pour ce faire, il suffit de cliquer sur le bouton "Supprimer" dans l'onglet "Compte".


![image](assets/en/005.webp)


**!Note!**


Après avoir changé l'adresse électronique, le nom d'utilisateur du compte ne changera pas. L'email Address donné précédemment restera le nom de connexion.


### Gérer le compte - Mot de passe


Un étudiant peut vouloir modifier son mot de passe. Il peut le faire en allant dans l'onglet Mot de passe. Il doit alors saisir son ancien mot de passe et peut le remplacer par un nouveau.


![image](assets/en/006.webp)


### Authentification à deux facteurs (2fa)


Pour limiter les conséquences d'un vol de mot de passe, vous pouvez utiliser l'authentification à deux facteurs (2FA), une méthode de sécurité relativement récente. Vous pouvez activer l'authentification à deux facteurs via le compte Gérer et l'onglet pour l'authentification à deux facteurs. Vous devez effectuer une deuxième étape après vous être connecté avec votre nom d'utilisateur et votre mot de passe.


Le serveur BTCPay prend en charge deux méthodes pour activer le 2FA : le 2FA basé sur une application (Authy, Google, Microsoft Authenticators) ou via des dispositifs de sécurité (FIDO2 ou LNURL Auth).


### Authentification à deux facteurs - basée sur une application


En fonction du système d'exploitation de votre téléphone portable (Android ou iOS), les utilisateurs peuvent choisir parmi les applications suivantes ;


1. Téléchargez un authentificateur à deux facteurs.


   - Authy pour [Android](https://play.google.com/store/apps/details?id=com.authy.authy) ou [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator pour [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) ou [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator pour [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) ou [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)

2. Après avoir téléchargé et installé l'application Authenticator.


   - Scanner le code QR fourni par le serveur BTCPay
   - Ou entrez manuellement la clé générée par le serveur BTCPay dans votre application Authenticator.

3. L'application Authenticator vous fournira un code unique. Entrez le code unique dans BTCPay Server pour vérifier la configuration, et cliquez sur Vérifier pour terminer le processus.


![image](assets/en/007.webp)


### Résumé des compétences


Dans cette section, vous avez appris ce qui suit :



- Les options de gestion de compte et les différentes façons de gérer un compte sur une instance de BTCPay Server.
- Comment mettre en place un 2FA basé sur une application.


### Évaluation des connaissances


#### Examen conceptuel de l'AC


Décrivez comment le 2FA basé sur une application permet de sécuriser votre compte.


## Création d'un nouveau magasin


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Créez votre assistant de magasin


Lorsqu'un nouvel utilisateur se connecte à BTCPay Server, l'environnement est vide et a besoin d'un premier magasin. L'assistant d'introduction de BTCPay Server donnera à l'utilisateur l'option de "Créer votre magasin" (1). Un magasin peut être considéré comme une maison pour vos besoins Bitcoin. Un nouveau nœud de BTCPay Server commencera par synchroniser le Bitcoin Blockchain (2). Selon l'infrastructure sur laquelle vous exécutez BTCPay Server, cela peut prendre de quelques heures à quelques jours. La version actuelle de l'instance est affichée dans le coin inférieur droit de l'interface utilisateur de BTCPay Server. Ceci est utile pour se référer lors du dépannage.


![image](assets/en/008.webp)


### Créez votre assistant de magasin


En suivant ce cours, vous commencerez par un écran légèrement différent de celui de la page précédente. Comme votre instructeur a préparé l'environnement de démonstration, le Bitcoin Blockchain a été synchronisé au préalable et, par conséquent, vous ne verrez pas l'état de synchronisation des nœuds.


Un utilisateur peut décider de supprimer l'ensemble de son compte. Pour ce faire, il suffit de cliquer sur le bouton "Supprimer" dans l'onglet "Compte".


![image](assets/en/009.webp)


**!Note!**


Les comptes BTCPay Server peuvent créer un nombre illimité de magasins. Chaque magasin est un Wallet ou " home ".


### Exemple


Commencez par cliquer sur "Créer votre magasin".


![image](assets/en/010.webp)


Cela créera votre première page d'accueil et votre premier tableau de bord pour l'utilisation de BTCPay Server.


(1) Après avoir cliqué sur "Créer votre boutique", le serveur BTCPay vous demandera de donner un nom à la boutique ; ce nom peut être n'importe quoi d'utile pour vous.


![image](assets/en/011.webp)


(2) Il faut ensuite définir la devise par défaut du magasin, soit une devise fiduciaire, soit une devise libellée en Bitcoin ou Sats. Pour l'environnement de démonstration, nous choisirons l'USD.


![image](assets/en/012.webp)


(3) Comme dernier paramètre de la configuration de la boutique, BTCPay Server vous demande de définir une "source de prix préférée" pour comparer le prix du Bitcoin au prix fiat actuel afin que votre boutique affiche le taux Exchange correct entre le Bitcoin et la devise fiat définie par la boutique. Nous nous en tiendrons à la valeur par défaut dans l'exemple de démonstration et définirons le taux Exchange de Kraken. Le serveur BTCPay utilise l'API Kraken pour vérifier les taux Exchange.


![image](assets/en/013.webp)


(4) Maintenant que ces paramètres de boutique ont été définis, cliquez sur le bouton Créer, et BTCPay Server créera le tableau de bord de votre première boutique, où l'assistant se poursuivra.


![image](assets/en/014.webp)


Félicitations, vous avez créé votre premier magasin, ce qui clôt cet exercice.


![image](assets/en/015.webp)


### Résumé des compétences


Dans cette section, vous avez appris



- Création d'un magasin et configuration d'une devise par défaut, combinée à des préférences en matière de sources de prix.
- Chaque "Boutique" est une nouvelle maison séparée des autres boutiques sur cette installation de BTCPay Server.


# Introduction à la sécurisation des clés Bitcoin


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Comprendre la génération des clés Bitcoin


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### Qu'est-ce qui permet de générer les clés Bitcoin ?


Les portefeuilles Bitcoin, lorsqu'ils sont créés, créent ce que l'on appelle un "seed". Dans le dernier objectif, vous avez créé un "seed". La série de mots générée précédemment est également connue sous le nom de phrases Mnemonic. La seed est utilisée pour dériver les clés Bitcoin individuelles et pour envoyer ou recevoir des Bitcoin. Les phrases seed ne doivent jamais être partagées avec des tiers ou des pairs non fiables.


La génération de seed est réalisée selon la norme industrielle connue sous le nom de cadre "déterministe hiérarchique" (HD).


![image](assets/en/016.webp)


### Adresses


Le serveur BTCPay est construit pour generate un nouveau Address. Cela permet d'éviter le problème de la réutilisation de la clé publique ou du Address. L'utilisation de la même clé publique facilite le suivi de l'ensemble de votre historique de paiement. Considérer les clés comme des bons à usage unique améliorerait considérablement la protection de votre vie privée. Nous utilisons également des adresses Bitcoin, à ne pas confondre avec les clés publiques.


Une Address est dérivée de la clé publique au moyen d'un "algorithme de hachage" Cependant, la plupart des portefeuilles et des transactions affichent des adresses plutôt que des clés publiques. Les adresses sont, en général, plus courtes que les clés publiques et commencent par `1`, `3`, ou `bc1`, alors que les clés publiques commencent par `02`, `03`, ou `04`.



- Les adresses commençant par `1.....` sont encore très courantes. Comme indiqué dans le chapitre "Création d'un nouveau magasin", il s'agit d'adresses anciennes. Ce type d'adresse Address est destiné aux transactions P2PKH. P2Pkh utilise le codage Base58, ce qui rend la Address sensible à la casse. Sa structure est basée sur la clé publique avec un chiffre supplémentaire comme identifiant.



- Les adresses commençant par "bc1...`" deviennent peu à peu des adresses très courantes. Il s'agit des adresses SegWit (natives). Elles offrent une meilleure structure tarifaire que les autres adresses mentionnées. Les adresses SegWit natives utilisent le codage Bech32 et n'autorisent que les lettres minuscules.



- Les adresses commençant par "3...`" sont encore couramment utilisées par les bourses pour les adresses de dépôt. Ces adresses sont mentionnées dans le chapitre "Créer un nouveau magasin". Il s'agit d'adresses SegWit enveloppées ou imbriquées. Cependant, elles peuvent également fonctionner comme des "Multisig Address". Lorsqu'elles sont utilisées en tant que SegWit Address, elles permettent de réaliser des économies sur les frais de transaction, mais dans une moindre mesure que les adresses SegWit natives. Les adresses P2SH utilisent le codage Base58. Elles sont donc sensibles à la casse, comme l'ancienne Address.



- Les adresses commençant par `2...` sont des adresses Testnet. Elles sont destinées à recevoir des Testnet Bitcoin (tBTC). Il ne faut jamais confondre et envoyer du Bitcoin à ces adresses. À des fins de développement, vous pouvez generate une Testnet Wallet. Il existe de nombreux robinets en ligne pour obtenir des Testnet Bitcoin. N'achetez jamais de Testnet Bitcoin. La Testnet Bitcoin est minée. Cela peut être une raison pour un développeur d'utiliser Regtest à la place. Il s'agit d'un environnement de jeu pour les développeurs, auquel il manque certains composants réseau. Bitcoin est cependant très utile pour le développement.


### Clés publiques


Les clés publiques sont moins utilisées dans la pratique aujourd'hui. Au fil du temps, les utilisateurs de Bitcoin les ont remplacées par des adresses. Elles existent toujours et sont encore utilisées occasionnellement. Les clés publiques sont, en général, des chaînes beaucoup plus longues que les adresses. Tout comme les adresses, elles commencent par un identifiant spécifique.



- Tout d'abord, `02...` et `03...` sont des identifiants de clé publique très standard encodés au format SEC. Ils peuvent être traités et transformés en adresses de réception, utilisés pour créer des adresses multi-sig ou pour vérifier une signature. Les premières transactions Bitcoin utilisaient des clés publiques dans le cadre de transactions P2PK.



- Les portefeuilles HD, cependant, utilisent une structure différente. les clés `xpub...`, `ypub...` ou `zpub...` sont appelées clés publiques étendues, ou xpubs. Ces clés sont utilisées pour dériver de nombreuses clés publiques dans le cadre du HD Wallet. Comme votre xpub contient les enregistrements de tout votre historique, c'est-à-dire les transactions passées et futures, ne les partagez jamais avec des parties non fiables.


### Résumé des compétences


Dans cette section, vous avez appris ce qui suit :



- Les différences entre les types de données des adresses et des clés publiques et les avantages de l'utilisation des adresses par rapport aux clés publiques.


### Évaluation des connaissances


Décrivez l'avantage de l'utilisation d'adresses fraîches pour chaque transaction par rapport à la réutilisation de Address ou aux méthodes à clé publique.


## Sécurisation des clés avec un Hardware Wallet


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Stockage des clés Bitcoin


Après avoir généré une phrase seed, la liste de 12 à 24 mots générée dans ce livre nécessite des sauvegardes et une sécurité appropriées, car ces mots sont le seul moyen de récupérer l'accès à une Wallet. La structure des portefeuilles HD et la façon dont ils génèrent des adresses de manière déterministe en utilisant une seule seed signifie que toutes les adresses créées seront sauvegardées en utilisant cette seule liste de mots Mnemonic, qui représente votre seed ou votre phrase de récupération.


Protégez votre phrase de recouvrement. Si quelqu'un y accède, notamment avec des intentions malveillantes, il peut déplacer vos fonds. Garder la seed en sécurité, tout en se rappelant qu'il s'agit d'un échange mutuel. Il existe plusieurs méthodes de stockage des clés privées Bitcoin, chacune présentant des avantages et des inconvénients en termes de sécurité, de confidentialité, de commodité et de stockage physique. En raison de l'importance des clés privées, les utilisateurs du Bitcoin ont tendance à les stocker et à les conserver en toute sécurité en "garde personnelle" plutôt que d'utiliser des services de "garde" comme les banques. Selon l'utilisateur, il doit utiliser soit une solution de stockage Cold, soit une solution Hot Wallet.


### Hot et Cold stockage des clés Bitcoin


En général, les portefeuilles Bitcoin sont libellés en Hot Wallet ou en Cold Wallet. La plupart des compromis portent sur la commodité, la facilité d'utilisation et les risques de sécurité. Chacune de ces méthodes peut également être utilisée dans le cadre d'une solution de dépôt. Toutefois, les compromis sont principalement liés à la sécurité et à la protection de la vie privée et dépassent le cadre de ce cours.


### Hot Wallet


Les portefeuilles Hot sont le moyen le plus pratique d'interagir avec le Bitcoin par le biais d'un logiciel mobile, web ou de bureau. Le Wallet est toujours connecté à Internet, ce qui permet aux utilisateurs d'envoyer ou de recevoir des Bitcoin. Cependant, c'est aussi sa faiblesse ; le Wallet étant toujours en ligne, il est désormais plus vulnérable aux attaques de pirates ou de logiciels malveillants sur votre appareil. Dans BTCPay Server, les portefeuilles Hot stockent les clés privées sur l'instance. Toute personne accédant à votre magasin BTCPay Server pourrait potentiellement voler des fonds à partir de ce Address si elle est malveillante. Lorsque BTCPay Server fonctionne dans un environnement hébergé, vous devez toujours en tenir compte dans votre profil de sécurité et, de préférence, ne pas utiliser de Hot Wallet dans un tel cas. Lorsque BTCPay Server est installé sur un matériel que vous possédez et sécurisez, le profil de risque diminue considérablement, mais il ne disparaît jamais complètement.


### Cold Wallet


Les particuliers placent leur Bitcoin dans un Cold Wallet parce qu'il permet d'isoler les clés privées de l'internet, les protégeant ainsi des menaces potentielles en ligne. La suppression de la connexion à Internet réduit le risque de logiciels malveillants, de logiciels espions et d'échanges de cartes SIM. Le stockage Cold est considéré comme supérieur au stockage Hot en termes de sécurité et d'autonomie, à condition que des précautions adéquates soient prises pour éviter la perte des clés privées Bitcoin. Le stockage Cold convient mieux aux grandes quantités de Bitcoin, qui ne sont pas destinées à être dépensées souvent en raison de la complexité de la configuration Wallet.


Il existe différentes méthodes de stockage des clés Bitcoin dans le stockage Cold, des portefeuilles papier aux portefeuilles cérébraux, en passant par les portefeuilles matériels ou, depuis le début, un fichier Wallet. La plupart des portefeuilles utilisent BIP 39 pour generate la phrase seed. Cependant, au sein du logiciel Bitcoin core, il n'y a pas encore de consensus sur son utilisation. Le logiciel Bitcoin core continuera à generate un fichier Wallet.dat, que vous devez stocker dans un emplacement hors ligne sécurisé.


### Résumé des compétences


Dans cette section, vous avez appris



- Les différences entre les portefeuilles Hot et Cold en termes de fonctionnalité et leurs compromis.


### Évaluation des connaissances Révision conceptuelle



- Qu'est-ce qu'un Wallet ?



- Quelle est la différence entre les portefeuilles Hot et Cold ?



- Qu'entend-on par "générer une Wallet" ?


## Utilisation des touches de votre Bitcoin


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### Serveur BTCPay Wallet


BTCPay Server comprend les fonctions Wallet standard suivantes :



- Transactions
- Envoyer
- Recevoir
- Rescan
- Paiements tirés
- Paiements
- PSBT
- Paramètres généraux


### Transactions


Les administrateurs peuvent voir les transactions entrantes et sortantes pour les On-Chain Wallet connectés à ce magasin spécifique dans la vue des transactions. Chaque transaction comporte une distinction entre les montants reçus et envoyés. Les transactions reçues seront en Green, et les transactions sortantes seront en rouge. Dans la vue des transactions de BTCPay Server, les administrateurs verront également un ensemble d'étiquettes standard.


| Transaction Type | Description                                          |
| ---------------- | ---------------------------------------------------- |
| App              | Payment was received through an app-created invoice  |
| invoice          | Payment was received through an invoice              |
| payjoin          | Not paid, invoice timer still has not expired        |
| payjoin-exposed  | UTXO was exposed through an invoice payjoin proposal |
| payment-request  | Payment was received through a payment request       |
| payout           | Payment was sent through a payout or refund          |

### Comment envoyer


La fonction d'envoi du serveur BTCPay envoie les transactions depuis votre serveur BTCPay On-Chain Wallet. Le serveur BTCPay permet plusieurs façons de signer vos transactions pour dépenser des fonds. Une transaction peut être signée avec ;



- Hardware Wallet
- Portefeuilles soutenant PSBT
- Clé privée HD ou graines de récupération.
- Hot Wallet


#### Hardware Wallet


BTCPay Server intègre la prise en charge de Hardware Wallet, ce qui vous permet d'utiliser votre Hardware Wallet avec BTCPay Vault sans divulguer d'informations à des applications ou des serveurs tiers. L'intégration de Hardware Wallet dans BTCPay Server vous permet d'importer votre Hardware Wallet et de dépenser les fonds entrants avec une simple confirmation sur votre appareil. Vos clés privées ne quittent jamais l'appareil et tous les fonds sont validés par rapport à votre Full node, ce qui garantit qu'il n'y a pas de fuite de données.


#### Signature avec une Wallet prenant en charge la PSBT


PSBT (Partially Signed Bitcoin Transactions) est un format d'échange pour les transactions Bitcoin qui doivent encore être entièrement signées. PSBT est pris en charge par le serveur BTCPay et peut être signé avec des portefeuilles matériels et logiciels compatibles.


La construction d'une transaction Bitcoin entièrement signée passe par les étapes suivantes :



- Une PSBT est construite avec des entrées et des sorties spécifiques, mais sans signature
- Le PSBT exporté peut être importé par un Wallet qui prend en charge ce format
- Les données de la transaction peuvent être contrôlées et signées à l'aide du Wallet
- Le fichier PSBT signé est exporté à partir du Wallet et importé sur le serveur BTCPay
- Le serveur de BTCPay produit la transaction Bitcoin finale
- Vous vérifiez le résultat et le diffusez sur le réseau


#### Signature avec la clé privée du disque dur ou Mnemonic seed


Si vous avez créé une Wallet avant d'utiliser le serveur BTCPay, vous pouvez dépenser les fonds en saisissant votre clé privée dans un champ approprié. Définissez un "AccountKeyPath" approprié dans Wallet> Settings ; sinon, vous ne pourrez pas dépenser.


#### Signature avec un Hot Wallet


Si vous avez créé une nouvelle Wallet lors de la configuration de votre magasin et que vous l'avez activée en tant que Hot Wallet, elle utilisera automatiquement la seed stockée sur un serveur pour signer.


### RBF (Replace-by-fee)


Replace-by-fee (RBF) est une fonction du protocole Bitcoin qui vous permet de remplacer une transaction précédemment diffusée (alors qu'elle n'est pas encore confirmée). Cela permet de rendre aléatoire l'empreinte de la transaction de votre Wallet ou de la remplacer par un taux de frais plus élevé afin de placer la transaction plus haut dans la file d'attente de la priorité de confirmation (Mining). Cela remplacera effectivement la transaction originale car le taux de frais plus élevé sera prioritaire et, une fois confirmé, il invalidera la transaction originale (pas de double dépense).


Appuyez sur le bouton "Paramètres avancés" pour afficher les options RBF.


![image](assets/en/017.webp)



- Randomize for higher privacy, permet de remplacer automatiquement la transaction pour randomiser l'empreinte digitale de la transaction.
- Oui, signaler la transaction pour RBF et la remplacer explicitement (non remplacée par défaut, uniquement par saisie)
- Non, ne permettez pas que la transaction soit remplacée.


### Sélection Coin


La sélection Coin est une fonction avancée d'amélioration de la confidentialité qui vous permet de sélectionner les pièces que vous souhaitez dépenser lors de l'élaboration d'une transaction. Par exemple, payer avec des pièces qui viennent d'être mélangées.


La sélection Coin fonctionne de manière native avec la fonction d'étiquetage Wallet. Cela vous permet d'étiqueter les fonds entrants pour une gestion et des dépenses plus faciles.


BTCPay Server prend en charge la norme BIP-329 pour la gestion des étiquettes. Si vous transférez à partir d'un Wallet qui prend en charge BIP-329 et que vous avez défini des étiquettes, BTCPay Server les reconnaîtra et les importera automatiquement. Lors de la migration des serveurs, ces informations peuvent également être exportées et importées dans le nouvel environnement.


### Comment recevoir


Lorsque l'on clique sur le bouton de réception dans BTCPay Server, cela génère une Address inutilisée qui peut être utilisée pour recevoir des paiements. Les administrateurs peuvent également créer une nouvelle Address en créant une nouvelle "Invoice"


Le serveur BTCPay vous invitera toujours à cliquer sur le generate du Address disponible suivant afin d'éviter la réutilisation du Address. Après avoir cliqué sur "generate next available BTC Address", BTCPay Server a généré une nouvelle Address et un QR. Il vous permet également d'attribuer directement une étiquette à la Address pour une meilleure gestion de vos adresses.


![image](assets/en/018.webp)


![image](assets/en/019.webp)


#### Re-scanner


La fonction Rescan s'appuie sur le "Scantxoutset" de Bitcoin core 0.17.0 pour analyser l'état actuel du Blockchain (appelé UTXO Set) à la recherche de pièces appartenant au schéma de dérivation configuré. Un rescan de Wallet résout deux problèmes communs que les utilisateurs du serveur BTCPay rencontrent fréquemment.


1. Problème de limite d'écart - La plupart des portefeuilles tiers sont des portefeuilles légers qui partagent un nœud entre plusieurs utilisateurs. Les portefeuilles légers et dépendant de la Full node limitent le nombre (généralement 20) d'adresses sans solde qu'ils suivent sur la Blockchain afin d'éviter les problèmes de performance. Le serveur BTCPay génère une nouvelle Address pour chaque Invoice. Compte tenu de ce qui précède, après que BTCPay Server ait généré 20 factures impayées consécutives, la Wallet externe cesse de récupérer les transactions, en supposant qu'aucune nouvelle transaction n'a eu lieu. Votre Wallet externe ne les affichera pas une fois que les factures auront été payées le 21, le 22, etc. D'autre part, en interne, la Wallet du serveur BTCPay suit toutes les Address qu'elle génère, ainsi qu'une limite d'écart nettement plus élevée. Il ne dépend pas d'un tiers et peut toujours afficher un solde correct.

2. La solution de la limite d'écart - Si votre [Wallet externe/existant](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) permet la configuration de la limite d'écart, la solution la plus simple est de l'augmenter. Cependant, la majorité des portefeuilles ne le permettent pas. À notre connaissance, les seuls portefeuilles qui prennent actuellement en charge la configuration de la limite de l'écart sont Electrum, Wasabi et Sparrow wallet. Malheureusement, il est probable que vous rencontriez un problème avec de nombreux autres portefeuilles. Pour une expérience utilisateur et une confidentialité optimales, envisagez d'utiliser le Wallet interne du serveur BTCPay plutôt que des portefeuilles externes.


#### Le serveur BTCPay utilise "mempoolfullrbf=1"


Le serveur BTCPay utilise "mempoolfullrbf=1" ; nous l'avons ajouté par défaut à votre configuration du serveur BTCPay. Cependant, nous avons également fait en sorte que vous puissiez désactiver cette fonctionnalité vous-même. Sans "mempoolfullrbf=1", si un client double un paiement avec une transaction ne signalant pas RBF, le marchand ne le saurait qu'après confirmation.


Un administrateur peut décider de ne pas utiliser ce paramètre. La chaîne de caractères suivante permet de modifier le paramètre par défaut.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i
```


### Paramètres du serveur BTCPay Wallet


Les paramètres Wallet dans BTCPay Server fournissent un aperçu clair et concis des paramètres généraux de votre Wallet. Tous ces paramètres sont pré-remplis si le Wallet a été créé avec BTCPay Server.


![image](assets/en/020.webp)


Les paramètres Wallet dans BTCPay Server fournissent un aperçu clair et concis des paramètres généraux de votre Wallet. Tous ces paramètres sont pré-remplis si la Wallet a été créée avec BTCPay Server. Les paramètres Wallet de BTCPay Server commencent par le statut de la Wallet. S'agit-il d'une Wallet Watch-only ou Hot ? Selon le type de Wallet, les actions peuvent varier, y compris la réanalyse de la Wallet pour les transactions manquantes, l'élagage des anciennes transactions de l'historique, l'enregistrement de la Wallet pour les liens de paiement, ou le remplacement et la suppression de la Wallet actuelle attachée à la boutique. Dans les paramètres Wallet de BTCPay Server, les administrateurs peuvent définir une étiquette pour le Wallet afin d'améliorer la gestion du Wallet. Ici, l'administrateur pourra également voir le schéma de dérivation, la clé de compte (xpub), l'empreinte digitale et le chemin d'accès. Les paiements dans les paramètres Wallet ont seulement deux paramètres principaux. Le paiement est invalide si la transaction n'est pas confirmée dans les minutes qui suivent l'expiration de la Invoice. La Invoice est considérée comme confirmée lorsque la transaction de paiement a reçu un nombre X de confirmations. Les administrateurs peuvent également activer l'affichage des frais recommandés sur l'écran de paiement ou fixer un objectif de confirmation manuelle en nombre de blocs.


![image](assets/en/021.webp)


**!Note!**


Si vous suivez ce cours de manière indépendante, la création de ce compte se fera probablement sur un hôte tiers. Par conséquent, nous vous conseillons à nouveau de ne pas les utiliser comme des environnements de production, mais plutôt à des fins de formation uniquement.


### Exemple


#### Configurer un Bitcoin Wallet dans le serveur BTCPay


Le serveur BTCPay propose deux méthodes pour configurer une Wallet. La première consiste à importer une Bitcoin Wallet existante. L'importation peut se faire en connectant une Hardware Wallet, en important un fichier Wallet, en saisissant une clé publique étendue, en scannant le code QR d'une Wallet ou, ce qui est le moins intéressant, en saisissant à la main une seed de récupération Wallet précédemment créée. Dans BTCPay Server, il est également possible de créer une nouvelle Wallet. Il existe deux façons de configurer BTCPay Server lors de la création d'une nouvelle Wallet.


L'option Hot Wallet de BTCPay Server permet des fonctions telles que 'PayJoin' ou 'Liquid'. Il y a cependant un inconvénient : la seed de récupération générée pour cette Wallet sera stockée sur le serveur, où toute personne disposant d'un contrôle administratif pourra la récupérer. Comme votre clé privée est dérivée de votre seed de recouvrement, un acteur malveillant pourrait avoir accès à vos fonds actuels et futurs !


Pour atténuer ce risque dans le serveur BTCPay, un administrateur peut définir la valeur dans Paramètres du serveur > Politiques > "Autoriser les non-administrateurs à créer des portefeuilles Hot pour leurs magasins" sur "non", car c'est la valeur par défaut. Pour renforcer la sécurité de ces portefeuilles Hot, l'administrateur du serveur doit activer l'authentification 2FA sur les comptes autorisés à avoir des portefeuilles Hot. Le stockage de clés privées sur un serveur public est une pratique dangereuse qui comporte des risques importants. Certains sont similaires aux risques liés à la norme Lightning Network (voir le chapitre suivant pour les risques liés à la norme Lightning Network).


La deuxième option offerte par BTCPay Server pour générer une nouvelle Wallet consiste à créer une Watch-only wallet. BTCPay Server generate vos clés privées une fois. Une fois que l'utilisateur a confirmé avoir écrit sa phrase seed, BTCPay Server efface les clés privées du serveur. Par conséquent, votre boutique a maintenant une Watch-only wallet connectée à elle. Pour dépenser les fonds reçus sur votre Watch-only wallet, voir le chapitre Comment envoyer, soit en utilisant le Coffre-fort du serveur BTCPay, PSBT (Partially Signed Bitcoin Transaction), soit, ce qui est le moins recommandé, en fournissant manuellement votre phrase seed.


Vous avez créé un nouveau 'Store' dans la dernière partie. L'assistant d'installation continue en vous demandant de "Configurer un Wallet" ou "Configurer un nœud Lightning". Dans cet exemple, vous suivrez la procédure de l'assistant "Set up a Wallet" (1).


![image](assets/en/022.webp)


Après avoir cliqué sur "Set up a Wallet", l'assistant continuera en vous demandant comment vous voulez continuer ; BTCPay Server offre maintenant l'option de connecter un Bitcoin Wallet existant à votre nouveau magasin. Si vous n'avez pas de Wallet, BTCPay Server suggère d'en créer une nouvelle. Cet exemple suivra les étapes pour "créer une nouvelle Wallet" (2). Suivez les étapes pour apprendre à "Connecter une Wallet existante" (1).


![image](assets/en/023.webp)


**!Note!**


Si vous suivez ce cours dans une salle de classe, veuillez noter que l'exemple actuel et la seed que nous avons générés sont uniquement destinés à des fins éducatives. Il ne devrait jamais y avoir de quantité substantielle autre que celle requise tout au long des exercices sur ces adresses.


(1) Poursuivre l'assistant "Nouvelle Wallet" en cliquant sur le bouton "Créer une nouvelle Wallet".


![image](assets/en/024.webp)


(2) Après avoir cliqué sur "Créer une nouvelle Wallet", la fenêtre suivante de l'assistant propose les options "Hot Wallet" et "Watch-only wallet" Si vous suivez un instructeur, votre environnement est une démo partagée et vous ne pouvez créer qu'une Watch-only wallet. Remarquez la différence entre les deux figures ci-dessous. Si vous êtes dans l'environnement de démonstration et que vous suivez l'instructeur, créez une "Watch-only wallet" et continuez avec l'assistant "Nouvelle Wallet".


![image](assets/en/025.webp)


![image](assets/en/026.webp)


(3) En continuant le nouvel assistant Wallet, vous êtes maintenant dans la section Créer un BTC Watch-only wallet. C'est ici que nous définissons le "type Address" de la Wallet BTCPay Server vous permet de choisir votre type de Address préféré ; au moment de la rédaction de ce cours, il est toujours recommandé d'utiliser les adresses bech32. Vous trouverez plus de détails sur les adresses dans le premier chapitre de cette partie.



- SegWit (bech32)
  - Les adresses natives SegWit commencent par `bc1q`.
  - Exemple : `bc1qXXXXXXXXXXXXXXXXXXXXXXXX`
- L'héritage
  - Les adresses héritées sont des adresses qui commencent par le chiffre "1".
  - Exemple : `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (pour les utilisateurs avancés)
  - Les adresses Taproot commencent par `bc1p`.
  - Exemple : `bc1pXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- SegWit enveloppé
  - Les adresses enveloppées de SegWit commencent par `3`.
  - Exemple : `37BBXXXXXXXXXXXXX`


Choisissez SegWit (recommandé) comme type Wallet Address préféré.


![image](assets/en/027.webp)


(4) Lors du paramétrage du Wallet, le serveur BTCPay permet aux utilisateurs de paramétrer un passphrase optionnel par l'intermédiaire du BIP39 ; veillez à confirmer votre mot de passe.


![image](assets/en/028.webp)


(5) Après avoir défini le type Address de la Wallet et éventuellement quelques options avancées, cliquez sur Créer, et BTCPay Server créera la generate de votre nouvelle Wallet. Notez qu'il s'agit de la dernière étape avant de générer votre phrase seed. Veillez à ne le faire que dans un environnement où quelqu'un ne pourrait pas voler la phrase seed en regardant votre écran.


![image](assets/en/029.webp)


(6) Dans l'écran suivant de l'assistant, BTCPay Server vous montre la phrase de récupération seed pour votre Wallet nouvellement générée ; ce sont les clés pour récupérer votre Wallet et signer des transactions. BTCPay Server génère une phrase seed de 12 mots. Ces mots seront effacés du serveur après cet écran de configuration. Cette Wallet est spécifiquement une Watch-only wallet. Il est conseillé de ne pas stocker cette phrase seed sous forme numérique ou photographique. Les utilisateurs ne peuvent aller plus loin dans l'assistant que s'ils reconnaissent avoir écrit leur phrase seed.


![image](assets/en/030.webp)


(7) Après avoir cliqué sur Terminé et sécurisé la phrase Bitcoin seed nouvellement générée, le serveur BTCPay mettra à jour votre boutique avec la nouvelle Wallet jointe et sera prêt à recevoir des paiements. Dans la Interface de l'utilisateur, dans le menu de navigation de gauche, remarquez que la Bitcoin est maintenant surlignée et activée sous la Wallet.


![image](assets/en/031.webp)


### Exemple : Écrire une phrase seed


C'est un moment particulièrement sûr pour utiliser la phrase Bitcoin. Comme nous l'avons déjà mentionné, vous êtes le seul à avoir accès à votre phrase seed ou à la connaître. Comme vous suivez un instructeur et une classe, la phrase seed générée ne doit être utilisée que dans le cadre de ce cours. Trop de facteurs, y compris les regards indiscrets des camarades de classe, les systèmes non sécurisés et autres, font que ces clés ne sont qu'éducatives et ne sont pas dignes de confiance. Toutefois, les clés générées doivent être conservées pour des exemples de cours.


La première méthode que nous utiliserons dans cette situation, qui est également la moins sûre, consiste à écrire la phrase seed dans le bon ordre. Une carte de phrase seed est incluse dans le matériel de cours fourni à l'étudiant ou peut être trouvée sur le GitHub du serveur BTCPay. Nous utiliserons cette carte pour écrire les mots générés à l'étape précédente. Veillez à les écrire dans le bon ordre. Une fois que vous les avez écrits, vérifiez-les par rapport à ce qui a été donné par le logiciel pour vous assurer que vous les avez écrits dans le bon ordre. Une fois que vous les avez écrits, cochez la case indiquant que vous avez correctement écrit votre phrase seed.


### Exemple : Stockage d'une phrase seed sur un Hardware Wallet


Dans ce cours, nous abordons le stockage d'une phrase seed sur un Hardware Wallet. Suivre ce cours avec un instructeur peut parfois inclure un tel dispositif. Dans le cours, les documents de référence ont compilé une liste de portefeuilles matériels qui conviendraient à cet exercice.


Dans cet exemple, nous utiliserons le coffre-fort du serveur BTCPay et un Blockstream Jade Hardware Wallet.


Vous pouvez également suivre un guide vidéo sur la connexion d'un Hardware Wallet.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


Télécharger BTCPay Server Vault : https://github.com/btcpayserver/BTCPayServer.Vault/releases


Assurez-vous de télécharger les fichiers corrects pour votre système spécifique. Les utilisateurs de Windows doivent télécharger le paquet [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), les utilisateurs de Mac doivent télécharger le paquet [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), et les utilisateurs de Linux doivent télécharger [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)


Après avoir installé BTCPay Server Vault, démarrez le logiciel en cliquant sur l'icône sur votre bureau. Lorsque BTCPay Server Vault est correctement installé et démarré pour la première fois, il demandera la permission d'être utilisé avec des applications Web. Il vous demandera d'accorder l'accès au serveur BTCPay spécifique avec lequel vous travaillez. Acceptez ces conditions. BTCPay Server Vault recherchera alors le périphérique matériel. Une fois le périphérique trouvé, BTCPay Server reconnaîtra que Vault est en cours d'exécution et qu'il a récupéré votre périphérique.


**!Note!**


Ne donnez pas vos clés SSH ou votre compte administrateur de serveur à quelqu'un d'autre que les administrateurs lorsque vous utilisez une Hot Wallet. Toute personne ayant accès à ces comptes aura accès aux fonds de la Hot Wallet.


### Résumé des compétences


Dans cette section, vous avez appris ce qui suit :



- La vue transactionnelle de la Bitcoin Wallet et ses différentes catégorisations.
- Différentes options sont disponibles pour l'envoi à partir d'un Bitcoin Wallet, du matériel aux portefeuilles Hot.
- Le problème de la limite de l'écart rencontré lors de l'utilisation de la plupart des portefeuilles et la manière d'y remédier.
- Comment generate une nouvelle Bitcoin Wallet dans le serveur BTCPay, y compris le stockage des clés dans une Hardware Wallet et la sauvegarde de la phrase de récupération.


Dans cet objectif, vous avez appris à generate un nouveau Bitcoin Wallet dans le serveur BTCPay. Nous n'avons pas encore abordé la manière de sécuriser ou d'utiliser ces clés. Dans un bref aperçu de cet objectif, vous avez appris à mettre en place le premier magasin. Vous avez appris à generate une phrase Bitcoin Recovery seed.


### Évaluation des connaissances Examen pratique


Décrire une méthode pour générer des clés et un système pour les sécuriser, ainsi que les compromis/risques du système de sécurité.


## Serveur BTCPay Lightning Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


Lorsqu'un administrateur de serveur provisionne une nouvelle instance de BTCPay Server, il peut configurer une implémentation Lightning Network, telle que LND, Core Lightning, ou Eclair ; voir la partie Configuration de BTCPay Server pour des instructions d'installation plus détaillées.


Si vous suivez une classe, la connexion d'un nœud Lightning à votre serveur BTCPay fonctionne par le biais d'un nœud personnalisé. Un utilisateur qui n'est pas administrateur de serveur sur BTCPay Server ne pourra pas utiliser le nœud Lightning interne par défaut. Ceci afin de protéger le propriétaire du serveur contre la perte de ses fonds. Les administrateurs de serveur peuvent installer un plugin pour permettre l'accès à leur nœud Lightning via LNBank ; ceci sort du cadre de ce livre. Pour plus d'informations sur LNBank, consultez la page officielle du plugin.


### Connecter le nœud interne (administrateur du serveur)


L'administrateur du serveur peut utiliser le nœud Lightning interne de BTCPay Server. Quelle que soit l'implémentation de Lightning, la connexion au nœud interne de Lightning est la même.


Allez dans un magasin de configuration précédent, et cliquez sur le Wallet "Lightning" dans le menu de gauche. BTCPay Server offre deux possibilités de configuration : utiliser le nœud interne (administrateur du serveur uniquement par défaut) ou un nœud personnalisé (connexion externe). Les administrateurs de serveur peuvent cliquer sur l'option "Utiliser le nœud interne". Aucune autre configuration n'est nécessaire. Cliquez sur le bouton "save" et remarquez la notification "BTC Lightning node updated". Le magasin a maintenant obtenu avec succès les capacités Lightning Network.


### Connecter un nœud externe (utilisateur du serveur/propriétaire du magasin)


Par défaut, les propriétaires de boutiques ne sont pas autorisés à utiliser le Lightning Node de l'administrateur du serveur. La connexion doit être faite à un nœud externe, soit un nœud appartenant au propriétaire de la boutique avant la mise en place d'un serveur BTCPay, un plugin LNBank s'il est mis à disposition par l'administrateur du serveur, ou une solution de dépôt comme Alby.


Allez dans un magasin déjà configuré et cliquez sur "Lightning" sous "wallets" dans le menu de gauche. Comme les propriétaires de magasins ne sont pas autorisés à utiliser le nœud interne par défaut, cette option est grisée. L'utilisation d'un nœud personnalisé est la seule option disponible par défaut pour les propriétaires de magasins.


Le serveur BTCPay nécessite des informations de connexion ; la solution pré-fabriquée (ou la solution de garde) fournira ces informations spécifiquement adaptées à une implémentation Lightning. Dans le serveur BTCPay, les propriétaires de boutiques peuvent utiliser les connexions suivantes ;



- C-lightning via TCPouUnixdomainsocketconnection.
- Charge éclair via HTTPS
- Eclair via HTTPS
- LND via le proxy REST
- LNDhub via l'API REST


![image](assets/en/032.webp)


Cliquez sur "tester la connexion" pour vous assurer que vous avez correctement saisi les détails de la connexion. Une fois que la connexion est confirmée comme étant bonne, cliquez sur " Enregistrer ", et BTCPay Server indique que la boutique a été mise à jour avec un nœud Lightning.


### Gestion du nœud interne Lightning LND (administrateur du serveur)


Après avoir connecté le nœud Lightning interne, les administrateurs de serveur remarqueront de nouvelles tuiles sur le tableau de bord, spécifiquement pour les informations sur Lightning.



- L'équilibre de la foudre
- BTC dans les canaux
  - Canaux d'ouverture de la BTC
  - Solde local en BTC
  - Solde à distance en BTC
  - Fermeture des canaux de la BTC
- BTC On-Chain
  - BTC confirmé
  - BTC non confirmé
  - BTC réservé
- Services de foudre
  - Ride the Lightning (RTL).


En cliquant sur le logo Ride the Lightning dans la tuile "Lightning services" ou sur "Lightning" sous les portefeuilles dans le menu de gauche, les administrateurs de serveurs peuvent accéder à RTL pour la gestion des nœuds Lightning.


**Note!**


Échec de la connexion du nœud de foudre interne - Si la connexion interne échoue, confirmez :


1. Le nœud Bitcoin On-Chain est entièrement synchronisé

2. Le nœud de foudre interne est "activé" sous "Lightning" > "Settings" > "BTC Lightning Settings"


Si vous ne parvenez pas à vous connecter à votre nœud Lightning, vous pouvez essayer de redémarrer votre serveur, ou lire plus de détails dans la documentation officielle de BTCPay Server ; https://docs.btcpayserver.org/Troubleshooting/. Vous ne pouvez pas accepter les paiements Lightning dans votre boutique tant que votre nœud Lightning n'apparaît pas "en ligne". Essayez de tester votre connexion Lightning en cliquant sur le lien "Public Node Info".


### Éclair Wallet


Dans l'option Lightning Wallet de la barre de menu de gauche, les administrateurs de serveur trouveront un accès facile à RTL, à leurs informations de nœud public et aux paramètres Lightning spécifiques à leur magasin BTCPay Server.


#### Informations sur le nœud interne


Les administrateurs de serveurs peuvent cliquer sur les informations relatives au nœud interne pour afficher l'état de leur serveur (en ligne/hors ligne) et la chaîne de connexion pour Clearnet ou Tor.


![image](assets/en/033.webp)


#### Modifier la connexion


Pour modifier le nœud Lightning externe, allez dans "Lightning Settings" et cliquez sur "Change connection" (à côté de "Public Node info"). Cette opération réinitialise la configuration existante. Saisissez les détails du nouveau nœud, cliquez sur Enregistrer et la boutique sera mise à jour en conséquence.


![image](assets/en/034.webp)


#### Services


Si l'administrateur du serveur décide d'installer plusieurs services pour l'implémentation de Lightning, ils seront listés ici. Avec une implémentation LND standard, les administrateurs auront Ride The Lightning (RTL) comme outil standard pour la gestion des nœuds.


#### Paramètres BTC Lightning Wallet


Après avoir ajouté le nœud Lightning à la boutique lors d'une étape précédente, les propriétaires de boutiques peuvent encore choisir de le désactiver pour leur boutique en utilisant le bouton situé en haut des paramètres Lightning.


![image](assets/en/035.webp)


#### Options de paiement Lightning


Les propriétaires de magasins peuvent définir les paramètres suivants pour améliorer l'expérience Lightning de leurs clients.



- Afficher les montants des paiements éclairs en Satoshis.
- Ajouter des indications de saut pour les canaux privés au Lightning Invoice.
- Unifier les codes URL/QR des paiements On-Chain et Lightning au moment du paiement.
- Définir un modèle de description pour les factures éclair.


#### LNURL


Les propriétaires de magasins peuvent choisir d'utiliser ou non LNURL. L'URL Lightning Network, ou LNURL, est une norme proposée pour les interactions entre le payeur Lightning et le bénéficiaire. En bref, une LNURL est une URL encodée en bech32 préfixée par LNURL. Le Lightning Wallet est censé décoder l'URL, la contacter et attendre un objet JSON contenant d'autres instructions, notamment une balise qui définit le comportement de la LNURL.



- Activer LNURL
- LNURL Mode classique
  - Pour la compatibilité avec Wallet, URL codée en Bech32 (classique) contre URL en clair (à venir)
- Permettre au bénéficiaire de transmettre un commentaire.


### Exemple 1


#### Se connecter à Lightning avec le nœud interne (Administrateur)


Cette option n'est disponible que si vous êtes l'administrateur de cette instance ou si l'administrateur a modifié les paramètres par défaut afin que les utilisateurs puissent utiliser le nœud d'éclairage interne.


En tant qu'administrateur, cliquez sur Lightning Wallet dans la barre de menu de gauche. BTCPay Server vous demandera de sélectionner l'une des deux options pour connecter un nœud Lightning : un nœud interne ou un nœud externe personnalisé. Cliquez sur "Use internal node" et cliquez ensuite sur "Save"


#### Gestion du nœud Lightning (RTL)


Après s'être connecté au nœud interne de Lightning, le serveur BTCPay sera mis à jour et affichera une notification "BTC Lightning node updated", confirmant que vous avez maintenant connecté Lightning à votre boutique.


La gestion du nœud d'éclairage est une tâche qui incombe à l'administrateur du serveur. Cela implique les éléments suivants :


- Gérer les transactions
- Gestion des liquidités
  - Liquidités entrantes
  - Liquidités sortantes
- Gestion des pairs et des canaux
  - Pairs connectés
  - Redevances pour les chaînes
  - État du canal
- Effectuer des sauvegardes fréquentes des états des canaux.
- Vérification des rapports de routage
- Vous pouvez également utiliser des services tels que Loop.


Toute la gestion des nœuds Lightning est effectuée en standard avec RTL (en supposant que vous utilisez une implémentation LND). Les administrateurs peuvent cliquer sur leur Wallet Lightning dans BTCPay Server et trouver un bouton pour ouvrir RTL. Le tableau de bord principal de BTCPay Server est maintenant mis à jour avec les tuiles Lightning Network, y compris l'accès rapide à RTL.


### Exemple 2


#### Se connecter à l'éclairage avec Alby


Pour entrer en contact avec un dépositaire comme Alby, les propriétaires de magasins doivent d'abord créer un compte et se rendre sur le site https://getalby.com/


![image](assets/en/036.webp)


Après avoir créé le compte Alby, allez dans votre magasin BTCPay Server.


Étape 1 : Cliquez sur "Configurer un nœud Lightning" sur le tableau de bord ou sur "Lightning" sous les portefeuilles.


![image](assets/en/037.webp)


Étape 2 : Insérez vos identifiants de connexion Wallet fournis par Alby. Sur le tableau de bord d'Alby, cliquez sur Wallet. Vous y trouverez "Wallet Connection Credentials". Copiez ces informations d'identification. Collez les informations d'identification d'Alby dans le champ de configuration de la connexion dans BTCPay Server.


![image](assets/en/038.webp)


Étape 3 : Après avoir fourni au serveur BTCPay les détails de la connexion, cliquez sur le bouton "Tester la connexion" pour vous assurer que la connexion fonctionne correctement. Remarquez le message "Connection to lightning node successful" en haut de votre écran. Cela confirme que tout fonctionne comme prévu.


![image](assets/en/039.webp)


Étape 4 : Cliquez sur "Enregistrer", et votre magasin est maintenant connecté à un nœud Lightning par Alby.


![image](assets/en/040.webp)


**!Note!**


Ne confiez jamais à un dépositaire une valeur supérieure à celle que vous êtes prêt à perdre.


### Résumé des compétences


Dans cette section, vous avez appris



- Comment connecter un nœud Lightning interne ou externe ?
- Contenu et fonction des différentes tuiles du tableau de bord relatives à la foudre
- Comment configurer le Lightning Wallet en utilisant Voltage Surge ou Alby


### Évaluation des connaissances Examen pratique


Décrivez quelques-unes des différentes options permettant de connecter un Lightning Wallet à votre magasin.


# Serveur BTCPay Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Aperçu du tableau de bord


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay Server est un logiciel modulaire. Cependant, il existe des normes auxquelles chaque serveur BTCPay doit adhérer, et ces normes régiront l'interaction entre l'administrateur et les utilisateurs. En commençant par le tableau de bord. Le point d'entrée principal de chaque serveur BTCPay après la connexion. Le tableau de bord fournit une vue d'ensemble des performances de votre magasin, du solde actuel de la Wallet et des transactions des 7 derniers jours. Comme il s'agit d'une vue modulaire, les plugins peuvent utiliser cette vue à leur avantage et créer leurs propres tuiles sur le tableau de bord. Pour ce cours, nous ne discuterons que des plugins et applications standards, ainsi que de leurs vues respectives, dans BTCPay Server.


### Carreaux du tableau de bord


Dans la vue principale du tableau de bord de BTCPay Server, quelques tuiles standard sont disponibles. Ces tuiles sont conçues pour que le propriétaire ou l'administrateur de la boutique puisse gérer rapidement sa boutique en une seule vue d'ensemble.



- Wallet équilibre
- Activité de transaction
- Solde Lightning (si Lightning est activé sur le magasin)
- Services Lightning (si Lightning est activé sur la boutique)
- Transactions récentes.
- Factures récentes
- Crowdfunds actuellement actifs
- Performances du magasin / articles les plus vendus.


### Wallet équilibre


La tuile Wallet Balance donne un aperçu rapide des fonds et de la performance de votre Wallet. Il peut être visualisé en BTC ou en monnaie fiduciaire dans un graphique hebdomadaire, mensuel ou annuel.


![image](assets/en/041.webp)


### Activité de transaction


À côté de la tuile Wallet Balance, BTCPay Server affiche un aperçu rapide des paiements en attente, le nombre de transactions au cours des 7 derniers jours, et si votre boutique a émis des remboursements. En cliquant sur le bouton Gérer, vous accédez à la gestion des paiements en attente (pour en savoir plus sur les paiements, consultez le chapitre Paiements de BTCPay Server).


![image](assets/en/042.webp)


### L'équilibre de la foudre


Elle n'est visible que lorsque l'éclair est activé.


Lorsque l'administrateur a autorisé l'accès à Lightning Network, le tableau de bord de BTCPay Server comporte désormais une nouvelle tuile contenant des informations sur votre nœud Lightning. Combien de BTC sont dans les canaux, comment ils sont équilibrés localement ou à distance (liquidité entrante ou sortante), si les canaux se ferment ou s'ouvrent, et combien de Bitcoin est détenu par On-Chain sur le nœud Lightning.


![image](assets/en/043.webp)


### Services de foudre


Elle n'est visible que lorsque la foudre est active.


En plus de voir votre solde Lightning sur le tableau de bord de BTCPay Server, les administrateurs verront également la tuile des services Lightning. Ici, les administrateurs peuvent trouver des boutons rapides pour les outils qu'ils utilisent pour gérer leur nœud Lightning ; par exemple, Ride the Lightning est l'un des outils standard de BTCPay Server pour la gestion des nœuds Lightning.


![image](assets/en/044.webp)


### Transactions récentes


La tuile Transactions récentes affiche les transactions les plus récentes de votre boutique. En un clic, l'administrateur de l'instance du serveur BTCPay peut désormais voir la dernière transaction et déterminer si elle nécessite une attention particulière.


![image](assets/en/045.webp)


### Factures récentes


La tuile Factures récentes affiche les 6 dernières factures générées par votre serveur BTCPay, y compris le statut et le montant Invoice. La tuile comprend également un bouton "Voir tout" pour accéder facilement à l'aperçu complet de la Invoice.


![image](assets/en/046.webp)


### Point de vente et crowdfunding


Comme BTCPay Server fournit un ensemble de plugins ou d'applications standard, Point Of Sale et Crowdfund sont les deux plugins principaux de BTCPay Server. Avec chaque magasin et Wallet, un utilisateur de BTCPay Server peut generate autant de points de vente ou de crowdfunds qu'il le souhaite. Chacun d'entre eux créera une nouvelle tuile de tableau de bord montrant la performance des plugins.


![image](assets/en/047.webp)


Remarquez la légère différence entre une tuile Point de vente et une tuile Crowdfund. L'administrateur voit les articles les plus vendus dans la tuile Point de vente. Dans la tuile Crowdfund, cela devient Top Perks. Les deux tuiles sont dotées de boutons rapides permettant de gérer les applications respectives et de consulter les factures récentes créées par les meilleurs articles ou les meilleurs avantages.


![image](assets/en/048.webp)


**!Note!**


Les graphiques de solde et les transactions récentes ne sont disponibles que pour les méthodes de paiement On-Chain. Les informations sur les soldes et les transactions Lightning Network sont sur la liste des choses à faire. Depuis la version 1.6.0 de BTCPay Server, les soldes de base Lightning Network sont disponibles.


### Résumé des compétences


Dans cette section, vous avez appris ce qui suit :



- La disposition principale des tuiles sur la page d'accueil principale est connue sous le nom de tableau de bord.
- Une compréhension de base du contenu de chaque tuile.


### Examen de l'évaluation des connaissances


Listez autant de tuiles de mémoire que possible à partir du tableau de bord.


## Serveur BTCPay - Paramètres du magasin


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


Dans le logiciel de BTCPay Server, nous connaissons deux types de paramètres. Les paramètres spécifiques à la boutique de BTCPay Server, le bouton des paramètres se trouvant dans la barre de menu de gauche sous le tableau de bord, et les paramètres de BTCPay Server, se trouvant en bas de la barre de menu, juste au-dessus de Compte. Les paramètres spécifiques au serveur de BTCPay ne peuvent être consultés que par les administrateurs du serveur.


Les paramètres du magasin se composent de nombreux onglets permettant de classer chaque ensemble de paramètres.



- Général
- Tarifs
- Apparence de la caisse
- Jetons d'accès
- Utilisateurs
- Rôles
- Crochets Web
- Processeurs de paiement
- Courriels
- Formulaires


### Général


Dans l'onglet Paramètres généraux, les propriétaires de magasins définissent leur marque et leurs paramètres de paiement par défaut. Lors de la configuration initiale du magasin, un nom de magasin a été donné ; il sera reflété dans les paramètres généraux sous Nom du magasin. Ici, le propriétaire du magasin peut également configurer son site web pour qu'il corresponde à son image de marque, ainsi qu'un identifiant de magasin que l'administrateur reconnaîtra dans la base de données.


#### L'image de marque


Comme BTCPay Server est un logiciel libre, le propriétaire d'une boutique peut personnaliser sa marque pour qu'elle corresponde à sa boutique. Définissez la couleur de la marque, stockez les logos de votre marque, et ajoutez des CSS personnalisés pour les pages publiques/clients (Factures, Demandes de paiement, Paiements Pull)


#### Paiement


Dans les paramètres de paiement, les propriétaires de magasins peuvent définir la devise par défaut de leur magasin (Bitcoin ou toute autre devise fiduciaire).


#### Permettre à n'importe qui de créer des factures


Ce paramètre est destiné aux développeurs ou aux constructeurs de BTCPay Server. Lorsque ce paramètre est activé pour votre boutique, il permet au monde extérieur de créer des factures sur votre instance de BTCPay Server.


#### Ajouter des frais supplémentaires (frais de réseau) aux factures


Une fonction de BTCPay pour protéger les marchands des attaques Dust ou les clients d'encourir des frais élevés plus tard lorsque le marchand a besoin de déplacer une grande quantité de Bitcoin en une seule fois. Par exemple, le client a créé une Invoice pour 20$ et l'a payée partiellement, en payant 1$ 20 fois jusqu'à ce que la Invoice soit entièrement payée. Le commerçant a maintenant une transaction plus importante, ce qui augmente le coût de la Mining si le commerçant décide de transférer ces fonds plus tard. Par défaut, BTCPay applique un coût de réseau supplémentaire au montant total de la Invoice afin de couvrir cette dépense pour le commerçant lorsque la Invoice est payée en plusieurs transactions. BTCPay offre plusieurs options pour personnaliser cette fonction de protection. Vous pouvez appliquer des frais de réseau :



- Uniquement si le client effectue plus d'un paiement pour la Invoice (dans l'exemple ci-dessus, si le client a créé une Invoice pour 20 $ et a payé 1 $, la Invoice totale due est maintenant de 19 $ + la redevance de réseau. Les frais de réseau sont appliqués après le premier paiement)
- Sur chaque paiement (y compris le premier paiement, dans notre exemple, le total sera de 20 $ + les frais de réseau immédiatement, même sur le premier paiement)
- Ne jamais ajouter de frais de réseau (désactive complètement les frais de réseau)


Bien qu'elle protège contre les transactions Dust, elle peut également avoir un effet négatif sur les entreprises si elle n'est pas communiquée correctement. Les clients peuvent avoir des questions supplémentaires et penser que vous les surfacturez.


#### La Invoice expire si le montant total n'a pas été payé après ?


La minuterie Invoice est réglée par défaut sur 15 minutes. Le minuteur sert de mécanisme de protection contre la volatilité, car il bloque le montant de la Bitcoin en fonction des taux Bitcoin-to-fiat Exchange. Si le client ne paie pas la Invoice dans la période définie, la Invoice est considérée comme expirée. La Invoice est considérée comme "payée" dès que la transaction est visible sur la Blockchain (avec zéro confirmation), et est "complète" lorsqu'elle atteint le nombre de confirmations défini par le commerçant (généralement de 1 à 6). Le minuteur est personnalisable en minutes.


#### La Invoice est-elle considérée comme payée même si le montant payé est inférieur de X % au montant prévu ?


Lorsqu'un client utilise une Exchange Wallet pour payer directement une Invoice, la Exchange prend une petite commission. Cela signifie que cette Invoice n'est pas considérée comme entièrement achevée. La Invoice est marquée comme "payée partiellement". Vous pouvez définir le taux de pourcentage ici si un commerçant souhaite accepter des factures insuffisamment payées.


### Tarifs


Dans BTCPay Server, lorsqu'un Invoice est généré, il a toujours besoin du prix Bitcoin-to-fiat le plus récent et le plus précis. Lors de la création d'un nouveau magasin dans BTCPay Server, les administrateurs sont invités à définir leur source de prix préférée. Une fois la boutique configurée, les propriétaires de la boutique peuvent à tout moment modifier leur source de prix dans cet onglet.


#### Scripting avancé des règles de tarification


Principalement utilisé par les utilisateurs chevronnés. S'il est activé, les propriétaires de magasins peuvent créer des scripts sur le comportement des prix et la manière de facturer leurs clients.


#### Essais


Un lieu de test rapide pour vos paires de devises préférées. Cette fonctionnalité inclut également la possibilité de vérifier les paires de devises par défaut via une requête REST.


### Apparence de la caisse


L'onglet "Checkout Appearance" commence par des paramètres spécifiques à Invoice et une méthode de paiement par défaut, puis active des méthodes de paiement spécifiques lorsque les conditions requises sont remplies.


#### Paramètres Invoice


Méthodes de paiement par défaut. Le serveur BTCPay, dans sa configuration standard, offre trois options.



- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain & Lightning)


Nous pouvons définir des paramètres pour notre magasin, où un client n'interagira avec Lightning que lorsque le prix est inférieur à un montant X, et vice versa pour les transactions On-Chain, lorsque X est supérieur à Y, toujours présenter l'option de paiement On-Chain.


![image](assets/en/049.webp)


#### Sortie de caisse


Depuis la version 1.7 de BTCPay Server, un nouveau Checkout Interface, Checkout V2, a été introduit. Depuis que la version 1.9 a été standardisée, les administrateurs et les propriétaires de magasins peuvent toujours régler la caisse sur la version précédente. En utilisant l'option "Use the classic checkout", le propriétaire d'une boutique peut revenir à l'ancienne méthode de paiement. BTCPay Server dispose également d'un ensemble de préréglages sélectionnés pour le commerce en ligne ou l'expérience en magasin.


![image](assets/en/050.webp)


Lorsqu'un client interagit avec la boutique et génère une Invoice, il y a un délai d'expiration pour la Invoice. Par défaut, BTCPay Server fixe ce délai à 5 minutes, mais les administrateurs peuvent l'adapter à leurs préférences. La page de paiement peut également être personnalisée en vérifiant les paramètres suivants :



- Célébrer le paiement en montrant des confettis
- Afficher l'en-tête du magasin (nom et logo)
- Afficher le bouton "Pay in Wallet" (payer en Wallet)
- Unifier les URL/QR des paiements On-Chain et off-chain
- Affichage des montants des paiements éclairs en Satoshis
- Détection automatique de la langue lors du paiement


![image](assets/en/051.webp)


Lorsque la fonction de détection automatique de la langue n'est pas activée, le serveur BTCPay affiche par défaut l'anglais. Le propriétaire d'un magasin peut modifier cette valeur par défaut pour la remplacer par la langue de son choix.


![image](assets/en/052.webp)


Cliquez sur le menu déroulant et les propriétaires de magasins peuvent définir un titre HTML personnalisé à afficher sur la page de paiement.


![image](assets/en/053.webp)


Pour s'assurer que les clients connaissent leur méthode de paiement, le propriétaire d'une boutique peut explicitement paramétrer son processus de paiement pour demander aux utilisateurs de choisir leur méthode de paiement préférée. Une fois que le Invoice est payé, le serveur BTCPay permet au client de retourner à la boutique en ligne. Les propriétaires de magasins peuvent paramétrer cette redirection pour qu'elle soit automatiquement appliquée après le paiement du client.


![image](assets/en/054.webp)


#### Réception du public


Dans les paramètres des reçus publics, le propriétaire d'un magasin peut rendre les pages de reçus publiques, en affichant la liste des paiements sur la page de reçus et le code QR pour que le client puisse y accéder facilement.


![image](assets/en/055.webp)


### Jetons d'accès


Les jetons d'accès sont utilisés pour l'appariement avec certaines intégrations de commerce électronique ou des intégrations personnalisées.


![image](assets/en/056.webp)


### Utilisateurs


Les utilisateurs du magasin sont l'endroit où le propriétaire du magasin peut gérer les membres de son personnel, leurs comptes et l'accès au magasin. Une fois que les membres du personnel ont créé leur compte, le propriétaire du magasin peut ajouter des utilisateurs spécifiques au magasin en tant qu'utilisateurs invités ou propriétaires. Pour définir plus précisément le rôle de l'employé, reportez-vous à la section suivante "Paramètres de la boutique de BTCPay Server - Rôles"


![image](assets/en/057.webp)


### Rôles


Le propriétaire d'un magasin peut estimer que les rôles standard de l'utilisateur ne sont pas suffisamment importants. Dans les paramètres des rôles personnalisés, le propriétaire d'un magasin peut définir les besoins exacts de chaque rôle dans son entreprise.


(1) Pour créer un nouveau rôle, cliquez sur le bouton "+ Ajouter un rôle".


![image](assets/en/058.webp)


(2) Saisissez un nom de rôle, par exemple "Caissier".


![image](assets/en/059.webp)


(3) Configurez les autorisations individuelles pour le rôle.



- Modifiez vos magasins.
- Gérer les comptes Exchange liés à vos magasins.
  - Voir les comptes Exchange liés à vos magasins.
- Gérez vos paiements de tirage.
- Créer des paiements tirés.
  - Créer des paiements tirés non approuvés.
- Modifier les factures.
  - Consulter les factures.
  - Créer une Invoice.
  - Créez des factures à partir des nœuds lumineux associés à vos magasins.
- Voir vos magasins.
  - Consulter les factures.
  - Consulter vos demandes de paiement.
  - Modifier les webhooks des magasins.
- Modifier vos demandes de paiement.
  - Consulter vos demandes de paiement.
- Utilisez les nœuds de foudre associés à vos magasins.
  - Visualisez les factures éclair associées à vos magasins.
  - Créez des factures à partir des nœuds lumineux associés à vos magasins.
- Déposez des fonds sur les comptes Exchange liés à vos magasins.
- Retirer des fonds des comptes Exchange vers votre magasin.
- Échangez des fonds sur les comptes Exchange de votre magasin.


Lorsque le rôle est créé, le nom est fixe et ne peut être modifié une fois qu'il est en mode édition.


![image](assets/en/060.webp)


### Crochets Web


Dans BTCPay Server, il est relativement facile de créer un nouveau "Webhook". Dans les paramètres de la boutique de BTCPay Server - onglet Webhooks, un propriétaire de boutique peut facilement créer un nouveau webhook en cliquant sur le bouton "+ Create Webhook". Les Webhooks permettent à BTCPay Server d'envoyer des événements HTTP liés à votre boutique à d'autres serveurs ou intégrations de commerce électronique.


![image](assets/en/061.webp)


Vous êtes maintenant dans la vue de création d'un Webhook. Assurez-vous de connaître l'URL de la charge utile et collez-la dans votre serveur BTCPay. Lorsque vous avez collé l'URL de la charge utile, le secret du webhook apparaît en dessous. Copiez le secret du webhook et fournissez-le au point de terminaison. Une fois que tout a été configuré, vous pouvez basculer dans BTCPay Server sur "Automatic redelivery" BTCPay Server essaiera de relivrer toute livraison échouée après 10 secondes, 1 minute, et jusqu'à 6 fois après 10 minutes. Vous pouvez basculer entre chaque événement ou spécifier les événements en fonction de vos besoins. Assurez-vous d'activer le webhook et cliquez sur le bouton "Add webhook" pour le sauvegarder.


![image](assets/en/062.webp)


Les Webhooks ne sont pas conçus pour être compatibles avec l'API Bitpay. Il existe deux IPN distincts (en termes de BitPay : "Notifications de paiement instantané") dans le serveur BTCPay.



- Webhookp
- Notifications


N'utilisez l'URL de notification que lorsque vous créez des factures via l'API Bitpay.


### Processeurs de paiement


Les processeurs de paiement fonctionnent avec le concept de paiement de BTCPay Server. Un agrégateur de paiements permet de regrouper plusieurs transactions et de les envoyer en une seule fois. Avec les processeurs de paiement, le propriétaire d'une boutique peut automatiser les paiements par lots. BTCPay Server offre deux méthodes de paiements automatisés : On-Chain et off-chain (LN).


Le propriétaire du magasin peut cliquer sur les deux processeurs de paiement et les configurer séparément. Un propriétaire de magasin peut vouloir exécuter le processeur On-Chain une fois toutes les X heures, alors que le processeur off-chain peut être exécuté toutes les quelques minutes. Pour le On-Chain, vous pouvez également définir un objectif pour le bloc dans lequel il doit être inclus. Par défaut, cette valeur est fixée à 1 (ou au prochain bloc disponible). Notez que la configuration du processeur de paiement off-chain ne comporte que le minuteur d'intervalle et pas d'objectif de bloc. Les paiements de la Lightning Network sont instantanés.


![image](assets/en/063.webp)

![image](assets/en/064.webp)


Les propriétaires de magasins ne peuvent configurer le processeur On-Chain que si un Hot Wallet est connecté à leur magasin.


![image](assets/en/065.webp)


Après avoir configuré un processeur de paiement, vous pouvez rapidement le supprimer ou le modifier en retournant à l'onglet Processeur de paiement dans les paramètres du magasin du serveur BTCPay.


**Note**


Processeur de paiement On-Chain - Le processeur de paiement On-Chain ne peut fonctionner que sur une boutique configurée avec un Hot Wallet connecté. Si aucun Hot Wallet n'est connecté, le serveur BTCPay ne détient pas les clés Wallet et ne sera pas en mesure de traiter les paiements automatiquement.


### Courriels


BTCPay Server peut utiliser les e-mails pour les notifications ou, lorsqu'ils sont correctement configurés, pour récupérer les comptes créés sur l'instance. Par défaut, BTCPay Server n'envoie pas d'e-mail en cas de perte du mot de passe, par exemple.


![image](assets/en/066.webp)


Avant qu'un propriétaire de boutique puisse définir des règles d'envoi de courriels pour déclencher des événements spécifiques dans sa boutique, il doit d'abord définir quelques paramètres de base pour les courriels. BTCPay Server a besoin de ces paramètres pour envoyer des courriels pour les événements liés à votre boutique ou pour les réinitialisations de mot de passe.


Le serveur BTCPay a facilité le remplissage de ces informations en utilisant l'option "Quick Fill" :



- Gmail.com
- Yahoo.com
- Arme à feu
- Office365
- SendGrid


En utilisant l'option de remplissage rapide, BTCPay Server pré-remplit les champs pour le serveur SMTP et le port. Le propriétaire de la boutique n'a plus qu'à remplir ses informations d'identification, y compris l'adresse électronique Address, le login (qui correspond généralement à votre adresse électronique Address) et son mot de passe. L'option avancée dans les paramètres de messagerie du serveur BTCPay consiste à désactiver les contrôles de sécurité du certificat TLS ; par défaut, cette option est activée.


![image](assets/en/067.webp)


Grâce aux règles d'e-mail, le propriétaire d'un magasin peut définir des événements spécifiques qui déclencheront l'envoi d'e-mails à des adresses électroniques spécifiques.



- Invoice Créé
- Invoice Paiement reçu
- Traitement de la Invoice
- Invoice Périmé
- Invoice réglée
- Invoice Invalide
- Invoice Paiement réglé


Si le client a fourni un courriel Address, ces déclencheurs peuvent également envoyer l'information au client. Les propriétaires de magasins peuvent pré-remplir la ligne Objet afin d'indiquer clairement la raison de l'envoi de cet e-mail et ce qui l'a déclenché.


![image](assets/en/068.webp)


### Formulaires


Étant donné que BTCPay Server ne collecte aucune donnée, le propriétaire d'une boutique peut souhaiter ajouter un formulaire personnalisé à son processus de paiement ; de cette façon, il peut collecter des informations supplémentaires auprès de ses clients. Le constructeur de formulaires de BTCPay Server se compose de deux parties : une vue visuelle et une vue plus avancée du code des formulaires.


Lors de la création d'un nouveau formulaire, BTCPay Server ouvre une nouvelle fenêtre demandant des informations de base sur ce que vous voulez que votre nouveau formulaire demande. Tout d'abord, le propriétaire de la boutique doit donner un nom clair à son nouveau formulaire ; ce nom ne peut pas être modifié une fois qu'il a été défini.


![image](assets/en/069.webp)


Une fois que le propriétaire du magasin a donné un nom au formulaire, vous pouvez également activer l'interrupteur "Autoriser l'utilisation publique du formulaire", qui deviendra Green. Cela permet de s'assurer que le formulaire est utilisé dans tous les points de vente en contact avec la clientèle. Par exemple, si le propriétaire d'un magasin crée un formulaire Invoice distinct qui n'est pas utilisé dans son point de vente, il peut souhaiter recueillir des informations auprès du client. Cette option permet de collecter ces informations.


![image](assets/en/070.webp)


Chaque formulaire commence par au moins un nouveau champ. Le propriétaire du magasin peut choisir le type de champ.



- Texte
- Nombre
- Mot de passe
- Courriel
- URL
- Numéros de téléphone
- Date
- Champs cachés
- Fieldset (jeu de mots)
- Une zone de texte pour les commentaires libres.
- Sélecteur d'options


Chaque type est accompagné de ses propres paramètres à remplir. Le propriétaire du magasin peut les définir à sa guise. En dessous du premier champ créé, les propriétaires de magasins peuvent ajouter de nouveaux champs à ce formulaire.


![image](assets/en/071.webp)


#### Formulaires personnalisés avancés


BTCPay Server vous permet également de construire des formulaires en code. JSON, en particulier. Au lieu de regarder l'éditeur, les propriétaires de magasins peuvent cliquer sur le bouton CODE juste à côté de l'éditeur et entrer dans le code de leurs formulaires. Dans une définition de champ, seuls les champs suivants peuvent être définis ; les valeurs des champs sont stockées dans les métadonnées de la Invoice :


| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | If true, the .value must be set in the form definition, and the user will not be able to change the field's value. ( example: the form definition's version)                                                                                                                                                                                                                                                                                                       |
| .fields.type          | The HTML input type text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                |
| .fields.options       | If .fields.type is select, the list of selectable values                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.options.text  | The text displayed for this option                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.value | The value of the field if this option is selected                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.type=fieldset | Create a HTML fieldset around the children .fields.fields (see below)                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.name          | The JSON property name of the field as it will appear in the invoice's metadata                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.value         | The default value of the field                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.required      | if true, the field will be required                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.label         | The label of the field                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.helpText      | Additional text to provide an explanation for the field.                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.fields        | You can organize your fields in a hierarchy, allowing child fields to be nested within the invoice’s metadata. This structure can help you better organize and manage the collected information, making it easier to access and interpret. For example, if you have a form that collects customer information, you can group the fields under a parent field called customer. Within this parent field, you might have child fields like name, Email, and address. |

Le nom du champ représente le nom de la propriété JSON qui stocke la valeur fournie par l'utilisateur dans les métadonnées du Invoice. Certains noms bien connus peuvent être interprétés et modifiés pour ajuster les paramètres du Invoice.


| Field name       | Description            |
| ---------------- | ---------------------- |
| invoice_amount   | The invoice's amount   |
| invoice_currency | The invoice's currency |

Vous pouvez pré-remplir automatiquement les champs d'un formulaire Invoice en ajoutant des chaînes de requête à l'URL du formulaire, telles que "?votre_champ=valeur".


Voici quelques cas d'utilisation de cette fonctionnalité :



- Aide à la saisie par l'utilisateur : Pré-remplir les champs avec des informations connues sur le client afin de faciliter le remplissage du formulaire. Par exemple, si vous connaissez déjà l'adresse électronique d'un client Address, vous pouvez pré-remplir le champ de l'adresse électronique pour lui faire gagner du temps.
- Personnalisation : Personnalisez le formulaire en fonction des préférences des clients ou de la segmentation. Par exemple, si vous avez différents niveaux de clients, vous pouvez pré-remplir le formulaire avec des données pertinentes, telles que leur niveau d'adhésion ou des offres spécifiques.
- Suivi : Suivez la source des visites des clients à l'aide de champs cachés et de valeurs pré-remplies. Par exemple, vous pouvez créer des liens avec des valeurs utm_media pré-remplies pour chaque canal de marketing (par exemple, Twitter, Facebook, Email). Cela vous permet d'analyser l'efficacité de vos efforts de marketing.
- Tests A/B : Remplissez les champs avec différentes valeurs pour tester différentes versions du formulaire, ce qui vous permet d'optimiser l'expérience de l'utilisateur et les taux de conversion.


### Résumé des compétences


Dans cette section, vous avez appris ce qui suit :



- La disposition et les fonctions des onglets dans les paramètres du magasin
- Une multitude d'options pour affiner le traitement des taux Exchange sous-jacents, des paiements partiels, des légers sous-paiements, etc.
- Personnaliser l'apparence de la caisse, y compris la chaîne principale en fonction du prix par rapport à l'activation de Lightning sur les factures.
- Gérer les niveaux d'accès au magasin et les autorisations en fonction des rôles.
- Configurer les courriels automatisés et leurs déclencheurs
- Créez des formulaires personnalisés pour recueillir des informations supplémentaires sur le client au moment du paiement.


### Évaluation des connaissances


#### Revue KA


Quelle est la différence entre les paramètres du magasin et les paramètres du serveur ?


#### KA Hypothétique


Décrivez certaines options que vous pourriez sélectionner dans Apparence de la caisse > Paramètres Invoice, et expliquez pourquoi.


## BTCPay Server - Paramètres du serveur


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


BTCPay Server se compose de deux vues de paramétrage différentes. L'une est consacrée aux paramètres de la boutique et l'autre aux paramètres du serveur. Cette dernière n'est disponible que pour les administrateurs de serveur et non pour les propriétaires de boutiques. Les administrateurs du serveur peuvent ajouter des utilisateurs, créer des rôles personnalisés, configurer le serveur de messagerie, définir des politiques, exécuter des tâches de maintenance, vérifier tous les services liés à BTCPay Server, télécharger des fichiers vers le serveur ou vérifier les journaux.


### Utilisateurs


Comme mentionné dans la partie précédente, les administrateurs de serveur peuvent inviter des utilisateurs sur leur serveur en les ajoutant à l'onglet Utilisateurs.


### Rôles personnalisés à l'échelle du serveur


BTCPay Server dispose de deux types de rôles personnalisés : les rôles personnalisés spécifiques aux magasins et les rôles personnalisés à l'échelle du serveur dans les paramètres de BTCPay Server. Les deux détiennent un ensemble similaire d'autorisations ; cependant, s'ils sont définis par le biais des Paramètres de BTCPay Server - onglet Rôles, le rôle appliqué sera à l'échelle du serveur et s'appliquera à plusieurs magasins. Notez que les rôles personnalisés dans les paramètres du serveur sont marqués "à l'échelle du serveur".


![image](assets/en/072.webp)


### Rôles personnalisés à l'échelle du serveur


Jeu d'autorisations pour les rôles personnalisés à l'échelle du serveur ;



- Modifiez vos magasins.
- Gérer les comptes Exchange liés à vos magasins.
  - Visualisez les comptes Exchange liés à vos magasins.
- Gérez vos paiements de tirage.
- Créer des paiements tirés.
  - Créer des paiements tirés non approuvés.
- Modifier les factures.
  - Consulter les factures.
  - Créer une Invoice.
  - Créez des factures à partir des nœuds lumineux associés à vos magasins.
- Voir vos magasins.
  - Consulter les factures.
  - Consulter vos demandes de paiement.
  - Modifier les webhooks des magasins.
- Modifier vos demandes de paiement.
  - Consulter vos demandes de paiement.
- Utilisez les nœuds de foudre associés à vos magasins.
  - Visualisez les factures éclair associées à vos magasins.
  - Créez des factures à partir des nœuds lumineux associés à vos magasins.
- Déposez des fonds sur les comptes Exchange liés à vos magasins.
- Retirer des fonds des comptes Exchange vers votre magasin.
- Échangez des fonds sur les comptes Exchange de votre magasin.


**!Note!**


Lorsque le rôle est créé, le nom est fixe et ne peut être modifié une fois qu'il est en mode édition.


### Courriel


Les paramètres de courrier électronique pour l'ensemble du serveur sont similaires à ceux des paramètres de courrier électronique spécifiques aux points de vente. Cependant, cette configuration gère non seulement les déclencheurs pour les magasins ou les journaux des administrateurs, mais aussi les déclencheurs pour d'autres événements. Cette configuration d'email rend également la récupération du mot de passe disponible sur le serveur BTCPay lors de la connexion. Elle fonctionne de la même manière que les paramètres spécifiques aux magasins ; les administrateurs peuvent rapidement remplir leurs paramètres d'email et entrer leurs informations d'identification, ce qui permet au serveur d'envoyer des emails.


![image](assets/en/073.webp)


### Politiques


Les administrateurs de politiques de BTCPay Server peuvent définir divers paramètres sur des sujets tels que les paramètres des utilisateurs existants, les paramètres des nouveaux utilisateurs, les paramètres de notification et les paramètres de maintenance. Ces paramètres sont destinés à enregistrer les nouveaux utilisateurs en tant qu'administrateurs ou utilisateurs réguliers, ou à cacher le serveur BTCPay aux moteurs de recherche en l'ajoutant à l'en-tête de votre serveur.


![image](assets/en/074.webp)


#### Utilisateur existant Paramètres


Les options disponibles ici sont distinctes des rôles personnalisés. Ces autorisations supplémentaires peuvent rendre un magasin ou son propriétaire vulnérable aux attaques. Politiques pouvant être ajoutées aux utilisateurs existants :



- Permettre aux non-administrateurs d'utiliser le nœud interne de Lightning dans leurs magasins.
  - Cela permettrait aux propriétaires de magasins d'utiliser le nœud Lightning de l'administrateur du serveur et, par conséquent, ses fonds ! Attention, il ne s'agit pas d'une solution pour donner accès à Lightning.
- Permettre aux non-administrateurs de créer des portefeuilles Hot pour leurs magasins.
  - Cela permettrait à toute personne ayant un compte sur votre instance de serveur BTCPay de créer des portefeuilles Hot et de stocker leur récupération seed sur le serveur de l'administrateur. Cela pourrait rendre l'administrateur responsable de la détention de fonds de tiers !
- Permettre aux non-administrateurs d'importer des portefeuilles Hot pour leurs magasins.
  - Comme pour la création de portefeuilles Hot, cette politique permet d'importer un Hot Wallet, avec les mêmes dangers que ceux mentionnés dans la section sur la création de portefeuilles Hot.


![image](assets/en/075.webp)


#### Paramètres du nouvel utilisateur


Nous pouvons définir certains paramètres importants pour gérer les nouveaux utilisateurs arrivant sur le serveur. Nous pouvons définir un courriel de confirmation pour les nouveaux enregistrements, désactiver la création de nouveaux utilisateurs via l'écran de connexion et restreindre l'accès des non-administrateurs à la création d'utilisateurs via l'API.



- Exiger un courriel de confirmation pour l'inscription.
  - L'administrateur du serveur doit avoir mis en place un serveur de courrier électronique.
- Désactiver l'enregistrement de nouveaux utilisateurs sur le serveur
- Désactiver l'accès des non-administrateurs au point de terminaison de l'API de création d'utilisateurs.


Par défaut, BTCPay Server a désactivé l'option "Disable new user registration on the server" (Désactiver l'enregistrement de nouveaux utilisateurs sur le serveur) et a désactivé l'accès des non-administrateurs au point de terminaison de l'API de création d'utilisateurs. C'est pour des raisons de sécurité, afin que les personnes qui tombent par hasard sur votre login BTCPay ne puissent pas créer de comptes.


![image](assets/en/076.webp)


#### Paramètres de notification


![image](assets/en/077.webp)


#### Paramètres de maintenance


BTCPay Server est un projet Open Source qui vit sur GitHub. Chaque fois que BTCPay Server publie une nouvelle version du logiciel, les administrateurs peuvent être informés qu'une nouvelle version est disponible. Les administrateurs peuvent également vouloir éviter que les moteurs de recherche (tels que Google, Yahoo et DuckDuckGo) n'indexent le domaine de BTCPay Server. BTCPay Server étant un logiciel libre, les développeurs du monde entier peuvent vouloir créer de nouvelles fonctionnalités. BTCPay Server dispose d'une fonction expérimentale qui, lorsqu'elle est activée, permet aux administrateurs d'utiliser des fonctions qui ne sont pas destinées à la production, mais plutôt à des fins de test.



- Vérifiez les versions sur GitHub et soyez averti lorsqu'une nouvelle version de BTCPay Server est disponible.
- Décourager les moteurs de recherche d'indexer ce site
- Activer les fonctions expérimentales.


![image](assets/en/078.webp)


#### Plugins


BTCPay Server peut ajouter des plugins et étendre ses fonctionnalités. Les plugins, par défaut, sont chargés à partir du dépôt de BTCPay Server plugin-builder. Un administrateur peut cependant choisir de voir les plugins dans un état de préversion, et si le développeur du plugin l'autorise, l'administrateur du serveur peut maintenant installer des versions bêta des plugins.


![image](assets/en/079.webp)


##### Paramètres de personnalisation


Un déploiement standard de BTCPay Server sera accessible via le domaine défini lors de l'installation. Cependant, un administrateur de serveur peut réaffecter le domaine racine et afficher l'une des applications créées à partir d'un magasin spécifique. L'administrateur du serveur peut également associer des domaines spécifiques à des applications spécifiques.



- Afficher l'application à la racine du site web
  - Affiche une liste d'applications possibles à afficher sur le domaine racine.


![image](assets/en/080.webp)



- Associer des domaines spécifiques à des applications spécifiques.
  - Lorsque vous cliquez pour configurer un domaine spécifique pour des applications spécifiques, l'administrateur peut configurer autant de domaines pointant vers des applications spécifiques que nécessaire.


![image](assets/en/081.webp)


#### Explorateurs de blocs


BTCPay Server est livré en standard avec Mempool.space comme Block explorer pour les transactions. Lorsque BTCPay Server génère un nouveau Invoice et qu'une transaction y est liée, le propriétaire du magasin peut cliquer pour ouvrir la transaction. Par défaut, BTCPay Server pointera vers Mempool.space en tant que Block explorer ; cependant, un administrateur de serveur peut changer cette option pour celle qu'il préfère.


![image](assets/en/082.webp)


### Services


L'onglet "Paramètres de BTCPay Server : Services" est un aperçu des composants utilisés par votre serveur BTCPay. Les services que votre BTCPay Server expose peuvent varier en fonction de la méthode de déploiement.


Un administrateur du serveur de BTCPay peut cliquer sur "Voir les informations" derrière chaque service pour l'ouvrir et définir des paramètres spécifiques.


![image](assets/en/083.webp)


#### LND (gRPC)


BTCPay expose le service GRPC du LND pour la consommation extérieure ; vous trouverez des informations de connexion dans ce menu de paramètres spécifique ; les portefeuilles compatibles sont listés ici. Le serveur BTCPay fournit également un code QR pour la connexion, qui peut être scanné et appliqué dans un Wallet mobile.


Les administrateurs de serveur peuvent ouvrir plus de détails pour voir.



- Coordonnées de l'hôte
- Utilisation de SSL
- Macaron
- AdminMacaron
- FactureMacaron
- Macaron en lecture seule
- Suite de chiffrement SSL GRPC (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


BTCPay expose le service REST de LND pour la consommation externe ; vous trouverez les informations de connexion [ici]((https://docs.btcpayserver.org/FAQ/LightningNetwork/#how-to-find-node-info-and-open-a-direct-channel-with-a-store-using-btcpay)) ; les portefeuilles compatibles sont listés [ici](https://docs.btcpayserver.org/FAQ/Wallet/#can-i-use-a-hardware-wallet-with-btcpay-server). Parmi les portefeuilles compatibles figurent Joule, Alby et ZeusLN. Le serveur BTCPay fournit un code QR pour la connexion, qui peut être scanné et appliqué dans un Wallet compatible.



- URI REST
- Macaron
- AdminMacaron
- FactureMacaron
- Macaron en lecture seule


#### LND seed Sauvegarde


La sauvegarde LND seed est utile pour récupérer les fonds de votre LND Wallet en cas de corruption du serveur. Le nœud Lightning étant un Hot-Wallet, vous trouverez sur cette page les informations confidentielles relatives au seed.


LND documente le processus de récupération. Voir https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md pour la documentation.


#### La foudre au bout des doigts


Ride the Lightning est un outil de gestion des nœuds Lightning construit en tant que logiciel Open Source. BTCPay Server utilise RTL comme composant de gestion de nœuds Lightning dans sa pile. Les administrateurs de BTCPay Server peuvent accéder à RTL via les paramètres du serveur - onglet Services ou en cliquant sur le Wallet de Lightning.


#### Full node P2P


Les administrateurs de serveur peuvent vouloir connecter leur nœud Bitcoin à un Wallet mobile. Cette page fournit des informations sur la façon de se connecter à distance à votre Full node via le protocole P2P. Au moment de la rédaction de ce cours, BTCPay Server répertorie les portefeuilles Blockstream Green et Wasabi comme portefeuilles compatibles. BTCPay Server fournit un code QR pour la connexion, qui peut être scanné et appliqué dans un Wallet compatible.


#### Full node RPC


Cette page expose les informations permettant de se connecter à distance à votre Full node via le protocole RPC.


#### SSH


SSH est utilisé à des fins de maintenance. BTCPay Server affiche la commande de connexion initiale pour atteindre votre serveur et les clés publiques SSH autorisées à se connecter à votre serveur. Les administrateurs du serveur peuvent vouloir désactiver les changements SSH via l'interface utilisateur de BTCPay Server.


#### DNS dynamique


Le DNS dynamique vous permet d'avoir un nom DNS stable pointant vers votre serveur, même si votre IP Address change régulièrement. Ceci est recommandé si vous hébergez le serveur BTCPay chez vous et que vous souhaitez avoir un domaine clair pour accéder à votre serveur.


Notez que vous devez configurer correctement votre NAT et l'installation de BTCPay Server pour obtenir le certificat HTTPS.


### Thème


BTCPay Server est livré en standard avec deux thèmes : Light et Dark. Ceux-ci peuvent être changés en cliquant sur Compte en bas à gauche et en basculant entre le thème Sombre et le thème Clair. Les administrateurs de BTCPay Server peuvent ajouter leur propre thème en fournissant un thème CSS personnalisé.


Les administrateurs peuvent étendre le thème Light/Dark en ajoutant leur propre CSS personnalisé ou en définissant leur thème personnalisé comme un thème entièrement personnalisé.


![image](assets/en/084.webp)


#### L'image de marque du serveur


Les administrateurs de serveur peuvent modifier l'image de marque de BTCPay Server en définissant une image de marque de votre entreprise pour l'ensemble du serveur. Comme BTCPay Server est un logiciel libre, les administrateurs de serveur peuvent mettre le logiciel en marque blanche et personnaliser l'apparence pour l'adapter à leur entreprise.


![image](assets/en/085.webp)


### Maintenance


En tant qu'administrateur de serveur, vos utilisateurs attendent de vous que vous preniez soin du serveur. Dans l'onglet Maintenance de BTCPay Server, l'administrateur peut effectuer quelques opérations de maintenance essentielles. Définir le nom de domaine de l'instance de BTCPay Server, redémarrer ou nettoyer le serveur. Peut-être le plus important, exécuter des mises à jour.


BTCPay Server est un projet Open Source et est fréquemment mis à jour. Chaque nouvelle version est annoncée soit par les notifications de BTCPay Server, soit sur les canaux officiels par lesquels BTCPay Server communique.


![image](assets/en/086.webp)


#### Nom de domaine


Après la mise en place de BTCPay Server, un administrateur peut vouloir changer de domaine. Dans l'onglet Maintenance, l'administrateur peut changer de domaine. Après avoir cliqué sur confirmer et configuré les enregistrements DNS appropriés sur le domaine, BTCPay Server se met à jour et redémarre pour revenir au nouveau domaine.


![image](assets/en/087.webp)


#### Redémarrage


Redémarrez le serveur BTCPay et les services associés.


![image](assets/en/088.webp)


#### Nettoyer


BTCPay Server fonctionne avec des composants Docker ; avec les mises à jour, il peut y avoir des restes d'images Docker, des fichiers temporaires, etc. Les administrateurs du serveur peuvent libérer de l'espace en exécutant le script Clean.


![image](assets/en/089.webp)


#### Mise à jour


C'est l'option la plus importante de l'onglet Maintenance. BTCPay Server est construit par la communauté et, par conséquent, ses cycles de mise à jour sont plus fréquents que ceux de la plupart des logiciels. Lorsque BTCPay Server a une nouvelle version, les administrateurs en seront informés dans leur centre de notification. En cliquant sur le bouton de mise à jour, BTCPay Server vérifiera GitHub pour la dernière version, mettra à jour le serveur et redémarrera. Avant de procéder à une mise à jour, il est toujours conseillé aux administrateurs de serveur de lire les notes de version distribuées par les canaux officiels de BTCPay Server.


![image](assets/en/090.webp)


### Journaux


Il n'est jamais agréable d'être confronté à un problème. Ce document décrit le déroulement des opérations et les étapes les plus courantes pour identifier et résoudre efficacement votre problème, de manière autonome ou avec l'aide de la communauté.


L'identification du problème est cruciale.


#### Reproduction du problème


Avant tout, essayez de déterminer à quel moment le problème se produit. Essayez de reproduire le problème. Essayez de mettre à jour et de redémarrer votre serveur pour vérifier que vous pouvez reproduire le problème. Si cela décrit mieux votre problème, faites une capture d'écran.


##### Mise à jour du serveur


Vérifiez votre version de BTCPay Server si elle est beaucoup plus ancienne que la [dernière version](https://github.com/btcpayserver/btcpayserver/releases) de BTCPay Server. La mise à jour de votre serveur peut résoudre le problème.


##### Redémarrage du serveur


Redémarrer votre serveur est un moyen facile de résoudre la plupart des problèmes les plus courants liés au serveur BTCPay. Il se peut que vous deviez vous connecter en SSH à votre serveur pour pouvoir le redémarrer.


##### Redémarrage d'un service


Il se peut que vous n'ayez besoin de redémarrer qu'un service particulier dans votre déploiement de BTCPay Server pour certains problèmes, comme le redémarrage du conteneur letsencrypt pour renouveler le certificat SSL.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Utilisez docker ps pour trouver le nom d'un autre service que vous souhaitez redémarrer.


#### Regarder dans les journaux de bord


Les journaux peuvent fournir des informations essentielles. Dans les paragraphes suivants, nous décrirons comment obtenir les informations du journal pour différentes parties de BTCPay.


##### Journaux de BTCPay


Depuis la version 1.0.3.8, vous pouvez facilement accéder aux journaux du serveur BTCPay depuis l'interface. Si vous êtes un administrateur de serveur, allez dans Paramètres du serveur > Journaux et ouvrez le fichier des journaux. Si vous ne savez pas ce que signifie une erreur particulière dans les journaux, mentionnez-la lors du dépannage.


Si vous souhaitez des journaux plus détaillés et que vous utilisez un déploiement Docker, vous pouvez consulter les journaux de conteneurs Docker spécifiques à l'aide de la ligne de commande. Voir ces [instructions pour ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) dans une instance de BTCPay fonctionnant sur un VPS.


Sur la page suivante, une liste générale des noms de conteneurs utilisés pour BTCPay Server.


Exécutez les commandes ci-dessous pour imprimer les journaux par nom de conteneur. Remplacez le nom du conteneur pour afficher les journaux d'autres conteneurs.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```


| Logs for     | Container Name                    |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker


Il y a plusieurs façons d'accéder à vos journaux LND lorsque vous utilisez Docker. Tout d'abord, connectez-vous en tant que root :


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Vous pouvez également imprimer rapidement les journaux en utilisant l'ID du conteneur (seuls les premiers caractères uniques de l'ID sont nécessaires, comme les deux caractères les plus à gauche) :


```bash
docker logs 'add your container ID'
```


Si, pour quelque raison que ce soit, vous avez besoin de plus de logs


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


Vous verrez quelque chose comme


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


Pour accéder aux logs non compressés de ces logs, faites `cat LND.log` ou si vous en voulez un autre, utilisez `cat LND.log.15`.


Pour accéder aux logs compressés en `.gzip`, utilisez `gzip -d LND.log.16.gz` (dans ce cas, nous accédons à `LND.log.16.gz`). Cela devrait vous donner un nouveau fichier, dans lequel vous pouvez faire `cat LND.log.16`. Au cas où ce qui précède ne fonctionnerait pas, vous pourriez avoir besoin d'installer gzip en premier avec `sudo apt-get install gzip`.


###### Lightning Network c-lightning - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


Vous pouvez également utiliser ceci :


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Vous pouvez également obtenir des informations sur les journaux avec la commande c-lightning CLI.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Journaux des nœuds Bitcoin


En plus de [consulter les journaux](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) de votre conteneur bitcoind, vous pouvez également utiliser n'importe laquelle des [commandes bitcoin-cli](https://developer.Bitcoin.org/reference/RPC/index.html)


[(ouvre une nouvelle fenêtre)](https://developer.Bitcoin.org/reference/RPC/index.html) pour obtenir des informations de votre nœud Bitcoin. BTCPay inclut un script qui vous permet de communiquer facilement avec votre nœud Bitcoin.


Dans le dossier btcpayserver-docker, récupérez les informations de Blockchain en utilisant votre node :


```bash
bitcoin-cli.sh getblockchaininfo
```


### Dossiers


Le serveur BTCPay dispose d'un système de fichiers local, ce qui lui permet de télécharger les actifs du magasin (produit), les logos et la marque directement sur le serveur. Le système de fichiers du serveur n'est accessible que par les administrateurs du serveur ; les propriétaires de magasins peuvent télécharger leurs logos ou leur marque au niveau du magasin.


Lorsque l'administrateur du serveur se trouve dans l'onglet Stockage de fichiers, il est possible de télécharger directement vers votre serveur ou de changer le fournisseur de stockage de fichiers pour un système de fichiers local ou Azure Blob Storage.


![image](assets/en/091.webp)


![image](assets/en/092.webp)


### Résumé des compétences


Dans cette section, vous avez appris ce qui suit :



- La différence entre les paramètres du magasin et ceux du serveur, en particulier en ce qui concerne les utilisateurs, les rôles et les courriers électroniques
- Définir des règles à l'échelle du serveur pour l'utilisation et la création de Lightning ou Bitcoin Hot Wallet, l'enregistrement de nouveaux utilisateurs et les notifications par courrier électronique.
- Comment ajouter des thèmes personnalisés (au lieu des simples options claires/foncées fournies) et créer des logos personnalisés ?
- Effectuer des tâches simples de maintenance du serveur via l'interface graphique fournie
- Résoudre les problèmes, y compris l'obtention de détails pour n'importe quel conteneur Docker ou votre nœud
- Gérer le stockage des fichiers


### Évaluation des connaissances


#### Examen conceptuel de l'AC


Quelle est la différence entre les rôles attribués par les paramètres du serveur et ceux attribués par les paramètres du magasin, et quelle est l'utilité potentielle de l'un par rapport à l'autre ?


#### KA Examen pratique


Décrire quelques cas d'utilisation possibles activés dans l'onglet Politiques.


#### KA Examen pratique


Décrivez quelques actions qu'un administrateur peut effectuer régulièrement dans l'onglet Maintenance.


## Serveur BTCPay - Paiements


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


La Invoice est un document que le vendeur remet à l'acheteur pour encaisser le paiement.


Dans le serveur BTCPay, une Invoice représente un document qui doit être payé dans un intervalle de temps défini à un taux Exchange fixe. Les factures ont des dates d'expiration parce qu'elles bloquent le taux Exchange dans un laps de temps spécifié, protégeant ainsi le destinataire des fluctuations de prix.


Le cœur de BTCPay Server est sa capacité à agir en tant que système de gestion Bitcoin Invoice. Un Invoice est un outil essentiel pour le suivi et la gestion des paiements reçus.


A moins que vous n'utilisiez un [Wallet](https://docs.btcpayserver.org/Wallet/) intégré pour recevoir les paiements manuellement, tous les paiements d'un magasin seront affichés sur la page Factures. Cette page trie les paiements par date et sert de ressource centrale pour la gestion et le dépannage des paiements.


![image](assets/en/093.webp)


### Général


#### Statuts Invoice


Le tableau ci-dessous énumère et décrit les statuts Invoice standard dans BTCPay, ainsi que les actions communes suggérées. Les actions ne sont que des recommandations. Il appartient aux utilisateurs de définir le meilleur plan d'action pour leur cas d'utilisation et leur entreprise.


| Invoice Status             | Description                                                                                                                             | Action                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New                        | Not paid, invoice timer still has not expired                                                                                           | None                                                                                                                        |
| New (paidPartial)          | Paid, not in full, invoice timer still has not expired                                                                                  | None                                                                                                                        |
| Expired                    | Not paid, invoice timer expired                                                                                                         | None                                                                                                                        |
| Expired (paidPartial) \*\* | Paid, not in full amount, and expired                                                                                                   | Contact buyer to arrange a refund or ask for them to pay their due. Optionally mark the invoice as settled or invalid           |
| Expired (paidLate)         | Paid, in full amount, after the invoice timer has expired                                                                               | Contact buyer to arrange a refund or process order if late confirmations are acceptable.                                    |
| Settled (paidOver)         | Paid more than the invoice amount, settled, received sufficient amount of confirmations                                                 | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing                 | Paid in full, but has not received sufficient amount of confirmations specified in the store settings                                   | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing (paidOver)      | Paid more than the invoice amount, not received sufficient amount of confirmations                                                      | Wait to be settled, then contact the  buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Settled                    | Paid, in full, received sufficient amount of confirmations in store                                                                     | Fulfil the order                                                                                                            |
| Settled (marked)           | Status was manually changed to settled from a processing or invalid status                                                             | Store admin has marked the payment as settled                                                                               |
| Invalid\*                  | Paid, but failed to receive sufficient amount of confirmations within the time specified in store settings                              | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |
| Invalid (marked)           | Status was manually changed to invalid from a settled or expired status                                                                 | Store admin has marked the payment as invalid                                                                               |
| Invalid (paidOver)         | Paid more than the invoice amount, but failed to receive sufficient amount of confirmations within the time specified in store settings | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |

#### Invoice détails


La page de détails Invoice contient toutes les informations relatives à une Invoice.


Les informations Invoice sont créées automatiquement en fonction du statut Invoice, du taux Exchange, etc. Les informations sur les produits sont créées automatiquement si la Invoice a été créée avec des informations sur les produits, par exemple dans l'application Point de vente.


#### Filtration Invoice


Les factures peuvent être filtrées à l'aide des filtres rapides situés à côté du bouton de recherche ou des filtres avancés, que l'on peut faire basculer en cliquant sur le lien (Aide) en haut de la page. Les utilisateurs peuvent filtrer les factures par magasin, numéro de commande, numéro d'article, statut ou date.


#### Invoice export


Les factures de BTCPay Server peuvent être exportées au format CSV ou JSON. Pour plus d'informations sur l'exportation et la comptabilité Invoice.


#### Remboursement d'une Invoice


Si, pour une raison quelconque, vous souhaitez effectuer un remboursement, vous pouvez facilement créer un remboursement à partir de la vue Invoice.


#### Archivage des factures


En raison de la fonction de non-réutilisation Address de BTCPay Server, il est courant de voir de nombreuses factures expirées sur la page Invoice de votre boutique. Pour les masquer, sélectionnez-les dans la liste et marquez-les comme archivées. Les factures marquées comme archivées ne sont pas supprimées. Le paiement d'une Invoice archivée sera toujours détecté par votre serveur BTCPay (statut paidLate). Vous pouvez consulter les factures archivées du magasin à tout moment en sélectionnant Factures archivées dans le menu déroulant du filtre de recherche.


#### Monnaie par défaut


Devise par défaut du magasin, définie lors de l'assistant de création du magasin.


#### Permettre à n'importe qui de créer une Invoice


Vous devez activer cette option si vous souhaitez permettre au monde extérieur de créer des factures dans votre boutique. Cette option n'est utile que si vous utilisez le bouton de paiement ou si vous émettez des factures via l'API ou un site web HTML tiers. L'application PoS est pré-autorisée et ne nécessite pas l'activation de ce paramètre pour qu'un visiteur aléatoire puisse ouvrir votre point de vente et créer une Invoice.


#### Ajouter une redevance supplémentaire (redevance de réseau) à la Invoice



- Uniquement si le client effectue plus d'un paiement pour la Invoice
- Sur chaque paiement
- Ne jamais ajouter de frais de réseau


#### La Invoice expire si le montant total n'a pas été payé après ... Procès-verbal.


La minuterie du Invoice est réglée par défaut sur 15 minutes. La minuterie sert de mécanisme de protection contre la volatilité, car elle bloque le montant en crypto-monnaie sur la base des taux crypto-fiat. Si le client ne paie pas la Invoice dans la période définie, la Invoice est considérée comme expirée. La Invoice est considérée comme "payée" dès que la transaction est visible sur la Blockchain (avec zéro confirmation), et est considérée comme "complète" lorsqu'elle atteint le nombre de confirmations défini par le commerçant (généralement de 1 à 6). La minuterie est personnalisable.


#### La Invoice est considérée comme payée même si le montant payé est inférieur de ...% au montant attendu.


Dans le cas où un client utilise une Exchange Wallet pour payer directement une Invoice, la Exchange prélève des frais minimes. Cela signifie que cette Invoice n'est pas considérée comme entièrement terminée. La Invoice est marquée comme "payée partiellement" Si un commerçant souhaite accepter des factures insuffisamment payées, vous pouvez définir le pourcentage ici


### Demandes


Les demandes de paiement sont une fonctionnalité qui permet aux propriétaires de boutiques BTCPay de créer des factures de longue durée. Les fonds sont versés conformément à la demande de paiement en utilisant le taux Exchange en vigueur au moment du paiement. Cela permet aux utilisateurs d'effectuer des paiements à leur convenance sans avoir à négocier ou à vérifier les taux Exchange avec le propriétaire du magasin au moment du paiement.


Les utilisateurs peuvent payer leurs demandes par paiements partiels. La demande de paiement reste valable jusqu'à ce qu'elle soit payée en totalité ou si le propriétaire du magasin exige un délai d'expiration. Les adresses ne sont jamais réutilisées. Une nouvelle Address est générée chaque fois que l'utilisateur clique sur "payer" pour créer une Invoice pour la demande de paiement.


Les propriétaires de boutiques peuvent imprimer les demandes de paiement (ou exporter les données Invoice) à des fins d'archivage et de comptabilité. BTCPay étiquette automatiquement les factures en tant que demandes de paiement dans la liste Invoice de votre boutique.


#### Personnalisez vos demandes de paiement



- Invoice Montant - Définir le montant du paiement demandé
- Dénomination - Afficher le montant demandé en monnaie fiduciaire ou en crypto-monnaie
- Quantité de paiements - Autoriser uniquement les paiements uniques ou partiels
- Délai d'expiration - Autoriser les paiements jusqu'à une date donnée ou sans délai d'expiration
- Description - Éditeur de texte, tableaux de données, intégration de photos et de vidéos
- Apparence - Couleur et style avec les thèmes CSS


![image](assets/en/094.webp)


#### Créer une demande de paiement


Dans le menu de gauche, allez à Demande de paiement et cliquez sur "Créer une demande de paiement".


![image](assets/en/095.webp)


Indiquez le nom de la demande, le montant, la dénomination affichée, le magasin associé, l'heure d'expiration et la description (facultatif)


Sélectionnez l'option Autoriser le bénéficiaire à créer des factures dans sa dénomination si vous souhaitez autoriser les paiements partiels.


Cliquez sur Enregistrer et consulter pour revoir votre demande de paiement.


BTCPay crée une URL pour la demande de paiement. Partagez cette URL pour voir votre demande de paiement. Vous avez besoin de plusieurs demandes identiques ? Vous pouvez dupliquer les demandes de paiement en utilisant l'option Cloner dans le menu principal.


![image](assets/en/096.webp)


**ATTENTION**


Les demandes de paiement dépendent du magasin, ce qui signifie que chaque demande de paiement est associée à un magasin lors de sa création. Veillez à ce qu'une Wallet soit connectée au magasin auquel appartient la demande de paiement.


#### Demande payée


Le bénéficiaire et le demandeur peuvent consulter le statut de la demande de paiement après l'envoi du paiement. Si le paiement a été reçu dans son intégralité, le statut est réglé. Si seuls des paiements partiels ont été effectués, le montant dû affichera le solde restant.


![image](assets/en/097.webp)


#### Personnaliser les demandes de paiement


Le contenu de la description peut être modifié à l'aide de l'éditeur de texte de la demande de paiement. Les deux options sont disponibles si vous souhaitez utiliser des thèmes de couleurs supplémentaires ou un style CSS personnalisé.


Les utilisateurs non techniques peuvent utiliser un [thème bootstrap](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Une personnalisation plus poussée peut être effectuée en fournissant du code CSS supplémentaire, comme indiqué ci-dessous.


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### Tirer les paiements


Traditionnellement, un destinataire partage son Bitcoin Address pour effectuer un paiement Bitcoin, et l'expéditeur envoie ensuite de l'argent à ce Address. Ce système est appelé "paiement poussé", car l'expéditeur initie le paiement alors que le destinataire n'est peut-être pas disponible, poussant ainsi le paiement vers le destinataire.


Mais qu'en est-il de l'inversion des rôles ?


Et si, au lieu de pousser le paiement, l'expéditeur permettait au destinataire de retirer le paiement au moment qu'il juge opportun ? C'est le concept du paiement tiré. Cela permet plusieurs nouvelles applications, telles que



- Un service d'abonnement (où l'abonné permet au service de retirer de l'argent tous les x temps)
- Remboursements (lorsque le commerçant permet au client de retirer l'argent du remboursement sur sa Wallet quand il le souhaite)
- Facturation au temps passé pour les freelances (lorsque la personne qui embauche autorise le freelance à verser de l'argent dans son Wallet au fur et à mesure que le temps passé est comptabilisé)
- Mécénat (lorsque le mécène permet au bénéficiaire de retirer de l'argent chaque mois pour continuer à soutenir son travail)
- Vente automatique (le client d'un Exchange peut autoriser un Exchange à prélever de l'argent sur son Wallet pour le vendre automatiquement chaque mois)
- Système de retrait du solde (lorsqu'un service à fort volume permet aux utilisateurs de demander des retraits de leur solde, le service peut alors facilement regrouper tous les paiements à de nombreux utilisateurs à des intervalles fixes)


### Paiements


La fonctionnalité de paiement est liée à la fonction [Pull Payments](https://docs.btcpayserver.org/PullPayments/). Cette fonctionnalité vous permet de créer des paiements dans votre BTCPay. Cette fonctionnalité vous permet de traiter les paiements pull (remboursements, paiements de salaires, ou retraits).


#### Exemple 1 : Remboursement


Commençons par l'exemple du remboursement. Le client a acheté un article dans votre magasin, mais il doit malheureusement le retourner. Il souhaite être remboursé. Dans BTCPay, vous pouvez créer un [Refund](https://docs.btcpayserver.org/Refund/) et fournir au client le lien pour réclamer ses fonds. Une fois que le client a fourni son Address et réclamé les fonds, ceux-ci seront affichés dans la section Paiements.


Le premier statut est "En attente d'approbation". Les employés du magasin peuvent vérifier si plusieurs demandes sont en attente, et après avoir fait la sélection, vous utilisez le bouton Actions.


Options du bouton d'action



- Approuver les paiements sélectionnés
- Approuver et envoyer les paiements sélectionnés
- Annuler les paiements sélectionnés


L'étape suivante consiste à approuver et à envoyer les paiements sélectionnés, car nous voulons rembourser le client. Vérifiez la Address du client, qui indique le montant et si nous souhaitons que les frais soient soustraits du remboursement ou non. Une fois les vérifications effectuées, il ne reste plus qu'à signer la transaction.


Le client est maintenant mis à jour sur la page de réclamation. Il peut suivre la transaction car il dispose d'un lien vers une Block explorer et sa transaction. Une fois la transaction confirmée, son statut passe à "Terminé".


#### Exemple 2 : Salaire


Passons maintenant au paiement des salaires, puisqu'il est piloté depuis le magasin et non en fonction de la demande du client. Le concept sous-jacent est le même ; il utilise les paiements tirés. Mais au lieu de créer un remboursement, nous allons effectuer un [Pull Payment](https://docs.btcpayserver.org/PullPayments/).


Allez dans l'onglet Paiements tirés de votre serveur BTCPay. En haut à droite, cliquez sur le bouton Créer un paiement tiré.


Nous en sommes maintenant à la création du paiement. Donnez-lui un nom et indiquez le montant souhaité dans la devise choisie. Remplissez la description, afin que l'employé sache de quoi il s'agit. La partie suivante est similaire aux remboursements. L'employé remplit le formulaire Address de destination et le montant qu'il souhaite réclamer pour ce paiement. Il peut décider de faire deux demandes distinctes, à des adresses différentes, ou même de faire une demande partielle sur l'éclairage.


Si plusieurs paiements sont en attente, vous pouvez les grouper pour les signer et les envoyer. Une fois signés, les paiements sont déplacés vers l'onglet En cours et affichent la transaction. Une fois accepté par le réseau, le paiement passe dans l'onglet Terminé. L'onglet Terminé a une fonction purement historique. Il contient les paiements traités et les transactions qui s'y rapportent


### Tirer les paiements


#### Concept


Lorsqu'un expéditeur configure un paiement Pull, il peut configurer un certain nombre de propriétés :



- Demande d'extraction Nom
- Un montant limite
- Une unité (telle que BTC, SAT, USD)
- Modes de paiement
  - BTC On-Chain
  - BTC off-chain
- Description
- CSS personnalisé
- Date de fin (facultatif pour Lightning Network BOLT11)


Ensuite, l'expéditeur peut partager le paiement à l'aide d'un lien avec le destinataire, ce qui permet à ce dernier de créer un paiement. Le destinataire choisira son paiement :



- Quel mode de paiement utiliser ?
- Où envoyer l'argent


Une fois qu'un paiement est créé, il est pris en compte dans la limite du paiement tiré pour la période en cours. L'expéditeur approuve alors le paiement en définissant le taux auquel le paiement sera envoyé et procède au paiement.


Pour l'expéditeur, nous fournissons une méthode facile à utiliser pour regrouper plusieurs paiements à partir du [BTCPay Internal Wallet](https://docs.btcpayserver.org/Wallet/).


#### Greenfield API


BTCPay Server fournit une API complète à l'expéditeur et au destinataire qui est documentée dans la page `/docs` de votre instance. (ou sur le site web de documentation https://docs.btcpayserver.org)


Étant donné que notre API expose l'ensemble des capacités des paiements tirés, un expéditeur peut automatiser les paiements en fonction de ses propres besoins.


### Résumé des compétences


Dans cette section, vous avez appris ce qui suit :



- Compréhension approfondie des statuts Invoice du serveur BTCPay, ainsi que des actions qui peuvent être effectuées sur ces statuts
- Personnaliser et gérer les mécanismes Invoice à durée de vie étendue, connus sous le nom de requêtes.
- Les possibilités de paiement flexibles supplémentaires offertes par la fonction unique de paiement par tirage de BTCPay Server, en particulier pour le traitement des remboursements et des paiements de salaires.


### Évaluation des connaissances


#### Examen conceptuel de l'AC


Quelles sont les différences entre les factures et les demandes de paiement, et quelles sont les bonnes raisons d'utiliser ces dernières ?


#### Examen conceptuel de l'AC


En quoi les paiements à flux tirés vont-ils au-delà de ce qui peut être fait en général en On-Chain ? Décrivez quelques cas d'utilisation qu'ils permettent.


## Plugins par défaut du serveur BTCPay


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Plugins et applications par défaut


Le serveur BTCPay est livré avec un ensemble standard de plugins (applications) qui peuvent transformer le serveur BTCPay en une passerelle de paiement pour le commerce électronique. Avec l'ajout d'un point de vente, d'une plateforme de crowdfunding et d'un bouton de paiement facile, BTCPay Server devient une solution facile à déployer.


### Point de vente


L'un des plugins standard de BTCPay Server est le point de vente (PoS). Avec le plugin PoS, le propriétaire d'un magasin peut créer une boutique en ligne directement à partir de BTCPay Server ; il n'a pas besoin de solutions de commerce électronique tierces pour gérer une boutique en ligne. L'application PoS basée sur le web permet aux utilisateurs de magasins de briques et de mortier d'accepter facilement des Bitcoin, sans frais ni tiers, directement dans leur Wallet. Le PoS peut être facilement affiché sur des tablettes ou d'autres appareils qui prennent en charge la navigation sur le web. Les utilisateurs peuvent facilement créer un raccourci sur l'écran d'accueil pour accéder rapidement à l'application web.


#### Comment créer un nouveau point de vente


BTCPay Server permet aux propriétaires de magasins de créer rapidement un point de vente dans plusieurs configurations. BTCPay Server reconnaît que tous les magasins ne sont pas des commerces électroniques, et que tous les magasins ne sont pas des bars ou des restaurants, et il est livré avec plusieurs configurations standard pour votre point de vente.


Lorsque le propriétaire de la boutique clique sur "Point de vente" dans la barre de menu de gauche, BTCPay Server demande un nom ; ce nom sera visible dans la barre de menu de gauche. Cliquez sur Créer pour créer le PoS.


![image](assets/en/098.webp)


#### Mettre à jour le point de vente nouvellement créé


Après avoir créé un nouveau point de vente, l'écran suivant vous permettra de mettre à jour votre point de vente et d'ajouter des articles à votre magasin.


##### Nom de l'application


Le nom donné ici à votre point de vente sera visible dans le menu principal du serveur BTCPay.


##### Titre d'affichage


Le public verra le titre ou le nom de votre boutique lorsqu'il la visitera. Par défaut, le serveur BTCPay nomme votre boutique "Tea shop" Remplacez ce nom par le nom de votre boutique.


![image](assets/en/099.webp)


#### Choisir le style du point de vente


Le serveur BTCPay est capable d'afficher son point de vente de plusieurs façons.



- Liste des produits
  - Vue d'un magasin où les clients ne peuvent acheter qu'un seul produit à la fois.
- Liste de produits avec panier.
  - Une vue de la boutique où les clients peuvent acheter plusieurs articles à la fois et obtenir une vue d'ensemble du panier à droite de leur écran.
- Clavier uniquement
  - Pas de liste de produits, juste un clavier pour la facturation directe.
- Affichage de l'impression (liste de produits imprimable avec QR)
  - Si vous ne pouvez pas toujours afficher votre liste de produits numériquement, vous avez besoin d'une solution "hors ligne" pour les produits ; BTCPay Server dispose d'un écran d'impression pour fonctionner comme un magasin hors ligne.


![image](assets/en/100.webp)


#### Point Of Sale Style - Liste des produits


![image](assets/en/101.webp)


#### Style Point de Vente - Liste des produits + Panier


![image](assets/en/102.webp)


#### Style point de vente - Clavier uniquement


![image](assets/en/103.webp)


#### Style du point de vente - Présentoir d'impression


![image](assets/en/104.webp)


#### Monnaie


Le propriétaire du magasin peut définir une devise différente de la devise par défaut pour son point de vente. La devise par défaut du magasin remplit automatiquement ce champ.


#### Description


Parlez au monde entier de votre boutique ; que vendez-vous et à quel prix ? Tout ce qui explique votre boutique se trouve ici.


![image](assets/en/105.webp)


#### Produits


Lorsqu'un point de vente est créé, un serveur BTCPay standard ajoute quelques éléments à la boutique pour référence. Cliquez sur le bouton Modifier sur n'importe quel élément standard pour mieux comprendre chaque option possible pour un élément.


La création d'un nouveau produit dans votre magasin se compose des champs suivants ;



- Titre
- Prix (fixe, minimum ou personnalisé)
- URL de l'image
- Description
- Inventaire
- ID
- Acheter le texte du bouton.
- Activer/Désactiver


Une fois que le propriétaire du magasin a rempli tous les champs relatifs aux nouveaux produits, cliquez sur "Enregistrer" et vous remarquerez que la section "Produits" du point de vente est maintenant remplie. Sauvegardez toujours dans le coin supérieur droit de votre écran afin d'éviter que les propriétaires de magasins ne perdent leur progression lors de l'ajout de produits.


Les propriétaires de magasins peuvent également utiliser l'"éditeur brut" pour configurer leurs produits. L'éditeur brut nécessite une compréhension de base des structures JSON.


![image](assets/en/106.webp)


#### Sortie de caisse


BTCPay Server permet une petite personnalisation de la caisse spécifique au PoS. Le propriétaire de la boutique peut définir le texte "Acheter pour x" ou demander des données client spécifiques en les ajoutant aux formulaires.


#### Conseils


Seules certaines boutiques ont besoin de l'option Conseils sur leurs ventes. Les propriétaires de magasins peuvent activer ou désactiver cette option comme ils le souhaitent pour leur magasin. Si la boutique utilise les pourboires activés, le propriétaire de la boutique peut définir le texte dans le champ pour les pourboires qu'il souhaite. Les pourboires du serveur BTCPay sont basés sur un pourcentage. Les propriétaires de boutique peuvent ajouter plusieurs pourcentages, séparés par des virgules.


#### Réductions


En tant que propriétaire d'un magasin, vous pouvez souhaiter offrir au client une remise personnalisée au moment du paiement ; la case à cocher des remises devient disponible à la caisse de votre magasin. Toutefois, il est fortement déconseillé d'utiliser des systèmes de caisse automatique.


#### Paiements personnalisés


Lorsque l'option Paiements personnalisés est activée, le client peut saisir un prix fixe égal ou supérieur au prix original Invoice généré par le magasin.


#### Options supplémentaires


Après avoir tout configuré pour votre point de vente, il reste quelques options supplémentaires. Les propriétaires de magasins peuvent facilement intégrer leur PdV dans une Iframe ou intégrer un bouton de paiement lié à un article spécifique du magasin. Pour styliser la boutique PoS qui vient d'être créée, les propriétaires peuvent ajouter des feuilles de style CSS personnalisées au bas des options supplémentaires.


#### Supprimer cette application


Si le propriétaire du magasin souhaite supprimer entièrement le point de vente de son serveur BTCPay, il peut cliquer sur le bouton Supprimer cette application au bas de la mise à jour du point de vente pour détruire entièrement son application de point de vente. En cliquant sur "Delete this app", BTCPay Server demandera une confirmation en tapant `DELETE` et en confirmant en cliquant sur le bouton Delete. Après la suppression, le propriétaire du magasin retourne au tableau de bord de BTCPay Server.


### Serveur BTCPay - Crowdfund


En plus du plugin de point de vente, BTCPay Server offre la possibilité de créer un crowdfunding. Comme pour toute autre plateforme de crowdfunding, les propriétaires de magasins peuvent fixer un objectif, créer des avantages pour les contributions et personnaliser le crowdfunding selon leurs besoins.


#### Comment mettre en place un nouveau crowdfunding


Cliquez sur le plugin Crowdfund dans le menu principal à gauche de votre serveur BTCPay, sous la section Plugin. BTCPay Server demandera alors un nom pour le Crowdfund ; ce nom sera également affiché dans la barre de menu de gauche.


![image](assets/en/107.webp)


#### Mettre à jour le point de vente nouvellement créé


Une fois que l'application a reçu un nom, l'écran suivant consistera à mettre à jour l'application pour qu'elle ait un contexte.


#### Nom de l'application


Le nom donné à votre Crowdfund sera visible dans le menu principal de BTCPay Server.


#### Titre d'affichage


Le titre est donné au Crowdfund pour le public.


#### Titre d'appel


Donnez au crowdfunding une phrase pour expliquer l'objet de la collecte de fonds.


![image](assets/en/108.webp)


#### URL de l'image vedette


Chaque crowdfund a son image principale, la bannière que vous reconnaissez directement. Cette image peut être stockée sur votre serveur si vous avez des droits d'administration. Les administrateurs peuvent télécharger sous les paramètres du serveur BTCPay - Fichiers. Si vous êtes propriétaire d'une boutique, l'image doit être téléchargée sur le web par l'intermédiaire d'un hébergeur tiers (par exemple, Imgur).


#### Rendre le crowdfunding public


Cette option rend votre Crowdfund public et donc visible au monde extérieur. A des fins de test ou pour voir si votre thème est appliqué correctement, laissez cette option sur OFF pendant la période de construction du crowdfund.


#### Description


Parlez au monde entier de votre crowdfunding. Pourquoi collectez-vous des fonds ? Tout ce qui explique votre crowdfunding se trouve ici.


![image](assets/en/109.webp)


#### Objectif du crowdfunding


Fixez un objectif pour ce que la collecte de fonds doit rapporter au projet et dans quelle devise l'objectif doit être libellé. Si vos objectifs sont fixés à des dates différentes, veillez à inclure ces dates d'objectif et de fin sous Objectifs dans le crowdfunding.


![image](assets/en/110.webp)


#### Avantages


Les avantages peuvent considérablement améliorer vos efforts de crowdfunding. En effet, les avantages donnent aux gens un moyen de participer à votre campagne. Ils exploitent à la fois les motivations égoïstes et bienveillantes. Et ils vous permettent d'accéder aux dépenses de vos supporters, et pas seulement à leur bourse philanthropique - vous pouvez deviner ce qui est le plus important.


La création d'un nouvel avantage consiste à remplir les champs suivants.



- Titre
- Prix (fixe, minimum ou personnalisé)
- URL de l'image
- Description
- Inventaire
- ID
- Acheter le texte du bouton.
- Activer/Désactiver


Une fois que le propriétaire du magasin a rempli tous les champs du nouvel avantage, cliquez sur Enregistrer, et vous remarquerez que la section Avantages dans Crowdfunds est maintenant remplie.


![image](assets/en/111.webp)


### Serveur BTCPay - Point de vente


#### Contributions


Les propriétaires de magasins peuvent choisir comment afficher les avantages, comment ils sont classés, ou même les classer par rapport à d'autres avantages. Cependant, une fois que les objectifs du Crowdfunds sont atteints, le propriétaire de la boutique peut vouloir arrêter les dons pour cette collecte de fonds. Il peut donc activer l'option "Ne pas autoriser de contributions supplémentaires après avoir atteint l'objectif". Cela empêchera le Crowdfund d'accepter des dons.


##### Le comportement du crowdfunding


Le standard de Crowdfund ne compte que les factures créées avec Crowdfund pour l'objectif. Cependant, dans certains cas, le propriétaire du magasin souhaite que toutes les factures créées dans ce magasin soient prises en compte pour le crowdfunding.


#### Options supplémentaires pour la personnalisation


BTCpay Server offre quelques personnalisations supplémentaires. Ajoutez des sons, des animations ou même des fils de discussion au Crowdfund. Les propriétaires de boutiques peuvent également modifier l'aspect et la convivialité du Crowdfund en entrant leur propre CSS personnalisé.


#### Supprimer cette application


Si le propriétaire de la boutique souhaite supprimer complètement le Crowdfund de son serveur BTCPay, en bas de la mise à jour du Crowdfund, il peut cliquer sur le bouton "Delete this app" (Supprimer cette application) pour supprimer complètement son application Crowdfund. En cliquant sur "Supprimer cette application", le serveur BTCPay demandera une confirmation en tapant `DELETE` et en confirmant en cliquant sur le bouton Supprimer. Après la suppression, le propriétaire de la boutique retourne au tableau de bord de BTCPay Server.


### Serveur BTCPay - Bouton de paiement


Des boutons de paiement HTML facilement intégrables et hautement personnalisables permettent aux propriétaires de magasins de recevoir des pourboires et des dons. Dans la barre de menu gauche de BTCPay Server, sous la section Plugins, les propriétaires de boutiques peuvent cliquer sur "Bouton de paiement" et cliquer sur Activer pour créer un bouton de paiement.


#### Paramètres généraux


Dans les paramètres généraux du bouton de paiement, les propriétaires de magasins peuvent définir les éléments suivants



- Prix standard
- Monnaie par défaut
- Mode de paiement par défaut
  - Utiliser la valeur par défaut du magasin
  - BTC On-Chain
  - BTC off-chain (éclair)
  - BTC off-chain (LNURL-pay)
- Description de la caisse
- Numéro d'ordre


#### Options d'affichage


Le bouton de paiement de BTCPay Server peut être configuré pour s'adapter à différents styles. Les boutons peuvent avoir un montant fixe ou personnalisé, qui est affiché avec un curseur ou des boutons à bascule plus et moins.


#### Utiliser le modal


Lors de la création du bouton de paiement, les propriétaires de magasins peuvent choisir son comportement lorsqu'un client clique dessus et l'afficher dans une fenêtre modale ou dans une nouvelle page.


**!Note!**


Avertissement : Le bouton Paiement ne doit être utilisé que pour les pourboires et les dons


Il n'est pas recommandé d'utiliser le bouton de paiement pour les intégrations de commerce électronique, car l'utilisateur peut modifier les informations relatives à la commande. Pour le commerce électronique, vous devez utiliser notre API Greenfield. Si ce magasin traite des transactions commerciales, nous vous recommandons de créer un magasin séparé avant d'utiliser le bouton de paiement.


#### Personnaliser le texte du bouton de paiement


Par défaut, le bouton de paiement de BTCPay Server indique "Payez avec BTCPay". Les propriétaires de boutiques peuvent définir ce texte à leur guise et changer le logo de BTCPay Server pour le leur. Définissez le texte en utilisant le "Texte du bouton de paiement" et collez l'URL de l'image sous l'"URL de l'image du bouton de paiement".


##### Taille de l'image


La taille de l'image dans le bouton ne peut être réglée que sur trois valeurs par défaut.



- 146x40px
- 168x46px
- 209x57px


#### Type de bouton


Le serveur de BTCPay connaît trois états pour le bouton de paiement.



- Montant fixe
  - Le prix fixé précédemment se trouve dans les paramètres généraux du bouton.
- Montant personnalisé
  - Le bouton Payer du serveur BTCPay est doté de boutons + et - permettant de définir un prix personnalisé.
  - Lors de l'utilisation du montant personnalisé, le serveur de BTCPay demandera un Min, un Max, et la façon dont il doit augmenter progressivement.
  - Les boutons peuvent être réglés sur "Utiliser le style d'entrée simple", ce qui supprime les bascules +/-.
  - Ajuster le bouton en ligne où le bouton et les bascules apparaissent en ligne.
- Curseur
  - Semblable au montant personnalisé, il est toutefois différent sur le plan visuel car il comporte un curseur au lieu des boutons +/-.
  - Lors de l'utilisation du curseur, le serveur de BTCPay demandera un Min, un Max, et la façon dont il doit augmenter progressivement.


**!Note!**


Le bouton Paiement peut être supprimé en haut de la description de l'avertissement.


#### Notifications de paiement


Le serveur IPN (Instant Payment Notification) est conçu pour les webhooks et peut être configuré avec une URL pour les données post-achat.


#### Notifications par courrier électronique


Lorsqu'un paiement a été effectué, le serveur de BTCPay peut en informer le propriétaire de la boutique.


#### Redirection du navigateur


Lorsque le client termine son achat, il est redirigé vers ce lien si celui-ci a été défini par le propriétaire du magasin.


#### Options avancées du bouton de paiement


Spécifiez des paramètres de chaîne de requête supplémentaires qui doivent être ajoutés à la page de paiement une fois que la Invoice est créée. Par exemple, `lang=da-DK` chargera la page de paiement en danois par défaut.


#### Utiliser l'application comme point final


Vous pouvez relier directement le bouton de paiement à un élément dans l'une des applications PoS ou Crowdfund que vous avez déjà utilisées.


Les propriétaires de magasins peuvent cliquer sur le menu déroulant et sélectionner l'application de leur choix ; une fois l'application sélectionnée, le propriétaire du magasin peut ajouter l'article à lier.


#### Code généré


Comme le bouton de paiement de BTCPay Server est un HTML facilement intégrable, BTCPay Server affiche le code généré à copier dans un site Web en bas de page après avoir configuré le bouton de paiement.


Les propriétaires de boutiques peuvent copier le code généré sur leur site web, et le bouton de paiement du serveur BTCPay est directement actif sur leur site web.


#### Notifications de paiement


Le serveur IPN (Instant Payment Notification) est conçu pour les webhooks et peut être configuré avec une URL pour afficher les données d'achat.


#### Notifications par courrier électronique


Lorsqu'un paiement est effectué, le serveur de BTCPay peut en informer le propriétaire du magasin.


#### Redirection du navigateur


Lorsque le client termine son achat, il est redirigé vers ce lien si celui-ci a été défini par le propriétaire du magasin.


#### Options avancées du bouton de paiement


Spécifiez des paramètres de chaîne de requête supplémentaires qui doivent être ajoutés à la page de paiement une fois que la Invoice est créée. Par exemple, `lang=da-DK` chargera la page de paiement en danois par défaut.


#### Utiliser l'application comme point final


Vous pouvez directement lier le bouton de paiement à un article dans l'une des applications PoS ou Crowdfund que vous avez déjà utilisées. Les propriétaires de magasins peuvent cliquer sur le menu déroulant et sélectionner l'application de leur choix. Une fois l'application sélectionnée, le propriétaire du magasin peut ajouter l'article à lier.


#### Code généré


Comme le bouton de paiement de BTCPay Server est un HTML facilement intégrable, BTCPay Server affiche le code généré à copier sur un site Web en bas de page après avoir configuré le bouton de paiement. Les propriétaires de boutiques peuvent copier le code généré sur leur site Web, et le bouton de paiement de BTCPay Server est directement actif sur leur site Web.


### Résumé des compétences


Dans cette section, vous avez appris



- Comment utiliser le plugin PoS intégré de BTCPay Server pour créer facilement une boutique personnalisée ?
- Comment utiliser le plugin Crowdfund intégré à BTCPay Server pour créer facilement une application de crowdfunding personnalisée ?
- Générer le code d'un bouton de paiement personnalisé à l'aide du plugin Pay Button


### Évaluation des connaissances


#### Revue KA


Quels sont les trois plugins intégrés qui sont livrés en standard avec BTCPay Server ? En quelques mots, décrivez comment chacun d'entre eux peut être utilisé.


# Configuration du serveur BTCPay


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## Compréhension de base de l'installation du serveur BTCPay sur un environnement LunaNode


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### Installation du serveur BTCPay sur un environnement hébergé (LunaNode)


Ces étapes fourniront toutes les informations nécessaires pour commencer à utiliser BTCPay Server sur LunaNode. Il existe de nombreuses options pour déployer le logiciel.

Vous pouvez trouver tous les détails du serveur BTCPay sur https://docs.btcpayserver.org.


#### Par où commencer ?


Dans cette partie, vous vous familiariserez avec LunaNode en tant que fournisseur d'hébergement, vous apprendrez les premières étapes de l'utilisation de votre serveur BTCPay et vous apprendrez à utiliser Lightning Network. Après avoir parcouru toutes les étapes, vous pourrez gérer une boutique en ligne ou une plateforme de crowdfunding acceptant Bitcoin !


C'est l'une des nombreuses façons de déployer BTCPay Server. Lisez notre documentation pour plus de détails.


https://docs.btcpayserver.org.


### Serveur BTCPay - Déploiement de LunaNode


#### Déploiement de LunaNode


Tout d'abord, rendez-vous sur le site web de LunaNode.com, où nous créerons un nouveau compte. Cliquez sur Sign Up en haut à droite ou utilisez l'assistant Get Started sur leur page d'accueil.


![image](assets/en/112.webp)


Après avoir créé votre nouveau compte, LunaNode vous envoie un e-mail de vérification. Une fois que vous avez vérifié le compte, par rapport à Voltage, vous avez immédiatement la possibilité d'augmenter le solde de votre compte. Ce solde est nécessaire pour couvrir les frais d'espace serveur et d'hébergement.


![image](assets/en/113.webp)


#### Ajouter du crédit à votre compte LunaNode


Une fois que vous avez cliqué sur "Déposer un crédit", vous pouvez définir le montant que vous souhaitez verser sur votre compte et la manière dont vous souhaitez le payer. LunaNode et BTCPay Server coûtent entre 10 et 20 $ par mois.

Par rapport à Voltage.cloud, vous obtenez un accès complet à votre Serveur Privé Virtuel (SPV), ce qui vous permet d'avoir plus de contrôle sur votre serveur. Après avoir créé votre nouveau compte, LunaNode vous envoie un e-mail de vérification.

Une fois que vous avez vérifié le compte, par rapport à Voltage, vous avez immédiatement la possibilité d'augmenter le solde de votre compte. Ce solde est nécessaire pour couvrir l'espace serveur et les coûts d'hébergement.


#### Comment déployer un nouveau serveur ?


Dans ce guide, nous vous guiderons à travers le processus d'installation en créant un ensemble de clés API et en utilisant le lanceur de serveur BTCPay développé par LunaNode.


Dans votre tableau de bord LunaNode, cliquez sur API en haut à droite. Une nouvelle page s'ouvre. Nous n'avons qu'à définir un Nom pour la clé API. Le reste sera pris en charge par LunaNode et ne sera pas abordé dans ce guide. Cliquez sur le bouton Create API Credential (Créer une clé API).

Après avoir créé les informations d'identification de l'API, vous obtenez une longue chaîne de lettres et de caractères. Il s'agit de votre clé API.


![image](assets/en/114.webp)


#### Comment déployer un nouveau serveur ?


Ces informations d'identification sont composées de deux parties, la clé et l'identifiant de l'API ; nous aurons besoin des deux. Avant de passer à l'étape suivante, ouvrons un deuxième onglet dans le navigateur et allons à https://launchbtcpay.lunanode.com/


Ici, il vous sera demandé de fournir votre clé API et votre ID API. Cela vous permet de savoir que c'est vous qui avez fourni ce nouveau serveur. La clé API devrait toujours être ouverte dans l'onglet précédent ; si vous faites défiler le tableau ci-dessous, vous trouverez l'ID API.


Vous pouvez retourner à la page avec le Launcher, remplir les champs avec votre clé API et votre ID, et cliquer sur continuer.


![image](assets/en/115.webp)


Dans l'étape suivante, vous pouvez fournir un nom de domaine. Si vous possédez déjà un domaine et que vous souhaitez l'utiliser pour le serveur BTCPay, assurez-vous d'ajouter également l'enregistrement DNS (appelé enregistrement A) sur votre domaine. Si vous ne possédez pas de domaine, utilisez le domaine fourni par LunaNode à la place (vous pouvez le modifier plus tard dans les paramètres du serveur BTCPay) et cliquez sur Continuer.


En savoir plus sur l'établissement ou la modification d'un enregistrement DNS pour le serveur BTCPay ; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### Lancer le serveur BTCPay sur LunaNode


Après avoir suivi les étapes précédentes, nous pouvons définir toutes les options pour notre nouveau serveur. Ici, nous allons sélectionner Bitcoin (BTC) comme monnaie supportée. Nous pouvons également définir un email pour recevoir des notifications sur les certificats d'encryptage à des fins de renouvellement, ce qui est facultatif.


Ce guide vise à mettre en place un environnement Mainnet (Bitcoin dans le monde réel) ; cependant, LunaNode vous permet également de le configurer en Testnet ou Regtest à des fins de développement. Pour ce guide, nous nous en tiendrons à l'option Mainnet.


Vous pouvez choisir votre implémentation de Lightning. LunaNode propose deux implémentations différentes, LND et Core Lightning. Pour ce guide, nous prendrons LND. Les différences entre les deux implémentations sont peu nombreuses mais réelles ; pour en savoir plus, nous vous recommandons de lire la documentation complète : https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/116.webp)


LunaNode propose plusieurs plans de machines virtuelles (VM). Ceux-ci diffèrent en termes de gamme de prix et de spécifications de serveur. Pour ce guide, un plan m2 suffira ; cependant, si vous avez choisi plus que le Bitcoin comme monnaie, envisagez d'utiliser au moins un plan m4.


Accélérer la synchronisation initiale Blockchain ; ceci est optionnel et dépend de vos besoins. Il existe des options avancées, telles que la définition d'un Alias Lightning, le pointage vers une version spécifique de GitHub, ou la définition de clés SSH ; aucune de ces options ne sera abordée dans ce guide.


Après avoir rempli le formulaire, vous devez cliquer sur Launch VM, et Lunanode commencera à créer votre nouvelle VM, avec BTCPay Server installé dessus. Ce processus prend quelques minutes ; une fois que votre serveur est prêt, LunaNode vous donne le lien vers votre nouveau serveur BTCPay.


Après le processus de création, cliquez sur le lien vers votre serveur BTCPay ; ici, il vous sera demandé de créer un compte administrateur.


![image](assets/en/117.webp)


### Résumé des compétences


Dans cette section, vous avez appris



- Créer et alimenter un compte sur LunaNode
- Utiliser le lanceur de serveur de BTCPay pour créer votre propre serveur


### Évaluation des connaissances


#### Examen conceptuel de l'AC


Décrivez quelques-unes des différences entre l'exécution d'une instance de BTCPay Server sur un VPS et la création d'un compte sur une instance hébergée.


## Installation de BTCPay Server dans un environnement Voltage


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


Vous vous familiariserez avec Voltage.cloud en tant que fournisseur d'hébergement, vous apprendrez les premières étapes de l'utilisation de votre serveur BTCPay et vous apprendrez à utiliser le Lightning Network. Après avoir parcouru toutes les étapes, vous pourrez gérer une boutique en ligne ou une plateforme de crowdfunding acceptant le Bitcoin !


C'est l'une des nombreuses façons de déployer BTCPay Server. Lisez notre documentation pour plus de détails.

https://docs.btcpayserver.org.


### Serveur BTCPay - Déploiement de Voltage.cloud


Tout d'abord, rendez-vous sur le site Web Voltage.cloud et créez un nouveau compte. Lors de la création du compte, vous pouvez vous inscrire pour un essai gratuit de 7 jours. Cliquez sur Sign Up en haut à droite ou utilisez la fonction "Try a free 7-day trial" sur la page d'accueil.


![image](assets/en/118.webp)


Après avoir créé un compte, cliquez sur le bouton "NODES" sur votre tableau de bord. Une fois que nous avons sélectionné Nodes et créé un nouveau nœud, les offres possibles de Voltage nous sont présentées. Comme ce guide couvrira également le Lightning Network, chez Voltage, nous devons d'abord choisir notre implémentation Lightning avant de créer un serveur BTCPay. Cliquez sur LightningNode.


![image](assets/en/119.webp)


Ici, vous devrez sélectionner le type de nœud d'éclairage que vous souhaitez. Voltage dispose d'une variété d'options pour votre configuration d'éclairage. Il en va différemment lors d'un déploiement avec, par exemple, LunaNode. Pour les besoins de ce guide, un Lite Node suffira. Pour en savoir plus sur les différences, consultez Voltage.cloud.


![image](assets/en/120.webp)


Donnez un nom à votre nœud, définissez un mot de passe et sécurisez ce mot de passe. Si ce mot de passe est perdu, vous perdez l'accès à vos sauvegardes et Voltage ne peut pas le récupérer. Créez le nœud, et Voltage vous montre la progression. Voltage a créé votre nœud Lightning. Nous pouvons maintenant créer l'instance du serveur BTCPay et accéder directement au Lightning Network.


Cliquez sur Nœuds en haut à gauche de votre tableau de bord. Ici, vous pouvez configurer la prochaine partie de votre instance de serveur BTCPay. Cliquez sur "create new" une fois que vous êtes dans la vue d'ensemble des nœuds. Vous obtenez un écran similaire à celui d'avant. Maintenant, au lieu de Lightning Node, nous choisissons BTCPay Server.


Voltage vous montre la géolocalisation de votre serveur BTCPay, qui est hébergé dans la région Ouest des Etats-Unis. Vous y verrez également le coût de l'hébergement du serveur. Cliquez sur Créer et donnez un nom à votre serveur BTCPay. Activez Lightning et Voltage vous montre le nœud Lightning créé à l'étape précédente. Cliquez sur Créer, et Voltage créera une instance de serveur BTCPay.


![image](assets/en/121.webp)


Après avoir cliqué sur créer, Voltage vous présente le nom d'utilisateur et le mot de passe par défaut. Ceux-ci sont similaires au mot de passe que vous avez défini précédemment dans Voltage. Cliquez sur le bouton Connexion au compte pour vous rediriger vers votre serveur BTCPay.


Bienvenue dans votre nouvelle instance de serveur BTCPay. Comme nous avons déjà mis en place Lightning dans le processus de création, cela montre que Lightning est déjà activé !


### Résumé des compétences


Dans ce chapitre, vous avez appris



- Créer un compte sur Voltage.cloud
- Etapes pour faire fonctionner le serveur BTCPay avec un nœud Lightning sur le compte


### Évaluation des connaissances


#### Examen conceptuel de l'AC


Quelles sont les principales différences entre les installations Voltage et LunaNode ?


## Installer BTCPay Server sur un nœud Umbrel


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


A la fin de ces étapes, vous pouvez accepter des paiements Lightning dans votre boutique BTCPay sur votre réseau local. Ce processus s'appliquera également si vous gérez un nœud umbrel dans un restaurant ou une entreprise. Si vous souhaitez connecter cette boutique à un site web public, suivez l'exercice Avancé pour exposer votre nœud umbrel au public.


https://umbrel.com/


![image](assets/en/122.webp)


### Serveur BTCPay - Déploiement d'Umbrel


Une fois que votre nœud Umbrel est entièrement synchronisé avec le Bitcoin Blockchain, allez dans l'App Store d'Umbrel, et cherchez BTCPay Server sous Apps.


![image](assets/en/123.webp)


Cliquez sur BTCPay Server pour voir les détails de l'application. Lorsque les détails de BTCPay Server sont ouverts, le coin inférieur droit montre les conditions requises pour que l'application fonctionne correctement. Il indique que l'application nécessite un Bitcoin et un nœud Lightning. Si vous n'avez pas installé le nœud Lightning sur votre Umbrel, cliquez sur Installer. Ce processus peut prendre quelques minutes.


![image](assets/en/124.webp)


Après avoir installé votre Node :


1. Cliquez sur ouvrir dans les détails de l'application ou sur l'application dans le tableau de bord des Parapluies.

2. Cliquez sur Configurer un nouveau nœud ; vous verrez apparaître 24 mots pour la récupération de votre nœud de foudre.

3. Notez-les.


![image](assets/en/125.webp)


Umbrel vous demandera de vérifier les mots que vous venez d'écrire. Une fois le nœud Lightning configuré, retournez dans l'App Store d'Umbrel et trouvez BTCPay Server. Cliquez sur le bouton d'installation, et Umbrel montrera si les composants requis sont installés et que BTCPay Server nécessite l'accès à ces composants. Après l'installation, cliquez sur Open dans le coin supérieur droit des détails de l'application ou ouvrez BTCPay Server via votre tableau de bord Umbrel.


Umbrel demandera une vérification des mots qui viennent d'être écrits.


![image](assets/en/126.webp)


**!Note!**


Veillez à les conserver dans un endroit sûr, comme vous l'avez appris précédemment en conservant les clés.


Une fois le nœud Lightning configuré, retournez à l'App Store d'Umbrel et trouvez BTCPay Server. Cliquez sur le bouton d'installation, et Umbrel montrera si les composants requis sont installés et que BTCPay Server nécessite l'accès à ces composants.


![image](assets/en/127.webp)


Après l'installation, cliquez sur Ouvrir en haut à droite des détails de l'application ou ouvrez BTCPay Server via votre tableau de bord Umbrels.


![image](assets/en/128.webp)


### Résumé des compétences


Dans cette section, vous avez appris



- Etapes pour installer le serveur BTCPay avec la fonctionnalité Lightning sur un nœud Umbrel


### Évaluation des connaissances


#### Examen conceptuel de l'AC


En quoi la configuration d'Umbrel diffère-t-elle des deux options d'hébergement précédentes ?


# Section finale


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Critiques et évaluations

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusion du cours


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>