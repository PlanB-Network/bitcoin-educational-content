---
name: Jade Plus - Green
description: Configurer facilement le Jade Plus avec Green
---
![cover](assets/cover.webp)

Le Jade Plus est un hardware wallet Bitcoin-only conçu par Blockstream. C'est le successeur du Jade classique avec des améliorations logicielles, des options en plus et une ergonomie repensée pour une utilisation plus intuitive. Cette nouvelle version se distingue notamment par son magnifique écran LCD de 1,9 pouce offrant une gamme de couleurs étendue comparée à son prédécesseur. Les boutons et la navigation dans les menus ont aussi été optimisés.

Le Jade Plus peut être utilisé de plusieurs manières : via une connexion filaire USB-C, en mode "*Air-Gap*" avec une carte micro SD (adaptateur nécessaire), en Bluetooth ou encore par échange de QR codes grâce à la caméra intégrée. Ce hardware wallet fonctionne sur batterie.

Il est disponible à partir de $149,99 en version noire de base, et le prix peut augmenter de jusqu'à $20 pour les versions "*Genesis Grey*" ou "*Lunar Silver*". Le Jade Plus se positionne donc comme un choix intéressant, avec des fonctionnalités avancées comparables à celles des hardware wallets haut de gamme tels que le Coldcard Q ou le Passport V2, mais à un tarif assez bas, proche des modèles de milieu de gamme.

![JADE-PLUS-GREEN](assets/fr/01.webp)

Le Jade Plus est compatible avec la majorité des logiciels de gestion de portefeuille. Voici un récapitulatif des compatibilités au moment de la rédaction de ce tutoriel (janvier 2025) :

| Logiciel de gestion | Desktop | Mobile | USB | Bluetooth   | QR  | JadeLink |
| ------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green   | 🟢      | 🟢     | 🟢  | 🟢 (Mobile) | 🟢  | 🔴       |
| Liana               | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Sparrow             | 🟢      | 🔴     | 🟢  | 🔴          | 🟢  | 🟢       |
| Nunchuk             | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Specter             | 🟢      | 🔴     | 🔴  | 🔴          | 🟢  | 🟢       |
| BlueWallet          | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Electrum            | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Keeper              | 🔴      | 🟢     | 🔴  | 🔴          | 🟢  | 🔴       |

Dans ce tutoriel, nous allons configurer et utiliser le Jade Plus avec l'application mobile Green Wallet de Blockstream via une connexion Bluetooth. Cette configuration est idéale pour les débutants. Si vous recherchez une approche plus avancée, je vous recommande de consulter ce tutoriel où nous utilisons le Jade Plus avec Sparrow Wallet en mode QR codes :

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Le modèle de sécurité du Jade Plus

Le Jade Plus utilise un modèle de sécurité reposant sur un "*secure element virtuel*", matérialisé par un "*blind oracle*". Concrètement, ce mécanisme combine le PIN choisi par l’utilisateur, un secret hébergé sur le Jade et un secret détenu par l’oracle (un serveur maintenu par Blockstream), afin de créer une clé AES-256 répartie sur deux entités. Lors de l’initiation, un échange ECDH sécurise la communication avec l’oracle, et permet de chiffrer la phrase de récupération sur le hardware wallet. Concrètement, lorsque l'on souhaite accéder à la seed pour signer des transactions, il faut avoir accès :
- À l'appareil Jade Plus en lui-même ;
- Au PIN pour déverrouiller l'appareil ;
- Et au secret de l'oracle.

L’avantage majeur de cette approche est l’absence de point de défaillance unique au niveau du hardware, puisque si jamais un attaquant a accès à votre Jade, l’extraction des clés exige de compromettre simultanément le Jade et l’oracle. Aussi, ce modèle permet au Jade Plus d'être entièrement open-source, puisqu'il permet d'éviter les contraintes liées à l'utilisation de véritables secure elements physiques, tels que ceux utilisés sur les Ledger par exemple.

L'inconvénient de ce système est que l'utilisation du Jade Plus dépend de l'oracle maintenu par Blockstream. Si cet oracle devient inaccessible, il n'est plus possible d'utiliser directement le hardware wallet avec le PIN. Cependant, cela ne signifie pas que vos bitcoins sont perdus, car ils peuvent toujours être récupérés grâce à votre phrase de récupération, que vous pouvez d'ailleurs entrer dans le Jade Plus en mode "*stateless*". Pour contourner cette dépendance, il est aussi possible de configurer et de gérer son propre serveur d'oracle.

## Unboxing du Jade Plus

Lors de la réception de votre Jade Plus, vérifiez que la boite et le sceau sont en bon état afin d'être sûr que votre paquet n'a pas été ouvert.

