---
name: Signal
description: Exprimez-vous librement
---
![cover](assets/cover.webp)

Signal est une application de messagerie chiffrée de bout en bout, conçue pour offrir une bonne confidentialité par défaut. Chaque message, appel et fichier est protégé grâce au protocole Signal, qui est reconnu comme l’un des protocoles de messagerie les plus robustes. Il est réutilisé par de nombreuses autres applications : WathsApp, Facebook Messenger, Skype ou encore Google Messages pour les communications RCS.

Signal a été lancé en 2014 par Moxie Marlinspike (pseudo) et développé depuis 2018 par la Signal Foundation, une organisation à but non lucratif créée avec le soutien de Brian Acton (cofondateur de WhatsApp).

![Image](assets/fr/01.webp)

Par rapport à WhatsApp, Signal se distingue par sa transparence : le code de l’application, tant côté client que côté serveur, est entièrement open source. Cela permet à quiconque de l’auditer, et notamment de vérifier que le chiffrement est bien appliqué conformément à ce qui est annoncé.

Signal repose toutefois sur l’utilisation d’un numéro de téléphone, ce qui représente son principal point faible en matière d’anonymat comparé à d’autres solutions. Malgré cela, l’application est selon moi l’une des plus fiables en matière de sécurité et de confidentialité, grâce à son architecture entièrement ouverte et à un protocole de chiffrement largement adopté, et donc testé et audité, contrairement à d’autres applications plus marginales.

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


## Installer l'application Signal

Signal est disponible sur toutes les plateformes. Vous pouvez télécharger l’application directement depuis la boutique d’applications de votre téléphone :
- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) ;
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669) ;

Sur Android, il est également possible de [l’installer via l’APK](https://github.com/signalapp/Signal-Android/releases).

Dans ce tutoriel, nous nous concentrerons sur la version mobile, mais sachez que [des versions pour ordinateur sont également disponibles](https://signal.org/fr/download/) (MacOS, Linux et Windows). Il faut toutefois commencer par configurer l’application mobile avant de pouvoir synchroniser votre compte avec la version desktop.

## Créer un compte sur Signal

Lors du premier lancement de l’application, cliquez sur le bouton "*Continue*".

![Image](assets/fr/02.webp)

Saisissez votre numéro de téléphone, puis cliquez sur "*Next*".

![Image](assets/fr/03.webp)

Un code de vérification vous sera envoyé par SMS. Renseignez ce code dans l’application Signal.

![Image](assets/fr/04.webp)

Choisissez un code PIN pour sécuriser votre compte Signal. Ce code permet de chiffrer vos données et vous servira à restaurer l’accès à votre compte en cas de perte de votre appareil. Il est donc important de choisir un code PIN robuste, aussi long et aléatoire que possible, et d’en effectuer une sauvegarde fiable.

![Image](assets/fr/05.webp)

Confirmez une seconde fois ce code PIN.

![Image](assets/fr/06.webp)

Vous pouvez maintenant personnaliser votre profil utilisateur. Choisissez une photo, indiquez votre nom ou un pseudo. À cette étape, vous pouvez également définir qui peut vous retrouver sur Signal via votre numéro. Sélectionnez "*Everyone*" si vous souhaitez être visible, ou "*Nobody*" pour rester introuvable via le numéro de téléphone (vous pourrez alors être ajouté uniquement avec votre "*Username*"). Une fois vos choix effectués, cliquez sur "*Next*".

![Image](assets/fr/07.webp)

Vous êtes désormais connecté à Signal et prêt à échanger des messages.

![Image](assets/fr/08.webp)

## Paramétrer votre compte Signal

En cliquant sur votre photo de profil en haut à gauche, vous accédez aux paramètres de l’application.

![Image](assets/fr/09.webp)

Le menu "*Account*" vous permet de gérer les paramètres liés à votre profil. Je vous conseille de conserver les réglages par défaut. Vous pouvez également activer l’option "*Registration Lock*", qui protège votre compte contre certains types d'attaques. Ce menu contient également les options nécessaires pour transférer votre compte vers un nouvel appareil.

![Image](assets/fr/10.webp)

En cliquant à nouveau sur votre image de profil dans les paramètres, vous accédez aux options de personnalisation de votre profil. Je vous recommande de définir un "*Username*" : cela vous permettra d’entrer en contact avec d’autres personnes sans exposer votre numéro de téléphone.

![Image](assets/fr/11.webp)

En sélectionnant "*QR code or link*", vous obtiendrez les informations à partager avec une personne souhaitant vous ajouter sur Signal.

![Image](assets/fr/12.webp)

Le menu "*Privacy*" est particulièrement important. Vous y trouverez des options permettant de contrôler la visibilité de votre numéro, la gestion de vos messages avec vos contacts, ainsi que diverses autorisations accordées sur l’application.

![Image](assets/fr/13.webp)

N’hésitez pas non plus à explorer les menus "*Appearance*", "*Chats*" et "*Notifications*" pour adapter l’interface et le fonctionnement de l’application à vos besoins personnels.

## Connecter l'application desktop

Pour connecter l’application desktop, commencez par installer le logiciel sur votre ordinateur (voir la première partie de ce tutoriel). Ensuite, sur votre téléphone, accédez aux paramètres et ouvrez la section "*Linked devices*".

![Image](assets/fr/14.webp)

Cliquez sur le bouton "*Link a new device*".

![Image](assets/fr/15.webp)

Sur votre ordinateur, lancez le logiciel, puis scannez le QR code affiché à l’écran à l’aide de votre téléphone. Si vous souhaitez importer vos conversations, sélectionnez l’option "*Transfer message history*".

![Image](assets/fr/16.webp)

Vos appareils sont désormais bien synchronisés.

![Image](assets/fr/17.webp)

## Envoyer des messages avec Signal

Pour communiquer avec quelqu’un sur Signal, il faut d’abord l’ajouter comme contact. Il y a plusieurs options : vous pouvez l’ajouter via son numéro de téléphone (si la personne a activé l’option permettant d’être trouvée par ce moyen), ou bien utiliser son identifiant Signal.

Cliquez sur l’icône en forme de crayon en bas à droite de l’interface.

![Image](assets/fr/18.webp)

Dans mon cas, je souhaite ajouter la personne via son nom d’utilisateur. Je clique donc sur "*Find by username*".

![Image](assets/fr/19.webp)

Vous pouvez ensuite soit coller son identifiant, soit scanner son QR code de connexion.

![Image](assets/fr/20.webp)

Envoyez-lui un message pour établir le contact.

![Image](assets/fr/21.webp)

La conversation apparaîtra ensuite sur la page d’accueil. Si la personne accepte votre demande de contact, vous pourrez voir son nom et sa photo de profil.

![Image](assets/fr/22.webp)

Félicitations, vous êtes maintenant au point sur l'utilisation de la messagerie Signal, une excellente alternative à WathsApp ! Si vous avez trouvé ce tutoriel utile, je vous serais très reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager ce tutoriel sur vos réseaux sociaux. Merci beaucoup !

Je vous recommande également de découvrir cet autre tutoriel, dans lequel je vous présente Proton Mail, une alternative à Gmail bien plus respectueuse de votre vie privée :

https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
