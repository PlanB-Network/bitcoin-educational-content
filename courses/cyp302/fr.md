---
name: Introduction à la cryptographie formelle
goal: Une introduction approfondie à la science et à la pratique de la cryptographie.
objectives: 

  - Explorer les algorithmes de chiffrement de Beale et les méthodes cryptographiques modernes pour comprendre les concepts de base et historiques de la cryptographie.
  - Plongez dans la théorie des nombres, des groupes et des champs pour maîtriser les concepts mathématiques clés qui sous-tendent la cryptographie.
  - Étudiez le chiffrement de flux RC4 et l'AES avec une clé de 128 bits pour vous familiariser avec les algorithmes cryptographiques symétriques.
  - Étudier le système cryptographique RSA, la distribution des clés et les fonctions de hachage pour explorer la cryptographie asymétrique.

---
# Plongée dans la cryptographie

Il est difficile de trouver beaucoup de matériel qui offre un juste milieu dans l'enseignement de la cryptographie.

D'une part, il existe de longs traités formels qui ne sont accessibles qu'aux personnes ayant une solide formation en mathématiques, en logique ou dans une autre discipline formelle. D'autre part, il y a des introductions de très haut niveau qui cachent trop de détails pour quiconque est un tant soit peu curieux.

Cette introduction à la cryptographie cherche à se situer à mi-chemin. Bien qu'elle soit relativement stimulante et détaillée pour toute personne débutant dans le domaine de la cryptographie, elle n'est pas le trou du lapin d'un traité fondamental typique.

+++
# Introduction

<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Brève description

<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Ce livre propose une introduction approfondie à la science et à la pratique de la cryptographie. Dans la mesure du possible, il se concentre sur l'exposition conceptuelle plutôt que formelle de la matière.

> Ce cours est basé sur [le repo de JWBurgers] (https://github.com/JWBurgers/An_Introduction_to_Cryptography). C'est son droit. Le contenu n'est pas encore terminé et n'est là que pour montrer comment nous pourrions l'intégrer si JWburger est d'accord.
### Motivation et objectifs

Il est difficile de trouver beaucoup de matériel qui offre un juste milieu dans l'enseignement de la cryptographie.

D'une part, il existe de longs traités formels qui ne sont accessibles qu'aux personnes ayant une solide formation en mathématiques, en logique ou dans une autre discipline formelle. D'autre part, il y a des introductions de très haut niveau qui cachent trop de détails pour quiconque est un tant soit peu curieux.

Cette introduction à la cryptographie cherche à se situer à mi-chemin. Bien qu'elle soit relativement stimulante et détaillée pour toute personne débutant dans le domaine de la cryptographie, elle n'est pas le trou du lapin d'un traité fondamental typique.

### Public cible

Des développeurs aux personnes intellectuellement curieuses, ce livre est utile à tous ceux qui veulent plus qu'une compréhension superficielle de la cryptographie. Si votre objectif est de maîtriser le domaine de la cryptographie, ce livre est également un bon point de départ.

### Guide de lecture

Le livre contient actuellement sept chapitres : "Qu'est-ce que la cryptographie ?" (chapitre 1), "Fondements mathématiques de la cryptographie I" (chapitre 2), "Fondements mathématiques de la cryptographie II" (chapitre 3), "Cryptographie symétrique" (chapitre 4), "RC4 et AES" (chapitre 5), "Cryptographie asymétrique" (chapitre 6) et "Le système cryptographique RSA" (chapitre 7). Un dernier chapitre, "La cryptographie en pratique", sera encore ajouté. Il se concentre sur diverses applications cryptographiques, notamment la sécurité de la couche transport, le routage en oignon et le système d'échange de valeur de Bitcoin.

À moins que vous n'ayez une solide formation en mathématiques, la théorie des nombres est probablement le sujet le plus difficile de ce livre. J'en propose une vue d'ensemble au chapitre 3, et elle apparaît également dans l'exposé de l'AES au chapitre 5 et du système de cryptage RSA au chapitre 7.

Si vous avez vraiment du mal avec les détails formels de ces parties du livre, je vous recommande de vous contenter d'une lecture de haut niveau la première fois.

### Remerciements

L'ouvrage qui a le plus influencé la conception de ce cours est _Introduction to Modern Cryptography_ de Jonathan Katz et Yehuda Lindell, CRC Press (Boca Raton, FL), 2015. Un cours d'accompagnement intitulé "Cryptography" est disponible sur Coursera

Les principales sources supplémentaires qui ont été utiles pour créer la vue d'ensemble de ce livre sont Simon Singh, _The Code Book_, Fourth Estate (Londres, 1999) ; Christof Paar et Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) et [un cours basé sur le livre de Paar intitulé "Introduction to Cryptography"] (https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg) ; et Bruce Schneier, Applied Cryptography, 2nd edn, 2015 (Indianapolis, IN : John Wiley & Sons).

Je ne citerai que les informations et les résultats très spécifiques que je tire de ces sources, mais je tiens à reconnaître ici ma dette générale à leur égard.

Pour les lecteurs qui souhaitent acquérir des connaissances plus avancées sur la cryptographie après cette introduction, je recommande vivement le livre de Katz et Lindell. Le cours de Katz sur Coursera est un peu plus accessible que le livre.

### Contributions

Veuillez consulter [le fichier des contributions dans le dépôt] (https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) pour obtenir des indications sur la manière de soutenir le projet.

### Notation

**Termes clés:**

Les termes clés des abécédaires sont introduits en les mettant en gras. Par exemple, l'introduction du cryptogramme Rijndael en tant que terme clé se présenterait comme suit : **Cryptage Rijndael**.

Les termes clés sont explicitement définis, sauf s'il s'agit de noms propres ou si leur signification est évidente dans la discussion.

Une définition est généralement donnée lors de l'introduction d'un terme clé, bien qu'il soit parfois plus pratique de laisser la définition à un stade ultérieur.

**Mots et phrases mis en exergue:**

Les mots et les phrases sont mis en évidence par l'italique. Par exemple, la phrase "Retenez votre mot de passe" se présenterait comme suit : *Mémorisez votre mot de passe*.

**Notation formelle:**

La notation formelle concerne principalement les variables, les variables aléatoires et les ensembles.


- Variables : Elles sont généralement indiquées par une lettre minuscule (par exemple, "x" ou "y"). Parfois, elles sont mises en majuscules pour plus de clarté (par exemple, "M" ou "K").
- Variables aléatoires : Elles sont toujours indiquées par une lettre majuscule (par exemple, "X" ou "Y")
- Ensembles : Ils sont toujours indiqués par des lettres majuscules en gras (par exemple, **S**)

# Qu'est-ce que la cryptographie ?

<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

## Les chiffres de Beale

<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>

Commençons notre enquête dans le domaine de la cryptographie par l'un des épisodes les plus charmants et les plus divertissants de son histoire : celui des chiffres de Beale. [1]

L'histoire des codes Beale est, à mon avis, plus proche de la fiction que de la réalité. Mais elle est censée s'être déroulée comme suit.

Au cours des hivers 1820 et 1822, un homme nommé Thomas J. Beale a séjourné dans une auberge appartenant à Robert Morriss à Lynchburg (Virginie). À la fin de son second séjour, Beale remet à Morriss une boîte en fer contenant des papiers de valeur à conserver.

Quelques mois plus tard, Morriss reçoit une lettre de Beale datée du 9 mai 1822. Elle souligne la grande valeur du contenu de la boîte en fer et donne quelques instructions à Morriss : si ni Beale ni aucun de ses associés ne viennent jamais réclamer la boîte, il devra l'ouvrir exactement dix ans après la date de la lettre (c'est-à-dire le 9 mai 1832). Certains des papiers à l'intérieur seraient écrits en texte normal. Plusieurs autres, en revanche, seraient "inintelligibles sans le secours d'une clef" Cette "clé" sera donc remise à Morriss par un ami anonyme de Beale en juin 1832.

