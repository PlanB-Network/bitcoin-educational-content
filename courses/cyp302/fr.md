---
name: Introduction à la cryptographie formelle
goal: Une introduction approfondie à la science et à la pratique de la cryptographie.
objectives:
  - Explorer les chiffres de Beale et les méthodes cryptographiques modernes pour comprendre les concepts de base et historiques de la cryptographie.
  - Se plonger dans la théorie des nombres, les groupes et les champs pour maîtriser les concepts mathématiques clés sous-jacents à la cryptographie.
  - Étudier le chiffrement en flux RC4 et l'AES avec une clé de 128 bits pour apprendre les algorithmes cryptographiques symétriques.
  - Enquêter sur le cryptosystème RSA, la distribution de clés et les fonctions de hachage pour explorer la cryptographie asymétrique.

---

# Plongée approfondie dans la cryptographie

Il est difficile de trouver de nombreux matériaux qui offrent un bon compromis dans l'éducation à la cryptographie.

D'une part, il y a des traités formels et longs, vraiment accessibles seulement à ceux qui ont une solide formation en mathématiques, en logique ou dans une autre discipline formelle. D'autre part, il y a des introductions très générales qui cachent vraiment trop de détails pour quiconque est au moins un peu curieux.

Cette introduction à la cryptographie cherche à capturer le juste milieu. Bien qu'elle devrait être relativement difficile et détaillée pour quiconque est nouveau dans le domaine de la cryptographie, ce n'est pas le terrier du lapin d'un traité fondamental typique.

+++

# Une introduction à la cryptographie
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Description courte
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Ce livre offre une introduction approfondie à la science et à la pratique de la cryptographie. Lorsque c'est possible, il se concentre sur l'exposition conceptuelle, plutôt que formelle du matériel.

> Ce cours est basé sur le dépôt [JWBurgers](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Tous droits à lui. Le contenu n'est pas encore terminé et est seulement ici pour montrer comment nous pourrions l'intégrer si JWburger's est d'accord.

### Motivation et objectifs

Il est difficile de trouver de nombreux matériaux qui offrent un bon compromis dans l'éducation à la cryptographie.

D'une part, il y a des traités formels et longs, vraiment accessibles seulement à ceux qui ont une solide formation en mathématiques, en logique ou dans une autre discipline formelle. D'autre part, il y a des introductions très générales qui cachent vraiment trop de détails pour quiconque est au moins un peu curieux.

Cette introduction à la cryptographie cherche à capturer le juste milieu. Bien qu'elle devrait être relativement difficile et détaillée pour quiconque est nouveau dans le domaine de la cryptographie, ce n'est pas le terrier du lapin d'un traité fondamental typique.

### Public cible

Des développeurs aux intellectuellement curieux, ce livre est utile pour quiconque veut plus qu'une compréhension superficielle de la cryptographie. Si votre objectif est de maîtriser le domaine de la cryptographie, alors ce livre est également un bon point de départ.

### Directives de lecture

Le livre contient actuellement sept chapitres : "Qu'est-ce que la Cryptographie ?" (Chapitre 1), "Fondements Mathématiques de la Cryptographie I" (Chapitre 2), "Fondements Mathématiques de la Cryptographie II" (Chapitre 3), "Cryptographie Symétrique" (Chapitre 4), "RC4 et AES" (Chapitre 5), "Cryptographie Asymétrique" (Chapitre 6), et "Le cryptosystème RSA" (Chapitre 7). Un dernier chapitre, "La Cryptographie en Pratique", sera encore ajouté. Il se concentre sur diverses applications cryptographiques, y compris la sécurité de la couche de transport, le routage en oignon et le système d'échange de valeur de Bitcoin.
À moins que vous n'ayez une solide formation en mathématiques, la théorie des nombres est probablement le sujet le plus difficile de ce livre. Je propose un aperçu dans le Chapitre 3, et elle apparaît également dans l'exposition de l'AES dans le Chapitre 5 et le cryptosystème RSA dans le Chapitre 7.
Si vous avez vraiment du mal avec les détails formels dans ces parties du livre, je vous recommande de vous contenter d'une lecture de haut niveau la première fois.

### Remerciements

Le livre le plus influent dans la conception de celui-ci a été _Introduction to Modern Cryptography_ de Jonathan Katz et Yehuda Lindell, CRC Press (Boca Raton, FL), 2015. Un cours accompagnant est disponible sur Coursera sous le nom "Cryptography."

Les principales sources supplémentaires qui ont été utiles pour créer l'aperçu dans ce livre sont Simon Singh, _The Code Book_, Fourth Estate (Londres, 1999); Christof Paar et Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) et un cours basé sur le livre de Paar appelé “Introduction to Cryptography” (disponible à https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); et Bruce Schneier, Applied Cryptography, 2e éd., 2015 (Indianapolis, IN : John Wiley & Sons).

Je ne citerai que des informations et des résultats très spécifiques que je prends de ces sources, mais je tiens à reconnaître ici ma dette générale envers elles.

Pour ces lecteurs qui souhaitent rechercher des connaissances plus avancées sur la cryptographie après cette introduction, je recommande vivement le livre de Katz et Lindell. Le cours de Katz sur Coursera est quelque peu plus accessible que le livre.

### Contributions

Veuillez consulter le fichier des contributions dans le dépôt pour quelques directives sur comment soutenir le projet.

# Qu'est-ce que la Cryptographie ?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

Commençons notre enquête sur le domaine de la cryptographie avec l'un des épisodes les plus charmants et divertissants de son histoire : celui des chiffres de Beale.<sup>[1](#footnote1)</sup>

L'histoire des chiffres de Beale est, à mon avis, plus susceptible d'être une fiction que la réalité. Mais elle se serait déroulée comme suit.

## Les chiffres de Beale
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>

Durant l'hiver de 1820 et 1822, un homme nommé Thomas J. Beale séjourna dans une auberge appartenant à Robert Morriss à Lynchburg (Virginie). À la fin du deuxième séjour de Beale, il remit à Morriss une boîte en fer contenant des papiers précieux pour les garder en sécurité.

Quelques mois plus tard, Morriss reçut une lettre de Beale datée du 9 mai 1822. Elle soulignait la grande valeur du contenu de la boîte en fer et donnait quelques instructions à Morriss : si ni Beale ni aucun de ses associés ne venait réclamer la boîte, il devrait l'ouvrir précisément dix ans après la date de la lettre (c'est-à-dire le 9 mai 1832). Certains des papiers à l'intérieur seraient rédigés en texte régulier. Plusieurs autres, cependant, seraient “inintelligibles sans l'aide d'une clé.” Cette “clé” serait alors livrée à Morriss par un ami non nommé de Beale en juin 1832.
Malgré les instructions claires, Morriss n'a pas ouvert la boîte en mai 1832 et l'ami mystérieux de Beale ne s'est jamais présenté en juin de cette année-là. Ce n'est qu'en 1845 que l'aubergiste a finalement décidé d'ouvrir la boîte. À l'intérieur, Morriss a trouvé une note expliquant comment Beale et ses associés ont découvert de l'or et de l'argent dans l'Ouest et l'ont enterré, avec quelques bijoux, pour le garder en sécurité. De plus, la boîte contenait trois **ciphertexts** : c'est-à-dire, des textes écrits en code qui nécessitent une **clé cryptographique**, ou un secret, et un algorithme d'accompagnement pour déverrouiller. Ce processus de déverrouillage d'un ciphertext est connu sous le nom de **décryptage**, tandis que le processus de verrouillage est connu sous le nom d'**encryptage**. (Comme expliqué dans le Chapitre 3, le terme cipher peut prendre diverses significations. Dans le nom "Beale ciphers", il est court pour ciphertexts.)
Les trois ciphertexts que Morriss a trouvés dans la boîte en fer consistent chacun en une série de nombres séparés par des virgules. Selon la note de Beale, ces ciphertexts fournissent séparément l'emplacement du trésor, le contenu du trésor, et une liste de noms avec les héritiers légitimes du trésor et leurs parts (cette dernière information étant pertinente au cas où Beale et ses associés ne viendraient jamais réclamer la boîte).

Morris a tenté de décrypter les trois ciphertexts pendant vingt ans. Cela aurait été facile avec la clé. Mais Morriss n'avait pas la clé et n'a pas réussi dans ses tentatives de récupérer les textes originaux, ou **plaintexts** comme ils sont typiquement appelés en cryptographie.

