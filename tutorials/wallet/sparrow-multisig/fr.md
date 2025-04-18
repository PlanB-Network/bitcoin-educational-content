---
name: Sparrow Wallet - Multisig
description: Créer un portefeuille multisignature sur Sparrow
---
![cover](assets/cover.webp)

Un portefeuille multisignature (souvent appelé "multisig") est une structure de portefeuille Bitcoin qui exige plusieurs signatures cryptographiques, issues de clés différentes, pour autoriser une dépense. Contrairement à un portefeuille classique ("singlesig"), où une seule clé privée suffit à déverrouiller un UTXO, le multisig repose sur un modèle **m-de-n** : parmi les _n_ clés associées au portefeuille, _m_ doivent impérativement co-signer chaque transaction.

Ce mécanisme permet de répartir le contrôle d’un portefeuille entre plusieurs entités ou dispositifs. Par exemple, dans une configuration 2-de-3, trois ensembles de clés indépendants sont générés, mais deux suffisent pour débloquer les fonds. Cette architecture réduit drastiquement les risques liés à la compromission ou à la perte d’une clé : un voleur ayant accès à une seule clé ne peut pas vider le portefeuille, et un utilisateur qui en perd une peut encore accéder à ses fonds avec les deux restantes.

01

Cependant, cette meilleure sécurité s’accompagne d’une complexité plus élevée. La configuration d’un portefeuille multisig nécessite la sécurisation de plusieurs phrases mnémoniques (une par facteur de signature) et des clés publiques étendues ("xpub"). En effet, si vous utilisez un portefeuille multisig 2-de-3, pour récupérer le portefeuille, vous devez soit posséder les trois phrases mnémoniques, soit disposer d'au moins deux des trois phrases. Mais si vous n'avez que deux phrases sur les trois, il faut également avoir accès aux trois *xpubs*, sans lesquelles il sera impossible de retrouver les clés publiques nécessaires pour accéder aux bitcoins qu'elles protègent.

Pour résumer, pour récupérer un portefeuille multisig, vous devez :
- Soit avoir accès à toutes les phrases mnémoniques associées à chaque facteur de signature ;
- Soit disposer du nombre minimum de phrases mnémoniques requis par le seuil pour pouvoir signer, et également avoir accès aux xpubs de tous les facteurs afin de pouvoir récupérer les clés publiques nécessaires.

02

Cette gestion des sauvegardes des portefeuilles multisig est facilitée par les *Output Script Descriptors*, qui regroupent toutes les données publiques nécessaires pour accéder aux fonds. Cependant, cette fonctionnalité n'est pas encore implémentée dans tous les logiciels de gestion de portefeuille.

Le multisig est particulièrement adapté aux bitcoiners qui recherchent une sécurité renforcée ou une gestion collective des fonds : entreprises, associations, familles, ou utilisateurs individuels détenant un montant significatif de bitcoins. Il permet de créer des schémas de gouvernance décentralisés, par exemple pour répartir le pouvoir de signature entre plusieurs dirigeants ou membres d’une équipe.

Dans ce tutoriel, nous allons apprendre à créer et utiliser un portefeuille multisignature classique avec **Sparrow Wallet**. Si vous souhaitez créer un portefeuille multisignature personnalisé avec des timelocks, je vous recommande plutôt d'utiliser le logiciel Liana :

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Prérequis

