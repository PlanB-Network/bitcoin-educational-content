---
name: Matrix
description: Guide pour comprendre, configurer et utiliser Matrix, la plateforme de communication sécurisée, ouverte et décentralisée.
---

![cover](assets/cover.webp)

## Qu’est-ce que Matrix ?

Matrix est un **protocole de communication décentralisé** conçu pour permettre l’échange de messages, de fichiers et d’appels audio/vidéo entre utilisateurs et applications, sans dépendance à une entreprise centrale. Contrairement aux plateformes de messagerie traditionnelles, Matrix constitue une **infrastructure ouverte**, comparable à l’email : chacun peut choisir un serveur ou en exploiter un soi-même, tout en conservant la possibilité d’échanger avec le reste du réseau.

Matrix se distingue par trois principes fondamentaux :

### Un protocole, pas une application

Matrix n’est pas une application comme WhatsApp ou Telegram.  
C’est un langage standardisé que plusieurs applications peuvent utiliser.  
Autrement dit, une grande variété de logiciels  Element, FluffyChat, Cinny, Nheko et d’autres, permettent d’accéder au même réseau Matrix.

Cela garantit une liberté totale : changement d’application sans perte de contacts, diversité des interfaces, indépendance vis-à-vis d’un fournisseur unique.

![capture](assets/fr/03.webp)

### Un réseau décentralisé et fédéré

La structure de Matrix repose sur la **fédération**, un modèle où plusieurs serveurs indépendants coopèrent entre eux.  
Chaque serveur (appelé _homeserver_) peut accueillir des utilisateurs, héberger des salons de discussion et synchroniser les messages avec les autres serveurs du réseau.
Ainsi :

- aucune entité ne contrôle l’ensemble du système ;
- un serveur peut disparaître sans affecter le reste du réseau ;
- chaque organisation ou individu peut administrer son propre espace.

Ce modèle assure une **résilience élevée** et reflète les valeurs de souveraineté technologique.

![capture](assets/fr/03.webp)

### Un système sécurisé et chiffré

Matrix prend en charge le **chiffrement de bout en bout (E2EE)** pour les échanges privés et les groupes chiffrés.  
Les messages sont lisibles uniquement par les participants, et non par les serveurs intermédiaires.  
Cette approche permet de communiquer sans exposer le contenu des échanges à un tiers, tout en conservant la transparence du protocole et la possibilité d’héberger son propre serveur.

![capture](assets/fr/05.webp)

### Une interopérabilité unique

Un des atouts majeurs de Matrix est sa capacité à servir de **pont entre différents systèmes de communication**. Grâce aux _bridges_, il est possible de connecter :

- Telegram
- WhatsApp
- Signal
- Messenger
- Slack
- Discord
- IRC, XMPP, etc.

Cela permet d’unifier des communautés dispersées entre plusieurs plateformes tout en conservant le contrôle sur son infrastructure.

![capture](assets/fr/06.webp)

## Comment fonctionne Matrix?

Cette section présente la structure interne du réseau Matrix afin de comprendre comment les utilisateurs, les serveurs et les applications interagissent au sein de cet écosystème décentralisé. Matrix repose sur trois éléments essentiels : les _homeservers_, les identités, et les _clients_ utilisés pour communiquer.

### Les serveurs : les homeservers

Matrix fonctionne grâce à des serveurs indépendants appelés _homeservers_.  
Chaque homeserver gère :

- les comptes des utilisateurs qu’il héberge,
- les conversations privées et les salons auxquels ces utilisateurs participent,
- la synchronisation avec les autres serveurs du réseau.

Tous les homeservers connectés au réseau Matrix échangent automatiquement les messages et les événements des salons partagés. Ainsi :

- un utilisateur inscrit sur le serveur A peut discuter avec un utilisateur du serveur B,
- un salon peut être réparti sur des dizaines de serveurs,
- personne ne détient le contrôle d’un salon ou d’une communauté dans son ensemble.

Ce modèle assure une grande résilience et permet à chaque organisation ou individu de gérer sa propre infrastructure.

### Les identifiants Matrix

Chaque utilisateur dispose d’un identifiant unique, appelé **MXID** (_Matrix ID_), qui ressemble à une adresse :

```bash
@nomdutilisateur:serveur.xyz
```

Il se compose :

- d’un nom d’utilisateur, précédé de **@**
- du nom du serveur sur lequel le compte a été créé, précédé de **:**

Exemples :

- `@alice:matrix.org`
- `@bened:monserveur.bj`

Cet identifiant permet de communiquer avec n’importe quel autre utilisateur Matrix, indépendamment du serveur d’origine.

