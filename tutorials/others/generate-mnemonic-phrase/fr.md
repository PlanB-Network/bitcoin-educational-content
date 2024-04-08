---
name: Phrase mnémonique - Lancé de dés
description: Comment générer soi-même sa phrase de récupération avec des dés ?
---
![cover](assets/cover.jpeg)

Dans ce tutoriel, vous allez apprendre comment construire manuellement une phrase de récupération pour un portefeuille Bitcoin en utilisant des lancés de dés.

**ATTENTION :** La génération d'une phrase mnémonique de manière sécurisée exige de ne laisser aucune trace numérique pendant sa création, ce qui s'avère presque infaisable. À défaut, le portefeuille présenterait une surface d'attaque bien trop grande, ce qui augmenterait fortement le risque de vol de vos bitcoins. **Il est donc fortement déconseillé de transférer des fonds sur un portefeuille qui dépend d'une phrase de récupération que vous avez vous-même générée.** Même si vous suivez ce tutoriel à la lettre, il existe un risque que la phrase de récupération soit compromise. **Ce tutoriel ne doit pas être appliqué à la création d'un véritable portefeuille.** Utiliser un hardware wallet pour cette tâche est bien moins risqué, car il génère la phrase hors-ligne, et de vrais cryptographes ont réfléchi à l'utilisation de sources d'entropie qualitatives.

Ce tutoriel peut être suivi à titre expérimental uniquement pour la création d'un portefeuille fictif, sans intention de l'utiliser avec de réels bitcoins. Toutefois, l'expérience vous offre deux bénéfices :
- Premièrement, cela vous permet de mieux comprendre les mécanismes à la base de votre portefeuille Bitcoin ;
- Secondement, cela vous permet de savoir le faire. Je ne dis pas que ça vous sera utile un jour, mais ça peut !

## C'est quoi une phrase mnémonique ?
Une phrase de récupération, également parfois nommée "mnémonique", "seed phrase", ou "phrase secrète", est une séquence composée habituellement de 12 ou 24 mots, qui est générée de manière pseudo-aléatoire à partir d'une source d'entropie. La séquence pseudo-aléatoire est toujours complétée d'une somme de contrôle (checksum).

La phrase mnémonique, conjointement avec une passphrase optionnelle, est utilisée pour dériver de façon déterministe l'intégralité des clés associées à un portefeuille HD (déterministe et hiérarchique). Cela signifie qu’à partir de cette phrase, il est possible de générer et de recréer déterministiquement l'ensemble des clés privées et publiques du portefeuille Bitcoin, et par conséquent, d'accéder aux fonds qui y sont associés. 
![mnemonic](assets/fr/1.webp)
L'utilité de cette phrase est de fournir un moyen de sauvegarde et de récupération des bitcoins facile à utiliser. Il est impératif de conserver cette phrase en lieu sûr et de manière sécurisée, car toute personne en possession de cette phrase aurait accès aux fonds du portefeuille correspondant. Si elle est utilisée dans le cadre d’un portefeuille classique, et sans passphrase optionnelle, elle constitue souvent un SPOF (point de défaillance unique). 

Habituellement, cette phrase vous est donnée directement lors de la création de votre portefeuille, par le logiciel ou le hardware wallet. Cependant, il est aussi possible de générer cette phrase par vous-même, pour ensuite la saisir sur le support choisi afin de dériver les clés du portefeuille. C'est ce que nous allons voir dans ce tutoriel.

## Préparation du matériel nécessaire
Pour la création de votre phrase de récupération, vous aurez besoin de :
- Une feuille de papier ;
- Un stylo ou un crayon, idéalement de couleurs différentes pour faciliter l'organisation ;
- Plusieurs dés, afin de minimiser les risques de biais liés à un dé déséquilibré ;
- [La liste des 2048 mots du BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt) imprimée.

Par la suite, l'usage d'un ordinateur avec un terminal deviendra nécessaire pour le calcul de la somme de contrôle (checksum). C'est précisément pour cette raison que je déconseille la génération manuelle de la phrase mnémonique. À mon sens, l'intervention d'un ordinateur, même sous les précautions mentionnées dans ce tutoriel, accroît de manière significative la vulnérabilité d'un portefeuille.