Malgré des instructions claires, Morriss n'a pas ouvert la boîte en mai 1832 et le mystérieux ami de Beale ne s'est jamais manifesté en juin de la même année. Ce n'est qu'en 1845 que l'aubergiste se décide enfin à ouvrir la boîte. Morriss y trouve une note expliquant comment Beale et ses associés ont découvert de l'or et de l'argent dans l'Ouest et les ont enterrés, ainsi que des bijoux, pour les mettre en sécurité. En outre, la boîte contenait trois **ciphertextes**, c'est-à-dire des textes écrits en code qui nécessitent une **clé cryptographique**, ou un secret, et un algorithme pour les déverrouiller. Ce processus de déverrouillage d'un texte chiffré est appelé **décryptage**, tandis que le processus de verrouillage est appelé **chiffrement**. (Comme expliqué au chapitre 3, le terme "chiffrement" peut revêtir plusieurs significations. Dans le nom "Beale ciphers", il est l'abréviation de ciphertexts)

Les trois textes chiffrés que Morriss a trouvés dans la boîte en fer consistent chacun en une série de chiffres séparés par des virgules. Selon la note de Beale, ces textes chiffrés fournissent séparément l'emplacement du trésor, le contenu du trésor et une liste de noms avec les héritiers légitimes du trésor et leurs parts (cette dernière information étant pertinente au cas où Beale et ses associés ne viendraient jamais réclamer la boîte).

Morris a tenté de décrypter les trois textes chiffrés pendant vingt ans. Avec la clé, cela aurait été facile. Mais Morriss n'avait pas la clé et n'a pas réussi à récupérer les textes originaux, ou **plaintexts**, comme on les appelle généralement en cryptographie.

Vers la fin de sa vie, Morriss a transmis la boîte à un ami en 1862. Cet ami a ensuite publié un pamphlet en 1885, sous le pseudonyme de J.B. Ward. Il y décrit l'histoire (supposée) de la boîte, les trois textes chiffrés et la solution qu'il a trouvée pour le deuxième texte chiffré. (Apparemment, il existe une clé pour chaque texte chiffré, et non une clé qui fonctionne pour les trois textes chiffrés, comme Beale semble l'avoir suggéré à l'origine dans sa lettre à Morriss)

Vous pouvez voir le deuxième texte chiffré dans la *Figure 2* ci-dessous. [La clé de ce texte chiffré est la Déclaration d'indépendance des États-Unis. La procédure de décryptage se résume à l'application des deux règles suivantes :


- Pour tout nombre n dans le texte chiffré, trouver le nième mot de la Déclaration d'indépendance des États-Unis
- Remplacez le chiffre n par la première lettre du mot que vous avez trouvé

*Figure 1 : Chiffre de Beale no. 2*

![Figure 1: Beale cipher no 2.](assets/Figure1-1.webp "Figure 1: Beale cipher no. 2")

Par exemple, le premier chiffre du deuxième texte chiffré est 115. Le 115e mot de la Déclaration d'indépendance étant "institué", la première lettre du texte en clair est "i" Le texte chiffré n'indique pas directement l'espacement des mots et les majuscules. Mais après avoir décrypté les premiers mots, vous pouvez logiquement en déduire que le premier mot du texte en clair était simplement "I" (Le texte en clair commence par la phrase "I have deposited in the county of Bedford")

Après décryptage, le second message fournit le contenu détaillé du trésor (or, argent et bijoux) et suggère qu'il a été enterré dans des pots en fer et recouvert de pierres dans le comté de Bedford (Virginie). Les gens adorent les mystères, c'est pourquoi de grands efforts ont été déployés pour décrypter les deux autres codes de Beale, en particulier celui décrivant l'emplacement du trésor. Plusieurs cryptographes de renom se sont même essayés à leur tâche. Cependant, personne n'a encore réussi à décrypter les deux autres textes chiffrés.

**Notes:**

[1] Pour un bon résumé de l'histoire, voir Simon Singh, *The Code Book*, Fourth Estate (Londres, 1999), pp. 82-99. Un court métrage de l'histoire a été réalisé par Andrew Allen en 2010. Vous pouvez trouver le film, "The Thomas Beale Cipher", [sur son site web] (http://www.thomasbealecipher.com/).

[2] Cette image est disponible sur la page Wikipédia consacrée aux chiffres de Beale.

## Cryptographie moderne

<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

La plupart d'entre nous associent la cryptographie à des histoires pittoresques comme celle des chiffres de Beale. Pourtant, la cryptographie moderne diffère de ces exemples historiques sur au moins quatre points importants.

Tout d'abord, historiquement, la cryptographie ne s'est intéressée qu'au **secret** (ou à la confidentialité)[3]. [Les textes chiffrés sont créés pour garantir que seules certaines parties peuvent avoir accès aux informations contenues dans les textes en clair, comme dans le cas des algorithmes de chiffrement de Beale. Pour qu'un système de cryptage serve bien cet objectif, le décryptage du texte chiffré ne doit être possible que si l'on possède la clé.

La cryptographie moderne s'intéresse à un éventail de thèmes plus large que le simple secret. Ces thèmes comprennent principalement (1) **l'intégrité du message**, c'est-à-dire l'assurance qu'un message n'a pas été modifié ; (2) **l'authenticité du message**, c'est-à-dire l'assurance qu'un message provient réellement d'un expéditeur particulier ; et (3) **la non-répudiation**, c'est-à-dire l'assurance qu'un expéditeur ne peut pas nier à tort plus tard qu'il a envoyé un message[4]. [4]

Il est donc important de faire la distinction entre un **système de chiffrement** et un **système cryptographique**. Un schéma de chiffrement ne concerne que le secret. Si un schéma de chiffrement est un schéma cryptographique, l'inverse n'est pas vrai. Un schéma cryptographique peut également servir les autres thèmes principaux de la cryptographie, notamment l'intégrité, l'authenticité et la non-répudiation.

Les thèmes de l'intégrité et de l'authenticité sont tout aussi importants que le secret. Nos systèmes de communication modernes ne pourraient pas fonctionner sans garanties concernant l'intégrité et l'authenticité des communications. La non-répudiation est également une préoccupation importante, par exemple pour les contrats numériques, mais elle est moins omniprésente dans les applications cryptographiques que le secret, l'intégrité et l'authenticité.

Deuxièmement, les systèmes de cryptage classiques, tels que les algorithmes de Beale, impliquent toujours une clé partagée entre toutes les parties concernées. Cependant, de nombreux schémas cryptographiques modernes impliquent non pas une, mais deux clés : une **clé privée** et une **clé publique**. Alors que la première doit rester privée dans toutes les applications, la seconde est généralement connue du public (d'où leurs noms respectifs). Dans le domaine du cryptage, la clé publique peut être utilisée pour crypter le message, tandis que la clé privée peut être utilisée pour le décrypter.

La branche de la cryptographie qui traite des systèmes dans lesquels toutes les parties partagent une clé est connue sous le nom de **cryptographie symétrique**. La clé unique dans ce type de système est généralement appelée **clé privée** (ou clé secrète). La branche de la cryptographie qui traite des systèmes nécessitant une paire de clés privée-publique est connue sous le nom de **cryptographie asymétrique**. Ces branches sont parfois appelées respectivement **cryptographie à clé privée** et **cryptographie à clé publique** (bien que cela puisse prêter à confusion, car les systèmes de cryptographie à clé publique ont également des clés privées).

L'avènement de la cryptographie asymétrique à la fin des années 1970 est l'un des événements les plus importants de l'histoire de la cryptographie. Sans elle, la plupart de nos systèmes de communication modernes, y compris Bitcoin, ne seraient pas possibles, ou du moins très peu pratiques.

Il est important de noter que la cryptographie moderne n'est pas exclusivement l'étude des schémas cryptographiques à clés symétriques et assymétriques (bien que cela couvre une grande partie du domaine). Par exemple, la cryptographie s'intéresse également aux fonctions de hachage et aux générateurs de nombres pseudo-aléatoires, et vous pouvez créer des applications sur ces primitives qui ne sont pas liées à la cryptographie à clé symétrique ou assymétrique.

Troisièmement, les systèmes de cryptage classiques, tels que ceux utilisés dans les codes Beale, relevaient plus de l'art que de la science. Leur sécurité perçue était largement basée sur des intuitions concernant leur complexité. Ils étaient généralement corrigés lorsqu'une nouvelle attaque était découverte, ou abandonnés si l'attaque était particulièrement grave. La cryptographie moderne, en revanche, est une science rigoureuse qui repose sur une approche formelle et mathématique du développement et de l'analyse des schémas cryptographiques. [5]

Plus précisément, la cryptographie moderne est centrée sur les **preuves de sécurité** formelles. Toute preuve de sécurité d'un système cryptographique se déroule en trois étapes :

1.	L'énoncé d'une **définition cryptographique de la sécurité**, c'est-à-dire un ensemble d'objectifs de sécurité et la menace posée par l'attaquant.

2.	L'énoncé de toute hypothèse mathématique concernant la complexité informatique du système. Par exemple, un système cryptographique peut contenir un générateur de nombres pseudo-aléatoires. Bien que nous ne puissions pas prouver leur existence, nous pouvons supposer qu'ils existent.

3.	L'exposé d'une **preuve de sécurité** mathématique du système sur la base de la notion formelle de sécurité et de toute hypothèse mathématique.

Quatrièmement, alors qu'historiquement la cryptographie était principalement utilisée dans le cadre militaire, elle est désormais omniprésente dans nos activités quotidiennes à l'ère numérique. Qu'il s'agisse d'effectuer des opérations bancaires en ligne, de publier des messages sur les médias sociaux, d'acheter un produit sur Amazon avec votre carte de crédit ou de donner un pourboire en bitcoins à un ami, la cryptographie est la condition sine qua non de notre ère numérique.

Compte tenu de ces quatre aspects de la cryptographie moderne, nous pourrions caractériser la **cryptographie** moderne comme la science qui s'intéresse au développement formel et à l'analyse des schémas cryptographiques pour sécuriser l'information numérique contre les attaques adverses[6]. [La sécurité doit être entendue au sens large comme la prévention des attaques qui portent atteinte au secret, à l'intégrité, à l'authentification et/ou à la non-répudiation des communications.

La cryptographie est considérée comme une sous-discipline de la **cybersécurité**, qui vise à empêcher le vol, la détérioration et l'utilisation abusive des systèmes informatiques. Il convient de noter que de nombreux problèmes de cybersécurité n'ont que peu ou pas de lien avec la cryptographie.

Par exemple, si une entreprise héberge localement des serveurs coûteux, elle peut se préoccuper de protéger ce matériel contre le vol et les dommages. Bien qu'il s'agisse d'un problème de cybersécurité, il n'a pas grand-chose à voir avec la cryptographie.

Autre exemple, les **attaques par hameçonnage** sont un problème courant à notre époque moderne. Ces attaques tentent de tromper les gens par le biais d'un courrier électronique ou d'un autre moyen de communication afin qu'ils renoncent à des informations sensibles telles que des mots de passe ou des numéros de carte de crédit. Si la cryptographie peut aider à lutter contre les attaques par hameçonnage dans une certaine mesure, une approche globale ne se limite pas à l'utilisation de la cryptographie.

**Notes:**

[Pour être exact, les principales applications des systèmes cryptographiques concernent le secret. Les enfants, par exemple, utilisent fréquemment des schémas cryptographiques simples pour "s'amuser". Le secret n'est pas vraiment une préoccupation dans ces cas-là.

[4] Bruce Schneier, *Applied Cryptography*, 2nd edn, 2015 (Indianapolis, IN : John Wiley & Sons), p. 2.

[5] Voir Jonathan Katz et Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL : 2015), en particulier les pages 16 à 23, pour une bonne description.

[6] Cf. Katz et Lindell, ibid. p. 3. Je pense que leur caractérisation pose quelques problèmes, c'est pourquoi je présente ici une version légèrement différente de leur déclaration.

## Communications ouvertes

<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

La cryptographie moderne est conçue pour fournir des garanties de sécurité dans un environnement de communication **ouvert**. Si notre canal de communication est si bien protégé que les oreilles indiscrètes n'ont aucune chance de manipuler ou même simplement d'observer nos messages, alors la cryptographie est superflue. Cependant, la plupart de nos canaux de communication sont loin d'être aussi bien protégés.

L'épine dorsale de la communication dans le monde moderne est un gigantesque réseau de câbles à fibres optiques. Passer des appels téléphoniques, regarder la télévision et naviguer sur le web dans un foyer moderne repose généralement sur ce réseau de câbles à fibres optiques (un petit pourcentage peut s'appuyer uniquement sur des satellites). Il est vrai que vous pouvez avoir différentes connexions de données à votre domicile, telles que le câble coaxial, la ligne d'abonné numérique (asymétrique) et le câble à fibre optique. Mais, du moins dans les pays développés, ces différents supports de données sont rapidement reliés, en dehors de votre domicile, à un nœud d'un gigantesque réseau de câbles à fibres optiques qui relie l'ensemble du globe. Les exceptions sont certaines régions éloignées des pays développés, comme les États-Unis et l'Australie, où le trafic de données peut encore parcourir des distances considérables sur les fils téléphoniques traditionnels en cuivre.

Il serait impossible d'empêcher des attaquants potentiels d'accéder physiquement à ce réseau de câbles et à son infrastructure de soutien. En fait, nous savons déjà que la plupart de nos données sont interceptées par diverses agences de renseignement nationales à des intersections cruciales de l'internet[7], qu'il s'agisse de messages Facebook ou d'adresses de sites web que vous visitez.

Si la surveillance de données à grande échelle nécessite un adversaire puissant, tel qu'une agence de renseignement nationale, les attaquants disposant de peu de ressources peuvent facilement tenter d'espionner à une échelle plus locale. Bien que cela puisse se produire au niveau de l'écoute des câbles, il est beaucoup plus facile d'intercepter les communications sans fil.

La plupart des données de notre réseau local - que ce soit à la maison, au bureau ou dans un café - transitent désormais par ondes radio vers les points d'accès sans fil des routeurs tout-en-un, plutôt que par des câbles physiques. Un pirate n'a donc besoin que de peu de ressources pour intercepter votre trafic local. Cette situation est d'autant plus préoccupante que la plupart des gens ne font pas grand-chose pour protéger les données qui transitent par leurs réseaux locaux. En outre, les attaquants potentiels peuvent également cibler nos connexions mobiles à large bande, telles que 3G, 4G et 5G. Toutes ces communications sans fil sont une cible facile pour les attaquants.

Par conséquent, l'idée de garder les communications secrètes en protégeant le canal de communication est une aspiration désespérément illusoire pour une grande partie du monde moderne. Tout ce que nous savons justifie une paranoïa sévère : il faut toujours supposer que quelqu'un écoute. Et la cryptographie est le principal outil dont nous disposons pour obtenir une quelconque sécurité dans cet environnement moderne.

**Notes:**

[7] Voir, par exemple, Olga Khazan, "The creepy, long-standing practice of undersea cable tapping", *The Atlantic*, 16 juillet 2013 (disponible sur [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).

# Fondements mathématiques de la cryptographie 1

<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

## Variables aléatoires

<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

La cryptographie repose sur les mathématiques. Et si vous voulez développer plus qu'une compréhension superficielle de la cryptographie, vous devez être à l'aise avec les mathématiques.

Ce chapitre présente la plupart des mathématiques de base que vous rencontrerez lors de votre apprentissage de la cryptographie. Les sujets abordés comprennent les variables aléatoires, les opérations modulo, les opérations XOR et le pseudo-aléa. Vous devez maîtriser le matériel de ces sections pour une compréhension non superficielle de la cryptographie.

La section suivante traite de la théorie des nombres, qui est beaucoup plus difficile.

### Variables aléatoires

Une variable aléatoire est généralement désignée par une lettre majuscule non grasse. Ainsi, par exemple, on peut parler d'une variable aléatoire $X$, d'une variable aléatoire $Y$ ou d'une variable aléatoire $Z$. C'est la notation que j'emploierai également à partir de maintenant.

Une **variable aléatoire** peut prendre deux ou plusieurs valeurs possibles, chacune ayant une certaine probabilité positive. Les valeurs possibles sont répertoriées dans l'**ensemble des résultats**.

Chaque fois que vous **échantillonnez** une variable aléatoire, vous tirez une valeur particulière de son ensemble de résultats selon les probabilités définies.

Prenons un exemple simple. Supposons une variable X définie comme suit :


- X a l'ensemble de résultats $\{1,2\}$

$$
Pr[X = 1] = 0.5
$$

$$
Pr[X = 2] = 0.5
$$

Il est facile de voir que $X$ est une variable aléatoire. Premièrement, $X$ peut prendre au moins deux valeurs possibles, à savoir $1$ et $2$. Deuxièmement, chaque valeur possible a une probabilité positive de se produire lorsque vous échantillonnez $X$, à savoir 0,5$.

Tout ce dont une variable aléatoire a besoin, c'est d'un ensemble de résultats avec deux possibilités ou plus, où chaque possibilité a une probabilité positive de se produire lors de l'échantillonnage. En principe, une variable aléatoire peut donc être définie de manière abstraite, sans aucun contexte. Dans ce cas, on peut considérer que l'"échantillonnage" consiste à réaliser une expérience naturelle pour déterminer la valeur de la variable aléatoire.

La variable $X$ ci-dessus a été définie de manière abstraite. Vous pouvez donc considérer que l'échantillonnage de la variable $X$ ci-dessus consiste à tirer à pile ou face une pièce de monnaie équitable et à attribuer "2" dans le cas de face et "1" dans le cas de pile. Pour chaque échantillon de $X$, vous jouez à nouveau à pile ou face.

Vous pouvez également considérer l'échantillonnage $X$ comme le lancement d'un dé équitable et l'attribution d'un "2" si le dé tombe sur $1$, $3$ ou $4$, et d'un "1" si le dé tombe sur $2$, $5$ ou $6$. Chaque fois que vous échantillonnez $X$, vous lancez à nouveau le dé.

En réalité, toute expérience naturelle qui permettrait de définir les probabilités des valeurs possibles de $X$ ci-dessus peut être imaginée par rapport au dessin.

Souvent, cependant, les variables aléatoires ne sont pas simplement introduites de manière abstraite. Au contraire, l'ensemble des valeurs de résultats possibles a une signification explicite dans le monde réel (et non pas seulement en tant que nombres). En outre, ces valeurs de résultats peuvent être définies par rapport à un type spécifique d'expérience (plutôt que comme n'importe quelle expérience naturelle avec ces valeurs).

Considérons maintenant un exemple de variable $X$ qui n'est pas définie abstraitement. X est définie comme suit afin de déterminer laquelle des deux équipes commence un match de football :


- $X$ a l'ensemble de résultats {rouge s'éteint, bleu s'éteint}
- Tirer à pile ou face une pièce de monnaie $C$ : pile = "le rouge se met en marche" ; face = "le bleu se met en marche"

$$
Pr [X = \text{red kicks off}] = 0.5
$$

$$
Pr [X = \text{blue kicks off}] = 0.5
$$

Dans ce cas, l'ensemble des résultats de X a une signification concrète, à savoir quelle équipe commence un match de football. En outre, les résultats possibles et leurs probabilités associées sont déterminés par une expérience concrète, à savoir tirer à pile ou face une pièce de monnaie $C$.

Dans les discussions sur la cryptographie, les variables aléatoires sont généralement introduites par rapport à un ensemble de résultats ayant une signification dans le monde réel. Il peut s'agir de l'ensemble des messages susceptibles d'être cryptés, appelé espace des messages, ou de l'ensemble des clés que les parties utilisant le cryptage peuvent choisir, appelé espace des clés.

Toutefois, dans les discussions sur la cryptographie, les variables aléatoires ne sont généralement pas définies par rapport à une expérience naturelle spécifique, mais par rapport à toute expérience susceptible de produire les bonnes distributions de probabilités.

Les variables aléatoires peuvent avoir des distributions de probabilité discrètes ou continues. Les variables aléatoires ayant une **distribution de probabilité discrète** - c'est-à-dire les variables aléatoires discrètes - ont un nombre fini de résultats possibles. La variable aléatoire $X$ dans les deux exemples donnés jusqu'à présent était discrète.

**Les variables aléatoires continues** peuvent prendre des valeurs dans un ou plusieurs intervalles. On peut dire, par exemple, qu'une variable aléatoire, lors de l'échantillonnage, prendra n'importe quelle valeur réelle entre 0 et 1, et que chaque nombre réel de cet intervalle a la même probabilité. Dans cet intervalle, il existe une infinité de valeurs possibles.

Pour les discussions sur la cryptographie, vous n'aurez besoin que de comprendre les variables aléatoires discrètes. Toute discussion sur les variables aléatoires à partir de maintenant doit donc être comprise comme faisant référence aux variables aléatoires discrètes, sauf indication contraire.

### Graphique des variables aléatoires

Les valeurs possibles et les probabilités associées à une variable aléatoire peuvent être facilement visualisées à l'aide d'un graphique. Par exemple, considérons la variable aléatoire $X$ de la section précédente avec un ensemble de résultats de $\{1, 2\}$, et $Pr [X = 1] = 0,5$ et $Pr [X = 2] = 0,5$. Une telle variable aléatoire est généralement représentée sous la forme d'un diagramme à barres, comme dans la *Figure 1*.

*Figure 1 : Variable aléatoire X*

![Figure 1: Random variable X.](assets/Figure2-1.webp)

Les barres larges de la *Figure 1* n'ont évidemment pas pour but de suggérer que la variable aléatoire $X$ est en fait continue. Au contraire, les barres sont larges afin d'être plus attrayantes visuellement (une simple ligne droite vers le haut offre une visualisation moins intuitive).

### Variables uniformes

Dans l'expression "variable aléatoire", le terme "aléatoire" signifie simplement "probabiliste". En d'autres termes, il signifie simplement que deux ou plusieurs résultats possibles de la variable se produisent avec certaines probabilités. Toutefois, ces résultats ne doivent pas nécessairement être également probables (bien que le terme "aléatoire" puisse avoir cette signification dans d'autres contextes).

Une **variable uniforme** est un cas particulier de variable aléatoire. Elle peut prendre deux ou plusieurs valeurs, toutes avec une probabilité égale. La variable aléatoire $X$ représentée dans la *Figure 1* est clairement une variable uniforme, puisque les deux résultats possibles se produisent avec une probabilité de 0,5$. Il existe cependant de nombreuses variables aléatoires qui ne sont pas des exemples de variables uniformes.

Considérons, par exemple, la variable aléatoire $Y$. Elle possède un ensemble de résultats $\{1, 2, 3, 8, 10\}$ et la distribution de probabilité suivante :

$$
\Pr[Y = 1] = 0.25
$$

$$
\Pr[Y = 2] = 0.35
$$

$$
\Pr[Y = 3] = 0.1
$$

$$
\Pr[Y = 8] = 0.25
$$

$$
\Pr[Y = 10] = 0.05
$$

Si deux résultats possibles ont en effet une probabilité égale de se produire, à savoir $1$ et $8$, $Y$ peut également prendre certaines valeurs avec des probabilités différentes de $0,25$ lors de l'échantillonnage. Par conséquent, si $Y$ est bien une variable aléatoire, ce n'est pas une variable uniforme.

Une représentation graphique de $Y$ est fournie dans la *Figure 2*.

*Figure 2 : Variable aléatoire Y*

![Figure 2: Random variable Y.](assets/Figure2-2.webp "Figure 2: Random variable Y")

Pour un dernier exemple, considérons la variable aléatoire Z. Elle possède l'ensemble de résultats {1,3,7,11,12} et la distribution de probabilité suivante :

$$
\Pr[Z = 2] = 0.2
$$

$$
\Pr[Z = 3] = 0.2
$$

$$
\Pr[Z = 9] = 0.2
$$

$$
\Pr[Z = 11] = 0.2
$$

$$
\Pr[Z = 12] = 0.2
$$

Vous pouvez le voir dans la *Figure 3*. La variable aléatoire Z est, contrairement à Y, une variable uniforme, car toutes les probabilités pour les valeurs possibles lors de l'échantillonnage sont égales.

*Figure 3 : Variable aléatoire Z*

![Figure 3: Random variable Z.](assets/Figure2-3.webp "Figure 3: Random variable Z")

### Probabilité conditionnelle

Supposons que Bob ait l'intention de choisir uniformément un jour de la dernière année civile. Quelle est la probabilité que le jour choisi soit un jour d'été ?

Tant que nous pensons que le processus de Bob sera réellement uniforme, nous devrions conclure qu'il y a une probabilité de 1/4 que Bob choisisse un jour en été. Il s'agit de la **probabilité inconditionnelle** que le jour choisi au hasard soit en été.

Supposons maintenant qu'au lieu de tirer uniformément un jour calendaire, Bob ne choisisse uniformément que parmi les jours où la température à midi à Crystal Lake (New Jersey) était supérieure ou égale à 21 degrés Celsius. Compte tenu de cette information supplémentaire, que pouvons-nous conclure sur la probabilité que Bob choisisse un jour d'été ?

Nous devrions vraiment tirer une conclusion différente, même en l'absence d'autres informations spécifiques (par exemple, la température à midi chaque jour de l'année civile écoulée).

Sachant que Crystal Lake se trouve dans le New Jersey, nous ne nous attendons certainement pas à ce que la température à midi soit de 21 degrés Celsius ou plus en hiver. Il est beaucoup plus probable qu'il s'agisse d'une journée chaude au printemps ou à l'automne, ou d'une journée quelque part en été. Par conséquent, si l'on sait que la température à midi à Crystal Lake le jour choisi était de 21 degrés Celsius ou plus, la probabilité que le jour choisi par Bob soit en été devient beaucoup plus élevée. Il s'agit de la **probabilité conditionnelle** que le jour choisi au hasard soit en été, étant donné que la température à midi à Crystal Lake était de 21 degrés Celsius ou plus.

Contrairement à l'exemple précédent, les probabilités de deux événements peuvent également être totalement indépendantes. Dans ce cas, on dit qu'elles sont **indépendantes**.

Supposons, par exemple, qu'une certaine pièce de monnaie équitable soit tombée sur pile ou face. Compte tenu de ce fait, quelle est la probabilité qu'il pleuve demain ? La probabilité conditionnelle dans ce cas devrait être la même que la probabilité inconditionnelle qu'il pleuve demain, étant donné qu'un jeu de pile ou face n'a généralement pas d'impact sur le temps qu'il fait.

Nous utilisons le symbole "|" pour écrire les énoncés de probabilité conditionnelle. Par exemple, la probabilité de l'événement $A$ étant donné que l'événement $B$ s'est produit peut être écrite comme suit :

$$
Pr[A|B]
$$

Ainsi, lorsque deux événements, $A$ et $B$, sont indépendants, alors :

$$
Pr[A|B] = Pr[A] \text{ and } Pr[B|A] = Pr[B]
$$

La condition d'indépendance peut être simplifiée comme suit :

$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$

Un résultat clé de la théorie des probabilités est connu sous le nom de **théorème de Bayes**. Il stipule que $Pr[A|B]$ peut être réécrit comme suit :

$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$

Au lieu d'utiliser les probabilités conditionnelles pour des événements spécifiques, nous pouvons également examiner les probabilités conditionnelles associées à deux variables aléatoires ou plus sur un ensemble d'événements possibles. Supposons deux variables aléatoires, $X$ et $Y$. Nous pouvons désigner toute valeur possible de $X$ par $x$, et toute valeur possible de $Y$ par $y$. On peut donc dire que deux variables aléatoires sont indépendantes si l'énoncé suivant s'applique :

$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$

pour tout $x$ et $y$.

Soyons un peu plus explicites sur le sens de cette déclaration.

Supposons que les ensembles de résultats pour $X$ et $Y$ soient définis comme suit : **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ et **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (Il est habituel d'indiquer les ensembles de valeurs par des lettres majuscules en gras)

Supposons maintenant que vous échantillonniez $Y$ et que vous observiez $y_1$. L'énoncé ci-dessus nous indique que la probabilité d'obtenir maintenant $x_1$ à partir de l'échantillon $X$ est exactement la même que si nous n'avions jamais observé $y_1$. Cela est vrai pour tout $y_i$ que nous aurions pu tirer de notre échantillonnage initial de $Y$. Enfin, cela n'est pas seulement vrai pour $x_1$. Pour tout $x_i$, la probabilité d'occurrence n'est pas influencée par le résultat d'un échantillonnage de $Y$. Tout ceci s'applique également au cas où $X$ est échantillonné en premier.

Terminons notre discussion sur un point un peu plus philosophique. Dans toute situation réelle, la probabilité d'un événement est toujours évaluée en fonction d'un ensemble particulier d'informations. Il n'existe pas de "probabilité inconditionnelle" au sens strict du terme.

Par exemple, supposons que je vous demande la probabilité que les cochons volent d'ici 2030. Bien que je ne vous donne aucune autre information, vous connaissez manifestement beaucoup de choses sur le monde qui peuvent influencer votre jugement. Vous n'avez jamais vu de cochons voler. Vous savez que la plupart des gens ne s'attendent pas à ce qu'ils volent. Vous savez qu'ils ne sont pas vraiment conçus pour voler. Et ainsi de suite.

Par conséquent, lorsque nous parlons d'une "probabilité inconditionnelle" d'un événement dans un contexte réel, ce terme n'a de sens que si nous le considérons comme "la probabilité sans aucune autre information explicite". Toute compréhension d'une "probabilité conditionnelle" doit donc toujours être comprise par rapport à un élément d'information spécifique.

Je pourrais, par exemple, vous demander la probabilité que les cochons volent d'ici 2030, après vous avoir donné des preuves que certaines chèvres en Nouvelle-Zélande ont appris à voler après quelques années d'entraînement. Dans ce cas, vous ajusterez probablement votre jugement sur la probabilité que les cochons volent d'ici 2030. La probabilité que les cochons volent d'ici 2030 est donc conditionnelle à cette preuve concernant les chèvres en Nouvelle-Zélande.

## L'opération modulo

<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

### Modulo

L'expression la plus élémentaire avec l'opération **modulo** est de la forme suivante : $x \mod y$.

La variable $x$ est appelée le dividende et la variable $y$ le diviseur. Pour effectuer une opération modulo avec un dividende et un diviseur positifs, il suffit de déterminer le reste de la division.

Par exemple, considérons l'expression $25 \mod 4$. Le nombre 4 entre dans le nombre 25 6 fois au total. Le reste de cette division est 1. Par conséquent, $25 \mod 4$ est égal à 1. De la même manière, nous pouvons évaluer les expressions ci-dessous :


- 29$ \mod 30 = 29$ (car 30 entre dans 29 un total de 0 fois et le reste est 29)
- 42$ \mod 2 = 0$ (car 2 entre dans 42 21 fois au total et le reste est 0)
- 12$ \mod 5 = 2$ (car 5 entre dans 12 2 fois au total et le reste est 2)
- 20$ \mod 8 = 4$ (car 8 entre 2 fois dans 20 et le reste est 4)

Lorsque le dividende ou le diviseur est négatif, les opérations modulo peuvent être traitées différemment par les langages de programmation.

Vous rencontrerez certainement des cas avec un dividende négatif en cryptographie. Dans ces cas, l'approche typique est la suivante :


- Déterminez d'abord la valeur la plus proche *inférieure ou égale* au dividende dans laquelle le diviseur se divise avec un reste de zéro. Appelons cette valeur $p$.
- Si le dividende est $x$, le résultat de l'opération modulo est la valeur de $x - p$.

Par exemple, supposons que le dividende soit $-20$ et le diviseur 3. La valeur la plus proche inférieure ou égale à $-20$ dans laquelle 3 se divise également est $-21$. La valeur de $x - p$ dans ce cas est $-20 - (-21)$. Cette valeur est égale à 1 et, par conséquent, $-20 \mod 3$ est égal à 1. De la même manière, nous pouvons évaluer les expressions ci-dessous :


- $-8 \mod 5 = 2$
- $-19 \mod 16 = 13$
- $-14 \mod 6 = 4$

En ce qui concerne la notation, vous verrez généralement les types d'expressions suivants : $x = [y \mod z]$. En raison des parenthèses, l'opération modulo ne s'applique dans ce cas qu'au côté droit de l'expression. Si $y$ est égal à 25 et $z$ à 4, par exemple, $x$ est égal à 1.

Sans parenthèses, l'opération modulo agit sur les *deux côtés* d'une expression. Supposons, par exemple, l'expression suivante : $x = y \mod z$. Si $y$ est égal à 25 et $z$ à 4, tout ce que nous savons est que $x \mod 4$ est égal à 1. Ceci est cohérent avec n'importe quelle valeur pour $x$ de l'ensemble $\{\ldots,-7, -3, 1, 5, 9,\ldots\}$.

La branche des mathématiques qui implique des opérations modulo sur les nombres et les expressions est appelée **arithmétique modulaire**. On peut considérer cette branche comme l'arithmétique pour les cas où la ligne des nombres n'est pas infiniment longue. Bien que les opérations modulo sur les nombres entiers (positifs) soient généralement utilisées en cryptographie, il est également possible d'effectuer des opérations modulo sur n'importe quel nombre réel.

### Le cryptogramme à décalage

L'opération modulo est fréquemment rencontrée en cryptographie. Pour l'illustrer, considérons l'un des systèmes de cryptage historiques les plus célèbres : le cryptogramme à décalage.

Commençons par la définir. Supposons un dictionnaire *D* qui assimile toutes les lettres de l'alphabet anglais, dans l'ordre, à l'ensemble des nombres $\{0, 1, 2, \ldots, 25\}$. Supposons un espace de messages **M**. Le **chiffrement par décalage** est donc un système de chiffrement défini comme suit :


- Sélectionner uniformément une clé $k$ dans l'espace des clés **K**, où **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Chiffrer un message $m \in \mathbf{M}$, comme suit :
    - Séparer $m$ en ses lettres individuelles $m_0, m_1, \ldots, m_i, \ldots, m_l$
    - Convertir chaque $m_i$ en un nombre selon *D*
    - Pour chaque $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Convertir chaque $c_i$ en lettre selon *D*
    - Combinez ensuite $c_0, c_1, \ldots, c_l$ pour obtenir le texte chiffré $c$
- Décrypter un texte chiffré $c$ comme suit :
    - Convertir chaque $c_i$ en un nombre selon *D*
    - Pour chaque $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Convertir chaque $m_i$ en lettre selon *D*
    - Combinez ensuite $m_0, m_1, \ldots, m_l$ pour obtenir le message original $m$

L'opérateur modulo du chiffrement par décalage garantit que les lettres s'enroulent autour d'elles, de sorte que toutes les lettres du texte chiffré sont définies. Pour illustrer ce propos, prenons l'exemple de l'application du chiffrement par décalage au mot "DOG".

Supposons que vous ayez sélectionné uniformément une clé pour qu'elle ait la valeur 17. La lettre "O" équivaut à 15. Sans l'opération modulo, l'addition de ce nombre en clair et de la clé donnerait un nombre chiffré de 32. Cependant, ce nombre de texte chiffré ne peut pas être transformé en lettre de texte chiffré, car l'alphabet anglais ne compte que 26 lettres. L'opération modulo garantit que le nombre du texte chiffré est en fait 6 (le résultat de $32 \mod 26$), ce qui équivaut à la lettre "G" du texte chiffré.

Le cryptage complet du mot "DOG" avec une valeur de clé de 17 est le suivant :


- Message = DOG = D,O,G = 3,15,6
- $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
- $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
- $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
- $c = UGX$

Tout le monde peut comprendre intuitivement le fonctionnement du cryptogramme à décalage et probablement l'utiliser lui-même. Toutefois, pour progresser dans la connaissance de la cryptographie, il est important de commencer à se familiariser avec la formalisation, car les schémas deviennent alors beaucoup plus difficiles. C'est pourquoi les étapes du chiffrement par décalage ont été formalisées.

**Notes:**

[Nous pouvons définir exactement cette affirmation en utilisant la terminologie de la section précédente. Soit une variable uniforme $K$ dont l'ensemble des résultats possibles est $K$. Ainsi :

$$
Pr[K = 0] = \frac{1}{26}
$$

$$
Pr[K = 1] = \frac{1}{26}
$$

... et ainsi de suite. Échantillonner une fois la variable uniforme $K$ pour obtenir une clé particulière.

## L'opération XOR

<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Toutes les données informatiques sont traitées, stockées et envoyées sur les réseaux au niveau des bits. Tous les systèmes cryptographiques appliqués aux données informatiques opèrent également au niveau des bits.

Supposons, par exemple, que vous ayez saisi un courriel dans votre application de messagerie. Le cryptage que vous appliquez ne s'applique pas directement aux caractères ASCII de votre courrier électronique. Il s'applique plutôt à la représentation bitmétrique des lettres et autres symboles de votre e-mail.

Outre l'opération modulo, une opération mathématique essentielle à comprendre pour la cryptographie moderne est l'opération **XOR**, ou opération "or exclusif". Cette opération prend deux bits en entrée et produit un autre bit en sortie. L'opération XOR sera simplement désignée par "XOR". Elle donne 0 si les deux bits sont identiques et 1 si les deux bits sont différents. Vous pouvez voir les quatre possibilités ci-dessous. Le symbole $\oplus$ représente "XOR" :


- $0 \oplus 0 = 0$
- $0 \oplus 1 = 1$
- $1 \oplus 0 = 1$
- $1 \oplus 1 = 0$

Pour illustrer cela, supposons que vous ayez un message $m_1$ (01111001) et un message $m_2$ (01011001). L'opération XOR de ces deux messages est illustrée ci-dessous.


- $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$

Le processus est simple. Vous devez d'abord faire un XOR des bits les plus à gauche de $m_1$ et $m_2$. Dans ce cas, il s'agit de $0 \oplus 0 = 0$. On effectue ensuite un XOR de la deuxième paire de bits en partant de la gauche. Dans ce cas, il s'agit de $1 \oplus 1 = 0$. Vous continuez ce processus jusqu'à ce que vous ayez effectué l'opération XOR sur les bits les plus à droite.

Il est facile de voir que l'opération XOR est commutative, à savoir que $m_1 \oplus m_2 = m_2 \oplus m_1$. En outre, l'opération XOR est également associative. Autrement dit, $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.

Une opération XOR sur deux chaînes de longueur différente peut avoir différentes interprétations, en fonction du contexte. Nous ne nous intéresserons pas ici aux opérations XOR sur des chaînes de longueur différente.

Une opération XOR est équivalente au cas particulier d'une opération modulo sur l'addition de bits lorsque le diviseur est 2. Vous pouvez voir l'équivalence dans les résultats suivants :


- $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
- $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
- $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
- $(1 + 1) \mod 2 = 1 \oplus 1 = 0$

## Pseudo-aléa

<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

Dans notre discussion sur les variables aléatoires et uniformes, nous avons établi une distinction spécifique entre "aléatoire" et "uniforme". Cette distinction est généralement maintenue dans la pratique lors de la description de variables aléatoires. Cependant, dans notre contexte actuel, cette distinction doit être abandonnée et les termes "aléatoire" et "uniforme" sont utilisés comme synonymes. J'expliquerai pourquoi à la fin de cette section.

Pour commencer, nous pouvons appeler une chaîne binaire de longueur $n$ **aléatoire** (ou **uniforme**), si elle est le résultat de l'échantillonnage d'une variable uniforme $S$ qui donne à chaque chaîne binaire d'une telle longueur $n$ une probabilité égale de sélection.

Supposons, par exemple, l'ensemble de toutes les chaînes binaires de longueur 8 : $\{0000\00, 0000\ 0001, \ldots, 1111\ 1111\}$. (Il est courant d'écrire une chaîne de 8 bits en deux quartets, chacun étant appelé **nibble**) Appelons cet ensemble de chaînes **$S_8$**.

Conformément à la définition ci-dessus, nous pouvons donc appeler aléatoire (ou uniforme) une chaîne binaire particulière de longueur 8, si elle est le résultat de l'échantillonnage d'une variable uniforme $S$ qui donne à chaque chaîne de **$S_8$** une probabilité égale de sélection. Étant donné que l'ensemble **$S_8$** comprend $2^8$ éléments, la probabilité de sélection lors de l'échantillonnage devrait être de $1/2^8$ pour chaque chaîne de l'ensemble.

Un aspect essentiel du caractère aléatoire d'une chaîne binaire est qu'il est défini par rapport au processus par lequel elle a été sélectionnée. La forme d'une chaîne binaire particulière ne révèle donc rien sur le caractère aléatoire de sa sélection.

Par exemple, de nombreuses personnes pensent intuitivement qu'une chaîne comme $1111\ 1111$ n'a pas pu être choisie au hasard. Or, cette idée est manifestement fausse.

En définissant une variable uniforme $S$ sur toutes les chaînes binaires de longueur 8, la probabilité de sélectionner $1111\ 1111$ dans l'ensemble **$S_8$** est la même que celle d'une chaîne telle que $0111\ 0100$. On ne peut donc rien dire sur le caractère aléatoire d'une chaîne de caractères en analysant la chaîne elle-même.

On peut également parler de chaînes aléatoires sans parler spécifiquement de chaînes binaires. On peut, par exemple, parler d'une chaîne hexagonale aléatoire $AF\ 02\ 82$. Dans ce cas, la chaîne aurait été choisie au hasard dans l'ensemble des chaînes hexagonales de longueur 6, ce qui équivaut à choisir au hasard une chaîne binaire de longueur 24, puisque chaque chiffre hexadécimal représente 4 bits.

Généralement, l'expression "une chaîne aléatoire", sans qualification, fait référence à une chaîne sélectionnée au hasard dans l'ensemble de toutes les chaînes de même longueur. C'est ainsi que je l'ai décrite ci-dessus. Une chaîne de longueur $n$ peut, bien sûr, être choisie au hasard dans un ensemble différent. Un ensemble, par exemple, qui ne constitue qu'un sous-ensemble de toutes les chaînes de longueur $n$, ou peut-être un ensemble qui comprend des chaînes de longueur variable. Dans ce cas, cependant, nous ne parlerions pas de "chaîne aléatoire", mais plutôt de "chaîne sélectionnée au hasard dans un ensemble **S**".

L'un des concepts clés de la cryptographie est celui de pseudo-aléa. Une **chaîne pseudo-aléatoire** de longueur $n$ apparaît *comme si elle était le résultat de l'échantillonnage d'une variable uniforme $S$ qui donne à chaque chaîne de **$S_n$** une probabilité égale de sélection. En fait, la chaîne est le résultat de l'échantillonnage d'une variable uniforme $S'$ qui définit uniquement une distribution de probabilité - pas nécessairement une distribution avec des probabilités égales pour tous les résultats possibles - sur un sous-ensemble de **$S_n$**. Le point crucial ici est que personne ne peut vraiment faire la distinction entre les échantillons de $S$ et de $S'$, même si l'on en prend un grand nombre.

Supposons, par exemple, une variable aléatoire $S$. Son ensemble de résultats est **$S_{256}$**, c'est-à-dire l'ensemble de toutes les chaînes binaires de longueur 256. Cet ensemble comporte $2^{256}$ éléments. Chaque élément a une probabilité égale de sélection, $1/2^{256}$, lors de l'échantillonnage.

En outre, supposons une variable aléatoire $S'$. Son ensemble de résultats ne comprend que $2^{128}$ chaînes binaires de longueur 256. Elle possède une certaine distribution de probabilité sur ces chaînes, mais cette distribution n'est pas nécessairement uniforme.

Supposons que je prenne des milliers d'échantillons de $S$ et des milliers d'échantillons de $S'$ et que je vous donne les deux ensembles de résultats. Je vous dis quel ensemble de résultats est associé à quelle variable aléatoire. Ensuite, je prélève un échantillon de l'une des deux variables aléatoires. Mais cette fois, je ne vous dis pas quelle variable aléatoire j'échantillonne. Si $S'$ était pseudo-aléatoire, alors l'idée est que votre probabilité de faire la bonne supposition quant à la variable aléatoire que j'ai échantillonnée n'est pratiquement pas meilleure que $1/2$.

Généralement, une chaîne pseudo-aléatoire de longueur $n$ est produite en sélectionnant au hasard une chaîne de taille $n - x$, où $x$ est un entier positif, et en l'utilisant comme entrée d'un algorithme d'expansion. Cette chaîne aléatoire de taille $n - x$ est appelée **semence**.

Les chaînes pseudo-aléatoires sont un concept clé pour rendre la cryptographie pratique. Prenons l'exemple des algorithmes de chiffrement de flux. Avec un chiffrement par flux, une clé sélectionnée au hasard est insérée dans un algorithme d'expansion pour produire une chaîne pseudo-aléatoire beaucoup plus importante. Cette chaîne pseudo-aléatoire est ensuite combinée avec le texte en clair via une opération XOR pour produire un texte chiffré.

Si nous n'étions pas en mesure de produire ce type de chaîne pseudo-aléatoire pour un chiffrement de flux, nous aurions alors besoin d'une clé aussi longue que le message pour assurer sa sécurité. Cette option n'est pas très pratique dans la plupart des cas.

La notion de pseudo-aléa abordée dans cette section peut être définie de manière plus formelle. Elle s'étend également à d'autres contextes. Mais il n'est pas nécessaire d'approfondir cette discussion ici. Tout ce qu'il faut comprendre intuitivement pour une grande partie de la cryptographie, c'est la différence entre une chaîne aléatoire et une chaîne pseudo-aléatoire. [2]

La raison de l'abandon de la distinction entre "aléatoire" et "uniforme" dans notre discussion devrait maintenant être claire. Dans la pratique, tout le monde utilise le terme pseudo-aléatoire pour indiquer une chaîne qui apparaît **comme** le résultat de l'échantillonnage d'une variable uniforme $S$. En toute rigueur, nous devrions appeler une telle chaîne "pseudo-uniforme", en adoptant le langage que nous avons utilisé précédemment. Comme le terme "pseudo-uniforme" est à la fois maladroit et n'est utilisé par personne, nous ne l'introduirons pas ici par souci de clarté. Au lieu de cela, nous abandonnons simplement la distinction entre "aléatoire" et "uniforme" dans le contexte actuel.

**Notes**

[2] Si vous souhaitez un exposé plus formel sur ces questions, vous pouvez consulter l'ouvrage de Katz et Lindell intitulé *Introduction to Modern Cryptography*, en particulier le chapitre 3.

# Fondements mathématiques de la cryptographie 2

<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

## Qu'est-ce que la théorie des nombres ?

<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>

Ce chapitre traite d'un sujet plus avancé sur les fondements mathématiques de la cryptographie : la théorie des nombres. Bien que la théorie des nombres soit importante pour la cryptographie symétrique (comme dans le chiffrement Rijndael), elle est particulièrement importante dans le cadre de la cryptographie à clé publique.

Si les détails de la théorie des nombres vous semblent fastidieux, je vous recommande une lecture de haut niveau la première fois. Vous pourrez toujours y revenir plus tard.

___

On pourrait caractériser la **théorie des nombres** comme l'étude des propriétés des nombres entiers et des fonctions mathématiques qui fonctionnent avec des nombres entiers.

Considérons, par exemple, que deux nombres $a$ et $N$ sont des **coprimes** (ou **premiers relatifs**) si leur plus grand diviseur commun est égal à 1. Supposons maintenant un entier particulier $N$. Combien d'entiers plus petits que $N$ sont coprimes avec $N$ ? Pouvons-nous faire des déclarations générales sur les réponses à cette question ? Tels sont les types de questions auxquelles la théorie des nombres cherche à répondre.

La théorie moderne des nombres s'appuie sur les outils de l'algèbre abstraite. L'algèbre abstraite** est une sous-discipline des mathématiques dans laquelle les principaux objets d'analyse sont des objets abstraits connus sous le nom de structures algébriques. Une **structure algébrique** est un ensemble d'éléments associé à une ou plusieurs opérations, qui répond à certains axiomes. Grâce aux structures algébriques, les mathématiciens peuvent mieux comprendre des problèmes mathématiques spécifiques, en faisant abstraction de leurs détails.

Le domaine de l'algèbre abstraite est parfois appelé algèbre moderne. Vous pouvez également rencontrer le concept de **mathématiques abstraites** (ou **mathématiques pures**). Ce dernier terme ne fait pas référence à l'algèbre abstraite, mais désigne plutôt l'étude des mathématiques pour elles-mêmes, et pas seulement en vue d'applications potentielles.

Les ensembles de l'algèbre abstraite peuvent traiter de nombreux types d'objets, depuis les transformations préservant la forme d'un triangle équilatéral jusqu'aux motifs de papier peint. En ce qui concerne la théorie des nombres, nous ne considérons que les ensembles d'éléments qui contiennent des entiers ou des fonctions qui fonctionnent avec des entiers.

## Groupes

<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Un concept de base en mathématiques est celui d'un ensemble d'éléments. Un ensemble est généralement désigné par des signes d'accolade, les éléments étant séparés par des virgules.

Par exemple, l'ensemble des entiers est ${..., -2, -1, 0, 1, 2, ...\}$. Les ellipses signifient ici qu'un certain modèle se poursuit dans une direction particulière. Ainsi, l'ensemble de tous les entiers comprend également $3, 4, 5, 6$ et ainsi de suite, ainsi que $-3, -4, -5, -6$ et ainsi de suite. Cet ensemble de tous les entiers est généralement désigné par $\mathbb{Z}$.

Un autre exemple d'ensemble est $\mathbb{Z} \Nmod 11$, ou l'ensemble de tous les entiers modulo 11. Contrairement à l'ensemble entier $\mathbb{Z}$, cet ensemble ne contient qu'un nombre fini d'éléments, à savoir $\{0, 1, \ldots, 9, 10\}$.

Une erreur courante consiste à penser que l'ensemble $\mathbb{Z} \mod 11$ est en fait $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. Mais ce n'est pas le cas, étant donné la façon dont nous avons défini l'opération modulo plus tôt. Tous les entiers négatifs réduits par modulo 11 s'enroulent sur $\{0, 1, \ldots, 9, 10\}$. Par exemple, l'expression $-2 \mod 11$ s'enroule autour de $9$, tandis que l'expression $-27 \mod 11$ s'enroule autour de $5$.

Un autre concept de base en mathématiques est celui d'opération binaire. Il s'agit de toute opération qui prend deux éléments pour en produire un troisième. Par exemple, l'arithmétique et l'algèbre de base vous familiarisent avec quatre opérations binaires fondamentales : l'addition, la soustraction, la multiplication et la division.

Ces deux concepts mathématiques de base, les ensembles et les opérations binaires, sont utilisés pour définir la notion de groupe, la structure la plus essentielle de l'algèbre abstraite.

Plus précisément, supposons une opération binaire $\circ$. De plus, supposons un ensemble d'éléments **S** équipé de cette opération. Tout ce que "équipé" signifie ici, c'est que l'opération $\circ$ peut être effectuée entre deux éléments quelconques de l'ensemble **S**.

La combinaison $\langle \mathbf{S}, \circ \rangle$ est donc un **groupe** si elle remplit quatre conditions spécifiques, connues sous le nom d'axiomes de groupe.

1. Pour tout $a$ et $b$ qui sont des éléments de $\mathbf{S}$, $a \circ b$ est aussi un élément de $\mathbf{S}$. C'est ce qu'on appelle la **condition de fermeture**.

2. Pour tout $a$, $b$ et $c$ qui sont des éléments de $\mathbf{S}$, il se peut que $(a \circ b) \circ c = a \circ (b \circ c)$. C'est ce qu'on appelle la **condition d'associativité**.

3. Il existe un élément unique $e$ dans $\mathbf{S}$, tel que pour tout élément $a$ dans $\mathbf{S}$, l'équation suivante s'applique : $e \circ a = a \circ e = a$. Comme il n'existe qu'un seul élément de ce type, $e$, on l'appelle **élément d'identité**. Cette condition est connue sous le nom de **condition d'identité**.

4. Pour chaque élément $a$ dans $\mathbf{S}$, il existe un élément $b$ dans $\mathbf{S}$, tel que l'équation suivante s'applique : $a \circ b = b \circ a = e$, où $e$ est l'élément identité. L'élément $b$ est ici appelé **élément inverse**, et il est communément désigné par $a^{-1}$. Cette condition est connue sous le nom de **condition inverse** ou **condition d'inversion**.

Explorons un peu plus les groupes. Dénotons l'ensemble des entiers par $\mathbb{Z}$. Cet ensemble, combiné à l'addition standard, ou $\langle \mathbb{Z}, + \rangle$, correspond clairement à la définition d'un groupe, car il satisfait aux quatre axiomes ci-dessus.

1. Pour tout $x$ et $y$ qui sont des éléments de $\mathbb{Z}$, $x + y$ est aussi un élément de $\mathbb{Z}$. Donc $\langle \mathbb{Z}, + \rangle$ satisfait la condition de fermeture.

2. Pour tout $x$, $y$ et $z$ qui sont des éléments de $\mathbb{Z}$, $(x + y) + z = x + (y + z)$. Donc $\langle \mathbb{Z}, + \rangle$ satisfait la condition d'associativité.

3. Il existe un élément d'identité dans $\langle \mathbb{Z}, + \rangle$, à savoir 0. Pour tout $x$ dans $\mathbb{Z}$, il s'avère que : $0 + x = x + 0 = x$. Donc $\langle \mathbb{Z}, + \rangle$ satisfait la condition d'identité.

4. Enfin, pour chaque élément $x$ dans $\mathbb{Z}$, il existe un $y$ tel que $x + y = y + x = 0$. Si $x$ est 10, par exemple, $y$ sera $-10$ (dans le cas où $x$ est 0, $y$ est aussi 0). Donc $\langle \mathbb{Z}, + \rangle$ satisfait la condition inverse.

Il est important de noter que le fait que l'ensemble des entiers avec addition constitue un groupe ne signifie pas qu'il constitue un groupe avec multiplication. Vous pouvez le vérifier en testant $\langle \mathbb{Z}, \cdot \rangle$ par rapport aux quatre axiomes de groupe (où $\cdot$ signifie multiplication standard).

Les deux premiers axiomes sont évidemment valables. De plus, sous la multiplication, l'élément 1 peut servir d'élément d'identité. Tout entier $x$ multiplié par 1 donne donc $x$. Cependant, $\langle \mathbb{Z}, \cdot \rangle$ ne remplit pas la condition inverse. En d'autres termes, il n'existe pas d'élément unique $y$ dans $\mathbb{Z}$ pour tout $x$ dans $\mathbb{Z}$, de sorte que $x \cdot y = 1$.

Par exemple, supposons que $x = 22$. Quelle valeur $y$ de l'ensemble $\mathbb{Z}$ multipliée par $x$ donnerait l'élément identité 1 ? La valeur $1/22$ fonctionnerait, mais elle ne fait pas partie de l'ensemble $\mathbb{Z}$. En fait, ce problème se pose pour tout entier $x$, autre que les valeurs 1 et -1 (où $y$ devrait être 1 et -1 respectivement).

Si nous autorisons les nombres réels pour notre ensemble, nos problèmes disparaissent en grande partie. Pour tout élément $x$ de l'ensemble, la multiplication par $1/x$ donne 1. Comme les fractions sont incluses dans l'ensemble des nombres réels, un inverse peut être trouvé pour chaque nombre réel. L'exception est le zéro, car toute multiplication avec zéro ne donnera jamais l'élément d'identité 1. Par conséquent, l'ensemble des nombres réels non nuls dotés d'une multiplication est bien un groupe.

Certains groupes remplissent une cinquième condition générale, connue sous le nom de **condition de commutativité**. Cette condition est la suivante :


- Supposons un groupe $G$ avec un ensemble **S** et un opérateur binaire $\circ$. Supposons que $a$ et $b$ sont des éléments de **S**. Si $a \circ b = b \circ a$ pour deux éléments $a$ et $b$ dans **S**, alors $G$ satisfait la condition de commutativité.

Tout groupe qui satisfait à la condition de commutativité est appelé **groupe commutatif** ou **groupe abélien** (d'après Niels Henrik Abel). Il est facile de vérifier que l'ensemble des nombres réels sur l'addition et l'ensemble des entiers sur l'addition sont des groupes abéliens. L'ensemble des entiers sur la multiplication n'est pas du tout un groupe et ne peut donc pas être un groupe abélien. L'ensemble des nombres réels non nuls sur la multiplication, en revanche, est également un groupe abélien.

Vous devez respecter deux conventions importantes en matière de notation. Premièrement, les signes "+" ou "×" seront souvent utilisés pour symboliser les opérations de groupe, même lorsque les éléments ne sont pas, en fait, des nombres. Dans ces cas, vous ne devez pas interpréter ces signes comme des additions ou des multiplications arithmétiques standard. Il s'agit plutôt d'opérations qui n'ont qu'une ressemblance abstraite avec ces opérations arithmétiques.

À moins que vous ne fassiez spécifiquement référence à l'addition ou à la multiplication arithmétique, il est plus facile d'utiliser des symboles tels que $\circ$ et $\diamond$ pour les opérations de groupe, car ils n'ont pas de connotations très ancrées dans la culture.

Deuxièmement, pour la même raison que "+" et "×" sont souvent utilisés pour indiquer des opérations non arithmétiques, les éléments identitaires des groupes sont fréquemment symbolisés par "0" et "1", même lorsque les éléments de ces groupes ne sont pas des nombres. À moins que vous ne fassiez référence à l'élément d'identité d'un groupe avec des nombres, il est plus facile d'utiliser un symbole plus neutre tel que "$e$" pour indiquer l'élément d'identité.

De nombreux ensembles de valeurs différents et très importants en mathématiques, dotés de certaines opérations binaires, sont des groupes. Les applications cryptographiques, cependant, ne fonctionnent qu'avec des ensembles d'entiers ou au moins des éléments décrits par des entiers, c'est-à-dire dans le domaine de la théorie des nombres. Par conséquent, les ensembles avec des nombres réels autres que les entiers ne sont pas utilisés dans les applications cryptographiques.

Terminons en donnant un exemple d'éléments qui peuvent être "décrits par des entiers", même s'ils ne sont pas des entiers. Un bon exemple est celui des points des courbes elliptiques. Bien que tout point d'une courbe elliptique ne soit clairement pas un entier, un tel point est en effet décrit par deux entiers.

Les courbes elliptiques sont, par exemple, cruciales pour Bitcoin. Toute paire de clés privée et publique standard de Bitcoin est sélectionnée à partir de l'ensemble des points définis par la courbe elliptique suivante :

$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$

(le plus grand nombre premier inférieur à $2^{256}$). La coordonnée $x$ est la clé privée et la coordonnée $y$ est votre clé publique.

Les transactions en bitcoin impliquent généralement de verrouiller les sorties sur une ou plusieurs clés publiques d'une manière ou d'une autre. La valeur de ces transactions peut ensuite être déverrouillée en créant des signatures numériques avec les clés privées correspondantes.

## Groupes cycliques

<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Une distinction majeure que nous pouvons faire est entre un groupe **fini** et un groupe **infini**. Le premier a un nombre fini d'éléments, tandis que le second a un nombre infini d'éléments. Le nombre d'éléments d'un groupe fini est appelé **ordre du groupe**. Toute la cryptographie pratique qui implique l'utilisation de groupes repose sur des groupes finis (en théorie des nombres).

Dans le cadre de la cryptographie à clé publique, une certaine classe de groupes abéliens finis connus sous le nom de groupes cycliques est particulièrement importante. Pour comprendre les groupes cycliques, il faut d'abord comprendre le concept d'exponentiation des éléments de groupe.

Supposons un groupe $G$ avec une opération de groupe $\circ$, et que $a$ est un élément de $G$. L'expression $a^n$ doit alors être interprétée comme l'élément $a$ combiné avec lui-même un total de $n - 1$ fois. Par exemple, $a^2$ signifie $a \circ a$, $a^3$ signifie $a \circ a \circ a$, et ainsi de suite. (Notez que l'exponentiation ici n'est pas nécessairement l'exponentiation au sens arithmétique standard)

Prenons un exemple. Supposons que $G = \langle \mathbb{Z} \mod 7, + \rangle$, et que notre valeur pour $a$ est égale à 4. Dans ce cas, $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Alternativement, $a^4$ représenterait $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.

Certains groupes abéliens possèdent un ou plusieurs éléments qui peuvent produire tous les autres éléments du groupe par exponentiation continue. Ces éléments sont appelés **générateurs** ou **éléments primitifs**.

Une classe importante de ces groupes est $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, où $N$ est un nombre premier. La notation $\mathbb{Z}^*$ signifie ici que le groupe contient tous les entiers positifs non nuls inférieurs à $N$. Un tel groupe a donc toujours $N - 1$ éléments.

Considérons, par exemple, $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Ce groupe possède les éléments suivants : $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. L'ordre de ce groupe est 10 (qui est bien égal à $11 - 1$).

Explorons l'exponentialisation de l'élément 2 de ce groupe. Les calculs effectués jusqu'à $2^{12}$ sont présentés ci-dessous. Notez que du côté gauche de l'équation, l'exposant se réfère à l'exponentiation de l'élément de groupe. Dans notre exemple particulier, il s'agit bien d'une exponentiation arithmétique du côté droit de l'équation (mais il aurait pu s'agir aussi, par exemple, d'une addition). Pour plus de clarté, j'ai écrit l'opération répétée, plutôt que la forme de l'exposant du côté droit.


- $2^1 = 2 \mod 11$
- $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
- $2^3 = 2 \cdot 2 \cdot 2 \cmod 11 = 8 \cmod 11$
- $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \cdot 11$
- $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cmod 11 = 32 \cmod 11 = 10 \cmod 11$
- $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cmod 11 = 64 \cmod 11 = 9 \cmod 11$
- $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cmod 11 = 128 \cdot 11 = 7 \cdot 11$
- $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cmod 11 = 256 \cdot 11 = 3 \cdot 11$
- $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cmod 11 = 512 \cdot 11 = 6 \cdot 11$
- $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cmod 11 = 1024 \cdot 11 = 1 \cdot 11$
- $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cmod 11 = 2048 \cdot 11 = 2 \cdot 11$
- $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cmod 11 = 4096 \cdot 11 = 4 \cdot 11$

Si vous regardez attentivement, vous pouvez voir que l'exponentiation de l'élément 2 parcourt tous les éléments de $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ dans l'ordre suivant : 2, 4, 8, 5, 10, 9, 7, 3, 6, 1 : 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Après $2^{10}$, l'exponentiation continue de l'élément 2 parcourt à nouveau tous les éléments dans le même ordre. Par conséquent, l'élément 2 est un générateur dans $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.

Bien que $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ ait plusieurs générateurs, tous les éléments de ce groupe ne sont pas des générateurs. Considérons, par exemple, l'élément 3. En parcourant les 10 premières exponentiations, sans montrer les calculs fastidieux, on obtient les résultats suivants :


- $3^1 = 3 \mod 11$
- $3^2 = 9 \mod 11$
- $3^3 = 5 \mod 11$
- $3^4 = 4 \mod 11$
- $3^5 = 1 \mod 11$
- $3^6 = 3 \mod 11$
- $3^7 = 9 \mod 11$
- $3^8 = 5 \mod 11$
- $3^9 = 4 \mod 11$
- $3^{10} = 1 \mod 11$

Au lieu de parcourir toutes les valeurs de $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, l'exponentiation de l'élément 3 ne conduit qu'à un sous-ensemble de ces valeurs : 3, 9, 5, 4 et 1. Après la cinquième exponentiation, ces valeurs commencent à se répéter.

Nous pouvons maintenant définir un **groupe cyclique** comme tout groupe ayant au moins un générateur. C'est-à-dire qu'il existe au moins un élément de groupe à partir duquel vous pouvez produire tous les autres éléments de groupe par exponentiation.

Vous avez peut-être remarqué dans notre exemple ci-dessus que $2^{10}$ et $3^{10}$ sont tous deux égaux à $1 \mod 11$. En fait, bien que nous ne fassions pas les calculs, l'exponentiation par 10 de tout élément du groupe $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ donnera $1 \mod 11$. Pourquoi en est-il ainsi ?

C'est une question importante, mais il faut du travail pour y répondre.

Pour commencer, supposons deux entiers positifs $a$ et $N$. Un théorème important de la théorie des nombres stipule que $a$ a un inverse multiplicatif modulo $N$ (c'est-à-dire un entier $b$ tel que $a \cdot b = 1 \mod N$) si et seulement si le plus grand diviseur commun entre $a$ et $N$ est égal à 1. Autrement dit, si $a$ et $N$ sont des coprimes.

Ainsi, pour tout groupe d'entiers doté de la multiplication modulo $N$, seuls les plus petits coprimes avec $N$ sont inclus dans l'ensemble. Nous pouvons désigner cet ensemble par $\mathbb{Z}^c \mod N$.

Par exemple, supposons que $N$ est 10. Seuls les entiers 1, 3, 7 et 9 sont des coprimes de 10. L'ensemble $\mathbb{Z}^c \mod 10$ ne comprend donc que $\{1, 3, 7, 9\}$. Il n'est pas possible de créer un groupe avec multiplication entière modulo 10 en utilisant d'autres entiers compris entre 1 et 10. Pour ce groupe particulier, les inverses sont les paires 1 et 9, et 3 et 7.

Dans le cas où $N$ est lui-même premier, tous les entiers de 1 à $N - 1$ sont coprimes de $N$. Un tel groupe a donc un ordre de $N - 1$. En utilisant notre notation précédente, $\mathbb{Z}^c \mod N$ est égal à $\mathbb{Z}^* \mod N$ lorsque $N$ est premier. Le groupe que nous avons choisi pour notre exemple précédent, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, est un exemple particulier de cette classe de groupes.

Ensuite, la fonction $\phi(N)$ calcule le nombre de coprimes jusqu'à un nombre $N$, et est connue sous le nom de **fonction Phi d'Euler**. [1] D'après le **théorème d'Euler**, lorsque deux entiers $a$ et $N$ sont des coprimes, la chose suivante est vraie :


- $a^{\phi(N)} \mod N = 1 \mod N$

Ceci a une implication importante pour la classe des groupes $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ où $N$ est premier. Pour ces groupes, l'exponentiation des éléments de groupe représente l'exponentiation arithmétique. Autrement dit, $a^{\phi(N)} \mod N$ représente l'opération arithmétique $a^{\phi(N)} \mod N$. Comme tout élément $a$ dans ces groupes multiplicatifs est coprime avec $N$, cela signifie que $a^{\phi(N)} \mod N = a^{N - 1} \mod N = 1 \mod N$.

Le théorème d'Euler est un résultat très important. Pour commencer, il implique que tous les éléments de $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ ne peuvent parcourir qu'un nombre de valeurs par exponentiation qui se divise en $N - 1$. Dans le cas de $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, cela signifie que chaque élément ne peut passer que par 2, 5 ou 10 éléments. Le groupe de valeurs que tout élément parcourt lors de l'exponentiation est appelé **ordre de l'élément**. Un élément dont l'ordre est équivalent à l'ordre d'un groupe est un générateur.

De plus, le théorème d'Euler implique que l'on peut toujours connaître le résultat de $a^{N - 1} \mod N$ pour tout groupe $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ où $N$ est premier. Il en est ainsi quelle que soit la complexité des calculs.

Par exemple, supposons que notre groupe soit $\mathbb{Z}^* \mod 160,481,182$ (où 160,481,182 est effectivement un nombre premier). Nous savons que tous les entiers de 1 à 160 481 181 doivent être des éléments de ce groupe, et que $\phi(n) = 160 481 181$. Bien que nous ne puissions pas effectuer toutes les étapes des calculs, nous savons que des expressions telles que $514^{160,481,181}$, $2,005^{160,481,181}$, et $256,212^{160,481,181}$ doivent toutes être évaluées à $1 \mod 160,481,182$.

**Notes:**

[1] La fonction fonctionne comme suit. Tout entier $N$ peut être factorisé en un produit de nombres premiers. Supposons qu'un $N$ particulier soit factorisé comme suit : $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$ où tous les $p$ sont des nombres premiers et tous les $e$ sont des entiers supérieurs ou égaux à 1. Alors.. :

$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$

Formule de la fonction Phi d'Euler pour la factorisation des nombres premiers de $N$.

## Champs

<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Un groupe est la structure algébrique de base de l'algèbre abstraite, mais il en existe beaucoup d'autres. La seule autre structure algébrique que vous devez connaître est celle d'un **champ**, plus précisément celle d'un **champ fini**. Ce type de structure algébrique est fréquemment utilisé en cryptographie, notamment dans l'Advanced Encryption Standard. Ce dernier est le principal système de cryptage symétrique que vous rencontrerez dans la pratique.

Un champ est dérivé de la notion de groupe. Plus précisément, un **champ** est un ensemble d'éléments **S** équipé de deux opérateurs binaires $\circ$ et $\diamond$, qui remplit les conditions suivantes :

1. L'ensemble **S** muni de $\circ$ est un groupe abélien.

2. L'ensemble **S** équipé de $\diamond$ est un groupe abélien pour les éléments "non nuls".

3. L'ensemble **S** muni des deux opérateurs satisfait à ce que l'on appelle la condition de distribution : Supposons que $a$, $b$ et $c$ sont des éléments de **S**. Alors **S** muni des deux opérateurs satisfait à la propriété distributive lorsque $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.

Notez que, comme pour les groupes, la définition d'un champ est très abstraite. Elle ne prétend rien sur les types d'éléments de **S**, ni sur les opérations $\circ$ et $\diamond$. Elle indique simplement qu'un champ est tout ensemble d'éléments avec deux opérations pour lesquelles les trois conditions ci-dessus sont remplies. (L'élément "zéro" du deuxième groupe abélien peut être interprété abstraitement)

Quel est donc l'exemple d'un champ ? Un bon exemple est l'ensemble $\mathbb{Z} \mod 7$, ou $\{0, 1, \ldots, 7\}$ défini sur l'addition standard (à la place de $\circ$ ci-dessus) et la multiplication standard (à la place de $\diamond$ ci-dessus).

Premièrement, $\mathbb{Z} \mod 7$ remplit la condition pour être un groupe abélien sur l'addition, et il remplit la condition pour être un groupe abélien sur la multiplication si l'on ne considère que les éléments non nuls. Deuxièmement, la combinaison de l'ensemble avec les deux opérateurs remplit la condition de distribution.

Il est didactiquement intéressant d'explorer ces affirmations en utilisant quelques valeurs particulières. Prenons les valeurs expérimentales 5, 2 et 3, des éléments choisis au hasard dans l'ensemble $\mathbb{Z} \mod 7$, pour inspecter le champ $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Nous utiliserons ces trois valeurs dans l'ordre, selon les besoins pour explorer des conditions particulières.

Voyons d'abord si $\mathbb{Z} \mod 7$ muni de l'addition est un groupe abélien.

1. **Condition de fermeture** : Prenons 5 et 2 comme valeurs. Dans ce cas, $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Il s'agit bien d'un élément de $\mathbb{Z} \mod 7$, donc le résultat est cohérent avec la condition de fermeture.

2. **Condition d'associativité** : Prenons 5, 2 et 3 comme valeurs. Dans ce cas, $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Ceci est cohérent avec la condition d'associativité.

3. **Condition d'identité** : Prenons 5 comme valeur. Dans ce cas, $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Ainsi, 0 semble être l'élément d'identité pour l'addition.

4. **Condition inverse** : Considérons l'inverse de 5. Il faut que $[5 + d] \mod 7 = 0$, pour une certaine valeur de $d$. Dans ce cas, l'unique valeur de $\mathbb{Z} \mod 7$ qui remplit cette condition est 2.

5. **Condition de commutativité** : Prenons 5 et 3 comme valeurs. Dans ce cas, $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Ceci est conforme à la condition de commutativité.

L'ensemble $\mathbb{Z} \mod 7$ équipé de l'addition apparaît clairement comme un groupe abélien. Voyons maintenant si $\mathbb{Z} \mod 7$ muni de la multiplication est un groupe abélien pour tous les éléments non nuls.

1. **Condition de fermeture** : Prenons 5 et 2 comme valeurs. Dans ce cas, $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. C'est aussi un élément de $\mathbb{Z} \mod 7$, donc le résultat est cohérent avec la condition de fermeture.

2. **Condition d'associativité** : Prenons 5, 2 et 3 comme valeurs. Dans ce cas, $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \cdot 7 = 2$. Ceci est conforme à la condition d'associativité.

3. **Condition d'identité** : Prenons 5 comme valeur. Dans ce cas, $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Ainsi, 1 semble être l'élément d'identité pour la multiplication.

4. **Condition inverse** : Considérons l'inverse de 5. Il faut que $[5 \cdot d] \mod 7 = 1$, pour une certaine valeur de $d$. L'unique valeur de $\mathbb{Z} \mod 7$ qui remplit cette condition est 3, ce qui est cohérent avec la condition d'inversion.

5. **Condition de commutativité** : Prenons 5 et 3 comme valeurs. Dans ce cas, $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. Ceci est cohérent avec la condition de commutativité.

L'ensemble $\mathbb{Z} \mod 7$ semble clairement répondre aux règles pour être un groupe abélien lorsqu'il est associé à l'addition ou à la multiplication sur les éléments non nuls.

Enfin, cet ensemble combiné avec les deux opérateurs semble satisfaire à la condition de distribution. Prenons 5, 2 et 3 comme valeurs. Nous voyons que $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.

Nous avons vu que $\mathbb{Z} \mod 7$ équipée de l'addition et de la multiplication satisfait aux axiomes d'un corps fini lorsqu'elle est testée avec des valeurs particulières. Bien sûr, nous pouvons aussi le montrer de manière générale, mais nous ne le ferons pas ici.

Une distinction essentielle est faite entre deux types de champs : les champs finis et les champs infinis.

Un **champ infini** est un champ dont l'ensemble **S** est infiniment grand. L'ensemble des nombres réels $\mathbb{R}$ muni de l'addition et de la multiplication est un exemple de champ infini. Un **champ fini**, également appelé **champ de Galois**, est un champ dont l'ensemble **S** est fini. Notre exemple ci-dessus de $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ est un corps fini.

En cryptographie, nous nous intéressons principalement aux corps finis. En général, on peut montrer qu'un corps fini existe pour un ensemble d'éléments **S** si et seulement s'il a $p^m$ éléments, où $p$ est un nombre premier et $m$ un entier positif supérieur ou égal à un. En d'autres termes, si l'ordre d'un ensemble **S** est un nombre premier ($p^m$ où $m = 1$) ou une puissance première ($p^m$ où $m > 1$), alors on peut trouver deux opérateurs $\circ$ et $\diamond$ tels que les conditions d'existence d'un corps soient satisfaites.

Si un corps fini possède un nombre premier d'éléments, on l'appelle **corps premier**. Si le nombre d'éléments du corps fini est une puissance première, le corps est appelé **champ d'extension**. En cryptographie, nous nous intéressons à la fois aux champs de nombres premiers et aux champs d'extension. [2]

Les principaux champs de nombres premiers qui présentent un intérêt pour la cryptographie sont ceux où l'ensemble des entiers est modulé par un nombre premier et où les opérateurs sont l'addition et la multiplication standard. Cette classe de champs finis comprend $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$, et ainsi de suite. Pour tout corps premier $\mathbb{Z} \mod p$, l'ensemble des entiers du corps est le suivant : $\{0, 1, \ldots, p - 2, p - 1\}$.

En cryptographie, nous nous intéressons également aux champs d'extension, en particulier aux champs à $2^m$ éléments où $m > 1$. De tels champs finis sont, par exemple, utilisés dans le chiffrement de Rijndael, qui constitue la base de l'Advanced Encryption Standard. Alors que les champs premiers sont relativement intuitifs, ces champs d'extension en base 2 ne sont probablement pas destinés à ceux qui ne sont pas familiers avec l'algèbre abstraite.

Pour commencer, il est vrai que tout ensemble d'entiers avec $2^m$ éléments peut se voir attribuer deux opérateurs qui feraient de leur combinaison un champ (tant que $m$ est un entier positif). Cependant, ce n'est pas parce qu'un champ existe qu'il est nécessairement facile à découvrir ou particulièrement pratique pour certaines applications.

Il s'avère que les champs d'extension de $2^m$ particulièrement applicables en cryptographie sont ceux définis sur des ensembles particuliers d'expressions polynomiales, plutôt que sur un ensemble d'entiers.

Par exemple, supposons que nous voulions un champ d'extension avec $2^3$ (c'est-à-dire 8) éléments dans l'ensemble. Bien qu'il puisse exister de nombreux ensembles différents pouvant être utilisés pour des champs de cette taille, l'un de ces ensembles comprend tous les polynômes uniques de la forme $a_2x^2 + a_1x + a_0$, où chaque coefficient $a_i$ est soit 0, soit 1. Par conséquent, cet ensemble **S** comprend les éléments suivants :

1. $0$ : Le cas où $a_2 = 0$, $a_1 = 0$, et $a_0 = 0$.

2. $1$ : Le cas où $a_2 = 0$, $a_1 = 0$, et $a_0 = 1$.

3. $x$ : Le cas où $a_2 = 0$, $a_1 = 1$, et $a_0 = 0$.

4. $x + 1$ : Le cas où $a_2 = 0$, $a_1 = 1$, et $a_0 = 1$.

5. $x^2$ : Le cas où $a_2 = 1$, $a_1 = 0$, et $a_0 = 0$.

6. $x^2 + 1$ : Le cas où $a_2 = 1$, $a_1 = 0$, et $a_0 = 1$.

7. $x^2 + x$ : Le cas où $a_2 = 1$, $a_1 = 1$, et $a_0 = 0$.

8. $x^2 + x + 1$ : Le cas où $a_2 = 1$, $a_1 = 1$, et $a_0 = 1$.

Donc **S** serait l'ensemble $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Quelles sont les deux opérations que l'on peut définir sur cet ensemble d'éléments pour s'assurer que leur combinaison est un champ ?

La première opération sur l'ensemble **S** ($\circ$) peut être définie comme une addition polynomiale standard modulo 2. Tout ce que vous avez à faire est d'additionner les polynômes comme vous le feriez normalement, puis d'appliquer le modulo 2 à chacun des coefficients du polynôme résultant. Voici quelques exemples :


- $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
- $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
- $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$

La deuxième opération sur l'ensemble **S** ($\diamond$) qui est nécessaire pour créer le champ est plus compliquée. Il s'agit d'une sorte de multiplication, mais pas de la multiplication standard de l'arithmétique. Au lieu de cela, vous devez considérer chaque élément comme un vecteur et comprendre l'opération comme la multiplication de ces deux vecteurs modulo un polynôme irréductible.

Commençons par l'idée d'un polynôme irréductible. Un **polynôme irréductible** est un polynôme qui ne peut pas être factorisé (tout comme un nombre premier ne peut pas être factorisé en composantes autres que 1 et le nombre premier lui-même). Pour nos besoins, nous nous intéressons aux polynômes irréductibles par rapport à l'ensemble des entiers. (Notez que vous pouvez être en mesure de factoriser certains polynômes par, par exemple, les nombres réels ou complexes, même si vous ne pouvez pas les factoriser en utilisant les nombres entiers)

Par exemple, considérons le polynôme $x^2 - 3x + 2$. Il peut être réécrit sous la forme $(x - 1)(x - 2)$. Il n'est donc pas irréductible. Considérons maintenant le polynôme $x^2 + 1$. En utilisant uniquement des entiers, il n'y a aucun moyen de factoriser cette expression. Il s'agit donc d'un polynôme irréductible par rapport aux entiers.

Passons maintenant au concept de multiplication vectorielle. Nous n'allons pas approfondir ce sujet, mais il suffit de comprendre une règle de base : Toute division vectorielle peut avoir lieu tant que le dividende a un degré supérieur ou égal à celui du diviseur. Si le dividende a un degré inférieur à celui du diviseur, alors le dividende ne peut plus être divisé par le diviseur.

Par exemple, considérons l'expression $x^6 + x + 1 \mod x^5 + x^2$. Cette expression se réduit encore puisque le degré du dividende, 6, est plus élevé que celui du diviseur, 5. Considérons maintenant l'expression $x^5 + x + 1 \mod x^5 + x^2$. Cette expression se réduit également, car les degrés du dividende, 5, et du diviseur, 5, sont égaux.

Cependant, considérons maintenant l'expression $x^4 + x + 1 \mod x^5 + x^2$. Cette expression ne se réduit pas davantage, car le degré du dividende, 4, est inférieur au degré du diviseur, 5.

Sur la base de ces informations, nous sommes maintenant prêts à trouver notre deuxième opération pour l'ensemble $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

J'ai déjà dit que la deuxième opération devait être comprise comme une multiplication vectorielle modulo un polynôme irréductible. Ce polynôme irréductible doit garantir que la deuxième opération définit un groupe abélien sur **S** et qu'elle est compatible avec la condition de distribution. Quel doit être ce polynôme irréductible ?

Comme tous les vecteurs de l'ensemble sont de degré 2 ou inférieur, le polynôme irréductible doit être de degré 3. Si toute multiplication de deux vecteurs de l'ensemble donne un polynôme de degré 3 ou supérieur, nous savons que modulo un polynôme de degré 3 donne toujours un polynôme de degré 2 ou inférieur, car tout polynôme de degré 3 ou supérieur est toujours divisible par un polynôme de degré 3. En outre, le polynôme qui sert de diviseur doit être irréductible. C'est le cas parce que tout polynôme de degré 3 ou plus est toujours divisible par un polynôme de degré 3. En outre, le polynôme qui sert de diviseur doit être irréductible.

Il s'avère qu'il existe plusieurs polynômes irréductibles de degré 3 que nous pourrions utiliser comme diviseur. Chacun de ces polynômes définit un champ différent en conjonction avec notre ensemble **S** et l'addition modulo 2. Cela signifie que vous avez plusieurs options lorsque vous utilisez les champs d'extension $2^m$ en cryptographie.

Pour notre exemple, supposons que nous choisissions le polynôme $x^3 + x + 1$. Ce polynôme est irréductible, car vous ne pouvez pas le factoriser en utilisant des entiers. De plus, il garantit que toute multiplication de deux éléments produira un polynôme de degré 2 ou moins.

Prenons un exemple de la deuxième opération en utilisant le polynôme $x^3 + x + 1$ comme diviseur pour illustrer son fonctionnement. Supposons que vous multipliez les éléments $x^2 + 1$ avec $x^2 + x$ dans notre ensemble **S**. Nous devons alors calculer l'expression $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Ceci peut être simplifié comme suit :


- $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
- $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
- $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$

Nous savons que $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ peut être réduit car le dividende a un degré plus élevé (4) que le diviseur (3).

Pour commencer, vous pouvez voir que l'expression $x^3 + x + 1$ entre dans $x^4 + x^3 + x^2 + x$ un total de $x$ fois. Vous pouvez le vérifier en multipliant $x^3 + x + 1$ par $x$, ce qui donne $x^4 + x^2 + x$. Comme ce dernier terme est du même degré que le dividende, à savoir 4, nous savons que cela fonctionne. Vous pouvez calculer le reste de cette division par $x$ comme suit :


- $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
- $[x^3] \mod x^3 + x + 1 =$$
- $x^3$

Ainsi, après avoir divisé $x^4 + x^3 + x^2 + x$ par $x^3 + x + 1$ un total de $x$ fois, nous avons un reste de $x^3$. Peut-on le diviser à nouveau par $x^3 + x + 1$ ?

Intuitivement, il peut être intéressant de dire que $x^3$ ne peut plus être divisé par $x^3 + x + 1$, parce que ce dernier terme semble plus grand. Cependant, rappelez-vous notre discussion sur la division vectorielle plus tôt. Tant que le dividende a un degré supérieur ou égal au diviseur, l'expression peut être réduite. Plus précisément, l'expression $x^3 + x + 1$ peut entrer dans $x^3$ exactement une fois. Le reste est calculé comme suit :

$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$

Vous vous demandez peut-être pourquoi $(x^3) - (x^3 + x + 1)$ s'évalue à $x + 1$ et non à $-x - 1$. Rappelez-vous que la première opération de notre champ est définie modulo 2. Par conséquent, la soustraction de deux vecteurs donne exactement le même résultat que l'addition de deux vecteurs.

Pour résumer la multiplication de $x^2 + 1$ et $x^2 + x$ : En multipliant ces deux termes, on obtient un polynôme de degré 4, $x^4 + x^3 + x^2 + x$, qui doit être réduit modulo $x^3 + x + 1$. Le polynôme de degré 4 est divisible par $x^3 + x + 1$ exactement $x + 1$ fois. Le reste après avoir divisé $x^4 + x^3 + x^2 + x$ par $x^3 + x + 1$ exactement $x + 1$ fois est $x + 1$. Il s'agit bien d'un élément de notre ensemble $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Pourquoi les champs d'extension de base 2 sur des ensembles de polynômes, comme dans l'exemple ci-dessus, seraient-ils utiles pour la cryptographie ? La raison en est que vous pouvez considérer les coefficients des polynômes de ces ensembles, soit 0 soit 1, comme des éléments de chaînes binaires d'une longueur particulière. L'ensemble **S** de notre exemple ci-dessus, par exemple, pourrait être considéré comme un ensemble **S** comprenant toutes les chaînes binaires de longueur 3 (de 000 à 111). Les opérations sur **S** peuvent donc également être utilisées pour effectuer des opérations sur ces chaînes binaires et produire une chaîne binaire de même longueur.

**Notes:**

[Les champs d'extension deviennent très contre-intuitifs. Au lieu d'avoir des éléments d'entiers, ils ont des ensembles de polynômes. En outre, toutes les opérations sont effectuées modulo un polynôme irréductible.

## L'algèbre abstraite en pratique

<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>

Malgré le langage formel et le caractère abstrait de la discussion, le concept de groupe ne devrait pas être trop difficile à saisir. Il s'agit simplement d'un ensemble d'éléments associé à une opération binaire, où l'exécution de cette opération binaire sur ces éléments répond à quatre conditions générales. Un groupe abélien est soumis à une condition supplémentaire, la commutativité. Un groupe cyclique, quant à lui, est un type particulier de groupe abélien, à savoir un groupe qui possède un générateur. Un champ est simplement une construction plus complexe à partir de la notion de groupe de base.

Mais si vous avez l'esprit pratique, vous pouvez vous demander à ce stade : Qui s'en soucie ? Savoir qu'un ensemble d'éléments avec un opérateur est un groupe, ou même un groupe abélien ou cyclique, a-t-il une quelconque pertinence dans le monde réel ? Savoir que quelque chose est un champ ?

Sans entrer dans les détails, la réponse est "oui". Les groupes ont été créés au 19e siècle par le mathématicien français Evariste Galois. Il les a utilisés pour tirer des conclusions sur la résolution d'équations polynomiales d'un degré supérieur à cinq.

Depuis lors, le concept de groupe a permis d'éclairer un certain nombre de problèmes en mathématiques et ailleurs. C'est ainsi que le physicien Murray-Gellman a pu prédire l'existence d'une particule avant qu'elle ne soit observée lors d'expériences[3]. [Autre exemple, les chimistes utilisent la théorie des groupes pour classer les formes des molécules. Les mathématiciens ont même utilisé le concept de groupe pour tirer des conclusions sur quelque chose d'aussi concret que le papier peint !

Montrer qu'un ensemble d'éléments avec un certain opérateur est un groupe signifie essentiellement que ce que vous décrivez possède une symétrie particulière. Pas une symétrie au sens commun du terme, mais sous une forme plus abstraite. Cela peut permettre de mieux comprendre des systèmes et des problèmes particuliers. Les notions plus complexes de l'algèbre abstraite ne font que nous donner des informations supplémentaires.

Plus important encore, vous verrez l'importance des groupes et des champs de la théorie des nombres dans la pratique grâce à leur application en cryptographie, en particulier en cryptographie à clé publique. Nous avons déjà vu dans notre discussion sur les champs, par exemple, comment les champs d'extension sont utilisés dans le chiffrement Rijndael. Nous développerons cet exemple au *chapitre 5*.

Pour une discussion plus approfondie sur l'algèbre abstraite, je recommande l'excellente série de vidéos sur l'algèbre abstraite de Socratica[4]. [Je recommande en particulier les vidéos suivantes : "Qu'est-ce que l'algèbre abstraite ?", "Définition des groupes (développée)", "Définition des anneaux (développée)", et "Définition des champs (développée)" Ces quatre vidéos vous donneront un aperçu supplémentaire de la majeure partie de la discussion ci-dessus. (Nous n'avons pas parlé des anneaux, mais un champ est un type particulier d'anneau)

Pour une discussion plus approfondie sur la théorie moderne des nombres, vous pouvez consulter de nombreuses discussions avancées sur la cryptographie. Je vous suggère l'ouvrage de Jonathan Katz et Yehuda Lindell intitulé Introduction to Modern Cryptography ou celui de Christof Paar et Jan Pelzl intitulé Understanding Cryptography. [5]

**Notes:**

[3] Voir [Vidéo YouTube] (https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)

[4] Socratica, [Algèbre abstraite](https://www.socratica.com/subject/abstract-algebra)

[5] Katz et Lindell, *Introduction to Modern Cryptography*, 2e édition, 2015 (CRC Press : Boca Raton, FL). Paar et Pelzl, *Understanding Cryptography*, 2010 (Springer-Verlag : Berlin).

# Cryptographie symétrique

<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

## Alice et Bob

<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

L'une des deux principales branches de la cryptographie est la cryptographie symétrique. Elle comprend les systèmes de cryptage ainsi que les systèmes d'authentification et d'intégrité. Jusqu'aux années 1970, l'ensemble de la cryptographie aurait consisté en des schémas de chiffrement symétrique.

La discussion principale commence par l'examen des systèmes de cryptage symétrique et la distinction cruciale entre les algorithmes de chiffrement par flot et les algorithmes de chiffrement par bloc. Nous abordons ensuite les codes d'authentification des messages, qui sont des systèmes permettant de garantir l'intégrité et l'authenticité des messages. Enfin, nous examinons comment les systèmes de cryptage symétrique et les codes d'authentification des messages peuvent être combinés pour garantir la sécurité des communications.

Ce chapitre aborde en passant divers schémas cryptographiques symétriques issus de la pratique. Le chapitre suivant présente en détail le cryptage avec un chiffrement par flux et un chiffrement par bloc, à savoir RC4 et AES respectivement.

Avant d'entamer notre discussion sur la cryptographie symétrique, je voudrais faire quelques remarques sur les illustrations d'Alice et de Bob dans ce chapitre et les suivants.

___

Pour illustrer les principes de la cryptographie, on utilise souvent des exemples impliquant Alice et Bob. Je le ferai également.

En particulier si vous êtes novice en matière de cryptographie, il est important de comprendre que ces exemples d'Alice et de Bob sont uniquement destinés à illustrer les principes et les constructions cryptographiques dans un environnement simplifié. Ces principes et constructions sont toutefois applicables à un éventail beaucoup plus large de contextes réels.

Voici cinq points essentiels à garder à l'esprit concernant les exemples impliquant Alice et Bob dans la cryptographie :

1. Ils peuvent facilement être traduits en exemples avec d'autres types d'acteurs tels que des entreprises ou des organisations gouvernementales.

2. Ils peuvent facilement être étendus pour inclure trois acteurs ou plus.

3. Dans ces exemples, Bob et Alice participent activement à la création de chaque message et à l'application de schémas cryptographiques sur ce message. Mais en réalité, les communications électroniques sont largement automatisées. Lorsque vous visitez un site web utilisant la sécurité de la couche transport, par exemple, la cryptographie est généralement prise en charge par votre ordinateur et le serveur web.

4. Dans le contexte de la communication électronique, les "messages" envoyés sur un canal de communication sont généralement des paquets TCP/IP. Ces paquets peuvent faire partie d'un courriel, d'un message Facebook, d'une conversation téléphonique, d'un transfert de fichiers, d'un site web, d'un téléchargement de logiciel, etc. Il ne s'agit pas de messages au sens traditionnel du terme. Néanmoins, les cryptographes simplifient souvent cette réalité en déclarant que le message est, par exemple, un courrier électronique.

5. Les exemples se concentrent généralement sur la communication électronique, mais ils peuvent également être étendus aux formes traditionnelles de communication telles que les lettres.

## Schémas de cryptage symétrique

<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Nous pouvons définir librement un **système de cryptage symétrique** comme tout système cryptographique comportant trois algorithmes :

1. Un **algorithme de génération de clés**, qui génère une clé privée.

2. Un **algorithme de chiffrement**, qui prend la clé privée et un texte en clair comme entrées et produit un texte chiffré.

3. Un **algorithme de décryptage**, qui prend la clé privée et le texte chiffré comme entrées et produit le texte en clair original.

Généralement, un schéma de chiffrement - symétrique ou asymétrique - offre un modèle de chiffrement basé sur un algorithme de base, plutôt qu'une spécification exacte.

Prenons l'exemple de Salsa20, un système de cryptage symétrique. Il peut être utilisé avec des clés de 128 et 256 bits. Le choix de la longueur de clé a une incidence sur certains détails mineurs de l'algorithme (le nombre de tours dans l'algorithme pour être exact).

Mais on ne peut pas dire que l'utilisation de Salsa20 avec une clé de 128 bits est un schéma de cryptage différent de celui de Salsa20 avec une clé de 256 bits. L'algorithme de base reste le même. Ce n'est que lorsque l'algorithme de base change que l'on peut réellement parler de deux schémas de cryptage différents.

Les systèmes de cryptage symétrique sont généralement utiles dans deux types de cas : (1) ceux où deux agents ou plus communiquent à distance et veulent garder le contenu de leurs communications secret ; et (2) ceux où un agent veut garder le contenu d'un message secret dans le temps.

La *Figure 1* ci-dessous illustre la situation (1). Bob souhaite envoyer un message $M$ à Alice à distance, mais ne veut pas que d'autres personnes puissent lire ce message.

Bob commence par chiffrer le message $M$ avec la clé privée $K$. Il envoie ensuite le texte chiffré $C$ à Alice. Une fois qu'Alice a reçu le texte chiffré, elle peut le déchiffrer à l'aide de la clé $K$ et lire le texte en clair. Avec un bon système de cryptage, tout attaquant qui intercepte le texte chiffré $C$ ne devrait pas être en mesure d'apprendre quoi que ce soit de vraiment significatif sur le message $M$.

La *Figure 2* ci-dessous illustre la situation (2). Bob souhaite empêcher d'autres personnes de consulter certaines informations. Une situation typique est celle d'un employé qui stocke des données sensibles sur son ordinateur, que ni les personnes extérieures ni ses collègues ne sont censés lire.

Bob chiffre le message $M$ au moment $T_0$ avec la clé $K$ pour produire le texte chiffré $C$. Au moment $T_1$, il a de nouveau besoin du message et déchiffre le texte chiffré $C$ avec la clé $K$. Tout attaquant qui serait tombé sur le texte chiffré $C$ entre-temps ne devrait pas avoir été en mesure d'en déduire quoi que ce soit d'important sur $M$.

*Figure 1 : Le secret dans l'espace*

![Figure 1: Secrecy across space](assets/Figure4-1.webp "Figure 1: Secrecy across space")

*Figure 2 : Le secret à travers le temps*

![Figure 2: Secrecy across time](assets/Figure4-2.webp "Figure 2: Secrecy across time")

## Un exemple : Le chiffrement par décalage

<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

Au chapitre 2, nous avons étudié le chiffrement par décalage, qui est un exemple de système de chiffrement symétrique très simple. Reprenons-le ici.

Supposons un dictionnaire *D* qui assimile toutes les lettres de l'alphabet anglais, dans l'ordre, à l'ensemble des nombres $\{0,1,2,\Npoints,25\N}$. Supposons un ensemble de messages possibles **M**. Le chiffrement par décalage est donc un système de chiffrement défini comme suit :


- Sélectionner aléatoirement une clé $k$ parmi l'ensemble des clés possibles **K**, où **K** = ${0,1,2,\Npoints,25\N}$
- Chiffrer un message $m \in$ **M**, comme suit :
    - Séparer $m$ en ses lettres individuelles $m_0, m_1,\dots, m_i, \dots, m_l$
    - Convertir chaque $m_i$ en un nombre selon *D*
    - Pour chaque $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Convertir chaque $c_i$ en lettre selon *D*
    - Combinez ensuite $c_0, c_1,\dots, c_l$ pour obtenir le texte chiffré $c$
- Décrypter un texte chiffré $c$ comme suit :
    - Convertir chaque $c_i$ en un nombre selon *D*
    - Pour chaque $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Convertir chaque $m_i$ en lettre selon *D*
    - Combinez ensuite $m_0, m_1, \dots, m_l$ pour obtenir le message original $m$

Ce qui fait du chiffrement par décalage un système de chiffrement symétrique, c'est que la même clé est utilisée à la fois pour le processus de chiffrement et de déchiffrement. Supposons, par exemple, que vous souhaitiez crypter le message "DOG" à l'aide du chiffrement par décalage et que vous choisissiez au hasard "24" comme clé. En chiffrant le message avec cette clé, vous obtiendrez "BME". Le seul moyen de retrouver le message original est d'utiliser la même clé, "24", pour le décryptage.

Ce chiffre de Shift est un exemple de **chiffre de substitution monoalphabétique** : un système de chiffrement dans lequel l'alphabet du texte chiffré est fixe (c'est-à-dire qu'un seul alphabet est utilisé). En supposant que l'algorithme de décryptage soit déterministe, chaque symobole du texte chiffré de substitution peut au maximum correspondre à un symbole du texte en clair.

Jusque dans les années 1700, de nombreuses applications de cryptage reposaient largement sur des algorithmes de substitution monoalphabétique, bien que ceux-ci fussent souvent beaucoup plus complexes que l'algorithme de Shift. On pouvait, par exemple, choisir au hasard une lettre de l'alphabet pour chaque lettre du texte original, sous réserve que chaque lettre n'apparaisse qu'une seule fois dans l'alphabet du texte chiffré. Cela signifie que vous auriez 26 clés privées possibles, ce qui était énorme à l'époque où les ordinateurs n'existaient pas encore.

Notez que vous rencontrerez souvent le terme **chiffrer** dans le domaine de la cryptographie. Sachez que ce terme a plusieurs significations. En fait, je connais au moins cinq significations distinctes de ce terme en cryptographie.

Dans certains cas, il fait référence à un schéma de chiffrement, comme c'est le cas pour le Shift cipher et le monoalphabetic substitution cipher. Cependant, le terme peut également se référer spécifiquement à l'algorithme de chiffrement, à la clé privée ou simplement au texte chiffré d'un tel système de chiffrement.

Enfin, le terme "chiffre" peut également désigner un algorithme de base à partir duquel il est possible de construire des schémas cryptographiques. Il peut s'agir de divers algorithmes de chiffrement, mais aussi d'autres types de schémas cryptographiques. Ce sens du terme devient pertinent dans le contexte des chiffrements par blocs (voir la section "Chiffrages par blocs" ci-dessous).

Vous pouvez également rencontrer les termes **chiffrer** ou **déchiffrer**. Ces termes sont simplement des synonymes de cryptage et de décryptage.

## Attaques par force brute et principe de Kerckhoff

<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Le chiffrement par décalage est un système de chiffrement symétrique très peu sûr, du moins dans le monde moderne[1]. [Un attaquant pourrait simplement tenter de décrypter n'importe quel texte chiffré avec les 26 clés possibles pour voir quel résultat a du sens. Ce type d'attaque, où l'attaquant se contente de parcourir les clés pour voir ce qui fonctionne, est connu sous le nom d'attaque **brute force** ou **recherche exhaustive de clés**.

Pour qu'un système de cryptage réponde à une notion minimale de sécurité, il doit disposer d'un ensemble de clés possibles, ou **espace clé**, si vaste que les attaques par force brute sont infaisables. Tous les systèmes de chiffrement modernes répondent à cette norme. C'est ce qu'on appelle le **principe de l'espace de clés suffisant**. Un principe similaire s'applique généralement à différents types de systèmes cryptographiques.

Pour avoir une idée de la taille de l'espace clé des systèmes de cryptage modernes, supposons qu'un fichier ait été crypté avec une clé de 128 bits à l'aide de la norme de cryptage avancée. Cela signifie qu'un attaquant dispose d'un ensemble de $2^{128}$ clés qu'il doit parcourir pour effectuer une attaque par force brute. Pour avoir 0,78 % de chances de réussir avec cette stratégie, l'attaquant doit parcourir environ 2,65 \Nfois 10^{36}$ clés.

Supposons, de manière optimiste, qu'un attaquant puisse essayer 10^{16}$ clés par seconde (c'est-à-dire 10 quadrillions de clés par seconde). Pour tester 0,78 % de toutes les clés de l'espace des clés, son attaque devrait durer 2,65 fois 10^{20}$ secondes. Cela représente environ 8,4 billions d'années. Ainsi, même une attaque par force brute menée par un adversaire absurdement puissant n'est pas réaliste avec un système de cryptage moderne de 128 bits. C'est le principe de l'espace de clés suffisant qui entre en jeu.

Le chiffrement par décalage est-il plus sûr si l'attaquant ne connaît pas l'algorithme de chiffrement ? Peut-être, mais pas de beaucoup.

En tout état de cause, la cryptographie moderne part toujours du principe que la sécurité d'un système de cryptage symétrique repose uniquement sur le maintien du secret de la clé privée. L'attaquant est toujours supposé connaître tous les autres détails, y compris l'espace du message, l'espace de la clé, l'espace du texte chiffré, l'algorithme de sélection de la clé, l'algorithme de chiffrement et l'algorithme de déchiffrement.

L'idée selon laquelle la sécurité d'un système de cryptage symétrique ne peut reposer que sur le secret de la clé privée est connue sous le nom de **principe de Kerckhoffs**.

Dans l'esprit de Kerckhoffs, ce principe ne s'applique qu'aux systèmes de cryptage symétrique. Une version plus générale du principe s'applique toutefois à tous les autres types de schémas cryptographiques modernes : La conception d'un système cryptographique ne doit pas être secrète pour qu'il soit sûr ; le secret ne peut s'étendre qu'à certaines chaînes d'information, généralement une clé privée.

Le principe de Kerckhoffs est au cœur de la cryptographie moderne pour quatre raisons. [Premièrement, il n'existe qu'un nombre limité de schémas cryptographiques pour certains types d'applications. Par exemple, la plupart des applications modernes de chiffrement symétrique utilisent le chiffrement Rijndael. Le secret sur la conception d'un schéma est donc très limité. Il y a cependant beaucoup plus de flexibilité à garder secrète une clé privée pour le chiffrement Rijndael.

Deuxièmement, il est plus facile de remplacer une chaîne d'informations qu'un système cryptographique complet. Supposons que les employés d'une entreprise disposent tous du même logiciel de cryptage et que chacun d'entre eux possède une clé privée lui permettant de communiquer en toute confidentialité. La compromission des clés est un problème dans ce scénario, mais l'entreprise peut au moins conserver le logiciel avec de telles failles de sécurité. Si l'entreprise s'appuyait sur le secret du système, toute violation de ce secret nécessiterait le remplacement de l'ensemble du logiciel.

Troisièmement, le principe de Kerckhoffs permet la normalisation et la compatibilité entre les utilisateurs de systèmes cryptographiques. Cela présente des avantages considérables en termes d'efficacité. Par exemple, il est difficile d'imaginer comment des millions de personnes pourraient se connecter en toute sécurité aux serveurs web de Google chaque jour, si cette sécurité nécessitait de garder les schémas cryptographiques secrets.

Quatrièmement, le principe de Kerckhoff permet un examen public des schémas cryptographiques. Ce type d'examen est absolument nécessaire pour obtenir des schémas cryptographiques sûrs. À titre d'exemple, le principal algorithme de base de la cryptographie symétrique, le chiffrement Rijndael, a été le résultat d'un concours organisé par le National Institute of Standards and Technology entre 1997 et 2000.

Tout système qui tente d'atteindre la **sécurité par l'obscurité** est un système qui repose sur le fait de garder secrets les détails de sa conception et/ou de sa mise en œuvre. En cryptographie, il s'agirait spécifiquement d'un système qui repose sur le fait de garder secrets les détails de la conception du schéma cryptographique. La sécurité par l'obscurité est donc en contradiction directe avec le principe de Kerckhoffs.

La capacité de l'ouverture à renforcer la qualité et la sécurité s'étend également au monde numérique de manière plus large que la simple cryptographie. Les distributions Linux libres et open source telles que Debian, par exemple, présentent généralement plusieurs avantages par rapport à leurs homologues Windows et MacOS en termes de confidentialité, de stabilité, de sécurité et de flexibilité. Bien que cela puisse avoir de multiples causes, le principe le plus important est probablement, comme Eric Raymond l'a formulé dans son célèbre essai "The Cathedral and the Bazaar", qu'"avec suffisamment d'yeux, tous les bugs sont superficiels"[3] [3] C'est ce principe de sagesse des foules qui a donné à Linux son succès le plus important.

On ne peut jamais affirmer sans ambiguïté qu'un schéma cryptographique est "sûr" ou "peu sûr" Au contraire, il existe plusieurs notions de sécurité pour les systèmes cryptographiques. Chaque **définition de la sécurité cryptographique** doit préciser (1) les objectifs de sécurité, ainsi que (2) les capacités d'un attaquant. L'analyse des systèmes cryptographiques par rapport à une ou plusieurs notions spécifiques de sécurité permet de mieux comprendre leurs applications et leurs limites.

Nous n'entrerons pas dans les détails des différentes notions de sécurité cryptographique, mais vous devez savoir que deux hypothèses sont omniprésentes dans toutes les notions cryptographiques modernes de sécurité relatives aux schémas symétriques et asymétriques (et, sous une forme ou une autre, à d'autres primitives cryptographiques) :


- Les connaissances de l'attaquant sur le système sont conformes au principe de Kerckhoffs.
- L'attaquant ne peut pas réaliser une attaque par force brute sur le système. Plus précisément, les modèles de menace des notions cryptographiques de sécurité n'autorisent généralement même pas les attaques par force brute, car ils partent du principe qu'elles ne sont pas pertinentes.

**Notes:**

[1] Selon Seutonius, un chiffre à décalage avec une valeur de clé constante de 3 a été utilisé par Jules César dans ses communications militaires. Ainsi, A devenait toujours D, B toujours E, C toujours F, et ainsi de suite. Cette version particulière du chiffrement par décalage est donc connue sous le nom de **chiffrement de César** (bien qu'il ne s'agisse pas vraiment d'un chiffrement au sens moderne du terme, puisque la valeur de la clé est constante). Le chiffre de César aurait pu être sûr au premier siècle avant J.-C., si les ennemis de Rome n'étaient pas familiarisés avec le chiffrement. J.-C., si les ennemis de Rome n'étaient pas familiarisés avec le cryptage. Mais il est clair que ce n'est pas un système très sûr à l'époque moderne.

[2] Jonathan Katz et Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL : 2015), p. 7f.

[3] Eric Raymond, "The Cathedral and the Bazaar", document présenté au Linux Kongress, Würzburg, Allemagne (27 mai 1997). Il existe un certain nombre de versions ultérieures ainsi qu'un livre. Mes citations sont tirées de la page 30 du livre : Eric Raymond, _The Cathedral and the Bazaar : Musings on Linux and Open Source by an Accidental Revolutionary_, revised edn. (2001), O'Reilly : Sebastopol, CA.

## Chiffres en flux

<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Les systèmes de cryptage symétrique sont généralement divisés en deux types : *les *chiffres en continu** et les **chiffres en bloc**. Cette distinction est toutefois quelque peu problématique, car les gens utilisent ces termes de manière incohérente. Dans les prochaines sections, j'établirai la distinction de la manière qui me semble la plus appropriée. Sachez toutefois que de nombreuses personnes utiliseront ces termes d'une manière quelque peu différente de celle que j'ai exposée.

Examinons tout d'abord les algorithmes de chiffrement de flux. Un **chiffrement de flux** est un système de cryptage symétrique dans lequel le cryptage se fait en deux étapes.

Tout d'abord, une chaîne de la longueur du texte en clair est produite à l'aide d'une clé privée. Cette chaîne est appelée **keystream**.

Ensuite, le flux de clés est combiné mathématiquement avec le texte en clair pour produire un texte chiffré. Cette combinaison est généralement une opération XOR. Pour le décryptage, il suffit d'inverser l'opération. (Notez que $A \oplus B = B \oplus A$, dans le cas où $A$ et $B$ sont des chaînes de bits. L'ordre d'une opération XOR dans un chiffrement de flux n'a donc pas d'importance pour le résultat. Cette propriété est connue sous le nom de **commutativité**)

Un algorithme de chiffrement XOR typique est illustré à la *figure 3*. Vous prenez d'abord une clé privée $K$ et l'utilisez pour générer un flux de clés. Le flux de clés est ensuite combiné au texte en clair par une opération XOR pour produire le texte chiffré. Tout agent qui reçoit le texte chiffré peut facilement le déchiffrer s'il possède la clé $K$. Il lui suffit de créer un flux de clés aussi long que le texte chiffré conformément à la procédure spécifiée dans le système et de l'associer au texte chiffré par une opération XOR.

*Figure 3 : Chiffrement d'un flux XOR*

![Figure 3: An XOR stream cipher](assets/Figure4-3.webp "Figure 3: An XOR stream cipher")

N'oubliez pas qu'un schéma de chiffrement est généralement un modèle de chiffrement avec le même algorithme de base, plutôt qu'une spécification exacte. Par extension, un algorithme de chiffrement par flot est généralement un modèle de chiffrement dans lequel vous pouvez utiliser des clés de différentes longueurs. Bien que la longueur de la clé puisse avoir un impact sur certains détails mineurs du schéma, elle n'aura pas d'impact sur sa forme essentielle.

Le chiffrement par décalage est un exemple de chiffrement de flux très simple et peu sûr. En utilisant une seule lettre (la clé privée), vous pouvez produire une chaîne de lettres de la longueur du message (le flux de clés). Ce flux de clés est ensuite combiné au texte en clair par une opération modulo pour produire un texte chiffré. (Cette opération modulo peut être simplifiée en une opération XOR lorsque les lettres sont représentées en bits).

Un autre exemple célèbre de chiffrement par flux est le **chiffrement de Vigenere**, d'après Blaise de Vigenere qui l'a entièrement mis au point à la fin du XVIe siècle (bien que d'autres aient effectué de nombreux travaux antérieurs). Il s'agit d'un exemple de **chiffrement par substitution polyalphabétique** : un système de chiffrement dans lequel l'alphabet du texte chiffré pour un symbole du texte clair change en fonction de sa position dans le texte. Contrairement au chiffrement par substitution monoalphabétique, les symboles du texte chiffré peuvent être associés à plus d'un symbole du texte en clair.

Alors que le cryptage gagnait en popularité dans l'Europe de la Renaissance, l'**analyse cryptographique**, c'est-à-dire le décryptage des textes chiffrés, gagnait également en popularité, en particulier grâce à l'**analyse de fréquence**. Cette dernière utilise les régularités statistiques de notre langue pour déchiffrer les textes chiffrés et a été découverte par les érudits arabes dès le IXe siècle. C'est une technique qui fonctionne particulièrement bien avec les textes longs. Dans les années 1700, en Europe, même les chiffres de substitution monoalphabétiques les plus sophistiqués n'étaient plus suffisants pour résister à l'analyse de fréquence, en particulier dans le domaine militaire et de la sécurité. Comme le chiffre de Vigenere offrait une avancée significative en matière de sécurité, il est devenu populaire à cette époque et s'est répandu à la fin des années 1700.

De manière informelle, le système de cryptage fonctionne de la manière suivante :

1. Sélectionnez un mot de plusieurs lettres comme clé privée.

2. Pour tout message, appliquer le chiffrement par décalage à chaque lettre du message en utilisant la lettre correspondante du mot-clé comme décalage.

3. Si vous avez parcouru le mot-clé mais que vous n'avez pas encore totalement déchiffré le texte en clair, appliquez à nouveau les lettres du mot-clé aux lettres correspondantes du reste du texte en tant que chiffre à décalage.

4. Poursuivre ce processus jusqu'à ce que l'ensemble du message ait été déchiffré.

Pour illustrer, supposons que votre clé privée soit "GOLD" et que vous souhaitiez crypter le message "CRYPTOGRAPHIE". Dans ce cas, vous procédez comme suit selon le chiffrement de Vigenère :


- $c_0 = [(2 + 6) \mod 26] = 8 = I$$
- $c_1 = [(17 + 14) \mod 26] = 5 = F$
- $c_2 = [(24 + 11) \mod 26] = 9 = J$
- $c_3 = [(15 + 3) \mod 26] = 18 = S$$
- $c_4 = [(19 + 6) \mod 26] = 25 = Z$$
- $c_5 = [(14 + 14) \mod 26] = 2 = C$
- $c_6 = [(6 + 11) \mod 26] = 17 = R$
- $c_7 = [(17 + 3) \mod 26] = 20 = U$
- $c_8 = [(0 + 6) \mod 26] = 6 = G$
- $c_9 = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$

Ainsi, le texte chiffré $c$ = "IFJSZCRUGDSB".

Un autre exemple célèbre de chiffrement de flux est le **compteur à usage unique**. Dans ce cas, il suffit de créer une chaîne de bits aléatoires aussi longue que le message en clair et de produire le texte chiffré par l'opération XOR. La clé privée et le flux de clés sont donc équivalents dans le cas d'un chiffrement à usage unique.

Alors que le chiffrement Shift et le chiffrement Vigenere sont très peu sûrs à l'ère moderne, le tampon à usage unique est très sûr s'il est utilisé correctement. L'application la plus célèbre du pavé à usage unique a probablement été, au moins jusque dans les années 1980, la **ligne directe Washington-Moscou**. [4]

La ligne directe est un lien de communication direct entre Washington et Moscou pour les questions urgentes. Elle a été mise en place après la crise des missiles de Cuba. La technologie utilisée s'est transformée au fil des ans. Actuellement, elle comprend un câble direct en fibre optique ainsi que deux liaisons par satellite (pour la redondance), qui permettent l'envoi de courriels et de messages textuels. La liaison aboutit à différents endroits aux États-Unis. Le Pentagone, la Maison Blanche et le mont Raven Rock sont des points d'arrivée connus. Contrairement à l'opinion générale, la ligne directe n'a jamais impliqué de téléphone.

Pour l'essentiel, le système du pavé numérique à usage unique fonctionnait de la manière suivante. Washington et Moscou disposaient de deux séries de nombres aléatoires. Une série de nombres aléatoires, créée par les Russes, concernait le cryptage et le décryptage de tous les messages en langue russe. Une série de nombres aléatoires, créée par les Américains, concerne le cryptage et le décryptage de tout message en langue anglaise. De temps à autre, d'autres nombres aléatoires étaient livrés à l'autre partie par des courriers de confiance.

Washington et Moscou ont donc pu communiquer secrètement en utilisant ces nombres aléatoires pour créer des codes à usage unique. Chaque fois que vous deviez communiquer, vous utilisiez la portion suivante de nombres aléatoires pour votre message.

Bien qu'il soit hautement sécurisé, le bloc-notes à usage unique est confronté à d'importantes limitations pratiques : la clé doit être aussi longue que le message et aucune partie d'un bloc-notes à usage unique ne peut être réutilisée. Cela signifie qu'il faut savoir où l'on se trouve dans le pavé à usage unique, stocker un nombre considérable de bits et échanger de temps en temps des bits aléatoires avec ses contreparties. Par conséquent, le pavé à usage unique n'est pas souvent utilisé dans la pratique.

Au lieu de cela, les principaux algorithmes de chiffrement de flux utilisés dans la pratique sont des algorithmes de chiffrement de flux pseudo-aléatoires**. Salsa20 et une variante étroitement liée appelée ChaCha sont des exemples de chiffrements de flux pseudo-aléatoires couramment utilisés.

Avec ces algorithmes de chiffrement de flux pseudo-aléatoires, il faut d'abord sélectionner au hasard une clé K plus courte que la longueur du texte en clair. Cette clé aléatoire K est généralement créée par notre ordinateur sur la base de données imprévisibles qu'il collecte au fil du temps, telles que le temps écoulé entre les messages du réseau, les mouvements de la souris, etc.

Cette clé aléatoire $K$ est ensuite insérée dans un algorithme d'expansion qui crée un flux de clés pseudo-aléatoires aussi long que le message. Vous pouvez spécifier précisément la longueur du flux de clés (par exemple, 500 bits, 1000 bits, 1200 bits, 29 117 bits, etc.)

Un flux de clés pseudo-aléatoire apparaît *comme s'il avait été choisi de manière totalement aléatoire dans l'ensemble des chaînes de caractères de même longueur. Par conséquent, le chiffrement à l'aide d'un flux de clés pseudo-aléatoire apparaît comme s'il avait été effectué à l'aide d'un bloc-notes à usage unique. Mais ce n'est évidemment pas le cas.

Comme notre clé privée est plus courte que le flux de clés et que notre algorithme expansionniste doit être déterministe pour que le processus de cryptage/décryptage fonctionne, tous les flux de clés de cette longueur particulière n'auraient pas pu être obtenus en sortie de notre opération expansionniste.

Supposons, par exemple, que notre clé privée ait une longueur de 128 bits et que nous puissions l'insérer dans un algorithme expansionniste pour créer un flux de clés beaucoup plus long, disons de 2 500 bits. Comme notre algorithme expansionniste doit être déterministe, il peut au maximum sélectionner des chaînes de $1/2^{128}$ d'une longueur de 2 500 bits. Un tel flux de clés ne peut donc jamais être sélectionné de manière entièrement aléatoire parmi toutes les chaînes de même longueur.

Notre définition du chiffrement de flux comporte deux aspects : (1) un flux de clés aussi long que le texte en clair est généré à l'aide d'une clé privée ; et (2) ce flux de clés est combiné avec le texte en clair, généralement par une opération XOR, pour produire le texte chiffré.

Certains définissent parfois la condition (1) de manière plus stricte, en affirmant que le flux de clés doit spécifiquement être pseudo-aléatoire. Cela signifie que ni le shift cipher, ni le one-time pad ne seraient considérés comme des stream ciphers.

À mon avis, une définition plus large de la condition (1) permet d'organiser plus facilement les systèmes de chiffrement. En outre, cela signifie que nous n'avons pas à cesser d'appeler un système de chiffrement particulier un chiffrement par flux simplement parce que nous apprenons qu'il ne repose pas réellement sur des flux de clés pseudo-aléatoires.

**Notes:**

[4] Crypto Museum, "Washington-Moscow hotline", 2013, disponible sur [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).

## Chiffres en bloc

<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

La première façon dont un **chiffrement en bloc** est communément compris est comme quelque chose de plus primitif qu'un chiffrement en flux : Un algorithme de base qui effectue une transformation préservant la longueur d'une chaîne d'une longueur appropriée à l'aide d'une clé. Cet algorithme peut être utilisé pour créer des schémas de chiffrement et peut-être d'autres types de schémas cryptographiques.

Fréquemment, un algorithme de chiffrement par blocs peut prendre en entrée des chaînes de longueur variable, telles que 64, 128 ou 256 bits, ainsi que des clés de longueur variable, telles que 128, 192 ou 256 bits. Bien que certains détails de l'algorithme puissent changer en fonction de ces variables, l'algorithme de base ne change pas. Si c'était le cas, nous parlerions de deux algorithmes de chiffrement par blocs différents. Notez que l'utilisation de la terminologie de l'algorithme de base ici est la même que pour les schémas de cryptage.

La *figure 4* ci-dessous illustre le fonctionnement d'un algorithme de chiffrement par blocs. Un message $M$ de longueur $L$ et une clé $K$ servent d'entrées au chiffrement par blocs. Il produit un message $M'$ de longueur $L$. La clé ne doit pas nécessairement avoir la même longueur que $M$ et $M'$ pour la plupart des algorithmes de chiffrement par blocs.

*Figure 4 : Un algorithme de chiffrement par blocs*

![Figure 4: A block cipher](assets/Figure4-4.webp "Figure 4: A block cipher")

Un algorithme de chiffrement par blocs n'est pas en soi un système de chiffrement. Mais il peut être utilisé avec différents **modes d'opération** pour produire différents schémas de chiffrement. Un mode d'opération ajoute simplement des opérations supplémentaires en dehors du chiffrement par blocs.

Pour illustrer ce fonctionnement, supposons un chiffrement par blocs (BC) qui nécessite une chaîne d'entrée de 128 bits et une clé privée de 128 bits. La figure 5 ci-dessous montre comment ce chiffrement par blocs peut être utilisé avec le **mode livre de code électronique** (**mode ECB**) pour créer un schéma de chiffrement. (Les ellipses à droite indiquent que vous pouvez répéter ce schéma aussi longtemps que nécessaire).

*Figure 5 : Chiffrement par blocs en mode ECB*

![Figure 5: A block cipher with ECB mode](assets/Figure4-5.webp "Figure 5: A block cipher with ECB mode")

Le processus de cryptage du livre de code électronique à l'aide du chiffrement par blocs est le suivant. Vérifiez si vous pouvez diviser votre message en clair en blocs de 128 bits. Si ce n'est pas le cas, ajoutez du **padding** au message, de manière à ce que le résultat puisse être divisé uniformément par la taille du bloc de 128 bits. Il s'agit des données utilisées pour le processus de cryptage.

Divisez maintenant les données en morceaux de chaînes de 128 bits ($M_1$, $M_2$, $M_3$, etc.). Faites passer chaque chaîne de 128 bits par le système de chiffrement par blocs avec votre clé de 128 bits pour produire des morceaux de texte chiffré de 128 bits ($C_1$, $C_2$, $C_3$, etc.). Ces morceaux, une fois recombinés, forment le texte chiffré complet.

Le décryptage est simplement le processus inverse, bien que le destinataire ait besoin d'un moyen reconnaissable pour retirer tout élément de remplissage des données décryptées afin de produire le message en clair d'origine.

Bien que relativement simple, le chiffrement par blocs en mode livre de code électronique manque de sécurité. En effet, il conduit à un **chiffrement déterministe**. Deux chaînes de données identiques de 128 bits sont cryptées exactement de la même manière. Cette information peut être exploitée.

Au lieu de cela, tout schéma de chiffrement construit à partir d'un chiffrement par blocs devrait être **probabiliste** : c'est-à-dire que le chiffrement de n'importe quel message $M$, ou de n'importe quel morceau spécifique de $M$, devrait généralement donner un résultat différent à chaque fois. [5]

Le **mode de chaînage de blocs de chiffrement** (**mode CBC**) est probablement le mode le plus couramment utilisé avec un chiffrement par blocs. La combinaison, si elle est bien faite, produit un système de cryptage probabiliste. Vous pouvez voir une représentation de ce mode de fonctionnement dans la *Figure 6* ci-dessous.

*Figure 6 : Chiffrement par blocs en mode CBC*

![Figure 6: A block cipher with CBC mode](assets/Figure4-6.webp "Figure 6: A block cipher with CBC mode")

Supposons que la taille du bloc soit à nouveau de 128 bits. Pour commencer, vous devez donc vous assurer que votre message en clair d'origine reçoit le rembourrage nécessaire.

Ensuite, vous faites un XOR entre la première partie de 128 bits de votre texte en clair et un **vecteur d'initialisation** de 128 bits. Le résultat est placé dans le chiffrement par blocs pour produire un texte chiffré pour le premier bloc. Pour le deuxième bloc de 128 bits, vous devez d'abord faire un XOR entre le texte en clair et le texte chiffré du premier bloc, avant de l'insérer dans le système de chiffrement par blocs. Vous continuez ce processus jusqu'à ce que vous ayez crypté l'intégralité de votre message en clair.

Lorsque vous avez terminé, vous envoyez le message crypté avec le vecteur d'initialisation non crypté au destinataire. Le destinataire doit connaître le vecteur d'initialisation, sinon il ne peut pas décrypter le texte chiffré.

Cette construction est beaucoup plus sûre que le mode livre de code électronique lorsqu'elle est utilisée correctement. Vous devez tout d'abord vous assurer que le vecteur d'initialisation est une chaîne aléatoire ou pseudo-aléatoire. En outre, vous devez utiliser un vecteur d'initialisation différent chaque fois que vous utilisez ce système de cryptage.

En d'autres termes, votre vecteur d'initialisation doit être un nonce aléatoire ou pseudo-aléatoire, où **nonce** signifie "un nombre qui n'est utilisé qu'une seule fois" Si vous respectez cette pratique, le mode CBC avec un chiffrement par blocs garantit que deux blocs de texte en clair identiques seront généralement chiffrés différemment à chaque fois.

Enfin, nous allons nous intéresser au **mode de rétroaction de la sortie** (**modeOFB**). Vous pouvez voir une représentation de ce mode dans la *Figure 7*.

*Figure 7 : Chiffrement par blocs en mode OFB*

![Figure 7: A block cipher with OFB mode](assets/Figure4-7.webp "Figure 7: A block cipher with OFB mode")

Avec le mode OFB, vous sélectionnez également un vecteur d'initialisation. Mais ici, pour le premier bloc, le vecteur d'initialisation est directement inséré dans le chiffrement par blocs avec votre clé. Les 128 bits qui en résultent sont alors traités comme un flux de clés. Ce flux de clés est mis en XOR avec le texte en clair pour produire le texte chiffré du bloc. Pour les blocs suivants, vous utilisez le flux de clés du bloc précédent comme entrée dans le chiffrement par blocs et vous répétez les étapes.

Si vous regardez attentivement, ce qui a été créé ici à partir du chiffrement par blocs avec le mode OFB est un chiffrement par flux. Vous générez des portions de flux de clés de 128 bits jusqu'à ce que vous obteniez la longueur du texte en clair (en éliminant les bits dont vous n'avez pas besoin dans la dernière portion de flux de clés de 128 bits). Ensuite, vous effectuez un XOR entre le flux de clés et votre message en clair pour obtenir le texte chiffré.

Dans la section précédente sur le chiffrement par flux, j'ai indiqué que vous produisiez un flux de clés à l'aide d'une clé privée. Pour être exact, il ne doit pas seulement être créé à l'aide d'une clé privée. Comme vous pouvez le voir en mode OFB, le flux de clés est produit à l'aide d'une clé privée et d'un vecteur d'initialisation.

Comme pour le mode CBC, il est important de sélectionner un nonce pseudo-aléatoire ou aléatoire pour le vecteur d'initialisation chaque fois que vous utilisez un chiffrement par blocs en mode OFB. Sinon, la même chaîne de messages de 128 bits envoyée dans différentes communications sera chiffrée de la même manière. C'est l'une des façons de créer un chiffrement probabiliste avec un chiffrement par flux.

Certains algorithmes de chiffrement par flux n'utilisent qu'une clé privée pour créer un flux de clés. Pour ces algorithmes de chiffrement par flux, il est important d'utiliser un nonce aléatoire pour sélectionner la clé privée pour chaque instance de communication. Sinon, les résultats du cryptage avec ces algorithmes de chiffrement de flux seront également déterministes, ce qui entraînera des problèmes de sécurité.

Le chiffrement par blocs moderne le plus populaire est le **chiffrement Rijndael**. Il a remporté le concours organisé par le National Institute of Standards and Technology (NIST) entre 1997 et 2000 pour remplacer une norme de cryptage plus ancienne, la **norme de cryptage des données** (**DES**).

Le chiffrement Rijndael peut être utilisé avec différentes spécifications pour la longueur des clés et la taille des blocs, ainsi que dans différents modes de fonctionnement. Le comité du concours du NIST a adopté une version restreinte du chiffrement de Rijndael, à savoir une version qui exige des tailles de blocs de 128 bits et des longueurs de clés de 128 bits, 192 bits ou 256 bits, dans le cadre de la **norme de chiffrement avancé** (**AES**). Il s'agit en fait de la principale norme pour les applications de cryptage symétrique. Il est si sûr que même la NSA est apparemment disposée à l'utiliser avec des clés de 256 bits pour des documents très secrets[6]. [6]

Le chiffrement par blocs AES sera expliqué en détail au *chapitre 5*.

**Notes:**

[5] L'importance du chiffrement probabiliste a été soulignée pour la première fois par Shafi Goldwasser et Silvio Micali, "Probabilistic encryption", _Journal of Computer and System Sciences_, 28 (1984), 270-99.

[6] Voir NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).

## Dissiper la confusion

<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

La confusion concernant la distinction entre les chiffrements par blocs et les chiffrements par flots est due au fait que les gens comprennent parfois que le terme chiffrements par blocs se réfère spécifiquement à un *chiffrement par blocs avec un mode de chiffrement par blocs*.

Prenons les modes ECB et CBC de la section précédente. Ces modes exigent spécifiquement que les données à chiffrer soient divisibles par la taille du bloc (ce qui signifie qu'il peut être nécessaire d'utiliser un tampon pour le message d'origine). En outre, dans ces modes, les données sont également traitées directement par le chiffrement par bloc (et pas seulement combinées avec le résultat d'une opération de chiffrement par bloc comme dans le mode OFB).

Par conséquent, on peut également définir un **chiffrement par blocs** comme tout système de chiffrement qui opère sur des blocs de longueur fixe du message à la fois (où tout bloc doit être plus long qu'un octet, sinon il s'effondre en un chiffrement par flux). Les données à chiffrer et le texte chiffré doivent être répartis uniformément dans cette taille de bloc. En général, la taille du bloc est de 64, 128, 192 ou 256 bits. En revanche, un algorithme de chiffrement par flux peut chiffrer n'importe quel message par morceaux d'un bit ou d'un octet à la fois.

Avec cette compréhension plus spécifique du chiffrement par blocs, on peut en effet affirmer que les schémas de chiffrement modernes sont soit des chiffrages par flux, soit des chiffrages par blocs. À partir de maintenant, j'utiliserai le terme "chiffrement par blocs" dans son sens le plus général, sauf indication contraire.

La discussion sur le mode OFB dans la section précédente soulève également un autre point intéressant. Certains algorithmes de chiffrement de flux sont construits à partir d'algorithmes de chiffrement par blocs, comme Rijndael avec OFB. D'autres, comme Salsa20 et ChaCha, ne sont pas créés à partir de chiffrages par blocs. On pourrait appeler ces derniers **chiffres de flux primitifs**. (Il n'existe pas vraiment de terme normalisé pour désigner ces algorithmes de chiffrement)

Lorsque l'on parle des avantages et des inconvénients des algorithmes de chiffrement par flot et des algorithmes de chiffrement par bloc, on compare généralement les algorithmes de chiffrement par flot primitifs aux systèmes de chiffrement basés sur les algorithmes de chiffrement par bloc.

Alors qu'il est toujours possible de construire facilement un algorithme de chiffrement par flux à partir d'un algorithme de chiffrement par bloc, il est généralement très difficile de construire un algorithme de chiffrement par bloc (tel que le mode CBC) à partir d'un algorithme de chiffrement par flux primitif.

À partir de cette discussion, vous devriez maintenant comprendre la *Figure 8*. Elle donne un aperçu des schémas de chiffrement symétrique. Nous utilisons trois types de systèmes de cryptage : les algorithmes de chiffrement de flux primitifs, les algorithmes de chiffrement de flux par blocs et les algorithmes de chiffrement par blocs en mode bloc (également appelés "algorithmes de chiffrement par blocs" dans le diagramme).

*Figure 8 : Vue d'ensemble des schémas de cryptage symétrique*

![Figure 8: Overview of symmetric encryption schemes](assets/Figure4-8.webp "Figure 8: Overview of symmetric encryption schemes")

## Codes d'authentification des messages

<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>

Le cryptage concerne le secret. Mais la cryptographie s'intéresse également à des thèmes plus larges, tels que l'intégrité, l'authenticité et la non-répudiation des messages. Les **codes d'authentification des messages** (MAC) sont des systèmes cryptographiques à clé symétrique qui assurent l'authenticité et l'intégrité des communications.

Pourquoi la communication a-t-elle besoin d'autre chose que du secret ? Supposons que Bob envoie un message à Alice en utilisant un cryptage pratiquement incassable. Tout attaquant qui intercepte ce message ne sera pas en mesure d'obtenir des informations significatives sur son contenu. Cependant, l'attaquant dispose encore d'au moins deux autres vecteurs d'attaque :

1. Elle pourrait intercepter le texte chiffré, en modifier le contenu et l'envoyer à Alice.

2. Elle pourrait bloquer entièrement le message de Bob et envoyer son propre texte chiffré.

Dans ces deux cas, l'attaquant pourrait ne pas avoir d'informations sur le contenu des cryptogrammes (1) et (2). Mais il pourrait tout de même causer des dommages importants de cette manière. C'est là que les codes d'authentification des messages prennent toute leur importance.

Les codes d'authentification des messages sont définis de manière générale comme des schémas cryptographiques symétriques comportant trois algorithmes : un algorithme de génération de clés, un algorithme de génération de balises et un algorithme de vérification. Un MAC sécurisé garantit que les balises sont **existentiellement infalsifiables** pour tout attaquant, c'est-à-dire qu'il ne peut pas créer avec succès une balise sur le message qui est vérifié, à moins qu'il ne possède la clé privée.

Bob et Alice peuvent lutter contre la manipulation d'un message particulier à l'aide d'un MAC. Supposons pour l'instant qu'ils ne se soucient pas du secret. Ils veulent seulement s'assurer que le message reçu par Alice provient bien de Bob et qu'il n'a pas été modifié de quelque manière que ce soit.

Le processus est décrit dans la *Figure 9*. Pour utiliser un **MAC** (Message Authentication Code), ils doivent d'abord générer une clé privée $K$ qu'ils partagent tous les deux. Bob crée une étiquette $T$ pour le message en utilisant la clé privée $K$. Il envoie ensuite le message ainsi que l'étiquette du message à Alice. Elle peut alors vérifier que Bob a bien créé la balise en soumettant la clé privée, le message et la balise à un algorithme de vérification.

*Figure 9 : Vue d'ensemble des schémas de cryptage symétrique*

![Figure 9: Overview of symmetric encryption schemes](assets/Figure4-9.webp "Figure 9: Overview of symmetric encryption schemes")

En raison de l'infalsifiabilité **existentielle**, un attaquant ne peut pas modifier le message $M$ de quelque manière que ce soit ou créer son propre message avec une balise valide. Il en est ainsi même si l'attaquant observe les étiquettes de nombreux messages entre Bob et Alice qui utilisent la même clé privée. Tout au plus, un attaquant pourrait empêcher Alice de recevoir le message $M$ (un problème que la cryptographie ne peut pas résoudre).

Un MAC garantit qu'un message a effectivement été créé par Bob. Cette authenticité implique automatiquement l'intégrité du message, c'est-à-dire que si Bob a créé un message, alors, ipso facto, il n'a été modifié en aucune façon par un attaquant. Ainsi, à partir de maintenant, toute préoccupation concernant l'authentification devrait être automatiquement comprise comme impliquant une préoccupation concernant l'intégrité.

Bien que j'aie établi une distinction entre l'authenticité et l'intégrité des messages dans mon analyse, il est également courant d'utiliser ces termes comme synonymes. Ils renvoient donc à l'idée de messages qui ont été créés par un expéditeur particulier et qui n'ont subi aucune modification. Dans cet esprit, les codes d'authentification des messages sont souvent appelés **codes d'intégrité des messages**.

## Cryptage authentifié

<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>

En règle générale, on souhaite garantir à la fois le secret et l'authenticité des communications, c'est pourquoi les systèmes de cryptage et les systèmes MAC sont généralement utilisés conjointement.

Un **système de chiffrement authentifié** est un système qui combine le chiffrement avec un MAC d'une manière hautement sécurisée. Plus précisément, il doit répondre aux normes d'infalsifiabilité existentielle ainsi qu'à une notion très forte de secret, à savoir une notion qui résiste aux **attaques par texte choisi**. [7]

Pour qu'un système de cryptage soit résistant aux attaques par texte choisi, il doit répondre aux normes de **non-malléabilité** : c'est-à-dire que toute modification d'un texte chiffré par un attaquant doit produire soit un texte chiffré invalide, soit un texte déchiffré qui n'a aucun rapport avec le texte original. [8]

Comme un schéma de chiffrement authentifié garantit qu'un texte chiffré créé par un attaquant est toujours invalide (puisque l'étiquette ne sera pas vérifiée), il répond aux normes de résistance aux attaques par texte chiffré choisi. Il est intéressant de noter qu'il est possible de prouver qu'un schéma de chiffrement authentifié peut toujours être créé à partir de la combinaison d'un MAC non falsifiable et d'un schéma de chiffrement qui répond à une notion de sécurité moins stricte, connue sous le nom de **sécurité contre les attaques par texte choisi**.

Nous n'entrerons pas dans tous les détails de la construction des systèmes de cryptage authentifiés. Mais il est important de connaître deux détails de leur construction.

Tout d'abord, un système de cryptage authentifié traite d'abord le cryptage et crée ensuite une étiquette de message sur le texte crypté. Il s'avère que d'autres approches, telles que la combinaison du texte chiffré avec une balise sur le texte en clair, ou la création d'une balise puis le chiffrement du texte en clair et de la balise, ne sont pas sûres. En outre, les deux opérations disposent de leur propre clé privée sélectionnée de manière aléatoire, sans quoi votre sécurité est gravement compromise.

Le principe susmentionné s'applique plus généralement : *vous devez toujours utiliser des clés distinctes lorsque vous combinez des schémas cryptographiques de base*.

Un schéma de cryptage authentifié est illustré à la *figure 10*. Bob crée d'abord un texte chiffré $C$ à partir du message $M$ en utilisant une clé choisie au hasard $K_C$. Il crée ensuite une étiquette de message $T$ en faisant passer le texte chiffré et une autre clé choisie au hasard $K_T$ par l'algorithme de génération d'étiquettes. Le texte chiffré et la balise de message sont envoyés à Alice.

Alice commence par vérifier si l'étiquette est valide compte tenu du texte chiffré $C$ et de la clé $K_T$. Si elle est valide, elle peut alors déchiffrer le message à l'aide de la clé $K_C$. Non seulement elle est assurée d'une notion très forte de secret dans leurs communications, mais elle sait également que le message a été créé par Bob.

*Figure 10 : Schéma de cryptage authentifié*

![Figure 10: An authenticated encryption scheme](assets/Figure4-10.webp "Figure 10: An authenticated encryption scheme")

Comment les MAC sont-ils créés ? Bien que les MAC puissent être créés par de multiples méthodes, un moyen courant et efficace consiste à utiliser des **fonctions de hachage cryptographiques**.

Nous présenterons les fonctions de hachage cryptographique plus en détail au *Chapitre 6*. Pour l'instant, sachez simplement qu'une **fonction de hachage** est une fonction efficacement calculable qui prend des entrées de taille arbitraire et produit des sorties de longueur fixe. Par exemple, la fonction de hachage populaire **SHA-256** (secure hash algorithm 256) génère toujours une sortie de 256 bits, quelle que soit la taille de l'entrée. Certaines fonctions de hachage, comme SHA-256, ont des applications utiles en cryptographie.

Le type d'étiquette le plus courant produit à l'aide d'une fonction de hachage cryptographique est le **code d'authentification de message basé sur le hachage** (HMAC). Le processus est décrit dans la *figure 11*. Une partie produit deux clés distinctes à partir d'une clé privée $K$, la clé intérieure $K_1$ et la clé extérieure $K_2$. Le texte en clair $M$ ou le texte chiffré $C$ est ensuite haché avec la clé interne. Le résultat $T'$ est ensuite haché avec la clé extérieure pour produire l'étiquette de message $T$.

Il existe une palette de fonctions de hachage qui peuvent être utilisées pour créer un HMAC. La fonction de hachage la plus couramment utilisée est SHA-256.

*Figure 11 : HMAC*

![Figure 11: HMAC](assets/Figure4-11.webp "Figure 11: HMAC")

**Notes:**

[7] Les résultats spécifiques discutés dans cette section sont tirés de Katz et Lindell, pp. 131-47.

[8] Techniquement, la définition des attaques par texte chiffré choisi est différente de la notion de non-malléabilité. Mais vous pouvez montrer que ces deux notions de sécurité sont équivalentes.

## Sessions de communication sécurisées

<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Supposons que deux parties participent à une session de communication et qu'elles envoient plusieurs messages dans les deux sens.

Un système de cryptage authentifié permet au destinataire d'un message de vérifier qu'il a été créé par son partenaire lors de la session de communication (tant que la clé privée n'a pas été divulguée). Cela fonctionne assez bien pour un seul message. Toutefois, en règle générale, deux parties s'envoient des messages dans un sens et dans l'autre au cours d'une session de communication. Dans ce cas, un système de cryptage simple et authentifié tel que celui décrit dans la section précédente n'offre pas une sécurité suffisante.

La principale raison en est qu'un système de cryptage authentifié n'offre aucune garantie que le message a bien été envoyé par l'agent qui l'a créé au cours d'une session de communication. Considérons les trois vecteurs d'attaque suivants :

1. **Attaque par relecture** : Un attaquant envoie à nouveau un texte chiffré et une balise qu'il a interceptés entre deux parties à un moment antérieur.

2. **Attaque par réordonnancement** : Un attaquant intercepte deux messages à des moments différents et les envoie au destinataire dans l'ordre inverse.

3. **Attaque par réflexion** : Un attaquant observe un message envoyé de A à B et envoie également ce message à A.

Bien que l'attaquant n'ait pas connaissance du texte chiffré et ne puisse pas créer des textes chiffrés usurpés, les attaques susmentionnées peuvent toujours causer des dommages importants aux communications.

Supposons, par exemple, qu'un message particulier entre les deux parties implique le transfert de fonds financiers. Une attaque par rejeu pourrait transférer les fonds une seconde fois. Un système de cryptage authentifié classique n'a aucune défense contre de telles attaques.

Heureusement, ces types d'attaques peuvent être facilement atténués dans une session de communication en utilisant des **identifiants** et des **indicateurs de temps relatif**.

Des identificateurs peuvent être ajoutés au message en clair avant le cryptage. Cela empêcherait toute attaque par réflexion. Un indicateur de temps relatif peut, par exemple, être un numéro de séquence dans une session de communication particulière. Chaque partie ajoute un numéro de séquence à un message avant le cryptage, de sorte que le destinataire sait dans quel ordre les messages ont été envoyés. Cela élimine la possibilité d'attaques par réordonnancement. Il élimine également les attaques par rejeu. Tout message envoyé par un attaquant en aval portera un ancien numéro de séquence, et le destinataire saura qu'il ne doit pas traiter le message à nouveau.

Pour illustrer le fonctionnement des sessions de communication sécurisées, supposons à nouveau Alice et Bob. Ils envoient un total de quatre messages dans les deux sens. Vous pouvez voir comment fonctionne un système de cryptage authentifié avec des identifiants et des numéros de séquence dans la *Figure 11* ci-dessous.

La session de communication commence par l'envoi par Bob d'un texte chiffré $C_{0,B}$ à Alice avec une étiquette de message $T_{0,B}$. Le texte chiffré contient le message, ainsi qu'un identifiant (BOB) et un numéro de séquence (0). La balise $T_{0,B}$ est apposée sur l'ensemble du texte chiffré. Dans leurs communications ultérieures, Alice et Bob conservent ce protocole, en mettant à jour les champs si nécessaire.

*Figure 12 : Une session de communication sécurisée*

![Figure 12: A secure communication session](assets/Figure4-12.webp "Figure 12: A secure communication sessesion")

# RC4 et AES

<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

## Le chiffrement de flux RC4

<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>

Dans ce chapitre, nous examinerons les détails d'un système de cryptage utilisant un algorithme de chiffrement primitif moderne, RC4 (ou "Rivest cipher 4"), et un algorithme de chiffrement par blocs moderne, AES. Alors que le chiffrement RC4 est tombé en disgrâce en tant que méthode de cryptage, AES est la norme en matière de cryptage symétrique moderne. Ces deux exemples devraient vous donner une meilleure idée de la manière dont le chiffrement symétrique fonctionne sous le capot.

___

Afin d'avoir une idée du fonctionnement des algorithmes de chiffrement de flux pseudo-aléatoires modernes, je me concentrerai sur l'algorithme de chiffrement de flux RC4. Il s'agit d'un algorithme de chiffrement de flux pseudo-aléatoire utilisé dans les protocoles de sécurité des points d'accès sans fil WEP et WAP, ainsi que dans le protocole TLS. Comme le RC4 présente de nombreuses faiblesses avérées, il est tombé en disgrâce. En fait, l'Internet Engineering Task Force interdit désormais l'utilisation des suites RC4 par les applications client et serveur dans toutes les instances de TLS. Néanmoins, il fonctionne bien comme exemple pour illustrer le fonctionnement d'un chiffrement de flux primitif.

Pour commencer, je vais d'abord montrer comment chiffrer un message en clair à l'aide d'un algorithme de chiffrement RC4. Supposons que notre message en clair soit "SOUP" Le cryptage à l'aide de notre algorithme de chiffrement RC4 pour bébés se déroule alors en quatre étapes.

### Étape 1

Tout d'abord, définissez un tableau **S** avec $S[0] = 0$ à $S[7] = 7$. Un tableau signifie ici simplement une collection mutable de valeurs organisées par un index, également appelée liste dans certains langages de programmation (par exemple, Python). Dans ce cas, l'index va de 0 à 7, et les valeurs vont également de 0 à 7. **S** se présente donc comme suit :


- $S = [0, 1, 2, 3, 4, 5, 6, 7]$

Les valeurs ne sont pas des nombres ASCII, mais des représentations décimales de chaînes de 1 octet. Ainsi, la valeur 2 serait égale à $0000 \ 0011$. La longueur du tableau **S** est donc de 8 octets.

### Étape 2

Deuxièmement, définissez un tableau de clés **K** de 8 octets en choisissant une clé entre 1 et 8 octets (aucune fraction d'octet n'est autorisée). Comme chaque octet est composé de 8 bits, vous pouvez choisir n'importe quel nombre entre 0 et 255 pour chaque octet de votre clé.

Supposons que nous choisissions notre clé **k** comme $[14, 48, 9]$, de sorte qu'elle ait une longueur de 3 octets. Chaque indice de notre tableau de clés est alors défini en fonction de la valeur décimale de l'élément particulier de la clé, dans l'ordre. Si vous parcourez toute la clé, recommencez au début, jusqu'à ce que vous ayez rempli les 8 emplacements du tableau de clés. Notre tableau de clés est donc le suivant :


- $K = [14, 48, 9, 14, 48, 9, 14, 48]$

### Étape 3

Troisièmement, nous transformerons le tableau **S** en utilisant le tableau de clés **K**, dans un processus connu sous le nom d' **ordonnancement des clés**. Le processus est le suivant en pseudocode :


- Créer les variables **j** et **i**
- Définir la variable $j = 0$
- Pour chaque $i$ de 0 à 7 :
    - Ensemble $j = (j + S[i] + K[i]) \mod 8$
    - Échanger $S[i]$ et $S[j]$

La transformation du tableau **S** est présentée dans le *Tableau 1*.

Pour commencer, l'état initial de **S** est $[0, 1, 2, 3, 4, 5, 6, 7]$ avec une valeur initiale de 0 pour **j**. Cet état sera transformé à l'aide du tableau de clés $[14, 48, 9, 14, 48, 9, 14, 48]$.

La boucle for commence avec $i = 0$. D'après notre pseudocode ci-dessus, la nouvelle valeur de **j** devient 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). En échangeant $S[0]$ et $S[6]$, l'état de **S** après 1 tour devient $[6, 1, 2, 3, 4, 5, 0, 7]$.

Dans la ligne suivante, $i = 1$. En repassant par la boucle for, **j** obtient la valeur 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). En échangeant $S[1]$ et $S[7]$ à partir de l'état actuel de **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, on obtient $[6, 7, 2, 3, 4, 5, 0, 1]$ après le 2e tour.

Nous continuons ce processus jusqu'à ce que nous obtenions la dernière ligne en bas du tableau **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.

*Tableau 1 : Tableau de programmation clé*

| S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |

| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |

| | | | | | | | | | | | |

| Initial | | 0 | | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

| 1 | 0 | 6 | | 6 | 1 | 2 | 3 | 4 | 5 | 0 | 7 |

| 2 | 1 | 7 | | 6 | 7 | 2 | 3 | 4 | 5 | 0 | 1 |

| 3 | 2 | 2 | | 6 | 7 | 2 | 3 | 4 | 5 | 0 | 1 |

| 4 | 3 | 3 | | 6 | 7 | 2 | 3 | 4 | 5 | 0 | 1 |

| 5 | 4 | 3 | | 6 | 7 | 2 | 0 | 3 | 5 | 4 | 1 |

| 6 | 5 | 6 | | 6 | 4 | 2 | 0 | 3 | 7 | 5 | 1 |

| 7 | 6 | 1 | | 6 | 4 | 2 | 0 | 3 | 7 | 5 | 2 |

| 8 | 7 | 2 | | 6 | 4 | 1 | 0 | 3 | 7 | 5 | 2 |

### Étape 4

La quatrième étape consiste à produire le **keystream**. Il s'agit d'une chaîne pseudo-aléatoire d'une longueur égale au message que nous voulons envoyer. Elle sera utilisée pour crypter le message original "SOUP" Comme le flux de clés doit être aussi long que le message, nous en avons besoin d'un de 4 octets.

Le flux de clés est produit par le pseudocode suivant :


- Créez les variables **j**, **i** et **t**.
- Fixer $j = 0$.
- Pour chaque $i$ du texte clair, en commençant par $i = 1$ et en continuant jusqu'à $i = 4$, chaque octet du flux de clés est produit comme suit :
    - $j = (j + S[i]) \Nmod 8$
    - Échangez $S[i]$ et $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$
    - Le $i^{th}$ byte du keystream = $S[t]$

Vous pouvez suivre les calculs dans le *Tableau 2*.

L'état initial de **S** est $S = [6, 4, 1, 0, 3, 7, 5, 2]$. En fixant $i = 1$, la valeur de **j** devient 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Nous échangeons ensuite $S[1]$ et $S[4]$ pour produire la transformation de **S** dans la deuxième ligne, $[6, 3, 1, 0, 4, 7, 5, 2]$. La valeur de **t** est alors 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Enfin, l'octet du flux de clés est $S[7]$, soit 2.

Nous continuons ensuite à produire les autres octets jusqu'à ce que nous obtenions les quatre octets suivants : 2, 6, 3 et 7. Chacun de ces octets peut alors être utilisé pour crypter chaque lettre du texte en clair, "SOUP".

Pour commencer, en utilisant une table ASCII, nous pouvons voir que "SOUP" encodé par les valeurs décimales des chaînes d'octets sous-jacentes est "83 79 85 80". La combinaison avec le flux de clés "2 6 3 7" donne "85 85 88 87", qui reste identique après une opération modulo 256. En ASCII, le texte chiffré "85 85 88 87" correspond à "UUXW".

Que se passe-t-il si le mot à crypter est plus long que le tableau **S** ? Dans ce cas, le tableau **S** continue à se transformer de la manière décrite ci-dessus pour chaque octet **i** du texte en clair, jusqu'à ce que le nombre d'octets du flux de clés soit égal au nombre de lettres du texte en clair.

*Tableau 2 : Génération Keystream*

| S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |

| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |

| | | | | | | | | | | | |

| | 0 | | | 6 | 4 | 1 | 0 | 3 | 7 | 5 | 2 |

| 1 | 4 | 7 | 2 | 6 | 3 | 1 | 0 | 4 | 7 | 5 | 2 |

| 2 | 5 | 0 | 6 | 6 | 3 | 7 | 0 | 4 | 1 | 5 | 2 |

| 3 | 5 | 1 | 3 | 6 | 3 | 7 | 1 | 4 | 0 | 5 | 2 |

| 4 | 1 | 7 | 2 | 6 | 4 | 7 | 1 | 3 | 0 | 5 | 2 |

L'exemple que nous venons de voir n'est qu'une version édulcorée du **chiffrement de flux RC4**. Le véritable chiffrement de flux RC4 comporte un tableau **S** d'une longueur de 256 octets, et non de 8 octets, et une clé qui peut être comprise entre 1 et 256 octets, et non entre 1 et 8 octets. Le tableau de clés et les flux de clés sont alors tous produits en tenant compte de la longueur de 256 octets du tableau **S**. Les calculs deviennent immensément plus complexes, mais les principes restent les mêmes. En utilisant la même clé, [14,48,9], avec le chiffrement RC4 standard, le message en clair "SOUP" est chiffré sous la forme 67 02 ed df au format hexadécimal.

Un chiffrement de flux dans lequel le flux de clés est mis à jour indépendamment du message en clair ou du texte chiffré est un **chiffrement de flux synchrone**. Le flux de clés ne dépend que de la clé. De toute évidence, RC4 est un exemple de chiffrement de flux synchrone, car le flux de clés n'a aucune relation avec le texte en clair ou le texte chiffré. Tous nos algorithmes de chiffrement primitifs mentionnés dans le chapitre précédent, y compris le chiffrement par décalage, le chiffrement de Vigenère et le tampon à usage unique, étaient également de type synchrone.

En revanche, un **chiffrement de flux asynchrone** a un flux de clés qui est produit à la fois par la clé et par les éléments précédents du texte chiffré. Ce type de chiffrement est également appelé **chiffrement auto-synchronisé**.

Il est important de noter que le flux de clés produit avec RC4 doit être traité comme un tampon à usage unique, et qu'il n'est pas possible de produire le flux de clés exactement de la même manière la fois suivante. Plutôt que de changer la clé à chaque fois, la solution pratique consiste à combiner la clé avec un **nonce** pour produire le flux de données.

## AES avec une clé de 128 bits

<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Comme mentionné dans le chapitre précédent, le National Institute of Standards and Technology (NIST) a organisé un concours entre 1997 et 2000 pour déterminer une nouvelle norme de cryptage symétrique. Le **chiffre Rijndael** a remporté le concours. Le nom est un jeu de mots sur les noms des créateurs belges, Vincent Rijmen et Joan Daemen.

Le chiffrement Rijndael est un **chiffrement par blocs**, ce qui signifie qu'il existe un algorithme de base qui peut être utilisé avec différentes spécifications pour la longueur des clés et la taille des blocs. Vous pouvez donc l'utiliser avec différents modes de fonctionnement pour construire des schémas de cryptage.

Le comité du concours du NIST a adopté une version restreinte du chiffrement de Rijndael, à savoir une version qui nécessite des blocs de 128 bits et des longueurs de clé de 128 bits, 192 bits ou 256 bits, dans le cadre de l'**Advanced Encryption Standard (AES)**. Cette version restreinte du chiffrement Rijndael peut également être utilisée dans plusieurs modes de fonctionnement. La spécification de la norme est connue sous le nom de **Advanced Encryption Standard (AES)**.

Afin de montrer comment fonctionne le chiffrement Rijndael, le cœur de l'AES, je vais illustrer le processus de chiffrement avec une clé de 128 bits. La taille de la clé a un impact sur le nombre de tours effectués pour chaque bloc de cryptage. Pour les clés de 128 bits, 10 tours sont nécessaires. Avec des clés de 192 bits et 256 bits, il aurait fallu 12 et 14 tours, respectivement.

En outre, je supposerai que l'AES est utilisé en mode **ECB**. Cela facilite légèrement l'exposé et n'a pas d'importance pour l'algorithme Rijndael. Il est certain que le mode ECB n'est pas sûr dans la pratique, car il conduit à un chiffrement déterministe. Le mode sécurisé le plus couramment utilisé avec AES est **CBC** (Cipher Block Chaining).

Appelons la clé $K_0$. La construction avec les paramètres ci-dessus se présente donc comme dans la *Figure 1*, où $M_i$ représente une partie du message en clair de 128 bits et $C_i$ une partie du texte chiffré de 128 bits. Un tampon est ajouté au texte en clair pour le dernier bloc, si le texte en clair ne peut pas être divisé uniformément par la taille du bloc.

*Figure 1 : AES-ECB avec une clé de 128 bits*

![Figure 1: AES-ECB with a 128-bit key](assets/Figure5-1.webp "Figure 1: AES-ECB with a 128-bit key")

Chaque bloc de texte de 128 bits passe par dix tours dans le schéma de cryptage Rijndael. Cela nécessite une clé distincte pour chaque tour ($K_1$ à $K_{10}$). Ces clés sont produites à chaque tour à partir de la clé originale de 128 bits $K_0$ à l'aide d'un **algorithme d'expansion de clé**. Par conséquent, pour chaque bloc de texte à chiffrer, nous utiliserons la clé originale $K_0$ ainsi que dix clés distinctes. Notez que ces mêmes 11 clés sont utilisées pour chaque bloc de 128 bits de texte en clair qui doit être crypté.

L'algorithme d'expansion des clés est long et complexe. Le parcourir n'a que peu d'intérêt didactique. Vous pouvez consulter l'algorithme d'expansion de clé par vous-même, si vous le souhaitez. Une fois les clés rondes produites, le chiffrement Rijndael manipule le premier bloc de 128 bits de texte en clair, $M_1$, comme le montre la *Figure 2*. Nous allons maintenant suivre ces étapes.

*Figure 2 : La manipulation de $M_1$ avec le chiffrement Rijndael:*

**Round 0:**


- XOR $M_1$ et $K_0$ pour produire $S_0$

---
**Ronde n pour n = {1,...,9}:**


- XOR $S_{n-1}$ et $K_n$
- Substitution d'octets
- Rangs de décalage
- Mélanger les colonnes
- XOR $S$ et $K_n$ pour produire $S_n$

---
**Round 10:**


- XOR $S_9$ et $K_{10}$
- Substitution d'octets
- Rangs de décalage
- XOR $S$ et $K_{10}$ pour produire $S_{10}$
- $S_{10}$ = $C_1$

### Tour 0

Le tour 0 du chiffrement Rijndael est simple. Un tableau $S_0$ est produit par une opération XOR entre le texte clair de 128 bits et la clé privée. C'est-à-dire,


- $S_0 = M_1 \oplus K_0$

### Premier tour

Lors du premier tour, le tableau $S_0$ est d'abord combiné avec la clé du tour $K_1$ à l'aide d'une opération XOR. Cela produit un nouvel état de $S$.

Deuxièmement, l'opération de **substitution d'octets** est effectuée sur l'état actuel de $S$. Elle consiste à prendre chaque octet du tableau de 16 octets de $S$ et à le remplacer par un octet d'un tableau appelé **Boîte en S de Rijndael**. Chaque octet a une transformation unique, et un nouvel état de $S$ est produit comme résultat. La boîte S de Rijndael est représentée à la *Figure 3*.

*Figure 3 : S-Box* de Rijndael

| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 0A | 0B | 0C | 0D | 0E | 0F |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 00 | 63 | 7C | 77 | 7B | F2 | 6B | 6F | C5 | 30 | 01 | 67 | 2B | FE | D7 | AB | 76 |

| 10 | CA | 82 | C9 | 7D | FA | 59 | 47 | F0 | AD | D4 | A2 | AF | 9C | A4 | 72 | C0 |

| 20 | B7 | FD | 93 | 26 | 36 | 3F | F7 | CC | 34 | A5 | E5 | F1 | 71 | D8 | 31 | 15 |

| 30 | 04 | C7 | 23 | C3 | 18 | 96 | 05 | 9A | 07 | 12 | 80 | E2 | EB | 27 | B2 | 75 |

| 40 | 09 | 83 | 2C | 1A | 1B | 6E | 5A | A0 | 52 | 3B | D6 | B3 | 29 | E3 | 2F | 84 |

| 50 | 53 | D1 | 00 | ED | 20 | FC | B1 | 5B | 6A | CB | BE | 39 | 4A | 4C | 58 | CF |

| 60 | D0 | EF | AA | FB | 43 | 4D | 33 | 85 | 45 | F9 | 02 | 7F | 50 | 3C | 9F | A8 |

| 70 | 51 | A3 | 40 | 8F | 92 | 9D | 38 | F5 | BC | B6 | DA | 21 | 10 | FF | F3 | D2 |

| 80 | CD | 0C | 13 | EC | 5F | 97 | 44 | 17 | C4 | A7 | 7E | 3D | 64 | 5D | 19 | 73 |

| 90 | 60 | 81 | 4F | DC | 22 | 2A | 90 | 88 | 46 | EE | B8 | 14 | DE | 5E | 0B | DB | |

| A0 | E0 | 32 | 3A | 0A | 49 | 06 | 24 | 5C | C2 | D3 | AC | 62 | 91 | 95 | E4 | 79 |

| B0 | E7 | C8 | 37 | 6D | 8D | D5 | 4E | A9 | 6C | 56 | F4 | EA | 65 | 7A | AE | 08 | |

| C0 | BA | 78 | 25 | 2E | 1C | A6 | B4 | C6 | E8 | DD | 74 | 1F | 4B | BD | 8B | 8A | |

| D0 | 70 | 3E | B5 | 66 | 48 | 03 | F6 | 0E | 61 | 35 | 57 | B9 | 86 | C1 | 1D | 9E | |

| E0 | E1 | F8 | 98 | 11 | 69 | D9 | 8E | 94 | 9B | 1E | 87 | E9 | CE | 55 | 28 | DF |

| F0 | 8C | A1 | 89 | 0D | BF | E6 | 42 | 68 | 41 | 99 | 2D | 0F | B0 | 54 | BB | 16 |

Cette boîte S est l'un des endroits où l'algèbre abstraite entre en jeu dans le chiffrement Rijndael, en particulier les **champs de Galois**.

Pour commencer, vous définissez chaque élément d'octet possible de 00 à FF comme un vecteur de 8 bits. Chacun de ces vecteurs est un élément du **champ de Galois GF(2^8)** où le polynôme irréductible pour l'opération modulo est $x^8 + x^4 + x^3 + x + 1$. Le corps de Galois avec ces spécifications est également appelé **champ fini de Rijndael**.

Ensuite, pour chaque élément possible du champ, nous créons ce que l'on appelle la **boîte S de Nyberg**. Dans cette boîte, chaque octet est mis en correspondance avec son **inverse multiplicatif** (c'est-à-dire que leur produit est égal à 1). Nous faisons ensuite correspondre ces valeurs de la boîte S de Nyberg à la boîte S de Rijndael à l'aide de la **transformation d'affine**.

La troisième opération sur le tableau **S** est l'opération **shift rows**. Elle prend l'état de **S** et liste les seize octets dans une matrice. Le remplissage de la matrice commence en haut à gauche et se fait de haut en bas, puis, à chaque fois qu'une colonne est remplie, elle se décale d'une colonne vers la droite et vers le haut.

Une fois la matrice **S** construite, les quatre lignes sont décalées. La première ligne reste inchangée. La deuxième ligne se déplace d'une unité vers la gauche. La troisième déplace deux lignes vers la gauche. La quatrième déplace trois lignes vers la gauche. Un exemple de ce processus est donné à la *figure 4*. L'état d'origine de **S** est indiqué en haut, et l'état résultant après l'opération de décalage des rangées est indiqué en dessous.

*Figure 4 : Opération de décalage des lignes*

| F1 | A0 | B1 | 23 |

|------|------|------|------|

| 59 | EF | 09 | 82 |

| 97 | 01 | B0 | CC |

| D4 | 72 | 04 | 21 |

| F1 | A0 | B1 | 23 |

|------|------|------|------|

| EF | 09 | 82 | 59 |

| B0 | CC | 97 | 01 |

| 21 | D4 | 72 | 04 |

Dans la quatrième étape, les **champs de Galois** refont leur apparition. Pour commencer, chaque colonne de la matrice **S** est multipliée par la colonne de la matrice 4 x 4 vue dans la *Figure 5*. Mais au lieu d'une multiplication matricielle normale, il s'agit d'une multiplication vectorielle **modulo un polynôme irréductible**, $x^8 + x^4 + x^3 + x + 1$. Les coefficients vectoriels résultants représentent les bits individuels d'un octet.

*Figure 5 : Matrice des colonnes de mélange*

| 02 | 03 | 01 | 01 |

|------|------|------|------|

| 01 | 02 | 03 | 01 |

| 01 | 01 | 02 | 03 |

| 03 | 01 | 01 | 02 |

La multiplication de la première colonne de la matrice **S** par la matrice 4 x 4 ci-dessus donne le résultat de la *figure 6*.

*Figure 6 : Multiplication de la première colonne:*

$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$

L'étape suivante consiste à transformer tous les termes de la matrice en polynômes. Par exemple, F1 représente 1 octet et devient $x^7 + x^6 + x^5 + x^4 + 1$, et 03 représente 1 octet et devient $x + 1$.

Toutes les multiplications sont alors effectuées **modulo** $x^8 + x^4 + x^3 + x + 1$. Il en résulte l'addition de quatre polynômes dans chacune des quatre cellules de la colonne. Après avoir effectué ces additions **modulo 2**, vous obtiendrez quatre polynômes. Chacun de ces polynômes représente une chaîne de 8 bits, ou 1 octet, de **S**. Nous n'effectuerons pas tous ces calculs ici sur la matrice de la *Figure 6*, car ils sont volumineux.

Une fois la première colonne traitée, les trois autres colonnes de la matrice **S** sont traitées de la même manière. Au final, on obtient une matrice de seize octets qui peut être transformée en tableau.

Dans une dernière étape, le tableau **S** est à nouveau combiné avec la clé circulaire dans une opération **XOR**. Cela produit l'état $S_1$. C'est-à-dire,


- s_1 = S \oplus K_0$

### Séries 2 à 10

Les tours 2 à 9 ne sont qu'une répétition du tour 1, *mutatis mutandis*. Le dernier tour ressemble beaucoup aux tours précédents, sauf que l'étape **mélanger les colonnes** est éliminée. En d'autres termes, le tour 10 est exécuté comme suit :


- s_9 \oplus K_{10}$
- Substitution d'octets
- Rangs de décalage
- s_{10} = S \oplus K_{10}$

L'état $S_{10}$ est maintenant $C_1$, les 128 premiers bits du texte chiffré. En parcourant les autres blocs de texte en clair de 128 bits, on obtient le texte chiffré complet **C**.

### Les opérations du cryptogramme Rijndael

Quel est le raisonnement qui sous-tend les différentes opérations du cryptogramme Rijndael ?

Sans entrer dans les détails, les systèmes de cryptage sont évalués en fonction de leur degré de confusion et de diffusion. Si le système de cryptage présente un degré élevé de **confusion**, cela signifie que le texte crypté est radicalement différent du texte en clair. Si le système de cryptage a un degré élevé de **diffusion**, cela signifie que toute petite modification du texte en clair produit un texte crypté radicalement différent.

Le raisonnement qui sous-tend les opérations du cryptogramme Rijndael est qu'elles produisent à la fois un degré élevé de confusion et de diffusion. La confusion est produite par l'opération de substitution d'octets, tandis que la diffusion est produite par les opérations de décalage des lignes et de mélange des colonnes.

# Cryptographie asymétrique

<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

## Le problème de la distribution et de la gestion des clés

<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Comme pour la cryptographie symétrique, les systèmes asymétriques peuvent être utilisés pour garantir à la fois le secret et l'authentification. En revanche, ces systèmes utilisent deux clés au lieu d'une : une clé privée et une clé publique.

Nous commençons notre enquête par la découverte de la cryptographie asymétrique, en particulier les problèmes qui l'ont stimulée. Nous examinerons ensuite le fonctionnement de haut niveau des systèmes asymétriques de cryptage et d'authentification. Nous présentons ensuite les fonctions de hachage, qui sont essentielles pour comprendre les systèmes d'authentification asymétriques et qui sont également pertinentes dans d'autres contextes cryptographiques, tels que les codes d'authentification des messages basés sur le hachage que nous avons examinés au chapitre 4.

___

Supposons que Bob veuille acheter un nouvel imperméable à Jim's Sporting Goods, un détaillant d'articles de sport en ligne qui compte des millions de clients en Amérique du Nord. Il s'agit de son premier achat et il souhaite utiliser sa carte de crédit. Bob devra donc d'abord créer un compte auprès de Jim's Sporting Goods, ce qui nécessite l'envoi de données personnelles telles que son adresse et les informations relatives à sa carte de crédit. Il pourra ensuite suivre les étapes nécessaires à l'achat de l'imperméable.

Bob et Jim's Sporting Goods voudront s'assurer que leurs communications sont sécurisées tout au long de ce processus, étant donné que l'internet est un système de communication ouvert. Ils voudront s'assurer, par exemple, qu'aucun attaquant potentiel ne puisse connaître les détails de la carte de crédit et de l'adresse de Bob, et qu'aucun attaquant potentiel ne puisse répéter ses achats ou en créer de faux en son nom.

Un système de cryptage authentifié avancé, tel que celui présenté dans le chapitre précédent, pourrait certainement sécuriser les communications entre Bob et Jim's Sporting Goods. Mais la mise en œuvre d'un tel système se heurte à des obstacles pratiques évidents.

Pour illustrer ces obstacles pratiques, supposons que nous vivions dans un monde où seuls les outils de la cryptographie symétrique existent. Que pourraient alors faire Jim's Sporting Goods et Bob pour assurer une communication sécurisée ?

Dans ces conditions, ils devraient faire face à des coûts substantiels pour communiquer en toute sécurité. L'internet étant un système de communication ouvert, ils ne peuvent pas simplement y échanger un ensemble de clés. Bob et un représentant de Jim's Sporting Goods devront donc procéder à un échange de clés en personne.

Une possibilité est que Jim's Sporting Goods crée des lieux spéciaux d'échange de clés, où Bob et d'autres nouveaux clients peuvent récupérer un jeu de clés pour une communication sécurisée. Cela entraînerait évidemment des coûts d'organisation considérables et réduirait considérablement l'efficacité avec laquelle les nouveaux clients peuvent effectuer leurs achats.

Par ailleurs, Jim's Sporting Goods peut envoyer à Bob une paire de clés par l'intermédiaire d'un coursier de confiance. Cette solution est probablement plus efficace que l'organisation de lieux d'échange de clés. Toutefois, cette solution entraînerait des coûts substantiels, en particulier si de nombreux clients n'effectuent qu'un seul ou quelques achats.

Ensuite, un système symétrique de cryptage authentifié oblige Jim's Sporting Goods à stocker des jeux de clés distincts pour tous ses clients. Il s'agit là d'un défi pratique important pour des milliers de clients, sans parler des millions.

Pour comprendre ce dernier point, supposons que Jim's Sporting Goods fournisse à chaque client la même paire de clés. Cela permettrait à chaque client - ou à toute autre personne pouvant obtenir cette paire de clés - de lire et même de manipuler toutes les communications entre Jim's Sporting Goods et ses clients. Dans ces conditions, vous pourriez tout aussi bien ne pas utiliser de cryptographie dans vos communications.

Même le fait de répéter un jeu de clés pour certains clients seulement est une pratique très mauvaise pour la sécurité. Tout attaquant potentiel pourrait tenter d'exploiter cette caractéristique du système (n'oubliez pas que les attaquants sont censés tout savoir sur un système, sauf les clés, conformément au principe de Kerckhoffs)

Ainsi, Jim's Sporting Goods devrait stocker une paire de clés pour chaque client, quelle que soit la manière dont ces paires de clés sont distribuées. Cette situation pose manifestement plusieurs problèmes pratiques.


- Jim's Sporting Goods devrait stocker des millions de paires de clés, un jeu pour chaque client.
- Ces clés devraient être correctement sécurisées, car elles constitueraient une cible infaillible pour les pirates informatiques. Toute violation de la sécurité nécessiterait la répétition d'échanges de clés coûteux, soit dans des lieux spéciaux d'échange de clés, soit par courrier.
- Tout client de Jim's Sporting Goods doit conserver une paire de clés en toute sécurité chez lui. Des pertes et des vols se produiront, ce qui nécessitera de répéter les échanges de clés. Les clients devront également suivre ce processus pour tout autre magasin en ligne ou tout autre type d'entité avec laquelle ils souhaitent communiquer et effectuer des transactions sur l'internet.

Les deux principaux défis que nous venons de décrire étaient des préoccupations fondamentales jusqu'à la fin des années 1970. Ils étaient connus sous le nom de **problème de distribution des clés** et **problème de gestion des clés**, respectivement.

Ces problèmes ont toujours existé, bien sûr, et ont souvent créé des maux de tête dans le passé. Les forces armées, par exemple, devaient constamment distribuer au personnel sur le terrain des livres contenant les clés permettant une communication sécurisée, ce qui présentait des risques et des coûts importants. Mais ces problèmes s'aggravaient à mesure que le monde évoluait vers une communication numérique à longue distance, en particulier pour les entités non gouvernementales.

Si ces problèmes n'avaient pas été résolus dans les années 1970, les achats efficaces et sécurisés chez Jim's Sporting Goods n'auraient probablement jamais existé. En fait, la plus grande partie de notre monde moderne, avec l'envoi de courriels pratiques et sécurisés, les services bancaires en ligne et les achats, ne serait probablement qu'un lointain fantasme. Tout ce qui ressemble de près ou de loin au bitcoin n'aurait peut-être jamais existé.

Que s'est-il donc passé dans les années 1970 ? Comment est-il possible de faire instantanément des achats en ligne et de naviguer en toute sécurité sur le web ? Comment est-il possible d'envoyer instantanément des bitcoins dans le monde entier à partir de nos téléphones intelligents ?

## Nouvelles orientations de la cryptographie

<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

Dans les années 1970, les problèmes de distribution et de gestion des clés ont attiré l'attention d'un groupe de cryptographes universitaires américains : Whitfield Diffie, Martin Hellman et Ralph Merkle. Face au scepticisme de la majorité de leurs pairs, ils se sont aventurés à trouver une solution.

Au moins l'une des principales motivations de leur entreprise était la prévision que les communications informatiques ouvertes allaient profondément affecter notre monde. Comme le notent Diffie et Helmann en 1976,

> Le développement de réseaux de communication contrôlés par ordinateur promet des contacts sans effort et peu coûteux entre des personnes ou des ordinateurs situés de part et d'autre du monde, remplaçant la plupart des courriers et de nombreuses excursions par des télécommunications. Pour de nombreuses applications, ces contacts doivent être sécurisés à la fois contre l'écoute et l'injection de messages illégitimes. Or, à l'heure actuelle, la résolution des problèmes de sécurité est très en retard par rapport à d'autres domaines de la technologie des communications. *La cryptographie contemporaine n'est pas en mesure de répondre aux exigences, en ce sens que son utilisation imposerait aux utilisateurs du système des inconvénients si graves qu'elle éliminerait une grande partie des avantages du télétraitement*
La ténacité de Diffie, Hellman et Merkle a porté ses fruits. La première publication de leurs résultats a été un article de Diffie et Helmann en 1976 intitulé "New Directions in Cryptography" Ils y présentent deux façons originales de résoudre les problèmes de distribution et de gestion des clés.

La première solution qu'ils ont proposée était un *protocole d'échange de clés* à distance, c'est-à-dire un ensemble de règles pour l'échange d'une ou de plusieurs clés symétriques sur un canal de communication non sécurisé. Ce protocole est aujourd'hui connu sous le nom d'échange de clés *Diffie-Helmann* ou d'échange de clés *Diffie-Helmann-Merkle*. [2]

Avec l'échange de clés Diffie-Helmann, deux parties échangent d'abord certaines informations publiquement sur un canal non sécurisé tel que l'internet. Sur la base de ces informations, elles créent ensuite indépendamment une clé symétrique (ou une paire de clés symétriques) pour une communication sécurisée. Bien que les deux parties créent leurs clés indépendamment, les informations qu'elles ont partagées publiquement garantissent que ce processus de création de clés aboutit au même résultat pour chacune d'entre elles.

Il est important de noter que si tout le monde peut observer les informations échangées publiquement par les parties sur le canal non sécurisé, seules les deux parties participant à l'échange d'informations peuvent créer des clés symétriques à partir de ces informations.

Bien entendu, cela semble totalement contre-intuitif. Comment deux parties pourraient-elles échanger publiquement des informations qui leur permettraient à elles seules de créer des clés symétriques à partir de ces informations ? Pourquoi toute autre personne observant l'échange d'informations ne serait-elle pas en mesure de créer les mêmes clés ?

Il s'appuie bien sûr sur de belles mathématiques. L'échange de clés Diffie-Helmann fonctionne via une fonction à sens unique avec une trappe. Examinons successivement la signification de ces deux termes.

Supposons que l'on vous donne une fonction $f(x)$ et le résultat $f(a) = y$, où $a$ est une valeur particulière de $x$. On dit que $f(x)$ est une **fonction à sens unique** s'il est facile de calculer la valeur $y$ lorsqu'on dispose de $a$ et de $f(x)$, mais qu'il est impossible de calculer la valeur $a$ lorsqu'on dispose de $y$ et de $f(x)$. Le nom **fonction à sens unique** vient bien sûr du fait qu'une telle fonction ne peut être calculée que dans un seul sens.

Certaines fonctions à sens unique possèdent ce que l'on appelle une **trapdoor**. Bien qu'il soit pratiquement impossible de calculer $a$ à partir de $y$ et $f(x)$, il existe un certain élément d'information $Z$ qui permet de calculer $a$ à partir de $y$. Cette information $Z$ est connue sous le nom de **trapdoor**. Les fonctions à sens unique qui possèdent une trappe sont appelées **fonctions à trappe**.

Nous n'entrerons pas ici dans les détails de l'échange de clés Diffie-Helmann. Mais en gros, chaque participant crée des informations, dont une partie est partagée publiquement et une autre reste secrète. Chaque partie prend ensuite son information secrète et l'information publique partagée par l'autre partie pour créer une clé privée. Et comme par miracle, les deux parties se retrouvent avec la même clé privée.

Toute partie observant uniquement les informations partagées publiquement entre les deux parties dans un échange de clés Diffie Helmann n'est pas en mesure de reproduire ces calculs. Elle aurait besoin des informations privées de l'une des deux parties pour le faire.

Bien que la version de base de l'échange de clés Diffie-Helmann présentée dans l'article de 1976 ne soit pas très sûre, des versions sophistiquées du protocole de base sont certainement encore utilisées aujourd'hui. Plus important encore, chaque protocole d'échange de clés dans la dernière version du protocole de sécurité de la couche transport (version 1.3) est essentiellement une version enrichie du protocole présenté par Diffie et Hellman en 1976. Le protocole de sécurité de la couche transport est le protocole prédominant pour l'échange sécurisé d'informations formatées selon le protocole de transfert hypertexte (http), la norme pour l'échange de contenu Web.

Il est important de noter que l'échange de clés Diffie-Helmann n'est pas un système asymétrique. Au sens strict, il appartient sans doute au domaine de la cryptographie à clé symétrique. Mais comme l'échange de clés de Diffie-Helmann et la cryptographie asymétrique reposent tous deux sur des fonctions de la théorie des nombres à sens unique avec des trappes, ils sont généralement abordés ensemble.

Le deuxième moyen proposé par Diffie et Helmann pour résoudre le problème de la distribution et de la gestion des clés dans leur article de 1976 était, bien entendu, la cryptographie asymétrique.

Contrairement à leur présentation de l'échange de clés Diffie-Hellman, ils n'ont fourni que les grandes lignes de la manière dont les systèmes cryptographiques asymétriques pourraient être construits de manière plausible. Ils n'ont proposé aucune fonction à sens unique susceptible de remplir les conditions nécessaires à une sécurité raisonnable dans ces schémas.

Une mise en œuvre pratique d'un système asymétrique a toutefois été trouvée un an plus tard par trois cryptographes et mathématiciens universitaires différents, Ronald Rivest, Shamir et Leonard Adleman : Ronald Rivest, Adi Shamir et Leonard Adleman[3]. [Le système de cryptage qu'ils ont introduit a été connu sous le nom de **système de cryptage RSA** (d'après leurs noms de famille).

Les fonctions de trappe utilisées dans la cryptographie asymétrique (et l'échange de clés Diffie Helmann) sont toutes liées à deux problèmes principaux **difficiles à calculer** : la factorisation des nombres premiers et le calcul des logarithmes discrets.

**La factorisation des nombres premiers** consiste, comme son nom l'indique, à décomposer un nombre entier en ses facteurs premiers. Le problème RSA est de loin l'exemple le plus connu de cryptosystème lié à la factorisation des nombres premiers.

Le **problème du logarithme discret** est un problème qui se pose dans les groupes cycliques. Etant donné un générateur dans un groupe cyclique particulier, il requiert le calcul de l'exposant unique nécessaire pour produire un autre élément du groupe à partir du générateur.

Les systèmes basés sur le logarithme discret reposent sur deux types principaux de groupes cycliques : les groupes multiplicatifs d'entiers et les groupes qui incluent les points des courbes elliptiques. L'échange de clés Diffie Helmann original, tel que présenté dans "New Directions in Cryptography", fonctionne avec un groupe multiplicatif cyclique d'entiers. L'algorithme de signature numérique de Bitcoin et le système de signature Schnorr récemment introduit (2021) sont tous deux basés sur le problème du logarithme discret pour un groupe cyclique de courbes elliptiques particulier.

Nous passerons ensuite à une vue d'ensemble du secret et de l'authentification dans le cadre asymétrique. Avant cela, il convient toutefois de faire un bref rappel historique.

Il semble aujourd'hui plausible qu'un groupe de cryptographes et de mathématiciens britanniques travaillant pour le Government Communications Headquarters (GCHQ) ait fait indépendamment les découvertes mentionnées ci-dessus quelques années auparavant. Ce groupe était composé de James Ellis, Clifford Cocks et Malcolm Williamson.

Selon leurs propres dires et ceux du GCHQ, c'est James Ellis qui a conçu le premier le concept de cryptographie à clé publique en 1969. Clifford Cocks aurait ensuite découvert le système cryptographique RSA en 1973, et Malcolm Williamson le concept d'échange de clés Diffie Helmann en 1974[4]. [Leurs découvertes n'auraient toutefois été révélées qu'en 1997, compte tenu de la nature secrète des travaux effectués au GCHQ.

**Notes:**

[1] Whitfield Diffie et Martin Hellman, "New directions in cryptography", _IEEE Transactions on Information Theory_ IT-22 (1976), pp. 644-654, p. 644.

[2] Ralph Merkle discute également d'un protocole d'échange de clés dans "Secure communications over insecure channels", _Communications of the Association for Computing Machinery_, 21 (1978), 294-99. Bien que Merkle ait soumis cet article avant celui de Diffie et Hellman, il a été publié plus tard. La solution de Merkle n'est pas exponentiellement sûre, contrairement à celle de Diffie-Hellman.

[3] Ron Rivest, Adi Shamir et Leonard Adleman, "A method for obtaining digital signatures and public-key cryptosystems", _Communications of the Association for Computing Machinery_, 21 (1978), pp. 120-26.

[4] Simon Singh, _The Code Book_, Fourth Estate (Londres, 1999), chapitre 6, présente un bon historique de ces découvertes.

## Cryptage et authentification asymétriques

<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

La *Figure 1* donne un aperçu du **chiffrement asymétrique** à l'aide de Bob et Alice.

Alice crée d'abord une paire de clés, composée d'une clé publique ($K_P$) et d'une clé privée ($K_S$), où le "P" de $K_P$ signifie "public" et le "S" de $K_S$ signifie "secret". Elle distribue ensuite librement cette clé publique à d'autres personnes. Nous reviendrons un peu plus tard sur les détails de ce processus de distribution. Mais pour l'instant, supposons que n'importe qui, y compris Bob, puisse obtenir en toute sécurité la clé publique d'Alice $K_P$.

À un moment donné, Bob souhaite écrire un message $M$ à Alice. Comme ce message contient des informations sensibles, il souhaite que son contenu reste secret pour tout le monde sauf pour Alice. Bob commence donc par chiffrer son message $M$ à l'aide de $K_P$. Il envoie ensuite le texte chiffré résultant $C$ à Alice, qui déchiffre $C$ avec $K_S$ pour produire le message original $M$.

*Figure 1 : Chiffrement asymétrique*

![Figure 1: Asymmetric encryption](assets/Figure6-1.webp "Figure 1: Asymmetric encryption")

Tout adversaire qui écoute les communications de Bob et Alice peut observer $C$. Il connaît également $K_P$ et l'algorithme de chiffrement $E(\cdot)$. Il est important de noter que ces informations ne permettent pas à l'attaquant de décrypter le texte chiffré $C$. Le décryptage nécessite spécifiquement $K_S$, que l'attaquant ne possède pas.

Les systèmes de chiffrement symétrique doivent généralement être sécurisés contre un attaquant qui peut chiffrer valablement les messages en clair (ce que l'on appelle la sécurité de l'attaque par texte chiffré choisi). Ils ne sont toutefois pas conçus dans le but explicite de permettre la création de tels cryptogrammes valides par un attaquant ou toute autre personne.

Le contraste est saisissant avec un système de chiffrement asymétrique, dont l'objectif est de permettre à n'importe qui, y compris aux attaquants, de produire des textes chiffrés valides. Les systèmes de chiffrement asymétrique peuvent donc être qualifiés de **chiffres à accès multiples**.

Pour mieux comprendre ce qui se passe, imaginons qu'au lieu d'envoyer un message électronique, Bob veuille envoyer une lettre physique en secret. Pour garantir le secret, Alice pourrait envoyer un cadenas sécurisé à Bob, tout en conservant la clé permettant de le déverrouiller. Après avoir écrit sa lettre, Bob pourrait la mettre dans une boîte et la fermer avec le cadenas d'Alice. Il pourrait ensuite envoyer la boîte verrouillée avec le message à Alice, qui possède la clé pour la déverrouiller.

Si Bob peut verrouiller le cadenas, ni lui ni aucune autre personne interceptant la boîte ne peut défaire le cadenas s'il est effectivement sécurisé. Seule Alice peut le déverrouiller et voir le contenu de la lettre de Bob, car elle possède la clé.

Un système de cryptage asymétrique est, grosso modo, une version numérique de ce processus. Le cadenas s'apparente à la clé publique et la clé du cadenas à la clé privée. Toutefois, comme le cadenas est numérique, il est beaucoup plus facile et moins coûteux pour Alice de le distribuer à toute personne susceptible de vouloir lui envoyer des messages secrets.

Pour l'authentification dans le cadre asymétrique, nous utilisons des **signatures numériques**. Celles-ci ont donc la même fonction que les codes d'authentification des messages dans le cadre symétrique. La *figure 2* donne un aperçu des signatures numériques.

Bob crée d'abord une paire de clés, composée de la clé publique ($K_P$) et de la clé privée ($K_S$), et distribue sa clé publique. Lorsqu'il veut envoyer un message authentifié à Alice, il prend d'abord son message $M$ et sa clé privée pour créer une **signature numérique** $D$. Bob envoie ensuite à Alice son message accompagné de la signature numérique.

Alice insère le message, la clé publique et la signature numérique dans un **algorithme de vérification**. Cet algorithme produit soit **vrai** pour une signature valide, soit **faux** pour une signature non valide.

Une signature numérique est, comme son nom l'indique clairement, l'équivalent numérique d'une signature écrite sur des lettres, des contrats, etc. En fait, une signature numérique est généralement beaucoup plus sûre. Avec un peu d'effort, il est possible de falsifier une signature écrite, ce qui est d'autant plus facile que les signatures écrites ne sont souvent pas vérifiées de près. Une signature numérique sécurisée, cependant, est, tout comme un code d'authentification de message sécurisé, **existentiellement infalsifiable** : c'est-à-dire qu'avec un système de signature numérique sécurisé, personne ne peut créer une signature pour un message qui passe la procédure de vérification, à moins qu'il ne possède la clé privée.

*Figure 2 : Authentification asymétrique*

![Figure 2: Asymmetric authentication](assets/Figure6-2.webp "Figure 2: Asymmetric authentication")

Comme pour le chiffrement asymétrique, nous constatons un contraste intéressant entre les signatures numériques et les codes d'authentification des messages. Pour ces derniers, l'algorithme de vérification ne peut être utilisé que par l'une des parties ayant connaissance de la communication sécurisée. En effet, il nécessite une clé privée. Dans le cadre asymétrique, cependant, n'importe qui peut vérifier une signature numérique $S$ apposée par Bob.

Tout cela fait des signatures numériques un outil extrêmement puissant. Elles constituent la base, par exemple, de la création de signatures de contrats qui peuvent être vérifiées à des fins juridiques. Si Bob a apposé une signature sur un contrat dans l'échange ci-dessus, Alice peut montrer le message $M$, le contrat et la signature $S$ à un tribunal. Le tribunal peut alors vérifier la signature à l'aide de la clé publique de Bob. [5]

Autre exemple, les signatures numériques sont un aspect important de la distribution sécurisée des logiciels et de leurs mises à jour. Ce type de vérifiabilité publique ne pourrait jamais être créé en utilisant uniquement des codes d'authentification des messages.

Pour illustrer une dernière fois la puissance des signatures numériques, prenons le cas du bitcoin. L'une des idées fausses les plus répandues à propos de Bitcoin, en particulier dans les médias, est que les transactions sont cryptées : ce n'est pas le cas. Au contraire, les transactions Bitcoin utilisent des signatures numériques pour garantir la sécurité.

Les bitcoins existent en lots appelés sorties de transaction non dépensées (ou **UTXO**). Supposons que vous receviez trois paiements sur une adresse bitcoin particulière pour 2 bitcoins chacun. Techniquement, vous ne possédez pas 6 bitcoins sur cette adresse. Au lieu de cela, vous avez trois lots de 2 bitcoins qui sont bloqués par un problème cryptographique associé à cette adresse. Pour tout paiement que vous effectuez, vous pouvez utiliser un, deux ou les trois lots, selon le montant dont vous avez besoin pour la transaction.

La preuve de la propriété des résultats de transaction non dépensés est généralement apportée par une ou plusieurs signatures numériques. Bitcoin fonctionne précisément parce que les signatures numériques valides sur les résultats de transactions non dépensées sont infaisables sur le plan informatique, à moins que vous ne soyez en possession des informations secrètes nécessaires pour les réaliser.

Actuellement, les transactions en bitcoins incluent de manière transparente toutes les informations qui doivent être vérifiées par les participants au réseau, telles que l'origine des résultats non dépensés utilisés dans la transaction. Bien qu'il soit possible de cacher certaines de ces informations tout en permettant une vérification (comme le font certaines crypto-monnaies alternatives telles que Monero), cela crée également des risques de sécurité particuliers.

Les signatures numériques et les signatures écrites capturées numériquement prêtent parfois à confusion. Dans ce dernier cas, vous capturez une image de votre signature écrite et la collez sur un document électronique tel qu'un contrat de travail. Il ne s'agit toutefois pas d'une signature numérique au sens cryptographique du terme. Cette dernière n'est qu'un long numéro qui ne peut être produit que si l'on est en possession d'une clé privée.

Tout comme pour le paramètre de clé symétrique, vous pouvez également utiliser des schémas de chiffrement et d'authentification asymétriques ensemble. Les mêmes principes s'appliquent. Tout d'abord, vous devez utiliser des paires de clés privées et publiques différentes pour le chiffrement et les signatures numériques. En outre, vous devez d'abord chiffrer un message, puis l'authentifier.

Il est important de noter que dans de nombreuses applications, la cryptographie asymétrique n'est pas utilisée tout au long du processus de communication. Au lieu de cela, elle n'est généralement utilisée que pour *échanger des clés symétriques* entre les parties par lesquelles elles communiqueront effectivement.

C'est le cas, par exemple, lorsque vous achetez des biens en ligne. Connaissant la clé publique du vendeur, celui-ci peut vous envoyer des messages signés numériquement dont vous pouvez vérifier l'authenticité. Sur cette base, vous pouvez suivre l'un des nombreux protocoles d'échange de clés symétriques pour communiquer en toute sécurité.

La principale raison de la fréquence de l'approche susmentionnée est que la cryptographie asymétrique est beaucoup moins efficace que la cryptographie symétrique pour produire un niveau de sécurité particulier. C'est l'une des raisons pour lesquelles nous avons encore besoin de la cryptographie à clé symétrique à côté de la cryptographie publique. En outre, la cryptographie à clé symétrique est beaucoup plus naturelle dans des applications particulières telles que le cryptage par un utilisateur d'ordinateur de ses propres données.

Comment les signatures numériques et le chiffrement à clé publique résolvent-ils exactement les problèmes de distribution et de gestion des clés ?

Il n'y a pas de réponse unique. La cryptographie asymétrique est un outil et il n'y a pas qu'une seule façon de l'utiliser. Mais reprenons l'exemple précédent de Jim's Sporting Goods pour montrer comment les problèmes seraient typiquement abordés dans cet exemple.

Pour commencer, Jim's Sporting Goods s'adressera probablement à une **autorité de certification**, une organisation qui prend en charge la distribution des clés publiques. L'autorité de certification enregistrera certains détails concernant Jim's Sporting Goods et lui attribuera une clé publique. Elle enverrait ensuite à Jim's Sporting Goods un certificat, connu sous le nom de **certificat TLS/SSL**, avec la clé publique de Jim's Sporting Goods signée numériquement à l'aide de la propre clé publique de l'autorité de certification. De cette manière, l'autorité de certification affirme qu'une clé publique particulière appartient effectivement à Jim's Sporting Goods.

La clé pour comprendre ce processus avec les certificats TLS/SSL est que, bien que la clé publique de Jim's Sporting Goods ne soit généralement stockée nulle part sur votre ordinateur, les clés publiques des autorités de certification reconnues sont en effet stockées dans votre navigateur ou dans votre système d'exploitation. Elles sont stockées dans ce que l'on appelle les **certificats racine**.

Par conséquent, lorsque Jim's Sporting Goods vous fournit son certificat TLS/SSL, vous pouvez vérifier la signature numérique de l'autorité de certification via un certificat racine dans votre navigateur ou votre système d'exploitation. Si la signature est valide, vous pouvez être relativement sûr que la clé publique du certificat appartient bien à Jim's Sporting Goods. Sur cette base, il est facile d'établir un protocole pour une communication sécurisée avec Jim's Sporting Goods.

La distribution des clés est désormais beaucoup plus simple pour Jim's Sporting Goods. Il n'est pas difficile de constater que la gestion des clés a également été grandement simplifiée. Au lieu de devoir stocker des milliers de clés, Jim's Sporting Goods n'a plus qu'à stocker une clé privée qui lui permet de signer la clé publique de son certificat SSL. Chaque fois qu'un client se rend sur le site de Jim's Sporting Goods, il peut établir une session de communication sécurisée à partir de cette clé publique. Les clients n'ont pas non plus besoin de stocker des informations (autres que les clés publiques des autorités de certification reconnues dans leur système d'exploitation et leur navigateur).

**Notes:**

[Tout système visant à assurer la non-répudiation, l'autre thème abordé au chapitre 1, devra à la base faire appel à des signatures numériques.

## Fonctions de hachage

<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Les fonctions de hachage sont omniprésentes en cryptographie. Elles ne sont ni symétriques ni asymétriques, mais appartiennent à une catégorie cryptographique à part entière.

Nous avons déjà rencontré les fonctions de hachage au chapitre 4 avec la création de messages d'authentification basés sur le hachage. Elles sont également importantes dans le contexte des signatures numériques, mais pour une raison légèrement différente : En effet, les signatures numériques sont généralement créées à partir de la valeur de hachage d'un message (crypté), plutôt que du message lui-même (crypté). Dans cette section, je proposerai une introduction plus approfondie des fonctions de hachage.

Commençons par définir une fonction de hachage. Une **fonction de hachage** est une fonction calculable efficacement qui prend des entrées de taille arbitraire et produit des sorties de longueur fixe.

Une **fonction de hachage cryptographique** est une fonction de hachage utile pour les applications de cryptographie. La sortie d'une fonction de hachage cyptographique est généralement appelée **hash**, **hash-value** ou **message digest**.

Dans le contexte de la cryptographie, une "fonction de hachage" fait généralement référence à une fonction de hachage cryptographique. C'est la pratique que j'adopterai à partir de maintenant.

Un exemple de fonction de hachage populaire est **SHA-256** (secure hash algorithm 256). Quelle que soit la taille de l'entrée (par exemple, 15 bits, 100 bits ou 10 000 bits), cette fonction produira une valeur de hachage de 256 bits. Vous trouverez ci-dessous quelques exemples de résultats de la fonction SHA-256.

"Hello" : `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

"52398" : `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`

"Cryptography is fun" : `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`

Tous les résultats sont exactement 256 bits écrits au format hexadécimal (chaque chiffre hexadécimal peut être représenté par quatre chiffres binaires). Ainsi, même si vous aviez inséré le livre *Le Seigneur des Anneaux* de Tolkien dans la fonction SHA-256, la sortie serait toujours de 256 bits.

Les fonctions de hachage telles que SHA-256 sont utilisées à diverses fins en cryptographie. Les propriétés exigées d'une fonction de hachage dépendent réellement du contexte d'une application particulière. Deux propriétés principales sont généralement souhaitées pour les fonctions de hachage en cryptographie : [6]

1.	Résistance aux collisions

2.	Cacher

Une fonction de hachage $H$ est dite **résistante aux collisions** s'il est impossible de trouver deux valeurs, $x$ et $y$, telles que $x \neq y$, et pourtant $H(x) = H(y)$.

Les fonctions de hachage résistantes aux collisions sont importantes, par exemple, pour la vérification des logiciels. Supposons que vous souhaitiez télécharger la version Windows de Bitcoin Core 0.21.0 (une application serveur pour le traitement du trafic réseau Bitcoin). Les principales étapes à suivre pour vérifier la légitimité du logiciel sont les suivantes :

1.	Vous devez d'abord télécharger et importer les clés publiques d'un ou plusieurs contributeurs Bitcoin Core dans un logiciel qui peut vérifier les signatures numériques (par exemple Kleopetra). Vous pouvez trouver ces clés publiques [ici] (https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Il est recommandé de vérifier le logiciel Bitcoin Core avec les clés publiques de plusieurs contributeurs.

2.	Ensuite, vous devez vérifier les clés publiques que vous avez importées. Vous devez au moins vérifier que les clés publiques que vous avez trouvées sont les mêmes que celles qui ont été publiées à d'autres endroits. Vous pouvez, par exemple, consulter les pages web personnelles, les pages Twitter ou les pages Github des personnes dont vous avez importé les clés publiques. En général, cette comparaison des clés publiques se fait en comparant un court hachage de la clé publique, appelé empreinte digitale.

3.	Ensuite, vous devez télécharger l'exécutable de Bitcoin Core depuis leur [site web] (www.bitcoincore.org). Des paquets sont disponibles pour les systèmes d'exploitation Linux, Windows et MAC.

4.	Ensuite, vous devez localiser deux fichiers de publication. Le premier contient le hachage officiel SHA-256 de l'exécutable que vous avez téléchargé ainsi que les hachages de tous les autres paquets qui ont été publiés. Un autre fichier de version contiendra les signatures des différents contributeurs sur le fichier de version avec les hachages des paquets. Ces deux fichiers de publication devraient se trouver sur le site web de Bitcoin Core.

5.	 Ensuite, vous devez calculer le hachage SHA-256 de l'exécutable que vous avez téléchargé sur le site web de Bitcoin Core sur votre propre ordinateur. Vous comparez ensuite ce résultat avec celui du hachage du paquet officiel de l'exécutable. Ils devraient être identiques.

6.	Enfin, vous devrez vérifier qu'une ou plusieurs signatures numériques sur le fichier de version avec les hachages officiels du paquet correspondent bien à une ou plusieurs clés publiques que vous avez importées (les versions de Bitcoin Core ne sont pas toujours signées par tout le monde). Vous pouvez le faire avec une application telle que Kleopetra.

Ce processus de vérification du logiciel présente deux avantages principaux. Premièrement, il garantit qu'il n'y a pas eu d'erreur de transmission lors du téléchargement à partir du site web de Bitcoin Core. Deuxièmement, il garantit qu'aucun attaquant n'a pu vous faire télécharger un code modifié et malveillant, que ce soit en piratant le site web de Bitcoin Core ou en interceptant le trafic.

Comment le processus de vérification des logiciels décrit ci-dessus permet-il de se prémunir contre ces problèmes ?

Si vous avez vérifié avec diligence les clés publiques que vous avez importées, vous pouvez être certain que ces clés sont les leurs et qu'elles n'ont pas été compromises. Étant donné que les signatures numériques sont infalsifiables, vous savez que seuls ces contributeurs auraient pu apposer une signature numérique sur les hachages officiels des paquets figurant dans le fichier de version.

Supposons que les signatures du fichier de version que vous avez téléchargé soient vérifiées. Vous pouvez maintenant comparer la valeur de hachage que vous avez calculée localement pour l'exécutable Windows que vous avez téléchargé avec celle incluse dans le fichier de version correctement signé. Comme vous le savez, la fonction de hachage SHA-256 est résistante aux collusions. Une correspondance signifie que votre exécutable est exactement le même que l'exécutable officiel.

Passons maintenant à la deuxième propriété commune des fonctions de hachage : **cacher**. On dit d'une fonction de hachage $H$ qu'elle a la propriété de cacher si, pour tout $x$ choisi au hasard dans un très large éventail, il est impossible de trouver $x$ si l'on dispose seulement de $H(x)$.

Ci-dessous, vous pouvez voir la sortie SHA-256 d'un message que j'ai écrit. Pour garantir un caractère aléatoire suffisant, le message comprend une chaîne de caractères générée de manière aléatoire à la fin. Étant donné que SHA-256 possède la propriété de dissimulation, personne ne pourrait déchiffrer ce message.


- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`

Mais je ne vous laisserai pas en suspens jusqu'à ce que SHA-256 devienne plus faible. Le message original que j'ai écrit était le suivant :


- "Il s'agit d'un message très aléatoire, ou plutôt d'une sorte d'aléatoire. La première partie ne l'est pas, mais je vais terminer par des caractères relativement aléatoires pour garantir un message très imprévisible. XLWz4dVG3BxUWm7zQ9qS".

Les fonctions de hachage dotées de la propriété de dissimulation sont couramment utilisées dans la gestion des mots de passe (la résistance aux collisions est également importante pour cette application). Tout service en ligne digne de ce nom basé sur un compte, tel que Facebook ou Google, ne stocke pas directement vos mots de passe pour gérer l'accès à votre compte. Au lieu de cela, ils ne stockent qu'un hachage de ce mot de passe. Chaque fois que vous saisissez votre mot de passe dans un navigateur, un hachage est d'abord calculé. Seul ce hachage est envoyé au serveur du fournisseur de services et comparé au hachage stocké dans la base de données dorsale. La propriété de dissimulation permet de s'assurer que les attaquants ne peuvent pas récupérer le mot de passe à partir de la valeur de hachage.

La gestion des mots de passe au moyen de hachages ne fonctionne bien sûr que si les utilisateurs choisissent effectivement des mots de passe difficiles. La propriété de dissimulation suppose que x soit choisi au hasard dans un très large éventail. Le choix de mots de passe tels que "1234", "mypassword" ou votre date d'anniversaire n'offre aucune sécurité réelle. Il existe de longues listes de mots de passe courants et de leurs hachages que les attaquants peuvent exploiter s'ils obtiennent le hachage de votre mot de passe. Ce type d'attaque est connu sous le nom d'"attaque par dictionnaire". Si les pirates connaissent certaines de vos données personnelles, ils peuvent également tenter de faire des suppositions éclairées. C'est pourquoi vous avez toujours besoin de mots de passe longs et sûrs (de préférence des chaînes longues et aléatoires provenant d'un gestionnaire de mots de passe).

Parfois, une application peut avoir besoin d'une fonction de hachage qui présente à la fois une résistance aux collisions et une capacité de dissimulation. Mais ce n'est certainement pas toujours le cas. Le processus de vérification des logiciels dont nous avons parlé, par exemple, exige uniquement que la fonction de hachage présente une résistance aux collisions, le masquage n'étant pas important.

Si la résistance aux collisions et le masquage sont les principales propriétés recherchées pour les fonctions de hachage en cryptographie, d'autres types de propriétés peuvent également être souhaitables dans certaines applications.

**Notes:**

[6] La terminologie " cacher " n'est pas un langage courant, mais elle est tirée spécifiquement de Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller et Steven Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), chapitre 1.

# Le système cryptographique RSA

<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

## Le problème de la factorisation

<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Si la cryptographie symétrique est généralement assez intuitive pour la plupart des gens, ce n'est pas le cas de la cryptographie asymétrique. Bien que vous soyez probablement à l'aise avec la description de haut niveau proposée dans les sections précédentes, vous vous demandez probablement ce que sont précisément les fonctions à sens unique et comment elles sont utilisées pour construire des schémas asymétriques.

Dans ce chapitre, je lèverai une partie du mystère qui entoure la cryptographie asymétrique, en examinant plus en profondeur un exemple spécifique, à savoir le cryptosystème RSA. Dans la première section, je présenterai le problème de factorisation sur lequel repose le problème RSA. Nous aborderons ensuite un certain nombre de résultats clés de la théorie des nombres. Dans la dernière section, nous rassemblerons ces informations pour expliquer le problème RSA et la manière dont il peut être utilisé pour créer des systèmes cryptographiques asymétriques.

Il n'est pas facile d'ajouter cette profondeur à notre discussion. Il faut en effet introduire un certain nombre de théorèmes et de propositions relatifs à la théorie des nombres. Mais ne vous laissez pas dissuader par les mathématiques. Travailler sur cette discussion améliorera considérablement votre compréhension de ce qui sous-tend la cryptographie asymétrique et c'est un investissement qui en vaut la peine.

Passons maintenant au problème de la factorisation.

___

Lorsque vous multipliez deux nombres, par exemple $a$ et $b$, nous appelons les nombres $a$ et $b$ **facteurs**, et le résultat **produit**. Tenter d'écrire un nombre $N$ en multipliant deux facteurs ou plus s'appelle **factorisation** ou **factoring**. [1] On peut appeler tout problème nécessitant cette opération un **problème de factorisation**.

Il y a environ 2 500 ans, le mathématicien grec Euclide d'Alexandrie a découvert un théorème clé sur la factorisation des nombres entiers. Ce théorème, communément appelé **théorème de factorisation unique**, énonce ce qui suit :

**Théorème 1**. Tout entier $N$ supérieur à 1 est soit un nombre premier, soit peut être exprimé comme un produit de facteurs premiers.

Tout ce que la dernière partie de cette affirmation signifie, c'est que vous pouvez prendre n'importe quel entier non premier $N$ supérieur à 1, et l'écrire comme une multiplication de nombres premiers. Vous trouverez ci-dessous plusieurs exemples d'entiers non premiers écrits comme le produit de facteurs premiers.


- $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
- 84$ = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
- $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$

Pour les trois entiers ci-dessus, il est relativement facile de calculer leurs facteurs premiers, même si l'on ne dispose que de $N$. Vous commencez par le plus petit nombre premier, à savoir 2, et vous voyez combien de fois l'entier $N$ est divisible par lui. Vous testez ensuite la divisibilité de $N$ par 3, 5, 7, etc. Vous continuez ce processus jusqu'à ce que votre entier $N$ s'écrive comme le produit de nombres premiers uniquement.

Prenons par exemple l'entier 84. Vous trouverez ci-dessous le processus de détermination de ses facteurs premiers. À chaque étape, nous éliminons le plus petit facteur premier restant (à gauche) et déterminons le terme restant à factoriser. Nous continuons jusqu'à ce que le terme restant soit également un nombre premier. À chaque étape, la factorisation actuelle de 84 est affichée à l'extrême droite.


- Facteur premier = 2 : reste du terme = 42 ($84 = 2 \cdot 42$)
- Facteur premier = 2 : reste du terme = 21 ($84 = 2 \cdot 2 \cdot 21$)
- Facteur premier = 3 : reste du terme = 7 ($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
- Comme 7 est un nombre premier, le résultat est $2 \cdot 2 \cdot 3 \cdot 7$, ou $2^2 \cdot 3 \cdot 7$.

Supposons maintenant que $N$ est très grand. Quelle serait la difficulté de réduire $N$ en ses facteurs premiers ?

Cela dépend vraiment de $N$. Supposons, par exemple, que $N$ soit égal à 50 450 400. Bien que ce nombre semble intimidant, les calculs ne sont pas très compliqués et peuvent facilement être effectués à la main. Comme ci-dessus, il suffit de commencer par 2 et d'aller plus loin. Ci-dessous, vous pouvez voir le résultat de ce processus de la même manière que ci-dessus.


- 2 : 25 225 200 (50 450 400 $ = 2 \cdot 25 225 200$)
- 2 : 12.612.600 ($50.450.400 = 2^2 \cdot 12.612.600$)
- 2 : 6 306 300 (50 450 400 $ = 2^3 \cdot 6 306 300$)
- 2 : 3 153 150 (50 450 400 $ = 2^4 \cdot 3 153 150$)
- 2 : 1 576 575 (50 450 400 $ = 2^5 \cdot 1 576 575$)
- 3 : 525,525 ($50,450,400 = 2^5 \cdot 3 \cdot 525,525$)
- 3 : 175,175 ($50,450,400 = 2^5 \cdot 3^2 \cdot 175,175$)
- 5 : 35,035 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5 \cdot 35,035$)
- 5 : 7 007 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7,007$)
- 7 : 1 001 (50 450 400 $ = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1 001$)
- 7 : 143 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
- 11 : 13 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
- Comme 13 est un nombre premier, le résultat est $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.

Résoudre ce problème à la main prend un certain temps. Un ordinateur, bien sûr, pourrait faire tout cela en une petite fraction de seconde. En fait, un ordinateur peut souvent factoriser des nombres entiers extrêmement grands en une fraction de seconde.

Il existe cependant certaines exceptions. Supposons que nous choisissions d'abord au hasard deux très grands nombres premiers. Il est courant d'appeler ces nombres $p$ et $q$, et j'adopterai cette convention ici.

Pour être concret, disons que $p$ et $q$ sont tous deux des nombres premiers de 1024 bits, et qu'ils nécessitent effectivement au moins 1024 bits pour être représentés (le premier bit doit donc être 1). Ainsi, par exemple, 37 ne peut pas être l'un des nombres premiers. Vous pouvez certainement représenter 37 avec 1024 bits. Mais il est clair que vous n'avez pas besoin de ce nombre de bits pour le représenter. Vous pouvez représenter 37 par n'importe quelle chaîne de 6 bits ou plus. (En 6 bits, 37 serait représenté par $100101$).

Il est important d'apprécier la taille de $p$ et $q$ s'ils sont sélectionnés dans les conditions ci-dessus. À titre d'exemple, j'ai choisi un nombre premier aléatoire dont la représentation nécessite au moins 1024 bits.


- 14,752,173,874,503,595,484,930,006,383,670,759,559,764,562,721,397,166,747,289,220,945,457,932,666,751,048,198,854,920,097,085,690,793,755,254,946,188,163,753,506,778,089,706,699,671,722,089,715,624,760,049,594,106,189,662,669,156,149,028,900,805,928,183,585,427,782,974,951,355,515,394,807,209,836,870,484,558,332,897,443,152,653,214,483,870,992,618,171,825,921,582,253,023,974,514,209,142,520,026,807,636,589

Supposons maintenant qu'après avoir choisi au hasard des nombres premiers $p$ et $q$, nous les multiplions pour obtenir un entier $N$. Ce dernier entier est donc un nombre de 2048 bits qui nécessite au moins 2048 bits pour sa représentation. Il est beaucoup, beaucoup plus grand que $p$ ou $q$.

Supposons que vous donniez seulement $N$ à un ordinateur et que vous lui demandiez de trouver les deux facteurs premiers de $N$ sur 1024 bits. La probabilité que l'ordinateur découvre $p$ et $q$ est extrêmement faible. On peut dire que c'est impossible à toutes fins pratiques. Il en est ainsi même si vous employez un superordinateur ou même un réseau de superordinateurs.

Pour commencer, supposons que l'ordinateur tente de résoudre le problème en parcourant 1024 nombres binaires, en testant dans chaque cas s'ils sont premiers et s'ils sont des facteurs de $N$. L'ensemble des nombres premiers à tester est alors d'environ $1.265 \cdot 10^{305}$. [2]

Même si l'on prend tous les ordinateurs de la planète et qu'on leur demande d'essayer de trouver et de tester des nombres premiers de 1024 bits de cette manière, une chance sur un milliard de trouver un facteur premier de $N$ nécessiterait une période de calcul bien plus longue que l'âge de l'Univers.

Dans la pratique, un ordinateur peut faire mieux que la procédure approximative décrite ci-dessus. Il existe plusieurs algorithmes que l'ordinateur peut appliquer pour parvenir plus rapidement à une factorisation. Cependant, même en utilisant ces algorithmes plus efficaces, la tâche de l'ordinateur reste infaisable d'un point de vue informatique. [3]

Il est important de noter que la difficulté de la factorisation dans les conditions décrites ci-dessus repose sur l'hypothèse qu'il n'existe pas d'algorithme efficace pour le calcul des facteurs premiers. Nous ne pouvons pas prouver qu'il n'existe pas d'algorithme efficace. Néanmoins, cette hypothèse est très plausible : malgré des efforts considérables déployés pendant des centaines d'années, nous n'avons pas encore trouvé d'algorithme efficace sur le plan informatique.

Par conséquent, le problème de la factorisation, dans certaines circonstances, peut être considéré comme un problème difficile. Plus précisément, lorsque $p$ et $q$ sont de très grands nombres premiers, leur produit $N$ n'est pas difficile à calculer ; mais la factorisation à partir de $N$ seulement est pratiquement impossible.

**Notes:**

[La factorisation peut également être importante pour travailler avec d'autres types d'objets mathématiques que les nombres. Par exemple, il peut être utile de factoriser des expressions polynomiales telles que $x^2 - 2x + 1$. Dans notre discussion, nous nous concentrerons uniquement sur la factorisation des nombres, en particulier des entiers.

[2] Selon le **théorème du nombre premier**, le nombre de nombres premiers inférieurs ou égaux à $N$ est approximativement $N/\ln(N)$. Cela signifie que vous pouvez approximer le nombre de nombres premiers de longueur 1024 bits par :

$$ \frac{2^{1024}}{\ln(2^{1024})} - \frac{2^{1023}}{\ln(2^{1023})} $$

...ce qui équivaut à environ 1,265 \\Npar 10^{305}$.

[Il en va de même pour les problèmes de logarithme discret. C'est pourquoi les constructions asymétriques fonctionnent avec des clés beaucoup plus grandes que les constructions cryptographiques symétriques.

## Résultats de la théorie des nombres

<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Malheureusement, le problème de la factorisation ne peut pas être utilisé directement pour les systèmes cryptographiques asymétriques. Cependant, nous pouvons utiliser un problème plus complexe mais connexe à cet effet : le problème RSA.

Pour comprendre le problème RSA, nous devons comprendre un certain nombre de théorèmes et de propositions de la théorie des nombres. Ceux-ci sont présentés dans cette section en trois sous-sections : (1) l'ordre de N, (2) l'inversibilité modulo N, et (3) le théorème d'Euler.

Une partie du contenu des trois sous-sections a déjà été présentée dans le *chapitre 3*. Mais je vais les rappeler ici pour des raisons de commodité.

### L'ordre de N

Un entier $a$ est **coprime** ou **premier relatif** avec un entier $N$, si le plus grand diviseur commun entre eux est 1. Bien que 1 ne soit pas, par convention, un nombre premier, il est coprime de tout entier (tout comme $-1$).

Par exemple, considérons le cas où $a = 18$ et $N = 37$. Il s'agit clairement de coprimes. Le plus grand entier qui se divise à la fois en 18 et 37 est 1. Par contre, considérons le cas où $a = 42$ et $N = 16$. Il est clair qu'il ne s'agit pas de coprimes. Les deux nombres sont divisibles par 2, qui est supérieur à 1.

Nous pouvons maintenant définir l'ordre de $N$ comme suit. Supposons que $N$ soit un entier supérieur à 1. L'**ordre de N** est alors le nombre de tous les coprimes avec $N$ tels que pour chaque coprimes $a$, la condition suivante s'applique : $1 \leq a < N$.

Par exemple, si $N = 12$, alors 1, 5, 7 et 11 sont les seuls coprimes qui répondent à la condition ci-dessus. Par conséquent, l'ordre de 12 est égal à 4.

Supposons que $N$ soit un nombre premier. Alors tout entier plus petit que $N$ mais supérieur ou égal à 1 est coprime avec lui. Cela inclut tous les éléments de l'ensemble suivant : $\{1,2,3,....,N - 1\}$. Par conséquent, lorsque $N$ est premier, l'ordre de $N$ est $N - 1$. C'est ce qu'affirme la proposition 1, où $\phi(N)$ désigne l'ordre de $N$.

**Proposition 1**. $\phi(N) = N - 1$ lorsque $N$ est premier

Supposons que $N$ ne soit pas premier. Vous pouvez alors calculer son ordre en utilisant **la fonction Phi d'Euler**. Si le calcul de l'ordre d'un petit entier est relativement simple, la fonction Phi d'Euler devient particulièrement importante pour les entiers plus grands. La proposition de la fonction Phi d'Euler est énoncée ci-dessous.

**Théorème 2**. Soit $N$ égal à $p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, où l'ensemble $\{p_i\}$ est constitué de tous les facteurs premiers distincts de $N$ et chaque $e_i$ indique combien de fois le facteur premier $p_i$ apparaît pour $N$. Dans ce cas,

$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$

*le *théorème 2** montre qu'une fois que l'on a décomposé tout $N$ non premier en ses facteurs premiers distincts, il est facile de calculer l'ordre de $N$.

Par exemple, supposons que $N = 270$. Il ne s'agit manifestement pas d'un nombre premier. En décomposant $N$ en ses facteurs premiers, on obtient l'expression : $2 \cdot 3^3 \cdot 5$. Selon la fonction Phi d'Euler, l'ordre de $N$ est alors le suivant :

$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$

Supposons ensuite que $N$ est un produit de deux nombres premiers, $p$ et $q$. *le *théorème 2** ci-dessus indique alors que l'ordre de $N$ est le suivant :

$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$

Il s'agit d'un résultat clé pour le problème RSA en particulier, qui est énoncé dans la **Proposition 2** ci-dessous.

**Proposition 2**. Si $N$ est le produit de deux nombres premiers, $p$ et $q$, l'ordre de $N$ est le produit $(p - 1) \cdot (q - 1)$.

Pour illustrer ce propos, supposons que $N = 119$. Cet entier peut être factorisé en deux nombres premiers, à savoir 7 et 17. Par conséquent, la fonction Phi d'Euler suggère que l'ordre de 119 est le suivant :

$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$$$

En d'autres termes, l'entier 119 a 96 coprimes dans l'intervalle de 1 à 119. En fait, cet ensemble comprend tous les entiers compris entre 1 et 119 qui ne sont pas des multiples de 7 ou de 17.

A partir de maintenant, nous désignerons l'ensemble des coprimes qui détermine l'ordre de $N$ par $C_N$. Pour notre exemple où $N = 119$, l'ensemble $C_{119}$ est beaucoup trop grand pour être énuméré complètement. Mais certains de ses éléments sont les suivants :

$$C_{119} = \N{1, 2, \Npoints 6, 8 \Npoints 13, 15, 16, 18, \Npoints 33, 35 \Npoints 96}$$$

### Invertibilité modulo N

On peut dire qu'un entier $a$ est **inversible modulo N**, s'il existe au moins un entier $b$ tel que $a \cdot b \mod N = 1 \mod N$. Un tel entier $b$ est appelé **inverse** (ou **inverse multiplicatif**) de $a$ compte tenu de la réduction modulo $N$.

Supposons, par exemple, que $a = 5$ et $N = 11$. Il existe de nombreux entiers par lesquels on peut multiplier 5, de sorte que $5 \cdot b \mod 11 = 1 \cmod 11$. Considérons, par exemple, les entiers 20 et 31. Il est facile de voir que ces deux entiers sont des inverses de 5 par réduction modulo 11.


- $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
- $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$

Alors que 5 a de nombreux inverses de réduction modulo 11, vous pouvez montrer qu'il n'existe qu'un seul inverse positif de 5 qui soit inférieur à 11. En fait, ce n'est pas propre à notre exemple particulier, mais un résultat général.

**Proposition 3**. Si l'entier $a$ est inversible modulo $N$, il doit y avoir exactement un inverse positif de $a$ inférieur à $N$ (cet unique inverse de $a$ doit donc provenir de l'ensemble $\{1, \dots, N - 1\}$).

Désignons l'unique inverse de $a$ de la **Proposition 3** par $a^{-1}$. Dans le cas où $a = 5$ et $N = 11$, on voit que $a^{-1} = 9$, étant donné que $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.

Notez que vous pouvez également obtenir la valeur 9 pour $a^{-1}$ dans notre exemple en réduisant simplement tout autre inverse de $a$ par modulo 11. Par exemple, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Ainsi, chaque fois qu'un entier $a > N$ est inversible modulo $N$, alors $a \mod N$ doit aussi être inversible modulo $N$.

Il n'existe pas nécessairement d'inverse de $a$ réduction modulo $N$. Supposons, par exemple, que $a = 2$ et $N = 8$. Il n'existe pas de $b$, ou plus précisément de $a^{-1}$, tel que $2 \cdot b \mod 8 = 1 \mod 8$. En effet, toute valeur de $b$ produira toujours un multiple de 2, de sorte qu'aucune division par 8 ne peut jamais produire un reste égal à 1.

Comment savoir si un entier $a$ a un inverse pour un $N$ donné ? Comme vous l'avez peut-être remarqué dans l'exemple ci-dessus, le plus grand diviseur commun entre 2 et 8 est supérieur à 1, à savoir 2. Et ceci illustre en fait le résultat général suivant :

**Proposition 4**. Il existe un inverse d'un entier $a$ donné par réduction modulo $N$, et en particulier un unique inverse positif inférieur à $N$, si et seulement si le plus grand diviseur commun entre $a$ et $N$ est 1 (c'est-à-dire s'ils sont coprimes).

Dans le cas où $a = 5$ et $N = 11$, nous avons conclu que $a^{-1} = 9$, étant donné que $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. Il est important de noter que l'inverse est également vrai. Autrement dit, lorsque $a = 9$ et $N = 11$, c'est le cas que $a^{-1} = 5$.

### Théorème d'Euler

Avant de passer au problème RSA, nous devons comprendre un autre théorème crucial, à savoir le **théorème d'Euler**. Il énonce ce qui suit :

**Théorème 3**. Supposons que deux entiers $a$ et $N$ soient coprimes. Alors, $a^{\phi(N)} \mod N = 1 \mod N$.

Il s'agit d'un résultat remarquable, mais un peu déroutant au premier abord. Prenons un exemple pour le comprendre.

Supposons que $a = 5$ et $N = 7$. Ce sont bien des coprimes comme l'exige le théorème d'Euler. Nous savons que l'ordre de 7 est égal à 6, étant donné que 7 est un nombre premier (voir **Proposition 1**).

Le théorème d'Euler stipule maintenant que $5^6 \mod 7$ doit être égal à $1 \mod 7$. Les calculs ci-dessous montrent que c'est effectivement le cas.


- $5^6 \mod 7 = 15,625 \mod 7 = 1 \mod N$

L'entier 7 se divise en 15 624 un total de 2 233 fois. Par conséquent, le reste de la division de 16 625 par 7 est 1.

Ensuite, en utilisant la fonction Phi d'Euler, **théorème 2**, vous pouvez dériver **la proposition 5** ci-dessous.

**Proposition 5**. \phi(a \cdot b) = \phi(a) \cdot \phi(b)$ pour tout entier positif $a$ et $b$.

Nous ne montrerons pas pourquoi c'est le cas. Mais notez simplement que vous avez déjà vu la preuve de cette proposition par le fait que $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ lorsque $p$ et $q$ sont des nombres premiers, comme indiqué dans la **Proposition 2**.

Le théorème d'Euler associé à la **Proposition 5** a des implications importantes. Voyez ce qui se passe, par exemple, dans les expressions ci-dessous, où $a$ et $N$ sont des coprimes.


- a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
- a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$
- a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$

Ainsi, la combinaison du théorème d'Euler et de la **Proposition 5** nous permet de calculer simplement un certain nombre d'expressions. En général, nous pouvons résumer l'idée comme dans la **Proposition 6**.

**Proposition 6**. a^x \mod N = a^{x \mod \phi(N)}$

Il nous reste maintenant à assembler le tout dans une dernière étape délicate.

Tout comme $N$ possède un ordre $\phi(N)$ qui inclut les éléments de l'ensemble $C_N$, nous savons que l'entier $\phi(N)$ doit à son tour posséder un ordre et un ensemble de coprimes. Fixons $\phi(N) = R$. Nous savons alors qu'il existe également une valeur pour $\phi(R)$ et un ensemble de coprimes $C_R$.

Supposons que nous choisissions maintenant un entier $e$ dans l'ensemble $C_R$. Nous savons d'après la **Proposition 3** que cet entier $e$ n'a qu'un seul inverse positif inférieur à $R$. C'est-à-dire que $e$ a un unique inverse dans l'ensemble $C_R$. Appelons cet inverse $d$. Etant donné la définition d'un inverse, cela signifie que $e \cdot d = 1 \mod R$.

Nous pouvons utiliser ce résultat pour faire une déclaration sur notre entier original $N$. Ceci est résumé dans la **Proposition 7**.

**Proposition 7**. Supposons que $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Alors pour tout élément $a$ de l'ensemble $C_N$ il faut que $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.

Nous disposons maintenant de tous les résultats de la théorie des nombres nécessaires pour énoncer clairement le problème RSA.

## Le système cryptographique RSA

<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>

Nous sommes maintenant prêts à énoncer le problème RSA. Supposons que vous créiez un ensemble de variables composé de $p$, $q$, $N$, $\phi(N)$, $e$, $d$ et $y$. Appelons cet ensemble $\Pi$. Il est créé comme suit :

1. Générer deux nombres premiers aléatoires $p$ et $q$ de même taille et calculer leur produit $N$.

2. Calculer l'ordre de $N$, $\phi(N)$, par le produit suivant : $(p - 1) \cdot (q - 1)$.

3. Choisir un $e > 2$ tel qu'il soit plus petit et coprime à $\phi(N)$.

4. Calculer $d$ en fixant $e \cdot d \mod \phi(N) = 1$.

5. Choisir une valeur aléatoire $y$ qui est plus petite et coprime à $N$.

Le problème RSA consiste à trouver un $x$ tel que $x^e = y$, tout en ne disposant que d'un sous-ensemble d'informations concernant $\Pi$, à savoir les variables $N$, $e$ et $y$. Lorsque $p$ et $q$ sont très grands, typiquement il est recommandé qu'ils aient une taille de 1024 bits, le problème RSA est considéré comme difficile. Vous pouvez maintenant comprendre pourquoi c'est le cas, compte tenu de ce qui précède.

Une façon simple de calculer $x$ lorsque $x^e \mod N = y \mod N$ est de calculer $y^d \mod N$. Nous savons que $y^d \mod N = x \mod N$ par les calculs suivants :

$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$

Le problème est que nous ne connaissons pas la valeur $d$, puisqu'elle n'est pas donnée dans le problème. On ne peut donc pas calculer directement $y^d \mod N$ pour obtenir $x \mod N$.

Nous pourrions cependant être en mesure de calculer indirectement $d$ à partir de l'ordre de $N$, $\phi(N)$, puisque nous savons que $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Mais par hypothèse, le problème ne donne pas non plus de valeur pour $\phi(N)$.

Enfin, l'ordre pourrait être calculé indirectement avec les facteurs premiers $p$ et $q$, de sorte que nous puissions éventuellement calculer $d$. Mais par hypothèse, les valeurs $p$ et $q$ ne nous ont pas non plus été fournies.

Strictement parlant, même si le problème de factorisation à l'intérieur d'un problème RSA est difficile, nous ne pouvons pas prouver que le problème RSA est également difficile. Il peut en effet y avoir d'autres moyens de résoudre le problème RSA que la factorisation. Cependant, il est généralement admis et supposé que si le problème de factorisation à l'intérieur du problème RSA est difficile, le problème RSA lui-même est également difficile.

Si le problème RSA est effectivement difficile, alors il produit une fonction à sens unique avec une trappe. La fonction est ici $f(g) = g^e \mod N$. En connaissant $f(g)$, n'importe qui pourrait facilement calculer une valeur $y$ pour un $g = x$ particulier. Cependant, il est pratiquement impossible de calculer une valeur particulière $x$ simplement en connaissant la valeur $y$ et la fonction $f(g)$. L'exception est lorsque l'on vous donne un élément d'information $d$, la trappe. Dans ce cas, il suffit de calculer $y^d$ pour obtenir $x$.

Prenons un exemple spécifique pour illustrer le problème RSA. Je ne peux pas choisir un problème RSA qui serait considéré comme difficile dans les conditions ci-dessus, car les chiffres seraient trop lourds. Cet exemple a pour but d'illustrer le fonctionnement général du problème RSA.

Pour commencer, supposons que vous choisissiez au hasard deux nombres premiers 13 et 31. Donc $p = 13$ et $q = 31$. Le produit $N$ de ces deux nombres premiers est égal à 403. Nous pouvons facilement calculer l'ordre de 403. Il est équivalent à $(13 - 1) \cdot (31 - 1) = 360$.

Ensuite, comme l'exige l'étape 3 du problème RSA, nous devons choisir un coprime pour 360 qui soit supérieur à 2 et inférieur à 360. Nous ne devons pas choisir cette valeur au hasard. Supposons que nous choisissions 103. Il s'agit d'une coprime de 360 car son plus grand diviseur commun avec 103 est 1.

L'étape 4 exige maintenant que nous calculions une valeur $d$ telle que $103 \cdot d \mod 360 = 1$. Ce n'est pas une tâche facile à la main lorsque la valeur de $N$ est grande. Il faut utiliser une procédure appelée **algorithme d'Euclide étendu**.

Bien que je ne montre pas la procédure ici, elle donne la valeur 7 lorsque $e = 103$. Vous pouvez vérifier que la paire de valeurs 103 et 7 répond bien à la condition générale $e \cdot d \mod \phi(n) = 1$ par les calculs ci-dessous.


- $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$

Il est important de noter qu'étant donné la *Proposition 4*, nous savons qu'aucun autre entier compris entre 1 et 360 pour $d$ ne produira le résultat $103 \cdot d = 1 \mod 360$. De plus, la proposition implique qu'en choisissant une valeur différente pour $e$, on obtiendra une valeur unique différente pour $d$.

A l'étape 5 du problème RSA, nous devons choisir un entier positif $y$ qui est un plus petit coprime de 403. Supposons que nous choisissions $y = 2^{103}$. L'exponentiation de 2 par 103 donne le résultat ci-dessous.


- $2^{103} \mod 403 = 10,141,204,801,825,835,211,973,625,643,008 \mod 403 = 349 \mod 403$

Le problème RSA dans cet exemple particulier est maintenant le suivant : Vous disposez de $N = 403$, $e = 103$ et $y = 349 \mod 403$. Vous devez maintenant calculer $x$ de telle sorte que $x^{103} = 349 \mod 403$. En d'autres termes, vous devez trouver que la valeur originale avant l'exponentiation par 103 était 2.

Il serait facile (du moins pour un ordinateur) de calculer $x$ si nous savions que $d = 7$. Dans ce cas, il suffirait de déterminer $x$ comme ci-dessous.


- x = y^7 \mod 403 = 349^7 \mod 403 = 630,634,881,591,804,949 \mod 403 = 2 \mod 403$

Le problème est que vous n'avez pas été informé que $d = 7$. Vous pourriez bien sûr calculer $d$ à partir du fait que $103 \cdot d = 1 \mod 360$. Le problème est que l'on ne vous a pas non plus indiqué que l'ordre de $N = 360$. Enfin, vous pourriez aussi calculer l'ordre de 403 en calculant le produit suivant : $(p - 1) \cdot (q - 1)$. Mais on ne vous dit pas non plus que $p = 13$ et $q = 31$.

Bien sûr, un ordinateur pourrait encore résoudre le problème RSA pour cet exemple relativement facilement, parce que les nombres premiers impliqués ne sont pas grands. Mais lorsque les nombres premiers deviennent très grands, la tâche devient pratiquement impossible.

Nous avons maintenant présenté le problème RSA, un ensemble de conditions sous lesquelles il est difficile, et les mathématiques sous-jacentes. En quoi cela peut-il être utile pour la cryptographie asymétrique ? Plus précisément, comment pouvons-nous transformer la difficulté du problème RSA sous certaines conditions en un système de cryptage ou de signature numérique ?

Une approche consiste à prendre le problème RSA et à construire des schémas de manière simple. Par exemple, supposons que vous ayez généré un ensemble de variables $\Pi$ comme décrit dans le problème RSA, et que vous vous assuriez que $p$ et $q$ sont suffisamment grands. Vous définissez votre clé publique comme étant $(N, e)$ et partagez cette information avec le monde entier. Comme décrit ci-dessus, vous gardez secrètes les valeurs de $p$, $q$, $\phi(n)$ et $d$. En fait, $d$ est votre clé privée.

Quiconque souhaite vous envoyer un message $m$ qui est un élément de $C_N$ peut simplement le chiffrer comme suit : $c = m^e \mod N$ (le texte chiffré est ici équivalent à la valeur $y$ dans le problème RSA) : $c = m^e \mod N$. (Le texte chiffré $c$ est ici équivalent à la valeur $y$ dans le problème RSA.) Vous pouvez facilement décrypter ce message en calculant simplement $c^d \mod N$.

Vous pouvez tenter de créer un système de signature numérique de la même manière. Supposons que vous souhaitiez envoyer à quelqu'un un message $m$ avec une signature numérique $S$. Vous pourriez simplement définir $S = m^d \mod N$ et envoyer la paire $(m,S)$ au destinataire. N'importe qui peut vérifier la signature numérique en contrôlant simplement si $S^e \mod N = m \mod N$. Cependant, tout attaquant aurait beaucoup de mal à créer une $S$ valide pour un message, étant donné qu'il ne possède pas $d$.

Malheureusement, transformer ce qui est en soi un problème difficile, le problème RSA, en un schéma cryptographique n'est pas aussi simple. Pour le schéma de cryptage simple, vous ne pouvez sélectionner que des coprimes de $N$ comme messages. Cela ne nous laisse pas beaucoup de messages possibles, certainement pas assez pour une communication standard. En outre, ces messages doivent être choisis au hasard. Cela semble peu pratique. Enfin, tout message sélectionné deux fois produira exactement le même texte chiffré. Cette situation est extrêmement indésirable dans tout système de cryptage et ne répond à aucune notion moderne et rigoureuse de sécurité en matière de cryptage.

Les problèmes sont encore plus graves pour notre système de signature numérique simple. Dans l'état actuel des choses, n'importe quel attaquant peut facilement falsifier des signatures numériques en choisissant d'abord un nombre premier de $N$ comme signature, puis en calculant le message original correspondant. Cela rompt clairement avec l'exigence d'infalsifiabilité existentielle.

Néanmoins, en ajoutant un peu de complexité intelligente, le problème RSA peut être utilisé pour créer un système de cryptage à clé publique sécurisé ainsi qu'un système de signature numérique sécurisé. Nous n'entrerons pas ici dans les détails de ces constructions. [Il est toutefois important de noter que cette complexité supplémentaire ne modifie pas le problème RSA fondamental sur lequel ces systèmes sont basés.

**Notes:**

[4] Voir, par exemple, Jonathan Katz et Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL : 2015), pp. 410-32 pour le chiffrement RSA et pp. 444-41 pour les signatures numériques RSA.

# Conclusion
<partId>e538fb79-bf28-40cd-a5c3-badf864d8567</partId>

## Avis & Notes

<chapterId>366d6fd0-ceb2-4299-bf37-8c6dfcb681d5</chapterId>
<isCourseReview>true</isCourseReview>
 
## Examen Final

<chapterId>44882d2b-63cd-4fde-8485-f76f14d8b2fe</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusion
<chapterId>f1905f78-8cf7-5031-949a-dfa8b76079b4</chapterId>
<isCourseConclusion>true</isCourseConclusion>
