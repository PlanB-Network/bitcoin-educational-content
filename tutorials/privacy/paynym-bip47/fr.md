---
name: BIP47 - PayNym
description: Utiliser un code de paiement réutilisable sur Ashigaru
---
![cover](assets/cover.webp)

La pire erreur que vous puissiez commettre sur Bitcoin en matière de confidentialité est la réutilisation d’adresses. Chaque fois qu’une même adresse reçoit plusieurs paiements, ces opérations sont liées entre elles, et offrent ainsi au monde entier une cartographie de vos transactions. Il est donc fortement recommandé de toujours générer, pour chaque réception, une adresse unique. Mais pour certains cas d'utilisation de Bitcoin, respecter cette pratique n'est pas simple.

Le BIP47, proposé par Justus Ranvier en 2015, apporte une réponse élégante à ce problème. Il introduit le concept de **code de paiement réutilisable** : un identifiant unique permettant de recevoir un nombre quasi illimité de paiements en bitcoins onchain, sans jamais réutiliser d’adresse. Grâce à un mécanisme cryptographique basé sur un échange ECDH (*Diffie-Hellman sur courbes elliptiques*), chaque paiement vers un même code aboutit sur une adresse vierge, propre à la relation entre l'expéditeur et le destinataire.

![Image](assets/fr/01.webp)

Ce principe du BIP47 est implémenté notamment par **PayNym**, le système développé initialement par Samourai Wallet et aujourd’hui repris par Ashigaru. Dans ce tutoriel, nous verrons concrètement comment activer votre PayNym, échanger des codes de paiement avec un correspondant et réaliser des transactions sans réutilisation d’adresse.

Je ne reviendrai pas ici sur le fonctionnement détaillé du BIP47. Si vous souhaitez approfondir le sujet, je vous invite à consulter le chapitre 6.6 de ma formation BTC 204.

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Prérequis

Pour suivre ce tutoriel, il vous suffit de disposer d’un portefeuille sur l’application Ashigaru. Si vous ne savez pas comment télécharger, vérifier, installer l’application ou créer un portefeuille, je vous recommande de consulter d’abord ce tutoriel :

https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Demander son PayNym

La première étape consiste à réclamer votre PayNym. Cette opération n’est à effectuer qu’une seule fois par portefeuille. Elle permet d’associer votre code de paiement BIP47 dérivé depuis votre seed (`PM...`) à un identifiant unique propre à l’implémentation PayNym. Cet identifiant, plus court et lisible, pourra ensuite être transmis à vos correspondants pour faciliter les échanges, sans avoir à partager le long code BIP47 complet.

Pour cela, cliquez sur votre image de PayNym en haut à gauche de l’interface, puis sur votre code de paiement `PM...`.

![Image](assets/fr/02.webp)

Cliquez ensuite sur les trois petits points situés en haut à droite, puis sélectionnez `Claim PayNym`.

![Image](assets/fr/03.webp)

Validez en cliquant sur le bouton `CLAIM YOUR PAYNYM`.

![Image](assets/fr/04.webp)

Rafraîchissez la page : votre identifiant PayNym s’affiche désormais sous votre image, juste au-dessus de votre code de paiement BIP47.

![Image](assets/fr/05.webp)

Votre PayNym est désormais actif et prêt à être utilisé pour vos premières transactions BIP47.

## Se connecter avec un contact

Deux types de connexions existent entre les PayNym : **suivre** et **connecter**. L’opération de suivi (`follow`) est totalement gratuite. Elle établit un lien entre deux PayNym à travers Soroban, un protocole de communication chiffré reposant sur Tor, développé par l’équipe de Samourai et repris par Ashigaru. Cette liaison permet aux deux utilisateurs qui se suivent d’échanger des informations de manière privée, notamment pour coordonner des transactions collaboratives comme Stowaway ou StonewallX2 que nous verrons dans un autre tutoriel. Cette étape est propre à PayNym et ne fait pas partie du protocole BIP47.

![Image](assets/fr/06.webp)

