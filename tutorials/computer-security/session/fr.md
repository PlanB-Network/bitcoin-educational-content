---
name: Session
description: Envoyez des messages chiffrés, pas des métadonnées
---
![cover](assets/cover.webp)

Session est une application de messagerie chiffrée créée en 2020, conçue pour offrir un niveau de confidentialité supérieur à celui des messageries traditionnelles. Elle a d'abord été développée par l’*Oxen Privacy Tech Foundation*, puis par la *Session Technology Foundation*.

Session dispose de caractéristiques techniques intéressantes : chiffrement de bout en bout des messages, réseau décentralisé organisé de manière à garantir la disponibilité et la redondance, et routage en oignon inspiré de Tor. Aussi, contrairement à WathsApp ou Signal qui imposent un numéro de téléphone pour l'inscription, Session ne demande aucune information personnelle (pas de numéro, pas d’email, seulement une paire de clés cryptographiques).

Session permet l’envoi de messages, fichiers, messages vocaux, appels audio, ainsi que des groupes jusqu’à 100 membres (et des communautés au-delà), tout en minimisant les fuites de métadonnées.

![Image](assets/fr/01.webp)

Session s’adresse avant tout aux utilisateurs qui placent la confidentialité au cœur de leurs priorités. Cette messagerie représente une alternative sérieuse à WhatsApp, avec une architecture pensée pour résister aux modèles de surveillance modernes.

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
| **Session**          | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Chiffrement de bout en bout.*

## Installer l'application Session

