---
name: Misty Breez
description: Le portefeuille Lightning sans nœud.
---

![misty-breez-cover](assets/cover.webp)

Misty Breez est un portefeuille Lightning d'auto détention développé par la société Breez en se basant sur leur Kit de Développement Logiciel et le réseau **Liquid** développé par BlockStream.
Il vient avec une toute nouvelle approche consistant à se passer de nœud Lightning pour fonctionner : un potentiel **GAME CHANGER** dans les transferts inter réseaux Bitcoin.
Dans ce tutoriel, nous décrirons le fonctionnement de ce portefeuille et en feront une prise en main complète.

## Comment fonctionne Misty Breez ?

Misty Breez est une implémentation sans nœud Lightning comme backend. Il a été développé sur la base de Breez SDK et Liquid.

Liquid est une couche parallèle au réseau Bitcoin qui permet des améliorations notables en matière de rapidité et de frais de transaction. Cette couche permet à Misty Breez de se passer d'un nœud Lightning et d'utiliser à la place, des services tiers d'échanges comme **Boltz** pour assurer l'interopérabilité entre le réseau Liquid et le réseau Lightning. Ne vous empressez pas, nous y reviendrons.

Pour le moment, démarrons notre aventure avec le portefeuille Misty Breez. 

## Prise en main de Misty Breez

L'application mobile Misty Breez est disponible sur les plateformes de téléchargement officielles telles que Google Play Store (sur Android) et Apple Store (sur iOS). Vous pouvez également être redirigé vers la bonne application depuis le site officiel de [Misty Breez](https://breez.technology/misty/).

⚠️ Assurez-vous de ne pas confondre Misty Breez et le portefeuille Breez.

⚠️ **IMPORTANT** : Il est primordial pour la sécurité de vos bitcoins de télécharger l'application sur des plateformes officielles pour assurer l'authenticité de l'application.

![download-misty-breez](assets/fr/01.webp)

Dans ce tutoriel, nous effectuerons une prise en main à partir d'un Android. Néanmoins, chacune des étapes et les spécificités qui seront détaillées dans cette section sont valables sur iOS.

Dès l'installation, Misty Breez vous donne la possibilité de créer un nouveau portefeuille ou de restaurer un ancien portefeuille Lightning dont vous possédez les mots de récupération.
Dans ce tutoriel, nous choisissons de créer nouveau portefeuille.

⚠️Misty Breez est actuellement en phase de développement, nous vous conseillons de démarrer avec des montants raisonnables.

![create-wallet](assets/fr/02.webp)
### Sauvegarder ses mots de récupération :
L'un des premiers réflexes que vous devez avoir lorsque vous créez un nouveau portefeuille est d'effectuer la sauvegarde de vos 12 mots de récupération.
Retrouvez ci-dessous des astuces pour effectuer une bonne sauvegarde de votre backup phrase.

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Pour effectuer la sauvegarde de vos phrases, sélectionnez le menu **Préférences > Sécurité** puis l'option **Vérifier son Backup Phrase**.

![backup](assets/fr/03.webp)
Pour plus de sécurité, vous pouvez également **créer un code PIN** pour authentifier l'accès à votre portefeuille.


Retrouvez votre devise locale dans la multitude de devises acceptées par Misty Breez. Procédez à votre configuration à partir du menu **Préférences > Monnaies Fiat** puis sélectionnez la ou les devises qui vous conviennent.

![devises](assets/fr/04.webp)

### Effectuer ses premières transactions
Si vous êtes déjà habitué au portefeuille Breez, vous ne serez pas du tout déphasé par l'interface intuitive de Misty Breez.

Sur l'interface du menu **Solde**, cliquez sur l'option **Recevoir** afin de créer des factures pour recevoir vos bitcoins sur votre portefeuille.

⚠️ Misty Breez vous demandera d'activer les notifications pour l'application dans les paramètres de votre téléphone afin de vous donner droit à une adresse Lightning.

Avec Misty Breez, vous pouvez : 
- Recevoir des bitcoins sur le réseau Lightning à partir de **100 satoshis** et à hauteur de **25.000.000 satoshis**.
- Recevoir des bitcoins sur le réseau principal de Bitcoin à partir de **25.000 satoshis**.

![transactions](assets/fr/05.webp)

C'est à partir d'ici que toute la magie de Misty Breez s'opère.
Contrairement au portefeuille Breez qui vous fournit un nœud Lightning et vous demande de couvrir, vous-même, les frais d'ouverture et de fermeture de canal de paiement, Misty Breez ne vous demande rien. Comme dit plus tôt, Misty Breez ne fonctionne même pas sur la base d'un nœud Lightning.

Explorons un peu plus les coulisses.

En réalité, vous possédez un portefeuille Liquid qui est associé à votre portefeuille Misty Breez. Logiquement, vous manipulerez des L-BTC (Liquid Bitcoin) à des taux fixes associés à des services tiers de conversion sous-marines en satoshis qui vous permettront une interopérabilité avec le réseau Lightning.

Lorsque vous recevez un paiement sur votre portefeuille Misty Breez, votre expéditeur vous envoie des satoshis qui passera par un service de conversion comme Boltz (actuellement utilisé par Misty Breez), pour convertir les satoshis envoyés en L-BTC qui seront reçus sur votre portefeuille Misty Breez (portefeuille Liquid associé).
Voici une schématisation simplifiée du processus qui s'opère en coulisse.

![lnswap-in](assets/fr/06.webp)

Cliquez sur l'interface du menu **Solde**, cliquez sur l'option **Envoyer** pour payer une facture Lightning.
Insérez la facture Lightning, l'adresse Lightning de votre destinataire ou scannez simplement le code QR de la facture pour effectuer votre paiement.

![send-bitcoins](assets/fr/07.webp)

Derrière la scène, vous permettez au portefeuille Liquid associé à votre portefeuille Misty Breez d'effectuer une conversion via Boltz de l'équivalant des L-BTC en satoshis puis de transférer ces satoshis sur le portefeuille Lightning de votre destinataire (présent sur le réseau Lightning).

![send-bitcoin-bts](assets/fr/08.webp)

Cette particularité dans l'infrastructure de Misty Breez permet aux utilisateurs d'effectuer leurs transactions même quand Misty Breez est hors ligne.

Pour les plus expérimentés, vous avez également un menu **Préférences > Développeurs** qui vous permet d'avoir un peu plus de détails sur :
- La version du Kit de Développement Logiciel de Breez.
- La clé publique de votre portefeuille Misty Breez.
- L'emprunte, l'identifiant unique dérivé de la clé publique primaire.
- Le solde de votre portefeuille.
- Le Tip Liquid, qui permet d'envoyer de petits montants de L-BTC.
- Le Tip Bitcoin, qui permet d'envoyer de petits montants de bitcoin.

Vous avez également la possibilité d'effectuer certaines actions telles que la synchronisation avec le réseau Liquid, la sauvegarde de vos clés, le partage votre journal d'activité et le choix de rescanner le réseau Liquid.

![dev-mode](assets/fr/09.webp)
Félicitations ! Vous avez désormais une bonne compréhension du portefeuille Misty Breez et de son apport dans les transactions inter réseaux Bitcoin. Si vous avez trouvé ce tutoriel utile, nous vous prions de nous laisser nous un pouce vert. Cela nous fera amplement plaisir.

Pour aller plus loin, je vous recommande également de découvrir notre tutoriel sur le portefeuille Aqua, qui fonctionne de manière similaire à Misty Breez :

https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125


