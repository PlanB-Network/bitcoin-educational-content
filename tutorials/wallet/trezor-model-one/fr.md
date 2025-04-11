---
name: Trezor Model One
description: Configurer et utiliser le hardware wallet Model One
---
![cover](assets/cover.webp)

Le Trezor Model One est le tout premier hardware wallet jamais commercialisé, lancé en 2014 par SatoshiLabs. Après plus de dix ans d’existence, il demeure un choix intéressant, notamment pour les utilisateurs à la recherche d'un hardware wallet accessible à la fois techniquement et en termes de budget. En effet, il est proposé à 49 € sur le site officiel de Trezor. C'est un des seuls hardware wallets dans cette gamme de prix. Il se situe à mi-chemin entre les appareils d'entrée de gamme à environ 20 €, comme le Tapsigner, souvent dépourvus d'écran, et ceux du milieu de gamme, autour de 80 €, tels que le Ledger Nano S Plus ou le Trezor Safe 3.

Le Model One est équipé d’un écran OLED monochrome de 0,96 pouce et de deux boutons physiques. Il fonctionne sans batterie, uniquement via une connexion micro-USB pour l’alimentation et les échanges de données.

01

Le principal inconvénient du Model One est son absence de Secure Element, qui le rend vulnérable à diverses attaques physiques, dont certaines sont relativement simples à exécuter. Ces attaques peuvent inclure l'analyse de canaux auxiliaires pour déterminer le code PIN de l'appareil ou des techniques plus avancées permettant d'extraire la seed chiffrée afin de la brute-forcer par la suite. Notez que ces attaques nécessitent un accès physique à l'appareil. Cependant, cette vulnérabilité peut être considérablement réduite par l'utilisation d'une passphrase BIP39 solide. Si vous optez pour ce hardware wallet, je vous conseille donc fortement de configurer une passphrase.

Le Model One présente deux avantages importants :
- Il est basé sur une architecture entièrement open-source. Contrairement aux modèles plus récents avec Secure Element, tous les composants matériels et logiciels du Model One sont auditables ;
- Il est équipé d'un écran. Dans cette gamme de prix, c'est à ma connaissance le seul hardware wallet du marché doté d'un écran. C'est un élément très important, car il permet de vérifier les informations signées et les adresses de réception, ce qui prévient de nombreuses attaques numériques.

Le Trezor Model One peut donc représenter un choix judicieux pour les utilisateurs débutants et intermédiaires disposant d'un budget limité. Toutefois, il est important de rester conscient de ses limites en matière de protection physique, dues à l'absence de Secure Element. Si votre budget est limité, c'est une bonne option, mais si vous pouvez vous permettre d'opter pour un modèle supérieur, tel que le Trezor Safe 3 à 79 €, c'est préférable, car il inclut un Secure Element.

## Unboxing du Trezor Model One

Lorsque vous recevez votre Model One, assurez-vous que la boîte et le sceau sont intacts pour confirmer que le paquet n'a pas été ouvert. Une vérification logicielle de l'authenticité et de l'intégrité du dispositif sera également réalisée lors de sa configuration plus tard.

Le contenu de la boîte inclut :
- Le Trezor Model One ;
- Des papiers cartonnés pour noter votre phrase mnémonique, des autocollants et une notice ;
- Un câble USB-A vers micro-USB.

02

La navigation sur l'appareil est très simple :
- Le bouton droit permet de confirmer et de passer aux étapes suivantes ;
- Le bouton gauche permet de revenir en arrière.

## Prérequis

