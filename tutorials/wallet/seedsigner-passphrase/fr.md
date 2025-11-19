---
name: BIP-39 Passphrase SeedSigner
description: Comment ajouter une passphrase sur son portefeuille SeedSigner ?
---

![cover](assets/cover.webp)

Une passphrase BIP39 est un mot de passe optionnel qui, combiné à la phrase mnémonique, offre une couche de sécurité supplémentaire pour les portefeuilles Bitcoin déterministes et hiérarchiques. Dans ce tutoriel, nous allons découvrir ensemble comment mettre en place une passphrase sur votre portefeuille Bitcoin utilisé avec un SeedSigner.

![Image](assets/fr/01.webp)

## Prérequis avant d'ajouter une Passphrase

Avant de commencer ce tutoriel, si vous n'êtes pas familier avec le concept de passphrase, son fonctionnement et ses implications pour votre portefeuille Bitcoin, je vous recommande fortement de consulter cet autre article théorique où je vous explique tout (c'est très important, car utiliser une passphrase sans en comprendre pleinement le fonctionnement peut mettre en danger vos bitcoins) :

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Avant de commencer ce tutoriel, assurez-vous également d'avoir déjà initialisé votre SeedSigner et généré votre phrase mnémonique. Si ce n'est pas le cas et que votre SeedSigner est neuf, suivez le tutoriel sur Plan ₿ Academy. Une fois cette étape complétée, vous pourrez revenir à ce tutoriel :

https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Comment ajouter une passphrase sur le SeedSigner ?

L’ajout d’une passphrase à votre portefeuille géré via le SeedSigner crée un tout nouveau portefeuille, générant ainsi un ensemble de clés entièrement distinct. Par conséquent, si vous possédez déjà un portefeuille contenant des sats, vous ne pourrez plus y accéder avec la passphrase, puisque celle-ci génère un portefeuille complètement différent.

Pour appliquer une passphrase sur votre SeedSigner, allumez l’appareil et scannez votre SeedQR comme à votre habitude. Le SeedSigner affichera alors l’empreinte de votre portefeuille actuel, correspondant à celui **sans passphrase**. Le portefeuille avec passphrase possédera, quant à lui, une empreinte différente.

Cliquez sur le bouton `BIP-39 Passphrase`.

![Image](assets/fr/02.webp)

Saisissez ensuite la passphrase de votre choix dans le champ prévu à cet effet à l’aide du clavier à l’écran. Assurez-vous d’en faire une ou plusieurs sauvegardes physiques (papier ou métal) : la perte de cette passphrase entraînerait la perte définitive de l’accès à vos bitcoins. **Pour restaurer un portefeuille, la phrase mnémonique et la passphrase sont toutes deux indispensables.** Si l’une d’elles est perdue, vos bitcoins seront irrémédiablement bloqués.

Une fois la saisie terminée, validez en appuyant sur le bouton `KEY3` situé en bas à droite du SeedSigner.

![Image](assets/fr/03.webp)

*Dans cet exemple, j’ai utilisé la passphrase `pba`. Cependant, dans votre cas, veillez à choisir une passphrase robuste. Pour savoir comment définir une passphrase optimale, je vous invite à consulter cet autre article :*

https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Le SeedSigner vous affiche ensuite la nouvelle empreinte de votre portefeuille associé à la passphrase. Faites plusieurs copies de cette empreinte : elle est importante lorsque vous utilisez un portefeuille avec passphrase, car elle vous permet de vérifier, à chaque saisie de la passphrase, que vous n’avez commis aucune erreur de frappe et que vous accédez bien au bon portefeuille.

Par exemple, si dans mon cas je note par erreur la passphrase `Pba` lors d'un démarrage du SeedSigner au lieu de `pba`, ce simple changement d’une minuscule en majuscule entraînera la création d’un portefeuille entièrement différent de celui auquel je souhaite accéder.

Cette empreinte ne présente aucun risque pour la sécurité ni pour la confidentialité de votre portefeuille. Elle ne divulgue aucune information, qu’elle soit publique ou privée, sur vos clés. Contrairement à la phrase mnémonique et à la passphrase, vous pouvez donc sauvegarder l'empreinte sur un support numérique. Je vous recommande d’en conserver une copie à plusieurs endroits : sur un papier, dans un gestionnaire de mots de passe, etc.

Une fois l’empreinte sauvegardée, cliquez sur `Done`.

![Image](assets/fr/04.webp)

Vous accédez alors à toutes les fonctionnalités de votre portefeuille, comme sur un SeedSigner classique.

![Image](assets/fr/05.webp)

Vous pouvez désormais importer le keystore dans Sparrow Wallet et utiliser votre portefeuille normalement. À chaque redémarrage, il faudra à la fois scanner votre SeedQR et ressaisir votre passphrase à l’aide du clavier, comme nous l'avons fait ici.

Avant d’utiliser réellement votre portefeuille avec passphrase, je vous recommande vivement d’effectuer un test de récupération à vide complet. Cela vous permettra de confirmer que vos sauvegardes de la phrase mnémonique et de la passphrase sont valides. Pour apprendre à réaliser cette vérification, consultez le tutoriel suivant :

https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
