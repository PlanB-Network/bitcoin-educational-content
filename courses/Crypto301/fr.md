---
name:  Introduction à la cryptographie
goal: Comprendre la création d’un portefeuille Bitcoin d’un point de vue cryptographique
---


Un voyage vers la cryptographie


:[affiche du cours](Formation\courses\btc101\assets\affiche\BTC101_vignette-presentation-front.png)

Loïc nous propose un cours technique sur la cryptographie utilisée dans les portefeuilles Bitcoin. Ce cours de 3ème année ira en profondeur sur les outils employés pour créer un portefeuille Bitcoin depuis la recherche d’entropie jusqu’à la dérivation des adresses. Des termes techniques tels que le hachage, la dérivation des clés, les courbes elliptiques et autres seront expliqués en détail. 


Qu’allez-vous apprendre durant ce cours ?

L’objectif final est de comprendre la création d’un portefeuille Bitcoin d’un point de vue cryptographique.

Démystifier les termes compliqués des wallets
Permettre aux étudiants de comprendre la structure d’un wallet
Préparer l’étudiant à suivre un cours plus poussé sur la cryptographie


 Si ce plan vous convient, je vous invite à suivre mon cours. Vous pouvez aller à votre rythme et faire comme bon vous semble. En espérant vous retrouver bientôt. Merci pour votre intérêt dans mon projet.

Curriculum : CRYPTO 301 – Introduction à la cryptographie


