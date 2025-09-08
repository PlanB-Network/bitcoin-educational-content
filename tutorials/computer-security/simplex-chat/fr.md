---
name: SimpleX Chat
description: La première messagerie sans identifiant d'utilisateur
---
![cover](assets/cover.webp)

Lancée en 2021, SimpleX est une application de messagerie instantanée libre et radicalement différente dans son approche de la confidentialité. Contrairement WhatsApp, Signal et d'autres services de messagerie centralisés, SimpleX se démarque par sa gestion des utilisateurs : il n’existe aucun identifiant utilisateur, ni pseudonyme, ni numéro, ni clé publique visible. Cette absence totale d’identifiants rend la corrélation entre les utilisateurs pratiquement impossible, ce qui garantit une très bonne protection de votre vie privée.

Contrairement à la plupart des applications qui imposent un compte ou un numéro de téléphone, SimpleX permet d’initier des conversations en partageant un lien ou un QR code éphémère. Chaque lien permet la création d’un canal chiffré unique, et les contacts ne peuvent pas retrouver ou recontacter l’émetteur sans échange explicite. Les messages sont chiffrés de bout en bout et transitent par des serveurs relais qui les suppriment après expédition, lesquels ne voient ni l’expéditeur, ni le destinataire, ni leurs clés.

![Image](assets/fr/01.webp)

L’architecture réseau est entièrement décentralisée et non fédérée : les serveurs ne se connaissent pas entre eux, ne conservent pas de répertoire global, et n’hébergent aucun profil utilisateur. Mieux encore, chaque utilisateur peut déployer et utiliser son propre serveur relais tout en restant interopérable avec ceux du réseau public.

SimpleX est entièrement open-source (clients, protocoles et serveurs), disponible sur Android, iOS, Linux, Windows et macOS. Son stockage local est chiffré et portable, ce qui permet de transférer un profil d’un appareil à un autre sans dépendre d’un serveur centralisé.

SimpleX intègre toutes les fonctionnalités classiques des applications de messagerie. Toutefois, son ergonomie reste à ce jour moins fluide que celle de WhatsApp ou Signal. Son utilisation peut également s’avérer plus contraignante, en particulier pour l’ajout de contacts. Il s’agit donc selon moi d’une alternative pertinente à WhatsApp ou Signal pour les utilisateurs qui placent la confidentialité au cœur de leurs priorités, et qui sont prêts, pour cela, à faire quelques concessions sur le confort d’usage au quotidien.

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
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Chiffrement de bout en bout.*

## Installer l'application SimpleX Chat