![JADE-PLUS-GREEN](assets/fr/02.webp)

Dans la boite, vous trouverez :
- Le Jade Plus ;
- Un cable USB-C ;
- Des cartons pour noter votre phrase mnémonique sous forme de mots ou bien sous forme "*CompactSeedQR*" ;
- Quelques notices d'utilisation ;
- Un cordon ;
- Quelques autocollants.

![JADE-PLUS-GREEN](assets/fr/03.webp)

L'appareil dispose de 4 boutons de navigation :
- Le bouton en bas à droite permet d'allumer le Jade ;
- Le gros bouton sur la face de l'appareil permet de sélectionner un élément ;
- Les deux petits boutons sur le haut permettent de naviguer à droite ou à gauche ;
- Vous pouvez également sélectionner un élément en cliquant simultanément sur les deux boutons en haut de l'appareil.

![JADE-PLUS-GREEN](assets/fr/04.webp)

## Configuration d'un nouveau portefeuille Bitcoin

Cliquez sur le bouton de démarrage.

![JADE-PLUS-GREEN](assets/fr/05.webp)

Cliquez sur "*Setup Jade*".

![JADE-PLUS-GREEN](assets/fr/06.webp)

Choisissez "*Begin Setup*". L'option "*Advanced Setup*" permet de faire la même chose, mais avec un accès aux paramètres avancés.

![JADE-PLUS-GREEN](assets/fr/07.webp)

Puis cliquez sur "*Create a New Wallet*" pour générer une nouvelle seed.

![JADE-PLUS-GREEN](assets/fr/08.webp)

Cliquez sur le bouton "*Continue*" pour afficher votre nouvelle phrase de récupération.

![JADE-PLUS-GREEN](assets/fr/09.webp)

Votre Jade Plus vous affiche votre phrase mnémonique de 12 mots. **Cette phrase mnémonique donne un accès complet et non restreint à tous vos bitcoins**. N'importe qui en possession de cette phrase peut subtiliser vos fonds, même sans accès physique à votre Jade Plus. La phrase de 12 mots permet de restaurer l'accès à vos bitcoins en cas de perte, vol ou casse de votre Jade. Il est donc très important de la sauvegarder soigneusement et de la stocker dans un endroit sécurisé.

Vous pouvez l'inscrire sur le papier cartonné fourni dans la boite, ou bien pour plus de sécurité, je vous recommande de la graver sur un support en acier inoxydable afin de la protéger contre les risques d'incendies, d'inondations ou d'écroulements.

![JADE-PLUS-GREEN](assets/fr/10.webp)

Pour plus d'informations sur la manière adéquate de sauvegarder et de gérer votre phrase mnémonique, je vous recommande vivement de suivre cet autre tutoriel, particulièrement si vous êtes débutant :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***Évidemment, vous ne devez jamais partager ces mots sur internet, contrairement à ce que je fais dans ce tutoriel. Ce portefeuille en exemple sera utilisé uniquement sur le Testnet et sera supprimé à l'issue du tutoriel.***

Cliquez sur la flèche à droite de l'écran pour afficher les mots suivants. 

![JADE-PLUS-GREEN](assets/fr/11.webp)

Une fois la sauvegarde de votre phrase terminée, le Jade Plus vous demande de la confirmer. Sélectionnez le bon mot en fonction de l'ordre en utilisant les boutons en haut de l'appareil, et cliquez sur le bouton central pour passer au mot suivant.

![JADE-PLUS-GREEN](assets/fr/12.webp)

## Connecter le Jade Plus à Green Wallet

Dans ce tutoriel, nous allons utiliser l'application Green Wallet pour gérer le portefeuille hébergé sur le Jade Plus. Cette méthode est particulièrement adaptée pour les débutants. Si vous désirez avoir une gestion plus fine de votre portefeuille Bitcoin, vous pouvez également utiliser Sparrow Wallet, que nous aborderons dans un autre tutoriel :

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Pour avoir des instructions sur l'installation et le paramétrage de l'application Blockstream Green, veuillez consulter la première partie de cet autre tutoriel :

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

Une fois sur l'application Blockstream Green, cliquez sur le bouton "*Configurer un nouveau portefeuille*".

![JADE-PLUS-GREEN](assets/fr/13.webp)

Choisissez "*On Hardware Wallet*".

![JADE-PLUS-GREEN](assets/fr/14.webp)

Activez le Bluetooth sur votre smartphone, puis cliquez sur le bouton "*Connectez votre Jade*".

![JADE-PLUS-GREEN](assets/fr/15.webp)

Autorisez l'application Green à accéder aux connexions Bluetooth.