Pour ce tutoriel, je vais vous montrer comment utiliser le Trezor Model One avec [le logiciel de gestion de portefeuille Sparrow Wallet](https://sparrowwallet.com/download/). Si vous n'avez pas encore installé ce logiciel, je vous invite à le faire dès maintenant. Si vous avez besoin d'aide, nous disposons également d'un tutoriel détaillé sur la configuration de Sparrow Wallet :

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Vous aurez également besoin du logiciel Trezor Suite pour configurer le Model One, vérifier son authenticité et installer le firmware. Nous utiliserons ce logiciel uniquement pour cela ; puis par la suite, il sera nécessaire uniquement pour les mises à jour du firmware. Pour la gestion quotidienne du portefeuille, nous utiliserons exclusivement Sparrow Wallet, car il est optimisé pour Bitcoin et pratique à utiliser, même pour les débutants (Sparrow ne prend en charge que le bitcoin et non les altcoins).

[Téléchargez Trezor Suite depuis le site officiel.](https://trezor.io/trezor-suite)

03

Pour ces deux logiciels, je vous recommande fortement de vérifier à la fois leur authenticité (avec GnuPG) et leur intégrité (via le hash) avant de les installer sur votre machine. Si vous ne savez pas comment le faire, vous pouvez suivre cet autre tutoriel :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Démarrage du Trezor Model One

Branchez votre Model One à votre ordinateur où Trezor Suite et Sparrow Wallet sont déjà installés.

04

Ouvrez Trezor Suite, puis cliquez sur "Set up my Trezor".

05

Sélectionnez "Bitcoin-only firmware", puis cliquez sur "Install Bitcoin-only".

06

Trezor Suite va alors procéder à l'installation du firmware sur votre Model One. Patientez pendant l'installation.

07

Cliquez sur "Continue".

08

## Création d'un portefeuille Bitcoin

Sur Trezor Suite, cliquez sur le bouton "Create new wallet".

09

Acceptez les conditions d'utilisation sur le hardware wallet.

10

Dans Trezor Suite, cliquez sur "Continue to backup".

11

Le logiciel vous fournit des instructions sur la manière de gérer votre phrase mnémonique.

Cette phrase mnémonique donne un accès complet et non restreint à tous vos bitcoins. N'importe qui en possession de cette phrase peut subtiliser vos fonds, même sans accès physique à votre Trezor Model One.

La phrase de 24 mots permet de restaurer l'accès à vos bitcoins en cas de perte, vol ou casse de votre hardware wallet. Il est donc très important de la sauvegarder soigneusement et de la stocker dans un endroit sécurisé.

Vous pouvez l'inscrire sur le papier cartonné fourni dans la boite, ou bien pour plus de sécurité, je vous recommande de la graver sur un support en acier inoxydable afin de la protéger contre les risques d'incendies, d'inondations ou d'écroulements.

Validez les instructions, puis cliquez sur le bouton "Create wallet backup".

12

Le Model One va créer votre phrase mnémonique en utilisant son générateur de nombres aléatoires. Assurez-vous de ne pas être observé durant cette opération. Notez les mots fournis sur l'écran sur le support physique de votre choix. Selon votre stratégie de sécurisation, vous pouvez envisager de réaliser plusieurs copies physiques complètes de la phrase (mais surtout, ne la divisez pas). Il est important de conserver les mots numérotés et dans l'ordre séquentiel.

***Évidemment, vous ne devez jamais partager ces mots sur internet, contrairement à ce que je fais dans ce tutoriel. Ce portefeuille en exemple sera utilisé uniquement sur le Testnet et sera supprimé à l'issue du tutoriel.***

Pour plus d'informations sur la manière adéquate de sauvegarder et de gérer votre phrase mnémonique, je vous recommande vivement de suivre cet autre tutoriel, particulièrement si vous êtes débutant :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Pour passer aux mots suivants, cliquez sur le bouton droit. Une fois tous les mots notés, cliquez de nouveau sur le bouton droit pour passer à l'étape suivante.

13

Votre hardware wallet vous montre une nouvelle fois l'intégralité de vos mots. Vérifiez que vous les avez tous bien notés.

14

## Mise en place du code PIN

Vient ensuite l'étape du code PIN. Le code PIN permet de déverrouiller votre Trezor. C'est donc une protection contre les accès physiques non autorisés. Ce code PIN n'intervient pas dans la dérivation des clés cryptographiques de votre portefeuille. Ainsi, même sans accès à ce code PIN, la possession de votre phrase mnémonique de 12 mots vous permettra de retrouver l'accès à vos bitcoins.

Sur Trezor Suite, cliquez sur "Continue to PIN", puis sur le bouton "Set PIN".

15

Confirmez sur le Model One.

16

Il est recommandé de choisir un code PIN le plus aléatoire possible. Assurez-vous également de sauvegarder ce code dans un lieu distinct de celui où est stocké votre Trezor (par exemple, dans un gestionnaire de mot de passe). Vous avez la possibilité de définir un code PIN composé de 8 à 50 chiffres. Je vous recommande de choisir un code PIN aussi long que possible pour renforcer la sécurité.

Le code PIN doit être saisi dans Trezor Suite sur votre ordinateur en cliquant sur les points qui correspondent aux chiffres, selon la configuration du clavier affichée sur le Trezor Model One.

Cette méthode spécifique de saisie du code PIN est requise chaque fois que vous déverrouillez votre Trezor Model One, que ce soit via Trezor Suite ou Sparrow Wallet.

17

Une fois terminé, cliquez sur le bouton "Enter PIN".

18

Notez une seconde fois votre code PIN pour confirmer.

19

Sur Trezor Suite, cliquez sur le bouton "Complete setup".

20

La configuration de votre Model One est désormais terminée. Si vous le souhaitez, vous pouvez modifier le nom et la page d'accueil de votre hardware wallet.

21

Nous n'aurons plus besoin du logiciel Trezor Suite, sauf pour effectuer des mises à jour régulières du firmware de votre hardware wallet, ou bien si vous souhaitez faire un test de récupération. Nous allons maintenant utiliser Sparrow pour gérer le portefeuille, car ce logiciel est parfaitement adapté pour une utilisation Bitcoin-only.

## Configurer le portefeuille sur Sparrow Wallet

Commencez par télécharger et installer Sparrow Wallet [depuis le site officiel](https://sparrowwallet.com/) sur votre ordinateur, si ce n'est pas déjà fait.

Une fois Sparrow Wallet ouvert, assurez-vous que le logiciel est bien connecté à un nœud Bitcoin, ce qui est indiqué par la coche en bas à droite de l'interface. Si vous rencontrez des difficultés pour connecter Sparrow, je vous recommande de consulter le début de ce tutoriel :

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Cliquez sur l'onglet "File", puis sur "New Wallet".

22

Nommez votre portefeuille, puis cliquez sur "Create Wallet".

23

Dans le menu déroulant "Script Type", sélectionnez le type de script qui sera utilisé pour sécuriser vos bitcoins. Je vous recommande d'opter pour "Taproot", ou à défaut, "Native SegWit".

24

Cliquez sur le bouton "Connected Hardware Wallet". Votre Model One doit évidemment être connecté à l'ordinateur.

25

Cliquez sur le bouton "Scan". Votre Model One devrait apparaitre.

Lorsque vous connectez votre Model One à un ordinateur avec Sparrow Wallet ouvert, on vous proposera ensuite de saisir une passphrase BIP39 sur Sparrow. Cette option avancée sera abordée dans un futur tutoriel. Pour l'instant, vous pouvez simplement sélectionner "Toggle Passphrase Off" pour éviter que votre Trezor ne vous demande de saisir une passphrase à chaque démarrage.

26

Cliquez sur "Import Keystore".

27

Vous pouvez maintenant voir les détails de votre portefeuille, y compris la clé publique étendue de votre premier compte. Cliquez sur le bouton "Apply" pour finaliser la création du portefeuille.

28

Choisissez un mot de passe fort pour sécuriser l'accès à Sparrow Wallet. Ce mot de passe assurera la sécurité de l'accès aux données de votre portefeuille sur Sparrow, ce qui permet de protéger vos clés publiques, vos adresses, vos labels et l'historique de vos transactions contre tout accès non autorisé.

Je vous conseille de sauvegarder ce mot de passe dans un gestionnaire de mots de passe pour ne pas l'oublier.

29

Et voilà, votre portefeuille est bien importé sur Sparrow Wallet !

30

Avant de recevoir vos premiers bitcoins sur votre portefeuille, **je vous conseille vivement de réaliser un test de récupération à vide**. Notez une information de référence, telle que votre xpub, puis réinitialisez votre Trezor Model One tant que le portefeuille est encore vide. Ensuite, essayez de restaurer votre portefeuille sur le Trezor en utilisant vos sauvegardes papier. Vérifiez que la xpub générée après la restauration correspond à celle que vous aviez notée initialement. Si c'est le cas, vous pouvez être assuré que vos sauvegardes papier sont fiables.

Pour en savoir plus sur comment effectuer un test de récupération, je vous conseille de consulter cet autre tutoriel :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Comment recevoir des bitcoins avec le Trezor Model One ?

Sur Sparrow, cliquez sur l'onglet "Receive".

31

Avant d'utiliser l'adresse proposée par Sparrow Wallet, vérifiez-la sur l'écran de votre Trezor. Cette pratique vous permet de confirmer que l'adresse affichée sur Sparrow n'est pas frauduleuse et que le hardware wallet détient bien la clé privée nécessaire pour dépenser ultérieurement les bitcoins sécurisés avec cette adresse. Cela vous permet d'éviter plusieurs types d'attaques.

Pour effectuer cette vérification, cliquez sur le bouton "Display Address".

32

Vérifiez que l'adresse affichée sur votre Trezor correspond à celle indiquée sur Sparrow Wallet. Il est également recommandé de réaliser cette vérification juste avant de communiquer votre adresse à l'envoyeur, afin d'être sûr de sa validité. Vous pouvez appuyer sur le bouton droit pour confirmer.

33

Vous pouvez également ajouter un "Label" pour décrire la source des bitcoins qui seront sécurisés avec cette adresse. C'est une bonne pratique qui vous permet de mieux gérer vos UTXOs.

34

Vous pouvez ensuite utiliser cette adresse pour recevoir des bitcoins.

35

## Comment envoyer des bitcoins avec le Trezor Model One ?

Maintenant que vous avez reçu vos premiers sats sur votre portefeuille sécurisé avec le Model One, vous pouvez également les dépenser ! Connectez votre Trezor à votre ordinateur, lancez Sparrow Wallet, puis allez dans l'onglet "Send" pour construire une nouvelle transaction.

36

Si vous souhaitez faire du *Coin Control*, c'est-à-dire choisir spécifiquement quels UTXOs consommer dans la transaction, rendez-vous dans l'onglet "UTXOs". Sélectionnez les UTXOs que vous souhaitez dépenser, puis cliquez sur "Send Selected". Vous serez redirigé vers le même écran de l'onglet "Send", mais avec vos UTXOs déjà sélectionnés pour la transaction.

37

Entrez l'adresse de destination. Vous pouvez également entrer plusieurs adresses en cliquant sur le bouton "+ Add".

38

Notez un "Label" pour vous souvenir de l'objet de cette dépense.

39

Choisissez le montant envoyé à cette adresse.

40

Ajustez le taux de frais de votre transaction en fonction du marché du moment. Vous pouvez par exemple utiliser [mempool.space](https://mempool.space/) pour choisir un taux de frais adapté.

Assurez-vous que tous les paramètres de votre transaction sont corrects, puis cliquez sur "Create Transaction".

41

Si tout vous convient, cliquez sur "Finalize Transaction for Signing".

42

Cliquez sur "Sign".

43

Cliquez sur "Sign" à côté de votre Trezor Model One.

44

Vérifiez les paramètres de la transaction sur l'écran de votre hardware wallet, notamment l'adresse de réception du destinataire, le montant envoyé et le montant des frais. Une fois la transaction vérifiée sur le Trezor, cliquez sur le bouton droit pour la signer.

45

Votre transaction est désormais signée. Vérifiez une dernière fois que tout vous convient, puis cliquez sur "Broadcast Transaction" pour la diffuser sur le réseau Bitcoin.

46

Vous pouvez la retrouver dans l'onglet "Transactions" de Sparrow Wallet.

47

Félicitations, vous êtes maintenant au point sur l'utilisation de base du Trezor Model One avec Sparrow Wallet ! Dans un prochain tutoriel, nous verrons comment utiliser un hardware wallet Trezor avec une passphrase BIP39 pour renforcer sa sécurité.

Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci beaucoup !
