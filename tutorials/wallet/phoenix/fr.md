---
name: Phoenix
description: Installer et utiliser Phoenix Wallet
---
![cover](assets/cover.webp)

Phoenix est un portefeuille et nœud Lightning self-custodial développé par ACINQ, une entreprise française spécialisée dans les solutions logicielles sur Lightning. Contrairement aux portefeuilles Lightning custodiaux comme Wallet of Satoshi par exemple, où les bitcoins sont détenus par un tiers, Phoenix permet à l’utilisateur de conserver la maîtrise totale de ses clés privées. 

En effet, Phoenix fonctionne comme un véritable nœud Lightning embarqué sur votre téléphone, qui va automatiquement ouvrir un canal avec le nœud Lightning d'ACINQ . L’application repose sur Lightning-KMP, une implémentation multiplateforme en Kotlin du Lightning Network, optimisée pour les portefeuilles mobiles. Contrairement à d'autres solutions de nœuds Lightning, Phoenix simplifie considérablement la gestion. L'utilisateur n'est pas obligé de gérer l'ouverture et la fermeture des canaux, de faire tourner un nœud Bitcoin, ou de gérer ses liquidités sur le réseau Lightning. Phoenix s'occupe de toutes ces opérations techniques en arrière-plan.

Cette application allie ainsi la facilité d'utilisation et la praticité des portefeuilles Lightning mobiles à la sécurité et la souveraineté d'un véritable nœud Lightning personnel. Grâce à Phoenix, il est possible d’utiliser le Lightning Network de manière sécurisée, efficace et autonome, tout en bénéficiant d’une expérience utilisateur fluide et intuitive.

En contrepartie, certains frais s’appliquent :
- Envoyer via Lightning coûte 0.4 % du montant plus 4 sats ;
- En cas de besoin de liquidités pour recevoir via Lightning, 1 % du montant est facturé ;
- L'ouverture de chaque canal coûte 1000 sats.

Selon moi, Phoenix représente une excellente solution intermédiaire entre les portefeuilles Lightning custodiaux et la gestion manuelle d'un nœud Lightning. Cette application convient aussi bien aux débutants qu'aux utilisateurs avancés qui préfèrent ne pas s'occuper en détail de la gestion de leur propre LND ou Core Lightning. Découvrons ensemble comment l'utiliser !

![Image](assets/fr/01.webp)

## Installer l'application

Rendez-vous sur votre store d'applications et installez Phoenix :
- Sur le [Google Play Store](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.mainnet) ;
- Sur l'[App Store](https://apps.apple.com/fr/app/phoenix-wallet/id1544097028?l=en-GB).

![Image](assets/fr/02.webp)

Vous pouvez également installer l'application [avec le fichier apk sur leur dépôt GitHub](https://github.com/ACINQ/phoenix/releases).

![Image](assets/fr/03.webp)

## Création du portefeuille

Une fois l'application démarrée, cliquez sur le bouton "*Suivant*" pour passer la présentation, puis sur "*Commencer*".

![Image](assets/fr/04.webp)

Sélectionnez "*Créer un nouveau wallet*".

![Image](assets/fr/05.webp)

Et voilà, votre portefeuille et nœud Lightning sont désormais créés.

![Image](assets/fr/06.webp)

## Sauvegarde de la phrase mnémonique

Avant de commencer, il faut sauvegarder notre phrase mnémonique de 12 mots. Cette phrase donne un accès complet et non restreint à tous vos bitcoins. N'importe qui en possession de cette phrase peut subtiliser vos fonds, même sans accès physique à votre téléphone.

La phrase de 12 mots permet de restaurer l'accès à vos bitcoins en cas de perte, vol ou casse de votre téléphone. Il est donc très important de la sauvegarder soigneusement et de la stocker dans un endroit sécurisé.

Vous pouvez l'inscrire un papier, ou éventuellement, pour plus de sécurité, la graver sur un support en acier inoxydable afin de la protéger contre les risques d'incendies, d'inondations ou d'écroulements. Le choix du support pour votre phrase mnémonique dépendra de votre stratégie de sécurisation, mais si vous utilisez Phoenix comme un portefeuille de dépenses contenant des montants modérés, le support papier devrait être suffisant.

Pour plus d'informations sur la manière adéquate de sauvegarder et de gérer votre phrase mnémonique, je vous recommande vivement de suivre cet autre tutoriel, particulièrement si vous êtes débutant :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Cliquez sur le message affiché en haut de l'interface "*Sauvegarder votre wallet...*".

![Image](assets/fr/07.webp)

Cliquez ensuite sur "*Sauvegarder mon wallet*".

![Image](assets/fr/08.webp)

Puis, cliquez sur "*Voir ma clé*" et sauvegardez votre phrase mnémonique sur un support physique.

![Image](assets/fr/09.webp)

Cochez les deux cases en bas de l'interface pour confirmer que la sauvegarde a été correctement effectuée.

![Image](assets/fr/10.webp)

## Paramétrage de l'application

Avant de réaliser vos premières transactions, vous pouvez personnaliser les paramètres en cliquant sur l'icône de roue crantée située en bas à gauche de l'interface.