SimpleX Chat est disponible sur toutes les plateformes. Vous pouvez télécharger l’application directement depuis la boutique d’applications de votre téléphone :
- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app) ;
- [App Store](https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084) ;
- [F-Droid](https://simplex.chat/fdroid/).

Sur Android, il est également possible de [l’installer via l’APK](https://github.com/simplex-chat/simplex-chat/releases).

Dans ce tutoriel, nous nous concentrerons sur la version mobile, mais sachez que [des versions pour ordinateur sont également disponibles](https://simplex.chat/downloads/) (MacOS, Linux et Windows). Il est possible de lier la version desktop à un profil utilisateur existant sur mobile, mais pour que cette synchronisation fonctionne, les deux appareils doivent impérativement être connectés au même réseau local.

![Image](assets/fr/02.webp)

## Créer un compte sur SimpleX Chat

Lors du premier lancement de l’application, cliquez sur le bouton "*Create your profile*".

![Image](assets/fr/03.webp)

Choisissez un nom d’utilisateur, qui peut être votre véritable nom ou un pseudonyme, puis cliquez sur "*Create*".

![Image](assets/fr/04.webp)

Vous devez ensuite définir la fréquence à laquelle l’application vérifiera l’arrivée de nouveaux messages. Si l’autonomie de la batterie de votre téléphone n’est pas un problème, sélectionnez "*Instant*" pour recevoir les messages en temps réel. Si vous préférez économiser votre batterie et empêcher l’application de fonctionner en arrière-plan, choisissez "*When app is running*" : vous ne recevrez alors les messages que lorsque l’application est ouverte. Un compromis possible consiste à opter pour une vérification périodique toutes les 10 minutes.

Une fois votre choix effectué, cliquez sur "*Use chat*".

![Image](assets/fr/05.webp)

Vous êtes désormais connecté à SimpleX Chat et prêt à commencer à échanger.

![Image](assets/fr/06.webp)

## Paramétrer SimpleX Chat

Avant toute chose, accédez aux paramètres en cliquant sur votre photo de profil en bas à droite, puis sur "*Settings*".

![Image](assets/fr/07.webp)

Les paramètres par défaut conviennent généralement à la majorité des utilisateurs. Toutefois, je vous recommande de vous rendre dans le menu "*Database passphrase & export*". C’est ici que vous pourrez exporter la base de données de votre compte SimpleX si vous souhaitez en faire une sauvegarde.

Vous avez également la possibilité de modifier la passphrase utilisée pour chiffrer cette base de données. Par défaut, elle est générée aléatoirement et stockée localement sur votre appareil. Si vous préférez, vous pouvez définir votre propre passphrase et supprimer la sauvegarde locale de la passphrase : vous devrez alors la saisir manuellement à chaque ouverture de l’application, ainsi que lors d’une éventuelle migration vers un autre appareil.

**Attention** : si vous choisissez cette option, la perte de la passphrase entraînera la perte définitive de tous vos profils et messages SimpleX.

![Image](assets/fr/08.webp)

Je vous recommande également de vous rendre dans le menu "*Privacy & security*", où vous pouvez activer l’option "*SimpleX Lock*". Cela permet de protéger l’accès à l’application à l’aide d’un code de verrouillage.

![Image](assets/fr/09.webp)

Enfin, les menus "*Notifications*" et "*Appearance*" vous permettront de personnaliser SimpleX Chat en fonction de vos préférences.

![Image](assets/fr/10.webp)

## Envoyer des messages avec SimpleX Chat

Pour vous connecter avec une autre personne sur SimpleX, vous avez deux possibilités :
- Utiliser un lien à usage unique ;
- Utiliser une adresse statique réutilisable.

L’adresse statique permet à toute personne qui la connaît de vous contacter sur SimpleX. Il s’agit d’une adresse persistante, pouvant être utilisée plusieurs fois, par différentes personnes, sans limitation de durée. C’est ce caractère permanent qui la rend plus vulnérable au spam. Toutefois, à la différence d’autres applications de messagerie, la suppression de votre adresse SimpleX suffit à stopper tout spam, sans affecter les conversations existantes. En effet, cette adresse ne sert qu’à établir la connexion initiale, et n’est plus nécessaire une fois l’échange amorcé.

Les liens à usage unique, quant à eux, ne peuvent être utilisés qu’une seule fois, par n’importe quel utilisateur. Une fois qu’un contact l'utilise, le lien devient invalide. Il vous faudra donc en générer un nouveau pour chaque nouvelle connexion.

### Avec l'adresse statique

Si vous souhaitez utiliser l’adresse, cliquez sur votre photo de profil en bas à gauche de l’interface, puis sélectionnez "*Create SimpleX address*". Cliquez ensuite à nouveau sur "*Create SimpleX address*".

![Image](assets/fr/11.webp)

Votre adresse réutilisable est maintenant créée. Vous pouvez la partager aux personnes souhaitant entrer en contact avec vous, soit en leur montrant le QR code, soit en leur transmettant le lien.

![Image](assets/fr/12.webp)

Cliquez sur le bouton "*Address settings*". Vous pourrez ici configurer les permissions associées à votre adresse. L’option "*Share with contacts*" permet de rendre votre adresse visible sur votre profil SimpleX. Ainsi, vos contacts pourront la consulter et la transmettre à d’autres personnes souhaitant vous contacter.

L’option "*Auto-accept*" permet d’accepter automatiquement les connexions entrantes via votre adresse. Cela signifie que toute personne disposant de votre adresse pourra voir votre profil et vous envoyer un message, sauf si vous activez l’option "*Accept incognito*". Cette dernière masque alors votre nom et votre photo de profil lors d’une nouvelle connexion, en les remplaçant par un pseudo aléatoire, distinct pour chaque interlocuteur.

![Image](assets/fr/13.webp)

### Avec le lien réutilisable

La seconde méthode pour entrer en connexion avec une personne consiste à créer un lien à usage unique. Pour cela, cliquez sur l’icône du crayon en bas à droite de l’interface, puis sélectionnez "*Create 1-time link*".

Si c’est votre contact qui vous a envoyé un lien, cliquez sur "*Scan / Paste link*" pour le scanner ou le coller.

![Image](assets/fr/14.webp)

SimpleX génère alors un lien à usage unique. Vous pouvez le transmettre à votre contact par n’importe quel moyen : échange physique, autre messagerie, etc.

![Image](assets/fr/15.webp)

Vous pouvez également choisir quel profil associer à ce lien d’invitation. Pour cela, cliquez sur votre profil situé juste en dessous du QR code. Vous aurez alors la possibilité :
- de sélectionner l’un de vos profils existants (nous verrons dans la partie suivante comment créer plusieurs profils) ;
- ou de choisir le mode "*Incognito*", qui masque votre nom et votre photo de profil avec un pseudonyme généré aléatoirement pour votre correspondant.

Ici, je choisis le mode "*Incognito*".

![Image](assets/fr/16.webp)

Mon contact a bien utilisé le lien. De son côté, il n’a pas activé le mode "*Incognito*", c’est pourquoi je vois son nom de profil, "*Bob*". En revanche, Bob ne voit pas mon vrai nom "*Loïc Morel*", mais un pseudonyme aléatoire, ici "*RealSynergy*".

![Image](assets/fr/17.webp)

Je pourrais commencer à discuter immédiatement, mais je souhaite d’abord vérifier que je parle bien à Bob, et non à une personne malveillante qui aurait intercepté le lien ou procédé à une attaque de type MITM.

Pour cela, nous allons vérifier notre lien de sécurité **en dehors de l’application**. C’est important, car en cas d’attaque MITM, une vérification interne serait compromise. Utilisez donc une autre messagerie sécurisée, ou encore mieux, vérifiez les codes en présentiel.

Dans le chat, cliquez sur la photo de Bob, puis sur "*Verify security code*". Bob doit faire la même chose de son côté.

![Image](assets/fr/18.webp)

Si vous êtes à distance, comparez les codes sur une autre messagerie sécurisée (ils doivent être identiques). Ou bien encore mieux, si vous pouvez vous voir en présentiel, scannez le QR code de votre interlocuteur en cliquant sur "*Scan code*".

![Image](assets/fr/19.webp)

Si la vérification réussit, une icône de bouclier avec une coche s’affichera à côté du nom de votre contact. Vous avez alors la garantie que vous échangez bien avec Bob. En cas d’échec, une alerte "*Incorrect security code!*" apparaîtra.

![Image](assets/fr/20.webp)

Vous pouvez maintenant échanger librement des messages, des appels et des fichiers avec Bob, selon les autorisations que vous avez définies pour cette conversation.

## Personnaliser ses profils SimpleX Chat

L’une des fonctionnalités les plus puissantes de SimpleX est la possibilité de gérer plusieurs profils d’utilisateurs complètement distincts, tous accessibles depuis un même compte local. Cela permet de séparer proprement vos différentes identités, sans complexifier la gestion de vos messages.

Par exemple, vous pourriez créer :
- Un profil avec votre vrai nom et une photo réelle pour vos échanges professionnels ;
- Un profil avec votre vrai nom et une photo marrante pour vos échanges familiaux ;
- Un profil avec une fausse photo et un pseudo pour vos conversations personnelles ;
- Un autre profil pseudonyme pour discuter avec des inconnus.

C’est ce que nous allons faire ici. Je commence par configurer mon profil principal, celui lié à mon identité réelle. Pour cela, je clique sur ma photo de profil en bas à droite, puis sur mon nom d’utilisateur.

![Image](assets/fr/21.webp)

Je clique ensuite sur ma photo de profil pour la modifier et en ajouter une nouvelle.

![Image](assets/fr/22.webp)

Pour ajouter d’autres profils, cliquez sur le menu "*Your chats profiles*".

![Image](assets/fr/23.webp)

Vous y verrez l’ensemble de vos profils. Cliquez sur "*Add profile*" pour en créer un nouveau.

![Image](assets/fr/24.webp)

Choisissez ensuite les informations de votre nouveau profil : nom, photo, etc. Ici, j’utilise un pseudo et une image différente pour masquer mon identité réelle dans certains échanges.

![Image](assets/fr/25.webp)

En maintenant votre doigt appuyé sur un profil, vous pouvez le masquer. Cela le rendra invisible dans l’application ainsi que toutes les conversations associées. Vous pouvez aussi choisir de le "*Mute*" pour ne plus recevoir de notifications.

![Image](assets/fr/26.webp)

Une fois vos profils créés, vous pouvez les gérer indépendamment. Depuis la page d’accueil, sélectionnez simplement le profil actif à afficher.

![Image](assets/fr/27.webp)

Lorsque vous créez un lien d’invitation ou une adresse statique, vous pouvez désormais choisir quel profil y associer. Par exemple, si je sélectionne le profil "*Satoshi Nakamoto*" pour générer un lien et que je l’envoie à Alice, elle ne verra que mon identité pseudonyme "*Satoshi Nakamoto*", sans jamais connaître mon identité réelle "*Loïc Morel*". Inversement, si je lui fournis un lien depuis mon vrai profil, elle n’aura aucun moyen de faire le lien avec mon profil pseudonyme.

![Image](assets/fr/28.webp)

Félicitations, vous êtes maintenant au point sur l'utilisation de la messagerie SimpleX, une excellente alternative à WathsApp !

Je vous recommande également de découvrir cet autre tutoriel, dans lequel je vous présente Threema, une autre alternative intéressante pour votre application de messagerie :

https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74
