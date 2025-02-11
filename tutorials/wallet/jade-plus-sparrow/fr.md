---
name: Jade Plus - Sparrow
description: Configuration avancée du Jade Plus avec Sparrow Wallet
---
![cover](assets/cover.webp)

Le Jade Plus est un hardware wallet Bitcoin-only conçu par Blockstream. C'est le successeur du Jade classique avec des améliorations logicielles, des options en plus et une ergonomie repensée pour une utilisation plus intuitive. Cette nouvelle version se distingue notamment par son magnifique écran LCD de 1,9 pouce offrant une gamme de couleurs étendue comparée à son prédécesseur. Les boutons et la navigation dans les menus ont aussi été optimisés.

Le Jade Plus peut être utilisé de plusieurs manières : via une connexion filaire USB-C, en mode "*Air-Gap*" avec une carte micro SD (adaptateur nécessaire), en Bluetooth ou encore par échange de QR codes grâce à la caméra intégrée. Ce hardware wallet fonctionne sur batterie.

Il est disponible à partir de $149,99 en version noire de base, et le prix peut augmenter de jusqu'à $20 pour les versions "*Genesis Grey*" ou "*Lunar Silver*". Le Jade Plus se positionne donc comme un choix intéressant, avec des fonctionnalités avancées comparables à celles des hardware wallets haut de gamme tels que le Coldcard Q ou le Passport V2, mais à un tarif assez bas, proche des modèles de milieu de gamme.

![JADE-PLUS-SPARROW](assets/fr/01.webp)

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

Dans ce tutoriel, nous allons réaliser une configuration avancée du Jade Plus avec le logiciel desktop Sparrow Wallet en mode QR codes. Cette configuration est idéale pour les utilisateur intermédiaires ou expérimentés. Si vous recherchez une approche plus simple pour les débutants, je vous recommande de consulter ce tutoriel où nous utilisons le Jade Plus avec Green Wallet avec une connexion Bluetooth :

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Le modèle de sécurité du Jade Plus

Le Jade Plus utilise un modèle de sécurité reposant sur un "*secure element virtuel*", matérialisé par un "*blind oracle*". Concrètement, ce mécanisme combine le PIN choisi par l’utilisateur, un secret hébergé sur le Jade et un secret détenu par l’oracle (un serveur maintenu par Blockstream), afin de créer une clé AES-256 répartie sur deux entités. Lors de l’initiation, un échange ECDH sécurise la communication avec l’oracle, et permet de chiffrer la phrase de récupération sur le hardware wallet. Concrètement, lorsque l'on souhaite accéder à la seed pour signer des transactions, il faut avoir accès :
- À l'appareil Jade Plus en lui-même ;
- Au PIN pour déverrouiller l'appareil ;
- Et au secret de l'oracle.

L’avantage majeur de cette approche est l’absence de point de défaillance unique au niveau du hardware, puisque si jamais un attaquant a accès à votre Jade, l’extraction des clés exige de compromettre simultanément le Jade et l’oracle. Aussi, ce modèle permet au Jade Plus d'être entièrement open-source, puisqu'il permet d'éviter les contraintes liées à l'utilisation de véritables secure elements physiques, tels que ceux utilisés sur les Ledger par exemple.

L'inconvénient de ce système est que l'utilisation du Jade Plus dépend de l'oracle maintenu par Blockstream. Si cet oracle devient inaccessible, il n'est plus possible d'utiliser directement le hardware wallet avec le PIN. Cependant, cela ne signifie pas que vos bitcoins sont perdus, car ils peuvent toujours être récupérés grâce à votre phrase de récupération, que vous pouvez d'ailleurs entrer dans le Jade Plus en mode "*stateless*". Pour contourner cette dépendance, il est aussi possible de configurer et de gérer son propre serveur d'oracle.

Une autre option pour la gestion de votre seed est tout simplement de ne pas l'enregistrer sur le Jade Plus. Dans ce cas, le Jade devient uniquement un périphérique de signature. Lors de l'initialisation, en plus de la sauvegarde habituelle de la phrase de récupération sous forme de mots, vous allez également l'enregistrer sous forme de QR code généré à la main. Ainsi, lors de chaque utilisation de votre portefeuille, vous pourrez importer la seed à l'aide de la caméra de votre Jade. Cela peut être une option intéressante pour els utilisateurs avancés en fonction de votre stratégie de sécurisation, mais attention, il faut veiller à la fois à bien sauvegarder votre seed, et également à la protéger, car même sous forme de QR code, elle permettrait à n'importe qui de vous voler vos fonds. Nous allons étudier cette option dans ce tutoriel, mais elle n'est pas obligatoire.

