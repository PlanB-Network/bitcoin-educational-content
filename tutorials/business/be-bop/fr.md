---
name: be-BOP
description: Guide pratique pour monétiser votre activité avec be-BOP
---

![cover-bebop](assets/cover.webp)

**be-BOP** est une plateforme de e-commerce pensée pour les entrepreneurs souhaitant vendre en ligne et hors ligne, en toute autonomie, tout en acceptant les paiements en Bitcoin, via un compte bancaire et en Cash. La solution est également utile pour tout type d’organisation souhaitant collecter des dons ou monétiser ses différentes activités.

La solution est simple, légère et autonome. Elle permet la création d’une boutique en ligne, même dans un environnement où les services financiers traditionnels sont limités ou absents. En effet, **be-BOP** a été conçue pour fonctionner efficacement avec ou sans accès aux banques, en utilisant Bitcoin comme infrastructure de paiement.

Dans ce tutoriel, nous allons vous accompagner pas à pas pour :

- Créer votre première boutique en ligne avec **be-BOP**
- Personnaliser votre vitrine et vos produits
- Configurer les moyens de paiement disponibles 
- Comprendre les bonnes pratiques pour vendre efficacement en ligne avec **be-BOP**

Ce tutoriel ne nécessite pas de compétences techniques avancées. Il s’adresse autant aux développeurs qu’aux artisans, commerçants, coopératives ou entrepreneurs souhaitant se lancer dans le commerce numérique de manière souveraine et résiliente.

## Les prérequis pour d’installer be-BOP sur votre propre serveur

Avant de commencer l’installation de be-BOP, assurez-vous de disposer de l’infrastructure technique suivante. Ce sont les éléments indispensables pour que la plateforme fonctionne correctement :

### Stockage compatible S3

be-BOP utilise un système de stockage pour gérer les fichiers (comme les images des produits). Ainsi, vous devez avoir accès à un service de type S3, tel que :

