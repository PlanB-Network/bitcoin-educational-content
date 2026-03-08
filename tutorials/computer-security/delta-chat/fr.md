---
name: Delta Chat
description: Guide pratique d'un outil de messagerie décentralisé
---

![image](assets/cover.webp)




## Introduction - Contrôle du chat et protection de la vie privée



Ces dernières années, on parle de plus en plus du "Chat Control", une proposition de réglementation qui vise à introduire l'analyse automatique des messages privés sur les principales plateformes de communication. L'objectif déclaré est de lutter contre les contenus illégaux, mais le problème est que ce mécanisme impliquerait en fait une surveillance de masse, qui porterait atteinte au cryptage de bout en bout et donc à la vie privée de tous les utilisateurs, et pas seulement des contrevenants.



Le risque réel est que les chats deviennent des environnements contrôlés, où chaque message, image ou pièce jointe pourrait être examiné avant même d'atteindre le destinataire. C'est là qu'intervient une solution possible : abandonner les plateformes centralisées au profit de systèmes de messagerie décentralisés, qui ne dépendent pas d'un fournisseur unique et ne peuvent pas facilement être soumis à ce type d'examen.



L'une de ces solutions sera présentée dans ce tutoriel : Delta Chat. Un outil mature et déjà utilisable.




## Pourquoi Delta Chat et comment cela fonctionne-t-il ?



Delta Chat est déjà une très bonne solution de messagerie pour un usage quotidien : très utile pour parler à des amis, à la famille et à d'autres personnes, comme un véritable équivalent de WhatsApp.



Il s'agit d'un système de messagerie décentralisé entièrement basé sur le courrier électronique. Il s'appuie sur l'infrastructure du courrier électronique traditionnel, tout en construisant une interface et une expérience de messagerie instantanée moderne. À première vue, cela peut sembler un peu improvisé, mais cela fonctionne très bien et est étonnamment robuste. Vous pouvez utiliser des serveurs de messagerie dédiés appelés ChatMail, mais il peut également fonctionner de manière transparente avec des serveurs de messagerie ordinaires. Cela signifie que vous pouvez vous connecter avec un compte existant si vous le souhaitez, sans avoir à créer quoi que ce soit de nouveau.



Un autre point fort est la prise en charge des WebXDC, qui sont de petites applications Web pouvant être utilisées directement dans les chats, à l'instar des mini-applications de Telegram. La différence importante est que ces applications n'ont pas d'accès à Internet et ne peuvent donc pas suivre l'utilisateur ou envoyer des données à l'extérieur.



Du point de vue de la sécurité, Delta Chat utilise un cryptage vérifié de bout en bout, basé sur PGP mais avec des extensions modernes qui le rendent comparable au niveau de protection de Signal. Le seul manque actuel est le Perfect Forward Secrecy, mais il s'agit d'un aspect évolutif.



Basé uniquement sur le courrier électronique, Delta Chat l'évite complètement :




- numéros de téléphone obligatoires
- Identifiants centralisés
- les inscriptions liées à un seul service



C'est ce qui rend cet outil très résistant aux réglementations invasives telles que Chat Control.




## Installation



Sur le site officiel de [Delta Chat] (https://delta.chat/download), vous pouvez accéder à la section Téléchargement. Sous Linux, il est disponible via Flathub, mais il existe également des paquets pour Arch, NixOS, Snap et des versions autonomes.



![image](assets/it/01.webp)



Il est également disponible pour :




- [F-Droid] (https://f-droid.org/app/com.b44t.messenger)
- [Play Store] (https://play.google.com/store/apps/details?id=chat.delta)
- [iOS] (https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows] (https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS] (https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch] (https://open-store.io/app/deltatouch.lotharketterer)
- et d'autres magasins...



Si vous cherchez un guide pour installer F-Droid, ce tutoriel pourrait vous aider :



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Une chose très importante : les versions de bureau ne nécessitent pas de téléphone. Contrairement à WhatsApp ou SimpleX Chat, il n'est pas nécessaire de s'inscrire d'abord à partir d'un téléphone portable. Vous pouvez créer votre profil directement sur votre PC ou le transférer depuis un autre appareil.




## Création d'un profil



Une fois l'application ouverte, Delta Chat vous demande si vous souhaitez créer un nouveau profil ou utiliser un profil existant.



![image](assets/it/02.webp)



En créant un nouveau profil, vous pouvez entrer :




- un nom
- une image (facultatif)



Un serveur ChatMail est proposé par défaut, mais c'est possible :




- choisir un autre serveur ChatMail
- utiliser un compte de messagerie classique
- configurer manuellement IMAP et SMTP
- s'inscrire en utilisant le code d'invitation d'un autre utilisateur



Après quelques secondes, le profil est prêt et vous pouvez commencer à utiliser l'application.



![image](assets/it/03.webp)




## Interface et chat



L'interface est très simple et directe :




- Les messages de l'appareil, qui sont des communications locales
- Messages enregistrés, similaires à ceux de Telegram et synchronisables entre les appareils



![image](assets/it/04.webp)



Pour ajouter un contact, il suffit de le faire :




- Afficher votre code QR
- Scannez l'image de l'autre personne
- Inviter par un lien (partager le lien d'invitation).



![image](assets/it/05.webp)



Une fois la connexion établie, le chiffrement de bout en bout est automatiquement configuré. L'interface utilisateur du chat est très similaire à celle de WhatsApp :




- les messages textuels et vocaux
- photos, vidéos et fichiers
- réponses aux messages
- réactions
- messages contextuels
- notifications personnalisables.



![image](assets/it/06.webp)



## WebXDC : applications dans les chats :



Delta Chat permet l'utilisation de WebXDC, c'est-à-dire de petites applications intégrées dans les conversations. Voici une courte liste des plus utiles identifiées :




- enquêtes
- planches à dessin
- chats privés temporaires
- jeux avec scores partagés par chat



Des jeux plus complexes peuvent également être lancés, ce qui démontre la flexibilité de cet outil.



![image](assets/it/07.webp)



## Groupes, canaux et fonctions avancées



Vous pouvez créer des groupes, utiliser des autocollants (en particulier sur les bureaux) et, en activant les options expérimentales, même des canaux, similaires à ceux de Telegram.



Dans les paramètres avancés, vous pouvez activer :




- appels vocaux (encore expérimental)
- gestion avancée des profils de courrier électronique
- des sauvegardes complètes.



![image](assets/it/08.webp)



## Multi-appareils et sauvegarde



Delta Chat est entièrement compatible avec les appareils multiples :




- vous pouvez ajouter un deuxième appareil via le code QR
- vous pouvez effectuer un transfert complet par le biais d'une sauvegarde.



En quelques secondes, vous retrouverez vos chats, vos groupes et votre historique complet, sans dépendre d'un serveur central.



![image](assets/it/09.webp)




## Conclusion



À l'heure où l'on parle de plus en plus de contrôler les communications privées, Delta Chat représente une réponse concrète : une messagerie décentralisée et cryptée réellement utilisable au quotidien.



C'est la solution qui, de toutes celles que j'ai essayées, m'a le plus convaincu en termes de simplicité, d'intimité et de liberté. Si vous le souhaitez, vous pouvez également me contacter sur Delta Chat via le [lien d'invitation] suivant (https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats)



Si vous avez apprécié ce guide, vous pouvez me soutenir en faisant un don et en laissant un pouce en l'air. Et n'oubliez pas : ce n'est qu'en utilisant et en explorant Delta Chat, à la fois sur mobile et sur ordinateur, que vous découvrirez toutes ses fonctionnalités.



Jusqu'à la prochaine fois.