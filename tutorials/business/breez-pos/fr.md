---
name: Breez - POS
description: Encaissez facilement des paiements en bitcoins dans votre commerce avec Breez.
---

![cover](assets/cover.webp)

Depuis la pandémie de COVID-19, les paiements numériques sans contact se sont généralisés, même dans les plus petits commerces. Durant cette période, de nombreux commerces ont découvert l'utilité pratique des solutions d'encaissement en bitcoins, qui leur permettaient de recevoir des paiements du monde entier. Toutefois, ces solutions sont parfois difficiles à utiliser ou peu adaptées aux petits commerces. Dans ce tutoriel, nous allons découvrir le terminal de paiement de Breez, une solution qui se distingue par sa simplicité d’utilisation tout en vous offrant un contrôle total sur la gestion de vos bitcoins.

## Installer Breez POS

Le point de vente Breez est un service en self-custody fourni par le portefeuille Breez. L'utilité de ce service est de permettre aux commerçants d'encaisser des paiements via Bitcoin tout en restant sur une interface simple, très similaire aux différents portefeuilles Lightning. Le point de vente Breez est disponible sur les plateformes de téléchargement [Google Play Store](https://play.google.com/store/apps/details?id=com.breez.client) (Android) et [App Store](https://apps.apple.com/app/breez-lightning-client-pos/id1463604142) (iOS).

![download](assets/fr/01.webp)

![setup](assets/fr/12.webp)

⚠️ Il est important de noter que ces applications sont en cours de développement et qu'il peut y avoir quelques erreurs dans l'utilisation des fonctionnalités. Nous vous recommandons une utilisation modérée.

Avec cette application, Breez vous offre un contrôle complet sur les configurations réseau et sur les paramètres de frais, tout en garantissant votre souveraineté dans la gestion de vos bitcoins. 

Vous pouvez explorer les différentes options du portefeuille Breez en suivant notre tutoriel ci-dessous. Cette étape vous sera utile pour mieux comprendre l’écosystème du point de vente et adopter les bonnes pratiques afin de sécuriser efficacement les bitcoins associés à votre seed.

https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## Utiliser Breez POS

Dans ce tutoriel, nous nous focaliserons sur la section "*Point-of-Sale*" proposée afin de vous permettre de comprendre comment l'intégrer comme moyen d'encaissement dans votre commerce.

Le point de vente est une partie intégrante du portefeuille Breez et se base principalement sur le Lightning Network pour encaisser des paiements. 

Dans le menu "*Point de Vente*", vous avez directement une interface pour encaisser des paiements. Elle se divise en deux parties :

### L'encaissement direct

La première partie est le clavier d'encaissement direct. Cette interface est pratique pour encaisser globalement un paiement lorsque vous connaissez le total des achats de votre client ou que vous n'avez pas besoin d'un catalogue de produits fixes dans votre activité (par exemple des prestations freelance).

![keyboard](assets/fr/02.webp)

Pour une première utilisation du point de vente Breez, vous devez encaisser un paiement de plus de 2500 satoshis (environ 3 euros au cours actuel). Ce montant payé uniquement lors de votre premier encaissement représente le coût de création d'un canal de paiement afin de pouvoir communiquer avec d'autres nœuds du Lightning Network, d'envoyer et de recevoir des satoshis.

![channel_fee](assets/fr/03.webp)
### Le catalogue d'articles

La seconde partie est le catalogue d'articles. Cette interface est idéale lorsque vous disposez d'un catalogue de produits avec des prix définis à l'avance. Vous pouvez ici préconfigurer vos produits puis les utiliser par la suite pour générer des factures afin d'améliorer la traçabilité de vos encaissements.

![items](assets/fr/04.webp)

Vous pouvez configurer manuellement chaque article à partir de cette interface en cliquant sur le bouton "**Plus**" puis en définissant le nom, le prix et un identifiant pour cet article.

![add_items](assets/fr/05.webp)

Vous pouvez ensuite l'ajouter et définir sa quantité pour encaisser le paiement associé.

Lorsque votre catalogue est assez grand, cela pourrait devenir compliqué d'ajouter vos produits un à un. Pour cela, dans la section **Préférences > Paramètres Point de Vente**, à partir du menu "Liste d'articles" vous pouvez importer et exporter automatiquement la liste de vos articles à partir de fichiers CSV.

![import](assets/fr/07.webp)

Dans cette même section, vous pouvez définir la durée de validité de vos factures Lightning. À partir de ce moment, pour toutes vos factures, vos clients disposent de `N` secondes pour effectuer leur paiement, faute de quoi vous devrez régénérer une nouvelle facture Lightning.

![invoice_time](assets/fr/08.webp)

En tant que gérant, vous pouvez renforcer la sécurité de vos bitcoins en ajoutant un mot de passe qui sera requis pour tous les paiements sortants de votre portefeuille. Cette fonctionnalité est particulièrement utile lorsque vous n'êtes pas seul à gérer votre point de vente.

![manager](assets/fr/09.webp)

Dans le menu **Transactions**, vous retrouverez la liste de tous les paiements que vous avez encaissés. Vous pouvez également filtrer les résultats sur une période spécifique en cliquant sur le bouton **Calendrier**.

![transactions](assets/fr/10.webp)

Vous pouvez également afficher un résumé journalier de vos ventes et du montant total encaissé en cliquant sur le bouton **Document**.

![summary](assets/fr/11.webp)

Vous avez désormais une prise en main complète du point de vente proposé par l'application Breez pour une intégration fluide de Bitcoin dans votre commerce. Si ce tutoriel vous a été utile, nous vous recommandons notre tutoriel sur be-BOP, une plateforme de e-commerce qui vous permet d'encaisser des paiements en bitcoins et de monétiser votre activité.

https://planb.network/tutorials/business/point-of-sale/be-bop-d8c40a3b-9090-48e7-9ba7-235d0c17e5fa