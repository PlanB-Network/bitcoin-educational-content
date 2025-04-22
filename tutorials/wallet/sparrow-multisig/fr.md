---
name: Sparrow Wallet - Multisig
description: Créer un portefeuille multisignature sur Sparrow
---
![cover](assets/cover.webp)

Un portefeuille multisignature (souvent appelé "*multisig*") est une structure de portefeuille Bitcoin qui exige plusieurs signatures cryptographiques, issues de clés différentes, pour autoriser une dépense. Contrairement à un portefeuille classique ("*singlesig*"), où une seule clé privée suffit à déverrouiller un UTXO, le multisig repose sur un modèle **m-de-n** : parmi les _n_ clés associées au portefeuille, _m_ doivent impérativement co-signer chaque transaction.

Ce mécanisme permet de répartir le contrôle d’un portefeuille entre plusieurs entités ou dispositifs. Par exemple, dans une configuration 2-de-3, trois ensembles de clés indépendants sont générés, mais deux suffisent pour débloquer les fonds. Cette architecture réduit drastiquement les risques liés à la compromission ou à la perte d’une clé : un voleur ayant accès à une seule clé ne peut pas vider le portefeuille, et un utilisateur qui en perd une peut encore accéder à ses fonds avec les deux restantes.

![Image](assets/fr/01.webp)

Cependant, cette meilleure sécurité s’accompagne d’une complexité plus élevée. La configuration d’un portefeuille multisig nécessite la sécurisation de plusieurs phrases mnémoniques (une par facteur de signature) et des clés publiques étendues ("*xpub*"). En effet, si vous utilisez un portefeuille multisig 2-de-3, pour récupérer le portefeuille, vous devez soit posséder les trois phrases mnémoniques, soit disposer d'au moins deux des trois phrases. Mais si vous n'avez que deux phrases sur les trois, il faut également avoir accès aux trois *xpubs*, sans lesquelles il sera impossible de retrouver les clés publiques nécessaires pour accéder aux bitcoins qu'elles protègent.

Pour résumer, pour récupérer un portefeuille multisig, vous devez :
- Soit avoir accès à toutes les phrases mnémoniques associées à chaque facteur de signature ;
- Soit disposer du nombre minimum de phrases mnémoniques requis par le seuil pour pouvoir signer, et également avoir accès aux xpubs de tous les facteurs afin de pouvoir récupérer les clés publiques nécessaires.

![Image](assets/fr/02.webp)

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

![Image](assets/fr/03.webp)

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

Ouvrez Sparrow Wallet, cliquez sur l'onglet "*File*", puis sélectionnez "*New Wallet*".

![Image](assets/fr/04.webp)

Attribuez un nom à votre portefeuille multisignature, puis validez en cliquant sur "*Create Wallet*".

![Image](assets/fr/05.webp)

Dans le menu déroulant "*Policy Type*", sélectionnez l’option "*Multi Signature*".

![Image](assets/fr/06.webp)

En haut à droite, vous pouvez désormais définir le nombre total de clés de votre multisig ainsi que le nombre de co-signataires requis pour autoriser une dépense. Dans mon exemple, il s’agit d’un schéma 2-de-3.

![Image](assets/fr/07.webp)

En bas de la fenêtre, Sparrow Wallet affiche trois "*Keystore*". Chacun représente un ensemble de clés. Ici, j’utilise trois portefeuilles matériels, chaque "*Keystore*" correspond donc à l’un d’entre eux. Nous allons maintenant les configurer.

Je commence avec la Coldcard. Dans l’onglet "*Keystore 1*", je choisis l’option "*Airgapped Hardware Wallet*".

![Image](assets/fr/08.webp)

Sur la Coldcard, une fois l’appareil déverrouillé, je me rends dans le menu "*Settings*", puis dans "*Multisig Wallets*".

![Image](assets/fr/09.webp)

Ce menu permet de gérer les portefeuilles multisigs auxquels la Coldcard participe. Je souhaite en créer un nouveau, je sélectionne donc "*Export XPUB*".

![Image](assets/fr/10.webp)

Pour le champ "*Account number*", si vous ne gérez qu’un seul compte, vous pouvez le laisser vide et valider directement en appuyant sur le bouton de confirmation.

![Image](assets/fr/11.webp)

La Coldcard va alors générer un fichier contenant votre xpub, enregistré sur la carte Micro SD.

![Image](assets/fr/12.webp)

Insérez cette Micro SD dans votre ordinateur. Dans Sparrow Wallet, cliquez sur le bouton "*Import File...*" situé à côté de "*Coldcard Multisig*", puis sélectionnez le fichier créé par la Coldcard sur la carte.

![Image](assets/fr/13.webp)

