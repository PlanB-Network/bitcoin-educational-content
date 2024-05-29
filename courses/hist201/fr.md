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

Le contenu est adapté (partiellement) de *L'Élégance de Bitcoin* (Ludovic Lars, 2024). En plus des sources directes archivées sur Internet, nous nous basons sur un certain nombre d'ouvrages de référence. En voici les principaux :

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

Cette révolution dans le domaine de la cryptographie a également inspiré le jeune David Chaum, informaticien originaire de la côté Ouest et alors doctorant à l'Université de Berkeley. Ce dernier s'est très vite pris de passion pour la protection de la vie privée. Il était en effet très inquiet pour l'avenir de la liberté et de la confidentialité dans une société qui était destinée à s'informatiser de plus en plus. Dans son article fondateur, « [Security Without Identification: Transaction Systems to Make Big Brother Obsolete](https://www.cs.ru.nl/~jhh/pub/secsem/chaum1985bigbrother.pdf) » publié en 1985 dans *Communications of the ACM*, il écrivait :

> « Les bases d'une société de dossiers sont en train d'être établies, société dans laquelle les ordinateurs pourraient être utilisés pour déduire les modes de vie, les habitudes, les déplacements et les associations des individus à partir de données collectées dans le cadre de transactions de consommation ordinaires. L'incertitude quant à la sécurité des données contre les abus de ceux qui les conservent ou les exploitent peut avoir un "effet paralysant", incitant les gens à modifier leurs activités observables. À mesure que l'informatisation se généralise, ces problèmes risquent de s'aggraver considérablement. »
>
> Original: "The foundation is being laid for a dossier society, in which computers could be used to infer individuals' life-styles, habits, whereabouts, and associations from data collected in ordinary consumer transactions. Uncertainty about whether data will remain secure against abuse by those maintaining or tapping it can have a 'chilling effect,' causing people to alter their observable activities. As computerization becomes more pervasive, the potential for these problems will grow dramatically."

Cela explique son intérêt pour le domaine de la cryptographie, auquel il a contribué dès l'année 1979. En 1981, il a décrit les bases de la communication anonyme au travers de réseaux de mélange (*mix networks*), qui servirait notamment aux services de relai de courriel (Mixmaster) et au réseau anonyme Tor. En 1982, il a participé à la fondation de l'*International Association for Cryptologic Research* (IACR) lors de la conférence annuelle CRYPTO '82. La même année (et c'est ce qui nous intéresse ici), dans un article intitulé « [Blind Signature for Untraceable Payments](https://sceweb.sce.uhcl.edu/yang/teaching/csci5234WebSecurityFall2011/Chaum-blind-signatures.PDF) » il a publié le procédé de signature aveugle, qui est à la base de son modèle de monnaie électronique respectueux de la vie privée : eCash.

Comme [l'expliquait](https://chaum.com/wp-content/uploads/2022/01/05-07-96-DigiCash_s-Ecash%E2%84%A2-to-be-Issued-by-Deutsche-Bank.pdf) David Chaum en 1996 dans un communiqué de presse :

> « Ecash [*sic*\] est une forme numérique d'argent liquide qui fonctionne sur Internet, où l'argent liquide papier ne peut pas exister. Comme les espèces, il offre aux consommateurs une réelle possibilité de cacher ce qu'ils achètent. »
>
> Original: "Ecash is a digital form of cash that works on the Internet where paper cash can't. Like cash, it offers consumers true privacy in what they buy."

Le modèle eCash est un concept de monnaie numérique permettant aux clients de réaliser des paiements qui sont relativement confidentiels. C'est une forme d'argent liquide, dans le sens où les utilisateurs peuvent conserver des billets numériques directement et pas sur un compte géré par un tiers de confiance. Le système repose cependant sur des serveurs, appelés des banques (*banks*) ou des monnaieries (*mints*), qui émettent et remplacent les billets des utilisateurs à chaque transaction. Lorsqu'un billet est transféré, le destinataire l'envoie à sa banque qui se charge de le vérifier et de lui en redonner un ou plusieurs autres. Les banques entretiennent chacune un registre des billets dépensés pour empêcher la double dépense. Chaque système eCash est chapeauté par une autorité centrale qui délivre les habilitations.

Les billets numériques peuvent être émis sans garantie ou bénéficier d'une adossement. Dans le premier cas, ils forment une monnaie de base qui doit acquérir une valeur en soi. Dans le second cas, ils sont adossés à une autre monnaie (typiquement le dollar) et l'utilisateur peut à tout moment rendre ses billets à sa banque pour récupérer la somme correspondante.

Dans son fonctionnement technique, le modèle eCash se fonde sur le procédé de signature aveugle, qui permet à un signataire de signer quelque chose sans voir ce qu'il signe. Chaque billet est généré par un utilisateur, puis signé par une banque pour en assurer l'authenticité, sans que la banque ne puisse identifier le billet. Chaque billet représente une quantité précise d'unités monétaires (coupure) et chaque banque du système dispose d'une clé privée pour signer chaque type de coupure. La procédure mathématique qui intervient (que nous ne décrirons pas ici) est analogue à la signature d'un billet physique en [papier carbone](https://fr.wikipedia.org/wiki/Papier_carbone) situé dans une enveloppe fermée.

Voici une illustration des différentes étapes qui interviennent dans la création et le remplacement d'un billet chaumien (provenant de *L'Élégance de Bitcoin*) :

![Création et remplacement d'un billet chaumien](assets/img/ch1/3.webp)

Les étapes (qui correspondent chacune à une opération mathématique ou à une transmission d'information) sont les suivantes :

1. Une utilisatrice nommée Alice crée un billet en papier carbone ;
2. Elle le place dans une enveloppe fermée ;
3. Alice envoie l'enveloppe contenant son billet à la banque et lui communique la coupure souhaitée ;
4. La banque signe l'enveloppe en indiquant la quantité d'unités que le billet représente, ce qui a pour effet de signer le billet en papier carbone à l'intérieur ;
5. La banque renvoie l'enveloppe à Alice ;
6. Alice ouvre l'enveloppe pour récupérer son billet signé ;
7. Elle vérifie que la signature de la banque est authentique.

Le transfert du billet signé se fait en le donnant à un autre utilisateur du système que nous appelerons Bob. Les étapes sont les suivantes :

- Alice transmet le billet à Bob ;
- Ce dernier vérifie qu'il a bien été signé par la banque d'Alice ;
- Il envoie immédiatement le billet réceptionné à sa banque ;
- La banque de Bob vérifie que le billet n'a pas déjà été utilisé et, le cas échéant, signe un nouveau billet ou crédite le compte de Bob (s'il y a un adossement).

Tout ceci implique qu'aucune banque du système ne peut relier le paiement à l'identité d'Alice, ce qui explique pourquoi on parle de confidentialité pour le client. Le commerçant (ici Bob) en revanche est obligé de passer par une banque pour confirmer le paiement, et sa banque peut donc avoir connaissance des montants reçus. De plus, le système dépend d'un tiers de confiance -- l'autorité centrale qui désigne les banques participantes -- ce qui le rend fragile.

### Les mises en œuvre de eCash

En 1990, David Chaum a fondé sa propre société, DigiCash B.V., pour mettre en application son idée d'argent liquide électronique. Cette entreprise était basée à Amsterdam aux Pays-Bas et détenait les brevets de son invention. À l'époque, Internet était encore naissant (le Web était encore en développement) et le commerce électronique inexistant ; ainsi, le modèle eCash constituait une formidable opportunité.

Toutefois, ce n'est l'entreprise de David Chaum qui a testé pour la première fois le modèle : ce sont les cypherpunks qui ont mis en œuvre la chose sans tenir compte des brevets et qui n'ont pas demandé l'autorisation. Ainsi, un protocole nommé Magic Money a été [proposé](https://cypherpunks.venona.com/date/1994/02/msg00247.html) sur la liste de diffusion des cypherpunks le 4 février 1994 par un développeur anonyme se faisant appeler Pr0duct Cypher. Ce protocole permettait de créer sa monnaie en faisant fonctionner un serveur de courrier électronique qui servait de monnaierie eCash. Les cypherpunks ont joué avec en créant toutes sortes d'unités de compte comme les Tacky Tokens, les GhostMarks, les DigiFrancs ou encore les NexusBucks. L'utilité de ces jetons était cependant minimale, et les échanges très rares.

Du côté de DigiCash, après quelques années de développement, un prototype a été [présenté](https://chaum.com/wp-content/uploads/2022/01/05-27-94-World_s-first-electronic-cash-payment-over-computer-networks.pdf) en mai 1994 lors de la première conférence internationale sur le World Wide Web au CERN à Genève. La société a ensuite réalisé un essai qui a débuté le 19 octobre de cette année, avec l'émission de CyberBucks qui n'étaient pas adossés à une autre monnaie. Divers commerçants acceptaient les CyberBucks dans le cadre de cette expérience. Les cypherpunks se sont également appropriés la chose en l'utilisant pour procéder à des échanges réels. Les CyberBucks ont ainsi acquis une valeur. Cependant, celle-ci s'est effondrée lorsque eCash a été déployé dans le système bancaire classique.

L'arrivée de eCash dans le système bancaire a commencé en octobre 1995 avec le début du partenariat de DigiCash avec la Mark Twain Bank, une petite banque du Missouri. Contrairement au cas des CyberBucks dont le taux de change était flottant, l'unité de compte était adossée au dollar américain. Entre 1996 et 1998, six banques ont suivi la Mark Twain Bank : la Merita Bank en Finlande, la Deutsche Bank en Allemagne, l'Advance Bank en Australie, la Bank Austria en Autriche, la Den norske Bank en Norvège et le Crédit Suisse en Suisse. La presse promettait alors à ce système un avenir radieux.

Néanmoins, tout ne s'est pas passé comme prévu. À cause de son caractère têtu et suspicieux, David Chaum a souhaité garder le contrôle sur son entreprise et a refusé des partenariats avec de grands acteurs financiers comme ING et ABN AMRO, Visa, Netscape et Microsoft. Il a quitté son poste en 1997 et la même année l'entreprise a déménagé son siège social en Californie. Durant l'année 1998, les banques partenaires ont annoncé abandonner eCash. DigiCash a fini par faire faillite en novembre 1998, mettant fin à la mise en œuvre de l'argent liquide électronique chaumien.

### L'héritage du modèle de David Chaum

Le développement du modèle eCash n'a cependant pas été infructueux. Il a été à la base de multiples initiatives.

Au cours des années 90, d'autres solutions techniques permettant de faire des paiements sur Internet ont profité de la tendance lancée par eCash : c'était le cas de CyberCash, First Virtual ou Open Market, qui profitait des inconvénients des paiements par carte bancaire qui étaient peu pratiques, coûteux et peu sécurisés à l'époque. Des systèmes de micropaiements ont également fait leur apparition à l'instar de CyberCoin (géré par CyberCash), NetBill et MilliCent. Ces systèmes n'ont jamais réellement pris, mais ils ont ouvert la voie au développement de PayPal à partir de 1999.

D'autres systèmes centralisés alternatifs sont également apparus en parallèle, comme e-gold et Liberty Reserve. Ces derniers géraient des monnaies numériques privées et bénéficiaient du flou juridique qui pouvait exister dans le cyberespace. Nous en parlerons dans le chapitre suivant.

Ensuite, eCash a inspiré les cypherpunks qui ont mis au point leurs propres modèles tels que b-money, bit gold et RPOW. Ils y ont ajouté de la preuve de travail et d'autres éléments. Nous étudierons ces concepts dans le chapitre 3.

Enfin, le modèle de David Chaum a considérablement influencé Satoshi Nakamoto lorsqu'il a mis en point Bitcoin. En témoignent les multiples références dans le [livre blanc](https://bitcoin.org/bitcoin.pdf) (le titre, la description du problème dans la section 2, le nom du PDF [envoyé](https://gwern.net/doc/bitcoin/2008-nakamoto) à Wei Dai en août 2008), ainsi que ses interventions privées et publiques. En ce sens, eCash est le prédécesseur principal de Bitcoin, même s'il n'en est pas le seul.

Avec Bitcoin, Satoshi Nakamoto a créé une monnaie numérique robuste et confidentielle. En ceci, il a réalisé la [prédiction](https://www.youtube.com/watch?v=mlwxdyLnMXM&t=872s) de Milton Friedman, prix Nobel d'économie et fondateur de l'École de Chicago, qui disait au micro de la National Taxpayers Union Foundation en 1999 :

> « Je pense qu'Internet va devenir l'une des forces majeures qui va réduire le rôle de l'État. La seule chose qui manque, mais qui sera bientôt développée, c'est un argent liquide électronique fiable, une méthode qui permette de transférer des fonds de A à B sur Internet sans que A connaisse B ou que B connaisse A. »
>
> Original: "I think that the Internet is going to be one of the major forces for reducing the role of government. The one thing that's missing, but that will soon be developed, is a reliable e-cash, a method whereby on the internet you can transfer funds from A to B without A knowing B or B knowing A."

## Les monnaies privées centralisées avant Bitcoin

Dans le chapitre précédent, nous avons étudié la première forme d'argent liquide électronique qui est issue de l'apparition d'Internet et de la cryptographie moderne : le modèle eCash de David Chaum. Ce dernier a grandement influencé Satoshi Nakamoto et constitue une étape clé dans le parcours qui a mené à Bitcoin. Mais l'histoire des origines de la cryptomonnaie ne se résume pas à eCash ; elle repose aussi sur les expériences de monnaie privées fonctionnant sur Internet, qui ont été développées à partir de la fin des années 1990.

Dans ce chapitre, nous regarderons ce qui a été fait du côté des monnaies privées au États-Unis. Nous évoquerons tout d'abord le cas du Liberty Dollar. Puis nous nous intéresserons au cas des systèmes centralisés comme e-gold et Liberty Reserve. Nous parlerons pour finir de PayPal, dont la démarche est différente mais qui n'en constitue pas moins un exemple éclairant.

Dans tous les cas, ces systèmes ont fini par être arrêtés par les autorités ou ont dû se conformer aux réglementations financières. C'est pourquoi Satoshi Nakamoto, qui avait une bonne connaissance de ces systèmes, comprenait profondément la nécessité pour un système alternatif de ne pas reposer sur un tiers de confiance.

### La liberté monétaire aux États-Unis et le Liberty Dollar

L'histoire des États-Unis a été caractérisée par une grande pluralité monétaire dès ses débuts. Du XVII^e siècle à la moitié XIX^e siècle, la colonie anglaise devenue république indépendante autorisait en effet la libre circulation de devises étrangères (le dollar étasunien n'a été créé officiellement qu'en 1792), ainsi que la [frappe privée](https://fee.org/articles/private-coinage-in-america/) de pièces de monnaie en or et en argent. Une relative [liberté bancaire](https://iea.org.uk/wp-content/uploads/2023/12/Dowd-Free-Banking-Interactive.pdf) a également prévalu entre 1837 et 1863.

Toutefois, les choses ont changé avec la guerre de Sécession, gagnée par l'Union, dans un processus de centralisation du pouvoir. Ainsi, une loi du Congrès du 8 juin 1864 a interdit la frappe privée de pièces. Cette loi, qui est aujourd'hui devenue la section 486 du titre 18 du Code des États-Unis (*18 U.S. Code § 486*), [disposait](https://www.law.cornell.edu/uscode/text/18/486) :

> « Quiconque, sauf dans le cas où cela est autorisé par la loi, fabrique, met en circulation ou fait passer, ou tente de mettre en circulation ou de faire passer, des pièces d'or ou d'argent ou d'autres métaux, ou des alliages de métaux, destinées à être utilisées comme monnaie courante, qu'elles ressemblent à des pièces des États-Unis ou de pays étrangers, ou qu'elles soient de conception originale, sera condamné à une amende en vertu du présent titre ou à une peine d'emprisonnement de cinq ans au maximum, ou aux deux. »
>
> Original: "Whoever, except as authorized by law, makes or utters or passes, or attempts to utter or pass, any coins of gold or silver or other metal, or alloys of metals, intended for use as current money, whether in the resemblance of coins of the United States or of foreign countries, or of original design, shall be fined under this title or imprisoned not more than five years, or both."

Pour faire appliquer ces restrictions, une agence étatique a été fondée en 1965 par Abraham Lincoln : le Secret Service. La mission initiale du Secret Service était de lutter contre le faux-monnayage et la fraude financière en général. Elle servait, de façon détournée, à affermir le seigneuriage de l'État fédéral en confiant le monopole sur la production de monnaie à l'*United States Mint*.

La situation s'est encore plus restreinte par la suite. La banque centrale, appelée la Réserve Fédérale des États-Unis, a été créée en 1913, conséquemment à la panique bancaire de 1907. Puis, l'étalon-or classique a été abandonné en 1933 dans le cadre du *New Deal* de F.D. Roosevelt, avec l'ordre exécutif 6102 qui interdisait aux particuliers et aux entreprises situées aux États-Unis de détenir de l'or. La référence à l'or dans le système monétaire a finalement été abandonnée en 1971 lorsque Richard Nixon a annoncé mettre fin à la convertibilité du dollar en or à l'international.

Avec l'abrogation de l'interdiction de la détention d'or et le développement d'Internet à partir des années 1970, l'idée de déployer des monnaies privées est réapparue. Ç'a été le cas de Bernard von NotHaus, qui a lancé le Liberty Dollar en 1998, une monnaie basée sur l'or et l'argent qu'on pouvait retrouver sous forme de pièces d'argent et de billets représentatifs. Le système était géré par une organisation à but non lucratif appelée NORFED ("*National Organization for the Repeal of the Federal Reserve and Internal Revenue Code*"). À partir de 2003, le Liberty Dollar était également disponible sous forme numérique, au travers d'un système de comptes à la e-gold (voir section suivante). Le système a connu un certain succès. Outre les pièces de monnaies en circulation, les coffres de NORFED contenaient environ 8 millions de dollars en métaux précieux pour assurer la convertibilité de la devise, dont 6 pour garantir l'unité numérique.

![Pièce de Liberty Dollar en argent 2003](assets/img/ch2/1.webp)

[Pièce de Liberty Dollar (10 $) en argent (2003)](https://en.numista.com/catalogue/exonumia242820.html)

En septembre 2006, l'*U.S. Mint* a émis un [communiqué de presse](https://www.usmint.gov/news/press-releases/20060914-liberty-dollars-not-legal-tender-united-states-mint-warns-consumers), écrit conjointement avec le département de la Justice, dans lequel elle concluait que l'utilisation des pièces de NORFED violait la section 486 du titre 18 du Code des États-Unis et constituait « un crime fédéral ». Par conséquent, après une descente du FBI dans les locaux de NORFED en 2007, les violations ont été retenues contre NotHaus et ses associés, qui ont été arrêtés en 2009 et jugés en mars 2011. En 2014, Bernard von NotHaus a été condamné en appel à six mois d'assignation à résidence et à trois ans de liberté conditionnelle.

### e-gold : de l'or sur le Web

Le système e-gold était ce qu'on appelle une « devise en or numérique » (ou *digital gold currency* en anglais), c'est-à-dire une monnaie transférée électroniquement et
garantie intégralement par une quantité équivalente en or conservée en lieu sûr. Il a été cofondé par Douglas Jackson et Barry Downey en 1996. Douglas Jackson était un
cancérologue américain vivant en Floride, qui était adepte de l'économiste autrichien Friedrich von Hayek et qui souhaitait créer une « [meilleure monnaie](https://blog.bettermoney.com/) » avec e-gold.

Le principe est que chaque unité d'e-gold peut être convertie en or réel. Les réserves d'or étaient administrée par une société située aux États-Unis appelée Gold & Silver Reserve Inc. (G&SR). Le système informatique était géré par une deuxième entreprise, e-gold Ltd., enregistrée à Saint-Christophe-et-Niévès dans les Caraïbes. L'or n'était pas le seul métal concerné : les utilisateurs pouvaient aussi détenir et échanger de l'e-silver, de l'e-platinum et de l'e-palladium sur le même modèle.

Le système e-gold profitait du Web naissant, et en particulier du tout récent navigateur Netscape. Chaque client pouvait avoir accès à son compte depuis le site web. Pour l'époque, il était très performant, mettant à profit un système à règlement brut en temps réel inspiré du virement interbancaire. Voici à quoi ressemblait l'envoi d'e-gold en 2005 (image tirée d'un [tutoriel](https://www.geocities.ws/rizuan_mahrol/setpbystep.html) de l'époque) :

![Envoi sur e-gold en 2005](assets/img/ch2/2.webp)

Le système e-gold a rencontré un grand succès : à son apogée en 2006, il [garantissait](https://web.archive.org/web/20060907024202if_/http://www.e-gold.com:80/examiner.html) 3,6 tonnes d'or, soit plus de 80 millions de dollars, [traitait](https://web.archive.org/web/20060208044937/http://www.e-gold.com/stats.html) 75 000 transactions par jour, pour un volume annualisé de 3 milliards de dollars, et gérait plus de 2,7 millions de comptes.

Ce succès s'est néanmoins estompé avec l'intervention étatique. Au terme d'une enquête menée par le Secret Service, Douglas Jackson, ses deux sociétés et ses associés ont été [inculpés](https://www.justice.gov/archive/opa/pr/2007/April/07_crm_301.html) le 27 avril 2007 par le département de la Justice pour facilitation de blanchiment d'argent et activité de transfert d'argent sans licence. En novembre 2008, Douglas Jackson a été jugé coupable et a notamment été condamné à 3 ans de liberté surveillée, incluant 6 mois d'assignation à résidence sous surveillance électronique. Après une tentative infructueuse d'obtenir une licence, e-gold a dû fermer ses portes définitivement en novembre 2009.

D'autres systèmes ont été créés sur le même modèle. Nous pouvons citer GoldMoney, fondé par James Turk et son fils en février 2001, qui s'est aujourd'hui adapté aux réglementations financières. e-Bullion, le système fondé par James Fayed en juillet 2001, a lui fermé ses portes en 2008. Enfin, l'une des dernières devises en or numérique était Pecunix, qui a été fondée au Panama par Simon Davis en 2002 et qui s'est arrêtée en 2015, dans le cadre d'une escroquerie de sortie.

### Liberty Reserve, l'alternative à la Federal Reserve

Un autre exemple de monnaie privée centralisée était le système Liberty Reserve, qui permettait à ses utilisateurs de détenir et de transférer des devises électroniques indexées sur le dollar étasunien, sur l'euro ou sur l'or. Ce système a été créé par Arthur Budovsky, un Américain d'origine ukrainienne, et Vladimir Kats, immigré russe de Saint-Petersbourg. En 2006, Arthur Budovsky s'est expatrié au Costa Rica, alors considéré comme un paradis fiscal, où il a enregistré sa société, Liberty Reserve S.A.

Le système était assez similaire à e-gold, à l'exception faite que les fonds (en dollars principalement) étaient conservés sur des comptes en banque *offshore*, et non pas dans des coffres propres. Il a grandement bénéficié de l'arrêt de ce dernier en avril 2007 suite à l'inculpation de Douglas Jackson et de ses associés. En mai 2013, [d'après le département de la Justice américaine](https://www.justice.gov/sites/default/files/usao-sdny/legacy/2015/03/25/Liberty%20Reserve%2C%20et%20al.%20Indictment%20-%20Redacted_0.pdf), Liberty Reserve possédait plus d'un million d'utilisateurs dans le monde, dont plus de 200 000 aux États-Unis, et traitait 12 millions de transactions financières annuellement, pour un volume combiné de plus de 1,4 milliard de dollars. L'utilisation se faisait majoritairement dans le cadre d'activités criminelles, mais [ne se limitait pas](https://web.archive.org/web/20150422023243/https://www.theatlantic.com/magazine/archive/2015/05/bank-of-the-underworld/389555/) à ces dernières : Liberty Reserve était aussi utilisé par les traders du Forex ou bien pour les transferts à l'étranger.

Toutefois, le système a fini par subir le même sort que e-gold. En 2009, la Superintendencia General de Entidades Financieras costaricaine s'est intéressée au cas de Liberty Reserve, lui demandant d'obtenir une licence (ce que la société n'est pas parvenue à faire). En novembre 2011, le FinCEN étasunien qui a délivré un avis selon lequel le système était « utilisé par les criminels pour effectuer des transactions anonymes ». Enfin, Liberty Reserve a été arrêtée au terme d'une opération internationale : le 24 mai 2013, Arthur
Budovsky et ses principaux associés ont été inculpés et arrêtés dans des juridictions différentes (Espagne, États-Unis, Costa Rica) et le site principal a été saisi par le département de la Justice. En 2016, après une extradition vers les États-Unis, Arthur Budovsky a été condamné à 20 ans de prison ferme pour blanchiment d'argent.

Cet exemple montre ainsi que l'arbitrage juridictionnel ne suffit pas pour protéger la monnaie de l'intervention étatique.

### PayPal et la vision de Peter Thiel

Il faut enfin évoquer le cas de PayPal. Si ses créateurs n'avaient pas pour intention d'en faire une monnaie indépendante du système en place, il n'en reste pas moins qu'ils envisageaient que ce produit, conformément à l'idéologie disruptrice de la Silicon Valley. Le produit PayPal a été développé par la société Confinity Inc., cofondée en décembre 1998 à San Francisco par Max Levchin et Peter Thiel, qui s'étaient rencontrés quelques mois plus tôt à l'université Stanford. La société, au départ appelée FieldLink, avait pour but initial de développer des systèmes de paiements sécurisés sur les ordinateurs de poche PalmPilot.

PayPal a été créé en octobre 1999 par un ingénieur de l'entreprise. Il permettait d'effectuer des paiements faciles et sans frais entre adresses de courrier électronique, et se destinait à l'envoi de paiements simples entre particuliers (*pay pal* signifie littéralement « payer copain »). Son modèle économique se fondait sur la perception des intérêts liés à la conservation des fonds des clients en banque, afin de payer les coûts de fonctionnement et de rémunérer les actionnaires. C'était donc un service bâti en surcouche du système bancaire, comme Liberty Reserve.

Alors que la bulle Internet battait son plein, le produit a connu une progression fulgurante dès les premiers mois, notamment grâce à son système de parrainage. Ce succès a attiré l'attention des concurrents, disposant de bien plus de capital, qui ont copié l'idée et lancé leur propre version du service, au détriment de Confinity. C'est pour cette raison que l'entreprise a dû fusionner avec l'un d'entre eux, la banque en ligne X.com d'Elon Musk, pour devenir PayPal Inc. en mars 2000.

La vision originelle de PayPal était révolutionnaire, conformément à la vision libertarienne de Peter Thiel. Voici quel était le discours de ce dernier à l'automne 1999, rapporté par Eric Jackson en 2012 dans *The PayPal Wars* :

> « Ce que nous qualifions de "pratique" pour les utilisateurs américains sera révolutionnaire pour les pays en développement. Les États de nombre de ces pays jouent avec leur monnaie. Ils ont recours à l'inflation et parfois à des dévaluations monétaires massives, comme nous l'avons vu en Russie et dans plusieurs pays d'Asie du Sud-Est l'année dernière, pour priver leurs citoyens de leurs richesses. La plupart des gens ordinaires n'ont jamais l'occasion d'ouvrir un compte à l'étranger ou de mettre la main sur plus de quelques billets d'une monnaie stable comme le dollar américain. Un jour, PayPal sera en mesure de changer cette situation. À l'avenir, lorsque notre service sera disponible en dehors des États-Unis et que la pénétration d'Internet continuera à s'étendre à tous les niveaux économiques, PayPal permettra aux citoyens du monde entier d'exercer un contrôle plus direct sur leurs monnaies qu'ils ne l'ont jamais fait auparavant. Il sera pratiquement impossible pour les États corrompus de voler les richesses de leurs citoyens par leurs anciens moyens, car, dans le cas où ils essaient, les citoyens se tourneront vers le dollar, la livre ou le yen, abandonnant ainsi leur monnaie locale sans valeur pour quelque chose de plus sûr. »
>
> Original: "Of course, what we're calling 'convenient' for American users will be revolutionary for the developing world. Many of these countries' governments play fast and loose with their currencies. They use inflation and sometimes wholesale currency devaluations, like we saw in Russia and several Southeast Asian countries last year, to take wealth away from their citizens. Most of the ordinary people there never have an opportunity to open an offshore account or to get their hands on more than a few bills of a stable currency like U.S. dollars. Eventually PayPal will be able to change this. In the future, when we make our service available outside the U.S. and as Internet penetration continues to expand to all economic tiers of people, PayPal will give citizens worldwide more direct control over their currencies than they ever had before. It will be nearly impossible for corrupt governments to steal wealth from their people through their old means because if they try the people will switch to dollars or Pounds or Yen, in effect dumping the worthless local currency for something more secure."

Toutefois, les choses n'ont pas évolué dans le sens souhaité et PayPal a dû se conformer aux réglementations financières en tous genres, à tel point que le service est devenu aujourd'hui célèbre pour la censure des paiements et les gels de compte tout autour du monde. Il était vain de croire qu'un tel système pouvait défier le pouvoir en place.

### Les alternatives centralisées et Bitcoin

Ainsi, les tentatives de créer des services centralisés alternatifs au système existant ont toutes finies par être arrêtées, d'une façon ou d'une autre. L'inconvénient de ces modèles est qu'ils reposent sur un tiers de confiance, qui peut faire faillite, partir avec la caisse ou bien être contrôlé par les autorités. Dans le dernier cas, le service en question est face à un dilemme : s'adapter en se conformant aux réglementations financières, comme l'ont fait GoldMoney et PayPal, ou périr en refusant d'obéir, un destin subi par e-gold et Liberty Reserve ou encore le Liberty Dollar.

La fermeture de ces derniers systèmes a été contemporaine de la création et des débuts de Bitcoin. Par conséquent, Satoshi Nakamoto et les premiers utilisateurs de Bitcoin les connaissaient bien. Pour ce qui est de Satoshi, il [avait connaissance](https://www.metzdowd.com/pipermail/cryptography/2009-January/015041.html) du modèle utilisé par e-gold et a [évoqué](https://bitcointalk.org/index.php?topic=87.msg807#msg807) à plusieurs reprises Pecunix et Liberty Reserve dans ses interventions publiques et privées.

C'est à cause de cette fragilité des systèmes centralisés que les partisans de la liberté -- dont notamment les cypherpunks -- ont cherché à créer une monnaie décentralisée. Il fallait trouver un moyen d'éviter de faire reposer l'intégralité de l'infrastructure du système sur un point unique. C'est pourquoi plusieurs modèles « minimisant la confiance » ont émergé à la fin des années 1990 et au début des années 2000, avant la découverte de Bitcoin. Le prochain chapitre sera consacré à eux.

## Les modèles décentralisés qui ont précédé Bitcoin

Bitcoin constitue un modèle décentralisé de monnaie numérique. En cela, il évite le recours à un tiers de confiance, qui constituerait un point de défaillance unique du système. Comme l'ont montré les exemples de eCash, des devises en or numérique et de Liberty Reserve, la centralisation d'un système qui se veut être alternatif au système en place mène inévitablement à sa fermeture, d'une façon ou d'une autre.

Bitcoin n'est cependant pas le premier concept de monnaie décentralisée à avoir été proposé. Dès la fin des années 1990, de tels modèles ont été décrits par les cypherpunks, qui étaient obsédés par la liberté et la confidentialité des individus sur Internet, et qui jugeaient (à l'instar de David Chaum) qui les systèmes surveillés menaient à un avenir dystopique. Ils [appelaient](https://cypherpunks.venona.com/date/1993/03/msg00392.html) à « écrire du code » et considéraient que la « monnaie électronique » constituait un élément essentiel de leur idéal.

Dans ce chapitre, nous étudierons l'émergence des divers éléments techniques fondateurs qui ont plus tard été utilisés dans Bitcoin : le consensus distribué, l'horodatage et la preuve de travail. Ensuite, nous parlerons de b-money, de bit gold et de RPOW, respectivement conçus par les cypherpunks Wei Dai, Nick Szabo et Hal Finney. Enfin, nous évoquerons le cas de Ripple, dont le modèle est légèrement différent, mais qui a sa place dans l'histoire de la création de Bitcoin.

### Le consensus distribué

Avec l'émergence des ordinateurs dans les années 1950, est apparue la possibilité de les connecter entre eux et c'est ainsi que les premiers réseaux informatiques se sont
formés, menant au développement d'Internet, le « réseau des réseaux », dans les années 70. S'est inévitablement posée la question de l'infrastructure de ces réseaux. Dans son article fondateur de 1964 (décrivant la commutation de paquets), l'informaticien polono-américain Paul Baran recensait ainsi trois types de réseaux~: le réseau centralisé, reposant sur un nœud unique ; le réseau distribué, où chaque point est un nœud ; le réseau décentralisé (non distribué), reposant sur un réseau distribué de nœuds multiples.

![Les réseaux centralisé, décentralisé et distirbué selon Paul Baran](assets/img/ch3/1.webp)

On peut dégager deux modèles purs de ces considérations : le modèle client-serveur, où un serveur central répond aux requêtes des clients, et le modèle pair à pair, où chaque nœud a le même rôle dans le système. Ce dernier modèle a particulièrement été utile pour le partage de fichiers dans les années 2000, avec la création de BitTorrent et d'autres protocoles similaires. Le réseau Tor est lui décentralisé, pas purement pair à pair.

Un problème qu'on rencontre dans le cas des architectures distribuées est le problème du consensus distribué, qu'on appelle généralement le problème des généraux byzantins, qui a été formalisé par Leslie Lamport, Robert Shostak et Marshall Pease dans un [article](https://lamport.azurewebsites.net/pubs/byz.pdf) publié en 1982. Ce problème traite de la remise en cause de la fiabilité des transmissions et de l'intégrité des participants dans les systèmes pair à pair, et il s'applique dans les cas où les composants d'un système informatique ont besoin d'être en accord.

Le problème est énoncé sous la forme d'une métaphore faisant intervenir des généraux de l'armée de l'Empire byzantin, qui assiègent une ville ennemie avec leurs troupes dans le but de l'attaquer et qui ne peuvent communiquer qu'à l'aide de messagers. L'objectif est de trouver une stratégie (c'est-à-dire un algorithme) permettant de gérer la présence de traîtres et de s'assurer que tous les généraux loyaux se mettent d'accord sur un plan de bataille pour que l'attaque soit un succès. En voici une illustration (source : *L'Élégance de Bitcoin*) :

![Le problème des généraux byzantins](assets/img/ch3/2.webp)

La résolution de ce problème est importante pour les systèmes distribués qui gèreraient une unité de compte. De tels systèmes demandent en effet que les participants se mettent d'accord sur la propriété des unités de compte, à savoir sur qui possède quoi.

Avant Bitcoin, le problème était résolu de manière absolue par des algorithmes dits « classiques » qui nécessitaient que les nœuds soient connus à l'avance et que deux d'entre eux soient honnêtes. Le plus connu d'entre eux est probablement l'algorithme de consensus [PBFT](https://css.csail.mit.edu/6.824/2014/papers/castro-practicalbft.pdf) (sigle de *Practical Byzantine Fault Tolerance*), qui a été mis au point par Miguel Castro et Barbara Liskov en 1999 et qui permettait à un nombre donné de participants de se mettre d'accord en gérant des milliers de requêtes par seconde avec une latence de moins d'une milliseconde.

Avec l'algorithme de consensus de Bitcoin, Satoshi Nakamoto l'a résolue de manière probabiliste, permettant de supprimer certaines contraintes en sacrifiant la finalité stricte des transactions. Le 13 novembre 2008, il [écrivait](https://www.metzdowd.com/pipermail/cryptography/2008-November/014849.html) ainsi que « la chaîne de preuves de travail [était\] une solution au problème des généraux byzantins ». (original: "The proof-of-work chain is a solution to the Byzantine Generals' Problem.")

### L'horodatage de documents

L'horodatage (*timestamping* en anglais) est une technique qui consiste à associer une date et une heure à une information comme un évènement ou un document. D'un point de vue légal, cela permet par exemple de s'assurer de l'existence d'un contrat avant une date donnée. Dans le monde réel, il existe ainsi une multitude de moyens d'horodater quelque chose, comme l'envoi d'un document dans une enveloppe scellée ou l'inscription d'une ligne chronologique dans un carnet de notes.

Mais l'horodatage est particulièrement utile dans le monde numérique, où les fichiers (texte, image, audio ou vidéo) sont facilement modifiables. L'horodatage peut être réalisé par des services centralisés, qui se chargent de sauvegarder des documents reçus (ou bien leurs empreintes) et d'y associer la date et l'heure de réception. On parle dans ce cas d'horodatage certifié (*trusted timestamping*).

En 1991, une technique d'horodatage confidentielle et sécurisée a été proposée par Stuart Haber et Scott Scornetta, deux chercheurs travaillant pour Bell Communications Research Inc. (communément appelé « Bellcore »), un consortium de R&D situé dans le New Jersey. Dans leur article intitulé « [*How to time-stamp a digital document*](http://www.staroceans.org/e-book/Haber_Stornetta.pdf) », ils décrivaient comment un service d'horodatage certifié pouvait utiliser une fonction à sens unique (comme la fonction de hachage MD4) et un algorithme de signature pour accroître la confidentialité des documents des clients et la fiabilité de la certification. En particulier, l'idée était de chaîner les informations en appliquant la fonction à sens unique à l'horodatage précédent.

![Exemple d'horodatage certifié](assets/img/ch3/3.webp)

Exemple d'horodatage certifié (source : [Wikimedia](https://en.m.wikipedia.org/wiki/File:Trusted_timestamping.svg))

Haber et Scornetta ont mis leur idée en application par la publication d'empreintes cryptographiques (résultant d'un hachage des données utiles) dans les petites annonces du New York Times à partir de 1992. Ils ont ensuite créé leur propre société en 1994, Surety Technologies, dans le but de se consacrer pleinement à cette activité. Ils sont ainsi [connus](https://www.vice.com/en/article/j5nzx4/what-was-the-first-blockchain) pour avoir créé la première chaîne temporelle d'horodatages, l'empreinte précédente étant prise en compte dans le calcul de la nouvelle empreinte à publier dans le journal, ce qui préfigurait la chaîne de blocs de Bitcoin.

Trois articles de Haber et Scornetta ont été cités par Satoshi Nakamoto dans [livre blanc de Bitcoin](https://bitcoin.org/bitcoin.pdf) : l'article de 1991 précédemment mentionné, un [article](https://www.math.columbia.edu/~bayer/papers/Timestamp_BHS93.pdf) de 1993 qui améliorait les protocoles proposés dans le précédent, notamment par l'utilisation des arbres de Merkle, et un [article](https://cdn.nakamotoinstitute.org/docs/secure-names-bit-strings.pdf) de 1997 qui présentait une façon de nommer les fichiers de manière universelle au moyen de fonctions à sens unique. Était aussi cité un [article](https://cdn.nakamotoinstitute.org/docs/secure-timestamping-service.pdf) décrivant un nouveau système d'horodatage écrit en 1999 par Henri Massias, Xavier Serret-Avila et Jean-Jacques Quisquater, trois hommes travaillant pour le groupe de recherche en cryptographie de l'Université catholique de Louvain, en Belgique.

### La preuve de travail et Hashcash

La preuve de travail (*proof of work* en anglais) est un procédé permettant à un appareil informatique de démontrer de manière objective et quantifiable qu'il a dépensé de l'énergie, afin d'être sélectionné pour accéder à un service ou à un privilège. Il s'agit essentiellement d'un mécanisme de résistance aux attaques Sybil, qui rend difficile pour un attaquant de multiplier des identités à l'excès pour perturber ou prendre le contrôle d'un système de réputation quelconque.

Le concept de preuve de travail a été décrit pour la première fois en 1992 par les informaticiens Cynthia Dwork et Moni Naor, qui travaillaient alors au centre de recherche IBM d'Almaden, situé au sud de San José en Californie. Au sein d'un article de recherche intitulé [*Pricing via Processing or Combatting Junk Mail*](https://www.wisdom.weizmann.ac.il/~naor/PAPERS/pvp.pdf), ils ont présenté une méthode pour combattre le courrier indésirable (*spam*) dans les boîtes e-mail. Le modèle consistait à forcer les utilisateurs à résoudre un puzzle cryptographique pour chaque courriel envoyé, afin de limiter la capacité à envoyer des courriels en masse tout en permettant aux expéditeurs ponctuels de ne pas être gênés. Toutefois, ils n'ont jamais été jusqu'à mettre en œuvre leur idée.

Avec la popularisation d'Internet dans les années 90, la problème du courrier électronique indésirable est devenu de plus en plus prégnant, y compris sur la liste de diffusion des cypherpunks. C'est pourquoi le concept de Dwork et Naor a été [implémenté](https://cypherpunks.venona.com/date/1997/03/msg00774.html) par le jeune cypherpunk britannique Adam Back en 1997 avec Hashcash, un algorithme produisant de manière simple des preuves de travail au moyen d'une fonction de hachage. Plus précisément, il s'agit de trouver une collision partielle de la fonction de hachage considérée, c'est-à-dire à obtenir deux messages ayant une empreinte commençant par les mêmes bits de données (note : à partir de la version 1.0 sortie en 2002, il s'agit de découvrir une collision partielle pour l'empreinte zéro, à savoir trouver un antécédent dont l'empreinte commence par un nombre de zéros binaires déterminés). Puisque la fonction de hachage est à sens unique, une telle obtention ne peut être réalisée qu'en testant une à une les différentes possibilités, ce qui demande une dépense énergétique.

![Adam Back en 2001](assets/img/ch3/4.webp)

Adam Back en 2001 (source : [archive de cypherspace.org/adam](https://web.archive.org/web/20040404011747/http://www.cypherspace.org/adam/))

Mais les cypherpunks ne se limitaient pas à considérer la preuve de travail comme un simple moyen de limiter le spam ; ils souhaitaient également l'utiliser comme une manière de garantir le coût de production d'une monnaie numérique. Ainsi, en 1997, Adam Back lui-même [envisageait](https://cypherpunks.venona.com/date/1997/04/msg00822.html) pleinement cette idée, mais il avait conscience que les preuves de travail ainsi obtenues ne pouvaient pas être transférées d'une manière pleinement distribuée (à cause du problème de la double dépense) et qu'il fallait par conséquent passer par un système centralisé à la eCash. De même, en 1996, les cryptographes Ronald Rivest et Adi Shamir ont décrit [MicroMint](https://people.csail.mit.edu/rivest/pubs/RS96a.pdf), un système de micropaiement centralisé dont les pièces devaient être impossibles à contrefaire grâce à la production de preuves de travail.

Il fallait trouver un bon agencement qui puisse permettre à un tel modèle de fonctionner de manière robuste et durable. C'est ce que les cypherpunks Wei Dai, Nick Szabo et Hal Finney ont essayé de faire avec leurs protocoles respectifs (b-money, bit gold et RPOW), que nous allons étudier dans la suite. Et c'est ce que Satoshi Nakamoto a fini par faire en incluant Hashcash dans sa conception de Bitcoin.

### b-money : le stablecoin décentralisé

Le premier protocole à être issu du mouvement des cypherpunks était b-money, un modèle monnaie numérique décentralisée conceptualisé par Wei Dai en 1998. Ce dernier était un jeune cryptographe sino-américain vivant à Seattle et travaillant pour Microsoft, qui s'était impliqué sur la liste de diffusion à partir de 1994. Il s'est notamment illustré par la création de la bibliothèque libre Crypto++, qui serait plus tard utilisée dans le logiciel de Bitcoin.

Wei Dai a publié le texte descriptif de b-money le 26 novembre 1998 sur sa page personnelle et en a partagé le lien à la liste de diffusion des cypherpunks le même jour. Dans son [courriel](https://cypherpunks.venona.com/date/1998/11/msg00941.html), il décrivait b-money comme « un nouveau protocole d'échange monétaire et d'exécution des contrats pour les pseudonymes ».

Dans son idée, le système se fondait sur un réseau pair à pair intraçable. Chaque participant était identifié par un « pseudonyme numérique », c'est-à-dire une clé publique, et chaque message de transaction était signé par l'expéditeur et chiffré pour le destinataire. Chaque participant maintenait une base de données qui recensait les montant d'unités de b-money détenus par chaque pseudonyme.

La création monétaire était ouverte à tous les participants et se faisait par preuve de travail en diffusant la solution d'un problème informatique connu et précédemment non résolu. Le nombre d'unités créées dépendait du coût de cet effort exprimé par rapport à un panier standard de marchandises (incluant par exemple des métaux précieux), de sorte à maintenir le cours de l'unité autour d'un point d'équilibre « stable ». Le système offrait également la possibilité de créer et d'exécuter des contrats directement sur le réseau, grâce à un procédé rudimentaire de dépôt fiduciaire.

Même s'il était assez ingénieux, le concept de b-money présenté par Wei Dai n'était pas tout à fait fonctionnel. Il présentait ainsi des défauts majeurs comme la vulnérabilité aux attaques Sybil sur le réseau (n'importe qui pouvait théoriquement ajouter de nouveaux nœuds sur le réseau), la centralisation du réseau dans le cas où on présélectionnerait les serveurs, et celle liée à la stabilisation de l'unité de compte (qui donne les prix observables sur le marché ?)

Après sa publication sur la liste, b-money a attiré l'attention des cypherpunks, et en particulier [celle d'Adam Back](https://cypherpunks.venona.com/date/1998/12/msg00203.html). Néanmoins, Wei Dai n'a jamais implémenté son modèle, non seulement parce ce dernier était dysfonctionnel, mais aussi à cause de la [désillusion](https://www.lesswrong.com/posts/YdfpDyRpNyypivgdu/aalwa-ask-any-lesswronger-anything#XKwphuwm366RegQ3d) du cryptographe à l'égard de la cryptoanarchie. Toutefois, b-money a fini par être cité dans le livre blanc de Bitcoin, ce qui en fait l'un de ses précurseurs.

![Citation de b-money dans le livre blanc de Bitcoin](assets/img/ch3/5.webp)

### bit gold : l'or numérique avant Bitcoin

Le deuxième modèle à avoir émergé des idées des cypherpunks était l'idée de bit gold imaginée par Nick Szabo en 1998. Celui-ci était un informaticien américain d'origine hongroise, qui avait notamment travaillé pour comme consultant pour DigiCash pendant six mois. Cypherpunk, il est connu pour avoir formalisé la notion de *smart contract* en 1995.

En 1994, Nick Szabo avait créé une liste de diffusion privée appelée libtech-l, qui avait pour but, comme son nom l'indique, d'héberger des discussions sur les techniques libératoires, permettant de protéger les libertés individuelles face aux assauts des autorités. Y avaient accès des cypherpunks comme les Wei Dai et Hal Finney, ainsi les économistes Larry White et George Selgin, partisans de la concurrence des monnaies hayekienne et de la banque libre.

![Nick Szabo en 1997](assets/img/ch3/6.webp)

Nick Szabo en 1997 (source : [Adrien Chen](https://twitter.com/AdrianChen/status/456922865992863744/photo/1))

C'est sur la liste libtech-l que Nick Szabo a initialement décrit son concept initialement sur libtech-l, avant d'héberger une [ébauche](https://web.archive.org/web/20140406003811/http://szabo.best.vwh.net/bitgold.html) de livre blanc en 1999 sur son site personnel. Il a ensuite présenté le concept en 2005, dans un [article](https://unenumerated.blogspot.com/2005/12/bit-gold.html) publié sur son blog, Unenumerated.

bit gold était un protocole censé gérer la création et les échanges d'une ressource virtuelle appelée le bit gold. Contrairement à l'e-gold qui était garanti par de l'or physique, ou la b-money indexée en théorie sur un panier de marchandises, le bit gold ne devait être adossé à aucun autre bien, mais posséder une rareté infalsifiable intrinsèque, et
constituer ainsi un or intégralement numérique.

L'élément central du protocole était que la création monétaire se faisait par preuve de travail : les morceaux de bit gold étaient créés grâce à la puissance de calcul des ordinateurs et chaque solution était calculée à partir d'une autre, ce qui conduisait à former une chaîne de preuves de travail. La date et l'heure de production de ces preuves de travail étaient certifiées au moyen de serveurs d'horodatage multiples. Le système reposait sur un registre public de titres de propriété, référençant les possessions et les échanges des utilisateurs, ces derniers étant identifiés par leurs clés publiques et autorisant les transactions grâce à leurs clés privées. Le registre était vérifié et maintenu par un réseau de serveurs appelé « club de propriété » coordonné par un algorithme de consensus classique appelé [*Byzantine Quorum System*](https://dahliamalkhi.wordpress.com/wp-content/uploads/2015/12/byzquorums-distcomputing1998.pdf).

Le ressemblance de bit gold avec Bitcoin est frappante. Les trois éléments constitutifs du systèmes (la production des preuves de travail, leur horodatage et la gestion du registre de propriété), qui étaient séparés dans bit gold, peuvent se retrouver dans Bitcoin en un seul et même concept : la chaîne de blocs. C'est pourquoi beaucoup y ont vu une ébauche de Bitcoin et spéculé sur le fait que Nick Szabo pourrait être Satoshi.

Toutefois, leurs deux visions divergeaient. La façon dont étaient produits les morceaux de bit gold faisait que ceux-ci n'étaient pas fongibles, c'est-à-dire qu'ils ne pouvaient pas être mélangés entre eux : ils devaient donc être évalués sur un marché extérieur au système pour pouvoir être utilisés pour servir de base à une réelle unité de compte homogène. bit gold était ainsi pensé comme un système de règlement permettant de gérer une monnaie de réserve rare, et au-dessus duquel serait construit une économie bancaire libre, si possible utilisant le modèle chaumien. Ainsi, en avril 2008, Nick Szabo [demandait](https://web.archive.org/web/20171227190431/http://unenumerated.blogspot.com/2008/04/bit-gold-markets.html?showComment=1207799580000#c3741843833998921269) encore de l'aide dans un commentaire sur son blog pour mettre en œuvre son concept. Cependant, cette mise en œuvre n'a jamais eu lieu.

### RPOW : les preuves de travail réutilisables

Le troisième système a être issu de l'esprit des cypherpunks est le système RPOW, abréviation de *Reusable Proofs of Work*, mis au point par Hal Finney en 2004. Hal Finney était un informaticien et cryptographe américain qui vivait dans la région de Los Angeles. Cypherpunk de la première heure, il s'était passionné pour les idées de David Chaum et pour son fameux modèle eCash. Il travaillait depuis 1996 sur le développement du logiciel de chiffrement PGP avec Phil Zimmermann.

Pour concevoir son système RPOW, Hal Finney a repris les idées derrière eCash et bit gold. La particularité de son système est qu'il se basait sur un serveur transparent qui permettait de rendre transférables les preuves de travail produites par Hashcash. Ce serveur utilisait le cryptoprocesseur IBM 4758 Secure Cryptographic Coprocessor, un élément de haute sécurité résistant aux falsifications, qui permettait, par un procédé d'authentification conçu par IBM, de vérifier quels programmes étaient exécutés sur la machine. Un utilisateur externe pouvait de cette façon s'assurer à tout instant que le serveur RPOW faisait fonctionner le bon programme, dont le code était par ailleurs disponible publiquement.

Les jetons de preuve de travail réutilisable étaient gérés par le serveur, qui se chargeait de les signer à l'aide du chiffrement RSA. Ils étaient fabriqués par la production d'une preuve de travail via Hashcash, ou bien à partir d'un jeton de RPOW précédent. Lors d'un paiement, l'expéditeur donnait ses jetons de RPOW au destinataire qui s'empressait de communiquer avec le serveur pour recevoir un ou plusieurs nouveaux jetons, dont la valeur globale était égale à la valeur en entrée. Le fonctionnement des RPOW était ainsi
similaire à celui des billets numériques dans eCash.

En voici une illustration [conçue](https://nakamotoinstitute.org/finney/rpow/slides/slide004.html) par Hal Finney lui-même :

![Échange dans RPOW](assets/img/ch3/7.webp)

Hal Finney a non seulement conçu un modèle, mais l'a mis en œuvre personnellement. Le 15 août 2004, il a ainsi [annoncé](https://lists.cpunks.org/pipermail/cypherpunks-legacy/2004-August/134945.html) le lancement du système RPOW sur le liste des cypherpunks, en plus de documenter son fonctionnement sur le site web consacré (rpow.net). Il l'a ensuite [présenté](https://web.archive.org/web/20050204193327/http://rpow.net/slides/slide001.html) à la CodeCon 2005 organisée à San Francisco, où il a pu faire part des utilisations qu'il envisageaient pour les jetons de preuve de travail, à savoir : le transfert de la valeur, la régulation du courrier indésirable, le commerce dans les jeux vidéos, le jeu d'argent en ligne comme le poker, et l'anti-parasitisme sur les protocoles de partage de fichiers comme BitTorrent.

Toutefois, RPOW présentait des défauts intrinsèques qui peuvent expliquer pourquoi il n'a pas rencontré le succès escompté :

- Son modèle de sécurité était plutôt faible, car il reposait sur un serveur centralisé ;
- Sa politique monétaire (basée sur le hachage) n'était pas spécialement attractive en raison de la hausse exponentielle des performances informatiques.

Ainsi, l'utilisation réelle de RPOW a été anecdotique, mais ce dernier a eu le mérite d'« [ouvrir la voie](https://mmalmi.github.io/satoshi/#email-24) » à Bitcoin en constituant une preuve de concept expérimentale, quatre ans avant l'arrivée de Satoshi Nakamoto.

### Ripple : la décentralisation du crédit

Un autre modèle prédécesseur de Bitcoin, moins connu, mais qui a pour autant sa place ici, est le protocole de crédit distribué Ripple, qui a été conçu par le développeur canadien Ryan Fugger en 2004. Ce dernier avait été inspiré par le concept du [système d'échange local](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27%C3%A9change_local) (SEL), quelque chose qu'il avait expérimenté à Vancouver avant de concevoir son protocole. Il a publié le [livre blanc](https://web.archive.org/web/20060221162102/http://ripple.sourceforge.net/decentralizedcurrency.pdf) de Ripple le 14 avril 2004 et l'a ensuite mis en œuvre par le biais d'une preuve de concept appelée RipplePay, qui fonctionnait sur un serveur central et qui permettait aux utilisateurs de se connecter avec une simple adresse de courrier électronique.

Le concept de Ripple se fondait sur l'idée que la monnaie était essentiellement constituée de reconnaissances de dette (IOUs), c'est-à-dire de crédit. Il s'agissait d'établir un réseau pair à pair dont les liens seraient des relations de crédit entre les personnes. Les paiements se faisaient alors par le routage d'une série d'emprunts, tous les participants étant des banquiers se prêtant de l'argent mutuellement. Alice pouvait payer 10 $ à David, en prêtant 10 $ à Bob, et en demandant à Bob de faire de même auprès de Carole, puis à Carole de faire de même auprès de David : le compte de David était ensuite crédité de 10 $ issus de la création monétaire d'Alice. Le système fonctionnait ainsi par ondulations, ce qui explique le nom du projet.

Voici une vidéo de présentation de Ripple réalisée en 2011 :

![Vidéo (Youtube) de présentation de Ripple en 2011](https://youtu.be/f9KqSgRZYgg)

Malgré l'enthousiasme de sa communauté et quelques milliers d'utilisateurs, Ripple possédait des défauts majeurs qui l'ont empêché de connaître le succès. En particulier, il souffrait du « [problème de l'engagement décentralisé](https://fiatjaf.com/3cb7c325.html) » : durant un paiement, les participants ne pouvaient pas s'engager d'une façon sûre pour assurer la chaîne de prêts, un problème qui serait résolu plus tard par Lightning.

Voyant que son projet n'allait nulle part,  Ryan Fugger a laissé les rênes de Ripple aux dirigeants de l'entreprise OpenCoin Inc., Chris Larsen et Jed McCaleb, en novembre 2012. La société a été renommée en Ripple Labs en 2013. Ces derniers en ont fait un protocole sensiblement différent du concept initial, reposant sur un algorithme de consensus et sur une unité de compte native, le XRP. Ryan Fugger a fini par modifier le nom de sa preuve de concept en [Rumplepay](https://rumplepay.com/) en 2020 pour éviter la confusion.

Ripple était pour ainsi dire contemporain de Bitcoin, et il s'avère que beaucoup de gens intéressés par ce dernier s'étaient aussi intéressés au premier. En effet, Ripple constituait un modèle novateur, fondée sur une architecture distribuée, une caractéristique partagée avec Bitcoin. À ce sujet, Satoshi Nakamoto [écrirait](https://diyhpl.us/~bryan/irc/bitcoin-satoshi/p2presearch-again/p2pfoundation.net/backups/p2p_research-archives/2009-February.txt.gz) que « Ripple est unique en ce qu'il répartit la confiance plutôt que de la concentrer ».

### Bitcoin, l'aboutissement d'une quête

Ainsi, à la fin des années 2000, tous les éléments constitutifs de Bitcoin étaient connus et plusieurs tentatives de les combiner avait été réalisées. Toutefois, les assemblages proposés n'avaient pas été probants. Les cypherpunks en particuliers se sont désintéressés de cette question, jugeant que la conception d'une monnaie numérique réellement décentralisée était impossible. Satoshi Nakamoto leur a donné tort.

Bitcoin constitue en effet un assemblage ingénieux de tous ces concepts. Il repose sur la signature numérique, issue de la cryptographie asymétrique proposée par Diffie et Hellmann en 1976. Il est un « argent liquide électronique » comme s'y destinait le modèle eCash de David Chaum mis en application dans les années 90. Par son algorithme de consensus novateur, il résout de manière robuste le problème des généraux byzantins, énoncé par Lamport, Shostak et Pease en 1982. Avec le gestion de sa chaîne de blocs sur un réseau pair à pair, il est une forme de « serveur d'horodatage distribué », reprenant le concept de Haber et Scornetta de 1991. Pour la sélection des blocs de transactions et pour la production des unités, il fait usage de la preuve de travail, utilisant un procédé proche de Hashcash, proposé par Adam Back en 1997. Enfin, il rappelle par sa conception les projets de b-money, bit gold, RPOW et Ripple, auxquels Satoshi Nakamoto a rendu hommage, d'une façon ou d'une autre.

Bitcoin forme donc l'aboutissement d'une quête pour la cybermonnaie, une monnaie existant intégralement sur Internet et n'étant pas à la merci des États. Dans les prochains chapitres, nous raconterons comment il a pris vie et quels ont été les évènements marquants de ses premières années d'existence.

# L'action de Satoshi Nakamoto (2008 -- 2011)

## La naissance de Bitcoin (août 2008 -- janv. 2009)

Après avoir appris d'où venait Bitcoin, nous allons à présent nous concentrer sur son histoire proprement dite. <!--TODO-->

La naissance de Bitcoin est marquée par un évènement majeur : la publication du livre blanc, le document fondateur qui explique le fonctionnement technique de Bitcoin, le 31 octobre 2008. Le réseau a été lancé en janvier 2009, un peu plus de deux mois plus tard. L'activité de Satoshi Nakamoto ne s'est cependant pas limitée à ça : il a tout fait pour que Bitcoin soit lancé dans les meilleures conditions.

### La découverte (printemps 2007 -- août 2008)

Si on en croit son [propre](https://www.metzdowd.com/pipermail/cryptography/2008-November/014863.html) [témoignage](https://bitcointalk.org/index.php?topic=13.msg46#msg46), Satoshi Nakamoto se met à travailler sur Bitcoin durant le printemps 2007. Après avoir [effectué](https://web.archive.org/web/20140511100607/https://bitcoinfoundation.org/forum/index.php?/topic/54-my-first-message-to-satoshi/#entry514) diverses recherches sur le sujet des monnaies numériques, il finit par trouver un moyen de résoudre le problème de la double dépense sans tiers de confiance. Pendant plus d'un an, il garde secret son modèle, souhaitant le peaufiner pour s'assurer de sa solidité. Tel qu'il [l'écrira](https://bitcointalk.org/index.php?topic=195.msg1617#msg1617) plus tard :

> « À un moment donné, j'ai été convaincu qu'il y avait un moyen de mettre en place ce système sans requérir aucune confiance et je n'ai pas pu m'empêcher de continuer à y penser. &nbsp;Le travail a consisté bien plus à concevoir qu'à coder. »
>
> Original: "At some point I became convinced there was a way to do this without any trust required at all and couldn't resist to keep thinking about it. &nbsp;Much more of the work was designing than coding."

Pour s'assurer qu'il fonctionne correctement, Satoshi [programme](https://www.metzdowd.com/pipermail/cryptography/2008-November/014832.html) un prototype avant de rédiger le livre blanc. Cette manière de faire est à l'opposé de ce qui se fait d'ordinaire au sein de la communauté universitaire, où les concepts sont présentés formellement dans des articles scientifiques avant qu'ils soient mis en application. Il [affirmera](https://www.metzdowd.com/pipermail/cryptography/2008-November/014832.html) :

> « En fait, j'ai fait ça un peu à l'envers. &nbsp;J'ai dû écrire tout le code avant de pouvoir me convaincre que je pouvais résoudre tous les problèmes, et je n'ai écrit le papier qu'après. »
>
> Original: "I actually did this kind of backwards. &nbsp;I had to write all the code before I could convince myself that I could solve every problem, then I wrote the paper."

### La préparation (août 2008 -- oct. 2008)

C'est en août 2008 que Satoshi Nakamoto se décide à préparer la sortie de Bitcoin. Le 18, il réserve le nom de domaine Bitcoin.org via le service anonyme AnonymousSpeech (ainsi que [Netcoin.org](https://twitter.com/orweinberger/status/1573234325046558720), n'ayant probablement pas finalisé le choix du nom à donner à son concept). Le nom de domaine sera utilisé pour héberger le site principal de Bitcoin. Le nom de domaine Bitcoin.com est alors détenu par un [spéculateur](https://mmalmi.github.io/satoshi/#email-28), et il sera [utilisé](https://web.archive.org/web/20090719065532/http://www.bitcoin.com/) entre 2009 et 2011 par une société appelée BitCoin Ltd., spécialisée dans les micropaiements.

Le 20 août, il [entre en contact](https://s3.documentcloud.org/documents/24439625/adam-back-exhibit-ab1-1.pdf) avec Adam Back en lui envoyant un courriel pour lui demander un conseil sur la façon de citer son article sur Hashcash dans le livre blanc. Difficile de ne pas y voir un prétexte servant à faire en sorte que l'inventeur de Hashcash prenne connaissance de son nouveau système.

![Adam Back en 2012](assets/img/ch4/1.webp)

Adam Back en 2012 (source : [cypherspace.org/adam](http://www.cypherspace.org/adam/))

Le courriel contient un lien vers une ébauche du livre blanc. Le nom du fichier PDF est `ecash.pdf` et son titre est « *Electronic Cash Without a Trusted Third Party* ». Le résumé est le même que celui de la première version publiée en octobre, à un mot près. Malheureusement nous ne disposons pas du document intégral.

Le lendemain, ayant lu le résumé envoyé par Satoshi (mais pas le papier), Adam Back le redirige vers le proposition b-money de Wei Dai, qui semble posséder des similarités avec son concept. Satoshi répond en le remerciant pour son indication et en précisant que « [ses propres\] idées partent exactement du même point ». (*original: "my ideas start from exactly that point"*). Adam Back lui indique aussi l'existence de MicroMint, mais Satoshi ne répondra pas.

Le surlendemain, le 22 août, Satoshi envoie donc un courriel à Wei Dai pour lui dire qu'il « se prépare à publier un document qui étend [ses\] idées à un système complètement fonctionnel » et pour lui demander l'année de publication de sa page sur la b-money afin d'y faire référence dans le livre blanc. (*original: "I'm getting ready to release a paper that expands on your ideas into a complete working system."*) Comme dans le cas de son échange avec Adam Back, il partage à Wei Dai l'ébauche du livre blanc.

Malgré ces interactions, Adam Back et Wei Dai ne s'intéressent pas immédiatement au concept de Satoshi. Ce ne sera que des années plus tard qu'ils reviendront vers Bitcoin : Wei Dai en 2011 et Adam Back en 2013.

De son côté, Satoshi se prépare à rendre public son invention. Le 3 octobre, il termine la première version du livre blanc de Bitcoin, dont le nom est désormais choisi. Le 5 octobre, il s'inscrit sur la plateforme de gestion de projets SourceForge, là où le code source ouvert du logiciel sera hébergé et maintenu jusqu'en 2011, avant de migrer sur GitHub.

### La publication du livre blanc (oct. 2008 -- nov. 2008)

Le 31 octobre 2008, Satoshi Nakamoto publie la [première version du livre blanc](assets/pdf/bitcoin-20081003.pdf) sur une liste de diffusion de courrier électronique dédiée à la cryptographie, appelée simplement la « *Cryptography mailing list* ». Cette liste est gérée par le développeur Perry Metzger depuis 1996, date de sa [création](https://cypherpunks.venona.com/date/1996/12/msg00102.html) en 1996, en réaction au nombre de plus en plus important de courriels sur la liste des cypherpunks, et est hébergée sur son site personnel, Metdowd.com, depuis [2003](https://www.metzdowd.com/pipermail/cryptography/2003-April/004484.html). Elle est l'héritière de la liste des cypherpunks, à la différence qu'elle est soumise à une modération stricte. En 2008, plusieurs anciens cypherpunks y participent encore, comme John Gilmore, Hal Finney ou encore Len Sassaman.

Dans son premier [courriel](https://www.metzdowd.com/pipermail/cryptography/2008-October/014810.html) adressé à la liste, Satoshi écrit sobrement :

> « J'ai travaillé sur un nouveau système d'argent liquide électronique qui est entièrement pair à pair, dépourvu de tiers de confiance. »
>
> Original: "I've been working on a new electronic cash system that's fully peer-to-peer, with no trusted third party."

Il liste également les propriétés principales de son modèle :

- « Les doubles dépenses sont empêchées grâce à un réseau pair à pair. »
- « Pas de monnaierie ni d'autre tiers de confiance. »
- « Les participants peuvent être anonymes. »
- « Les nouvelles pièces sont fabriquées à partir d'une preuve de travail de style Hashcash. »
- « La preuve de travail utilisée pour la génération des nouvelles pièces permet également au réseau d'empêcher les doubles dépenses. »

(*original: "Double-spending is prevented with a peer-to-peer network. &nbsp;No mint or other trusted parties. &nbsp;Participants can be anonymous. &nbsp;New coins are made from Hashcash style proof-of-work. &nbsp;The proof-of-work for new coin generation also powers the network to prevent double-spending."*)

Dans son courriel, il inclue un lien vers le livre blanc, déjà hébergé sur Bitcoin.org, qui est un court document de 9 pages, présenté comme un article scientifique, décrivant le fonctionnement technique de Bitcoin. Ce document est centré sur le problème des paiements en ligne.

![Titre et résumé de la première version du livre blanc (octobre 2008)](assets/img/ch4/2.webp)

Suite à cette annonce, Satoshi reçoit quelques réponses, mais la plupart d'entre elles sont sceptiques. On lui reproche notamment trois choses :

- Tout d'abord, le cypherpunk James A. Donald [remet en cause](https://www.metzdowd.com/pipermail/cryptography/2008-November/014814.html) le passage à l'échelle du système en disant qu'« il ne semble pas pouvoir s'adapter à la taille requise ». Satoshi lui [répond](https://www.metzdowd.com/pipermail/cryptography/2008-November/014815.html) que « la bande passante n'est peut-être pas aussi prohibitive » qu'il le pense.
- Le deuxième commentaire négatif provient de John R. Levine, auteur du livre *Internet pour les Nuls* et consultant spécialisé dans l'infrastructure du courrier électronique, le filtrage des spams et les brevets logiciels. Ce dernier [critique](https://www.metzdowd.com/pipermail/cryptography/2008-November/014817.html) la sécurité de Bitcoin en évoquant la puissance de calcul détenue par les « fermes de machines zombies » composées d'ordinateurs contrôlés par des pirates. Il explique en particulier que, sur Internet, « les gentils ont une puissance de calcul nettement inférieure à celle des méchants ». Satoshi [répond](https://www.metzdowd.com/pipermail/cryptography/2008-November/014818.html) brillamment : « L'exigence est que les gentils disposent collectivement d'une puissance de calcul supérieure à celle de n'importe quel attaquant. »
- Enfin, un individu du nom de Ray Dillinger (utilisant le pseudonyme bear) s'interroge sur la valeur de l'unité de compte, déplorant le fait que « les preuves de travail informatiques n'ont pas de valeur intrinsèque » et reprochant leur caractère inflationniste en raison de l'évolution technique du matériel informatique. Satoshi lui [répond](https://www.metzdowd.com/pipermail/cryptography/2008-November/014831.html) que « l'augmentation de la vitesse du matériel est prise en charge » par l'ajustement périodique de la difficulté de production.

Même si le scepticisme est l'attitude majoritaire sur la liste, il n'est pas partagé par l'intégralité des personnes inscrites sur la liste de diffusion. En particulier, une personne se démarque des autres par son enthousiasme : il s'agit de Hal Finney, qui a une vision optimiste de l'avenir et qui n'a jamais abandonné l'idée de l'argent liquide électronique, malgré les échecs des années 90. Il [déclarera](https://bitcointalk.org/index.php?topic=155054.msg1643833#msg1643833) à ce sujet quelques années plus tard que « les cryptographes grisonnants \[...\] ont tendance à devenir cyniques » mais que lui « était plus idéaliste » ayant « toujours aimé la cryptographie, son mystère et son paradoxe ».  Ainsi, le 7 novembre, il écrit dans un [courriel](https://www.metzdowd.com/pipermail/cryptography/2008-November/014827.html) adressé à la liste que « Bitcoin semble être une idée très prometteuse » et compare le modèle de Satoshi au bit gold de Nick Szabo.

![Hal Finney en 2007](assets/img/ch4/3.webp)

Hal Finney en 2007

### La politique monétaire et le code du logiciel (nov. 2008 -- déc. 2008)

Bitcoin utilise un algorithme de consensus distribué permettant à tous les nœuds du réseau de se mettre d'accord sur le contenu d'un registre, que Hal Finney désigne dès son premier courriel par le terme « *block chain* », en deux mots. La chaîne de blocs correcte choisie est celle qui possède le plus de blocs et les conflits sur les blocs concurrents sont réglés selon ce principe simple. Le mécanisme sera affiné [plus tard](https://sourceforge.net/p/bitcoin/code/109/) pour prendre en compte la quantité de travail accumulée plutôt que la longueur en nombre de blocs.

Ce mécanisme de consensus permet d'imposer toutes sortes de règles et incitations (pour reprendre la dernière phrase du livre blanc) au sein du système. Puisque Bitcoin constitue un service d'horodatage distribué, il est aussi possible de faire interagir ces règles avec le temps qui passe. D'où l'algorithme d'ajustement de la difficulté qui intervient pour réguler la production des nouveaux blocs et des bitcoins qui y sont associés : si le nombre de blocs produits sur une période donnée est trop élevée, alors la difficulté de production augmente ; dans le cas inverse, elle diminue. Bitcoin se différencie ainsi de RPOW, où les preuves de travail elles-mêmes forment les unités de compte.

Grâce à cet ajustement de la difficulté, Bitcoin peut donc avoir une politique monétaire, c'est-à-dire que le montant de nouvelles unités émises par le protocole peut être déterminé à l'avance. Au départ, il est prévu que l'émission monétaire soit constante, afin d'inciter les nœuds producteurs à apporter leur puissance de calcul au réseau, et il n'y a pas de frais de transaction. Tel que l'écrit Satoshi Nakamoto dans la section « Incitation » du livre blanc :

> « L'ajout régulier d'une quantité constante de nouvelles pièces est analogue aux mineurs d'or qui dépensent des ressources pour ajouter de l'or dans la circulation. »

> original: "The steady addition of a constant of amount of new coins is analogous to gold miners expending resources to add gold to circulation."

Cette propriété, [confirmée](https://www.metzdowd.com/pipermail/cryptography/2008-November/014831.html) par Satoshi sur la liste de diffusion, n'échappe pas à James A. Donald. Le 9 novembre, ce dernier [reproche](https://www.metzdowd.com/pipermail/cryptography/2008-November/014837.html) ainsi au « travail de suivi de qui possède quoi » (c'est-à-dire au minage) d'être « payé par le seigneuriage » et de « nécessiter de l'inflation », même s'il fait remarquer qu'« une inflation prévisible est moins choquante qu'une inflation qui est traficotée de temps à autre pour transférer des richesses d'un groupe électoral à un autre ». (*original: "in the proposed system the work of tracking who owns what coins is paid for by seigniorage, which requires inflation. This is not an intolerable flaw - predictable inflation is less objectionable than inflation that gets jiggered around from time to time to transfer wealth from one voting block to another."*) En outre, il [remarque](https://www.metzdowd.com/pipermail/cryptography/2008-November/014841.html) aussi qu'un nœud producteur qui « ignore toutes les dépenses dont il ne se préoccupe pas » ne subit « aucune conséquence négative ». (*original: "If one node is ignoring all spends that it does not care about, it suffers no adverse consequences."*)

Ces remarques font probablement prendre conscience à Satoshi qu'il peut mettre en place un [mécanisme de frais de transaction](https://www.metzdowd.com/pipermail/cryptography/2008-November/014842.html) qui résout les deux problèmes, en pouvant remplacer la création de nouvelles unités et en incitant les mineurs [à](https://www.metzdowd.com/pipermail/cryptography/2008-November/014843.html) « inclure toutes les transactions payantes qu'ils reçoivent ». (*original: "nodes would have an incentive to include all the paying transactions they receive."*)

<!-- L'absence de réduction de l'émission monétaire et de mécanisme de frais sera confirmée quelques mois plus tard par Satoshi lorsqu'il [écrira](https://mmalmi.github.io/satoshi/#email-3) à Martti Malmi que « cette discussion sur l'inflation a eu lieu avant la mise en place du mécanisme des frais de transaction et du plan fixe des 21 millions de pièces ». -->

Dans le même temps, les questions de ses interlocuteurs le poussent à partager le code source de son modèle. Le 16 novembre, Satoshi transmet le code à Hal Finney, James A. Donald et Ray Dillinger. Le 17, dans un réponse à James A. Donald sur la liste, il [écrit](https://www.metzdowd.com/pipermail/cryptography/2008-November/014863.html) qu'il lui a envoyé « les fichiers principaux », que ceux-ci sont « disponibles sur demande pour le moment » et que leur « publication complète » aura lieu « bientôt ». (*original: "I sent you the main files. &nbsp;(available by request at the moment, full release soon)"*) Dans cette portion du code, qui sera [rendu publique](https://bitcointalk.org/index.php?action=printpage;topic=382374.0) en 2013 par Ray Dillinger lui-même, on peut constater que tous les éléments fondateurs de Bitcoin sont présents : la chaîne de blocs (alors encore appelée « *timechain* »), la preuve de travail, le modèle de représentation par des pièces (UTXO), la programmabilité des transactions, les frais de transaction et la réduction de moitié (*halving*).

Des paramètres diffèrent cependant, ce qui indique qu'ils ont été choisis de façon spontanée ou, comme l'[écrira](https://plan99.net/~mike/satoshi-emails/thread1.html) Satoshi, que ce choix constituait une « estimation éclairée ». (*original: "educated guess"*) Le temps de bloc, c'est-à-dire la période visée entre chaque bloc, est de 15 minutes au lieu de 10. La période d'ajustement de la difficulté est de 2 880 blocs (soit 30 jours pour un temps de blocs de 15 minutes) au lieu de 2 016 blocs (ce qui correspond à 14 jours pour un temps de bloc de 10 minutes). La mécanique de réduction de moitié, présente dans la fonction `GetBlockValue`, fait que le halving doit avoir lieu 100 000 blocs, soit tous les 2 ans et 311 jours environ :

```cpp
int64 GetBlockValue(int64 nFees)
{
    int64 nSubsidy = 10000 * CENT;
    for (int i = 100000; i <= nBestHeight; i += 100000)
        nSubsidy /= 2;
    return nSubsidy + nFees;
}
```

Il se crée 100 bitcoins durant la première période de 100 000 blocs, 50 durant la deuxième période, etc. de sorte que la quantité totale de bitcoins converge vers 20 millions. Chaque bitcoin (COIN) est divisible en 100 centimes (CENT), qui sont eux-mêmes divisibles en 10 000 unités de base, si bien qu'un bitcoin peut être divisé en 1 million d'unités plus petites, et non en 100 millions comme dans la version 0.1.

Hal Finney et Ray Dillinger [réalisent](https://www.linkedin.com/pulse/id-known-what-we-were-starting-ray-dillinger/) alors un examen minutieux du code. Chacun se concentre sur une partie spécifique du système : Ray Dillinger s'intéresse à la partie concernant le consensus, et Hal Finney étudie le système de script.

Le 10 décembre, Satoshi [crée](https://web.archive.org/web/20131016004654/http://sourceforge.net/p/bitcoin/mailman/bitcoin-list/?viewmonth=200812) la liste de diffusion bitcoin-list, qui est hébergée sur SourceForge. Cette liste aura peu de succès, même si quelques courriels de personnes intéressées y seront envoyés au fur et à mesure des années. Mais cela démontre que tout est place pour le lancement du prototype, évènement qui adviendra un mois plus tard, au début de l'année 2009.

### La sortie du logiciel et le lancement du réseau (janv. 2009)

Le 8 janvier 2009 à 19 heures 27, Satoshi Nakamoto publie la première version du logiciel (numérotée 0.1.0) sur la liste de diffusion de Metzdowd.com. Le code source en C++ est publié de manière ouverte sous licence libre (MIT), de sorte que n'importe qui peut le copier, le modifier et l'utiliser à sa guise. Il contient notamment les données du bloc de genèse, le premier bloc de la chaîne à partir duquel cette dernière doit se prolonger. Le logiciel ne fonctionne que sous Windows. Dans son [courriel](https://www.metzdowd.com/pipermail/cryptography/2009-January/014994.html) d'annonce, Satoshi écrit :

> « Voici la première version de Bitcoin, un nouveau système de monnaie électronique qui utilise un réseau pair à pair pour empêcher la double dépense. &nbsp;C'est un système complètement décentralisé, sans serveur ni autorité centrale. »
>
> original: "Announcing the first release of Bitcoin, a new electronic cash system that uses a peer-to-peer network to prevent double-spending. &nbsp;It's completely decentralized with no server or central authority."

Il précise que « le logiciel est encore en version alpha et en phase expérimentale » et qu'« il n'y a aucune garantie que l'état du système ne doive pas être redémarré à un moment donné ». (*original: "The software is still alpha and experimental. &nbsp;There's no guarantee the system's state won't have to be restarted at some point if it becomes necessary"*) Il y a deux moyens d'obtenir des bitcoins : en demandant à quelqu'un de nous en envoyer ou bien en activant la production de pièces par CPU. Il y a également deux façons d'envoyer des unités : en utilisant l'adresse IP du destinataire, ou bien en passant par une adresse Bitcoin, ce qui permet d'envoyer un paiement hors-ligne. Enfin, le courriel décrit la politique monétaire finale de Bitcoin, dont nous parlerons dans le chapitre suivant.

Quelques heures plus tard, dans la nuit du 8 au 9 janvier, Satoshi se met à miner, ce qui marque le lancement effectif du réseau. Le deuxième bloc de la chaîne, le bloc 1, est validé par Satoshi le 9 à 2 heures 54 du matin.

Une fois cela fait, il se charge de prévenir les différentes personnes avec qui il a communiqué de ce lancement. À 5 heures 21, il envoie un [courriel](https://www.coindesk.com/markets/2020/11/26/previously-unpublished-emails-of-satoshi-nakamoto-present-a-new-puzzle/) à Hal Finney l'informant que « la version Bitcoin v0.1 avec l'exécutable et le code source complet est disponible sur Sourceforge ». Le lendemain, il contacte Adam Back et Wei Dai en leur écrivant un courriel personnalisé. Dans ces derniers e-mails, il inclue en particulier une description publiée par Hal Finney sur la liste de diffusion, qui mentionne la preuve de travail et b-money.

Le 10 janvier, Hal Finney essaie de lancer le fichier exécutable du logiciel, mais il rencontre un problème technique qui fait planter son ordinateur. Il [contacte](https://web.archive.org/web/20140821141611/http://sourceforge.net/p/bitcoin/mailman/message/21295694/) donc Satoshi et commence à échanger avec lui à ce sujet. Hal Finney arrive tant bien que mal à faire fonctionner le logiciel. Dans la nuit du 10 au 11, à 1 heure du matin, il trouve ainsi son premier bloc (le [bloc 78](https://mempool.space/block/00000000a2886c95400fd3b263b9920af80b118b28fee5d2a162a18e4d9d8b2f) et gagne de ce fait 50 bitcoins. Une heure plus tard, il envoie un [courriel élogieux](https://www.metzdowd.com/pipermail/cryptography/2009-January/015004.html) à la *Cryptography mailing list* où il félicite Satoshi pour la sortie du la version alpha et où il met en valeur la politique monétaire de l'unité de compte. Enfin, à 3 heures 33, il [fait part](https://twitter.com/halfin/status/1110302988) son expérience sur Twitter (média social alors naissant) en indiquant qu'il fait fonctionner Bitcoin, en anglais : « *Running bitcoin* ». C'est le premier tweet qui parle de Bitcoin.

De ces échanges entre Satoshi et Hal Finney sortent la version 0.1.3 qui est [publiée](https://web.archive.org/web/20171124135217/https://sourceforge.net/p/bitcoin/mailman/message/21313152/) le 12 janvier, et qui est beaucoup plus stable. Satoshi profite également de converser avec Hal Finney pour lui donner quelques bitcoins : il lui [envoie](https://mempool.space/tx/f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16) ainsi 10 bitcoins par l'intermédiaire de son adresse IP dans la nuit du 11 au 12 janvier, à 3 heures 30 du matin. Il s'agit du premier transfert d'une personne à une autre sur le réseau.

Mais Hal Finney n'est pas la seule personne à essayer Bitcoin à ce moment-là. C'est aussi le cas de Dustin D. Trammell, un chercheur en sécurité informatique américain qui s'intéresse alors aux monnaies numériques (et en particulier à la version électronique du Liberty Dollar) qui découvre Bitcoin via la liste de diffusion. Le 11 janvier, il exécute le logiciel sur une de ses machines de travail (mais il ne mine son premier [bloc](https://mempool.space/block/00000000d3ec2f50772c2d42d4afb054c283555766a0ca1d8da65b9b5058a49e) que le 13 à cause d'un problème technique). Dans la nuit du 11 au 12, il rentre en contact avec Satoshi, avec lequel il [communique](https://www.dustintrammell.com/s/Satoshi_Nakamoto.zip) longuement au cours des jours suivants. Le 15 janvier, Dustin Trammell [reçoit](https://mempool.space/tx/d71fd2f64c0b34465b7518d240c00e83f6a5b10138a7079d1252858fe7e6b577) également 25 bitcoins de sa part.

![Dustin Trammell](assets/img/ch4/4.webp)

Dustin Trammell (source : archive de [blog.dustintrammell.com](https://web.archive.org/web/20100419181845/http://blog.dustintrammell.com/))

Par la suite, d'autres personnes essaient de faire fonctionner le logiciel. C'est le cas de Nicholas Bohm, un avocat britannique, qui envoie un courriel le 25 janvier sur bitcoin-list car il rencontre un problème technique et échange en privé avec Satoshi. Un certain Jeff Kane arrive de son côté à faire fonctionner la version 0.1.3 le 30 janvier. Nicholas Bohm sera mentionné aux côtés de Dustin Trammell dans les crédits de la version 0.1.5 du logiciel sorti début février.

À partir du 9 janvier 2009, le réseau ne s'arrêtera pas. Bloc après bloc, la chaîne continuera de s'allonger. Et Bitcoin finira par connaître le succès.

### Une conception progressive

Ce que nous pouvons retenir de ce récit de la conception de Bitcoin est que cette dernière a eu lieu de manière progressive. Entre la première idée au printemps 2007 et le lancement effectif du réseau lors de l'hiver 2009, il s'est en effet écoulé plus d'un an et demi. De plus, certains éléments du modèle ont évolué, comme nous l'avons vu avec la politique monétaire et le mécanisme des frais de transaction qui sont apparus après la publication de la première version du livre blanc le 31 octobre 2008.

**extrait** Cependant, ce travail n'a pas été suffisant, et il a fallu de la persévérance à Satoshi pour amorcer son système. Dès le début, il savait bien que peu de gens s'étaient penchés sérieusement sur son modèle et qu'il allait être compliqué d'attirer de nouveaux utilisateurs et contributeurs. C'est pourquoi il a essayé de susciter l'enthousiasme en vendant son idée du mieux possible. Nous étudierons cet aspect dans le chapitre suivant, qui couvre une grande partie de l'année 2009.

## Présenter Bitcoin au monde (janv. 2009 -- oct. 2009)

La communication de Satoshi. Présenter Bitcoin pour attirer de nouveaux utilisateurs.

### Le bloc de genèse (3--8 janv. 2009)

Le mois de janvier 2009 est l'occasion pour Satoshi Nakamoto d'établir deux choses importantes : le bloc de genèse (*genesis block*) et la limite des 21 millions d'unités. Ces deux éléments sont présents dans la version 0.1.0 du logiciel publiée le 8 janvier sur la liste de diffusion de Metzdowd.com.

Le bloc de genèse le bloc de base de la chaîne de blocs de Bitcoin, qui doit être prolongée à partir de lui, et est par conséquent inscrit en dur dans le logiciel. À l'occasion du lancement du réseau, Satoshi construit un nouveau bloc de genèse, qui est horodaté au 3 janvier 2009 à 18:15:05 UTC. Dans ce bloc (et plus précisément dans la transaction de récompense), il inscrit le message suivant :

```
The Times 03/Jan/2009 Chancellor on brink of second bailout for banks
```

Ce message est le titre de la une du quotidien britannique *The Times* de ce jour-là et il indique que le chancelier de l'Échiquier (c'est-à-dire le ministre des finances britannique) est sur le point de renflouer les banques pour la seconde fois. La présence de cette une dans le bloc possède un rôle double :

- D'une part, elle empêche l'antidatage du lancement du réseau en prouvant que le système n'a pas été démarré avant le 3 janvier, car Satoshi ne pouvait pas connaître cette une avant cette date ;
- D'autre part, elle indique symboliquement ce à quoi Bitcoin s'oppose en faisant référence au contexte monétaire et financier de l'époque.

**extrait** À l'époque, le monde subit en effet de plein fouet les effets de la crise financière amorcée en 2007 par le dégonflement de la bulle des subprimes aux États-Unis. Les États renflouent les banques pour éviter de nouvelles faillites bancaires après la chute de Lehman Brothers survenue le 15 septembre 2008, et les banques centrales procèdent à des assouplissements quantitatifs en injectant des liquidités sur les marchés financiers. Cette utilisation d'argent public créé pour l'occasion, a pour effet de choquer profondément un certain nombre de citoyens qui réalisent que le système bancaire est en fait un système de profits privés et de pertes socialisées.

![The Times : Chancellor on brink of second bailout for banks](assets/img/ch5/1.webp)

**extrait** De par son absence de tiers de confiance, Bitcoin n'est, lui, pas soumis à l'arbitraire d'une banque centrale. Il contraste ainsi avec les monnaies étatiques, telles que le dollar ou l'euro, dont la quantité peut être modifiée arbitrairement par ceux qui contrôlent la création monétaire. La politique monétaire du bitcoin est quant à elle programmée à l'avance, inscrite dans le protocole, pour en théorie ne jamais être altérée.

### La limite des 21 millions (8--16 janvier 2009)

Cela nous amène au second élément présenté par Satoshi le jour du lancement du réseau : la limite des 21 millions. Le 8 janvier, dans son [courriel d'introduction](https://www.metzdowd.com/pipermail/cryptography/2009-January/014994.html), il décrit cette politique monétaire de la façon suivante : (*note : "coin" traduit par "unité", à modifier si besoin*)

> « La circulation totale sera de 21 000 000 d'unités. &nbsp;Elles seront distribuées aux nœuds du réseau lorsqu'ils créeront des blocs, la quantité émise étant divisée par deux tous les 4 ans.
>
> les 4 premières années : 10 500 000 unités<br>
> les 4 années suivantes : 5 250 000 unités<br>
> les 4 années suivantes : 2 625 000 unités<br>
> les 4 années suivantes : 1 312 500 unités<br>
> etc.
>
> Lorsque cela sera épuisé, le système pourra prendre en charge les frais de transaction si nécessaire. »
>
> original: "Total circulation will be 21,000,000 coins. &nbsp;It'll be distributed to network nodes when they make blocks, with the amount cut in half every 4 years.
>
> first 4 years: 10,500,000 coins<br>
> next 4 years: 5,250,000 coins<br>
> next 4 years: 2,625,000 coins<br>
> next 4 years: 1,312,500 coins<br>
> etc...
>
> When that runs out, the system can support transaction fees if needed. &nbsp;It's based on open market competition, and there will probably always be nodes willing to process transactions for free."

Quelques jours plus tard, Hal Finney [réagit](https://www.metzdowd.com/pipermail/cryptography/2009-January/015004.html) à cette politique monétaire sur la liste en s'enthousiasmant du fait que « le système peut être configuré pour n'autoriser qu'un nombre maximum certain de pièces à être générées ». Dans son courriel, il estime que si Bitcoin devient « le système de paiement dominant utilisé dans le monde entier » (*original: "the dominant payment system in use throughout the world"*), chaque unité aura alors « une valeur d'environ 10 millions » de dollars. (*original: "a value of about $10 million"*) Il conclue en écrivant que « la possibilité de produire des pièces aujourd'hui avec quelques centimes de temps de calcul » peut constituer « un très bon pari ». (*original: "the possibility of generating coins today with a few cents of compute time may be quite a good bet"*) Même si l'estimation est contestable (car elle se base sur une valorisation du bitcoin qui serait équivalente à la totalité de la richesse mondiale), le raisonnement se tient. C'est notamment cet élément qui pousse Dustin Trammell à lancer un nœud très rapidement, comme il le confie à Satoshi dans leur correspondance privée.

**extrait** Le 16 janvier, Satoshi reprend cet idée d'« investissement à long terme » dans un courriel qu'il partage à la liste de diffusion, où il décrit les cas d'utilisation potentiels et où il [déclare](https://www.metzdowd.com/pipermail/cryptography/2009-January/015014.html) qu'il « pourrait être judicieux d'en avoir au cas où cela prendrait » et que « si suffisamment de gens pensent la même chose, cela deviendra une prophétie autoréalisatrice ». (*original: "It might make sense just to get some in case it catches on. &nbsp;If enough people think the same way, that becomes a self fulfilling prophecy."*) Il [réitérera](https://p2pfoundation.ning.com/xn/detail/2003008:Comment:9562) cette affirmation un mois plus tard en expliquant que le montant limité d'unités est susceptible de créer une « boucle de rétroaction positive » dans le sens où « plus les utilisateurs sont nombreux, plus la valeur augmente, ce qui pourrait attirer davantage d'utilisateurs désireux de profiter de la valeur croissante ». De ce fait, l'élément spéculatif est présent dès la départ, dans le but d'amorcer le système.

### La réglementation, les réseaux de zombies et l'écologie (17--26 janvier 2009)

Dans la foulée, une autre discussion se développe sur la liste de diffusion. Satoshi a mentionné la limitation du spam comme un cas d'utilisation, ce qui fait réagir les différents contributeurs. Le créateur de Bitcoin préfère répondre en privé à ces reproches, mais Hal Finney se charge d'objecter en public. Ce dernier a en effet eu le temps de réfléchir à ses questions, lorsqu'il avait essayé de mettre au point une monnaie numérique avec RPOW.

D'abord, survient la question de la réglementation et de la potentielle interdiction de Bitcoin par les États. Cette question est [soulevée](https://www.metzdowd.com/pipermail/cryptography/2009-January/015016.html) par Jonathan Thornburg, chercheur pour le département d'astronomie de l'université de l'Indiana à Bloomington et habitué de la liste. Dans son courriel en réponse aux cas d'utilisation proposés par Satoshi, il dresse la situation de la surveillance financière mondiale et indique que Bitcoin pourrait permettre de transférer des montants supérieurs au seuil toléré par les autorités. La conséquence logique de son raisonnement est qu'« aucun État majeur n'est susceptible d'autoriser le fonctionnement à grande échelle de Bitcoin sous sa forme actuelle ».

Cette question intéresse Hal Finney qui écrit un écrit un [tweet](https://twitter.com/halfin/status/1136749815) le 21 janvier indiquant qu'il cherche « un moyen d'ajouter plus d'anonymat à Bitcoin ». Puis le 24, il [répond](https://www.metzdowd.com/pipermail/cryptography/2009-January/015036.html) à Jonathan Thornburg en écrivant qu'« il s'agit certainement d'un argument valable » mais que « Bitcoin dispose de plusieurs atouts », dont le principal est qu'il est « distribué, sans point de défaillance unique, sans "monnaierie", sans société dont les dirigeants peuvent être assignés à comparaître ». (*original: "Certainly a valid point, and one which has been widely discussed in the debates over the years about electronic cash. Bitcoin has a couple of things going for it: one is that it is distributed, with no single point of failure, no "mint", no company with officers that can be subpoenaed and arrested and shut down."*)

Ensuite, dans le même courriel, Jonathan Thornburg aborde le sujet des réseaux d'ordinateurs zombies, qui pourraient trivialement « passer à travers les filtres de courrier électronique payants », en référence au cas d'utilisation ayant été mis en avant par Satoshi. Ce dernier lui [répond](https://mmalmi.github.io/satoshi/#email-3) en privé, lui expliquant qu'il pourrait dans ce cas « réaliser un joli profit en créant des adresses électroniques payantes et en collectant tout l'argent du spam », une opinion qu'il [retranscrit](https://www.metzdowd.com/pipermail/cryptography/2009-January/015041.html) sur la liste le 25. Hal Finney de son côté rappelle que la preuve de travail « vise principalement à garantir la fiabilité de la base de données de l'historique des transactions », puis ajoute que si les jetons de preuve de travail utiles, alors les machines ne resteront plus inutilisées et le parasitage diminuera.

Enfin, le dernier commentaire émane de John Gilmore, ancien membre fondateur des cypherpunks et tenancier de la première liste de diffusion du mouvement entre 1992 et 1997. Dans un courriel envoyé le 25 janvier, il met en avant les supposées conséquences écologiques de Bitcoin et [écrit](https://www.metzdowd.com/pipermail/cryptography/2009-January/015042.html) que « la dernière chose dont nous avons besoin est de déployer un système conçu pour brûler tous les cycles disponibles, consommant de l'électricité et générant du dioxyde de carbone, partout sur Internet, afin de produire de petites quantités de bitbux pour faire passer des courriels ou des spams ». (*original: "The last thing we need is to deploy a system designed to burn all available cycles, consuming electricity and generating carbon dioxide, all over the Internet, in order to produce small amounts of bitbux to get emails or spams through."*) Satoshi lui [répond](https://mmalmi.github.io/satoshi/#email-3) en privé qu'« il serait ironique de devoir choisir entre la liberté économique et la préservation de l'environnement ». Il ajoute que « la preuve est la seule solution \[qu'il a\] trouvée pour faire fonctionner un système d'argent électronique pair à pair » et que, même si elle devait consommer beaucoup d'énergie, « elle gaspillerait toujours moins que l'activité bancaire conventionnelle nécessitant beaucoup de main-d'œuvre et de ressources ». (*original: "Ironic if we end up having to choose between economic liberty and conservation. &nbsp;Unfortunately, proof of work is the only solution I've found to make p2p e-cash work without a trusted third party. (...) If it did grow to consume significant energy, I think it would still be less wasteful than the labour and resource intensive conventional banking activity it would replace."*)

Le 27, Hal Finney [évoque](https://www.metzdowd.com/pipermail/cryptography/2009-January/015056.html) des pistes qui permettait de réduire la dissipation énergétique liée au calcul des preuves de travail. Une heure plus tard, il [écrit](https://twitter.com/halfin/status/1153096538) sur Twitter « réfléchir à la manière de réduire les émissions de CO2 liées à une mise en œuvre généralisée de Bitcoin ».

Un autre soutien provient du cypherpunk Zooko Wilcox-O'Hearn, qui travaille alors sur Tahoe-LAFS, un système de partage de fichiers héritier. Le 26 janvier, au sein de la discussion sur la liste, il glisse le lien vers un billet qu'il a publié le jour-même sur son blog intitulé « [*Decentralized Money*](https://web.archive.org/web/20090303195936/http://testgrid.allmydata.org:3567/uri/URI:DIR2-RO:j74uhg25nwdpjpacl6rkat2yhm:kav7ijeft5h7r7rxdp5bgtlt3viv32yabqajkrdykozia5544jqa/wiki.html#%5B%5BDecentralized%20Money%5D%5D) », où il cite les différents projets de monnaies numériques (DigiCash, bit gold, b-money) et où il fait la part belle à Bitcoin. Il écrit notamment :

> « Ce que je veux, c'est une monnaie que tout le monde puisse utiliser de manière pratique et peu coûteuse, mais que **personne** n'ait le pouvoir de manipuler cette monnaie. &nbsp;Que personne n'ait le pouvoir de gonfler ou de dégonfler la masse monétaire ; que personne n'ait le pouvoir de surveiller, de taxer ou d'empêcher les transactions. &nbsp;Un véritable équivalent numérique de l'or, dans les périodes et les lieux où l'or était la monnaie universelle. »
>
> original: "What I want is a currency which everyone can cheaply and conveniently use but which **no-one** has the power to manipulate.  No-one has the power to inflate or deflate the currency supply, no-one has the power to monitor, tax, or prevent transactions.  Truly the digital equivalent of gold, during the times and places when gold was the universal currency."

Le lien vers ce texte finira par être [ajouté](https://web.archive.org/web/20090303195936/http://bitcoin.org/) sur le site Bitcoin.org, et Satoshi [remerciera](https://bitcointalk.org/index.php?topic=890.msg10723#msg10723) personnellement Zooko un an et demi plus tard.

### Le pair-à-pair et la défiance des banques (févr. 2009)

La *Cryptography mailing list* n'est pas le seul endroit où Satoshi Nakamoto intervient pour promouvoir son modèle. En février 2009, il interagit avec la Fondation P2P, une organisation créée en 2007 qui étudie l'impact des infrastructures pair à pair sur la société, par le biais de son forum (p2pfoundation.ning.com) et de sa liste de diffusion (p2p-research). Le 11 février, il publie un [message d'introduction](https://p2pfoundation.ning.com/forum/topics/bitcoin-open-source) présentant Bitcoin sur le forum, dont il envoie une [copie](https://diyhpl.us/~bryan/irc/bitcoin-satoshi/p2presearch-again/p2pfoundation.net/backups/p2p_research-archives/2009-February/001347.html) par courriel sur la liste. Dans ce texte, il écrit :

> « Le problème fondamental de la monnaie conventionnelle est toute la confiance nécessaire pour la faire fonctionner. &nbsp;Il faut faire confiance à la banque centrale pour qu'elle ne déprécie pas la monnaie, mais l'histoire des monnaies fiat est pleine de violations de cette confiance. &nbsp;Il faut faire confiance aux banques pour détenir notre argent et le transférer par voie électronique, mais elles le prêtent par vagues de bulles de crédit avec à peine une fraction en réserve. &nbsp;Nous devons leur faire confiance pour protéger notre vie privée, pour ne pas laisser les voleurs d'identité vider nos comptes. &nbsp;Leurs frais généraux considérables rendent les micropaiements impossibles. »
>
> original: "The root problem with conventional currency is all the trust that's required to make it work. The central bank must be trusted not to debase the currency, but the history of fiat currencies is full of breaches of that trust. Banks must be trusted to hold our money and transfer it electronically, but they lend it out in waves of credit bubbles with barely a fraction in reserve. We have to trust them with our privacy, trust them not to let identity thieves drain our accounts. Their massive overhead costs make micropayments impossible."

Sur son profil, il indique être un homme japonais, mais ce n'est pas tout. Une mise à jour de l'interface fera apparaître son âge en 2011 : 35 ans en 2011. Puis, on [découvrira](https://www.reddit.com/r/Bitcoin/comments/229qvr/happy_birthday_satoshi_nakamoto/) en 2014 qu'il a indiqué une date de naissance particulière : le 5 avril 1975. Cette date, d'apparence bénigne, est vraisemblablement une date composite faisant référence à l'interdiction pour les citoyens américains de détenir de l'or entre 1933 et 1975 aux États-Unis. Le jour du 5 avril se rapporte au jour de l'instauration de cette interdiction par l'[Ordre exécutif 6102](https://www.presidency.ucsb.edu/documents/executive-order-6102-forbidding-the-hoarding-gold-coin-gold-bullion-and-gold-certificates) signé par le président Franklin Delano Roosevelt le 5 avril 1933, et l'année 1975 correspond à son année d'abrogation lors de l'entrée en vigueur de la [Public Law 93-373](https://www.govtrack.us/congress/bills/93/s2665/text). Ce détail est très important puisque cette prohibition a mis fin à l'étalon-or classique (où chacun pouvait obtenir de l'or en échange d'un billet représentatif), a permis de dévaluer le dollar (par le biais du *Gold Reserve Act* en 1934) et a facilité l'instauration du régime monétaire à taux de change flottants que nous connaissons suite au *Nixon Shock* de 1971.

![Profil de Satoshi Nakamoto sur le forum de la Fondation P2P, capture du 17 mars 2011](assets/img/ch5/satoshi-p2p-foundation-profile-2011.webp)

[Profil de Satoshi Nakamoto sur le forum de la Fondation P2P, capture du 17 mars 2011](https://web.archive.org/web/20110317060514/http://p2pfoundation.ning.com:80/profile/SatoshiNakamoto)

Ce n'est pas la seule référence aux métaux précieux qui se retrouve dans les interventions de Satoshi. Le créateur de Bitcoin [écrit](https://p2pfoundation.ning.com/forum/topics/bitcoin-open-source?commentId=2003008:Comment:9562) ainsi dans les commentaires le 18 février :

> « Il n'y a personne pour agir en tant que banque centrale ou réserve fédérale afin d'ajuster la masse monétaire au fur et à mesure que le nombre d'utilisateurs augmente. &nbsp;Il aurait fallu qu'un tiers de confiance détermine la valeur, car je ne connais aucun moyen pour un logiciel de connaître la valeur des choses dans le monde réel. &nbsp;S'il existait un moyen astucieux, ou si nous voulions faire confiance à quelqu'un pour gérer activement la masse monétaire afin de l'ancrer à quelque chose, les règles auraient pu être programmées à cet effet. &nbsp;En ce sens, c'est un système qui se comporte davantage comme un métal précieux. »
>
> original: "To Sepp's question, indeed there is nobody to act as central bank or federal reserve to adjust the money supply as the population of users grows. That would have required a trusted party to determine the value, because I don't know a way for software to know the real world value of things. If there was some clever way, or if we wanted to trust someone to actively manage the money supply to peg it to something, the rules could have been programmed for that. In this sense, it's more typical of a precious metal."

Satoshi Nakamoto est aussi actif sur la liste de diffusion où il échange notamment avec Martien van Steenbergen, un consultant en gestion de projet néerlandais. Le 13 février, il aborde le sujet de la programmabilité de Bitcoin et [écrit](https://diyhpl.us/~bryan/irc/bitcoin-satoshi/p2presearch-again/p2pfoundation.net/backups/p2p_research-archives/2009-February/001362.html) à ce dernier :

> « Je considère Bitcoin comme une pierre angulaire, comme une première étape si l'on veut mettre en œuvre des monnaies sociales de pair à pair programmables telles que décrites par les idées de Marc \[Fawzi\] et d'autres discutées ici. &nbsp;Il faut d'abord qu'une monnaie pair à pair basique et normale fonctionne. &nbsp;Une fois qu'elle est établie et éprouvée, il est facile de passer à l'étape suivante, celle de la monnaie automatique dynamique.
>
> J'aime beaucoup l'idée de communautés virtuelles, sans appartenance géographique, qui expérimentent de nouveaux paradigmes économiques. »
>
> *original: "I see Bitcoin as a foundation and first step if you want to implement programmable P2P social currencies like Marc's ideas and others discussed here. &nbsp;First you need normal, basic P2P currency working. &nbsp;Once that is established and proven out, dynamic smart money is an easy next step.*
>
> *I love the idea of virtual, non-geographic communities experimenting with new economic paradigms."*

Satoshi cherche à s'adapter à son public et à pousser les gens à s'intéresser à sa découverte.

### Mike Hearn

La stratégie de communication de Satoshi prote peu à peu ses fruits. Au mois d'avril 2009, d'autres personnes commencent à s'intéresser à son invention. Le 12, Mike Hearn, un développeur britannique travaillant pour Google et s'adonnant au logiciel libre sur son temps libre, lui envoie un [courriel](https://plan99.net/~mike/satoshi-emails/thread1.html) posant une série de questions à propos de Bitcoin, en précisant qu'« il est rare de rencontrer des idées vraiment révolutionnaires ». Hearn s'intéresse alors aux systèmes de paiement numériques, et notamment à Ripple, qu'il ne manque pas de mentionner.

![Mike Hearn](assets/img/ch5/mike-hearn.webp)

En particulier, Mike Hearn demande à Satoshi pourquoi il a choisi la quantité de « 24 millions » (*sic*) pour le montant total de bitcoins et si ces derniers peuvent être fractionnés. Satoshi donne alors l'explication suivante :

> « Mon choix pour le nombre d'unités et le programme de distribution était une estimation éclairée. &nbsp;C'était un choix difficile, car une fois le réseau en marche, ces paramètres étaient verrouillés et nous étions bloqués avec eux. &nbsp;Je voulais choisir quelque chose qui rendrait les prix similaires à ceux des monnaies existantes, mais c'était très difficile sans avoir connaissance de l'avenir. &nbsp;J'ai fini par choisir un entre-deux. &nbsp;Si Bitcoin reste une petite niche, il vaudra moins par unité que les monnaies existantes. &nbsp;Si l'on imagine qu'il est utilisé pour une partie du commerce mondial, alors il n'y aura que 21 millions d'unités pour le monde entier, donc elles vaudront beaucoup plus par unité. &nbsp;Les valeurs sont des entiers codées sur 64 bits avec 8 décimales, donc une pièce est représentée en interne par 100 000 000. &nbsp;Il y a beaucoup de granularité si jamais les prix usuels deviennent petits. &nbsp;Par exemple, si 0,001 [Bitcoin\] vaut 1 euro, il peut être plus facile de changer l'emplacement de la virgule, de sorte que si on a 1 Bitcoin, il sera désormais affiché comme 1000, et 0,001 sera affiché comme 1. »
>
> *original: "My choice for the number of coins and distribution schedule was an educated guess. &nbsp;It was a difficult choice, because once the network is going it's locked in and we're stuck with it. &nbsp;I wanted to pick something that would make prices similar to existing currencies, but without knowing the future, that's very hard. &nbsp;I ended up picking something in the middle. &nbsp;If Bitcoin remains a small niche, it'll be worth less per unit than existing currencies. &nbsp;If you imagine it being used for some fraction of world commerce, then there's only going to be 21 million coins for the whole world, so it would be worth much more per unit. &nbsp;Values are 64-bit integers with 8 decimal places, so 1 coin is represented internally as 100000000. &nbsp;There's plenty of granularity if typical prices become small. &nbsp;For example, if 0.001 is worth 1 Euro, then it might be easier to change where the decimal point is displayed, so if you had 1 Bitcoin it's now displayed as 1000, and 0.001 is displayed as 1."*

Après leurs discussions, ils effectuent quelques échanges monétaires. Le 18 avril, Mike Hearn envoie ainsi 32,51 bitcoins à Satoshi, que ce dernier lui renvoie dans la journée. Il s'envoient également mutuellement 50 bitcoins issus de leur production personnelle. <!--TODO-->

### Martti Malmi et la présentation de Bitcoin (avr. 2009 -- juin 2009)

La communication de Satoshi ne laisse pas non plus indifférent un jeune étudiant en informatique finlandais du nom de Martti Malmi. Ce dernier découvre Bitcoin début avril, par l'intermédiaire du texte sur le forum de la Fondation P2P. Le 9, il se met à utiliser le logiciel et mine son premier bloc (le bloc 10 351). Dans la soirée, il rédige une courte présentation de Bitcoin où il soutient l'hypothèse anarchiste que « la monnaie pair à pair pourrait faire disparaître l'État ». (*original: "P2P Currency could make the government extinct?"*). Il publie son texte sous le pseudonyme Trickster(n) sur deux forums libertariens de sensibilités différentes : anti-state.com (ASC) et le forum de Freedomain Radio (le média de l'anarcho-capitaliste Stefan Molyneux). Il écrit :

> « Le système est anonyme, et aucun État ne pourrait possiblement taxer ou empêcher les transactions. Il n'y a pas de banque centrale qui puisse déprécier la devise avec la création illimitée de nouvelle monnaie. L'adoption généralisée d'un tel système ressemblerait à quelque chose qui pourrait avoir un effet dévastateur sur la capacité de l'État à se nourrir à partir de son bétail. »

> *original: "The system is anonymous, and no government could possibly tax or prevent the transactions. There's no central bank to debase the currency with unlimited creation of new money. A widespread adoption of such a system sounds like something that could have a devastating effect on the state's ability to feed on its livestock."*

![Martti Malmi en 2013](assets/img/ch5/martti-malmi-2013.webp)

Martti Malmi en 2013 (source : [Business Insider](https://www.businessinsider.com/bitcoins-martti-malmi-not-worried-about-liberty-reserve-2013-5)

Il envoie ensuite un [courriel](https://mmalmi.github.io/satoshi/#email-1) un Satoshi précisant qu'il est l'auteur de ce texte, où il écrit qu'il « aimerait aider avec Bitcoin » même s'il n'a « pas encore beaucoup d'expérience en matière de développement ». (*original: "I'm Trickstern from the anti-state.com forum, and I would like to help with Bitcoin, if there's something I can do. I have a good touch on Java and C languages from school courses (I'm studying CS), but not so very much development experience yet."*) Satoshi Nakamoto lui répond le 2 mai, en lui disant que sa « compréhension de Bitcoin » est « en plein dans le mille ». (*original: "Thanks for starting that topic on ASC, your understanding of bitcoin is spot on."*)

Satoshi le met à contribution pour remplir la page web sur SourceForge ([bitcoin.sourceforge.net](https://web.archive.org/web/20090511173000/http://bitcoin.sourceforge.net/)), la plateforme où est hébergé le code du logiciel, notamment en écrivant une [foire aux questions](https://mmalmi.github.io/satoshi/#email-4) (FAQ). Sur la page de garde, il présente Bitcoin comme une « monnaie numérique anonyme basée sur un réseau pair à pair » ne reposant sur « aucune autorité centrale pour émettre du nouvel argent ou pour surveiller les transactions ». Il met en avant les avantages suivants :

- « Transférez de l'argent facilement via Internet, sans avoir à faire confiance à des tiers. » (*original: "Transfer money easily through the internet, without having to trust third parties."*)
- « Aucun tiers ne peut empêcher ou contrôler vos transactions. » (*original: "Third parties can't prevent or control your transactions."*)
- « Soyez à l'abri de l'instabilité causée par l'activité bancaire à réserves fractionnaires bancaire et par les mauvaises politiques des banques centrales. L'inflation limitée de la masse monétaire du système Bitcoin est répartie uniformément (par puissance de calcul) sur tout le réseau, et pas monopolisée par les banques. » (*original: "Be safe from the unstability caused by fractional reserve banking and the bad policies of the central banks. The limited inflation of the Bitcoin system's money supply is distributed evenly (by CPU power) throughout the network, not monopolized to the banks."*)
- « La valeur du Bitcoin est susceptible d'augmenter à mesure que la croissance de l'économie de Bitcoin dépasse le taux d'inflation – considérez le Bitcoin comme un investissement et commencez à faire tourner un nœud aujourd'hui ! » (*original: "Bitcoin's value is likely to increase as the growth of the Bitcoin economy exceeds the inflation rate - consider Bitcoin an investment and start running a node today!"*)

Satoshi [approuve](https://mmalmi.github.io/satoshi/#email-5) globalement cette présentation même s'il émet quelques réserves. Il [est](https://mmalmi.github.io/satoshi/#email-19) en particulier « mal à l'aise » avec le fait de déclarer que le bitcoin est un « investissement », redoutant probablement les répercussions légales à ce sujet. Cette description modifiée de Martti Malmi [se retrouvera](https://web.archive.org/web/20100106082749/http://www.bitcoin.org/) sur le site web principal à la fin de l'année 2009.

Le printemps 2009 est également marqué par l'apparition du mot « cryptomonnaie » (« *cryptocurrency* » en anglais) qui est intialement utilisé pour se référer à Bitcoin. Le 11, Satoshi [écrit](https://mmalmi.github.io/satoshi/#email-19) ainsi à Martti Malmi :

> « Quelqu'un a proposé le mot "cryptomonnaie"... c'est peut-être un mot que nous devrions utiliser pour décrire Bitcoin, ça te plaît ? »

Le jeune Finlandais approuve et avance que « *The P2P Cryptocurrency* » (« La cryptomonnaie pair à pair ») pourrait être le slogan de Bitcoin. Cette suggestion sera mise à exécution : le titre de la page de présentation deviendra « *Bitcoin P2P Cryptocurrency* » et l'annonce de la version 0.3 en juillet 2010 décrira le projet comme « *Bitcoin, the P2P cryptocurrency* ».

### Les deux forums de Bitcoin (juin 2009 -- nov. 2009)

Martti Malmi met aussi en place un forum et un wiki, toujours sur la page SourceForge. Ces éléments sont [ouverts](https://mmalmi.github.io/satoshi/#email-17) le 9 juin. Le 13, Malmi [annonce](https://web.archive.org/web/20131016004650/http://sourceforge.net/p/bitcoin/mailman/bitcoin-list/?viewmonth=200906) l'existence de la page SourceForge, du forum et du wiki sur la liste de diffusion de Bitcoin :

> « Le nouveau site/portail de Bitcoin est disponible à l'adresse bitcoin.sourceforge.net. Des forums et un wiki sont intégrés, vous êtes donc invités à participer aux discussions et à la documentation sur le wiki. »
>
> original: "The new Bitcoin website/portal is up at bitcoin.sourceforge.net. Forums and a wiki are included, so you're welcome to join discussion and wiki documentation."

Nous n'en avons pas de trace de ce premier forum, mis à part les quelques messages transférés par Satoshi sur son successeur.

Le deuxième forum est ouvert en novembre 2009 à l'adresse bitcoin.org/smf.

### Le développement initial du logiciel (janv. 2009 -- déc. 2009)

Un dernier élément important de l'année 2009 est l'évolution du logiciel.

Martti Malmi, Linux, v0.2



## L'amorçage (oct. 2009 -- mai 2010)

### Les premiers mineurs de bitcoins (2009)

Dustin Trammell, James Howells, Martti Malmi, NewLibertyStandard

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
