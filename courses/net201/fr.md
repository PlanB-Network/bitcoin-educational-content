---
name: Principes fondamentaux des réseaux
goal: Acquérir une compréhension approfondie des principes fondamentaux des réseaux.
objectives:
  - Comprendre l’architecture et le fonctionnement du protocole TCP/IP
  - Expliquer les différences, avantages et contraintes d’IPv4 et d’IPv6
  - Identifier et distinguer les différents types d’adresses IP
  - Configurer et vérifier l’adressage IP sur des systèmes Unix/Linux
  - Utiliser les principaux outils de diagnostic pour analyser et résoudre des problèmes réseau
---

# L’essentiel pour naviguer dans l’univers IP


___
Ce cours NET 201 est une adaptation du cours *Les bases du réseau : TCP/IP, IPv4 et IPv6*, rédigé par Philippe Pierre en français et publié sur [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), sous licence Creative Commons Attribution - ShareAlike 4.0 International (CC BY-SA 4.0).
___

Dans ce cours, je vous propose de décrire le fonctionnement de l’adressage IP, brique de base de nos architectures et de nos équipements en réseau. On va notamment balayer le protocole TCP/IP afin de voir quelle(s) relation(s) entretiennent ces fameuses adresses IP avec d’un côté les adresses physiques et de l’autre, les noms de machine, enregistrés dans les DNS.

On essaiera de voir les différences entre IPv4 et IPv6, et, pour chacun de ces protocoles on expliquera les différents types d’adresses : privée, publique, broadcast, unicast…

Je propose de terminer ce tour d’horizon par un récapitulatif des différents outils de diagnostic d’un réseau, permettant d’analyser, d’auditer mais également de modifier le comportement de celui-ci.

Ce cours s’adresse principalement aux informaticiens et linuxiens ou étudiants ayant quelques notions en réseau et souhaitant approfondir leurs connaissances et mieux maitriser la gestion et l’administration des équipements connectés sur des environnements de type Unix/Linux.

+++



# Introduction
<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>

## Aperçu du cours
<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>

Ce cours propose une introduction complète aux fondamentaux des réseaux IP et se structure en quatre grandes parties, chacune abordant un aspect essentiel pour comprendre, configurer et diagnostiquer un réseau informatique.

### Protocole TCP/IP

Dans cette première section, nous poserons les bases nécessaires en explorant la notion de réseau et l’historique du protocole TCP/IP. Nous étudierons ses composantes majeures : l’IP, le TCP, ainsi qu’une brève incursion dans le protocole QoS IPv5. Nous aborderons également les primitives de services pour comprendre la logique d’échange de données.

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


# Protocole TCP/IP


## Qu’est-ce qu’un réseau ?


Ce premier module se propose de décrire de façon approfondie le fonctionnement du protocole TCP/IP. Nous verrons notamment les origines de ce mécanisme d’échange ainsi que l’adressage associé.

On décrira ici les différents composants et comment s’articule le modèle TCP/IP. Les principales définitions seront posées afin d’avoir une meilleure compréhension du fonctionnement de ce modèle et surtout quels sont les périphériques accédés. Mais commençons d'abord par revoir ce qu'est un réseau.

Un réseau au sens étymologique représente un ensemble de points entrelacés par un ensemble de relations. Par extension, cela désigne un ensemble interconnecté d’équipements et de leurs relations, autorisant la circulation en continu ou discontinue. On va ainsi trouver différents types de réseaux :

- Réseau en anneau
- Réseau en arbre
- Réseau en bus
- Réseau en étoile
- Réseau maillé

### Réseau en anneau

On dit d’un réseau que sa topologie est en anneau, lorsque toutes les stations, ou les équipements, sont connectés en chaine les uns aux autres par une liaison bipoint de la dernière à la première. Chaque poste joue le rôle de station intermédiaire. Toute trame émise depuis une station est réémise vers la suivante. La défaillance d’un hôte rompt la chaîne.

![](https://www.it-connect.fr/wp-content-itc/uploads/2017/06/reseau-en-anneau.jpg)


### Réseau en arbre

On parle aussi de réseau hiérarchique, car l’architecture est divisée en niveaux. Le sommet représente la racine ou le sommet et est connecté à plusieurs nœuds du niveau inférieur. Ces nœuds peuvent également être connectés à un ou plusieurs nœuds du niveau inférieur… Le tout forme un arbre. Là encore, si le père des équipements (le sommet de l’arbre), vient à défaillir, cela interdit toute communication avec ses subordonnés.

![](https://www.it-connect.fr/wp-content-itc/uploads/2017/06/reseau-en-arbre.jpg)

### Réseau en bus

Le câblage ici s’effectue via une liaison unique des unités. Cela représente un faible coût de déploiement et la défaillance d’un nœud, n’empêche pas les autres de fonctionner. Les équipements peuvent être reliés de façon passive par dérivation électrique ou optique. Le point faible, dans ce cas, est le support (ou média) de transfert. Lorsque celui-ci tombe en panne, c’est tout le réseau qui s’arrête.

![](https://www.it-connect.fr/wp-content-itc/uploads/2017/06/reseau-en-bus.jpg)

### Réseau en étoile

Ce genre d’architecture est également appelé "_hub & spoke_". C’est la topologie la plus courante. Elle permet une gestion et un dépannage très facile. La panne d’un nœud ne perturbe absolument par le réseau global. En revanche, le concentrateur (aussi appelé hub ou plus fréquemment appelé commutateur), qui relie tous les nœuds entre eux, constitue un point unique de défaillance. Une panne de cet équipement rend le réseau totalement inutilisable. Le réseau Ethernet est un très bon exemple de réseau en étoile. Il faut toujours veiller, par contre à la longueur des câbles utilisés.

![](https://www.it-connect.fr/wp-content-itc/uploads/2017/06/reseau-en-etoile.jpg)


**REMARQUE** : on trouve encore dans certains cas une topologie de réseau linéaire. Son énorme avantage est son faible coût de déploiement, mais la défaillance d’un nœud provoque la scission du réseau en deux sous-réseaux distincts.

### Réseau maillé

Cela correspond à plusieurs liaisons point à point où chaque unité est reliée à N-1 point permettant ainsi de la mettre en relation avec l’ensemble des autres équipements. L’inconvénient de cette architecture est le nombre de liaisons nécessaires qui croient lorsque le nombre de points augmente : pour `N` terminaux, il faut `N x (N-1) / 2` liaisons. Ce genre de topologie se rencontre dans les grands réseaux de distribution, comme Internet.

![](https://www.it-connect.fr/wp-content-itc/uploads/2017/06/reseau-maill%C3%A9.jpg)

Il existe évidemment un certain nombre d’autres topologies, comme le réseau en grille ou le réseau en hyper cube. En fait, Internet est le nom donné à l’interconnexion de nombreux réseaux ayant des topologies différentes. L’unification se fait au niveau de l’adressage IP (qu’il s’agisse de IPv4 ou IPv6) et d’un très grand nombre de règles et de protocoles définis par l’IETF. Ainsi, aucun des cas de topologies mentionnés ci-dessus ne correspond. Comme la majorité des grands réseaux, on dit d’Internet que sa topologie est quelconque et indépendante du plan d’adressage qui y est défini.




























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
