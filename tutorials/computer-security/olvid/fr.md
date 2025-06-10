---
name: Olvid
description: La messagerie privée, pour tous
---
![cover](assets/cover.webp)

Olvid est une application de messagerie instantanée française lancée en 2019, pensée pour offrir un haut niveau de sécurité, sans compromis sur la vie privée. Contrairement à WhatsApp ou Signal, Olvid ne demande aucune donnée personnelle à l’inscription : pas de numéro de téléphone, pas d’email, rien. L’identification entre utilisateurs repose sur un échange de clés, sans serveur d’annuaire ni carnet d’adresses partagé.

Tous les messages sont chiffrés de bout en bout avec un protocole cryptographique original, conçu pour protéger aussi les métadonnées : personne ne sait avec qui vous discutez, ni quand. Le code des clients est open source, mais le serveur central utilisé pour acheminer les messages chiffrés reste propriétaire et hébergé sur AWS.

Le modèle de sécurité d’Olvid repose sur un principe important : l’absence totale de tiers de confiance dans l’établissement des identités numériques. Contrairement à la majorité des messageries chiffrées qui s’appuient sur un annuaire centralisé pour gérer les identités des utilisateurs, Olvid ne dépend d’aucune infrastructure centralisée pour garantir l’intégrité des communications. Cette architecture élimine ainsi les risques liés à une compromission de l’annuaire.

Olvid utilise néanmoins un serveur central de distribution des messages, mais celui-ci est strictement cantonné à un rôle logistique : il assure la transmission asynchrone des messages chiffrés. Ce serveur ne participe à aucune étape du chiffrement, ne connaît ni l’identité réelle des utilisateurs ni le contenu ou les métadonnées des messages (à l’exception de la clé publique du destinataire, nécessaire au routage). Il peut donc être considéré comme hostile par défaut sans remettre en cause la sécurité de l’ensemble. Même s’il était compromis, il ne permettrait aucun accès au contenu des communications. Olvid assume donc une centralisation de la distribution des messages (pour des raisons d’efficacité et de qualité de service) tout en garantissant une sécurité indépendante de cette infrastructure.

Olvid propose une version gratuite et une version payante avec abonnement à 4,99 € par mois. La version gratuite offre l’ensemble des fonctionnalités, à l’exception de l'émission d'appels audio et vidéo (il est toutefois possible d’en recevoir), et ne permet pas la synchronisation du compte sur plusieurs appareils. Donc si vous envisagez un usage exclusivement sur votre smartphone et que vous n’avez pas besoin de passer d’appels, Olvid constitue une excellente solution.

