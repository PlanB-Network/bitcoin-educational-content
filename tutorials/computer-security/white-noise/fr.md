---
name: White Noise
description: Une application de messagerie privée et décentralisée, basée sur les protocoles Nostr et MLS
---

![cover](assets/cover.webp)


## Introduction

"Au milieu de la difficulté se trouve l'opportunité". Cette citation de Albert Einstein nous rappelle que les problèmes ne sont pas définitifs, mais contiennent en eux les germes de nouvelles solutions innovantes.

Les motivations derrière le lancement de la solution que nous vous proposons de découvrir dans ce tutoriel l'illustre parfaitement. Il s'agit de **White Noise** qui est née d'une nécessité. 

Selon les propos de son fondateur, Max Hillebrand, rapportés par *Bitcoin Magazine* : « Nous avons lancé ce projet faute d’alternatives. » Il explique que « les applications de chiffrement existantes sont inefficaces à grande échelle : ajouter 100 personnes à une conversation de groupe ralentit considérablement le chiffrement. Les plateformes décentralisées, quant à elles, ne proposent pas de messagerie privée. Enfin, le réseau de relais ouvert de Nostr permet à chacun de diffuser des idées, mais la protection des messages directs y reste dramatiquement insuffisante. Nous l’avons compris : pour protéger la liberté, il fallait fusionner ces systèmes. »

## Qu'est ce que White Noise?

White Noise est une application de messagerie open source développée par une équipe à but non lucratif. Cette application prône la sécurité, la vie privée et la décentralisation. Contrairement aux applications classiques, elle ne nécessite ni numéro de téléphone ni adresse email. 
White Noise se distingue par l’intégration de deux protocoles fondamentaux  — Nostr et MLS —  qui constituent sa base technique.

Nostr (Notes and Other Stuff Transmitted by Relays) est un protocole décentralisé et open source conçu dans un but de résistance à la censure.  Ce protocole fonctionne grâce à des relais, des paires de clés et des clients. 

https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Avec white Noise, vous avez même la possibilité de choisir vos propres de relais pour maximiser la confidentialité.

Tandis que le MLS (Messaging Layer Security), est un protocole de sécurité qui permet le chiffrement bout en bout des messages. Autrement dit, les messages ne sont accessibles qu'aux bouts ou terminaisons de communication que sont l'expéditeur et le destinataire du message. Ainsi, les relais impliqués dans l'acheminement des messages ne peuvent pas accéder à leur contenu. 

Voici un petit tableau comparatif entre White Noise et un certain nombre d'applications de messagerie les plus connues.

| Points de comparaisons      | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Chiffrement E2EE / 1:1      | ✅ Oui       | Facultatif | ✅ Oui           | ✅ Oui   | ✅ Oui    | ✅ Oui            | ✅ Oui  |
| Chiffrement de groupe E2EE  | ✅ Oui       | ❌ Non      | ✅ Oui           | ✅ Oui   | ✅ Oui    | Facultatif       | ✅ Oui  |
| Anonymisation de l'identité | ✅ Oui       | Facultatif | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Serveur open source         | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Client open source          | ✅ Oui       | ✅ Oui      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Serveur décentralisé        | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Année de création           | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |


## Débuter avec White Noise

### Installation de White Noise

