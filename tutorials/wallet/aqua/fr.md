---
name: Aqua
description: Bitcoin, Lightning et Liquid en un seul wallet
---
![cover](assets/cover.webp)

Aqua est une application mobile qui permet de créer facilement un portefeuille chaud pour Bitcoin et Liquid, et qui offre aussi la possibilité d'utiliser Lightning sans la complexité de gestion d'un nœud, grâce à des swaps intégrés. Elle permet aussi la gestion des stablecoins USDT sur divers réseaux.

Développée par l'entreprise JAN3 sous la direction de Samson Mow, l'application Aqua a été initialement conçue spécifiquement pour les besoins des utilisateurs en Amérique latine, bien qu'elle soit adaptée à n'importe quel utilisateur dans le monde. Elle est notamment intéressante pour les débutants et ceux qui utilisent Bitcoin au quotidien pour leurs paiements.

Dans ce tutoriel, nous allons découvrir comment utiliser les nombreuses fonctionnalités d'Aqua. Mais avant cela, prenons un moment pour comprendre ce qu'est une sidechain sur Bitcoin et comment fonctionne Liquid, ce qui nous permettra de saisir pleinement l'intérêt d'Aqua.

![AQUA](assets/fr/01.webp)

## C'est quoi une sidechain ?

Le protocole Bitcoin présente des limitations techniques intentionnelles qui permettent de maintenir la décentralisation du réseau et d'assurer une distribution de la sécurité parmi tous les utilisateurs. Cependant, ces limites peuvent parfois frustrer les utilisateurs, notamment lors de congestions dues à un volume élevé de transactions simultanées. Le débat sur la scalabilité de Bitcoin a longtemps divisé la communauté, en particulier lors de la Blocksize War. Depuis cet épisode, il est largement reconnu au sein de la communauté Bitcoin que l'évolutivité doit être assurée par des solutions off-chain, sur des systèmes de seconde couche. Parmi ces solutions, il y a les sidechains, qui sont encore relativement méconnues et peu utilisées comparativement à d'autres systèmes comme le Lightning Network.

Une sidechain est une blockchain indépendante qui fonctionne en parallèle de la blockchain principale de Bitcoin. Elle utilise le bitcoin comme unité de compte grâce à un mécanisme appelé "*two-way peg*". Ce système permet de verrouiller des bitcoins sur la chaîne principale afin de reproduire leur valeur sur la sidechain, où ils circulent sous forme de tokens adossés aux bitcoins d'origine. Ces tokens conservent normalement une parité de valeur avec les bitcoins verrouillés sur la chaîne principale, et le processus peut être inversé pour récupérer les fonds sur Bitcoin.

L'objectif des sidechains est d'offrir des fonctionnalités supplémentaires ou des améliorations techniques, comme des transactions plus rapides, des frais réduits ou la prise en charge de contrats intelligents. Ces innovations ne peuvent pas toujours être mises en œuvre directement sur la blockchain de Bitcoin sans en compromettre la décentralisation ou la sécurité. Les sidechains permettent donc de tester et d’explorer de nouvelles solutions tout en préservant l’intégrité de Bitcoin. Cependant, ces protocoles nécessitent souvent des compromis, notamment en matière de décentralisation et de sécurité, en fonction du modèle de gouvernance et du mécanisme de consensus choisi.

## C'est quoi Liquid ?

Liquid est une sidechain fédérée en surcouche de Bitcoin, développée par Blockstream, qui vise à améliorer la vitesse, la confidentialité et les fonctionnalités des transactions. Elle utilise un mécanisme d’ancrage bilatéral établi sur une fédération pour verrouiller les bitcoins sur la chaîne principale et créer en contrepartie des Liquid-bitcoins (L-BTC), des tokens circulant sur Liquid tout en restant adossés aux bitcoins originaux.

![AQUA](assets/fr/02.webp)

Le réseau Liquid repose sur une fédération de participants, composée d’entités reconnues de l’écosystème Bitcoin, qui valident les blocs et gèrent l’ancrage bilatéral. En plus des L-BTC, Liquid permet également l’émission d’autres actifs numériques, comme le stablecoin USDT ou d'autres cryptomonnaies.

![AQUA](assets/fr/03.webp)

## Installer l'application Aqua

