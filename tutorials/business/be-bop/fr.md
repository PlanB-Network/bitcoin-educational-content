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

### Environnement Node.js

be-BOP fonctionne avec Node.js. Assurez-vous d’avoir **Node.js** version 18 ou une version supérieure ainsi que **Corepack** activé (nécessaire pour gérer les gestionnaires de paquets comme pnpm). La commande à exécuter est `corepack enable`

### Git LFS installé

Certaines ressources (comme les images lourdes) sont gérées via Git LFS (Large File Storage). Assurez-vous que Git LFS est bien installé sur votre machine avec la commande `git lfs install`. Une fois ces prérequis en place, vous serez prêt à passer à l’étape suivante : le **téléchargement** et la **configuration** de be-BOP.

**Note :** un guide technique pour le déploiement du logiciel est disponible sous un autre tutoriel. 

## Création du compte Super-Admin

Au tout premier démarrage de be-BOP, le logiciel propose la création d’un compte **Super Admin**. Ce dernier dispose de toutes les autorisations nécessaires pour gérer les fonctionnalités du back-office. Pour le créer, vous devez suivre les étapes suivantes : 

- Rendez-vous sur `votresiteweb/admin/login`
- Créez un compte super-admin en choisissant un identifiant et un mot de passe sécurisés
 
Ce compte vous permettra d’accéder à l’ensemble des fonctionnalités du back-office. Une fois créé, vous pouvez vous connecter en remplissant votre identifiant ainsi que votre mot de passe.

![login](assets/fr/01.webp)

## Configuration et sécurisation du Back-Office

Avant de configurer votre interface de connexion au back-office, vous devez créer un hash unique. Ce dernier permet d'avoir une protection contre les acteurs malveillants qui essaieraient de déviner le lien de connexion à votre interface admin. 

Pour créer le hash, allez dans `/admin/Settings`. Dans la section dédiée à la sécurisation (ex. « Admin hash »), définissez une chaîne unique (hash).
Une fois enregistré, l’URL du back-office sera modifiée (par exemple : `/admin-votrehash/login`) afin de limiter l’accès aux personnes non autorisées.

![hash-login](assets/fr/02.webp)  

