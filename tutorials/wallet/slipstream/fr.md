---
name: Slipstream
description: Envoyer une transaction signée directement à un mineur avec Slipstream, sans la diffuser sur le réseau Bitcoin
---

![cover](assets/cover.webp)

Habituellement, lorsque l'on signe une transaction, celle-ci est diffusée automatiquement à tous les nœuds Bitcoin du réseau. Elle est alors en attente d'être minée.

Or, tant qu'elle n'est pas dans un bloc, un attaquant ayant obtenu votre clé privée pourrait la remplacer et voler ses fonds. Typiquement, dans le cas où vous utilisez un portefeuille matériel ColdCard.

L'outil Slipstream de l'entreprise de minage MARA permet ainsi de contourner la diffusion de la transaction au réseau : celle-ci est directement (et uniquement) envoyée à un mineur, permettant de ne pas la rendre publique et de ne pas l'exposer sur le réseau. Cette transaction sera alors probablement plus lente à être minée, mais elle sera protégée d'une attaque par remplacement.

Ci-dessous, nous vous proposons un tutoriel permettant aux utilisateurs de [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), ainsi qu'à ceux utilisant le portefeuille [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), d'utiliser l'outil Slipstream du mineur MARA en passant par la page [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Attention** : cet outil ne s'adresse qu'à certains profils, principalement les portefeuilles Liana, miniscript et certains types de multisig. Wizardsardine le **déconseille explicitement** aux portefeuilles dont les fonds sont déjà à risque critique de vol, par exemple ceux dont la phrase de récupération a été générée sur un appareil ColdCard affecté par la vulnérabilité du générateur d'aléa. Dans ce cas, la course contre l'attaquant se joue à la seconde, et une transaction envoyée à un seul mineur met bien plus longtemps à être confirmée qu'une transaction diffusée normalement. Si vous êtes concerné, lisez d'abord notre tutoriel dédié :

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Pour les utilisateurs de Liana

Liana étant maintenu par Wizardsardine, l'éditeur de la page [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), le parcours y est direct : il suffit d'exporter le fichier PSBT signé plutôt que de le diffuser.

*Prérequis : disposer de fonds sur votre portefeuille Liana.*

### Étape 1 : Créez votre transaction avec Liana

Comme habituellement, construisez votre transaction en y ajoutant l'adresse d'envoi, la description, et le montant (ici, le maximum disponible sur le portefeuille).

Pour ajouter le taux de frais :

- sélectionnez les jetons que vous souhaitez envoyer en cliquant sur la petite case en bas à gauche, en dessous de « Coins selection » ;
- entrez alors le taux de frais. Pensez à mettre des frais bien plus élevés que le taux proposé, comme décrit sur cette page : [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Cliquez enfin sur « Next ».

![Construction de la transaction dans Liana](assets/fr/01.webp)

### Étape 2 : Vérifiez les informations de votre transaction

Avant de cliquer sur « Sign », vérifiez les informations de votre transaction ; en particulier :

- le montant envoyé ;
- le nombre de satoshis affectés aux frais de transaction ;
- mais surtout, l'adresse à laquelle vous envoyez les fonds (pensez à regarder les 5/6 premiers caractères, les 5/6 derniers, et 5/6 caractères au milieu de l'adresse afin d'éviter les attaques de type « empoisonnement d'adresse »).

![Vérification des informations de la transaction](assets/fr/02.webp)

### Étape 3 : Sélectionnez les portefeuilles de signature

Par suite, sélectionnez les portefeuilles logiciels et/ou matériels avec lesquels vous devez signer votre transaction. Petit rappel : dans le cas d'un portefeuille multi-signature en 2-sur-2, il vous faut 2 signatures sur 2.

### Étape 4 : Exportez le fichier PSBT de votre transaction

La transaction Bitcoin est désormais signée par les clés adéquates. Ne cliquez alors pas sur « Broadcast », sans quoi celle-ci sera partagée à l'ensemble du réseau et, si vous utilisez un portefeuille matériel ColdCard, votre transaction sera exposée publiquement et vos fonds seront à risque.

Vous pouvez désormais cliquer sur « Export », puis enregistrer en local le fichier PSBT sur votre ordinateur.

![Export du fichier PSBT depuis Liana](assets/fr/03.webp)

### Étape 5 : Diffusez la transaction au mineur via outofband.wizardsardine.com

Dernières étapes désormais. Pour diffuser la transaction au mineur, il suffit désormais de prendre le fichier PSBT et de le glisser-déposer dans la zone prévue.

![Dépôt du fichier PSBT sur outofband.wizardsardine.com](assets/fr/04.webp)

La transaction s'affiche alors comme ci-dessous.

