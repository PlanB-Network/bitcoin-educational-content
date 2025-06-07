---
name: Blue Wallet

description: Portefeuille Bitcoin Radicalement Simple et Puissant
---
![cover](assets/cover.webp)

Débuter avec Bitcoin semble être un grand défi pour des personnes septiques sur la simplicité de son utilisation. Trouver les bons outils pour assurer cette simplicité devient donc d'une importance capitale pour une meilleure adoption de bitcoin comme un moyen d'échange et pas seulement comme une réserve de valeur.

Dans ce tutoriel nous allons à la découverte de Blue Wallet, un portefeuille Bitcoin simple mais tellement efficace qui vous permet de gérer vos bitcoins personnellement mais aussi de créer des coopératives de gestion basées sur le [multisig](https://planb.network/resources/glossary/multisig) (pas d'inquiétudes, nous y reviendrons).

![Vidéo tutoriel Blue Wallet](https://www.youtube.com/watch?v=UCAtFgkdJtM)

## Débuter avec Blue Wallet

Blue Wallet est un portefeuille Bitcoin open Source et d'auto détention qui vous permet de prendre le contrôle de vos bitcoins. Il est disponible en application mobile sur les plateformes Android et iOS. Dans ce tutoriel nous nous baserons sur la version Android, toutefois, tous les processus qui seront développés sont également valables sur iOS.

![download](assets/fr/01.webp)

⚠️ Veuillez vous assurer de télécharger l'application Blue Wallet Bitcoin Wallet sur une plateforme officielle pour garantir son authenticité afin de préserver vos bitcoins d'éventuelles fuites et piratages.

Une fois l'installation achevée, vous avez la possibilité de créer un nouveau portefeuille puis de sauvegarder les 12 mots de récupération ou d'importer un portefeuille Bitcoin déjà existant. Découvrez les astuces pour faire une sauvegarde efficiente de vos mots clés afin de ne pas perdre accès à vos bitcoins.

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Avec Blue Wallet vous avez la possibilité de créer des portefeuilles bitcoin dédiés et distincts. Par exemple, vous pouvez avoir un portefeuille pour vos épargnes et un autre pour vos dépenses quotidiennes toujours dans la même application.

![home](assets/fr/02.webp)

## Types de portefeuille

Dans Blue Wallet, vous retrouverez nativement deux types de portefeuille Bitcoin.

### Portefeuille Bitcoin

Si vous êtes habitués à d'autres portefeuilles Bitcoin comme Phoenix ou Aqua, vous ne serez absolument pas déphasés sur l'interface du portefeuille Bitcoin de Blue Wallet.

https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Le portefeuille Bitcoin de Blue Wallet représente le portefeuille standard dans l'écosystème Bitcoin. Vous pouvez dépenser des bitcoins du moment où vous êtes en possession des mots de récupération qui pourront fournir une signature valide sur le réseau pour authentifier que vous êtes propriétaires des bitcoins.

Pour créer un portefeuille Bitcoin, cliquez sur le bouton **Add now**, insérez le nom de votre portefeuille puis choisissez le type Bitcoin.

![bitcoin-wallet](assets/fr/03.webp)

Lorsque vous cliquez sur la prévisualisation de votre portefeuille Bitcoin, vous pourrez retrouver l'historique de vos transactions et envoyer et recevoir des bitcoins.

⚠️ Toutes les transactions effectuées dans votre portefeuille Bitcoin sont sur la chaîne principale du protocole Bitcoin (mainnet).

- Recevoir des bitcoins avec le portefeuille Bitcoin Blue Wallet est intuitif. En bas de votre écran, cliquez sur le bouton **Receive**. Partagez le code QR ou votre adresse Bitcoin à votre expéditeur afin qu'il puisse vous envoyer les bitcoins.

Vous avez également la possibilité de configurer un montant prédéfini afin de spécifier le montant de bitcoin que vous souhaitez recevoir.

![receive-bitcoin](assets/fr/04.webp)

- Sur le bouton **Send**, envoyez des bitcoins à une adresse bitcoin en définissant le montant souhaité puis en validant la transaction.

![send-bitcoin](assets/fr/05.webp)

Blue Wallet vous permet de configurer à votre convenance les paramètres de votre envoi de bitcoin.

Vous pouvez donc sélectionner le ratio de frais de transaction qui vous correspond si vous voulez voir la transaction rapidement validée dans un mempool et incluse dans un bloc par les mineurs. Selon le ratio choisi, les mineurs prioriseront plus ou moins votre transaction. Apprenez en plus dans notre tutoriel sur le mempool Space.

https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)

- Dans le cadre des paiements groupés, Blue Wallet vous permet, à partir d'un seul envoi, d'ajouter plusieurs receveurs.

Lorsque vous ajoutez l'adresse bitcoin de votre premier receveur, dans les options, cliquez sur **Add Recipient**, ajoutez l'adresse bitcoin puis définissez le montant à envoyer à ce receveur ainsi de suite. Blue Wallet se chargera de dispatcher les bitcoins pour effectuer plusieurs envois à partir de votre seule action.

![add-recipients](assets/fr/07.webp)

Vous pouvez retirer un ou tous les receveurs en cliquant respectivement sur **Remove Recipient** et **Remove All Recipents**.

![remove-recipient](assets/fr/08.webp)

- **Gonflez les frais** : Avez-vous fait une transaction qui prend du temps à être confirmée ? En activant le gonflement des frais vous pourrez ajouter des frais de transaction supplémentaires à votre transaction en attente pour accélérer sa confirmation.

![bumping](assets/fr/09.webp)

### Portefeuille MultiSig

Le portefeuille Multisig (multi signatures), représente un portefeuille créé à partir du regroupement d'un certain nombre (minimum 2) de portefeuilles Bitcoin. Dans ce type de portefeuille, selon la configuration et la méthode choisie, dépenser des bitcoins devient une action collective et coopérative.

Dans Blue Wallet, vous pouvez créer des portefeuilles multi signatures pour votre association, votre famille, votre entreprise. Tout au long de cette section, nous tâcherons de découvrir et de décortiquer chaque aspect de ce type particulier de portefeuille.

Ajoutez un nouveau portefeuille et selectionnez le type **Multisig Vault** pour créer un portefeuille multi signatures.

![multisig-vault](assets/fr/10.webp)

Définissez la configuration m-de-n dans votre organisation multi signatures en cliquant sur **Vault Settings**.

⚠️ Dans une configuration m-de-n, **m** représente le nombre de signature minimale requise pour approuver une transaction et **n** le nombre de portefeuilles de votre organisation.

Veillez à définir un nombre de signature minimal (m) majoritaire dans votre organisation. Par exemple une configuration 2-de-3 multi signatures nécessite que deux portefeuilles de votre organisation signent la transaction pour qu'elle puisse être effectuée.

❗Définir une configuration m-de-n où n est égale à m constitue un grand risque. Lorsqu'un membre perd l'accès à son portefeuille vous perdez l'autorisation de dépenser les bitcoins dans le portefeuille.

Quelques exemples de configurations optimales pour assurer la sécurité et votre accessibilité aux bitcoins :

- 2-de-3 multi signatures.

- 5-de-7 multi signatures.

![vault-settings](assets/fr/11.webp)

Gardez les meilleurs pratiques en sélectionnant le format P2WSH.

❗ **[P2WSH](https://planb.network/resources/glossary/p2wsh) ou Pay to Witness Script Hash** est une méthode de verrouillage qui bloque les bitcoins sortants de votre transaction (Outputs) au hash d'un script personnalisé que Blue wallet met en place. Le principale avantage avec ce type de verrouillage est qu'il réduit la taille de données des transactions et implicitement vous permet de payer moins de frais de transactions.

Créez ou importez chacun des **n** portefeuilles de votre configuration. Dans notre tutoriel, nous utiliserons une configuration 2-de-3 multi signatures. Veillez à sauvegarder individuellement les mots de récupération de chacun des portefeuilles.

![vault-keys](assets/fr/12.webp)

- **Recevoir des bitcoins**

Sur la page de votre portefeuille Multisig, vous retrouverez l'historique de vos transactions et les boutons Recevoir et Envoyer.

Recevoir des bitcoins dans un portefeuille multi signatures est le même processus que lorsque vous êtes dans un portefeuille Bitcoin standard.

- **Envoyer des bitcoins** :

En étant gestionnaire d'un portefeuille multi signatures, dépenser des bitcoins devient une action composée que ce soit avec d'autres personnes ou un second portefeuille qui vous appartient. La signature unique de votre portefeuille n'est plus suffisante. Cela rajoute une couche de sécurité à vos bitcoins parce qu'un individu malicieux ne pourra non plus dépenser ces bitcoins lorsqu'il entre en possession d'une seule de vos clés privées.

Tout comme le portefeuille Bitcoin standard de Blue Wallet, vous pouvez définir plusieurs receveurs dans l'option **Add recipients**.

Lors de la validation de votre transaction, vous aurez besoin d'une seconde signature pour approuver la dépense des bitcoins, rappelez vous nous sommes dans une configuration 2-de-3 multi signatures.

Le second portefeuille signataire s'il utilise également a la possibilité de signer la transaction même en étant d'un hors réseau internet (Pas de Wi-Fi, pas de donnés mobile) en scannant le code QR de la [transaction partiellement signée](https://planb.network/resources/glossary/psbt) que vous venez de créer.

![mutisig-send](assets/fr/13.webp)

- **Aller plus loin avec le portefeuille Multi signature**:

Sur l'interface de votre portefeuille multi signature, cliquez sur le bouton **Manage keys**.

En oubliant un des mots de récupération d'un des portefeuilles signataires (**Forget this seed...**), vous notifiez à Blue Wallet de supprimer la sauvegarde de ces mots de sa mémoire. Vous aurez donc préalablement fait une sauvegarde externe.

![revoke-key](assets/fr/14.webp)

En effectuant cette action, vous gardez seulement la clé publique associée à ces mots de récupération.

⚠️ Garder uniquement les clés publiques (XPUB) vous permet d'ajouter un niveau de sécurité en plus dans votre configuration 2-de-3 multi signatures. En effet, il pourrait être préjudiciable de garder tous les mots de récupération en un seul endroit lorsque votre téléphone est sujet à une attaque. Les attaquants n'ayant accès qu'à un seul **VAULT** (mots clés) que vous utilisez pour signer vos transactions, ne pourront pas voler vos bitcoins (minimum de 02 signatures requises) car les clés publiques ne permettent pas de signer des transactions.

## Plus d'options avec Blue Wallet

### Améliorer la sécurité de l'accès au portefeuille

Dans les paramètres, l'option **Sécurité** vous permet de définir l'utilisation de l'empreinte digitale pour effectuer une transaction, exporter ou supprimer votre portefeuille. Cela permet d'authentifier la personne utilisant votre smartphone.

![biometry](assets/fr/15.webp)

## Activer Lightning Network

Le Lightning Network n'est plus supporté nativement dans l'application Blue Wallet.

Dans les paramètres > **Lightning Settings**, vous pouvez manuellement associer votre portefeuille Lightning lorsque vous faites tourner un nœud Lightning Network Daemon (LND). Installez le Hub LND puis associez votre portefeuille en entrant le lien généré par le Hub.

![ln](assets/fr/16.webp)

https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Vous avez désormais fait le tour de Blue Wallet, prêt à utiliser bitcoin dans toute sa simplicité et avec toute sa puissance. Nous vous recommandons de passer le cap, découvrez comment accepter des paiements en bitcoins dans vos commerces grâce à la puissance de Lightning.

https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06