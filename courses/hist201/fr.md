---
name: L'histoire de la création de Bitcoin
goal: Découvrir l'histoire des origines, du lancement et des premiers développements de Bitcoin.
objectives:
  - Contexte technique dans lequel Bitcoin a émergé
  - Lancement de Bitcoin par Satoshi Nakamoto
  - Évènements qui ont marqué son développement
---

# Une plongée dans l'histoire de la création de Bitcoin

Bienvenue dans ce cours consacré à l'histoire de la création de Bitcoin ! Vous y découvrirez le cheminement des évènements qui ont marqué sa conception, son lancement et sa lente évolution.

<!-- TODO -->

+++

# Introduction

## Introduction à l'histoire de la création de Bitcoin

Ce cours vise à vous raconter l'histoire de la création de Bitcoin comme vous ne l'avez jamais lu ailleurs. Celle-ci est trop souvent méconnue et il est salutaire de la connaître ne serait-ce que pour ne pas reproduire les erreurs du passé. Elle vous permettra également de mieux comprendre les rouages de Bitcoin, dont les fonctions ont été déterminés par le contexte entourant sa conception.

### Petit aperçu

Bitcoin a été conçu par un individu (ou un groupe) utilisant le pseudonyme de Satoshi Nakamoto. Le 31 octobre 2008, ce dernier a partagé un livre blanc décrivant son modèle via une obscure liste de diffusion de courrier électronique sur Internet. Le 8 janvier 2008, il a mis en application son concept en publiant le code source du logiciel et en lançant le réseau par le minage des premiers blocs de la chaîne. Soucieux d'attirer un nombre critiques d'utilisateurs, il a fait la promotion de sa création sur divers canaux de communication. Après des débuts difficiles, l'amorçage du système a finalement eu lieu en octobre 2009, lorsque l'unité de compte -- le bitcoin -- a acquis un prix. Puis les premiers services commerçants ont commencé à émerger. Le projet a réellement pris au cours de l'été 2010, suite à la publication d'un article sur le site populaire Slashdot. Le change avec le dollar, le minage de Bitcoin et le développement informatique du logiciel se sont considérablement améliorés. Satoshi Nakamoto s'est progressivement mis en retrait et il a fini par disparaître complètement au printemps 2011, après avoir transmis les accès à ses bras droits, Martti Malmi et Gavin Andresen. La communauté a su prendre le relai et porter le projet pour en faire ce qu'il est aujourd'hui.

Bien entendu, Bitcoin n'est pas quelque chose qui est sorti de nulle part. Sa création s'inscrit dans un contexte précis : la recherche d'un moyen de transcrire les propriétés de l'argent liquide dans le cyberespace. En particulier, ses éléments techniques sont le fruit de décennies de recherches et d'expérimentations qui l'ont précédé. Bitcoin repose ainsi sur :

- La signature numérique, issue de la cryptographie asymétrique née en 1976 ;
- Le consensus distribué, élaboré dans les années 1980 suite aux premiers développements d'Internet ;
- L'horodatage de documents, inventé au début des années 90 avec l'émergence des premières fonctions de hachage solides ;
- La preuve de travail, décrite et mise en application au cours des années 90.

Pour concevoir Bitcoin, Satoshi Nakamoto s'est grandement inspiré du modèle eCash proposé par David Chaum en 1982 et implémenté par le biais de son entreprise DigiCash dans les années 90. Ce modèle, qui reposait sur le procédé de signature aveugle, permettait aux utilisateurs de disposer d'une certaine confidentialité des échanges. Toutefois, il reposait sur un réseau centralisé de banques qui intervenaient pour empêcher la double dépense. Ainsi, lorsque DigiCash a fait faillite, le système s'est effondré. En permettant de ne plus avoir besoin de tiers de confiance, Bitcoin corrigeait ce problème.

La création de Bitcoin s'inscrivait également dans un contexte de fermeture des systèmes de monnaies privées tels que e-gold et Liberty Reserve. Il constituait en cela un modèle robuste de monnaie numérique, pouvant résister aux assauts directs de l'État fédéral américain. En répartissant le risque entre ses participants, à l'instar des systèmes de partage en pair à pair comme BitTorrent, il assurait sa propre survie.

Bitcoin a enfin hérité de l'éthos du mouvement des cypherpunks, un mouvement de cryptographes rebelles des années 90, qui cherchaient à préserver la confidentialité et la liberté des individus sur Internet par l'utilisation proactive de la cryptographie. Bitcoin est en continuité avec des projets comme b-money, bit gold ou encore RPOW imaginés à la fin des années 90 et au début des années 2000. Satoshi Nakamoto y a ainsi fait mention, bien qu'il n'en avait pas connaissance avant de concevoir Bitcoin et qu'il ne faisait probablement pas partie du mouvement d'origine.

