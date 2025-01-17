---
name: Les bases de GitHub
description: Comprendre les bases de Git et GitHub
---

![cover](assets/cover.webp)

La mission de PlanB est de mettre à disposition des ressources éducatives de premier plan sur Bitcoin, et ce, dans un maximum de langues. L'intégralité des contenus publiés sur le site est open-source et est hébergée sur GitHub, ce qui offre la possibilité à quiconque de participer à l'enrichissement de la plateforme. Les contributions peuvent prendre diverses formes : correction et relecture des textes existants, traduction dans d'autres langues, mise à jour des informations ou encore création de nouveaux tutoriels encore absents de notre site.

Si vous souhaitez contribuer à PlanB Network, vous devrez utiliser Git et GitHub. Si ces outils vous sont inconnus ou si leur fonctionnement vous semble obscur, pas de panique, cet article est fait pour vous ! Nous allons revoir ensemble les fondamentaux de Git et de GitHub, ainsi que le jargon technique associé, pour vous permettre par la suite de prendre en main ces outils efficacement.

## C'est quoi Git ?

Git est un système de contrôle de version, spécialement conçu pour gérer des projets logiciels. Créé en 2005 par Linus Torvalds, Git est rapidement devenu la norme dans l'industrie du développement de logiciels pour le contrôle de version. Mais qu'est-ce que cela signifie exactement ?
![git](assets/1.webp)
À la base, Git permet aux développeurs de suivre les modifications apportées au code source d'un projet au fil du temps. Cela signifie qu'à chaque changement dans le code, Git enregistre une nouvelle version du projet. Si une erreur survient ou si une fonctionnalité expérimentale ne fonctionne pas comme prévu, il est possible de revenir à un état antérieur du code, comme une sorte de machine à remonter le temps pour les fichiers.

Une des fonctionnalités clés de Git est la gestion des branches. Une branche est une sorte de ligne parallèle où les développeurs peuvent travailler indépendamment du reste du projet. Cela facilite grandement l'ajout de nouvelles fonctionnalités ou la correction de bugs sans perturber le code principal. Une fois les modifications testées et validées, elles peuvent être fusionnées avec la branche principale.

Une des particularités de Git est sa capacité à fonctionner de manière distribuée. Chaque développeur possède une copie complète du projet sur le disque dur de son propre ordinateur, ce qui permet de travailler hors ligne et de fusionner les changements plus tard, lorsqu'une connexion Internet est disponible. Cela réduit le risque de conflits et permet à plusieurs développeurs de travailler simultanément sur le même projet sans se marcher sur les pieds.

Initialement, Git est donc principalement pensé pour les projets de développement logiciel. Cependant, il peut tout aussi bien servir à gérer des projets de rédaction de contenu. Plutôt que de collaborer sur du code, nous collaborons sur du texte. Et c'est justement cette méthode que PlanB Network a adoptée pour gérer ses contenus ! Git nous facilite la collaboration sur la rédaction de cours et de tutoriels, car il permet un suivi précis des modifications, une gestion efficace des versions et permet également la revue et l'amélioration du contenu par d'autres contributeurs. 

## C'est quoi GitHub ?

GitHub est une plateforme de gestion et d'hébergement de code source qui repose sur le système de contrôle de version Git dont nous venons de parler. Lancée en 2008, GitHub a rapidement gagné en popularité et est devenue une référence incontournable pour les développeurs du monde entier. Mais en quoi GitHub se distingue-t-il de Git et pourquoi est-il si essentiel dans notre méthode de production de contenu ?
![github](assets/2.webp)
Tout d'abord, il faut comprendre que GitHub repose sur Git (dont nous avons parlé dans la partie précédente). Alors que Git est l'outil qui permet de suivre les modifications du code, GitHub est le service en ligne qui permet d'héberger, de partager et de gérer ce code.

Imaginez que Git est comme une sorte de carnet de bord que chaque développeur utilise sur son propre ordinateur pour enregistrer toutes les modifications de son projet. GitHub, quant à lui, est comme une bibliothèque publique où tous ces carnets de bord peuvent être partagés, comparés et combinés.

La différence fondamentale entre Git et GitHub réside donc dans leur fonction : Git est l'outil utilisé localement par chaque développeur pour gérer les versions de leur code, tandis que GitHub est la plateforme en ligne qui héberge ces versions et facilite la collaboration.

