---
name: Ledger Flex
description: Configuration et utilisation de la Ledger Flex
---
![cover](assets/cover.webp)

Un hardware wallet est un dispositif électronique dédié à la gestion et à la sécurisation des clés privées d'un portefeuille Bitcoin. Contrairement aux portefeuilles logiciels (ou portefeuilles chauds) installés sur des machines généralistes souvent connectées à Internet, les hardware wallets permettent d'isoler physiquement les clés privées, ce qui réduit les risques de piratage et de vol.

Le principal objectif d'un hardware wallet est de réduire au maximum les fonctionnalités de l'appareil afin de minimiser sa surface d'attaque. Moins de surface d'attaque, ça veut également dire moins de potentiels vecteurs d'attaque, c'est-à-dire moins de points faibles dans le système que les attaquants pourraient exploiter pour accéder aux bitcoins. 

Il est recommandé d'utiliser un hardware wallet pour sécuriser vos bitcoins, surtout si vous en détenez des quantités importantes, que ce soit en valeur absolue ou en proportion de votre patrimoine total.

Les hardware wallets s’utilisent en combinaison avec un logiciel de gestion de portefeuille sur un ordinateur ou un smartphone. Ce dernier permet de gérer la création des transactions, mais la signature cryptographique nécessaire pour rendre valide ces transactions se fait uniquement au sein du hardware wallet. Cela signifie que les clés privées ne sont jamais exposées à un environnement potentiellement vulnérable.

Les hardware wallets offrent une double protection pour l'utilisateur : d'une part, ils sécurisent vos bitcoins contre les attaques à distance en gardant les clés privées hors ligne, et d'autre part, ils offrent généralement une meilleure résistance physique face aux tentatives d'extraction des clés. Et c'est justement sur ces 2 critères de sécurité que l'on peut juger et classer les différents modèles existants sur le marché.

Dans ce tutoriel, je vous propose de découvrir une de ces solutions : le **Ledger Flex**.

![LEDGER FLEX](assets/notext/01.webp)

## Présentation du Ledger Flex

Le Ledger Flex est un hardware wallet produit par l’entreprise française Ledger, commercialisé au tarif de 249 €.

![LEDGER FLEX](assets/notext/02.webp)

Il dispose d'un grand écran tactile E Ink, une technologie d’affichage en noir et blanc. C'est la même technologie que vous pouvez retrouver sur les liseuses électroniques. L'écran E Ink permet un affichage clair et lisible, même en plein soleil, et consomme très peu d’énergie, voire pas du tout lorsque l'écran est figé. Cela fonctionne en utilisant des microcapsules contenant des particules de pigments noirs et blancs. Lorsqu'une charge électrique est appliquée, les particules noires ou blanches se déplacent vers la surface de l'écran, et permettent ainsi de former du texte ou des images.

Le Ledger Flex est équipé d’une puce certifiée CC EAL6+ ("*secure element*"), ce qui vous offre une protection avancée contre les attaques physiques contre le hardware. L'écran est directement contrôlé par cette puce.

Un point de critique souvent soulevé est que le code de cette puce n'est pas open-source, ce qui impose une certaine confiance dans l’intégrité de ce composant. Néanmoins, cet élément est audité par des experts indépendants.

En termes d’usage, le Ledger Flex offre plusieurs options de connectivité : Bluetooth, USB-C et NFC. L'écran de grande taille permet de bien vérifier les détails de vos transactions. Ledger se distingue également de ses concurrents par son adoption rapide des nouvelles fonctionnalités de Bitcoin, comme Miniscript par exemple.

Après l'avoir testé, je suis impressionné par la qualité du produit. L'expérience utilisateur est excellente et le dispositif est intuitif. C'est un excellent hardware wallet. Toutefois, il présente 2 inconvénients majeurs selon moi : l'impossibilité de vérifier le code de la puce et évidemment son prix, nettement supérieur à celui des concurrents. Pour comparaison, le modèle le plus avancé de Foundation est vendu à 199 $, celui de Coinkite à 219,99 $, tandis que la dernière Trezor, dotée également d'un grand écran tactile, est proposée à 169 €.

## Comment acheter un Ledger Flex ?

