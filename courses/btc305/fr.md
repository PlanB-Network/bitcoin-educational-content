---
name: Bitcoin et BTCPay Server
goal: Installer BTCPay Server pour votre entreprise
objectives:
  - Comprendre ce qu'est btcpayserver.
  - Auto-héberger et configurer BTCPay Server.
  - Utiliser btcpayserver dans votre activité quotidienne.
---

# Bitcoin et BTCPay Server

Ceci est un cours d'introduction sur l'opérateur BTCPay Server écrit par Alekos et Bas, qui a été adapté au format de cours Plan ₿ par melontwist et asi0.

UNE HISTOIRE INACHEVÉE

"Ceci est faux, ma confiance en vous est brisée, je vous rendrai obsolète".

Produit par la Fondation BTCPay Server

+++

# Introduction

<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>

## Acclamations critiques pour l'œuvre de l'auteur sur Bitcoin et BTCPay Server

<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>

Commençons par ce qu'est BTCPay Server et d'où il vient. Nous valorisons la transparence et certaines normes pour former la confiance dans l'espace Bitcoin.
Un projet dans cet espace a rompu ces valeurs. Le développeur principal de BTCPay Server, Nicolas Dorier, a pris cela personnellement et a fait la promesse de les rendre obsolètes. Nous voici, des années plus tard, travaillant vers cet avenir, entièrement open-source, chaque jour.

> Ceci est faux, ma confiance en vous est brisée, je vous rendrai obsolète.
> Nicolas Dorier

Après les mots prononcés par Nicolas, il était temps de commencer à construire. Beaucoup de travail a été investi dans ce que nous appelons maintenant BTCPay Server. Plus de personnes voulaient aider à pousser ce projet. Les plus reconnaissables sont r0ckstardev, MrKukks, Pavlenex, et le premier commerçant à utiliser le logiciel, astupidmoose.

Que signifie open source, et qu'implique un tel projet ?

FOSS signifie Logiciel Libre et Open Source. Le premier terme se réfère à des conditions qui permettent à quiconque de copier, modifier, et même distribuer des versions (même à des fins lucratives) du logiciel. Le second terme se réfère au partage ouvert du code source, encourageant le public à contribuer et à l'améliorer.
Cela attire des utilisateurs expérimentés enthousiastes à contribuer au logiciel qu'ils utilisent déjà et dont ils tirent de la valeur, prouvant avec le temps que cela l'emporte en adoption sur les logiciels propriétaires. Cela est conforme à l'éthos de Bitcoin selon lequel "l'information aspire à être libre". Cela rassemble des personnes passionnées qui forment une communauté et c'est tout simplement plus amusant. Comme Bitcoin, le FOSS est inévitable.

### Avant de commencer

Ce cours se compose de plusieurs parties. Beaucoup seront pris en charge par votre enseignant en classe, des environnements de démonstration auxquels vous aurez accès, un serveur hébergé pour vous-même, et éventuellement un nom de domaine. Si vous suivez ce cours de manière indépendante, veuillez être conscient que les environnements étiquetés comme DEMO ne seront pas disponibles pour vous.
NB. Si vous suivez ce cours en classe, les noms de serveurs peuvent différer en fonction de votre configuration de classe. Les variables dans les noms de serveurs peuvent être différentes à cause de cela.

### Structure du cours

Chaque chapitre a des objectifs et des évaluations des connaissances. Dans ce cours, nous couvrirons chacun de ces points et aurons un résumé des caractéristiques clés à chaque bloc de leçon (c.-à-d. chapitre). Des illustrations sont présentées pour fournir un retour visuel et renforcer les concepts clés d'un point de vue visuel. Les objectifs sont fixés au début de chaque bloc de leçon. Ces objectifs vont au-delà d'une simple liste de vérification. Ils vous fournissent un guide vers un nouvel ensemble de compétences. Les évaluations des connaissances deviennent progressivement plus difficiles à mesure que vous configurez votre BTCPay Server.

### Que reçoivent les étudiants avec le cours ?

Avec le cours BTCPay Server, un étudiant peut comprendre les principes de base, techniques et non techniques, de Bitcoin. La formation approfondie à l'utilisation de Bitcoin via BTCPay Server permettra aux étudiants d'opérer leur propre infrastructure Bitcoin.

### Adresses Web importantes ou opportunités de contact

La Fondation BTCPay Server, qui a permis à Alekos et Bas d'écrire ce cours, se trouve à Tokyo, Japon. La Fondation BTCPay Server peut être contactée via le site web listé ;

- https://foundation.btcpayserver.org
- rejoignez les canaux de chat officiels :https://chat.btcpayserver.org

## Introduction à Bitcoin

<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>

### Comprendre Bitcoin via un exercice en classe

Ceci est un exercice en classe donc si vous suivez ce cours vous-même, vous ne pouvez pas le réaliser mais vous pouvez quand même passer par cet exercice. Pour compléter cette tâche, le nombre minimum de personnes est entre 9 et 11.

L'exercice commence après avoir regardé l'introduction "Comment fonctionnent Bitcoin et la blockchain" par la BBC.