L’opération de connexion (`connect`), quant à elle, est payante puisqu'il faut faire une transaction on-chain. Elle consiste à réaliser une transaction de notification telle que définie dans le BIP47. Cette transaction Bitcoin contient des métadonnées dans une sortie `OP_RETURN` qui permet d’établir un canal de communication chiffré entre le payeur et le destinataire. À partir de ce canal, le payeur pourra générer des adresses de réception uniques pour chaque paiement, et le destinataire sera notifié de ces paiements, et pourra générer les clés privées associées aux adresses pour dépenser ces fonds par la suite.

Cette transaction de notification a un coût : les frais de minage et 546 sats envoyés à l’adresse de notification du destinataire pour signaler la connexion. Une fois la connexion établie, on peut faire une quasi infinité de paiements via le BIP47.

En résumé :
* `Follow` : gratuit, établit une communication chiffrée via Soroban, utile pour les outils collaboratifs d'Ashigaru ;
* `Connect` : payant, réalise la transaction de notification BIP47 pour activer le canal entre le payeur et le destinataire.

Pour interagir avec un PayNym, il faut d’abord le *follow*. C’est la première étape avant d’établir une connexion BIP47. Imaginons que vous souhaitiez envoyer des paiements récurrents au PayNym `+instinctiveoffer10`.

Rendez-vous sur la page de votre PayNym sur Ashigaru, puis cliquez sur le bouton `+` en bas à droite de l’interface.

![Image](assets/fr/07.webp)

Vous pouvez ensuite soit coller le code de paiement complet du destinataire, soit scanner son QR code.

![Image](assets/fr/08.webp)

Si vous ne possédez que son identifiant PayNym, rendez-vous sur le site [Paynym.rs](https://paynym.rs/) pour retrouver le QR code associé à son code de paiement.

![Image](assets/fr/09.webp)

Une fois le QR code scanné, cliquez sur le bouton `FOLLOW` pour suivre ce PayNym.

![Image](assets/fr/10.webp)

L’action `FOLLOW` suffit pour effectuer des transactions collaboratives (*cahoots*). Cependant, pour envoyer des paiements BIP47, il est nécessaire d’établir une connexion : cliquez sur `CONNECT` pour réaliser la transaction de notification.

![Image](assets/fr/11.webp)

La transaction de notification est alors diffusée sur le réseau. Patientez jusqu’à ce qu’elle ait au moins une confirmation avant d’effectuer un premier paiement.

![Image](assets/fr/12.webp)

## Faire un paiement BIP47

Vous êtes désormais connecté au destinataire et pouvez lui envoyer un paiement sur une adresse unique, générée automatiquement grâce au protocole BIP47, sans aucun échange préalable avec lui.

Depuis la page principale de votre PayNym, cliquez sur le contact à qui vous souhaitez envoyer un paiement.

![Image](assets/fr/13.webp)

En haut à droite de l’interface, cliquez sur l’icône en forme de flèche.

![Image](assets/fr/14.webp)

Indiquez le montant à envoyer. Vous n’avez pas besoin de saisir d’adresse de réception : elle sera automatiquement dérivée grâce au protocole BIP47.

![Image](assets/fr/15.webp)

Vérifiez attentivement les détails de la transaction, notamment les frais, puis faites glisser la flèche verte en bas de l’écran pour signer et diffuser la transaction.

![Image](assets/fr/16.webp)

La transaction a bien été envoyée.

![Image](assets/fr/17.webp)

Dans cet exemple, le paiement a été effectué vers un autre de mes PayNym. Je peux donc constater qu’il est bien arrivé sur mon autre portefeuille Ashigaru, sans qu’aucune adresse n’ait été échangée manuellement : seul l’identifiant PayNym a été utilisé.

![Image](assets/fr/18.webp)

Vous savez désormais comment utiliser les codes de paiement réutilisables BIP47 grâce à l’implémentation PayNym sur l’application Ashigaru. Vous pouvez désormais partager ce code de paiement avec toute personne souhaitant vous envoyer des paiements (notamment des paiements récurrents). Vous pouvez également publier votre identifiant PayNym sur votre site web ou vos réseaux sociaux afin de recevoir des dons.

Pour approfondir vos connaissances sur ce protocole, comprendre en détail son fonctionnement et ses implications en matière de confidentialité, je vous recommande vivement de suivre mon cours BTC 204 :

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c