Votre xpub a bien été importée. Nous allons maintenant répéter la procédure avec les deux autres hardware wallets.

![Image](assets/fr/14.webp)

Pour la Ledger Flex, je sélectionne "*Keystore 2*", puis je clique sur "*Connected Hardware Wallet*". Assurez-vous que la Ledger est connectée à l’ordinateur, déverrouillée, et que l’application Bitcoin est bien ouverte.

![Image](assets/fr/15.webp)

Cliquez ensuite sur le bouton "*Scan...*".

![Image](assets/fr/16.webp)

À côté du nom de votre portefeuille matériel, cliquez sur "*Import Keystore*".

![Image](assets/fr/17.webp)

Le second signataire est maintenant correctement enregistré dans Sparrow Wallet.

![Image](assets/fr/18.webp)

Je réitère exactement la même procédure avec le Trezor One afin de finaliser la configuration du multisig.

![Image](assets/fr/19.webp)

Dans ma configuration nous ne couvrons pas ce cas, mais si vous souhaitez inclure une signature via un portefeuille logiciel dans Sparrow (portefeuille chaud) au sein de votre multisig, cliquez simplement sur le bouton "*New or Imported Software Wallet*".

Maintenant que tous vos dispositifs de signature sont importés dans Sparrow Wallet, vous pouvez finaliser la création du multisig en cliquant sur "*Apply*".

![Image](assets/fr/20.webp)

Choisissez un mot de passe robuste pour sécuriser l’accès à votre portefeuille sur Sparrow Wallet. Ce mot de passe protège vos clés publiques, vos adresses, vos étiquettes et l’historique de vos transactions contre tout accès non autorisé.

Pensez à sauvegarder ce mot de passe dans un endroit sûr, comme un gestionnaire de mots de passe, afin d’éviter de le perdre.

![Image](assets/fr/21.webp)

## Sauvegarder un portefeuille multisig

Nous allons maintenant enregistrer notre *Output Script Descriptor* sur la Coldcard (cela ne concerne que les utilisateurs intégrant une Coldcard dans leur multisig), et surtout, nous allons en conserver une sauvegarde sur un support indépendant.

Le *Descriptor* regroupe l’ensemble des xpubs de votre portefeuille multisig, ainsi que les chemins de dérivation utilisés pour générer les clés. Souvenez-vous de ce que nous avons vu dans la première partie : pour restaurer un portefeuille multisig, il faut soit disposer **de toutes** les phrases mnémoniques, soit uniquement du nombre minimal requis pour atteindre le seuil de signatures. Toutefois, dans ce second cas, il est également indispensable d’avoir **les xpubs** des signataires manquants. Le *Descriptor* contient justement toutes les xpubs de votre multisig.

Si ce n’est pas clair, retenez simplement ceci : pour récupérer un multisig, il vous faut le nombre minimal de phrases mnémoniques de chaque hardware wallet utilisé en fonction du seuil (dans mon cas : 2 phrases), ainsi que le *Descriptor*.

Ce *Descriptor* ne contient aucune clé privée, uniquement des clés publiques. Cela signifie qu’il ne permet pas d’accéder aux fonds. Il n’est donc pas aussi critique que les phrases mnémoniques, qui, elles, donnent un accès total à vos bitcoins. Le risque avec le *Descriptor* est uniquement lié à la confidentialité : en cas de compromission, une tierce personne pourrait observer toutes vos transactions, mais ne pourrait pas dépenser vos fonds.

Je vous recommande vivement de créer plusieurs copies de ce *Descriptor*, et de les conserver avec chaque dispositif de signature de votre multisig. Par exemple, dans mon cas, j’imprime le *Descriptor* sur papier et j’en conserve une copie avec la Coldcard, une autre avec le Trezor, et une dernière avec la Ledger. J’enregistre aussi ce *Descriptor* sous forme de fichier PDF sur trois clés USB, chacune rangée avec l’un des portefeuilles matériels. De cette manière, je maximise mes chances de ne jamais perdre ce *Descriptor*, et je suis certain d’avoir deux copies (une physique et une numérique) avec chaque appareil.

Une fois votre portefeuille multisig créé, Sparrow vous fournit automatiquement ce *Descriptor*. Cliquez sur le bouton "*Save PDF...*" pour le sauvegarder à la fois en version texte et sous forme de QR code.

![Image](assets/fr/22.webp)

Vous pourrez ensuite imprimer ce PDF et le copier sur vos clés USB.

![Image](assets/fr/23.webp)

Nous allons également enregistrer ce *Descriptor* dans la Coldcard (si vous en utilisez une dans votre configuration). Cela permettra à la Coldcard de vérifier que chaque transaction signée ultérieurement correspond bien au portefeuille d’origine : bonnes xpubs, bon format d’adresse, bon chemin de dérivation... Sans ce *Descriptor* importé, la Coldcard ne peut pas confirmer que les adresses de change n’ont pas été détournées ou que la PSBT n’a pas été altérée.