![JADE-PLUS-GREEN](assets/fr/16.webp)

L'application est en train de rechercher votre Jade Plus.

![JADE-PLUS-GREEN](assets/fr/17.webp)

Sur le Jade Plus, cliquez sur le menu "*Bluetooth*".

![JADE-PLUS-GREEN](assets/fr/18.webp)

Sélectionnez votre appareil sur l'application Green.

![JADE-PLUS-GREEN](assets/fr/19.webp)

Confirmez le code d'appairage sur votre Jade Plus.

![JADE-PLUS-GREEN](assets/fr/20.webp)

Green vous propose de réaliser un test pour vous assurer que votre Jade est bien authentique. Cliquez sur le bouton pour le faire.

![JADE-PLUS-GREEN](assets/fr/21.webp)

Confirmez sur le Jade.

![JADE-PLUS-GREEN](assets/fr/22.webp)

Green vous confirme si votre appareil est bien authentique.

![JADE-PLUS-GREEN](assets/fr/23.webp)

## Configurer le code PIN

Cliquez sur le bouton "*Continuer*" pour choisir le code PIN de votre Jade.

![JADE-PLUS-GREEN](assets/fr/24.webp)

Le code PIN permet de déverrouiller votre Jade. C'est donc une protection contre les accès physiques non autorisés. Ce code PIN n'intervient pas dans la dérivation des clés cryptographiques de votre portefeuille. Ainsi, même sans accès à ce code PIN, la possession de votre phrase mnémonique de 12 mots vous permettra de retrouver l'accès à vos bitcoins. Il est recommandé de choisir un code PIN le plus aléatoire possible. Assurez-vous également de sauvegarder ce code dans un lieu distinct de celui où est stocké votre Jade (par exemple, dans un gestionnaire de mot de passe).

Choisissez le code PIN à 6 chiffres sur votre Jade en utilisant les boutons de droite et de gauche pour faire défiler les chiffres, et le bouton du milieu pour confirmer la saisie d'un chiffre.

![JADE-PLUS-GREEN](assets/fr/25.webp)

Confirmez votre PIN une seconde fois.

![JADE-PLUS-GREEN](assets/fr/26.webp)

Votre portefeuille bitcoin a bien été créé.

![JADE-PLUS-GREEN](assets/fr/27.webp)

## Créer un compte Bitcoin

Vous devez maintenant créer un compte au sein de votre portefeuille. Cliquez sur le bouton "*Créer un compte*".

![JADE-PLUS-GREEN](assets/fr/28.webp)

Choisissez "*Standard*" si vous souhaitez créer un portefeuille single-sig classique. 

![JADE-PLUS-GREEN](assets/fr/29.webp)

Pour plus d'informations sur l'option "*2FA*", vous pouvez suivre cet autre tutoriel :

https://planb.network/tutorials/wallet/mobile/blockstream-green-2FA-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Votre compte a bien été créé.

![JADE-PLUS-GREEN](assets/fr/30.webp)

Si vous souhaitez personnaliser votre portefeuille sur Green, cliquez sur les trois petits points en haut à droite.

![JADE-PLUS-GREEN](assets/fr/31.webp)

L'option "*Renommer*" vous permet de personnaliser le nom de votre portefeuille, ce qui est particulièrement utile si vous gérez plusieurs portefeuilles sur la même application. Le menu "*Unité*" vous permet de changer l'unité de base de votre portefeuille. Vous pouvez par exemple choisir de l'afficher en satoshis plutôt qu'en bitcoins. Enfin, le menu "*Paramètres*" vous donne accès à d'autres options. Vous y trouverez par exemple votre clé publique étendue et son descriptor, utiles si vous envisagez de configurer un portefeuille en mode watch-only à partir de votre Jade.

![JADE-PLUS-GREEN](assets/fr/32.webp)

Pour vous reconnecter à votre Jade après l'avoir éteint, appuyez sur le bouton on/off situé en bas de l'appareil. Sur l'application Green, sélectionnez votre appareil depuis la page d'accueil :

![JADE-PLUS-GREEN](assets/fr/33.webp)

Puis saisissez le code PIN sur votre Jade, et vous serez de nouveau connecté.

![JADE-PLUS-GREEN](assets/fr/34.webp)

Le déverrouillage de votre Jade s'effectue via le "*secure element virtuel*" de Blockstream (référez-vous à la première section du tutoriel). Pour cela, une connexion Bluetooth avec l'application Green est nécessaire. Si vous rencontrez des difficultés avec la connexion Bluetooth lors du déverrouillage, tentez de dissocier et de réassocier les deux appareils. Si le problème persiste, vous pouvez toujours déverrouiller votre Jade en sélectionnant l'option "*Scan QR*" et en suivant les instructions disponibles [sur le site web de Blockstream](https://jadefw.blockstream.com/pinqr/index.html).