## Unboxing du Jade Plus

Lors de la réception de votre Jade Plus, vérifiez que la boite et le sceau sont en bon état afin d'être sûr que votre paquet n'a pas été ouvert.

![JADE-PLUS-SPARROW](assets/fr/02.webp)

Dans la boite, vous trouverez :
- Le Jade Plus ;
- Un cable USB-C ;
- Des cartons pour noter votre phrase mnémonique sous forme de mots ou bien sous forme "*CompactSeedQR*" ;
- Quelques notices d'utilisation ;
- Un cordon ;
- Quelques autocollants.

![JADE-PLUS-SPARROW](assets/fr/03.webp)

L'appareil dispose de 4 boutons de navigation :
- Le bouton en bas à droite permet d'allumer le Jade ;
- Le gros bouton sur la face de l'appareil permet de sélectionner un élément ;
- Les deux petits boutons sur le haut permettent de naviguer à droite ou à gauche ;
- Vous pouvez également sélectionner un élément en cliquant simultanément sur les deux boutons en haut de l'appareil.

![JADE-PLUS-SPARROW](assets/fr/04.webp)

## Configuration d'un nouveau portefeuille Bitcoin

Cliquez sur le bouton de démarrage.

![JADE-PLUS-SPARROW](assets/fr/05.webp)

Cliquez sur "*Setup Jade*".

![JADE-PLUS-SPARROW](assets/fr/06.webp)

Choisissez "*Advanced Setup*".

![Image](assets/fr/07.webp)

Ensuite, cliquez sur "*Create a New Wallet*" pour générer une nouvelle seed. Vous avez le choix entre une phrase mnémonique de 12 ou de 24 mots. La sécurité de votre portefeuille reste équivalente avec les deux options, donc il peut être plus pratique de choisir l'option la plus simple à sauvegarder, soit 12 mots.

![Image](assets/fr/08.webp)

Cliquez sur le bouton "*Continue*" pour afficher votre nouvelle phrase de récupération.

![Image](assets/fr/09.webp)

Votre Jade Plus vous affiche votre phrase mnémonique de 12 mots. **Cette phrase mnémonique donne un accès complet et non restreint à tous vos bitcoins**. N'importe qui en possession de cette phrase peut subtiliser vos fonds, même sans accès physique à votre Jade Plus. La phrase de 12 mots permet de restaurer l'accès à vos bitcoins en cas de perte, vol ou casse de votre Jade. Il est donc très important de la sauvegarder soigneusement et de la stocker dans un endroit sécurisé.

Vous pouvez l'inscrire sur le papier cartonné fourni dans la boite, ou bien pour plus de sécurité, je vous recommande de la graver sur un support en acier inoxydable afin de la protéger contre les risques d'incendies, d'inondations ou d'écroulements.

![Image](assets/fr/10.webp)

Pour plus d'informations sur la manière adéquate de sauvegarder et de gérer votre phrase mnémonique, je vous recommande vivement de suivre cet autre tutoriel, particulièrement si vous êtes débutant :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

_**Évidemment, vous ne devez jamais partager ces mots sur internet, contrairement à ce que je fais dans ce tutoriel. Ce portefeuille en exemple sera utilisé uniquement sur le Testnet et sera supprimé à l'issue du tutoriel.**_

Cliquez sur la flèche à droite de l'écran pour afficher les mots suivants.

![Image](assets/fr/11.webp)

Une fois la sauvegarde de votre phrase terminée, le Jade Plus vous demande de la confirmer. Sélectionnez le bon mot en fonction de l'ordre en utilisant les boutons en haut de l'appareil, et cliquez sur le bouton central pour passer au mot suivant.

![Image](assets/fr/12.webp)

Vous avez ensuite 2 options. Comme expliqué dans l'introduction, vous pouvez choisir de sauvegarder votre seed directement sur l'appareil et utiliser le système de protection "*Virtual Secure Element*" de Blockstream pour accéder à votre portefeuille (Option 1), ou bien sauvegarder votre seed sous forme de QR code et la scanner à chaque utilisation (Option 2).

Pour l'Option 1, sélectionnez "*No*", et pour l'Option 2, sélectionnez "*Yes*".

![Image](assets/fr/13.webp)

### Option 1 : QR PIN Unlock