C’est ce qui fait tout l’intérêt de la Coldcard dans un multisig : elle offre des vérifications supplémentaires contre certaines attaques sophistiquées, que d’autres hardware wallets ne permettent pas (à condition bien sûr de l’utiliser pour signer).

Dans Sparrow, accédez au menu "*Settings*", puis cliquez sur "*Export...*".

![Image](assets/fr/24.webp)

À côté de l’option "*Coldcard Multisig*", cliquez sur "*Export File...*" et enregistrez le fichier texte sur la carte Micro SD.

![Image](assets/fr/25.webp)

Insérez ensuite la carte dans la Coldcard. Allez dans le menu "*Settings*", puis "*Multisig Wallets*", et sélectionnez "*Import from SD*".

![Image](assets/fr/26.webp)

Choisissez le fichier approprié et confirmez l’importation.

![Image](assets/fr/27.webp)

Cliquez sur le nom de votre multisig nouvellement importé.

![Image](assets/fr/28.webp)

Vérifiez les paramètres de configuration du multisig, puis confirmez son enregistrement.

![Image](assets/fr/29.webp)

Votre multisig est désormais correctement sauvegardé dans votre Coldcard. Si vous possédez plusieurs Coldcard au sein du même multisig, répétez cette procédure pour chacune d’elles.

Au-delà de la sauvegarde du *Descriptor*, n’oubliez pas de porter une attention toute particulière à la sauvegarde des phrases mnémoniques de chacun de vos dispositifs de signature. Si vous débutez, je vous recommande vivement de consulter cet autre tutoriel pour apprendre à les sauvegarder et les gérer correctement :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Avant de recevoir vos premiers bitcoins sur votre multisig, **je vous conseille vivement de réaliser un test de récupération à vide**. Notez une information de référence, telle que la première adresse de réception, puis réinitialisez vos hardware wallets tant que le portefeuille est encore vide. Ensuite, essayez de restaurer votre portefeuille multisig sur les hardware wallet en utilisant vos sauvegardes papier des phrase mnémonique, puis sur Sparrow en utilisant le *Descriptor*. Vérifiez que la première adresse générée après la restauration correspond à celle que vous aviez notée initialement. Si c'est le cas, vous pouvez être assuré que vos sauvegardes papier sont fiables.

Pour en savoir plus sur comment effectuer un test de récupération, je vous conseille de consulter cet autre tutoriel :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Recevoir des bitcoins sur son multisig

Votre portefeuille est désormais prêt à recevoir des bitcoins. Dans Sparrow, cliquez sur l’onglet "*Receive*".

![Image](assets/fr/30.webp)

Avant d’utiliser l’adresse générée par Sparrow Wallet, prenez le temps de la vérifier directement sur l’écran de vos hardware wallets. Cette vérification vous garantit que l’adresse n’a pas été modifiée et que vos dispositifs détiennent bien les clés privées nécessaires pour dépenser les fonds associés. Cela permet de se prémunir contre plusieurs vecteurs d’attaques.

Pour cela, cliquez sur "*Display Address*" pour afficher l’adresse sur votre Trezor ou votre Ledger, lorsqu’ils sont connectés par câble.

![Image](assets/fr/31.webp)

Avec la Coldcard, cette vérification peut s’effectuer sans aucune interaction avec Sparrow. Il suffit d’ouvrir le menu "*Address Explorer*", puis de sélectionner votre multisig tout en bas du menu.

![Image](assets/fr/32.webp)

Vous verrez alors les adresses de réception générées par le multisig.

![Image](assets/fr/33.webp)

Vérifiez que l’adresse affichée sur chacun des hardware wallets correspond exactement à celle indiquée dans Sparrow Wallet. Il est conseillé de faire cette vérification juste avant de partager l’adresse au payeur, pour être certain de son intégrité.

Vous pouvez ensuite attribuer un "*Label*" à cette adresse, afin d’indiquer la provenance des bitcoins reçus. C’est une bonne pratique pour mieux organiser la gestion de vos UTXOs.

![Image](assets/fr/34.webp)

Une fois cette vérification effectuée, vous pouvez utiliser l’adresse pour recevoir des bitcoins.

![Image](assets/fr/35.webp)

## Envoyer des bitcoins avec son multisig

Maintenant que vous avez reçu vos premiers sats sur votre portefeuille multisig, vous pouvez également les dépenser ! Dans Sparrow, rendez-vous dans l’onglet "*Send*" pour construire une nouvelle transaction.

![Image](assets/fr/36.webp)

