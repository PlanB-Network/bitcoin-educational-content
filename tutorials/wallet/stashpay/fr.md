---
name: StashPay
description: Le portefeuille Bitcoin minimaliste pour tous
---

![cover](assets/cover.webp)

L'expérience utilisateur est un facteur déterminant dans l'adoption des solutions Bitcoin tout autour du globe. Proposer une expérience fluide, simple et sans contraintes techniques est la priorité de nombreux portefeuilles et plateformes d'échange. Dans ce sens, StashPay se démarque par son approche très minimaliste tout en montrant la puissance du Lightning Network.

Dans ce tutoriel, nous partons à la découverte de ce portefeuille afin de découvrir comment il fonctionne et comment il est idéal pour les petits commerces ou les solopreneurs.

## Débuter avec StashPay

StashPay est un portefeuille self-custodial Lightning reconnu principalement pour son expérience utilisateur minimaliste centrée sur l'utilisateur.  Avec ce portefeuille, vous n'avez pas besoin de connaissances techniques pour recevoir et envoyer vos premiers satoshis.

StashPay est un projet open-source développé en React Native et vise à résoudre le problème des frais de transactions élevés même avec les transactions sur la chaîne principale du protocole Bitcoin. Il est disponible en application mobile sur les plateformes Android et iOS via les liens de téléchargement présents sur le [site web](https://stashpay.me/).

![introduce](assets/fr/01.webp)

Il est important de télécharger l'application Android à partir du site web car elle n'est pas disponible sur Google Play Store.
Lorsque le téléchargement est achevé, veuillez accorder les permissions nécessaires afin de pouvoir installer l'application sur votre téléphone Android.

Une fois l'application installée, à votre première ouverture StashPay vous créera un portefeuille Bitcoin initial. Avant toute transaction, nous vous recommandons de faire la sauvegarde de ce portefeuille. Retrouvez ci-dessous, toutes nos directives pour assurer une bonne sauvegarde de vos phrases de récupération.

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Accédez aux paramètres de StashPay en cliquant sur l'icône "Paramètres" puis cliquez sur l'option **Créer une sauvegarde**. Autorisez ensuite l'affichage des phrases de récupération. Ne copiez pas vos phrases de récupération dans le presse-papier de votre téléphone, car elles peuvent être accessibles à d'autres applications frauduleuses installées sur votre mobile.

![backup](assets/fr/02.webp)

Vous avez également la possibilité de récupérer un portefeuille Bitcoin que vous utilisez déjà en cliquant sur l'option **Récupérer un portefeuille** puis en insérant vos 12 ou 24 mots de récupération.

### Recevoir ses premiers satoshis sur StashPay

Sur l'écran d'accueil, cliquez sur le bouton **Recevoir** puis définissez un montant supérieur au montant spécifié en rouge. Dans notre cas, nous ne pouvons pas recevoir moins de 0.11 USD avec le portefeuille StashPay.

![receive](assets/fr/03.webp)

Lorsque vous avez défini le montant, vous pouvez cliquer sur le bouton **Créer une facture** puis faites scanner ou copiez cette facture pour l'envoyer à votre expéditeur de satoshis.

![receive_sats](assets/fr/04.webp)

Vous pouvez consulter l'historique de vos transactions en cliquant sur l'icône "horloge" de l'accueil.

![network_fee](assets/fr/05.webp)

Vous aurez constaté que pour recevoir des satoshis vous aurez à payer des frais de réseau. Ces frais seront déduits des satoshis que vous êtes sur le point de recevoir. En effet StashPay est un portefeuille qui se base sur le Kit de Développement de Breez. Pour recevoir des satoshis avec l'implémentation sans nœud Lightning du Kit, Breez facturera au client (StashPay dans notre cas) `0,25% + 40 satoshis`. Découvrez-en plus avec notre tutoriel sur Misty Breez.

https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Envoyer des bitcoins avec StashPay

Envoyer des bitcoins avec StashPay est assez intuitif grâce à l'interface minimaliste. Sur l'écran d'accueil, cliquez sur le bouton **Envoyer**. Scannez le QR code ou collez l'adresse vers laquelle vous souhaitez envoyer des satoshis. StashPay détectera automatiquement la chaîne du protocole Bitcoin vers laquelle vous souhaitez envoyer des bitcoins.

![send](assets/fr/06.webp)

StashPay étant un portefeuille basé sur le Kit de Développement de Breez, il bénéficie d'un avantage intéressant : envoyer des bitcoins sur la chaîne principale avec peu de frais. Pour effectuer les transactions entre les différentes chaînes du protocole Bitcoin, Breez utilise le service Boltz et permet aux clients qui implémentent le Kit de Développement de profiter de ce service directement dans leur application.

https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Toutefois, Breez SDK vous impose un montant minimal à partir duquel vous pouvez envoyer des bitcoins vers une adresse de la chaîne principale.

![onchain](assets/fr/07.webp)

Vous pouvez également envoyer des bitcoins en utilisant l'adresse Lightning de votre destinataire. Relisez les informations concernant votre transaction puis confirmez en cliquant sur le bouton **Envoyer**.

![confirm](assets/fr/08.webp)

## Plus de configurations

Dans les paramètres de StashPay, vous pouvez régler les configurations pour personnaliser votre utilisation du portefeuille.

StashPay vous permet d'échanger des satoshis en vous basant sur la devise locale de votre choix. Cliquez sur l'option **Monnaies** puis recherchez votre devise dans la liste de +113 devises que vous propose StashPay.

![currencies](assets/fr/09.webp)

Dans le menu **Options de réception**, vous retrouverez les configurations liées à la réception de bitcoins avec StashPay. Par exemple, en sélectionnant **Choisir Lightning ou Onchain**, permettez à votre portefeuille de recevoir des bitcoins depuis la chaîne principale.

![receive-onchain](assets/fr/10.webp)

L'option **Scanner les adresses OnChain** vous permet de rafraîchir la balance de votre portefeuille en vérifiant tous les UTXO (bitcoins que vous n'avez pas encore dépensés) qui sont liés à vos différentes adresses.

![rescan](assets/fr/11.webp)

Le menu **Exporter le journal** liste toutes les actions des infrastructures de Breez et de Boltz concernant vos transactions et vos échanges atomiques entre les différentes chaînes du protocole Bitcoin.

![export](assets/fr/12.webp)

Vous venez de prendre en main le portefeuille Bitcoin minimaliste StashPay. Si vous avez trouvé ce tutoriel utile, nous vous recommandons notre cursus pour débuter avec Bitcoin et obtenir vos premiers bitcoins.

https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f