Si vous avez choisi l'option 1 (CompactSeedQR : "*No*"), vous serez directement dirigé vers le choix de la méthode de connexion. Dans ce tutoriel, nous souhaitons utiliser l'appareil en mode Air-Gap via des échanges de QR code, donc sélectionnez "*QR*".

![Image](assets/fr/27.webp)

Cliquez sur "*Continue*".

![Image](assets/fr/28.webp)

Le code PIN sert à déverrouiller votre Jade et offre une protection contre les accès physiques non autorisés. Ce code PIN n'intervient pas dans la dérivation des clés cryptographiques de votre portefeuille. Ainsi, même sans accès à ce code PIN, la possession de votre phrase mnémonique de 12 mots vous permettra de retrouver l'accès à vos bitcoins. Il est recommandé de choisir un code PIN aussi aléatoire que possible. Assurez-vous également de sauvegarder ce code dans un endroit distinct de celui où est stocké votre Jade, comme dans un gestionnaire de mots de passe par exemple.

Choisissez un code PIN à 6 chiffres sur votre Jade en utilisant les boutons de droite et de gauche pour faire défiler les chiffres, et le bouton du milieu pour confirmer chaque chiffre.

![Image](assets/fr/29.webp)

Confirmez votre PIN une seconde fois.

![Image](assets/fr/30.webp)

Comme expliqué dans l'introduction, votre seed est stockée chiffrée sur le Jade Plus. Pour la déchiffrer, il faut obligatoirement fournir :
- Le code PIN valide (que nous venons de mettre en place) ;
- Le secret de l'oracle maintenu par Blockstream.

Dans ce tutoriel avancé, nous utiliserons Sparrow Wallet pour gérer notre portefeuille Bitcoin. Cependant, contrairement au logiciel Green Wallet de Blockstream, Sparrow n'a pas accès à l'oracle sur les serveurs de Blockstream. Nous utiliserons donc le site web de Blockstream pour récupérer le secret de l'oracle à chaque déverrouillage du Jade Plus.

Rendez-vous sur le site suivant : https://jadefw.blockstream.com/pinqr/index.html

Cliquez sur "*Start QR Unlock*".

![Image](assets/fr/31.webp)

Cliquez sur "*Done*", puisque vous avez déjà choisi votre PIN sur le Jade Plus.

![Image](assets/fr/32.webp)

Utilisez la caméra de votre ordinateur pour scanner les QR codes affichés sur l'écran de votre Jade.

![Image](assets/fr/33.webp)

Validez sur votre Jade pour accéder à l'écran suivant.

![Image](assets/fr/34.webp)

Scannez le QR code maintenant visible sur le site web pour récupérer le secret de l'oracle.

![Image](assets/fr/35.webp)

Votre portefeuille est désormais créé, vous pouvez procéder aux étapes suivantes et ignorer la sous-partie "*Option 2 : CompactSeedQR*".

![Image](assets/fr/36.webp)

Lors de chaque démarrage, cliquez sur "*QR Mode*".

![Image](assets/fr/37.webp)

Sélectionnez "*QR PIN Unlock*".

![Image](assets/fr/38.webp)

Entrez votre code PIN.

![Image](assets/fr/39.webp)