Rendez-vous sur le [site web de White Noise](https://www.whitenoise.chat/), puis cliquez sur **Download**.

![screen](assets/fr/03.webp)

À l'heure actuelle, White Noise n'est accessible que sur les appareils mobiles.
Sur la nouvelle interface qui apparait, appuyez sur : 

- le bouton **Zapstore** ou **Android APK** si vous souhaitez le télécharger sur Android ;
- sur le bouton **iOS TestFlight** si vous utilisez un iPhone. 

![screen](assets/fr/04.webp)

Dans le cadre de notre tutoriel, nous procèderons à un téléchargement sur Android. 
Si vous choisissez le téléchargement via **Zapstore**, vous serez redirigé vers ce dernier. Une fois sur Zapstore, tapez **White Noise** dans la barre de recherche. Ensuite procédez , au téléchargement en cliquant sur **Install**.

![screen](assets/fr/05.webp)

![screen](assets/fr/06.webp)

Si vous optez pour le téléchargement du fichier APK, vous serez redirigé vers le dépôt GitHub de White Noise pour choisir la version adaptée à votre smartphone.  

Les fichiers APK disponibles sont : 

- **whitenoise-0.2.1-arm64-v8a.apk** (57,7 Mo), adapté aux téléphones récents avec processeur 64 bits ;
- **whitenoise-0.2.1-armeabi-v7a.apk** (47,5 Mo) adapté aux téléphones plus anciens avec processeur 32 bits.

Par ailleurs, vous avez les fichiers **.sha256** qui sont juste des checksums pour vérifier l'intégrité du téléchargement.

![screen](assets/fr/07.webp)

Dès que le téléchargement est terminé, installez puis ouvrez l’application. 

![screen](assets/fr/08.webp)

### Configuration initiale du compte utilisateur

Pour votre première connexion sur White Noise, appuyez sur le bouton **S'inscrire**. 

![screen](assets/fr/09.webp)

Ensuite, configurez votre profil en choisissant une photo de profil, un nom et en ajoutant une petite description de vous. Vous n'êtes pas obligé de renseigner votre véritable identité (nom et photo). 
Notez que White Noise vous choisit un nom (pseudonyme) automatiquement, que vous pouvez conserver ou modifier. Appuyez enfin, sur le bouton **Terminer**.

![screen](assets/fr/10.webp)   

Vous êtes redirigé vers **l'interface principale (écran d'accueil)** de White Noise où seront listées vos conversations. Votre compte est désormais configuré et prêt à être utilisé. Vous pouvez partager votre profil ou rechercher des amis pour commencer une discussion.

![screen](assets/fr/11.webp)


### Découverte des interfaces de White Noise

Sur l'interface principale, vous avez en haut de l’écran :

Dans le coin supérieur gauche, l'icône de profil qui est votre photo de profil en miniature, à défaut la première lettre de votre nom de profil. En cliquant dessus, vous accédez aux paramètres de votre compte. 

![screen](assets/fr/12.webp)

![screen](assets/fr/13.webp)

Dans le coin supérieur droit, se trouve l'icône de l'interface de démarrage d'une nouvelle conversation. 

![screen](assets/fr/14.webp)

![screen](assets/fr/15.webp)


## Paramètres du compte utilisateur

Appuyez sur l'icône de profil dans le coin supérieur gauche pour accéder aux paramètres.

![screen](assets/fr/16.webp) 

En haut de l'interface **Paramètres**, vous avez votre photo et votre nom de profil, suivi de votre clé publique que vous pouvez partager grâce au code QR situé juste à côté. 

![screen](assets/fr/17.webp)

Juste en dessous, vous avez le bouton **Changer de compte** qui vous permet de vous connecter à un autre profil dans l'application. 

![screen](assets/fr/18.webp)

Ensuite, vous disposez d'une première section composée de quatre (4) sous-menus tels que :

- **Modifier le profil**

Dans ce sous-menu, vous pouvez modifier le nom du profil, l'adresse Nostr (NIP-05)… N'oubliez pas de cliquer sur **Sauvegarder** afin d'enregistrer vos changements.

![screen](assets/fr/19.webp)

- **Clés du profil**

Ici, vous avez accès à vos clés publique et privée (secret). Comme vous le rappelle White Noise, votre clé privée n'est à divulguer sous aucun prétexte. 

![screen](assets/fr/20.webp)

- **Relais réseau**

Ajoutez ou supprimez dans ce sous-menu les **relais généraux** (relais définis pour une utilisation dans toutes vos applications Nostr), les **relais de boîte de réception** et les **relais de paquets de clés**. 

Pour le faire, tapez sur l'icône **poubelle** devant un relai pour le supprimer ou tapez sur l'icône **+** (plus) pour en ajouter un nouveau.

![screen](assets/fr/21.webp)

- **Se déconnecter**

Cliquez sur ce sous-menu pour déconnecter votre compte de l'application. Mais, rassurez-vous d'avoir correctement sauvegardé vos clés privées hors ligne sinon vous ne pourrez plus vous reconnecter ultérieurement.

![screen](assets/fr/22.webp)


Une deuxième section, vous propose les sous-menus : 

