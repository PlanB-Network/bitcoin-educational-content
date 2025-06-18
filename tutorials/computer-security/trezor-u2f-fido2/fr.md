---
name: Trezor U2F & FIDO2
description: Renforcer sa sécurité en ligne avec Trezor
---
![cover](assets/cover.webp)

Les dispositifs Trezor sont des hardware wallets initialement conçu pour sécuriser un portefeuille Bitcoin, mais ils disposent également d'options avancées pour réaliser de l'authentification forte sur le web. Grâce à leur compatibilité avec les protocoles **U2F** et **FIDO2**, ils permettent de sécuriser l’accès à vos comptes en ligne sans dépendre uniquement de mots de passe.

Le protocole U2F (*Universal 2nd Factor*) a été introduit par Google et Yubico en 2014, puis standardisé par le FIDO Alliance. Il permet d’ajouter un second facteur d’authentification physique (2FA) lors d’une connexion. Une fois activé, en plus du mot de passe classique, l’utilisateur doit approuver chaque tentative de connexion à son compte en pressant un bouton sur son Trezor. Dans ce contexte, le Trezor fonctionne de manière similaire à une Yubikey.

Cette méthode repose sur la cryptographie asymétrique : aucune donnée secrète n’est transmise, ce qui rend les attaques par hameçonnage ou interception inefficaces. U2F est aujourd’hui pris en charge par de nombreux services en ligne.

En plus de U2F qui permet de faire de l'authentification à deux facteurs, les Trezor prennent également en charge FIDO2 (*Fast IDentity Online 2.0*), une évolution de U2F. C'est un protocole d'authentification standardisé à partir de 2018, qui étend la logique d'U2F et vise à remplacer complètement les mots de passe. Il repose sur deux composants : *WebAuthn* (côté navigateur) et *CTAP2* (côté clé physique). FIDO2 permet une authentification dite "*passwordless*" : l’utilisateur s’identifie uniquement via son dispositif Trezor, qui agit comme un jeton cryptographique unique, sans mot de passe additionnel. Ce protocole est aujourd’hui compatible avec certains services en ligne, en particulier ceux orientés entreprise.

En plus de la fonctionnalité "*passwordless*", FIDO2 permet également de réaliser une authentification à deux facteurs de manière similaire à U2F.

FIDO2 introduit également la notion de credentials résidents, c’est-à-dire des identifiants stockés directement dans le Trezor, qui incluent à la fois la clé privée permettant la connexion et les informations d’identification de l’utilisateur. Ce mécanisme permet une authentification véritablement sans mot de passe : il suffit de brancher son Trezor et de confirmer l’accès, sans saisir ni identifiant ni mot de passe. À l’inverse, les credentials non-résidents, plus classiques, n’enregistrent dans l’appareil que la clé privée ; l’identifiant utilisateur reste stocké côté serveur, et doit donc être saisi à chaque connexion. Nous verrons plus loin comment les sauvegarder avec votre Trezor.

Dans ce tutoriel nous allons découvrir comment activer U2F ou FIDO2 pour l’authentification à deux facteurs, puis comment configurer FIDO2 pour accéder à vos comptes sans mot de passe, directement avec votre Trezor.

**Remarque :** U2F est compatible avec tous les modèles de Trezor, mais FIDO2 n'est pris en charge que sur les Safe 3, Safe 5, et Model T, et non sur le Model One.

## Utiliser U2F/FIDO2 pour du 2FA sur un Trezor

Avant de commencer, assurez-vous d'avoir configuré votre portefeuille Bitcoin sur votre Trezor. Il est important de sauvegarder correctement votre phrase mnémonique, car les clés utilisées pour U2F et FIDO2 en authentification à deux facteurs sont dérivées de cette phrase. En cas de perte ou de dommage de votre Trezor, vous pourrez récupérer l'accès à vos clés en saisissant votre phrase mnémonique sur un autre appareil Trezor (attention, pour les identifiants FIDO2 en mode "*passwordless*", la seed seule ne suffit pas, comme nous le verrons dans les prochaines parties).

Branchez votre Trezor à votre ordinateur et déverrouillez-le.

![Image](assets/fr/01.webp)

Accédez au compte que vous souhaitez sécuriser avec une authentification à deux facteurs. Par exemple, je vais utiliser un compte Bitwarden. Vous trouverez généralement l'option du 2FA dans les paramètres du service, sous les onglets "*authentification*", "*sécurité*", "*connexion*" ou bien "*mot de passe*".

![Image](assets/fr/02.webp)

Dans la section dédiée à l'authentification à deux facteurs, sélectionnez l'option "*Passkey*" (le terme peut varier selon le site que vous utilisez).

![Image](assets/fr/03.webp)

