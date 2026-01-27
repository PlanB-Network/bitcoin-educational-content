---
name: Peach
description: Guide complet pour utiliser Peach et échanger des bitcoins en P2P
---

![cover](assets/cover.webp)



## Introduction

Les échanges de pair-à-pair (P2P) sans KYC sont essentiels pour préserver la confidentialité et l'autonomie financière des utilisateurs. Ils permettent des transactions directes entre individus sans nécessiter de vérification d'identité, ce qui est crucial pour ceux qui valorisent la vie privée. Pour une compréhension plus approfondie des concepts théoriques, consultez le cours BTC204 :

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Qu'est-ce que Peach ?

Peach est une plateforme d'échange P2P qui permet aux utilisateurs d'acheter et de vendre des bitcoins sans KYC. Elle offre une interface intuitive et des fonctionnalités de sécurité avancées. Comparée à d'autres solutions comme Bisq, HodlHodl, et Robosat, Peach se distingue par sa simplicité d'utilisation.
Un système d'entiercement multisignature (2-2) garantit la sécurité des fonds lors des transactions. Peach prend en charge divers modes de paiement, et est constitué d'un systeme de réputation qui joue le rôle de guider les traders dans leurs actions. Comme à l'habitude dans les plateformes P2P, il est donc important de guarder un bonne réputation pour garder de la credibilité auprès d'autres traders.

### 2. Confidentialité et données Collectées

**Quelles informations Peach collecte-t-elle ?**

Peach s'efforce de stocker le minimum absolu de données sur ses utilisateurs. Voici un aperçu des données conservées sur ses serveurs :

- Un hash de votre identifiant unique d'application (AdID)
- Un hash de vos données de paiement
- Vos conversations chiffrées
- Les données des transactions pour s'assurer que les utilisateurs anonymes ne dépassent pas la limite de trading (types de méthodes de paiement utilisées, montants d'achat et de vente)
- Les adresses utilisées pour envoyer et recevoir depuis le compte séquestre
- Données d'utilisation (Firebase & Google Analytics), uniquement si vous y avez consenti

Pour rappel, un hash est une donnée rendue méconnaissable, similaire à un chiffrement. Les mêmes données produiront toujours le même hash, permettant de détecter les doublons sans connaître les données d'origine.

*Pour plus d'explications sur le hachage, vous pouvez suivre ce cours :*

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Qui peut voir mes détails de paiement ?**

- Seule votre contrepartie peut voir vos détails de paiement
- Les données sont transmises via les serveurs Peach, mais sont entièrement chiffrées de bout en bout
- En cas de litige, vos détails de paiement et l'historique des conversations seront visibles par le médiateur Peach assigné

## Installation et configuration

### 1. Installer l'application Peach

![Installation de Peach](assets/fr/01.webp)

- Téléchargez l'application depuis [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/). Sur iOS, vous devrez d'abord installer l'application [testflight](https://apps.apple.com/us/app/testflight/id899247664).
- Suivez les instructions d'installation sur votre appareil.
- Lors de l'installation, vous serez invité à choisir si vous souhaitez partager certaines données pour améliorer l'application Peach. (image 1)
- Sur l'écran suivant (image 2), vous aurez deux options : 
	- Si vous êtes un nouvel utilisateur, cliquez sur "New user" pour créer un nouveau profil
	- Si vous avez déjà un compte, utilisez "Restore" pour restaurer votre profil existant
- Si vous avez un code de parrainage, vous pouvez l'entrer à ce moment-là.
- Pour la restauration d'un compte existant (image 3), vous aurez besoin : 
	- De votre fichier de sauvegarde (backup)
	- Du mot de passe permettant de déchiffrer ce fichier

### 2. Présentation des Écrans Principaux

L'application Peach est organisée autour de quatre écrans principaux accessibles depuis la barre de navigation inférieure :