- **Paramètres de l'application**

Vous avez la possibilité de définir ici, l'apparence (le thème et la langue d'affichage) de l'application, voire de supprimer les données si vous les sentez compromises ou si vous vous sentez vous-même en danger.

![screen](assets/fr/23.webp)

- **Faire un don à White Noise**

Vous pouvez supporter l'équipe derrière White Noise (organisation à but non lucratif) par des dons via leur adresse Lightning ou leur adresse de paiement silencieux Bitcoin. 

![screen](assets/fr/24.webp)

Finalement, vous avez tout en bas les **paramètres développeur**.

![screen](assets/fr/25.webp)


## Démarrer une conversation

Maintenant, intéressons-nous au démarrage d'une conversation. Au moment où nous rédigeons ce tutoriel, White Noise met à disposition trois options de communication. Nous explorerons successivement les **conversations privées** (**Chat 1:1**) c'est-à-dire entre seulement vous et une autre personne, les **conversations de groupe** et l'**envoi de fichiers multimédias**.


### Chat 1:1

Depuis l'interface principale, pour ajouter un nouvel correspondant, cliquez sur l'icône de l'interface de démarrage d'une nouvelle conversation. 
Ensuite, scannez le code QR de la clé publique (1) ou collez dans la barre de recherche la clé publique (2) de votre nouvel correspondant pour le rechercher. 

![screen](assets/fr/26.webp)

Puis, tapez sur le bouton **Commencer la conversation** pour démarrer une conversation avec votre correspondant. Vous pouvez aussi **suivre** votre correspondant ou l'inviter à une conversation de groupe en appuyant sur le bouton **Ajouter au groupe**.

![screen](assets/fr/27.webp)

Votre premier message à un nouvel correspondant s'apparente à une demande d'invitation. Cette demande devra être acceptée par votre correspondant avant que vous ne puissiez communiquer avec lui. En cas de refus, bah pas de conversation possible.  

![screen](assets/fr/28.webp)

Par ailleurs, tant qu'il n'accepte pas votre invitation, il ne pourra pas prendre connaissance du contenu de votre message initial.  

Une fois qu'il accepte votre invitation, il peut maintenant vous répondre et vous pourrez tous deux communiquer de manière fluide et sécurisée. 

![screen](assets/fr/29.webp)

En outre, dans une discussion, vous avez des fonctionnalités additionnelles.

Vous pouvez faire un appui long sur un message spécifique pour faire apparaitre les options comme :
- réagir au message avec un émoji (1) ;
- faire une **citation directe** pour répondre au message en appuyant sur **Répondre** (2) ;
- copier le message en tapant sur **Copier** (3). 

![screen](assets/fr/30.webp)

- supprimer un message avec le bouton **Supprimer** seulement s'il émane de vous.

![screen](assets/fr/31.webp)

Vous pouvez faire des recherches dans une conversation.

Cliquez sur l'avatar du correspondant en haut de l'écran pour accéder aux "informations de conversation" et tapez sur le bouton **Recherche dans la conversation**. 

![screen](assets/fr/32.webp)

![screen](assets/fr/33.webp)

Dans la barre de recherche qui s'affiche, tapez le mot à rechercher et lancez ladite recherche. Vous verrez ensuite les mots recherchés s'afficher avec une certaine surbrillance en **gras**.

![screen](assets/fr/34.webp)


### Conversations de groupe

Il est possible de créer des groupes de conversation sur White Noise. 

Pour y parvenir, touchez l’icône de l'interface de démarrage d'une nouvelle conversation, puis cliquez sur **Nouvelle conversation de groupe**. Ensuite, dans la barre de recherche, entrez la clé publique du premier membre que vous souhaitez mettre dans votre groupe.

![screen](assets/fr/35.webp)

![screen](assets/fr/36.webp)

Éventuellement, si cette option ne fonctionne pas, depuis l'interface **Commencer une nouvelle conversation**, saisissez la clé publique du premier membre que vous souhaitez ajouter au groupe dans la barre de recherche. Vous pouvez également scanner le code QR associé à sa clé publique.

Cette fois-ci, au lieu de taper sur le bouton **Commencer la conversation**, cliquez plutôt sur le bouton **Ajouter au groupe**.