![how bitcoin and the blockchain works](https://youtu.be/mhE_vvwAiRc)

Cet exercice nécessite la participation d'au moins neuf personnes. Cet exercice a pour but de se faire une idée physique du fonctionnement de Bitcoin. En jouant chaque rôle dans le réseau, vous aurez une manière interactive et ludique d'apprendre. Cet exercice n'implique pas le Lightning Network.

### Exemple ; Nécessite 9 / 11 personnes

Les rôles sont :

- 1 Client
- 1 Commerçant
- 7 à 9 nœuds Bitcoin

**La configuration est la suivante :**

Le client achète un produit dans le magasin avec Bitcoin.

**Scénario 1 - Système bancaire traditionnel**

- Configuration :
  - Voir les schémas/explications dans le Figjam joint - [Schéma d'Activité](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Obtenir trois volontaires parmi les étudiants pour jouer les rôles du Client (Alice), du Commerçant (Bob) et de la Banque.
- Déroulement des événements :
  - Client- navigue sur le magasin en ligne et trouve un article à 25 $ qu'il souhaite, et informe le Commerçant qu'il aimerait acheter
  - Commerçant- demande un paiement.
  - Client- envoie les informations de carte au Commerçant
  - Commerçant- transmet les informations à la Banque (identifiant à la fois leur propre identité et celle/informations) demandant le paiement de
  - La Banque collecte des informations sur le Client et le Commerçant (Alice et Bob) et vérifie que le solde du client est suffisant.
  - Déduit 25 \$ du compte d'Alice, ajoute 24 \$ au compte de Bob, prend 1 \$ pour le service
  - Le Commerçant reçoit le feu vert de la Banque et expédie l'article au client.
- Commentaires :
  - Bob et Alice doivent avoir une relation avec une banque.
  - La banque collecte des informations d'identification sur Bob et Alice.
  - La banque prend une commission.
  - La banque doit être digne de confiance pour la garde de l'argent de chaque participant tout le temps.

**Scénario 2 - Système Bitcoin**

- Configuration :
  - Voir les schémas/explications dans le Figjam joint - [Schéma d'Activité](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
- Remplacez la Banque par neuf étudiants qui joueront le rôle d'un Ordinateur (Nœuds/Miniers Bitcoin) dans un réseau pour remplacer la Banque. - Chacun des 9 Ordinateurs possède un historique complet de toutes les transactions passées jamais effectuées (assurant ainsi des soldes précis sans contrefaçons), ainsi qu'un ensemble de règles :
  - Vérifier que la transaction est correctement signée (laclécorrespondauloquet)
  - Diffuser et recevoir des transactions valides auprès des pairs dans le réseau, rejeter les invalides (y compris celles qui tentent de dépenser les mêmes fonds deux fois)
- Mettre à jour/Ajouter des enregistrements périodiquement avec de nouvelles transactions reçues d’un ordinateur “aléatoire” à condition que tous les contenus soient valides (note : nous ignorons, pour l'instant, le composant Preuve de Travail de tout cela, pour simplifier), sinon rejeter ces dernières et continuer comme avant jusqu'à ce que le prochain ordinateur “aléatoire” envoie une mise à jour
  - La quantité appropriée a été récompensée si les contenus étaient valides.
- Jouer la séquence d'événements :
  - Client- naviguant sur le magasin en ligne et trouve un article à 25 $ qu'ils veulent, et informe le Marchand qu’ils aimeraient acheter
  - Marchand- demande un paiement en envoyant au client une facture/adresse de leur portefeuille.
  - Client- construit une transaction (envoyant 25 $ en BTC à une adresse fournie par le Marchand) et la diffuse au Réseau Bitcoin.
- Ordinateurs- reçoivent la transaction et vérifient :
  - Il y a au moins 25 $ de BTC dans l'adresse envoyée
  - La transaction est correctement signée (“déverrouillée” par le client)
  - Si ce n'est pas le cas, alors la transaction ne sera pas propagée à travers le réseau, et si c'est le cas, alors elle se propage et est mise en attente.
  - Les marchands peuvent vérifier que la transaction est en attente.
- Un ordinateur est “choisi aléatoirement” pour proposer de finaliser la transaction proposée en diffusant “un bloc” la contenant ; si cela est vérifié, ils recevront une récompense en BTC.
  - OPTIONNEL/AVANCÉ - au lieu de sélectionner aléatoirement un Ordinateur, simuler le minage en faisant lancer des dés aux Ordinateurs jusqu'à ce qu'un résultat prédéterminé se produise (par exemple, le premier à obtenir un double six est sélectionné)
  - Cela peut aussi jouer ce qui se passerait si deux Ordinateurs gagnent approximativement simultanément, résultant en une scission de la chaîne.
  - Les ordinateurs vérifient la validité, mettent à jour/ajoutent des enregistrements à leurs registres si les règles sont respectées, et diffusent le bloc à leurs pairs.
  - L'ordinateur choisi aléatoirement reçoit une récompense pour avoir proposé un bloc valide.
  - Le marchand vérifie que la transaction a été finalisée ; ainsi, les fonds ont été reçus, et l'article a été envoyé au client.
- Commentaires :
  - Remarquez qu'il n'était pas nécessaire d'avoir une relation bancaire préexistante.
  - Aucune tierce partie n'est nécessaire pour faciliter ; remplacée par le code/les incitations.
  - Aucune collecte de données par quiconque en dehors de l'échange direct et seulement la quantité nécessaire doit être échangée entre les participants (par exemple, adresse de livraison).
  - Aucune confiance n'est requise entre les personnes (autre que le Marchand envoyant l'article), à bien des égards comme un achat en espèces.
  - L'argent est directement possédé par les individus.
  - Le registre Bitcoin est représenté en dollars pour simplifier, mais en réalité, c'est en BTC.
  - Nous simulons une seule transaction diffusée, mais en réalité, de multiples transactions sont en attente dans le réseau, et les blocs comprennent des milliers de transactions à la fois. Les nœuds vérifient également qu'il n'y a pas de transactions de double dépense en attente (je rejetterais toutes sauf une si c'était le cas).
- Scénarios de tricherie :
  - Que se passerait-il si le client n'avait pas 25 $ en BTC ?
    - Ils ne seraient pas capables de créer la transaction parce que “déverrouiller” et “posséder” sont la même chose, et les ordinateurs vérifient que la transaction est correctement signée ; sinon, ils la rejettent.
- Que se passe-t-il si l'ordinateur choisi au hasard tente de "modifier le registre" ?
  - Le bloc serait rejeté, car tous les autres ordinateurs ont un historique complet et remarqueraient le changement, violant ainsi l'une de leurs règles.
  - L'Ordinateur Aléatoire ne recevrait pas de récompense, et aucune transaction de leur bloc ne serait finalisée.

## Évaluation des connaissances

<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>

### Discussion en classe KA

Discutez de certaines simplifications faites lors de l'exercice en classe sous le deuxième scénario et décrivez ce que le système Bitcoin fait réellement de manière plus détaillée.

### Révision du vocabulaire KA

Définissez les termes clés suivants introduits dans la section précédente :

- Nœud
- Mempool
- Cible de Difficulté
- Bloc

**Discutez de la signification de certains termes supplémentaires en groupe :**

Blockchain, Transaction, Double-Dépense, Problème des Généraux Byzantins, Minage, Preuve de Travail (PoW), Fonction de Hachage, Récompense de Bloc, Blockchain, Chaîne la Plus Longue, Attaque des 51%, Sortie, Verrou de Sortie, Changement, Satoshis, Clé Publique/Privée, Adresse, Cryptographie à Clé Publique, Signature Numérique, Portefeuille

# Présentation du serveur BTCPay

<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>

## Comprendre l'écran de connexion BTCPay Server

<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>

### Travailler avec BTCPay Server

L'objectif de ce bloc de cours sera d'avoir une compréhension générale du logiciel BTCPay Server. Dans un environnement partagé, il est recommandé de suivre la démonstration de l'instructeur et de suivre le manuel de cours BTCPay Server pour suivre l'enseignant. Vous apprendrez à créer un portefeuille par plusieurs méthodes. Les exemples incluent les configurations de portefeuilles chauds et les portefeuilles matériels connectés via BTCPay Server Vault. Ces objectifs se déroulent dans l'environnement de démonstration, affiché et donné accès par votre instructeur de cours.

Si vous suivez ce cours par vous-même, vous pouvez trouver une liste d'hôtes tiers à des fins de démonstration sur https://directory.btcpayserver.org/filter/hosts. Nous déconseillons vivement d'utiliser ces options tierces comme environnements de production, mais elles servent les bons objectifs pour une introduction à l'utilisation de Bitcoin et BTCPay Server.

En tant que stagiaire rockstar BTCPay Server, vous pourriez avoir une expérience préalable de la configuration d'un nœud Bitcoin. Ce cours parlera spécifiquement adapté à la pile logicielle BTCPay Server.

De nombreuses options dans BTCPay Server existent sous une forme ou une autre dans d'autres logiciels liés aux portefeuilles Bitcoin.

### Écran de connexion BTCPay Server

Lorsque vous êtes accueilli dans l'environnement de démonstration, on vous demande de vous 'Connecter' ou de 'Créer votre compte'. Les administrateurs de serveur peuvent désactiver la fonction de création de nouveaux comptes pour des raisons de sécurité. Les logos et les couleurs des boutons BTCPay Server peuvent être modifiés car BTCPay Server est un logiciel Open Source. Un hôte tiers peut appliquer sa marque sur le logiciel et changer tout l'aspect.

![image](assets/en/0.webp)

### Fenêtre de création de compte

La création de comptes sur BTCPay Server nécessite des chaînes d'adresse Email valides ; example@email.com serait une chaîne valide pour Email.

Le mot de passe doit comporter au moins 8 caractères, incluant des lettres, des chiffres et des caractères. Après avoir défini le mot de passe une fois, vous devrez vérifier le mot de passe saisi pour vous assurer qu'il est correct par rapport à ce qui a été tapé dans le premier champ de mot de passe.
Lorsque les champs Email et Mot de passe sont correctement remplis, cliquez sur le bouton « Créer un compte ». Cela enregistrera l'Email et le mot de passe sur l'instance BTCPay Server de l'instructeur.
![image](assets/en/1.webp)

**!Note!**

Si vous suivez ce cours par vous-même, la création de ce compte serait quelque chose que vous pourriez faire sur un hôte tiers ; donc, encore une fois, nous mentionnons de ne jamais utiliser ces environnements comme des environnements de production mais uniquement à des fins de formation.

### Création de compte par l'administrateur de BTCPay Server

L'administrateur de l'instance BTCPay Server peut également créer des comptes pour BTCPay Server. L'administrateur de l'instance BTCPay Server peut cliquer sur « Paramètres du serveur » (1), cliquer sur l'onglet « Utilisateurs » (2), et cliquer sur le bouton « + Ajouter un utilisateur » (3) en haut à droite de l'onglet Utilisateurs. Dans l'Objectif (4.3), vous en apprendrez plus sur le contrôle des comptes par l'administrateur.

![image](assets/en/2.webp)

En tant qu'administrateur, vous aurez besoin de l'adresse Email de l'utilisateur et de définir un mot de passe standard. Il est conseillé, en tant qu'administrateur, d'informer l'utilisateur qu'il doit changer ce mot de passe avant d'utiliser le compte pour des raisons de sécurité. Si l'administrateur NE définit PAS de mot de passe et que SMTP a été configuré sur le serveur, l'utilisateur recevra un email avec un lien d'invitation pour créer son compte et définir le mot de passe lui-même.

### Exemple

Lorsque vous suivez le cours avec un instructeur, suivez le lien donné par l'instructeur et créez votre compte sur l'environnement de démonstration fourni. Assurez-vous que votre adresse email et votre mot de passe sont sauvegardés en sécurité ; vous aurez besoin de ces identifiants de connexion pour le reste des objectifs de démonstration de ce cours.

Votre instructeur peut avoir recueilli l'adresse email à l'avance et envoyé un lien d'invitation avant cet exercice. Si cela vous est indiqué, vérifiez votre Email.

Lorsque vous prenez le cours sans instructeur, créez votre compte en utilisant l'environnement de démonstration de BTCPay Server ; allez sur

https://mainnet.demo.btcpayserver.org/login.

Ce compte ne doit être utilisé que pour des fins de démonstration/formation et jamais pour des affaires.

### Résumé des compétences

Dans cette section, vous avez appris ce qui suit :

- Comment créer un compte sur un serveur hébergé via l'interface.
- Comment un administrateur de serveur peut manuellement ajouter des utilisateurs dans les paramètres du serveur.

### Évaluation des connaissances

#### Révision conceptuelle de KA

Donnez des raisons pour lesquelles utiliser un serveur de démo est une mauvaise idée à des fins de production.

## Gestion des compte(s) utilisateur

<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>

### Gestion de compte sur BTCPay Server

Après qu'un propriétaire de magasin ait créé son compte, il peut le gérer en bas à gauche de l'interface utilisateur de BTCPay Server. Sous le bouton Compte, il y a plusieurs paramètres de niveau supérieur.

- Mode Sombre/Clair.
- Basculer Masquer les infos sensibles.
- Gérer le compte.

![image](assets/en/3.webp)

### Mode Sombre et Clair

Les utilisateurs de BTCPay Server peuvent choisir entre une version en mode Sombre ou Clair de l'interface utilisateur. Les pages orientées client ne changeront pas. Elles utilisent les paramètres préférés des clients concernant le mode sombre ou clair.

### Basculer Masquer les infos sensibles

Le bouton masquer les infos sensibles apporte une couche de sécurité rapide et simple. Lorsque vous devez opérer votre BTCPay Server, mais qu'il pourrait y avoir des personnes qui regardent par-dessus votre épaule dans un espace public, activez Masquer les infos sensibles, et toutes les valeurs dans BTCPay Server seront cachées. Quelqu'un pourrait regarder par-dessus votre épaule mais ne pourra plus voir les valeurs avec lesquelles vous traitez.

### Gérer le compte

Une fois le compte utilisateur créé, c'est ici que vous gérez les mots de passe, la 2fa, ou les clés API.

### Gérer le compte - Compte

Il est possible de mettre à jour votre compte avec une adresse Email différente. Pour vous assurer que votre adresse email est correcte, BTCPay Server vous permet d'envoyer un email de vérification. Cliquez sur enregistrer si l'utilisateur définit une nouvelle adresse email et confirme que la vérification a fonctionné. Le nom d'utilisateur reste le même que l'Email précédent.

Un utilisateur peut décider de supprimer son compte entièrement. Cela peut être fait en cliquant sur le bouton de suppression dans l'onglet Compte.

![image](assets/en/4.webp)

**!Note!**

Après avoir changé l'Email, le nom d'utilisateur pour le compte ne changera pas. L'adresse Email précédemment donnée restera le nom de connexion.

### Gérer le compte - Mot de passe

Un étudiant peut vouloir changer son mot de passe. Il peut le faire en allant dans l'onglet Mot de passe. Ici, il doit taper son ancien mot de passe et peut le changer pour un nouveau.

![image](assets/en/5.webp)

### Authentification à Deux Facteurs (2fa)

Pour limiter les conséquences d'un mot de passe volé, vous pouvez utiliser l'authentification à deux facteurs (2fa), une méthode de sécurité relativement nouvelle. Vous pouvez activer l'authentification à deux facteurs via le Gérer le compte et l'onglet pour l'authentification à deux facteurs. Vous devez compléter une deuxième étape après vous être connecté avec votre nom d'utilisateur et votre mot de passe.

BTCPay Server permet deux manières d'activer la 2FA, 2FA basée sur l'application (Authy, Google, Microsoft authenticators) ou via des dispositifs de sécurité (FIDO2 ou LNURL Auth).

### Authentification à Deux Facteurs - Basée sur l'application

En fonction du système d'exploitation de votre téléphone mobile (Android ou iOS), les utilisateurs peuvent choisir entre les applications suivantes ;

1. Téléchargez un authentificateur à deux facteurs ;
   - Authy pour [Android](https://play.google.com/store/apps/details?id=com.authy.authy) ou [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator pour [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) ou [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator pour [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) ou [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)
2. Après avoir téléchargé et installé l'application Authenticator.
   - Scannez le QR Code fourni par BTCPay Server
   - Ou entrez la clé générée par BTCPay Server manuellement dans votre application Authenticator.
3. L'application Authenticator vous fournira un code unique. Entrez le code unique dans BTCPay Server pour vérifier la configuration, et cliquez sur vérifier pour compléter le processus.

![image](assets/en/6.webp)

### Résumé des compétences

Dans cette section, vous avez appris ce qui suit :

- Les options de gestion de compte et les différentes manières de gérer un compte sur une instance BTCPay Server.
- Comment configurer la 2FA basée sur l'application.

### Évaluation des connaissances

#### Révision conceptuelle de KA

Décrivez comment la 2FA basée sur l'application aide à sécuriser votre compte

## Création d'une nouvelle boutique

<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>

### Créez votre boutique avec l'assistant

Lorsqu'un nouvel utilisateur se connecte à BTCPay Server, l'environnement est vide et nécessite la création d'un premier magasin. L'assistant d'introduction de BTCPay Server donnera à l'utilisateur l'option de « Créer votre magasin » (1). Un magasin peut être vu comme un foyer pour vos besoins en Bitcoin. Un nouveau nœud BTCPay Server commencera par la synchronisation de la Blockchain Bitcoin (2). Selon l'infrastructure sur laquelle vous exécutez BTCPay Server, cela peut prendre de quelques heures à quelques jours. La version actuelle de l'instance est affichée dans le coin inférieur droit de votre interface utilisateur BTCPay Server. Ceci est utile pour référence lors du dépannage.
![image](assets/en/7.webp)

### Assistant de création de votre magasin

Suivre ce cours commencera avec un écran légèrement différent de la page précédente. Comme votre instructeur a préparé l'environnement de démonstration, la blockchain Bitcoin a été synchronisée au préalable, et donc vous ne verrez pas le statut de synchronisation des nœuds.

Un utilisateur peut décider de supprimer son compte entier. Cela peut être fait en cliquant sur le bouton de suppression dans l'onglet Compte.

![image](assets/en/8.webp)

**!Note!**

Les comptes BTCPay Server peuvent créer un nombre illimité de magasins. Chaque magasin est un portefeuille ou « foyer ».

### Exemple

Commencez par cliquer sur "Créer votre magasin".

![image](assets/en/9.webp)

Cela créera votre premier foyer et tableau de bord pour utiliser BTCPay Server.

(1) Après avoir cliqué sur "Créer votre magasin", BTCPay Server vous demandera de nommer le magasin ; cela peut être n'importe quoi d'utile pour vous.

![image](assets/en/10.webp)

(2) Il faut ensuite définir une devise par défaut pour le magasin, soit une monnaie fiduciaire soit une dénomination en standard Bitcoin / Sats. Pour l'environnement de démo, nous le définirons en USD.

![image](assets/en/11.webp)

(3) Comme dernier paramètre lors de la configuration du magasin, BTCPay Server vous demande de définir une "Source de prix préférée" pour comparer le prix du Bitcoin par rapport au prix fiat actuel afin que votre magasin affiche le taux de change correct entre le Bitcoin et la devise fiat définie pour le magasin. Nous resterons avec la valeur par défaut dans l'exemple de démo et définirons cela à l'échange Kraken. BTCPay Server utilise l'API Kraken pour vérifier les taux de change.

![image](assets/en/12.webp)

(4) Maintenant que ces paramètres de magasin ont été définis, cliquez sur le bouton Créer, et BTCPay Server créera le tableau de bord de votre premier magasin, où l'assistant continuera.

![image](assets/en/13.webp)

Félicitations, vous avez créé votre premier magasin, et cela conclut cet exercice.

![image](assets/en/14.webp)

### Résumé des compétences

Dans cette section, vous avez appris :

- La création de magasin et la configuration d'une devise par défaut combinée aux préférences de source de prix.
- Chaque "Magasin" est un nouveau foyer séparé des autres magasins sur cette installation de BTCPay Server.

# Introduction à la sécurisation des clés Bitcoin

<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>

## Comprendre la génération des clés Bitcoin

<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>

### Qu'est-ce qui est impliqué dans la génération des clés bitcoin ?

Les portefeuilles Bitcoin, lorsqu'ils sont créés, génèrent ce qu'on appelle une "graine". Dans le dernier objectif, vous avez créé une "graine". La série de mots générés avant est également connue sous le nom de phrases mnémoniques. La graine est utilisée pour dériver des clés Bitcoin individuelles et utilisée pour envoyer ou recevoir des Bitcoin. Les phrases de graine ne doivent jamais être partagées avec des tiers ou des pairs non fiables.
La génération de clés est réalisée selon la norme industrielle connue sous le nom de cadre "Hierarchical Deterministic" (HD).
![image](assets/en/15.webp)

### Adresses

BTCPay Server est conçu pour générer une nouvelle Adresse. Cela soulage le problème de réutilisation de clé publique ou d'Adresse. Utiliser la même clé publique rend le suivi de votre historique de paiement complet très facile. Penser aux clés comme à des bons à usage unique améliorerait considérablement votre vie privée. Nous utilisons également des Adresses Bitcoin, ne les confondez pas avec les clés publiques.

Une Adresse est dérivée de la clé publique via un "algorithme de hachage". Cependant, la plupart des portefeuilles et des transactions afficheront des Adresses plutôt que ces clés publiques. Les Adresses sont, en général, plus courtes que les clés publiques et commencent généralement par `1`, `3`, ou `bc1`, tandis que les clés publiques commencent par `02`, `03`, ou `04`.

- Les Adresses commençant par `1.....` sont encore des adresses très courantes. Comme mentionné dans le chapitre Création d'un nouveau magasin, ce sont des adresses héritées. Ce type d'adresse est destiné aux transactions P2PKH. P2Pkh utilise l'encodage Base58, ce qui rend l'adresse sensible à la casse. Sa structure est basée sur la clé publique avec un chiffre supplémentaire comme identifiant.

- Les Adresses commençant par `bc1...` passent lentement dans la catégorie des adresses très courantes. Elles sont connues comme Adresses SegWit (natives). Elles offrent une meilleure structure de frais que les autres Adresses mentionnées. Les Adresses SegWit natives utilisent l'encodage Bech32 et n'autorisent que les lettres minuscules.

- Les Adresses commençant par `3...` sont couramment utilisées par les échanges pour les adresses de dépôt. Ces adresses sont mentionnées dans le chapitre Création d'un nouveau magasin, comme des adresses SegWit emballées ou imbriquées. Cependant, elles pourraient également fonctionner comme une "Adresse Multisig". Lorsqu'elles sont utilisées comme une adresse SegWit, il y a encore des économies sur les frais de transaction, moins cependant que pour le SegWit natif. Les Adresses P2SH utilisent l'encodage Base58. Cela les rend sensibles à la casse, comme l'adresse héritée.

- Les Adresses commençant par `2...` sont des adresses Testnet. Elles sont destinées à recevoir du bitcoin testnet (tBTC). Vous ne devriez jamais confondre cela et envoyer du Bitcoin à ces adresses. Pour des fins de développement, vous pouvez générer un portefeuille testnet. Il existe plusieurs robinets en ligne pour obtenir du Bitcoin testnet. Ne jamais acheter de Bitcoin testnet. Le Bitcoin testnet est miné. Cela pourrait être une raison pour un développeur d'utiliser Regtest à la place. Il s'agit d'un environnement de jeu pour les développeurs, manquant de certains composants réseau. Cependant, le Bitcoin est, à des fins de développement, très utile.

### Clés Publiques

Les clés publiques sont moins utilisées en pratique aujourd'hui. Avec le temps, les utilisateurs de bitcoin les ont remplacées par des Adresses. Elles existent toujours et sont occasionnellement utilisées. Les clés publiques sont, en général, des chaînes beaucoup plus longues que les adresses. Tout comme avec les adresses, elles commencent par un identifiant spécifique.

- D'abord, `02...` et `03...` sont des identifiants de clé publique très standards codés au format SEC. Ils peuvent être traités et transformés en adresses pour recevoir, utilisés pour créer des adresses multi-signatures, ou pour vérifier une signature. Les transactions Bitcoin des premiers jours utilisaient des clés publiques comme partie des transactions P2PK.

- Cependant, les portefeuilles HD utilisent une structure différente. `xpub...`, `ypub...` ou `zpub...` sont appelés clés publiques étendues, plus communément appelées xpubs. Ces clés sont utilisées pour dériver de nombreuses clés publiques car elles font partie du portefeuille HD. Comme votre xpub détient les enregistrements de votre historique complet, signifiant les transactions passées et futures, ne partagez jamais ces informations avec des parties non fiables.

### Résumé des Compétences

Dans cette section, vous avez appris ce qui suit :

- Les différences entre les adresses et les types de données de clé publique et les avantages de l'utilisation des adresses par rapport aux clés publiques.

### Évaluation des connaissances

Décrivez l'avantage d'utiliser des adresses fraîches pour chaque transaction par rapport à la réutilisation d'adresses ou aux méthodes de clé publique

## Sécurisation des clés avec un portefeuille matériel

<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>

### Stockage des clés Bitcoin

Après avoir généré une phrase de récupération, la liste de 12 à 24 mots générés dans ce livre nécessite des sauvegardes et une sécurité appropriées, car ces mots sont le seul moyen de récupérer l'accès à un portefeuille. La structure des portefeuilles HD et comment elle génère des adresses de manière déterministe en utilisant cette unique graine, toutes vos adresses créées seront sauvegardées en utilisant cette unique liste de mots mnémoniques représentant votre graine ou phrase de récupération.

Gardez votre phrase de récupération en sécurité. Si elle est accédée par quelqu'un, spécifiquement avec une intention malveillante, ils peuvent déplacer vos fonds. Garder la graine sûre et sécurisée mais aussi se souvenir d'elle est mutuel. Il existe plusieurs méthodes pour stocker les clés privées Bitcoin, chacune avec des avantages et des inconvénients, que ce soit en termes de sécurité, de confidentialité, de commodité ou de moyens physiques. En raison de l'importance des clés privées, les utilisateurs de bitcoin ont tendance à stocker et à garder ces clés en "auto-garde" plutôt que d'utiliser des services "custodiaux" comme les banques. Selon l'utilisateur, il doit utiliser soit une solution de stockage à froid soit un portefeuille chaud.

### Stockage chaud et froid des clés bitcoin

Habituellement, les portefeuilles bitcoin sont dénommés en portefeuille chaud ou portefeuille froid. La plupart des compromis résident dans la commodité, la facilité d'utilisation et les risques de sécurité. Chacune de ces méthodes peut également être vue dans une solution de custodian. Cependant, les compromis ici sont principalement basés sur la sécurité et la confidentialité et vont au-delà du cadre de ce cours.

### Portefeuille chaud

Les portefeuilles chauds sont le moyen le plus pratique d'interagir avec Bitcoin via mobile, web ou logiciel de bureau. Le portefeuille est toujours connecté à Internet, permettant aux utilisateurs d'envoyer ou de recevoir du Bitcoin. Cependant, c'est aussi sa faiblesse, le portefeuille, étant toujours en ligne, est maintenant plus vulnérable aux attaques par des pirates informatiques ou des logiciels malveillants sur votre appareil. Dans BTCPay Server, les portefeuilles chauds stockent les clés privées sur l'instance. Toute personne accédant à votre magasin BTCPay Server pourrait voler des fonds de cette adresse si malveillante. Lorsque BTCPay Server fonctionne dans un environnement hébergé, vous devriez toujours considérer cela dans votre profil de sécurité et de préférence ne pas utiliser un portefeuille chaud dans un tel cas. Lorsque BTCPay Server est installé sur du matériel vous appartenant, sécurisé et de confiance pour vous, le profil de risque diminue considérablement, mais il ne disparaît jamais !

### Portefeuille froid

Les individus déplacent leur Bitcoin dans un portefeuille froid parce qu'il peut isoler les clés privées d'Internet. Retirer la connexion Internet de l'équation réduit le risque de logiciels malveillants, de logiciels espions et de swaps de SIM. Le stockage à froid est considéré comme supérieur au stockage chaud pour la sécurité et l'autonomie, tant que des précautions adéquates sont prises pour éviter de perdre les clés privées Bitcoin. Le stockage à froid convient le mieux aux grandes quantités de Bitcoin, qui ne sont pas destinées à être dépensées souvent en raison de la complexité de la configuration du portefeuille.

Il existe diverses méthodes de stockage des clés Bitcoin en stockage à froid, des portefeuilles papier aux portefeuilles cérébraux, portefeuilles matériels, ou, dès le début, un fichier de portefeuille. La plupart des portefeuilles utilisent BIP 39 pour générer la phrase de récupération. Cependant, au sein du logiciel Bitcoin Core, un consensus n'a pas encore été atteint sur son utilisation. Le logiciel Bitcoin Core générera toujours un fichier Wallet.dat que vous devez stocker dans un emplacement hors ligne sécurisé.

### Résumé des compétences

Dans cette section, vous avez appris :

- Les différences entre les portefeuilles chauds et froids en termes de fonctionnalité et leurs compromis.

### Évaluation des connaissances Revue conceptuelle

- Qu'est-ce qu'un portefeuille ?
- Quelle est la différence entre les portefeuilles chauds et froids ?

- Décrire ce que signifie "générer un portefeuille" ?

## Utiliser vos clés Bitcoin

<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>

### Portefeuille BTCPay Server

BTCPay Server comprend les fonctionnalités standard suivantes de portefeuille :

- Transactions
- Envoyer
- Recevoir
- Rescan
- Paiements Pull
- Paiements
- PSBT
- Paramètres généraux

### Transactions

Les administrateurs peuvent voir les transactions entrantes et sortantes pour le portefeuille on-chain connecté à ce magasin spécifique dans la vue des transactions. Chaque transaction a une distinction entre reçu et envoyé. Les transactions reçues seront en vert et les transactions sortantes seront en rouge. Dans la vue des transactions de BTCPay Server, les administrateurs verront également un ensemble d'étiquettes standard.

| Type de Transaction | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| App                 | Le paiement a été reçu via une facture créée par une application |
| invoice             | Le paiement a été reçu via une facture                           |
| payjoin             | Non payé, le minuteur de la facture n'a pas encore expiré        |
| payjoin-exposed     | UTXO a été exposé via une proposition de payjoin de facture      |
| payment-request     | Le paiement a été reçu via une demande de paiement               |
| payout              | Le paiement a été envoyé via un paiement ou un remboursement     |

### Comment envoyer

La fonction d'envoi de BTCPay Server permet d'envoyer des transactions depuis votre portefeuille on-chain BTCPay Server. BTCPay Server permet plusieurs façons de signer vos transactions pour dépenser des fonds. Une transaction peut être signée avec ;

- Portefeuille matériel
- Portefeuilles prenant en charge PSBT
- Clé privée HD ou graines de récupération.
- Portefeuille chaud

#### Portefeuille matériel

BTCPay Server intègre un support de portefeuille matériel vous permettant d'utiliser votre portefeuille matériel avec BTCPay Vault sans divulguer d'informations à des applications ou des serveurs tiers. L'intégration de portefeuille matériel dans BTCPay Server vous permet d'importer votre portefeuille matériel et de dépenser les fonds entrants avec une simple confirmation sur votre appareil. Vos clés privées ne quittent jamais l'appareil, et tous les fonds sont validés contre votre nœud complet, donc il n'y a pas de fuite de données.

#### Signature avec un portefeuille prenant en charge PSBT

PSBT (Partially Signed Bitcoin transactions) est un format d'échange pour les transactions Bitcoin qui doivent encore être entièrement signées. PSBT est pris en charge dans BTCPay Server et peut être signé avec des portefeuilles matériels et logiciels compatibles.

La construction d'une transaction Bitcoin entièrement signée passe par les étapes suivantes :

- Un PSBT est construit avec des entrées et des sorties spécifiques mais sans signatures
- Le PSBT exporté peut être importé par un portefeuille prenant en charge ce format
- Les données de la transaction peuvent être inspectées et signées en utilisant le portefeuille
- Le fichier PSBT signé est exporté du portefeuille et importé avec BTCPay Server
- BTCPay Server produit la transaction Bitcoin finale
- Vous vérifiez le résultat et le diffusez sur le réseau

#### Signature avec une clé privée HD ou une graine mnémonique

Si vous avez créé un portefeuille auparavant en utilisant BTCPay Server, vous pouvez dépenser les fonds en entrant votre clé privée dans un champ approprié. Définissez un "AccountKeyPath" approprié dans les paramètres du portefeuille ; sinon, vous ne pouvez pas dépenser.

#### Signature avec un portefeuille chaud

Si vous avez créé un nouveau portefeuille lors de la configuration de votre magasin et l'avez activé en tant que portefeuille chaud, il utilisera automatiquement la graine stockée sur un serveur pour signer.

### RBF (Replace-By-Fee)

Replace-By-Fee (RBF) est une fonctionnalité du protocole Bitcoin qui vous permet de remplacer une transaction précédemment diffusée (tant qu'elle n'est pas confirmée). Cela permet de randomiser l'empreinte de transaction de votre portefeuille ou de la remplacer par un taux de frais plus élevé pour déplacer la transaction plus haut dans la file d'attente de priorité de confirmation (minage). Cela remplacera effectivement la transaction originale car le taux de frais plus élevé sera priorisé, et une fois confirmé, invalidera l'originale (pas de double dépense).
Appuyez sur le bouton "Paramètres avancés" pour voir les options RBF ;

![image](assets/en/16.webp)

- Randomiser pour plus de confidentialité, permet à la transaction d'être remplacée automatiquement pour la randomisation de l'empreinte de transaction.
- Oui, Marquer la transaction pour RBF et être remplacée explicitement (Non remplacée par défaut, seulement par saisie)
- Non, Ne pas permettre que la transaction soit remplacée.

### Sélection de pièces

La sélection de pièces est une fonctionnalité avancée améliorant la confidentialité qui vous permet de sélectionner les pièces que vous souhaitez dépenser lors de la création d'une transaction. Par exemple, payer avec des pièces fraîchement issues d'un mixage de conjoin.

La sélection de pièces fonctionne de manière native avec la fonctionnalité d'étiquettes de portefeuille. Cela vous permet d'étiqueter les fonds entrants pour une gestion et une dépense des UTXO plus fluides.

BTCPay Server prend également en charge le BIP-329 pour la gestion des étiquettes. Le BIP-329 permet d'appliquer des étiquettes sur ; si vous transférez depuis un portefeuille prenant en charge ce BIP particulier et définissez des étiquettes, BTCPay Server les reconnaîtra et les importera. Lors de la migration de serveurs, ces informations peuvent également être exportées et importées dans le nouvel environnement.

### Comment recevoir

Lorsque vous cliquez sur le bouton de réception dans BTCPay Server, il génère une adresse inutilisée qui peut être utilisée pour recevoir des paiements. Les administrateurs peuvent également générer une nouvelle adresse en générant une nouvelle "Facture".

BTCPay Server demandera toujours de générer l'adresse BTC disponible suivante pour éviter la réutilisation d'adresse. Après avoir cliqué sur "Générer l'adresse BTC disponible suivante", BTCPay Server a généré une nouvelle adresse et un QR. Il vous permet également de définir directement une étiquette pour l'adresse pour une meilleure gestion de vos adresses.

![image](assets/en/17.webp)

![image](assets/en/18.webp)

#### Re-scan

La fonctionnalité Re-scan repose sur "Scantxoutset" de Bitcoin Core 0.17.0 pour scanner l'état actuel de la blockchain (appelé ensemble UTXO) à la recherche de pièces appartenant au schéma de dérivation configuré. Le re-scan de portefeuille résout deux problèmes rencontrés par les utilisateurs de BTCPay Server.

1. Problème de limite de gap - La plupart des portefeuilles tiers sont des portefeuilles légers qui partagent un nœud entre de nombreux utilisateurs. Les portefeuilles dépendant de nœuds légers et complets limitent le nombre (typiquement 20) d'adresses sans solde qu'ils suivent sur la blockchain pour éviter les problèmes de performance. BTCPay Server génère une nouvelle adresse pour chaque facture. Dans cet esprit, après que BTCPay Server ait généré 20 factures impayées consécutives, le portefeuille externe cesse de récupérer les transactions, supposant qu'aucune nouvelle transaction n'a eu lieu. Votre portefeuille externe ne les affichera pas une fois les factures payées sur le 21e, 22e, etc. D'autre part, en interne, le portefeuille BTCPay Server suit toute adresse qu'il génère avec une limite de gap bien plus grande. Il ne dépend pas d'un tiers et peut toujours afficher un solde correct.
2. La solution de la limite de l'écart - Si votre [portefeuille externe/existant](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-wallet) permet la configuration de la limite de l'écart, la solution facile est d'augmenter cette limite. Cependant, la majorité des portefeuilles ne permettent pas cela. Les seuls portefeuilles qui permettent la configuration de la limite de l'écart que nous connaissons sont Electrum, Wasabi et Sparrow Wallet. Malheureusement, vous risquez de rencontrer un problème avec de nombreux autres portefeuilles. Pour une meilleure expérience utilisateur et confidentialité, envisagez d'abandonner les portefeuilles externes et d'utiliser le portefeuille interne de BTCPay Server.

#### BTCPay Server utilise “mempoolfullrbf=1”

BTCPay Server utilise “mempoolfullrbf=1” ; nous avons ajouté cela par défaut à votre configuration BTCPay Server. Cependant, nous l'avons également rendu désactivable par vous-même. Sans “mempoolfullrbf=1”, si un client effectue un double paiement avec une transaction ne signalant pas RBF, le commerçant ne le saurait qu'après confirmation.

Un administrateur peut vouloir se désabonner de ce paramètre. Avec la chaîne suivante, vous pouvez changer le paramètre par défaut.

```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCLUDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```

### Paramètres du portefeuille BTCPay Server

Les paramètres du portefeuille au sein de BTCPay Server offrent un aperçu clair et rapide des paramètres généraux de votre portefeuille. Tous ces paramètres sont préremplis si le portefeuille a été créé avec BTCPay Server.

![image](assets/en/19.webp)

Les paramètres du portefeuille au sein de BTCPay Server offrent un aperçu clair et rapide des paramètres généraux de votre portefeuille. Tous ces paramètres sont préremplis si le portefeuille a été créé avec BTCPay Server. Les paramètres du portefeuille de BTCPay Server commencent par le statut du portefeuille. Est-ce un portefeuille en lecture seule ou un portefeuille actif ? Selon le type de portefeuille, les actions peuvent varier de la rescanisation du portefeuille pour les transactions manquantes, l'élagage des anciennes transactions de l'historique, l'enregistrement du portefeuille pour les liens de paiement, ou le remplacement et la suppression du portefeuille actuel attaché au magasin. Dans les paramètres du portefeuille de BTCPay Server, les administrateurs peuvent définir une Étiquette pour le portefeuille pour une meilleure gestion du portefeuille. Ici, l'Administrateur pourra également voir le Schéma de Dérivation, la clé de compte (xpub), l'Empreinte digitale et le Chemin de clé. Les paiements dans les paramètres du portefeuille n'ont que 2 paramètres principaux. Le paiement est invalide si la transaction échoue à se confirmer dans (minutes définies) après l'expiration de la facture. Considérer la facture comme confirmée lorsque la transaction de paiement a X nombre de confirmations. Les administrateurs peuvent également définir un bascule pour montrer les frais recommandés lors des paiements ou définir une cible de confirmation manuelle en nombre de blocs.

![image](assets/en/20.webp)

**!Note!**

Si vous suivez ce cours par vous-même, créer ce compte serait quelque chose que vous pourriez faire sur un hôte tiers, donc encore une fois nous mentionnons de ne jamais utiliser ces environnements comme environnements de production, mais plutôt uniquement à des fins de formation.

### Exemple

#### Configurer un portefeuille Bitcoin dans BTCPay Server

BTCPay Server permet deux manières de configurer un portefeuille. Une manière est d'importer un portefeuille Bitcoin déjà existant. L'importation peut être réalisée en connectant un portefeuille matériel, en important un fichier de portefeuille, en entrant une clé publique étendue, en scannant le code QR d'un portefeuille, ou la moins favorable, en entrant manuellement une graine de récupération de portefeuille précédemment créée. Dans BTCPay Server, il est également possible de créer un nouveau portefeuille. Il y a deux manières possibles de configurer BTCPay Server lors de la génération d'un nouveau portefeuille.
L'option de portefeuille chaud (hot wallet) dans BTCPay Server permet des fonctionnalités comme 'Payjoin' ou 'Liquid'. Cependant, il y a un inconvénient : la graine de récupération générée pour ce portefeuille sera stockée sur le serveur, où toute personne ayant le contrôle Admin pourrait récupérer cette graine de récupération. Comme votre clé privée est dérivée de votre graine de récupération, un acteur malveillant pourrait accéder à vos fonds actuels et futurs !

Pour atténuer un tel risque dans BTCPay Server, un Admin peut régler dans Paramètres du Serveur > Politiques > "Permettre aux non-admins de créer des portefeuilles chauds pour leurs boutiques" sur non, comme c'est le cas par défaut. Pour renforcer la sécurité de ces portefeuilles chauds, l'administrateur du serveur devrait activer l'authentification 2FA sur les comptes autorisés à avoir des portefeuilles chauds. Stocker des clés privées sur un serveur public est dangereux et comporte des risques. Certains sont similaires aux risques du Réseau Lightning (voir le chapitre suivant pour les risques du Réseau Lightning).

La deuxième option que BTCPay Server offre pour générer un nouveau portefeuille est de créer un portefeuille en mode observation seulement (Watch-Only wallet). BTCPay Server générera vos clés privées une seule fois. Après que l'utilisateur confirme avoir noté sa Phrase de Graine (Seed Phrase), BTCPay Server effacera les clés privées du serveur. En conséquence, votre boutique dispose maintenant d'un portefeuille en mode observation seulement connecté à celle-ci. Pour dépenser les fonds reçus sur votre portefeuille en mode observation seulement, voir le chapitre Comment Envoyer, soit en utilisant BTCPay Server Vault, PSBT (transaction bitcoin partiellement signée), ou, le moins recommandé, en fournissant manuellement votre phrase de graine.

Vous avez créé une nouvelle 'Boutique' dans la dernière partie. L'assistant d'installation continuera en demandant de "Configurer un portefeuille" ou "Configurer un nœud Lightning". Dans cet exemple, vous suivrez le processus de l'assistant "Configurer un portefeuille" (1).

![image](assets/fr/21.webp)

Après avoir cliqué sur "Configurer un portefeuille", l'assistant continuera en demandant comment vous souhaitez continuer ; BTCPay Server offre maintenant l'option de connecter un portefeuille Bitcoin existant à votre nouvelle boutique. Si vous n'avez pas de portefeuille, BTCPay Server propose d'en créer un nouveau. Cet exemple suivra les étapes pour "créer un nouveau portefeuille" (2). Suivez les étapes pour apprendre comment "Connecter un portefeuille existant" (1).

![image](assets/fr/22.webp)

**!Note!**

Si vous suivez ce cours dans une salle de classe, l'exemple actuel et la graine que nous avons générée sont uniquement à des fins éducatives. Il ne devrait jamais y avoir de montant substantiel autre que celui requis tout au long des exercices sur ces adresses.

(1) Continuez l'assistant "Nouveau portefeuille" en cliquant sur le bouton "Créer un nouveau portefeuille".

![image](assets/fr/23.webp)

(2) Après avoir cliqué sur “Créer un nouveau portefeuille”, la fenêtre suivante de l'assistant donnera les options “Portefeuille chaud” et “Portefeuille en mode observation seulement”. Si vous suivez avec un instructeur, votre environnement est une Démo partagée, et vous ne pouvez créer qu'un portefeuille en mode observation seulement. Remarquez la différence entre les deux images ci-dessous. Comme vous êtes dans l'environnement Démo en suivant avec l'instructeur, créez un "Portefeuille en mode observation seulement" et continuez avec l'assistant "Nouveau Portefeuille".

![image](assets/fr/24.webp)

![image](assets/fr/25.webp)

(3) En continuant l'assistant du nouveau portefeuille, vous êtes maintenant dans la section Créer un portefeuille BTC en mode observation seulement. Ici, nous pouvons définir le type d'adresse du portefeuille "Type d'adresse" BTCPay Server vous permet de choisir votre type d'adresse préféré ; au moment de la rédaction de ce cours, il est toujours recommandé d'utiliser des adresses bech32. Apprenez-en plus en détail sur les adresses dans le premier chapitre de cette partie.

- Segwit (bech32)
- Les adresses Native SegWit commencent par `bc1q`. - Exemple : `bc1qXXXXXXXXXXXXXXXXXXXXXX`
- Legacy
  - Les adresses Legacy commencent par le chiffre `1`.
  - Exemple : `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (Pour utilisateurs avancés)
  - Les adresses Taproot commencent par `bc1p`.
  - Exemple : `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- Segwit enveloppé
  - Les adresses Segwit enveloppées commencent par `3`.
  - Exemple : `37BBXXXXXXXXXXXXXXX`

Choisissez segwit (recommandé) comme type d'adresse de portefeuille préféré.

![image](assets/en/26.webp)

(4) Lors de la configuration du paramètre pour le Wallet, BTCPay Server permet aux utilisateurs de définir une phrase secrète optionnelle via BIP39, assurez-vous de confirmer votre mot de passe.

![image](assets/en/27.webp)

(5) Après avoir défini le type d'adresse du Wallet et éventuellement configuré certaines options avancées, cliquez sur Créer, et BTCPay Server générera votre nouveau Wallet. Notez que ceci est la dernière étape avant de générer votre phrase de récupération. Assurez-vous de ne faire cela que dans un environnement où personne ne pourrait voler la phrase de récupération en regardant votre écran.

![image](assets/en/28.webp)

(6) Dans l'écran suivant de l'assistant, BTCPay Server vous montre la phrase de récupération pour votre Wallet nouvellement généré ; ce sont les clés pour récupérer votre Wallet et signer des transactions. BTCPay Server génère une phrase de récupération de 12 mots. Ces mots seront effacés du serveur après cet écran de configuration. Ce Wallet est spécifiquement un portefeuille en mode observation uniquement. Il est conseillé de ne pas stocker cette phrase de récupération numériquement ou par image photographique. Les utilisateurs ne peuvent aller plus loin dans l'assistant qu'après avoir reconnu activement qu'ils ont bien noté leur phrase de récupération.

![image](assets/en/29.webp)

(7) Après avoir cliqué sur Terminé et sécurisé la nouvelle phrase de récupération Bitcoin générée, BTCPay Server mettra à jour votre magasin avec le nouveau Wallet attaché et sera prêt à recevoir des paiements. Dans l'interface utilisateur, dans le menu de navigation gauche, remarquez comment Bitcoin est maintenant mis en évidence et activé sous Wallet.

![image](assets/en/30.webp)

### Exemple : Noter une phrase de récupération

C'est un moment très particulier et sécurisé pour utiliser Bitcoin. Comme mentionné précédemment, seulement vous devriez avoir accès ou connaître votre phrase de récupération. Alors que vous suivez un instructeur et une classe, la phrase générée ne devrait être utilisée que dans ce cours. Trop de facteurs, des regards indiscrets de camarades de classe, des systèmes non sécurisés, et bien d'autres rendent ces clés uniquement éducatives et non fiables. Cependant, les clés générées devraient toujours être stockées pour des exemples de cours.

La première méthode que nous utiliserons dans la situation actuelle, aussi la moins sécurisée, est de noter la phrase de récupération dans le bon ordre. Une carte de phrase de récupération se trouve dans le matériel de cours fourni à l'étudiant ou trouvé sur GitHub de BTCPay Server. Nous utiliserons cette carte pour noter les mots générés à l'étape précédente. Assurez-vous de les écrire dans le bon ordre. Après les avoir écrits, vérifiez-les par rapport à ce qui a été donné par le logiciel pour vous assurer que vous les avez écrits dans le bon ordre. Une fois que vous les avez écrits, cliquez sur la case indiquant que vous avez correctement noté votre phrase de récupération.

### Exemple : Stocker une phrase de récupération sur un portefeuille matériel

Dans ce cours, nous abordons le stockage d'une phrase de récupération sur un portefeuille matériel. Suivre ce cours avec un instructeur n'inclut pas toujours un tel dispositif. Dans le cours, les matériaux de guide ont écrit une liste de portefeuilles matériels fournis qui conviendraient à cet exercice.
Nous utiliserons le coffre-fort BTCPay Server et un portefeuille matériel Blockstream Jade dans cet exemple.
Vous pouvez également suivre en vidéo pour vous référer à la connexion d'un portefeuille matériel.
![BTCPay Server - Comment connecter votre portefeuille matériel avec BTCPay Vault.](https://youtu.be/s4qbGxef43A)

Téléchargez BTCPay Server Vault : https://github.com/btcpayserver/BTCPayServer.Vault/releases

Assurez-vous de télécharger les fichiers corrects pour votre système. Les utilisateurs Windows devraient télécharger le paquet [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), les utilisateurs Mac téléchargent [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), et les utilisateurs Linux devraient télécharger [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

Après avoir installé BTCPay Server Vault, démarrez le logiciel en cliquant sur l'icône sur votre bureau. Lorsque BTCPay Server Vault est correctement installé et lancé pour la première fois, il demandera la permission d'être utilisé avec des applications Web. Il demandera d'accorder l'accès au BTCPay Server spécifique avec lequel vous travaillez. Acceptez ces conditions. BTCPay Server Vault recherchera maintenant le dispositif matériel. Une fois le dispositif trouvé, BTCPay Server reconnaîtra que Vault est en fonctionnement et a récupéré votre dispositif.

**!Note!**

Ne donnez vos clés SSH ou compte d'administrateur de serveur à personne d'autre qu'aux administrateurs lorsque vous utilisez un portefeuille chaud. Toute personne ayant accès à ces comptes aura accès aux fonds dans le portefeuille chaud.

### Résumé des Compétences

Dans cette section, vous avez appris ce qui suit :

- La vue des transactions du portefeuille Bitcoin et ses différentes catégorisations.
- Les différentes options disponibles lors de l'envoi à partir d'un portefeuille Bitcoin, des portefeuilles matériels aux portefeuilles chauds.
- Le problème de limite de gap rencontré lors de l'utilisation de la plupart des portefeuilles, et comment le corriger.
- Comment générer un nouveau portefeuille Bitcoin au sein de BTCPay Server, y compris le stockage des clés dans un portefeuille matériel et la sauvegarde de la phrase de récupération.

Dans cet objectif, vous avez appris comment générer un nouveau portefeuille Bitcoin au sein de BTCPay Server. Nous n'avons pas encore abordé comment sécuriser ou utiliser ces clés. Dans un aperçu rapide de cet objectif, vous avez appris comment configurer le premier magasin. Vous avez appris comment générer une phrase de récupération Bitcoin Seed.

### Évaluation Pratique des Connaissances

Décrivez une méthode pour générer des clés et un schéma pour les sécuriser, ainsi que les compromis/risques du schéma de sécurité.

## Portefeuille Lightning BTCPay Server

<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>

Lorsqu'un administrateur de serveur provisionne une nouvelle instance de BTCPay Server, il peut configurer une implémentation du réseau Lightning, LND, Core Lightning, ou Eclair ; voir la partie Configurer BTCPay Server pour des instructions d'installation plus détaillées.
Si vous suivez le cours en classe, la connexion d'un nœud Lightning à votre serveur BTCPay se fait via un nœud personnalisé. Un utilisateur qui n'est pas administrateur du serveur sur BTCPay Server ne pourra pas utiliser le nœud Lightning interne par défaut. Cela est fait pour protéger le propriétaire du serveur de la perte de ses fonds. Les administrateurs de serveur peuvent installer un Plugin pour donner accès à leur nœud Lightning via LNBank ; cela est hors du champ de ce livre ; pour en savoir plus sur LNBank, consultez la page officielle du plugin.

### Connecter le nœud interne (administrateur du serveur)

L'administrateur du serveur peut utiliser le nœud Lightning interne de BTCPay Server. Indépendamment de l'implémentation de Lightning, la connexion au nœud Lightning interne est la même.

Allez dans un magasin configuré précédemment, et cliquez sur le portefeuille "Lightning" dans le menu de gauche. BTCPay Server offre deux possibilités de configuration, en utilisant le nœud interne (seulement par défaut pour l'admin du serveur) ou un nœud personnalisé (connexion externe). Les administrateurs de serveur peuvent cliquer sur l'option "Utiliser le nœud interne". Aucune configuration supplémentaire n'est requise. Cliquez sur le bouton "enregistrer" et remarquez la notification indiquant, "Nœud Lightning BTC mis à jour". Le magasin a maintenant réussi à obtenir les capacités du réseau Lightning.

### Connecter le nœud externe (utilisateur du serveur/propriétaire du magasin)

Comme les propriétaires de magasin ne sont par défaut pas autorisés à utiliser le nœud Lightning de l'administrateur du serveur. La connexion doit être faite à un nœud externe, soit un nœud possédé par le propriétaire du magasin avant la configuration d'un serveur BTCPay, un plugin LNBank s'il est rendu disponible par l'administrateur du serveur, ou une solution de custodian comme Alby.

Allez dans un magasin configuré précédemment, et cliquez sur "Lightning" sous portefeuilles dans le menu de gauche. Comme les propriétaires de magasin ne sont pas autorisés à utiliser le nœud interne par défaut, cette option est grisée. Utiliser un nœud personnalisé est la seule option par défaut disponible pour les propriétaires de magasin.

BTCPay Server a besoin d'informations de connexion ; la solution préalablement mise en place (ou la solution de custodian) fournira ces informations spécifiques à une implémentation de Lightning. Dans BTCPay Server, les propriétaires de magasin peuvent utiliser les connexions suivantes ;

- C-lightning via TCP ou connexion de socket de domaine Unix.
- Lightning Charge via HTTPS
- Eclair via HTTPS
- LND via le proxy REST
- LNDhub via l'API REST

![image](assets/en/31.webp)

Cliquez sur "tester la connexion" pour vous assurer que vous avez correctement saisi les détails de la connexion. Après la confirmation que la connexion est bonne, cliquez sur enregistrer, et BTCPay Server montre que le magasin est mis à jour avec un nœud Lightning.

### Gestion du nœud Lightning interne LND (Administrateur du serveur)

Après avoir connecté le nœud Lightning interne, les administrateurs de serveur remarqueront de nouvelles tuiles sur le tableau de bord spécifiquement pour les informations Lightning.

- Solde Lightning
- BTC dans les canaux
  - BTC ouvrant des canaux
  - Solde local BTC
  - Solde distant BTC
  - BTC fermant des canaux
- BTC On-chain
  - BTC confirmé
  - BTC non confirmé
  - BTC réservé
- Services Lightning
  - Ride the Lightning (RTL).

En cliquant soit sur le logo Ride the Lightning dans la tuile "Services Lightning" soit sur "Lightning" sous portefeuilles dans le menu de gauche, les administrateurs de serveur peuvent accéder à RTL pour la gestion du nœud Lightning.

**Note !**

Si la connexion au nœud Lightning interne échoue - Confirmez :

1. Que le nœud Bitcoin on-chain est entièrement synchronisé
2. Que le nœud Lightning interne est "Activé" sous "Lightning" > "Paramètres" > "Paramètres Lightning BTC"
   Si vous ne parvenez pas à vous connecter à votre nœud Lightning, essayez de redémarrer votre serveur, ou consultez la documentation officielle de BTCPay Server pour plus de détails ; https://docs.btcpayserver.org/Troubleshooting/ . Vous ne pouvez pas accepter de paiements Lightning dans votre magasin tant que votre nœud Lightning n'apparaît pas comme "En ligne". Essayez de tester votre connexion Lightning en cliquant sur le lien "Informations sur le nœud public".

### Portefeuille Lightning

Dans l'option Portefeuille Lightning située dans la barre de menu de gauche, les administrateurs de serveur trouveront un accès facile à RTL, leurs Informations sur le nœud public, et les paramètres Lightning spécifiques à leur magasin BTCPay Server.

#### Informations sur le nœud interne

Les administrateurs de serveur peuvent cliquer sur les informations du nœud interne et apercevoir le statut de leur serveur (En ligne/ Hors ligne) et la chaîne de connexion pour Clearnet ou Tor.

![image](assets/en/32.webp)

#### Changer de connexion

Si le propriétaire du magasin décide d'utiliser des modifications dans les Paramètres Lightning - Changer de connexion.
À côté des informations du Nœud public, les propriétaires de magasin peuvent trouver cette option. Cela ramènera la configuration initiale pour la connexion au nœud Lightning externe, remplissez les nouvelles informations du nœud Lightning, cliquez sur enregistrer et mettez à jour le magasin avec les nouvelles informations du nœud.

![image](assets/en/33.webp)

#### Services

Si l'administrateur du serveur décide d'installer plusieurs services pour l'implémentation Lightning, ils seront listés ici. Avec une implémentation LND standard, les administrateurs auront Ride The Lightning (RTL) comme outil standard pour la gestion du nœud.

#### Paramètres du portefeuille BTC Lightning

Après avoir ajouté le nœud Lightning au magasin dans une étape précédente, dans les paramètres du portefeuille Lightning, les propriétaires de magasin peuvent toujours choisir de le désactiver pour leur magasin en utilisant le Toggle en haut des paramètres Lightning.

![image](assets/en/34.webp)

#### Options de paiement Lightning

Les propriétaires de magasin peuvent définir des paramètres pour améliorer l'expérience Lightning pour leurs clients.

- Afficher les montants des paiements Lightning en Satoshis.
- Ajouter des indices de saut pour les canaux privés à la facture Lightning.
- Unifier les URL/QR codes de paiement on-chain et Lightning lors du paiement.
- Définir un modèle de description pour les factures Lightning.

#### LNURL

Les propriétaires de magasin peuvent choisir d'utiliser ou non LNURL. Une URL du réseau Lightning, ou LNURL, est une norme proposée pour les interactions entre le payeur et le bénéficiaire Lightning. En bref, une LNURL est une URL encodée en bech32 préfixée par lnurl. Le portefeuille Lightning est censé décoder l'URL, contacter l'URL, et attendre un objet JSON avec des instructions supplémentaires, notamment une balise définissant le comportement de la lnurl.

- Activer LNURL
- Mode LNURL Classique
  - Pour la compatibilité des portefeuilles, Bech32 encodé (classique) vs URL en texte clair (à venir)
- Permettre au bénéficiaire de passer un commentaire.

### Exemple 1

#### Se connecter à Lightning avec le nœud interne (Administrateur)

Cette option n'est disponible que si vous êtes l'Administrateur de cette instance ou si l'Administrateur a modifié les paramètres par défaut permettant aux utilisateurs d'utiliser le nœud lightning interne.

En tant qu'administrateur, cliquez sur Portefeuille Lightning dans la barre de menu de gauche. BTCPay Server demandera d'utiliser l'une des deux options pour connecter un Nœud Lightning, un nœud interne ou un nœud externe personnalisé. Cliquez sur Utiliser le nœud interne et cliquez sur enregistrer.

#### Gérer votre nœud Lightning (RTL)

Après s'être connecté au nœud lightning interne, BTCPay Server se mettra à jour et affichera une notification "Nœud Lightning BTC mis à jour", confirmant que vous avez maintenant connecté Lightning à votre magasin.

Gérer le nœud lightning est une tâche pour l'Administrateur du serveur. Cela implique :

- Gérer les transactions
- Gérer la liquidité
  - Liquidité entrante
  - Liquidité sortante
- Gérer les pairs et les canaux
  - Pairs connectés
  - Frais de canal
  - Statut du canal
- Faire des sauvegardes fréquentes des états des canaux.
- Vérifier les rapports de routage
- Alternativement, utiliser des services comme Loop.

Toute la gestion des nœuds Lightning est standardisée avec RTL (en supposant que vous utilisez une implémentation LND). Les administrateurs peuvent cliquer sur leur Portefeuille Lightning dans BTCPay Server et trouver un bouton pour ouvrir RTL. Le tableau de bord principal de BTCPay Server est maintenant mis à jour avec les tuiles du Réseau Lightning, incluant un accès rapide à RTL.

### Exemple 2

#### Se connecter à Lightning avec Alby

Lors de la connexion avec un gardien comme Alby, les propriétaires de magasin doivent d'abord créer un compte, visitez : https://getalby.com/

![image](assets/fr/35.webp)

Après avoir créé le compte Alby, allez à votre magasin BTCPay Server.

Étape 1 : Cliquez sur 'Configurer un nœud Lightning' sur le tableau de bord ou sur 'Lightning' sous portefeuilles.

![image](assets/fr/36.webp)

Étape 2 : Insérez vos identifiants de connexion de portefeuille fournis par Alby. Sur le tableau de bord d'Alby, cliquez sur Portefeuille. Ici, vous trouverez "Identifiants de connexion au portefeuille". Copiez ces identifiants. Collez les identifiants d'Alby dans le champ de configuration de connexion dans BTCPay Server.

![image](assets/fr/37.webp)

Étape 3 : Après avoir fourni à BTCPay Server les détails de la connexion, cliquez sur le bouton "Tester la connexion" pour vous assurer que la connexion fonctionne correctement. Remarquez le message "Connexion au nœud Lightning réussie" en haut de votre écran. Cela confirme que tout fonctionne dans l'ordre.

![image](assets/fr/38.webp)

Étape 4 : Cliquez sur sauvegarder, et votre magasin est maintenant connecté à un nœud Lightning par Alby.

![image](assets/fr/39.webp)

**!Note!**

Ne faites jamais confiance à une solution Lightning de gardien pour plus de valeur que vous êtes prêt à perdre.

### Résumé des compétences

Dans cette section, vous avez appris :

- Comment connecter un nœud Lightning interne ou externe
- Le contenu et la fonction des différentes tuiles liées à Lightning dans le tableau de bord
- Comment configurer un portefeuille Lightning en utilisant Voltage Surge ou Alby

### Évaluation des connaissances Examen pratique

Décrivez certaines des différentes options pour connecter un portefeuille Lightning à votre magasin.

# Interface du serveur BTCPay

<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>

## Vue d'ensemble du tableau de bord

<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>

BTCPay Server est un package logiciel modulaire. Cependant, il existe des normes que chaque BTCPay Server aura et avec lesquelles l'administrateur/les utilisateurs interagiront. En commençant par le tableau de bord. Le principal point d'entrée de chaque BTCPay Server après la connexion. Le tableau de bord donne un aperçu de la performance de votre magasin, du solde actuel du portefeuille, et des dernières transactions au cours des 7 derniers jours. Comme il s'agit d'une vue modulaire, les plugins peuvent utiliser cette vue à leur avantage et créer leurs tuiles sur le tableau de bord. Pour ce manuel de cours, nous ne parlerons que des plugins/applications standard et de leurs vues respectives à travers BTCPay Server.

### Tuiles du tableau de bord

Dans la vue principale du tableau de bord BTCPay Server, il y a quelques tuiles standard disponibles. Ces tuiles sont destinées au propriétaire du magasin ou à l'administrateur pour gérer rapidement son magasin dans une vue d'ensemble.

- Solde du portefeuille
- Activité transactionnelle
- Solde Lightning (si Lightning est activé sur le magasin)
- Services Lightning (si Lightning est activé sur le magasin)
- Transactions récentes.
- Factures récentes
- Crowdfunds actifs
- Performance du magasin / articles les plus vendus.

### Solde du portefeuille

La tuile Solde du Portefeuille offre un aperçu rapide des fonds et de la performance de votre portefeuille. Elle peut être affichée en BTC ou en devise Fiat dans un graphique hebdomadaire, mensuel ou annuel.
![image](assets/en/40.webp)

### Activité de transaction

À côté de la tuile Solde du Portefeuille, BTCPay Server montre un aperçu rapide des Paiements en attente, le nombre de Transactions dans les 7 derniers jours, et si votre magasin a émis des remboursements. Cliquer sur le bouton Gérer vous amène à la gestion des paiements en attente (en savoir plus sur les paiements dans BTCPay Server - Chapitre des Paiements).

![image](assets/en/41.webp)

### Solde Lightning

Ceci n'est visible que lorsque Lightning est activé.

Lorsque l'Administrateur a autorisé l'accès au réseau Lightning, le tableau de bord de BTCPay Server affiche maintenant une nouvelle tuile avec les informations de votre nœud Lightning. Combien de BTC se trouve dans les canaux, comment cela est équilibré localement ou à distance (liquidité entrante ou sortante), si les canaux sont en train de se fermer ou de s'ouvrir, et combien de bitcoin est détenu on-chain sur le nœud lightning.

![image](assets/en/42.webp)

### Services Lightning

Ceci n'est visible que lorsque lightning est actif.

À côté de voir votre solde Lightning sur le tableau de bord de BTCPay Server, les administrateurs verront également la tuile pour les Services Lightning. Ici, les administrateurs peuvent trouver des boutons rapides pour les outils qu'ils utilisent pour gérer leur nœud Lightning ; par exemple, Ride the Lightning est l'un des outils standards avec BTCPay Server pour la gestion des nœuds Lightning.

![image](assets/en/43.webp)

### Transactions Récentes

La tuile des transactions récentes montrera les transactions les plus récentes de votre magasin. En un clic, l'Administrateur de l'instance BTCPay Server peut maintenant voir la dernière transaction et voir si une attention particulière est nécessaire.

![image](assets/en/44.webp)

### Factures récentes

La tuile des factures récentes montre les 6 dernières factures générées par votre BTCPay Server, incluant le Statut et le montant de la facture. La tuile inclut également un bouton "Voir tout" pour accéder facilement à l'aperçu complet des factures.

![image](assets/en/45.webp)

### Point De Vente et Crowdfunds

Comme BTCPay Server fournit un ensemble de plugins ou d'applications standards, Point De Vente et Crowdfund sont les deux principaux plugins de BTCPay Server. Avec chaque magasin et portefeuille, un utilisateur de BTCPay Server peut générer autant de Points De Vente ou de Crowdfunds qu'il le souhaite. Chacun créera une nouvelle tuile de tableau de bord montrant la performance des plugins.

![image](assets/en/46.webp)

Remarquez la légère différence entre une tuile Point de Vente et Crowdfund. L'Administrateur voit les articles les plus vendus dans la tuile Point de Vente. Dans la tuile Crowdfund, cela devient Top Perks. Les deux tuiles ont des boutons rapides pour gérer l'application respective et voir les factures récentes créées par les articles les plus vendus ou les top perks.

![image](assets/en/47.webp)

**!?Note!?**

Les graphiques de solde et les transactions récentes sont disponibles uniquement pour une méthode de paiement on-chain. Les informations sur les soldes et transactions du réseau Lightning sont à faire. À partir de la version 1.6.0 de BTCPay Server, les soldes basiques du réseau Lightning sont disponibles.

### Résumé des Compétences

Dans cette section, vous avez appris ce qui suit :

- La disposition principale des tuiles sur la page d'accueil est connue sous le nom de Tableau de bord.
- Une compréhension de base du contenu de chaque tuile.

### Révision de l'Évaluation des Connaissances

Listez autant de tuiles que possible de mémoire du Tableau de bord.

## BTCPay Server - Paramètres du magasin

<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>
Au sein du logiciel BTCPay Server, nous connaissons 2 types de paramètres. Les paramètres spécifiques au magasin BTCPay Server, le bouton de paramètres trouvé dans la barre de menu gauche sous le tableau de bord, et les paramètres BTCPay Server, trouvés au bas de la barre de menu juste au-dessus de Compte. Les paramètres spécifiques au serveur BTCPay Server ne peuvent être consultés que par les administrateurs du serveur.
Les paramètres du magasin comprennent de nombreux onglets pour catégoriser chaque ensemble de paramètres.

- Général
- Taux
- Apparence du paiement
- Jetons d'accès
- Utilisateurs
- Rôles
- Webhooks
- Processeurs de paiement
- Emails
- Formulaires

### Général

Dans l'onglet Paramètres Généraux, les propriétaires de magasin définissent leur image de marque et les paramètres par défaut de paiement. Lors de la configuration initiale du magasin, un nom de magasin a été donné ; cela sera reflété dans les paramètres généraux sous Nom du Magasin. Ici, le propriétaire du magasin peut également définir son site web pour correspondre à l'image de marque et un ID de Magasin pour que l'Administrateur puisse reconnaître dans la base de données.

#### Image de marque

Comme BTCPay Server est FOSS, un propriétaire de magasin peut personnaliser l'image de marque pour correspondre à son magasin. Définissez la couleur de la marque, stockez les logos de votre marque et ajoutez du CSS personnalisé pour les pages publiques/face aux clients (Factures, Demandes de paiement, Paiements Pull)

#### Paiement

Dans les paramètres de paiement, les propriétaires de magasin définissent la devise par défaut de leur magasin (soit en Bitcoin soit dans n'importe quelle devise fiat).

#### Permettre à quiconque de créer des factures

Ce paramètre est destiné aux développeurs ou aux constructeurs sur BTCPay Server. Avec ce paramètre activé pour votre magasin, il permet au monde extérieur de créer des factures sur votre instance BTCPay Server.

#### Ajouter des frais supplémentaires (frais de réseau) aux factures

Une fonctionnalité au sein de BTCPay pour protéger les commerçants des attaques de poussière ou des clients pour entraîner un coût élevé en frais plus tard lorsque le commerçant doit déplacer beaucoup de bitcoins à la fois. Par exemple, le client a créé une facture de 20$ et l'a payée partiellement, payant 1$ 20 fois jusqu'à ce que la facture soit entièrement payée. Le commerçant a maintenant une transaction plus importante, augmentant le coût de minage au cas où le commerçant décide de déplacer ces fonds plus tard. Par défaut, BTCPay applique un coût de réseau supplémentaire au montant total de la facture pour couvrir cette dépense pour le commerçant lorsque la facture est payée en plusieurs transactions. BTCPay offre plusieurs options pour personnaliser cette fonctionnalité de protection. Vous pouvez appliquer des frais de réseau :

- Seulement si le client effectue plus d'un paiement pour la facture (Dans l'exemple ci-dessus, si le client a créé une facture de 20\$ et payé 1\$, le montant total dû est maintenant de 19\$ + les frais de réseau. Les frais de réseau sont appliqués après le premier paiement)
- Sur chaque paiement (y compris le premier paiement, dans notre exemple, le total sera de 20\$ + frais de réseau dès le départ, même sur le premier paiement)
- Ne jamais ajouter de frais de réseau (désactive entièrement les frais de réseau)

Bien qu'il protège des transactions de poussière, cela peut également se refléter négativement sur les entreprises si cela n'est pas communiqué correctement. Les clients peuvent avoir des questions supplémentaires et penser que vous les surchargez.

#### La facture expire si le montant total n'a pas été payé après ?

Le minuteur de la facture est réglé par défaut sur 15 minutes. Le minuteur est un mécanisme de protection contre la volatilité puisqu'il verrouille le montant en Bitcoin selon les taux Bitcoin vers fiat. Si le client ne paie pas la facture dans le délai défini, la facture est considérée comme expirée. La facture est considérée comme "payée" dès que la transaction est visible sur la blockchain (0-confirmations) mais considérée comme "complète" lorsqu'elle atteint le nombre de confirmations défini par le commerçant (généralement, 1-6). Le minuteur est personnalisable par minutes.

#### Considérer la facture payée même si le montant payé est inférieur de X% à ce qui était attendu ?

Lorsqu'un client utilise un portefeuille d'échange pour payer directement une facture, l'échange prend une petite commission. Cela signifie qu'une telle facture n'est pas considérée comme entièrement réglée. La facture obtient le statut "payée partiellement". Vous pouvez définir le taux de pourcentage ici si un commerçant souhaite accepter les factures sous-payées.

### Tarifs

Dans BTCPay Server, lorsqu'une facture est générée, elle a toujours besoin du prix Bitcoin vers fiat le plus récent et le plus précis. Lors de la création d'un nouveau magasin dans BTCPay Server, les administrateurs sont invités à définir leur source de prix préférée ; après la configuration du magasin, les propriétaires de magasin peuvent toujours changer leur source de prix dans cet onglet.

#### Scripting de règle de tarif avancé

Principalement utilisé par les utilisateurs expérimentés. Si activé, les propriétaires de magasin peuvent créer des scripts autour du comportement des prix et comment facturer leurs clients.

#### Test

Un lieu de test rapide pour vos paires de devises préférées. Cela inclut également une fonctionnalité pour vérifier les paires de devises par défaut via une requête REST.

### Apparence du paiement

L'onglet Apparence du paiement commence avec les paramètres spécifiques aux factures et une méthode de paiement par défaut et permet d'activer des méthodes de paiement spécifiques lorsque les exigences définies sont satisfaites.

#### Paramètres de la facture

Méthodes de paiement par défaut. BTCPay Server dans une configuration standard propose trois options.

- BTC (sur chaîne)
- BTC (LNURL-pay)
- BTC (Hors chaîne & Lightning)

Nous pouvons définir des paramètres pour notre magasin, où un client n'interagira avec Lightning que si le prix est inférieur à un montant X et vice versa pour les transactions sur chaîne lorsque X est supérieur à Y, présenter toujours l'option de paiement sur chaîne.

![image](assets/en/48.webp)

#### Paiement

Depuis la sortie de BTCPay Server 1.7, une nouvelle interface de paiement, Checkout V2, comme elle est appelée, a été introduite. Depuis la version 1.9, elle a été standardisée, les administrateurs et les propriétaires de magasin peuvent toujours régler le paiement sur la version précédente. En utilisant le bascule "Utiliser le paiement classique", un propriétaire de magasin peut revenir à l'expérience de paiement précédente. BTCPay Server propose également un ensemble de présélections pour le commerce en ligne ou une expérience en magasin.

![image](assets/en/49.webp)

Lorsqu'un client interagit avec le magasin et génère une facture, il y a un temps d'expiration pour la facture. Par défaut, BTCPay Server fixe cela à 5 minutes, et l'Administrateur peut le régler à ce qu'il juge approprié. La page de paiement peut être personnalisée davantage en vérifiant les paramètres suivants :

- Célébrer le paiement en montrant des confettis
- Afficher l'en-tête du magasin (Nom et logo)
- Afficher le bouton "Payer dans le portefeuille"
- Unifier les URL/QR de paiements sur chaîne et hors chaîne
- Afficher les montants des paiements Lightning en Satoshis
- Détection automatique de la langue au paiement

![image](assets/en/50.webp)

Lorsque la détection automatique de la langue n'est pas configurée, BTCPay Server, par défaut, affichera l'anglais. Un propriétaire de magasin peut changer cette langue par défaut pour celle qu'il préfère.

![image](assets/en/51.webp)

Cliquez sur le menu déroulant et les propriétaires de magasin peuvent définir un titre HTML personnalisé à afficher sur la page de paiement.

![image](assets/en/52.webp)

Pour s'assurer que le client connaît sa méthode de paiement, un propriétaire de magasin peut explicitement configurer son paiement pour toujours exiger des utilisateurs de choisir leur méthode de paiement préférée. Lorsque la facture est payée, BTCPay Server permet au client de retourner à la boutique en ligne. Les propriétaires de magasin peuvent configurer cette redirection après le paiement du client automatiquement.

![image](assets/en/53.webp)

#### Reçu public

Dans les paramètres du reçu public, un propriétaire de magasin peut rendre les pages de reçu publiques et afficher la liste des paiements sur la page du reçu ainsi que le code QR du reçu pour que le client puisse y accéder facilement de manière numérique.

### Jetons d'Accès

Les jetons d'accès sont utilisés pour l'appariement à certaines intégrations de commerce électronique ou des intégrations personnalisées.

### Utilisateurs

Les utilisateurs du magasin sont ceux où le propriétaire du magasin peut gérer ses membres du personnel, leurs comptes et l'accès au magasin. Après que les membres du personnel aient créé leurs comptes, le propriétaire du magasin peut ajouter des utilisateurs spécifiques au magasin en tant qu'utilisateurs invités ou propriétaires. Pour définir davantage le rôle du membre du personnel, reportez-vous à la section suivante sur "Paramètres du magasin BTCPay Server - Rôles".

### Rôles

Un propriétaire de magasin pourrait ne pas trouver les rôles standard des utilisateurs suffisamment significatifs. Dans les paramètres des rôles personnalisés, un propriétaire de magasin peut définir les besoins exacts pour chaque rôle dans son entreprise.

(1) Pour créer un nouveau rôle, cliquez sur le bouton "+ Ajouter un rôle".

(2) Entrez un nom de rôle, par exemple, "Caissier".

(3) Configurez les permissions individuelles pour le rôle.

- Modifier vos magasins.
- Gérer les comptes d'échange liés à vos magasins.
  - Voir les comptes d'échange liés à vos magasins.
- Gérer vos paiements différés.
- Créer des paiements différés.
  - Créer des paiements différés non approuvés.
- Modifier les factures.
  - Voir les factures.
  - Créer une facture.
  - Créer des factures à partir des nœuds lightning associés à vos magasins.
- Voir vos magasins.
  - Voir les factures.
  - Voir vos demandes de paiement.
  - Modifier les webhooks des magasins.
- Modifier vos demandes de paiement.
  - Voir vos demandes de paiement.
- Utiliser les nœuds lightning associés à vos magasins.
  - Voir les factures lightning associées à vos magasins.
  - Créer des factures à partir des nœuds lightning associés à vos magasins.
- Déposer des fonds sur les comptes d'échange liés à vos magasins.
- Retirer des fonds des comptes d'échange vers votre magasin.
- Échanger des fonds sur les comptes d'échange de votre magasin.

Lorsque le rôle est créé, le nom est fixé et ne peut pas être changé après en mode édition.

### Webhooks

Dans BTCPay Server, il est assez facile de créer un nouveau "Webhook". Dans l'onglet Paramètres du magasin BTCPay Server - Webhooks, un propriétaire de magasin peut facilement créer un nouveau webhook en cliquant sur "+ Créer un Webhook". Les webhooks permettent à BTCPay Server d'envoyer des événements HTTP liés à votre magasin vers d'autres serveurs ou intégrations de commerce électronique.

Vous êtes maintenant dans la vue pour créer un Webhook. Assurez-vous de connaître votre URL de Payload et collez-la dans votre BTCPay Server. Tout en ayant collé l'URL de Payload, en dessous, cela montre le secret du webhook. Copiez le secret du webhook et fournissez-le sur le point de terminaison. Une fois tout configuré, vous pouvez basculer dans BTCPay Server en Redélivrance Automatique. Nous essaierons de redélivrer toute livraison échouée après 10 secondes, 1 minute, et jusqu'à 6 fois après 10 minutes. Vous pouvez basculer entre chaque événement ou spécifier les événements selon vos besoins. Assurez-vous d'activer le webhook et cliquez sur Ajouter le webhook pour le sauvegarder.

Les webhooks ne sont pas destinés à être compatibles avec l'API Bitpay. Il y a deux IPN distincts (en termes BitPay : "Notifications de Paiement Instantané") dans BTCPay Server.

- Webhook
- Notifications

Utilisez uniquement l'URL de Notification lorsque vous créez des factures via l'api Bitpay.

### Processeurs de Paiement

Les processeurs de paiement travaillent conjointement avec le concept de Payouts dans BTCPay Server. Un agrégateur de paiement permet de regrouper plusieurs transactions et de les envoyer en une seule fois. Avec les processeurs de paiement, un propriétaire de magasin peut automatiser les paiements groupés. BTCPay Server propose deux méthodes de paiements automatiques, On-chain et Off-chain (LN).
Le propriétaire du magasin peut cliquer et configurer les deux processeurs de paiement séparément. Un propriétaire de magasin pourrait vouloir exécuter le processeur on-chain seulement une fois toutes les X heures, tandis que le off-chain pourrait fonctionner toutes les quelques minutes. Pour On-chain, vous pouvez également définir une cible pour le bloc dans lequel il devrait être inclus. Par défaut, cela est réglé sur 1 (ou le prochain bloc disponible). Notez que configurer le processeur de paiement Off-chain n'a que le minuteur d'intervalle et pas de cible de bloc. Les paiements via le réseau Lightning sont instantanés.

![image](assets/en/62.webp)
![image](assets/en/63.webp)

Les propriétaires de magasin ne peuvent configurer le processeur on-chain que s'ils ont un Hot-wallet connecté à leur magasin.

![image](assets/en/64.webp)

Après avoir configuré un processeur de paiement, vous pouvez rapidement le supprimer ou le modifier en retournant à l'onglet du processeur de paiement dans les paramètres du magasin BTCPay Server.

**!?Note!?**

Processeur de paiement on-chain - Le processeur de paiements onchain ne peut fonctionner que sur un magasin configuré avec un Hot wallet connecté. Si aucun hot wallet n'est connecté, BTCPay Server ne détient pas les clés du portefeuille et ne pourra pas traiter automatiquement les paiements.

### Emails

BTCPay Server peut utiliser les Emails pour les Notifications ou, lorsqu'ils sont correctement configurés, pour récupérer des comptes qui ont été créés sur l'instance, car standard BTCPay Server n'envoie pas d'email lorsque le mot de passe est perdu, par exemple.

![image](assets/en/65.webp)

Avant qu'un propriétaire de magasin puisse définir des règles d'Email pour déclencher des événements spécifiques de son magasin, nous devons configurer quelques paramètres de base pour les emails. BTCPay Server a besoin de ces paramètres pour envoyer des emails pour des événements basés sur votre magasin ou pour les réinitialisations de mot de passe.

BTCPay Server a facilité la saisie de ces informations en utilisant l'option "Remplissage rapide" :

- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid

En utilisant l'option de remplissage rapide, BTCPay Server pré-remplira les champs pour le serveur SMTP et le port ; maintenant, le propriétaire du magasin doit seulement remplir ses identifiants dans une adresse Email, Login (qui est généralement identique à votre adresse email), et votre mot de passe. L'option avancée que BTCPay Server offre dans les paramètres d'email est de Désactiver les vérifications de sécurité du certificat TLS ; par défaut, cela est Activé.

![image](assets/en/66.webp)

Avec les règles d'Email, un propriétaire de magasin peut définir des événements spécifiques pour déclencher des emails à des adresses email spécifiques.

- Facture Créée
- Paiement de Facture Reçu
- Traitement de Facture
- Facture Expirée
- Facture Réglée
- Facture Invalide
- Paiement de Facture Réglé

Si le client a fourni une adresse Email, ces déclencheurs peuvent également envoyer les informations au client. Les propriétaires de magasin peuvent pré-remplir la ligne d'objet pour clarifier pourquoi cet Email a été envoyé et quel déclencheur l'a causé.

![image](assets/en/67.webp)

### Formulaires

Comme BTCPay Server ne collecte aucune donnée, un propriétaire de magasin pourrait vouloir ajouter un formulaire personnalisé à son expérience de paiement ; de cette façon, le propriétaire du magasin peut recueillir des informations supplémentaires de son client. Le constructeur de formulaires BTCPay Server se compose de deux parties, une vue visuelle et une vue de code plus avancée des formulaires.
Lors de la création d'un nouveau formulaire, BTCPay Server ouvre une nouvelle fenêtre demandant des informations de base sur ce que vous souhaitez que votre nouveau formulaire demande. Au début, le propriétaire du magasin doit donner un nom clair à son nouveau formulaire, ce nom NE PEUT PAS être changé après l'avoir défini.
![image](assets/en/68.webp)

Après que le propriétaire du magasin ait nommé le formulaire, vous pouvez également basculer l'interrupteur pour "Permettre l'utilisation publique du formulaire" sur ON, et il devient vert. Cela permet d'utiliser le formulaire dans tous les endroits visibles par les clients. Par exemple, si un propriétaire de magasin crée 1 facture séparée non pas via son Point De Vente, il pourrait quand même vouloir recueillir les informations du client ; basculer cet interrupteur sur ON permet de recueillir ces informations.

![image](assets/en/69.webp)

Chaque formulaire commence avec au moins 1 nouveau champ de formulaire. Un propriétaire de magasin peut choisir le type de champ qu'il doit être ;

- Texte
- Nombre
- Mot de passe
- Email
- URL
- Numéros de téléphone
- Date
- Champs cachés
- Fieldset
- Une zone de texte pour des commentaires libres.
- Sélecteur d'option

Chaque type vient avec ses paramètres à remplir. Le propriétaire du magasin peut le configurer à son goût. En dessous du premier champ créé, les propriétaires de magasin peuvent continuer à ajouter de nouveaux champs à ce formulaire.

![image](assets/en/70.webp)

#### Formulaires personnalisés avancés

BTCPay Server vous permet également de construire des Formulaires en code. JSON, en particulier. Au lieu de regarder l'éditeur, les propriétaires de magasin peuvent cliquer sur le bouton CODE juste à côté de l'éditeur et entrer dans le code de leurs Formulaires. Dans une définition de champ, seuls les champs suivants peuvent être définis ; les valeurs des champs sont stockées dans les métadonnées de la facture :

| Champ                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .fields.constant      | Si vrai, la .value doit être définie dans la définition du formulaire, et l'utilisateur ne pourra pas changer la valeur du champ. (exemple : la version de la définition du formulaire)                                                                                                                                                                                                                                                                                                                                                   |
| .fields.type          | Le type d'entrée HTML text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.options       | Si .fields.type est select, la liste des valeurs sélectionnables                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| .fields.options.text  | Le texte affiché pour cette option                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| .fields.options.value | La valeur du champ si cette option est sélectionnée                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| .fields.type=fieldset | Crée un fieldset HTML autour des enfants .fields.fields (voir ci-dessous)                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.name          | Le nom de propriété JSON du champ tel qu'il apparaîtra dans les métadonnées de la facture                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.value         | La valeur par défaut du champ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.required      | si vrai, le champ sera requis                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.label         | L'étiquette du champ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| .fields.helpText      | Texte supplémentaire pour fournir une explication pour le champ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| .fields.fields        | Vous pouvez organiser vos champs dans une hiérarchie, permettant aux champs enfants d'être imbriqués dans les métadonnées de la facture. Cette structure peut vous aider à mieux organiser et gérer les informations collectées, rendant leur accès et leur interprétation plus faciles. Par exemple, si vous avez un formulaire qui collecte les informations des clients, vous pouvez regrouper les champs sous un champ parent nommé client. Dans ce champ parent, vous pourriez avoir des champs enfants comme nom, Email et adresse. |

Le nom du champ représente le nom de la propriété JSON qui stocke la valeur fournie par l'utilisateur dans les métadonnées de la facture. Certains noms bien connus peuvent être interprétés et modifier les paramètres de la facture.

| Nom du champ     | Description              |
| ---------------- | ------------------------ |
| invoice_amount   | Le montant de la facture |
| invoice_currency | La devise de la facture  |

Vous pouvez pré-remplir automatiquement les champs d'une facture en ajoutant des chaînes de requête à l'URL du formulaire, telles que "?your_field=value".

Voici quelques cas d'utilisation pour cette fonctionnalité :

- Assistance à la saisie utilisateur : Pré-remplir les champs avec des informations connues sur le client pour leur faciliter la complétion du formulaire. Par exemple, si vous connaissez déjà l'adresse email d'un client, vous pouvez pré-remplir le champ email pour lui faire gagner du temps.
- Personnalisation : Personnaliser le formulaire en fonction des préférences des clients ou de la segmentation. Par exemple, si vous avez différents niveaux de clients, vous pouvez pré-remplir le formulaire avec des données pertinentes, telles que leur niveau d'adhésion ou des offres spécifiques.
- Suivi : Suivre la source des visites des clients en utilisant des champs cachés et des valeurs pré-remplies. Par exemple, vous pouvez créer des liens avec des valeurs utm_media pré-remplies pour chaque canal marketing (par exemple, Twitter, Facebook, Email). Cela vous aide à analyser l'efficacité de vos efforts marketing.
- Tests A/B : Pré-remplir les champs avec différentes valeurs pour tester différentes versions du formulaire, vous permettant d'optimiser l'expérience utilisateur et les taux de conversion.

### Résumé des compétences

Dans cette section, vous avez appris ce qui suit :

- La disposition et les fonctions des onglets dans les Paramètres du magasin
- Une multitude d'options pour affiner la gestion des taux de change sous-jacents, des paiements partiels, des légers sous-paiements, et plus encore.
- Personnaliser l'apparence du paiement, y compris l'activation principale de la chaîne en fonction du prix vs. l'activation de Lightning sur les factures.
- Gérer les niveaux d'accès au magasin et les permissions à travers les rôles.
- Configurer les emails automatiques et leurs déclencheurs
- Créer des formulaires personnalisés pour recueillir des informations supplémentaires sur les clients au moment du paiement.

### Évaluations des connaissances

#### Revue KA

Quelle est la différence entre les Paramètres du magasin et les Paramètres du serveur ?

#### Hypothèse KA

Décrivez certaines options que vous pourriez sélectionner dans Apparence du paiement > Paramètres de la facture, et pourquoi.

## BTCPay Server - Paramètres du serveur

<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>

BTCPay Server se compose de deux vues de paramètres différentes. L'une est dédiée aux Paramètres du magasin et l'autre aux Paramètres du serveur. Cette dernière n'est disponible que si vous êtes un administrateur du serveur et non pour les propriétaires de magasin. Les administrateurs de serveur peuvent ajouter des utilisateurs, créer des rôles personnalisés, configurer le serveur de messagerie, définir des politiques, exécuter des tâches de maintenance, vérifier tous les services attachés à BTCPay Server, télécharger des fichiers sur le serveur ou vérifier les journaux.

### Utilisateurs

Comme mentionné précédemment, les administrateurs de serveur peuvent inviter des utilisateurs sur leur serveur en les ajoutant à l'onglet Utilisateurs.

### Rôles personnalisés à l'échelle du serveur

BTCPay Server connaît deux types de rôles personnalisés, les rôles personnalisés spécifiques au magasin et les rôles personnalisés à l'échelle du serveur dans les paramètres de BTCPay Server. Les deux disposent d'un ensemble similaire de permissions ; cependant, si défini via l'onglet Paramètres de BTCPay Server - Rôles, le rôle appliqué sera à l'échelle du serveur et s'appliquera à plusieurs magasins. Remarquez une étiquette "À l'échelle du serveur" pour les rôles personnalisés dans les paramètres du serveur.

### Rôles personnalisés sur l'ensemble du serveur

Ensemble de permissions pour les rôles personnalisés sur l'ensemble du serveur :

- Modifier vos boutiques.
- Gérer les comptes d'échange liés à vos boutiques.
  - Voir les comptes d'échange liés à vos boutiques.
- Gérer vos paiements tirés.
- Créer des paiements tirés.
  - Créer des paiements tirés non approuvés.
- Modifier les factures.
  - Voir les factures.
  - Créer une facture.
  - Créer des factures à partir des nœuds Lightning associés à vos boutiques.
- Voir vos boutiques.
  - Voir les factures.
  - Voir vos demandes de paiement.
  - Modifier les webhooks des boutiques.
- Modifier vos demandes de paiement.
  - Voir vos demandes de paiement.
- Utiliser les nœuds Lightning associés à vos boutiques.
  - Voir les factures Lightning associées à vos boutiques.
  - Créer des factures à partir des nœuds Lightning associés à vos boutiques.
- Déposer des fonds sur les comptes d'échange liés à vos boutiques.
- Retirer des fonds des comptes d'échange vers votre boutique.
- Échanger des fonds sur les comptes d'échange de votre boutique.

**!?Note!?**

Lorsque le rôle est créé, le nom est fixe et ne peut pas être changé après en mode édition.

### Email

Les paramètres d'Email sur l'ensemble du serveur ressemblent à ceux des paramètres d'Email spécifiques à la boutique. Cependant, cette configuration gère non seulement les déclencheurs pour les boutiques ou les journaux d'administrateur. Cette configuration d'Email rend également la récupération de mot de passe disponible sur BTCPay Server lors de la connexion. Elle fonctionne de manière similaire aux paramètres spécifiques à la boutique ; les administrateurs peuvent rapidement remplir leurs paramètres d'Email et entrer leurs identifiants d'email, et le serveur peut maintenant envoyer des emails.

### Politiques

Les administrateurs de politique de BTCPay Server peuvent définir certains paramètres sur des sujets comme les paramètres des utilisateurs existants, les paramètres des nouveaux utilisateurs, les paramètres de notifications et les paramètres de maintenance. Ces paramètres sont destinés à enregistrer de nouveaux utilisateurs en tant qu'admin ou utilisateurs normaux ou même à cacher BTCPay Server des moteurs de recherche en ajoutant à l'en-tête de votre serveur.

#### Paramètres des utilisateurs existants

Les options disponibles ici sont séparées des rôles personnalisés. Ces permissions supplémentaires pourraient rendre une boutique ou le propriétaire d'une boutique vulnérable aux attaques. Politiques pouvant être ajoutées aux utilisateurs existants :

- Permettre aux non-admins d'utiliser le nœud Lightning interne dans leurs boutiques.
  - Cela permettrait aux propriétaires de boutique d'utiliser le nœud Lightning de l'administrateur du serveur et, par conséquent, ses fonds ! Attention, ce n'est pas une solution pour donner accès à Lightning.
- Permettre aux non-admins de créer des portefeuilles chauds pour leurs boutiques.
  - Cela permettrait à toute personne ayant un compte sur votre instance BTCPay Server de créer des portefeuilles chauds et de stocker leur graine de récupération sur le serveur de l'Administrateur. Cela pourrait rendre l'Administrateur responsable de la détention des fonds de tiers !
- Permettre aux non-admins d'importer des portefeuilles chauds pour leurs boutiques.
  - Similaire au sujet précédent de la création de portefeuilles chauds, cette politique permet d'importer un portefeuille chaud, avec les mêmes dangers mentionnés dans la section de création de portefeuilles chauds.

#### Paramètres des nouveaux utilisateurs

Nous pouvons définir certains paramètres importants pour gérer les nouveaux utilisateurs arrivant sur le serveur. Nous pouvons définir un email de confirmation pour les nouvelles inscriptions, désactiver la création de nouveaux utilisateurs via l'écran de connexion, et restreindre l'accès des non-admins à la création d'utilisateurs via l'API.

- Exiger un email de confirmation pour l'inscription.
  - L'administrateur du serveur doit avoir configuré un serveur Email !
- Désactiver l'inscription de nouveaux utilisateurs sur le serveur
- Désactiver l'accès des non-admins à l'endpoint API de création d'utilisateur.

Par défaut, BTCPay Server a activé la désactivation de l'inscription de nouveaux utilisateurs et désactivé l'accès des non-admins à l'endpoint API de création d'utilisateur. Cela est dû à un aspect de sécurité où aucune personne aléatoire qui aurait trouvé la connexion BTCPay de votre serveur ne peut commencer à créer des comptes.

#### Paramètres de Notification

![image](assets/en/76.webp)

#### Paramètres de Maintenance

BTCPay Server est un projet Open Source hébergé sur GitHub. Lorsque BTCPay Server publie une nouvelle version du logiciel, les administrateurs peuvent être notifiés qu'une nouvelle version est disponible. Les administrateurs peuvent également vouloir décourager les moteurs de recherche (google, yahoo, duckduckgo) d'indexer le domaine BTCPay Server. Comme BTCPay Server est FOSS, les développeurs du monde entier peuvent vouloir créer de nouvelles fonctionnalités ; BTCPay Server dispose d'une fonctionnalité expérimentale qui, une fois activée, permet à un administrateur d'utiliser des fonctionnalités non destinées à la production, uniquement à des fins de test.

- Vérifier les releases sur GitHub et notifier lorsqu'une nouvelle version de BTCPay Server est disponible.
- Décourager les moteurs de recherche d'indexer ce site
- Activer les fonctionnalités expérimentales.

![image](assets/en/77.webp)

#### Plugins

BTCPay Server peut ajouter des Plugins et étendre son ensemble de fonctionnalités. Les plugins, par défaut, sont chargés depuis le dépôt plugin-builder de BTCPay Server. Un administrateur, cependant, peut choisir de voir les plugins dans un état de Pré-release, et si le développeur du plugin le permet, l'administrateur du serveur peut maintenant installer des versions bêta des plugins.

![image](assets/en/78.webp)

##### Paramètres de Personnalisation

Un déploiement standard de BTCPay Server sera accessible via le domaine configuré pour celui-ci lors de l'installation. Cependant, un administrateur de serveur peut remapper le domaine racine et afficher l'une des applications créées à partir d'un magasin spécifique. L'administrateur du serveur peut également mapper des domaines spécifiques à des applications spécifiques.

- Afficher l'application à la racine du site web
  - Affiche la liste des applications possibles à montrer sur le domaine racine.

![image](assets/en/79.webp)

- Mapper des domaines spécifiques à des applications spécifiques.
  - Lorsque vous cliquez pour configurer un domaine spécifique pour des applications spécifiques, l'administrateur peut configurer autant de domaines pointant vers des applications spécifiques que nécessaire.

![image](assets/en/80.webp)

#### Explorateurs de Blocs

BTCPay Server, par défaut, utilise mempool.space comme son explorateur de blocs pour les transactions. Lorsque BTCPay Server génère une nouvelle facture, et qu'il y a une transaction liée à celle-ci, le propriétaire du magasin peut cliquer pour ouvrir la transaction ; BTCPay Server pointera par défaut vers mempool.space comme explorateur de blocs ; un administrateur de serveur peut changer cela selon ses préférences.

![image](assets/en/81.webp)

### Services

L'onglet des paramètres de BTCPay Server : Services offre une vue d'ensemble des composants utilisés par votre BTCPay Server. Les services exposés par votre BTCPay Server peuvent varier selon la méthode de déploiement.

Un administrateur de BTCPay Server peut cliquer sur "Voir les informations" derrière chaque service pour l'ouvrir et configurer des paramètres spécifiques.

![image](assets/en/82.webp)

#### LND (gRPC)

BTCPay expose le service gRPC de LND pour une consommation externe ; vous trouverez ici les informations de connexion ; les portefeuilles compatibles sont listés ici. BTCPay Server fournit également un code QR pour la connexion à scanner et à appliquer dans le portefeuille mobile.

Les administrateurs de serveur peuvent ouvrir plus de détails pour voir ;

- Détails de l'hôte
- Utilisation de SSL
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- Suite de chiffrement SSL GRPC (GRPC_SSL_CIPHER_SUITES)

#### LND (REST)

BTCPay expose le service REST de LND pour une consommation externe ; vous trouverez ici les informations de connexion ; les portefeuilles compatibles sont listés ici. Parmi les portefeuilles compatibles se trouvent Joule, Alby et ZeusLN. BTCPay Server fournit un code QR pour la connexion, à scanner et à appliquer dans le portefeuille compatible.

- URI REST
- Macaroon
- AdminMacaroon - InvoiceMacaroon
- ReadonlyMacaroon

#### Sauvegarde de la graine LND

La sauvegarde de la graine LND est utile pour récupérer les fonds de votre portefeuille LND en cas de corruption de votre serveur. Comme le nœud Lightning est un Hot-wallet, vous pouvez trouver les informations confidentielles de la graine sur cette page.

LND documente le processus de récupération. Voir https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md pour la documentation.

#### Ride The Lightning

Ride the Lightning est un outil de gestion de nœud Lightning développé comme logiciel Open Source. BTCPay Server utilise RTL comme composant de gestion de nœud Lightning dans sa pile. Les administrateurs de BTCPay Server peuvent accéder à RTL via l'onglet Services des paramètres du serveur ou en cliquant sur le portefeuille Lightning.

#### Nœud complet P2P

Les administrateurs de serveur peuvent vouloir connecter leur nœud Bitcoin à un portefeuille mobile. Cette page expose les informations pour se connecter à distance à votre nœud complet via le protocole P2P. Au moment de la rédaction de ce livre, BTCPay Server liste Blockstream Green et Wasabi wallet comme portefeuilles compatibles. BTCPay Server donne un code QR pour la connexion, scannez et appliquez dans le portefeuille compatible.

#### Nœud complet RPC

Cette page expose les informations pour se connecter à distance à votre nœud complet via le protocole RPC.

#### SSH

SSH est utilisé à des fins de maintenance. BTCPay Server montre la commande de connexion initiale pour atteindre votre serveur et les clés publiques SSH autorisées à se connecter à votre serveur. Les administrateurs de serveur pourraient vouloir désactiver les changements SSH via l'interface utilisateur de BTCPay Server.

#### DNS dynamique

Le DNS dynamique vous permet d'avoir un nom DNS stable pointant vers votre serveur, même si votre adresse IP change régulièrement. Cela est recommandé si vous hébergez BTCPay Server chez vous et souhaitez avoir un domaine clearnet pour accéder à votre serveur.

Notez que vous devez configurer correctement votre NAT et l'installation de BTCPay Server pour obtenir le certificat HTTPS.

### Thème

BTCPay Server, standard, vient avec deux thèmes : modes Clair et Sombre. Ils peuvent être changés en cliquant sur Compte en bas à gauche et en basculant entre le thème Sombre ou le thème Clair. Les administrateurs de BTCPay Server peuvent ajouter leur thème en fournissant un thème CSS personnalisé.

Les administrateurs peuvent étendre le thème Clair/Sombre en ajoutant leur propre CSS personnalisé ou en définissant leur thème personnalisé comme un thème complet.

![image](assets/en/83.webp)

#### Branding du serveur

Les administrateurs de serveur peuvent changer le branding de BTCPay Server en définissant un branding à l'échelle du serveur de votre entreprise. Comme BTCPay Server est FOSS, les administrateurs de serveur peuvent personnaliser le logiciel et changer l'apparence pour l'adapter à leur entreprise.

![image](assets/en/84.webp)

### Maintenance

En tant qu'administrateur de serveur, vos utilisateurs s'attendent à ce que vous preniez bien soin du serveur. Dans l'onglet Maintenance de BTCPay Server, l'admin peut effectuer une maintenance essentielle. Définir le nom de domaine de l'instance BTCPay Server, redémarrer ou nettoyer le serveur. Peut-être le plus important, exécuter des mises à jour.

BTCPay Server est un projet Open Source et se met à jour fréquemment. Chaque nouvelle version est annoncée soit par vos notifications BTCPay Server soit sur les canaux officiels de communication de BTCPay Server.

![image](assets/en/85.webp)

#### Nom de domaine

Après la configuration de BTCPay Server, un administrateur pourrait vouloir changer de son Domaine original. Dans l'onglet Maintenance, l'administrateur peut changer le Domaine. Après avoir cliqué sur confirmer et configuré les enregistrements DNS appropriés sur le Domaine, BTCPay Server se met à jour et redémarre pour revenir au nouveau Domaine.

![image](assets/en/86.webp)

#### Redémarrer

Redémarrer BTCPay Server et les services associés.

![image](assets/en/87.webp)

#### Nettoyer

BTCPay Server fonctionne avec des composants Docker ; avec les mises à jour, il peut rester des images Docker, des fichiers temporaires, etc. Les administrateurs de serveur peuvent nettoyer cela et récupérer de l'espace sur leur environnement en exécutant le script de nettoyage.
![image](assets/en/88.webp)

#### Mise à jour

Possiblement l'option la plus importante dans l'onglet de maintenance. BTCPay Server est construit par la communauté, et donc, ses cycles de mise à jour sont plus fréquents que la plupart des produits logiciels. Lorsque BTCPay Server a une nouvelle version, les administrateurs seront notifiés dans leur centre de notifications. En cliquant sur le bouton de mise à jour, BTCPay Server vérifiera GitHub pour la dernière version, mettra à jour le serveur et redémarrera. Avant de mettre à jour, il est toujours conseillé aux administrateurs de serveur de lire les notes de version distribuées par les canaux officiels de BTCPay Server.

![image](assets/en/89.webp)

### Journaux

Faire face à un problème n'est jamais agréable. Ce document explique le flux de travail le plus commun et les étapes pour identifier efficacement votre problème et le résoudre vous-même ou avec l'aide de la communauté.

Identifier le problème est crucial.

#### Reproduire le problème

Tout d'abord, essayez de déterminer quand le problème se produit. Essayez de reproduire le problème. Essayez de mettre à jour et de redémarrer votre serveur pour vérifier que vous pouvez reproduire votre problème. Si cela décrit mieux votre problème, prenez une capture d'écran.

##### Mettre à jour le serveur

Vérifiez votre version de BTCPay Server si elle est beaucoup plus ancienne que la [dernière version](https://github.com/btcpayserver/btcpayserver/releases) de BTCPay Server. Mettre à jour votre serveur peut résoudre le problème.

##### Redémarrer le serveur

Redémarrer votre serveur est un moyen facile de résoudre bon nombre des problèmes les plus courants de BTCPay Server. Vous devrez peut-être vous connecter en SSH à votre serveur pour le redémarrer.

##### Redémarrer un service

Pour certains problèmes, vous pourriez avoir besoin de redémarrer un service particulier dans votre déploiement BTCPay Server. Comme redémarrer le conteneur lets encrypt pour renouveler le certificat SSL.

```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```

Utilisez docker ps pour trouver le nom d'un autre service que vous souhaitez redémarrer.

#### Examiner les journaux

Les journaux peuvent fournir une pièce d'information essentielle. Dans les paragraphes suivants, nous décrirons comment obtenir les informations de journal pour différentes parties de BTCPay.

##### Journaux BTCPay

Depuis la version v1.0.3.8, vous pouvez facilement accéder aux journaux de BTCPay Server depuis l'interface. Si vous êtes un administrateur de serveur, allez dans Paramètres du serveur > Journaux et ouvrez le fichier des journaux. Si vous ne savez pas ce que signifie une erreur particulière dans les journaux, mentionnez-le lors du dépannage.

Si vous voulez des journaux plus détaillés et utilisez un déploiement Docker, vous pouvez voir les journaux de conteneurs Docker spécifiques en utilisant la ligne de commande. Voir ces [instructions pour se connecter en ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) à une instance de BTCPay fonctionnant sur un VPS.

Sur la page suivante, une liste générale des noms de conteneurs utilisés pour BTCPay Server.

Exécutez les commandes ci-dessous pour imprimer les journaux par nom de conteneur. Remplacez le nom du conteneur pour voir les journaux d'autres conteneurs.

```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```

| Journaux pour | Nom du conteneur                  |
| ------------- | --------------------------------- |
| BTCPayServer  | generated_btcpayserver_1          |
| NBXplorer     | generated_nbxplorer_1             |
| Bitcoind      | btcpayserver_bitcoind             |
| Postgres      | generated_postgres_1              |
| proxy         | letsencrypt-nginx-proxy-companion |
| Nginx         | nginx-gen                         |
| Nginx         | nginx                             |
| c-lightning   | btcpayserver_clightning_bitcoin   |
| LND           | btcpayserver_lnd_bitcoin          |
| RTL           | generated_lnd_bitcoin_rtl_1       |
| Thunderhub    | generated_bitcoin_thub_1          |
| LibrePatron   | librepatron                       |
| Tor           | tor-gen                           |
| Tor           | tor                               |

###### Lightning Network LND - Docker

Il existe plusieurs façons d'accéder à vos logs LND lorsque vous utilisez Docker. Commencez par vous connecter en tant que root :

```bash
sudo su -
Naviguez vers le répertoire correct :
cd btcpayserver-docker
# Trouvez le nom du conteneur :
docker ps
Imprimez les logs par nom de conteneur :
docker logs --tail 100 btcpayserver_lnd_bitcoin
```

Alternativement, vous pouvez rapidement imprimer les logs en utilisant l'ID du conteneur (seuls les premiers caractères ID uniques sont nécessaires, comme les deux caractères les plus à gauche) :

```bash
docker logs 'ajoutez votre ID de conteneur'
```

Si pour une raison quelconque vous avez besoin de plus de logs

```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/_data/logs/bitcoin/mainnet/
ls
```

Vous verrez quelque chose comme

```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```

Pour accéder aux logs non compressés de ces logs faites `cat lnd.log` ou si vous voulez un autre, utilisez `cat lnd.log.15`.

Pour accéder aux logs compressés en `.gzip` utilisez `gzip -d lnd.log.16.gz` (dans ce cas, nous accédons à `lnd.log.16.gz`). Cela devrait vous donner un nouveau fichier, où vous pouvez faire `cat lnd.log.16`. Au cas où cela ne fonctionnerait pas, vous devrez peut-être d'abord installer gzip avec `sudo apt-get install gzip`.

###### Lightning Network c-lightning - Docker

```bash
sudo su -
docker ps
# Trouvez l'ID du conteneur c-lightning.
docker logs 'ajoutez ici votre ID de conteneur'
```

alternativement, utilisez ceci

```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```

Vous pouvez également obtenir des informations de log avec la commande cli c-lightning.

```bash
bitcoin-lightning-cli.sh getlog
```

#### Logs du Nœud Bitcoin

En plus de [consulter les logs](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) de votre conteneur Bitcoind, vous pouvez également utiliser l'une des [commandes bitcoin-cli](https://developer.bitcoin.org/reference/rpc/index.html)

[(ouvre une nouvelle fenêtre)](https://developer.bitcoin.org/reference/rpc/index.html) pour obtenir des informations de votre nœud bitcoin. BTCPay inclut un script pour vous permettre de communiquer facilement avec votre nœud Bitcoin.

Dans le dossier btcpayserver-docker, obtenez les informations de la blockchain en utilisant votre nœud :

```bash
bitcoin-cli.sh getblockchaininfo
```

BTCPay Server dispose d'un système de fichiers local et télécharge directement les actifs des magasins (produits), logos et éléments de marque sur le serveur. Le système de fichiers du serveur n'est accessible que par les administrateurs du serveur ; les propriétaires de magasins peuvent télécharger leurs logos/éléments de marque au niveau du magasin.
Lorsque l'administrateur du serveur se trouve dans l'onglet de stockage de fichiers, il est possible de télécharger directement sur votre serveur ou de changer le fournisseur de stockage de fichiers pour un système de fichiers local ou Azure Blob Storage.

![image](assets/en/90.webp)

![image](assets/en/91.webp)

### Résumé des compétences

Dans cette section, vous avez appris ce qui suit :

- La différence entre les paramètres du magasin et du serveur, en particulier en ce qui concerne les utilisateurs, les rôles et les emails
- Définir des politiques à l'échelle du serveur pour l'utilisation et la création de portefeuilles chauds Lightning ou Bitcoin, l'enregistrement de nouveaux utilisateurs et les notifications par email.
- Comment ajouter des thèmes personnalisés (au lieu des simples options clair/sombre fournies) ainsi que créer des logos personnalisés
- Effectuer des tâches simples de maintenance du serveur via l'interface graphique fournie
- Résoudre les problèmes, y compris récupérer les détails pour l'un des conteneurs Docker ou votre nœud
- Gérer le stockage de fichiers

### Évaluation des connaissances

#### Révision conceptuelle KA

Quelle est la différence dans les rôles attribués via les paramètres du serveur vs les paramètres du magasin, et quelle pourrait être une utilisation potentielle pour l'un par rapport à l'autre ?

#### Révision pratique KA

Décrivez quelques cas d'utilisation possibles activés dans l'onglet Politiques.

#### Révision pratique KA

Décrivez certaines actions qu'un administrateur pourrait effectuer régulièrement dans l'onglet Maintenance.

## BTCPay Server - Paiements

<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>

Une facture est un document émis par le vendeur à l'acheteur pour collecter un paiement.

Dans BTCPay Server, une facture représente un document qui doit être payé dans un intervalle de temps défini à un taux de change fixe. Les factures ont une expiration car elles verrouillent le taux de change dans un cadre temporel spécifié pour protéger le destinataire des fluctuations de prix.

Le cœur de BTCPay Server est la capacité d'agir comme un système de gestion de factures Bitcoin. Une facture est un outil essentiel pour le suivi et la gestion d'un paiement reçu.

À moins que vous n'utilisiez un [Wallet](https://docs.btcpayserver.org/Wallet/) intégré pour recevoir manuellement les paiements, tous les paiements au sein d'un magasin seront affichés sur la page des factures. Cette page classe cumulativement les paiements par date et constitue une pièce centrale pour la gestion des factures et le dépannage des paiements.

![image](assets/en/92.webp)

### Général

#### Statuts des factures

Le tableau ci-dessous liste et décrit les statuts standard des factures dans BTCPay et suggère des actions communes. Les actions ne sont que des recommandations. Il appartient aux utilisateurs de définir le meilleur cours d'action pour leur cas d'utilisation et leur entreprise.

| Statut de la facture           | Description                                                                                                                                                 | Action                                                                                                                                                              |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nouveau                        | Non payé, le minuteur de la facture n'a pas encore expiré                                                                                                   | Aucune                                                                                                                                                              |
| Nouveau (paiement partiel)     | Payé, mais pas en totalité, le minuteur de la facture n'a pas encore expiré                                                                                 | Aucune                                                                                                                                                              |
| Expiré                         | Non payé, le minuteur de la facture a expiré                                                                                                                | Aucune                                                                                                                                                              |
| Expiré (paiement partiel) \*\* | Payé, mais pas en totalité, et expiré                                                                                                                       | Contacter l'acheteur pour organiser un remboursement ou lui demander de payer le reste. Marquer éventuellement la facture comme réglée ou invalide                  |
| Expiré (paiement tardif)       | Payé, en totalité, après l'expiration du minuteur de la facture                                                                                             | Contacter l'acheteur pour organiser un remboursement ou traiter la commande si les confirmations tardives sont acceptables.                                         |
| Réglé (payé en trop)           | Payé plus que le montant de la facture, réglé, reçu un nombre suffisant de confirmations                                                                    | Contacter l'acheteur pour organiser un remboursement du montant supplémentaire, ou attendre optionnellement que l'acheteur vous contacte                            |
| En traitement                  | Payé intégralement, mais n'a pas reçu un nombre suffisant de confirmations spécifié dans les paramètres du magasin                                          | Contacter l'acheteur pour organiser un remboursement du montant supplémentaire, ou attendre optionnellement que l'acheteur vous contacte                            |
| En traitement (payé en trop)   | Payé plus que le montant de la facture, n'a pas reçu un nombre suffisant de confirmations                                                                   | Attendre d'être réglé puis contacter l'acheteur pour organiser un remboursement du montant supplémentaire, ou attendre optionnellement que l'acheteur vous contacte |
| Réglé                          | Payé, intégralement, reçu un nombre suffisant de confirmations dans le magasin                                                                              | Exécuter la commande                                                                                                                                                |
| Réglé (marqué)                 | Le statut a été manuellement changé en réglé à partir d'un statut en traitement ou invalide                                                                 | L'administrateur du magasin a marqué le paiement comme réglé                                                                                                        |
| Invalide\*                     | Payé, mais a échoué à recevoir un nombre suffisant de confirmations dans le temps spécifié dans les paramètres du magasin                                   | Vérifier la transaction sur un explorateur de blockchain, si elle a reçu suffisamment de confirmations, marquer comme réglé                                         |
| Invalide (marqué)              | Le statut a été manuellement changé en invalide à partir d'un statut réglé ou expiré                                                                        | L'administrateur du magasin a marqué le paiement comme invalide                                                                                                     |
| Invalide (payé en trop)        | Payé plus que le montant de la facture, mais a échoué à recevoir un nombre suffisant de confirmations dans le temps spécifié dans les paramètres du magasin | Vérifier la transaction sur un explorateur de blockchain, si elle a reçu suffisamment de confirmations, marquer comme réglé                                         |

#### Détails de la facture

La page des détails de la facture contient toutes les informations relatives à une facture.

Les informations de la facture sont créées automatiquement en fonction du statut de la facture, du taux de change, etc. Les informations sur le produit sont créées automatiquement si la facture a été créée avec des informations sur le produit, comme dans l'application Point de Vente.

#### Filtrage des factures

Les factures peuvent être filtrées via les filtres rapides situés à côté du bouton de recherche ou les filtres avancés, qui peuvent être activés en cliquant sur le lien (Aide) en haut. Les utilisateurs peuvent filtrer les factures par magasin, identifiant de commande, identifiant d'article, statut ou date.

#### Exportation des factures

Les factures BTCPay Server peuvent être exportées au format CSV ou JSON. Pour plus d'informations sur l'exportation de factures et la comptabilité.

#### Rembourser une facture

Si, pour une raison quelconque, vous souhaitez émettre un remboursement, vous pouvez facilement créer un remboursement depuis la vue de la facture.

#### Archivage des factures

En raison de la fonctionnalité de non-réutilisation d'adresse de BTCPay Server, il est courant de voir de nombreuses factures expirées sur la page des factures de votre magasin. Pour les cacher de votre vue, sélectionnez-les dans la liste et marquez-les comme archivées. Les factures qui ont été marquées comme archivées ne sont pas supprimées. Le paiement à une facture archivée sera toujours détecté par votre BTCPay Server (statut payé en retard). Vous pouvez voir les factures archivées du magasin à tout moment en sélectionnant les factures archivées dans le menu déroulant du filtre de recherche.

#### Devise par défaut

Devise par défaut du magasin, cela a été défini lors de l'assistant de création du magasin

#### Permettre à quiconque de créer une facture

Vous devriez activer cette option si vous souhaitez permettre au monde extérieur de créer des factures dans votre magasin. Cette option n'est utile que si vous utilisez le bouton de paiement ou si vous émettez des factures via API ou site web HTML tiers. L'application PoS est pré-autorisée et n'a pas besoin de cette activation pour qu'un visiteur aléatoire puisse ouvrir votre magasin PoS et créer une facture.

#### Ajouter des frais supplémentaires (frais de réseau) à la facture

- Seulement si le client effectue plus d'un paiement pour la facture
- À chaque paiement
- Ne jamais ajouter de frais de réseau

#### La facture expire si le montant total n'a pas été payé après .. Minutes.

Le minuteur de la facture est réglé par défaut sur 15 minutes. Le minuteur est un mécanisme de protection contre la volatilité puisqu'il verrouille le montant de la cryptomonnaie selon les taux de change crypto vers fiat. Si le client ne paie pas la facture dans le délai défini, la facture est considérée comme expirée. La facture est considérée comme "payée" dès que la transaction est visible sur la blockchain (o-confirmations) mais considérée comme "complète" lorsqu'elle atteint le nombre de confirmations défini par le marchand (généralement, 1-6). Le minuteur est personnalisable.

#### Considérez la facture payée même si le montant payé est ..% inférieur au montant attendu.

Dans une situation où un client utilise un portefeuille d'échange pour payer directement une facture, l'échange prend une petite commission. Cela signifie que cette facture n'est pas considérée comme entièrement complétée. La facture obtient le statut "payée partiellement". Si un marchand souhaite accepter les factures sous-payées, vous pouvez définir ici le taux en pourcentage.

### Demandes

Les Demandes de Paiement sont une fonctionnalité qui permet aux propriétaires de magasins BTCPay de créer des factures de longue durée. Les fonds sont versés à une demande de paiement en utilisant le taux de change au moment du paiement. Cela permet aux utilisateurs de faire des paiements à leur convenance sans négocier ou vérifier les taux de change avec le propriétaire du magasin au moment du paiement.

Les utilisateurs peuvent payer les demandes en paiements partiels. La demande de paiement reste valide jusqu'à ce qu'elle soit payée en totalité ou si le propriétaire du magasin exige un délai d'expiration. Les adresses ne sont jamais réutilisées. Une nouvelle adresse est générée chaque fois que l'utilisateur clique sur payer pour créer une facture pour la demande de paiement.

Les propriétaires de magasins peuvent imprimer les demandes de paiement (ou exporter les données de facture) pour la tenue des registres et la comptabilité. BTCPay étiquette automatiquement les factures comme Demandes de Paiement dans la liste des factures de votre magasin.

#### Personnalisez Vos Demandes de Paiement

- Montant de la Facture - Définir le Montant de Paiement Demandé
- Dénomination - Afficher le Montant Demandé en Fiat ou Cryptomonnaie
- Quantité de Paiement - Autoriser uniquement les paiements uniques ou partiels
- Temps d'Expiration - Autoriser les paiements jusqu'à une date ou sans expiration
- Description - Éditeur de Texte, Tableaux de Données, Intégrer Photos & Vidéos
- Apparence - Couleur et Style avec des Thèmes CSS

![image](assets/en/93.webp)

#### Créer une Demande de Paiement

Dans le menu de gauche, allez sur Demande de Paiement et cliquez sur "Créer Demande de Paiement".

![image](assets/en/94.webp)

Fournissez le Nom de la Demande, le Montant, la Dénomination Affichée, le Magasin Associé, le Temps d'Expiration & la Description (Facultatif)

Sélectionnez l'option Permettre au payeur de créer des factures dans sa propre dénomination si vous souhaitez autoriser les paiements partiels.

Cliquez sur Enregistrer & Voir pour réviser votre demande de paiement.

BTCPay crée une URL pour la demande de paiement. Partagez cette URL pour voir votre demande de paiement. Besoin de plusieurs demandes identiques ? Vous pouvez dupliquer les demandes de paiement en utilisant l'option Clone dans le menu principal.

![image](assets/en/95.webp)

**ATTENTION**

Les demandes de paiement dépendent du magasin, ce qui signifie que chaque demande de paiement est associée à un magasin lors de sa création. Assurez-vous d'avoir un portefeuille connecté à votre magasin auquel appartient la demande de paiement.

#### Demande Payée

Le payeur et le demandeur peuvent voir le statut de la demande de paiement après l'envoi du paiement. Le statut apparaîtra comme Réglé si le paiement a été reçu en totalité. Si seulement des paiements partiels ont été effectués, le Montant Dû affichera le solde dû.

![image](assets/en/96.webp)

#### Personnaliser les Demandes de Paiement

Le contenu de la description peut être édité en utilisant l'éditeur de texte de la demande de paiement. Les deux options sont disponibles si vous souhaitez utiliser des thèmes de couleur supplémentaires ou un style CSS personnalisé.
Les utilisateurs non techniques peuvent utiliser un [thème bootstrap](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Une personnalisation supplémentaire peut être réalisée en fournissant du code CSS additionnel, comme montré ci-dessous.

```css
:racine {
  --btcpay-police-de-base: "Source Sans Pro", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --btcpay-primaire: #7d4698;
  --btcpay-accent-primaire: #59316b;
  --btcpay-texte-du-corps: #333a41;
  --btcpay-fond-du-corps: #fff;
  --btcpay-tuile-de-fond: #f8f9fa;
}

#mainNav {
  couleur: blanc;
  arrière-plan: dégradé linéaire(#59316b, #331840);
}

#mainNav .btn-link {
  couleur: blanc;
}
```

### Paiements Pull

Traditionnellement, un destinataire partage son adresse Bitcoin pour effectuer un paiement Bitcoin, et l'expéditeur envoie ensuite de l'argent à cette adresse. Un tel système est appelé paiement Push, car l'expéditeur initie le paiement tandis que le destinataire peut être indisponible, poussant le paiement vers le destinataire.

Cependant, que se passe-t-il si on inverse le rôle ?

Et si, au lieu qu'un expéditeur pousse le paiement, l'expéditeur permet au destinataire de tirer le paiement au moment jugé opportun par le destinataire ? C'est le concept du paiement Pull. Cela permet plusieurs nouvelles applications, telles que :

- Un service d'abonnement (où l'abonné permet au service de tirer de l'argent chaque x période de temps)
- Les remboursements (où le commerçant permet au client de tirer l'argent du remboursement dans son portefeuille quand il le juge opportun)
- La facturation basée sur le temps pour les freelances (où la personne embauchant permet au freelance de tirer de l'argent dans son portefeuille à mesure que le temps est rapporté)
- Le patronage (où le mécène permet au bénéficiaire de tirer de l'argent chaque mois pour continuer à soutenir leur travail)
- La vente automatique (où un client d'un échange permettrait à un échange de tirer de l'argent de son portefeuille pour vendre automatiquement chaque mois)
- Le système de retrait de solde (où un service à haut volume permet aux utilisateurs de demander des retraits de leur solde, le service peut alors facilement regrouper tous les paiements à de nombreux utilisateurs à intervalles fixes)

### Paiements

La fonctionnalité de paiement est liée aux [Paiements Pull](https://docs.btcpayserver.org/PullPayments/). Cette fonctionnalité vous permet de créer des paiements au sein de votre BTCPay. Cette fonctionnalité vous permet de traiter des paiements pull (remboursements, paiements de salaires ou retraits).

#### Exemple 1 : Remboursement

Commençons par l'exemple du remboursement. Le client a acheté un article dans votre magasin mais doit malheureusement retourner l'article. Il souhaite un remboursement. Au sein de BTCPay, vous pouvez créer un [Remboursement](https://docs.btcpayserver.org/Refund/) et fournir au client le lien pour réclamer ses fonds. Lorsque le client a donné son adresse et réclamé les fonds, cela sera affiché dans les Paiements.

Le premier statut est En attente d'approbation. Les employés du magasin peuvent vérifier si plusieurs sont en attente, et après avoir fait leur sélection, vous utilisez le bouton Actions.

Options sur le bouton d'action

- Approuver les paiements sélectionnés
- Approuver et envoyer les paiements sélectionnés
- Annuler les paiements sélectionnés

L'étape suivante est d'Approuver et envoyer les paiements sélectionnés puisque nous voulons rembourser le client. Vérifiez l'Adresse du Client, montre le montant et si nous voulons que les frais soient soustraits du remboursement ou non. Une fois que vous avez fait les vérifications, il ne reste plus qu'à signer la transaction.
Le client est désormais informé sur la page de Réclamation. Il peut suivre la transaction puisqu'il dispose d'un lien vers un explorateur de blocs et sa transaction. Une fois la transaction confirmée et le statut passé à Complété.

#### Exemple 2 : Salaire

Abordons maintenant le paiement des salaires, car cela est géré depuis l'intérieur du magasin et non à la demande du client. Le principe est le même ; cela utilise les paiements Pull. Mais au lieu de créer un remboursement, nous allons effectuer un [Paiement Pull](https://docs.btcpayserver.org/PullPayments/).

Allez dans l'onglet Paiements Pull de votre serveur BTCPay. En haut à droite, cliquez sur le bouton Créer un Paiement Pull.

Nous sommes maintenant dans la création du Paiement, donnez-lui un nom et le montant souhaité dans la devise voulue, remplissez la Description, pour que l'employé sache de quoi il s'agit. La partie suivante est similaire aux remboursements. L'employé remplit l'adresse de Destination et le montant qu'il souhaite réclamer de ce Paiement. Il peut décider de le faire en 2 réclamations séparées, vers des adresses différentes, ou même de réclamer partiellement via lightning.

Si plusieurs Paiements en attente existent, vous pouvez les regrouper pour qu'ils soient signés et envoyés. Une fois signés, les paiements passent à l'onglet En cours et affichent la Transaction. Lorsqu'ils sont acceptés par le réseau, le paiement passe à l'onglet Complété. L'onglet Complété sert uniquement à des fins historiques. Il contient les Paiements traités et la transaction qui lui appartient.

### Paiements Pull

#### Concept

Lorsqu'un expéditeur configure un paiement Pull, il peut configurer un certain nombre de propriétés :

- Nom de la demande de Pull
- Un montant limite
- Une Unité (comme BTC, SAT, USD)
- Méthodes de paiement
  - BTC On-chain
  - BTC Off-chain
- Description
- CSS personnalisé
- Date de fin (optionnelle pour Lightning Network BOLT11)

Après cela, l'expéditeur peut partager le paiement Pull à l'aide d'un lien avec le destinataire, permettant à ce dernier de créer un paiement. Le destinataire choisira son paiement :

- Quelle méthode de paiement utiliser
- Où envoyer l'argent

Une fois un paiement créé, il comptera dans la limite du paiement Pull pour la période en cours. L'expéditeur approuvera alors le paiement en définissant le taux auquel le paiement sera envoyé et procédera au paiement.

Pour l'expéditeur, nous fournissons un moyen facile à utiliser pour regrouper le paiement de plusieurs paiements depuis le [Portefeuille Interne BTCPay](https://docs.btcpayserver.org/Wallet/).

#### API Greenfield

Le serveur BTCPay fournit une API complète à la fois pour l'expéditeur et le destinataire, documentée sur la page `/docs` de votre instance. (ou sur le site de documentation https://docs.btcpayserver.org)

Puisque notre API expose la capacité complète des paiements Pull, un expéditeur peut automatiser les paiements selon ses propres besoins.

### Résumé des compétences

Dans cette section, vous avez appris ce qui suit :

- Une compréhension approfondie des statuts de facture de BTCPay Server ainsi que des actions pouvant être effectuées sur celles-ci
- Personnaliser et gérer les mécanismes de facture à longue durée connus sous le nom de Demandes.
- Les possibilités de paiement flexibles supplémentaires ouvertes avec la fonctionnalité unique de Paiement Pull de BTCPay Server, en particulier comment gérer les remboursements et les paiements de salaires.

### Évaluation des connaissances

#### KA Revue conceptuelle

Quelles sont certaines différences entre les factures et les demandes de paiement, et quelle pourrait être une bonne raison d'utiliser ces dernières ?

#### KA Revue conceptuelle

Comment les paiements Pull étendent-ils ce qui peut typiquement être fait on-chain ? Décrivez certains cas d'utilisation qu'ils permettent.

## Plugins par défaut du serveur BTCPay

<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>

### Plugins et Applications par Défaut

Le serveur BTCPay inclut un ensemble standard de Plugins (Applications) qui peuvent transformer le serveur BTCPay en une passerelle de paiement e-commerce. Avec l'ajout d'un Point de vente, d'une plateforme de Crowdfunding et d'un bouton de paiement facile, le serveur BTCPay devient une solution facile à déployer.

### Point De Vente

L'un des Plugins standards du serveur BTCPay est le Point de Vente (PoS). Avec le plugin PoS, un propriétaire de magasin peut créer un Webshop directement depuis le serveur BTCPay, le propriétaire du magasin n'a pas besoin de solutions e-commerce tierces pour gérer un Webshop. L'application web PoS permet aux utilisateurs possédant des magasins physiques d'accepter facilement le Bitcoin, sans frais ni intermédiaire, directement dans leur portefeuille. Le PoS peut être facilement affiché sur des tablettes ou d'autres appareils supportant la navigation web. Les utilisateurs peuvent facilement créer un raccourci sur l'écran d'accueil pour accéder rapidement à l'application web.

#### Comment créer un nouveau Point de Vente

Le serveur BTCPay permet aux propriétaires de magasins de créer rapidement un Point de Vente dans plusieurs configurations. Le serveur BTCPay reconnaît que tous les magasins ne sont pas e-commerce, et que tous les magasins ne sont pas des bars ou des restaurants, et il propose plusieurs configurations standard pour votre PoS.

Lorsque le propriétaire du magasin clique sur "Point de Vente" dans sa barre de menu gauche, le serveur BTCPay demandera maintenant un nom ; ce nom sera visible dans la barre de menu gauche. Cliquez sur Créer pour créer le PoS.

![image](assets/en/97.webp)

#### Mettre à jour le Point de Vente nouvellement créé

Après avoir créé un nouveau PoS, l'écran suivant sera pour mettre à jour votre Point de Vente et ajouter des articles pour votre magasin.

##### Nom de l'application

Le nom donné ici à votre Point de Vente sera visible dans le menu principal du serveur BTCPay.

##### Titre d'affichage

Le public verra le titre public ou le nom lors de la visite de votre magasin. Le serveur BTCPay nomme par défaut votre magasin "Tea shop" Remplacez cela par le nom de votre magasin.

![image](assets/en/98.webp)

#### Choisir le Style du Point de Vente

Le serveur BTCPay est capable d'afficher son Point De Vente de plusieurs manières.

- Liste de produits
  - Une vue de magasin où les clients ne peuvent acheter qu'un produit à la fois.
- Liste de produits avec un panier.
  - Une vue de magasin où les clients peuvent acheter plusieurs articles à la fois et obtenir un aperçu du panier d'achat à droite de leur écran.
- Clavier uniquement
  - Pas de liste de produits, juste un clavier pour la facturation directe.
- Affichage d'impression (Liste de produits imprimable avec QR)
  - Si vous ne pouvez pas toujours afficher votre liste de produits numériquement, vous avez besoin d'une solution "hors ligne" pour les produits ; le serveur BTCPay dispose d'un affichage d'impression pour fonctionner comme un magasin hors ligne.

![image](assets/en/99.webp)

#### Style du Point de Vente - Liste de produits

![image](assets/en/100.webp)

#### Style du Point de Vente - Liste de produits + Panier

![image](assets/en/101.webp)

#### Style du Point de Vente - Clavier uniquement

![image](assets/en/102.webp)

#### Style du Point de Vente - Affichage d'impression

![image](assets/en/103.webp)

#### Devise

Le propriétaire du magasin peut définir une devise différente pour son Point de Vente que sa devise par défaut. La devise par défaut du magasin remplira automatiquement ce champ.

#### Description

Parlez au monde de votre magasin ; que vendez-vous, et à quel prix ? Tout ce qui explique votre magasin va ici.

#### Produits

Lorsqu'un Point de Vente est créé, un serveur BTCPay standard ajoute quelques articles au magasin pour référence. Cliquez sur le bouton Modifier sur l'un des articles standards pour mieux comprendre chaque option possible pour un article.

Créer un nouveau produit dans votre magasin consiste en les champs suivants ;

- Titre
- Prix (fixe, minimum ou personnalisé)
- URL de l'image
- Description
- Inventaire
- ID
- Texte du bouton d'achat.
- Activer/Désactiver

Une fois que le propriétaire du magasin a rempli tous les champs du nouveau produit, cliquez sur enregistrer, et vous remarquerez que la section Produits dans le Point de Vente commence à se remplir. Assurez-vous toujours d'enregistrer en haut à droite de votre écran pour éviter que les propriétaires de magasin ne perdent leur progression sur l'ajout de produits.

Les propriétaires de magasin peuvent également utiliser l'"Éditeur Brut" pour configurer leurs produits. L'éditeur brut nécessite une compréhension basique des structures JSON.

#### Paiement

Le serveur BTCPay permet une petite personnalisation spécifique au PoS pour le paiement. Le propriétaire du magasin peut définir le texte "Acheter pour x" ou demander des données spécifiques au client en ajoutant des formulaires.

#### Pourboires

Seuls certains magasins ont besoin de l'option pour les pourboires sur leurs ventes. Les propriétaires de magasin peuvent activer ou désactiver cette option comme ils le jugent approprié pour leur magasin. Si le magasin utilise l'option pourboires activée, le propriétaire du magasin peut définir le texte dans le champ pour les pourboires qu'il préfère. Les pourboires sur le serveur BTCPay fonctionnent sur la base d'un montant en pourcentage. Les propriétaires de magasin peuvent ajouter plusieurs pourcentages séparés par des virgules.

#### Réductions

En tant que propriétaire de magasin, vous voudrez peut-être donner au client une réduction personnalisée au moment du paiement ; le basculement pour les Réductions devient disponible lors du paiement de votre magasin. Cependant, cela est très déconseillé pour les systèmes de paiement en libre-service.

#### Paiements Personnalisés

Lorsque l'option Paiements Personnalisés est activée, le client peut saisir son prix fixé égal ou supérieur à la facture originale générée par le magasin.

#### Options Supplémentaires

Après avoir tout configuré pour votre Point de Vente, il reste quelques options supplémentaires. Les propriétaires de magasin peuvent facilement intégrer leur PoS via un Iframe ou intégrer un bouton de paiement renvoyant à un article spécifique du magasin. Pour styliser le PoS store tout juste créé, les propriétaires peuvent ajouter du CSS personnalisé au bas des options supplémentaires.

#### Supprimer cette application

Si le propriétaire du magasin souhaite supprimer entièrement le Point de Vente de son serveur BTCPay, au bas de la mise à jour du PoS, les propriétaires de magasin peuvent cliquer sur le bouton Supprimer cette application pour détruire complètement leur application PoS. Lors du clic sur "Supprimer cette application", le serveur BTCPay demandera une confirmation en tapant `DELETE` et en confirmant en cliquant sur le bouton Supprimer. Après la suppression, le propriétaire du magasin retourne au tableau de bord du serveur BTCPay.

### Serveur BTCPay - Crowdfund

À côté du plugin Point de Vente, le serveur BTCPay offre la possibilité de créer un financement participatif. Comme sur toute autre plateforme de Crowdfund, les propriétaires de magasin peuvent définir un objectif, créer des avantages pour les contributions, et le personnaliser selon leurs besoins.

#### Comment configurer un nouveau financement participatif

Cliquez sur le plugin Crowdfund via le menu principal à gauche de votre serveur BTCPay, sous la section Plugin. Le serveur BTCPay demandera maintenant un nom pour le Crowdfund ; ce nom sera également affiché dans la barre de menu de gauche.

#### Mettre à jour le Point de Vente nouvellement créé

Une fois l'application nommée, l'écran suivant sera de mettre à jour l'application pour lui donner du contexte.

#### Nom de l'application

Le nom donné à votre Crowdfund sera visible dans le menu principal du serveur BTCPay.

#### Titre d'affichage

Le titre est donné au Crowdfund pour le public.

#### Slogan

Donnez au crowdfund une phrase accrocheuse pour reconnaître de quoi la collecte de fonds parle.

![image](assets/en/107.webp)

#### URL de l'image vedette

Chaque crowdfund a son image principale, celle que vous reconnaissez directement. Cette image peut être stockée sur votre serveur si vous avez des droits administratifs, les administrateurs peuvent télécharger sous les paramètres du serveur BTCPay Server - Fichiers. Lorsque vous êtes propriétaire d'une boutique, l'image doit être téléchargée sur le web via un hébergeur tiers (par exemple imgur)

#### Rendre le Crowdfund Public

Ce basculeur rend votre Crowdfund public et donc visible pour le monde extérieur. À des fins de test ou pour voir si votre thème est appliqué correctement, on peut vouloir garder cela sur OFF pendant la période de création du crowdfund.

#### Description

Parlez au monde de votre Crowdfund, pour quoi collectez-vous des fonds ? Tout ce qui explique votre crowdfund va ici.

![image](assets/en/108.webp)

#### Objectif du Crowdfund

Fixez un objectif cible pour ce que la collecte de fonds devrait rapporter au projet et dans quelle devise l'objectif doit être libellé. Assurez-vous que si vos objectifs sont fixés entre des dates, incluez ces dates cibles et de fin sous Objectifs dans le crowdfund.

![image](assets/en/109.webp)

#### Avantages

Les avantages aident beaucoup votre crowdfunding. C'est parce que les avantages donnent aux gens un moyen de participer à votre campagne. Ils exploitent les motivations égoïstes ainsi que les motivations bienveillantes. Et ils vous permettent d'accéder aux dépenses de vos supporters, pas seulement à leur bourse philanthropique -- vous pouvez deviner laquelle est la plus significative.

Créer un nouvel avantage consiste en les champs suivants ;

- Titre
- Prix (fixe, minimum, ou personnalisé)
- URL de l'image
- Description
- Inventaire
- ID
- Texte du bouton d'achat.
- Activer/Désactiver

Une fois que le propriétaire de la boutique a rempli tous les champs du nouvel avantage à créer, cliquez sur enregistrer, et vous remarquerez que la section Avantages dans les crowdfunds commence maintenant à se remplir.

![image](assets/en/110.webp)

### BTCPay Server - Point De Vente

#### Contributions

Les propriétaires de magasins peuvent choisir comment afficher les Avantages, comment ils sont triés, ou même classés par rapport aux autres avantages. Cependant, une fois que les objectifs du Crowdfund sont atteints, les propriétaires de magasins peuvent vouloir arrêter les dons vers cette collecte de fonds. Par conséquent, il peut basculer sur "Ne pas autoriser de contributions supplémentaires après avoir atteint l'objectif". Cela arrêtera le Crowdfund d'accepter des dons.

##### Comportement du Crowdfund

Le standard du Crowdfund ne compte que les factures créées avec le Crowdfund vers l'objectif. Cependant, il peut y avoir des cas où le propriétaire du magasin veut que toutes les factures faites dans ce magasin comptent pour le crowdfund.

#### Options supplémentaires pour la personnalisation

BTCPay Server offre quelques personnalisations supplémentaires. Ajoutez des sons, des animations, ou même des fils de discussion au Crowdfund. Les propriétaires de magasins peuvent également changer l'apparence du Crowdfund en entrant leur propre CSS personnalisé.

#### Supprimer cette application

Si le propriétaire du magasin veut supprimer complètement le Crowdfund de son BTCPay Server, au bas de la mise à jour du Crowdfund, les propriétaires de magasins peuvent cliquer sur le bouton "Supprimer cette application" pour détruire complètement leur application Crowdfund. Lors du clic sur "Supprimer cette application", BTCPay Server demandera une confirmation en tapant `DELETE` et en confirmant en cliquant sur le bouton Supprimer. Après la suppression, le propriétaire du magasin retourne au tableau de bord BTCPay Server.

### BTCPay Server - Bouton de Paiement

Des boutons de paiement HTML facilement intégrables et hautement personnalisables permettent aux propriétaires de magasins de recevoir des pourboires et des dons. Dans la barre de menu gauche de BTCPay Server, sous la section Plugins, les propriétaires de magasins peuvent cliquer sur "Pay Button" et cliquer sur Activer pour créer un bouton de paiement.

#### Paramètres généraux

Dans les Paramètres généraux pour le bouton de paiement, les propriétaires de magasins peuvent définir

- Prix standard
- Devise par défaut
- Méthode de paiement par défaut
  - Utiliser la valeur par défaut du magasin
  - BTC on-chain
  - BTC Off-chain (Lightning)
  - BTC Off-chain (LNURL-pay)
- Description du paiement
- ID de commande

#### Options d'affichage

Le bouton de paiement de BTCPay Server peut être configuré pour s'adapter à différents styles. Les boutons peuvent avoir un montant fixe ou personnalisé, affiché soit avec un curseur soit avec des bascules plus et moins.

#### Utiliser le Modal

Lors de la création du bouton de paiement, les propriétaires de magasins peuvent choisir son comportement lorsqu'un client clique dessus et l'afficher dans un modal ou comme une nouvelle page.

**!?Note!?**

Attention : Le bouton de paiement ne doit être utilisé que pour les pourboires et les dons.

L'utilisation du bouton de paiement pour les intégrations de commerce électronique n'est pas recommandée puisque les informations pertinentes à la commande peuvent être modifiées par l'utilisateur. Pour le commerce électronique, vous devriez utiliser notre API Greenfield. Si ce magasin traite des transactions commerciales, nous vous conseillons de créer un magasin séparé avant d'utiliser le bouton de paiement.

#### Personnaliser le texte du bouton de paiement

Par défaut, le bouton de paiement de BTCPay Server indique "Pay With BTCPay". Les propriétaires de magasins peuvent définir ce texte à leur guise et changer le logo de BTCPay Server par le leur. Définissez le texte en utilisant "Pay Button Text" et collez l'URL de l'image sous "Pay Button Image URL".

##### Taille de l'image

La taille de l'image dans le bouton ne peut être définie que sur trois valeurs par défaut.

- 146x40px
- 168x46px
- 209x57px

#### Type de bouton

BTCPay Server connaît trois états pour le bouton de paiement.

- Montant fixe
  - Le prix précédemment défini se trouve dans les paramètres généraux du bouton.
- Montant personnalisé
  - Le bouton de paiement de BTCPay Server a des bascules + et - pour définir un prix personnalisé.
  - Lors de l'utilisation du montant personnalisé, BTCPay Server demandera un Min, Max et comment il devrait augmenter progressivement.
  - Les boutons peuvent être réglés sur "Utiliser le style d'entrée simple". Cela supprime les bascules +/-.
  - Adapter le bouton en ligne où le bouton et les bascules apparaissent en ligne.
- Curseur
  - Similaire au montant personnalisé, cependant, visuellement différent car il a un curseur au lieu des bascules +/-.
  - Lors de l'utilisation du curseur, BTCPay Server demandera un Min, Max et comment il devrait augmenter progressivement.

**!?Note!?**

La suppression du bouton de paiement peut être effectuée en haut dans la description d'avertissement.

#### Notifications de paiement

Le IPN (Instant Payment Notification) du serveur est destiné aux webhooks et peut être rempli par une URL pour poster les données après achat.

#### Notifications par email

Chaque fois qu'un paiement a lieu, BTCPay Server peut notifier le propriétaire du magasin.

#### Redirection du navigateur

Lorsque le client termine l'achat, il sera redirigé vers ce lien s'il est défini par le propriétaire du magasin.

#### Options avancées du bouton de paiement

Spécifiez des paramètres de chaîne de requête supplémentaires qui doivent être ajoutés à la page de paiement une fois la facture créée. Par exemple, `lang=da-DK` chargerait la page de paiement en danois par défaut.

#### Utiliser l'application comme point de terminaison

Liez directement le bouton de paiement à un article dans l'une des applications PoS ou Crowdfund avant.
Les propriétaires de magasins peuvent cliquer sur le menu déroulant et sélectionner l'App désirée ; une fois l'App sélectionnée, le propriétaire du magasin peut ajouter l'article qui doit être lié.

#### Code Généré

Comme le bouton de paiement de BTCPay Server est un HTML facilement intégrable, BTCPay Server affiche le code généré à copier sur un site web en bas après avoir configuré le bouton de paiement.

Les propriétaires de magasins peuvent copier le code généré sur leur site web, et le bouton de paiement de BTCPay Server est directement actif sur leur site web.

#### Notifications de Paiement

L'IPN (Instant Payment Notification) du serveur est destiné aux webhooks et peut être rempli par une URL pour poster les données d'achat.

#### Notifications par Email

Chaque fois qu'un paiement est effectué, BTCPay Server peut notifier le propriétaire du magasin.

#### Redirection du Navigateur

Lorsque le client termine l'achat, il sera redirigé vers ce lien s'il est défini par le propriétaire du magasin.

#### Options Avancées du Bouton de Paiement

Spécifiez des paramètres de chaîne de requête supplémentaires qui doivent être ajoutés à la page de paiement une fois la facture créée. Par exemple, `lang=da-DK` chargerait la page de paiement en danois par défaut.

#### Utiliser l'App comme Point de Terminaison

Liez directement le bouton de paiement à un article dans l'une des applications PoS ou Crowdfund précédentes. Les propriétaires de magasins peuvent cliquer sur le menu déroulant et sélectionner l'app désirée, une fois l'app sélectionnée, le propriétaire du magasin peut ajouter l'article qui doit être lié.

#### Code Généré

Comme le bouton de paiement de BTCPay Server est un HTML facilement intégrable, BTCPay Server affiche le code généré à copier sur un site web en bas après avoir configuré le bouton de paiement. Les propriétaires de magasins peuvent copier le code généré sur leur site web et le bouton de paiement de BTCPay Server est directement actif sur leur site web.

### Résumé des Compétences

Dans cette section, vous avez appris :

- Comment utiliser le plugin PoS intégré de BTCPay Server pour créer facilement un magasin personnalisé
- Comment utiliser le plugin Crowdfund intégré de BTCPay Server pour créer facilement une application de financement participatif personnalisée
- Générer du code pour un bouton de paiement personnalisé en utilisant le plugin du bouton de paiement

### Évaluation des Connaissances

#### Révision de l'Évaluation des Connaissances

Quels sont les trois plugins intégrés qui sont fournis standard avec BTCPay Server ? En quelques mots, décrivez comment chacun peut être utilisé.

# Configuration de BTCPay Server

<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>

## Compréhension de base de l'installation de BTCPay Server sur un environnement LunaNode

<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>

### Installation de BTCPay Server sur Env. Hébergé (LunaNode)

Ces étapes fourniront toutes les informations nécessaires pour commencer à utiliser BTCPay Server sur LunaNode. Il existe de nombreuses options sur la manière de déployer le logiciel.
Vous pouvez trouver tous les détails de BTCPay Server sur https://docs.btcpayserver.org.

#### Par où commencer ?

Dans cette partie, vous vous familiariserez avec LunaNode en tant que fournisseur d'hébergement, apprendrez les premières étapes de l'utilisation de votre BTCPay Server et comment procéder avec le Lightning Network. Après avoir parcouru toutes les étapes, vous pourrez gérer un webshop ou une plateforme de financement participatif acceptant Bitcoin !

Ceci est l'une des nombreuses façons de déployer BTCPay Server. Lisez notre documentation pour plus de détails,

https://docs.btcpayserver.org.

### Déploiement de BTCPay Server - LunaNode

#### Déploiement LunaNode

Tout d'abord, rendez-vous sur le site de LunaNode.com, où nous allons créer un nouveau compte. Cliquez sur "Sign Up" en haut à droite ou utilisez l'assistant "Get Started" sur leur page d'accueil.
![image](assets/en/111.webp)

Après avoir créé votre nouveau compte, LunaNode envoie un e-mail de vérification. Une fois le compte vérifié, contrairement à Voltage, vous êtes immédiatement invité à recharger le solde de votre compte. Ce solde est nécessaire pour payer l'espace serveur et les coûts d'hébergement.

![image](assets/en/112.webp)

#### Ajouter du crédit à votre compte LunaNode

Une fois que vous avez cliqué sur "Deposit credit", vous pouvez définir combien vous souhaitez ajouter à votre compte et comment vous souhaitez payer. LunaNode et BTCPay Server coûteront entre 10$USD et 20$USD par mois.
Contrairement à Voltage.cloud, vous avez un accès complet à votre serveur privé virtuel (VPS désormais) et avez donc un peu plus de contrôle sur votre serveur. Après avoir créé votre nouveau compte, LunaNode envoie un e-mail de vérification.
Une fois le compte vérifié, contrairement à Voltage, vous êtes maintenant immédiatement invité à recharger le solde de votre compte. Ce solde est nécessaire pour payer l'espace serveur et les coûts d'hébergement.

#### Comment déployer un nouveau serveur ?

Dans ce guide, nous allons passer par la configuration en créant un ensemble de clés API et en utilisant le lanceur BTCPay Server créé par LunaNode.

Dans votre tableau de bord LunaNode, cliquez sur API en haut à droite. Cela ouvre une nouvelle page. Nous devons seulement définir un nom pour la clé API. Le reste sera pris en charge par LunaNode et ne sera pas couvert dans ce guide. Cliquez sur le bouton "Create API Credential".
Après avoir créé les identifiants API, vous obtenez une longue chaîne de lettres et de caractères. C'est votre clé API.

![image](assets/en/113.webp)

#### Comment déployer un nouveau serveur ?

Il y a 2 parties à ces identifiants, la clé API et l'ID API ; nous aurons besoin des deux. Avant de passer à l'étape suivante, ouvrons un second onglet dans le navigateur et allons sur https://launchbtcpay.lunanode.com/

Ici, il vous sera demandé de fournir votre clé API et votre ID API. Cela pour vérifier que c'est bien vous qui provisionnez ce nouveau serveur. La clé API devrait toujours être ouverte dans votre onglet précédent ; si vous faites défiler la table ci-dessous, vous trouverez l'ID API.

Revenez à la page avec le lanceur, remplissez les champs avec votre clé API et votre ID, et cliquez sur continuer.

![image](assets/en/114.webp)

Dans l'étape suivante, vous pouvez fournir un nom de domaine. Si vous possédez déjà un domaine et souhaitez l'utiliser pour BTCPay Server, assurez-vous d'ajouter également l'enregistrement DNS (appelé un enregistrement `A`) sur votre domaine. Si vous ne possédez pas de domaine, utilisez le domaine fourni par LunaNode à la place (vous pouvez modifier cela plus tard dans les paramètres de BTCPay Server) et cliquez sur Continuer.

Pour en savoir plus sur la configuration ou la modification d'un enregistrement DNS pour BTCPay Server ; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name

#### Lancer BTCPay Server sur LunaNode

Après avoir suivi les étapes précédentes, nous pouvons définir toutes les options pour notre nouveau serveur. Ici, nous sélectionnerons Bitcoin (BTC) comme devise prise en charge ; nous pouvons définir un e-mail pour être notifié des certificats de chiffrement pour des fins de renouvellement ; cela n'est pas obligatoire.
Ce guide vise à mettre en place un environnement Mainnet (Bitcoin dans le monde réel) ; cependant, LunaNode vous permet également de configurer cela pour Testnet ou Regtest à des fins de développement. Nous laisserons l'option Mainnet activée pour ce guide.
Choisissez votre implémentation Lightning. LunaNode propose deux implémentations différentes, LND et Core Lightning. Pour ce guide, nous choisirons LND. Il existe de petites mais réelles différences entre les deux implémentations ; pour en savoir plus, nous vous recommandons de lire la documentation extensive ; https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln

![image](assets/en/115.webp)

LunaNode propose plusieurs plans de Machine Virtuelle (VM). Ces plans diffèrent en termes de gammes de prix et de spécifications du serveur. Pour ce guide, un plan m2 suffira ; cependant, si vous avez sélectionné plus que Bitcoin comme monnaie, envisagez d'utiliser au moins un m4.

Accélérez la synchronisation initiale de la blockchain ; cela est optionnel et dépend de vos besoins. Il existe des options avancées comme définir un Alias Lightning, pointer vers une release spécifique sur GitHub, ou configurer des clés SSH ; aucune de ces options ne sera abordée dans ce guide.

Après avoir rempli le formulaire, vous devez cliquer sur Lancer VM, et LunaNode commencera à créer votre nouvelle VM, incluant BTCPay Server installé dessus. Ce processus prend quelques minutes ; une fois votre serveur prêt, LunaNode vous donne le lien vers votre nouveau BTCPay Server.

Après le processus de création, cliquez sur le lien vers votre BTCPay Server ; ici, il vous sera demandé de créer un compte Administrateur.

![image](assets/en/116.webp)

### Résumé des compétences

Dans cette section, vous avez appris :

- Créer et financer un compte sur LunaNode
- Utiliser le lanceur BTCPay Server pour créer votre propre serveur

### Évaluation des connaissances

#### Révision conceptuelle KA

Décrivez certaines des différences entre exécuter une instance de BTCPay Server sur un VPS et créer un compte sur une instance hébergée.

## Installer BTCPay Server sur un environnement Voltage

<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>

Vous vous familiariserez avec Voltage.cloud en tant que fournisseur d'hébergement, apprendrez les premières étapes d'utilisation de votre BTCPay Server, et découvrirez comment procéder avec le Lightning Network. Après avoir parcouru toutes les étapes, vous pourrez gérer une boutique en ligne ou une plateforme de financement participatif acceptant Bitcoin !

Ceci est l'une des nombreuses façons de déployer BTCPay Server. Lisez notre documentation pour plus de détails,
https://docs.btcpayserver.org.

### Déploiement de BTCPay Server - Voltage.cloud

D'abord, allez sur le site web Voltage.cloud et inscrivez-vous pour un nouveau compte. Lors de la création d'un compte, vous pouvez vous inscrire pour un essai gratuit de 7 jours. Cliquez soit sur le bouton Inscription en haut à droite, soit utilisez l'option "Essayer un essai gratuit de 7 jours" sur leur page d'accueil.

![image](assets/en/117.webp)

Après avoir créé un compte, cliquez sur le bouton `NODES` sur votre tableau de bord. Une fois que nous avons sélectionné Nodes et créé un nouveau nœud, nous sommes présentés avec les nœuds possibles que Voltage offre. Comme ce guide couvrira également LightningNetwork, chez Voltage, nous devons d'abord choisir notre implémentation Lightning avant de créer un BTCPay Server. Cliquez sur LightningNode.

![image](assets/en/118.webp)
Ici, vous devrez sélectionner le type de nœud Lightning que vous souhaitez. Voltage offre une variété d'options pour votre configuration d'éclairage. Cela diffère lors de la mise en place avec, par exemple, LunaNode. Pour l'intention de ce guide, un Lite Node sera suffisant. Lisez plus sur les différences sur Voltage.cloud.
![image](assets/en/119.webp)

Donnez un Nom à votre nœud, définissez un mot de passe et sécurisez ce mot de passe. Si ce mot de passe est perdu, vous perdez l'accès à vos sauvegardes, et Voltage ne peut pas le récupérer. Créez le nœud, et Voltage vous montre la progression. Voltage a créé votre nœud Lightning. Nous pouvons maintenant créer l'instance BTCPay Server et accéder directement au Lightning Network.

Cliquez sur Nodes en haut à gauche de votre tableau de bord. Ici, vous pouvez configurer la partie suivante de votre instance BTCPay Server. Cliquez sur "créer nouveau" une fois que vous êtes dans l'aperçu des nœuds. Vous obtenez un écran similaire à celui d'avant. Maintenant, au lieu de Lightning Node, nous choisissons BTCPay Server.

Voltage vous montre la géolocalisation de votre BTCPay Server, Voltage héberge dans la région Ouest des États-Unis. Ici, vous verrez également le coût d'hébergement du serveur. Cliquez sur Créer et donnez un nom à votre BTCPay Server. Activez Lightning et Voltage vous montre le nœud Lightning créé à l'étape précédente. Cliquez sur Créer, et Voltage créera une instance BTCPay Server.

![image](assets/en/120.webp)

Après avoir cliqué sur créer, Voltage vous présente le nom d'utilisateur et le mot de passe par défaut. Ceux-ci sont similaires à votre mot de passe défini précédemment dans Voltage. Cliquez sur le bouton Se connecter au compte pour être redirigé vers votre BTCPay Server.

Bienvenue dans votre nouvelle instance BTCPay Server. Comme nous avons déjà configuré Lightning lors du processus de création, il vous montre que Lightning est déjà activé !

### Résumé des compétences

Dans ce chapitre, vous avez appris :

- Créer un compte sur Voltage.cloud
- Étapes pour faire fonctionner BTCPay Server avec un nœud Lightning sur le compte

### Évaluation des connaissances

#### Révision conceptuelle KA

Quelles sont quelques différences clés entre les configurations Voltage et LunaNode ?

## Installer BTCPay Server sur un nœud Umbrel

<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>

À la fin de ces étapes, vous pouvez accepter des paiements lightning pour votre magasin BTCPay sur votre réseau local. Ce processus s'applique également si vous exécutez un nœud umbrel dans un restaurant ou une entreprise. Si vous souhaitez connecter ce magasin à un site web public, suivez l'exercice avancé pour exposer votre nœud umbrel au public.

https://umbrel.com/

![image](assets/en/121.webp)

### Déploiement BTCPay Server - Umbrel

Après que votre nœud Umbrel ait été complètement synchronisé avec la blockchain Bitcoin, allez dans l'Umbrel App Store et recherchez BTCPay Server sous Apps.

![image](assets/en/122.webp)

Cliquez sur BTCPay Server pour voir les détails de l'App. Quand les détails de BTCPay Server sont ouverts, en bas à droite, sont affichées les exigences pour que l'App fonctionne correctement. Il est indiqué qu'elle nécessite un nœud Bitcoin et Lightning. Si vous n'avez pas installé le nœud Lightning sur votre Umbrel, cliquez sur Installer. Ce processus peut prendre quelques minutes.

![image](assets/en/123.webp)

Après avoir installé votre nœud Lightning :

1. Cliquez sur ouvrir dans les détails de l'app ou sur l'App dans le tableau de bord d'Umbrel.
2. Cliquez sur configurer un nouveau nœud ; on vous montrera 24 mots pour la récupération de votre nœud Lightning.
3. Notez-les.

![image](assets/en/124.webp)
Umbrel demandera une vérification des mots que vous venez de noter. Après la configuration du nœud Lightning, retournez au magasin d'applications Umbrel et trouvez BTCPay Server. Cliquez sur le bouton d'installation, et Umbrel affichera si les composants requis sont installés et que BTCPay Server nécessite l'accès à ces composants. Après l'installation, cliquez sur Ouvrir en haut à droite des détails de l'application ou ouvrez BTCPay Server via le tableau de bord de votre Umbrel.
Umbrel demandera une vérification des mots que vous venez de noter.

![image](assets/en/125.webp)

**!?Note!?**

Assurez-vous de les stocker dans un endroit approprié, comme appris précédemment avec le stockage des clés.

Après la configuration du nœud Lightning, retournez au magasin d'applications Umbrel et trouvez BTCPay Server. Cliquez sur le bouton d'installation, et Umbrel affichera si les composants requis sont installés et que BTCPay Server nécessite l'accès à ces composants.

![image](assets/en/126.webp)

Après l'installation, cliquez sur Ouvrir en haut à droite des détails de l'application ou ouvrez BTCPay Server via le tableau de bord de votre Umbrel.

![image](assets/en/127.webp)

### Résumé des compétences

Dans cette section, vous avez appris :

- Les étapes pour installer BTCPay Server avec la fonctionnalité Lightning sur un nœud Umbrel

### Évaluation des connaissances

#### Révision conceptuelle KA

Comment la configuration sur Umbrel diffère-t-elle des deux options hébergées précédentes ?

# Conclusion

<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>



## Évaluez ce cours
<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>
<isCourseReview>true</isCourseReview>

## Conclusion du cours

<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

![image](assets/en/128.webp)

Vous devriez également avoir une compréhension générale de ce qu'est Bitcoin, comment il fonctionne, et comment il peut évoluer avec des secondes couches comme le Lightning Network. Dans ce cours, nous avons couvert de manière approfondie comment n'importe qui peut utiliser BTCPay Server, de l'installation initiale à la création de magasin et la gestion complexe des factures, pour devenir un individu ou un commerçant financièrement souverain.

Félicitations pour avoir terminé ce cours. Nous espérons que vous avez apprécié le contenu et que vous continuerez à utiliser et explorer BTCPay Server, et que vous êtes aussi enthousiaste à propos de l'avenir prometteur que Bitcoin et la communauté grandissante de bâtisseurs et de participants apporteront.

> **FOSS est inévitable.**

### Glossaire

| Terme                                           | Définition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 51% Attack                                      | L'acte de construire intentionnellement une nouvelle chaîne de blocs la plus longue pour remplacer les blocs dans la blockchain. Cela vous permet de remplacer les transactions qui ont été minées dans la blockchain. Ce type d'attaque est plus facile à réaliser lorsque vous avez la majorité de la puissance de minage, c'est pourquoi elle est appelée une « Attaque Majoritaire » ou une « Attaque à 51% ».                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| AccountKey                                      | La clé de compte à rebaser                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| AccountKeyPath                                  | Le chemin de la racine à la clé de compte est préfixé par l'empreinte de la clé publique maîtresse.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Adresse                                         | Les adresses Bitcoin codent de manière compacte les informations nécessaires pour payer un destinataire. Une adresse moderne se compose d'une chaîne de lettres et de chiffres qui commence par bc1 et ressemble à bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4. Une adresse est une abréviation pour le script de verrouillage d'un destinataire, qui peut être utilisé par un expéditeur pour signer et transférer des fonds au destinataire. La plupart des adresses représentent soit la clé publique du destinataire, soit une forme de script définissant des conditions de dépense plus complexes. L'exemple précédent est une adresse bech32 codant un programme témoin verrouillant les fonds à l'empreinte d'une clé publique (Voir Pay-to-Witness-Public-Key-Hash). Il existe également d'anciens formats d'adresse qui commencent par 1 ou 3 et qui utilisent le codage d'adresse Base58Check pour représenter les empreintes de clé publique ou les empreintes de script. |
| Type d'Adresse                                  | Une adresse peut représenter plusieurs scripts différents. Les adresses sont codées et préfixées afin de transmettre leur type de script. Les adresses héritées utilisent Base58, et lorsqu'une adresse héritée est l'empreinte d'une clé publique, une adresse dite P2PKH, elle commence par un ‘1’. Moins fréquemment, une adresse héritée est l'empreinte d'un script, auquel cas elle commencera par un ‘3’. Actuellement, toutes les adresses SegWit sont codées en Bech32 et commencent par le préfixe ‘bc1’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| App                                             | BTCPay Server dispose de plugins qui peuvent fonctionner comme une application en soi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| BIP 329                                         | Exporter/importer les étiquettes de portefeuille                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| BIP49                                           | Définit le schéma de dérivation pour les portefeuilles HD utilisant le format de sérialisation P2WPKH-nested-in-P2SH (BIP 141) pour les transactions avec témoin séparé.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Adresse Bitcoin                                 | Chaîne alphanumérique où vous envoyez votre bitcoin, il "vit" désormais là-bas. C'est un identifiant, qui se compose d'une chaîne d'environ 33 lettres et chiffres combinés. Dans une version actuelle du protocole, une adresse commence par 1, 3, ou b. Avoir l'adresse d'un destinataire est une partie nécessaire pour initier une transaction Bitcoin. Les adresses Bitcoin sont générées à partir de clés publiques et plusieurs adresses peuvent être générées à partir d'un ensemble de clés publiques pour améliorer la confidentialité. Les adresses Bitcoin agissent tout comme les adresses email, si vous voulez envoyer un message, vous devez savoir où il va, de même pour le bitcoin. Avant d'envoyer une transaction Bitcoin, vous devez vous assurer que l'adresse du destinataire est exacte puisque les transactions Bitcoin sont irréversibles et vous pourriez envoyer des bitcoins à une adresse qui n'appartient pas au destinataire.                       |
| bitcoin versus Bitcoin                          | Bitcoin est le réseau monétaire, et bitcoin (en minuscule) est une unité monétaire sur le réseau Bitcoin. Vous utilisez la monnaie bitcoin ou un jeton pour effectuer des transactions sur un réseau Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Bloc                                            | Un bloc est une structure de données dans la blockchain Bitcoin qui se compose d'un en-tête et d'un corps de transactions Bitcoin. Le bloc est marqué d'un horodatage et s'engage vis-à-vis d'un bloc prédécesseur (parent) spécifique. Lorsqu'il est haché, l'en-tête du bloc fournit la preuve de travail qui rend la blockchain probabilistiquement immuable. Les blocs doivent adhérer aux règles imposées par le consensus du réseau pour étendre la blockchain. Lorsqu'un bloc est ajouté à la blockchain, les transactions incluses sont considérées comme ayant leur première confirmation.                                                                                                                                                                                                                                                                                                                                                                                  |
| Explorateur de Blocs                            | Un outil en ligne qui vous permet de rechercher des informations en temps réel et historiques sur une blockchain, y compris des données liées aux blocs, transactions, adresses, et plus encore.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Hash de Bloc                                    | Un hash de bloc est le hash SHA-256 des données du bloc, et est généralement représenté au format hexadécimal. Un hash de bloc peut être interprété comme un très grand nombre. Pour satisfaire à l'exigence de Preuve de Travail, un hash de bloc doit être inférieur à un certain seuil. Ainsi, tous les hashes de bloc commencent par une série de zéros suivie d'une chaîne alphanumérique. Certains blocs ont jusqu'à vingt zéros initiaux, tandis que les blocs plus anciens en ont aussi peu que huit. Le nombre de zéros requis démontre approximativement la difficulté du minage au moment de la publication du bloc.                                                                                                                                                                                                                                                                                                                                                      |
| Hauteur de Bloc                                 | Chaque bloc est numéroté dans un ordre croissant, en commençant par zéro.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Récompense de Bloc                              | Comprend la subvention de bloc (bitcoin nouvellement créé) et la somme de toutes les frais de transaction des transactions incluses dans le bloc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Taille de Bloc                                  | Chaque bloc a une quantité limitée de données qu'il peut contenir. Les données qui n'ont pas pu être insérées dans un certain bloc seront enregistrées dans l'un des blocs suivants. En ce qui concerne les blocs bitcoin, ils avaient une taille de bloc de 1 Mo, cependant, après un soft fork, la taille de bloc peut techniquement contenir jusqu'à 4 Mo de données.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Subvention de Bloc                              | La quantité de nouveau bitcoin créé dans chaque bloc. Chaque bloc qui est produit et ajouté à la blockchain permet au créateur du bloc de créer une certaine quantité de nouveau bitcoin. La subvention a commencé à 50 BTC par bloc, et est divisée par deux tous les 210 000 blocs ou environ tous les 4 ans.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Blockchain                                      | Un journal distribué, ou base de données, de toutes les transactions Bitcoin. Les transactions sont regroupées dans des mises à jour discrètes appelées blocs, limitées jusqu'à 4 millions d'unités de poids. Les blocs sont produits environ toutes les 10 minutes via un processus stochastique appelé minage. Chaque bloc inclut une "preuve de travail" informatiquement intensive. L'exigence de preuve de travail est utilisée pour réguler les intervalles de blocs et protéger la blockchain contre les attaques visant à réécrire l'histoire : un attaquant aurait besoin de surpasser la preuve de travail existante pour remplacer les blocs déjà publiés, rendant chaque bloc probabilistiquement immuable au fur et à mesure qu'il est enterré sous les blocs subséquents.                                                                                                                                                                                              |
| BTCPay Server Vault                             | Pour un équilibre optimal entre facilité d'utilisation, sécurité et confidentialité, il est recommandé d'utiliser BTCPay Server Wallet avec un portefeuille matériel. BTCPay Vault est conçu pour faire le lien entre le Hardware Wallet et BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Problème des Généraux Byzantins                 | Un problème de théorie des jeux qui décrit la difficulté pour des parties décentralisées d'arriver à un consensus sans se fier à une partie centrale de confiance. Le nom provient du scénario de plusieurs généraux assiégeant Byzance. Ils ont encerclé la ville, mais ils doivent décider collectivement quand attaquer. Si tous les généraux attaquent en même temps, ils gagneront, mais s'ils attaquent à des moments différents, ils perdront. Les généraux n'ont pas de canaux de communication sécurisés entre eux car tout message qu'ils envoient ou reçoivent peut avoir été intercepté ou envoyé de manière trompeuse par les défenseurs de Byzance. Comment les généraux peuvent-ils s'organiser pour attaquer en même temps ?                                                                                                                                                                                                                                         |
| Censure                                         | Contrôle sur les informations pouvant être transmises aux masses. En ce qui concerne bitcoin, la censure concerne la capacité d'arrêter la transaction par des tiers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Monnaie de Rendu                                | La portion de UTXOs retournée au portefeuille de l'expéditeur, généralement via une adresse différente. Équivaut à la somme des entrées moins le montant dépensé et les frais de transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Child Pays For Parent (CPFP)                    | Une technique d'augmentation de frais où un utilisateur dépense une sortie d'une transaction non confirmée à faible taux de frais dans une transaction enfant avec un taux de frais élevé afin d'encourager les mineurs à inclure les deux transactions dans un bloc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Coinbase Transaction                            | La toute première transaction de chaque bloc qui distribue la récompense de bloc et les frais de transaction à celui qui a miné le bloc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Coincidence of Wants                            | Un phénomène économique où deux parties détiennent chacune un objet que l'autre désire, elles échangent donc ces objets directement sans aucun intermédiaire monétaire.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Cold Storage                                    | Une manière de gérer des données sans être connecté à internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Cold Wallet                                     | Un type de portefeuille bitcoin qui stocke de manière sécurisée vos clés privées hors ligne, généralement sur un dispositif physique. Connu également sous le nom de portefeuille matériel, il protège votre bitcoin numérique des pirates en ligne en utilisant un dispositif semblable à une clé USB qui n'est pas connecté à internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Command Line Interface (CLI)                    | Interaction avec un dispositif ou un programme informatique avec des commandes d'un utilisateur ou client, et des réponses du dispositif ou programme, sous forme de lignes de texte.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Commitment Transaction                          | Une transaction d'engagement est une transaction Bitcoin, signée par les deux partenaires du canal, qui encode le solde le plus récent d'un canal. Chaque fois qu'un nouveau paiement est effectué ou transmis via le canal, le solde du canal se met à jour, et une nouvelle transaction d'engagement est signée par les deux parties. Important, dans un canal entre Alice et Bob, Alice et Bob conservent chacun leur propre version de la transaction d'engagement, qui est également signée par l'autre partie. À tout moment, le canal peut être fermé par Alice ou Bob s'ils soumettent leur transaction d'engagement à la blockchain Bitcoin. Soumettre une transaction d'engagement plus ancienne (périmée) est considéré comme une tricherie (c.-à-d., une violation du protocole) dans le Lightning Network et peut être pénalisé par l'autre partie, en réclamant tous les fonds du canal pour eux-mêmes, via une transaction de pénalité.                               |
| Confirmation                                    | Une fois qu'une transaction est incluse dans un bloc, elle a une confirmation. Dès qu'un autre bloc est miné sur la blockchain, la transaction a deux confirmations, et ainsi de suite. Six confirmations ou plus sont considérées comme une preuve suffisante qu'une transaction ne peut pas être inversée.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Crowdfund (CF)                                  | Un plugin par défaut de BTCPay Server permettant à un propriétaire de magasin de créer facilement un site web de financement participatif typique. Ils peuvent facilement définir un objectif, créer des avantages pour les contributions, et le personnaliser selon leurs besoins.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Cryptography                                    | Un système spécial, où le message original est modifié pour que seuls les destinataires prévus puissent le recevoir.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Dashboard                                       | La page d'accueil centrale de BTCPay Server. Elle offre un aperçu de toute l'activité d'un magasin, affichée à travers un certain nombre de tuiles récapitulatives.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Demo                                            | Fait référence à l'environnement virtuel dans lequel se déroulent les démos de logiciels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Deployment                                      | Le déploiement de logiciel englobe toutes les activités rendant un système logiciel disponible à l'usage. Le processus général de déploiement consiste en plusieurs activités interdépendantes avec des transitions possibles entre elles.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Chemin de dérivation                            | Un élément de données qui indique à un portefeuille hiérarchique déterministe (HD) comment dériver une clé spécifique au sein d'un arbre de clés. Les chemins de dérivation sont utilisés comme standard Bitcoin et ont été introduits avec les portefeuilles HD dans le cadre du BIP 32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Ajustement de la difficulté                     | Ajustement de la cible de difficulté, tous les 2016 blocs (environ toutes les deux semaines) pour essayer de garantir que les blocs sont minés une fois toutes les 10 minutes en moyenne. Cela crée donc un temps constant entre les blocs et une émission constante de nouveaux bitcoins dans le réseau (via la récompense de bloc).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Cible de difficulté                             | Utilisée dans le minage, c'est un nombre en dessous duquel doit se trouver le hash d'un bloc pour que le bloc soit ajouté à la blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Signature numérique                             | Une signature numérique est un schéma mathématique permettant de vérifier l'authenticité et l'intégrité de messages ou documents numériques. Elle peut être vue comme un engagement cryptographique dans lequel le message n'est pas caché.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Divisible                                       | Propriété d'un bien qui peut être divisé en montants plus petits sans perdre de valeur. Étant donné que les transactions économiques se produisent fréquemment en montants variables, une monnaie doit être divisible pour être largement utilisée dans une économie.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Docker                                          | Logiciel qui emballe le logiciel dans des unités standardisées appelées conteneurs qui contiennent tout ce dont le logiciel a besoin pour fonctionner, y compris les bibliothèques, les outils système, le code et l'environnement d'exécution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Double dépense                                  | Résultat de dépenser avec succès de l'argent plus d'une fois. Bitcoin protège contre la double dépense en vérifiant que chaque transaction ajoutée à la blockchain respecte les règles de consensus ; cela signifie vérifier que les entrées pour la transaction n'ont pas été précédemment dépensées.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Durable                                         | Propriété de l'argent, dans laquelle la monnaie peut maintenir son état original au fil du temps et résister à une utilisation répétée. Une monnaie durable doit être capable de survivre à d'éventuels dommages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Electrum                                        | Electrum est l'un des portefeuilles Bitcoin les plus populaires, créé en 2011.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Clé publique étendue (Xpub)                     | Clé publique étendue également connue sous le nom de Xpub, une clé publique qui fonctionne comme parent pour les clés dérivées du xpub en tant que fonctionnalité du portefeuille HD. Ce Xpub est un standard introduit dans le BIP 32. Les portefeuilles l'utilisent en coulisse pour dériver des clés publiques. Le partage du Xpub n'est pas conseillé contre, vos fonds ne seront pas directement à risque d'être déplacés, le xpub ne peut pas dériver de clés privées. L'avantage de partager un xpub pourrait être pour des fins de financement participatif dans BTCPay Server. Le xpub est partagé par des moyens en ligne, tandis que les clés privées restent hors ligne sur un HWW.                                                                                                                                                                                                                                                                                      |
| F.U.D.                                          | Abréviation de Fear, uncertainty and doubt (Peur, incertitude et doute) ; généralement évoquée intentionnellement afin de mettre un concurrent en position de désavantage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Frais                                           | Dans le contexte du Lightning Network, les nœuds factureront des frais de routage pour transférer les paiements d'autres utilisateurs. Les nœuds individuels peuvent définir leurs propres politiques de frais qui seront calculées comme la somme d'une base_fee fixe et d'un fee_rate qui dépend du montant du paiement. Dans le contexte de Bitcoin, l'expéditeur d'une transaction paie des frais de transaction aux mineurs pour inclure la transaction dans un bloc. Les frais de transaction Bitcoin n'incluent pas de frais de base et dépendent linéairement du poids de la transaction, mais pas du montant.                                                                                                                                                                                                                                                                                                                                                               |
| Fiat                                            | Monnaie émise par le gouvernement qui n'est pas adossée à une marchandise comme l'or.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Finite                                          | Se réfère à l'offre limitée de Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Fork                                            | Un changement apporté à un protocole ou à un morceau de code. Les forks sont généralement introduits pour mettre à niveau un projet. Dans la communauté open source, les forks existent parce que de nombreuses personnes choisissent de télécharger et d'exécuter le même logiciel à différents moments et ne mettent pas toujours à jour. Si deux utilisateurs téléchargent et exécutent la version 1 d'un logiciel, et que seul un utilisateur effectue la mise à jour lorsque la version 2 est publiée, l'utilisateur qui a mis à jour exécute un fork de la version 1.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Funding Transaction                             | Transaction utilisée pour ouvrir un canal de paiement. La valeur (en bitcoin) de la transaction de financement est exactement la capacité du canal de paiement. La sortie de la transaction de financement est un script multisignature 2 sur 2 (multisig) où chaque partenaire du canal contrôle une clé. De par sa nature multisig, elle ne peut être dépensée que par accord mutuel entre les partenaires du canal. Elle sera finalement dépensée par l'une des transactions d'engagement ou par la transaction de clôture.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Fungible                                        | Être quelque chose (comme de l'argent ou une marchandise) de nature telle qu'une partie ou une quantité peut être remplacée par une autre partie ou quantité égale pour payer une dette ou régler un compte.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Gap Limit                                       | Se réfère au nombre standard d'adresses publiques qui sont vérifiées pour les transactions dans la blockchain afin de calculer le solde d'un compte. Les transactions reçues sur une adresse au-delà de la limite de l'écart d'adresse ne sont pas détectées.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Genesis Block                                   | Premier bloc de la blockchain Bitcoin. Satoshi Nakamoto, le créateur de Bitcoin, a miné le bloc Genesis le 3 janvier 2009 et a inclus le titre du Financial Times de ce jour-là, “Chancellor on brink of second bailout for banks” (Chancelier au bord d'un second sauvetage pour les banques).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Github                                          | Une plateforme et un service basé sur le cloud pour le développement de logiciels et le contrôle de version utilisant Git, permettant aux développeurs de stocker et de gérer leur code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Gossip Protocol                                 | Les nœuds LN envoient et reçoivent des informations sur la topologie du Lightning Network grâce à des messages de gossip qui sont échangés avec leurs pairs. Le protocole de gossip est principalement défini dans BOLT #7 et définit le format des messages node_announcement, channel_announcement, et channel_update. Pour prévenir le spam, les messages d'annonce de nœud ne seront transmis que si le nœud a déjà un canal, et les messages d'annonce de canal ne seront transmis que si la transaction de financement du canal a été confirmée par le réseau Bitcoin. Habituellement, les nœuds Lightning se connectent avec leurs partenaires de canal, mais il est acceptable de se connecter avec tout autre nœud Lightning pour traiter les messages de gossip.                                                                                                                                                                                                           |
| Gresham's Law                                   | Loi affirmant que “la mauvaise monnaie chasse la bonne”. En d'autres termes, dans une économie où deux monnaies sont utilisées, les individus dépenseront la mauvaise monnaie, qui se dévalue constamment, et garderont la bonne monnaie, qui conserve sa valeur. Ainsi, la mauvaise monnaie dominera en termes de circulation et d'utilisation dans les transactions quotidiennes, tandis que la bonne monnaie dominera en termes d'épargne et d'investissement à long terme.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Halving                                         | Un événement qui réduit le taux d'émission de bitcoin de moitié tous les 210 000 blocs (environ tous les quatre ans).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Hard Fork                                       | Un changement de consensus qui n'est pas rétrocompatible. La rétro-incompatibilité survient lorsqu'un comportement précédemment invalide est rendu valide. Pour maintenir le consensus à travers un hard fork, tous les nœuds doivent être mis à niveau. Sinon, les anciens nœuds rejettent les transactions ou les blocs comme invalides selon les anciennes règles, tandis que les nœuds mis à niveau les acceptent comme valides. Pour cette raison, les hard forks sont évités à tout prix dans Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Hardware Wallet (HWW)                           | Un type spécial de portefeuille Bitcoin qui stocke les clés privées de l'utilisateur dans un dispositif matériel sécurisé.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Hash Function                                   | Une fonction de hachage cryptographique est un algorithme mathématique qui mappe des données de taille arbitraire à une chaîne de bits de taille fixe (un hash) et est conçue pour être une fonction à sens unique, c'est-à-dire une fonction qu'il est infaisable d'inverser. La seule façon de recréer les données d'entrée à partir de la sortie d'une fonction de hachage cryptographique idéale est de tenter une recherche par force brute des entrées possibles pour voir si elles produisent une correspondance.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Hash Rate                                       | Une mesure de combien de hachages les mineurs produisent cumulativement par seconde sur le réseau Bitcoin. Un seul hash est une tentative de créer une Preuve-de-Travail pour un bloc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Hot Wallet                                      | Un dispositif avec des connexions externes, en particulier à Internet. Un hot wallet est un portefeuille Bitcoin qui se connecte à Internet. Ces portefeuilles sont plus pratiques pour les dépenses de tous les jours, mais ne sont pas aussi sécurisés que les options de stockage à froid car ils interagissent avec Internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Initial Block Download (IBD)                    | Le processus de construction de la blockchain Bitcoin complète à partir de zéro. Lorsqu'un nouveau nœud est configuré et rejoint le réseau, il se connecte à d'autres nœuds et leur demande des blocs. Le nouveau nœud traite ces blocs et construit la blockchain jusqu'à ce qu'il soit à jour et synchronisé avec le réseau.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Invoice                                         | Un document commercial émis par un vendeur à un acheteur concernant une transaction de vente et indiquant les produits, les quantités et les prix convenus pour les produits ou services que le vendeur a fournis à l'acheteur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Know Your Customer (KYC)                        | Des lois destinées à empêcher que les institutions financières soient utilisées pour des transferts d'argent illicites en exigeant que tous les comptes financiers soient identifiables à des individus ou des organisations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Layer 2                                         | Un réseau construit au-dessus d'une blockchain, par exemple, le Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Legacy Address                                  | Les adresses Legacy utilisent Base58, et lorsqu'une adresse Legacy est le hash d'une clé publique, une adresse dite P2PKH, elle commence par un ‘1’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Lightning Network                               | Un protocole au-dessus de Bitcoin. Il crée un réseau de canaux de paiement qui permet le transfert de paiements sans confiance à travers le réseau avec l'aide de HTLCs et de routage en oignon. D'autres composants du Lightning Network sont le protocole de gossip, la couche de transport et les demandes de paiement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Liquidity                                       | Mesure de plusieurs caractéristiques du carnet d'ordres d'un actif particulier au sein d'un marché donné. La liquidité est un indicateur de l'impact qu'une grande commande aura sur le prix d'un actif. Un actif avec plus de liquidité a une profondeur de carnet d'ordres plus importante. Cela signifie qu'il sera capable d'absorber plus de commandes avec des mouvements de prix plus petits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Chaîne la Plus Longue                           | La chaîne de blocs qui a nécessité le plus d'effort pour être construite. Nom donné ainsi car intuitivement, une blockchain contenant plus de blocs aura nécessité plus d'énergie pour sa construction qu'une chaîne avec moins de blocs, mais plus précisément, c'est la chaîne qui a requis le plus de travail pour être produite, donc un meilleur nom aurait pu être "chaîne la plus lourde".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Chaîne Principale                               | Dans le contexte du Lightning Network, cela fait référence au réseau Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Moyen d'Échange                                 | Un type de bien qui facilite l'échange d'autres biens et services au sein d'une économie. Historiquement, des objets comme les coquillages, les perles et l'or ont été utilisés comme moyens d'échange.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Mempool                                         | Abréviation de "pool de mémoire", il s'agit d'un stockage temporaire pour les transactions qui ont été reçues par un nœud.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Mineur                                          | Un nœud engagé dans le processus de construction de la blockchain en ajoutant de nouveaux blocs par le processus de hachage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Minage                                          | Processus de construction d'un bloc à partir des transactions Bitcoin récentes puis de résolution d'un problème computationnel requis comme preuve de travail. C'est le processus par lequel le grand livre partagé de bitcoin (c.-à-d., la blockchain Bitcoin) est mis à jour et par lequel de nouvelles transactions sont incluses dans le grand livre. C'est également le processus par lequel de nouveaux bitcoins sont émis. Chaque fois qu'un nouveau bloc est créé, le nœud de minage recevra de nouveaux bitcoins créés dans la transaction coinbase de ce bloc.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Multisignature (multisig)                       | Un script qui nécessite plus d'une signature pour autoriser une dépense. Les canaux de paiement sont toujours codés comme des adresses multisig nécessitant une signature de chaque partenaire du canal de paiement. Dans le cas standard d'un canal de paiement à deux parties, une adresse multisig 2 sur 2 est utilisée.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Nœud                                            | Un ordinateur participant à un réseau. En particulier les réseaux Bitcoin ou Lightning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Sortie                                          | Paquet de bitcoins créé dans une transaction bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Verrou de Sortie                                | Un ensemble d'exigences placées sur une sortie. Ces exigences doivent être remplies pour pouvoir utiliser la sortie dans une transaction. L'exemple le plus courant est une simple exigence de possession de la clé privée.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Adresse P2SH                                    | Les adresses P2SH sont des encodages Base58Check du hachage sur 20 octets d'un script. Les adresses P2SH commencent par un "3". Les adresses P2SH cachent toute la complexité, de sorte que l'expéditeur d'un paiement ne voit pas le script.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Adresse P2WPKH                                  | Le format d'adresse "SegWit v0 natif", les adresses P2WPKH sont encodées en bech32 et commencent par "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Adresse P2WSH                                   | Le format d'adresse de script "SegWit v0 natif", les adresses P2WSH sont encodées en bech32 et commencent par "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Transaction Bitcoin Partiellement Signée (PSBT) | Une norme Bitcoin qui facilite la portabilité des transactions non signées, permettant ainsi à plusieurs parties de signer facilement la même transaction. Cela est particulièrement utile lorsque plusieurs parties souhaitent ajouter des entrées à la même transaction. PSBT a été introduit par le BIP 174, et permet aux utilisateurs de signer plus facilement des transactions sur un dispositif de stockage à froid puis de diffuser la transaction signée depuis un dispositif connecté à Internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Cheminement                                     | Le processus de recherche d'un chemin pour un paiement de la source à la destination dans le Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Pay-to-Public-Key-Hash (P2PKH)                  | P2PKH est un type de sortie qui verrouille des bitcoins sur le hash d'une clé publique. Une sortie verrouillée par un script P2PKH peut être déverrouillée (dépensée) en présentant la clé publique correspondant au hash et une signature numérique créée par la clé privée correspondante.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Pay-to-Script-Hash (P2SH)                       | P2SH est un type de sortie polyvalent qui permet l'utilisation de scripts Bitcoin complexes. Avec P2SH, le script complexe qui détaille les conditions pour dépenser la sortie (script de rachat) n'est pas présenté dans le script de verrouillage. Au lieu de cela, la valeur est verrouillée au hash d'un script, qui doit être présenté et satisfait pour dépenser la sortie.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Pay-to-Taproot (P2TR)                           | Activé en novembre 2021, Taproot est un nouveau type de sortie qui verrouille des bitcoins à un arbre de conditions de dépense, ou à une condition racine unique.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Pay-to-Witness-Public-Key-Hash (P2WPKH)         | P2WPKH est l'équivalent SegWit de P2PKH, utilisant un témoin séparé. La signature pour dépenser une sortie P2WPKH est placée dans l'arbre des témoins au lieu du champ ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Pay-to-Witness-Script-Hash (P2WSH)              | P2WSH est l'équivalent SegWit de P2SH, utilisant un témoin séparé. La signature et le script pour dépenser une sortie P2WSH sont placés dans l'arbre des témoins au lieu du champ ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Payjoin                                         | Un type spécial de transaction Bitcoin où à la fois l'expéditeur et le destinataire contribuent des entrées afin de briser l'heuristique de propriété d'entrée commune, une hypothèse utilisée pour retirer la confidentialité des utilisateurs de bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Canal de Paiement                               | Une relation financière entre deux nœuds sur le Lightning Network, créée en utilisant une transaction bitcoin payant une adresse multisignature. Les partenaires du canal peuvent utiliser le canal pour envoyer des bitcoins l'un à l'autre sans enregistrer toutes les transactions sur la blockchain Bitcoin. Dans un canal de paiement typique, seulement deux transactions, la transaction de financement et la transaction d'engagement, sont ajoutées à la blockchain. Les paiements envoyés à travers le canal ne sont pas enregistrés dans la blockchain et sont dits se produire "hors chaîne".                                                                                                                                                                                                                                                                                                                                                                            |
| Demande de Paiement                             | Une fonctionnalité qui permet aux propriétaires de magasins BTCPay de créer des factures de longue durée. Les fonds versés à une demande de paiement utilisent le taux de change au moment du paiement. Cela permet aux utilisateurs de faire des paiements à leur convenance sans avoir à négocier ou vérifier les taux de change avec le propriétaire du magasin au moment du paiement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Paiement                                        | La fonctionnalité de paiement est liée aux Paiements Pull. Cette fonctionnalité vous permet de traiter des paiements pull (remboursements, paiements de salaires ou retraits).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Plugin                                          | Un add-on logiciel qui est installé sur un programme, améliorant ses capacités.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Point de Vente (PoS)                            | Un plugin par défaut de BTCPay Server permettant à un propriétaire de magasin de créer un webshop directement à partir de BTCPay Server. Le propriétaire du magasin n'a pas besoin de solutions de commerce électronique tierces pour gérer un webshop.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Portable                                        | Capacité d'un bien à être facilement transporté dans l'espace. La portabilité est une caractéristique importante de la monnaie solide ; pour qu'une monnaie soit largement adoptée, et donc utilisable, elle doit pouvoir se déplacer facilement à travers les frontières, entre les individus et sur de longues distances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Proof Of Work (PoW)                             | Données qui nécessitent un calcul significatif pour être trouvées, et qui peuvent être facilement vérifiées par quiconque pour prouver la quantité de travail qui a été nécessaire pour les produire. Dans Bitcoin, les mineurs doivent trouver une solution numérique à l'algorithme SHA-256 qui répond à un objectif fixé par le réseau, appelé la cible de difficulté.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Pseudonym                                       | Un faux nom utilisé par des individus pour protéger leur identité ou construire une réputation indépendante de leur véritable identité. Les clés publiques sont utilisées pour permettre aux utilisateurs de Bitcoin de recevoir des bitcoins tout en restant pseudonymes vis-à-vis de la blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Public-Key Cryptography                         | Implique une paire de clés connue sous le nom de clé publique et clé privée, qui sont associées à une entité qui doit authentifier son identité électroniquement ou pour signer ou chiffrer des données. La clé publique est publiée et la clé privée correspondante est gardée secrète. Les données qui sont chiffrées avec la clé publique ne peuvent être déchiffrées qu'avec la clé privée correspondante.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Public/Private Key                              | Paire de clés utilisée dans la cryptographie à clé publique. La clé publique est partagée avec d'autres ouvertement, et peut être considérée comme un numéro de compte, tandis que la clé privée est gardée secrète et peut être considérée comme un mot de passe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Pull Payment                                    | Traditionnellement, pour effectuer un paiement Bitcoin, un destinataire partage son adresse bitcoin et l'expéditeur envoie ensuite de l'argent à cette adresse. Un tel système est appelé paiement par poussée car l'expéditeur initie le paiement tandis que le destinataire peut être indisponible, poussant ainsi le paiement au destinataire. Au lieu du scénario typique d'un expéditeur "poussant" le paiement, l'expéditeur permet au destinataire de tirer le paiement au moment jugé opportun par le destinataire.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Rabbit Hole                                     | Une référence à Alice au pays des merveilles où le héros se lance dans une aventure en entrant dans un terrier de lapin. Dans Bitcoin, cela fait référence aux sujets apparemment sans fin que l'on explore et voit sous un nouveau jour une fois qu'on a commencé à comprendre Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Receive                                         | Le processus de réception de bitcoin envoyé à une adresse fournie.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Register                                        | Le processus de création d'un compte ou d'inscription à un service généralement effectué en choisissant un nom d'utilisateur et un mot de passe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Replace By Fee (RBF)                            | Une transaction Bitcoin peut être désignée comme RBF afin de permettre à l'expéditeur de remplacer cette transaction par une autre transaction similaire qui paie des frais plus élevés. Ce mécanisme existe pour permettre aux utilisateurs de réagir si le réseau devient congestionné et que les frais augmentent de manière inattendue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Repository                                      | Dans les systèmes de contrôle de version, un dépôt est une structure de données qui stocke les métadonnées pour un ensemble de fichiers ou une structure de répertoire. Selon que le système de contrôle de version utilisé est distribué, comme Git ou Mercurial, ou centralisé, comme Subversion, CVS ou Perforce, l'ensemble des informations dans le dépôt peut être dupliqué sur le système de chaque utilisateur ou peut être maintenu sur un seul serveur. Certaines des métadonnées qu'un dépôt contient incluent, entre autres, un historique des modifications dans le dépôt, un ensemble d'objets de validation, et un ensemble de références aux objets de validation, appelés têtes.                                                                                                                                                                                                                                                                                    |
| Rescan                                          | Processus de balayage de l'état actuel de l'ensemble UTXO pour les pièces appartenant à un schéma de dérivation préalablement configuré.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Revokation Key                                  | Chaque Contrat de Maturité de Séquence Révocable (RSMC) contient deux clés de révocation. Chaque partenaire de canal connaît une clé de révocation. Connaissant les deux clés de révocation, la sortie du RSMC peut être dépensée dans le délai prédéfini. Lors de la négociation d'un nouvel état de canal, les anciennes clés de révocation sont partagées, révoquant ainsi l'ancien état. Les clés de révocation sont utilisées pour décourager les partenaires de canal de diffuser un ancien état de canal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Routing                                         | Le processus d'utilisation du chemin du Lightning Network pour effectuer un paiement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Routing Fees                                    | Dans le Lightning Network, frais facturés pour le transfert des paiements d'autres utilisateurs. Les nœuds individuels peuvent définir leurs propres politiques de frais qui seront calculées comme la somme d'une base_fee fixe et d'un fee_rate qui dépend du montant du paiement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Salability                                      | La facilité avec laquelle un bien peut être vendu sur le marché lorsque son détenteur le souhaite, avec la moindre perte de son prix.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Satoshi (sat)                                   | Un satoshi est la plus petite unité (dénomination) de bitcoin pouvant être enregistrée sur la blockchain. Un satoshi équivaut à un cent-millionième (0,00000001) de bitcoin et porte le nom du créateur du Bitcoin, Satoshi Nakamoto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Satoshi Nakamoto                                | Le nom utilisé par la personne ou le groupe de personnes qui a conçu Bitcoin et créé sa mise en œuvre de référence originale. Dans le cadre de la mise en œuvre, ils ont également conçu la première base de données blockchain. Dans ce processus, ils ont été les premiers à résoudre le problème de la double dépense pour la monnaie numérique. Leur véritable identité reste inconnue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Satoshi Per Byte                                | Une unité pour mesurer la priorité de transaction, définie par les frais de la transaction en satoshi divisés par la taille de la transaction en octets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Satoshi Per Verabyte                            | Concept similaire à Satoshi Per Byte, mais pour les adresses plus récentes utilisant Segwit. Équivaut à la taille de la transaction en unités de poids divisée par 4. Les unités de poids sont calculées en prenant la taille de la transaction (sans le témoin) fois 3, ajoutée à la taille de la transaction incluant le témoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Scarcity                                        | Propriété d'un bien qui ne peut pas être reproduit sans coût. La rareté ne dépend pas du nombre d'unités existantes d'un bien, mais plutôt du coût de production de plus d'unités.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Script                                          | Bitcoin utilise un système de script pour les transactions appelé Bitcoin Script. Ressemblant au langage de programmation Forth, il est simple, basé sur une pile et traité de gauche à droite. Il est délibérément Turing-incomplet, sans boucles ni récursion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Seed Phrase                                     | Une liste de mots qui stocke toutes les informations nécessaires pour récupérer les fonds Bitcoin sur la chaîne. Le logiciel de portefeuille générera généralement une phrase de récupération et instruira l'utilisateur de la noter sur papier. Si l'ordinateur de l'utilisateur tombe en panne ou si son disque dur devient corrompu, il peut télécharger à nouveau le même logiciel de portefeuille et utiliser la sauvegarde papier pour récupérer ses bitcoins.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Segregated Witness (SegWit)                     | Segregated Witness (SegWit) est une mise à niveau du protocole Bitcoin introduite en 2017 qui ajoute un nouveau témoin pour les signatures et autres preuves d'autorisation de transaction. Ce nouveau champ témoin est exempté du calcul de l'ID de transaction, ce qui résout la plupart des classes de malléabilité de transaction par des tiers. Segregated Witness a été déployé comme un soft fork et est un changement qui rend techniquement les règles du protocole Bitcoin plus restrictives.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Self-Sovereignty                                | Un modèle de gestion des identités numériques dans lequel les individus ou les entreprises ont la propriété exclusive sur la capacité de contrôler leurs comptes et données personnelles.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Send                                            | Le processus de transfert de bitcoin vers une adresse.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Sensitivity Mode                                | Activé via un basculeur dans les paramètres du magasin, l'activation entraîne l'obscurcissement des valeurs numériques (par exemple, quantité de bitcoin) dans toutes les vues.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Server Settings                                 | Paramètres au sein de BTCPay Server qui s'appliquent à l'échelle du serveur (par opposition aux paramètres de magasin qui sont limités à un seul magasin).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| SHA-256                                         | Une fonction de hachage cryptographique. Membre d'une famille de fonctions de hachage appelées fonctions Secure Hashing Algorithm (SHA).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Shopify                                         | Une entreprise multinationale canadienne de commerce électronique dont le siège est à Ottawa, Ontario. Shopify est le nom de sa plateforme de commerce électronique propriétaire pour les boutiques en ligne et les systèmes de point de vente au détail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| SMTP                                            | Simple Mail Transfer Protocol est un protocole de communication standard de l'Internet pour la transmission de courrier électronique.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Soft Fork                                       | Une mise à niveau du protocole qui est compatible vers l'avant et vers l'arrière, permettant ainsi aux anciens nœuds et aux nouveaux nœuds de continuer à utiliser la même chaîne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Software Stack                                  | En informatique, une pile de solutions ou pile logicielle est un ensemble de sous-systèmes ou composants logiciels nécessaires pour créer une plateforme complète de sorte qu'aucun logiciel supplémentaire n'est nécessaire pour soutenir les applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Store                                           | Un magasin au sein de BTCPay Server peut être vu comme un "foyer" pour un portefeuille bitcoin spécifique, s'étendant avec toutes les fonctionnalités de BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Store Settings                                  | Paramètres au sein de BTCPay Server spécifiques à un magasin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Taproot                                         | Mise à niveau de Bitcoin qui introduirait plusieurs nouvelles fonctionnalités. La mise à niveau est décrite dans les BIPs 340, 341 et 342, et introduit le schéma de signature Schnorr, Taproot et Tapscript. Ensemble, ces mises à niveau introduisent de nouvelles façons plus efficaces, flexibles et privées de transférer des bitcoins.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Thier's Law                                     | Loi qui stipule que la bonne monnaie chassera la mauvaise monnaie.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Third-Party Host                                | Lorsqu'un site Web pour un individu ou une entreprise est hébergé sur des serveurs possédés et gérés par une autre entreprise. L'alternative est d'avoir votre site Web hébergé sur vos serveurs dans votre propre centre de données.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Timelock                                        | Un timelock est un type d'entrave qui restreint la dépense de certains bitcoins jusqu'à un moment ou une hauteur de bloc spécifié(e) dans le futur. Les timelocks jouent un rôle important dans de nombreux contrats Bitcoin, y compris les canaux de paiement et les HTLCs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Topologie                                       | La topologie du Lightning Network décrit la forme du Lightning Network comme un graphe mathématique. Les nœuds du graphe sont les nœuds Lightning (participants au réseau/peers). Les arêtes du graphe sont les canaux de paiement. La topologie du Lightning Network est diffusée publiquement avec l'aide du protocole de gossip, à l'exception des canaux non annoncés. Cela signifie que le Lightning Network peut être significativement plus grand que le nombre annoncé de canaux et de nœuds. Connaître la topologie est particulièrement intéressant dans le processus de routage basé sur la source des paiements où l'expéditeur découvre un itinéraire.                                                                                                                                                                                                                                                                                                                  |
| Transaction                                     | Les transactions sont des structures de données utilisées par Bitcoin pour transférer des bitcoins d'une adresse à une autre. Plusieurs milliers de transactions sont agrégées dans un bloc, qui est ensuite enregistré (miné) sur la blockchain. La première transaction de chaque bloc, appelée transaction coinbase, génère de nouveaux bitcoins.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Transaction ID                                  | Une chaîne de lettres et de chiffres qui identifie une transaction spécifique sur la blockchain. La chaîne est simplement le double hash SHA-256 d'une transaction. Ce hash peut être utilisé pour rechercher une transaction sur un nœud ou un explorateur de blocs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Authentification à Deux Facteurs (2FA)          | Une méthode de sécurité de gestion d'identité et d'accès qui nécessite deux formes d'identification pour accéder aux ressources et aux données, souvent avec un dispositif secondaire en plus du mot de passe de connexion standard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Incensurable                                    | Propriété selon laquelle aucune entité n'a la capacité d'annuler une transaction Bitcoin ou de mettre sur liste noire un portefeuille ou une adresse.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Insaisissable                                   | Propriété selon laquelle aucune entité ne peut prendre des bitcoins à une entité contre son gré.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Outputs de Transaction Non Dépensés (UTXO)      | Outputs qui n'ont pas encore été dépensés, donc disponibles pour être utilisés dans de nouvelles transactions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Expérience Utilisateur (UX)                     | Comment un utilisateur interagit avec et expérimente un produit, système ou service. Cela inclut les perceptions d'une personne sur l'utilité, la facilité d'utilisation et l'efficacité.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Interface Utilisateur (UI)                      | Le point d'interaction et de communication homme-ordinateur dans un dispositif.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Vérifiable                                      | Propriété d'un bien qui peut être facilement différencié des imposteurs et des contrefaçons.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Virtuel                                         | Qui existe ou est simulé sur un ordinateur ou un réseau informatique.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Machine Virtuelle (VM)                          | En informatique, une machine virtuelle est la virtualisation ou l'émulation d'un système informatique. Les machines virtuelles sont basées sur des architectures informatiques et fournissent la fonctionnalité d'un ordinateur physique. Leurs implémentations peuvent impliquer du matériel spécialisé, des logiciels, ou une combinaison des deux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Serveur Privé Virtuel                           | Un serveur privé virtuel est une machine virtuelle vendue comme un service par un service d'hébergement Internet. Le terme "serveur dédié virtuel" a également un sens similaire. Un serveur privé virtuel exécute sa propre copie d'un système d'exploitation, et les clients peuvent avoir un accès de niveau superutilisateur à cette instance du système d'exploitation, leur permettant d'installer presque n'importe quel logiciel qui fonctionne sur cet OS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Volatilité                                      | Mesure du degré de variation du prix d'un actif au fil du temps. Les actifs qui connaissent de grands changements de prix régulièrement sont plus volatils, tandis que les actifs qui ont un prix plus stable sont moins volatils.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Portefeuille                                    | Les portefeuilles Bitcoin conservent les clés d'un utilisateur, lui permettant de recevoir des bitcoins, de signer des transactions et de vérifier le solde de son compte. Les clés privées et publiques contenues dans un portefeuille Bitcoin remplissent deux fonctions distinctes, mais sont liées dans leur création. Les portefeuilles Bitcoin contiennent les clés d'un utilisateur, et non ses bitcoins réels. Conceptuellement, un portefeuille est comme un trousseau de clés dans le sens où il détient de nombreuses paires de clés privées et publiques. Ces clés sont utilisées pour signer des transactions, permettant à un utilisateur de prouver qu'il possède des sorties de transaction sur la blockchain, c'est-à-dire ses bitcoins. Tous les bitcoins sont enregistrés sur la blockchain sous forme de sorties de transaction.                                                                                                                                 |
| Wasabi Wallet                                   | Un portefeuille Bitcoin open-source, non-custodial, axé sur la confidentialité pour Desktop qui implémente CoinJoin sans confiance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Portefeuille en Lecture Seule                   | Des portefeuilles Bitcoin qui vous permettent de suivre vos bitcoins en stockage à froid tout en désactivant la capacité de dépenser des fonds. Cela est dû au fait que les portefeuilles en lecture seule ne stockent ni n'utilisent de clés privées, et sont donc incapables d'autoriser des dépenses au nom de l'utilisateur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Baleine                                         | Dans le contexte de Bitcoin, une baleine est quelqu'un qui détient une grande quantité de bitcoins.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| White-Label                                     | Un produit white-label est un produit ou service produit par une entreprise que d'autres entreprises rebrandent pour le faire apparaître comme s'ils l'avaient fabriqué.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Livre Blanc                                     | Présente une nouvelle idée ou sujet de discussion. Le livre blanc de Bitcoin a introduit Bitcoin comme un "système de paiement électronique peer-to-peer" qui "ne nécessite aucun tiers de confiance". Satoshi Nakamoto a publié le livre blanc le 31 octobre 2008 à une liste de diffusion d'email de cryptographes et de cypherpunks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Wrapped Segwit                                  | Une implémentation de conception incluse dans la mise à niveau SegWit destinée à permettre aux portefeuilles et autres logiciels Bitcoin de prendre en charge plus facilement SegWit. Pour ce faire, les deux scripts SegWit natifs, P2WPKH et P2WSH, sont utilisés comme le "redeemScript" d'une transaction P2SH, produisant des types de script SegWit enveloppés P2SH-P2WPKH et P2SH-P2WSH respectivement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

![image](assets/fr/129.webp)