Si vous souhaitez pratiquer le *Coin Control*, c’est-à-dire sélectionner manuellement les UTXOs à dépenser, allez dans l’onglet "*UTXOs*". Choisissez les UTXOs désirés, puis cliquez sur "*Send Selected*". Vous serez automatiquement redirigé vers l’onglet "*Send*", avec les UTXOs déjà pré-remplis.

![Image](assets/fr/37.webp)

Renseignez l’adresse de destination. Il est possible d’ajouter plusieurs adresses en cliquant sur "*+ Add*".

![Image](assets/fr/38.webp)

Ajoutez un "*Label*" pour décrire l’objet de cette dépense, afin de faciliter le suivi de vos transactions.

![Image](assets/fr/39.webp)

Indiquez le montant à envoyer vers l’adresse sélectionnée.

![Image](assets/fr/40.webp)

Ajustez le taux de frais selon les conditions actuelles du réseau. Vous pouvez par exemple consulter [mempool.space](https://mempool.space/) pour choisir un niveau de frais adapté.

Après avoir vérifié tous les paramètres de la transaction, cliquez sur "*Create Transaction*".

![Image](assets/fr/41.webp)

Si tout vous convient, poursuivez en cliquant sur "*Finalize Transaction for Signing*".

![Image](assets/fr/42.webp)

En bas de l’écran, vous verrez que Sparrow attend 2 signatures. C’est normal : le portefeuille utilisé ici est un multisig 2-de-3.

![Image](assets/fr/43.webp)

Je commence la signature avec ma Coldcard. Pour cela, j’insère une carte Micro SD dans l’ordinateur, puis je clique sur "*Save Transaction*".

![Image](assets/fr/44.webp)

Il existe 3 méthodes pour transmettre la transaction à signer à votre hardware wallet, puis la récupérer dans Sparrow. La première consiste à utiliser une carte Micro SD, comme nous allons le faire ici pour la Coldcard. La seconde passe par une connexion par câble, que nous utiliserons pour la seconde signature (Ledger et Trezor). Enfin, il est possible d'utiliser une communication par QR code, pour les appareils dotés d’une caméra comme la Coldcard Q, le Jade Plus ou encore le Passport V2.

Une fois la PSBT (*Partially Signed Bitcoin Transaction*) enregistrée sur la Micro SD, je l’insère dans la Coldcard MK3, puis je sélectionne le menu "*Ready to Sign*".

![Image](assets/fr/45.webp)

Sur l’écran de votre hardware wallet, vérifiez attentivement les paramètres de la transaction : l’adresse du destinataire, le montant envoyé, ainsi que les frais. Une fois la transaction confirmée, validez pour procéder à la signature.

![Image](assets/fr/46.webp)

Replacez ensuite la Micro SD dans votre ordinateur, puis cliquez sur "*Load Transaction*" dans Sparrow. Sélectionnez alors la PSBT signée par la Coldcard parmi vos fichiers.

![Image](assets/fr/47.webp)

Vous pouvez constater que la signature de la Coldcard a bien été ajoutée. Je vais maintenant utiliser un second appareil, ici la Ledger, pour réaliser la seconde signature nécessaire. Je la connecte, je la déverrouille, puis je clique sur "*Sign*" sur Sparrow.

![Image](assets/fr/48.webp)

Cliquez sur "*Sign*" à côté du nom de votre hardware wallet.

![Image](assets/fr/49.webp)

Lors de la première utilisation de votre Ledger avec ce multisig, Sparrow vous demandera de vérifier les clés publiques étendues (xpubs) des co-signataires. Comme avec la Coldcard, cette étape évite de signer à l’aveugle par la suite. Pour valider ces informations, comparez la xpub affichée sur l’écran de la Ledger avec celles fournies directement par vos autres hardware wallets.

![Image](assets/fr/50.webp)

Vérifiez l’adresse du destinataire, le montant transféré et les frais de transaction, puis vous pouvez ensuite signer la transaction.

![Image](assets/fr/51.webp)

Appuyez sur l’écran pour signer.

![Image](assets/fr/52.webp)

Sparrow dispose désormais des deux signatures nécessaires pour débloquer les fonds du portefeuille multisig. Vérifiez une dernière fois la transaction, et si tout vous convient, cliquez sur "*Broadcast Transaction*" pour la diffuser sur le réseau.

![Image](assets/fr/53.webp)

Vous retrouverez cette transaction dans l’onglet "*Transactions*" de Sparrow Wallet.

![Image](assets/fr/54.webp)

Félicitations, vous savez dorénavant comment configurer et utiliser un portefeuille multisignature sur Sparrow. Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci !

Pour aller plus loin, je vous recommande de consulter ce tutoriel sur une autre méthode pour augmenter la sécurité de votre portefeuille Bitcoin, la Passphrase BIP39 :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
