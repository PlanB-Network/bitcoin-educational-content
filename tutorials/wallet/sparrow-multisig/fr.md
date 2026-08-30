---
name: Sparrow Wallet - Multisig
description: Créer un portefeuille multisignature sur Sparrow
---
![cover](assets/cover.webp)


Un portefeuille multisignature (souvent appelé « *Multisig* ») est une structure de portefeuille Bitcoin qui exige plusieurs signatures cryptographiques, provenant de clés différentes, pour autoriser une dépense. Contrairement à un portefeuille classique (« *singlesig* »), où une seule clé privée suffit à débloquer un UTXO, le Multisig repose sur un modèle **m-de-n** : parmi les _n_ clés associées au portefeuille, _m_ doivent impérativement cosigner chaque transaction.


Ce mécanisme permet de partager le contrôle d'un portefeuille entre plusieurs entités ou appareils. Par exemple, dans une configuration 2-de-3, trois jeux de clés indépendants sont générés, mais seuls deux sont nécessaires pour libérer les fonds. Cette architecture réduit drastiquement les risques liés à la compromission ou à la perte d'une clé : un voleur ayant accès à une seule clé ne peut pas vider le portefeuille, et un utilisateur qui en perd une peut toujours accéder à ses fonds avec les deux restantes.


![Image](assets/fr/01.webp)


Cependant, cette sécurité accrue s'accompagne d'une complexité plus grande. Configurer un portefeuille Multisig nécessite de sécuriser plusieurs phrases mnémoniques (une par facteur de signature) ainsi que des clés publiques étendues (« *xpub* »). En effet, si vous utilisez un portefeuille Multisig 2-de-3, pour le récupérer vous devez soit disposer des trois phrases mnémoniques, soit d'au moins deux des trois phrases. Mais si vous n'avez que deux des trois phrases, vous avez également besoin d'accéder aux trois *xpubs*, sans lesquelles il sera impossible de retrouver les clés publiques nécessaires pour accéder aux bitcoins qu'elles protègent.


Pour résumer, pour récupérer un portefeuille Multisig, vous devez :


- Soit accéder à toutes les phrases mnémoniques associées à chaque facteur de signature ;
- Soit disposer du nombre minimal de phrases mnémoniques requis par le seuil pour pouvoir signer, et avoir également accès aux xpubs de tous les facteurs afin de retrouver les clés publiques nécessaires.


![Image](assets/fr/02.webp)


Cette gestion des sauvegardes de portefeuille Multisig est facilitée par les *Output Script Descriptors*, qui regroupent toutes les données publiques nécessaires pour accéder aux fonds. Cependant, cette fonctionnalité n'est pas encore implémentée dans tous les logiciels de gestion de portefeuille.


Le Multisig convient particulièrement aux bitcoiners recherchant une sécurité renforcée ou une gestion collective des fonds : entreprises, associations, familles, ou utilisateurs individuels détenant une quantité significative de bitcoins. Il peut être utilisé pour créer des schémas de gouvernance décentralisée, par exemple pour répartir l'autorité de signature entre plusieurs gestionnaires ou membres d'une équipe.


Dans ce tutoriel, nous allons apprendre à créer et utiliser un portefeuille multisignature classique avec **Sparrow Wallet**. Si vous souhaitez créer un portefeuille multisignature personnalisé avec des timelocks, je vous recommande d'utiliser Liana à la place :


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Prérequis