Pour ce tutoriel, je vais vous montrer comment réaliser un multisig avec [le logiciel de gestion de portefeuille Sparrow Wallet](https://sparrowwallet.com/download/). Si vous n'avez pas encore installé ce logiciel, je vous invite à le faire dès maintenant. Si vous avez besoin d'aide, nous disposons également d'un tutoriel détaillé sur la configuration de Sparrow Wallet :

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Pour mettre en place un portefeuille multisignature, il vous faudra différents hardware wallets. Pour un multisig 2-de-3, par exemple, vous pourriez utiliser :
- Un Trezor Model One ;
- Un Ledger Flex ;
- Une Coldcard MK3.

Il est judicieux d'utiliser des marques de hardware wallet différentes au sein de votre configuration multisig. Cela garantit que si un modèle spécifique rencontre un problème grave, cela n'affectera pas la sécurité globale de votre multisig. De plus, cela vous permet de profiter des avantages spécifiques de chaque appareil. Par exemple, dans ma configuration :

- Le Trezor Model One est entièrement open-source, ce qui permet de vérifier la génération de la seed. Cependant, comme il n'est pas équipé d'un Secure Element, il reste vulnérable aux attaques physiques ;

- Le Ledger Flex, à l'inverse, bénéficie d'un firmware propriétaire non vérifiable, mais il intègre un Secure Element qui offre une excellente protection physique ;

- La Coldcard est équipée d'un Secure Element et son code est consultable. Elle est intéressante dans notre configuration, car elle offre des fonctionnalités de vérification que les autres modèles ne proposent pas.

Avant de procéder à la configuration de votre portefeuille multisig, assurez-vous que chaque hardware wallet est correctement configuré (génération et sauvegarde de la phrase mnémonique, définition du code PIN). Pour des instructions détaillées, vous pouvez consulter nos tutoriels pour chaque hardware wallet, par exemple :

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Comme nous allons le voir plus tard dans ce tutoriel, il est également possible d'intégrer dans votre configuration multisig un facteur qui n'est pas associé à un hardware wallet, mais dont les clés privées sont conservées sur votre PC. Cette méthode est évidemment moins sécurisée que l'utilisation exclusive de hardware wallets, mais elle peut être pertinente dans certains cas. Par exemple, pour un multisig 2-de-3, vous pourriez opter pour deux hardware wallets et un software wallet.

## Créer un portefeuille multisig

Ouvrez Sparrow Wallet, puis cliquez sur l'onglet "File" puis "New Wallet".

03

Choisissez un nom pour votre portefeuille multisig, puis cliquez sur le bouton "Create Wallet".

04

Dans la liste déroulante "Policy Type", il faut choisir "Multi Signature".

05

En haut à droite, vous pouvez maintenant ajuster le nombre de clés dans votre multisig et le nombre de co-signataire nécessaire pour débloquer les bitcoins. Dans mon cas, je fais un 2-de-3.

06

En bas de la fenêtre, vous pouvez voir que Sparrow Wallet indique 3 "Keystore". Chaque "Keystore" correspond à un ensemble de clés. Dans mon cas, j'utilise 3 hardware wallets, donc chaque "Keystore" sera un de mes hardware wallets. Il va falloir maintenant les paramétrer.

Commençons avec la Coldcard. Sur l'onglet "Keystore 1", je sélectionne "Airgapped Hardware Wallet".

07

Sur la Coldcard, après l'avoir déverouillée, je vais dans le menu "Settings", puis "Multisig Wallets".

08

C'est dans ce menu que l'on peut gérer les multisigs danbs lesquels participe le portfeuille de la Coldcard. Je souahite en créer un nouveau donc je clique sur "Export XPUB".

09

Pour le numéro de compte, si vous n'en utilisez qu'un seul, vous pouvez laisser cette information vide et cliquer sur le bouton de validation.

10

La Coldcard va générer un fichier contenant votre xpub sur la carte Micro SD.

11

Insérez la Micro SD dans votre ordinateur, puis sur Sparrow Wallet cliquez sur le bouton "Import File..." à côté de "Coldcard Multisig". Choisissez le fichier généré par la Coldcard sur la Micro SD.

12

Votre xpub a bien été ajoutée. Nous allons maintenant répéter l'opération pour les deux autre hardware wallets.

13

Pour la Ledger Flex, je clique sur "Keystore 2", puis sur "Conencted Hardware Wallet". La Ledger doit être branchée à l'ordinateur, déverouillée, et avec l'application Bitcoin ouverte.

14

Cliquez sur le bouton "Scan...".

15

À côté de votre hardware wallet, cliquez sur "Import Keystore".

16

Votre second signataire est bien enregistré sur Sparrow.

17

Je répète exactement la même opération avec le Trezor One pour compléter la configuraiton du multisig.

18

Maintenant que tous vos appareils de signature ont été importé sur Sparrow, vous pouvez confirmer la création du multisig en cliquant sur le bouton "Apply".

19

Définissez un mot de passe robuste pour sécuriser l'accès à votre portefeuille sur Sparrow Wallet. Ce mot de passe protégera vos clés publiques, vos adresses, vos étiquettes, et l'historique de vos transactions contre les accès non autorisés.

Il est recommandé de sauvegarder ce mot de passe pour éviter de l'oublier (par exemple dans un gestionnaire de mots de passe).

20

## Sauvegarder un portefeuille multisig

Nous allons maintenant enregistrer notre *Output Script Descriptor* sur la Coldcard (valable uniquement si vous utilisez une Coldcard dans votre multisig), et surtout, nous allons également en faire une sauvegarde sur un support différent.

Le *Descriptor* contient toutes les xpubs de votre portefeuille multisig, ainsi que les chemins de dérivations utilisés pour dériver les différentes clés. Rappelez-vous de ce que je vous ai expliqué dans la première partie : pour récupérer un portefeuille multisig, vous avez besoin soit d'avoir accès à **toutes** les phrase mnémoniques, soit au nombre minimal de phrases mnémoniques pour atteindre le seuil nécessaire de signatures, mais dans ce second cas, vous devez également avoir accès aux xpubs des signataires manquants. Cela tombe bien, le *Descriptor* contient toutes les xpubs de votre multisig.

Si vous n'avez pas ciompris, pour simplifier : pour récupérer un multisig, vous avez besoin à la fois des phrases mnémoniques de chaque hardware wallet, et du *Descriptor*.

Ce *Descriptor* ne contient aucune information sur vos clés privées. Il ne contient que vos clés publiques. Cela signifie que ce n'est pas une information aussi sensible que vos phrase mnémoniques (qui elles, donnent accès à tous vos bitcoins). Le *Descriptor* est donc uniquement un risque de confidentialité. Si vous vous le faites voler, la personne en sa possession ne pourra pas voler les bitcoins de votre multisig, en revanche, il pourra observer toutes vos transactions.

Je vous conseille donc de réaliser plusieurs copies de ce *Descriptor*, et si possible, de les conserver avec chaque facteur de signature de votre multisig. Par exemple, dans mon cas, je vais imprimer sur papier le *Descriptor* et conserver une copie papier avec la Coldcard, une autre avec le Trezor et une dernière avec le Ledger. Je vais également mettre ce *Descriptor* sous forme de fichier PDF dans 3 clés USB, et conserver une clé USB avec chaque hardware wallet. Ainsi, je suis maximise mes chances de ne pas perdre ce *Descriptor*, et je sais que j'en ai 2 copies (une physique et une numréique) avec chaque hardware wallet du multisig.

Après la création de votre wallet, Sparrow vous donne votre *Descriptor*. Vous pouvez cliquer sur le bouton "Save PDF..." pour l'enregistrer à la fois en version écrite et sous forme de QR code.

21

Vous pourrez ensuite imprimer ce PDF et le mettre sur les clés USB.

22

Ce *Descriptor*, nous allons également l'enregistrer dans notre Coldcard (si vous en avez une dans votre setup). Cela va permettre à la Coldcard de vérifier que chaque transaction que nous signerons par la suite correspond bien à la configuration d’origine : bonnes xpubs, bon ordre des clés, bon type d’adresse, bon chemin de dérivation... Sans ce *Descriptor* enregistré, la Coldcard ne peut pas s’assurer que les adresses de change ne sont pas détournées ni que la PSBT n’a pas été manipulée.

C'est pour cela que la Coldcard est très intéressante dans un multisig. Elle permet de vérifier des paramètres supplémentaires pour faire face à certaines attaques avancées que les autres hardware wallets ne permettent pas (à condition de l'utiliser lorsque l'on signe évidemment).

Sur Sparrow, dans le menu "Settings", cliquez sur le bouton "Export...".

23

À côté de "Coldcard Multisig", cliquez sur le bouton "Export File...", puis enregistrez le fichier texte sur votre carte Micro SD.

24

Aprez avoir inséré cette carte Micro SD dans la Coldcard, rendez-vous de nouveau dans le menu "Settings" puis "Multisig Wallets" et sélectionnez l'option "Import from SD".

25

Choisissez le bon fichier puis confirmez.

26

Cliquez sur le nom de votre multisig.

27

Vérifiez les paramètres de votre multisig, puis confirmez son enregistrement.

28

Votre multisig est dorénavant bien enregistré dans votre Coldcard. Si vous avez plusieurs Coldcard au sein de votre multisig, répétez cette opération.

En plus de la sauvegarde du *Descriptor*, vous devez évidemment soigner la sauvegarde des phrase mnémoniques de chacun de vos facteurs de signature. Pour plus d'informations sur la manière adéquate de sauvegarder et de gérer votre phrase mnémonique, je vous recommande vivement de suivre cet autre tutoriel, particulièrement si vous êtes débutant :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Avant de recevoir vos premiers bitcoins sur votre multisig, **je vous conseille vivement de réaliser un test de récupération à vide**. Notez une information de référence, telle que la première adresse de réception, puis réinitialisez vos hardware wallets tant que le portefeuille est encore vide. Ensuite, essayez de restaurer votre portefeuille multisig sur les hardware wallet en utilisant vos sauvegardes papier des phrase mnémonique, puis sur Sparrow en utilisant le *Descriptor*. Vérifiez que la première adresse générée après la restauration correspond à celle que vous aviez notée initialement. Si c'est le cas, vous pouvez être assuré que vos sauvegardes papier sont fiables.

Pour en savoir plus sur comment effectuer un test de récupération, je vous conseille de consulter cet autre tutoriel :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Recevoir des bitcoins sur son multisig

Maintenant que votre portefeuille est créé, vous allez pouvoir recevoir des bitcoins. Sur Sparrow, cliquez sur l'onglet "Receive".

29

Avant d'utiliser l'adresse proposée par Sparrow Wallet, vérifiez-la sur l'écran de vos hardware wallets. Cette pratique vous permet de confirmer que l'adresse affichée sur Sparrow n'est pas frauduleuse et que les hardwares wallet détiennent bien les clés privées nécessaires pour dépenser ultérieurement les bitcoins sécurisés avec cette adresse. Cela vous permet d'éviter plusieurs types d'attaques.

Pour effectuer cette vérification, cliquez sur le bouton "Display Address" pour la Trezor ou laLedger qui foncitonnent par cable.

30

Sur la Coldcard, vous pouvez vérifier l'adresse sans avoir à communiquer avec Sparrow. Rendez-vous dans le menu "Address Explorer", puis sélectionnez votre multisig en bas du menu.

31

Vous pouvez alors voir vos adresses de réceptions.

32

Vérifiez que l'adresse affichée sur votre les hardware wallets correspond à celle indiquée sur Sparrow Wallet. Il est également recommandé de réaliser cette vérification juste avant de communiquer votre adresse à l'envoyeur, afin d'être sûr de sa validité.

Vous pouvez ensuite ajouter un "Label" pour décrire la source des bitcoins qui seront sécurisés avec cette adresse. C'est une bonne pratique qui vous permet de mieux gérer vos UTXOs.

33

Vous pouvez ensuite utiliser cette adresse pour recevoir des bitcoins.

34

## Envoyer des bitcoins avec son multisig

Maintenant que vous avez reçu vos premiers sats sur votre portefeuille multisig, vous pouvez également les dépenser ! Sur Sparrow, rendez-vous dans l'onglet "Send" pour construire une nouvelle transaction.

35

Si vous souhaitez faire du *Coin Control*, c'est-à-dire choisir spécifiquement quels UTXOs consommer dans la transaction, rendez-vous dans l'onglet "UTXOs". Sélectionnez les UTXOs que vous souhaitez dépenser, puis cliquez sur "Send Selected". Vous serez redirigé vers le même écran de l'onglet "Send", mais avec vos UTXOs déjà sélectionnés pour la transaction.

36

Entrez l'adresse de destination. Vous pouvez également entrer plusieurs adresses en cliquant sur le bouton "+ Add".

37

Notez un "Label" pour vous souvenir de l'objet de cette dépense.

38

Choisissez le montant envoyé à cette adresse.

39

Ajustez le taux de frais de votre transaction en fonction du marché du moment. Vous pouvez par exemple utiliser [mempool.space](https://mempool.space/) pour choisir un taux de frais adapté.

Assurez-vous que tous les paramètres de votre transaction sont corrects, puis cliquez sur "Create Transaction".

40

Si tout vous convient, cliquez sur "Finalize Transaction for Signing".

41

Vous pouvez voir sur le bas de la page que Sparrow attend 2 signatures. C'est normal, j'ai réalisé ici un portefeuille multisig 2-de-3.

42

Je vais commencer par signer avec ma Coldcard. Pour ce faire, il faut insérer une carte Micro SD dans l'ordinateur, puis cliquer sur le bouton "Save Transaction".

43

Il existe en tout 3 options pour communiquer la transaction à signer au hardware wallet, puis pour la récupérer sur Sparrow. Il y a celle avec la Micro SD comme nous allons faire ici. Il y a également la méthode de communication par cable que nous allons voir avec la seconde signature. Et enfin, il y a l'option avec QR code pour les hardware wallets qui sont équipés d'une caméra comme la Coldcard Q, le Jade Plus ou encore le Passport V2.

Après avoir enregistré la PSBT (*Partially signed bitcoin transactions*) sur la micro SD, je l'insère dans la Coldcard MK3. Il faut donc cliquer sur le menu "Ready to Sign"

44

Vérifiez les paramètres de la transaction sur l'écran de votre hardware wallet, notamment l'adresse de réception du destinataire, le montant envoyé et le montant des frais. Une fois la transaciton vérifiée, cliquez sur le bouton de validation pour la signer.

45

Placez de nouveau la Micro SD dans votre ordinateur, puis cliquez sur le bouton "Load Transaction" sur Sparrow. Puis, sélectionnez la PSBT signée par la Coldcard parmis vos fichiers.

46

On peut voir que la signature de la Coldcard a bien été ajoutée. Je peux maintenant choisir de signer avec un second périphérique, soit le Trezor, soit la Ledger. Ici je vais le faire avec la Ledger. Je clique donc sur "Sign" après l'avoir branchée et déverouillée.

47

Cliquez sur "Sign" à côté de votre hardware wallet.

48

La première fois que vous utilisez la Ledger avec votre mutlisig, il vous sera demandé de vérifier les clés publiques étendues des co-signataires. De la même manière que pour la Coldcard, cela vous permet de ne pas signer à l'aveugle par la suite. Pour être sûr que ces informations sont bien bonnes, vous pouvez comparer la xpub sur l'écran de la Ledger avec la xpub donnée par chaque hardware wallet sur son écran.

49

Vous pourrez ensuite signer la transaction. De la même manière que pour la signature avec la Coldcard, vérifiez les paramètres de la transaction, notamment l'adresse de réception du destinataire, le montant envoyé et le montant des frais.

50

Une fois la transaction vérifiée, appuyez de manière prolongée sur l'écran pour la signer.

51

Sur Sparrow, vous avez maintenant les 2 signatures nécessaire pour dépenser les fonds de votre multisig. Vérifiez une dernière fois la transaciton, et si tout vous convient, vous pouvez la diffuser aux noeud du réseau en cliquant sur le bouton "Broadcast Transaction".

52

Vous pouvez la retrouver dans l'onglet "Transactions" de Sparrow Wallet.

53

Félicitations, vous savez dorénavant comment configurer et utiliser un portefeuille multisignature sur Sparrow. Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci !

Pour aller plus loin, je vous recommande de consulter ce tutoriel sur une autre méthode pour augmenter la sécurité de votre portefeuille Bitcoin, la Passphrase BIP39 :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
