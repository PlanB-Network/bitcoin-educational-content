---
name: Réseaux IP de la théorie à la pratique
goal: Maîtriser les fondamentaux des réseaux IP pour mieux les configurer et les dépanner.
objectives:
  - Comprendre l’architecture et le fonctionnement du protocole TCP/IP
  - Expliquer les différences, avantages et contraintes d’IPv4 et d’IPv6
  - Identifier et distinguer les différents types d’adresses IP
  - Configurer et vérifier l’adressage IP sur des systèmes Unix/Linux
  - Utiliser les principaux outils de diagnostic pour analyser et résoudre des problèmes réseau
---

# L’essentiel pour naviguer au sein de l'IP

Plongez au cœur de l’univers IP et donnez-vous les moyens de comprendre et d’administrer efficacement vos réseaux. Dans ce cours, vous découvrirez de manière claire et concrète tout ce qu’il faut savoir sur les réseaux informatiques.

Vous allez comprendre le fonctionnement des réseaux et de l’adressage IP. Vous apprendrez également à distinguer IPv4 et IPv6, à identifier et utiliser les différentes catégories d’adresses, et à saisir toute l’importance du protocole TCP/IP et des liens qu’il tisse entre adresses IP, adresses physiques et noms DNS.

NET 302 s’adresse avant tout aux étudiants, utilisateurs de Linux ou simplement aux curieux souhaitant comprendre les notions de base en réseau et renforcer leur autonomie dans la gestion, le dépannage et l’optimisation des infrastructures.

Rejoignez-nous et transformez vos connaissances en véritable expertise opérationnelle !

___
Ce cours NET 302 est une adaptation du cours *Les bases du réseau : TCP/IP, IPv4 et IPv6*, rédigé par Philippe Pierre en français et publié sur [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), sous licence Creative Commons Attribution - ShareAlike 4.0 International ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)).

Des modifications substantielles ont été apportées à la version originale par Loïc Morel : le texte original a été intégralement réécrit, développé et enrichi afin d’offrir un contenu actualisé et approfondi, tout en conservant l’esprit pédagogique de la version initiale de Philippe Pierre. Les schémas ont également été refaits.

+++



# Introduction
<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>

## Aperçu du cours
<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>

Ce cours propose une introduction complète aux fondamentaux des réseaux IP et se structure en quatre grandes parties, chacune abordant un aspect essentiel pour comprendre, configurer et diagnostiquer un réseau informatique.

### Protocole TCP/IP

Dans cette première partie, nous poserons les bases nécessaires en explorant la notion de réseau et l’historique du protocole TCP/IP. Nous étudierons ses composantes majeures : l’IP, le TCP, ainsi qu’une brève incursion dans le protocole QoS IPv5. Nous aborderons également les primitives de services pour comprendre la logique d’échange de données.

### L’adressage IPv4

Nous poursuivrons avec un module dédié à l’adressage IPv4. Vous apprendrez l’utilisation concrète de l’IPv4, ses différents types d’adresses (privées, publiques, broadcast…), le rôle fondamental du DNS, ainsi que le fonctionnement de l’adresse Ethernet et du protocole ARP. Vous découvrirez également la traduction d’adresses via le NAT et la configuration réseau de base.

### L’adressage IPv6

La troisième partie sera consacrée à l’adressage IPv6, nécessaire pour répondre aux limites de l’IPv4. Nous détaillerons ses normes et définitions, l’assignation des adresses dans un réseau local, la gestion des blocs d’adresses et la relation entre IPv6 et le DNS.

### Outils de diagnostic réseau

Enfin, nous conclurons par une présentation des principaux outils de diagnostic réseau. Ces derniers vous permettront d’analyser, contrôler et résoudre les dysfonctionnements. Cette partie sera structurée par couches : Accès Réseau, Réseau, Transport et supérieure.

À l’issue de ce parcours, vous disposerez des connaissances fondamentales pour administrer efficacement une infrastructure réseau et diagnostiquer ses éventuelles défaillances.

Prêt à plonger dans l’univers des réseaux informatiques ? Allons-y ! 

**REMARQUE** : les descriptions sont celles d’un système GNU/Linux CentOS 7. Mais, les configurations réseau sont sensiblement les mêmes entre un système Debian et un système CentOS. Donc, on ne fera pas de différence. Lorsqu’il y en aura une, on la préfixera avec un logo spécifique.

