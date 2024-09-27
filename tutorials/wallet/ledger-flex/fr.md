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

01

## Présentation du Ledger Flex

Le Ledger Flex est un hardware wallet produit par l’entreprise française Ledger, commercialisé au tarif de 249 €.

02

Il dispose d'un grand écran tactile E Ink, une technologie d’affichage en noir et blanc. C'est la même technologie que vous pouvez retrouver sur les liseuses électroniques. L'écran E Ink permet un affichage clair et lisible, même en plein soleil, et consomme très peu d’énergie, voire pas du tout lorsque l'écran est figé. Cela fonctionne en utilisant des microcapsules contenant des particules de pigments noirs et blancs. Lorsqu'une charge électrique est appliquée, les particules noires ou blanches se déplacent vers la surface de l'écran, et permettent ainsi de former du texte ou des images.

Le Ledger Flex est équipé d’une puce certifiée CC EAL6+ ("*secure element*"), ce qui vous offre une protection avancée contre les attaques physiques contre le hardware. L'écran est directement contrôlé par cette puce.

Un point de critique souvent soulevé est que le code de cette puce n'est pas open-source, ce qui impose une certaine confiance dans l’intégrité de ce composant. Néanmoins, cet élément est audité par des experts indépendants.

En termes d’usage, le Ledger Flex offre plusieurs options de connectivité : Bluetooth, USB-C et NFC. L'écran de grande taille permet de bien vérifier les détails de vos transactions. Ledger se distingue également de ses concurrents par son adoption rapide des nouvelles fonctionnalités de Bitcoin, comme Miniscript par exemple.

Après l'avoir testé, je suis impressionné par la qualité du produit. L'expérience utilisateur est excellente et le dispositif est intuitif. C'est un excellent hardware wallet. Toutefois, il présente 2 inconvénients majeurs selon moi : l'impossibilité de vérifier le code de la puce et évidemment son prix, nettement supérieur à celui des concurrents. Pour comparaison, le modèle le plus avancé de Foundation est vendu à 199 $, celui de Coinkite à 219,99 $, tandis que la dernière Trezor, dotée également d'un grand écran tactile, est proposée à 169 €.

## Comment acheter un Ledger Flex ?

