---
name: Introduction à la cryptographie
goal: Comprendre la création d’un portefeuille Bitcoin d’un point de vue cryptographique
objectives:
  - Démystifier la terminologie de la cryptographie liée aux Bitcoin.
  - Maîtriser la création d'un portefeuille Bitcoin.
  - Comprendre la structure d'un portefeuille Bitcoin.
---

# Un voyage au cœur de la cryptographie

Vous êtes fasciné par Bitcoin ? Vous vous demandez comment fonctionne un portefeuille Bitcoin ? Préparez-vous à embarquer dans un voyage captivant au cœur de la cryptographie ! Loïc, notre expert, vous guidera à travers les méandres de la création d'un portefeuille Bitcoin, dévoilant les mystères derrière les termes techniques intimidants tels que le hachage, la dérivation des clés et les courbes elliptiques. 

Cette formation vous dotera non seulement des connaissances pour comprendre la structure d'un portefeuille Bitcoin, mais vous préparera également à plonger plus profondément dans le passionnant univers de la cryptographie. Alors, êtes-vous prêt à entreprendre ce voyage ? Rejoignez-nous et transformez votre curiosité en compétence !

+++

# Introduction à la cryptographie

![introduction par Rogzy](https://youtu.be/ul8zU5QWIXg)

C'est avec grand plaisir que nous vous accueillons à la nouvelle formation intitulée "Crypto 301 : Introduction à la cryptographie et au portefeuille HD", orchestrée par l'expert en la matière, Loïc Morel. Ce cours va vous faire plonger dans le fascinant univers de la cryptographie, cette discipline fondamentale des mathématiques qui assure l'encryption et la sécurité de vos données.

Dans notre vie quotidienne et particulièrement dans le domaine des Bitcoins, la cryptographie joue un rôle primordial. Les concepts liés à celle-ci tels que les clés privées, publiques, les adresses, les chemins de dérivation, la graine et l'entropie, sont au cœur de l'utilisation et de la création d'un portefeuille Bitcoin. À travers ce cours, Loïc vous expliquera en détail comment sont créées les clés privées et comment elles sont liées aux adresses. Loïc consacrera également une heure à vous expliquer les détails mathématiques de la courbe elliptique, cette complexe courbe mathématique. De plus, vous comprendrez pourquoi l'utilisation de HMAC SHA512 est importante pour sécuriser votre portefeuille et quelle est la différence entre la graine et la phrase mnémonique.

Le but ultime de cette formation est de vous permettre de comprendre techniquement les processus de création d'un portefeuille HD et les méthodes cryptographiques employées. Au fil des années, les portefeuilles Bitcoin ont évolué pour devenir plus faciles à utiliser, plus sécurisés et standardisés grâce à des BIP spécifiques. Loïc vous aidera à comprendre ces BIP pour saisir les choix des développeurs de Bitcoin et des cryptographes. Comme toutes les formations offertes par notre université, celle-ci est entièrement gratuite et open source. Cela signifie que vous pouvez librement la reprendre et l'utiliser à votre guise. Nous avons hâte de recevoir vos retours à la fin de ce cours passionnant.

![intro par loïc](https://youtu.be/mwuxXLk4Kws)

Bonjour à toutes et à tous, je suis Loïc Morel, votre guide à travers cette exploration technique de la cryptographie utilisée dans les portefeuilles Bitcoin.

Notre voyage commence avec une plongée dans les abysses des fonctions de hachage cryptographiques. Nous démonterons ensemble les rouages de l'incontournable SHA256 et explorerons divers algorithmes dédiés à la dérivation.

Nous poursuivrons notre aventure en déchiffrant le monde mystérieux des signatures numériques. Vous découvrirez comment la magie des courbes elliptiques s'applique à ces signatures, et nous ferons la lumière sur la manière de calculer la clé publique à partir de la clé privée. Et bien sûr, nous aborderons l'acte de signer avec la clé privée.

Ensuite, nous remonterons le temps pour voir l'évolution des portefeuilles Bitcoin, et nous nous aventurerons dans les concepts d'entropie et de nombres aléatoires. Nous passerons en revue la fameuse phrase mnémonique, tout en ouvrant une parenthèse sur la passphrase. Vous aurez même l'occasion de vivre une expérience unique en créant une graine depuis 128 lancés de dés !

Avec ces bases solides, nous serons prêts pour la partie cruciale : la création d'un portefeuille Bitcoin. De la naissance de la graine et de la clé maître, en passant par l'étude des clés étendues, jusqu'à la dérivation des paires de clés enfants, chaque étape sera décortiquée. Nous discuterons également de la structure du portefeuille et des chemins de dérivation.

Pour couronner le tout, nous terminerons notre parcours en examinant les adresses Bitcoin. Nous expliquerons comment elles sont créées et comment elles jouent un rôle essentiel dans le fonctionnement des portefeuilles Bitcoin.

Embarquez avec moi pour ce voyage captivant, et préparez-vous à explorer l'univers de la cryptographie comme jamais auparavant. Laissez vos préconceptions à la porte et ouvrez votre esprit à une nouvelle manière de comprendre Bitcoin et sa structure fondamentale.

# Les fonctions de hachage

## Introduction aux fonctions de hachage cryptographique relative à Bitcoin

![2.1 - les fonctions de hachage cryptographiques](https://youtu.be/dvnGArYvVr8)

Bienvenue à notre session d'aujourd'hui consacrée à une immersion approfondie dans le monde cryptographique des fonctions de hachage, une pierre angulaire essentielle à la sécurité du protocole Bitcoin. Imaginez une fonction de hachage comme un robot déchiffreur cryptographique ultra-efficace qui transforme des informations de toutes tailles en une empreinte digitale unique et de taille fixe, appelée "hash". Au fil de notre exploration, nous dépeindrons le portrait des fonctions de hachage cryptographiques, en mettant en lumière leur utilisation dans le protocole Bitcoin, et en définissant les objectifs spécifiques que ces fonctions cryptographiques doivent atteindre.

Dépeindre le profil des fonctions de hachage cryptographiques nécessite de comprendre deux qualités essentielles : leur irréversibilité et leur résistance à la falsification. Chaque fonction de hachage cryptographique est comme un artiste unique, produisant un "hash" distinct pour chaque entrée. Même un pinceau qui dévie légèrement altère considérablement le tableau final, c'est-à-dire le hash. Ces fonctions agissent comme des sentinelles numériques, vérifiant l'intégrité des logiciels téléchargés. Une autre caractéristique cruciale qu'elles possèdent est leur résistance aux collisions. Certes, dans l'univers du hachage, les collisions sont inévitables, mais une excellente fonction de hachage cryptographique les minimise considérablement. C'est comme si chaque hash était une maison dans une ville immense ; malgré le nombre énorme de maisons, une bonne fonction de hachage veille à ce que chaque maison ait une adresse unique.

Naviguons maintenant sur les flots tumultueux des fonctions de hachage désuètes. SHA0, SHA1, et MD5 sont aujourd'hui considérées comme des coques rouillées dans l'océan du hachage cryptographique. Elles sont souvent déconseillées car elles ont perdu leur résistance aux collisions. Le principe des tiroirs explique pourquoi, malgré nos meilleurs efforts, l'évitement des collisions est impossible en raison de la limitation de la taille de sortie. Il est également important de noter que la résistance à la seconde préimage est dépendante de la résistance aux collisions. Pour être véritablement considérée comme sûre, une fonction de hachage doit résister aux collisions, à la seconde préimage et à la préimage.

Élément clé dans le protocole Bitcoin, la fonction de hachage SHA-256 est le capitaine du navire. D'autres fonctions, comme SHA-512, sont utilisées pour la dérivation avec HMAC et PBKDF. De plus, RIPMD160 est utilisée pour réduire une empreinte à 160 bits. Lorsque nous parlons de HASH256 et HASH160, nous nous référons à l'utilisation d'un double hachage avec SHA-256 et RIPMD. L'utilisation de HASH160 est particulièrement avantageuse car elle permet de bénéficier de la sécurité de SHA-256 tout en réduisant la taille de l'empreinte.

Pour résumer, l'objectif ultime d'une fonction de hachage cryptographique est de transmuter une information de taille arbitraire en une empreinte de taille fixe. Pour être reconnue comme sécurisée, elle doit avoir plusieurs cordes à son arc : irréversibilité, résistance à la falsification, résistance aux collisions, et résistance à la seconde préimage.

Au terme de cette exploration, nous avons démystifié les fonctions de hachage cryptographiques, mis en évidence leur utilisation dans le protocole Bitcoin, et décortiqué leurs objectifs spécifiques. Nous avons appris que pour être considérées comme sûres, les fonctions de hachage doivent être résistantes à la préimage, à la seconde préimage, aux collisions et à la falsification. Nous avons également parcouru l'éventail des différentes fonctions de hachage utilisées dans le protocole Bitcoin. Dans notre prochaine session, nous plongerons dans le coeur de la fonction de hachage SHA256, et découvrirons les mathématiques fascinantes qui lui confèrent ses caractéristiques uniques.

## Les rouages de SHA256

![Les rourages de SHA256](https://youtu.be/74SWg_ZbUj4)

Bienvenue à la suite de notre voyage fascinant à travers les labyrinthes cryptographiques de la fonction de hachage. Aujourd'hui, nous dévoilons le voile sur les mystères de SHA256, un processus complexe mais ingénieux, que nous avons introduit lors de notre précédente discussion sur les fonctions de hachage. Faisons un pas de plus dans ce labyrinthe, en débutant par le pré-traitement de SHA256. Imaginez le pré-traitement comme la préparation d'un plat savoureux, où nous ajoutons des "bits de remplissage" pour que la taille de notre ingrédient principal, l'entrée, atteigne un multiple parfait de 512 bits. Tout ceci dans le but ultime de générer un hash succulent de 256 bits à partir d'un ingrédient de taille variée.

Dans cette recette cryptographique, nous jouons avec les bits, ayant une taille de message initial que nous appellerons M. Un bit est réservé pour le séparateur, tandis que P bits sont utilisés pour le rembourrage. En outre, nous mettons de côté 64 bits pour la deuxième phase de pré-traitement. Le total doit être un multiple de 512 bits. Un peu comme s'assurer que tous les ingrédients s'harmonisent parfaitement dans notre plat.

Nous passons maintenant à la deuxième phase du prétraitement, qui implique l'ajout de la représentation binaire de la taille du message initial, en bits. Pour cela, nous utilisons nos 64 bits réservés lors de l'étape précédente. Nous ajoutons des zéros pour arrondir nos 64 bits à notre entrée équilibrée. Ensuite, nous fusionnons le message initial, le remplissage des bits et le remplissage de la taille, comme des ingrédients dans un mixeur, pour obtenir notre entrée équilibrée.

À présent, nous nous préparons pour les premières étapes du traitement de la fonction SHA-256. Comme dans toute bonne recette, nous avons besoin de certains ingrédients de base, que nous appelons constantes et vecteurs d'initialisation. Les vecteurs d'initialisation, de A à H, sont les premiers 32 bits des parties décimales des racines carrées des 8 premiers nombres premiers. Les constantes K, de 0 à 63, représentent quant à elles les 32 premiers bits des parties décimales des racines cubiques des 64 premiers nombres premiers.

Au sein de la fonction de compression, nous utilisons des opérateurs spécifiques tels que XOR, AND et NOT. Nous traitons les bits un par un selon leur rang, en utilisant l'opérateur XOR et une table de vérité. L'opérateur AND est utilisé pour retourner 1 seulement si les deux opérandes sont égales à 1, et l'opérateur NOT pour renvoyer la valeur opposée d'une opérande. Nous utilisons également l'opération SHR pour décaler les bits vers la droite selon un nombre choisi.

Enfin, après avoir séparé l'entrée équilibrée en différents blocs de messages de 512 bits, nous effectuons 64 tours de calcul dans la fonction de compression. Comme dans une course cycliste, chaque tour de piste améliore notre

position. Nous additionnons modulo 2^32 l'état intermédiaire à l'état initial de la fonction de compression. Les additions dans la fonction de compression sont des additions modulo 2^32 pour contenir la taille des sommes à 32 bits.

Pour conclure, nous voudrions souligner le rôle crucial des calculs effectués dans les boîtes CH, MAJ, σ0 et σ1. Ces opérations, parmi d'autres, sont les gardiens qui assurent la robustesse de la fonction de hachage SHA256 face aux attaques, faisant de celle-ci un choix privilégié pour la sécurisation de nombreux systèmes numériques, notamment au sein du protocole Bitcoin. Il est donc évident que bien que complexe, la beauté de SHA256 réside dans sa robustesse à retrouver l'entrée à partir du hash, alors que la vérification du hash pour une entrée donnée est une action mécaniquement simple.

## Les algorithmes utilisés pour la dérivation

![Les algorithmes utilisés pour la dérivation](https://youtu.be/ZF1_BMsOJXc)

Les algorithmes de dérivation HMAC et PBKDF2 sont des composants clés dans la mécanique de sécurité du protocole Bitcoin. Ils préviennent une variété d'attaques potentielles et garantissent l'intégrité des portefeuilles Bitcoin.

HMAC et PBKDF2 sont des outils cryptographiques utilisés pour différentes tâches dans Bitcoin. HMAC est principalement utilisé pour contrer les attaques par extension de longueur lors de la dérivation des portefeuilles hiérarchiquement déterministes (HD), tandis que PBKDF2 est utilisé pour convertir une phrase mémonique en graine.

HMAC, qui prend un message et une clé comme entrées, génère une sortie de taille fixe. Pour assurer l'uniformité, la clé est ajustée en fonction de la taille des blocs utilisés dans la fonction de hachage. Dans le cadre de la dérivation des portefeuilles HD, HMAC-SHA-512 est utilisé. Ce dernier fonctionne avec des blocs de 1024 bits (128 octets) et ajuste la clé en conséquence. Il utilise les constantes OPAD (0x5c) et IPAD (0x36), répétées autant de fois que nécessaire pour renforcer la sécurité.

Le processus de HMAC-SHA-512 implique la concaténation du résultat de SHA-512 appliqué à la clé XOR OPAD et à la clé XOR IPAD avec le message. Lorsqu'il est utilisé avec des blocs de 1024 bits (128 octets), la clé d'entrée est complétée par des zéros si nécessaire, puis XORée avec IPAD et OPAD. La clé ainsi modifiée est ensuite concaténée avec le message.

Le code de chaîne, en intégrant une source supplémentaire d'entropie, augmente la sécurité des clés dérivées. Sans lui, une attaque pourrait compromettre l'ensemble du portefeuille et voler tous les bitcoins.

PBKDF2 est utilisé pour convertir une phrase mémonique en graine. Cet algorithme réalise 2048 tours en utilisant HMAC SHA512. Grâce à ces algorithmes de dérivation, deux entrées différentes peuvent donner une sortie unique et fixe, ce qui pallie le problème des attaques par extension de longueur possibles sur les fonctions de la famille SHA-2.
Une attaque par extension de longueur exploite une propriété spécifique de certaines fonctions de hachage cryptographiques. Dans une telle attaque, un attaquant qui possède déjà le hachage d'un message inconnu peut l'utiliser pour calculer le hachage d'un message plus long, qui est une extension du message original. Cela est souvent possible sans connaître le contenu du message original, ce qui peut mener à des failles de sécurité importantes si ce genre de fonction de hachage est utilisé pour des tâches comme la vérification d'intégrité.

En conclusion, les algorithmes HMAC et PBKDF2 jouent des rôles essentiels dans la sécurité de la dérivation des portefeuilles HD dans le protocole Bitcoin. L'HMAC-SHA-512 est utilisé pour se prémunir contre les attaques par extension de longueur, tandis que PBKDF2 permet la conversion de la phrase mémonique en graine. Le code de chaîne ajoute une source d'entropie supplémentaire dans la dérivation des clés, assurant ainsi la robustesse du système.

# Les signatures numériques

## Signatures numériques et courbes elliptiques

![Signatures numériques et courbes elliptiques](https://youtu.be/gOjYiPkx4z8)

Dans le monde des cryptomonnaies, la sécurité des transactions est primordiale. Au cœur du protocole Bitcoin, on retrouve l'utilisation de signatures numériques qui servent de preuves mathématiques démontrant la possession d'une clé privée associée à une clé publique spécifique. Cette technique de protection des données est essentiellement basée sur un domaine fascinant de la cryptographie appelé la cryptographie à courbes elliptiques (ECC).

La cryptographie à courbes elliptiques est la colonne vertébrale de la sécurité des transactions Bitcoin. Ces courbes elliptiques, qui ne sont pas sans rappeler les courbes mathématiques que l'on a pu étudier à l'école, sont utiles dans une variété d'applications cryptographiques, allant des échanges de clés au chiffrement asymétrique en passant par la création de signatures numériques. Un détail intéressant qui distingue les courbes elliptiques est leur symétrie : toute ligne non verticale coupant deux points de la courbe intersectera un troisième point.

Maintenant, creusons un peu plus : le protocole Bitcoin utilise une courbe elliptique particulière dénommée SecP256K1 pour effectuer ses opérations cryptographiques. Cette courbe, définie sur un ensemble fini d'entiers positifs modulo un nombre premier de 256 bits, peut être visualisée comme un nuage de points plutôt qu'une courbe traditionnelle. C'est cette conception unique qui permet à Bitcoin de sécuriser efficacement ses transactions.

Quant au choix de la courbe secp256k1 pour Bitcoin, il est intéressant de noter qu'elle a été privilégiée à la courbe secp256r1. Cette courbe se définit par les paramètres a=0 et b=7, et son équation est y² = x³ + 7 modulo n, avec n représentant le nombre premier qui détermine l'ordre de la courbe.

Lorsque l'on parle des constantes utilisées dans le système Bitcoin, on fait généralement référence aux paramètres spécifiques de l'algorithme Elliptic Curve Digital Signature Algorithm (ECDSA) et du système de courbes elliptiques utilisé par Bitcoin, qui est la courbe secp256k1. Voici ces paramètres:

- champ primaire (p): Bitcoin utilise une courbe sur un champ primaire, donc p est le premier nombre utilisé pour définir ce champ. Pour la courbe secp256k1, p est égal à `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` en hexadécimal ou p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 en décimal.
- ordre de la courbe (n): Il s'agit du nombre de points sur la courbe, y compris le point à l'infini. Pour secp256k1, n est égal à `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` en hexadécimal ou n = 2^256 - 432420386565659656852420866394968145599 en décimal.
- point générateur (G): Le point de base, ou générateur, est le point sur la courbe à partir duquel toutes les autres clés publiques sont générées. Il a des coordonnées x et y spécifiques, généralement représentées en hexadécimal. Pour secp256k1, les coordonnées G sont, en hexadécimale :
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Notez que toutes les valeurs hexadécimales sont généralement représentées en base 16, tandis que les valeurs décimales sont en base 10. De plus, toutes les opérations sur ces constantes sont effectuées modulo p pour les coordonnées de points sur la courbe et modulo n pour les opérations de clé et de signature.

Alors, où sont stockés ces fameux bitcoins ? Pas dans un portefeuille Bitcoin, comme on pourrait le penser. En réalité, un portefeuille Bitcoin conserve les clés privées nécessaires pour prouver la possession des bitcoins. Les bitcoins eux-mêmes sont enregistrés sur la blockchain, une base de données décentralisée qui archive toutes les transactions.

Dans le système Bitcoin, l'unité de compte est le bitcoin (notez le "b" minuscule). Ce dernier est divisible jusqu'à huit décimales, la plus petite unité étant le satoshi. Les UTXO, ou "Unspent Transaction Output", représentent les sorties de transactions non dépensées appartenant à un utilisateur. Pour dépenser ces bitcoins, il faut démontrer la possession de la clé privée correspondante à la clé publique liée à chaque UTXO.

Pour assurer la sécurité des transactions, Bitcoin fait appel à deux protocoles de signature numérique : l'ECDSA (Elliptic Curve Digital Signature Algorithm) et Schnorr. ECDSA est un protocole de signature intégré à Bitcoin depuis son lancement en 2009, tandis que les signatures de Schnorr ont été ajoutées plus récemment, en novembre 2021. Bien que ces deux protocoles reposent sur la cryptographie à courbes elliptiques et utilisent des mécanismes mathématiques similaires, ils diffèrent principalement en termes de structure de signature.

Avant de plonger plus profondément dans ces mécanismes de signature, il est important de bien comprendre ce qu'est une courbe elliptique. Une courbe elliptique est définie par l'équation y² = x³ + ax + b. Tout point sur cette courbe a une symétrie distinctive qui est la clé de son utilité en cryptographie.

En fin de compte, diverses courbes elliptiques sont reconnues comme étant sécurisées pour un usage cryptographique. Le plus connu est peut-être la courbe secp256r1. Cependant, pour Bitcoin, Satoshi Nakamoto a opté pour une autre courbe : la secp256k1.

Dans la prochaine section de ce cours, nous examinerons de plus près la clé publique et la clé privée pour une compréhension approfondie de la cryptographie sur les courbes elliptiques et de l'algorithme de signature numérique. Ce sera le moment de consolider vos connaissances et de comprendre comment toutes ces informations s'articulent pour garantir la sécurité du protocole Bitcoin.

## Calculer la clé publique depuis la clé privée

![Calculer la clé publique depuis la clé privée](https://youtu.be/NJENwFU889Y)

Dans la suite de ce cours, nous allons nous pencher sur les mécanismes des clés publiques et privées, deux éléments cruciaux du protocole Bitcoin. Ces clés sont intrinsèquement liées par l'algorithme Elliptic Curve Digital Signature Algorithm (ECDSA). Les comprendre nous donnera un aperçu profond de la manière dont Bitcoin sécurise les transactions sur sa plateforme.

Pour commencer, plongeons dans l'univers de l'algorithme ECDSA. Bitcoin exploite cet algorithme de signature numérique pour lier les clés privées et publiques. Dans ce système, la clé privée est un nombre aléatoire ou pseudo-aléatoire de 256 bits. Le nombre total de possibilités pour une clé privée est théoriquement de 2^256, mais il est légèrement inférieur à cela dans la réalité. Pour être précis, certaines clés privées de 256 bits ne sont pas valides pour Bitcoin.

Pour être compatible avec Bitcoin, une clé privée doit être comprise entre 1 et n-1, où n représente l'ordre de la courbe elliptique. Cela signifie que le nombre total de possibilités pour une clé privée Bitcoin est presque égal à 1,158 x 10^77. Pour mettre cela en perspective, c'est à peu près le même nombre d'atomes présents dans l'univers observable. La clé privée unique est ensuite utilisée pour déterminer une clé publique de 512 bits.

La clé publique, notée K, est un point sur la courbe elliptique qui est dérivé de la clé privée en utilisant des opérations de points sur la courbe. Il est important de noter que la fonction ECDSA est irréversible, c'est-à-dire qu'il est impossible de retrouver la clé privée à partir de la clé publique. Cette irréversibilité est la pierre angulaire de la sécurité du portefeuille Bitcoin.

La clé publique se compose de deux points de 256 bits chacun, totalisant 512 bits. Cependant, elle peut être compressée en un nombre de 264 bits. Le point G est le point de départ pour calculer toutes les clés publiques des utilisateurs du système.

L'une des propriétés remarquables des courbes elliptiques est qu'une droite intersectant la courbe en deux points intersectera également un troisième point, appelé point O. Cette propriété est utilisée pour déterminer le point U, qui est l'opposé du point O. L'addition d'un point à lui-même se fait en traçant une tangente à la courbe au niveau de ce point, ce qui donne un nouveau point unique appelé j. Le produit scalaire d'un point par n revient à ajouter ce point à lui-même n fois.

Ces opérations sur les points d'une courbe elliptique sont la base du calcul des clés publiques. Connaissant la clé privée, il est facile de calculer la clé publique. Cependant, connaître la clé publique ne permet pas de calculer la clé privée, garantissant ainsi la sécurité du système Bitcoin. En effet, la sécurité des clés publiques et privées repose sur le problème du logarithme discret, une question mathématique complexe.

Dans notre prochain cours, nous explorerons comment une signature numérique est réalisée en utilisant l'algorithme ECDSA avec une clé privée pour débloquer des bitcoins. Restez à l'écoute pour cette exploration passionnante du monde des cryptomonnaies et de la cryptographie.

## Signer avec la clé privée

![Signer avec la clé privée](https://youtu.be/h2hIyGgPqkM)

Le processus de signature numérique est une méthode clé pour prouver que vous êtes le détenteur d'une clé privée sans avoir à la révéler. Ceci est réalisé en utilisant l'algorithme ECDSA, qui comprend la détermination d'un nonce unique, le calcul d'un nombre spécifique, V, et la création d'une signature numérique composée de deux parties, S1 et S2. Il est crucial de toujours utiliser un nonce unique pour éviter les attaques de sécurité. Un exemple notoire de ce qui peut se produire lorsque cette règle n'est pas respectée est le cas du piratage de la PlayStation 3, qui a été compromis en raison de la réutilisation du nonce.

De manière précise, pour valider une signature numérique à l'aide de l'algorithme ECDSA (Elliptic Curve Digital Signature Algorithm), les étapes suivantes sont généralement impliquées :

1. Vérifiez que les valeurs de la signature, S1 et S2, sont dans l'intervalle [1, n-1]. Si ce n'est pas le cas, la signature est invalide.
2. Calculez l'inverse de S2 mod n. Nous allons appeler cela u. On le calcule souvent comme suit : u = (S2)^-1 mod n.
3. Calculez H, qui est la valeur de hachage du message signé.
4. Calculez u1 = H _ u mod n et u2 = S1 _ u mod n.
5. Calculez le point P sur la courbe elliptique en utilisant u1, u2, et la clé publique K : P = u1*G + u2*K, où G est le point de génération de la courbe.
6. Si P est le point à l'infini, la signature est invalide.
7. Calculez I = x-coordinate of P mod n.
8. La signature est valide si I est égal à S1.

Il est important de noter que chaque logiciel peut utiliser différentes notations et certaines étapes peuvent être combinées ou réarrangées, mais la logique de base est la même. Notez également que toutes les opérations arithmétiques sont effectuées dans le corps fini défini par la courbe elliptique (mod n, où n est l'ordre de la courbe). Pour rappel, la courbe secp256k1 (utilisée dans Bitcoin) n = 2^256 - 432420386565659656852420866394968145599.

En ce qui concerne la génération de clés publiques et privées, il est essentiel de se familiariser avec la courbe elliptique et le point générateur. Pour obtenir une clé publique, un nombre aléatoire doit être choisi comme clé privée, souvent appelé `nonce`, et utilisé dans l'équation de la courbe elliptique.

La courbe elliptique est un outil puissant pour générer des clés publiques et privées sécurisées. Par exemple, pour obtenir la clé publique 3G, vous dessinez une tangente au point G, calculez l'opposé de -G pour obtenir 2G, puis additionnez G et 2G. Pour réaliser une transaction, vous devez prouver que vous connaissez le nombre 3 en débloquant les bitcoins associés à la clé publique 3G.

Pour créer une signature numérique et prouver que vous connaissez la clé privée associée à la clé publique 3G, vous calculez d'abord un nonce, puis le point V associé à ce nonce (dans l'exemple donné, c'est 4G). Ensuite, vous calculez le point T en additionnant la clé publique 3G et le point V, ce qui donne 7G.

La vérification d'une signature numérique est une étape cruciale dans l'utilisation de l'algorithme ECDSA, qui permet de confirmer l'authenticité d'un message signé sans avoir besoin de la clé privée de l'expéditeur. Voici comment cela se déroule en détail :

Dans notre exemple, nous avons deux valeurs importantes : T et V. T est une valeur numérique (7 dans cet exemple), et V est un point sur la courbe elliptique (représenté par 4G ici). Ces valeurs sont produites lors de la création de la signature numérique et sont ensuite envoyées avec le message pour permettre la vérification.

Quand le vérificateur reçoit le message, il va également recevoir ces deux valeurs, T et V.

Voici les étapes que le vérificateur va suivre pour valider la signature :

1. Il va d'abord calculer le hachage du message, que nous appellerons H.
2. Ensuite, il calculera u1 et u2. Pour ce faire, il utilisera les formules suivantes :
   - u1 = H \* (S2)^-1 mod n
   - u2 = T \* (S2)^-1 mod n
     Où S2 est la deuxième partie de la signature numérique, n est l'ordre de la courbe elliptique et (S2)^-1 est l'inverse de S2 mod n.
3. Le vérificateur calculera ensuite un point P' sur la courbe elliptique à l'aide de la formule : P' = u1 _ G + u2 _ K
   - G est le point de génération de la courbe
   - K est la clé publique de l'expéditeur
4. Le vérificateur calculera alors I', qui est simplement la coordonnée x du point P' modulo n.
5. Enfin, le vérificateur confirmera que I' est égal à T. Si c'est le cas, la signature est considérée comme valide. Si ce n'est pas le cas, la signature est invalide.

Cette procédure garantit que seul l'expéditeur possédant la clé privée correspondante pourrait avoir produit une signature qui passe ce processus de vérification.

En conclusion, la vérification d'une signature numérique ECDSA est une procédure essentielle dans les transactions Bitcoin. Elle permet de garantir que le message signé n'a pas été altéré lors de sa transmission et que l'expéditeur est bien le détenteur de la clé privée. Cette technique d'authentification numérique repose sur des principes mathématiques complexes, notamment l'arithmétique de courbe elliptique, tout en maintenant la confidentialité de la clé privée. Elle offre une solide base de sécurité pour les transactions cryptographiques.

Cela dit, la gestion de ces clés, ainsi que leur création, est une autre question essentielle dans Bitcoin. Comment générer une nouvelle paire de clés ? Comment organiser une multitude de clés de manière sécurisée et efficace ? Comment les récupérer si nécessaire ?

Pour répondre à ces questions et approfondir votre compréhension de la sécurité de la cryptographie, notre prochain cours se concentrera sur le concept de Portefeuille Déterministe Hiérarchique (HD wallets) et l'utilisation des phrases mnémoniques. Ces mécanismes offrent des moyens élégants de gérer efficacement vos clés de cryptomonnaie tout en renforçant la sécurité et la récupérabilité.

# La phrase mnémonique

## Évolution des portefeuilles Bitcoin

![Évolution des portefeuilles Bitcoin](https://youtu.be/6tmu1R9cXyk)

Le Portefeuille Déterministe Hiérarchique, ou plus couramment appelé portefeuille HD, joue un rôle prépondérant dans l'écosystème des cryptomonnaies. Le terme "portefeuille" peut sembler trompeur pour ceux qui sont novices dans ce domaine, car il n'implique pas la détention d'argent ou de devises. Il fait plutôt référence à une collection de clés cryptographiques privées dérivées d'une seule clé mère, grâce à un ingénieux procédé d'arithmétique algorithmique. Ces clés privées, qui sont d'une longueur fixe de 256 bits, sont l'essence même de la possession de crypto-monnaies, et sont parfois désignées sous le nom un peu plus brut de "Just a Bunch Of Keys" (JBOC).

Cependant, la complexité de la gestion de ces clés est compensée par un ensemble de protocoles, appelés Bitcoin Improvement Proposals (BIP). Ces propositions de mise à niveau sont au cœur de la fonctionnalité et de la sécurité des portefeuilles HD. Par exemple, le [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), lancé en 2012, a révolutionné la manière dont ces clés sont générées et stockées, en introduisant le concept de clés dérivées de manière déterministe et hiérarchique. Ainsi, le processus de sauvegarde de ces clés est grandement simplifié, tout en conservant leur niveau de sécurité.

Par la suite, le [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) a introduit une innovation marquante : la phrase mnémonique de 24 mots. Ce système a permis de transformer une suite de chiffres complexe et difficile à retenir en une série de mots ordinaires, bien plus facile à mémoriser et à stocker. En outre, le [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) a proposé d'ajouter une phrase de passe supplémentaire pour renforcer la sécurité des clés individuelles. Ces améliorations successives ont abouti aux normes BIP43 et BIP44, qui ont standardisé la structure et la hiérarchisation des portefeuilles HD, rendant ces portefeuilles plus accessibles et plus faciles à utiliser pour le grand public.

Dans les sections suivantes, nous allons plonger plus profondément dans le fonctionnement des portefeuilles HD. Nous aborderons les principes de dérivation des clés et nous examinerons les concepts fondamentaux de l'entropie et de la génération de nombres aléatoires, qui sont essentiels pour garantir la sécurité de votre portefeuille HD.

En guise de synthèse, il est essentiel de souligner le rôle central des BIP32 et BIP39 dans la conception et la sécurisation des portefeuilles HD. Ces protocoles permettent de générer une multitude de clés à partir d'une seule graine, qui est supposée être un nombre aléatoire ou pseudo-aléatoire. Aujourd'hui, ces normes sont adoptées par la majorité des portefeuilles de cryptomonnaies, qu'ils soient dédiés à une seule cryptomonnaie ou qu'ils prennent en charge plusieurs types de devises.

J'espère que cette introduction vous a permis de mieux comprendre les fondements du portefeuille HD et ses diverses caractéristiques. Notre objectif est de vous aider à maîtriser ces concepts essentiels et à naviguer plus efficacement dans l'univers complexe des cryptomonnaies. Alors, restez avec nous alors que nous continuons à explorer les subtilités et les nuances de ce monde fascinant dans les prochaines leçons.

## Entropie et nombre aléatoire

![Entropie et nombre aléatoire](https://youtu.be/k18yH18w2TE)

L'importance de la sécurité des clés privées dans l'écosystème du Bitcoin est incontestable. Elles sont en effet la pierre angulaire qui assure la sécurité des transactions Bitcoin. Pour éviter toute vulnérabilité associée à la prédictibilité, ces clés doivent être générées de manière véritablement aléatoire, ce qui peut rapidement se révéler être un exercice laborieux pour l'utilisateur. Une solution à cette énigme est le Portefeuille Déterministe Hiérarchique, ou portefeuille HD. Cette méthode permet de générer de manière déterministe et hiérarchique des paires de clés enfant à partir d'une unique information à la base du portefeuille. C'est ici que l'aléatoire se révèle indispensable pour garantir la sécurité des clés dérivées.

La génération de nombres aléatoires est en effet un élément crucial en cryptographie, pour assurer l'intégrité des clés privées. Pour prévenir toute vulnérabilité liée à la prédictibilité, une clé privée doit être produite de manière aléatoire. L'usage d'une nouvelle paire de clés pour chaque transaction permet de renforcer davantage la sécurité, bien que cela complexifie leur sauvegarde et ne préserve la confidentialité que partiellement. En résumé, la sécurité des clés privées est une priorité absolue, nécessitant une génération rigoureuse et aléatoire. Les portefeuilles HD offrent une solution pour faciliter la génération et la gestion des clés tout en conservant un niveau de sécurité élevé.

Cependant, la génération de nombres aléatoires sur les ordinateurs pose un défi de taille, puisque les résultats obtenus ne sont pas véritablement aléatoires. C'est pourquoi il est essentiel d'utiliser un Générateur de Nombres Aléatoires (RNG). Les types de RNG varient, allant des Pseudo-Random Number Generators (PRNG) aux True Random Number Generators (TRNG), ainsi qu'aux PRNG qui intègrent une source d'entropie.

Dans le cas du Bitcoin, les clés privées sont générées à partir d'une seule information à la base du portefeuille. Cette information permet une dérivation déterministe et hiérarchique des paires de clés enfant. L'entropie est le socle de tout portefeuille HD, bien qu'il n'existe pas de standard pour la génération de ce nombre aléatoire. Par conséquent, la génération de nombres aléatoires est un enjeu majeur pour sécuriser les transactions Bitcoin.

La phase de vérification de la génération des clés est cruciale pour assurer la sécurité et l'authenticité de la génération de nombres aléatoires, une étape fondamentale pour prévenir toute vulnérabilité associée à la prédictibilité. Il est donc fortement recommandé d'utiliser des portefeuilles open source pour permettre cette vérification.

Cependant, il est important de noter que certains portefeuilles matériels peuvent être "closed source", rendant impossible la vérification de la génération du nombre aléatoire. Un contournement possible serait de générer soi-même sa phrase mnémonique à l'aide de dés, bien que cette approche puisse présenter certains risques.

L'utilisation d'une passphrase générée aléatoirement peut aider à atténuer ces risques.

Un exemple d'application de cette méthode est l'option "dice roll" offerte par CoinKit pour générer des phrases mnémoniques. Une autre possibilité serait d'utiliser une information initiale très large et de réduire cette information à 256 bits avec la fonction de hachage SHA-256, capable de générer un bon nombre aléatoire. Il est important de mentionner que la fonction de hachage SHA-256 résiste aux collisions, à la falsification, et aux attaques de pré-image et de seconde pré-image.

En définitive, l'aléatoire occupe une place centrale en cryptographie et en informatique, et la capacité à générer de l'aléatoire de manière sécurisée est cruciale pour garantir la sécurité des clés privées et des transactions Bitcoin. L'entropie, qui est au cœur du portefeuille HD de Bitcoin, est essentielle pour sa sécurité. Dans notre prochaine leçon, nous continuerons à explorer ce sujet, en abordant plus en détail la manière dont l'entropie contribue à la sécurité des portefeuilles HD.

### Soutiens-nous

Ce cours, ainsi que l'intégralité du contenu présent sur cette université, vous a été offert gratuitement par notre communauté. Pour nous soutenir, vous pouvez le partager autour de vous, devenir membre de l'université et même contribuer à son développement via GitHub. Au nom de toute l'équipe, merci !

### Note la formation

Un système de notation pour la formation sera bientôt intégré à cette nouvelle plateforme de E-learning ! En attendant, merci beaucoup d'avoir suivi le cours et si vous l'avez apprécié, pensez à le partager autour de vous.

## La phrase mnémonique

![La phrase mnémonique](https://youtu.be/uJERqH9Xp7I)

La sécurité d'un portefeuille Bitcoin est une préoccupation majeure pour tous ses utilisateurs. Une manière essentielle d'assurer la sauvegarde du portefeuille consiste à générer une phrase mémonique basée sur l'entropie et la checksum.

L'entropie est le pilier de la sécurité du portefeuille HD. Plusieurs méthodes existent pour générer cette entropie, notamment par le biais de générateurs de nombres pseudo-aléatoires (PRNG), de générateurs de nombres aléatoires véritables (TRNG) ou manuellement. Il est crucial que cette entropie soit aléatoire ou pseudo-aléatoire pour garantir la sécurité du portefeuille.

De son côté, la checksum assure la vérification de l'exactitude de la phrase de récupération. Sans cette checksum, une erreur dans la phrase pourrait aboutir à la création d'un portefeuille différent et donc à la perte des fonds. On obtient la checksum en passant l'entropie par la fonction SHA256 et en récupérant les 8 premiers bits du hachage.

Différents standards existent pour la phrase mémonique en fonction de la taille de l'entropie. Le standard le plus couramment utilisé pour une phrase de récupération de 24 mots est une entropie de 256 bits. La taille de la checksum est déterminée en divisant la taille de l'entropie par 32.

Par exemple, une entropie de 256 bits génère une checksum de 8 bits. La concaténation de l'entropie et de la checksum conduit alors à des tailles respectives de 128 bits, 160 bits, etc. En fonction de la taille de l'entropie, la phrase de récupération comportera 12 mots pour 128 bits, 15 mots pour 160 bits, et 24 mots pour 256 bits.

Pour transformer les bits en phrases, chaque segment est associé à un mot issu d'une liste de 2048 mots. Il est important de préciser qu'aucun mot ne présente les quatre premières lettres dans le même ordre.

Il est essentiel de sauvegarder la phrase de récupération de 24 mots pour préserver l'intégrité du portefeuille Bitcoin. Les deux standards les plus couramment utilisés se basent sur une entropie de 128 ou 256 bits et une concaténation de 12 ou 24 mots. L'ajout d'une passphrase constitue une option supplémentaire pour renforcer la sécurité du portefeuille.

En conclusion, la génération d'une phrase mémonique pour sécuriser un portefeuille Bitcoin est un processus crucial. Il est important de respecter les standards de la phrase mémonique en fonction de la taille de l'entropie. La sauvegarde de la phrase de récupération de 24 mots est essentielle pour prévenir toute perte de fonds. Nous vous remercions de votre attention et vous donnons rendez-vous pour notre prochain cours sur la cryptomonnaie.

## La passphrase

![La passphrase](https://youtu.be/dZkOYO7MXwc)

La passphrase est un mot de passe additionnel qui peut être intégré à un portefeuille Bitcoin pour accroître sa sécurité. Son utilisation est optionnelle et revient à l'appréciation de l'utilisateur. En ajoutant des informations arbitraires qui, conjointement avec la phrase mémonique, permettent de calculer la graine du portefeuille, la passphrase renforce la sécurité de celui-ci.

Pour dériver les clés d'un portefeuille HD, la phrase mémonique ainsi que la passphrase sont nécessaires. La passphrase est libre et peut atteindre une taille presque infinie. Elle n'est pas incluse dans la phrase mémonique, qui est standardisée et doit suivre certaines contraintes de taille, de checksum et de codage. Un attaquant ne peut pas accéder aux bitcoins d'un utilisateur sans connaître la passphrase. Cette dernière joue un rôle dans la construction et le calcul de toutes les clés du portefeuille.

La fonction pbkdf2 est utilisée pour générer la graine à partir de la passphrase. Cette graine permet de dériver toutes les paires de clés enfants du portefeuille. Si la passphrase est modifiée, le portefeuille Bitcoin devient complètement différent.

La passphrase est un outil essentiel pour renforcer la sécurité des portefeuilles Bitcoin. Elle peut permettre l'application de diverses stratégies de sécurité. Par exemple, elle peut être utilisée pour créer des doublons et faciliter les sauvegardes de la phrase mémonique. Elle peut également améliorer la sécurité du portefeuille en atténuant les risques associés à la génération aléatoire de la phrase mémonique.

Une passphrase efficace devrait être longue (20 à 40 caractères) et diversifiée (utilisant des majuscules, des minuscules, des chiffres et des symboles). Elle ne devrait pas être directement liée à l'utilisateur ou à son environnement. Il est plus sûr d'utiliser une séquence aléatoire de caractères plutôt qu'un mot simple comme passphrase.

Une passphrase est plus sécurisée qu'un simple mot de passe. La passphrase idéale est longue, variée et aléatoire. Elle peut renforcer la sécurité d'un portefeuille ou d'un logiciel chaud. Elle peut également être utilisée pour créer des sauvegardes redondantes et sécurisées.

Il est crucial de prendre soin des sauvegardes de la passphrase pour éviter de perdre l'accès au portefeuille. Une passphrase est une option pour un portefeuille HD. Elle peut être générée aléatoirement avec des dés ou un autre générateur de nombres pseudo-aléatoires. Il est déconseillé de mémoriser une passphrase ou une phrase mémonique.

Dans notre prochain cours, nous examinerons en détail le fonctionnement de la graine et la première paire de clés générée à partir de celle-ci. N'hésitez pas à suivre ce cours pour continuer votre apprentissage. Nous avons hâte de vous retrouver très bientôt.

## Création d’une seed depuis 128 lancés de dés !

![Création d’une seed depuis 128 lancés de dés !](https://youtu.be/lUw-1kk75Ok)

La création d'une phrase mnémonique est une étape cruciale pour la sécurisation de votre portefeuille de crypto-monnaie. Il existe plusieurs méthodes pour générer une phrase mnémonique, cependant, nous allons nous focaliser sur la méthode de génération manuelle utilisant des dés. Il est important de souligner que cette méthode n'est pas adaptée pour un portefeuille de grande valeur. Il est conseillé d'utiliser un logiciel open source ou un portefeuille matériel pour générer la phrase mnémonique. Pour créer une phrase mnémonique, nous allons utiliser des dés pour générer une information binaire. L'objectif est de comprendre le processus de création de la phrase mnémonique.

**Étape 1 - Préparation :**
Assurez-vous d'avoir une distribution Linux amnésique, comme Tails OS, installée sur une clé USB pour plus de sécurité. Notez que ce tutoriel ne devrait pas être utilisé pour créer un portefeuille principal.

**Étape 2 - Génération d'un nombre aléatoire binaire :**
Nous allons utiliser des dés pour générer une information binaire. Lancez un dé 128 fois et notez chaque résultat (1 pour impair, 0 pour pair).

**Étape 3 - Organisation des nombres binaires :**
Organisez les nombres binaires obtenus en rangées de 11 chiffres pour faciliter les calculs ultérieurs. La douzième ligne ne devrait que 7 chiffres.

**Étape 4 - Calcul de la checksum :**

Les derniers 4 chiffres pour la douxième ligne correspondent à la checksum. Pour calculer cette checksum, il nous faut utiliser un terminal d'une distribution Linux. Il est conseillé d'utiliser [TailOs](https://tails.boum.org/index.fr.html) qui est une distribution sans mémoire bootable à partir d'une clé USB. Une fois sur votre terminal, entrez la commande `echo <binary number> | shasum -a 254 -0`. Remplacer `<binary number>` par votre liste de 128 zéro et un. La sortie est un hash en hexadécimal. Relevez le premier caractère de ce hash et convertissez le en binaire. Vous pouvez vous aider de cette [table](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table). Ajoutez la checksum en binaire (4 chiffres) à la douxième ligne de votre feuille.

**Étape 5 - Conversion en décimale :**
Pour trouver les mots associés à chacune de vos lignes, il vous faut d'abord convertir en décimal chaque séries de 11 bits. Ici vous ne pouvez pas utiliser de convertisseur en ligne car ces bits représentent votre phrase mnémonique. Il va donc falloir convertir à l'aide d'une calculatrice et d'une astuce que voici : chaque bit est associé à une puissance de 2 ainsi de la gauche vers la droite nous avons 11 rangs qui correspondent à respectivement 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Pour convertir votre série de 11 bit en décimal il vous suffit d'additionner uniquement les rangs qui contiennent un 1. Par exemple pour la série 00110111011, cela correspond à l'addtion suivante : 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Vous pouvez maintenant convertir chaque ligne en décimale. Et avant de passer à l'encodage en mots il faut ajouter +1 à toutes les lignes car l'index de la liste des mots BIP39 commence à partir de 1 et non 0.

**Étape 8 - Génération de la phrase mnémonique :**
Commencez par imprimer la [liste des 2048 mots](https://seedxor.com/files/wordlist.pdf) pour faire la conversion entre vos nombres décimales et les mots du BIP39. La particularité de cette liste est qu'aucun mot ne possède ces 4 premières lettres en commun avec tous les autres mots de ce dictionnaire. Puis chercher pour chacune de vos lignes le mots associés au nombre décimal.

**Étape 9 - Test de la phrase mnémonique :**
Testez immédiatement votre phrase mnémonique sur Sparrow Wallet en créant un portefeuille à partir de celle-ci. Si vous obtenez une erreur de checksum invalide, il est probable que vous ayez fait une erreur de calcul. Corrigez cette erreur en repartant à l'étape 4 et testez à nouveau sur Sparrow Wallet. Voilà ! Vous venez de créer un nouveau portefeuille Bitcoin à partir de 128 lancés de dés.

Générer une phrase mnémonique est un processus important pour sécuriser votre portefeuille de crypto-monnaie. Il est recommandé d'utiliser des méthodes plus sécurisées, comme l'utilisation de logiciels open source ou de hardware wallet, pour générer la phrase mnémonique. Toutefois, réaliser cet atelier permet de mieux saisir comment à partir d'un nombre aléatoire nous pouvons créer un portefeuille Bitcoin.

# Création d’un portefeuille Bitcoin

## Création de la graine et de la clé maîtresse

![Création de la graine et de la clé maîtresse](https://youtu.be/56yAt_JDWhY)

Dans cette partie du cours, nous allons explorer les étapes de dérivation d'un portefeuille HD (Hierarchical Deterministic Wallet), qui permet de créer et gérer des clés privées et publiques de manière hiérarchique.

Le fondement du portefeuille HD repose sur deux éléments essentiels : la phrase mnémonique et la passphrase (mot de passe supplémentaire optionnel). Ensemble, ils constituent la seed, une séquence alphanumérique de 512 bits qui sert de base pour dériver les clés du portefeuille. À partir de cette seed, il est possible de dériver toutes les paires de clés enfants du portefeuille Bitcoin. La seed est la clé permettant d'accéder à l'ensemble des bitcoins associés au portefeuille, que vous utilisiez une passphrase ou non.

Pour obtenir la seed, on utilise la fonction pbkdf2 (Password-Based Key Derivation Function 2) avec la phrase mnémonique et la passphrase. La sortie de pbkdf2 est une seed de 512 bits. La clé privée maîtresse et le code de chaîne maître sont déterminés en utilisant l'algorithme HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512). Cet algorithme nécessite un message et une clé pour générer un résultat. La clé privée maîtresse est calculée à partir de la seed et de la phrase "Bitcoin SEED". Cette phrase est identique pour toutes les dérivations de portefeuille HD, garantissant ainsi une cohérence entre les portefeuilles.

Initialement, la fonction SHA-512 n'était pas implémentée dans le protocole Bitcoin, c'est pourquoi on utilise HMAC SHA-512. L'utilisation de HMAC SHA-512 avec la phrase "Bitcoin SEED" contraint l'utilisateur à générer un portefeuille spécifique à Bitcoin. Le résultat de HMAC SHA-512 est un nombre de 512 bits, divisé en deux parties : les 256 bits de gauche représentent la clé privée maîtresse, tandis que les 256 bits de droite représentent le code de chaîne maître.

La clé privée maîtresse est la clé parente de toutes les futures clés du portefeuille, tandis que le code de chaîne maître intervient dans la dérivation des clés enfants. Il est important de noter qu'il est impossible de dériver une paire de clés enfant sans connaître le code de chaîne correspondant de la paire parente. Le code de chaîne ajoute une source d'entropie dans le processus de dérivation.

Une paire de clés dans le portefeuille comprend une clé privée, une clé publique et un code de chaîne. Le code de chaîne permet d'introduire une source d'aléatoire dans la dérivation des clés enfants et d'isoler chaque paire de clés pour éviter toute fuite d'information.

Il est important de souligner que la clé privée maîtresse est la première clé privée dérivée à partir de la seed et n'a aucun lien avec les clés étendues du portefeuille. La seed est donc l'élément fondamental pour dériver toutes les clés du portefeuille. Elle diffère de la phrase mnémonique et de la passphrase, qui sont utilisées pour la création de la seed.

Dans le prochain cours, nous explorerons en détail les clés étendues, telles que les xPub, xPRV, zPub, et nous comprendrons pourquoi elles sont utilisées et comment elles sont construites.

## Les clés étendues

![Les clés étendues](https://youtu.be/TRz760E_zUY)

Dans cette partie du cours, nous allons étudier les clés étendues (xPub, zPub, yPub) et leurs préfixes, qui jouent un rôle important dans la dérivation des clés enfants dans un portefeuille HD (Hierarchical Deterministic Wallet).

Les clés étendues se distinguent des clés maîtresses. Un portefeuille HD génère une phrase mnémonique et une graine pour obtenir la clé maîtresse et le code de chaîne maître. Les clés étendues sont utilisées pour dériver les clés enfants et nécessitent à la fois la clé parente et le code de chaîne correspondant. Une clé étendue combine ces deux informations pour simplifier le processus de dérivation.

Les clés étendues sont identifiées par des préfixes spécifiques (XPRV, XPUB, YPUB, ZPUB) qui indiquent s'il s'agit d'une clé étendue privée ou publique, ainsi que son objectif spécifique. Les métadonnées associées à une clé étendue comprennent la version (préfixe), la profondeur, l'empreinte de la clé publique, l'index et la charge utile (code de chaîne et clé parente).

La charge utile est composée du code de chaîne (32 octets) et de la clé parente (33 octets). Ces éléments sont essentiels pour la dérivation des clés enfants. Une clé privée est générée à partir d'un nombre aléatoire ou pseudo-aléatoire, tandis qu'une clé publique est générée à l'aide de l'algorithme ECDSA (Elliptic Curve Digital Signature Algorithm).

Chaque paire de clés étendues est associée à un code de chaîne unique, qui permet d'effectuer des dérivations spécifiques. En concaténant la clé parente avec le code de chaîne, on obtient une clé privée ou publique étendue.

Les clés publiques étendues ne peuvent dériver que des clés publiques enfants normales, tandis que les clés privées étendues peuvent dériver des clés enfants publiques et privées, que ce soit sur une dérivation normale ou endurcie. L'utilisation de clés étendues avec le préfixe XPUB permet de dériver de nouvelles adresses sans remonter jusqu'aux clés privées correspondantes, offrant ainsi une meilleure sécurité. Les métadonnées associées aux clés étendues fournissent des informations importantes sur leur rôle et leur position dans la hiérarchie des clés.

Les clés publiques compressées ont une taille de 33 octets, tandis que les clés publiques brutes sont de 512 bits. Les clés publiques compressées conservent les mêmes informations que les clés brutes, mais avec une taille réduite. Les clés étendues ont une taille de 82 octets et leur préfixe est représenté en base 58 grâce à une conversion en hexadécimal. Le checksum est calculé à l'aide de la fonction de hachage HASH256.

Les dérivations renforcées commencent à partir des indexes qui sont des puissances de 2 (2^31). Les clés publiques étendues permettent uniquement de dériver des clés publiques enfants normales, tandis que les clés privées étendues permettent de dériver n'importe quelle clé enfant. Il est intéressant de noter que les préfixes les plus couramment utilisés sont xpub et zpub, qui correspondent respectivement aux standards legacy et segwit v1 et segwit v0.

Dans notre prochain cours, nous nous pencherons sur la dérivation des paires de clés enfants en utilisant les connaissances acquises sur les clés étendues et la clé maîtresse du portefeuille.

En conclusion, les clés étendues jouent un rôle essentiel dans la cryptographie et le fonctionnement des portefeuilles HD. Comprendre leur utilisation et leur calcul est crucial pour assurer la sécurité des transactions et la protection des actifs numériques. Les préfixes et les métadonnées associés aux clés étendues permettent une utilisation efficace et une dérivation précise des clés enfants nécessaires.

## Dérivation des paires de clés enfants

![Dérivation des paires de clés enfants](https://youtu.be/FXhI-GmE9Aw)

À présent, nous allons aborder le calcul de la graine et de la clé maîtresse, qui constituent les premiers éléments essentiels pour la hiérarchisation et la dérivation du portefeuille HD (Hierarchical Deterministic Wallet). La graine, d'une longueur de 128 à 256 bits, est générée de manière aléatoire ou à partir d'une phrase secrète. Elle joue un rôle déterministe dans la dérivation de toutes les autres clés. La clé maîtresse est la première clé dérivée à partir de la graine, et elle permet de dériver toutes les autres paires de clés enfants.

Le code de chaîne maître joue un rôle important dans la reprise du portefeuille à partir de la graine. Il est à noter que toutes les clés dérivées à partir de la même graine auront le même code de chaîne maître.

La hiérarchisation et la dérivation du portefeuille HD offrent une gestion plus efficace des clés et des structures de portefeuille. Les clés étendues permettent la dérivation d'une paire de clés enfant à partir d'une paire parent en utilisant des calculs mathématiques et des algorithmes spécifiques.

Il existe différents types de paires de clés enfants, notamment les clés renforcées et les clés normales. La clé publique étendue permet uniquement la dérivation de clés publiques enfants normales, tandis que la clé privée étendue permet la dérivation de toutes les clés enfants, à la fois publiques et privées, qu'elles soient en mode normal ou renforcé. Chaque paire de clés dispose d'un index qui permet de les différencier les unes des autres.

La dérivation des clés enfants utilise la fonction HMAC-SHA512 en utilisant la clé parent concaténée à l'index et au code de chaîne associé à la paire de clés. Les clés enfants normales ont un index compris entre 0 et 2 puissance 31 moins 1, tandis que les clés enfants renforcées ont un index compris entre 2 puissance 31 et 2 puissance 32 moins 1.

Il existe deux types de paires de clés enfants : les paires renforcées et les paires normales. Le processus de dérivation des clés enfants utilise les clés publiques pour générer les conditions de dépense, tandis que les clés privées sont utilisées pour la signature. La clé publique étendue permet uniquement la dérivation de clés publiques enfants normales, tandis que la clé privée étendue permet la dérivation de toutes les clés enfants, à la fois publiques et privées, en mode normal ou renforcé.

La dérivation renforcée utilise la clé privée parent, tandis que la dérivation normale utilise la clé publique parent. La fonction HMAC-SHA512 est utilisée pour la dérivation renforcée, tandis que la dérivation normale utilise un condensat de 512 bits. La clé publique enfant est obtenue en multipliant la clé privée enfant par le générateur de la courbe elliptique.

La hiérarchisation et la dérivation de nombreuses paires de clés de manière déterministe permettent de créer un schéma en arbre généalogique pour la dérivation hiérarchique. Dans le prochain cours de cette formation, nous étudierons la structure du portefeuille HD ainsi que les chemins de dérivation, en mettant notamment l'accent sur les notations des chemins de dérivation.

## Structure du portefeuille et chemins de dérivation

![Structure du portefeuille et chemins de dérivation](https://youtu.be/etO9UxwyE2I)

Dans ce chapitre, nous allons étudier la structure de l'arbre de dérivation dans un portefeuille HD (Hierarchical Deterministic Wallet). Nous avons déjà exploré le calcul de la graine, la clé maîtresse et la dérivation des paires de clés enfants. Maintenant, nous allons nous concentrer sur l'organisation des clés au sein du portefeuille.

Le portefeuille HD utilise des couches de profondeur pour organiser les clés. Chaque dérivation d'une paire parent vers une paire enfant correspond à une couche de profondeur. La profondeur 0 correspond à la clé maîtresse et au code de chaîne maître.

La profondeur 1 est utilisée pour dériver des clés enfants selon un objectif spécifique, qui est déterminé par l'index. Les objectifs sont conformes aux standards BIP 84 et Segwit v0/v1.

La profondeur 2 permet de différencier les comptes de différentes cryptomonnaies ou réseaux. Cela permet d'organiser le portefeuille en fonction des différentes sources de fonds.

La profondeur 3 est utilisée pour organiser le portefeuille en différents comptes, offrant ainsi une structure plus claire et organisée.

La profondeur 4 correspond aux chaînes interne et externe, qui sont utilisées pour les adresses destinées à être communiquées publiquement. L'index 0 est associé à la chaîne externe, tandis que l'index 1 est associé à la chaîne interne. Chaque compte dispose de deux chaînes : la chaîne externe (0) et la chaîne interne (1). La profondeur 4 est également utilisée pour gérer les types de script dans le cas des portefeuilles multi signatures.

La profondeur 5 est utilisée pour les adresses de réception sur un portefeuille classique. Dans la prochaine section, nous examinerons plus en détail la dérivation des paires de clés enfants.

Pour chaque couche de profondeur, nous utilisons des index pour différencier les paires de clés enfants. Les index renforcés sont utilisés avec une apostrophe pour certaines dérivations. La clé publique par an est utilisée comme entrée pour la fonction HMAC. L'index dans un chemin de dérivation indique la valeur utilisée dans la fonction HMAC.

L'index sans apostrophe correspond à l'index réel utilisé, tandis que l'index avec apostrophe correspond à l'index réel + 2^31. Les dérivations renforcées utilisent des index de 2^31 à 2^32-1. Par exemple, l'index 44' correspond à l'index réel 2^31 + 44.

Pour générer une adresse de réception spécifique, nous dérivons une paire de clés enfants à partir de la clé maîtresse et du code de chaîne maître. Ensuite, nous utilisons l'index pour différencier les différentes paires de clés enfants de la même profondeur.

Les clés étendues, telles que XPUB, permettent de partager votre portefeuille avec plusieurs personnes. La chaîne de dérivation est utilisée pour différencier la chaîne externe (adresses destinées à être communiquées) et la chaîne interne (adresses de change).

Il est important de noter que différentes profondeurs sont utilisées dans un portefeuille HD en fonction des différents standards. La dérivation des clés parent vers les clés enfants permet de passer d'une profondeur à une autre. L'utilisation de différentes branches dans le portefeuille HD permet d'indiquer les différents standards suivis.

Dans le prochain chapitre, nous allons étudier les adresses de réception, leurs avantages d'utilisation et les étapes de leur construction.

# Qu'est-ce qu'une adresse Bitcoin ?

## Les adresses Bitcoin

![Les adresses Bitcoin](https://youtu.be/nqGBMjPtFNI)

Dans ce chapitre, nous allons explorer les adresses de réception, qui jouent un rôle crucial dans le système Bitcoin. Elles permettent de recevoir des fonds sur une pièce et sont générées à partir de paires de clés privées et publiques. Bien qu'il existe un type de script appelé Pay2PublicKey qui permet de bloquer des bitcoins sur une clé publique, les utilisateurs préfèrent généralement utiliser des adresses de réception plutôt que ce script.

Lorsqu'un destinataire souhaite recevoir des bitcoins, il fournit une adresse de réception à l'émetteur plutôt que sa clé publique. Une adresse est en réalité un hash d'une clé publique, avec un format spécifique. La clé publique est dérivée de la clé privée enfant en utilisant des opérations mathématiques telles que l'addition et le doublement de points sur les courbes elliptiques.

Il est important de noter qu'il n'est pas possible de remonter de l'adresse vers la clé publique, ni de la clé publique vers la clé privée. L'utilisation d'une adresse permet de réduire la taille de l'information de la clé publique, qui initialement fait 512 bits. Il est possible de compresser une clé publique en conservant uniquement la valeur de x et en ajoutant un préfixe, mais cette technique n'était pas connue à l'époque de la création de Bitcoin. L'utilisation d'une adresse ne permet donc pas de gagner de l'espace dans les blocs.

Les adresses Bitcoin ont été réduites en taille pour faciliter leur utilisation. Elles possèdent une checksum, ce qui permet de détecter les fautes de frappe et de réduire les risques de perte de bitcoins. En revanche, les clés publiques n'ont pas de checksum, ce qui signifie que les fautes de frappe peuvent entraîner la perte des fonds correspondants.

Les adresses offrent également une deuxième couche de sécurité entre l'information publique et privée, rendant plus difficile la prise de contrôle de la clé privée. Les fonctions de hachage utilisées permettent aux paires de clés d'être résistantes à d'éventuelles attaques menées par des calculateurs quantiques. En effet, ces calculateurs peuvent potentiellement casser ECDSA (Elliptic Curve Digital Signature Algorithm), mais ils ne peuvent pas casser une fonction de hachage.

Il est essentiel de souligner que chaque adresse est à usage unique, ce qui contribue à la sécurité et à la confidentialité. La réutilisation d'une même adresse pose de graves problèmes de confidentialité et doit être évitée. De plus, chaque adresse est un hash d'une clé publique, accompagné d'une checksum pour réduire le risque de perte de bitcoins.

Différents préfixes sont utilisés pour les adresses Bitcoin. Par exemple, BC1Q correspond à une adresse Segwit V0, BC1P à une adresse Taproot/Segwit V1, et les préfixes 1 et 3 sont associés aux adresses Pay2PublicKeyH/Pay2ScriptH (legacy). Dans le prochain cours, nous expliquerons étape par étape la dérivation d'une adresse à partir d'une clé publique.

En résumé, les adresses de réception sont un élément essentiel du système Bitcoin. Elles sont générées à partir de paires de clés privées et publiques, et servent à recevoir des fonds sur une pièce. Les adresses intègrent une checksum pour réduire les risques de perte de bitcoins et sont conçues pour être utilisées de manière unique, garantissant ainsi la sécurité et la confidentialité. Différents types d'adresses sont utilisés dans le système Bitcoin, offrant une confidentialité et une sécurité renforcées.

## Comment créer une adresse Bitcoin ?

![Comment créer une adresse Bitcoin ?](https://youtu.be/ewMGTN8dKjI)

Dans ce chapitre, nous allons aborder la construction d'une adresse de réception pour les transactions Bitcoin. Une adresse de réception est une représentation sous forme de caractères alphanumériques d'une clé publique compressée. La conversion d'une clé publique en une adresse de réception passe par plusieurs étapes.

L'une des caractéristiques avantageuses des adresses de réception est la présence d'une checksum, qui permet la détection des erreurs. Pour cela, nous utilisons la technologie de checksum BCH (Bose-Chaudhuri-Hocquenghem) qui assure une détection précise des erreurs. Cette technologie contribue également à la réduction du nombre de caractères nécessaires pour représenter une adresse, facilitant ainsi son utilisation.

Pour commencer la construction d'une adresse, nous devons compresser la clé publique correspondante. Une clé publique brute occupe 520 bits, mais grâce à la symétrie de la courbe elliptique utilisée, une courbe elliptique peut avoir une abscisse x associée à deux valeurs possibles pour y : positive ou négative. Sur le réseau Bitcoin, nous travaillons avec un corps d'entiers positifs finis plutôt qu'avec le corps des réels. Pour représenter une clé publique à partir de x, nous ajoutons un préfixe indiquant la valeur de y (pair ou impair). La compression d'une clé publique permet de réduire sa taille de 520 à 264 bits. La parité de y dans un corps d'entiers positifs finis correspond à la parité de y dans le corps des réels.

Prenons l'exemple de la clé publique appartenant à Satoshi Nakamoto, avec un préfixe 0,3 indiquant une valeur impaire de y. Nous pouvons alors passer à la deuxième étape de la construction d'une adresse à partir de clés publiques compressées. Il est possible de calculer deux adresses pour chaque clé publique. Pour cela, nous utilisons la fonction SHA256 pour obtenir le condensat (hash) de la clé publique. Ensuite, nous appliquons la fonction ripemd160 sur le résultat de SHA256 pour obtenir une suite de caractères. Cette suite est ensuite encodée en format binaire par groupes de 5 bits, auxquels des métadonnées sont ajoutées pour le calcul de la checksum à l'aide du programme BCH.

Dans le cas des adresses legacy, nous utilisons le double hachage SHA256 pour générer la somme de contrôle de l'adresse. Cependant, pour les adresses Segwit V0 et V1, nous faisons appel à la technologie de checksum BCH pour assurer la détection des erreurs. Le programme BCH est capable de suggérer et de corriger les erreurs avec une probabilité d'erreur extrêmement faible. Actuellement, le programme BCH est utilisé pour détecter et suggérer les modifications à apporter, mais il ne les effectue pas automatiquement à la place de l'utilisateur. Le calcul de la checksum avec le code BCH repose sur l'arithmétique de Chien-Chauffage polynomiale.

Le programme BCH requiert plusieurs informations en entrée, dont le HRP (Human Readable Part) qui doit être étendu. L'extension du HRP consiste à encoder chaque lettre en base 2, en prenant les trois premiers bits de chaque caractère

, en insérant un séparateur 0, puis en concaténant les cinq derniers bits de chaque caractère. Les caractères bleus convertis en base 10 correspondent à 3 et 3 en décimal, tandis que les cinq autres caractères orange correspondent à 2 et 3 en base 10. L'extension du HRP en base 10 permet d'isoler les cinq derniers bits de chaque caractère, renforçant ainsi la checksum.

La version Segwit V0 est représentée par le code 00 et le "payload" est en noir, en base 10. Cela est suivi de six caractères réservés pour la checksum. L'entrée contenant les métadonnées est ensuite soumise au programme BCH pour obtenir la checksum en base 10. La concaténation de la version, du payload et de la checksum permet de construire l'adresse. Les caractères en base 10 sont ensuite convertis en caractères bech32 à l'aide d'une table de correspondance. L'alphabet bech32 comprend tous les caractères alphanumériques, à l'exception de 1, b, i et o, afin d'éviter toute confusion.

Pour construire une adresse commençant par bc1q, nous devons appliquer une fonction de hachage (H160) à une clé publique compressée, puis ajouter la checksum, la version (q), le HRP (bc) et le séparateur (1). Les adresses Taproot, quant à elles, commencent par bc1p car leur version (Segwit V1) correspond à 0+1=1, d'où l'utilisation du caractère p. Tous ces éléments sont ensuite convertis en BCH32, une variante de la base 32 spécifique à Bitcoin.

Ainsi, nous avons parcouru les étapes de construction d'une adresse de réception, l'utilisation de la technologie de checksum BCH, ainsi que la construction d'une adresse commençant par bc1q ou bc1p en utilisant la variante BCH32 de la base 32 spécifique à Bitcoin.

## Récapitulatif de la cryptographie pour les portefeuilles Bitcoin

![synthèse de la formation](https://youtu.be/NkAYoVUMvOs)

Tout au long de cette formation, nous avons étudié en profondeur le portefeuille déterministe hiérarchique (HD) avec le BIP32. L'entropie joue un rôle central dans ce type de portefeuille, car elle est utilisée pour générer une phrase mnémonique à partir d'un nombre aléatoire. Grâce à la liste de 2048 mots fournie dans le BIP39, cette phrase mnémonique peut être encodée en une série de mots faciles à retenir. La phrase mnémonique, ainsi qu'une passphrase éventuelle, sont nécessaires pour générer la seed du portefeuille. La passphrase agit comme un sel cryptographique qui ajoute une couche de protection supplémentaire au portefeuille.

La fonction pbkdf2 est utilisée pour générer la graine à partir de la phrase mnémonique et de la passphrase, en utilisant un hmacha512 et 2048 itérations. La clé maîtresse et le code de chaîne maître sont ensuite dérivés à partir de cette graine en utilisant à nouveau la fonction hmacha512 avec la phrase "bitcoin seed". La clé privée maîtresse et le code de chaîne maître sont les éléments les plus élevés dans la hiérarchie du portefeuille HD.

La dérivation d'une clé enfant dépend de plusieurs facteurs, notamment la clé parent et le code de chaîne correspondant. Une clé étendue est obtenue en concaténant une clé parent avec son code de chaîne, tandis qu'une clé maîtresse est une clé distincte. Pour dériver une adresse, la clé publique compressée est d'abord hachée à l'aide de SHA256 et RIPMD160, puis une chèque somme est calculée. Le double hachage SHA256 est utilisé pour calculer la chèque somme dans le cas d'un standard legacy, tandis que le programme BCH (Bose-Chaudhuri-Hocquenghem) est utilisé pour calculer la chèque somme dans le cas d'un standard segwit. Ensuite, une représentation au format base 58 est utilisée pour un standard legacy, tandis que le format bech32 est utilisé pour un standard segwit, afin d'obtenir l'adresse du portefeuille HD.

En résumé, nous avons exploré en détail les fonctions de hachage et leurs caractéristiques, ainsi que les signatures numériques et les courbes elliptiques. Nous avons ensuite plongé dans l'univers du portefeuille déterministe hiérarchique (HD) avec le BIP32, en utilisant l'entropie et la passphrase pour générer la seed du portefeuille. Nous avons également appris comment dériver les clés enfants et obtenir l'adresse du portefeuille HD. J'espère que ces informations vous ont été utiles, et je vous encourage maintenant à passer à l'évaluation pour tester vos connaissances acquises au cours de la formation Crypto 301. Merci de votre attention.

# Remerciements et continuez à creuser le terrier du lapin

Nous tenons à vous remercier sincèrement d'avoir suivi la formation Crypto 301. Nous espérons que cette expérience a été enrichissante et formatrice pour vous. Nous avons abordé de nombreux sujets passionnants, allant des mathématiques à la cryptographie en passant par le fonctionnement du protocole Bitcoin.

Si vous souhaitez approfondir davantage le sujet, nous avons une ressource supplémentaire à vous offrir. Nous avons réalisé une interview exclusive avec Théo Pantamis et Loïc Morel, deux experts renommés dans le domaine de la cryptographie. Cette interview explore en profondeur divers aspects du sujet et offre des perspectives intéressantes.

N'hésitez pas à regarder cette interview pour continuer à explorer le domaine fascinant de la cryptographie. Nous espérons que cela vous sera utile et inspirant dans votre parcours. Encore une fois, merci de votre participation et de votre engagement tout au long de cette formation.

## Interview avec Théo Pantamis

![Interview avec Théo Pantamis](https://youtu.be/c9MvtGJsEvY)

Voici un résumé de l'interview :

Dans cette interview, Théo Pantamys, spécialisé en mathématiques et passionné par Bitcoin, Lightning Network et les protocoles, partage son parcours et ses réflexions sur divers sujets.

Théo a découvert Bitcoin en 2009, mais son intérêt s'est développé davantage en 2015-2016 grâce à des vulgarisateurs scientifiques sur YouTube. Il s'est concentré sur la mathématique et la cryptographie de Bitcoin, ainsi que sur la comparaison avec d'autres protocoles.

Il souligne l'importance de la décentralisation dans Bitcoin et comment cela va à l'encontre de l'autorité de l'État, offrant une ouverture du registre. Bitcoin résout également le problème de la régulation de manière efficace.

Théo aborde également le sujet de la confidentialité dans Bitcoin. Il explique l'importance du CoinJoin pour préserver la vie privée des utilisateurs et éviter la divulgation d'informations personnelles. Il recommande l'utilisation de Wasabi et Whirlpool pour améliorer l'anonymat des transactions.

Ensuite, Théo discute de RGB, un protocole complexe qui résout les problèmes techniques de Bitcoin. Il explique comment RGB utilise des contrats discrets pour créer des tokens et des produits financiers tout en maintenant la validation de l'état du contrat sur la blockchain Bitcoin.

La discussion se poursuit sur la menace de l'informatique quantique sur Bitcoin. Théo mentionne qu'il faudrait une centaine de qubits pour casser la plupart des algorithmes, et pour l'instant, les ordinateurs quantiques n'ont pas encore atteint ce niveau de puissance.

En ce qui concerne la checksum des adresses Bitcoin, Théo explique comment les codes BCH sont utilisés pour détecter et potentiellement corriger les erreurs de frappe. Il souligne l'importance de la checksum pour éviter la perte de bitcoins et optimiser la taille des adresses.

En conclusion, Théo partage des ressources pour approfondir la compréhension de Bitcoin, notamment des chaînes YouTube de vulgarisation mathématique, des livres recommandés et des espaces Twitter où les développeurs discutent de leurs travaux.