Vers la fin de sa vie, Morriss a passé la boîte à un ami en 1862. Cet ami a par la suite publié un pamphlet en 1885, sous le pseudonyme J.B. Ward. Il comprenait une description de l'histoire (présumée) de la boîte, les trois ciphertexts, et une solution qu'il avait trouvée pour le deuxième ciphertext. (Apparemment, il y a une clé pour chaque ciphertext, et non une clé qui fonctionne sur les trois ciphertexts comme Beale semble l'avoir suggéré dans sa lettre à Morriss.)

Vous pouvez voir le deuxième ciphertext dans la *Figure 2* ci-dessous.<sup>[2](#footnote2)</sup> La clé de ce ciphertext est la Déclaration d'Indépendance des États-Unis. La procédure de décryptage se résume à appliquer les deux règles suivantes :

* Pour tout nombre n dans le ciphertext, localisez le nième mot dans la Déclaration d'Indépendance des États-Unis
* Remplacez le nombre n par la première lettre du mot que vous avez trouvé

*Figure 1 : Beale cipher n° 2*

![Figure 1 : Beale cipher n° 2.](assets/Figure1-1.webp "Figure 1 : Beale cipher n° 2")

Par exemple, le premier nombre du deuxième ciphertext est 115. Le 115ème mot de la Déclaration d'Indépendance est “instituted”, donc la première lettre du plaintext est “i”. Le ciphertext n'indique pas directement les espaces entre les mots et la capitalisation. Mais après avoir décrypté les premiers mots, vous pouvez logiquement déduire que le premier mot du plaintext était simplement “I.” (Le plaintext commence par la phrase “I have deposited in the county of Bedford.”)
Après déchiffrement, le second message fournit le contenu détaillé du trésor (or, argent et bijoux) et suggère qu'il a été enterré dans des pots en fer et recouvert de pierres dans le comté de Bedford (Virginie). Les gens adorent un bon mystère, donc de grands efforts ont été consacrés au déchiffrement des deux autres chiffres de Beale, en particulier celui décrivant l'emplacement du trésor. Même divers cryptographes éminents ont tenté leur chance. Cependant, jusqu'à présent, personne n'a réussi à déchiffrer les deux autres textes chiffrés.

## Cryptographie moderne
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Des histoires colorées telles que celle des chiffres de Beale sont ce que la plupart d'entre nous associent à la cryptographie. Pourtant, la cryptographie moderne diffère d'au moins quatre manières importantes de ces types d'exemples historiques.

Premièrement, historiquement, la cryptographie ne s'est préoccupée que de la **confidentialité**. Les textes chiffrés étaient créés pour garantir que seules certaines parties pouvaient avoir accès aux informations dans les textes en clair, comme dans le cas des chiffres de Beale. Pour qu'un schéma de chiffrement remplisse bien cette fonction, le déchiffrement du texte chiffré ne devrait être possible que si vous avez la clé.

La cryptographie moderne se préoccupe d'un éventail de thèmes plus large que la simple confidentialité. Ces thèmes incluent principalement (1) **l'intégrité du message**—c'est-à-dire, assurer qu'un message n'a pas été modifié ; (2) **l'authenticité du message**—c'est-à-dire, assurer qu'un message provient réellement d'un expéditeur particulier ; et (3) **la non-répudiation**—c'est-à-dire, assurer qu'un expéditeur ne peut pas nier faussement plus tard qu'il a envoyé un message.

Une distinction importante à garder à l'esprit est donc entre un **schéma de chiffrement** et un **schéma cryptographique**. Un schéma de chiffrement ne se préoccupe que de la confidentialité. Alors qu'un schéma de chiffrement est un schéma cryptographique, l'inverse n'est pas vrai. Un schéma cryptographique peut également servir les autres thèmes principaux de la cryptographie, y compris l'intégrité, l'authenticité et la non-répudiation.

Les thèmes de l'intégrité et de l'authenticité sont tout aussi importants que la confidentialité. Nos systèmes de communication modernes ne pourraient pas fonctionner sans garanties concernant l'intégrité et l'authenticité des communications. La non-répudiation est également une préoccupation importante, comme pour les contrats numériques, mais moins omniprésente dans les applications cryptographiques que la confidentialité, l'intégrité et l'authenticité.

Deuxièmement, les schémas de chiffrement classiques tels que les chiffres de Beale impliquent toujours une clé partagée entre toutes les parties concernées. Cependant, de nombreux schémas cryptographiques modernes impliquent non pas une, mais deux clés : une **clé privée** et une **clé publique**. Alors que la première doit rester privée dans toutes les applications, la seconde est généralement de connaissance publique (d'où leurs noms respectifs). Dans le domaine du chiffrement, la clé publique peut être utilisée pour chiffrer le message, tandis que la clé privée peut être utilisée pour le déchiffrer.

La branche de la cryptographie qui traite des schémas où toutes les parties partagent une clé est connue sous le nom de **cryptographie symétrique**. La clé unique dans un tel schéma est généralement appelée la **clé privée** (ou clé secrète). La branche de la cryptographie qui traite des schémas nécessitant une paire de clés privée-publique est connue sous le nom de **cryptographie asymétrique**. Ces branches sont parfois également appelées **cryptographie à clé privée** et **cryptographie à clé publique**, respectivement (bien que cela puisse prêter à confusion, car les schémas cryptographiques à clé publique ont également des clés privées).
L'avènement de la cryptographie asymétrique à la fin des années 1970 a été l'un des événements les plus importants dans l'histoire de la cryptographie. Sans elle, la plupart de nos systèmes de communication modernes, y compris Bitcoin, ne seraient pas possibles, ou du moins seraient très peu pratiques.
Il est important de noter que la cryptographie moderne n'est pas exclusivement l'étude des schémas cryptographiques à clé symétrique et asymétrique (bien que cela couvre une grande partie du domaine). Par exemple, la cryptographie s'intéresse également aux fonctions de hachage et aux générateurs de nombres pseudo-aléatoires, et vous pouvez construire des applications sur ces primitives qui ne sont pas liées à la cryptographie à clé symétrique ou asymétrique.

Troisièmement, les schémas de chiffrement classiques, comme ceux utilisés dans les chiffres de Beale, étaient plus de l'art que de la science. Leur sécurité perçue était largement basée sur des intuitions concernant leur complexité. Ils étaient typiquement corrigés lorsqu'une nouvelle attaque était découverte, ou abandonnés entièrement si l'attaque était particulièrement sévère. La cryptographie moderne, cependant, est une science rigoureuse avec une approche formelle et mathématique tant dans le développement que dans l'analyse des schémas cryptographiques.<sup>[5](#footnote5)</sup>

Plus précisément, la cryptographie moderne se concentre sur des **preuves formelles de sécurité**. Toute preuve de sécurité pour un schéma cryptographique procède en trois étapes :

1. La déclaration d'une **définition cryptographique de la sécurité**, c'est-à-dire un ensemble d'objectifs de sécurité et la menace posée par l'attaquant.
2. La déclaration de toute hypothèse mathématique concernant la complexité computationnelle du schéma. Par exemple, un schéma cryptographique peut contenir un générateur de nombres pseudo-aléatoires. Bien que nous ne puissions pas prouver leur existence, nous pouvons supposer qu'ils existent.
3. L'exposition d'une **preuve mathématique de sécurité** du schéma sur la base de la notion formelle de sécurité et de toute hypothèse mathématique.

Quatrièmement, alors qu'historiquement la cryptographie était principalement utilisée dans des contextes militaires, elle a fini par imprégner nos activités quotidiennes à l'ère numérique. Que vous fassiez des opérations bancaires en ligne, postiez sur les réseaux sociaux, achetiez un produit sur Amazon avec votre carte de crédit, ou envoyiez un pourboire en bitcoin à un ami, la cryptographie est la condition sine qua non de notre ère numérique.

Étant donné ces quatre aspects de la cryptographie moderne, nous pourrions caractériser la **cryptographie** moderne comme la science concernée par le développement formel et l'analyse de schémas cryptographiques pour sécuriser les informations numériques contre les attaques adverses.<sup>[6](#footnote6)</sup> La sécurité ici doit être comprise au sens large comme la prévention des attaques qui nuisent à la confidentialité, à l'intégrité, à l'authentification et/ou à la non-répudiation dans les communications.

La cryptographie est mieux perçue comme une sous-discipline de la **cybersécurité**, qui est préoccupée par la prévention du vol, des dommages et de l'abus des systèmes informatiques. Notez que de nombreuses préoccupations en matière de cybersécurité ont peu ou seulement un lien partiel avec la cryptographie.

Par exemple, si une entreprise possède localement des serveurs coûteux, elle peut être préoccupée par la sécurisation de ce matériel contre le vol et les dommages. Bien que cela soit une préoccupation de cybersécurité, cela a peu à voir avec la cryptographie.

Pour un autre exemple, les **attaques par hameçonnage** sont un problème courant à notre époque moderne. Ces attaques tentent de tromper les gens via un e-mail ou un autre moyen de messagerie pour qu'ils renoncent à des informations sensibles telles que des mots de passe ou des numéros de carte de crédit. Bien que la cryptographie puisse aider à adresser les attaques par hameçonnage dans une certaine mesure, une approche globale nécessite plus que l'utilisation de la cryptographie.


## Communications ouvertes
<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

La cryptographie moderne est conçue pour fournir des assurances de sécurité dans un environnement de **communications ouvertes**. Si notre canal de communication est si bien protégé que les écouteurs n'ont aucune chance de manipuler ou même d'observer nos messages, alors la cryptographie est superflue. La plupart de nos canaux de communication, cependant, sont loin d'être aussi bien gardés.
L'épine dorsale de la communication dans le monde moderne est un vaste réseau de câbles à fibre optique. Passer des appels téléphoniques, regarder la télévision et naviguer sur le web dans un foyer moderne dépend généralement de ce réseau de câbles à fibre optique (un petit pourcentage peut dépendre purement des satellites). Il est vrai que vous pourriez avoir différentes connexions de données dans votre maison, telles que le câble coaxial, la ligne d'abonné numérique (asymétrique) et le câble à fibre optique. Mais, au moins dans le monde développé, ces différents supports de données se rejoignent rapidement à l'extérieur de votre maison vers un nœud dans un vaste réseau de câbles à fibre optique qui connecte le globe entier. Les exceptions sont certaines zones reculées du monde développé, comme aux États-Unis et en Australie, où le trafic de données peut encore également parcourir de longues distances sur des fils de téléphone en cuivre traditionnels.

Il serait impossible d'empêcher les attaquants potentiels d'accéder physiquement à ce réseau de câbles et à son infrastructure de soutien. En fait, nous savons déjà que la plupart de nos données sont interceptées par diverses agences de renseignement nationales à des intersections cruciales de l'Internet.<sup>[7](#footnote7)</sup> Cela inclut tout, des messages Facebook aux adresses de sites web que vous visitez.

Bien que la surveillance des données à grande échelle nécessite un adversaire puissant, tel qu'une agence de renseignement nationale, les attaquants disposant de peu de ressources peuvent facilement tenter d'espionner à une échelle plus locale. Bien que cela puisse se produire au niveau de l'écoute des fils, il est bien plus facile d'intercepter simplement les communications sans fil.

La plupart de nos données de réseau local - que ce soit dans nos maisons, au bureau ou dans un café - voyagent maintenant via des ondes radio vers des points d'accès sans fil sur des routeurs tout-en-un, plutôt que par des câbles physiques. Ainsi, un attaquant a besoin de peu de ressources pour intercepter tout votre trafic local. Cela est particulièrement préoccupant car la plupart des gens font très peu pour protéger les données qui traversent leurs réseaux locaux. De plus, les attaquants potentiels peuvent également cibler nos connexions à large bande mobile, telles que 3G, 4G et 5G. Toutes ces communications sans fil sont une cible facile pour les attaquants.

Par conséquent, l'idée de garder les communications secrètes en protégeant le canal de communication est une aspiration désespérément illusoire pour une grande partie du monde moderne. Tout ce que nous savons justifie une paranoïa sévère : vous devriez toujours supposer que quelqu'un écoute. Et la cryptographie est l'outil principal que nous avons pour obtenir une quelconque sécurité dans cet environnement moderne.

### Notes
[^1] : Pour un bon résumé de l'histoire, voir Simon Singh, *The Code Book*, Fourth Estate (Londres, 1999), pp. 82-99. Un court métrage de l'histoire a été réalisé par Andrew Allen en 2010. Vous pouvez trouver le film, “The Thomas Beale Cipher,” sur son site web [^1].

[^2] : Cette image est disponible sur la page Wikipedia pour les chiffres de Beale [^2].

[^3] : Pour être exact, les applications importantes des schémas cryptographiques ont été concernées par le secret. Les enfants, par exemple, utilisent fréquemment des schémas cryptographiques simples pour le « plaisir ». Le secret n'est pas vraiment une préoccupation dans ces cas [^3].

[^4] : Bruce Schneier, *Applied Cryptography*, 2e éd., 2015 (Indianapolis, IN : John Wiley & Sons), p. 2 [^4].

[^5] : Voir Jonathan Katz et Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL : 2015), esp. pp. 16–23, pour une bonne description [^5].

[^6] : Cf. Katz et Lindell, ibid., p. 3. Je pense que leur caractérisation a quelques problèmes, donc présente ici une version légèrement différente de leur déclaration [^6].
[^7]: Voir, par exemple, Olga Khazan, "The creepy, long-standing practice of undersea cable tapping", *The Atlantic*, 16 juillet 2013 (disponible sur [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)) [^7].

# Fondements Mathématiques de la Cryptographie I
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

La cryptographie repose sur les mathématiques. Et si vous souhaitez acquérir une compréhension qui dépasse le niveau superficiel de la cryptographie, vous devez être à l'aise avec ces mathématiques.

Ce chapitre introduit la plupart des mathématiques de base que vous rencontrerez en apprenant la cryptographie. Les sujets incluent les variables aléatoires, les opérations modulo, les opérations XOR et la pseudo-aléatoireité. Vous devriez maîtriser le contenu de ces sections pour toute compréhension non superficielle de la cryptographie.

Le chapitre suivant traite de la théorie des nombres, qui est beaucoup plus complexe.

## Variables aléatoires
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Une variable aléatoire est typiquement notée par une lettre majuscule non en gras. Ainsi, par exemple, nous pourrions parler d'une variable aléatoire X, d'une variable aléatoire Y, ou d'une variable aléatoire Z. C'est la notation que j'emploierai également à partir de maintenant.

Une **variable aléatoire** peut prendre deux valeurs ou plus, chacune avec une certaine probabilité positive. Les valeurs possibles sont répertoriées dans l'**ensemble des résultats**.

Chaque fois que vous **échantillonnez** une variable aléatoire, vous tirez une valeur particulière de son ensemble de résultats selon les probabilités définies.

Prenons un exemple simple. Supposons une variable X qui est définie comme suit :

* X a l'ensemble des résultats {1,2}
* Pr [X = 1] = 0,5
* Pr [X = 2] = 0,5

Il est facile de voir que X est une variable aléatoire. Premièrement, il y a deux valeurs possibles ou plus que X peut prendre, à savoir 1 et 2. Deuxièmement, chaque valeur possible a une probabilité positive de se produire chaque fois que vous échantillonnez X, à savoir 0,5.

Tout ce qu'une variable aléatoire nécessite est un ensemble de résultats avec deux possibilités ou plus, où chaque possibilité a une probabilité positive de se produire lors de l'échantillonnage. En principe, alors, une variable aléatoire peut être définie de manière abstraite, dépourvue de tout contexte. Dans ce cas, vous pourriez penser à l'« échantillonnage » comme à la réalisation d'une expérience naturelle pour déterminer la valeur de la variable aléatoire.

La variable X ci-dessus a été définie de manière abstraite. Ainsi, vous pourriez penser à échantillonner la variable X ci-dessus en lançant une pièce de monnaie équitable et en attribuant « 2 » dans le cas d'un pile et « 1 » dans le cas d'un face. Pour chaque échantillon de X, vous lancez à nouveau la pièce.

Alternativement, vous pourriez également penser à échantillonner X, en lançant un dé équitable et en attribuant « 2 » dans le cas où le dé atterrit sur 1, 3, ou 4, et en attribuant « 1 » dans le cas où le dé atterrit sur 2, 5, ou 6. Chaque fois que vous échantillonnez X, vous lancez à nouveau le dé.

Vraiment, toute expérience naturelle qui vous permettrait de définir les probabilités des valeurs possibles de X ci-dessus peut être imaginée par rapport au tirage.
Souvent, cependant, les variables aléatoires ne sont pas seulement introduites de manière abstraite. Au lieu de cela, l'ensemble des valeurs de résultat possibles a une signification concrète dans le monde réel (plutôt que de n'être que des nombres). De plus, ces valeurs de résultat pourraient être définies par rapport à un type spécifique d'expérience (plutôt que comme n'importe quelle expérience naturelle avec ces valeurs).
Considérons maintenant un exemple de variable X qui n'est pas définie de manière abstraite. X est définie comme suit afin de déterminer quelle équipe de deux commence un match de football :

* X a l'ensemble de résultat {coup d'envoi rouge, coup d'envoi bleu}
* Lancez une pièce de monnaie particulière C : pile = "coup d'envoi rouge" ; face = "coup d'envoi bleu"
* Pr [X = coup d'envoi rouge] = 0.5
* Pr [X = coup d'envoi bleu] = 0.5

Dans ce cas, l'ensemble de résultat de X est fourni avec une signification concrète, à savoir quelle équipe commence dans un match de football. De plus, les résultats possibles et leurs probabilités associées sont déterminés par une expérience concrète, à savoir le lancer d'une pièce de monnaie particulière C.

Dans les discussions sur la cryptographie, les variables aléatoires sont généralement introduites par rapport à un ensemble de résultats ayant une signification réelle. Il pourrait s'agir de l'ensemble de tous les messages qui pourraient être cryptés, connu sous le nom d'espace de message, ou l'ensemble de toutes les clés que les parties utilisant le cryptage peuvent choisir, connu sous le nom d'espace de clé.

Cependant, dans les discussions sur la cryptographie, les variables aléatoires ne sont généralement pas définies par rapport à une expérience naturelle spécifique, mais par rapport à toute expérience qui pourrait produire les bonnes distributions de probabilité.

Les variables aléatoires peuvent avoir des distributions de probabilité discrètes ou continues. Les variables aléatoires avec une **distribution de probabilité discrète** — c'est-à-dire, les variables aléatoires discrètes — ont un nombre fini de résultats possibles. La variable aléatoire X dans les deux exemples donnés jusqu'à présent était discrète.

**Les variables aléatoires continues** peuvent au contraire prendre des valeurs dans un ou plusieurs intervalles. Vous pourriez dire, par exemple, qu'une variable aléatoire, lors d'un échantillonnage, prendra n'importe quelle valeur réelle entre 0 et 1, et que chaque nombre réel dans cet intervalle est également probable. Dans cet intervalle, il y a une infinité de valeurs possibles.

Pour les discussions cryptographiques, vous aurez seulement besoin de comprendre les variables aléatoires discrètes. Toute discussion sur les variables aléatoires à partir de maintenant devrait donc être comprise comme se référant aux variables aléatoires discrètes, sauf indication contraire spécifique.

### Représentation graphique des variables aléatoires

Les valeurs possibles et les probabilités associées pour une variable aléatoire peuvent être facilement visualisées à travers un graphique. Par exemple, considérez la variable aléatoire X de la section précédente avec un ensemble de résultat de {1,2}, et Pr [X = 1] = 0.5 et Pr [X = 2] = 0.5. Nous afficherions typiquement une telle variable aléatoire sous forme de graphique à barres comme dans *Figure 1*.

*Figure 1 : Variable aléatoire X*

![Figure 1 : Variable aléatoire X.](assets/Figure2-1.webp)

Les larges barres dans *Figure 1* ne signifient évidemment pas suggérer que la variable aléatoire X est en réalité continue. Au lieu de cela, les barres sont rendues larges afin d'être plus visuellement attrayantes (juste une ligne droite vers le haut offre une visualisation moins intuitive).

### Variables uniformes

Dans l'expression "variable aléatoire", le terme "aléatoire" signifie simplement "probabiliste". En d'autres termes, cela signifie simplement que deux résultats possibles ou plus de la variable se produisent avec certaines probabilités. Ces résultats, cependant, ne doivent *pas nécessairement* être également probables (bien que le terme "aléatoire" puisse en effet avoir ce sens dans d'autres contextes).
Une **variable uniforme** est un cas particulier d'une variable aléatoire. Elle peut prendre deux valeurs ou plus, toutes avec une probabilité égale. La variable aléatoire X représentée dans la *Figure 1* est clairement une variable uniforme, puisque les deux issues possibles se produisent avec une probabilité de 0,5. Il existe cependant de nombreuses variables aléatoires qui ne sont pas des instances de variables uniformes.
Considérez, par exemple, la variable aléatoire Y. Elle a un ensemble de résultats {1,2,3,8,10} et la distribution de probabilité suivante : Pr [Y = 1] = 0,25 ; Pr [Y = 2] = 0,35 ; Pr [Y = 3] = 0,1 ; Pr [Y = 8] = 0,25 ; Pr [Y = 10] = 0,05.

Bien que deux résultats possibles aient en effet une probabilité égale de se produire, à savoir 1 et 8, Y peut également prendre certaines valeurs avec des probabilités différentes de 0,25 lors de l'échantillonnage. Par conséquent, bien que Y soit effectivement une variable aléatoire, ce n'est pas une variable uniforme.

Une représentation graphique de Y est fournie dans la *Figure 2*.

*Figure 2 : Variable aléatoire Y*

![Figure 2 : Variable aléatoire Y.](assets/Figure2-2.webp "Figure 2 : Variable aléatoire Y")

Pour un dernier exemple, considérez la variable aléatoire Z. Elle a l'ensemble de résultats {1,3,7,11,12} et la distribution de probabilité suivante : Pr (2) = 0,2 ; Pr (3) = 0,2 ; Pr (9) = 0,2 ; Pr (11) = 0,2 ; Pr (12) = 0,2. Vous pouvez la voir représentée dans la Figure 3. La variable aléatoire Z est, contrairement à Y, effectivement une variable uniforme, car toutes les probabilités pour les valeurs possibles lors de l'échantillonnage sont égales.

*Figure 3 : Variable aléatoire Z*

![Figure 3 : Variable aléatoire Z.](assets/Figure2-3.webp "Figure 3 : Variable aléatoire Z")


### Probabilité conditionnelle

Supposons que Bob ait l'intention de sélectionner uniformément un jour de la dernière année calendaire. Que devrions-nous conclure être la probabilité que le jour sélectionné soit en été ?

Tant que nous pensons que le processus de Bob sera effectivement vraiment uniforme, nous devrions conclure qu'il y a une probabilité de 1/4 que Bob sélectionne un jour en été. C'est la **probabilité inconditionnelle** que le jour sélectionné aléatoirement soit en été.

Supposons maintenant qu'au lieu de tirer uniformément un jour du calendrier, Bob ne sélectionne uniformément que parmi les jours où la température de midi au lac Crystal (New Jersey) était de 21 degrés Celsius ou plus. Étant donné ces informations supplémentaires, que pouvons-nous conclure sur la probabilité que Bob sélectionne un jour en été ?

Nous devrions vraiment tirer une conclusion différente de celle d'avant, même sans aucune information spécifique supplémentaire (par exemple, la température à midi chaque jour de l'année dernière).

Sachant que le lac Crystal se trouve dans le New Jersey, nous ne nous attendrions certainement pas à ce que la température à midi soit de 21 degrés Celsius ou plus en hiver. Au lieu de cela, il est beaucoup plus probable qu'il s'agisse d'un jour chaud au printemps ou en automne, ou d'un jour quelque part en été. Par conséquent, sachant que la température de midi au lac Crystal le jour sélectionné était de 21 degrés Celsius ou plus, la probabilité que le jour sélectionné par Bob soit en été devient beaucoup plus élevée. C'est la **probabilité conditionnelle** que le jour sélectionné aléatoirement soit en été, étant donné que la température de midi au lac Crystal était de 21 degrés Celsius ou plus.
Contrairement à l'exemple précédent, les probabilités de deux événements peuvent également être complètement indépendantes. Dans ce cas, nous disons qu'ils sont **indépendants**.
Supposons, par exemple, qu'une certaine pièce équitable ait atterri sur face. Étant donné ce fait, quelle est alors la probabilité qu'il pleuve demain ? La probabilité conditionnelle dans ce cas devrait être la même que la probabilité inconditionnelle qu'il pleuve demain, car un lancer de pièce n'a généralement aucun impact sur le temps.

Nous utilisons un symbole “|” pour écrire les déclarations de probabilité conditionnelle. Par exemple, la probabilité de l'événement A étant donné que l'événement B s'est produit peut être écrite comme suit : Pr[A|B]. Ainsi, lorsque deux événements, A et B, sont indépendants, alors Pr[A|B] = Pr[A] et Pr[B|A] = Pr[B]. La condition d'indépendance peut être simplifiée comme suit : Pr[A,B] = Pr[A]*Pr[B].

Un résultat clé en théorie des probabilités est connu sous le nom de **Théorème de Bayes**. Il stipule essentiellement que Pr[A|B] peut être réécrit comme suit :

Pr[A|B] = (Pr[B|A] • Pr[A]) / Pr[B]

Au lieu d'utiliser des probabilités conditionnelles avec des événements spécifiques, nous pouvons également examiner les probabilités conditionnelles impliquées avec deux ou plusieurs variables aléatoires sur un ensemble d'événements possibles. Supposons deux variables aléatoires, X et Y. Nous pouvons désigner toute valeur possible pour X par x, et toute valeur possible pour Y par y. Nous pourrions dire, alors, que deux variables aléatoires sont indépendantes si l'énoncé suivant est vrai :

Pr[X = x,Y = y] = Pr[X = x] • Pr[Y = y] pour tous x et y

Soyons un peu plus explicites sur ce que signifie cet énoncé.

Supposons que les ensembles de résultats pour X et Y soient définis comme suit : **X** = {x<sub>1</sub>,x<sub>2</sub>….,x<sub>i</sub>,….x<sub>n</sub>} et **Y** = {y<sub>1</sub>,y<sub>2</sub>….,y<sub>i</sub>,….y<sub>m</sub>}. (Il est typique d'indiquer les ensembles de valeurs par des lettres en gras et majuscules.)

Maintenant, supposons que vous échantillonnez Y et observez y<sub>1</sub>. L'énoncé ci-dessus nous dit que la probabilité d'obtenir maintenant x<sub>1</sub> en échantillonnant X est exactement la même que si nous n'avions jamais observé y<sub>1</sub>. Cela est vrai pour n'importe quel y<sub>i</sub> que nous aurions pu tirer de notre échantillonnage initial de Y. Enfin, cela reste vrai non seulement pour x<sub>1</sub>. Pour n'importe quel x<sub>i</sub>, la probabilité de se produire n'est pas influencée par le résultat d'un échantillonnage de Y. Tout cela s'applique également dans le cas où X est échantillonné en premier.

Terminons notre discussion sur un point un peu plus philosophique. Dans toute situation réelle, la probabilité d'un événement est toujours évaluée par rapport à un ensemble particulier d'informations. Il n'y a pas de "probabilité inconditionnelle" dans un sens très strict du terme.

Par exemple, supposons que je vous demande la probabilité que les cochons volent d'ici 2030. Bien que je ne vous donne aucune information supplémentaire, vous savez clairement beaucoup de choses sur le monde qui peuvent influencer votre jugement. Vous n'avez jamais vu de cochons voler. Vous savez que la plupart des gens ne s'attendent pas à ce qu'ils volent. Vous savez qu'ils ne sont pas vraiment faits pour voler. Et ainsi de suite.
Ainsi, lorsque nous parlons d'une "probabilité inconditionnelle" d'un certain événement dans un contexte réel, ce terme ne peut vraiment avoir de sens que si nous le considérons comme signifiant quelque chose comme "la probabilité sans aucune information explicite supplémentaire". Toute compréhension d'une "probabilité conditionnelle" devrait alors toujours être interprétée par rapport à une information spécifique.
Je pourrais, par exemple, vous demander la probabilité que les cochons volent d'ici 2030, après vous avoir donné des preuves que certaines chèvres en Nouvelle-Zélande ont appris à voler après quelques années d'entraînement. Dans ce cas, vous ajusterez probablement votre jugement sur la probabilité que les cochons volent d'ici 2030. Ainsi, la probabilité que les cochons volent d'ici 2030 est conditionnelle à cette preuve concernant les chèvres en Nouvelle-Zélande.

## L'opération modulo
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

L'expression la plus basique avec l'**opération modulo** est de la forme suivante : x mod y.

La variable x est appelée le dividende et la variable y le diviseur. Pour effectuer une opération modulo avec un dividende positif et un diviseur positif, vous déterminez simplement le reste de la division.

Par exemple, considérez l'expression 25 mod 4. Le nombre 4 rentre dans le nombre 25 un total de 6 fois. Le reste de cette division est 1. Donc, 25 mod 4 égale 1. De manière similaire, nous pouvons évaluer les expressions ci-dessous :

* 29 mod 30 = 29 (car 30 rentre dans 29 un total de 0 fois et le reste est 29)
* 42 mod 2 = 0 (car 2 rentre dans 42 un total de 21 fois et le reste est 0)
* 12 mod 5 = 2 (car 5 rentre dans 12 un total de 2 fois et le reste est 2)
* 20 mod 8 = 4 (car 8 rentre dans 20 un total de 2 fois et le reste est 4)

Lorsque le dividende ou le diviseur est négatif, les opérations modulo peuvent être traitées différemment par les langages de programmation.

Vous rencontrerez certainement des cas avec un dividende négatif en cryptographie. Dans ces cas, l'approche typique est la suivante :

* Déterminez d'abord la valeur la plus proche *inférieure ou égale* au dividende dans laquelle le diviseur divise avec un reste de zéro. Appelez cette valeur p.
* Si le dividende est x, alors le résultat de l'opération modulo est la valeur de x – p.

Par exemple, supposons que le dividende soit – 20 et le diviseur 3. La valeur la plus proche inférieure ou égale à – 20 dans laquelle 3 divise uniformément est – 21. La valeur de x – p dans ce cas est – 20 – – 21. Cela égale 1 et, donc, – 20 mod 3 égale 1. De manière similaire, nous pouvons évaluer les expressions ci-dessous :

* – 8 mod 5 = 2
* – 19 mod 16 = 13
* – 14 mod 6 = 4

Concernant la notation, vous verrez typiquement les types d'expressions suivants : x = [y mod z]. En raison des crochets, l'opération modulo dans ce cas s'applique uniquement au côté droit de l'expression. Si y égale 25 et z égale 4, par exemple, alors x s'évalue à 1.
Sans les crochets, l'opération modulo agit sur *les deux côtés* d'une expression. Supposons, par exemple, l'expression suivante : x = y mod z. Si y vaut 25 et z vaut 4, alors tout ce que nous savons, c'est que x mod 4 évalue à 1. Cela est cohérent avec n'importe quelle valeur pour x de l'ensemble {….– 7, – 3, 1, 5, 9….}.
La branche des mathématiques qui implique des opérations modulo sur les nombres et les expressions est appelée **arithmétique modulaire**. Vous pouvez considérer cette branche comme de l'arithmétique pour les cas où la ligne des nombres n'est pas infiniment longue. Bien que nous rencontrions typiquement des opérations modulo pour les entiers (positifs) en cryptographie, vous pouvez également effectuer des opérations modulo en utilisant n'importe quels nombres réels.

### Le chiffre de César

L'opération modulo est fréquemment rencontrée en cryptographie. Pour illustrer, considérons l'un des schémas de chiffrement historiques les plus célèbres : le chiffre de César.

Définissons-le d'abord. Supposons un dictionnaire *D* qui équivaut toutes les lettres de l'alphabet anglais, dans l'ordre, avec l'ensemble de nombres {0,1,2…,25}. Supposons un espace de message **M**. Le **chiffre de César** est, alors, un schéma de chiffrement défini comme suit :

- Sélectionnez uniformément une clé k de l'espace de clés **K**, où **K** = {0,1,2,…,25}<sup>[1](#footnote1)</sup>
- Chiffrez un message m є **M**, comme suit :
    - Séparez m en ses lettres individuelles m<sub>0</sub>, m<sub>1</sub>,….m<sub>i</sub>….,m<sub>l</sub>
    - Convertissez chaque m<sub>i</sub> en un nombre selon *D*
    - Pour chaque m<sub>i</sub>, c<sub>i</sub> = [(m<sub>i</sub> + k) mod 26]
    - Convertissez chaque c<sub>i</sub> en une lettre selon *D*
    - Puis combinez c<sub>0</sub>, c<sub>1</sub>,….,c<sub>l</sub> pour obtenir le texte chiffré c
- Déchiffrez un texte chiffré c comme suit :
    -- Convertissez chaque c<sub>i</sub> en un nombre selon *D*
    -- Pour chaque c<sub>i</sub>, m<sub>i</sub> = [(c<sub>i</sub> – k) mod 26]
    -- Convertissez chaque m<sub>i</sub> en une lettre selon *D*
    -- Puis combinez m<sub>0</sub>, m<sub>1</sub>,….,m<sub>l</sub> pour obtenir le message original m

L'opérateur modulo dans le chiffre de César assure que les lettres bouclent, de sorte que toutes les lettres du texte chiffré sont définies. Pour illustrer, considérons l'application du chiffre de César sur le mot “DOG”.

Supposons que vous avez sélectionné uniformément une clé ayant la valeur de 17. La lettre “O” équivaut à 15. Sans l'opération modulo, l'addition de ce nombre de texte en clair avec la clé donnerait un nombre de texte chiffré de 32. Cependant, ce nombre de texte chiffré ne peut pas être transformé en lettre de texte chiffré, car l'alphabet anglais n'a que 26 lettres. L'opération modulo assure que le nombre de texte chiffré est en fait 6 (le résultat de 32 mod 26), ce qui équivaut à la lettre de texte chiffré “G”.

Le chiffrement complet du mot “DOG” avec une valeur de clé de 17 est le suivant :
* Message = CHIEN = C,H,I,E,N = 3,8,9,5,14* c<sub>0</sub> = [(3 + 17) Mod 26] = [(20) Mod 26] = 20 = U
* c<sub>1</sub> = [(8 + 17) Mod 26] = [(25) Mod 26] = 25 = Z
* c<sub>2</sub> = [(9 + 17) Mod 26] = [(26) Mod 26] = 0 = A
* c<sub>3</sub> = [(5 + 17) Mod 26] = [(22) Mod 26] = 22 = W
* c<sub>4</sub> = [(14 + 17) Mod 26] = [(31) Mod 26] = 5 = F
* c = UZAWF

Tout le monde peut intuitivement comprendre comment fonctionne le chiffrement par décalage et probablement l'utiliser eux-mêmes. Cependant, pour approfondir vos connaissances en cryptographie, il est important de commencer à se familiariser avec la formalisation, car les schémas deviendront beaucoup plus difficiles. D'où la raison pour laquelle les étapes du chiffrement par décalage ont été formalisées.

## L'opération XOR
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Toutes les données informatiques sont traitées, stockées et envoyées à travers les réseaux au niveau des bits. Tous les schémas cryptographiques appliqués aux données informatiques fonctionnent également au niveau des bits.

Par exemple, supposons que vous avez tapé un e-mail dans votre application de messagerie. Tout chiffrement que vous appliquez ne se produit pas directement sur les caractères ASCII de votre e-mail. Au lieu de cela, il est appliqué à la représentation binaire des lettres et autres symboles de votre e-mail.

Une opération mathématique clé à comprendre pour la cryptographie moderne, outre l'opération modulo, est celle de l'**opération XOR**, ou opération "ou exclusif". Cette opération prend en entrée deux bits et produit en sortie un autre bit. L'opération XOR sera simplement désignée par "XOR". Elle donne 0 si les deux bits sont identiques et 1 si les deux bits sont différents. Vous pouvez voir les quatre possibilités ci-dessous.

* 0 XOR 0 = 0
* 0 XOR 1 = 1
* 1 XOR 0 = 1
* 1 XOR 1 = 0

Vous pouvez effectuer une opération XOR sur deux messages plus longs qu'un seul bit en alignant les bits de ces deux messages et en effectuant l'opération XOR sur chaque paire individuelle de bits.

Pour illustrer, supposons que vous avez un message m<sub>1</sub> (01111001) et un message m<sub>2</sub> (01011001). L'opération XOR de ces deux messages peut être vue ci-dessous.

* m<sub>1</sub> XOR m<sub>2</sub> = 01111001 XOR 01011001 = 00100000

Le processus est simple. Vous effectuez d'abord le XOR des bits les plus à gauche de m<sub>1</sub> et m<sub>2</sub>. Dans ce cas, cela donne 0 XOR 0 = 0. Vous effectuez ensuite le XOR de la deuxième paire de bits en partant de la gauche. Dans ce cas, cela donne 1 XOR 1 = 0. Vous continuez ce processus jusqu'à avoir effectué l'opération XOR sur les bits les plus à droite.
Il est facile de voir que l'opération XOR est commutative, c'est-à-dire que m<sub>1</sub> XOR m<sub>2</sub> = m<sub>2</sub> XOR m<sub>1</sub>. De plus, l'opération XOR est également associative. Cela signifie que (m<sub>1</sub> XOR m<sub>2</sub>) XOR m<sub>3</sub> = m<sub>1</sub> XOR (m<sub>2</sub> XOR m<sub>3</sub>).
Une opération XOR sur deux chaînes de longueurs alternatives peut avoir différentes interprétations, selon le contexte. Nous ne nous préoccuperons pas ici des opérations XOR sur des chaînes de longueurs différentes.

Une opération XOR est équivalente au cas spécial de l'exécution d'une opération modulo sur l'addition de bits lorsque le diviseur est 2. Vous pouvez voir l'équivalence dans les résultats suivants :

* (0 + 0) mod 2 = 0 XOR 0 = 0
* (1 + 0) mod 2 = 1 XOR 0 = 1
* (0 + 1) mod 2 = 0 XOR 1 = 1
* (1 + 1) mod 2 = 1 XOR 1 = 0

## Pseudo-aléatoire
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

Dans notre discussion sur les variables aléatoires et uniformes, nous avons fait une distinction spécifique entre "aléatoire" et "uniforme". Cette distinction est généralement maintenue en pratique lors de la description des variables aléatoires. Cependant, dans notre contexte actuel, cette distinction doit être abandonnée et "aléatoire" et "uniforme" sont utilisés de manière synonyme. J'expliquerai pourquoi à la fin de cette section.

Pour commencer, nous pouvons appeler une chaîne binaire de longueur n **aléatoire** (ou **uniforme**), si elle était le résultat de l'échantillonnage d'une variable uniforme S qui donne à chaque chaîne binaire de cette longueur n une probabilité égale de sélection.

Supposons, par exemple, l'ensemble de toutes les chaînes binaires de longueur 8 : {0000 0000, 0000 0001,…, 1111 1111}. (Il est typique d'écrire une chaîne de 8 bits en deux quatuors, chacun appelé un **nibble**.) Appelons cet ensemble de chaînes **S<sub>8</sub>**.

Selon la définition ci-dessus, nous pouvons alors appeler une chaîne binaire particulière de longueur 8 aléatoire (ou uniforme), si elle était le résultat de l'échantillonnage d'une variable uniforme S qui donne à chaque chaîne dans **S<sub>8</sub>** une probabilité égale de sélection. Étant donné que l'ensemble **S<sub>8</sub>** comprend 2<sup>8</sup> éléments, la probabilité de sélection lors de l'échantillonnage devrait être de 1/2<sup>8</sup> pour chaque chaîne de l'ensemble.

Un aspect clé de l'aléatoire d'une chaîne binaire est qu'il est défini en référence au processus par lequel elle a été sélectionnée. La forme de toute chaîne binaire particulière en elle-même ne révèle donc rien sur son aléatoire dans la sélection.

Par exemple, beaucoup de gens ont intuitivement l'idée qu'une chaîne comme 1111 1111 n'aurait pas pu être sélectionnée de manière aléatoire. Mais cela est clairement faux.
Définissant une variable uniforme S sur toutes les chaînes binaires de longueur 8, la probabilité de sélectionner 1111 1111 de l'ensemble **S<sub>8</sub>** est la même que celle d'une chaîne telle que 0111 01001. Ainsi, vous ne pouvez rien dire sur l'aléatoire d'une chaîne, juste en analysant la chaîne elle-même.
Nous pouvons également parler de chaînes aléatoires sans spécifiquement signifier des chaînes binaires. Nous pourrions, par exemple, parler d'une chaîne hexadécimale aléatoire AF 02 82. Dans ce cas, la chaîne aurait été sélectionnée au hasard parmi l'ensemble de toutes les chaînes hexadécimales de longueur 6. Cela équivaut à sélectionner au hasard une chaîne binaire de longueur 24, puisque chaque chiffre hexadécimal représente 4 bits.

Typiquement, l'expression « une chaîne aléatoire », sans qualification, fait référence à une chaîne sélectionnée au hasard parmi l'ensemble de toutes les chaînes de même longueur. C'est ainsi que je l'ai décrit ci-dessus. Une chaîne de longueur n peut, bien sûr, également être sélectionnée au hasard dans un ensemble différent. Un, par exemple, qui ne constitue qu'un sous-ensemble de toutes les chaînes de longueur n, ou peut-être un ensemble qui inclut des chaînes de longueurs variées. Dans ces cas, cependant, nous ne nous référerions pas à elle comme à une « chaîne aléatoire », mais plutôt « une chaîne qui est sélectionnée au hasard dans un certain ensemble **S** ».

Un concept clé en cryptographie est celui de la pseudorandomness. Une **chaîne pseudorandom** de longueur n semble *comme si* elle était le résultat de l'échantillonnage d'une variable uniforme S qui donne à chaque chaîne dans **S<sub>n</sub>** une probabilité égale de sélection. En fait, cependant, la chaîne est le résultat de l'échantillonnage d'une variable uniforme S' qui ne définit qu'une distribution de probabilité — pas nécessairement une avec des probabilités égales pour tous les résultats possibles — sur un sous-ensemble de **S<sub>n</sub>**. Le point crucial ici est que personne ne peut vraiment distinguer entre des échantillons de S et S', même si vous en prenez beaucoup.

Supposons, par exemple, une variable aléatoire S. Son ensemble de résultats est **S<sub>256</sub>**, c'est l'ensemble de toutes les chaînes binaires de longueur 256. Cet ensemble a 2<sup>256</sup> éléments. Chaque élément a une probabilité égale de sélection, 1/2<sup>256</sup>, lors de l'échantillonnage.

Supposons en plus une variable aléatoire S’. Son ensemble de résultats inclut seulement 2<sup>128</sup> chaînes binaires de longueur 256. Il a une certaine distribution de probabilité sur ces chaînes, mais cette distribution n'est pas nécessairement uniforme.

Supposons que j'ai maintenant pris 1000s d'échantillons de S et 1000s d'échantillons de S' et que j'ai donné les deux ensembles de résultats à vous. Je vous dis quel ensemble de résultats est associé à quelle variable aléatoire. Ensuite, je prends un échantillon de l'une des deux variables aléatoires. Mais cette fois, je ne vous dis pas de quelle variable aléatoire je prends l'échantillon. Si S' était pseudorandom, alors l'idée est que votre probabilité de faire le bon choix quant à la variable aléatoire que j'ai échantillonnée est pratiquement pas meilleure que 1/2.

Typiquement, une chaîne pseudorandom de longueur n est produite en sélectionnant au hasard une chaîne de taille n – x, où x est un entier positif, et en l'utilisant comme entrée pour un algorithme d'expansion. Cette chaîne aléatoire de taille n – x est connue sous le nom de **graine**.
Les chaînes pseudorandom sont un concept clé pour rendre la cryptographie pratique. Considérez, par exemple, les chiffrements en flux. Avec un chiffrement en flux, une clé sélectionnée aléatoirement est insérée dans un algorithme d'expansion pour produire une chaîne pseudorandom beaucoup plus grande. Cette chaîne pseudorandom est ensuite combinée avec le texte en clair via une opération XOR pour produire un texte chiffré.
Si nous étions incapables de produire ce type de chaîne pseudorandom pour un chiffrement en flux, alors nous aurions besoin d'une clé aussi longue que le message pour sa sécurité. Ce n'est pas une option très pratique dans la plupart des cas.

La notion de pseudorandomness discutée dans cette section peut être définie de manière plus formelle. Elle s'étend également à d'autres contextes. Mais il n'est pas nécessaire de plonger dans cette discussion ici. Tout ce que vous avez vraiment besoin de comprendre intuitivement pour une grande partie de la cryptographie est la différence entre une chaîne aléatoire et une chaîne pseudorandom.<sup>[2](#footnote2)</sup>

La raison pour laquelle nous abandonnons la distinction entre « aléatoire » et « uniforme » dans notre discussion devrait maintenant être également claire. En pratique, tout le monde utilise le terme pseudorandom pour indiquer une chaîne qui semble **comme si** elle était le résultat d'un échantillonnage d'une variable uniforme S. Strictement parlant, nous devrions appeler une telle chaîne « pseudo-uniforme », adoptant notre langage d'antérieurement. Comme le terme « pseudo-uniforme » est à la fois lourd et non utilisé par quiconque, nous ne l'introduirons pas ici pour plus de clarté. Au lieu de cela, nous abandonnons simplement la distinction entre « aléatoire » et « uniforme » dans le contexte actuel.

## Notes
<chapterId>7cccd92c-15bc-5394-9024-af126988ecd7</chapterId>

[^1]: Nous pouvons définir cette déclaration exactement, en utilisant la terminologie de la section précédente. Laissez une variable uniforme K avoir **K** comme son ensemble de résultats possibles. Ainsi Pr [K = 0] = 1/26, Pr [K = 1] = 1/26, et ainsi de suite. Échantillonnez la variable uniforme K une fois pour produire une clé particulière [^1].

[^2]: Si vous êtes intéressé par une exposition plus formelle sur ces sujets, vous pouvez consulter l'*Introduction à la Cryptographie Moderne* de Katz et Lindell, en particulier le chapitre 3 [^2].

# Fondements Mathématiques de la Cryptographie II
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

Ce chapitre couvre un sujet plus avancé sur les fondements mathématiques de la cryptographie : la théorie des nombres. Bien que la théorie des nombres soit importante pour la cryptographie symétrique (comme dans le Chiffre de Rijndael), elle est particulièrement importante dans le contexte de la cryptographie à clé publique.

Si vous trouvez les détails de la théorie des nombres fastidieux, je recommanderais une lecture de haut niveau la première fois. Vous pouvez toujours y revenir à un moment ultérieur.

## Qu'est-ce que la théorie des nombres ?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>

Vous pourriez caractériser la **théorie des nombres** comme l'étude des propriétés des entiers et des fonctions mathématiques qui travaillent avec les entiers.

Considérez, par exemple, que deux nombres a et N sont des **coprimes** (ou **primes relatifs**) si leur plus grand diviseur commun égale 1. Supposons maintenant un entier particulier N. Combien d'entiers plus petits que N sont des coprimes avec N ? Peut-on faire des déclarations générales sur les réponses à cette question ? Ce sont les types typiques de questions que la théorie des nombres cherche à répondre.
La théorie moderne des nombres repose sur les outils de l'algèbre abstraite. Le domaine de l'**algèbre abstraite** est une sous-discipline des mathématiques où les principaux objets d'analyse sont des objets abstraits connus sous le nom de structures algébriques. Une **structure algébrique** est un ensemble d'éléments conjugués avec une ou plusieurs opérations, qui respectent certains axiomes. À travers les structures algébriques, les mathématiciens peuvent obtenir des aperçus sur des problèmes mathématiques spécifiques, en faisant abstraction de leurs détails.
Le domaine de l'algèbre abstraite est parfois également appelé algèbre moderne. Vous pouvez également rencontrer le concept de **mathématiques abstraites** (ou **mathématiques pures**). Ce dernier terme ne fait pas référence à l'algèbre abstraite, mais signifie plutôt l'étude des mathématiques pour elles-mêmes, et pas seulement en vue d'applications potentielles.

Les ensembles de l'algèbre abstraite peuvent traiter de nombreux types d'objets, des transformations préservant la forme sur un triangle équilatéral aux motifs de papier peint. Pour la théorie des nombres, nous ne considérons que des ensembles d'éléments qui contiennent des entiers ou des fonctions qui travaillent avec des entiers.

## Groupes
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Un concept de base en mathématiques est celui d'un ensemble d'éléments. Un ensemble est généralement noté par des signes d'accolade avec les éléments séparés par des virgules.

Par exemple, l'ensemble de tous les entiers est {…,-2,-1,0,1,2,…}. Les points de suspension signifient ici qu'un certain motif continue dans une direction particulière. Ainsi, l'ensemble de tous les entiers inclut également 3,4,5,6 et ainsi de suite, ainsi que -3,-4,-5,-6 et ainsi de suite. Cet ensemble de tous les entiers est typiquement noté par ℤ.

Un autre exemple d'ensemble est ℤ mod 11, ou l'ensemble de tous les entiers modulo 11. Contrairement à l'ensemble entier ℤ, cet ensemble ne contient qu'un nombre fini d'éléments, à savoir {0,1,…,9,10}.

Une erreur courante est de penser que l'ensemble ℤ mod 11 est en fait {-10,-9,…,0,…,9,10}. Mais ce n'est pas le cas, étant donné la manière dont nous avons défini l'opération modulo plus tôt. Tout entier négatif réduit par modulo 11 se ramène à {0,1,…,9,10}. Par exemple, l'expression -2 mod 11 se ramène à 9, tandis que l'expression -27 mod 11 se ramène à 5.

Un autre concept de base en mathématiques est celui d'une opération binaire. Il s'agit de toute opération qui prend deux éléments pour produire un troisième. Par exemple, à partir de l'arithmétique et de l'algèbre de base, vous seriez familier avec quatre opérations binaires fondamentales : l'addition, la soustraction, la multiplication et la division.

Ces deux concepts mathématiques de base, ensembles et opérations binaires, sont utilisés pour définir la notion de groupe, la structure la plus essentielle en algèbre abstraite.

Plus précisément, supposons une opération binaire ◌. De plus, supposons un ensemble d'éléments **S** équipé de cette opération. Tout ce que signifie "équipé" ici est que l'opération ◌ peut être effectuée entre n'importe quels deux éléments de l'ensemble **S**.

La combinaison 〈**S**, ◌〉 est, alors, un **groupe** s'il répond à quatre conditions spécifiques, connues sous le nom d'axiomes de groupe.

1. Pour tout a et b qui sont des éléments de **S**, a ◌ b est également un élément de **S**. Cela est connu sous le nom de **condition de fermeture**.
2. Pour tout a, b et c qui sont des éléments de **S**, il est vrai que (a ◌ b) ◌ c = a ◌ (b ◌ c). Cela est connu sous le nom de **condition d'associativité**. 3. Il existe un élément unique e dans **S**, tel que pour chaque élément a dans **S**, l'équation suivante est vérifiée : e ◌ a = a ◌ e = a. Comme il n'y a qu'un seul tel élément e, il est appelé l'**élément neutre**. Cette condition est connue sous le nom de **condition d'identité**.
4. Pour chaque élément a dans **S**, il existe un élément b dans **S**, tel que l'équation suivante est vérifiée : a ◌ b = b ◌ a = e, où e est l'élément neutre. L'élément b ici est connu sous le nom d'**élément inverse**, et il est couramment noté a<sup>-1</sup>. Cette condition est connue sous le nom de **condition d'inversibilité**.

Explorons un peu plus les groupes. Désignons l'ensemble de tous les entiers par ℤ. Cet ensemble combiné à l'addition standard, ou 〈ℤ, +〉, correspond clairement à la définition d'un groupe, car il répond aux quatre axiomes ci-dessus.

1. Pour tout x et y qui sont des éléments de ℤ, x + y est également un élément de ℤ. Donc 〈ℤ, +〉 répond à la condition de fermeture.
2. Pour tout x, y et z qui sont des éléments de ℤ, (x + y) + z = x + (y + z). Donc 〈ℤ, +〉 répond à la condition d'associativité.
3. Il existe un élément neutre dans 〈ℤ, +〉, à savoir 0. Pour tout x dans ℤ, il est vrai que : 0 + x = x + 0 = x. Donc 〈ℤ, +〉 répond à la condition d'identité.
4. Enfin, pour chaque élément x dans ℤ, il existe un y tel que x + y = y + x = 0. Si x était 10, par exemple, y serait – 10 (dans le cas où x est 0, y est également 0). Donc 〈ℤ, +〉 répond à la condition d'inversibilité.

Il est important de noter que le fait que l'ensemble des entiers avec l'addition constitue un groupe ne signifie pas qu'il constitue un groupe avec la multiplication. Vous pouvez vérifier cela en testant 〈ℤ, •〉 contre les quatre axiomes du groupe (où • signifie la multiplication standard).

Les deux premiers axiomes sont évidemment respectés. De plus, sous la multiplication, l'élément 1 peut servir d'élément neutre. Tout entier x multiplié par 1 donne en effet x. Cependant, 〈ℤ, •〉 ne répond pas à la condition d'inversibilité. C'est-à-dire, il n'existe pas d'élément unique y dans ℤ pour chaque x dans ℤ, tel que x • y = 1.

Par exemple, supposons que x = 22. Quelle valeur y de l'ensemble ℤ multipliée par x donnerait l'élément neutre 1 ? La valeur de 1/22 fonctionnerait, mais cela n'est pas dans l'ensemble ℤ. En fait, vous rencontrez ce problème pour tout entier x, à part les valeurs de 1 et -1 (où y devrait être 1 et -1 respectivement).
Si nous autorisions les nombres réels pour notre ensemble, alors nos problèmes disparaîtraient en grande partie. Pour tout élément x dans l'ensemble, la multiplication par 1/x donne 1. Comme les fractions sont incluses dans l'ensemble des nombres réels, un inverse peut être trouvé pour chaque nombre réel. L'exception est zéro, car toute multiplication avec zéro ne donnera jamais l'élément identité 1. Par conséquent, l'ensemble des nombres réels non nuls équipé de la multiplication est en effet un groupe.

Certains groupes répondent à une cinquième condition générale, connue sous le nom de **condition de commutativité**. Cette condition est la suivante :

* Supposons un groupe G avec un ensemble **S** et un opérateur binaire ◌. Supposons que a et b soient des éléments de **S**. Si il est vrai que a ◌ b = b ◌ a pour n'importe quels deux éléments a et b dans **S**, alors G répond à la condition de commutativité.

Tout groupe qui répond à la condition de commutativité est connu comme un **groupe commutatif**, ou un **groupe abélien** (d'après Niels Henrik Abel). Il est facile de vérifier que l'ensemble des nombres réels sur l'addition et l'ensemble des entiers sur l'addition sont des groupes abéliens. L'ensemble des entiers sur la multiplication n'est pas du tout un groupe, donc de facto ne peut pas être un groupe abélien. L'ensemble des nombres réels non nuls sur la multiplication, en revanche, est également un groupe abélien.

Vous devriez prêter attention à deux conventions importantes sur la notation. Premièrement, les signes “+” ou “x” seront fréquemment employés pour symboliser les opérations de groupe, même lorsque les éléments ne sont pas, en fait, des nombres. Dans ces cas, vous ne devriez pas interpréter ces signes comme l'addition ou la multiplication arithmétique standard. Au lieu de cela, ce sont des opérations ayant seulement une similarité abstraite avec ces opérations arithmétiques.

À moins que vous ne vous référiez spécifiquement à l'addition ou à la multiplication arithmétique, il est plus facile d'utiliser des symboles tels que ◌ et ◊ pour les opérations de groupe, car ceux-ci n'ont pas de connotations très culturellement ancrées.

Deuxièmement, pour la même raison que “+” et “x” sont souvent utilisés pour indiquer des opérations non arithmétiques, les éléments identité des groupes sont fréquemment symbolisés par “0” et “1”, même lorsque les éléments dans ces groupes ne sont pas des nombres. À moins que vous ne vous référiez à l'élément identité d'un groupe avec des nombres, il est plus facile d'utiliser un symbole plus neutre tel que “e” pour indiquer l'élément identité.

De nombreux ensembles de valeurs très différents et très importants en mathématiques équipés de certaines opérations binaires sont des groupes. Cependant, les applications cryptographiques ne fonctionnent qu'avec des ensembles d'entiers ou au moins des éléments qui sont décrits par des entiers, c'est-à-dire, dans le domaine de la théorie des nombres. Par conséquent, les ensembles avec des nombres réels autres que les entiers ne sont pas employés dans les applications cryptographiques.

Terminons en fournissant un exemple d'éléments qui peuvent être “décrits par des entiers”, bien qu'ils ne soient pas des entiers. Un bon exemple est les points des courbes elliptiques. Bien qu'un point sur une courbe elliptique ne soit clairement pas un entier, un tel point est en effet décrit par deux entiers.

Les courbes elliptiques sont, par exemple, cruciales pour Bitcoin. Toute paire de clés privée et publique standard Bitcoin est sélectionnée à partir de l'ensemble de points qui est défini par la courbe elliptique suivante : x<sup>3</sup> + 7 = y<sup>2</sup> mod 2<sup>256</sup> – 232 – 29 – 28 – 27 – 26 - 24 - 1 (le plus grand nombre premier inférieur à 2<sup>256</sup>). La coordonnée x est la clé privée et la coordonnée y est votre clé publique.
Les transactions en Bitcoin impliquent généralement de verrouiller des sorties à une ou plusieurs clés publiques d'une certaine manière. La valeur de ces transactions peut ensuite être débloquée en créant des signatures numériques avec les clés privées correspondantes.

## Groupes cycliques
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Une distinction majeure que nous pouvons établir est entre un **groupe fini** et un **groupe infini**. Le premier a un nombre fini d'éléments, tandis que le dernier a un nombre infini d'éléments. Le nombre d'éléments dans tout groupe fini est connu comme l'**ordre du groupe**. Toute la cryptographie pratique qui implique l'utilisation de groupes repose sur des groupes finis (théorie des nombres).

Dans la cryptographie à clé publique, une certaine classe de groupes abéliens finis connus sous le nom de groupes cycliques est particulièrement importante. Pour comprendre les groupes cycliques, nous devons d'abord comprendre le concept d'exponentiation des éléments du groupe.

Supposons un groupe G avec une opération de groupe ◌, et que a est un élément de G. L'expression a<sup>n</sup> doit alors être interprétée comme l'élément a combiné avec lui-même un total de n – 1 fois. Par exemple, a<sup>2</sup> signifie a ◌ a, a<sup>3</sup> signifie a ◌ a ◌ a, et ainsi de suite. (Notez que l'exponentiation ici n'est pas nécessairement l'exponentiation dans le sens arithmétique standard.)

Passons à un exemple. Supposons que G = 〈ℤ mod 7,+〉, et que notre valeur pour a égale 4. Dans ce cas, a<sup>2</sup> = [4 + 4 mod 7] = [8 mod 7] = 1 mod 7. Alternativement, a<sup>4</sup> représenterait [4 + 4 + 4 + 4 mod 7] = [16 mod 7] = 2 mod 7.

Certains groupes abéliens ont un ou plusieurs éléments, qui peuvent produire tous les autres éléments du groupe par exponentiation continue. Ces éléments sont appelés **générateurs** ou **éléments primitifs**.

Une classe importante de tels groupes est 〈ℤ* mod N, •〉, où N est un nombre premier. La notation ℤ* signifie ici que le groupe contient tous les entiers positifs non nuls inférieurs à N. Un tel groupe a donc toujours N – 1 éléments.

Considérons, par exemple, G = 〈ℤ* mod 11, •〉. Ce groupe a les éléments suivants : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}. L'ordre de ce groupe est 10 (ce qui est en effet égal à 11 – 1).

Explorons l'exponentiation de l'élément 2 de ce groupe. Les calculs jusqu'à 2<sup>12</sup> sont montrés ci-dessous. Notez que du côté gauche de l'équation, l'exposant se réfère à l'exponentiation de l'élément du groupe. Dans notre exemple particulier, cela implique en effet une exponentiation arithmétique du côté droit de l'équation (mais cela aurait aussi pu impliquer, par exemple, une addition). Pour clarifier, j'ai écrit l'opération répétée, plutôt que la forme d'exposant du côté droit.

* 2<sup>1</sup> = 2 mod 11
* 2<sup>2</sup> = 2 · 2 mod 11 = 4 mod 11
* 2<sup>3</sup> = 2 · 2 · 2 mod 11 = 8 mod 11
* 2<sup>4</sup> = 2 · 2 · 2 · 2 mod 11 = 16 mod 11 = 5 mod 11
* 2<sup>5</sup> = 2 · 2 · 2 · 2 · 2 mod 11 = 32 mod 11 = 10 mod 11
* 2<sup>6</sup> = 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 64 mod 11 = 9 mod 11
* 2<sup>7</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 128 mod 11 = 7 mod 11
* 2<sup>8</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 256 mod 11 = 3 mod 11
* 2<sup>9</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 512 mod 11 = 6 mod 11
* 2<sup>10</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 1024 mod 11 = 1 mod 11
* 2<sup>11</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 2048 mod 11 = 2 mod 11
* 2<sup>12</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 4096 mod 11 = 4 mod 11

Si vous observez attentivement, vous pouvez voir que l'exponentiation de l'élément 2 parcourt tous les éléments de 〈ℤ* mod 11, •〉 dans l'ordre suivant : 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Après 2<sup>10</sup>, l'exponentiation continue de l'élément 2 parcourt à nouveau tous les éléments et dans le même ordre. Par conséquent, l'élément 2 est un générateur dans 〈ℤ* mod 11, •〉.

Bien que 〈ℤ* mod 11, •〉 possède plusieurs générateurs, tous les éléments de ce groupe ne sont pas des générateurs. Considérons, par exemple, l'élément 3. En parcourant les 10 premières exponentiations, sans montrer les calculs fastidieux, on obtient les résultats suivants :

* 3<sup>1</sup> = 3 mod 11
* 3<sup>2</sup> = 9 mod 11
* 3<sup>3</sup> = 5 mod 11
* 3<sup>4</sup> = 4 mod 11
* 3<sup>5</sup> = 1 mod 11
* 3<sup>6</sup> = 3 mod 11
* 3<sup>7</sup> = 9 mod 11
* 3<sup>8</sup> = 5 mod 11
* 3<sup>9</sup> = 4 mod 11
* 3<sup>10</sup> = 1 mod 11

Au lieu de parcourir toutes les valeurs dans 〈ℤ* mod 11, •〉, l'exponentiation de l'élément 3 ne mène qu'à un sous-ensemble de ces valeurs : 3, 9, 5, 4 et 1. Après la cinquième exponentiation, ces valeurs commencent à se répéter.

Nous pouvons maintenant définir un **groupe cyclique** comme tout groupe ayant au moins un générateur. C'est-à-dire, il existe au moins un élément du groupe à partir duquel vous pouvez produire tous les autres éléments du groupe par exponentiation.

Vous avez peut-être remarqué dans notre exemple ci-dessus que tant 2<sup>10</sup> que 3<sup>10</sup> équivalent à 1 mod 11. En fait, bien que nous ne réaliserons pas les calculs, l'exponentiation par 10 de n'importe quel élément dans le groupe 〈ℤ* mod 11, •〉 donnera 1 mod 11. Pourquoi est-ce le cas ?

C'est une question importante, mais elle demande un peu de travail pour y répondre.

Pour commencer, supposons deux entiers positifs a et N. Un théorème important en théorie des nombres stipule que a a un inverse multiplicatif modulo N (c'est-à-dire, un entier b tel que a • b = 1 mod N) si et seulement si le plus grand commun diviseur entre a et N égale 1. C'est-à-dire, si a et N sont copremiers.

Ainsi, pour tout groupe d'entiers équipé de la multiplication modulo N, seuls les copremiers plus petits avec N sont inclus dans l'ensemble. Nous pouvons désigner cet ensemble par ℤ<sup>c</sup> mod N.

Par exemple, supposons que N est 10. Seuls les entiers 1, 3, 7 et 9 sont copremiers avec 10. Donc, l'ensemble ℤ<sup>c</sup> mod 10 inclut uniquement {1, 3, 7, 9}. Vous ne pouvez pas créer un groupe avec la multiplication d'entiers modulo 10 en utilisant d'autres entiers entre 1 et 10. Pour ce groupe particulier, les inverses sont les paires 1 et 9, et 3 et 7.

Dans le cas où N lui-même est premier, tous les entiers de 1 à N – 1 sont copremiers avec N. Un tel groupe a donc un ordre de N – 1. En utilisant notre notation précédente, ℤ<sup>c</sup> mod N équivaut à ℤ* mod N lorsque N est premier. Le groupe que nous avons sélectionné pour notre exemple précédent, 〈ℤ* mod 11, •〉, est une instance particulière de cette classe de groupes.

Ensuite, la fonction φ(N) calcule le nombre de copremiers jusqu'à un nombre N, et est connue sous le nom de **fonction Phi d'Euler**.<sup>[1](#footnote1)</sup> Selon **le théorème d'Euler**, chaque fois que deux entiers a et N sont copremiers, ce qui suit est vrai :

* a<sup>φ(N)</sup> mod N = 1 mod N
Cela a une implication importante pour la classe de groupes 〈ℤ* mod N, •〉 où N est un nombre premier. Pour ces groupes, l'exponentiation d'un élément du groupe représente l'exponentiation arithmétique. C'est-à-dire, a<sup>φ(N)</sup> mod N représente l'opération arithmétique a<sup>φ(N)</sup> mod N. Comme tout élément a dans ces groupes multiplicatifs est premier avec N, cela signifie que a<sup>φ(N)</sup> mod N = a<sup>N – 1</sup> mod N = 1 mod N.
Le théorème d'Euler est un résultat vraiment important. Pour commencer, il implique que tous les éléments dans 〈ℤ* mod N, •〉 ne peuvent que parcourir un nombre de valeurs par exponentiation qui se divise dans N – 1. Dans le cas de 〈ℤ* mod 11, •〉, cela signifie que chaque élément ne peut parcourir que 2, 5, ou 10 éléments. Les valeurs de groupe que tout élément parcourt par exponentiation sont connues comme l'**ordre de l'élément**. Un élément avec un ordre équivalent à l'ordre d'un groupe est un générateur.

De plus, le théorème d'Euler implique que nous pouvons toujours connaître le résultat de a<sup>N – 1</sup> mod N pour tout groupe 〈ℤ* mod N, •〉 où N est premier. Cela est vrai quelle que soit la complexité des calculs réels.

Par exemple, supposons que notre groupe soit ℤ* mod 160,481,182 (où 160,481,182 est effectivement un nombre premier). Nous savons que tous les entiers de 1 à 160,481,181 doivent être des éléments de ce groupe, et que φ(n) = 160,481,181. Bien que nous ne puissions pas réaliser toutes les étapes des calculs, nous savons que des expressions telles que 514<sup>160,481,181</sup>, 2,005<sup>160,481,181</sup>, et 256,212<sup>160,481,181</sup> doivent toutes évaluer à 1 mod 160,481,182.

## Fields
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Un groupe est la structure algébrique de base en algèbre abstraite, mais il en existe beaucoup d'autres. La seule autre structure algébrique dont vous devez être familier est celle d'un champ, spécifiquement celle d'un champ fini. Ce type de structure algébrique est fréquemment utilisé en cryptographie, comme dans le Standard de Chiffrement Avancé. Ce dernier est le principal schéma de chiffrement symétrique que vous rencontrerez en pratique.

Un champ est dérivé de la notion de groupe. Spécifiquement, un **champ** est un ensemble d'éléments **S** équipé de deux opérateurs binaires ◌ et ◊, qui répond aux conditions suivantes :

1. L'ensemble **S** équipé de ◌ est un groupe abélien.
2. L'ensemble **S** équipé de ◊ est un groupe abélien pour les éléments "non-zéro".
3. L'ensemble **S** équipé des deux opérateurs répond à ce qui est connu comme la condition distributive : Supposons que a, b, et c soient des éléments de **S**. Alors **S** équipé des deux opérateurs répond à la propriété distributive quand a ◌ (b ◊ c) = a ◌ b ◊ a ◌ c.
Notez que, comme pour les groupes, la définition d'un champ (field) est très abstraite. Elle ne fait aucune affirmation sur les types d'éléments dans **S**, ni sur les opérations ◌ et ◊. Elle déclare simplement qu'un champ est tout ensemble d'éléments avec deux opérations pour lesquelles les trois conditions ci-dessus sont respectées. (L'élément "zéro" dans le second groupe abélien peut être interprété de manière abstraite.)
Alors, quel pourrait être un exemple de champ ? Un bon exemple est l'ensemble ℤ mod 7, ou {0,1,…,7} défini sur l'addition standard (à la place de ◌ ci-dessus) et la multiplication standard (à la place de ◊ ci-dessus).

Premièrement, ℤ mod 7 répond à la condition pour être un groupe abélien sur l'addition, et il répond à la condition pour être un groupe abélien sur la multiplication si vous ne considérez que les éléments non nuls. Deuxièmement, la combinaison de l'ensemble avec les deux opérateurs répond à la condition distributive.

Il est didactiquement utile d'explorer ces affirmations en utilisant certaines valeurs particulières. Prenons les valeurs expérimentales 5, 2 et 3, quelques éléments sélectionnés au hasard de l'ensemble ℤ mod 7, pour inspecter le champ 〈ℤ mod 7, +, •〉. Nous utiliserons ces trois valeurs dans l'ordre, selon les besoins pour explorer des conditions particulières.

Explorons d'abord si ℤ mod 7 équipé de l'addition est un groupe abélien.

1. Condition de fermeture : Prenons 5 et 2 comme nos valeurs. Dans ce cas, [5 + 2] mod 7 = 7 mod 7 = 0. Cela est en effet un élément de ℤ mod 7, donc le résultat est cohérent avec la condition de fermeture.
2. Condition d'associativité : Prenons 5, 2 et 3 comme nos valeurs. Dans ce cas, [(5 + 2) + 3] mod 7 = [5 + (2 + 3)] mod 7 = 10 mod 7 = 3. Cela est cohérent avec la condition d'associativité.
3. Condition d'identité : Prenons 5 comme notre valeur. Dans ce cas, [5 + 0] mod 7 = [0 + 5] mod 7 = 5. Donc 0 semble être l'élément identité pour l'addition.
4. Condition d'inverse : Considérons l'inverse de 5. Il faut que [5 + d] mod 7 = 0, pour une certaine valeur de d. Dans ce cas, la valeur unique de ℤ mod 7 qui répond à cette condition est 2.
5. Condition de commutativité : Prenons 5 et 3 comme nos valeurs. Dans ce cas, [5 + 3] mod 7 = [3 + 5] mod 7 = 1. Cela est cohérent avec la condition de commutativité.

L'ensemble ℤ mod 7 équipé de l'addition semble clairement être un groupe abélien. Explorons maintenant si ℤ mod 7 équipé de la multiplication est un groupe abélien pour tous les éléments non nuls.

1. Condition de fermeture : Prenons 5 et 2 comme nos valeurs. Dans ce cas, [5 • 2] mod 7 = 10 mod 7 = 3. Cela est également un élément de ℤ mod 7, donc le résultat est cohérent avec la condition de fermeture.
2. Condition d'associativité : Prenons 5, 2 et 3 comme nos valeurs. Dans ce cas, [(5 • 2) • 3] mod 7 = [5 • (2 • 3)] mod 7 = 30 mod 7 = 2. Cela est conforme à la condition d'associativité.
3. Condition d'identité : Prenons 5 comme notre valeur. Dans ce cas, [5 • 1] mod 7 = [1 • 5] mod 7 = 5. Donc 1 semble être l'élément identité pour la multiplication.
4. Condition d'inverse : Considérons l'inverse de 5. Il faut que [5 • d] mod 7 = 1, pour une certaine valeur de d. La valeur unique de ℤ mod 7 qui satisfait cette condition est 3. Cela est conforme à la condition d'inverse.
5. Condition de commutativité : Prenons 5 et 3 comme nos valeurs. Dans ce cas, [5 • 3] mod 7 = [3 • 5] mod 7 = 15 mod 7 = 1. Cela est conforme à la condition de commutativité.

L'ensemble ℤ mod 7 semble clairement répondre aux règles pour être un groupe abélien lorsqu'il est conjugué soit à l'addition soit à la multiplication sur les éléments non nuls.

Finalement, cet ensemble combiné avec les deux opérateurs semble satisfaire à la condition distributive. Prenons 5, 2 et 3 comme nos valeurs. Nous pouvons voir que [5 • (2 + 3)] mod 7 = [5 • 2 + 5 • 3] mod 7 = 25 mod 7 = 4.

Nous avons maintenant vu que ℤ mod 7 équipé de l'addition et de la multiplication répond aux axiomes d'un champ fini lors des tests avec des valeurs particulières. Bien sûr, nous pouvons également montrer cela de manière générale, mais nous ne le ferons pas ici.

Une distinction clé est faite entre deux types de champs : les champs finis et les champs infinis.

Un **champ infini** implique un champ où l'ensemble **S** est infiniment grand. L'ensemble des nombres réels ℝ équipé de l'addition et de la multiplication est un exemple de champ infini. Un **champ fini**, également connu sous le nom de **champ de Galois**, est un champ où l'ensemble **S** est fini. Notre exemple ci-dessus de 〈ℤ mod 7, +, •〉 est un champ fini.

En cryptographie, nous nous intéressons principalement aux champs finis. Généralement, il peut être démontré qu'un champ fini existe pour un certain ensemble d'éléments **S** si et seulement si il a p<sup>m</sup> éléments, où p est un nombre premier et m un entier positif supérieur ou égal à un. En d'autres termes, si l'ordre de quelque ensemble **S** est un nombre premier (p<sup>m</sup> où m = 1) ou une puissance de premier (p<sup>m</sup> où m > 1), alors vous pouvez trouver deux opérateurs ◌ et ◊ tels que les conditions pour un champ sont satisfaites.

Si un champ fini a un nombre premier d'éléments, alors il est appelé un **champ premier**. Si le nombre d'éléments dans le champ fini est une puissance de premier, alors le champ est appelé un **champ d'extension**. En cryptographie, nous nous intéressons à la fois aux champs premiers et aux champs d'extension.<sup>[2](#footnote2)</sup>
Les principaux champs d'intérêt en cryptographie sont ceux où l'ensemble de tous les entiers est modulé par un certain nombre premier, et les opérateurs sont l'addition et la multiplication standard. Cette classe de champs finis inclurait ℤ mod 2, ℤ mod 3, ℤ mod 5, ℤ mod 7, ℤ mod 11, ℤ mod 13, et ainsi de suite. Pour tout champ premier ℤ mod p, l'ensemble des entiers du champ est le suivant : {0,1,….,p – 2, p – 1}.
En cryptographie, nous nous intéressons également aux champs d'extension, en particulier à tout champ avec 2<sup>m</sup> éléments où m > 1. Ces champs finis sont, par exemple, utilisés dans le Chiffrement Rijndael, qui forme la base de la Norme de Chiffrement Avancée. Alors que les champs premiers sont relativement intuitifs, ces champs d'extension de base 2 ne le sont probablement pas pour quelqu'un qui n'est pas familier avec l'algèbre abstraite.

Pour commencer, il est en effet vrai que tout ensemble d'entiers avec 2<sup>m</sup> éléments peut se voir attribuer deux opérateurs qui feraient de leur combinaison un champ (tant que m est un entier positif). Pourtant, le fait qu'un champ existe ne signifie pas nécessairement qu'il est facile à découvrir ou particulièrement pratique pour certaines applications.

Il s'avère que les champs d'extension particulièrement applicables de 2<sup>m</sup> en cryptographie sont ceux définis sur des ensembles particuliers d'expressions polynomiales, plutôt que sur un ensemble d'entiers.

Par exemple, supposons que nous voulions un champ d'extension avec 2<sup>3</sup> (c'est-à-dire, 8) éléments dans l'ensemble. Bien qu'il puisse y avoir de nombreux ensembles différents qui peuvent être utilisés pour des champs de cette taille, un tel ensemble inclut tous les polynômes uniques de la forme a<sub>2</sub>x<sup>2</sup> + a<sub>1</sub>x + a<sub>0</sub>, où chaque coefficient a<sub>i</sub> est soit 0 soit 1. Ainsi, cet ensemble **S** inclut les éléments suivants :

1. 0 : Le cas où a<sub>2</sub> = 0, a<sub>1</sub> = 0, et a<sub>0</sub> = 0.
2. 1 : Le cas où a<sub>2</sub> = 0, a<sub>1</sub> = 0, et a<sub>0</sub> = 1.
3. x : Le cas où a<sub>2</sub> = 0, a<sub>1</sub> = 1, et a<sub>0</sub> = 0.
4. x + 1 : Le cas où a<sub>2</sub> = 0, a<sub>1</sub> = 1, et a<sub>0</sub> = 1.
5. x<sup>2</sup> : Le cas où a<sub>2</sub>= 1, a<sub>1</sub> = 0, et a<sub>0</sub> = 0.
6. x<sup>2</sup> + 1 : Le cas où a<sub>2</sub> = 1, a<sub>1</sub> = 0, et a<sub>0</sub> = 1.
7. x<sup>2</sup> + x : Le cas où a<sub>2</sub> = 1, a<sub>1</sub> = 1 et a<sub>0</sub> = 0. 8. x<sup>2</sup> + x + 1 : Le cas où a<sub>2</sub> = 1, a<sub>1</sub> = 1 et a<sub>0</sub> = 1.

Donc **S** serait l'ensemble {0,1,x,x + 1, x<sup>2</sup>,x<sup>2</sup> + 1, x<sup>2</sup> + x, x<sup>2</sup> + x + 1}. Quelles deux opérations peuvent être définies sur cet ensemble d'éléments pour garantir que leur combinaison forme un corps ?

La première opération sur l'ensemble S (◌) peut être définie comme l'addition polynomiale standard modulo 2. Tout ce que vous avez à faire est d'ajouter les polynômes comme vous le feriez normalement, puis d'appliquer le modulo 2 à chacun des coefficients du polynôme résultant. Voici quelques exemples :

* [(x<sup>2</sup>) + (x<sup>2</sup> + x + 1)] mod 2 = [2x<sup>2</sup> + x + 1] mod 2 = x + 1
* [(x<sup>2</sup> + x) + (x)] mod 2 = [x<sup>2</sup> + 2x] mod 2 = x<sup>2</sup>
* [(x + 1) + (x<sup>2</sup> + x + 1)] mod 2 = [x<sup>2</sup> + 2x + 2] mod 2 = x<sup>2</sup> + 1

La seconde opération sur l'ensemble S (◌) nécessaire pour créer le corps est plus compliquée. Il s'agit d'une sorte de multiplication, mais pas de la multiplication standard de l'arithmétique. Au lieu de cela, vous devez voir chaque élément comme un vecteur et comprendre l'opération comme la multiplication de ces deux vecteurs modulo un polynôme irréductible.

Abordons d'abord l'idée d'un polynôme irréductible. Un **polynôme irréductible** est un polynôme qui ne peut pas être factorisé (tout comme un nombre premier ne peut pas être factorisé en composants autres que 1 et le nombre premier lui-même). Pour nos besoins, nous nous intéressons aux polynômes qui sont irréductibles par rapport à l'ensemble de tous les entiers. (Notez que vous pourriez être capable de factoriser certains polynômes, par exemple, par les nombres réels ou complexes, même si vous ne pouvez pas les factoriser en utilisant des entiers.)

Par exemple, considérez le polynôme x<sup>2</sup> - 3x + 2. Cela peut être réécrit comme (x – 1)(x – 2). Par conséquent, ce n'est pas irréductible. Maintenant, considérez le polynôme x<sup>2</sup> + 1. En utilisant uniquement des entiers, il n'y a aucun moyen de factoriser davantage cette expression. Par conséquent, ceci est un polynôme irréductible par rapport aux entiers.
Ensuite, tournons-nous vers le concept de multiplication vectorielle. Nous n'allons pas explorer ce sujet en profondeur, vous devez juste comprendre une règle de base : toute division vectorielle peut avoir lieu tant que le dividende a un degré supérieur ou égal à celui du diviseur. Si le dividende a un degré inférieur à celui du diviseur, alors le dividende ne peut plus être divisé par le diviseur.
Par exemple, considérez l'expression x<sup>6</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Cela se réduit davantage car le degré du dividende, 6, est supérieur au degré du diviseur, 5. Considérez maintenant l'expression x<sup>5</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Cela se réduit également davantage, car le degré du dividende, 5, et celui du diviseur, 5, sont égaux.

Cependant, considérez maintenant l'expression x<sup>4</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Cela ne se réduit pas davantage, car le degré du dividende, 4, est inférieur au degré du diviseur, 5.

Sur la base de ces informations, nous sommes maintenant prêts à trouver notre seconde opération pour l'ensemble {0,1,x,x + 1,x<sup>2</sup>,x<sup>2</sup> + 1,x<sup>2</sup> + x,x<sup>2</sup> + x + 1}.

J'ai déjà dit que la seconde opération devrait être comprise comme une multiplication vectorielle modulo un certain polynôme irréductible. Ce polynôme irréductible devrait garantir que la seconde opération définit un groupe abélien sur **S** et est cohérente avec la condition distributive. Alors, quel devrait être ce polynôme irréductible ?

Comme tous les vecteurs de l'ensemble sont de degré 2 ou inférieur, le polynôme irréductible devrait être de degré 3. Si toute multiplication de deux vecteurs dans l'ensemble produit un polynôme de degré 3 ou supérieur, nous savons que modulo un polynôme de degré 3 produit toujours un polynôme de degré 2 ou inférieur. C'est le cas parce que tout polynôme de degré 3 ou supérieur est toujours divisible par un polynôme de degré 3. De plus, le polynôme qui fonctionne comme diviseur doit être irréductible.

Il s'avère qu'il existe plusieurs polynômes irréductibles de degré 3 que nous pourrions utiliser comme notre diviseur. Chacun de ces polynômes définit un champ différent en conjonction avec notre ensemble S et l'addition modulo 2. Cela signifie que vous avez plusieurs options lors de l'utilisation des champs d'extension 2<sup>m</sup> en cryptographie.

Pour notre exemple, supposons que nous sélectionnons le polynôme x<sup>3</sup> + x + 1. Celui-ci est en effet irréductible, car vous ne pouvez pas le factoriser en utilisant des entiers. De plus, il garantira que toute multiplication de deux éléments produira un polynôme de degré 2 ou moins.
Travaillons sur un exemple de la seconde opération en utilisant le polynôme x<sup>3</sup> + x + 1 comme diviseur pour illustrer comment cela fonctionne. Supposons que vous multipliez les éléments x<sup>2</sup> + 1 avec x<sup>2</sup> + x dans notre ensemble **S**. Nous devons alors calculer l'expression [(x<sup>2</sup> + 1) • (x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1. Cela peut être simplifié comme suit :
* [(x<sup>2</sup> + 1) • (x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1 =
* [x<sup>2</sup> • x<sup>2</sup> + x<sup>2</sup> • x + 1 • x<sup>2</sup> + 1 • x] mod x<sup>3</sup> + x + 1 = 
* [x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x] mod x<sup>3</sup> + x + 1

Nous savons que [x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x] mod x<sup>3</sup> + x + 1 peut être réduit car le dividende a un degré supérieur (4) au diviseur (3).

Pour commencer, vous pouvez voir que l'expression x<sup>3</sup> + x + 1 rentre dans x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x un total de x fois. Vous pouvez vérifier cela en multipliant x<sup>3</sup> + x + 1 par x, ce qui donne x<sup>4</sup> + x<sup>2</sup> + x. Comme le dernier terme est du même degré que le dividende, à savoir 4, nous savons que cela fonctionne. Vous pouvez calculer le reste de cette division par x comme suit :

* [(x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x) – (x<sup>4</sup> + x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1 = 
* [x<sup>3</sup>] mod x<sup>3</sup> + x + 1 =
* x<sup>3</sup>

Donc, après avoir divisé x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x par x<sup>3</sup> + x + 1 un total de x fois, nous avons un reste de x<sup>3</sup>. Cela peut-il être davantage divisé par x<sup>3</sup> + x + 1 ?
Intuitivement, il pourrait sembler logique de dire que x<sup>3</sup> ne peut plus être divisé par x<sup>3</sup> + x + 1, car ce dernier terme semble plus grand. Cependant, souvenez-vous de notre discussion sur la division vectorielle plus tôt. Tant que le dividende a un degré supérieur ou égal au diviseur, l'expression peut être encore réduite. Spécifiquement, l'expression x<sup>3</sup> + x + 1 peut entrer dans x<sup>3</sup> exactement 1 fois. Le reste est calculé comme suit :
[(x<sup>3</sup>) – (x<sup>3</sup> + x + 1)] mod x<sup>3</sup> + x + 1 = 
[x + 1] mod x<sup>3</sup> + x + 1 = 
x + 1

Vous vous demandez peut-être pourquoi (x<sup>3</sup>) – (x<sup>3</sup> + x + 1) évalue à x + 1 et non à – x – 1. Souvenez-vous que la première opération de notre champ est définie modulo 2. Ainsi, la soustraction de deux vecteurs donne exactement le même résultat que l'addition de deux vecteurs.

Pour résumer la multiplication de x<sup>2</sup> + 1 et x<sup>2</sup> + x : Lorsque vous multipliez ces deux termes, vous obtenez un polynôme de degré 4, x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x, qui doit être réduit modulo x<sup>3</sup> + x + 1. Le polynôme de degré 4 est divisible par x<sup>3</sup> + x + 1 exactement x + 1 fois. Le reste après avoir divisé x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x par x<sup>3</sup> + x + 1 exactement x + 1 fois est x + 1. C'est en effet un élément de notre ensemble {0,1,x,x + 1,x<sup>2</sup>,x<sup>2</sup> + 1,x<sup>2</sup> + x,x<sup>2</sup> + x + 1}.

Pourquoi les champs d'extension avec base 2 sur des ensembles de polynômes, comme dans l'exemple ci-dessus, seraient-ils utiles pour la cryptographie ? La raison est que vous pouvez voir les coefficients dans les polynômes de tels ensembles, soit 0 soit 1, comme des éléments de chaînes binaires d'une longueur particulière. L'ensemble **S** dans notre exemple ci-dessus, par exemple, pourrait être vu à la place comme un ensemble S qui inclut toutes les chaînes binaires de longueur 3 (000 à 111). Les opérations sur **S**, alors, peuvent également être utilisées pour effectuer des opérations sur ces chaînes binaires et produire une chaîne binaire de la même longueur.

## L'algèbre abstraite en pratique
Malgré le langage formel et l'abstraction de la discussion, le concept de groupe ne devrait pas être trop difficile à saisir. Il s'agit simplement d'un ensemble d'éléments associés à une opération binaire, où l'exécution de cette opération binaire sur ces éléments répond à quatre conditions générales. Un groupe abélien ajoute juste une condition supplémentaire connue sous le nom de commutativité. Un groupe cyclique, à son tour, est un type spécial de groupe abélien, à savoir celui qui possède un générateur. Un champ (field) est simplement une construction plus complexe à partir de la notion de base de groupe.
Mais si vous êtes une personne pratiquement inclinée, vous pourriez vous demander à ce stade : Qui s'en soucie ? Savoir qu'un ensemble d'éléments avec un opérateur est un groupe, ou même un groupe abélien ou cyclique, a-t-il une pertinence dans le monde réel ? Savoir que quelque chose est un champ ?

Sans entrer dans trop de détails, la réponse est "oui". Les groupes ont été créés pour la première fois au 19e siècle par le mathématicien français Evariste Galois. Il les a utilisés pour tirer des conclusions sur la résolution des équations polynomiales d'un degré supérieur à cinq.

Depuis lors, le concept de groupe a aidé à éclairer un certain nombre de problèmes en mathématiques et ailleurs. Sur leur base, par exemple, le physicien Murray-Gellman a pu prédire l'existence d'une particule avant qu'elle ne soit réellement observée dans des expériences. Pour un autre exemple, les chimistes utilisent la théorie des groupes pour classer les formes des molécules. Les mathématiciens ont même utilisé le concept de groupe pour tirer des conclusions sur quelque chose d'aussi concret que le papier peint !

Essentiellement, montrer qu'un ensemble d'éléments avec un opérateur est un groupe, signifie que ce que vous décrivez possède une symétrie particulière. Pas une symétrie au sens commun du terme, mais dans une forme plus abstraite. Et cela peut fournir des aperçus substantiels sur des systèmes et problèmes particuliers. Les notions plus complexes de l'algèbre abstraite nous donnent simplement des informations supplémentaires.

Plus important encore, vous verrez l'importance des groupes et des champs théoriques des nombres dans la pratique à travers leur application en cryptographie, en particulier la cryptographie à clé publique. Nous avons déjà vu dans notre discussion sur les champs, par exemple, comment les champs d'extension sont employés dans le Chiffre de Rijndael. Nous travaillerons cet exemple dans le *Chapitre 5*.

## Exploration supplémentaire

Pour une discussion plus approfondie sur l'algèbre abstraite, je recommanderais l'excellente série de vidéos sur l'algèbre abstraite par Socratica. Je recommanderais particulièrement les vidéos suivantes : "Qu'est-ce que l'algèbre abstraite ?", "Définition de groupe (élargie)", "Définition d'anneau (élargie)", et "Définition de champ (élargie)". Ces quatre vidéos vous donneront un aperçu supplémentaire sur une grande partie de la discussion ci-dessus. (Nous n'avons pas discuté des anneaux, mais un champ est juste un type spécial d'anneau.)

Pour une discussion plus approfondie sur la théorie moderne des nombres, vous pouvez consulter de nombreuses discussions avancées sur la cryptographie. Je proposerais comme suggestions l'Introduction à la Cryptographie Moderne de Jonathan Katz et Yehuda Lindell ou la Compréhension de la Cryptographie de Christof Paar et Jan Pelzl pour une discussion plus approfondie.
[^1]: La fonction fonctionne comme suit. Tout entier N peut être factorisé en un produit de nombres premiers. Supposons qu'un N particulier soit factorisé de la manière suivante : p<sub>1</sub><sup>e1</sup> • p<sub>2</sub><sup>e2</sup> …. • p<sub>m</sub><sup>em</sup> où tous les p sont des nombres premiers et tous les e sont des entiers supérieurs ou égaux à 1. Alors, φ(N) = Somme<sub>i=1…m</sub>[p<sub>i</sub><sup>ei</sup> – p<sub>i</sub><sup>ei - 1</sup>] [^1].
[^2]: Les champs d'extension deviennent très contre-intuitifs. Au lieu d'avoir des éléments d'entiers, ils ont des ensembles de polynômes. De plus, toutes les opérations sont effectuées modulo un certain polynôme irréductible [^2].

[^3]: Voir [Vidéo YouTube](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be) [^3].

[^4]: Socratica, [Algèbre Abstraite](https://www.socratica.com/subject/abstract-algebra) [^4].

[^5]: Katz et Lindell, *Introduction à la Cryptographie Moderne*, 2e éd., 2015 (CRC Press : Boca Raton, FL). Paar et Pelzl, *Comprendre la Cryptographie*, 2010 (Springer-Verlag : Berlin) [^5].

# Cryptographie Symétrique
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

L'une des deux principales branches de la cryptographie est la cryptographie symétrique. Elle inclut les schémas de chiffrement ainsi que les schémas concernés par l'authentification et l'intégrité. Jusqu'aux années 1970, toute la cryptographie aurait consisté en des schémas de chiffrement symétrique.

La discussion principale commence par examiner les schémas de chiffrement symétrique et faire la distinction cruciale entre les chiffrements en flux et les chiffrements par blocs. Nous nous tournons ensuite vers les codes d'authentification de message, qui sont des schémas pour assurer l'intégrité et l'authenticité des messages. Enfin, nous explorons comment les schémas de chiffrement symétrique et les codes d'authentification de message peuvent être combinés pour assurer une communication sécurisée.

Ce chapitre discute de divers schémas cryptographiques symétriques de la pratique en passant. Le chapitre suivant offre une exposition détaillée du chiffrement avec un chiffrement en flux et un chiffrement par blocs de la pratique, à savoir RC4 et AES respectivement.

Avant de commencer notre discussion sur la cryptographie symétrique, je souhaite brièvement faire quelques remarques sur les illustrations d'Alice et Bob dans ce chapitre et les suivants.

## Alice et Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Pour illustrer les principes de la cryptographie, les gens s'appuient souvent sur des exemples impliquant Alice et Bob. Je ferai de même.

Surtout si vous êtes nouveau dans le domaine de la cryptographie, il est important de réaliser que ces exemples d'Alice et Bob ne sont destinés qu'à servir d'illustrations des principes et constructions cryptographiques dans un environnement simplifié. Les principes et constructions, cependant, sont applicables à une gamme beaucoup plus large de contextes de la vie réelle.

Voici cinq points clés à garder à l'esprit concernant les exemples impliquant Alice et Bob en cryptographie :

1. Ils peuvent facilement être traduits en exemples avec d'autres types d'acteurs tels que des entreprises ou des organisations gouvernementales.
2. Ils peuvent facilement être étendus pour inclure trois acteurs ou plus.
3. Dans les exemples, Bob et Alice sont typiquement des participants actifs dans la création de chaque message et dans l'application des schémas cryptographiques sur ce message. Mais en réalité, les communications électroniques sont largement automatisées. Lorsque vous visitez un site web utilisant la sécurité de la couche de transport, par exemple, la cryptographie est généralement entièrement gérée par votre ordinateur et le serveur web. 4. Dans le contexte de la communication électronique, les "messages" qui sont envoyés à travers un canal de communication sont généralement des paquets TCP/IP. Ils peuvent appartenir à un e-mail, un message Facebook, une conversation téléphonique, un transfert de fichier, un site web, un téléchargement de logiciel, et ainsi de suite. Ce ne sont pas des messages au sens traditionnel. Néanmoins, les cryptographes simplifient souvent cette réalité en affirmant que le message est, par exemple, un e-mail.
5. Les exemples se concentrent généralement sur la communication électronique, mais ils peuvent également être étendus aux formes traditionnelles de communication telles que les lettres.

## Schémas de chiffrement symétrique
<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Nous pouvons définir de manière générale un **schéma de chiffrement symétrique** comme tout schéma cryptographique avec trois algorithmes :

1. Un **algorithme de génération de clé**, qui génère une clé privée.
2. Un **algorithme de chiffrement**, qui prend la clé privée et un texte clair comme entrées et produit un texte chiffré.
3. Un **algorithme de déchiffrement**, qui prend la clé privée et le texte chiffré comme entrées et produit le texte clair original.

Typiquement, un schéma de chiffrement—qu'il soit symétrique ou asymétrique—offre un modèle pour le chiffrement basé sur un algorithme central, plutôt qu'une spécification exacte.

Par exemple, considérons Salsa20, un schéma de chiffrement symétrique. Il peut être utilisé avec des longueurs de clé de 128 et 256 bits. Le choix concernant la longueur de la clé impacte certains détails mineurs de l'algorithme (le nombre de tours dans l'algorithme pour être exact).

Mais on ne dirait pas que l'utilisation de Salsa20 avec une clé de 128 bits est un schéma de chiffrement différent de Salsa20 avec une clé de 256 bits. L'algorithme central reste le même. Ce n'est que lorsque l'algorithme central change que nous parlerions vraiment de deux schémas de chiffrement différents.

Les schémas de chiffrement symétriques sont typiquement utiles dans deux types de cas : (1) Ceux dans lesquels deux ou plusieurs agents communiquent à distance et veulent garder le contenu de leurs communications secret ; et (2) ceux dans lesquels un agent veut garder le contenu d'un message secret à travers le temps.

Vous pouvez voir une représentation de la situation (1) dans la *Figure 1* ci-dessous. Bob veut envoyer un message M à Alice à distance, mais ne veut pas que d'autres puissent lire ce message.

Bob chiffre d'abord le message M avec la clé privée K. Il envoie ensuite le texte chiffré C à Alice. Une fois qu'Alice a reçu le texte chiffré, elle peut le déchiffrer en utilisant la clé K et lire le texte clair. Avec un bon schéma de chiffrement, tout attaquant interceptant le texte chiffré C ne devrait pas être capable d'apprendre quoi que ce soit de réellement significatif sur le message M.

Vous pouvez voir une représentation de la situation (2) dans la *Figure 2* ci-dessous. Bob veut empêcher d'autres de voir certaines informations. Une situation typique pourrait être que Bob est un employé stockant des données sensibles sur son ordinateur, que ni les personnes extérieures ni ses collègues ne sont supposés lire.
Bob chiffre le message M au moment T<sub>0</sub> avec la clé K pour produire le texte chiffré C. Au moment T<sub>1</sub>, il a besoin à nouveau du message et déchiffre le texte chiffré C avec la clé K. Tout attaquant qui aurait pu tomber sur le texte chiffré C entre-temps ne devrait pas avoir été capable de déduire quoi que ce soit de significatif à propos de M.

*Figure 1 : Secret à travers l'espace*

![Figure 1 : Secret à travers l'espace](assets/Figure4-1.webp "Figure 1 : Secret à travers l'espace")

*Figure 2 : Secret à travers le temps*

![Figure 2 : Secret à travers le temps](assets/Figure4-2.webp "Figure 2 : Secret à travers le temps")

## Un exemple : Le chiffre par décalage
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

Dans le Chapitre 2, nous avons rencontré le chiffre par décalage qui est un exemple de schéma de chiffrement symétrique très simple. Regardons-le à nouveau ici.

Supposons un dictionnaire *D* qui associe toutes les lettres de l'alphabet anglais, dans l'ordre, avec l'ensemble des nombres {0,1,2…,25}. Supposons un ensemble de messages possibles **M**. Le chiffre par décalage est, alors, un schéma de chiffrement défini comme suit :

- Sélectionner aléatoirement une clé k parmi l'ensemble des clés possibles **K**, où **K** = {0,1,2,…,25}
- Chiffrer un message m є **M**, comme suit :
    - Séparer m en ses lettres individuelles m<sub>0</sub>, m<sub>1</sub>,….m<sub>i</sub>….,m<sub>l</sub>
    - Convertir chaque m<sub>i</sub> en un nombre selon *D*
    - Pour chaque m<sub>i</sub>, c<sub>i</sub> = [(m<sub>i</sub> + k) mod 26]
    - Convertir chaque c<sub>i</sub> en une lettre selon *D*
    - Puis combiner c<sub>0</sub>, c<sub>1</sub>,….,c<sub>l</sub> pour obtenir le texte chiffré c
- Déchiffrer un texte chiffré c comme suit :
    - Convertir chaque c<sub>i</sub> en un nombre selon *D*
    - Pour chaque c<sub>i</sub>, m<sub>i</sub> = [(c<sub>i</sub> – k) mod 26]
    - Convertir chaque m<sub>i</sub> en une lettre selon *D*
    - Puis combiner m<sub>0</sub>, m<sub>1</sub>,….,m<sub>l</sub> pour obtenir le message original m

Ce qui fait du chiffre par décalage un schéma de chiffrement symétrique est que la même clé est utilisée à la fois pour le processus de chiffrement et de déchiffrement. Par exemple, supposons que vous voulez chiffrer le message « DOG » en utilisant le chiffre par décalage, et que vous avez sélectionné aléatoirement "24" comme clé. Chiffrer le message avec cette clé donnerait « BME ». La seule façon de récupérer le message original est d'utiliser la même clé, "24", pour le processus de déchiffrement.
Ce chiffre de César est un exemple de **chiffrement par substitution monoalphabétique** : un schéma de cryptage où l'alphabet du texte chiffré est fixe (c'est-à-dire, un seul alphabet est utilisé). En supposant que l'algorithme de déchiffrement soit déterministe, chaque symbole dans le texte chiffré par substitution peut au maximum correspondre à un symbole dans le texte clair.

Jusqu'aux années 1700, de nombreuses applications de cryptage reposaient fortement sur les chiffrements par substitution monoalphabétique, bien que souvent ceux-ci étaient beaucoup plus complexes que le chiffre de César. Vous pourriez, par exemple, sélectionner aléatoirement une lettre de l'alphabet pour chaque lettre du texte original sous la contrainte que chaque lettre n'apparaisse qu'une seule fois dans l'alphabet du texte chiffré. Cela signifie que vous auriez factorial 26 clés privées possibles, ce qui était énorme à l'ère pré-informatique.

Notez que vous rencontrerez souvent le terme **chiffre** en cryptographie. Soyez conscient que ce terme a plusieurs significations. En fait, je connais au moins cinq significations distinctes du terme dans la cryptographie.

Dans certains cas, il fait référence à un schéma de cryptage, comme c'est le cas pour le chiffre de César et le chiffrement par substitution monoalphabétique. Cependant, le terme peut également se référer spécifiquement à l'algorithme de cryptage, la clé privée, ou juste au texte chiffré de tout schéma de cryptage.

Enfin, le terme chiffre peut également se référer à un algorithme de base à partir duquel vous pouvez construire des schémas cryptographiques. Cela peut inclure divers algorithmes de cryptage, mais aussi d'autres types de schémas cryptographiques. Ce sens du terme devient pertinent dans le contexte des chiffres en bloc (voir la section "Chiffres en bloc" ci-dessous).

Vous pouvez également rencontrer les termes **chiffrer** ou **déchiffrer**. Ces termes sont simplement des synonymes pour cryptage et décryptage.

## Attaques par force brute et principe de Kerckhoff
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Le chiffre de César est un schéma de cryptage symétrique très peu sécurisé, du moins dans le monde moderne.<sup>[1](#footnote1)</sup> Un attaquant pourrait simplement tenter de déchiffrer n'importe quel texte chiffré avec les 26 clés possibles pour voir quel résultat a du sens. Ce type d'attaque, où l'attaquant passe simplement en revue les clés pour voir ce qui fonctionne, est connu sous le nom d'**attaque par force brute** ou **recherche exhaustive de clé**.

Pour qu'un schéma de cryptage réponde à une notion minimale de sécurité, il doit disposer d'un ensemble de clés possibles, ou **espace de clés**, qui est si grand que les attaques par force brute sont infaisables. Tous les schémas de cryptage modernes répondent à cette norme. C'est ce qu'on appelle le **principe d'espace de clés suffisant**. Un principe similaire s'applique généralement dans différents types de schémas cryptographiques.

Pour avoir une idée de la taille massive de l'espace de clés dans les schémas de cryptage modernes, supposons qu'un fichier a été crypté avec un 128 bits en utilisant le standard de cryptage avancé. Cela signifie qu'un attaquant a un ensemble de 2<sup>128</sup> clés à parcourir pour une attaque par force brute. Une chance de succès de 0,78 % avec cette stratégie nécessiterait que l'attaquant parcoure environ 2,65 x 10<sup>36</sup> clés.
Supposons que nous supposions optimistement qu'un attaquant puisse tenter 10 quadrillions de clés par seconde (c'est-à-dire, 10<sup>16</sup> clés par seconde). Pour tester 0,78 % de toutes les clés dans l'espace des clés, son attaque devrait durer 2,65 x 10<sup>20</sup> secondes. Cela représente environ 8,4 trillions d'années. Ainsi, même une attaque par force brute par un adversaire absurdement puissant n'est pas réaliste avec un schéma de cryptage moderne de 128 bits. C'est le principe de l'espace de clé suffisant en action.

Le chiffre de César est-il plus sécurisé si l'attaquant ne connaît pas l'algorithme de cryptage ? Peut-être, mais pas de beaucoup.

Dans tous les cas, la cryptographie moderne suppose toujours que la sécurité de tout schéma de cryptage symétrique repose uniquement sur le secret de la clé privée. On suppose toujours que l'attaquant connaît tous les autres détails, y compris l'espace des messages, l'espace des clés, l'espace des textes chiffrés, l'algorithme de sélection des clés, l'algorithme de cryptage et l'algorithme de décryptage.

L'idée que la sécurité d'un schéma de cryptage symétrique ne peut reposer que sur le secret de la clé privée est connue sous le nom de **principe de Kerckhoffs**.

Tel qu'initialement prévu par Kerckhoffs, le principe ne s'applique qu'aux schémas de cryptage symétriques. Une version plus générale du principe s'applique cependant également à tous les autres types de schémas cryptographiques modernes : la conception d'un schéma cryptographique ne doit pas être requise pour être secrète afin qu'il soit sécurisé ; le secret ne peut s'étendre qu'à certaines chaînes d'informations, typiquement une clé privée.

Le principe de Kerckhoffs est central à la cryptographie moderne pour quatre raisons.<sup>[2](#footnote2)</sup> Premièrement, il n'existe qu'un nombre limité de schémas cryptographiques pour des types particuliers d'applications. Par exemple, la plupart des applications de cryptage symétrique moderne utilisent le chiffre de Rijndael. Ainsi, votre secret concernant la conception d'un schéma est juste très limité. Il y a, cependant, beaucoup plus de flexibilité dans le fait de garder secrète une clé privée pour le chiffre de Rijndael.

Deuxièmement, il est plus facile de remplacer une chaîne d'informations qu'un schéma cryptographique entier. Supposons que les employés d'une entreprise aient tous le même logiciel de cryptage, et que chaque deux employés aient une clé privée pour communiquer confidentiellement. Les compromissions de clés sont un problème dans ce scénario, mais au moins l'entreprise pourrait conserver le logiciel avec de telles failles de sécurité. Si l'entreprise comptait sur le secret du schéma, alors toute violation de ce secret nécessiterait de remplacer tout le logiciel.

Troisièmement, le principe de Kerckhoffs permet la standardisation et la compatibilité entre les utilisateurs de schémas cryptographiques. Cela a d'énormes avantages pour l'efficacité. Par exemple, il est difficile d'imaginer comment des millions de personnes pourraient se connecter de manière sécurisée aux serveurs web de Google chaque jour, si cette sécurité nécessitait de garder les schémas cryptographiques secrets.

Quatrièmement, le principe de Kerckhoff permet l'examen public des schémas cryptographiques. Ce type d'examen est absolument nécessaire pour atteindre des schémas cryptographiques sécurisés. À titre d'illustration, l'algorithme principal de la cryptographie symétrique, le chiffre de Rijndael, a été le résultat d'un concours organisé par le National Institute of Standards and Technology entre 1997 et 2000.

Tout système qui tente d'atteindre la **sécurité par l'obscurité** est celui qui repose sur le secret des détails de sa conception et/ou de sa mise en œuvre. En cryptographie, ce serait spécifiquement un système qui repose sur le secret des détails de conception du schéma cryptographique. Ainsi, la sécurité par l'obscurité est en contraste direct avec le principe de Kerckhoffs.
La capacité de l'ouverture à renforcer la qualité et la sécurité s'étend également plus largement au monde numérique que juste la cryptographie. Les distributions Linux libres et open source telles que Debian, par exemple, ont généralement plusieurs avantages par rapport à leurs homologues Windows et MacOS en termes de confidentialité, de stabilité, de sécurité et de flexibilité. Bien que cela puisse avoir plusieurs causes, le principe le plus important est probablement, comme Eric Raymond l'a formulé dans son célèbre essai "La Cathédrale et le Bazar", que "[g]iven enough eyeballs, all bugs are shallow.”<sup>[3](#footnote3)</sup> C'est ce principe de la sagesse des foules qui a donné à Linux son succès le plus significatif.
On ne peut jamais affirmer de manière univoque qu'un schéma cryptographique est "sécurisé" ou "non sécurisé". Au lieu de cela, il existe diverses notions de sécurité pour les schémas cryptographiques. Chaque **définition de la sécurité cryptographique** doit spécifier (1) les objectifs de sécurité, ainsi que (2) les capacités d'un attaquant. Analyser les schémas cryptographiques contre une ou plusieurs notions spécifiques de sécurité fournit des aperçus de leurs applications et limitations.

Bien que nous n'allons pas entrer dans tous les détails des différentes notions de sécurité cryptographique, vous devez savoir que deux hypothèses sont omniprésentes dans toutes les notions modernes de sécurité cryptographique concernant les schémas symétriques et asymétriques (et sous une certaine forme pour d'autres primitives cryptographiques) :

* La connaissance de l'attaquant sur le schéma est conforme au principe de Kerckhoffs.
* L'attaquant ne peut pas réaliser de manière réalisable une attaque par force brute sur le schéma. Spécifiquement, les modèles de menace des notions de sécurité cryptographique ne permettent généralement même pas les attaques par force brute, car ils supposent que celles-ci ne sont pas une considération pertinente.

## Chiffrements en flux
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Les schémas de chiffrement symétrique sont généralement subdivisés en deux types : les chiffrements en flux et les chiffrements par blocs. Cette distinction est cependant quelque peu problématique, car les gens utilisent ces termes de manière incohérente. Dans les prochaines sections, je vais établir la distinction de la manière que je pense être la meilleure. Vous devez cependant être conscient que beaucoup de gens utiliseront ces termes d'une manière quelque peu différente de celle que je décris.

Commençons d'abord par les chiffrements en flux. Un **chiffrement en flux** est un schéma de chiffrement symétrique où le chiffrement consiste en deux étapes.

D'abord, une chaîne de la longueur du texte clair est produite via une clé privée. Cette chaîne est appelée le **flux de clés**.

Ensuite, le flux de clés est combiné mathématiquement avec le texte clair pour produire un texte chiffré. Cette combinaison est typiquement une opération XOR. Pour le déchiffrement, vous pouvez simplement inverser l'opération. (Notez que A XOR B = B XOR A, dans le cas où A et B sont des chaînes de bits. Ainsi, l'ordre d'une opération XOR dans un chiffrement en flux n'affecte pas le résultat. Cette propriété est connue sous le nom de commutativité.)

Un chiffrement en flux XOR typique est représenté dans la *Figure 3*. Vous prenez d'abord une clé privée K et l'utilisez pour générer un flux de clés. Le flux de clés est ensuite combiné avec le texte clair via une opération XOR pour produire le texte chiffré. Tout agent qui reçoit le texte chiffré peut facilement le déchiffrer s'il a la clé K. Tout ce qu'elle a besoin de faire est de créer un flux de clés aussi long que le texte chiffré selon la procédure spécifiée du schéma et de le XOR avec le texte chiffré.

*Figure 3 : Un chiffrement en flux XOR*

![Figure 3 : Un chiffrement en flux XOR](assets/Figure4-3.webp "Figure 3 : Un chiffrement en flux XOR")
Rappelez-vous qu'un schéma de chiffrement est généralement un modèle pour le chiffrement utilisant le même algorithme de base, plutôt qu'une spécification exacte. Par extension, un chiffre de flux est généralement un modèle pour le chiffrement dans lequel vous pouvez utiliser des clés de différentes longueurs. Bien que la longueur de la clé puisse impacter certains détails mineurs du schéma, cela n'affectera pas sa forme essentielle.

Le chiffre de décalage est un exemple de chiffre de flux très simple et non sécurisé. En utilisant une seule lettre (la clé privée), vous pouvez produire une chaîne de lettres de la longueur du message (le flux de clés). Ce flux de clés est ensuite combiné avec le texte en clair via une opération modulo pour produire un texte chiffré. (Cette opération modulo peut être simplifiée en une opération XOR lors de la représentation des lettres en bits).

Un autre exemple célèbre de chiffre de flux est le **chiffre de Vigenère**, d'après Blaise de Vigenère qui l'a pleinement développé à la fin du 16ème siècle (bien que d'autres aient fait beaucoup de travail précurseur). C'est un exemple de **chiffre de substitution polyalphabétique** : un schéma de chiffrement où l'alphabet du texte chiffré pour un symbole de texte en clair change en fonction de sa position dans le texte. Contrairement à un chiffre de substitution monoalphabétique, les symboles de texte chiffré peuvent être associés à plus d'un symbole de texte en clair.

Alors que le chiffrement gagnait en popularité en Europe à la Renaissance, la **cryptanalyse**—c'est-à-dire, le décryptage des textes chiffrés—devenait particulièrement populaire, en utilisant l'**analyse de fréquence**. Cette dernière utilise les régularités statistiques de notre langue pour décrypter les textes chiffrés, et a été découverte par des savants arabes déjà au neuvième siècle. C'est une technique qui fonctionne particulièrement bien avec les textes longs. Et même les chiffres de substitution monoalphabétiques les plus sophistiqués n'étaient plus suffisants contre l'analyse de fréquence au 1700 en Europe, particulièrement dans les contextes militaires et de sécurité. Comme le chiffre de Vigenère offrait une avancée significative en matière de sécurité, il est devenu populaire à cette période et était répandu à la fin des années 1700.

De manière informelle, le schéma de chiffrement fonctionne comme suit :

1. Sélectionnez un mot de plusieurs lettres comme clé privée
2. Pour tout message, appliquez le chiffre de décalage à chaque lettre du message en utilisant la lettre correspondante dans le mot clé comme décalage
3. Si vous avez parcouru le mot clé mais que vous n'avez pas encore totalement chiffré le texte en clair, appliquez à nouveau les lettres du mot clé comme un chiffre de décalage aux lettres correspondantes dans le reste du texte
4. Continuez ce processus jusqu'à ce que le message entier ait été chiffré

Pour illustrer, supposons que votre clé privée soit GOLD et que vous souhaitiez chiffrer le message "CRYPTOGRAPHY". Dans ce cas, vous procéderiez comme suit selon le chiffre de Vigenère :

- c<sub>0</sub> = [(2 + 6) Mod 26] = 8 = I
- c<sub>1</sub> = [(17 + 14) Mod 26] = 5 = F
- c<sub>2</sub> = [(24 + 11) Mod 26] = 9 = J
- c<sub>3</sub> = [(15 + 3) Mod 26] = 18 = S
- c<sub>4</sub> = [(19 + 6) Mod 26] = 25 = Z
- c<sub>5</sub> = [(14 + 14) Mod 26] = 2 = C
- c<sub>6</sub> = [(6 + 11) Mod 26] = 17 = R
- c<sub>7</sub> = [(17 + 3) Mod 26] = 20 = U
- c<sub>8</sub> = [(0 + 6) Mod 26] = 6 = G
- c<sub>9</sub> = [(15 + 14) Mod 26] = 3 = D
- c<sub>10</sub> = [(7 + 11) Mod 26] = 18 = S
- c<sub>11</sub> = [(24 + 3) Mod 26] = 1 = B
- c = "IFJSZCRUGDSB"

Un autre exemple célèbre de chiffrement en flux est le **one-time pad**. Avec le one-time pad, vous créez simplement une chaîne de bits aléatoires aussi longue que le message en clair et produisez le texte chiffré via l'opération XOR. Ainsi, la clé privée et le flux de clés sont équivalents avec un one-time pad.

Alors que le chiffre de César et les chiffres de Vigenère sont très peu sécurisés à l'ère moderne, le one-time pad est très sécurisé s'il est utilisé correctement. Probablement l'application la plus célèbre du one-time pad était, au moins jusqu'aux années 1980, pour la **ligne directe Washington-Moscou**.<sup>[4](#footnote4)</sup>

La ligne directe est un lien de communication direct entre Washington et Moscou pour les affaires urgentes qui a été installé après la crise des missiles de Cuba. La technologie pour cela a évolué au fil des ans. Actuellement, elle inclut un câble à fibre optique direct ainsi que deux liaisons par satellite (pour la redondance), qui permettent l'e-mail et la messagerie texte. Le lien se termine en divers endroits aux États-Unis. Le Pentagone, la Maison Blanche et Raven Rock Mountain sont des points de terminaison connus. Contrairement à l'opinion populaire, la ligne directe n'a jamais impliqué de téléphones.

En essence, le schéma du one-time pad fonctionnait comme suit. Washington et Moscou auraient chacun deux ensembles de nombres aléatoires. Un ensemble de nombres aléatoires, créé par les Russes, concernait le chiffrement et le déchiffrement de tout message en langue russe. Un ensemble de nombres aléatoires, créé par les Américains, concernait le chiffrement et le déchiffrement de tout message en langue anglaise. De temps en temps, plus de nombres aléatoires seraient livrés à l'autre partie par des coursiers de confiance.

Washington et Moscou étaient alors capables de communiquer secrètement en utilisant ces nombres aléatoires pour créer des one-time pads. Chaque fois que vous aviez besoin de communiquer, vous utiliseriez la portion suivante de nombres aléatoires pour votre message.

Bien que très sécurisé, le one-time pad fait face à d'importantes limitations pratiques : la clé doit être aussi longue que le message et aucune partie d'un one-time pad ne peut être réutilisée. Cela signifie que vous devez garder une trace de l'endroit où vous en êtes dans le one-time pad, stocker un nombre massif de bits et échanger des bits aléatoires avec vos contreparties de temps en temps. En conséquence, le one-time pad n'est pas fréquemment utilisé en pratique.

Au lieu de cela, les chiffrements en flux prédominants utilisés en pratique sont les **chiffrements en flux pseudo-aléatoires**. Salsa20 et une variante étroitement liée appelée ChaCha sont des exemples de chiffrements en flux pseudo-aléatoires couramment utilisés.

Avec ces chiffrements en flux pseudo-aléatoires, vous sélectionnez d'abord aléatoirement une clé K qui est plus courte que la longueur du texte en clair. Une telle clé aléatoire K est généralement créée par notre ordinateur sur la base de données imprévisibles qu'il collecte au fil du temps, telles que le temps entre les messages réseau, les mouvements de la souris, et ainsi de suite.
Cette clé aléatoire K est ensuite insérée dans un algorithme d'expansion qui crée un flux de clés pseudorandom aussi long que le message. Vous pouvez spécifier précisément la longueur nécessaire du flux de clés (par exemple, 500 bits, 1000 bits, 1200 bits, 29 117 bits, etc.). Un flux de clés pseudorandom semble *comme si* il avait été choisi complètement au hasard parmi l'ensemble de toutes les chaînes de la même longueur. Ainsi, le chiffrement avec un flux de clés pseudorandom semble comme s'il avait été effectué avec un chiffrement par masque jetable. Mais cela, bien sûr, n'est pas le cas.

Comme notre clé privée est plus courte que le flux de clés et que notre algorithme d'expansion doit être déterministe pour que le processus de chiffrement/déchiffrement fonctionne, tous les flux de clés de cette longueur particulière n'auraient pas pu résulter en sortie de notre opération d'expansion.

Supposons, par exemple, que notre clé privée ait une longueur de 128 bits et que nous puissions l'insérer dans un algorithme d'expansion pour créer un flux de clés beaucoup plus long, disons de 2 500 bits. Comme notre algorithme d'expansion doit être déterministe, notre algorithme peut au maximum sélectionner 1/2<sup>128</sup> chaînes d'une longueur de 2 500 bits. Ainsi, un tel flux de clés ne pourrait jamais être sélectionné entièrement au hasard parmi toutes les chaînes de la même longueur.

Notre définition d'un chiffre de flux a deux aspects : (1) un flux de clés aussi long que le texte en clair est généré avec l'aide d'une clé privée ; et (2) ce flux de clés est combiné avec le texte en clair, typiquement via une opération XOR, pour produire le texte chiffré.

Parfois, les gens définissent la condition (1) de manière plus stricte, en affirmant que le flux de clés doit spécifiquement être pseudorandom. Cela signifie que ni le chiffre de décalage, ni le chiffrement par masque jetable ne seraient considérés comme des chiffres de flux.

À mon avis, définir la condition (1) de manière plus large offre une manière plus simple d'organiser les schémas de chiffrement. De plus, cela signifie que nous n'avons pas à arrêter d'appeler un schéma de chiffrement particulier un chiffre de flux simplement parce que nous apprenons qu'il ne repose pas réellement sur des flux de clés pseudorandom.

## Chiffres de bloc
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

La première manière de comprendre un **chiffre de bloc** est comme quelque chose de plus primitif qu'un chiffre de flux : Un algorithme de base qui effectue une transformation préservant la longueur sur une chaîne d'une longueur appropriée avec l'aide d'une clé. Cet algorithme peut être utilisé pour créer des schémas de chiffrement et peut-être d'autres types de schémas cryptographiques.

Fréquemment, un chiffre de bloc peut prendre des chaînes d'entrée de longueurs variables telles que 64, 128 ou 256 bits, ainsi que des clés de longueurs variables telles que 128, 192 ou 256 bits. Bien que certains détails de l'algorithme puissent changer en fonction de ces variables, l'algorithme de base ne change pas. Si c'était le cas, nous parlerions de deux chiffres de bloc différents. Notez que l'utilisation de la terminologie de l'algorithme de base ici est la même que pour les schémas de chiffrement.

Une représentation du fonctionnement d'un chiffre de bloc peut être vue dans la *Figure 4* ci-dessous. Un message M de longueur L et une clé K servent d'entrées au chiffre de bloc. Il produit un message M’ de longueur L. La clé n'a pas nécessairement besoin d'être de la même longueur que M et M’ pour la plupart des chiffres de bloc.

*Figure 4 : Un chiffre de bloc*

![Figure 4 : Un chiffre de bloc](assets/Figure4-4.webp "Figure 4 : Un chiffre de bloc")
Un chiffrement par bloc à lui seul n'est pas un schéma de chiffrement. Cependant, un chiffrement par bloc peut être utilisé avec divers **modes de fonctionnement** pour produire différents schémas de chiffrement. Un mode de fonctionnement ajoute simplement certaines opérations supplémentaires en dehors du chiffrement par bloc.

Pour illustrer comment cela fonctionne, supposons un chiffrement par bloc (BC) qui nécessite une chaîne d'entrée de 128 bits et une clé privée de 128 bits. La figure 5 ci-dessous montre comment ce chiffrement par bloc peut être utilisé avec le **mode de livre de codes électronique** (**mode ECB**) pour créer un schéma de chiffrement. (Les points de suspension à droite indiquent que vous pouvez répéter ce motif aussi longtemps que nécessaire).

*Figure 5 : Un chiffrement par bloc avec mode ECB*

![Figure 5 : Un chiffrement par bloc avec mode ECB](assets/Figure4-5.webp "Figure 5 : Un chiffrement par bloc avec mode ECB")

Le processus pour le chiffrement en livre de codes électronique avec le chiffrement par bloc est le suivant. Vérifiez si vous pouvez diviser votre message en clair en blocs de 128 bits. Si ce n'est pas le cas, ajoutez du **bourrage** au message, de sorte que le résultat puisse être divisé de manière égale par la taille de bloc de 128 bits. Ceci constitue vos données utilisées pour le processus de chiffrement.

Maintenant, divisez les données en morceaux de chaînes de 128 bits (M<sub>1</sub>, M<sub>2</sub>, M<sub>3</sub>, et ainsi de suite). Faites passer chaque chaîne de 128 bits à travers le chiffrement par bloc avec votre clé de 128 bits pour produire des morceaux de texte chiffré de 128 bits (C<sub>1</sub>, C<sub>2</sub>, C<sub>3</sub>, et ainsi de suite). Ces morceaux recombinés forment le texte chiffré complet.

Le déchiffrement est simplement le processus inverse, bien que le destinataire ait besoin d'une manière reconnaissable d'éliminer tout bourrage des données déchiffrées pour produire le message en clair original.

Bien que relativement simple, un chiffrement par bloc avec le mode livre de codes électronique manque de sécurité. Cela est dû au fait qu'il conduit à un **chiffrement déterministe**. Deux chaînes de données de 128 bits identiques sont chiffrées exactement de la même manière. Cette information peut être exploitée.

Au lieu de cela, tout schéma de chiffrement construit à partir d'un chiffrement par bloc devrait être **probabiliste** : c'est-à-dire que le chiffrement de n'importe quel message M, ou de n'importe quel morceau spécifique de M, devrait généralement produire un résultat différent à chaque fois.<sup>[5](#footnote5)</sup>

Le **mode de chaînage des blocs de chiffrement** (**mode CBC**) est probablement le mode le plus couramment utilisé avec un chiffrement par bloc. La combinaison, si elle est bien faite, produit un schéma de chiffrement probabiliste. Vous pouvez voir une représentation de ce mode de fonctionnement dans la figure 6 ci-dessous.

*Figure 6 : Un chiffrement par bloc avec mode CBC*

![Figure 6 : Un chiffrement par bloc avec mode CBC](assets/Figure4-6.webp "Figure 6 : Un chiffrement par bloc avec mode CBC")

Supposons que la taille du bloc soit à nouveau de 128 bits. Donc, pour commencer, vous devriez à nouveau vous assurer que votre message en clair original reçoit le bourrage nécessaire.

Ensuite, vous faites un XOR de la première portion de 128 bits de votre texte en clair avec un **vecteur d'initialisation** de 128 bits. Le résultat est placé dans le chiffrement par bloc pour produire un texte chiffré pour le premier bloc. Pour le deuxième bloc de 128 bits, vous faites d'abord un XOR du texte en clair avec le texte chiffré du premier bloc, avant de l'insérer dans le chiffrement par bloc. Vous continuez ce processus jusqu'à ce que vous ayez chiffré l'intégralité de votre message en clair.

Lorsque vous avez terminé, vous envoyez le message chiffré avec le vecteur d'initialisation non chiffré au destinataire. Le destinataire a besoin de connaître le vecteur d'initialisation, sinon il ne peut pas déchiffrer le texte chiffré.
Cette construction est beaucoup plus sûre que le mode livre de codes électronique lorsqu'elle est utilisée correctement. Vous devriez, d'abord, vous assurer que le vecteur d'initialisation est une chaîne aléatoire ou pseudo-aléatoire. De plus, vous devriez utiliser un vecteur d'initialisation différent chaque fois que vous utilisez ce schéma de chiffrement.
En d'autres termes, votre vecteur d'initialisation devrait être un nonce aléatoire ou pseudo-aléatoire, où un **nonce** signifie "un nombre qui est utilisé une seule fois." Si vous maintenez cette pratique, alors le mode CBC avec un chiffrement par blocs assure que deux blocs de texte clair identiques seront généralement chiffrés différemment à chaque fois.

Enfin, tournons notre attention vers le **mode de retour de feedback** (**mode OFB**). Vous pouvez voir une représentation de ce mode dans la *Figure 7*.

*Figure 7 : Un chiffrement par blocs avec mode OFB*

![Figure 7 : Un chiffrement par blocs avec mode OFB](assets/Figure4-7.webp "Figure 7 : Un chiffrement par blocs avec mode OFB")

Avec le mode OFB, vous sélectionnez également un vecteur d'initialisation. Mais ici, pour le premier bloc, le vecteur d'initialisation est directement inséré dans le chiffrement par blocs avec votre clé. Les 128 bits résultants sont, ensuite, traités comme un flux de clés. Ce flux de clés est XORé avec le texte clair pour produire le texte chiffré pour le bloc. Pour les blocs suivants, vous utilisez le flux de clés du bloc précédent comme entrée dans le chiffrement par blocs et répétez les étapes.

Si vous regardez attentivement, ce qui a réellement été créé ici à partir du chiffrement par blocs avec le mode OFB est un chiffrement en flux. Vous générez des portions de flux de clés de 128 bits jusqu'à ce que vous ayez la longueur du texte clair (en écartant les bits dont vous n'avez pas besoin de la dernière portion de flux de clés de 128 bits). Vous, ensuite, XOR le flux de clés avec votre message en texte clair pour obtenir le texte chiffré.

Dans la section précédente sur les chiffrements en flux, j'ai déclaré que vous produisez un flux de clés avec l'aide d'une clé privée. Pour être exact, il ne doit pas seulement être créé avec une clé privée. Comme vous pouvez le voir dans le mode OFB, le flux de clés est produit avec le soutien à la fois d'une clé privée et d'un vecteur d'initialisation.

Notez que, comme avec le mode CBC, il est important de sélectionner un nonce pseudo-aléatoire ou aléatoire pour le vecteur d'initialisation chaque fois que vous utilisez un chiffrement par blocs en mode OFB. Sinon, la même chaîne de message de 128 bits envoyée dans différentes communications sera chiffrée de la même manière. C'est une façon de créer un chiffrement probabiliste avec un chiffrement en flux.

Certains chiffrements en flux utilisent uniquement une clé privée pour créer un flux de clés. Pour ces chiffrements en flux, il est important que vous utilisiez un nonce aléatoire pour sélectionner la clé privée pour chaque instance de communication. Sinon, les résultats du chiffrement avec ces chiffrements en flux seront également déterministes, conduisant à des problèmes de sécurité.

Le chiffrement par blocs moderne le plus populaire est le **chiffrement Rijndael**. Il a été l'entrée gagnante parmi quinze soumissions à un concours organisé par le National Institute of Standards and Technology (NIST) entre 1997 et 2000 afin de remplacer une ancienne norme de chiffrement, le **standard de chiffrement de données** (**DES**).
Le chiffrement Rijndael peut être utilisé avec différentes spécifications pour les longueurs de clés et les tailles de blocs, ainsi que dans différents modes d'opération. Le comité pour le concours NIST a adopté une version restreinte du chiffrement Rijndael, à savoir une qui exige des tailles de blocs de 128 bits et des longueurs de clé de 128 bits, 192 bits ou 256 bits, comme partie de la **norme de chiffrement avancée** (**AES**). C'est vraiment la norme principale pour les applications de chiffrement symétrique. Elle est tellement sécurisée que même la NSA est apparemment prête à l'utiliser avec des clés de 256 bits pour des documents top secrets.<sup>[6](#footnote6)</sup>
Le chiffrement par blocs AES sera expliqué en détail dans le *Chapitre 5*.

## Dissiper la confusion
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

La confusion concernant la distinction entre les chiffrements par blocs et les chiffrements en flux survient parce que parfois les gens comprennent le terme chiffrement par blocs comme se référant spécifiquement à un *chiffrement par blocs avec un mode de chiffrement par blocs*.

Considérez les modes ECB et CBC dans la section précédente. Ces modes exigent spécifiquement que les données à chiffrer soient divisibles par la taille du bloc (ce qui signifie que vous pourriez devoir utiliser un remplissage pour le message original). De plus, les données dans ces modes sont également opérées directement par le chiffrement par blocs (et pas seulement combinées avec le résultat d'une opération de chiffrement par blocs comme dans le mode OFB).

Par conséquent, alternativement, vous pouvez définir un **chiffrement par blocs** comme tout schéma de chiffrement, qui opère sur des blocs de message de longueur fixe à la fois (où tout bloc doit être plus long qu'un octet, sinon il se transforme en un chiffrement en flux). Les données pour le chiffrement et le texte chiffré doivent se diviser uniformément dans cette taille de bloc. Typiquement, la taille du bloc est de 64, 128, 192 ou 256 bits de longueur. Par contraste, un chiffrement en flux peut chiffrer n'importe quel message en morceaux d'un bit ou d'un octet à la fois.

Avec cette compréhension plus spécifique du chiffrement par blocs, vous pouvez en effet affirmer que les schémas de chiffrement modernes sont soit des chiffrements en flux, soit des chiffrements par blocs. Désormais, j'utiliserai le terme chiffrement par blocs dans le sens le plus général sauf indication contraire.

La discussion sur le mode OFB dans la section précédente soulève également un autre point intéressant. Certains chiffrements en flux sont construits à partir de chiffrements par blocs, comme Rijndael avec OFB. Certains, comme Salsa20 et ChaCha, ne sont pas créés à partir de chiffrements par blocs. Vous pourriez appeler ces derniers **chiffrements en flux primitifs**. (Il n'y a pas vraiment de terme standardisé pour désigner de tels chiffrements en flux.)

Lorsque les gens parlent des avantages et des inconvénients des chiffrements en flux et des chiffrements par blocs, ils comparent typiquement les chiffrements en flux primitifs aux schémas de chiffrement basés sur des chiffrements par blocs.

Bien que vous puissiez toujours facilement construire un chiffrement en flux à partir d'un chiffrement par blocs, il est généralement très difficile de construire un type de construction avec un mode de chiffrement par blocs (comme avec le mode CBC) à partir d'un chiffrement en flux primitif.

À partir de cette discussion, vous devriez maintenant comprendre la *Figure 8*. Elle fournit un aperçu des schémas de chiffrement symétrique. Nous utilisons trois types de schémas de chiffrement : les chiffrements en flux primitifs, les chiffrements en flux par chiffrement par blocs, et les chiffrements par blocs dans un mode par blocs (également appelés « chiffrements par blocs » dans le diagramme).

*Figure 8 : Aperçu des schémas de chiffrement symétrique*

![Figure 8 : Aperçu des schémas de chiffrement symétrique](assets/Figure4-8.webp "Figure 8 : Aperçu des schémas de chiffrement symétrique")

## Codes d'authentification de message
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>
Le chiffrement concerne le secret. Mais la cryptographie s'intéresse également à des thèmes plus larges, tels que l'intégrité des messages, l'authenticité et la non-répudiation. Les **codes d'authentification de message** (MACs) sont des schémas cryptographiques à clé symétrique qui soutiennent l'authenticité et l'intégrité dans les communications.

Pourquoi a-t-on besoin de quelque chose d'autre que le secret dans la communication ? Supposons que Bob envoie à Alice un message en utilisant un chiffrement pratiquement incassable. Tout attaquant interceptant ce message ne pourra pas obtenir d'aperçus significatifs concernant son contenu. Cependant, l'attaquant dispose encore d'au moins deux autres vecteurs d'attaque :

1. Elle pourrait intercepter le texte chiffré, en modifier le contenu et envoyer le texte chiffré modifié à Alice.
2. Elle pourrait bloquer entièrement le message de Bob et envoyer son propre texte chiffré créé.

Dans ces deux cas, l'attaquant pourrait ne pas avoir d'aperçus sur le contenu des textes chiffrés (1) et (2). Mais elle pourrait encore causer des dommages significatifs de cette manière. C'est là que les codes d'authentification de message deviennent importants.

Les codes d'authentification de message sont définis de manière lâche comme des schémas cryptographiques symétriques avec trois algorithmes : un algorithme de génération de clé, un algorithme de génération de tag et un algorithme de vérification. Un MAC sécurisé garantit que les tags sont **existentiallement infalsifiables** pour tout attaquant, c'est-à-dire qu'ils ne peuvent pas créer avec succès un tag sur le message qui vérifie, à moins qu'ils n'aient la clé privée.

Bob et Alice peuvent combattre la manipulation d'un message particulier en utilisant un MAC. Supposons pour le moment qu'ils ne se soucient pas du secret. Ils veulent seulement s'assurer que le message reçu par Alice provient bien de Bob et n'a pas été modifié de quelque manière que ce soit.

Le processus est décrit dans la *Figure 9*. Pour utiliser un MAC, ils généreraient d'abord une clé privée K partagée entre eux deux. Bob crée un tag T pour le message en utilisant la clé privée K. Il envoie ensuite le message ainsi que le tag du message à Alice. Elle peut alors vérifier que Bob a bien fait le tag, en faisant passer la clé privée, le message et le tag à travers un algorithme de vérification.

*Figure 9 : Vue d'ensemble des schémas de chiffrement symétrique*

![Figure 9 : Vue d'ensemble des schémas de chiffrement symétrique](assets/Figure4-9.webp "Figure 9 : Vue d'ensemble des schémas de chiffrement symétrique")

En raison de l'infalsifiabilité existentielle, un attaquant ne peut ni modifier le message M de quelque manière que ce soit, ni créer un message avec un tag valide. Cela est vrai, même si l'attaquant observe les tags de nombreux messages entre Bob et Alice qui utilisent la même clé privée. Au maximum, un attaquant pourrait empêcher Alice de recevoir le message M (un problème que la cryptographie ne peut pas adresser).

Un MAC garantit qu'un message a été réellement créé par Bob. Cette authenticité implique automatiquement l'intégrité du message, c'est-à-dire, si Bob a créé un message, alors, de facto, il n'a pas été modifié de quelque manière que ce soit par un attaquant. Ainsi, à partir de maintenant, toute préoccupation pour l'authentification devrait être automatiquement comprise comme impliquant une préoccupation pour l'intégrité.

Bien que j'aie fait une distinction entre l'authenticité et l'intégrité des messages dans ma discussion, il est également courant d'utiliser ces termes comme synonymes. Ils se réfèrent alors à l'idée de messages qui ont été à la fois créés par un expéditeur particulier et non altérés de quelque manière que ce soit. Dans cet esprit, les codes d'authentification de message sont souvent également appelés **codes d'intégrité de message**.

## Authenticated encryption
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>
Généralement, vous voudriez garantir à la fois le secret et l'authenticité dans la communication et, par conséquent, les schémas de chiffrement et les schémas MAC sont typiquement utilisés ensemble. Un **schéma de chiffrement authentifié** est un schéma qui combine le chiffrement avec un MAC de manière hautement sécurisée. Spécifiquement, il doit répondre aux normes d'infalsifiabilité existentielle ainsi qu'à une notion très forte de secret, à savoir une qui résiste aux **attaques par texte chiffré choisi**.<sup>[7](#footnote7)</sup>

Pour qu'un schéma de chiffrement résiste aux attaques par texte chiffré choisi, il doit répondre aux normes de **non-malléabilité** : c'est-à-dire, toute modification d'un texte chiffré par un attaquant doit produire soit un texte chiffré invalide, soit un texte qui, une fois déchiffré, n'a aucun rapport avec l'original.<sup>[8](#footnote8)</sup>

Comme un schéma de chiffrement authentifié garantit qu'un texte chiffré créé par un attaquant est toujours invalide (car le tag ne sera pas vérifié), il répond aux normes de résistance aux attaques par texte chiffré choisi. Intéressant, vous pouvez prouver qu'un schéma de chiffrement authentifié peut toujours être créé à partir de la combinaison d'un MAC infalsifiable existentiellement et d'un schéma de chiffrement qui répond à une notion de sécurité moins forte, connue sous le nom de sécurité contre les **attaques par texte en clair choisi**.

Nous n'entrerons pas dans tous les détails de la construction des schémas de chiffrement authentifiés. Mais il est important de connaître deux détails de leur construction.

Premièrement, un schéma de chiffrement authentifié gère d'abord le chiffrement puis crée un tag de message sur le texte chiffré. Il s'avère que d'autres approches—telles que combiner le texte chiffré avec un tag sur le texte en clair, ou d'abord créer un tag puis chiffrer à la fois le texte en clair et le tag—sont non sécurisées. De plus, les deux opérations ont leur propre clé privée sélectionnée aléatoirement, sinon votre sécurité est gravement compromise.

Le principe mentionné s'applique plus généralement : *vous devriez toujours utiliser des clés distinctes lors de la combinaison de schémas cryptographiques de base*.

Un schéma de chiffrement authentifié est décrit dans la *Figure 10*. Bob crée d'abord un texte chiffré C à partir du message M en utilisant une clé K<sub>C</sub> sélectionnée aléatoirement. Il crée ensuite un tag de message T en faisant passer le texte chiffré et une autre clé K<sub>T</sub> sélectionnée aléatoirement à travers l'algorithme de génération de tag. Le texte chiffré et le tag de message sont envoyés à Alice.

Alice vérifie d'abord si le tag est valide étant donné le texte chiffré C et la clé K<sub>T</sub>. Si valide, elle peut alors déchiffrer le message en utilisant la clé K<sub>C</sub>. Non seulement elle est assurée d'une notion très forte de secret dans leurs communications, mais elle sait aussi que le message a été créé par Bob.

*Figure 10 : Un schéma de chiffrement authentifié*

![Figure 10: Un schéma de chiffrement authentifié](assets/Figure4-10.webp "Figure 10: Un schéma de chiffrement authentifié")

Comment les MAC sont-ils créés ? Bien que les MAC puissent être créés par plusieurs méthodes, une manière courante et efficace de les créer est via des fonctions de hachage cryptographiques.

Nous introduirons les fonctions de hachage cryptographiques plus en détail dans le *Chapitre 6*. Pour l'instant, sachez juste qu'une **fonction de hachage** est une fonction calculable efficacement qui prend des entrées de taille arbitraire et produit des sorties de longueur fixe. Par exemple, la fonction de hachage populaire **SHA-256** (secure hash algorithm 256) génère toujours une sortie de 256 bits, quelle que soit la taille de l'entrée. Certaines fonctions de hachage, telles que SHA-256, ont des applications utiles en cryptographie.
Le type de balise le plus courant produit avec une fonction de hachage cryptographique est le **code d'authentification de message basé sur le hachage** (HMAC). Le processus est illustré dans la *Figure 11*. Une partie produit deux clés distinctes à partir d'une clé privée K, la clé intérieure K<sub>1</sub> et la clé extérieure K<sub>2</sub>. Le texte en clair M ou le texte chiffré C est ensuite haché avec la clé intérieure. Le résultat T' est ensuite haché avec la clé extérieure pour produire la balise de message T.
Il existe une palette de fonctions de hachage qui peuvent être utilisées pour créer un HMAC. La fonction de hachage la plus couramment employée est SHA-256.

*Figure 11 : HMAC*

![Figure 11 : HMAC](assets/Figure4-11.webp "Figure 11 : HMAC")

## Sessions de communication sécurisées
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Supposons que deux parties soient dans une session de communication, elles s'envoient donc plusieurs messages aller-retour.

Un schéma de chiffrement authentifié permet au destinataire d'un message de vérifier qu'il a été créé par son partenaire dans une session de communication (tant que la clé privée n'a pas fuité). Cela fonctionne assez bien pour un seul message. Typiquement, cependant, deux parties envoient des messages aller-retour dans une session de communication. Et dans ce contexte, un schéma de chiffrement authentifié simple, tel que décrit dans la section précédente, ne suffit pas à assurer la sécurité.

La raison principale est qu'un schéma de chiffrement authentifié ne fournit aucune garantie que le message a réellement été également envoyé par l'agent qui l'a créé au sein d'une session de communication. Considérez les trois vecteurs d'attaque suivants :

1. **Attaque par rejeu** : Un attaquant renvoie un texte chiffré et une balise qu'elle a interceptés entre deux parties à un moment antérieur.
2. **Attaque par réorganisation** : Un attaquant intercepte deux messages à des moments différents et les envoie au destinataire dans l'ordre inverse.
3. **Attaque par réflexion** : Un attaquant observe un message envoyé de A à B, et envoie également ce message à A.

Bien que l'attaquant n'ait aucune connaissance du texte chiffré et ne puisse pas créer de faux textes chiffrés, les attaques ci-dessus peuvent encore causer des dommages significatifs dans les communications.

Supposons, par exemple, qu'un message particulier entre les deux parties implique le transfert de fonds financiers. Une attaque par rejeu pourrait transférer les fonds une seconde fois. Un schéma de chiffrement authentifié simple n'a aucune défense contre de telles attaques.

Heureusement, ces types d'attaques peuvent être facilement atténués dans une session de communication en utilisant des **identifiants** et des **indicateurs de temps relatifs**.

Des identifiants peuvent être ajoutés au message en clair avant le chiffrement. Cela empêcherait toute attaque par réflexion. Un indicateur de temps relatif peut, par exemple, être un numéro de séquence dans une session de communication particulière. Chaque partie ajoute un numéro de séquence à un message avant le chiffrement, de sorte que le destinataire sait dans quel ordre les messages ont été envoyés. Cela élimine la possibilité d'attaques par réorganisation. Cela élimine également les attaques par rejeu. Tout message qu'un attaquant envoie plus tard aura un ancien numéro de séquence, et le destinataire saura ne pas traiter le message à nouveau.

Pour illustrer comment fonctionnent les sessions de communication sécurisées, supposons à nouveau Alice et Bob. Ils envoient un total de quatre messages aller-retour. Vous pouvez voir comment un schéma de chiffrement authentifié avec des identifiants et des numéros de séquence fonctionnerait ci-dessous dans la *Figure 11*.
La session de communication commence par Bob envoyant un texte chiffré C<sub>0,B</sub> à Alice avec une étiquette de message T<sub>0,B</sub>. Le texte chiffré contient le message, ainsi qu'un identifiant (BOB) et un numéro de séquence (0). L'étiquette T<sub>0,B</sub> est réalisée sur l'ensemble du texte chiffré. Dans leurs communications ultérieures, Alice et Bob maintiennent ce protocole, mettant à jour les champs selon les besoins.
*Figure 12 : Une session de communication sécurisée*

![Figure 12 : Une session de communication sécurisée](assets/Figure4-12.webp "Figure 12 : Une session de communication sécurisée")

## Notes
<chapterId>b96d38dd-c9cb-56a7-8764-4af8526bc63f</chapterId>

[^1] : Selon Seutonius, un chiffre de décalage avec une valeur de clé constante de 3 était utilisé par Jules César dans ses communications militaires. Ainsi, A deviendrait toujours D, B toujours E, C toujours F, et ainsi de suite. Cette version particulière du chiffre de décalage est donc devenue connue sous le nom de **Chiffre de César** (bien qu'il ne soit pas vraiment un chiffre au sens moderne du terme, car la valeur de la clé est constante). Le chiffre de César aurait pu être sécurisé au premier siècle avant J.-C., si les ennemis de Rome étaient très peu familiers avec le chiffrement. Mais il ne serait clairement pas un schéma très sécurisé à l'époque moderne [^1].

[^2] : Jonathan Katz et Yehuda Lindell, *Introduction à la Cryptographie Moderne*, CRC Press (Boca Raton, FL : 2015), p. 7f [^2].

[^3] : Eric Raymond, “La Cathédrale et le Bazar,” présentation faite au Linux Kongress, Würzburg, Allemagne (27 mai 1997). Il existe un certain nombre de versions ultérieures disponibles ainsi qu'un livre. Mes citations proviennent de la page 30 du livre : Eric Raymond, *La Cathédrale et le Bazar : Réflexions sur Linux et l'Open Source par un Révolutionnaire Accidentel*, édition révisée. (2001), O’Reilly : Sebastopol, CA [^3].

[^4] : Crypto Museum, "Ligne directe Washington-Moscou," 2013, disponible sur [Crypto Museum](https://www.cryptomuseum.com/crypto/hotline/index.htm) [^4].

[^5] : L'importance du chiffrement probabiliste a été soulignée pour la première fois par Shafi Goldwasser et Silvio Micali, “Chiffrement probabiliste,” *Journal of Co [^5].

# RC4 et AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

Dans ce chapitre, nous discuterons des détails d'un schéma de chiffrement avec un chiffre de flux primitif moderne, RC4 (ou "chiffre Rivest 4"), et un chiffre de bloc moderne, AES. Bien que le chiffre RC4 soit tombé en désuétude comme méthode de chiffrement, AES est la norme pour le chiffrement symétrique moderne. Ces deux exemples devraient donner une meilleure idée de comment fonctionne le chiffrement symétrique sous le capot.

## Le chiffre de flux RC4
<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>
Pour comprendre le fonctionnement des chiffrements de flux pseudorandom modernes, je vais me concentrer sur le chiffrement de flux RC4. Il s'agit d'un chiffrement de flux pseudorandom qui a été utilisé dans les protocoles de sécurité des points d'accès sans fil WEP et WAP, ainsi que dans TLS. Comme le RC4 présente de nombreuses faiblesses avérées, il est tombé en désuétude. En fait, l'Internet Engineering Task Force interdit désormais l'utilisation des suites RC4 par les applications clientes et serveurs dans tous les cas de TLS.<sup>[3](#footnote3)</sup> Néanmoins, il sert bien d'exemple pour illustrer le fonctionnement d'un chiffrement de flux primitif.

Pour commencer, je vais d'abord montrer comment chiffrer un message en clair avec un chiffrement RC4 simplifié. Supposons que notre message en clair soit "SOUP". Le chiffrement avec notre chiffrement RC4 simplifié se déroule alors en quatre étapes.

### Étape 1

D'abord, définissez un tableau S avec S[0] = 0 à S[7] = 7. Un tableau ici signifie simplement une collection mutable de valeurs organisées par un index, également appelé une liste dans certains langages de programmation (par exemple, Python). Dans ce cas, l'index va de 0 à 7, et les valeurs vont également de 0 à 7. Donc S est comme suit :

- S = [0,1,2,3,4,5,6,7]

Les valeurs ici ne sont pas des nombres ASCII, mais les représentations en valeur décimale de chaînes de 1 octet. Ainsi, la valeur 2 équivaudrait à 0000 0011. La longueur du tableau S est donc de 8 octets.

### Étape 2

Ensuite, définissez un tableau de clés K de longueur 8 octets en choisissant une clé entre 1 et 8 octets (sans fractions d'octets permises). Comme chaque octet est de 8 bits, vous pouvez sélectionner n'importe quel nombre entre 0 et 255 pour chaque octet de votre clé.

Supposons que nous choisissons notre clé k comme [14,48,9], de sorte qu'elle ait une longueur de 3 octets. Chaque index de notre tableau de clés est alors défini selon la valeur décimale pour cet élément particulier de la clé, dans l'ordre. Si vous parcourez toute la clé, recommencez au début, jusqu'à ce que vous ayez rempli les 8 emplacements du tableau de clés. Ainsi, notre tableau de clés est le suivant :

- K = [14,48,9,14,48,9,14,48]

### Étape 3

Troisièmement, nous allons transformer le tableau S en utilisant le tableau de clés K, dans un processus connu sous le nom d'ordonnancement des clés. Le processus est le suivant en pseudocode :

- Créez les variables j et i
- Définissez la variable j = 0
- Pour chaque i de 0 à 7 :
	- Définissez j = j + S[i] + K[i] mod 8
	- Échangez S[i] et S[j]

La transformation du tableau S est capturée par *Tableau 1*.

Pour commencer, vous pouvez voir l'état initial de S comme [0,1,2,3,4,5,6,7] avec une valeur initiale de 0 pour j. Cela sera transformé en utilisant le tableau de clés [14,48,9,14,48,9,14,48].
La boucle for commence avec i = 0. Selon notre pseudocode ci-dessus, la nouvelle valeur de j devient 6 (j = j + S[0] + K[0] mod 8 = 0 + 0 + 14 mod 8 = 6 mod 8). En échangeant S[0] et S[6], l'état de S après 1 tour devient [6,1,2,3,4,5,0,7]. 
Dans la ligne suivante, i = 1. En parcourant à nouveau la boucle for, j obtient une valeur de 7 (j = j + S[1] + K[1] mod 8 = 6 + 1 + 48 mod 8 = 55 mod 8 = 7 mod 8). L'échange de S[1] et S[7] à partir de l'état actuel de S, [6,1,2,3,4,5,0,7], donne [6,7,2,3,4,5,0,1] après le 2ème tour.

Nous continuons avec ce processus jusqu'à produire la ligne finale en bas pour le tableau S, [6,4,1,0,3,7,5,2].

*Tableau 1 : Tableau de planification des clés*

![Tableau 1 : Tableau de planification des clés](assets/Table5-1.webp "Tableau 1 : Tableau de planification des clés")

### Étape 4

Comme quatrième étape, nous produisons le flot de clés. C'est la chaîne pseudo-aléatoire d'une longueur égale au message que nous voulons envoyer. C'est ce qui sera utilisé pour chiffrer le message original "SOUP". Comme le flot de clés doit être aussi long que le message, nous avons besoin d'un qui a 4 octets.

Le flot de clés est produit par le pseudocode suivant :

- Créer les variables j, i, et t
- Mettre j = 0
- Pour chaque i du texte en clair, en commençant par i = 1 et allant jusqu'à i = 4, chaque octet du flot de clés est produit comme suit :
    - j = j + S[i] mod 8
	- Échanger S[i] et S[j]
	- t = S[i] + S[j] mod 8
	- Le ième octet du flot de clés = S[t]

Vous pouvez suivre les calculs dans le *Tableau 2*.

L'état initial de S = S = [6,4,1,0,3,7,5,2]. En mettant i = 1, la valeur j devient 4 (j = j + S[i] mod 8 = 0 + 4 mod 8 = 4). Nous échangeons ensuite S[1] et S[4] pour produire la transformation de S dans la deuxième ligne, [6,3,1,0,4,7,5,2]. La valeur t est, ensuite, 7 (t = S[i] + S[j] mod 8 = 3 + 4 mod 8 = 7). Finalement, l'octet pour le flot de clés est, ensuite, S[7], ou 2.

Nous pouvons, ensuite, continuer à produire les autres octets jusqu'à ce que nous ayons les quatre octets suivants : 2, 6, 3, et 7. Chacun de ces octets peut, ensuite, être utilisé pour chiffrer chaque lettre du texte en clair, "SOUP".
Pour commencer, en utilisant une table ASCII, nous pouvons voir que "SOUP" codé par les valeurs décimales des chaînes d'octets sous-jacentes est "83 79 85 80". La combinaison avec le flux de clés "2 6 3 2" donne "85 85 88 82", qui reste le même après une opération modulo 256. En ASCII, le texte chiffré "85 85 88 82" équivaut à "UUXR". 
Que se passe-t-il si le mot à chiffrer était plus long que le tableau S ? Dans ce cas, le tableau S continue simplement de se transformer de cette manière affichée ci-dessus pour chaque octet i du texte en clair, jusqu'à ce que nous ayons un nombre d'octets dans le flux de clés égal au nombre de lettres dans le texte en clair.

*Tableau 2 : Génération du flux de clés*

![Tableau 2 : Génération du flux de clés](assets/Table5-2.webp "Tableau 2 : Génération du flux de clés")

L'exemple que nous venons de discuter est seulement une version simplifiée du chiffrement de flux RC4. Le véritable chiffrement de flux RC4 a un tableau S de 256 octets de longueur, pas 8 octets, et une clé qui peut être entre 1 et 256 octets, pas entre 1 et 8 octets. Le tableau de clés et les flux de clés sont, alors, tous produits en considérant la longueur de 256 octets du tableau S. Cela rend les calculs immensément plus complexes, mais les principes restent les mêmes. En utilisant la même clé, [14,48,9], avec le chiffrement RC4 standard, le message en texte clair "SOUP" est chiffré comme 67 02 ed df au format hexadécimal.

Un chiffrement de flux dans lequel le flux de clés se met à jour indépendamment du message en texte clair ou du texte chiffré est un **chiffrement de flux synchrone**. Le flux de clés dépend uniquement de la clé. Clairement, RC4 est un exemple de chiffrement de flux synchrone, car le flux de clés n'a aucune relation avec le texte en clair ou le texte chiffré. Tous nos chiffrements de flux primitifs mentionnés dans le chapitre précédent, y compris le chiffrement par décalage, le chiffre de Vigenère et le masque jetable, étaient également de la variété synchrone.

Par contraste, un **chiffrement de flux asynchrone** a un flux de clés qui est produit à la fois par la clé et les éléments précédents du texte chiffré. Ce type de chiffrement est également appelé un **chiffrement auto-synchronisant**.

Il est important que le flux de clés produit avec RC4 soit traité comme un masque jetable, et vous ne pouvez pas produire le flux de clés de la même manière la prochaine fois. Plutôt que de changer la clé à chaque fois, la solution pratique est de combiner la clé avec un nonce pour produire le flux d'octets.

## AES avec une clé de 128 bits
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Comme mentionné dans le chapitre précédent, le National Institute of Standards and Technology (NIST) a organisé un concours entre 1997 et 2000 pour déterminer un nouveau standard de chiffrement symétrique. Le chiffre Rijndael s'est avéré être l'entrée gagnante. Le nom est un jeu de mots sur les noms des créateurs belges, Vincent Rijmen et Joan Daemen.

Le chiffre Rijndael est un chiffre par blocs, ce qui signifie qu'il y a un algorithme central, qui peut être utilisé avec différentes spécifications pour les longueurs de clés et les tailles de blocs. Vous pouvez, alors, l'utiliser avec différents modes d'opération pour construire des schémas de chiffrement.
Le comité pour le concours du NIST a adopté une version restreinte du chiffre Rijndael, à savoir une qui nécessite des tailles de blocs de 128 bits et des longueurs de clé de 128 bits, 192 bits ou 256 bits, comme partie de la norme de chiffrement avancée. Cette version restreinte du chiffre Rijndael peut également être utilisée sous plusieurs modes d'opération. La spécification pour la norme est ce qui est connu sous le nom de Standard de Chiffrement Avancé (AES).

Afin de montrer comment fonctionne le chiffre Rijndael, le cœur de l'AES, je vais illustrer le processus de chiffrement avec une clé de 128 bits. La taille de la clé a un impact sur le nombre de tours tenus pour chaque bloc de chiffrement. Pour les clés de 128 bits, 10 tours sont nécessaires. Avec 192 bits et 256 bits, il aurait fallu respectivement 12 et 14 tours.

De plus, je vais supposer que l'AES est utilisé en mode ECB. Cela rend l'exposition légèrement plus facile et n'a pas d'importance pour l'algorithme Rijndael. Pour être sûr, le mode ECB n'est pas sécurisé en pratique car il conduit à un chiffrement déterministe. Le mode le plus couramment utilisé et sécurisé avec l'AES est le CBC.

Appelons la clé K<sub>0</sub>. La construction avec les paramètres ci-dessus, alors, se présente comme dans la Figure 1, où M<sub>i</sub> représente une partie du message en clair de 128 bits et C<sub>i</sub> une partie du texte chiffré de 128 bits. Un bourrage est ajouté au texte en clair pour le dernier bloc, si le texte en clair ne peut pas être divisé de manière égale par la taille du bloc.

*Figure 1 : AES-ECB avec une clé de 128 bits*

![Figure 1 : AES-ECB avec une clé de 128 bits](assets/Figure5-1.webp "Figure 1 : AES-ECB avec une clé de 128 bits")

Chaque bloc de 128 bits de texte passe par dix tours dans le schéma de chiffrement Rijndael. Cela nécessite une clé de tour séparée pour chaque tour (K<sub>1</sub> à K<sub>10</sub>). Celles-ci sont produites pour chaque tour à partir de la clé originale de 128 bits K<sub>0</sub> en utilisant un algorithme d'expansion de clé. Ainsi, pour chaque bloc de texte à chiffrer, nous utiliserons la clé originale K<sub>0</sub> ainsi que dix clés de tour séparées. Notez que ces mêmes 11 clés sont utilisées pour chaque bloc de 128 bits de texte en clair nécessitant un chiffrement.

L'algorithme d'expansion de clé est long et complexe. Le parcourir a peu d'avantages didactiques. Vous pouvez examiner l'algorithme d'expansion de clé par vous-même, si vous le souhaitez. Une fois les clés de tour produites, le chiffre Rijndael manipulera le premier bloc de 128 bits de texte en clair, M<sub>1</sub>, comme vu dans la Figure 2. Nous allons maintenant passer par ces étapes.

*Figure 2 : La manipulation de M<sub>1</sub> avec le chiffre Rijndael*

![Figure 2 : AES-ECB avec une clé de 128 bits](assets/Figure5-2.webp "Figure 2 : AES-ECB avec une clé de 128 bits")

### Tour 0

Le tour 0 du chiffre Rijndael est simple. Un tableau S<sub>0</sub> est produit par une opération XOR entre le texte en clair de 128 bits et la clé privée. C'est-à-dire,

- S<sub>0</sub> = M<sub>1</sub> XOR K<sub>0</sub>
Au premier tour, le tableau S<sub>0</sub> est d'abord combiné avec la clé de tour K<sub>1</sub> en utilisant une opération XOR. Cela produit un nouvel état de S.
Ensuite, l'opération de substitution de byte est effectuée sur l'état actuel de S. Elle fonctionne en prenant chaque byte du tableau S de 16 bytes et en le substituant par un byte d'un tableau appelé **Boîte S de Rijndael**. Chaque byte subit une transformation unique, et un nouvel état de S est produit comme résultat. La Boîte S de Rijndael est affichée dans la *Figure 3*.

*Figure 3 : Boîte S de Rijndael*

![Figure 3: Boîte S de Rijndael](assets/Figure5-3.webp "Figure 3: Boîte S de Rijndael")

Cette Boîte S est l'un des endroits où l'algèbre abstraite entre en jeu dans le chiffrement de Rijndael, spécifiquement les champs de Galois.

Pour commencer, vous définissez chaque élément de byte possible de 00 à FF comme un vecteur de 8 bits. Chaque vecteur est un élément du champ de Galois GF(2<sup>8</sup>) où le polynôme irréductible pour l'opération modulo est x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Le champ de Galois avec ces spécifications est également appelé Champ Fini de Rijndael.

Ensuite, pour chaque élément possible dans le champ, nous créons ce qui est appelé la **Boîte S de Nyberg**. Dans cette boîte, chaque byte est mappé sur son inverse multiplicatif (c'est-à-dire, de sorte que leur produit égale 1). Nous mappions ensuite ces valeurs de la Boîte S de Nyberg à la Boîte S de Rijndael en utilisant la transformation affine.

La troisième opération sur le tableau S est l'opération de décalage des lignes. Elle prend l'état de S et liste tous les seize bytes dans une matrice. Le remplissage de la matrice commence en haut à gauche et se fait en allant de haut en bas et ensuite, chaque fois qu'une colonne est remplie, en décalant d'une colonne vers la droite et vers le haut.

Une fois la matrice de S construite, les quatre lignes sont décalées. La première ligne reste la même. La deuxième ligne se déplace d'un cran vers la gauche. La troisième se déplace de deux crans vers la gauche. La quatrième se déplace de trois crans vers la gauche. Un exemple du processus est fourni dans la *Figure 4*. L'état original de S est montré en haut, l'état résultant après l'opération de décalage des lignes est montré en dessous.

*Figure 4 : Opération de décalage des lignes*

![Figure 4: Opération de décalage des lignes](assets/Figure5-4.webp "Figure 4: Opération de décalage des lignes")

Dans la quatrième étape, les champs de Galois font leur apparition à nouveau. Pour commencer, chaque colonne de la matrice S est multipliée par la colonne de la matrice 4 x 4 vue dans la *Figure 5*. Mais au lieu d'être une multiplication matricielle régulière, il s'agit d'une multiplication vectorielle modulo un polynôme irréductible, x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Les coefficients vectoriels résultants représentent les bits individuels d'un byte.

*Figure 5 : Matrice de mélange des colonnes*

![Figure 5: Matrice de mélange des colonnes](assets/Figure5-5.webp "Figure 5: Matrice de mélange des colonnes")

La multiplication de la première colonne de la matrice S avec la matrice 4 x 4 ci-dessus donne le résultat dans la *Figure 6*.
*Figure 6 : Multiplication de la première colonne*
![Figure 6 : Multiplication de la première colonne](assets/Figure5-6.webp "Figure 6 : Multiplication de la première colonne")

Comme prochaine étape, tous les termes de la matrice doivent être transformés en polynômes. Par exemple, F1 représente 1 octet et deviendrait x<sup>7</sup> + x<sup>6</sup> + x<sup>5</sup> + x<sup>4</sup> + 1 et 03 représente 1 octet et deviendrait x + 1.

Toutes les multiplications sont ensuite effectuées modulo x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Cela aboutit à l'addition de quatre polynômes dans chacune des quatre cellules de la colonne. Après avoir effectué ces additions modulo 2, vous obtiendrez quatre polynômes. Chacun de ces polynômes représente une chaîne de 8 bits, ou 1 octet, de S. Nous n'effectuerons pas tous ces calculs ici sur la matrice dans la *Figure 6* car ils sont étendus.

Une fois la première colonne traitée, les trois autres colonnes de la matrice S sont traitées de la même manière. Finalement, cela produira une matrice de seize octets qui peut être transformée en un tableau.

Comme étape finale, le tableau S est combiné de nouveau avec la clé de ronde dans une opération XOR. Cela produit l'état S<sub>1</sub>. C'est-à-dire,

- S<sub>1</sub> = S XOR K<sub>0</sub>

### Tours 2 à 10

Les tours 2 à 9 ne sont qu'une répétition du tour 1, *mutatis mutandis*. Le tour final ressemble beaucoup aux tours précédents, sauf que l'étape de mixage des colonnes est éliminée. Ainsi, le tour 10 est exécuté comme suit :

- S<sub>9</sub> XOR K<sub>10</sub>
- Substitution d'octets
- Décalage des lignes
- S<sub>10</sub> = S XOR K<sub>10</sub>

L'état S<sub>10</sub> est maintenant fixé à C<sub>1</sub>, les premiers 128 bits du texte chiffré. Le traitement des blocs de texte en clair de 128 bits restants produit le texte chiffré complet C.

### Les opérations du chiffrement Rijndael

Quelle est la raison d'être des différentes opérations observées dans le chiffrement Rijndael ?

Sans entrer dans les détails, les schémas de chiffrement sont évalués sur la base de la mesure dans laquelle ils créent de la confusion et de la diffusion. Si le schéma de chiffrement a un haut degré de **confusion**, cela signifie que le texte chiffré semble radicalement différent du texte en clair. Si le schéma de chiffrement a un haut degré de **diffusion**, cela signifie que tout petit changement apporté au texte en clair produit un texte chiffré radicalement différent.

La raison d'être des opérations derrière le chiffrement Rijndael est qu'elles produisent à la fois un haut degré de confusion et de diffusion. La confusion est produite par l'opération de substitution d'octets, tandis que la diffusion est produite par les opérations de décalage des lignes et de mixage des colonnes.

# Cryptographie asymétrique
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

Comme avec la cryptographie symétrique, les schémas asymétriques peuvent être utilisés pour garantir à la fois le secret et l'authentification. Cependant, par contraste, ces schémas emploient deux clés plutôt qu'une : une clé privée et une clé publique.
Nous commençons notre enquête avec la découverte de la cryptographie asymétrique, en particulier les problèmes qui l'ont stimulée. Ensuite, nous discutons de la manière dont les schémas asymétriques pour le chiffrement et l'authentification fonctionnent à un niveau élevé. Nous introduisons ensuite les fonctions de hachage, qui sont clés pour comprendre les schémas d'authentification asymétriques, et ont également une pertinence dans d'autres contextes cryptographiques, tels que pour les codes d'authentification de message basés sur le hachage que nous avons discutés dans le Chapitre 4.

## Le problème de distribution et de gestion des clés
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Supposons que Bob souhaite acheter un nouveau manteau de pluie chez Jim’s Sporting Goods, un détaillant d'articles de sport en ligne avec des millions de clients en Amérique du Nord. Ce sera son premier achat chez eux et il veut utiliser sa carte de crédit. Donc, Bob devra d'abord créer un compte chez Jim’s Sporting Goods, ce qui nécessite l'envoi de détails personnels tels que son adresse et les informations de sa carte de crédit. Il peut, ensuite, suivre les étapes nécessaires pour acheter le manteau de pluie.

Bob et Jim’s Sporting Goods voudront s'assurer que leurs communications sont sécurisées tout au long de ce processus, considérant que l'Internet est un système de communications ouvert. Ils voudront s'assurer, par exemple, qu'aucun attaquant potentiel ne puisse connaître les détails de la carte de crédit et de l'adresse de Bob, et qu'aucun attaquant potentiel ne puisse répéter ses achats ou en créer de faux en son nom.

Un schéma avancé de chiffrement authentifié, tel que discuté dans le chapitre précédent, pourrait certainement rendre les communications entre Bob et Jim’s Sporting Goods sécurisées. Mais il y a clairement des obstacles pratiques à la mise en œuvre d'un tel schéma.

Pour illustrer ces obstacles pratiques, supposons que nous vivions dans un monde où seuls les outils de la cryptographie symétrique existaient. Que pourraient alors faire Jim’s Sporting Goods et Bob pour assurer une communication sécurisée ?

Dans ces circonstances, ils seraient confrontés à des coûts substantiels pour communiquer de manière sécurisée. Comme l'Internet est un système de communications ouvert, ils ne peuvent pas simplement échanger un ensemble de clés par celui-ci. Par conséquent, Bob et un représentant de Jim’s Sporting Goods devraient effectuer un échange de clés en personne.

Une possibilité est que Jim’s Sporting Goods crée des emplacements spéciaux d'échange de clés, où Bob et d'autres nouveaux clients peuvent récupérer un ensemble de clés pour une communication sécurisée. Cela entraînerait évidemment des coûts organisationnels substantiels et réduirait grandement l'efficacité avec laquelle les nouveaux clients peuvent effectuer des achats.

Alternativement, Jim’s Sporting Goods peut envoyer à Bob une paire de clés avec un coursier hautement fiable. Cela est probablement plus efficace que d'organiser des emplacements d'échange de clés. Mais cela entraînerait toujours des coûts substantiels, en particulier si de nombreux clients ne font qu'un ou quelques achats.

Ensuite, un schéma symétrique pour le chiffrement authentifié oblige également Jim’s Sporting Goods à stocker des ensembles de clés séparés pour tous leurs clients. Cela représenterait un défi pratique significatif pour des milliers de clients, sans parler de millions.

Pour comprendre ce dernier point, supposons que Jim’s Sporting Goods fournisse à chaque client la même paire de clés. Cela permettrait à chaque client, ou à toute autre personne qui pourrait obtenir cette paire de clés, de lire et même de manipuler toutes les communications entre Jim’s Sporting Goods et ses clients. Vous pourriez alors, tout aussi bien, ne pas utiliser du tout de cryptographie dans vos communications.

Même répéter un ensemble de clés pour seulement certains clients est une terrible pratique de sécurité. Tout attaquant potentiel pourrait tenter d'exploiter cette caractéristique du schéma (rappelons que les attaquants sont supposés tout savoir d'un schéma sauf les clés, conformément au principe de Kerckhoffs.)

Ainsi, Jim’s Sporting Goods devrait stocker une paire de clés pour chaque client, indépendamment de la manière dont ces paires de clés sont distribuées. Cela présente clairement plusieurs problèmes pratiques.

- Jim’s Sporting Goods devrait stocker des millions de paires de clés, un ensemble pour chaque client.
- Ces clés devraient être correctement sécurisées, car elles constitueraient une cible de choix pour les hackers. Toute violation de sécurité nécessiterait la répétition d'échanges de clés coûteux, soit dans des lieux d'échange de clés spéciaux, soit par coursier. - Tout client de Jim’s Sporting Goods devrait stocker en toute sécurité une paire de clés chez lui. Des pertes et des vols se produiront, nécessitant une répétition des échanges de clés. Les clients devraient également passer par ce processus pour tout autre magasin en ligne ou autres types d'entités avec lesquelles ils souhaitent communiquer et effectuer des transactions sur Internet.

Ces deux principaux défis décrits étaient des préoccupations très fondamentales jusqu'à la fin des années 1970. Ils étaient connus sous le nom de **problème de distribution de clés** et **problème de gestion de clés**, respectivement.

Ces problèmes ont toujours existé, bien sûr, et ont souvent causé des maux de tête dans le passé. Les forces militaires, par exemple, devaient constamment distribuer des livres avec des clés pour la communication sécurisée au personnel sur le terrain, à grands risques et coûts. Mais ces problèmes s'aggravaient à mesure que le monde se dirigeait de plus en plus vers une ère de communication numérique à longue distance, en particulier pour les entités non gouvernementales.

Si ces problèmes n'avaient pas été résolus dans les années 1970, le shopping efficace et sécurisé chez Jim’s Sporting Goods n'aurait probablement pas existé. En fait, la plupart de notre monde moderne avec des e-mails pratiques et sécurisés, la banque en ligne et le shopping seraient probablement juste un lointain fantasme. Tout ce qui ressemblerait même de loin à Bitcoin n'aurait pas pu exister du tout.

Alors, que s'est-il passé dans les années 1970 ? Comment est-il possible que nous puissions faire des achats en ligne instantanément et naviguer en toute sécurité sur le World Wide Web ? Comment est-il possible que nous puissions envoyer instantanément des Bitcoins partout dans le monde depuis nos smartphones ?

## Nouvelles orientations en cryptographie
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

Dans les années 1970, les problèmes de distribution de clés et de gestion de clés avaient attiré l'attention d'un groupe de cryptographes universitaires américains : Whitfield Diffie, Martin Hellman et Ralph Merkle. Face au scepticisme sévère de la majorité de leurs pairs, ils se sont aventurés à trouver une solution.

Au moins une motivation principale pour leur entreprise était la prévision que les communications informatiques ouvertes affecteraient profondément notre monde. Comme Diffie et Hellman le notent en 1976,

> Le développement de réseaux de communication contrôlés par ordinateur promet un contact sans effort et peu coûteux entre des personnes ou des ordinateurs aux antipodes du monde, remplaçant la plupart du courrier et de nombreuses excursions par des télécommunications. Pour de nombreuses applications, ces contacts doivent être sécurisés contre l'écoute clandestine et l'injection de messages illégitimes. Cependant, à l'heure actuelle, la solution des problèmes de sécurité est bien en retard sur d'autres domaines de la technologie des communications. *La cryptographie contemporaine est incapable de répondre aux exigences, en ce sens que son utilisation imposerait des inconvénients si sévères aux utilisateurs du système, au point d'éliminer bon nombre des avantages du télétraitement.*<sup>[1](#footnote1)</sup>

La ténacité de Diffie, Hellman et Merkle a porté ses fruits. La première publication de leurs résultats fut un article de Diffie et Hellman en 1976 intitulé “New Directions in Cryptography.” Dans celui-ci, ils ont présenté deux manières originales d'aborder les problèmes de distribution de clés et de gestion de clés.
La première solution qu'ils ont proposée était un *protocole d'échange de clés à distance*, c'est-à-dire, un ensemble de règles pour l'échange d'une ou plusieurs clés symétriques sur un canal de communication non sécurisé. Ce protocole est maintenant connu sous le nom d'*échange de clés Diffie-Hellman* ou *échange de clés Diffie-Hellman-Merkle*.<sup>[2](#footnote2)</sup>
Avec l'échange de clés Diffie-Hellman, deux parties échangent d'abord publiquement certaines informations sur un canal non sécurisé tel que l'Internet. Sur la base de ces informations, elles créent ensuite, indépendamment, une clé symétrique (ou une paire de clés symétriques) pour une communication sécurisée. Bien que les deux parties créent leurs clés indépendamment, les informations qu'elles ont partagées publiquement garantissent que ce processus de création de clé donne le même résultat pour les deux.

Il est important de noter que, bien que tout le monde puisse observer les informations échangées publiquement par les parties sur le canal non sécurisé, seules les deux parties participant à l'échange d'informations peuvent créer des clés symétriques à partir de celles-ci.

Cela, bien sûr, semble complètement contre-intuitif. Comment deux parties pourraient-elles échanger certaines informations publiquement qui permettraient uniquement à elles de créer des clés symétriques à partir de celles-ci ? Pourquoi quelqu'un d'autre observant l'échange d'informations ne serait-il pas capable de créer les mêmes clés ?

Cela repose bien sûr sur de magnifiques mathématiques. L'échange de clés Diffie-Hellman fonctionne via une fonction à sens unique avec une trappe. Discutons de la signification de ces deux termes à leur tour.

Supposons que vous ayez une certaine fonction f(x) et le résultat f(a) = y, où a est une valeur particulière pour x. Nous disons que f(x) est une **fonction à sens unique** si il est facile de calculer la valeur y lorsque a et f(x) sont donnés, mais qu'il est informatiquement infaisable de calculer la valeur a lorsque y et f(x) sont donnés. Le nom de fonction à sens unique, bien sûr, vient du fait qu'une telle fonction n'est pratique à calculer que dans une direction.

Certaines fonctions à sens unique ont ce que l'on appelle une trappe. Alors qu'il est pratiquement impossible de calculer a seulement avec y et f(x), il existe une certaine pièce d'information Z qui rend le calcul de a à partir de y informatiquement faisable. Cette pièce d'information Z est connue sous le nom de **trappe**. Les fonctions à sens unique qui ont une trappe sont connues sous le nom de **fonctions à trappe**.

Nous n'entrerons pas dans les détails de l'échange de clés Diffie-Hellman ici. Mais essentiellement, chaque participant crée certaines informations, dont une partie est partagée publiquement et dont certaines restent secrètes. Chaque partie prend ensuite sa pièce d'information secrète et l'information publique partagée par l'autre partie pour créer une clé privée. Et, de manière quelque peu miraculeuse, les deux parties se retrouvent avec la même clé privée.

Toute partie observant juste l'information partagée publiquement entre les deux parties dans un échange de clés Diffie-Hellman est incapable de reproduire ces calculs. Elle aurait besoin de l'information privée de l'une des deux parties pour le faire.

Bien que la version de base de l'échange de clés Diffie-Hellman présentée dans l'article de 1976 ne soit pas très sécurisée, des versions sophistiquées du protocole de base sont certainement encore utilisées aujourd'hui. Plus important encore, chaque protocole d'échange de clés dans la dernière version du protocole de sécurité de la couche de transport (version 1.3) est essentiellement une version enrichie du protocole présenté par Diffie et Hellman en 1976. Le protocole de sécurité de la couche de transport est le protocole prédominant pour l'échange sécurisé d'informations formatées selon le protocole de transfert hypertexte (http), la norme pour l'échange de contenu Web.
Il est important de noter que l'échange de clés Diffie-Hellman n'est pas un schéma asymétrique. Strictement parlant, il appartient plutôt au domaine de la cryptographie à clé symétrique. Cependant, comme l'échange de clés Diffie-Hellman et la cryptographie asymétrique reposent tous deux sur des fonctions théoriques des nombres à sens unique avec des portes dérobées, ils sont généralement discutés ensemble.
La seconde méthode proposée par Diffie et Hellman pour aborder le problème de distribution et de gestion des clés dans leur article de 1976 était, bien sûr, via la cryptographie asymétrique.

Contrairement à leur présentation de l'échange de clés Diffie-Hellman, ils n'ont fourni que les contours généraux de la manière dont les schémas cryptographiques asymétriques pourraient plausiblement être construits. Ils n'ont pas proposé de fonction à sens unique qui pourrait spécifiquement remplir les conditions nécessaires pour une sécurité raisonnable dans de tels schémas.

Cependant, une mise en œuvre pratique d'un schéma asymétrique a été trouvée un an plus tard par trois cryptographes et mathématiciens universitaires différents : Ronald Rivest, Adi Shamir et Leonard Adleman. Le cryptosystème qu'ils ont introduit est devenu connu sous le nom de **cryptosystème RSA** (d'après leurs noms de famille).

Les fonctions à trappe utilisées dans la cryptographie asymétrique (et l'échange de clés Diffie-Hellman) sont toutes liées à deux principaux **problèmes computationnellement difficiles** : la factorisation de nombres premiers et le calcul de logarithmes discrets.

La **factorisation de nombres premiers** exige, comme son nom l'indique, de décomposer un entier en ses facteurs premiers. Le problème RSA est de loin l'exemple le plus connu d'un cryptosystème lié à la factorisation de nombres premiers.

Le **problème du logarithme discret** est un problème qui survient dans les groupes cycliques. Étant donné un générateur dans un groupe cyclique particulier, il nécessite le calcul de l'exposant unique nécessaire pour produire un autre élément du groupe à partir du générateur.

Les schémas basés sur le logarithme discret s'appuient sur deux principaux types de groupes cycliques : les groupes multiplicatifs d'entiers et les groupes qui incluent les points sur des courbes elliptiques. L'échange de clés Diffie-Hellman original, tel que présenté dans "New Directions in Cryptography", fonctionne avec un groupe multiplicatif cyclique d'entiers. L'algorithme de signature numérique de Bitcoin et le schéma de signature Schnorr récemment introduit (2021) sont tous deux basés sur le problème du logarithme discret pour un groupe cyclique de courbes elliptiques particulier.

Ensuite, nous passerons à un aperçu de haut niveau de la confidentialité et de l'authentification dans le cadre asymétrique. Avant cela, cependant, nous devons faire une brève note historique.

Il semble maintenant plausible qu'un groupe de cryptographes et de mathématiciens britanniques travaillant pour le Government Communications Headquarters (GCHQ) ait fait indépendamment les découvertes mentionnées ci-dessus quelques années plus tôt. Ce groupe était composé de James Ellis, Clifford Cocks et Malcolm Williamson.

Selon leurs propres comptes et celui du GCHQ, c'est James Ellis qui a d'abord conçu le concept de cryptographie à clé publique en 1969. Supposément, Clifford Cocks a ensuite découvert le système cryptographique RSA en 1973, et Malcolm Williamson le concept d'échange de clés Diffie-Hellman en 1974. Leurs découvertes n'ont cependant été révélées qu'en 1997, étant donné la nature secrète du travail effectué au GCHQ.

## Cryptage et authentification asymétriques
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Un aperçu du cryptage asymétrique avec l'aide de Bob et Alice est fourni dans la *Figure 1*.
Alice crée d'abord une paire de clés, composée d'une clé publique (K<sub>P</sub>) et d'une clé privée (K<sub>S</sub>), où le “P” dans K<sub>P</sub> signifie “public” et le “S” dans K<sub>S</sub> signifie “secret”. Elle distribue ensuite librement cette clé publique à d'autres. Nous reviendrons sur les détails de ce processus de distribution un peu plus tard. Mais pour l'instant, supposons que n'importe qui, y compris Bob, puisse obtenir de manière sécurisée la clé publique d'Alice K<sub>P</sub>.
À un moment donné, Bob souhaite écrire un message M à Alice. Comme il contient des informations sensibles, cependant, il veut que le contenu reste secret pour tous sauf Alice. Donc, Bob chiffre d'abord son message M en utilisant K<sub>P</sub>. Il envoie ensuite le texte chiffré C à Alice, qui déchiffre C avec K<sub>S</sub> pour reproduire le message original M.

*Figure 1 : Chiffrement asymétrique*

![Figure 1 : Chiffrement asymétrique](assets/Figure6-1.webp "Figure 1: Asymmetric encryption")

Tout adversaire qui écoute la communication entre Bob et Alice peut observer C. Elle connaît également K<sub>P</sub> et l'algorithme de chiffrement E(·). Cependant, cette information ne permet pas à l'attaquant de déchiffrer de manière faisable le texte chiffré C. Le déchiffrement nécessite spécifiquement K<sub>S</sub>, que l'attaquant ne possède pas.

Les schémas de chiffrement symétrique doivent généralement être sécurisés contre un attaquant qui peut chiffrer de manière valide des messages en clair (sécurité connue sous le nom d'attaque par texte chiffré choisi). Cependant, ils ne sont pas conçus avec le but explicite de permettre la création de tels textes chiffrés valides par un attaquant ou toute autre personne.

Ceci est en contraste frappant avec un schéma de chiffrement asymétrique, dont le but entier est de permettre à quiconque, y compris les attaquants, de produire des textes chiffrés valides. Les schémas de chiffrement asymétrique peuvent donc être étiquetés comme **ciphers à accès multiple**.

Pour mieux comprendre ce qui se passe, imaginez qu'au lieu d'envoyer un message électroniquement, Bob voulait envoyer une lettre physique en secret. Une manière d'assurer le secret serait qu'Alice envoie un cadenas sécurisé à Bob, mais garde la clé pour le déverrouiller. Après avoir écrit sa lettre, Bob pourrait mettre la lettre dans une boîte et la fermer avec le cadenas d'Alice. Il pourrait ensuite envoyer la boîte verrouillée avec le message à Alice qui a la clé pour la déverrouiller.

Bien que Bob soit capable de verrouiller le cadenas, ni lui ni aucune autre personne interceptant la boîte ne peut déverrouiller le cadenas s'il est effectivement sécurisé. Seule Alice peut le déverrouiller et voir le contenu de la lettre de Bob parce qu'elle a la clé.

Un schéma de chiffrement asymétrique est, grossièrement parlant, une version numérique de ce processus. Le cadenas est semblable à la clé publique et la clé du cadenas est semblable à la clé privée. Cependant, comme le cadenas est numérique, il est beaucoup plus facile et moins coûteux pour Alice de le distribuer à quiconque souhaitant lui envoyer des messages secrets.

Pour l'authentification dans le cadre asymétrique, nous utilisons les **signatures numériques**. Celles-ci ont donc la même fonction que les codes d'authentification de message dans le cadre symétrique. Un aperçu des signatures numériques est fourni dans la *Figure 2*.
Bob crée d'abord une paire de clés, composée de la clé publique (K<sub>P</sub>) et de la clé privée (K<sub>S</sub>), et distribue sa clé publique. Lorsqu'il souhaite envoyer un message authentifié à Alice, il prend d'abord son message M et sa clé privée pour créer une signature numérique D. Bob envoie ensuite à Alice son message accompagné de la signature numérique. Alice insère le message, la clé publique et la signature numérique dans un algorithme de vérification. Cet algorithme produit soit vrai pour une signature valide, soit faux pour une signature invalide.
Une signature numérique est, comme son nom l'indique clairement, l'équivalent numérique d'une signature écrite sur des lettres, des contrats, et ainsi de suite. En fait, une signature numérique est généralement beaucoup plus sécurisée. Avec un certain effort, vous pouvez falsifier une signature écrite ; un processus facilité par le fait que les signatures écrites ne sont pas fréquemment vérifiées de près. Une signature numérique sécurisée, cependant, est, tout comme un code d'authentification de message sécurisé, **existentially unforgeable** : c'est-à-dire, avec un schéma de signature numérique sécurisé, personne ne peut raisonnablement créer une signature pour un message qui passe la procédure de vérification, à moins qu'ils n'aient la clé privée.

*Figure 2 : Authentification asymétrique*

![Figure 2 : Authentification asymétrique](assets/Figure6-2.webp "Figure 2 : Authentification asymétrique")

Comme avec le chiffrement asymétrique, nous voyons un contraste intéressant entre les signatures numériques et les codes d'authentification de message. Pour ces derniers, l'algorithme de vérification ne peut être employé que par l'une des parties privées à la communication sécurisée. Cela est dû au fait qu'il nécessite une clé privée. Dans le cadre asymétrique, cependant, n'importe qui peut vérifier une signature numérique S faite par Bob.

Tout cela fait des signatures numériques un outil extrêmement puissant. Cela forme la base, par exemple, de la création de signatures sur des contrats qui peuvent être vérifiés à des fins légales. Si Bob avait fait une signature sur un contrat dans l'échange ci-dessus, Alice peut montrer le message M, le contrat et la signature S à un tribunal. Le tribunal peut alors vérifier la signature en utilisant la clé publique de Bob.<sup>[5](#footnote5)</sup>

Pour un autre exemple, les signatures numériques sont un aspect important pour sécuriser les logiciels et la distribution des mises à jour logicielles. Ce type de vérifiabilité publique ne pourrait jamais être créé en utilisant juste des codes d'authentification de message.

Comme dernier exemple de la puissance des signatures numériques, considérons Bitcoin. L'une des idées fausses les plus courantes à propos de Bitcoin, particulièrement dans les médias, est que les transactions sont chiffrées : elles ne le sont pas. Au lieu de cela, les transactions Bitcoin fonctionnent avec des signatures numériques pour assurer la sécurité.

Les bitcoins existent par lots appelés sorties de transaction non dépensées (ou UTXO). Supposons que vous recevez trois paiements sur une adresse Bitcoin particulière pour 2 bitcoins chacun. Techniquement, vous n'avez pas maintenant 6 bitcoins sur cette adresse. Au lieu de cela, vous avez trois lots de 2 bitcoins qui sont verrouillés par un problème cryptographique associé à cette adresse. Pour tout paiement que vous effectuez, vous pouvez utiliser un, deux ou les trois de ces lots, selon le montant dont vous avez besoin pour la transaction.

La preuve de propriété sur les sorties de transaction non dépensées est généralement montrée via une ou plusieurs signatures numériques. Bitcoin fonctionne précisément parce que des signatures numériques valides sur des sorties de transaction non dépensées sont computationnellement infaisables à réaliser, à moins que vous ne soyez en possession des informations secrètes nécessaires pour les faire.
Actuellement, les transactions Bitcoin incluent de manière transparente toutes les informations qui doivent être vérifiées par les participants du réseau, telles que les origines des sorties de transaction non dépensées utilisées dans la transaction. Bien qu'il soit possible de cacher certaines de ces informations tout en permettant leur vérification (comme le font certaines cryptomonnaies alternatives telles que Monero), cela crée également des risques de sécurité particuliers. 
Une confusion survient parfois entre les signatures numériques et les signatures écrites capturées numériquement. Dans ce dernier cas, vous capturez une image de votre signature écrite et la collez sur un document électronique tel qu'un contrat de travail. Cependant, cela n'est pas une signature numérique au sens cryptographique. Cette dernière est juste un long nombre qui ne peut être produit qu'en étant en possession d'une clé privée.

Tout comme dans le cadre de la clé symétrique, vous pouvez également utiliser des schémas de chiffrement et d'authentification asymétriques ensemble. Des principes similaires s'appliquent. Tout d'abord, vous devriez utiliser des paires de clés privées-publiques différentes pour le chiffrement et la création de signatures numériques. De plus, vous devriez d'abord chiffrer un message puis l'authentifier.

Il est important de noter que, dans de nombreuses applications, la cryptographie asymétrique n'est pas utilisée tout au long du processus de communication. Au lieu de cela, elle sera typiquement utilisée uniquement pour *échanger des clés symétriques* entre les parties par lesquelles elles communiqueront réellement.

C'est le cas, par exemple, lorsque vous achetez des biens en ligne. Connaissant la clé publique du vendeur, elle peut vous envoyer des messages signés numériquement que vous pouvez vérifier pour leur authenticité. Sur cette base, vous pouvez suivre l'un des multiples protocoles pour échanger des clés symétriques afin de communiquer de manière sécurisée.

La principale raison de la fréquence de l'approche susmentionnée est que la cryptographie asymétrique est beaucoup moins efficace que la cryptographie symétrique pour produire un niveau de sécurité particulier. C'est une raison pour laquelle nous avons encore besoin de la cryptographie à clé symétrique à côté de la cryptographie publique. De plus, la cryptographie à clé symétrique est beaucoup plus naturelle dans des applications particulières telles qu'un utilisateur d'ordinateur chiffrant ses propres données.

Alors, comment exactement les signatures numériques et le chiffrement à clé publique abordent-ils les problèmes de distribution et de gestion des clés ?

Il n'y a pas une seule réponse ici. La cryptographie asymétrique est un outil et il n'y a pas qu'une seule manière d'employer cet outil. Mais prenons notre exemple précédent de Jim’s Sporting Goods pour montrer comment les problèmes seraient typiquement abordés dans cet exemple.

Pour commencer, Jim’s Sporting Goods s'adresserait probablement à une **autorité de certification**, une organisation qui soutient la distribution de clé publique. L'autorité de certification enregistrerait certains détails sur Jim’s Sporting Goods et lui accorderait une clé publique. Elle enverrait ensuite à Jim’s Sporting Goods un certificat, connu sous le nom de **certificat TLS/SSL**, avec la clé publique de Jim’s Sporting Goods signée numériquement en utilisant la clé publique de l'autorité de certification. De cette manière, l'autorité de certification affirme qu'une clé publique particulière appartient bien à Jim’s Sporting Goods.

La clé pour comprendre ce processus avec les certificats TLS/SSL est que, bien que vous n'ayez généralement pas la clé publique de Jim’s Sporting Goods stockée quelque part sur votre ordinateur, les clés publiques des autorités de certification reconnues sont effectivement stockées dans votre navigateur ou dans votre système d'exploitation. Elles sont stockées dans ce qu'on appelle des **certificats racine**.

Ainsi, lorsque Jim’s Sporting Goods vous fournit son certificat TLS/SSL, vous pouvez vérifier la signature numérique de l'autorité de certification via un certificat racine dans votre navigateur ou système d'exploitation. Si la signature est valide, vous pouvez être relativement sûr que la clé publique sur le certificat appartient bien à Jim’s Sporting Goods. Sur cette base, il est facile de mettre en place un protocole pour une communication sécurisée avec Jim’s Sporting Goods.
La distribution de clés est devenue beaucoup plus simple pour Jim’s Sporting Goods. Il est facile de voir que la gestion des clés s'est également grandement simplifiée. Au lieu de devoir stocker des milliers de clés, Jim’s Sporting Goods a juste besoin de stocker une clé privée qui lui permet de faire des signatures pour la clé publique sur son certificat SSL. Chaque fois qu'un client visite le site de Jim’s Sporting Goods, il peut établir une session de communication sécurisée à partir de cette clé publique. Les clients n'ont également pas besoin de stocker d'informations (autre que les clés publiques des autorités de certification reconnues dans leur système d'exploitation et navigateur).

## Fonctions de hachage
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Les fonctions de hachage sont omniprésentes en cryptographie. Elles ne sont ni des schémas symétriques ni asymétriques, mais elles appartiennent à une catégorie cryptographique à part entière.

Nous avons déjà rencontré les fonctions de hachage dans le Chapitre 4 avec la création de messages d'authentification basés sur le hachage. Elles sont également importantes dans le contexte des signatures numériques, bien que pour une raison légèrement différente : les signatures numériques sont généralement réalisées sur la valeur de hachage de certains messages (cryptés), plutôt que sur le message (crypté) lui-même. Dans cette section, je vais offrir une introduction plus approfondie aux fonctions de hachage.

Commençons par définir une fonction de hachage. Une **fonction de hachage** est toute fonction calculable efficacement qui prend des entrées de taille arbitraire et produit des sorties de longueur fixe.

Une **fonction de hachage cryptographique** est simplement une fonction de hachage qui est utile pour des applications en cryptographie. La sortie d'une fonction de hachage cryptographique est typiquement appelée le **hachage**, **valeur de hachage**, ou **résumé de message**.

Dans le contexte de la cryptographie, une "fonction de hachage" fait généralement référence à une fonction de hachage cryptographique. Je vais adopter cette pratique à partir de maintenant.

Un exemple de fonction de hachage populaire est **SHA-256** (secure hash algorithm 256). Peu importe la taille de l'entrée (par exemple, 15 bits, 100 bits, ou 10 000 bits), cette fonction produira une valeur de hachage de 256 bits. Ci-dessous, vous pouvez voir quelques exemples de sorties de la fonction SHA-256.

* "Hello" : 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
* "52398" : a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90
* "La cryptographie c'est amusant" : 3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c

Toutes les sorties sont exactement de 256 bits écrites au format hexadécimal (chaque chiffre hexadécimal peut être représenté par quatre chiffres binaires). Donc, même si vous aviez inséré le livre *Le Seigneur des Anneaux* de Tolkien dans la fonction SHA-256, la sortie serait toujours de 256 bits.

Les fonctions de hachage telles que SHA-256 sont employées à diverses fins en cryptographie. Les propriétés requises d'une fonction de hachage dépendent vraiment du contexte d'une application particulière. Il y a deux propriétés principalement souhaitées des fonctions de hachage en cryptographie :

1. Résistance aux collisions
2. Masquage

On dit qu'une fonction de hachage H est **résistante aux collisions** si il est infaisable de trouver deux valeurs, x et y, telles que x ≠ y, et pourtant H(x) = H(y).
Les fonctions de hachage résistantes aux collisions sont importantes, par exemple, dans la vérification de logiciels. Supposons que vous souhaitiez télécharger la version Windows de Bitcoin Core 0.21.0 (une application serveur pour traiter le trafic réseau Bitcoin). Les principales étapes que vous devriez suivre, afin de vérifier la légitimité du logiciel, sont les suivantes :
1. Vous devez d'abord télécharger et importer les clés publiques d'un ou plusieurs contributeurs de Bitcoin Core dans un logiciel capable de vérifier les signatures numériques (par exemple, Kleopetra). Vous pouvez trouver ces clés publiques [ici](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Il est recommandé de vérifier le logiciel Bitcoin Core avec les clés publiques de plusieurs contributeurs.
2. Ensuite, vous devez vérifier les clés publiques que vous avez importées. Au moins une étape à suivre est de vérifier que les clés publiques que vous avez trouvées sont les mêmes que celles publiées dans divers autres emplacements. Vous pourriez, par exemple, consulter les pages web personnelles, les pages Twitter ou les pages Github des personnes dont vous avez importé les clés publiques. Typiquement, cette comparaison des clés publiques est réalisée en comparant un court hachage de la clé publique connu sous le nom d'empreinte.
3. Ensuite, vous devez télécharger l'exécutable pour Bitcoin Core depuis leur [site web](www.bitcoincore.org). Il y aura des paquets disponibles pour les systèmes d'exploitation Linux, Windows et MAC.
4. Ensuite, vous devez localiser deux fichiers de sortie. Le premier contient le hachage SHA-256 officiel pour l'exécutable que vous avez téléchargé ainsi que les hachages pour tous les autres paquets qui ont été publiés. Un autre fichier de sortie contiendra les signatures de divers contributeurs sur le fichier de sortie avec les hachages des paquets. Ces deux fichiers de sortie devraient se trouver sur le site web de Bitcoin Core.
5. Ensuite, vous devriez calculer le hachage SHA-256 de l'exécutable que vous avez téléchargé depuis le site web de Bitcoin Core sur votre propre ordinateur. Vous comparez ensuite ce résultat avec celui du hachage officiel du paquet pour l'exécutable. Ils devraient être identiques.
6. Enfin, vous devriez vérifier qu'une ou plusieurs des signatures numériques sur le fichier de sortie avec les hachages officiels des paquets correspondent effectivement à une ou plusieurs clés publiques que vous avez importées (les sorties de Bitcoin Core ne sont pas toujours signées par tout le monde). Vous pouvez faire cela avec une application telle que Kleopetra.

Ce processus de vérification de logiciel a deux avantages principaux. Premièrement, il garantit qu'il n'y a eu aucune erreur de transmission lors du téléchargement depuis le site web de Bitcoin Core. Deuxièmement, il garantit qu'aucun attaquant n'aurait pu vous amener à télécharger un code modifié et malveillant, soit en piratant le site web de Bitcoin Core, soit en interceptant le trafic.

Comment exactement le processus de vérification de logiciel ci-dessus protège-t-il contre ces problèmes ?

Si vous avez vérifié avec diligence les clés publiques que vous avez importées, alors vous pouvez être assez certain que ces clés sont réellement les leurs et n'ont pas été compromises. Étant donné que les signatures numériques ont une inviolabilité existentielle, vous savez que seuls ces contributeurs auraient pu faire une signature numérique sur les hachages officiels des paquets dans le fichier de sortie.

Supposons que les signatures sur le fichier de sortie que vous avez téléchargé sont correctes. Vous pouvez maintenant comparer la valeur de hachage que vous avez calculée localement pour l'exécutable Windows que vous avez téléchargé avec celle incluse dans le fichier de sortie correctement signé. Comme vous le savez, la fonction de hachage SHA-256 est résistante aux collisions, une correspondance signifie que votre exécutable est exactement le même que l'exécutable officiel.

Passons maintenant à la seconde propriété commune des fonctions de hachage : l'occultation. Toute fonction de hachage H est dite avoir la propriété d'occultation, si, pour tout x sélectionné aléatoirement dans une très large gamme, il est infaisable de trouver x lorsque seul H(x) est donné.
Ci-dessous, vous pouvez voir la sortie SHA-256 d'un message que j'ai écrit. Pour garantir une aléatoire suffisante, le message incluait une chaîne de caractères générée aléatoirement à la fin. Étant donné que SHA-256 possède la propriété de dissimulation, personne ne serait capable de déchiffrer ce message.
* b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded

Mais je ne vous laisserai pas dans le suspense jusqu'à ce que SHA-256 devienne plus faible. Le message original que j'ai écrit était le suivant :

* “Ceci est un message très aléatoire, ou bien, en quelque sorte aléatoire. Cette partie initiale ne l'est pas, mais je terminerai avec quelques caractères relativement aléatoires pour garantir un message très imprévisible. XLWz4dVG3BxUWm7zQ9qS”.

Une manière courante d'utiliser les fonctions de hachage avec la propriété de dissimulation est dans la gestion des mots de passe (la résistance aux collisions est également importante pour cette application). Tout service en ligne basé sur un compte décent tel que Facebook ou Google ne stockera pas directement vos mots de passe pour gérer l'accès à votre compte. Au lieu de cela, ils ne stockeront qu'un hachage de ce mot de passe. Chaque fois que vous saisissez votre mot de passe sur un navigateur, un hachage est d'abord calculé. Seul ce hachage est envoyé au serveur du fournisseur de services et comparé avec le hachage stocké dans la base de données en arrière-plan. La propriété de dissimulation peut aider à garantir que les attaquants ne peuvent pas le récupérer à partir de la valeur du hachage.

La gestion des mots de passe via des hachages, bien sûr, ne fonctionne que si les utilisateurs choisissent réellement des mots de passe difficiles. La propriété de dissimulation suppose que x est choisi aléatoirement dans une très large gamme. Sélectionner des mots de passe tels que “1234”, “mypassword”, ou la date de votre anniversaire ne fournira aucune sécurité réelle. De longues listes de mots de passe communs et leurs hachages existent, que les attaquants peuvent exploiter s'ils obtiennent jamais le hachage de votre mot de passe. Ces types d'attaques sont connus sous le nom d'**attaques par dictionnaire**. Si les attaquants connaissent certains de vos détails personnels, ils pourraient également tenter quelques suppositions informées. Par conséquent, vous avez toujours besoin de mots de passe longs et sécurisés (de préférence de longues chaînes aléatoires provenant d'un gestionnaire de mots de passe).

Parfois, une application peut nécessiter une fonction de hachage qui possède à la fois une résistance aux collisions et une dissimulation. Mais certainement pas toujours. Le processus de vérification logicielle dont nous avons discuté, par exemple, ne nécessite que la fonction de hachage affiche une résistance aux collisions, la dissimulation n'est pas importante.

Bien que la résistance aux collisions et la dissimulation soient les principales propriétés recherchées des fonctions de hachage en cryptographie, dans certaines applications, d'autres types de propriétés pourraient également être souhaitables.

### Notes
[^1] : Whitfield Diffie et Martin Hellman, “New directions in cryptography,” *IEEE Transactions on Information Theory* IT-22 (1976), pp. 644–654, à la p. 644 [^1].

[^2] : Ralph Merkle discute également d'un protocole d'échange de clés dans “Secure communications over insecure channels”, *Communications of the Association for Computing Machinery*, 21 (1978), 294–99. Bien que Merkle ait soumis cet article avant celui de Diffie et Hellman, il a été publié plus tard. La solution de Merkle n'est pas exponentiellement sécurisée, contrairement à celle de Diffie-Hellman [^2].

[^3] : Ron Rivest, Adi Shamir et Leonard Adleman, “A method for obtaining digital signatures and public-key cryptosystems”, *Communications of the Association for Computing Machinery*, 21 (1978), pp. 120–26 [^3].

[^4] : Une bonne histoire de ces découvertes est fournie par Simon Singh, *The Code Book*, Fourth Estate (Londres, 1999), Chapitre 6 [^4].
[^5]: Toute tentative de mise en place de schémas visant à garantir la non-répudiation, l'autre thème que nous avons discuté dans le *Chapitre 1*, devra à sa base impliquer des signatures numériques [^5].
[^6]: La terminologie de "cachette" n'est pas un langage courant, mais est spécifiquement tirée de Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller, et Steven Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Chapitre 1 [^6].

# Le cryptosystème RSA
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

Alors que la cryptographie symétrique est généralement assez intuitive pour la plupart des gens, ce n'est généralement pas le cas avec la cryptographie asymétrique. Bien que vous soyez probablement à l'aise avec la description de haut niveau offerte dans les sections précédentes, vous vous demandez probablement ce que sont précisément les fonctions à sens unique et comment elles sont exactement utilisées pour construire des schémas asymétriques.

Dans ce chapitre, je vais lever une partie du mystère entourant la cryptographie asymétrique, en examinant plus en détail un exemple spécifique, à savoir le cryptosystème RSA. Dans la première section, je vais introduire le problème de factorisation sur lequel se base le problème RSA. Je couvrirai ensuite un certain nombre de résultats clés de la théorie des nombres. Dans la dernière section, nous mettrons ces informations ensemble pour expliquer le problème RSA, et comment cela peut être utilisé pour créer des schémas cryptographiques asymétriques.

Ajouter cette profondeur à notre discussion n'est pas une tâche facile. Cela nécessite d'introduire un certain nombre de théorèmes et de propositions de théorie des nombres. Mais ne laissez pas les mathématiques vous dissuader. Travailler à travers cette discussion améliorera significativement votre compréhension de ce qui sous-tend la cryptographie asymétrique et représente un investissement valable.

Voyons maintenant d'abord le problème de factorisation.

## Le problème de factorisation
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Lorsque vous multipliez deux nombres, disons a et b, nous appelons les nombres a et b des **facteurs**, et le résultat le **produit**. Tenter d'écrire un nombre N sous la forme de la multiplication de deux ou plusieurs facteurs est appelé **factorisation** ou **factoring**.<sup>[1](#footnote1)</sup> Vous pouvez appeler tout problème nécessitant cela un **problème de factorisation**.

Il y a environ 2 500 ans, le mathématicien grec Euclide d'Alexandrie a découvert un théorème clé sur la factorisation des entiers. Il est communément appelé le **théorème de factorisation unique** et énonce ce qui suit :

*Théorème 1*. Tout entier N supérieur à 1 est soit un nombre premier, soit peut être exprimé comme un produit de facteurs premiers.

Toute la dernière partie de cette déclaration signifie simplement que vous pouvez prendre n'importe quel entier non premier N supérieur à 1, et l'écrire comme une multiplication de nombres premiers. Ci-dessous, plusieurs exemples d'entiers non premiers écrits comme le produit de facteurs premiers.

* 18 = 2 • 3 • 3 = 2 • 3<sup>2</sup>
* 84 = 2 • 2 • 3 • 7 = 2<sup>2</sup> • 3 • 7
* 144 = 2 • 2 • 2 • 2 • 3 • 3 = 2<sup>4</sup> • 3<sup>2</sup>
Pour les trois entiers mentionnés ci-dessus, calculer leurs facteurs premiers est relativement facile, même si vous n'avez que N. Vous commencez avec le plus petit nombre premier, à savoir 2, et voyez combien de fois l'entier N est divisible par celui-ci. Ensuite, vous passez à tester la divisibilité de N par 3, 5, 7, et ainsi de suite. Vous continuez ce processus jusqu'à ce que votre entier N soit écrit comme le produit de nombres premiers uniquement.
Prenons, par exemple, l'entier 84. Ci-dessous, vous pouvez voir le processus pour déterminer ses facteurs premiers. À chaque étape, nous prenons le plus petit facteur premier restant (à gauche) et déterminons le terme restant à factoriser. Nous continuons jusqu'à ce que le terme restant soit également un nombre premier. À chaque étape, la factorisation actuelle de 84 est affichée à l'extrême droite.

* Facteur premier = 2 : terme restant = 42 (84 = 2 • 42)
* Facteur premier = 2 : terme restant = 21 (84 = 2 • 2 • 21)
* Facteur premier = 3 : terme restant = 7 (84 = 2 • 2 • 3 • 7)
* Comme 7 est un nombre premier, le résultat est 2 • 2 • 3 • 7, ou 2<sup>2</sup> • 3 • 7.

Supposons maintenant que N est très grand. À quel point serait-il difficile de réduire N en ses facteurs premiers ?

Cela dépend vraiment de N. Supposons, par exemple, que N est 50 450 400. Bien que ce nombre semble intimidant, les calculs ne sont pas si compliqués et peuvent facilement être faits à la main. Comme ci-dessus, vous commencez juste avec 2 et continuez votre chemin. Ci-dessous, vous pouvez voir le résultat de ce processus de manière similaire à celle mentionnée ci-dessus.

* 2 : 25 225 200 (50 450 400 = 2 • 25 225 200)
* 2 : 12 612 600 (50 450 400 = 2<sup>2</sup> • 12 612 600)
* 2 : 6 306 300 (50 450 400 = 2<sup>3</sup> • 6 306 300)
* 2 : 3 153 150 (50 450 400 = 2<sup>4</sup> • 3 153 150)
* 2 : 1 576 575 (50 450 400 = 2<sup>5</sup> • 1 576 575)
* 3 : 525 525 (50 450 400 = 2<sup>5</sup> • 3 • 525 525)
* 3 : 175 175 (50 450 400 = 2<sup>5</sup> • 3<sup>2</sup> • 175 175)
* 5 : 35 035 (50 450 400 = 2<sup>5</sup> • 3<sup>2</sup> • 5 • 35 035)
* 5 : 7 007 (50 450 400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7 007)
* 7 : 1 001 (50 450 400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7 • 1 001) * 7 : 143 (50 450 400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 143)
* 11 : 13 (50 450 400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 11 • 13)
* Comme 13 est un nombre premier, le résultat est 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 11 • 13.

Résoudre ce problème à la main prend du temps. Un ordinateur, bien sûr, pourrait faire tout cela en une fraction de seconde. En fait, un ordinateur peut souvent même factoriser des entiers extrêmement grands en une fraction de seconde.

Il y a, cependant, certaines exceptions. Supposons que nous sélectionnons d'abord au hasard deux très grands nombres premiers. Il est typique de les étiqueter p et q, et j'adopterai cette convention ici.

Pour être concret, disons que p et q sont tous deux des nombres premiers de 1024 bits, et qu'ils nécessitent en effet au moins 1024 bits pour être représentés (donc le premier bit doit être 1). Ainsi, par exemple, 37 ne pourrait pas être l'un des nombres premiers. Vous pouvez certainement représenter 37 avec 1024 bits. Mais clairement *vous n'avez pas besoin* de tant de bits pour le représenter. Vous pouvez représenter 37 par n'importe quelle chaîne qui a 6 bits ou plus. (En 6 bits, 37 serait représenté comme 100101).

Il est important d'apprécier à quel point p et q sont grands s'ils sont sélectionnés selon les conditions ci-dessus. Comme exemple, j'ai sélectionné un nombre premier aléatoire qui nécessite au moins 1024 bits pour la représentation ci-dessous.

* 14 752 173 874 503 595 484 930 006 383 670 759 559 764 562 721 397 166 747 289 220 945 457 932 666 751 048 198 854 920 097 085 690 793 755 254 946 188 163 753 506 778 089 706 699 671 722 089 715 624 760 049 594 106 189 662 669 156 149 028 900 805 928 183 585 427 782 974 951 355 515 394 807 209 836 870 484 558 332 897 443 152 653 214 483 870 992 618 171 825 921 582 253 023 974 514 209 142 520 026 807 636 589

Supposons maintenant qu'après avoir sélectionné au hasard les nombres premiers p et q, nous les multiplions pour obtenir un entier N. Ce dernier entier est donc un nombre de 2048 bits qui nécessite au moins 2048 bits pour sa représentation. Il est beaucoup, beaucoup plus grand que p ou q.
Supposons que vous ne donniez à un ordinateur que N, et que vous lui demandiez de trouver les deux facteurs premiers de 1024 bits de N. La probabilité que l'ordinateur découvre p et q est extrêmement faible. On peut dire que c'est impossible à toutes fins pratiques. Cela est vrai, même si vous deviez employer un superordinateur ou même un réseau de superordinateurs.
Pour commencer, supposons que l'ordinateur tente de résoudre le problème en parcourant les nombres de 1024 bits, en testant dans chaque cas s'ils sont premiers et s'ils sont des facteurs de N. L'ensemble des nombres premiers à tester est alors d'environ 1.265 • 10<sup>305</sup>.<sup>[2](#footnote2)</sup>

Même si vous prenez tous les ordinateurs de la planète et que vous les faites essayer de trouver et tester des nombres premiers de 1024 bits de cette manière, une chance sur un milliard de trouver avec succès un facteur premier de N nécessiterait une période de calcul bien plus longue que l'âge de l'Univers.

Maintenant, en pratique, un ordinateur peut faire mieux que la procédure grossière décrite jusque-là. Il existe plusieurs algorithmes que l'ordinateur peut appliquer pour arriver à une factorisation plus rapidement. Le point, cependant, est que même en utilisant ces algorithmes plus efficaces, la tâche de l'ordinateur reste informatiquement infaisable.<sup>[3](#footnote3)</sup>

Il est important de noter que la difficulté de la factorisation dans les conditions décrites repose sur l'hypothèse qu'il n'existe pas d'algorithmes informatiquement efficaces pour calculer les facteurs premiers. Nous ne pouvons pas réellement prouver qu'un algorithme efficace n'existe pas. Néanmoins, cette hypothèse est très plausible : malgré des efforts considérables déployés sur des centaines d'années, nous n'avons pas encore trouvé un tel algorithme informatiquement efficace.

Ainsi, le problème de factorisation, dans certaines circonstances, peut vraisemblablement être considéré comme un problème difficile. Spécifiquement, lorsque p et q sont de très grands nombres premiers, leur produit N n'est pas difficile à calculer ; mais la factorisation donnée seulement N est pratiquement impossible.


## Résultats théoriques des nombres
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Malheureusement, le problème de factorisation ne peut pas être utilisé directement pour les schémas cryptographiques asymétriques. Cependant, nous pouvons utiliser un problème plus complexe mais lié à cet effet : le problème RSA.

Pour comprendre le problème RSA, nous devrons comprendre un certain nombre de théorèmes et propositions de la théorie des nombres. Ces derniers sont présentés dans cette section en trois sous-sections : (1) l'ordre de N, (2) l'inversibilité modulo N, et (3) le théorème d'Euler.

Une partie du matériel dans les trois sous-sections a déjà été introduite dans le *Chapitre 3*. Mais je vais ici réitérer ce matériel pour plus de commodité.


### L'ordre de N

Un entier a est **copremier** ou un **premier relatif** avec un entier N, si le plus grand diviseur commun entre eux est 1. Bien que 1 ne soit pas conventionnellement un nombre premier, il est un copremier de chaque entier (tout comme – 1).

Par exemple, considérons le cas où a = 18 et N = 37. Ce sont clairement des copremiers. Le plus grand entier qui se divise à la fois dans 18 et 37 est 1. Par contraste, considérons le cas où a = 42 et N = 16. Ce ne sont clairement pas des copremiers. Les deux nombres sont divisibles par 2, ce qui est supérieur à 1.
Nous pouvons maintenant définir l'ordre de N comme suit. Supposons que N est un entier supérieur à 1. L'**ordre de N** est alors le nombre de tous les nombres premiers entre eux avec N tels que pour chaque nombre premier entre eux a, la condition suivante est respectée : 1 ≤ a < N.
Par exemple, si N = 12, alors 1, 5, 7 et 11 sont les seuls nombres premiers entre eux qui répondent à la condition ci-dessus. Par conséquent, l'ordre de 12 est égal à 4.

Supposons que N est un nombre premier. Alors tout entier inférieur à N mais supérieur ou égal à 1 est premier entre eux avec lui. Cela inclut tous les éléments de l'ensemble suivant : {1,2,3….,N – 1}. Ainsi, lorsque N est premier, l'ordre de N est N – 1. Ceci est énoncé dans la proposition 1, où φ(N) désigne l'ordre de N.

**Proposition 1**. φ(N) = N – 1 lorsque N est premier

Supposons que N n'est pas premier. Vous pouvez alors calculer son ordre en utilisant **la fonction Phi d'Euler**. Bien que le calcul de l'ordre d'un petit entier soit relativement simple, la fonction Phi d'Euler devient particulièrement importante pour les grands entiers. La proposition de la fonction Phi d'Euler est énoncée ci-dessous.

*Théorème 2*. Soit N égal à p<sub>1</sub><sup>e_1</sup> • p<sub>2</sub><sup>e_2</sup> • … • p<sub>i</sub><sup>e_i</sup> • … • p<sub>n</sub><sup>e_n</sup>, où l'ensemble {p<sub>i</sub>} consiste en tous les facteurs premiers distincts de N et chaque e_i indique combien de fois le facteur premier p<sub>i</sub> se produit pour N. Alors, φ(N) = p<sub>1</sub><sup>e_1 - 1</sup> • (p<sub>1</sub> - 1) • p<sub>2</sub><sup>e_2 - 1</sup> • (p<sub>2</sub> - 1) • … • p<sub>n</sub><sup>e_n - 1</sup> • (p<sub>n</sub> - 1).

*Le Théorème 2* montre qu'une fois que vous avez décomposé tout N non premier en ses facteurs premiers distincts, il est facile de calculer l'ordre de N.

Par exemple, supposons que N = 270. C'est clairement pas un nombre premier. La décomposition de N en ses facteurs premiers donne l'expression : 2 • 3<sup>3</sup> • 5. Selon la fonction Phi d'Euler, l'ordre de N est alors comme suit :

* φ(N) = 2<sup>1 – 1</sup> (2 – 1) + 3<sup>3 – 1</sup> (3 – 1) + 5<sup>1 – 1</sup> (5 – 1) = 1 (1) + 9 (2) + 1 (4) = 1 + 18 + 4 = 23
Supposons ensuite que N soit le produit de deux nombres premiers, p et q. *Théorème 2* ci-dessus, indique alors que l'ordre de N est le suivant : p<sup>1 – 1</sup> (p – 1) x q<sup>1 – 1</sup> (q – 1) = (p – 1) x (q – 1). C'est un résultat clé pour le problème RSA en particulier, et est énoncé dans *Proposition 2* ci-dessous.
*Proposition 2*. Si N est le produit de deux nombres premiers, p et q, l'ordre de N est le produit (p – 1) x (q – 1).

Pour illustrer, supposons que N = 119. Ce nombre entier peut être factorisé en deux nombres premiers, à savoir 7 et 17. Ainsi, la fonction Phi d'Euler suggère que l'ordre de 119 est le suivant :

* φ(119) = (7 – 1) • (17 – 1) = 6 • 16 = 96.

En d'autres termes, le nombre entier 119 a 96 copremiers dans l'intervalle de 1 à 119. En fait, cet ensemble inclut tous les entiers de 1 à 119, qui ne sont pas des multiples de 7 ou de 17.

À partir de maintenant, désignons l'ensemble des copremiers qui détermine l'ordre de N par **C<sub>N</sub>**. Pour notre exemple où N = 119, l'ensemble **C<sub>119</sub>** est bien trop grand pour être listé complètement. Mais certains des éléments sont les suivants : **C<sub>119</sub>** = {1,2,….6,8….13,15,16,18,….,33,35….,96}.

### Inversibilité modulo N

Nous pouvons dire qu'un entier a est **inversible modulo N**, s'il existe au moins un entier b tel que a x b modulo N = 1 modulo N. Tout tel entier b est désigné comme un **inverse** (ou **inverse multiplicatif**) d'un donné par réduction modulo N.

Supposons, par exemple, que a = 5 et N = 11. Il y a de nombreux entiers par lesquels vous pouvez multiplier 5, de sorte que 5 x b mod 11 = 1 mod 11. Considérez, par exemple, les entiers 20 et 31. Il est facile de voir que ces deux entiers sont des inverses de 5 pour la réduction modulo 11.

* 5 x 20 mod 11 = 100 mod 11 = 1 mod 11
* 5 x 31 mod 11 = 155 mod 11 = 1 mod 11

Bien que 5 ait de nombreux inverses pour la réduction modulo 11, vous pouvez montrer qu'il existe seulement un seul inverse positif de 5 qui est inférieur à 11. En fait, cela n'est pas unique à notre exemple particulier, mais c'est un résultat général.

*Proposition 3*. Si l'entier a est inversible modulo N, il doit être le cas qu'exactement un inverse positif de a est inférieur à N. (Donc, cet inverse unique de a doit venir de l'ensemble {1,…,N – 1}).
Désignons l'inverse unique de a de la Proposition 3 comme a<sup>-1</sup>. Dans le cas où a = 5 et N = 11, vous pouvez voir que a<sup>-1</sup> = 9, étant donné que 5 x 9 mod 11 = 45 mod 11 = 1 mod 11.
Notez que vous pouvez également obtenir la valeur 9 pour a<sup>-1</sup> dans notre exemple en réduisant simplement tout autre inverse de a par modulo 11. Par exemple, 20 mod 11 = 31 mod 11 = 9 mod 11. Ainsi, chaque fois qu'un entier a > N est inversible modulo N, alors a mod N doit également être inversible modulo N.

Ce n'est pas nécessairement le cas qu'un inverse de a existe en réduction modulo N. Supposons, par exemple, que a = 2 et N = 8. Il n'existe aucun b, ou tout a<sup>-1</sup> spécifiquement, tel que 2 x b mod 8 = 1 mod 8. C'est parce que toute valeur de b produira toujours un multiple de 2, donc aucune division par 8 ne peut jamais donner un reste égal à 1.

Comment savons-nous exactement si un entier a a un inverse pour un N donné ? Comme vous l'avez peut-être remarqué dans l'exemple ci-dessus, le plus grand commun diviseur entre 2 et 8 est supérieur à 1, à savoir 2. Et ceci est en fait illustratif du résultat général suivant :

*Proposition 4*. Un inverse existe d'un entier a donné en réduction modulo N, et spécifiquement un inverse positif unique inférieur à N, si et seulement si le plus grand commun diviseur entre a et N est 1 (c'est-à-dire, s'ils sont copremiers).

Dans le cas où a = 5 et N = 11, nous avons conclu que a<sup>-1</sup> = 9, étant donné que 5 x 9 mod 11 = 45 mod 11 = 1 mod 11. Il est important de noter que l'inverse est également vrai. C'est-à-dire, quand a = 9 et N = 11, il est vrai que a<sup>-1</sup> = 5.

### Théorème d'Euler

Avant de passer au problème RSA, nous devons comprendre un autre théorème crucial, à savoir **le théorème d'Euler**. Il énonce ce qui suit :

*Théorème 3*. Supposons que deux entiers a et N sont copremiers. Alors, a<sup>φ(N)</sup> mod N = 1 mod N.

C'est un résultat remarquable, mais un peu déroutant au début. Tournons-nous vers un exemple pour le comprendre.

Supposons que a = 5 et N = 7. Ce sont en effet des copremiers comme le théorème d'Euler l'exige. Nous savons que l'ordre de 7 égale 6, étant donné que 7 est un nombre premier (voir **Proposition 1**).

Ce que le théorème d'Euler énonce maintenant, c'est que 5<sup>6</sup> mod 7 doit être égal à 1 mod 7. Voici les calculs pour montrer que cela est effectivement vrai.

* 5<sup>6</sup> mod 7 = 15 625 mod 7 = 1 mod N

L'entier 7 divise 15 624 un total de 2 233 fois. Ainsi, le reste de la division de 16 625 par 7 est 1.

Ensuite, en utilisant la fonction Phi d'Euler, *Théorème 2*, vous pouvez dériver *Proposition 5* ci-dessous.
*Proposition 5*. φ(a • b) = φ(a) • φ(b) pour tout entier positif a et b.
Nous ne montrerons pas pourquoi c'est le cas. Mais notons simplement que vous avez déjà vu des preuves de cette proposition par le fait que φ(p • q) = φ(p) • φ(q) = (p – 1) • (q – 1) lorsque p et q sont des nombres premiers, comme indiqué dans la *Proposition 2*.

Le théorème d'Euler en conjonction avec la *Proposition 5* a des implications importantes. Voyez ce qui se passe, par exemple, dans les expressions ci-dessous, où a et N sont copremiers.

* a<sup>2 • φ(N)</sup> mod N = a<sup>φ(N)</sup> • a<sup>φ(N)</sup> mod N = 1 • 1 mod N = 1 mod N
* a<sup>φ(N) + 1</sup> mod N = a<sup>φ(N)</sup> • a<sup>1</sup> mod N = 1 • a<sup>1</sup> mod N = a mod N
* a<sup>8 • φ(N) + 3</sup> mod N = a<sup>8 • φ(N)</sup> • a<sup>3</sup> mod N = 1 • a<sup>3</sup> mod N = a<sup>3</sup> mod N

Ainsi, la combinaison du théorème d'Euler et de la *Proposition 5* nous permet de calculer simplement un certain nombre d'expressions. En général, nous pouvons résumer l'aperçu comme dans la *Proposition 6*.

*Proposition 6*. a<sup>x</sup> mod N = a<sup>x mod φ(N)</sup>

Maintenant, nous devons tout assembler dans une dernière étape délicate.

Tout comme N a un ordre φ(N) qui inclut les éléments de l'ensemble **C<sub>N</sub>**, nous savons que l'entier φ(N) doit à son tour également avoir un ordre et un ensemble de copremiers. Posons φ(N) = R. Alors nous savons qu'il existe également une valeur pour φ(R) et un ensemble de copremiers **C<sub>R</sub>**.

Supposons que nous sélectionnons maintenant un entier e de l'ensemble **C<sub>R</sub>**. Nous savons d'après la *Proposition 3* que cet entier e n'a qu'un seul inverse positif unique inférieur à R. C'est-à-dire, e a un unique inverse de l'ensemble **C<sub>R</sub>**. Appelons cet inverse d. Étant donné la définition d'un inverse, cela signifie que e • d = 1 mod R.

Nous pouvons utiliser ce résultat pour faire une déclaration sur notre entier original N. Ceci est résumé dans la *Proposition 7*.

*Proposition 7*. Supposons que e • d mod φ(N) = 1 mod φ(N). Alors pour tout élément a de l'ensemble **C<sub>N</sub>** il doit être le cas que a<sup>e • d mod φ(N)</sup> = a<sup>1 mod φ(N)</sup> = a mod N.

Nous avons maintenant tous les résultats théoriques des nombres nécessaires pour énoncer clairement le problème RSA.

## Le cryptosystème RSA
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>
Nous sommes maintenant prêts à définir le problème RSA. Supposons que vous créez un ensemble de variables composé de p, q, N, φ(N), e, d et y. Nommons cet ensemble Π. Il est créé comme suit :
1. Générer deux nombres premiers aléatoires p et q de taille égale et calculer leur produit N.
2. Calculer l'ordre de N, φ(N), par le produit suivant : (p – 1) • (q – 1).
3. Sélectionner un e > 2 tel qu'il soit plus petit et premier avec φ(N).
4. Calculer d en fixant e • d mod φ(N) = 1.
5. Sélectionner une valeur aléatoire y qui est plus petite et première avec N.

Le problème RSA consiste à trouver un x tel que x<sup>e</sup> = y, tout en ayant seulement un sous-ensemble d'informations concernant Π, à savoir les variables N, e et y. Lorsque p et q sont très grands, typiquement il est recommandé qu'ils soient de taille 1024 bits, le problème RSA est considéré comme difficile. Vous pouvez maintenant comprendre pourquoi c'est le cas au vu de la discussion précédente.

Une manière simple de calculer x quand x<sup>e</sup> mod N = y mod N est simplement de calculer y<sup>d</sup> mod N. Nous savons que y<sup>d</sup> mod N = x mod N par les calculs suivants :

* y<sup>d</sup> mod N = x<sup>e • d</sup> mod N = x<sup>e • d mod φ(N)</sup> mod N = x<sup>1 mod φ(N)</sup> mod N = x mod N.

Le problème est que nous ne connaissons pas la valeur de d, car elle n'est pas donnée dans le problème. Par conséquent, nous ne pouvons pas calculer directement y<sup>d</sup> mod N pour produire x mod N.

Cependant, nous pourrions être capables de calculer indirectement d à partir de l'ordre de N, φ(n), car nous savons que e • d mod φ(N) = 1 mod φ(N). Mais par hypothèse, le problème ne donne pas non plus une valeur pour φ(N).

Finalement, l'ordre pourrait être calculé indirectement avec les facteurs premiers p et q, de sorte que nous puissions éventuellement calculer d. Mais par hypothèse, les valeurs de p et q ne nous ont pas été fournies non plus.

Strictement parlant, même si le problème de factorisation au sein d'un problème RSA est difficile, nous ne pouvons pas prouver que le problème RSA est également difficile. Il pourrait en effet exister d'autres moyens de résoudre le problème RSA qu'à travers la factorisation. Cependant, il est généralement accepté et supposé que si le problème de factorisation au sein du problème RSA est difficile, alors le problème RSA lui-même est également difficile.

Si le problème RSA est effectivement difficile, alors il produit une fonction à sens unique avec une trappe. La fonction ici est f(g) = g<sup>e</sup> mod N. Avec la connaissance de f(g), n'importe qui pourrait facilement calculer une valeur y pour un g particulier = x. Cependant, il est pratiquement impossible de calculer une valeur particulière x juste en connaissant la valeur y et la fonction f(g). L'exception est lorsque vous recevez une pièce d'information d, la trappe. Dans ce cas, vous pouvez simplement calculer y<sup>d</sup> pour obtenir x.

Prenons un exemple spécifique pour illustrer le problème RSA. Je ne peux pas sélectionner un problème RSA qui serait considéré comme difficile dans les conditions ci-dessus, car les nombres seraient trop lourds à gérer. Au lieu de cela, cet exemple est juste pour illustrer comment fonctionne généralement le problème RSA.
Pour commencer, supposons que vous sélectionnez deux nombres premiers aléatoires 13 et 31. Donc p = 13 et q = 31. Le produit N de ces deux premiers égale 403. Nous pouvons facilement calculer l'ordre de 403. Il est équivalent à (13 - 1) • (31 - 1) = 360.
Ensuite, comme dicté par l'étape 3 du problème RSA, nous devons sélectionner un copremier pour 360 qui est supérieur à 2 et inférieur à 360. Nous n'avons pas à sélectionner cette valeur de manière aléatoire. Supposons que nous sélectionnons 103. C'est un copremier de 360 car son plus grand diviseur commun avec 103 est 1.

L'étape 4 exige maintenant que nous calculions une valeur d telle que 103 • d mod 360 = 1. Ce n'est pas une tâche facile à la main lorsque la valeur de N est grande. Cela nécessite que nous utilisions une procédure appelée **algorithme euclidien étendu**.

Bien que je ne montre pas la procédure ici, elle donne la valeur 7 lorsque e = 103. Vous pouvez vérifier que la paire de valeurs 103 et 7 répond en effet à la condition générale e • d mod φ(n) = 1 à travers les calculs ci-dessous.

* 103 • 7 mod 360 = 721 mod 360 = 1 mod 360

Important, étant donné *Proposition 4*, nous savons qu'aucun autre entier entre 1 et 360 pour d ne produira le résultat que 103 • d = 1 mod 360. De plus, la proposition implique que sélectionner une valeur différente pour e, produira une valeur unique différente pour d.

Dans l'étape 5 du problème RSA, nous devons sélectionner un entier positif y qui est un plus petit copremier de 403. Supposons que nous fixons y = 2<sup>103</sup>. L'exponentiation de 2 par 103 donne le résultat ci-dessous.

* 2<sup>103</sup> mod 403 = 10,141,204,801,825,835,211,973,625,643,008 mod 403 = 349 mod 403

Le problème RSA dans cet exemple particulier est maintenant le suivant : On vous fournit N = 403, e = 103, et y = 349 mod 403. Vous devez maintenant calculer x tel que x<sup>103</sup> = 349 mod 403. C'est-à-dire, vous devez trouver que la valeur originale avant l'exponentiation par 103 était 2.

Ce serait facile (pour un ordinateur au moins) de calculer x si nous savions que d = 7. Dans ce cas, vous pourriez simplement déterminer x comme ci-dessous.

* x = y<sup>7</sup> mod 403 = 349<sup>7</sup> mod 403 = 630,634,881,591,804,949 mod 403 = 2 mod 403

Le problème est que vous n'avez pas reçu l'information que d = 7. Vous pourriez, bien sûr, calculer d à partir du fait que 103 • d = 1 mod 360. Le problème est que vous n'avez également pas reçu l'information que l'ordre de N = 360. Enfin, vous pourriez également calculer l'ordre de 403 en calculant le produit suivant : (p – 1) • (q – 1). Mais on ne vous a également pas dit que p = 13 et q = 31.
Bien sûr, un ordinateur pourrait encore résoudre le problème RSA pour cet exemple relativement facilement, car les nombres premiers impliqués ne sont pas grands. Mais lorsque les nombres premiers deviennent très grands, il est confronté à une tâche pratiquement impossible.

Nous avons maintenant présenté le problème RSA, un ensemble de conditions sous lesquelles il est difficile, et les mathématiques sous-jacentes. Comment tout cela aide-t-il avec la cryptographie asymétrique ? Spécifiquement, comment pouvons-nous transformer la difficulté du problème RSA sous certaines conditions en un schéma de chiffrement ou un schéma de signature numérique ?

Une approche consiste à prendre le problème RSA et à construire des schémas de manière directe. Par exemple, supposons que vous avez généré un ensemble de variables Π comme décrit dans le problème RSA, et assurez-vous que p et q sont suffisamment grands. Vous définissez votre clé publique égale à (N, e) et partagez cette information avec le monde. Comme décrit ci-dessus, vous gardez les valeurs de p, q, φ(n), et d secrètes. En fait, d est votre clé privée.

Quiconque veut vous envoyer un message m qui est un élément de **C<sub>N</sub>** pourrait simplement le chiffrer comme suit : c = m<sup>e</sup> mod N. (Le texte chiffré c ici est équivalent à la valeur y dans le problème RSA.) Vous pouvez facilement déchiffrer ce message en calculant juste c<sup>d</sup> mod N.

Vous pourriez tenter de créer un schéma de signature numérique de la même manière. Supposons que vous voulez envoyer à quelqu'un un message m avec une signature numérique S. Vous pourriez simplement définir S = m<sup>d</sup> mod N et envoyer la paire (m,S) au destinataire. N'importe qui peut vérifier la signature numérique simplement en vérifiant si S<sup>e</sup> mod N = m mod N. Cependant, tout attaquant aurait vraiment du mal à créer un S valide pour un message, étant donné qu'ils ne possèdent pas d.

Malheureusement, transformer ce qui est en soi un problème difficile, le problème RSA, en un schéma cryptographique n'est pas aussi simple. Pour le schéma de chiffrement direct, vous ne pouvez sélectionner que des copremiers de N comme vos messages. Cela ne nous laisse pas beaucoup de messages possibles, certainement pas assez pour une communication standard. De plus, ces messages doivent être sélectionnés aléatoirement. Cela semble quelque peu impraticable. Enfin, tout message qui est sélectionné deux fois produira exactement le même texte chiffré. C'est extrêmement indésirable dans tout schéma de chiffrement, et ne répond à aucune notion moderne rigoureuse de sécurité dans le chiffrement.

Les problèmes deviennent encore pires pour notre schéma de signature numérique direct. En l'état, n'importe quel attaquant peut facilement forger des signatures numériques simplement en sélectionnant d'abord un copremier de N comme signature puis en calculant le message original correspondant. Cela rompt clairement l'exigence d'infalsifiabilité existentielle.

Néanmoins, en ajoutant un peu de complexité astucieuse, le problème RSA peut être utilisé pour créer un schéma de chiffrement de clé publique sécurisé ainsi qu'un schéma de signature numérique sécurisé. Nous n'entrerons pas dans les détails de telles constructions ici.<sup>[4](#footnote4)</sup> Importamment, cependant, cette complexité supplémentaire ne change pas le problème RSA fondamental sous-jacent sur lequel ces schémas sont basés.

### Notes

[^1]: La factorisation peut également être importante pour travailler avec d'autres types d'objets mathématiques que les nombres. Par exemple, il peut être utile de factoriser des expressions polynomiales telles que x^2 – 2x + 1. Dans notre discussion, nous nous concentrerons uniquement sur la factorisation de nombres, spécifiquement des entiers [^1].
[^2]: Selon le théorème des nombres premiers, le nombre de nombres premiers inférieurs ou égaux à N est approximativement N/ln(N). Cela signifie que vous pouvez approximer le nombre de nombres premiers de longueur 1024 bits par 2^1024/ln(2^1024) - 2^1023/ln(2^1023) qui est égal à environ 1.265 x 10^305 [^2].

# Contributions
<partId>4556aab1-4876-552a-b6db-df6837bbf27a</partId>

## À propos
<chapterId>ff08a57b-740f-5d7e-8cf2-81db0908166e</chapterId>

Toutes les contributions sont les bienvenues. Avant de le faire, veuillez consulter les informations de fond sur mes propres plans pour le livre ainsi que les directives pour faire des contributions.

### Plans actuels

Mes plans actuels pour le développement ultérieur du livre sont les suivants :

- Créer un chapitre final qui entre dans les détails des applications cryptographiques pratiques, telles que la sécurité de la couche de transport, le routage en oignon et l'échange de valeur dans Bitcoin
- Créer de meilleures figures et diagrammes pour soutenir la discussion écrite
- Utiliser LaTeX Math ou une autre application de composition pour la notation formelle (plutôt que juste Markdown)

### Directives pour les contributions

Si vous avez des corrections mineures ou des suggestions concernant le texte existant, vous pouvez créer une demande de tirage ou soulever un problème. Si vous créez une demande de tirage, veuillez respecter les directives suivantes :

- Créez les commits sur une branche séparée dans votre fork du dépôt
- Étiquetez clairement les commits
- Créez des commits séparés pour des problèmes logiquement distincts afin de faciliter le processus de révision

Si vous avez des suggestions plus substantielles concernant le livre, veuillez soulever un problème ou me contacter directement à **jaburgers@protonmail.com**.

### Licence

Le travail dans ce dépôt est sous licence Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0).

Vous pouvez trouver une courte description de la licence [ici](https://creativecommons.org/licenses/by-nc-nd/4.0/).

Vous pouvez trouver une version complète de la licence [ici](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode).

## Notation
<chapterId>07250f8d-ad7c-5531-a70c-4417d6d1b865</chapterId>

### Termes clés

Les termes clés dans les primers sont introduits en les mettant en gras. Par exemple, l'introduction du chiffre Rijndael comme un terme clé se présenterait comme suit : **chiffre Rijndael**.

Les termes clés sont explicitement définis, sauf s'il s'agit de noms propres ou que leur signification est évidente dans la discussion.

Toute définition est généralement donnée lors de l'introduction d'un terme clé, bien que parfois il soit plus pratique de laisser la définition à un moment ultérieur.

### Mots et phrases soulignés

Les mots et les phrases sont soulignés via l'italique. Par exemple, la phrase "Souvenez-vous de votre mot de passe" se présenterait comme suit : *Souvenez-vous de votre mot de passe*.

### Notation formelle

La notation formelle concerne principalement les variables, les variables aléatoires et les ensembles.

* Variables : Elles sont généralement indiquées simplement par une lettre minuscule (par exemple, "x" ou "y"). Parfois, elles sont capitalisées pour plus de clarté (par exemple, "M" ou "K").
* Variables aléatoires : Elles sont toujours indiquées par une lettre majuscule (par exemple, "X" ou "Y").
* Ensembles : Ceux-ci sont toujours indiqués par des lettres en gras et en majuscules (par exemple, **S**)