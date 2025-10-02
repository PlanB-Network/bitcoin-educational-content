---
name: Seedkeeper - Password Manager
description: Comment sauvegarder vos mots de passe avec la carte à puce Seedkeeper ?
---

![cover](assets/cover.webp)

Le Seedkeeper est une carte à puce développée par Satochip, une entreprise belge spécialisée dans les solutions matérielles pour la gestion et la protection des secrets numériques. Reconnue pour sa gamme de smartcards destinées à l’écosystème Bitcoin, Satochip a conçu le Seedkeeper comme une alternative aux méthodes traditionnelles de conservation de phrases mnémoniques, et de tout autre secret numérique.

Concrètement, le Seedkeeper prend la forme d’une carte à puce multifonctionnelle, certifiée EAL6, dotée d’un processeur sécurisé et d’une mémoire inviolable (c'est donc ce que l'on appelle un "Secure Element"). Comme son nom l'indique, son rôle est de stocker de manière chiffrée et protégée des phrases mnémoniques de portefeuilles Bitcoin ainsi que des mots de passe. Avec le Seedkeeper, vous pouvez générer, importer, organiser et sauvegarder vos secrets directement dans le composant sécurisé de la carte.

Le Seedkeeper répond donc selon moi à deux cas d’utilisation principaux que nous étudierons en 2 tutoriels distincs :
- **La conservation de phrases mnémoniques Bitcoin** : au lieu de noter vos 12 ou 24 mots sur un support papier, vous pouvez les importer dans la smartcard et les protéger par un code PIN.
- **La gestion de mots de passe** : vous pouvez générer des mots de passe forts via l’application Seedkeeper et les stocker directement dans la smartcard, ce qui donne un gestionnaire de mots de passe sécurisé hors ligne pratique et facile à utiliser.

