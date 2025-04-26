---
name: Threema
description: Messagerie instantanée sûre et anonyme
---
![cover](assets/cover.webp)

Fondée en 2012 en Suisse, Threema est une application de messagerie instantanée pensée pour garantir confidentialité et sécurité. Contrairement à WhatsApp, Telegram ou Signal, Threema ne nécessite ni numéro de téléphone, ni adresse e-mail pour créer un compte. Chaque utilisateur dispose d'un identifiant unique qui permet une inscription totalement anonyme.

Côté technique, les communications sur Threema sont chiffrées de bout en bout. Le code des applications mobiles est open source depuis 2020, mais l’infrastructure serveur reste propriétaire et centralisée. Les serveurs sont hébergés exclusivement en Suisse (un pays réputé pour son cadre juridique en matière de protection des données).

![Image](assets/fr/01.webp)

Threema dispose de clients de base pour Android et iOS. Il existe également une application web, ainsi qu’un logiciel disponible pour Windows, Linux et macOS. Cependant, l’inscription doit obligatoirement être réalisée au préalable sur un appareil mobile pour pouvoir les utiliser.

L’application Threema n'est pas gratuite. Elle fonctionne sur un modèle d’achat unique : 5.99€ pour utiliser l'application à vie (ou 4.99€ si vous l'achetez en direct). Pour utiliser réellement Threema de manière anonyme, il est nécessaire que le paiement le soit également. C’est pourquoi vous pouvez acheter une clé d’activation en bitcoins ou en cash sur le "*Threema Shop*" afin d’activer la version Android. Sur iOS, en revanche, l’achat doit obligatoirement passer par l’App Store, en raison des restrictions imposées par Apple sur la monétisation des applications.

Il existe également une version dédiée aux entreprises nommée "*Threema Work*". Dans ce tutoriel, nous allons nous concentrer sur la version destinée aux particuliers.

| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| **Threema**          | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Chiffrement de bout en bout.*

## Installer l'application Threema

Threema est disponible sur toutes les plateformes. Vous pouvez télécharger l’application directement depuis la boutique d’applications de votre téléphone :
- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app) ;
- [F-Droid](https://f-droid.org/en/packages/ch.threema.app.libre/) ;
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829) ;
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).