*N.B. : Si vous rencontrez des termes qui vous sont inconnus au cours de la formation, veuillez consulter [le glossaire](https://planb.network/resources/glossary) pour en trouver les définitions.*


# Les protocoles TCP/IP
<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>


## Qu’est-ce qu’un réseau ?
<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>

Dans ce premier module, nous allons présenter de manière approfondie le fonctionnement du protocole TCP/IP, pierre angulaire de nos communications numériques modernes. Nous y aborderons notamment ses origines, ses principes fondamentaux et le système d’adressage qui en découle, indispensable pour garantir la circulation de l’information entre les différents équipements connectés.

Nous détaillerons également les principaux composants qui structurent ce modèle et expliquerons comment ces éléments interagissent pour former un réseau opérationnel, fiable et extensible. Mais avant toute chose, il est essentiel de revenir à la notion même de réseau.

Étymologiquement, un réseau désigne un ensemble de points reliés entre eux par des liens, formant une structure interconnectée. Dans le domaine des télécommunications et de l’informatique, cette définition se traduit concrètement par un regroupement d’équipements (ordinateurs, routeurs, commutateurs, points d’accès...) capables d’échanger des données par l’intermédiaire de supports physiques ou sans fil. Un réseau permet ainsi la circulation d’informations de manière continue ou intermittente, selon les besoins, les protocoles utilisés et la nature de l’architecture déployée.

Au fil du temps, différentes topologies se sont imposées pour répondre à des besoins spécifiques en termes de coût, de performance, de résilience ou encore de facilité de maintenance. Parmi ces topologies classiques, on retrouve notamment :
- le réseau en anneau,
- le réseau en arbre,
- le réseau en bus,
- le réseau en étoile,
- le réseau maillé.

### Réseau en anneau

Une topologie en anneau se caractérise par une connexion des équipements selon une boucle fermée : chaque station est reliée à la suivante jusqu’à ce que la dernière soit connectée à la première. Dans ce schéma, chaque équipement agit comme un relais pour transmettre les données au maillon suivant, ce qui permet à l’information de circuler dans un seul sens ou parfois dans les deux sens selon le type de réseau.

L’avantage d’une telle organisation réside dans la simplicité de son câblage et dans l’absence de dépendance vis-à-vis d’un équipement central. Toutefois, la continuité du réseau repose sur la bonne santé de chaque élément : la défaillance d’un seul poste peut interrompre l’ensemble de la communication, ce qui impose souvent la mise en place de mécanismes de redondance ou de contournement.

![Image](assets/fr/001.webp)

### Réseau en arbre

Le réseau en arbre, ou topologie hiérarchique, s’inspire directement de la structure d’un arbre généalogique. Il est constitué de niveaux successifs : un nœud racine situé au sommet dessert plusieurs nœuds de rang inférieur, eux-mêmes pouvant alimenter d’autres nœuds et ainsi de suite.

Cette organisation hiérarchique est particulièrement adaptée aux réseaux étendus nécessitant une répartition claire des responsabilités et une gestion segmentée. Toutefois, cette structuration rend le réseau vulnérable à la défaillance des nœuds supérieurs : la perte du sommet ou d’un branchement principal peut priver de connectivité une partie entière de l’infrastructure.

![Image](assets/fr/002.webp)

### Réseau en bus

Dans une topologie en bus, tous les équipements partagent un même support de transmission, généralement une ligne coaxiale ou une fibre optique. Chaque unité est connectée de manière passive, sans modification active du signal, et peut émettre ou recevoir des données sur ce canal commun.

Le principal avantage d’un réseau en bus est son coût d’installation réduit grâce à un câblage simplifié. Cependant, dans les implémentations historiques reposant sur un support coaxial (Ethernet 10BASE2/10BASE5), la déconnexion ou la panne d’une station peut perturber, voire interrompre, l’ensemble du trafic : la continuité électrique du bus et son impédance de terminaison ne sont alors plus respectées. Aussi, le support physique unique représente un point critique : toute coupure ou dysfonctionnement de ce média entraîne l’arrêt complet de la communication pour l’ensemble du réseau.

![Image](assets/fr/003.webp)

### Réseau en étoile

La topologie en étoile, appelée "*hub and spoke*", est aujourd’hui la plus répandue, notamment grâce au réseau Ethernet domestique et professionnel. Tous les périphériques y sont reliés à un équipement central.

Cette disposition offre une grande facilité de gestion et de maintenance : la défaillance d’un nœud périphérique n’affecte pas la totalité du réseau. En revanche, le dispositif central représente un point de défaillance unique : sa panne entraîne l’arrêt global de la communication. Il convient également de veiller à la qualité du câblage et à la longueur des liaisons afin d’assurer des performances optimales.

![Image](assets/fr/004.webp)

**Remarque** : il existe encore des réseaux organisés selon une topologie linéaire, proche du bus, où les équipements sont raccordés les uns à la suite des autres. Cette solution, bien que peu coûteuse à déployer, présente l’inconvénient majeur qu’une seule rupture isole une partie des hôtes et scinde le réseau en sous-ensembles indépendants.

### Réseau maillé

Le réseau maillé est conçu pour offrir une redondance maximale : chaque équipement est directement relié à tous les autres. Une telle organisation garantit une continuité de service même en cas de défaillance de plusieurs liens ou hôtes, car le trafic peut être redirigé par des chemins alternatifs.

En contrepartie, le nombre de connexions à établir croît rapidement avec le nombre de terminaux. Pour `N` points de connexion, il faut prévoir `N × (N-1) / 2` liaisons distinctes, ce qui rend cette topologie coûteuse et complexe à mettre en place. Elle est donc réservée aux réseaux critiques nécessitant une haute disponibilité, comme certains segments d’Internet ou des infrastructures industrielles sensibles.

![Image](assets/fr/005.webp)

Il existe par ailleurs d’autres variantes topologiques, telles que les réseaux en grille ou en hypercube, qui répondent à des besoins spécifiques en matière de calcul distribué ou de traitement parallèle.

À l’échelle mondiale, Internet se présente comme une interconnexion massive de réseaux utilisant des topologies diverses, unifiés par un adressage commun (IPv4 et IPv6) et une collection de protocoles normalisés définis par l’IETF (*Internet Engineering Task Force*). C’est cette hétérogénéité qui fait dire qu’Internet n’obéit à aucune topologie unique : sa structure est souple, évolutive et indépendante du schéma d’adressage logique qui la rend exploitable.

## Les origines de TCP/IP
<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>

À l’origine du protocole TCP, on trouve l’**ARPA** (*Advanced Research Projects Agency*, renommée "DARPA" en 1972), qui lança dès 1966 le projet **ARPANET**. Le premier segment d’ARPANET devient opérationnel en octobre 1969, et interconnecte les universités de l’UCLA et de Stanford. L’objectif était de relier des centres de recherche au moyen d’un réseau à commutation de paquets capable de poursuivre ses communications même en cas de défaillance partielle de l’infrastructure.

Dans cette dynamique, l'ARPA finança notamment l'université de Berkeley afin d’intégrer les premiers protocoles TCP/IP au sein de son système Unix BSD, ce qui a contribué à la diffusion et à la normalisation de ce protocole dans le monde académique et plus tard dans le monde industriel.

**Remarque** : à cette époque, les informaticiens ne disposaient pas encore de Linux, qui ne verra le jour qu’au début des années 1990, ni même réellement de Minix, le système éducatif conçu par Andrew Tanenbaum. Les options se limitaient essentiellement à Unix, ou parfois à des systèmes centraux propriétaires comme OpenVMS. Unix, grâce à sa souplesse et son ouverture, joua donc un rôle essentiel dans la propagation des premiers concepts de mise en réseau.

Le protocole TCP/IP (qui devrait plus justement être désigné comme une suite de protocoles articulés autour de TCP et IP) s’est imposé grâce à sa capacité à offrir une interface de programmation standardisée pour l’échange de données entre machines sur un même réseau. Cette interface qui repose sur l’utilisation de primitives appelées "*sockets*", facilite la création de connexions fiables et flexibles, tout en intégrant des protocoles applicatifs essentiels.

ARPANET constitue donc le socle historique de l’Internet moderne. En effet, Internet est un réseau mondial fondé sur le principe de la commutation de paquets, où l’information circule au moyen d’un ensemble de protocoles standardisés qui assurent la compatibilité et l’interopérabilité entre des systèmes hétérogènes. Cette architecture ouverte permet le développement et l’exploitation de nombreux services et applications, parmi lesquels :
- les emails,
- le World Wide Web (www),
- le transfert et le partage de fichiers...

La gouvernance et l’évolution de ces protocoles sont supervisées par l’***Internet Architecture Board*** (IAB). Cet organisme coordonne les orientations techniques par l’intermédiaire de deux structures principales :
- **IRTF** (_Internet Research Task Force_), qui mène des recherches de fond sur l’évolution et l’amélioration des protocoles ;
- **IETF** (_Internet Engineering Task Force_), qui élabore, standardise et documente les protocoles opérationnels déployés sur Internet.

Pour la distribution des ressources réseau (plages d’adresses IP, numéros de systèmes autonomes, noms de domaine racine...) la coordination internationale relève aujourd’hui de l’**IANA/ICANN**. La gestion opérationnelle s’appuie sur cinq **RIR** (*Regional Internet Registries*) : **RIPE NCC** (Europe, Moyen-Orient, Asie centrale), **ARIN**, **APNIC**, **LACNIC** et **AFRINIC**.

L’ensemble des spécifications des protocoles TCP/IP est consigné dans des documents appelés **RFC** (_Request For Comments_), véritables références techniques, dont la numérotation est en perpétuelle évolution pour refléter l’enrichissement constant de la suite protocolaire.

La pile TCP/IP est souvent représentée comme un empilement de quatre couches fonctionnelles, parfois mises en parallèle avec le modèle **OSI** (_Open Systems Interconnection_) élaboré par l’**ISO** (_International Standards Organization_), qui compte sept couches et constitue une référence conceptuelle en matière de réseaux.

On distingue ainsi dans la pile TCP/IP :
- la couche ACCÈS RÉSEAU, qui assure la liaison physique et les protocoles de contrôle d’accès au média ;
- la couche INTERNET, qui prend en charge le routage et l’adressage IP ;
- la couche TRANSPORT, qui garantit la fiabilité et la gestion des flux de données grâce à des protocoles tels que TCP ou UDP ;
- la couche APPLICATION, qui regroupe les protocoles destinés aux utilisateurs et aux logiciels comme HTTP, FTP, SMTP ou encore DNS.

![Image](assets/fr/006.webp)

Aujourd’hui, la version la plus utilisée du protocole IP est IPv4, mais ses limitations en matière d’adressage (32 bits) ont conduit à l’élaboration de la version IPv6. Cette dernière, avec son adressage sur 128 bits, offre une capacité quasi illimitée, essentielle pour accompagner l’expansion fulgurante des équipements connectés et répondre aux enjeux de l’Internet des objets, de la mobilité et de la sécurité.

Chaque couche de la pile TCP/IP apporte des services spécifiques, permettant de traiter de manière modulaire les différentes problématiques : transmission physique, adressage logique, intégrité des échanges et services applicatifs.

| Périphérique estimé    | Description                                                                               | Couche du modèle TCP/IP |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Serveur web            | Services applicatifs au plus proche des utilisateurs                                      | Application             |
| Passerelle ou proxy    | Encode, crypte, compresse les données utiles                                              | Application             |
| Commutateur de session | Établit des sessions entre des applications                                               | Application             |
| Pare-feu ou routeur L4 | Établit, maintient et termine les sessions entre périphériques terminaux                  | Transport               |
| Routeur                | Adresse globalement les interfaces et détermine les meilleurs chemins à travers un réseau | Réseau                  |
| Commutateur (switch)   | Adresse localement les interfaces, transmet localement via MAC                            | Accès au Réseau         |
| Carte réseau (NIC)     | Encodage du signal, câblage, connecteurs, spécifications physiques                        | Accès au Réseau         |

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864

## Le protocole QoS IPv5
<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>

L’en-tête d’un paquet IP est une structure de données essentielle, organisée en plusieurs champs distincts, chacun remplissant une fonction précise pour assurer la bonne transmission et le traitement des paquets tout au long de leur parcours sur le réseau. Parmi ces champs, on trouve notamment l’adresse IP de destination, indispensable pour aiguiller correctement le paquet vers son destinataire final, mais aussi la longueur de l’en-tête, indiquée par le champ IHL (*Internet Header Length*), et la longueur totale du paquet, stockée dans le champ *Total Length*, des informations de contrôle et de vérification, et d’autres paramètres permettant de gérer le flux et la qualité de la communication.

Le tout premier champ de cet en-tête se nomme "Version". Il occupe 4 bits et indique clairement la version du protocole IP à laquelle le paquet se conforme. Cette version est importante, car elle informe chaque routeur ou équipement intermédiaire de la manière dont il doit interpréter et manipuler les données encapsulées.

**Remarque** : la gestion et l’attribution des versions de protocoles IP relèvent de l’**IANA**. Un champ de 4 bits permet 16 combinaisons binaires (valeurs 0 à 15). À ce jour, leur affectation est la suivante :

| Version Number | Protocol   | Version Description         | Reference               |
| -------------- | ---------- | --------------------------- | ----------------------- |
| 0–1            | Reserved   | Reserved                    |                         |
| 2–3            | Unassigned | Unassigned                  |                         |
| 4              | IP         | Internet Protocol           | RFC 791                 |
| **5**          | **ST**     | **ST Datagram mode**        | **RFC 1190** / RFC 1819 |
| 6              | IPv6       | Internet Protocol version 6 | RFC 8200                |
| 7              | TP/IX      | The Next Internet           | RFC 1475                |
| 8              | PIP        | The P Internet Protocol     | RFC 1621                |
| 9              | TUBA       | Tuba                        | RFC 1347                |
| 10–14          | Unassigned | Unassigned                  |                         |
| 15             | Reserved   | Reserved                    |                         |

Parmi ces versions figure la version IPv5, qui, bien que méconnue du grand public, a bel et bien existé sous la forme du protocole ST (_Stream Protocol_). Conçu dans les années 1980, IPv5 visait principalement à répondre à un besoin émergent à l’époque : garantir une "_Quality of Service_" ou "QoS" pour certains flux de données nécessitant une transmission continue et stable, comme la voix sur IP ou les flux multimédias. L’objectif était d’offrir une bande passante et une priorité garanties de bout en bout, un concept similaire à ce que propose aujourd’hui le protocole RSVP (_Resource Reservation Protocol_) pour la réservation dynamique de ressources réseau sur les routeurs modernes.

Cependant, le protocole IPv5 est resté au stade expérimental et n’a été mis en œuvre que sur une poignée d’équipements réseau. Son adoption limitée et l’évolution rapide des besoins en adressage ont conduit les concepteurs de l’Internet à opter pour un saut direct de la version IPv4 à IPv6. Ce choix visait notamment à contourner les limitations d’adressage posées par IPv4, tout en évitant toute confusion ou incompatibilité avec les spécifications expérimentales de la version 5.

Ainsi, bien que le protocole IPv5 ait contribué à ouvrir la voie à la réflexion sur la qualité de service et la gestion du trafic, il n’a jamais été déployé à grande échelle et reste aujourd’hui un jalon historique plus qu’un standard utilisé.

**Rappel** : un protocole définit avant tout un ensemble de règles de communication : structures de données, algorithmes, formats de paquets et conventions permettant à différents équipements d’échanger des informations de manière fiable et compréhensible. Le service, quant à lui, correspond à l’implémentation concrète de ce protocole au travers de programmes spécifiques (clients, serveurs) qui mettent en œuvre ces règles et rendent les fonctionnalités accessibles aux utilisateurs et aux applications.

Nous pouvons désormais nous pencher plus en détail sur la structure et le fonctionnement du protocole IP, socle indispensable de toute communication en réseau.

## Le protocole IP
<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>

### Définitions et généralités

Le protocole IP, ou "***Internet Protocol***", constitue la pierre angulaire du modèle TCP/IP : il assure le transport des paquets de données d’un hôte à un autre au sein d’un réseau, qu’il soit local ou étendu à l’échelle mondiale. Son rôle est double : il prend en charge l’adressage logique des équipements et garantit l’acheminement des paquets à travers des réseaux souvent hétérogènes et interconnectés.

Au niveau physique, la transmission repose sur des interfaces matérielles qui établissent les connexions point à point entre les nœuds. Toutefois, c’est bien le protocole IP qui rend possible la communication de bout en bout en fournissant à chaque paquet les informations nécessaires pour trouver sa route parmi un ensemble de chemins possibles.

Grâce à trois éléments de configuration réseau, il est possible de déterminer comment orienter un paquet vers sa destination :

- **L’adresse IP** : identifie de manière unique l’hôte de destination dans le réseau.
- **Le masque de sous-réseau** : précise la partie de l’adresse qui désigne le réseau et celle qui identifie l’hôte, ce qui facilite le découpage logique en sous-réseaux.
- **La passerelle** : indique le routeur intermédiaire par lequel le paquet peut transiter pour atteindre un réseau extérieur ou une autre portion du réseau local.

Sur Internet, les données ne circulent pas sous forme de flux continus mais sous forme de **datagrammes**, c’est-à‑dire des blocs de données autonomes encapsulés avec toutes les informations indispensables à leur acheminement. Ce principe illustre la **commutation de paquets**, qui permet de fragmenter l’information en unités indépendantes pouvant emprunter des chemins différents pour rejoindre le même destinataire.

Chaque datagramme IP contient ainsi, en plus de la charge utile (*payload*), un en-tête structuré où figurent notamment l’adresse de destination, l’adresse source, le type de service, le numéro de version du protocole, et diverses informations de contrôle nécessaires à la gestion de la transmission.

La taille maximale théorique d’un datagramme IP est de **65 536 octets**, valeur fixée par la limite de codage du champ longueur totale dans l’en-tête. Dans la pratique, cette taille est rarement atteinte car les réseaux physiques sur lesquels transitent les paquets (Ethernet, Wi-Fi, fibre optique…) imposent souvent des contraintes plus strictes, connues sous le nom de **MTU** (_Maximum Transmission Unit_). Si un datagramme excède la capacité du lien physique, il doit être fragmenté en paquets plus petits, chaque fragment étant transmis séparément puis réassemblé à l’arrivée.

Cette capacité d’adaptation fait du protocole IP un protocole robuste et flexible, apte à s’appuyer sur une multitude de technologies sous-jacentes tout en assurant une compatibilité universelle entre les systèmes et réseaux hétérogènes.

### Fragmentation des datagrammes IP

Lorsqu’un datagramme IP doit transiter sur un réseau dont la capacité de transmission est inférieure à sa taille, il devient nécessaire de le **fragmenter** pour qu’il puisse être transporté sans encombre. Cette limite physique de taille est donc désignée par le terme **MTU**, c’est-à‑dire la taille maximale qu’une trame peut atteindre sur un réseau donné sans nécessiter de découpage préalable.

Chaque technologie de réseau impose son propre MTU en fonction de ses caractéristiques matérielles et protocolaires. Parmi les valeurs les plus répandues, on peut citer :

- **ARPANET** : 1000 octets
- **Ethernet** : 1500 octets
- **FDDI** : 4470 octets

Quand un datagramme dépasse le MTU d’un segment de réseau qu’il doit emprunter, les équipements de routage se chargent de le **fragmenter** en plusieurs morceaux plus petits, chacun respectant la limite imposée. Cette opération se produit typiquement lors du passage d’un réseau à haut MTU vers un réseau à plus faible capacité. Par exemple, un datagramme provenant d’un réseau FDDI peut être fragmenté pour être transmis sur un segment Ethernet.

![Image](assets/fr/008.webp)

Le processus de fragmentation se déroule ainsi :
- Le routeur découpe le datagramme en fragments de taille inférieure ou égale au MTU du réseau cible.
- Il veille également à ce que chaque fragment ait une taille qui soit un multiple de 8 octets, car le protocole IP utilise ce multiple pour coder correctement l’offset de réassemblage.
- Chaque fragment reçoit son propre en-tête IP, qui comporte notamment des informations indispensables pour permettre au destinataire final de réassembler les fragments dans l’ordre initial.

Ces fragments sont ensuite transmis indépendamment les uns des autres : chacun peut suivre un chemin différent à travers le réseau, en fonction des tables de routage, de la charge des liaisons ou d’éventuelles pannes sur certaines routes. Rien ne garantit donc qu’ils parviendront à destination dans l’ordre où ils ont été émis.

Au moment de l’arrivée, c’est la machine destinatrice qui se charge du **réassemblage**. Grâce aux informations contenues dans les en-têtes (identifiant commun, offset et indicateurs de fragmentation) le système réordonne les fragments pour reconstituer le datagramme initial avant de le transmettre à la couche supérieure. Si l’un des fragments est perdu ou corrompu pendant la transmission, l’intégralité du datagramme est généralement rejetée, car sans tous les morceaux, le contenu reconstitué serait incomplet ou incohérent.

Ce mécanisme de fragmentation et de réassemblage, bien qu’efficace, présente néanmoins certaines limites en termes de performance et de charge réseau : chaque fragment ajoute une surcharge de traitement pour les routeurs et les hôtes, et le risque de perte de fragments augmente le taux de retransmission. C’est pourquoi la gestion adéquate du MTU et l’optimisation de la taille des paquets transmis restent des aspects importants pour garantir une communication fluide et efficace sur un réseau IP.

### Encapsulation des données

Pour garantir l’acheminement correct des données à travers les différentes couches du modèle TCP/IP, le mécanisme de l’**encapsulation** joue un rôle important. À chaque étape du passage d’un message depuis l’application de l’expéditeur jusqu’à la machine destinataire, des informations supplémentaires (appelées entêtes) sont ajoutées afin de fournir aux équipements intermédiaires et aux couches logicielles les instructions nécessaires au traitement, à la livraison et, le cas échéant, à la reconstitution de l’information initiale.

Lorsqu’un message est émis, il traverse successivement les quatre couches de la pile TCP/IP. À chaque couche, un nouvel entête est préfixé au bloc de données existant : chaque entête contient des métadonnées spécifiques, telles que les adresses logiques ou physiques, les ports de communication, les numéros de séquence, les indicateurs de contrôle d’erreurs, et toute information permettant de gérer la transmission et le routage.

Ainsi, la transmission suit un processus structuré : la couche Application génère le **message** initial, contenant les données brutes. La couche Transport encapsule ce message dans un **segment**, en y adjoignant notamment les ports source et destination, les numéros de séquence et les mécanismes de contrôle de flux. La couche Internet prend le segment, y ajoute un entête IP pour former un **datagramme**, spécifiant notamment les adresses IP source et destination. Enfin, la couche Accès Réseau encapsule ce datagramme dans une **trame**, en ajoutant des informations comme les adresses MAC et les codes de vérification d’intégrité (CRC).

![Image](assets/fr/009.webp)

Ce processus d’encapsulation assure non seulement l’intégrité et la traçabilité des données, mais aussi leur adaptabilité : à chaque transition d’un réseau à un autre, les entêtes fournissent aux équipements les informations essentielles pour décider de l’itinéraire, vérifier la validité ou procéder à la fragmentation si nécessaire.

À l’arrivée, le mécanisme s’inverse : la machine réceptrice reçoit la trame au niveau de la couche Accès Réseau, qui lit l’entête correspondant et le retire. Le datagramme est ensuite transmis à la couche Internet, qui lit l’entête IP, puis l’enlève à son tour pour livrer le segment à la couche Transport. Cette dernière traite les entêtes de transport, vérifie l’intégrité du flux et remet finalement le **message** à l’application cible dans son état originel.

![Image](assets/fr/010.webp)

Ce schéma illustre la transformation progressive des données à chaque niveau :

- **Message** : bloc d’information au niveau de la couche Application.
- **Segment** : unité de données après encapsulation par la couche Transport.
- **Datagramme** : forme prise à la suite de l’ajout de l’entête IP par la couche Internet.
- **Trame** : bloc final prêt à être transmis sur le support physique par la couche Accès Réseau.

![Image](assets/fr/011.webp)

Ce processus, essentiel à la fiabilité et à l’universalité des communications sur Internet, garantit que chaque donnée, aussi fragmentée ou complexe soit-elle, puisse être transportée de bout en bout tout en restant compréhensible et exploitable par la machine réceptrice.

### Adressage IP

Même en appliquant les mécanismes fondamentaux de commutation de paquets, de fragmentation et d’encapsulation, un réseau ne pourrait remplir sa mission sans un système d’adressage rigoureux. Pour que chaque paquet de données trouve son chemin vers le bon destinataire, la couche Internet s’appuie sur un identifiant unique : l’**adresse IP**. En version IPv4, celle-ci est codée sur **32 bits** et se présente sous la forme de quatre nombres décimaux séparés par des points, selon le format classique N1.N2.N3.N4 (par exemple : 192.168.1.12).

Une adresse IP est structurée en deux parties distinctes : la première, appelée **_netid_**, identifie le réseau auquel appartient l’hôte ; la seconde, le **_hostid_**, précise l’hôte individuel à l’intérieur de ce réseau. Cette séparation logique facilite la hiérarchisation et l’organisation du réseau mondial en de multiples réseaux interconnectés.

Historiquement, le système IPv4 s’appuie sur un découpage en classes, notées de A à E, qui détermine l’étendue des plages d’adresses et leur usage. Chaque classe réserve un nombre défini de bits au _netid_ et au _hostid_, ce qui influe directement sur le nombre de réseaux et d’hôtes possibles.

| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Il faut savoir que toutes les combinaisons binaires ne sont pas exploitables pour identifier des hôtes. Dans une adresse de **classe C**, par exemple, le dernier octet offre 8 bits, soit 256 valeurs possibles. Toutefois, deux d’entre elles ont une fonction spéciale : la valeur 0 désigne le réseau lui-même, tandis que 255 correspond à l’adresse de **diffusion** (_broadcast_), qui permet d’envoyer un paquet à tous les hôtes du réseau en une seule fois. Il reste donc 254 adresses réellement utilisables pour des machines.

Le nombre maximum d’adresses varie sensiblement d’une classe à l’autre, ce qui permet d’adapter le plan d’adressage aux besoins : de vastes réseaux publics pour les classes A, des réseaux d’entreprise pour les classes B, ou des réseaux plus restreints pour les classes C.

![Image](assets/fr/013.webp)

Certaines plages d’adresses sont réservées et ne transitent jamais sur Internet. On parle alors d’**adresses privées**, destinées aux réseaux internes d’organisations, d’entreprises ou de particuliers. Elles ne peuvent pas être routées directement sur Internet sans passer par une traduction d’adresses, généralement assurée par un dispositif NAT (*Network Address Translation*). Ces plages sont :
- Pour la **Classe A** : de 10.0.0.0 à 10.255.255.255
- Pour la **Classe B** : de 172.16.0.0 à 172.31.255.255
- Pour la **Classe C** : de 192.168.0.0 à 192.168.255.255

Lorsqu’un équipement interne utilise l’une de ces adresses pour accéder à Internet, son adresse privée est remplacée par une adresse publique valide par un routeur ou une passerelle NAT.

Prenons un exemple : si un hôte possède l’adresse **192.168.7.5**, on peut en déduire plusieurs informations complémentaires. L’adresse **192.168.7.0** correspond au réseau, **192.168.7.1** est souvent attribuée au routeur local, **192.168.7.5** désigne l’hôte spécifique.

Une adresse particulière mérite d’être citée : **127.0.0.1**, appelée "***loopback***" ou adresse de **bouclage**. Sur les systèmes Linux, elle est associée à l’interface **lo**. Cette adresse permet à une machine de s’adresser à elle-même pour des tests ou des diagnostics locaux, sans passer par une interface physique. L’ensemble de la plage **127.0.0.0/8** est réservé à cet usage.

Pour optimiser l’utilisation des adresses et organiser des réseaux complexes, le concept de **masque de sous-réseau** (_netmask_) est indispensable. Ce masque binaire permet de distinguer, à l’intérieur d’une adresse IP, la partie _netid_ de la partie _hostid_. Chaque classe dispose d’un masque par défaut : **255.0.0.0** pour la classe A, **255.255.0.0** pour la classe B et **255.255.255.0** pour la classe C.

Une bonne conception réseau repose sur le respect d’un principe fondamental : les machines qui doivent échanger directement des données doivent appartenir au même réseau ou au même sous-réseau. Pour répondre à des besoins de segmentation, on procède donc souvent au ***subnetting***, c’est-à‑dire à la division d’un réseau en sous-réseaux plus petits grâce à des masques plus fins.

Prenons un cas concret. Soit un réseau de **classe C** : 192.168.1.0/24 avec un masque initial de 255.255.255.0. Si l’on souhaite organiser ce réseau pour accueillir quatre sous-réseaux de 60 machines chacun, plusieurs étapes sont nécessaires.

**Étape 1** : Déterminer le nombre d’adresses nécessaires. Ici, 60 hôtes + 2 adresses réservées (réseau et diffusion) donnent 62 adresses par sous-réseau.

**Étape 2** : Chercher la puissance de deux immédiatement supérieure. 2⁶ = 64.

**Étape 3** : Adapter le masque en conséquence. En binaire, on conserve les bits du _netid_ et on réserve les bits nécessaires au _hostid_. Ici, on obtient un masque binaire qui, une fois converti, donne **255.255.255.192**.

```
11111111 11111111 11111111 11000000
```


**Étape 4** : Calculer les plages d’adresses pour chaque sous-réseau en variant les bits réservés à l’hôte.

| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Étape 5** : Ainsi, on obtient quatre sous-réseaux, chacun capable d’héberger jusqu’à 62 machines, tout en conservant l’efficacité du plan d’adressage global. La partie _hostid_ de l’adresse est donc subdivisée en deux : une pour le _subnetid_ et l’autre pour l’hôte proprement dit.

![Image](assets/fr/016.webp)

Ce principe fondamental du subnetting reste incontournable dans l’ingénierie réseau moderne, car il permet d’allouer les ressources IP avec précision, de contrôler le trafic et d’assurer une bonne isolation entre segments tout en maintenant une gestion claire et évolutive.

### Adressage CIDR

Au début des années 1990, avec l’essor fulgurant d’Internet dans le monde des entreprises et des organismes, le système classique d’attribution d’adresses IP basé sur les classes (A, B, C) a révélé ses limites. En effet, cette approche, rigide par nature, provoquait un gaspillage conséquent d’adresses IP et compliquait considérablement la gestion des tables de routage, qui devenaient de plus en plus volumineuses et difficiles à maintenir à jour. Pour pallier ces contraintes, une solution plus souple et optimisée a vu le jour : le **CIDR** (_Classless Inter-Domain Routing_), qui s’est progressivement imposé comme la norme et a largement supplanté l’ancien modèle par classes.

L’idée fondatrice du CIDR est de pouvoir regrouper plusieurs réseaux adjacents, notamment des blocs de classe C, en une seule entité logique appelée **superréseau** (_supernet_). Grâce à cette agrégation, une seule entrée suffit dans les tables de routage pour représenter plusieurs sous-réseaux, ce qui réduit significativement la taille des routes gérées par les routeurs et améliore leur performance. À l’origine, le besoin d’agrégation était surtout pressant pour les adresses de classe C, plus restreintes en capacité, mais le concept s’est étendu aux classes B, et même par principe aux classes A, bien que la problématique y soit moins critique en raison de la vaste plage d’adresses qu’elles offrent.

Avec le CIDR, la notion de classe disparaît : l’espace d’adressage est traité comme un continuum qu’il est possible de découper ou d’agréger à volonté selon les besoins. Concrètement, on peut ainsi définir des **blocs CIDR** en utilisant des masques de sous-réseau plus flexibles que ceux imposés par les classes standards. Ces blocs peuvent représenter soit un réseau unique, soit un ensemble contigu de sous-réseaux partageant le même préfixe.

Un bloc CIDR est désigné par la syntaxe _adresse/préfixe_, où le "/" est suivi du nombre de bits définissant la portion fixe du réseau. Par exemple, **/17** signifie que les dix-sept premiers bits de l’adresse représentent la partie réseau, laissant les quinze bits restants pour identifier les hôtes à l’intérieur de ce bloc.

Prenons un exemple concret : un bloc **/17** permet de disposer de 2^(32-17) adresses, soit 2^15 = 32 768 adresses potentielles. En soustrayant les deux adresses réservées (adresse du réseau et adresse de diffusion), on obtient 32 766 adresses réellement attribuables à des hôtes. Ce principe permet aux administrateurs réseaux de dimensionner très finement leurs plages IP, en ajustant les tailles des sous-réseaux aux besoins réels, sans gaspiller inutilement des adresses précieuses.

Pour faciliter la conversion et la compréhension, on utilise des tableaux de correspondance, tel que celui ci-dessous, qui présente les préfixes CIDR courants et leur équivalence en nombre d’adresses :

| CIDR Prefix | Available Host Bits | Subnet Mask     | Usable Host Addresses         |
| ----------- | ------------------- | --------------- | ----------------------------- |
| /8          | 24                  | 255.0.0.0       | 2^24 - 2 = 16,777,214         |
| /12         | 20                  | 255.240.0.0     | 2^20 - 2 = 1,048,574          |
| /16         | 16                  | 255.255.0.0     | 2^16 - 2 = 65,534             |
| /20         | 12                  | 255.255.240.0   | 2^12 - 2 = 4,094              |
| /24         | 8                   | 255.255.255.0   | 2^8 - 2 = 254                 |
| /26         | 6                   | 255.255.255.192 | 2^6 - 2 = 62                  |
| /27         | 5                   | 255.255.255.224 | 2^5 - 2 = 30                  |
| /28         | 4                   | 255.255.255.240 | 2^4 - 2 = 14                  |
| /29         | 3                   | 255.255.255.248 | 2^3 - 2 = 6                   |
| /30         | 2                   | 255.255.255.252 | 2^2 - 2 = 2                   |
| /31         | 1                   | 255.255.255.254 | 2^1 = 2 (point-to-point only) |
| /32         | 0                   | 255.255.255.255 | 1 (host address only)         |


**NOTE** : Historiquement, le RFC 950 considérait le sous-réseau zéro comme non standard et déconseillait son usage, principalement pour éviter des confusions lors du routage. Toutefois, cette restriction est devenue obsolète avec le RFC 1878, qui autorise pleinement son exploitation. Les anciennes réserves concernaient avant tout la compatibilité avec du matériel ancien, incapable de gérer correctement les notations CIDR. Aujourd’hui, grâce aux équipements modernes, cette limitation a disparu.

À titre d’exemple : le sous-réseau **1.0.0.0** associé à un masque de sous-réseau **255.255.0.0** illustre parfaitement ce principe : autrefois ambigu avec l’identifiant de réseau complet en classe A, il est désormais parfaitement valide et utilisable.

**ASTUCE** : pour réaliser sans erreur les calculs de sous-réseaux et convertir rapidement des adresses en notation CIDR, il existe des outils pratiques comme ***ipcalc***. Véritable calculette réseau, cet utilitaire simplifie la planification d’adressage en affichant clairement le découpage, les plages disponibles et les masques associés, ce qui est particulièrement utile pour les administrateurs et les étudiants qui souhaitent se familiariser avec cette notation devenue incontournable.

```shell
sudo apt install ipcalc
```

https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## Le protocole TCP
<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>

Le **protocole TCP** (_Transmission Control Protocol_) occupe une place centrale au sein de la **couche TRANSPORT** du modèle TCP/IP. Il constitue un maillon entre les applications et la couche Internet, en organisant le transfert fiable des données échangées entre deux machines distantes. Là où le protocole IP se contente de transmettre des paquets sans garantie de livraison ni d’ordre, TCP prend en charge l’intégrité et la cohérence du flux de données, ce qui garantit ainsi aux applications une communication sans perte, sans doublon et dans l’ordre d’envoi.

Les principales responsabilités de TCP peuvent se résumer ainsi :
- il réordonne les segments reçus,
- il surveille le flux de données pour éviter la congestion,
- il segmente ou recompose les blocs de données en unités adaptées (appelées **segments**),
- il gère les étapes d’établissement et de terminaison de la connexion entre les deux extrémités de la communication.

Concrètement, TCP est un protocole orienté connexion, ce qui signifie qu’il met en place une relation explicite et suivie entre le client et le serveur. Pour cela, il s’appuie sur un système de **numéros de séquence** et d’**accusés de réception** : à chaque segment envoyé, un identifiant unique est attribué pour permettre à la machine réceptrice de vérifier l’intégrité et l’ordre des données reçues. En retour, le destinataire renvoie un segment de confirmation avec un **flag ACK** positionné à 1, indiquant la bonne réception et précisant le prochain numéro attendu.

![Image](assets/fr/018.webp)

Pour renforcer la fiabilité, TCP intègre une minuterie : dès l’envoi d’un segment, un délai est activé. Si l’accusé de réception ne parvient pas dans ce laps de temps, le segment est réémis automatiquement, l’émetteur considérant qu’il a été perdu durant le transit. Ce mécanisme de retransmission automatique compense les pertes inhérentes aux réseaux IP, qui peuvent survenir en cas de surcharge, d’erreur de routage ou de panne d’équipement.

![Image](assets/fr/019.webp)

TCP est capable de détecter et gérer les doublons éventuels. Si un segment est réémis mais que l’original arrive tout de même, le destinataire, grâce aux numéros de séquence, identifie le doublon et ne conserve que la version correcte, ce qui élimine ainsi toute ambiguïté dans le flux reçu.

Pour que ce processus fonctionne, il est indispensable que les deux machines partagent une compréhension commune des numéros de séquence initiaux. Cela suppose que l’établissement de la connexion s’effectue en respectant une procédure stricte : d’un côté, le **serveur** écoute sur un port spécifique en attente d’une demande entrante (mode passif) ; de l’autre, le **client** initie activement la connexion en envoyant une requête au serveur via le même port de service.

**REMARQUE** : Un "port" est un identifiant numérique (allant de 0 à 65 535) attribué à une application réseau sur un ordinateur ; il sert à différencier plusieurs services qui utilisent simultanément la même adresse IP. Lorsqu’un client envoie des données, il précise le numéro de port afin que le système d’exploitation du serveur sache quel programme (par exemple : 80 pour HTTP, 443 pour HTTPS, 25 pour SMTP) doit recevoir la communication. Un port fonctionne donc comme une porte dédiée : il organise la circulation des paquets entrants et sortants, évite les confusions entre services et permet une gestion fine des accès grâce à des règles de pare-feu ou de filtrage.

L’échange de synchronisation des séquences repose sur le fameux mécanisme dit du **"*three-way handshake*"** (littéralement : "poignée de main en trois temps"), comparable à la manière dont deux personnes se saluent pour établir un contact. Cette phase d’initialisation, qui permet la fiabilité de TCP, se déroule donc en 3 étapes :

1. Le client envoie un premier segment de synchronisation (**SYN**) avec le flag approprié activé et un numéro de séquence initial (par exemple : C) ;
2. Le serveur à la réception répond en retour avec un segment d’accusé de réception (**SYN-ACK**) : il accuse réception du numéro de séquence du client et communique à son tour son propre numéro de séquence initial, incrémenté de 1 ;
3. Enfin, le client envoie un dernier segment (**ACK**) confirmant qu’il a bien reçu le numéro de séquence du serveur et finalise la synchronisation : le flag SYN est alors désactivé et le flag ACK reste positionné pour signifier que la connexion est prête.

![Image](assets/fr/020.webp)

Ce protocole d’échange garantit que les deux parties partagent la même base de numérotation avant de transmettre des données utiles. Une fois cette synchronisation réalisée, la session est ouverte : les segments peuvent circuler dans les deux sens, chacun étant accusé de réception, ce qui assure une fiabilité maximale du flux.

Ce ***three-way handshake*** concerne uniquement l’établissement de la connexion. Pour la fermeture, TCP utilise un *four-way handshake* : FIN → ACK → FIN → ACK, qui garantie qu’aucun segment en transit n’est perdu avant la libération complète de la session.

Enfin, bien que conçu pour la robustesse et la fiabilité, ce processus a aussi donné naissance à certaines vulnérabilités exploitables : des attaques comme l’**IP Spoofing** visent à contourner ou corrompre cette relation de confiance, en se faisant passer pour une machine autorisée grâce à la falsification des numéros de séquence, ouvrant ainsi une brèche pour intercepter ou manipuler le flux de données échangé.

Afin de limiter ces risques liés au détournement du mécanisme de synchronisation des séquences et de maîtriser la charge réseau, le protocole TCP a recours à une technique de gestion du flux appelée "**méthode de la fenêtre glissante**" ("_Sliding Window_"). Ce système permet de réguler la quantité de données qui peuvent être envoyées sans nécessiter immédiatement d’accusé de réception pour chaque segment, ce qui réduit ainsi la surcharge inutile sur le réseau tout en maintenant une bonne fiabilité.

Concrètement, la fenêtre glissante définit une plage de numéros de séquence autorisés à circuler librement entre l’émetteur et le récepteur sans que chaque segment individuel ne doive être accusé réception. À mesure que des accusés de réception parviennent au système émetteur, la fenêtre "glisse" : elle se décale vers la droite pour inclure de nouveaux segments à transmettre. La taille de cette fenêtre (importante pour optimiser le débit tout en évitant la congestion) est précisée dans le champ "*Window*" de l’en-tête TCP.

**Exemple** : si le numéro de séquence initial est 3 et que la fenêtre autorise jusqu’à la séquence 5, les segments compris entre 3 et 5 peuvent être envoyés sans attendre d’accusé de réception pour chacun.

![Image](assets/fr/021.webp)

Il est important de souligner que la taille de la fenêtre glissante n’est pas fixe. Elle s’ajuste dynamiquement en fonction de l’état du réseau et de la capacité de traitement du récepteur. Lorsqu’un récepteur estime pouvoir traiter un volume de données plus important, il peut indiquer au travers du champ "fenêtre" qu’une extension est souhaitée. L’émetteur adapte alors sa fenêtre en conséquence. À l’inverse, en cas de surcharge ou de risque de saturation, le récepteur peut demander une réduction : l’émetteur attendra alors que la fenêtre se déplace avant de poursuivre l’envoi de segments supplémentaires.

Concernant la **clôture d’une connexion TCP**, le protocole prévoit une procédure symétrique pour garantir la fin propre et ordonnée des échanges. L’une des deux machines peut initier la fermeture en émettant un segment avec le drapeau **FIN** positionné à 1, qui signale sa volonté de terminer la communication. Elle attend ensuite la fin de réception des segments encore en transit et ignore toute donnée ultérieure.

À réception de ce segment, la machine destinataire répond par un accusé de réception, également marqué du drapeau FIN : elle finalise l’envoi de ses propres segments en cours, puis informe l’application locale de la fermeture effective de la session. Ainsi, la fermeture est toujours double et contrôlée, ce qui minimise le risque de perte de données.

Cette gestion précise, qui allie la souplesse de l’acheminement IP au contrôle rigoureux de TCP, est souvent illustrée par un schéma mettant en parallèle la rapidité du protocole IP (qui fonctionne selon le principe **"best effort"** sans garantie de livraison) et la fiabilité du protocole TCP (qui encadre la transmission grâce à une logique d’accusés de réception et de séquences négociées).

![Image](assets/fr/022.webp)

Cependant, dans certaines situations, la priorité n’est pas donnée à la fiabilité absolue mais à la vitesse de transmission et à la simplicité. C’est notamment le cas pour des applications comme le streaming en direct ou la voix sur IP, qui tolèrent quelques pertes de paquets sans impact majeur sur l’expérience utilisateur. Dans ces cas, on privilégie le recours au **protocole UDP** (_User Datagram Protocol_).

UDP fonctionne sur un principe radicalement différent de TCP : il est **orienté sans connexion**, c’est-à‑dire qu’il ne met en place aucune relation préalable entre l’émetteur et le destinataire. Lorsqu’une machine émet des paquets via UDP, elle les envoie de façon unidirectionnelle : le destinataire reçoit les données sans jamais renvoyer d’accusé de réception, et l’émetteur ne sait pas précisément si le message est bien arrivé. L’en-tête UDP est volontairement minimaliste : il ne contient que le port source, le port destination, la longueur du segment et une checksum, sans mécanisme interne d’accusé de réception ni de contrôle d’état ; les adresses IP sont, comme toujours, portées par l’en-tête IP sous-jacent.

Cette logique est souvent comparée à une analogie du quotidien : le protocole TCP ressemble à un **appel téléphonique**, où un circuit est établi, suivi, et contrôlé tout au long de la conversation. À l’inverse, le protocole UDP s’apparente à l’envoi d’un **message par courrier**, où l’expéditeur glisse une lettre dans une boîte aux lettres sans garantie immédiate que le destinataire l’a bien reçue, ni retour d’information systématique.

Cette complémentarité entre TCP et UDP permet aux réseaux modernes de s’adapter à des usages variés, selon qu’ils requièrent une fiabilité maximale ou une rapidité d’exécution prioritaire.

## Primitives de services
<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>

### Architecture en couches et organisation des échanges

Comme nous l’avons évoqué précédemment, les **services** constituent l’implémentation concrète des protocoles que nous avons détaillés jusqu’ici. Le modèle TCP/IP, bien qu’il diffère du modèle **OSI**, hérite de son approche structurée en couches : chaque couche est conçue pour remplir un rôle spécifique et pour offrir des **services** à la couche immédiatement supérieure, ce qui établit ainsi une architecture modulaire, robuste et facilement maintenable.

Chaque couche s’appuie sur les fonctionnalités offertes par la couche inférieure et, réciproquement, fournit à la couche supérieure une interface cohérente pour gérer les données. Dans cette architecture, chaque couche dispose de **structures de données propres**, soigneusement définies pour garantir une parfaite compatibilité avec celles des autres couches. Cette compatibilité est indispensable pour assurer une transmission fluide, fiable et compréhensible des informations, d’un point d’extrémité à un autre.

Deux aspects fondamentaux organisent ces échanges :

- L’**aspect vertical**, qui décrit la relation entre une couche et la couche qui la surplombe ou la sous-tend (de la couche N vers la couche N+1, et inversement).

![Image](assets/fr/023.webp)

- L’**aspect horizontal**, qui met en lumière l’interaction entre les applications distantes, c’est-à-dire le dialogue qui s’établit d’un **client** vers un **serveur**, ou réciproquement.

![Image](assets/fr/024.webp)

L’architecture en couches repose sur le principe que chaque niveau ne traite que les informations qui relèvent de sa compétence : ainsi, les structures de données, les entêtes et les mécanismes de contrôle varient d’une couche à l’autre, mais l’ensemble forme un tout cohérent, permettant l’acheminement progressif des données vers leur destination finale.

**Rappel** : pour nommer les unités de données qui transitent entre les couches, une terminologie spécifique a été définie : **message** pour la couche Application, **segment** pour la couche Transport (TCP), **datagramme** pour la couche Internet (IP) et **trame** pour la couche Accès Réseau. Cette distinction s’accompagne de structures adaptées à chaque contexte, comme le montre le schéma suivant :

| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Primitives de service et unités de données

Au cœur de ce fonctionnement, les échanges entre couches reposent sur des **primitives de service**, qui servent d’interfaces de communication. Ces primitives jouent le rôle de guichets, qui écoutent sur des **ports spécifiques** réservés, et permettent ainsi aux processus d’établir, de maintenir et de terminer les connexions réseau de manière contrôlée. Si les protocoles organisent le format et la transmission des données sur le réseau, ce sont bien les **services et leurs primitives** qui assurent la liaison verticale entre les couches.

Ainsi, le modèle TCP/IP combine l’aspect horizontal (communication entre applications distribuées) et l’aspect vertical (interactions internes entre couches) pour offrir une architecture complète et extensible. La superposition de ces deux aspects donne une vue d’ensemble de l’échange de données dans une communication réseau structurée.

![Image](assets/fr/026.webp)

### Synthèse de la partie

Dans cette première grande partie, nous avons mis en lumière l’architecture fondamentale qui régit aujourd’hui la configuration et le fonctionnement des réseaux connectés à Internet. Cette architecture repose sur un **modèle en quatre couches**, inspiré du modèle OSI, et s’articule autour de la suite de protocoles **TCP/IP**, la colonne vertébrale des communications modernes. Nous avons vu que TCP, grâce à son approche orientée connexion, garantit un transfert fiable, tandis que l’UDP, plus léger et plus rapide, offre une alternative pour des usages où la rapidité prime sur la fiabilité.

Le bon fonctionnement de ce modèle repose sur l’implémentation des protocoles au moyen de **primitives de services**. Celles-ci assurent la liaison entre les couches et permettent d’adapter le traitement des données aux spécificités de chaque niveau, du transport à l’application, en passant par Internet et l’accès réseau. Cette approche modulaire rend le système à la fois souple et robuste.

L’adressage IP constitue un autre pilier de cette infrastructure. Chaque équipement connecté est identifié par une **adresse IP unique**, issue d’un espace structuré en **classes** (de A à E). Certaines de ces adresses sont réservées à des usages spécifiques, comme le bouclage local ou la multidiffusion, tandis que d’autres, dites "**adresses privées**", ne sont pas routées sur Internet sans être traduites (NAT). Cette classification permet une organisation logique et hiérarchique des réseaux.

Nous avons également abordé la notion de **sous-réseaux**, qui permet de fractionner un réseau en segments plus petits pour mieux gérer les ressources IP et optimiser la circulation des données. Si le découpage manuel à l’aide des masques de sous-réseaux reste un principe important, il a été largement modernisé grâce au **CIDR** (_Classless Inter-Domain Routing_). Cette méthode a transformé la gestion de l’adressage en permettant une attribution plus souple et plus rationnelle des plages IP, tout en réduisant la taille des tables de routage.

En maîtrisant ces concepts : couches, protocoles, primitives de services, adressage et sous-réseautage, on dispose des bases solides pour comprendre le fonctionnement technique des réseaux modernes et pour configurer efficacement une infrastructure réseau adaptée aux besoins actuels. Dans la prochaine partie, nous allons étudier plus précisément l'adressage IPv4.


# L’adressage IPv4
<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>

## Utilisation de l’IPv4
<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>

Cette deuxième partie approfondit les principes abordés précédemment en mettant l’accent sur la manière dont les **adresses IPv4** sont effectivement mises en œuvre dans un réseau informatique concret. Il s’agit ici de comprendre en détail non seulement leur format et leur logique, mais aussi les mécanismes qui permettent de relier ces adresses aux autres éléments indispensables du réseau : **noms DNS**, **adresses MAC**, **sous-réseaux** et **techniques de traduction**.

Une adresse IP est, pour rappel, un identifiant numérique unique attribué à chaque **interface réseau** d’un équipement. Elle permet de localiser cet équipement au sein d’un réseau et de l’atteindre pour lui transmettre des données. Ainsi, un routeur, un serveur, un poste de travail, une imprimante réseau ou même une caméra de surveillance dispose d’au moins une adresse IP propre. L’adresse IP sert de base à la **routabilité**, c’est-à-dire la capacité des équipements à acheminer les paquets d’un point A à un point B, même s’ils sont physiquement très éloignés.

Il est important de retenir qu’une adresse IP peut être attribuée de manière **statique**, c’est-à-dire fixée manuellement et inscrite dans la configuration de l’appareil, ou **dynamique**, c’est-à-dire allouée automatiquement à la demande grâce au protocole **DHCP** (_Dynamic Host Configuration Protocol_). Le DHCP simplifie la gestion du parc réseau, en évitant la configuration manuelle de chaque poste, tout en permettant un contrôle précis grâce à des réservations et des durées de bail.

Le protocole **IPv4**, toujours dominant malgré l’émergence de l’IPv6, utilise un format codé sur **32 bits**, divisés en **quatre octets**. Chaque octet, composé de 8 bits, est exprimé en décimal sous forme d’un nombre compris entre 0 et 255. Les 4 octets sont séparés par des points pour former une notation claire et lisible.

_Exemple : l’adresse 172.16.254.1_

![Image](assets/fr/027.webp)

Chaque bit au sein d’un octet a un poids bien défini : le bit de gauche (bit de poids fort) vaut 128, le suivant 64, puis 32, 16, 8, 4, 2 et 1 pour le bit de droite (bit de poids faible). Ainsi, l’écriture binaire est convertie en décimal par simple addition des poids activés.  
Le tableau ci-dessous rappelle cette correspondance :

| Binary Code | Activated Bit Values          | Decimal Value |
|-------------|-------------------------------|---------------|
| 00000000    | 0                             | 0             |
| 00000001    | 1                             | 1             |
| 00000011    | 1 + 2                         | 3             |
| 00000111    | 1 + 2 + 4                     | 7             |
| 00001111    | 1 + 2 + 4 + 8                 | 15            |
| 00011111    | 1 + 2 + 4 + 8 + 16            | 31            |
| 00111111    | 1 + 2 + 4 + 8 + 16 + 32       | 63            |
| 01111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64  | 127           |
| 11111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 | 255      |

Par exemple, pour convertir une adresse IP binaire en notation décimale, on additionne les valeurs des bits à 1 pour chaque octet.

| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

Il est important de noter qu’une adresse IP identifie **une interface réseau** et non l’appareil dans sa globalité. Un serveur multi-cartes, comme un pare-feu ou un routeur, possède donc plusieurs interfaces, chacune avec sa propre adresse IP. De plus, une seule interface peut se voir attribuer plusieurs adresses IP, notamment pour répondre à plusieurs réseaux virtuels ou services.

Chaque paquet IP encapsule l’adresse IP de **l’expéditeur** et celle du **destinataire** dans son en-tête. Les **routeurs**, situés aux jonctions des réseaux, lisent ces informations pour déterminer la route optimale pour transmettre le paquet de proche en proche jusqu’à la machine cible. Sans un adressage rigoureux, le trafic ne saurait être orienté correctement et l’interconnexion mondiale des réseaux serait impossible.

L’adressage IPv4 obéit à des règles précises : chaque adresse est composée de deux parties : le **NetID**, qui désigne le réseau de rattachement, et le **HostID**, qui identifie l’équipement au sein de ce réseau. La délimitation entre NetID et HostID est fixée par le **masque de sous-réseau**, qui précise combien de bits appartiennent à chaque portion. Plus le NetID est long, plus le nombre de sous-réseaux possibles est grand, mais le nombre d’hôtes par sous-réseau diminue en conséquence.

Dans les débuts d’IPv4, les réseaux étaient organisés en **classes** (A, B, C, D et E). Chaque classe correspond à une plage spécifique de NetID et définit une granularité fixe :

- Classe A : réseaux très vastes avec un grand nombre d’hôtes
- Classe B : réseaux de taille intermédiaire
- Classe C : réseaux de petite taille
- Classe D : adresses réservées à la multidiffusion (_multicast_)
- Classe E : adresses expérimentales, non utilisées pour l’adressage classique

| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Certaines adresses ont un rôle bien particulier. L’**adresse de réseau** désigne l’identifiant du réseau lui-même et sert à configurer les tables de routage ; l’**adresse de diffusion** (_broadcast_) permet d’envoyer un paquet à tous les hôtes d’un même sous-réseau en une seule émission : pour cela, tous les bits du HostID sont mis à 1.

Les plages suivantes sont réservées pour des usages internes :

- **10.0.0.0/8** (Classe A privée)
- **127.0.0.0/8** (bouclage local ou _loopback_)
- **172.16.0.0 à 172.31.255.255** (Classe B privée)
- **192.168.0.0 à 192.168.255.255** (Classe C privée)

Les adresses **127.0.0.1** et plus largement tout le bloc 127.0.0.0/8 servent au test interne : une requête envoyée à cette adresse ne quitte jamais la machine. Cela permet de vérifier localement qu’un service réseau répond bien.

Pour tirer pleinement parti de l’espace d’adressage, les administrateurs segmentent souvent leurs réseaux en **sous-réseaux** (_subnets_) grâce à des masques de sous-réseau ou à la notation **CIDR** (_Classless Inter-Domain Routing_), qui offre une gestion plus fine et réduit le gaspillage d’adresses. Le CIDR est aujourd’hui incontournable pour ajuster précisément la taille des plages IP et pour alléger les tables de routage.

Dans les réseaux modernes, l’adressage IP est souvent associé à d’autres identifiants : le **nom de domaine** enregistré dans un **DNS** (_Domain Name System_) permet d’associer une adresse IP à un nom plus facile à retenir ; l’**adresse MAC**, quant à elle, est un identifiant physique gravé dans la carte réseau, utilisé pour le transport au niveau local (_Ethernet_). Lorsqu’un paquet IP doit être transmis physiquement, c’est la table ARP qui fait la correspondance entre l’adresse IP et l’adresse MAC de destination.

Enfin, pour pallier la pénurie d’adresses IPv4 et améliorer la sécurité on peut recourir à la **traduction d’adresses** (_NAT_). Le NAT permet à plusieurs hôtes internes, utilisant des adresses privées, de partager une seule adresse IP publique pour sortir sur Internet.

**Remarque** : de nombreux outils en ligne et intégrés aux systèmes d’exploitation facilitent le calcul des masques, comme le [calculateur du CRIC de Grenoble](http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/). Ces utilitaires aident à planifier efficacement le découpage du réseau.

Pour conclure, l’adresse de diffusion reste une fonction pratique pour envoyer un même message à tous les équipements connectés à un segment : en pratique, la partie _HostID_ est mise à 1 pour signifier que tous les hôtes sont visés par le même paquet.

## Les différents types d’adresses IPv4
<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>

L’adressage IPv4 se divise principalement en deux grandes catégories : les adresses publiques, directement accessibles sur Internet, et les adresses privées, destinées à un usage interne dans un réseau local.

Une adresse IPv4 publique est une adresse unique au niveau mondial. Elle est enregistrée auprès d’un organisme officiel et est routable sur l’ensemble du réseau Internet. Les entreprises et organisations s’en servent pour rendre accessibles leurs services : serveurs web, infrastructures de messagerie, services de cloud public, etc. L’unicité mondiale de ces adresses est indispensable pour éviter tout conflit ou collision d’acheminement.

C’est l’**IANA** (_Internet Assigned Numbers Authority_), opérant sous l’égide de l’**ICANN** (_Internet Corporation for Assigned Names and Numbers_), qui gère la distribution de ces plages. Concrètement, l’IANA divise l’espace IPv4 en 256 blocs de taille /8, selon la notation CIDR. Chaque bloc représente un peu plus de 16,7 millions d’adresses (2³² / 2⁸).

Ces blocs d’adresses unicast sont confiés par l’IANA aux **Registres Internet Régionaux** (_Regional Internet Registries_ ou RIR). Ces RIR se chargent de redistribuer les adresses au niveau régional, en fonction des besoins réels des fournisseurs d’accès, des entreprises ou des administrations. L’espace d’adressage unicast s’étend des blocs **1/8 à 223/8**, avec des portions soit réservées pour des usages particuliers (recherche, documentation, tests), soit attribuées directement à un réseau final ou à un RIR pour redistribution.

Pour vérifier à qui appartient une adresse IP publique, il est possible de consulter les bases des RIR grâce à la commande **whois** ou en utilisant les interfaces web mises à disposition par chaque registre. Ces outils permettent de remonter à l’organisation ou au fournisseur ayant déclaré cette adresse.

À l’opposé, on trouve les adresses IPv4 privées, qui constituent une réponse pragmatique à la pénurie d’adresses publiques. Ces adresses, non routables sur Internet, sont réservées à des environnements locaux : réseaux d’entreprises, LAN domestiques, datacenters ou clusters de calcul. Elles ne sont pas uniques au niveau mondial : de nombreux réseaux privés peuvent réutiliser les mêmes plages sans interférence tant qu’ils restent isolés ou qu’ils passent par un dispositif de traduction d’adresses pour sortir sur Internet.

Pour qu’un équipement interne, configuré avec une adresse privée, puisse accéder au réseau global, on recourt au mécanisme de **NAT** (_Network Address Translation_). Le NAT joue un rôle important : il traduit l’adresse privée en adresse publique à la volée, ce qui permet à des dizaines, voire des centaines de postes internes de partager une seule adresse publique. Cette méthode optimise l’utilisation de l’espace IPv4 tout en ajoutant une couche de sécurité par dissimulation des topologies internes.

Par ailleurs, certaines adresses spéciales sont dites **non spécifiées**. La notation **0.0.0.0** ou sa version en IPv6 **::/128** indique l’absence d’adresse concrète : cette valeur est illégale comme adresse de destination sur le réseau, mais elle peut être utilisée localement par un hôte pour signifier "toutes les interfaces" ou "adresse non encore assignée". Ce mécanisme est couramment exploité lors de l’attribution dynamique par DHCP ou pour l’écoute sur toutes les interfaces d’un serveur.

En IPv6, comme nous le verrons dans la partie suivante, le principe d’adressage privé existe aussi, même si le standard recommande de privilégier l’adressage public pour éviter la multiplication des couches NAT. Les anciennes **adresses locales de site** (_site-local_) du bloc **fec0::/10** ont été déclarées obsolètes par le **RFC 3879**, pour des raisons de cohérence et de sécurité. Elles ont été remplacées par le concept d’**adresses locales uniques** (_ULA_), situées dans le bloc **fc00::/7**. Les ULA permettent de construire des réseaux privés IPv6 tout en assurant une interconnexion interne propre, grâce à un identifiant aléatoire sur 40 bits qui garantit l’unicité à l’échelle locale.

Face à la saturation de l’espace IPv4 (l’épuisement des blocs libres fut officiellement constaté en 2011) plusieurs stratégies ont vu le jour pour prolonger la viabilité du protocole. Parmi elles : la migration progressive vers **IPv6**, la généralisation du **NAT**, le durcissement des politiques d’allocation par les RIR (imposant une gestion plus fine et la justification des besoins) et, plus rarement, la récupération de blocs non utilisés ou rendus par des entreprises.

Ces différentes catégories et stratégies illustrent à quel point l’adressage IP est à la fois une problématique technique et une question de gouvernance mondiale, au cœur même de l’expansion continue d'Internet.


## Le DNS, un annuaire d’adresses
<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>

Il faut bien admettre que pour nous autres humains, mémoriser de longues suites de chiffres binaires ou décimaux n’est pas chose aisée. Cette difficulté devient encore plus marquée lorsque l’on considère la complexité de l’adressage IP et la multiplicité des adresses qu’une seule peut parfois masquer, notamment lorsqu’on emploie des mécanismes comme le NAT ou l’hébergement virtuel.

Pour pallier cette limite naturelle, la couche Application s’appuie sur un système capable de faire le lien entre une adresse IP et un nom logique plus compréhensible et surtout plus simple à manipuler. C’est précisément le rôle du **DNS**, pour *Domain Name System*, un immense annuaire hiérarchique et distribué qui associe des noms de domaine lisibles à des adresses IP. Ce système repose sur un ensemble de protocoles et de services, dont le plus connu est **BIND** (_Berkeley Internet Name Domain_), un logiciel libre servant de référence pour la majorité des serveurs DNS dans le monde.

Le principe fondamental du DNS est simple : pour tout équipement connecté (qu’il s’agisse d’un site web, d’un serveur de messagerie ou d’un service réseau) on enregistre une correspondance entre un nom de domaine et une ou plusieurs adresses IP. Cette correspondance est bidirectionnelle : on peut résoudre un nom en adresse (résolution directe) ou retrouver un nom à partir d’une adresse IP (résolution inverse). Cela rend l’adressage humainement exploitable tout en maintenant la précision technique indispensable pour le routage.

Un nom de domaine est toujours structuré hiérarchiquement, chaque niveau étant séparé par un point : le nom complet est appelé **FQDN** (_Fully Qualified Domain Name_). L’élément le plus à droite est le **TLD** (_Top Level Domain_) comme `.com`, `.org` ou `.fr`. L’élément le plus à gauche désigne l’hôte, c’est-à‑dire la machine spécifique à laquelle l’adresse IP est liée.

Le système DNS est conçu comme un **arbre de zones**. Chaque **zone** représente une portion de l’espace de noms, gérée par un serveur DNS spécifique. Une même zone peut inclure plusieurs **sous-domaines**, eux-mêmes potentiellement répartis sur d’autres zones administrées par des serveurs distincts. Une zone est donc l’unité administrative de base dont un administrateur est responsable : gestion, mises à jour, délégations éventuelles...

Ainsi, il devient possible non seulement de pointer vers un domaine principal (par exemple `example.com`) mais aussi de gérer finement chaque hôte (`www`, `mail`, `ftp`, etc.) par des enregistrements précis. À l’origine, cette fonction de résolution était assurée par de simples fichiers statiques (`/etc/hosts` sous Linux) mais cette méthode s’est vite révélée inadaptée pour un Internet mondial, évolutif et interconnecté.

Il est important de comprendre qu’un **serveur DNS** peut avoir un périmètre limité : un DNS interne à une entreprise, par exemple, peut ne pas être accessible directement depuis Internet. Si ce DNS n’est pas configuré pour déléguer les requêtes ou n’a pas de relation de confiance avec d’autres serveurs, certaines requêtes échoueront : ni le nom ni l’adresse IP ne pourront alors être résolus en dehors de la zone définie.

Un serveur DNS contient également des informations spécifiques au routage des courriels. Par exemple, un enregistrement de type **MX** (_Mail Exchange_) désigne les serveurs de messagerie responsables de recevoir les e-mails pour un domaine donné. Ces enregistrements définissent des priorités (facteur de pondération) et des solutions de basculement en cas de panne. Le fichier de zone d’un serveur DNS contient obligatoirement un enregistrement **SOA** (_Start Of Authority_), qui désigne le serveur comme source officielle de l’information pour la zone qu’il administre.

Le DNS, grâce à sa structure hiérarchique et distribuée, reste aujourd’hui une brique incontournable d'Internet, et permet à chaque utilisateur de se connecter à des services en utilisant des noms de domaine clairs au lieu de longues adresses IP techniques.

Dans le prochain chapitre, nous aborderons une autre notion fondamentale : les **adresses Ethernet**, également connues sous le nom d’**adresses MAC**, qui permettent d’assurer l’acheminement des données au niveau physique du réseau local.


## À la découverte de l’adresse Ethernet et d’ARP
<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>

### Définitions

Pour que le protocole d’acheminement des données puisse fonctionner de manière fiable et cohérente, une composante fondamentale reste indispensable. Si, en tant qu’êtres humains, nous savons facilement identifier une machine grâce à son adresse IP ou à son nom, récupéré via le DNS, une machine, quant à elle, doit pouvoir reconnaître sans ambiguïté l’équipement de destination pour transmettre les paquets. Pour cela, elle s’appuie sur un identifiant matériel spécifique, directement exploitable par son interface réseau : l’adresse MAC (_Media Access Control_).

Il convient de ne surtout pas confondre cette adresse MAC avec ce que l’on nomme l’adresse physique au sens de l’architecture mémoire. En effet, l’adresse physique, en informatique, désigne un emplacement précis dans le bus d’adresse de la mémoire centrale, et s’oppose à l’adresse virtuelle qui, elle, relève de la gestion de la mémoire par le système d’exploitation. L’adresse MAC, quant à elle, relève strictement du matériel réseau.

Attribuée de manière permanente et unique par le constructeur lors de la fabrication de l’équipement, l’adresse MAC identifie sans équivoque la carte réseau, qu’il s’agisse d’un ordinateur, d’un smartphone, d’une imprimante réseau ou de tout autre périphérique communicant. Contrairement à l’adresse IP, qui peut être dynamique et assignée par l’administrateur ou un serveur DHCP, l’adresse MAC reste, en principe, inchangée durant toute la vie du périphérique, sauf intervention volontaire.

Il est essentiel de rappeler que toute interface réseau, qu’elle soit câblée ou sans fil, possède une adresse MAC. Cette adresse est utilisée au sein de la couche liaison de données (couche 2 du modèle OSI) pour insérer et gérer l’adresse matérielle dans chaque trame réseau échangée. On parle parfois d’_adresse Ethernet_ ou encore d’_UAA_ (_Universally Administered Address_). Standardisée sur une longueur de 48 bits, soit 6 octets, elle s’écrit en notation hexadécimale, généralement sous la forme d’octets séparés par des `:` ou des `-`.

Par exemple : `5A:BC:17:A2:AF:15`

Dans cette structure, les trois premiers octets servent à identifier le fabricant de la carte réseau : c’est ce que l’on appelle l’**OUI** (*Organisationally Unique Identifier*). Ces préfixes, attribués par l’IEEE, sont réutilisés dans d’autres schémas d’adressage matériel, par exemple pour le Bluetooth ou le protocole LLDP, afin de garantir l’unicité mondiale des identifiants.


### Modification de l’adresse MAC

En théorie, l’adresse MAC est conçue pour rester fixe, mais il existe des méthodes pour la modifier, notamment pour répondre à des besoins particuliers ou contourner certaines contraintes. Cette opération, que l’on appelle souvent _spoofing MAC_, consiste à remplacer l’adresse matérielle d’origine par une valeur différente, définie au niveau logiciel. Certains systèmes d’exploitation facilitent cette modification, notamment lorsque l’adresse Ethernet réelle n’est pas exploitée directement par le pilote.

Les motifs pouvant conduire à un tel changement sont variés. Il peut s’agir de la nécessité pour une application donnée d’exiger une adresse Ethernet spécifique pour fonctionner correctement, ou de résoudre un conflit d’adresses identiques entre deux équipements partageant le même réseau local.

Changer l’adresse MAC peut également être motivé par des considérations de confidentialité : en masquant l’identifiant unique gravé dans la carte, l’utilisateur réduit ainsi les possibilités de traçage de son appareil par des réseaux ou des services de surveillance. Toutefois, cette pratique n’est pas sans conséquences. Modifier une adresse MAC peut perturber certains dispositifs de filtrage ou nécessiter de reconfigurer les pare-feu pour autoriser le nouveau matériel.

Dans certains réseaux, notamment dans le cadre de la sécurisation des accès Wi-Fi, il est fréquent de recourir au filtrage d’adresses MAC pour restreindre l’accès aux seuls équipements préalablement autorisés. Bien que cette technique puisse apporter un premier niveau de contrôle, elle présente une efficacité limitée. Des attaquants peuvent facilement capturer une adresse MAC valide autorisée sur le réseau, la forger et l’utiliser à leur profit pour contourner la restriction, ce qui rend ce type de filtrage insuffisant s’il n’est pas couplé à d’autres mesures de sécurité plus robustes.
### Correspondance MAC/IP

Pour qu’un réseau local fonctionne de manière fluide et cohérente, il est indispensable d’établir un lien clair entre les adresses physiques, comme les adresses MAC, et les adresses logiques, c’est-à‑dire les adresses IP. Sans cette correspondance, un ordinateur saurait certes vers quelle adresse IP envoyer un paquet, mais serait incapable de savoir comment le transmettre concrètement sur le réseau physique. C’est là qu’intervient le protocole ARP (_Address Resolution Protocol_), qui automatise ce mécanisme.

Dans la pratique, lorsqu’un utilisateur souhaite connaître l’adresse MAC correspondant à une adresse IP précise, il peut s’appuyer sur l’utilitaire `arp`. Cet outil interroge la table ARP locale de la machine pour afficher les correspondances déjà connues entre adresses IP et adresses MAC sur le réseau local. Il est ainsi possible de vérifier rapidement la liaison effective entre les couches logiques et physiques.

Exemple pratique : si l’on veut vérifier quelle carte réseau correspond à l’adresse IP `192.168.1.5`, on utilisera la commande suivante :

```bash
arp –a 192.168.1.5
```

La sortie affichera notamment l’adresse physique (MAC) associée, la nature de l’entrée (statique ou dynamique) et l’interface concernée.

```
Interface : 192.168.1.5 --- 0x5
    IP Address            MAC Address                Type
    192.168.1.5           00:54:BC:17:14:6E          D
```

Il est donc important de garder à l’esprit que l’adresse MAC et l’adresse IP sont deux identifiants totalement distincts mais étroitement complémentaires. L’adresse MAC est gravée de façon unique par le constructeur dans chaque interface réseau et sert à identifier physiquement l’équipement sur le réseau local. L’adresse IP, quant à elle, est une adresse logique attribuée dynamiquement ou statiquement pour permettre à la machine de s’intégrer au réseau IP et d’échanger des paquets au-delà de son réseau local.

- Exemple visuel d’adresse MAC :

![Image](assets/fr/032.webp)

- Exemple visuel d’adresse IP :

![Image](assets/fr/027.webp)

Dans un environnement d’entreprise, ces deux niveaux d’adressage ne peuvent fonctionner séparément. Par exemple, lors de l’attribution automatique d’une adresse IP par un serveur DHCP, c’est l’adresse MAC de l’équipement qui sert de point de départ. L’ordinateur envoie une requête DHCP en broadcast, incluant son adresse MAC, afin de se voir attribuer une adresse IP disponible par le serveur. Sans cette identification matérielle, le serveur DHCP ne saurait pas à quel appareil délivrer l’adresse.

Le protocole ARP est donc fondamental : il assure la liaison entre les adresses IP et les adresses physiques, et permet donc aux machines de traduire une destination logique en une destination matérielle réelle. Lorsqu’un ordinateur doit envoyer un paquet à une machine du même réseau, il consulte d’abord sa table ARP pour vérifier si l’adresse MAC du destinataire est déjà connue. Si ce n’est pas le cas, il diffuse une requête ARP à tous les hôtes du réseau local. La machine qui reconnaît l’adresse IP cible dans cette requête répond en précisant son adresse MAC. L’émetteur inscrit alors ce couple IP/MAC dans son cache ARP pour éviter d’avoir à répéter l’opération à chaque envoi.

Cette table ARP agit donc comme un mini-annuaire de correspondance, mis à jour dynamiquement, un peu comme le DNS le fait pour associer des noms de domaine à des adresses IP. Sans ARP, aucun échange local ne serait possible car la couche liaison de données doit impérativement connaître l’adresse MAC pour encapsuler correctement les trames Ethernet.

À l’inverse, le protocole RARP (_Reverse Address Resolution Protocol_) a été conçu pour résoudre la situation opposée : permettre à une machine qui ne connaît que son adresse MAC de découvrir son adresse IP. C’était notamment le cas pour les anciennes stations de travail sans disque dur local, qui devaient démarrer via le réseau et réclamer une adresse IP. Il a toutefois été rapidement supplanté par **BOOTP**, puis par **DHCP**, des solutions plus souples et automatisées.

Ces protocoles d’association jouent un rôle important dans le routage. Un routeur est en réalité une machine dotée de plusieurs interfaces réseau, reliant différents segments. Quand un routeur reçoit une trame, il la traite pour extraire le datagramme IP, puis examine l’entête IP pour déterminer la destination. Si la destination se trouve sur un réseau directement connecté, le datagramme est remis en remise directe après mise à jour de l’entête. Si la destination appartient à un autre réseau, le routeur consulte sa table de routage pour identifier le meilleur chemin, ou _next hop_, vers la destination.

Ce fonctionnement permet de diviser le trajet en segments plus courts et gérables. Chaque routeur intermédiaire ne connait que la prochaine étape, pas forcément la destination finale.

**Rappel :** on parle de remise directe quand l’expéditeur et le destinataire sont sur le même réseau physique ; sinon, la remise est dite indirecte car elle transite par un ou plusieurs routeurs.

La table de routage, administrée soit manuellement (routage statique), soit dynamiquement (routage dynamique), contient les informations nécessaires pour décider du chemin à emprunter. Dans les petits réseaux, une configuration statique est suffisante, mais dans les grandes infrastructures, le routage dynamique s’impose pour ajuster automatiquement les routes en fonction des changements de topologie ou d’état des liens.

La table de routage agit comme un tableau de correspondance entre les adresses IP cibles et les passerelles suivantes. Elle ne conserve généralement pas toutes les adresses hôtes mais seulement l’identifiant du réseau (_network ID_), ce qui allège considérablement son volume.

| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Grâce à ces entrées, le routeur peut déterminer rapidement via quelle interface et vers quel nœud il doit transmettre chaque datagramme. Cette logique d’acheminement, combinée au protocole ARP pour résoudre les adresses MAC correspondantes, garantit l’efficacité et la fiabilité du transfert de données sur l’ensemble du réseau.

Enfin, parmi les protocoles de routage dynamiques, on retrouve des standards comme RIP (_Routing Information Protocol_), basé sur l’algorithme de distance, et OSPF (_Open Shortest Path First_), qui calcule les chemins les plus courts à travers une topologie complexe. Ces protocoles s’échangent en permanence des informations de mise à jour pour optimiser les chemins, réduire les coûts de transmission et améliorer la résilience du réseau face aux pannes ou aux congestions.

## NAT : Traduction d’adresse
<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>

### Définition

Le _Network Address Translation_ (NAT) est une technique qui a vu le jour pour pallier l’épuisement progressif du stock d’adresses IPv4 disponibles. Conçu comme un mécanisme intermédiaire avant la généralisation d’IPv6, le NAT a permis aux entreprises et aux particuliers de continuer à connecter un grand nombre de machines tout en utilisant un nombre restreint d’adresses IP publiques.

**Rappel important :** le passage d’IPv4 à IPv6 permet théoriquement de résoudre ce problème d’épuisement puisque l’espace d’adressage passe de 32 bits à 128 bits, ce qui offre ainsi un nombre d’adresses quasi illimité (2^128). Toutefois, en pratique, la transition reste partielle et le NAT demeure aujourd’hui encore très répandu.

Le principe du NAT repose sur un fonctionnement simple mais particulièrement efficace : au lieu d’attribuer une adresse IP publique unique à chaque machine du réseau interne, on utilise une seule adresse routable (ou un petit pool d'adresses) pour l’ensemble des terminaux privés. La passerelle NAT, souvent intégrée au routeur ou au pare-feu, se charge alors de traduire dynamiquement l’adresse IP interne et les informations nécessaires pour acheminer correctement le trafic vers l’extérieur, puis d’assurer le retour des réponses vers la machine émettrice.

Ce procédé présente un avantage immédiat : il masque totalement l’architecture interne du réseau. Pour un observateur externe, toutes les requêtes émises par les postes de travail, serveurs ou imprimantes partagent la même identité publique. L’adressage privé, généralement constitué d’adresses IP issues des plages réservées (par exemple 192.168.x.x ou 10.x.x.x), reste donc invisible depuis Internet.

En plus de répondre à la pénurie d’adresses IPv4, le NAT renforce donc la sécurité en créant une première barrière logique entre le réseau interne et le réseau public. Les communications entrantes non sollicitées sont ainsi naturellement filtrées, car seules les connexions initiées depuis l’intérieur bénéficient de la traduction nécessaire pour recevoir les réponses.

![Image](assets/fr/035.webp)

### Types de traduction

Le NAT peut être mis en œuvre sous différentes formes, adaptées à des besoins spécifiques. On distingue principalement deux grands modes de fonctionnement : la traduction statique et la traduction dynamique.

**La traduction statique** consiste à établir une correspondance fixe entre une adresse IP privée et une adresse IP publique. Chaque machine interne dispose alors d’une adresse publique dédiée qui lui est associée de manière permanente. Par exemple, une machine interne configurée en 192.168.20.1 peut être associée à l’adresse routable 157.54.130.1. Lorsqu’un paquet sortant quitte le réseau local, le routeur modifie l’adresse source du paquet pour lui substituer l’adresse publique, et effectue l’opération inverse pour le trafic entrant. Cette traduction bidirectionnelle est transparente pour l’utilisateur.

**Attention :** si ce mécanisme permet d’isoler le réseau interne, il ne résout en rien le problème de pénurie d’adresses IP publiques, car il faut toujours autant d’adresses publiques que de machines à exposer. La traduction statique est donc surtout utilisée lorsque certaines ressources internes doivent impérativement rester joignables depuis l’extérieur (serveur web, serveur mail…).

La traduction dynamique, quant à elle, met à disposition un pool d’adresses IP publiques. Lorsqu’un hôte interne initie une connexion, le routeur sélectionne provisoirement l’une de ces adresses et l’associe à l’adresse privée de l’hôte pour toute la durée de la session. Le lien est 1-vers-1, mais temporaire : dès que le flux s’interrompt, l’adresse publique redevient disponible pour un autre poste. Le Dynamic NAT économise donc le nombre d’adresses publiques quand toutes les machines n’ont pas besoin d’être connectées en même temps, mais il requiert tout de même un bloc d’adresses externes de taille au moins égale au nombre maximal de connexions simultanées.

La traduction de ports (PAT), appelée aussi *NAT overload* ou *IP masquerading*, va plus loin : toutes les machines privées partagent une seule adresse IP publique (ou un très petit nombre). Pour différencier les sessions, la passerelle modifie non seulement l’adresse source mais aussi le port source. Elle maintient alors une table qui associe chaque couple *(adresse privée, port privé)* à un couple *(adresse publique, port public)* unique. C’est cette forme de NAT qui équipe la quasi-totalité des box et routeurs domestiques, car il permet à des dizaines de terminaux (ordinateurs, smartphones, objets connectés...) de partager la même adresse IP publique, tout en maintenant une communication fluide.

Le NAT prolonge donc la durée de vie d’IPv4 tout en ajoutant un niveau de cloisonnement et de sécurité appréciable. Toutefois, avec l’adoption progressive d’IPv6 et son espace d’adressage immense, le rôle du NAT tendra à se réduire, même si, pour des raisons de compatibilité et de contrôle, il restera encore utilisé dans certains environnements pour segmenter et filtrer les flux.

### Implémentation du NAT

Pour garantir le fonctionnement correct du mécanisme de traduction d’adresses, le routeur ou la passerelle NAT doit conserver une trace précise des correspondances établies entre chaque adresse privée du réseau interne et l’adresse publique qu’elle utilise pour communiquer vers l’extérieur. Ces informations sont stockées dans une table dite de "traduction NAT", qui joue un rôle central dans la gestion des flux réseau.

Chaque entrée de cette table associe au minimum une paire composée de l’adresse IP interne de la machine émettrice et de l’adresse IP externe qui sera exposée sur Internet. Lorsque qu’un paquet issu du réseau privé est émis vers une destination publique, le routeur NAT intercepte la trame, analyse l’entête IP et TCP/UDP, puis remplace l’adresse source privée par l’adresse publique de la passerelle. Dans le sens retour, le paquet entrant est capturé par la même passerelle, qui vérifie la table de correspondance et effectue l’opération inverse pour rediriger le flux vers l’adresse IP interne initiale.

Ce principe de traduction dynamique repose sur une gestion fine de la table : chaque entrée reste valide tant qu’un trafic actif la justifie. Après un délai d’inactivité paramétrable, l’entrée est purgée et peut être réutilisée pour de nouvelles connexions.

_Exemple de table de traduction NAT simplifiée :_

| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

Dans cet exemple, si aucun paquet n’a transité pour la seconde ligne depuis plus d’une heure (3600 secondes), l’entrée est marquée comme réutilisable. À l’inverse, un champ de durée à zéro indique qu’une communication est en cours et que la correspondance est verrouillée.

Bien que le NAT s’intègre de manière transparente pour la majorité des usages courants (navigation web, courrier électronique, transfert de fichiers...) il peut cependant introduire des contraintes supplémentaires pour certaines applications réseau. En effet, certaines technologies reposent sur l’échange explicite d’adresses IP ou de ports dans le corps même des paquets. Or, ces informations deviennent incohérentes après passage par la passerelle NAT.

Parmi les cas les plus typiques de limitations, on peut citer :
- Les protocoles de type pair-à-pair (P2P), qui nécessitent l’établissement de connexions directes entre postes, sont perturbés par la barrière du NAT, car chaque machine interne partage la même adresse IP externe et ne peut être contactée directement sans configuration spécifique (comme le *port forwarding* ou l’UPnP) ;
- Le protocole IPSec, utilisé pour sécuriser les communications réseau, chiffre l’entête des paquets. Or, comme le NAT a besoin de modifier ces entêtes pour remplacer les adresses IP, le chiffrement rend impossible cette modification, ce qui compromet la compatibilité sans mise en place de mécanismes d’adaptation comme le NAT-T (*NAT Traversal*) ;
- Le protocole X Window, qui permet l’affichage distant d’applications graphiques sous Unix/Linux, fonctionne selon une logique où le serveur X envoie activement des connexions TCP vers les clients. Cette inversion du sens habituel des connexions peut être bloquée par la traduction NAT.

De manière générale, tout protocole intégrant une référence explicite à l’adresse IP interne dans la charge utile du paquet sera affecté, car cette adresse ne correspond plus à l’adresse réelle visible depuis Internet une fois la traduction effectuée.

**Remarque importante :** pour pallier ces problèmes, certains routeurs NAT disposent de fonctionnalités de _Deep Packet Inspection_ (DPI) ou de _Protocol Helpers_, qui inspectent le contenu des paquets pour identifier et remplacer dynamiquement les adresses ou numéros de ports inscrits dans les données applicatives. Cette manipulation nécessite toutefois une parfaite connaissance du format du protocole à traiter et peut représenter une vulnérabilité ou un surcoût en ressources.

**Point de vigilance :** le NAT contribue certes à masquer le réseau interne et à contrôler la circulation des flux entrants, mais il ne remplace en aucun cas un pare-feu dédié. La traduction ne constitue pas une barrière de sécurité complète : elle doit toujours être complétée par des règles de filtrage précises pour bloquer le trafic non sollicité ou indésirable.

_Pour illustrer le fonctionnement concret, prenons l’exemple suivant :_

![Image](assets/fr/037.webp)

Dans ce scénario, un poste interne peut accéder au serveur web interne en appelant directement l’URL `http://192.168.1.20:80`. Ici, l’indication du port est optionnelle puisque `80` est le port standard pour le HTTP. À l’inverse, si une requête est initiée depuis l’extérieur, l’utilisateur saisira l’adresse publique `http://85.152.44.14:80`. Le routeur NAT réceptionne la requête, consulte sa table de correspondance et traduit automatiquement l’adresse publique en adresse privée, redirigeant la connexion vers `http://192.168.1.20:80`.

Ce principe est identique pour tout autre serveur autorisé à recevoir des connexions depuis Internet, comme le serveur Extranet (circuit bleu sur le schéma).

**Remarque pratique :** dans les environnements virtualisés, on rencontre fréquemment des interfaces réseau appelées _virbrX_ (pour _Virtual Bridge X_). Ces ponts virtuels, fournis notamment par la bibliothèque libvirt ou l’hyperviseur Xen, servent à relier le réseau interne virtuel des machines invitées au réseau physique, tout en appliquant le NAT. Leur configuration se réalise généralement via des scripts situés dans `/etc/sysconfig/network-scripts/`, comme illustré ci-dessous pour `virbr0` :

```ini
NAME=""
BOOTPROTO=none
MACADDR=""
TYPE=Bridge
DEVICE=virbr0
NETMASK=255.255.255.0
MTU=""
BROADCAST=192.168.0.255
IPADDR=192.168.0.1
NETWORK=192.168.0.0
ONBOOT=yes
```

Une fois le pont virtuel en place, il est nécessaire d’activer le routage IP et de configurer la traduction de ports avec `iptables` :

```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```

```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```

Grâce à cette configuration, le trafic sortant est routé et la traduction NAT est assurée pour permettre aux machines virtuelles de communiquer avec l’extérieur sans exposer directement leurs adresses IP internes.

Dans le chapitre suivant, nous aborderons en détail la configuration des adresses IP sous Linux, à travers des méthodes simples et avancées adaptées à différents contextes d’administration.

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Comment configurer le réseau avec `ip` ?
<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>

### Configuration standard

Après avoir posé les bases théoriques du réseau et compris comment s’articulent adresses IP, masques, routage et traduction, il est temps de passer à la pratique. Sous GNU/Linux, la configuration réseau se fait aujourd’hui avec la commande **`ip`** (paquet _iproute2_), qui remplace l’historique `ifconfig`.

Véritable couteau suisse, `ip` permet d’attribuer ou de modifier une adresse IP, de changer un masque, de démarrer ou d’arrêter une interface, ou encore de consulter son état à tout moment.

**ASTUCE :** pour visualiser toutes les interfaces (actives ou non) :  `ip addr show`

Exemple concret : attribution d’une adresse statique et activation de l’interface

Ajouter l’adresse `192.168.1.2/24` à l’interface `eth0` :

```shell
ip addr add 192.168.1.2/24 dev eth0
```

Activer l’interface :

```shell
ip link set dev eth0 up
```

Pour désactiver la même interface :

```shell
ip link set dev eth0 down
```

Pour afficher l’état d’une interface précise :

```shell
ip addr show dev eth2
```

**Astuce pratique :** avec `ip`, l’ajout d’une adresse supplémentaire sur une interface ne requiert plus de suffixe `:1`. Il suffit d’ajouter une seconde ligne `ip addr add …` :

```shell
ip addr add 172.18.2.39/24 dev eth2
```

### Scripts d’activation : ifup / ifdown

Les utilitaires `ifup` et `ifdown` lisent les fichiers statiques de `/etc/sysconfig/network-scripts/` (sur RHEL, CentOS, Rocky Linux, AlmaLinux…) ou `/etc/network/interfaces` (sur Debian/Ubuntu) afin d'activer ou de désactiver proprement les interfaces.

```shell
ifup eth1
ifdown eth2
```

Fichiers de configuration (RHEL-like) :
- **/etc/sysconfig/network** : paramètres globaux (NETWORKING, HOSTNAME, GATEWAY…).
- **ifcfg-*** : paramètres spécifiques à chaque interface.

Exemple statique (ifcfg-eth0) :

```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```

Exemple DHCP :

```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```

Cette structuration modulaire reste valable et facilement automatisable sur les systèmes actuels.

### Configuration avancée : le bonding

Dans les environnements professionnels, on cherche à garantir la continuité de service et/ou à agréger la bande passante. Les mécanismes de *bonding* (ou *teaming* avec _teamd_) répondent à ces besoins : plusieurs interfaces physiques fonctionnent comme une seule interface logique, souvent nommée `bond0` ou `team0`.

![Image](assets/fr/039.webp)

Prérequis :
- Charger le module `bonding` (ou utiliser `teamd`) ;
- Disposer d’au moins deux interfaces physiques.

#### Les différents modes de bonding courants :

|Mode|Nom|Principe|
|---|---|---|
|0|balance-rr|Round-robin, répartition circulaire des trames|
|1|active-backup|Une seule interface active, bascule à chaud|
|2|balance-xor|Sélection via XOR MAC src/dst|
|3|broadcast|Diffusion simultanée sur toutes les interfaces|
|4|802.3ad (LACP)|Agrégation dynamique normalisée, nécessite switch compatible|
|5|tlb (Transmit Load Balancing)|Répartition selon la charge d’émission|
|6|alb (Adaptive Load Balancing)|Répartition adaptative, équilibre aussi la réception via ARP|


#### Mise en place avec `ip link`

- Désactiver les interfaces physiques :

```shell
ip link set eth0 down
ip link set eth1 down
```

- Créer l’interface bondée :

```shell
ip link add bond0 type bond mode balance-alb
```

- Configuration des options après création

```shell
ip link set bond0 type bond miimon 100
```

- Attribuer adresse MAC et IP :

```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```

- Attacher les interfaces esclaves :

```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```

- Remettre tout en service :

```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```

**Astuce :** pour détacher un esclave sans couper le bond :  `ip link set eth1 nomaster`

#### Configuration permanente (RHEL-like)

Créer trois fichiers dans `/etc/sysconfig/network-scripts` :

_ifcfg-bond0_

```ini
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.2.3
NETMASK=255.255.255.0
BROADCAST=192.168.2.255
GATEWAY=192.168.2.1
BONDING_OPTS="mode=balance-alb miimon=100"
```

_ifcfg-eth0_

```ini
DEVICE=eth0
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```

_ifcfg-eth1_

```ini
DEVICE=eth1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```

Puis :

```shell
systemctl restart network
```

#### Adresse IP supplémentaire (alias moderne)

Avec `ip`, il suffit d’ajouter une seconde adresse sur le même périphérique :

```shell
ip addr add 192.168.1.2/24 dev eth0
```

Pour que cet alias survive au redémarrage, créez un deuxième bloc `IPADDR2=…` / `PREFIX2=…` dans `ifcfg-eth0`, ou une nouvelle connexion *NetworkManager* via `nmcli`.

Grâce à `ip` et aux commandes connexes (`ip link`, `ip addr`, `ip route`), la configuration réseau gagne en cohérence, en scriptabilité et en clarté. Le bonding est un pilier des architectures haute disponibilité et l’ajout d’adresses multiples par interface se simplifie nettement.

Dans la suite de ce cours, nous aborderons les particularités et la mise en œuvre de l’adressage IPv6.


# L’adressage IPv6
<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>

## IPv6 : Normes et définitions
<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>

Nous abordons à présent la nouvelle génération d’adressage IP : le protocole IPv6, initialement désigné sous le nom d’IPng (_IP Next Generation_). Conçu pour surmonter les limites structurelles d’IPv4, ce protocole introduit une architecture d’adressage largement étendue, ainsi que de nombreuses optimisations techniques.

Les motivations qui ont conduit à l’adoption d’IPv6 sont multiples et répondent à des besoins critiques pour l’évolution d’Internet. Tout d’abord, IPv6 devait permettre de supporter la croissance exponentielle du nombre d’équipements connectés (un objectif inatteignable avec l’espace d’adressage limité d’IPv4). Ensuite, le protocole vise à réduire la taille des tables de routage, ce qui contribue à rendre les échanges plus efficaces et allège le travail des routeurs sur le long terme.

IPv6 ambitionne également de simplifier certains aspects du traitement des paquets, afin de fluidifier la circulation des datagrammes et d’optimiser la vitesse de transfert entre les réseaux. Du point de vue de la sécurité, les en-têtes AH/ESP du protocole *IPsec* font partie du jeu de base, et tous les nœuds IPv6 doivent pouvoir les prendre en charge (RFC 6434). Leur usage reste toutefois optionnel : l’administrateur décide de les activer ou non selon le contexte.

Parmi les autres objectifs, on note une prise en compte plus fine des types de services, notamment pour garantir une meilleure qualité pour les applications temps réel (voix sur IP, visioconférence...). IPv6 doit également permettre une gestion plus souple de la mobilité : un appareil peut ainsi changer de point d’accès sans changer d’adresse de manière visible pour ses correspondants.

Enfin, IPv6 a été conçu pour coexister avec les protocoles historiques. S’il n’est pas directement compatible avec IPv4 sur le plan binaire, il reste parfaitement interopérable avec les couches supérieures comme TCP, UDP, ICMPv6, DNS, ainsi qu’avec les protocoles de routage tels qu’OSPF ou BGP, moyennant certains ajustements. Pour la gestion du multicast, IPv6 emploie le protocole MLD (*Multicast Listener Discovery*), l’équivalent fonctionnel d’IGMP en environnement IPv4.

### Règles d’écriture

L’un des changements majeurs avec IPv6 est le format même de l’adresse IP. Pour résoudre la pénurie chronique d’adresses IPv4, la longueur de l’adresse a été portée à 128 bits, soit 16 octets, contre seulement 32 bits pour IPv4. En théorie, cela ouvre un champ d'adresses possibles de :

$$3.4 \times 10^{38}$$

Cela garantit ainsi une capacité quasi illimitée pour accueillir tous les équipements actuels et futurs.

L’écriture des adresses IPv6 diffère notablement de la notation décimale pointée classique. Une adresse IPv6 se compose de huit groupes de 16 bits, exprimés en hexadécimal et séparés par des deux-points `:`.

Par exemple :

```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```

Pour alléger cette écriture, les zéros en tête de chaque groupe peuvent être omis. L’exemple précédent devient alors :

```
1987:c02:0:84c2:0:0:cf2a:9077
```

De plus, une seule séquence continue de groupes de zéros peut être remplacée par la notation `::`, ce qui permet de condenser l’adresse :

```
1987:c02:0:84c2::cf2a:9077
```

**Attention :** la règle est stricte : une seule et unique séquence de zéros consécutifs peut être abrégée par `::`. Si une adresse comporte plusieurs suites de zéros, seule la plus longue est condensée. C’est ce principe qui garantit l’unicité et la lisibilité de l’adresse.

**Particularité importante :** le caractère `:` utilisé pour séparer les blocs hexadécimaux pose un problème potentiel dans les URL, car `:` sert également à indiquer le port du service. Pour lever toute ambiguïté, les adresses IPv6 insérées dans une URL doivent obligatoirement être encadrées par des crochets `[ ]`.

Exemple d’accès HTTP sur un port spécifique pour l’adresse `2002:400:2A41:378::34A2:36` :

```
http://[2002:400:2A41:378::34A2:36]:8080
```

Lorsque l’on souhaite exprimer une adresse IPv4 dans un contexte IPv6, on peut employer une notation mixte en décimal pointé, précédée de la chaîne `::` :

```
::192.168.1.5
```

Cette compatibilité facilite la transition entre les deux protocoles en permettant d’inclure des blocs IPv4 dans l’espace IPv6.

**Note :** pour uniformiser les représentations, la RFC 5952 définit un format canonique qui précise les règles d’abréviation à suivre pour éviter les variantes multiples d’une même adresse. Bien respecter ces recommandations contribue à limiter les erreurs d’interprétation et à garantir la cohérence des configurations réseau.

### Les types d’adresses IPv6

L’adressage IPv6 se distingue de son prédécesseur par une grande diversité de catégories d’adresses, chacune conçue pour répondre à des usages précis, tout en garantissant une flexibilité d’acheminement et de gestion du réseau. Comme en IPv4, on y retrouve des adresses globales, locales, réservées ou spécifiques à certains mécanismes de transition.

Une adresse IPv6 non spécifiée est représentée par `::` ou, sous forme plus explicite, `::0.0.0.0`. Cette forme particulière sert notamment lors de l’acquisition d’une adresse ou comme valeur par défaut pour indiquer l’absence d’adresse.

| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
| ::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1) : *Sur un réseau local privé, on privilégie le préfixe `fd00::/8` pour affecter des adresses internes non routables sur Internet.*

#### Adresses réservées

Certaines plages IPv6 sont explicitement réservées et ne doivent pas être utilisées comme adresses globales. Elles ont un rôle technique bien défini :

- **`::/128`** : adresse non spécifiée, jamais attribuée à un équipement de façon persistante, mais utilisée comme adresse source par une machine en attente de configuration.
- **`::1/128`** : l’adresse de _loopback_, équivalent direct de `127.0.0.1` en IPv4, qui permet à une machine de s’adresser à elle-même.
- **`64:ff9b::/96`** : bloc réservé aux traducteurs de protocoles pour l’interconnexion IPv4/IPv6, tel que défini dans la RFC6052.
- **`::ffff:0:0/96`** : bloc de compatibilité pour représenter une adresse IPv4 dans une structure IPv6 spécifique, souvent utilisé en interne par les applications.

Ces blocs garantissent l’interopérabilité et facilitent la migration entre les deux versions du protocole.

#### Adresses globales unicast

Les adresses globales unicast constituent l’essentiel de l’espace IPv6 routable publiquement. Elles représentent environ 1/8ème de l’espace d’adressage. Depuis 1999, l’IANA attribue ces blocs, tels que le préfixe `2001::/16`, par blocs CIDR (de `/23` à `/12`) aux registres régionaux, qui les redistribuent ensuite aux fournisseurs et aux organisations.

Certaines plages ont des usages documentés particuliers :

- **`2001:2::/48`** : réservée aux tests de performance et d’interopérabilité, RFC5180.
- **`2001:db8::/32`** : réservée à la documentation et aux exemples, RFC3849.
- **`2002::/16`** : utilisée pour le mécanisme 6to4, qui permet de transporter du trafic IPv6 à travers une infrastructure IPv4 (important pour la phase de transition entre les deux protocoles).

**À noter :** une large part des adresses globales reste encore inexploitée et constitue une réserve pour les extensions futures d'Internet.

#### Adresses locales uniques (ULA)

Les adresses locales uniques (`fc00::/7`) sont l’équivalent IPv6 des adresses privées IPv4 (RFC1918). Elles permettent de créer des réseaux internes isolés sans risque de conflit avec l’adressage public. Dans la pratique, le préfixe effectif est `fd00::/8`, le 8ème bit étant fixé à 1 pour définir l’usage local. Chaque bloc ULA intègre un identifiant pseudo-aléatoire de 40 bits, ce qui minimise ainsi les collisions d’adresses en cas d’interconnexion de réseaux privés distincts.

#### Adresses locales de lien (Link-local)

Les adresses link-local (`fe80::/64`) servent exclusivement aux communications internes sur un même segment de niveau 2 (même VLAN ou switch). Elles ne sont jamais routées au-delà du lien local. Chaque interface réseau génère automatiquement une adresse link-local, souvent dérivée de son adresse MAC via le schéma EUI-64.

Particularité : une même machine peut utiliser la même adresse link-local sur plusieurs interfaces, à condition de préciser l’interface lors des communications pour éviter toute ambiguïté.

#### Adresses multicast

En IPv6, le concept de broadcast disparaît au profit du multicast, plus efficace pour diffuser des paquets à un groupe de destinataires définis. La plage multicast est préfixée par `ff00::/8`. Parmi ces adresses, on trouve par exemple `ff02::1`, qui cible tous les nœuds du lien local. Bien que pratique, cette adresse est désormais déconseillée pour les applications, car elle peut générer des diffusions non contrôlées.

Un usage fréquent du multicast concerne le _Neighbor Discovery Protocol_ (NDP), qui remplace ARP en IPv6. NDP s’appuie sur des adresses multicast spécifiques, comme `ff02::1:ff00:0/104`, pour découvrir automatiquement les autres hôtes connectés au même lien.

En combinant ces types d’adresses, IPv6 offre une palette complète pour répondre aux besoins de routage global, de communications locales, de migration IPv4/IPv6 et d’autoconfiguration des équipements tout en améliorant l’efficacité des transmissions réseau.

### Périmètre des adresses

La portée d’une adresse IPv6 (*scope*), définit précisément le domaine dans lequel cette adresse est considérée comme valide et unique. Comprendre cette notion est important pour maîtriser l’acheminement des paquets et l’organisation logique d’un réseau fonctionnant en IPv6. On regroupe généralement les adresses IPv6 en trois grandes catégories selon leur périmètre et leur mode d’utilisation : unicast, anycast et multicast.

Les **adresses unicast** constituent la catégorie la plus courante et englobent plusieurs sous-types bien distincts. Elles regroupent notamment l’adresse _loopback_ (`::1`), dont la portée est strictement limitée à l’hôte qui l’utilise, et qui permet de tester la pile réseau en interne sans émettre de trafic sur le réseau physique. À cela s’ajoutent les adresses locales de lien (_link-local_) dont la portée est restreinte à un segment de réseau unique : elles servent aux communications directes entre équipements situés sur le même lien physique ou logique (par exemple un switch ou un VLAN unique). Enfin, les adresses locales uniques (_ULA_, pour _Unique Local Addresses_) correspondent à des plages d’adresses internes à un réseau d’entreprise ; elles ont une portée potentiellement plus large car elles peuvent être routées à travers plusieurs segments privés mais ne sont jamais visibles sur Internet.

Ce découpage conceptuel se matérialise souvent par une structure binaire où la première partie de l’adresse (les 64 premiers bits) identifie le préfixe réseau et la seconde moitié (64 bits également) identifie de façon unique l’interface de l’équipement sur ce réseau. Cette séparation facilite l’autoconfiguration des adresses grâce aux mécanismes comme SLAAC (_Stateless Address Autoconfiguration_), qui permettent aux machines de générer automatiquement une adresse stable basée sur l’adresse MAC ou un identifiant pseudo-aléatoire.

| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

L’architecture IPv6 reprend le modèle hiérarchique du routage global de l’Internet actuel : le découpage des préfixes permet aux registres régionaux et aux opérateurs de gérer la distribution d’adresses de façon décentralisée, tout en assurant l’unicité globale. C’est dans ce cadre qu’un même hôte peut posséder simultanément une adresse unicast globale, pour communiquer sur Internet, et une adresse link-local pour interagir localement, par exemple pour le voisinage immédiat ou les messages de découverte de routeur.

| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

Les **adresses anycast** représentent une notion intermédiaire qui tire parti du modèle unicast tout en offrant un comportement proche du multicast dans certains cas. Une adresse anycast est, en réalité, une adresse unicast affectée à plusieurs interfaces réparties sur différents nœuds du réseau. Lorsqu’un paquet est émis vers une adresse anycast, le protocole IPv6 s’efforce de le livrer à l’un des hôtes partageant cette adresse, en privilégiant généralement celui qui est le plus proche selon la topologie du routage. Ce principe optimise la rapidité de traitement des requêtes et améliore la résilience des services distribués : l’exemple typique est celui des serveurs DNS racine, pour lesquels l’adressage anycast permet de diriger automatiquement les requêtes vers le point de présence le plus proche.

| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

Enfin, les **adresses multicast** remplacent dans IPv6 le mécanisme de broadcast, jugé trop coûteux et inadapté à l’échelle d’un réseau mondial. Une adresse multicast identifie un groupe d’interfaces, généralement dispersées sur plusieurs hôtes, qui souhaitent recevoir simultanément les mêmes paquets. Pour chaque adresse multicast, la portée est spécifiée par un champ particulier : les 4 bits de _scope_ inclus dans la structure de l’adresse. Ces bits définissent la limite géographique ou logique de diffusion :

- Un scope de `1` signifie que le paquet est destiné uniquement à l’équipement local.
- Un scope de `2` indique une portée limitée au lien local : tous les équipements sur le même segment physique ou virtuel peuvent recevoir le message.
- Un scope de `5` étend la portée au site, typiquement à l’ensemble d’un réseau d’entreprise interne.
- Un scope de `8` étend la portée à une organisation, permettant la diffusion à tous les sous-réseaux d’une même entité.
- Enfin, un scope de `e` (14 en hexadécimal) désigne une portée globale, qui rend le groupe multicast accessible depuis Internet tout entier, sous réserve que l’infrastructure de routage le permette.

Chaque adresse multicast IPv6 est structurée en plusieurs champs : un champ _Flag_ (4 bits) précise notamment si le groupe est permanent ou transitoire, un champ _Scope_ (4 bits) définit la portée, et un champ d’identification (112 bits) indique le numéro du groupe multicast.

| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Un exemple emblématique de multicast IPv6 est l’utilisation par le protocole _Neighbor Discovery Protocol_ (NDP). Plutôt que de recourir à ARP comme en IPv4, NDP s’appuie sur des adresses multicast comme `ff02::1:ff00:0/104` pour diffuser ses requêtes de découverte de voisinage, en sollicitant uniquement les hôtes concernés sur le même lien.

Ainsi, le périmètre des adresses IPv6 structure finement la manière dont les flux de données sont émis, reçus et routés. Cette granularité rend le protocole plus souple et plus performant pour gérer les communications locales comme globales, tout en évitant les inconvénients d’un broadcast généralisé.

## Assignation des adresses dans un réseau local
<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>

Dans ce chapitre, nous allons aborder l’un des aspects les plus concrets de la mise en œuvre d’IPv6 : l’assignation des adresses IP aux hôtes dans un réseau local. L’architecture IPv6 a été pensée pour offrir une grande souplesse et permettre à chaque machine de générer automatiquement sa propre adresse, tout en laissant la possibilité d’une configuration entièrement manuelle.

Un réseau local IPv6 repose sur un découpage systématique de l’adresse en deux parties : les 64 premiers bits représentent le préfixe du sous-réseau, fourni généralement par un routeur ou une autorité d’adressage, tandis que les 64 bits restants sont utilisés par l’hôte pour s’identifier de manière unique sur ce segment. Ce modèle simplifie grandement l’agrégation des routes et la gestion des blocs d’adresses.

Pour attribuer des adresses aux équipements, deux approches principales sont utilisées :
- La configuration manuelle, dans laquelle l’administrateur spécifie précisément l’adresse de chaque interface ;
- La configuration automatique, qui permet aux équipements de générer ou d’obtenir dynamiquement leur propre adresse.

En configuration manuelle, l’administrateur définit l’adresse IPv6 complète sur chaque interface. Attention : certaines valeurs restent toutefois réservées :
- `::/128` : adresse non spécifiée, jamais attribuée de façon permanente ;
- `::1/128` : adresse de bouclage (_loopback_), équivalent IPv4 : `127.0.0.1`.

Il n’existe en revanche aucun concept de diffusion générale (_broadcast_) comme en IPv4 ; les autres combinaisons "tout à 0" ou "tout à 1" dans la partie hôte n’ont pas de rôle particulier. Cette approche manuelle reste pertinente dans des environnements maîtrisés, mais elle devient vite lourde à maintenir à grande échelle.

En configuration automatique, plusieurs méthodes existent pour permettre aux équipements d’obtenir une adresse IPv6 fonctionnelle sans intervention manuelle. Le protocole **NDP** (_Neighbor Discovery Protocol_), spécifié par la RFC4862, permet l’auto-configuration *stateless*. Dans ce mode, l’hôte reçoit un préfixe réseau depuis un routeur local, et complète lui-même l’adresse avec un identifiant basé sur son adresse MAC. Cette méthode est extrêmement simple à mettre en œuvre et ne nécessite aucun serveur central.

Certaines implémentations, comme celles présentes dans les systèmes Windows, peuvent utiliser un tirage pseudo-aléatoire pour générer la partie hôte de l’adresse, ce qui améliore la confidentialité par rapport à l’utilisation directe de l’adresse MAC. En effet, la visibilité de l’adresse MAC dans les paquets IPv6 pose des problèmes de protection de la vie privée, car elle permet de suivre un appareil dans différents contextes réseau.

Une autre méthode largement utilisée est l’emploi du protocole DHCPv6, spécifié dans la RFC3315. Similaire au DHCP utilisé en IPv4, il permet une configuration plus contrôlée, centralisée, avec gestion des baux, options supplémentaires (DNS, MTU...), et enregistrement dans des bases de données. DHCPv6 peut être utilisé seul ou en complément de la configuration stateless pour fournir des paramètres annexes sans forcément attribuer l’adresse IP elle-même.

**Remarque importante :** lorsqu’on utilise la méthode basée sur l’adresse MAC, celle-ci est transformée en identifiant de 64 bits par le mécanisme EUI-64. Ce mécanisme insère les octets `FF:FE` au centre de l’adresse MAC d’origine (en 48 bits), et inverse le 7ème bit pour marquer l’unicité globale. Cela donne un identifiant d’interface stable, utilisé dans l’adresse IPv6 complète.

Voici un exemple de transformation d’une adresse MAC en EUI-64 :

![Image](assets/fr/045.webp)

Cependant, en raison des inquiétudes croissantes autour du traçage des appareils, les systèmes d’exploitation modernes (notamment Linux, Windows 10+, macOS, Android) proposent par défaut des mécanismes de "privacy extension", qui utilisent des identifiants d’interface aléatoires renouvelés périodiquement pour les connexions sortantes, tout en conservant un identifiant stable pour les communications internes (DNS, DHCPv6…).

Comme pour le DHCP en IPv4, les adresses IPv6 automatiquement assignées peuvent être associées à deux durées de vie définies par les routeurs ou serveurs DHCPv6 :
- *Preferred lifetime* : au-delà de cette durée, l’adresse reste valide, mais elle n’est plus utilisée pour initier de nouvelles connexions ;
- *Valid lifetime* : lorsque cette durée expire, l’adresse est entièrement retirée de la configuration de l’interface.

Cette logique permet de gérer dynamiquement l’évolution du réseau, en assurant par exemple une transition fluide d’un ancien fournisseur d’accès à un nouveau. En mettant à jour le préfixe annoncé par les routeurs et en ajustant les enregistrements DNS en parallèle, il est possible d’opérer une migration IPv6 sans interruption de service perceptible.

**Astuce :** l’utilisation combinée des durées de vie des adresses et des DNS permet de mettre en place une stratégie de transition progressive, où les nouvelles connexions s’orientent vers une nouvelle topologie, tandis que les anciennes terminent leur cycle de vie de façon transparente.

En résumé, IPv6 propose une flexibilité très étendue pour l’assignation des adresses : configuration manuelle, auto-configuration avec ou sans état, DHCPv6, ou encore génération aléatoire. Chaque approche a ses avantages et ses contraintes, et peut être adaptée en fonction du niveau de contrôle requis, de la taille du réseau, ou encore des exigences en matière de confidentialité.


## Assignation des blocs d’adresses IPv6
<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>

### Distribution des adresses

Le plan d’allocation des adresses IPv6 a été structuré pour répondre à deux objectifs : garantir l’unicité globale des adresses et permettre une hiérarchisation logique favorisant l’agrégation et la simplification des tables de routage. À l’instar d’IPv4, l’*Internet Assigned Numbers Authority* (IANA) reste au sommet de cette hiérarchie. C’est elle qui gère l’espace d’adressage unicast global et délègue des blocs d’adresses aux cinq registres Internet régionaux (_RIR_).

Les cinq RIR existants sont :
- ARIN (Amérique du Nord),
- RIPE NCC (Europe, Moyen-Orient, Asie centrale),
- APNIC (Asie-Pacifique),
- AFRINIC (Afrique),
- LACNIC (Amérique latine et Caraïbes).

L’IANA attribue à chaque RIR des blocs IPv6 de taille variable, généralement compris entre /23 et /12. Ces tailles permettent une grande souplesse tout en assurant l’évolutivité à long terme. Une fois ces blocs reçus, les RIR sont chargés de les redistribuer aux fournisseurs d’accès à Internet (FAI), aux grandes entreprises ou à des institutions publiques.

L’IANA attribue à chaque RIR un bloc IPv6 /12. Cette taille unique, fixée depuis 2006, assure à chaque registre régional une réserve stable et suffisamment large pour ses besoins de long terme. Une fois ce /12 reçu, le RIR le subdivise typiquement en /23, /26 ou /29. Les FAI se voient le plus souvent attribuer des blocs de type /32, bien que cette taille puisse varier selon la taille du FAI et sa zone géographique. À leur tour, ils peuvent allouer à chacun de leurs clients un bloc de /48, ce qui offre à chaque organisation 65 536 sous-réseaux distincts de /64 (ce qui est extrêmement généreux comparé à IPv4).

**Remarque importante :** un bloc /32 contient exactement 65 536 sous-blocs /48. On comprend ainsi que chaque FAI peut desservir plusieurs dizaines de milliers de clients sans manquer d’adresses. Chaque client disposera alors, grâce à son /48, d’un espace gigantesque pour structurer son propre réseau interne avec autant de segments /64 qu’il le souhaite.

Cette hiérarchie peut se visualiser dans le tableau suivant, qui illustre les tailles typiques de blocs alloués à chaque niveau :

| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Avec cette abondance d’adresses, le recours au NAT (*Network Address Translation*), devenu quasi indispensable en IPv4 pour pallier la pénurie d’adresses publiques, n’a plus lieu d’être. Chaque hôte connecté à Internet peut disposer d’une adresse publique unique et globale, ce qui simplifie la connectivité de bout en bout et facilite l’usage de protocoles comme IPSec, VoIP ou les connexions entrantes.

Pour vérifier à quel organisme une adresse IPv6 a été attribuée, on peut utiliser la commande `whois`, qui interroge les bases de données publiques des RIR. Cette transparence permet d’identifier l’organisation propriétaire d’un préfixe, ce qui peut être utile pour des questions de réseau, d’analyse ou de sécurité.

### Adressage PA vs PI

À l’origine, le modèle d’allocation IPv6 prévoyait uniquement l’usage de blocs de type PA (*Provider Aggregatable*), c’est-à-dire liés au fournisseur d’accès. Dans ce modèle, l’organisation cliente reçoit son préfixe du FAI, ce qui implique qu’en cas de changement de fournisseur, elle devra renuméroter l’ensemble de son infrastructure.

Ce mécanisme est facilité par les capacités d’auto-configuration d’IPv6 et la gestion des durées de vie des adresses, mais il reste contraignant pour les entreprises ayant des infrastructures critiques ou des exigences de redondance avec plusieurs fournisseurs.

C’est pourquoi, à partir de 2009, les politiques d’attribution ont été élargies pour permettre l’existence de blocs PI (*Provider Independent*). Ces blocs (généralement de taille /48) sont attribués directement à une entreprise ou une institution par un RIR, indépendamment de tout FAI. Ce modèle est particulièrement adapté aux organisations pratiquant le *multihoming*, c’est-à-dire connectées à plusieurs opérateurs simultanément. Le document RIPE-512 détaille précisément la politique européenne d’attribution de ces blocs PI par exemple.

### Notation des masques de sous-réseau

La notation des sous-réseaux en IPv6 utilise, tout comme en IPv4, la notation CIDR (*Classless Inter-Domain Routing*). Elle consiste à indiquer, après l’adresse, le nombre de bits constituant le préfixe, à l’aide du caractère `/`.

Prenons l’exemple suivant :

```
2001:db8:1:1a0::/59
```

Cela signifie que les 59 premiers bits sont fixes et désignent le réseau. Tous les bits restants (ici 69 bits) peuvent varier pour identifier des sous-réseaux ou des hôtes.

Ainsi, cette notation couvre les adresses allant de `2001:db8:1:1a0:0:0:0:0` à `2001:db8:1:1bf:ffff:ffff:ffff:ffff`.

Ce bloc couvre donc un ensemble de 8 sous-réseaux /64, chacun pouvant accueillir un très grand nombre d’hôtes.

La souplesse offerte par cette notation permet une planification fine de l’espace d’adressage, aussi bien dans les grandes infrastructures que dans les réseaux domestiques ou les environnements virtualisés. Elle favorise également l’agrégation des routes, réduisant la charge sur les routeurs et facilitant le déploiement à grande échelle.

### Paquets IPv6 et en-têtes

Le format d’un paquet IPv6 se distingue de son prédécesseur IPv4 par sa simplicité apparente et sa grande extensibilité. Un datagramme IPv6 débute toujours par un en-tête de taille fixe de 40 octets, qui contient les informations essentielles au routage du paquet. Ce choix bien plus épuré que l’en-tête IPv4 (qui pouvait varier de 20 à 60 octets) permet de traiter les paquets plus rapidement et plus efficacement dans les routeurs.

Toutefois, IPv6 ne sacrifie pas les fonctionnalités : au lieu d’intégrer de nombreux champs optionnels dans l’en-tête principal, il introduit un système d’en-têtes d’extension, placés immédiatement après l’en-tête de base. Ces en-têtes facultatifs permettent d’ajouter des données ou des instructions spécifiques à certaines fonctionnalités sans alourdir inutilement le traitement des paquets ordinaires.

Certains de ces en-têtes suivent un format rigide, mais d'autres sont conçus pour contenir un nombre variable d’options. Dans ces cas-là, chaque option est encodée selon un triplet `{Type, Longueur, Valeur}` :

- Le champ "Type" (1 octet) indique la nature de l’option ;
- Les deux premiers bits du "Type" précisent la conduite à adopter par les routeurs si l’option n’est pas reconnue :
	- Ignorer l’option et continuer le traitement,
	- Supprimer le datagramme,
	- Supprimer le datagramme et retourner un message ICMP d’erreur à la source,
	- Supprimer le datagramme sans notification (dans le cas de paquets multicast).
- Le champ "Longueur" (1 octet) spécifie la taille du champ "Valeur", compris entre 0 et 255 octets ;
- Le champ "Valeur" contient les données associées à l’option.

Voici un aperçu des différents types d’en-têtes d’extension définis par IPv6.

#### En-tête Hop-by-Hop

Cet en-tête, s’il est présent, est toujours placé immédiatement après l’en-tête de base. Il contient des informations destinées à être lues par chaque routeur traversé, ce qui le distingue des autres en-têtes généralement traités uniquement par la destination. Il est typiquement utilisé pour signaler des paramètres globaux ou déclencher des traitements spécifiques tout au long du trajet.

![Image](assets/fr/047.webp)

#### En-tête de routage

L’en-tête de routage permet de spécifier une liste d’adresses intermédiaires par lesquelles le paquet doit transiter. On distingue deux grandes approches :
- Le routage strict : le chemin exact est déterminé à l’avance ;
- Le routage lâche : seules certaines étapes obligatoires sont spécifiées.

Les quatre premiers champs de cet en-tête sont les suivants :
- **Next Header** : identifie le type de l’en-tête suivant ;
- **Routing Type** : définit la méthode de routage (généralement `0`) ;
- **Segments Left** : nombre de segments restant à parcourir ;
- **Address[n]** : liste des adresses intermédiaires.

Le champ "Segments Left" est initialisé au nombre total de segments restant et est décrémenté d’une unité à chaque saut.


![Image](assets/fr/048.webp)

#### En-tête de fragmentation

Contrairement à IPv4, où les routeurs pouvaient fragmenter les paquets, seul l’hôte source est autorisé à fragmenter un datagramme IPv6. Tous les nœuds IPv6 doivent pouvoir transmettre des paquets d’au moins 1280 octets. Si un routeur rencontre un paquet plus grand que la MTU du lien suivant, il renvoie un message *ICMPv6 Packet Too Big* à la source, qui ajuste alors la taille de ses envois.

L’en-tête de fragmentation contient les champs suivants :
- **Identification** : identifiant du datagramme pour reconstitution.
- **Fragment Offset** : position du fragment dans le datagramme original.
- **M flag** : indique s’il reste d’autres fragments.

![Image](assets/fr/049.webp)

#### En-tête d’authentification (AH)

Cet en-tête vise à sécuriser les communications en garantissant l’authenticité de l’émetteur et l’intégrité des données. Il est utilisé notamment avec le protocole IPsec. Grâce à un code de vérification (authentificateur), le destinataire peut s’assurer que le message provient bien de l’expéditeur attendu et qu’il n’a pas été altéré en cours de route.

En cas de tentative de modification frauduleuse, le code d’authentification ne correspondra plus, et le datagramme pourra être rejeté. Ce mécanisme permet également de lutter contre les attaques par rejeu, en détectant les duplications non autorisées.

![Image](assets/fr/050.webp)

#### En-tête Option de destination

Cet en-tête est destiné uniquement au destinataire final du datagramme. Il permet d’ajouter des options ou des métadonnées propres à l’application, sans que les routeurs intermédiaires n’en tiennent compte.

Initialement, aucune option de ce type n’était définie dans le protocole. Toutefois, cet en-tête a été introduit dès la conception d’IPv6 pour permettre l’ajout futur d’extensions sans modifier la structure globale des paquets. L’option nulle, par exemple, sert uniquement à compléter l’en-tête jusqu’à un multiple de 8 octets, pour des raisons d’alignement mémoire.

![Image](assets/fr/051.webp)


La conception des paquets IPv6 repose donc sur une séparation claire entre un en-tête de base minimaliste et des en-têtes d’extension optionnels, introduits de manière modulaire. Cette architecture garantit à la fois la performance du traitement standard et la souplesse nécessaire pour faire évoluer le protocole, intégrer des mécanismes de sécurité, de routage complexe ou de qualité de service, tout en maintenant la compatibilité avec les infrastructures futures.

## Relation entre IPv6 et DNS
<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>

Dans les réseaux modernes, le DNS (*Domain Name System*) permet la traduction des noms de domaine en adresses IP utilisables par les machines. Avec l’introduction d’IPv6, le DNS a naturellement dû s’adapter pour supporter les nouvelles adresses sur 128 bits, tout en maintenant la compatibilité avec IPv4. Cette coexistence est importante dans les environnements dual-stack où les deux versions du protocole IP cohabitent.

### Enregistrements DNS spécifiques à IPv6

Pour associer un nom de domaine à une adresse IPv6, le DNS utilise un enregistrement de type AAAA (*quad-A*), par analogie avec le type "A" utilisé pour les adresses IPv4. L’enregistrement AAAA permet donc d’indiquer qu’un nom de domaine correspond à une adresse IPv6 donnée. Voici un exemple concret :

```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```

Cet enregistrement indique que le domaine `ipv6.mydmn.org` est associé à l’adresse IPv6 `2001:66c:2a8:22::c100:68b`. Il est tout à fait possible, et même recommandé dans un contexte de compatibilité, d’associer un même nom de domaine à plusieurs adresses IP, qu’elles soient de type IPv4 (via un enregistrement A) ou IPv6 (via un enregistrement AAAA). Cela permet aux clients compatibles IPv6 de préférer cette version du protocole, tout en assurant le fonctionnement pour ceux qui ne supportent qu’IPv4.

Par ailleurs, le DNS prend également en charge la résolution inverse, c’est-à-dire la correspondance entre une adresse IP et un nom de domaine. Dans le cas d’IPv6, cette opération utilise des enregistrements de type PTR placés dans la zone `ip6.arpa`. Cette zone est spécifiquement réservée pour les résolutions inverses IPv6, à l’instar de la zone `in-addr.arpa` pour IPv4.

### Résolution inverse

La résolution inverse d’une adresse IPv6 suit une règle stricte : on transforme l’adresse en notation hexadécimale complète (16 octets, soit 32 caractères), on inverse l’ordre de chaque chiffre hexadécimal, et on les sépare par des points, en suffixant le tout avec `ip6.arpa`. Par exemple, pour l’adresse suivante :

```shell
2001:66c:2a8:22::c100:68b
```

On l’étend d’abord sur 32 chiffres hexadécimaux :

```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```

On inverse ensuite chaque nibble et on les sépare par des points, puis on termine par `ip6.arpa` :

```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```

Cette méthode garantit l’unicité et la standardisation des résolutions inverses dans l’espace d’adressage IPv6.

**Attention** : les requêtes DNS peuvent être envoyées indifféremment sur une liaison IPv4 ou IPv6. Le protocole de transport utilisé n’a aucune influence sur le type de réponse attendue. En d’autres termes, un client connecté en IPv6 peut tout à fait demander une adresse IPv4, et inversement. Le serveur DNS doit donc fournir les informations disponibles, sans se baser sur le protocole utilisé par le client pour la requête.

Le choix entre une adresse IPv4 ou IPv6 à utiliser pour se connecter à une machine cible, lorsqu’un nom d’hôte est associé aux deux types d’adresses, est régi par la RFC 6724. Cette norme définit un algorithme de sélection des adresses basé sur des critères tels que la proximité, la portée, ou la préférence explicite de certains préfixes. Par défaut, IPv6 est généralement prioritaire sur IPv4, sauf configuration contraire imposée par l’administrateur du système ou du réseau.

**Rappel important** : lorsqu’une adresse IPv6 doit être utilisée dans une URL (*Uniform Resource Locator*), elle doit impérativement être encadrée par des crochets (`[]`). Cela permet d’éviter toute confusion entre les deux-points (`:`) utilisés pour séparer les segments de l’adresse IPv6 et ceux qui sont utilisés dans l’URL pour séparer le nom de l’hôte du port de service.

Exemple valide :

```shell
http://[2001:db8::1]:8080
```

Cela garantit un traitement correct de l’URL, aussi bien par les navigateurs que par les serveurs web.

L’intégration d’IPv6 dans le système DNS repose donc sur de nouveaux types d’enregistrements, une méthode stricte pour les résolutions inverses, et des règles précises de sélection et de formatage qui assurent la compatibilité et la cohérence du routage.

### Synthèse de la partie

Dans cette partie, nous avons exploré en détail les principes fondamentaux qui régissent l’adressage IPv6. Nous avons d’abord expliqué la manière dont une adresse IPv6 est structurée, en insistant sur sa longueur de 128 bits, sa notation hexadécimale, ainsi que sur les différentes règles de simplification d’écriture permettant de raccourcir certaines séquences répétitives de zéros. Cette structure permet à IPv6 de surmonter les limitations de l’espace d’adressage d’IPv4, tout en apportant des garanties de scalabilité et de hiérarchisation efficaces.

Nous avons ensuite examiné les différentes catégories d’adresses IPv6 : unicast, anycast et multicast, en détaillant pour chacune leurs portées, leur utilisation typique et leur représentation dans l’espace d’adressage.

Par la suite, nous avons étudié les méthodes d’assignation des adresses IPv6 dans un réseau local, que ce soit via une configuration manuelle, via le protocole DHCPv6, ou encore grâce à des mécanismes d’autoconfiguration sans état comme ceux proposés par NDP. Ces approches permettent aux équipements de générer automatiquement leur propre adresse à partir du préfixe reçu et de leur adresse MAC (via EUI-64), tout en assurant une certaine flexibilité en matière de gestion de durée de vie et de confidentialité.

Nous avons également détaillé la manière dont les blocs d’adresses sont alloués, en partant de l’IANA, qui les distribue aux cinq RIR (*Registres Internet Régionaux*), puis aux fournisseurs d’accès, qui les redistribuent à leurs clients sous forme de sous-réseaux (souvent en /48, permettant 65536 sous-réseaux /64). La distinction entre les blocs _Provider Aggregatable_ (PA) et _Provider Independent_ (PI) permet de gérer des situations de _multihoming_ ou de changement de fournisseur.

Nous avons vu que le DNS s’adapte à IPv6 grâce à l’enregistrement AAAA et que les mécanismes de résolution inverse utilisent une nouvelle structure dans la zone `ip6.arpa`. Le protocole DNS reste indépendant du protocole de transport utilisé (IPv4 ou IPv6), ce qui assure une parfaite interopérabilité dans un environnement dual-stack.

IPv6 n’est donc pas une simple évolution de son prédécesseur, mais bien une refonte en profondeur du système d’adressage, pensée pour les défis actuels et futurs du réseau mondial.

Dans la dernière partie de ce cours NET 302, nous allons passer à la pratique et nous intéresser aux outils de diagnostic réseau.


# Outils de diagnostic réseau
<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>

## Les outils de la couche Accès Réseau
<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>

Dans ce premier chapitre de la dernière section consacrée au diagnostic réseau, nous allons nous concentrer sur les outils qui permettent d’analyser la couche d’accès réseau du modèle TCP/IP. Cette couche est en charge de la communication directe entre les équipements connectés à un même réseau physique, notamment à travers l’utilisation des adresses MAC et des interfaces réseau physiques comme les cartes Ethernet ou les interfaces Wi-Fi.

L’objectif est ici de fournir à l’administrateur les moyens concrets pour inspecter, tester et optimiser cette couche essentielle à la connectivité de bas niveau. Ces outils permettent d’évaluer le bon fonctionnement des interfaces, de diagnostiquer des problèmes liés à la configuration des cartes réseau ou encore d’identifier des anomalies comme des collisions, des pertes de paquets ou des erreurs de liaison.

### Utilitaires de voisinage IP/MAC

#### Outil `arp`

L’un des outils historiques de diagnostic réseau au niveau de la couche Accès Réseau est la commande `arp`. Bien qu’il tende à être remplacé par des commandes plus modernes comme `ip neigh` (que nous allons découvrir juste après), `arp` reste encore présent sur de nombreux systèmes pour consulter ou manipuler le cache ARP (*Address Resolution Protocol*). Ce cache contient les correspondances entre les adresses IP et les adresses MAC connues localement sur une machine. En d’autres termes, il permet d’identifier quelle adresse physique (adresse MAC) correspond à une certaine adresse IP dans le cadre d’une communication sur un réseau local.

Concrètement, lorsqu’un hôte souhaite envoyer un paquet à une adresse IP appartenant au même sous-réseau, il doit d’abord connaître l’adresse MAC de la machine cible. Cette association est réalisée grâce au protocole ARP, qui transmet une requête sur le réseau local et reçoit une réponse contenant l’adresse MAC de la machine correspondante. Cette information est ensuite mémorisée temporairement dans une table locale appelée "cache ARP", afin d’éviter des requêtes répétées à chaque envoi de paquet.

Pour consulter ce cache et observer les entrées actuellement connues par la machine, la commande suivante peut être utilisée :

```bash
arp -a
```

Cette commande liste l’ensemble des correspondances IP/MAC enregistrées localement, toutes interfaces confondues. Chaque ligne fournit le nom de l’hôte (s’il peut être résolu), l’adresse IP, l’adresse MAC correspondante et l’interface sur laquelle cette correspondance est observée.

Si l’on souhaite filtrer l’affichage en se concentrant sur une adresse IP spécifique, on peut préciser cette adresse dans la commande :

```bash
arp -a 192.168.1.5
```

Cela permet de vérifier si une adresse IP en particulier est bien connue du cache, ce qui peut aider à diagnostiquer une défaillance de communication entre deux hôtes du même réseau.

De même, pour afficher uniquement les entrées ARP associées à une interface réseau donnée (comme une carte Ethernet nommée `eth0`), on peut écrire :

```bash
arp -a -i eth0
```

Cette option est utile pour cibler des cas particuliers, notamment dans des environnements multicarte où une machine possède plusieurs interfaces réseau (filaire, sans fil, VPN...).

L’utilitaire `arp` ne se limite pas à la consultation. Il permet également de manipuler manuellement le cache ARP, ce qui peut s’avérer précieux dans certains cas de diagnostic avancé ou de simulation de situations spécifiques. Il est par exemple possible d’ajouter manuellement une association IP/MAC :

```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```

Cette commande crée une entrée statique dans la table ARP locale, qui associe l’adresse IP `192.168.1.7` à l’adresse MAC `00:17:BC:56:4F:25` sur l’interface `eth2`. Si l’interface n’est pas précisée, la première interface réseau jugée applicable est utilisée par défaut.

Enfin, il est également possible de supprimer une entrée du cache ARP, si celle-ci est incorrecte ou si l’on souhaite forcer une redécouverte :

```bash
arp -d 192.168.1.7
```

Cette commande efface l’entrée correspondante, ce qui oblige la machine à émettre une nouvelle requête ARP lors de la prochaine tentative de communication avec cette adresse IP.

**REMARQUE** : L’option de suppression accepte elle aussi un nom d’interface, si l’on souhaite cibler précisément l’entrée à supprimer sur une interface spécifique.

En résumé, l’outil `arp` permet un diagnostic bas niveau, particulièrement utile dans le cadre de réseaux locaux où les problèmes de connectivité peuvent souvent être liés à une résolution d’adresse incorrecte ou obsolète. Toutefois, il convient de noter que sur les systèmes récents, notamment avec les distributions Linux modernes, cet outil est de plus en plus remplacé par la commande `ip neigh`, issue de l’ensemble d’outils `iproute2`, qui offre des fonctionnalités similaires dans un cadre plus unifié.

#### Outil `ip neigh`

Sur les systèmes modernes, notamment les distributions Linux récentes, la commande `ip neigh` est l’outil de référence pour l’inspection et la gestion des correspondances entre adresses IP et adresses MAC. Cette commande est issue de la suite `iproute2` qui remplace progressivement les outils plus anciens comme `arp`, en offrant une interface plus cohérente et plus flexible pour le diagnostic réseau au niveau de la couche liaison de données.

La commande `ip neigh` permet de consulter le cache de voisinage IP local, qui joue un rôle équivalent au cache ARP pour IPv4 et au cache NDP (_Neighbor Discovery Protocol_) pour IPv6. Ce cache contient les associations connues entre les adresses IP (v4 ou v6) et les adresses MAC, ainsi que leur état (valide, en attente, expiré...).

La commande de base pour afficher le contenu du cache est :

```bash
ip neigh
```

Elle produit une liste des entrées connues, sous une forme synthétique indiquant l’adresse IP de destination, l’interface réseau concernée, l’adresse MAC correspondante (si disponible), ainsi que l’état de l’entrée (par exemple `REACHABLE`, `STALE`, `DELAY`, `FAILED`...).

Exemple de sortie :

```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```

Cette ligne indique que la machine connaît une correspondance valide entre l’adresse IP `192.168.1.5` et l’adresse MAC `00:17:BC:56:4F:25` via l’interface `eth0`.

Il est également possible de filtrer les entrées du cache en fonction de critères spécifiques, tels qu’une adresse IP, une interface, ou un état particulier. Par exemple, pour interroger uniquement l’adresse `192.168.1.7` :

```bash
ip neigh show 192.168.1.7
```

Ou pour afficher les entrées associées à l’interface `eth1` :

```bash
ip neigh show dev eth1
```

Au-delà de la consultation, la commande `ip neigh` permet également de modifier le cache manuellement. Par exemple, pour ajouter une entrée statique :

```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```

Cette commande associe de manière permanente l’adresse IP `192.168.1.7` à l’adresse MAC indiquée, sur l’interface `eth1`. Le mot-clé `nud permanent` (pour _Neighbor Unreachability Detection_) précise que l’entrée ne sera pas invalidée automatiquement.

Inversement, pour supprimer une entrée du cache :

```bash
ip neigh del 192.168.1.7 dev eth1
```

Cela force le système à effectuer une nouvelle résolution de voisinage lors du prochain envoi de paquet à cette adresse.

**REMARQUE** : L’outil `ip neigh` fonctionne aussi bien pour IPv4 que pour IPv6. Il interagit avec ARP dans le premier cas, et avec NDP dans le second, en utilisant une interface unifiée et cohérente pour les deux familles de protocoles. `ip neigh` offre donc une approche moderne et centralisée pour la gestion des relations IP/MAC sur un hôte.

### Outils d’analyse de paquets

Pour analyser finement ce qui transite sur un réseau informatique, il est important de disposer d’outils capables de capturer les paquets échangés entre les machines. Deux utilitaires se distinguent comme des références pour les administrateurs réseau et les analystes : `tcpdump` et `Wireshark`. Ces outils permettent de diagnostiquer des comportements anormaux, d’auditer les échanges protocolaires, ou encore d’étudier la sécurité du réseau en inspectant le contenu des trames.

#### `tcpdump` : l’analyse en ligne de commande

`tcpdump` est un outil en ligne de commande extrêmement puissant, conçu pour capturer et afficher les paquets circulant sur une interface réseau. Il fonctionne en temps réel, et grâce à sa légèreté, il peut être utilisé sur des systèmes sans interface graphique ou à ressources limitées. Il s’appuie sur la bibliothèque `libpcap`, qui fournit les fonctions de capture bas niveau indépendantes du matériel.

Un usage typique de `tcpdump` permet de surveiller l’activité réseau d’une machine ou d’un segment réseau, en filtrant les paquets selon des critères précis. En redirigeant les résultats vers un fichier, il devient possible de conserver une trace du trafic pour une analyse ultérieure ou pour une relecture dans un autre outil, comme Wireshark.

Voici la syntaxe générale de la commande :

```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```

- `-w` permet d’écrire les paquets capturés dans un fichier au format `libpcap` (extension `.cap` ou `.pcap`) ;
- `-i` désigne l’interface réseau à surveiller (par exemple `eth0`, `wlan0`) ;
- `-s` définit la taille maximale de capture pour chaque paquet. En spécifiant `0`, on capture l’intégralité des paquets ;
- `-n` empêche la résolution DNS ou la conversion d’adresses IP et de ports en noms symboliques, ce qui accélère les performances.

Les filtres d’expression, situés en fin de commande, permettent de ne capturer qu’un sous-ensemble spécifique du trafic. On peut combiner les mots-clés `host`, `port`, `src`, `dst`, etc., pour affiner la sélection.

Exemple concret : pour capturer les paquets HTTP (port 80) à destination ou en provenance du serveur `192.168.25.24`, et enregistrer le tout dans un fichier `fichier.cap` :

```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```

Cette capture pourra ensuite être réutilisée dans un outil graphique ou pour une relecture sur un autre système.

#### Wireshark : l’analyse visuelle avancée

Wireshark, anciennement connu sous le nom d’*Ethereal*, est un logiciel d’analyse réseau complet, doté d’une interface graphique. Contrairement à `tcpdump`, il permet une visualisation détaillée et structurée des paquets, avec décomposition protocolaire, graphiques de flux, statistiques de trafic, et filtres interactifs. Il repose lui aussi sur `libpcap`, ce qui lui permet d’ouvrir et d’exploiter les fichiers capturés par `tcpdump`.

Wireshark est disponible sur de nombreux systèmes d’exploitation, notamment Linux et Windows. Son installation nécessite des droits d’administrateur pour accéder à l’interface de capture. Une fois lancé, vous pouvez choisir une interface réseau dans le menu *Capture*. En cliquant sur *Start*, l’enregistrement des paquets débute en temps réel. L’affichage des paquets se fait en trois volets :
- la liste des trames ;
- les détails décodés par protocole ;
- les données brutes hexadécimales.

![Image](assets/fr/052.webp)

Wireshark excelle dans les scénarios où l’on souhaite observer les comportements complexes des protocoles, reconstituer les dialogues applicatifs (comme une session HTTP ou DNS), ou étudier les temps de réponse d’un service. Il est également possible d’appliquer des filtres d’affichage très précis à l’aide de sa syntaxe dédiée (différente de celle de `tcpdump`), afin de ne visualiser que les paquets pertinents.

#### Complémentarité des outils

Il est important de souligner que `tcpdump` et Wireshark ne sont pas interchangeables : chacun est spécialisé pour un usage particulier. `tcpdump` est adapté aux environnements en ligne de commande, aux scripts d’analyse automatisés et aux interventions sur des serveurs distants. Wireshark, quant à lui, est idéal pour une analyse détaillée, interactive et pédagogique du trafic réseau.

Les deux outils peuvent être combinés : on effectue une capture sur un système distant avec `tcpdump`, puis on transfère le fichier `.cap` pour l’analyser avec Wireshark sur une machine locale. Cette approche est très répandue.


### Outils d’analyse d’interface

Au niveau de la couche Accès Réseau, il est important de pouvoir interroger et configurer les interfaces réseau physiques afin de diagnostiquer des dysfonctionnements, optimiser les performances ou vérifier l’intégrité des connexions. Pour cela, l’un des outils les plus puissants à disposition sous Linux est `ethtool`, un utilitaire en ligne de commande permettant d’obtenir des informations techniques détaillées sur une interface Ethernet, mais aussi de modifier certains de ses paramètres en temps réel.

#### Visualiser les caractéristiques d’une interface

L’une des fonctionnalités de base de `ethtool` est sa capacité à interroger une interface afin d’en afficher les caractéristiques actuelles. On peut ainsi connaître :
- la vitesse du lien (par exemple, 100 Mbit/s, 1 Gbit/s ou 10 Gbit/s) ;
- le mode de négociation (half duplex ou full duplex) ;
- si l’auto-négociation est activée ou non ;
- le type de port utilisé (cuivre, fibre…) ;
- l’état du lien (actif ou non) ;
- la prise en charge de fonctionnalités avancées comme le *Wake-on-LAN*.

Ces informations sont importantes pour diagnostiquer des problèmes liés à la connectivité physique ou à un désalignement des négociations entre la carte réseau de l’hôte et l’équipement auquel elle est connectée (commutateur, routeur...).

Pour obtenir ces informations, on utilise simplement la commande suivante :

```bash
ethtool enp0s3
```

Cette commande renvoie un ensemble complet de données sur l’interface `enp0s3`, souvent rencontrée dans les distributions basées sur CentOS ou RHEL.

![Image](assets/fr/053.webp)

#### Modifier dynamiquement les paramètres d’une interface

`ethtool` ne se limite pas à l’observation : il permet aussi d’agir directement sur certains paramètres de l’interface sans redémarrage de la machine. Cela permet, par exemple, de forcer la vitesse du lien ou d’activer des options spécifiques selon les besoins du réseau local.

L’option `-s` est utilisée pour configurer dynamiquement des paramètres tels que :
- la vitesse (`speed`) à fixer explicitement (par exemple 1000 pour 1 Gbit/s) ;
- le type de duplex (`duplex`) à choisir entre `half` ou `full` ;
- l’activation ou la désactivation de l’auto-négociation (`autoneg`) ;
- l’activation du *Wake-on-LAN* (`wol`) ;
- ou encore le type de port.

Exemple 1 : activer l’auto-négociation sur l’interface :

```bash
ethtool -s enp0s3 autoneg on
```

Exemple 2 : activer la fonctionnalité *Wake-on-LAN* (pour permettre à la machine de se réveiller à distance via un paquet magique) :

```bash
ethtool -s enp0s3 wol p
```

Dans cet exemple, l’option `p` signifie que le réveil se fera dès la détection d’un paquet *Wake-on-LAN*. Cette configuration est souvent utilisée dans les environnements professionnels pour effectuer des mises à jour nocturnes ou des maintenances à distance.

#### Installation de l’outil

Il est important de noter que `ethtool` n’est pas systématiquement installé par défaut. Sur les distributions Red Hat/CentOS, on peut l’installer avec la commande :

```bash
yum install -y ethtool
```

Sur Debian et Ubuntu, la commande équivalente est :

```bash
sudo apt install ethtool
```

**ATTENTION** : dans toutes les commandes `ethtool`, le nom de l’interface réseau doit toujours être spécifié immédiatement après l’option (comme `-s`). Toute erreur de syntaxe dans la position des paramètres rendra la commande invalide ou inefficace.


## Les outils de couche Réseau
<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>

### Outils d’analyse de trafic

Dans le domaine du diagnostic réseau, la commande `ping` reste l’un des outils les plus simples mais également l’un des plus puissants à utiliser pour vérifier la connectivité entre deux machines. Elle permet d’établir si un hôte distant est atteignable à un instant donné, tout en fournissant des informations sur la latence du réseau, la stabilité de la liaison et la résolution des noms DNS.

La commande `ping` repose sur le protocole ICMP (*Internet Control Message Protocol*). Lorsqu’un utilisateur envoie une requête `ping`, son système émet un paquet ICMP de type "Echo Request" à destination d’une adresse IP ou d’un nom d’hôte. Si la machine cible est en ligne et que le chemin réseau est valide, celle-ci répond par un paquet ICMP de type "Echo Reply". Ce mécanisme simple permet de mesurer la latence et d’identifier des problèmes de connectivité ou de résolution de noms.

Exemple de commande classique :

```bash
ping 172.17.18.19
```

Réponse typique :

```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```

Dans cet exemple, on remarque que la résolution de nom a été effectuée automatiquement. Le nom de domaine `mydmn.org` est associé à l’adresse IP `172.17.18.19`, ce qui indique que la résolution DNS fonctionne correctement. La commande fournit également des données techniques comme :
- le numéro de séquence ICMP (`icmp_seq`), utile pour vérifier l’ordre d’arrivée des réponses ;
- le TTL (*Time-To-Live*), qui correspond au nombre de sauts réseau restants avant destruction du paquet ;
- le temps de réponse ou round-trip time/delay (`time`), exprimé en millisecondes, qui donne une indication sur la latence du lien.

#### Analyse plus fine des paramètres ICMP

Le TTL est un paramètre critique du protocole IP. Chaque datagramme envoyé comporte un champ TTL, initialisé par l’émetteur (souvent à 64, 128 ou 255). À chaque routeur traversé, ce champ est décrémenté de 1. Si le TTL atteint 0 avant l’arrivée à destination, le paquet est détruit et une erreur ICMP est renvoyée à l’émetteur. Ce mécanisme empêche les boucles réseau infinies.

Le temps de propagation (*round-trip delay/time*) mesure le délai total pour qu’un paquet parte de l’émetteur, atteigne la cible et revienne. En pratique, un temps inférieur à 200 millisecondes est considéré comme satisfaisant pour une liaison stable. Un allongement anormal de ce délai peut être le symptôme d’une congestion réseau, d’un routage inefficace ou d’une liaison de mauvaise qualité.

#### Utilisation avancée de `ping`

L’outil `ping` peut être utilisé avec différentes options pour affiner les tests et mieux observer certains comportements réseau.

Pour émettre des requêtes en broadcast, on peut utiliser l’option `-b` qui permet d’envoyer une requête à tous les hôtes d’un sous-réseau :

```bash
ping -b 192.168.1.255
```

Cette commande est utile dans les réseaux locaux pour détecter rapidement les hôtes actifs ou tester le comportement du réseau face à des requêtes broadcast. Attention cependant : dans de nombreuses configurations, les routeurs et pare-feu bloquent ce type de requêtes pour éviter les attaques par amplification.

Il est aussi possible de spécifier un intervalle d’envoi personnalisé avec l’option `-i` (par défaut, les requêtes sont espacées d’une seconde) :

```bash
ping -i 0.2 -c 10 192.168.1.7
```

Ici, on envoie 10 requêtes ICMP à l’intervalle de 0,2 seconde. Ce type de test est particulièrement utile pour détecter des fluctuations de latence sur une courte période ou pour stresser légèrement un lien afin d’observer sa stabilité.

### Outils d’analyse de la table de routage

La commande `ip route`, issue de la suite `iproute2`, est l'outil recommandé et standard sur les systèmes Linux modernes pour consulter et manipuler la table de routage IP du noyau. Elle remplace l’ancienne commande `route`, aujourd’hui obsolète, en offrant une syntaxe plus claire, une plus grande cohérence, et une prise en charge étendue des fonctionnalités réseau contemporaines (IPv6, multiples tables, espaces de noms...).

#### Affichage de la table de routage

La commande suivante permet d’afficher l’état actuel de la table de routage :

```bash
ip route show
```

Ce résultat liste l’ensemble des routes connues par le noyau, c’est-à-dire les chemins empruntés par les paquets IP sortants en fonction de leur destination.

Exemple typique de sortie :

```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100 
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```

Chaque ligne représente une route. Voici une explication des champs essentiels :
- **default** : route par défaut, utilisée si aucune route plus spécifique n’est trouvée.
- **via** : adresse de la passerelle utilisée pour atteindre la destination.
- **dev** : interface réseau empruntée par les paquets.
- **proto** : source d’origine de la route (manuelle, DHCP, kernel, etc.).
- **metric** : coût de la route, utilisé pour départager plusieurs chemins possibles.
- **scope** : portée de la route (par exemple : `link` pour une route directement connectée).
- **src** : adresse IP source utilisée sur cette interface pour les communications sortantes.

#### Ajout et suppression de routes

L’outil `ip route` permet également de modifier dynamiquement la table de routage, notamment pour ajouter ou retirer des routes statiques.

Ajout d’une route statique :

```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```

Cela configure une route vers le réseau `192.168.1.0/24`, en passant par la passerelle `192.168.1.1`, via l’interface `eth0`.

Suppression de cette route :

```bash
ip route del 192.168.1.0/24
```

Cette commande supprime la route définie précédemment.

#### Commandes utiles

Voici quelques variantes utiles pour l’analyse ou les scripts :
- `ip -4 route` : n’affiche que les routes IPv4 ;
- `ip -6 route` : n’affiche que les routes IPv6 ;
- `ip route list table main` : affiche la table de routage principale (valeur par défaut) ;
- `ip route get <address>` : permet de déterminer par quelle interface et passerelle un paquet vers une adresse donnée serait routé.

Exemple :

```bash
ip route get 8.8.8.8
```

Cela renvoie la route précise qu’emprunterait un paquet vers l’adresse `8.8.8.8`.

### Outils de traçage

L’un des outils les plus efficaces pour analyser la route suivie par les paquets IP entre un hôte source et une destination cible est la commande `traceroute`. Elle permet de visualiser, étape par étape, le chemin que parcourent les paquets, en identifiant les routeurs intermédiaires traversés. En cas de dysfonctionnement sur une liaison réseau ou d’interruption de service, `traceroute` permet de localiser précisément à quel niveau la rupture intervient.

Comme pour la commande `ping`, il est possible de cibler l’hôte distant soit par son nom de domaine complet (FQDN), soit par son adresse IP. Par exemple :

```bash
traceroute mydmn.org
```

#### Principe de fonctionnement

Le fonctionnement de `traceroute` repose sur le champ TTL (*Time To Live*) présent dans l’en-tête des paquets IP. Comme expliqué précédemment, ce champ est un compteur décrémenté à chaque passage par un routeur. Si la valeur du TTL atteint zéro, le paquet est considéré comme perdu et est supprimé par le routeur, qui retourne alors un message ICMP de type "Time Exceeded" à l’émetteur. Cela empêche les boucles infinies en cas de routage incorrect.

L’outil `traceroute` exploite précisément ce comportement pour cartographier les routeurs situés entre l’émetteur et le destinataire :
- Il envoie une première série de paquets UDP (généralement trois), avec un TTL égal à 1. Le premier routeur rencontre alors un TTL nul, détruit le paquet, et envoie une réponse ICMP. Son adresse IP et le temps de réponse sont enregistrés ;
- Puis, `traceroute` envoie une nouvelle série de paquets avec un TTL égal à 2. Le deuxième routeur fait de même ;
- Ce processus se répète jusqu’à ce que le paquet atteigne sa destination, qui retourne alors un message ICMP "Port unreachable" indiquant que l’hôte a bien été atteint.

L’outil utilise par défaut des paquets UDP envoyés sur des ports non utilisés (typiquement à partir du port 33434), mais peut être configuré pour utiliser ICMP (comme `ping`) ou même TCP, selon les systèmes ou les variantes de la commande.

Voici un exemple de résultat obtenu :

```bash
traceroute to www.google.fr (216.58.210.35), 64 hops max, 52 byte packets

 1  par81-024.ff.avast.com (62.210.189.205)   25.107 ms  24.235 ms  24.383 ms
 2  62-210-189-1.rev.poneytelecom.eu (62.210.189.1)  27.341 ms  27.119 ms  28.184 ms
 3  a9k1-45x-s43-1.dc3.poneytelecom.eu (195.154.1.92)  25.910 ms  25.040 ms  25.558 ms
 4  72.14.218.182 (72.14.218.182)  36.234 ms  39.907 ms  38.130 ms
 5  108.170.244.177 (108.170.244.177)  25.880 ms
    108.170.244.240 (108.170.244.240)  25.791 ms
    108.170.244.177 (108.170.244.177)  26.449 ms
 6  216.239.62.143 (216.239.62.143)  26.491 ms
    216.239.43.157 (216.239.43.157)  26.414 ms
    216.239.62.139 (216.239.62.139)  26.400 ms
 ...
 9  108.170.246.161 (108.170.246.161)  33.174 ms
    108.170.246.129 (108.170.246.129)  34.342 ms
    108.170.246.161 (108.170.246.161)  33.707 ms
10  108.170.232.105 (108.170.232.105)  33.845 ms  33.846 ms
    108.170.232.103 (108.170.232.103)  34.206 ms
11  lhr25s11-in-f35.1e100.net (216.58.210.35)  34.094 ms  33.353 ms  33.718 ms
```

Chaque ligne correspond à un routeur traversé, avec jusqu’à trois mesures de temps (en millisecondes) indiquant la latence du trajet aller-retour vers ce routeur. Ces temps permettent d’évaluer les performances de chaque segment du chemin.

#### Interprétation des résultats

Si un routeur ne répond pas ou filtre les messages ICMP, des astérisques `*` s’affichent à la place du temps de réponse. Cela peut signifier :
- un pare-feu qui bloque les réponses ICMP ;
- un équipement configuré pour ne pas répondre à ces messages ;
- un problème temporaire de connectivité sur le chemin.

La commande `traceroute` permet ainsi non seulement d’identifier la route suivie, mais également de repérer les zones de latence anormale ou les ruptures de connexion.

Sur certains systèmes, la commande peut être remplacée par `tracepath`, qui ne nécessite pas les privilèges root. Pour les connexions IPv6, on utilisera `traceroute6` ou `tracepath6`.

Exemple pour tracer une route IPv6 :

```bash
traceroute6 ipv6.google.com
```

### Outils de vérification des connexions actives

Pour diagnostiquer les connexions réseau en cours et obtenir une vue d’ensemble de l’activité réseau d’un système Linux, la commande `ss` (pour _socket statistics_) est aujourd’hui l’outil de référence. Issue de la suite `iproute2`, elle remplace `netstat`, désormais obsolète, en offrant des performances supérieures et une meilleure précision.

`ss` permet d’afficher les connexions TCP et UDP actives, les ports en écoute, les adresses locales et distantes, les états des connexions, ainsi que les processus associés.

#### Utilisation générale

Exécutée sans option, la commande `ss` affiche les connexions TCP actives. Voici sa syntaxe de base :

```bash
ss [options]
```

Quelques options courantes pour affiner l’analyse :
- `-t` : affiche uniquement les connexions TCP ;
- `-u` : affiche uniquement les connexions UDP ;
- `-l` : limite l’affichage aux sockets en écoute ;
- `-n` : désactive la résolution de noms (affichage brut des adresses IP et numéros de ports) ;
- `-p` : affiche les processus associés à chaque socket (PID et nom du programme) ;
- `-a` : affiche toutes les connexions, y compris les inactives ;
- `-s` : fournit des statistiques de haut niveau sur les sockets.

#### Cas pratique

Si l’on souhaite afficher toutes les connexions actives utilisant le port TCP 80 (HTTP), on peut utiliser :

```bash
ss -ant | grep ':80'
```

Cette commande affiche les connexions TCP actives impliquant le port 80. Les états typiques (comme `LISTEN`, `ESTABLISHED`, `TIME-WAIT`) permettent d’interpréter le statut des échanges en cours.

Exemple de sortie :

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```

Pour afficher toutes les connexions réseau avec les processus associés :

```bash
ss -tulnp
```

Pour obtenir un résumé statistique global des sockets utilisés :

```bash
ss -s
```

Pour filtrer les connexions UDP uniquement :

```bash
ss -unp
```

Ces commandes sont particulièrement utiles pour repérer des connexions suspectes, des ports inattendus en écoute, ou surveiller l’activité réseau d’un service particulier.


## Les outils de la couche Transport et supérieure
<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### Outils d’interrogation DNS

Dans les couches supérieures du modèle TCP/IP, et notamment à la couche Application, il est important de comprendre le fonctionnement des résolutions de noms. Les outils d’interrogation DNS permettent non seulement de vérifier si un nom de domaine est bien associé à une adresse IP, mais également de diagnostiquer des problèmes de configuration, de propagation ou d’inaccessibilité d’un serveur DNS. Ces outils sont essentiels pour tout administrateur réseau ou tout utilisateur qui souhaite mieux comprendre les échanges DNS dans un environnement IP.

#### La commande `nslookup`

Le plus simple des outils d’interrogation DNS est `nslookup`. Il permet de soumettre une requête à un serveur DNS et d’obtenir en retour l’adresse IP associée à un nom de domaine (ou inversement). Utilisé sans option, il interroge par défaut le serveur DNS configuré sur le système, mais on peut lui indiquer explicitement un serveur à interroger en le précisant directement dans la commande.

Exemple d’utilisation simple avec résolution directe :

```bash
nslookup mydmn.org
```

Et pour interroger un serveur DNS spécifique :

```bash
nslookup mydmn.org 192.6.23.4
```

Cette requête demande au serveur situé à l’adresse `192.6.23.4` la résolution du nom `mydmn.org`. C’est une méthode utile lorsqu’on souhaite vérifier si un serveur DNS donné connaît ou non un nom de domaine, ou encore pour vérifier le bon fonctionnement de ce serveur.

#### La commande `dig`

Plus moderne, plus complète et plus souple que `nslookup`, la commande `dig` (*Domain Information Groper*) permet d’effectuer des requêtes DNS complexes, tout en fournissant des informations détaillées sur le processus de résolution, la hiérarchie des serveurs consultés, le type d’enregistrement obtenu (A, AAAA, MX, TXT, etc.) et les éventuels problèmes rencontrés.

Voici un exemple de requête standard :

```bash
dig mydmn.org
```

Ou encore pour cibler un serveur DNS spécifique :

```bash
dig @192.6.23.4 mydmn.org
```

Cette commande permet de tester la disponibilité d’un enregistrement DNS sur un serveur donné. L’un des avantages majeurs de `dig` est sa capacité à afficher le détail du message DNS retourné, ce qui est utile pour diagnostiquer des erreurs de configuration.

#### Configuration manuelle des résolveurs DNS

Il est parfois nécessaire de modifier les serveurs DNS utilisés localement, notamment dans des environnements de test ou pour forcer l’utilisation de serveurs spécifiques. Pour cela, on peut éditer le fichier `/etc/resolv.conf`, qui permet de définir les paramètres de recherche DNS du système.

Voici un exemple de configuration :

```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```

- Le champ `search` indique le domaine à ajouter automatiquement lors de la résolution de noms courts ;
- Les directives `nameserver` précisent les adresses IP des serveurs DNS à utiliser. L’ordre d’apparition détermine la priorité d’interrogation.

Attention, cette configuration est temporaire dans de nombreuses distributions modernes (notamment avec `systemd-resolved`) et peut être écrasée à chaque redémarrage ou reconnexion réseau. Des méthodes plus pérennes existent (comme l’usage de `resolvconf`, `systemd-resolved`, ou la modification de fichiers *NetworkManager*).

#### La commande `host`

L’outil `host` est un autre utilitaire DNS simple mais efficace. Il permet de résoudre des noms de domaine en adresse IP, ou inversement, et peut également servir à diagnostiquer des erreurs de réponse DNS ou des pannes sur une interface réseau.

Exemple d'utilisation :

```bash
host mydmn.org
```

Ou pour une résolution inverse :

```bash
host 192.6.23.4
```

Il est particulièrement utile pour des vérifications ponctuelles, notamment en ligne de commande dans des scripts automatisés.

Il est important de rappeler qu’interroger de manière répétée ou intensive des serveurs DNS tiers sans autorisation peut être considéré comme une tentative d’intrusion ou un comportement malveillant. Certaines commandes, lorsqu’elles sont mal utilisées (ou utilisées sur des réseaux qui ne vous appartiennent pas), peuvent être assimilées à de la reconnaissance réseau, une première étape dans certaines formes d’attaques. Il est donc important de limiter l’usage de ces outils aux environnements que l’on administre ou dont on a explicitement la charge.

### Outils d’interrogation du réseau

Dans une démarche de surveillance ou de sécurisation d’un réseau local ou étendu, il est important de pouvoir identifier les équipements actifs et les services qu’ils exposent. C’est précisément ce que permet l’outil `nmap` (*Network Mapper*).

https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Présentation de `nmap`

`nmap` permet d’interroger de manière ciblée un ou plusieurs hôtes afin de détecter les ports ouverts, les services accessibles (HTTP, SSH, DNS...) et parfois même le type de système d’exploitation utilisé. Grâce à ses nombreuses options, il est possible d’obtenir une vision précise et synthétique de l’état de la surface d’exposition d’un réseau, ce qui est essentiel dans les phases d'audit ou de durcissement d'une infrastructure.

Attention cependant à l’usage de cet outil : comme pour la commande `host`, il ne doit jamais être utilisé sur un réseau ou une infrastructure qui ne vous appartient pas ou sans autorisation explicite. Les scans de ports non autorisés peuvent être considérés comme des tentatives de reconnaissance malveillante et sont souvent détectés comme telles par les dispositifs de sécurité (pare-feu, IDS/IPS), voire sanctionnés.

#### Utilisation de base

Pour scanner un hôte spécifique et visualiser les ports ouverts, il suffit d’exécuter :

```bash
nmap 192.168.0.1
```

Cette commande va effectuer un scan des 1000 ports les plus courants sur l’hôte `192.168.0.1` et afficher les services accessibles ainsi que les protocoles utilisés. Si le DNS est configuré, il est également possible d’utiliser le nom d’hôte au lieu de l’adresse IP.

#### Scan d’un réseau complet

L’un des avantages de `nmap` est sa capacité à analyser une plage d’adresses en une seule commande. Cela permet, par exemple, de dresser un inventaire rapide des machines actives sur un réseau donné :

```bash
nmap 192.168.0.0/24
```

Dans cet exemple, tous les hôtes de l’espace `192.168.0.0` à `192.168.0.255` seront interrogés. Le résultat présentera, pour chaque adresse IP, la liste des ports ouverts, leur état (open, filtered…), et si possible, le nom du service correspondant.

![Image](assets/fr/055.webp)

Un administrateur peut s’appuyer sur `nmap` pour plusieurs tâches :
- Détection d’hôtes actifs : en scannant un sous-réseau, on identifie les machines qui répondent à une requête ;
- Inventaire des services exposés : utile pour vérifier que seuls les ports nécessaires sont accessibles (principe du moindre privilège) ;
- Vérification de la conformité : comparer les ports ouverts avec la politique de sécurité réseau ;
- Prévention des failles : repérer des services non sécurisés ou obsolètes ouverts sur des machines critiques.

https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Outils d’interrogation des processus

Pour analyser en profondeur les processus actifs et les fichiers ouverts sur un système, notamment dans un contexte réseau, l’un des outils les plus puissants à la disposition des administrateurs Linux est la commande `lsof` (*List Open Files*). Contrairement à ce que son nom pourrait laisser penser, `lsof` ne se limite pas aux fichiers classiques : dans le système UNIX, tout est considéré comme un fichier, y compris les sockets réseau, les périphériques, les canaux de communication...

Cet outil permet donc d’avoir une vue transversale du système, en croisant des informations sur les processus actifs, les ports réseau ouverts, les fichiers manipulés et les utilisateurs impliqués.

#### Analyse réseau avec `lsof`

L’option `-i` permet de restreindre la sortie aux connexions réseau, qu’il s’agisse de TCP, UDP, IPv4 ou IPv6. Elle est utile pour observer rapidement quels processus interagissent avec le réseau :

```bash
lsof -i
```

Ce type de commande liste tous les processus en cours qui utilisent une socket réseau, avec l’information sur le port utilisé, le protocole (TCP/UDP), l’état de la connexion, ainsi que le PID et l’utilisateur correspondant.

#### Filtrage par adresse IP ou port

Pour affiner la recherche, il est possible de spécifier une adresse IP et un port. Cela permet d’isoler précisément un flux réseau, par exemple une communication SMTP (port 25) avec une machine donnée :

```bash
lsof -n -i @192.168.2.1:25
```

Cela affichera uniquement les connexions réseau actives avec l’hôte `192.168.2.1` sur le port 25, ce qui peut être utile pour diagnostiquer une activité suspecte ou un blocage SMTP.

#### Suivi des accès à un périphérique

L’un des grands atouts de `lsof` est sa capacité à surveiller l’utilisation des fichiers spéciaux, tels que les partitions de disque. On peut par exemple connaître les processus qui ont ouvert des fichiers sur la partition `/dev/sda1` :

```bash
lsof /dev/sda1
```

Cela est utile lorsqu’une tentative de démontage échoue parce que le périphérique est encore utilisé, ou lorsqu’on cherche à comprendre quelles applications accèdent à une partition donnée.

#### Analyse croisée : processus et réseau

Il est possible de combiner plusieurs options pour obtenir des informations précises sur les ressources ouvertes par un processus spécifique. Par exemple, pour connaître tous les ports réseau ouverts par le processus ayant pour PID 1521 :

```bash
lsof -i -a -p 1521
```

L’option `-a` réalise une intersection des critères (ici : `-i` et `-p`), qui limite ainsi l’affichage aux connexions réseau appartenant à ce seul processus.

#### Suivi multi-utilisateur

Enfin, `lsof` permet aussi d’analyser le comportement d’un ou plusieurs utilisateurs, en listant tous les fichiers ouverts par ceux-ci, éventuellement en filtrant par PID :

```bash
lsof -p 1521 -u 500,phil
```

Cette commande permet par exemple de savoir quels fichiers ou connexions réseau sont utilisés par l’utilisateur `phil` ou l’UID 500, pour le processus 1521.

### Synthèse de la partie

Au terme de cette dernière partie, nous avons exploré une large palette d’outils indispensables pour le diagnostic, l’analyse et l’administration des réseaux informatiques. Cette étude, organisée autour des différentes couches du modèle TCP/IP, permet non seulement de mieux comprendre le fonctionnement des communications réseau, mais également d’acquérir une méthodologie rigoureuse pour identifier, localiser et résoudre les problèmes potentiels.

Grâce à ces outils, l’administrateur dispose d’un ensemble cohérent de leviers techniques pour surveiller l’état du réseau, analyser les flux, auditer les connexions et intervenir rapidement sur les équipements ou les services défaillants.

#### Couche Accès Réseau

Ces utilitaires offrent une visibilité directe sur les interfaces et les trames :
- **arp / ip neigh** : inspection et modification du cache ARP/NDP pour vérifier ou corriger les associations IP-MAC ;
- **tcpdump** : capture en ligne de commande, filtrable et exportable, des paquets circulant sur une interface ;
- **Wireshark** : décodage graphique approfondi des trames pour une analyse ;
- **ethtool** : interrogation et réglage dynamiques des paramètres physiques d’une carte Ethernet (vitesse, duplex, WoL...).

#### Couche Réseau

Ici, on évalue la connectivité IP, le routage et le cheminement des paquets :
- **ping** : test d'accessibilité et mesure de latence via ICMP ;
- **ip route** : consultation et manipulation de la table de routage pour contrôler les chemins empruntés ;
- **traceroute** : identification, saut par saut, des routeurs traversés jusqu’à la destination ;
- **ss** : inventaire précis des sockets TCP/UDP et des processus associés (en remplacement de netstat).

#### Couches Transport et Application

Aux niveaux supérieurs, l’objectif est de diagnostiquer services et processus :
- **nslookup / dig / host** : requêtes DNS pour valider la résolution de noms et analyser les enregistrements ;
- **nmap** : exploration des ports ouverts et des services exposés afin d’évaluer la surface d’attaque ;
- **lsof** : recensement des fichiers et sockets ouverts par les processus, pour corréler activités système et réseau.

La maîtrise conjointe de ces outils, chacun dédié à une étape précise du modèle TCP/IP, permet d’adopter une démarche méthodique : partir de la couche physique, remonter vers le routage, puis jusqu’aux services applicatifs. Cette chaîne d’expertise assure à l’administrateur la capacité de diagnostiquer, de sécuriser et d’optimiser l’infrastructure, ce qui garantit ainsi la performance et la disponibilité du réseau.


# Partie finale
<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>




## Avis & Notes
<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>


## Examen final
<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>


## Conclusion
<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>
