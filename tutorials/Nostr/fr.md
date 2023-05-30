# Comment utiliser Nostr en 2023 : Un guide pour débutant

‌‌À la fin de ce guide, tu comprendras ce qu'est Nostr, tu te seras créé un compte et tu seras en mesure de l'utiliser.

** Ce guide vous est offert par FranklynHart dans le cadre de Agora256. Merci à lui **


![Un nouveau challenger est arrivé](1)

## Qu'est-ce que Nostr?

Nostr est un protocole qui a le pouvoir de remplacer twitter, Telegram et les autres médias sociaux.‌‌‌‌ Il s'agit d'un protocole ouvert simple et capable de créer une fois pour toutes un réseau social mondial résistant à la censure.

## Comment ça fonctionne?

Nostr repose sur trois composantes : des paires de clés, des clients et des relais.

Chaque utilisateur possède une ou plusieurs identités, chaque identité est déterminée par une paire de clés cryptographiques.

Pour accéder au réseau, il faut utiliser un logiciel client et se connecter à des relais pour recevoir et émettre du contenu.

![systeme de clef](2)

## 1. Les clés cryptographiques

Contrairement à Facebook ou Twitter où l'utilisateur doit fournir une adresse courriel et une pléthore d'informations à une entreprise privée, Nostr fonctionne en l'absence d'une autorité centrale.‌‌‌‌ L'utilisateur génère une paire de clés cryptographiques, une clé secrète (aussi appelée clé privée) et une clé publique.

La clé secrète, nsec, connue seulement de l'utilisateur, lui servira à s'authentifier et à publier du contenu.

La clé publique, npub, est un identifiant unique auquel est attaché tout le contenu publié par un utilisateur. Ta clé publique est une sorte de nom d'utilisateur qui permet aux autres utilisateurs de te trouver et de s'abonner à ton fil Nostr.

## 2. Les clients

Les clients sont des logiciels qui permettent d'interagir avec Nostr.  Les principaux clients sont :‌‌‌‌

    iOS : damus
    Android : amethyst
    Web : iris.to; snort.social; astral.ninja

Les clients permettent à un utilisateur de générer une nouvelle paire de clés (l'équivalent de se créer un compte) ou de s'authentifier avec une paire de clés préexistante.

## 3. Les relais

Les relais sont des serveurs simplistes que tu peux abandonner à n'importe quel moment si tu n'aimes pas le contenu qu'ils t'acheminent. Tu peux également rouler ton propre relais, si tu le souhaites. 

    💡 Truc de pro: Les relais payants sont généralement plus efficaces pour filtrer le spam et le contenu indésirable.

# Guide

Voilà, tu en connais assez sur Nostr pour te lancer et créer ta première identité sur ce protocole.

Pour les fins de ce guide, nous utiliserons iris.to (https://iris.to/) puisque ce client web fonctionne sur n'importe quelle plate-forme.

## Étape 1 : Génération des clés