Olvid est certifiée par l’ANSSI (autorité française chargée de la cybersécurité). Cette application est une excellente alternative aux messageries traditionnelles (WhatsApp, Facebook Messenger, WeChat...) pour ceux qui recherchent la confidentialité tout en conservant une simplicité d’usage.

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
| **Olvid**            | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | 🟡(pas d'annuaire)   | **2019**          |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Chiffrement de bout en bout.*

## Installer l'application Olvid

Olvid est disponible sur toutes les plateformes. Vous pouvez télécharger l’application directement depuis la boutique d’applications de votre téléphone :
- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger) ;
- [App Store](https://apps.apple.com/app/olvid/id1414865219) ;

Sur Android, il est également possible de [l’installer via l’APK](https://www.olvid.io/download/).

Dans ce tutoriel, nous nous concentrerons sur la version mobile, mais sachez que [des versions pour ordinateur sont également disponibles](https://www.olvid.io/download/) (MacOS, Linux et Windows). Si vous choisissez la version payante, vous pourrez synchroniser votre compte sur plusieurs appareils.

![Image](assets/fr/01.webp)

## Créer un compte sur Olvid

Lors du premier lancement de l’application, cliquez sur le bouton "*Je suis un nouvel utilisateur*".

![Image](assets/fr/02.webp)

Choisissez un pseudo ou bien indiquez votre nom et prénom.

![Image](assets/fr/03.webp)

Ajoutez une photo de profil.

![Image](assets/fr/04.webp)

Votre compte est maintenant créé.

![Image](assets/fr/05.webp)

Pour éviter toute perte d’accès à votre compte Olvid, il est recommandé de configurer des sauvegardes automatiques. Pour cela, ouvrez les paramètres en cliquant sur les trois points situés en haut à droite de l’interface, puis sélectionnez "*Paramètres*".

⚠️ **Attention** : depuis la version 3.7 d'Olvid, la procédure pour sauvegarder vos profils et contacts a été remplacée par une nouvelle. Ce tutoriel présente encore l'ancienne version. Vous pouvez la découvrir la nouvelle version sur leur FAQ : [💾 Sauvegarder vos profils](https://www.olvid.io/faq/sauvegarder-vos-profils/)

![Image](assets/fr/06.webp)

Accédez au menu "*Sauvegarde des clés et contacts*".

![Image](assets/fr/07.webp)

Cliquez ensuite sur "*Générer une clé de sauvegarde*". Cette clé permettra de chiffrer vos sauvegardes. Si vous devez récupérer votre compte sur un autre appareil et que vous n'avez plus accès à celui-ci, vous aurez besoin à la fois d’une sauvegarde et de cette clé pour la déchiffrer.

![Image](assets/fr/08.webp)

Conservez cette clé dans un endroit sécurisé. Vous pouvez également en faire une copie papier.

![Image](assets/fr/09.webp)

Vous pouvez alors choisir de créer une sauvegarde locale ou une sauvegarde automatique sur un service cloud. Cette seconde option est fortement recommandée pour garantir l’accès à votre compte Olvid en toutes circonstances, même si vous perdez votre téléphone.

![Image](assets/fr/10.webp)

Assurez-vous que l’option "*Activer la sauvegarde automatique*" est bien cochée.

![Image](assets/fr/11.webp)

Vous pouvez également explorer les autres paramètres disponibles afin de personnaliser l’application selon vos besoins.

![Image](assets/fr/12.webp)

## Envoyer des messages avec Olvid

Pour pouvoir envoyer des messages, vous devez d’abord ajouter des contacts. Depuis la page d’accueil, cliquez sur le bouton bleu "*+*".

![Image](assets/fr/13.webp)

Olvid vous affiche alors votre identifiant utilisateur. Vous pouvez le transmettre aux personnes avec qui vous souhaitez échanger afin qu'elles vous ajoute comme contact.

Pour ajouter une personne, scannez son identifiant à l’aide de votre caméra, ou collez-le manuellement en cliquant sur les trois petits points situés en haut à droite.

![Image](assets/fr/14.webp)

Une fois l’identifiant scanné, vous devez soit faire scanner par votre interlocuteur le QR code affiché, soit lui envoyer une demande de connexion à distance en cliquant sur "*Entrer en contact à distance*".

![Image](assets/fr/15.webp)

La connexion est désormais établie.

![Image](assets/fr/16.webp)

Vous pouvez commencer à échanger des messages et autres contenus avec votre correspondant !

![Image](assets/fr/17.webp)

Depuis la page d’accueil, vous retrouverez toutes vos conversations.

![Image](assets/fr/18.webp)

Le second onglet regroupe l’ensemble de vos contacts.

![Image](assets/fr/19.webp)

Il est également possible de créer des discussions de groupe.

![Image](assets/fr/20.webp)

Félicitations, vous êtes maintenant au point sur l'utilisation de la messagerie Olvid, une excellente alternative à WathsApp ! Si vous avez trouvé ce tutoriel utile, je vous serais très reconnaissant de laisser un pouce vert ci-dessous. N'hésitez pas à partager ce tutoriel sur vos réseaux sociaux. Merci beaucoup !

Je vous recommande également de découvrir cet autre tutoriel, dans lequel je vous présente Proton Mail, une alternative à Gmail bien plus respectueuse de votre vie privée :

https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2