### Les clients Matrix (applications)

Pour utiliser Matrix, il faut se connecter avec une application appelée **client Matrix**.

Les plus connus sont :

- Element (web, mobile, desktop)
- FluffyChat (mobile)
- Cinny (web/desktop minimaliste)
- Nheko (desktop)

Ces applications ne sont que des interfaces permettant :

- de consulter les messages,
- d’envoyer du texte, des images ou des fichiers,
- de rejoindre ou créer des salons,
- d’effectuer des appels audio/vidéo.

Toutes les applications communiquent avec les serveurs via le même protocole standardisé.

### Les salons (rooms) et les messages privés (DM)

Dans Matrix, les échanges se déroulent dans des **rooms** :

- une room peut être publique ou privée
- elle peut contenir deux personnes ou des milliers
- elle peut être partagée entre plusieurs serveurs
- elle possède un identifiant unique commençant par **!**

Les messages privés sont simplement des salons avec deux participants, souvent appelés **DM (Direct Messages)**.

La synchronisation des salons se fait en temps réel entre les serveurs participants, ce qui permet une expérience fluide tout en conservant la décentralisation.

## Pourquoi utiliser Matrix ?

Matrix n’est pas simplement une alternative aux messageries centralisées : c’est une technologie qui répond à des besoins réels en matière de souveraineté numérique, de sécurité et d’interopérabilité. Plusieurs raisons expliquent pourquoi de plus en plus de personnes, d’entreprises et d’institutions choisissent ce protocole pour communiquer.

### Reprendre le contrôle de ses communications

La plupart des plateformes de messagerie fonctionnent selon un modèle centralisé : un acteur unique contrôle les serveurs, l'accès, les données et les règles d'utilisation. Ce modèle implique une dépendance totale envers le fournisseur.
Matrix adopte une approche différente.  
Chacun peut choisir où héberger son compte, ou même déployer son propre serveur. Aucune entité n’est en position de bloquer un utilisateur, d'exiger une identification intrusive ou d’imposer un changement de politique.
Cette architecture redonne de l’autonomie, tant aux individus qu’aux organisations. Les communications ne reposent plus sur la confiance envers une entreprise, mais sur un protocole ouvert, documenté et vérifiable.

### Communiquer de manière sécurisée et chiffrée

Matrix prend en charge le chiffrement de bout en bout pour les conversations privées et les groupes. Ce mécanisme garantit que seuls les participants peuvent lire les messages, même si ceux-ci transitent par des serveurs tiers dans la fédération.

Le protocole utilise l’algorithme Megolm/Olm, conçu spécifiquement pour fournir une sécurité forte dans des environnements distribués et multi-appareils.

Cela permet de :

- protéger les conversations sensibles,
- empêcher tout accès non autorisé (même de la part du serveur hôte),
- conserver la confidentialité sur le long terme.

Le chiffrement n’est pas une option : c’est une brique centrale du protocole.

### Ne plus dépendre d’une seule application

Matrix n’est pas une application, mais un protocole.  

Cette diversité de client garantit :

- un choix adapté aux besoins de chacun,
- la possibilité d’utiliser Matrix sur n’importe quel type d’appareil,
- l’absence de dépendance envers un logiciel unique.

Si un client ne convient pas ou cesse d’être maintenu, il suffit d’en choisir un autre : le compte continue de fonctionner normalement.

### Fédérer et interconnecter différentes communautés

La fédération permet à différents serveurs de fonctionner ensemble tout en étant administrés indépendamment.  
Ainsi :

- une organisation peut gérer son propre homeserver,
- des particuliers peuvent rejoindre des serveurs publics,
- tous peuvent communiquer entre eux comme s’ils étaient sur une même plateforme.

Cette flexibilité permet de créer des espaces de communication adaptés à chaque besoin : équipes, associations, communautés, institutions ou projets open source.

Matrix est particulièrement prisé dans les milieux techniques, les collectifs d’activistes, les chercheurs, les gouvernements, et de plus en plus dans les communautés Bitcoin.

### Une interopérabilité unique dans le paysage de la messagerie

L’un des atouts majeurs de Matrix est sa capacité à **étendre** les échanges grâce à des bridges (passerelles) capables de relier :

- WhatsApp
- Telegram
- Signal
- Slack
- Discord
- IRC
- XMPP
- et de nombreuses autres plateformes

Matrix devient ainsi une couche unificatrice pour les communications, permettant de rassembler plusieurs communautés dispersées sur différentes applications.

Cette interopérabilité réduit la fragmentation et simplifie la collaboration.

### Un protocole libre, ouvert et pérenne