Puis rendez-vous sur [le site de Blockstream](https://jadefw.blockstream.com/pinqr/qrpin.html) pour faire l'échange de QR codes avec l'oracle.

![Image](assets/fr/40.webp)

Votre Jade est maintenant déverrouillé.

![Image](assets/fr/41.webp)

### Option 2 : CompactSeedQR

Si vous avez choisi l'option 2 (CompactSeedQR : "*Yes*"), cliquez de nouveau sur "*Yes*".

![Image](assets/fr/14.webp)

Cliquez sur "*Start*".

![Image](assets/fr/15.webp)

Vous pouvez utiliser la base de QR code fournie dans la boîte du Jade Plus. Sélectionnez le carton adapté selon que vous avez opté pour une phrase de 12 ou de 24 mots. Vous pouvez également [imprimer le gabarit depuis le site de Blockstream](https://help.blockstream.com/hc/article_attachments/41928319071769).

Votre Jade Plus affichera chaque zone de votre QR code.

![Image](assets/fr/16.webp)

Utilisez un stylo pour colorier les carrés et ainsi reproduire votre seed sous forme de QR code. Soyez précis pour garantir que la caméra du Jade Plus puisse le scanner ultérieurement. Utilisez la flèche pour passer à la zone suivante.

![Image](assets/fr/17.webp)

Une fois terminé, cliquez sur "*Done*".

![Image](assets/fr/18.webp)

Scannez votre QR code fait à la main avec le Jade Plus pour en vérifier la validité.

![Image](assets/fr/19.webp)

Si votre sauvegarde papier est correcte, cliquez sur "*Continue*".

![Image](assets/fr/20.webp)

Dans ce tutoriel, nous allons utiliser un mode de connexion exclusivement basé sur le scan de QR codes, donc sélectionnez "*QR*".

![Image](assets/fr/21.webp)

Vous pouvez également choisir d'ajouter un PIN en plus de votre sauvegarde CompactSeedQR, comme dans l'option 1. Cela offre deux moyens d'accès à votre portefeuille : soit via le PIN et le système de "*Virtual Secure Element*" de Blockstream, soit via le CompactSeedQR.

Si vous optez pour l'option double avec le PIN, choisissez "*PIN*" et suivez les mêmes étapes que dans l'option 1 pour configurer votre code PIN.

Si vous préférez continuer uniquement avec le CompactSeedQR, sélectionnez "*SeedQR*".

![Image](assets/fr/22.webp)

Votre portefeuille est maintenant créé, vous pouvez passer aux étapes suivantes.

![Image](assets/fr/23.webp)

À chaque démarrage, cliquez sur le bouton "*QR Mode*" puis "*Scan SeedQR*".

![Image](assets/fr/24.webp)

Utilisez la caméra de l'appareil pour scanner votre seed sauvegardée sous forme de QR code.

![Image](assets/fr/25.webp)

Votre Jade est maintenant déverrouillé.

![Image](assets/fr/26.webp)

## Ajouter une passphrase BIP39

Une passphrase BIP39 est un mot de passe optionnel que vous pouvez choisir librement, et qui vient s'ajouter à votre phrase mnémonique pour renforcer la sécurité du portefeuille. Avec cette fonctionnalité activée, l'accès à votre portefeuille Bitcoin nécessitera à la fois la phrase mnémonique et la passphrase. Sans l'une ou l'autre, il serait impossible de récupérer le portefeuille.

Avant de configurer cette option sur votre Jade Plus, il est fortement recommandé de lire cet article pour bien comprendre le fonctionnement théorique de la passphrase et éviter les erreurs qui pourraient entraîner la perte de vos bitcoins :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Sur votre Jade encore verrouillé (la passphrase ne peut être renseignée que lorsque l'appareil n'est pas déverrouillé), accédez au menu "*Options*".

![Image](assets/fr/42.webp)

Sélectionnez "*BIP39 Passphrase*".

![Image](assets/fr/43.webp)

Dans l'option "*Frequency*", vous pouvez choisir si le Jade Plus vous demandera de renseigner votre passphrase à chaque démarrage : 
- "*Disabled*" désactive l'utilisation d'une passphrase ;
- "*Next Login Only*" nécessitera que vous reveniez dans ce menu pour activer la demande de votre passphrase au prochain démarrage. Cette option permet de ne pas révéler son utilisation ;
- "*Always Ask*" fait en sorte que le Jade vous demande systématiquement votre passphrase à chaque démarrage, ce qui vient donc révéler que votre portefeuille est protégé par une passphrase.

Choisissez l'option selon votre stratégie de sécurité. Personnellement, je sélectionne "*Always Ask*" pour l'exemple.

![Image](assets/fr/44.webp)

Vous avez ensuite le choix entre deux méthodes pour saisir votre passphrase :
- "*Manual*" : Un clavier virtuel vous permet d'entrer, caractère par caractère, des lettres (majuscules et minuscules), chiffres et symboles. C'est la méthode standard pour tous les hardware wallets ;
- "*WordList*" : Méthode spécifique conçue par Blockstream pour le Jade, qui accélère la saisie de la passphrase et augmente son entropie. Lors de la saisie, le système suggère des mots de la liste BIP39, ce qui facilite le déverouillage. Cette méthode génère automatiquement une phrase en concaténant les mots choisis, séparés par des espaces (exemple : `abandon ability able`).

Personnellement, je vous conseille d'utiliser la première méthode, car c'est le standard que vous retrouverez sur tous les autres supports de portefeuille.

![Image](assets/fr/45.webp)

Vous pouvez ensuite revenir à l'écran d'accueil et déverrouiller votre portefeuille normalement, soit en utilisant votre code PIN, soit en utilisant votre CompactSeedQR (comme vu précédemment). On vous demandera alors de renseigner votre passphrase.

![Image](assets/fr/46.webp)

Saisissez-la sur le clavier du Jade, et assurez-vous de faire une ou plusieurs sauvegardes sur des supports physiques (papier ou métal). Pour l'exemple, j'utilise une passphrase très faible, mais vous devez choisir une passphrase forte, aléatoire, incluant tous les types de caractères et suffisamment longue (comme un mot de passe fort).

![Image](assets/fr/47.webp)

Si votre passphrase est valide, confirmez.

![Image](assets/fr/48.webp)

Attention, les passphrases BIP39 sont sensibles à la casse et aux fautes de frappe. Si vous entrez une passphrase légèrement différente de celle configurée initialement, le Jade ne signalera pas d'erreur mais dérivera un autre ensemble de clés cryptographiques qui ne seront pas celles de votre portefeuille initial.

Il est donc important, lors de la configuration, de noter quelque part l'empreinte de votre clé maîtresse, qui se trouve en bas à droite de l'écran. Par exemple, avec ma passphrase `PBN`, mon empreinte de clé maîtresse est `3AD1AE65`.

![Image](assets/fr/49.webp)

À chaque fois que vous déverrouillez votre Jade avec votre passphrase, vérifiez que cette empreinte est bien la même que celle notée lors de la configuration. Si c'est le cas, votre passphrase est correcte et vous accédez au bon portefeuille Bitcoin. Si ce n'est pas le cas, vous n'êtes pas sur le bon portefeuille et vous devez essayer de nouveau, en veillant à ne pas faire d'erreur de saisie.

Avant de recevoir vos premiers bitcoins sur votre portefeuille, **je vous conseille vivement de réaliser un test de récupération à vide**. Notez une information de référence, telle que votre xpub ou la première adresse de réception, puis supprimez votre portefeuille sur le Jade Plus tant qu'il est encore vide (`Options -> Device -> Factory Reset`). Ensuite, essayez de restaurer votre portefeuille en utilisant vos sauvegardes papier de la phrase mnémonique et de l'éventuelle passphrase. Vérifiez que l'information témoin générée après la restauration correspond à celle que vous aviez notée initialement. Si c'est le cas, vous pouvez être assuré que vos sauvegardes papier sont fiables. Pour en savoir plus sur comment effectuer un test de récupération, je vous conseille de consulter cet autre tutoriel :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Configurer le portefeuille sur Sparrow Wallet

Dans ce tutoriel, je vous présente une utilisation avancée du Jade Plus en utilisant Sparrow Wallet. Cependant, ce hardware wallet est compatible avec de nombreux autres logiciels tels que Liana, Nunchuk, Specter, Green ou encore Keeper. Ces compatibilités varient dans les connexions : USB, Bluetooth ou encore par QR code (voir le tableau en introduction pour plus de détails).

Commencez par télécharger et installer Sparrow Wallet [depuis le site officiel](https://sparrowwallet.com/) sur votre ordinateur, si ce n'est pas déjà fait.

![Image](assets/fr/50.webp)

Assurez-vous de vérifier l'authenticité et l'intégrité du logiciel avant l'installation. Si vous ne savez pas comment procéder, vous pouvez consulter ce tutoriel :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Une fois Sparrow Wallet ouvert, cliquez sur l'onglet "*File*", puis sur "*New Wallet*".

![Image](assets/fr/51.webp)

Nommez votre portefeuille, puis cliquez sur "*Create Wallet*".

![Image](assets/fr/52.webp)

Sélectionnez "*Airgapped Hardware Wallet*".

![Image](assets/fr/53.webp)

Cliquez sur "*Scan...*" à côté de l'option "*Jade*".

![Image](assets/fr/54.webp)

Déverrouillez votre Jade Plus et, si vous en utilisez une, saisissez votre passphrase. Ensuite, allez dans le menu "*Options*", sélectionnez "*Wallet*", et cliquez sur "*Export Xpub*".

![Image](assets/fr/55.webp)

Votre Jade affichera votre Keystore via plusieurs QR codes. Scannez-les sur votre machine à l'aide de Sparrow.

![Image](assets/fr/56.webp)

Vous devriez maintenant voir votre xpub et l'empreinte de votre clé maîtresse, qui doit correspondre à celle indiquée sur votre Jade Plus. Cliquez sur "*Apply*".

![Image](assets/fr/57.webp)

Définissez un mot de passe fort pour sécuriser l'accès à votre portefeuille Sparrow Wallet. Ce mot de passe protégera vos clés publiques, vos adresses, vos étiquettes et l'historique de vos transactions contre les accès non autorisés. Il est conseillé de sauvegarder ce mot de passe dans un gestionnaire de mots de passe pour éviter de l'oublier.

![Image](assets/fr/58.webp)

Votre portefeuille est désormais correctement configuré sur Sparrow.

![Image](assets/fr/59.webp)

## Recevoir des bitcoins

Maintenant que votre Jade Plus est configuré, vous êtes prêt à recevoir vos premiers sats sur votre nouveau portefeuille Bitcoin. Pour ce faire, sur Sparrow, cliquez sur le menu "*Receive*".

![Image](assets/fr/60.webp)

Sparrow affichera la première adresse de réception vierge de votre portefeuille.

![Image](assets/fr/61.webp)

Avant de l'utiliser, nous allons la vérifier sur l'écran du Jade Plus pour nous assurer qu'elle appartient bien à notre portefeuille Bitcoin. Sur le Jade, cliquez sur "*Scan QR*", puis scannez le QR code de l'adresse affiché sur Sparrow.

![Image](assets/fr/62.webp)

Vérifiez que l'adresse affichée sur l'écran de votre Jade correspond bien à celle affichée sur Sparrow Wallet. Si c'est le cas, cliquez sur la coche pour continuer.

![Image](assets/fr/63.webp)

Votre hardware wallet va ensuite confirmer que cette adresse fait partie de votre portefeuille et qu'il détient bien la clé privée associée.

![Image](assets/fr/64.webp)

Si l'adresse est validée par votre Jade, vous pouvez désormais l'utiliser pour recevoir des bitcoins. Lorsque la transaction sera diffusée sur le réseau, elle apparaîtra sur Sparrow. Attendez d'obtenir suffisamment de confirmations pour considérer la transaction comme définitive.

![Image](assets/fr/65.webp)

## Envoyer des bitcoins

Maintenant que vous avez quelques sats dans votre portefeuille, vous pouvez également en envoyer. Pour ce faire, cliquez sur le menu "*UTXOs*".

![Image](assets/fr/66.webp)

Sélectionnez les UTXOs que vous souhaitez utiliser en tant qu'inputs pour cette transaction, puis cliquez sur "*Send Selected*".

![Image](assets/fr/67.webp)

Entrez l'adresse du destinataire, une étiquette pour vous rappeler de l'objectif de la transaction et le montant que vous souhaitez envoyer à cette adresse.

![Image](assets/fr/68.webp)

Ajustez le taux de frais en fonction de l'état actuel du marché, puis cliquez sur "*Create Transaction*".

![Image](assets/fr/69.webp)

Vérifiez que tous les paramètres de la transaction sont corrects, puis cliquez sur "*Finalize Transaction for Signing*".

![Image](assets/fr/70.webp)

Cliquez sur "*Show QR*" pour afficher la PSBT (*Partially Signed Bitcoin Transaction*). Sparrow a construit la transaction, mais il manque encore les signatures pour déverrouiller les bitcoins utilisés en input. Ces signatures ne peuvent être réalisées que par le Jade Plus, qui héberge votre seed donnant accès aux clés privées nécessaires pour signer la transaction.

![Image](assets/fr/71.webp)

Sur votre Jade Plus, cliquez sur "*Scan QR*" pour scanner la PSBT affichée sur Sparrow.

![Image](assets/fr/72.webp)

Confirmez que l'adresse de réception et le montant envoyé sont corrects, puis cliquez sur la flèche pour valider.

![Image](assets/fr/73.webp)

Assurez-vous que le montant des frais est celui que vous avez choisi, puis cliquez sur l'icône de la coche en haut à gauche de l'interface pour signer la transaction.

![Image](assets/fr/74.webp)

Sur Sparrow Wallet, cliquez sur "*Scan QR*" et scannez le QR code affiché sur votre Jade.

![Image](assets/fr/75.webp)

Votre transaction signée est prête à être diffusée sur le réseau Bitcoin pour être ensuite incluse dans un bloc par un mineur. Si tout est correct, cliquez sur "*Broadcast Transaction*".

![Image](assets/fr/76.webp)

Votre transaction a été diffusée et est en attente de confirmations.

![Image](assets/fr/77.webp)

Félicitations, vous savez dorénavant comment configurer et utiliser le Jade Plus en mode QR. Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci !

Pour aller plus loin, je vous recommande de consulter cet autre tutoriel sur le Jade Plus, où nous le configurons en Bluetooth avec l'application mobile Green :

https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0