Il vous sera souvent demandé de confirmer votre mot de passe actuel.

![Image](assets/fr/04.webp)

Donnez un nom à votre clé de sécurité pour pouvoir la reconnaître facilement, puis cliquez sur "*Read Key*".

![Image](assets/fr/05.webp)

Les détails de votre compte apparaîtront sur l'écran du Trezor. Touchez l'écran ou appuyez sur le bouton pour confirmer. On vous demandera aussi de confirmer votre code PIN.

![Image](assets/fr/06.webp)

Enregistrez cette clé de sécurité.

![Image](assets/fr/07.webp)

Désormais, lorsque vous voudrez vous connecter à votre compte, en plus de votre mot de passe habituel, on vous demandera de connecter votre Trezor.

![Image](assets/fr/08.webp)

Vous pourrez alors appuyer sur l'écran de votre Trezor pour valider l'authentification.

![Image](assets/fr/09.webp)

L'utilisation d'un hardware wallet Trezor pour l'authentification à deux facteurs présente l'avantage de pouvoir récupérer facilement vos clés grâce à la phrase mnémonique. En plus de cette sauvegarde de base, vous pouvez aussi utiliser un code d'urgence fourni par chaque service où vous avez activé le 2FA. Ce code d'urgence vous permet de vous connecter à votre compte en cas de perte de votre clé de sécurité. Il remplace donc le 2FA pour une connexion si nécessaire.

Par exemple, sur Bitwarden, vous pouvez accéder à ce code en cliquant sur "*View recovery code*".

![Image](assets/fr/10.webp)

Je vous recommande de conserver ce code dans un endroit différent de celui où vous stockez votre mot de passe principal, afin d'éviter qu'ils ne soient volés ensemble. Par exemple, si votre mot de passe est sauvegardé dans un gestionnaire de mots de passe, gardez votre code d'urgence du 2FA sur papier, séparément.

Cette approche vous offre deux niveaux de sauvegarde en cas de perte de votre Trezor pour l'authentification 2FA : une première sauvegarde grâce à la phrase mnémonique pour tous vos comptes et une seconde spécifique à chaque compte avec les codes d'urgence. Toutefois, il est important de **ne pas confondre le rôle de la phrase mnémonique et celui du code d'urgence** :
- La phrase mnémonique de 12 ou 24 mots vous donne accès non seulement aux clés utilisées pour le 2FA sur tous vos comptes, mais aussi à vos bitcoins sécurisés avec votre Trezor ;
- Le code d'urgence vous permet de contourner temporairement la demande de 2FA uniquement sur le compte concerné (dans cet exemple, uniquement sur Bitwarden).

## Utiliser FIDO2 sur un Trezor

En plus de l'authentification à deux facteurs, FIDO2 permet également de réaliser une authentification "*passwordless*", c'est-à-dire sans avoir à saisir de mot de passe lors de la connexion à un site. Il suffit de connecter votre Trezor à votre ordinateur pour accéder à votre compte sécurisé de cette manière. Voici comment configurer cette fonctionnalité.

Avant de commencer, assurez-vous d'avoir configuré votre portefeuille Bitcoin sur votre Trezor. Il est important de bien sauvegarder la phrase mnémonique, car les identifiant FIDO2 "*passwordless*" sont chiffrés avec votre seed (nous découvrirons dans la prochaine partie comment effectuer correctement une sauvegarde de ces identifiants).

Connectez le Trezor à votre ordinateur et déverrouillez-le.

![Image](assets/fr/01.webp)

Accédez au compte que vous souhaitez sécuriser en mode "*passwordless*". Je vais utiliser un compte Bitwarden comme exemple. Cette option se trouve généralement dans les paramètres du service, souvent sous un onglet "*authentification*", "*sécurité*" ou "*mot de passe*".

Sur Bitwarden, par exemple, l'option se trouve sous l'onglet "*Master password*". Cliquez sur "*Turn on*" pour activer l'authentification via FIDO2.

![Image](assets/fr/11.webp)

Il vous sera souvent demandé de confirmer votre mot de passe.

![Image](assets/fr/12.webp)

Les détails de votre compte apparaîtront sur l'écran du Trezor. Touchez l'écran ou appuyez sur le bouton pour confirmer. Vous devrez également confirmer votre code PIN.

![Image](assets/fr/13.webp)

Sur le site, ajoutez un nom pour vous souvenir de votre clé de sécurité, puis cliquez sur "*Turn on*".

![Image](assets/fr/14.webp)

Vous serez ensuite invité à vous identifier pour vérifier le bon fonctionnement de la clé.

![Image](assets/fr/15.webp)

Désormais, lors de la connexion à votre compte, il ne sera plus nécessaire de renseigner votre adresse email ou votre identifiant. Cliquez simplement sur le bouton pour vous authentifier avec une clé physique sur le formulaire de connexion.

