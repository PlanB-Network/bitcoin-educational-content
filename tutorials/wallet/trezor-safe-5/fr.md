---
name: Trezor Safe 5
description: Configurer et utiliser le hardware wallet Safe 5
---
![cover](assets/cover.webp)

Le Trezor Safe 5 est un hardware wallet de dernière génération conçu par SatoshiLabs et lancé en 2024. Il se positionne comme une version haut de gamme du Safe 3, avec un accent mis sur l'ergonomie et la durabilité. Il bénéficie des mêmes avancées en termes de sécurité que son prédécesseur le Safe 3 par rapport au Model One et Model T.

Proposé à 169 €, le Safe 5 se positionne dans la catégorie des hardware wallets haut de gamme, en concurrence avec des modèles tels que le Coldcard, Ledger Nano X et Flex, Jade Plus, Passport, ou encore Bitbox.

Le Safe 5 se distingue notamment par son écran tactile couleur de 1,54 pouce, protégé par du verre *Gorilla Glass 3*, résistant aux chocs et aux rayures. Il est également équipé d’un moteur haptique *Trezor Touch* qui émet de petites vibrations au toucher. Tout comme le Safe 3, il intègre un Secure Element et fonctionne via une connexion USB-C, avec en plus un port Micro SD.

La principale différence entre le Safe 3 et le Safe 5 réside dans la qualité de l'appareil en dehors des aspects de sécurité. Il améliore significativement l'expérience utilisateur grâce à une utilisation plus fluide et un écran plus confortable. En termes de sécurité, c'est équivalent.

01

Le Safe 5 embarque toutes les fonctionnalités essentielles attendues d'un bon hardware wallet, avec notamment une excellente intégration de la passphrase BIP39. Cependant, il ne supporte pas encore Miniscript.

Ce modèle est particulièrement adapté aux débutants et aux utilisateurs intermédiaires. En revanche, il peut ne pas répondre à toutes les attentes des utilisateurs avancés qui recherchent des fonctionnalités plus spécifiques, disponibles sur des appareils comme le Coldcard. Néanmoins, si ces options avancées ne vous sont pas nécessaires, le Trezor Safe 5 peut s'avérer être un excellent choix.

## Le modèle de sécurité du Trezor Safe 5

Tout comme le Safe 3, le Trezor Safe 5 est équipé d'un **Secure Element certifié EAL6+**, une avancée significative par rapport aux modèles antérieurs tels que le Model One et le Model T. Il s'agit de la puce OPTIGA Trust M V3, qui ne stocke pas directement la seed mais joue un rôle de composant cryptographique pour en sécuriser l'accès. Le Secure Element retient un secret qui n'est accessible qu'après la saisie correcte du PIN par l'utilisateur. Ce secret est ensuite utilisé pour déchiffrer la seed, qui est conservée chiffrée dans la mémoire principale de l'appareil.

Ce système de sécurité hybride offre une meilleure protection physique, notamment contre les attaques par extraction ou analyse invasive, problèmes auxquels le Model One pouvait être sujet, notamment dans la gestion du code PIN. Ces vulnérabilités sont désormais contournées grâce à l'utilisation du Secure Element. Ce modèle maintient également une architecture logicielle open-source : le code qui gère la génération et l'utilisation des clés privées reste entièrement accessible et vérifiable. La puce OPTIGA gère uniquement le code PIN, un élément externe à la gestion des clés du portefeuille Bitcoin. Elle se limite à libérer un secret permettant de déchiffrer la seed. Aussi, la puce OPTIGA Trust M V3 bénéficie d'une licence relativement libre, qui autorise SatoshiLabs à publier librement les vulnérabilités potentielles (NDA-Free).

Ce modèle de sécurité représente, à mon avis, l'un des meilleurs compromis disponibles sur le marché actuellement. Il combine les avantages d'un Secure Element avec une gestion logicielle open-source. Auparavant, les utilisateurs devaient choisir entre une sécurité physique renforcée avec une puce et la transparence avec l'open-source ; avec les Trezor Safe, il est possible de bénéficier des deux.