![Navigation dans l'application](assets/fr/02.webp)

- **Acceuil (4)** : L'écran principal d'ou vous pourrez choisir de vendre ou acheter, creer de nouvelles transactions et accéder aux offres disponibles.L'interface vous suggère deux manières d'interagir avec le marché:
	- créer des offres avec les deux bouton du dessu (create buy / create sell)
	- prendre les offres existantes créées par d'autres utilisateurs, avec les deux boutons du dessous ("Buy"/"Sell"). 

- **Wallet (5)** : Votre portefeuille bitcoin intégré qui vous permet de :
	- Consulter votre solde
	- Recevoir des bitcoins
	- Envoyer des bitcoins (avec coin control)
	- Voir l'historique de vos transactions
	- Financer vos ventes

- **Trades (6)** : vos contrats présents et passés, sous trois onglets:
	- Achats en cours
	- Ventes en cours
	- L'historique de vos échanges

- **Paramètres (7)** : Le hub de configuration permettant de
	- Visualiser votre profil (reputation, badges, limites, etc.)
	- Gerer la securité (backup, pin)
	- Gérer vos méthodes de paiement
	- Contacter du support
	- Changer de langue
	- etc..

### 3. Configurer ses moyens de paiements

![Accès aux paramètres de paiement](assets/fr/03.webp)

Vous pouvez gerer vos méthodes de payments dans les paramètres (image 8)

Peach propose des payments en ligne, et des payements en face-à-face (uniquement dans les meetups enregistrés).

**Paiements en ligne**

**Important :**
 afin de protéger les utilisateurs, Peach requière que la provenance des fonds corresponde à celle annoncée. C'est aux traders de s'assurer que ce soit le cas, pour leur propre protection.

![Configuration des paiements en ligne](assets/fr/04.webp)

Pour ajouter une méthode :
- Dans l'onglet "en ligne", cliquez sur "ajouter une devise/methode"
- Choisissez votre devise
- Sélectionnez votre méthode de paiement préférée

*Types de méthodes de paiement disponibles :*

***Pour les virements bancaires :***
- SEPA (standard ou instantané)
- Remplissez vos coordonnées bancaires SEPA.

***Les portefeuilles en ligne acceptés :***
- Plusieurs options disponibles selon votre pays (Revolut, Paypal, Wise, Strike, etc.)
- Suivez les instructions pour ajouter vos identifiants

***La carte-cadeau utilisable :***
- Amazon, Steam, etc.
- Saisissez le pays d'émission de la carte et ainsi que d'autres informations nécessaires

***Les options de paiement nationales :***
Systèmes de paiement spécifiques par pays :
- Satispay (Italie)
- MB Way (Portugal)
- Bizum (Espagne)
- Faster Payments (Royaume-Uni)
- etc.

***Pour les paiements en face à face :***

![Configuration des paiements en personne](assets/fr/05.webp)

- Sélectionnez "Meetup" (image 12)
- Puis sélectionner votre meetup parmi la liste (image 13)

### Conseils d'utilisation

- Vous pouvez ajouter plusieurs méthodes de paiement
- Plus vous ajoutez de méthodes, plus vous aurez accès à un large éventail d'offres
- Vérifiez l'exactitude de vos informations avant de les enregistrer
- Vous pouvez modifier ou supprimer vos méthodes de paiement à tout moment

**Note de sécurité** : Vos informations de paiement sont chiffrées et ne sont partagées qu'avec votre partenaire d'échange lors d'une transaction, sauf en cas de dispute ou un médiateur Peach y aura aussi accès.

### 4. Comment sécuriser son portefeuille

**Comprendre votre compte Peach**

Un compte Peach n'a pas d'identifiant et mot de passe. C'est un fichier stocké localement sur votre téléphone, ce qui signifie que Peach n'a pas besoin de stocker vos données ni de connaître votre identité : vous gardez le contrôle. Ce fichier contient toutes vos données: incluant les 12 mots de récuperation bitcoin, clefs PGP, détails de paiement etc. Il est donc crucial de sauvegarder ce fichier et de le protéger avec un mot de passe __robuste__.

Cette approche garantit un degré de confidentialité, et laisse la responsabilité de la gestion des donnés et des backup dans les main des utilisateurs. La perte de votre téléphone sans sauvegarde signifie la perte d'accès à votre compte Peach et à vos fonds. 

**Créer vos sauvegardes**


- Accédez aux paramètres depuis l'onglet en bas à droite de l'écran d'accueil
- Sélectionnez l'option "backups" dans le menu des paramètres

![Processus de sauvegarde](assets/fr/06.webp)

Deux types de sauvegardes sont disponibles :

**Sauvegarde du fichier de compte (image 14)**
- Cliquez sur "Create new backup"
- Créez un mot de passe **fort** pour chiffrer votre fichier de sauvegarde
- Enoyer ce fichier ce fichier dans un endroit qui assurera sa redondance en cas de perte du telephone.

La sauvegarde du fichier permet de restaurer votre compte Peach complet, incluant :
- Votre portefeuille
- Vos méthodes de paiement
- Les données de paiement
- L'historique des transactions avec les détails des contreparties, et les conversations avec celles-ci

**Sauvegarde de la phrase de récupération (image 15)**
- Suivez les instructions pour afficher votre phrase de récupération
- Notez soigneusement les mots dans l'ordre exact
- Stockez cette sauvegarde dans un lieu sécurisé, idéalement différent de celui du fichier de compte

La phrase de récupération permet de récupérer :
- Votre réputation, vos trades
- Vos fonds bitcoin

Mais **PAS** les choses suivantes:
- Vos conversations en cours et passés
- Les données de paiement
- Les informations des contreparties dans l'historique des transactions


## Acheter et vendre des bitcoins

### 1.a Comment acheter des bitcoins : Prendre un offre de vente

Le premier premier reflexe d'un acheteur doit être d'aller voir les offres de vente qui sont déjà financée avec du bitcoin.

![Vue des offres de vente et filtres](assets/fr/07.webp)

- Sur l'écran d'accueil, cliquez sur le bouton "Acheter" (image 16)
- Vous pouvez alors parcourir une liste des bitcoins qui sont placés dans le système d'entiercement ("escrow") et sont prêts pour la vente (image 17). Vous pourrez observer le montant, le prix (en % par rapport au marché KYC), les méthodes de payment et les devises acceptées.
- Utilisez les filtres pour trier et ordonner les offres (image 18).
- Notez: le bouton en bas de la page des filtres qui vous permet de recevoir une notification lorsqu'une offre correspondant à vos filtres a été publiée ; insi que le bouton "reset", qui permet simplement d'effacer tous les filtres (image 18).

![Sélection et confirmation d'achat](assets/fr/08.webp)

- Visualisez l'offre qui vous convient et envoyer un demande d'échange (image 19)
- Vous pouvez faire plusieurs demandes d'échange, et la première offre dont la réponse est positive annulera vos autres demandes.
- Effectuez le paiement selon la méthode convenue.
	**Rappel:** la provenance des fonds doit correspondre à celle que vous avez annonceé lors de l'ajout de la méthode de payment.
- **Confirmez votre paiement dans l'application dès lors que c'est fait**.
- Patientez que le vendeur perçoive le payment et le déclare comme tel. (image 20)
- Et enfin évaluez votre experience avec le vendeur (image 21)

![Réception des bitcoins](assets/fr/09.webp)

- Suivez le statut de votre transaction
- Vérifiez la confirmation de la réception des bitcoins
- Les fonds seront disponibles dans votre portefeuille Peach (image 22 et 23)

### 1.b Comment acheter des bitcoins : Créer une offre d'achat

Si vous ne trouvez pas d'offre de vente à votre goût, vous pouvez alors créer une offre d'achat. Puisque ceci n'engage pas de bitcoin à cette étape, vous aurez moins de chance de trouver un partenaire de change, spécialement si votre historique et réputation est faible voir nulle. Pour remédier à cela, il est important, lors de la création de l'offre, de *mettre une offre a haut premium* pour motiver les vendeurs à séléctionner votre offre. Procédons donc:

![Creation d'ordre d'achat](assets/fr/10.webp)

- Sur l'écran d'accueil, cliquez sur le bouton "Créer une offre d'achat" (image 24)
- Ajoutez une methode de payment, si ce n'est déja fait, et entrez vos prérences (quantité, premium etc.) (image 25).
	L'option "instantané" vous donne la possibilité d'accepter une requête de trade automatiquement.
	- Cliquez a nouveau sur "créer une offre d'achat" pour continuer
- Une fois créée, c'est au tour des vendeurs de venir vous faire une demande d'échange. Vous pouvez fermer et quitter l'app sans soucis.
- Vous pouvez changer le premium si vous ne recevez pas de demandes. Rappel : un premium plus haut motivera les vendeurs à venir chercher votre offre d'achat (image 26). 
- Vous trouverez votre offre dans l'onglet "acheter", qui se trouve lui même dans la fenêtre "échanges" (img. 27)

![Reception d'une demande de vente, messagerie](assets/fr/11.webp)

- Lorsque vous receverez une demande d'achat (image 28) (et si vous n'avez pas désactivé le trade instantané dans l'image 25), acceptez le trade apres avoir vérifié la reputation du vendeur. Si le trade instantané est activé, sautez directement à l'image 29.
- Le vendeur doit alors placer le bitcoin dans le système d'entiercement,  ("financer le coffre"). (image 29)
- Ensuite, payez le vendeur à la destination indiquée dans l'image 30, via votre système banquaire personnel. Ne glissez le curseur "J'ai fait le payement" qu'uniquement lorsque ce sera fait!
- Vous pouvez communiquer au vendeur dans la messageries (cryptée en P2P). En cas de soucis, il est possible d'ouvrir une dispute, en cliquant sur l'icone en haut à droite (image 31). Un médiateur Peach entrera alors dans la discussion. 

![Offre de vente completée](assets/fr/12.webp)

- Une fois que le vendeur aura reçu l'argent, il le signalera et le système de d'entiercement relachera le bitcoin, qui seront en route vers votre portefeuil (par default via GroupHug, le système de groupement de transactions de Peach, qui se déroule une fois par jour),
- Notez votre experience avec le vendeur

Et voila !

**Note pour les nouveau acheteurs:** les vendeurs se basent sur la réputation des acheteurs pour leurs trades, et tendent à éviter les offres d'achat provenant d'acheteurs sans aucuns trades completés. Il est plus facile, dans un premier temps, de construire une réputation en prenant des offres de vente existantes.


### 2.a Comment vendre des bitcoins : Créer une vente

La manière la plus simple et rapide pour vendre sur Peach est de **créer une offre de vente**.

![Création d'un ordre de vente](assets/fr/13.webp)

- Depuis la page d'acceuil, cliquez sur "Créer une offre de vente" (image 32)
- Parametrez votre offre, assurez vous d'insérer une methode de payement et le bon paramètres
	voux pouvez aussi : 
		- créer plusieurs offres identiques
		- activer l'"échange instantané" pour que le premier acheteur qui passe puisse prendre le contrat (sans votre confirmation) et procéder au payement.
		- choisir une addresse de remboursement
		- financer le coffre depuis votre wallet Peach
- Financez la transaction en envoyant les bitcoins à l'adresse fournie (image 34)
- Attendez la confirmation de la transaction. Une fois fait, votre offre sera visible sur le marché. 

![Attente du paiement](assets/fr/14.webp)

- Patientez qu'un acheteur prenne votre offre. Pensez à augmenter le premium (%) si vous voulez accélérer les choses. (image 36)
- Après demande d'échange reçue, vérifiez la réputation de l'acheteur. Jugez par vous-même si son profil vous convient, et cliquez "accepter" si c'est le cas. (37)
- C'est maintenant au tour de l'acheteur de procéder avec le payment depuis sa banque vers la votre. Il délarera le payement effectué. N'hesitez pas à communiquer avec l'acheteur dans le chat.
- *apres avoir bien controlé la reception des fonds dans votre banque*, relachez les fonds, en glissant le bouton "j'ai reçu le payment" (image 38). Ne confirmez jamais la réception d'un paiement avant d'avoir vérifié qu'il a bien été reçu sur votre compte.
- Évaluez la transaction
- Les bitcoins sont automatiquement libérés vers l'acheteur,

Et voilà !

**Note de Sécurité et conseils pour une transaction réeussie:**
	- Observez les détails de l'acheteur, et controlez bien que l'origine des fonds corresponde à celle décrite sur Peach Si l'origine des fonds ne correspond pas celle annoncée, allez dans le Chat et ouvrez une dispute (image 39), et renvoyez les fonds à leur origine.
	- Suivez bien les reccomendations qui se trouvent des le chat, en jaune. 
	- Répondez rapidement aux messages de votre contrepartie
	- restez méfiants aux égards de l'acheteur, surtout en cas de profil avec peu d'experience
	- N'hésitez pas à utiliser le service de médiation en cas de problème
	
### 2.b Comment vendre des bitcoins : prendre une offre d'achat

Il est aussi possible d'aller visualiser et et piocher pamri les offres d'achats. Il faudra etre particulièrement sur ses garde, car c'est la que se trouvent le plus d'arnaqueurs.

![Prendre une offre d'achat](assets/fr/15.webp)

- Depuis la page d'acceuil, cliquez sur "Vente" (image 40)
- Visualisez et choisissez les offres les plus attrayantes en vous aidant des filtres (image 41)

![vérification de la réputation](assets/fr/16.webp)

- avant de demander un trade, il est recommandé de juger si le profil de l'acheteur nous convient. On peut cliquer sur une offre, puis sur l'ID du l'utilisateur pour voir sont profil. Par example, l'offre dans l'image 42 pourrait etre considéré comme "risquée" (nouvel utilisateur, montant relativement élevé). Le "risque" que vous courrez en prenant cette offre, est simplement de perdre du temps, tant que vous ne commettez pas l'erreur de relacher les bitcoins sans avoir recu l'argent. Vous pouvez tout de même deposer les bitocins dans le coffre.
Celle qui figure dans l'image 43, par contre, vient d'un trader experimenté (image 44), sans disputes dans son historique. C'est donc un offre moins risquée.

![Match avec vendeur](assets/fr/17.webp)

- Une fois l'offre demandée, si l'acheteur accepte votre demande, l'application vous menera a l'image 34, ou vous pourrez continuer le trade comme décrit ci dessu.


## Avantages et Inconvénients

### Avantages de Peach

- **Pas de KYC requis** : Préserve la confidentialité des utilisateurs.
- **Aucun accès aux données bancaires** : Peach n'a pas accès à vos informations bancaires ni à votre identité.
- **Interface intuitive** : Facile à utiliser pour les utilisateurs intermédiaires.
- **Open Source** : Le code source est public et vérifiable par la communauté.

### Inconvénients de Peach

- **Liquidité limitée** : Moins de volume d'échange comparé à des plateformes plus établies.
- **Risque réglementaire** : L'application est gérée par une entreprise suisse. Elle est donc soumise à la réglementation suisse qui pourrait évoluer et potentiellement censurer l'application.

## Ressources Utiles

- Vidéo explicative en français : [YouTube](https://youtu.be/ziwhv9KqVkM)
- Guide de démarrage rapide : [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (attention aux arnaqueurs, les administrateurs ne vous écriront jamais en premier par message privé)