### Précisions

Toutes les dates et les heures sont données selon le fuseau horaire UTC (correspondant au méridien de Greenwich) et peuvent ainsi différer des dates américaines. Il est vraisemblable que Satoshi Nakamoto se trouvait aux États-Unis lorsqu'il travaillait sur son projet. Toutefois, Bitcoin est un projet international et nous nous référerons donc au fuseau universel. Ainsi, nous dirons que le lancement effectif du réseau principal a eu lieu le 9 janvier à 2 heures 54 du matin, plutôt que le 8 janvier à 18 heures 54 (heure du Pacifique, UTC-8).

En plus des sources directes archivées sur Internet, nous nous basons sur un certain nombre d'ouvrages de référence. En voici les principaux :

- *The Genesis Book* d'Aaron van Wirdum, publié en 2024 ;
- *Digital Gold* de Nathaniel Popper, publié en 2014 ;
- *The Book of Satoshi* de Phil Champagne, publié en 2014 ;
- *Digital Cash* de Finn Brunton, publié en 2019 ;
- *This Machine Kills Secrets* d'Andy Greenberg, publié en 2012.

# Aux origines de Bitcoin

## eCash : l'argent liquide électronique chaumien

Avant d'aborder l'histoire proprement dite de la création de Bitcoin par Satoshi Nakamoto, il convient de parler de ce qui a précédé. Nous aborderons le sujet en trois parties : le concept d'argent liquide chaumien communément appelé *eCash*, les monnaies privées reposant sur les systèmes centralisés telles que e-gold, et les modèles techniques qui ont été imaginés avant la mise en place du système distribué robuste qu'est Bitcoin.

Le premier concept, eCash, est issu du travail de David Chaum, informaticien et cryptographe américain né en 1955, qui est considéré comme un pionnier dans le domaine des communications anonymes et comme un précurseur des cypherpunks. Ce dernier a contribué de façon majeure au développement de la cryptographie dans les années 80. Il a mis au point son système d'argent liquide (dit « chaumien ») dans le même temps, et a tenté de le mettre en application dans les années 90 par le biais de son entreprise DigiCash.

L'action de David Chaum faisait suite à une révolution conceptuelle : le dévoilement de la cryptographie asymétrique en 1976 par Whitfield Diffie et Martin Hellman. L'idée de monnaie numérique a également émergé de cette découverte primordiale. Outre la dissimulation de l'information contenue dans un message, la cryptographie asymétrique permettait la mise en place de procédés de signature. Il devenait ainsi possible pour une personne de prouver mathématiquement qu'elle était propriétaire d'un certain montant d'unités de compte numérique.

Dans ce chapitre, nous étudierons ce que la cryptographie asymétrique a apporté, comment David Chaum l'a utilisée pour concevoir eCash, et comment son concept a par la suite été mis en application.

### L'émergence de la cryptographie moderne

La cryptographie est la discipline qui a pour but la sécurisation de la communication en présence de tiers malveillants en assurant la confidentialité, l'authenticité et l'intégrité de l'information transmise.