Session est disponible sur toutes les plateformes. Vous pouvez télécharger l’application directement depuis la boutique d’applications de votre téléphone :
- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger) ;
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868) ;
- [F-Droid](https://fdroid.getsession.org/).

Sur Android, il est également possible de [l’installer via l’APK](https://github.com/session-foundation/session-android/releases).

Dans ce tutoriel, nous nous concentrerons sur la version mobile, mais sachez que [des versions pour ordinateur sont également disponibles](https://getsession.org/download) (MacOS, Linux et Windows). Nous verrons plus loin comment synchroniser un compte sur plusieurs appareils.

## Créer un compte sur Session

Lors du premier lancement, cliquez sur "*Create account*".

![Image](assets/fr/02.webp)

Choisissez un nom d’affichage pour votre profil. Cela peut être un pseudonyme ou votre véritable nom.

![Image](assets/fr/03.webp)

Vous devrez ensuite choisir entre deux modes de gestion des notifications :

- **Le mode rapide ("*Firebase Cloud Messaging/Apple Push Notification Service*")** : permet de recevoir les notifications de messages quasiment en temps réel grâce aux services de notification fournis par Google ou Apple (en fonction de votre système). Pour que cela fonctionne, votre adresse IP ainsi qu’un identifiant de notification unique sont transmis à Google ou Apple, et l’identifiant de compte Session est également enregistré auprès d’un serveur STF (via Tor). Ce mode implique une exposition (certes minimale) de métadonnées, mais il n'entraîne aucune compromission du contenu des messages ni des contacts, et ne permet pas de retracer votre activité réelle. Ce mode est donc plus efficace en termes de réactivité, mais il repose sur une infrastructure centralisée et légèrement moins bonne sur le plan de la confidentialité.

- **Le mode lent ("*background polling*")** : l'application Session reste active en arrière-plan et interroge périodiquement le réseau pour détecter de nouveaux messages. Cette approche garantit plus de confidentialité que la première, car aucune donnée n’est transmise à des serveurs tiers ; ni Google, ni Apple, ni les serveurs STF ne reçoivent la moindre information. En revanche, ce mode présente deux inconvénients : les notifications peuvent être retardées (jusqu'à plusieurs minutes), et la consommation d'énergie est généralement plus élevée à cause de l’activité de l’application en arrière-plan.

![Image](assets/fr/04.webp)

Vous êtes maintenant connecté à l’application Session et pouvez commencer à échanger des messages.

![Image](assets/fr/05.webp)

## Sauvegarder son compte Session

La première chose à faire avant de commencer à utiliser Session est de sauvegarder votre compte afin de pouvoir le restaurer en cas de perte de votre appareil. Pour cela, cliquez sur le bouton "*Continue*" à côté de "*Save your recovery password*".

![Image](assets/fr/06.webp)

Session va alors vous afficher une phrase mnémonique. Copiez-la soigneusement et conservez-la dans un endroit sécurisé. Cette phrase procure un accès complet à votre compte Session, il est donc important de ne pas la divulguer. Vous en aurez besoin pour accéder à votre compte sur un autre appareil, notamment en cas de perte ou de remplacement de votre téléphone actuel.

![Image](assets/fr/07.webp)

Cette phrase fonctionne d’une manière semblable aux phrases mnémoniques utilisées dans les portefeuilles Bitcoin. Je vous recommande donc de consulter cet autre tutoriel, dans lequel je vous explique les bonnes pratiques à suivre pour sauvegarder une phrase mnémonique :

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Attention** : Contrairement aux phrases mnémoniques utilisées sur les portefeuilles Bitcoin, sur Session, **vous devez absolument sauvegarder chaque mot en entier**. Les 4 premières lettres ne suffisent pas !

## Paramétrer l'application Session

Pour accéder aux paramètres de l’application, cliquez sur votre photo de profil en haut à gauche de l’interface. C'est dans ce menu que vous pouvez ajouter une photo de profil.

![Image](assets/fr/08.webp)

Dans le menu "*Privacy*", vous pouvez activer ou désactiver différentes fonctionnalités (attention, certaines peuvent exposer votre adresse IP). Je vous recommande également d’activer l’option "*Lock App*", qui impose une authentification pour accéder à l’application.

![Image](assets/fr/09.webp)

Dans le menu "*Notification*", vous retrouverez le choix entre le "*Fast Mode*" et le "*Slow Mode*" (voir les parties précédentes du tutoriel). Vous pouvez aussi y personnaliser les notifications selon vos préférences.

![Image](assets/fr/10.webp)

Enfin, rendez-vous dans le menu "*Appearance*" pour adapter l’interface à votre goût. Le menu "*Recovery Password*" vous permet, quant à lui, de retrouver votre phrase mnémonique si vous souhaitez en faire une nouvelle sauvegarde.

![Image](assets/fr/11.webp)

## Envoyer des messages avec Session

Pour entrer en contact avec d’autres personnes, cliquez sur le bouton "*+*" depuis la page d’accueil.

![Image](assets/fr/12.webp)

Plusieurs options s’offrent à vous. Si vous souhaitez créer ou rejoindre un groupe, sélectionnez "*Create Group*" ou "*Join Community*".

![Image](assets/fr/13.webp)

Si vous souhaitez que quelqu’un vous ajoute comme contact, vous pouvez lui faire scanner votre identifiant Session sous forme de QR code.

![Image](assets/fr/14.webp)

Pour envoyer votre identifiant à distance, cliquez sur "*Invite a Friend*". Vous pourrez alors copier votre identifiant Session et l’envoyer via un autre canal de communication. Vous pouvez également retrouver ces informations en cliquant sur votre photo de profil depuis la page d'accueil.

![Image](assets/fr/15.webp)

Si vous avez l’identifiant Session d’une autre personne et souhaitez l’ajouter, cliquez sur "*New Message*".

![Image](assets/fr/16.webp)

Vous pouvez alors coller son identifiant en texte ou le scanner directement si vous l'avez sous forme de QR code.

![Image](assets/fr/17.webp)

Envoyez ensuite un premier message à cette personne.

![Image](assets/fr/18.webp)

Dès que la personne aura accepté votre demande, vous verrez apparaître son pseudo, et vous pourrez échanger librement avec elle.

![Image](assets/fr/19.webp)

## Synchroniser le logiciel Desktop

Pour synchroniser votre compte sur votre ordinateur, vous devez évidemment installer le logiciel. [Téléchargez-le depuis le site officiel](https://getsession.org/download). Je vous conseille de vérifier son authenticité et son intégrité avant de l'installer.

![Image](assets/fr/20.webp)

Au premier lancement, cliquez sur "*I have an account*".

![Image](assets/fr/21.webp)

Saisissez votre phrase mnémonique en veillant à bien laisser un espace entre chaque mot.

![Image](assets/fr/22.webp)

Vous avez désormais accès à vos conversations depuis votre ordinateur.

![Image](assets/fr/23.webp)

Félicitations, vous êtes maintenant au point sur l'utilisation de la messagerie Session, une excellente alternative à WathsApp !

Je vous recommande également de découvrir cet autre tutoriel, dans lequel je vous présente Threema, une autre alternative intéressante pour votre application de messagerie :

https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74