- [MinIO](https://min.io/) auto-hébergé
- Amazon S3 (AWS)
- Scaleway Object Storage

Il faudra configurer un bucket et fournir les informations suivantes :

- **S3_BUCKET** : nom du bucket
- **S3_ENDPOINT_URL** : lien d’accès à votre service S3
- **S3_KEY_ID** et S3_KEY_SECRET : vos identifiants d’accès
- **S3_REGION** : la région de votre service S3

### Base de données MongoDB en mode ReplicaSet

be-BOP utilise MongoDB pour stocker les données des boutiques, utilisateurs, produits, etc.

Vous avez deux options :

- Installer MongoDB en local avec le mode **ReplicaSet activé**
- Utiliser un service en ligne comme **MongoDB Atlas**

Vous aurez besoin des variables suivantes :

- **MONGODB_URL** : l’adresse de connexion à la base
- **MONGODB_DB** : le nom de la base de données

## Environnement Node.js

be-BOP fonctionne avec Node.js. Assurez-vous d’avoir **Node.js** version 18 ou une version supérieure ainsi que **Corepack** activé (nécessaire pour gérer les gestionnaires de paquets comme pnpm). La commande à exécuter est `corepack enable`

### Git LFS installé

Certaines ressources (comme les images lourdes) sont gérées via Git LFS (Large File Storage). Assurez-vous que Git LFS est bien installé sur votre machine avec la commande `git lfs install`. Une fois ces prérequis en place, vous serez prêt à passer à l’étape suivante : le **téléchargement** et la **configuration** de be-BOP.

**Note :** un guide technique pour le déploiement du logiciel est disponible sous un autre tutoriel. 

## Création du compte Super-Admin

Au tout premier démarrage de be-BOP, le logiciel propose la création d’un compte **Super Admin**. Ce dernier dispose de toutes les autorisations nécessaires pour gérer les fonctionnalités du back-office. Pour le créer, vous devez suivre les étapes suivantes : 

- Rendez-vous sur `votresiteweb/admin/login`
- Créez un compte super-admin en choisissant un identifiant et un mot de passe sécurisés
 
Ce compte vous permettra d’accéder à l’ensemble des fonctionnalités du back-office. Une fois créé, vous pouvez vous connecter en remplissant votre identifiant ainsi que votre mot de passe.

![login](assets/fr/001.webp)

## Configuration et sécurisation du Back-Office

Avant de configurer votre interface de connexion au back-office, vous devez créer un hash unique. Ce dernier permet d'avoir une protection contre les acteurs malveillants qui essaieraient de deviner le lien de connexion à votre interface admin. 

Pour créer le hash, allez dans `/admin/Settings`. Dans la section dédiée à la sécurisation (ex. « Admin hash »), définissez une chaîne unique (hash). Une fois enregistré, l’URL du back-office sera modifiée (par exemple : `/admin-votrehash/login`) afin de limiter l’accès aux personnes non autorisées.

![hash-login](assets/fr/002.webp)  

2.2. Activation du mode maintenance (si nécessaire)

Toujours dans /admin/Settings, (Settings > General via l'interface graphique) cochez l’option “enable maintenance mode” au bas de la page.

![maintenance-mode](assets/fr/003.webp)

Vous pouvez, le cas échéant, indiquer une liste d’adresses IPv4 autorisées (séparées par des virgules) pour permettre l’accès au front-office pendant la maintenance. Le back-office reste accessible pour les administrateurs.

![ip-bebop](assets/fr/004.webp)

## Configuration des communications 

Pour que be-BOP puisse envoyer des notifications (par exemple pour les commandes, les inscriptions ou les messages système), vous devez configurer au moins une méthode de communication. Deux options sont possibles : l’e-mail (SMTP) ou Nostr.

### Configuration SMTP (e-mail)

be-BOP peut envoyer des e-mails via un serveur SMTP. Il vous faut des identifiants SMTP valides, souvent fournis par un service d’email (ex. : Mailgun, Gmail, etc.).

Voici les informations à renseigner :

SMTP_HOST : l’adresse du serveur SMTP (ex. : smtp.mailgun.org)

SMTP_PORT : le port à utiliser (souvent 587 ou 465)

SMTP_USER : votre nom d’utilisateur (généralement une adresse e-mail)

SMTP_PASSWORD : votre mot de passe ou clé API

SMTP_FROM : l’adresse e-mail qui apparaîtra comme expéditeur


### Configuration Nostr
   
be-BOP permet l'envoi de notifications via le protocole Nostr, une infrastructure décentralisée de messagerie. Pour cela, vous devez générer ou fournir une clé privée Nostr (NSEC). Vous pouvez générer cette clé directement via l’interface de be-BOP, dans la section dédiée à Nostr. Lorsque ces éléments sont correctement configurés, be-BOP pourra envoyer automatiquement des messages et alertes à vos utilisateurs.

## Méthodes de paiement compatibles

be-BOP est compatible avec plusieurs solutions de paiement, ce qui vous permet d’offrir plus de flexibilité à vos clients. Voici ce dont vous avez besoin pour configurer le moyen de paiement qui vous convient le mieux.

### Bitcoin Onchain

be-BOP vous permet d’accepter des paiements Bitcoin directement sur la blockchain (on-chain), de manière simple et souveraine.

**Étapes de configuration :**

- Rendez-vous dans le menu **Payment Settings**
- Cliquez sur **Bitcoin Nodeless** pour accéder aux paramètres de paiement on-chain.
- Renseignez les champs suivants :

| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)

**Astuce :** Pour obtenir votre clé publique étendue (Zpub), vous pouvez consulter les paramètres avancés de votre portefeuille Bitcoin (Sparrow Wallet, BlueWallet, Specter, etc.). Assurez-vous que le portefeuille n’est **pas en lecture seule** si vous comptez utiliser l’historique des transactions.

### Lightning Network

be-BOP permet également d’accepter des paiements instantanés en Bitcoin grâce au Lightning Network. Deux options de configuration sont actuellement disponibles :

**Phoenixd**

Allez dans le menu `Payment Settings`, Cliquez sur `Phoenixd`

![phoenixd](assets/fr/006.webp)

Vous devrez ensuite renseigner **le mot de passe ou token d’authentification** qui permet de vous connecter à votre instance  Phoenixd, un backend développé par Acinq qui permet de gérer les paiements Lightning avec son propre nœud mais sans la complexité liée à la gestion de canaux de paiements. 

**Swiss Bitcoin Pay**

Si vous ne souhaitez pas gérer vous-même un nœud Lightning, **Swiss Bitcoin Pay** est une solution prête à l’emploi, simple à configurer et idéale pour commencer à accepter des paiements Lightning sans infrastructure complexe.

Étapes de configuration :

- Dans le menu “Payment Settings, cliquez sur `Swiss Bitcoin Pay`
- Connectez-vous à votre compte Swiss Bitcoin Pay (ou créez-en un si vous n’en avez pas encore).
- Renseignez la Clé API fournie par Swiss Bitcoin Pay puis cliquer sur `enregistrer`

Une fois terminé la configuration, be-BOP pourra automatiquement générer des factures Lightning pour vos clients, et vous recevrez les paiements directement sur votre compte Swiss Bitcoin Pay. Cette solution est idéale pour les utilisateurs qui veulent éviter la complexité technique d’un nœud personnel tout en acceptant des paiements rapides et à faibles frais.

![swissbtcpay](assets/fr/007.webp)

### PayPal

En plus de Bitcoin, be-BOP vous permet aussi d’accepter des paiements en monnaie fiduciaire via PayPal, une solution bien connue et largement utilisée à l’international.

Étapes de configuration :

- Allez dans le menu `Payment Settings`
- Cliquez sur `PayPal`
- Dans votre compte Paypal (section développeur), renseignez le `Client ID` ainsi que le `Secret`
- Sélectionnez la devise de votre choix (par exemple : **USD**, **EUR**, **XOF**, etc.)
- Cliquez sur `enregistrer` 

![paypal](assets/fr/008.webp) 

**Remarque :** Vous devez disposer d’un compte professionnel PayPal pour générer ces identifiants. Vous pouvez les obtenir via le portail  [développeur](https://developer.paypal.com)

### SumUp

Le logiciel intègre désormais la solution de paiement **SumUp**, permettant d’accepter les paiements par carte bancaire de manière simple, sécurisée et efficace. Pour bénéficier de cette fonctionnalité, il est indispensable de procéder à une configuration initiale. Voici les étapes à suivre, numérotées pour une mise en œuvre claire et progressive :

- Commencez par saisir votre **API Key**, une clé confidentielle fournie par SumUp lors de la création de votre compte développeur. Elle permet d’établir une connexion sécurisée entre votre compte SumUp et le logiciel.
- Remplissez le champ `Merchant Code` avec le code unique qui identifie votre commerce au sein de la plateforme SumUp. Ce code est essentiel pour associer les transactions à votre établissement.
- Dans le champ `Currency`, choisissez la devise principale que vous utilisez pour vos transactions (par exemple **EUR**, **USD**, **CDF**, etc.).
- Une fois tous les champs correctement renseignés, cliquez sur le bouton `Save` afin d’enregistrer les paramètres. Le système établira alors le lien avec votre compte SumUp, et votre logiciel sera prêt à accepter les paiements.

![payment-sumup](assets/fr/009.webp)

Après cette configuration, l'intégration de **SumUp** sera active et opérationnelle, vous permettant d'encaisser rapidement et de suivre vos transactions directement depuis le logiciel.

### Stripe

be-BOP propose également une intégration complète avec **Stripe**, l’une des plateformes de paiement en ligne les plus populaires. Stripe permet d’accepter des paiements en ligne via carte bancaire, portefeuille numérique et plusieurs autres méthodes de paiement. Voici les étapes à suivre pour l’activer :

- Saisissez la **clé secrète** (`Secret Key`) fournie dans le tableau de bord Stripe.
- Complétez le champ **Public Key**, également fourni par Stripe.
- Sélectionnez la **devise principale**.
- Enregistrez la configuration, puis cliquez sur `Save`.

![payment-stripe](assets/fr/010.webp)

⚠️ **Attention :** Il est indispensable de connaître le régime de TVA applicable à votre activité (ex. : vente sous TVA du pays du vendeur, exemption sous justification, ou vente au taux de TVA du pays de l’acheteur) afin de configurer correctement les options de facturation dans **be-BOP**.

## Configuration de devises

**be-BOP** permet une gestion avancée des devises et est adapté aux environnements multidevises et aux besoins comptables spécifiques. Pour assurer une cohérence dans les opérations financières et les rapports, il est essentiel de bien configurer les différentes monnaies utilisées dans le système. Voici les étapes à suivre pour effectuer cette configuration :

- Sélectionner la **devise principale** (`Main currency`)
- Choisir la **devise secondaire** (`Secondary currency`)
- Définir la **devise de référence** (`Price reference currency`)
- Indiquer la **monnaie comptable** (`Accounting currency`)

Une fois toutes les devises correctement configurées, le logiciel assurera une conversion automatique et précise lors des opérations multidevises, tout en maintenant une cohérence comptable rigoureuse.

![settings-currencies](assets/fr/011.webp)

## Configuration des accès de récupération via email ou Nostr

Toujours dans `/admin/settings`, via le module **ARM**, assurez-vous que le compte super-admin comporte une **adresse e-mail** ou une **npub de récupération**, facilitant ainsi la procédure en cas d’oubli du mot de passe.

![settings-users](assets/fr/012.webp)

## Configuration de la langue

Le logiciel offre la possibilité de fonctionner en plusieurs langues afin de s’adapter à un public international et améliorer l’expérience utilisateur. Pour activer la fonctionnalité multilingue, il est important de configurer les langues disponibles et d’en définir une **langue par défaut**.

![settings-languages](assets/fr/13.webp)

## Configuration de l’Interface et de l’Identité dans be-BOP

**be-BOP** offre aux créateurs tous les outils pour designer un site web. La première étape consiste à ouvrir, dans les paramètres, la partie `/Admin > Merch > Layout`. Commencez par configurer le **Top Bar**, la **Navbar**, ainsi que le **Footer**.

### Le Top Bar

La configuration du **Top Bar** permet de personnaliser l’identité visuelle de votre logiciel en affichant des informations clés dès la première ligne de l’interface. Cela contribue à renforcer la reconnaissance de votre marque et à fournir un contexte clair aux utilisateurs.

#### Étapes de configuration :

- **Renseigner le nom de la marque (Brand name)** : dans le champ `Brand name`, saisissez le nom de votre entreprise, organisation ou produit. Ce nom apparaîtra en haut de l’interface et représentera votre identité visuelle principale.
- **Indiquer le titre du site (Website title)** : le titre choisi doit résumer le but de la plateforme. Ce titre peut apparaître dans l’en-tête ou dans l’onglet du navigateur.
- **Ajouter la description du site (Website description)** : à ce niveau, il faut renseigner une brève description de votre initiative. Cette description aide à contextualiser l’outil pour les utilisateurs et peut aussi être utilisée à des fins SEO.

Une fois ces informations saisies, le **Top Bar** affichera une présentation claire, professionnelle et cohérente de votre solution.

#### Liens dans le Top Bar

La section `Links` du Top Bar vous permet d’ajouter des raccourcis vers des pages importantes de votre application ou de sites externes. Ces liens s’affichent directement dans la barre supérieure, offrant un accès rapide et structuré à vos utilisateurs.

#### Étapes de configuration :

- **Saisir le nom du lien (Text)** : dans le champ `Text`, écrivez le nom ou le libellé du lien tel qu’il apparaîtra (ex. : Accueil, Contact, Aide...).
- **Indiquer l’adresse du lien (Url)** : dans le champ `Url`, saisissez l’adresse complète de la page cible (interne ou externe).
- **Ajouter d’autres liens si nécessaire** : chaque ligne de configuration permet d’ajouter un lien supplémentaire avec les champs `Text` et `Url`.
- **Enregistrer les liens** : une fois tous les liens renseignés, cliquez sur le bouton `Add top bar link` pour les enregistrer.

Cette configuration vous permet d’offrir une navigation claire, fluide et accessible à travers les différentes sections de votre site web ou vers des ressources complémentaires.

![settings-topbar](assets/fr/014.webp)

### La Nav Bar

La section **Navbar** permet de configurer le menu principal de navigation de votre be-BOP, généralement situé sur le côté ou en haut de l’interface. Ce menu guide les utilisateurs vers les différentes pages ou fonctionnalités de l’application. La configuration des liens s’effectue de manière simple et intuitive. Voici comment procéder :

- **Saisir le nom du lien (`Text`)** : sur la ligne de configuration, commencez par remplir le champ `Text`. Il correspond au libellé du lien qui s'affiche dans la barre de navigation (exemples : *Tableau de bord*, *Utilisateurs*, *Paramètres*...).
- **Entrer l’adresse du lien (`Url`)** : à côté du champ `Text`, vous trouverez le champ `Url`. Dans ce dernier, saisissez l’adresse de la page vers laquelle le lien doit rediriger. Il peut s’agir d’une route interne ou d’un lien vers une page externe.
- **Ajouter plusieurs liens si nécessaire** : en dessous de la première ligne, de nouveaux champs `Text` et `Url` sont disponibles pour ajouter autant de liens que nécessaire. Chaque ligne représente un lien de navigation supplémentaire.
- **Enregistrer les liens** : une fois tous les éléments saisis, cliquez sur le bouton `Add nav bar link` pour enregistrer et afficher les résultats dans la barre de navigation.

Cette configuration permet de structurer efficacement l’accès aux différentes parties du logiciel, améliorant ainsi l’ergonomie et l’expérience utilisateur.

![navbar](assets/fr/015.webp)

### Le Footer

La section **Footer** vous permet de personnaliser le bas de page de votre logiciel, en y ajoutant des informations ou des liens utiles. Avant de configurer les liens, commencez par activer une option spécifique :

- **Activer l’affichage du label "Powered by be-BOP"** : activez le bouton `Display Powered by be-BOP` pour afficher cette mention dans le pied de page.
- **Saisir le nom du lien (`Text`)** : remplissez le champ `Text`, qui correspond au libellé du lien dans le footer (exemples : *Conditions*, *Confidentialité*, *Contact*...).
- **Indiquer l’adresse du lien (`Url`)** : dans le champ `Url`, entrez l’adresse de la page cible (interne ou externe).
- **Ajouter d’autres liens si nécessaire** : utilisez les lignes supplémentaires pour créer autant de liens que souhaité.
- **Enregistrer les liens** : cliquez sur le bouton `Add footer link` pour enregistrer les liens.

![footer](assets/fr/016.webp)

### Personnalisation visuelle

**⚠️ N’oubliez pas de définir les logos pour les thèmes clair et sombre, ainsi que le favicon, via** `Admin > Merch > Pictures`.

Voici comment personnaliser l’apparence de votre site :

#### Accéder à la section Pictures

Menu `Admin` > `Merch` > `Pictures`.

#### Ajouter une nouvelle image

Cliquez sur `New Picture`.

#### Choisir un fichier local

Cliquez sur `Choose Files`, puis sélectionnez une image depuis votre disque dur.

#### Sélectionner le fichier à importer

Double-cliquez sur l’image à importer (logo clair, logo sombre ou favicon).

#### Nommer l’image 

Remplissez le champ `Name of the picture`.
   
#### Ajouter l’image  

Cliquez sur `Add` pour finaliser l’importation.

![pictures](assets/fr/017.webp)

### Configuration de l’Identité du Vendeur

#### Paramétrage de l’identité

Accessible via `Admin > Identity` (ou `Settings > Identity`), cette section vous permet de configurer les informations administratives et légales de votre entreprise.

#### Informations légales

- **Business name** : nom officiel de l’entreprise.  
- **Business ID** : identifiant légal ou numéro d’enregistrement (RCCM, SIRET...).

#### Adresse professionnelle

- **Street** : adresse postale (rue, numéro…).  
- **Country** : pays.  
- **State** : province ou région.  
- **City** : ville.  
- **ZIP code** : code postal.

#### Informations de contact

- **Email** : adresse email professionnelle.  
- **Phone** : numéro de téléphone de l’entreprise.

#### Compte bancaire

- **Account holder name** : nom du titulaire du compte.  
- **Account holder address** : adresse du titulaire.  
- **IBAN** : numéro de compte international.  
- **BIC** : code SWIFT/BIC.

![bank-account](assets/fr/019.webp)

#### Facturation

- Cliquez sur `Fill with main shop informations` pour pré-remplir les données.  
- **Very-top-right issuer information** : champ pour les mentions légales/fiscales visibles sur les factures.  
- Cliquez sur `Update` pour enregistrer les modifications.

**Remarque :** vous pouvez également renseigner des informations complémentaires à afficher sur la facture, selon vos besoins.

![vat](assets/fr/019.webp)

![issuer-info](assets/fr/020.webp)

#### Adresse physique du magasin

Pour ceux ayant un magasin physique, ajoutez une adresse complète spécifique dans `Admin > Settings > Identity` ou une section dédiée. Cela permettra son affichage sur les documents officiels et dans le footer si nécessaire.

![seller-id](assets/fr/021.webp)

## Gestion des Produits

### Création d’un nouveau produit

Accédez à `Admin > Merch > Products` pour ajouter ou modifier un produit. Remplissez les champs suivants :

#### Informations de base

- **Product Name** : nom du produit (ex. : *T-shirt BOP édition limitée*).  
- **Slug** : identifiant URL sans espaces (ex. : `tshirt-bop-edition-limitee`).  
- **Alias** *(optionnel)* : utile pour l’ajout rapide au panier via un champ dédié.

![product-config](assets/fr/028.webp)

#### Tarification

- **Price Amount** : prix du produit (ex. : `25.00`).  
- **Price Currency** : devise (EUR, USD, BTC, etc.).  
- **Produits spéciaux** :
  - `This is a free product` : pour un produit gratuit.
  - `This is a pay-what-you-want product` : pour un produit à prix libre.

#### Options du produit

- **Produit simple (`standalone`)** : un seul ajout possible par commande (ex. : don, billet d’entrée).
- **Produit avec variations** :
  - Ne cochez pas `Standalone`.
  - Cochez `Product has light variations (no stock difference)`.
  - Ajoutez :
    - **Nom** (ex. : *Taille*),
    - **Valeurs** (ex. : S, M, L, XL),
    - **Différences de prix** si applicables (ex. : `+2 USD` pour XL).

![product-details](assets/fr/029.webp)

## Gestion du stock

### Options avancées lors de la création d’un produit (Stock, Livraison, Tickets, etc.)

#### Produit avec stock limité

Si votre produit n’est pas disponible en quantité illimitée, cochez `The product has a limited stock`. Cela active le suivi automatique des quantités restantes. Une fois cette case cochée, un champ apparaît pour indiquer le **stock disponible**.

Le système gère :

- **Stock réservé** → produits dans les paniers non encore payés  
- **Stock vendu** → produits déjà achetés

**Délai de réservation en panier** : Quand un client ajoute un produit à son panier, il est “réservé” pendant un temps limité. Vous pouvez modifier cette durée dans :  `Admin > Config > Réservation panier` (valeur en minutes)

#### Produit à livrer ?

Cochez `The product has a physical component that will be shipped to the customer's address`. Cela est utile pour tous les produits à envoyer physiquement (livres, t-shirts, etc.)

#### Autres options

- **Ticket** : cochez si le produit est un billet pour un événement  
- **Booking** : cochez si c’est un créneau de réservation (ex. : séance, rendez-vous)

![product-options](assets/fr/030.webp)

### Action Settings (tout en bas)

Cette section détermine **où** et **comment** le produit est visible et achetable :

| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Cochez uniquement les canaux que vous souhaitez utiliser.

## Création et personnalisation des pages CMS et des widgets

### Pages CMS obligatoires

Allez dans `Admin > Merch > CMS`. Vous verrez la liste des pages existantes et pourrez en ajouter avec **Add CMS page**.

Les pages CMS sont importantes pour :

- Informer vos visiteurs (ex. : conditions d’utilisation)
- Se conformer à la loi (ex. : politique de confidentialité)
- Expliquer certaines fonctionnalités de la boutique (ex. : collecte d’IP, TVA à 0%)

Vous pouvez ajouter d’autres pages selon vos besoins :

- À propos / Qui sommes-nous  
- Nous soutenir / Donations  
- FAQ  
- Contact  
- etc.

**Conseil** : Cliquez sur chaque lien ou icône pour modifier le **contenu**, le **titre**, ou la **visibilité SEO** de chaque page.

### Layout et éléments graphiques

Accédez à : `Admin > Merch > Layout`. Vous pouvez personnaliser les éléments visuels de votre site :

![product-options](assets/fr/032.webp)

#### Top Bar (barre supérieure)

- Modifier ou supprimer les liens (EX : ACCUEIL, QUI SOMMES-NOUS,…)
- Navigation entre les sections clés du site

#### Navbar (barre de navigation principale)

- Présente dans la partie grise sous la top bar
- Contient les accès rapides à : `Config`, `Payment Settings`, `Transaction`, `Node Management`, `Widgets`, etc.
- Réservée aux administrateurs

#### Footer (pied de page)

- Modifiable depuis `Admin > Merch > Layout`
- Contient : informations de contact, liens utiles, mentions légales…

#### Personnalisation des visuels

Allez dans :  `Admin > Merch > Pictures`

Vous pouvez :

- Changer le **logo principal**
- Modifier ou ajouter les **images** du layout

#### Description du site

Aussi modifiable dans `Pictures`, elle permet d’afficher un **résumé ou slogan** dans le header ou le footer selon le thème.

**Remarque :** cela vous permet d’ajuster l’apparence à votre identité de marque (éducative, commerciale ou communautaire).

### Intégration de widgets dans les pages CMS

Les **widgets** permettent d’enrichir vos pages CMS avec des éléments dynamiques ou visuels.

#### Création des widgets

Allez dans :  `Admin > Widgets`

Exemples de widgets disponibles :

- **Challenges** : défis ou missions  
- **Tags** : catégories ou mots-clés  
- **Sliders** : carrousels d’images  
- **Specifications** : tableaux de caractéristiques  
- **Forms** : formulaires (contact, feedback, etc.)  
- **Countdowns** : minuteurs  
- **Galleries** : galeries d’images  
- **Leaderboards** : classements d’utilisateurs

![widgets](assets/fr/033.webp)

#### Intégration dans les pages CMS

Utilisez des **shortcodes** dans le contenu de vos pages CMS :

| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Paramètres courants** :

- `slug` : identifiant unique du widget  
- `display=img-1` : image spécifique du produit  
- `width`, `height`, `fit` : dimensions et style de l’image  
- `autoplay=3000` : temps en ms entre deux slides

**Avantages** :

- Facile à insérer (copier-coller)
- Dynamique : toute modification du widget est reflétée automatiquement
- Ne nécessite pas de développeur

## Gestion des Commandes et du Reporting

### Suivi des commandes

Pour consulter et gérer les commandes passées, allez dans : `Admin > Transaction > Orders`

Vous y trouverez la **liste complète des commandes** effectuées sur votre site.

![orders](assets/fr/034.webp)

#### Visualisation et recherche

L’interface permet de rechercher et filtrer les commandes selon plusieurs critères :

- `Order Number` : numéro de la commande
- `Product alias` : identifiant ou nom du produit
- `Payment Mean` : méthode de paiement utilisée (carte, crypto, etc.)
- `Email` : email du client

Ces filtres facilitent la recherche rapide et la gestion ciblée.

#### Détail de chaque commande

En cliquant sur une commande, vous accédez à une fiche complète contenant :

- Les produits commandés  
- Les informations du client  
- L’adresse de livraison (si applicable)  
- Les notes éventuelles associées à la commande  

#### Actions possibles sur une commande

Vous pouvez :

- Confirmer la commande (si elle est en attente)  
- Annuler une commande (en cas de problème ou demande client)  
- Ajouter des **labels** (pour l’organisation interne)  
- Consulter / ajouter des **notes internes**  

**Remarque :** cette section est essentielle pour un bon suivi logistique et relation client.

### Reporting et export

Pour accéder aux statistiques de ventes et paiements :  
`Admin > Settings > Reporting`

![reporting](assets/fr/035.webp)

Vous y trouverez une vue d’ensemble de votre activité, sous forme de **rapports mensuels et annuels**.

#### Contenu des rapports

Les rapports sont divisés en sections :

- **Order Detail** : nombre de commandes, état (confirmées, annulées, en attente), évolution  
- **Product Detail** : produits vendus, quantités, produits populaires  
- **Payment Detail** : montants encaissés, répartition par méthode de paiement  

#### Exportation des données

Chaque section inclut un bouton **Export CSV**, qui permet de :

- Télécharger les données au format CSV  
- Les ouvrir dans Excel, Google Sheets, etc.  
- Les archiver pour usage administratif ou comptable  
- Les utiliser pour des rapports internes

**Remarque :** idéal pour le suivi de performance, la comptabilité et les présentations.

## Configuration de la Messagerie Nostr (optionnel)

![nostr-config](assets/fr/036.webp)

La plateforme prend en charge le protocole **Nostr** pour certaines fonctionnalités avancées :

- Notifications décentralisées  
- Connexion sans mot de passe  
- Interface d’administration légère

### Génération et ajout de la clé privée Nostr

Allez dans :  
`Admin > Node Management > Nostr`

- Cliquez sur **Créer une nsec** si vous n’en avez pas.  
- Le système peut la générer automatiquement.  
- Sinon, vous pouvez utiliser une clé déjà existante (ex. : depuis Damus ou Amethyst).

Ensuite :

- Copiez la clé `nsec`  
- Ajoutez-la dans votre fichier `.env.local` (ou `.env`) : ```env NOSTR_PRIVATE_KEY=VotreCléNsecIci

### Fonctionnalités activées avec Nostr

Une fois configuré, plusieurs fonctions sont disponibles :

**Notifications via Nostr**

- Envoyer des alertes en cas de commande, paiement, ou événement système
- Destinées aux administrateurs ou utilisateurs

**Interface d’administration légère**

- Accessible via un client Nostr
- Permet la gestion rapide (mobile-friendly)

**Connexion sans mot de passe**

- Login par lien sécurisé (envoyé via Nostr)
- Meilleure sécurité et fluidité pour l’utilisateur

## Personnalisation du Design et des Thèmes

Pour adapter l’apparence de votre boutique à votre charte graphique, rendez-vous dans : `Admin > Merch > Theme`

Vous y trouverez toutes les options pour **créer** et **configurer** un thème personnalisé.

### Création d’un thème

![theme](assets/fr/037.webp)

Lors de la création ou modification d’un thème, vous pouvez définir :

- **Couleurs** : pour les boutons, arrière-plans, textes, liens, etc.  
- **Polices** : choix des typographies pour titres, paragraphes, menus  
- **Styles graphiques** : bordures, marges, espacements, formes des blocs

### Sections personnalisables

Chaque partie du site peut être ajustée indépendamment :

- **Header** : barre de navigation supérieure  
- **Body** : contenu principal  
- **Footer** : bas de page  

**Remarque :** cette granularité permet d’assurer une cohérence entre le visuel du site et l’identité de votre marque.

### Activation du thème

Une fois le thème configuré :

- Cliquez sur **Save**
- Activez-le comme **thème principal** de la boutique

**Remarque :** le thème actif est celui qui sera visible par les visiteurs.

## Configuration des Templates d’E-mails

La plateforme permet de personnaliser les emails envoyés automatiquement aux utilisateurs. Rendez-vous dans : `Admin > Settings > Templates`

![emails-templates](assets/fr/038.webp)

### Création / édition des templates

Chaque email (confirmation de commande, mot de passe oublié, etc.) possède :

- **Subject** : le sujet de l’email (ex. : "Votre commande a été validée")  
- **HTML Body** : contenu en HTML affiché dans l’email

**Remarque :** vous pouvez insérer du texte, images, liens, etc.

### Utilisation de variables dynamiques

Pour rendre les emails dynamiques, insérez des variables comme :

- `{{orderNumber}}` : remplacé par le numéro réel de la commande  
- `{{invoiceLink}}` : lien vers la facture  
- `{{websiteLink}}` : URL de votre site

**Remarque :** ces balises sont automatiquement remplacées à l’envoi.

### Conseils avancés

- Créez des emails **responsive** pour une bonne lecture sur mobile  
- Ajoutez des **boutons d’action** (payer, télécharger, suivre une commande)  
- Testez vos emails en vous les envoyant à vous-même avant publication

## Configuration des Tags et Widgets Spécifiques

### Gestion des Tags

Les **tags** permettent de structurer et enrichir votre contenu. Pour y accéder : `Admin > Widgets > Tag`

![tags-config](assets/fr/039.webp)

### Création d’un tag

Renseignez les champs suivants :

- **Tag Name** : nom affiché du tag  
- **Slug** : identifiant unique (sans espace ni accent)  
- **Tag Family** : regroupe les tags par catégorie

![targsconfig](assets/fr/040.webp)

#### Familles disponibles :

- `Creators` : auteurs ou producteurs  
- `Retailers` : vendeurs ou points de vente  
- `Temporal` : périodes ou dates  
- `Events` : événements associés

### Champs optionnels

Ces champs permettent d’enrichir un tag comme s’il s’agissait d’une page de contenu :

- **Titre**  
- **Sous-titre**  
- **Contenu court**  
- **Contenu complet**  
- **CTAs** (boutons d'action)

### Utilisation des tags

Les tags peuvent être :

- Affectés à des produits  
- Intégrés dans des pages CMS avec une balise : [Tag=slug?display=var-1]

## Configuration des Fichiers Téléchargeables

Pour proposer des documents téléchargeables à vos clients : `Admin > Merch > Files`

### Ajout d’un fichier

1. Cliquez sur **New file**
2. Renseignez :
   - **Nom du fichier** (ex. : *Guide d’installation*)
   - **Fichier à charger** (PDF, image, Word…)

**Remarque :** une fois ajouté, la plateforme génère automatiquement un **lien permanent**.

### Utilisation du lien

Ce lien peut ensuite être inséré dans :

- Une **page CMS** (en tant que lien texte ou bouton)
- Un **e-mail client** (via un template)
- Une **fiche produit** (ex. : téléchargement de notice)

Il est idéal pour fournir *notices d’utilisation, guides techniques, fiches produits…* sans avoir besoin d’un hébergement externe.

## Nostr-bot

La plateforme propose une intégration avancée avec le protocole **Nostr**, via un bot automatisé.

Accédez à : `Node Management > Nostr`

### Fonctionnalités principales

#### Gestion des relais

- Ajouter ou retirer des **relays** utilisés par le bot  
- Optimiser la **portée** et la **fiabilité** des messages envoyés

#### Message d’introduction automatique

- Activez un message automatique à la **première interaction** utilisateur  
- Idéal pour :  
  - Présenter votre service  
  - Envoyer un lien utile (ex. : FAQ, contact, commande)

#### Certification de votre `npub`

- Ajoutez un **logo** et un **nom public**
- Associez un **domaine web vérifié**
- Améliore la crédibilité et la reconnaissance de votre identité Nostr

### Cas d’usage du Nostr-bot

- Envoi de **confirmations de commande**  
- Réponse automatique à des **événements (ex. nouvelle commande)**  
- Création d’une **interaction client décentralisée**

## Surcharge des Libellés de Traduction

be-BOP est multilingue (FR, EN, ES…), mais vous pouvez adapter les traductions à vos besoins.

Pour cela, rendez-vous dans : `Settings > Language`

### Chargement et modification

Les fichiers de traduction sont en JSON. Vous pouvez :

- **Télécharger** les fichiers de langue  
- **Modifier** les textes existants  
- **Ajouter** vos propres traductions

Lien vers les fichiers d’origine :  
[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)

**Exemple :** remplacer `Add to cart` par `Ajouter au panier` ou `Acheter`.

## Teamwork & Point of Sale (POS)

### Gestion des Utilisateurs et des Droits d’Accès

#### Création des rôles

Allez dans : `Admin > Settings > ARM`

Cliquez sur **Create a role** pour créer un rôle (ex. : `Super Admin`, `POS`, `Ticket checker`).

Chaque rôle contient :

- **write access** : accès en écriture  
- **read access** : accès en lecture  
- **forbidden access** : sections interdites

#### Création d’utilisateurs

Dans le même menu `Admin > Settings > ARM`, ajoutez un utilisateur avec :

- login  
- alias  
- email de récupération  
- (optionnel) `recovery npub` pour connexion via Nostr

Assignez un rôle défini précédemment.

![pos-users](assets/fr/045.webp)

Les utilisateurs **read-only** verront les menus en *italique* et ne pourront pas modifier les contenus.

## Configuration du Point of Sale (POS)

### Attribution du rôle POS

Pour qu’un utilisateur accède au POS, attribuez-lui le rôle `Point of Sale (POS)` dans : `Admin > Config > ARM`

Il pourra se connecter via l’URL sécurisée : `/pos` ou `/pos/touch`

### Fonctionnalités spécifiques POS

Be-BOP propose une interface dédiée aux ventes physiques (magasin, événement, etc.).

#### Ajout rapide via alias

Dans `/cart`, un champ permet d’ajouter un produit :

- En scannant un **code-barres** (ISBN, EAN13)  
- En entrant un **alias produit** manuellement

**Remarque :** le produit s’ajoute automatiquement au panier.

#### Moyens de paiement

Le POS prend en charge :

- Espèces  
- Carte bancaire  
- Lightning Network (crypto)  
- Autres selon configuration

Deux options avancées sont disponibles :

- **Exemption de TVA** : applicable sur justification (ONG, étrangers…)  
- **Réduction cadeau** : remise exceptionnelle avec commentaire obligatoire

#### Affichage côté client

L’URL `/pos/session` est prévue pour un **écran secondaire** (HDMI, tablette…) :

Affiche :

- Produits en cours  
- Montant total  
- Mode de paiement  
- Remises appliquées

**Remarque :** le client suit la commande en direct, pendant que le vendeur l’enregistre sur `/pos`.

### Résumé POS

| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Merci d'avoir suivi ce tutoriel avec attention.  