Le Ledger Flex est disponible à la vente [sur le site officiel](https://shop.ledger.com/pages/ledger-flex). Pour l'acheter dans une boutique physique, vous pouvez également retrouver [la liste des revendeurs certifiés](https://www.ledger.com/reseller) sur le site de Ledger.

## Prérequis

Une fois votre Ledger Flex reçu, la première étape consiste à examiner l'emballage pour s'assurer qu'il n'a pas été ouvert.

03

L'emballage du Ledger doit comporter 2 bandes de scellement. Si ces bandes sont manquantes ou endommagées, cela pourrait indiquer que le hardware wallet a été compromis et qu'il pourrait ne pas être authentique.

04

À l'ouverture, vous devriez trouver les éléments suivants dans la boîte : 
- Le Ledger Flex ;
- Un câble USB-C ;
- Une notice d'utilisation ;
- Des cartons pour inscrire votre phrase mnémonique.

05

Pour ce tutoriel, vous aurez besoin de 2 logiciels : Ledger Live pour initialiser le Ledger Flex, et Sparrow Wallet pour gérer votre portefeuille Bitcoin. Téléchargez [Ledger Live](https://www.ledger.com/ledger-live) et [Sparrow Wallet](https://sparrowwallet.com/download/) depuis leurs sites officiels.

06

Nous vous proposerons prochainement un tutoriel pour savoir comment vérifier l'authenticité et l'intégrité d'un logiciel que vous téléchargez. Je vous conseille vivement de le faire ici pour Ledger Live et Sparrow.

## Comment initialiser un Ledger Flex avec Ledger Live ?

Allumez votre Ledger Flex en cliquant quelques secondes sur le bouton latéral droit.

07

Faites défiler les différentes pages de présentation.

08

Sélectionnez l'option "*Set up without Ledger Live*", puis cliquez sur le bouton "*Skip Ledger Live*".

09

On vous demande ensuite de choisir un nom pour votre Ledger. Cliquez sur "*Set name*", puis notez le nom de votre choix.

10

Choisissez le code PIN de votre appareil, qui vous servira à déverrouiller votre Ledger. C'est donc une protection contre les accès physiques non autorisés. Ce code PIN n'intervient pas dans la dérivation des clés cryptographiques de votre portefeuille. Ainsi, même sans accès à ce code PIN, la possession de votre phrase mnémonique de 24 mots vous permettra de retrouver l'accès à vos bitcoins.

Il est recommandé de choisir un code PIN de 8 chiffres, le plus aléatoire possible. Assurez-vous également de sauvegarder ce code dans un lieu distinct de celui où est stocké votre Ledger Flex (par exemple, dans un gestionnaire de mot de passe).

11

Entrez votre PIN une seconde fois pour le confirmer.

12

Vous serez ensuite invité à choisir entre récupérer un portefeuille existant ou en créer un nouveau. Dans ce tutoriel, nous abordons la création d'un nouveau portefeuille à partir de zéro, donc sélectionnez l'option "*Set up as a new Ledger*" pour générer une nouvelle phrase mnémonique.

13

Votre Flex vous fournira des instructions sur la manière de gérer votre phrase de récupération.

**Cette phrase mnémonique donne un accès complet et non restreint à tous vos bitcoins**. N'importe qui en possession de cette phrase peut subtiliser vos fonds, même sans accès physique à votre Ledger. La phrase de 24 mots permet de restaurer l'accès à vos bitcoins en cas de perte, vol ou casse de votre Ledger Flex. Il est donc très important de la sauvegarder soigneusement et de la stocker dans un endroit sécurisé.

Vous pouvez l'inscrire sur le papier cartonné fourni avec votre Ledger, ou bien pour plus de sécurité, je vous recommande de la graver sur un support en acier inoxydable afin de la protéger contre les risques d'incendies, d'inondations ou d'écroulements.

Vous pouvez parcourir ces instructions et passer les pages en touchant l'écran.

14

La Ledger va créer votre phrase mnémonique en utilisant son générateur de nombres aléatoires. Assurez-vous de ne pas être observé durant cette opération. Notez les mots fournis par la Ledger sur le support physique de votre choix. Selon votre stratégie de sécurisation, vous pouvez envisager de réaliser plusieurs copies physiques complètes de la phrase (mais surtout, ne la divisez pas). Il est important de conserver les mots numérotés et dans l'ordre séquentiel.

*Évidemment, vous ne devez jamais partager ces mots sur internet, contrairement à ce que je fais dans ce tutoriel. Ce portefeuille en exemple sera utilisé uniquement sur le Testnet et sera supprimé à l'issue du tutoriel.*

15

Pour passer au groupe de mots suivants, cliquez sur le bouton "*Next*". Une fois tous les mots notés, cliquez sur le bouton "*Done*" pour passer à l'étape suivante.

16

Cliquez sur le bouton "*Start confirmation*", puis sélectionnez les mots de votre phrase mnémonique en fonction de leur ordre pour confirmer que vous les avez correctement notés. Continuez cette procédure jusqu'au 24e mot.

17

Si la phrase que vous confirmez correspond exactement à celle que le Flex vous a fournie à l'étape précédente, vous pourrez poursuivre. Si ce n'est pas le cas, cela indique que votre sauvegarde physique de la phrase mnémonique est incorrecte et que vous devez recommencer le processus.

18

Et voilà, votre seed a été correctement créée sur votre Ledger Flex. Avant de procéder à la création d'un nouveau portefeuille Bitcoin à partir de cette seed, explorons ensemble les paramètres de l'appareil.

## Comment modifier les paramètres de votre Ledger ?

Pour verrouiller et déverrouiller votre Ledger, appuyez sur le bouton latéral. Il vous sera ensuite demandé de saisir le code PIN que vous avez défini lors de l'étape précédente.

18

Pour accéder aux paramètres, cliquez sur le symbole de roue crantée en bas à gauche de votre appareil.

19

Le menu "*Name*" vous permet de changer le nom de votre Ledger.

20

Dans "*About this Ledger*", vous trouverez des informations sur votre Flex.

21

Dans le menu "*Lock screen*", vous avez la possibilité de modifier l'image affichée sur l'écran de verrouillage en sélectionnant "*Customize lock screen picture*". Grâce à la technologie de l'écran E Ink de l'appareil, il est possible de garder l'écran constamment allumé sans consommer de batterie. Les écrans E Ink n'utilisent pas d'énergie pour maintenir une image statique. Ils en consomment en revanche lors des changements d'affichage.

Le sous-menu "*Auto-lock*" vous permet de configurer et d'activer le verrouillage automatique de votre Ledger après une période d'inactivité déterminée.

22

Le menu "*Sounds*" vous permet d'activer ou de désactiver les sons de votre Flex.

23

En cliquant sur la flèche de droite, vous pouvez accéder aux autres paramètres. "*Change PIN*" vous permet de changer votre code PIN.

24

Les menus "*Bluetooth*" et "*NFC*" vous permettent de gérer ces communications.

25

Dans "*Battery*" vous pouvez notamment paramétrer un arrêt automatique de la Ledger.

26

La section "*Advanced*" vous donne accès à des paramètres de sécurité plus poussés. Il est conseillé de maintenir l'option "*PIN shuffle*" activée pour renforcer la sécurité. C'est également dans ce menu que vous pouvez configurer une passphrase BIP39.

27

La passphrase est un mot de passe optionnel qui, combiné à la phrase de récupération, offre une couche de sécurité supplémentaire pour votre portefeuille.

Pour le moment, votre portefeuille est généré à partir d’une phrase mnémonique constituée de 24 mots. Cette phrase de récupération est très importante, car elle permet de restaurer l'ensemble des clés de votre portefeuille en cas de perte. Cependant, elle constitue un point de défaillance unique (SPOF). Si elle est compromise, les bitcoins sont en danger. C'est ici qu'intervient la passphrase. C'est un mot de passe optionnel, que vous pouvez choisir arbitrairement, qui s'ajoute à la phrase mnémonique pour renforcer la sécurité du portefeuille. 

La passphrase ne doit pas être confondue avec le code PIN. Elle joue un rôle dans la dérivation de vos clés cryptographiques. Elle fonctionne en tandem avec la phrase mnémonique, en modifiant la graine à partir de laquelle sont générées les clés. Ainsi, même si une personne obtient votre phrase de 24 mots, sans la passphrase, elle ne peut pas accéder à vos fonds. L'utilisation d'une passphrase crée essentiellement un nouveau portefeuille avec des clés distinctes. Modifier (même légèrement) la passphrase générera un portefeuille différent.

La passphrase est un outil très puissant pour renforcer la sécurité de vos bitcoins. Toutefois, il est très important de comprendre son fonctionnement avant de l'implémenter, afin d'éviter de perdre l'accès à votre portefeuille. Je vous expliquerai comment utiliser la passphrase dans un autre tutoriel dédié.

28

Enfin, la dernière page de paramètres vous permet de réinitialiser votre Ledger. Ne procédez à cette réinitialisation que si vous êtes certain qu'il ne contient aucune clé sécurisant des bitcoins, car vous risqueriez de perdre définitivement l'accès à vos fonds.

29

## Comment installer l'application Bitcoin ?

Commencez par lancer le logiciel Ledger Live sur votre ordinateur, puis connectez et déverrouillez votre Ledger Flex.

30

Sur Ledger Live, allez dans le menu "*My Ledger*".

31

On vous demande d'autoriser l'accès à votre Flex.

32

Validez l'accès sur votre Ledger en cliquant sur le bouton "*Allow*".

33

Tout d'abord, si le firmware de votre Ledger Flex n'est pas à jour, Ledger Live vous proposera automatiquement de le mettre à jour. Le cas échéant, cliquez sur "*Update firmware*", puis sur "*Install update*" pour lancer l'installation.

34

Sur votre Ledger, cliquez sur le bouton "*Install*", puis patientez le temps de l'installation.

35

Le firmware de votre Ledger Flex est bien à jour.

36

Si vous le souhaitez, vous pouvez modifier le fond d'écran de verrouillage de votre Ledger Flex. Pour ce faire, cliquez sur "*Add >*".

37

Cliquez sur le bouton "*Upload from computer*" et choisissez votre fond d'écran parmi vos photos.

38

Vous pouvez recadrer votre image.

39

Choisissez un contraste parmi les différentes options, puis cliquez sur "*Confirm contrast*".

40

Sur votre Flex, cliquez sur le bouton "*Load picture*".

41

Si l'image vous convient, cliquez sur "*Keep*" pour la mettre en fond d'écran de verrouillage.

42

Enfin, nous allons ajouter l'application Bitcoin. Pour ce faire, sur Ledger Live, cliquez sur le bouton "*Install*" à côté de "*Bitcoin (BTC)*".

43

L'application va s'installer sur votre Flex.

44

À partir de maintenant, vous n'aurez plus besoin du logiciel Ledger Live pour la gestion courante de votre portefeuille. Vous pourrez y revenir occasionnellement pour mettre à jour le firmware lorsque de nouvelles versions seront disponibles. Pour le reste, nous allons utiliser Sparrow Wallet qui est un outil bien plus complet pour gérer efficacement un portefeuille Bitcoin.

## Comment configurer un nouveau portefeuille Bitcoin avec Sparrow ?

Ouvrez Sparrow Wallet et passez les pages d'introduction pour accéder à l'écran d'accueil. Vérifiez que vous êtes correctement connecté à un nœud en observant l'interrupteur situé en bas à droite de l'écran.

45

Cliquez sur le menu "*File*" puis "*New Wallet*".

46

Choisissez un nom pour ce portefeuille, puis cliquez sur "*Create Wallet*".

47

Dans le menu déroulant "*Script Type*", sélectionnez le type de script qui sera utilisé pour sécuriser vos bitcoins. Je vous recommande d'opter pour "*Taproot*", ou à défaut, "*Native SegWit*".

48

Cliquez sur le bouton "*Connected Hardware Wallet*".

49

Connectez votre Ledger Flex à l'ordinateur, déverrouillez-le avec votre code PIN, puis ouvrez l'application "*Bitcoin*". Dans ce tutoriel, j'utilise l'application "*Bitcoin Testnet*", mais la procédure reste identique pour le mainnet.

50

Sur Sparrow, cliquez sur le bouton "*Scan*".

51

Puis cliquez sur "*Import Keystore*".

52

Vous pouvez maintenant voir les détails de votre portefeuille, y compris la clé publique étendue de votre premier compte. Cliquez sur le bouton "*Apply*" pour finaliser la création du portefeuille.

53

Choisissez un mot de passe fort pour sécuriser l'accès à Sparrow Wallet. Ce mot de passe assurera la sécurité de l'accès aux données de votre portefeuille sur Sparrow, ce qui permet de protéger vos clés publiques, vos adresses, vos labels et l'historique de vos transactions contre tout accès non autorisé.

Je vous conseille de sauvegarder ce mot de passe dans un gestionnaire de mots de passe pour ne pas l'oublier.

54

Et voilà, votre portefeuille est bien créé !

55

## Comment recevoir des bitcoins avec la Ledger Flex ?

Cliquez sur l'onglet "*Receive*".

56

Connectez votre Ledger Flex à l'ordinateur, déverrouillez-le avec votre code PIN, puis ouvrez l'application "*Bitcoin*".

57

Avant d'utiliser l'adresse proposée par Sparrow Wallet, vérifiez-la sur l'écran de votre Ledger Flex. Cette pratique vous permet de confirmer que l'adresse affichée sur Sparrow n'est pas frauduleuse et que le Ledger détient bien la clé privée nécessaire pour dépenser ultérieurement les bitcoins sécurisés avec cette adresse.

Pour effectuer cette vérification, cliquez sur le bouton "*Display Address*".

58

Vérifiez que l'adresse affichée sur votre Ledger Flex correspond à celle indiquée sur Sparrow Wallet. Il est également recommandé de réaliser cette vérification juste avant de communiquer votre adresse à l'envoyeur, afin d'être sûr de sa validité.

59

Vous pouvez ajouter un "*Label*" pour décrire la source des bitcoins qui seront sécurisés avec cette adresse. C'est une bonne pratique qui vous permet de mieux gérer vos UTXOs.

60

Pour plus d'informations sur l'étiquetage, je vous conseille également de découvrir cet autre tutoriel :

https://planb.network/tutorials/privacy/utxo-labelling

Vous pouvez ensuite utiliser cette adresse pour recevoir des bitcoins.

61

## Comment envoyer des bitcoins avec la Ledger Flex ?

Maintenant que vous avez reçu vos premiers sats sur votre portefeuille sécurisé avec le Flex, vous pouvez également les dépenser ! Connectez votre Ledger à votre ordinateur, déverrouillez-le, lancez Sparrow Wallet, puis allez dans l'onglet "*Send*" pour construire une nouvelle transaction.

62

Si vous souhaitez faire du "*coin control*", c'est-à-dire choisir spécifiquement quels UTXOs consommer dans la transaction, rendez-vous dans l'onglet "*UTXOs*". Sélectionnez les UTXOs que vous souhaitez dépenser, puis cliquez sur "*Send Selected*". Vous serez redirigé vers le même écran de l'onglet "*Send*", mais avec vos UTXOs déjà sélectionnés pour la transaction.

63

Entrez l'adresse de destination. Vous pouvez également entrer plusieurs adresses en cliquant sur le bouton "*+ Add*".

64

Notez un "*Label*" pour vous souvenir de l'objet de cette dépense.

65

Choisissez le montant envoyé à cette adresse.

66

Ajustez le taux de frais de votre transaction en fonction du marché du moment.

67

Assurez-vous que tous les paramètres de votre transaction sont corrects, puis cliquez sur "*Create Transaction*".

68

Si tout vous convient, cliquez sur "*Finalize Transaction for Signing*".

69

Cliquez sur "*Sign*".

70

Cliquez sur "*Sign*" à côté de votre Ledger Flex.

71

Vérifiez les paramètres de la transaction sur l'écran de votre Flex, notamment l'adresse de réception du destinataire, le montant envoyé et le montant des frais.

72

Pour signer, maintenez votre doigt sur le bouton "*Hold to sign*".

73

Votre transaction est désormais signée. Cliquez sur "*Broadcast Transaction*" pour la diffuser sur le réseau Bitcoin.

74

Vous pouvez la retrouver dans l'onglet "*Transactions*" de Sparrow Wallet.

75

Félicitations, vous êtes maintenant au point sur l'utilisation de base de la Ledger Flex avec Sparrow Wallet ! Dans un prochain tutoriel, nous verrons comment utiliser la Ledger Flex avec Liana pour tirer parti de Miniscript.

Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci beaucoup !