Pour une démarche expérimentale concernant un "portefeuille fictif", il est possible d'utiliser votre ordinateur habituel et son terminal. Cependant, pour une approche plus rigoureuse visant à limiter les risques de compromission de votre phrase, l'idéal serait d'utiliser un PC déconnecté d'internet (de préférence sans composant wifi ni connexion filaire RJ45), équipé du minimum de périphériques (tous devant être connectés par câble, afin d'éviter le bluetooth), et surtout, fonctionnant sous une distribution Linux amnésique telle que [Tails](https://tails.boum.org/index.fr.html), démarrée depuis un support amovible.

![mnemonic](assets/fr/2.webp)

Dans un contexte réel, il serait primordial de garantir la confidentialité de votre espace de travail en choisissant un lieu à l'abri des regards, sans circulation de personnes et exempt de caméras (webcams, téléphones...).

Il est conseillé d'utiliser un nombre élevé de dés pour atténuer l'impact d'un dé éventuellement déséquilibré sur l'entropie. Avant leur utilisation, une vérification des dés est recommandée : cela peut être réalisé en les testant dans un bol d'eau saturée en sel, permettant ainsi aux dés de flotter. Procédez ensuite à une vingtaine de lancers pour chaque dé dans l'eau salée, en observant les résultats. Si une ou deux faces apparaissent de manière disproportionnée par rapport aux autres, prolongez le test avec davantage de lancers. Des résultats uniformément répartis indiquent que le dé est fiable. Cependant, si une ou deux faces dominent régulièrement, ces dés doivent être mis de côté, car ils pourraient compromettre l'entropie de votre phrase mnémonique et, par conséquent, la sécurité de votre portefeuille.

Dans des conditions réelles, après avoir effectué ces vérifications, vous seriez prêt à générer l'entropie nécessaire. Pour un portefeuille expérimental fictif réalisé dans le cadre de ce tutoriel, vous pourriez naturellement omettre ces préparatifs.

## Quelques rappels sur la phrase de récupération
Pour commencer, nous allons réviser les fondamentaux de la création d'une phrase de récupération selon le BIP39. Comme expliqué précédemment, la phrase est issue d'une information pseudo-aléatoire d'une certaine taille, à laquelle on ajoute une somme de contrôle pour assurer son intégrité.

La taille de cette information initiale, souvent désignée sous le terme "entropie", est déterminée par le nombre de mots que l'on souhaite obtenir dans la phrase de récupération. Les formats les plus courants sont les phrases de 12 et de 24 mots, dérivant respectivement d'une entropie de 128 bits et de 256 bits. Voici donc un tableau de correspondance des différentes tailles d'entropie selon le BIP39 :

| Nombre de mots | Entropie (bits) | Checksum (bits) | Entropie + Checksum (bits) |
| -------------- | --------------- | --------------- | -------------------------- |
| 12             | 128             | 4               | 132                        |
| 15             | 160             | 5               | 165                        |
| 18             | 192             | 6               | 198                        |
| 21             | 224             | 7               | 231                        |
| 24             | 256             | 8               | 264                        |
L'entropie est donc un nombre aléatoire entre 128 et 256 bits. Dans ce tutoriel, nous allons prendre l'exemple d'une phrase de 12 mots, dans laquelle l'entropie est de 128 bits, c'est-à-dire que nous allons générer une séquence aléatoire de 128 `0` ou `1`. Cela représente un nombre composé de 128 chiffres en base 2 (binaire).

Sur la base de cette entropie, on va générer une somme de contrôle. Une somme de contrôle est une valeur calculée à partir d'un ensemble de données, utilisée pour vérifier l'intégrité et la validité de ces données lors de leur transmission ou de leur stockage. Les algorithmes de somme de contrôle sont conçus pour détecter des erreurs accidentelles ou des altérations involontaires des données, comme les erreurs de transmission ou les corruptions de fichiers.

Dans le cas de notre phrase de récupération, la somme de contrôle a pour fonction de repérer toute erreur de saisie lorsque l'on entre la phrase dans un logiciel de portefeuille. Une somme de contrôle invalide signale la présence d'une erreur dans la phrase. À l'inverse, une somme de contrôle valide indique que la phrase est très probablement correcte.

Pour obtenir cette somme de contrôle, l'entropie est passée dans la fonction de hachage SHA256. Cette opération produit une séquence de 256 bits en sortie, parmi lesquels seuls les `N` premiers bits seront conservés, `N` dépendant de la longueur de la phrase de récupération voulue (voir le tableau ci-dessus). Ainsi, pour une phrase de 12 mots, ce sont les 4 premiers bits du hachage qui seront retenus.
![mnemonic](assets/fr/3.webp)
Ces 4 premiers bits, formant la somme de contrôle, seront alors ajoutés à l'entropie originale. À cette étape, la phrase de récupération est pratiquement constituée, mais elle se présente encore sous une forme binaire. Pour convertir cette suite binaire en mots conformément au standard BIP39, nous allons d'abord diviser la séquence en segments de 11 bits.
![mnemonic](assets/fr/4.webp)
Chacun de ces paquets représente un nombre en binaire qui sera ensuite converti en un nombre décimal (base 10). Nous ajouterons `1` sur chaque nombre car dans l'informatique, on compte à partir de `0`, mais la liste BIP39 est numérotée à partir de `1`.

![mnemonic](assets/fr/5.webp)

Enfin, le nombre en décimal nous indique la position du mot correspondant dans la liste des 2048 mots du BIP39. Il ne reste alors plus qu'à sélectionner ces mots pour composer la phrase de récupération de notre portefeuille.

![mnemonic](assets/fr/6.webp)

Maintenant, passons à la pratique ! Nous allons générer une phrase de récupération de 12 mots. Toutefois, cette opération demeure identique dans le cas d'une phrase de 24 mots, à l'exception qu'il faudrait opter pour une entropie de 256 bits et une somme de contrôle de 8 bits, comme l'indique le tableau d'équivalence situé au début de cette partie.

## Génération de l'entropie

Munissez-vous de votre feuille de papier, de votre stylo et de vos dés. Pour commencer, nous allons devoir générer 128 bits de manière aléatoire, c'est-à-dire une séquence de 128 `0` et `1` à la suite. Pour ce faire, nous allons utiliser les dés.

Les dés possèdent 6 faces, toutes avec une probabilité identique d'être tirée. Cependant, notre objectif est de produire un résultat binaire, soit deux issues possibles. Nous allons donc attribuer la valeur `0` à chaque lancer aboutissant sur un chiffre pair, et `1` pour un chiffre impair. En conséquence, nous effectuerons 128 lancers pour constituer notre entropie de 128 bits. Si le dé affiche `2`, `4`, ou `6`, nous inscrirons `0`; pour `1`, `3`, ou `5`, ce sera `1`. Chaque résultat sera noté de manière séquentielle, de gauche à droite et de haut en bas. Pour faciliter les étapes suivantes, nous regrouperons les bits par paquets de quatre et de trois, comme sur l'image ci-dessous. Chaque ligne doit disposer de 11 bits : 2 paquets de 4 bits et un paquet de 3 bits.






Comme on peut le voir sur mon exemple, le douzième mot est actuellement constitué de seulement 7 bits. Ceux-ci seront complétés par les 4 bits de la somme de contrôle lors de l'étape suivante pour former les 11 bits.


## Calcul de la checksum

Cette étape est la plus critique dans la génération manuelle d'une phrase mnémonique, car elle requiert l'utilisation d'un ordinateur. Comme évoqué précédemment, la checksum correspond au début du hash SHA256 généré à partir de l'entropie. Bien qu'il soit théoriquement possible de calculer un SHA256 à la main pour une entrée de 128 ou 256 bits, cette tâche pourrait prendre une semaine entière. De plus, la moindre erreur dans les calculs manuels ne serait identifiée qu'à l'issue du processus, ce qui vous obligerait à tout reprendre depuis le début. Il est donc inimaginable de faire cette étape avec une feuille de papier et un stylo. L'ordinateur est quasi obligatoire. Si vous voulez toutefois apprendre à faire un SHA256 à la main, nous vous expliquons comment le faire dans [la formation CRYPTO301](https://planb.network/en/courses/crypto301).

C'est pour cette raison que je vous déconseille fortement de faire une phrase manuelle pour un véritable portefeuille. Selon moi, l'utilisation d'un ordinateur dans ce processus, même en prenant toutes les précautions nécessaires, augmente de manière irraisonnable la surface d'attaque du portefeuille.