Le Ledger Flex est disponible à la vente [sur le site officiel](https://shop.ledger.com/pages/ledger-flex). Pour l'acheter dans une boutique physique, vous pouvez également retrouver [la liste des revendeurs certifiés](https://www.ledger.com/reseller) sur le site de Ledger.

## Prérequis

Une fois votre Ledger Flex reçu, la première étape consiste à examiner l'emballage pour s'assurer qu'il n'a pas été ouvert.

![LEDGER FLEX](assets/notext/03.webp)

L'emballage du Ledger doit comporter 2 bandes de scellement. Si ces bandes sont manquantes ou endommagées, cela pourrait indiquer que le hardware wallet a été compromis et qu'il pourrait ne pas être authentique.

![LEDGER FLEX](assets/notext/04.webp)

À l'ouverture, vous devriez trouver les éléments suivants dans la boîte : 
- Le Ledger Flex ;
- Un câble USB-C ;
- Une notice d'utilisation ;
- Des cartons pour inscrire votre phrase mnémonique.

![LEDGER FLEX](assets/notext/05.webp)

Pour ce tutoriel, vous aurez besoin de 2 logiciels : Ledger Live pour initialiser le Ledger Flex, et Sparrow Wallet pour gérer votre portefeuille Bitcoin. Téléchargez [Ledger Live](https://www.ledger.com/ledger-live) et [Sparrow Wallet](https://sparrowwallet.com/download/) depuis leurs sites officiels.

![LEDGER FLEX](assets/notext/06.webp)

Pour ces deux logiciels, je vous recommande fortement de vérifier à la fois leur authenticité (avec GnuPG) et leur intégrité (via le hash) avant de les installer sur votre machine. Si vous ne savez pas comment le faire, vous pouvez suivre cet autre tutoriel :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Comment initialiser un Ledger Flex avec Ledger Live ?

Allumez votre Ledger Flex en cliquant quelques secondes sur le bouton latéral droit.

![LEDGER FLEX](assets/notext/07.webp)

Faites défiler les différentes pages de présentation.

![LEDGER FLEX](assets/notext/08.webp)

Sélectionnez l'option "*Set up without Ledger Live*", puis cliquez sur le bouton "*Skip Ledger Live*".

![LEDGER FLEX](assets/notext/09.webp)

On vous demande ensuite de choisir un nom pour votre Ledger. Cliquez sur "*Set name*", puis notez le nom de votre choix.

![LEDGER FLEX](assets/notext/10.webp)

Choisissez le code PIN de votre appareil, qui vous servira à déverrouiller votre Ledger. C'est donc une protection contre les accès physiques non autorisés. Ce code PIN n'intervient pas dans la dérivation des clés cryptographiques de votre portefeuille. Ainsi, même sans accès à ce code PIN, la possession de votre phrase mnémonique de 24 mots vous permettra de retrouver l'accès à vos bitcoins.

Il est recommandé de choisir un code PIN de 8 chiffres, le plus aléatoire possible. Assurez-vous également de sauvegarder ce code dans un lieu distinct de celui où est stocké votre Ledger Flex (par exemple, dans un gestionnaire de mot de passe).

![LEDGER FLEX](assets/notext/11.webp)

Entrez votre PIN une seconde fois pour le confirmer.

![LEDGER FLEX](assets/notext/12.webp)

Vous serez ensuite invité à choisir entre récupérer un portefeuille existant ou en créer un nouveau. Dans ce tutoriel, nous abordons la création d'un nouveau portefeuille à partir de zéro, donc sélectionnez l'option "*Set up as a new Ledger*" pour générer une nouvelle phrase mnémonique.

![LEDGER FLEX](assets/notext/13.webp)

Votre Flex vous fournira des instructions sur la manière de gérer votre phrase de récupération.

**Cette phrase mnémonique donne un accès complet et non restreint à tous vos bitcoins**. N'importe qui en possession de cette phrase peut subtiliser vos fonds, même sans accès physique à votre Ledger. La phrase de 24 mots permet de restaurer l'accès à vos bitcoins en cas de perte, vol ou casse de votre Ledger Flex. Il est donc très important de la sauvegarder soigneusement et de la stocker dans un endroit sécurisé.

Vous pouvez l'inscrire sur le papier cartonné fourni avec votre Ledger, ou bien pour plus de sécurité, je vous recommande de la graver sur un support en acier inoxydable afin de la protéger contre les risques d'incendies, d'inondations ou d'écroulements.

Vous pouvez parcourir ces instructions et passer les pages en touchant l'écran.

![LEDGER FLEX](assets/notext/14.webp)

La Ledger va créer votre phrase mnémonique en utilisant son générateur de nombres aléatoires. Assurez-vous de ne pas être observé durant cette opération. Notez les mots fournis par la Ledger sur le support physique de votre choix. Selon votre stratégie de sécurisation, vous pouvez envisager de réaliser plusieurs copies physiques complètes de la phrase (mais surtout, ne la divisez pas). Il est important de conserver les mots numérotés et dans l'ordre séquentiel.

***Évidemment, vous ne devez jamais partager ces mots sur internet, contrairement à ce que je fais dans ce tutoriel. Ce portefeuille en exemple sera utilisé uniquement sur le Testnet et sera supprimé à l'issue du tutoriel.***

![LEDGER FLEX](assets/notext/15.webp)

Pour passer au groupe de mots suivants, cliquez sur le bouton "*Next*". Une fois tous les mots notés, cliquez sur le bouton "*Done*" pour passer à l'étape suivante.

![LEDGER FLEX](assets/notext/16.webp)

Cliquez sur le bouton "*Start confirmation*", puis sélectionnez les mots de votre phrase mnémonique en fonction de leur ordre pour confirmer que vous les avez correctement notés. Continuez cette procédure jusqu'au 24e mot.

![LEDGER FLEX](assets/notext/17.webp)

Si la phrase que vous confirmez correspond exactement à celle que le Flex vous a fournie à l'étape précédente, vous pourrez poursuivre. Si ce n'est pas le cas, cela indique que votre sauvegarde physique de la phrase mnémonique est incorrecte et que vous devez recommencer le processus.

![LEDGER FLEX](assets/notext/18.webp)

Et voilà, votre seed a été correctement créée sur votre Ledger Flex. Avant de procéder à la création d'un nouveau portefeuille Bitcoin à partir de cette seed, explorons ensemble les paramètres de l'appareil.

## Comment modifier les paramètres de votre Ledger ?

Pour verrouiller et déverrouiller votre Ledger, appuyez sur le bouton latéral. Il vous sera ensuite demandé de saisir le code PIN que vous avez défini lors de l'étape précédente.

![LEDGER FLEX](assets/notext/19.webp)

Pour accéder aux paramètres, cliquez sur le symbole de roue crantée en bas à gauche de votre appareil.

![LEDGER FLEX](assets/notext/20.webp)

Le menu "*Name*" vous permet de changer le nom de votre Ledger.

![LEDGER FLEX](assets/notext/21.webp)

Dans "*About this Ledger*", vous trouverez des informations sur votre Flex.

![LEDGER FLEX](assets/notext/22.webp)

Dans le menu "*Lock screen*", vous avez la possibilité de modifier l'image affichée sur l'écran de verrouillage en sélectionnant "*Customize lock screen picture*". Grâce à la technologie de l'écran E Ink de l'appareil, il est possible de garder l'écran constamment allumé sans consommer de batterie. Les écrans E Ink n'utilisent pas d'énergie pour maintenir une image statique. Ils en consomment en revanche lors des changements d'affichage.

Le sous-menu "*Auto-lock*" vous permet de configurer et d'activer le verrouillage automatique de votre Ledger après une période d'inactivité déterminée.

![LEDGER FLEX](assets/notext/23.webp)

Le menu "*Sounds*" vous permet d'activer ou de désactiver les sons de votre Flex. Et dans le menu "Language", vous pouvez changer la langue d'affichage.

![LEDGER FLEX](assets/notext/24.webp)

En cliquant sur la flèche de droite, vous pouvez accéder aux autres paramètres. "*Change PIN*" vous permet de changer votre code PIN.

![LEDGER FLEX](assets/notext/25.webp)

Les menus "*Bluetooth*" et "*NFC*" vous permettent de gérer ces communications.

![LEDGER FLEX](assets/notext/26.webp)

Dans "*Battery*" vous pouvez notamment paramétrer un arrêt automatique de la Ledger.

![LEDGER FLEX](assets/notext/27.webp)

La section "*Advanced*" vous donne accès à des paramètres de sécurité plus poussés. Il est conseillé de maintenir l'option "*PIN shuffle*" activée pour renforcer la sécurité. C'est également dans ce menu que vous pouvez configurer une passphrase BIP39.

![LEDGER FLEX](assets/notext/28.webp)

La passphrase est un mot de passe optionnel qui, combiné à la phrase de récupération, offre une couche de sécurité supplémentaire pour votre portefeuille.

Pour le moment, votre portefeuille est généré à partir d’une phrase mnémonique constituée de 24 mots. Cette phrase de récupération est très importante, car elle permet de restaurer l'ensemble des clés de votre portefeuille en cas de perte. Cependant, elle constitue un point de défaillance unique (SPOF). Si elle est compromise, les bitcoins sont en danger. C'est ici qu'intervient la passphrase. C'est un mot de passe optionnel, que vous pouvez choisir arbitrairement, qui s'ajoute à la phrase mnémonique pour renforcer la sécurité du portefeuille. 

La passphrase ne doit pas être confondue avec le code PIN. Elle joue un rôle dans la dérivation de vos clés cryptographiques. Elle fonctionne en tandem avec la phrase mnémonique, en modifiant la graine à partir de laquelle sont générées les clés. Ainsi, même si une personne obtient votre phrase de 24 mots, sans la passphrase, elle ne peut pas accéder à vos fonds. L'utilisation d'une passphrase crée essentiellement un nouveau portefeuille avec des clés distinctes. Modifier (même légèrement) la passphrase générera un portefeuille différent.

![LEDGER FLEX](assets/notext/29.webp)

La passphrase est un outil très puissant pour renforcer la sécurité de vos bitcoins. Toutefois, il est très important de comprendre son fonctionnement avant de l'implémenter, afin d'éviter de perdre l'accès à votre portefeuille. C'est pour cela que je vous explique tout dans un autre tutoriel dédié :

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49

Enfin, la dernière page de paramètres vous permet de réinitialiser votre Ledger. Ne procédez à cette réinitialisation que si vous êtes certain qu'il ne contient aucune clé sécurisant des bitcoins, car vous risqueriez de perdre définitivement l'accès à vos fonds.

![LEDGER FLEX](assets/notext/30.webp)

## Comment installer l'application Bitcoin ?

Commencez par lancer le logiciel Ledger Live sur votre ordinateur, puis connectez et déverrouillez votre Ledger Flex.

![LEDGER FLEX](assets/notext/31.webp)

Sur Ledger Live, allez dans le menu "*My Ledger*". On vous demande d'autoriser l'accès à votre Flex.

![LEDGER FLEX](assets/notext/32.webp)

Validez l'accès sur votre Ledger en cliquant sur le bouton "*Allow*".

![LEDGER FLEX](assets/notext/33.webp)

Tout d'abord, si le firmware de votre Ledger Flex n'est pas à jour, Ledger Live vous proposera automatiquement de le mettre à jour. Le cas échéant, cliquez sur "*Update firmware*", puis sur "*Install update*" pour lancer l'installation.

![LEDGER FLEX](assets/notext/34.webp)

Sur votre Ledger, cliquez sur le bouton "*Install*", puis patientez le temps de l'installation.

![LEDGER FLEX](assets/notext/35.webp)

Le firmware de votre Ledger Flex est bien à jour.

![LEDGER FLEX](assets/notext/36.webp)

Si vous le souhaitez, vous pouvez modifier le fond d'écran de verrouillage de votre Ledger Flex. Pour ce faire, cliquez sur "*Add >*".

![LEDGER FLEX](assets/notext/37.webp)

Cliquez sur le bouton "*Upload from computer*" et choisissez votre fond d'écran parmi vos photos.

![LEDGER FLEX](assets/notext/38.webp)

Vous pouvez recadrer votre image.

![LEDGER FLEX](assets/notext/39.webp)

Choisissez un contraste parmi les différentes options, puis cliquez sur "*Confirm contrast*".

![LEDGER FLEX](assets/notext/40.webp)

Sur votre Flex, cliquez sur le bouton "*Load picture*".

![LEDGER FLEX](assets/notext/41.webp)

Si l'image vous convient, cliquez sur "*Keep*" pour la mettre en fond d'écran de verrouillage.

![LEDGER FLEX](assets/notext/42.webp)

Enfin, nous allons ajouter l'application Bitcoin. Pour ce faire, sur Ledger Live, cliquez sur le bouton "*Install*" à côté de "*Bitcoin (BTC)*".

![LEDGER FLEX](assets/notext/43.webp)

L'application va s'installer sur votre Flex.

![LEDGER FLEX](assets/notext/44.webp)

À partir de maintenant, vous n'aurez plus besoin du logiciel Ledger Live pour la gestion courante de votre portefeuille. Vous pourrez y revenir occasionnellement pour mettre à jour le firmware lorsque de nouvelles versions seront disponibles. Pour le reste, nous allons utiliser Sparrow Wallet qui est un outil bien plus complet pour gérer efficacement un portefeuille Bitcoin.

## Comment configurer un nouveau portefeuille Bitcoin avec Sparrow ?

Ouvrez Sparrow Wallet et passez les pages d'introduction pour accéder à l'écran d'accueil. Vérifiez que vous êtes correctement connecté à un nœud en observant l'interrupteur situé en bas à droite de l'écran.

![LEDGER FLEX](assets/notext/45.webp)

Je vous recommande vivement d'utiliser votre propre nœud Bitcoin. Dans ce tutoriel, j'utilise un nœud public (jaune) car je suis sur le testnet, mais pour une utilisation normale, il est préférable d'opter pour un Bitcoin Core local (vert) ou un serveur Electrum associé à un nœud distant (bleu).

Cliquez sur le menu "*File*" puis "*New Wallet*".

![LEDGER FLEX](assets/notext/46.webp)

Choisissez un nom pour ce portefeuille, puis cliquez sur "*Create Wallet*".

![LEDGER FLEX](assets/notext/47.webp)

Dans le menu déroulant "*Script Type*", sélectionnez le type de script qui sera utilisé pour sécuriser vos bitcoins. Je vous recommande d'opter pour "*Taproot*", ou à défaut, "*Native SegWit*".

![LEDGER FLEX](assets/notext/48.webp)

Cliquez sur le bouton "*Connected Hardware Wallet*".

![LEDGER FLEX](assets/notext/49.webp)

Connectez votre Ledger Flex à l'ordinateur, déverrouillez-le avec votre code PIN, puis ouvrez l'application "*Bitcoin*". Dans ce tutoriel, j'utilise l'application "*Bitcoin Testnet*", mais la procédure reste identique pour le mainnet.

![LEDGER FLEX](assets/notext/50.webp)

Sur Sparrow, cliquez sur le bouton "*Scan*".

![LEDGER FLEX](assets/notext/51.webp)

Puis cliquez sur "*Import Keystore*".

![LEDGER FLEX](assets/notext/52.webp)

Vous pouvez maintenant voir les détails de votre portefeuille, y compris la clé publique étendue de votre premier compte. Cliquez sur le bouton "*Apply*" pour finaliser la création du portefeuille.

![LEDGER FLEX](assets/notext/53.webp)

Choisissez un mot de passe fort pour sécuriser l'accès à Sparrow Wallet. Ce mot de passe assurera la sécurité de l'accès aux données de votre portefeuille sur Sparrow, ce qui permet de protéger vos clés publiques, vos adresses, vos labels et l'historique de vos transactions contre tout accès non autorisé.

Je vous conseille de sauvegarder ce mot de passe dans un gestionnaire de mots de passe pour ne pas l'oublier.

![LEDGER FLEX](assets/notext/54.webp)

Et voilà, votre portefeuille est bien créé !

![LEDGER FLEX](assets/notext/55.webp)

***Avant de recevoir vos premiers bitcoins sur votre portefeuille, je vous conseille vivement de réaliser un test de récupération à vide. Notez une information de référence, telle que votre xpub, puis réinitialisez votre Ledger Flex tant que le portefeuille est encore vide. Ensuite, essayez de restaurer votre portefeuille sur la Ledger en utilisant vos sauvegardes papier. Vérifiez que la xpub générée après la restauration correspond à celle que vous aviez notée initialement. Si c'est le cas, vous pouvez être assuré que vos sauvegardes papier sont fiables.***

Pour en savoir plus sur comment effectuer un test de récupération, je vous conseille de consulter cet autre tutoriel :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Comment recevoir des bitcoins avec la Ledger Flex ?

Cliquez sur l'onglet "*Receive*".

![LEDGER FLEX](assets/notext/56.webp)

Connectez votre Ledger Flex à l'ordinateur, déverrouillez-le avec votre code PIN, puis ouvrez l'application "*Bitcoin*".

![LEDGER FLEX](assets/notext/57.webp)

Avant d'utiliser l'adresse proposée par Sparrow Wallet, vérifiez-la sur l'écran de votre Ledger Flex. Cette pratique vous permet de confirmer que l'adresse affichée sur Sparrow n'est pas frauduleuse et que le Ledger détient bien la clé privée nécessaire pour dépenser ultérieurement les bitcoins sécurisés avec cette adresse.

Pour effectuer cette vérification, cliquez sur le bouton "*Display Address*".

![LEDGER FLEX](assets/notext/58.webp)

Vérifiez que l'adresse affichée sur votre Ledger Flex correspond à celle indiquée sur Sparrow Wallet. Il est également recommandé de réaliser cette vérification juste avant de communiquer votre adresse à l'envoyeur, afin d'être sûr de sa validité.

![LEDGER FLEX](assets/notext/59.webp)

Vous pouvez ajouter un "*Label*" pour décrire la source des bitcoins qui seront sécurisés avec cette adresse. C'est une bonne pratique qui vous permet de mieux gérer vos UTXOs.

![LEDGER FLEX](assets/notext/60.webp)

Pour plus d'informations sur l'étiquetage, je vous conseille également de découvrir cet autre tutoriel :

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Vous pouvez ensuite utiliser cette adresse pour recevoir des bitcoins.

![LEDGER FLEX](assets/notext/61.webp)

## Comment envoyer des bitcoins avec la Ledger Flex ?

Maintenant que vous avez reçu vos premiers sats sur votre portefeuille sécurisé avec le Flex, vous pouvez également les dépenser ! Connectez votre Ledger à votre ordinateur, déverrouillez-le, lancez Sparrow Wallet, puis allez dans l'onglet "*Send*" pour construire une nouvelle transaction.

![LEDGER FLEX](assets/notext/62.webp)

Si vous souhaitez faire du "*coin control*", c'est-à-dire choisir spécifiquement quels UTXOs consommer dans la transaction, rendez-vous dans l'onglet "*UTXOs*". Sélectionnez les UTXOs que vous souhaitez dépenser, puis cliquez sur "*Send Selected*". Vous serez redirigé vers le même écran de l'onglet "*Send*", mais avec vos UTXOs déjà sélectionnés pour la transaction.

![LEDGER FLEX](assets/notext/63.webp)

Entrez l'adresse de destination. Vous pouvez également entrer plusieurs adresses en cliquant sur le bouton "*+ Add*".

![LEDGER FLEX](assets/notext/64.webp)

Notez un "*Label*" pour vous souvenir de l'objet de cette dépense.

![LEDGER FLEX](assets/notext/65.webp)

Choisissez le montant envoyé à cette adresse.

![LEDGER FLEX](assets/notext/66.webp)

Ajustez le taux de frais de votre transaction en fonction du marché du moment.

![LEDGER FLEX](assets/notext/67.webp)

Assurez-vous que tous les paramètres de votre transaction sont corrects, puis cliquez sur "*Create Transaction*".

![LEDGER FLEX](assets/notext/68.webp)

Si tout vous convient, cliquez sur "*Finalize Transaction for Signing*".

![LEDGER FLEX](assets/notext/69.webp)

Cliquez sur "*Sign*".

![LEDGER FLEX](assets/notext/70.webp)

Cliquez sur "*Sign*" à côté de votre Ledger Flex.

![LEDGER FLEX](assets/notext/71.webp)

Vérifiez les paramètres de la transaction sur l'écran de votre Flex, notamment l'adresse de réception du destinataire, le montant envoyé et le montant des frais.

![LEDGER FLEX](assets/notext/72.webp)

Pour signer, maintenez votre doigt sur le bouton "*Hold to sign*".

![LEDGER FLEX](assets/notext/73.webp)

Votre transaction est désormais signée. Cliquez sur "*Broadcast Transaction*" pour la diffuser sur le réseau Bitcoin.

![LEDGER FLEX](assets/notext/74.webp)

Vous pouvez la retrouver dans l'onglet "*Transactions*" de Sparrow Wallet.

![LEDGER FLEX](assets/notext/75.webp)

Félicitations, vous êtes maintenant au point sur l'utilisation de base de la Ledger Flex avec Sparrow Wallet ! Dans un prochain tutoriel, nous verrons comment utiliser la Ledger Flex avec Liana pour tirer parti de Miniscript.

Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci beaucoup !