Sur le plan technique, le Seedkeeper offre une capacité de 8192 octets, ce qui permet de stocker au minimum 50 secrets distincts (le nombre exact dépendra de leur taille et des métadonnées associées à chacun). L’accès au Seedkeeper se fait soit [par lecteur de carte à puce relié](https://satochip.io/accessories/) à un ordinateur, soit via l’application mobile avec connexion NFC. Le tout fonctionne en mode hors ligne, sans connexion Internet, ce qui garantit une surface d’attaque limitée.

001

Une fonctionnalité particulièrement intéressante est la possibilité de dupliquer le contenu d’un Seedkeeper vers un autre afin de créer une sauvegarde. Nous allons voir dans ce tutoriel comment faire cette manipulation.

Dans ce tutoriel, nous traiterons uniquement de l’utilisation du SeedKeeper pour des mots de passe traditionnels, à la manière d’un gestionnaire de mots de passe. Si vous souhaitez utiliser le SeedKeeper pour sauvegarder des phrases mnémoniques de portefeuilles Bitcoin, je vous conseille de consulter cet autre tutoriel :

https://planb.network/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Comment obtenir un Seedkeeper ?

Il existe principalement deux façons d’obtenir votre Seedkeeper. Vous pouvez l’[acheter directement sur la boutique officielle](https://satochip.io/product/seedkeeper/) de Satochip ou auprès d’un revendeur agréé. Mais puisque [l’applet du Seedkeeper est open-source](https://github.com/Toporin/Seedkeeper-Applet), vous avez également la possibilité de l’installer vous-même sur [une carte à puce vierge](https://satochip.io/product/blank-javacard-for-diy-project/).

Si vous souhaitez utiliser la fonctionnalité de sauvegarde du Seedkeeper, il vous faudra évidemment acquérir deux smartcards.

## 2. Installer le client Seedkeeper

La première étape consiste à installer le logiciel sur votre ordinateur ou votre smartphone. Sur PC, vous devrez [télécharger la dernière version de Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). Sur mobile, l’application Seedkeeper est disponible sur le [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) ainsi que sur l’[App Store Apple](https://apps.apple.com/be/app/seedkeeper/id6502836060).

002

## 3. Initialisation du Seedkeeper

Lancez l’application et cliquez sur le bouton "Click & Scan".

003

Un code PIN vous est demandé pour votre Seedkeeper. Comme il s’agit d’une nouvelle carte, aucun PIN n’a encore été défini. Entrez donc un code quelconque pour passer cette étape, puis cliquez sur "Suivant".

004

Placez ensuite la carte à l’arrière de votre smartphone. L’application détectera que le Seedkeeper n’est pas encore initialisé et vous invitera à définir le code PIN de votre carte à puce, compris entre 4 et 16 caractères. Pour une sécurité optimale, choisissez un code PIN robuste, le plus long possible, aléatoire et composé d’une grande diversité de caractères. Ce code PIN constitue la seule barrière de protection contre un accès physique à vos mots de passe.

**Pensez également à sauvegarder ce code PIN dès maintenant**, par exemple dans un gestionnaire de mots de passe, ou bien sur un support physique distinct. Dans ce dernier cas, ne conservez jamais le support contenant le PIN au même endroit que votre Seedkeeper, sans quoi cette sécurité deviendrait inutile. Il est important de disposer d’une sauvegarde fiable : sans ce code PIN, il vous sera impossible de récupérer les secrets enregistrés sur votre Seedkeeper.

005

Confirmez votre code PIN une seconde fois.

006

Votre Seedkeeper est désormais initialisé. Vous pouvez le déverrouiller en entrant le code PIN que vous venez de définir.

007

Vous accédez maintenant à la page de gestion de votre carte à puce.

008

## 4. Enregistrer des mots de passe sur le Seedkeeper

Une fois votre Seedkeeper déverrouillé, cliquez sur le bouton "+".

009

Sélectionnez "Générer un secret". L’option "Importer un secret" permet quant à elle d'enregistrer un secret déjà existant (par exemple, un mot de passe que vous aviez déjà créé par le passé).

010

Dans notre cas, nous voulons sauvegarder un mot de passe. Cliquez donc sur "Mot de passe".

011

Attribuez un "Label" à ce secret afin de l’identifier facilement si vous enregistrez plusieurs informations dans votre Seedkeeper. Vous pouvez également ajouter un identifiant associé au mot de passe et l'URL du site.

012

Choisissez ensuite la longueur et les paramètres de votre mot de passe, puis cliquez sur le bouton "Générer", puis "Importer".

013

Placez votre Seedkeeper à l’arrière de votre smartphone.

014

Votre mot de passe a bien été enregistré.

015

## 5. Accéder à votre mot de passe sur le Seedkeeper

Si vous souhaitez consulter votre mot de passe, prenez votre Seedkeeper et cliquez sur le bouton "Click & Scan".

016

Saisissez votre code PIN puis appuyez sur "Suivant".

017

Placez votre Seedkeeper à l’arrière du smartphone.

018

Vous accédez alors à la liste de tous vos secrets enregistrés. Dans cet exemple, je veux afficher le mot de passe de mon compte sur Plan ₿ Network, je clique donc dessus.

019

Appuyez sur le bouton "Révéler".

020

Scannez de nouveau votre Seedkeeper.

021

Votre mot de passe précédemment enregistré s’affiche désormais à l’écran. Vous pouvez le copier pour l'utiliser sur le site web concerné.

022

## 6. Faire une sauvegarde du Seedkeeper

Nous allons maintenant réaliser une sauvegarde de mon Seedkeeper sur un second Seedkeeper afin d’en avoir deux exemplaires. Cette redondance peut faire partie d’une stratégie de sécurisation de vos mots de passe les plus importants : par exemple, stocker vos Seedkeepers à 2 endroits distincts pour limiter les risques physiques, ou encore en confier une copie à un proche de confiance.

Pour cela, munissez-vous de votre second Seedkeeper (pensez à identifier l’un des deux avec une marque dessus pour éviter toute confusion). Commencez par l’initialiser en reproduisant le processus de l’étape 3 de ce tutoriel. Choisissez une nouvelle fois un code PIN fort. Selon votre stratégie, vous pouvez opter pour un PIN différent ou conserver le même.

023

Ouvrez l’application, cliquez sur "Click & Scan", saisissez le PIN de votre Seedkeeper n°1 (source), puis scannez-le.

024

Vous accédez à sa page d’accueil avec la liste de vos secrets. Cliquez sur les trois petits points en haut à droite de l'interface.

025

Sélectionnez "Faire une sauvegarde", puis appuyez sur "Start".

026

Saisissez le code PIN de votre carte de sauvegarde (Seedkeeper n°2).

027

Scannez ensuite cette carte.

028

Faites de même avec la carte principale (Seedkeeper n°1), puis cliquez sur "Faire une sauvegarde".

029

Votre Seedkeeper n°2 contient désormais l’intégralité des secrets enregistrés sur le Seedkeeper n°1.

030

Vous pouvez scanner votre Seedkeeper n°2 pour vérifier que les secrets ont bien été copiés.

031

Voilà ! Vous savez désormais comment utiliser le Seedkeeper pour stocker vos mots de passe. Dans un prochain tutoriel, nous verrons comment utiliser le Seedkeeper pour faire une sauvegarde d'un portefeuille Bitcoin. Je vous invite également à découvrir son usage combiné avec le SeedSigner :

https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.network/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356
