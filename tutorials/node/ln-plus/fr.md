---
name: LN+
description: Comment améliorer la connectivité et la liquidité d’un nœud Lightning sans recourir à des solutions centralisées ni à des hubs imposés.
---

![cover](assets/cover.webp)

## Introduction

LN+ (Lightning Network Plus) est une plateforme communautaire conçue pour faciliter la coopération entre opérateurs de nœuds Lightning Network. Son objectif principal est d’améliorer la connectivité, la liquidité et la décentralisation du réseau Lightning, sans passer par des intermédiaires centralisés.

Ce tutoriel se concentre principalement sur le service **« Swaps »**, qui constitue aujourd’hui la fonctionnalité la plus utilisée et la plus structurante de LN+. Les autres services proposés par la plateforme seront brièvement présentés, sans entrer dans des détails opérationnels.

## Présentation générale de LN+

### Qu’est-ce que Lightning Network Plus ?

Lightning Network Plus (LN+) est une plateforme communautaire destinée aux opérateurs de nœuds Lightning souhaitant coopérer de manière directe et volontaire. Elle vise à faciliter la création de canaux Lightning utiles, équilibrés et durables, tout en évitant le recours à des solutions centralisées ou à des hubs imposés.

LN+ repose sur un principe fondamental : la coopération entre pairs, fondée sur la transparence, la réciprocité et la réputation.

### Aperçu des services proposés par LN+

LN+ propose plusieurs services destinés à améliorer la topologie et la liquidité du réseau Lightning, parmi lesquels :

- **Swaps** : ouverture réciproque de canaux entre opérateurs (service principal).
- **Rings** : ouvertures de canaux circulaires entre plusieurs participants.
- **Trust-based swaps** : variantes reposant davantage sur la confiance et l’historique des participants.
- **Fonctionnalités sociales** : profils, commentaires et système de réputation.

Dans la suite de ce tutoriel, nous nous concentrerons exclusivement sur le service **Swaps**, qui constitue le cœur de l’usage actuel de LN+.

## Le service « Swaps » de LN+

### Définition d’un swap LN+

Un **swap LN+** est un accord volontaire entre deux opérateurs de nœuds Lightning consistant à ouvrir mutuellement des canaux Lightning d’une capacité équivalente (ou convenue à l’avance). Contrairement à une ouverture de canal classique unilatérale, le swap repose sur une **réciprocité explicite**.

En pratique :

- Vous ouvrez un canal vers le nœud de votre partenaire.
- Votre partenaire ouvre un canal vers votre nœud.
- Les deux parties immobilisent une quantité similaire de bitcoins on-chain.

### À quoi servent les swaps pour les opérateurs de nœuds ?

Le service Swaps répond à plusieurs problématiques clés rencontrées par les opérateurs Lightning :

- **Amélioration de la connectivité** : création de canaux bidirectionnels utiles dès leur ouverture.
- **Meilleure gestion de la liquidité** : chaque partie dispose à la fois de capacité entrante et sortante.
- **Réduction du risque de canaux inutiles** : le partenaire est incité à maintenir le canal ouvert.
- **Renforcement de la décentralisation** : mise en relation directe entre opérateurs, sans hubs imposés.

### Pour quels profils de nœuds les swaps sont-ils utiles ?

Les swaps sont particulièrement utiles pour :

- Les nouveaux nœuds souhaitant améliorer rapidement leur routabilité.
- Les opérateurs intermédiaires cherchant à densifier leur graphe de canaux.
- Les nœuds orientés routing qui souhaitent optimiser leur topologie.

## Connexion de votre nœud Lightning à LN+

### Prérequis techniques

Avant de commencer, vous devez disposer :

- D’un nœud Lightning fonctionnel (LND, Core Lightning ou Eclair).
- D’un accès à l’interface de gestion de votre nœud.
- D’une capacité on-chain suffisante pour ouvrir des canaux.

