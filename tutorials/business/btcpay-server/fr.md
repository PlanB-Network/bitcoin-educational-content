---
name: BTCPay Server
description: Accepter des paiements en BTC sans intermédiaire
---

![cover](assets/cover.webp)

![video](https://youtu.be/KqsM-n-e4aY)

BTCPay Server est un logiciel libre et open source créé par Nicolas Dorier permettant d’accepter des paiements en bitcoin sans intermédiaire. Conçu pour offrir autonomie et souveraineté financière, il s’installe sur son propre serveur et assure la gestion complète des transactions, depuis la facturation jusqu’à la validation des paiements on-chain ou via le Lightning Network, et la comptabilité. Il s'intègre facilement à des sites e-commerce (WooComerce, Shopify, etc.) ou peut être utilisé comme un terminal de paiement pour les commerces physiques (*POS*).

BTCPay Server constitue sans doute la solution la plus aboutie pour les commerçants souhaitant accepter le bitcoin. C’est le logiciel le plus complet et le plus robuste en matière de sécurité, de souveraineté et de confidentialité. En contrepartie, il est également le plus complexe à installer et à maintenir. Il existe également des alternatives plus simples : certaines sont entièrement custodiales, comme OpenNode, tandis que d’autres proposent un compromis intéressant entre simplicité d’utilisation et souveraineté, à l’image de Swiss Bitcoin Pay :

https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Ce tutoriel a justement pour objectif de vous guider pas à pas dans l’installation, la configuration et l’utilisation de BTCPay Server, afin de vous permettre de déployer une infrastructure de paiement sécurisée, indépendante et conforme à l’éthos de Bitcoin.

## Spécificités de BTCPay Server

Les solutions de point de vente Bitcoin centralisées, comme *OpenNode* par exemple, offrent une grande simplicité d’utilisation, mais reposent sur une entreprise tierce puisqu’elles ne peuvent pas être auto-hébergées et sont, la plupart du temps, propriétaires. Si elles facilitent la mise en place des paiements, elles impliquent des frais de commission et exposent leurs utilisateurs à davantage de risques qu’une solution comme BTCPay Server, aussi bien en matière de garde des fonds que de confidentialité.

BTCPay Server s’adresse aux commerçants en ligne ou physiques, aux associations et organismes à but non lucratif désireux de recevoir des dons en bitcoins. Il constitue également une solution idéale pour les porteurs de projets ainsi que pour les développeurs souhaitant obtenir un soutien direct de leur communauté.

Les spécificités de BTCPay Server résident dans :
- son **autonomie complète**,
- l’absence de procédure **KYC**,
- le **contrôle intégral des fonds**,
- la **suppression des frais de plateforme**.

En devenant votre propre processeur de paiement, vous éliminez toute dépendance à un tiers centralisé entre vous et vos clients. Vous pouvez ainsi accepter des paiements directement en bitcoins et générer des factures de paiement. Cela garantit que ni vous ni votre entreprise ne pourrez être bannis par qui que ce soit. Vous jouez à la fois le rôle de banque et de processeur de paiement, sans avoir à verser de commissions à un intermédiaire pour chaque transaction.

Les frais liés aux transactions **on-chain** demeurent, mais ils peuvent être réduits grâce à l’utilisation du réseau **Liquid** ou **Lightning**.

À cela s’ajoutent :
- Personnalisation complète de l’interface et des factures ;
- Prise en charge native de **Tor**, garantissant une confidentialité accrue ;
- Prise en charge du **crowdfunding**, du **POS** et des **boutons de paiement** ;
- Compatibilité avec de nombreuses devises ;
- Paiements Bitcoin directs et pair-à-pair ;
- Contrôle complet sur vos clés privées ;
- Confidentialité améliorée ;
- Sécurité renforcée ;
- Logiciel auto-hébergé ;
- Prise en charge de **SegWit** et du **réseau Lightning** ;
- Portefeuille interne, basé sur les nœuds, avec intégration de portefeuilles matériels.

## Installation et configuration de BTCPay Server

### Choisir son mode d’hébergement

BTCPay Server peut être installé de différentes manières. Selon vos besoins et vos ressources, trois options principales s’offrent à vous :
- **BTCPay Server hébergé par un tiers** : vous utilisez une plateforme qui héberge le service pour vous. C’est simple, mais généralement payant.
- **BTCPay Server auto-hébergé sur un serveur cloud** (par exemple via [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) ou tout autre fournisseur). C’est la solution recommandée pour la plupart des commerçants débutants.
- **BTCPay Server installé sur votre propre matériel (en local)** : sur un ordinateur, un mini-PC ou un Umbrel. Cette méthode est plus technique, mais offre une indépendance totale.

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Pour un commerçant débutant, le **déploiement sur un serveur cloud** est le meilleur compromis entre autonomie, simplicité et sécurité, sans devoir gérer toute l’infrastructure technique.

Plusieurs hébergeurs permettent un déploiement rapide de BTCPay Server. Parmi eux, **Voltage** s’impose comme une solution de référence pour les utilisateurs souhaitant une **infrastructure fiable**, **professionnelle** et **souveraine**.

### Créer une instance BTCPay Server sur Voltage

**Voltage** est une plateforme d’hébergement Bitcoin et Lightning clé en main qui permet de déployer instantanément votre propre BTCPay Server, sans configuration complexe ni maintenance du serveur.

Rendez-vous sur le [site officiel de Voltage](https://voltage.cloud).

![capture](assets/fr/03.webp)

Créez un **compte utilisateur** avec une adresse e-mail valide et un mot de passe fort.

![capture](assets/fr/04.webp)

Voltage offre un **essai gratuit de 7 jours**. À noter qu’après nos 7 jours d’essai gratuit, vous serez invité à souscrire à un abonnement fixe de **25 $ par mois** afin de continuer à **garder vos nœuds actifs**.

Une fois votre compte Voltage créé et votre première connexion effectuée, vous serez redirigé vers la page d’accueil, qui présente deux sections principales :
- Une section **Infrastructure** qui permet de gérer les nœuds Lightning, Bitcoin Core, BTCPay Server et d’autres services Bitcoin dans le cloud ;
- et une section **Paiements** qui vous permet d’accéder à l’API Lightning de Voltage pour intégrer des paiements Bitcoin dans des applications personnalisées.

Pour déployer votre instance **BTCPay Server**, cliquez sur **Accéder à l’infrastructure**. C’est ici que vous pourrez créer, gérer et superviser l’ensemble de vos services, dont votre nœud Bitcoin et votre serveur BTCPay.

#### Créer un groupe

Avant de pouvoir déployer un service, la plateforme vous invitera à **créer un groupe**. Un **groupe** (workspace) est un espace de travail qui regroupe tous vos services Bitcoin et Lightning (par exemple un nœud, un BTCPay Server, un explorateur, etc.). C’est un peu comme un dossier qui contient vos différents projets.

![capture](assets/fr/05.webp)

Dans le cadre de notre tutoriel, le groupe que nous avons créé portera le nom **Genesis**. Vous pouvez ajouter une image de profil si vous le souhaitez. Une fois que c'est fait, cliquez sur le bouton **Créer**. Vous pouvez inviter d'autres utilisateurs à rejoindre le groupe, voire changer le nom du groupe si vous le souhaitez.

Sur la page d’accueil du groupe, plusieurs options apparaissent :
- **Lightning Nodes** : pour déployer un nœud Lightning complet (LND) ;
- **Bitcoin Core Nodes** : pour lancer un nœud Bitcoin complet ;
- **BTCPay Server** : pour héberger une instance BTCPay prête à l’emploi ;
- **Nostr Accounts** : pour gérer des identités Nostr.

Activez la **double authentification (2FA)** pour sécuriser votre compte et vos services (le bouton est visible en rouge si elle est désactivée).

![capture](assets/fr/06.webp)

Cliquez sur **BTCPay Server** parmi les options, puis sur **Launch a BTCPay Store**.

![capture](assets/fr/07.webp)

Voltage vous proposera alors de **créer et configurer votre instance BTCPay Server** en choisissant un **nom de service** (1) et en activant selon votre convenance les paiements Lightning (2).

Vous aurez forcément besoin d'un nœud Lightning, si vous décidez d'accepter les paiements Lightning.

Si vous n’avez pas encore de nœud Bitcoin ou Lightning, Voltage vous proposera d’en créer un automatiquement.

Cliquez sur **Créer un nœud Lightning** (3) .

![capture](assets/fr/08.webp)

Une fois sur l'interface de création de votre nœud, vous aurez à choisir entre le plan **standard** et  le plan **professionnel**.

Vous pouvez créer un nœud réel (**Mainnet**) ou de test (**Testnet**). Cliquez ensuite sur le bouton **Continuer**.

![capture](assets/fr/09.webp)

Pour ce tutoriel, utilisons le plan standard. Entrez le **nom du nœud**, un **mot de passe** puis appuyez sur le bouton **Create**.

![capture](assets/fr/10.webp)

Après quelques instants, votre nœud sera opérationnel et vous pourrez ouvrir gratuitement un canal avec une capacité de réception de 500 000 sats.

![capture](assets/fr/11.webp)

Un peu plus en bas à droite, vous avez toutes les informations concernant votre nœud !

![capture](assets/fr/12.webp)

Maintenant que nous avons notre nœud Lightning qui tourne, retournons à l'installation de notre serveur BTCPay. À présent, vous pouvez cliquer sur le bouton **Create BTCPay**. 

![capture](assets/fr/13.webp)

Une page s’ouvrira avec vos identifiants par défaut, accompagnée d’un message vous invitant à modifier le mot de passe initial qui vous est attribué. Une fois cette étape terminée, cliquez sur le bouton **Login Now** (Se connecter) pour accéder à votre interface.

![capture](assets/fr/14.webp)

Ça y est ! Votre serveur BTCPay est prêt à être utilisé. Vous serez directement redirigé vers la page de connexion de votre serveur BTCPay.

![capture](assets/fr/15.webp)

Une fois connecté, configurez votre premier **magasin (Store)** :

- Donnez-lui un **nom**.

- Choisissez la **devise par défaut** (EUR, USD, CFA, etc.).

- Sélectionnez un **fournisseur de taux de change** (ex. CoinGecko).

![capture](assets/fr/16.webp)

Ensuite, vous serez redirigé vers le tableau de bord de votre magasin. Sur l'interface du tableau de bord, vous allez constater que le bouton **Créer votre boutique** est marqué en vert, puisque l'étape est déjà franchie.

![capture](assets/fr/17.webp)

Un peu plus bas nous avons le bouton **Configurer un portefeuille** et **Configurer un nœud Lightning**. Dans notre cas, nous nous sommes déjà connecté à un nœud Lightning qui tourne sur voltage. Donc on aura plus à le faire ici.

Nous allons donc passer à la configuration d’un portefeuille. Cliquez sur le bouton **Configurer un portefeuille**.

Puisque nous débutons la prise en main de BTCPay Server, nous allons connecter un portefeuille existant. Appuyez donc sur **Connecter un portefeuille existant**.

![capture](assets/fr/18.webp)

Vous devez ensuite choisir votre **méthode d’importation**. Parmi les options disponibles, sélectionnez **Entrer la clé publique étendue**.

![capture](assets/fr/19.webp)

En reliant un portefeuille existant, vous pouvez recevoir vos paiements **directement sur ce portefeuille externe**, sans que le serveur BTCPay ait accès à votre clé privée. Ainsi, même en cas de piratage du serveur ou de compromission de la clé publique (`xpub`), un attaquant pourrait consulter l’historique de vos transactions, mais il lui serait **impossible d’accéder à vos fonds**.

Une fois que vous cliquez sur le bouton **Entrer la clé publique étendue**, vous serez **redirigé** vers la page où vous devez fournir cette clé.

Allons maintenant récupérer la **clé publique étendue**.

### Connecter un portefeuille Bitcoin

Pour recevoir vos paiements, vous devez connecter un **portefeuille Bitcoin** à votre magasin. Pour cela, plusieurs options s’offrent à vous :

- **Portefeuille matériel** (Ledger, Trezor, Coldcard...) ;

- **Portefeuille logiciel** (Blockstream App, Ashigaru, Electrum, Sparrow...)

- **Portefeuille interne BTCPay Server** (non recommandé, car il est moins sécurisé et expose davantage vos fonds en cas de piratage du serveur).

Dans ce tutoriel, nous allons utiliser un **portefeuille logiciel**, plus accessible pour une première configuration. Vous pouvez choisir parmi de nombreuses applications compatibles : **Electrum**, **Phoenix**, **Zeus**, **Muun**, etc.

Pour la démonstration, nous utiliserons **Electrum**. Ouvrez **Electrum**, cliquez sur **Portefeuille**, puis sur **Informations** :

![capture](assets/fr/20.webp)

Ensuite, copiez la **clé publique maîtresse (xpub)**.

![capture](assets/fr/21.webp)

Une fois la clé publique maîtresse copiée, collez-la dans le champ prévu à cet effet sur la page BTCPay Server.

![capture](assets/fr/22.webp)

Après vérification, vous serez redirigé vers le tableau de bord de votre magasin.

![capture](assets/fr/23.webp)

### Générer un Point de Vente (PoS)

Une fois votre boutique et votre portefeuille configurés, vous pouvez désormais mettre en place un **Point de Vente (PoS)** pour commencer à recevoir des paiements Bitcoin directement de vos clients.

Cette fonctionnalité intégrée à **BTCPay Server** est idéale pour les **commerçants, artisans, restaurateurs ou prestataires de services** souhaitant accepter le Bitcoin **sans site web** ni compétences techniques particulières.

### À quoi sert le Point de Vente ?

Le **PoS** est une **interface de caisse simplifiée** qui agit comme un **terminal de paiement Bitcoin**.  
Il vous permet de :
- Créer un **menu de produits ou services** avec prix fixes.
- Générer une **facture instantanée avec QR code** à scanner.
- Partager une **URL de paiement** accessible sur smartphone, tablette ou ordinateur.

En d’autres termes, le PoS transforme votre BTCPay Server en une **interface de vente directe**, où chaque paiement est reçu **dans votre propre portefeuille Bitcoin**, sans intermédiaire.

### Configurer le PoS

Dans le tableau de bord BTCPay, cliquez sur **PLUGINS**, puis sur **Point de vente**.

Cliquez ensuite sur **Créer une nouvelle application PoS**. Cette action permet d’ajouter une **nouvelle application** à votre boutique BTCPay, comme si vous installiez un mini site de vente interne.

Une page s’ouvre pour la création de votre application. Définissez un **nom de l’application** : il s’agit d’un nom interne, visible uniquement depuis votre tableau de bord (ex. : _Boutique Chaussures_).

Cliquez sur **Créer** pour valider.

![capture](assets/fr/24.webp)

Une fois créée, vous serez redirigé vers la **page de configuration détaillée** du Point de Vente.

### Personnaliser votre interface de vente

Sur cette page, vous pouvez définir les éléments essentiels de votre PoS :

- **Nom de l’application** (nom interne de gestion, modifiable à tout moment).

- **Titre d’affichage** (ce que verront vos clients en haut de la page).

- **Style du point de vente** (le mode **Description** convient aux services ou prestations comme une coupe de cheveux ou un repas, tandis que le mode **Catalogue de produits** est idéal pour les boutiques proposant plusieurs articles).

- **Devise d’affichage** (choisissez **XOF**, **EUR** ou **USD** selon vos prix habituels).

- **Liste des articles** ( ici ajoutez vos produits, descriptions et prix).

![capture](assets/fr/25.webp)  

![capture](assets/fr/26.webp)

### Sauvegarder et tester votre PoS

Lorsque vous avez terminé la configuration, cliquez sur **Enregistrer** pour sauvegarder vos paramètres, puis sur **Voir** pour afficher un aperçu de votre PoS.

Vous verrez une page présentant vos produits, chaque bouton correspondant à un article ou service.

Dès qu’un client sélectionne un produit :

1. BTCPay génère automatiquement une **facture Bitcoin ou Lightning**.

2. Un **QR code** s’affiche à l’écran.

3. Le client peut **scanner et payer directement** avec son portefeuille Bitcoin.


![capture](assets/fr/27.webp)

### Résultat final

Vous disposez désormais d’un **Point de Vente Bitcoin complet** que vous pouvez :

- Ouvrir depuis un smartphone ou une tablette dans votre boutique ;

- Afficher sur un écran pour que le client scanne ;

- Ou partager via une **URL publique**, comme une page de commande simplifiée.

À chaque paiement, le montant est automatiquement crédité sur **votre propre portefeuille BTCPay**, sans intermédiaire ni frais tiers.  
Votre PoS devient ainsi un **terminal de paiement Bitcoin autonome**.


## Utilisation au quotidien

Avant d’encaisser de vrais paiements, il est recommandé d’effectuer **un test** pour vérifier que tout fonctionne correctement.

### Tester un paiement

- **Créez une facture** depuis votre interface PoS (par exemple, un produit à 1 satoshi ou une petite somme).

- **Scannez le QR code** affiché à l’écran à l’aide d’un portefeuille Bitcoin ou Lightning (comme **Phoenix**, **Muun** ou **Wallet of Satoshi**).


![capture](assets/fr/28.webp)

- **Validez le paiement** dans votre portefeuille : la transaction est envoyée instantanément.

- **Retournez dans BTCPay Server** : la facture apparaîtra comme **Payée** dans la liste.

![capture](assets/fr/29.webp)

Félicitations ! Votre Point de Vente est désormais **fonctionnel**. Vous pouvez commencer à recevoir des paiements Bitcoin de vos clients, simplement, rapidement et sans intermédiaire.

### Créer une facture pour un client

Dans le menu **Factures**, cliquez sur **Nouvelle facture**.

![capture](assets/fr/30.webp)

Entrez le **montant** et la **devise locale** (BTCPay calcule automatiquement l’équivalent en BTC), ainsi que les autres informations concernant le produit.

![capture](assets/fr/31.webp)

Partagez le **QR code** ou l’**URL** avec le client.    

![capture](assets/fr/32.webp)

### Suivre les paiements reçus

Toujours dans le menu **Factures**, vous verrez la liste de toutes vos transactions.  
Les statuts possibles sont :

- **En attente** : paiement non encore confirmé.

- **Réglée** : paiement confirmé.

- **Expirée** : facture non réglée dans le délai imparti.

### Rembourser un client

Dans le menu **Factures**, sélectionnez la facture à rembourser.

![capture](assets/fr/33.webp)

Cliquez sur **Rembourser** et saisissez l’adresse Bitcoin fournie par le client.

![capture](assets/fr/34.webp)  

![capture](assets/fr/35.webp)

### Rapports et exportation des données

BTCPay Server permet d’**exporter vos transactions** (au format CSV ou Excel). C’est très pratique pour votre comptabilité et votre suivi de caisse.

![capture](assets/fr/36.webp)

Dans le menu **Rapport**, cliquez sur **Exporter** : toutes vos transactions seront enregistrées dans un fichier CSV que vous pourrez ensuite consulter localement.

## Sécurité et Bonnes pratiques

L’autonomie que confère BTCPay Server (la pleine souveraineté sur vos fonds) constitue une véritable force. Mais cette liberté s’accompagne d’une responsabilité plus grande en matière de sécurité. En gérant vous-même vos paiements, vous endossez le rôle de votre propre banque. Il est donc impératif d’adopter de bonnes pratiques pour protéger vos fonds, vos données et votre infrastructure. Voici les principaux points à prendre en considération.

### Sécuriser l’accès à votre serveur

- Utilisez un mot de passe fort : combinez majuscules, minuscules, chiffres et caractères spéciaux. Évitez toute réutilisation d’un mot de passe existant.
- Activez l’authentification à deux facteurs (2FA) pour accéder à votre interface BTCPay.
- Mettez régulièrement à jour votre système d’exploitation, votre instance BTCPay Server et vos dépendances (Docker, nœud Bitcoin, nœud Lightning...). Les mises à jour corrigent souvent des vulnérabilités de sécurité.

### Gérer et sauvegarder les clés privées

- Sauvegardez vos clés privées et vos seedphrases hors ligne, sur un support physique (papier ou métal).
- Utilisez de préférence un portefeuille matériel (hardware wallet).
- Conservez plusieurs copies de vos sauvegardes, dans des lieux physiques distincts et protégés.

### Sécuriser les paiements et la confidentialité

- Utilisez le réseau Tor ou un VPN pour masquer l’adresse IP de votre serveur et protéger votre vie privée.
- Désactivez les ports non nécessaires sur votre serveur et limitez les connexions SSH aux seules adresses de confiance.
- Activez le HTTPS (certificat SSL) pour toutes les connexions à votre interface web BTCPay.
- Ne partagez jamais votre interface d’administration avec du personnel non formé à la gestion de portefeuilles Bitcoin.

### Mettre en place de bonnes pratiques pour le réseau Lightning

Votre boutique est connectée à un **nœud Lightning hébergé sur Voltage**, ce qui simplifie considérablement la gestion technique du réseau. Néanmoins, il reste important d’adopter **de bonnes pratiques de suivi et de sécurité** :

- **Sauvegardez les identifiants et clés d’accès API** de votre nœud Voltage (elles permettent à BTCPay de se connecter).
- **Protégez votre compte Voltage** avec une authentification à deux facteurs et un mot de passe fort.
- **Surveillez l’état du nœud et des canaux** depuis votre tableau de bord Voltage : cela vous aide à repérer toute anomalie ou désynchronisation.
- **Évitez de partager vos identifiants d’API** ou de les exposer publiquement (par exemple dans le code du site).
- En cas de migration, **reconfigurez simplement le lien entre BTCPay et Voltage** : aucun canal n’a besoin d’être fermé manuellement.

Grâce à Voltage, vous bénéficiez d’une infrastructure **sécurisée, hautement disponible** et **automatiquement sauvegardée**, tout en gardant la **pleine souveraineté sur vos paiements Lightning**.

### Organiser et structurer des procédures internes

- Définissez une politique claire de gestion des accès : qui peut créer une facture, consulter les paiements, accéder au nœud, etc.
- Consignez vos procédures de sauvegarde et de restauration afin de pouvoir réagir rapidement en cas d’incident.
- Testez régulièrement la restauration de vos sauvegardes pour vous assurer qu’elles fonctionnent correctement.
- Formez votre personnel ou vos collaborateurs à la sécurité opérationnelle de base : vigilance face au phishing, utilisation de mots de passe sécurisés, respect de la confidentialité.

### Superviser et établir une maintenance continue

- Surveillez en permanence l’activité de votre serveur via des outils de logs ou de monitoring.
- Planifiez une revue de sécurité périodique : vérifiez les mises à jour, les accès, les sauvegardes et la cohérence des transactions.

Félicitations! Vous êtes à la fin de ce tutoriel. Vous pouvez maintenant prendre en main BTCPay Server tout seul pour vous faciliter la tâche dans la gestion de votre boutique.

Pour aller plus loin, je vous recommande de suivre notre formation complète consacrée à l’intégration de Bitcoin au sein de votre entreprise :

https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a