![Image](assets/fr/16.webp)

Confirmez la connexion sur votre Trezor en renseignant le PIN de votre hardware wallet.

![Image](assets/fr/17.webp)

Vous serez connecté à votre compte sans avoir besoin de saisir votre mot de passe.

![Image](assets/fr/18.webp)

**Attention, même si vous activez l'authentification "*passwordless*" via FIDO2 sur votre Trezor, le mot de passe principal de votre compte en ligne reste toujours valide pour la connexion.**

## Sauvegarder ses identifiants FIDO2 (credentials residents)

Si vous utilisez FIDO2 ou U2F pour l'authentification à deux facteurs, c'est-à-dire pour vous connecter à des comptes qui requièrent un mot de passe en plus de la validation 2FA via votre Trezor, alors la phrase mnémonique seule permettra de retrouver l'accès à vos clés. Toutefois, si vous utilisez FIDO2 en mode "*passwordless*" comme décrit dans la partie précédente, il sera nécessaire de faire une copie de vos identifiants FIDO en plus de la sauvegarde de votre phrase mnémonique qui chiffre ces identifiants.

Pour cela, vous aurez besoin d'un ordinateur avec Python installé. Ouvrez un terminal et exécutez la commande suivante pour installer le logiciel Trezor nécessaire :

```shell
pip3 install --upgrade trezor
```

Connectez votre Trezor à l'ordinateur via USB et déverrouillez-le à l'aide de votre code PIN.

![Image](assets/fr/01.webp)

Pour récupérer la liste des identifiants FIDO2 enregistrés sur le Trezor, exécutez la commande suivante :

```shell
trezorctl fido credentials list
```

Confirmez l'exportation sur votre Trezor.

![Image](assets/fr/19.webp)

Les informations de vos identifiants FIDO2 s'afficheront dans votre terminal. Par exemple, pour mon compte Bitwarden, j'ai obtenu ces informations :

```shell
WebAuthn credential at index 0:
  Relying party ID:       vault.bitwarden.com
  Relying party name:     Bitwarden
  User ID:                6e315ebabc8b6945a253b1c50116538d
  User name:              tutoplanbnetwork@proton.me
  User display name:      PBN
  Creation time:          2
  hmac-secret enabled:    True
  Use signature counter:  True
  Algorithm:              ES256 (ECDSA w/ SHA-256)
  Curve:                  P-256 (secp256r1)
  Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```

Copiez et enregistrez toutes ces informations dans un fichier texte. Il n'y a pas de risque significatif associé à cette sauvegarde, à part révéler que vous utilisez ces services avec FIDO2. Le "*Credential ID*" est chiffré en utilisant la seed de votre portefeuille, ce qui signifie qu'un attaquant qui obtiendrait cette sauvegarde ne pourrait pas se connecter à vos comptes, mais seulement constater que vous utilisez ces comptes. Pour déchiffrer ces identifiants, il faut avoir la seed de votre portefeuille.

Vous pouvez donc créer plusieurs copies de ce fichier texte, et les conserver en différents lieux, par exemple en local sur votre ordinateur, sur un service d'hébergement de fichiers et sur un support externe comme une clé USB. Cependant, gardez à l'esprit que cette sauvegarde n'est pas mise à jour automatiquement, vous devrez donc la renouveler à chaque fois que vous configurez une nouvelle connexion "*passwordless*" avec votre Trezor.

Imaginons maintenant que vous ayez cassé votre Trezor. Pour récupérer vos identifiants FIDO2, vous devrez d'abord récupérer votre portefeuille à l'aide de votre phrase mnémonique sur un nouveau appareil Trezor compatible FIDO2.

Une fois la récupération effectuée, pour importer vos identifiants FIDO2 sur le nouvel appareil, exécutez la commande suivante dans votre terminal :

```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```

Remplacez simplement `<CREDENTIAL_ID>` par l'un de vos identifiants. Par exemple, dans mon cas, cela donnerait :

```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```

Votre Trezor vous propose d'importer votre identifiant FIDO2. Confirmez en appuyant sur l'écran.

![Image](assets/fr/20.webp)

Votre identifiant FIDO2 est désormais opérationnel sur votre Trezor. Répétez cette procédure pour chacun de vos identifiants.

Félicitations, vous êtes maintenant au point sur l'utilisation de votre Trezor avec U2F et FIDO2 ! Si vous avez trouvé ce tutoriel utile, je vous serais très reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager ce tutoriel sur vos réseaux sociaux. Merci beaucoup !

Je vous conseille également de découvrir cet autre tutoriel dans lequel nous abordons une autre solution pour l'authentification U2F et FIDO2 :

https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e