2.2. Activation du mode maintenance (si nécessaire)
Toujours dans /admin/Settings, (Settings > General via l'interface graphique) cochez l’option “enable maintenance mode” au bas de la page.

![maintenance-mode](assets/fr/03.webp)

Vous pouvez, le cas échéant, indiquer une liste d’adresses IPv4 autorisées (séparées par des virgules) pour permettre l’accès au front-office pendant la maintenance. Le back-office reste accessible pour les administrateurs.

![ip-bebop](assets/fr/04.webp)

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
   
be-BOP permet l'envoi de notifications via le protocole Nostr, une infrastructure décentralisée de messagerie.
Pour cela, vous devez générer ou fournir une clé privée Nostr (NSEC). Vous pouvez générer cette clé directement via l’interface de be-BOP, dans la section dédiée à Nostr.
Lorsque ces éléments sont correctement configurés, be-BOP pourra envoyer automatiquement des messages et alertes à vos utilisateurs.

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

![payment-nodeless](assets/fr/05.webp)

**Astuce :** Pour obtenir votre clé publique étendue (Zpub), vous pouvez consulter les paramètres avancés de votre portefeuille Bitcoin (Sparrow Wallet, BlueWallet, Specter, etc.). Assurez-vous que le portefeuille n’est **pas en lecture seule** si vous comptez utiliser l’historique des transactions.

### Lightning Network

be-BOP permet également d’accepter des paiements instantanés en Bitcoin grâce au Lightning Network. 
Deux options de configuration sont actuellement disponibles :

**Phoenixd**

Allez dans le menu `Payment Settings`
Cliquez sur `Phoenixd`

![phoenixd](assets/fr/06.webp)

Vous devrez ensuite renseigner **le mot de passe ou token d’authentification** qui permet de vous connecter à votre instance  Phoenixd, un backend développé par Acinq qui permet de gérer les paiements Lightning avec son propre nœud mais sans la complexité liée à la gestion de canaux de paiements. 

**Swiss Bitcoin Pay**

Si vous ne souhaitez pas gérer vous-même un nœud Lightning, **Swiss Bitcoin Pay** est une solution prête à l’emploi, simple à configurer et idéale pour commencer à accepter des paiements Lightning sans infrastructure complexe.

Étapes de configuration :

- Dans le menu “Payment Settings, cliquez sur `Swiss Bitcoin Pay`
- Connectez-vous à votre compte Swiss Bitcoin Pay (ou créez-en un si vous n’en avez pas encore).
- Renseignez la Clé API fournie par Swiss Bitcoin Pay puis cliquer sur `enregistrer`

Une fois terminé la configuration, be-BOP pourra automatiquement générer des factures Lightning pour vos clients, et vous recevrez les paiements directement sur votre compte Swiss Bitcoin Pay. Cette solution est idéale pour les utilisateurs qui veulent éviter la complexité technique d’un nœud personnel tout en acceptant des paiements rapides et à faibles frais.

![swissbtcpay](assets/fr/07.webp)

### PayPal

En plus de Bitcoin, be-BOP vous permet aussi d’accepter des paiements en monnaie fiduciaire via PayPal, une solution bien connue et largement utilisée à l’international.

Étapes de configuration :

- Allez dans le menu `Payment Settings`
- Cliquez sur `PayPal`
- Dans votre compte Paypal (section développeur), renseignez le `Client ID` ainsi que le `Secret`
- Sélectionnez la devise de votre choix (par exemple : **USD**, **EUR**, **XOF**, etc.)
- Cliquez sur `enregistrer` 

![paypal](assets/fr/08.webp) 

**Remarque :** Vous devez disposer d’un compte professionnel PayPal pour générer ces identifiants. Vous pouvez les obtenir via le portail  [développeur](https://developer.paypal.com)

### SumUp

Le logiciel intègre désormais la solution de paiement **SumUp**, permettant d’accepter les paiements par carte bancaire de manière simple, sécurisée et efficace.  
Pour bénéficier de cette fonctionnalité, il est indispensable de procéder à une configuration initiale. Voici les étapes à suivre, numérotées pour une mise en œuvre claire et progressive :

- Commencez par saisir votre **API Key**, une clé confidentielle fournie par SumUp lors de la création de votre compte développeur. Elle permet d’établir une connexion sécurisée entre votre compte SumUp et le logiciel.
- Remplissez le champ `Merchant Code` avec le code unique qui identifie votre commerce au sein de la plateforme SumUp. Ce code est essentiel pour associer les transactions à votre établissement.
- Dans le champ `Currency`, choisissez la devise principale que vous utilisez pour vos transactions (par exemple **EUR**, **USD**, **CDF**, etc.).
- Une fois tous les champs correctement renseignés, cliquez sur le bouton `Save` afin d’enregistrer les paramètres. Le système établira alors le lien avec votre compte SumUp, et votre logiciel sera prêt à accepter les paiements.

![payment-sumup](assets/fr/09.webp)

Après cette configuration, l'intégration de **SumUp** sera active et opérationnelle, vous permettant d'encaisser rapidement et de suivre vos transactions directement depuis le logiciel.

### Stripe

be-BOP propose également une intégration complète avec **Stripe**, l’une des plateformes de paiement en ligne les plus populaires.  
Stripe permet d’accepter des paiements en ligne via carte bancaire, portefeuille numérique et plusieurs autres méthodes de paiement. Voici les étapes à suivre pour l’activer :

- Saisissez la **clé secrète** (`Secret Key`) fournie dans le tableau de bord Stripe.
- Complétez le champ **Public Key**, également fourni par Stripe.
- Sélectionnez la **devise principale**.
- Enregistrez la configuration, puis cliquez sur `Save`.

![payment-stripe](assets/fr/010.webp)

> ⚠️ **Attention :** Il est indispensable de connaître le régime de TVA applicable à votre activité (ex. : vente sous TVA du pays du vendeur, exemption sous justification, ou vente au taux de TVA du pays de l’acheteur) afin de configurer correctement les options de facturation dans **be-BOP**.

## Configuration de devises

**be-BOP** permet une gestion avancée des devises et est adapté aux environnements multidevises et aux besoins comptables spécifiques.  
Pour assurer une cohérence dans les opérations financières et les rapports, il est essentiel de bien configurer les différentes monnaies utilisées dans le système. Voici les étapes à suivre pour effectuer cette configuration :

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

Le logiciel offre la possibilité de fonctionner en plusieurs langues afin de s’adapter à un public international et améliorer l’expérience utilisateur.  
Pour activer la fonctionnalité multilingue, il est important de configurer les langues disponibles et d’en définir une **langue par défaut**.

![settings-languages](assets/fr/13.webp)

## Comment designer votre site web

**be-BOP** offre aux créateurs tous les outils pour designer un site web.  
La première étape consiste à ouvrir, dans les paramètres, la partie `/Admin > Merch > Layout`.  
Commencez par configurer le **Top Bar**, la **Navbar**, ainsi que le **Footer**.

### Le Top Bar

La configuration du **Top Bar** permet de personnaliser l’identité visuelle de votre logiciel en affichant des informations clés dès la première ligne de l’interface. Cela contribue à renforcer la reconnaissance de votre marque et à fournir un contexte clair aux utilisateurs.

#### Étapes de configuration :

- **Renseigner le nom de la marque (Brand name)** : dans le champ `Brand name`, saisissez le nom de votre entreprise, organisation ou produit. Ce nom apparaîtra en haut de l’interface et représentera votre identité visuelle principale.
- **Indiquer le titre du site (Website title)** : le titre choisi doit résumer le but de la plateforme. Ce titre peut apparaître dans l’en-tête ou dans l’onglet du navigateur.
- **Ajouter la description du site (Website description)** : à ce niveau, il faut renseigner une brève description de votre initiative. Cette description aide à contextualiser l’outil pour les utilisateurs et peut aussi être utilisée à des fins SEO.

Une fois ces informations saisies, le **Top Bar** affichera une présentation claire, professionnelle et cohérente de votre solution.

### Liens dans le Top Bar

La section `Links` du Top Bar vous permet d’ajouter des raccourcis vers des pages importantes de votre application ou de sites externes. Ces liens s’affichent directement dans la barre supérieure, offrant un accès rapide et structuré à vos utilisateurs.

#### Étapes de configuration :

- **Saisir le nom du lien (Text)** : dans le champ `Text`, écrivez le nom ou le libellé du lien tel qu’il apparaîtra (ex. : Accueil, Contact, Aide...).
- **Indiquer l’adresse du lien (Url)** : dans le champ `Url`, saisissez l’adresse complète de la page cible (interne ou externe).
- **Ajouter d’autres liens si nécessaire** : chaque ligne de configuration permet d’ajouter un lien supplémentaire avec les champs `Text` et `Url`.
- **Enregistrer les liens** : une fois tous les liens renseignés, cliquez sur le bouton `Add top bar link` pour les enregistrer.

Cette configuration vous permet d’offrir une navigation claire, fluide et accessible à travers les différentes sections de votre site web ou vers des ressources complémentaires.

![settings-topbar](assets/fr/014.webp)






