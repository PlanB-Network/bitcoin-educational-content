---
builder: Blockstream

difficulty: Beginners

tag:
  - wallet
  - self-custodial
---
![cover](assets\cover.jpg)
# Tutoriel portefeuille – Green Wallet

Portefeuille mobile chaud – Débutant – Gratuit – Pour sécuriser de 0 à 1 000 €

Pour sécuriser des sommes en dessous de 1 000€, un portefeuille chaud (connecté à Internet) gratuit est parfait pour commencer.
Sa mise en place est facile et son interface est conçue pour les débutants.

Si tu souhaites faire un tour sur leur site, c’est juste ici (https://blockstream.com/green/)!

## Tuto Vidéo

![vidéo tuto green wallet](https://www.youtube.com/watch?v=lONbCS31am4)

## Tuto écrie

    Ce guide a été produit et appartient a Bitstack. Bitstack est une néo banque bitcoin basé sur paris qui permet de DCA sur bitcoin. Guide écrit par Loic Morel le 15/02/2023. Ceci leur appartient. https://www.bitstack-app.com/blog/installer-portefeuille-bitcoin-green-wallet


![image](assets\0.png)

Comment installer son premier portefeuille Bitcoin ? Tutoriel Green Wallet

Si vous souhaitez bénéficier des nombreux avantages du système Bitcoin, notamment l’incensurabilité et l’insaisissabilité de vos fonds, vous devez obligatoirement conserver vous-même vos clés donnant accès à vos bitcoins. 

Dans ce tutoriel, je vous explique comment mettre en place votre premier portefeuille avec Green Wallet. Ce logiciel est particulièrement adapté pour les utilisateurs débutants. Il est très simple à prendre en main, et ce, même si vous ne disposez pas de connaissances avancées sur Bitcoin.

Green Wallet est disponible sur tous types d’appareils. Dans ce tutoriel, nous allons voir comment l’utiliser sur mobile, mais vous pouvez également le télécharger sur un ordinateur.

La première étape consiste évidemment à télécharger le logiciel ou l’application Green Wallet. Si vous êtes sur mobile, vous pouvez simplement la télécharger depuis votre store. Il convient de vérifier que vous êtes bien sur la page de téléchargement de l’application officielle. Voici les pages en fonction de votre système : 

    Google Play Store

    Apple App Store

Si vous téléchargez le logiciel sur un ordinateur, je vous conseille fortement de vérifier l’authenticité et l’intégrité du binaire avant de l’installer sur votre machine. Je vous expliquerai comment réaliser cette opération dans un prochain tutoriel.
Choix des paramètres de l’application

Au lancement de l’application, vous arrivez sur l’écran d’accueil. Pour le moment, vous ne disposez d’aucun portefeuille. Par la suite, si vous avez créé plusieurs wallets, vous pourrez les retrouver ici.

La première action à mener, avant de créer votre portefeuille, est d’ouvrir les paramètres de l’application pour choisir ceux qui vous conviennent le mieux.

    « Enhanced Privacy » vous permet de désactiver la possibilité de faire des captures d’écran sur l’application. Cette option va également cacher les aperçus et sécuriser automatiquement l’application lorsque vous verrouillez votre téléphone. Elle n’est disponible que sur Android ;

    Vous pouvez ensuite choisir de router votre trafic via Tor afin que toutes vos connexions soient chiffrées. Cela ralentit légèrement le fonctionnement de votre application, mais je vous conseille de l’activer afin de préserver votre vie privée ;

    L’option « Testnet » vous permet de créer des portefeuilles sur le Testnet. C’est un réseau qui agit exactement comme le système Bitcoin, à la différence près que les bitcoins qui y sont échangés n’ont strictement aucune valeur. Ce réseau Testnet séparé est plébiscité par des utilisateurs ou des développeurs qui désirent tester des applications, sans pour autant prendre de risque financier. Si vous souhaitez utiliser Green Wallet sur le vrai système Bitcoin, vous pouvez conserver cette option décochée ;

    L’option « Aider Green » vous permet de transmettre des informations confidentielles à Blockstream afin qu’ils améliorent leur application ;

    L’option « Serveur Electrum personnel » vous permet de connecter votre propre nœud Bitcoin à distance afin de disposer des informations du réseau et de diffuser vos transactions ;

    L’option « SPV verification » vous permet de télécharger et de vérifier vous-même certaines informations de la Blockchain. Cela permet de réduire le besoin de confiance envers le nœud de Blockstream. Attention, cette option ne vous donne pas toutes les garanties d’un vrai nœud Bitcoin, mais à défaut d’en avoir un, cela peut être une bonne option à activer.


Une fois vos paramètres choisis, vous pouvez cliquer sur le bouton « Sauvegarder », puis redémarrez votre application.
Création d’un portefeuille Bitcoin

La prochaine étape consiste à créer votre portefeuille Bitcoin. Pour ce faire, cliquez sur : 

    Ajouter un portefeuille ;

    Nouveau portefeuille ;

    Bitcoin.

L’option « Restaurez un portefeuille » vous permet de récupérer l’accès à un portefeuille déjà existant grâce à sa phrase mnémonique. L’option « Watch-Only Wallet » vous permet d’importer une clé publique étendue (xpub) afin de voir les mouvements d’un portefeuille, sans pour autant pouvoir dépenser ses fonds. 

    "Le portefeuille Watch-Only est particulièrement utile si vous disposez d’un hardware wallet. Vous pouvez importer la xpub sur votre téléphone afin de créer des adresses de réception et de suivre le solde du portefeuille hébergé sur le hardware wallet. "

Les options de réseaux vous permettent de connecter votre portefeuille sur des systèmes différents. Le réseau « Liquid » est une sidechain de Bitcoin. Le réseau « Testnet » est une copie du réseau Bitcoin, mais avec des bitcoins qui n’ont aucune valeur. Enfin, le réseau « Testnet Liquid » est l’équivalent du Testnet pour la sidechain Liquid. Dans ce tutoriel, nous souhaitons simplement faire un portefeuille Bitcoin, donc nous sélectionnons le réseau « Bitcoin ».

Ensuite, on vous demande quel type de portefeuille vous désirez faire. Le plus simple est de réaliser un portefeuille « Single Sig ». Dans ce cas, chaque UTXO (morceau de bitcoin) nous appartenant ne sera bloqué que par une seule paire de clés. 

Sélectionnez « Signature unique ».

Vous pouvez ensuite choisir de disposer d’une phrase mnémonique de 12 mots ou de 24 mots. C’est cette phrase qui vous permettra de récupérer l’accès à votre portefeuille, à partir de n’importe quel logiciel compatible, en cas de perte, de vol ou de casse de votre téléphone. 

Une phrase de 24 mots est plus sécurisée qu’une phrase de 12 mots face aux attaques par brute force. Néanmoins, à date, une phrase de 12 mots reste suffisamment sécurisée. Concrètement, si vous choisissez une phrase de 12 mots, vous serez juste au-dessus de la limite minimale conseillée par le NIST. Cela veut dire que votre phrase est sécurisée aujourd’hui, mais qu’elle ne le sera peut-être plus dans les années à venir à cause de l’évolution de l’informatique (sauf si vous utilisez en plus une passphrase BIP39). Par défaut, je vous conseille plutôt de choisir une phrase de 24 mots, mais c’est à vous de faire votre propre choix.


Le logiciel va ensuite vous fournir votre phrase de récupération. Vous devez la sauvegarder convenablement en la notant sur un support physique adapté. Il est fortement déconseillé de conserver cette phrase sur un quelconque support numérique, même chiffré. Il faut la noter sur du papier ou sur du métal en fonction de la valeur stockée. 

Cette phrase est d’une importance capitale, puisqu’elle permet de donner accès aux clés de votre portefeuille sans aucune restriction. En cas de perte de celle-ci, vous ne pourrez plus accéder à vos bitcoins si votre téléphone ne fonctionne plus. En cas de vol de cette phrase mnémonique, un attaquant pourra irrévocablement vous voler tous vos fonds.

Les mots de cette phrase doivent absolument être notés ensemble. Ne divisez pas votre phrase ! Par ailleurs, il est également essentiel de noter chaque mot dans l’ordre défini, avec son numéro. Une phrase en désordre est inutile.

Pour en savoir plus sur les méthodes de sécurisation de la phrase de récupération, je vous conseille vivement de lire mon article dédié à ce sujet.

Green Wallet vous demande ensuite de confirmer certains mots de votre phrase afin de s’assurer que vous les avez bien notés. 

Vous pouvez ensuite choisir un nom pour votre portefeuille afin de le différencier des autres si par la suite vous en créez plusieurs. À cette étape, le nom a peu d’importance puisque nous allons supprimer ce portefeuille afin de vérifier la validité de la phrase mnémonique à l’étape suivante.

On vous demande également de mettre en place un PIN. Il permet de bloquer l’accès à votre portefeuille. Il convient de mettre en place un mot de passe complexe et aléatoire, notamment pour protéger votre portefeuille en cas de vol de votre téléphone.

Ce PIN n’a rien à voir avec le portefeuille Bitcoin en lui-même. En effet, uniquement avec la phrase de récupération, vous pourrez récupérer l’accès à tous vos bitcoins. Le PIN permet seulement de bloquer l’accès à votre portefeuille sur votre téléphone. La sauvegarde de la phrase est donc bien plus importante que la sauvegarde de ce PIN.

Vous pourrez par la suite ajouter une option de blocage par biométrie afin d’éviter de rentrer le PIN à chaque utilisation. De façon générale, la biométrie est bien moins sécurisée que le PIN en lui-même. Ainsi, par défaut, je vous déconseille de mettre en place cette option de déverrouillage.

Vous devez entrer le PIN choisi une seconde fois sur l’application Green afin de le confirmer.

Félicitations ! Vous avez terminé la création de votre portefeuille Bitcoin. 

Si vous souhaitez ajouter une passphrase BIP39 sur ce portefeuille Bitcoin, vous devez cliquer sur les trois points en haut à droite de l’écran lorsque vous entrez votre PIN pour déverrouiller le wallet. Attention, je vous déconseille fortement d’utiliser une passphrase si vous ne comprenez pas les mécanismes de dérivation en jeu. Vous pourriez perdre l’accès à vos bitcoins.


Avant d’envoyer des bitcoins vers votre nouveau portefeuille, il est essentiel de réaliser un test de récupération afin de vous assurer que votre sauvegarde de la phrase mnémonique est bien fonctionnelle. Concrètement, nous allons supprimer le portefeuille tant qu’il est encore vide, et tenter de le récupérer uniquement à l’aide de la phrase de récupération, comme si nous avions perdu l’accès à notre téléphone. 

En plus de vérifier la validité de la phrase, cette pratique vous permet également de vous entraîner à la récupération d’un portefeuille Bitcoin. Ainsi, si un jour vous vous retrouvez face à une situation d’urgence, vous saurez exactement quelles sont les étapes à réaliser pour récupérer l’accès à vos fonds.

Pour ce faire, avant de supprimer votre portefeuille, vous devez récupérer une information témoin permettant de le reconnaître par la suite. Vous allez donc copier les 8 derniers caractères de la première adresse qui vous est proposée. 

Pour accéder à cette information, cliquez sur le bouton « Recevoir ». Le portefeuille vous affiche une adresse. Notez sur un autre bout de papier ses 8 derniers caractères. C’est ce qui correspond à la somme de contrôle de l’adresse. 

Par exemple, sur mon portefeuille, les 8 caractères à noter seraient : JTbP4482.

Une fois que vous avez noté cette information, vous pouvez supprimer votre portefeuille. Depuis l’écran d’accueil du wallet, cliquez sur l’icône des paramètres, puis sur « Déconnexion ».

    "Je précise une nouvelle fois que cette opération doit se faire avec un portefeuille encore vide, avant d’y avoir envoyé des bitcoins. Sinon, vous risquez de les perdre."

Vous êtes alors envoyé sur l’écran de déverrouillage de votre wallet. Cliquez sur les trois petits points en haut à droite de l’écran, puis sur « Supprimer le portefeuille », et confirmez.

Vous êtes dorénavant sur l’écran d’accueil de l’application Green Wallet, et il n’y a plus aucun portefeuille disponible. Vous êtes donc actuellement dans la même situation que si vous aviez perdu ou cassé votre téléphone, et que vous essayiez de récupérer votre portefeuille à partir de la phrase mnémonique uniquement.

Il faut maintenant cliquer sur « Ajouter un portefeuille », puis sur « Restaurez un  portefeuille », et enfin sur « Bitcoin ».

Le logiciel nous demande ensuite si l’on souhaite récupérer à partir d’un QR code, ou à partir d’une phrase mnémonique. Dans notre cas, c’est une phrase.

Par la suite, il nous est demandé de renseigner la phrase de récupération. C’est celle que nous avions notée lors de la création du portefeuille. Si vous utilisez une phrase de 24 mots, pensez à cliquer sur la petite case « 24 ».

Une fois tous les mots entrés, si le logiciel vous indique qu’il y a une erreur, c’est que la somme de contrôle (checksum) de votre phrase n’est pas bonne. Dans ce cas, cela veut dire que la sauvegarde papier de votre phrase mnémonique est invalide. Vous devez donc recommencer ce tutoriel depuis le départ, et veiller à bien écrire la phrase lorsqu’elle vous est donnée.

Sinon, vous pouvez cliquer sur « Continuez ».

Le logiciel vous indiquera « Portefeuille non trouvé ». C’est absolument normal puisque, pour le moment, nous n’y avons pas encore envoyé de bitcoins. Ainsi, il ne peut détecter aucune transaction sur la blockchain liée à ce wallet.

Cliquez en bas de l’écran sur « Manual Restore », puis sur « Signature unique ». 

Enfin, on vous redemande de nommer ce portefeuille et de lui attribuer un PIN. Vous pouvez lui donner le même nom et le même PIN que le portefeuille initial. 

Pour rappel, ce PIN n’a pour fonctionnalité que de permettre le déverrouillage du portefeuille sur cette application et sur ce téléphone spécifiquement. Contrairement à la phrase de récupération, il ne permet pas de régénérer votre portefeuille sur un autre logiciel ou matériel.

Une fois le PIN validé, vous arrivez de nouveau sur la page d’accueil de votre portefeuille. Il est temps de vérifier si votre phrase de récupération est bien fonctionnelle en allant observer la première adresse dérivée. Pour ce faire, une nouvelle fois, cliquez sur « Recevoir » pour accéder à la première adresse. 

Si les 8 derniers caractères sont exactement les mêmes que ceux que vous avez notés comme témoins sur votre papier avant de supprimer le portefeuille, alors votre phrase est bien valide. Dans mon cas, on peut voir que la checksum de ma première adresse est bien égale à la valeur notée précédemment : JTbP4482.

Je sais que cette pratique de vérification est fastidieuse, mais elle est absolument essentielle afin d’assurer la bonne sécurisation de votre portefeuille Bitcoin. Je vous conseille fortement de prendre cette habitude lorsque vous créez un wallet, que ce soit sur un logiciel ou sur un matériel.

Avec Green Wallet, j'ai utilisé la première adresse pour réaliser ce processus. Cependant, vous pouvez également prendre comme information témoin une clé publique étendue (xpub/zpub), ou encore l’empreinte de la clé privée maîtresse (master fingerprint).
Utilisation du portefeuille Bitcoin Green Wallet

Une fois votre portefeuille mis en place et vérifié, vous allez pouvoir commencer à l’utiliser. 

Pour bien débuter, je vous conseille de personnaliser les paramètres de votre wallet. Pour ce faire, cliquez sur l’icône des paramètres en haut à droite de l’écran. 

    L’option « Unité affichée » vous permet de personnaliser l’unité utilisée sur votre portefeuille. Si vous disposez de peu de fonds, cela peut être pertinent d’afficher votre portefeuille en sats plutôt qu’en bitcoins. Le satoshi (sat) correspond à un cent millionième d’un bitcoin : 1 BTC = 100 000 000 sats. 

    L’option « Montant des frais par défaut » vous permet de personnaliser les frais alloués à vos transactions par défaut. Au plus les frais par vbyte (octet virtuel) sont élevés, au plus vos transactions seront confirmées rapidement. Vous pourrez par la suite modifier ce taux de frais à chaque transaction émise en fonction de la congestion du réseau Bitcoin.

    L’option « Connexion avec la biométrie » vous permet de déverrouiller votre portefeuille avec votre empreinte digitale plutôt qu’avec le PIN. Généralement, je vous déconseille d’activer cette option. La biométrie est bien moins sécurisée que le code PIN.

Par défaut, Green Wallet vous attribue un compte BIP49 « Nested SegWit » avec des adresses P2SH (Pay to Script Hash). Quelques années auparavant, l’utilisation de ce type de compte était pertinente puisque tout le monde ne prenait pas encore en charge les adresses natives SegWit. Aujourd’hui, la grande majorité des services en rapport avec Bitcoin prennent en charge SegWit, il n’y a donc plus aucune raison d’utiliser un compte « Nested SegWit ». 

Nous allons alors créer un nouveau compte BIP84 « Native SegWit » afin de bénéficier de tous ses avantages, et également pour avoir des adresses P2WPKH (Pay to Witness Public Key Hash). Pour ce faire, cliquez sur votre compte « Legacy SegWit Account », puis sur « Ajouter un nouveau compte », et enfin sur « Compte SegWit ». Vous pouvez ensuite donner un nom à ce compte si vous le souhaitez.

Par la suite, si vous avez besoin de créer de nouveaux comptes sur ce portefeuille, je vous conseille de choisir par défaut des comptes SegWit V0 BIP84, ou SegWit V1 BIP86 (lorsqu’ils seront disponibles).

Sur la page d’accueil de votre portefeuille, vous pouvez voir vos différents comptes, et notamment votre nouveau compte SegWit. 

Ensuite, le fonctionnement de l’application Green Wallet est très simple. Pour recevoir des bitcoins sur votre portefeuille, cliquez sur le bouton « Recevoir ». Le wallet vous affiche une adresse de réception. Une adresse permet de recevoir des bitcoins sur votre portefeuille. Vous pouvez soit la copier en format texte afin de l’envoyer à votre payeur, soit flasher le QR code avec un autre portefeuille Bitcoin afin de payer l’adresse.

Ce type d’adresse n’indique pas au payeur le montant qu’il doit vous envoyer. Vous pouvez également créer une adresse qui demandera automatiquement un montant choisi au payeur. Pour ce faire, cliquez sur « Plus d’options » et entrez le montant voulu.

Puisque vous utilisez un compte SegWit V0 BIP84, votre adresse devrait débuter par le préfixe « bc1q ». Dans mon exemple, j’utilise un portefeuille Testnet, donc le préfixe est légèrement différent du vôtre.

Une adresse de réception ne doit pas être utilisée plusieurs fois. C’est une mauvaise pratique qui mène à des risques pour votre vie privée. Par défaut, le portefeuille Green vous générera une nouvelle adresse lorsque vous cliquerez sur « Recevoir » et que la précédente a déjà été utilisée. Vous pouvez aussi cliquer sur l’icône de la flèche qui tourne pour demander une nouvelle adresse vierge liée à votre portefeuille.

    "Astuce : Lorsque vous copiez collez une adresse de réception, vous n’avez pas besoin de vérifier que chaque caractère de l’adresse est bien le bon. En effet, les adresses comprennent une checksum permettant de détecter une petite faute de frappe. Il est seulement nécessaire de vérifier les premiers et les derniers caractères de l’adresse pour s’assurer de sa validité."

Sur les captures d’écrans ci-dessous, vous pouvez voir que j’ai envoyé 0,02 btc vers mon adresse. La transaction apparait sur Green, d’abord en « non confirmée » en attendant qu’elle soit incluse dans la blockchain par un mineur. Une fois que la transaction a reçu plusieurs confirmations, vous avez bien reçu vos bitcoins sur votre propre portefeuille.

Si vous souhaitez envoyer des bitcoins, vous devez récupérer l’adresse de réception vers laquelle vous désirez envoyer les fonds et cliquer sur le bouton « Envoyer ». Sur la page suivante, vous devez entrer l’adresse de destination. Vous pouvez soit l’entrer manuellement, soit flasher un QR code en cliquant sur l’icône correspondante. Choisissez ensuite le montant de la transaction. Vous pouvez soit noter un montant en bitcoins, soit un montant en dollars américains en cliquant sur la double flèche blanche.

Au centre de l’écran, vous pouvez choisir le taux de frais alloués à cette transaction. Il est possible, au choix, de suivre les recommandations de l’application, ou bien de personnaliser vos frais. Au plus vous mettez des frais élevés par rapport aux autres transactions en attente de confirmation, au plus votre transaction sera incluse rapidement, et inversement. 

Cliquez ensuite sur « Suivant ». Vous arrivez alors sur un écran vous donnant les détails de votre transaction. Vous pouvez vérifier que l’adresse entrée est bien la bonne, que le montant correspond à ce que vous souhaitez envoyer et que les frais sont corrects.

Pour signer la transaction et la diffuser au réseau Bitcoin, faites glisser le bouton vert en bas de l’écran vers la droite.

Votre transaction apparaît dorénavant sur le tableau de bord de votre portefeuille Bitcoin.
Conclusion

Félicitations ! Vous disposez désormais de votre propre portefeuille Bitcoin en self-custody. Vos bitcoins vous appartiennent réellement.

Ce portefeuille Green Wallet de Blockstream est une excellente solution pour les débutants qui disposent de peu de bitcoins. Comme vous avez pu le constater, sa prise en main est très simple. Toutefois, cela reste un portefeuille chaud. Si vous disposez de sommes conséquentes en bitcoins, je vous conseille de vous tourner vers un hardware wallet.

Une fois que vous avez appris à bien maîtriser Green Wallet et que vous comprenez les mécanismes en jeu, vous pourrez vous tourner vers des solutions plus complètes comme Samourai Wallet ou Sparrow Wallet.

Pour conclure, je vous rappelle une nouvelle fois que vous devez absolument soigner la sauvegarde de votre phrase de récupération. Elle donne un accès direct et sans restriction à vos bitcoins. Si vous la perdez, vous ne serez plus en capacité de récupérer vos bitcoins si votre téléphone est perdu, cassé ou volé. N’importe qui ayant accès à cette phrase pourra vous voler vos bitcoins et il n’y aura aucun moyen de les récupérer.