Dans ce tutoriel, vous allez découvrir comment configurer et utiliser de manière sécurisée votre Trezor Safe 5.

## Unboxing du Trezor Safe 5

Lorsque vous recevez votre Safe 5, assurez-vous que la boîte et le sceau sont intacts pour confirmer que le paquet n'a pas été ouvert. Une vérification logicielle de l'authenticité et de l'intégrité du dispositif sera également réalisée lors de sa configuration plus tard.

Le contenu de la boîte inclut :
- Le Trezor Safe 5 ;
- Une pochette contenant des papiers cartonnés pour noter votre phrase mnémonique, des autocollants, et une notice ;
- Un câble USB-C vers USB-C.

À l'ouverture, votre Trezor Safe 5 devrait être protégé par un plastique de protection et le port USB-C doit être sécurisé par un sceau holographique. Assurez-vous de sa présence.

02

La navigation sur l'appareil est assez intuitive :
- Touchez la moitié inférieure de l'écran pour avancer ;
- Glissez vers le bas pour revenir en arrière ;
- Maintenez une pression sur l'écran pour confirmer une opération.

## Prérequis

Pour ce tutoriel, je vais vous montrer comment utiliser le Trezor Safe 5 avec [le logiciel de gestion de portefeuille Sparrow Wallet](https://sparrowwallet.com/download/). Si vous n'avez pas encore installé ce logiciel, je vous invite à le faire dès maintenant. Si vous avez besoin d'aide, nous disposons également d'un tutoriel détaillé sur la configuration de Sparrow Wallet :

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Vous aurez également besoin du logiciel Trezor Suite pour configurer le Safe 5, vérifier son authenticité et installer le firmware. Nous utiliserons ce logiciel uniquement pour cela ; puis par la suite, il sera nécessaire uniquement pour les mises à jour du firmware. Pour la gestion quotidienne du portefeuille, nous utiliserons exclusivement Sparrow Wallet, car il est optimisé pour Bitcoin et pratique à utiliser, même pour les débutants (Sparrow ne prend en charge que le bitcoin et non les altcoins).

[Téléchargez Trezor Suite depuis le site officiel.](https://trezor.io/trezor-suite)

03

Pour ces deux logiciels, je vous recommande fortement de vérifier à la fois leur authenticité (avec GnuPG) et leur intégrité (via le hash) avant de les installer sur votre machine. Si vous ne savez pas comment le faire, vous pouvez suivre cet autre tutoriel :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Démarrage du Trezor Safe 5

Branchez votre Safe 5 à votre ordinateur où Trezor Suite et Sparrow Wallet sont déjà installés.

04

Ouvrez Trezor Suite, puis cliquez sur "Set up my Trezor".

05

Sélectionnez "Bitcoin-only firmware", puis cliquez sur "Install Bitcoin-only".

06

Trezor Suite va alors procéder à l'installation du firmware sur votre Safe 5. Patientez pendant l'installation.

07

Cliquez sur "Continue".

08

Procédez ensuite au test d'authenticité pour vous assurer que votre hardware wallet n'est pas faux ou compromis.

09

Sur votre Safe 5, appuyez sur l'écran pour confirmer.

10

Si votre Trezor est authentique, un message de confirmation apparaîtra dans Trezor Suite.

11

Vous pouvez ensuite passer les fenêtres avec les instructions de base d'utilisation.

12

## Création d'un portefeuille Bitcoin

Sur Trezor Suite, cliquez sur le bouton "Create new wallet".

13

Pour créer un portefeuille standard BIP39, commencez par sélectionner "Legacy wallet backup types" dans le menu déroulant, puis choisissez entre une phrase mnémonique de 12 ou 24 mots (12 mots étant actuellement recommandés). Cela vous permettra de créer un portefeuille single-sig classique. Je vous conseille d'opter pour des paramètres conformes au BIP39 ici, afin de faciliter la récupération et d'éviter d'être restreint à un environnement spécifique. Pour finaliser, cliquez sur "Create wallet".

14

Acceptez les conditions d'utilisation sur le hardware wallet.

15

Maintenez une pression sur l'écran pour créer un nouveau portefeuille.

16

Dans Trezor Suite, cliquez sur "Continue to backup".

17

Le logiciel vous fournit des instructions sur la manière de gérer votre phrase mnémonique.

Cette phrase mnémonique donne un accès complet et non restreint à tous vos bitcoins. N'importe qui en possession de cette phrase peut subtiliser vos fonds, même sans accès physique à votre Trezor Safe 5.

La phrase de 12 mots permet de restaurer l'accès à vos bitcoins en cas de perte, vol ou casse de votre hardware wallet. Il est donc très important de la sauvegarder soigneusement et de la stocker dans un endroit sécurisé.

Vous pouvez l'inscrire sur le papier cartonné fourni dans la boite, ou bien pour plus de sécurité, je vous recommande de la graver sur un support en acier inoxydable afin de la protéger contre les risques d'incendies, d'inondations ou d'écroulements.

Validez les instructions, puis cliquez sur le bouton "Create wallet backup".

18

Le Safe 5 va créer votre phrase mnémonique en utilisant son générateur de nombres aléatoires. Assurez-vous de ne pas être observé durant cette opération. Notez les mots fournis sur l'écran sur le support physique de votre choix. Selon votre stratégie de sécurisation, vous pouvez envisager de réaliser plusieurs copies physiques complètes de la phrase (mais surtout, ne la divisez pas). Il est important de conserver les mots numérotés et dans l'ordre séquentiel.

***Évidemment, vous ne devez jamais partager ces mots sur internet, contrairement à ce que je fais dans ce tutoriel. Ce portefeuille en exemple sera utilisé uniquement sur le Testnet et sera supprimé à l'issue du tutoriel.***

Pour plus d'informations sur la manière adéquate de sauvegarder et de gérer votre phrase mnémonique, je vous recommande vivement de suivre cet autre tutoriel, particulièrement si vous êtes débutant :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

19

Pour passer aux mots suivants, cliquez sur le bas de l'écran. Vous pouvez revenir en arrière en glissant vers le bas. Une fois tous les mots notés, restez appuyé sur l'écran pour passer à l'étape suivante.

20

Sélectionnez les mots de votre phrase mnémonique en fonction de leur ordre pour confirmer que vous les avez correctement notés.

21

Une fois cette procédure de vérification terminée, cliquez sur l'écran pour continuer.

22

## Mise en place du code PIN

Vient ensuite l'étape du code PIN. Le code PIN permet de déverrouiller votre Trezor. C'est donc une protection contre les accès physiques non autorisés. Ce code PIN n'intervient pas dans la dérivation des clés cryptographiques de votre portefeuille. Ainsi, même sans accès à ce code PIN, la possession de votre phrase mnémonique de 12 mots vous permettra de retrouver l'accès à vos bitcoins.

Sur Trezor Suite, cliquez sur "Continue to PIN", puis sur le bouton "Set PIN".

23

Confirmez sur le Safe 5.

24

Il est recommandé de choisir un code PIN le plus aléatoire possible. Assurez-vous également de sauvegarder ce code dans un lieu distinct de celui où est stocké votre Trezor (par exemple, dans un gestionnaire de mot de passe). Vous avez la possibilité de définir un code PIN composé de 8 à 50 chiffres. Je vous recommande de choisir un code PIN aussi long que possible pour renforcer la sécurité.

Utilisez le clavier tactile pour renseigner votre PIN.

25

Une fois terminé, cliquez sur la coche verte en bas à droite, puis confirmez votre PIN une seconde fois.

26

Votre code PIN a bien été enregistré.

27

Sur Trezor Suite, cliquez sur le bouton "Complete setup".

28

La configuration de votre Safe 5 est désormais terminée. Si vous le souhaitez, vous pouvez modifier le nom et la page d'accueil de votre hardware wallet.

29

Nous n'aurons plus besoin du logiciel Trezor Suite, sauf pour effectuer des mises à jour régulières du firmware de votre hardware wallet, ou bien si vous souhaitez faire un test de récupération. Nous allons maintenant utiliser Sparrow pour gérer le portefeuille, car ce logiciel est parfaitement adapté pour une utilisation Bitcoin-only.

## Configurer le portefeuille sur Sparrow Wallet

Commencez par télécharger et installer Sparrow Wallet [depuis le site officiel](https://sparrowwallet.com/) sur votre ordinateur, si ce n'est pas déjà fait.

Une fois Sparrow Wallet ouvert, assurez-vous que le logiciel est bien connecté à un nœud Bitcoin, ce qui est indiqué par la coche en bas à droite de l'interface. Si vous rencontrez des difficultés pour connecter Sparrow, je vous recommande de consulter le début de ce tutoriel :

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Cliquez sur l'onglet "File", puis sur "New Wallet".

30

Nommez votre portefeuille, puis cliquez sur "Create Wallet".

31

Dans le menu déroulant "Script Type", sélectionnez le type de script qui sera utilisé pour sécuriser vos bitcoins. Je vous recommande d'opter pour "Taproot", ou à défaut, "Native SegWit".

32

Cliquez sur le bouton "Connected Hardware Wallet". Votre Safe 5 doit évidemment être connecté à l'ordinateur et déverrouillé.

Lorsque vous connectez votre Safe 5 à un ordinateur avec Sparrow Wallet ouvert, on vous proposera de saisir une passphrase BIP39 sur l'écran du hardware wallet. Cette option avancée sera abordée dans un futur tutoriel. Pour l'instant, vous pouvez simplement cliquez sur la coche verte en haut à droite pour confirmer que vous souhaitez utiliser une passphrase vide (c'est-à-dire sans passphrase). Pour éviter que votre Trezor ne vous demande de saisir une passphrase à chaque démarrage, allez dans Trezor Suite, accédez aux paramètres, et modifiez l'option dans "Device" > "Wallet default" pour la régler sur "Standard" au lieu de "Passphrase".

33

Cliquez sur le bouton "Scan". Votre Safe 5 devrait apparaitre. Cliquez sur "Import Keystore".

34

Vous pouvez maintenant voir les détails de votre portefeuille, y compris la clé publique étendue de votre premier compte. Cliquez sur le bouton "Apply" pour finaliser la création du portefeuille.

35

Choisissez un mot de passe fort pour sécuriser l'accès à Sparrow Wallet. Ce mot de passe assurera la sécurité de l'accès aux données de votre portefeuille sur Sparrow, ce qui permet de protéger vos clés publiques, vos adresses, vos labels et l'historique de vos transactions contre tout accès non autorisé.

Je vous conseille de sauvegarder ce mot de passe dans un gestionnaire de mots de passe pour ne pas l'oublier.

36

Et voilà, votre portefeuille est bien importé sur Sparrow Wallet !

37

Avant de recevoir vos premiers bitcoins sur votre portefeuille, **je vous conseille vivement de réaliser un test de récupération à vide**. Notez une information de référence, telle que votre xpub, puis réinitialisez votre Trezor Safe 5 tant que le portefeuille est encore vide. Ensuite, essayez de restaurer votre portefeuille sur le Trezor en utilisant vos sauvegardes papier. Vérifiez que la xpub générée après la restauration correspond à celle que vous aviez notée initialement. Si c'est le cas, vous pouvez être assuré que vos sauvegardes papier sont fiables.

Pour en savoir plus sur comment effectuer un test de récupération, je vous conseille de consulter cet autre tutoriel :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Comment recevoir des bitcoins avec le Trezor Safe 5 ?

Sur Sparrow, cliquez sur l'onglet "Receive".

38

Avant d'utiliser l'adresse proposée par Sparrow Wallet, vérifiez-la sur l'écran de votre Trezor. Cette pratique vous permet de confirmer que l'adresse affichée sur Sparrow n'est pas frauduleuse et que le hardware wallet détient bien la clé privée nécessaire pour dépenser ultérieurement les bitcoins sécurisés avec cette adresse. Cela vous permet d'éviter plusieurs types d'attaques.

Pour effectuer cette vérification, cliquez sur le bouton "Display Address".

39

Vérifiez que l'adresse affichée sur votre Trezor correspond à celle indiquée sur Sparrow Wallet. Il est également recommandé de réaliser cette vérification juste avant de communiquer votre adresse à l'envoyeur, afin d'être sûr de sa validité. Vous pouvez appuyer sur l'écran pour confirmer.

40

Vous pouvez ensuite ajouter un "Label" pour décrire la source des bitcoins qui seront sécurisés avec cette adresse. C'est une bonne pratique qui vous permet de mieux gérer vos UTXOs.

41

Vous pouvez ensuite utiliser cette adresse pour recevoir des bitcoins.

42

## Comment envoyer des bitcoins avec le Trezor Safe 5 ?

Maintenant que vous avez reçu vos premiers sats sur votre portefeuille sécurisé avec le Safe 5, vous pouvez également les dépenser ! Connectez votre Trezor à votre ordinateur, déverrouillez-le à l'aide du code PIN, lancez Sparrow Wallet, puis allez dans l'onglet "Send" pour construire une nouvelle transaction.

43

Si vous souhaitez faire du *Coin Control*, c'est-à-dire choisir spécifiquement quels UTXOs consommer dans la transaction, rendez-vous dans l'onglet "UTXOs". Sélectionnez les UTXOs que vous souhaitez dépenser, puis cliquez sur "Send Selected". Vous serez redirigé vers le même écran de l'onglet "Send", mais avec vos UTXOs déjà sélectionnés pour la transaction.

44

Entrez l'adresse de destination. Vous pouvez également entrer plusieurs adresses en cliquant sur le bouton "+ Add".

45

Notez un "Label" pour vous souvenir de l'objet de cette dépense.

46

Choisissez le montant envoyé à cette adresse.

47

Ajustez le taux de frais de votre transaction en fonction du marché du moment. Vous pouvez par exemple utiliser [mempool.space](https://mempool.space/) pour choisir un taux de frais adapté.

Assurez-vous que tous les paramètres de votre transaction sont corrects, puis cliquez sur "Create Transaction".

48

Si tout vous convient, cliquez sur "Finalize Transaction for Signing".

49

Cliquez sur "Sign".

50

Cliquez sur "Sign" à côté de votre Trezor Safe 5.

51

Vérifiez les paramètres de la transaction sur l'écran de votre hardware wallet, notamment l'adresse de réception du destinataire, le montant envoyé et le montant des frais. Une fois la transaction vérifiée sur le Trezor, maintenez une pression sur l'écran pour la signer.

52

Votre transaction est désormais signée. Vérifiez une dernière fois que tout vous convient, puis cliquez sur "Broadcast Transaction" pour la diffuser sur le réseau Bitcoin.

53

Vous pouvez la retrouver dans l'onglet "Transactions" de Sparrow Wallet.

54

Félicitations, vous êtes maintenant au point sur l'utilisation de base du Trezor Safe 5 avec Sparrow Wallet ! Dans un prochain tutoriel, nous verrons comment utiliser un hardware wallet Trezor avec une passphrase BIP39 pour renforcer sa sécurité.

Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci beaucoup !








1. top
2. enter
3. before
4. potato
5. model
6. push
7. bleak
8. fun
9. oxygen
10. add
11. minor
12. call

