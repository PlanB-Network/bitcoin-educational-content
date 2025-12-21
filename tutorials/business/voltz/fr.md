---
name: Voltz
description: Le portefeuille Lightning tout en un pour votre commerce.
---

![cover](assets/cover.webp)

L'idée de la plateforme Voltz est née d'un groupe de bitcoineurs qui souhaitait fournir leur propre service de portefeuille bitcoin. Il s'en est finalement résulté une infrastructure complète pour accepter le bitcoin dans les commerces. Dans ce tutoriel, nous vous emmenons à la découverte de Voltz et des possibilités d'intégration de bitcoin que la plateforme vous offre.

## Débuter avec Voltz

Au-delà d'être un portefeuille custodial Lightning qui vous permet d'envoyer, de recevoir et de payer quotidiennement, Voltz est une plateforme complète qui fournit des nombreuses extensions pour intégrer bitcoin comme point de vente ou place de marché dans votre commerce.

Rendez-vous sur la plateforme [Voltz](https://www.voltz.com/en) puis créez en compte en cliquant sur le bouton "Essayer maintenant".

![voltz](assets/fr/01.webp)

![login](assets/fr/02.webp)

⚠️ Il est important de définir un mot de passe alphanumérique fort afin d'augmenter vos chances contre les attaques brute-force, vérifiez également que vous êtes bel et bien sur le site officiel de Voltz afin de renseigner vos informations de connexion pour vous prémunir de l'hameçonnage (phishing).

L'interface de Voltz est très similaire à celle de la plateforme LnBits.

https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz est en effet construit sur un serveur LnBits; découvrez notre tutoriel pour apprendre à monter vos propres serveurs LnBits et construire vos solutions dessus.

https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

La plateforme vous permet une gestion efficace entre plusieurs portefeuilles. Par défaut, à l'inscription vous avez automatiquement un portefeuille Lightning. Toutefois, vous avez la possibilité d'ajouter d'autres portefeuilles.

![wallets](assets/fr/03.webp)

### La portabilité

Voltz ne se limite pas qu'à une interface web, dans la section **Accès Mobile**, vous pouvez connecter votre portefeuille actif Voltz dans les applications telles que Zeus ou Blue Wallet.

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

Pour ce faire, vous devez installer et activer l'extension **LndHub** sur la plateforme.

![lndhub](assets/fr/04.webp)

Sélectionnez votre portefeuille Voltz actif puis, en fonction des droits que vous souhaitez accorder, faites scanner le QR code adéquat.
- Le QR code des factures permet uniquement de lire l'historique de votre portefeuille et de générer de nouvelles factures.
- Le QR code admin vous permet de consulter l'historique, de générer des factures et aussi de payer des factures Lightning.

![qrs](assets/fr/05.webp)

Dans ce tutoriel, nous connectons notre portefeuille Voltz avec l'application Blue Wallet.

![connect](assets/fr/06.webp)

Une fois notre portefeuille connecté, toutes les actions effectuées seront synchronisées entre Blue Wallet et Voltz. Par exemple, lorsque vous générez une facture sur Blue Wallet, vous avez également une historique sur Voltz.

![sync](assets/fr/07.webp)

Vous retrouverez dans la section **Configuration de portefeuille**, des paramètres minimaux tels que la personnalisation du nom du portefeuille et aussi la devise dans laquelle vous souhaitez encaisser vos paiements.

![config](assets/fr/08.webp)

### Les extensions

L'une des particularité de la plateforme Voltz est sa modularité qui vous permet d'activer les extensions dont vous avez besoin. La liste des extensions se retrouve dans le menu **Extensions**.

![extensions](assets/fr/09.webp)

Parmi ces extensions, nous pouvons retrouver le TPoS, un terminal de point de vente que vous pourrez utiliser pour avoir un inventaire et encaisser les paiements de vos clients.

![tpos](assets/fr/10.webp)

A partir du terminal de Point de Vente, vous pouvez :
- Obtenir une page web que vous pouvez partager à vos clients et partenaires;
- Gérer un inventaire de produits;
- Générer des factures Lightning;
- Encaisser des paiements via des cartes Bolt.

L'extension est disponible en version gratuite et payante pour des fonctionnalités plus avancées. Pour créer un terminal de point de vente, cliquez sur le bouton **Ouvrir** en dessous du logo de l'extension, puis cliquez sur **Nouveau TPOS**.

![new_tpos](assets/fr/11.webp)

Définissez le nom de votre point de vente puis reliez votre portefeuille Voltz à votre terminal afin d'encaisser les paiements. Vous avez la possibilité d'activer les pourboires en cochant la case **Activer les dons**. Activez également l'option d'impression de facture si vous souhaitez délivrer les tickets de caisse à vos clients (Cette fonctionnalité est toujours sous développement, il se pourrait qu'il y ait des dysfonctionnements).

Le terminal de point de vente inclut également la configuration des taxes lorsque vous souhaitez appliquer la taxe de votre pays directement sur vos produits.

![tpos](assets/fr/12.webp)

Une fois votre terminal de point de vente créé, vous pouvez ajouter des produits et services pré-configurés pour vous assurer ainsi qu'à vos clients, une expérience de paiement et de comptabilité fluide.

![product](assets/fr/13.webp)

Créez vos produits en définissant leur nom, en ajoutant une image et en configurant un prix de vente.  Vous pouvez catégoriser vos produits pour un meilleur suivi. Vous pouvez appliquer directement des taxes sur un produit spécifique. Si le produit n'a pas de taxe appliquée, la taxe configurée au niveau de la création du terminal de point de vente s'appliquera automatiquement.

![products](assets/fr/14.webp)

Vous pouvez importer automatiquement la liste de vos produits depuis un format JSON en cliquant sur le bouton **Importer/Exporter**.

![exports](assets/fr/15.webp)

Accédez à l'espace d'encaissement via le lien en cliquant sur l'icône de **Nouvel Onglet** ou partagez votre plateforme de point  de vente via code QR avec vos clients en cliquant sur l'icône **QR code**.

![lien](assets/fr/16.webp)

![qr](assets/fr/17.webp)

Vos clients peuvent ainsi consulter votre catalogue et faire leur paiement depuis cette interface.

![pos](assets/fr/18.webp)

![chose](assets/fr/19.webp)

![pay](assets/fr/20.webp)

![checkout](assets/fr/21.webp)

Dans le groupe d'extensions disponible, vous retrouverez également des outils comme les extension de **Factures** et de **Lien de paiement** qui vous permettent de générer des factures avec des produits spécifiques pour encaisser des paiements isolés sans passer par le terminal de point de vente.
 
## Suivre ses paiements

Dans le menu **Paiements**, Voltz vous permet d'avoir une vue d'ensemble sur les paiements vers vos différents portefeuilles.
Vous pouvez suivre vos paiements selon :
- Le statut.
- L'étiquette : par exemple **TPOS** pour les paiements via le point de vente et **lnhub** via la connexion portable dans les portefeuilles Zeus et Blue Wallet.
- Le portefeuille d'encaissement.
- Le total des paiements entrant et sortant.
- Une période bien définie.

![payments](assets/fr/22.webp)

## Plus d'options

Voltz est également une infrastructure sur laquelle vous pouvez vous baser pour développer vos propres solutions. Dans la section **Extensions**, vous avez un guide pour développer vos propres extensions dans l'écosystème Voltz et LnBits.

![build](assets/fr/23.webp)

Dans le cas où vous voudriez développer des solutions hors de l'écosystème tout en utilisant leur infrastructure, dans la section **URL du nœud**, vous retrouverez des clés API et des informations sur la documentation avec un exemple de ce que vous pourrez faire avec ces données.

Vous pouvez ainsi créer des factures Lightning depuis vos applications en utilisant votre portefeuille Voltz, payer des factures Lightning, décoder et vérifier des factures.

![keys](assets/fr/24.webp)

Vous avez désormais une bonne prise en main de Voltz. Si vous avez apprécié ce tutoriel, nous sommes convaincues que vous apprendrez plus sur les meilleures méthodes et les meilleurs outils pour intégrer bitcoin dans votre commerce avec notre parcours : Bitcoin pour les entreprises.

https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a