---
name: Phrase mnémonique - Lancé de dés
description: Comment générer soi-même sa phrase de récupération avec des dés ?
---
![cover](assets/cover.jpeg)

Ce tutoriel a pour but de vous expliquer comment construire manuellement une phrase de récupération pour un portefeuille Bitcoin en utilisant des lancés de dés.

**ATTENTION :** La génération d'une phrase mnémonique de manière sécurisée exige de ne laisser aucune trace numérique pendant sa création, ce qui s'avère presque infaisable. À défaut, le portefeuille présenterait une surface d'attaque bien trop grande, ce qui augmenterait fortement le risque de vol de vos bitcoins. **Il est donc fortement déconseillé de transférer des fonds sur un portefeuille qui dépend d'une phrase de récupération que vous avez vous-même générée.** Même si vous suivez ce tutoriel à la lettre, il existe un risque que la phrase de récupération soit compromise. **Ce tutoriel ne doit pas être appliqué à la création d'un véritable portefeuille.** Utiliser un hardware wallet pour cette tâche est bien moins risqué, car il génère la phrase hors-ligne, et de vrais cryptographes ont réfléchi à l'utilisation de sources d'entropie qualitatives.

Ce tutoriel peut être suivi à titre expérimental uniquement pour la création d'un portefeuille fictif, sans intention de l'utiliser avec de réels bitcoins. Toutefois, l'expérience vous offre deux bénéfices :
- Premièrement, cela vous permet de mieux comprendre les mécanismes à la base de votre portefeuille Bitcoin ;
- Secondement, cela vous permet de savoir le faire. Je ne dis pas que ça vous sera utile un jour, mais ça peut !

## C'est quoi une phrase mnémonique ?
Une phrase de récupération, également parfois nommée "mnémonique", "seed phrase", ou "phrase secrète", est une séquence composée habituellement de 12 ou 24 mots, qui est générée de manière pseudo-aléatoire à partir d'une source d'entropie. La séquence pseudo-aléatoire est toujours complétée d'une somme de contrôle (checksum).

La phrase mnémonique, conjointement avec une passphrase optionnelle, est utilisée pour dériver de façon déterministe l'intégralité des clés associées à un portefeuille HD (déterministe et hiérarchique). Cela signifie qu’à partir de cette phrase, il est possible de générer et de recréer déterministiquement l'ensemble des clés privées et publiques du portefeuille Bitcoin, et par conséquent, d'accéder aux fonds qui y sont associés. 

L'utilité de cette phrase est de fournir un moyen de sauvegarde et de récupération des bitcoins facile à utiliser. Il est impératif de conserver cette phrase en lieu sûr et de manière sécurisée, car toute personne en possession de cette phrase aurait accès aux fonds du portefeuille correspondant. Si elle est utilisée dans le cadre d’un portefeuille classique, et sans passphrase optionnelle, elle constitue souvent un SPOF (point de défaillance unique). 

Habituellement, cette phrase vous est donnée directement lors de la création de votre portefeuille, par le logiciel ou le hardware wallet. Cependant, il est aussi possible de générer cette phrase par vous-même, pour ensuite la saisir sur le support choisi afin de dériver les clés du portefeuille. C'est ce que nous allons voir dans ce tutoriel.

## Préparation du matériel nécessaire
Pour la création de votre phrase de récupération, vous aurez besoin de :
- Une feuille de papier ;
- Un stylo ou un crayon, idéalement de couleurs différentes pour faciliter l'organisation ;
- Plusieurs dés, afin de minimiser les risques de biais liés à un dé déséquilibré ;
- [La liste des 2048 mots du BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt).

Par la suite, l'usage d'un ordinateur avec un terminal deviendra nécessaire pour le calcul de la somme de contrôle (checksum). C'est précisément pour cette raison que je déconseille la génération manuelle de la phrase mnémonique. À mon sens, l'intervention d'un ordinateur, même sous les précautions mentionnées dans ce tutoriel, accroît de manière significative la vulnérabilité d'un portefeuille.

Pour une démarche expérimentale concernant un "portefeuille fictif", il est possible d'utiliser votre ordinateur habituel et à son terminal. Cependant, pour une approche plus rigoureuse visant à limiter les risques de compromission de votre phrase, l'idéal serait d'utiliser un PC déconnecté d'internet (de préférence sans composant wifi ni connexion filaire RJ45), équipé du minimum de périphériques (tous devant être connectés par câble, évitant le bluetooth), et surtout, fonctionnant sous une distribution Linux amnésique telle que [Tails](https://tails.boum.org/index.fr.html), démarrée depuis un support externe.

Dans un contexte réel, il serait primordial de garantir la confidentialité de votre espace de travail en choisissant un lieu à l'abri des regards, sans circulation de personnes et exempt de caméras (webcams, téléphones...).

Il est conseillé d'utiliser un nombre élevé de dés pour atténuer l'impact d'un dé éventuellement déséquilibré sur l'entropie. Avant leur utilisation, une vérification des dés est recommandée : cela peut être réalisé en les testant dans un bol d'eau fortement salée, permettant ainsi aux dés de flotter. Procédez ensuite à une vingtaine de lancers pour chaque dé dans l'eau salée, en observant les résultats. Si une ou deux faces apparaissent de manière disproportionnée par rapport aux autres, prolongez le test avec davantage de lancers. Des résultats uniformément répartis indiquent que le dé est fiable. Cependant, si une ou deux faces dominent régulièrement, ces dés doivent être mis de côté, car ils pourraient compromettre l'entropie de votre phrase mnémonique et, par conséquent, la sécurité de votre portefeuille.

Dans des conditions réelles, après avoir effectué ces vérifications, vous seriez prêt à générer l'entropie nécessaire. Pour un portefeuille expérimental fictif réalisé dans le cadre de ce tutoriel, vous pourriez naturellement omettre ces préparatifs.
