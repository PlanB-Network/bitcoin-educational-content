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

## Les alternatives centralisées et Bitcoin

Ainsi, les tentatives de créer des services centralisés alternatifs au système existant ont toutes finies par être arrêtées, d'une façon ou d'une autre. L'inconvénient de ces modèles est qu'ils reposent sur un tiers de confiance, qui peut faire faillite, partir avec la caisse ou bien être contrôlé par les autorités. Dans le dernier cas, le service en question est face à un dilemme : s'adapter en se conformant aux réglementations financières, comme l'ont fait GoldMoney et PayPal, ou périr en refusant d'obéir, un destin subi par e-gold et Liberty Reserve.

La fermeture de ces systèmes est contemporaine de la création et des débuts de Bitcoin.

Dustin Trammell, eLD

Satoshi, e-gold, Pecunix, Liberty Reserve

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