Avant de recevoir vos premiers bitcoins sur votre portefeuille, **je vous conseille vivement de réaliser un test de récupération à vide**. Notez une information de référence, telle que votre xpub ou la première adresse de réception, puis supprimez votre portefeuille sur l'application Green et sur la Jade Plus tant qu'il est encore vide (`Options -> Device -> Factory Reset`). Ensuite, essayez de restaurer votre portefeuille en utilisant vos sauvegardes papier de la phrase mnémonique. Vérifiez que l'information témoin générée après la restauration correspond à celle que vous aviez notée initialement. Si c'est le cas, vous pouvez être assuré que vos sauvegardes papier sont fiables. Pour en savoir plus sur comment effectuer un test de récupération, je vous conseille de consulter cet autre tutoriel :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Recevoir des bitcoins

Maintenant que votre portefeuille Bitcoin est configuré, vous êtes prêt à recevoir vos premiers sats ! Pour cela, cliquez simplement sur le bouton "*Recevoir*" sur l'application Green.

![JADE-PLUS-GREEN](assets/fr/35.webp)

Green affiche une adresse de réception, mais avant de l'utiliser, il est essentiel de la vérifier sur le Jade pour confirmer qu'elle appartient bien à notre portefeuille. Pour cela, cliquez sur le bouton "*Vérifier sur l'appareil*".

![JADE-PLUS-GREEN](assets/fr/36.webp)

Vérifiez sur le Jade que l'adresse est bien la même que sur Green, puis cliquez sur le bouton pour confirmer.

![JADE-PLUS-GREEN](assets/fr/37.webp)

Vous pouvez maintenant partager l'adresse avec le payeur pour recevoir des bitcoins sur votre portefeuille. Quand la transaction sera diffusée sur le réseau, elle apparaîtra dans votre portefeuille. Attendez d'obtenir suffisamment de confirmations pour considérer la transaction comme définitive.

![JADE-PLUS-GREEN](assets/fr/38.webp)

## Envoyer des bitcoins

Avec des bitcoins dans votre portefeuille, vous pouvez maintenant également en envoyer. Cliquez sur "*Envoyer*".

![JADE-PLUS-GREEN](assets/fr/39.webp)

Sur la page suivante, entrez l'adresse du destinataire. Vous pouvez la saisir manuellement ou scanner un QR code.

![JADE-PLUS-GREEN](assets/fr/40.webp)

Choisissez le montant du paiement.

![JADE-PLUS-GREEN](assets/fr/41.webp)

En bas de l'écran, vous pouvez sélectionner le taux de frais pour cette transaction. Vous avez le choix de suivre les recommandations de l'application ou de personnaliser vos frais. Plus les frais sont élevés par rapport aux autres transactions en attente, plus vite votre transaction sera traitée. Pour connaitre le marché de frais, vous pouvez consulter le site [Mempool.space](https://mempool.space/) dans la section "*Transaction Fees*".

![JADE-PLUS-GREEN](assets/fr/42.webp)

Cliquez sur "*Suivant*" pour accéder à un écran récapitulatif de votre transaction. Vérifiez que l'adresse, le montant et les frais sont corrects.

![JADE-PLUS-GREEN](assets/fr/43.webp)

Si tout vous convient, faites glisser le bouton vert en bas de l'écran vers la droite pour signer et diffuser la transaction sur le réseau Bitcoin.

![JADE-PLUS-GREEN](assets/fr/44.webp)

On vous demande maintenant de confirmer la transaction sur le Jade.

![JADE-PLUS-GREEN](assets/fr/45.webp)

Assurez-vous que l'adresse de réception du destinataire est correcte. Cliquez sur la coche pour confirmer.

![JADE-PLUS-GREEN](assets/fr/46.webp)

Vérifiez que le montant des frais est correct, puis validez.

![JADE-PLUS-GREEN](assets/fr/47.webp)

Votre transaction a bien été signée puis diffusée depuis Green.

![JADE-PLUS-GREEN](assets/fr/48.webp)

Félicitations, vous savez dorénavant comment configurer et utiliser le Jade Plus avec l'application Blockstream Green sur mobile, par connexion Bluetooth. Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci !

Pour aller plus loin, je vous recommande de consulter ce tutoriel sur le Jade Plus, où nous le configurons avec le logiciel Sparrow Wallet en mode QR. Vous y apprendrez également comment utiliser les paramètres avancés de votre hardware wallet :

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
