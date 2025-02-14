---
name: Contribution - Tutoriels
description: Comment proposer un nouveau contenu sur Plan ₿ Network ?
---
![cover](assets/cover.webp)

La mission de Plan ₿ Network est de mettre à disposition des ressources éducatives de premier plan sur Bitcoin, et ce, dans un maximum de langues. L'intégralité des contenus publiés sur le site est open-source et est hébergée sur GitHub, ce qui offre la possibilité à quiconque de participer à l'enrichissement de la plateforme. Les contributions peuvent prendre diverses formes : correction et relecture des textes existants, traduction dans d'autres langues, mise à jour des informations ou encore création de nouveaux tutoriels encore absents de notre site.

Dans ce tutoriel, nous allons voir comment ajouter un nouveau contenu, tel qu'un tutoriel ou un cours, sur la plateforme Plan ₿ Network.

## Quelle est la différence entre un tutoriel et un cours ?

Les deux principales sections de notre plateforme sont les cours et les tutoriels. Les cours fournissent des ressources éducatives théoriques, tandis que les tutoriels offrent des contenus pratiques montrant comment utiliser un outil spécifique (par exemple, un hardware wallet ou un logiciel) ou une pratique particulière (comme sécuriser une phrase mnémonique ou vérifier l'authenticité d'un logiciel).

Les cours sont naturellement plus longs et plus structurés que les tutoriels. Ils doivent explorer un sujet spécifique lié à Bitcoin ou à son écosystème de manière approfondie, précise et détaillée.

[Découvrir les cours de Plan ₿ Network.](https://planb.network/courses)

![TUTO](assets/fr/37.webp)

Les tutoriels sont généralement plus courts. Ils doivent servir de guides expliquant étape par étape comment réaliser une tâche spécifique en lien avec Bitcoin, avec des images comme support.

[Découvrir les tutoriels de Plan ₿ Network.](https://planb.network/tutorials)

![TUTO](assets/fr/38.webp)

## Comment proposer un nouveau cours ?

Si vous avez une idée de cours sur Bitcoin qui n'est pas encore présent sur la plateforme et que vous souhaitez le rédiger, vous pouvez nous contacter à l'adresse suivante :

contact@planb.network

Dans votre message, veuillez vous présenter brièvement et décrire votre idée de cours. Si vous avez déjà une idée de structure pour votre cours, incluez également les différents chapitres prévus. Nous vous répondrons rapidement pour vous expliquer la marche à suivre et, éventuellement, discuter de la structure de votre cours.

## Comment proposer un nouveau tutoriel ?

Pour ajouter un nouveau tutoriel sur Plan ₿ Network, vous pouvez le faire directement sur GitHub en soumettant une Pull Request. Dans le tutoriel ci-dessous et les tutoriels attenants, je vous guide pas à pas à travers ce processus et vous informe des lignes directrices à respecter pour assurer la compatibilité de votre tutoriel avec la plateforme, tout en maintenant un historique de contributions clair.

## 1 - Choisir le thème de votre tutoriel

Nous recherchons en priorité des tutoriels sur des outils liés à Bitcoin ou à son écosystème. Ces contenus peuvent s'articuler autour de six catégories principales :
- Portefeuille ;
- Nœud ;
- Minage ;
- Marchand ;
- Échange ;
- Confidentialité.

Au-delà de ces sujets spécifiquement liés à Bitcoin, Plan ₿ Network cherche également des contributions sur des thèmes qui mettent en avant la souveraineté individuelle, tels que :
- Les outils open sources ;
- L'informatique ;
- La cryptographie ;
- L'énergie ;
- Les mathématiques ;
- L'économie ;
- Les DIY ;
- Le LifeHacking...

Par exemple, nous avons actuellement des tutoriels sur Tails, Nostr ou encore GrapheneOS. Ces outils ne sont pas directement en rapport avec Bitcoin, mais ce sont des systèmes qui peuvent nous intéresser dans une démarche de souveraineté dans le monde du numérique. Ces contenus peuvent être intégrés dans une sous-catégorie de la section "Autres".

Vous avez le choix entre concevoir un tutoriel de zéro ou reprendre un tutoriel préalablement publié sur votre site web (à condition d'en détenir les droits d'auteur) pour le partager également sur Plan ₿ Network, en y ajoutant un lien vers l'article d'origine.

Quel que soit votre choix, gardez à l'esprit que tous les contenus publiés sur Plan ₿ Network sont sous la licence libre [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). Cette licence autorise quiconque à copier et, potentiellement, à modifier votre contenu, à la seule condition que la source originale soit dûment créditée.

## 2 - Prendre contact avec l'équipe de Plan ₿ Network

Une fois que vous avez choisi le thème de votre tutoriel, la prochaine étape consiste à nous informer de votre intention d'ajouter ce contenu sur la plateforme. La méthode la plus simple, si vous disposez d'un compte Telegram, est de [rejoindre notre groupe](https://t.me/PlanBNetwork_ContentBuilder).

![TUTO](assets/fr/39.webp)

Présentez-vous brièvement et précisez le contenu spécifique que vous souhaitez rédiger ainsi que la langue de rédaction, en envoyant un message dans le canal "General". Un membre de l’équipe créera ensuite une issue sur GitHub correspondant à votre future contribution.

Si vous n'avez pas de compte Telegram et que vous préférez ne pas en créer un, vous pouvez également nous contacter par email à l'adresse suivante :

paolo@planb.network

## 3 - Choisir ses outils pour contribuer

Pour contribuer sur Plan ₿ Network, vous avez 3 options selon votre niveau d'expérience avec GitHub :

- **Utilisateurs expérimentés** : Continuez avec vos méthodes habituelles et consultez simplement le court tutoriel ci-dessous qui résume la structure des fichiers du dépôt de Plan ₿ Network, les exigences spécifiques et la méthode de travail :

https://planb.network/tutorials/others/contribution/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410

- **Intermédiaire (GitHub Desktop)** : Si vous n'êtes pas familier avec l'utilisation de Git, la première option consiste à configurer facilement votre propre environnement local pour contribuer sur Plan ₿ Network. Cette approche est recommandée pour les contributions significatives, telles que la rédaction d'un tutoriel complet. Pour ce faire, suivez pas à pas le tutoriel détaillé ci-dessous :

https://planb.network/tutorials/others/contribution/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

- **Débutants (interface web)** : Vous pouvez également opter pour l'utilisation directe de l'interface web de GitHub, sans nécessiter la configuration d'un environnement local complet. Cette méthode peut être envisagée pour des contributions mineures. Cependant, pour des contributions majeures, telles que l'ajout d'un nouveau tutoriel complet, cette option peut s'avérer plus complexe que la configuration d'un environnement local. Je vous explique tout de même comment le faire dans ce tutoriel :

https://planb.network/tutorials/others/contribution/write-tutorials-github-web-beginner-e64f8fed-4c0b-4225-9ebb-7fc5f1c01a79

Choisissez l'une de ces trois options en fonction de votre niveau de connaissances, puis lancez-vous dans la rédaction de votre premier tutoriel sur Plan ₿ Network !