Rendez-vous sur le site de [Lightning Network](https://lightningnetwork.plus/) Plus et cliquez sur le bouton `Login` en haut à droite de l’interface.

![capture](assets/fr/03.webp)

### Authentification par signature de message

Pour vous authentifier, vous devez signer le message fourni à l’aide de la clé privée de votre nœud Lightning. Avec ThunderHub, cette opération est très simple.

Commencez par copier le message affiché par LN+.

![capture](assets/fr/04.webp)

Dans ThunderHub, allez dans l’onglet `Tools`, puis cliquez sur le bouton `Sign` dans la section `Messages`.

![capture](assets/fr/05.webp)

Collez le message d’authentification fourni par LN+, puis cliquez sur `Sign`.

![capture](assets/fr/06.webp)

ThunderHub signe alors ce message à l’aide de la clé privée de votre nœud. Copiez la signature générée.

![capture](assets/fr/07.webp)

Collez cette signature dans le champ correspondant sur le site LN+, puis cliquez sur `Sign in`.

![capture](assets/fr/08.webp)

Vous êtes maintenant connecté à LN+ avec votre nœud Lightning. Ce processus permet à LN+ de vérifier que vous êtes bien le propriétaire légitime du nœud que vous revendiquez sur leur plateforme.

![capture](assets/fr/09.webp)

Si vous le souhaitez, vous pouvez personnaliser votre profil LN+, par exemple en ajoutant une courte biographie.

## Participer à un swap existant

### Accéder aux offres de swap

Pour participer à votre première ouverture de canaux, rendez-vous dans le menu `Swaps` en haut de l’interface. Vous y trouverez l’ensemble des swaps actuellement disponibles en fonction des caractéristiques de votre nœud.

![capture](assets/fr/10.webp)

### Conditions d’éligibilité

Pour rejoindre une offre de swap existante, il suffit de sélectionner l’annonce correspondante puis de s’y inscrire. LN+ permet toutefois au créateur d’un swap de définir certaines **conditions d’éligibilité**, telles que :

- un nombre minimal de canaux déjà ouverts ;
- une capacité totale minimale du nœud ;
- certains types de connexions acceptées.

### Cas des nœuds récents

En conséquence, surtout lors des premières utilisations, il est possible que **peu, voire aucune offre ne soit accessible** à votre nœud. C’est une situation courante pour les nœuds récents ou encore peu connectés.

Dans mon cas, malgré l’existence de quelques canaux ouverts, aucune offre ne répondait aux critères requis.

## Créer sa propre offre de swap

### Quand créer son propre swap ?

Lorsque aucune offre existante n’est accessible, créer son propre swap constitue souvent la meilleure solution. Cela permet également de garder le contrôle sur les paramètres du swap.

### Configuration d’un swap

Cliquez sur **Start Liquidity Swap**, puis configurez les paramètres de votre offre :

- sélectionnez le nombre total de participants (3, 4 ou 5) ;
- indiquez la capacité des canaux à ouvrir ;
- définissez la durée d’engagement pendant laquelle les participants s’engagent à ne pas fermer leurs canaux ;
- précisez les restrictions éventuelles applicables aux participants (nombre minimal de canaux, capacité totale minimale, type de connexion accepté).

![capture](assets/fr/11.webp)

###  Publication et attente des participants

Une fois l’ensemble des paramètres renseignés, cliquez sur **Start Liquidity Swap** pour publier votre offre. Il ne reste plus qu’à attendre que d’autres opérateurs s’y inscrivent.

![capture](assets/fr/12.webp)

## Finaliser un swap

###  Ouverture effective des canaux

Toutes les places du swap ayant été prises, chaque participant peut voir, depuis son interface LN+, vers quel nœud il doit ouvrir un canal Lightning.

![capture](assets/fr/13.webp)

De votre côté, ouvrez le canal en utilisant le Node ID fourni par LN+ et en respectant le montant indiqué. Cette opération peut être réalisée via ThunderHub, un autre gestionnaire de nœud Lightning ou directement via l’interface de base de votre nœud.

![capture](assets/fr/14.webp)

Une fois l’ouverture lancée, le canal apparaît dans la section des canaux en attente.

![capture](assets/fr/15.webp)

###  Confirmation dans LN+

Retournez ensuite sur LN+ afin de confirmer que vous avez bien initié l’ouverture du canal, en cliquant sur le bouton `Channel Opening Started`.

![capture](assets/fr/16.webp)

###  Fin du swap

Lorsque tous les participants ont ouvert les canaux auxquels ils s’étaient engagés, le swap est considéré comme terminé.

##  Réputation et bonnes pratiques de communication

###  Le système de réputation sur LN+

LN+ intègre un système de réputation basé sur les avis laissés par les participants à l’issue des swaps. Ces avis sont publics et influencent directement la capacité d’un opérateur à rejoindre ou créer de futurs swaps.

![capture](assets/fr/17.webp)

###  Bonnes pratiques recommandées

Afin de préserver une bonne réputation et de garantir le bon déroulement des swaps, il est recommandé de :

- respecter les délais d’ouverture des canaux ;
- communiquer rapidement en cas de problème ou de retard ;
- utiliser la section commentaires pour échanger avec les autres participants ;
- ne pas fermer un canal avant la fin de la période d’engagement.


![capture](assets/fr/18.webp)

###  Pourquoi la réputation est centrale dans LN+

LN+ repose sur un modèle de coopération volontaire, sans contrainte technique forte. La réputation constitue donc le principal mécanisme incitatif garantissant le sérieux et la fiabilité des participants.

## Autres services proposés par LN+

En complément des Swaps, LN+ propose d’autres services destinés à améliorer la connectivité et la coordination entre opérateurs de nœuds Lightning. Les **Rings** permettent à plusieurs participants de créer une boucle d’ouvertures de canaux, renforçant ainsi la redondance des chemins de routage et la densité du graphe Lightning. Les **Trust-based swaps** reposent sur des principes similaires aux swaps classiques, mais accordent davantage de flexibilité aux participants disposant déjà d’une réputation établie sur la plateforme.

LN+ intègre également des fonctionnalités sociales, telles que les profils publics de nœuds, les commentaires associés aux swaps et un système de réputation. Ces outils ne constituent pas des services techniques à proprement parler, mais jouent un rôle central dans le bon fonctionnement de la plateforme, en facilitant la communication, la coordination et la confiance entre opérateurs.

## Conclusion

Le service Swaps de LN+ constitue un outil efficace pour améliorer la connectivité, la liquidité et la décentralisation du réseau Lightning. En favorisant des ouvertures de canaux réciproques et coordonnées, LN+ permet aux opérateurs de nœuds de renforcer leur topologie tout en s’inscrivant dans une logique de coopération responsable et décentralisée.
