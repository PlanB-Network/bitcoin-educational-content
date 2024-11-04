---
term: BIP
---

Acronyme de « *Bitcoin Improvement Proposal* ». Une proposition d'amélioration de Bitcoin (BIP) est un processus formel de proposition et de documentation des améliorations et des modifications apportées au protocole Bitcoin et à ses normes. Étant donné que Bitcoin ne possède pas d'entité centrale pour décider des mises à jour, les BIPs permettent à la communauté de suggérer, discuter et mettre en œuvre des améliorations de manière structurée et transparente. Chaque BIP détaille les objectifs de l'amélioration proposée, les justifications, les impacts potentiels sur la compatibilité, ainsi que les avantages et inconvénients. Les BIPs peuvent être rédigés par n'importe quel membre de la communauté, mais doivent être approuvés par d'autres développeurs et les éditeurs qui maintiennent la base de donnée sur le GitHub de Bitcoin Core : Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun et Ruben Somsen. Cependant, il est important de comprendre que le rôle de ces individus dans l'édition des BIPs ne signifie pas pour autant qu'ils contrôlent Bitcoin. Si quelqu'un propose une amélioration qui n'est pas acceptée dans le cadre formel des BIPs, il peut toujours la présenter directement à la communauté Bitcoin, voire créer un fork incluant sa modification. L'avantage du processus des BIPs réside dans sa formalité et sa centralisation, qui facilitent le débat pour éviter la division parmi les utilisateurs de Bitcoin, en cherchant à implémenter des mises à jour de manière consensuelle. À la fin, c'est bien le principe de majorité économique qui détermine les jeux de pouvoir au sein du protocole.

Les BIPs sont classés en trois catégories principales :
* *Standards Track BIPs* : Concernent les modifications qui affectent directement les implémentations de Bitcoin, comme les règles de validation des transactions et des blocs ;
* *Informational BIPs* : Fournissent des informations ou des recommandations sans proposer de changements directs au protocole ;
* *Process BIPs* : Décrivent les changements dans les procédures entourant Bitcoin, comme les processus de gouvernance.

Les BIPs Standards Track et informationnels sont également classifiés par « Layer » ou couche :
* *Consensus Layer* : Les BIPs de cette couche concernent les règles de consensus de Bitcoin, telles que les modifications des règles de validation des blocs ou des transactions. Ces propositions peuvent être soit des soft forks (modifications rétrocompatibles) soit des hard forks (modifications non rétrocompatibles). Par exemple, les BIPs de SegWit et Taproot appartiennent à cette catégorie ;
* *Peer Services* : Cette couche concerne le fonctionnement du réseau de nœuds Bitcoin, c’est-à-dire comment les nœuds se trouvent et communiquent entre eux sur Internet ;
* *API/RPC* : Les BIPs de cette couche concernent les interfaces de programmation applicative (API) et les appels de procédure à distance (RPC) qui permettent aux logiciels Bitcoin d'interagir avec les nœuds ;
* *Applications Layer* : Cette couche concerne les applications construites par-dessus Bitcoin. Les BIPs de cette catégorie vont typiquement traiter les modifications au niveau des standards des portefeuilles Bitcoin.

Le processus de soumission d'un BIP commence par la conceptualisation et la discussion de l'idée sur la liste de diffusion *Bitcoin-dev*. Si l'idée est prometteuse, l'auteur rédige un BIP en respectant un format spécifique et le soumet via une Pull Request sur le dépôt GitHub de Core. Les éditeurs examinent cette proposition pour vérifier si elle respecte bien tous les critères. Le BIP doit être techniquement réalisable, bénéfique pour le protocole, conforme au formatage requis, et en accord avec la philosophie de Bitcoin. Si le BIP répond à ces conditions, il est officiellement intégré au dépôt GitHub des BIPs. Il se verra ensuite attribuer un numéro. Ce numéro est généralement décidé par l'éditeur, souvent Luke Dashjr, et est attribué de manière logique : les BIPs traitant de sujets similaires reçoivent souvent des numéros consécutifs.

Les BIPs passent ensuite par différents statuts au cours de leur cycle de vie. Le statut actuel est précisé dans l’entête de chaque BIP :
* Brouillon (*Draft*) : La proposition est encore en phase de rédaction et de débat ;
* Proposé (*Proposed*) : Le BIP est considéré comme complet et prêt pour être examiné par la communauté ;
* Différé (*Deferred*) : Le BIP est mis en attente pour plus tard par le champion ou par un éditeur ;
* Rejeté (*Rejected*) : Un BIP est classé comme rejeté s'il n'a montré aucune activité pendant 3 ans. Son auteur peut choisir de le reprendre ultérieurement, ce qui lui permettrait de retourner au statut de brouillon ;
* Retiré (*Withdrawn*) : Le BIP a été retiré par son auteur ;
* Final (*Final*) : Le BIP est accepté et largement implémenté sur Bitcoin ;
* Actif (*Active*) : Pour les BIPs de processus uniquement, ce statut est attribué une fois qu'un certain consensus est atteint ;
* Remplacé / Obsolète (*Replaced* / *Obsolete*) : Le BIP n’est plus applicable ou a été remplacé par une proposition plus récente qui le rend inutile.

![](../../dictionnaire/assets/25.webp)

> ► *BIP est l'acronyme anglais pour « Bitcoin Improvement Proposal ». En français, on peut le traduire par « Proposition d'amélioration de Bitcoin ». Toutefois, la plupart des textes français utilisent directement l'acronyme « BIP » comme un nom commun, parfois au féminin, parfois au masculin.*

