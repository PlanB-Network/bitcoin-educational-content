---
name: Trezor Shamir Backup
description: Les phrases mnémoniques Single-share et Multi-share sur Trezor
---
![cover](assets/cover.webp)

*Image credit: [Trezor.io](https://trezor.io/)*

## Les nouvelles options de sauvegarde sur Trezor

Depuis 2023, Trezor propose un nouveau format de sauvegarde appelé ***Single-share Backup***, qui remplace progressivement l’approche classique que l'on retrouve sur la plupart des portefeuilles fondée sur le BIP39. Contrairement aux phrases mnémoniques traditionnelles de 12 ou 24 mots, ce nouveau format repose sur une phrase unique de 20 mots issue d’un standard développé par SatoshiLabs : le **SLIP39**. L’objectif est d’améliorer la robustesse et la lisibilité de la sauvegarde, tout en rendant possible une migration fluide vers un modèle de sauvegarde distribué.

Ce modèle distribué s'appelle le ***Multi-share Backup***. Il repose sur le même principe, mais au lieu de générer une seule phrase mnémonique, il permet de la scinder en plusieurs fragments appelés ***shares***, chacun étant une phrase mnémonique à part entière. Pour restaurer le portefeuille, un certain nombre de ces *shares* (défini par un *seuil*) doivent être réunis. Par exemple, dans un schéma 3-de-5, n’importe quels 3 *shares* sur les 5 existantes permettent de reconstituer le portefeuille. Attention, le système de sauvegarde distribué de Trezor est différent des portefeuilles multisigs. Pour dépenser vos bitcoins, seul votre hardware wallet Trezor est requis. Il ne faut produire qu'une seule signature. La distribution s'applique uniquement au niveau de la phrase mnémonique, c'est-à-dire de la sauvegarde.

![Image](assets/fr/01.webp)

Ce système permet de résoudre le problème du point de défaillance unique de la phrase mnémonique sans les inconvénients liés à la gestion d'un multisig ou d'une passphrase BIP39. Le processus de récupération ne repose plus sur une seule information, mais sur plusieurs, avec en plus une certaine tolérance à la perte grâce au seuil.

Les utilisateurs ayant créé un portefeuille avec un *Single-share Backup* peuvent à tout moment passer à un *Multi-share Backup* sans avoir à migrer leur portefeuille. Les adresses de réception et les comptes resteront identiques. Le système *Multi-share* affecte uniquement la sauvegarde, tandis que le reste du portefeuille demeure inchangé.

Le *Multi-share Backup* est disponible sur les Trezor Model T, Safe 3 et Safe 5. Cette fonctionnalité n'est donc pas prise en charge par le Trezor Model One.

**Remarque importante :** Le système *Multi-share* de Trezor est sûr cryptographiquement, car il utilise le schéma *Shamir's Secret Sharing* pour la distribution. Il est fortement déconseillé d'appliquer un système similaire manuellement en divisant soi-même une phrase mnémonique classique. C'est une mauvaise pratique qui augmente significativement les risques de vol et de perte de vos bitcoins, donc ne le faites pas. Une phrase mnémonique classique se conserve en entier.

## Le Shamir’s Secret Sharing dans le SLIP39

Le mécanisme cryptographique sous-jacent aux sauvegardes *Multi-share* sur les Trezor est le *Shamir’s Secret Sharing Scheme* (SSSS). Son principe est le suivant : une information secrète (ici, la seed du portefeuille) est transformée en un polynôme mathématique. Ensuite, plusieurs points de ce polynôme sont calculés : chacun devient un share. La reconstruction du secret original se fait par interpolation polynomiale, en réunissant un nombre minimal de points (le seuil).

Aucune information sur le secret ne peut être déduite d’un nombre de shares inférieur au seuil, ce qui garantit une sécurité théorique parfaite de l'information secrète. En d’autres termes, même un attaquant disposant d’une puissance de calcul illimitée ne peut pas deviner la seed si le seuil n’est pas atteint.

Le SLIP39 utilise ce schéma pour distribuer la seed du portefeuille. Chaque share est une phrase de 20 mots, construite à partir d’une liste de 1024 mots (différente de la liste du BIP39).

## Mettre en place un Multi-share Backup sur un Trezor

Lors de la création de votre portefeuille sur le Trezor, vous avez trois options différentes :
- Utiliser une phrase mnémonique classique BIP39 de 12 ou 24 mots ;
- Utiliser une phrase mnémonique unique Single-share (SLIP39) ;
- Configurer plusieurs phrases mnémoniques en Multi-share (SLIP39).

Si vous optez pour une phrase mnémonique Single-share SLIP39, vous aurez la possibilité d'évoluer vers un Multi-share plus tard sans avoir à réinitialiser le portefeuille. En revanche, si vous commencez avec un portefeuille classique BIP39 (phrase de 12 ou 24 mots), vous ne pourrez pas le convertir directement en Multi-share. Vous devrez créer un nouveau portefeuille Multi-share de zéro et transférer vos fonds de l'ancien portefeuille au nouveau via une ou plusieurs transactions Bitcoin. Cette opération est plus complexe et coûteuse. Si vous souhaitez faire cette migration, je vous recommande l'achat d'un nouveau hardware wallet Trezor pour éviter de devoir entrer votre seed sur un logiciel de portefeuille.

Dans ce tutoriel, nous allons d'abord voir comment configurer un Multi-share lors de la création du portefeuille, puis, dans une section suivante, nous verrons comment convertir un Single-share en Multi-share sur un portefeuille existant.

Si vous avez besoin d'aide pour la configuration initiale de votre appareil, nous avons également un tutoriel détaillé pour chaque modèle de Trezor :

https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Sur un nouveau portefeuille

Vous avez passé les étapes de configuration initiale de votre Trezor et vous êtes prêt à créer le portefeuille. Dans Trezor Suite, cliquez sur le bouton "*Create new wallet*".

![Image](assets/fr/02.webp)

Choisissez l'option "*Multi-share Backup*", puis cliquez sur "*Create wallet*".

![Image](assets/fr/03.webp)

Acceptez les conditions d'utilisation sur votre Trezor et confirmez la création du portefeuille.

![Image](assets/fr/04.webp)

Dans Trezor Suite, cliquez sur "*Continue to backup*".

![Image](assets/fr/05.webp)

Lisez attentivement les instructions, validez-les, puis cliquez sur "*Create wallet backup*".

![Image](assets/fr/06.webp)

Pour plus d'informations sur la manière adéquate de sauvegarder et de gérer vos phrases mnémoniques, je vous recommande vivement de suivre cet autre tutoriel, particulièrement si vous êtes débutant :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Sur le Trezor, choisissez le nombre total de shares que vous souhaitez configurer. Les configurations les plus courantes sont 2-de-3 et 3-de-5. Pour cet exemple, je vais créer un 2-de-3, donc je sélectionne 3 shares. Chaque share représentera une phrase mnémonique de 20 mots.

*Pour les utilisateurs du Safe 5, bien que l'écran indique "*Tap to continue*", vous devrez en réalité faire un swipe vers le haut pour confirmer.*

![Image](assets/fr/07.webp)

Confirmez ensuite le seuil, c'est-à-dire le nombre de shares nécessaires pour récupérer l'accès au portefeuille et aux bitcoins qu'il contient.

![Image](assets/fr/08.webp)

Le Trezor va créer vos différentes shares (phrases mnémoniques) en utilisant son générateur de nombres aléatoires. Assurez-vous de ne pas être observé durant cette opération. Notez les mots fournis sur l'écran sur le support physique de votre choix. Il est important de conserver les mots numérotés et dans l'ordre séquentiel.

Je vous recommande de noter chaque share sur un support distinct et de gérer soigneusement leur stockage afin d'éviter que plusieurs ne soient accessibles au même endroit. Par exemple, pour une configuration 2-de-3 comme la mienne, une option serait de conserver une share chez moi, une autre chez un ami de confiance, et la dernière dans un coffre de banque. Le choix des emplacements de stockage va dépendre de votre stratégie personnelle de sécurisation.

Vous pouvez voir sur le haut de l'écran quelle share vous êtes en train de consulter.

_**Évidemment, vous ne devez jamais partager ces mots sur internet, contrairement à ce que je fais dans ce tutoriel. Ce portefeuille en exemple sera utilisé uniquement sur le Testnet et sera supprimé à l'issue du tutoriel.**_

![Image](assets/fr/09.webp)

Pour passer aux mots suivants, cliquez sur le bas de l'écran. Vous pouvez revenir en arrière en glissant vers le bas. Une fois tous les mots notés, restez appuyé sur l'écran pour passer à la share suivante, et répétez cette opération.

![Image](assets/fr/10.webp)

À la fin de l'enregistrement de chaque share, on vous demandera de sélectionner les mots de votre phrase mnémonique dans l'ordre pour confirmer que vous les avez correctement notés.

![Image](assets/fr/11.webp)

Et voilà, vous avez réussi à sauvegarder votre portefeuille en utilisant l'option Multi-share. Vous pouvez maintenant poursuivre avec le reste des instructions de configuration.

### Sur un portefeuille Single-share existant

Si vous disposez déjà d'un portefeuille Trezor avec une sauvegarde Single-share (une phrase mnémonique SLIP39, et non une phrase classique BIP39), et que vous souhaitez améliorer la disponibilité et la sécurité de la sauvegarde de votre portefeuille, vous pouvez établir un système Multi-share sans avoir à transférer vos bitcoins.

Pour ce faire, connectez et déverrouillez votre hardware wallet. Dans Trezor Suite, accédez aux paramètres.

![Image](assets/fr/12.webp)

Allez dans l'onglet "*Device*".

![Image](assets/fr/13.webp)

Cliquez ensuite sur "*Create Multi-share Backup*".

![Image](assets/fr/14.webp)

Lisez les instructions, puis cliquez sur "*Create Multi-share Backup*".

![Image](assets/fr/15.webp)

Vous devrez ensuite saisir votre phrase mnémonique actuelle (en Single-share) sur l'écran de votre Trezor. Sélectionnez le nombre de mots (par défaut, c'est 20).