Le protocole Matrix est entièrement open source et développé de manière transparente.  
Cela garantit plusieurs avantages :

- une évolution continue du standard,
- la possibilité pour n’importe qui de vérifier le code,
- une indépendance face aux changements commerciaux ou politiques,
- une résilience à long terme.

Contrairement aux messageries propriétaires, l’avenir de Matrix ne dépend pas d’une entreprise, mais d’une communauté mondiale et d’un standard ouvert.

## Comment créer un compte Matrix ?

Créer un compte Matrix est simple et ne nécessite aucune compétence technique. L’utilisateur peut rejoindre un serveur existant, créer son identifiant, puis commencer à discuter immédiatement. Cette section présente les étapes essentielles.

### Choisir un serveur (public ou privé)

Matrix est un réseau fédéré : il existe de nombreux serveurs (homeservers) gérés par différentes organisations, communautés ou particuliers. Le choix du serveur détermine seulement _où_ le compte est hébergé, mais n’empêche pas de communiquer avec l’ensemble du réseau.
**Deux options existent :**

### • Utiliser un serveur public

C’est la solution la plus simple.  
Exemples de serveurs très utilisés :

- _matrix.org_ (le plus connu)
- _envs.net_
- serveurs communautaires thématiques (tech, privacy, open-source…)

Ces serveurs conviennent aux utilisateurs débutants qui souhaitent une inscription rapide.

### • Utiliser un serveur privé

Idéal pour :

- une organisation,
- une famille,
- un projet open source,
- une équipe de travail,
- ou pour une utilisation souveraine et auto-hébergée.

Dans ce cas, quelqu’un doit administrer le serveur (Synapse, Dendrite, Conduit…).
Peu importe le serveur choisi, les utilisateurs peuvent discuter entre eux grâce à la fédération.

### Créer un compte étape par étape

Comme Matrix est un protocole ouvert, plusieurs applications permettent d’y accéder.  
Comme présentées, plus haut, elles offrent des interfaces et des fonctionnalités différentes selon les besoins :

- **Element** : le client le plus complet, disponible sur toutes les plateformes.
- **FluffyChat** : simple, moderne et idéal pour les mobiles.
- **Nheko** : client léger et ergonomique pour ordinateurs.
- **SchildiChat** : variante d’Element avec des améliorations d’ergonomie.
- **NeoChat** : intégré à l’écosystème KDE.

Le choix du client n’a pas d’impact sur le compte : tous fonctionnent avec n’importe quel serveur Matrix.

### Étapes classiques :

- Ouvrir l’application choisie. Pour notre cas, nous allons le faire avec [Element](app.element.io).
- Choisir “Créer un compte”.

![cover-kali](assets/fr/10.webp)

Pour plus de simplicité, il est possible de créer un compte Matrix en utilisant **Google, Facebook, Apple, GitHub ou GitLab**. Ces services sauront uniquement que leur compte a été utilisé pour accéder à Matrix : c’est ce qu’on appelle une **connexion sociale**.

Pour davantage de confidentialité, il est également possible de s’inscrire manuellement en choisissant un **nom d’utilisateur**, un **mot de passe** et une **adresse e-mail**.

Selon le serveur choisi, un **captcha** peut être demandé, ainsi que l’acceptation des **conditions d’utilisation**.

Une fois l’inscription validée, un e-mail de confirmation est envoyé.  
Il suffit de cliquer sur le lien reçu pour activer le compte et accéder à l’application web (Element) afin de rejoindre ses premières conversations Matrix.

![cover-kali](assets/fr/11.webp)

Vous disposez désormais d'un compte et utilisez la version Web d'Element.

## Ajouter son premier contact

Pour communiquer avec quelqu’un sur Matrix, il suffit de connaître son identifiant complet, appelé **Matrix ID**.

Exemple :

`@alice:matrix.org   @bened:monserveur.bj`

### Ajouter un contact

Pour inviter des amis à votre chat de groupe, cliquez sur le cercle `i` en haut à droite coin. Il ouvre le panneau de droite. Cliquez sur « Personnes » pour afficher la liste des membres de cette salle : vous devriez être les seuls présents pour le moment.

![cover-kali](assets/fr/12.webp)

Cliquez sur « Inviter dans cette salle » en haut de la liste des personnes et une invite s'ouvrira vous pouvez donc inviter vos amis à vous rejoindre dans Matrix. S'ils sont déjà allumés Matrice, entrez leur ID de matrice. S'ils ne le sont pas, entrez leur adresse e-mail et ils seront invités à se joindre à nous.

Il n’existe pas de système “d’amis” : un contact est simplement une personne avec laquelle une conversation a été ouverte.

![cover-kali](assets/fr/13.webp)