GitHub est donc bien plus qu'un simple hébergeur de code. C'est une plateforme de collaboration qui permet aux développeurs de travailler ensemble efficacement. Et justement, PlanB Network utilise cette plateforme pour héberger à la fois tout le code qui permet de faire tourner le site web, mais également, et c'est ce qui nous intéresse, tous les contenus (tutoriels, formations, ressources...).

## Quelques termes techniques

Sur Git et GitHub, vous rencontrerez des commandes et des fonctionnalités dont les noms peuvent sembler complexes. Dans cette dernière partie, je vous donne des définitions simples à comprendre des termes techniques que vous pourriez croiser lors de votre utilisation de Git et GitHub :

- **Fetch origin :** Commande qui permet de récupérer les informations et les modifications récentes d'un dépôt distant sans les fusionner avec votre travail local. Elle met à jour votre dépôt local avec les nouvelles branches et les nouveaux commits présents sur le dépôt distant.

- **Pull origin :** Commande qui permet de récupérer les mises à jour d'un dépôt distant et de les intégrer immédiatement à votre branche locale afin de la synchroniser. Cela combine les étapes de fetch et de merge en une seule commande.

- **Sync Fork :** Fonctionnalité sur GitHub qui permet de mettre à jour votre fork d'un projet avec les dernières modifications du dépôt source. Cela assure que votre copie du projet reste à jour avec le développement principal.

- **Push origin :** Commande qui sert à envoyer vos modifications locales à un dépôt distant.

- **Pull Request :** Demande envoyée par un contributeur pour indiquer qu'il a poussé des modifications sur une branche dans un dépôt distant et qu'il souhaite que ces modifications soient examinées et potentiellement intégrées (merge) dans la branche principale du dépôt.

- **Commit :** Sauvegarde de vos modifications. Un commit est comme une photo instantanée de votre travail à un moment donné, qui permet de garder un historique des changements. Chaque commit inclut un message descriptif expliquant ce qui a été modifié.

- **Branche :** Version parallèle du dépôt, permettant de travailler sur des modifications sans affecter la branche principale (souvent appelée "main" ou "master"). Les branches facilitent le développement de nouvelles fonctionnalités et la correction de bugs sans risque de perturber le code stable.

- **Merge :** Fusionner consiste à intégrer les modifications d'une branche dans une autre. On l'utilise, par exemple, pour ajouter les modifications d'une branche de travail sur la branche principale, ce qui permet d'ajouter les différentes contributions.

- **Fork :** Faire un fork d'un dépôt consiste à créer une copie de ce dépôt sur votre propre compte GitHub, ce qui vous permet de travailler sur le projet sans affecter le dépôt original. Le fork peut soit faire son propre chemin, et devenir un projet différent du projet initial, soit se synchroniser régulièrement avec le projet initial, afin d'y contribuer.

- **Clone :** Cloner un dépôt signifie en faire une copie locale sur votre ordinateur, ce qui vous donne accès à tous les fichiers et à l'historique. Cela vous permet de travailler sur le projet directement en local.

- **Repository :** Espace de stockage pour un projet sur GitHub. Un dépôt contient tous les fichiers du projet ainsi que l'historique de toutes les modifications qui y ont été apportées. C'est la base de stockage et de collaboration sur GitHub.

- **Issue :** Outil de suivi des tâches et des bugs sur GitHub. Les issues permettent de signaler des problèmes, de proposer des améliorations ou de discuter de nouvelles fonctionnalités. Chaque issue peut être assignée, étiquetée et commentée.

Cette liste n'est évidemment pas exhaustive. Il existe de nombreux autres termes techniques spécifiques à Git et GitHub. Cependant, ceux mentionnés ici sont les principaux que vous rencontrerez fréquemment.

Après avoir lu cet article, il est possible que certains aspects de Git et GitHub restent encore flous pour vous. Je vous encourage à commencer à utiliser ces outils par vous-même. La pratique est souvent le meilleur moyen pour comprendre le fonctionnement de la machine ! Et pour commencer, vous pouvez découvrir ces 2 autres tutoriels :
**[Créer son compte GitHub](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Mettre en place son environnement local pour contribuer à PlanB Network](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**