![Transaction en file d'attente](assets/fr/05.webp)

### Étape 6 : Envoyez la transaction via Slipstream

Enfin, il vous suffit de cliquer sur « Send » afin que la transaction soit envoyée via Slipstream à MARA.

![Envoi de la transaction via Slipstream](assets/fr/06.webp)

La transaction passe alors, en quelques secondes, de « Sending » à « Accepted » :

![Transaction acceptée par Slipstream](assets/fr/07.webp)

Il ne vous reste plus qu'à copier l'identifiant de la transaction (TXID), puis de le coller dans [mempool.space](https://mempool.space/fr/) afin de visualiser son minage :

![Recherche du TXID sur mempool.space](assets/fr/08.webp)

À noter : la transaction sera notée « Transaction introuvable » jusqu'à ce que le mineur, MARA, mine un bloc et y ajoute votre transaction. Cela peut prendre plusieurs dizaines de minutes, voire heures, car MARA ne possède qu'environ 4,5 % du taux de calcul du réseau Bitcoin. Cela correspond donc, en date du 4 août 2026, à environ un bloc miné toutes les 3 h 45 min.

## Pour les utilisateurs d'autres portefeuilles

Dans le cas où vous n'utilisez pas [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) mais que vous souhaitez tout de même utiliser l'outil, voici un tutoriel proposé avec un portefeuille multi-signature 2-sur-2. Nous utiliserons pour ce faire le portefeuille logiciel [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Prérequis : disposer de fonds sur votre portefeuille Sparrow.*

### Étape 1 : Créez votre transaction

Avec [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), créez la transaction sur votre portefeuille multi-signature. Pensez à mettre des frais bien plus élevés que le taux proposé, comme décrit sur cette page : [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Une fois créée, cliquez sur « Create Transaction ».

![Création de la transaction dans Sparrow](assets/fr/09.webp)

### Étape 2 : Finalisez votre transaction

Afin de finaliser votre transaction, il est désormais nécessaire de la signer. Pour ce faire, cliquez sur « Finalize Transaction for Signing ».

![Finalisation de la transaction pour signature](assets/fr/10.webp)

### Étape 3 : Signez votre transaction avec vos différentes clés

Désormais, vient le moment de signer la transaction. Pour ce faire, il suffit de la signer avec le(s) portefeuille(s) logiciel(s) ou matériel(s) que vous utilisez.

![Signature de la transaction avec les clés du multisig](assets/fr/11.webp)

### Étape 4 : Téléchargez la transaction signée, et ne la diffusez pas au réseau

La transaction Bitcoin est désormais signée par les deux clés de notre multisig 2-sur-2. Ne cliquez alors pas sur « Broadcast Transaction », sans quoi celle-ci sera partagée à l'ensemble du réseau et, si vous utilisez un portefeuille matériel ColdCard, votre transaction sera exposée publiquement et vos fonds seront à risque.

![Transaction signée, prête mais non diffusée](assets/fr/12.webp)

### Étape 5 : Affichez le script de transaction signé, ou téléchargez le fichier PSBT

Pour afficher la transaction Bitcoin signée, cliquez désormais sur « View Final Transaction ». Vous pouvez alors copier le script de transaction Bitcoin signé :

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Affichage du script de transaction signé](assets/fr/13.webp)

Si vous souhaitez télécharger le fichier de la transaction, il vous suffit alors :

- soit de cliquer sur « File », puis sur « Save transaction… » ;
- soit de cliquer en bas à droite sur le bouton de connexion au réseau (bouton jaune), puis de cliquer sur « Save Final Transaction ».

La transaction sera alors enregistrée en local sur votre ordinateur.

![Enregistrement local de la transaction finale](assets/fr/14.webp)

### Étape 6 : Diffusez la transaction au mineur via outofband.wizardsardine.com

Dernières étapes désormais. Pour diffuser la transaction au mineur, il suffit désormais :

- d'aller sur [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) ;
- de coller le script de transaction signé copié à l'étape précédente, puis de cliquer sur « ADD TO QUEUE » en dessous ;

![Collage du script de transaction sur l'outil](assets/fr/15.webp)

- ou de prendre le fichier et de le glisser-déposer dans la zone prévue.

![Dépôt du fichier de transaction sur l'outil](assets/fr/16.webp)

La transaction s'affiche alors comme ci-dessous.

![Transaction en file d'attente](assets/fr/17.webp)

Si un message vous signale que le montant total de satoshis en entrée de votre transaction n'est pas connu (et que, de ce fait, le nombre de satoshis pour les frais ne peut pas être calculé), il vous suffit d'entrer manuellement le montant total de satoshis en entrée. Pour trouver cela, il suffit de cliquer sur l'affichage de votre transaction dans Sparrow, au milieu du graphique :

![Montant total en entrée affiché dans Sparrow](assets/fr/18.webp)

Entrez alors ce montant (15 904 sats dans notre exemple) sur l'outil [outofband.wizardsardine.com](https://outofband.wizardsardine.com/) :

![Saisie manuelle du montant total en entrée](assets/fr/19.webp)

Vérifiez enfin que le taux de frais est le bon.

### Étape 7 : Envoyez la transaction via Slipstream

Enfin, il vous suffit de cliquer sur « Send » afin que la transaction soit envoyée via Slipstream à MARA.

![Envoi de la transaction via Slipstream](assets/fr/20.webp)

La transaction passe alors, en quelques secondes, de « Sending » à « Accepted » :

![Transaction acceptée par Slipstream](assets/fr/21.webp)

Il ne vous reste plus qu'à copier l'identifiant de la transaction (TXID), puis de le coller dans [mempool.space](https://mempool.space/fr/) afin de visualiser son minage :

![Recherche du TXID sur mempool.space](assets/fr/22.webp)

À noter : la transaction sera notée « Transaction introuvable » jusqu'à ce que le mineur, MARA, mine un bloc et y ajoute votre transaction. Cela peut prendre plusieurs dizaines de minutes, voire heures, car MARA ne possède qu'environ 4,5 % du taux de calcul du réseau Bitcoin. Cela correspond donc, en date du 4 août 2026, à environ un bloc miné toutes les 3 h 45 min.