![screen](assets/fr/37.webp)

Sur le menu contextuel qui apparait, tapez sur **Nouvelle conversation de groupe**.

![screen](assets/fr/38.webp)

Puis, appuyez sur **Continuer** (vous n'avez plus besoin de renseigner sa clé publique à nouveau).

![screen](assets/fr/39.webp)

Étant le créateur du groupe, vous en êtes d'office l'administrateur. Renseignez les détails du groupe tel que **le nom et la description du groupe**, puis tapez sur le bouton **Créer un groupe**.

![screen](assets/fr/40.webp)

L'utilisateur que vous ajoutez comme premier membre, de même que les autres que vous ajouterez ultérieurement reçoivent une notification d'invitation à rejoindre le groupe. Il faut donc qu'il accepte en cliquant sur **Accepter** pour intégrer le groupe.

![screen](assets/fr/41.webp)

L'ajout d'un nouveau membre avec qui vous conversez déjà à un groupe existant aussi est possible. Pour le faire, cliquez sur l'avatar du correspondant en haut de l'écran pour accéder aux "informations de conversation" et tapez sur le bouton **Ajouter au groupe**.

![screen](assets/fr/42.webp)

Sur la nouvelle interface qui s'affiche, **cochez** le groupe dans lequel vous souhaitez l'ajoutez et tapez sur **Add to group**. Il ne reste plus qu'à attendre qu'il accepte d'intégrer le groupe.

![screen](assets/fr/43.webp)

Notez que seul un administrateur de groupe peut modifier les informations du groupe, ajouter ou expulser des membres. Aussi, la rotation des clés permet que les personnes bannies ne puissent plus déchiffrer les futurs messages.

Pour retirer un membre, depuis l'interface principale du groupe, tapez en haut sur l'icône du groupe pour accéder à l'interface des informations du groupe. 

![screen](assets/fr/44.webp)

![screen](assets/fr/45.webp)

 Ensuite, cliquez sur le nom du membre puis sur **Retirer du groupe**. À partir de cette interface qui apparait, vous pouvez aussi lui envoyer un message, le suivre ou l'ajouter à un autre groupe. 
 
 ![screen](assets/fr/46.webp)

### Envoi de fichiers multimédias

Pour le moment, seules les photos peuvent être partagées entre utilisateurs sur White Noise. Que vous soyez dans une conversation privée ou dans une conversation de groupe, pour le faire, vous devez : 

- appuyez sur le symbole **plus (+)** situé du côté gauche dans la zone de saisie de message texte.

![screen](assets/fr/47.webp)

- ensuite, cliquez sur la case avec l'inscription **Photos** qui apparait juste en bas pour accéder à votre galerie.

![screen](assets/fr/48.webp)

- choisissez la ou les photos à envoyer. 

![screen](assets/fr/49.webp)

![screen](assets/fr/50.webp)

![screen](assets/fr/51.webp)



## Points clés à retenir

White Noise offre un bon niveau de confidentialité et de sécurité supérieur. En revanche, elle est une application très récente, peu répandue et encore à ses débuts. Par conséquent, il est encore très tôt pour tirer des conclusions actives. Il est possible de rencontrer quelques de dysfonctionnements lors de l'utilisation.

 Actuellement, il lui manque certaines fonctionnalités (pas d’appels audio ou vidéo, pas d’envoi de fichiers multimédias audios ou vidéos) comparé aux applications de messagerie populaires. 
 
Néanmoins, White Noise reste une option intéressante pour des conversations où la confidentialité prime (par exemple avec de la famille, entre amis proches ou militants d'une cause commune), même si elle demande un petit effort d'installation (par store d'applications alternatifs ou de fichiers APK) et d’apprentissage (maîtriser un peu le concept des paires de clés, des clients et des relais avec le protocole Nostr).

Vous savez désormais comment utiliser White Noise, pour communiquer en toute sécurité avec vos amis et votre famille. N'hésitez pas à nous laisser un pouce vert si ce tutoriel vous a été utile. 

Nous vous recommandons notre tutoriel sur Tox Chat, une application qui vous permet de converser sans intermédiaires sur le protocole décentralisé Tox.

https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3
