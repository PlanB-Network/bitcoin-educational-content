---
name: Keet
description: Peer-to-peer chat
---
![cover](assets/cover.webp)

Keet est une messagerie instantanée pensée pour fonctionner sans aucun serveur. Lancée en 2022 par la société Holepunch (une entreprise financée par Tether et Bitfinex), l'application repose entièrement sur un réseau pair-à-pair et se distingue par une approche radicalement décentralisée : les messages, appels et fichiers sont échangés directement entre les utilisateurs, sans intermédiaire.

Keet chiffre toutes les communications de bout en bout et ne demande aucune donnée personnelle. L’inscription est anonyme, il n’y a ni numéro de téléphone ni email requis. En plus des échanges de messages texte, Keet propose des appels vidéo en très haute qualité, ainsi que le partage de fichiers volumineux sans limite de taille. Cette application peut donc être utilisée de manière hybride, à la fois pour un usage personnel et professionnel.

![Image](assets/fr/01.webp)

Pour le moment (avril 2025), Keet n’est pas entièrement open-source. Une partie du code source est disponible sur [le dépôt GitHub de Holepunch](https://github.com/holepunchto), notamment les composants liés à la cryptographie et au réseau, mais l’interface du client ne l’est pas encore. Holepunch a toutefois annoncé son intention de rendre l’ensemble de l’application open-source à terme. Selon le moment où vous découvrez ce tutoriel, cela a peut-être déjà été fait.


| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| **Keet**             | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Chiffrement de bout en bout.*

## Installer Keet

Keet est disponible sur toutes les plateformes. Vous pouvez télécharger l’application directement depuis la boutique d’applications de votre téléphone :
- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1) ;
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549) ;

Sur Android, il est également possible de [l’installer via l’APK](https://github.com/holepunchto/keet-mobile-releases/releases).

Dans ce tutoriel, nous nous concentrerons sur la version mobile, mais sachez que [des versions pour ordinateur sont également disponibles](https://keet.io/) (MacOS, Linux et Windows). Il est d'ailleurs possible de synchroniser son compte sur plusieurs appareil.

## Créer un compte sur Keet

Lors du premier lancement, vous pouvez ignorer les écrans de présentation.

![Image](assets/fr/02.webp)

Cliquez sur le bouton "*I'm a new user*".

![Image](assets/fr/03.webp)

Acceptez les conditions d’utilisation, puis cliquez sur "*Quick setup*".

![Image](assets/fr/04.webp)

Choisissez un nom ou un pseudo, puis cliquez sur "*Finish setup*".

![Image](assets/fr/05.webp)

Votre profil est désormais créé. Cliquez à nouveau sur "*Finish setup*" pour finaliser.

![Image](assets/fr/06.webp)

Vous pouvez personnaliser votre profil à tout moment depuis l’onglet "*Profile*".

## Sauvegarder son compte Keet

La première chose à faire avec votre nouveau compte Keet est de sauvegarder votre phrase de récupération. Il s’agit d’une suite de 24 mots qui vous permettra de restaurer l’accès à votre compte en cas de perte ou de changement d’appareil. Cette phrase donne un accès complet à votre compte à toute personne qui la connaît : il est donc important d’en faire une sauvegarde fiable et de ne jamais la divulguer.

Pour ce faire, cliquez sur l’onglet "*Profile*" situé en bas à droite de l’interface.

![Image](assets/fr/07.webp)

Puis accédez au menu "*Settings*".

![Image](assets/fr/08.webp)

Sélectionnez "*Privacy and Security*".

![Image](assets/fr/09.webp)

Cliquez ensuite sur "*Recovery phrase*".

![Image](assets/fr/10.webp)

Appuyez sur le bouton "*View phrase*" pour afficher votre phrase de récupération. Copiez-la soigneusement et conservez-la dans un endroit sécurisé.

![Image](assets/fr/11.webp)

## Envoyer des messages avec Keet

Pour communiquer sur Keet, il faut créer des "*Room*". Pour cela, cliquez sur l’icône en forme de crayon située en haut à droite de l’interface.

![Image](assets/fr/12.webp)

Sélectionnez "*New group chat*".

![Image](assets/fr/13.webp)

Choisissez un nom et une description pour votre "*Room*", puis cliquez sur "*Create group chat*".

![Image](assets/fr/14.webp)

Votre "*Room*" est maintenant créée. Cliquez sur l’icône "*+*" en haut à droite pour inviter des participants.

![Image](assets/fr/15.webp)

Définissez les droits que vous accordez aux nouveaux membres via le lien d’invitation, ainsi que la durée de validité du lien. Cliquez ensuite sur "*Generate invite*".

![Image](assets/fr/16.webp)

Keet va générer un lien pour rejoindre votre "*Room*". Vous pouvez soit le copier et le partager, soit faire scanner son QR code par les personnes que vous souhaitez inviter.

![Image](assets/fr/17.webp)

Vous pouvez à présent commencer à échanger des messages et des fichiers multimédias. Pour lancer un appel, cliquez sur l’icône de téléphone en haut à droite.

![Image](assets/fr/18.webp)

Depuis ce groupe, vous pouvez également envoyer des messages privés à un membre spécifique. Cliquez sur la photo de profil du groupe, puis sélectionnez le membre souhaité dans la section "*Members*".

![Image](assets/fr/19.webp)

Cliquez sur le bouton "*Send DM request*" et saisissez votre message.

![Image](assets/fr/20.webp)

Une fois la demande de DM acceptée, vous retrouverez ce contact sur la page d’accueil et pourrez échanger avec lui en privé.

![Image](assets/fr/21.webp)

## Synchroniser son compte sur plusieurs appareils

Maintenant que vous savez utiliser Keet et que vous disposez d’un compte, vous pouvez également le synchroniser sur un autre appareil, comme un ordinateur. Pour cela, ouvrez l’application sur votre mobile, puis cliquez sur "*Profile*" et accédez aux "*Settings*".

![Image](assets/fr/22.webp)

Rendez-vous ensuite dans le menu "*My devices*".

![Image](assets/fr/23.webp)

Cliquez sur "*Add device*". Keet va générer un lien permettant de synchroniser un nouvel appareil. Copiez ce lien.

![Image](assets/fr/24.webp)

Sur votre second appareil, installez Keet. Sur l’écran d’accueil, sélectionnez l’option "*I'm a current user*".

![Image](assets/fr/25.webp)

Cliquez ensuite sur "*Link device*".

![Image](assets/fr/26.webp)

Collez le lien fourni par votre premier appareil, puis cliquez sur "*Start syncing*".

![Image](assets/fr/27.webp)

Sur votre premier appareil, cliquez sur "*Confirm link devices*" pour autoriser la connexion.

![Image](assets/fr/28.webp)

Sur le second appareil, finalisez le processus en cliquant sur "*Link devices*".

![Image](assets/fr/29.webp)

Vous avez maintenant accès à toutes vos "*Room*" et à vos conversations depuis ce nouvel appareil.

![Image](assets/fr/30.webp)

Félicitations, vous êtes maintenant au point sur l'utilisation de la messagerie Keet, une excellente alternative à WathsApp ! Si vous avez trouvé ce tutoriel utile, je vous serais très reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager ce tutoriel sur vos réseaux sociaux. Merci beaucoup !

Je vous recommande également de découvrir cet autre tutoriel, dans lequel je vous présente Proton Mail, une alternative à Gmail bien plus respectueuse de votre vie privée :

https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2