La première étape est naturellement de télécharger l'application Aqua. Rendez-vous sur votre store d'applications :
- [Pour Android](https://play.google.com/store/apps/details?id=io.aquawallet.android) ;
- [Pour Apple](https://apps.apple.com/us/app/aqua-wallet/id6468594241).

![AQUA](assets/fr/04.webp)

Pour les utilisateurs Android, vous avez aussi la possibilité d'installer l'application via le fichier `.apk` [disponible sur leur GitHub](https://github.com/AquaWallet/aqua-wallet/releases).

![AQUA](assets/fr/05.webp)

Lancez l'application, puis cochez la case "*I have read and agreed to the Terms of Service & Privacy Policy*".

![AQUA](assets/fr/06.webp)

## Créer son portefeuille sur Aqua

Cliquez sur le bouton "*Create Wallet*".

![AQUA](assets/fr/07.webp)

Et voilà, votre portefeuille est déjà créé !

![AQUA](assets/fr/08.webp)

Mais avant toute chose, puisqu'il s'agit d'un portefeuille en self-custody, il est impératif de réaliser une sauvegarde physique de votre phrase mnémonique. **Cette phrase mnémonique donne un accès complet et non restreint à tous vos bitcoins**. N'importe qui en possession de cette phrase peut subtiliser vos fonds, même sans accès physique à votre téléphone.

Elle permet de restaurer l'accès à vos bitcoins en cas de perte, de vol ou de casse de votre téléphone. Il est donc très important de la sauvegarder soigneusement sur un support physique (pas numérique) et de la stocker dans un endroit sécurisé. Vous pouvez l'inscrire sur un bout de papier, ou bien pour plus de sécurité, si ce portefeuille est important, je vous recommande de la graver sur un support en acier inoxydable afin de la protéger contre les risques d'incendies, d'inondations ou d'écroulements (pour un portefeuille chaud destiné à sécuriser une petite quantité de bitcoins, une simple sauvegarde sur papier est probablement suffisante).

Pour ce faire, cliquez sur le menu des paramètres.

![AQUA](assets/fr/09.webp)

Puis cliquez sur "*View Seed Phrase*". Réalisez la sauvegarde physique de cette phrase de 12 mots.

![AQUA](assets/fr/10.webp)

Dans ce même menu des paramètres, vous pouvez également modifier la langue de l'application ainsi que la monnaie fiat utilisée.

![AQUA](assets/fr/11.webp)

Avant de recevoir vos premiers bitcoins sur votre portefeuille, **je vous conseille vivement de réaliser un test de récupération à vide**. Notez une information de référence, telle que votre xpub ou la première adresse de réception, puis supprimez votre portefeuille sur l'application Aqua tant qu'il est encore vide. Ensuite, essayez de restaurer votre portefeuille sur Aqua en utilisant vos sauvegardes papier. Vérifiez que l'information témoin générée après la restauration correspond à celle que vous aviez notée initialement. Si c'est le cas, vous pouvez être assuré que vos sauvegardes papier sont fiables. Pour en savoir plus sur comment effectuer un test de récupération, je vous conseille de consulter cet autre tutoriel :

https://planb.network/tutorials/wallet/recovery-test

## Recevoir des bitcoins sur Aqua

Maintenant que votre portefeuille est configuré, vous êtes prêt à recevoir vos premiers sats ! Cliquez simplement sur le bouton "*Receive*" dans le menu "*Wallet*".

![AQUA](assets/fr/12.webp)

Vous pouvez choisir de recevoir des bitcoins onchain, sur Liquid, ou via Lightning.

![AQUA](assets/fr/13.webp)

Pour les transactions onchain, Aqua générera une adresse de réception spécifique où vous pourrez recevoir vos sats.

![AQUA](assets/fr/14.webp)

De la même manière, en optant pour Liquid, Aqua vous fournira une adresse Liquid.

![AQUA](assets/fr/15.webp)

Si vous préférez recevoir des fonds via Lightning, vous devrez d'abord spécifier le montant désiré.

![AQUA](assets/fr/16.webp)

Ensuite, cliquez sur "*Generate Invoice*".

![AQUA](assets/fr/17.webp)

Aqua créera une invoice pour recevoir des fonds depuis un portefeuille Lightning. À noter que, contrairement aux options onchain et Liquid, les fonds reçus via Lightning seront automatiquement convertis en L-BTC sur Liquid grâce à l'outil Boltz, puisque Aqua n'est pas un nœud Lightning. Ce processus vous permet de recevoir et d'envoyer des fonds via Lightning, mais sans jamais conserver vos bitcoins sur Lightning.

![AQUA](assets/fr/18.webp)

Personnellement, je vais commencer en envoyant des bitcoins via Lightning vers Aqua. Une fois la transaction effectuée avec l'invoice fournie, on reçoit une confirmation.

![AQUA](assets/fr/19.webp)

Pour suivre la progression du swap, retournez à l'accueil de votre portefeuille et cliquez sur le compte "*L2 Bitcoin*", qui répertorie les transactions Lightning (via swap) et Liquid.

![AQUA](assets/fr/20.webp)

Ici, vous pourrez visualiser votre transaction ainsi que votre solde en L-BTC.

![AQUA](assets/fr/21.webp)

## Swap des bitcoins avec Aqua

Maintenant que vous disposez d'actifs dans votre portefeuille Aqua, vous avez la possibilité de les swap directement depuis l'application, soit pour les transférer sur la blockchain principale de Bitcoin, soit sur Liquid. Vous pouvez aussi convertir vos bitcoins en stablecoin USDT (ou autres). Pour cela, accédez au menu "*Marketplace*".

![AQUA](assets/fr/22.webp)

Cliquez sur "*Swaps*".

![AQUA](assets/fr/23.webp)

Dans la case "*Transfer from*", choisissez l'actif que vous souhaitez échanger. Actuellement, je possède uniquement du L-BTC, donc c'est ce que je sélectionne.

![AQUA](assets/fr/24.webp)

Dans la case "*Transfer to*", choisissez l'actif cible de votre swap. Pour ma part, j'ai opté pour de l'USDT sur le réseau Liquid.

![AQUA](assets/fr/25.webp)

Saisissez le montant que vous désirez convertir.

![AQUA](assets/fr/26.webp)

Confirmez en cliquant sur "*Continue*".

![AQUA](assets/fr/27.webp)

Assurez-vous que les paramètres du swap vous conviennent, puis confirmez en faisant glisser le bouton "*Swap*" en bas de l'écran.

![AQUA](assets/fr/28.webp)

Votre swap est maintenant confirmé.

![AQUA](assets/fr/29.webp)

Si l'on revient sur notre portefeuille, on peut voir que l'on a maintenant des USDT sur Liquid.

![AQUA](assets/fr/30.webp)

## Envoyer des bitcoins avec Aqua

Maintenant que vous avez des bitcoins sur votre portefeuille Aqua, vous avez la possibilité de les envoyer. Cliquez sur le bouton "*Send*".

![AQUA](assets/fr/31.webp)

Choisissez l'actif que vous voulez envoyer ou sélectionnez le réseau pour effectuer la transaction. Pour ma part, je vais envoyer des bitcoins via Lightning.

![AQUA](assets/fr/32.webp)

Ensuite, entrez les informations nécessaires pour l'envoi du paiement : pour des bitcoins onchain ou Liquid, il faut entrer une adresse de réception ; pour Lightning, une invoice est nécessaire. Vous pouvez coller ces informations directement dans le champ prévu ou utiliser l'icône de QR code pour ouvrir votre appareil photo et scanner l'adresse ou l'invoice. Cliquez ensuite sur "*Continue*".

![AQUA](assets/fr/33.webp)

Cliquez à nouveau sur "*Continue*" si toutes les informations vous semblent correctes.

![AQUA](assets/fr/34.webp)

Aqua vous présente alors un résumé de la transaction. Assurez-vous que toutes les informations sont correctes, notamment l'adresse de destination, les frais, et le montant. Pour confirmer la transaction, faites glisser le bouton "*Slide to send*" situé en bas de l'écran.

![AQUA](assets/fr/35.webp)

Une confirmation de l'envoi vous est ensuite fournie.

![AQUA](assets/fr/36.webp)

Et voilà, vous savez désormais comment utiliser l'application Aqua pour recevoir et dépenser des fonds sur Bitcoin, Lightning et Liquid, le tout depuis une interface unique.

Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci beaucoup !

Je vous conseille également de découvrir cet autre tutoriel complet sur l'application mobile Blockstream Green, qui est une autre solution intéressante pour mettre en place son portefeuille Liquid :

https://planb.network/tutorials/wallet/blockstream-green-liquid