![Image](assets/fr/11.webp)

Dans le menu "*Display*", vous pouvez choisir le thème de l'application, la dénomination utilisée pour le bitcoin, et votre monnaie fiat locale.

![Image](assets/fr/12.webp)

Dans "*Payment options*", vous trouverez différents paramètres avancés pour les paiements Lightning. Vous pouvez conserver les paramètres par défaut.

![Image](assets/fr/13.webp)

Dans "*Channel management*", définissez le montant maximal de frais que vous êtes prêt à payer lors de l'ouverture d'un canal Lightning.

![Image](assets/fr/14.webp)

Dans le menu "*Access control*", je vous recommande fortement d'activer un système d'authentification pour sécuriser l'accès à l'application sur votre téléphone. Cela empêchera toute personne ayant accès à votre téléphone déverrouillé d'accéder à Phoenix et de voler vos bitcoins.

![Image](assets/fr/15.webp)

Dans le menu "*Electrum server*", si vous disposez d'un serveur Electrs, vous pouvez le connecter pour la diffusion de vos transactions.

![Image](assets/fr/16.webp)

Pour renforcer la confidentialité de vos connexions, activez les connexions via Tor dans le menu "*Tor*". Bien que l'utilisation de Tor puisse légèrement ralentir vos paiements et nécessite que l'application Phoenix soit ouverte en premier plan lors de la réception, cela augmente significativement votre confidentialité.

![Image](assets/fr/17.webp)

## Recevoir des bitcoins on-chain

Lors de la première utilisation, vous avez la possibilité de charger votre portefeuille Phoenix avec des fonds on-chain. Vous pouvez également effectuer ce premier dépôt directement depuis Lightning (voir la section suivante), mais dans tous les cas, des frais supplémentaires seront appliqués pour l'ouverture de votre premier canal.

Cliquez sur le bouton "*Receive*".

![Image](assets/fr/18.webp)

Faites glisser le QR code vers la droite pour révéler une adresse de réception Bitcoin. Envoyez-y le montant que vous souhaitez déposer sur Phoenix.

![Image](assets/fr/19.webp)

Le montant reçu on-chain apparaîtra d'abord en attente sous le solde de votre portefeuille. Il faudra attendre 3 confirmations pour que les fonds soient utilisables.

![Image](assets/fr/20.webp)

Une fois les fonds reçus, Phoenix ouvre automatiquement un canal Lightning pour vous. Vous pouvez désormais envoyer et recevoir des bitcoins via le Lightning Network.

![Image](assets/fr/21.webp)

## Recevoir des bitcoins via Lightning

Pour recevoir des sats via le Lightning Network, cliquez sur le bouton "*Receive*".

![Image](assets/fr/22.webp)

Phoenix génère une invoice Lightning. Vous pouvez soit la scanner, soit l'envoyer à la personne qui souhaite vous transférer des sats.

![Image](assets/fr/23.webp)

En cliquant sur le bouton "*Edit*", vous avez la possibilité d'ajouter une description qui sera visible par le payeur sur l'invoice, et de définir un montant spécifique que le payeur devra envoyer.

![Image](assets/fr/24.webp)

Les invoices classiques mentionnées ci-dessus ne sont utilisables qu'une seule fois. Pour une option de paiement réutilisable, vous pouvez utiliser votre QR code réutilisable, qui est une offre BOLT12.

![Image](assets/fr/25.webp)

Une fois l'invoice ou l'offre BOLT12 réglée, la transaction apparaîtra sur votre portefeuille Lightning.

![Image](assets/fr/26.webp)

## Envoyer des bitcoins via Lightning

Maintenant que vous disposez de sats sur Phoenix, vous êtes prêt à effectuer des paiements via le Lightning Network. Commencez par cliquer sur le bouton "*Send*".

![Image](assets/fr/27.webp)

Plusieurs options s'offrent à vous. En cliquant sur "*Scan QR code*", vous pouvez scanner une invoice Lightning, une offre BOLT12, ou même une adresse de réception pour un paiement on-chain.

![Image](assets/fr/28.webp)

Vous pouvez également entrer ces informations manuellement via le clavier dans le champ situé en haut de l'interface, ou saisir une adresse Lightning (BOLT12 ou LNURL). Vous avez aussi la possibilité de coller les informations directement avec le bouton "*Paste*".

![Image](assets/fr/29.webp)

Pour cet exemple, j'ai scanné une invoice de 10 000 sats. Pour effectuer le paiement, il suffit de cliquer sur "*Pay*".

![Image](assets/fr/30.webp)

La transaction est réalisée.

![Image](assets/fr/31.webp)

Félicitations, vous savez dorénavant comment configurer et utiliser Phoenix. Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci !

Pour aller plus loin, je vous conseille de découvrir ce tutoriel sur Alby Hub, une autre solution innovante et facile à utiliser pour lancer votre propre nœud Lightning :

https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Et pour en savoir plus sur le fonctionnement technique du Lightning Network, vous pouvez retrouver l'excellente formation gratuite de Fanis Michalakis sur Plan ₿ Network :

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
