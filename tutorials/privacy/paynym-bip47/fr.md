---
name: BIP47 - PayNym
description: Utiliser un code de paiement réutilisable sur Ashigaru
---
![cover](assets/cover.webp)

La pire erreur que vous puissiez commettre sur Bitcoin en matière de confidentialité est la réutilisation d’adresses. Chaque fois qu’une même adresse reçoit plusieurs paiements, ces opérations sont liées entre elles, et offrent ainsi au monde entier une cartographie de vos transactions. Il est donc fortement recommandé de toujours générer, pour chaque réception, une adresse unique. Mais pour certains cas d'utilisation de Bitcoin, respecter cette pratique n'est pas simple.

Le BIP47, proposé par Justus Ranvier en 2015, apporte une réponse élégante à ce problème. Il introduit le concept de **code de paiement réutilisable** : un identifiant unique permettant de recevoir un nombre quasi illimité de paiements en bitcoins onchain, sans jamais réutiliser d’adresse. Grâce à un mécanisme cryptographique basé sur un échange ECDH (*Diffie-Hellman sur courbes elliptiques*), chaque paiement vers un même code aboutit sur une adresse vierge, propre à la relation entre l'expéditeur et le destinataire.

Ce principe du BIP47 est implémenté notamment par **PayNym**, le système développé initialement par Samourai Wallet et aujourd’hui repris par Ashigaru. Dans ce tutoriel, nous verrons concrètement comment activer votre PayNym, échanger des codes de paiement avec un correspondant et réaliser des transactions sans réutilisation d’adresse.

Je ne reviendrai pas ici sur le fonctionnement détaillé du BIP47. Si vous souhaitez approfondir le sujet, je vous invite à consulter le chapitre 6.6 de ma formation BTC 204.

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Prérequis

Pour suivre ce tutoriel vous aurez simplement besoin d'un portefeuille sur l'applciaiton Ashigaru. Si vous ne savez pas comment téléchager, vérifier, installer l'applciaiton et y créer un protefeuile, je vous invite à d'abord suivre cet autre tutoriel :

https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f