Sur Android, il est également possible de [l’installer via l’APK](https://shop.threema.ch/en/download).

Il existe également [des versions pour ordinateur](https://threema.ch/download) (MacOS, Linux et Windows). Nous verrons dans ce tutoriel comment les synchroniser.

## Acheter la licence Threema

Après avoir installé l’application, si vous êtes passé directement par un magasin d’applications, vous avez déjà réglé la licence et devriez y avoir immédiatement accès. Si vous êtes passé par F-Droid ou via l’APK, vous devez maintenant acheter une licence sur le site officiel.

[Rendez-vous sur le "*Threema Shop*"](https://shop.threema.ch/) et cliquez sur le bouton "*Buy Threema for Android*".

![Image](assets/fr/02.webp)

Sélectionnez le nombre de licences souhaité (une seule si c’est uniquement pour vous), choisissez la devise, ainsi que le mode de livraison de la licence. Vous pouvez opter pour une réception par email ou directement sur le site si vous souhaitez préserver votre anonymat. Cliquez ensuite sur "*Proceed to payment*".

![Image](assets/fr/03.webp)

Choisissez votre méthode de paiement. Dans mon cas, je vais payer en bitcoins, ce que je vous recommande également de faire, car cela permet de conserver l’anonymat (à condition d’utiliser Bitcoin de manière adéquate) et reste bien plus pratique qu’un paiement en espèces à distance. Cliquez ensuite sur "*Next*".

![Image](assets/fr/04.webp)

Si vous n’avez pas besoin d’une facture, cliquez de nouveau sur "*Next*" sans renseigner d’informations personnelles.

Puis, confirmez votre achat en cliquant sur "*Confirm payment*".

![Image](assets/fr/05.webp)

Il vous faudra ensuite envoyer le montant indiqué à l’adresse Bitcoin fournie (malheureusement, Lightning n’est pas encore pris en charge). Une fois la transaction confirmée sur la blockchain, cliquez sur "*Close*" à côté de la facture.

Vous aurez alors accès à votre clé de licence. Attention : si vous n’avez pas saisi d’adresse email, cette clé ne sera affichée qu’à cet endroit. Pensez à sauvegarder l’URL de la page pour pouvoir y accéder ultérieurement si besoin.

![Image](assets/fr/06.webp)

## Créer un compte sur Threema

Maintenant que vous disposez de votre clé de licence, vous pouvez enfin lancer l’application. Lors du premier lancement, si vous n’avez pas acheté Threema via un magasin d’applications, il vous sera demandé de saisir votre clé de licence achetée sur le site.

![Image](assets/fr/07.webp)

Cliquez ensuite sur le bouton "*Set up now*".

![Image](assets/fr/08.webp)

Déplacez votre doigt sur l’écran pour générer une source d’entropie, nécessaire à la création de votre "*Threema ID*".

![Image](assets/fr/09.webp)

Votre "*Threema ID*" sera ensuite affiché. Il vous permettra d’entrer en contact avec d’autres utilisateurs. Cliquez sur "*Next*".

![Image](assets/fr/10.webp)

Choisissez un mot de passe. Il vous permettra de restaurer l’accès à votre compte en cas de besoin. Optez pour un mot de passe aussi long et aléatoire que possible, et conservez-en une copie sécurisée, par exemple dans un gestionnaire de mots de passe.

![Image](assets/fr/11.webp)

Choisissez ensuite un nom d’utilisateur, qui peut être soit votre véritable nom, soit un pseudonyme.

![Image](assets/fr/12.webp)

Vous aurez ensuite la possibilité de lier votre Threema ID à votre numéro de téléphone. Cela facilite votre recherche par vos contacts, mais si vous utilisez Threema, c’est aussi pour préserver votre anonymat : il est donc préférable de ne pas l’associer. Cliquez sur "*Next*".

![Image](assets/fr/13.webp)

Une fois l’étape terminée, cliquez sur "*Finish*".

![Image](assets/fr/14.webp)

Vous êtes maintenant connecté à Threema et pouvez commencer à communiquer.

![Image](assets/fr/15.webp)

## Paramétrer Threema

Avant toute chose, accédez aux paramètres en cliquant sur les trois petits points en haut à droite, puis sélectionnez "*Settings*".

![Image](assets/fr/16.webp)

Dans l’onglet "*Privacy*", vous trouverez plusieurs options à ajuster selon vos besoins :
- La synchronisation des contacts présents sur votre téléphone ;
- L’acceptation des messages provenant de personnes inconnues ;
- L’indicateur d’écriture lors de la saisie ;
- L’avis de réception des messages…

![Image](assets/fr/17.webp)

Dans l’onglet "*Security*", je vous recommande d’activer l’option "*Locking mechanism*" pour protéger l’accès à l’application. Il est également conseillé d’activer la passphrase pour sécuriser vos sauvegardes locales.

![Image](assets/fr/18.webp)

N’hésitez pas à explorer les autres sections des paramètres afin de personnaliser l’application selon vos préférences.

![Image](assets/fr/19.webp)

## Sauvegarder son compte Threema

Avant de commencer à échanger des messages, il est important de prévoir un moyen de récupérer votre compte, notamment en cas de changement ou de perte de votre téléphone. Pour cela, cliquez sur les trois points en haut à droite de l’interface, puis accédez au menu "*Backups*".

![Image](assets/fr/20.webp)

Vous trouverez ici deux options pour sauvegarder vos données :
- "*Threema Safe*" ;
- "*Data Backup*".

"*Threema Safe*" permet de sauvegarder toutes les informations de votre compte **sauf vos conversations**, sur les serveurs de Threema. Ces données sont chiffrées avec le mot de passe que vous avez choisi lors de la création de votre compte, ce qui garantit que Threema n’y a pas accès. Les sauvegardes se font automatiquement et régulièrement.

Avec "*Threema Safe*", pour récupérer votre compte sur un nouvel appareil, il vous suffira de renseigner votre "*Threema ID*" et votre mot de passe. S'il vous manque l'une de ces deux informations, il sera impossible de restaurer votre compte.

Cette option permet donc uniquement de récupérer votre ID, votre profil, vos contacts, vos groupes et certains paramètres, mais **pas l’historique de vos conversations**.

Pour activer "*Threema Safe*", il suffit de cocher l’option dans le menu "*Backups*".

![Image](assets/fr/21.webp)

Si vous souhaitez également sauvegarder et restaurer l’historique de vos conversations, vous devrez utiliser l’option "*Data Backup*". Celle-ci génère une sauvegarde complète de votre compte, stockée localement sur votre téléphone. Vous devrez transférer cette sauvegarde sur votre nouvel appareil et utiliser votre mot de passe (et éventuellement votre passphrase) pour restaurer l’intégralité de votre compte.

Étant donné que cette sauvegarde est uniquement locale, elle nécessite d’être régulièrement copiée sur un support externe. Sinon, en cas de perte de votre appareil, la récupération sera impossible. Cette méthode est donc surtout adaptée pour un transfert planifié d’un appareil à un autre, plutôt que pour des situations d’urgence.

Attention : "*Data Backup*" ne fonctionne que si vous restez sur le même système d’exploitation. Vous ne pourrez pas l’utiliser, par exemple, pour migrer d’un Samsung à un iPhone.

## Personnaliser son profil Threema

En haut à gauche de l’interface, cliquez sur votre image de profil, puis sélectionnez "*My Profile*".

![Image](assets/fr/22.webp)

Vous pouvez ici personnaliser votre profil : ajouter une photo, choisir qui peut la voir, ou encore consulter votre identifiant Threema.

![Image](assets/fr/23.webp)

## Synchroniser le logiciel PC

Si vous souhaitez accéder à vos conversations sur PC, vous pouvez synchroniser votre compte Threema avec le logiciel dédié. Téléchargez le logiciel correspondant à votre système d’exploitation [depuis le site officiel](https://threema.ch/en/download).

![Image](assets/fr/24.webp)

Sur votre téléphone, cliquez sur les trois points en haut à droite, puis ouvrez le menu "*Threema 2.0 for Desktop*".

![Image](assets/fr/25.webp)

Cliquez sur "*Add device*", puis scannez avec votre téléphone le QR code affiché par le logiciel sur votre ordinateur.

![Image](assets/fr/26.webp)

Pour confirmer la synchronisation, cliquez sur le groupe d’émojis affiché dans le logiciel.

![Image](assets/fr/27.webp)

Sur votre ordinateur, connectez-vous ensuite en utilisant votre mot de passe.

![Image](assets/fr/28.webp)

Vous avez désormais accès à votre compte Threema directement depuis votre ordinateur en plus de l'application mobile.

![Image](assets/fr/29.webp)

## Envoyer des messages avec Threema

Maintenant que tout est correctement configuré, vous pouvez commencer à communiquer. Cliquez sur le bouton "*Start chat*".

![Image](assets/fr/30.webp)

Sélectionnez "*New contact*".

![Image](assets/fr/31.webp)

Saisissez ou scannez le "*Threema ID*" de votre correspondant.

![Image](assets/fr/32.webp)

Cliquez sur l’icône de message.

![Image](assets/fr/33.webp)

Envoyez un premier message à votre correspondant.

![Image](assets/fr/34.webp)

Lorsque votre correspondant vous répondra, la connexion sera établie, et vous pourrez voir son nom ainsi que sa photo de profil. Vous pourrez alors échanger des messages, des fichiers multimédias et même passer des appels.

![Image](assets/fr/35.webp)

Félicitations, vous êtes maintenant au point sur l'utilisation de la messagerie Threema, une excellente alternative à WathsApp ! Si vous avez trouvé ce tutoriel utile, je vous serais très reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager ce tutoriel sur vos réseaux sociaux. Merci beaucoup !

Je vous recommande également de découvrir cet autre tutoriel, dans lequel je vous présente Proton Mail, une alternative à Gmail bien plus respectueuse de votre vie privée :

https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
