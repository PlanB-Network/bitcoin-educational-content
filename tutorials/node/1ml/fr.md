---
name: 1ML
description: Apprendre à utiliser l’explorateur 1ML pour comprendre et analyser le réseau Lightning de Bitcoin.
---
![cover](assets/cover.webp)

## Introduction

Le Lightning Network est une solution de paiement rapide et peu coûteuse construite au‑dessus de Bitcoin, permettant des transactions instantanées et sécurisées. Observer ce réseau est essentiel pour comprendre son fonctionnement, sa topologie et l’état des nœuds qui le composent. Un explorateur Lightning, comme 1ML, sert à visualiser les données publiques du réseau, notamment les nœuds actifs, les canaux ouverts et la capacité disponible, offrant ainsi une vue d’ensemble précieuse pour les utilisateurs, développeurs et opérateurs de nœuds.

## Accéder à 1ML et comprendre la page d’accueil

Pour accéder à 1ML, il suffit d’ouvrir votre navigateur web et de taper l’adresse [https://1ml.com](https://1ml.com). Vous arrivez alors sur la page d’accueil, qui sert de tableau de bord global pour le Lightning Network.

![capture](assets/fr/03.webp)

Cette page affiche plusieurs statistiques importantes en haut de l’écran, dont :

- Le **nombre total de nœuds actifs** sur le réseau, c’est-à-dire les ordinateurs qui participent à l’envoi et la réception des paiements Lightning.
- Le **nombre de canaux ouverts**, qui correspondent aux connexions entre ces nœuds permettant les transferts de fonds.
- La **capacité totale du réseau**, exprimée en bitcoin (BTC), qui indique la somme des capacités de tous les canaux publics.

Ces chiffres sont mis à jour régulièrement pour refléter l’état actuel du réseau. Ils permettent de se faire une idée de sa taille, de sa croissance et de sa robustesse.

![capture](assets/fr/04.webp)

Juste en dessous, la page propose des listes avec des classements :

- Les **nœuds les plus connectés**, qui ont le plus de canaux ouverts vers d’autres nœuds.
- Les **plus grandes capacités** sur les nœuds, indiquant ceux qui peuvent transférer les montants les plus importants.
- Les canaux les plus importants en termes de capacité.

Des filtres permettent aussi d’affiner ces listes par localisation géographique ou autres critères.

Cette page est une base idéale pour débuter l’exploration du Lightning Network et comprendre sa topologie générale.

![capture](assets/fr/05.webp)

![capture](assets/fr/06.webp)

## Explorer les nœuds Lightning

Pour explorer un nœud sur 1ML, commencez par utiliser la barre de recherche située en haut de la page. Vous pouvez y entrer le **Node ID**, c’est-à-dire l’identifiant unique du nœud, ou son **alias**, qui est un nom plus facile à retenir.

Une fois la recherche effectuée, cliquez sur le nœud correspondant pour accéder à sa page détaillée.

![capture](assets/fr/07.webp)

Sur cette page, plusieurs informations importantes sont affichées :

- **Node ID** : cet identifiant unique est une longue suite de caractères qui permet de reconnaître précisément le nœud dans tout le réseau.  

![capture](assets/fr/08.webp)

- **Alias** : c’est le nom choisi par le propriétaire du nœud pour le représenter publiquement.  

![capture](assets/fr/09.webp)

- Le **nombre de canaux** indique combien de connexions le nœud a ouvertes avec d’autres nœuds, tandis que la **capacité totale** représente la somme des bitcoins disponibles dans ces canaux. Un nœud avec un grand nombre de canaux et une forte capacité est généralement bien connecté et capable de transférer d’importants montants rapidement sur le réseau.

![capture](assets/fr/10.webp)

- L’**uptime**, ou disponibilité, mesure la durée pendant laquelle un nœud est resté actif et accessible en ligne, ce qui reflète sa fiabilité. L’**âge** du nœud, quant à lui, indique depuis combien de temps ce nœud est présent sur le réseau, témoignant de sa stabilité et de son expérience au sein du Lightning Network.

![capture](assets/fr/11.webp)

Ces données vous aident à comprendre l’importance et la fiabilité d’un nœud dans le Lightning Network. Par exemple, un nœud avec un grand nombre de canaux, une forte capacité et un uptime élevé est souvent un acteur majeur du réseau.

## Explorer les canaux lightning

### Qu’est-ce qu’un canal Lightning ?

Un canal Lightning est une connexion directe entre deux nœuds du réseau. Il permet à ces deux nœuds d’échanger des paiements instantanés et à faible coût sans passer par la chaîne principale Bitcoin pour chaque transaction. Les canaux sont la base qui rend le Lightning Network rapide et scalable.

### Lire les informations d’un canal sur 1ML

Sur 1ML, chaque canal dispose d’une page ou d’une fiche descriptive contenant plusieurs données importantes :

 Depuis la page d’un nœud, il est possible d’accéder à la liste de ses canaux. En cliquant sur un canal, 1ML affiche une page dédiée avec plusieurs informations clés.

![capture](assets/fr/12.webp)

![capture](assets/fr/13.webp)

Les principales données visibles sont les suivantes :

- **Nœuds partenaires** : chaque canal relie deux nœuds. 1ML affiche les deux identifiants et leurs alias respectifs.  

![capture](assets/fr/14.webp)

- **Capacité du canal** : il s’agit du montant total de bitcoins verrouillés dans ce canal. Cette capacité représente la limite maximale des paiements pouvant transiter par ce canal.  

![capture](assets/fr/15.webp)

- **Ancienneté du canal** : indique depuis combien de temps le canal est ouvert. Un canal ancien est souvent signe d’une relation stable entre deux nœuds.  

![capture](assets/fr/16.webp)

### Limites de visibilité des canaux

Il est important de comprendre que 1ML ne montre qu’une **partie** du Lightning Network. L’explorateur affiche uniquement les **canaux publics**, c’est-à-dire ceux qui ont été annoncés sur le réseau. Les canaux privés, souvent utilisés pour des raisons de confidentialité ou de stratégie, ne sont pas visibles. De plus, 1ML n’indique ni la répartition exacte des fonds de chaque côté d’un canal, ni les paiements effectués, ni la liquidité réellement disponible à un instant précis. Les informations affichées permettent donc d’analyser la **structure générale du réseau**, mais pas son activité financière réelle ni son état de liquidité détaillé.

## Explorer le Lightning Network par localisation

### Nœuds par pays et par région

1ML permet d’explorer le Lightning Network selon une **répartition géographique**. Depuis la page d’accueil ou via les sections dédiées, il est possible d’afficher les nœuds par pays ou par région. Cette fonctionnalité repose sur les informations de localisation déclarées par les opérateurs de nœuds.
Au niveau de la barre de navigation, on y voit le lien **Location**. Sur la page sont regroupés les nœuds par continents, Pays, et villes.

![capture](assets/fr/17.webp)

En sélectionnant un pays, 1ML affiche la liste des nœuds associés, ainsi que des statistiques agrégées comme le nombre de nœuds et la capacité totale visible pour cette zone géographique.

#### Ce que cela révèle sur l’adoption locale

- **Adoption technologique** : Un grand nombre de nœuds dans une région indique que les utilisateurs, entreprises ou services Bitcoin adoptent activement le Lightning Network. Cela montre une maturité technologique et une volonté de profiter des avantages du Lightning (transactions rapides, frais réduits).
- **Écosystème économique** : La présence dense de nœuds peut aussi signaler un tissu économique local autour de Bitcoin : commerçants acceptant le Lightning, startups développant des outils, événements communautaires, etc.
- **Sécurité et résilience** : Une distribution géographique diversifiée renforce la résilience du réseau face aux pannes ou aux restrictions locales. Plus les nœuds sont dispersés, plus le réseau est décentralisé et difficile à censurer.
- **Politiques et régulations** : Certains pays peuvent voir une adoption plus rapide grâce à un cadre réglementaire favorable ou à une communauté proactive. Inversement, dans des zones où les réglementations sont strictes ou hostiles, le nombre de nœuds sera plus faible.

#### Limites des données géographiques

Il faut cependant garder à l’esprit que la géolocalisation des nœuds Lightning a ses limites et biais :

- **Localisation IP approximative** : 1ML utilise généralement l’adresse IP publique des nœuds pour estimer leur localisation. Or, cette méthode peut être faussée par l’usage de VPN, de serveurs cloud (AWS, Google Cloud), ou d’hébergements dans des pays différents du domicile réel du propriétaire du nœud.
- **Nœuds virtuels** : Certains opérateurs hébergent leurs nœuds sur des serveurs distants pour des raisons de fiabilité et disponibilité, ce qui peut donner une fausse idée de la localisation physique.
- **Mobilité des utilisateurs** : Un opérateur de nœud peut changer d’emplacement, déplacer son infrastructure, ou ouvrir plusieurs nœuds dans des régions différentes, ce qui complexifie la lecture des données.
- **Invisibilité des nœuds privés** : Certains nœuds ne publient pas leur adresse IP ou utilisent des méthodes pour masquer leur localisation, ce qui rend impossible leur géolocalisation.

## Cas d’usage concrets de 1ML

### Comprendre la topologie du réseau

1ML permet de visualiser la **structure générale du Lightning Network**. En observant les connexions entre les nœuds, le nombre de canaux et la capacité globale, il est possible de comprendre comment le réseau est organisé, quels nœuds jouent un rôle central et comment les flux de paiement peuvent théoriquement circuler.

Cette compréhension est essentielle pour appréhender le fonctionnement du Lightning Network au-delà d’une simple utilisation de portefeuille.

### Identifier des nœuds importants

Grâce aux classements proposés par 1ML (nœuds les plus connectés, plus grande capacité, ancienneté), il est possible d’identifier les nœuds qui occupent une place importante dans le réseau. Ces nœuds servent souvent de points de passage majeurs pour les paiements Lightning.

![capture](assets/fr/18.webp)

### Vérifier la visibilité publique d’un nœud

Pour un opérateur de nœud, 1ML permet de vérifier si son nœud est bien **annoncé publiquement** sur le Lightning Network. Si un nœud apparaît sur 1ML, cela signifie qu’il est visible et accessible aux autres nœuds pour l’ouverture de canaux publics.
Cela peut être utile pour diagnostiquer des problèmes de visibilité ou de connectivité.

### Observer l’évolution du Lightning Network dans le temps

En comparant les statistiques globales sur différentes périodes, 1ML permet d’observer l’évolution du Lightning Network : augmentation ou diminution du nombre de nœuds, variation de la capacité totale ou changements dans la répartition géographique.
Ces observations offrent une perspective intéressante sur la croissance, la maturité et les tendances du Lightning Network.

## Bonnes pratiques et limites de 1ML

### Données publiques ≠ réalité complète

1ML repose uniquement sur les **données publiques annoncées** sur le Lightning Network. Cela signifie que l’outil ne montre qu’une partie de la réalité. De nombreux canaux peuvent être privés, certains nœuds peuvent ne pas être annoncés, et la liquidité réelle disponible dans les canaux n’est pas visible. Il est donc essentiel d’utiliser 1ML comme un outil d’analyse globale, et non comme une représentation exhaustive du réseau.

### Vie privée et Lightning

Le Lightning Network a été conçu avec une forte attention portée à la **confidentialité des paiements**. Les transactions individuelles ne sont pas visibles sur 1ML, et les soldes exacts des canaux ne sont pas publics. Cette limitation n’est pas un défaut de l’explorateur, mais une caractéristique fondamentale du Lightning Network, visant à protéger la vie privée des utilisateurs.

### Ne pas tirer de conclusions hâtives

Un nœud avec une grande capacité ou de nombreux canaux n’est pas nécessairement plus « fiable » ou « performant » dans tous les cas. De même, une baisse temporaire de la capacité globale du réseau ne signifie pas forcément un problème structurel. Les chiffres doivent toujours être interprétés avec recul et replacés dans leur contexte.

### Complémentarité avec d’autres outils

1ML est un excellent point de départ pour explorer le Lightning Network, mais il gagne à être utilisé en complément d’autres outils : portefeuilles Lightning, interfaces de gestion de nœuds ou autres explorateurs. Cette approche permet d’obtenir une vision plus complète et plus nuancée du réseau.

## L’option de connexion sur 1ML (fonctionnalité avancée)

1ML propose une option de **connexion / création de compte**, visible sur le site, mais celle-ci n’est **pas nécessaire** pour consulter les données du Lightning Network. Toutes les fonctionnalités abordées jusqu’ici dans ce tutoriel sont accessibles **sans compte**.

La connexion s’adresse principalement aux **opérateurs de nœuds Lightning**. Elle permet notamment d’associer un nœud à un compte 1ML afin de gérer certaines informations publiques, comme la présentation du nœud, des liens de contact ou d’autres métadonnées. Cette fonctionnalité vise à améliorer la visibilité et l’identification d’un nœud au sein de l’explorateur.

Il est important de souligner que 1ML n’est **pas un service custodial**. La création d’un compte ne donne aucun accès aux fonds, aux canaux ou aux paiements d’un nœud. Elle ne sert qu’à interagir avec l’explorateur d’un point de vue déclaratif et informatif.

Dans le cadre d’un apprentissage ou d’une découverte du Lightning Network, cette option peut donc être considérée comme **facultative** et réservée à un usage plus avancé.

## Conclusion

1ML est un outil précieux pour observer et comprendre le Lightning Network à partir de ses données publiques. Il permet d’explorer la structure du réseau, d’analyser les nœuds et les canaux, et de suivre l’évolution globale de l’adoption du Lightning Network dans le temps. Sans nécessiter de compte ni de manipulation de fonds, 1ML offre une porte d’entrée accessible à toute personne souhaitant approfondir sa compréhension du fonctionnement de Lightning.
Si vous voulez aller plus loin avec le Lightning Network, je vous recommande le cours complet d'introduction au Lightning Network: 

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