Pour ce tutoriel, je vais vous montrer comment créer un Multisig avec le [logiciel de gestion de portefeuille Sparrow Wallet](https://sparrowwallet.com/download/). Si vous n'avez pas encore installé ce logiciel, faites-le maintenant. Si vous avez besoin d'aide, nous avons également un tutoriel détaillé sur la configuration de Sparrow Wallet :


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

Pour configurer un portefeuille multisignature, vous aurez besoin de différents hardware wallets. Pour un Multisig 2-de-3, par exemple, vous pourriez utiliser :


- Un Trezor Model One ;
- Un Ledger Flex ;
- Un Passport Core.


![Image](assets/fr/03.webp)


Il est conseillé d'utiliser différentes marques de Hardware Wallet dans votre configuration Multisig. Cela garantit que si un modèle spécifique rencontre un problème grave, cela n'affecte pas la sécurité globale de votre Multisig. De plus, cela vous permet de profiter des avantages spécifiques de chaque appareil. Par exemple, dans ma configuration :



- Le Trezor Model One est entièrement open-source, ce qui permet de vérifier la génération de la graine. Cependant, comme il n'est pas équipé d'un Secure Element, il reste vulnérable aux attaques physiques ;



- Le Ledger Flex, quant à lui, bénéficie d'un firmware propriétaire invérifiable, mais intègre un Secure Element qui offre une excellente protection physique ;



- Le Passport Core combine un firmware entièrement open-source, un Secure Element, et des échanges par QR code air-gapped. C'est un troisième signataire indépendant capable de vérifier des adresses et de signer des PSBT sans connexion de données USB.


Avant de configurer votre portefeuille Multisig, assurez-vous que chaque Hardware Wallet est correctement configuré (génération et sauvegarde de la phrase mnémonique, définition du PIN). Pour des instructions détaillées, vous pouvez consulter nos tutoriels pour chaque Hardware Wallet, par exemple :


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Comme nous le verrons plus loin dans ce tutoriel, il est également possible d'intégrer dans votre configuration Multisig un facteur qui n'est pas associé à un Hardware Wallet, mais dont les clés privées sont stockées sur votre PC. Cette méthode est évidemment moins sécurisée que l'utilisation exclusive de hardware wallets, mais elle peut être pertinente dans certains cas. Par exemple, pour un Multisig 2-de-3, vous pourriez opter pour deux hardware wallets et un Software Wallet.

> ⚠️ **Avis de sécurité Coldcard MK3 :** ne créez pas de nouvelle graine sur un MK3 exécutant un firmware antérieur à la version 4.2.0. Les graines générées sur un firmware antérieur doivent être remplacées et les fonds déplacés. Ce tutoriel utilise donc le Passport Core comme signataire de référence air-gapped.


## Créer un portefeuille Multisig


Ouvrez Sparrow Wallet, cliquez sur l'onglet « *File* », puis sélectionnez « *New Wallet* ».


![Image](assets/fr/04.webp)


Attribuez un nom à votre portefeuille multisignature, puis cliquez sur « *Create Wallet* » pour confirmer.


![Image](assets/fr/05.webp)


Dans le menu déroulant « *Policy Type* », sélectionnez l'option « *Multi Signature* ».


![Image](assets/fr/06.webp)


Dans le coin supérieur droit, vous pouvez maintenant définir le nombre total de clés de votre Multisig, ainsi que le nombre de cosignataires requis pour autoriser une dépense. Dans mon exemple, il s'agit d'un schéma 2-de-3.


![Image](assets/fr/07.webp)


En bas de la fenêtre, Sparrow Wallet affiche trois « *Keystore* ». Chacun représente un jeu de clés. Ici, j'utilise trois hardware wallets, donc chaque « *Keystore* » correspond à l'un d'eux. Nous allons maintenant les configurer.


Je commence par le Passport Core. Dans l'onglet « *Keystore 1* », je choisis l'option « *Airgapped Hardware Wallet* ».


![Image](assets/fr/08.webp)


Sur le Passport, ouvrez le compte que vous souhaitez utiliser, puis sélectionnez « *Connect Wallet* » > « *Sparrow* » > « *Connect as Multisig* ». Le Passport affiche un QR code animé contenant les informations de sa clé publique.

Dans Sparrow, sélectionnez « *Scan...* » à côté de « *Passport* » et scannez ce QR code animé avec la webcam de votre ordinateur. Vérifiez que l'empreinte de la clé maîtresse affichée par Sparrow correspond à celle affichée par le Passport, puis importez le keystore.

Votre xpub Passport a maintenant été importée. Répétez la procédure appropriée pour le Ledger Flex et le Trezor Model One.


Pour le Ledger Flex, je sélectionne « *Keystore 2* », puis je clique sur « *Connected Hardware Wallet* ». Assurez-vous que le Ledger est connecté à l'ordinateur, déverrouillé, et que l'application Bitcoin est ouverte.


![Image](assets/fr/15.webp)


Cliquez ensuite sur le bouton « *Scan...* ».


![Image](assets/fr/16.webp)


À côté du nom de votre hardware wallet, cliquez sur « *Import Keystore* ».


![Image](assets/fr/17.webp)


Le deuxième signataire est maintenant correctement enregistré dans Sparrow Wallet.


![Image](assets/fr/18.webp)


Je répète exactement la même procédure avec le Trezor One pour finaliser la configuration du Multisig.


![Image](assets/fr/19.webp)


Dans ma configuration nous ne traitons pas ce cas, mais si vous souhaitez inclure une signature via un software wallet dans Sparrow (hot wallet) au sein de votre Multisig, cliquez simplement sur le bouton « *New or Imported Software Wallet* ».


Maintenant que tous vos appareils de signature sont importés dans Sparrow Wallet, vous pouvez finaliser la création du Multisig en cliquant sur « *Apply* ».


![Image](assets/fr/20.webp)


Choisissez un mot de passe robuste pour sécuriser l'accès à votre portefeuille Sparrow Wallet. Ce mot de passe protège vos clés publiques, adresses, labels et historique de transactions contre tout accès non autorisé.


Pensez à sauvegarder ce mot de passe en lieu sûr, par exemple dans un gestionnaire de mots de passe, pour éviter de le perdre.


![Image](assets/fr/21.webp)


## Sauvegarder un portefeuille Multisig


Nous allons maintenant sauvegarder l'*Output Script Descriptor* sur un support indépendant et en conserver plusieurs copies.


Le *Descriptor* contient tous les xpubs de votre portefeuille Multisig, ainsi que les chemins de dérivation utilisés pour générer les clés. Rappelez-vous ce que nous avons vu dans la première partie : pour restaurer un portefeuille Multisig, vous devez soit disposer de **toutes** les phrases mnémoniques, soit seulement du nombre minimal requis pour atteindre le seuil de signature. Toutefois, dans ce dernier cas, il est également essentiel de disposer des **xpubs** des signataires manquants. Le *Descriptor* contient tous les xpubs de votre Multisig.


Si ce n'est pas clair, retenez simplement ceci : pour récupérer un Multisig, vous avez besoin du nombre minimal de phrases mnémoniques pour chaque Hardware Wallet utilisé, en fonction du seuil (dans mon cas : 2 phrases), ainsi que du *Descriptor*.


Ce *Descriptor* ne contient aucune clé privée, uniquement des clés publiques. Cela signifie qu'il ne donne pas accès aux fonds. Il n'est donc pas aussi critique que les phrases mnémoniques, qui donnent un accès complet à vos bitcoins. Le risque lié au *Descriptor* concerne uniquement la confidentialité : en cas de compromission, un tiers pourrait observer toutes vos transactions, mais ne pourrait pas dépenser vos fonds.


Je vous recommande vivement de créer plusieurs copies de ce *Descriptor*, et de les conserver avec chaque appareil de signature de votre Multisig. Par exemple, dans mon cas, j'imprime le *Descriptor* sur papier et j'en conserve une copie avec le Passport, une autre avec le Trezor, et une avec le Ledger. Je sauvegarde également ce *Descriptor* sous forme de fichier PDF sur trois clés USB, chacune stockée avec l'un des hardware wallets. De cette façon, je maximise mes chances de ne jamais perdre ce *Descriptor*, et je suis sûr d'avoir deux copies (une physique et une numérique) avec chaque appareil.


Une fois votre portefeuille Multisig créé, Sparrow vous fournit automatiquement ce *Descriptor*. Cliquez sur le bouton « *Save PDF...* » pour le sauvegarder à la fois en texte et en QR code.


![Image](assets/fr/22.webp)


Vous pouvez ensuite imprimer ce PDF et le copier sur vos clés USB.


![Image](assets/fr/23.webp)


Le Passport utilise la configuration multisig importée par Sparrow pour afficher et vérifier les informations de clé pertinentes lors du pairing par QR code et du flux de signature. Conservez le *Descriptor* de manière indépendante : il reste essentiel pour récupérer le portefeuille si un signataire est indisponible.


En plus de sauvegarder le *Descriptor*, n'oubliez pas d'accorder une attention particulière à la sauvegarde des phrases mnémoniques de chacun de vos appareils de signature. Si vous débutez, je vous recommande vivement de consulter cet autre tutoriel pour apprendre à les sauvegarder et à les gérer correctement :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Avant de recevoir vos premiers bitcoins sur votre Multisig, **je vous conseille vivement d'effectuer un test de récupération à vide**. Notez quelques informations de référence, telles que la première adresse de réception, puis réinitialisez vos hardware wallets tant que le portefeuille est encore vide. Ensuite, essayez de restaurer votre portefeuille Multisig sur les Hardware Wallets à l'aide de vos sauvegardes papier des phrases mnémoniques, puis sur Sparrow à l'aide du *Descriptor*. Vérifiez que la première adresse générée après la restauration correspond à celle que vous aviez notée à l'origine. Si c'est le cas, vous pouvez être rassuré : vos sauvegardes papier sont fiables.


Pour en savoir plus sur la manière d'effectuer un test de récupération, je vous suggère de consulter cet autre tutoriel :


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Recevoir des bitcoins sur votre Multisig


Votre portefeuille est maintenant prêt à recevoir des bitcoins. Dans Sparrow, cliquez sur l'onglet « *Receive* ».


![Image](assets/fr/30.webp)


Avant d'utiliser l'adresse générée par Sparrow Wallet, prenez le temps de la vérifier directement sur l'écran de vos hardware wallets. Cela garantira que l'adresse n'a pas été altérée, et que vos appareils détiennent les clés privées nécessaires pour dépenser les fonds associés. Cela vous protège contre un certain nombre de vecteurs d'attaque.


Pour ce faire, cliquez sur « *Display Address* » pour afficher l'adresse sur votre Trezor ou votre Ledger, lorsqu'ils sont connectés par câble.


![Image](assets/fr/31.webp)


Avec le Passport, sélectionnez le compte multisig et choisissez « *Verify Address* ». Scannez le QR code de l'adresse de réception affichée par Sparrow. Le Passport confirme sur son écran si l'adresse appartient au portefeuille multisig.


Vérifiez que l'adresse affichée sur chaque hardware wallet correspond exactement à celle de Sparrow Wallet. Il est conseillé de le faire juste avant de partager l'adresse avec le payeur, pour être sûr de son intégrité.


Vous pouvez ensuite attribuer un « *Label* » à cette adresse, pour indiquer l'origine des bitcoins reçus. C'est un bon moyen d'organiser la gestion de vos UTXOs.


![Image](assets/fr/34.webp)


Une fois cette vérification effectuée, vous pouvez utiliser l'adresse pour recevoir des bitcoins.


![Image](assets/fr/35.webp)


## Envoyer des bitcoins avec votre Multisig


Maintenant que vous avez reçu vos premiers sats sur votre portefeuille Multisig, vous pouvez aussi les dépenser ! Dans Sparrow, allez dans l'onglet « *Send* » pour construire une nouvelle transaction.


![Image](assets/fr/36.webp)


Si vous souhaitez utiliser le *Coin Control*, c'est-à-dire sélectionner manuellement les UTXOs que vous souhaitez dépenser, allez dans l'onglet « *UTXOs* ». Choisissez les UTXOs que vous souhaitez dépenser, puis cliquez sur « *Send Selected* ». Vous serez automatiquement redirigé vers l'onglet « *Send* », avec les UTXOs déjà pré-remplis.


![Image](assets/fr/37.webp)


Saisissez l'adresse de destination. Plusieurs adresses peuvent être ajoutées en cliquant sur « *+ Add* ».


![Image](assets/fr/38.webp)


Ajoutez un « *Label* » pour décrire l'objet de cette dépense, afin de faciliter le suivi de vos transactions.


![Image](assets/fr/39.webp)


Saisissez le montant à envoyer à l'adresse sélectionnée.


![Image](assets/fr/40.webp)


Ajustez le taux de frais en fonction des conditions actuelles du réseau. Par exemple, consultez [Mempool.space](https://Mempool.space/) pour choisir un niveau de frais adapté.


Après avoir vérifié tous les paramètres de la transaction, cliquez sur « *Create Transaction* ».


![Image](assets/fr/41.webp)


Si tout vous convient, cliquez sur « *Finalize Transaction for Signing* ».


![Image](assets/fr/42.webp)


En bas de l'écran, vous verrez que Sparrow attend 2 signatures. C'est normal : le portefeuille utilisé ici est un Multisig 2-de-3.


![Image](assets/fr/43.webp)


Je commence à signer avec mon Passport. Dans Sparrow, cliquez sur « *Show QR* » pour afficher la PSBT (*Partially Signed Bitcoin Transaction*) sous forme de QR codes animés. Sur le Passport, sélectionnez le compte multisig et choisissez « *Sign with QR Code* », puis scannez le QR code affiché par Sparrow.


Sur l'écran de votre Hardware Wallet, vérifiez attentivement les paramètres de la transaction : l'adresse du destinataire, le montant envoyé et les frais. Une fois la transaction confirmée, validez pour procéder à la signature.


Après avoir approuvé la transaction, le Passport affiche la PSBT signée sous forme de QR codes animés. Dans Sparrow, cliquez sur « *Scan QR* » et scannez ces codes avec votre webcam. La signature du Passport est alors ajoutée. J'utilise maintenant le Ledger pour la deuxième signature requise : je le connecte et le déverrouille, puis je clique sur « *Sign* » dans Sparrow.


![Image](assets/fr/48.webp)


Cliquez sur « *Sign* » à côté du nom de votre Hardware Wallet.


![Image](assets/fr/49.webp)


La première fois que vous utilisez votre Ledger avec ce Multisig, Sparrow vous demandera de vérifier les clés publiques étendues (xpubs) des cosignataires. Comme avec le Passport, cette étape vous empêche de signer à l'aveugle par la suite. Pour valider ces informations, comparez le xpub affiché sur l'écran du Ledger avec ceux fournis directement par vos autres hardware wallets.


![Image](assets/fr/50.webp)


Vérifiez l'adresse du destinataire, le montant transféré et les frais de transaction, puis signez la transaction.


![Image](assets/fr/51.webp)


Appuyez sur l'écran pour signer.


![Image](assets/fr/52.webp)


Sparrow dispose maintenant des deux signatures nécessaires pour libérer les fonds du portefeuille Multisig. Vérifiez la transaction une dernière fois, et si tout va bien, cliquez sur « *Broadcast Transaction* » pour la diffuser sur le réseau.


![Image](assets/fr/53.webp)


Vous retrouverez cette transaction dans l'onglet « *Transactions* » de Sparrow Wallet.


![Image](assets/fr/54.webp)


Félicitations, vous savez désormais configurer et utiliser un portefeuille multisignature sur Sparrow. Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci du partage !


Pour aller plus loin, je vous recommande de consulter ce tutoriel sur une autre méthode pour renforcer la sécurité de votre portefeuille Bitcoin, la passphrase BIP39 :


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