Pendant des siècles, il s'agissait uniquement de dissimuler le contenu d'un message par une méthode de chiffrement reposant sur une clé unique servant à chiffrer et à déchiffrer ce message. C'est ce qu'on appelle la cryptographie *symétrique*. Le [code de César](https://fr.wikipedia.org/wiki/Chiffrement_par_décalage), consistant à remplacer chaque lettre d'un texte par une lettre à une distance fixe dans l'alphabet, en est l'exemple le plus connu (la distance choisie est alors la clé). Avec le développement de la télécommunication et avec la construction des premières machines à calculer et des ordinateurs au cours du XX^e siècle, les algorithmes de chiffrement se sont ensuite considérablement complexifiés. Toutefois, même si ce type de cryptographie fonctionne très bien, il possède un inconvénient majeur : la nécessité d'échanger la clé de manière sécurisée avant de pouvoir communiquer.

C'est pour résoudre ce problème que la cryptographie *asymétrique*, aussi appelée cryptographie à clé publique, est apparue. Celle-ci repose sur deux clés distinctes : une clé privée, censée rester secrète, et une clé publique, dérivée de la clé privée. La clé privée ne peut théoriquement pas être retrouvée facilement à partir de la clé publique, ce qui fait que cette dernière peut être partagée à tous en toute tranquillité.

Ce type de cryptographie permet à la fois de mettre en place des algorithmes de chiffrement et des procédés de signature. Le chiffrement asymétrique consiste à utiliser la clé publique comme une clé de chiffrement et la clé privée comme une clé de déchiffrement. L'utilisateur génère une paire de clés, conserve la clé privée et partage la clé publique à ses interlocuteurs pour qu'ils lui envoient des messages. Ce type de chiffrement est analogue à une boîte aux lettres que le destinataire utiliserait pour recevoir des lettres et dont lui seul posséderait la clé.

Le signature numérique repose à l'inverse sur le fait d'utiliser la clé privée comme une clé de signature et la clé publique comme clé de vérification. L'utilisateur génère une paire de clés, signe un message à l'aide de la clé privée et l'envoie à ses interlocuteurs, qui peuvent vérifier son authenticité en utilisant la clé publique. Ces dernier n'ont ainsi jamais besoin de connaître la clé privée.

La cryptographie asymétrique a été découverte indépendamment par plusieurs chercheurs au cours des années 70. Néanmoins, les premiers à présenter ce qu'ils avaient trouvé ont été Whitfield Diffie et Martin Hellman, deux cryptographes de l'université Stanford. Ainsi, en novembre 1976, ils ont publié un article intitulé « [New Directions in Cryptography](https://ee.stanford.edu/~hellman/publications/24.pdf) » dans la revue *IEEE Transactions on Information Theory*. Dans l'introduction de cet article, ils écrivaient :

> « Nous sommes aujourd'hui à la veille d'une révolution dans le domaine de la cryptographie. Le développement de matériel numérique bon marché a permis de s'affranchir des limites de conception de l'informatique mécanique et de ramener le coût des dispositifs cryptographiques de haute qualité à un niveau tel qu'ils peuvent être utilisés dans des applications commerciales telles que les distributeurs de billets distants et les terminaux d'ordinateurs. À leur tour, ces applications créent un besoin pour de nouveaux types de systèmes cryptographiques qui minimisent la nécessité de canaux de distribution de clés sécurisés et fournissent l'équivalent d'une signature écrite. Dans le même temps, les développements théoriques de la théorie de l'information et de l'informatique promettent de fournir des cryptosystèmes dont la sécurité est prouvée, transformant ainsi cet art ancien en science. »
>
> Original: "We stand today on the brink of a revolution in cryptography. The development of cheap digital hardware has freed it from the design limitations of mechanical computing and brought the cost of high grade cryptographic devices down to where they can be used in such commercial applications as remote cash dispensers and computer terminals. In turn, such applications create a need for new types of cryptographic systems which minimize the necessity of secure key distribution channels and supply the equivalent of a written signature. At the same time, theoretical developments in information theory and computer science show promise of providing provably secure cryptosystems, changing this ancient art into a science."

L'article décrivait un algorithme d'échange de clés (destiné à la transmission de clés secrètes pour le chiffrement symétrique) ainsi qu'un procédé de signature numérique. Il a ouvert la voie à une multitude d'innovations. L'une d'elle était le cryptosystème [RSA](https://people.csail.mit.edu/rivest/Rsapaper.pdf), qui a été créé en 1977 par les cryptographes Ronald Rivest, Adi Shamir et Leonard Adleman (qui leur ont donné son nom) et breveté par le MIT en 1983. Ce système permet à la fois de chiffrer et de signer des messages, grâce à l'interversion des rôles des clés. RSA a été présenté publiquement pour la première fois au sein d'un article de Martin Gardner publié dans le magazine *Scientific American* en août 1977, qui était intitulé « [Mathematical Games: A new kind of cipher that would take millions of years to break](https://simson.net/ref/1977/Gardner_RSA.pdf) » (en français : « Un nouveau type de code dont le déchiffrement prendrait des millions d'années »).

La découverte de la cryptographie asymétrique a également motivé la confection de fonctions à sens unique, qui ont pour particularité de rendre le calcul d'une image (sens direct) très facile et l'obtention d'un antécédent (sens inverse) très difficile. On a assisté en particulier au développement des premières fonctions de hachage cryptographiques, qui transformaient un message de taille variable en une empreinte de taille fixe. Entre 1989 et 1991, plusieurs algorithmes de hachage (MD2, MD4, MD5) ont été ainsi conçus par Ronald Rivest pour le MIT.

Les éléments cryptographiques de base de Bitcoin sont issus de ces recherches. Le schéma de signature ECDSA, permettant d'autoriser la dépense d'une transaction classique, a été créé en 1992 pour le NIST. La fonction de hachage SHA-256, intervenant à de multiples endroits dans le protocole, a elle été publiée en 2001, au sein de la suite d'algorithmes SHA-2 rendue publique par la NSA. Pour en savoir plus à ce sujet, vous pouvez vous reporter à la formation [Crypto 301](../crypto301/fr.md) présentée par Loïc Morel.

### Les signatures aveugles et l'argent liquide électronique

Cette révolution dans le domaine de la cryptographie a également inspiré le jeune David Chaum, originaire de la côté Ouest et alors doctorant à l'Université de Berkeley. Ce dernier s'est très vite pris de passion pour la protection de la vie privée. Il était en effet très inquiet pour l'avenir de la liberté et de la confidentialité dans la société informatisée en devenir. Dans son article fondateur, « [Security Without Identification: Transaction Systems to Make Big Brother Obsolete](https://www.cs.ru.nl/~jhh/pub/secsem/chaum1985bigbrother.pdf) » publié en 1985 dans *Communications of the ACM*, il écrivait :

> « Les bases d'une société de dossiers sont en train d'être établies, société dans laquelle les ordinateurs pourraient être utilisés pour déduire les modes de vie, les habitudes, les déplacements et les associations des individus à partir de données collectées dans le cadre de transactions de consommation ordinaires. L'incertitude quant à la sécurité des données contre les abus de ceux qui les conservent ou les exploitent peut avoir un "effet paralysant", incitant les gens à modifier leurs activités observables. À mesure que l'informatisation se généralise, ces problèmes risquent de s'aggraver considérablement. »
>
> Original: "The foundation is being laid for a dossier society, in which computers could be used to infer individuals' life-styles, habits, whereabouts, and associations from data collected in ordinary consumer transactions. Uncertainty about whether data will remain secure against abuse by those maintaining or tapping it can have a 'chilling effect,' causing people to alter their observable activities. As computerization becomes more pervasive, the potential for these problems will grow dramatically."

Cela explique son intérêt pour le domaine de la cryptographie, auquel il a contribué dès l'année 1979. En 1981, il a décrit les bases de la communication anonyme au travers de réseaux de mélange (*mix networks*), qui servirait notamment aux services de relai de courriel (Mixmaster) et au réseau anonyme Tor. En 1982, il a participé à la fondation de l'*International Association for Cryptologic Research* (IACR) lors de la conférence annuelle CRYPTO '82. La même année (et c'est ce qui nous intéresse ici), dans un article intitulé « [Blind Signature for Untraceable Payments](https://sceweb.sce.uhcl.edu/yang/teaching/csci5234WebSecurityFall2011/Chaum-blind-signatures.PDF) » il a publié le procédé de signature aveugle, qui est à la base de son modèle de monnaie électronique respectueux de la vie privée : eCash.

Le modèle eCash permet aux clients de réaliser des paiements qui sont relativement confidentiels. Les utilisateurs peuvent conserver des billets numériques directement. Il repose sur des serveurs, appelés des banques (*banks*) ou des monnaieries (*mints*), qui émettent et remplacent les billets des utilisateurs à chaque transaction. Lorsqu'un billet est transféré, le destinataire l'envoie à sa banque qui se charge de le vérifier et de lui en redonner un autre. Les banques entretiennent chacune un registre des billets dépensés pour empêcher la double dépense. Chaque système eCash est chapeauté par une autorité centrale qui délivre les habilitations.

Comme [l'expliquait](https://chaum.com/wp-content/uploads/2022/01/05-07-96-DigiCash_s-Ecash%E2%84%A2-to-be-Issued-by-Deutsche-Bank.pdf) David Chaum en 1996 :

> « Ecash [*sic*\] est une forme numérique d'argent liquide qui fonctionne sur Internet, où l'argent liquide papier ne peut pas exister. Comme les espèces, il offre aux consommateurs une réelle possibilité de cacher ce qu'ils achètent. »
>
> Original: "Ecash is a digital form of cash that works on the Internet where paper cash can't. Like cash, it offers consumers true privacy in what they buy."

Voyons maintenant comment intervient le procédé de signature aveugle dans le modèle... Ce procédé permet à un signataire de signer quelque chose sans voir ce qu'il signe et sans pour autant qu'il signe n'importe quoi.

![Création et remplacement d'un billet chaumien](assets/img/ch1/3.webp)
*Création et remplacement d'un billet chaumien (source : L'Élégance de Bitcoin)*

### Les mises en œuvre de eCash

CyberBucks, Magic Money, Mark Twain Bank

## Les systèmes centralisés

### Liberty Dollar

Monnaies privées avant Internet

### e-gold

Douglas Jackson, 1996, systèmes apparentés (Pecunix, e-Bullion, GoldMoney)

### PayPal

Peter Thiel, Confinity Inc., 1998

### Liberty Reserve

Arthur Budovsky, 2006

## Les systèmes décentralisés

### Le consensus distribué

Lamport et al., 1980

### L'horodatage de documents

Haber et Scornetta, 1991

### La preuve de travail

Adam Back, Hashcash, 1997

### b-money

Wei Dai, 1998

### bit gold

Nick Szabo, 1998

### RPOW

Hal Finney, 2004

### Ripple

Ryan Fugger, 2004

# L'action de Satoshi Nakamoto (2008 -- 2011)

## La naissance de Bitcoin (août 2008 -- janv. 2009)

### La préparation (août 2008 -- oct. 2008)

Contact d'Adam Back et de Wei Dai, brouillon de livre blanc, site web, dépôt SourceForge

### La publication du livre blanc (oct. 2008 -- déc. 2008)

Metzdowd Cryptography mailing list, document de 9 pages, critiques et réponses, code, bitcoin-list

### La sortie du logiciel et le lancement du réseau (janv. 2009)

Annonce sur la liste, version 0.1, réponse aux questions, échanges avec Hal Finney

## Présenter Bitcoin au monde (janv. 2009 -- oct. 2009)

### La communication de Satoshi (janv. 2009 -- févr. 2009)

21M, bloc de genèse, forum de la Fondation P2P, date de naissance

### Les outils de présentation (avr. 2009 -- nov. 2009)

Mike Hearn, Martti Malmi, page SourceForge, FAQ, forum, wiki

### Le développement initial du logiciel (avr. 2009 -- déc. 2009)

Martti Malmi, Linux, v0.2

### Les premiers mineurs de bitcoins (2009)

Dustin Trammell, James Howells, Martti Malmi, NewLibertyStandard

## L'amorçage (oct. 2009 -- mai 2010)

### Le premier service de change et le premier prix (oct. 2009)

NewLibertyStandard, échange avec Martti Malmi

### Les balbutiements de l'économie (oct. 2010 -- avr. 2010)

Premiers services (VPN, etc.), premières applications dépositaires (MyBitcoin), échanges sur IRC

### Le minage devient sérieux (déc. 2009 -- avr. 2010)

Augmentation de la difficulté, Lazslo Hanyecz, minage par GPU

### Le Bitcoin Pizza Day (22 mai 2010)

Lazslo Hanyecz, Jeremy Sturdivant

## Bitcoin prend ! (mai 2010 -- déc. 2010)

### L'arrivée de développeurs expérimentés (juin 2010 -- juil. 2010)

Gavin Andresen, Jeff Garzik, tcatm, gmaxwell

### Slashdotted (11 juillet 2010)

Version 0.3, présentation par teppy, augmentation du prix et du taux de hachage, création de Mt. Gox

### L'optimisation du minage (juil. 2010 -- nov. 2010)

Première ferme de minage (Artforz), première coopérative (slush)

### Les difficultés techniques (juil. 2010 -- sept. 2010)

Vulnérabilités majeures, server/daemon, 1 RETURN, value overflow, ajout de la limite de taille des blocs

## La disparition de Satoshi (déc. 2010 -- avr. 2011)

### L'affaire WikiLeaks (oct. 2010 -- déc. 2010)

Amir Taaki, PayPal, blocus financier, Wladimir van der Laan, Robert Horning

### Le retrait progressif de Satoshi (déc. 2010)

Opposition à WikiLeaks, « nid de frelons », dernier message public

### La transmission des accès et derniers courriels (déc. 2010 -- mai 2011)

Page de contact, Gavin Andresen, Martti Malmi, Mike Hearn

# L'après-Satoshi

## La prise de relai de la communauté (avr. 2011 -- avr. 2012)

### Le développement communautaire

Bitcoin Improvement Proposals (BIP), liste de diffusion bitcoin-dev, canal IRC, première conférence à New York

### Les portefeuilles SPV (mars 2011)

BitCoinJ (Mike Hearn), Bitcoin Wallet for Android (Andreas Schildbach), Electrum (Thomas Voegtlin)

### P2SH : la première discorde majeure (déc. 2011 -- avr. 2012)

OP\_EVAL, OP\_CHV, luke-jr, commentaire d'Amir Taaki, guerre des blocs

## Autres développements (2011 -- nov. 2012)

### Le change

Mt. Gox, TradeHill, Bitcoinica, BitInstant

### Le commerce

BitPay, Overstock.com

### Le dark web

Silk Road

### Le jeu d'argent

SatoshiDICE

### Le minage

Slushpool, Bitmain, voir min201 cryptomonnaies alternatives, changement de discours, premier halving
