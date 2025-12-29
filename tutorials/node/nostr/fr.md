---
name: Nostr
description: Découvre et commence a utiliser Nostr
---


![Un nouveau challenger est arrivé](assets/1.webp)

*À la fin de ce guide, vous comprendrez ce qu’est Nostr, vous aurez créé un compte et vous serez en mesure de l’utiliser.*

## Qu'est-ce que Nostr?

Nostr est un protocole capable de remplacer Twitter, Telegram et les autres médias sociaux.‌‌‌‌ C’est un protocole ouvert simple et capable de créer une fois pour toutes un réseau social mondial résistant à la censure.

## Comment ça fonctionne?

Nostr repose sur trois éléments : les paires de clés, les clients et les relais.

Chaque utilisateur possède une ou plusieurs identités, chacune déterminée par une paire de clés cryptographiques.

Pour accéder au réseau, il faut utiliser un logiciel client et se connecter à des relais afin de recevoir et publier du contenu.

![Systeme de clef](assets/2.webp)

## 1. Les clés cryptographiques

Contrairement à Facebook ou Twitter, où l'utilisateur doit fournir une adresse courriel ainsi que de nombreuses informations personnelles à une entreprise privée, Nostr fonctionne sans autorité centrale.‌‌‌‌ L'utilisateur génère simplement une paire de clés cryptographiques, une clé secrète (aussi appelée clé privée) et une clé publique.

La clé secrète (nsec), connue uniquement de l'utilisateur, lui servira à s'authentifier et à publier du contenu.

La clé publique (npub), est un identifiant unique auquel tout le contenu publié par un utilisateur est rattaché. Ta clé publique est une sorte de nom d'utilisateur qui permet aux autres utilisateurs de te trouver et de s'abonner à ton fil Nostr.

## 2. Les clients

Les clients sont des logiciels qui permettent d'interagir avec Nostr. Les principaux clients sont :‌‌‌‌

- iOS: Damus
- Android: Amethyst
- Web: iris.to, snort.social, astral.ninja

Ils permettent de générer une nouvelle paire de clés (l'équivalent de se créer un compte) ou de s'authentifier avec une paire de clés préexistante.

## 3. Les relais

Les relais sont de simples serveurs auxquels vous pouvez vous connecter ou que vous pouvez abandonner à n'importe quel moment si le contenu transmis ne vous convient pas. Vous pouvez également exécuter votre propre relais, si vous le souhaitez.

> 💡 Truc de pro: Les relais payants sont généralement plus efficaces pour filtrer le spam et le contenu indésirable.

## Guide

Vous avez maintenant les bases nécessaires pour créer votre première identité sur Nostr.

Dans ce guide, nous utiliserons iris.to (https://iris.to/)  un client web qui fonctionne sur n'importe quelle plate-forme.

## Étape 1 : Génération des clés

Iris générera pour vous un jeu de clés sans que tu n'aies à faire rien de plus qu'entrer un nom (réel ou fictif) pour ton profil. Clique ensuite sur GO et le tour est joué!

![Main menu](assets/3.webp)

> ⚠️ Attention ! Tu devras garder une trace de tes clés si tu veux pouvoir accéder à nouveau à ton profil une fois ta session fermée. Je te montrerai comment faire à la toute fin de ce guide.

## Étape 2 : Publier un contenu

Pour publier un contenu, rien de plus simple et d'intuitif que d'écrire quelques mots dans le champ de publication.

![Publication](assets/4.webp)

Voilà, ça y est ! Tu as publié ta première note sur Nostr.

![Post](assets/5.webp)

## Étape 3 : Trouver un ami

Retrouve-moi sur Nostr et ne sois plus jamais seul. Je m’abonnerai en retour à toutes les personnes qui s'abonnent à mon fil. Pour ce faire, il te suffira d'entrer ma clé publique

npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 dans la barre de recherche.

![Mon profil](assets/6.webp)

Clique sur "follow" et d'ici quelques jours au plus, je m'abonnerai aussi à ton fil. Nous serons amis. Je serai aussi heureux de te lire si tu veux m'envoyer un message.

Finalement, assure-toi aussi de t'abonner au fil d'Agora256 pour recevoir une note chaque fois que nous publions quelque chose de nouveau : npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx

## Étape 4 : Personnalise ton profil

Il te reste encore un peu de travail pour personnaliser ton profil. Pour ce faire, clique sur l'avatar qu'iris a généré automatiquement pour toi dans le coin supérieur droit de l'écran puis clique sur "edit profil".

![Profile](assets/7.webp)

Il ne te reste plus qu'à indiquer à Iris où trouver ton image et ta bannière de profil sur les interwebs. Je te recommande d'héberger toi-même ton contenu : protège ce qui t'appartient.

![Autre option](assets/8.webp)

Si tu préfères, tu peux aussi télécharger des images, elles seront stockées pour toi par iris sur nostr.build, un service gratuit d'hébergement de contenu visuel pour Nostr.

Comme tu peux le constater, tu peux aussi configurer ton client pour être en mesure de recevoir et d'envoyer des sats. Ainsi tu pourras récompenser les auteurs de contenus que tu as aimés ou mieux encore, accumuler toi-même des sats pour le contenu formidable que tu vas publier.

## Étape 5 : Sauvegarde de la paire de clés

Cette étape est cruciale si tu veux conserver l'accès à ton profil une fois que tu te seras déconnecté du client ou que ta session aura expiré.

D'abord, clique sur l'icône "settings" représentée par un engrenage

![Setting](assets/9.webp)

Puis, copie-colle à tour de rôle tes npub, npub hex, nsec et nsec hex dans un fichier texte que tu garderas en sécurité. Je te recommande de crypter ce fichier, si tu sais comment le faire.

![Clef](assets/10.webp)

> ⚠️ Remarque bien l'avertissement que te donne iris. Si tu peux partager ta clé publique sans crainte, il en est tout autrement de ta clé privée. Quiconque possède cette dernière pourra accéder à ton compte.

## Conclusion

Ça y est, petite autruche, tu as fait tes premiers pas sur Nostr. Maintenant, il te faudra apprendre à courir à la vitesse de l'éclair. Nous publierons prochainement des guides qui te montreront à gérer tes clés et comment intégrer lightning à ton expérience Nostr à l'aide de getalby.
