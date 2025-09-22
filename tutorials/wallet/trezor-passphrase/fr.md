---
name: BIP-39 Passphrase Trezor
description: Comment ajouter une passphrase sur son portefeuille Trezor ?
---
![cover](assets/cover.webp)

Une passphrase BIP39 est un mot de passe optionnel qui, combiné à la phrase mnémonique, offre une couche de sécurité supplémentaire pour les portefeuilles Bitcoin déterministes et hiérarchiques. Dans ce tutoriel, nous allons découvrir ensemble comment mettre en place une passphrase sur votre portefeuille Bitcoin sécurisé sur un Trezor (Safe 3, Safe 5 et Model One).

![Image](assets/fr/01.webp)

Avant de commencer ce tutoriel, si vous n'êtes pas familier avec le concept de passphrase, son fonctionnement et ses implications pour votre portefeuille Bitcoin, je vous recommande fortement de consulter cet autre article théorique où je vous explique tout (c'est très important, car utiliser une passphrase sans en comprendre pleinement le fonctionnement peut mettre en danger vos bitcoins) :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

La passphrase sur Trezor est gérée de manière classique si vous avez opté pour le standard BIP39 lors de la configuration (ce que je vous recommande si vous n'avez pas besoin du *Multi-share Backup*). La particularité sur les Trezor est que vous pouvez soit entrer la passphrase directement sur le hardware wallet, soit via le clavier de votre ordinateur en utilisant le logiciel Trezor Suite. Cette seconde option est nettement moins sécurisée, car l'ordinateur dispose d'une surface d'attaque immensément plus grande que le hardware wallet. Toutefois, saisir une passphrase complexe peut être plus rapide sur un clavier classique que sur celui du hardware wallet, ce qui pourrait encourager l'utilisation de passphrases fortes. Aussi, il vaut toujours mieux utiliser une passphrase, même si elle doit être saisie au clavier, que de ne pas en utiliser du tout. Il est cependant important de rester conscient du risque accru d'attaques numériques que cela implique.

Ces options ne sont pas disponibles sur tous les logiciels de gestion de portefeuille compatibles avec les appareils de Trezor. Par exemple, pour le Model One, la passphrase peut être saisie via le clavier sur Sparrow Wallet. Pour les modèles Model T, Safe 3 et Safe 5, vous devez soit utiliser Trezor Suite, soit entrer la passphrase directement sur le hardware wallet, car l'option de saisie via Sparrow a été désactivée par HWI il y a quelques années.

![Image](assets/fr/02.webp)

Dans Trezor Suite, vous disposez de deux méthodes différentes pour gérer la demande de passphrase. Vous pouvez activer l'option "*Passphrase*" dans l'onglet "*Device*". Si activée, Trezor Suite et tous les autres logiciels de gestion de portefeuille vous demanderont systématiquement de saisir votre passphrase à chaque démarrage. Si vous préférez une approche plus discrète quant à l'utilisation d'une passphrase, vous pouvez conserver le réglage sur "*Standard*". Dans ce cas, vous devrez accéder manuellement au menu de votre hardware wallet en haut à gauche et cliquer sur le bouton "*+ Passphrase*" à chaque démarrage de celui-ci.

Avant de commencer ce tutoriel, assurez-vous d'avoir déjà initialisé votre Trezor et généré votre phrase mnémonique. Si ce n'est pas le cas et que votre Trezor est neuf, suivez le tutoriel spécifique à votre modèle disponible sur Plan ₿ Network. Une fois cette étape complétée, vous pourrez revenir à ce tutoriel.

https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Ajouter une passphrase sur un Safe 3 ou Safe 5

Après avoir créé votre portefeuille, enregistré votre sauvegarde de la phrase mnémonique et paramétré un code PIN, vous accéderez au menu d'accueil de Trezor Suite. En haut à gauche, une fenêtre devrait apparaître vous invitant à activer la passphrase BIP39.

![Image](assets/fr/03.webp)

Si cette fenêtre ne s'affiche pas, vous devrez activer manuellement l'option "*Passphrase*" dans l'onglet "*Device*" des paramètres.

![Image](assets/fr/04.webp)

On vous demande dans cette fenêtre de renseigner votre passphrase. Choisissez une passphrase forte et procédez immédiatement à une sauvegarde physique, sur un support tel que du papier ou du métal. Dans cet exemple, j'ai choisi la passphrase : `fH3&kL@9mP#2sD5qR!82`. C'est un exemple ; cependant, je vous recommande de choisir une passphrase légèrement plus longue. Entre 30 et 40 caractères serait idéal (comme un bon mot de passe).

_**Évidemment, vous ne devez jamais partager votre passphrase sur internet, contrairement à ce que je fais dans ce tutoriel. Ce portefeuille en exemple sera utilisé uniquement sur le Testnet et sera supprimé à l'issue du tutoriel.**_

Pour des recommandations plus précises sur le choix de votre passphrase, je vous invite encore une fois à consulter cet autre article :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Si vous voulez saisir votre passphrase via le clavier de votre ordinateur, entrez-la dans le champ prévu à cet effet puis cliquez sur "*Access Passphrase wallet*".

![Image](assets/fr/05.webp)

Votre hardware wallet affichera alors votre passphrase. Assurez-vous qu'elle correspond à votre sauvegarde physique (papier ou métal) avant de cliquer sur l'écran pour continuer.

![Image](assets/fr/06.webp)

Vous accéderez ainsi à votre portefeuille protégé par passphrase.

![Image](assets/fr/07.webp)

Si vous préférez renforcer la sécurité en saisissant votre passphrase uniquement sur votre Trezor, lorsqu'on vous demandera de la renseigner, cliquez sur "*Enter passphrase on Trezor*".

![Image](assets/fr/08.webp)

Un clavier T9 s'affichera sur votre Trezor pour vous permettre de saisir votre passphrase. Une fois la saisie terminée, cliquez sur la coche verte pour appliquer la passphrase à votre portefeuille.

![Image](assets/fr/09.webp)

Vous accéderez alors à votre portefeuille sécurisé par passphrase.

![Image](assets/fr/10.webp)

Pour utiliser Sparrow Wallet, la procédure est similaire, mais pour les modèles T, Safe 3 et Safe 5, la passphrase doit obligatoirement être saisie sur le hardware wallet et non via le clavier de l'ordinateur.

Chaque fois que Sparrow Wallet nécessitera l'accès à votre Trezor et que la passphrase n'aura pas encore été appliquée depuis le dernier démarrage, vous devrez la renseigner à l'aide du clavier T9.

![Image](assets/fr/11.webp)

## Ajouter une passphrase sur un Model One

Sur le Model One, l'utilisation d'une passphrase BIP39 est presque indispensable. Étant donné que cet appareil n'intègre pas de Secure Element, il est relativement facile d'en extraire des informations sensibles. Il n'est donc pas résistant aux attaques physiques. Cependant, comme la passphrase n'est pas conservée sur l'appareil après son extinction, l'utilisation d'une passphrase forte (non brute-forçable) peut vous prémunir contre la plupart des attaques physiques connues sur ce modèle.

Sur le Model One, il n'est pas possible de saisir la passphrase directement sur le hardware wallet. Vous devrez donc la renseigner via le clavier de votre ordinateur.

Après avoir créé votre portefeuille, enregistré votre sauvegarde de la phrase mnémonique et paramétré un code PIN, vous accéderez au menu d'accueil de Trezor Suite. En haut à gauche, une fenêtre vous invitant à activer la passphrase BIP39 devrait apparaître.

![Image](assets/fr/12.webp)

Si cette fenêtre ne s'affiche pas, vous devez activer l'option "*Passphrase*" dans l'onglet "*Device*" des paramètres.

![Image](assets/fr/13.webp)

On vous demande dans cette fenêtre de renseigner votre passphrase. Choisissez une passphrase forte et procédez immédiatement à une sauvegarde physique, sur un support tel que du papier ou du métal. Dans cet exemple, j'ai choisi la passphrase : `fH3&kL@9mP#2sD5qR!82`. C'est un exemple ; cependant, je vous recommande de choisir une passphrase légèrement plus longue. Entre 30 et 40 caractères serait idéal (comme un bon mot de passe).

Pour des recommandations plus précises sur le choix de votre passphrase, je vous invite encore une fois à consulter cet autre article :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Renseignez votre passphrase dans le champ prévu à cet effet puis cliquez sur le bouton "*Access Passphrase wallet*".

![Image](assets/fr/14.webp)

Votre hardware wallet affichera votre passphrase. Assurez-vous qu'elle correspond à votre sauvegarde physique (papier ou métal), puis cliquez sur le bouton de droite pour continuer.

![Image](assets/fr/15.webp)

Vous accéderez alors à votre portefeuille protégé par passphrase.

![Image](assets/fr/16.webp)

Pour utiliser Sparrow Wallet par la suite, la procédure reste identique. À chaque fois que Sparrow nécessitera l'accès à votre hardware wallet et que la passphrase n'a pas été saisie depuis le dernier démarrage de l'appareil, vous devrez la renseigner.

![Image](assets/fr/17.webp)

Félicitations, vous êtes maintenant au point sur l'utilisation de la passphrase BIP39 sur les hardware wallets Trezor. Pour aller plus loin dans la sécurisation de votre portefeuille, je vous conseille de découvrir ce tutoriel sur les systèmes de sauvegardes *Multi-share* de Trezor (*Shamir’s Secret Sharing Scheme*) :

https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci beaucoup !