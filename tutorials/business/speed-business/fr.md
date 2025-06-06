---
name: Speed Wallet - PoS
description: Intégrez facilement les paiements en bitcoins et en stablecoins dans votre commerce
---
![cover](assets/cover.webp)

L'adoption du Bitcoin sur l'ensemble du globe passe par des cas d'utilisations palpables dans la vie quotidienne. L'utilisation de Bitcoin dans les transactions commerciales instantanées partout dans le monde renforce cette adoption aussi bien au niveau des grandes institutions qu'au niveau de petits commerces. Dans ce tutoriel, nous découvrirons Speed Business, une plateforme de paiement unifiés qui permet à votre commerce d'accepter des paiements par Bitcoin via Lightning.

![btc-session](https://www.youtube.com/watch?v=ywUNZ_sxr0Q)

## Premiers pas avec Speed Business

[Speed Business](https://www.tryspeed.com/) est une plateforme développée par [Speed Wallet](https://www.speed.app/) qui permet à tout marchant d'intégrer des paiements instantanés et à faible coût par Bitcoin et stablecoins.

Speed possède un grand éventail de fonctionnalités pour couvrir les aspects financiers de votre commerce. Vous retrouverez : 

- **La configuration des paiements en ligne** : Recevez des paiements de vos clients peu importe leur localisation grâce à votre site internet.

- **Les paiements sur site** : Idéal pour les magasins et les commerces qui encaissent en boutique.

- **Les reversements** : Effectuez les retraits de vos avoirs sans accros et utiliser vos bitcoins pour rembourser vos clients ainsi que payez vos salaires.

- **La connexion avec d'autres plateformes** : Utilisez-vous des outils externes pour gérer vos paiements ? Speed vous offre la possibilité de les connecter à sa plateforme pour avoir un écosystème tout-en-un à l'image de votre commerce.

Créez votre compte sur [Speed](https://app.tryspeed.com/register/) puis nous débuterons la configuration des paiements pour votre commerce.

![account-creation](assets/fr/01.webp)

Fournissez des informations à Speed Wallet pour qu'il puisse vous aider à simplifier la prise en main de la plateforme selon votre expérience avec Bitcoin et Lightning Network 

![onboard](assets/fr/02.webp)

Speed dispose d'un kit de développement logiciel qui vous permet de personnaliser votre intégration et d'une extension pour une intégration standard.

Nous partirons, dans le cadre de ce tutoriel, sur une intégration standard en utilisant l'extension fournie par Speed.

Pour faciliter votre expérience, Speed vous propose un mode de test qui vous permet de tester les différentes fonctionnalités sans avoir à vous inquiéter de leurs répercussions sur la gestion de votre boutique. 

![test-data](assets/fr/03.webp)

Vous pourrez tester tous les aspects que nous aborderons dans ce tutoriel en utilisant le mode test.

Lorsque vous désactivez le mode test, vous devez configurer votre portefeuille de retrait.

![configure-wallet](assets/fr/04.webp)

Si vous ne possédez pas encore un portefeuille Bitcoin et/ou Lightning, nous vous recommandons de découvrir nos tutoriels sur les [portefeuilles mobiles](https://planb.network/tutorials/wallet).

https://planb.network/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

⚠️ **IMPORTANT** : Dans la configuration de votre portefeuille, choisissez le type **BTC (On-Chain)** lorsque vous recevez des montants importants, de l'ordre de milliers d'euros pour assurer la fiabilité de confirmation sur Bitcoin et le type **LN address**, lorsque vous souhaitez recevoir des micro-paiements instantanés dans votre commerce.

![setup-wallet](assets/fr/05.webp)

Confirmez ensuite l'ajout de votre portefeuille à partir du mail de vérification envoyé par Speed.

![verfication](assets/fr/06.webp)

Définissez le minimum de retrait à faire et le solde minimal en dessous duquel vous ne pourrez pas retirer vos avoirs.

![payout](assets/fr/07.webp)

## Ajouter vos produits

Dans la section **Produits**, ajoutez votre catalogue de produits que vous vendez dans votre commerce.

![product-creation](assets/fr/08.webp)

Appuyez sur **Next** pour continuer à définir votre produit et ses caractéristiques.

![product-details](assets/fr/09.webp)

Définissez ensuite le prix de vente de votre produit.

![product-price](assets/fr/10.webp)

Ces produits vous permettent de pouvoir générer des liens de paiements afin de permettre à vos clients de les payer.

## Recevoir des paiements 

Speed Wallet vous offre la possibilité d'utiliser plusieurs méthodes pour recevoir des paiements en ligne ou sur site dans votre commerce. 

Dans le menu **Receive Payments > Payments** , vous retrouverez l'historique des paiements reçus et leur statut (payé, expiré, non payé, annulé).

![payments](assets/fr/11.webp)

- Les liens de paiement se situent dans l'option **Checkout Links** et vous permettent de configurer des pages de paiements uniques pour vos produits.

![checkout-link](assets/fr/12.webp)

Vous pouvez, selon vos besoins, configurer et personnaliser la page de paiement pour recevoir les paiements d'un montant spécifique.

![configure-checkout](assets/fr/13.webp)

![finalize-checkout](assets/fr/14.webp)

Vous pourrez retrouver la liste des liens de paiement que vous avez configurés sur votre compte dans le menu **Payment Links**.

- Les factures : Speed vous permet d'initier des devis et des factures à l'endroit de vos clients.

![invoices](assets/fr/16.webp)

Sélectionnez un client que vous avez au préalable enregistré ou créez-en un facilement.

En définissant la devise, vous aurez accès à la liste des produits configurés dans cette devise.

Vous pouvez envoyer cette facture sous format PDF, par mail ou générer un lien QR code à scanner (idéal pour les magasins qui encaissent sur site) afin que votre client puisse régler la facture.

![configure-invoice](assets/fr/17.webp)


- Le menu **Payment Addresses** vous permet de configurer une adresse Lightning sur laquelle vous pouvez recevoir des paiements multiples et de montants variés.

![addresses](assets/fr/19.webp)

⚠️ Vous avez la possibilité d'ajouter et d'utiliser des noms de domaine autres que celui de Speed, toutefois, pour une première expérience, nous vous recommandons d'utiliser la configuration standard afin de bénéficier de toute l'expertise du support technique de Speed business.

- Le **One QR**: Idéal pour les paiements sur site, créez un code QR associé à votre commerce pour permettre à vos clients de payer vos produits.

![one-qr](assets/fr/20.webp)

## Effectuer des paiements à partir de Speed

Speed business ne se limite pas qu'à l'encaissement des paiements de votre commerce, il constitue un portefeuille qui vous permet de gérer sans accroc, tout l'aspect financier de votre structure.

Dans le menu **Send Payments**, vous retrouverez toutes les possibilités de speed vous propose en matière de transfert d'argent.

- **Les paiements instantanés** : Grâce à l'option Instant Send, envoyez de façon sécurisée, des bitcoins instantanément à partir de votre compte marchand.

- **Générez des liens de retrait** pour permettre à vos partenaires et fournisseurs d'accéder à leur paiement ultérieurement sans nécessiter votre présence en ligne.

Dans l'option **Withdrawal Links**, créez un nouveau lien de retrait puis configurez-le en définissant la devise, le montant et un mot de passe pour sécuriser l'opération de votre destinataire.

![withdrawal-links](assets/fr/21.webp)

⚠️Les liens de retrait ne sont utilisables qu'une seule fois, nous vous recommandons vivement de définir un mot de passe unique pour chaque lien, autrement toute personne en possession du lien peut retirer le montant configuré sur le lien de retrait.

- **Les versements**: Dans le menu Payouts, initiez des retraits de votre solde Speed Business vers votre portefeuille personnel.

![payouts](assets/fr/22.webp)

- **Les Remises**: Encouragez vos clients réguliers en mettant en place des options de ristournes pour qu'ils gagnent des bonus.

![cashbacks](assets/fr/23.webp)

## Explorer Speed Business

Speed Business est une plateforme multidevises qui vous permet de tenir sur un seul système, des portefeuilles séparés.

Dans l'option **Balances** retrouvez le solde de vos portefeuilles Bitcoin, USDT et USDC.

![balance](assets/fr/24.webp)

A l'instar de Speed Wallet, dans le menu **Swap**, Speed Business vous permet de faire des opérations de change entre vos différents portefeuilles de devises (BTC, USDT, USDC) à partir de 20.000 sats (environ $20 au taux actuel).

![swap](assets/fr/25.webp)

Dans le menu **Transfer**, communiquez avec d'autres marchants et transférez des bitcoins facilement en utilisant leur identifiant Speed.

![transferts](assets/fr/26.webp)

Dans le menu **Customers**, vous pourrez enregistrer et consulter la liste de vos clients (particuliers ou entreprises).

![customers](assets/fr/27.webp)

Gagnez des récompenses en participant au programme d'affiliation initié par Speed.

Dans le menu **Partners**, invitez des marchants à configurer leur commerce sur Speed business et faites-vous du revenu passif.

![partners](assets/fr/28.webp)

## Intégrer Speed sur le site Web de votre commerce

Speed Business possède un Kit de développement qui vous permet d'intégrer sa solution de paiement dans votre propre site Web.

Dans le menu **Developers**, créez vos clés publiques et privées afin d'utiliser les méthodes de l'API de Speed Wallet.

Retrouvez la [documentation](https://apidocs.tryspeed.com/reference/introduction) complète pour une meilleure intégration de Speed Business.

![developers](assets/fr/29.webp)

## Personnaliser son commerce

Dans le menu **Settings**, vous pouvez configurer votre profil marchant et les informations relatives à votre commerce.

Dans la section **Business Settings** :

- Éditez les détails de votre compte marchant tels que votre nom, votre localisation et votre fuseau horaire.

- Vérifiez les permissions activées (réception de paiement, envoi de bitcoin, échange, transfert, retrait) sur votre compte dans le menu **Account Status**.

- Définissez vos portefeuilles de retrait dans le menu **Payout Wallets** et configurez-les dans le menu **Payout Scheduling**.

- Définissez la charte graphique correspondante à votre commerce et personnalisez les pages de paiement, les emails, les codes QR et les factures à votre convenance dans le menu **Branding**.

- Configurez les méthodes de paiement dans les devises acceptées dans le menu **Payment Method**.

![payment-method](assets/fr/30.webp)

⚠️ La tolérance correspond au pourcentage de réduction que vous acceptez sur le montant de la facture pour qu'un paiement soit considéré comme valide. Si votre client doit payer 100 USD et que votre tolérance est de 1%, tout paiement de 99 USD valide la facture de 100 USD.



Vous avez une bonne prise en main de Speed, intégrez Bitcoin dans votre commerce et développez votre économie locale circulaire basée sur Bitcoin. Si ce tutoriel vous a été utile, nous sommes convaincues que vous apprécierez tout autant notre tutoriel sur Swiss Bitcoin Pay.

https://planb.network/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a