La personne que vous avez invitée peut soit accepter, soit refuser l’invitation. S'ils acceptent ça, tu devrais les voir rejoindre la pièce. Plus on est de fous, plus on rit !

![cover-kali](assets/fr/14.webp)

### Installer son propre serveur

Matrix prend tout son sens lorsqu'il est utilisé avec un serveur personnel.  
Déployer son propre homeserver permet :

- de conserver le contrôle complet des données,
- de définir ses propres règles d’utilisation,
- d’héberger plusieurs comptes (amis, équipe, communauté),
- et d’assurer une résilience maximale en cas de restrictions ou de censure.

 **Solutions disponibles :**

- **Synapse** : l’implémentation historique et la plus complète.
- **Dendrite** : plus léger, performant et conçu pour l’avenir du protocole.
- **Conduit** : une variante minimaliste, simple à déployer.

 **Prérequis :**

- un nom de domaine,
- une machine ou un VPS,
- un minimum de compétences en administration système.

Même si cela demande un peu de configuration, gérer son propre serveur transforme Matrix en un outil souverain et durable.

### Rejoindre ses premiers salons

Matrix repose en grande partie sur les _rooms_ (salons).  
Il existe des salons publics, privés, communautaires, techniques, locaux ou internationaux.

 **Trois façons de rejoindre un salon :**

1. **Via un lien d’invitation** (souvent sous forme d’URL `matrix.to`).
2. **En cherchant le nom du salon** dans l’application.
3. **En entrant l’identifiant complet du salon**, par exemple :  
    `#bitcoin:matrix.org`  
    `#communauté-bénin:monsrv.bj`

Une fois rejoint, le salon se comporte comme un groupe de discussion classique avec historique, chiffrement, fichiers, réactions et appels audio/vidéo selon le client utilisé.

![capture](assets/fr/09.webp)

## Aller plus loin

Une fois les bases maîtrisées, Matrix offre de nombreuses possibilités avancées. Que ce soit pour connecter d’autres messageries, héberger son propre serveur ou organiser une communauté, l’écosystème est très riche.

### Bridges (WhatsApp, Telegram, Signal, etc.)

Un bridge (pont) permet de relier Matrix à d’autres messageries.  
Grâce à lui, il devient possible d’envoyer et recevoir des messages provenant de :

- **WhatsApp**
- **Telegram**
- **Signal**
- **Facebook Messenger**
- **Discord**
- **Slack**
- **IRC**
- et bien d’autres

### Ce que permettent les bridges

- Centraliser toutes ses conversations dans Matrix
- Fournir une interface libre pour interagir avec des services propriétaires
- Gérer une communauté multi-plateforme depuis un seul endroit

Certains bridges sont officiels, d’autres communautaires.  
Selon le service, ils peuvent nécessiter :

- un serveur personnel,
- une configuration supplémentaire,
- ou l’utilisation d’un bridge public existant.
  
### Utiliser Matrix pour une organisation, une communauté ou un projet Bitcoin

Matrix n’est pas seulement un outil personnel.  
Il peut être utilisé pour structurer des groupes de travail, organiser des communautés locales ou gérer la communication d’un projet.

 **Exemples d’usages :**

- Communautés open-source
- Projets Bitcoin et écosystèmes Lightning
- Groupes d’étudiants ou de développeurs
- Organisations citoyennes
- Médias indépendants
- Collectifs et associations locales

 **Pourquoi c’est intéressant ?**

- Outil **100 % open-source**
- Communication **souveraine et décentralisée**
- Espaces organisés en **salons**, **sous-groupes**, **salons privés**, etc.
- Intégration possible avec Nextcloud, GitLab, Mattermost, ou des bots personnalisés
- Gestion fine des permissions et de la modération

Matrix devient alors un pilier de la communication pour toute structure souhaitant rester indépendante des grandes plateformes centralisées.

## Conclusion

Matrix représente une solution moderne, ouverte et sécurisée pour la communication en temps réel, offrant une alternative décentralisée aux plateformes traditionnelles. Grâce à son architecture fédérée et à ses protocoles de chiffrement avancés, il permet aux utilisateurs de conserver le contrôle de leurs données tout en bénéficiant d’une expérience fluide et interopérable. Que ce soit pour un usage personnel, professionnel ou communautaire, Matrix offre un cadre robuste et évolutif pour construire des environnements de communication adaptés aux besoins d’aujourd’hui.

Pour approfondir davantage et découvrir toutes les fonctionnalités offertes par Matrix, vous pouvez consulter la documentation officielle disponible ici :  
[https://matrix.org/docs/](https://matrix.org/docs/)