![Image](assets/fr/16.webp)

Utilisez ensuite le clavier sur l'écran de la Trezor pour entrer chaque mot de votre phrase mnémonique actuelle.

![Image](assets/fr/17.webp)

Vous pourrez alors choisir la configuration de votre Multi-share Backup en suivant les instructions fournies dans la section précédente.

![Image](assets/fr/18.webp)

Une fois votre Multi-share Backup créé, vous devrez décider de ce que vous faites de votre phrase mnémonique Single-share initiale. Comme le portefeuille Bitcoin reste le même, cette phrase unique permet toujours d'y accéder. Cela va dépendre de votre stratégie de sécurisation, mais en général, il est conseillé de détruire cette phrase pour éliminer ce point de défaillance unique, ce qui est justement l'objectif du Multi-share Backup. Si vous décidez de la détruire, assurez-vous de le faire de manière sécurisée, car **elle donne toujours accès à vos bitcoins**.

Félicitations, vous êtes maintenant au point sur l'utilisation des Single-share et Multi-share Backups sur les hardware wallets Trezor. Pour aller plus loin dans la sécurisation de votre portefeuille, je vous conseille de découvrir ce tutoriel sur les passphrases BIP39 :

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Si vous avez trouvé ce tutoriel utile, je vous serais reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager cet article sur vos réseaux sociaux. Merci beaucoup !

## Ressources supplémentaires

- [SLIP-0039 : Shamir's Secret-Sharing for Mnemonic Codes](https://github.com/satoshilabs/slips/blob/master/slip-0039.md) ;
- [Multi-share Backup on Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor) ;
- [Wikipedia : Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).