Pas convaincu ? Tu peux regarder le curriculum complet ici: [BTC 101 - Curriculum](https://academie.decouvrebitcoin.fr/wp-content/uploads/2022/07/BTC-101-Curriculum.pdf)


contributeur financier au lancement: 

Contributeurs : Drikxe, Thomas, Samuel, Fabrice, Marco, OsyGeni, Gregory, Fabien, Lounès

Team créateur

        Loïc Morel – Création & production
        Rogzy – Coordination
        Rachel – Communication
        Pantamis – Interview
        WillKek – Chapitrage

---

A propose du prof. 


Loïc Morel
PDG de Pandul

Fondateur de Pandul, je suis un jeune autodidacte, passionné de Bitcoin et de cryptographie. J’essaie, à mon humble échelle, de transmettre mon savoir et mon savoir-faire sur Bitcoin et son environnement, en me focalisant sur la confidentialité, la souveraineté de l’utilisateur et les stratégies de sécurisation.

Retrouvez tous les travaux de Loic sur sa page professeur

---

Curriculum:


# Chapitre 1 - Introduction

Récuper le texte video

intro by rogzy - https://youtu.be/ul8zU5QWIXg

intro by loic - https://youtu.be/mwuxXLk4Kws



![Alt Text](Formation\courses\Crypto301\assets\Bitcoin démocratisé 1 _ Bitcoin et la cryptographie. (2)(1).pdf)


![Alt Text](Formation\courses\Crypto301\assets\Bitcoin démocratisé 2 _ Le portefeuille Bitcoin. (1)(1).pdf)

# Chapitre 2 - Les fonctions de hachage
## 2.1 – Les fonctions de hachage cryptographiques

![2.1 - les fonctions de hachage cryptographiques](https://youtu.be/dvnGArYvVr8)

### Introduction aux fonctions de hachage cryptographique dans le cadre du protocole Bitcoin

Cet article est consacré aux fonctions de hachage cryptographique au sein du protocole Bitcoin. Les fonctions de hachage représentent une part cruciale de la sécurité de Bitcoin, dans la mesure où elles transforment des informations de taille variable en une empreinte digitale, ou hash, de taille fixe. Dans le présent document, nous examinerons en détail les spécificités des fonctions de hachage cryptographique, leur rôle dans le protocole Bitcoin, ainsi que les finalités de la fonction de hachage cryptographique.
Propriétés des fonctions de hachage cryptographique et leur application

Les fonctions de hachage cryptographique se caractérisent par leur irréversibilité et leur résistance à l'altération. Chaque entrée distincte aboutit à un hash unique par le biais d'une fonction de hachage cryptographique. Une modification même infime de l'entrée se traduit par une transformation importante du hash. Les fonctions de hachage cryptographique sont couramment employées pour vérifier l'intégrité de logiciels téléchargés. La résistance aux collisions constitue une propriété fondamentale d'une fonction de hachage cryptographique. Bien que les collisions soient inévitables, une fonction de hachage cryptographique adéquate parvient à les réduire au minimum. L'attaque des anniversaires représente une limite inhérente à la résistance aux collisions. Pour SHA256, la résistance aux collisions attendue est de 2^128.

Les fonctions SHA0, SHA1 et MD5 sont obsolètes et souvent déconseillées, du fait de leur insuffisante résistance aux collisions. Le principe des tiroirs explique qu'une limitation de la taille de la sortie rend inévitable l'apparition de collisions. La résistance à la seconde préimage est liée à la résistance aux collisions. Une fonction de hachage cryptographiquement sûre doit résister aux collisions, à la seconde préimage et à la préimage.
Application de différentes fonctions de hachage dans le cadre du protocole Bitcoin et objectifs de la fonction de hachage cryptographique

La fonction de hachage SHA-256 est la plus utilisée dans le protocole Bitcoin. SHA-512 est appliquée pour la dérivation avec HMAC et PBKDF. RIPMD160 est employée pour réduire une empreinte à 160 bits. H.256 et H.160 désignent l'utilisation d'un double hachage avec SHA-256 et RIPMD. L'usage de H.160 permet de profiter de la sécurité de SHA-256 tout en diminuant la taille de l'empreinte.

La fonction de hachage cryptographique vise à produire une information de taille fixe à partir d'une information de taille variable. Pour être considérée comme sûre, elle doit posséder les caractéristiques suivantes : irréversibilité, résistance à l'altération, résistance aux collisions, et résistance à la seconde préimage.
Conclusion

Au cours de cet exposé, nous avons étudié les fonctions de hachage cryptographique, leur rôle dans le protocole Bitcoin, et les finalités de la fonction de hachage cryptographique. 

Dans notre prochain cours, nous étudierons en détail la fonction de hachage SHA256 et les mathématiques qui permettent ses caractéristiques.



## 2.2 – Les rouages de SHA256

![2.2 - Les rourages de SHA256](https://youtu.be/74SWg_ZbUj4)

Démystification de SHA256 : Pré-traitement et initialisation

Cet article met en lumière les principes sous-jacents de SHA256, qui ont été introduits dans notre précédent cours portant sur les fonctions de hachage et leurs caractéristiques spécifiques. Pour commencer, le pré-traitement de SHA256 débute avec l'ajout de bits de remplissage pour porter la taille de l'entrée à un multiple de 512 bits. Le but ultime de SHA256 est de générer un hash de 256 bits à partir d'une donnée d'une taille quelconque.

Dans ce processus, nous nous concentrons sur les bits, avec une taille de message initial M. Un bit est alloué pour le séparateur et P bits sont utilisés pour le rembourrage. De plus, 64 bits sont réservés pour la deuxième phase de pré-traitement. L'ensemble doit correspondre à N x 512 bits.
Fonction de compression de SHA256

La deuxième phase du prétraitement implique l'ajout de la représentation binaire de la taille du message initial, en bits. Pour cela, nous utilisons 64 bits pour le remplissage de la taille, prévus à l'étape précédente. Nous ajoutons des zéros pour obtenir nos 64 bits dans notre entrée équilibrée. Ensuite, nous concaténons le message initial, le remplissage des bits et le remplissage de la taille pour obtenir notre entrée équilibrée.

Pour les premières étapes de traitement de la fonction SHA-256, nous définissons des constantes et des vecteurs d'initialisation. Les vecteurs d'initialisation, associés aux lettres de A à H, sont exprimés en hexadécimal. Ils représentent les 32 premiers bits des parties décimales des racines carrées des 8 premiers nombres premiers. Les constantes K de 0 à 63 représentent les 32 premiers bits des parties décimales des racines cubiques des 64 premiers nombres premiers.

Des opérateurs tels que XOR, AND et NOT sont utilisés dans la fonction de compression. Nous traitons les bits un par un en fonction de leur rang, en utilisant l'opérateur XOR et la table de vérité. L'opérateur AND est utilisé pour retourner 1 si les deux opérandes sont égales à 1, et l'opérateur NOT pour renvoyer la valeur opposée d'une opérande. Nous utilisons également l'opération SHR pour décaler les bits vers la droite selon un nombre sélectionné.
Résistance de SHA256 aux attaques et ses applications

Pour recevoir une information de taille arbitraire comme entrée de la fonction SHA256, nous appliquons des bits de remplissage et le remplissage de taille. Nous définissons certaines constantes et vecteurs d'initialisation, puis définissons les calculs qui sont utilisés au sein de la fonction de compression.

Nous séparons l'entrée équilibrée en différents blocs de messages de 512 bits, puis effectuons 64 tours de calcul dans la fonction de compression. Nous additionnons modulo 2^32 l'état intermédiaire à l'état initial de la fonction de compression. Les additions dans la fonction de compression sont des additions modulo 2^32 pour réduire la taille des sommes à 32 bits.

Nous concluons en soulignant l'importance des calculs effectués dans les boîtes CH, MAJ, σ0 et σ1. CH prend en entrée E, F et G et donne CH(E, F, G), égal à (E AND F) XOR ((NOT E) AND G). MAJORITY prend en entrée A, B et C et donne (A AND B) XOR (A AND C) XOR (B AND C). Ces opérations, parmi d'autres, garantissent la robustesse de la fonction de hachage SHA256 face aux attaques, faisant de celle-ci un choix privilégié pour la sécurisation de nombreux systèmes numériques, notamment au sein du protocole Bitcoin.





## 2.3 – Les algorithmes utilisés pour la dérivation

Analyse des algorithmes de dérivation basés sur les fonctions de hachage

Cet article décortique l'utilisation des algorithmes de dérivation HMAC et PBKDF2, fondamentalement liés aux fonctions de hachage, dans le cadre du protocole Bitcoin. Ces algorithmes jouent un rôle crucial dans l'établissement de la sécurité du système, prévenant diverses attaques potentielles et assurant l'intégrité des portefeuilles de Bitcoin.
HMAC et PBKDF2 : Boucliers contre les attaques

Le protocole Bitcoin repose sur deux algorithmes de dérivation : HMAC et PBKDF2. L'HMAC est essentiellement utilisé pour contrer les attaques par extension de longueur lors de la dérivation des portefeuilles HD, tandis que le PBKDF2 est employé pour transformer la phrase mémonique en graine.

HMAC, qui accepte un message et une clé comme entrées, génère une sortie de taille fixe. Pour garantir la cohérence, la clé est ajustée en fonction de la taille des blocs utilisés dans la fonction de hachage.
HMAC-SHA-512 : Protection des portefeuilles HD

L'HMAC-SHA-512, utilisé dans la dérivation des portefeuilles HD, fonctionne avec des blocs de 1024 bits (128 octets), la clé étant ajustée en conséquence. Les constantes OPAD (0x5c) et IPAD (0x36) sont répétées B fois, chacune étant unique pour chaque utilisation afin de renforcer la sécurité.

Le fonctionnement de l'HMAC-SHA-512 se résume en la concaténation du résultat de SHA-512 appliqué sur K' XOR OPAD et sur K' XOR IPAD avec le message. Lors de l'utilisation de l'HMAC-SHA-512 avec des blocs de 1024 bits (128 octets), la clé d'entrée est ajustée avec des zéros si nécessaire, et ensuite XORée avec IPAD et OPAD. ICLEPAD est alors concaténé avec le message.
Code de chaîne et Sécurité des bitcoins

Le code de chaîne, intégrant une source supplémentaire d'entropie, renforce la sécurité des paires enfants dérivées. Sans lui, une attaque pourrait compromettre l'ensemble du portefeuille et voler tous les bitcoins.

HMAC SHA512 est largement utilisé pour la dérivation des paires enfants ainsi que pour la conversion de la graine en clé maîtresse et en code de chaîne maître.
PBKDF2 : De la phrase mémonique à la graine

PBKDF2 est employé pour passer de la phrase mémonique à la graine. L'algorithme réalise 2048 tours et utilise HMAC SHA512.
Conclusion : Des entrées multiples, une sortie fixe

Grâce aux algorithmes de dérivation, deux entrées différentes peuvent donner une sortie unique et fixe, ce qui pallie le problème des attaques par extension de longueur possibles sur les fonctions de la famille SHA-2.

Ainsi, l'utilisation des algorithmes HMAC et PBKDF2 assure la sécurité de la dérivation des portefeuilles HD dans le protocole Bitcoin. L'algorithme HMAC-SHA-512 est utilisé pour éviter les attaques par extension de longueur, tandis que PBKDF2 permet de passer de la phrase mémonique à la graine. Le code de chaîne ajoute une source d'entropie dans la dérivation des paires enfants, et les algorithmes permettent d'utiliser deux entrées différentes sur de la dérivation pour sortir avec un output unique et fixe.

![2.3 – Les algorithmes utilisés pour la dérivation](https://youtu.be/ZF1_BMsOJXc)

# Chapitre 3 - Les signatures numériques
## 3.1 – Signatures numériques et courbes elliptiques

![3.1 – Signatures numériques et courbes elliptiques](https://youtu.be/gOjYiPkx4z8)

La sécurité des transactions est au cœur du protocole Bitcoin, qui repose sur l'utilisation de signatures numériques. Ces dernières constituent une preuve mathématique de la possession d'une clé privée correspondant à une clé publique spécifique. Le système de sécurité de Bitcoin est fondé sur la cryptographie à courbes elliptiques.

### Introduction à la cryptographie à courbes elliptiques

La cryptographie à courbes elliptiques (ECC) est au cœur de la sécurité des transactions Bitcoin. Les courbes elliptiques sont exploitables dans diverses applications cryptographiques, comme les échanges de clés, le chiffrement asymétrique et la création de signatures numériques. Une propriété essentielle des courbes elliptiques est leur symétrie: toute droite non-verticale intersectant deux points de la courbe en coupera toujours un troisième.

Bitcoin utilise spécifiquement la courbe elliptique SecP256K1 pour ses opérations cryptographiques. Cette courbe est définie sur un corps fini d'entiers positifs modulo un nombre premier de 256 bits. Les courbes elliptiques appliquées à Bitcoin ne sont pas exactement des courbes sur le corps des réels, mais elles sont plutôt conceptualisées comme des nuages de points pour une meilleure compréhension.

La courbe secp256k1 a été préférée à la courbe secp256r1, que Satoshi Nakamoto n'a pas retenue pour Bitcoin. Elle est définie par les paramètres a=0 et b=7. Le nombre premier P détermine l'ordre de la courbe utilisée dans Bitcoin. L'équation de cette courbe elliptique est y² = x³ + 7 modulo P.

### Fonctionnement des portefeuilles Bitcoin

Un portefeuille Bitcoin n'emmagasine pas directement des bitcoins, mais conserve les clés privées nécessaires pour démontrer la possession de ces derniers. En effet, les bitcoins sont stockés sur la blockchain, une base de données décentralisée qui enregistre l'ensemble des transactions.

Dans le système Bitcoin, l'unité de compte est le bitcoin (avec un "b" minuscule). Un bitcoin est divisible jusqu'à la huitième décimale, l'unité la plus petite étant le satoshi. Les UTXO, ou "Unspent Transaction Output", représentent les sorties de transactions non dépensées appartenant à un utilisateur. Chaque UTXO est lié à une clé publique associée à une clé privée. Pour utiliser les bitcoins, il faut fournir une preuve mathématique de la possession de la clé privée correspondante.
3.6. Possession des UTXO

La possession des UTXO est liée à une clé publique, elle-même associée à une clé privée. Cette dernière sécurise les fonds de l'utilisateur. Pour dépenser des bitcoins, il est nécessaire de prouver la possession de la clé privée ( à savoir une preuve mathématique).

Deux algorithmes de signature numérique sont utilisés dans le protocole Bitcoin : l'ECDSA (Elliptic Curve Digital Signature Algorithm) et Schnorr. ECDSA est un protocole de signature présent dans Bitcoin depuis son lancement en 2009. Les signatures de Schnorr, quant à elles, ont été introduites plus récemment, en novembre 2021. Bien que ces deux protocoles soient basés sur la cryptographie à courbes elliptiques et utilisent des mécanismes mathématiques similaires, ils diffèrent principalement par la structure de la signature.

Avant d'explorer plus en détail ces mécanismes de signatures numériques, il est important de comprendre ce qu'est une courbe elliptique. Ces courbes sont largement employées dans différents domaines de la cryptographie, comme les échanges de clés, le chiffrement asymétrique et la création de signatures numériques. Les courbes elliptiques présentent une symétrie caractéristique: toute droite non-verticale intersectant deux points de la courbe en coupera toujours un troisième. De plus, toute ligne non verticale et tangente à la courbe en un point intersectera toujours la courbe en un deuxième point unique. Toute courbe elliptique est définie par l'équation y² = x³ + ax + b.

Plusieurs standards de courbes elliptiques sont reconnus comme étant sécurisés pour une utilisation cryptographique. Le plus connu est sans doute la courbe secp256r1. Cependant, Satoshi Nakamoto a choisi une autre courbe pour Bitcoin, à savoir la courbe secp256k1.

Pour une compréhension plus approfondie, la clé publique et la clé privée seront examinées de plus près dans la prochaine partie de ce cours, dédiée à la cryptographie sur les courbes elliptiques et à l'algorithme de signature numérique.


## 3.2 – Calculer la clé publique depuis la clé privée

![3.2 – Calculer la clé publique depuis la clé privée](https://youtu.be/NJENwFU889Y)



Dans ce cours, nous nous concentrons sur les mécanismes des clés publiques et privées. Pour rappel, ces clés sont mathématiquement liées dans Bitcoin grâce à l'algorithme Elliptic Curve Digital Signature Algorithm (ECDSA).
### Algorithme ECDSA et clés privées pour Bitcoin

Le protocole Bitcoin exploite un algorithme de signature numérique nommé ECDSA. Dans cette méthode, la clé privée est un nombre aléatoire ou pseudo-aléatoire de 256 bits. Alors que le nombre de possibilités pour une clé privée sur Bitcoin est théoriquement de 2^256, il est légèrement inférieur à cela en réalité. Autrement dit, certaines clés privées de 256 bits ne sont pas valides pour Bitcoin.

Pour qu'une clé privée soit applicable à Bitcoin, elle doit être comprise entre 1 et n-1, où n représente l'ordre de la courbe elliptique. Le nombre total de possibilités pour une clé privée sur Bitcoin est pratiquement égal à 1,158 x 10^77. C'est à peu près le même nombre d'atomes qu'il y a dans l'univers observable. Cette clé privée unique permet de déterminer la clé publique de 512 bits.

### Opérations de points sur une courbe elliptique pour calculer des clés publiques

La clé publique, qui est un point sur la courbe elliptique noté K, est dérivée de la clé privée via des opérations de points sur une courbe elliptique. La fonction ECDSA est irréversible, c'est-à-dire qu'on ne peut pas retrouver la clé privée à partir de la clé publique. C'est sur ce principe que repose la sécurité du portefeuille Bitcoin. La clé publique sert à recevoir des fonds tandis que la clé privée permet de les débloquer.

La clé publique est constituée de deux points de 256 bits chacun, soit 512 bits au total. Cependant, elle peut être compressée en un nombre de 264 bits. Le point G est le point de départ pour calculer toutes les clés publiques de tous les utilisateurs du système.

Une propriété remarquable des courbes elliptiques est que toute droite coupant la courbe en deux points va également couper la courbe en un troisième point, nommé le point O. On utilise cette propriété pour déterminer le point U, qui est l'opposé du point O. Pour ajouter un même point à lui-même, on trace la tangente à la courbe en ce point, ce qui donne un nouveau point unique appelé j. Le produit scalaire d'un point par n revient à ajouter ce point à lui-même n fois.

Le calcul des clés publiques repose sur ces opérations de points sur une courbe elliptique. Connaissant la clé privée, il est facile de calculer la clé publique. En revanche, il est impossible de calculer la clé privée si l'on ne connaît que la clé publique. Une droite verticale permet de déterminer un point, mais pas la tangente qui le coupe. La sécurité des clés publiques et privées repose sur le problème du logarithme discret.

Le prochain cours traitera de la réalisation d'une signature numérique en utilisant l'algorithme ECDSA avec une clé privée pour débloquer des bitcoins.

## 3.3 – Signer avec la clé privée

![3.3 – Signer avec la clé privée](https://youtu.be/h2hIyGgPqkM)


Le processus de signature numérique est un moyen de prouver que vous possédez une clé privée sans avoir à la divulguer. Cela s'effectue à l'aide de la méthode ECDSA, qui implique la détermination d'un nonce unique, le calcul du nombre V et la composition de la signature numérique en deux parties, S1 et S2. Il est essentiel de choisir un nonce unique pour prévenir les attaques. Un exemple bien connu de l'échec de cette précaution est celui de la PlayStation 3, qui a été piratée en raison de la réutilisation de nonce.

Pour vérifier une signature numérique, vous devez calculer un point P en utilisant S1, S2, H et K. Si I modulo N est égal à S1, alors la signature est considérée comme valide et la transaction peut être inscrite.

Concernant la génération de clés publiques et privées, les utilisateurs doivent être familiarisés avec la courbe elliptique et le point générateur. Pour obtenir la clé publique, il faut choisir un nombre aléatoire pour la clé privée et utiliser la formule de la courbe elliptique.

La courbe elliptique permet de générer des clés publiques et privées plus sûres. Par exemple, pour obtenir la clé publique 3G, vous dessinez la tangente au point G, calculez l'opposé de -G pour obtenir 2G, puis additionnez G et 2G. Pour effectuer une transaction, vous devez prouver que vous connaissez le nombre 3 en déverrouillant les bitcoins associés à la clé publique 3G.

Pour créer une signature numérique et prouver que vous connaissez la clé privée associée à la clé publique 3G, vous calculez un nonce, puis le point V associé à ce nonce (dans l'exemple donné, c'est 4G). Ensuite, vous calculez le point T en additionnant la clé publique 3G et le point V, ce qui donne 7G.

Pour vérifier la signature numérique, vous transmettez le nombre T minuscule (7 dans l'exemple donné) et le point V majuscule (4G dans l'exemple donné) au vérificateur.

Ensuite, le portefeuille déterministe hiérarchique, ou HD, est un mécanisme qui aide à une meilleure compréhension et utilisation du portefeuille. Il utilise des fonctions de hachage et une dérivation sur les courbes elliptiques. Les étapes du portefeuille HD comprennent la phrase mémonique, les graines, la clé étendue, la clé maîtresse, la dérivation des clés enfants, la structure de dérivation et les chemins de dérivation.

Il est essentiel de comprendre comment calculer manuellement une adresse de réception et d'apprendre à utiliser le portefeuille plus efficacement pour renforcer la sécurité de votre crypto-monnaie. Pour en savoir plus sur le portefeuille déterministe hiérarchique, consultez le cours 4.1.


# Chapitre 4 - La phrase mnémonique
## 4.1 – Évolution des portefeuilles Bitcoin

![4.1 – Évolution des portefeuilles Bitcoin](https://youtu.be/6tmu1R9cXyk)

Le portefeuille HD est un outil crucial dans le monde des crypto-monnaies. Son unicité réside dans son utilisation d'une clé privée de 256 bits, offrant ainsi une multitude de possibilités. Il est également connu comme un portefeuille JBOC (Just a Bunch of Keys), ce qui le rend facile à utiliser et à stocker.

Cependant, des contraintes d'utilisation existent pour le portefeuille HD, en particulier en ce qui concerne la sauvegarde unique des informations essentielles au fonctionnement du portefeuille. C'est ici que les différents BIP (Bitcoin Improvement Proposals) interviennent.

Le BIP32, publié en 2012, a introduit le concept de portefeuille déterministe hiérarchique ou HD. L'idée était de dériver les clés privées de manière déterministe et hiérarchique, ce qui facilite la sauvegarde de toutes les clés de votre portefeuille.

Par la suite, le BIP39 a introduit la phrase mémonique de 24 mots, facilitant encore plus la sauvegarde de toutes les clés de votre portefeuille. Le BIP38 a proposé l'utilisation d'une phrase de passe sur des paires de clés uniques, avant que le BIP39 ne l'applique aussi au portefeuille HD. Le BIP43, quant à lui, a défini une standardisation de la structure du portefeuille HD et le BIP44 a établi les schémas de hiérarchisation pour le portefeuille HD.

Les chapitres 4 et 5 exploreront en détail toutes les étapes de dérivation du portefeuille HD.

Enfin, nous étudierons l'information aléatoire pour le portefeuille HD. L'entropie et la définition d'un nombre aléatoire sont des éléments clés pour garantir la sécurité de votre portefeuille HD.

En résumé, les BIP32 et BIP39 sont particulièrement importants dans la définition des portefeuilles HD. Le portefeuille HD dérive toutes les clés enfants à partir d'une information unique, supposée être aléatoire ou pseudo-aléatoire, à la base du portefeuille. De plus, le BIP32 est un nouveau standard pour les portefeuilles déterministes hiérarchiques dans l'écosystème des crypto-monnaies et est aujourd'hui utilisé sur tous les portefeuilles, qu'ils soient spécialisés sur certaines crypto-monnaies, multicoin ou bitcoin only.

J'espère que ce cours vous a aidé à approfondir votre compréhension du portefeuille HD et de ses différentes caractéristiques.


## 4.2 – Entropie et nombre aléatoire

![4.2 – Entropie et nombre aléatoire](https://youtu.be/k18yH18w2TE)

La sécurité des clés privées est fondamentale pour assurer la sécurité des transactions Bitcoin. Les clés privées doivent être générées de manière aléatoire pour prévenir les vulnérabilités liées à la prédictibilité. Cependant, la génération constante de nouvelles clés privées peut s'avérer fastidieuse pour l'utilisateur.

### Génération de nombres aléatoires en cryptographie

Une solution à cette difficulté est le portefeuille déterministe hiérarchique (HD), qui permet une dérivation déterministe et hiérarchique des paires de clés enfants à partir d'une seule et unique information située à la base du portefeuille. Pour garantir la sécurité des clés dérivées, cette information doit être aléatoire.

La génération de nombres aléatoires est fondamentale en cryptographie et est essentielle pour assurer la sécurité des clés privées. Pour être sécurisée et éviter toute vulnérabilité liée à la prédictibilité, une clé privée doit être aléatoire.

Utiliser une nouvelle paire de clés pour chaque transaction peut également renforcer la sécurité, mais cela complique la sauvegarde et assure une préservation partielle de la vie privée. En résumé, la sécurité des clés privées est une nécessité absolue et requiert une génération aléatoire rigoureuse. Le portefeuille HD offre une solution pour simplifier la génération et la gestion des clés tout en maintenant un niveau de sécurité élevé.


### Importance de l'aléatoire dans la génération de clés privées pour Bitcoin

L'importance de l'aléatoire dans la génération de clés privées pour Bitcoin ne peut pas être sous-estimée. La génération d'un nombre aléatoire est essentielle pour garantir la sécurité des clés privées et pour générer de nouvelles clés à partir d'une seule information à la base du portefeuille Bitcoin.

Cependant, la génération de nombres aléatoires sur les ordinateurs pose un problème, car les résultats ne sont pas vraiment aléatoires. C'est pour cette raison qu'il est indispensable d'utiliser un générateur de nombres aléatoires (RNG).

Il existe plusieurs types de RNG : les PRNG (Pseudo-Random Number Generators), les TRNG (True Random Number Generators) et les PRNG avec entropie.

Les PRNG avec entropie utilisent des sources externes d'informations exploitables sur un ordinateur, mais qui sont physiques et ne dépendent pas de l'ordinateur lui-même. Les PRNG doivent être statistiquement aléatoires, imprévisibles, résistants même si les résultats précédents sont connus et doivent avoir une période suffisamment longue pour éviter la répétition.

Dans le cas de Bitcoin, les clés privées sont générées à partir d'une seule information à la base du portefeuille, ce qui permet une dérivation déterministe et hiérarchique des paires de clés enfants. L'entropie est le fondement de tout portefeuille HD, mais il n'existe pas de standard pour la génération de ce nombre aléatoire. Par conséquent, la génération de nombres aléatoires est un enjeu de taille dans la sécurisation des transactions Bitcoin.

### Vérification de la génération de clés

L'étape de vérification de la génération de clés est cruciale pour assurer la sécurité et l'authenticité de la génération de nombres aléatoires, une étape fondamentale pour éviter toute vulnérabilité associée à la prévisibilité. L'utilisation de portefeuilles open source est fortement recommandée pour permettre cette vérification.

Il faut néanmoins noter que certains portefeuilles matériels peuvent être "closed source", ce qui rend impossible la vérification de la génération du nombre aléatoire. Une solution pourrait être de générer soi-même sa phrase mémonique avec des dés, bien que cette méthode puisse présenter des risques. L'utilisation d'une passphrase générée aléatoirement peut aider à atténuer ces risques.

Un exemple de cette méthode serait l'option "dice roll" offerte par CoinKit pour générer des phrases mémoniques. Une autre méthode serait d'utiliser une information initiale très large et de réduire cette information à 256 bits avec la fonction de hachage SHA-256, ce qui pourrait générer un bon nombre aléatoire. Il est à noter que la fonction de hachage SHA-256 résiste aux collisions, à la falsification, et aux attaques de pré-image et de seconde pré-image.

En conclusion, l'aléatoire joue un rôle central dans la cryptographie et l'informatique, et la capacité à générer de l'aléatoire de manière sécurisée est cruciale pour garantir la sécurité des clés privées et des transactions dans Bitcoin. L'entropie, qui est à la base du portefeuille HD de Bitcoin


## Soutiens la formation !

Partage cette formation sur tes réseaux, ca nous aide beaucoup ! oui lounes et muriel faut un truc standard. 


## 4.3 – La phrase mnémonique

![4.3 – La phrase mnémonique](https://youtu.be/uJERqH9Xp7I)


La sécurité d'un portefeuille Bitcoin est primordiale pour tout utilisateur. Pour assurer la sauvegarde du portefeuille, il est essentiel de générer une phrase mémonique à partir de l'entropie et de la checksum.

L'entropie est à la base de la sécurité du portefeuille HD. Il existe plusieurs méthodes pour générer cette entropie, notamment à travers des générateurs de nombres pseudo-aléatoires (PRNG), des générateurs de nombres aléatoires véritables (TRNG) ou manuellement. Il est fondamental que cette entropie soit aléatoire ou pseudo-aléatoire pour garantir la sécurité du portefeuille.

La checksum, de son côté, permet de confirmer l'exactitude de la phrase de récupération. Sans cette checksum, une erreur dans la phrase pourrait générer un portefeuille différent et entraîner la perte des fonds. La checksum est obtenue en passant l'entropie par la fonction SHA256 et en récupérant les 8 premiers bits du hachage.

Il existe différents standards pour la phrase mémonique selon la taille de l'entropie. Le standard le plus couramment utilisé pour une phrase de récupération de 24 mots est une entropie de 256 bits. La taille de la checksum est déterminée en divisant la taille de l'entropie par 32.

À titre d'exemple, une entropie de 256 bits donne une checksum de 8 bits. Ensuite, la concaténation de l'entropie et de la checksum donne respectivement des tailles de 128 bits, 160 bits, etc. En fonction de la taille de l'entropie, la phrase de récupération comprendra 12 mots pour 128 bits, 15 mots pour 160 bits et 24 mots pour 256 bits.

Les bits sont convertis en phrases en associant chaque segment à un mot provenant d'une liste de 2048 mots. Il est important de noter qu'aucun mot ne présente les quatre premières lettres dans le même ordre.

La sauvegarde de la phrase de récupération de 24 mots est essentielle pour maintenir l'intégrité du portefeuille Bitcoin. Les deux standards les plus courants sont ceux avec une entropie de 128 ou 256 bits et une concaténation de 12 ou 24 mots. La passphrase est une option supplémentaire pour renforcer la sécurité du portefeuille.

En conclusion, la génération d'une phrase mémonique pour la sécurisation du portefeuille Bitcoin est un processus crucial. Les standards de la phrase mémonique doivent être respectés en fonction de la taille de l'entropie. La sauvegarde de la phrase de récupération de 24 mots est primordiale pour éviter toute perte de fonds. Merci de votre attention et à bientôt pour le prochain cours sur la crypto-monnaie.

## 4.4 – Parenthèse sur la passphrase 


![4.4 – Parenthèse sur la passphrase ](https://youtu.be/dZkOYO7MXwc)


La passphrase est un mot de passe supplémentaire qui peut être ajouté à un portefeuille Bitcoin pour renforcer sa sécurité. C'est un choix optionnel qui revient à l'utilisateur. La passphrase augmente la sécurité d'un portefeuille en ajoutant des informations arbitraires qui, lorsqu'elles sont combinées avec la phrase mémonique, permettent de calculer la graine du portefeuille.

Pour dériver les clés d'un portefeuille HD, la phrase mémonique et la passphrase sont nécessaires. La passphrase est libre et peut atteindre une taille presque infinie. Elle n'est pas incluse dans la phrase mémonique, qui est standardisée et doit respecter certaines contraintes de taille, de checksum et de codage. Un attaquant ne peut pas accéder aux bitcoins d'un utilisateur sans découvrir la passphrase. Cette dernière intervient dans la construction et le calcul de toutes les clés du portefeuille.

La fonction pbkdf2 est utilisée pour générer la graine à partir de la passphrase. Cette graine permet de dériver toutes les paires de clés enfants du portefeuille. Si la passphrase est modifiée, le portefeuille Bitcoin devient totalement différent.

La passphrase est un outil clé pour renforcer la sécurité des portefeuilles Bitcoin. Elle peut permettre l'application de diverses stratégies de sécurité. Par exemple, elle peut être utilisée pour créer des doublons et faciliter les sauvegardes de la phrase mémonique. Elle peut également améliorer la sécurité du portefeuille en atténuant les risques associés à la génération aléatoire de la phrase mémonique.

Une passphrase efficace devrait être longue (20 à 40 caractères) et diversifiée (utilisant des majuscules, des minuscules, des chiffres et des symboles). Elle ne devrait pas être directement liée à l'utilisateur ou à son environnement. Il est plus prudent d'utiliser une séquence aléatoire de caractères plutôt qu'un mot simple comme passphrase.

Une passphrase est plus sécurisée qu'un simple mot de passe. La passphrase idéale est longue, variée et aléatoire. Elle peut renforcer la sécurité d'un portefeuille ou d'un logiciel chaud. Elle peut également être utilisée pour créer des sauvegardes redondantes et sécurisées.

Il est essentiel de prendre soin des sauvegardes de la passphrase pour éviter de perdre l'accès au portefeuille. Une passphrase est une option pour un portefeuille HD. Elle peut être générée aléatoirement avec des dés ou un autre générateur de nombres pseudo-aléatoires. Il est déconseillé de mémoriser une passphrase ou une phrase mémonique.

Dans notre prochain cours, nous examinerons de manière approfondie le fonctionnement de la graine et la première paire de clés générée à partir de celle-ci. N'hésitez pas à cliquer sur le cours pour continuer votre apprentissage. Au plaisir de vous retrouver prochainement.


## 4.5 – Création d’une seed depuis 128 lancés de dés ! [ATELIER]

![4.5 – Création d’une seed depuis 128 lancés de dés ! [ATELIER]](https://youtu.be/lUw-1kk75Ok)



# Chapitre 5 - Création d’un portefeuille Bitcoin
## 5.1 – Création de la graine et de la clé maîtresse

![5.1 – Création de la graine et de la clé maîtresse](https://youtu.be/56yAt_JDWhY)

## 5.2 – Les clés étendues

![5.2 – Les clés étendues](https://youtu.be/TRz760E_zUY)

## 5.3 – Dérivation des paires de clés enfants

![5.3 – Dérivation des paires de clés enfants](https://youtu.be/FXhI-GmE9Aw)

## 5.4 – Structure du portefeuille et chemins de dérivation

![5.4 – Structure du portefeuille et chemins de dérivation](https://youtu.be/etO9UxwyE2I)

# Chapitre 6 - Les adresses Bitcoin



## 6.1 – Les adresses Bitcoin

![6.1 – Les adresses Bitcoin](https://youtu.be/nqGBMjPtFNI)


## Note cette formation 😀



## 6.2 – Comment créer une adresse Bitcoin ?

![6.2 – Comment créer une adresse Bitcoin ?](https://youtu.be/ewMGTN8dKjI)

# Conclusion
## Récapitulatif du processus complet par Loïc

## Soutenir la formation

## Interview avec Théo Pantamis

![Interview avec Théo Pantamis](https://youtu.be/c9MvtGJsEvY)

E-BOOK 1 – Bitcoin et la cryptographie
E-BOOK 2 – Le portefeuille Bitcoin

Ressources pour aller plus loin 